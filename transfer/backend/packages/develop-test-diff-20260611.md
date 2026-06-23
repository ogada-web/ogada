<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-11T23:50:00+00:00 -->
# develop ↔ test diff 메타 (2026-06-11, 385차 — develop WT CLEAN @225b104 · test @598d108 · 122 ahead)

> **385차 재검증 (23:50 UTC) — test `@598d108` CLEAN·origin/test 동기화·246/246 PASS·npm N/A(no package.json)·develop `@225b104`(+1 vs 383차 `c4b230b`: `fix(v2/G21): normalize visit enum-like inputs` — `VisitService`·`VisitServiceTest`, 2 files +97/-4) **WT CLEAN** · develop `mvn test` **640/640 PASS**(118 suites, ~33s, +3 @Test vs 637) · develop **122 ahead** · origin/develop @ `225b104` · PASS(v1) · Open 0(backend) · ★ **v1.2.1 merge FULLY UNBLOCKED**(backend)**:
> develop HEAD **`225b104`** · test와의 ahead **122** · origin/develop 동기화.
> `src/backend-test` `mvn test` **246/246 PASS**(64 suites, ~15s). develop merge gate **FULLY UNBLOCKED**(backend). 교차(frontend git): `@6875af5` WT **CLEAN** · 152 ahead · Open 0(frontend) · **양 스트림 merge gate FULLY UNBLOCKED** · merge pending **274**.

> **383차 재검증 (23:29 UTC) — test `@598d108` CLEAN·origin/test 동기화·246/246 PASS·npm N/A(no package.json)·develop `@c4b230b` WT **CLEAN** · develop `mvn test` **637/637 PASS**(24.515s) · origin/develop 동기화(0 ahead) · PASS(v1) · Open 0(backend) · ★ **v1.2.1 merge FULLY UNBLOCKED**(backend)**:
> develop HEAD **`c4b230b`** · test와의 ahead **0**(origin/develop 동기화).
> `src/backend-test` `mvn test` **246/246 PASS**(64 suites, 14.404s). develop merge gate **FULLY UNBLOCKED**(backend). 교차(frontend git): `@23bcd8c` WT **CLEAN** · origin/develop 동기화(0 ahead) · Open 0(frontend) · **양 스트림 merge gate FULLY UNBLOCKED** · merge pending **0**.

> **381차 재검증 (23:13 UTC) — test `@598d108` CLEAN·origin/test 동기화·246/246 PASS·npm N/A(no package.json)·develop `@0325d95` HEAD **불변**(379차 대비) · WT **DIRTY 1U**(`V79__ltc_grade_history_attachments_integrity_g37.sql`+78 — G37/V78 attachment integrity follow-up, **379차 CLEAN→재오염**) · HEAD **637/637 PASS**(118 suites) · 120 ahead · origin/develop @ `0325d95` · PASS(v1) · **Open 1 BLOCK QA-B45**(backend) · ⚠ **v1.2.1 merge BLOCK**(backend WT dirty)**:
> develop HEAD **`0325d95`**(불변) · untracked **`V79__ltc_grade_history_attachments_integrity_g37.sql`**(78 lines — client-scoped composite FK·uploaded_by actor·temporal CHECK·purge index for V78 attachment table).
> `src/backend-test` `mvn test` **246/246 PASS**(64 suites, ~24s). develop **120커밋 ahead** — merge gate **BLOCK**(backend WT dirty). 교차(frontend git): `@e026ae93` WT **CLEAN** · 150 ahead · Open 0(frontend) · **양 스트림 merge BLOCK**(BE WT clean 선행) · merge pending **270**.

> **379차 재검증 (22:35 UTC) — test `@598d108` CLEAN·origin/test 동기화·246/246 PASS·npm N/A(no package.json)·develop `@0325d95`(+1 vs 377차 `d86405c`: `feat(v2/G37): add LTC grade history care-plan attachment API (BNK-105)` — `LtcGradeHistoryAttachmentStorageService`·V78·`LtcGradeHistoryAttachmentServiceTest`·`MustApiEndpointRoutingTest`, 18 files +1341) **WT CLEAN** · HEAD **637/637 PASS**(118 suites, +11 @Test vs 626) · 120 ahead · origin/develop @ `0325d95` · PASS(v1) · Open 0(backend) · ★ **v1.2.1 merge FULLY UNBLOCKED**(backend)**:
> develop HEAD **`0325d95`**(+1: v2/G37 LTC grade history care-plan attachment API — `ClientController` upload/list/download·`LtcGradeHistoryAttachmentStorageService`·V78 migration·`LtcGradeHistoryAttachmentServiceTest` 400 lines).
> `src/backend-test` `mvn test` **246/246 PASS**(64 suites, ~24s). develop **120커밋 ahead** — merge gate **FULLY UNBLOCKED**(backend). 교차(frontend git): `@730792b` WT **CLEAN** · 148 ahead · Open 0(frontend) · **양 스트림 merge gate FULLY UNBLOCKED** · merge pending **268**.

> **377차 재검증 (22:14 UTC) — test `@598d108` CLEAN·origin/test 동기화·246/246 PASS·npm N/A(no package.json)·develop `@d86405c`(+1 vs 375차 `555a19f`: `test(v2/J03): add primary guardian dispatch E2E coverage` — `J03AlimtalkServiceFlowE2eTest`·`NotificationAlimtalkDispatchE2eTest`, 2 files +180) **WT CLEAN** · HEAD **626/626 PASS**(116 suites, +3 @Test vs 623) · 119 ahead · origin/develop @ `d86405c` · PASS(v1) · Open 0(backend) · ★ **v1.2.1 merge FULLY UNBLOCKED**(backend)**:
> develop HEAD **`d86405c`**(+1: v2/J03 primary guardian dispatch E2E — `J03AlimtalkServiceFlowE2eTest` +74 lines·`NotificationAlimtalkDispatchE2eTest` +106 lines).
> `src/backend-test` `mvn test` **246/246 PASS**(64 suites, ~23s). develop **119커밋 ahead** — merge gate **FULLY UNBLOCKED**(backend). 교차(frontend git): `@eb488799` WT **CLEAN** · 147 ahead · Open 0(frontend) · **양 스트림 merge gate FULLY UNBLOCKED** · merge pending **266**.

> **375차 재검증 (21:55 UTC) — test `@598d108` CLEAN·origin/test 동기화·246/246 PASS·npm N/A(no package.json)·develop `@555a19f`(+1 vs 373차 `c58b739`: `feat(v2/J03): prioritize primary guardian for dispatch` — `NotificationService`·`NotificationServiceTest`, 2 files +149/-13) **WT CLEAN** · HEAD **623/623 PASS**(116 suites, +2 @Test vs 621) · 118 ahead · origin/develop @ `555a19f` · PASS(v1) · Open 0(backend) · ★ **v1.2.1 merge FULLY UNBLOCKED**(backend)**:
> develop HEAD **`555a19f`**(+1: v2/J03 알림 발송 시 primary guardian 우선 — `NotificationService` dispatch 대상 정렬·`NotificationServiceTest` +91 lines).
> `src/backend-test` `mvn test` **246/246 PASS**(64 suites, ~24s). develop **118커밋 ahead** — merge gate **FULLY UNBLOCKED**(backend). 교차(frontend git): `@48827b6` WT **CLEAN** · 146 ahead · Open 0(frontend) · **양 스트림 merge gate FULLY UNBLOCKED** · merge pending **264**.

> **371차 재검증 (21:12 UTC) — test `@598d108` CLEAN·origin/test 동기화·246/246 PASS·npm N/A(no package.json)·develop `@367fd45`(+1 vs 369차 `8626f18`: `test(v2/G33): add billing start balance pilot service-flow E2E (BNK-103)` — `BillingStartBalancePilotServiceFlowE2eTest`·`PilotChecklistJwtE2eTest`, 2 files +110) **WT CLEAN** · HEAD **617/617 PASS**(115 suites, +3 @Test vs 614) · 116 ahead · origin/develop @ `367fd45` · PASS(v1) · Open 0(backend) · ★ **v1.2.1 merge FULLY UNBLOCKED**(backend)**:
> develop HEAD **`367fd45`**(+1: G33 billing start balance pilot service-flow E2E — `BillingStartBalancePilotServiceFlowE2eTest` 3 @Test·`PilotChecklistJwtE2eTest` +53 lines).
> `src/backend-test` `mvn test` **246/246 PASS**(64 suites, ~27s). develop **116커밋 ahead** — merge gate **FULLY UNBLOCKED**(backend). 교차(frontend 370차): `@1113caf` WT **CLEAN** · 144 ahead · Open 0(frontend) · **양 스트림 merge gate FULLY UNBLOCKED** · merge pending **260**.

> **369차 재검증 (20:54 UTC) — test `@598d108` CLEAN·origin/test 동기화·246/246 PASS·npm N/A(no package.json)·develop `@8626f18`(+1 vs 367차 `838a7f6`: `test(v2/G17-G32): add program compliance pilot service-flow E2E (BNK-103)` — `ProgramCompliancePilotServiceFlowE2eTest`·`PilotChecklistJwtE2eTest`, 2 files +384) **WT CLEAN** · HEAD **614/614 PASS**(115 suites, +5 @Test vs 609) · 115 ahead · origin/develop @ `8626f18` · PASS(v1) · Open 0(backend) · ★ **v1.2.1 merge FULLY UNBLOCKED**(backend)**:
> develop HEAD **`8626f18`**(+1: G17/G32 program compliance pilot service-flow E2E — `ProgramCompliancePilotServiceFlowE2eTest` 3 @Test·`PilotChecklistJwtE2eTest` +52 lines).
> `src/backend-test` `mvn test` **246/246 PASS**(64 suites, ~24s). develop **115커밋 ahead** — merge gate **FULLY UNBLOCKED**(backend). 교차(frontend git): `@63361c0` WT **CLEAN** · 143 ahead · Open 0(frontend) · **양 스트림 merge gate FULLY UNBLOCKED** · merge pending **258**.

> **367차 재검증 (20:01 UTC) — test `@598d108` CLEAN·origin/test 동기화·246/246 PASS·npm N/A(no package.json)·develop `@838a7f6`(+1 vs 365차 `c5a6cec`: `fix(v2/G2): return FAILED CMS debit response for operator retry` — `CmsService`·`CmsCopayLifecycleE2eTest`·`CmsServiceTest`, 4 files +136/-35) **WT CLEAN** · HEAD **609/609 PASS**(114 suites, +1 @Test vs 608) · 114 ahead · origin/develop @ `838a7f6` · PASS(v1) · Open 0(backend) · ★ **v1.2.1 merge FULLY UNBLOCKED**(backend)**:
> develop HEAD **`838a7f6`**(+1: G2 FCMS debit 실패 시 FAILED 응답 반환·운영자 재시도 UX — `CmsService` debit 실패 처리·`CmsCopayLifecycleE2eTest`·`CmsServiceTest` +101 lines).
> `src/backend-test` `mvn test` **246/246 PASS**(64 suites, ~26s). develop **114커밋 ahead** — merge gate **FULLY UNBLOCKED**(backend). 교차(frontend git): `@f1c60fe` WT **CLEAN** · 141 ahead · Open 0(frontend) · **양 스트림 merge gate FULLY UNBLOCKED** · merge pending **255**.

> **365차 재검증 (19:41 UTC) — test `@598d108` CLEAN·origin/test 동기화·246/246 PASS·npm N/A(no package.json)·develop `@c5a6cec`(+1 vs 363차 `e820b28`: `fix(v2/G2): preserve failed CMS debit history` — `CmsDebitFailureException`·`CmsService`·`CmsServiceTest`, 3 files +55/-3) **WT CLEAN** · HEAD **608/608 PASS**(114 suites, +2 @Test vs 606) · 113 ahead · origin/develop @ `c5a6cec` · PASS(v1) · Open 0(backend) · ★ **v1.2.1 merge FULLY UNBLOCKED**(backend)**:
> develop HEAD **`c5a6cec`**(+1: G2 FCMS debit 실패 시에도 debit 이력 커밋·운영자 검수 가능 — `CmsDebitFailureException`·`CmsService` rollback 제거·`CmsServiceTest` +43 lines).
> `src/backend-test` `mvn test` **246/246 PASS**(64 suites, ~25s). develop **113커밋 ahead** — merge gate **FULLY UNBLOCKED**(backend). 교차(frontend 364차): `@21b1855` WT **CLEAN** · 140 ahead · Open 0(frontend) · **양 스트림 merge gate FULLY UNBLOCKED** · merge pending **253**.

> **363차 재검증 (19:22 UTC) — test `@598d108` CLEAN·origin/test 동기화·246/246 PASS·npm N/A(no package.json)·develop `@e820b28`(+1 vs 361차 `0048105`: `feat(v2/G17): add provision-recorded compliance and benefit-start create guard (BNK-100)` — `FunctionalRecoveryComplianceItemResponse`·`FunctionalRecoveryService`·`FunctionalRecoveryPlanEntity`·`FunctionalRecoveryServiceTest`·routing/RBAC, 6 files +54/-2) **WT CLEAN** · HEAD **606/606 PASS**(114 suites, +1 @Test vs 605) · 112 ahead · origin/develop @ `e820b28` · PASS(v1) · Open 0(backend) · ★ **v1.2.1 merge FULLY UNBLOCKED**(backend)**:
> develop HEAD **`e820b28`**(+1: G17 `provisionRecordedMet` compliance(silverangel 지표27 row2)·`ltcCertValidFrom` 이후 신규 plan 생성 차단 — `FunctionalRecoveryService`·`FunctionalRecoveryServiceTest` +31 lines·routing/RBAC +2).
> `src/backend-test` `mvn test` **246/246 PASS**(64 suites, ~15s). develop **112커밋 ahead** — merge gate **FULLY UNBLOCKED**(backend). 교차(frontend 362차): `@359cf0c` WT **CLEAN** · 139 ahead · Open 0(frontend) · **양 스트림 merge gate FULLY UNBLOCKED** · merge pending **251**.

> **361차 재검증 (18:58 UTC) — test `@598d108` CLEAN·origin/test 동기화·246/246 PASS·npm N/A(no package.json)·develop `@0048105`(+1 vs 359차 `42bc06e`: `feat(v2/G17): add benefit-start plan due compliance to functional recovery API (BNK-100)` — `FunctionalRecoveryComplianceItemResponse`·`FunctionalRecoveryService`·`FunctionalRecoveryPlanEntity`·`FunctionalRecoveryServiceTest`·routing/RBAC, 7 files +67/-2) **WT CLEAN** · HEAD **605/605 PASS**(114 suites, +1 @Test vs 604) · 111 ahead · origin/develop @ `0048105` · PASS(v1) · Open 0(backend) · ★ **v1.2.1 merge FULLY UNBLOCKED**(backend)**:
> develop HEAD **`0048105`**(+1: G17 benefit-start plan due compliance — `FunctionalRecoveryService`·`FunctionalRecoveryPlanEntity`·compliance DTO·`FunctionalRecoveryServiceTest` +34 lines·routing/RBAC +2).
> `src/backend-test` `mvn test` **246/246 PASS**(64 suites, ~16s). develop **111커밋 ahead** — merge gate **FULLY UNBLOCKED**(backend). 교차(frontend git): `@e88a125` WT **CLEAN** · 138 ahead · Open 0(frontend) · **양 스트림 merge gate FULLY UNBLOCKED** · merge pending **249**.

> **359차 재검증 (18:37 UTC) — test `@598d108` CLEAN·origin/test 동기화·246/246 PASS·npm N/A(no package.json)·develop `@42bc06e`(+1 vs 357차 `70e6191`: `fix(v2/G33): enforce billing start balance integrity invariants` — `BillingSettingsService`·`V77__billing_start_balance_integrity.sql`·`BillingSettingsServiceTest`, 3 files +147/-3) **WT CLEAN** · HEAD **604/604 PASS**(114 suites, @Test 수 불변 vs 357차 WT) · 110 ahead · origin/develop @ `42bc06e` · PASS(v1) · **QA-20260611-B44 Fixed** · Open 0(backend) · ★ **v1.2.1 merge FULLY UNBLOCKED**(backend)**:
> develop HEAD **`42bc06e`**(+1: G33/V76 follow-up integrity — `V77__billing_start_balance_integrity.sql`(actor tenant FK·lock immutability·settlement guards)·`BillingSettingsService` hardening·`BillingSettingsServiceTest` +30 lines).
> `src/backend-test` `mvn test` **246/246 PASS**(64 suites, ~26s). develop **110커밋 ahead** — merge gate **FULLY UNBLOCKED**(backend). 교차(frontend git): `@0ba2b68` WT **CLEAN** · 137 ahead · Open 0(frontend) · **양 스트림 merge gate FULLY UNBLOCKED** · merge pending **247**.

> **357차 재검증 (18:19 UTC) — test `@598d108` CLEAN·origin/test 동기화·246/246 PASS·npm N/A(no package.json)·develop `@70e6191` HEAD **불변**(355차 대비)·WT **DIRTY 2M+1U**(`BillingSettingsService.java`+11/-3 · `BillingSettingsServiceTest.java`+30 · `V77__billing_start_balance_integrity.sql`+109 — G33/V76 billing start balance integrity WIP, **355차 CLEAN→재오염**) · HEAD **603/603 PASS** · WT **604/604 PASS**(+1 @Test) · 109 ahead · origin/develop @ `70e6191` · PASS(v1) · **Open 1 BLOCK QA-B44**(backend) · ⚠ **v1.2.1 merge BLOCK**(backend)**:
> develop HEAD **`70e6191`**(**불변**). WT **DIRTY** — G33/V76 follow-up: `V77__billing_start_balance_integrity.sql`(actor tenant FK·lock immutability·settlement guards)·`BillingSettingsService` integrity hardening·`BillingSettingsServiceTest` +30 lines.
> `src/backend-test` `mvn test` **246/246 PASS**(64 suites, ~14s). develop **109커밋 ahead** — merge gate **BLOCK**(backend WT dirty). 교차(frontend git): `@4b06200` WT **CLEAN** · 136 ahead · SEC-D22 Planned · **양 스트림 merge BLOCK** · merge pending **245**.

> **355차 재검증 (17:40 UTC) — test `@598d108` CLEAN·origin/test 동기화·246/246 PASS·npm N/A(no package.json)·develop `@70e6191`(+1 vs 353차 `deaae7a`: `feat(v2/G33): add billing start balance settlement API and claim guard` — `BillingSettingsController`·`BillingStartBalanceSettlementResponse`·`RecordBillingStartBalanceSettlementRequest`·`BillingService`·`BillingSettingsService`·tests, 7 files +308/-5) **WT CLEAN** · HEAD **603/603 PASS**(114 suites, +4 @Test) · 109 ahead · origin/develop @ `70e6191` · PASS(v1) · Open 0(backend) · ★ **v1.2.1 merge FULLY UNBLOCKED**(backend)**:
> develop HEAD **`70e6191`**(+1: G33 locked onboarding start balance 정산 API·청구 생성 시 start balance guard — `BillingSettingsService` settlement·`BillingService` claim guard·`BillingSettingsServiceTest` +93 lines).
> `src/backend-test` `mvn test` **246/246 PASS**(64 suites, ~20s). develop **109커밋 ahead** — merge gate **FULLY UNBLOCKED**(backend). 교차(frontend 354차): `@7564c2a` WT **CLEAN** · 135 ahead · Open 1 SEC-D22(BLOCK 아님) · **양 스트림 merge gate FULLY UNBLOCKED** · merge pending **244**.

> **353차 재검증 (17:22 UTC) — test `@598d108` CLEAN·origin/test 동기화·246/246 PASS·npm N/A(no package.json)·develop `@deaae7a`(+1 vs 351차 `e7df238`: `feat(v2/G33): surface unpaid billing start balance in overdue list` — `BillingService`·`DashboardService`·`BillingServiceTest`·`DashboardServiceTest`·`BankDepositExcelParserTest`, 5 files +304/-1) **WT CLEAN** · HEAD **599/599 PASS**(114 suites, +11 @Test) · 108 ahead · origin/develop @ `deaae7a` · PASS(v1) · Open 0(backend) · ★ **v1.2.1 merge FULLY UNBLOCKED**(backend)**:
> develop HEAD **`deaae7a`**(+1: G33 locked onboarding start balance를 overdue list·dashboard summary에 반영 — 미납 이월잔액 E2E·`BillingServiceTest`·`DashboardServiceTest` +176 lines·`BankDepositExcelParserTest` 신규).
> `src/backend-test` `mvn test` **246/246 PASS**(64 suites, ~20s). develop **108커밋 ahead** — merge gate **FULLY UNBLOCKED**(backend). 교차(frontend 352차): `@eba413a` WT **CLEAN** · 134 ahead · Open 1 SEC-D22(BLOCK 아님) · **양 스트림 merge gate FULLY UNBLOCKED** · merge pending **242**.

> **351차 재검증 (17:01 UTC) — test `@598d108` CLEAN·origin/test 동기화·246/246 PASS·npm N/A(no package.json)·develop `@e7df238`(+1 vs 349차 `3d5eb3e`: `feat(v2/G33): include billing start balance in charges ledger report` — `BillingService`·`BillingServiceTest`, 2 files +153/-2) **WT CLEAN** · HEAD **588/588 PASS**(114 suites, +1 @Test) · 107 ahead · origin/develop @ `e7df238` · PASS(v1) · Open 0(backend) · ★ **v1.2.1 merge FULLY UNBLOCKED**(backend)**:
> develop HEAD **`e7df238`**(+1: G33 locked opening balance를 US-M03 charges ledger report에 선행 반영 — effectiveMonth 일치 시 onboarding carry-over가 copay totals에 E2E 반영·BNK-94 P2).
> `src/backend-test` `mvn test` **246/246 PASS**(64 suites, ~26s). develop **107커밋 ahead** — merge gate **FULLY UNBLOCKED**(backend). 교차(frontend git): `@9e1a2ed` WT **CLEAN** · 133 ahead · **양 스트림 merge gate FULLY UNBLOCKED** · merge pending **240**.

> **349차 재검증 (16:40 UTC) — test `@598d108` CLEAN·origin/test 동기화·246/246 PASS·npm N/A(no package.json)·develop `@3d5eb3e`(+1 vs 347차 `0441a07`: `feat(v2/G33): add one-time billing start balance API (BNK-94)` — `BillingSettingsController`·`BillingStartBalanceResponse`·`SetBillingStartBalanceRequest`·`BillingSettingsService`·`OrganizationEntity`·`V76__billing_start_balance_g33.sql`·`BillingSettingsServiceTest`, 8 files +290/-2) **WT CLEAN** · HEAD **587/587 PASS**(114 suites, +3 @Test) · 106 ahead · origin/develop @ `3d5eb3e` · PASS(v1) · Open 0(backend) · ★ **v1.2.1 merge FULLY UNBLOCKED**(backend)**:
> develop HEAD **`3d5eb3e`**(+1: G33 케어포 PDF 7-3 온보딩 이월잔액 API — 미납(+)·선납(-) 1회 설정·hq_admin 전용·`V76` 조직 컬럼·`BillingSettingsServiceTest` +90 lines).
> `src/backend-test` `mvn test` **246/246 PASS**(64 suites, ~25s). develop **106커밋 ahead** — merge gate **FULLY UNBLOCKED**(backend). 교차(frontend git): `@7f2289b` WT **CLEAN** · 132 ahead · **양 스트림 merge gate FULLY UNBLOCKED** · merge pending **238**.

> **347차 재검증 (16:20 UTC) — test `@598d108` CLEAN·origin/test 동기화·246/246 PASS·npm N/A(no package.json)·develop `@0441a07`(+1 vs 345차 `cbb7f55`: `fix(v2/US-D01): require and persist primary guardian on client creation` — `CreateClientRequest`·`PrimaryGuardianLinkRequest`·`ClientService`·`ClientServiceTest`·`RoleBasedControllerAccessTest`, 5 files +84/-1) **WT CLEAN** · HEAD **584/584 PASS**(114 suites, @Test 수 불변) · 105 ahead · origin/develop @ `0441a07` · PASS(v1) · Open 0(backend) · ★ **v1.2.1 merge FULLY UNBLOCKED**(backend)**:
> develop HEAD **`0441a07`**(+1: US-D01 이용자 등록 시 `primaryGuardian` 필수·동일 트랜잭션 `guardian_clients` 링크 생성 — API_SPEC 계약 정합·고아 client 레코드 방지 · `ClientService`·`PrimaryGuardianLinkRequest`·`ClientServiceTest` +24 lines).
> `src/backend-test` `mvn test` **246/246 PASS**(64 suites, ~25s). develop **105커밋 ahead** — merge gate **FULLY UNBLOCKED**(backend). 교차(frontend git): `@c89a82b` WT **CLEAN** · 131 ahead · **양 스트림 merge gate FULLY UNBLOCKED** · merge pending **236**.

> **345차 재검증 (15:56 UTC) — test `@598d108` CLEAN·origin/test 동기화·246/246 PASS·npm N/A(no package.json)·develop `@cbb7f55`(+1 vs 343차 `208b37e`: `fix(security): run tenant context filter after JWT bearer auth` — `SecurityConfig`·`TenantContextFilterTest`, 2 files +91/-2) **WT CLEAN** · HEAD **584/584 PASS**(114 suites, +3 @Test vs 581) · 104 ahead · origin/develop @ `cbb7f55` · PASS(v1) · Open 0(backend) · ★ **v1.2.1 merge FULLY UNBLOCKED**(backend)**:
> develop HEAD **`cbb7f55`**(+1: JWT Bearer 인증 이후 `TenantContextFilter` 실행 순서 보장 — 멀티테넌트 컨텍스트가 인증 전에 적용되던 보안 이슈 수정 · `SecurityConfig` filter chain reorder · `TenantContextFilterTest` +89 lines).
> `src/backend-test` `mvn test` **246/246 PASS**(64 suites, ~20s). develop **104커밋 ahead** — merge gate **FULLY UNBLOCKED**(backend). 교차(frontend git): `@fa2ad1e`(+1 G32 evaluationConductedMet StatCard) WT **CLEAN** · 130 ahead · **양 스트림 merge gate FULLY UNBLOCKED** · merge pending **234**.

> **343차 재검증 (15:14 UTC) — test `@598d108` CLEAN·origin/test 동기화·246/246 PASS·npm N/A(no package.json)·develop `@208b37e`(+1 vs 341차 `98e40a3`: `fix(clients): allow hq admin to create clients` — `ClientController`·`RoleBasedControllerAccessTest`, 2 files +72/-1) **WT CLEAN** · HEAD **581/581 PASS**(113 suites, +2 @Test vs 579) · 103 ahead · origin/develop @ `208b37e` · PASS(v1) · Open 0(backend) · ★ **v1.2.1 merge FULLY UNBLOCKED**(backend)**:
> develop HEAD **`208b37e`**(+1: clients API — HQ admin(`ROLE_HQ_ADMIN`)이 `POST /api/v1/clients` 생성 허용 · `ClientController` `@PreAuthorize` 확장 · `RoleBasedControllerAccessTest` HQ admin create client E2E +71 lines).
> `src/backend-test` `mvn test` **246/246 PASS**(64 suites, ~53s). develop **103커밋 ahead** — merge gate **FULLY UNBLOCKED**(backend). 교차(frontend git): `@932078b` HEAD **불변** · WT **DIRTY 6M+9U**(15 files) · 128 ahead · **QA-B43 BLOCK** · merge pending **231**.

> **341차 재검증 (14:52 UTC) — test `@598d108` CLEAN·origin/test 동기화·246/246 PASS·npm N/A(no package.json)·develop `@98e40a3`(+1 vs 339차 `11277b9`: `fix(v2/J03): enforce approved Solapi template mappings` — `NotificationConfig`·`NotificationConfigTest`, 2 files +69) **WT CLEAN** · HEAD **579/579 PASS**(113 suites, +1 @Test vs 578) · 102 ahead · origin/develop @ `98e40a3` · PASS(v1) · Open 0(backend) · ★ **v1.2.1 merge FULLY UNBLOCKED**(backend)**:
> develop HEAD **`98e40a3`**(+1: v2/J03 Solapi Kakao template ID placeholder 거부 — 미승인 매핑으로 live 알림톡 기동 방지 · `NotificationConfig` startup guard·`NotificationConfigTest` +32 lines).
> `src/backend-test` `mvn test` **246/246 PASS**(64 suites, ~15s). develop **102커밋 ahead** — merge gate **FULLY UNBLOCKED**(backend). 교차(frontend git): `@40c303d` WT **CLEAN** · 127 ahead · **QA-B42 Fixed** · merge pending **229**.

> **339차 재검증 (14:25 UTC) — test `@598d108` CLEAN·origin/test 동기화·246/246 PASS·npm N/A(no package.json)·develop `@11277b9`(+1 vs 8431b5c: `feat(v2/G32): add evaluation conducted compliance for indicator 29 (BNK-92 P1)` — `CaseManagementService`·`FunctionalRecoveryPlanRepository`·`ProgramParticipationRepository`·`CaseManagementServiceTest`, 8 files +144/-4) **WT CLEAN** · HEAD **578/578 PASS**(113 suites, +1 @Test vs 577) · 101 ahead · origin/develop @ `11277b9` · PASS(v1) · Open 0(backend) · ★ **v1.2.1 merge FULLY UNBLOCKED**(backend)**:
> develop HEAD **`11277b9`**(+1: G32 지표29 evaluation conducted compliance — `CaseManagementService` compliance API·G17 functional recovery plan·program participation 집계·`CaseManagementServiceTest` +62 lines).
> `src/backend-test` `mvn test` **246/246 PASS**(64 suites, ~23s). develop **101커밋 ahead** — merge gate **FULLY UNBLOCKED**(backend). 교차(frontend git): `@443f379` WT **CLEAN** · 126 ahead · **QA-B42 BLOCK** · merge pending **227**.

> **337차 재검증 (14:04 UTC) — test `@598d108` CLEAN·origin/test 동기화·246/246 PASS·npm N/A(no package.json)·develop `@8431b5c`(+1 vs 335차 `0a270a2`: `fix(v2/US-L03): reuse cancelled CMS enrollment on re-registration` — `CmsService`·`CmsServiceTest`, 2 files +52/-14) **WT CLEAN** · HEAD **577/577 PASS**(113 suites, +1 @Test vs 576) · 100 ahead · origin/develop @ `8431b5c` · PASS(v1) · Open 0(backend) · ★ **v1.2.1 merge FULLY UNBLOCKED**(backend)**:
> develop HEAD **`8431b5c`**(+1: v2/US-L03 CMS 취소된 등록(enrollment) 재등록 시 기존 레코드 재사용 — `CmsService.registerEnrollment()` cancelled 상태 enrollment lookup·reactivate·`CmsServiceTest` +1 @Test).
> `src/backend-test` `mvn test` **246/246 PASS**(64 suites, ~24s). develop **100커밋 ahead** — merge gate **FULLY UNBLOCKED**(backend). 교차(frontend git): `@18f5173` WT **CLEAN** · 125 ahead · merge pending **225**.

> **334차 재검증 (13:45 UTC) — test `@598d108` CLEAN·origin/test 동기화·246/246 PASS·npm N/A(no package.json)·develop `@0a270a2`(+1 vs 333차 `5e1828c`: `feat(v2/G32): add case management plan field to meeting API (BNK-91 P2)` — DTO 3종·`CaseManagementService`·`CaseManagementMeetingEntity`·`V75__case_management_plan_g32.sql`·`CaseManagementServiceTest`·routing/RBAC, 9 files +46) **WT CLEAN** · HEAD **576/576 PASS**(113 suites, @Test 수 불변) · 99 ahead · origin/develop @ `0a270a2` · PASS(v1) · Open 0(backend) · ★ **v1.2.1 merge FULLY UNBLOCKED**(backend)**:
> develop HEAD **`0a270a2`**(+1: G32 사례관리 회의록 `managementPlan` 필드 — silverangel 지표43·케어포 8-5 패리티(BNK-91 P2) · Flyway V75 · create/update/response DTO·entity·service·tests).
> `src/backend-test` `mvn test` **246/246 PASS**(64 suites, ~24s). develop **99커밋 ahead** — merge gate **FULLY UNBLOCKED**(backend). 교차(frontend git): `@b71a10e`(+1 NHIS comparison copay column) WT **CLEAN** · 124 ahead · merge pending **223**.

> **333차 재검증 (13:28 UTC) — test `@598d108` CLEAN·origin/test 동기화·246/246 PASS·npm N/A(no package.json)·develop `@5e1828c` HEAD **불변**(331차 대비) **WT CLEAN** · HEAD **576/576 PASS**(113 suites) · 98 ahead · origin/develop @ `5e1828c` · PASS(v1) · Open 0(backend) · ★ **v1.2.1 merge FULLY UNBLOCKED**(backend)**:
> 331차 이후 develop delta **없음** — `5e1828c`(`test(v2/US-M03): harden copay guardian notify/payment response assertions`) 유지.
> `src/backend-test` `mvn test` **246/246 PASS**(64 suites, ~15s). develop **98커밋 ahead** — merge gate **FULLY UNBLOCKED**(backend). 교차(frontend git): `@869a6fd`(+1 vs `0adf8c6`: ds-billing-nhis-comparison CSS) WT **CLEAN** · 123 ahead · merge pending **221**.

> **331차 재검증 (12:42 UTC) — test `@598d108` CLEAN·origin/test 동기화·246/246 PASS·npm N/A(no package.json)·develop `@5e1828c`(+1 vs 329차 `fea28b8`: `test(v2/US-M03): harden copay guardian notify/payment response assertions` — `CopayGuardianNotifyPaymentE2eTest`, 1 file +10/-3) **WT CLEAN** · HEAD **576/576 PASS**(113 suites) · 98 ahead · origin/develop @ `5e1828c` · PASS(v1) · **QA-20260611-B41 Fixed** · Open 0(backend) · ★ **v1.2.1 merge FULLY UNBLOCKED**(backend)**:
> develop HEAD **`5e1828c`**(+1: v2/US-M03·G2 copay guardian notify/payment receipt response metadata assertion hardening — `notifyClaimGuardians`·`recordCopayPayment`·`notifyPaymentReceipt` claimId·dispatchedCount·status·paymentMethod·paidAt 계약 검증).
> `src/backend-test` `mvn test` **246/246 PASS**(64 suites). develop **98커밋 ahead** — v1.2.1 merge gate **FULLY UNBLOCKED**(backend). 교차(frontend 330차): Open 0 · FE `@b58429d` WT **CLEAN** · 635/635 PASS · 121 ahead · **양 스트림 merge gate FULLY UNBLOCKED** · merge pending **219**.

> **329차 재검증 (12:18 UTC) — test `@598d108` CLEAN·origin/test 동기화·246/246 PASS·npm N/A(no package.json)·develop `@fea28b8` HEAD **불변**·WT **DIRTY 1M**(`CopayGuardianNotifyPaymentE2eTest.java`+10/-3 — v2/US-M03·G2 billing notify response assertion WIP, **327차 CLEAN→재오염**) · HEAD **576/576 PASS**·WT **576/576 PASS**(@Test 수 불변) · 97 ahead · origin/develop @ `fea28b8` · PASS(v1) · **Open 1 BLOCK QA-B41(backend)** · ⚠ **v1.2.1 merge BLOCK**(backend)**:
> develop HEAD **`fea28b8`**(327차 대비 **불변**). WT modified **`CopayGuardianNotifyPaymentE2eTest.java`**(+10/-3) — `notifyClaimGuardians`·`recordCopayPayment`·`notifyPaymentReceipt` response metadata assertion hardening (claimId·dispatchedCount·status·paymentMethod·paidAt).
> `src/backend-test` `mvn test` **246/246 PASS**(64 suites). develop **97커밋 ahead** — v1.2.1 merge gate **BLOCK**(WT dirty). 교차(frontend 328차): Open 0 · FE `@7f8bdc7` WT **CLEAN** · 634/634 PASS · 120 ahead · **양 스트림 merge BLOCK**(BE WT clean 선행) · merge pending **217**.

> **327차 재검증 (12:00 UTC) — test `@598d108` CLEAN·origin/test 동기화·246/246 PASS·npm N/A(no package.json)·develop `@fea28b8`(+1 vs 325차 `2225a7a`: `fix(v2/G32): validate case management quarter query bounds` — `CaseManagementService`·`CaseManagementServiceTest`, 2 files +13/-4) **WT CLEAN** · HEAD **576/576 PASS**(113 suites) · 97 ahead · origin/develop @ `fea28b8` · PASS(v1) · Open 0(backend) · ★ **v1.2.1 merge FULLY UNBLOCKED**(backend)**:
> develop HEAD **`fea28b8`**(+1: G32 case management meeting list quarter 파라미터 범위 검증 — compliance API 규칙 정합·무효 필터 방지, 575→576 +1 @Test).
> `src/backend-test` `mvn test` **246/246 PASS**(64 suites). develop **97커밋 ahead** — v1.2.1 merge gate **FULLY UNBLOCKED**(backend). 교차(frontend 326차): Open 0 · FE `@0821ce8` WT **CLEAN** · 631/631 PASS · 119 ahead · **양 스트림 merge gate FULLY UNBLOCKED** · merge pending **216**.

> **325차 재검증 (11:35 UTC) — test `@598d108` CLEAN·origin/test 동기화·246/246 PASS·npm N/A(no package.json)·develop `@2225a7a`(+1 vs 323차 `622b5e5`: `feat(v2): add NHIS claim comparison API and normalize G32 attendee names` — `BillingController`·`BillingService`·`CaseManagementService`·`BillingClaimNhisComparisonResponse`·tests·routing/RBAC, 9 files +468/-8) **WT CLEAN** · HEAD **575/575 PASS**(113 suites) · 96 ahead · origin/develop @ `2225a7a` · PASS(v1) · Open 0(backend) · ★ **v1.2.1 merge FULLY UNBLOCKED**(backend)**:
> develop HEAD **`2225a7a`**(+1: v2 NHIS claim comparison GET `/api/v1/billing/claims/{id}/nhis-comparison` — BNK-87 pre-confirm copay reconciliation · G32 `CaseManagementService` attendee_names normalize on persist, 569→575 +6 @Test).
> `src/backend-test` `mvn test` **246/246 PASS**(64 suites). develop **96커밋 ahead** — v1.2.1 merge gate **FULLY UNBLOCKED**(backend). 교차(frontend 324차): Open 0 · FE `@7eebd8c` WT **CLEAN** · 627/627 PASS · 118 ahead · **양 스트림 merge gate FULLY UNBLOCKED** · merge pending **214**.

> **323차 재검증 (11:08 UTC) — test `@598d108` CLEAN·origin/test 동기화·246/246 PASS·npm N/A(no package.json)·develop `@622b5e5`(+1 vs 321차 `55fae99`: `feat(dba): add V74 integrity constraints for V71/V72/V73` — `V74__v71_v72_v73_integrity.sql`+211) **WT CLEAN** · HEAD **569/569 PASS**(113 suites) · 95 ahead · origin/develop @ `622b5e5` · PASS(v1) · **QA-20260611-B39 Fixed** · Open 0(backend) · ★ **v1.2.1 merge FULLY UNBLOCKED**(backend)**:
> develop HEAD **`622b5e5`**(+1: DBA V74 integrity constraints — billing_claims refund CHECK/trigger·functional_recovery_plans org/branch sync·case_management_meetings integrity, V71·V72·V73 follow-up).
> `src/backend-test` `mvn test` **246/246 PASS**(64 suites). develop **95커밋 ahead** — v1.2.1 merge gate **FULLY UNBLOCKED**(backend). 교차(frontend 322차): Open 1 BLOCK QA-B40 · FE `@c288fdd` WT **DIRTY 2M** · 117 ahead · **양 스트림 merge BLOCK**(FE WT clean 선행) · merge pending **212**.

> **321차 재검증 (10:39 UTC) — test `@598d108` CLEAN·origin/test 동기화·246/246 PASS·npm N/A(no package.json)·develop `@55fae99` HEAD **불변**·WT **DIRTY 1U**(`V74__v71_v72_v73_integrity.sql`+211 — DBA V71/V72/V73 integrity follow-up WIP, **319차 CLEAN→재오염**) · HEAD **569/569 PASS**(113 suites) · 94 ahead · origin/develop @ `55fae99` · PASS(v1) · **Open 1 BLOCK QA-B39(backend)** · ⚠ **v1.2.1 merge BLOCK**(backend)**:
> develop HEAD **`55fae99`**(319차 대비 **불변**). WT untracked **`V74__v71_v72_v73_integrity.sql`**(211 lines) — billing_claims refund CHECK/trigger·functional_recovery_plans org/branch sync·case_management_meetings integrity (V71·V72·V73 follow-up).
> `src/backend-test` `mvn test` **246/246 PASS**(64 suites). develop **94커밋 ahead** — v1.2.1 merge gate **BLOCK**(WT dirty). 교차(frontend 320차): Open 0 · FE `@c288fdd`(+1 G17/G32 FE pages) WT **CLEAN** · 117 ahead · **양 스트림 merge BLOCK**(BE WT clean 선행) · merge pending **211**.

> **319차 재검증 (09:56 UTC) — test `@598d108` CLEAN·origin/test 동기화·246/246 PASS·npm N/A(no package.json)·develop `@55fae99`(+1 vs 317차 `73e169a`: `feat(v2/G32): add case management meeting API (indicator 43)` — `CaseManagementController`·`CaseManagementService`·V73·`CaseManagementServiceTest`·routing/RBAC, 16 files +1250) **WT CLEAN** · **569/569 PASS**(113 suites) · 94 ahead · origin/develop @ `55fae99` · PASS(v1) · Open 0(backend) · ★ **v1.2.1 merge FULLY UNBLOCKED**(backend)**:
> develop HEAD **`55fae99`**(+1: G32 case management meeting CRUD + compliance API — `CaseManagementController`·`CaseManagementService`·`CaseManagementMeetingEntity`·V73·`CaseManagementServiceTest`·routing/RBAC, 559→569 +10 @Test).
> `src/backend-test` `mvn test` **246/246 PASS**(64 suites). develop **94커밋 ahead** — v1.2.1 merge gate **FULLY UNBLOCKED**(backend). 교차(frontend 318차): Open 0 · FE `@212e010` WT **CLEAN** · 614/614 PASS · 115 ahead · **양 스트림 merge gate FULLY UNBLOCKED** · merge pending **209**.

> **317차 재검증 (09:26 UTC) — test `@598d108` CLEAN·origin/test 동기화·246/246 PASS·npm N/A(no package.json)·develop `@73e169a`(+1 vs 315차 `0af6526`: `feat(v2/G17): add functional recovery plan API and program type (US-T06)` — `FunctionalRecoveryController`·`FunctionalRecoveryService`·`ProgramType`·V72·tests·routing/RBAC, 22 files +1066) **WT CLEAN** · **559/559 PASS**(110 suites) · 93 ahead · origin/develop @ `73e169a` · PASS(v1) · Open 0(backend) · ★ **v1.2.1 merge FULLY UNBLOCKED**(backend)**:
> develop HEAD **`73e169a`**(+1: G17 functional recovery plan CRUD + compliance API + `ProgramType.FUNCTIONAL_RECOVERY` — `FunctionalRecoveryController`·`FunctionalRecoveryService`·`FunctionalRecoveryPlanEntity`·V72·`FunctionalRecoveryServiceTest`·routing/RBAC, 550→559 +9 @Test).
> `src/backend-test` `mvn test` **246/246 PASS**(64 suites). develop **93커밋 ahead** — v1.2.1 merge gate **FULLY UNBLOCKED**(backend). 교차(frontend 316차): Open 0 · FE `@b92a1d4` WT **CLEAN** · 610/610 PASS · 114 ahead · **양 스트림 merge gate FULLY UNBLOCKED** · merge pending **207**.

> **315차 재검증 (09:02 UTC) — test `@598d108` CLEAN·origin/test 동기화·246/246 PASS·npm N/A(no package.json)·develop `@0af6526`(+1 vs 313차 `de49b21`: `feat(v2/US-M03): expose copay refund metadata in billing API responses` — `BillingClaimResponse`·`ClientBillingHistoryItemResponse`·`BillingService`·`BillingServiceTest`·`CopayGuardianNotifyPaymentE2eTest`·routing/RBAC, 7 files +197) **WT CLEAN** · **550/550 PASS**(107 suites) · 92 ahead · origin/develop @ `0af6526` · PASS(v1) · Open 0(backend) · ★ **v1.2.1 merge FULLY UNBLOCKED**(backend)**:
> develop HEAD **`0af6526`**(+1: US-M03 copay refund metadata in billing claim/history responses — `BillingClaimResponse.refundAmount`·`ClientBillingHistoryItemResponse` refund fields·`BillingService` mapping·`BillingServiceTest` refund metadata regression·`CopayGuardianNotifyPaymentE2eTest`·routing/RBAC, 548→550 +2 @Test).
> `src/backend-test` `mvn test` **246/246 PASS**(64 suites). develop **92커밋 ahead** — v1.2.1 merge gate **FULLY UNBLOCKED**(backend). 교차(frontend 314차): Open 1 BLOCK QA-B38 · FE `@c30aaac` WT **DIRTY 1M** · 113 ahead · **양 스트림 merge BLOCK**(FE WT clean 선행) · merge pending **205**.

> **313차 재검증 (08:35 UTC) — test `@598d108` CLEAN·origin/test 동기화·246/246 PASS·npm N/A(no package.json)·develop `@de49b21`(+1 vs 311차 `22d82e2`: `feat(v2/US-M03): add copay refund API and refunds ledger report (7-9)` — `BillingController`·`RecordCopayRefundRequest`·`BillingService`·`BillingClaimEntity`·V71·tests·routing/RBAC, 10 files +546/-7) **WT CLEAN** · **548/548 PASS**(107 suites) · 91 ahead · origin/develop @ `de49b21` · PASS(v1) · Open 0(backend) · ★ **v1.2.1 merge FULLY UNBLOCKED**(backend)**:
> develop HEAD **`de49b21`**(+1: US-M03 copay refund POST API + refunds ledger report variant — `BillingController.recordCopayRefund()`·`RecordCopayRefundRequest`·`BillingService` refund logic·`BillingClaimEntity` refund metadata·`V71__billing_copay_refund_metadata.sql`·`BillingServiceTest`·routing/RBAC tests, 542→548 +6 @Test).
> `src/backend-test` `mvn test` **246/246 PASS**(64 suites). develop **91커밋 ahead** — v1.2.1 merge gate **FULLY UNBLOCKED**(backend). 교차(frontend 312차): Open 0 · FE `@c30aaac` WT **CLEAN** · 607/607 PASS · 113 ahead · **양 스트림 merge gate FULLY UNBLOCKED** · merge pending **204**.

> **311차 재검증 (08:08 UTC) — test `@598d108` CLEAN·origin/test 동기화·246/246 PASS·npm N/A(no package.json)·develop `@22d82e2`(+1 vs 309차 `8f208e4`: `feat(v2/US-M03): add billing ledger report API for charges, deposits, receipts` — `BillingController`·`BillingReport*Response` DTO 3종·`BillingService`·`BillingClaimRepository`·tests·routing/RBAC, 9 files +543) **WT CLEAN** · **542/542 PASS**(107 suites) · 90 ahead · origin/develop @ `22d82e2` · PASS(v1) · Open 0(backend) · ★ **v1.2.1 merge FULLY UNBLOCKED**(backend)**:
> develop HEAD **`22d82e2`**(+1: US-M03 billing ledger report GET `/api/v1/billing/reports/{variant}` — charges/deposits/receipts variants · `BillingController`·`BillingReportItemResponse`·`BillingReportListResponse`·`BillingReportSummaryResponse`·`BillingService` ledger query·`BillingClaimRepository`·`BillingServiceTest`·routing/RBAC tests, 537→542 +5 @Test).
> `src/backend-test` `mvn test` **246/246 PASS**(64 suites). develop **90커밋 ahead** — v1.2.1 merge gate **FULLY UNBLOCKED**(backend). 교차(frontend 310차): Open 0 · FE `@dd163cf` WT **CLEAN** · 606/606 PASS · 112 ahead · **양 스트림 merge gate FULLY UNBLOCKED**.

> **309차 재검증 (07:40 UTC) — test `@598d108` CLEAN·origin/test 동기화·246/246 PASS·npm N/A(no package.json)·develop `@8f208e4`(+1 vs 307차 `970c7af`: `feat(v2/US-G04): add fee schedule year coverage pre-check API` — `BillingController`·`FeeScheduleYearCoverageResponse`·`BillingService`·tests·routing/RBAC, 6 files +154/-2) **WT CLEAN** · **537/537 PASS**(107 suites) · 89 ahead · origin/develop @ `8f208e4` · PASS(v1) · Open 0(backend) · ★ **v1.2.1 merge FULLY UNBLOCKED**(backend)**:
> develop HEAD **`8f208e4`**(+1: US-G04 fee schedule year coverage pre-check GET API — `BillingController.getFeeScheduleYearCoverage()`·`FeeScheduleYearCoverageResponse`·`BillingService` coverage query·`BillingServiceTest`·`MustApiEndpointRoutingTest`·`RoleBasedControllerAccessTest`, 532→537 +5 @Test).
> `src/backend-test` `mvn test` **246/246 PASS**(64 suites). develop **89커밋 ahead** — v1.2.1 merge gate **FULLY UNBLOCKED**(backend). 교차(frontend 308차): QA-B37 **Planned** · FE `@5c0d83d` WT **DIRTY 2M** · 110 ahead · **양 스트림 merge BLOCK**(FE WT clean 선행).

> **307차 재검증 (07:00 UTC) — test `@598d108` CLEAN·origin/test 동기화·246/246 PASS·npm N/A(no package.json)·develop `@970c7af`(+1 vs 305차 `0ae5f8d`: `fix(v2/US-G04): reject NHIS import when fee schedule year grid is incomplete` — `FeeScheduleYearCoverage`·`NhisImportService`·tests, 4 files +233) **WT CLEAN** · **532/532 PASS**(107 suites) · 88 ahead · origin/develop @ `970c7af` · PASS(v1) · Open 0(backend) · ★ **v1.2.1 merge FULLY UNBLOCKED**(backend)**:
> develop HEAD **`970c7af`**(+1: US-G04 NHIS import fee schedule year grid completeness guard — `FeeScheduleYearCoverage` 25-cell grade×duration-band coverage·`NhisImportService` pre-import validation·`FeeScheduleYearCoverageTest`·`NhisImportServiceTest` +4 @Test).
> `src/backend-test` `mvn test` **246/246 PASS**(64 suites). develop **88커밋 ahead** — v1.2.1 merge gate **FULLY UNBLOCKED**(backend). 교차(frontend 306차): Open 0 · FE `@5c0d83d` WT **CLEAN** · 601/601 PASS · 110 ahead · **양 스트림 merge gate FULLY UNBLOCKED**.

> **305차 재검증 (06:32 UTC) — test `@598d108` CLEAN·origin/test 동기화·246/246 PASS·npm N/A(no package.json)·develop `@0ae5f8d`(+1 vs 303차 `aacf20b`: `fix(v2/G21): guard duplicate paired PLAN/BILLING visit slots on create/update/import` — `VisitService`·`VisitServiceTest`, 2 files +214) **WT CLEAN** · **528/528 PASS**(106 suites) · 87 ahead · origin/develop @ `0ae5f8d` · PASS(v1) · **QA-20260611-B36 Fixed** · Open 0(backend) · ★ **v1.2.1 merge FULLY UNBLOCKED**(backend)**:
> develop HEAD **`0ae5f8d`**(+1: G21 paired PLAN/BILLING duplicate visit-slot guard on create/update/NHIS import — `VisitService.ensureNoDuplicateVisitSlot`·`hasExistingVisitSchedule`(+45) · `VisitServiceTest` 회귀(+169, +3 @Test)).
> `src/backend-test` `mvn test` **246/246 PASS**(64 suites). develop **87커밋 ahead** — v1.2.1 merge gate **FULLY UNBLOCKED**(backend). 교차(frontend 304차): Open 0 · FE `@b9845ac` WT **CLEAN** · 595/595 PASS · 109 ahead · **양 스트림 merge gate FULLY UNBLOCKED**.

> **303차 재검증 (06:13 UTC) — test `@598d108` CLEAN·origin/test 동기화·246/246 PASS·npm N/A(no package.json)·develop `@aacf20b` HEAD **불변**·WT **DIRTY 2M**(`VisitService.java`+45 · `VisitServiceTest.java`+169 — v2/G21 paired PLAN/BILLING duplicate visit-slot guard WIP, **301차 CLEAN→재오염**)·HEAD **525/525 PASS**·WT **528/528 PASS**(+3 @Test, 106 suites)·86 ahead·origin/develop @ `aacf20b`·PASS(v1)·Open 1 BLOCK QA-B36(backend)·⚠ **v1.2.1 merge BLOCK**(backend)**:
> develop HEAD **`aacf20b`**(**불변** — 301차 G21 paired PLAN/BILLING confirm committed).
> WIP(uncommitted): `VisitService.ensureNoDuplicateVisitSlot`·`hasExistingVisitSchedule` paired PLAN/BILLING duplicate slot guard on create/update/NHIS import(+45) · `VisitServiceTest` 회귀(+169, +3 @Test).
> `src/backend-test` `mvn test` **246/246 PASS**(64 suites). develop **86커밋 ahead** — v1.2.1 merge gate **BLOCK**(backend). 교차(frontend 302차): Open 0 · FE `@758e590` WT **CLEAN** · 593/593 PASS · 108 ahead · **양 스트림 merge BLOCK**(BE WT clean 선행).

> **301차 재검증 (05:51 UTC) — test `@598d108` CLEAN·origin/test 동기화·246/246 PASS·npm N/A(no package.json)·develop `@aacf20b`(+1 vs `ff12473`: `fix(v2/G21): confirm paired PLAN/BILLING schedules together` — `VisitService`·`VisitPilotServiceFlowE2eTest`·`VisitServiceTest`, 3 files +101) **WT CLEAN** · **525/525 PASS** · 86 ahead · origin/develop @ `aacf20b` · PASS(v1) · Open 0(backend) · ★ **v1.2.1 merge FULLY UNBLOCKED**(backend)**:
> develop HEAD **`aacf20b`**(+1: G21 paired PLAN/BILLING 일정 동시 확정 guard — `VisitService` 확정 플로우 + `VisitPilotServiceFlowE2eTest`·`VisitServiceTest` 회귀 강화, 3 files +101/-0).
> `src/backend-test` `mvn test` **246/246 PASS**(64 suites). develop **86커밋 ahead** — v1.2.1 merge gate **FULLY UNBLOCKED**(backend). 교차(frontend 300차): Open 0 · FE `@fd569d7` WT **CLEAN** · 580/580 PASS · 107 ahead · **양 스트림 merge gate FULLY UNBLOCKED**.

> **299차 재검증 (05:45 UTC) — test `@598d108` CLEAN·origin/test 동기화·246/246 PASS·npm N/A(no package.json)·develop `@ff12473`(+1 vs `923e610`: `fix(v2/G21): block duplicate visit slots in visit schedules` — `VisitService`·`VisitScheduleRepository`·`VisitServiceTest`, 3 files +176) **WT CLEAN** · **523/523 PASS**(106 suites) · 85 ahead · origin/develop @ `ff12473` · PASS(v1) · Open 0(backend) · ★ **v1.2.1 merge FULLY UNBLOCKED**(backend)**:
> develop HEAD **`ff12473`**(+1: G21 duplicate visit slot guard — `VisitService` slot overlap validation·`VisitScheduleRepository` duplicate lookup·`VisitServiceTest` +2 @Test).
> `src/backend-test` `mvn test` **246/246 PASS**(64 suites). develop **85커밋 ahead** — v1.2.1 merge gate **FULLY UNBLOCKED**(backend). 교차(frontend 298차): Open 0 · FE `@e2c2ffe` WT **CLEAN** · 579/579 PASS · 106 ahead · **양 스트림 merge gate FULLY UNBLOCKED**.

> **297차 재검증 (04:57 UTC) — test `@598d108` CLEAN·origin/test 동기화·246/246 PASS·npm N/A(no package.json)·develop `@923e610`(+1 vs `1af5b1f`: `fix(v2/G2): reject PAID status when claim copayAmount is null` — `BillingService`·`BillingServiceTest`·`J03AlimtalkServiceFlowE2eTest`, 3 files +58) **WT CLEAN** · **521/521 PASS**(106 suites) · 84 ahead · origin/develop @ `923e610` · PASS(v1) · Open 0(backend) · ★ **v1.2.1 merge FULLY UNBLOCKED**(backend)**:
> develop HEAD **`923e610`**(+1: G2 PAID status null `copayAmount` guard — `updateClaimStatus()` BusinessRuleException·`updateClaimStatusShouldRejectPaidWhenCopayAmountMissing` +1 @Test·J03 E2E fixture +1).
> `src/backend-test` `mvn test` **246/246 PASS**(64 suites). develop **84커밋 ahead** — v1.2.1 merge gate **FULLY UNBLOCKED**(backend). 교차(frontend 296차): Open 0 · FE `@c1d9788` WT **CLEAN** · 574/574 PASS · 104 ahead · **양 스트림 merge gate FULLY UNBLOCKED**.

> **295차 재검증 (04:25 UTC) — test `@598d108` CLEAN·origin/test 동기화·246/246 PASS·npm N/A(no package.json)·develop `@1af5b1f`(+1 vs `970f547`: `fix(v2/G2): reject copay payment when claim copayAmount is null` — `BillingService`·`BillingServiceTest`, 2 files +64) **WT CLEAN** · **520/520 PASS**(106 suites) · 83 ahead · origin/develop @ `1af5b1f` · PASS(v1) · **QA-20260611-B35 Fixed** · Open 0(backend) · ★ **v1.2.1 merge FULLY UNBLOCKED**(backend)**:
> develop HEAD **`1af5b1f`**(+1: G2 copay payment null `copayAmount` guard — `recordCopayPayment()` BusinessRuleException·`recordCopayPaymentShouldRejectMissingCopayAmountOnClaim` +1 @Test).
> `src/backend-test` `mvn test` **246/246 PASS**(64 suites). develop **83커밋 ahead** — v1.2.1 merge gate **FULLY UNBLOCKED**(backend). 교차(frontend 294차): Open 0 · FE `@be1bdd0` WT **CLEAN** · 570/570 PASS · 103 ahead · **양 스트림 merge gate FULLY UNBLOCKED**.

> **293차 재검증 (04:10 UTC) — test `@598d108` CLEAN·origin/test 동기화·246/246 PASS·npm N/A(no package.json)·develop `@970f547` HEAD **불변**·WT **DIRTY 2M**(`BillingService.java`+3·`BillingServiceTest.java`+61 — v2/G2 `recordCopayPayment()` null `copayAmount` guard WIP, **291차 CLEAN→재오염**)·HEAD **519/519 PASS**·WT **520/520 PASS**(+1 @Test, 106 suites)·82 ahead·origin/develop @ `970f547`·PASS(v1)·Open 1 BLOCK QA-B35(backend)·⚠ **v1.2.1 merge BLOCK**(backend)**:
> develop HEAD **`970f547`**(**불변** — 291차 G26 CMS·easy-pay deduction exclude committed).
> WIP(uncommitted): `BillingService.recordCopayPayment()` null `copayAmount` → `BusinessRuleException`(+3) · `recordCopayPaymentShouldRejectMissingCopayAmountOnClaim`(+61, +1 @Test).
> `src/backend-test` `mvn test` **246/246 PASS**(64 suites). develop **82커밋 ahead** — v1.2.1 merge gate **BLOCK**(backend). 교차(frontend 292차): Open 0 · FE `@13272bc` WT **CLEAN** · 569/569 PASS · 102 ahead · **양 스트림 merge BLOCK**(BE WT clean 선행).

## 스냅샷

| 항목 | develop | test |
|------|---------|------|
| HEAD | `0af6526` | `598d108` |
| working tree | **CLEAN** | **CLEAN** |
| `mvn test` | **550/550 PASS** (HEAD) | 246/246 |
| ahead of test | 92 | — |
| origin sync | origin/develop @ `0af6526` | origin/test @ `598d108` |
| merge gate | **UNBLOCKED** | PASS(v1 baseline) |

## WIP (develop — 315차, 없음)

_(develop WT CLEAN · US-M03 copay refund metadata exposure @ `0af6526` committed)_

## 최신 커밋 (develop — 315차)

| 커밋 | 변경 |
|------|------|
| `0af6526` | `billing/api/BillingClaimResponse.java` +3 — refund metadata fields |
| `0af6526` | `billing/api/ClientBillingHistoryItemResponse.java` +2 — refund metadata in history |
| `0af6526` | `billing/domain/BillingService.java` +5 — refund amount mapping |
| `0af6526` | `billing/domain/BillingServiceTest.java` +150 — refund metadata regression (+2 @Test total) |
| `0af6526` | `billing/domain/CopayGuardianNotifyPaymentE2eTest.java` +28 — refund E2E coverage |
| `0af6526` | `routing/MustApiEndpointRoutingTest.java` +6 — route assertions |
| `0af6526` | `security/RoleBasedControllerAccessTest.java` +3 — RBAC coverage |

## 이전 스냅샷 (313차)

| HEAD | `de49b21` | `598d108` |
| working tree | **CLEAN** | **CLEAN** |
| `mvn test` | **548/548 PASS** (HEAD) | 246/246 |
| ahead of test | 91 | — |
| origin sync | origin/develop @ `de49b21` | origin/test @ `598d108` |
| merge gate | **UNBLOCKED** | PASS(v1 baseline) |

## WIP (develop — 313차, 없음)

_(develop WT CLEAN · US-M03 copay refund API @ `de49b21` committed)_

## 최신 커밋 (develop — 313차)

| 커밋 | 변경 |
|------|------|
| `de49b21` | `billing/api/BillingController.java` +24 — POST copay refund + refunds ledger report |
| `de49b21` | `billing/api/RecordCopayRefundRequest.java` +new — refund request DTO |
| `de49b21` | `billing/domain/BillingService.java` +refund logic — copay refund recording |
| `de49b21` | `billing/persistence/BillingClaimEntity.java` +refund fields |
| `de49b21` | `db/migration/V71__billing_copay_refund_metadata.sql` +new |
| `de49b21` | `billing/domain/BillingServiceTest.java` +tests — refund API regression (+6 @Test total) |

## 이전 스냅샷 (311차)

| 커밋 | 변경 |
|------|------|
| `8f208e4` | `billing/api/BillingController.java` +12 — GET fee schedule year coverage pre-check |
| `8f208e4` | `billing/api/FeeScheduleYearCoverageResponse.java` +13 — coverage response DTO |
| `8f208e4` | `billing/domain/BillingService.java` +31 — year coverage query logic |
| `8f208e4` | `billing/domain/BillingServiceTest.java` +69 — pre-check API regression (+5 @Test total) |
| `8f208e4` | `routing/MustApiEndpointRoutingTest.java` +11 — route coverage |
| `8f208e4` | `security/RoleBasedControllerAccessTest.java` +20 — RBAC coverage |

## 이전 스냅샷 (307차)

| 커밋 | 변경 |
|------|------|
| `970c7af` | `billing/domain/FeeScheduleYearCoverage.java` +75 — 25-cell grade×duration-band year coverage |
| `970c7af` | `billing/domain/NhisImportService.java` +14 — pre-import fee schedule year grid validation |
| `970c7af` | `billing/domain/FeeScheduleYearCoverageTest.java` +61 — coverage unit tests |
| `970c7af` | `billing/domain/NhisImportServiceTest.java` +83 — import guard regression (+4 @Test total) |

## 최신 커밋 (develop — 305차)

| 커밋 | 변경 |
|------|------|
| `0ae5f8d` | `visits/domain/VisitService.java` +45 — paired PLAN/BILLING duplicate visit-slot guard on create/update/import |
| `0ae5f8d` | `visits/domain/VisitServiceTest.java` +169 — 회귀 테스트 (+3 @Test) |

## 최신 커밋 (develop — 301차)

| 커밋 | 변경 |
|------|------|
| `aacf20b` | `visits/domain/VisitService.java` +61 — confirm paired PLAN/BILLING schedule status updates |
| `aacf20b` | `visits/domain/VisitPilotServiceFlowE2eTest.java` +18 — paired PLAN/BILLING confirm flow E2E regression |
| `aacf20b` | `visits/domain/VisitServiceTest.java` +22 — paired confirm 회귀 테스트 보강 |

## 최신 커밋 (develop — 297차)

| 커밋 | 변경 |
|------|------|
| `923e610` | `billing/domain/BillingService.java` +3 — `updateClaimStatus()` PAID null `copayAmount` guard |
| `923e610` | `billing/domain/BillingServiceTest.java` +54 — `updateClaimStatusShouldRejectPaidWhenCopayAmountMissing` 회귀 테스트 |
| `923e610` | `domain/J03AlimtalkServiceFlowE2eTest.java` +1 — E2E fixture 보강 |

## 최신 커밋 (develop HEAD — 295차)

| 커밋 | 변경 |
|------|------|
| `1af5b1f` | `billing/domain/BillingService.java` +3 — `recordCopayPayment()` null `copayAmount` guard |
| `1af5b1f` | `billing/domain/BillingServiceTest.java` +61 — `recordCopayPaymentShouldRejectMissingCopayAmountOnClaim` 회귀 테스트 |

## 최신 커밋 (develop HEAD — 291차)

| 파일 | 변경 |
|------|------|
| `billing/domain/BillingService.java` | +16/-3 — G26 medical expense deduction: CMS·easy-pay 결제 수단 제외 |
| `billing/domain/BillingServiceTest.java` | +120 — CMS·easy-pay exclusion 회귀 테스트 |

## 이전 커밋 (develop only — 289차)

| 파일 | 변경 |
|------|------|
| `billing/cms/domain/CmsService.java` | +26/-4 — CMS SUCCEEDED debit claim integrity validation (claim status·amount·provider result cross-check) |
| `billing/cms/domain/CmsServiceTest.java` | +50 — CMS SUCCEEDED debit integrity 회귀 테스트 |

## 이전 커밋 (develop only — 287차)

| 파일 | 변경 |
|------|------|
| `billing/cms/domain/CmsService.java` | +10 — CMS debit amount integrity guard (non-positive rejection·amount mismatch fail) |
| `billing/cms/domain/CmsServiceTest.java` | +40 — CMS debit integrity 회귀 테스트 |

## 이전 커밋 (develop only — 285차)

| 파일 | 변경 |
|------|------|
| `billing/domain/BillingService.java` | +121 — G26 medical expense deduction API |
| `billing/domain/BillingServiceTest.java` | +153 — medical expense deduction 회귀 테스트 |
| `client/ClientController.java` | +endpoint — client medical expense deduction 조회 |
| `guardian/GuardianCheckinController.java` | +endpoint — guardian medical expense deduction 조회 |
