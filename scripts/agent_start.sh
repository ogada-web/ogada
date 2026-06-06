#!/usr/bin/env bash
# tmux 세션 안에서 build 모드로 에이전트를 백그라운드 시작한다.
# 사용 예:
#   ./scripts/agent_start.sh                  # build --target src/backend (1회)
#   ./scripts/agent_start.sh build --loop     # 반복 실행
#   ./scripts/agent_start.sh plan             # 기획자 모드 (인터랙티브)
#
# 정책:
# - 동일 이름 세션이 있으면 새로 만들지 않는다.
# - 활성화는 tmux attach -t "$SESSION" 으로 확인한다.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
SESSION="${AGENT_TMUX_SESSION:-ogada-agent}"

if ! command -v tmux >/dev/null 2>&1; then
  echo "[fatal] tmux 가 설치돼 있지 않습니다. sudo apt install tmux 를 먼저 실행하세요." >&2
  exit 1
fi

if tmux has-session -t "$SESSION" 2>/dev/null; then
  echo "[skip] tmux 세션 '$SESSION' 이미 존재합니다. attach 로 확인하세요:"
  echo "        tmux attach -t $SESSION"
  exit 0
fi

ARGS=("$@")
if [[ ${#ARGS[@]} -eq 0 ]]; then
  ARGS=("build" "--target" "src/backend")
fi

CMD=". '$ROOT/.venv/bin/activate' && cd '$ROOT' && python scripts/run_agent.py ${ARGS[*]}"

echo "[start] session=$SESSION cmd=$CMD"
tmux new-session -d -s "$SESSION" "$CMD"

echo "[ok] tmux 세션 시작됨: $SESSION"
echo "      로그 확인: tmux attach -t $SESSION"
echo "      분리:       Ctrl+b 다음 d"
echo "      중지:       ./scripts/agent_stop.sh"
