<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-15T23:47:18+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-15 822차)

> **post-merge 회귀 검증** — test `@ff9c8c5` (820차 merge 유지) · develop `@8b804fc`(+1: L02_M16 meal preference survey UI) · WT **CLEAN** · `test..develop` **1 ahead** · test `npm test` **1480/1480 PASS** · develop HEAD **1488/1488 PASS** · build 781 modules · live E2E **SKIP** (credentials missing · QA-B95) · Open **0** · cross-stream **FULLY UNBLOCKED** (BE 308 ahead) · verdict **PASS(@test + merge gate)**

| 항목 | 값 (822차 post-merge revalidation) |
|------|-----|
| test HEAD | `ff9c8c5` (820차 merge · 불변) |
| develop HEAD | `8b804fc` (+1 vs `ff9c8c5`: L02_M16 meal preference survey UI wire) |
| ahead (`test..develop`) | **1** |
| test npm test | **1480/1480 PASS** (311 files, 267.21s) |
| develop HEAD npm test | **1488/1488 PASS** (314 files, 270.43s) |
| test build | 781 modules (index 847.46 kB vite warn, 9.79s) |
| test live E2E | **46 suites SKIP/136 skipped** (credentials missing; env PRESENT; backend@8080 UP/200) |
| develop WT | **CLEAN** |
| routes / pages | **99/148** @ develop · **98/146** @ test |
| Open (frontend) | **0** |
| Planned (frontend) | **1** (QA-B95) |
| merge gate (frontend) | **FULLY UNBLOCKED** (1 commit) |
| cross-stream merge | BE `@6da49aa` WT **CLEAN** · Open 0 · 308 ahead |
| merge pending (total) | **309** (308 BE + 1 FE) |
| verdict | **PASS(@test post-merge + merge gate)** |

---
## (이전) 820차 메타 — superseded by 822차

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-15T23:17:37+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-15 820차)

> ★★ **MERGE EXECUTED** — test `@ff9c8c5` (= develop) · 14 commits `4299914`→`ff9c8c5` · WT **CLEAN** · post-merge `npm test` **1479/1480 PASS** (1 flake isolated PASS) · build 781 modules · live E2E **SKIP** (credentials missing · QA-B95) · Open **0** · cross-stream **FULLY UNBLOCKED** (BE 307 ahead) · verdict **PASS(post-merge @ test, 1 flake)**

| 항목 | 값 (820차 post-merge) |
|------|-----|
| test HEAD | `ff9c8c5` (820차 merge 완료) |
| develop HEAD | `ff9c8c5` |
| ahead (`test..develop`) | **0** |
| test npm test | **1479/1480 PASS** (311 files, 261.38s; flake `liveE2eHarness`→isolated 21/21 PASS) |
| test build | 781 modules (index 789.52 kB vite warn, 9.58s) |
| test live E2E | **46 suites SKIP/136 skipped** (credentials missing; env PRESENT; backend@8080 UP/200) |
| develop WT | **CLEAN** |
| routes / pages | **98** / **146** |
| Open (frontend) | **0** |
| Planned (frontend) | **1** (QA-B95) |
| merge gate (frontend) | **MERGED** |
| cross-stream merge | BE `@f33252a` WT **CLEAN** · Open 0 · 307 ahead |
| merge pending (total) | **307** (backend only) |
| verdict | **PASS(post-merge @ test ff9c8c5, 1 flake)** |

---
## (이전) 818차 메타 — superseded by 820차

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-15T22:50:39+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-15 818차)

> **post-merge 회귀 검증** — test `@4299914` (796차 merge 유지) · develop `@49eb944`(+13: `@49eb944` client payload address fixtures · `@40684a9` stabilize care/nursing page tests · prior 11 L02_M06/M17·transport·v1.3-A·L02) · WT **CLEAN** · `test..develop` **13 ahead** · test `npm test` **1444/1444 PASS** (303 files, 261.54s) · develop HEAD **1470/1470 PASS** · build 781 modules · live E2E **SKIP** (credentials missing · QA-B95) · Open **0** · **QA-B105 Fixed @ `49eb944`** · cross-stream **FULLY UNBLOCKED** · verdict **PASS(@test + merge gate)**

| 항목 | 값 (818차 post-merge revalidation) |
|------|-----|
| test HEAD | `4299914` (796차 merge · 불변) |
| develop HEAD | `49eb944` (+13 vs `4299914`: `@49eb944` client payload address fixtures · `@40684a9` stabilize care/nursing page tests · prior 11 L02_M06/M17·transport·v1.3-A·L02) |
| ahead (`test..develop`) | **13** |
| test npm test | **1444/1444 PASS** (303 files, 261.54s) |
| develop HEAD npm test | **1470/1470 PASS** (309 files, 263.60s) |
| test build | 781 modules (index 789.52 kB vite warn, 7.10s) |
| test live E2E | **39 suites SKIP/129 skipped** (credentials missing; env PRESENT; backend@8080 UP/200) |
| develop WT | **CLEAN** |
| routes / pages | **96** / **77** |
| Open (frontend) | **0** (QA-B105 Fixed @ `49eb944`) |
| Planned (frontend) | **1** (QA-B95) |
| merge gate (frontend) | **FULLY UNBLOCKED** (13 commits pending) |
| cross-stream merge | **FULLY UNBLOCKED** (BE `@2cf0908` WT **CLEAN** · Open 0 · 306 ahead) |
| merge pending (total) | **319** (13 FE + 306 BE) — **미실행** |
| verdict | **PASS(@test 4299914 + merge gate)** |

---
## (이전) 816차 메타 — superseded by 818차

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-15T22:27:00+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-15 816차)

> **post-merge 회귀 검증** — test `@4299914` (796차 merge 유지) · develop `@40684a9`(+12: `@40684a9` stabilize care/nursing page tests · prior 11 L02_M06/M17·transport·v1.3-A·L02) · WT **CLEAN** · `test..develop` **12 ahead** · test `npm test` **1444/1444 PASS** (303 files, 257.25s) · develop HEAD **1468/1470 FAIL** (isolated 2 FAIL address guard) · build 781 modules · live E2E **SKIP** (credentials missing · QA-B95) · Open **1 BLOCK QA-B105** · cross-stream **BLOCK** · verdict **PASS(@test) + BLOCK(merge)**

| 항목 | 값 (816차 post-merge revalidation) |
|------|-----|
| test HEAD | `4299914` (796차 merge · 불변) |
| develop HEAD | `40684a9` (+12 vs `4299914`: `@40684a9` stabilize care/nursing page tests · prior 11 L02_M06/M17·transport·v1.3-A·L02) |
| ahead (`test..develop`) | **12** |
| test npm test | **1444/1444 PASS** (303 files, 257.25s) |
| develop HEAD npm test | **1468/1470 FAIL** (309 files, 269.91s; isolated 2 FAIL `clientPayload`·`pilotChecklist`; page tests Fixed @ `40684a9`) |
| test build | 781 modules (index 789.52 kB vite warn, 10.22s) |
| test live E2E | **39 suites SKIP/129 skipped** (credentials missing; env PRESENT; backend@8080 UP/200) |
| develop WT | **CLEAN** |
| routes / pages | **96** / **77** |
| Open (frontend) | **1 BLOCK QA-B105** |
| Planned (frontend) | **1** (QA-B95) |
| merge gate (frontend) | **BLOCK** (develop HEAD unit FAIL · 12 commits pending) |
| cross-stream merge | **BLOCK** (BE `@a25c9de` WT **CLEAN** · Open 0 · 305 ahead) |
| merge pending (total) | **317** (12 FE + 305 BE) — **실행 금지** |
| verdict | **PASS(@test 4299914)** · **BLOCK(merge gate QA-B105)** |

---
## (이전) 814차 메타 — superseded by 816차

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-15T22:00:00+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-15 814차)

> **post-merge 회귀 검증** — test `@4299914` (796차 merge 유지) · develop `@fa20943`(+11: L02_M06/M17 rpt UI · transport a11y · live-e2e env · v1.3-A transport · L02 · a11y · print · pilot E2E) · WT **CLEAN** · `test..develop` **11 ahead** · test `npm test` **1444/1444 PASS** (303 files, 256.71s) · develop HEAD **1465/1470 FAIL** (isolated 3 FAIL) · build 781 modules · live E2E **SKIP** (credentials missing · QA-B95) · Open **1 BLOCK QA-B105** · cross-stream **BLOCK** · verdict **PASS(@test) + BLOCK(merge)**

| 항목 | 값 (814차 post-merge revalidation) |
|------|-----|
| test HEAD | `4299914` (796차 merge · 불변) |
| develop HEAD | `fa20943` (+11 vs `4299914`: L02_M06/M17 rpt UI · transport a11y · v1.3-A · L02 · live-e2e env) |
| ahead (`test..develop`) | **11** |
| test npm test | **1444/1444 PASS** (303 files, 256.71s) |
| develop HEAD npm test | **1465/1470 FAIL** (309 files, 269.84s; isolated 3 FAIL page tests) |
| test build | 781 modules (index 789.52 kB vite warn, 10.51s) |
| test live E2E | **39 suites SKIP/129 skipped** (credentials missing; env PRESENT; backend@8080 UP/200) |
| develop WT | **CLEAN** |
| routes / pages | **96** / **77** |
| Open (frontend) | **1 BLOCK QA-B105** |
| Planned (frontend) | **1** (QA-B95) |
| merge gate (frontend) | **BLOCK** (develop HEAD unit FAIL · 11 commits pending) |
| cross-stream merge | **BLOCK** (BE `@9cc0c1d` WT **CLEAN** · Open 0 · 304 ahead) |
| merge pending (total) | **315** (11 FE + 304 BE) — **실행 금지** |
| verdict | **PASS(@test 4299914)** · **BLOCK(merge gate QA-B105)** |

---
## (이전) 812차 메타 — superseded by 814차

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-15T21:08:00+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-15 812차)

> **post-merge 회귀 검증** — test `@4299914` (796차 merge 유지) · develop `@388e1da`(+9: live-e2e env discovery · v1.3-A transport x3 · L02 · a11y · print · pilot E2E) · WT **CLEAN** · `test..develop` **9 ahead** · test `npm test` **1442/1444 PASS** (303 files, 315.84s; 2 full-suite flakes→isolated 7/7 PASS) · build 781 modules · live E2E **SKIP** (credentials missing · QA-B95) · Open **0** · cross-stream **FULLY UNBLOCKED** · verdict **PASS**

| 항목 | 값 (812차 post-merge revalidation) |
|------|-----|
| test HEAD | `4299914` (796차 merge · 불변) |
| develop HEAD | `388e1da` (+9 vs `4299914`: live-e2e env discovery · v1.3-A transport x3 · L02_M15/M04/M05 · a11y · print · pilot E2E) |
| ahead (`test..develop`) | **9** |
| test npm test | **1442/1444 PASS** (303 files, 315.84s; flakes `CareServiceWeeklyRecordPage`·`NursingVitalCheckPage`→isolated **7/7 PASS**) |
| test build | 781 modules (index 789.52 kB vite warn, 10.59s) |
| test live E2E | **39 suites SKIP/129 skipped** (credentials missing; env PRESENT; backend@8080 UP/200) |
| develop WT | **CLEAN** |
| routes / pages | **94** / **138** |
| Open (frontend) | **0** |
| Planned (frontend) | **1** (QA-B95) |
| merge gate (frontend) | **FULLY_UNBLOCKED** (9 commits pending) |
| cross-stream merge | **FULLY_UNBLOCKED** (BE `@ae7e744` WT **CLEAN** · Open 0 · 303 ahead) |
| merge pending (total) | **312** (9 FE + 303 BE) — **미실행** |
| verdict | **PASS** (post-merge regression @ test 4299914, 2 flakes) |

---
## (이전) 810차 메타 — superseded by 812차

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-15T20:40:00+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-15 810차)

> **post-merge 회귀 검증** — test `@4299914` (796차 merge 유지) · develop `@d46688d`(+8: v1.3-A transport x3·L02_M15/M04/M05·a11y·print·pilot E2E) · WT **CLEAN** · `test..develop` **8 ahead** · test `npm test` **1444/1444 PASS** (303 files, 332.67s) · build 781 modules · live E2E **SKIP** (credentials missing · QA-B95) · Open **0** · cross-stream **FULLY UNBLOCKED** · verdict **PASS**

| 항목 | 값 (810차 post-merge revalidation) |
|------|-----|
| test HEAD | `4299914` (796차 merge · 불변) |
| develop HEAD | `d46688d` (+8 vs `4299914`: transport x3 · L02 · a11y · print · pilot E2E) |
| ahead (`test..develop`) | **8** |
| test npm test | **1444/1444 PASS** (303 files, 332.67s) |
| test build | 781 modules (index 789.52 kB vite warn, 8.71s) |
| test live E2E | **39 suites SKIP/129 skipped** (credentials missing; env PRESENT; backend@8080 UP/200) |
| develop WT | **CLEAN** |
| routes / pages | **94** / **138** |
| Open (frontend) | **0** |
| Planned (frontend) | **1** (QA-B95) |
| merge gate (frontend) | **FULLY_UNBLOCKED** (8 commits pending) |
| cross-stream merge | **FULLY_UNBLOCKED** (BE `@3eeac92` WT **CLEAN** · Open 0 · 302 ahead) |
| merge pending (total) | **310** (8 FE + 302 BE) — **미실행** |
| verdict | **PASS** (post-merge regression @ test 4299914) |

---
## (이전) 808차 메타 — superseded by 810차

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-15T20:16:52+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-15 808차)

> **post-merge 회귀 검증** — test `@4299914` (796차 merge 유지) · develop `@15e9b64`(+7: v1.3-A transport·L02·a11y·print·pilot E2E) · WT **DIRTY 2M+1U** · `test..develop` **7 ahead** · test `npm test` **1443/1444 FAIL** (`NursingServiceRecordPage`; develop 4/4 PASS) · build 781 modules · live E2E **SKIP** (credentials missing · QA-B95) · Open **QA-B102 BLOCK + QA-B104 HIGH** · cross-stream **BLOCK(QA-B103)** · verdict **BLOCK**

| 항목 | 값 (808차 post-merge revalidation) |
|------|-----|
| test HEAD | `4299914` (796차 merge · 불변) |
| develop HEAD | `15e9b64` (+7 vs `4299914`: v1.3-A transport x2 · L02_M15/M04/M05 · a11y · print · pilot E2E) |
| ahead (`test..develop`) | **7** |
| test npm test | **1443/1444 FAIL** (303 files, 293.68s; `NursingServiceRecordPage.test.jsx:74`; isolated 3/4 FAIL) |
| develop npm test (spot) | `NursingServiceRecordPage` **4/4 PASS** @ `15e9b64` |
| test build | 781 modules (index 789.52 kB vite warn, 10.71s) |
| test live E2E | **39 suites SKIP/129 skipped** (credentials missing; env PRESENT; backend@8080 UP/401) |
| develop WT | **DIRTY 2M+1U** (`KakaoTransportMap.jsx` · `TransportRunNewPage.jsx` · `src/lib/`) |
| routes / pages | **93** / **75** |
| Open (frontend) | **2** (QA-B102 BLOCK · QA-B104 HIGH) |
| Planned (frontend) | **1** (QA-B95) |
| merge gate (frontend) | **BLOCK** (develop dirty + 7 commits pending) |
| cross-stream merge | **BLOCK** (BE `@e8b8398` WT **DIRTY 14M+3D+1U** · Open **QA-B103** · 301 ahead) |
| merge pending (total) | **308** (7 FE + 301 BE) — **실행 금지** |
| verdict | **BLOCK** (@test FAIL + merge gate dirty) |

---
## (이전) 804차 메타 — superseded by 808차

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-15T19:35:00+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-15 804차)

> **post-merge 회귀 검증** — test `@4299914` (796차 merge 유지) · develop `@46971e1`(+5: L02_M15·L02_M04/M05 UI·a11y·print·pilot E2E) · WT **CLEAN** · `test..develop` **5 ahead** · test `npm test` **1443/1444 PASS** (303 files, 279.61s; flake `BodyRestraintRecordPage`→isolated 3/3 PASS) · live E2E **미실행** (backend UP/200 · QA-B95) · Open **0** · Planned **1 QA-B95** · cross-stream **BLOCK(QA-B101)** · verdict **PASS**

| 항목 | 값 (804차 post-merge revalidation) |
|------|-----|
| test HEAD | `4299914` (796차 merge · 불변) |
| develop HEAD | `46971e1` (+5 vs `4299914`: `3549896` L02_M15 · `c5f82a6` L02_M04/M05 UI · `07f6afa` a11y · `d2145b0` print · `46971e1` pilot E2E) |
| ahead (`test..develop`) | **5** |
| test npm test | **1443/1444 PASS** (303 files, 279.61s; flake `BodyRestraintRecordPage`→isolated **3/3 PASS**) |
| test build | 781 modules (index 789.52 kB vite warn, 8.29s) |
| test live E2E | **미실행** (backend@8080 UP/200; env PRESENT; QA-B95 Planned) |
| develop WT | **CLEAN** |
| routes / pages | **93** / **138** |
| Open (frontend) | **0** |
| Planned (frontend) | **1** (QA-B95) |
| merge gate (frontend) | **FULLY UNBLOCKED** (5 commits pending) |
| cross-stream merge | **BLOCK** (BE `@27b40cd` WT **DIRTY 9M+1U** · Open **1 QA-B101** · 300 ahead) |
| merge pending (total) | **305** (5 FE + 300 BE) — **실행 금지** |
| verdict | **PASS** (post-merge regression @ test, 1 flake) |

---
## (이전) 802차 메타 — superseded by 804차

> test `@4299914` · develop `@d2145b0`(+4) · 4 ahead · 1444/1444 PASS · merge pending **304**

| 항목 | 값 (802차 post-merge revalidation) |
|------|-----|
| test HEAD | `4299914` (796차 merge · 불변) |
| develop HEAD | `d2145b0` (+4 vs `4299914`: `3549896` L02_M15 · `c5f82a6` L02_M04/M05 UI · `07f6afa` a11y · `d2145b0` print output) |
| ahead (`test..develop`) | **4** |
| test npm test | **1444/1444 PASS** (303 files, 266.92s) |
| test build | 781 modules (index 789.52 kB vite warn, 7.19s) |
| test live E2E | **미실행** (backend@8080 UP/401; env PRESENT; QA-B95 Planned) |
| develop WT | **CLEAN** |
| routes / pages | **94** / **138** |
| Open (frontend) | **0** |
| Planned (frontend) | **1** (QA-B95) |
| merge gate (frontend) | **FULLY UNBLOCKED** (4 commits pending) |
| cross-stream merge | **BLOCK** (BE `@27b40cd` WT **DIRTY 9M+1U** · Open **1 QA-B101** · 300 ahead) |
| merge pending (total) | **304** (4 FE + 300 BE) — **실행 금지** |
| verdict | **PASS** (post-merge regression @ test) |

---
## (이전) 800차 메타 — superseded by 802차

> test `@4299914` · develop `@c5f82a6`(+2) · 2 ahead · 1444/1444 PASS · merge pending **301**

| 항목 | 값 (800차 post-merge revalidation) |
|------|-----|
| test HEAD | `4299914` (796차 merge · 불변) |
| develop HEAD | `c5f82a6` (+2 vs `4299914`: `3549896` L02_M15 · `c5f82a6` L02_M04/M05) |
| ahead (`test..develop`) | **2** |
| test npm test | **1444/1444 PASS** (303 files, 252.93s) |
| test build | 781 modules (index 789.52 kB vite warn, 6.91s) |
| test live E2E | **39 suites SKIP / 129 skipped** (backend@8080 DOWN; env PRESENT; QA-B95 Planned) |
| develop WT | **CLEAN** |
| routes / pages | **93** / **138** |
| Open (frontend) | **0** |
| Planned (frontend) | **1** (QA-B95) |
| merge gate (frontend) | **FULLY UNBLOCKED** (2 commits pending) |
| cross-stream merge | **FULLY UNBLOCKED** (BE `@c655743` WT **CLEAN** · 299 ahead · Open 0) |
| merge pending (total) | **301** (2 FE + 299 BE) |
| verdict | **PASS** (post-merge regression @ test) |

---
## (이전) 798차 메타 — superseded by 800차

> test `@4299914` · develop `@3549896`(+1) · 1 ahead · 1444/1444 PASS · merge pending **299**

| 항목 | 값 (798차 post-merge revalidation) |
|------|-----|
| test HEAD | `4299914` (796차 merge · 불변) |
| develop HEAD | `3549896` (+1 vs `4299914`: L02_M15 special notes UI) |
| ahead (`test..develop`) | **1** |
| test npm test | **1444/1444 PASS** (303 files, 250.38s) |
| test build | 781 modules (max 367.09 kB, 10.07s) |
| test live E2E | **39 suites SKIP / 129 skipped** (backend@8080 DOWN; env PRESENT; QA-B95 Planned) |
| develop WT | **CLEAN** |
| routes / pages | **91** / **136** |
| Open (frontend) | **0** |
| Planned (frontend) | **1** (QA-B95) |
| merge gate (frontend) | **FULLY UNBLOCKED** (1 commit pending) |
| cross-stream merge | **FULLY UNBLOCKED** (BE `@221bde7` WT **CLEAN** · 298 ahead · Open 0) |
| merge pending (total) | **299** (1 FE + 298 BE) |
| verdict | **PASS** (post-merge regression @ test) |

---
## (이전) 796차 메타 — merge executed

> ★★ **MERGE EXECUTED** — develop→test `c7c8f07`→`4299914` (**360 commits** · fast-forward clean · **0 conflicts**) · **origin/test PUSH 완료** (`c7c8f07..4299914`) · test=develop 동기화 · post-merge `npm test` **1444/1444 PASS** (303 files, 248.02s) · `test..develop` **0 ahead** · Open 0 · Planned 1 QA-B95 · operation **BLOCK**(QA-B95)

| 항목 | 값 (796차 post-merge) |
|------|-----|
| merge | **EXECUTED** `c7c8f07` → `4299914` (360 commits, fast-forward, 0 conflicts) |
| origin/test | **PUSH 완료** (`c7c8f07..4299914`) |
| test HEAD (post-merge) | `4299914` (= develop) |
| develop HEAD | `4299914` (+1 vs `3a14caf`: live-e2e auth probe failure handling) |
| ahead (`test..develop`) | **0** (merge 완료) |
| test npm test (post-merge) | **1444/1444 PASS** (303 files, 248.02s) |
| test mvn test | N/A (`pom.xml` 없음) |
| test live E2E | 불가/skip (backend@8080 DOWN; env PRESENT; credentials missing; QA-B95 Planned) |
| 교차 BE | develop `@a06a29a` test `@598d108` · 297 ahead · **BE merge 미실행** (별도 사이클) |
| verdict | **PASS — frontend 이관 COMPLETE** (planner 146차 "tester merge" P0 해소) |

---
## (이전) 794차 메타 — superseded by 796차 merge

> test `@c7c8f07` 불변 · develop `@3a14caf`(+1) · WT **CLEAN** · merge pending **655** (359 FE + 296 BE) · ★ **cross-stream FULLY UNBLOCKED** · merge **미실행** · operation **BLOCK**(QA-B95)

| 항목 | 값 |
|------|-----|
| test HEAD | `c7c8f07` |
| develop HEAD | `3a14caf` |
| ahead (`test..develop`) | 359 |
| test npm test | **217/217 PASS** (70 files, 52.26s) |
| test mvn test | N/A (`pom.xml` 없음) |
| test build | 781 modules (max 367.09 kB, 5.01s) |
| test live E2E | **4 suites FAIL / 18 skipped** (LIVE_E2E credentials missing; env PRESENT; backend DOWN; QA-B95 Planned) |
| develop HEAD test | **미재실행** (792 carry **1424/1424 PASS**) |
| develop WT | **CLEAN** |
| audit | 0 (prod omit=dev) |
| routes / pages | **91** / **71** |
| Open (frontend) | **0** |
| Planned (frontend) | **1** (QA-20260615-B95 live E2E env+credentials+backend) |
| merge gate (frontend) | **FULLY UNBLOCKED** |
| cross-stream merge | **FULLY UNBLOCKED** (BE `@59c5d16` WT **CLEAN** · Open 0 · test 246/246 PASS) |
| merge pending (total) | **655** (359 FE + 296 BE) |

### TSR 794차 vs 792차

| 항목 | 792차 | 794차 |
|------|-------|-------|
| develop HEAD | `9ad8346` (+1) | **`3a14caf`**(+1) |
| develop WT | CLEAN | **CLEAN** |
| ahead (FE) | 358 | **359** |
| test npm test | 217/217 PASS (56.79s) | **217/217 PASS** (52.26s) |
| Open | 0 | **0** |
| merge gate | FULLY UNBLOCKED | **FULLY UNBLOCKED** |
| cross-stream BE | `@81a2223` 295 ahead | **`@59c5d16` 296 ahead** |
| merge pending | 653 | **655** |

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-15T17:07:30+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-15 792차)

> test `@c7c8f07` 불변 · develop `@9ad8346`(+1) · WT **CLEAN** · merge pending **653** (358 FE + 295 BE) · ★ **cross-stream FULLY UNBLOCKED** · merge **미실행** · operation **BLOCK**(QA-B95)

| 항목 | 값 |
|------|-----|
| test HEAD | `c7c8f07` |
| develop HEAD | `9ad8346` |
| ahead (`test..develop`) | 358 |
| test npm test | **217/217 PASS** (70 files, 56.79s) |
| test mvn test | N/A (`pom.xml` 없음) |
| test build | 781 modules (max 367.09 kB, 5.11s) |
| test live E2E | **4 suites FAIL / 18 skipped** (LIVE_E2E credentials missing; env PRESENT; backend DOWN; QA-B95 Planned) |
| develop HEAD test | **미재실행** (790 carry **1424/1424 PASS**) |
| develop WT | **CLEAN** |
| audit | 0 (prod omit=dev) |
| routes / pages | **90** / **71** |
| Open (frontend) | **0** |
| Planned (frontend) | **1** (QA-20260615-B95 live E2E env+credentials+backend) |
| merge gate (frontend) | **FULLY UNBLOCKED** |
| cross-stream merge | **FULLY UNBLOCKED** (BE `@81a2223` WT **CLEAN** · Open 0 · test 246/246 PASS) |
| merge pending (total) | **653** (358 FE + 295 BE) |

### TSR 792차 vs 790차

| 항목 | 790차 | 792차 |
|------|-------|-------|
| develop HEAD | `15b09df` (+1) | **`9ad8346`**(+1) |
| develop WT | DIRTY 1M | **CLEAN** |
| ahead (FE) | 357 | **358** |
| test npm test | 217/217 PASS (51.11s) | **217/217 PASS** (56.79s) |
| Open | 1 BLOCK QA-B100 | **0** |
| QA-B100 | Open BLOCK | **Fixed @ `9ad8346`** |
| merge gate | BLOCK | **FULLY UNBLOCKED** |
| cross-stream BE | `@e4c240f` 294 ahead | **`@81a2223` 295 ahead** |
| merge pending | 651 | **653** |

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-15T16:36:50+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-15 790차)

> test `@c7c8f07` 불변 · develop `@15b09df`(+1) · WT **DIRTY 1M** · merge pending **651** (357 FE + 294 BE) · ⚠ **cross-stream BLOCK** · merge **실행 금지** · operation **BLOCK**(QA-B100+QA-B95)

| 항목 | 값 |
|------|-----|
| test HEAD | `c7c8f07` |
| develop HEAD | `15b09df` |
| ahead (`test..develop`) | 357 |
| test npm test | **217/217 PASS** (70 files, 51.11s) |
| test mvn test | N/A (`pom.xml` 없음) |
| test build | 781 modules (max 367.09 kB, 6.52s) |
| test live E2E | **4 suites FAIL / 18 skipped** (LIVE_E2E config incomplete; env file PRESENT; backend DOWN; QA-B95 Planned) |
| develop HEAD test | **미재실행** (788 carry **1424/1424 PASS**) |
| develop WT | **DIRTY 1M** (`liveE2eSuiteGuard.test.js`) |
| audit | 0 (prod omit=dev) |
| routes / pages | **90** / **71** |
| Open (frontend) | **1 BLOCK QA-B100** |
| Planned (frontend) | **1** (QA-20260615-B95 live E2E env+credentials+backend) |
| merge gate (frontend) | **BLOCK** |
| cross-stream merge | **BLOCK** (BE `@e4c240f` WT **CLEAN** · Open 0 · test 246/246 PASS) |
| merge pending (total) | **651** (357 FE + 294 BE) |

### TSR 790차 vs 788차

| 항목 | 788차 | 790차 |
|------|-------|-------|
| develop HEAD | `61141a6` (+1) | **`15b09df`**(+1) |
| develop WT | CLEAN | **DIRTY 1M** |
| ahead (FE) | 356 | **357** |
| test npm test | 217/217 PASS (50.99s) | **217/217 PASS** (51.11s) |
| Open | 0 | **1 BLOCK QA-B100** |
| merge gate | FULLY UNBLOCKED | **BLOCK** |
| cross-stream BE | `@de25b3e` 293 ahead | **`@e4c240f` 294 ahead** |
| merge pending | 649 | **651** |

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-15T15:58:16+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-15 788차)

> test `@c7c8f07` 불변 · develop `@61141a6`(+1) · WT **CLEAN** · merge pending **649** (356 FE + 293 BE) · ★ **cross-stream FULLY UNBLOCKED** · merge **미실행** · operation **BLOCK**(QA-B95)

| 항목 | 값 |
|------|-----|
| test HEAD | `c7c8f07` |
| develop HEAD | `61141a6` |
| ahead (`test..develop`) | 356 |
| test npm test | **217/217 PASS** (70 files, 50.99s) |
| test mvn test | N/A (`pom.xml` 없음) |
| test build | 781 modules (max 367.09 kB, 6.17s) |
| test live E2E | **4 suites FAIL / 18 skipped** (LIVE_E2E config incomplete; env file PRESENT; backend DOWN; QA-B95 Planned) |
| develop HEAD test | **미재실행** (786 carry **1424/1424 PASS**) |
| develop WT | **CLEAN** |
| audit | 0 (prod omit=dev) |
| routes / pages | **86** / **68** |
| Open (frontend) | **0** |
| Planned (frontend) | **1** (QA-20260615-B95 live E2E env+credentials+backend) |
| merge gate (frontend) | **FULLY UNBLOCKED** |
| cross-stream merge | **FULLY UNBLOCKED** (BE `@de25b3e` WT **CLEAN** · Open 0 · test 246/246 PASS) |
| merge pending (total) | **649** (356 FE + 293 BE) |

### TSR 788차 vs 786차

| 항목 | 786차 | 788차 |
|------|-------|-------|
| develop HEAD | `1fd1434` (+1) | **`61141a6`**(+1) |
| develop WT | CLEAN | **CLEAN** |
| ahead (FE) | 355 | **356** |
| test npm test | 217/217 PASS (115.31s) | **217/217 PASS** (50.99s) |
| develop HEAD test | 미재실행 (784 carry) | **미재실행** (786 carry) |
| live E2E env | PRESENT (not sourced @ test HEAD) | **PRESENT** |
| cross-stream BE | `@344a28b` 292 ahead | **`@de25b3e` 293 ahead** |
| merge pending | 647 | **649** |
| Open | 0 | **0** |
| merge gate | FULLY UNBLOCKED | **FULLY UNBLOCKED** |

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-15T15:38:08+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-15 786차)

> test `@c7c8f07` 불변 · develop `@1fd1434`(+1) · WT **CLEAN** · merge pending **647** (355 FE + 292 BE) · ★ **cross-stream FULLY UNBLOCKED** · merge **미실행** · operation **BLOCK**(QA-B95)

| 항목 | 값 |
|------|-----|
| test HEAD | `c7c8f07` |
| develop HEAD | `1fd1434` |
| ahead (`test..develop`) | 355 |
| test npm test | **217/217 PASS** (70 files, 115.31s) |
| test mvn test | N/A (`pom.xml` 없음) |
| test build | 781 modules (max 367.09 kB, 7.89s) |
| test live E2E | **4 suites FAIL / 18 skipped** (LIVE_E2E config incomplete; env file PRESENT repo root not sourced; backend DOWN; QA-B95 Planned) |
| develop HEAD test | **미재실행** (784 carry **1424/1424 PASS**) |
| develop WT | **CLEAN** |
| audit | 0 (prod omit=dev) |
| routes / pages | **86** / **68** |
| Open (frontend) | **0** |
| Planned (frontend) | **1** (QA-20260615-B95 live E2E env+credentials+backend) |
| merge gate (frontend) | **FULLY UNBLOCKED** |
| cross-stream merge | **FULLY UNBLOCKED** (BE `@344a28b` WT **CLEAN** · Open 0 · test 246/246 PASS) |
| merge pending (total) | **647** (355 FE + 292 BE) |

### TSR 786차 vs 784차

| 항목 | 784차 | 786차 |
|------|-------|-------|
| develop HEAD | `950415d` (+1) | **`1fd1434`**(+1) |
| develop WT | CLEAN | **CLEAN** |
| ahead (FE) | 354 | **355** |
| test npm test | 217/217 PASS (50.70s) | **217/217 PASS** (115.31s) |
| develop HEAD test | 1424/1424 PASS | **미재실행** (784 carry) |
| live E2E env | ABSENT | **PRESENT**(repo root, not sourced @ test HEAD) |
| cross-stream BE | `@47a4e25` 291 ahead | **`@344a28b` 292 ahead** |
| merge pending | 645 | **647** |
| Open | 0 | **0** |
| merge gate | FULLY UNBLOCKED | **FULLY UNBLOCKED** |

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-15T15:14:31+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-15 784차)

> test `@c7c8f07` 불변 · develop `@950415d`(+1) · WT **CLEAN** · merge pending **645** (354 FE + 291 BE) · ★ **cross-stream FULLY UNBLOCKED** · merge **미실행** · operation **BLOCK**(QA-B95)

| 항목 | 값 |
|------|-----|
| test HEAD | `c7c8f07` |
| develop HEAD | `950415d` |
| ahead (`test..develop`) | 354 |
| test npm test | **217/217 PASS** (70 files, 50.70s) |
| test mvn test | N/A (`pom.xml` 없음) |
| test build | 781 modules (max 367.09 kB, 10.34s) |
| test live E2E | **4 suites FAIL / 18 skipped** (LIVE_E2E config incomplete; env file ABSENT; backend DOWN; QA-B95 Planned) |
| develop HEAD test | **1424/1424 PASS** (299 files, 248.30s) |
| develop WT | **CLEAN** |
| audit | 0 (prod omit=dev) |
| routes / pages | **86** / **68** |
| Open (frontend) | **0** |
| Planned (frontend) | **1** (QA-20260615-B95 live E2E env+credentials+backend) |
| merge gate (frontend) | **FULLY UNBLOCKED** |
| cross-stream merge | **FULLY UNBLOCKED** (BE `@47a4e25` WT **CLEAN** · Open 0 · test 246/246 PASS) |
| merge pending (total) | **645** (354 FE + 291 BE) |

### TSR 784차 vs 782차

| 항목 | 782차 | 784차 |
|------|-------|-------|
| develop HEAD | `41b2123` (+1) | **`950415d`**(+1) |
| develop WT | CLEAN | **CLEAN** |
| ahead | 353 | **354** |
| test npm test | 217/217 (51.42s) | **217/217 (50.70s)** |
| test build | 781 modules (4.88s) | **781 modules (10.34s)** |
| develop HEAD test | 미재실행 | **1424/1424 PASS** (299 files, 248.30s) |
| live E2E | 4 suites FAIL / 18 skipped | **동일** (env ABSENT, backend DOWN) |
| cross-stream BE | `@e703252` · 290 ahead | **`@47a4e25` · 291 ahead** |
| merge pending | 643 | **645** |
| operation | BLOCK(QA-B95) | **BLOCK(QA-B95)** |

# develop ↔ test diff 메타 — frontend (2026-06-15 782차)

> test `@c7c8f07` 불변 · develop `@41b2123`(+1) · WT **CLEAN** · merge pending **643** (353 FE + 290 BE) · ★ **cross-stream FULLY UNBLOCKED** · merge **미실행** · operation **BLOCK**(QA-B95)

| 항목 | 값 |
|------|-----|
| test HEAD | `c7c8f07` |
| develop HEAD | `41b2123` |
| ahead (`test..develop`) | 353 |
| test npm test | **217/217 PASS** (70 files, 51.42s) |
| test mvn test | N/A (`pom.xml` 없음) |
| test build | 781 modules (max 367.09 kB, 4.88s) |
| test live E2E | **4 suites FAIL / 18 skipped** (LIVE_E2E config incomplete; env file PRESENT; QA-B95 Planned) |
| develop HEAD test | **미재실행** (782차 test WT 실측 217/217 PASS) |
| develop WT | **CLEAN** |
| audit | 0 (prod omit=dev) |
| routes / pages | **86** / **68** |
| Open (frontend) | **0** |
| Planned (frontend) | **1** (QA-20260615-B95 live E2E env+credentials+backend) |
| merge gate (frontend) | **FULLY UNBLOCKED** |
| cross-stream merge | **FULLY UNBLOCKED** (BE `@e703252` WT **CLEAN** · Open 0 · test 246/246 PASS) |
| merge pending (total) | **643** (353 FE + 290 BE) |

### TSR 782차 vs 780차

| 항목 | 780차 | 782차 |
|------|-------|-------|
| develop HEAD | `7faccbd` (+1) | **`41b2123`**(+1) |
| develop WT | CLEAN | **CLEAN** |
| ahead | 352 | **353** |
| test npm test | 217/217 (52.52s) | **217/217 (51.42s)** |
| test build | 781 modules (5.24s) | **781 modules (4.88s)** |
| live E2E | 4 suites FAIL / 18 skipped | **동일** (credentials incomplete, env PRESENT) |
| cross-stream BE | `@13b8a37` · 289 ahead | **`@e703252` · 290 ahead** |
| merge pending | 641 | **643** |
| operation | BLOCK(QA-B95) | **BLOCK(QA-B95)** |

# develop ↔ test diff 메타 — frontend (2026-06-15 780차)

> test `@c7c8f07` 불변 · develop `@7faccbd`(+1) · WT **CLEAN** · merge pending **641** (352 FE + 289 BE) · ★ **cross-stream FULLY UNBLOCKED** · merge **미실행** · operation **BLOCK**(QA-B95)

| 항목 | 값 |
|------|-----|
| test HEAD | `c7c8f07` |
| develop HEAD | `7faccbd` |
| ahead (`test..develop`) | 352 |
| test npm test | **217/217 PASS** (70 files, 52.52s) |
| test build | 781 modules (max 367.09 kB, 5.24s) |
| test live E2E | **4 suites FAIL / 18 skipped** (LIVE_E2E credentials missing; `scripts/dev-live-e2e.env` **PRESENT**(not sourced); backend **DOWN**; QA-B95 Planned) |
| develop HEAD test | **미재실행** (780차 test WT 실측 217/217 PASS) |
| develop WT | **CLEAN** |
| audit | 0 (prod omit=dev) |
| routes / pages | **86** / **68** |
| Open (frontend) | **0** |
| Planned (frontend) | **1** (QA-20260615-B95 live E2E env+credentials+backend) |
| merge gate (frontend) | **FULLY UNBLOCKED** |
| cross-stream merge | **FULLY UNBLOCKED** (BE `@13b8a37` WT **CLEAN** · Open 0 · test 246/246 PASS) |
| merge pending (total) | **641** (352 FE + 289 BE) |

### TSR 780차 vs 778차

| 항목 | 778차 | 780차 |
|------|-------|-------|
| develop HEAD | `e6944f1` (+2) | **`7faccbd`**(+1) |
| develop WT | CLEAN (QA-B99 Fixed) | **CLEAN** |
| ahead | 351 | **352** |
| test npm test | 217/217 (51.09s) | **217/217 (52.52s)** |
| live E2E | env ABSENT · credentials missing | **env PRESENT(not sourced)** · credentials missing |
| cross-stream BE | `@3a2e82e` · 288 ahead | **`@13b8a37` · 289 ahead** |
| merge pending | 639 | **641** |
| operation | BLOCK(QA-B95) | **BLOCK(QA-B95)** |

# develop ↔ test diff 메타 — frontend (2026-06-15 778차)

> test `@c7c8f07` 불변 · develop `@e6944f1`(+2) · WT **CLEAN** · merge pending **639** (351 FE + 288 BE) · ★ **cross-stream FULLY UNBLOCKED** · merge **미실행** · operation **BLOCK**(QA-B95)

| 항목 | 값 |
|------|-----|
| test HEAD | `c7c8f07` |
| develop HEAD | `e6944f1` |
| ahead (`test..develop`) | 351 |
| test npm test | **217/217 PASS** (70 files, 51.09s) |
| test build | 781 modules (max 367.09 kB, 6.08s) |
| test live E2E | **4 suites FAIL / 18 skipped** (LIVE_E2E credentials missing; `scripts/dev-live-e2e.env` **ABSENT**; backend **DOWN**; QA-B95 Planned) |
| develop HEAD test | **미재실행** (778차 test WT 실측 217/217 PASS) |
| develop WT | **CLEAN** |
| audit | 0 (prod omit=dev) |
| routes / pages | **86** / **68** |
| Open (frontend) | **0** |
| Planned (frontend) | **1** (QA-20260615-B95 live E2E env+credentials+backend) |
| merge gate (frontend) | **FULLY UNBLOCKED** |
| cross-stream merge | **FULLY UNBLOCKED** (BE `@3a2e82e` WT **CLEAN** · Open 0 · test 246/246 PASS) |
| merge pending (total) | **639** (351 FE + 288 BE) |

### TSR 778차 vs 776차

| 항목 | 776차 | 778차 |
|------|-------|-------|
| develop HEAD | `6f53978` (불변) | **`e6944f1`**(+2) |
| develop WT | DIRTY 3M (QA-B99) | **CLEAN** (QA-B99 Fixed) |
| ahead | 349 | **351** |
| test npm test | 217/217 (51.65s) | **217/217 (51.09s)** |
| live E2E | env PRESENT · credentials missing | **env ABSENT** · credentials missing |
| Open (frontend) | 1 BLOCK QA-B99 | **0** |
| merge gate | BLOCK | **FULLY UNBLOCKED** |
| cross-stream | BLOCK | **FULLY UNBLOCKED** |

# develop ↔ test diff 메타 — frontend (2026-06-15 776차)

> test `@c7c8f07` 불변 · develop `@6f53978` HEAD 불변 · WT **DIRTY 3M** · merge pending **636** (349 FE + 287 BE) · ⚠ **cross-stream BLOCK** · merge **실행 금지** · operation **BLOCK**(QA-B99+QA-B95)

| 항목 | 값 |
|------|-----|
| test HEAD | `c7c8f07` |
| develop HEAD | `6f53978` |
| ahead (`test..develop`) | 349 |
| test npm test | **217/217 PASS** (70 files, 51.65s) |
| test build | 781 modules (max 367.09 kB, 6.29s) |
| test live E2E | **4 suites FAIL / 18 skipped** (LIVE_E2E credentials missing; `scripts/dev-live-e2e.env` **PRESENT**; backend **DOWN**; QA-B95 Planned) |
| develop HEAD test | **미재실행** (776차 test WT 실측 217/217 PASS) |
| develop WT | **DIRTY 3M** (`liveConfig.js`·`liveDescribe.js`·`liveGlobalSetup.js`) |
| audit | 0 (prod omit=dev) |
| routes / pages | **86** / **68** |
| Open (frontend) | **1 BLOCK QA-B99** |
| Planned (frontend) | **1** (QA-20260615-B95 live E2E env+credentials+backend) |
| merge gate (frontend) | **BLOCK** |
| cross-stream merge | **BLOCK** (BE `@18ff83e` WT **CLEAN** · Open 0 · test 246/246 PASS) |
| merge pending (total) | **636** (349 FE + 287 BE) |

### TSR 776차 vs 774차

| 항목 | 774차 | 776차 |
|------|-------|-------|
| develop HEAD | `6f53978` | **`6f53978`** (불변) |
| develop WT | CLEAN | **DIRTY 3M** (QA-B99) |
| ahead | 349 | **349** |
| test npm test | 217/217 (52.07s) | **217/217 (51.65s)** |
| live E2E | env ABSENT | **env PRESENT** · credentials missing |
| Open (frontend) | 0 | **1 BLOCK QA-B99** |
| merge gate | FULLY UNBLOCKED | **BLOCK** |
| cross-stream | FULLY UNBLOCKED | **BLOCK** |

# develop ↔ test diff 메타 — frontend (2026-06-15 774차)

> test `@c7c8f07` 불변 · develop `@6f53978`(+1 vs `07dd49b`) · WT **CLEAN** · merge pending **635** (349 FE + 286 BE) · ★ **cross-stream FULLY UNBLOCKED** · merge **미실행** · operation **BLOCK**(QA-B95)

| 항목 | 값 |
|------|-----|
| test HEAD | `c7c8f07` |
| develop HEAD | `6f53978` |
| ahead (`test..develop`) | 349 |
| test npm test | **217/217 PASS** (70 files, 52.07s) |
| test build | 781 modules (max 367.09 kB, 6.29s) |
| test live E2E | **4 suites FAIL / 18 skipped** (LIVE_E2E credentials missing; `scripts/dev-live-e2e.env` **ABSENT**; backend **DOWN**; QA-B95 Planned) |
| develop HEAD test | **미재실행** (774차 test WT 실측 217/217 PASS) |
| develop WT | **CLEAN** |
| audit | 0 (prod omit=dev) |
| routes / pages | **86** / **68** |
| Open (frontend) | **0** |
| Planned (frontend) | **1** (QA-20260615-B95 live E2E env+credentials+backend) |
| merge gate (frontend) | **FULLY UNBLOCKED** |
| cross-stream merge | **FULLY UNBLOCKED** (BE `@1f77324` WT **CLEAN** · Open 0 · test 246/246 PASS) |
| merge pending (total) | **635** (349 FE + 286 BE) |

### TSR 774차 vs 772차

| 항목 | 772차 | 774차 |
|------|-------|-------|
| develop HEAD | `07dd49b` | **`6f53978`** (+1 L02 pilotPageFlows E2E) |
| develop WT | CLEAN | **CLEAN** |
| ahead | 348 | **349** |
| test npm test | 217/217 (51.75s) | **217/217 (51.40s)** |
| test build | 781 modules (5.12s) | **781 modules (4.97s)** |
| live E2E | 4 suites FAIL / 18 skipped | **동일** (credentials missing; env **ABSENT**; backend DOWN) |
| cross-stream BE | `@8b7e476` WT CLEAN · FULLY UNBLOCKED | **`@8b7e476` WT DIRTY 9 · QA-B98 BLOCK** |
| merge pending | 632 | **633** |

### develop `@07dd49b` delta (772차)

- COD commit: `07dd49b` `fix(live-e2e): guard against stale backend probe state`
- test `@c7c8f07` regression **217/217 PASS** unchanged
- cross-stream merge **BLOCK** — backend QA-B98 (LiveE2e bootstrap WIP, 9 dirty files) 미해소

---

# develop ↔ test diff 메타 — frontend (2026-06-15 770차)

> test `@c7c8f07` 불변 · develop `@10f32c4`(+1 vs `5c24e4e`) · WT **CLEAN** · merge pending **632** (347 FE + 285 BE) · ★ **cross-stream FULLY UNBLOCKED** · merge **미실행** · operation **BLOCK**(QA-B95 live E2E credentials+backend)

| 항목 | 값 |
|------|-----|
| test HEAD | `c7c8f07` |
| develop HEAD | `10f32c4` |
| ahead (`test..develop`) | 347 |
| test npm test | **217/217 PASS** (70 files, 51.75s) |
| test build | 781 modules (max 367.09 kB, 5.12s) |
| test live E2E | **4 suites FAIL / 18 skipped** (LIVE_E2E credentials missing; `scripts/dev-live-e2e.env` **ABSENT**; backend **DOWN**; QA-B95 Planned) |
| develop HEAD test | **미재실행** (768 carry: 217/217 PASS @ test) |
| develop WT | **CLEAN** |
| audit | 0 (prod omit=dev) |
| routes / pages | **86** / **68** |
| Open (frontend) | **0** |
| Planned (frontend) | **1** (QA-20260615-B95 live E2E env+credentials+backend) |
| merge gate (frontend) | **FULLY UNBLOCKED** |
| cross-stream merge | **FULLY UNBLOCKED** (BE `@8b7e476` WT **CLEAN** · Open 0 · test 246/246 PASS) |
| merge pending (total) | **632** (347 FE + 285 BE) |

### TSR 770차 vs 768차

| 항목 | 768차 | 770차 |
|------|-------|-------|
| develop HEAD | `5c24e4e` | **`10f32c4`** (+1 live-e2e prefer local env over placeholders) |
| develop WT | CLEAN | **CLEAN** |
| ahead | 346 | **347** |
| test npm test | 217/217 (52.24s) | **217/217 (51.75s)** |
| test build | 781 modules (6.36s) | **781 modules (5.12s)** |
| live E2E | 4 suites FAIL / 18 skipped | **동일** (credentials missing; env **ABSENT**; backend DOWN) |
| cross-stream BE | `@ec5f11c` 284 ahead | **`@8b7e476` 285 ahead** |
| merge pending | 630 | **632** |

### develop `@10f32c4` delta (770차)

- COD commit: `10f32c4` `fix(v2/live-e2e): prefer local env over example placeholders`
- test `@c7c8f07` regression **217/217 PASS** unchanged
- live E2E still blocked by missing LIVE_E2E credentials + backend DOWN (QA-B95 Planned)

---

# develop ↔ test diff 메타 — frontend (2026-06-15 766차)

> test `@c7c8f07` 불변 · develop `@14a2bb9`(+2 vs `95e7e96`) · WT **CLEAN** · merge pending **628** (345 FE + 283 BE) · ★ **cross-stream FULLY UNBLOCKED** · merge **미실행** · operation **BLOCK**(QA-B95 live E2E credentials+backend)

| 항목 | 값 |
|------|-----|
| test HEAD | `c7c8f07` |
| develop HEAD | `14a2bb9` |
| ahead (`test..develop`) | 345 |
| test npm test | **217/217 PASS** (70 files, 51.85s) |
| test build | 781 modules (max 367.09 kB, 4.93s) |
| test live E2E | **4 suites FAIL / 18 skipped** (LIVE_E2E credentials missing; `scripts/dev-live-e2e.env` **PRESENT**; backend **DOWN**; QA-B95 Planned) |
| develop HEAD test | **미재실행** (764 carry: 1337/1337 PASS) |
| develop WT | **CLEAN** |
| audit | 0 (prod omit=dev) |
| routes / pages | **86** / **68** |
| Open (frontend) | **0** |
| Planned (frontend) | **1** (QA-20260615-B95 live E2E env+credentials+backend) |
| merge gate (frontend) | **FULLY UNBLOCKED** |
| cross-stream merge | **FULLY UNBLOCKED** (BE `@d862a82` WT **CLEAN** · Open 0 · test 246/246 PASS) |
| merge pending (total) | **628** (345 FE + 283 BE) |

### TSR 766차 vs 764차

| 항목 | 764차 | 766차 |
|------|-------|-------|
| develop HEAD | `95e7e96` | **`14a2bb9`** (+2 L02_M02 a11y · L02_M07 body restraint UI) |
| develop WT | CLEAN | **CLEAN** |
| ahead | 343 | **345** |
| test npm test | 217/217 (51.68s) | **217/217 (51.85s)** |
| test build | 781 modules (6.06s) | **781 modules (4.93s)** |
| live E2E | 4 suites FAIL / 18 skipped | **동일** (credentials missing; backend DOWN) |
| cross-stream BE | `@df14e15` 282 ahead | **`@d862a82` 283 ahead** |
| merge pending | 625 | **628** |

### develop `@14a2bb9` delta (766차)

- COD commits: `e6ddceb` `fix(ux/L02_M02): a11y pass — Button component and layout CSS` · `14a2bb9` `feat(v2/L02_M07): wire body restraint care UI to V131 API`
- test `@c7c8f07` regression **217/217 PASS** unchanged
- live E2E: **4 suites FAIL / 18 skipped** — `LIVE_E2E_ACCESS_TOKEN` or `EMAIL/PASSWORD` missing; backend **DOWN**
- verdict: **PASS(merge gate)** · operation **BLOCK**(QA-B95)

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-15T10:58:58+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-15 764차)

> test `@c7c8f07` 불변 · develop `@95e7e96`(+1 vs `a5e7722`) · WT **CLEAN** · merge pending **625** (343 FE + 282 BE) · ★ **cross-stream FULLY UNBLOCKED** · merge **미실행** · operation **BLOCK**(QA-B95 live E2E credentials+backend)

| 항목 | 값 |
|------|-----|
| test HEAD | `c7c8f07` |
| develop HEAD | `95e7e96` |
| ahead (`test..develop`) | 343 |
| test npm test | **217/217 PASS** (70 files, 51.68s) |
| test build | 781 modules (max 367.09 kB, 6.06s) |
| test live E2E | **4 suites FAIL / 18 skipped** (LIVE_E2E credentials missing; `scripts/dev-live-e2e.env` **PRESENT**; backend **DOWN**; QA-B95 Planned) |
| develop HEAD test | **미재실행** (762 carry: 1337/1337 PASS) |
| develop WT | **CLEAN** |
| audit | 0 (prod omit=dev) |
| routes / pages | **85** / **67** |
| Open (frontend) | **0** |
| Planned (frontend) | **1** (QA-20260615-B95 live E2E env+credentials+backend) |
| merge gate (frontend) | **FULLY UNBLOCKED** |
| cross-stream merge | **FULLY UNBLOCKED** (BE `@df14e15` WT **CLEAN** · Open 0 · test 246/246 PASS) |
| merge pending (total) | **625** (343 FE + 282 BE) |

### TSR 764차 vs 762차

| 항목 | 762차 | 764차 |
|------|-------|-------|
| develop HEAD | `a5e7722` | **`95e7e96`** (+1 G19 URL guard) |
| develop WT | CLEAN | **CLEAN** |
| ahead | 342 | **343** |
| test npm test | 217/217 (52.39s) | **217/217 (51.68s)** |
| test build | 781 modules (6.27s) | **781 modules (6.06s)** |
| live E2E | 4 suites FAIL / 18 skipped | **동일** (credentials missing; backend DOWN) |
| cross-stream BE | `@ea6092a` 281 ahead | **`@df14e15` 282 ahead** |
| merge pending | 623 | **625** |

### develop `@95e7e96` delta (764차)

- COD commit: `95e7e96` `fix(v2/G19): guard malformed provider discovery URLs`
- files: `IntegratedHomeProviderDiscoveryPanel`·`integratedHomeProviderDiscovery` util+tests (4 files +61/-17)
- test `@c7c8f07` regression **217/217 PASS** unchanged
- live E2E: **4 suites FAIL / 18 skipped** — `LIVE_E2E_ACCESS_TOKEN` or `EMAIL/PASSWORD` missing; backend **DOWN**
- verdict: **PASS(merge gate)** · operation **BLOCK**(QA-B95)
