<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-22T08:15:00+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-22 1268차)

> **1268차 PASS(SYNCED revalidation)** — test/develop `@8aabeae` · `test..develop` **0/0** · npm test **1984/1984 PASS**(670.15s carry, 387 files) · build **1139 modules PASS**(8.34s carry) · audit **0** · live E2E **126 PASS/19 SKIP**(34.72s carry) · Open **0** · transfer **PASS** · cross-stream **SYNCED(FE@8aabeae + BE@175d9cb)** · operation **BLOCK**(origin/test push 511 BE+161 FE+QA-B95)

## 1268차 검증 요약 (SYNCED revalidation)

| 항목 | 결과 |
|---|---|
| test/develop HEAD | `8aabeae` (SYNCED) |
| ahead (`test..develop`) | **0/0** |
| develop working tree | **CLEAN** |
| test working tree | **?? 9** (무해한 빈 파일 carry) |
| npm test (1268차 revalidation) | **1984/1984 PASS** @ `8aabeae` (670.15s carry, 387 files) |
| merge (1267차 carry) | EXECUTED FF `daaba4b`→`8aabeae` (2 commits) |
| build | **1139 modules SUCCESS** (8.34s carry) |
| npm audit (high+) | **0 vulnerabilities** |
| live E2E | **126 PASS / 19 SKIP** (34.72s carry) |
| transfer verdict | **PASS** |
| cross-stream | **SYNCED (FE@8aabeae + BE@175d9cb)** |
| operation | **BLOCK** (origin/test push 511 BE + 161 FE + QA-B95) |

### Merged commits (1267차 carry · `daaba4b`→`8aabeae`)

1. `250619e` — `fix(v1.2.1/US-E03): render branch QR image from signed qrToken` (`branchQrCode.js` + `qrcode` dep + 2 tests)
2. `8aabeae` — `chore(v1.2.1): ignore benchmark snapshots in frontend submodule` (`.gitignore`)

### 잔여 리스크

- **operation BLOCK**: `origin/test push 511 BE + 161 FE` 미실행 · `QA-B95` live E2E 19 SKIP carry

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-22T07:53:00+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-22 1267차)

> **1267차 PASS(merge EXECUTED)** — test/develop `@8aabeae` **SYNCED** · `test..develop` **0/0** · develop pre-merge **1984/1984 PASS** · post-merge **1984/1984 PASS** · build **1139 modules PASS** · audit **0** · live E2E **126 PASS/19 SKIP** · Open **0(active frontend)** · **★ QA-B238 Fixed @ `8aabeae`** · transfer **PASS** · cross-stream **SYNCED(FE@8aabeae + BE@175d9cb)** · operation **BLOCK**

## 1267차 검증 요약 (merge EXECUTED — 2 commits)

| 항목 | 결과 |
|---|---|
| test worktree HEAD | `8aabeae` |
| develop HEAD | `8aabeae` |
| ahead (`test..develop`) | **0/0** (SYNCED) |
| develop working tree | **CLEAN** |
| test working tree | **DIRTY** (`?? 9`, 무해한 빈 파일 carry) |
| baseline npm test | **1984/1984 PASS** @ `daaba4b` (672.99s carry, 1266차) |
| develop pre-merge npm test | **1984/1984 PASS** @ `8aabeae` (669.42s, 387 files) |
| post-merge npm test | **1984/1984 PASS** @ `8aabeae` (670.15s, 387 files) |
| build | **1139 modules SUCCESS** (8.34s) |
| npm audit (high+) | **0 vulnerabilities** |
| live E2E | **126 PASS / 19 SKIP** (34.72s) |
| transfer verdict | **PASS** |
| cross-stream | **SYNCED (FE@8aabeae + BE@175d9cb)** |
| operation | **BLOCK** (origin/test push 511 BE + 161 FE + QA-B95) |

### Merged commits (FF `daaba4b`→`8aabeae`)

1. `250619e` — `fix(v1.2.1/US-E03): render branch QR image from signed qrToken` (`branchQrCode.js` + `qrcode` dep)
2. `8aabeae` — `chore(v1.2.1): ignore benchmark snapshots in frontend submodule`

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-22T06:10:05+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-22 1264차)

> **1264차 BLOCK(merge SKIP)** — test `@daaba4b` 기준 회귀 `npm test` **1984/1984 PASS**(671.39s) · develop `@250619e` (`test..develop` **0/1**) · develop WT **DIRTY 2U**(`carefor_func.php`, `silverangel_essential.html`) · merge **SKIP** · build/audit/live E2E **SKIP** · **QA-20260622-B238 Open (BLOCK)** · transfer **BLOCK** · cross-stream **BLOCK(FE pending 1 + BE pending 1)** · operation **BLOCK**

## 1264차 검증 요약 (merge SKIP — pending 1)

| 항목 | 결과 |
|---|---|
| test worktree HEAD | `daaba4b` |
| develop HEAD | `250619e` |
| ahead (`test..develop`) | **0/1** |
| develop working tree | **DIRTY** (`?? carefor_func.php`, `?? silverangel_essential.html`) |
| test working tree | **DIRTY** (`?? 9`, 무해한 빈 파일 carry) |
| npm test (test worktree) | **1984/1984 PASS** @ `daaba4b` (671.39s, 387 files) |
| develop pre-merge npm test | **SKIP** (merge pending + develop WT DIRTY) |
| post-merge npm test | **SKIP** (merge not executed) |
| build / audit / live E2E | **SKIP** (merge not executed) |
| transfer verdict | **BLOCK** |
| open issue | **QA-20260622-B238 (BLOCK)** |
| cross-stream | **BLOCK (FE@250619e pending 1 + BE@dce9bf1 pending 1)** |
| operation | **BLOCK** (origin/test push 509 BE + 159 FE + QA-B95) |

### Planned blocker action

1. `src/frontend` develop WT를 **CLEAN**으로 정리(현재 untracked 2건 처리).
2. develop `@250619e` 기준 pre-merge 검증 완료 후 develop→test merge 재시도.
3. post-merge `npm test`/build/audit/live E2E 재검증으로 QA-B238 해소.

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-22T04:54:00+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-22 1261차)

> **1261차 PASS(merge EXECUTED)** — test/develop `@daaba4b` **SYNCED** · `test..develop` **0/0** · develop pre-merge **1979/1979 PASS** · post-merge **1979/1979 PASS** · build **1089 modules PASS** · audit **0** · live E2E **126 PASS/19 SKIP** · Open **0(active frontend)** · **★ QA-B233 Fixed @ `daaba4b`** · **★ QA-B234 Fixed @ `daaba4b`** · transfer **PASS** · cross-stream **SYNCED(FE@daaba4b + BE@99d03fa)** · operation **BLOCK**

## 1261차 검증 요약 (merge EXECUTED — 4 commits)

| 항목 | 결과 |
|---|---|
| test worktree HEAD | `daaba4b` |
| develop HEAD | `daaba4b` |
| ahead (`test..develop`) | **0/0** (SYNCED) |
| develop working tree | **CLEAN** |
| test working tree | **DIRTY** (`?? 9` 1개, 무해한 빈 파일 carry) |
| baseline npm test | **1970/1970 PASS** @ `dfa981c` (648s carry, 1259차) |
| develop pre-merge npm test | **1979/1979 PASS** @ `daaba4b` (671.08s, 386 files) |
| post-merge npm test | **1979/1979 PASS** @ `daaba4b` (671.66s) |
| build | **1089 modules SUCCESS** (8.07s) |
| npm audit (high+) | **0 vulnerabilities** |
| live E2E | **126 PASS / 19 SKIP** (35.23s) |
| transfer verdict | **PASS** |
| cross-stream | **SYNCED (FE@daaba4b + BE@99d03fa)** |
| operation | **BLOCK** (origin/test push 509 BE + 159 FE + QA-B95) |

### Merged commits (FF `dfa981c`→`daaba4b`)

1. `dffd726` — `fix(v1.2.1/US-E05): align attendance stats API and absence checkout wire`
2. `df7f308` — `ux(a11y): G-STAFF-WORK-ATTENDANCE·CmsDebitPanel·US-E05 접근성 재점검 (UXD-152)`
3. `77b1ea8` — `feat(v1.2.1/G-BILLING-REPORT-FILTER-PERSISTENCE): wire billing report filter persistence API`
4. `daaba4b` — `fix(v1.2.1/QA-B233): match DatePicker today suffix in test utils`

### Changed files (14 files, +732/-118)

- `src/api/attendanceServices.test.js` (new)
- `src/api/services.js`
- `src/components/ui/CmsDebitPanel.jsx`
- `src/pages/AttendancePage.test.jsx`
- `src/pages/AttendanceStatsPage.jsx`
- `src/pages/AttendanceStatsPage.test.jsx`
- `src/pages/BillingReportPage.jsx`
- `src/pages/BillingReportPage.test.jsx`
- `src/pages/StaffWorkAttendancePage.jsx`
- `src/pages/StaffWorkAttendancePage.test.jsx`
- `src/pages/pilotPageFlows.test.jsx`
- `src/test/pickerTestUtils.js`
- `src/utils/monthlyAttendanceStats.js` (new)
- `src/utils/monthlyAttendanceStats.test.js` (new)

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-22T05:12:00+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-22 1262차)

> **1262차 PASS(SYNCED revalidation)** — test/develop `@daaba4b` · `test..develop` **0/0** · npm test **1979/1979 PASS**(668.57s) · build **1089 modules PASS**(8.68s) · audit **0** · live E2E **126 PASS/19 SKIP**(34.56s) · Open **0** · transfer **PASS** · cross-stream **SYNCED(FE@daaba4b + BE@99d03fa)** · operation **BLOCK**(origin/test push 509 BE+159 FE)

## 1262차 검증 요약 (SYNCED revalidation)

| 항목 | 결과 |
|---|---|
| test/develop HEAD | `daaba4b` (SYNCED) |
| ahead (`test..develop`) | **0/0** |
| develop working tree | **CLEAN** |
| test working tree | **?? 9** (무해한 빈 파일 carry) |
| npm test (1262차 revalidation) | **1979/1979 PASS** @ `daaba4b` (668.57s, 386 files) |
| merge (1261차 carry) | EXECUTED FF `dfa981c`→`daaba4b` (4 commits) |
| build | **1089 modules SUCCESS** (8.68s) |
| npm audit (high+) | **0 vulnerabilities** |
| live E2E | **126 PASS / 19 SKIP** (34.56s) |
| transfer verdict | **PASS** |
| cross-stream | **SYNCED (FE@daaba4b + BE@99d03fa)** |
| operation | **BLOCK** (origin/test push 509 BE + 159 FE + QA-B95) |

### Vitest concurrency (1262차 관측)

`agent_pipeline` live-e2e vitest와 겹쳐 `npm test` 3회 exit 143(SIGTERM). `vitest-stop.sh` 정리 후 4회째 **1979/1979 PASS**. 파이프라인 동시 실행 시 `.agents/rules.md` §5 준수 필요.

### Merged commits (1261차 · `dfa981c`→`daaba4b`)

1. `dffd726` — US-E05 attendance stats API + absence checkout wire
2. `df7f308` — UXD-152 a11y (G-STAFF-WORK-ATTENDANCE·CmsDebitPanel·US-E05)
3. `77b1ea8` — G-BILLING-REPORT-FILTER-PERSISTENCE FE wire
4. `daaba4b` — QA-B233 DatePicker `오늘` suffix test utils fix

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-22T03:38:36+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-22 1259차)

> **1259차 BLOCK(merge SKIP)** — test `@dfa981c` · develop `@77b1ea8` · `test..develop` **0/3** pending · develop HEAD committed **1978/1979 FAIL**(carry) · develop WT **DIRTY 1M**(`pickerTestUtils.js` WIP) · dirty partial `CareServiceSpecialNotesPage` **3/3 PASS** · merge **SKIP** · build **1089 modules PASS** · audit **0** · live E2E **SKIP** · Open **2(active frontend: QA-B233+B234)** · transfer **BLOCK** · cross-stream **BLOCK(BE SYNCED@fd0a3b3 · FE pending 3+dirty)** · operation **BLOCK**
