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

  git -C "$path" fetch origin 2>/dev/null || true

  local base=""
  if git -C "$path" show-ref --verify --quiet refs/remotes/origin/develop; then
    base="origin/develop"
  elif git -C "$path" show-ref --verify --quiet refs/remotes/origin/main; then
    base="origin/main"
  else
    base="$(git -C "$path" symbolic-ref --short HEAD 2>/dev/null || echo main)"
    if ! git -C "$path" show-ref --verify --quiet "refs/heads/$base"; then
      base="main"
    fi
  fi

  for b in "${PHASE_BRANCHES[@]}"; do
    if git -C "$path" show-ref --verify --quiet "refs/heads/$b"; then
      if [[ "$b" == "develop" && "$base" == "origin/develop" ]]; then
        local local_sha remote_sha
        local_sha="$(git -C "$path" rev-parse "refs/heads/$b" 2>/dev/null || true)"
        remote_sha="$(git -C "$path" rev-parse "refs/remotes/origin/develop" 2>/dev/null || true)"
        if [[ -n "$local_sha" && -n "$remote_sha" && "$local_sha" != "$remote_sha" ]]; then
          echo "[sync] $name: develop ← origin/develop (was stale)"
          git -C "$path" branch -f develop origin/develop
        else
          echo "[skip] $name: branch exists: $b"
        fi
      else
        echo "[skip] $name: branch exists: $b"
      fi
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

setup_worktree() {
  local name=$1
  local primary=$2
  local wt_path=$3
  local branch=$4
  local develop_branch=$5

  if [[ ! -d "$primary" ]]; then
    echo "[skip] worktree primary missing: $primary ($name)"
    return 0
  fi

  if ! git -C "$primary" rev-parse --git-dir >/dev/null 2>&1; then
    echo "[skip] worktree git repo missing: $primary ($name)"
    return 0
  fi

  if git -C "$primary" worktree list --porcelain 2>/dev/null | grep -q "^worktree $wt_path$"; then
    echo "[skip] $name worktree exists: $wt_path"
    git -C "$wt_path" checkout "$branch" 2>/dev/null || true
    echo "       worktree branch: $(git -C "$wt_path" branch --show-current)"
    echo ""
    return 0
  fi

  if [[ -e "$wt_path" ]]; then
    echo "[warn] $name: path exists but is not a registered worktree: $wt_path" >&2
    echo "       remove or rename it, then re-run this script." >&2
    echo ""
    return 0
  fi

  local current
  current="$(git -C "$primary" branch --show-current 2>/dev/null || true)"
  if [[ "$current" == "$branch" ]]; then
    echo "[prep] $name: primary is on $branch — switching primary to $develop_branch"
    if ! git -C "$primary" checkout "$develop_branch" 2>/dev/null; then
      echo "[fatal] $name: cannot checkout $develop_branch on $primary (dirty tree?)." >&2
      echo "        commit or stash changes in $primary, then re-run." >&2
      exit 1
    fi
  fi

  echo "[create] $name worktree: $wt_path ← $branch"
  git -C "$primary" worktree add "$wt_path" "$branch"
  git -C "$primary" checkout "$develop_branch" 2>/dev/null || true
  echo "[ok] $name worktrees:"
  git -C "$primary" worktree list
  echo ""
}

cd "$ROOT"

echo "=== submodule 초기화 (git submodule) ==="
git submodule update --init src/backend src/frontend 2>/dev/null || {
  git submodule update --init --recursive
}

echo "=== submodule 브랜치 설정 ==="
setup_submodule_branches backend "$ROOT/src/backend"
setup_submodule_branches frontend "$ROOT/src/frontend"

echo "=== test worktree (coder/tester 분리) ==="
setup_worktree backend "$ROOT/src/backend" "$ROOT/src/backend-test" test develop
setup_worktree frontend "$ROOT/src/frontend" "$ROOT/src/frontend-test" test develop

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
echo "coder   → src/backend · src/frontend @ develop (주 worktree)"
echo "tester  → src/backend-test · src/frontend-test @ test (별도 worktree)"
echo "planner → 루트 main (submodule checkout 불필요)"
