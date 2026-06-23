<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-16T22:39:26+00:00 -->
# develop ↔ test diff 메타 (2026-06-16, 894차 — develop WT CLEAN @d8d51a7 · test @598d108 · 341 ahead)

> **875차 재검증 (16:28 UTC) — test `@598d108` CLEAN·`mvn test` **246/246 PASS**(64 suites, ~15.8s)·develop `@7ac0a46` HEAD **불변** · WT **DIRTY 6M+3U**(QA-B112 scope expanded) · Open **0(active)** · **QA-B114 Fixed @ `5ebaade`** · cross-stream FE `@5ebaade` CLEAN · 11 ahead · merge pending **342** · operation **BLOCK**(QA-B112+QA-B95).

> **872차 재검증 (15:15 UTC) — superseded by 875차**.

> **870차 재검증 (14:44 UTC) — superseded by 875차**.

> **868차 재검증 (14:08 UTC) — superseded by 870차**.

> **866차 재검증 (13:36 UTC) — superseded by 870차**.

> **865차 재검증 (12:58 UTC) — superseded by 868차**.

> **863차 재검증 (12:26 UTC) — superseded by 868차**.

> **861차 재검증 (11:20 UTC) — superseded by 868차**.

> **859차 재검증 (10:51 UTC) — superseded by 868차**.


> **894차 재검증 (22:39 UTC) — test `@598d108` CLEAN·`mvn test` **246/246 PASS**(64 suites, 14.094s)·`npm test` N/A(`package.json` 없음)·develop `@d8d51a7`(+1 vs `440ed84`)·WT **CLEAN**·origin/develop `@d8d51a7`·origin/test `@598d108`·Open **0(active backend)**·Planned **2 BLOCK QA-B116+QA-B95**·merge pending **361**(341 BE + 20 FE)·operation **BLOCK**(QA-B95).

> **892차 재검증 (22:11 UTC) — superseded by 894차**.
## 894차 delta (892→894)

- develop HEAD: **`440ed84`→`d8d51a7`**(+1 committed; `origin/develop` 동기화)
- develop WT: **CLEAN 유지**
- test HEAD: `598d108` (변경 없음)
- regression: `mvn test` **246/246 PASS** (14.094s)
- npm: **N/A** (`src/backend-test`에 `package.json` 없음)
- cross-stream: FE `@ddd4489` WT **CLEAN**(893차 carry) · **20 ahead**
- verdict: **PASS(@backend-test)** · backend merge **FULLY UNBLOCKED** · cross-stream **FULLY UNBLOCKED** · operation **BLOCK(QA-B95)**

## 875차 delta (872→875)

- develop HEAD: **`7ac0a46` 불변**
- develop WT: **DIRTY 2M → DIRTY 6M+3U** (QA-B112 scope expanded)
  - live-e2e: `LiveE2eBootstrapService.java`·`LiveE2eBootstrapServiceTest.java`
  - transport geocode (new): `TransportRoutePreviewService.java`·`TransportSuggestService.java`·`TransportRoutePreviewRequest.java`·`TransportRoutePreviewServiceTest.java` + untracked `BranchLocationResolver.java`·`KakaoGeocodeClient.java`·`KakaoGeocodeClientTest.java`
- test HEAD: `598d108` (변경 없음)
- regression: `mvn test` **246/246 PASS** (~15.8s)
- cross-stream: FE `@5ebaade` WT **CLEAN** (QA-B114 Fixed) · **11 ahead** (was 9+dirty @872)
- verdict: **PASS(@test)** · backend merge **BLOCK** · FE merge **FULLY UNBLOCKED** · cross-stream **BLOCK**(BE only)

## 872차 delta (870→872)

- develop HEAD: **`7ac0a46` 불변**
- develop WT: **CLEAN → DIRTY 2M** (`LiveE2eBootstrapService*` +70; QA-B112)
- test HEAD: `598d108` (변경 없음)
- regression: `mvn test` **246/246 PASS** (14.197s)
- cross-stream: FE `@27a3996` WT **DIRTY 5M+4U** (QA-B113) · 9 ahead
- verdict: **PASS(@test)** · merge **BLOCK** · cross-stream **BLOCK**

## 870차 delta (868→870)

- develop HEAD: **`ec142db`→`7ac0a46`**(+1 committed; `origin/develop` 동기화)
  - commit: `fix(v2/live-e2e): avoid role-mismatched seed account reuse for QA-B95`
  - files: `LiveE2eBootstrapService.java`·`LiveE2eBootstrapServiceTest.java` (2 files +136/-3)
- develop WT: **CLEAN 유지**
- test HEAD: `598d108` (변경 없음)
- `test..develop`: **330→331 ahead**
- regression: `mvn test` **246/246 PASS** (19.515s)
- cross-stream: FE develop `@b3bd0cc` / test `@7106106` · WT **DIRTY 6M+2U** (QA-B111 expanded) · **8 ahead**
- npm: **N/A** (`src/backend-test`에 `package.json` 없음)
- verdict: **PASS** · backend merge **FULLY UNBLOCKED** · cross-stream **BLOCK**(QA-B111) · QA-B95 role-collision guard on develop (merge+live E2E verify pending)

## 868차 delta (866→868)

- develop HEAD: **`f5205e3`→`ec142db`**(+1 committed; `origin/develop` 동기화)
  - commit: `feat(v2/live-e2e,L02): seed onboarding support and add live API routing E2E`
  - files: `LiveE2eBootstrapService.java`·`BranchOnboardingSupportLiveApiRoutingE2eTest.java`·`CareNursingReportsLiveApiRoutingE2eTest.java`·`StaffStatusReportLiveApiRoutingE2eTest.java`·`LiveE2eBootstrapServiceTest.java` (5 files +340)
- develop WT: **CLEAN 유지**
- test HEAD: `598d108` (변경 없음)
- `test..develop`: **329→330 ahead**
- regression: `mvn test` **246/246 PASS** (14.892s)
- cross-stream: FE develop `@b3bd0cc` / test `@7106106` · WT **CLEAN** · **8 ahead**
- npm: **N/A** (`src/backend-test`에 `package.json` 없음)
- verdict: **PASS** · backend merge **FULLY UNBLOCKED** · QA-B95 onboarding seed+routing harness on develop (merge+live E2E verify pending)

## 866차 delta (865→866)

- develop HEAD: **`2ba2761`→`f5205e3`**(+1 committed; `origin/develop` 동기화)
  - commit: `feat(v2/live-e2e): add guardian bootstrap endpoint for QA-B95`
  - files: `LiveE2eBootstrapService.java`·`LiveE2eController.java`·`LiveE2eGuardianBootstrapResponse.java`·tests·`SecurityConfig`·`application.yml` (9 files +582/-5)
- develop WT: **CLEAN 유지**
- test HEAD: `598d108` (변경 없음)
- `test..develop`: **328→329 ahead**
- regression: `mvn test` **246/246 PASS** (14.452s)
- cross-stream: FE develop `@d499130` / test `@7106106` · WT **CLEAN** · **7 ahead**
- npm: **N/A** (`src/backend-test`에 `package.json` 없음)
- verdict: **PASS** · backend merge **FULLY UNBLOCKED** · QA-B95 guardian bootstrap on develop (merge+live E2E verify pending)

## 865차 delta (863→865)

- develop HEAD: **`304bb2a`→`2ba2761`**(+1 committed; `origin/develop` 동기화)
  - commit: `test(v2/L02_M09_M10_M14): add care-scoped nursing report pilot E2E (BNK-280)`
  - files: `CareNursingReportsPilotServiceFlowE2eTest.java` (1 file +318)
- develop WT: **CLEAN 유지**
- test HEAD: `598d108` (변경 없음)
- `test..develop`: **327→328 ahead**
- regression: `mvn test` **246/246 PASS** (15.841s)
- cross-stream: FE develop `@57114b8` / test `@7106106` · WT **CLEAN** · **6 ahead**
- npm: **N/A** (`src/backend-test`에 `package.json` 없음)
- verdict: **PASS** · backend merge **FULLY UNBLOCKED** · BNK-280 pilot E2E on develop (merge pending)

## 863차 delta (861→863)

- develop HEAD: **`f6f1756`→`304bb2a`**(+1 committed; `origin/develop` 동기화)
  - commit: `fix(v2/live-e2e): restore bootstrap HTTP status and bean wiring (QA-B95)`
  - files: `GlobalExceptionHandler.java`·`LiveE2eBootstrapService.java`·`GlobalExceptionHandlerTest.java`·`LiveE2eControllerRoutingTest.java` (4 files +58/-1)
- develop WT: **CLEAN 유지**
- test HEAD: `598d108` (변경 없음)
- `test..develop`: **326→327 ahead**
- regression: `mvn test` **246/246 PASS** (15.150s)
- cross-stream: FE develop `@8ed937c` / test `@7106106` · WT **CLEAN** · **5 ahead**
- npm: **N/A** (`src/backend-test`에 `package.json` 없음)
- verdict: **PASS** · backend merge **FULLY UNBLOCKED** · QA-B95 fix on develop (merge+live E2E verify pending)

## 861차 delta (859→861)

- develop HEAD: **`002e3eb`→`f6f1756`**(+1 committed; `origin/develop` 동기화)
  - commit: `fix(v2/live-e2e): harden bootstrap error fallback paths`
  - files: `LiveE2eController.java`·`LiveE2eControllerTest.java` (2 files +32/-3)
- develop WT: **CLEAN 유지**
- test HEAD: `598d108` (변경 없음)
- `test..develop`: **325→326 ahead**
- regression: `mvn test` **246/246 PASS** (15.321s)
- cross-stream: FE develop `@58ee122` / test `@7106106` · WT **CLEAN** · **3 ahead**
- npm: **N/A** (`src/backend-test`에 `package.json` 없음)
- verdict: **PASS** · backend merge **FULLY UNBLOCKED**

## 859차 delta (857→859)

- develop HEAD: **`8a92179`→`002e3eb`**(+1 committed; `origin/develop` 동기화)
  - commit: `feat(v2/L02): add care-scoped nursing service report proxy APIs`
  - files: `CareReportController.java`·`CareReportService.java`·`CareReportServiceTest.java`·`CareReportLiveApiRoutingE2eTest.java`·`MustApiEndpointRoutingTest.java`·`RoleBasedControllerAccessTest.java` (6 files +265/-1)
- develop WT: **CLEAN 유지**
- test HEAD: `598d108` (변경 없음)
- `test..develop`: **324→325 ahead**
- regression: `mvn test` **246/246 PASS** (13.877s)
- cross-stream: FE develop `@cb457b7` / test `@7106106` · WT **CLEAN** · **2 ahead**
- npm: **N/A** (`src/backend-test`에 `package.json` 없음)
- verdict: **PASS** · backend merge **FULLY UNBLOCKED**

## 857차 delta (855→857)

- develop HEAD: **`39f5f4e`→`8a92179`**(+1 committed; `origin/develop` 동기화)
  - commit: `fix(v2/live-e2e): harden bootstrap controller failure handling`
  - files: `LiveE2eController.java`·`LiveE2eControllerTest.java` (2 files +80/-4)
- develop WT: **CLEAN 유지**
- test HEAD: `598d108` (변경 없음)
- `test..develop`: **323→324 ahead**
- regression: `mvn test` **246/246 PASS** (14.784s)
- npm: **N/A** (`src/backend-test`에 `package.json` 없음)
- verdict: **PASS** · backend merge **FULLY UNBLOCKED**

## 855차 delta (851→855)

- develop HEAD: **`e54a699`→`39f5f4e`**(+2 committed; `origin/develop` 동기화)
- develop WT: **CLEAN 유지**
- test HEAD: `598d108` (변경 없음)
- `test..develop`: **321→323 ahead**
- regression: `mvn test` **246/246 PASS** (14.034s)
- npm: **N/A** (`src/backend-test`에 `package.json` 없음)
- verdict: **PASS** · backend merge **FULLY UNBLOCKED**

## 851차 delta (850→851)

- develop HEAD: **`e54a699` 유지**(신규 커밋 없음)
- develop WT: **CLEAN 유지**
- test HEAD: `598d108` (변경 없음)
- `test..develop`: **321 ahead(불변)**
- regression: `mvn test` **246/246 PASS** (14.788s)
- npm: **N/A** (`src/backend-test`에 `package.json` 없음)
- verdict: **PASS** · backend merge **FULLY UNBLOCKED**

## 850차 delta (848→850) — superseded by 851차

- develop HEAD: **`c5f1325`→`e54a699`**(+1 committed; `origin/develop` 동기화)
  - commit: `fix(v2/visits): return unpaired status for missing paired schedule`
  - files: `VisitService.java`·`VisitServiceTest.java` (2 files +12/-1)
- develop WT: **DIRTY 2M → CLEAN** (**QA-B110 Fixed**)
- test HEAD: `598d108` (변경 없음)
- `test..develop`: **320→321 ahead**
- regression: `mvn test` **246/246 PASS** (13.608s)
- npm: **N/A** (`src/backend-test`에 `package.json` 없음)
- verdict: **PASS** · backend merge **FULLY UNBLOCKED**

## 848차 delta (846→848)

- develop HEAD: **`c5f1325` 유지**(신규 커밋 없음)
- develop WT: **CLEAN → DIRTY 2M**
  - modified: `src/main/java/com/ogada/backend/visits/domain/VisitService.java`
  - modified: `src/test/java/com/ogada/backend/visits/domain/VisitServiceTest.java`
- test HEAD: `598d108` (변경 없음)
- `test..develop`: **320 ahead(불변)**
- regression: `mvn test` **246/246 PASS** (13.955s)
- npm: **N/A** (`src/backend-test`에 `package.json` 없음)
- verdict: **BLOCK**(QA-B110 backend dirty recurrence)

## 844차 delta (842→844)

- develop HEAD: **`30f03e8`→`aa6816a`**(+1 committed; `origin/develop` 동기화)
  - commit: `fix(v2/security): harden live-e2e bootstrap exposure in prod`
  - files: `ProductionSecretValidator.java`·`LiveE2eBootstrapResponse.java`·`LiveE2eBootstrapService.java`·`ProductionSecretValidatorTest.java`·`LiveE2eBootstrapServiceTest.java`·`LiveE2eControllerTest.java` (6 files +78/-10)
- develop WT: **CLEAN 유지**
- test HEAD: `598d108` (변경 없음)
- `test..develop`: **318→319 ahead**
- regression: `mvn test` **246/246 PASS** (13.778s)
- npm: **N/A** (`src/backend-test`에 `package.json` 없음)
- cross-stream: FE develop `@43d308a` / test `@09e4ec1` CLEAN · **BLOCK(QA-B109)**

## 842차 delta (840→842) — superseded by 844차

> **842차 재검증 (06:22 UTC) — test `@598d108` CLEAN·`mvn test` **246/246 PASS**(64 suites, 14.193s)·develop `@30f03e8`(+1) · WT **CLEAN** · `test..develop` **318 ahead** · cross-stream BLOCK(QA-B108).

- develop HEAD: **`2495753`→`30f03e8`**(+1 committed; `origin/develop` 동기화)
  - commit: `test(v2/G26): extend statistics pilot flow for transport fee aggregates`
  - files: `G26StatisticsReportsPilotServiceFlowE2eTest.java` (1 file +125/-4)
- develop WT: **CLEAN 유지**
- test HEAD: `598d108` (변경 없음)
- `test..develop`: **317→318 ahead**
- regression: `mvn test` **246/246 PASS** (14.193s)
- npm: **N/A** (`src/backend-test`에 `package.json` 없음)
- cross-stream: FE develop `@64f6753` / test `@09e4ec1` CLEAN · **BLOCK(QA-B108)**

## 840차 delta (838→840) — superseded by 842차

- develop HEAD: **`3672bbe`→`2495753`**(+1 committed; `origin/develop` 동기화)
  - commit: `fix(v2/L02): align care report RBAC with API spec`
  - files: `CareReportController.java`·`RoleBasedControllerAccessTest.java` (2 files +47/-18)
- develop WT: **CLEAN 유지**
- test HEAD: `598d108` (변경 없음)
- `test..develop`: **316→317 ahead**
- regression: `mvn test` **246/246 PASS** (13.900s)
- npm: **N/A** (`src/backend-test`에 `package.json` 없음)
- cross-stream: FE `@09e4ec1` CLEAN · merge **FULLY UNBLOCKED**

## 838차 delta (836→838) — superseded by 842차

- develop HEAD: **`3481eb8`→`3672bbe`**(+1 committed; `origin/develop` 동기화)
  - commit: `feat(v2/G26): add transport service fee monthly statistics API`
  - files: `BillingStatisticsReportController.java`·`BillingStatisticsService.java`·`BillingStatisticsServiceTest.java`·`TransportServiceFeeSettlementRepository.java` (4 files +727/-39)
- develop WT: **CLEAN 유지**
- test HEAD: `598d108` (변경 없음)
- `test..develop`: **315→316 ahead**
- regression: `mvn test` **246/246 PASS** (14.139s)
- npm: **N/A** (`src/backend-test`에 `package.json` 없음)
- cross-stream: FE `@d8f1fdf` CLEAN · merge **FULLY UNBLOCKED**

## 836차 delta (834→836) — superseded by 838차

- develop HEAD: **`92ae60b`→`3481eb8`**(+1 committed; `origin/develop` 동기화)
  - commit: `test(v2/G26): add dual-function statistics pilot service flow E2E`
  - files: `G26StatisticsReportsPilotServiceFlowE2eTest.java` (1 file +307)
- develop WT: **CLEAN 유지**
- test HEAD: `598d108` (변경 없음)
- `test..develop`: **314→315 ahead**
- regression: `mvn test` **246/246 PASS** (~15.5s)
- npm: **N/A** (`src/backend-test`에 `package.json` 없음)
- cross-stream: FE `@e10113f` CLEAN · merge **FULLY UNBLOCKED**

## 834차 delta (832→834) — superseded by 836차

- develop HEAD: **`472cb1d`→`92ae60b`**(+1 committed; `origin/develop` 동기화)
  - commit: `test(v2/G26): add dual-function statistics live API routing harness`
  - files: `G26StatisticsReportsLiveApiRoutingE2eTest.java`·`BillingServiceTest.java` (2 files +219)
- develop WT: **CLEAN 유지**
- test HEAD: `598d108` (변경 없음)
- `test..develop`: **313→314 ahead**
- regression: `mvn test` **246/246 PASS** (~14.9s)
- npm: **N/A** (`src/backend-test`에 `package.json` 없음)
- cross-stream: FE `@9006a53` CLEAN · QA-B107 Fixed · merge **FULLY UNBLOCKED**

## 832차 delta (830→832) — superseded by 834차

## 830차 delta (828→830) — superseded by 834차

## 전체 diff 스냅샷 (test..develop)

- commit count: **318**
- short stat: **915 files changed, 100684 insertions(+), 1145 deletions(-)**
- 최신 커밋(top 10):
  - `30f03e8` test(v2/G26): extend statistics pilot flow for transport fee aggregates
  - `2495753` fix(v2/L02): align care report RBAC with API spec
  - `3672bbe` feat(v2/G26): add transport service fee monthly statistics API
  - `3481eb8` test(v2/G26): add dual-function statistics pilot service flow E2E
  - `92ae60b` test(v2/G26): add dual-function statistics live API routing harness
  - `472cb1d` fix(v2/live-e2e): keep bootstrap user tenant-scoped
  - `6d10e0d` feat(v2/G26): add copay monthly statistics report API
  - `1840640` test(v2/G26): add medical deduction report live API pilot E2E
  - `903f462` feat(v2/G26): add branch medical expense deduction statistics report API
  - `b38c6f7` test(v2/G21): add billing claim reflection pilot E2E coverage
  - `6da49aa` feat(v2/G21): expose billing claim reflection status on visit schedules
  - `f33252a` feat(v2/L02_M16): add meal preference survey API (G-MEAL-PREFERENCE)
