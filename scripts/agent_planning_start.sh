#!/usr/bin/env bash
# benchmark_researcher 를 30분 주기 loop 실행 (하위 호환).
# planner 는 agent_team_start.sh pipeline (30분) 에서 실행.
#
# 권장: ./scripts/agent_team_start.sh (pipeline + 보조 역할 일괄 기동)
#
# 사용:
#   ./scripts/agent_planning_start.sh
#   ./scripts/agent_planning_start.sh --no-loop

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
# shellcheck source=_agent_common.sh
source "$SCRIPT_DIR/_agent_common.sh"
_agent_common_init

INTERVAL="${AGENT_BENCHMARK_INTERVAL_SECONDS:-1800}"

LOOP_FLAG=(--loop)
if [[ "${1:-}" == "--no-loop" ]]; then
  LOOP_FLAG=()
fi

agent_require_tmux

agent_start_tmux_session "$_AGENT_BENCHMARK_SESSION" \
  "python scripts/run_agent.py build --role benchmark_researcher --interval $INTERVAL ${LOOP_FLAG[*]:-}"

echo ""
echo "[ok] 벤치마크 에이전트 tmux 세션"
echo "  benchmark_researcher : tmux attach -t $_AGENT_BENCHMARK_SESSION   (interval ${INTERVAL}s = 30min)"
echo ""
echo "  planner 는 ./scripts/agent_team_start.sh pipeline (30분) 에서 실행됩니다."
echo "  전체 상태: ./scripts/agent_status.sh"
echo "  전체 중지: ./scripts/agent_stop.sh"
