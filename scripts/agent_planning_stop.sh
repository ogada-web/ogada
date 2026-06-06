#!/usr/bin/env bash
# agent_planning_start.sh 로 띄운 benchmark tmux 세션 + 관련 프로세스 정리.

set -uo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

BENCHMARK_SESSION="${AGENT_BENCHMARK_SESSION:-ogada-benchmark}"

killed=0

if command -v tmux >/dev/null 2>&1 && tmux has-session -t "$BENCHMARK_SESSION" 2>/dev/null; then
  echo "[stop] tmux $BENCHMARK_SESSION"
  tmux kill-session -t "$BENCHMARK_SESSION" || true
  killed=1
fi

PIDS=$(pgrep -f "run_agent.py build --role benchmark_researcher" || true)
if [[ -n "$PIDS" ]]; then
  echo "[stop] benchmark run_agent PIDs: $PIDS"
  # shellcheck disable=SC2086
  kill $PIDS 2>/dev/null || true
  sleep 1
  # shellcheck disable=SC2086
  kill -9 $PIDS 2>/dev/null || true
  killed=1
fi

if [[ "$killed" -eq 0 ]]; then
  echo "[ok] 실행 중인 벤치마크 에이전트 없음"
else
  echo "[ok] 벤치마크 에이전트 정리 완료"
fi
