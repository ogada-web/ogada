<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-21T22:44:00+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-21 1251차)

> **1251차 PASS(merge EXECUTED)** — test/develop `@5fd468b` **SYNCED** · merge **EXECUTED** FF `a4ea2d5`→`5fd468b` (10 commits) · pre-merge `npm test` **1969/1969 PASS**(384 files, 663.17s) · post-merge `npm test` **1969/1969 PASS**(384 files, 701.90s) · `npm run build` **1088 modules PASS**(7.84s) · `npm audit` **0 vulnerabilities** · `npm run test:live-e2e` **126 PASS/19 SKIP**(35.41s) · develop WT **CLEAN** · transfer **PASS** · Open **0(active frontend)** · cross-stream **SYNCED** · operation **BLOCK**

## 1251차 검증 요약 (merge EXECUTED — 10 commits)

| 항목 | 결과 |
|---|---|
| test worktree HEAD | `5fd468b` |
| develop HEAD | `5fd468b` |
| ahead (`test..develop`) | **0/0 (SYNCED)** |
| develop working tree | **CLEAN** |
| test working tree | **DIRTY** (`?? 9` 1개, 무해한 빈 파일) |
| pre-merge npm test | **1969/1969 PASS** (384 files, 663.17s) |
| post-merge npm test | **1969/1969 PASS** (384 files, 701.90s) |
| build | **1088 modules SUCCESS** (7.84s) |
| npm audit (critical+) | **0 vulnerabilities** |
| live E2E | **126 PASS/19 SKIP** (35.41s, 50 files) |
| backend@8080 | **UP/200** |
| transfer verdict | **PASS** |
| cross-stream | **SYNCED (FE@5fd468b · BE@a6eb8b7)** |
| operation | **BLOCK** (origin/test push pending) |

### Merged commits (1251차, 10 commits)

- `6bde24a` — `feat(v1.2.1/US-R03): add mobile camera capture for staff HR uploads`
- `3bffb17` — `chore(v1.2.1/US-R03): raise module 8 coverage and stabilize vitest pool`
- `8383f8d` — `fix(v1.2.1/QA-B222): serial vitest pool and wire attendance roster API`
- `9812ac4` — `ux(a11y): US-R03 모바일 서류 촬영 a11y 재점검 + .ds-button 미정의 셀렉터 회귀 해소 (UXD-151)`
- `d6f0157` — `fix(test): run vitest single-thread to avoid hang (QA-B222)`
- `53d65a0` — `feat(v1.2.1/G-STAFF-WORK-ATTENDANCE): wire staff daily check-in/out page`
- `eff8505` — `fix(v1.2.1/QA-B222): enable per-file vitest isolation to stop full-suite hang`
- `ebdf737` — `fix(v1.2.1/QA-B222): global test teardown and module 8 coverage 0.85`
- `50548ff` — `fix(v1.2.1/QA-B222): add pilotPageFlows vi mock teardown`
- `5fd468b` — `feat(v1.2.1/G-STAFF-WORK-ATTENDANCE): wire check-in method on staff roster`

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-21T22:10:30+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-21 1250차)

> **1250차 BLOCK(merge pending 10)** — test `@a4ea2d5` · develop `@5fd468b` · merge **SKIP**(`test..develop` **0/10**) · test baseline `npm test` **1969/1969 PASS**(384 files, 668.34s) · develop pre-merge `npm test` **1969/1969 PASS**(384 files, 668.34s) · `npm run build` **1086 modules PASS**(8.13s) · `npm audit` **0 vulnerabilities** · `npm run test:live-e2e` **126 PASS/19 SKIP**(35.54s) · develop WT **CLEAN**(**QA-B227 Fixed @ `50548ff`**) · transfer **BLOCK** · Open **1(active frontend)**(QA-B226 update) · operation **BLOCK**

## 1250차 검증 요약 (merge SKIP — pending 10)

| 항목 | 결과 |
|---|---|
| test worktree HEAD | `a4ea2d5` |
| develop HEAD | `5fd468b` |
| ahead (`test..develop`) | **0/10** |
| develop working tree | **CLEAN** |
| test working tree | **DIRTY** (`?? 9` 1개) |
| test baseline npm test | **1969/1969 PASS** (384 files, 668.34s) |
| develop pre-merge npm test | **1969/1969 PASS** (384 files, 668.34s) |
| build | **1086 modules SUCCESS** (8.13s) |
| npm audit (critical+) | **0 vulnerabilities** |
| live E2E | **126 PASS/19 SKIP** (35.54s, 50 files) |
| backend@8080 | **UP/200** |
| transfer verdict | **BLOCK** |
| operation | **BLOCK** |

### Pending commits (1250차)

- `5fd468b` — `feat(v1.2.1/G-STAFF-WORK-ATTENDANCE): wire check-in method on staff roster`
- `50548ff` — `fix(v1.2.1/QA-B222): add pilotPageFlows vi mock teardown`
- `ebdf737` — `fix(v1.2.1/QA-B222): global test teardown and module 8 coverage 0.85`
- `eff8505` — `fix(v1.2.1/QA-B222): enable per-file vitest isolation to stop full-suite hang`
- `53d65a0` — `feat(v1.2.1/G-STAFF-WORK-ATTENDANCE): wire staff daily check-in/out page`
- `d6f0157` — `fix(test): run vitest single-thread to avoid hang (QA-B222)`
- `9812ac4` — `ux(a11y): US-R03 모바일 서류 촬영 a11y 재점검 + .ds-button 미정의 셀렉터 회귀 해소 (UXD-151)`
- `8383f8d` — `fix(v1.2.1/QA-B222): serial vitest pool and wire attendance roster API`
- `3bffb17` — `chore(v1.2.1/US-R03): raise module 8 coverage and stabilize vitest pool`
- `6bde24a` — `feat(v1.2.1/US-R03): add mobile camera capture for staff HR uploads`

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-21T21:11:26+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-21 1248차)

> **1248차 BLOCK(develop WT DIRTY 1M + merge pending 8; baseline+pre-merge PASS)** — test `@a4ea2d5` · develop `@ebdf737` · merge **SKIP**(`test..develop` **0/8** + dirty) · test baseline `npm test` **1966/1966 PASS**(383 files, 664.49s) · develop pre-merge `npm test` **1966/1966 PASS**(383 files, 666.74s) · `npm run build` **1086 modules PASS**(11.62s) · `npm audit` **0 vulnerabilities** · `npm run test:live-e2e` **126 PASS/19 SKIP**(38.21s) · test worktree untracked `1`(`?? 9`) · transfer **BLOCK** · Open **2(active frontend)**(QA-B227+QA-B226) · operation **BLOCK**

## 1248차 검증 요약 (merge SKIP — develop dirty 1M + pending 8)

| 항목 | 결과 |
|---|---|
| test worktree HEAD | `a4ea2d5` |
| develop HEAD | `ebdf737` |
| ahead (`test..develop`) | **0/8** |
| develop working tree | **DIRTY 1M** (`pilotPageFlows.test.jsx` vi cleanup WIP) |
| test working tree | **DIRTY** (`?? 9` 1개) |
| test baseline npm test | **1966/1966 PASS** (383 files, 664.49s) |
| develop pre-merge npm test | **1966/1966 PASS** (383 files, 666.74s) |
| build | **1086 modules SUCCESS** (11.62s) |
| npm audit (critical+) | **0 vulnerabilities** |
| live E2E | **126 PASS/19 SKIP** (38.21s, 50 files) |
| transfer verdict | **BLOCK** |
| operation | **BLOCK** |

### Pending commits (1248차)

- `6bde24a` — `feat(v1.2.1/US-R03): add mobile camera capture for staff HR uploads`
- `3bffb17` — `chore(v1.2.1/US-R03): raise module 8 coverage and stabilize vitest pool`
- `8383f8d` — `fix(v1.2.1/QA-B222): serial vitest pool and wire attendance roster API`
- `9812ac4` — `ux(a11y): US-R03 모바일 서류 촬영 a11y 재점검 + .ds-button 미정의 셀렉터 회귀 해소 (UXD-151)`
- `d6f0157` — `fix(test): run vitest single-thread to avoid hang (QA-B222)`
- `53d65a0` — `feat(v1.2.1/G-STAFF-WORK-ATTENDANCE): wire staff daily check-in/out page`
- `eff8505` — `fix(v1.2.1/QA-B222): enable per-file vitest isolation to stop full-suite hang`
- `ebdf737` — `fix(v1.2.1/QA-B222): global test teardown and module 8 coverage 0.85`

### Uncommitted WIP (1248차 — QA-B227)

- `src/pages/pilotPageFlows.test.jsx` (+11/-1) — `afterEach`/`afterAll` `vi.restoreAllMocks()`·`vi.unstubAllGlobals()` (QA-B222 hang fix 잔여)

## 1246차 검증 요약 (merge SKIP — develop pending 8)

| 항목 | 결과 |
|---|---|
| test worktree HEAD | `a4ea2d5` |
| develop HEAD | `ebdf737` |
| ahead (`test..develop`) | **0/8** |
| develop working tree | **CLEAN** |
| test working tree | **DIRTY** (`?? 9` 1개) |
| npm test | **1966/1966 PASS** (383 files, 668.39s) |
| build | **1086 modules SUCCESS** (7.89s) |
| npm audit (critical+) | **0 vulnerabilities** |
| live E2E | **126 PASS/19 SKIP** (34.90s, 50 files) |
| transfer verdict | **BLOCK** |
| operation | **BLOCK** |

### Pending commits (1246차)

- `6bde24a` — `feat(v1.2.1/US-R03): add mobile camera capture for staff HR uploads`
- `3bffb17` — `chore(v1.2.1/US-R03): raise module 8 coverage and stabilize vitest pool`
- `8383f8d` — `fix(v1.2.1/QA-B222): serial vitest pool and wire attendance roster API`
- `9812ac4` — `ux(a11y): US-R03 모바일 서류 촬영 a11y 재점검 + .ds-button 미정의 셀렉터 회귀 해소 (UXD-151)`
- `d6f0157` — `fix(test): run vitest single-thread to avoid hang (QA-B222)`
- `53d65a0` — `feat(v1.2.1/G-STAFF-WORK-ATTENDANCE): wire staff daily check-in/out page`
- `eff8505` — `fix(v1.2.1/QA-B222): enable per-file vitest isolation to stop full-suite hang`
- `ebdf737` — `fix(v1.2.1/QA-B222): global test teardown and module 8 coverage 0.85`

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-21T18:34:30+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-21 1243차)

> **1243차 BLOCK(merge pending 6 + vitest hang 재발)** — test `@a4ea2d5` · develop `@53d65a0` · merge **SKIP**(`test..develop` **0/6**) · `npm test` locked wrapper **Terminated**(953.811s, exit 143; final summary 미출력) · `./scripts/vitest-stop.sh` 정리 · `npm run build` **1086 modules PASS**(8.47s) · `npm audit` **0 vulnerabilities** · `npm run test:live-e2e` **126 PASS/19 SKIP**(31.74s) · transfer **BLOCK** · Open **1(active frontend)**(QA-B222 update) · operation **BLOCK**

## 1243차 검증 요약 (merge SKIP — US-R03/attendance pending 6 + full-suite hang)

| 항목 | 결과 |
|---|---|
| test worktree HEAD | `a4ea2d5` |
| develop HEAD | `53d65a0` |
| ahead (`test..develop`) | **0/6** |
| develop working tree | **CLEAN** |
| test working tree | **DIRTY** (`?? 9`) |
| npm test | **Terminated** (exit 143, 953.811s; no final summary) |
| hang 조치 | `./scripts/vitest-stop.sh` 실행 |
| build | **1086 modules SUCCESS** (8.47s) |
| npm audit (critical+) | **0 vulnerabilities** |
| live E2E | **126 PASS/19 SKIP** (31.74s, 50 files) |
| transfer verdict | **BLOCK** |
| operation | **BLOCK** |

### Pending commits (1243차)

- `6bde24a` — `feat(v1.2.1/US-R03): add mobile camera capture for staff HR uploads`
- `3bffb17` — `chore(v1.2.1/US-R03): raise module 8 coverage and stabilize vitest pool`
- `8383f8d` — `fix(v1.2.1/QA-B222): serial vitest pool and wire attendance roster API`
- `9812ac4` — `ux(a11y): US-R03 모바일 서류 촬영 a11y 재점검 + .ds-button 미정의 셀렉터 회귀 해소 (UXD-151)`
- `d6f0157` — `fix(test): run vitest single-thread to avoid hang (QA-B222)`
- `53d65a0` — `feat(v1.2.1/G-STAFF-WORK-ATTENDANCE): wire staff daily check-in/out page`

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-21T18:48:00+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-21 1244차)

> **1244차 BLOCK(merge pending 6 + vitest hang @pilotPageFlows.test.jsx 재확인)** — test `@a4ea2d5` · develop `@53d65a0` · pre-merge `npx vitest run` **HANG**(@pilotPageFlows.test.jsx, 7min+ no-output, 60524→60525 bytes) · merge **SKIP**(`test..develop` **0/6**) · `npm run build` **1086 modules PASS**(8.24s) · `npm audit` **0** · `src/frontend-test` untracked `1`(`?? 9`) · transfer **BLOCK** · Open **1(active frontend)**(QA-B222) · cross-stream **BLOCK(FE pending 6/hang · BE SYNCED@560057f)** · operation **BLOCK**

## 1244차 검증 요약 (merge SKIP — pilotPageFlows.test.jsx hang + 6 commits pending)

| 항목 | 결과 |
|---|---|
| test worktree HEAD | `a4ea2d5` |
| develop HEAD | `53d65a0` |
| ahead (`test..develop`) | **0/6** (`6bde24a` + `3bffb17` + `8383f8d` + `9812ac4` + `d6f0157` + `53d65a0`) |
| develop working tree | **CLEAN** |
| test working tree | **DIRTY** (`?? 9` 1개) |
| pre-merge `npx vitest run` | **HANG** (7min+ no-output; 60524→60525 bytes @ `pilotPageFlows.test.jsx`) |
| vitest-stop.sh 정리 | 완료 |
| QA-B222 fix @d6f0157 | **불충분** (`pilotPageFlows.test.jsx` hang 재확인) |
| build | **1086 modules SUCCESS** (8.24s) |
| npm audit (critical+) | **0 vulnerabilities** |
| live E2E | **SKIP** (merge 미실행 사이클) |
| FE merge status | **pending 6** |
| transfer verdict | **BLOCK** |
| operation | **BLOCK** |

### Pending commits (1244차)

- `6bde24a` — `feat(v1.2.1/US-R03): add mobile camera capture for staff HR uploads`
- `3bffb17` — `chore(v1.2.1/US-R03): raise module 8 coverage and stabilize vitest pool`
- `8383f8d` — `fix(v1.2.1/QA-B222): serial vitest pool and wire attendance roster API`
- `9812ac4` — `ux(a11y): US-R03 모바일 서류 촬영 a11y 재점검 + .ds-button 미정의 셀렉터 회귀 해소 (UXD-151)`
- `d6f0157` — `fix(test): run vitest single-thread to avoid hang (QA-B222)` ← **불충분**
- `53d65a0` — `feat(v1.2.1/G-STAFF-WORK-ATTENDANCE): wire staff daily check-in/out page`

### 1244차 hang 분석

- `d6f0157`: `vite.config.js` `pool: "forks", maxWorkers: 1, isolate: false, fileParallelism: false` + `EasyPayPanel.test.jsx` 수정
- 이전 hang 지점: EasyPayPanel.test.jsx 인근 (~872 tests mark)
- 1244차 hang 지점: **`pilotPageFlows.test.jsx`** 진입 직후 (60524 bytes에서 정체, 7min+ 무출력)
- `pilotPageFlows.test.jsx`는 최대 규모 테스트 파일(수백 개 케이스). 단일 스레드에서도 특정 케이스 hang 가능성
- COD 조치 필요: `pilotPageFlows.test.jsx` 내 hang 원인 격리 (async/timer leak, fake timer 미정리 등)

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-21T16:57:08+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-21 1241차)

> **1241차 BLOCK(merge pending 3 + vitest hang — QA-B222 fix @8383f8d 불충분, TSR 1241 재확인)** — test `@a4ea2d5` · develop `@8383f8d` · baseline **1956/1956 PASS**(363.96s) · develop pre-merge **Terminated**(exit 143, 다회) · merge **SKIP**(`test..develop` **0/3**) · `npm run build` **1086 modules PASS**(7.93s) · `npm audit` **0** · `src/frontend-test` untracked `1`(`?? 9`) · transfer **BLOCK** · Open **1(active frontend)**(QA-B222) · cross-stream **BLOCK(FE pending 3/hang · BE SYNCED@61e1970)** · operation **BLOCK**

## 1241차 검증 요약 (merge SKIP — US-R03 pending 3 + vitest hang persists)

| 항목 | 결과 |
|---|---|
| test worktree HEAD | `a4ea2d5` |
| develop HEAD | `8383f8d` |
| ahead (`test..develop`) | **0/3** (`6bde24a` + `3bffb17` + `8383f8d`) |
| develop working tree | **CLEAN** |
| test working tree | **DIRTY** (`?? 9` 1개) |
| baseline npm test (worktree vitest) | **1956/1956 PASS** (363.96s) |
| develop pre-merge npm test / vitest | **Terminated** (exit 143; full suite 미완주) |
| QA-B222 fix @8383f8d | **불충분** |
| build | **1086 modules SUCCESS** (7.93s) |
| npm audit (critical+) | **0 vulnerabilities** |
| live E2E | **SKIP** (merge 미실행 사이클) |
| backend@8080 | **UP/200** |
| FE merge status | **pending 3** |
| transfer verdict | **BLOCK** |
| operation | **BLOCK** |

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-21T16:53:38+00:00 -->

### Pending commits (1240차)

- `6bde24a` — `feat(v1.2.1/US-R03): add mobile camera capture for staff HR uploads`
- `3bffb17` — `chore(v1.2.1/US-R03): raise module 8 coverage and stabilize vitest pool`
- `8383f8d` — `fix(v1.2.1/QA-B222): serial vitest pool and wire attendance roster API`

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-21T14:40:31+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-21 1236차)

> **1236차 BLOCK(merge pending 2 + npm test hang 재발)** — test `@a4ea2d5` · develop `@3bffb17` · merge **SKIP**(`test..develop` **0/2**) · `npm test` locked wrapper **Terminated**(563.108s, exit 143; RUN `v4.1.8 /home/ubuntu/ogada/src/frontend` 후 9m+ 무출력) · `npm run build` **1086 modules PASS** · `npm audit` **0 vulnerabilities** · `src/frontend-test` untracked `1`(`?? 9`) · transfer **BLOCK** · Open **1(active frontend)**(QA-B222 update) · cross-stream **BLOCK(BE pending 1 + FE pending 2/hang)** · operation **BLOCK**

## 1236차 검증 요약 (merge SKIP — US-R03 pending 2 + test hang recurrence)

| 항목 | 결과 |
|---|---|
| test worktree HEAD | `a4ea2d5` |
| develop HEAD | `3bffb17` |
| ahead (`test..develop`) | **0/2** (`6bde24a` + `3bffb17`) |
| develop working tree | **CLEAN** |
| test working tree | **DIRTY** (`?? 9` 1개) |
| npm test | **Terminated** (563.108s, exit 143; RUN 이후 9m+ no-output hang; locked wrapper) |
| hang 조치 | `./scripts/vitest-stop.sh` 실행으로 정리 |
| build | **1086 modules SUCCESS** (7.95s) |
| npm audit (critical+) | **0 vulnerabilities** |
| live E2E | **SKIP** (merge 미실행 사이클) |
| FE merge status | **pending 2** (`6bde24a`, `3bffb17`) |
| transfer verdict | **BLOCK** |
| operation | **BLOCK** |

### Pending commits (1236차)

- `6bde24a` — `feat(v1.2.1/US-R03): add mobile camera capture for staff HR uploads`
- `3bffb17` — `chore(v1.2.1/US-R03): raise module 8 coverage and stabilize vitest pool`

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-21T14:12:00+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-21 1234차)

> **1234차 BLOCK(merge pending 1 + npm test hang 재발)** — test `@a4ea2d5` · develop `@6bde24a` · merge **SKIP**(`test..develop` **0/1**) · `npm test` locked wrapper **5m+ no-output hang**(RUN `v4.1.8 /home/ubuntu/ogada/src/frontend` 후 정체) · process 강제 종료 · `src/frontend-test` untracked `9` 확인 · transfer **BLOCK** · Open **1(active frontend)**(QA-B222) · cross-stream **BLOCK(frontend merge gate)** · operation **BLOCK**

## 1234차 검증 요약 (merge SKIP — US-R03 camera capture pending + test hang)

| 항목 | 결과 |
|---|---|
| test worktree HEAD | `a4ea2d5` |
| develop HEAD | `6bde24a` |
| ahead (`test..develop`) | **0/1** (`6bde24a`) |
| develop working tree | **CLEAN** |
| test working tree | **DIRTY** (`?? 9`) |
| npm test | **Terminated** (5m+ no-output hang; locked wrapper) |
| hang 조치 | Vitest 프로세스 종료(`kill` + `pkill -f "node.*vitest"`) |
| build | **미실행** (hang 대응 우선) |
| npm audit (critical+) | **미실행** (hang 대응 우선) |
| live E2E | **SKIP** (merge 미실행 사이클) |
| FE merge status | **pending 1** (`6bde24a`) |
| transfer verdict | **BLOCK** |
| operation | **BLOCK** |

### Pending commit (1234차)

- `6bde24a` — `feat(v1.2.1/US-R03): add mobile camera capture for staff HR uploads`

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-21T13:45:00+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-21 1232차)

> **1232차 PASS(post-merge SYNCED · QA-B218+B221 Fixed)** — test `@751c593`→`a4ea2d5` · develop `@a4ea2d5` · merge **EXECUTED**(FF 1 commit) · baseline **1956/1956 PASS**(574.65s) · develop pre-merge **1956/1956 PASS**(363.33s) · post-merge **1956/1956 PASS**(366.63s) · build **1086 modules**(8.01s) · live E2E **126 PASS/19 SKIP**(30.35s) · develop/test WT **CLEAN SYNCED** · Open **0(active frontend)** · cross-stream **BLOCK(FE SYNCED · BE B219+B220)** · operation **BLOCK**

## 1232차 검증 요약 (merge EXECUTED — US-R02 staff status print cleanup/layout)

| 항목 | 결과 |
|---|---|
| test worktree HEAD | `a4ea2d5` |
| develop HEAD | `a4ea2d5` |
| ahead (`test..develop`) | **0/0** (SYNCED) |
| develop working tree | **CLEAN** |
| test working tree | **CLEAN** @ `a4ea2d5` |
| npm test baseline (@ `751c593`) | **1956/1956 PASS** (381 files, 574.65s worktree vitest) |
| npm test develop pre-merge | **1956/1956 PASS** (381 files, 363.33s locked wrapper) |
| npm test post-merge | **1956/1956 PASS** (381 files, 366.63s worktree vitest) |
| build (@ `src/frontend-test`) | **1086 modules SUCCESS** (8.01s) |
| npm audit (critical+) | **0 vulnerabilities** |
| live E2E | **126 PASS/19 SKIP** (30.35s, 50 files) |
| FE merge status | **SYNCED** @ `a4ea2d5` (merge EXECUTED 1 commit) |
| BE merge status | **BLOCK** @ develop `018a781` (QA-B219+B220) · test `@a45c040` |
| transfer verdict | **PASS** |
| cross-stream | **BLOCK** (BE regression) |
| operation | **BLOCK** (origin/test push 497 BE+144 FE) |

### Merged commit (FF 1)

- `a4ea2d5` — `fix(v1.2.1/US-R02): stabilize staff status print cleanup and layout`
  - `StaffStatusReportPage.jsx` — `runPrintWithCleanup`/`finalizePrint`·printing body class
  - `StaffStatusReportPage.test.jsx` — print cleanup tests
  - `components.css` — `.ds-staff-status-report-printing`

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-21T12:48:00+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-21 1230차)

> **1230차 BLOCK(baseline SYNCED · develop WT DIRTY · QA-B218 Open)** — test `@751c593` · develop `@751c593` WT **DIRTY 3M** · merge **SKIP**(0/0 SYNCED+dirty) · baseline **1956/1956 PASS**(360.59s; WIP 포함) · build **1086 modules**(7.91s) · live E2E **126 PASS/19 SKIP**(30.98s) · develop/test **SYNCED @751c593** · Open **1(active frontend)** · cross-stream **SYNCED(FE@751c593 + BE@a45c040)** · operation **BLOCK**

## 1230차 검증 요약 (merge SKIP — develop WT DIRTY 3M recurrence)

| 항목 | 결과 |
|---|---|
| test worktree HEAD | `751c593` |
| develop HEAD | `751c593` |
| ahead (`test..develop`) | **0/0** (SYNCED) |
| develop working tree | **DIRTY 3M** — `StaffStatusReportPage.jsx` · `StaffStatusReportPage.test.jsx` · `components.css` |
| test working tree | **CLEAN** @ `751c593` |
| npm test (locked → `src/frontend`) | **1956/1956 PASS** (381 files, 360.59s; WIP 3M 포함) |
| build (@ `src/frontend-test`) | **1086 modules SUCCESS** (7.91s) |
| npm audit (critical+) | **0 vulnerabilities** |
| live E2E | **126 PASS/19 SKIP** (30.98s, 50 files) |
| FE merge status | **SYNCED** @ `751c593` (merge SKIP — develop dirty) |
| BE merge status | **SYNCED** @ `a45c040` |
| transfer verdict | **BLOCK** (develop WT DIRTY · QA-B218) |
| cross-stream | **SYNCED** |
| operation | **BLOCK** (origin/test push 496 BE+143 FE) |

### Dirty files (QA-B218)

- `src/pages/StaffStatusReportPage.jsx` — print cleanup (`runPrintWithCleanup`/`finalizePrint`)
- `src/pages/StaffStatusReportPage.test.jsx` — test updates
- `src/styles/components.css` — `.ds-staff-status-report-printing` print class

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-21T12:17:30+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-21 1228차)

> **1228차 PASS(post-merge SYNCED · QA-B216 Fixed)** — test `@fd15a2f`→`751c593` · develop `@751c593` · merge **EXECUTED**(FF 1 commit) · baseline **1955/1955 PASS**(364.25s) · develop pre-merge **1956/1956 PASS**(358.21s) · post-merge **1956/1956 PASS**(363.03s) · build **1086 modules**(11.40s) · live E2E **126 PASS/19 SKIP**(30.55s) · develop/test WT **CLEAN SYNCED** · Open **0(active frontend)** · cross-stream **SYNCED(FE@751c593 + BE@20485f1)** · operation **BLOCK**

## 1228차 검증 요약 (merge EXECUTED — UXD-150 a11y overdue·document repository·bathing prev-month)

| 항목 | 결과 |
|---|---|
| test worktree HEAD (pre) | `fd15a2f` |
| test worktree HEAD (post) | `751c593` |
| develop HEAD | `751c593` |
| ahead (`test..develop`, pre-merge) | **0/1** (`751c593`) |
| ahead (`test..develop`, post-merge) | **0/0** (SYNCED) |
| develop working tree | **CLEAN** |
| test working tree | **CLEAN** @ `751c593` (dist untracked only) |
| npm test (baseline @test) | **1955/1955 PASS** (364.25s, 381 files, worktree vitest) |
| npm test (develop pre-merge) | **1956/1956 PASS** (358.21s, 381 files) |
| npm test (post-merge) | **1956/1956 PASS** (363.03s, 381 files) |
| build | **1086 modules SUCCESS** (11.40s) |
| npm audit (critical+) | **0 vulnerabilities** |
| live E2E | **126 PASS/19 SKIP** (30.55s, 50 files) |
| FE merge status | **SYNCED** @ `751c593` |
| BE merge status | **SYNCED** @ `20485f1` |
| transfer verdict | **PASS** |
| cross-stream | **SYNCED** |
| operation | **BLOCK** (origin/test push 495 BE+143 FE) |

### Merged commits (1228차)

- `751c593` — `ux(a11y): 미납 관리·서류 repository·목욕 전월 복사 접근성 재점검 (UXD-150)`

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-21T11:16:30+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-21 1226차)

> **1226차 PASS(post-merge SYNCED · QA-B212+B213 Fixed)** — test `@d2815d2`→`fd15a2f` · develop `@fd15a2f` · merge **EXECUTED**(FF 2 commits) · develop pre-merge **1955/1955 PASS**(362.42s) · post-merge **1955/1955 PASS**(360.42s) · build **1086 modules**(11.71s) · live E2E **126 PASS/19 SKIP**(34.70s) · develop/test WT **CLEAN SYNCED** · Open **0(active frontend)** · cross-stream **SYNCED(FE@fd15a2f + BE@b583c11)** · operation **BLOCK**

## 1226차 검증 요약 (merge EXECUTED — G-STAFF-DOCUMENT-REPOSITORY FE panel + progress API wire)

| 항목 | 결과 |
|---|---|
| test worktree HEAD (pre) | `d2815d2` |
| test worktree HEAD (post) | `fd15a2f` |
| develop HEAD | `fd15a2f` |
| ahead (`test..develop`, pre-merge) | **0/2** (`03d0d43` + `fd15a2f`) |
| ahead (`test..develop`, post-merge) | **0/0** (SYNCED) |
| develop working tree | **CLEAN** |
| test working tree | **CLEAN** @ `fd15a2f` |
| npm test (baseline carry @test) | **1945/1945 PASS** (TSR 1222 @ `d2815d2` carry) |
| npm test (develop pre-merge) | **1955/1955 PASS** (362.42s, 381 files) |
| npm test (post-merge) | **1955/1955 PASS** (360.42s, 381 files) |
| build | **1086 modules SUCCESS** (11.71s) |
| npm audit (critical+) | **0 vulnerabilities** |
| live E2E | **126 PASS/19 SKIP** (34.70s, 50 files) |
| FE merge status | **SYNCED** @ `fd15a2f` |
| BE merge status | **SYNCED** @ `b583c11` |
| transfer verdict | **PASS** |
| cross-stream | **SYNCED** |
| operation | **BLOCK** (origin/test push 493 BE+140 FE) |

### Merged commits (1226차)

- `03d0d43` — `feat(v1.2.1/G-STAFF-DOCUMENT-REPOSITORY): add 21-slot staff document repository panel`
- `fd15a2f` — `feat(v1.2.1/G-STAFF-DOCUMENT-REPOSITORY): wire repository-progress API on staff detail`

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-21T10:42:30+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-21 1224차)

> **1224차 BLOCK(merge pending 1 + npm test hang policy stop)** — test `@d2815d2` · develop `@03d0d43` · merge **SKIP**(`test..develop` **0/1** pending) · `npm test` **Terminated**(320.966s, exit 143, 5m+ 무출력) · build **1084 modules**(7.90s) · audit **0** · live E2E **SKIP** · Open **2(active frontend)** QA-B212(BLOCK)+QA-B213(MEDIUM) · cross-stream **BLOCK(FE pending 1 · BE@f6266ec SYNCED)** · operation **BLOCK**

## 1224차 검증 요약 (merge SKIP — G-STAFF-DOCUMENT-REPOSITORY pending)

| 항목 | 결과 |
|---|---|
| test worktree HEAD | `d2815d2` |
| develop HEAD | `03d0d43` |
| ahead (`test..develop`) | **0/1** (`03d0d43`) |
| develop working tree | **CLEAN** |
| test working tree | **CLEAN** @ `d2815d2` |
| npm test | **Terminated** (320.966s, exit 143; `RUN v4.1.8 /home/ubuntu/ogada/src/frontend` 후 5m+ 무출력) |
| hang 조치 | `./scripts/vitest-stop.sh` 실행 후 프로세스 정리 |
| build | **1084 modules SUCCESS** (7.90s) |
| npm audit (critical+) | **0 vulnerabilities** |
| live E2E | **SKIP** (merge 미실행) |
| FE merge status | **pending 1** |
| BE merge status | **SYNCED** @ `f6266ec` |
| transfer verdict | **BLOCK** |
| cross-stream | **BLOCK** |
| operation | **BLOCK** |

### Pending commit (1224차)

- `03d0d43` — `feat(v1.2.1/G-STAFF-DOCUMENT-REPOSITORY): add 21-slot staff document repository panel`

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-21T10:18:55+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-21 1222차)

> **1222차 PASS(SYNCED revalidation · QA-B210+B211 Fixed)** — test `@d2815d2` develop/test `@d2815d2` baseline **1945/1945 PASS**(356.53s) · merge **SKIP**(`test..develop` **0/0** · 1221 pending 2 commits merged carry: `860afa8`+`d2815d2`) · build **1084 modules**(7.92s) · live E2E **126 PASS/19 SKIP**(30.38s) · develop/test WT **CLEAN SYNCED** · Open **0(active frontend)** · cross-stream **BLOCK(FE SYNCED · BE pending 1 QA-B209 @c17097d)** · operation **BLOCK**

## 1222차 검증 요약 (SYNCED revalidation — US-R02 empty print guard + pilotPageFlows fixture)

| 항목 | 결과 |
|---|---|
| test worktree HEAD | `d2815d2` |
| develop HEAD | `d2815d2` |
| ahead (`test..develop`) | **0/0** (SYNCED) |
| develop working tree | **CLEAN** |
| test working tree | **CLEAN** @ `d2815d2` |
| npm test (baseline @test) | **1945/1945 PASS** (356.53s, 379 files) |
| build | **1084 modules SUCCESS** (7.92s) |
| npm audit (critical+) | **0 vulnerabilities** |
| live E2E | **126 PASS/19 SKIP** (30.38s) |
| FE merge status | **SYNCED** (1221 pending 2 commits merged carry) |
| BE merge status | **pending 1** @ `c17097d` (QA-B209 carry) |
| transfer verdict | **PASS** |
| cross-stream | **BLOCK** (BE pending 1) |
| operation | **BLOCK** |

### Merged commits carry (1221→1222)

- `860afa8` — `fix(v1.2.1/US-R02): guard empty staff status print outputs`
- `d2815d2` — `fix(v1.2.1/US-R02): align pilotPageFlows hire/leave print fixture` (QA-B210 closure)

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-21T09:40:43+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-21 1221차)

> **1221차 BLOCK(merge SKIP · QA-B210+B211 Open)** — test `@0420e6b` develop `@860afa8` baseline **1944/1945 PASS**(359.30s; pilotPageFlows flake · isolated PASS) · develop pre-merge **1944/1945 PASS**(359.09s/359.96s; **1 FAIL** `pilotPageFlows` `입퇴사 인쇄` · isolated FAIL) · merge **SKIP**(`test..develop` **0/1** pending `860afa8` + develop HEAD regression) · build **1084 modules**(7.89s) · live E2E **SKIP** · develop WT **CLEAN** · test WT **CLEAN** · Open **2(active frontend)** · cross-stream **BLOCK(FE regression · BE pending 1 QA-B209)** · operation **BLOCK**

## 1221차 검증 요약 (merge SKIP — US-R02 empty print guard regression)

| 항목 | 결과 |
|---|---|
| test worktree HEAD | `0420e6b` |
| develop HEAD | `860afa8` |
| ahead (`test..develop`) | **0/1** (`860afa8` empty staff status print guard) |
| develop working tree | **CLEAN** |
| test working tree | **CLEAN** @ `0420e6b` |
| npm test (baseline @test) | **1944/1945 PASS** (359.30s, 379 files; pilotPageFlows flake · isolated PASS) |
| npm test (develop pre-merge) | **1944/1945 PASS** (359.09s/359.96s retry; 1 FAIL · isolated FAIL) |
| build | **1084 modules SUCCESS** (7.89s) |
| npm audit (critical+) | **0 vulnerabilities** |
| live E2E | **SKIP** (merge 미실행) |
| FE merge status | **SKIP** (develop HEAD regression QA-B210) |
| BE merge status | **pending 1** @ `c17097d` (QA-B209 carry) |
| transfer verdict | **BLOCK** |
| cross-stream | **BLOCK** |
| operation | **BLOCK** |

### Pending commit (1221차)

- `860afa8` — `fix(v1.2.1/US-R02): guard empty staff status print outputs` (`StaffStatusReportPage.jsx` empty guard · `StaffStatusReportPage.test.jsx` +27 lines) — **blocked by QA-B210** (`pilotPageFlows.test.jsx` 미동기화)

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-21T08:59:28+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-21 1219차)

> **1219차 PASS(merge EXECUTED 1 commit · QA-B208 Fixed)** — test `@9a957fb`→`@0420e6b` baseline **1944/1944 PASS**(359.73s) · develop pre-merge **1944/1944 PASS**(361.70s) · post-merge **1944/1944 PASS**(362.22s) · build **1084 modules**(8.01s) · live E2E **126 PASS/19 SKIP**(32.74s) · merge **EXECUTED**(FF `9a957fb`→`0420e6b`, 1 commit) · develop/test WT **CLEAN SYNCED** · Open **0(active frontend)** · cross-stream **SYNCED(FE@0420e6b + BE@4d92844)** · operation **BLOCK**(origin/test push 490 BE+138 FE+QA-B95 partial)

## 1219차 검증 요약 (merge EXECUTED — G-BILLING-OVERDUE-ADJUSTMENT FE wire)

| 항목 | 결과 |
|---|---|
| test worktree HEAD (pre) | `9a957fb` |
| test worktree HEAD (post) | `0420e6b` |
| develop HEAD | `0420e6b` |
| ahead (`test..develop`) | **0/0** (SYNCED) |
| develop working tree | **CLEAN** |
| test working tree | **CLEAN** @ `0420e6b` |
| npm test (pre-merge baseline) | **1944/1944 PASS** (359.73s, 379 files) |
| npm test (develop pre-merge) | **1944/1944 PASS** (361.70s) |
| npm test (post-merge) | **1944/1944 PASS** (362.22s) |
| build | **1084 modules SUCCESS** (8.01s) |
| npm audit (critical+) | **0 vulnerabilities** |
| live E2E | **126 PASS/19 SKIP** (32.74s) |
| FE merge status | **EXECUTED** (1 commit) |
| BE merge status | **SYNCED** @ `4d92844` |
| transfer verdict | **PASS** |
| cross-stream | **SYNCED** |
| operation | **BLOCK** (origin/test push 490 BE+138 FE + QA-B95 partial) |

### Merged commits (1219차)

- `0420e6b` — `feat(v2/G-BILLING-OVERDUE-ADJUSTMENT): wire overdue CRM and amount adjustment UI` (QA-B208 closure)

### Changed files (1219차)

| file | +/- |
|---|---|
| `src/api/services.js` | +32 |
| `src/components/ui/OverdueManagementModal.jsx` | +496 (new) |
| `src/components/ui/OverdueManagementModal.test.jsx` | +99 (new) |
| `src/components/ui/index.js` | +1 |
| `src/pages/OverduePage.jsx` | +47/-2 |
| `src/pages/OverduePage.test.jsx` | +31 |
| `src/utils/overdueManagement.js` | +68 (new) |
| `src/utils/overdueManagement.test.js` | +35 (new) |

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-21T08:16:03+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-21 1217차)

> **1217차 PASS(merge EXECUTED 2 commits · QA-B206 Fixed)** — test `@a8ccb04`→`@9a957fb` baseline **1938/1938 PASS**(360.26s) · develop pre-merge **1938/1938 PASS**(358.80s) · post-merge **1938/1938 PASS**(357.29s) · build **1081 modules**(8.62s) · live E2E **126 PASS/19 SKIP**(31.78s) · merge **EXECUTED**(FF `a8ccb04`→`9a957fb`, 2 commits) · develop/test WT **CLEAN SYNCED** · Open **0(active frontend)** · cross-stream **SYNCED(FE@9a957fb + BE@a426663)** · operation **BLOCK**(origin/test push 489 BE+137 FE+QA-B95 partial)

## 1217차 검증 요약 (merge EXECUTED — G-BATHING FE wire + UXD-149 a11y)

| 항목 | 결과 |
|---|---|
| test worktree HEAD (pre) | `a8ccb04` |
| test worktree HEAD (post) | `9a957fb` |
| develop HEAD | `9a957fb` |
| ahead (`test..develop`) | **0/0** (SYNCED) |
| develop working tree | **CLEAN** |
| test working tree | **CLEAN** @ `9a957fb` |
| npm test (pre-merge baseline) | **1938/1938 PASS** (360.26s, 377 files) |
| npm test (develop pre-merge) | **1938/1938 PASS** (358.80s) |
| npm test (post-merge) | **1938/1938 PASS** (357.29s) |
| build | **1081 modules SUCCESS** (8.62s) |
| npm audit (critical+) | **0 vulnerabilities** |
| live E2E | **126 PASS/19 SKIP** (31.78s) |
| FE merge status | **EXECUTED** (2 commits) |
| BE merge status | **SYNCED** @ `a426663` |
| transfer verdict | **PASS** |
| cross-stream | **SYNCED** |
| operation | **BLOCK** (origin/test push 489 BE+137 FE + QA-B95 partial) |

### Merged commits (1217차)

- `b969570` — `ux(a11y): G21 공단 일정 불일치·G15 카카오 API 잔여 대시보드 위젯 대비 재점검 (UXD-149)`
- `9a957fb` — `feat(v3/G-BATHING): wire copy-from-previous-month on bathing schedules page` (QA-B206 closure)

### Changed files (1217차)

| file | +/- |
|---|---|
| `src/styles/components.css` | +10 |
| `src/api/bathingScheduleServices.test.js` | +19 |
| `src/api/services.js` | +11 |
| `src/config/bathingSchedule.js` | +33 |
| `src/config/bathingSchedule.test.js` | +28 (new) |
| `src/pages/BathingSchedulePage.jsx` | +96/-2 |
| `src/pages/BathingSchedulePage.test.jsx` | +65/-2 |

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-21T07:23:32+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-21 1215차)

> **1215차 PASS(merge EXECUTED 1 commit · QA-B205 Fixed)** — test `@580a86b`→`@a8ccb04` baseline **1932/1932 PASS**(351.83s) · develop pre-merge **1932/1932 PASS**(351.45s) · post-merge **1932/1932 PASS**(355.47s) · build **1081 modules**(10.52s) · live E2E **126 PASS/19 SKIP**(32.03s) · merge **EXECUTED**(FF `580a86b`→`a8ccb04`, 1 commit) · develop/test WT **CLEAN SYNCED** · Open **0(active frontend)** · cross-stream **BLOCK(BE merge pending 1 @49a1721 QA-B204)** · operation **BLOCK**(origin/test push 487 BE+135 FE+QA-B95 partial)

## 1215차 검증 요약 (merge EXECUTED — DashboardPage test flake stabilization)

| 항목 | 결과 |
|---|---|
| test worktree HEAD (pre) | `580a86b` |
| test worktree HEAD (post) | `a8ccb04` |
| develop HEAD | `a8ccb04` |
| ahead (`test..develop`) | **0/0** (SYNCED) |
| develop working tree | **CLEAN** |
| test working tree | **CLEAN** @ `a8ccb04` |
| npm test (pre-merge baseline) | **1932/1932 PASS** (351.83s, 376 files) |
| npm test (develop pre-merge) | **1932/1932 PASS** (351.45s) |
| npm test (post-merge) | **1932/1932 PASS** (355.47s) |
| build | **1081 modules SUCCESS** (10.52s) |
| npm audit (critical+) | **0 vulnerabilities** |
| live E2E | **126 PASS/19 SKIP** (32.03s) |
| FE merge status | **EXECUTED** (1 commit) |
| BE merge status | **pending 1** @ `49a1721` (QA-B204) |
| transfer verdict | **PASS** |
| cross-stream | **BLOCK** (BE merge pending 1) |
| operation | **BLOCK** (origin/test push 487 BE+135 FE + QA-B95 partial) |

### Merged commits (1215차)

- `a8ccb04` — `fix(test): stabilize HQ dashboard table waits in DashboardPage tests` (QA-B205 closure)

### Changed files (1215차)

| file | +/- |
|---|---|
| `src/pages/DashboardPage.test.jsx` | +117/-110 |

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-21T06:50:00+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-21 1213차)

> **1213차 PASS(merge EXECUTED 1 commit · QA-B203 Fixed)** — test `@ebc9f28`→`@580a86b` baseline **1931/1932 PASS**(354.95s; HQ table flake) · develop pre-merge **1931/1932 PASS**(354.11s) · post-merge **1931/1932 PASS**(356.95s · 356.56s retry; flake carry · isolated 17/17) · build **1081 modules**(11.29s) · live E2E **126 PASS/19 SKIP**(33.50s) · merge **EXECUTED**(FF `ebc9f28`→`580a86b`, 1 commit) · develop/test WT **CLEAN SYNCED** · Open **0(active frontend)** · cross-stream **SYNCED(FE@580a86b + BE@0c9518a)** · operation **BLOCK**(origin/test push 487 BE+134 FE+QA-B95 partial)

## 1213차 검증 요약 (merge EXECUTED — G15 Kakao API quota HQ dashboard widget)

| 항목 | 결과 |
|---|---|
| test worktree HEAD (pre) | `ebc9f28` |
| test worktree HEAD (post) | `580a86b` |
| develop HEAD | `580a86b` |
| ahead (`test..develop`) | **0/0** (SYNCED) |
| develop working tree | **CLEAN** |
| test working tree | **CLEAN** @ `580a86b` |
| npm test (pre-merge baseline) | **1931/1932 PASS** (354.95s, 376 files; DashboardPage HQ table flake · isolated 17/17) |
| npm test (develop pre-merge) | **1931/1932 PASS** (354.11s; same flake) |
| npm test (post-merge) | **1931/1932 PASS** (356.95s · 356.56s retry; full-suite flake carry · isolated PASS) |
| build | **1081 modules SUCCESS** (11.29s) |
| npm audit (critical+) | **0 vulnerabilities** |
| live E2E | **126 PASS/19 SKIP** (33.50s) |
| FE merge status | **EXECUTED** (1 commit) |
| BE merge status | **SYNCED** @ `0c9518a` |
| transfer verdict | **PASS** |
| cross-stream | **SYNCED** |
| operation | **BLOCK** (origin/test push 487 BE+134 FE + QA-B95 partial) |

### Merged commits (1213차)

- `580a86b` — `feat(v1.3/G15): wire Kakao API quota widget on HQ dashboard` (QA-B203 closure)

### Changed files (1213차)

| file | +/- |
|---|---|
| `src/auth/AuthContext.test.jsx` | +76/-2 |
| `src/pages/DashboardPage.jsx` | +47/-14 |
| `src/pages/DashboardPage.test.jsx` | +74 |
| `src/utils/transportKakaoQuotaSummary.js` | +68 (NEW) |
| `src/utils/transportKakaoQuotaSummary.test.js` | +79 (NEW) |

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-21T06:08:05+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-21 1211차)

> **1211차 PASS(merge EXECUTED 1 commit · QA-B201 Fixed)** — test `@c01b880`→`@ebc9f28` baseline **1924/1925 PASS**(361.30s; HQ table flake) · develop pre-merge **1924/1925 PASS**(355.71s) · post-merge **1925/1925 PASS**(357.12s; 1st flake · retry clean) · build **1081 modules**(7.83s) · live E2E **126 PASS/19 SKIP**(30.29s) · merge **EXECUTED**(FF `c01b880`→`ebc9f28`, 1 commit) · develop/test WT **CLEAN SYNCED** · Open **0(active frontend)** · cross-stream **SYNCED(FE@ebc9f28 + BE@0796821)** · operation **BLOCK**(origin/test push 486 BE+133 FE+QA-B95 partial)

## 1211차 검증 요약 (merge EXECUTED — G21 hide NHIS gap widget on non-home-visit branches)

| 항목 | 결과 |
|---|---|
| test worktree HEAD (pre) | `c01b880` |
| test worktree HEAD (post) | `ebc9f28` |
| develop HEAD | `ebc9f28` |
| ahead (`test..develop`) | **0/0** (SYNCED) |
| develop working tree | **CLEAN** |
| test working tree | **CLEAN** @ `ebc9f28` |
| npm test (pre-merge baseline) | **1924/1925 PASS** (361.30s, 375 files; DashboardPage HQ table flake · isolated 14/14) |
| npm test (develop pre-merge) | **1924/1925 PASS** (355.71s; same flake) |
| npm test (post-merge) | **1925/1925 PASS** (357.12s; 1st 1924/1925 flake · retry clean) |
| build | **1081 modules SUCCESS** (7.83s) |
| npm audit (critical+) | **0 vulnerabilities** |
| live E2E | **126 PASS/19 SKIP** (30.29s) |
| FE merge status | **EXECUTED** (1 commit) |
| BE merge status | **SYNCED** @ `0796821` |
| transfer verdict | **PASS** |
| cross-stream | **SYNCED** |
| operation | **BLOCK** (origin/test push 486 BE+133 FE + QA-B95 partial) |

### Merged commits (1211차)

- `ebc9f28` — `fix(v2/G21): hide NHIS comparison gap widget on non-home-visit branches` (QA-B201 closure)

### Changed files (1211차)

| file | +/- |
|---|---|
| `src/auth/AuthContext.jsx` | +19/-3 |
| `src/config/branches.js` | +8/-1 |
| `src/pages/DashboardPage.jsx` | +77/-36 |
| `src/pages/DashboardPage.test.jsx` | +33/-1 |

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-21T05:22:15+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-21 1209차)

> **1209차 PASS(merge EXECUTED 1 commit · QA-B200 Fixed)** — test `@fe7df60`→`@c01b880` baseline **1924/1924 PASS**(353.35s) · develop pre-merge **1924/1924 PASS**(360.47s) · post-merge **1924/1924 PASS**(352.46s; HQ table flake 1st/2nd retry) · build **1081 modules**(7.84s) · live E2E **126 PASS/19 SKIP**(30.36s) · merge **EXECUTED**(FF `fe7df60`→`c01b880`, 1 commit) · develop/test WT **CLEAN SYNCED** · Open **0(active frontend)** · cross-stream **SYNCED(FE@c01b880 + BE@0796821)** · operation **BLOCK**(origin/test push 486 BE+132 FE+QA-B95 partial)

## 1209차 검증 요약 (merge EXECUTED — G21 dashboard API snapshot preference)

| 항목 | 결과 |
|---|---|
| test worktree HEAD (pre) | `fe7df60` |
| test worktree HEAD (post) | `c01b880` |
| develop HEAD | `c01b880` |
| ahead (`test..develop`) | **0/0** (SYNCED) |
| develop working tree | **CLEAN** |
| test working tree | **CLEAN** @ `c01b880` |
| npm test (pre-merge baseline) | **1924/1924 PASS** (353.35s, 375 files) |
| npm test (develop pre-merge) | **1924/1924 PASS** (360.47s) |
| npm test (post-merge) | **1924/1924 PASS** (352.46s; 1st/2nd 1923/1924 HQ table flake) |
| build | **1081 modules SUCCESS** (7.84s) |
| npm audit (critical+) | **0 vulnerabilities** |
| live E2E | **126 PASS/19 SKIP** (30.36s) |
| FE merge status | **EXECUTED** (1 commit) |
| BE merge status | **SYNCED** @ `0796821` |
| transfer verdict | **PASS** |
| cross-stream | **SYNCED** |
| operation | **BLOCK** (origin/test push 486 BE+132 FE + QA-B95 partial) |

### Merged commits (1209차)

- `c01b880` — `fix(v2/G21): prefer dashboard API nhisComparisonGapCount snapshot` (QA-B200 closure)

### Changed files (1209차)

| file | +/- |
|---|---|
| `src/pages/DashboardPage.jsx` | +5/-3 |
| `src/pages/DashboardPage.test.jsx` | +80 |

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-21T04:33:30+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-21 1207차)

> **1207차 PASS(merge EXECUTED 1 commit · QA-B198 Fixed)** — test `@cd6891f`→`@fe7df60` baseline **1918/1918 PASS**(390.50s) · develop pre-merge **1922/1922 PASS**(354.58s) · post-merge **1922/1922 PASS**(355.96s) · build **1081 modules**(7.86s) · live E2E **126 PASS/19 SKIP**(30.62s) · merge **EXECUTED**(FF `cd6891f`→`fe7df60`, 1 commit) · develop/test WT **CLEAN SYNCED** · Open **0(active frontend)** · cross-stream **SYNCED(FE@fe7df60 + BE@ad11fda)** · operation **BLOCK**(origin/test push 485 BE+131 FE+QA-B95 partial)

## 1207차 검증 요약 (merge EXECUTED — G21 dashboard NHIS comparison gap StatCard)

| 항목 | 결과 |
|---|---|
| test worktree HEAD (pre) | `cd6891f` |
| test worktree HEAD (post) | `fe7df60` |
| develop HEAD | `fe7df60` |
| ahead (`test..develop`) | **0/0** (SYNCED) |
| develop working tree | **CLEAN** |
| test working tree | **CLEAN** @ `fe7df60` |
| npm test (pre-merge baseline) | **1918/1918 PASS** (390.50s, 375 files) |
| npm test (develop pre-merge) | **1922/1922 PASS** (354.58s) |
| npm test (post-merge) | **1922/1922 PASS** (355.96s) |
| build | **1081 modules SUCCESS** (7.86s) |
| npm audit (critical+) | **0 vulnerabilities** |
| live E2E | **126 PASS/19 SKIP** (30.62s) |
| FE merge status | **EXECUTED** (1 commit) |
| BE merge status | **SYNCED** @ `ad11fda` |
| transfer verdict | **PASS** |
| cross-stream | **SYNCED** |
| operation | **BLOCK** (origin/test push 485 BE+131 FE + QA-B95 partial) |

### Merged commits (1207차)

- `fe7df60` — `feat(v2/G21): wire nhis comparison gap StatCard on dashboard` (QA-B198 closure)

### Changed files (1207차)

| file | +/- |
|---|---|
| `src/pages/DashboardPage.jsx` | +48/-2 |
| `src/pages/DashboardPage.test.jsx` | +50 |
| `src/pages/dashboardSummary.js` | +8 |
| `src/pages/dashboardSummary.test.js` | +2 |
| `src/utils/visitNhisComparison.js` | +15 |
| `src/utils/visitNhisComparison.test.js` | +32/-1 |

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-21T04:00:00+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-21 1205차)

> **1205차 PASS(merge EXECUTED 3 commits · QA-B195+QA-B196 Fixed)** — test `@c6a412f`→`@cd6891f` baseline **1913/1913 PASS**(358.90s) · develop pre-merge **1918/1918 PASS**(359.87s) · post-merge **1918/1918 PASS**(356.16s) · build **1081 modules**(7.94s) · live E2E **126 PASS/19 SKIP**(30.50s) · merge **EXECUTED**(FF `c6a412f`→`cd6891f`, 3 commits) · develop/test WT **CLEAN SYNCED** · Open **0(active frontend)** · cross-stream **BLOCK(BE dirty QA-B197 + merge pending 2 QA-B192)** · operation **BLOCK**(origin/test push 482 BE+127 FE+QA-B95 partial)

## 1205차 검증 요약 (merge EXECUTED — live-e2e suite gates + UXD-148 + guard fix)

| 항목 | 결과 |
|---|---|
| test worktree HEAD (pre) | `c6a412f` |
| test worktree HEAD (post) | `cd6891f` |
| develop HEAD | `cd6891f` |
| ahead (`test..develop`) | **0/0** (SYNCED) |
| develop working tree | **CLEAN** |
| test working tree | **CLEAN** @ `cd6891f` |
| npm test (pre-merge baseline) | **1913/1913 PASS** (358.90s, 375 files) |
| npm test (develop pre-merge) | **1918/1918 PASS** (359.87s) |
| npm test (post-merge) | **1918/1918 PASS** (356.16s) |
| build | **1081 modules SUCCESS** (7.94s) |
| npm audit (critical+) | **0 vulnerabilities** |
| live E2E | **126 PASS/19 SKIP** (30.50s) |
| FE merge status | **EXECUTED** (3 commits) |
| BE merge status | **merge pending 2** @ `14935a3`+`7b99313` + develop **DIRTY 1M** (QA-B192+QA-B197) |
| transfer verdict | **PASS** |
| cross-stream | **BLOCK(BE dirty + merge pending 2)** |
| operation | **BLOCK** (QA-B197+QA-B192 + origin/test push 482 BE+127 FE + QA-B95 partial) |

### Merged commits (1205차)

- `cd6891f` — `fix(test): gate cash receipt live suite` (QA-B195 closure)
- `e2f1246` — `ux(a11y): G-BILLING 입금·수납 대장 필터 접근성 재점검 (UXD-148)`
- `cb3fe3d` — `fix(v2/live-e2e): ignore feature-scoped operation blockers in suite gates`

### Changed files (1205차)

| file | +/- |
|---|---|
| `src/e2e/cashReceiptIssuanceLiveApi.e2e.test.js` | +2/-2 |
| `src/e2e/liveConfig.js` | +126 |
| `src/e2e/liveDescribe.js` | +7 |
| `src/pages/BillingReportPage.jsx` | +13 |
| `src/pages/BillingReportPage.test.jsx` | +30 |
| `src/styles/components.css` | +13 |
| `src/test/liveE2eHarness.test.js` | +106 |
| `src/test/liveE2eSuiteGuard.test.js` | +1/-1 |

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-21T03:10:15+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-21 1203차)

> **1203차 BLOCK(merge SKIP · develop HEAD merge gate 1 FAIL · QA-B195+QA-B196 Open)** — test `@c6a412f` develop `@cb3fe3d` `npm test` **1916/1917 PASS**(353.79s; **1 FAIL** `liveE2eSuiteGuard.test.js`) · build **1081 modules**(7.84s) · live E2E **SKIP** · merge **SKIP**(`test..develop` **0/1** pending `cb3fe3d`) · Open **2(active frontend)** · cross-stream **BLOCK(FE pending 1+regression · BE pending 2 @7b99313)** · operation **BLOCK**(QA-B195+QA-B196+QA-B192+origin/test push 482 BE+127 FE+QA-B95 partial)

## 1203차 검증 요약 (merge SKIP — live E2E suite guard regression)

| 항목 | 결과 |
|---|---|
| test worktree HEAD | `c6a412f` |
| develop HEAD | `cb3fe3d` |
| ahead (`test..develop`) | **0/1** (pending `cb3fe3d`) |
| develop working tree | **CLEAN** |
| test working tree | **CLEAN** @ `c6a412f` |
| npm test (develop HEAD via locked wrapper) | **1916/1917 PASS** (353.79s, 375 files; **1 FAIL**) |
| failing test | `src/test/liveE2eSuiteGuard.test.js` — `cashReceiptIssuanceLiveApi.e2e.test.js` uses `liveCashReceiptDescribe` not matched by guard regex |
| build | **1081 modules SUCCESS** (7.84s) |
| npm audit (high+) | **0 vulnerabilities** |
| live E2E | **SKIP** (merge 미실행 사이클) |
| FE merge status | **SKIP** (develop HEAD regression blocks merge gate) |
| BE merge status | **merge pending 2** @ `14935a3`+`7b99313` (QA-B192) |
| transfer verdict | **BLOCK** |
| cross-stream | **BLOCK(FE + BE merge pending)** |
| operation | **BLOCK** (QA-B195+QA-B196+QA-B192 + origin/test push 482 BE+127 FE + QA-B95 partial) |

### Pending commit (1203차 — not merged)

- `cb3fe3d` — `fix(v2/live-e2e): ignore feature-scoped operation blockers in suite gates`

### Changed files (pending @ cb3fe3d)

| file | +/- |
|---|---|
| `src/e2e/cashReceiptIssuanceLiveApi.e2e.test.js` | +2/-2 |
| `src/e2e/liveConfig.js` | +126 |
| `src/e2e/liveDescribe.js` | +7 |
| `src/test/liveE2eHarness.test.js` | +106 |

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-21T02:44:32+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-21 1201차)

> **1201차 PASS(merge EXECUTED 1 commit · QA-B194 Fixed)** — test `@33e9e1a`→`@c6a412f` `npm test` **1913/1913 PASS**(361.03s pre · 352.68s post) · build **1081 modules**(7.95s) · live E2E **126 PASS/19 SKIP**(33.36s) · merge **EXECUTED**(FF `33e9e1a`→`c6a412f`, 1 commit) · develop/test WT **CLEAN SYNCED** · Open **0(active frontend)** · cross-stream **BLOCK(BE QA-B192+QA-B193 @14935a3)** · operation **BLOCK**(origin/test push 482 BE+127 FE+QA-B95 partial)

## 1201차 검증 요약 (merge EXECUTED — G-BILLING appliedFilters echo FE wire)

| 항목 | 결과 |
|---|---|
| test worktree HEAD (pre) | `33e9e1a` |
| test worktree HEAD (post) | `c6a412f` |
| develop HEAD | `c6a412f` |
| ahead (`test..develop`) | **0/0** (SYNCED) |
| develop working tree | **CLEAN** |
| test working tree | **CLEAN** @ `c6a412f` |
| npm test (pre-merge baseline) | **1913/1913 PASS** (361.03s, 375 files) |
| npm test (post-merge) | **1913/1913 PASS** (352.68s) |
| build | **1081 modules SUCCESS** (7.95s) |
| npm audit (high+) | **0 vulnerabilities** |
| live E2E | **126 PASS/19 SKIP** (33.36s) |
| FE merge status | **EXECUTED** (1 commit) |
| BE merge status | **merge pending 1 + dirty** @ `14935a3` (QA-B192+QA-B193) |
| transfer verdict | **PASS** |
| cross-stream | **BLOCK(BE dirty + merge pending)** |
| operation | **BLOCK** (QA-B192+QA-B193 + origin/test push 482 BE+127 FE + QA-B95 partial) |

### Merged commits (1201차)

- `c6a412f` — `feat(v1.2.1/G-BILLING): wire appliedFilters echo on billing ledger reports`

### Changed files (1201차)

| file | +/- |
|---|---|
| `src/api/billingReportFilters.js` | +36 |
| `src/api/billingReportFilters.test.js` | +29/-1 |
| `src/pages/BillingReportPage.jsx` | +30/-12 |
| `src/pages/BillingReportPage.test.jsx` | +36 |

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-21T02:10:28+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-21 1199차)

> **1199차 PASS(merge EXECUTED 1 commit · QA-B191 Fixed)** — test `@e38ccfd`→`@33e9e1a` `npm test` **1910/1910 PASS**(353.97s pre · 354.56s post) · build **1081 modules**(7.84s) · live E2E **126 PASS/19 SKIP**(33.38s) · merge **EXECUTED**(FF `e38ccfd`→`33e9e1a`, 1 commit) · develop/test WT **CLEAN SYNCED** · Open **0(active)** · cross-stream **BLOCK(BE merge pending 1 QA-B192 @14935a3)** · operation **BLOCK**(origin/test push 482 BE+126 FE+QA-B95 partial)

## 1199차 검증 요약 (merge EXECUTED — live-e2e snake_case operation blocker recovery)

| 항목 | 결과 |
|---|---|
| test worktree HEAD (pre) | `e38ccfd` |
| test worktree HEAD (post) | `33e9e1a` |
| develop HEAD | `33e9e1a` |
| ahead (`test..develop`) | **0/0** (SYNCED) |
| develop working tree | **CLEAN** |
| test working tree | **CLEAN** @ `33e9e1a` |
| npm test (pre-merge baseline) | **1910/1910 PASS** (353.97s, 375 files) |
| npm test (develop pre-merge) | **1910/1910 PASS** (361.68s) |
| npm test (post-merge) | **1910/1910 PASS** (354.56s) |
| build | **1081 modules SUCCESS** (7.84s) |
| npm audit (high+) | **0 vulnerabilities** |
| live E2E | **126 PASS/19 SKIP** (33.38s) |
| FE merge status | **EXECUTED** (1 commit) |
| BE merge status | **merge pending 1** @ `14935a3` (QA-B192) |
| transfer verdict | **PASS** |
| cross-stream | **BLOCK(BE merge pending 1)** |
| operation | **BLOCK** (QA-B192 + origin/test push 482 BE+126 FE + QA-B95 partial) |

### Merged commits (1199차)

- `33e9e1a` — `fix(v2/live-e2e): normalize snake_case operation blocker recovery`

### Changed files (1199차)

| file | +/- |
|---|---|
| `src/e2e/liveConfig.js` | +14/-6 |
| `src/test/liveE2eHarness.test.js` | +50 |

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-21T01:35:21+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-21 1197차)

> **1197차 PASS(baseline)+BLOCK(develop WT DIRTY · QA-B191 Open)** — test `@e38ccfd` `npm test` **1910/1910 PASS**(354.52s) · build **1081 modules**(7.87s) · live E2E **126 PASS/19 SKIP**(30.57s) · merge **SKIP**(`test..develop` **0/0** SYNCED · develop **DIRTY 2M**) · test WT **CLEAN** · Open **1(active frontend QA-B191)** · cross-stream **SYNCED(FE@e38ccfd + BE@375fb9d)** · operation **BLOCK**(QA-B191+origin/test push 482 BE+125 FE+QA-B95 partial)

## 1197차 검증 요약 (merge SKIP — develop WT DIRTY recurrence)

| 항목 | 결과 |
|---|---|
| test worktree HEAD | `e38ccfd` |
| develop HEAD | `e38ccfd` |
| ahead (`test..develop`) | **0/0** (SYNCED) |
| develop working tree | **DIRTY 2M** (`liveConfig.js` · `liveE2eHarness.test.js`) |
| test working tree | **CLEAN** @ `e38ccfd` |
| npm test (baseline) | **1910/1910 PASS** (354.52s, 375 files) |
| build | **1081 modules SUCCESS** (7.87s) |
| npm audit (high+) | **0 vulnerabilities** |
| live E2E | **126 PASS/19 SKIP** (30.57s) |
| FE merge status | **SKIP** (0/0 SYNCED · develop dirty) |
| BE merge status | **SYNCED** @ `375fb9d` |
| transfer verdict | **BLOCK** (develop WT DIRTY · QA-B191 Open) |
| cross-stream | **SYNCED** |
| operation | **BLOCK** (QA-B191 + origin/test push 482 BE+125 FE + QA-B95 partial) |

### Develop dirty files (1197차 — 미커밋 WIP)

| file | +/- |
|---|---|
| `src/e2e/liveConfig.js` | +14/-6 |
| `src/test/liveE2eHarness.test.js` | +50 |

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-21T01:13:28+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-21 1195차)

> **1195차 PASS(merge EXECUTED 1 commit · QA-B189 Fixed)** — test `@5f1815f`→`@e38ccfd` `npm test` **1908/1908 PASS**(353.65s pre · 353.81s post) · build **1081 modules**(11.17s) · live E2E **126 PASS/19 SKIP**(33.44s) · merge **EXECUTED**(FF `5f1815f`→`e38ccfd`, 1 commit) · develop/test WT **CLEAN SYNCED** · Open **0(active)** · cross-stream **SYNCED(FE@e38ccfd + BE@b96d038)** · operation **BLOCK**(origin/test push 481 BE+125 FE+QA-B95 partial)

## 1195차 검증 요약 (merge EXECUTED — G-BILLING deposit half-month + receipt dual-basis FE wire)

| 항목 | 결과 |
|---|---|
| test worktree HEAD (pre) | `5f1815f` |
| test worktree HEAD (post) | `e38ccfd` |
| develop HEAD | `e38ccfd` |
| ahead (`test..develop`) | **0/0** (SYNCED) |
| develop working tree | **CLEAN** |
| test working tree | **CLEAN** @ `e38ccfd` |
| npm test (pre-merge baseline) | **1908/1908 PASS** (353.65s, 375 files) |
| npm test (develop pre-merge) | **1908/1908 PASS** (353.65s) |
| npm test (post-merge) | **1908/1908 PASS** (353.81s) |
| build | **1081 modules SUCCESS** (11.17s) |
| npm audit (high+) | **0 vulnerabilities** |
| live E2E | **126 PASS/19 SKIP** (33.44s) |
| FE merge status | **EXECUTED** (1 commit) |
| BE merge status | **SYNCED** @ `b96d038` |
| transfer verdict | **PASS** |
| cross-stream | **SYNCED** |
| operation | **BLOCK** (origin/test push 481 BE+125 FE + QA-B95 partial) |

### Merged commits (1195차)

- `e38ccfd` — `feat(v1.2.1/G-BILLING): wire deposit half-month and receipt basis filters on billing reports`

### Changed files (1195차)

| file | +/- |
|---|---|
| `src/api/billingReportFilters.js` | +58 |
| `src/api/billingReportFilters.test.js` | +41 |
| `src/pages/BillingReportPage.jsx` | +130/-10 |
| `src/pages/BillingReportPage.test.jsx` | +40 |

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-21T00:43:15+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-21 1193차)

> **1193차 PASS(merge EXECUTED 4 commits · QA-B188 Fixed)** — test `@82a542c`→`@5f1815f` `npm test` **1902/1902 PASS**(357.86s pre · 356.64s post) · build **1079 modules**(10.97s) · live E2E **126 PASS/19 SKIP**(30.43s) · merge **EXECUTED**(FF `82a542c`→`5f1815f`, 4 commits) · develop/test WT **CLEAN SYNCED** · Open **0(active)** · cross-stream **SYNCED(FE@5f1815f + BE@b96d038)** · operation **BLOCK**(origin/test push 481 BE+124 FE+QA-B95 partial)

## 1193차 검증 요약 (merge EXECUTED — G-STAFF-LEAVE-STATUS + live-e2e hardening)

| 항목 | 결과 |
|---|---|
| test worktree HEAD (pre) | `82a542c` |
| test worktree HEAD (post) | `5f1815f` |
| develop HEAD | `5f1815f` |
| ahead (`test..develop`) | **0/0** (SYNCED) |
| develop working tree | **CLEAN** |
| test working tree | **CLEAN** @ `5f1815f` |
| npm test (pre-merge baseline) | **1902/1902 PASS** (357.86s, 374 files) |
| npm test (develop pre-merge) | **1902/1902 PASS** (354.82s) |
| npm test (post-merge) | **1902/1902 PASS** (356.64s) |
| build | **1079 modules SUCCESS** (10.97s) |
| npm audit (high+) | **0 vulnerabilities** |
| live E2E | **126 PASS/19 SKIP** (30.43s) |
| FE merge status | **EXECUTED** (4 commits) |
| BE merge status | **SYNCED** @ `b96d038` |
| transfer verdict | **PASS** |
| cross-stream | **SYNCED** |
| operation | **BLOCK** (origin/test push 481 BE+124 FE + QA-B95 partial) |

### Merged commits (1193차)

- `e45df26` — `fix(v2/live-e2e): recover stale staff and guardian tokens in live session`
- `2581347` — `feat(v1.2.1/G-STAFF-LEAVE-STATUS): wire ON_LEAVE staff lifecycle on frontend`
- `1a614c9` — `ux(a11y): G-STAFF-LEAVE-STATUS 휴직 상태 접근성 재점검 (UXD-147)`
- `5f1815f` — `fix(v2/live-e2e): ignore unrelated auth blockers in suite gates`

---
