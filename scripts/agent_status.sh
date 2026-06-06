#!/usr/bin/env bash
# 에이전트 관련 상태(tmux 세션 + 프로세스 + 승인 상태) 요약.

set -uo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
SESSION="${AGENT_TMUX_SESSION:-ogada-agent}"

echo "[tmux]"
if command -v tmux >/dev/null 2>&1; then
  if tmux has-session -t "$SESSION" 2>/dev/null; then
    echo "  session '$SESSION' : RUNNING"
    tmux list-sessions || true
  else
    echo "  session '$SESSION' : NONE"
  fi
else
  echo "  tmux not installed"
fi

echo ""
echo "[processes]"
ps -ef | grep -E "run_agent.py|cursor-sdk-bridge" | grep -v grep || echo "  none"

echo ""
echo "[approval]"
"$ROOT/.venv/bin/python" "$ROOT/scripts/run_agent.py" status || true
