"""
Cursor SDK 기반 멀티 모드 에이전트 실행기.

모드:
  plan    기획자(planner)가 사용자에게 인터뷰 → docs/PLAN_NOTES.md 및 REQUIREMENTS.md 갱신
  build   승인된 REQUIREMENTS 기반 구현 (--role: coder | db_architect | tech_writer |
          benchmark_researcher | planner). benchmark/planner 는 승인 없이 docs/ 만 갱신
  status  현재 상태(승인 여부, 최근 작업) 출력

핵심 정책:
- 모든 프롬프트에 .agents/rules.md 와 .agents/agents.yaml 을 강제 주입한다.
- build 모드는 docs/REQUIREMENTS.md 안에 사용자 승인 마커가 있어야만 실행된다.
  마커: HTML 주석 한 줄로 `<!-- approved-by-user: true -->`
- 비밀값은 환경변수/.env 로만 관리하고 로그에 출력하지 않는다.
- 자율 무한 실행을 피하기 위해, build 모드는 1회 실행을 기본으로 한다.
  반복이 필요하면 --loop 옵션으로 명시적으로 켠다.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import subprocess
import sys
import time
import traceback
from pathlib import Path

from dotenv import load_dotenv
from cursor_sdk import (
    Agent,
    AgentOptions,
    CursorAgentError,
    LocalAgentOptions,
)

# UTF-8 강제 (한국어/이모지 깨짐 방지)
try:
    sys.stdout.reconfigure(encoding="utf-8")  # type: ignore[attr-defined]
    sys.stdin.reconfigure(encoding="utf-8")  # type: ignore[attr-defined]
except Exception:
    pass

# readline: 화살표 키, 라인 편집, 히스토리 자동 지원 (prompt_toolkit fallback용)
try:
    import readline  # type: ignore  # noqa: F401
    _READLINE = True
except Exception:
    _READLINE = False

# prompt_toolkit: CJK(한국어) 폭 인식, 멀티라인 편집, 안정적 백스페이스
try:
    from prompt_toolkit import PromptSession  # type: ignore
    from prompt_toolkit.history import FileHistory  # type: ignore
    _PTK = True
except Exception:
    _PTK = False

_PTK_SESSION = None  # 지연 생성

# rich: 기획자 응답을 마크다운으로 렌더링 + 로딩 스피너
try:
    from rich.console import Console
    from rich.markdown import Markdown
    from rich.panel import Panel
    from rich.rule import Rule
    _CONSOLE = Console()
    _RICH = True
except Exception:
    _CONSOLE = None
    _RICH = False

WORKSPACE_ROOT = Path(__file__).resolve().parent.parent
load_dotenv(WORKSPACE_ROOT / ".env")

AGENTS_DIR = WORKSPACE_ROOT / ".agents"
RULES_FILE = AGENTS_DIR / "rules.md"
ROLES_FILE = AGENTS_DIR / "agents.yaml"
BRANCHES_FILE = AGENTS_DIR / "branches.yaml"
DOCS_DIR = WORKSPACE_ROOT / "docs"
PLAN_NOTES_FILE = DOCS_DIR / "PLAN_NOTES.md"
REQUIREMENTS_FILE = DOCS_DIR / "REQUIREMENTS.md"
BENCHMARK_REPORT_FILE = DOCS_DIR / "BENCHMARK_REPORT.md"
COMPETITOR_MATRIX_FILE = DOCS_DIR / "COMPETITOR_MATRIX.md"
USER_STORIES_FILE = DOCS_DIR / "USER_STORIES.md"
FLOWCHART_FILE = DOCS_DIR / "FLOWCHART.md"
API_SPEC_FILE = DOCS_DIR / "API_SPEC.md"
DECISIONS_FILE = WORKSPACE_ROOT / "memory" / "decisions.md"
PLANNER_SESSION_FILE = AGENTS_DIR / ".planner_session.json"
PLANNER_HISTORY_FILE = AGENTS_DIR / ".planner_history"

APPROVAL_MARKER = "<!-- approved-by-user: true -->"

DEFAULT_MODEL_FALLBACK = "composer-2.5"
ENV_MODEL = os.environ.get("AGENT_MODEL")
DEFAULT_INTERVAL = int(os.environ.get("AGENT_INTERVAL_SECONDS", "900"))
DEFAULT_WRITER_INTERVAL = int(os.environ.get("AGENT_WRITER_INTERVAL_SECONDS", "3600"))
DEFAULT_PLANNING_INTERVAL = int(os.environ.get("AGENT_PLANNING_INTERVAL_SECONDS", "10800"))

BUILD_ROLES = frozenset({"coder", "db_architect", "tech_writer", "tester"})
AUTO_ROLES = frozenset({"benchmark_researcher", "planner"})
ALL_BUILD_ROLES = BUILD_ROLES | AUTO_ROLES
ROLE_LABELS = {
    "coder": "코더",
    "db_architect": "DB 설계자",
    "tech_writer": "기술 문서",
    "tester": "QA(이관)",
    "benchmark_researcher": "벤치마크 분석",
    "planner": "기획자(자동)",
}
ROLE_QUESTION_MARKERS = {
    "coder": "코더 질문",
    "db_architect": "DB 설계 질문",
    "tech_writer": "문서 작성 질문",
    "tester": "QA 이관 질문",
    "benchmark_researcher": "벤치마크 질문",
    "planner": "기획 질문",
}

# 일시적인 네트워크/브리지 오류에 대한 재시도 정책
RETRY_MAX = max(0, int(os.environ.get("AGENT_RETRY_MAX", "3")))
RETRY_BASE_DELAY = max(0.1, float(os.environ.get("AGENT_RETRY_BASE_DELAY", "1.5")))


def _load_branches_yaml() -> dict | None:
    if not BRANCHES_FILE.exists():
        return None
    try:
        import yaml  # type: ignore

        data = yaml.safe_load(BRANCHES_FILE.read_text(encoding="utf-8"))
        return data if isinstance(data, dict) else None
    except Exception:
        return None


def _git_repo_ready() -> bool:
    try:
        subprocess.run(
            ["git", "rev-parse", "--git-dir"],
            cwd=WORKSPACE_ROOT,
            capture_output=True,
            check=True,
        )
        return True
    except Exception:
        return False


def _git_current_branch() -> str | None:
    if not _git_repo_ready():
        return None
    try:
        r = subprocess.run(
            ["git", "branch", "--show-current"],
            cwd=WORKSPACE_ROOT,
            capture_output=True,
            text=True,
            check=True,
        )
        branch = (r.stdout or "").strip()
        return branch or None
    except Exception:
        return None


def _git_checkout(branch: str) -> None:
    subprocess.run(
        ["git", "checkout", branch],
        cwd=WORKSPACE_ROOT,
        check=True,
    )


def branch_for_stream(stream: str, phase: str) -> str:
    data = _load_branches_yaml() or {}
    streams = data.get("streams") or {}
    cfg = streams.get(stream) or {}
    name = cfg.get(phase)
    if isinstance(name, str) and name.strip():
        return name.strip()
    return f"{stream}/{phase}"


def resolve_stream(args: argparse.Namespace, target: Path) -> str:
    stream = getattr(args, "stream", None)
    if stream in ("backend", "frontend"):
        return stream
    target_str = target.as_posix()
    if "frontend" in target_str:
        return "frontend"
    return "backend"


def required_branch_for_role(role: str, stream: str) -> str | None:
    if role == "coder":
        return branch_for_stream(stream, "develop")
    if role == "tester":
        return branch_for_stream(stream, "migration")
    return None


def ensure_role_branch(role: str, stream: str) -> str | None:
    """역할·스트림에 맞는 git 브랜치로 checkout. 저장소 없으면 경고만."""

    branch = required_branch_for_role(role, stream)
    if branch is None:
        return None
    if not _git_repo_ready():
        print(
            "[warn] git 저장소 없음 — 브랜치 정책 미적용. "
            "./scripts/git_branch_setup.sh 실행 권장.",
            file=sys.stderr,
        )
        return branch
    current = _git_current_branch()
    if current == branch:
        print(f"[git] branch={branch} (ok)")
        return branch
    print(f"[git] checkout {branch} (was: {current or 'unknown'})")
    try:
        _git_checkout(branch)
    except subprocess.CalledProcessError as err:
        print(
            f"[fatal] git checkout 실패: {branch}. "
            "./scripts/git_branch_setup.sh 로 브랜치를 생성하세요.",
            file=sys.stderr,
        )
        raise SystemExit(2) from err
    return branch


def transfer_dir_for_stream(stream: str) -> Path:
    return WORKSPACE_ROOT / "transfer" / stream


def _load_agents_yaml() -> dict | None:
    """`.agents/agents.yaml` 을 파싱한다. yaml 미설치/파싱 실패 시 None."""

    if not ROLES_FILE.exists():
        return None
    try:
        import yaml  # type: ignore

        data = yaml.safe_load(ROLES_FILE.read_text(encoding="utf-8"))
        return data if isinstance(data, dict) else None
    except Exception:
        return None


def resolve_model_chain(role: str | None = None) -> list[str]:
    """모델 우선순위 체인을 반환한다.

    1) 환경변수 AGENT_MODEL 이 있으면 그 값만 단일 항목으로 (폴백 없음)
    2) agents[<role>].model -> agents[<role>].fallback_models[*] -> models.default
       -> DEFAULT_MODEL_FALLBACK
    """

    if ENV_MODEL:
        return [ENV_MODEL]

    data = _load_agents_yaml() or {}
    chain: list[str] = []

    if role:
        for a in data.get("agents", []) or []:
            if isinstance(a, dict) and a.get("name") == role:
                m = a.get("model")
                if isinstance(m, str) and m.strip():
                    chain.append(m.strip())
                for f in a.get("fallback_models") or []:
                    if isinstance(f, str) and f.strip():
                        chain.append(f.strip())

    default = (data.get("models") or {}).get("default")
    if isinstance(default, str) and default.strip():
        chain.append(default.strip())

    chain.append(DEFAULT_MODEL_FALLBACK)

    # 순서 보존 dedupe
    seen: set[str] = set()
    out: list[str] = []
    for m in chain:
        if m not in seen:
            seen.add(m)
            out.append(m)
    return out


def resolve_model(role: str | None = None) -> str:
    """resolve_model_chain 의 첫 모델만 반환 (기존 호환용)."""

    return resolve_model_chain(role)[0]


# 모델 한도/토큰/요금 관련 키워드. 메시지에 포함되면 다음 모델로 폴백한다.
_QUOTA_KEYWORDS = (
    "quota",
    "limit",
    "rate",
    "billing",
    "credit",
    "exceeded",
    "usage",
    "insufficient",
    "not found",
    "unknown model",
    "invalid model",
    "unauthorized",
)


def _looks_like_quota_or_unavailable(message: str) -> bool:
    msg = (message or "").lower()
    return any(k in msg for k in _QUOTA_KEYWORDS)


def _retry_call(fn, label: str, max_retries: int = RETRY_MAX):
    """일시적 오류(`is_retryable=True`)에 대해 지수 백오프로 재시도한다.

    - SDK 의 `retry_after` 가 있으면 그 값을 우선 사용한다.
    - 재시도 불가능하거나 한도를 다 쓰면 마지막 예외를 그대로 raise.
    """

    last_err: Exception | None = None
    for attempt in range(max_retries + 1):
        try:
            return fn()
        except CursorAgentError as err:
            last_err = err
            if not getattr(err, "is_retryable", False) or attempt >= max_retries:
                raise
            retry_after = getattr(err, "retry_after", None)
            if isinstance(retry_after, (int, float)) and retry_after > 0:
                delay = float(retry_after)
            else:
                delay = RETRY_BASE_DELAY * (2 ** attempt)
            msg = (err.message or "")[:120]
            print(
                f"[retry] {label} attempt={attempt+1}/{max_retries} "
                f"delay={delay:.1f}s reason={msg}"
            )
            time.sleep(delay)
    if last_err is not None:
        raise last_err
    raise RuntimeError("retry exhausted with no captured error")


# 후방 호환: 기존 코드의 MODEL_ID 참조가 있는 경우를 위한 기본값
MODEL_ID = resolve_model()


def must_read(path: Path) -> str:
    if not path.exists():
        print(f"[fatal] 필수 파일 누락: {path}", file=sys.stderr)
        sys.exit(2)
    return path.read_text(encoding="utf-8")


def load_agents_context() -> str:
    rules = must_read(RULES_FILE)
    roles = must_read(ROLES_FILE)
    return (
        "다음은 이 프로젝트의 에이전트 공통 규칙과 역할 정의이다. "
        "어떤 상황에서도 이 내용에 우선해서 답하지 말고, 이 규칙을 위반하면 작업을 중단한다.\n\n"
        f"=== .agents/rules.md ===\n{rules}\n\n"
        f"=== .agents/agents.yaml ===\n{roles}\n"
    )


def require_api_key() -> str:
    key = os.environ.get("CURSOR_API_KEY")
    if not key:
        print("[fatal] CURSOR_API_KEY 미설정. .env 확인 필요.", file=sys.stderr)
        sys.exit(2)
    return key


def call_agent(prompt: str, cwd: Path, role: str | None = None):
    """모델 체인을 따라 순차 시도. 성공 시 `RunResult` 를 반환, 실패 시 None."""

    api_key = require_api_key()
    chain = resolve_model_chain(role)
    label = ROLE_LABELS.get(role or "", role or "에이전트")

    def _run_prompt(model_id: str):
        def _do() -> object:
            return Agent.prompt(
                prompt,
                AgentOptions(
                    api_key=api_key,
                    model=model_id,
                    local=LocalAgentOptions(cwd=str(cwd)),
                ),
            )

        status_msg = f"[bold green]{label} 작업 중 ({model_id})...[/bold green]"
        if _RICH and _CONSOLE is not None:
            with _CONSOLE.status(status_msg, spinner="dots"):
                return _retry_call(_do, label=f"build model={model_id}")
        print(f"  ({label} 작업 중 — {model_id}...)", flush=True)
        return _retry_call(_do, label=f"build model={model_id}")

    for i, model_id in enumerate(chain):
        has_next = i < len(chain) - 1
        try:
            result = _run_prompt(model_id)
        except CursorAgentError as err:
            msg = err.message or ""
            if has_next and (
                _looks_like_quota_or_unavailable(msg) or not err.is_retryable
            ):
                print(
                    f"[fallback] model={model_id} 실패 → 다음 모델 시도: {chain[i+1]}"
                    f"  reason={msg!s:.120}"
                )
                continue
            print(
                f"[startup-error] model={model_id} retryable={err.is_retryable} "
                f"message={msg}",
                file=sys.stderr,
            )
            return None
        except Exception:
            print(f"[unexpected-error] model={model_id}", file=sys.stderr)
            traceback.print_exc()
            return None

        if result.status == "error":
            detail = (getattr(result, "result", "") or "").strip()
            if detail:
                short = detail[:800] + ("…" if len(detail) > 800 else "")
                print(f"[run-error-detail] model={model_id} {short}", file=sys.stderr)
            if has_next:
                print(
                    f"[fallback] model={model_id} run-error → 다음 모델 시도: {chain[i+1]}"
                )
                continue
            print(f"[run-error] id={result.id} model={model_id}", file=sys.stderr)
            return result

        print(
            f"[ok] model={model_id} status={result.status} "
            f"run={result.id} duration={result.duration_ms}ms"
        )
        return result
    return None


def _sprint_progress_hint(target: Path) -> str:
    """src/backend·frontend 상태로 §7 스프린트 중 다음 작업을 추정."""

    backend = WORKSPACE_ROOT / "src/backend"
    frontend = WORKSPACE_ROOT / "src/frontend"
    has_java = any(
        (backend / name).exists()
        for name in ("pom.xml", "build.gradle", "build.gradle.kts")
    )
    has_react = (frontend / "package.json").exists()
    has_auth = (backend / "src/main/java").exists() if has_java else False

    if not has_java and not has_react:
        return (
            "현재 진행: **0/7 — §7-1 프로젝트 초기화 미착수**\n"
            "→ 지금 즉시 수행: Spring Boot 3.x 백엔드(`src/backend`: pom.xml, "
            "`src/main/java/...`, application.yml, Flyway/Liquibase 초기 마이그레이션), "
            "React(Vite) SPA(`src/frontend`: package.json, vite.config), "
            "PostgreSQL 연결·멀티테넌트(organization/branch) 기본 스키마.\n"
            "→ 사용자에게 질문하지 말고 파일을 생성할 것."
        )
    if has_java and not has_react:
        return (
            "현재 진행: **백엔드 스켈레톤만 있음 — React 프론트 미착수**\n"
            "→ `src/frontend` 에 Vite+React SPA 초기화 및 API 클라이언트 골격 생성."
        )
    if not has_auth:
        return (
            "현재 진행: **1/7 프로젝트 초기화 부분 완료 — RBAC 미착수**\n"
            "→ §7-2: JWT 인증, 7역할 RBAC, Organization/Branch 멀티테넌트 API 골격."
        )
    return (
        "현재 진행: **초기화·인증 골격 이후**\n"
        "→ `docs/REQUIREMENTS.md` §7 순서표·§7 완료 기준표를 읽고, "
        "아직 산출물이 없는 **다음 번호** 작업을 즉시 구현."
    )


def _build_coder_prompt(target: Path, task: str | None = None, stream: str = "backend") -> str:
    """build 모드용 코더 프롬프트. 거대한 REQUIREMENTS 전문 인라인 대신 워크스페이스 파일 참조."""

    rules = must_read(RULES_FILE)
    progress = _sprint_progress_hint(target)
    task_block = (
        f"## 이번 build 명시 작업\n{task.strip()}\n"
        if task and task.strip()
        else progress
    )
    try:
        target_rel = target.relative_to(WORKSPACE_ROOT)
    except ValueError:
        target_rel = target
    develop_branch = branch_for_stream(stream, "develop")

    return (
        f"=== .agents/rules.md ===\n{rules}\n\n"
        "지금 너의 역할은 `.agents/agents.yaml` 의 `coder` 이다.\n"
        "역할 상세·출력 경로는 agents.yaml 의 coder 섹션을 워크스페이스에서 읽어라.\n\n"
        "## 0. 브랜치·범위 (CRITICAL)\n"
        f"- **현재 스트림**: `{stream}` | **작업 브랜치**: `{develop_branch}` (개발 전용)\n"
        "- **개발(develop) 브랜치에서만** `src/backend` 또는 `src/frontend` 코드를 작성한다.\n"
        "- `transfer/`, migration·operation 브랜치, `docs/TEST_REPORT.md` 는 **수정 금지** "
        "(QA/tester 이관 전담).\n"
        "- `.agents/branches.yaml` 브랜치 정책을 따른다.\n\n"
        "## 1. 스택 강제 (최우선)\n"
        "- **반드시** `docs/REQUIREMENTS.md` §1-1 기술 스택 표를 읽고 그대로 따른다.\n"
        "  (Java Spring Boot 3.x / React Vite SPA / PostgreSQL / JWT+RBAC / SaaS 멀티테넌트)\n"
        "- Python/FastAPI 등 다른 스택 코드는 **작성 금지**. `src/backend/.venv` 등 레거시는 무시.\n"
        "- agents.yaml 에 Python/FastAPI 가 적혀 있어도 REQUIREMENTS §1-1 이 우선.\n\n"
        "## 2. 자율 실행 (필수 — 위반 시 실패)\n"
        "- 사용자에게 \"무엇부터 할까요?\" \"어떤 작업부터?\" 같은 **질문 금지**.\n"
        "- 이번 호출에서 **반드시 파일을 생성·수정**한다. 텍스트만 돌려주면 실패.\n"
        "- 불확실하면 `docs/PLAN_NOTES.md` 의 `### 코더 질문` 에 기록 후 중단.\n"
        "- 비밀값 하드코딩 금지 (.agents/rules.md §3).\n\n"
        f"{task_block}\n\n"
        "## 3. 읽어야 할 문서 (워크스페이스에서 직접 열기)\n"
        "- docs/REQUIREMENTS.md (§1-1 스택, §7 스프린트, Must 기능)\n"
        "- docs/API_SPEC.md\n"
        "- docs/USER_STORIES.md\n"
        "- docs/FLOWCHART.md\n\n"
        "## 4. 코드 작성 위치\n"
        f"- 백엔드: `src/backend/` (Java Spring Boot) — stream=backend\n"
        "- 프론트: `src/frontend/` (React Vite) — stream=frontend\n"
        f"- 이번 `--target` / `--stream` 강조: `{target_rel}` / `{stream}`\n\n"
        "## 5. 최종 응답 포맷\n"
        "  ## 코더 작업 요약\n"
        f"  - 브랜치: {develop_branch}\n"
        "  - 사용한 스택 (REQUIREMENTS §1-1 일치 여부)\n"
        "  - 생성/수정한 파일 목록\n"
        "  - 핵심 결정\n"
        "  - 다음 build 에서 이어갈 작업 (§7 기준)\n"
    )


def _db_progress_hint() -> str:
    erd = DOCS_DIR / "ERD.md"
    retention = DOCS_DIR / "DATA_RETENTION_POLICY.md"
    backend = WORKSPACE_ROOT / "src/backend"
    migrations = list(backend.rglob("db/migration/*.sql")) if backend.exists() else []
    migrations += list(backend.rglob("db/migrations/*.sql")) if backend.exists() else []
    flyway = list(backend.rglob("**/db/migration/V*.sql")) if backend.exists() else []

    if not erd.exists():
        return (
            "현재 진행: **ERD 미작성**\n"
            "→ `docs/ERD.md` 작성: SaaS 멀티테넌트(organization/branch), "
            "7역할 RBAC, core_entities(이용자·출석·건강·청구·audit_logs 등) 관계도.\n"
            "→ REQUIREMENTS §3·API_SPEC 과 정합성 유지. 사용자 질문 금지, 파일 생성 필수."
        )
    if not flyway and not migrations:
        return (
            "현재 진행: **ERD 있음 — Flyway/Liquibase 마이그레이션 미작성**\n"
            "→ `src/backend/src/main/resources/db/migration/` 아래 V1__*.sql DDL 작성.\n"
            "→ 멀티테넌트 organization_id/branch_id, PII 암호화 컬럼, audit_logs 포함."
        )
    if not retention.exists():
        return (
            "현재 진행: **마이그레이션 있음 — 데이터 보존 정책 미작성**\n"
            "→ `docs/DATA_RETENTION_POLICY.md` 작성 (PII·의료 데이터 보관·삭제 정책)."
        )
    return (
        "현재 진행: **기본 DB 산출물 있음**\n"
        "→ ERD·마이그레이션·API_SPEC 대조 후 누락 테이블/인덱스/제약 추가.\n"
        "→ 청구(billing)·출석(attendance) 등 Must 엔티티 커버리지 점검."
    )


def _tech_writer_progress_hint() -> str:
    outputs = {
        "USER_MANUAL.md": "역할별 사용자 매뉴얼 (센터장·사회복지사·보호자)",
        "ADMIN_GUIDE.md": "시스템 관리자·sysadmin 가이드",
        "DEPLOYMENT_GUIDE.md": "Spring Boot + React + PostgreSQL 배포 가이드",
        "CHANGELOG.md": "버전별 변경 이력",
        "FAQ.md": "자주 묻는 질문",
    }
    missing = [name for name in outputs if not (DOCS_DIR / name).exists()]
    if missing:
        first = missing[0]
        return (
            f"현재 진행: **{len(missing)}개 문서 미작성**\n"
            f"→ 지금 즉시 `docs/{first}` 초안 작성 ({outputs[first]}).\n"
            "→ `src/` 구현·`docs/REQUIREMENTS.md`·`docs/API_SPEC.md` 를 근거로 작성.\n"
            "→ 코드 변경 금지, docs/ 만 수정. 사용자 질문 금지."
        )
    return (
        "현재 진행: **기본 문서 세트 있음**\n"
        "→ 최근 `src/`·`CHANGELOG.md` 변경 반영, FAQ/매뉴얼 보강.\n"
        "→ 아직 문서화 안 된 Must 기능(API·화면) 우선."
    )


def _build_db_architect_prompt(task: str | None = None) -> str:
    rules = must_read(RULES_FILE)
    progress = _db_progress_hint()
    task_block = (
        f"## 이번 build 명시 작업\n{task.strip()}\n"
        if task and task.strip()
        else progress
    )
    return (
        f"=== .agents/rules.md ===\n{rules}\n\n"
        "지금 너의 역할은 `.agents/agents.yaml` 의 `db_architect` 이다.\n"
        "agents.yaml 의 db_architect 섹션(출력물·core_entities)을 워크스페이스에서 읽어라.\n\n"
        "## 0. 스택 (REQUIREMENTS §1-1 우선)\n"
        "- DB: **PostgreSQL**. 백엔드: **Java Spring Boot 3.x**.\n"
        "- 마이그레이션: Flyway (`src/backend/src/main/resources/db/migration/V*.sql`).\n"
        "- agents.yaml 의 `src/db/` 경로는 레거시 — Java 백엔드 Flyway 경로 사용.\n\n"
        "## 1. 자율 실행 (필수)\n"
        "- 사용자에게 질문하지 말고 **docs/ 또는 migration SQL 파일**을 생성·수정.\n"
        "- 애플리케이션 Java 코드는 작성하지 않는다 (coder 역할).\n"
        "- 불확실하면 `docs/PLAN_NOTES.md` 의 `### DB 설계 질문` 에 기록 후 중단.\n\n"
        f"{task_block}\n\n"
        "## 2. 읽을 문서\n"
        "- docs/REQUIREMENTS.md, docs/API_SPEC.md, docs/USER_STORIES.md\n"
        "- docs/ERD.md (있으면 갱신)\n\n"
        "## 3. 출력 위치\n"
        "- docs/ERD.md, docs/DATA_RETENTION_POLICY.md\n"
        "- src/backend/src/main/resources/db/migration/\n\n"
        "## 4. 최종 응답 포맷\n"
        "  ## DB 설계 작업 요약\n"
        "  - 생성/수정한 파일\n"
        "  - 핵심 테이블·관계 결정\n"
        "  - coder 에게 전달할 구현 메모\n"
    )


def _build_tech_writer_prompt(task: str | None = None) -> str:
    rules = must_read(RULES_FILE)
    progress = _tech_writer_progress_hint()
    task_block = (
        f"## 이번 build 명시 작업\n{task.strip()}\n"
        if task and task.strip()
        else progress
    )
    return (
        f"=== .agents/rules.md ===\n{rules}\n\n"
        "지금 너의 역할은 `.agents/agents.yaml` 의 `tech_writer` 이다.\n\n"
        "## 0. 범위\n"
        "- **docs/ 아래 문서만** 작성·갱신. src/ 코드 변경 금지.\n"
        "- 스택은 REQUIREMENTS §1-1 (Java Spring Boot + React + PostgreSQL) 기준으로 서술.\n\n"
        "## 1. 자율 실행 (필수)\n"
        "- 사용자 질문 금지. 이번 호출에서 docs/ 파일을 반드시 생성·수정.\n"
        "- 불확실하면 `docs/PLAN_NOTES.md` 의 `### 문서 작성 질문` 에 기록 후 중단.\n\n"
        f"{task_block}\n\n"
        "## 2. 읽을 자료\n"
        "- docs/REQUIREMENTS.md, docs/API_SPEC.md, docs/FLOWCHART.md\n"
        "- src/backend/, src/frontend/ (구현 상태 파악용, 수정 금지)\n\n"
        "## 3. 출력 위치\n"
        "- docs/USER_MANUAL.md, docs/ADMIN_GUIDE.md, docs/DEPLOYMENT_GUIDE.md\n"
        "- docs/CHANGELOG.md, docs/FAQ.md\n\n"
        "## 4. 최종 응답 포맷\n"
        "  ## 문서 작업 요약\n"
        "  - 생성/수정한 문서\n"
        "  - 대상 독자·범위\n"
        "  - 다음 문서화 우선순위\n"
    )


def _benchmark_progress_hint() -> str:
    missing = [
        name
        for name, path in (
            ("BENCHMARK_REPORT.md", BENCHMARK_REPORT_FILE),
            ("COMPETITOR_MATRIX.md", COMPETITOR_MATRIX_FILE),
        )
        if not path.exists()
    ]
    if missing:
        first = missing[0]
        return (
            f"현재 진행: **{len(missing)}개 벤치마크 산출물 미작성**\n"
            f"→ 지금 즉시 `docs/{first}` 초안 작성.\n"
            "→ REQUIREMENTS §1-5, PLAN_NOTES 의 경쟁사 목록(케어포·이지케어·엔젤시스템·롱텀)을 우선 조사.\n"
            "→ 각 서비스의 **제공 항목·기능·모듈·역할별 화면·청구·출석·보호자 포털**을 표로 정리.\n"
            "→ 출처 URL·조사일 기록. 사용자 질문 금지, docs/·memory/ 파일 생성 필수."
        )
    return (
        "현재 진행: **기본 벤치마크 산출물 있음**\n"
        "→ 최신 공식 사이트·매뉴얼·공지를 재조사해 BENCHMARK_REPORT·COMPETITOR_MATRIX 갱신.\n"
        "→ ogada REQUIREMENTS·USER_STORIES 대비 갭·차별화·MVP 우선순위 제안 추가.\n"
        "→ 새 인사이트는 memory/decisions.md 최상단에 기록."
    )


def _planner_auto_progress_hint() -> str:
    benchmark_ready = BENCHMARK_REPORT_FILE.exists() and COMPETITOR_MATRIX_FILE.exists()
    benchmark_note = (
        "벤치마크 산출물 있음 — 최신 BENCHMARK_REPORT·COMPETITOR_MATRIX를 반영해 기획 갱신."
        if benchmark_ready
        else "벤치마크 산출물 없음 — REQUIREMENTS §1-5 기준으로 기획 유지·보강."
    )
    return (
        f"현재 진행: **자동 기획 동기화**\n"
        f"→ {benchmark_note}\n"
        "→ docs/REQUIREMENTS.md, docs/USER_STORIES.md, docs/PLAN_NOTES.md, "
        "docs/FLOWCHART.md, docs/API_SPEC.md 중 **벤치마크·갭 분석에 따라 수정이 필요한 문서**를 갱신.\n"
        "→ 미확정 사항은 PLAN_NOTES `### 추가 질문`에 누적.\n"
        "→ 사용자 승인 마커(`<!-- approved-by-user: true -->`) 추가 금지.\n"
        "→ src/ 코드 작성 금지. 사용자 질문 금지."
    )


def _build_benchmark_researcher_prompt(task: str | None = None) -> str:
    rules = must_read(RULES_FILE)
    progress = _benchmark_progress_hint()
    task_block = (
        f"## 이번 build 명시 작업\n{task.strip()}\n"
        if task and task.strip()
        else progress
    )
    return (
        f"=== .agents/rules.md ===\n{rules}\n\n"
        "지금 너의 역할은 `.agents/agents.yaml` 의 `benchmark_researcher` 이다.\n"
        "agents.yaml 의 benchmark_researcher 섹션(research_focus·outputs)을 읽어라.\n\n"
        "## 0. 범위\n"
        "- **docs/ 및 memory/decisions.md 만** 작성·갱신. src/ 코드 변경 금지.\n"
        "- 주간보호·요양기관 관리 SaaS/ERP 경쟁사의 **서비스 제공 항목·기능·모듈**을 조사·정리.\n"
        "- 웹 검색·공식 사이트·매뉴얼·교육 공지 등 **공개 자료**를 근거로 한다.\n\n"
        "## 1. 자율 실행 (필수)\n"
        "- 사용자에게 질문하지 말고 **반드시 파일을 생성·수정**한다.\n"
        "- 불확실한 내용은 「가정」으로 표시하고 출처·조사일을 남긴다.\n"
        "- 불명확해 작업을 중단해야 하면 `docs/PLAN_NOTES.md` 의 "
        "`### 벤치마크 질문` 에 기록 후 중단.\n\n"
        f"{task_block}\n\n"
        "## 2. 읽을 문서\n"
        "- docs/REQUIREMENTS.md (§1-5 벤치마킹, MVP 범위)\n"
        "- docs/PLAN_NOTES.md\n"
        "- docs/BENCHMARK_REPORT.md, docs/COMPETITOR_MATRIX.md (있으면 갱신)\n\n"
        "## 3. 출력 위치\n"
        "- docs/BENCHMARK_REPORT.md — 경쟁사별 상세 분석(기능·UX·청구·출석·가격 등)\n"
        "- docs/COMPETITOR_MATRIX.md — 기능·서비스 항목 비교 표(ogada vs 경쟁사)\n"
        "- memory/decisions.md — 벤치마킹에서 도출된 기획 결정(최상단 추가)\n\n"
        "## 4. COMPETITOR_MATRIX 권장 구조\n"
        "- 행: 기능/서비스 항목 (이용자관리, 출석, 건강기록, 청구, 대시보드, 보호자포털, 다지점, QR 등)\n"
        "- 열: ogada, 케어포, 이지케어, 엔젤시스템, 롱텀(공단)\n"
        "- 셀: 지원 여부(✅/❌/△), 비고, 근거 URL\n\n"
        "## 5. 최종 응답 포맷\n"
        "  ## 벤치마크 작업 요약\n"
        "  - 조사·갱신한 경쟁사\n"
        "  - 생성/수정한 파일\n"
        "  - ogada 기획에 반영할 핵심 제안 (planner 가 읽을 수 있게)\n"
        "  - 다음 조사 우선순위\n"
    )


def _build_planner_auto_prompt(task: str | None = None) -> str:
    rules = must_read(RULES_FILE)
    progress = _planner_auto_progress_hint()
    task_block = (
        f"## 이번 build 명시 작업\n{task.strip()}\n"
        if task and task.strip()
        else progress
    )
    return (
        f"=== .agents/rules.md ===\n{rules}\n\n"
        "지금 너의 역할은 `.agents/agents.yaml` 의 `planner` 이다.\n"
        "이번 호출은 **자동 기획 동기화** — 사용자 대화 없이 벤치마크 결과를 반영한다.\n\n"
        "## 0. 범위\n"
        "- **docs/ 기획 문서만** 작성·갱신. src/ 코드 변경 금지.\n"
        "- `docs/BENCHMARK_REPORT.md`, `docs/COMPETITOR_MATRIX.md`, "
        "`memory/decisions.md` 를 **먼저 읽고** ogada 기획에 반영한다.\n"
        "- REQUIREMENTS §1-1 스택(Java Spring Boot + React + PostgreSQL) 유지.\n\n"
        "## 1. 자율 실행 (필수)\n"
        "- 사용자에게 질문하지 말고 **반드시 docs/ 파일을 생성·수정**한다.\n"
        "- 경쟁사 대비 갭·차별화·MVP 우선순위를 REQUIREMENTS·USER_STORIES에 반영.\n"
        "- 미확정 사항은 `docs/PLAN_NOTES.md` `### 추가 질문`에 누적.\n"
        "- **`<!-- approved-by-user: true -->` 승인 마커는 절대 추가하지 않는다.**\n"
        "- 불명확해 중단해야 하면 `docs/PLAN_NOTES.md` `### 기획 질문`에 기록 후 중단.\n\n"
        f"{task_block}\n\n"
        "## 2. 읽을 문서 (우선순위)\n"
        "1. docs/BENCHMARK_REPORT.md, docs/COMPETITOR_MATRIX.md\n"
        "2. memory/decisions.md\n"
        "3. docs/REQUIREMENTS.md, docs/USER_STORIES.md, docs/PLAN_NOTES.md\n"
        "4. docs/FLOWCHART.md, docs/API_SPEC.md (필요 시만 갱신)\n\n"
        "## 3. 출력·갱신 대상\n"
        "- docs/REQUIREMENTS.md — §1-5 벤치마킹·기능 우선순위·갭 반영\n"
        "- docs/USER_STORIES.md — 경쟁사 대비 누락 스토리 추가\n"
        "- docs/PLAN_NOTES.md — 확인된 결정·추가 질문\n"
        "- docs/FLOWCHART.md, docs/API_SPEC.md — 벤치마크 기반 수정 필요 시\n\n"
        "## 4. 최종 응답 포맷\n"
        "  ## 기획 동기화 요약\n"
        "  - 반영한 벤치마크 인사이트\n"
        "  - 생성/수정한 문서\n"
        "  - 추가·변경한 기능/우선순위\n"
        "  - planner·사용자가 확인할 미확정 질문\n"
    )


def _tester_migration_hint(stream: str) -> str:
    transfer = transfer_dir_for_stream(stream)
    develop = branch_for_stream(stream, "develop")
    migration = branch_for_stream(stream, "migration")
    checklist = transfer / "checklists" / "migration.md"
    manifest = transfer / "manifests" / "latest.yaml"

    if not checklist.exists():
        return (
            f"현재 진행: **{stream} 이관 체크리스트 미작성**\n"
            f"→ `transfer/{stream}/checklists/migration.md` 초안 작성.\n"
            f"→ develop(`{develop}`) 산출물 대비 migration(`{migration}`) 이관 가능 여부 점검.\n"
            f"→ `transfer/{stream}/manifests/latest.yaml` 에 버전·커밋·빌드 정보 기록.\n"
            "→ src/ 코드 **수정 금지** — transfer/·TEST_REPORT·tests/ 만 갱신."
        )
    if not manifest.exists():
        return (
            f"현재 진행: **체크리스트 있음 — 매니페스트 미작성**\n"
            f"→ `transfer/{stream}/manifests/latest.yaml` 작성 "
            f"(develop→migration 이관 대상 커밋, Flyway 버전, npm version 등).\n"
            "→ src/ 수정 금지."
        )
    return (
        f"현재 진행: **{stream} 기본 이관 산출물 있음**\n"
        f"→ develop 최신 대비 migration 체크리스트·매니페스트·packages/ diff 요약 갱신.\n"
        "→ Maven/npm 테스트 실행 결과를 docs/TEST_REPORT.md 에 반영.\n"
        "→ src/ 수정 금지."
    )


def _build_tester_prompt(stream: str = "backend", task: str | None = None) -> str:
    rules = must_read(RULES_FILE)
    progress = _tester_migration_hint(stream)
    task_block = (
        f"## 이번 build 명시 작업\n{task.strip()}\n"
        if task and task.strip()
        else progress
    )
    migration_branch = branch_for_stream(stream, "migration")
    develop_branch = branch_for_stream(stream, "develop")
    transfer = transfer_dir_for_stream(stream)

    return (
        f"=== .agents/rules.md ===\n{rules}\n\n"
        "지금 너의 역할은 `.agents/agents.yaml` 의 `tester`(QA·이관) 이다.\n"
        "agents.yaml tester 섹션과 `.agents/branches.yaml` 을 읽어라.\n\n"
        "## 0. 브랜치·범위 (CRITICAL)\n"
        f"- **현재 스트림**: `{stream}` | **작업 브랜치**: `{migration_branch}` (이관 전용)\n"
        f"- develop 브랜치 `{develop_branch}` 산출물은 **읽기만** — src/ 직접 수정 **금지**.\n"
        f"- **수정 허용**: `transfer/{stream}/`, `docs/TEST_REPORT.md`, `tests/`.\n"
        "- operation 브랜치·develop 브랜치 checkout·src/ 패치는 **금지**.\n\n"
        "## 1. 자율 실행 (필수)\n"
        "- develop → migration **이관** 체크리스트·매니페스트·검증 리포트를 갱신.\n"
        "- Maven(`src/backend`) 또는 npm(`src/frontend`) 테스트 **실행·결과 기록**.\n"
        "- 불확실하면 `docs/PLAN_NOTES.md` `### QA 이관 질문` 에 기록 후 중단.\n\n"
        f"{task_block}\n\n"
        "## 2. 읽을 자료\n"
        "- docs/USER_STORIES.md, docs/API_SPEC.md, docs/REQUIREMENTS.md\n"
        f"- src/{stream}/ (읽기 전용 — develop 산출물)\n"
        f"- {transfer}/ (이관 산출물)\n\n"
        "## 3. 출력 위치\n"
        f"- transfer/{stream}/checklists/migration.md\n"
        f"- transfer/{stream}/manifests/latest.yaml\n"
        f"- transfer/{stream}/packages/ (diff·빌드 메타)\n"
        "- docs/TEST_REPORT.md\n"
        "- tests/ (회귀 테스트 추가·수정 가능)\n\n"
        "## 4. 최종 응답 포맷\n"
        "  ## QA 이관 작업 요약\n"
        f"  - 브랜치: {migration_branch}\n"
        "  - 이관 가능 여부 (PASS/BLOCK)\n"
        "  - 갱신한 transfer/ 파일\n"
        "  - 테스트 실행 결과 요약\n"
        "  - operation 승격 전 잔여 리스크\n"
    )


def _build_role_prompt(
    role: str,
    target: Path,
    task: str | None = None,
    stream: str = "backend",
) -> str:
    if role == "coder":
        return _build_coder_prompt(target, task=task, stream=stream)
    if role == "db_architect":
        return _build_db_architect_prompt(task=task)
    if role == "tech_writer":
        return _build_tech_writer_prompt(task=task)
    if role == "benchmark_researcher":
        return _build_benchmark_researcher_prompt(task=task)
    if role == "planner":
        return _build_planner_auto_prompt(task=task)
    if role == "tester":
        return _build_tester_prompt(stream=stream, task=task)
    raise ValueError(f"unknown role: {role}")


def _role_watched_paths(role: str, target: Path, stream: str = "backend") -> list[Path]:
    paths: set[Path] = set()
    if role == "coder":
        paths.update(_build_watched_paths(target))
        paths.update(_build_watched_paths(WORKSPACE_ROOT / "src/frontend"))
    elif role == "db_architect":
        for name in ("ERD.md", "DATA_RETENTION_POLICY.md"):
            paths.add(DOCS_DIR / name)
        backend = WORKSPACE_ROOT / "src/backend"
        if backend.is_dir():
            for p in backend.rglob("*"):
                if not p.is_file() or _is_ignored_path(p):
                    continue
                rel = p.relative_to(backend).as_posix()
                if any(
                    part in rel
                    for part in (
                        "db/migration",
                        "db/migrations",
                        "flyway",
                        "liquibase",
                        "schema.sql",
                    )
                ):
                    paths.add(p)
    elif role == "tech_writer":
        for name in (
            "USER_MANUAL.md",
            "ADMIN_GUIDE.md",
            "DEPLOYMENT_GUIDE.md",
            "CHANGELOG.md",
            "FAQ.md",
        ):
            paths.add(DOCS_DIR / name)
    elif role == "benchmark_researcher":
        for path in (
            BENCHMARK_REPORT_FILE,
            COMPETITOR_MATRIX_FILE,
            REQUIREMENTS_FILE,
            PLAN_NOTES_FILE,
            DECISIONS_FILE,
        ):
            paths.add(path)
    elif role == "planner":
        for path in (
            BENCHMARK_REPORT_FILE,
            COMPETITOR_MATRIX_FILE,
            REQUIREMENTS_FILE,
            USER_STORIES_FILE,
            PLAN_NOTES_FILE,
            FLOWCHART_FILE,
            API_SPEC_FILE,
            DECISIONS_FILE,
        ):
            paths.add(path)
    elif role == "tester":
        transfer = transfer_dir_for_stream(stream)
        if transfer.is_dir():
            for p in transfer.rglob("*"):
                if p.is_file():
                    paths.add(p)
        paths.add(DOCS_DIR / "TEST_REPORT.md")
        tests_root = WORKSPACE_ROOT / "tests"
        if tests_root.is_dir():
            for p in tests_root.rglob("*"):
                if p.is_file():
                    paths.add(p)
    paths.add(PLAN_NOTES_FILE)
    return sorted(paths)


def approval_present() -> bool:
    if not REQUIREMENTS_FILE.exists():
        return False
    return APPROVAL_MARKER in REQUIREMENTS_FILE.read_text(encoding="utf-8")


def _role_default_interval(role: str) -> int:
    if role == "tech_writer":
        return DEFAULT_WRITER_INTERVAL
    if role in AUTO_ROLES:
        return DEFAULT_PLANNING_INTERVAL
    return DEFAULT_INTERVAL


def save_planner_session(agent_id: str) -> None:
    AGENTS_DIR.mkdir(parents=True, exist_ok=True)
    PLANNER_SESSION_FILE.write_text(
        json.dumps({"agent_id": agent_id}, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def load_planner_session() -> str | None:
    if not PLANNER_SESSION_FILE.exists():
        return None
    try:
        data = json.loads(PLANNER_SESSION_FILE.read_text(encoding="utf-8"))
        agent_id = data.get("agent_id")
        return agent_id if isinstance(agent_id, str) and agent_id else None
    except Exception:
        return None


def planner_system_prompt() -> str:
    context = load_agents_context()
    return (
        f"{context}\n\n"
        "지금 너의 역할은 .agents/agents.yaml 의 `planner` 이다.\n"
        "원칙:\n"
        "- 사용자와 한국어로 대화하며 요구사항을 명확하게 다듬는다.\n"
        "- 매 턴 마지막에 다음에 답해야 할 질문을 1~3개로 명시한다.\n"
        "- 사용자의 답이 들어올 때마다 docs/REQUIREMENTS.md 를 갱신한다.\n"
        f"- 사용자 승인 마커 `{APPROVAL_MARKER}` 는 절대로 추가하지 않는다 "
        "  (승인은 사용자가 직접 추가한다).\n"
        "- 미확정/추가 질문은 docs/PLAN_NOTES.md 의 '### 추가 질문' 섹션에 누적한다.\n"
        "- 벤치마크 산출물(docs/BENCHMARK_REPORT.md, docs/COMPETITOR_MATRIX.md)과 "
        "memory/decisions.md 를 참고해 기획에 반영한다.\n"
        "- 코드는 절대 작성하지 않는다. build 단계는 별도로 사용자 승인 후 실행된다.\n"
        "- 응답은 간결하게(불릿/번호 위주) 작성한다.\n"
    )


def _get_ptk_session():
    """prompt_toolkit 세션을 지연 생성한다. 히스토리 파일은 .agents/.planner_history."""

    global _PTK_SESSION
    if not _PTK:
        return None
    if _PTK_SESSION is None:
        try:
            AGENTS_DIR.mkdir(parents=True, exist_ok=True)
            _PTK_SESSION = PromptSession(history=FileHistory(str(PLANNER_HISTORY_FILE)))
        except Exception:
            _PTK_SESSION = None
    return _PTK_SESSION


def _prompt(prompt_text: str) -> str:
    """prompt_toolkit 우선, 실패 시 readline+input 으로 폴백."""

    session = _get_ptk_session()
    if session is not None:
        return session.prompt(prompt_text)
    return input(prompt_text)


def _file_fingerprint(path: Path) -> str | None:
    """파일 변경 감지를 위한 지문(SHA256). 존재하지 않으면 None."""

    if not path.exists() or not path.is_file():
        return None
    try:
        return hashlib.sha256(path.read_bytes()).hexdigest()
    except Exception:
        return None


def _watched_paths() -> list[Path]:
    """plan 모드에서 매 턴 감시할 경로 목록.

    - docs/ 하위 모든 파일
    - 명시적으로 추가 관찰하는 정적 경로
    """

    paths: set[Path] = set()
    if DOCS_DIR.exists():
        for p in DOCS_DIR.rglob("*"):
            if p.is_file():
                paths.add(p)
    paths.add(REQUIREMENTS_FILE)
    paths.add(PLAN_NOTES_FILE)
    return sorted(paths)


def _build_watched_paths(target: Path) -> list[Path]:
    """build 모드에서 감시할 경로: target 디렉토리 전체 + 핵심 docs."""

    paths: set[Path] = set()
    if target.is_dir():
        for p in target.rglob("*"):
            if p.is_file() and not _is_ignored_path(p):
                paths.add(p)
    elif target.is_file():
        paths.add(target)
    paths.add(PLAN_NOTES_FILE)
    paths.add(REQUIREMENTS_FILE)
    return sorted(paths)


_IGNORE_DIR_NAMES = {
    ".git",
    ".venv",
    "node_modules",
    "__pycache__",
    ".pytest_cache",
    ".mypy_cache",
    "dist",
    "build",
    ".next",
    "target",
}


def _is_ignored_path(p: Path) -> bool:
    parts = set(p.parts)
    return bool(parts & _IGNORE_DIR_NAMES)


def _file_line_count(path: Path) -> int:
    try:
        with path.open("rb") as fh:
            return sum(1 for _ in fh)
    except Exception:
        return 0


def render_build_changes(
    changes: list[tuple[Path, str]],
    before: dict[str, str | None],
) -> None:
    """build 결과로 변경된 파일들을 +/- 라인 통계와 함께 출력."""

    if not changes:
        if _RICH and _CONSOLE is not None:
            _CONSOLE.print(
                Panel(
                    "변경된 파일이 없습니다. coder 가 (1) 요구사항 누락으로 중단했거나 "
                    "(2) 작업할 항목이 없다고 판단했을 수 있습니다.\n"
                    "→ docs/PLAN_NOTES.md '### 코더 질문' 섹션을 확인하세요.",
                    title="변경 없음",
                    border_style="yellow",
                )
            )
        else:
            print("[빈 결과] 변경된 파일이 없습니다.")
            print("  → docs/PLAN_NOTES.md '### 코더 질문' 섹션을 확인하세요.")
        return

    rows: list[str] = []
    total_added = 0
    total_removed = 0
    for path, kind in changes:
        try:
            rel = path.relative_to(WORKSPACE_ROOT)
        except ValueError:
            rel = path
        if kind == "deleted":
            removed = before.get(str(path)) and _file_line_count(path) or 0
            # before snapshot has only hash, we don't know prior line count
            # so just mark as deleted
            rows.append(f"  -  {rel}  (deleted)")
            continue
        cur = _file_line_count(path)
        if kind == "created":
            total_added += cur
            rows.append(f"  +  {rel}  (created, {cur} lines)")
        else:
            # modified: we don't have prior content, so we just show current size
            rows.append(f"  ~  {rel}  (modified, now {cur} lines)")
    body = "\n".join(rows)
    summary = (
        f"파일 {len(changes)}개 변경  /  추가된 라인 합계 ~{total_added}"
    )
    if _RICH and _CONSOLE is not None:
        _CONSOLE.print(
            Panel(
                f"{body}\n\n{summary}",
                title="코더 변경 사항",
                border_style="green",
            )
        )
    else:
        print("[코더 변경 사항]")
        print(body)
        print(summary)
        print()


def snapshot_files(paths: list[Path]) -> dict[str, str | None]:
    return {str(p): _file_fingerprint(p) for p in paths}


def diff_snapshots(
    before: dict[str, str | None],
    after_paths: list[Path],
) -> list[tuple[Path, str]]:
    """변경된 파일 (created/modified/deleted) 목록을 반환한다.

    before 에 없던 경로가 after_paths 에 새로 등장하면 'created' 로 잡힌다.
    """

    after = snapshot_files(after_paths)
    keys = set(before.keys()) | set(after.keys())
    out: list[tuple[Path, str]] = []
    for k in sorted(keys):
        b = before.get(k)
        a = after.get(k)
        if b == a:
            continue
        path = Path(k)
        if b is None and a is not None:
            out.append((path, "created"))
        elif b is not None and a is None:
            out.append((path, "deleted"))
        else:
            out.append((path, "modified"))
    return out


def render_file_changes(changes: list[tuple[Path, str]]) -> None:
    if not changes:
        return
    lines = []
    for path, kind in changes:
        try:
            rel = path.relative_to(WORKSPACE_ROOT)
        except ValueError:
            rel = path
        lines.append(f"- {rel}  ({kind})")
    body = "\n".join(lines)
    if _RICH and _CONSOLE is not None:
        _CONSOLE.print(Panel(body, title="변경된 파일", border_style="yellow"))
    else:
        print("[변경된 파일]")
        print(body)
        print()


def render_agent_output(text: str, title: str = "기획자") -> None:
    """에이전트 응답을 가독성 좋게 출력한다."""

    body = text.strip() if text else "(빈 응답)"
    if _RICH and _CONSOLE is not None:
        _CONSOLE.print(Rule(title, style="cyan"))
        _CONSOLE.print(Panel(Markdown(body), border_style="cyan"))
    else:
        print(f"{title}:")
        print(body)
        print()


def send_and_print(
    agent,
    message: str,
    watch_before: dict[str, str | None] | None = None,
) -> None:
    """에이전트에게 메시지를 보내고 응답을 렌더링한다.

    - 일시적 브리지/네트워크 오류는 자동 재시도한다.
    - watch_before 가 주어지면 전송 전후 docs 변경을 함께 표시한다.
    """

    def _do_send() -> str:
        run = agent.send(message)
        return run.text() or ""

    try:
        if _RICH and _CONSOLE is not None:
            with _CONSOLE.status(
                "[bold cyan]기획자 생각 중...[/bold cyan]",
                spinner="dots",
            ):
                text = _retry_call(_do_send, label="plan send")
        else:
            sys.stdout.write("  (기획자 생각 중...)")
            sys.stdout.flush()
            text = _retry_call(_do_send, label="plan send")
            sys.stdout.write("\r" + " " * 40 + "\r")
            sys.stdout.flush()
    except CursorAgentError as err:
        msg = err.message or ""
        print(
            f"[send-error] retryable={err.is_retryable} message={msg}",
            file=sys.stderr,
        )
        if "internal error" in msg.lower():
            hint = (
                "팁: 세션 컨텍스트가 너무 길어졌거나 모델 백엔드 일시 오류일 수 있습니다.\n"
                "  1) 가용 모델/계정 상태부터 진단:\n"
                "     .venv/bin/python scripts/run_agent.py doctor\n"
                "  2) 짧은 질문으로 다시 시도\n"
                "  3) 새 세션으로 재시작 (대화 기록은 초기화됨):\n"
                "     .venv/bin/python scripts/run_agent.py plan --new\n"
                "  4) 환경변수로 특정 모델만 강제:\n"
                "     AGENT_MODEL=composer-2.5 .venv/bin/python scripts/run_agent.py plan --new"
            )
            if _RICH and _CONSOLE is not None:
                _CONSOLE.print(Panel(hint, title="복구 안내", border_style="red"))
            else:
                print(hint, file=sys.stderr)
        return
    except Exception:
        print("[unexpected-error]", file=sys.stderr)
        traceback.print_exc()
        return

    render_agent_output(text)

    if watch_before is not None:
        changes = diff_snapshots(watch_before, _watched_paths())
        render_file_changes(changes)


def setup_input_history() -> None:
    """readline 히스토리를 파일과 연결한다."""

    if not _READLINE:
        return
    try:
        import readline  # type: ignore

        AGENTS_DIR.mkdir(parents=True, exist_ok=True)
        if PLANNER_HISTORY_FILE.exists():
            try:
                readline.read_history_file(str(PLANNER_HISTORY_FILE))
            except Exception:
                pass
        readline.set_history_length(1000)

        import atexit

        def _save() -> None:
            try:
                readline.write_history_file(str(PLANNER_HISTORY_FILE))
            except Exception:
                pass

        atexit.register(_save)
    except Exception:
        pass


EXIT_TOKEN = "__EXIT__"


def read_user_line(prompt: str = "사용자: ") -> str | None:
    """한 줄 또는 멀티라인 입력을 받는다.

    반환값:
    - 일반 문자열: 사용자 입력 (또는 ":xxx" 슬래시 명령)
    - 빈 문자열: 빈 입력 (호출자가 무시하도록)
    - EXIT_TOKEN: 종료 요청 (:q 등)
    - None: EOF/Ctrl+C
    """

    try:
        line = _prompt(prompt)
    except (EOFError, KeyboardInterrupt):
        print()
        return None
    line = line.strip()
    if line in {":q", ":quit", ":exit", ":bye"}:
        return EXIT_TOKEN
    if line == ":multi":
        return read_multiline()
    if line == ":help":
        print(_HELP_TEXT)
        return ""
    return line


def read_multiline() -> str:
    """:multi … :end 사이의 모든 줄을 하나의 문자열로 합쳐 반환한다."""

    print("[multiline] 한 줄에 :end 만 입력하면 종료됩니다.")
    buf: list[str] = []
    while True:
        try:
            line = _prompt("  | ")
        except (EOFError, KeyboardInterrupt):
            print()
            break
        if line.strip() == ":end":
            break
        buf.append(line)
    text = "\n".join(buf).strip()
    if not text:
        print("[multiline] 입력이 비어 있어 무시합니다.")
    return text


_HELP_TEXT = (
    "명령어:\n"
    "  :q | :quit | :exit | :bye   대화 종료\n"
    "  :multi                      여러 줄 입력 시작 (:end 로 종료)\n"
    "  :show                       현재 docs/REQUIREMENTS.md 출력\n"
    "  :reload                     현재 docs/REQUIREMENTS.md 를 기획자에게 다시 컨텍스트로 전달\n"
    "  :help                       이 도움말 표시\n"
)


def cmd_doctor(_: argparse.Namespace) -> None:
    """가용 모델에 최소 프롬프트를 보내서 어떤 모델/계정이 동작하는지 진단."""

    api_key = require_api_key()
    masked = api_key[:6] + "..." + api_key[-4:]
    candidates = [
        # 서버가 "Available models" 로 공개한 풀 (2026-06). 계정 권한에
        # 따라 일부는 거절될 수 있다. 거절되면 서버가
        # "Cannot use this model. Available models: ..." 를 돌려준다.
        # 기본/저비용
        "default",
        "composer-2.5",
        "composer-2",
        # Claude Opus
        "claude-opus-4-8",
        "claude-opus-4-7",
        "claude-opus-4-6",
        "claude-opus-4-5",
        # Claude Sonnet / Haiku
        "claude-sonnet-4-6",
        "claude-sonnet-4-5",
        "claude-sonnet-4",
        "claude-haiku-4-5",
        # GPT-5 일반
        "gpt-5.5",
        "gpt-5.4",
        "gpt-5.4-mini",
        "gpt-5.4-nano",
        "gpt-5.2",
        "gpt-5.1",
        "gpt-5-mini",
        # GPT 코드 특화
        "gpt-5.3-codex",
        "gpt-5.2-codex",
        "gpt-5.1-codex-max",
        "gpt-5.1-codex-mini",
        # Gemini
        "gemini-3.1-pro",
        "gemini-3-flash",
        "gemini-3.5-flash",
        "gemini-2.5-flash",
        # Grok
        "grok-build-0.1",
        "grok-4.3",
    ]
    print(f"[doctor] API key={masked} (len={len(api_key)})")
    print("[doctor] 최소 프롬프트로 모델 가용성 점검")
    results: list[tuple[str, str, object, object, str]] = []
    # (model, kind, status, code, message)
    for m in candidates:
        t0 = time.time()
        try:
            result = Agent.prompt(
                "ping",
                AgentOptions(
                    api_key=api_key,
                    model=m,
                    local=LocalAgentOptions(cwd=str(WORKSPACE_ROOT)),
                ),
            )
            dt = time.time() - t0
            status = result.status
            print(f"  {m:32s}  OK     status={status:<10s} time={dt:.1f}s")
            results.append((m, "OK", status, None, ""))
        except CursorAgentError as err:
            dt = time.time() - t0
            msg = err.message or ""
            short = msg[:140]
            status = getattr(err, "status_code", None) or getattr(err, "status", None)
            code = getattr(err, "code", None)
            req_id = getattr(err, "request_id", None)
            print(
                f"  {m:32s}  FAIL   status={status} code={code} "
                f"req={req_id} retryable={err.is_retryable} "
                f"time={dt:.1f}s msg={short}"
            )
            results.append((m, "FAIL", status, code, msg))
        except Exception as e:
            dt = time.time() - t0
            print(f"  {m:32s}  CRASH  {type(e).__name__}: {e} time={dt:.1f}s")
            results.append((m, "CRASH", None, type(e).__name__, str(e)))

    import re

    server_allowed: list[str] | None = None
    slug_re = re.compile(r"^[A-Za-z0-9][A-Za-z0-9.\-]*$")
    for _m, kind, _status, _code, msg in results:
        if kind != "FAIL" or not msg:
            continue
        mobj = re.search(r"Available models:\s*(.+?)(?:\n|$)", msg, re.S)
        if not mobj:
            continue
        raw = mobj.group(1).strip()
        if raw.endswith("."):
            raw = raw[:-1]
        parts = [p.strip().rstrip(",") for p in raw.split(",")]
        parts = [p for p in parts if p and slug_re.match(p)]
        if parts:
            server_allowed = parts
            break

    ok_models = [m for m, kind, *_ in results if kind == "OK"]
    if ok_models:
        print()
        print("[doctor] 실제 OK 응답을 받은 모델:")
        print("  " + ", ".join(ok_models))

    if server_allowed:
        print()
        print(
            "[doctor] 서버가 알려준 사용 가능 슬러그:\n  "
            + ", ".join(server_allowed)
        )
        # 서버 메시지가 잘려서 코덱스/그록 등이 빠질 수 있다.
        # 실제 OK 받은 모델까지 합쳐서 권장 풀을 출력한다.
        merged = list(dict.fromkeys(server_allowed + ok_models))
        if merged != server_allowed:
            print("  (실제 OK 응답까지 합친 풀):\n  " + ", ".join(merged))
        print(
            "  → .agents/agents.yaml 의 model / fallback_models 는 이 풀 안에서만\n"
            "    구성하세요. 그 외 슬러그는 매 호출마다 거절되어 폴백 비용만 듭니다."
        )

    all_500_internal = (
        bool(results)
        and all(
            kind == "FAIL" and status == 500 and code == "internal"
            for _, kind, status, code, _msg in results
        )
    )
    if all_500_internal and results:
        print()
        print(
            "[doctor] 모든 모델이 HTTP 500 internal 응답.\n"
            "  → 클라이언트 코드/모델 선택 문제가 아닙니다. Cursor 백엔드가 이 API 키로 들어오는 호출을 거절 중.\n"
            "  점검 순서:\n"
            "    1) https://status.cursor.com 에서 SDK/Agent API 장애 여부 확인\n"
            "    2) https://www.cursor.com/dashboard?tab=integrations 에서 API 키가 살아있는지 / 만료/회수 여부 확인\n"
            "    3) 키를 새로 발급해서 .env 의 CURSOR_API_KEY 교체 후 재시도\n"
            "       (chmod 600 .env, 키는 채팅/PR 어디에도 노출되지 않게)\n"
            "    4) Cursor 요금제/사용량 한도 확인 (Settings → Billing). 한도 소진 시 일부 응답은 500으로 떨어집니다.\n"
            "    5) Python SDK preview access 가 계정에 활성화돼 있는지 확인 (Cursor 지원 문의).\n"
            "  최소 우회: 일단 IDE 의 채팅에서 동일 계정으로 동작하는지 먼저 확인."
        )


def cmd_status(_: argparse.Namespace) -> None:
    print(f"workspace : {WORKSPACE_ROOT}")
    print(f"rules     : {'OK' if RULES_FILE.exists() else 'MISSING'}")
    print(f"roles     : {'OK' if ROLES_FILE.exists() else 'MISSING'}")
    print(f"reqs file : {'OK' if REQUIREMENTS_FILE.exists() else 'MISSING'}")
    print(f"approved  : {'YES' if approval_present() else 'NO (build 차단됨)'}")
    print(f"env model : {ENV_MODEL or '(unset)'}")
    print(f"planner              : {resolve_model_chain('planner')}")
    print(f"tester               : {resolve_model_chain('tester')}")
    print(f"benchmark_researcher : {resolve_model_chain('benchmark_researcher')}")
    print(f"coder                : {resolve_model_chain('coder')}")
    print(f"db_architect         : {resolve_model_chain('db_architect')}")
    print(f"tech_writer          : {resolve_model_chain('tech_writer')}")
    print(f"default              : {resolve_model_chain(None)}")
    if _git_repo_ready():
        print(f"git branch  : {_git_current_branch() or '(detached)'}")
    else:
        print("git branch  : (no repo — run ./scripts/git_branch_setup.sh)")
    print(f"branch policy: .agents/branches.yaml")


def cmd_plan(args: argparse.Namespace) -> None:
    """기획자 에이전트와 멀티턴 대화를 수행한다.

    동작:
    - 새 세션은 .agents/.planner_session.json 에 agent_id 를 저장한다.
    - --resume 옵션을 주면 직전 세션을 이어 받아 대화한다.
    - 종료 키워드: :q, :exit, :quit, :bye (또는 Ctrl+D)
    """

    DOCS_DIR.mkdir(parents=True, exist_ok=True)
    PLAN_NOTES_FILE.touch(exist_ok=True)
    api_key = require_api_key()
    setup_input_history()

    if getattr(args, "new", False) and PLANNER_SESSION_FILE.exists():
        PLANNER_SESSION_FILE.unlink()
        print("[info] 기존 planner 세션 파일을 삭제하고 새 세션으로 시작합니다.")

    planner_chain = resolve_model_chain("planner")

    prev_id = load_planner_session() if args.resume else None
    if args.resume and not prev_id:
        print("[warn] 저장된 planner 세션이 없습니다. 새 세션을 시작합니다.")

    def _open_with_chain():
        """모델 체인 순으로 Agent.create/resume 시도. 마지막에 사용된 모델 ID 도 반환."""

        last_err: Exception | None = None
        for i, model_id in enumerate(planner_chain):
            has_next = i < len(planner_chain) - 1
            try:
                if prev_id:
                    return (
                        _retry_call(
                            lambda mid=model_id: Agent.resume(
                                prev_id,
                                AgentOptions(api_key=api_key, model=mid),
                            ),
                            label=f"plan resume model={model_id}",
                        ),
                        model_id,
                    )
                return (
                    _retry_call(
                        lambda mid=model_id: Agent.create(
                            api_key=api_key,
                            model=mid,
                            local=LocalAgentOptions(cwd=str(WORKSPACE_ROOT)),
                        ),
                        label=f"plan create model={model_id}",
                    ),
                    model_id,
                )
            except CursorAgentError as err:
                last_err = err
                msg = err.message or ""
                if has_next and (
                    _looks_like_quota_or_unavailable(msg) or not err.is_retryable
                ):
                    print(
                        f"[fallback] planner model={model_id} 실패 → 다음 모델 시도: "
                        f"{planner_chain[i+1]}  reason={msg!s:.120}"
                    )
                    continue
                raise
        if last_err is not None:
            raise last_err
        raise RuntimeError("모델 체인이 비어 있습니다.")

    if _RICH and _CONSOLE is not None:
        _CONSOLE.print(
            Panel.fit(
                f"planner ({'resume' if prev_id else 'new'}) | chain={planner_chain}\n"
                "도움말: :help / :multi / :show / :reload / :q",
                title="기획자 모드",
                border_style="green",
            )
        )
    else:
        print(
            f"[planner] 시작 ({'resume' if prev_id else 'new'}) | chain={planner_chain}"
        )
        print(_HELP_TEXT)
        print()

    def handle_slash(line: str, agent) -> bool:
        """슬래시 명령을 처리하면 True를 반환, 아니면 False."""

        if line == ":show":
            if REQUIREMENTS_FILE.exists():
                if _RICH and _CONSOLE is not None:
                    _CONSOLE.print(Rule("REQUIREMENTS.md", style="magenta"))
                    _CONSOLE.print(Markdown(REQUIREMENTS_FILE.read_text(encoding="utf-8")))
                else:
                    print(REQUIREMENTS_FILE.read_text(encoding="utf-8"))
            else:
                print("[info] REQUIREMENTS.md 가 아직 없습니다.")
            return True
        if line == ":reload":
            if not REQUIREMENTS_FILE.exists():
                print("[info] REQUIREMENTS.md 가 없어 reload 불가.")
                return True
            current = REQUIREMENTS_FILE.read_text(encoding="utf-8")
            before = snapshot_files(_watched_paths())
            send_and_print(
                agent,
                "다음은 현재 docs/REQUIREMENTS.md 의 전체 내용이다. "
                "이 내용을 컨텍스트로 받아들이고, 모순/누락/추가 질문이 있으면 짚어 줘. "
                "코드는 작성하지 마라.\n\n"
                f"=== REQUIREMENTS.md ===\n{current}\n",
                watch_before=before,
            )
            return True
        return False

    try:
        agent_ctx, active_model = _open_with_chain()
        with agent_ctx as agent:
            save_planner_session(agent.agent_id)
            print(f"[session] {agent.agent_id} | model={active_model}")
            print()

            if not prev_id:
                first_user = args.brief
                if not first_user:
                    user_line = read_user_line("사용자(첫 입력): ")
                    if user_line is None or user_line == EXIT_TOKEN or user_line == "":
                        print("[abort] 입력이 비어 있어 종료합니다.")
                        return
                    first_user = user_line
                before = snapshot_files(_watched_paths())
                send_and_print(
                    agent,
                    f"{planner_system_prompt()}\n\n=== 사용자 첫 입력 ===\n{first_user}\n",
                    watch_before=before,
                )

            while True:
                user_input = read_user_line("사용자: ")
                if user_input is None or user_input == EXIT_TOKEN:
                    print("[exit]")
                    break
                if user_input == "":
                    continue
                if user_input.startswith(":"):
                    if handle_slash(user_input, agent):
                        continue
                    print(f"[info] 알 수 없는 명령: {user_input}. :help 참고")
                    continue
                before = snapshot_files(_watched_paths())
                send_and_print(agent, user_input, watch_before=before)
    except CursorAgentError as err:
        print(
            f"[fatal] planner 세션 시작 실패: retryable={err.is_retryable} message={err.message}",
            file=sys.stderr,
        )
        sys.exit(2)

    print()
    print("[다음 단계 안내]")
    print(f"1) {REQUIREMENTS_FILE} 를 직접 확인/수정하세요.")
    print(f"2) 만족하면 파일 끝에 다음 줄을 추가하세요:\n   {APPROVAL_MARKER}")
    print("3) 같은 대화로 다시 들어오려면:")
    print("   .venv/bin/python scripts/run_agent.py plan --resume")
    print("4) 승인 완료 후 코더 실행:")
    print("   .venv/bin/python scripts/run_agent.py build --target src/backend")


def cmd_build(args: argparse.Namespace) -> None:
    role = getattr(args, "role", "coder") or "coder"
    if role not in ALL_BUILD_ROLES:
        print(
            f"[fatal] --role 은 {', '.join(sorted(ALL_BUILD_ROLES))} 중 하나여야 합니다.",
            file=sys.stderr,
        )
        sys.exit(2)

    if role in BUILD_ROLES and not approval_present():
        print(
            "[blocked] docs/REQUIREMENTS.md 에 사용자 승인 마커가 없습니다. "
            f"파일 끝에 `{APPROVAL_MARKER}` 를 추가한 뒤 다시 실행하세요.",
            file=sys.stderr,
        )
        sys.exit(3)

    target = (WORKSPACE_ROOT / args.target).resolve()
    stream = resolve_stream(args, target)

    if role in ("coder", "tester"):
        ensure_role_branch(role, stream)
        if role == "tester":
            target = transfer_dir_for_stream(stream)
        elif stream == "frontend":
            target = WORKSPACE_ROOT / "src" / "frontend"
        else:
            target = WORKSPACE_ROOT / "src" / "backend"
    else:
        pass

    if role == "coder" and not target.exists():
        print(f"[fatal] 작업 대상이 존재하지 않습니다: {target}", file=sys.stderr)
        sys.exit(2)

    if role in AUTO_ROLES:
        DOCS_DIR.mkdir(parents=True, exist_ok=True)
        PLAN_NOTES_FILE.touch(exist_ok=True)
        DECISIONS_FILE.parent.mkdir(parents=True, exist_ok=True)

    interval = getattr(args, "interval", None)
    if interval is None:
        interval = _role_default_interval(role)
    label = ROLE_LABELS.get(role, role)
    question_marker = ROLE_QUESTION_MARKERS.get(role, "질문")

    def one_iteration() -> None:
        task = getattr(args, "task", None)
        prompt = _build_role_prompt(role, target, task=task, stream=stream)

        watched = _role_watched_paths(role, target, stream=stream)
        before = snapshot_files(watched)
        plan_notes_before = (
            PLAN_NOTES_FILE.read_text(encoding="utf-8")
            if PLAN_NOTES_FILE.exists()
            else ""
        )

        print(f"[build] role={role} model_chain={resolve_model_chain(role)}")
        result = call_agent(prompt, WORKSPACE_ROOT, role=role)

        watched_after = _role_watched_paths(role, target, stream=stream)
        changes = diff_snapshots(before, watched_after)

        if result is not None and getattr(result, "result", ""):
            render_agent_output(result.result, title=label)
        else:
            print(f"[info] {role} 가 텍스트 요약을 반환하지 않았습니다.")

        render_build_changes(changes, before)

        plan_notes_after = (
            PLAN_NOTES_FILE.read_text(encoding="utf-8")
            if PLAN_NOTES_FILE.exists()
            else ""
        )
        if plan_notes_after != plan_notes_before and question_marker in plan_notes_after:
            msg = (
                f"{role} 가 docs/PLAN_NOTES.md '### {question_marker}' 섹션에 "
                "질문을 추가했습니다.\n"
                "→ plan 모드에서 해결:\n"
                "    .venv/bin/python scripts/run_agent.py plan --resume"
            )
            if _RICH and _CONSOLE is not None:
                _CONSOLE.print(Panel(msg, title="확인 필요", border_style="red"))
            else:
                print("[확인 필요]")
                print(msg)

        print()
        print(f"[다음 단계] role={role}")
        if role == "coder":
            print("  - git diff 로 코드 확인 후 커밋")
            print(f"      git -C {WORKSPACE_ROOT / 'src/backend'} status")
        elif role == "db_architect":
            print("  - docs/ERD.md · db/migration SQL 확인")
        elif role == "benchmark_researcher":
            print("  - docs/BENCHMARK_REPORT.md · docs/COMPETITOR_MATRIX.md 확인")
            print("  - planner 자동 동기화: build --role planner")
        elif role == "tester":
            print(f"  - transfer/{stream}/checklists · manifests 확인")
            print("  - docs/TEST_REPORT.md 확인")
        elif role == "planner":
            print("  - docs/REQUIREMENTS.md · docs/USER_STORIES.md · docs/PLAN_NOTES.md 확인")
            print("  - 사용자 승인 전 plan --resume 으로 대화형 검토 권장")
        else:
            print("  - docs/USER_MANUAL.md 등 문서 확인")

    if not args.loop:
        one_iteration()
        return

    print(f"[loop] role={role} interval={interval}s")
    while True:
        if role in BUILD_ROLES and not approval_present():
            print("[blocked] 승인 마커가 사라져 build 루프를 종료합니다.", file=sys.stderr)
            sys.exit(3)
        one_iteration()
        time.sleep(interval)


def main() -> None:
    parser = argparse.ArgumentParser(description=".agents 기반 멀티 모드 에이전트 실행기")
    sub = parser.add_subparsers(dest="mode", required=True)

    p_plan = sub.add_parser("plan", help="기획자 모드 (멀티턴 대화)")
    p_plan.add_argument("--brief", help="첫 입력을 대화형 대신 인자로 전달")
    p_plan.add_argument(
        "--resume",
        action="store_true",
        help="직전 planner 세션을 이어서 대화 (.agents/.planner_session.json)",
    )
    p_plan.add_argument(
        "--new",
        action="store_true",
        help="기존 planner 세션 파일을 삭제하고 새 세션으로 시작",
    )
    p_plan.set_defaults(func=cmd_plan)

    p_doctor = sub.add_parser(
        "doctor",
        help="SDK 연결/모델 가용성 진단 (각 모델에 ping)",
    )
    p_doctor.set_defaults(func=cmd_doctor)

    p_build = sub.add_parser("build", help="구현/설계/문서 에이전트 (승인된 REQUIREMENTS 기반)")
    p_build.add_argument(
        "--role",
        default="coder",
        choices=sorted(ALL_BUILD_ROLES),
        help=(
            "에이전트 역할: coder(코드), db_architect(DB), tech_writer(문서), "
            "benchmark_researcher(경쟁사 벤치마크), planner(벤치마크 반영 자동 기획), "
            "tester(QA 이관 — migration 브랜치·transfer/ 전용)"
        ),
    )
    p_build.add_argument(
        "--stream",
        choices=["backend", "frontend"],
        default=None,
        help="coder/tester 스트림: backend(기본) 또는 frontend. develop/migration 브랜치 선택",
    )
    p_build.add_argument(
        "--target",
        default="src/backend",
        help="coder 전용 작업 대상 (--stream 과 연동, tester 는 transfer/ 사용)",
    )
    p_build.add_argument(
        "--task",
        help="이번 build 에서 수행할 작업을 명시 (미지정 시 역할별 자동 추정)",
    )
    p_build.add_argument(
        "--interval",
        type=int,
        default=None,
        help="--loop 반복 간격(초). 미지정 시 coder/db=900, tech_writer=3600, benchmark/planner=10800",
    )
    p_build.add_argument("--loop", action="store_true", help="반복 실행")
    p_build.set_defaults(func=cmd_build)

    p_status = sub.add_parser("status", help="현재 상태 확인")
    p_status.set_defaults(func=cmd_status)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
