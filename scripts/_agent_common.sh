#!/usr/bin/env bash
# 에이전트 셸 스크립트 공통 라이브러리.
# source "$SCRIPT_DIR/_agent_common.sh" 후 사용.

_agent_common_init() {
  if [[ -n "${_AGENT_COMMON_LOADED:-}" ]]; then
    return 0
  fi
  _AGENT_COMMON_LOADED=1

  _AGENT_SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
  _AGENT_ROOT="$(cd "$_AGENT_SCRIPT_DIR/.." && pwd)"
  _AGENT_VENV="$_AGENT_ROOT/.venv/bin/activate"
  _AGENT_PYTHON="$_AGENT_ROOT/.venv/bin/python"

  _AGENT_SESSION="${AGENT_TMUX_SESSION:-ogada-agent}"
  _AGENT_PIPELINE_SESSION="${AGENT_PIPELINE_SESSION:-ogada-pipeline}"
  _AGENT_WRITER_SESSION="${AGENT_WRITER_SESSION:-ogada-writer}"
  _AGENT_SECURITY_SESSION="${AGENT_SECURITY_SESSION:-ogada-security}"
  _AGENT_BENCHMARK_SESSION="${AGENT_BENCHMARK_SESSION:-ogada-benchmark}"
}

agent_root() { _agent_common_init; echo "$_AGENT_ROOT"; }
agent_python() { _agent_common_init; echo "$_AGENT_PYTHON"; }

agent_tmux_available() {
  command -v tmux >/dev/null 2>&1
}

agent_check_session() {
  local name=$1
  local role=$2
  if agent_tmux_available && tmux has-session -t "$name" 2>/dev/null; then
    echo "  $role ($name): RUNNING"
  else
    echo "  $role ($name): STOPPED"
  fi
}

agent_show_all_sessions() {
  _agent_common_init
  echo "[tmux sessions]"
  agent_check_session "$_AGENT_SESSION" "single (ad-hoc)"
  agent_check_session "$_AGENT_PIPELINE_SESSION" "pipeline (PLN→DBA→UXD→COD→TSR ×2)"
  agent_check_session "$_AGENT_SECURITY_SESSION" "security_auditor (daily)"
  agent_check_session "$_AGENT_BENCHMARK_SESSION" "benchmark_researcher (30min)"
  agent_check_session "$_AGENT_WRITER_SESSION" "tech_writer"
}

agent_pgrep_workspace() {
  local pattern=$1
  _agent_common_init
  local pids=""
  local pid cwd
  while IFS= read -r pid; do
    [[ -z "$pid" ]] && continue
    cwd="$(readlink -f "/proc/$pid/cwd" 2>/dev/null || true)"
    if [[ "$cwd" == "$_AGENT_ROOT" || "$cwd" == "$_AGENT_ROOT/"* ]]; then
      pids+="$pid "
    fi
  done < <(pgrep -f "$pattern" 2>/dev/null || true)
  echo "${pids%" "}"
}

agent_show_processes() {
  _agent_common_init
  echo "[processes]"
  local found=0
  local bridge_count=0
  local agent_count=0
  while IFS= read -r line; do
    [[ -z "$line" ]] && continue
    echo "$line"
    found=1
    if [[ "$line" == *cursor-sdk-bridge* ]]; then
      bridge_count=$((bridge_count + 1))
    elif [[ "$line" == *run_agent.py* ]]; then
      agent_count=$((agent_count + 1))
    fi
  done < <(
    ps -ef 2>/dev/null | grep -E "run_agent\.py|agent_pipeline\.sh|cursor-sdk-bridge" | grep -v grep || true
  )
  if [[ "$found" -eq 0 ]]; then
    echo "  none"
  else
    echo "  summary: run_agent=${agent_count} bridge=${bridge_count}"
  fi
}

agent_prune_orphan_bridges() {
  _agent_common_init
  echo "[bridge-prune] orphan cursor-sdk-bridge 정리"
  "$_AGENT_PYTHON" "$_AGENT_ROOT/scripts/run_agent.py" prune-bridges "$@" || true
}

agent_show_approval() {
  _agent_common_init
  echo "[approval]"
  "$_AGENT_PYTHON" "$_AGENT_ROOT/scripts/run_agent.py" status || true
}

agent_show_status() {
  agent_show_all_sessions
  echo ""
  agent_show_processes
  echo ""
  agent_show_approval
}

agent_kill_pids() {
  local pids=$1
  [[ -z "$pids" ]] && return 0
  echo "[stop] PIDs: $pids"
  # shellcheck disable=SC2086
  kill $pids 2>/dev/null || true
  sleep 1
  # shellcheck disable=SC2086
  kill -9 $pids 2>/dev/null || true
}

agent_stop_session() {
  local name=$1
  if agent_tmux_available && tmux has-session -t "$name" 2>/dev/null; then
    echo "[stop] tmux $name"
    tmux kill-session -t "$name" || true
    return 0
  fi
  return 1
}

agent_stop_all() {
  _agent_common_init
  local killed=0

  for s in \
    "$_AGENT_PIPELINE_SESSION" \
    "$_AGENT_SECURITY_SESSION" \
    "$_AGENT_BENCHMARK_SESSION" \
    "$_AGENT_WRITER_SESSION" \
    "$_AGENT_SESSION"
  do
    if agent_stop_session "$s"; then
      killed=1
    fi
  done

  local pids
  pids="$(agent_pgrep_workspace "run_agent.py")"
  if [[ -n "$pids" ]]; then
    agent_kill_pids "$pids"
    killed=1
  fi

  pids="$(agent_pgrep_workspace "agent_pipeline.sh")"
  if [[ -n "$pids" ]]; then
    agent_kill_pids "$pids"
    killed=1
  fi

  pids="$(pgrep -f "tmux new-session -d -s ${_AGENT_PIPELINE_SESSION}" 2>/dev/null || true)"
  if [[ -n "$pids" ]]; then
    agent_kill_pids "$pids"
    killed=1
  fi

  pids="$(agent_pgrep_workspace "cursor-sdk-bridge")"
  if [[ -n "$pids" ]]; then
    agent_kill_pids "$pids"
    killed=1
  fi

  agent_prune_orphan_bridges --quiet

  if [[ "$killed" -eq 0 ]]; then
    echo "[ok] 실행 중인 에이전트 없음"
  else
    echo "[ok] 정리 완료"
  fi
}

agent_start_tmux_session() {
  local name=$1
  shift
  _agent_common_init
  if ! agent_tmux_available; then
    echo "[fatal] tmux 가 필요합니다: sudo apt install tmux" >&2
    return 1
  fi
  if tmux has-session -t "$name" 2>/dev/null; then
    echo "[skip] tmux '$name' 이미 실행 중 → tmux attach -t $name"
    return 0
  fi
  local cmd=". '$_AGENT_VENV' && cd '$_AGENT_ROOT' && $*"
  echo "[start] $name → $*"
  tmux new-session -d -s "$name" "$cmd"
}

agent_require_tmux() {
  if ! agent_tmux_available; then
    echo "[fatal] tmux 가 설치돼 있지 않습니다. sudo apt install tmux" >&2
    exit 1
  fi
}
