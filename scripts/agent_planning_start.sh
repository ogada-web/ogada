#!/usr/bin/env bash
# benchmark_researcher + planner 를 각각 별도 tmux 세션에서 3시간 간격 loop 실행.
#
# benchmark_researcher: 경쟁사 기능·서비스 조사 → BENCHMARK_REPORT, COMPETITOR_MATRIX
# planner:            벤치마크 산출물을 읽고 REQUIREMENTS·USER_STORIES 등 기획 갱신
#
# 사용 예:
#   ./scripts/agent_planning_start.sh
#   ./scripts/agent_planning_start.sh --no-loop    # 각 역할 1회만
#
# 환경변수:
#   AGENT_PLANNING_INTERVAL_SECONDS=10800  기본 3시간

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
VENV="$ROOT/.venv/bin/activate"

BENCHMARK_SESSION="${AGENT_BENCHMARK_SESSION:-ogada-benchmark}"
PLANNER_SESSION="${AGENT_PLANNER_SESSION:-ogada-planner}"
INTERVAL="${AGENT_PLANNING_INTERVAL_SECONDS:-10800}"

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

# benchmark: 경쟁사 조사 (승인 마커 불필요)
start_session "$BENCHMARK_SESSION" \
  build --role benchmark_researcher --interval "$INTERVAL" "${LOOP_FLAG[@]}"

# planner: 벤치마크 반영 자동 기획 (승인 마커 불필요)
start_session "$PLANNER_SESSION" \
  build --role planner --interval "$INTERVAL" "${LOOP_FLAG[@]}"

echo ""
echo "[ok] 기획·벤치마크 에이전트 tmux 세션"
echo "  benchmark_researcher : tmux attach -t $BENCHMARK_SESSION   (interval ${INTERVAL}s = 3h)"
echo "  planner (auto)       : tmux attach -t $PLANNER_SESSION      (interval ${INTERVAL}s = 3h)"
echo ""
echo "  전체 상태: ./scripts/agent_planning_status.sh"
echo "  전체 중지: ./scripts/agent_planning_stop.sh"
