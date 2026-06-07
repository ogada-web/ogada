#!/usr/bin/env bash
# 팀 에이전트(pipeline + 보조 역할) 상태 요약.
# agent_status.sh 와 동일 출력 — 하위 호환용 래퍼.

set -uo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
# shellcheck source=_agent_common.sh
source "$SCRIPT_DIR/_agent_common.sh"

agent_show_status
