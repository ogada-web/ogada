<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-22T22:03:57+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-22 1292차)

> **1292차 BLOCK(merge SKIP)** — regression run `@a170f9c` **2030/2031 PASS**(689.73s, 397 files, **1 FAIL**) · FAIL: `pilotPageFlows.test.jsx` > `renders Must page /staff/annual-leaves` (`직원 연차휴가` text not found) · develop `@80613c3` **CLEAN** · `test..develop` **0/1 pending** · build **1147 modules PASS**(9.45s) · audit **0** · live E2E 1차 LOCKED(concurrency guard) → `vitest-stop.sh` 정리 후 **126 PASS/19 SKIP**(35.61s) · **QA-20260622-B255 Open(BLOCK)** + backend carry **QA-20260622-B254 Open(BLOCK)** · transfer **BLOCK** · cross-stream **BLOCK(BE pending 1 + FE pending 1/regression)** · operation **BLOCK**

## 1292차 검증 요약 (merge SKIP — BLOCK)

| 항목 | 결과 |
|---|---|
| test worktree HEAD | `a170f9c` |
| develop HEAD | `80613c3` |
| ahead (`test..develop`) | **0/1** (`80613c3` pending) |
| develop working tree | **CLEAN** |
| test working tree | **DIRTY** (`?? 9`, 무해한 빈 파일 carry) |
| npm test (regression @ test) | **2030/2031 PASS** (689.73s, 397 files, **1 FAIL**) |
| failing test | `pilotPageFlows` → `renders Must page /staff/annual-leaves` (`직원 연차휴가` text mismatch) |
| npm test (develop pre-merge) | **SKIP** (pending 1 + test regression 우선) |
| post-merge npm test | **SKIP** (merge 미실행) |
| build | **1147 modules PASS** (9.45s) |
| npm audit (high+) | **0 vulnerabilities** |
| live E2E | **126 PASS / 19 SKIP** (35.61s; 1차 LOCKED → cleanup rerun PASS) |
| transfer verdict | **BLOCK** |
| open issue (frontend) | **1** (`QA-20260622-B255`) |
| open issue (backend carry) | **1** (`QA-20260622-B254`) |
| cross-stream | **BLOCK (BE pending 1 @f88e8b1 + FE pending 1 @80613c3 with regression)** |
| operation | **BLOCK** (origin/test push 519 BE+173 FE + QA-B255 + QA-B254 + QA-B95 partial 19 SKIP) |

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-22T20:20:00+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-22 1289차)

> **1289차 PASS(merge EXECUTED)** — baseline carry `@3902dba` **2023/2023 PASS**(1287차) · develop pre-merge `@6fcd750` **2025/2025 PASS**(692.61s, 397 files) · ★ merge EXECUTED FF `3902dba`→`6fcd750` (1 commit) · post-merge **2025/2025 PASS**(692.61s) · build **1147 modules PASS**(8.58s) · audit **0** · live E2E **126 PASS/19 SKIP**(36.32s) · develop/test `@6fcd750` **SYNCED** · **QA-20260622-B252 Fixed** · transfer **PASS** · cross-stream **SYNCED(FE@6fcd750 + BE@6b84bcd)** · operation **BLOCK**

## 1289차 검증 요약 (merge EXECUTED — SYNCED)

| 항목 | 결과 |
|---|---|
| test worktree HEAD | `6fcd750` |
| develop HEAD | `6fcd750` |
| ahead (`test..develop`) | **0/0** (SYNCED) |
| develop working tree | **CLEAN** |
| test working tree | **DIRTY** (`?? 9`, 무해한 빈 파일 carry) |
| npm test (baseline) | **2023/2023 PASS** carry @ `3902dba` (1287차) |
| npm test (develop pre-merge) | **2025/2025 PASS** @ `6fcd750` (692.61s, 397 files) |
| post-merge npm test | **2025/2025 PASS** @ `6fcd750` (692.61s, 397 files) |
| build | **1147 modules PASS** (8.58s) |
| npm audit (high+) | **0 vulnerabilities** |
| live E2E | **126 PASS / 19 SKIP** (36.32s) |
| transfer verdict | **PASS** |
| open issue (frontend) | **0** |
| cross-stream | **SYNCED (FE@6fcd750 + BE@6b84bcd)** |
| operation | **BLOCK** (origin/test push 518 BE+172 FE + QA-B95 partial 19 SKIP) |

### Merged commits (`3902dba`→`6fcd750`, 1 commit)

1. `6fcd750` — `fix(v1.2.1/qa-b95): ignore default credential blockers after auth recovery` (`liveConfig.js` default-credential blocker ignore · `liveE2eHarness.test.js` +2 tests)

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-22T17:48:37+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-22 1285차)

> **1285차 PASS(SYNCED revalidation)** — `@3ece965` **2010/2010 PASS**(671.86s, 393 files) · build **1144 modules PASS**(8.05s) · audit **0** · live E2E **126 PASS/19 SKIP**(35.00s) · develop/test `@3ece965` **SYNCED** · merge **SKIP**(`test..develop` **0/0**) · transfer **PASS** · cross-stream **BLOCK(BE pending 2 @d3d4d2d QA-B248 · FE SYNCED@3ece965)** · operation **BLOCK**

## 1285차 검증 요약 (SYNCED revalidation)

| 항목 | 결과 |
|---|---|
| test worktree HEAD | `3ece965` |
| develop HEAD | `3ece965` |
| ahead (`test..develop`) | **0/0** (SYNCED) |
| develop working tree | **CLEAN** |
| test working tree | **DIRTY** (`?? 9`, 무해한 빈 파일 carry) |
| npm test (SYNCED revalidation) | **2010/2010 PASS** @ `3ece965` (671.86s, 393 files) |
| build | **1144 modules PASS** (8.05s) |
| npm audit (high+) | **0 vulnerabilities** |
| live E2E | **126 PASS / 19 SKIP** (35.00s) |
| transfer verdict | **PASS** |
| open issue (frontend) | **0** |
| cross-stream | **BLOCK (FE SYNCED · BE pending 2 QA-B248)** |
| operation | **BLOCK** (origin/test push 514 BE+169 FE + QA-B95 partial 19 SKIP) |

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-22T17:26:49+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-22 1284차)

> **1284차 PASS(merge EXECUTED)** — baseline carry `@947312c` **2008/2008 PASS**(1282차) · develop pre-merge **2010/2010 PASS**(685.44s, 393 files) · ★ merge EXECUTED FF `947312c`→`3ece965` (1 commit) · post-merge **2010/2010 PASS**(678.62s, 393 files) · build **1144 modules PASS**(8.04s) · audit **0** · live E2E **126 PASS/19 SKIP**(35.22s) · develop/test `@3ece965` **SYNCED** WT **CLEAN** · **QA-20260622-B250 Fixed** · transfer **PASS** · cross-stream **BLOCK(BE pending 2 @d3d4d2d QA-B248 · FE SYNCED@3ece965)** · operation **BLOCK**

## 1284차 검증 요약 (merge EXECUTED — SYNCED)

| 항목 | 결과 |
|---|---|
| test worktree HEAD | `3ece965` |
| develop HEAD | `3ece965` |
| ahead (`test..develop`) | **0/0** (SYNCED) |
| develop working tree | **CLEAN** |
| test working tree | **DIRTY** (`?? 9`, 무해한 빈 파일 carry) |
| npm test (develop pre-merge) | **2010/2010 PASS** @ `3ece965` (685.44s, 393 files) |
| post-merge npm test | **2010/2010 PASS** @ `3ece965` (678.62s, 393 files) |
| build | **1144 modules PASS** (8.04s) |
| npm audit (high+) | **0 vulnerabilities** |
| live E2E | **126 PASS / 19 SKIP** (35.22s) |
| transfer verdict | **PASS** |
| open issue (frontend) | **0** |
| cross-stream | **BLOCK (FE SYNCED · BE pending 2 QA-B248)** |
| operation | **BLOCK** (origin/test push 514 BE+169 FE + QA-B95 partial 19 SKIP) |

### Merged commits (`947312c`→`3ece965`, 1 commit)

1. `3ece965` — `feat(v1.2.1/G2-CMS-ENROLLMENT-ROSTER): deepen CMS roster branch scope and client links` (`CmsEnrollmentTable` branch scope · `CmsPage` client links · unit tests +2)

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-22T16:41:32+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-22 1282차)

> **1282차 PASS(merge EXECUTED)** — baseline carry `@df9ec6c` **2005/2005 PASS**(1280차) · develop pre-merge **2008/2008 PASS**(683.98s, 393 files) · ★ merge EXECUTED FF `df9ec6c`→`947312c` (1 commit) · post-merge **2008/2008 PASS**(685.77s, 393 files) · build **1144 modules PASS**(12.09s) · audit **0** · live E2E **126 PASS/19 SKIP**(39.13s) · develop/test `@947312c` **SYNCED** WT **CLEAN** · **QA-20260622-B249 Fixed** · transfer **PASS** · cross-stream **BLOCK(BE pending 1 @d0c0d12 QA-B248 · FE SYNCED@947312c)** · operation **BLOCK**

## 1282차 검증 요약 (merge EXECUTED — SYNCED)

| 항목 | 결과 |
|---|---|
| test worktree HEAD | `947312c` |
| develop HEAD | `947312c` |
| ahead (`test..develop`) | **0/0** (SYNCED) |
| develop working tree | **CLEAN** |
| test working tree | **DIRTY** (`?? 9`, 무해한 빈 파일 carry) |
| npm test (develop pre-merge) | **2008/2008 PASS** @ `947312c` (683.98s, 393 files) |
| post-merge npm test | **2008/2008 PASS** @ `947312c` (685.77s, 393 files) |
| build | **1144 modules PASS** (12.09s) |
| npm audit (high+) | **0 vulnerabilities** |
| live E2E | **126 PASS / 19 SKIP** (39.13s) |
| transfer verdict | **PASS** |
| open issue (frontend) | **0** |
| cross-stream | **BLOCK (FE SYNCED · BE pending 1 QA-B248)** |
| operation | **BLOCK** (origin/test push 514 BE+168 FE + QA-B95 partial 19 SKIP) |

### Merged commits (`df9ec6c`→`947312c`, 1 commit)

1. `947312c` — `feat(v1.2.1/G2-CMS-ENROLLMENT-ROSTER): deepen CMS roster UX with FilterChips and payment deep links` (`CmsPage` FilterChips · `PaymentPage` payment deep links · unit tests +3)

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-22T15:29:00+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-22 1280차)

> **1280차 PASS(merge EXECUTED)** — baseline carry `@9f110a5` **2004/2004 PASS**(1278차) · develop pre-merge **2005/2005 PASS**(684.94s, 393 files) · ★ merge EXECUTED FF `9f110a5`→`df9ec6c` (1 commit) · post-merge **2005/2005 PASS**(685.05s, 393 files) · build **1144 modules PASS**(8.15s) · audit **0** · live E2E **126 PASS/19 SKIP**(41.10s) · develop/test `@df9ec6c` **SYNCED** WT **CLEAN** · **QA-20260622-B247 Fixed** · transfer **PASS** · cross-stream **BLOCK(BE dirty@d361833 QA-B246 · FE SYNCED@df9ec6c)** · operation **BLOCK**

## 1280차 검증 요약 (merge EXECUTED — SYNCED)

| 항목 | 결과 |
|---|---|
| test worktree HEAD | `df9ec6c` |
| develop HEAD | `df9ec6c` |
| ahead (`test..develop`) | **0/0** (SYNCED) |
| develop working tree | **CLEAN** |
| test working tree | **DIRTY** (`?? 9`, 무해한 빈 파일 carry) |
| npm test (develop pre-merge) | **2005/2005 PASS** @ `df9ec6c` (684.94s, 393 files) |
| post-merge npm test | **2005/2005 PASS** @ `df9ec6c` (685.05s, 393 files) |
| build | **1144 modules PASS** (8.15s) |
| npm audit (high+) | **0 vulnerabilities** |
| live E2E | **126 PASS / 19 SKIP** (41.10s) |
| transfer verdict | **PASS** |
| open issue (frontend) | **0** |
| cross-stream | **BLOCK (FE SYNCED · BE dirty QA-B246)** |
| operation | **BLOCK** (origin/test push 514 BE+167 FE + QA-B95 partial 19 SKIP) |

### Merged commits (`9f110a5`→`df9ec6c`, 1 commit)

1. `df9ec6c` — `feat(v1.2.1/G2-CMS-ENROLLMENT-ROSTER): wire branch roster filters into CMS and payments` (`services.js` branch roster query params · `CmsEnrollmentTable`/`CmsPage`/`PaymentPage` branch filter wire · unit tests +1)

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-22T13:55:17+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-22 1278차)

> **1278차 PASS(merge EXECUTED)** — pre-merge baseline `@77cfc38` · develop pre-merge **2004/2004 PASS**(683.88s, 393 files) · ★ merge EXECUTED FF `77cfc38`→`9f110a5` (1 commit) · post-merge **2004/2004 PASS**(685.34s, 393 files) · build **1144 modules PASS**(8.20s) · audit **0** · live E2E **126 PASS/19 SKIP**(35.89s) · develop/test `@9f110a5` **SYNCED** WT **CLEAN** · **QA-20260622-B245 Fixed** · transfer **PASS** · cross-stream **SYNCED(FE@9f110a5 + BE@d361833)** · operation **BLOCK**

## 1278차 검증 요약 (merge EXECUTED — SYNCED)

| 항목 | 결과 |
|---|---|
| test worktree HEAD | `9f110a5` |
| develop HEAD | `9f110a5` |
| ahead (`test..develop`) | **0/0** (SYNCED) |
| develop working tree | **CLEAN** |
| test working tree | **DIRTY** (`?? 9`, 무해한 빈 파일 carry) |
| npm test (develop pre-merge) | **2004/2004 PASS** @ `9f110a5` (683.88s, 393 files) |
| post-merge npm test | **2004/2004 PASS** @ `9f110a5` (685.34s, 393 files) |
| build | **1144 modules PASS** (8.20s) |
| npm audit (high+) | **0 vulnerabilities** |
| live E2E | **126 PASS / 19 SKIP** (35.89s) |
| transfer verdict | **PASS** |
| open issue (frontend) | **0** |
| cross-stream | **SYNCED (FE@9f110a5 + BE@d361833)** |
| operation | **BLOCK** (origin/test push 514 BE+166 FE + QA-B95 partial 19 SKIP) |

### Merged commits (`77cfc38`→`9f110a5`, 1 commit)

1. `9f110a5` — `feat(v1.2.1/G34-WORKFLOW-CATALOG): add cycle/citation filters and ezCare FAQ links` (`EzcareWorkflowCatalogPanel` FilterChips · `ezcareWorkflowCatalog.js` cycle/citation metadata · external FAQ anchors · pilot page-flow coverage)

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-22T12:50:09+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-22 1276차)

> **1276차 PASS(merge EXECUTED)** — pre-merge baseline `@fdc135b` · develop pre-merge **1999/1999 PASS**(684.75s, 393 files) · ★ merge EXECUTED FF `fdc135b`→`77cfc38` (1 commit) · post-merge **1999/1999 PASS**(688.19s, 393 files) · build **1144 modules PASS**(8.53s) · audit **0** · live E2E **126 PASS/19 SKIP**(36.00s) · develop/test `@77cfc38` **SYNCED** WT **CLEAN** · **QA-20260622-B243 Fixed** · transfer **PASS** · cross-stream **SYNCED(FE@77cfc38 + BE@24d25f1)** · operation **BLOCK**

## 1276차 검증 요약 (merge EXECUTED — SYNCED)

| 항목 | 결과 |
|---|---|
| test worktree HEAD | `77cfc38` |
| develop HEAD | `77cfc38` |
| ahead (`test..develop`) | **0/0** (SYNCED) |
| develop working tree | **CLEAN** |
| test working tree | **DIRTY** (`?? 9`, 무해한 빈 파일 carry) |
| npm test (develop pre-merge) | **1999/1999 PASS** @ `77cfc38` (684.75s, 393 files) |
| post-merge npm test | **1999/1999 PASS** @ `77cfc38` (688.19s, 393 files) |
| build | **1144 modules PASS** (8.53s) |
| npm audit (high+) | **0 vulnerabilities** |
| live E2E | **126 PASS / 19 SKIP** (36.00s) |
| transfer verdict | **PASS** |
| open issue (frontend) | **0** |
| cross-stream | **SYNCED (FE@77cfc38 + BE@24d25f1)** |
| operation | **BLOCK** (origin/test push 513 BE+165 FE + QA-B95 partial 19 SKIP) |

### Merged commits (`fdc135b`→`77cfc38`, 1 commit)

1. `77cfc38` — `feat(v1.2.1/G34-WORKFLOW-CATALOG): add ezCare workflow catalog cross-walk page` (`WorkflowCatalogPage` · `EzcareWorkflowCatalogPanel` · `ezcareWorkflowCatalog.js` 15/28 FAQ cross-walk)

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-22T11:44:44+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-22 1274차)

> **1274차 PASS(merge EXECUTED)** — pre-merge baseline `@d058e43` **1993/1993 PASS**(681.70s carry) · ★ merge EXECUTED FF `d058e43`→`fdc135b` (2 commits) · post-merge **1993/1993 PASS**(684.80s, 390 files) · build **1139 modules PASS**(11.56s) · audit **0** · live E2E **126 PASS/19 SKIP**(38.55s) · develop/test `@fdc135b` **SYNCED** WT **CLEAN** · **QA-20260622-B242 Fixed** · transfer **PASS** · cross-stream **BLOCK(BE dirty@9db0bbb QA-B241)** · operation **BLOCK**

## 1274차 검증 요약 (merge EXECUTED — SYNCED)

| 항목 | 결과 |
|---|---|
| test worktree HEAD | `fdc135b` |
| develop HEAD | `fdc135b` |
| ahead (`test..develop`) | **0/0** (SYNCED) |
| develop working tree | **CLEAN** |
| test working tree | **DIRTY** (`?? 9`, 무해한 빈 파일 carry) |
| npm test (pre-merge baseline) | **1993/1993 PASS** @ `d058e43` (681.70s carry, 390 files) |
| post-merge npm test | **1993/1993 PASS** @ `fdc135b` (684.80s, 390 files) |
| build | **1139 modules PASS** (11.56s) |
| npm audit (high+) | **0 vulnerabilities** |
| live E2E | **126 PASS / 19 SKIP** (38.55s) |
| transfer verdict | **PASS** |
| open issue (frontend) | **0** |
| cross-stream | **BLOCK (FE SYNCED@fdc135b · BE@9db0bbb DIRTY QA-B241)** |
| operation | **BLOCK** (origin/test push 512 BE+164 FE + QA-B95 partial 19 SKIP) |

### Merged commits (`d058e43`→`fdc135b`, 2 commits)

1. `da34daf` — `ux(a11y): US-D03출석탭·G-BILLING-REPORT-FILTER-PERSISTENCE·US-E03 QR 접근성 재점검 (UXD-153)`
2. `fdc135b` — `feat(v1.2.1/G30-LEGEND): add official indicator cross-walk legend on monitoring page`

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-22T10:54:46+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-22 1273차)

> **1273차 BLOCK(merge SKIP)** — test `@d058e43` 기준 회귀 `npm test` **1993/1993 PASS**(681.70s, 390 files) · build **1139 modules PASS**(10.07s) · audit **0** · live E2E **SKIP**(merge 미실행, 1271차 `126 PASS/19 SKIP` carry) · develop `@fdc135b` (`test..develop` **0/2**) WT **CLEAN** · merge **SKIP** · **QA-20260622-B242 Open (BLOCK)** · transfer **BLOCK** · cross-stream **BLOCK(FE pending 2 + BE dirty@9db0bbb)** · operation **BLOCK**

## 1273차 검증 요약 (merge SKIP — pending 2)

| 항목 | 결과 |
|---|---|
| test worktree HEAD | `d058e43` |
| develop HEAD | `fdc135b` |
| ahead (`test..develop`) | **0/2** |
| develop working tree | **CLEAN** |
| test working tree | **DIRTY** (`?? 9`, 무해한 빈 파일 carry) |
| npm test (test worktree) | **1993/1993 PASS** @ `d058e43` (681.70s, 390 files) |
| develop pre-merge npm test | **SKIP** (merge pending 2) |
| post-merge npm test | **SKIP** (merge not executed) |
| build | **1139 modules PASS** (10.07s) |
| npm audit (high+) | **0 vulnerabilities** |
| live E2E | **SKIP** (merge 미실행; carry = 1271차 126 PASS / 19 SKIP) |
| transfer verdict | **BLOCK** |
| open issue | **QA-20260622-B242 (BLOCK)** |
| cross-stream | **BLOCK (FE@fdc135b pending 2 + BE@9db0bbb DIRTY)** |
| operation | **BLOCK** (origin/test push pending + QA-B95 partial 19 SKIP) |

### Pending commits (`test..develop` 0/2)

1. `da34daf` — `ux(a11y): US-D03출석탭·G-BILLING-REPORT-FILTER-PERSISTENCE·US-E03 QR 접근성 재점검 (UXD-153)`
2. `fdc135b` — `feat(v1.2.1/G30-LEGEND): add official indicator cross-walk legend on monitoring page`

### Planned blocker action

1. `da34daf`+`fdc135b` 기준 develop→test merge 실행.
2. post-merge `npm test`/`npm run build`/`npm run test:live-e2e` 재검증.
3. `QA-20260622-B242`를 Fixed로 전환하고 transfer verdict를 PASS로 복구.

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-22T09:02:45+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-22 1271차)

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
