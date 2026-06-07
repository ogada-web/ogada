#!/usr/bin/env bash
# 개발 팀 에이전트 tmux 기동 (pipeline 중심):
#   - pipeline: planner → db → ux → coder → tester (backend → frontend), 15분 주기
#   - tech_writer: 보조 loop (1h)
#   - security_auditor / benchmark_researcher: 1일 1회
#
# 사용:
#   ./scripts/agent_team_start.sh
#   ./scripts/agent_team_start.sh --no-loop

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
# shellcheck source=_agent_common.sh
source "$SCRIPT_DIR/_agent_common.sh"
_agent_common_init

INTERVAL="${AGENT_INTERVAL_SECONDS:-900}"
WRITER_INTERVAL="${AGENT_WRITER_INTERVAL_SECONDS:-3600}"
SECURITY_INTERVAL="${AGENT_SECURITY_INTERVAL_SECONDS:-86400}"
BENCHMARK_INTERVAL="${AGENT_BENCHMARK_INTERVAL_SECONDS:-86400}"

PIPELINE_LOOP=()
if [[ "${1:-}" == "--no-loop" ]]; then
  PIPELINE_LOOP=(--once)
fi

agent_require_tmux

if [[ ! -d "$_AGENT_ROOT/src/frontend" ]] || [[ ! -d "$_AGENT_ROOT/src/backend-test" ]]; then
  echo "[preflight] submodule/worktree 준비 중..."
  git -C "$_AGENT_ROOT" submodule update --init src/backend src/frontend 2>/dev/null || true
  "$_AGENT_ROOT/scripts/git_branch_setup.sh"
fi

if ! "$_AGENT_PYTHON" "$_AGENT_ROOT/scripts/run_agent.py" status 2>/dev/null | grep -q "approved  : YES"; then
  echo "[warn] REQUIREMENTS 승인 마커가 없으면 build 가 차단됩니다." >&2
fi

chmod +x "$_AGENT_ROOT/scripts/agent_pipeline.sh"

agent_start_tmux_session "$_AGENT_PIPELINE_SESSION" \
  "AGENT_INTERVAL_SECONDS=$INTERVAL ./scripts/agent_pipeline.sh ${PIPELINE_LOOP[*]:-}"

agent_start_tmux_session "$_AGENT_SECURITY_SESSION" \
  "python scripts/run_agent.py build --role security_auditor --interval $SECURITY_INTERVAL --loop"

agent_start_tmux_session "$_AGENT_BENCHMARK_SESSION" \
  "python scripts/run_agent.py build --role benchmark_researcher --interval $BENCHMARK_INTERVAL --loop"

agent_start_tmux_session "$_AGENT_WRITER_SESSION" \
  "python scripts/run_agent.py build --role tech_writer --interval $WRITER_INTERVAL --loop"

echo ""
echo "[ok] 팀 에이전트 tmux 세션"
echo "  pipeline (PLN→DBA→UXD→COD→TSR ×2) : tmux attach -t $_AGENT_PIPELINE_SESSION  (interval ${INTERVAL}s)"
echo "  security_auditor                     : tmux attach -t $_AGENT_SECURITY_SESSION  (interval ${SECURITY_INTERVAL}s = 24h)"
echo "  benchmark_researcher                 : tmux attach -t $_AGENT_BENCHMARK_SESSION  (interval ${BENCHMARK_INTERVAL}s = 24h)"
echo "  tech_writer                          : tmux attach -t $_AGENT_WRITER_SESSION   (interval ${WRITER_INTERVAL}s)"
echo ""
echo "  전체 상태: ./scripts/agent_status.sh"
echo "  전체 중지: ./scripts/agent_stop.sh"
