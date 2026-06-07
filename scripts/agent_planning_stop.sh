#!/usr/bin/env bash
# benchmark_researcher tmux 세션만 정리 (하위 호환).
# 전체 중지는 ./scripts/agent_stop.sh 권장.

set -uo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
# shellcheck source=_agent_common.sh
source "$SCRIPT_DIR/_agent_common.sh"

_agent_common_init
killed=0

if agent_stop_session "$_AGENT_BENCHMARK_SESSION"; then
  killed=1
fi

pids="$(agent_pgrep_workspace "run_agent.py build --role benchmark_researcher")"
if [[ -n "$pids" ]]; then
  agent_kill_pids "$pids"
  killed=1
fi

if [[ "$killed" -eq 0 ]]; then
  echo "[ok] 실행 중인 벤치마크 에이전트 없음"
else
  echo "[ok] 벤치마크 에이전트 정리 완료"
fi
