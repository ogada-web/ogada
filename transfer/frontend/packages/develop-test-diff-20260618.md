<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-19T01:14:28+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-19 1044차)

> **1044차 BLOCK(unit regression @test worktree)** — test `@cf85003` (`src/frontend-test`) `npm test`(locked) **1 FAIL/1750 PASS** (353 files, 322.92s; `liveE2eSuiteGuard.test.js` regex guard가 `liveG21Describe`를 허용하지 않아 실패) · `npm run build` **1056 modules SUCCESS** (10.57s) · `npm audit --omit=dev --audit-level=high` **0 vulnerabilities** · `npm run test:live-e2e` **123 PASS/19 SKIP** (31.54s) · develop `@689f377` / test `@cf85003` WT **CLEAN** · `test..develop` **0 ahead / 1 behind** · origin/test `@ab4de83` (**47 unpushed**) · Open **1 BLOCK QA-20260619-B144(active frontend)** · cross-stream **BLOCK(frontend merge pending 1)** · operation **BLOCK**(QA-B144 + origin/test push 410 BE+47 FE + QA-B95)

## 1044차 검증 요약 (merge SKIP)

| 항목 | 값 (1044차) |
|------|-----|
| test HEAD | `cf85003` (origin/test `ab4de83`, 47 unpushed) |
| develop HEAD | `689f377` |
| ahead (`test..develop`) | **0 ahead / 1 behind** (frontend merge pending 1) |
| develop working tree | **CLEAN** |
| unit test (@test worktree, locked) | **1 FAIL/1750 PASS** (353 files, 322.92s) |
| 실패 항목 | `src/test/liveE2eSuiteGuard.test.js` (`liveG21Describe` pattern gate) |
| build | 1056 modules SUCCESS (10.57s) |
| audit | 0 vulnerabilities |
| live E2E | **123 PASS/19 SKIP** (49 files, 31.54s) |
| FE merge status | **SKIP (unit regression + merge pending 1)** |
| transfer verdict | **BLOCK(QA-20260619-B144)** |
| operation | **BLOCK** (QA-B144 + origin/test push + QA-B95) |

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-19T00:11:30+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-19 1041차)

> **1041차 PASS(post-merge)+merge EXECUTED** — pre-merge test `@f26e075` vitest(worktree) **1 FAIL/1738 PASS** (353 files, 326.62s; baseline flake) · develop `@2095985` `npm test`(locked) **1744/1744 PASS** (324.50s) · ★ **develop→test merge EXECUTED**(FF `f26e075`→`2095985`, 3 commits) · post-merge **1744/1744 PASS** (333.69s) · `npm run build` **1056 modules SUCCESS** (10.49s) · `npm audit --omit=dev --audit-level=high` **0 vulnerabilities** · `npm run test:live-e2e` **122 PASS/19 SKIP** (32.00s) · develop/test `@2095985` WT **CLEAN** · `test..develop` **0 ahead** · origin/test `@ab4de83` (**46 unpushed**) · Open **0(active frontend)** · **★ QA-20260618-B143 Fixed** · cross-stream **BLOCK(BE merge pending 1)** · operation **BLOCK**(origin/test push 407 BE+46 FE+BE merge pending 1+QA-B95)

## 1041차 검증 요약 (merge EXECUTED)

| 항목 | 값 (1041차) |
|------|-----|
| test HEAD | `2095985` (origin/test `ab4de83`, 46 unpushed) |
| develop HEAD | `2095985` |
| ahead (`test..develop`) | **0 ahead / 0 behind** (SYNCED) |
| develop working tree | **CLEAN** |
| pre-merge unit test (@test worktree) | **1 FAIL/1738 PASS** (353 files, 326.62s) |
| develop HEAD unit test (locked) | **1744/1744 PASS** (353 files, 324.50s) |
| post-merge unit test | **1744/1744 PASS** (353 files, 333.69s) |
| build | 1056 modules SUCCESS (10.49s) |
| audit | 0 vulnerabilities |
| live E2E | **122 PASS/19 SKIP** (49 files, 32.00s) |
| FE merge status | **EXECUTED** (FF `f26e075`→`2095985`, 3 commits) |
| transfer verdict | **PASS(post-merge)** |
| operation | **BLOCK** (origin/test push + BE merge pending 1 + QA-B95) |

### merge commits (3)

| SHA | message |
|-----|---------|
| `28e5525` | fix(g41): show filter-year validation errors in training logs |
| `5c4e241` | ux(a11y): G21 standalone NHIS compare panel and G41 filter-year (UXD-134) |
| `2095985` | fix(test): stabilize care report and special notes page tests (QA-B141) |

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-18T23:33:15+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-18 1039차)

> **1039차 BLOCK(develop dirty)+merge SKIP** — test `@f26e075` flock vitest **1739/1739 PASS** (353 files, 331.65s) · develop `@28e5525` WT **DIRTY 2M** (QA-B141 test stabilization WIP · **QA-20260618-B143**) · develop HEAD `npm test`(locked) **1743/1743 PASS** (324.98s) · `npm run build` **1056 modules SUCCESS** (7.58s) · `npm audit --omit=dev --audit-level=high` **0 vulnerabilities** · `npm run test:live-e2e` **122 PASS/19 SKIP** (32.66s) · test `@f26e075` WT **CLEAN** · `test..develop` **0 ahead / 1 behind** · origin/test `@ab4de83` (**44 unpushed**) · Open **1 BLOCK QA-20260618-B143(active frontend)** · cross-stream **BLOCK(BE QA-B142)** · operation **BLOCK**(QA-B143+QA-B142+push 407 BE+44 FE+QA-B95)

## 1039차 검증 요약 (merge SKIP)

| 항목 | 값 (1039차) |
|------|-----|
| test HEAD | `f26e075` (origin/test `ab4de83`, 44 unpushed) |
| develop HEAD | `28e5525` |
| ahead (`test..develop`) | **0 ahead / 1 behind** (merge pending 1) |
| develop working tree | **DIRTY 2M** (QA-B143) |
| unit test (@test worktree) | **1739/1739 PASS** (353 files, 331.65s) |
| develop HEAD unit test (locked, WIP 포함) | **1743/1743 PASS** (353 files, 324.98s) |
| build | 1056 modules SUCCESS (7.58s) |
| audit | 0 vulnerabilities |
| live E2E | **122 PASS/19 SKIP** (49 files, 32.66s) |
| FE merge status | **SKIP (develop dirty + merge pending 1)** |
| transfer verdict | **BLOCK(QA-20260618-B143)** |
| operation | **BLOCK** (QA-B143 + QA-B142 + origin/test push + QA-B95) |

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-18T22:49:01+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-18 1037차)

> **1037차 BLOCK(unit regression)+merge SKIP** — test `@f26e075` `npm test` **2 FAIL/1741 PASS** (353 files, 323.60s; `CareNursingServiceReportPage`·`CareServiceSpecialNotesPage`) · `npm run build` **1056 modules SUCCESS** (10.65s) · `npm audit --omit=dev --audit-level=high` **0 vulnerabilities** · `npm run test:live-e2e` **122 PASS/19 SKIP** (49 files, 32.02s) · develop `@28e5525` / test `@f26e075` WT **CLEAN** · `test..develop` **0 ahead / 1 behind**(merge pending 1) · origin/test `@ab4de83` (**43 unpushed**) · Open **1 BLOCK QA-20260618-B141(active frontend)** · cross-stream **SYNCED(BE @f932fd3)** · operation **BLOCK**(QA-B141+push 407 BE+43 FE+QA-B95)

## 1037차 검증 요약 (merge SKIP)

| 항목 | 값 (1037차) |
|------|-----|
| test HEAD | `f26e075` (origin/test `ab4de83`, 43 unpushed) |
| develop HEAD | `28e5525` |
| ahead (`test..develop`) | **0 ahead / 1 behind** (merge pending 1) |
| develop working tree | **CLEAN** |
| unit test | **2 FAIL/1741 PASS** (353 files, 323.60s) |
| 실패 항목 | `CareNursingServiceReportPage.test.jsx` · `CareServiceSpecialNotesPage.test.jsx` |
| build | 1056 modules SUCCESS (10.65s) |
| audit | 0 vulnerabilities |
| live E2E | **122 PASS/19 SKIP** (49 files, 32.02s) |
| FE merge status | **SKIP (unit regression + merge pending 1)** |
| transfer verdict | **BLOCK(QA-20260618-B141)** |
| operation | **BLOCK** (QA-B141 + origin/test push 407 BE+43 FE + QA-B95) |

---

<!-- 1034차 이전 기록 -->
<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-18T21:55:00+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-18 1034차)

> **1034차 PASS(@frontend-test post-merge)+merge EXECUTED** — merge FF `ad18606`→`797c529` (1 commit: v2/G21 standalone NHIS comparison panel on visits page) · `npm test` **1737/1737 PASS** (353 files, 332s pre / 326s post) · `npm run build` **1056 modules SUCCESS** (7.51s) · `npm audit --omit=dev --audit-level=high` **0 vulnerabilities** · `npm run test:live-e2e` **122 PASS/19 SKIP** (49 files, 29.25s) · develop/test `@797c529` WT **CLEAN** · origin/test `@ab4de83` (**42 unpushed**) · Open **0(active frontend)** · cross-stream **BLOCK(BE merge pending 1)** · operation **BLOCK**(push 405 BE+42 FE+BE merge pending 1+QA-B95)

## 1034차 병합 커밋 (ad18606→797c529)

| SHA | 메시지 |
|-----|--------|
| `797c529` | feat(v2/G21): add standalone NHIS comparison panel on visits page |

## diff stat (ad18606..797c529)

```
src/components/visits/VisitBatchConfirmPanel.jsx         |  55 +------
src/components/visits/VisitNhisComparisonDetail.jsx      |   9 +-
src/components/visits/VisitNhisComparisonDetail.test.jsx |  32 +++++
src/components/visits/VisitNhisComparisonPanel.jsx       | 158 ++++++++++++
src/components/visits/VisitNhisComparisonPanel.test.jsx  | 101 +++++++++++++
src/pages/VisitsPage.jsx                                 |   9 ++
src/pages/VisitsPage.test.jsx                            |   3 +
src/utils/visitNhisComparison.js                         |  52 +++++++
src/utils/visitNhisComparison.test.js                    |  32 +++++
9 files changed, 396 insertions(+), 55 deletions(-)
```

---

<!-- 1032차 이전 기록 -->
> **1032차 PASS(@test baseline)+merge SKIP(이미 synced)** — test/develop `@ad18606` · `npm test` **1730/1730 PASS** (351 files, 326.22s) · `npm run build` **1054 modules SUCCESS** (7.63s) · `npm audit --omit=dev --audit-level=high` **0 vulnerabilities** · `npm run test:live-e2e` **122 PASS/19 SKIP** (49 files, 29.67s) · develop/test WT **CLEAN** · origin/test `@ab4de83` (**41 unpushed**) · Open **0(active frontend)** · cross-stream **SYNCED(FE+BE @39fa41a)** · operation **BLOCK**(push 405 BE+41 FE + QA-B95)

## 1032차 (2026-06-18T21:00 UTC) — baseline PASS · synced 유지

| 항목 | 값 (1032차) |
|------|-----|
| test HEAD | `ad18606` (origin/test `ab4de83`, 41 unpushed) |
| develop HEAD | `ad18606` |
| ahead (`test..develop`) | **0** (SYNCED) |
| develop working tree | **CLEAN** |
| unit test | **1730/1730 PASS** (351 files, 326.22s) |
| build | 1054 modules SUCCESS (7.63s) |
| audit | 0 vulnerabilities |
| live E2E | **122 PASS/19 SKIP** (49 files, 29.67s) |
| route / page | 106 route · 85 page |
| FE merge status | **SKIP (already synced post-1031)** |
| cross-stream | BE develop/test `@39fa41a` **SYNCED** |
| transfer verdict | **PASS(@frontend-test baseline)** |
| operation | **BLOCK** (origin/test push 405 BE+41 FE + QA-B95) |

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-18T20:52:49+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-18 1031차)

> **1031차 PASS(@test post-merge)+merge EXECUTED(1 FE)** — pre-merge test `@68a4e35` carry **1730/1730 PASS** (351 files, 321.45s) · develop `@ad18606` **1730/1730 PASS** (320.60s) · ★ merge FF `68a4e35`→`ad18606` (1 commit) · post-merge **1730/1730 PASS** (320.79s) · build **1054 modules** (7.39s) · audit **0** · live E2E **122 PASS/19 SKIP** (31.72s) · develop/test `@ad18606` WT **CLEAN** · origin/test `@ab4de83` (**41 unpushed**) · Open **0(active)** · cross-stream **SYNCED(FE+BE @39fa41a)** · operation **BLOCK**(push 405 BE+41 FE + QA-B95)

## 1031차 (2026-06-18T20:52 UTC) — merge EXECUTED · post-merge PASS · v2/G21 NHIS comparison detail

| 항목 | 값 (1031차) |
|------|-----|
| test HEAD | `ad18606` (origin/test `ab4de83`, 41 unpushed) |
| develop HEAD | `ad18606` |
| ahead (`test..develop`) | **0** (SYNCED post-merge) |
| develop working tree | **CLEAN** |
| unit test (@test pre-merge) | **1730/1730 PASS** @ `68a4e35` (351 files, 321.45s) |
| unit test (develop HEAD) | **1730/1730 PASS** (351 files, 320.60s) |
| unit test (post-merge) | **1730/1730 PASS** (351 files, 320.79s) |
| build | 1054 modules SUCCESS (7.39s) |
| audit | 0 vulnerabilities |
| live E2E (@test) | **122 PASS/19 SKIP** (49 files, 31.72s) |
| route / page | 106 route · 84 page |
| merge commits | `ad18606` feat(v2/G21): add per-client NHIS comparison detail in batch confirm |
| changed files | `VisitBatchConfirmPanel*` · `VisitNhisComparisonDetail*` · `services.js` · `visitServices.test.js` |
| FE merge status | **EXECUTED (local FF)** |
| cross-stream | BE develop/test `@39fa41a` **SYNCED** |
| transfer verdict | **PASS(@test post-merge)** |
| operation | **BLOCK** (origin/test push 405 BE+41 FE + QA-B95) |

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-18T20:04:45+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-18 1029차)

> **1029차 PASS(@test baseline)+merge SKIP(이미 synced)** — test/develop `@68a4e35` · `npm test` **1725/1725 PASS** (350 files, 320.57s) · `npm run build` **1053 modules SUCCESS** (7.43s) · `npm audit --omit=dev --audit-level=high` **0 vulnerabilities** · `npm run test:live-e2e` **122 PASS/19 SKIP** (49 files, 28.88s) · develop/test WT **CLEAN** · origin/test `@ab4de83` (**40 unpushed**) · Open **0(active frontend)** · cross-stream **BLOCK(BE regression QA-20260618-B139 + merge pending 2)** · operation **BLOCK**(push 40 FE+402 BE + QA-B95)

## 1029차 (2026-06-18T20:04 UTC) — baseline PASS · synced 유지

| 항목 | 값 (1029차) |
|------|-----|
| test HEAD | `68a4e35` (origin/test `ab4de83`, 40 unpushed) |
| develop HEAD | `68a4e35` |
| ahead (`test..develop`) | **0** (SYNCED) |
| develop working tree | **CLEAN** |
| unit test | **1725/1725 PASS** (350 files, 320.57s) |
| build | 1053 modules SUCCESS (7.43s) |
| audit | 0 vulnerabilities |
| live E2E | **122 PASS/19 SKIP** (49 files, 28.88s) |
| route / page | 106 route · 84 page |
| FE merge status | **SKIP (already synced)** |
| cross-stream | BE develop `@4046046` / test `@03a052a` · BE merge pending **2** · **QA-20260618-B139 active** |
| transfer verdict | **PASS(@frontend-test baseline)** |
| operation | **BLOCK** (QA-B139 + origin/test push 40 FE+402 BE + QA-B95) |

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-18T18:52:00+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-18 1027차)

> **1027차 PASS(@test post-merge)+merge EXECUTED(1 FE)** — pre-merge test `@570912e` carry **1722/1722 PASS** (1025차) · develop `@f232285` **1723/1723 PASS** (317.96s) · ★ merge FF `570912e`→`f232285` (1 commit) · post-merge **1723/1723 PASS** (318.79s) · build **1053 modules** (10.79s) · audit **0** · live E2E **122 PASS/19 SKIP** (31.68s) · develop/test `@f232285` WT **CLEAN** · origin/test `@ab4de83` (**38 unpushed**) · Open **0(active)** · cross-stream **BLOCK(BE merge pending 1 @8a8c5b3/03a052a)** · operation **BLOCK**(push 38 FE+402 BE + BE merge + QA-B95)

## 1027차 (2026-06-18T18:52 UTC) — merge EXECUTED · post-merge PASS · v2/G21 RFID no-diff alert

| 항목 | 값 (1027차) |
|------|-----|
| test HEAD | `f232285` (origin/test `ab4de83`, 38 unpushed) |
| develop HEAD | `f232285` |
| ahead (`test..develop`) | **0** (SYNCED post-merge) |
| develop working tree | **CLEAN** |
| unit test (@test pre-merge) | **1722/1722 PASS** @ `570912e` (carry 1025차) |
| unit test (develop HEAD) | **1723/1723 PASS** (350 files, 317.96s) |
| unit test (post-merge) | **1723/1723 PASS** (350 files, 318.79s) |
| build | 1053 modules SUCCESS (10.79s) |
| audit | 0 vulnerabilities |
| live E2E (@test) | **122 PASS/19 SKIP** (49 files, 31.68s) |
| route / page | 106 route · 84 page |
| merge commits | `f232285` Add no-diff success alert for RFID compare |
| FE merge status | **EXECUTED (local)** |
| cross-stream | BE develop `@8a8c5b3` / test `@03a052a` · **merge pending 1** |
| transfer verdict | **PASS(@test post-merge)** |
| operation | **BLOCK** (origin/test push 38 FE+402 BE + BE merge + QA-B95) |

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-18T18:18:00+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-18 1025차)

> **1025차 PASS(@test post-merge)+merge EXECUTED(1 FE)** — pre-merge test `@3a27303` carry **1720/1720 PASS** (1023차) · develop `@570912e` **1722/1722 PASS** (319.98s) · ★ merge FF `3a27303`→`570912e` (1 commit) · post-merge **1722/1722 PASS** (325.05s) · build **1051 modules** (10.64s) · audit **0** · live E2E **122 PASS/19 SKIP** (32.08s) · develop/test `@570912e` WT **CLEAN** · origin/test `@ab4de83` (**37 unpushed**) · Open **0(active)** · cross-stream **SYNCED(FE+BE @03a052a)** · operation **BLOCK**(push 37 FE+402 BE + QA-B95)

## 1025차 (2026-06-18T18:18 UTC) — merge EXECUTED · post-merge PASS · v2/G21 RFID diff normalize

| 항목 | 값 (1025차) |
|------|-----|
| test HEAD | `570912e` (origin/test `ab4de83`, 37 unpushed) |
| develop HEAD | `570912e` |
| ahead (`test..develop`) | **0** (SYNCED post-merge) |
| develop working tree | **CLEAN** |
| unit test (@test pre-merge) | **1720/1720 PASS** @ `3a27303` (carry 1023차) |
| unit test (develop HEAD) | **1722/1722 PASS** (350 files, 319.98s) |
| unit test (post-merge) | **1722/1722 PASS** (350 files, 325.05s) |
| build | 1051 modules SUCCESS (10.64s) |
| audit | 0 vulnerabilities |
| live E2E (@develop) | **122 PASS/19 SKIP** (49 files, 32.08s) |
| route / page | 106 route · 84 page |
| merge commits | `570912e` v2/G21 normalize RFID diff code variants in compare results |
| FE merge status | **EXECUTED (local)** |
| cross-stream | BE develop/test `@03a052a` **SYNCED** |
| transfer verdict | **PASS(@test post-merge)** |
| operation | **BLOCK** (origin/test push 37 FE+402 BE + QA-B95) |

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-18T17:45:00+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-18 1023차)

> **1023차 PASS(@test post-merge)+merge EXECUTED(1 FE)** — pre-merge test `@f9ed97d` carry **1710/1710 PASS** (1021차) · develop `@3a27303` **1720/1720 PASS** (322.13s) · ★ merge FF `f9ed97d`→`3a27303` (1 commit) · post-merge **1720/1720 PASS** (321.42s) · build **1051 modules** (10.65s) · audit **0** · live E2E **122 PASS/19 SKIP** (29.34s) · develop/test `@3a27303` WT **CLEAN** · origin/test `@ab4de83` (**36 unpushed**) · Open **0(active)** · cross-stream **SYNCED(FE+BE @5f710e3)** · operation **BLOCK**(push 36 FE+401 BE + QA-B95)

## 1023차 (2026-06-18T17:45 UTC) — merge EXECUTED · post-merge PASS · v2/G21 context nav

| 항목 | 값 (1023차) |
|------|-----|
| test HEAD | `3a27303` (origin/test `ab4de83`, 36 unpushed) |
| develop HEAD | `3a27303` |
| ahead (`test..develop`) | **0** (SYNCED post-merge) |
| develop working tree | **CLEAN** |
| unit test (@test pre-merge) | **1710/1710 PASS** @ `f9ed97d` (carry 1021차) |
| unit test (develop HEAD) | **1720/1720 PASS** (350 files, 322.13s) |
| unit test (post-merge) | **1720/1720 PASS** (350 files, 321.42s) |
| build | 1051 modules SUCCESS (10.65s) |
| audit | 0 vulnerabilities |
| live E2E (@test) | **122 PASS/19 SKIP** (49 files, 29.34s) |
| route / page | 106 route · 85 page |
| merge commits | `3a27303` v2/G21 add plan/billing/split context nav with URL sync |
| FE merge status | **EXECUTED (local)** |
| cross-stream | BE develop/test `@5f710e3` **SYNCED** |
| transfer verdict | **PASS(@test post-merge)** |
| operation | **BLOCK** (origin/test push 36 FE+401 BE + QA-B95) |

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-18T17:10:00+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-18 1021차)

> **1021차 PASS(@test post-merge)+merge EXECUTED(1 FE)** — pre-merge test `@f5639df` carry **1709/1709 PASS** (1019차) · develop `@f9ed97d` **1710/1710 PASS** (321.66s) · ★ merge FF `f5639df`→`f9ed97d` (1 commit) · post-merge **1710/1710 PASS** (323.05s) · build **1051 modules** (10.55s) · audit **0** · live E2E **122 PASS/19 SKIP** (32.45s) · develop/test `@f9ed97d` WT **CLEAN** · origin/test `@ab4de83` (**35 unpushed**) · Open **0(active)** · cross-stream **SYNCED(FE+BE @f26abb0)** · operation **BLOCK**(push 35 FE+400 BE + QA-B95)

## 1021차 (2026-06-18T17:10 UTC) — merge EXECUTED · post-merge PASS · v2/G21 batch confirm readiness

| 항목 | 값 (1021차) |
|------|-----|
| test HEAD | `f9ed97d` (origin/test `ab4de83`, 35 unpushed) |
| develop HEAD | `f9ed97d` |
| ahead (`test..develop`) | **0** (SYNCED post-merge) |
| develop working tree | **CLEAN** |
| unit test (@test pre-merge) | **1709/1709 PASS** @ `f5639df` (carry 1019차) |
| unit test (develop HEAD) | **1710/1710 PASS** (348 files, 321.66s) |
| unit test (post-merge) | **1710/1710 PASS** (348 files, 323.05s) |
| build | 1051 modules SUCCESS (10.55s) |
| audit | 0 vulnerabilities |
| live E2E (@test) | **122 PASS/19 SKIP** (49 files, 32.45s) |
| route / page | 106 route · 85 page |
| merge commits | `f9ed97d` v2/G21 wire PLAN/BILLING split readiness counts in batch confirm panel |
| FE merge status | **EXECUTED (local)** |
| cross-stream | BE develop/test `@f26abb0` **SYNCED** |
| transfer verdict | **PASS(@test post-merge)** |
| operation | **BLOCK** (origin/test push 35 FE+400 BE + QA-B95) |

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-18T16:37:00+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-18 1019차)

> **1019차 PASS(@test post-merge)+merge EXECUTED(1 FE)** — pre-merge test `@50d330d` **1709/1709 PASS** (320.89s) · develop `@f5639df` **1709/1709 PASS** (320.68s) · ★ merge FF `50d330d`→`f5639df` (1 commit) · post-merge **1709/1709 PASS** (323.49s) · build **1051 modules** (10.42s) · audit **0** · live E2E **122 PASS/19 SKIP** (29.76s) · develop/test `@f5639df` WT **CLEAN** · origin/test `@ab4de83` (**34 unpushed**) · Open **0(active)** · cross-stream **SYNCED(FE+BE @28860ae)** · operation **BLOCK**(push 34 FE+399 BE + QA-B95)

## 1019차 (2026-06-18T16:37 UTC) — merge EXECUTED · post-merge PASS · G-7-1 all-print label

| 항목 | 값 (1019차) |
|------|-----|
| test HEAD | `f5639df` (origin/test `ab4de83`, 34 unpushed) |
| develop HEAD | `f5639df` |
| ahead (`test..develop`) | **0** (SYNCED post-merge) |
| develop working tree | **CLEAN** |
| unit test (@test pre-merge) | **1709/1709 PASS** @ `50d330d` (348 files, 320.89s) |
| unit test (develop HEAD) | **1709/1709 PASS** (348 files, 320.68s) |
| unit test (post-merge) | **1709/1709 PASS** (348 files, 323.49s) |
| build | 1051 modules SUCCESS (10.42s) |
| audit | 0 vulnerabilities |
| live E2E (@test) | **122 PASS/19 SKIP** (49 files, 29.76s) |
| route / page | 106 route · 85 page |
| merge commits | `f5639df` v1.2.1/G-7-1 clarify all-print label for unpaid claims |
| FE merge status | **EXECUTED (local)** |
| cross-stream | BE develop/test `@28860ae` **SYNCED** |
| transfer verdict | **PASS(@test post-merge)** |
| operation | **BLOCK** (origin/test push 34 FE+399 BE + QA-B95) |

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-18T15:53:19+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-18 1017차)

> **1017차 PASS(@test post-merge)+merge EXECUTED(2 FE)** — pre-merge test `@94c65e2` **1699/1699 PASS** (320.92s) · develop `@50d330d` **1709/1709 PASS** (321.84s) · ★ merge FF `94c65e2`→`50d330d` (2 commits) · post-merge **1709/1709 PASS** (324.68s) · build **1051 modules** (10.43s) · audit **0** · live E2E **122 PASS/19 SKIP** (29.19s) · develop/test `@50d330d` WT **CLEAN** · origin/test `@ab4de83` (**33 unpushed**) · Open **0(active)** · cross-stream **SYNCED(FE+BE @6aeafe7)** · operation **BLOCK**(push 33 FE+398 BE + QA-B95)

## 1017차 (2026-06-18T15:53 UTC) — merge EXECUTED · post-merge PASS · G-7-1 billing print bundle + UXD-132

| 항목 | 값 (1017차) |
|------|-----|
| test HEAD | `50d330d` (origin/test `ab4de83`, 33 unpushed) |
| develop HEAD | `50d330d` |
| ahead (`test..develop`) | **0** (SYNCED post-merge) |
| develop working tree | **CLEAN** |
| unit test (@test pre-merge) | **1699/1699 PASS** @ `94c65e2` (346 files, 320.92s) |
| unit test (develop HEAD) | **1709/1709 PASS** (348 files, 321.84s) |
| unit test (post-merge) | **1709/1709 PASS** (348 files, 324.68s) |
| build | 1051 modules SUCCESS (10.43s) |
| audit | 0 vulnerabilities |
| live E2E (@test) | **122 PASS/19 SKIP** (49 files, 29.19s) |
| route / page | 106 route · 85 page |
| merge commits | `f8321c7` UXD-132 G15 compliance badges+SideNav · `50d330d` G-7-1 billing statement print bundle |
| FE merge status | **EXECUTED (local)** |
| cross-stream | BE develop/test `@6aeafe7` **SYNCED** |
| transfer verdict | **PASS(@test post-merge)** |
| operation | **BLOCK** (origin/test push 33 FE+398 BE + QA-B95) |

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-18T14:49:36+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-18 1015차)

> **1015차 PASS(@test post-merge)+merge EXECUTED(1 FE)** — pre-merge test `@b1a16ff` carry **1699/1699 PASS** (1013차) · develop `@94c65e2` **1699/1699 PASS** (320.86s) · ★ merge FF `b1a16ff`→`94c65e2` (1 commit) · post-merge **1699/1699 PASS** (320.67s) · build **1049 modules** (7.34s) · audit **0** · live E2E **122 PASS/19 SKIP** (31.96s) · develop/test `@94c65e2` WT **CLEAN** · origin/test `@ab4de83` (**31 unpushed**) · Open **0(active)** · **★ QA-20260618-B138 Fixed verified** · cross-stream **BLOCK(BE merge pending 1)** · operation **BLOCK**(push 31 FE+396 BE+BE merge+QA-B95)

## 1015차 (2026-06-18T14:49 UTC) — merge EXECUTED · post-merge PASS · v2/live-e2e guardian credential fallback

| 항목 | 값 (1015차) |
|------|-----|
| test HEAD | `94c65e2` (origin/test `ab4de83`, 31 unpushed) |
| develop HEAD | `94c65e2` |
| ahead (`test..develop`) | **0** (SYNCED post-merge) |
| develop working tree | **CLEAN** |
| unit test (@test pre-merge) | **1699/1699 PASS** carry @ `b1a16ff` (1013차) |
| unit test (develop HEAD) | **1699/1699 PASS** (346 files, 320.86s) |
| unit test (post-merge) | **1699/1699 PASS** (346 files, 320.67s) |
| build | 1049 modules SUCCESS (7.34s) |
| audit | 0 vulnerabilities |
| live E2E (@test) | **122 PASS/19 SKIP** (49 files, 31.96s) |
| route / page | 106 route · 85 page |
| merge commits | `94c65e2` v2/live-e2e align guardian credential fallback with backend seed |
| FE merge status | **EXECUTED (local)** |
| cross-stream | BE develop `@72124f7` / test `@8cf09d8` (**1 ahead**) |
| transfer verdict | **PASS(@test post-merge)** |
| operation | **BLOCK** (origin/test push 31 FE+396 BE + BE merge pending 1 + QA-B95) |

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-18T14:19:03+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-18 1013차)

> **1013차 PASS(@test)+BLOCK(transfer develop dirty)** — test `@b1a16ff` **1699/1699 PASS** (322.11s) · build **1049 modules** (7.41s) · audit **0** · live E2E **122 PASS/19 SKIP** (29.92s) · develop `@b1a16ff` WT **DIRTY 2M** (QA-B138) · test `@b1a16ff` CLEAN SYNCED · origin/test `@ab4de83` (**30 unpushed**) · Open **1 BLOCK QA-20260618-B138** · cross-stream **BLOCK(FE)** / BE `@8cf09d8` SYNCED · operation **BLOCK**(QA-B138+push 30 FE+396 BE+QA-B95)

## 1013차 (2026-06-18T14:19 UTC) — develop dirty-tree BLOCK · test baseline PASS

| 항목 | 값 (1013차) |
|------|-----|
| test HEAD | `b1a16ff` (origin/test `ab4de83`, 30 unpushed) |
| develop HEAD | `b1a16ff` |
| ahead (`test..develop`) | **0** (SYNCED · merge SKIP) |
| develop working tree | **DIRTY 2M** — `liveGlobalSetup.js`·`liveE2eHarness.test.js` (QA-B138) |
| unit test (@test) | **1699/1699 PASS** (346 files, 322.11s) |
| build | 1049 modules SUCCESS (7.41s) |
| audit | 0 vulnerabilities |
| live E2E (@test) | **122 PASS/19 SKIP** (49 files, 29.92s) |
| route / page | 106 route · 85 page |
| merge commits | **SKIP** (0 ahead · develop dirty) |
| FE merge status | **BLOCK(develop dirty)** |
| cross-stream | BE develop/test `@8cf09d8` SYNCED |
| transfer verdict | **PASS(@test)+BLOCK(transfer)** |
| operation | **BLOCK** (QA-B138+origin/test push 30 FE+396 BE + QA-B95) |

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-18T13:53:00+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-18 1011차)

> **1011차 PASS(@test post-merge)+merge EXECUTED(1 FE)** — pre-merge test `@07be394` carry **1697/1697 PASS** (1009차) · develop `@b1a16ff` **1699/1699 PASS** (326.42s) · ★ merge FF `07be394`→`b1a16ff` (1 commit) · post-merge **1699/1699 PASS** (320.63s) · build **1049 modules** (10.65s) · audit **0** · live E2E **122 PASS/19 SKIP** (32.23s) · develop/test `@b1a16ff` WT **CLEAN** · origin/test `@ab4de83` (**30 unpushed**) · Open **0(active)** · cross-stream **SYNCED(FE+BE)** · operation **BLOCK**(push 30 FE+395 BE+QA-B95)

## 1011차 (2026-06-18T13:53 UTC) — merge EXECUTED · post-merge PASS · G15 branch contact info in 별지 제22호 export

| 항목 | 값 (1011차) |
|------|-----|
| test HEAD | `b1a16ff` (origin/test `ab4de83`, 30 unpushed) |
| develop HEAD | `b1a16ff` |
| ahead (`test..develop`) | **0** (SYNCED post-merge) |
| develop working tree | **CLEAN** |
| unit test (@test pre-merge) | **1697/1697 PASS** carry @ `07be394` (1009차) |
| unit test (develop HEAD) | **1699/1699 PASS** (346 files, 326.42s) |
| unit test (post-merge) | **1699/1699 PASS** (346 files, 320.63s) |
| build | 1049 modules SUCCESS (10.65s) |
| audit | 0 vulnerabilities |
| live E2E (@test) | **122 PASS/19 SKIP** (49 files, 32.23s) |
| route / page | 106 route · 85 page |
| merge commits | `b1a16ff` v1.3-C/G15 wire branch contact info into 별지 제22호 export |
| FE merge status | **EXECUTED (local)** |
| cross-stream | BE develop/test `@e358f2d` SYNCED |
| transfer verdict | **PASS(@test post-merge)** |
| operation | **BLOCK** (origin/test push 30 FE+395 BE + QA-B95) |

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-18T13:19:05+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-18 1009차)

> **1009차 PASS(@test post-merge)+merge EXECUTED(1 FE)** — pre-merge test `@7de5a6f` carry **1693/1693 PASS** (1007차) · develop `@07be394` **1697/1697 PASS** (323.99s) · ★ merge FF `7de5a6f`→`07be394` (1 commit) · post-merge **1697/1697 PASS** (320.62s) · build **1049 modules** (7.52s) · audit **0** · live E2E **122 PASS/19 SKIP** (29.68s) · develop/test `@07be394` WT **CLEAN** · origin/test `@ab4de83` (**29 unpushed**) · Open **0(active)** · cross-stream **SYNCED(FE+BE)** · operation **BLOCK**(push 29 FE+394 BE+QA-B95)

## 1009차 (2026-06-18T13:19 UTC) — merge EXECUTED · post-merge PASS · G15 complete 별지 제22호 input form

| 항목 | 값 (1009차) |
|------|-----|
| test HEAD | `07be394` (origin/test `ab4de83`, 29 unpushed) |
| develop HEAD | `07be394` |
| ahead (`test..develop`) | **0** (SYNCED post-merge) |
| develop working tree | **CLEAN** |
| unit test (@test pre-merge) | **1693/1693 PASS** carry @ `7de5a6f` (1007차) |
| unit test (develop HEAD) | **1697/1697 PASS** (346 files, 323.99s) |
| unit test (post-merge) | **1697/1697 PASS** (346 files, 320.62s) |
| build | 1049 modules SUCCESS (7.52s) |
| audit | 0 vulnerabilities |
| live E2E (@test) | **122 PASS/19 SKIP** (49 files, 29.68s) |
| route / page | 106 route · 85 page |
| merge commits | `07be394` v1.3-C/G15 complete 별지 제22호 input form with remark and direction labels |
| FE merge status | **EXECUTED (local)** |
| cross-stream | BE develop/test `@a8e2bb2` SYNCED |
| transfer verdict | **PASS(@test post-merge)** |
| operation | **BLOCK** (origin/test push 29 FE+394 BE + QA-B95) |

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-18T12:42:18+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-18 1007차)

> **1007차 PASS(@test post-merge)+merge EXECUTED(1 FE)** — pre-merge test `@a1d6e32` **1693/1693 PASS** (321.83s) · develop `@7de5a6f` **1 FAIL/1692 PASS** (320.87s; flake)→rerun **1693/1693 PASS** (323.55s) · ★ merge FF `a1d6e32`→`7de5a6f` (1 commit) · post-merge **1693/1693 PASS** (324.40s) · build **1050 modules** (10.78s) · audit **0** · live E2E **122 PASS/19 SKIP** (29.80s) · develop/test `@7de5a6f` WT **CLEAN** · origin/test `@ab4de83` (**28 unpushed**) · Open **0(active)** · cross-stream **SYNCED(FE+BE)** · operation **BLOCK**(push 28 FE+393 BE+QA-B95)

## 1007차 (2026-06-18T12:42 UTC) — merge EXECUTED · post-merge PASS · G15 per-stop form alignment

| 항목 | 값 (1007차) |
|------|-----|
| test HEAD | `7de5a6f` (origin/test `ab4de83`, 28 unpushed) |
| develop HEAD | `7de5a6f` |
| ahead (`test..develop`) | **0** (SYNCED post-merge) |
| develop working tree | **CLEAN** |
| unit test (@test pre-merge) | **1693/1693 PASS** (346 files, 321.83s) |
| unit test (develop HEAD) | **1693/1693 PASS** (346 files, 323.55s; 1st run 1 FAIL flake) |
| unit test (post-merge) | **1693/1693 PASS** (346 files, 324.40s) |
| build | 1050 modules SUCCESS (10.78s) |
| audit | 0 vulnerabilities |
| live E2E (@test) | **122 PASS/19 SKIP** (49 files, 29.80s) |
| route / page | 106 route · 85 page |
| merge commits | `7de5a6f` v1.3-C/G15 align 별지 제22호 per-stop input form with print columns |
| FE merge status | **EXECUTED (local)** |
| cross-stream | BE develop/test `@a179256` SYNCED |
| transfer verdict | **PASS(@test post-merge)** |
| operation | **BLOCK** (origin/test push 28 FE+393 BE + QA-B95) |

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-18T11:48:31+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-18 1005차)

> **1005차 PASS(@test post-merge)+merge EXECUTED(2 FE)** — pre-merge test `@caa215f` **1690/1690 PASS** (321.61s) · develop `@a1d6e32` **1693/1693 PASS** (320.69s) · ★ merge FF `caa215f`→`a1d6e32` (2 commits) · post-merge **1693/1693 PASS** (327.90s) · build **1050 modules** (10.55s) · audit **0** · live E2E **122 PASS/19 SKIP** (29.62s) · develop/test `@a1d6e32` WT **CLEAN** · origin/test `@ab4de83` (**27 unpushed**) · Open **0(active)** · cross-stream **SYNCED(FE)** · BE merge pending **3** · operation **BLOCK**(push 27 FE+389 BE+QA-B95+BE merge pending 3)

## 1005차 (2026-06-18T11:48 UTC) — merge EXECUTED · post-merge PASS · UXD-131 a11y + G15 print layout

| 항목 | 값 (1005차) |
|------|-----|
| test HEAD | `a1d6e32` (origin/test `ab4de83`, 27 unpushed) |
| develop HEAD | `a1d6e32` |
| ahead (`test..develop`) | **0** (SYNCED post-merge) |
| develop working tree | **CLEAN** |
| unit test (@test pre-merge) | **1690/1690 PASS** (346 files, 321.61s) |
| unit test (develop HEAD) | **1693/1693 PASS** (346 files, 320.69s) |
| unit test (post-merge) | **1693/1693 PASS** (346 files, 327.90s) |
| build | 1050 modules SUCCESS (10.55s) |
| audit | 0 vulnerabilities |
| live E2E (@test) | **122 PASS/19 SKIP** (49 files, 29.62s) |
| route / page | 106 route · 84 page |
| merge commits | `7f94654` UXD-131 G41/G21 a11y labels · `a1d6e32` v1.3-C/G15 별지 제22호 pickup address print |
| FE merge status | **EXECUTED (local)** |
| cross-stream | BE develop `@2d98040` / test `@9e050b1` · BE merge pending **3** |
| transfer verdict | **PASS(@test post-merge)** |
| operation | **BLOCK** (origin/test push 27 FE+389 BE + QA-B95 + BE merge pending 3) |

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-18T10:45:40+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-18 1003차)

> **1003차 PASS(@test post-merge)+merge EXECUTED(1 FE)** — pre-merge test `@9e91e6a` **1690/1690 PASS** (320.41s) · develop `@caa215f` **1 FAIL/1689 PASS** (321.23s; flake `CareNursingServiceReportPage`)→rerun **1690/1690 PASS** (326.47s) · ★ merge FF `9e91e6a`→`caa215f` (1 commit) · post-merge **1690/1690 PASS** (324.47s) · build **1049 modules** (7.46s) · audit **0** · live E2E **122 PASS/19 SKIP** (29.45s) · develop/test `@caa215f` WT **CLEAN** · origin/test `@ab4de83` (**25 unpushed**) · Open **0(active)** · cross-stream **SYNCED(FE)** · BE merge pending **1** · operation **BLOCK**(push 25 FE+389 BE+QA-B95+BE merge pending 1)

## 1003차 (2026-06-18T10:45 UTC) — merge EXECUTED · post-merge PASS · G41 PDF 8-7 alerts+export

| 항목 | 값 (1003차) |
|------|-----|
| test HEAD | `caa215f` (origin/test `ab4de83`, 25 unpushed) |
| develop HEAD | `caa215f` |
| ahead (`test..develop`) | **0** (SYNCED post-merge) |
| develop working tree | **CLEAN** |
| unit test (@test pre-merge) | **1690/1690 PASS** (346 files, 320.41s) |
| unit test (develop HEAD) | **1690/1690 PASS** (346 files, 326.47s; 1st run 1 FAIL flake) |
| unit test (post-merge) | **1690/1690 PASS** (346 files, 324.47s) |
| build | 1049 modules SUCCESS (7.46s) |
| audit | 0 vulnerabilities |
| live E2E (@test) | **122 PASS/19 SKIP** (49 files, 29.45s) |
| route / page | 106 route · 85 page |
| merge commits | `caa215f` G41 PDF 8-7 mandatory alerts + 8-7-1 report export |
| FE merge status | **EXECUTED (local)** |
| cross-stream | BE develop `@dac19d3` / test `@9e050b1` · BE merge pending **1** |
| transfer verdict | **PASS(@test post-merge)** |
| operation | **BLOCK** (origin/test push 25 FE+389 BE + QA-B95 + BE merge pending 1) |

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-18T09:54:12+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-18 1001차)

> **1001차 PASS(@test post-merge)+merge EXECUTED(1 FE)** — pre-merge test `@4a112fe` **1685/1685 PASS** (323.06s) · develop `@9e91e6a` **1685/1685 PASS** (320.13s) · ★ merge FF `4a112fe`→`9e91e6a` (1 commit) · post-merge **1685/1685 PASS** (322.46s) · build **1048 modules** (10.19s) · audit **0** · live E2E **122 PASS/19 SKIP** (32.93s) · develop/test `@9e91e6a` WT **CLEAN** · origin/test `@ab4de83` (**24 unpushed**) · Open **0(active)** · cross-stream **SYNCED(BE @9e050b1)** · operation **BLOCK**(push 24 FE+389 BE+QA-B95)

## 1001차 (2026-06-18T09:54 UTC) — merge EXECUTED · post-merge PASS · G41 staff training compliance

| 항목 | 값 (1001차) |
|------|-----|
| test HEAD | `9e91e6a` (origin/test `ab4de83`, 24 unpushed) |
| develop HEAD | `9e91e6a` |
| ahead (`test..develop`) | **0** (SYNCED post-merge) |
| develop working tree | **CLEAN** |
| unit test (@test pre-merge) | **1685/1685 PASS** (345 files, 323.06s) |
| unit test (develop HEAD) | **1685/1685 PASS** (345 files, 320.13s) |
| unit test (post-merge) | **1685/1685 PASS** (345 files, 322.46s) |
| build | 1048 modules SUCCESS (10.19s) |
| audit | 0 vulnerabilities |
| live E2E (@test) | **122 PASS/19 SKIP** (49 files, 32.93s) |
| route / page | 106 route · 84 page |
| merge commits | `9e91e6a` G41 staff training compliance gap dashboard widget |
| FE merge status | **EXECUTED (local)** |
| cross-stream | BE develop/test `@9e050b1` SYNCED (TSR 1000) |
| transfer verdict | **PASS(@test post-merge)** |
| operation | **BLOCK** (origin/test push 24 FE+389 BE + QA-B95) |

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-18T09:13:09+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-18 999차)

> **999차 PASS(@test post-merge)+merge EXECUTED(2 FE)** — pre-merge test `@4a47675` **1683/1683 PASS** (320.28s) · develop `@4a112fe` **1683/1683 PASS** (320.84s) · ★ merge FF `4a47675`→`4a112fe` (2 commits) · post-merge **1683/1683 PASS** (320.53s) · build **1048 modules** (7.53s) · audit **0** · live E2E **122 PASS/19 SKIP** (29.55s) · develop/test `@4a112fe` WT **CLEAN** · origin/test `@ab4de83` (**23 unpushed**) · Open **0(active)** · **★ QA-20260618-B137 Fixed** · cross-stream **SYNCED(BE @1ca6c19)** · operation **BLOCK**(push 23 FE+388 BE+QA-B95)

## 999차 (2026-06-18T09:13 UTC) — merge EXECUTED · post-merge PASS · QA-B137 Fixed

| 항목 | 값 (999차) |
|------|-----|
| test HEAD | `4a112fe` (origin/test `ab4de83`, 23 unpushed) |
| develop HEAD | `4a112fe` |
| ahead (`test..develop`) | **0** (SYNCED post-merge) |
| develop working tree | **CLEAN** |
| unit test (@test pre-merge) | **1683/1683 PASS** (345 files, 320.28s) |
| unit test (develop HEAD) | **1683/1683 PASS** (345 files, 320.84s) |
| unit test (post-merge) | **1683/1683 PASS** (345 files, 320.53s) |
| build | 1048 modules SUCCESS (7.53s) |
| audit | 0 vulnerabilities |
| live E2E (@test) | **122 PASS/19 SKIP** (49 files, 29.55s) |
| route / page | 106 route · 84 page |
| merge commits | `27c9de3` G21 RFID diff compare · `4a112fe` harden rendering |
| FE merge status | **EXECUTED (local)** |
| cross-stream | BE develop/test `@1ca6c19` SYNCED (TSR 998) |
| transfer verdict | **PASS(@test post-merge)** |
| operation | **BLOCK** (origin/test push 23 FE+388 BE + QA-B95) |

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-18T08:26:21+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-18 997차)

> **997차 PASS(@test baseline)+merge pending(1 FE)** — test `@4a47675` **1683/1683 PASS** (319.67s) · build **1047 modules** (7.39s) · audit **0** · live E2E **122 PASS/19 SKIP** (29.17s) · develop `@27c9de3` WT **CLEAN** · test `@4a47675` WT **CLEAN** · `test..develop` **1 ahead** · origin/test `@ab4de83` (**21 unpushed**) · Open **1 BLOCK QA-20260618-B137(active)** · cross-stream **SYNCED(BE @0db1e68 CLEAN)** · operation **BLOCK**(QA-B137+push 21 FE+386 BE+QA-B95)

## 997차 (2026-06-18T08:26 UTC) — revalidation PASS(@test) · merge pending 1 FE

| 항목 | 값 (997차) |
|------|-----|
| test HEAD | `4a47675` (origin/test `ab4de83`, 21 unpushed) |
| develop HEAD | `27c9de3` |
| ahead (`test..develop`) | **1** (`27c9de3` G21 RFID diff compare commit pending merge) |
| develop working tree | **CLEAN** |
| unit test (@test) | **1683/1683 PASS** (345 files, 319.67s) |
| unit test (develop) | 미실행 (develop/test 불일치 상태, `test..develop=1`) |
| build | 1047 modules SUCCESS (7.39s) |
| audit | 0 vulnerabilities |
| live E2E (@test) | **122 PASS/19 SKIP** (49 files, 29.17s) |
| route / page | 106 route · 84 page |
| merge commits | pending: `27c9de3` (`feat(v2/G21): wire RFID plan-vs-tag diff compare on visits page`) |
| FE merge status | **PENDING (1 commit)** |
| cross-stream | BE develop/test `@0db1e68` WT **CLEAN** |
| transfer verdict | **BLOCK(latest develop 미검증)** |
| operation | **BLOCK** (QA-B137+origin/test push 21 FE+386 BE + QA-B95) |

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-18T07:21:20+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-18 993차)

> **993차 PASS(@test post-merge)+merge EXECUTED(2 FE)** — pre-merge test `@1c8f236` **1 FAIL/1676 PASS** (319.26s; flake)→rerun **1677/1677 PASS** (318.33s) · develop `@7424c30` **1678/1678 PASS** (315.99s) · ★ merge FF `1c8f236`→`7424c30` (2 commits) · post-merge **1678/1678 PASS** (320.52s) · build **1047 modules** (10.40s) · audit **0** · live E2E **122 PASS/19 SKIP** (32.20s) · develop/test `@7424c30` WT **CLEAN** · origin/test `@ab4de83` (**20 unpushed**) · Open **0(active)** · cross-stream **SYNCED(BE @eeac205)** · operation **BLOCK**(push 20 FE+385 BE+QA-B95)

## 993차 (2026-06-18T07:21 UTC) — merge EXECUTED · post-merge PASS

| 항목 | 값 (993차) |
|------|-----|
| test HEAD | `7424c30` (origin/test `ab4de83`, 20 unpushed) |
| develop HEAD | `7424c30` |
| ahead (`test..develop`) | **0** (SYNCED post-merge) |
| develop working tree | **CLEAN** |
| unit test (@test pre-merge) | **1677/1677 PASS** (rerun after 1 flake @ `1c8f236`) |
| unit test (post-merge) | **1678/1678 PASS** (344 files, 320.52s) |
| build | 1047 modules SUCCESS (10.40s) |
| audit | 0 vulnerabilities |
| live E2E (@test) | **122 PASS/19 SKIP** (49 files, 32.20s) |
| route / page | 106 route · 84 page |
| merge commits | `bfe0283` UXD-130 driver signature a11y · `7424c30` live-e2e guardian unblock |
| FE merge status | **EXECUTED (local)** |
| cross-stream | BE develop/test `@eeac205` SYNCED (TSR 992) |
| transfer verdict | **PASS(@test post-merge)** |
| operation | **BLOCK** (origin/test push 20 FE+385 BE + QA-B95) |

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-18T06:00:13+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-18 991차)

> **991차 PASS(@test post-merge)+merge EXECUTED(1 FE)** — pre-merge test `@f51e365` carry **1676/1676 PASS** · develop `@1c8f236` **1677/1677 PASS** (317.37s) · ★ merge FF `f51e365`→`1c8f236` (1 commit) · post-merge **1677/1677 PASS** (322.03s) · build **1047 modules** (10.51s) · audit **0** · live E2E **122 PASS/19 SKIP** (32.33s) · develop/test `@1c8f236` WT **CLEAN** · origin/test `@ab4de83` (**18 unpushed**) · Open **0(active)** · cross-stream **SYNCED(BE @d7f1a9a)** · operation **BLOCK**(push 18 FE+384 BE+QA-B95)

## 991차 (2026-06-18T06:00 UTC) — merge EXECUTED · post-merge PASS

| 항목 | 값 (991차) |
|------|-----|
| test HEAD | `1c8f236` (origin/test `ab4de83`, 18 unpushed) |
| develop HEAD | `1c8f236` |
| ahead (`test..develop`) | **0** (SYNCED post-merge) |
| develop working tree | **CLEAN** |
| unit test (@test pre-merge) | carry **1676/1676 PASS** (989차 @ `f51e365`) |
| unit test (post-merge) | **1677/1677 PASS** (344 files, 322.03s) |
| build | 1047 modules SUCCESS (10.51s) |
| audit | 0 vulnerabilities |
| live E2E (@test) | **122 PASS/19 SKIP** (49 files, 32.33s) |
| route / page | 106 route · 84 page |
| merge commits | `1c8f236` meal assistance client normalization |
| FE merge status | **EXECUTED (local)** |
| cross-stream | BE develop/test `@d7f1a9a` SYNCED (TSR 990) |
| transfer verdict | **PASS(@test post-merge)** |
| operation | **BLOCK** (origin/test push 18 FE+384 BE + QA-B95) |

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-18T05:30:12+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-18 989차)

> **989차 PASS(@test post-merge)+merge EXECUTED(2 FE)** — pre-merge test `@b6ce301` **1 FAIL/1675 PASS** (319.43s; flake)→rerun **1676/1676 PASS** (322.85s) · develop `@f51e365` **1676/1676 PASS** (319.98s) · ★ merge FF `b6ce301`→`f51e365` (2 commits) · post-merge **1676/1676 PASS** (318.04s) · build **1046 modules** (11.20s) · audit **0** · live E2E **122 PASS/19 SKIP** (32.07s) · develop/test `@f51e365` WT **CLEAN** · origin/test `@ab4de83` (**17 unpushed**) · Open **0(active)** · cross-stream **BLOCK(BE QA-B135 dirty 3 ahead)** · operation **BLOCK**(push 17 FE+380 BE+QA-B95+QA-B135)

## 989차 (2026-06-18T05:30 UTC) — merge EXECUTED · post-merge PASS

| 항목 | 값 (989차) |
|------|-----|
| test HEAD | `f51e365` (origin/test `ab4de83`, 17 unpushed) |
| develop HEAD | `f51e365` |
| ahead (`test..develop`) | **0** (SYNCED post-merge) |
| develop working tree | **CLEAN** |
| unit test (@test pre-merge) | **1676/1676 PASS** (rerun after 1 flake) |
| unit test (post-merge worktree) | **1676/1676 PASS** (344 files, 318.04s) |
| build | 1046 modules SUCCESS (11.20s) |
| audit | 0 vulnerabilities |
| live E2E (@test) | **122 PASS/19 SKIP** (49 files, 32.07s) |
| route / page | 106 route · 85 page |
| merge commits | `0df6902` legal guide · `f51e365` driver signature |
| FE merge status | **EXECUTED (local)** |
| cross-stream | BE test `@52e3340` · BE develop `@bc3a35c` (**3 ahead DIRTY QA-B135**) |
| transfer verdict | **PASS(@test post-merge)** |
| operation | **BLOCK** (origin/test push 17 FE+380 BE + QA-B95 + QA-B135) |

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-18T04:47:00+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-18 987차)

> **987차 PASS(@test)+merge FULLY UNBLOCKED(1 FE)** — test `@b6ce301` `npm test` **1675/1675 PASS** (316.81s) · build **1046 modules** (7.45s) · audit **0** · live E2E **122 PASS/19 SKIP** (29.38s) · develop `@0df6902` WT **CLEAN** · test `@b6ce301` WT **CLEAN** · `test..develop` **1 ahead** · origin/test `@ab4de83` (**15 unpushed**) · Open **0(active)** · Planned **QA-B116+QA-B95 partial** · cross-stream **BLOCK(BE 3 ahead)** · operation **BLOCK**(push 15 FE+380 BE+QA-B95+BE merge)

## 987차 (2026-06-18T04:47 UTC) — revalidation PASS(@test) · FE merge gate UNBLOCKED

| 항목 | 값 (987차) |
|------|-----|
| test HEAD | `b6ce301` (origin/test `ab4de83`, 15 unpushed) |
| develop HEAD | `0df6902` |
| ahead (`test..develop`) | **1** (`0df6902` legal-guide commit pending merge) |
| develop working tree | **CLEAN** |
| unit test (@test, npm test locked) | **1675/1675 PASS** (344 files, 316.81s) |
| build | 1046 modules SUCCESS (7.45s) |
| audit | 0 vulnerabilities |
| live E2E (@test) | **122 PASS/19 SKIP** (49 files, 29.38s) |
| route / page | 106 route · 84 page |
| FE merge status | **FULLY UNBLOCKED (1 FE pending)** |
| cross-stream | BE test `@52e3340` · BE develop `@bc3a35c` (**3 ahead**) |
| transfer verdict | **PASS(@test)** |
| operation | **BLOCK** (origin/test push 15 FE+380 BE + QA-B95 + BE merge pending 3) |

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-18T04:24:00+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-18 985차)

> **985차 PASS(@test)+BLOCK(transfer develop dirty)** — test `@b6ce301` `npm test` **1674/1674 PASS** (317.19s) · build **1046 modules** (7.42s) · audit **0** · live E2E **122 PASS/19 SKIP** (29.59s) · develop `@b6ce301` WT **DIRTY 2M+1U** (G15 legal guide WIP) · test `@b6ce301` WT **CLEAN** · `test..develop` **0 ahead** · origin/test `@ab4de83` (**15 unpushed**) · Open **1 BLOCK QA-20260618-B134** · cross-stream **BLOCK(BE 2 ahead)** · operation **BLOCK**(QA-B134+push+QA-B95+BE merge)

## 985차 (2026-06-18T04:24 UTC) — revalidation PASS(@test) · develop dirty BLOCK

| 항목 | 값 (985차) |
|------|-----|
| test HEAD | `b6ce301` (origin/test `ab4de83`, 15 unpushed) |
| develop HEAD | `b6ce301` |
| ahead (`test..develop`) | **0** (HEAD SYNCED · develop WT dirty) |
| develop working tree | **DIRTY 2M+1U** — `TransportCompliancePage.jsx` · `TransportCompliancePage.test.jsx` · `TransportServiceLogLegalGuide.jsx`(??) |
| unit test (@test, npm test locked) | **1674/1674 PASS** (343 files, 317.19s) |
| build | 1046 modules SUCCESS (7.42s) |
| audit | 0 vulnerabilities |
| live E2E (@test) | **122 PASS/19 SKIP** (49 files, 29.59s) |
| route / page | 106 route · 84 page |
| FE merge status | **BLOCK** (develop dirty — merge 실행 금지) |
| cross-stream | BE test `@52e3340` · BE develop `@c5dd4f2` (**2 ahead**) |
| transfer verdict | **BLOCK(develop dirty)** · **PASS(@test)** |
| operation | **BLOCK** (QA-B134 + origin/test push 15 FE+380 BE + QA-B95 + BE merge pending) |

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-18T04:00:00+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-18 983차)

> **983차 PASS(transfer)+merge EXECUTED** — pre-merge test `@b4644e8` `npm test` **1 FAIL/1673 PASS** (321.73s; flake `CareServiceSpecialNotesPage`→isolated **3/3 PASS**→rerun **1674/1674 PASS**) · develop `@b6ce301` **1674/1674 PASS** (317.85s) · ★ FF merge `b4644e8`→`b6ce301` (1 commit) · post-merge **1674/1674 PASS** (317.92s) · build **1046 modules** (10.75s) · audit **0** · live E2E **122 PASS/19 SKIP** (32.48s) · develop/test `@b6ce301` WT **CLEAN** · origin/test `@ab4de83` (**15 unpushed**) · Open **0(active)** · cross-stream **BLOCK(BE 1 ahead)** · operation **BLOCK**(push 15 FE+380 BE+QA-B95)

## 983차 (2026-06-18T04:00 UTC) — merge EXECUTED · PASS

| 항목 | 값 (983차) |
|------|-----|
| test HEAD | `b6ce301` (origin/test `ab4de83`, 15 unpushed) |
| develop HEAD | `b6ce301` |
| ahead (`test..develop`) | **0** (SYNCED) |
| merge 커밋 수 | FF merge `b4644e8`→`b6ce301` (1 commit) |
| merge 변경 | `b6ce301` staff health checkup roster → HR file hub (FAQ 21799) |
| unit test (@pre-merge, npm test locked) | **1 FAIL/1673 PASS** (321.73s)→rerun **1674/1674 PASS** (318.31s; flake) |
| develop HEAD unit test | **1674/1674 PASS** (317.85s) |
| unit test (@post-merge) | **1674/1674 PASS** (317.92s) |
| build | 1046 modules SUCCESS (10.75s) |
| audit | 0 vulnerabilities |
| live E2E (@test post-merge) | **122 PASS/19 SKIP** (49 files, 32.48s) |
| route / page | 106 route · 84 page |
| FE merge status | **EXECUTED** (local SYNCED) |
| cross-stream | BE test `@52e3340` · BE develop `@ac1d43f` (**1 ahead**) |
| transfer verdict | **PASS** |
| operation | **BLOCK** (origin/test push 15 FE+380 BE + QA-B95 + BE merge pending) |

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-18T01:54:31+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-18 978차)

> **978차 PASS(transfer)** — test `@40d4284` `npm test` **1670/1670 PASS** (321.33s) · `mvn test` N/A(no `pom.xml`) · build **1046 modules** (7.47s) · audit **0** · live E2E **122 PASS/19 SKIP** (31.20s) · develop `@8e6310a` / test `@40d4284` WT **CLEAN** · `test..develop` **1 ahead** (merge pending 1 FE) · origin/test `@ab4de83` (**10 unpushed**) · Open **0(active)** · operation **BLOCK**(push+QA-B95)

## 978차 (2026-06-18T01:54 UTC) — revalidation PASS · merge pending 1 FE

| 항목 | 값 (978차) |
|------|-----|
| test HEAD | `40d4284` (origin/test `ab4de83`, 10 unpushed) |
| develop HEAD | `8e6310a` |
| ahead (`test..develop`) | **1** (merge FULLY UNBLOCKED) |
| unit test (@test, npm test locked) | **1670/1670 PASS** (321.33s) |
| build | 1046 modules SUCCESS (7.47s) |
| audit | 0 vulnerabilities |
| live E2E (@test) | **122 PASS/19 SKIP** (31.20s) |
| route / page | 106 route · 84 page |
| FE merge status | **UNBLOCKED** (pending 1 FE local merge) |
| cross-stream | BE develop/test `@2e6c35f` SYNCED |
| transfer verdict | **PASS** |
| operation | **BLOCK** (origin/test push 378 BE+10 FE + QA-B95) |

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-18T01:32:00+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-18 976차)

> **976차 PASS(transfer)+merge EXECUTED** — ★ FF merge `101aaee`→`40d4284` (1 commit: QA-B133 DateInput today-label) · post-merge `npm test` **1665/1665 PASS** (315.73s) · build **1046 modules** (7.45s) · audit **0** · live E2E **122 PASS/19 SKIP** (32.40s) · develop/test `@40d4284` WT **CLEAN** · origin/test `@ab4de83` (**10 unpushed**) · Open **0(active)** · operation **BLOCK**(push+QA-B95)

## 976차 (2026-06-18T01:32 UTC) — merge EXECUTED · QA-B133 verified · PASS

| 항목 | 값 (976차) |
|------|-----|
| test HEAD | `40d4284` (origin/test `ab4de83`, 10 unpushed) |
| develop HEAD | `40d4284` |
| ahead (`test..develop`) | **0** (SYNCED) |
| merge 커밋 수 | FF merge `101aaee`→`40d4284` (1 commit) |
| merge 변경 | `DateInput.test.jsx` (today-label selector regex 완화) |
| unit test (@post-merge, npm test locked) | **1665/1665 PASS** (315.73s) |
| pre-merge flake | `CareServiceSpecialNotesPage` 1 FAIL→isolated **3/3 PASS** (post-merge full suite PASS) |
| build | 1046 modules SUCCESS (7.45s) |
| audit | 0 vulnerabilities |
| live E2E (@test post-merge) | **122 PASS/19 SKIP** (49 files, 32.40s) |
| route / page | 106 route · 84 page |
| FE merge status | **EXECUTED** (local SYNCED) |
| cross-stream | BE develop/test `@d02f78a` SYNCED |
| transfer verdict | **PASS** |
| operation | **BLOCK** (origin/test push 10 FE+377 BE + QA-B95) |

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-18T01:00:00+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-18 974차)

> **974차 BLOCK(transfer)+merge EXECUTED** — ★ FF merge `e35efb2`→`101aaee` (1 commit: QA-B132 staff lifecycle test stabilize) · post-merge `npm test` **1664/1665 PASS** (317.35s; FAIL `DateInput` today-label QA-B133) · `StaffLifecyclePanel` isolated **9/9 PASS** · build **1045 modules** (7.50s) · audit **0** · live E2E **122 PASS/19 SKIP** (30.62s) · develop/test `@101aaee` WT **CLEAN** · origin/test `@ab4de83` (**9 unpushed**) · Open **1 MEDIUM QA-B133** · operation **BLOCK**(push+QA-B95+QA-B133)

## 974차 (2026-06-18T01:00 UTC) — merge EXECUTED · QA-B132 verified · QA-B133 Open

| 항목 | 값 (974차) |
|------|-----|
| test HEAD | `101aaee` (origin/test `ab4de83`, 9 unpushed) |
| develop HEAD | `101aaee` |
| ahead (`test..develop`) | **0** (SYNCED) |
| merge 커밋 수 | FF merge `e35efb2`→`101aaee` (1 commit) |
| merge 변경 | `StaffLifecyclePanel.test.jsx` (+25 lines; `vi.setSystemTime` FAQ21806 deadline) |
| unit test (@post-merge, npm test locked) | **1664/1665 PASS** (317.35s; FAIL `DateInput` QA-B133) |
| StaffLifecyclePanel isolated | **9/9 PASS** (QA-B132 verified) |
| build | 1045 modules SUCCESS (7.50s) |
| audit | 0 vulnerabilities |
| live E2E (@test post-merge) | **122 PASS/19 SKIP** (49 files, 30.62s) |
| route / page | 106 route · 84 page |
| FE merge status | **EXECUTED** (local SYNCED) |
| cross-stream | BE develop/test `@4c5d3bc` SYNCED |
| transfer verdict | **BLOCK** (Open QA-B133) |
| operation | **BLOCK** (origin/test push 9 FE+375 BE + QA-B95 + QA-B133) |

---
