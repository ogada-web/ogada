#!/usr/bin/env bash
# 실백엔드 Live E2E (src/frontend/src/e2e/**)
#
# 전제: PostgreSQL + Spring Boot API 기동 (scripts/dev-backend.env)
# 사용:
#   ./scripts/run-live-e2e.sh
#   ./scripts/run-live-e2e.sh src/e2e/transportLiveApi.e2e.test.js

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

"$SCRIPT_DIR/setup-dev-live-e2e-env.sh" || true

if [[ -f "$SCRIPT_DIR/dev-live-e2e.env" ]]; then
  # shellcheck source=/dev/null
  source "$SCRIPT_DIR/dev-live-e2e.env"
elif [[ -f "$SCRIPT_DIR/dev-live-e2e.env.example" ]]; then
  # shellcheck source=/dev/null
  source "$SCRIPT_DIR/dev-live-e2e.env.example"
fi

export LIVE_E2E="${LIVE_E2E:-1}"
export VITE_API_BASE="${VITE_API_BASE:-http://127.0.0.1:8080}"
export LIVE_E2E_EMAIL="${LIVE_E2E_EMAIL:-test@test.com}"
export LIVE_E2E_PASSWORD="${LIVE_E2E_PASSWORD:-ogada1234}"

if [[ -z "${LIVE_E2E_CLIENT_ID:-}" ]]; then
  if [[ -f "$SCRIPT_DIR/dev-backend.env" ]]; then
    # shellcheck source=/dev/null
    source "$SCRIPT_DIR/dev-backend.env"
  fi
  LIVE_E2E_CLIENT_ID="$(
    PGPASSWORD="${DB_PASSWORD:-ogada}" psql -h localhost -U "${DB_USERNAME:-ogada}" -d ogada -t -A \
      -c "SELECT id::text FROM clients WHERE is_active = true ORDER BY created_at LIMIT 1;" 2>/dev/null || true
  )"
  export LIVE_E2E_CLIENT_ID
fi

if ! curl -sf "${VITE_API_BASE}/api/v1/health" >/dev/null; then
  echo "[live-e2e] fatal: API가 응답하지 않습니다 — ${VITE_API_BASE}" >&2
  echo "[live-e2e] hint: backend 기동 후 다시 실행 (docs/ops/DEPLOYMENT_GUIDE.md §3-4)" >&2
  exit 2
fi

if [[ -z "${LIVE_E2E_CLIENT_ID:-}" ]]; then
  echo "[live-e2e] warn: LIVE_E2E_CLIENT_ID 없음 — pilotLiveApi 일부·guardian 테스트 실패 가능" >&2
  echo "[live-e2e] hint: scripts/seed-dev-fixtures.sql 또는 이용자 1건 등록 후 재실행" >&2
fi

echo "[live-e2e] API=${VITE_API_BASE} email=${LIVE_E2E_EMAIL} client=${LIVE_E2E_CLIENT_ID:-<none>} write=${LIVE_E2E_WRITE:-0}"

cd "$ROOT/src/frontend"
if [[ $# -gt 0 ]]; then
  exec npx vitest run --config vitest.live.config.js "$@"
fi
exec npm run test:live-e2e
