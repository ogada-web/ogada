#!/usr/bin/env bash
# 순차 파이프라인 (순서 보장):
#   planner → db_architect → ux_designer
#   → [backend: coder → tester] → [frontend: coder → tester]
#
# 한 사이클 완료 후 AGENT_INTERVAL_SECONDS(기본 900=15분) 대기.
#
# 사용:
#   ./scripts/agent_pipeline.sh
#   ./scripts/agent_pipeline.sh --once
#
# 환경변수:
#   AGENT_INTERVAL_SECONDS=900   사이클 간 대기(초)

set -uo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
PYTHON="$ROOT/.venv/bin/python"
RUN="$PYTHON $ROOT/scripts/run_agent.py"

INTERVAL="${AGENT_INTERVAL_SECONDS:-900}"
STREAMS=(backend frontend)
ONCE=0
PIPELINE_FAILURES=()

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
  if $RUN build --role "$role" "$@"; then
    return 0
  fi
  local rc=$?
  echo "[pipeline] ERROR role=$role exit=$rc" >&2
  PIPELINE_FAILURES+=("${role}${*:+ $*}")
  return "$rc"
}

stream_cycle() {
  local stream=$1
  echo ""
  echo "---------- stream: $stream ----------"
  run_step coder --stream "$stream" --target "src/$stream" || true
  run_step tester --stream "$stream" || true
}

cycle() {
  PIPELINE_FAILURES=()
  run_step planner || true
  run_step db_architect || true
  run_step ux_designer || true
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

echo "[pipeline] streams=${STREAMS[*]} interval=${INTERVAL}s"
echo "[pipeline] order: planner → db_architect → ux_designer → coder → tester (×2 streams)"

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
