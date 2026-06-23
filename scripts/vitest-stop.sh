#!/usr/bin/env bash
# Stop stray frontend vitest / npm test processes (e.g. hung agent runs).
set -euo pipefail

LOCK_FILE="${OGADA_VITEST_LOCK_FILE:-/tmp/ogada-vitest.lock}"

before="$(pgrep -fc 'vitest run' 2>/dev/null || echo 0)"
pkill -f 'vitest run' 2>/dev/null || true
pkill -f 'npm test.*--run' 2>/dev/null || true
sleep 1
pkill -9 -f 'vitest' 2>/dev/null || true
rm -f "$LOCK_FILE"

after="$(pgrep -fc 'vitest' 2>/dev/null || echo 0)"
echo "vitest-stop: cleared (vitest run before=$before, remaining vitest=$after)"
