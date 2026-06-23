#!/usr/bin/env bash
# Run frontend vitest with a repo-wide flock so only one npm test can run at a time.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
FRONTEND_DIR="$ROOT_DIR/src/frontend"
LOCK_FILE="${OGADA_VITEST_LOCK_FILE:-/tmp/ogada-vitest.lock}"

if [[ ! -d "$FRONTEND_DIR" ]]; then
  echo "npm-test-locked: frontend dir not found: $FRONTEND_DIR" >&2
  exit 1
fi

exec 9>"$LOCK_FILE"
if ! flock -n 9; then
  holder="$(fuser "$LOCK_FILE" 2>/dev/null | tr ' ' '\n' | head -1 || true)"
  echo "vitest: another npm test is already running (lock: $LOCK_FILE${holder:+, pid $holder})" >&2
  echo "  status: ps aux | grep -E '[v]itest run'" >&2
  echo "  stop:   $SCRIPT_DIR/vitest-stop.sh" >&2
  echo "  doc:    docs/qa/VITEST_CONCURRENCY.md" >&2
  exit 75
fi

cd "$FRONTEND_DIR"
echo "vitest: locked run started at $(date -u +%H:%M:%S)Z — full suite ~6–8 min; 15min+ no output = hang (docs/qa/VITEST_CONCURRENCY.md)" >&2
exec npx vitest run "$@"
