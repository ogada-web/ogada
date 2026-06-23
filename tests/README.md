# 회귀 테스트 메타 (tester)

> **owner**: TSR  
> **updated**: 2026-06-06T18:04:00+00:00  
> **실행 위치**: submodule `test` 브랜치 worktree (`src/backend-test`, `src/frontend-test`)

## Backend (`src/backend-test` @ test)

- 자동 테스트 (test 브랜치): `mvn -q test` — **79/79 PASS** (23 suites, 2026-06-06T18:03)
- Package: `mvn -q -DskipTests package` — **SUCCESS** (JAR 76,466,058 B)
- develop HEAD (`fac3d07`): `@Test` grep **98** — merge 후 ~101 예상 (working tree +3 guardian RBAC WIP)
- BLOCK: ROADMAP `merge_status: pending`, develop dirty-tree (**B02 recurrence**), develop→test merge 미실행
- 상세: `docs/qa/TEST_REPORT.md` §1·§4, `transfer/backend/checklists/test.md`

## Frontend (`src/frontend-test` @ test)

- 14차 baseline 유효 — develop HEAD `998ac87`, working tree DIRTY (19 files, B07 recurrence Planned)
- 상세: `docs/qa/TEST_REPORT.md` F-1

## 루트 `tests/` 통합 스위트

- **미구축** — submodule worktree 단위 테스트·빌드가 1차 회귀 기준
- 후속: merge 후 cross-stream smoke 스크립트 검토

## 후속 (coder develop)

1. Backend: **B02 recurrence** — `RoleBasedControllerAccessTest` guardian RBAC WIP commit or revert
2. ROADMAP v1 완료 기준 충족 → `merge_status: ready`
3. develop → test merge → tester 재검증 (clean tree ~101 PASS 기대)
