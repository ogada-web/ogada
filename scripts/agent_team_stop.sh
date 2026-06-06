#!/usr/bin/env bash
# agent_team_start.sh 로 띄운 3개 tmux 세션 + run_agent.py 프로세스 정리.

set -uo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

CODER_SESSION="${AGENT_CODER_SESSION:-ogada-coder}"
DB_SESSION="${AGENT_DB_SESSION:-ogada-db}"
WRITER_SESSION="${AGENT_WRITER_SESSION:-ogada-writer}"

killed=0

for s in "$CODER_SESSION" "$DB_SESSION" "$WRITER_SESSION"; do
  if command -v tmux >/dev/null 2>&1 && tmux has-session -t "$s" 2>/dev/null; then
    echo "[stop] tmux $s"
    tmux kill-session -t "$s" || true
    killed=1
  fi
done

PIDS=$(pgrep -f "run_agent.py build" || true)
if [[ -n "$PIDS" ]]; then
  echo "[stop] run_agent.py build PIDs: $PIDS"
  # shellcheck disable=SC2086
  kill $PIDS 2>/dev/null || true
  sleep 1
  # shellcheck disable=SC2086
  kill -9 $PIDS 2>/dev/null || true
  killed=1
fi

PIDS_BRIDGE=$(pgrep -f "cursor-sdk-bridge" || true)
if [[ -n "$PIDS_BRIDGE" ]]; then
  echo "[stop] cursor-sdk-bridge PIDs: $PIDS_BRIDGE"
  # shellcheck disable=SC2086
  kill $PIDS_BRIDGE 2>/dev/null || true
  killed=1
fi

if [[ "$killed" -eq 0 ]]; then
  echo "[ok] 실행 중인 팀 에이전트 없음"
else
  echo "[ok] 팀 에이전트 정리 완료"
fi
