"""
Cursor SDK 기반 멀티 모드 에이전트 실행기.

모드:
  plan    기획자(planner)가 사용자에게 인터뷰 → docs/planning/PLAN_NOTES.md 및 REQUIREMENTS.md 갱신
  build   승인된 REQUIREMENTS 기반 구현 (--role: coder | db_architect | tech_writer |
          benchmark_researcher | planner). benchmark/planner 는 승인 없이 docs/ 만 갱신
  status  현재 상태(승인 여부, 최근 작업) 출력

핵심 정책:
- 모든 프롬프트에 .agents/rules.md 와 .agents/agents.yaml 을 강제 주입한다.
- build 모드는 docs/planning/REQUIREMENTS.md 안에 사용자 승인 마커가 있어야만 실행된다.
  마커: HTML 주석 한 줄로 `<!-- approved-by-user: true -->`
- 비밀값은 환경변수/.env 로만 관리하고 로그에 출력하지 않는다.
- 자율 무한 실행을 피하기 위해, build 모드는 1회 실행을 기본으로 한다.
  반복이 필요하면 --loop 옵션으로 명시적으로 켠다.
"""

from __future__ import annotations

import argparse
import atexit
import fcntl
import hashlib
import json
import os
import signal
import subprocess
import sys
import time
import traceback
from collections.abc import Mapping
from contextlib import contextmanager
from pathlib import Path

from dotenv import load_dotenv
from cursor_sdk import (
    Agent,
    AgentOptions,
    Client,
    CursorAgentError,
    LocalAgentOptions,
    SendOptions,
    close_default_client,
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
PLANNING_DIR = DOCS_DIR / "planning"
RESEARCH_DIR = PLANNING_DIR / "research"
QA_DIR = DOCS_DIR / "qa"
TECHNICAL_DIR = DOCS_DIR / "technical"
PRODUCT_DIR = DOCS_DIR / "product"
OPS_DIR = DOCS_DIR / "ops"
SECURITY_DIR = DOCS_DIR / "security"
PLAN_NOTES_FILE = PLANNING_DIR / "PLAN_NOTES.md"
ROADMAP_FILE = PLANNING_DIR / "ROADMAP.md"
QA_FEEDBACK_FILE = QA_DIR / "QA_FEEDBACK.md"
TEST_REPORT_FILE = QA_DIR / "TEST_REPORT.md"
REQUIREMENTS_FILE = PLANNING_DIR / "REQUIREMENTS.md"
BENCHMARK_REPORT_FILE = RESEARCH_DIR / "BENCHMARK_REPORT.md"
COMPETITOR_MATRIX_FILE = RESEARCH_DIR / "COMPETITOR_MATRIX.md"
SNAPSHOTS_DIR = RESEARCH_DIR / "snapshots"
SNAPSHOTS_README_FILE = SNAPSHOTS_DIR / "README.md"
USER_STORIES_FILE = PLANNING_DIR / "USER_STORIES.md"
FLOWCHART_FILE = PLANNING_DIR / "FLOWCHART.md"
API_SPEC_FILE = TECHNICAL_DIR / "API_SPEC.md"
ERD_FILE = TECHNICAL_DIR / "ERD.md"
DATA_RETENTION_POLICY_FILE = OPS_DIR / "DATA_RETENTION_POLICY.md"
DESIGN_SYSTEM_FILE = PRODUCT_DIR / "DESIGN_SYSTEM.md"
DECISIONS_FILE = WORKSPACE_ROOT / "memory" / "decisions.md"
PLANNER_SESSION_FILE = AGENTS_DIR / ".planner_session.json"
PLANNER_HISTORY_FILE = AGENTS_DIR / ".planner_history"
WORKSPACE_BASELINE_FILE = AGENTS_DIR / "workspace_baseline.yaml"

APPROVAL_MARKER = "<!-- approved-by-user: true -->"

DEFAULT_MODEL_FALLBACK = "composer-2.5"
ENV_MODEL = os.environ.get("AGENT_MODEL")
DEFAULT_INTERVAL = int(os.environ.get("AGENT_INTERVAL_SECONDS", "1800"))
DEFAULT_WRITER_INTERVAL = int(os.environ.get("AGENT_WRITER_INTERVAL_SECONDS", "3600"))
DEFAULT_TESTER_INTERVAL = int(os.environ.get("AGENT_TESTER_INTERVAL_SECONDS", "1800"))
DEFAULT_PLANNING_INTERVAL = int(os.environ.get("AGENT_PLANNING_INTERVAL_SECONDS", "1800"))
DEFAULT_BENCHMARK_INTERVAL = int(os.environ.get("AGENT_BENCHMARK_INTERVAL_SECONDS", "1800"))
DEFAULT_UX_INTERVAL = int(os.environ.get("AGENT_UX_INTERVAL_SECONDS", "1800"))
DEFAULT_SECURITY_INTERVAL = int(os.environ.get("AGENT_SECURITY_INTERVAL_SECONDS", "86400"))

BUILD_ROLES = frozenset({
    "coder", "db_architect", "tech_writer", "tester", "ux_designer", "security_auditor",
})
AUTO_ROLES = frozenset({"benchmark_researcher", "planner"})
ALL_BUILD_ROLES = BUILD_ROLES | AUTO_ROLES
ROLE_LABELS = {
    "coder": "코더",
    "db_architect": "DB 설계자",
    "tech_writer": "기술 문서",
    "tester": "QA(이관)",
    "ux_designer": "UX 디자이너",
    "security_auditor": "보안 감사",
    "benchmark_researcher": "벤치마크 분석",
    "planner": "기획자(자동)",
}
ROLE_QUESTION_MARKERS = {
    "coder": "코더 질문",
    "db_architect": "DB 설계 질문",
    "tech_writer": "문서 작성 질문",
    "tester": "QA 이관 질문",
    "ux_designer": "UX 설계 질문",
    "security_auditor": "보안 감사 질문",
    "benchmark_researcher": "벤치마크 질문",
    "planner": "기획 질문",
}

# 일시적인 네트워크/브리지 오류에 대한 재시도 정책
RETRY_MAX = max(0, int(os.environ.get("AGENT_RETRY_MAX", "3")))
RETRY_BASE_DELAY = max(0.1, float(os.environ.get("AGENT_RETRY_BASE_DELAY", "1.5")))
# plan send: bridge 끊김·일시 internal 에 더 관대하게 (환경변수로 조절 가능)
PLAN_SEND_RETRY_MAX = max(
    1, int(os.environ.get("AGENT_PLAN_RETRY_MAX", os.environ.get("AGENT_RETRY_MAX", "6")))
)
BRIDGE_RECOVER_MAX = max(1, int(os.environ.get("AGENT_BRIDGE_RECOVER_MAX", "5")))
BRIDGE_RECOVER_DELAY = max(0.2, float(os.environ.get("AGENT_BRIDGE_RECOVER_DELAY", "1.0")))
BRIDGE_POST_INTERNAL_RETRY = max(
    0, int(os.environ.get("AGENT_BRIDGE_POST_INTERNAL_RETRY", "1"))
)
# 연속 internal error N 모델이면 API/bridge 전역 장애로 보고 체인 중단
PLAN_INTERNAL_ABORT_STREAK = max(
    1, int(os.environ.get("AGENT_PLAN_INTERNAL_ABORT", "2"))
)
# 체인 전체 실패 시 bridge 재시작 후 처음부터 재시도
PLAN_CHAIN_PASS_MAX = max(1, int(os.environ.get("AGENT_PLAN_CHAIN_PASS", "1")))
# plan: 매 답변 전 ping (별도 Agent.prompt — bridge 간섭 가능). 기본 OFF
PLAN_PROBE_BEFORE_SEND = os.environ.get("AGENT_PLAN_PROBE", "0").strip().lower() in (
    "1",
    "true",
    "yes",
)
BRIDGE_LAUNCH_LOCK = AGENTS_DIR / "bridge.launch.lock"
_BRIDGE_LAUNCH_LOCK_INSTALLED = False


@contextmanager
def _bridge_launch_lock():
    """동시 Bridge.launch 직렬화 (race → --tool-callback-auth-token 누락 방지)."""

    BRIDGE_LAUNCH_LOCK.parent.mkdir(parents=True, exist_ok=True)
    with open(BRIDGE_LAUNCH_LOCK, "a+", encoding="utf-8") as fp:
        fcntl.flock(fp.fileno(), fcntl.LOCK_EX)
        try:
            yield
        finally:
            fcntl.flock(fp.fileno(), fcntl.LOCK_UN)


def _install_bridge_launch_lock() -> None:
    global _BRIDGE_LAUNCH_LOCK_INSTALLED
    if _BRIDGE_LAUNCH_LOCK_INSTALLED:
        return
    from cursor_sdk._bridge import Bridge

    original = Bridge.launch.__func__

    @classmethod
    def locked_launch(cls, *args, **kwargs):
        with _bridge_launch_lock():
            return original(cls, *args, **kwargs)

    Bridge.launch = locked_launch
    _BRIDGE_LAUNCH_LOCK_INSTALLED = True


_install_bridge_launch_lock()

# build 모드: 프로세스당 1 bridge 재사용 + 종료 시 반드시 close (orphan node 누수 방지)
_BUILD_CLIENT: Client | None = None
_BRIDGE_CLEANUP_HANDLERS_INSTALLED = False
BRIDGE_PRUNE_ENABLED = os.environ.get("AGENT_BRIDGE_PRUNE", "1").strip().lower() not in (
    "0",
    "false",
    "no",
)


def _proc_ppid(pid: int) -> int | None:
    try:
        for line in Path(f"/proc/{pid}/status").read_text(encoding="utf-8").splitlines():
            if line.startswith("PPid:"):
                return int(line.split()[1])
    except (OSError, ValueError, IndexError):
        return None
    return None


def _proc_cmdline(pid: int) -> str | None:
    try:
        raw = Path(f"/proc/{pid}/cmdline").read_bytes()
        if not raw:
            return None
        return raw.replace(b"\0", b" ").decode("utf-8", errors="replace").strip()
    except OSError:
        return None


def _parse_ps_pid_cmd(line: str) -> tuple[int, str] | None:
    line = line.strip()
    if not line:
        return None
    parts = line.split(None, 1)
    if len(parts) != 2 or not parts[0].isdigit():
        return None
    return int(parts[0]), parts[1]


def _iter_ps_lines(pattern: str) -> list[tuple[int, str]]:
    try:
        proc = subprocess.run(
            ["pgrep", "-af", pattern],
            capture_output=True,
            text=True,
            timeout=15,
        )
    except (OSError, subprocess.TimeoutExpired):
        return []
    rows: list[tuple[int, str]] = []
    for line in (proc.stdout or "").splitlines():
        parsed = _parse_ps_pid_cmd(line)
        if parsed is not None:
            rows.append(parsed)
    return rows


def _workspace_path_token() -> str:
    return WORKSPACE_ROOT.as_posix()


def _cmd_targets_workspace(cmd: str) -> bool:
    token = _workspace_path_token()
    return token in cmd and "cursor-sdk-bridge" in cmd


def _iter_workspace_bridge_processes() -> list[dict[str, int | str]]:
    rows: list[dict[str, int | str]] = []
    for pid, cmd in _iter_ps_lines("cursor-sdk-bridge"):
        if not _cmd_targets_workspace(cmd):
            continue
        ppid = _proc_ppid(pid)
        rows.append(
            {
                "pid": pid,
                "ppid": ppid if ppid is not None else -1,
                "cmd": cmd,
            }
        )
    return rows


def _is_run_agent_ancestor(pid: int, *, max_depth: int = 12) -> bool:
    """pid 의 조상 중 python run_agent.py 프로세스가 있으면 True."""

    cur = pid
    for _ in range(max_depth):
        if cur <= 1:
            return False
        cmd = _proc_cmdline(cur)
        if cmd and "run_agent.py" in cmd and "python" in cmd.lower():
            base = Path(cmd.split(None, 1)[0]).name.lower() if cmd.split() else ""
            if base.startswith("python") or "/python" in cmd.lower():
                return True
        parent = _proc_ppid(cur)
        if parent is None:
            return False
        cur = parent
    return False


def _active_run_agent_pids() -> set[int]:
    active: set[int] = set()
    root_token = _workspace_path_token()
    for pid, cmd in _iter_ps_lines("run_agent.py"):
        if "run_agent.py" not in cmd:
            continue
        if root_token not in cmd and "scripts/run_agent.py" not in cmd:
            continue
        # pgrep -af 는 cursor sandbox bash wrapper 도 매칭 — python 프로세스만
        base = Path(cmd.split(None, 1)[0]).name.lower() if cmd.split() else ""
        if base not in ("python", "python3", "python3.10", "python3.11", "python3.12"):
            if "python" not in cmd.lower() or " extglob " in cmd:
                continue
        active.add(pid)
    return active


def _owned_build_bridge_pid() -> int | None:
    client = _BUILD_CLIENT
    if client is None:
        return None
    owned = getattr(client, "_owned_bridge", None)
    if owned is None:
        return None
    process = getattr(owned, "process", None)
    if process is None:
        return None
    pid = getattr(process, "pid", None)
    return int(pid) if isinstance(pid, int) and pid > 0 else None


def _close_build_client() -> None:
    global _BUILD_CLIENT
    client = _BUILD_CLIENT
    _BUILD_CLIENT = None
    if client is None:
        return
    try:
        client.close()
    except Exception:
        pass


def _ensure_build_client() -> Client:
    global _BUILD_CLIENT
    if _BUILD_CLIENT is not None:
        return _BUILD_CLIENT
    close_default_client()
    _BUILD_CLIENT = Client.launch_bridge(workspace=str(WORKSPACE_ROOT))
    return _BUILD_CLIENT


def prune_orphan_bridges(
    *,
    dry_run: bool = False,
    quiet: bool = False,
    keep_pids: set[int] | None = None,
) -> dict[str, int | list[int]]:
    """ogada workspace orphan cursor-sdk-bridge 정리.

    orphan = PPID 1(reparented) · 부모 프로세스 소멸 · 부모가 run_agent.py 가 아님.
    """

    keep = set(keep_pids or ())
    owned = _owned_build_bridge_pid()
    if owned is not None:
        keep.add(owned)

    active_agents = _active_run_agent_pids()
    killed: list[int] = []
    kept: list[int] = []

    for info in _iter_workspace_bridge_processes():
        pid = int(info["pid"])
        if pid in keep:
            kept.append(pid)
            continue

        ppid = int(info["ppid"])
        if ppid in active_agents or _is_run_agent_ancestor(pid):
            kept.append(pid)
            continue

        parent_cmd = _proc_cmdline(ppid) if ppid > 0 else None
        if ppid > 0 and parent_cmd and "run_agent.py" in parent_cmd:
            kept.append(pid)
            continue

        is_orphan = ppid <= 0 or ppid == 1 or parent_cmd is None
        if not is_orphan and parent_cmd:
            is_orphan = not _is_run_agent_ancestor(pid)

        if not is_orphan:
            kept.append(pid)
            continue

        if dry_run:
            killed.append(pid)
            continue

        try:
            os.kill(pid, signal.SIGTERM)
        except OSError:
            kept.append(pid)
            continue
        time.sleep(0.05)
        if Path(f"/proc/{pid}").exists():
            try:
                os.kill(pid, signal.SIGKILL)
            except OSError:
                pass
        if not Path(f"/proc/{pid}").exists():
            killed.append(pid)
        else:
            kept.append(pid)

    summary: dict[str, int | list[int]] = {
        "killed": killed,
        "kept": kept,
        "killed_count": len(killed),
        "kept_count": len(kept),
    }
    if not quiet:
        print(
            f"[bridge-prune] killed={len(killed)} kept={len(kept)} "
            f"active_run_agent={len(active_agents)}"
        )
        if killed:
            print(f"  removed PIDs: {' '.join(str(p) for p in killed[:20])}"
                  + (" …" if len(killed) > 20 else ""))
    return summary


def _release_bridge_resources(*, prune: bool = True) -> None:
    _close_build_client()
    try:
        close_default_client()
    except Exception:
        pass
    if prune and BRIDGE_PRUNE_ENABLED:
        prune_orphan_bridges(quiet=True)


def _install_bridge_cleanup_handlers() -> None:
    global _BRIDGE_CLEANUP_HANDLERS_INSTALLED
    if _BRIDGE_CLEANUP_HANDLERS_INSTALLED:
        return
    _BRIDGE_CLEANUP_HANDLERS_INSTALLED = True
    atexit.register(_release_bridge_resources)

    def _signal_release(signum: int, _frame: object) -> None:
        _release_bridge_resources()
        raise SystemExit(128 + signum if signum < 128 else 1)

    for sig in (signal.SIGTERM, signal.SIGINT):
        try:
            signal.signal(sig, _signal_release)
        except (OSError, ValueError):
            pass


_install_bridge_cleanup_handlers()


def _load_branches_yaml() -> dict | None:
    if not BRANCHES_FILE.exists():
        return None
    try:
        import yaml  # type: ignore

        data = yaml.safe_load(BRANCHES_FILE.read_text(encoding="utf-8"))
        return data if isinstance(data, dict) else None
    except Exception:
        return None


def _git_repo_ready(cwd: Path | None = None) -> bool:
    work = cwd or WORKSPACE_ROOT
    try:
        subprocess.run(
            ["git", "rev-parse", "--git-dir"],
            cwd=work,
            capture_output=True,
            check=True,
        )
        return True
    except Exception:
        return False


def _git_current_branch(cwd: Path | None = None) -> str | None:
    work = cwd or WORKSPACE_ROOT
    if not _git_repo_ready(work):
        return None
    try:
        r = subprocess.run(
            ["git", "branch", "--show-current"],
            cwd=work,
            capture_output=True,
            text=True,
            check=True,
        )
        branch = (r.stdout or "").strip()
        return branch or None
    except Exception:
        return None


def _git_checkout(branch: str, cwd: Path) -> None:
    subprocess.run(
        ["git", "checkout", branch],
        cwd=cwd,
        check=True,
    )


def _git_status_porcelain(cwd: Path) -> str:
    if not _git_repo_ready(cwd):
        return ""
    try:
        r = subprocess.run(
            ["git", "status", "--porcelain"],
            cwd=cwd,
            capture_output=True,
            text=True,
            check=True,
        )
        return r.stdout or ""
    except Exception:
        return ""


def _git_commits_ahead(cwd: Path, branch: str, remote: str = "origin") -> int:
    """로컬 branch 가 remote/{branch} 보다 앞선 커밋 수."""
    if not _git_repo_ready(cwd):
        return 0
    try:
        subprocess.run(
            ["git", "fetch", remote, branch],
            cwd=cwd,
            capture_output=True,
            text=True,
            timeout=120,
        )
    except Exception:
        pass
    try:
        r = subprocess.run(
            ["git", "rev-list", "--count", f"{remote}/{branch}..{branch}"],
            cwd=cwd,
            capture_output=True,
            text=True,
            check=True,
        )
        return int((r.stdout or "0").strip() or "0")
    except Exception:
        return 0


def _git_short_rev(cwd: Path, ref: str = "HEAD") -> str | None:
    if not _git_repo_ready(cwd):
        return None
    try:
        r = subprocess.run(
            ["git", "rev-parse", "--short", ref],
            cwd=cwd,
            capture_output=True,
            text=True,
            check=True,
        )
        rev = (r.stdout or "").strip()
        return rev or None
    except Exception:
        return None


def _measure_submodule_baseline(stream: str) -> dict[str, object]:
    repo = submodule_dir_for_stream(stream)
    develop = branch_for_stream(stream, "develop")
    test = branch_for_stream(stream, "test")
    head = _git_short_rev(repo) or "unknown"
    test_head = _git_short_rev(repo, test) or "unknown"
    dirty_lines = [
        ln.strip()
        for ln in _git_status_porcelain(repo).splitlines()
        if ln.strip()
    ]
    return {
        "stream": stream,
        "path": f"src/{stream}",
        "develop": head,
        "test": test_head,
        "dirty": bool(dirty_lines),
        "dirty_count": len(dirty_lines),
        "ahead_of_origin": _git_commits_ahead(repo, develop),
    }


def measure_workspace_baseline() -> dict[str, object]:
    return {
        "backend": _measure_submodule_baseline("backend"),
        "frontend": _measure_submodule_baseline("frontend"),
    }


def _load_workspace_baseline_notes() -> list[str]:
    if not WORKSPACE_BASELINE_FILE.exists():
        return []
    notes: list[str] = []
    in_notes = False
    for raw in WORKSPACE_BASELINE_FILE.read_text(encoding="utf-8").splitlines():
        line = raw.rstrip()
        if line.startswith("notes:"):
            in_notes = True
            continue
        if in_notes:
            if line and not line.startswith(" ") and not line.startswith("-"):
                break
            stripped = line.strip()
            if stripped.startswith("- "):
                note = stripped[2:].strip().strip('"')
                if note:
                    notes.append(note)
    return notes


def format_baseline_prompt_block(stream: str | None = None) -> str:
    """coder 프롬프트에 주입할 실측 baseline 블록."""
    measured = measure_workspace_baseline()
    notes = _load_workspace_baseline_notes()
    lines = [
        "## 0-0. 실측 baseline (CRITICAL — ROADMAP/QA 과거 SHA보다 우선)",
        "",
        "다음은 **지금 워크스페이스 git 실측**이다. ROADMAP·QA_FEEDBACK·PLAN_NOTES의 "
        "과거 SHA(`d5654c0`, `e5fd48d`, `428ba7d` 등)는 **유실·폐기** — "
        "**checkout 재현 금지**. `.agents/workspace_baseline.yaml` 과 동일 우선순위.",
        "",
        "| stream | develop HEAD | test HEAD | dirty | ahead(origin/develop) |",
        "|--------|--------------|-----------|-------|------------------------|",
    ]
    for key in ("backend", "frontend"):
        info = measured[key]
        dirty = "YES" if info["dirty"] else "clean"
        if info["dirty_count"]:
            dirty += f" ({info['dirty_count']} files)"
        lines.append(
            f"| {key} | `{info['develop']}` | `{info['test']}` | {dirty} | "
            f"{info['ahead_of_origin']} |"
        )
    if notes:
        lines.extend(["", "**확정 메모:**"])
        lines.extend(f"- {n}" for n in notes[:6])
    if stream in ("backend", "frontend"):
        cur = measured[stream]
        lines.extend(
            [
                "",
                f"**이번 스트림 (`{stream}`)**: `src/{stream}` @ develop **`{cur['develop']}`** "
                f"에서만 작업. working tree **clean** 유지 후 커밋·push.",
            ]
        )
    return "\n".join(lines)


def _roadmap_in_progress_streams() -> list[str]:
    if not ROADMAP_FILE.exists():
        return []
    text = ROADMAP_FILE.read_text(encoding="utf-8")
    versions = _roadmap_parse_versions(text)
    return [
        v.get("stream", "backend")
        for v in versions
        if v.get("status") == "in_progress"
    ]


def coder_preflight_warnings(stream: str) -> list[str]:
    warnings: list[str] = []
    measured = measure_workspace_baseline()
    for name in ("backend", "frontend"):
        info = measured[name]
        if info["dirty"]:
            warnings.append(
                f"{info['path']} working tree dirty "
                f"({info['dirty_count']} entries) — 커밋 후 작업"
            )
    active = _roadmap_in_progress_streams()
    if len(active) > 1:
        warnings.append(
            f"ROADMAP in_progress 스트림 {len(active)}개({', '.join(active)}) — "
            "한 번에 하나만 구현"
        )
    if stream not in active and active:
        warnings.append(
            f"현재 --stream={stream} 이지만 ROADMAP in_progress는 "
            f"{', '.join(active)} — stream 확인"
        )
    return warnings


def print_coder_preflight(stream: str) -> None:
    for msg in coder_preflight_warnings(stream):
        print(f"[preflight-warn] {msg}", file=sys.stderr)
    block = format_baseline_prompt_block(stream)
    print(block)


def push_submodule_develop(role: str, stream: str) -> None:
    """coder/ux_designer 작업 후 submodule develop 을 origin 에 push."""
    if role not in ("coder", "ux_designer"):
        return

    stream = "frontend" if role == "ux_designer" else stream
    if stream not in ("backend", "frontend"):
        return

    repo = submodule_dir_for_stream(stream)
    if not _git_repo_ready(repo):
        print(f"[push-skip] submodule git 없음: {repo}", file=sys.stderr)
        return

    branch = branch_for_stream(stream, "develop")
    current = _git_current_branch(repo)
    if current != branch:
        print(
            f"[push-warn] {repo.name} branch={current or 'unknown'} "
            f"(expected {branch}) — push 생략",
            file=sys.stderr,
        )
        return

    if _git_status_porcelain(repo).strip():
        print(
            f"[push-warn] {repo.name} working tree dirty — "
            "커밋 후 push 필요 (run_agent build 종료 시 자동 push)",
            file=sys.stderr,
        )
        return

    ahead = _git_commits_ahead(repo, branch)
    if ahead <= 0:
        print(f"[push-ok] {repo.name}@{branch} origin 과 동기화됨 (push 불필요)")
        return

    try:
        subprocess.run(
            ["git", "push", "origin", branch],
            cwd=repo,
            check=True,
            capture_output=True,
            text=True,
            timeout=180,
        )
        print(f"[push-ok] {repo.name} → origin/{branch} ({ahead} commit(s))")
    except subprocess.CalledProcessError as err:
        detail = (err.stderr or err.stdout or str(err)).strip()
        print(
            f"[push-fail] {repo.name} git push origin {branch} 실패: {detail}",
            file=sys.stderr,
        )


def stream_config(stream: str) -> dict:
    data = _load_branches_yaml() or {}
    submodules = data.get("submodules") or data.get("streams") or {}
    cfg = submodules.get(stream) or {}
    return cfg if isinstance(cfg, dict) else {}


def submodule_dir_for_stream(stream: str) -> Path:
    cfg = stream_config(stream)
    rel = cfg.get("path") or cfg.get("src") or f"src/{stream}"
    return WORKSPACE_ROOT / str(rel)


def worktree_dir_for_stream(stream: str, phase: str = "test") -> Path:
    """branches.yaml worktrees.{phase} 경로. 없으면 src/{stream}-{phase} 관례."""

    cfg = stream_config(stream)
    worktrees = cfg.get("worktrees") or {}
    rel = worktrees.get(phase) if isinstance(worktrees, dict) else None
    if isinstance(rel, str) and rel.strip():
        return WORKSPACE_ROOT / rel.strip()
    return WORKSPACE_ROOT / f"src/{stream}-{phase}"


def role_src_dir(role: str, stream: str) -> Path | None:
    """역할별 소스코드 디렉터리 (develop 주 경로 vs test worktree)."""

    if role in ("coder", "ux_designer"):
        return submodule_dir_for_stream(stream if role != "ux_designer" else "frontend")
    if role == "tester":
        return worktree_dir_for_stream(stream, "test")
    return None


def _worktree_registered(primary: Path, wt_path: Path) -> bool:
    if not _git_repo_ready(primary):
        return False
    try:
        r = subprocess.run(
            ["git", "worktree", "list", "--porcelain"],
            cwd=primary,
            capture_output=True,
            text=True,
            check=True,
        )
    except Exception:
        return False
    target = wt_path.resolve().as_posix()
    for line in (r.stdout or "").splitlines():
        if line.startswith("worktree "):
            listed = line.split(" ", 1)[1].strip()
            if Path(listed).resolve().as_posix() == target:
                return True
    return False


def ensure_worktree(stream: str, phase: str = "test") -> Path:
    """test worktree 를 생성·검증한다. primary(develop) 는 checkout 하지 않는다."""

    primary = submodule_dir_for_stream(stream)
    wt_path = worktree_dir_for_stream(stream, phase)
    branch = branch_for_stream(stream, phase)
    develop = branch_for_stream(stream, "develop")

    if not _git_repo_ready(primary):
        print(
            f"[warn] submodule git 없음 ({primary}) — worktree 미적용. "
            "./scripts/git_branch_setup.sh 실행 권장.",
            file=sys.stderr,
        )
        return wt_path

    if _worktree_registered(primary, wt_path):
        current = _git_current_branch(wt_path)
        if current != branch:
            print(f"[worktree] {wt_path.name} checkout {branch} (was: {current or 'unknown'})")
            try:
                _git_checkout(branch, wt_path)
            except subprocess.CalledProcessError as err:
                print(
                    f"[fatal] worktree checkout 실패: {wt_path} → {branch}",
                    file=sys.stderr,
                )
                raise SystemExit(2) from err
        else:
            print(f"[worktree] {wt_path.name} branch={branch} (ok)")
        return wt_path

    if wt_path.exists():
        print(
            f"[fatal] worktree 경로가 이미 있으나 등록되지 않음: {wt_path}. "
            "수동 정리 후 ./scripts/git_branch_setup.sh 실행.",
            file=sys.stderr,
        )
        raise SystemExit(2)

    current = _git_current_branch(primary)
    if current == branch:
        print(
            f"[worktree] primary({primary.name}) 가 {branch} 에 있음 "
            f"→ {develop} 로 전환 후 worktree 생성"
        )
        try:
            _git_checkout(develop, primary)
        except subprocess.CalledProcessError as err:
            print(
                f"[fatal] primary checkout 실패: {primary} → {develop}. "
                "dirty tree 를 commit/stash 한 뒤 ./scripts/git_branch_setup.sh 실행.",
                file=sys.stderr,
            )
            raise SystemExit(2) from err

    print(f"[worktree] create {wt_path.name} ← {branch}")
    try:
        subprocess.run(
            ["git", "worktree", "add", str(wt_path), branch],
            cwd=primary,
            check=True,
        )
    except subprocess.CalledProcessError as err:
        print(
            f"[fatal] worktree 생성 실패: {wt_path}. "
            "./scripts/git_branch_setup.sh 실행.",
            file=sys.stderr,
        )
        raise SystemExit(2) from err
    return wt_path


def git_cwd_for_role(role: str, stream: str) -> Path | None:
    """역할별 git 작업 디렉터리. tester 는 test worktree, coder/ux 는 develop 주 경로."""

    if role in ("planner", "benchmark_researcher", "tech_writer", "db_architect"):
        return None
    return role_src_dir(role, stream)


def _roadmap_parse_versions(text: str) -> list[dict[str, str]]:
    """ROADMAP.md 에서 ## vN 블록 메타데이터 추출."""

    import re

    versions: list[dict[str, str]] = []
    for match in re.finditer(
        r"^## (v[\w.]+)[^\n]*\n(.*?)(?=^## v|\Z)",
        text,
        re.MULTILINE | re.DOTALL,
    ):
        block = match.group(2)
        meta = {"id": match.group(1)}

        def _field(name: str) -> str | None:
            m = re.search(rf"\*\*{name}\*\*:\s*(\S+)", block)
            return m.group(1).strip() if m else None

        for key in ("status", "merge_status", "stream"):
            val = _field(key)
            if val:
                meta[key] = val
        versions.append(meta)
    return versions


def _roadmap_merge_ready(stream: str) -> str | None:
    """stream 과 일치하고 merge_status=ready 인 첫 버전 id."""

    if not ROADMAP_FILE.exists():
        return None
    text = ROADMAP_FILE.read_text(encoding="utf-8")
    for ver in _roadmap_parse_versions(text):
        if ver.get("merge_status") != "ready":
            continue
        ver_stream = ver.get("stream", "backend")
        if ver_stream == stream:
            return ver.get("id")
    return None


def _roadmap_mark_merged(version_id: str) -> None:
    """버전 블록의 merge_status 를 merged, status 를 done 으로 갱신."""

    if not ROADMAP_FILE.exists():
        return
    import re

    text = ROADMAP_FILE.read_text(encoding="utf-8")
    pattern = rf"(## {re.escape(version_id)}[^\n]*\n.*?)(- \*\*merge_status\*\*:\s*)\w+"
    if not re.search(pattern, text, re.DOTALL):
        return
    text = re.sub(
        pattern,
        r"\1\2merged",
        text,
        count=1,
        flags=re.DOTALL,
    )
    status_pat = rf"(## {re.escape(version_id)}[^\n]*\n.*?)(- \*\*status\*\*:\s*)\w+"
    text = re.sub(
        status_pat,
        r"\1\2done",
        text,
        count=1,
        flags=re.DOTALL,
    )
    ROADMAP_FILE.write_text(text, encoding="utf-8")


def merge_develop_to_test(stream: str, version_id: str) -> bool:
    """develop 을 test worktree 에 merge (primary develop 경로는 그대로 유지)."""

    primary = submodule_dir_for_stream(stream)
    if not _git_repo_ready(primary):
        print(f"[merge-skip] submodule git 없음: {primary}")
        return False

    develop = branch_for_stream(stream, "develop")
    test = branch_for_stream(stream, "test")
    test_wt = ensure_worktree(stream, "test")

    result = subprocess.run(
        [
            "git",
            "merge",
            develop,
            "-m",
            f"chore({stream}): merge {develop} into {test} ({version_id})",
        ],
        cwd=test_wt,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        err = (result.stderr or result.stdout or "").strip()
        print(
            f"[merge-fail] {test_wt.name}: {develop} → {test}: {err[:500]}",
            file=sys.stderr,
        )
        return False
    print(f"[merge-ok] {test_wt.name}: {develop} → {test} ({version_id})")
    return True


def maybe_merge_version_to_test(stream: str) -> bool:
    """ROADMAP merge_status=ready 이면 develop → test 자동 merge."""

    version_id = _roadmap_merge_ready(stream)
    if not version_id:
        return False
    if merge_develop_to_test(stream, version_id):
        _roadmap_mark_merged(version_id)
        print(f"[merge] ROADMAP {version_id} → merge_status=merged")
        return True
    return False


def run_live_e2e_post_merge(stream: str, version_id: str | None = None) -> int:
    """frontend merge 성공 직후 실백엔드 Vitest (결정 73 post-merge, 결정 96 파이프라인)."""

    if stream != "frontend":
        return 0
    if os.environ.get("AGENT_SKIP_LIVE_E2E", "").strip().lower() in ("1", "true", "yes"):
        print("[live-e2e-skip] AGENT_SKIP_LIVE_E2E set")
        return 0

    script = WORKSPACE_ROOT / "scripts" / "run-live-e2e.sh"
    if not script.is_file():
        print("[live-e2e-skip] scripts/run-live-e2e.sh 없음", file=sys.stderr)
        return 0

    label = version_id or "merge"
    print(f"[live-e2e] post-merge ({label}): {script.name} 실행 중...")
    result = subprocess.run(
        [str(script)],
        cwd=WORKSPACE_ROOT,
        capture_output=True,
        text=True,
    )
    if result.stdout:
        print(result.stdout.rstrip())
    if result.returncode == 0:
        print("[live-e2e-ok] post-merge live E2E passed")
        return 0

    print(
        f"[live-e2e-fail] post-merge live E2E failed (exit={result.returncode})",
        file=sys.stderr,
    )
    if result.stderr:
        print(result.stderr.rstrip(), file=sys.stderr)
    _record_live_e2e_failure(version_id or "unknown", result)
    return result.returncode


def _record_live_e2e_failure(version_id: str, result: subprocess.CompletedProcess) -> None:
    """LIVE E2E 실패 요약을 QA_FEEDBACK Open 에 기록."""

    if not QA_FEEDBACK_FILE.exists():
        return
    tail = (result.stdout or "")[-1200:] + (result.stderr or "")[-800:]
    tail = tail.strip().replace("\n", " ")[:500]
    stamp = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    entry = (
        f"\n### [TSR] post-merge live E2E FAIL — {version_id} ({stamp})\n\n"
        f"- **severity**: HIGH\n"
        f"- **stream**: frontend\n"
        f"- **exit**: {result.returncode}\n"
        f"- **요약**: `./scripts/run-live-e2e.sh` 실패 — 백엔드 기동·DB 마이그레이션·"
        f"`scripts/dev-live-e2e.env` 확인\n"
        f"- **로그 tail**: `{tail or 'empty'}`\n"
    )
    text = QA_FEEDBACK_FILE.read_text(encoding="utf-8")
    marker = "## Open\n"
    if marker not in text:
        return
    text = text.replace(marker, marker + entry, 1)
    QA_FEEDBACK_FILE.write_text(text, encoding="utf-8")
    print("[live-e2e] QA_FEEDBACK.md Open 에 실패 항목 기록")


def branch_for_stream(stream: str, phase: str) -> str:
    cfg = stream_config(stream)
    branches = cfg.get("branches") or {}
    name = branches.get(phase) if isinstance(branches, dict) else None
    if not name:
        name = cfg.get(phase)
    if isinstance(name, str) and name.strip():
        return name.strip()
    return phase


def resolve_stream(args: argparse.Namespace, target: Path) -> str:
    stream = getattr(args, "stream", None)
    if stream in ("backend", "frontend"):
        return stream
    target_str = target.as_posix()
    if "frontend" in target_str:
        return "frontend"
    if "backend" in target_str:
        return "backend"
    return "backend"


def required_branch_for_role(role: str, stream: str) -> str | None:
    if role == "coder":
        return branch_for_stream(stream, "develop")
    if role == "tester":
        return branch_for_stream(stream, "test")
    if role == "ux_designer":
        return branch_for_stream("frontend", "develop")
    return None


def ensure_role_branch(role: str, stream: str) -> str | None:
    """역할·스트림에 맞는 worktree/브랜치를 준비한다.

    - coder/ux_designer: 주 경로(src/{stream})를 develop 으로 checkout
    - tester: 별도 worktree(src/{stream}-test)만 사용 — 주 경로는 건드리지 않음
    """

    branch = required_branch_for_role(role, stream)
    if branch is None:
        return None

    if role == "tester":
        ensure_worktree(stream, "test")
        return branch

    primary = submodule_dir_for_stream(stream if role != "ux_designer" else "frontend")
    if not _git_repo_ready(primary):
        print(
            f"[warn] submodule git 없음 ({primary}) — 브랜치 정책 미적용. "
            "./scripts/git_branch_setup.sh 실행 권장.",
            file=sys.stderr,
        )
        return branch

    current = _git_current_branch(primary)
    if current == branch:
        print(f"[git] {primary.name} branch={branch} (ok)")
        return branch
    print(f"[git] {primary.name} checkout {branch} (was: {current or 'unknown'})")
    try:
        _git_checkout(branch, primary)
    except subprocess.CalledProcessError as err:
        print(
            f"[fatal] git checkout 실패: {primary} → {branch}. "
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


def _agent_meta(role: str) -> dict[str, str | list[str]]:
    """agents.yaml 의 id · doc_signature · doc_audience 조회."""

    data = _load_agents_yaml() or {}
    for a in data.get("agents", []) or []:
        if isinstance(a, dict) and a.get("name") == role:
            return {
                "id": str(a.get("id") or role[:3].upper()),
                "doc_signature": str(a.get("doc_signature") or f"[{role[:3].upper()}]"),
                "doc_audience": a.get("doc_audience") or [],
            }
    return {"id": role[:3].upper(), "doc_signature": f"[{role[:3].upper()}]", "doc_audience": []}


def _doc_identity_block(role: str) -> str:
    meta = _agent_meta(role)
    aud = meta.get("doc_audience") or []
    aud_str = ",".join(str(x) for x in aud) if aud else "(해당 역할 소비자)"
    return (
        "## 문서 식별 (agent_identity)\n"
        f"- 작성자 id: `{meta['id']}` | 섹션 postfix: `{meta['doc_signature']}`\n"
        f"- 문서 최상단 메타: `<!-- doc:owner={meta['id']} doc:audience={aud_str} updated=ISO8601 -->`\n"
        f"- PLAN_NOTES 질문 섹션: `### {meta['doc_signature']} ...`\n"
    )


def resolve_model_chain(role: str | None = None) -> list[str]:
    """모델 우선순위 체인을 반환한다.

    1) agents[<role>].model -> agents[<role>].fallback_models[*] -> models.default
       -> DEFAULT_MODEL_FALLBACK
    2) 환경변수 AGENT_MODEL 이 있으면 체인 **맨 앞**에 끼워 넣는다 (폴백 유지).
    """

    data = _load_agents_yaml() or {}
    chain: list[str] = []
    chain_exclusive = False

    if role:
        for a in data.get("agents", []) or []:
            if isinstance(a, dict) and a.get("name") == role:
                for p in a.get("preferred_models") or []:
                    if isinstance(p, str) and p.strip():
                        chain.append(p.strip())
                m = a.get("model")
                if isinstance(m, str) and m.strip():
                    chain.append(m.strip())
                for f in a.get("fallback_models") or []:
                    if isinstance(f, str) and f.strip():
                        chain.append(f.strip())
                if a.get("model_chain_exclusive") is True or a.get("preferred_models"):
                    chain_exclusive = True
                break

    if not chain_exclusive:
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

    if ENV_MODEL:
        override = ENV_MODEL.strip()
        if override:
            out = [override] + [m for m in out if m != override]

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


def _looks_like_global_api_error(message: str) -> bool:
    """모델을 바꿔도 동일하게 실패하는 Cursor 백엔드/계정 전역 오류."""

    msg = (message or "").lower()
    return "internal error" in msg or msg.startswith("internal:")


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


def _recover_build_bridge(*, restart: bool = False) -> None:
    """build/plan bridge 정리 — owned client 종료 + orphan prune."""

    if restart:
        _close_build_client()
    try:
        close_default_client()
    except Exception:
        pass
    if BRIDGE_PRUNE_ENABLED:
        prune_orphan_bridges(quiet=True)


def _build_agent_prompt(
    prompt: str,
    *,
    api_key: str,
    model_id: str,
    cwd: Path,
) -> object:
    """build 모드용 Agent.prompt — 프로세스별 bridge 재사용 + 기본 client 오염 방지."""

    client = _ensure_build_client()
    return Agent.prompt(
        prompt,
        AgentOptions(
            api_key=api_key,
            model=model_id,
            local=LocalAgentOptions(cwd=str(cwd)),
        ),
        client=client,
    )


def call_agent(prompt: str, cwd: Path, role: str | None = None):
    """모델 체인을 따라 순차 시도. 성공 시 `RunResult` 를 반환, 실패 시 None."""

    api_key = require_api_key()
    chain = resolve_model_chain(role)
    label = ROLE_LABELS.get(role or "", role or "에이전트")

    def _run_prompt(model_id: str):
        bridge_recoveries = 0

        def _do() -> object:
            return _build_agent_prompt(
                prompt,
                api_key=api_key,
                model_id=model_id,
                cwd=cwd,
            )

        while True:
            status_msg = f"[bold green]{label} 작업 중 ({model_id})...[/bold green]"
            try:
                if _RICH and _CONSOLE is not None:
                    with _CONSOLE.status(status_msg, spinner="dots"):
                        return _retry_call(_do, label=f"build model={model_id}")
                print(f"  ({label} 작업 중 — {model_id}...)", flush=True)
                return _retry_call(_do, label=f"build model={model_id}")
            except CursorAgentError as err:
                msg = err.message or ""
                if (
                    _looks_like_bridge_restart_needed(msg)
                    and bridge_recoveries < BRIDGE_RECOVER_MAX
                ):
                    bridge_recoveries += 1
                    print(
                        f"[recover] bridge 재시작 ({bridge_recoveries}/{BRIDGE_RECOVER_MAX}) "
                        f"— {msg[:80]}",
                        file=sys.stderr,
                    )
                    _recover_build_bridge(restart=True)
                    time.sleep(BRIDGE_RECOVER_DELAY * bridge_recoveries)
                    continue
                raise

    for i, model_id in enumerate(chain):
        has_next = i < len(chain) - 1
        try:
            result = _run_prompt(model_id)
        except CursorAgentError as err:
            msg = err.message or ""
            if has_next and (
                _looks_like_quota_or_unavailable(msg)
                or _looks_like_bridge_restart_needed(msg)
                or not err.is_retryable
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


def _roadmap_progress_hint(stream: str = "backend") -> str:
    """ROADMAP.md 기준 현재 in_progress 버전 작업 힌트."""

    if not ROADMAP_FILE.exists():
        return (
            "현재 진행: **ROADMAP 미작성**\n"
            "→ planner 가 `docs/planning/ROADMAP.md` 를 작성할 때까지 "
            "`docs/planning/REQUIREMENTS.md` §7 순서로 진행."
        )
    text = ROADMAP_FILE.read_text(encoding="utf-8")
    versions = _roadmap_parse_versions(text)
    active = next(
        (
            v
            for v in versions
            if v.get("status") == "in_progress"
            and v.get("stream", "backend") == stream
        ),
        None,
    )
    if not active:
        planned = next(
            (v for v in versions if v.get("status") == "planned"),
            None,
        )
        if planned:
            return (
                f"현재 진행: **{stream} in_progress 버전 없음**\n"
                f"→ `docs/planning/ROADMAP.md` 에서 `{planned['id']}` 를 "
                f"`status: in_progress` 로 전환 후 구현 시작."
            )
        return (
            f"현재 진행: **{stream} 활성 버전 없음**\n"
            "→ ROADMAP·QA_FEEDBACK 확인 후 planner 와 협의."
        )
    vid = active["id"]
    merge_st = active.get("merge_status", "pending")
    qa_note = ""
    if QA_FEEDBACK_FILE.exists():
        qa = QA_FEEDBACK_FILE.read_text(encoding="utf-8")
        if "### [OPEN]" in qa or "### [PLANNED]" in qa:
            qa_note = (
                "\n→ **우선**: `docs/qa/QA_FEEDBACK.md` Open/Planned BLOCK·HIGH 항목부터 수정."
            )
    if merge_st == "ready":
        return (
            f"현재 진행: **{vid} 완료 — test merge 대기**\n"
            f"→ 완료 기준 재확인 후 merge_status=ready 유지 "
            f"(다음 build 시 {stream}/develop → {stream}/test 자동 merge)."
        )
    return (
        f"현재 진행: **ROADMAP {vid} ({stream}) — in_progress**\n"
        f"→ `docs/planning/ROADMAP.md` 의 `{vid}` 범위·완료 기준만 구현.\n"
        f"→ 모든 완료 기준 `[x]` 후 `merge_status: ready` 로 변경.{qa_note}"
    )


def _sprint_progress_hint(target: Path, stream: str = "backend") -> str:
    """src/backend·frontend + ROADMAP 상태로 다음 작업 추정."""

    roadmap_hint = _roadmap_progress_hint(stream)
    if ROADMAP_FILE.exists():
        return roadmap_hint

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
        "→ `docs/planning/REQUIREMENTS.md` §7 순서표·§7 완료 기준표를 읽고, "
        "아직 산출물이 없는 **다음 번호** 작업을 즉시 구현."
    )


def _build_coder_prompt(target: Path, task: str | None = None, stream: str = "backend") -> str:
    """build 모드용 코더 프롬프트. 거대한 REQUIREMENTS 전문 인라인 대신 워크스페이스 파일 참조."""

    rules = must_read(RULES_FILE)
    progress = _sprint_progress_hint(target, stream=stream)
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
    baseline_block = format_baseline_prompt_block(stream)

    return (
        f"=== .agents/rules.md ===\n{rules}\n\n"
        "지금 너의 역할은 `.agents/agents.yaml` 의 `coder` 이다.\n"
        "역할 상세·출력 경로는 agents.yaml 의 coder 섹션을 워크스페이스에서 읽어라.\n\n"
        f"{baseline_block}\n\n"
        "## 0. 브랜치·범위 (CRITICAL)\n"
        f"- **현재 스트림**: `{stream}` | **submodule**: `src/{stream}` | **브랜치**: `{develop_branch}`\n"
        f"- submodule `src/{stream}` 의 **develop** 브랜치에서만 코드를 작성한다.\n"
        "- `transfer/`, test·operation 브랜치, `docs/qa/TEST_REPORT.md` 는 **수정 금지** "
        "(QA/tester 이관 전담).\n"
        "- `.agents/branches.yaml` submodule 브랜치 정책을 따른다.\n"
        f"- 작업 후 **반드시** `src/{stream}` @ `{develop_branch}` 에 **커밋**한다 "
        "(working tree clean). build 종료 시 `git push origin {develop_branch}` 가 "
        "자동 실행되며, **미커밋 변경은 push 되지 않는다**.\n\n"
        f"{_doc_identity_block('coder')}\n"
        "## 0-1. 버전·피드백 (CRITICAL)\n"
        "- **`docs/planning/ROADMAP.md`** 의 `status: in_progress` 버전 **하나만** 구현.\n"
        "- **`docs/qa/QA_FEEDBACK.md`** Open/Planned 항목(BLOCK·HIGH)을 **우선** 수정.\n"
        "- 수정 완료 시 QA_FEEDBACK 항목을 **Fixed** 섹션으로 이동.\n"
        "- 해당 버전 **완료 기준 전부 [x]** 후 `merge_status: ready` 로 변경 "
        f"→ 다음 build 시 `{develop_branch}`가 `{branch_for_stream(stream, 'test')}`에 **자동 merge**.\n"
        "- test·operation 브랜치 직접 checkout·merge **금지** (스크립트가 처리).\n\n"
        "## 1. 스택 강제 (최우선)\n"
        "- **반드시** `docs/planning/REQUIREMENTS.md` §1-1 기술 스택 표를 읽고 그대로 따른다.\n"
        "  (Java Spring Boot 3.x / React Vite SPA / PostgreSQL / JWT+RBAC / SaaS 멀티테넌트)\n"
        "- Python/FastAPI 등 다른 스택 코드는 **작성 금지**. `src/backend/.venv` 등 레거시는 무시.\n"
        "- agents.yaml 에 Python/FastAPI 가 적혀 있어도 REQUIREMENTS §1-1 이 우선.\n\n"
        "## 2. 자율 실행 (필수 — 위반 시 실패)\n"
        "- 사용자에게 \"무엇부터 할까요?\" \"어떤 작업부터?\" 같은 **질문 금지**.\n"
        "- 이번 호출에서 **반드시 파일을 생성·수정**한다. 텍스트만 돌려주면 실패.\n"
        "- 불확실하면 `docs/planning/PLAN_NOTES.md` 의 `### 코더 질문` 에 기록 후 중단.\n"
        "- 비밀값 하드코딩 금지 (.agents/rules.md §3).\n\n"
        "## 2-1. 구현 품질 — 신중하게 (CRITICAL)\n"
        "- **추측 구현 금지**: 커밋 전에 `docs/technical/API_SPEC.md`·백엔드 Request/Response record·"
        "기존 유사 화면을 **읽고** HTTP 메서드·필드명·필수값을 맞춘다.\n"
        "- **반쪽 기능 금지**: UI만 있고 API가 없거나, raw `fetch`로 JWT가 빠지거나, "
        "백엔드 DTO와 다른 필드명(`address` vs `addressLine1` 등)으로 저장하는 코드는 **실패**로 간주.\n"
        "- **프론트**: `src/frontend/src/api/http.js` 의 `apiFetch`·`services.js` 패턴 준수. "
        "`Field`는 render-prop `{(p) => <TextInput {...p} />}` 로 label 연결.\n"
        "- **범위 최소화**: 요청·ROADMAP·QA 항목만 수정. 무관한 리팩터·문서 대량 수정 금지.\n"
        "- **검증**: backend는 `mvn test`(관련 테스트), frontend는 `npm test`(관련 파일) "
        "최소 1회 — 실패 시 원인 수정 후 커밋.\n"
        "- **사용자 체감**: 저장 실패·모달 오동작·빈 목록이 '정상'처럼 보이게 만들지 말 것 — "
        "오류 메시지·필수 필드·권한 분기를 명확히.\n\n"
        "## 2-2. 파이프라인 속도 — 사용자 피드백과 동일 (CRITICAL)\n"
        "- **느긋한 문서 작업 금지**: TEST_REPORT·ROADMAP·PLAN_NOTES만 손대고 `src/` 를 안 고치면 **실패**.\n"
        "- **우선순위**: (1) `memory/decisions.md` 최근 사용자 확정·버그 (2) `docs/qa/QA_FEEDBACK.md` "
        "Open BLOCK/HIGH (3) ROADMAP `in_progress` 완료 기준 미충족 항목.\n"
        "- **한 사이클 목표**: 사용자가 채팅으로 지적한 유형의 버그 1건 이상을 **end-to-end**로 "
        "(API+UI+테스트) 닫거나, Open QA 1건을 Fixed로 옮길 만큼 구현.\n"
        "- **질문·대기 금지**: 피드백이 있으면 바로 코드 수정·커밋. \"다음에 할까요?\" 금지.\n"
        "- 신중함(§2-1)은 **속도와 양립** — 스펙 읽기는 하되, 범위는 QA·피드백 항목에만 한정.\n\n"
        f"{task_block}\n\n"
        "## 3. 읽어야 할 문서 (워크스페이스에서 직접 열기)\n"
        "- `.agents/workspace_baseline.yaml` (확정 baseline — **최우선**)\n"
        "- docs/planning/ROADMAP.md (현재 in_progress 버전·완료 기준)\n"
        "- docs/qa/QA_FEEDBACK.md (Open/Planned — tester 피드백)\n"
        "- docs/planning/REQUIREMENTS.md (§1-1 스택, §7 스프린트, Must 기능)\n"
        "- docs/technical/API_SPEC.md\n"
        "- docs/planning/USER_STORIES.md\n"
        "- docs/planning/FLOWCHART.md\n\n"
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
    erd = ERD_FILE
    retention = DATA_RETENTION_POLICY_FILE
    backend = WORKSPACE_ROOT / "src/backend"
    migrations = list(backend.rglob("db/migration/*.sql")) if backend.exists() else []
    migrations += list(backend.rglob("db/migrations/*.sql")) if backend.exists() else []
    flyway = list(backend.rglob("**/db/migration/V*.sql")) if backend.exists() else []

    if not erd.exists():
        return (
            "현재 진행: **ERD 미작성**\n"
            "→ `docs/technical/ERD.md` 작성: SaaS 멀티테넌트(organization/branch), "
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
            "→ `docs/ops/DATA_RETENTION_POLICY.md` 작성 (PII·의료 데이터 보관·삭제 정책)."
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
    missing = [name for name in outputs if not (OPS_DIR / name).exists()]
    if missing:
        first = missing[0]
        return (
            f"현재 진행: **{len(missing)}개 문서 미작성**\n"
            f"→ 지금 즉시 `docs/ops/{first}` 초안 작성 ({outputs[first]}).\n"
            "→ `src/` 구현·`docs/planning/REQUIREMENTS.md`·`docs/technical/API_SPEC.md` 를 근거로 작성.\n"
            "→ 코드 변경 금지, docs/ 만 수정. 사용자 질문 금지."
        )
    return (
        "현재 진행: **기본 문서 세트 있음**\n"
        "→ 최근 `src/`·`docs/ops/CHANGELOG.md` 변경 반영, FAQ/매뉴얼 보강.\n"
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
        f"{_doc_identity_block('db_architect')}\n"
        "## 0. 스택 (REQUIREMENTS §1-1 우선)\n"
        "- DB: **PostgreSQL**. 백엔드: **Java Spring Boot 3.x**.\n"
        "- 마이그레이션: Flyway (`src/backend/src/main/resources/db/migration/V*.sql`).\n"
        "- agents.yaml 의 `src/db/` 경로는 레거시 — Java 백엔드 Flyway 경로 사용.\n\n"
        "## 1. 자율 실행 (필수)\n"
        "- 사용자에게 질문하지 말고 **docs/ 또는 migration SQL 파일**을 생성·수정.\n"
        "- 애플리케이션 Java 코드는 작성하지 않는다 (coder 역할).\n"
        "- 불확실하면 `docs/planning/PLAN_NOTES.md` 의 `### DB 설계 질문` 에 기록 후 중단.\n\n"
        f"{task_block}\n\n"
        "## 2. 읽을 문서\n"
        "- docs/planning/REQUIREMENTS.md, docs/technical/API_SPEC.md, docs/planning/USER_STORIES.md\n"
        "- docs/technical/ERD.md (있으면 갱신)\n\n"
        "## 3. 출력 위치\n"
        "- docs/technical/ERD.md, docs/ops/DATA_RETENTION_POLICY.md\n"
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
        f"{_doc_identity_block('tech_writer')}\n"
        "## 0. 범위\n"
        "- **docs/ 아래 문서만** 작성·갱신. src/ 코드 변경 금지.\n"
        "- 스택은 REQUIREMENTS §1-1 (Java Spring Boot + React + PostgreSQL) 기준으로 서술.\n\n"
        "## 1. 자율 실행 (필수)\n"
        "- 사용자 질문 금지. 이번 호출에서 docs/ 파일을 반드시 생성·수정.\n"
        "- 불확실하면 `docs/planning/PLAN_NOTES.md` 의 `### 문서 작성 질문` 에 기록 후 중단.\n\n"
        f"{task_block}\n\n"
        "## 2. 읽을 자료\n"
        "- docs/planning/REQUIREMENTS.md, docs/technical/API_SPEC.md, docs/planning/FLOWCHART.md\n"
        "- src/backend/, src/frontend/ (구현 상태 파악용, 수정 금지)\n\n"
        "## 3. 출력 위치\n"
        "- docs/ops/USER_MANUAL.md, docs/ops/ADMIN_GUIDE.md, docs/ops/DEPLOYMENT_GUIDE.md\n"
        "- docs/ops/CHANGELOG.md, docs/ops/FAQ.md\n\n"
        "## 4. 최종 응답 포맷\n"
        "  ## 문서 작업 요약\n"
        "  - 생성/수정한 문서\n"
        "  - 대상 독자·범위\n"
        "  - 다음 문서화 우선순위\n"
    )


def _benchmark_rotation_focus() -> str:
    """30분 주기 역공학 로테이션 — UTC 시각 기준."""
    slot = (int(time.time()) // 1800) % 5
    focuses = (
        (
            "**케어포 역공학** — `daycare/func.php` 109항목 전수·매뉴얼 PDF 목차·"
            "`demo-work.carefor.co.kr` loadPage/view 파싱(시설 셸=이동서비스 없음 명시). "
            "메뉴 depth·리포트 밀도·본인부담 7-x 번호식 흐름을 ogada Route와 1:1 매핑."
        ),
        (
            "**이지케어 역공학** — `./scripts/ezcare-demo-fetch.sh`(데모 로그인→`/new.ez`)·"
            "`ezCare_fnc.html`·Channel.io 도움말·FAQ rowid "
            "전수(기능명·엑셀 컬럼·처리상태·RFID·이중 일정). 가격·도입 기관 수 재실측."
        ),
        (
            "**엔젤·롱텀·규제** — silverangel/lcms 공개 기능·CMS 부가·"
            "law.go.kr 이동서비스비 러-1~4 **1차 확인**(PLAN_NOTES #44). "
            "2026 수가·평가 #27·단기보호·통합재가 고시 교차검증."
        ),
        (
            "**ogada git 실측** — `src/backend`·`src/frontend` develop HEAD·"
            "`npm test`/`mvn test`·Route·page·모듈 커버 % 재산정. "
            "COMPETITOR_MATRIX ogada 열을 `@HEAD` SHA로 일괄 갱신."
        ),
        (
            "**교차검증·갭 우선순위** — 이전 BNK 가정 번복 여부·미확인 항목 축소·"
            "G14·대시보드·v1.3-C·v2 CMS 등 P0/P1 재정렬. "
            "신규 경쟁사 공지·엑셀 포맷 변경 스캔."
        ),
    )
    return focuses[slot]


def _benchmark_progress_hint() -> str:
    rotation = _benchmark_rotation_focus()
    missing = [
        name
        for name, path in (
            ("BENCHMARK_REPORT.md", BENCHMARK_REPORT_FILE),
            ("COMPETITOR_MATRIX.md", COMPETITOR_MATRIX_FILE),
        )
        if not path.exists()
    ]
    cycle_minimum = (
        "→ **이번 사이클 최소 산출**: 신규 증거 URL 1건+ · 메뉴/필드/워크플로 상세 1블록+ · "
        "COMPETITOR_MATRIX 1행+ `@HEAD` 갱신 · BENCHMARK_REPORT §소절 1건+.\n"
    )
    if missing:
        first = missing[0]
        return (
            f"현재 진행: **{len(missing)}개 벤치마크 산출물 미작성**\n"
            f"→ 지금 즉시 `docs/planning/research/{first}` 초안 작성.\n"
            "→ REQUIREMENTS §1-5, PLAN_NOTES 의 경쟁사 목록(케어포·이지케어·엔젤시스템·롱텀)을 우선 조사.\n"
            "→ **역공학**: func.php·demo-work·FAQ·Channel.io에서 메뉴·필드명·화면 흐름 추출.\n"
            f"{cycle_minimum}"
            f"→ 이번 로테이션 초점: {rotation}\n"
            "→ 출처 URL·조사일·HTTP 상태 기록. 사용자 질문 금지, docs/·memory/ 파일 생성 필수."
        )
    return (
        "현재 진행: **30분 주기 역공학 벤치마크**\n"
        f"→ 이번 로테이션 초점: {rotation}\n"
        f"{cycle_minimum}"
        "→ agents.yaml `reverse_engineering` 방법론 준수 — HTML/JS·FAQ·PDF·git 실측 병행.\n"
        "→ ogada REQUIREMENTS·USER_STORIES·ROADMAP 대비 갭·차별화·MVP 우선순위 제안.\n"
        "→ 새 인사이트는 memory/decisions.md 최상단 + BENCHMARK_REPORT 차수(BNK-N) 기록."
    )


def _planner_auto_progress_hint() -> str:
    benchmark_ready = BENCHMARK_REPORT_FILE.exists() and COMPETITOR_MATRIX_FILE.exists()
    benchmark_note = (
        "벤치마크 산출물 있음 — 최신 BENCHMARK_REPORT·COMPETITOR_MATRIX를 반영해 기획 갱신."
        if benchmark_ready
        else "벤치마크 산출물 없음 — REQUIREMENTS §1-5 기준으로 기획 유지·보강."
    )
    qa_note = ""
    if QA_FEEDBACK_FILE.exists():
        qa = QA_FEEDBACK_FILE.read_text(encoding="utf-8")
        if "### [OPEN]" in qa:
            qa_note = (
                "\n→ **우선**: `docs/qa/QA_FEEDBACK.md` Open 항목을 읽고 "
                "ROADMAP·USER_STORIES·PLAN_NOTES에 태스크 반영 후 Planned 로 이동."
            )
    return (
        f"현재 진행: **자동 기획 동기화**\n"
        f"→ {benchmark_note}\n"
        "→ **docs/planning/ROADMAP.md** 를 v1·v2… 단계별 로드맵으로 유지·갱신 "
        "(status / merge_status / 완료 기준).\n"
        "→ docs/planning/REQUIREMENTS.md, docs/planning/USER_STORIES.md, docs/planning/PLAN_NOTES.md, "
        "docs/planning/FLOWCHART.md, docs/technical/API_SPEC.md 중 **벤치마크·QA 피드백·갭 분석에 따라 수정이 필요한 문서**를 갱신.\n"
        "→ 미확정 사항은 PLAN_NOTES `### 추가 질문`에 누적.\n"
        "→ 사용자 승인 마커(`<!-- approved-by-user: true -->`) 추가 금지.\n"
        f"→ src/ 코드 작성 금지. 사용자 질문 금지.{qa_note}"
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
        "agents.yaml 의 benchmark_researcher 섹션(research_focus·reverse_engineering·outputs)을 읽어라.\n\n"
        f"{_doc_identity_block('benchmark_researcher')}\n"
        "## 0. 범위\n"
        "- **docs/ 및 memory/decisions.md 만** 작성·갱신. src/ 코드 변경 금지.\n"
        "- 주간보호·요양기관 관리 SaaS/ERP 경쟁사의 **서비스 제공 항목·기능·모듈**을 조사·정리.\n"
        "- 공개 자료 + **역공학**(HTML/JS·데모·FAQ·도움말·앱스토어·PDF·git 실측)을 병행한다.\n\n"
        "## 1. 자율 실행 (필수)\n"
        "- 사용자에게 질문하지 말고 **반드시 파일을 생성·수정**한다.\n"
        "- **30분 주기 최소 산출**(agents.yaml `reverse_engineering.per_cycle_minimum`):\n"
        "  · 신규 증거 URL 1건 이상 (또는 기존 URL 재실측 + 변동 기록)\n"
        "  · 경쟁사 메뉴/필드/워크플로 상세 1블록 이상\n"
        "  · COMPETITOR_MATRIX 1행 이상 ogada `@develop HEAD` SHA로 갱신\n"
        "  · BENCHMARK_REPORT §신규 소절 또는 BNK 차수 메모 1건 이상\n"
        "- 불확실한 내용은 「가정」으로 표시 — 로그인·인증서 필요 영역은 「미확인」.\n"
        "- 확인한 내용은 「확인」+ URL·조사일·HTTP 상태·인용 문구.\n"
        "- 불명확해 작업을 중단해야 하면 `docs/planning/PLAN_NOTES.md` 의 "
        "`### 벤치마크 질문` 에 기록 후 중단.\n\n"
        f"{task_block}\n\n"
        "## 2. 역공학 방법 (필수 — 매 사이클 1개 이상 적용)\n"
        "- **케어포**: `daycare/func.php` 정적 메뉴(주야간 정본)·매뉴얼 PDF 목차·"
        "`demo-work.carefor.co.kr` loadPage/view 파싱(시설 셸, 이동서비스 없음).\n"
        "- **이지케어**: `./scripts/ezcare-demo-fetch.sh` 로 데모 로그인 후 `/new.ez` ERP 셸·"
        "`ezcare_top_nav_v2.js`·PGID 화면 스냅샷(비로그인 `/new.ez` 70B stub 금지). "
        "Channel.io 도움말·FAQ rowid·공지에서 기능·엑셀 컬럼·RFID·이중 일정·가격 역추출.\n"
        "- **엔젤·롱텀**: silverangel/lcms 공개 페이지·law.go.kr 고시(이동서비스비 #44).\n"
        "- **로컬 스냅샷**: `docs/planning/research/snapshots/` — live 재실측 후 md5/SIZE 비교·"
        "DRIFT 시 HTML 덮어쓰기·`snapshots/README.md` 표 갱신. grep/verbatim은 "
        "`docs/planning/research/snapshots/<파일명>` 경로 사용.\n"
        "- **ogada 실측**: `git -C src/frontend rev-parse develop`·Route grep·"
        "`git -C src/backend rev-parse develop`·테스트 집계로 baseline 갱신.\n"
        "- HTML에서 form field name·menu-id·Ajax endpoint 힌트·리포트 화면 목록 추출.\n\n"
        "## 3. 읽을 문서\n"
        "- docs/planning/REQUIREMENTS.md (§1-5 벤치마킹, MVP 범위)\n"
        "- docs/planning/PLAN_NOTES.md · docs/planning/ROADMAP.md\n"
        "- .agents/workspace_baseline.yaml (ogada HEAD)\n"
        "- docs/planning/research/BENCHMARK_REPORT.md, docs/planning/research/COMPETITOR_MATRIX.md (있으면 갱신)\n"
        "- docs/planning/research/snapshots/README.md 및 snapshots/*.html (오프라인 carry·md5 비교)\n\n"
        "## 4. 출력 위치\n"
        "- docs/planning/research/BENCHMARK_REPORT.md — 경쟁사별 상세·역공학 실측·§차수(BNK-N)\n"
        "- docs/planning/research/COMPETITOR_MATRIX.md — 기능 비교 표(ogada `@SHA` 열 최신화)\n"
        "- docs/planning/research/snapshots/ — live HTML 스냅샷 갱신·신규 추가·README md5 표 동기화\n"
        "- memory/decisions.md — 벤치마킹에서 도출된 기획 결정(최상단 추가)\n\n"
        "## 5. COMPETITOR_MATRIX 권장 구조\n"
        "- 행: 기능/서비스 항목 (이용자관리, 출석, 건강기록, 청구, 대시보드, 보호자포털, 다지점, QR, 배차 등)\n"
        "- 열: ogada `@HEAD`, 케어포, 이지케어, 엔젤시스템, 롱텀(공단)\n"
        "- 셀: 지원 여부(✅/❌/△), 비고, 근거 URL·역공학 출처\n\n"
        "## 6. 최종 응답 포맷\n"
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
        f"{_doc_identity_block('planner')}\n"
        "## 0. 범위\n"
        "- **docs/ 기획 문서만** 작성·갱신. src/ 코드 변경 금지.\n"
        "- `docs/planning/research/BENCHMARK_REPORT.md`, `docs/planning/research/COMPETITOR_MATRIX.md`, "
        "`memory/decisions.md` 를 **먼저 읽고** ogada 기획에 반영한다.\n"
        "- **`docs/qa/QA_FEEDBACK.md`**, **`docs/qa/TEST_REPORT.md`**, **`docs/planning/ROADMAP.md`** 를 읽고 "
        "tester 검증 이슈를 기획·로드맵에 반영한다.\n"
        "- REQUIREMENTS §1-1 스택(Java Spring Boot + React + PostgreSQL) 유지.\n\n"
        "## 1. 자율 실행 (필수)\n"
        "- 사용자에게 질문하지 말고 **반드시 docs/ 파일을 생성·수정**한다.\n"
        "- **버전 로드맵**: `docs/planning/ROADMAP.md` 에 v1·v2… 단계별 범위·완료 기준·status 유지.\n"
        "- **QA 피드백 반영**: QA_FEEDBACK Open → ROADMAP/USER_STORIES/PLAN_NOTES 태스크화 후 "
        "QA_FEEDBACK Planned 섹션으로 이동, `docs/planning/PLAN_NOTES.md` `### QA 피드백 반영` 기록.\n"
        "- 경쟁사 대비 갭·차별화·MVP 우선순위를 REQUIREMENTS·USER_STORIES에 반영.\n"
        "- 미확정 사항은 `docs/planning/PLAN_NOTES.md` `### 추가 질문`에 누적.\n"
        "- **`<!-- approved-by-user: true -->` 승인 마커는 절대 추가하지 않는다.**\n"
        "- 불명확해 중단해야 하면 `docs/planning/PLAN_NOTES.md` `### 기획 질문`에 기록 후 중단.\n\n"
        f"{task_block}\n\n"
        "## 2. 읽을 문서 (우선순위)\n"
        "1. docs/qa/QA_FEEDBACK.md, docs/qa/TEST_REPORT.md (tester 산출물)\n"
        "2. docs/planning/ROADMAP.md\n"
        "3. docs/planning/research/BENCHMARK_REPORT.md, docs/planning/research/COMPETITOR_MATRIX.md\n"
        "4. memory/decisions.md\n"
        "5. docs/planning/REQUIREMENTS.md, docs/planning/USER_STORIES.md, docs/planning/PLAN_NOTES.md\n"
        "6. docs/planning/FLOWCHART.md, docs/technical/API_SPEC.md (필요 시만 갱신)\n\n"
        "## 3. 출력·갱신 대상\n"
        "- docs/planning/ROADMAP.md — v1·v2… 단계별 범위·완료 기준·status\n"
        "- docs/planning/REQUIREMENTS.md — §1-5 벤치마킹·기능 우선순위·갭 반영\n"
        "- docs/planning/USER_STORIES.md — 경쟁사·QA 대비 누락 스토리 추가\n"
        "- docs/planning/PLAN_NOTES.md — 확인된 결정·추가 질문·`### QA 피드백 반영`\n"
        "- docs/qa/QA_FEEDBACK.md — Open → Planned 이동 (반영 완료 시)\n"
        "- docs/planning/FLOWCHART.md, docs/technical/API_SPEC.md — 벤치마크·QA 기반 수정 필요 시\n\n"
        "## 4. 최종 응답 포맷\n"
        "  ## 기획 동기화 요약\n"
        "  - 반영한 QA 피드백·벤치마크 인사이트\n"
        "  - 갱신한 ROADMAP 버전·우선순위\n"
        "  - 생성/수정한 문서\n"
        "  - 추가·변경한 기능/우선순위\n"
        "  - planner·사용자가 확인할 미확정 질문\n"
    )


def _tester_test_hint(stream: str) -> str:
    transfer = transfer_dir_for_stream(stream)
    develop = branch_for_stream(stream, "develop")
    test_branch = branch_for_stream(stream, "test")
    test_rel = worktree_dir_for_stream(stream, "test").relative_to(WORKSPACE_ROOT)
    develop_rel = submodule_dir_for_stream(stream).relative_to(WORKSPACE_ROOT)
    checklist = transfer / "checklists" / "test.md"
    manifest = transfer / "manifests" / "latest.yaml"

    if not checklist.exists():
        return (
            f"현재 진행: **{stream} 이관 체크리스트 미작성**\n"
            f"→ `transfer/{stream}/checklists/test.md` 초안 작성.\n"
            f"→ `{develop_rel}`(`{develop}`) 대비 `{test_rel}`(`{test_branch}`) 이관 가능 여부 점검.\n"
            f"→ `transfer/{stream}/manifests/latest.yaml` 에 버전·커밋·빌드 정보 기록.\n"
            f"→ `{test_rel}` 에서 테스트 실행. src 주 경로·코드 **수정 금지**."
        )
    if not manifest.exists():
        return (
            f"현재 진행: **체크리스트 있음 — 매니페스트 미작성**\n"
            f"→ `transfer/{stream}/manifests/latest.yaml` 작성 "
            f"(develop→test 이관 대상 커밋, Flyway 버전, npm version 등).\n"
            "→ src/ 수정 금지."
        )
    return (
        f"현재 진행: **{stream} 기본 이관 산출물 있음**\n"
        f"→ `docs/planning/ROADMAP.md` merged 버전 기준 회귀·통합 테스트 실행.\n"
        f"→ 실패·누락은 **`docs/qa/QA_FEEDBACK.md` Open** 에 기록 (템플릿 준수).\n"
        f"→ `{test_rel}` 에서 Maven/npm 결과를 docs/qa/TEST_REPORT.md 에 반영.\n"
        "→ transfer/ 체크리스트·매니페스트 갱신.\n"
        f"→ `{develop_rel}`·`{test_rel}` 소스 수정 금지 — planner 가 QA_FEEDBACK 을 기획에 반영."
    )


def _ux_progress_hint() -> str:
    design = DESIGN_SYSTEM_FILE
    frontend = WORKSPACE_ROOT / "src/frontend"
    tokens = frontend / "src/styles/tokens.css"
    components = frontend / "src/styles/components.css"
    ui_dir = frontend / "src/components/ui"

    if not design.exists():
        return (
            "현재 진행: **DESIGN_SYSTEM.md 미작성**\n"
            "→ `docs/product/DESIGN_SYSTEM.md` 초안: 색상·타이포·간격 토큰, WCAG AA, 터치 44px.\n"
            "→ REQUIREMENTS·USER_STORIES·FLOWCHART 기반 React 컴포넌트 가이드."
        )
    if not tokens.exists() or not components.exists():
        return (
            "현재 진행: **디자인 문서 있음 — CSS 토큰 미작성**\n"
            "→ `src/frontend/src/styles/tokens.css`, `components.css` 생성.\n"
            "→ submodule frontend/develop 브랜치에서 작업."
        )
    if not ui_dir.exists() or not any(ui_dir.iterdir()):
        return (
            "현재 진행: **토큰 있음 — 공통 UI 컴포넌트 미작성**\n"
            "→ `src/frontend/src/components/ui/` Button, Input, Card 등 초안."
        )
    return (
        "현재 진행: **기본 디자인 시스템 있음**\n"
        "→ USER_STORIES·FLOWCHART 대비 누락 화면·컴포넌트 보강.\n"
        "→ 접근성(ARIA, 대비) 재점검."
    )


def _security_progress_hint() -> str:
    outputs = {
        "SECURITY_AUDIT.md": "OWASP Top 10 기반 취약점 점검 결과",
        "SECURITY_CHECKLIST.md": "배포 전 보안 체크리스트",
        "THREAT_MODEL.md": "STRIDE 위협 모델",
    }
    missing = [name for name in outputs if not (SECURITY_DIR / name).exists()]
    if missing:
        first = missing[0]
        return (
            f"현재 진행: **{len(missing)}개 보안 문서 미작성**\n"
            f"→ 지금 즉시 `docs/security/{first}` 초안 작성 ({outputs[first]}).\n"
            "→ src/backend(Java Spring), src/frontend(React) 코드·설정 점검.\n"
            "→ Maven dependency-check 또는 npm audit 결과 요약 포함.\n"
            "→ src/ 코드 **수정 금지**, docs/SECURITY_*.md 만 갱신."
        )
    return (
        "현재 진행: **기본 보안 문서 있음 — 일일 재점검**\n"
        "→ 최근 src/ 변경·의존성·JWT/RBAC·PII 처리 재검토.\n"
        "→ docs/security/SECURITY_AUDIT.md 에 신규/미해결 이슈 추가.\n"
        "→ BLOCK 이슈는 docs/qa/QA_FEEDBACK.md Open 에 `[SEC]` 항목으로 기록."
    )


def _build_security_auditor_prompt(task: str | None = None) -> str:
    rules = must_read(RULES_FILE)
    progress = _security_progress_hint()
    task_block = (
        f"## 이번 build 명시 작업\n{task.strip()}\n"
        if task and task.strip()
        else progress
    )
    return (
        f"=== .agents/rules.md ===\n{rules}\n\n"
        "지금 너의 역할은 `.agents/agents.yaml` 의 `security_auditor` 이다.\n\n"
        f"{_doc_identity_block('security_auditor')}\n"
        "## 0. 범위\n"
        "- **docs/SECURITY_*.md 만** 작성·갱신. src/ 코드 변경 **금지**.\n"
        "- Java Spring Boot + React + PostgreSQL 스택 기준 OWASP Top 10 점검.\n"
        "- Maven(`src/backend`)·npm(`src/frontend`) 의존성 취약점 스캔 결과 요약.\n\n"
        "## 1. 자율 실행 (필수)\n"
        "- 사용자 질문 금지. 이번 호출에서 docs/ 보안 문서를 반드시 생성·수정.\n"
        "- 치명적 이슈는 `docs/qa/QA_FEEDBACK.md` Open 에 `[SEC]` prefix 로 기록.\n"
        "- 불확실하면 `docs/planning/PLAN_NOTES.md` `### 보안 감사 질문` 에 기록 후 중단.\n\n"
        f"{task_block}\n\n"
        "## 2. 읽을 자료\n"
        "- src/backend/, src/frontend/ (읽기 전용)\n"
        "- docs/ops/DATA_RETENTION_POLICY.md, docs/technical/API_SPEC.md, docs/planning/REQUIREMENTS.md\n"
        "- docs/security/SECURITY_AUDIT.md 등 기존 보안 문서\n\n"
        "## 3. 출력 위치\n"
        "- docs/security/SECURITY_AUDIT.md\n"
        "- docs/security/SECURITY_CHECKLIST.md\n"
        "- docs/security/THREAT_MODEL.md\n\n"
        "## 4. 최종 응답 포맷\n"
        "  ## 보안 감사 작업 요약\n"
        "  - 점검 범위 (backend/frontend)\n"
        "  - 신규·미해결 취약점 (severity)\n"
        "  - QA_FEEDBACK Open 에 기록한 [SEC] 항목\n"
        "  - coder/planner 에게 전달할 조치\n"
    )


def _build_ux_designer_prompt(task: str | None = None) -> str:
    rules = must_read(RULES_FILE)
    progress = _ux_progress_hint()
    task_block = (
        f"## 이번 build 명시 작업\n{task.strip()}\n"
        if task and task.strip()
        else progress
    )
    develop_branch = branch_for_stream("frontend", "develop")
    return (
        f"=== .agents/rules.md ===\n{rules}\n\n"
        "지금 너의 역할은 `.agents/agents.yaml` 의 `ux_designer` 이다.\n\n"
        f"{_doc_identity_block('ux_designer')}\n"
        "## 0. 브랜치·범위 (CRITICAL)\n"
        f"- **submodule**: `src/frontend` | **브랜치**: `{develop_branch}`\n"
        "- React(Vite) + TypeScript 기반 UI·디자인 토큰만 작성.\n"
        "- `src/backend`, `transfer/` 수정 **금지**.\n"
        f"- 작업 후 **반드시** frontend @ `{develop_branch}` 에 **커밋**한다. "
        f"build 종료 시 `git push origin {develop_branch}` 자동 실행.\n\n"
        "## 1. 자율 실행 (필수)\n"
        "- 사용자 질문 금지. docs/product/DESIGN_SYSTEM.md 또는 frontend 스타일·UI 파일 생성·수정.\n"
        "- 불확실하면 `docs/planning/PLAN_NOTES.md` `### UX 설계 질문` 에 기록 후 중단.\n\n"
        f"{task_block}\n\n"
        "## 2. 읽을 문서\n"
        "- docs/planning/FLOWCHART.md, docs/planning/USER_STORIES.md, docs/planning/REQUIREMENTS.md\n"
        "- docs/product/DESIGN_SYSTEM.md (있으면 갱신)\n\n"
        "## 3. 출력 위치\n"
        "- docs/product/DESIGN_SYSTEM.md\n"
        "- src/frontend/src/styles/tokens.css, components.css\n"
        "- src/frontend/src/components/ui/\n\n"
        "## 4. 최종 응답 포맷\n"
        "  ## UX 설계 작업 요약\n"
        f"  - 브랜치: frontend/{develop_branch}\n"
        "  - 생성/수정한 파일\n"
        "  - 접근성·디자인 결정\n"
        "  - coder 에게 전달할 구현 메모\n"
    )


def _build_tester_prompt(stream: str = "backend", task: str | None = None) -> str:
    rules = must_read(RULES_FILE)
    progress = _tester_test_hint(stream)
    task_block = (
        f"## 이번 build 명시 작업\n{task.strip()}\n"
        if task and task.strip()
        else progress
    )
    test_branch = branch_for_stream(stream, "test")
    develop_branch = branch_for_stream(stream, "develop")
    transfer = transfer_dir_for_stream(stream)
    develop_dir = submodule_dir_for_stream(stream)
    test_dir = worktree_dir_for_stream(stream, "test")
    try:
        develop_rel = develop_dir.relative_to(WORKSPACE_ROOT)
    except ValueError:
        develop_rel = develop_dir
    try:
        test_rel = test_dir.relative_to(WORKSPACE_ROOT)
    except ValueError:
        test_rel = test_dir

    return (
        f"=== .agents/rules.md ===\n{rules}\n\n"
        "지금 너의 역할은 `.agents/agents.yaml` 의 `tester`(QA·이관) 이다.\n"
        "agents.yaml tester 섹션과 `.agents/branches.yaml` 을 읽어라.\n\n"
        "## 0. 브랜치·범위 (CRITICAL)\n"
        f"- **현재 스트림**: `{stream}` | **검증 worktree**: `{test_rel}` | **브랜치**: `{test_branch}`\n"
        f"- `{test_rel}` (git worktree) 에서 이관·검증·Maven/npm 테스트 실행.\n"
        f"- develop 산출물은 `{develop_rel}` (`{develop_branch}`) — **읽기만**, 수정·checkout **금지**.\n"
        f"- **수정 허용**: `transfer/{stream}/`, `docs/qa/TEST_REPORT.md`, `docs/qa/QA_FEEDBACK.md`, `tests/`.\n"
        f"- `{develop_rel}` 패치·브랜치 전환 **금지** (coder 와 worktree 분리).\n\n"
        f"{_doc_identity_block('tester')}\n"
        "## 1. 자율 실행 (필수)\n"
        "- `docs/planning/ROADMAP.md` merged 버전 기준으로 회귀·통합 테스트 실행.\n"
        "- **실패·누락·불일치**는 `docs/qa/QA_FEEDBACK.md` **Open** 섹션에 기록 "
        "(템플릿·severity·version 포함) — **planner 가 기획 반영**.\n"
        "- develop → test 이관 체크리스트·매니페스트·검증 리포트 갱신.\n"
        f"- `{'Maven' if stream == 'backend' else 'npm'}` 테스트는 `{test_rel}` 에서 실행·결과 기록.\n"
        "- BLOCK 이슈 있으면 transfer/ 체크리스트에 PASS 금지 명시.\n"
        "- 불확실하면 `docs/planning/PLAN_NOTES.md` `### QA 이관 질문` 에 기록 후 중단.\n\n"
        "## 1-1. 파이프라인 속도 (CRITICAL)\n"
        "- **문서만 갱신하는 긴 사이클 금지** — develop WT가 DIRTY·Open QA가 남았는데 "
        "TEST_REPORT 1000줄만 다시 쓰지 말 것.\n"
        "- develop에 **미커밋 구현**이 있으면: merge 스킵 + QA_FEEDBACK에 coder BLOCK 1건 "
        "(무엇을 커밋해야 하는지)만 추가해도 됨 — Opus 장문 리포트보다 **coder 압박**이 우선.\n"
        "- `docs/qa/QA_FEEDBACK.md` Open이 있으면 TEST_REPORT보다 **재현·severity·담당 stream** "
        "명확화가 우선.\n\n"
        "## 1-2. post-merge live E2E (결정 96)\n"
        "- **frontend** `merge_status: ready` → develop→test merge 성공 시 "
        "`scripts/run-live-e2e.sh` 가 **자동 실행**된다 (백엔드 `localhost:8080` 필요).\n"
        "- 실패 시 Open 항목이 자동 추가됨 — TEST_REPORT에 결과 요약·재현 절차 기록.\n"
        "- merge가 없었으면 live E2E는 스킵(정상).\n\n"
        f"{task_block}\n\n"
        "## 2. 읽을 자료\n"
        "- docs/planning/ROADMAP.md (검증 대상 버전·완료 기준)\n"
        "- docs/planning/USER_STORIES.md, docs/technical/API_SPEC.md, docs/planning/REQUIREMENTS.md\n"
        f"- {test_rel}/ (읽기 전용 — test 브랜치 산출물, worktree)\n"
        f"- {develop_rel}/ (읽기 전용 — develop 대비 diff 참고)\n"
        f"- {transfer}/ (이관 산출물)\n\n"
        "## 3. 출력 위치\n"
        f"- transfer/{stream}/checklists/test.md\n"
        f"- transfer/{stream}/manifests/latest.yaml\n"
        f"- transfer/{stream}/packages/ (diff·빌드 메타)\n"
        "- docs/qa/TEST_REPORT.md\n"
        "- docs/qa/QA_FEEDBACK.md (Open — 미해결 이슈)\n"
        "- tests/ (회귀 테스트 추가·수정 가능)\n\n"
        "## 4. 최종 응답 포맷\n"
        "  ## QA 이관 작업 요약\n"
        f"  - 브랜치: {test_branch}\n"
        "  - 이관 가능 여부 (PASS/BLOCK)\n"
        "  - QA_FEEDBACK Open 항목 수·severity\n"
        "  - 갱신한 transfer/·TEST_REPORT·QA_FEEDBACK\n"
        "  - planner 에게 전달할 핵심 수정 요청\n"
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
    if role == "ux_designer":
        return _build_ux_designer_prompt(task=task)
    if role == "security_auditor":
        return _build_security_auditor_prompt(task=task)
    raise ValueError(f"unknown role: {role}")


def _role_watched_paths(role: str, target: Path, stream: str = "backend") -> list[Path]:
    paths: set[Path] = set()
    if role == "coder":
        paths.update(_build_watched_paths(target))
        paths.update(_build_watched_paths(WORKSPACE_ROOT / "src/frontend"))
        for doc in (ROADMAP_FILE, QA_FEEDBACK_FILE):
            paths.add(doc)
    elif role == "db_architect":
        for path in (ERD_FILE, DATA_RETENTION_POLICY_FILE):
            paths.add(path)
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
            paths.add(OPS_DIR / name)
    elif role == "benchmark_researcher":
        for path in (
            BENCHMARK_REPORT_FILE,
            COMPETITOR_MATRIX_FILE,
            SNAPSHOTS_README_FILE,
            REQUIREMENTS_FILE,
            PLAN_NOTES_FILE,
            DECISIONS_FILE,
        ):
            paths.add(path)
        if SNAPSHOTS_DIR.is_dir():
            for html in SNAPSHOTS_DIR.glob("*.html"):
                paths.add(html)
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
            ROADMAP_FILE,
            QA_FEEDBACK_FILE,
            TEST_REPORT_FILE,
        ):
            paths.add(path)
    elif role == "tester":
        transfer = transfer_dir_for_stream(stream)
        if transfer.is_dir():
            for p in transfer.rglob("*"):
                if p.is_file():
                    paths.add(p)
        for doc in (TEST_REPORT_FILE, QA_FEEDBACK_FILE, ROADMAP_FILE):
            paths.add(doc)
        tests_root = WORKSPACE_ROOT / "tests"
        if tests_root.is_dir():
            for p in tests_root.rglob("*"):
                if p.is_file():
                    paths.add(p)
    elif role == "ux_designer":
        for path in (
            DESIGN_SYSTEM_FILE,
            WORKSPACE_ROOT / "src/frontend/src/styles/tokens.css",
            WORKSPACE_ROOT / "src/frontend/src/styles/components.css",
            WORKSPACE_ROOT / "src/frontend/src/components/ui",
        ):
            if path.is_dir():
                for p in path.rglob("*"):
                    if p.is_file():
                        paths.add(p)
            else:
                paths.add(path)
    elif role == "security_auditor":
        for name in ("SECURITY_AUDIT.md", "SECURITY_CHECKLIST.md", "THREAT_MODEL.md"):
            paths.add(SECURITY_DIR / name)
        paths.add(QA_FEEDBACK_FILE)
    paths.add(PLAN_NOTES_FILE)
    return sorted(paths)


def approval_present() -> bool:
    if not REQUIREMENTS_FILE.exists():
        return False
    return APPROVAL_MARKER in REQUIREMENTS_FILE.read_text(encoding="utf-8")


def _role_default_interval(role: str) -> int:
    if role == "tech_writer":
        return DEFAULT_WRITER_INTERVAL
    if role == "security_auditor":
        return DEFAULT_SECURITY_INTERVAL
    if role == "benchmark_researcher":
        return DEFAULT_BENCHMARK_INTERVAL
    if role == "ux_designer":
        return DEFAULT_UX_INTERVAL
    if role == "tester":
        return DEFAULT_TESTER_INTERVAL
    if role == "planner":
        return DEFAULT_PLANNING_INTERVAL
    return DEFAULT_INTERVAL


def save_planner_session(
    agent_id: str,
    *,
    locked_model: str | None = None,
    model_locked: bool = False,
) -> None:
    AGENTS_DIR.mkdir(parents=True, exist_ok=True)
    payload: dict[str, object] = {"agent_id": agent_id}
    if model_locked and locked_model:
        payload["locked_model"] = locked_model
        payload["model_locked"] = True
    PLANNER_SESSION_FILE.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def load_planner_session() -> tuple[str | None, str | None, bool]:
    if not PLANNER_SESSION_FILE.exists():
        return None, None, False
    try:
        data = json.loads(PLANNER_SESSION_FILE.read_text(encoding="utf-8"))
        agent_id = data.get("agent_id")
        locked = data.get("locked_model")
        model_locked = bool(data.get("model_locked"))
        aid = agent_id if isinstance(agent_id, str) and agent_id else None
        lm = locked if isinstance(locked, str) and locked else None
        return aid, lm, model_locked and bool(lm)
    except Exception:
        return None, None, False


def planner_system_prompt() -> str:
    context = load_agents_context()
    return (
        f"{context}\n\n"
        "지금 너의 역할은 .agents/agents.yaml 의 `planner` 이다.\n"
        "원칙:\n"
        "- 사용자와 한국어로 대화하며 요구사항을 명확하게 다듬는다.\n"
        "- 매 턴 마지막에 다음에 답해야 할 질문을 1~3개로 명시한다.\n"
        "- 사용자의 답이 들어올 때마다 docs/planning/REQUIREMENTS.md 를 갱신한다.\n"
        f"- 사용자 승인 마커 `{APPROVAL_MARKER}` 는 절대로 추가하지 않는다 "
        "  (승인은 사용자가 직접 추가한다).\n"
        "- 미확정/추가 질문은 docs/planning/PLAN_NOTES.md 의 '### 추가 질문' 섹션에 누적한다.\n"
        "- docs/qa/QA_FEEDBACK.md 의 Open 항목을 읽고 ROADMAP·USER_STORIES·PLAN_NOTES "
        "('### QA 피드백 반영')에 반영한다.\n"
        "- docs/planning/ROADMAP.md 를 v1·v2… 단계별 로드맵으로 유지한다.\n"
        "- 벤치마크 산출물(docs/planning/research/BENCHMARK_REPORT.md, docs/planning/research/COMPETITOR_MATRIX.md)과 "
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
                    "→ docs/planning/PLAN_NOTES.md '### 코더 질문' 섹션을 확인하세요.",
                    title="변경 없음",
                    border_style="yellow",
                )
            )
        else:
            print("[빈 결과] 변경된 파일이 없습니다.")
            print("  → docs/planning/PLAN_NOTES.md '### 코더 질문' 섹션을 확인하세요.")
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


def _message_field_text(message: object) -> str:
    """AgentMessage.message 등에서 텍스트를 최대한 추출."""

    if message is None:
        return ""
    if isinstance(message, str):
        return message.strip()
    if isinstance(message, Mapping):
        for key in ("text", "content", "result"):
            val = message.get(key)
            if isinstance(val, str) and val.strip():
                return val.strip()
            if isinstance(val, list):
                parts: list[str] = []
                for item in val:
                    if isinstance(item, str) and item.strip():
                        parts.append(item.strip())
                    elif isinstance(item, Mapping):
                        t = item.get("text") or item.get("content")
                        if isinstance(t, str) and t.strip():
                            parts.append(t.strip())
                if parts:
                    return "\n".join(parts)
    text_attr = getattr(message, "text", None)
    if isinstance(text_attr, str) and text_attr.strip():
        return text_attr.strip()
    return ""


def _extract_run_text(run, agent) -> str:
    """Run.result 가 비어도 conversation/stream/messages 에서 텍스트를 수집."""

    primary = (getattr(run, "result", "") or "").strip()
    if primary:
        return primary

    try:
        waited = run.text() or ""
        if waited.strip():
            return waited.strip()
    except Exception:
        pass

    try:
        streamed = "".join(run.iter_text()).strip()
        if streamed:
            return streamed
    except Exception:
        pass

    try:
        for turn in reversed(run.conversation()):
            if turn.type != "agentConversationTurn":
                continue
            agent_turn = turn.turn
            steps = getattr(agent_turn, "steps", ()) or ()
            chunks: list[str] = []
            for step in steps:
                if getattr(step, "type", None) != "assistantMessage":
                    continue
                msg = getattr(step, "message", None)
                text = getattr(msg, "text", "") if msg is not None else ""
                if isinstance(text, str) and text.strip():
                    chunks.append(text.strip())
            if chunks:
                return "\n\n".join(chunks)
    except Exception:
        pass

    try:
        for msg in reversed(agent.list_messages()):
            text = _message_field_text(getattr(msg, "message", None))
            if text:
                return text
    except Exception:
        pass

    return ""


class PlanSendState:
    """plan 모드 send 시 모델 체인 폴백을 위해 가변 agent/model 인덱스를 보관."""

    __slots__ = (
        "agent",
        "agent_id",
        "chain",
        "model_idx",
        "api_key",
        "model_locked",
        "session_rebuilt",
    )

    def __init__(
        self,
        agent,
        agent_id: str,
        chain: list[str],
        model_idx: int,
        api_key: str,
    ) -> None:
        self.agent = agent
        self.agent_id = agent_id
        self.chain = chain
        self.model_idx = model_idx
        self.api_key = api_key
        self.model_locked = False
        self.session_rebuilt = False

    @property
    def active_model(self) -> str:
        return self.chain[self.model_idx]

    def begin_send(self, *, force_chain_walk: bool = False) -> None:
        """send 직전: 첫 연결(또는 강제)에만 체인 맨 위부터, 이후엔 고정 모델."""

        fresh = resolve_model_chain("planner")
        if fresh:
            # yaml 변경 반영. 잠금 전이면 idx 유지 가능, 잠금 후엔 active_model 이름으로 idx 재매칭
            prev = self.active_model if self.chain else None
            self.chain = fresh
            if self.model_locked and prev:
                try:
                    self.model_idx = fresh.index(prev)
                except ValueError:
                    self.model_idx = min(self.model_idx, len(fresh) - 1)
            elif not self.model_locked or force_chain_walk:
                self.model_idx = 0

        if force_chain_walk:
            self.model_locked = False
            self.model_idx = 0

    def lock_model(self) -> None:
        """한 번 성공한 모델을 세션 동안 유지."""

        self.model_locked = True
        save_planner_session(
            self.agent_id,
            locked_model=self.active_model,
            model_locked=True,
        )


def _looks_like_transient_send_error(message: str) -> bool:
    msg = (message or "").lower()
    return _looks_like_bridge_down(msg) or "internal error" in msg


def _looks_like_bridge_down(message: str) -> bool:
    msg = (message or "").lower()
    return (
        "connection refused" in msg
        or "bridge request failed" in msg
        or "client has been closed" in msg
    )


def _looks_like_bridge_restart_needed(message: str) -> bool:
    """bridge 프로세스 재시작이 필요한 오류 (Connection refused, bridge crash 등)."""

    msg = (message or "").lower()
    return (
        _looks_like_bridge_down(msg)
        or "bridge exited" in msg
        or "tool-callback" in msg
        or "cursor-sdk-bridge failed" in msg
    )


def _plan_send_resilient(
    plan_state: PlanSendState | None,
    agent,
    message: str,
    *,
    model_id: str | None,
    label: str,
) -> tuple[str, str, str, str]:
    """plan send: bridge 끊김 시 즉시 재연결, send 실패 시 충분히 재시도."""

    bridge_recoveries = 0
    post_bridge_internal = 0
    last_err: Exception | None = None

    for attempt in range(PLAN_SEND_RETRY_MAX + 1):
        active = plan_state.agent if plan_state else agent
        try:
            return _plan_raw_send(active, message, model_id=model_id)
        except RuntimeError as err:
            last_err = err
            msg = str(err)
            if (
                _looks_like_bridge_restart_needed(msg)
                and bridge_recoveries < BRIDGE_RECOVER_MAX
            ):
                bridge_recoveries += 1
                print(
                    f"[recover] bridge 재시작 ({bridge_recoveries}/{BRIDGE_RECOVER_MAX}) "
                    f"— {msg[:80]}",
                    file=sys.stderr,
                )
                _recover_plan_bridge(plan_state, restart_bridge=True)
                time.sleep(BRIDGE_RECOVER_DELAY * bridge_recoveries)
                continue
            raise
        except CursorAgentError as err:
            last_err = err
            msg = err.message or ""
            if (
                _looks_like_bridge_restart_needed(msg)
                and bridge_recoveries < BRIDGE_RECOVER_MAX
            ):
                bridge_recoveries += 1
                print(
                    f"[recover] bridge 재시작 ({bridge_recoveries}/{BRIDGE_RECOVER_MAX}) "
                    f"— {msg[:80]}",
                    file=sys.stderr,
                )
                _recover_plan_bridge(plan_state, restart_bridge=True)
                time.sleep(BRIDGE_RECOVER_DELAY * bridge_recoveries)
                post_bridge_internal = 0
                continue
            if (
                "internal error" in msg.lower()
                and post_bridge_internal < BRIDGE_POST_INTERNAL_RETRY
            ):
                post_bridge_internal += 1
                delay = RETRY_BASE_DELAY * post_bridge_internal
                print(
                    f"[retry] {label} API 일시 오류 "
                    f"({post_bridge_internal}/{BRIDGE_POST_INTERNAL_RETRY}) "
                    f"delay={delay:.1f}s",
                    file=sys.stderr,
                )
                time.sleep(delay)
                continue
            if getattr(err, "is_retryable", False) and attempt < PLAN_SEND_RETRY_MAX:
                retry_after = getattr(err, "retry_after", None)
                if isinstance(retry_after, (int, float)) and retry_after > 0:
                    delay = float(retry_after)
                else:
                    delay = RETRY_BASE_DELAY * (2 ** min(attempt, 4))
                print(
                    f"[retry] {label} attempt={attempt + 1}/{PLAN_SEND_RETRY_MAX} "
                    f"delay={delay:.1f}s reason={msg[:120]}",
                    file=sys.stderr,
                )
                time.sleep(delay)
                continue
            raise
    if last_err is not None:
        raise last_err
    raise RuntimeError("plan send retry exhausted")


def _recover_plan_bridge(
    state: PlanSendState | None = None,
    *,
    restart_bridge: bool = True,
) -> None:
    """plan agent 를 resume 으로 재연결한다.

    `restart_bridge=True` 일 때만 bridge 프로세스를 죽였다 다시 띄운다.
    internal error 마다 bridge 를 재시작하면 tool-callback 서버가 깨질 수 있다.
    """

    if restart_bridge:
        _recover_build_bridge(restart=True)
    if state is None:
        return
    try:
        state.agent = Agent.resume(
            state.agent_id,
            AgentOptions(api_key=state.api_key, model=state.active_model),
        )
    except CursorAgentError as err:
        print(
            f"[recover-fail] agent resume 실패: {err.message!s:.120}",
            file=sys.stderr,
        )
        raise


def _is_stale_plan_agent_error(message: str) -> bool:
    return "internal error" in (message or "").lower()


def _recreate_plan_agent(state: PlanSendState) -> None:
    """cloud 쪽 agent 세션이 깨졌을 때 새 agent 를 만든다 (로컬 docs 는 유지)."""

    model = state.active_model
    print(
        f"[recover] cloud agent 손상 — 새 agent 생성 (model={model}). "
        "REQUIREMENTS/PLAN_NOTES 는 디스크에 그대로.",
        file=sys.stderr,
    )
    try:
        close_default_client()
    except Exception:
        pass
    _recover_build_bridge(restart=True)
    new_agent = Agent.create(
        api_key=state.api_key,
        model=model,
        local=LocalAgentOptions(cwd=str(WORKSPACE_ROOT)),
    )
    state.agent = new_agent
    state.agent_id = new_agent.agent_id
    state.model_locked = False
    state.session_rebuilt = True
    save_planner_session(state.agent_id)


def _ensure_plan_agent_alive(state: PlanSendState) -> None:
    """resume 직후 짧은 send 로 cloud agent 가 살아있는지 확인."""

    try:
        run = state.agent.send("ping", SendOptions(model=state.active_model))
        status = str(getattr(run, "status", "") or "")
        if status == "error":
            raise CursorAgentError("run status=error on probe", status=500, code="internal")
    except CursorAgentError as err:
        if _is_stale_plan_agent_error(err.message or ""):
            _recreate_plan_agent(state)
            return
        raise


def _plan_raw_send(
    agent, message: str, model_id: str | None = None
) -> tuple[str, str, str, str]:
    """send 1회 실행. (text, status, run_id, error_detail) 반환."""

    send_opts = SendOptions(model=model_id) if model_id else None
    run = agent.send(message, send_opts)
    text = _extract_run_text(run, agent)
    status = str(getattr(run, "status", "?") or "?")
    run_id = str(getattr(run, "id", "?") or "?")
    err_detail = (getattr(run, "result", "") or "").strip()
    if status == "error" and not err_detail:
        try:
            for turn in run.conversation():
                steps = getattr(getattr(turn, "turn", None), "steps", ()) or ()
                for step in steps:
                    if getattr(step, "type", None) != "statusMessage":
                        continue
                    msg = getattr(step, "message", None)
                    body = getattr(msg, "message", "") if msg is not None else ""
                    if isinstance(body, str) and body.strip():
                        err_detail = body.strip()
                        break
                if err_detail:
                    break
        except Exception:
            pass
    return text, status, run_id, err_detail


def _advance_plan_model(state: PlanSendState) -> bool:
    """체인에서 다음 모델로 전환. 성공 시 True, 더 이상 없으면 False.

    같은 agent 세션을 유지하고 다음 send 에 model override 만 넘긴다.
    (Agent.close + resume 은 로컬 bridge 를 끊어 Connection refused 를 유발할 수 있음)
    """

    next_idx = state.model_idx + 1
    if next_idx >= len(state.chain):
        return False
    model_id = state.chain[next_idx]
    state.model_idx = next_idx
    print(
        f"[fallback] planner send → model={model_id} "
        f"({next_idx + 1}/{len(state.chain)})",
        file=sys.stderr,
    )
    return True


def _plan_fallback_with_bridge(state: PlanSendState, *, reason: str = "") -> bool:
    """다음 모델로 넘긴다. bridge crash/refused 일 때만 bridge 재시작."""

    if _looks_like_bridge_restart_needed(reason):
        print(
            f"[recover] bridge crash/refused — 재시작 후 다음 모델 ({reason!s:.60})",
            file=sys.stderr,
        )
        try:
            _recover_plan_bridge(state, restart_bridge=True)
            time.sleep(BRIDGE_RECOVER_DELAY)
        except CursorAgentError as err:
            print(f"[recover-warn] {err.message!s:.80}", file=sys.stderr)
    return _advance_plan_model(state)


def _probe_planner_model(api_key: str, model_id: str) -> bool:
    """최소 ping 으로 SDK run 가능 여부 확인 (기획자 대화 세션과 분리)."""

    try:
        t0 = time.time()
        result = Agent.prompt(
            "Reply with exactly: ok",
            AgentOptions(
                api_key=api_key,
                model=model_id,
                local=LocalAgentOptions(cwd=str(WORKSPACE_ROOT)),
            ),
        )
        dt = time.time() - t0
        ok = str(getattr(result, "status", "") or "") == "finished"
        print(
            f"[probe] {model_id:24s} {'OK' if ok else 'ERR':<4s} time={dt:.1f}s",
            file=sys.stderr,
        )
        return ok
    except CursorAgentError as err:
        print(
            f"[probe] {model_id:24s} FAIL {err.message!s:.100}",
            file=sys.stderr,
        )
        return False


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
    plan_state: PlanSendState | None = None,
) -> None:
    """에이전트에게 메시지를 보내고 응답을 렌더링한다.

    - 일시적 브리지/네트워크 오류는 자동 재시도한다.
    - plan_state 가 주어지면 **세션 첫 send** 에만 체인 맨 위(고급)부터 확인하고,
      성공 후에는 같은 모델을 유지한다.
    - watch_before 가 주어지면 전송 전후 docs 변경을 함께 표시한다.
    """

    current_message = message
    last_send_error = ""

    for chain_pass in range(PLAN_CHAIN_PASS_MAX):
        if plan_state is not None:
            force_walk = chain_pass > 0 and not plan_state.model_locked
            plan_state.begin_send(force_chain_walk=force_walk)
            if chain_pass > 0:
                print(
                    f"[recover] 체인 전체 실패 — bridge 재시작 후 "
                    f"{chain_pass + 1}/{PLAN_CHAIN_PASS_MAX}회차 재시도",
                    file=sys.stderr,
                )
                _recover_plan_bridge(plan_state, restart_bridge=True)
                time.sleep(BRIDGE_RECOVER_DELAY * 2)
            if plan_state.model_locked:
                print(
                    f"[chain] 세션 고정 모델: {plan_state.active_model}",
                    file=sys.stderr,
                )
            else:
                print(
                    f"[chain] 첫 연결 — agents.yaml 체인: {' → '.join(plan_state.chain)}",
                    file=sys.stderr,
                )

        same_model_retry = False
        internal_streak = 0

        while True:
            active_model = plan_state.active_model if plan_state else "?"
            has_next = (
                plan_state is not None
                and plan_state.model_idx < len(plan_state.chain) - 1
            )
            mid = plan_state.active_model if plan_state else None
            label = f"plan send model={active_model}"

            if plan_state is not None and PLAN_PROBE_BEFORE_SEND and not plan_state.model_locked:
                if not _probe_planner_model(plan_state.api_key, active_model):
                    if has_next:
                        nxt = plan_state.chain[plan_state.model_idx + 1]
                        print(
                            f"[chain] {active_model} 가용하지 않음 → {nxt} 시도",
                            file=sys.stderr,
                        )
                        if _advance_plan_model(plan_state):
                            continue
                    else:
                        print(
                            f"[chain] {active_model} probe FAIL — "
                            "마지막 모델, send 그대로 시도",
                            file=sys.stderr,
                        )
                else:
                    print(
                        f"[chain] {active_model} probe OK — 본문 send 시작",
                        file=sys.stderr,
                    )

            try:
                if _RICH and _CONSOLE is not None:
                    with _CONSOLE.status(
                        f"[bold cyan]기획자 생각 중 ({active_model})...[/bold cyan]",
                        spinner="dots",
                    ):
                        text, status, run_id, err_detail = _plan_send_resilient(
                            plan_state,
                            agent,
                            current_message,
                            model_id=mid,
                            label=label,
                        )
                else:
                    sys.stdout.write(f"  (기획자 생각 중 — {active_model}...)")
                    sys.stdout.flush()
                    text, status, run_id, err_detail = _plan_send_resilient(
                        plan_state,
                        agent,
                        current_message,
                        model_id=mid,
                        label=label,
                    )
                    sys.stdout.write("\r" + " " * 40 + "\r")
                    sys.stdout.flush()
            except CursorAgentError as err:
                msg = err.message or ""
                last_send_error = msg
                if (
                    plan_state is not None
                    and not same_model_retry
                    and _looks_like_bridge_restart_needed(msg)
                ):
                    same_model_retry = True
                    print(
                        f"[recover] {active_model} bridge 오류 — 재시작 후 같은 모델 재시도",
                        file=sys.stderr,
                    )
                    _recover_plan_bridge(plan_state, restart_bridge=True)
                    time.sleep(BRIDGE_RECOVER_DELAY)
                    continue
                same_model_retry = False
                if "internal error" in msg.lower():
                    internal_streak += 1
                    if internal_streak >= PLAN_INTERNAL_ABORT_STREAK:
                        print(
                            "[abort] 연속 internal error — Cursor API/bridge 전역 장애로 "
                            "판단, 남은 모델 시도 중단",
                            file=sys.stderr,
                        )
                        last_send_error = msg
                        break
                if has_next:
                    print(
                        f"[fallback] planner model={active_model} send 실패 → "
                        f"{plan_state.chain[plan_state.model_idx + 1]}  "
                        f"reason={msg!s:.120}",
                        file=sys.stderr,
                    )
                    if _plan_fallback_with_bridge(plan_state, reason=msg):
                        continue
                break
            except Exception:
                print("[unexpected-error]", file=sys.stderr)
                traceback.print_exc()
                return

            if status == "error":
                last_send_error = err_detail or "run status=error"
                if err_detail:
                    short = err_detail[:800] + ("…" if len(err_detail) > 800 else "")
                    print(
                        f"[run-error-detail] model={active_model} {short}",
                        file=sys.stderr,
                    )
                else:
                    print(
                        f"[info] run status=error id={run_id} model={active_model}",
                        file=sys.stderr,
                    )
                if has_next:
                    print(
                        f"[fallback] planner model={active_model} run-error → "
                        f"{plan_state.chain[plan_state.model_idx + 1]}",
                        file=sys.stderr,
                    )
                    internal_streak += 1
                    if internal_streak >= PLAN_INTERNAL_ABORT_STREAK:
                        print(
                            "[abort] 연속 run-error/internal — 남은 모델 시도 중단",
                            file=sys.stderr,
                        )
                        break
                    if _plan_fallback_with_bridge(plan_state, reason=last_send_error):
                        same_model_retry = False
                        continue
                break
            elif not text.strip():
                print(
                    f"[info] run status={status} id={run_id} — "
                    "assistant 텍스트 없음 (파일 수정만 했을 수 있음)",
                    file=sys.stderr,
                )

            if watch_before is not None:
                changes = diff_snapshots(watch_before, _watched_paths())
                if not text.strip() and changes:
                    note = (
                        "기획자가 채팅 텍스트는 비웠지만 아래 파일을 변경했습니다.\n"
                        "  → `:show` 로 REQUIREMENTS 확인, 또는 diff 로 내용 검토"
                    )
                    if _RICH and _CONSOLE is not None:
                        _CONSOLE.print(
                            Panel(note, title="파일 변경됨", border_style="yellow")
                        )
                    else:
                        print(note)
                    render_file_changes(changes)
                    return

            if plan_state is not None:
                plan_state.lock_model()
                print(f"[chain] 답변 모델: {active_model} (세션 고정)", file=sys.stderr)
            render_agent_output(text, title=f"기획자 ({active_model})")

            if not text.strip():
                hint = (
                    "텍스트 응답이 없습니다. 시도:\n"
                    "  1) `:show` — REQUIREMENTS 가 갱신됐는지 확인\n"
                    "  2) 짧은 질문으로 다시 입력\n"
                    "  3) `AGENT_PLAN_PROBE=0 plan --resume` (probe 끄기)\n"
                    "  4) 새 세션: plan --new"
                )
                if status == "error":
                    hint = (
                        f"모델 `{active_model}` run 이 error 로 끝났습니다.\n" + hint
                    )
                if _RICH and _CONSOLE is not None:
                    _CONSOLE.print(
                        Panel(hint, title="빈 응답 복구", border_style="yellow")
                    )
                else:
                    print(hint)
                if watch_before is not None:
                    changes = diff_snapshots(watch_before, _watched_paths())
                    render_file_changes(changes)
                return

            if watch_before is not None:
                changes = diff_snapshots(watch_before, _watched_paths())
                render_file_changes(changes)
            return

        if chain_pass + 1 < PLAN_CHAIN_PASS_MAX:
            continue

    if (
        plan_state is not None
        and not plan_state.session_rebuilt
        and _is_stale_plan_agent_error(last_send_error)
    ):
        try:
            _recreate_plan_agent(plan_state)
            plan_state.begin_send(force_chain_walk=False)
            print("[recover] 새 agent 로 같은 메시지 재시도...", file=sys.stderr)
            return send_and_print(agent, message, watch_before=watch_before, plan_state=plan_state)
        except CursorAgentError as err:
            last_send_error = err.message or last_send_error

    if plan_state is not None:
        plan_state.model_locked = False
    print(
        f"[send-error] {PLAN_CHAIN_PASS_MAX}회차 체인 모두 실패 "
        f"message={last_send_error!s:.120}",
        file=sys.stderr,
    )
    hint = (
        "답변 실패. API 키/모델은 doctor 기준 정상일 수 있으나, "
        "저장된 cloud agent 세션이 손상된 경우가 많습니다.\n"
        "  → `plan --new` 로 새 agent (로컬 REQUIREMENTS 는 유지)\n"
        "  → 또는 위 [recover] 새 agent 생성 후 같은 질문 재입력\n"
        "  → `:show` 로 REQUIREMENTS 확인\n"
        "  → doctor: `.venv/bin/python scripts/run_agent.py doctor --ok-only`"
    )
    if _RICH and _CONSOLE is not None:
        _CONSOLE.print(Panel(hint, title="복구 안내", border_style="red"))
    else:
        print(hint, file=sys.stderr)


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
    "  :show                       현재 docs/planning/REQUIREMENTS.md 출력\n"
    "  :reload                     현재 docs/planning/REQUIREMENTS.md 를 기획자에게 다시 컨텍스트로 전달\n"
    "  :help                       이 도움말 표시\n"
)


def cmd_doctor(args: argparse.Namespace) -> None:
    """가용 모델에 최소 프롬프트를 보내서 어떤 모델/계정이 동작하는지 진단."""

    ok_only = getattr(args, "ok_only", False)
    api_key = require_api_key()
    masked = api_key[:6] + "..." + api_key[-4:]
    candidates = [
        # 서버가 "Available models" 로 공개한 풀 (2026-06). 계정 권한에
        # 따라 일부는 거절될 수 있다. 거절되면 서버가
        # "Cannot use this model. Available models: ..." 를 돌려준다.
        # 기본/자동 라우팅
        "default",
        "auto",
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
    # kind: RUN-OK | RUN-ERR | FAIL | CRASH
    try:
        for m in candidates:
            t0 = time.time()
            try:
                _recover_build_bridge()
                result = _build_agent_prompt(
                    "ping",
                    api_key=api_key,
                    model_id=m,
                    cwd=WORKSPACE_ROOT,
                )
                dt = time.time() - t0
                status = str(result.status or "?")
                detail = (getattr(result, "result", "") or "").strip()
                if detail:
                    short = detail[:80] + ("…" if len(detail) > 80 else "")
                else:
                    short = ""
                if status == "finished":
                    kind = "RUN-OK"
                    label = "RUN-OK"
                else:
                    kind = "RUN-ERR"
                    label = "RUN-ERR"
                extra = f" detail={short!s}" if short else ""
                if not ok_only or kind != "RUN-ERR":
                    print(
                        f"  {m:32s}  {label:<7s} status={status:<10s} time={dt:.1f}s{extra}"
                    )
                results.append((m, kind, status, None, detail))
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
                if not ok_only:
                    print(f"  {m:32s}  CRASH  {type(e).__name__}: {e} time={dt:.1f}s")
                results.append((m, "CRASH", None, type(e).__name__, str(e)))

    finally:
        _release_bridge_resources()

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

    ok_models = [m for m, kind, *_ in results if kind == "RUN-OK"]
    run_err_models = [m for m, kind, *_ in results if kind == "RUN-ERR"]
    fail_models = [m for m, kind, *_ in results if kind == "FAIL"]
    if ok_only and run_err_models:
        print(f"  (... RUN-ERR {len(run_err_models)}개 생략 — 전체는 doctor 만 실행)")
    if ok_models:
        print()
        print("[doctor] SDK 에서 실제 사용 가능 (RUN-OK, status=finished):")
        for m in ok_models:
            print(f"  - {m}")
        print()
        print("  agents.yaml model / fallback_models 는 위 목록 안에서만 구성하세요.")
    if run_err_models and not ok_only:
        print()
        print(
            "[doctor] API 호출은 됐지만 run status=error (plan/build 에서도 실패 가능):"
        )
        print("  " + ", ".join(run_err_models))

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


def cmd_prune_bridges(args: argparse.Namespace) -> None:
    """ogada workspace orphan cursor-sdk-bridge 프로세스 정리."""

    dry_run = bool(getattr(args, "dry_run", False))
    quiet = bool(getattr(args, "quiet", False))
    prune_orphan_bridges(dry_run=dry_run, quiet=quiet)


def cmd_bridge_status(_: argparse.Namespace) -> None:
    """bridge / run_agent 프로세스 현황 (htop 대조용)."""

    bridges = _iter_workspace_bridge_processes()
    agents = _active_run_agent_pids()
    orphans = 0
    managed = 0
    for info in bridges:
        pid = int(info["pid"])
        ppid = int(info["ppid"])
        if ppid in agents or _is_run_agent_ancestor(pid):
            managed += 1
            continue
        parent_cmd = _proc_cmdline(ppid) if ppid > 0 else None
        if ppid > 0 and parent_cmd and "run_agent.py" in parent_cmd:
            managed += 1
        else:
            orphans += 1

    print(f"workspace : {_workspace_path_token()}")
    print(f"bridges   : total={len(bridges)} managed={managed} orphan={orphans}")
    print(f"run_agent : active={len(agents)} PIDs={sorted(agents)}")
    owned = _owned_build_bridge_pid()
    if owned is not None:
        print(f"owned     : build_client bridge PID={owned}")


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
    print(f"ux_designer          : {resolve_model_chain('ux_designer')}")
    print(f"security_auditor     : {resolve_model_chain('security_auditor')}")
    print(f"tech_writer          : {resolve_model_chain('tech_writer')}")
    print(f"default              : {resolve_model_chain(None)}")
    bridges = _iter_workspace_bridge_processes()
    agents = _active_run_agent_pids()
    print(
        f"bridges              : {len(bridges)} process(es), "
        f"run_agent={len(agents)} "
        f"(prune: .venv/bin/python scripts/run_agent.py prune-bridges)"
    )
    if _git_repo_ready(WORKSPACE_ROOT):
        print(f"git root branch     : {_git_current_branch(WORKSPACE_ROOT) or '(detached)'}")
    for stream in ("backend", "frontend"):
        sub = submodule_dir_for_stream(stream)
        wt = worktree_dir_for_stream(stream, "test")
        if _git_repo_ready(sub):
            print(
                f"git {stream:8} dev   : "
                f"{_git_current_branch(sub) or '(detached)'} "
                f"({sub.relative_to(WORKSPACE_ROOT)})"
            )
            if _worktree_registered(sub, wt):
                print(
                    f"git {stream:8} test  : "
                    f"{_git_current_branch(wt) or '(detached)'} "
                    f"({wt.relative_to(WORKSPACE_ROOT)})"
                )
            else:
                print(
                    f"git {stream:8} test  : (worktree missing — "
                    f"run ./scripts/git_branch_setup.sh)"
                )
        else:
            print(f"git {stream:8}       : (no repo — run ./scripts/git_branch_setup.sh)")
    print(
        "branch policy: .agents/branches.yaml "
        "(develop=주 경로, test=worktree 분리)"
    )


def cmd_plan(args: argparse.Namespace) -> None:
    """기획자 에이전트와 멀티턴 대화를 수행한다.

    동작:
    - 새 세션은 .agents/.planner_session.json 에 agent_id 를 저장한다.
    - --resume 옵션을 주면 직전 세션을 이어 받아 대화한다.
    - 종료 키워드: :q, :exit, :quit, :bye (또는 Ctrl+D)
    """

    DOCS_DIR.mkdir(parents=True, exist_ok=True)
    PLAN_NOTES_FILE.parent.mkdir(parents=True, exist_ok=True)
    PLAN_NOTES_FILE.touch(exist_ok=True)
    api_key = require_api_key()
    setup_input_history()

    if getattr(args, "new", False) and PLANNER_SESSION_FILE.exists():
        PLANNER_SESSION_FILE.unlink()
        print("[info] 기존 planner 세션 파일을 삭제하고 새 세션으로 시작합니다.")

    planner_chain = resolve_model_chain("planner")

    prev_id, locked_model, was_locked = (
        load_planner_session() if args.resume else (None, None, False)
    )
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

    def handle_slash(line: str, plan_state: PlanSendState) -> bool:
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
                plan_state.agent,
                "다음은 현재 docs/planning/REQUIREMENTS.md 의 전체 내용이다. "
                "이 내용을 컨텍스트로 받아들이고, 모순/누락/추가 질문이 있으면 짚어 줘. "
                "코드는 작성하지 마라.\n\n"
                f"=== REQUIREMENTS.md ===\n{current}\n",
                watch_before=before,
                plan_state=plan_state,
            )
            return True
        return False

    try:
        agent_ctx, active_model = _open_with_chain()
        with agent_ctx as agent:
            try:
                model_idx = planner_chain.index(active_model)
            except ValueError:
                model_idx = 0
            plan_state = PlanSendState(
                agent=agent,
                agent_id=agent.agent_id,
                chain=planner_chain,
                model_idx=model_idx,
                api_key=api_key,
            )
            if was_locked and locked_model:
                try:
                    plan_state.model_idx = planner_chain.index(locked_model)
                    plan_state.model_locked = True
                    print(f"[session] 고정 모델 복원: {locked_model}", file=sys.stderr)
                except ValueError:
                    pass
            save_planner_session(agent.agent_id)
            if prev_id:
                try:
                    _ensure_plan_agent_alive(plan_state)
                except CursorAgentError as err:
                    print(f"[warn] planner 세션 probe: {err.message}", file=sys.stderr)
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
                if first_user.startswith(":"):
                    if handle_slash(first_user, plan_state):
                        pass
                    else:
                        print(f"[info] 알 수 없는 명령: {first_user}. :help 참고")
                else:
                    before = snapshot_files(_watched_paths())
                    send_and_print(
                        plan_state.agent,
                        f"{planner_system_prompt()}\n\n=== 사용자 첫 입력 ===\n{first_user}\n",
                        watch_before=before,
                        plan_state=plan_state,
                    )
                    if plan_state.active_model != active_model:
                        print(
                            f"[session] model={plan_state.active_model} "
                            "(send 폴백으로 전환됨)"
                        )

            while True:
                user_input = read_user_line("사용자: ")
                if user_input is None or user_input == EXIT_TOKEN:
                    print("[exit]")
                    break
                if user_input == "":
                    continue
                if user_input.startswith(":"):
                    if handle_slash(user_input, plan_state):
                        continue
                    print(f"[info] 알 수 없는 명령: {user_input}. :help 참고")
                    continue
                before = snapshot_files(_watched_paths())
                send_and_print(
                    plan_state.agent,
                    user_input,
                    watch_before=before,
                    plan_state=plan_state,
                )
    except CursorAgentError as err:
        print(
            f"[fatal] planner 세션 오류: retryable={err.is_retryable} message={err.message}",
            file=sys.stderr,
        )
        if _looks_like_bridge_down(err.message or ""):
            print(
                "[hint] bridge 끊김 → plan --resume 으로 같은 agent_id 에 재접속",
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
            "[blocked] docs/planning/REQUIREMENTS.md 에 사용자 승인 마커가 없습니다. "
            f"파일 끝에 `{APPROVAL_MARKER}` 를 추가한 뒤 다시 실행하세요.",
            file=sys.stderr,
        )
        sys.exit(3)

    target = (WORKSPACE_ROOT / args.target).resolve()
    stream = resolve_stream(args, target)

    if role in ("coder", "tester", "ux_designer"):
        ensure_role_branch(role, stream if role != "ux_designer" else "frontend")
        if role == "tester":
            target = transfer_dir_for_stream(stream)
        elif role == "ux_designer":
            target = WORKSPACE_ROOT / "src" / "frontend"
        elif stream == "frontend":
            target = WORKSPACE_ROOT / "src" / "frontend"
        else:
            target = WORKSPACE_ROOT / "src" / "backend"
    else:
        pass

    if role == "coder" and not target.exists():
        print(f"[fatal] 작업 대상이 존재하지 않습니다: {target}", file=sys.stderr)
        sys.exit(2)

    if role == "ux_designer" and not (WORKSPACE_ROOT / "src/frontend").exists():
        print(
            "[fatal] src/frontend submodule 이 없습니다.\n"
            "  git submodule update --init src/frontend\n"
            "  ./scripts/git_branch_setup.sh",
            file=sys.stderr,
        )
        sys.exit(2)

    if role == "coder":
        print_coder_preflight(stream)

    if role in AUTO_ROLES:
        DOCS_DIR.mkdir(parents=True, exist_ok=True)
        PLAN_NOTES_FILE.parent.mkdir(parents=True, exist_ok=True)
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

        try:
            if BRIDGE_PRUNE_ENABLED:
                prune_orphan_bridges(quiet=True)
            _recover_build_bridge()
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
                    f"{role} 가 docs/planning/PLAN_NOTES.md '### {question_marker}' 섹션에 "
                    "질문을 추가했습니다.\n"
                    "→ plan 모드에서 해결:\n"
                    "    .venv/bin/python scripts/run_agent.py plan --resume"
                )
                if _RICH and _CONSOLE is not None:
                    _CONSOLE.print(Panel(msg, title="확인 필요", border_style="red"))
                else:
                    print("[확인 필요]")
                    print(msg)

            if role in ("coder", "ux_designer"):
                push_submodule_develop(role, stream)

            print()
            print(f"[다음 단계] role={role}")
            if role == "coder":
                sub = submodule_dir_for_stream(stream)
                print(f"  - git -C {sub} status · develop 커밋 후 push (자동 push 시도 완료)")
            elif role == "tester":
                wt = worktree_dir_for_stream(stream, "test")
                print(f"  - {wt.relative_to(WORKSPACE_ROOT)} (test worktree) · transfer/{stream}/ 확인")
                print("  - docs/qa/TEST_REPORT.md · docs/qa/QA_FEEDBACK.md 확인")
                print("  - planner 자동 반영: agent_pipeline.sh")
                version_id = _roadmap_merge_ready(stream)
                merged = maybe_merge_version_to_test(stream)
                if merged:
                    rc = run_live_e2e_post_merge(stream, version_id=version_id)
                    if rc != 0:
                        print(
                            f"[warn] post-merge live E2E exit={rc} — docs/qa/QA_FEEDBACK.md 확인",
                            file=sys.stderr,
                        )
            elif role == "db_architect":
                print("  - docs/technical/ERD.md · db/migration SQL 확인")
            elif role == "benchmark_researcher":
                print("  - docs/planning/research/BENCHMARK_REPORT.md · docs/planning/research/COMPETITOR_MATRIX.md 확인")
                print("  - planner 자동 동기화: agent_pipeline.sh")
            elif role == "security_auditor":
                print("  - docs/security/SECURITY_AUDIT.md · SECURITY_CHECKLIST.md 확인")
                print("  - [SEC] QA_FEEDBACK Open 항목 → coder/planner 반영")
            elif role == "ux_designer":
                print("  - docs/product/DESIGN_SYSTEM.md · src/frontend/src/styles 확인")
            elif role == "planner":
                print("  - docs/planning/REQUIREMENTS.md · docs/planning/USER_STORIES.md · docs/planning/PLAN_NOTES.md 확인")
                print("  - 사용자 승인 전 plan --resume 으로 대화형 검토 권장")
            else:
                print("  - docs/ops/USER_MANUAL.md 등 문서 확인")
        finally:
            _release_bridge_resources()

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


def _iter_all_agents(api_key: str) -> list:
    page = Agent.list({"apiKey": api_key})
    items = list(page.items)
    while page.next_cursor:
        page = page.get_next_page()
        items.extend(page.items)
    return items


def cmd_cleanup_agents(_: argparse.Namespace) -> None:
    """running 상태 cloud agent 를 cancel → close → archive 로 정리."""

    api_key = require_api_key()
    opts = {"apiKey": api_key}
    resume_opts = AgentOptions(api_key=api_key)

    agents = _iter_all_agents(api_key)
    running = [
        a
        for a in agents
        if getattr(a, "status", None) == "running" and not getattr(a, "archived", False)
    ]
    if not running:
        print("[cleanup] running agent 없음.")
        return

    print(f"[cleanup] running agent {len(running)}개 정리 시도...")
    cancelled = closed = archived = failed = 0

    for info in running:
        aid = info.agent_id
        label = aid[:28]

        try:
            for run in Agent.list_runs(aid, opts):
                if getattr(run, "status", None) != "running":
                    continue
                try:
                    Agent.cancel_run(run.id, agent_id=aid)
                    print(f"  [cancel] {label} run={run.id[:20]}")
                    cancelled += 1
                except CursorAgentError as err:
                    print(f"  [cancel-skip] {label} {err.message!s:.80}")
        except CursorAgentError as err:
            print(f"  [list-runs-skip] {label} {err.message!s:.80}")

        try:
            Agent.resume(aid, resume_opts).close()
            closed += 1
        except CursorAgentError as err:
            print(f"  [close-skip] {label} {err.message!s:.80}")

        try:
            Agent.archive(aid, opts)
            print(f"  [archive] {label}")
            archived += 1
        except CursorAgentError as err:
            print(f"  [archive-fail] {label} {err.message!s:.80}")
            failed += 1

    if PLANNER_SESSION_FILE.exists():
        PLANNER_SESSION_FILE.unlink()
        print("[cleanup] .agents/.planner_session.json 삭제")

    remaining = [
        a.agent_id
        for a in _iter_all_agents(api_key)
        if getattr(a, "status", None) == "running" and not getattr(a, "archived", False)
    ]
    print(
        f"[cleanup] cancel={cancelled} close={closed} archive={archived} "
        f"archive_fail={failed} running_remaining={len(remaining)}"
    )
    if remaining:
        print("  남은 running:")
        for aid in remaining:
            print(f"    {aid}")
        print(
            "  → Cursor API 가 500 internal 이면 cloud 에서 상태가 안 바뀝니다.\n"
            "     doctor 가 RUN-OK 일 때 다시 실행하거나 Dashboard Cloud Agents 에서 확인."
        )


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
    p_doctor.add_argument(
        "--ok-only",
        action="store_true",
        help="RUN-OK 모델만 자세히 표시 (RUN-ERR 목록 생략)",
    )
    p_doctor.set_defaults(func=cmd_doctor)

    p_cleanup = sub.add_parser(
        "cleanup-agents",
        help="running 상태 cloud agent 정리 (cancel/close/archive)",
    )
    p_cleanup.set_defaults(func=cmd_cleanup_agents)

    p_prune = sub.add_parser(
        "prune-bridges",
        help="orphan cursor-sdk-bridge 프로세스 정리 (API 키 불필요)",
    )
    p_prune.add_argument(
        "--dry-run",
        action="store_true",
        help="종료할 PID만 출력하고 kill 하지 않음",
    )
    p_prune.add_argument("--quiet", action="store_true", help="요약만 출력")
    p_prune.set_defaults(func=cmd_prune_bridges)

    p_bridge = sub.add_parser(
        "bridge-status",
        help="bridge/run_agent 프로세스·orphan 현황",
    )
    p_bridge.set_defaults(func=cmd_bridge_status)

    p_build = sub.add_parser("build", help="구현/설계/문서 에이전트 (승인된 REQUIREMENTS 기반)")
    p_build.add_argument(
        "--role",
        default="coder",
        choices=sorted(ALL_BUILD_ROLES),
        help=(
            "에이전트 역할: coder(코드), db_architect(DB), tech_writer(문서), "
            "ux_designer(UX/UI), security_auditor(보안·1일1회), "
            "benchmark_researcher(경쟁사 벤치마크), "
            "planner(벤치마크 반영 자동 기획), "
            "tester(QA 이관 — submodule test·transfer/ 전용)"
        ),
    )
    p_build.add_argument(
        "--stream",
        choices=["backend", "frontend"],
        default=None,
        help="coder/tester 스트림: backend(기본) 또는 frontend. develop/test 브랜치 선택",
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
        help="--loop 반복 간격(초). 미지정 시 coder/db/ux/tester/planner/benchmark=1800, tech_writer=3600, security=86400",
    )
    p_build.add_argument("--loop", action="store_true", help="반복 실행")
    p_build.set_defaults(func=cmd_build)

    p_status = sub.add_parser("status", help="현재 상태 확인")
    p_status.set_defaults(func=cmd_status)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
