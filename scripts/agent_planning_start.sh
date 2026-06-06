#!/usr/bin/env bash
# benchmark_researcher 를 1일 1회 loop 실행.
# planner 는 agent_team_start.sh pipeline 에서 15분 주기로 실행.
#
# 사용:
#   ./scripts/agent_planning_start.sh
#   ./scripts/agent_planning_start.sh --no-loop
#
# 환경변수:
#   AGENT_BENCHMARK_INTERVAL_SECONDS=86400  기본 24시간

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
VENV="$ROOT/.venv/bin/activate"

BENCHMARK_SESSION="${AGENT_BENCHMARK_SESSION:-ogada-benchmark}"
INTERVAL="${AGENT_BENCHMARK_INTERVAL_SECONDS:-86400}"

LOOP_FLAG=(--loop)
if [[ "${1:-}" == "--no-loop" ]]; then
  LOOP_FLAG=()
fi

if ! command -v tmux >/dev/null 2>&1; then
  echo "[fatal] tmux 가 필요합니다: sudo apt install tmux" >&2
  exit 1
fi

start_session() {
  local name=$1
  shift
  if tmux has-session -t "$name" 2>/dev/null; then
    echo "[skip] tmux '$name' 이미 실행 중 → tmux attach -t $name"
    return 0
  fi
  local cmd=". '$VENV' && cd '$ROOT' && python scripts/run_agent.py $*"
  echo "[start] $name → python scripts/run_agent.py $*"
  tmux new-session -d -s "$name" "$cmd"
}

start_session "$BENCHMARK_SESSION" \
  build --role benchmark_researcher --interval "$INTERVAL" "${LOOP_FLAG[@]}"

echo ""
echo "[ok] 벤치마크 에이전트 tmux 세션"
echo "  benchmark_researcher : tmux attach -t $BENCHMARK_SESSION   (interval ${INTERVAL}s = 24h)"
echo ""
echo "  planner 는 ./scripts/agent_team_start.sh pipeline (15분) 에서 실행됩니다."
echo "  전체 상태: ./scripts/agent_planning_status.sh"
echo "  전체 중지: ./scripts/agent_planning_stop.sh"
