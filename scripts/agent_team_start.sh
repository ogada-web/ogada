#!/usr/bin/env bash
# coder + db_architect + tech_writer 를 각각 별도 tmux 세션에서 loop 실행.
#
# 사용 전:
#   1) build 1회 수동 실행으로 Java 초기화가 되는지 확인
#   2) git -C src/backend commit 등으로 스냅샷 저장
#
# 사용 예:
#   ./scripts/agent_team_start.sh
#   ./scripts/agent_team_start.sh --no-loop    # 각 역할 1회만
#
# 환경변수:
#   AGENT_INTERVAL_SECONDS=900          coder·db_architect loop 간격(초)
#   AGENT_WRITER_INTERVAL_SECONDS=3600  tech_writer loop 간격(초, 기본 1시간)

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
VENV="$ROOT/.venv/bin/activate"

CODER_SESSION="${AGENT_CODER_SESSION:-ogada-coder}"
DB_SESSION="${AGENT_DB_SESSION:-ogada-db}"
WRITER_SESSION="${AGENT_WRITER_SESSION:-ogada-writer}"

CODER_INTERVAL="${AGENT_INTERVAL_SECONDS:-900}"
WRITER_INTERVAL="${AGENT_WRITER_INTERVAL_SECONDS:-3600}"

LOOP_FLAG=(--loop)
if [[ "${1:-}" == "--no-loop" ]]; then
  LOOP_FLAG=()
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

# coder: Java/React 구현 (15분 간격, backend/develop)
start_session "$CODER_SESSION" \
  build --role coder --stream backend --target src/backend "${LOOP_FLAG[@]}"

# db_architect: ERD + Flyway SQL (15분 간격)
start_session "$DB_SESSION" \
  build --role db_architect "${LOOP_FLAG[@]}"

# tech_writer: 문서 (1시간 간격 — 가끔)
start_session "$WRITER_SESSION" \
  build --role tech_writer --interval "$WRITER_INTERVAL" "${LOOP_FLAG[@]}"

echo ""
echo "[ok] 팀 에이전트 tmux 세션"
echo "  coder        : tmux attach -t $CODER_SESSION   (interval ${CODER_INTERVAL}s)"
echo "  db_architect : tmux attach -t $DB_SESSION      (interval ${CODER_INTERVAL}s)"
echo "  tech_writer  : tmux attach -t $WRITER_SESSION   (interval ${WRITER_INTERVAL}s)"
echo ""
echo "  전체 상태: ./scripts/agent_team_status.sh"
echo "  전체 중지: ./scripts/agent_team_stop.sh"
