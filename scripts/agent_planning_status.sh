#!/usr/bin/env bash
# benchmark_researcher 상태 요약 (하위 호환).
# 전체 상태는 ./scripts/agent_status.sh 권장.

set -uo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
# shellcheck source=_agent_common.sh
source "$SCRIPT_DIR/_agent_common.sh"

_agent_common_init
echo "[planning tmux]"
agent_check_session "$_AGENT_BENCHMARK_SESSION" "benchmark_researcher (daily)"
echo ""
agent_show_processes
echo ""
agent_show_approval
