#!/usr/bin/env bash
# 실행 중인 에이전트 관련 프로세스/세션을 모두 정리한다.
# 정리 대상:
# 1) tmux 세션: AGENT_TMUX_SESSION (기본 ogada-agent)
# 2) 워크스페이스 안에서 실행 중인 run_agent.py 파이썬 프로세스
# 3) cursor-sdk-bridge 보조 프로세스

set -uo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
SESSION="${AGENT_TMUX_SESSION:-ogada-agent}"

killed_any=0

if command -v tmux >/dev/null 2>&1; then
  if tmux has-session -t "$SESSION" 2>/dev/null; then
    echo "[stop] tmux session: $SESSION"
    tmux kill-session -t "$SESSION" || true
    killed_any=1
  fi
fi

PIDS_RUN_AGENT=$(pgrep -f "run_agent.py" || true)
if [[ -n "$PIDS_RUN_AGENT" ]]; then
  echo "[stop] run_agent.py PIDs: $PIDS_RUN_AGENT"
  # shellcheck disable=SC2086
  kill $PIDS_RUN_AGENT 2>/dev/null || true
  sleep 1
  # shellcheck disable=SC2086
  kill -9 $PIDS_RUN_AGENT 2>/dev/null || true
  killed_any=1
fi

PIDS_BRIDGE=$(pgrep -f "cursor-sdk-bridge" || true)
if [[ -n "$PIDS_BRIDGE" ]]; then
  echo "[stop] cursor-sdk-bridge PIDs: $PIDS_BRIDGE"
  # shellcheck disable=SC2086
  kill $PIDS_BRIDGE 2>/dev/null || true
  sleep 1
  # shellcheck disable=SC2086
  kill -9 $PIDS_BRIDGE 2>/dev/null || true
  killed_any=1
fi

if [[ "$killed_any" -eq 0 ]]; then
  echo "[ok] 실행 중인 에이전트 프로세스를 찾지 못했습니다."
else
  echo "[ok] 정리 완료."
fi
