<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-09T22:48:00+00:00 -->
# develop ↔ test diff 메타 (2026-06-09, 157차 — origin 동기화 @598d108 · develop @6eba2ef WT CLEAN)

> **157차 재검증 (22:48 UTC) — test `@598d108` CLEAN·origin/test 동기화·246/246 PASS·develop `6eba2ef`(+1) WT CLEAN·342/342 PASS(+6)·29 ahead·origin/develop 동기화·PASS(v1)·Open 0(backend)·★ v1.2.1 merge FULLY UNBLOCKED**:
> test·origin/test `598d108` 동기화 유지. test `mvn test` **246/246 PASS**(64 suites)·Boot **3.3.1**·Flyway **V50**.
> develop HEAD **`6eba2ef`**(`feat(v2/G2): enrich email channel with guardian resolver and billing content` — `GuardianEmailResolver`·`EmailNotificationContent`·`J03EmailServiceFlowE2eTest`·`StubEmailProvider` enrich·`EmailNotificationContentTest`·`StubEmailProviderTest`, 7 files +537/-9, 336→342 +6 @Test). develop `mvn test` **342/342 PASS**(76 suites). develop **29커밋 ahead** — v1.2.1 merge gate **FULLY UNBLOCKED**. G2 email **Stub** — 실 SMTP P1 잔여.

> **155차 재검증 (22:27 UTC) — test `@598d108` CLEAN·origin/test 동기화·246/246 PASS·develop `fbedcc3`(+1) WT CLEAN·336/336 PASS(+1)·28 ahead·origin/develop 동기화·PASS(v1)·Open 0(backend)·★ v1.2.1 merge FULLY UNBLOCKED**:
> test·origin/test `598d108` 동기화 유지. test `mvn test` **246/246 PASS**(64 suites)·JAR **76,675,999 B**·Boot **3.3.1**·Flyway **V50**.
> develop HEAD **`fbedcc3`**(`feat(v2/US-J03): add email notification channel dispatch` — `NotificationService`·`StubEmailProvider`·`NotificationConfig`·`GuardianPreferenceSnapshot`·`NotificationServiceTest` +47, 5 files +100/-1, 335→336 +1 @Test). develop `mvn test` **336/336 PASS**(73 suites). develop **28커밋 ahead** — v1.2.1 merge gate **FULLY UNBLOCKED**. G2 email **Stub** — 실 SMTP P1 잔여.

> **153차 재검증 (22:10 UTC) — test `@598d108` CLEAN·origin/test 동기화·246/246 PASS·develop `a401537`(+1) WT CLEAN·335/335 PASS(불변)·27 ahead·origin/develop 동기화·PASS(v1)·Open 0(backend)·★ v1.2.1 merge FULLY UNBLOCKED**:
> test·origin/test `598d108` 동기화 유지. test `mvn test` **246/246 PASS**(64 suites)·JAR **76,675,999 B**·Boot **3.3.1**·Flyway **V50**.
> develop HEAD **`a401537`**(`fix(v2/US-L02): keep overdue client names after discharge` — `BillingService`·`BillingServiceTest` 2 files +17/-14, 335 @Test 불변). develop `mvn test` **335/335 PASS**(73 suites). develop **27커밋 ahead** — v1.2.1 merge gate **FULLY UNBLOCKED**.

> **151차 재검증 (21:51 UTC) — test `@598d108` CLEAN·origin/test 동기화·246/246 PASS·develop `f755428`(+1) WT CLEAN·335/335 PASS(+1)·26 ahead·origin/develop 동기화·PASS(v1)·Open 0(backend)·★ v1.2.1 merge FULLY UNBLOCKED**:
> test·origin/test `598d108` 동기화 유지. test `mvn test` **246/246 PASS**(64 suites)·JAR **76,675,999 B**·Boot **3.3.1**·Flyway **V50**.
> develop HEAD **`f755428`**(`feat(v2/US-M02): add NHIS and overdue widget counts to branch dashboard API` — `DashboardService`·`BranchDashboardResponse`·`BillingClaimItemRepository`·`NhisImportRowRepository`·`DashboardServiceTest` +85, 5 files +152/-10, 334→335 +1 @Test). develop `mvn test` **335/335 PASS**(73 suites). develop **26커밋 ahead** — v1.2.1 merge gate **FULLY UNBLOCKED**.

> **149차 재검증 (21:34 UTC) — test `@598d108` CLEAN·origin/test 동기화·246/246 PASS·develop `c67ff1e`(+1) WT CLEAN·334/334 PASS(불변)·25 ahead·origin/develop 동기화·PASS(v1)·Open 0(backend)·★ v1.2.1 merge FULLY UNBLOCKED**:
> test·origin/test `598d108` 동기화 유지. test `mvn test` **246/246 PASS**(64 suites)·JAR **76,675,999 B**·Boot **3.3.1**·Flyway **V50**.
> develop HEAD **`c67ff1e`**(`perf(v2/US-L02): add partial index for billing reminder claim lookup` — `V58__notifications_billing_reminder_claim_lookup_index.sql` +18 lines, migration-only, 334 @Test 불변). develop `mvn test` **334/334 PASS**(73 suites). develop **25커밋 ahead** — v1.2.1 merge gate **FULLY UNBLOCKED**.

> **147차 재검증 (21:07 UTC) — test `@598d108` CLEAN·origin/test 동기화·246/246 PASS·develop `0ebe945`(+1) WT CLEAN·334/334 PASS·24 ahead·origin/develop 동기화·PASS(v1)·Open 0(backend)·★ v1.2.1 merge FULLY UNBLOCKED**:
> test·origin/test `598d108` 동기화 유지. test `mvn test` **246/246 PASS**(64 suites)·JAR **76,675,999 B**·Boot **3.3.1**·Flyway **V50**.
> develop HEAD **`0ebe945`**(`test(v2/US-V01): add visit pilot service flow coverage` — `VisitPilotServiceFlowE2eTest.java` +210 lines, 1 file +210, 333→334 +1 @Test). develop `mvn test` **334/334 PASS**(73 suites). develop **24커밋 ahead** — v1.2.1 merge gate **FULLY UNBLOCKED** · QA-20260609-B10 Fixed.

> **145차 재검증 (20:45 UTC) — test `@598d108` CLEAN·origin/test 동기화·246/246 PASS·develop `09932ef` HEAD 불변·WT DIRTY 1U·333/333 HEAD·WT 334/334·23 ahead·PASS(v1)·Open 1 BLOCK·⚠ v1.2.1 merge BLOCK**:
> test·origin/test `598d108` 동기화 유지. test `mvn test` **246/246 PASS**(64 suites)·JAR **76,675,999 B**·Boot **3.3.1**·Flyway **V50**.
> develop HEAD **`09932ef`** 불변(143차 대비). WT **DIRTY 1U** — untracked `VisitPilotServiceFlowE2eTest.java`(210 lines·1 @Test·v2/G21 US-V01). develop HEAD `mvn test` **333/333 PASS**·WT **334/334 PASS**. develop **23커밋 ahead** — v1.2.1 merge gate **BLOCK**(WT clean 선행·QA-20260609-B10).

> **143차 재검증 (20:23 UTC) — test `@598d108` CLEAN·origin/test 동기화·246/246 PASS·develop `09932ef` CLEAN·333/333 PASS·23 ahead·origin/develop 동기화·PASS(v1)·Open 0(backend)·★ v1.2.1 merge UNBLOCKED**:
> test·origin/test `598d108` 동기화 유지. test `mvn test` **246/246 PASS**(64 suites)·JAR **76,675,999 B**·Boot **3.3.1**·Flyway **V50**.
> develop HEAD **`09932ef`**(`test(v2/US-L01,L02): cover overdue notify-payment lifecycle` — `BillingServiceTest` +127 lines, test-only, 332→333 +1 @Test). develop `mvn test` **333/333 PASS**(72 suites). develop **23커밋 ahead** — v1.2.1 merge gate **FULLY UNBLOCKED**.

> **141차 재검증 (19:58 UTC) — test `@598d108` CLEAN·origin/test 동기화·246/246 PASS·develop `7fbd219` CLEAN·332/332 PASS·22 ahead·origin/develop 동기화·PASS(v1)·Open 0(backend)·★ v1.2.1 merge UNBLOCKED**:
> test·origin/test `598d108` 동기화 유지. test `mvn test` **246/246 PASS**(64 suites)·JAR **76,675,999 B**·Boot **3.3.1**·Flyway **V50**.
> develop HEAD **`7fbd219`**(`fix(v2/G21): harden NHIS visit date/time parsing formats` — `NhisVisitScheduleExcelParser` +59·`NhisVisitScheduleExcelParserTest` +33, 2 files +87/-5, 330→332 +2 @Test). develop `mvn test` **332/332 PASS**(72 suites). develop **22커밋 ahead** — v1.2.1 merge gate **FULLY UNBLOCKED**.

> **139차 재검증 (19:42 UTC) — test `@598d108` CLEAN·origin/test 동기화·246/246 PASS·develop `4ee652d` CLEAN·330/330 PASS·21 ahead·origin/develop 동기화·PASS(v1)·Open 0(backend)·★ v1.2.1 merge UNBLOCKED**:
> test·origin/test `598d108` 동기화 유지. test `mvn test` **246/246 PASS**(64 suites)·JAR **76,675,999 B**·Boot **3.3.1**·Flyway **V50**.
> develop HEAD **`4ee652d`**(`feat(v2/US-L02): enrich overdue claims list with pagination and guardian context` — `BillingService` +147·`BillingServiceTest` +200·`NotificationRepository` +19·`OverdueClaimListResponse`, 7 files +358/-33, 329→330 +1 @Test). develop `mvn test` **330/330 PASS**(72 suites). develop **21커밋 ahead** — v1.2.1 merge gate **FULLY UNBLOCKED**.

> **137차 재검증 (19:18 UTC) — test `@598d108` CLEAN·origin/test 동기화·246/246 PASS·develop `469d08c` CLEAN·329/329 PASS·20 ahead·origin/develop 동기화·PASS(v1)·Open 0(backend)·★ v1.2.1 merge UNBLOCKED**:
> test·origin/test `598d108` 동기화 유지. test `mvn test` **246/246 PASS**(64 suites)·JAR **76,675,999 B**·Boot **3.3.1**·Flyway **V50**.
> develop HEAD **`469d08c`**(`perf(v2/G21): add partial index for confirmed-plan import guard` — `V57__visit_schedules_plan_blocking_exists_index.sql` +17 lines, migration-only·329 @Test 불변). develop `mvn test` **329/329 PASS**(72 suites). develop **20커밋 ahead** — v1.2.1 merge gate **FULLY UNBLOCKED**.

> **135차 재검증 (18:50 UTC) — test `@598d108` CLEAN·origin/test 동기화·246/246 PASS·develop `3e4d3e6` CLEAN·329/329 PASS·19 ahead·origin/develop 동기화·PASS(v1)·Open 0(backend)·★ v1.2.1 merge UNBLOCKED**:
> test·origin/test `598d108` 동기화 유지. test `mvn test` **246/246 PASS**(64 suites)·JAR **76,675,999 B**·Boot **3.3.1**·Flyway **V50**.
> develop HEAD **`3e4d3e6`**(`feat(v2/G21): sync paired PLAN/BILLING draft updates` — `VisitService` +22·`VisitServiceTest` +47, 2 files +69, 328→329 +1 @Test). develop `mvn test` **329/329 PASS**(72 suites). develop **19커밋 ahead** — v1.2.1 merge gate **FULLY UNBLOCKED**.

> **133차 재검증 (18:32 UTC) — test `@598d108` CLEAN·origin/test 동기화·246/246 PASS·develop `b63bb1f` CLEAN·328/328 PASS·18 ahead·origin/develop 동기화·PASS(v1)·Open 0(backend)·★ v1.2.1 merge UNBLOCKED**:
> test·origin/test `598d108` 동기화 유지. test `mvn test` **246/246 PASS**(64 suites)·JAR **76,675,999 B**·Boot **3.3.1**·Flyway **V50**.
> develop HEAD **`b63bb1f`**(`feat(v2/G21): cascade visit cancel to paired PLAN/BILLING schedule (US-V02)` — `VisitService` +36·`VisitServiceTest` +90, 2 files +123, 325→328 +3 @Test). develop `mvn test` **328/328 PASS**(72 suites). develop **18커밋 ahead** — v1.2.1 merge gate **FULLY UNBLOCKED**.

> **131차 재검증 (18:10 UTC) — test `@598d108` CLEAN·origin/test 동기화·246/246 PASS·develop `84f3441` CLEAN·325/325 PASS·17 ahead·PASS(v1)·Open 0(backend)·★ v1.2.1 merge UNBLOCKED**:
> test·origin/test `598d108` 동기화 유지. test `mvn test` **246/246 PASS**(64 suites)·JAR **76,675,999 B**·Boot **3.3.1**·Flyway **V50**.
> develop HEAD **`84f3441`**(`feat(v2/G21,G2): block billing NHIS import on confirmed plan and add guardian billing notify API` — `VisitService` 확정 plan import 차단·`BillingController` guardian billing notify·`BillingServiceTest` +109·`VisitServiceTest` +83·`J03AlimtalkServiceFlowE2eTest` +44, 8 files +338, 320→325 +5 @Test). develop `mvn test` **325/325 PASS**(72 suites). develop **17커밋 ahead** — v1.2.1 merge gate **FULLY UNBLOCKED**.

> **129차 재검증 (17:52 UTC) — test `@598d108` CLEAN·origin/test 동기화·246/246 PASS·develop `803436d` CLEAN·320/320 PASS·16 ahead·PASS(v1)·Open 0(backend)·★ v1.2.1 merge UNBLOCKED**:
> test·origin/test `598d108` 동기화 유지. test `mvn test` **246/246 PASS**(64 suites)·JAR **76,675,999 B**·Boot **3.3.1**·Flyway **V50**.
> develop HEAD **`803436d`**(`test: add routing coverage for visit APIs` — `VisitControllerRoutingTest` +225 lines, test-only, 311→320 +9 @Test). develop `mvn test` **320/320 PASS**(72 suites). develop **16커밋 ahead** — v1.2.1 merge gate **FULLY UNBLOCKED**.

> **127차 재검증 (17:35 UTC) — test `@598d108` CLEAN·origin/test 동기화·246/246 PASS·develop `0c069b5` CLEAN·311/311 PASS·15 ahead·PASS(v1)·Open 0(backend)·★ v1.2.1 merge UNBLOCKED**:
> test·origin/test `598d108` 동기화 유지. test `mvn test` **246/246 PASS**(64 suites)·JAR **76,675,999 B**·Boot **3.3.1**·Flyway **V50**.
> develop HEAD **`0c069b5`**(`fix(v2/G21): guard invalid visit service minutes` — `VisitService` create/update·NHIS import service minutes 범위 가드·`VisitServiceTest` +93, 2 files +105, 309→311 +2 @Test). develop `mvn test` **311/311 PASS**(71 suites). develop **15커밋 ahead** — v1.2.1 merge gate **FULLY UNBLOCKED**.

> **125차 재검증 (17:13 UTC) — test `@598d108` CLEAN·origin/test 동기화·246/246 PASS·develop `fe5b38b` CLEAN·309/309 PASS·14 ahead·PASS(v1)·Open 0·★ v1.2.1 merge UNBLOCKED**:
> test·origin/test `598d108` 동기화 유지. test `mvn test` **246/246 PASS**(64 suites)·JAR **76,675,999 B**·Boot **3.3.1**·Flyway **V50**.
> develop HEAD **`fe5b38b`**(`feat(auth): add POST /auth/change-password for logged-in users`) + `adec560`(`feat(v2/G21): add visit_schedules FK-backing indexes (V56)`) 반영. develop `mvn test` **309/309 PASS**(71 suites, 306→+3)·`mvn -DskipTests package` JAR **76,768,334 B**. develop **14커밋 ahead** — v1.2.1 merge gate **FULLY UNBLOCKED**.

> **123차 재검증 (16:32 UTC) — test `@598d108` CLEAN·origin/test 동기화·246/246 PASS·develop `ee3fa3a` CLEAN·306/306 PASS·12 ahead·PASS(v1)·Open 0·★ v1.2.1 merge UNBLOCKED**:
> test·origin/test `598d108` 동기화 유지. test `mvn test` **246/246 PASS**(64 suites)·JAR **76,675,999 B**·Boot **3.3.1**·Flyway **V50**.
> develop HEAD **`ee3fa3a`**(`feat(v2/G21): add NHIS visit schedule import API` — `NhisVisitScheduleExcelParser`·`VisitController` import endpoint·`NhisVisitScheduleExcelParserTest`·`VisitServiceTest`·`RoleBasedControllerAccessTest` +50, 8 files +732, 298→306 +8 @Test). develop `mvn test` **306/306 PASS**(71 suites). develop **12커밋 ahead** — v1.2.1 merge gate **FULLY UNBLOCKED**. v2/G21 NHIS visit import **develop-only bleed**(결정 92).

> **121차 재검증 (16:12 UTC) — test `@598d108` CLEAN·origin/test 동기화·246/246 PASS·develop `e304fd3` CLEAN·298/298 PASS·11 ahead·PASS(v1)·Open 0·★ v1.2.1 merge UNBLOCKED**:
> test·origin/test `598d108` 동기화 유지. test `mvn test` **246/246 PASS**(64 suites)·JAR **76,675,999 B**·Boot **3.3.1**·Flyway **V50**.
> develop HEAD **`e304fd3`**(`feat(v2/G21): restrict visit schedules to HOME_VISIT branches only`)로 119차 Open 이슈 `QA-20260609-B08` 원인(VisitService dirty-tree) 해소. develop `mvn test` **298/298 PASS**(70 suites). develop **11커밋 ahead** — v1.2.1 merge gate **FULLY UNBLOCKED**.

> **119차 재검증 (15:55 UTC) — test `@598d108` CLEAN·origin/test **동기화**·**246/246 PASS**·develop `a49e496` HEAD **불변**·WT **DIRTY 2M**(VisitService·VisitServiceTest — INTEGRATED_HOME 제외 WIP)·develop HEAD **297/297 PASS**·WT **298/298 PASS**(+1)·10 ahead·PASS(v1)·Open 1 BLOCK·⚠ v1.2.1 merge BLOCK**:
> test·origin/test **`598d108`** 동기화 유지. test `mvn test` **246/246 PASS**(64 suites)·JAR **76,675,999 B**·Boot **3.3.1**·Flyway **V50**.
> develop HEAD **`a49e496`** — 117차 대비 **불변**. WT **CLEAN→DIRTY 2M**(117차 재오염): `VisitService.java` INTEGRATED_HOME 제거·에러 메시지 변경 · `VisitServiceTest.java` +25 lines(+1 @Test).
> develop HEAD `mvn test` **297/297 PASS**(70 suites). WT dirty **298/298 PASS**. develop **10커밋 ahead** — v1.2.1 merge ready이나 **merge gate BLOCK**(WT dirty·QA-20260609-B08). **신규 Open 1건 BLOCK**. **판정 PASS(v1 merged baseline)**.

> **117차 재검증 (15:40 UTC) — test `@598d108` CLEAN·origin/test **동기화**·**246/246 PASS**·develop `a49e496` CLEAN·**297/297 PASS**(70 suites)·10 ahead·PASS(v1)·Open 0·★ merge gate UNBLOCKED**:
> test·origin/test **`598d108`** 동기화 유지. test `mvn test` **246/246 PASS**(64 suites)·JAR **76,675,999 B**·Boot **3.3.1**·Flyway **V50**.
> develop HEAD **`a49e496`** — 115차 `dd49204` 대비 **+4커밋**·WT **DIRTY 22→CLEAN**(115차 WIP 전부 커밋): `8068148` validation errors · `7db78cc` v3 POST meals/programs schedule · `83fe308` V55 visit integrity · `a49e496` clients guardian summary.
> develop `mvn test` **297/297 PASS**(70 suites, 115차 288 → +9). develop **10커밋 ahead** — v1.2.1 merge ready · **merge gate FULLY UNBLOCKED**. **신규 Open 0건**. **판정 PASS(v1 merged baseline)**.

> **115차 재검증 (14:35 UTC) — test `@598d108` CLEAN·origin/test **동기화**·**246/246 PASS**(64 suites·0 fail)·develop `dd49204` HEAD **불변**·WT **DIRTY 22**(15→22)·6 ahead·PASS(v1)·Open 0·⚠ v1.2.1 merge 선행 develop WT clean 미충족**:
> test·origin/test **`598d108`** 동기화 유지. test `mvn test` **246/246 PASS**(64 suites·0 fail/0 error)·JAR **76,675,999 B**·Boot **3.3.1**·Flyway **V50**.
> develop HEAD **`dd49204`** — 113차 대비 **불변**. WT **DIRTY 15→22**(18M+4U): ① v3 meals/programs **schedule API**(`CreateMealMenuRequest`·`CreateProgramScheduleRequest`·Meal/Program Controller·Service) ② `V55__visit_schedules_integrity_triggers.sql` + Visit WIP ③ **validation-error 매핑 리팩터**(`ValidationErrorMapper`·`ApiError`·`GlobalExceptionHandler`+Test·`CreateUserRequest`) ④ Client WIP. 전부 **coder develop-only 미커밋**. **HEAD Fixed @ dd49204** ✓ (6-ahead artifact cat-file PRESENT).
> develop HEAD `mvn test` **미재실행**(WT DIRTY — HEAD 불변·113차 288/288 유효). develop **6커밋 ahead** — v1.2.1 merge ready이나 **merge 선행 develop WT clean 미충족**(DIRTY 22·coder 커밋 필요). **신규 Open 0건**·회귀 0. **판정 PASS(v1 merged baseline)**.

> **113차 재검증 (13:25 UTC) — test `@598d108` CLEAN·origin/test **동기화**·246/246 PASS·develop `dd49204` HEAD **불변**·WT **DIRTY 15**·PASS(v1)·Open 0**:
> test·origin/test **`598d108`** 동기화 유지. test `mvn test` **246/246 PASS**(64 suites)·JAR **76,675,999 B**·Boot **3.3.1**·Flyway **V50**.
> develop HEAD **`dd49204`** — 112차 대비 **불변**. WT **CLEAN→DIRTY 15**(12M+3U): v3 meals/programs schedule API(`CreateMealMenuRequest`·`CreateProgramScheduleRequest`)·`V55__visit_schedules_integrity_triggers.sql`·`ClientResponse`/`ClientService`·`VisitService` WIP. **HEAD Fixed @ dd49204** ✓.
> develop **6커밋 ahead** — v1.2.1 merge ready · **merge 선행 develop WT clean**. **신규 Open 0건**. **판정 PASS(v1 merged baseline)**.

> **112차 재검증 (12:35 UTC) — test `@598d108` CLEAN·origin/test **동기화**·246/246 PASS·develop `dd49204`(+6) CLEAN·288/288 PASS·PASS(v1)·Open 0·TSR 110차 Region 테스트 gap 해소**:
> test·origin/test **`598d108`** 동기화 유지. test `mvn test` **246/246 PASS**(64 suites)·JAR **76,675,999 B**·Boot **3.3.1**·Flyway **V50**.
> develop HEAD **`dd49204`**(+1 vs 110차 `4cc328d`): `test(v1.2.1/G7): Region API tests + NHIS pilot fixture parser coverage` — `RegionLookupServiceTest`(11 @Test)·`RegionControllerRoutingTest`(4)·`RoleBasedControllerAccessTest$RegionAccess`(3 regions RBAC)·`NhisExcelParserTest`(+3-state pilot workbook)·`NhisReconciliationMatcherTest`(6)·`NhisFixtureExporter`(dev 샘플 생성), 5 files +442.
> develop `mvn test` **288/288 PASS**(70 suites, 110차 269 → +19). 신규 Region/NHIS suite 전부 PASS: Region 11+4+3 RBAC·NHIS 4(pilot)+6. WT **CLEAN**. develop **6커밋 ahead** — v1.2.1 merge ready·차기 merge.
> **TSR 110차 `RegionController 단위 테스트 없음` gap 해소** ✓ (COD action item 완료). **신규 Open 0건**. **판정 PASS(v1 merged baseline)**.

> **110차 재검증 (11:50 UTC) — test `@598d108` CLEAN·origin/test **동기화**·246/246 PASS·develop `4cc328d`(+5) CLEAN·269/269 PASS·PASS(v1)·Open 0**:
> test·origin/test **`598d108`** 동기화 유지. test `mvn test` **246/246 PASS**(64 suites)·JAR **76,675,999 B**·Boot **3.3.1**·Flyway **V50**.
> develop HEAD **`4cc328d`**(+5 vs test):
> 1. `2012945` — `feat(v1.2.1): add region master, branch profile, and billing integrity` — `RegionController`·`RegionLookupService`·`V51`·`V52`·27 files +742
> 2. `d768820` — `feat(v2/G21): add visit schedules schema, REST API, and tests` — `VisitController`·`VisitService`·`V53__visit_schedules_v2.sql`·`VisitServiceTest`(5 @Test) — **v2 bleed(결정 92)**
> 3. `15e41e3` — `feat(v1.2.1/G14): add GET ltc-grade-history API for US-M01` — `LtcGradeHistoryService`·`LtcGradeHistoryServiceTest`(4 @Test)·`ClientController` GET endpoint — 12 files +564
> 4. `1812165` — `feat(v2/G21): enforce home-visit branch guard for visit APIs` — `VisitService.java`(+13/-6)·`VisitServiceTest.java`(+32, 5→7 @Test), 2 files +39/-6 — **v2 bleed(결정 92)**
> 5. `4cc328d` — `feat(G7): add NHIS PENDING_REVIEW reconciliation state` — `NhisReconciliationMatcher`·`NhisImportService`·`V54__nhis_pending_review_status.sql`·Nhis*Test(+5 @Test, 264→269), 13 files +336/-24 — **G7 develop-only(v1.2.1 P1)**
> develop `mvn test` **269/269 PASS**(67 suites, 108차 264 → +5). WT **CLEAN**. develop **5커밋 ahead** — v1.2.1 merge ready·차기 merge.
> **RegionController 단위 테스트 없음** — v1.2.1 merge 전 coder 보강 권장. **신규 Open 0건**. **판정 PASS(v1 merged baseline)**.

## 커밋 차이 (develop ahead of test)

| SHA | 메시지 | 범위 | 테스트 증가 |
|-----|--------|------|------------|
| `2012945` | v1.2.1 region master·branch profile·billing integrity | V51·V52·RegionController | 0 (246 불변) |
| `d768820` | v2/G21 visit schedules·REST API | V53·VisitController·VisitServiceTest | +11 (257) |
| `15e41e3` | v1.2.1/G14 GET ltc-grade-history API | LtcGradeHistoryService·Test·routing | +5 (262) |
| `1812165` | v2/G21 home-visit branch guard for visit APIs | VisitService·VisitServiceTest(5→7 @Test) | +2 (264) |
| `4cc328d` | G7 NHIS PENDING_REVIEW reconciliation state | V54·NhisReconciliationMatcher·Nhis*Test | +5 (269) |
| `dd49204` | v1.2.1/G7 Region API tests + NHIS pilot fixture parser coverage | RegionLookupServiceTest 11·RegionControllerRoutingTest 4·RegionAccess RBAC 3·NhisExcelParserTest(pilot)·NhisReconciliationMatcherTest 6·NhisFixtureExporter | +19 (288) |
| `8068148` | field-level validation errors to clients | ValidationErrorMapper·ApiError·GlobalExceptionHandler(+Test)·CreateUserRequest·LoginRequest | +1 (289) |
| `7db78cc` | v3 POST meals menus and programs schedule APIs | CreateMealMenuRequest·CreateProgramScheduleRequest·Meal/Program Controller·Service(+routing·service test) | +4 (293) |
| `83fe308` | v2/G21 visit schedule integrity triggers (V55) | V55__visit_schedules_integrity_triggers.sql·VisitService(+Test) | +3 (296) |
| `a49e496` | clients guardian summary·org-scoped branches | ClientResponse·ClientService·GuardianClientRepository | +1 (297) |
| `e304fd3` | v2/G21 restrict visit schedules to HOME_VISIT branches only | VisitService·VisitServiceTest | +1 (298) |
| `ee3fa3a` | v2/G21 NHIS visit schedule import API | NhisVisitScheduleExcelParser·VisitController import·VisitServiceTest | +8 (306) |
| `adec560` | v2/G21 visit_schedules FK-backing indexes (V56) | `V56__visit_schedules_fk_backing_indexes.sql` | +0 (306) |
| `fe5b38b` | auth change-password API | AuthController/AuthService + tests | +3 (309) |
| `0c069b5` | v2/G21 guard invalid visit service minutes | VisitService·VisitServiceTest | +2 (311) |
| `803436d` | visit API routing coverage (test-only) | VisitControllerRoutingTest | +9 (320) |

## 검증 요약

| 항목 | test @598d108 | develop @803436d |
|------|---------------|------------------|
| `mvn test` | 246/246 PASS (64 suites) | 320/320 PASS (72 suites) |
| working tree | CLEAN | CLEAN |
| origin/test | 동기화 ✓ | — |
| Flyway latest | V50 | V56 |
| JAR size | 76,675,999 B | (develop 미빌드·test 기준) |
| merge gate | — | **FULLY UNBLOCKED** (WT clean·16 ahead·ff 가능) |

## 신규 테스트 (dd49204 — TSR 110차 Region 테스트 gap 해소)

| 테스트 suite | @Test | surefire 결과 |
|--------------|-------|---------------|
| `regions/domain/RegionLookupServiceTest` | 11 | 11/11 PASS |
| `regions/api/RegionControllerRoutingTest` | 4 | 4/4 PASS |
| `security/RoleBasedControllerAccessTest$RegionAccess` | 3 | 3/3 PASS (regions RBAC) |
| `billing/domain/NhisExcelParserTest` (pilot workbook 확장) | 4 | 4/4 PASS |
| `billing/domain/NhisReconciliationMatcherTest` | 6 | 6/6 PASS |
| `billing/domain/NhisFixtureExporter` | — | dev 샘플 생성 유틸 |
