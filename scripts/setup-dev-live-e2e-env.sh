#!/usr/bin/env bash
# Creates scripts/dev-live-e2e.env from example when absent (QA-B95).
# Safe to run repeatedly — never overwrites an existing file.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
TARGET="$SCRIPT_DIR/dev-live-e2e.env"
EXAMPLE="$SCRIPT_DIR/dev-live-e2e.env.example"

if [[ ! -f "$EXAMPLE" ]]; then
  echo "[setup-dev-live-e2e-env] fatal: missing $EXAMPLE" >&2
  exit 1
fi

if [[ -f "$TARGET" ]]; then
  echo "[setup-dev-live-e2e-env] ok: $TARGET already exists"
  exit 0
fi

cp "$EXAMPLE" "$TARGET"
echo "[setup-dev-live-e2e-env] created $TARGET from example"
echo "[setup-dev-live-e2e-env] edit LIVE_E2E_* values as needed (file is gitignored)"
