<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-08T23:53:38+00:00 -->
# develop ↔ test diff 메타 (2026-06-08, 104차 — origin 동기화 @598d108 · develop v1.2.1 @2012945)

> **104차 재검증 (23:53 UTC) — test `@598d108` CLEAN·origin/test **동기화**·246/246 PASS·develop `2012945`(+1 v1.2.1) CLEAN·1 ahead·PASS(v1)·Open 0**:
> test·origin/test **`598d108`** 동기화(QA-B12 Fixed). test `mvn test` **246/246 PASS**(64 suites)·JAR **76,675,999 B**·Boot **3.3.1**·Flyway **V50**. develop HEAD **`2012945`**(+1 vs test — `feat(v1.2.1): add region master, branch profile, and billing integrity`: `regions/api/RegionController`·`regions/domain/RegionLookupService`·`V51__admin_regions_and_branch_profile.sql`·`V52__billing_payment_recorded_by_actor_integrity.sql`·`organizations/domain/BranchService` profile·27 files +742), WT **CLEAN**. develop `mvn test` **246/246 PASS**. develop **1커밋 ahead** — v1.2.1 develop-only·차기 merge. **신규 Open 0건**. **판정 PASS(v1 merged baseline)**.

> **102차 재검증 (16:13 UTC) — test `@598d108` CLEAN·develop HEAD `@598d108` DIRTY(13 WIP)·246/246 PASS·origin/test STALE 26 ahead·PASS(conditional)·Open 0**:
> 로컬 **develop·test HEAD 동기화** @ `598d108` (`feat(v2): add copay payment recording, overdue list, and guardian billing API` — V50·BillingServiceTest +198). test `mvn test` **246/246 PASS**(64 suites)·JAR **76,675,999 B**·Boot 3.3.1. v1 baseline + v1.3-A + v3 + V50 **test HEAD PRESENT** ✓. develop WT **DIRTY 13**(regions/V51/V52 WIP). **origin/test STALE** `2799e29` — **26 ahead·미푸시**(QA-B12 Planned). 판정 **PASS(conditional)**.

> **100차 재검증 (15:10 UTC) — ✅ develop→test MERGE 실행(로컬 worktree)·test `2799e29`→`32575aa`(25커밋 fast-forward)·test 243/243 PASS·develop `598d108`(+1 v2 copay payment)·246/246 PASS·신규 Open 1(QA-20260608-B12 HIGH)·판정 PASS(conditional)**:
> **MERGE 실행** — test HEAD **`2799e29`(79 tests, 23 suites) → `32575aa`(25커밋 fast-forward 머지)**, working tree **CLEAN**. 98차까지 단일 BLOCK 이던 develop→test merge 게이트가 **로컬 worktree 에서 해소**.
> 머지 후 test `mvn test` **243/243 PASS**(64 suites, surefire-reports 집계) — 98차 develop HEAD(`32575aa`) 243/243 과 **동일 산출물**(Flyway 49 migrations·V47/V48/V49 포함·Boot 3.3.1·JAR 76,466,058 B). `git cat-file -e test:` v1 baseline + BE-11 + V45/V46 + v2/J03 alimtalk + v1.3-A transport(API·V47·V48·geocode proxy·unconfirm·client profile·pilot service-flow E2E·pickup masking·masking 단위 테스트) + v3 meals/programs(V49) **전부 PRESENT** ✓.
> develop HEAD **`32575aa`→`598d108`**(+1커밋, 머지 이후 신규 — `feat(v2): add copay payment recording, overdue list, and guardian billing API`: `billing/api/RecordCopayPaymentRequest.java`·`billing/api/OverdueClaimListResponse.java`·`billing/domain/BillingService.java`·`db/migration/V50__billing_copay_payment_metadata.sql`·`billing/domain/BillingServiceTest.java`(+198), 13 files +507/-3), working tree **CLEAN**. develop `mvn test` **246/246 PASS**(64 suites, 243 → +3 BillingServiceTest copay payment).
> develop **1커밋 ahead** of test(`598d108`) — 차기 merge 사이클.
> **⚠ 신규 Open 1건 QA-20260608-B12(HIGH)**: 머지가 **로컬 worktree 한정** — `origin/test` 여전히 **`2799e29`(STALE)**·`git rev-list --count origin/test..HEAD` = **25**(미푸시). operation 승격은 origin 기준 → `git_merge_to_test.sh` 로 **origin/test push 필수**(재clone 시 머지 유실 위험·SEC-D14 origin 미반영·`.agents/rules.md` §6 push 누락 금지).
> **판정 PASS(conditional)** — merge(`32575aa`) 로컬 검증 완료·**merge 게이트 BLOCK 해소**. operation 승격 전 ① origin/test push(QA-B12) ② develop +1(`598d108`) 차기 merge 잔여. v1.3-A US-T02/T03 live E2E(post-merge)·v3 ROADMAP 버전 정의(planner) 잔여.

> **98차 재검증 (13:55 UTC) — develop `32575aa` CLEAN·v1.3-A transport pickup contact masking 단위 테스트 보강(SEC-D9 PII)·merge 25커밋·develop 243/243·test 79/79·Open 0·BLOCK(merge 게이트 단일)**:
> develop HEAD **`32575aa`**(+1커밋 vs 96차 `c7941e9` — `test(v1.3-A): add pickup contact masking unit tests for roster and run detail`: `transport/domain/TransportServiceTest.java`(+86 — hq_admin pickup 연락처 전체 노출 어서션·caregiver `getRun` 마스킹(`010-****-5678`) 어서션 추가·non-HQ PII 마스킹 회귀 안전망 강화, **test-only commit**), 1 file +86), working tree **CLEAN**.
> test HEAD **`2799e29`**(v1 초기 구현 baseline) — ROADMAP v1 merged 기대 **`e8750d2`** 와 **불일치**.
> test `mvn test` **79/79 PASS**(23 suites, Boot 3.3.1, JAR 76,466,058 B). develop HEAD `mvn test` **243/243 PASS**(64 suites, 96차 241 → +2: `TransportServiceTest` 8→10 @Test, 신규 production 코드 없음).
> develop **25커밋 ahead** — merge 미실행. **모든 v1 baseline + v1.3-A transport(unconfirm·client profile·pilot service-flow E2E·pickup address+contact masking + masking 단위 테스트 보강) + v3 meals/programs artifacts PRESENT @ 32575aa(TSR 98차 독립 검증 PASS)**.
> **v1.3-A transport privacy 회귀 보강** — non-HQ pickup 연락처 마스킹·hq_admin 전체 가시성·caregiver `getRun` 마스킹 단위 테스트로 SEC-D9 PII 보호(개인정보보호법) 커버리지 강화(merge 직전 회귀 안전망). US-T02·T03 live E2E 잔여(test 승격 후).
> **v3 develop-only** — ROADMAP v3 버전·merge 게이트 미정의(planner 정의 대기).

> **96차 재검증 (12:40 UTC) — develop `c7941e9` CLEAN·v1.3-A transport pickup contact masking(non-HQ)·merge 24커밋·develop 241/241·test 79/79·Open 0·BLOCK(merge 게이트 단일)**:
> develop HEAD **`c7941e9`**(+1커밋 vs 94차 `e7d4cf6` — `feat(transport): mask pickup contact for non-hq views`: `transport/domain/TransportService.java`(+21 — `maskPhone` 헬퍼·non-HQ 역할 roster·run detail 응답 pickup 연락처 마스킹 `010-****-5678`·HQ 가시성 유지)·`transport/domain/TransportGeocodeService.java`(+4 — `resolvePickupContactPlain`)·`transport/api/TransportRosterItemResponse.java`(+1 — pickupContact 필드)·`transport/api/TransportStopResponse.java`(+1 — pickupContact 필드)·`transport/domain/TransportServiceTest.java`(+2 — pickup contact 마스킹 어서션)·`transport/domain/TransportPilotServiceFlowE2eTest.java`(+4 — roster·confirmed run detail privacy 회귀), 6 files, +33), working tree **CLEAN**.
> test HEAD **`2799e29`**(v1 초기 구현 baseline) — ROADMAP v1 merged 기대 **`e8750d2`** 와 **불일치**.
> test `mvn test` **79/79 PASS**(23 suites, Boot 3.3.1, JAR 76,466,058 B). develop HEAD `mvn test` **241/241 PASS**(64 suites, 94차 241 불변 — 신규 @Test 없음·기존 테스트 마스킹 어서션 확장만).
> develop **24커밋 ahead** — merge 미실행. **모든 v1 baseline + v1.3-A transport(unconfirm·client profile·pilot service-flow E2E·pickup address+contact masking) + v3 meals/programs artifacts PRESENT @ c7941e9(TSR 96차 독립 검증 PASS)**.
> **v1.3-A transport privacy 완성** — non-HQ 역할 pickup **주소(e7d4cf6) + 연락처(c7941e9)** 마스킹 — PII 보호(개인정보보호법) 강화. API_SPEC·ROADMAP v1.3·DATA_RETENTION_POLICY 반영 planner 확인 권장. US-T02·T03 live E2E 잔여(test 승격 후).
> **v3 develop-only** — ROADMAP v3 버전·merge 게이트 미정의(planner 정의 대기).

> **94차 재검증 (11:32 UTC) — develop `e7d4cf6` CLEAN·v1.3-A transport pickup address masking(non-HQ)·merge 23커밋·develop 241/241·test 79/79·Open 0·BLOCK(merge 게이트 단일)**:
> develop HEAD **`e7d4cf6`**(+1커밋 vs 93차 `f8d1b02` — `feat(transport): mask pickup addresses for non-HQ transport views`: `TransportService.java`(+47/-10 — non-hq 역할 roster·run detail pickup 주소 마스킹·HQ 편집 흐름 유지)·`TransportPilotServiceFlowE2eTest.java`(+1 privacy 회귀)·`TransportServiceTest.java`(+38 pickup masking 단위 테스트), 3 files, +76/-10), working tree **CLEAN**.
> test HEAD **`2799e29`**(v1 초기 구현 baseline) — ROADMAP v1 merged 기대 **`e8750d2`** 와 **불일치**.
> test `mvn test` **79/79 PASS**(23 suites, Boot 3.3.1, JAR 76,466,058 B). develop HEAD `mvn test` **241/241 PASS**(64 suites, 93차 240 → +1: `TransportServiceTest` pickup masking).
> develop **23커밋 ahead** — merge 미실행. **모든 v1 baseline + v1.3-A transport(unconfirm·client profile·pilot service-flow E2E·pickup address masking) + v3 meals/programs artifacts PRESENT @ e7d4cf6(TSR 94차 독립 검증 PASS)**.
> **v1.3-A transport privacy** — non-HQ 역할 pickup 주소 마스킹 @ `e7d4cf6` — API_SPEC·ROADMAP v1.3 반영 planner 확인 권장. US-T02·T03 live E2E 잔여(test 승격 후).
> **v3 develop-only** — ROADMAP v3 버전·merge 게이트 미정의(planner 정의 대기).

> **93차 재검증 (10:20 UTC) — develop `f8d1b02` CLEAN·v1.3-A transport pilot service-flow E2E·RBAC coverage(US-T01~T03)·merge 22커밋·develop 240/240·test 79/79·Open 0·BLOCK(merge 게이트 단일)**:
> develop HEAD **`f8d1b02`**(+1커밋 vs 92차 `1ec538b` — `test(v1.3-A): add transport pilot service-flow E2E and RBAC coverage (US-T01~T03)`: `transport/domain/TransportPilotServiceFlowE2eTest.java`(+183 new — US-T01~T03 배차 서비스 흐름 E2E)·`pilot/PilotChecklistJwtE2eTest.java`(+32 — transport pilot 체크리스트 흐름)·`security/RoleBasedControllerAccessTest.java`(+125 — transport RBAC 커버리지), 3 files, +340, **test-only commit**), working tree **CLEAN**.
> test HEAD **`2799e29`**(v1 초기 구현 baseline) — ROADMAP v1 merged 기대 **`e8750d2`** 와 **불일치**.
> test `mvn test` **79/79 PASS**(23 suites, Boot 3.3.1, JAR 76,466,058 B). develop HEAD `mvn test` **240/240 PASS**(64 suites, 92차 231 → +9: `TransportPilotServiceFlowE2eTest` new·`PilotChecklistJwtE2eTest` +·`RoleBasedControllerAccessTest` transport RBAC +).
> develop **22커밋 ahead** — merge 미실행. **모든 v1 baseline + v1.3-A transport(unconfirm PATCH+POST·client transport profile US-T01·pilot service-flow E2E) + v3 meals/programs artifacts PRESENT @ f8d1b02(TSR 93차 독립 검증 PASS)**.
> **US-T01 backend 완료·US-T01~T03 service-flow E2E 커버리지 추가** — frontend roster 구성 가능. US-T02·T03 live E2E 잔여(test 승격 후).
> **v3 develop-only** — ROADMAP v3 버전·merge 게이트 미정의(planner 정의 대기).

> **92차 재검증 (09:00 UTC) — develop `1ec538b` CLEAN·v1.3-A client transport profile(US-T01)·merge 21커밋·develop 231/231·test 79/79·Open 0·BLOCK(merge 게이트 단일)**:
> develop HEAD **`1ec538b`**(+1커밋 vs 91차 `767d977` — `feat(v1.3-A): expose client transport profile on Clients API (US-T01)`: `ClientResponse.java`(+5 — usesTransport·pickup address/contact·defaultPickupTime 필드)·`CreateClientRequest.java`(+7 — transport profile 입력)·`UpdateClientRequest.java`(+7 — transport profile 수정)·`ClientService.java`(+52 — transport profile 처리·pickup geocode 캐시 무효화)·`ClientServiceTest.java`(+176 — transport profile 9 @Test·기존 7→9)·`PilotChecklistJwtE2eTest.java`(+45 — transport roster·run detail endpoint 라우팅 smoke test), 6 files, +286/-6), working tree **CLEAN**.
> test HEAD **`2799e29`**(v1 초기 구현 baseline) — ROADMAP v1 merged 기대 **`e8750d2`** 와 **불일치**.
> test `mvn test` **79/79 PASS**(23 suites, Boot 3.3.1, JAR 76,466,058 B). develop HEAD `mvn test` **231/231 PASS**(62 suites, 91차 226 → +5: `ClientServiceTest` transport profile +2·`PilotChecklistJwtE2eTest` transport routing +3).
> develop **21커밋 ahead** — merge 미실행. **모든 v1 baseline + v1.3-A transport(unconfirm PATCH+POST·client transport profile US-T01) + v3 meals/programs artifacts PRESENT @ 1ec538b(TSR 92차 독립 검증 PASS)**.
> **US-T01 backend 완료**: Clients API 에 transport profile 노출(usesTransport·pickup address/contact·defaultPickupTime) — frontend roster 구성 가능. US-T02·T03 live E2E 잔여(frontend unconfirm UI 연동·test 승격 후).
> **v3 develop-only** — ROADMAP v3 버전·merge 게이트 미정의(planner 정의 대기).

> **91차 재검증 (08:00 UTC) — develop `767d977` 불변·CLEAN·merge 20커밋·develop 226/226·test 79/79·Open 0·BLOCK(merge 게이트 단일)**:

> **91차 재검증 (08:00 UTC) — develop `767d977` 불변·CLEAN·merge 20커밋·develop 226/226·test 79/79·Open 0·BLOCK(merge 게이트 단일)**:
> develop HEAD **`767d977`**(89차 대비 **불변** — v1.3-A transport unconfirm PATCH contract + POST legacy alias), working tree **CLEAN**.
> test HEAD **`2799e29`**(v1 초기 구현 baseline) — ROADMAP v1 merged 기대 **`e8750d2`** 와 **불일치**.
> test `mvn test` **79/79 PASS**(23 suites, Boot 3.3.1, JAR 76,466,058 B). develop HEAD `mvn test` **226/226 PASS**(62 suites, 91차 독립 실측).
> develop **20커밋 ahead** — merge 미실행. **모든 v1 baseline + v1.3-A transport(unconfirm PATCH+POST) + v3 meals/programs artifacts PRESENT @ 767d977(TSR 91차 독립 검증 PASS)**.
> **교차 관측**: frontend `73f7d39` `TransportUnconfirmModal`·US-T02 unconfirm UI PRESENT — backend test 미승격·live E2E 잔여.
> **v3 develop-only** — ROADMAP v3 버전·merge 게이트 미정의(planner 정의 대기).

> **89차 재검증 (07:02 UTC) — develop `767d977` CLEAN·v1.3-A transport unconfirm PATCH 계약·merge 20커밋·develop 226/226·test 79/79·Open 0·BLOCK(merge 게이트 단일)**:
> develop HEAD **`767d977`**(+1커밋 vs 87차 `0d8968d` — `fix(v1.3-A): align transport unconfirm route with PATCH contract`: `TransportController.java`(+11 — `PATCH /runs/{runId}/unconfirm` v1.3 API 계약·`POST` legacy alias)·`TransportControllerRoutingTest.java`(+3 — PATCH·POST dual-method RBAC)·`MustApiEndpointRoutingTest`(+2 transport unconfirm PATCH routing), 3 files, +15/-1), working tree **CLEAN**.
> test HEAD **`2799e29`**(v1 초기 구현 baseline) — ROADMAP v1 merged 기대 **`e8750d2`** 와 **불일치**.
> test `mvn test` **79/79 PASS**(23 suites, Boot 3.3.1, JAR 76,466,058 B). develop HEAD `mvn test` **226/226 PASS**(62 suites, 87차 불변 — routing assertion 확장만).
> develop **20커밋 ahead** — merge 미실행. **모든 v1 baseline + v1.3-A transport(unconfirm PATCH+POST) + v3 meals/programs artifacts PRESENT @ 767d977(TSR 89차 독립 검증 PASS)**.
> **v3 develop-only** — ROADMAP v3 버전·완료 기준·merge 게이트 미정의(planner 정의 대기). v1.3-A transport unconfirm PATCH API develop-only — frontend unconfirm UI·US-T01~T03 live E2E 잔여.

> **87차 재검증 (05:58 UTC) — develop `0d8968d` CLEAN·v1.3-A transport run unconfirm·merge 19커밋·develop 226/226·test 79/79·Open 0·BLOCK(merge 게이트 단일)**:
> develop HEAD **`0d8968d`**(+1커밋 vs 85차 `dfd9be2` — `feat(v1.3-A): support transport run unconfirm flow for hq_admin`: `TransportController.java`(+9 — `POST /runs/{runId}/unconfirm` hq_admin RBAC)·`TransportService.java`(+31 — `unconfirmRun` CONFIRMED→DRAFT·`unconfirmedAt`/`unconfirmedBy`)·`TransportRunResponse.java`(+3)·`TransportServiceTest.java`(+46 — 2 @Test)·`TransportControllerRoutingTest.java`(+7)·`MustApiEndpointRoutingTest`(+6 transport unconfirm RBAC), 6 files, +102 insertions), working tree **CLEAN**.
> test HEAD **`2799e29`**(v1 초기 구현 baseline) — ROADMAP v1 merged 기대 **`e8750d2`** 와 **불일치**.
> test `mvn test` **79/79 PASS**(23 suites, Boot 3.3.1, JAR 76,466,058 B). develop HEAD `mvn test` **226/226 PASS**(62 suites, 85차 224 → +2: `TransportServiceTest` unconfirm 2건).
> develop **19커밋 ahead** — merge 미실행. **모든 v1 baseline + v1.3-A transport(unconfirm) + v3 meals/programs artifacts PRESENT @ 0d8968d(TSR 87차 독립 검증 PASS)**.
> **v3 develop-only** — ROADMAP v3 버전·완료 기준·merge 게이트 미정의(planner 정의 대기). v1.3-A transport unconfirm API develop-only — frontend unconfirm UI·US-T01~T03 live E2E 잔여.

> **85차 재검증 (04:55 UTC) — develop `dfd9be2` CLEAN·v3 meals/programs REST API·Flyway V49·merge 18커밋·develop 224/224·test 79/79·Open 0·BLOCK(merge 게이트 단일)**:
> develop HEAD **`dfd9be2`**(+1커밋 vs 83차 `53a1ffe` — `feat(v3): add meals and programs REST API with Flyway V49 schema`: `meals/api/MealController.java`(54 lines)·`meals/domain/MealService.java`(179 lines)·`meals/persistence/MealMenuEntity`(132)·`MealRecordEntity`(154)+Repository 2종·meals DTO 6종·`programs/api/ProgramController.java`(56 lines)·`programs/domain/ProgramService.java`(249 lines)·`programs/persistence/ActivityProgramEntity`(155)·`ProgramParticipationEntity`(143)+Repository 2종·programs DTO 6종·`db/migration/V49__meals_programs_v3_schema.sql`(403 lines — meal_menus·meal_records·activity_programs·program_participations)·`meals/domain/MealServiceTest`(146)·`meals/api/MealControllerRoutingTest`(67)·`programs/domain/ProgramServiceTest`(171)·`programs/api/ProgramControllerRoutingTest`(67)·`routing/MustApiEndpointRoutingTest`(+100 meals/programs RBAC nested), 28 files, +2265 insertions), working tree **CLEAN**.
> test HEAD **`2799e29`**(v1 초기 구현 baseline) — ROADMAP v1 merged 기대 **`e8750d2`** 와 **불일치**.
> test `mvn test` **79/79 PASS**(23 suites, Boot 3.3.1, JAR 76,466,058 B). develop HEAD `mvn test` **224/224 PASS**(62 suites, 83차 212 → +12: MealServiceTest + MealControllerRoutingTest + ProgramServiceTest + ProgramControllerRoutingTest + MustApiEndpointRoutingTest meals/programs).
> develop **18커밋 ahead** — merge 미실행. **모든 v1 baseline + v1.3-A transport + v3 meals/programs artifacts PRESENT @ dfd9be2(TSR 85차 독립 검증 PASS)**.
> **v3 develop-only** — ROADMAP v3 버전·완료 기준·merge 게이트 미정의(planner 정의 대기). v3 backend API(dfd9be2) + v3 frontend UI 셸(7ef1083) 양 스트림 develop 존재 → planner ROADMAP v3 정의 권장(정상·결함 아님).

> **83차 재검증 (03:40 UTC) — develop `53a1ffe` CLEAN·v1.3-A transport API·Flyway V47·V48·Kakao geocode proxy·merge 17커밋·develop 212/212·test 79/79·Open 0·BLOCK(merge 게이트 단일)**:
> develop HEAD **`53a1ffe`**(+1커밋 vs 82차 `52e0621` — `feat(v1.3-A): add transport API, Flyway schema, and Kakao geocode proxy`: `TransportController.java`(98 lines — roster·runs CRUD·confirm RBAC·15-stop 검증)·`TransportService.java`(409 lines)·`KakaoGeocodeClient.java`(103 lines)·`TransportGeocodeService.java`(124 lines)·`TransportRunEntity.java`(165 lines)·`TransportRunStopEntity.java`(155 lines)·`TransportRunRepository`·`TransportRunStopRepository`·DTOs 8종·`TransportConfig`·`TransportProperties`·`V47__transport_v1_3_a.sql`(326 lines)·`V48__client_ltc_grade_history.sql`(85 lines)·`ClientEntity.java`(145 lines, ltcGrade 추가)·`ClientRepository.java`(+15)·`TransportServiceTest.java`(210 lines)·`TransportControllerRoutingTest.java`(100 lines)·`MustApiEndpointRoutingTest`(+79 TransportRouting nested class)·`application.yml`(+2 kakao.geocode), 30 files, +2233 insertions), working tree **CLEAN**.
> test HEAD **`2799e29`**(v1 초기 구현 baseline) — ROADMAP v1 merged 기대 **`e8750d2`** 와 **불일치**.
> test `mvn test` **79/79 PASS**(23 suites, Boot 3.3.1, JAR 76,466,058 B). develop HEAD `mvn test` **212/212 PASS**(82차 202 → +10: TransportServiceTest + TransportControllerRoutingTest + MustApiEndpointRoutingTest$TransportRouting).
> develop **17커밋 ahead** — merge 미실행. **모든 v1 baseline artifacts + v1.3-A transport artifacts PRESENT @ 53a1ffe(TSR 83차 독립 검증 PASS)**.

> **82차 재검증 (02:30 UTC) — develop `52e0621` CLEAN·v2/J03 copay claim PAID alimtalk dispatch·merge 16커밋·develop 202/202·test 79/79·Open 0·BLOCK(merge 게이트 단일)**:
> develop HEAD **`52e0621`**(+1커밋 vs 80차 `ac17ad8` — `feat(v2/J03): dispatch alimtalk when copay claim is marked PAID`: `NotificationEventType.java`(+1 — `BILLING_PAYMENT_RECEIVED` 이벤트 타입·`notifyBilling` consent 재사용)·`NotificationTemplateCodes.java`(+1)·`application.yml`(+1 — `KAKAO_TPL_BILLING_PAYMENT`)·`BillingService.java`(+17 — copay claim CONFIRMED→PAID 전환 시 보호자 알림톡 디스패치)·`AlimtalkFallbackText.java`(+25)·`AlimtalkTemplateVariables.java`(+3)·`BillingServiceTest.java`(+62)·`AlimtalkFallbackTextTest.java`(+12)·`AlimtalkTemplateVariablesTest.java`(+16)·`J03AlimtalkServiceFlowE2eTest.java`(+34), 11 files, +159/-16), working tree **CLEAN**.
> test HEAD **`2799e29`**(v1 초기 구현 baseline) — ROADMAP v1 merged 기대 **`e8750d2`** 와 **불일치**.
> test `mvn test` **79/79 PASS**(23 suites, Boot 3.3.1, JAR 76,466,058 B). develop HEAD `mvn test` **202/202 PASS**(53 suites, 80차 198 → +4: `BillingServiceTest` copay PAID + `AlimtalkTemplateVariablesTest` + `AlimtalkFallbackTextTest` + `J03AlimtalkServiceFlowE2eTest`).
> develop **16커밋 ahead** — merge 미실행. **모든 v1 baseline artifacts + service-layer alimtalk flow E2E + AlimtalkTemplateVariables + AlimtalkFallbackText + copay-claim PAID dispatch PRESENT @ 52e0621(TSR 82차 독립 검증 PASS)**.

> **80차 재검증 (01:25 UTC) — develop `ac17ad8` CLEAN·v2/J03 Korean SMS fallback text for alimtalk relay·merge 15커밋·develop 198/198·test 79/79·Open 0·BLOCK(merge 게이트 단일)**:
> develop HEAD **`ac17ad8`**(+1커밋 vs 79차 `4c74f84` — `feat(v2/J03): add Korean SMS fallback text for alimtalk relay`: `AlimtalkFallbackText.java`(89 lines — 알림 payload→Solapi 한국어 SMS fallback 메시지 매핑 도메인 모델)·`AlimtalkTemplateVariables.java`(+3 — `incidentType` emergency 카테고리 alias)·`SolapiKakaoAlimtalkProvider.java`(+3 — fallback text 전달)·`SolapiSmsProvider.java`(+6 — SMS fallback 본문 적용)·`AlimtalkFallbackTextTest.java`(64 lines)·`AlimtalkTemplateVariablesTest.java`(+31)·`SolapiKakaoAlimtalkProviderTest.java`(+31), 7 files, +225/-2), working tree **CLEAN**.
> test HEAD **`2799e29`**(v1 초기 구현 baseline) — ROADMAP v1 merged 기대 **`e8750d2`** 와 **불일치**.
> test `mvn test` **79/79 PASS**(23 suites, Boot 3.3.1). develop HEAD `mvn test` **198/198 PASS**(53 suites, 79차 191 → +7: `AlimtalkFallbackTextTest` + `AlimtalkTemplateVariablesTest` incidentType + `SolapiKakaoAlimtalkProviderTest` fallback).
> develop **15커밋 ahead** — merge 미실행. **모든 v1 baseline artifacts + service-layer alimtalk flow E2E + AlimtalkTemplateVariables + AlimtalkFallbackText PRESENT @ ac17ad8(TSR 80차 독립 검증 PASS)**.

> **79차 재검증 (00:18 UTC) — develop `4c74f84` CLEAN·v2/J03 alimtalk payload Solapi 변수 매핑·merge 14커밋·develop 191/191·test 79/79·Open 0·BLOCK(merge 게이트 단일)**:
> develop HEAD **`4c74f84`**(+1커밋 vs 78차 `32a1f8f` — `feat(v2/J03): map alimtalk payload to Solapi template variables`: `AlimtalkTemplateVariables.java`(74 lines — 카카오 템플릿 변수 매핑 도메인 모델)·`SolapiKakaoAlimtalkProvider.java`(+9 — `kakaoOptions.variables` 주입)·`SolapiMessageClient.java`(+11 — variables 전달)·`AlimtalkTemplateVariablesTest.java`(67 lines — 빌더·직렬화 단위 테스트)·`J03AlimtalkServiceFlowE2eTest.java`(+35 — medication·note daily-care dispatch 경로 확장)·`SolapiKakaoAlimtalkProviderTest.java`(+6 — variables 주입 커버리지), 6 files, +197/-5), working tree **CLEAN**.
> test HEAD **`2799e29`**(v1 초기 구현 baseline) — ROADMAP v1 merged 기대 **`e8750d2`** 와 **불일치**.
> test `mvn test` **79/79 PASS**(23 suites, Boot 3.3.1). develop HEAD `mvn test` **191/191 PASS**(51→52 suites, 78차 185 → +6: `AlimtalkTemplateVariablesTest` + `J03AlimtalkServiceFlowE2eTest` medication·note E2E + `SolapiKakaoAlimtalkProviderTest` variables).
> develop **14커밋 ahead** — merge 미실행. **모든 v1 baseline artifacts + service-layer alimtalk flow E2E + AlimtalkTemplateVariables PRESENT @ 4c74f84(TSR 79차 독립 검증 PASS)**.

> **78차 재검증 (23:20 UTC) — develop `32a1f8f` CLEAN·v2/J03 service-layer alimtalk flow E2E·merge 13커밋·develop 185/185·test 79/79·Open 0·BLOCK(merge 게이트 단일)**:

> **78차 재검증 (23:20 UTC) — develop `32a1f8f` CLEAN·v2/J03 service-layer alimtalk flow E2E·merge 13커밋·develop 185/185·test 79/79·Open 0·BLOCK(merge 게이트 단일)**:
> develop HEAD **`32a1f8f`**(+1커밋 vs 76차 `0832fbf` — `feat(v2/J03): add service-layer alimtalk flow E2E tests`: `J03AlimtalkServiceFlowE2eTest`(357 lines — attendance·health·billing 도메인 액션을 `NotificationService` 경유로 wire·US-J03 커버리지)·`AttendanceServiceTest`(+67 lines — check-out dispatch 커버리지), 2 files +424), working tree **CLEAN**.
> test HEAD **`2799e29`**(v1 초기 구현 baseline) — ROADMAP v1 merged 기대 **`e8750d2`** 와 **불일치**.
> test `mvn test` **79/79 PASS**(23 suites, Boot 3.3.1). develop HEAD `mvn test` **185/185 PASS**(51 suites, 76차 179 → +6: `J03AlimtalkServiceFlowE2eTest` + `AttendanceServiceTest` check-out dispatch).
> develop **13커밋 ahead** — merge 미실행. **모든 v1 baseline artifacts + service-layer alimtalk flow E2E PRESENT @ 32a1f8f(TSR 78차 독립 검증 PASS)**.

> **76차 재검증 (22:23 UTC) — develop `0832fbf` CLEAN·v2/J03 DAILY_CARE vitals dispatch·merge 12커밋·develop 179/179·test 79/79·Open 0·BLOCK(merge 게이트 단일)**:
> develop HEAD **`0832fbf`**(+1커밋 vs 74차 `8ce1151` — `feat(v2/J03): dispatch DAILY_CARE notifications for vitals`: `HealthRecordService`(활력징후 기록 생성 시 보호자 일일돌봄 알림톡 디스패치)·`HealthRecordServiceTest`(vitals dispatch payload 단위 테스트 +53 lines), 2 files +96), working tree **CLEAN**.
> test HEAD **`2799e29`**(v1 초기 구현 baseline) — ROADMAP v1 merged 기대 **`e8750d2`** 와 **불일치**.
> test `mvn test` **79/79 PASS**(23 suites, Boot 3.3.1). develop HEAD `mvn test` **179/179 PASS**(50 suites, 74차 178 → +1: `HealthRecordServiceTest` vitals dispatch).
> develop **12커밋 ahead** — merge 미실행. **모든 v1 baseline artifacts + vitals dispatch PRESENT @ 0832fbf(TSR 76차 독립 검증 PASS)**.

> **74차 재검증 (21:20 UTC) — develop `8ce1151` CLEAN·V46 notification history query index·merge 11커밋·develop 178/178·test 79/79·Open 0·BLOCK(merge 게이트 단일)**:
> develop HEAD **`8ce1151`**(+1커밋 vs 72차 `c53dd3b` — `feat(v2/J03): add notification history query index (V46)`: `V46__notification_history_query_index.sql`(9 lines — `idx_notifications_org_recipient_created`(organization_id, recipient_user_id, created_at DESC)), 1 file +9), working tree **CLEAN**.
> test HEAD **`2799e29`**(v1 초기 구현 baseline) — ROADMAP v1 merged 기대 **`e8750d2`** 와 **불일치**.
> test `mvn test` **79/79 PASS**(23 suites, Boot 3.3.1). develop HEAD `mvn test` **178/178 PASS**(50 suites, 72차 불변 — V46 신규 @Test 없음).
> develop **11커밋 ahead** — merge 미실행. **모든 v1 baseline artifacts + V46 PRESENT @ 8ce1151(TSR 74차 독립 검증 PASS)**.

> **72차 재검증 (20:10 UTC) — develop `c53dd3b` CLEAN·v2/J03 guardian·staff 알림 이역 API·merge 10커밋·develop 178/178·test 79/79·Open 0·BLOCK(merge 게이트 단일)**:
> develop HEAD **`c53dd3b`**(+1커밋 vs 70차 `78e8928` — `feat(v2/J03): add guardian and staff notification history APIs`: `GuardianNotificationHistoryController`·`StaffClientNotificationHistoryController`·`NotificationHistoryService`(187)·`NotificationHistoryServiceTest`(168)·`MustApiEndpointRoutingTest`(+46 알림 이력 RBAC), 8 files +514), working tree **CLEAN**.
> test HEAD **`2799e29`**(v1 초기 구현 baseline) — ROADMAP v1 merged 기대 **`e8750d2`** 와 **불일치**.
> test `mvn test` **79/79 PASS**(23 suites, Boot 3.3.1). develop HEAD `mvn test` **178/178 PASS**(50 suites, 70차 171 → +7: `NotificationHistoryServiceTest` + `MustApiEndpointRoutingTest` 알림 이력).
> develop **10커밋 ahead** — merge 미실행. **모든 v1 baseline artifacts + 신규 알림 이력 API PRESENT @ c53dd3b(TSR 72차 독립 검증 PASS)**.

> **70차 재검증 (19:05 UTC) — develop `78e8928` CLEAN·v2/J03 DAILY_CARE medication dispatch·merge 9커밋·develop 171/171·test 79/79·Open 0·BLOCK(merge 게이트 단일)**:
> develop HEAD **`78e8928`**(+1커밋 vs 68차 `44e0f02` — `feat(v2/J03): dispatch DAILY_CARE alimtalk on medication records`: `HealthRecordService`(투약기록 생성 시 보호자 일일돌봄 알림톡 디스패치)·`HealthRecordServiceTest`(dispatch payload 단위 테스트)), working tree **CLEAN**.
> test HEAD **`2799e29`**(v1 초기 구현 baseline) — ROADMAP v1 merged 기대 **`e8750d2`** 와 **불일치**.
> test `mvn test` **79/79 PASS**(23 suites, Boot 3.3.1). develop HEAD `mvn test` **171/171 PASS**(48 suites, 68차 170 → +1: `HealthRecordServiceTest`).
> develop **9커밋 ahead** — merge 미실행. **모든 v1 baseline artifacts PRESENT @ 78e8928(TSR 70차 독립 검증 PASS)**.

> **68차 재검증 (18:07 UTC) — develop `44e0f02` CLEAN·NotificationConfig quiet hours·merge 8커밋·develop 170/170·test 79/79·Open 0·BLOCK(merge 게이트 단일)**:
> develop HEAD **`44e0f02`**(+1커밋 vs 66차 `c221531` — `Ensure quiet hours clock is provided and add coverage`: `NotificationConfig`·`NotificationConfigTest`·`GlobalExceptionHandler`·`SecurityConfig`), working tree **CLEAN**.
> test HEAD **`2799e29`**(v1 초기 구현 baseline) — ROADMAP v1 merged 기대 **`e8750d2`** 와 **불일치**.
> test `mvn test` **79/79 PASS**(23 suites, Boot 3.3.1). develop HEAD `mvn test` **170/170 PASS**(66차 169 → +1: `NotificationConfigTest`).
> develop **8커밋 ahead** — merge 미실행. **모든 v1 baseline artifacts PRESENT @ 44e0f02(TSR 68차 독립 검증 PASS)**.

> **66차 재검증 (17:22 UTC) — develop `c221531` CLEAN·v2/J03 daily care·emergency health alimtalk E2E·merge 7커밋·develop 169/169·test 79/79·Open 0·BLOCK(merge 게이트 단일)**:
> develop HEAD **`c221531`**(+1커밋 vs 64차 `80bdb1e` — `feat(v2/J03): wire daily care·emergency health notifications and alimtalk E2E tests`), working tree **CLEAN**.
> test HEAD **`2799e29`**(v1 초기 구현 baseline) — ROADMAP v1 merged 기대 **`e8750d2`** 와 **불일치**.
> test `mvn test` **79/79 PASS**(23 suites, Boot 3.3.1). develop HEAD `mvn test` **169/169 PASS**(64차 158 → +11).
> develop **7커밋 ahead** — merge 미실행. **모든 v1 baseline artifacts PRESENT @ c221531(TSR 66차 독립 검증 PASS)**.

## 커밋 수준 (80차)

| 항목 | 값 |
|------|-----|
| `develop` HEAD | `ac17ad8` — `feat(v2/J03): add Korean SMS fallback text for alimtalk relay` |
| `test` HEAD | `2799e29` — `feat: Spring Boot 3.x 백엔드 초기 구현` |
| ROADMAP v1 merged 기대 test | `e8750d2` — **미달** (213 tests·Boot 3.5.3·SEC-007) |
| `git rev-list --count test..develop` | **15** |
| develop working tree | **CLEAN** (0 dirty) |
| test working tree | **CLEAN** |

### develop 15커밋 ahead (test 미반영 — merge 게이트)

| 커밋 | QA | 요약 |
|------|-----|------|
| `f47ffa1` | **B09·B08·BE-8 Fixed** | J01 `guardianinvitations/*` + V43 + notification V41–V42 + V35–V40 + SecurityConfig |
| `cf6116c` | **BE-10 Fixed** | v1 baseline 복원 — `PilotChecklistJwtE2eTest`·`MustApiEndpointRoutingTest`·`ProductionSecretValidatorTest`·`SevenRoleJwtLoginE2eTest`·`RoleBasedControllerAccessTest` |
| `3f9264f` | v2/J03 | NotificationService dispatch skeleton + stub providers |
| `136239e` | v2/J03 Solapi | SolapiKakaoAlimtalkProvider·GuardianPhoneStorage·BillingNotifyService·PhoneMaskingUtil |
| `8d42bdd` | **BE-11 Fixed (SEC-D13)** | `AuthRateLimitService` IP+email 슬라이딩 윈도우 60s, login·refresh·reset rate limit, 429 RATE_LIMITED |
| `80bdb1e` | v2 V45 | `V45__v2_notification_prefs_integrity_and_users_phone_pair.sql` — users phone pair·notifications FK·guardian_invitations index |
| `c221531` | v2/J03 | `NotificationAlimtalkDispatchE2eTest`(7 @Test) — daily care·emergency health notifications alimtalk dispatch E2E |
| `44e0f02` | v2/J03 follow-up | `NotificationConfig` quiet hours clock·`NotificationConfigTest`·`GlobalExceptionHandler`·`SecurityConfig` 정리 |
| `78e8928` | v2/J03 | `HealthRecordService` 투약기록 생성 시 보호자 DAILY_CARE 알림톡 디스패치 연동·`HealthRecordServiceTest` dispatch payload 단위 테스트 |
| `c53dd3b` | v2/J03 | `GuardianNotificationHistoryController`·`StaffClientNotificationHistoryController`·`NotificationHistoryService`(187)·`NotificationHistoryServiceTest`(168)·`MustApiEndpointRoutingTest`(+46) — 보호자/직원 알림 이력 조회 API |
| `8ce1151` | v2/J03 V46 | `V46__notification_history_query_index.sql`(9 lines) — `idx_notifications_org_recipient_created`(organization_id, recipient_user_id, created_at DESC) — tenant-scoped pagination 성능 최적화 |
| `0832fbf` | v2/J03 | `HealthRecordService` 활력징후 기록 생성 시 보호자 DAILY_CARE 알림톡 디스패치·`HealthRecordServiceTest` vitals dispatch payload 단위 테스트 (+53 lines) |
| `32a1f8f` | v2/J03 | `J03AlimtalkServiceFlowE2eTest`(357 lines — attendance·health·billing 도메인 액션 `NotificationService` 경유 wire·US-J03 커버리지)·`AttendanceServiceTest`(+67 — check-out dispatch) |
| `4c74f84` | v2/J03 | `AlimtalkTemplateVariables.java`(74 lines — 카카오 템플릿 변수 매핑)·`SolapiKakaoAlimtalkProvider`(+9 variables 주입)·`AlimtalkTemplateVariablesTest.java`(67 lines)·`J03AlimtalkServiceFlowE2eTest`(+35 medication·note path)·`SolapiKakaoAlimtalkProviderTest`(+6) |
| `ac17ad8` | v2/J03 | `AlimtalkFallbackText.java`(89 lines — 알림 payload→Solapi 한국어 SMS fallback 메시지 매핑)·`AlimtalkTemplateVariables`(+3 `incidentType` emergency alias)·`SolapiKakaoAlimtalkProvider`(+3 fallback text 전달)·`SolapiSmsProvider`(+6 SMS fallback 본문)·`AlimtalkFallbackTextTest.java`(64 lines)·`AlimtalkTemplateVariablesTest`(+31)·`SolapiKakaoAlimtalkProviderTest`(+31) |

### develop HEAD 산출물 검증 (규율 5, 80차)

| path | HEAD |
|------|------|
| `guardianinvitations/api/GuardianInvitationController.java` | **PRESENT** (f47ffa1) |
| `db/migration/V43__guardian_invitations.sql` | **PRESENT** (f47ffa1) |
| `notification/domain/NotificationPreferenceService.java` | **PRESENT** (f47ffa1) |
| `db/migration/V42__*.sql` | **PRESENT** (f47ffa1) |
| `pilot/PilotChecklistJwtE2eTest.java` | **PRESENT** (cf6116c) |
| `security/SevenRoleJwtLoginE2eTest.java` | **PRESENT** (cf6116c) |
| `security/ProductionSecretValidatorTest.java` | **PRESENT** (cf6116c) |
| `routing/MustApiEndpointRoutingTest.java` | **PRESENT** (cf6116c) |
| `security/RoleBasedControllerAccessTest.java` | **PRESENT** (cf6116c) |
| `auth/domain/AuthRateLimitService.java` | **PRESENT** (8d42bdd) ← **BE-11 Fixed** |
| `auth/domain/AuthRateLimitServiceTest.java` | **PRESENT** (8d42bdd) |
| `db/migration/V45__*.sql` | **PRESENT** (80bdb1e) ← **V45** |
| `notification/domain/NotificationAlimtalkDispatchE2eTest.java` | **PRESENT** (c221531) |
| `notification/config/NotificationConfigTest.java` | **PRESENT** (44e0f02) ← **quiet hours coverage** |
| `health/domain/HealthRecordServiceTest.java` | **PRESENT** (78e8928·0832fbf) ← **DAILY_CARE medication + vitals dispatch coverage** |
| `notification/api/GuardianNotificationHistoryController.java` | **PRESENT** (c53dd3b) ← **보호자 알림 이력** |
| `notification/api/StaffClientNotificationHistoryController.java` | **PRESENT** (c53dd3b) ← **직원 알림 이력** |
| `notification/domain/NotificationHistoryService.java` | **PRESENT** (c53dd3b) ← **스코프 페이지네이션 이력** |
| `db/migration/V46__notification_history_query_index.sql` | **PRESENT** (8ce1151) ← **V46 tenant-scoped pagination index** |
| `notification/domain/NotificationHistoryServiceTest.java` | **PRESENT** (c53dd3b) ← **이력 조회 단위 테스트** |
| `notification/domain/J03AlimtalkServiceFlowE2eTest.java` | **PRESENT** (32a1f8f·4c74f84) ← **service-layer alimtalk flow E2E + medication·note path** |
| `attendance/domain/AttendanceServiceTest.java` | **PRESENT** (32a1f8f) ← **check-out dispatch 커버리지** |
| `notification/provider/solapi/AlimtalkTemplateVariables.java` | **PRESENT** (4c74f84) ← **Solapi 변수 매핑 도메인 모델** |
| `notification/provider/solapi/AlimtalkTemplateVariablesTest.java` | **PRESENT** (4c74f84) ← **변수 매핑 단위 테스트** |
| `notification/provider/solapi/SolapiKakaoAlimtalkProvider.java` | **PRESENT** (4c74f84·ac17ad8) ← **kakaoOptions.variables + fallback text** |
| `notification/domain/AlimtalkFallbackText.java` | **PRESENT** (ac17ad8) ← **한국어 SMS fallback 매핑 도메인 모델** |
| `notification/domain/AlimtalkFallbackTextTest.java` | **PRESENT** (ac17ad8) ← **fallback 매핑 단위 테스트** |
| `notification/provider/solapi/SolapiSmsProvider.java` | **PRESENT** (ac17ad8) ← **SMS fallback 본문 적용** |

## Maven (80차 실측)

| context | command | result |
|---------|---------|--------|
| test `@2799e29` | `mvn test` | **79/79 PASS** (23 suites) |
| develop `@ac17ad8` | `mvn test` | **198/198 PASS** (53 suites, 79차 191 → +7) |
| test package | `mvn -q -DskipTests package` | SUCCESS — JAR **76,466,058 B** (test 불변) |

## 판정

**BLOCK** — merge 게이트(15커밋). develop CLEAN·v1 baseline artifacts + AlimtalkTemplateVariables + service-layer alimtalk flow E2E + AlimtalkFallbackText PRESENT·198/198 PASS. test `@2799e29` stale 79/79. **Open 0건**.

---

## 이력 — 58차 재검증 (2026-06-07T14:00 UTC)

> develop HEAD **`f47ffa1`**, working tree CLEAN. test **`2799e29`** 79/79. develop **1커밋 ahead**. **QA-B09 Fixed** · **SEC-D8 Fixed** · **신규 Open QA-B10**(v1 merged baseline regression). 판정 **BLOCK**(merge+history).
