#!/usr/bin/env bash
# submodule 내부 develop → test 수동 merge.
# ROADMAP merge_status=ready 일 때 coder build 가 자동 merge 하므로 보통은 불필요.
#
# 사용:
#   ./scripts/git_merge_to_test.sh backend
#   ./scripts/git_merge_to_test.sh frontend

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
STREAM="${1:-backend}"
VERSION="${2:-manual}"

case "$STREAM" in
  backend) SUBMODULE="$ROOT/src/backend" ;;
  frontend) SUBMODULE="$ROOT/src/frontend" ;;
  *)
    echo "[fatal] stream 은 backend 또는 frontend 여야 합니다." >&2
    exit 1
    ;;
esac

DEVELOP="develop"
TEST="test"

if ! git -C "$SUBMODULE" rev-parse --git-dir >/dev/null 2>&1; then
  echo "[fatal] submodule git 저장소가 아닙니다: $SUBMODULE" >&2
  exit 1
fi

CURRENT="$(git -C "$SUBMODULE" branch --show-current 2>/dev/null || true)"

echo "[merge] $STREAM: ${DEVELOP} → ${TEST} (${VERSION}) in $SUBMODULE"
git -C "$SUBMODULE" checkout "$TEST"
git -C "$SUBMODULE" merge "$DEVELOP" -m "chore(${STREAM}): merge ${DEVELOP} into ${TEST} (${VERSION})"

if [[ -n "$CURRENT" ]]; then
  git -C "$SUBMODULE" checkout "$CURRENT"
else
  git -C "$SUBMODULE" checkout "$DEVELOP"
fi

echo "[ok] merge 완료"
