#!/usr/bin/env bash
# agent_team_start.sh 로 띄운 tmux 세션 + pipeline 프로세스 정리.

set -uo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
# shellcheck source=_agent_common.sh
source "$SCRIPT_DIR/_agent_common.sh"

agent_stop_all
