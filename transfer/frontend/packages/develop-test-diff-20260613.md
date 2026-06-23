<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-13T23:36:30+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-13 607차)

> test `@c7c8f07` 불변 · develop `@a4ab0c2`(+1 vs `38d24b6`, G41b training log compliance live E2E harness BNK-186) · WT **CLEAN** · frontend **Open 1 BLOCK QA-B77** · HEAD **1108/1109 FAIL** · merge pending **475** (262 FE + 213 BE) · **cross-stream merge BLOCK** (BE @ `0f11158` Open 1 BLOCK QA-B76 · WT **DIRTY 2M**)

| 항목 | 값 |
|------|-----|
| test HEAD | `c7c8f07` |
| develop HEAD | `a4ab0c2` |
| ahead (`test..develop`) | 262 |
| test npm test | 217/217 PASS (50.69s) |
| test build | 781 modules (max 367.09 kB, 6.73s) |
| develop HEAD test | **1108/1109 FAIL** (~185.95s, 235 files) |
| develop HEAD test fail | `StaffTrainingLogPage.test.jsx:178` — duplicate `0/1회` |
| develop WT test | 미재실행 (WT CLEAN) |
| develop WT | **CLEAN** |
| dirty files | 없음 |
| route count | 67 (최근 기준 유지) |
| audit | 0 (prod omit=dev) |
| origin/develop | @ `a4ab0c2` (동기화) |
| merge gate (frontend) | **BLOCK** (Open 1 QA-B77 · HEAD test FAIL) |
| cross-stream merge | **BLOCK** (BE @ `0f11158` WT **DIRTY 2M** · Open 1 QA-B76) |

### TSR 607차 vs 605차

| 항목 | 605차 | 607차 |
|------|-------|-------|
| develop HEAD | `38d24b6` | **`a4ab0c2`** (+1) |
| develop WT | **CLEAN** | **CLEAN** |
| develop HEAD test | 미재실행 | **1108/1109 FAIL** |
| test npm test | 217/217 PASS (50.35s) | **217/217 PASS (50.69s)** |
| test build | 781 modules (5.10s) | **781 modules (6.73s)** |
| ahead | 261 | **262** |
| Open (frontend) | 0 | **1 BLOCK QA-B77** |
| merge gate | FULLY UNBLOCKED | **BLOCK** |
| cross-stream | FULLY UNBLOCKED | **BLOCK** |
| merge pending | 474 | **475** |

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-13T23:17:20+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-13 605차)

> test `@c7c8f07` 불변 · develop `@38d24b6`(+1 vs `e43295b`, G41b wire training log compliance BNK-185) · WT **CLEAN** · frontend **Open 0** · merge pending **474** (261 FE + 213 BE) · **cross-stream merge FULLY UNBLOCKED** (BE @ `0f11158` Open 0 · WT **CLEAN**)

| 항목 | 값 |
|------|-----|
| test HEAD | `c7c8f07` |
| develop HEAD | `38d24b6` |
| ahead (`test..develop`) | 261 |
| test npm test | 217/217 PASS (50.35s) |
| test build | 781 modules (max 367.09 kB, 5.10s) |
| develop HEAD test | 미재실행 (tester read-only 정책) |
| develop WT test | 미재실행 (WT CLEAN) |
| develop WT | **CLEAN** |
| dirty files | 없음 |
| route count | 67 (최근 기준 유지) |
| audit | 0 (prod omit=dev) |
| origin/develop | @ `38d24b6` (동기화) |
| merge gate (frontend) | **FULLY UNBLOCKED** (Open 0 · WT CLEAN) |
| cross-stream merge | **FULLY UNBLOCKED** (BE @ `0f11158` WT **CLEAN** · Open 0) |

### TSR 605차 vs 603차

| 항목 | 603차 | 605차 |
|------|-------|-------|
| develop HEAD | `e43295b` | **`38d24b6`** (+1) |
| develop WT | **CLEAN** | **CLEAN** |
| develop HEAD test | 미재실행 | **미재실행** |
| test npm test | 217/217 PASS (51.00s) | **217/217 PASS (50.35s)** |
| test build | 781 modules (4.84s) | **781 modules (5.10s)** |
| ahead | 260 | **261** |
| Open (frontend) | 0 | **0** |
| merge pending | 472 | **474** |

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-13T23:03:04+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-13 603차)

> test `@c7c8f07` 불변 · develop `@e43295b`(+1 vs `e69bf00`, G41 training log nav·services tests·pilot E2E BNK-184) · WT **CLEAN** · frontend **Open 0** · merge pending **472** (260 FE + 212 BE) · **cross-stream merge FULLY UNBLOCKED** (BE @ `613b6af` Open 0 · WT **CLEAN**)

| 항목 | 값 |
|------|-----|
| test HEAD | `c7c8f07` |
| develop HEAD | `e43295b` |
| ahead (`test..develop`) | 260 |
| test npm test | 217/217 PASS (51.00s) |
| test build | 781 modules (max 367.09 kB, 4.84s) |
| develop HEAD test | 미재실행 (tester read-only 정책) |
| develop WT test | 미재실행 (WT CLEAN) |
| develop WT | **CLEAN** |
| dirty files | 없음 |
| route count | 67 (최근 기준 유지) |
| audit | 0 (prod omit=dev) |
| origin/develop | @ `e43295b` (동기화) |
| merge gate (frontend) | **FULLY UNBLOCKED** (Open 0 · WT CLEAN) |
| cross-stream merge | **FULLY UNBLOCKED** (BE @ `613b6af` WT **CLEAN** · Open 0) |

### TSR 603차 vs 601차

| 항목 | 601차 | 603차 |
|------|-------|-------|
| develop HEAD | `e69bf00` | **`e43295b`** (+1) |
| develop WT | **CLEAN** | **CLEAN** |
| develop HEAD test | 미재실행 | **미재실행** |
| test npm test | 217/217 PASS (53.06s) | **217/217 PASS (51.00s)** |
| test build | 781 modules (6.05s) | **781 modules (4.84s)** |
| ahead | 259 | **260** |
| merge pending | 471 | **472** |
| Open | 0 | **0** |

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-13T22:18:02+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-13 599차)

> test `@c7c8f07` 불변 · develop `@5146895`(+1 vs `400c835`, G30 monitoring checklist pilot E2E) · WT **CLEAN** · frontend **Open 0** · merge pending **468** (257 FE + 211 BE) · **cross-stream merge FULLY UNBLOCKED** (BE @ `6191b91` Open 0 · WT **CLEAN**)

| 항목 | 값 |
|------|-----|
| test HEAD | `c7c8f07` |
| develop HEAD | `5146895` |
| ahead (`test..develop`) | 257 |
| test npm test | 217/217 PASS (51.14s) |
| test build | 781 modules (max 367.09 kB, 6.76s) |
| develop HEAD test | 1094/1094 PASS (232 files, 186.42s) |
| develop WT test | 미재실행 (WT CLEAN) |
| develop WT | **CLEAN** |
| dirty files | 없음 |
| route count | 67 (최근 기준 유지) |
| audit | 0 (prod omit=dev) |
| origin/develop | @ `5146895` (동기화) |
| merge gate (frontend) | **FULLY UNBLOCKED** (Open 0 · WT CLEAN · HEAD PASS) |
| cross-stream merge | **FULLY UNBLOCKED** (BE @ `6191b91` WT **CLEAN** · Open 0) |

### TSR 599차 vs 597차

| 항목 | 597차 | 599차 |
|------|-------|-------|
| develop HEAD | `400c835` | **`5146895`** (+1) |
| develop WT | **CLEAN** | **CLEAN** |
| develop HEAD test | 미재실행 | **1094/1094 PASS** (+12 @Test) |
| test npm test | 217/217 PASS (49.73s) | **217/217 PASS (51.14s)** |
| ahead | 256 | **257** |
| merge pending | 466 | **468** |
| Open | 0 | **0** |

### TSR 597차 vs 596차

| 항목 | 596차 | 597차 |
|------|-------|-------|
| develop HEAD | `400c835` | **`400c835`** (불변) |
| develop WT | **CLEAN** | **CLEAN** |
| test npm test | 217/217 PASS (52.09s) | **217/217 PASS (49.73s)** |
| test build | 781 modules (5.06s) | **781 modules (4.81s)** |
| ahead | 256 | **256** |
| Open (frontend) | 0 | **0** |
| merge gate | FULLY UNBLOCKED | **FULLY UNBLOCKED** |
| cross-stream | FULLY UNBLOCKED | **FULLY UNBLOCKED** |
| merge pending | 466 | **466** |

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-13T21:45:30+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-13 596차)

> test `@c7c8f07` 불변 · develop `@400c835`(+1 vs `574bd08`) · WT **CLEAN** · frontend **Open 0** · merge pending **466** (256 FE + 210 BE) · **cross-stream merge FULLY UNBLOCKED** (BE @ `997831c` Open 0 · WT **CLEAN**)

| 항목 | 값 |
|------|-----|
| test HEAD | `c7c8f07` |
| develop HEAD | `400c835` |
| ahead (`test..develop`) | 256 |
| test npm test | 217/217 PASS (52.09s) |
| test build | 781 modules (max 367.09 kB, 5.06s) |
| develop HEAD test | 미재실행 (tester read-only 정책) |
| develop WT test | 미재실행 (WT CLEAN) |
| develop WT | **CLEAN** |
| dirty files | 없음 |
| route count | 67 (최근 기준 유지) |
| audit | 0 (prod omit=dev) |
| origin/develop | @ `400c835` (동기화) |
| merge gate (frontend) | **FULLY UNBLOCKED** (Open 0 · WT CLEAN) |
| cross-stream merge | **FULLY UNBLOCKED** (BE @ `997831c` WT **CLEAN** · Open 0) |

### TSR 596차 vs 594차

| 항목 | 594차 | 596차 |
|------|-------|-------|
| develop HEAD | `574bd08` | **`400c835`** (+1) |
| develop WT | **CLEAN** | **CLEAN** |
| test npm test | 217/217 PASS | **217/217 PASS** |
| test build | 781 modules | **781 modules** |
| ahead | 255 | **256** |
| Open (frontend) | 0 | **0** |
| merge gate | FULLY UNBLOCKED | **FULLY UNBLOCKED** |
| cross-stream | FULLY UNBLOCKED | **FULLY UNBLOCKED** |
| merge pending | 464 | **466** |

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-13T21:28:23+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-13 594차)

> test `@c7c8f07` 불변 · develop `@574bd08`(+2 vs `dbf0299`) · WT **CLEAN** · frontend **Open 0** (**QA-B75 Fixed**) · merge pending **464** (255 FE + 209 BE) · **cross-stream merge FULLY UNBLOCKED** (BE @ `b1dfd34` Open 0 · WT **CLEAN**)

| 항목 | 값 |
|------|-----|
| test HEAD | `c7c8f07` |
| develop HEAD | `574bd08` |
| ahead (`test..develop`) | 255 |
| test npm test | 217/217 PASS (50.73s) |
| test build | 781 modules (max 367.09 kB, 4.85s) |
| develop HEAD test | 미재실행 (tester read-only 정책) |
| develop WT test | 미재실행 (WT CLEAN) |
| develop WT | **CLEAN** |
| dirty files | 없음 |
| route count | 67 (최근 기준 유지) |
| audit | 0 (prod omit=dev) |
| origin/develop | @ `574bd08` (동기화) |
| merge gate (frontend) | **FULLY UNBLOCKED** (Open 0 · WT CLEAN · QA-B75 Fixed) |
| cross-stream merge | **FULLY UNBLOCKED** (BE @ `b1dfd34` WT **CLEAN** · Open 0) |

### TSR 594차 vs 592차

| 항목 | 592차 | 594차 |
|------|-------|-------|
| develop HEAD | `dbf0299` | **`574bd08`** (+2) |
| develop WT | **DIRTY 5M** | **CLEAN** |
| develop HEAD test | 1084/1084 PASS | **미재실행** |
| develop WT test | 1085/1085 PASS | **미재실행** |
| test npm test | 217/217 PASS | **217/217 PASS** |
| ahead | 253 | **255** |
| Open (frontend) | 1 BLOCK QA-B75 | **0** |
| merge gate | BLOCK | **FULLY UNBLOCKED** |
| cross-stream | BLOCK | **FULLY UNBLOCKED** |
| merge pending | 462 | **464** |

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-13T20:07:13+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-13 588차)

> test `@c7c8f07` 불변 · develop `@cfd87c5`(+2 vs `443efca`) · WT **CLEAN** · frontend **Open 0** (**QA-B74 Fixed**) · merge pending **458** (252 FE + 206 BE) · **cross-stream merge FULLY UNBLOCKED** (BE @ `726b3de` Open 0 · WT **CLEAN**)

| 항목 | 값 |
|------|-----|
| test HEAD | `c7c8f07` |
| develop HEAD | `cfd87c5` |
| ahead (`test..develop`) | 252 |
| test npm test | 217/217 PASS (51.02s) |
| test build | 781 modules (max 367.09 kB, 4.85s) |
| develop HEAD test | **1082/1082 PASS** (229 files, 179.58s) |
| develop HEAD build | 미재실행 |
| develop WT | **CLEAN** |
| route count | 67 (최근 기준 유지) |
| audit | 0 (prod omit=dev) |
| origin/develop | @ `cfd87c5` (동기화) |
| merge gate (frontend) | **FULLY UNBLOCKED** (Open 0 · QA-B74 Fixed) |
| cross-stream merge | **FULLY UNBLOCKED** (BE @ `726b3de` WT **CLEAN** · Open 0) |

### TSR 588차 vs 586차

| 항목 | 586차 | 588차 |
|------|-------|-------|
| develop HEAD | `443efca` | **`cfd87c5`** |
| develop WT | **CLEAN** | **CLEAN** |
| develop HEAD test | 1081/1082 FAIL (QA-B74) | **1082/1082 PASS** (QA-B74 Fixed) |
| test npm test | 217/217 PASS | **217/217 PASS** |
| ahead | 250 | **252** |
| Open (frontend) | 1 BLOCK QA-B74 | **0** |
| merge gate | BLOCK | **FULLY UNBLOCKED** |
| cross-stream | BLOCK | **FULLY UNBLOCKED** |
| merge pending | 455 | **458** |

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-13T18:33:39+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-13 581차)

> test `@c7c8f07` 불변 · develop `@6b1258c`(+1 vs `ff173af`) · WT **CLEAN** · frontend **Open 0** · merge pending **451** (248 FE + 203 BE) · **cross-stream merge FULLY UNBLOCKED** (BE @ `c16f4fe` Open 0 · WT **CLEAN**)

| 항목 | 값 |
|------|-----|
| test HEAD | `c7c8f07` |
| develop HEAD | `6b1258c` |
| ahead (`test..develop`) | 248 |
| test npm test | 217/217 PASS (50.52s) |
| test build | 781 modules (max 367.09 kB, 4.74s) |
| develop HEAD test | 미재실행 (tester read-only 정책) |
| develop HEAD build | 미재실행 (tester read-only 정책) |
| develop WT | **CLEAN** |
| route count | 67 (최근 기준 유지) |
| audit | 0 (prod omit=dev) |
| origin/develop | @ `6b1258c` (동기화) |
| merge gate (frontend) | **FULLY UNBLOCKED** (Open 0) |
| cross-stream merge | **FULLY UNBLOCKED** (BE @ `c16f4fe` WT **CLEAN** · Open 0) |

### TSR 581차 vs 579차

| 항목 | 579차 | 581차 |
|------|-------|-------|
| develop HEAD | `ff173af` | **`6b1258c`** |
| develop WT | **CLEAN** | **CLEAN** |
| develop HEAD test | 1072/1072 PASS | **미재실행** |
| test npm test | 217/217 PASS | **217/217 PASS** |
| ahead | 247 | **248** |
| Open (frontend) | 0 | **0** |
| merge gate | FULLY UNBLOCKED | **FULLY UNBLOCKED** |
| cross-stream | BLOCK (QA-B73) | **FULLY UNBLOCKED** |
| merge pending | 449 | **451** |

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-13T18:18:05+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-13 579차)

> test `@c7c8f07` 불변 · develop `@ff173af`(+1 vs `5bba7a2`) · WT **CLEAN** · frontend **Open 0** · merge pending **449** (247 FE + 202 BE) · **cross-stream merge BLOCK** (BE @ `d4acab7` Open 1 BLOCK QA-B73 · WT **DIRTY 2M**)

| 항목 | 값 |
|------|-----|
| test HEAD | `c7c8f07` |
| develop HEAD | `ff173af` |
| ahead (`test..develop`) | 247 |
| test npm test | 217/217 PASS (50.36s) |
| test build | 781 modules (max 367.09 kB, 6.70s) |
| develop HEAD test | 1072/1072 PASS (227 files, 179.63s) |
| develop HEAD build | multi-chunk (index 577.50 kB >500 kB vite warn, 6.26s) |
| develop WT | **CLEAN** |
| route count | 67 (최근 기준 유지) |
| audit | 0 (prod omit=dev) |
| origin/develop | @ `ff173af` (동기화) |
| merge gate (frontend) | **FULLY UNBLOCKED** (Open 0) |
| cross-stream merge | **FULLY UNBLOCKED** (BE @ `d4acab7` WT CLEAN · Open 0) |

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-13T17:33:20+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-13 575차)

> test `@c7c8f07` 불변 · develop `@488f547`(+1 vs `a7a6004`) · WT **CLEAN** · frontend **Open 0** · merge pending **446** (245 FE + 201 BE) · **cross-stream merge FULLY UNBLOCKED** (BE @ `c4dbe43` Open 0 · WT CLEAN)

| 항목 | 값 |
|------|-----|
| test HEAD | `c7c8f07` |
| develop HEAD | `488f547` |
| ahead (`test..develop`) | 245 |
| test npm test | 217/217 PASS (50.06s) |
| test build | 781 modules (max 367.09 kB, 4.85s) |
| develop HEAD test/build | 미재실행 (tester read-only 정책) |
| develop WT | **CLEAN** |
| route count | 67 (최근 기준 유지) |
| audit | 0 (prod omit=dev) |
| origin/develop | @ `488f547` (동기화) |
| merge gate (frontend) | **FULLY UNBLOCKED** (Open 0) |
| cross-stream merge | **FULLY UNBLOCKED** (BE @ `c4dbe43` WT CLEAN · Open 0) |

### TSR 575차 vs 573차

| 항목 | 573차 | 575차 |
|------|-------|-------|
| develop HEAD | `a7a6004` | **`488f547`** |
| develop WT | **CLEAN** | **CLEAN** |
| test npm test | 217/217 PASS | **217/217 PASS** |
| ahead | 243 | **245** |
| Open (frontend) | 0 | **0** |
| merge gate | FULLY UNBLOCKED | **FULLY UNBLOCKED** |
| cross-stream | FULLY UNBLOCKED | **FULLY UNBLOCKED** |
| merge pending | 443 | **446** |

---

# develop ↔ test diff 메타 — frontend (2026-06-13 573차)

> test `@c7c8f07` 불변 · develop `@a7a6004`(+1 vs `892450a`, G42 grievance approval E2E — **QA-B72 Fixed**) · WT **CLEAN** · frontend **Open 0** · merge pending **443** (243 FE + 200 BE) · **cross-stream merge FULLY UNBLOCKED** (BE @ `39ee679` Open 0 · WT CLEAN)

| 항목 | 값 |
|------|-----|
| test HEAD | `c7c8f07` |
| develop HEAD | `a7a6004` |
| ahead (`test..develop`) | 243 |
| test npm test | 217/217 PASS (78.04s) |
| test build | 781 modules (max 367.09 kB, 4.84s) |
| develop HEAD npm test | **1067/1067 PASS** (227 files, 207.24s) |
| develop HEAD build | 781 modules @ test baseline; develop multi-chunk @ HEAD (vite warn >500 kB index) |
| develop WT | **CLEAN** |
| route count | 67 |
| audit | 0 (prod omit=dev) |
| origin/develop | @ `a7a6004` (동기화) |
| merge gate (frontend) | **FULLY UNBLOCKED** (HEAD test PASS · Open 0) |
| cross-stream merge | **FULLY UNBLOCKED** (BE @ `39ee679` WT CLEAN · Open 0) |

### TSR 573차 vs 571차

| 항목 | 571차 | 573차 |
|------|-------|-------|
| develop HEAD | `892450a` | **`a7a6004`** (+1 QA-B72 fix) |
| develop WT | **CLEAN** | **CLEAN** |
| test npm test | 217/217 PASS | **217/217 PASS** |
| develop HEAD npm test | 1066/1067 FAIL (approve API E2E) | **1067/1067 PASS** |
| ahead | 242 | **243** |
| Open (frontend) | 1 BLOCK QA-B72 | **0** |
| merge gate | BLOCK | **FULLY UNBLOCKED** |
| cross-stream | BLOCK | **FULLY UNBLOCKED** |
| merge pending | 441 | **443** |

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-13T16:28:00+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-13 571차, superseded)

| 항목 | 569차 | 571차 |
|------|-------|-------|
| develop HEAD | `14124d6` | **`892450a`** (+1 partial fix) |
| develop WT | **CLEAN** | **CLEAN** |
| test npm test | 217/217 PASS | **217/217 PASS** |
| develop HEAD npm test | 1065/1066 FAIL (duplicate button) | **1066/1067 FAIL** (approve API E2E) |
| ahead | 241 | **242** |
| Open (frontend) | 1 BLOCK QA-B72 | **1 BLOCK QA-B72** (증상 갱신) |
| merge gate (frontend) | BLOCK | **BLOCK** |
| cross-stream merge | BLOCK | **BLOCK** (BE FULLY UNBLOCKED) |
| merge pending | 439 | **441** |

### TSR 571차 판정

- **PASS(v1.2+v1.3-A @ test)** — test 브랜치 회귀 217/217 GREEN.
- **frontend develop clean + 원격 동기화 확인** — `892450a`, `test..develop=242`.
- **Open 1 BLOCK QA-B72** — G42 `pilotPageFlows.test.jsx:3911` approve API 미호출 (duplicate button partial fix @ `892450a`).
- **operation 승격 BLOCK** — develop→test merge 미실행 상태, post-merge live E2E 미실행.

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-13T16:02:21+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-13 569차)

> test `@c7c8f07` 불변 · develop `@14124d6`(+1 vs `47a4928`, G42 grievance follow-up checklist·approval queue UI) · WT **CLEAN** · frontend **Open 1 BLOCK QA-B72** · merge pending **439** (241 FE + 198 BE) · **cross-stream merge BLOCK**

| 항목 | 값 |
|------|-----|
| test HEAD | `c7c8f07` |
| develop HEAD | `14124d6` |
| ahead (`test..develop`) | 241 |
| test npm test | 217/217 PASS (51.11s) |
| test build | 781 modules (max 367.09 kB, ~7s) |
| develop HEAD npm test | **1065/1066 FAIL** (227 files, 180.31s) |
| develop WT | **CLEAN** |
| route count | 67 (567차 기준 유지) |
| audit | 0 (prod omit=dev) |
| origin/develop | @ `14124d6` (동기화) |
| merge gate (frontend) | **BLOCK** (HEAD test FAIL · Open 1 QA-B72) |
| cross-stream merge | **BLOCK** (BE @ `bcb1d9f` WT CLEAN · Open 0 · 198 ahead) |

### TSR 569차 vs 567차

| 항목 | 567차 | 569차 |
|------|-------|-------|
| develop HEAD | `47a4928` | **`14124d6`** (+1 G42 UI) |
| develop WT | **CLEAN** | **CLEAN** |
| test npm test | 217/217 PASS | **217/217 PASS** |
| develop HEAD npm test | 미재실행 | **1065/1066 FAIL** |
| ahead | 240 | **241** |
| Open (frontend) | 0 | **1 BLOCK QA-B72** |
| merge gate (frontend) | FULLY UNBLOCKED | **BLOCK** |
| cross-stream merge | FULLY UNBLOCKED | **BLOCK** |
| merge pending | 438 | **439** |

### TSR 569차 판정

- **PASS(v1.2+v1.3-A @ test)** — test 브랜치 회귀 217/217 GREEN.
- **frontend develop clean + 원격 동기화 확인** — `14124d6`, `test..develop=241`.
- **Open 1 BLOCK QA-B72** — G42 duplicate approval button `aria-label` → `pilotPageFlows.test.jsx:3908` FAIL.
- **operation 승격 BLOCK** — develop→test merge 미실행 상태, post-merge live E2E 미실행.

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-13T15:40:16+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-13 567차)

> test `@c7c8f07` 불변 · develop `@47a4928`(+1 vs `ccc4d75`, G30 monitoring live E2E harness + HR photo board images) · WT **CLEAN** · frontend **Open 0** · merge pending **437** (240 FE + 197 BE) · **cross-stream merge FULLY UNBLOCKED**

| 항목 | 값 |
|------|-----|
| test HEAD | `c7c8f07` |
| develop HEAD | `47a4928` |
| ahead (`test..develop`) | 240 |
| test npm test | 217/217 PASS (51.86s) |
| test build | 781 modules (max 367.09 kB, 7.15s) |
| develop HEAD npm test | 미재실행 (tester read-only 정책) |
| develop WT | **CLEAN** |
| route count | 67 (최근 문서 기준 유지) |
| audit | 0 (prod omit=dev) |
| origin/develop | @ `47a4928` (동기화) |
| merge gate (frontend) | **FULLY UNBLOCKED** (WT clean · Open 0) |
| cross-stream merge | **FULLY UNBLOCKED** (BE 최신 관측 @ `9fef436` WT CLEAN · Open 0 · 197 ahead) |

### TSR 567차 vs 565차

| 항목 | 565차 | 567차 |
|------|-------|-------|
| develop HEAD | `ccc4d75` | **`47a4928`** (+1 latest develop) |
| develop WT | **CLEAN** | **CLEAN** |
| test npm test | 217/217 PASS | **217/217 PASS** |
| test build | 781 modules | **781 modules** |
| ahead | 239 | **240** |
| Open (frontend) | 0 | **0** |
| merge gate (frontend) | FULLY UNBLOCKED | **FULLY UNBLOCKED** |
| cross-stream merge | FULLY UNBLOCKED | **FULLY UNBLOCKED** |
| merge pending | 435 | **437** |

### TSR 567차 판정

- **PASS(v1.2+v1.3-A @ test)** — test 브랜치 회귀 217/217 GREEN.
- **frontend develop clean + 원격 동기화 확인** — `47a4928`, `test..develop=240`.
- **Open 이슈 없음** — QA_FEEDBACK Open 0(frontend), merge gate 유지.
- **operation 승격 BLOCK** — develop→test merge 미실행 상태, post-merge live E2E 미실행.

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-13T14:24:30+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-13 561차)

> test `@c7c8f07` 불변 · develop `@07956f5`(+1 vs `bf6dd25`, US-R02 8-12 staff status report exports·reference date filter) · WT **CLEAN** · frontend **Open 0** · merge pending **430** (236 FE + 194 BE) · **cross-stream merge FULLY UNBLOCKED**

| 항목 | 값 |
|------|-----|
| test HEAD | `c7c8f07` |
| develop HEAD | `07956f5` |
| ahead (`test..develop`) | 236 |
| test npm test | 217/217 PASS (50.36s) |
| test build | 781 modules (max 367.09 kB, 6.64s) |
| develop HEAD npm test | **1048/1048 PASS** (226 files, 178.33s) |
| develop WT | **CLEAN** |
| develop HEAD build | multi-chunk (928 modules, index 576.28 kB >500 kB vite warn, 6.29s) |
| route count | 67 |
| audit | 0 (prod omit=dev) |
| origin/develop | @ `07956f5` (동기화) |
| merge gate (frontend) | **FULLY UNBLOCKED** (WT clean · Open 0 · HEAD 1048/1048 PASS) |
| cross-stream merge | **FULLY UNBLOCKED** (BE @ `5692662` WT CLEAN · Open 0 · 194 ahead) |

### TSR 561차 vs 559차

| 항목 | 559차 | 561차 |
|------|-------|-------|
| develop HEAD | `bf6dd25` | **`07956f5`** (+1 US-R02 8-12 exports) |
| develop WT | **CLEAN** | **CLEAN** |
| test npm test | 217/217 PASS | **217/217 PASS** |
| develop HEAD npm test | 1039/1039 PASS | **1048/1048 PASS** (+9 @Test) |
| ahead | 235 | **236** |
| route count | 67 | **67** |
| Open (frontend) | 0 | **0** |
| merge gate (frontend) | FULLY UNBLOCKED | **FULLY UNBLOCKED** |
| cross-stream merge | FULLY UNBLOCKED | **FULLY UNBLOCKED** |
| merge pending | 428 | **430** |

### TSR 561차 판정

- **PASS(v1.2+v1.3-A @ test)** — test 브랜치 회귀 217/217 GREEN.
- **★ US-R02 8-12 exports·reference date filter** — develop `@07956f5` staff status report CSV/XLSX export·기준일 필터.
- **★ frontend merge gate FULLY UNBLOCKED** — WT CLEAN · Open 0 · HEAD 1048/1048 PASS.
- **★ cross-stream merge FULLY UNBLOCKED** — BE Open 0 @ `5692662` · WT CLEAN.
- **operation 승격 BLOCK** — merge(430) 미실행 · post-merge live E2E 미실행.

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-13T14:07:00+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-13 559차)

> test `@c7c8f07` 불변 · develop `@bf6dd25`(+1 vs `0da41c6`, US-R02 8-12 staff status report aggregated API) · WT **CLEAN** · frontend **Open 0** · merge pending **428** (235 FE + 193 BE) · **cross-stream merge FULLY UNBLOCKED**

| 항목 | 값 |
|------|-----|
| test HEAD | `c7c8f07` |
| develop HEAD | `bf6dd25` |
| ahead (`test..develop`) | 235 |
| test npm test | 217/217 PASS (79.52s) |
| test build | 781 modules (max 367.09 kB, 9.69s) |
| develop HEAD npm test | **1039/1039 PASS** (225 files, 209.12s) |
| develop WT | **CLEAN** |
| develop HEAD build | multi-chunk (928 modules, index 576.28 kB >500 kB vite warn, 11.59s) |
| route count | 67 |
| audit | 0 (prod omit=dev) |
| origin/develop | @ `bf6dd25` (동기화) |
| merge gate (frontend) | **FULLY UNBLOCKED** (WT clean · Open 0 · HEAD 1039/1039 PASS) |
| cross-stream merge | **FULLY UNBLOCKED** (BE @ `b8e92bf` WT CLEAN · Open 0 · 931/931 PASS · 193 ahead) |

### TSR 559차 vs 557차

| 항목 | 557차 | 559차 |
|------|-------|-------|
| develop HEAD | `0da41c6` | **`bf6dd25`** (+1 US-R02 8-12) |
| develop WT | **CLEAN** | **CLEAN** |
| test npm test | 217/217 PASS | **217/217 PASS** |
| develop HEAD npm test | 1036/1036 PASS | **1039/1039 PASS** (+3 @Test) |
| ahead | 234 | **235** |
| route count | 67 | **67** |
| Open (frontend) | 0 | **0** |
| merge gate (frontend) | FULLY UNBLOCKED | **FULLY UNBLOCKED** |
| cross-stream merge | FULLY UNBLOCKED | **FULLY UNBLOCKED** |
| merge pending | 426 | **428** |

### TSR 559차 판정

- **PASS(v1.2+v1.3-A @ test)** — test 브랜치 회귀 217/217 GREEN.
- **★ US-R02 8-12 aggregated API wiring** — develop `@bf6dd25` staff status report → backend aggregated endpoint 연동.
- **★ frontend merge gate FULLY UNBLOCKED** — WT CLEAN · Open 0 · HEAD 1039/1039 PASS.
- **★ cross-stream merge FULLY UNBLOCKED** — BE Open 0 @ `b8e92bf` · 931/931 PASS.
- **operation 승격 BLOCK** — merge(428) 미실행 · post-merge live E2E 미실행.

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-13T13:46:00+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-13 557차)

> test `@c7c8f07` 불변 · develop `@0da41c6`(+1 vs `6f6915f`, FAQ21836 monitoring template basis fallback) · WT **CLEAN** · frontend **Open 0** · merge pending **426** (234 FE + 192 BE) · **cross-stream merge FULLY UNBLOCKED**

| 항목 | 값 |
|------|-----|
| test HEAD | `c7c8f07` |
| develop HEAD | `0da41c6` |
| ahead (`test..develop`) | 234 |
| test npm test | 217/217 PASS (50.43s) |
| test build | 781 modules (max 367.09 kB, 6.97s) |
| develop HEAD npm test | **1036/1036 PASS** (224 files, 179.34s) |
| develop WT | **CLEAN** |
| develop HEAD build | multi-chunk (928 modules, index 576.59 kB >500 kB vite warn, 6.24s) |
| route count | 67 |
| audit | 0 (prod omit=dev) |
| origin/develop | @ `0da41c6` (동기화) |
| merge gate (frontend) | **FULLY UNBLOCKED** (WT clean · Open 0 · HEAD 1036/1036 PASS) |
| cross-stream merge | **FULLY UNBLOCKED** (BE @ `5501745` WT CLEAN · Open 0 · 192 ahead) |

### TSR 557차 vs 555차

| 항목 | 555차 | 557차 |
|------|-------|-------|
| develop HEAD | `6f6915f` | **`0da41c6`** (+1 FAQ21836) |
| develop WT | **CLEAN** | **CLEAN** |
| test npm test | 217/217 PASS | **217/217 PASS** |
| develop HEAD npm test | 1035/1035 PASS | **1036/1036 PASS** (+1 @Test) |
| ahead | 233 | **234** |
| route count | 67 | **67** |
| Open (frontend) | 0 | **0** |
| merge gate (frontend) | FULLY UNBLOCKED | **FULLY UNBLOCKED** |
| cross-stream merge | FULLY UNBLOCKED | **FULLY UNBLOCKED** |
| merge pending | 424 | **426** |

### TSR 557차 판정

- **PASS(v1.2+v1.3-A @ test)** — test 브랜치 회귀 217/217 GREEN.
- **★ G30 FAQ21836 basis fallback** — develop `@0da41c6` monitoring template 근거 문구 보강.
- **★ frontend merge gate FULLY UNBLOCKED** — WT CLEAN · Open 0 · HEAD 1036/1036 PASS.
- **★ cross-stream merge FULLY UNBLOCKED** — BE Open 0 @ `5501745`.
- **operation 승격 BLOCK** — merge(426) 미실행 · post-merge live E2E 미실행.

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-13T13:22:00+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-13 555차)

> test `@c7c8f07` 불변 · develop `@6f6915f`(+1 vs `b47e85c`, G30 monitoring self-diagnosis UI BNK-169) · WT **CLEAN** · frontend **Open 0** · merge pending **424** (233 FE + 191 BE) · **cross-stream merge FULLY UNBLOCKED**

| 항목 | 값 |
|------|-----|
| test HEAD | `c7c8f07` |
| develop HEAD | `6f6915f` |
| ahead (`test..develop`) | 233 |
| test npm test | 217/217 PASS (79.73s) |
| test build | 781 modules (max 367.09 kB, 6.25s) |
| develop HEAD npm test | **1035/1035 PASS** (224 files, 205.37s) |
| develop WT | **CLEAN** |
| develop HEAD build | multi-chunk (index 576.45 kB >500 kB vite warn, 7.74s) |
| route count | 67 |
| audit | 0 (prod omit=dev) |
| origin/develop | @ `6f6915f` (동기화) |
| merge gate (frontend) | **FULLY UNBLOCKED** (WT clean · Open 0 · HEAD 1035/1035 PASS) |
| cross-stream merge | **FULLY UNBLOCKED** (BE @ `6a72b70` WT CLEAN · Open 0 · 191 ahead) |

### TSR 555차 vs 553차

| 항목 | 553차 | 555차 |
|------|-------|-------|
| develop HEAD | `b47e85c` | **`6f6915f`** (+1 G30 FE) |
| develop WT | **CLEAN** | **CLEAN** |
| test npm test | 217/217 PASS | **217/217 PASS** |
| develop HEAD npm test | 1023/1023 PASS | **1035/1035 PASS** (+12 @Test) |
| ahead | 232 | **233** |
| route count | 66 | **67** |
| Open (frontend) | 0 | **0** |
| merge gate (frontend) | FULLY UNBLOCKED | **FULLY UNBLOCKED** |
| cross-stream merge | FULLY UNBLOCKED | **FULLY UNBLOCKED** |
| merge pending | 422 | **424** |

### TSR 555차 판정

- **PASS(v1.2+v1.3-A @ test)** — test 브랜치 회귀 217/217 GREEN.
- **★ G30 FE+BE BNK-169** — develop `@6f6915f` UI + backend `@6a72b70` API (cross-stream aligned).
- **★ frontend merge gate FULLY UNBLOCKED** — WT CLEAN · Open 0 · HEAD 1035/1035 PASS.
- **★ cross-stream merge FULLY UNBLOCKED** — BE Open 0 @ `6a72b70`.
- **operation 승격 BLOCK** — merge(424) 미실행 · post-merge live E2E 미실행.

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-13T12:58:00+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-13 553차)

> test `@c7c8f07` 불변 · develop `@b47e85c`(+1 vs `a5c2736`, G27 no-branch guard — **QA-B71 Fixed**) · WT **CLEAN** · frontend **Open 0** · merge pending **422** (232 FE + 190 BE) · **cross-stream merge FULLY UNBLOCKED**

| 항목 | 값 |
|------|-----|
| test HEAD | `c7c8f07` |
| develop HEAD | `b47e85c` |
| ahead (`test..develop`) | 232 |
| test npm test | 217/217 PASS (50.47s) |
| test build | 781 modules (max 367.09 kB, 7.24s) |
| develop HEAD npm test | **1023/1023 PASS** (222 files, 174.89s) |
| develop WT | **CLEAN** |
| develop HEAD build | multi-chunk (index 559.65 kB >500 kB vite warn, 6.23s) |
| route count | 66 |
| audit | 0 (prod omit=dev) |
| origin/develop | @ `b47e85c` (동기화) |
| merge gate (frontend) | **FULLY UNBLOCKED** (WT clean · Open 0 · HEAD 1023/1023 PASS) |
| cross-stream merge | **FULLY UNBLOCKED** (BE @ `aaa16f8` WT CLEAN · Open 0 · 190 ahead) |

### TSR 553차 vs 551차

| 항목 | 551차 | 553차 |
|------|-------|-------|
| develop HEAD | `a5c2736` | **`b47e85c`** (+1 G27) |
| develop WT | **DIRTY 2M** | **CLEAN** |
| test npm test | 217/217 PASS | **217/217 PASS** |
| develop HEAD npm test | 1022/1022 PASS | **1023/1023 PASS** (+1 @Test) |
| ahead | 231 | **232** |
| Open (frontend) | 1 BLOCK QA-B71 | **0** |
| merge gate (frontend) | BLOCK | **FULLY UNBLOCKED** |
| cross-stream merge | BLOCK | **FULLY UNBLOCKED** |
| merge pending | 420 | **422** |

### TSR 553차 판정

- **PASS(v1.2+v1.3-A @ test)** — test 브랜치 회귀 217/217 GREEN.
- **★ frontend merge gate FULLY UNBLOCKED** — QA-B71 Fixed @ `b47e85c`.
- **★ cross-stream merge FULLY UNBLOCKED** — BE Open 0 @ `aaa16f8`.
- **operation 승격 BLOCK** — merge(422) 미실행 · post-merge live E2E 미실행.

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-13T12:32:00+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-13 551차)

> test `@c7c8f07` 불변 · develop `@a5c2736`(+1 vs `e77b7e4`, UXD-94 lifecycle heading·copay aria-describedby) · WT **DIRTY 2M** · frontend **Open 1 BLOCK QA-B71** · merge pending **420** (231 FE + 189 BE) · **cross-stream merge BLOCK**

| 항목 | 값 |
|------|-----|
| test HEAD | `c7c8f07` |
| develop HEAD | `a5c2736` |
| ahead (`test..develop`) | 231 |
| test npm test | 217/217 PASS (50.95s) |
| test build | 781 modules (max 367.09 kB, 6.75s) |
| develop HEAD npm test | **1022/1022 PASS** (222 files, stash-clean) |
| develop WT npm test | **1023/1023 PASS** (+1 @Test WIP) |
| develop WT | **DIRTY 2M** (`MonthlyBenefitCapGuardPanel*`) |
| develop HEAD build | multi-chunk (index 559.65 kB >500 kB vite warn) |
| route count | 66 |
| audit | 0 (prod omit=dev) |
| origin/develop | @ `a5c2736` (동기화) |
| merge gate (frontend) | **BLOCK** (WT dirty · Open 1 QA-B71 · HEAD 1022/1022 PASS) |
| cross-stream merge | **BLOCK** (BE @ `8bb6583` WT CLEAN · Open 0 · 902/902 PASS · FE WT clean 선행) |

### TSR 551차 vs 549차

| 항목 | 549차 | 551차 |
|------|-------|-------|
| develop HEAD | `e77b7e4` | **`a5c2736`** (+1 UXD-94) |
| develop WT | **CLEAN** | **DIRTY 2M** |
| test npm test | 217/217 PASS | **217/217 PASS** |
| develop HEAD npm test | 1020/1020 PASS | **1022/1022 PASS** (+2 @Test) |
| develop WT npm test | — | **1023/1023 PASS** (+1 @Test WIP) |
| ahead | 230 | **231** |
| Open (frontend) | 0 | **1 BLOCK QA-B71** |
| merge gate (frontend) | FULLY UNBLOCKED | **BLOCK** |
| cross-stream merge | FULLY UNBLOCKED | **BLOCK** |
| merge pending | 418 | **420** |

### TSR 551차 판정

- **PASS(v1.2+v1.3-A @ test)** — test 브랜치 회귀 217/217 GREEN.
- **⚠ frontend merge gate BLOCK** — develop WT DIRTY 2M, Open 1 BLOCK QA-B71.
- **⚠ cross-stream merge BLOCK** — FE WT clean 선행 필요 (BE @8bb6583 Open 0).
- **operation 승격 BLOCK** — merge(420) 실행 금지 · post-merge live E2E 미실행.

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-13T11:47:00+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-13 549차)

> test `@c7c8f07` 불변 · develop `@e77b7e4`(+1 vs `6ef671b`, G9-COPAY-NAMING statutory wording) · WT **CLEAN** · frontend **Open 0** · merge pending **418** (230 FE + 188 BE) · **cross-stream merge FULLY UNBLOCKED**

| 항목 | 값 |
|------|-----|
| test HEAD | `c7c8f07` |
| develop HEAD | `e77b7e4` |
| ahead (`test..develop`) | 230 |
| test npm test | 217/217 PASS (50.91s) |
| test build | 781 modules (max 367.09 kB, 6.57s) |
| develop HEAD npm test | **1020/1020 PASS** (222 files, 174.13s, +3 @Test) |
| develop WT | **CLEAN** |
| develop HEAD build | multi-chunk (index 559.61 kB >500 kB vite warn, 6.17s) |
| route count | 66 |
| audit | 0 (prod omit=dev) |
| origin/develop | @ `e77b7e4` (동기화) |
| merge gate (frontend) | **FULLY UNBLOCKED** (WT clean · HEAD 1020/1020 PASS · Open 0) |
| cross-stream merge | **FULLY UNBLOCKED** (BE @ `edd2771` WT CLEAN · Open 0 · 897/897 PASS) |

### TSR 549차 vs 547차

| 항목 | 547차 | 549차 |
|------|-------|-------|
| develop HEAD | `6ef671b` | **`e77b7e4`** (+1 G9-COPAY-NAMING) |
| develop WT | **CLEAN** | **CLEAN** |
| test npm test | 217/217 PASS | **217/217 PASS** |
| develop HEAD npm test | 1017/1017 PASS | **1020/1020 PASS** (+3 @Test) |
| ahead | 229 | **230** |
| Open (frontend) | 0 | **0** |
| merge gate (frontend) | FULLY UNBLOCKED | **FULLY UNBLOCKED** |
| cross-stream merge | FULLY UNBLOCKED | **FULLY UNBLOCKED** |
| merge pending | 416 | **418** |

### TSR 549차 판정

- **PASS(v1.2+v1.3-A @ test)** — test 브랜치 회귀 217/217 GREEN.
- **★ frontend merge gate FULLY UNBLOCKED** — develop WT clean, HEAD 1020/1020 PASS, Open 0.
- **★ cross-stream merge FULLY UNBLOCKED** — backend @edd2771 WT clean, Open 0 (548차 G9-COG BE 반영).
- **operation 승격 BLOCK** — merge(418) 미실행 · post-merge live E2E 미실행.

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-13T11:25:00+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-13 547차)

> test `@c7c8f07` 불변 · develop `@6ef671b`(+1 vs `58256c6`, G9-COG cognitive support grade daily rate catalog FE) · WT **CLEAN** · frontend **Open 0** · merge pending **416** (229 FE + 187 BE) · **cross-stream merge FULLY UNBLOCKED**

| 항목 | 값 |
|------|-----|
| test HEAD | `c7c8f07` |
| develop HEAD | `6ef671b` |
| ahead (`test..develop`) | 229 |
| test npm test | 217/217 PASS (80.49s) |
| test build | 781 modules (max 367.09 kB, 6.97s) |
| develop HEAD npm test | **1017/1017 PASS** (222 files, 204.17s, +2 @Test) |
| develop WT | **CLEAN** |
| develop HEAD build | multi-chunk (index 559.29 kB >500 kB vite warn, 8.37s) |
| route count | 66 |
| audit | 0 (prod omit=dev) |
| origin/develop | @ `6ef671b` (동기화) |
| merge gate (frontend) | **FULLY UNBLOCKED** (WT clean · HEAD 1017/1017 PASS · Open 0) |
| cross-stream merge | **FULLY UNBLOCKED** (BE @ `2efc557` WT CLEAN · Open 0 · 894/894 PASS) |

### TSR 547차 vs 545차

| 항목 | 545차 | 547차 |
|------|-------|-------|
| develop HEAD | `58256c6` | **`6ef671b`** (+1 G9-COG catalog FE) |
| develop WT | **CLEAN** | **CLEAN** |
| test npm test | 217/217 PASS | **217/217 PASS** |
| develop HEAD npm test | 1015/1015 PASS | **1017/1017 PASS** (+2 @Test) |
| ahead | 228 | **229** |
| Open (frontend) | 0 | **0** |
| merge gate (frontend) | FULLY UNBLOCKED | **FULLY UNBLOCKED** |
| cross-stream merge | FULLY UNBLOCKED | **FULLY UNBLOCKED** |
| merge pending | 414 | **416** |

### TSR 547차 판정

- **PASS(v1.2+v1.3-A @ test)** — test 브랜치 회귀 217/217 GREEN.
- **★ frontend merge gate FULLY UNBLOCKED** — develop WT clean, HEAD 1017/1017 PASS, Open 0.
- **★ cross-stream merge FULLY UNBLOCKED** — backend @2efc557 WT clean, Open 0 (546차 G9-COG BE catalog 반영).
- **operation 승격 BLOCK** — merge(416) 미실행 · post-merge live E2E 미실행.

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-13T11:02:00+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-13 545차)

> test `@c7c8f07` 불변 · develop `@58256c6`(+1 vs `7668459`, FAQ21824 billing lifecycle checklist) · WT **CLEAN** · frontend **Open 0** · merge pending **414** (228 FE + 186 BE) · **cross-stream merge FULLY UNBLOCKED**

| 항목 | 값 |
|------|-----|
| test HEAD | `c7c8f07` |
| develop HEAD | `58256c6` |
| ahead (`test..develop`) | 228 |
| test npm test | 217/217 PASS (81.02s) |
| test build | 781 modules (max 367.09 kB, 6.48s) |
| develop HEAD npm test | **1015/1015 PASS** (222 files, 206.63s, +6 @Test) |
| develop WT | **CLEAN** |
| develop HEAD build | multi-chunk (index 558.64 kB >500 kB vite warn, 7.73s) |
| route count | 66 |
| audit | 0 (prod omit=dev) |
| origin/develop | @ `58256c6` (동기화) |
| merge gate (frontend) | **FULLY UNBLOCKED** (WT clean · HEAD 1015/1015 PASS · Open 0) |
| cross-stream merge | **FULLY UNBLOCKED** (BE @ `21eb0af` WT CLEAN · Open 0 · 886/886 PASS) |

### TSR 545차 vs 543차

| 항목 | 543차 | 545차 |
|------|-------|-------|
| develop HEAD | `7668459` | **`58256c6`** (+1 FAQ21824 checklist) |
| develop WT | **CLEAN** | **CLEAN** |
| test npm test | 217/217 PASS | **217/217 PASS** |
| develop HEAD npm test | 1009/1009 PASS | **1015/1015 PASS** (+6 @Test) |
| ahead | 227 | **228** |
| Open (frontend) | 0 | **0** |
| merge gate (frontend) | FULLY UNBLOCKED | **FULLY UNBLOCKED** |
| cross-stream merge | BLOCK (BE B70) | **FULLY UNBLOCKED** |
| merge pending | 412 | **414** |

### TSR 545차 판정

- **PASS(v1.2+v1.3-A @ test)** — test 브랜치 회귀 217/217 GREEN.
- **★ frontend merge gate FULLY UNBLOCKED** — develop WT clean, HEAD 1015/1015 PASS, Open 0.
- **★ cross-stream merge FULLY UNBLOCKED** — backend @21eb0af WT clean, Open 0 (544차 QA-B70 Fixed 반영).
- **operation 승격 BLOCK** — merge(414) 미실행 · post-merge live E2E 미실행.

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-13T10:38:00+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-13 543차)

> test `@c7c8f07` 불변 · develop `@7668459`(+1 vs `338c014`, QA-B69 Fixed) · WT **CLEAN** · frontend **Open 0** · merge pending **412** (227 FE + 185 BE) · **cross-stream merge BLOCK** (backend QA-B70)

| 항목 | 값 |
|------|-----|
| test HEAD | `c7c8f07` |
| develop HEAD | `7668459` |
| ahead (`test..develop`) | 227 |
| test npm test | 217/217 PASS (81.48s) |
| test build | 781 modules (max 367.09 kB, 10.27s) |
| develop HEAD npm test | **1009/1009 PASS** (221 files, 204.35s) |
| develop WT | **CLEAN** |
| develop HEAD build | multi-chunk (index 551.66 kB >500 kB vite warn, 6.12s) |
| route count | 66 |
| audit | 0 (prod omit=dev) |
| origin/develop | @ `7668459` (동기화) |
| merge gate (frontend) | **FULLY UNBLOCKED** (WT clean · HEAD 1009/1009 PASS · Open 0) |
| cross-stream merge | **BLOCK** (BE @ `6f6094d` WT DIRTY 2M · Open 1 QA-B70) |

### TSR 543차 vs 541차

| 항목 | 541차 | 543차 |
|------|-------|-------|
| develop HEAD | `338c014` | **`7668459`** (+1 QA-B69 Fixed) |
| develop WT | **DIRTY 1M** | **CLEAN** |
| test npm test | 217/217 PASS | **217/217 PASS** |
| develop HEAD npm test | 1008/1009 FAIL | **1009/1009 PASS** |
| ahead | 226 | **227** |
| Open (frontend) | 1 BLOCK QA-B69 | **0** |
| merge gate (frontend) | BLOCK | **FULLY UNBLOCKED** |
| cross-stream merge | BLOCK (FE) | **BLOCK** (BE B70) |
| merge pending | 411 | **412** |

### TSR 543차 판정

- **PASS(v1.2+v1.3-A @ test)** — test 브랜치 회귀 217/217 GREEN.
- **★ frontend merge gate FULLY UNBLOCKED** — QA-B69 Fixed @ `7668459`, develop WT clean, HEAD 1009/1009 PASS.
- **⚠ cross-stream merge BLOCK** — backend QA-B70 (BillingService 2M uncommitted).
- **operation 승격 BLOCK** — merge(412) 미실행 · post-merge live E2E 미실행.

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-13T10:03:44+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-13 541차)

> test `@c7c8f07` 불변 · develop `@338c014` HEAD **불변** · WT **DIRTY 1M**(`BillingPage.test.jsx`) · frontend **Open 1 BLOCK QA-B69** · merge pending **411** (226 FE + 185 BE) · **cross-stream merge BLOCK**

| 항목 | 값 |
|------|-----|
| test HEAD | `c7c8f07` |
| develop HEAD | `338c014` |
| ahead (`test..develop`) | 226 |
| test npm test | 217/217 PASS (79.24s) |
| test build | 781 modules (max 367.09 kB, 6.32s) |
| develop HEAD npm test | **1008/1009 FAIL** (173.17s, stash 검증) |
| develop WT npm test | **1009/1009 PASS** (221 files, 202.07s) |
| develop WT | **DIRTY 1M** — `BillingPage.test.jsx` guard title assertion |
| develop HEAD build | multi-chunk (index 551.66 kB >500 kB vite warn, 7.70s) |
| route count | 66 |
| audit | 0 (prod omit=dev) |
| origin/develop | @ `338c014` (동기화) |
| merge gate (frontend) | **BLOCK** (WT dirty · HEAD test FAIL · Open 1 QA-B69) |
| cross-stream merge | **BLOCK** (BE @ `6f6094d` WT CLEAN · Open 0) |

### TSR 541차 vs 539차

| 항목 | 539차 | 541차 |
|------|-------|-------|
| develop HEAD | `338c014` | **`338c014`** (불변) |
| develop WT | **CLEAN** | **DIRTY 1M** (QA-B69 fix WIP) |
| test npm test | 217/217 PASS | **217/217 PASS** |
| develop HEAD npm test | 1008/1009 FAIL | **1008/1009 FAIL** (재현) |
| develop WT npm test | — | **1009/1009 PASS** |
| Open (frontend) | 1 BLOCK QA-B69 | **1 BLOCK QA-B69** (B07 recurrence — commit 필요) |
| merge gate (frontend) | BLOCK | **BLOCK** |
| merge pending | 411 | **411** |

### TSR 541차 판정

- **PASS(v1.2+v1.3-A @ test)** — test 브랜치 회귀 217/217 GREEN.
- **⚠ frontend merge gate BLOCK** — QA-B69 assertion fix가 WT에만 존재(미커밋). COD: `BillingPage.test.jsx` 커밋 → WT clean → tester merge(411).

---

# develop ↔ test diff 메타 — frontend (2026-06-13 539차)

> test `@c7c8f07` 불변 · develop `@338c014`(+2 vs `02cbd05`) · WT **CLEAN** · frontend **Open 1 BLOCK QA-B69** · merge pending **411** (226 FE + 185 BE) · **cross-stream merge BLOCK**

| 항목 | 값 |
|------|-----|
| test HEAD | `c7c8f07` |
| develop HEAD | `338c014` |
| ahead (`test..develop`) | 226 |
| test npm test | 217/217 PASS (51.89s) |
| test build | 781 modules (max 367.09 kB, 6.85s) |
| develop HEAD npm test | **1008/1009 FAIL** (189.99s) |
| develop HEAD build | multi-chunk (index 551.66 kB >500 kB vite warn, 6.18s) |
| route count | 66 |
| audit | 0 (prod omit=dev) |
| origin/develop | @ `338c014` (동기화) |
| merge gate (frontend) | **BLOCK** (HEAD test FAIL · Open 1 QA-B69) |
| cross-stream merge | **BLOCK** (BE @ `6f6094d` WT CLEAN · Open 0) |

### TSR 539차 vs 537차

| 항목 | 537차 | 539차 |
|------|-------|-------|
| develop HEAD | `02cbd05` (+1: US-R02 staff status report) | **`338c014`** (+2: G-7x-1 prior-deposit UX guard) |
| develop WT | **CLEAN** | **CLEAN** |
| test npm test | 217/217 PASS | **217/217 PASS** |
| develop HEAD npm test | 1001/1001 PASS | **1008/1009 FAIL** |
| route count | 65 | **66** |
| ahead | 224 | **226** |
| Open (frontend) | 0 | **1 BLOCK QA-B69** |
| merge gate (frontend) | FULLY UNBLOCKED | **BLOCK** |
| cross-stream merge | FULLY UNBLOCKED | **BLOCK** |
| merge pending | 408 | **411** |
| backend develop | `8487667` | **`6f6094d`** |

### TSR 539차 판정

- **PASS(v1.2+v1.3-A @ test)** — test 브랜치 회귀 217/217 GREEN.
- **⚠ frontend merge gate BLOCK** — `@338c014` G-7x-1 guard banner title 변경 후 `BillingPage.test.jsx` 미갱신.
- **⚠ cross-stream merge BLOCK** — FE HEAD test fix 선행.
- **operation 승격 BLOCK** — merge(411) 미실행 · post-merge live E2E 미실행.

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-13T09:00:00+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-13 537차)

> test `@c7c8f07` 불변 · develop `@02cbd05`(+1 vs `8bbba4d`) · WT **CLEAN** · frontend **Open 0** · merge pending **408** (224 FE + 184 BE) · **cross-stream merge FULLY UNBLOCKED**

| 항목 | 값 |
|------|-----|
| test HEAD | `c7c8f07` |
| develop HEAD | `02cbd05` |
| ahead (`test..develop`) | 224 |
| test npm test | 217/217 PASS (79.55s) |
| test build | 781 modules (max 367.09 kB, 7.33s) |
| develop HEAD npm test | **1001/1001 PASS** (204.38s) |
| develop HEAD build | 923 modules (index 548.84 kB >500 kB vite warn, 6.42s) |
| route count | 65 (+1 `/staff/reports/status`) |
| audit | 0 (prod omit=dev) |
| origin/develop | @ `02cbd05` (동기화) |
| merge gate (frontend) | **FULLY UNBLOCKED** (WT CLEAN · HEAD test PASS · Open 0) |
| cross-stream merge | **FULLY UNBLOCKED** (BE @ `8487667` WT CLEAN · Open 0) |

### TSR 537차 vs 535차

| 항목 | 535차 | 537차 |
|------|-------|-------|
| develop HEAD | `8bbba4d` (+1: G42/G34b live API harness) | **`02cbd05`** (+1: US-R02 staff status report page) |
| develop WT | **CLEAN** | **CLEAN** |
| test npm test | 217/217 PASS | **217/217 PASS** |
| develop HEAD npm test | 994/994 PASS | **1001/1001 PASS** (+7 @Test) |
| develop build modules | 921 | **923** |
| route count | 64 | **65** |
| ahead | 223 | **224** |
| Open (frontend) | 0 | **0** |
| merge gate (frontend) | FULLY UNBLOCKED | **FULLY UNBLOCKED** |
| cross-stream merge | FULLY UNBLOCKED | **FULLY UNBLOCKED** |
| merge pending | 406 | **408** |
| backend develop | `b6ecc35` | **`8487667`** |

### TSR 537차 판정

- **PASS(v1.2+v1.3-A @ test)** — test 브랜치 회귀 217/217 GREEN.
- **★ frontend merge gate FULLY UNBLOCKED** — develop HEAD **1001/1001 PASS** · US-R02 staff status report @ `/staff/reports/status`.
- **★ cross-stream merge FULLY UNBLOCKED** — backend `@8487667` WT CLEAN · Open 0.
- **operation 승격 BLOCK** — merge(408) 미실행 · post-merge live E2E 미실행.

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-13T08:41:24+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-13 535차)

> test `@c7c8f07` 불변 · develop `@8bbba4d`(+1 vs `994f5ea`) · WT **CLEAN** · frontend **Open 0** · merge pending **406** (223 FE + 183 BE) · **cross-stream merge FULLY UNBLOCKED**

| 항목 | 값 |
|------|-----|
| test HEAD | `c7c8f07` |
| develop HEAD | `8bbba4d` |
| ahead (`test..develop`) | 223 |
| test npm test | 217/217 PASS (50.48s) |
| test build | 781 modules (max 367.09 kB, 6.61s) |
| develop HEAD npm test | **994/994 PASS** (171.84s) |
| develop HEAD build | 921 modules (index 547.83 kB >500 kB vite warn, 6.06s) |
| route count | 64 |
| audit | 0 (prod omit=dev) |
| origin/develop | @ `8bbba4d` (동기화) |
| merge gate (frontend) | **FULLY UNBLOCKED** (WT CLEAN · HEAD test PASS · Open 0) |
| cross-stream merge | **FULLY UNBLOCKED** (BE @ `b6ecc35` WT CLEAN · Open 0) |

### TSR 535차 vs 533차

| 항목 | 533차 | 535차 |
|------|-------|-------|
| develop HEAD | `994f5ea` (+1: G34b cognitive role guard) | **`8bbba4d`** (+1: G42/G34b live API harness·pilot E2E) |
| develop WT | **CLEAN** | **CLEAN** |
| test npm test | 217/217 PASS | **217/217 PASS** |
| develop HEAD npm test | 991/991 PASS | **994/994 PASS** (+3 @Test) |
| develop build modules | 921 | **921** |
| ahead | 222 | **223** |
| Open (frontend) | 0 | **0** |
| merge gate (frontend) | FULLY UNBLOCKED | **FULLY UNBLOCKED** |
| cross-stream merge | FULLY UNBLOCKED | **FULLY UNBLOCKED** |
| merge pending | 404 | **406** |
| backend develop | `bccf978` | **`b6ecc35`** |

### TSR 535차 판정

- **PASS(v1.2+v1.3-A @ test)** — test 브랜치 회귀 217/217 GREEN.
- **★ frontend merge gate FULLY UNBLOCKED** — develop HEAD **994/994 PASS** · G42/G34b live API harness·pilot E2E.
- **★ cross-stream merge FULLY UNBLOCKED** — backend `@b6ecc35` WT CLEAN · Open 0.
- **operation 승격 BLOCK** — merge(406) 미실행 · post-merge live E2E 미실행.

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-13T08:13:29+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-13 533차)

> test `@c7c8f07` 불변 · develop `@994f5ea`(+1 vs `b0a9e06`) · WT **CLEAN** · frontend **Open 0** · merge pending **404** (222 FE + 182 BE) · **cross-stream merge FULLY UNBLOCKED**

| 항목 | 값 |
|------|-----|
| test HEAD | `c7c8f07` |
| develop HEAD | `994f5ea` |
| ahead (`test..develop`) | 222 |
| test npm test | 217/217 PASS (79.95s) |
| test build | 781 modules (max 367.09 kB, 5.51s) |
| develop HEAD npm test | **991/991 PASS** (200.45s) |
| develop HEAD build | 921 modules (index 547.83 kB >500 kB vite warn, 6.92s) |
| route count | 64 |
| audit | 0 (prod omit=dev) |
| origin/develop | @ `994f5ea` (동기화) |
| merge gate (frontend) | **FULLY UNBLOCKED** (WT CLEAN · HEAD test PASS · Open 0) |
| cross-stream merge | **FULLY UNBLOCKED** (BE @ `bccf978` WT CLEAN · Open 0) |

### TSR 533차 vs 531차

| 항목 | 531차 | 533차 |
|------|-------|-------|
| develop HEAD | `b0a9e06` (+1: G42 grievance counseling UI) | **`994f5ea`** (+1: G34b cognitive role guard) |
| develop WT | **CLEAN** | **CLEAN** |
| test npm test | 217/217 PASS | **217/217 PASS** |
| develop HEAD npm test | 989/989 PASS | **991/991 PASS** (+2 @Test) |
| develop build modules | 921 | **921** |
| ahead | 221 | **222** |
| Open (frontend) | 0 | **0** |
| merge gate (frontend) | FULLY UNBLOCKED | **FULLY UNBLOCKED** |
| cross-stream merge | FULLY UNBLOCKED | **FULLY UNBLOCKED** |
| merge pending | 402 | **404** |
| backend develop | `0460e9b` | **`bccf978`** |

### TSR 533차 판정

- **PASS(v1.2+v1.3-A @ test)** — test 브랜치 회귀 217/217 GREEN.
- **★ frontend merge gate FULLY UNBLOCKED** — develop HEAD **991/991 PASS** · G34b work-log save cognitive role guard.
- **★ cross-stream merge FULLY UNBLOCKED** — backend `@bccf978` WT CLEAN · Open 0.
- **operation 승격 BLOCK** — merge(404) 미실행 · post-merge live E2E 미실행.

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-13T07:54:02+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-13 531차)

> test `@c7c8f07` 불변 · develop `@b0a9e06`(+1 vs `db21e85`) · WT **CLEAN** · frontend **Open 0** · merge pending **402** (221 FE + 181 BE) · **cross-stream merge FULLY UNBLOCKED**

| 항목 | 값 |
|------|-----|
| test HEAD | `c7c8f07` |
| develop HEAD | `b0a9e06` |
| ahead (`test..develop`) | 221 |
| test npm test | 217/217 PASS (76.31s) |
| test build | 781 modules (max 367.09 kB, 9.42s) |
| develop HEAD npm test | **989/989 PASS** (241.27s) |
| develop HEAD build | 921 modules (index 547.83 kB >500 kB vite warn, 9.29s) |
| route count | 64 |
| audit | 0 (prod omit=dev) |
| origin/develop | @ `b0a9e06` (동기화) |
| merge gate (frontend) | **FULLY UNBLOCKED** (WT CLEAN · HEAD test PASS · Open 0) |
| cross-stream merge | **FULLY UNBLOCKED** (BE @ `0460e9b` WT CLEAN · Open 0) |

### TSR 531차 vs 529차

| 항목 | 529차 | 531차 |
|------|-------|-------|
| develop HEAD | `db21e85` (+1: QA-B68 test fix) | **`b0a9e06`** (+1: G42 grievance counseling UI) |
| develop WT | **CLEAN** | **CLEAN** |
| test npm test | 217/217 PASS | **217/217 PASS** |
| develop HEAD npm test | 979/979 PASS | **989/989 PASS** (+10 @Test) |
| develop build modules | 919 | **921** |
| ahead | 220 | **221** |
| Open (frontend) | 0 | **0** |
| merge gate (frontend) | FULLY UNBLOCKED | **FULLY UNBLOCKED** |
| cross-stream merge | FULLY UNBLOCKED | **FULLY UNBLOCKED** |
| merge pending | 400 | **402** |
| backend develop | `bcdc411` | **`0460e9b`** |

### TSR 531차 판정

- **PASS(v1.2+v1.3-A @ test)** — test 브랜치 회귀 217/217 GREEN.
- **★ frontend merge gate FULLY UNBLOCKED** — develop HEAD **989/989 PASS** · G42 `/staff/grievance-counselings` wired.
- **★ cross-stream merge FULLY UNBLOCKED** — BE `@0460e9b` WT CLEAN · Open 0.
- **잔여**: **tester merge(402)** → post-merge live E2E (`scripts/run-live-e2e.sh`).

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-13T07:25:23+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-13 529차)

> test `@c7c8f07` 불변 · develop `@db21e85`(+1 vs `1b5fabe`) · WT **CLEAN** · frontend **Open 0** · **QA-B68 Fixed** · merge pending **400** (220 FE + 180 BE) · **cross-stream merge FULLY UNBLOCKED**

| 항목 | 값 |
|------|-----|
| test HEAD | `c7c8f07` |
| develop HEAD | `db21e85` |
| ahead (`test..develop`) | 220 |
| test npm test | 217/217 PASS (79.73s) |
| test build | 781 modules (max 367.09 kB, 6.33s) |
| develop HEAD npm test | **979/979 PASS** (198.31s) |
| develop HEAD build | 919 modules (index 546.98 kB >500 kB vite warn, 7.60s) |
| route count | 64 |
| audit | 0 (prod omit=dev) |
| origin/develop | @ `db21e85` (동기화) |
| merge gate (frontend) | **FULLY UNBLOCKED** (WT CLEAN · HEAD test PASS · Open 0) |
| cross-stream merge | **FULLY UNBLOCKED** (BE @ `bcdc411` WT CLEAN · Open 0) |

### TSR 529차 vs 527차

| 항목 | 527차 | 529차 |
|------|-------|-------|
| develop HEAD | `1b5fabe` (+2: UXD-92·G34b) | **`db21e85`** (+1: QA-B68 test fix) |
| develop WT | **CLEAN** | **CLEAN** |
| test npm test | 217/217 PASS | **217/217 PASS** |
| develop HEAD npm test | 978/979 FAIL | **979/979 PASS** |
| ahead | 219 | **220** |
| Open (frontend) | 1 BLOCK QA-B68 | **0** |
| merge gate (frontend) | BLOCK | **FULLY UNBLOCKED** |
| cross-stream merge | BLOCK | **FULLY UNBLOCKED** |
| merge pending | 398 | **400** |
| backend develop | `b459f4c` | **`bcdc411`** |

### TSR 529차 판정

- **PASS(v1.2+v1.3-A @ test)** — test 브랜치 회귀 217/217 GREEN.
- **★ frontend merge gate FULLY UNBLOCKED** — QA-B68 Fixed @ `db21e85` · develop HEAD **979/979 PASS**.
- **★ cross-stream merge FULLY UNBLOCKED** — BE `@bcdc411` WT CLEAN · Open 0.
- **잔여**: **tester merge(400)** → post-merge live E2E (`scripts/run-live-e2e.sh`).

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-13T07:07:16+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-13 527차)

> test `@c7c8f07` 불변 · develop `@1b5fabe`(+2 vs `3c7d2c7`) · WT **CLEAN** · frontend **Open 1 BLOCK QA-B68** · merge pending **398** (219 FE + 179 BE) · **cross-stream merge BLOCK**

| 항목 | 값 |
|------|-----|
| test HEAD | `c7c8f07` |
| develop HEAD | `1b5fabe` |
| ahead (`test..develop`) | 219 |
| test npm test | 217/217 PASS (50.39s) |
| test build | 781 modules (max 367.09 kB, 5.20s) |
| develop HEAD npm test | **978/979 FAIL** (167.79s) |
| route count | 63 |
| audit | 0 (prod omit=dev) |
| origin/develop | @ `1b5fabe` (동기화) |
| merge gate (frontend) | **BLOCK** (WT CLEAN · HEAD test FAIL · Open 1 BLOCK QA-B68) |
| cross-stream merge | **BLOCK** (BE @ `b459f4c` WT CLEAN · Open 0) |

### TSR 527차 vs 525차

| 항목 | 525차 | 527차 |
|------|-------|-------|
| develop HEAD | `3c7d2c7` (+1: QA-B67 fix) | **`1b5fabe`** (+2: UXD-92·G34b) |
| develop WT | **CLEAN** | **CLEAN** |
| test npm test | 217/217 PASS | **217/217 PASS** |
| develop HEAD npm test | 965/965 PASS | **978/979 FAIL** |
| ahead | 217 | **219** |
| Open (frontend) | 0 | **1 BLOCK QA-B68** |
| merge gate (frontend) | FULLY UNBLOCKED | **BLOCK** |
| cross-stream merge | FULLY UNBLOCKED | **BLOCK** |
| merge pending | 395 | **398** |
| backend develop | `2925ff7` | **`b459f4c`** |

### TSR 527차 판정

- **PASS(v1.2+v1.3-A @ test)** — test 브랜치 회귀 217/217 GREEN.
- **⚠ frontend merge gate BLOCK** — QA-B68 Open · develop HEAD test **978/979 FAIL** (`CarePlanNotificationPage.test.jsx` UXD-92 aria-label).
- **⚠ cross-stream merge BLOCK** — FE HEAD test fix 선행.
- **잔여**: COD `CarePlanNotificationPage.test.jsx` 수정→HEAD PASS→tester merge(398) → post-merge live E2E (`scripts/run-live-e2e.sh`).

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-13T06:34:36+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-13 525차)

> test `@c7c8f07` 불변 · develop `@3c7d2c7`(+1 vs `d41546f`) · WT **CLEAN** · frontend **Open 0** · merge pending **395** (217 FE + 178 BE) · **cross-stream merge FULLY UNBLOCKED**

| 항목 | 값 |
|------|-----|
| test HEAD | `c7c8f07` |
| develop HEAD | `3c7d2c7` |
| ahead (`test..develop`) | 217 |
| test npm test | 217/217 PASS (169.19s) |
| test build | 781 modules (max 367.09 kB, 22.18s) |
| develop HEAD npm test | 965/965 PASS (388.09s) |
| route count | 64 |
| audit | 0 (prod omit=dev) |
| origin/develop | @ `3c7d2c7` (동기화) |
| merge gate (frontend) | **FULLY UNBLOCKED** (WT CLEAN · Open 0 · QA-B67 Fixed) |
| cross-stream merge | **FULLY UNBLOCKED** (BE @ `2925ff7` WT CLEAN · Open 0) |

### TSR 525차 vs 523차

| 항목 | 523차 | 525차 |
|------|-------|-------|
| develop HEAD | `d41546f` (불변) | **`3c7d2c7`** (+1: QA-B67 fix) |
| develop WT | **DIRTY 2M** | **CLEAN** |
| test npm test | 217/217 PASS | **217/217 PASS** |
| develop HEAD npm test | 963/963 PASS | **965/965 PASS** |
| ahead | 216 | **217** |
| Open (frontend) | 1 BLOCK QA-B67 | **0** |
| merge gate (frontend) | BLOCK | **FULLY UNBLOCKED** |
| cross-stream merge | BLOCK (BE QA-B66) | **FULLY UNBLOCKED** (BE QA-B66 Fixed) |
| merge pending | 393 | **395** |
| backend develop | `dc48933` DIRTY 1M | **`2925ff7` CLEAN** |

### TSR 525차 판정

- **PASS(v1.2+v1.3-A @ test)** — test 브랜치 회귀 217/217 GREEN.
- **★ frontend merge gate FULLY UNBLOCKED** — QA-B67 Fixed @ `3c7d2c7` · WT CLEAN · Open 0.
- **★ cross-stream merge FULLY UNBLOCKED** — backend QA-B66 Fixed @ `2925ff7`.
- **잔여**: tester develop→test merge(395) → post-merge live E2E (`scripts/run-live-e2e.sh`).

---

# develop ↔ test diff 메타 — frontend (2026-06-13 523차)

> test `@c7c8f07` 불변 · develop `@d41546f` HEAD **불변** · WT **DIRTY 2M** · frontend **Open 1 BLOCK QA-B67** · merge pending **393** (216 FE + 177 BE) · **cross-stream merge BLOCK**

| 항목 | 값 |
|------|-----|
| test HEAD | `c7c8f07` |
| develop HEAD | `d41546f` |
| ahead (`test..develop`) | 216 |
| test npm test | 217/217 PASS (51.82s) |
| test build | 781 modules (max 367.09 kB, 6.91s) |
| develop HEAD npm test | 963/963 PASS |
| develop WT npm test | 965/965 PASS (+2 @Test, 163.32s) |
| route count | 64 |
| audit | 0 (prod omit=dev) |
| origin/develop | @ `d41546f` (동기화) |
| merge gate (frontend) | **BLOCK** (WT DIRTY 2M · Open 1 QA-B67) |
| cross-stream merge | **BLOCK** (BE @ `dc48933` WT DIRTY 1M · Open 1 QA-B66) |

### TSR 523차 vs 521차

| 항목 | 521차 | 523차 |
|------|-------|-------|
| develop HEAD | `d41546f` | `d41546f` (불변) |
| develop WT | CLEAN | **DIRTY 2M** (`http.js`·`http.test.js`) |
| test npm test | 217/217 PASS | **217/217 PASS** |
| develop HEAD npm test | 963/963 PASS | 963/963 PASS |
| develop WT npm test | — | **965/965 PASS** (+2 @Test) |
| ahead | 216 | **216** |
| Open (frontend) | 0 | **1 BLOCK QA-B67** |
| merge gate (frontend) | FULLY UNBLOCKED | **BLOCK** |
| cross-stream merge | FULLY UNBLOCKED | **BLOCK** (BE QA-B66) |
| merge pending | 393 | **393** |
| backend develop | `dc48933` CLEAN | `dc48933` **DIRTY 1M** (QA-B66) |

### TSR 523차 판정

- **PASS(v1.2+v1.3-A @ test)** — test 브랜치 회귀 217/217 GREEN.
- **⚠ frontend merge gate BLOCK** — FE develop WT DIRTY 2M · Open 1 BLOCK QA-B67.
- **⚠ cross-stream merge BLOCK** — backend QA-B66 동반 (양 스트림 WT clean 선행).
- **잔여**: COD `http.js`·`http.test.js` + `VisitServiceTest.java` 커밋/revert → WT clean → tester merge(393) → post-merge live E2E.

---

# develop ↔ test diff 메타 — frontend (2026-06-13 521차)

> test `@c7c8f07` 불변 · develop `@d41546f`(+1 vs `0ce04ad`) · WT **CLEAN** · frontend **Open 0** · merge pending **393** (216 FE + 177 BE) · **cross-stream merge FULLY UNBLOCKED**

| 항목 | 값 |
|------|-----|
| test HEAD | `c7c8f07` |
| develop HEAD | `d41546f` |
| ahead (`test..develop`) | 216 |
| test npm test | 217/217 PASS (51.08s) |
| test build | 781 modules (max 367.09 kB, 6.77s) |
| develop HEAD npm test | 963/963 PASS (212 files, 171.51s) |
| develop HEAD build | 922 modules (index 545.84 kB >500 kB vite warn, 6.13s) |
| route count | 64 |
| audit | 0 (prod omit=dev) |
| origin/develop | @ `d41546f` (동기화) |
| merge gate (frontend) | **FULLY UNBLOCKED** (WT CLEAN · Open 0) |
| cross-stream merge | **FULLY UNBLOCKED** (BE @ `dc48933` WT CLEAN · Open 0) |

### TSR 521차 vs 519차

| 항목 | 519차 | 521차 |
|------|-------|-------|
| develop HEAD | `0ce04ad` | `d41546f` (+1) |
| develop WT | CLEAN | **CLEAN** |
| test npm test | 217/217 PASS | **217/217 PASS** |
| develop HEAD npm test | 미재실행 | **963/963 PASS** (+10 @Test vs 953) |
| ahead | 215 | **216** |
| Open (frontend) | 0 | **0** |
| merge gate (frontend) | FULLY UNBLOCKED | **FULLY UNBLOCKED** |
| cross-stream merge | BLOCK (BE QA-B65) | **FULLY UNBLOCKED** (BE QA-B65 Fixed @ `dc48933`) |
| merge pending | 391 | **393** (216+177) |
| backend develop | `a7b4a39` DIRTY 4M | `dc48933` **CLEAN** |

### TSR 521차 판정

- **PASS(v1.2+v1.3-A @ test)** — test 브랜치 회귀 217/217 GREEN.
- **★ frontend merge gate FULLY UNBLOCKED** — FE develop WT CLEAN · Open 0 · HEAD 963/963 PASS.
- **★ cross-stream merge FULLY UNBLOCKED** — backend QA-B65 Fixed @ `dc48933`.
- **operation 승격 BLOCK** — develop→test merge 미실행(393 commits) · post-merge live E2E 미실행.

### planner/COD 액션

1. **tester**: develop→test merge(393) 실행
2. **tester**: post-merge `scripts/run-live-e2e.sh` (backend `localhost:8080` 필요)
3. **COD/OPS**: SEC-D22 `.gitignore` (infra·BLOCK 아님)

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-13T05:31:10+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-13 519차)

> test `@c7c8f07` 불변 · develop `@0ce04ad`(+1 vs `6657d90`) · WT **CLEAN** · frontend **Open 0** · merge pending **391** (215 FE + 176 BE) · **cross-stream merge BLOCK**(backend QA-B65)

| 항목 | 값 |
|------|-----|
| test HEAD | `c7c8f07` |
| develop HEAD | `0ce04ad` |
| ahead (`test..develop`) | 215 |
| test npm test | 217/217 PASS (50.38s) |
| test build | 781 modules (max 367.09 kB, 4.85s) |
| develop HEAD npm test | 미재실행 (read-only 정책) |
| develop HEAD build | 미재실행 (read-only 정책) |
| route count | 64 (직전 517차 기준) |
| audit | 0 (prod omit=dev) |
| origin/develop | @ `0ce04ad` (동기화) |
| merge gate (frontend) | **FULLY UNBLOCKED** (WT CLEAN · Open 0) |
| cross-stream merge | **BLOCK** (BE @ `a7b4a39` WT DIRTY 4M · Open 1 QA-B65) |

### TSR 519차 vs 517차

| 항목 | 517차 | 519차 |
|------|-------|-------|
| develop HEAD | `6657d90` | `0ce04ad` (+1) |
| develop WT | CLEAN | **CLEAN** |
| test npm test | 217/217 PASS | **217/217 PASS** |
| develop HEAD npm test | 953/953 PASS | **미재실행** |
| ahead | 214 | **215** |
| Open (frontend) | 0 | **0** |
| merge gate (frontend) | FULLY UNBLOCKED | **FULLY UNBLOCKED** |
| cross-stream merge | BLOCK (BE QA-B65) | **BLOCK** (BE QA-B65) |
| merge pending | 390 | **391** (215+176) |
| backend develop | `a7b4a39` CLEAN (515차 오판) | `a7b4a39` **DIRTY 4M** |

### TSR 519차 판정

- **PASS(v1.2+v1.3-A @ test)** — test 브랜치 회귀 217/217 GREEN.
- **★ frontend merge gate FULLY UNBLOCKED** — FE develop WT CLEAN · Open 0.
- **⚠ cross-stream merge BLOCK** — backend QA-B65(4M WIP) 선행 해소 필요.
- **operation 승격 BLOCK** — develop→test merge 미실행(391 commits) · post-merge live E2E 미실행.

### planner/COD 액션

1. **COD**: backend 4M WIP 커밋/revert → WT clean (QA-B65)
2. **tester**: develop→test merge(391) 실행
3. **tester**: post-merge `scripts/run-live-e2e.sh` (backend `localhost:8080` 필요)

---

# develop ↔ test diff 메타 — frontend (2026-06-13 513차)

> test `@c7c8f07` 불변 · develop `@22325f4`(+1 vs `72676a5`) · WT **CLEAN** · frontend **Open 0** · merge pending **386** (211 FE + 175 BE) · **양 스트림 merge FULLY UNBLOCKED**

| 항목 | 값 |
|------|-----|
| test HEAD | `c7c8f07` |
| develop HEAD | `22325f4` |
| ahead (`test..develop`) | 211 |
| test npm test | 217/217 PASS (51.11s) |
| test build | 781 modules (max 367.09 kB, 4.90s) |
| audit | 0 (prod omit=dev) |
| origin/develop | @ `22325f4` (동기화) |
| merge gate (frontend) | **FULLY UNBLOCKED** (WT CLEAN · Open 0) |
| cross-stream merge | **FULLY UNBLOCKED** (BE @ `bdfc140` WT CLEAN · Open 0) |

### TSR 513차 vs 511차

| 항목 | 511차 | 513차 |
|------|-------|-------|
| develop HEAD | `72676a5` | `22325f4` (+1) |
| develop WT | CLEAN | **CLEAN** |
| test npm test | 217/217 PASS | **217/217 PASS** |
| ahead | 210 | **211** |
| Open (frontend) | 0 | **0** |
| merge gate (frontend) | FULLY UNBLOCKED | **FULLY UNBLOCKED** |
| cross-stream merge | FULLY UNBLOCKED | **FULLY UNBLOCKED** |
| merge pending | 384 | **386** (211+175) |
| backend develop | `84e59d2` CLEAN | `bdfc140` **CLEAN** |

### TSR 513차 판정

- **PASS(v1.2+v1.3-A @ test)** — test 브랜치 회귀 217/217 GREEN.
- **★ 양 스트림 merge gate FULLY UNBLOCKED** — FE/BE develop WT CLEAN · Open 0.
- **operation 승격 BLOCK** — develop→test merge 미실행(386 commits) · post-merge live E2E 미실행.

### planner/COD 액션

1. **tester**: develop→test merge(386) 실행 (`scripts/git_merge_to_test.sh` 또는 파이프라인)
2. **tester**: post-merge `scripts/run-live-e2e.sh` (backend `localhost:8080` 필요)
3. **COD**: merge 이후 live E2E 실패 시 QA_FEEDBACK Open 템플릿으로 즉시 회귀 등록

---

# develop ↔ test diff 메타 — frontend (2026-06-13 507차)

> test `@c7c8f07` 불변 · develop `@2f5af63` HEAD **불변** · WT **DIRTY 2M** · frontend **Open 1 BLOCK QA-B62 recurrence** · merge pending **380** (208 FE + 172 BE) · **양 스트림 merge BLOCK**

| 항목 | 값 |
|------|-----|
| test HEAD | `c7c8f07` |
| develop HEAD | `2f5af63` |
| ahead (`test..develop`) | 208 |
| test npm test | 217/217 PASS (52.41s) |
| develop HEAD npm test | 929/929 PASS |
| develop WT npm test | 931/931 PASS (+2 @Test, 163.02s) |
| test build | 781 modules (max 367.09 kB, 6.93s) |
| develop HEAD build | 911 modules (index 528.97 kB >500 kB vite warn, 8.34s) |
| audit | 0 (prod omit=dev) |
| origin/develop | @ `2f5af63` (동기화) |
| merge gate (frontend) | **BLOCK** (WT DIRTY 2M · Open 1 BLOCK QA-B62 recurrence) |
| cross-stream merge | **BLOCK** (BE @ `f0752b6` WT DIRTY 2M · Open 1 BLOCK QA-B64) |

### TSR 507차 vs 505차

| 항목 | 505차 | 507차 |
|------|-------|-------|
| develop HEAD | `2f5af63` | `2f5af63` (불변) |
| develop WT | CLEAN | **DIRTY 2M** (505 CLEAN→재오염) |
| test npm test | 217/217 PASS | **217/217 PASS** (불변) |
| develop HEAD npm test | 929/929 PASS | **929/929 PASS** (불변) |
| develop WT npm test | N/A | **931/931 PASS** (+2 @Test) |
| ahead | 208 | **208** (불변) |
| Open (frontend) | 0 | **1 BLOCK QA-B62 recurrence** |
| merge gate (frontend) | FULLY UNBLOCKED | **BLOCK** |
| cross-stream merge | FULLY UNBLOCKED | **BLOCK** (BE+FE WT dirty) |
| merge pending | 380 | **380** (208+172) |
| backend develop | `f0752b6` CLEAN | `f0752b6` **DIRTY 2M** (QA-B64) |

### TSR 507차 판정

- **PASS(v1.2+v1.3-A @ test)** — test 브랜치 회귀 217/217 GREEN.
- **merge gate BLOCK** — develop WT DIRTY 2M(`http.js`·`http.test.js`) · QA-B62 recurrence.
- **cross-stream BLOCK** — backend WT DIRTY 2M(QA-B64) 동시 존재.
- **COD 선행**: FE `http.js`·`http.test.js` + BE `ClientRiskAssessmentService*` 각 커밋/revert → WT clean → TSR 재검증 → tester merge(380).

---

# develop ↔ test diff 메타 — frontend (2026-06-13 505차)

> test `@c7c8f07` 불변 · develop `@2f5af63`(+1 vs `9f80082`) · WT **CLEAN** · frontend **Open 0** · merge pending **380** (208 FE + 172 BE) · **양 스트림 merge FULLY UNBLOCKED**

| 항목 | 값 |
|------|-----|
| test HEAD | `c7c8f07` |
| develop HEAD | `2f5af63` |
| ahead (`test..develop`) | 208 |
| diff stat | 364 files (+47534/-1262, HEAD 기준) |
| test npm test | 217/217 PASS (49.78s) |
| develop HEAD npm test | 929/929 PASS (208 files, 162.81s) |
| develop WT npm test | N/A (WT CLEAN) |
| test build | 781 modules (max 367.09 kB, 6.54s) |
| develop HEAD build | 911 modules (index 528.89 kB >500 kB vite warn, 5.99s) |
| audit | 0 (prod omit=dev) |
| routes | 63 route |
| origin/develop | @ `2f5af63` (동기화) |
| merge gate (frontend) | **FULLY UNBLOCKED** (WT CLEAN · Open 0) |
| cross-stream merge | **FULLY UNBLOCKED** (BE @ `f0752b6` WT CLEAN · Open 0) |

### TSR 505차 vs 503차

| 항목 | 503차 | 505차 |
|------|-------|-------|
| develop HEAD | `9f80082` | `2f5af63` (+1) |
| develop WT | CLEAN | **CLEAN** |
| test npm test | 217/217 PASS | **217/217 PASS** (불변) |
| develop HEAD npm test | 미재실행 | **929/929 PASS** |
| ahead | 207 | **208** |
| Open (frontend) | 0 | **0** |
| merge gate (frontend) | UNBLOCKED | **FULLY UNBLOCKED** |
| cross-stream merge | BLOCK (QA-B63) | **FULLY UNBLOCKED** |
| merge pending | 378 | **380** (208+172) |
| backend develop | `686d686` DIRTY 1U | `f0752b6` **CLEAN** |

### TSR 505차 판정

- **PASS(v1.2+v1.3-A @ test)** — test 브랜치 회귀 217/217 GREEN.
- **★ 양 스트림 merge gate FULLY UNBLOCKED** — FE/BE develop WT CLEAN · Open 0.
- **operation 승격 BLOCK** — develop→test merge 미실행(380 commits) · post-merge live E2E 미실행.

### planner/COD 액션

1. **tester**: develop→test merge(380) 실행 (`scripts/git_merge_to_test.sh` 또는 파이프라인)
2. **tester**: post-merge `scripts/run-live-e2e.sh` (backend `localhost:8080` 필요)
3. **COD**: G40 FE Panel·live API E2E 잔여(ROADMAP 120차 P2) — merge 후 회귀
