#!/usr/bin/env bash
# benchmark_researcher tmux 세션 상태 요약.

set -uo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

BENCHMARK_SESSION="${AGENT_BENCHMARK_SESSION:-ogada-benchmark}"

check_session() {
  local name=$1
  local role=$2
  if command -v tmux >/dev/null 2>&1 && tmux has-session -t "$name" 2>/dev/null; then
    echo "  $role ($name): RUNNING"
  else
    echo "  $role ($name): STOPPED"
  fi
}

echo "[planning tmux]"
check_session "$BENCHMARK_SESSION" "benchmark_researcher (daily)"

echo ""
echo "[processes]"
ps -ef | grep -E "run_agent.py build --role benchmark_researcher|cursor-sdk-bridge" | grep -v grep || echo "  none"

echo ""
"$ROOT/.venv/bin/python" "$ROOT/scripts/run_agent.py" status || true
