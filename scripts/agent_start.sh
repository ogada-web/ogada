#!/usr/bin/env bash
# tmux 세션 안에서 build 모드로 에이전트를 백그라운드 시작한다.
# 사용 예:
#   ./scripts/agent_start.sh                  # build --target src/backend (1회)
#   ./scripts/agent_start.sh build --loop     # 반복 실행
#
# 팀 전체 기동은 ./scripts/agent_team_start.sh 를 사용한다.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
# shellcheck source=_agent_common.sh
source "$SCRIPT_DIR/_agent_common.sh"
_agent_common_init

ARGS=("$@")
if [[ ${#ARGS[@]} -eq 0 ]]; then
  ARGS=("build" "--target" "src/backend")
fi

agent_require_tmux
agent_start_tmux_session "$_AGENT_SESSION" "python scripts/run_agent.py ${ARGS[*]}"

echo "[ok] tmux 세션 시작됨: $_AGENT_SESSION"
echo "      로그 확인: tmux attach -t $_AGENT_SESSION"
echo "      분리:       Ctrl+b 다음 d"
echo "      중지:       ./scripts/agent_stop.sh"
