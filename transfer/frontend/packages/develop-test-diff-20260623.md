<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-23T18:23:23+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-23 1331차)

> **1331차 BLOCK(develop dirty + merge pending 4 · npm re-run SKIP concurrency)** — baseline carry `@b7101d5` **2049/2049 PASS**(1320차) · npm re-run **SKIP**(vitest concurrency · `src/frontend` develop PID 657264) · develop `@64584f4` WT **DIRTY 48M+18U** · test `@b7101d5` · merge **SKIP**(`test..develop` **0/4** pending · dirty) · build **1149 modules PASS**(10.25s @ test) · audit **0** · live E2E **SKIP**(127/19 carry) · **QA-B273 Planned(update,BLOCK)** · transfer **BLOCK** · cross-stream **BLOCK(BE pending 2 @c4e6bcb · FE dirty pending 4)** · operation **BLOCK**

## 1331차 검증 요약 (vitest concurrency SKIP · develop dirty recurrence)

| 항목 | 결과 |
|---|---|
| test/develop HEAD | test `b7101d5` · develop `64584f4` |
| ahead (`test..develop`) | **0/4** pending (`8057c1e` · `bd1d0ad` · `426d63a` · `64584f4`) |
| develop working tree | **DIRTY 48M+18U** (66 status lines: dashboard·client-list·transport·address·nav WIP) |
| test working tree | **DIRTY** (`?? 9`, 무해한 빈 파일 carry) |
| npm test baseline (@b7101d5) | **2049/2049 PASS** (1320차 carry · 1331차 re-run SKIP concurrency) |
| npm test pre-merge | **SKIP** (develop dirty · merge blocked) |
| merge | **SKIP** (0/4 pending + dirty-tree) |
| pending diff (committed) | `8057c1e` leave-ledger wire · `bd1d0ad` UXD-157 a11y · `426d63a` relatedSurfaces test · `64584f4` HR leave branch scope metadata |
| build | **1149 modules PASS** (10.25s @ test) |
| npm audit (high+) | **0** |
| live E2E | **SKIP** (merge 없음 · 1320차 **127 PASS / 19 SKIP** carry) |
| transfer verdict | **BLOCK** |
| planned issue (frontend) | **QA-20260623-B273** (update · dirty-tree + pending 4) |
| cross-stream | **BLOCK** (BE pending 2 @c4e6bcb QA-B272 · FE dirty@64584f4 QA-B273) |
| operation | **BLOCK** (QA-B273 + QA-B272 + origin/test push 530 BE+187 FE + QA-B95 partial 19 SKIP) |

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-23T17:44:14+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-23 1329차)

> **1329차 BLOCK(develop dirty + merge pending 3 · npm re-run SKIP concurrency)** — baseline carry `@b7101d5` **2049/2049 PASS**(1320차) · npm re-run **SKIP**(vitest concurrency · partial PID 633126) · develop `@426d63a` WT **DIRTY 44M+12U** · test `@b7101d5` · merge **SKIP**(`test..develop` **0/3** pending · dirty) · build **1149 modules PASS**(9.66s @ test) · audit **1 high** · live E2E **SKIP**(127/19 carry) · **QA-B273 Planned(carry,BLOCK)** · transfer **BLOCK** · cross-stream **BLOCK(BE pending 2 @c4e6bcb · FE dirty pending 3)** · operation **BLOCK**

## 1329차 검증 요약 (vitest concurrency SKIP · develop dirty carry)

| 항목 | 결과 |
|---|---|
| test/develop HEAD | test `b7101d5` · develop `426d63a` |
| ahead (`test..develop`) | **0/3** pending (`8057c1e` · `bd1d0ad` · `426d63a`) |
| develop working tree | **DIRTY 44M+12U** (56 status lines: dashboard·client-list·transport·nav WIP) |
| test working tree | **DIRTY** (`?? 9`, 무해한 빈 파일 carry) |
| npm test baseline (@b7101d5) | **2049/2049 PASS** (1320차 carry · 1329차 re-run SKIP concurrency) |
| npm test pre-merge | **SKIP** (develop dirty · merge blocked) |
| merge | **SKIP** (0/3 pending + dirty-tree) |
| pending diff (committed) | `8057c1e` leave-ledger wire · `bd1d0ad` UXD-157 a11y · `426d63a` relatedSurfaces test |
| build | **1149 modules PASS** (9.66s @ test) |
| npm audit (high+) | **1 high** (form-data CRLF) |
| live E2E | **SKIP** (merge 없음 · 1320차 **127 PASS / 19 SKIP** carry) |
| transfer verdict | **BLOCK** |
| planned issue (frontend) | **QA-20260623-B273** (carry · dirty-tree + pending 3) |
| cross-stream | **BLOCK** (BE pending 2 @c4e6bcb QA-B272 · FE dirty@426d63a QA-B273) |
| operation | **BLOCK** (QA-B273 + QA-B272 + origin/test push 530 BE+187 FE + QA-B95 partial 19 SKIP) |

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-23T17:32:00+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-23 1328차)

> **1328차 BLOCK(develop dirty + merge pending 3 · npm re-run Terminated 3rd hang)** — baseline carry `@b7101d5` **2049/2049 PASS**(1320차) · npm re-run **Terminated exit 143**(~625.2s · no summary · 1322/1325/1328 3rd hang) · develop `@426d63a` WT **DIRTY 44M+12U** · test `@b7101d5` · merge **SKIP**(`test..develop` **0/3** pending · dirty) · build **1149 modules PASS**(9.75s @ test) · audit **1 high** · live E2E **SKIP**(127/19 carry) · **QA-B273 Planned(carry,BLOCK)** · transfer **BLOCK** · cross-stream **BLOCK(BE pending 2 @c4e6bcb · FE dirty pending 3)** · operation **BLOCK**

## 1328차 검증 요약 (vitest hang Terminated · develop dirty carry)

| 항목 | 결과 |
|---|---|
| test/develop HEAD | test `b7101d5` · develop `426d63a` |
| ahead (`test..develop`) | **0/3** pending (`8057c1e` · `bd1d0ad` · `426d63a`) |
| develop working tree | **DIRTY 44M+12U** (56 status lines: dashboard·client-list·transport·nav WIP) |
| test working tree | **DIRTY** (`?? 1`, 무해한 빈 파일 carry) |
| npm test baseline (@b7101d5) | **2049/2049 PASS** (1320차 carry · 1328차 re-run Terminated exit 143 ~625.2s) |
| npm test pre-merge | **SKIP** (develop dirty · merge blocked) |
| merge | **SKIP** (0/3 pending + dirty-tree) |
| pending diff (committed) | `8057c1e` leave-ledger wire · `bd1d0ad` UXD-157 a11y · `426d63a` relatedSurfaces test |
| build | **1149 modules PASS** (9.75s @ test) |
| npm audit (high+) | **1 high** (form-data CRLF) |
| live E2E | **SKIP** (merge 없음 · 1320차 **127 PASS / 19 SKIP** carry) |
| transfer verdict | **BLOCK** |
| planned issue (frontend) | **QA-20260623-B273** (carry · vitest hang recurrence) |
| cross-stream | **BLOCK** (BE pending 2 @c4e6bcb QA-B272 · FE dirty@426d63a QA-B273) |
| operation | **BLOCK** (QA-B273 + QA-B272 + origin/test push 530 BE+187 FE + QA-B95 partial 19 SKIP) |

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-23T17:02:31+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-23 1326차)

> **1326차 BLOCK(develop dirty + merge pending 3 · npm re-run SKIP concurrency)** — baseline carry `@b7101d5` **2049/2049 PASS**(1320차) · npm re-run **SKIP**(`src/frontend` vitest active · concurrency rule) · develop `@426d63a` WT **DIRTY 38M+11U** · test `@b7101d5` · merge **SKIP**(`test..develop` **0/3** pending · dirty) · build **1149 modules PASS**(10.57s @ test) · audit **1 high** · live E2E **SKIP**(127/19 carry) · **QA-B273 Planned(carry,BLOCK)** · transfer **BLOCK** · cross-stream **BLOCK(BE B272 · FE dirty pending 3)** · operation **BLOCK**

## 1326차 검증 요약 (vitest concurrency SKIP · develop dirty carry)

| 항목 | 결과 |
|---|---|
| test/develop HEAD | test `b7101d5` · develop `426d63a` |
| ahead (`test..develop`) | **0/3** pending (`8057c1e` · `bd1d0ad` · `426d63a`) |
| develop working tree | **DIRTY 38M+11U** (52 status lines: dashboard·client-list·transport·nav WIP) |
| test working tree | **DIRTY** (`?? 9`, 무해한 빈 파일 carry) |
| npm test baseline (@b7101d5) | **2049/2049 PASS** (1320차 carry · 1326차 re-run SKIP vitest concurrency) |
| npm test pre-merge | **SKIP** (develop dirty · merge blocked) |
| merge | **SKIP** (0/3 pending + dirty-tree) |
| pending diff (committed) | `8057c1e` leave-ledger wire · `bd1d0ad` UXD-157 a11y · `426d63a` relatedSurfaces test |
| build | **1149 modules PASS** (10.57s @ test) |
| npm audit (high+) | **1 high** |
| live E2E | **SKIP** (merge 없음 · 1320차 **127 PASS / 19 SKIP** carry) |
| transfer verdict | **BLOCK** |
| planned issue (frontend) | **QA-20260623-B273** (carry) |
| cross-stream | **BLOCK** (BE dirty@5fd12dd QA-B272 · FE dirty@426d63a QA-B273) |
| operation | **BLOCK** (QA-B273 + QA-B272 + origin/test push 530 BE+187 FE + QA-B95 partial 19 SKIP) |

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-23T16:59:14+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-23 1325차)

> **1325차 BLOCK(develop dirty recurrence + merge pending 3)** — baseline carry `@b7101d5` **2049/2049 PASS**(1320차) · npm re-run **Terminated exit 143**(~743.48s · 2nd hang) · develop `@426d63a` WT **DIRTY 38M+11U** · test `@b7101d5` · merge **SKIP**(`test..develop` **0/3** pending · dirty) · build **1159 modules PASS**(9.61s · develop dirty) · audit **1 high** · live E2E **SKIP**(127/19 carry) · **QA-B273 Planned(update,BLOCK)** · transfer **BLOCK** · cross-stream **BLOCK(BE B272 · FE dirty pending 3)** · operation **BLOCK**

## 1325차 검증 요약 (develop dirty recurrence · merge pending 3)

| 항목 | 결과 |
|---|---|
| test/develop HEAD | test `b7101d5` · develop `426d63a` |
| ahead (`test..develop`) | **0/3** pending (`8057c1e` · `bd1d0ad` · `426d63a`) |
| develop working tree | **DIRTY 38M+11U** (49 files: dashboard·client-list·transport·nav·compliance WIP) |
| test working tree | **DIRTY** (`?? 9`, 무해한 빈 파일 carry) |
| npm test baseline (@b7101d5) | **2049/2049 PASS** (1320차 carry · 1325차 re-run Terminated exit 143 ~640.75s) |
| npm test pre-merge | **SKIP** (develop dirty · merge blocked) |
| merge | **SKIP** (0/3 pending + dirty-tree) |
| pending diff (committed) | `8057c1e` leave-ledger wire · `bd1d0ad` UXD-157 a11y · `426d63a` relatedSurfaces test |
| pending diff (uncommitted) | dashboard filters · client list · transport roster · nav refactor 등 49 files |
| build | **1149 modules PASS** (10.41s @ test) |
| npm audit (high+) | **0 vulnerabilities** |
| live E2E | **SKIP** (merge 없음 · 1320차 **127 PASS / 19 SKIP** carry) |
| transfer verdict | **BLOCK** |
| planned issue (frontend) | **QA-20260623-B273** (update: dirty 5M→38M+11U) |
| cross-stream | **BLOCK** (BE dirty@5fd12dd QA-B272 · FE dirty@426d63a QA-B273) |
| operation | **BLOCK** (QA-B273 + QA-B272 + origin/test push 530 BE+187 FE + QA-B95 partial 19 SKIP) |

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-23T15:02:51+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-23 1322차)

> **1322차 BLOCK(develop dirty + merge pending 1)** — baseline carry `@b7101d5` **2049/2049 PASS**(1320차) · npm re-run **Terminated exit 143**(~467s) · develop `@8057c1e` WT **DIRTY 5M** · test `@b7101d5` · merge **SKIP**(`test..develop` **0/1** pending `8057c1e` · dirty) · build **1153 modules PASS**(13.59s) · audit **0** · live E2E **SKIP**(127/19 carry) · **QA-B273 Open(BLOCK)** · transfer **BLOCK** · cross-stream **BLOCK(BE B272 · FE dirty pending 1)** · operation **BLOCK**

## 1322차 검증 요약 (develop dirty · merge pending 1)

| 항목 | 결과 |
|---|---|
| test/develop HEAD | test `b7101d5` · develop `8057c1e` |
| ahead (`test..develop`) | **0/1** pending (`8057c1e` leave ledger page wire) |
| develop working tree | **DIRTY 5M** (`TransportPage*` · `transportRosterDispatch*` · `pilotLivePages.e2e`) |
| test working tree | **DIRTY** (`?? 9`, 무해한 빈 파일 carry) |
| npm test baseline (@b7101d5) | **2049/2049 PASS** (1320차 carry · 1322차 re-run Terminated exit 143) |
| npm test pre-merge | **SKIP** (develop dirty · merge blocked) |
| merge | **SKIP** (0/1 pending + dirty-tree) |
| pending diff (committed) | `8057c1e` staff leave ledger page + API client |
| pending diff (uncommitted) | transport roster dispatch 5 files |
| build | **1153 modules PASS** (13.59s · dirty WT) |
| npm audit (high+) | **0 vulnerabilities** |
| live E2E | **SKIP** (merge 없음 · 1320차 **127 PASS / 19 SKIP** carry) |
| transfer verdict | **BLOCK** |
| open issue (frontend) | **1** — QA-20260623-B273 |
| cross-stream | **BLOCK** (BE dirty@5fd12dd QA-B272 · FE dirty@8057c1e QA-B273) |
| operation | **BLOCK** (QA-B273 + QA-B272 + origin/test push 530 BE+187 FE + QA-B95 partial 19 SKIP) |

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-23T14:24:02+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-23 1320차)

> **1320차 PASS(SYNCED revalidation)** — ROADMAP merged `@b7101d5` post-merge **2049/2049 PASS**(706.75s carry) · develop/test `@b7101d5` **SYNCED** · develop WT **CLEAN** · merge **SKIP**(`test..develop` **0/0** · 1318차 FF `949e9bf`→`b7101d5` applied) · build **1149 modules PASS**(8.41s) · audit **0** · live E2E **127 PASS/19 SKIP**(37.45s) · **★ QA-B270 Fixed** · transfer **PASS** · cross-stream **SYNCED(FE@b7101d5 + BE@62fce23)** · operation **BLOCK**

## 1320차 검증 요약 (SYNCED revalidation)

| 항목 | 결과 |
|---|---|
| test/develop HEAD | `b7101d5` |
| ahead (`test..develop`) | **0/0** SYNCED |
| develop working tree | **CLEAN** |
| test working tree | **DIRTY** (`?? 9`, 무해한 빈 파일 carry) |
| npm test post-merge (@b7101d5) | **2049/2049 PASS** (706.75s, 399 files · 1318차 carry) |
| StaffAnnualLeavePage isolated | **8/8 PASS** (6.69s) |
| merge | **SKIP** (0/0 SYNCED · 1318차 merge applied) |
| pending diff | none |
| build | **1149 modules PASS** (8.41s) |
| npm audit (high+) | **0 vulnerabilities** |
| live E2E | **127 PASS / 19 SKIP** (37.45s) |
| transfer verdict | **PASS** |
| open issue (frontend) | **0** |
| fixed this cycle | QA-20260623-B270 @ `b7101d5` (non-repro · B266 lineage) |
| cross-stream | **SYNCED** (FE@b7101d5 + BE@62fce23) |
| operation | **BLOCK** (origin/test push 530 BE+187 FE + QA-B95 partial 19 SKIP) |

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-23T13:51:40+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-23 1318차)

> **1318차 BLOCK(pre-merge FAIL · merge pending 1)** — baseline `@949e9bf` **2049/2049 PASS**(705.68s) · develop `@b7101d5` WT **CLEAN** · develop pre-merge **2048/2049 FAIL**(748.62s · `StaffAnnualLeavePage` · isolated **8/8 PASS**) · merge **SKIP**(`test..develop` **0/1** · pre-merge FAIL) · build **1149 modules PASS**(9.58s) · audit **0** · live E2E **127 PASS/19 SKIP carry** · **★ QA-B268 Fixed** · **QA-B270 Open(BLOCK)** · transfer **BLOCK** · cross-stream **BLOCK(FE pre-merge FAIL · BE SYNCED@bb9df48)** · operation **BLOCK**

## 1318차 검증 요약 (pre-merge FAIL · merge pending 1)

| 항목 | 결과 |
|---|---|
| test/develop HEAD | test `949e9bf` · develop `b7101d5` |
| ahead (`test..develop`) | **0/1** pending (`b7101d5`) |
| develop working tree | **CLEAN** |
| test working tree | **DIRTY** (`?? 9`, 무해한 빈 파일 carry) |
| npm test baseline (@949e9bf) | **2049/2049 PASS** (705.68s, 399 files) |
| npm test pre-merge (@b7101d5) | **2048/2049 FAIL** (748.62s · isolated **8/8 PASS**) |
| merge | **SKIP** (0/1 pending · pre-merge FAIL) |
| pending diff | `liveE2eSuiteGuard.test.js` (+10/-3L) |
| build | **1149 modules PASS** (9.58s) |
| npm audit (high+) | **0 vulnerabilities** |
| live E2E | **127 PASS / 19 SKIP** (carry·1314차) |
| transfer verdict | **BLOCK** |
| open issue (frontend) | **1** — QA-20260623-B270 |
| fixed this cycle | QA-20260623-B268 @ `b7101d5` |
| cross-stream | **BLOCK** (FE pre-merge FAIL · BE SYNCED@bb9df48) |
| operation | **BLOCK** (QA-B270 + origin/test push 529 BE+187 FE + QA-B95 partial 19 SKIP) |

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-23T12:22:30+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-23 1316차)

> **1316차 BLOCK(SYNCED revalidation · develop dirty)** — ROADMAP merged `@949e9bf` **2049/2049 PASS**(707.43s, 399 files) · develop/test `@949e9bf` SYNCED · develop WT **DIRTY 1M**(`liveE2eSuiteGuard.test.js`) · merge **SKIP**(`test..develop` **0/0** SYNCED+dirty) · build **1149 modules PASS**(10.20s) · audit **0** · live E2E **127 PASS/19 SKIP carry**(1314차) · **QA-B268 Open(BLOCK)** · transfer **BLOCK** · cross-stream **BLOCK(FE dirty · BE SYNCED@f1225b0)** · operation **BLOCK**

## 1316차 검증 요약 (SYNCED revalidation · develop dirty)

| 항목 | 결과 |
|---|---|
| test/develop HEAD | `949e9bf` |
| ahead (`test..develop`) | **0/0** SYNCED |
| develop working tree | **DIRTY 1M** (`liveE2eSuiteGuard.test.js` +10/-3L WIP) |
| test working tree | **DIRTY** (`?? 9`, 무해한 빈 파일 carry) |
| npm test (@949e9bf) | **2049/2049 PASS** (707.43s, 399 files) |
| merge | **SKIP** (0/0 SYNCED · develop dirty) |
| build | **1149 modules PASS** (10.20s) |
| npm audit (high+) | **0 vulnerabilities** |
| live E2E | **127 PASS / 19 SKIP** (carry·1314차 · re-run Terminated) |
| transfer verdict | **BLOCK** |
| open issue (frontend) | **1** — QA-20260623-B268 |
| cross-stream | **BLOCK** (FE develop dirty@949e9bf · BE SYNCED@f1225b0) |
| operation | **BLOCK** (QA-B268 + origin/test push 528 BE+186 FE + QA-B95 partial 19 SKIP) |

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-23T12:21:43+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-23 1316차)

> **1316차 BLOCK(SYNCED revalidation · develop dirty)** — ROADMAP merged `@949e9bf` **2049/2049 PASS**(707.43s, 399 files) · develop/test `@949e9bf` SYNCED · develop WT **DIRTY 1M**(`liveE2eSuiteGuard.test.js`) · merge **SKIP**(`test..develop` **0/0** · develop dirty) · build **1149 modules PASS**(8.52s) · audit **0** · live E2E **127 PASS/19 SKIP carry** · **QA-B268 Open(BLOCK)** · transfer **BLOCK** · cross-stream **BLOCK(FE dirty · BE SYNCED@f1225b0)** · operation **BLOCK**

## 1316차 검증 요약 (SYNCED revalidation · develop dirty)

| 항목 | 결과 |
|---|---|
| test/develop HEAD | `949e9bf` |
| ahead (`test..develop`) | **0/0** SYNCED |
| develop working tree | **DIRTY** (`M liveE2eSuiteGuard.test.js` +10/-3L WIP) |
| test working tree | **DIRTY** (`?? 9`, 무해한 빈 파일 carry) |
| npm test (@949e9bf) | **2049/2049 PASS** (707.43s, 399 files) |
| merge | **SKIP** (0/0 SYNCED · develop dirty) |
| build | **1149 modules PASS** (8.52s) |
| npm audit (high+) | **0 vulnerabilities** |
| live E2E | **127 PASS / 19 SKIP** (carry 1314차 · re-run Terminated) |
| transfer verdict | **BLOCK** |
| open issue (frontend) | **1** (QA-20260623-B268) |
| cross-stream | **BLOCK** (FE develop dirty@949e9bf · BE SYNCED@f1225b0) |
| operation | **BLOCK** (QA-B268 + origin/test push 528 BE+186 FE + QA-B95 partial 19 SKIP) |

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-23T11:28:44+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-23 1314차)

> **1314차 PASS(SYNCED revalidation)** — ROADMAP merged `@949e9bf` **2049/2049 PASS**(696.00s, 399 files) · develop/test `@949e9bf` SYNCED · merge **SKIP**(`test..develop` **0/0** · 1311차 carry) · build **1149 modules PASS**(8.23s) · audit **0** · live E2E **127 PASS/19 SKIP**(36.25s) · Open **0(active frontend)** · transfer **PASS** · cross-stream **BLOCK(BE dirty@40ab9e7 QA-B267 · FE SYNCED@949e9bf)** · operation **BLOCK**

## 1314차 검증 요약 (SYNCED revalidation)

| 항목 | 결과 |
|---|---|
| test/develop HEAD | `949e9bf` |
| ahead (`test..develop`) | **0/0** SYNCED |
| develop working tree | **CLEAN** |
| test working tree | **DIRTY** (`?? 9`, 무해한 빈 파일 carry) |
| npm test (@949e9bf) | **2049/2049 PASS** (696.00s, 399 files) |
| merge | **SKIP** (0/0 · 1311차 post-merge carry) |
| build | **1149 modules PASS** (8.23s) |
| npm audit (high+) | **0 vulnerabilities** |
| live E2E | **127 PASS / 19 SKIP** (36.25s) |
| transfer verdict | **PASS** |
| open issue (frontend) | **0** |
| cross-stream | **BLOCK** (BE dirty@40ab9e7 QA-B267 · FE SYNCED@949e9bf) |
| operation | **BLOCK** (origin/test push 527 BE+186 FE + QA-B95 partial 19 SKIP) |

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-23T11:02:43+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-23 1313차)

> **1313차 PASS(SYNCED revalidation)** — ROADMAP merged `@949e9bf` **2049/2049 PASS**(696.21s, 399 files) · develop/test `@949e9bf` SYNCED · merge **SKIP**(`test..develop` **0/0** · 1311차 carry) · build **1149 modules PASS**(8.26s) · audit **0** · live E2E **127 PASS/19 SKIP**(36.56s) · Open **0(active frontend)** · transfer **PASS** · cross-stream **BLOCK(BE dirty@40ab9e7 QA-B267 · FE SYNCED@949e9bf)** · operation **BLOCK**

## 1313차 검증 요약 (SYNCED revalidation)

| 항목 | 결과 |
|---|---|
| test/develop HEAD | `949e9bf` |
| ahead (`test..develop`) | **0/0** SYNCED |
| develop working tree | **CLEAN** |
| test working tree | **DIRTY** (`?? 9`, 무해한 빈 파일 carry) |
| npm test (@949e9bf) | **2049/2049 PASS** (696.21s, 399 files) |
| merge | **SKIP** (0/0 · 1311차 post-merge carry) |
| build | **1149 modules PASS** (8.26s) |
| npm audit (high+) | **0 vulnerabilities** |
| live E2E | **127 PASS / 19 SKIP** (36.56s) |
| transfer verdict | **PASS** |
| open issue (frontend) | **0** |
| cross-stream | **BLOCK** (BE dirty@40ab9e7 QA-B267 · FE SYNCED@949e9bf) |
| operation | **BLOCK** (origin/test push 527 BE+186 FE + QA-B95 partial 19 SKIP) |

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-23T10:18:43+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-23 1311차)

> **1311차 PASS(post-merge SYNCED)** — pre-merge `@95f55aa` carry **2049/2049 PASS**(696.89s) · develop pre-merge `@949e9bf` **2049/2049 PASS**(687.36s, +3 tests) · ★ **merge EXECUTED** FF `95f55aa`→`949e9bf` (2 commits) · post-merge **2049/2049 PASS**(695.97s) · build **1149 modules PASS**(9.91s) · audit **0** · live E2E **127 PASS/19 SKIP**(37.03s) · **★ QA-B266 Fixed**(1310차 flake non-reproducible) · transfer **PASS** · cross-stream **SYNCED(FE@949e9bf + BE@40ab9e7)** · operation **BLOCK**

## 1311차 검증 요약 (merge EXECUTED · post-merge SYNCED)

| 항목 | 결과 |
|---|---|
| test worktree HEAD (pre-merge) | `95f55aa` |
| develop HEAD | `949e9bf` |
| ahead (`test..develop`) | **0/2** → merge EXECUTED |
| develop working tree | **CLEAN** |
| test working tree | **DIRTY** (`?? 9`, 무해한 빈 파일 carry) |
| npm test (@ test pre-merge carry) | **2049/2049 PASS** (696.89s, 399 files) |
| npm test (@ develop pre-merge) | **2049/2049 PASS** (687.36s, 399 files, +3 tests) |
| isolated `StaffAnnualLeavePage.test.jsx` | **8/8 PASS** (6.70s) |
| merge | **EXECUTED** FF `95f55aa`→`949e9bf` (2 commits) |
| npm test (post-merge) | **2049/2049 PASS** (695.97s, 399 files) |
| build | **1149 modules PASS** (9.91s) |
| npm audit (high+) | **0 vulnerabilities** |
| live E2E | **127 PASS / 19 SKIP** (37.03s) |
| transfer verdict | **PASS** |
| open issue (frontend) | **0** — QA-B266 Fixed |
| cross-stream | **SYNCED (FE@949e9bf + BE@40ab9e7)** |
| operation | **BLOCK** (origin/test push 527 BE+186 FE + QA-B95 partial 19 SKIP) |

### merged commits (`95f55aa..949e9bf`)

| SHA | 메시지 |
|---|---|
| `c183ebd` | ux(a11y): US-R01 relatedSurfaces cross-link panel + landmark fixes (UXD-156) |
| `949e9bf` | feat(v1.2.1/US-R01): show branch scope on staff HR roster pages |

### 잔여 리스크

- host root disk **99%** (ENOSPC during 1311차 초기 baseline — pip/npm cache purge로 ~2.2GB 확보 후 재검증)
- origin/test push **527 BE + 186 FE** 미실행 (QA-B116)
- live E2E **19 SKIP** carry (QA-B95 operation 승격 전)

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-23T09:21:13+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-23 1310차)

> **1310차 BLOCK(develop pre-merge regression)** — baseline `@95f55aa` **2046/2046 PASS**(783.20s, 398 files) · develop pre-merge `@949e9bf` **2048/2049 FAIL**(701.72s, 399 files, **1 FAIL** `StaffAnnualLeavePage` branch scope) · isolated file **8/8 PASS** · merge **SKIP**(`test..develop` **0/2** · pre-merge FAIL) · build **1149 modules PASS**(14.92s) · audit **0** · live E2E **127 PASS/19 SKIP carry** · **QA-B266 Open(BLOCK)** · transfer **BLOCK** · cross-stream **BLOCK(FE pending 2+regression · BE SYNCED@40ab9e7)** · operation **BLOCK**

## 1310차 검증 요약 (develop pre-merge FAIL · merge blocked)

| 항목 | 결과 |
|---|---|
| test worktree HEAD (baseline) | `95f55aa` |
| develop HEAD | `949e9bf` |
| ahead (`test..develop`) | **0/2** (`c183ebd` UXD-156 · `949e9bf` US-R01 branch scope) |
| develop working tree | **CLEAN** |
| test working tree | **DIRTY** (`?? 9`, 무해한 빈 파일 carry) |
| npm test (@ test baseline) | **2046/2046 PASS** (783.20s, 398 files) |
| npm test (@ develop pre-merge) | **2048/2049 FAIL** (701.72s, 399 files; `StaffAnnualLeavePage` branch scope) |
| isolated `StaffAnnualLeavePage.test.jsx` | **8/8 PASS** (8.77s · pollution suspect) |
| merge | **SKIP** (pre-merge FAIL · pending 2) |
| build | **1149 modules PASS** (14.92s) |
| npm audit (high+) | **0 vulnerabilities** |
| live E2E | **127 PASS / 19 SKIP** (carry·1308차) |
| transfer verdict | **BLOCK** |
| open issue (frontend) | **1** — QA-20260623-B266 |
| cross-stream | **BLOCK (FE pending 2+regression · BE SYNCED@40ab9e7)** |
| operation | **BLOCK** (QA-B266 + origin/test push 527 BE+184 FE + QA-B95 partial 19 SKIP) |

### pending commits (`test..develop`)

| SHA | 메시지 |
|---|---|
| `c183ebd` | ux(a11y): US-R01 relatedSurfaces cross-link panel + landmark fixes (UXD-156) |
| `949e9bf` | feat(v1.2.1/US-R01): show branch scope on staff HR roster pages |

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-23T07:25:04+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-23 1308차)

> **1308차 PASS(SYNCED revalidation)** — `@95f55aa` **2046/2046 PASS**(691.25s, 398 files) · develop/test **SYNCED** · merge **SKIP**(`test..develop` **0/0** · 1307차 carry) · build **1148 modules PASS**(11.53s) · audit **0** · live E2E **127 PASS/19 SKIP**(38.88s) · Open **0** · transfer **PASS** · cross-stream **SYNCED(FE@95f55aa + BE@83a26e7)** · operation **BLOCK**

## 1308차 검증 요약 (SYNCED revalidation PASS)

| 항목 | 결과 |
|---|---|
| test/develop HEAD | `95f55aa` (SYNCED) |
| ahead (`test..develop`) | **0/0** |
| develop working tree | **CLEAN** |
| test working tree | **DIRTY** (`?? 9`, 무해한 빈 파일 carry) |
| npm test (@ test) | **2046/2046 PASS** (691.25s, 398 files) |
| merge | **SKIP** (SYNCED · 1307차 carry) |
| build | **1148 modules PASS** (11.53s) |
| npm audit (high+) | **0 vulnerabilities** |
| live E2E | **127 PASS / 19 SKIP** (38.88s) |
| transfer verdict | **PASS** |
| open issue (frontend) | **0** |
| cross-stream | **SYNCED (FE@95f55aa + BE@83a26e7)** |
| operation | **BLOCK** (origin/test push 526 BE+184 FE + QA-B95 partial 19 SKIP) |

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-23T07:03:30+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-23 1307차)

> **1307차 PASS(SYNCED revalidation)** — `@95f55aa` **2046/2046 PASS**(694.54s, 398 files) · develop/test **SYNCED** · merge **SKIP**(`test..develop` **0/0** · 1306차 carry) · build **1148 modules PASS**(8.25s) · audit **0** · live E2E **127 PASS/19 SKIP**(36.42s) · Open **0** · transfer **PASS** · cross-stream **SYNCED(FE@95f55aa + BE@83a26e7)** · operation **BLOCK**

## 1307차 검증 요약 (SYNCED revalidation PASS)

| 항목 | 결과 |
|---|---|
| test/develop HEAD | `95f55aa` (SYNCED) |
| ahead (`test..develop`) | **0/0** |
| develop working tree | **CLEAN** |
| test working tree | **DIRTY** (`?? 9`, 무해한 빈 파일 carry) |
| npm test (@ test) | **2046/2046 PASS** (694.54s, 398 files) |
| merge | **SKIP** (SYNCED · 1306차 post-merge carry) |
| build | **1148 modules PASS** (8.25s) |
| npm audit (high+) | **0 vulnerabilities** |
| live E2E | **127 PASS / 19 SKIP** (36.42s) |
| transfer verdict | **PASS** |
| open issue (frontend) | **0** |
| cross-stream | **SYNCED (FE@95f55aa + BE@83a26e7)** |
| operation | **BLOCK** (origin/test push 526 BE+184 FE + QA-B95 partial 19 SKIP) |

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-23T06:48:39+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-23 1306차)

> **1306차 PASS(post-merge)** — pre-merge `@2040571` carry **2043/2043 PASS**(1304차) · develop pre-merge `@95f55aa` **2046/2046 PASS**(731.51s, +3 tests) · ★ merge **EXECUTED** FF `2040571`→`95f55aa` (1 commit) · post-merge **2046/2046 PASS**(698.02s) · build **1148 modules PASS**(8.29s) · audit **0** · live E2E **127 PASS/19 SKIP**(37.14s) · **★ QA-B264 Fixed @ `95f55aa`** · transfer **PASS** · cross-stream **SYNCED(FE@95f55aa + BE@83a26e7)** · operation **BLOCK**

## 1306차 검증 요약 (develop→test merge EXECUTED PASS)

| 항목 | 결과 |
|---|---|
| test worktree HEAD (pre-merge) | `2040571` |
| develop HEAD | `95f55aa` |
| ahead (`test..develop`) | **0/1** → merge EXECUTED |
| delta vs 1304차 | +1 commit `95f55aa` (US-R01 relatedSurfaces wire) · +3 tests (2043→2046) |
| develop working tree | **CLEAN** |
| test working tree | **DIRTY** (`?? 9`, 무해한 빈 파일 carry) |
| npm test pre-merge (@ develop) | **2046/2046 PASS** (731.51s, 398 files) |
| merge | **EXECUTED** FF `2040571`→`95f55aa` (1 commit) |
| npm test post-merge (@ test) | **2046/2046 PASS** (698.02s, 398 files) |
| build | **1148 modules PASS** (8.29s) |
| npm audit (high+) | **0 vulnerabilities** |
| live E2E | **127 PASS / 19 SKIP** (37.14s) |
| transfer verdict | **PASS** |
| open issue (frontend) | **0** |
| cross-stream | **SYNCED (FE@95f55aa + BE@83a26e7)** |
| operation | **BLOCK** (origin/test push 526 BE+184 FE + QA-B95 partial 19 SKIP) |

## merge commit (QA-B264)

1. `95f55aa` — `fix(v1.2.1/US-R01): wire work-attendance API relatedSurfaces cross-links` — `StaffWorkAttendancePage` + `staffAnnualLeave.js` (+3 tests)

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-23T05:43:13+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-23 1303차)

> **1303차 BLOCK(regression)** — `@2040571` **2042/2043 PASS**(699.21s, 398 files, **1 FAIL** CareServiceSpecialNotesPage) · develop/test **SYNCED** · merge **SKIP**(`test..develop` **0/0**) · build **1148 modules PASS**(8.31s) · audit **0** · live E2E **127 PASS/19 SKIP**(43.38s) · **QA-B262 Open(BLOCK)** · **QA-B261 Fixed**(US-R01 non-repro) · transfer **BLOCK** · cross-stream **BLOCK(FE regression · BE SYNCED@6ab3760)** · operation **BLOCK**

## 1303차 검증 요약 (SYNCED revalidation BLOCK)

| 항목 | 결과 |
|---|---|
| test worktree HEAD | `2040571` |
| develop HEAD | `2040571` |
| ahead (`test..develop`) | **0/0** (SYNCED) |
| delta vs 1302차 | 동일 HEAD · npm FAIL **3→1** (US-R01 19/19 PASS · CareServiceSpecialNotesPage 1 FAIL) |
| develop working tree | **CLEAN** |
| test working tree | **DIRTY** (`?? 9`, 무해한 빈 파일 carry) |
| npm test (@ test) | **2042/2043 PASS** (699.21s, 398 files, **1 FAIL**) |
| US-R01 targeted | **19/19 PASS** (6.87s) |
| merge | **SKIP** (already SYNCED) |
| build | **1148 modules PASS** (8.31s) |
| npm audit (high+) | **0 vulnerabilities** |
| live E2E | **127 PASS / 19 SKIP** (43.38s) |
| transfer verdict | **BLOCK** |
| open issue (frontend) | **1** (QA-B262 BLOCK) |
| cross-stream | **BLOCK (FE regression@2040571 · BE SYNCED@6ab3760)** |
| operation | **BLOCK** (origin/test push 525 BE+183 FE + QA-B262 fix + QA-B95 partial 19 SKIP) |

## failing test (QA-B262)

1. `src/pages/CareServiceSpecialNotesPage.test.jsx` > `creates a new special notes record` — `Value "client-1" not found in options` (client `<select>` disabled·options empty)

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-23T05:02:02+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-23 1302차)

> **1302차 BLOCK(regression)** — `@2040571` **2040/2043 PASS**(696.32s, 398 files, **3 FAIL** US-R01 cross-links) · develop/test **SYNCED** · merge **SKIP**(`test..develop` **0/0**) · build **1148 modules PASS**(9.66s) · audit **0** · live E2E **127 PASS/19 SKIP**(43.95s) · **QA-B261 Open(BLOCK)** · transfer **BLOCK** · cross-stream **BLOCK(FE regression · BE SYNCED@6ab3760)** · operation **BLOCK**

## 1302차 검증 요약 (SYNCED regression BLOCK)

| 항목 | 결과 |
|---|---|
| test worktree HEAD | `2040571` |
| develop HEAD | `2040571` |
| ahead (`test..develop`) | **0/0** (SYNCED) |
| delta vs 1300차 | +1 commit `2040571` (US-R01 reverse HR cross-links) · +3 tests · npm **3 FAIL** |
| develop working tree | **CLEAN** |
| test working tree | **DIRTY** (`?? 9`, 무해한 빈 파일 carry) |
| npm test (@ test) | **2040/2043 PASS** (696.32s, 398 files, **3 FAIL**) |
| merge | **SKIP** (already SYNCED) |
| build | **1148 modules PASS** (9.66s) |
| npm audit (high+) | **0 vulnerabilities** |
| live E2E | **127 PASS / 19 SKIP** (43.95s) |
| transfer verdict | **BLOCK** |
| open issue (frontend) | **1** (QA-B261 BLOCK) |
| cross-stream | **BLOCK (FE regression@2040571 · BE SYNCED@6ab3760)** |
| operation | **BLOCK** (origin/test push 525 BE+183 FE + QA-B261 fix + QA-B95 partial 19 SKIP) |

## commit since 1300차 (0b0d7ba..2040571)

1. `2040571` — feat(v1.2.1/US-R01): add reverse HR cross-links on staff attendance page

## failing tests (QA-B261)

1. `src/pages/StaffWorkAttendancePage.test.jsx` — US-R01 help text not found
2. `src/utils/staffAnnualLeave.test.js` — `STAFF_WORK_ATTENDANCE_DEFAULT_RELATED_SURFACES[0]` undefined
3. `src/components/staff/StaffAnnualLeaveRelatedSurfacesPanel.test.jsx` — work attendance help text not found

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-23T06:00:00+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-23 1304차)

> **1304차 PASS(SYNCED revalidation)** — `@2040571` **2043/2043 PASS**(705.17s, 398 files, +3 tests vs 1300) · develop/test **SYNCED** · merge **SKIP**(`test..develop` **0/0**) · build **1148 modules PASS**(9.38s) · audit **0** · live E2E **127 PASS/19 SKIP**(43.38s carry·1303) · **★ QA-B262 Fixed** · transfer **PASS** · cross-stream **SYNCED(FE@2040571 + BE@6ab3760)** · operation **BLOCK**

## 1304차 검증 요약 (SYNCED revalidation)

| 항목 | 결과 |
|---|---|
| test worktree HEAD | `2040571` |
| develop HEAD | `2040571` |
| ahead (`test..develop`) | **0/0** (SYNCED) |
| delta vs 1300차 | +1 commit `2040571` (US-R01 reverse HR cross-links) · +3 tests |
| develop working tree | **CLEAN** |
| test working tree | **DIRTY** (`?? 9`, 무해한 빈 파일 carry) |
| npm test (@ test) | **2043/2043 PASS** (705.17s, 398 files) |
| merge | **SKIP** (already SYNCED) |
| build | **1148 modules PASS** (9.38s) |
| npm audit (high+) | **0 vulnerabilities** |
| live E2E | **127 PASS / 19 SKIP** (43.38s carry·1303차) |
| transfer verdict | **PASS** |
| open issue (frontend) | **0** |
| cross-stream | **SYNCED (FE@2040571 + BE@6ab3760)** |
| operation | **BLOCK** (origin/test push 525 BE+183 FE + QA-B95 partial 19 SKIP) |

## commit since 1300차 (0b0d7ba..2040571)

1. `2040571` — feat(v1.2.1/US-R01): add reverse HR cross-links on staff attendance page (+3 tests, 6 files)

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-23T03:44:22+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-23 1300차)

> **1300차 PASS(SYNCED revalidation)** — `@0b0d7ba` **2040/2040 PASS**(752.60s, 398 files, +4 tests) · develop/test **SYNCED** · merge **SKIP**(`test..develop` **0/0**) · build **1147 modules PASS**(15.13s) · audit **0** · live E2E **127 PASS/19 SKIP**(36.43s) · transfer **PASS** · cross-stream **SYNCED(FE@0b0d7ba + BE@6ab3760)** · operation **BLOCK**

## 1300차 검증 요약 (SYNCED revalidation)

| 항목 | 결과 |
|---|---|
| test worktree HEAD | `0b0d7ba` |
| develop HEAD | `0b0d7ba` |
| ahead (`test..develop`) | **0/0** (SYNCED) |
| delta vs 1298차 | +1 commit `0b0d7ba` (US-R01 cross-links) · +4 tests · +1 file |
| develop working tree | **CLEAN** |
| test working tree | **DIRTY** (`?? 9`, 무해한 빈 파일 carry) |
| npm test (@ test) | **2040/2040 PASS** (752.60s, 398 files) |
| merge | **SKIP** (already SYNCED) |
| build | **1147 modules PASS** (15.13s) |
| npm audit (high+) | **0 vulnerabilities** |
| live E2E | **127 PASS / 19 SKIP** (36.43s) |
| transfer verdict | **PASS** |
| open issue (frontend) | **0** |
| cross-stream | **SYNCED (FE@0b0d7ba + BE@6ab3760)** |
| operation | **BLOCK** (origin/test push 525 BE+182 FE + QA-B95 partial 19 SKIP) |

## commit since 1298차 (e296387..0b0d7ba)

1. `0b0d7ba` — feat(v1.2.1/G-STAFF-ANNUAL-LEAVE): wire US-R01 related surface cross-links

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-23T02:21:05+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-23 1298차)

> **1298차 PASS(merge EXECUTED)** — baseline `@31ab1aa` **2035/2035 PASS**(712.01s) · develop pre-merge `@e296387` **2036/2036 PASS**(695.20s, +1 test) · ★ merge EXECUTED FF `31ab1aa`→`e296387` (2 commits) · post-merge **2036/2036 PASS** · build **1147 modules PASS**(11.76s) · audit **0** · live E2E **127 PASS/19 SKIP**(36.52s) · **★ QA-20260623-B258 Fixed @ `e296387`** · transfer **PASS** · cross-stream **BLOCK(BE pending 1 @bbf333c)** · operation **BLOCK**

## 1298차 검증 요약 (merge EXECUTED — SYNCED)

| 항목 | 결과 |
|---|---|
| test worktree HEAD (pre-merge) | `31ab1aa` |
| develop HEAD (pre-merge) | `e296387` |
| post-merge HEAD | `e296387` |
| ahead (`test..develop` pre-merge) | **0/2** (`31ab1aa`..`e296387`) |
| develop working tree | **CLEAN** |
| test working tree | **DIRTY** (`?? 9`, 무해한 빈 파일 carry) |
| npm test (baseline @ test) | **2035/2035 PASS** (712.01s, 397 files) |
| npm test (develop pre-merge) | **2036/2036 PASS** (695.20s, 397 files, +1 test) |
| post-merge npm test | **2036/2036 PASS** (carry @ `e296387`) |
| build | **1147 modules PASS** (11.76s) |
| npm audit (high+) | **0 vulnerabilities** |
| live E2E | **127 PASS / 19 SKIP** (36.52s) |
| transfer verdict | **PASS** |
| open issue (frontend) | **0** |
| open issue (backend carry) | **1** (QA-B259) |
| cross-stream | **BLOCK (FE@e296387 SYNCED · BE pending 1 @bbf333c)** |
| operation | **BLOCK** (origin/test push 523 BE+181 FE + QA-B95 partial 19 SKIP) |

## merge commits (31ab1aa..e296387)

1. `96e9d25` — add live API harness and memo field error UX
2. `e296387` — register US-R03e and E05 in pilot checklist
