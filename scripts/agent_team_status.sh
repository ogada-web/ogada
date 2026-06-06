#!/usr/bin/env bash
# pipeline / db / security / tech_writer tmux 세션 상태 요약.

set -uo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

PIPELINE_SESSION="${AGENT_PIPELINE_SESSION:-ogada-pipeline}"
WRITER_SESSION="${AGENT_WRITER_SESSION:-ogada-writer}"
SECURITY_SESSION="${AGENT_SECURITY_SESSION:-ogada-security}"
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

echo "[team tmux]"
check_session "$PIPELINE_SESSION" "pipeline (PLN→DBA→UXD→COD→TSR backend→frontend)"
check_session "$SECURITY_SESSION" "security_auditor (daily)"
check_session "$BENCHMARK_SESSION" "benchmark_researcher (daily)"
check_session "$WRITER_SESSION" "tech_writer"

echo ""
echo "[processes]"
ps -ef | grep -E "run_agent.py build|agent_pipeline.sh|cursor-sdk-bridge" | grep -v grep || echo "  none"

echo ""
"$ROOT/.venv/bin/python" "$ROOT/scripts/run_agent.py" status || true
