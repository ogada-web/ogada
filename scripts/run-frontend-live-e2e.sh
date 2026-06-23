#!/usr/bin/env bash
# npm run test:live-e2e entry (src/frontend or src/frontend-test).
# QA-B131: frontend-test is its own git root with a local scripts/ dir but no
# npm-test-locked.sh — always resolve the ogada monorepo scripts/ directory.

set -euo pipefail

resolve_scripts_dir() {
  local candidate

  candidate="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
  if [[ -x "$candidate/npm-test-locked.sh" ]]; then
    echo "$candidate"
    return 0
  fi

  if [[ -x "${PWD}/../../scripts/npm-test-locked.sh" ]]; then
    echo "$(cd "${PWD}/../.." && pwd)/scripts"
    return 0
  fi

  candidate="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
  if [[ -x "$candidate/scripts/npm-test-locked.sh" ]]; then
    echo "$candidate/scripts"
    return 0
  fi

  echo "run-frontend-live-e2e: npm-test-locked.sh not found" >&2
  exit 127
}

SCRIPTS_DIR="$(resolve_scripts_dir)"

if [[ -x "$SCRIPTS_DIR/setup-dev-live-e2e-env.sh" ]]; then
  "$SCRIPTS_DIR/setup-dev-live-e2e-env.sh" || true
fi

set -a
if [[ -f "$SCRIPTS_DIR/dev-live-e2e.env.example" ]]; then
  # shellcheck source=/dev/null
  source "$SCRIPTS_DIR/dev-live-e2e.env.example"
fi
if [[ -f "$SCRIPTS_DIR/dev-live-e2e.env" ]]; then
  # shellcheck source=/dev/null
  source "$SCRIPTS_DIR/dev-live-e2e.env"
fi
if [[ -f "$SCRIPTS_DIR/dev-backend.env" ]]; then
  # shellcheck source=/dev/null
  source "$SCRIPTS_DIR/dev-backend.env"
fi
set +a

export LIVE_E2E_SCRIPTS_DIR="$SCRIPTS_DIR"
export LIVE_E2E="${LIVE_E2E:-1}"
export VITE_API_BASE="${VITE_API_BASE:-http://127.0.0.1:8080}"

if [[ -z "${LIVE_E2E_CLIENT_ID:-}" ]] && command -v psql >/dev/null 2>&1; then
  LIVE_E2E_CLIENT_ID="$(
    PGPASSWORD="${DB_PASSWORD:-ogada}" psql -h localhost -U "${DB_USERNAME:-ogada}" -d ogada -t -A \
      -c "SELECT id::text FROM clients WHERE is_active = true ORDER BY created_at LIMIT 1;" 2>/dev/null || true
  )"
  export LIVE_E2E_CLIENT_ID
fi

exec bash "$SCRIPTS_DIR/npm-test-locked.sh" --config vitest.live.config.js "$@"
