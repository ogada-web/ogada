<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-20T23:46:25+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-20 1191차)

> **1191차 BLOCK(merge pending 2 · QA-B188 Open update)** — test `@82a542c` develop `@2581347` `npm test` **1901/1901 PASS**(360.72s) · build **1079 modules**(7.88s) · live E2E **SKIP**(merge 미실행 사이클) · merge **SKIP**(`test..develop` **0/2** pending `2581347`+`e45df26`) · develop/test WT **CLEAN** · Open **2(active frontend+backend)**(QA-B188+QA-B187) · cross-stream **BLOCK(FE@2581347 + BE@1d7cee2)** · operation **BLOCK**(origin/test push 478 BE+120 FE+QA-B95 partial)

## 1191차 검증 요약 (merge pending 2 — staff lifecycle + live-e2e token recovery 미이관)

| 항목 | 결과 |
|---|---|
| test worktree HEAD | `82a542c` |
| develop HEAD | `2581347` |
| ahead (`test..develop`) | **0/2** (merge pending) |
| develop working tree | **CLEAN** |
| test working tree | **CLEAN** @ `82a542c` |
| npm test | **1901/1901 PASS** (360.72s, 374 files) |
| build | **1079 modules SUCCESS** (7.88s) |
| live E2E | **SKIP** (merge 미실행 사이클) |
| FE merge status | **PENDING 2** (`2581347`, `e45df26`) |
| BE merge status | **PENDING 2** (`1d7cee2`, `68d4457`) |
| transfer verdict | **BLOCK** |
| cross-stream | **BLOCK** |
| operation | **BLOCK** (QA-B188+QA-B187+origin/test push 478 BE+120 FE + QA-B95 partial) |

### Pending commits (1191차)

- `2581347` — `feat(v1.2.1/G-STAFF-LEAVE-STATUS): wire ON_LEAVE staff lifecycle on frontend`
- `e45df26` — `fix(v2/live-e2e): recover stale staff and guardian tokens in live session`

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-20T23:27:40+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-20 1189차)

> **1189차 BLOCK(merge pending 1 · QA-B188 Open)** — test `@82a542c` develop `@e45df26` `npm test` **1895/1895 PASS**(357.14s) · build **1079 modules**(7.84s) · live E2E **126 PASS/19 SKIP**(30.12s) · merge **SKIP**(`test..develop` **0/1** pending `e45df26`) · develop/test WT **CLEAN** · Open **2(active frontend+backend)**(QA-B188+QA-B187) · cross-stream **BLOCK(FE@e45df26 + BE@68d4457)** · operation **BLOCK**(origin/test push 478 BE+120 FE+QA-B95 partial)

## 1189차 검증 요약 (merge pending — stale token recovery commit 미이관)

| 항목 | 결과 |
|---|---|
| test worktree HEAD | `82a542c` |
| develop HEAD | `e45df26` |
| ahead (`test..develop`) | **0/1** (merge pending) |
| develop working tree | **CLEAN** |
| test working tree | **CLEAN** @ `82a542c` |
| npm test | **1895/1895 PASS** (357.14s, 373 files) |
| build | **1079 modules SUCCESS** (7.84s) |
| live E2E | **126 PASS/19 SKIP** (30.12s) |
| FE merge status | **PENDING 1** (`e45df26`) |
| BE merge status | **PENDING 1** (`68d4457`) |
| transfer verdict | **BLOCK** |
| cross-stream | **BLOCK** |
| operation | **BLOCK** (QA-B188+QA-B187+origin/test push 478 BE+120 FE + QA-B95 partial) |

### Pending commit (1189차)

- `e45df26` — `fix(v2/live-e2e): recover stale staff and guardian tokens in live session`

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-20T22:52:10+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-20 1187차)

> **1187차 PASS(merge EXECUTED · QA-B186 Fixed)** — test `@b60c622` develop `@82a542c` pre-merge `npm test` **1892/1892 PASS**(351.15s) · ★ merge EXECUTED(FF `b60c622`→`82a542c`, 1 commit) · post-merge **1892/1892 PASS**(351.83s) · build **1079 modules**(7.91s) · audit **0** · live E2E **126 PASS/19 SKIP**(QA-B95 partial carry) · develop/test **SYNCED @82a542c** WT **CLEAN** · **★ QA-B186 Fixed** · Open **0(active frontend)** · cross-stream **SYNCED(BE@2edbdc4)** · operation **BLOCK**(origin/test push 478 BE+120 FE+QA-B95 partial)

## 1187차 검증 요약 (merge EXECUTED — live-e2e placeholder auth token bootstrap probing)

| 항목 | 결과 |
|---|---|
| test worktree HEAD (pre-merge) | `b60c622` |
| develop HEAD (pre-merge) | `82a542c` |
| ahead (`test..develop`) | **0/1** → merge EXECUTED |
| develop working tree | **CLEAN** |
| test working tree (post-merge) | **CLEAN** @ `82a542c` |
| npm test (pre-merge) | **1892/1892 PASS** (351.15s, 372 files) |
| npm test (post-merge) | **1892/1892 PASS** (351.83s) |
| build | **1079 modules SUCCESS** (7.91s) |
| audit | **0 vulnerabilities** |
| live E2E | **126 PASS/19 SKIP** (30.56s) |
| FE merge status | **EXECUTED** (1 commit) |
| BE merge status | **SYNCED** @ `2edbdc4` |
| transfer verdict | **PASS** |
| cross-stream | **SYNCED** |
| operation | **BLOCK** (origin/test push 478 BE+120 FE + QA-B95 partial) |

### Merged commit (1187차)

- `82a542c` — `fix(v2/live-e2e): ignore placeholder auth tokens during bootstrap probing` (`liveGlobalSetup.js` + `liveE2eHarness.test.js`)

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-20T22:25:12+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-20 1185차)

> **1185차 PASS(merge EXECUTED · QA-B185 Fixed)** — test `@06c6bb5` develop `@b60c622` pre-merge `npm test` **1890/1890 PASS**(357.32s) · ★ merge EXECUTED(FF `06c6bb5`→`b60c622`, 1 commit) · post-merge **1890/1890 PASS**(358.19s; 1st run `DashboardPage.test.jsx` flake · retry clean) · build **1079 modules**(8.03s) · audit **0** · live E2E **126 PASS/19 SKIP**(QA-B95 partial carry) · develop/test **SYNCED @b60c622** WT **CLEAN** · **★ QA-B185 Fixed** · Open **0(active frontend)** · cross-stream **SYNCED(BE@2edbdc4)** · operation **BLOCK**(origin/test push 478 BE+119 FE+QA-B95 partial)

## 1185차 검증 요약 (merge EXECUTED — live-e2e stale auth token recovery)

| 항목 | 결과 |
|---|---|
| test worktree HEAD (pre-merge) | `06c6bb5` |
| develop HEAD (pre-merge) | `b60c622` |
| ahead (`test..develop`) | **0/1** → merge EXECUTED |
| develop working tree | **CLEAN** |
| test working tree (post-merge) | **CLEAN** @ `b60c622` |
| npm test (pre-merge) | **1890/1890 PASS** (357.32s, 372 files) |
| npm test (post-merge) | **1890/1890 PASS** (358.19s; 1st run 1889/1890 flake) |
| build | **1079 modules SUCCESS** (8.03s) |
| audit | **0 vulnerabilities** |
| live E2E | **126 PASS/19 SKIP** (31.59s) |
| FE merge status | **EXECUTED** (1 commit) |
| BE merge status | **SYNCED** @ `2edbdc4` |
| transfer verdict | **PASS** |
| cross-stream | **SYNCED** |
| operation | **BLOCK** (origin/test push 478 BE+119 FE + QA-B95 partial) |

### Merged commit (1185차)

- `b60c622` — `fix(v2/live-e2e): recover from stale auth tokens` (`liveGlobalSetup.js` + `liveE2eHarness.test.js`)

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-20T21:51:52+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-20 1183차)

> **1183차 PASS(SYNCED revalidation · merge SKIP)** — test `@06c6bb5` develop `@06c6bb5` `npm test` **1888/1888 PASS**(359.79s) · merge **SKIP**(`test..develop` **0/0**) · build **1079 modules**(8.04s) · audit **0** · live E2E **126 PASS/19 SKIP**(QA-B95 partial carry) · develop/test **SYNCED @06c6bb5** WT **CLEAN** · Open **0(active frontend)** · cross-stream **SYNCED(BE@2edbdc4)** · operation **BLOCK**(origin/test push 478 BE+118 FE+QA-B95 partial)

## 1183차 검증 요약 (SYNCED revalidation — live-e2e auth blocker label normalization)

| 항목 | 결과 |
|---|---|
| test worktree HEAD | `06c6bb5` |
| develop HEAD | `06c6bb5` |
| ahead (`test..develop`) | **0/0** SYNCED |
| develop working tree | **CLEAN** |
| test working tree | **CLEAN** @ `06c6bb5` |
| npm test | **1888/1888 PASS** (359.79s, 372 files) |
| build | **1079 modules SUCCESS** (8.04s) |
| audit | **0 vulnerabilities** |
| live E2E | **126 PASS/19 SKIP** (31.66s) |
| FE merge status | **SKIP** (SYNCED) |
| BE merge status | **SYNCED** @ `2edbdc4` |
| transfer verdict | **PASS** |
| cross-stream | **SYNCED** |
| operation | **BLOCK** (origin/test push 478 BE+118 FE + QA-B95 partial) |

### New commit since 1181차

- `06c6bb5` — `fix(v2/live-e2e): normalize auth blocker labels for skip gating` (already on develop+test)

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-20T21:09:21+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-20 1181차)

> **1181차 PASS(merge EXECUTED · QA-B183 Fixed)** — test `@a18b30e` develop `@9105332` pre-merge `npm test` **1887/1887 PASS**(354.05s) · ★ merge EXECUTED(FF `a18b30e`→`9105332`, 2 commits) · post-merge **1887/1887 PASS**(366.28s) · build **1079 modules**(10.90s) · audit **0** · live E2E **126 PASS/19 SKIP**(QA-B95 partial carry) · develop/test **SYNCED @9105332** WT **CLEAN** · **★ QA-B183 Fixed** · Open **0(active frontend)** · cross-stream **SYNCED(BE@6ed7cd4)** · operation **BLOCK**(origin/test push 477 BE+117 FE+QA-B95 partial)

## 1181차 검증 요약 (merge EXECUTED — UXD-146 a11y + live-e2e auth blocker recovery)

| 항목 | 결과 |
|---|---|
| test worktree HEAD (pre-merge) | `a18b30e` |
| develop HEAD | `9105332` |
| ahead (`test..develop`) | **0/2** → merge EXECUTED |
| develop working tree | **CLEAN** |
| test working tree (post-merge) | **CLEAN** @ `9105332` |
| npm test (develop pre-merge) | **1887/1887 PASS** (354.05s, 372 files) |
| npm test (post-merge) | **1887/1887 PASS** (366.28s) |
| build | **1079 modules SUCCESS** (10.90s) |
| audit | **0 vulnerabilities** |
| live E2E | **126 PASS/19 SKIP** (30.58s) |
| FE merge status | **EXECUTED** FF `a18b30e`→`9105332` (2 commits) |
| BE merge status | **SYNCED** @ `6ed7cd4` |
| transfer verdict | **PASS** |
| cross-stream | **SYNCED** |
| operation | **BLOCK** (origin/test push 477 BE+117 FE + QA-B95 partial) |

### Fixed (1181차)

- **QA-20260620-B183** — UXD-146 a11y + live-e2e auth blocker recovery `@9105332` (Fixed · merge EXECUTED)

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-20T20:18:45+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-20 1179차)

> **1179차 PASS(merge EXECUTED · QA-B181 Fixed)** — test `@fffc2c1` develop `@a18b30e` pre-merge `npm test` **1885/1885 PASS**(350.95s develop · 359.45s baseline) · ★ merge EXECUTED(FF `fffc2c1`→`a18b30e`, 1 commit) · post-merge **1885/1885 PASS**(352.64s) · build **1079 modules**(7.87s) · audit **0** · live E2E **145 SKIP/0 PASS**(QA-B95 staff-bootstrap-not-ready) · develop/test **SYNCED @a18b30e** WT **CLEAN** · **★ QA-B181 Fixed** · Open **0(active frontend)** · cross-stream **BLOCK(BE QA-B182)** · operation **BLOCK**(QA-B182+origin/test push 475 BE+115 FE+QA-B95)

## 1179차 검증 요약 (merge EXECUTED — G-BANK-EXCEL-8 FE wire)

| 항목 | 결과 |
|---|---|
| test worktree HEAD (pre-merge) | `fffc2c1` |
| develop HEAD | `a18b30e` |
| ahead (`test..develop`) | **0/1** → merge EXECUTED |
| develop working tree | **CLEAN** |
| test working tree (post-merge) | **CLEAN** @ `a18b30e` |
| npm test (develop pre-merge) | **1885/1885 PASS** (350.95s, 372 files) |
| npm test (test baseline) | **1885/1885 PASS** (359.45s) |
| npm test (post-merge) | **1885/1885 PASS** (352.64s) |
| build | **1079 modules SUCCESS** (7.87s) |
| audit | **0 vulnerabilities** |
| live E2E | **145 SKIP/0 PASS** (staff-bootstrap-not-ready · QA-B95 carry) |
| FE merge status | **EXECUTED** FF `fffc2c1`→`a18b30e` (1 commit) |
| BE merge status | **pending 1** @ `7d29a38` (QA-B182) |
| transfer verdict | **PASS** |
| cross-stream | **BLOCK(BE merge pending 1)** |
| operation | **BLOCK** (QA-B182 + origin/test push 475 BE+115 FE + QA-B95) |

### Fixed (1179차)

- **QA-20260620-B181** — G-BANK-EXCEL-8 FE wire `@a18b30e` (Fixed · merge EXECUTED)

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-20T19:40:02+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-20 1177차)

> **1177차 BLOCK(develop WT DIRTY · WIP unit regression 9 FAIL)** — test `@fffc2c1` develop `@fffc2c1` `npm test` **1876/1885 PASS**(352.85s; WIP included) · test baseline carry **1885/1885** @1175 · merge **SKIP**(`test..develop` **0/0** SYNCED · develop **DIRTY 4M**) · build **1079 modules**(7.87s) · audit **0** · live E2E **SKIP** · Open **1(active)** QA-B181 · operation **BLOCK**(QA-B181+origin/test push 475 BE+114 FE+QA-B95)

## 1177차 검증 요약 (merge SKIP — G-BANK-EXCEL-8 FE wire WIP)

| 항목 | 결과 |
|---|---|
| test worktree HEAD | `fffc2c1` |
| develop HEAD | `fffc2c1` |
| ahead (`test..develop`) | **0/0** SYNCED |
| develop working tree | **DIRTY 4M** (`services.js`·`BankDepositImportPanel*`·`PaymentPage.test.jsx`) |
| test working tree | **CLEAN** |
| npm test (develop WIP) | **1876/1885 PASS** (352.85s, 372 files; **9 FAIL**) |
| npm test (test baseline carry) | **1885/1885 PASS** (@1175차 committed HEAD) |
| build | **1079 modules SUCCESS** (7.87s) |
| audit | **0 vulnerabilities** |
| live E2E | **SKIP** (develop dirty) |
| FE merge status | **SKIP** (SYNCED + dirty) |
| BE merge status | **SYNCED** @ `e3b74a0` |
| transfer verdict | **BLOCK** |
| cross-stream | **BLOCK(FE dirty)** |
| operation | **BLOCK** (QA-B181 + origin/test push 475 BE+114 FE + QA-B95) |

### WIP failures (1177차)

- `BankDepositImportPanel.formats.e2e.test.jsx` — 8 FAIL (missing `fetchBankDepositFormatsApi` vi.mock)
- `pilotPageFlows.test.jsx` — 1 FAIL (`imports bank deposit excel from payment page`)

### Open (1177차)

- **QA-20260620-B181** — G-BANK-EXCEL-8 FE wire WIP dirty-tree + 9 unit FAIL (BLOCK)

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-20T19:16:23+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-20 1175차)

> **1175차 PASS(merge EXECUTED · cross-stream SYNCED)** — test `@4315ee2` develop `@fffc2c1` pre-merge `npm test` **1885/1885 PASS**(366.99s baseline · 371.76s develop) · ★ merge EXECUTED(FF `4315ee2`→`fffc2c1`, 1 commit) · post-merge **1885/1885 PASS**(362.74s) · build **1078 modules**(11.83s) · audit **0** · live E2E **126 PASS/19 SKIP**(33.45s) · develop/test **SYNCED @fffc2c1** WT **CLEAN** · Open **0(active)** · operation **BLOCK**(origin/test push 475 BE+114 FE+QA-B95)

## 1175차 검증 요약 (merge EXECUTED — live-e2e credential gate)

| 항목 | 결과 |
|---|---|
| test worktree HEAD (pre-merge) | `4315ee2` |
| develop HEAD | `fffc2c1` |
| ahead (`test..develop`) | **0/1** → merge EXECUTED |
| develop working tree | **CLEAN** |
| test working tree (post-merge) | **CLEAN** @ `fffc2c1` |
| npm test (pre-merge baseline) | **1885/1885 PASS** (366.99s, 372 files) |
| npm test (pre-merge develop) | **1885/1885 PASS** (371.76s) |
| npm test (post-merge) | **1885/1885 PASS** (362.74s) |
| build | **1078 modules SUCCESS** (11.83s) |
| audit | **0 vulnerabilities** |
| live E2E | **126 PASS/19 SKIP** (33.45s) |
| FE merge status | **EXECUTED** (1 commit) |
| BE merge status | **SYNCED** @ `e3b74a0` |
| transfer verdict | **PASS** |
| cross-stream | **SYNCED** |
| operation | **BLOCK** (origin/test push 475 BE+114 FE + QA-B95) |

### Merged commits (1175차)

- `fffc2c1` — fix(v2/live-e2e): reject placeholder access tokens in credential gates

### Open (1175차)

- _(none)_

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-20T18:36:23+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-20 1173차)

> **1173차 PASS(merge EXECUTED · QA-B179 Fixed · cross-stream SYNCED)** — test `@a0f051d` develop `@4315ee2` pre-merge `npm test` **1883/1883 PASS**(367.44s) · ★ merge EXECUTED(FF `a0f051d`→`4315ee2`, 2 commits) · post-merge **1883/1883 PASS**(367.63s) · build **1078 modules**(7.98s) · audit **0** · live E2E **126 PASS/19 SKIP**(31.37s) · develop/test **SYNCED @4315ee2** WT **CLEAN** · Open **0(active)** · operation **BLOCK**(origin/test push 474 BE+113 FE+QA-B95)

## 1173차 검증 요약 (merge EXECUTED — QA-B179 Fixed)

| 항목 | 결과 |
|---|---|
| test worktree HEAD (pre-merge) | `a0f051d` |
| develop HEAD | `4315ee2` |
| ahead (`test..develop`) | **0/2** → merge EXECUTED |
| develop working tree | **CLEAN** |
| test working tree (post-merge) | **CLEAN** @ `4315ee2` |
| npm test (pre-merge develop) | **1883/1883 PASS** (367.44s, 372 files) |
| npm test (post-merge) | **1883/1883 PASS** (367.63s) |
| build | **1078 modules SUCCESS** (7.98s) |
| audit | **0 vulnerabilities** |
| live E2E | **126 PASS/19 SKIP** (31.37s) |
| FE merge status | **EXECUTED** (2 commits) |
| BE merge status | **SYNCED** @ `2f6f3bc` |
| transfer verdict | **PASS** |
| cross-stream | **SYNCED** |
| operation | **BLOCK** (origin/test push 474 BE+113 FE + QA-B95) |

### Merged commits (1173차)

- `a2f599c` — ux(a11y): G-BILLING-PRIOR-DEPOSIT-GUARD·HQ 듀얼 대시보드 접근성 재점검 (UXD-145)
- `4315ee2` — feat(v2/G-STAFF-NHIS-EXCEL-IMPORT): wire NHIS caregiver import flow on staff page

### Open (1173차)

- _(none — QA-B179 Fixed @ `4315ee2`)_

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-20T18:02:16+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-20 1171차)

> **1171차 BLOCK(develop WT DIRTY 3M+2U · merge SKIP · QA-B179+QA-B180 Open)** — test `@a0f051d` develop `@a2f599c` `npm test` **1883/1883 PASS**(367.10s; WIP 3M+2U included; test baseline carry **1878/1878**) · merge **SKIP**(`test..develop` **0/1** `@a2f599c` + develop dirty) · build **1078 modules**(8.13s) · audit **0** · live E2E **SKIP** · develop WT **DIRTY 3M+2U**(`services.js`·`StaffPage.jsx`·`StaffPage.test.jsx`·`StaffNhisCaregiverImportPanel*`) · test WT **CLEAN** · Open **2(active)** QA-B179(FE)+QA-B180(BE) · operation **BLOCK**

## 1171차 검증 요약 (merge SKIP — QA-B179 Open)

| 항목 | 결과 |
|---|---|
| test worktree HEAD | `a0f051d` |
| develop HEAD | `a2f599c` |
| ahead (`test..develop`) | **0/1** (pending `a2f599c` UXD-145) |
| develop working tree | **DIRTY 3M+2U** (`services.js` · `StaffPage.jsx` · `StaffPage.test.jsx` · `StaffNhisCaregiverImportPanel.jsx` · `StaffNhisCaregiverImportPanel.test.jsx`) |
| test working tree | **CLEAN** |
| npm test (develop path, WIP included) | **1883/1883 PASS** (367.10s, 372 files) |
| npm test (test baseline carry) | **1878/1878 PASS** (@1167차) |
| build | **1078 modules SUCCESS** (8.13s) |
| audit | **0 vulnerabilities** |
| live E2E | **SKIP** (merge 미실행) |
| FE merge status | **SKIP** (dirty + pending 1) |
| BE merge status | **pending 1** @ `b11e29a` (QA-B180) |
| transfer verdict | **BLOCK** |
| cross-stream | **BLOCK(FE dirty+pending 1 · BE merge pending 1)** |
| operation | **BLOCK** (QA-B179 + QA-B180 + origin/test push 472 BE+111 FE + QA-B95) |

### Open (1171차)

- **QA-20260620-B179** (BLOCK, frontend) — develop WT DIRTY 3M+2U G-STAFF-NHIS-EXCEL-IMPORT FE wire WIP + merge pending 1 `@a2f599c`
- **QA-20260620-B180** (BLOCK, backend carry) — backend merge pending 1 `@b11e29a`

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-20T17:34:30+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-20 1169차)

> **1169차 BLOCK(develop WT DIRTY 2M+2U · merge SKIP · QA-B179 Open)** — test `@a0f051d` develop `@a2f599c` `npm test` **1882/1882 PASS**(365.04s; WIP 2M+2U included; test baseline carry **1878/1878**) · merge **SKIP**(`test..develop` **0/1** `@a2f599c` + develop dirty) · build **1079 modules**(7.98s) · audit **0** · live E2E **SKIP** · develop WT **DIRTY 2M+2U**(`services.js`·`StaffPage.jsx`·`StaffNhisCaregiverImportPanel*`) · test WT **CLEAN** · Open **1(active frontend)** QA-B179 · operation **BLOCK**

## 1169차 검증 요약 (merge SKIP — QA-B179 Open)

| 항목 | 결과 |
|---|---|
| test worktree HEAD | `a0f051d` |
| develop HEAD | `a2f599c` |
| ahead (`test..develop`) | **0/1** (pending `a2f599c` UXD-145) |
| develop working tree | **DIRTY 2M+2U** (`services.js` · `StaffPage.jsx` · `StaffNhisCaregiverImportPanel.jsx` · `StaffNhisCaregiverImportPanel.test.jsx`) |
| test working tree | **CLEAN** |
| npm test (develop path, WIP included) | **1882/1882 PASS** (365.04s, 372 files) |
| npm test (test baseline carry) | **1878/1878 PASS** (@1167차) |
| build | **1079 modules SUCCESS** (7.98s) |
| audit | **0 vulnerabilities** |
| live E2E | **SKIP** (merge 미실행) |
| FE merge status | **SKIP** (dirty + pending 1) |
| BE merge status | **SYNCED** @ `3bbfc00` |
| transfer verdict | **BLOCK** |
| cross-stream | **BLOCK(FE dirty+pending 1 · BE SYNCED)** |
| operation | **BLOCK** (QA-B179 + origin/test push 472 BE+111 FE + QA-B95) |

### Open (1169차)

- **QA-20260620-B179** (BLOCK, frontend) — develop WT DIRTY 2M+2U G-STAFF-NHIS-EXCEL-IMPORT FE wire WIP + merge pending 1 `@a2f599c`

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-20T16:27:50+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-20 1167차)

> **1167차 PASS(merge EXECUTED · QA-B177 Fixed · cross-stream BLOCK BE QA-B178)** — pre-merge test `@c1ebaaf` develop `@a0f051d` `npm test` **1878/1878 PASS**(362.07s) · ★ merge **EXECUTED**(FF `c1ebaaf`→`a0f051d`, 2 commits) · post-merge **1878/1878 PASS**(370.27s) · build **1078 modules**(11.30s) · audit **0** · live E2E **126 PASS/19 SKIP**(32.13s) · develop/test `@a0f051d` WT **CLEAN** · `test..develop` **0/0** · Open **0(active frontend)** · operation **BLOCK**(QA-B178 BE + origin/test push 469 BE+111 FE + QA-B95)

## 1167차 검증 요약 (merge EXECUTED — QA-B177 Fixed)

| 항목 | 결과 |
|---|---|
| test worktree HEAD | `a0f051d` |
| develop HEAD | `a0f051d` |
| ahead (`test..develop`) | **0/0 SYNCED** |
| develop working tree | **CLEAN** |
| test working tree | **CLEAN** |
| npm test (pre-merge develop) | **1878/1878 PASS** (362.07s) |
| npm test (post-merge) | **1878/1878 PASS** (370.27s) |
| build | **1078 modules SUCCESS** (11.30s) |
| audit | **0 vulnerabilities** |
| live E2E | **126 PASS/19 SKIP** (32.13s) |
| FE merge status | **EXECUTED** (FF 2 commits: `8e4a496` live-e2e skip diagnostics · `a0f051d` L02_M15 test fix) |
| BE merge status | **BLOCK** (QA-B178 merge pending 1 @ `6f7f145`) |
| transfer verdict | **PASS** |
| cross-stream | **BLOCK(BE merge pending 1 QA-B178)** |
| operation | **BLOCK** (QA-B178 + origin/test push 469 BE+111 FE + QA-B95) |

### Fixed (1167차)

- **QA-20260620-B177** (BLOCK→Fixed, frontend) — `CareServiceSpecialNotesPage.test.jsx` create-flow regression fixed @ `a0f051d`

### Open carry (1167차)

- **QA-20260620-B178** (BLOCK, backend) — develop→test merge pending 1 (G-BANK-EXCEL-8)

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-20T15:18:00+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-20 1163차)

> **1163차 BLOCK(develop WT DIRTY 2M · merge SKIP · QA-B176 Open)** — test `@c1ebaaf` develop `@c1ebaaf` `npm test` **1878/1878 PASS**(361.48s; WIP 2M included·committed HEAD 1876/1876) · merge **SKIP**(`test..develop` **0/0** · develop dirty) · build **1075 modules**(7.91s) · audit **0** · live E2E **126 PASS/19 SKIP** · develop WT **DIRTY 2M**(`liveConfig.js`·`liveE2eHarness.test.js`) · test WT **CLEAN** · Open **1(active frontend)** QA-B176 · operation **BLOCK**

## 1163차 검증 요약 (merge SKIP — QA-B176 Open)

| 항목 | 결과 |
|---|---|
| test worktree HEAD | `c1ebaaf` |
| develop HEAD | `c1ebaaf` |
| ahead (`test..develop`) | **0/0 SYNCED** |
| develop working tree | **DIRTY 2M** (`src/e2e/liveConfig.js` · `src/test/liveE2eHarness.test.js` — live E2E skip diagnostics WIP) |
| test working tree | **CLEAN** |
| npm test (develop path, WIP included) | **1878/1878 PASS** (361.48s) |
| npm test (committed HEAD @1161차) | **1876/1876 PASS** (carry) |
| build | **1075 modules SUCCESS** (7.91s) |
| audit | **0 vulnerabilities** |
| live E2E | **126 PASS/19 SKIP** (31.27s) |
| FE merge status | **SKIP** (SYNCED but develop dirty recurrence) |
| BE merge status | **SYNCED @1283153** |
| transfer verdict | **BLOCK** |
| cross-stream | **SYNCED(FE+BE @ test)** |
| operation | **BLOCK** (QA-B176 + origin/test push 468 BE+109 FE + QA-B95) |

### Open (1163차)

- **QA-20260620-B176** (BLOCK, frontend) — develop WT **DIRTY 2M** live E2E harness skip diagnostics WIP 미커밋

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-20T14:51:16+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-20 1161차)

> **1161차 PASS(merge EXECUTED · QA-B175 Fixed)** — pre-merge test `@0d233b9` develop `@c1ebaaf` `npm test` **1876/1876 PASS**(368.67s) · ★ merge EXECUTED FF `0d233b9`→`c1ebaaf` (2 commits) · post-merge **1876/1876 PASS**(367.60s) · build **1075 modules**(7.88s) · audit **0** · live E2E **126 PASS/19 SKIP** · develop/test **SYNCED @ `c1ebaaf`** · Open **0(active frontend)** · operation **BLOCK**

## 1161차 검증 요약 (merge EXECUTED — QA-B175 Fixed)

| 항목 | 결과 |
|---|---|
| test worktree HEAD | `c1ebaaf` |
| develop HEAD | `c1ebaaf` |
| ahead (`test..develop`) | **0/0 SYNCED** |
| develop working tree | **CLEAN** |
| test working tree | **CLEAN** |
| npm test (pre-merge develop) | **1876/1876 PASS** (368.67s) |
| npm test (post-merge test) | **1876/1876 PASS** (367.60s) |
| build | **1075 modules SUCCESS** (7.88s) |
| audit | **0 vulnerabilities** |
| live E2E | **126 PASS/19 SKIP** (31.42s; QA-B95 seed readiness partial) |
| FE merge status | **EXECUTED** (2 commits) |
| BE merge status | **SYNCED @8b3f66d** |
| transfer verdict | **PASS** |
| cross-stream | **SYNCED(FE+BE)** |
| operation | **BLOCK** (origin/test push 469 BE+109 FE + QA-B95) |

### Fixed (1161차)

- **QA-20260620-B175** (BLOCK, frontend) — develop WT DIRTY `liveDescribe.js` → **`c93e673`** commit + merge EXECUTED · post-merge **1876/1876 PASS**

### merge commits (1161차 · 2)

1. `c93e673` — fix(v1.2.1/live-e2e): gate live suites on operation readiness (QA-B175)
2. `c1ebaaf` — feat(v1.2.1/US-H01): add HQ branch drill-down and dual dashboard nav

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-20T14:18:00+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-20 1159차)

> **1159차 BLOCK(develop WT DIRTY 1M · merge SKIP · QA-B175 Open)** — test `@0d233b9` develop `@0d233b9` `npm test` **1869/1869 PASS**(363.85s) · merge **SKIP**(`test..develop` **0/0** · develop dirty) · build **1075 modules**(12.08s) · audit **0** · live E2E **126 PASS/19 SKIP** · develop WT **DIRTY 1M**(`liveDescribe.js`) · test WT **CLEAN** · Open **1(active frontend)** QA-B175 · operation **BLOCK**

## 1159차 검증 요약 (merge SKIP — QA-B175 Open)

| 항목 | 결과 |
|---|---|
| test worktree HEAD | `0d233b9` |
| develop HEAD | `0d233b9` |
| ahead (`test..develop`) | **0/0 SYNCED** |
| develop working tree | **DIRTY 1M** (`src/e2e/liveDescribe.js` — QA-B95 `requireOperationReady` gate WIP) |
| test working tree | **CLEAN** |
| npm test (test baseline) | **1869/1869 PASS** (363.85s) |
| build | **1075 modules SUCCESS** (12.08s) |
| audit | **0 vulnerabilities** |
| live E2E | **126 PASS/19 SKIP** (36.15s; develop path WIP may affect gating) |
| FE merge status | **SKIP** (SYNCED but develop dirty recurrence) |
| BE merge status | **SYNCED @1134b2d** |
| transfer verdict | **BLOCK** |
| cross-stream | **SYNCED(FE+BE @ test)** |
| operation | **BLOCK** (QA-B175 + origin/test push 466 BE+107 FE + QA-B95) |

### Open (1159차)

- **QA-20260620-B175** (BLOCK, frontend) — develop WT **DIRTY 1M** `liveDescribe.js` QA-B95 operation-readiness gate WIP 미커밋

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-20T13:42:00+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-20 1157차)

> **1157차 PASS(merge EXECUTED · QA-B174 Fixed)** — pre-merge test `@d723d5a` develop `@0d233b9` `npm test` **1869/1869 PASS**(368.72s) · ★ merge EXECUTED FF `d723d5a`→`0d233b9` (2 commits) · post-merge **1869/1869 PASS**(357.05s) · build **1075 modules**(8.33s) · audit **0** · live E2E **122 PASS/23 SKIP** · develop/test **SYNCED @ `0d233b9`** · Open **0(active frontend)** · operation **BLOCK**

## 1157차 검증 요약 (merge EXECUTED — QA-B174 Fixed)

| 항목 | 결과 |
|---|---|
| test worktree HEAD | `0d233b9` |
| develop HEAD | `0d233b9` |
| ahead (`test..develop`) | **0/0 SYNCED** |
| develop working tree | **CLEAN** |
| test working tree | **CLEAN** |
| npm test (pre-merge develop) | **1869/1869 PASS** (368.72s) |
| npm test (post-merge test) | **1869/1869 PASS** (357.05s) |
| build | **1075 modules SUCCESS** (8.33s) |
| audit | **0 vulnerabilities** |
| live E2E | **122 PASS/23 SKIP** (QA-B95 seed readiness partial) |
| FE merge status | **EXECUTED** (2 commits) |
| BE merge status | **SYNCED @07a03c0** |
| transfer verdict | **PASS** |
| cross-stream | **SYNCED(FE+BE)** |
| operation | **BLOCK** (origin/test push 465 BE+107 FE + QA-B95) |

### Fixed (1157차)

- **QA-20260620-B174** (BLOCK, frontend) — merge pending 2 (UXD-144 + G-BILLING-PRIOR-DEPOSIT-GUARD FE widget) → merge EXECUTED · post-merge **1869/1869 PASS**

### merge commits (1157차 · 2)

1. `08a8b9f` — ux(a11y): G14 급여제공계획서·직원 계정 요청 UI 접근성 재점검 (UXD-144)
2. `0d233b9` — feat(v1.2.1/G-BILLING-PRIOR-DEPOSIT-GUARD): wire dashboard prior-deposit guard widget

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-20T12:38:00+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-20 1155차)

> **1155차 PASS(merge EXECUTED · QA-B172 Fixed)** — pre-merge test `@c37228d` `npm test` **1866/1866 PASS**(360.73s) · ★ merge EXECUTED FF `c37228d`→`d723d5a` (2 commits) · post-merge **1866/1866 PASS**(360.94s) · build **1075 modules**(8.05s) · audit **0** · live E2E **122 PASS/23 SKIP** · develop/test **SYNCED @ `d723d5a`** · Open **0(active frontend)** · operation **BLOCK**

## 1155차 검증 요약 (merge EXECUTED — QA-B172 Fixed)

| 항목 | 결과 |
|---|---|
| test worktree HEAD | `d723d5a` |
| develop HEAD | `d723d5a` |
| ahead (`test..develop`) | **0/0 SYNCED** |
| develop working tree | **CLEAN** |
| test working tree | **CLEAN** |
| npm test (pre-merge test) | **1866/1866 PASS** (360.73s) |
| npm test (post-merge test) | **1866/1866 PASS** (360.94s) |
| build | **1075 modules SUCCESS** (8.05s) |
| audit | **0 vulnerabilities** |
| live E2E | **122 PASS/23 SKIP** (QA-B95 seed readiness partial) |
| FE merge status | **EXECUTED** (2 commits) |
| BE merge status | **SYNCED @80b9619** |
| transfer verdict | **PASS** |
| cross-stream | **SYNCED(FE+BE)** |
| operation | **BLOCK** (origin/test push 464 BE+105 FE + QA-B95) |

### Fixed (1155차)

- **QA-20260620-B172** (BLOCK, frontend) — develop WT DIRTY 2M + merge pending → COD commit `@d723d5a` → merge EXECUTED · post-merge **1866/1866 PASS**

### merge commits (1155차 · 2)

1. `ce422e3` — feat(v1.2.1/G14): wire NHIS 10-field care plan form UI
2. `d723d5a` — fix(v1.2.1): wire branch switcher auth and design token layout (QA-B172)

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-20T12:06:30+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-20 1153차)

> **1153차 BLOCK(develop WT DIRTY · merge SKIP · QA-B172 Open)** — develop `@ce422e3` `npm test` **1866/1866 PASS**(357.01s) · develop WT **DIRTY 2M**(`components.css`·`tokens.css`) · test `@c37228d` · `test..develop` **0/1** · merge **SKIP** · build **1072 modules**(7.78s) · audit **0** · live E2E **SKIP** · Open **1(active frontend)** QA-B172 · cross-stream **BLOCK(B171+B172)** · operation **BLOCK**

## 1153차 검증 요약 (merge SKIP — QA-B172 Open)

| 항목 | 결과 |
|---|---|
| test worktree HEAD | `c37228d` |
| develop HEAD | `ce422e3` |
| ahead (`test..develop`) | **0/1** (pending `ce422e3`) |
| develop working tree | **DIRTY 2M** (`components.css`·`tokens.css`) |
| test working tree | **CLEAN** |
| npm test (develop HEAD+WT) | **1866/1866 PASS** (357.01s) |
| build | **1072 modules SUCCESS** (7.78s) |
| audit | **0 vulnerabilities** |
| live E2E | **SKIP** (merge 미실행) |
| FE merge status | **SKIP** (dirty-tree + pending 1) |
| BE merge status | **BLOCK** QA-B171 carry |
| transfer verdict | **BLOCK** |
| cross-stream | **BLOCK(BE B171 + FE B172)** |
| operation | **BLOCK** (QA-B171+QA-B172+origin/test push 461 BE+103 FE+QA-B95) |

### Open (1153차)

- **QA-20260620-B172** (BLOCK, frontend) — develop WT **DIRTY 2M** UXD token WIP + merge pending 1 `@ce422e3` G14 care plan UI

### pending merge commit (1153차 · 1)

1. `ce422e3` — feat(v1.2.1/G14): wire NHIS 10-field care plan form UI

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-20T11:17:49+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-20 1149차)

> **1149차 PASS(merge EXECUTED · QA-B170 Fixed)** — pre-merge develop `@c37228d` `npm test` **1858/1858 PASS**(357.57s) · ★ merge EXECUTED FF `acc5933`→`c37228d` (6 commits) · post-merge **1858/1858 PASS**(353.45s) · build **1068 modules**(11.51s) · audit **0** · live E2E **122 PASS/23 SKIP** · develop/test **SYNCED @ `c37228d`** · Open **0(active frontend)** · operation **BLOCK**

## 1149차 검증 요약 (merge EXECUTED — QA-B170 Fixed)

| 항목 | 결과 |
|---|---|
| test worktree HEAD | `c37228d` |
| develop HEAD | `c37228d` |
| ahead (`test..develop`) | **0/0 SYNCED** |
| develop working tree | **CLEAN** |
| test working tree | **CLEAN** |
| npm test (pre-merge develop) | **1858/1858 PASS** (357.57s) |
| npm test (post-merge test) | **1858/1858 PASS** (353.45s) |
| build | **1068 modules SUCCESS** (11.51s) |
| audit | **0 vulnerabilities** |
| live E2E | **122 PASS/23 SKIP** (QA-B95 seed readiness partial) |
| FE merge status | **EXECUTED** (6 commits) |
| BE merge status | **SYNCED @483f657** (carry) |
| transfer verdict | **PASS** |
| cross-stream | **SYNCED(FE+BE)** |
| operation | **BLOCK** (origin/test push 461 BE+103 FE + QA-B95) |

### Fixed (1149차)

- **QA-20260620-B170** (BLOCK, frontend) — post-merge `@acc5933` 5 FAIL → merge EXECUTED · post-merge **1858/1858 PASS** @ `c37228d`

### merge commits (1149차 · 6)

1. `ba74bb5` — fix(transport): commit Kakao map WIP and resolve QA-B167/B170 regressions
2. `4d87e19` — ux(a11y): v1.3-A transport dispatch tool external link a11y (UXD-143)
3. `22718d0` — fix: align staff account requests and stabilize qa-b170 tests
4. `380be3c` — feat: require platform admin name and password on issuance
5. `8ac0d01` — feat(branches): require road address and improve region selector UX
6. `c37228d` — test(branches): guard empty road address on branch create

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-20T10:40:40+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-20 1147차)

> **1147차 BLOCK(test branch merge pending 5 + QA-B170 carry)** — `src/frontend-test` `npm test` locked wrapper **1857/1857 PASS**(366 files, 360.85s; RUN `/home/ubuntu/ogada/src/frontend`) · `npm run build` **1068 modules**(7.91s) · `npm audit` **0** · FE develop WT **CLEAN** @ `8ac0d01` · FE `test..develop` **0/5**(`test @acc5933`) · Open **QA-B170(FE)** · operation **BLOCK**

## 1147차 검증 요약 (merge SKIP — QA-B170 carry)

| 항목 | 결과 |
|---|---|
| test worktree HEAD | `acc5933` |
| develop HEAD | `8ac0d01` |
| ahead (`test..develop`) | **0/5** |
| develop working tree | **CLEAN** |
| test working tree | **CLEAN** |
| npm test (`src/frontend-test`) | **1857/1857 PASS** (실행 경로: `/home/ubuntu/ogada/src/frontend`) |
| build | **1068 modules SUCCESS** (7.91s) |
| audit | **0 vulnerabilities** |
| live E2E | **SKIP** (merge 미실행) |
| FE merge status | **SKIP** (pending 5 + QA-B170 carry) |
| BE merge status | **EXECUTED @5e1b656** (carry) |
| transfer verdict | **BLOCK** |
| cross-stream | **BLOCK(FE B170)** |
| operation | **BLOCK** (QA-B170 + origin/test push 460 BE+97 FE + QA-B95) |

### Open QA (1147차)

- **QA-20260620-B170** (BLOCK, frontend) — test branch post-merge FAIL 이력 해소 확인 전(merge pending 5)

### Fixed (1147차)

- 신규 fixed 없음 (carry only)

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-20T09:12:00+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-20 1143차)

> **1143차 BLOCK(test branch post-merge FAIL 잔존 + backend dirty)** — `src/frontend-test` `npm test` 실행 결과 locked wrapper가 `src/frontend`(develop `@ba74bb5`)에서 수행되어 **1856/1856 PASS**(366 files, 361.91s) · `npm run build` **1068 modules**(8.33s) · `npm audit` **0** · FE develop WT **CLEAN**(**QA-B167 Fixed**) · FE `test..develop` **0/1**(`test @acc5933`) · Open **QA-B170(FE)+QA-B169(BE)** · operation **BLOCK**

## 1143차 검증 요약 (merge SKIP — QA-B170 + QA-B169)

| 항목 | 결과 |
|---|---|
| test worktree HEAD | `acc5933` |
| develop HEAD | `ba74bb5` |
| ahead (`test..develop`) | **0/1** (`ba74bb5`) |
| develop working tree | **CLEAN** |
| test working tree | **CLEAN** |
| npm test (`src/frontend-test`) | **1856/1856 PASS** (실행 경로: `/home/ubuntu/ogada/src/frontend`) |
| build | **1068 modules SUCCESS** (8.33s) |
| audit | **0 vulnerabilities** |
| live E2E | **SKIP** (merge 미실행) |
| FE merge status | **SKIP** (test `@acc5933` post-merge FAIL 이슈 QA-B170 잔존) |
| BE merge status | **SKIP** (`test..develop` 0/1 + develop WT DIRTY 9M+4U, QA-B169) |
| transfer verdict | **BLOCK** |
| cross-stream | **BLOCK(FE B170 + BE B169)** |
| operation | **BLOCK** (QA-B170+QA-B169+push 456 BE+97 FE+QA-B95) |

### Open QA (1143차)

- **QA-20260620-B170** (BLOCK, frontend) — post-merge `@acc5933` unit regression 5 FAIL 미해소
- **QA-20260620-B169** (BLOCK, backend) — develop WT **DIRTY 9M+4U** + merge pending 1

### Fixed (1143차)

- **QA-20260620-B167** — frontend develop WT DIRTY recurrence **해소** (`@ba74bb5` CLEAN)

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-20T08:25:03+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-20 1141차)

> **1141차 BLOCK(post-merge unit FAIL + develop WT DIRTY)** — pre-merge test `@debe6dd` vitest **1833/1833 PASS**(363 files, 429.10s) · ★ **merge EXECUTED** FF `debe6dd`→`acc5933` (7 commits) · post-merge `@acc5933` vitest **1847/1852 FAIL**(365 files, 486.96s; 5 FAIL) · **★ QA-B168 Fixed**(`pilotPageFlows` 146/146) · develop WT **DIRTY 10M+2U** · build **1069 modules**(13.17s) · audit **0** · live E2E **SKIP** · Open **QA-B167+QA-B170(FE)+QA-B169(BE)** · operation **BLOCK**

## 1141차 검증 요약 (merge EXECUTED — QA-B170 post-merge FAIL)

| 항목 | 결과 |
|---|---|
| pre-merge test HEAD | `debe6dd` |
| develop HEAD | `acc5933` |
| post-merge test HEAD | `acc5933` |
| ahead (`test..develop`) | **0/0 SYNCED** |
| develop working tree | **DIRTY 10M+2U** (Kakao map import WIP · QA-B167) |
| test working tree | **CLEAN** |
| pre-merge vitest | **1833/1833 PASS** @ `debe6dd` (429.10s, 363 files) |
| post-merge vitest | **1847/1852 FAIL** @ `acc5933` (486.96s, 365 files; 5 FAIL) |
| merge | **EXECUTED** FF (7 commits) |
| build | **1069 modules SUCCESS** (13.17s) |
| audit | **0 vulnerabilities** |
| live E2E | **SKIP** (post-merge unit FAIL) |
| Maven | N/A |
| FE merge status | **EXECUTED** · post-merge **BLOCK(QA-B170)** |
| BE merge status | **SYNCED** @ `48eea95` (develop WT DIRTY 7M — QA-B169) |
| transfer verdict | **BLOCK(post-merge FAIL + develop dirty)** |
| cross-stream | **BLOCK(FE B167+B170 + BE B169)** |
| operation | **BLOCK** (push 456 BE+97 FE+QA-B95) |

### 실패 상세 (post-merge @acc5933)

| 테스트 | 파일 | 증상 |
|---|---|---|
| 4× KakaoTransportMap | `src/components/transport/KakaoTransportMap.test.jsx` | `ReferenceError: Alert is not defined` / `KakaoTransportMapView is not defined` — committed HEAD import 누락 |
| `loads hospital visit report` | `src/pages/CareNursingServiceReportPage.test.jsx` | `서울내과` text not found |

### Open QA (1141차)

- **QA-20260620-B167** (BLOCK, frontend) — develop WT **DIRTY 10M+2U** (Kakao map WIP uncommitted)
- **QA-20260620-B170** (BLOCK, frontend) — post-merge **1847/1852 FAIL** @ committed `@acc5933`
- **QA-20260620-B169** (BLOCK, backend) — develop WT **DIRTY 7M** (`TransportSuggestService` WIP)

### Fixed (1141차)

- **QA-20260620-B168** — `pilotPageFlows` **146/146 PASS** @ `acc5933`

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-20T07:31:34+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-20 1139차)

> **1139차 BLOCK(develop merge gate 2 FAIL + develop WT DIRTY + merge pending 6)** — pre-merge test `@debe6dd` **carry 1844/1844 PASS**(1136차) · develop HEAD `@863b135` `npm test` **1848/1850 PASS**(365 files, 414.54s; 2 FAIL `pilotPageFlows.test.jsx` G30·G39) · merge **SKIP**(`test..develop` 0/6) · develop WT **DIRTY 10M+2U** · build **1069 modules**(10.09s) · audit **0** · live E2E **SKIP** · Open **QA-B167+QA-B168(FE)+QA-B169(BE)** · cross-stream **BLOCK** · operation **BLOCK**

## 1139차 검증 요약 (merge SKIP — QA-B167+QA-B168)

| 항목 | 결과 |
|---|---|
| pre-merge test HEAD | `debe6dd` |
| develop HEAD | `863b135` |
| ahead (`test..develop`) | **0 ahead / 6 behind** (`033b319` · `16afd4c` · `bd6e1c2` · `94f2535` · `4681b5a` · `863b135`) |
| develop working tree | **DIRTY 10M+2U** (transport map/geocoder v1.3-A WIP) |
| test working tree | **CLEAN** |
| pre-merge npm test | **carry 1844/1844 PASS** @ `debe6dd` (1136차, merge 미실행) |
| develop npm test | **1848/1850 PASS** @ `863b135` (414.54s, 365 files; 2 FAIL) |
| isolated pilotPageFlows rerun | **144/146 PASS** (2 FAIL reproduced) |
| post-merge npm test | **SKIP** (merge 미실행) |
| build | **1069 modules SUCCESS** (`src/frontend`, 10.09s) |
| audit | **0 vulnerabilities** |
| live E2E | **SKIP** (merge 미실행 사이클) |
| Maven | N/A (`pom.xml` 없음) |
| FE merge status | **SKIP** (develop merge gate 2 FAIL + WT DIRTY) |
| BE merge status | **SYNCED** @ `48eea95` (develop WT DIRTY 4M — QA-B169) |
| transfer verdict | **BLOCK(merge gate 2 FAIL + develop WT DIRTY + merge pending 6)** |
| cross-stream | **BLOCK(FE B167+B168 + BE B169)** |
| operation | **BLOCK** (QA-B167+QA-B168+QA-B169+push 456 BE+90 FE+QA-B95) |

### 실패 상세 (develop HEAD)

| 테스트 | 파일 | 증상 |
|---|---|---|
| `renders G30 integrated monitoring checklist page (BNK-183)` | `src/pages/pilotPageFlows.test.jsx` | `waitFor` timeout — `주간 상태변화 미기록` 미표시 |
| `shows G39 provision result compliance widgets on dashboard (BNK-107)` | `src/pages/pilotPageFlows.test.jsx` | `waitFor` timeout — `월간 기록지 미제공` 미표시 |

### Open QA (1139차)

- **QA-20260620-B167** (BLOCK, frontend) — develop WT **DIRTY 10M+2U** recurrence (transport v1.3-A WIP)
- **QA-20260620-B168** (BLOCK, frontend) — `pilotPageFlows` G30·G39 unit regression 2 FAIL (confirmed full-suite 1139차)
- **QA-20260620-B169** (BLOCK, backend) — develop WT **DIRTY 4M** after SYNCED merge (`TransportSuggestService` WIP)

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-20T07:24:44+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-20 1138차)

> **1138차 BLOCK(vitest terminated + develop WT DIRTY + merge pending 6)** — `src/frontend-test` `npm test`(locked wrapper) **Terminated** after partial run on develop workspace (`RUN v4.1.8 /home/ubuntu/ogada/src/frontend`) with observed 2 FAIL in `pilotPageFlows`(G30/G39) · isolated retry stale-lock Exit 75 then `vitest-stop.sh` cleanup but rerun also **Terminated** · FE develop `@863b135` WT **DIRTY 9M+1U** · `test..develop` **0/6** · build **1066 modules** · audit **0** · live E2E **SKIP** · Open **QA-B167+QA-B168** · cross-stream **BLOCK** · operation **BLOCK**

## 1138차 검증 요약 (merge SKIP — QA-B167+QA-B168)

| 항목 | 결과 |
|---|---|
| pre-merge test HEAD | `debe6dd` |
| develop HEAD | `863b135` |
| ahead (`test..develop`) | **0 ahead / 6 behind** |
| develop working tree | **DIRTY 9M+1U** (transport map/geocoder WIP) |
| test working tree | **CLEAN** |
| pre-merge npm test | **Terminated** @ locked wrapper (partial run에서 `pilotPageFlows` 2 FAIL 관측 후 Exit 143, ~302.64s) |
| isolated npm test | lock Exit 75 → `vitest-stop.sh` 후 재실행 **Terminated** (~28.19s) |
| post-merge npm test | **SKIP** (merge 미실행) |
| build | **1066 modules SUCCESS** (`src/frontend-test`, 12.06s) |
| audit | **0 vulnerabilities** |
| live E2E | **SKIP** (merge 미실행 사이클) |
| Maven | N/A (`pom.xml` 없음) |
| FE merge status | **SKIP** (develop WT DIRTY + 회귀 확정 불가) |
| BE merge status | **SYNCED** @ `48eea95` |
| transfer verdict | **BLOCK(vitest terminated + develop WT DIRTY + merge pending 6)** |
| cross-stream | **BLOCK(FE B167+B168)** |
| operation | **BLOCK** (QA-B167+QA-B168+push 456 BE+90 FE+QA-B95) |

### Open QA (1138차)

- **QA-20260620-B167** (BLOCK, frontend) — develop WT **DIRTY 9M+1U** recurrence
- **QA-20260620-B168** (BLOCK, frontend) — `npm test` 비정상 종료 + `pilotPageFlows` G30/G39 2 FAIL 관측

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-20T06:47:37+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-20 1136차)

> **1136차 BLOCK(develop WT DIRTY + merge pending 4)** — pre-merge test `@debe6dd` **1844/1844 PASS** (388.21s) · develop HEAD `@94f2535` **1844/1844 PASS** (498.67s) · **★ QA-B163 Fixed verified @ `94f2535`** · develop WT **DIRTY 11M+2U** (+492/-105) · merge **SKIP** (`test..develop` 0/4) · build **1066/1069 modules** · audit **0** · live E2E **SKIP** · Open **QA-B165(FE)+QA-B166(BE)** · cross-stream **BLOCK** · operation **BLOCK**

## 1136차 검증 요약 (merge SKIP — QA-B165 develop WT DIRTY)

| 항목 | 결과 |
|---|---|
| pre-merge test HEAD | `debe6dd` |
| develop HEAD | `94f2535` |
| ahead (`test..develop`) | **0 ahead / 4 behind** (`033b319` · `16afd4c` · `bd6e1c2` · `94f2535`) |
| develop working tree | **DIRTY 11M+2U** (SideNav·transport roster/modals·map ETAs·staff renewal WIP) |
| test working tree | **CLEAN** |
| pre-merge npm test | **1844/1844 PASS** @ `debe6dd` (388.21s, 364 files) |
| develop npm test | **1844/1844 PASS** @ `94f2535` (498.67s, 364 files) |
| post-merge npm test | **SKIP** (merge 미실행) |
| build | **1066 modules** @ test (8.28s) · **1069 modules** @ develop (8.12s) |
| audit | **0 vulnerabilities** |
| live E2E | **SKIP** (merge 미실행 사이클) |
| Maven | N/A (`pom.xml` 없음) |
| FE merge status | **SKIP** (develop WT DIRTY QA-B165) |
| BE merge status | **SKIP** (merge pending 1 · QA-B166 @ `cfce0b4`) |
| transfer verdict | **BLOCK(develop WT DIRTY + merge pending 4)** |
| cross-stream | **BLOCK(BE B166 + FE B165)** |
| operation | **BLOCK** (QA-B166+QA-B165+push 454 BE+90 FE+QA-B95) |

### Open QA (1136차)

- **QA-20260620-B163** — **Fixed verified @ `94f2535`** (1844/1844 PASS · isolated panel **2/2 PASS**)
- **QA-20260620-B165** (BLOCK, frontend) — develop WT **DIRTY 11M+2U**
- **QA-20260620-B166** (BLOCK, backend) — merge pending 1 @ `cfce0b4`

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-20T06:33:23+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-20 1134차)

> **1134차 BLOCK(develop WT DIRTY + merge pending 4)** — pre-merge test `@debe6dd` **1833/1833 PASS** (carry) · develop HEAD `@94f2535` **1840/1840 PASS** (360.45s) · **★ QA-B163 Fixed @ `94f2535`** · develop WT **DIRTY 9M+2U** · merge **SKIP** (`test..develop` 0/4) · build **1069 modules** (16.65s) · audit **0** · live E2E **SKIP** · Open **QA-B165(FE)+QA-B164(BE)** · cross-stream **BLOCK** · operation **BLOCK**

## 1134차 검증 요약 (merge SKIP — QA-B165 develop WT DIRTY)

| 항목 | 결과 |
|---|---|
| pre-merge test HEAD | `debe6dd` (carry 1131차) |
| develop HEAD | `94f2535` |
| ahead (`test..develop`) | **0 ahead / 4 behind** (`033b319` · `16afd4c` · `bd6e1c2` · `94f2535`) |
| develop working tree | **DIRTY 9M+2U** (transport·staff renewal WIP) |
| test working tree | **CLEAN** |
| pre-merge npm test | **1833/1833 PASS** @ `debe6dd` (carry) |
| develop npm test | **1840/1840 PASS** @ `94f2535` (360.45s, 364 files) |
| post-merge npm test | **SKIP** (merge 미실행) |
| build | **1069 modules SUCCESS** (16.65s) |
| audit | **0 vulnerabilities** |
| live E2E | **SKIP** (merge 미실행 사이클) |
| Maven | N/A (`pom.xml` 없음) |
| FE merge status | **SKIP** (develop WT DIRTY QA-B165) |
| BE merge status | **SYNCED** @ `520f10a` (develop WT DIRTY QA-B164 carry) |
| transfer verdict | **BLOCK(develop WT DIRTY + merge pending 4)** |
| cross-stream | **BLOCK(BE B164 + FE B165)** |
| operation | **BLOCK** (QA-B165+QA-B164+push 454 BE+90 FE+QA-B95) |

### Pending commits (1134차 — 미이관)

- `033b319` — `feat(v1.2.1/US-R03): add FAQ21823 contract renewal record and due alerts`
- `16afd4c` — `fix(v2/live-e2e): honor legacy G21 seed readiness fields`
- `bd6e1c2` — `ux(a11y): FAQ21823 renewal alerts·CRUD·checklist CSS 승격 (UXD-142)`
- `94f2535` — `fix(v1.2.1/US-R03): align renewal summary panel tests with lifecycle deep-link`

### Open QA (1134차)

- **QA-20260620-B163** — **Fixed @ `94f2535`** (panel test 2 FAIL → 1840/1840 PASS)
- **QA-20260620-B165** (BLOCK, frontend) — develop WT **DIRTY 9M+2U** transport roster/modals·map ETAs·staff renewal copy WIP
- **QA-20260620-B164** (BLOCK, backend carry) — develop WT **DIRTY 8M** live-e2e + transport suggest WIP

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-20T05:54:00+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-20 1131차)

> **1131차 BLOCK(develop merge gate)** — pre-merge test `@debe6dd` **1833/1833 PASS** (carry) · develop `@16afd4c` **1838/1840 PASS** (352.11s; 2 FAIL `StaffEmploymentContractRenewalSummaryPanel.test.jsx`) · merge **SKIP** (`test..develop` 0/2) · build **1067 modules** (8.66s) · audit **0** · live E2E **SKIP** · Open **1(active frontend)** QA-B163 · cross-stream **BLOCK(FE merge gate · BE SYNCED @bfad37d)** · operation **BLOCK**

## 1131차 검증 요약 (merge SKIP — QA-B163 @ `16afd4c`)

| 항목 | 결과 |
|---|---|
| pre-merge test HEAD | `debe6dd` (carry 1127차) |
| develop HEAD | `16afd4c` |
| ahead (`test..develop`) | **0 ahead / 2 behind** (`033b319` · `16afd4c`) |
| develop working tree | **CLEAN** |
| test working tree | **CLEAN** |
| pre-merge npm test | **1833/1833 PASS** @ `debe6dd` (carry) |
| develop npm test | **1838/1840 PASS** @ `16afd4c` (352.11s, 364 files; **2 FAIL**) |
| post-merge npm test | **SKIP** (merge 미실행) |
| build | **1067 modules SUCCESS** (8.66s) |
| audit | **0 vulnerabilities** |
| live E2E | **SKIP** (merge 미실행 사이클) |
| Maven | N/A (`pom.xml` 없음) |
| FE merge status | **SKIP** (develop merge gate BLOCK) |
| BE merge status | **SYNCED** @ `bfad37d` |
| transfer verdict | **BLOCK(develop merge gate)** |
| cross-stream | **BLOCK(FE merge gate · BE SYNCED)** |
| operation | **BLOCK** (QA-B163 + origin/test push 453 BE+90 FE + QA-B95) |

### Pending commits (1131차 — 미이관)

- `033b319` — `feat(v1.2.1/US-R03): add FAQ21823 contract renewal record and due alerts`
- `16afd4c` — `fix(v2/live-e2e): honor legacy G21 seed readiness fields`

### Open QA (1131차)

- **QA-20260620-B163** (BLOCK) — `StaffEmploymentContractRenewalSummaryPanel.test.jsx` 2 FAIL: lifecycle Link `href` `/staff/u-overdue?tab=lifecycle` vs test expectation; terminated-staff render without Router wrapper

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-20T05:25:00+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-20 1127차)

> **1127차 PASS(@test post-merge SYNCED)** — pre-merge test `@1b6d2b1` **1833/1833 PASS** (337.94s) · develop `@debe6dd` **1833/1833 PASS** (337.64s) · ★ merge FF `1b6d2b1`→`debe6dd` (1 commit UXD-141) · post-merge **1833/1833 PASS** (341.15s) · build **1066 modules** (8.42s) · audit **0** · live E2E **126 PASS/19 SKIP** (83.31s) · Open **0(active frontend)** · cross-stream **SYNCED(FE+BE)** · operation **BLOCK**

## 1127차 검증 요약 (merge EXECUTED — UXD-141 @ `debe6dd`)

| 항목 | 결과 |
|---|---|
| pre-merge test HEAD | `1b6d2b1` |
| develop HEAD | `debe6dd` |
| ahead (`test..develop`) | **0 ahead / 1 behind** → merge 후 **0/0 SYNCED** |
| develop working tree | **CLEAN** |
| test working tree | **CLEAN** |
| pre-merge npm test | **1833/1833 PASS** @ `1b6d2b1` (337.94s, 363 files) |
| develop npm test | **1833/1833 PASS** @ `debe6dd` (337.64s, 363 files) |
| post-merge npm test | **1833/1833 PASS** @ `debe6dd` (341.15s, 363 files) |
| build | **1066 modules SUCCESS** (8.42s) |
| audit | **0 vulnerabilities** |
| live E2E | **126 PASS/19 SKIP/0 FAIL** (83.31s) |
| Maven | N/A (`pom.xml` 없음) |
| FE merge status | **EXECUTED** (FF `1b6d2b1`→`debe6dd`, 1 commit) |
| BE merge status | **SYNCED** @ `091c372` |
| transfer verdict | **PASS(@test post-merge SYNCED)** |
| cross-stream | **SYNCED(FE@debe6dd + BE@091c372)** |
| operation | **BLOCK** (origin/test push 451 BE+90 FE + QA-B95) |

### Merged commit (1127차)

- `debe6dd` — `fix(uxd-141): make staff detail aria labels unique` (StaffPage·StaffStatusReportPage·pilotPageFlows)

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-20T04:46:18+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-20 1125차)

> **1125차 PASS(@test baseline SYNCED)** — test `@1b6d2b1` **1833/1833 PASS** (340.62s) · merge **SKIP** (`test..develop` **0/0** · SYNCED) · build **1066 modules** (7.65s) · audit **0** · live E2E **126 PASS/19 SKIP** (30.46s) · Open **0(active frontend)** · **★ QA-B161 Fixed @ `202c1fe`** · cross-stream **BLOCK(BE QA-B162)** · operation **BLOCK**

## 1125차 검증 요약 (merge SKIP — develop/test SYNCED)

| 항목 | 결과 |
|---|---|
| test HEAD | `1b6d2b1` |
| develop HEAD | `1b6d2b1` |
| ahead (`test..develop`) | **0 ahead / 0 behind** (SYNCED) |
| develop working tree | **CLEAN** |
| test working tree | **CLEAN** |
| test npm test (locked) | **1833/1833 PASS** @ `1b6d2b1` (340.62s, 363 files) |
| develop npm test (locked) | **SYNCED** (same HEAD @ `1b6d2b1`) |
| build | **1066 modules SUCCESS** (7.65s) |
| audit | **0 vulnerabilities** |
| live E2E | **126 PASS/19 SKIP/0 FAIL** (30.46s) |
| Maven | N/A (`pom.xml` 없음) |
| FE merge status | **SKIP** (SYNCED — coder merged 4 commits since `f31c346`) |
| BE merge status | **BLOCK** (develop WT DIRTY 3M · QA-B162) |
| transfer verdict | **PASS(@test baseline SYNCED)** |
| cross-stream | **BLOCK(BE QA-B162)** |
| operation | **BLOCK** (QA-B162 + push 450 BE+89 FE + QA-B95) |

### SYNCED commits (since 1123차 pending — now on test)

- `965e569` — UXD-141 FAQ21823 a11y (root cause of QA-B161)
- `682d647` — live-e2e nested health readiness payloads
- `202c1fe` — **QA-B161 Fixed** dedupe renewal summary link aria-labels
- `1b6d2b1` — FAQ21823 contract clauses checklist + template modal

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-20T03:50:48+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-20 1123차)

> **1123차 PASS(@test baseline)+BLOCK(develop merge gate)** — test `@f31c346` **1831/1831 PASS** (344.29s) · merge **SKIP** (`test..develop` 0/3) · live E2E **SKIP** (merge 미실행 사이클) · Open **1(active frontend QA-B161, unchanged)** · cross-stream **BLOCK(FE merge gate)** · operation **BLOCK**

## 1123차 검증 요약 (merge SKIP — test baseline revalidation)

| 항목 | 결과 |
|---|---|
| test HEAD | `f31c346` |
| develop HEAD | `202c1fe` |
| ahead (`test..develop`) | **0 ahead / 3 behind** |
| develop working tree | **READ-ONLY (미검증)** |
| test working tree | **CLEAN** |
| test npm test (locked) | **1831/1831 PASS** @ `f31c346` (344.29s) |
| develop npm test (locked) | **SKIP** (이번 사이클 미실행) |
| build | **SKIP** (이번 사이클 미실행) |
| audit | **SKIP** (이번 사이클 미실행) |
| live E2E | **SKIP** (merge 미실행 사이클) |
| Maven | N/A (`pom.xml` 없음) |
| FE merge status | **SKIP** (develop merge gate BLOCK) |
| BE merge status | **N/A (frontend 재검증 사이클)** |
| transfer verdict | **BLOCK(develop merge gate)** |
| cross-stream | **BLOCK(FE QA-B161)** |
| operation | **BLOCK** (QA-B161+push 450 BE+85 FE+QA-B95) |

### pending commits (not merged — 3)

- `965e569` — `ux(a11y): FAQ21823 근로재계약 UI·현금영수증 identifier 접근성 재점검 (UXD-141)` — **BLOCK**: `StaffEmploymentContractRenewalSummaryPanel` Link `aria-label` 중복
- `682d647` — `fix(v2/live-e2e): accept nested health readiness payloads`
- `202c1fe` — `fix(v2/live-e2e): tolerate optional title in health readiness payloads`

### root cause (QA-B161)

`StaffPage.test.jsx` 「shows staff list」— `StaffEmploymentContractRenewalSummaryPanel` (`@965e569`)과 직원 목록 테이블이 동일 `aria-label` (`{name} 직원 상세`) 사용 → `getByRole("link", { name: "김요양 직원 상세" })` multiple elements.

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-20T03:29:46+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-20 1121차)

> **1121차 BLOCK(develop merge gate)** — test `@f31c346` **1830/1831 PASS** (338.51s; StaffPage full-suite 1 FAIL) · develop `@682d647` **1830/1831 PASS** (340.08s; isolated StaffPage FAIL — UXD-141 duplicate aria-label) · merge **SKIP** (`test..develop` 0/2) · build **1066 modules** (7.67s) · audit **0** · live E2E **126 PASS/19 SKIP** (30.22s) · Open **1(active frontend QA-B161)** · cross-stream **BLOCK(BE QA-B160 + FE merge gate)** · operation **BLOCK**

## 1121차 검증 요약 (merge SKIP — UXD-141 StaffPage unit regression)

| 항목 | 결과 |
|---|---|
| test HEAD | `f31c346` |
| develop HEAD | `682d647` |
| ahead (`test..develop`) | **0 ahead / 2 behind** |
| develop working tree | **CLEAN** |
| test working tree | **CLEAN** |
| test npm test (locked) | **1830/1831 PASS** @ `f31c346` (338.51s; StaffPage full-suite 1 FAIL) |
| develop npm test (locked) | **1830/1831 PASS** @ `682d647` (340.08s; isolated StaffPage FAIL) |
| build | 1066 modules SUCCESS (7.67s) |
| audit | 0 vulnerabilities |
| live E2E | **126 PASS/19 SKIP/0 FAIL** (30.22s) |
| Maven | N/A (`pom.xml` 없음) |
| FE merge status | **SKIP** (develop merge gate BLOCK) |
| BE merge status | **BLOCK** (develop WT DIRTY QA-B160 · `test..develop` 0/3) |
| transfer verdict | **BLOCK(develop merge gate)** |
| cross-stream | **BLOCK(BE QA-B160 + FE QA-B161)** |
| operation | **BLOCK** (QA-B161+QA-B160+push 446 BE+85 FE+QA-B95) |

### pending commits (not merged — 2)

- `965e569` — `ux(a11y): FAQ21823 근로재계약 UI·현금영수증 identifier 접근성 재점검 (UXD-141)` — **BLOCK**: `StaffEmploymentContractRenewalSummaryPanel` Link `aria-label` 중복
- `682d647` — `fix(v2/live-e2e): accept nested health readiness payloads`

### root cause (QA-B161)

`StaffPage.test.jsx` 「shows staff list」— `StaffEmploymentContractRenewalSummaryPanel` (`@965e569`)과 직원 목록 테이블이 동일 `aria-label` (`{name} 직원 상세`) 사용 → `getByRole("link", { name: "김요양 직원 상세" })` multiple elements.

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-20T02:45:11+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-20 1119차)

> **1119차 PASS(@test post-merge)+merge EXECUTED** — pre-merge test `@10585b9` **1827/1827 PASS** (carry) · develop `@f31c346` **1828/1828 PASS** (363 files, 333.42s) · ★ merge FF `10585b9`→`f31c346` (1 commit) · post-merge **1828/1828 PASS** (337.21s) · build **1066 modules SUCCESS** (7.64s) · audit **0 vulnerabilities** · live E2E **126 PASS/19 SKIP** (30.78s) · BE develop/test `@beef81e`/`@7e4c07e` **merge pending 2** · Open **0(active frontend)** · cross-stream **BLOCK(BE merge pending 2 · QA-B159)** · operation **BLOCK**(BE merge pending 2 + origin/test push 446 BE+85 FE + QA-B95)

## 1119차 검증 요약 (merge EXECUTED — US-R03 FAQ21823 dashboard widget)

| 항목 | 결과 |
|---|---|
| pre-merge test HEAD | `10585b9` |
| develop HEAD | `f31c346` |
| post-merge test HEAD | `f31c346` |
| ahead (`test..develop`) | **0 ahead / 0 behind** (post-merge SYNCED) |
| develop working tree | **CLEAN** |
| test working tree | **CLEAN** |
| develop npm test (locked) | **1828/1828 PASS** @ `f31c346` (333.42s) |
| post-merge vitest (locked) | **1828/1828 PASS** @ `f31c346` (337.21s) |
| build | 1066 modules SUCCESS (7.64s) |
| audit | 0 vulnerabilities |
| live E2E | **126 PASS/19 SKIP/0 FAIL** (30.78s) |
| Maven | N/A (`pom.xml` 없음) |
| FE merge status | **EXECUTED** (FF 1 commit) |
| BE merge status | **BLOCK** (`test..develop` 0/2 @ `7a9d7a5`·`beef81e`) |
| transfer verdict | **PASS(@test post-merge)+merge EXECUTED** |
| cross-stream | **BLOCK(BE merge pending 2 · QA-B159)** |
| operation | **BLOCK** (BE merge pending 2 + push 446 BE+85 FE + QA-B95) |

### commit landed (1119차 merge)

- `f31c346` — `feat(v1.2.1/US-R03): add FAQ21823 employment contract renewal dashboard widget`
  - `DashboardPage` employment contract renewal StatCard/widget + tests
  - `dashboardSummary.js` wire + tests
  - `staffEmploymentContractCompliance.js` shared utility + tests

### changed files (6)

- `src/pages/DashboardPage.jsx` (+41)
- `src/pages/DashboardPage.test.jsx` (+39)
- `src/pages/dashboardSummary.js` (+8)
- `src/pages/dashboardSummary.test.js` (+2)
- `src/utils/staffEmploymentContractCompliance.js` (+13)
- `src/utils/staffEmploymentContractCompliance.test.js` (+26)

---

## 1117차 (이전 사이클 — 보존)

> pre-merge `@f62402f` · merge FF → `@10585b9` · post-merge **1827/1827 PASS**
