#!/usr/bin/env bash
# submodule별 develop · test · operation 브랜치 생성.
#
# 루트 monorepo 가 아닌 src/backend, src/frontend 각각의 git 저장소에
# 3단계 브랜치를 만든다. 루트(.) 는 docs·transfer·agents 메타용 main 유지.
#
# 사용:
#   ./scripts/git_branch_setup.sh

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

PHASE_BRANCHES=(develop test operation)

setup_submodule_branches() {
  local name=$1
  local path=$2

  if [[ ! -d "$path" ]]; then
    echo "[skip] submodule path missing: $path ($name)"
    return 0
  fi

  if ! git -C "$path" rev-parse --git-dir >/dev/null 2>&1; then
    echo "[init] git 저장소 생성: $path"
    git -C "$path" init
    git -C "$path" add -A
    git -C "$path" commit -m "chore: initial commit for ogada ${name}" || true
  fi

  local base
  base="$(git -C "$path" symbolic-ref --short HEAD 2>/dev/null || echo main)"
  if ! git -C "$path" show-ref --verify --quiet "refs/heads/$base"; then
    base="main"
  fi

  for b in "${PHASE_BRANCHES[@]}"; do
    if git -C "$path" show-ref --verify --quiet "refs/heads/$b"; then
      echo "[skip] $name: branch exists: $b"
    else
      echo "[create] $name: $b (from $base)"
      git -C "$path" branch "$b" "$base"
    fi
  done

  if git -C "$path" show-ref --verify --quiet refs/heads/develop; then
    git -C "$path" checkout develop
  fi

  echo "[ok] $name branches:"
  git -C "$path" branch --list develop test operation main 2>/dev/null || true
  echo "       current: $(git -C "$path" branch --show-current)"
  echo ""
}

cd "$ROOT"

echo "=== submodule 브랜치 설정 ==="
setup_submodule_branches backend "$ROOT/src/backend"
setup_submodule_branches frontend "$ROOT/src/frontend"

# 루트 저장소 (docs·transfer·agents)
if ! git rev-parse --git-dir >/dev/null 2>&1; then
  echo "[init] 루트 git 저장소 생성"
  git init
  git add -A
  git commit -m "$(cat <<'EOF'
chore: initial commit for ogada meta repo

Docs, transfer, agent tooling. Code lives in src/backend and src/frontend submodules.
EOF
)"
fi

ROOT_BRANCH="$(git symbolic-ref --short HEAD 2>/dev/null || echo main)"

# 루트 기본 브랜치: main (docs·transfer·agents 메타)
if git show-ref --verify --quiet refs/heads/main; then
  git checkout main
elif [[ "$ROOT_BRANCH" != "main" ]]; then
  git checkout -B main
fi

echo "[ok] 루트 저장소 branch: $(git branch --show-current) (docs·transfer·agents)"
echo ""
echo "coder   → git -C src/backend checkout develop  (또는 src/frontend)"
echo "tester  → git -C src/backend checkout test      (또는 src/frontend)"
echo "planner → 루트 main (submodule checkout 불필요)"
