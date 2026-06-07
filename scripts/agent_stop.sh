#!/usr/bin/env bash
# 실행 중인 모든 에이전트 tmux 세션·프로세스 정리 (워크스페이스 범위).

set -uo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
# shellcheck source=_agent_common.sh
source "$SCRIPT_DIR/_agent_common.sh"

agent_stop_all
