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

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
PYTHON="$ROOT/.venv/bin/python"
RUN="$PYTHON $ROOT/scripts/run_agent.py"

INTERVAL="${AGENT_INTERVAL_SECONDS:-900}"
STREAMS=(backend frontend)
ONCE=0
if [[ "${1:-}" == "--once" ]]; then
  ONCE=1
fi

run_step() {
  local role=$1
  shift
  echo ""
  echo "========================================"
  echo "[pipeline] $(date -Is) role=$role $*"
  echo "========================================"
  # shellcheck disable=SC2086
  $RUN build --role "$role" "$@"
}

stream_cycle() {
  local stream=$1
  echo ""
  echo "---------- stream: $stream ----------"
  run_step coder --stream "$stream" --target "src/$stream"
  run_step tester --stream "$stream"
}

cycle() {
  run_step planner
  run_step db_architect
  run_step ux_designer
  for stream in "${STREAMS[@]}"; do
    stream_cycle "$stream"
  done
}

echo "[pipeline] streams=${STREAMS[*]} interval=${INTERVAL}s"
echo "[pipeline] order: planner → db_architect → ux_designer → coder → tester (×2 streams)"
while true; do
  cycle
  if [[ "$ONCE" -eq 1 ]]; then
    echo "[pipeline] --once 완료"
    break
  fi
  echo "[pipeline] 다음 사이클까지 ${INTERVAL}s 대기..."
  sleep "$INTERVAL"
done
