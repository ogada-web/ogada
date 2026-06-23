#!/usr/bin/env bash
# 순차 파이프라인 (순서 보장):
#   planner → db_architect → ux_designer
#   → [backend: coder → tester] → [frontend: coder → tester]
#
# 한 사이클 완료 후 AGENT_INTERVAL_SECONDS(기본 3분) 대기.
# 기본은 구현 사이클(coder→tester만). planner/db/ux는 N사이클마다 1회(기본 6).
#
# 사용:
#   ./scripts/agent_pipeline.sh
#   ./scripts/agent_pipeline.sh --once
#
# 환경변수:
#   AGENT_INTERVAL_SECONDS=180    사이클 간 대기(초, 기본 3분)
#   AGENT_PIPELINE_FULL_EVERY=6   planner·db·ux 포함 전체 사이클 주기(기본 6회마다 1번)

set -uo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
PYTHON="$ROOT/.venv/bin/python"
RUN="$PYTHON $ROOT/scripts/run_agent.py"

INTERVAL="${AGENT_INTERVAL_SECONDS:-180}"
FULL_EVERY="${AGENT_PIPELINE_FULL_EVERY:-6}"
CYCLE_FILE="$ROOT/.agents/pipeline_cycle"
STREAMS=(backend frontend)
ONCE=0
PIPELINE_FAILURES=()

pipeline_release_resources() {
  echo "[pipeline] bridge/run_agent 자원 정리"
  "$PYTHON" "$ROOT/scripts/run_agent.py" prune-bridges --quiet 2>/dev/null || true
}

pipeline_release_bridge() {
  pipeline_release_resources
}

pipeline_release_bridge_resources() {
  pipeline_release_resources
}

trap pipeline_release_resources EXIT INT TERM

if [[ "${1:-}" == "--once" ]]; then
  ONCE=1
fi

preflight() {
  local spec name path ok=1
  echo "[preflight] submodule·worktree 확인"

  for spec in "backend:$ROOT/src/backend" "frontend:$ROOT/src/frontend"; do
    name="${spec%%:*}"
    path="${spec#*:}"
    if [[ ! -d "$path" ]] || ! git -C "$path" rev-parse --git-dir >/dev/null 2>&1; then
      echo "[preflight] $name submodule 없음 → git submodule update --init src/$name"
      if ! git -C "$ROOT" submodule update --init "src/$name"; then
        echo "[preflight] fatal: src/$name 초기화 실패" >&2
        ok=0
      fi
    fi
  done

  if [[ "$ok" -eq 0 ]]; then
    echo "[preflight] fatal: submodule 초기화 후 ./scripts/git_branch_setup.sh 실행" >&2
    return 1
  fi

  if [[ ! -d "$ROOT/src/backend-test" ]] || [[ ! -d "$ROOT/src/frontend-test" ]]; then
    echo "[preflight] test worktree 없음 → ./scripts/git_branch_setup.sh 실행"
    "$ROOT/scripts/git_branch_setup.sh"
  fi

  for spec in "backend:$ROOT/src/backend" "frontend:$ROOT/src/frontend"; do
    name="${spec%%:*}"
    path="${spec#*:}"
    if [[ ! -d "$path/.git" && ! -f "$path/.git" ]]; then
      echo "[preflight] fatal: src/$name git 메타 없음" >&2
      return 1
    fi
    echo "[preflight] ok: src/$name ($(git -C "$path" branch --show-current 2>/dev/null || echo unknown))"
  done
  return 0
}

run_step() {
  local role=$1
  shift
  echo ""
  echo "========================================"
  echo "[pipeline] $(date -Is) role=$role $*"
  echo "========================================"
  local rc=0
  if $RUN build --role "$role" "$@"; then
    rc=0
  else
    rc=$?
    echo "[pipeline] ERROR role=$role exit=$rc" >&2
    PIPELINE_FAILURES+=("${role}${*:+ $*}")
  fi
  pipeline_release_bridge_resources
  return "$rc"
}

stream_cycle() {
  local stream=$1
  echo ""
  echo "---------- stream: $stream ----------"
  run_step coder --stream "$stream" --target "src/$stream" || true
  run_step tester --stream "$stream" || true
}

next_cycle_number() {
  local n=0
  if [[ -f "$CYCLE_FILE" ]]; then
    n=$(cat "$CYCLE_FILE" 2>/dev/null || echo 0)
  fi
  n=$((n + 1))
  echo "$n" > "$CYCLE_FILE"
  echo "$n"
}

cycle() {
  PIPELINE_FAILURES=()
  pipeline_release_bridge
  local cycle_no
  cycle_no="$(next_cycle_number)"
  local run_full=0
  if (( cycle_no == 1 || cycle_no % FULL_EVERY == 0 )); then
    run_full=1
  fi

  if (( run_full == 1 )); then
    echo "[pipeline] cycle=$cycle_no mode=full (planner·db·ux 포함)"
    run_step planner || true
    run_step db_architect || true
    run_step ux_designer || true
  else
    echo "[pipeline] cycle=$cycle_no mode=implement (coder→tester만 — 기획 스킵)"
  fi

  for stream in "${STREAMS[@]}"; do
    stream_cycle "$stream"
  done

  if [[ ${#PIPELINE_FAILURES[@]} -gt 0 ]]; then
    echo ""
    echo "[pipeline] cycle finished with failures: ${PIPELINE_FAILURES[*]}" >&2
    return 1
  fi
  return 0
}

echo "[pipeline] streams=${STREAMS[*]} interval=${INTERVAL}s full_every=${FULL_EVERY}"
echo "[pipeline] order: [full] planner → db_architect → ux_designer → coder → tester (×2 streams)"

if ! preflight; then
  exit 2
fi

while true; do
  if ! cycle; then
    echo "[pipeline] 사이클 실패 — 다음 주기까지 대기하거나 로그를 확인하세요." >&2
    if [[ "$ONCE" -eq 1 ]]; then
      exit 1
    fi
  elif [[ "$ONCE" -eq 1 ]]; then
    echo "[pipeline] --once 완료"
    break
  fi
  if [[ "$ONCE" -eq 1 ]]; then
    break
  fi
  echo "[pipeline] 다음 사이클까지 ${INTERVAL}s 대기..."
  sleep "$INTERVAL"
done
