#!/usr/bin/env bash
# coder / db_architect / tech_writer tmux 세션 상태 요약.

set -uo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

CODER_SESSION="${AGENT_CODER_SESSION:-ogada-coder}"
DB_SESSION="${AGENT_DB_SESSION:-ogada-db}"
WRITER_SESSION="${AGENT_WRITER_SESSION:-ogada-writer}"

check_session() {
  local name=$1
  local role=$2
  if command -v tmux >/dev/null 2>&1 && tmux has-session -t "$name" 2>/dev/null; then
    echo "  $role ($name): RUNNING"
  else
    echo "  $role ($name): STOPPED"
  fi
}

echo "[team tmux]"
check_session "$CODER_SESSION" "coder"
check_session "$DB_SESSION" "db_architect"
check_session "$WRITER_SESSION" "tech_writer"

echo ""
echo "[processes]"
ps -ef | grep -E "run_agent.py build|cursor-sdk-bridge" | grep -v grep || echo "  none"

echo ""
"$ROOT/.venv/bin/python" "$ROOT/scripts/run_agent.py" status || true
