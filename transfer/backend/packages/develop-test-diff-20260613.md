<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-13T23:48:36+00:00 -->
# develop ↔ test diff 메타 (2026-06-13, 608차 — develop WT CLEAN @299d21f · test @598d108 · 214 ahead)

> **608차 재검증 (23:48 UTC) — test `@598d108` CLEAN·origin/test 동기화·**246/246 PASS**(64 suites, 13.694s)·develop `@299d21f`(+1 vs `0f11158`: `fix(v1.2.1/G41b): use earliest new-hire orientation date in compliance (BNK-187)`) · WT **CLEAN** · develop HEAD `mvn test` **미재실행**(tester read-only 정책) · develop **214 ahead** · **QA-B76 Fixed @ `299d21f`** · ★ backend merge **FULLY UNBLOCKED** · ⚠ cross-stream FE **BLOCK**(@`a4ab0c2` CLEAN, Open 1 BLOCK QA-B77, 262 ahead, 607차) · merge pending **476**(214+262).

> **606차 재검증 (23:27 UTC) — superseded by 608차 — develop `@299d21f` WT **CLEAN** 확인·QA-B76 Fixed** · merge pending 476.

## 요약

| 항목 | 값 |
|------|-----|
| test HEAD | `598d108` — feat(v2): copay payment recording, overdue list, and guardian billing API |
| develop HEAD | `299d21f` — fix(v1.2.1/G41b): use earliest new-hire orientation date in compliance (BNK-187) |
| develop ahead of test | **214** commits |
| test ahead of develop | 0 |
| develop WT | **CLEAN** |
| test WT | **CLEAN** |
| test `mvn test` | **246/246 PASS** (64 suites, 13.694s) |
| develop HEAD `mvn test` | **미재실행** (tester read-only 정책) |
| QA Open (backend) | **0** (QA-B76 Fixed @ `299d21f`) |
| merge gate (backend) | **FULLY UNBLOCKED** |
| merge executed | **No** (214 commits pending) |
| cross-stream (frontend, 607차) | `@a4ab0c2` WT **CLEAN** · 262 ahead · Open **1 BLOCK QA-B77** |
| merge pending (total) | **476** (214 BE + 262 FE) · ⚠ **cross-stream merge BLOCK** |

## 608차 delta (606→608)

- develop HEAD **`0f11158`→`299d21f`** (+1 commit: BNK-187 earliest new-hire orientation date compliance fix)
- develop WT **DIRTY 2M→CLEAN**
- test `@598d108` `mvn test` **246/246 PASS** 재실행(13.694s)
- **QA-B76 Fixed @ `299d21f`** · backend merge gate **BLOCK→FULLY UNBLOCKED**
- cross-stream: FE `@a4ab0c2` HEAD test FAIL(**QA-B77**)로 양 스트림 merge **BLOCK 유지**
- merge pending **474→476** (BE 213→214, FE 261→262)

## 606차 delta (604→606)

- develop HEAD **불변** `@0f11158` (604차 대비 커밋 없음)
- develop WT **CLEAN→DIRTY 2M** — uncommitted G41b follow-up:
  - `StaffTrainingLogService.java` — `orientationDatesByUser` earliest `trainedAt` merge·null guard
  - `StaffTrainingLogServiceTest.java` — annual compliance orientation date merge regression (+35 lines, +1 @Test)
- test `@598d108` **246/246 PASS** 불변
- **신규 Open 1 BLOCK QA-20260614-B76** — backend merge gate **BLOCK**
- cross-stream: FE `@38d24b6` WT **CLEAN**(605차) → 양 스트림 merge **BLOCK**(BE WT clean 선행)
- merge pending **473→474** (FE 260→261 ahead, +1 `@38d24b6` G41b FE wire BNK-185)

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-13T23:11:31+00:00 -->
# develop ↔ test diff 메타 (2026-06-13, 604차 — develop WT CLEAN @0f11158 · test @598d108 · 213 ahead)

> **604차 재검증 (23:11 UTC) — test `@598d108` CLEAN·origin/test 동기화·**246/246 PASS**(64 suites, ~14.4s)·develop `@0f11158`(+1 vs `613b6af`: G41b annual compliance on training log API BNK-185) · WT **CLEAN** · develop HEAD `mvn test` **미재실행**(tester read-only 정책) · develop **213 ahead** · **Open 0(backend)** · ★ backend merge **FULLY UNBLOCKED** · ★ cross-stream FE **FULLY UNBLOCKED**(@`e43295b` CLEAN, Open 0, 260 ahead, 603차) · merge pending **473**(213+260).

> **602차 재검증 (22:56 UTC) — superseded by 604차 — develop `@613b6af` · 212 ahead · merge pending 471**.

> **600차 재검증 (22:41 UTC) — superseded by 604차 — develop `@613b6af` · 212 ahead · merge pending 470**.

> **598차 재검증 (22:03 UTC) — superseded by 600차 — develop `@6191b91` · 211 ahead · merge pending 467**.

> **595차 재검증 (21:39 UTC) — superseded by 598차 — develop `@997831c` · 210 ahead · merge pending 465**.

> **591차 재검증 (20:40 UTC) — superseded by 595차 — develop `@9a8bd2a` · 208 ahead · merge pending 461**.

> **589차 재검증 (20:18 UTC) — superseded by 591차 — develop `@8615e3c` · 207 ahead · merge pending 459**.

> **587차 재검증 (19:54 UTC) — test `@598d108` CLEAN·origin/test 동기화·**246/246 PASS**(64 suites, 14.543s)·develop `@726b3de`(+1 vs `229f84c`: G34-QUAL team-lead eligibility gate) · WT **CLEAN** · develop HEAD `mvn test` **미재실행**(tester read-only 정책) · develop **206 ahead** · **Open 0(backend)** · ★ backend merge **FULLY UNBLOCKED** · ⚠ cross-stream FE **BLOCK**(@`76b5ff0` CLEAN, Open 0 + Planned 1 BLOCK QA-B74, 251 ahead) · merge pending **457**(206+251).

## 요약

| 항목 | 값 |
|------|-----|
| test HEAD | `598d108` — feat(v2): copay payment recording, overdue list, and guardian billing API |
| develop HEAD | `0f11158` — feat(v1.2.1/G41b): expose G41b annual compliance on training log API (BNK-185) |
| develop ahead of test | **213** commits |
| test ahead of develop | 0 |
| develop WT | **CLEAN** |
| test WT | **CLEAN** |
| test `mvn test` | **246/246 PASS** (64 suites, ~14.4s) |
| develop HEAD `mvn test` | **미재실행** (tester read-only 정책) |
| QA Open (backend) | **0** |
| merge gate (backend) | **FULLY UNBLOCKED** |
| merge executed | **No** (213 commits pending) |
| cross-stream (frontend, 603차) | `@e43295b` WT **CLEAN** · 260 ahead · Open **0** |
| merge pending (total) | **473** (213 BE + 260 FE) · ★ **cross-stream merge FULLY UNBLOCKED** |

## 604차 delta (602→604)

- develop HEAD **`613b6af`→`0f11158`** (+1 commit: G41b annual compliance — `StaffTrainingLogComplianceResponse`·`StaffTrainingLogCompliance`·`StaffTrainingLogService` deepen·pilot E2E·routing/RBAC tests, 10 files +179, +45 @Test)
- develop WT **CLEAN 유지**
- test `mvn test` **246/246 PASS 재실행** (~14.4s, 604차 독립 확인)
- develop ahead **212→213**
- **Open 0(backend) 유지**
- cross-stream frontend **603차 `@e43295b`(+1 G41 FE wire)·260 ahead·Open 0** · merge pending **472→473**
- **신규 Open 0** · **BLOCK 없음**

## 602차 delta (600→602)

- develop HEAD **`613b6af` 불변** · WT **CLEAN 유지** · ahead **212 유지**
- test `mvn test` **246/246 PASS 재실행** (~14.8s, 602차 독립 확인)
- **Open 0(backend) 유지**
- cross-stream frontend **601차 `@e69bf00`(+2 G41b FE wire)·259 ahead·Open 0** · merge pending **470→471**
- **신규 Open 0** · **BLOCK 없음**

## 600차 delta (598→600)

- develop HEAD `6191b91`→`613b6af` (+1 commit: G41b staff training log integrity — V105/V106 migrations·StaffTrainingLogType 3종·StaffTrainingLogService deepen·+35 @Test, 5 files +161)
- develop WT **CLEAN 유지**
- test `mvn test` **246/246 PASS 유지** (~14.9s, 600차 재실행 확인)
- develop ahead **211→212**
- **Open 0(backend) 유지**
- cross-stream FE @ `f5658de` WT **CLEAN** · 258 ahead · Open **0** (599차 +1 G41 FE wire)
- merge pending **468→470**

## 598차 delta (595→598)

- develop HEAD `997831c`→`6191b91` (+1 commit: US-S02 staff training log API — V104 migration·StaffTrainingLogService·controller/DTO 8종·pilot E2E·routing/RBAC tests, 18 files +1602)
- develop WT **CLEAN 유지**
- test `mvn test` **246/246 PASS 유지** (14.329s, 598차 재실행 확인)
- develop ahead **210→211**
- **Open 0(backend) 유지**
- cross-stream FE @ `400c835` WT **CLEAN** · 256 ahead · Open **0** (597차)
- merge pending **465→467**

## 595차 delta (593→595)

- develop HEAD `b1dfd34`→`997831c` (+1 commit: G30/G34-QUAL monitoring checklist·team-lead pilot E2E — `MonitoringPilotServiceFlowE2eTest`·`TeamLeadQualificationPilotServiceFlowE2eTest`·`MustApiEndpointRoutingTest`·`RoleBasedControllerAccessTest`·`PilotChecklistJwtE2eTest`, 5 files +257)
- develop WT **CLEAN 유지**
- test `mvn test` **246/246 PASS 유지** (26.931s, 595차 재실행 확인)
- develop ahead **209→210**
- **Open 0(backend) 유지**
- cross-stream FE @ `574bd08` WT **CLEAN** · 255 ahead · Open **0**
- merge pending **464→465**

## 591차 delta (589→591)

- develop HEAD `8615e3c`→`9a8bd2a` (+1 commit: G34-QUAL team lead eligibility compliance API — `TeamLeadQualificationController`·`TeamLeadQualificationService`·DTO 2종·`TeamLeadQualificationServiceTest`, 5 files +330)
- develop WT **CLEAN 유지**
- test `mvn test` **246/246 PASS 유지** (14.745s, 591차 재실행 확인)
- develop ahead **207→208**
- **Open 0(backend) 유지**
- cross-stream FE @ `dbf0299` WT **CLEAN** · 253 ahead · Open **0**
- merge pending **459→461**

## 589차 delta (587→589)

- develop HEAD `726b3de`→`8615e3c` (+1 commit: latest backend develop HEAD between cycles)
- develop ahead **206→207**
- merge pending **457→459**

## 585차 delta (582→585)

- develop HEAD `fffd355`→`229f84c` (+1 commit: J03 quiet-hours readiness KST clock zone)
- develop WT **CLEAN 유지**
- test `mvn test` **246/246 PASS 유지** (~24s, 585차 재실행 확인)
- develop ahead **204→205**
- **Open 0(backend) 유지**
- cross-stream FE @ `d695923` WT **CLEAN** · 249 ahead · Open **0**
- merge pending **452→454**

## 582차 delta (580→582)

- develop HEAD `c16f4fe`→`fffd355` (+1 commit: J03 notification channel readiness email+quiet-hours gates)
- develop WT **CLEAN 유지**
- test `mvn test` **246/246 PASS 유지** (~15s, 582차 재실행 확인)
- develop ahead **203→204**
- **Open 0(backend) 유지**
- cross-stream FE @ `6b1258c` WT **CLEAN** · 248 ahead · Open **0**
- merge pending **450→452**

## 580차 delta (578→580)

- develop HEAD `d4acab7`→`c16f4fe` (+1 commit: QA-B73 G21 assigned-user check-in guard)
- develop WT **DIRTY 2M→CLEAN**
- test `mvn test` **246/246 PASS 유지** (~15s, 580차 재실행 확인)
- develop ahead **202→203**
- **QA-B73 Fixed @ `c16f4fe`** · **Open 0(backend)**
- backend merge gate **BLOCK→FULLY UNBLOCKED**
- cross-stream FE @ `ff173af` WT **CLEAN** · 247 ahead · Open **0**
- merge pending **448→450**

## 578차 delta (576→578)

- develop HEAD **불변** @ `d4acab7`
- develop WT **CLEAN→DIRTY 2M** (`VisitService.java`·`VisitServiceTest.java` — G21 assigned caregiver check-in guard WIP, 2 files +25/-1, +1 @Test)
- test `mvn test` **246/246 PASS 유지** (~26s, 578차 재실행 확인)
- develop HEAD `mvn test` **미재실행**(tester read-only 정책)
- **신규 Open 1 BLOCK QA-20260613-B73(backend)** — 576차 CLEAN 기록 오류 수정
- backend merge gate **FULLY UNBLOCKED→BLOCK**(WT dirty)
- cross-stream FE @ `5bba7a2` WT **CLEAN** · 246 ahead · Open **0** · merge pending **447→448**

## 576차 delta (574→576)

- develop HEAD `c4dbe43`→`d4acab7` (+1 commit: J03 notification channel readiness status API)
- develop WT **CLEAN 유지**
- test `mvn test` **246/246 PASS 유지** (~15.9s)
- develop HEAD `mvn test` **미재실행**(tester read-only 정책)
- develop ahead **201→202**
- cross-stream FE **`6012044`→`488f547`** (+1, 244→245 ahead)
- merge pending **445→447**

## 572차 delta (570→572)

- develop HEAD `bc927f7`→`39ee679` (+1 commit: G16 RU-3/RU-4 이동서비스비 seed 정정)
- develop WT **CLEAN 유지**
- test `mvn test` **246/246 PASS 유지** (14.257s)
- develop HEAD `mvn test` **미재실행**(tester read-only 정책)
- develop ahead **199→200**
- cross-stream FE `14124d6`→`892450a` (+1, 241→242 ahead) · Open **1 BLOCK QA-B72 유지** · HEAD test **1066/1067 FAIL**
- merge pending **440→442**
- **Open 0 유지(backend)** · **신규 backend BLOCK 없음** · **cross-stream BLOCK 유지**(FE QA-B72)

## 570차 delta (568→570)

- develop HEAD `bcb1d9f`→`bc927f7` (+1 commit: US-R02 staff status report CSV export endpoint)
- develop WT **CLEAN 유지**
- test `mvn test` **246/246 PASS 유지** (~15s)
- develop HEAD `mvn test` **미재실행**(tester read-only 정책)
- develop ahead **198→199**
- cross-stream FE `47a4928`→`14124d6` (+1, 240→241 ahead) · Open **0→1 BLOCK QA-B72** · HEAD test **FAIL**
- merge pending **438→440**
- **Open 0 유지(backend)** · **신규 backend BLOCK 없음** · **cross-stream BLOCK**(FE QA-B72)

## 568차 delta (566→568)

- develop HEAD `9fef436`→`bcb1d9f` (+1 commit: G42 pending follow-up checklist API·anonymous box pilot E2E BNK-161 P2)
- develop WT **CLEAN 유지**
- test `mvn test` **246/246 PASS 유지** (~15s)
- develop HEAD `mvn test` **미재실행**(tester read-only 정책)
- develop ahead **197→198**
- cross-stream FE `ccc4d75`→`47a4928` (+1, 239→240 ahead)
- merge pending **436→438**
- **Open 0 유지** · **신규 BLOCK 없음**

## 566차 delta (564→566)

- develop HEAD `2ebca70`→`9fef436` (+1 commit: G42 grievance compliance dashboard snapshot counts)
- develop WT **CLEAN 유지**
- test `mvn test` **246/246 PASS 유지** (~15s)
- develop HEAD `mvn test` **미재실행**(tester read-only 정책)
- develop ahead **196→197**
- cross-stream FE `772e96f`→`ccc4d75` (+1, 238→239 ahead)
- merge pending **434→436**
- **Open 0 유지** · **신규 BLOCK 없음**

## 564차 delta (562→564)

- develop HEAD `5692662`→`f4c8558` (+1 commit: G30 monitoring integrity migration V101)
- develop WT **CLEAN 유지**
- test `mvn test` **246/246 PASS 유지**
- develop HEAD `mvn test` **931→935 PASS** (+4 @Test, 170 suites)
- develop ahead **194→195**
- **Open 0 유지**(backend)
- cross-stream merge pending **429→432**

## 560차 delta (558→560)

- develop HEAD `b8e92bf`→`5692662` (+1 commit)
- develop WT **CLEAN 유지**
- test `mvn test` **246/246 PASS 유지** (13.632s)
- develop ahead **193→194**
- **Open 0 유지**(backend)
- cross-stream merge pending **427→429**

## 558차 delta (556→558)

- develop HEAD `5501745`→`b8e92bf` (+1 commit: G30 six-month monitoring self-diagnosis compliance endpoint)
- develop WT **CLEAN 유지**
- develop HEAD `mvn test` **921→931 PASS** (+10 @Test)
- develop ahead **192→193**
- **Open 0 유지**(backend)
- cross-stream merge pending **425→427**

## 556차 delta (554→556)

- develop HEAD `6a72b70`→`5501745` (+1 commit: monitoring phone consult route coverage)
- develop WT **CLEAN 유지**
- develop HEAD `mvn test` **920→921 PASS** (+1 @Test, 168 suites)
- develop ahead **191→192**
- **Open 0 유지**(backend)
- cross-stream merge pending **423→425**

## 554차 delta (552→554)

- develop HEAD `aaa16f8`→`6a72b70` (+1 commit: v2/G30 monitoring self-diagnosis·phone consultation API, BNK-169)
- develop WT **CLEAN 유지**
- develop HEAD `mvn test` **909→920 PASS** (+11 @Test)
- develop ahead **190→191**
- **Open 0 유지**(backend)
- backend merge gate **FULLY UNBLOCKED 유지**
- cross-stream FE **BLOCK→FULLY UNBLOCKED** (`a5c2736` DIRTY 2M/Open1 → `b47e85c` CLEAN/Open0)
- merge pending **421→423**

## 552차 delta (550→552)

- develop HEAD `8bb6583`→`aaa16f8` (+1 commit: US-R02/8-12 staff status report API)
- develop WT **CLEAN 유지**
- develop HEAD `mvn test` **902→909 PASS** (+7 @Test, 161→165 suites)
- develop ahead **189→190**
- **Open 0 유지**(backend)
- backend merge gate **FULLY UNBLOCKED 유지**
- cross-stream FE **QA-B71 BLOCK 유지** (WT DIRTY 2M)
- merge pending **420→421**

## 550차 delta (548→550)

- develop HEAD `edd2771`→`8bb6583` (+1 commit: G9-COG NHIS import gate on cognitive support fee grid BNK-166)
- develop WT **CLEAN 유지**
- develop HEAD `mvn test` **897→902 PASS** (+5 @Test, 160→161 suites)
- develop ahead **188→189**
- **Open 0 유지**(backend)
- backend merge gate **FULLY UNBLOCKED 유지**
- cross-stream FE `@e77b7e4`→`a5c2736` (+1 UXD-94, 230→231 ahead)
- merge pending **417→420**

## 548차 delta (546→548)

- develop HEAD `2efc557`→`edd2771` (+1 commit: G9-COG cognitive support grade + bulk NHIS seed apply BNK-166)
- develop WT **CLEAN 유지**
- develop HEAD `mvn test` **894→897 PASS** (+3 @Test)
- develop ahead **187→188**
- **Open 0 유지**(backend)
- backend merge gate **FULLY UNBLOCKED 유지**
- cross-stream **양 스트림 FULLY UNBLOCKED** (FE 547차 @ `6ef671b`)
- merge pending **415→417**

## 546차 delta (544→546)

- develop HEAD `21eb0af`→`2efc557` (+1 commit: G9-COG cognitive support grade daily rate catalog BNK-166)
- develop WT **CLEAN 유지**
- develop HEAD `mvn test` **886→894 PASS** (+8 @Test, +1 suite)
- develop ahead **186→187**
- **Open 0 유지**(backend)
- backend merge gate **FULLY UNBLOCKED 유지**
- cross-stream **양 스트림 FULLY UNBLOCKED** (FE 545차 @ `58256c6`)
- merge pending **413→415**

## 544차 delta (542→544)

- develop HEAD `6f6094d`→`21eb0af` (+1 commit: QA-B70 Fixed — G-7x-1 prior-deposit `YearMonth` guard)
- develop WT **DIRTY 2M→CLEAN**
- develop HEAD `mvn test` **885→886 PASS** (+1 @Test)
- develop ahead **185→186**
- **Open 1 BLOCK QA-B70→0(backend)**
- backend merge gate **BLOCK→FULLY UNBLOCKED**
- cross-stream **양 스트림 FULLY UNBLOCKED** (FE QA-B69 Fixed @ `7668459`)
- merge pending **411→413**
