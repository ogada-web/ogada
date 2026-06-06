#!/usr/bin/env bash
# 개발 팀 에이전트 tmux 기동 (pipeline 중심):
#   - pipeline: planner → db → ux → coder → tester (backend → frontend), 15분 주기
#   - tech_writer: 보조 loop (1h)
#   - security_auditor / benchmark_researcher: 1일 1회
#
# pipeline 역할은 별도 tmux 없음 (경합 방지).
#
# 사용:
#   ./scripts/agent_team_start.sh
#   ./scripts/agent_team_start.sh --no-loop

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
VENV="$ROOT/.venv/bin/activate"

PIPELINE_SESSION="${AGENT_PIPELINE_SESSION:-ogada-pipeline}"
WRITER_SESSION="${AGENT_WRITER_SESSION:-ogada-writer}"
SECURITY_SESSION="${AGENT_SECURITY_SESSION:-ogada-security}"
BENCHMARK_SESSION="${AGENT_BENCHMARK_SESSION:-ogada-benchmark}"

INTERVAL="${AGENT_INTERVAL_SECONDS:-900}"
WRITER_INTERVAL="${AGENT_WRITER_INTERVAL_SECONDS:-3600}"
SECURITY_INTERVAL="${AGENT_SECURITY_INTERVAL_SECONDS:-86400}"
BENCHMARK_INTERVAL="${AGENT_BENCHMARK_INTERVAL_SECONDS:-86400}"

PIPELINE_LOOP=()
if [[ "${1:-}" == "--no-loop" ]]; then
  PIPELINE_LOOP=(--once)
fi

if ! command -v tmux >/dev/null 2>&1; then
  echo "[fatal] tmux 가 필요합니다: sudo apt install tmux" >&2
  exit 1
fi

if ! "$ROOT/.venv/bin/python" "$ROOT/scripts/run_agent.py" status 2>/dev/null | grep -q "approved  : YES"; then
  echo "[warn] REQUIREMENTS 승인 마커가 없으면 build 가 차단됩니다." >&2
fi

start_session() {
  local name=$1
  shift
  if tmux has-session -t "$name" 2>/dev/null; then
    echo "[skip] tmux '$name' 이미 실행 중 → tmux attach -t $name"
    return 0
  fi
  local cmd=". '$VENV' && cd '$ROOT' && python scripts/run_agent.py $*"
  echo "[start] $name → python scripts/run_agent.py $*"
  tmux new-session -d -s "$name" "$cmd"
}

start_shell_session() {
  local name=$1
  shift
  if tmux has-session -t "$name" 2>/dev/null; then
    echo "[skip] tmux '$name' 이미 실행 중 → tmux attach -t $name"
    return 0
  fi
  local cmd=". '$VENV' && cd '$ROOT' && $*"
  echo "[start] $name → $*"
  tmux new-session -d -s "$name" "$cmd"
}

chmod +x "$ROOT/scripts/agent_pipeline.sh"

start_shell_session "$PIPELINE_SESSION" \
  "AGENT_INTERVAL_SECONDS=$INTERVAL ./scripts/agent_pipeline.sh ${PIPELINE_LOOP[*]:-}"

start_session "$SECURITY_SESSION" \
  build --role security_auditor --interval "$SECURITY_INTERVAL" --loop

start_session "$BENCHMARK_SESSION" \
  build --role benchmark_researcher --interval "$BENCHMARK_INTERVAL" --loop

start_session "$WRITER_SESSION" \
  build --role tech_writer --interval "$WRITER_INTERVAL" --loop

echo ""
echo "[ok] 팀 에이전트 tmux 세션"
echo "  pipeline (PLN→DBA→UXD→COD→TSR ×2) : tmux attach -t $PIPELINE_SESSION  (interval ${INTERVAL}s)"
echo "  security_auditor                     : tmux attach -t $SECURITY_SESSION  (interval ${SECURITY_INTERVAL}s = 24h)"
echo "  benchmark_researcher                 : tmux attach -t $BENCHMARK_SESSION  (interval ${BENCHMARK_INTERVAL}s = 24h)"
echo "  tech_writer                          : tmux attach -t $WRITER_SESSION   (interval ${WRITER_INTERVAL}s)"
echo ""
echo "  전체 상태: ./scripts/agent_team_status.sh"
echo "  전체 중지: ./scripts/agent_team_stop.sh"
