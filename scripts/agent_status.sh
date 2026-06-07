#!/usr/bin/env bash
# 모든 에이전트 tmux 세션 + 프로세스 + 승인 상태 요약.

set -uo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
# shellcheck source=_agent_common.sh
source "$SCRIPT_DIR/_agent_common.sh"

agent_show_status
