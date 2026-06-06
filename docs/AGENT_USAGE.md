# 에이전트 사용 가이드 (AGENT_USAGE.md)

> 이 문서는 `scripts/run_agent.py` 와 `scripts/agent_*.sh` 의 사용법을 정리한
> 단일 레퍼런스입니다. 새 멤버는 이 문서만 보면 운영할 수 있어야 합니다.

---

## 1. 구성 개요

```
ogada/
├── .agents/
│   ├── rules.md            # 모든 에이전트 공통 규칙 (강제 주입됨)
│   ├── agents.yaml         # 역할 정의 (planner/coder/...)
│   ├── .planner_session.json   # planner 세션 ID (자동 생성, gitignore)
│   └── .planner_history    # 입력 히스토리 (자동 생성, gitignore)
├── docs/
│   ├── REQUIREMENTS.md     # 기획자가 갱신하는 요구사항 명세
│   ├── PLAN_NOTES.md       # 미확정/추가 질문 누적
│   ├── BENCHMARK_REPORT.md # benchmark_researcher 경쟁사 분석
│   ├── COMPETITOR_MATRIX.md# 기능·서비스 비교 매트릭스
│   └── AGENT_USAGE.md      # (이 문서)
├── scripts/
│   ├── run_agent.py        # 메인 실행기 (plan / build / status)
│   ├── agent_start.sh      # tmux 시작 헬퍼
│   ├── agent_stop.sh       # 프로세스/세션 정리
│   ├── agent_status.sh     # 현재 상태 한눈에 보기
│   ├── agent_planning_start.sh   # benchmark + planner 3시간 loop
│   ├── agent_planning_status.sh
│   └── agent_planning_stop.sh
├── .env                    # CURSOR_API_KEY 등 (gitignore)
└── .venv/                  # Python 가상환경
```

---

## 2. 초기 설정 (한 번만)

```bash
# 가상환경 활성화
source .venv/bin/activate

# 의존성 설치 (이미 설치된 경우 생략)
pip install -r requirements.txt
```

`.env` 파일에는 다음이 있어야 합니다.

```
CURSOR_API_KEY=cursor_xxxxx
```

---

## 3. 모드 요약

| 모드     | 목적                              | 사용자 입력 | 코드 작성 |
|----------|----------------------------------|------------|----------|
| `plan`   | 기획자와 대화로 요구사항 확정      | 대화형      | ❌       |
| `build`  | 승인된 요구사항 기반 코드 작성     | 거의 없음   | ✅ (coder 등) |
| `build`  | 벤치마크·자동 기획 (benchmark/planner) | 없음 | ❌ (docs만) |
| `status` | 현재 상태 표시 (승인/세션/프로세스)| 없음        | ❌       |

`build`는 `docs/REQUIREMENTS.md` 끝에 다음 줄이 있어야만 실행됩니다.

```
<!-- approved-by-user: true -->
```

---

## 4. 모드별 사용법

### 4.1 plan — 기획자 모드 (멀티턴 대화)

기획자가 사용자에게 질문하면서 `docs/REQUIREMENTS.md` 를 갱신합니다.
미확정/추가 질문은 `docs/PLAN_NOTES.md` 의 `### 추가 질문` 섹션에 누적됩니다.

```bash
# 처음 시작
.venv/bin/python scripts/run_agent.py plan

# 첫 입력을 인자로 전달 (이후 대화는 그대로 이어짐)
.venv/bin/python scripts/run_agent.py plan --brief "주간보호센터 운영 웹"
```

#### 세션 이어서 대화하기 (resume)

`plan` 을 시작하면 세션 ID 가 자동으로 저장됩니다.

```
.agents/.planner_session.json
```

다음에 같은 대화 맥락을 이어가려면 `--resume` 을 붙입니다.

```bash
# 직전 planner 세션을 이어서 대화
.venv/bin/python scripts/run_agent.py plan --resume
```

동작 규칙:

- `--resume` 을 주었는데 세션 파일이 없으면 자동으로 새 세션을 시작합니다.
- 새 세션이 만들어지면 항상 세션 파일이 갱신됩니다.
- 이전 대화는 같은 기획자 컨텍스트(역할/규칙/이전 응답)를 유지합니다.

새 세션을 강제로 시작하려면 세션 파일을 지우거나 `--new` 를 씁니다.

```bash
rm .agents/.planner_session.json
# 또는
.venv/bin/python scripts/run_agent.py plan --new
```

세션이 백엔드에서 꼬여 `internal error` 가 반복되면 `--new` 로 새 세션을
열어 보는 게 가장 빠릅니다.

#### plan 모드 안에서 쓰는 명령

| 명령      | 동작                                                       |
|----------|------------------------------------------------------------|
| `:q` / `:quit` / `:exit` / `:bye` | 대화 종료                                |
| `:multi` | 여러 줄 입력 시작. 한 줄에 `:end` 만 입력하면 종료         |
| `:show`  | 현재 `docs/REQUIREMENTS.md` 출력                          |
| `:reload`| 현재 `docs/REQUIREMENTS.md` 내용을 기획자에게 다시 전달    |
| `:help`  | 명령 도움말                                                |

#### plan 모드 입력 팁

- 한국어 입력/백스페이스 정상 (prompt_toolkit 사용)
- 위/아래 화살표로 이전 입력 히스토리 사용 가능
- 응답 대기 동안 `기획자 생각 중...` 스피너 표시

#### 매 턴 파일 변경 알림

기획자 응답 직후 `docs/` 안에서 변경된 파일이 있으면 자동으로 알림이 출력됩니다.

표시 예:

```
변경된 파일
- docs/REQUIREMENTS.md  (modified)
- docs/PLAN_NOTES.md    (created)
```

상태 종류:

- `created` : 이번 턴에서 새로 생성된 파일
- `modified`: 내용이 바뀐 파일 (SHA256 기반 비교)
- `deleted` : 삭제된 파일

감시 대상은 `docs/` 하위 모든 파일이며, 특히 `REQUIREMENTS.md` 와
`PLAN_NOTES.md` 는 항상 포함됩니다. 변경이 없으면 이 패널은 표시되지 않습니다.

### 4.2 build — 구현/설계/문서 에이전트

`docs/REQUIREMENTS.md` 에 사용자 승인 마커가 있어야만 동작합니다.

```bash
# coder — Java/React 코드 (기본)
.venv/bin/python scripts/run_agent.py build --role coder --target src/backend

# db_architect — ERD + Flyway SQL
.venv/bin/python scripts/run_agent.py build --role db_architect

# tech_writer — USER_MANUAL, DEPLOYMENT_GUIDE 등 문서
.venv/bin/python scripts/run_agent.py build --role tech_writer

# 반복 (coder/db 15분, tech_writer 기본 1시간)
.venv/bin/python scripts/run_agent.py build --role coder --loop
.venv/bin/python scripts/run_agent.py build --role tech_writer --loop --interval 3600
```

역할별 산출물:

| `--role` | 담당 | 주요 출력 | 승인 마커 |
|----------|------|-----------|-----------|
| `coder` | Full-Stack | `src/backend/`, `src/frontend/` | 필요 |
| `db_architect` | DB 설계 | `docs/ERD.md`, `src/backend/.../db/migration/` | 필요 |
| `tech_writer` | 문서 | `docs/USER_MANUAL.md`, `CHANGELOG.md` 등 | 필요 |
| `benchmark_researcher` | 경쟁사 벤치마크 | `docs/BENCHMARK_REPORT.md`, `docs/COMPETITOR_MATRIX.md`, `memory/decisions.md` | **불필요** |
| `planner` | 자동 기획 동기화 | `docs/REQUIREMENTS.md`, `USER_STORIES.md`, `PLAN_NOTES.md` 등 | **불필요** |

```bash
# benchmark — 경쟁사 기능·서비스 조사 (1회)
.venv/bin/python scripts/run_agent.py build --role benchmark_researcher

# planner — 벤치마크 산출물을 읽고 기획 문서 갱신 (1회)
.venv/bin/python scripts/run_agent.py build --role planner

# 3시간마다 반복 (10800초)
.venv/bin/python scripts/run_agent.py build --role benchmark_researcher --loop --interval 10800
.venv/bin/python scripts/run_agent.py build --role planner --loop --interval 10800
```

**협업 흐름**: `benchmark_researcher` 가 경쟁사 제공 항목·기능을 정리 → `planner`(build) 가 `BENCHMARK_REPORT`·`COMPETITOR_MATRIX`·`decisions.md` 를 읽고 REQUIREMENTS·USER_STORIES·PLAN_NOTES 를 추가·수정한다. 대화형 `plan` 모드도 동일 벤치마크 문서를 참고한다.

공통 정책:

- REQUIREMENTS §1-1 스택 우선 (Java Spring Boot + React + PostgreSQL)
- 의문 시 `docs/PLAN_NOTES.md` 에 역할별 질문 섹션 기록 후 중단
- 비밀값 하드코딩 금지 (`.agents/rules.md` §3)

### 4.3 status — 상태 확인

```bash
.venv/bin/python scripts/run_agent.py status
```

출력 예:

```
workspace : /home/ubuntu/ogada
rules     : OK
roles     : OK
reqs file : OK
approved  : NO (build 차단됨)
model     : composer-2.5
```

### 4.4 doctor — SDK 연결 진단

```bash
.venv/bin/python scripts/run_agent.py doctor
```

가용 모델 4종(`default`, `composer-2.5`, `claude-opus-4-8`, `gpt-5.5`)에
최소 프롬프트를 보내 어떤 모델이 동작하는지, 또는 백엔드가 어떤 코드로
응답하는지를 보여줍니다. 모두 `status=500 code=internal` 로 나오면
**계정/키 단의 문제**(키 만료·회수, 요금제 한도, SDK preview 권한 미부여
등)이지 코드 문제가 아닙니다. 출력 하단에 점검 순서가 함께 표시됩니다.

---

## 5. 백그라운드 실행 (tmux 헬퍼)

### 5.1 시작

```bash
# 기본: build --target src/backend (1회)
./scripts/agent_start.sh

# build 반복 실행
./scripts/agent_start.sh build --loop

# 세션 이름 변경
AGENT_TMUX_SESSION=my-session ./scripts/agent_start.sh
```

> `plan` 모드는 인터랙티브 대화라 tmux 백그라운드 의미가 없습니다.
> 백그라운드 권장은 `build --loop` 시나리오입니다.

### 5.2 상태 확인

```bash
./scripts/agent_status.sh
```

tmux 세션, run_agent 프로세스, 승인 여부를 한 번에 보여줍니다.

### 5.3 중지

```bash
./scripts/agent_stop.sh
```

다음을 모두 정리합니다.

- tmux 세션 (`AGENT_TMUX_SESSION` 또는 기본 `ogada-agent`)
- `run_agent.py` 파이썬 프로세스
- `cursor-sdk-bridge` 보조 프로세스

### 5.4 팀 에이전트 (coder + db + writer 동시 백그라운드)

3역할을 **별도 tmux 세션**에서 동시에 loop 실행합니다.

```bash
# 사전: coder 1회 수동 실행으로 Java 초기화 확인 후
./scripts/agent_team_start.sh

# 각 역할 1회만 (테스트)
./scripts/agent_team_start.sh --no-loop

# 상태
./scripts/agent_team_status.sh

# 전체 중지
./scripts/agent_team_stop.sh
```

| tmux 세션 | 역할 | 기본 간격 |
|-----------|------|-----------|
| `ogada-coder` | coder | 900초 (15분) |
| `ogada-db` | db_architect | 900초 |
| `ogada-writer` | tech_writer | 3600초 (1시간) |

환경변수:

| 변수 | 기본값 | 설명 |
|------|--------|------|
| `AGENT_INTERVAL_SECONDS` | `900` | coder·db_architect loop 간격 |
| `AGENT_WRITER_INTERVAL_SECONDS` | `3600` | tech_writer loop 간격 |
| `AGENT_CODER_SESSION` | `ogada-coder` | coder tmux 세션 이름 |

---

## 6. 표준 워크플로우

1. **기획**

   ```bash
   .venv/bin/python scripts/run_agent.py plan
   ```

   기획자와 대화하며 `docs/REQUIREMENTS.md` 를 다듬는다.
   필요하면 `:multi`, `:show`, `:reload` 사용.

2. **검토/수정**

   `docs/REQUIREMENTS.md` 를 직접 열어 확인한다.
   추가 질문이 있다면 `docs/PLAN_NOTES.md` 도 확인.

3. **승인**

   `docs/REQUIREMENTS.md` 파일 끝에 한 줄을 직접 추가한다.

   ```
   <!-- approved-by-user: true -->
   ```

4. **구현**

   ```bash
   .venv/bin/python scripts/run_agent.py build --target src/backend
   ```

   또는 백그라운드로:

   ```bash
   ./scripts/agent_start.sh build --loop
   ```

5. **상태/중지**

   ```bash
   ./scripts/agent_status.sh
   ./scripts/agent_stop.sh
   ```

---

## 7. 환경변수

`.env` 또는 셸 환경에 설정 가능합니다.

| 변수                      | 기본값         | 설명                              |
|--------------------------|---------------|----------------------------------|
| `CURSOR_API_KEY`         | (필수)        | Cursor SDK 인증 키                |
| `AGENT_MODEL`            | (없음)        | 모든 모드의 모델을 강제 오버라이드 |
| `AGENT_INTERVAL_SECONDS` | `900`         | `build --loop` 의 반복 간격(초)   |
| `AGENT_TMUX_SESSION`     | `ogada-agent` | tmux 세션 이름                    |
| `AGENT_RETRY_MAX`        | `3`           | 일시적 오류에 대한 최대 재시도 횟수 |
| `AGENT_RETRY_BASE_DELAY` | `1.5`         | 재시도 기본 대기(초). 지수 백오프  |

### 모델 선택 우선순위와 자동 폴백 체인

`run_agent.py` 는 각 모드/역할에 대해 **모델 체인**(우선순위 리스트)을
계산하고, 앞 모델이 한도/오류로 실패하면 다음 모델로 자동 전환합니다.

체인 계산 순서:

1. 환경변수 `AGENT_MODEL` 이 있으면 그 값만 단일 체인으로 (폴백 없음)
2. `.agents/agents.yaml` 의 `agents[<role>].model` (1순위)
3. `.agents/agents.yaml` 의 `agents[<role>].fallback_models[*]` (지정 순)
4. `.agents/agents.yaml` 의 `models.default`
5. 내부 폴백값 `composer-2.5`

자동 폴백이 트리거되는 조건:

- 모델 한도/토큰/요금 관련 오류 메시지
  (`quota`, `limit`, `rate`, `billing`, `credit`, `exceeded`, `usage` 등)
- 모델 이름이 유효하지 않거나 권한이 없을 때
- 그 외 retryable 하지 않은 시작 실패

`build` 모드(`Agent.prompt`)는 시도 전체에서 체인 폴백이 적용되고,
`plan` 모드(`Agent.create`/`Agent.resume`)는 **세션 생성 시점**에 체인을
시도해 가장 먼저 성공하는 모델로 세션을 엽니다. 세션이 한번 열린 뒤에는
같은 모델로 대화가 이어집니다.

알려진 모델 슬러그 (계정 권한에 따라 사용 가능 여부 다름):

| 카테고리         | 슬러그                                |
|------------------|---------------------------------------|
| extra-high 추론  | `claude-opus-4-7-thinking-xhigh`      |
| high 추론        | `claude-opus-4-8-thinking-high`       |
| sonnet thinking  | `claude-4.6-sonnet-medium-thinking`   |
| 일반 Opus 4.8    | `claude-opus-4-8`                     |
| 코드 특화        | `gpt-5.3-codex`                       |
| 일반 GPT-5       | `gpt-5.5`, `gpt-5.5-medium`, `gpt-5.4-medium` |
| 기본/저비용      | `composer-2.5`, `composer-2.5-fast`, `default` |
| 빌드용           | `grok-build-0.1`                      |

코드 품질을 위해 `coder` 는 코드 특화 모델을 1순위로 두고, 점진적으로
일반 GPT → Opus → composer 로 폴백하도록 기본 설정되어 있습니다.

```yaml
- name: coder
  model: gpt-5.3-codex
  fallback_models:
    - gpt-5.5
    - gpt-5.5-medium
    - gpt-5.4-medium
    - claude-opus-4-8-thinking-high
    - claude-opus-4-8
    - composer-2.5
    - default
```

> 어떤 슬러그가 현재 계정에서 실제로 OK 인지 확인하려면 먼저 `doctor` 를
> 한 번 돌려보세요. 12개 슬러그에 최소 프롬프트를 보내 결과를 표시합니다.

```bash
.venv/bin/python scripts/run_agent.py doctor
```

현재 적용된 체인 확인:

```bash
.venv/bin/python scripts/run_agent.py status
```

출력 예:

```
env model : (unset)
planner   : ['composer-2.5']
coder     : ['claude-4.6-sonnet-medium-thinking', 'composer-2.5']
default   : ['composer-2.5']
```

특정 모델로 일괄 강제하고 싶으면 `.env` 에서 `AGENT_MODEL=composer-2.5`
처럼 설정하면 됩니다.

---

## 8. 자주 묻는 문제

### Q. build 가 즉시 `blocked` 종료된다
`docs/REQUIREMENTS.md` 끝에 다음 줄이 있어야 합니다.

```
<!-- approved-by-user: true -->
```

### Q. 기획자가 갑자기 새 세션처럼 행동한다
세션 파일이 사라졌거나 무효화된 경우입니다.

```bash
ls .agents/.planner_session.json
```

없으면 새 세션입니다. 이어가려면 다음과 같이 `--resume` 을 사용하세요.

```bash
.venv/bin/python scripts/run_agent.py plan --resume
```

세션 파일이 있는데도 새 세션처럼 동작하면 SDK 측에서 세션이 만료되었을 수
있습니다. 그 경우엔 파일을 지우고 새로 시작합니다.

```bash
rm .agents/.planner_session.json
```

### Q. `Bridge request failed` / `peer closed connection` 같은 에러가 뜬다
SDK 가 내부에서 쓰는 브리지에 일시적인 네트워크 문제가 생긴 경우입니다.
`run_agent.py` 는 `is_retryable=True` 인 오류를 자동으로 재시도합니다.

- 기본 재시도 횟수: `AGENT_RETRY_MAX=3`
- 기본 대기: `AGENT_RETRY_BASE_DELAY=1.5` (지수 백오프, SDK 가 `retry_after` 를 알려주면 그 값 우선)

여전히 자주 실패하면 다음을 확인하세요.

- 인터넷 연결이 불안정한지
- 너무 큰 입력(수만 토큰)을 한 번에 보내지 않았는지 (`:multi` 분할 권장)
- 다른 프로세스가 같은 워크스페이스에서 SDK 를 동시에 쓰고 있지는 않은지

### Q. 변경된 파일이 너무 많이 떠서 지저분하다
`render_file_changes` 는 `docs/` 하위만 감시합니다.
다른 폴더는 표시되지 않습니다. 그래도 너무 많이 뜬다면
기획자가 의도와 다른 파일을 만든 것일 수 있으니
`docs/PLAN_NOTES.md` 에 기록하고 기획자에게 확인해달라고 요청하세요.

### Q. 한국어 입력에서 백스페이스가 깨진다
`prompt_toolkit` 미설치 환경입니다. 설치하세요.

```bash
.venv/bin/pip install prompt_toolkit
```

### Q. 응답이 멈춘 듯 보인다
`기획자 생각 중...` 스피너가 돌지 않는 경우 `rich` 설치를 확인하세요.

```bash
.venv/bin/pip install rich
```

### Q. CURSOR_API_KEY 가 노출됐을 때
1. [Cursor Integrations](https://cursor.com/dashboard/integrations) 에서 즉시 `Revoke`
2. 새 키 발급
3. `.env` 의 값만 새 키로 교체

---

## 9. 보안 주의

- 비밀값은 항상 `.env` 또는 환경변수로만 관리한다 (`.agents/rules.md` §3 준수)
- 채팅/로그/PR/커밋 메시지에 API 키, 토큰, 비밀번호를 절대 평문으로 남기지 않는다
- `.env`, `.agents/.planner_session.json`, `.agents/.planner_history` 는 모두 gitignore 처리됨

---

*마지막 업데이트: 2026-06-06 | 관리: planner/coder 공통*
