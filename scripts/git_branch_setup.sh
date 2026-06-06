#!/usr/bin/env bash
# backend/frontend × develop·migration·operation 브랜치 6개 생성.
#
# 사용:
#   ./scripts/git_branch_setup.sh
#
# 최초 실행 시 git init + 초기 커밋 후 브랜치를 만든다.
# 이미 git 저장소면 현재 HEAD 에서 브랜치만 추가(없을 때).

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

BRANCHES=(
  backend/develop
  backend/migration
  backend/operation
  frontend/develop
  frontend/migration
  frontend/operation
)

cd "$ROOT"

if ! git rev-parse --git-dir >/dev/null 2>&1; then
  echo "[init] git 저장소 생성"
  git init
  git add -A
  git commit -m "$(cat <<'EOF'
chore: initial commit for ogada monorepo

Backend (Java Spring Boot) + frontend (React Vite) + docs + agent tooling.
EOF
)"
fi

BASE="$(git symbolic-ref --short HEAD 2>/dev/null || echo backend/develop)"

for b in "${BRANCHES[@]}"; do
  if git show-ref --verify --quiet "refs/heads/$b"; then
    echo "[skip] branch exists: $b"
  else
    echo "[create] $b (from $BASE)"
    git branch "$b" "$BASE"
  fi
done

# 기본 작업 브랜치: backend/develop
if git show-ref --verify --quiet refs/heads/backend/develop; then
  git checkout backend/develop
fi

echo ""
echo "[ok] 브랜치 목록:"
git branch --list 'backend/*' 'frontend/*'
echo ""
echo "현재 브랜치: $(git branch --show-current)"
echo "coder  → backend/develop 또는 frontend/develop"
echo "tester → backend/migration 또는 frontend/migration"
