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

## 에이전트 루프 회귀 테스트 (2026-10-07)

```bash
.venv/bin/python -m unittest discover -s tests -p 'test_agent_*.py' -v
```

`test_agent_runner.py`는 실행 실패의 종료 코드, push/merge 차단, live E2E 실패 전파, 명시적인 모델 고정과 키를 노출하지 않는 선택 모델 진단을 검증한다.

`test_agent_shell.py`는 임시 작업 공간과 가짜 실행 도구로 한 사이클의 순서, 실패 시 후속 단계·반복 차단, 사전 점검 실패, 팀 전체 일회 실행, SIGTERM 종료를 검증한다. 실제 API 호출·에이전트 기동·Git push는 수행하지 않는다.

## 후속 (coder develop)

1. Backend: **B02 recurrence** — `RoleBasedControllerAccessTest` guardian RBAC WIP commit or revert
2. ROADMAP v1 완료 기준 충족 → `merge_status: ready`
3. develop → test merge → tester 재검증 (clean tree ~101 PASS 기대)
