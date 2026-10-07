#!/usr/bin/env bash
# 검증된 Grok 모델로 팀 루프 기동. --no-loop: 모든 역할 1회 실행.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
source "$SCRIPT_DIR/_agent_common.sh"
_agent_common_init
agent_require_runtime
cd "$_AGENT_ROOT"

MODEL="$("$_AGENT_PYTHON" - <<'PY'
import os
from dotenv import load_dotenv
load_dotenv('.env')
print(os.environ.get('AGENT_MODEL', '').strip())
PY
)"
if [[ "$MODEL" != grok-* ]]; then
  echo "[fatal] .env의 AGENT_MODEL에 doctor --list-models로 확인한 Grok ID를 설정하세요." >&2
  exit 2
fi

"$_AGENT_PYTHON" "$_AGENT_ROOT/scripts/run_agent.py" doctor --model "$MODEL"
exec bash "$SCRIPT_DIR/agent_team_start.sh" "$@"
