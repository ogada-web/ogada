#!/usr/bin/env bash
# submodule develop → test merge (test worktree 에서 수행).
# ROADMAP merge_status=ready 일 때 run_agent.py 가 자동 merge 하므로 보통은 불필요.
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
  backend)
    PRIMARY="$ROOT/src/backend"
    TEST_WT="$ROOT/src/backend-test"
    ;;
  frontend)
    PRIMARY="$ROOT/src/frontend"
    TEST_WT="$ROOT/src/frontend-test"
    ;;
  *)
    echo "[fatal] stream 은 backend 또는 frontend 여야 합니다." >&2
    exit 1
    ;;
esac

DEVELOP="develop"
TEST="test"

if ! git -C "$PRIMARY" rev-parse --git-dir >/dev/null 2>&1; then
  echo "[fatal] submodule git 저장소가 아닙니다: $PRIMARY" >&2
  exit 1
fi

if ! git -C "$PRIMARY" worktree list --porcelain 2>/dev/null | grep -q "^worktree $TEST_WT$"; then
  echo "[fatal] test worktree 없음: $TEST_WT — ./scripts/git_branch_setup.sh 실행" >&2
  exit 1
fi

echo "[merge] $STREAM: ${DEVELOP} → ${TEST} (${VERSION}) in $TEST_WT"
git -C "$TEST_WT" checkout "$TEST"
git -C "$TEST_WT" merge "$DEVELOP" -m "chore(${STREAM}): merge ${DEVELOP} into ${TEST} (${VERSION})"

echo "[ok] merge 완료 (primary $PRIMARY 는 develop 유지)"
