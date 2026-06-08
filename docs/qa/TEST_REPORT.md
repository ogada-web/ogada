<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-08T09:13:00+00:00 -->
<!-- tester-sync: TSR 92차 2026-06-08T09:13 UTC (frontend) — test `@c510f5c` **불변**(v1.2 merged) · `npm test` **143/46 PASS** · build **125 modules** · audit **0**(독립 실측) · develop `637b9b3`(+2 vs 91차 `8a764df`: `00375f6` feat(uxd-49): HQ 통합 대시보드 건강 이상 목록 지점명 표시(US-H02) · `637b9b3` feat(v1.3-A): pilotPageFlows transport US-T01~T03 E2E + pilotChecklist T01~T03) CLEAN · develop `npm test` **189/60 PASS**(+6/0 vs 91차 183/60) · build **766 modules**(JS 756 kB, vite >500kB **non-blocking LOW**) · audit **0** · develop **12커밋 ahead** · 이관 규율 5 PRESENT(+ChartContainer·TransportUnconfirmModal·pilotPageFlows T01~T03)·SEC-005 0건·KAKAO 키 env(하드코딩 0). **신규 Open 0건** — 판정 **PASS**(v1.2). v1.3 `pending`(backend transport API test 미승격·US-T01~T03 live E2E 잔여). v3 develop-only(+UXD-49·T01~T03 E2E). 잔여 BLOCK = backend merge(21) + SEC-D14 + post-merge live E2E(결정 73). -->
<!-- tester-sync: TSR 92차 2026-06-08T09:00 UTC (backend) — develop HEAD **`1ec538b`**(+1커밋 vs 91차 `767d977`: `feat(v1.3-A): expose client transport profile on Clients API (US-T01)` — `ClientResponse.java`(+5 — usesTransport·pickupAddress·pickupContact·defaultPickupTime)·`CreateClientRequest.java`(+7)·`UpdateClientRequest.java`(+7)·`ClientService.java`(+52 — transport profile 처리·pickup geocode 캐시 무효화)·`ClientServiceTest.java`(+176 — 9 @Test, transport profile 단위 테스트)·`PilotChecklistJwtE2eTest.java`(+45 — transport roster·run detail endpoint 라우팅 smoke test), 6 files, +286/-6) CLEAN · **`mvn test` develop 231/231 PASS**(62 suites, 91차 226 → +5: `ClientServiceTest` transport profile +2·`PilotChecklistJwtE2eTest` transport routing +3) · test `2799e29` **79/79 PASS**(23 suites, Boot 3.3.1, JAR 76,466,058 B) · develop **21커밋 ahead** of test · merge **미실행** · v1 baseline + v1.3-A transport(unconfirm PATCH+POST·client transport profile) + v3 meals/programs artifacts PRESENT @ 1ec538b(TSR 92차 독립 검증 PASS) ✓ (이관 규율 5·6 PASS). **신규 Open 0건** — 판정 **BLOCK**(merge 게이트 21커밋 단일). **US-T01 backend 완료**: Clients API transport profile 노출(usesTransport·pickup address/contact·defaultPickupTime) — frontend roster 구성 가능. US-T02·T03 live E2E 잔여(frontend 연동 + test 승격 후). v3 develop-only(ROADMAP v3 미정의). 잔여 BLOCK = develop→test merge(21) + SEC-D14. -->
<!-- tester-sync: TSR 91차 2026-06-08T08:05 UTC (frontend) — test `@c510f5c` **불변**(v1.2 merged) · `npm test` **143/46 PASS** · build **125 modules** · audit **0**(독립 실측) · develop `8a764df`(+1 vs `73f7d39`: UXD-48 Recharts ChartContainer·AttendanceRateChart·HealthTrendChart) CLEAN · develop `npm test` **183/60 PASS** · build **766 modules**(JS 756 kB, vite >500kB LOW) · audit **0** · develop **10커밋 ahead** · 이관 규율 5 PRESENT(+ChartContainer·TransportUnconfirmModal)·SEC-005 0건. **신규 Open 0건** — 판정 **PASS**(v1.2). v1.3 pending·v3 develop-only(+Recharts). 잔여 BLOCK = backend merge(20) + SEC-D14 + post-merge live E2E(결정 73). -->
<!-- tester-sync: TSR 90차 2026-06-08T07:08 UTC (frontend) — test `@c510f5c` **불변**(v1.2 merged) · `npm test` **143/46 PASS** · build **125 modules** · audit **0**(독립 실측) · develop `73f7d39`(+1 vs `fe33e7c`: UXD-47 StaffPage a11y·TransportUnconfirmModal US-T02) CLEAN · develop `npm test` **179/58 PASS** · build **143 modules** · audit **0** · develop **9커밋 ahead** · 이관 규율 5 PRESENT(+TransportUnconfirmModal)·SEC-005 0건. **신규 Open 0건** — 판정 **PASS**(v1.2). v1.3 unconfirm UI develop-only·live E2E 잔여. v3 develop-only. 잔여 BLOCK = backend merge(20) + SEC-D14 + post-merge live E2E(결정 73). -->
<!-- tester-sync: TSR 89차 2026-06-08T07:02 UTC (backend) — develop HEAD **`767d977`**(+1커밋 vs 87차 `0d8968d`: v1.3-A transport unconfirm PATCH contract + POST legacy alias, 3 files +15/-1) CLEAN · `mvn test` develop **226/226 PASS**(62 suites, 87차 불변) · test `2799e29` **79/79 PASS**(23 suites, Boot 3.3.1, JAR 76,466,058 B) · develop **20커밋 ahead** of test · merge **미실행** · v1 baseline + v1.3-A transport(unconfirm PATCH+POST) + v3 meals/programs artifacts PRESENT @ 767d977(TSR 89차 독립 검증 PASS) ✓ (이관 규율 5·6 PASS). **신규 Open 0건** — 판정 **BLOCK**(merge 게이트 20커밋 단일). 잔여 BLOCK = develop→test merge(20) + SEC-D14. v1.3-A transport unconfirm PATCH develop-only — frontend unconfirm UI·US-T01~T03 live E2E 잔여. -->
<!-- tester-sync: TSR 88차 2026-06-08T06:10 UTC (frontend) — test `@c510f5c` **불변**(v1.2 merged) · `src/frontend-test` `npm test` **143/46 PASS** · build **125 modules**(vite 6.4.3, JS 320.10 kB gzip 91.25 kB, CSS 31.03 kB) · audit **0**(독립 실측, 86차와 동일) · develop `fe33e7c`(+8 vs `c510f5c`: `f01e3a8` US-G06 UNMATCHED · `e8d1854` v1.3-A 배차 UI 셸 · `f0b174a` v1.3 배차 a11y · `7ef1083` v3 식사·프로그램 UI 셸 · `3e9a9ab` v3 a11y · `362dbf0` v3 meals/programs E2E · `762b5a8` UXD-46 CSS 유틸·체크인 접근성 · `fe33e7c` v3 직원 관리 UI) CLEAN · develop `npm test` **170/55 PASS**(+6/+1 vs 86차 164/54: StaffPage·UXD-46 AttendancePage 회귀) · build **140 modules**(JS 351.51 kB gzip 98.38 kB, CSS 33.97 kB) · audit **0** · develop **8커밋 ahead** · 이관 규율 5 — ProtectedRoute·services.js·SideNav·pilotChecklist·AuthContext·ReconciliationPage + v1.3-A Transport + v3 Meals/Programs + v3 StaffPage **PRESENT** · SEC-005 **0건** · KAKAO map key env(하드코딩 0) · **신규 Open 0건** · **PASS**(v1.2). v1.3 `pending`(backend transport API test 미승격·라이브 E2E 잔여)·v3 develop-only(+직원 UI 셸 fe33e7c·ROADMAP v3 정의 대기). 잔여 BLOCK = backend merge(19) + SEC-D14 + post-merge live E2E(결정 73). -->
<!-- tester-sync: TSR 87차 2026-06-08T05:58 UTC (backend) — develop HEAD **`0d8968d`**(+1커밋 vs 85차 `dfd9be2`: v1.3-A transport run unconfirm hq_admin, 6 files +102) CLEAN · `mvn test` develop **226/226 PASS**(85차 224 → +2) · test `2799e29` **79/79 PASS**(23 suites, Boot 3.3.1, JAR 76,466,058 B) · develop **19커밋 ahead** of test · merge **미실행** · v1 baseline + v1.3-A transport(unconfirm) + v3 meals/programs artifacts PRESENT @ 0d8968d(TSR 87차 독립 검증 PASS) ✓ (이관 규율 5·6 PASS). **신규 Open 0건** — 판정 **BLOCK**(merge 게이트 19커밋 단일). 잔여 BLOCK = develop→test merge(19) + SEC-D14. v1.3-A transport unconfirm develop-only — frontend unconfirm UI·US-T01~T03 live E2E 잔여. -->
<!-- tester-sync: TSR 86차 2026-06-08T05:00 UTC (frontend) — test `@c510f5c` **불변**(v1.2 merged) · `src/frontend-test` `npm ci`+`npm test` **143/46 PASS** · build **125 modules**(vite 6.4.3, JS 320.10 kB gzip 91.25 kB, CSS 31.03 kB) · audit **0**(독립 실측, 84차와 동일) · develop `362dbf0`(+6 vs `c510f5c`: `f01e3a8` US-G06 UNMATCHED 검색 · `e8d1854` v1.3-A 배차 UI 셸 · `f0b174a` v1.3 배차 a11y 재점검 · `7ef1083` v3 식사·프로그램 관리 UI 셸 §3-5·§3-6 · `3e9a9ab` v3 식사·프로그램 기록 폼 a11y 재점검 US-N01·N02 · `362dbf0` v3 meals/programs API E2E via pilotPageFlows US-N01·N02) CLEAN · develop `npm test` **164/54 PASS**(+7/+1 vs 84차 157/53: v3 meals/programs pilotPageFlows US-N01·N02 E2E 회귀) · build **139 modules**(JS 347.60 kB gzip 97.57 kB, CSS 33.35 kB) · audit **0** · develop **6커밋 ahead** · 이관 규율 5 — ProtectedRoute·services.js·SideNav·pilotChecklist·AuthContext·ReconciliationPage + v1.3-A Transport(Page·RunNew·RunDetail·KakaoMap·Disclaimer·StopList·transport.js·transportUtils) + v3 Meals/Programs(MealsPage·ProgramsPage·MealRecordForm·ProgramParticipationForm·meals.js·programs.js + a11y + pilotPageFlows US-N01·N02) **PRESENT** · SEC-005 **0건** · KAKAO map key `VITE_KAKAO_MAP_JS_KEY` env(하드코딩 0) · `MAX_TRANSPORT_STOPS=15` · **신규 Open 0건** · **PASS**(v1.2). v1.3 `in_progress`/`merge_status: pending` — v1.3-A frontend UI 셸은 backend v1.3-A transport API(develop `53a1ffe` PRESENT·test 미승격)·RBAC·US-T01~T03 라이브 E2E 동반 후 merge. **v3(식사·프로그램) develop-only** — ROADMAP 버전·merge 게이트 미설정(planner 정의 대기), 정상(결함 아님). backend v3 API(dfd9be2) + frontend v3 UI 셸(362dbf0) 양 스트림 develop 존재 → planner: ROADMAP v3·USER_STORIES(식사 §3-5·프로그램 §3-6)·API_SPEC v3 정의 권장. 잔여 BLOCK = backend merge(18) + SEC-D14 + post-merge live E2E(결정 73). -->
<!-- tester-sync: TSR 85차 2026-06-08T04:55 UTC (backend) — develop HEAD **`dfd9be2`**(+1커밋 vs 83차 `53a1ffe`: `feat(v3): add meals and programs REST API with Flyway V49 schema` — `MealController`·`MealService`·`MealMenuEntity`·`MealRecordEntity`+Repository·meals DTO 6종·`ProgramController`·`ProgramService`·`ActivityProgramEntity`·`ProgramParticipationEntity`+Repository·programs DTO 6종·`V49__meals_programs_v3_schema.sql`(403 lines — meal_menus·meal_records·activity_programs·program_participations)·`MealServiceTest`(146)·`MealControllerRoutingTest`(67)·`ProgramServiceTest`(171)·`ProgramControllerRoutingTest`(67)·`MustApiEndpointRoutingTest`(+100 meals/programs RBAC), 28 files +2265) CLEAN · **`mvn test` develop 224/224 PASS**(62 suites, 83차 212 → +12) · test `2799e29` **79/79 PASS**(23 suites, Boot 3.3.1, JAR 76,466,058 B) · develop **18커밋 ahead** of test · merge **미실행** · v1 baseline + v1.3-A transport + v3 meals/programs artifacts PRESENT @ dfd9be2(TSR 85차 독립 검증 PASS) ✓ (이관 규율 5·6 PASS). **신규 Open 0건** — 판정 **BLOCK**(merge 게이트 18커밋 단일). 잔여 BLOCK = develop→test merge(18) + SEC-D14. **v3 develop-only** — ROADMAP v3 버전·완료 기준·merge 게이트 미정의(planner 정의 대기). 이제 v3 backend API(dfd9be2) + v3 frontend UI 셸(7ef1083) 양 스트림 develop 존재 → planner ROADMAP v3·USER_STORIES·API_SPEC v3 정의 권장(정상·결함 아님). -->
<!-- tester-sync: TSR 84차 2026-06-08T03:55 UTC (frontend) — test `@c510f5c` **불변**(v1.2 merged) · `src/frontend-test` `npm ci`+`npm test` **143/46 PASS** · build **125 modules**(vite 6.4.3, JS 320.10 kB gzip 91.25 kB, CSS 31.03 kB) · audit **0** (독립 실측, 82차와 동일) · develop `7ef1083`(+4 vs `c510f5c`: `f01e3a8` US-G06 UNMATCHED 검색 · `e8d1854` v1.3-A 배차 UI 셸 · `f0b174a` v1.3 배차 a11y 재점검 · `7ef1083` v3 식사·프로그램 관리 UI 셸 §3-5·§3-6) CLEAN · develop `npm test` **157/53 PASS**(+7/+3 vs 82차 150/50) · build **139 modules**(JS 347.26 kB gzip 97.45 kB, CSS 33.35 kB) · audit **0** · develop **4커밋 ahead** · 이관 규율 5 — ProtectedRoute·services.js·SideNav·pilotChecklist·AuthContext·ReconciliationPage + v1.3-A Transport(Page·RunNew·RunDetail·KakaoMap·Disclaimer·StopList·transport.js·transportUtils) + v3 Meals/Programs(MealsPage·ProgramsPage·MealRecordForm·ProgramParticipationForm·meals.js·programs.js) **PRESENT** · SEC-005 **0건** · KAKAO map key `VITE_KAKAO_MAP_JS_KEY` env(하드코딩 0) · `MAX_TRANSPORT_STOPS=15` · **신규 Open 0건** · **PASS**(v1.2). v1.3 `in_progress`/`merge_status: pending` — v1.3-A frontend UI 셸은 backend v1.3-A transport API(develop `53a1ffe` PRESENT·test 미승격)·RBAC·US-T01~T03 라이브 E2E 동반 후 merge. **v3(식사·프로그램) develop-only** — ROADMAP 버전·merge 게이트 미설정(planner 정의 대기), 정상(결함 아님). 잔여 BLOCK = backend merge(17) + SEC-D14 + post-merge live E2E(결정 73). planner: 7ef1083 v3 식사·프로그램 UI 셸 → ROADMAP v3 버전·완료 기준 정의 권장. -->
<!-- tester-sync: TSR 83차 2026-06-08T03:40 UTC (backend) — develop HEAD **`53a1ffe`**(+1커밋 vs 82차 `52e0621`: `feat(v1.3-A): add transport API, Flyway schema, and Kakao geocode proxy` — `TransportController.java`(98 lines — roster·runs CRUD·confirm RBAC·15-stop)·`TransportService.java`(409 lines)·`KakaoGeocodeClient.java`(103 lines)·`TransportGeocodeService.java`(124 lines)·`TransportRunEntity.java`(165 lines)·`TransportRunStopEntity.java`(155 lines)·`V47__transport_v1_3_a.sql`(326 lines)·`V48__client_ltc_grade_history.sql`(85 lines)·`ClientEntity.java`(145 lines, ltcGrade 추가)·`TransportServiceTest.java`(210 lines)·`TransportControllerRoutingTest.java`(100 lines)·`MustApiEndpointRoutingTest`(+79 TransportRouting nested class), 30 files, +2233 insertions) CLEAN · **`mvn test` develop 212/212 PASS**(53 suites→56, 82차 202 → +10: TransportServiceTest + TransportControllerRoutingTest + MustApiEndpointRoutingTest$TransportRouting) · test `2799e29` **79/79 PASS**(23 suites, Boot 3.3.1, JAR 76,466,058 B) · develop **17커밋 ahead** of test · merge **미실행** · v1 baseline artifacts + v1.3-A transport artifacts PRESENT @ 53a1ffe(TSR 83차 독립 검증 PASS) ✓ (이관 규율 5·6 PASS). **신규 Open 0건** — 판정 **BLOCK**(merge 게이트 17커밋 단일). 잔여 BLOCK = develop→test merge(17) + SEC-D14 단일. planner: 53a1ffe v1.3-A transport API backend 완료 → ROADMAP v1.3·US-T01~T03·API_SPEC v1.3-A 갱신 권장. -->
<!-- tester-sync: TSR 82차 2026-06-08T02:37 UTC (frontend) — **v1.2 merged @ test `c510f5c`** (81차 `4f71543` → v1.2 develop→test merge 완료) · `src/frontend-test` `npm ci`+`npm test` **143/46 PASS** · build **125 modules**(vite 6.4.3, JS 320.10 kB gzip 91.25 kB, CSS 31.03 kB) · audit **0** (독립 실측) · develop `e8d1854`(+2 vs 81차 `c510f5c`: `f01e3a8` feat(uxd-43): US-G06 UNMATCHED 후보 이용자 검색 UI 보강 · `e8d1854` feat(v1.3): add transport pickup dispatch UI shell (US-T01~T03)) CLEAN · develop `npm test` **150/50 PASS** · build **133 modules** · audit **0** · develop **2커밋 ahead** · 이관 규율 5 — ProtectedRoute·services.js·SideNav·pilotChecklist·liveConfig·AuthContext + v1.3-A(TransportPage·TransportRunNewPage·TransportRunDetailPage·KakaoTransportMap·TransportDisclaimer·transport.js·transportUtils) **PRESENT** · SEC-005 **0건** · KAKAO map key `VITE_KAKAO_MAP_JS_KEY` env(하드코딩 0) · **신규 Open 0건** · **PASS**(v1.2). v1.3 `in_progress`/`merge_status: pending` — v1.3-A는 frontend UI 셸 한정(DBA 스키마·roster/runs API·Geocoding 프록시·US-T01~T03 라이브 E2E 잔여) → 이관 게이트 미충족. -->
<!-- tester-sync: TSR 82차 2026-06-08T02:30 UTC (backend) — develop HEAD **`52e0621`**(+1커밋 vs 80차 `ac17ad8`: `feat(v2/J03): dispatch alimtalk when copay claim is marked PAID` — `NotificationEventType.java`(+1 `BILLING_PAYMENT_RECEIVED`·`notifyBilling` consent 재사용)·`NotificationTemplateCodes.java`(+1)·`application.yml`(+1 `KAKAO_TPL_BILLING_PAYMENT`)·`BillingService.java`(+17 copay claim CONFIRMED→PAID dispatch)·`AlimtalkFallbackText.java`(+25)·`AlimtalkTemplateVariables.java`(+3)·`BillingServiceTest.java`(+62)·`AlimtalkFallbackTextTest.java`(+12)·`AlimtalkTemplateVariablesTest.java`(+16)·`J03AlimtalkServiceFlowE2eTest.java`(+34), 11 files +159/-16) CLEAN · **`mvn test` develop 202/202 PASS**(53 suites, 80차 198 → +4) · test `2799e29` **79/79 PASS**(23 suites, Boot 3.3.1, JAR 76,466,058 B) · develop **16커밋 ahead** of test · merge **미실행** · v1 baseline artifacts + service-layer alimtalk flow E2E + AlimtalkTemplateVariables + AlimtalkFallbackText + copay-claim PAID dispatch PRESENT @ 52e0621(TSR 82차 독립 검증 PASS) ✓ (이관 규율 5·6 PASS). **신규 Open 0건** — 판정 **BLOCK**(merge 게이트 16커밋 단일). 잔여 BLOCK = develop→test merge(16) + SEC-D14 단일. -->
<!-- tester-sync: TSR 81차 2026-06-08T01:35 UTC (frontend) — test `@4f71543` **불변** · `npm test` **58/18 PASS** · build **86 modules** · audit **0** (독립 실측 CONFIRMED) · develop `c510f5c`(+2 vs 80차 `95b92b9`: `fd4e8f3` feat(ux): US-G06 DISCREPANCY 청구 라인 비교 링크·접근성 재점검 · `c510f5c` test(v1.2): US-G06 DISCREPANCY compare pilotPageFlows E2E) CLEAN · develop `npm test` **143/46 PASS**(+6/+1 vs 80차 137/45: US-G06 DISCREPANCY 회귀) · audit **0** · develop **15커밋 ahead** · 이관 규율 5 — ProtectedRoute·services.js·SideNav·pilotChecklist·liveConfig·AuthContext **PRESENT** · SEC-005 **0건** · **신규 Open 0건** · **PASS**(v1.1). 잔여 BLOCK = backend merge(15) only. -->
<!-- tester-sync: TSR 80차 2026-06-08T01:25 UTC (backend) — develop HEAD **`ac17ad8`**(+1커밋 vs 79차 `4c74f84`: `feat(v2/J03): add Korean SMS fallback text for alimtalk relay` — `AlimtalkFallbackText.java`(89 lines — 알림 payload→Solapi 한국어 SMS fallback 메시지 매핑 도메인 모델)·`AlimtalkTemplateVariables.java`(+3 — `incidentType` emergency 카테고리 alias)·`SolapiKakaoAlimtalkProvider.java`(+3 — fallback text 전달)·`SolapiSmsProvider.java`(+6 — SMS fallback 본문 적용)·`AlimtalkFallbackTextTest.java`(64 lines)·`AlimtalkTemplateVariablesTest.java`(+31)·`SolapiKakaoAlimtalkProviderTest.java`(+31), 7 files +225/-2) CLEAN · **`mvn test` develop 198/198 PASS**(53 suites, 79차 191 → +7: `AlimtalkFallbackTextTest` + `AlimtalkTemplateVariablesTest` incidentType + `SolapiKakaoAlimtalkProviderTest` fallback) · test `2799e29` **79/79 PASS**(23 suites, Boot 3.3.1, JAR 76,466,058 B) · develop **15커밋 ahead** of test · merge **미실행** · v1 baseline artifacts + service-layer alimtalk flow E2E + AlimtalkTemplateVariables + AlimtalkFallbackText PRESENT @ ac17ad8(TSR 80차 독립 검증 PASS) ✓ (이관 규율 5·6 PASS). **신규 Open 0건** — 판정 **BLOCK**(merge 게이트 15커밋 단일). -->
<!-- tester-sync: TSR 80차 2026-06-08T00:30 UTC (frontend) — test `@4f71543` **불변** · `npm test` **58/18 PASS** · build **86 modules** · audit **0** (독립 재실측 CONFIRMED) · develop `95b92b9`(+2 vs 77차 `4957bd3`: `3ec8206` feat(uxd-41): US-F03 낙상·사고·특이사항 이벤트 기록 UI 신설 · `95b92b9` fix(v1.2): US-F03 incident API 본문 detail 필드 정합) CLEAN · develop `npm test` **137/45 PASS** · build **124 modules** · audit **0** · develop **13커밋 ahead** · 이관 규율 5 — ProtectedRoute·services.js·SideNav·pilotChecklist·liveConfig·AuthContext **PRESENT** · SEC-005 **0건** · **신규 Open 0건** · **PASS**(v1.1). 잔여 BLOCK = backend merge(15) only. -->
<!-- tester-sync: TSR 79차 2026-06-08T00:18 UTC (backend) — develop HEAD **`4c74f84`**(+1커밋 vs 78차 `32a1f8f`: `feat(v2/J03): map alimtalk payload to Solapi template variables` — `AlimtalkTemplateVariables.java`(74 lines — 카카오 알림톡 템플릿 변수 매핑 도메인 모델)·`SolapiKakaoAlimtalkProvider.java`(+9 — `kakaoOptions.variables` 주입)·`SolapiMessageClient.java`(+11)·`AlimtalkTemplateVariablesTest.java`(67 lines — 빌더·직렬화 단위 테스트)·`J03AlimtalkServiceFlowE2eTest.java`(+35 — medication·note daily-care path 확장)·`SolapiKakaoAlimtalkProviderTest.java`(+6), 6 files +197/-5) CLEAN · **`mvn test` develop 191/191 PASS**(78차 185 → +6: `AlimtalkTemplateVariablesTest` + `J03AlimtalkServiceFlowE2eTest` medication·note path + `SolapiKakaoAlimtalkProviderTest` variables) · test `2799e29` **79/79 PASS**(23 suites, Boot 3.3.1, JAR 76,466,058 B) · develop **14커밋 ahead** of test · merge **미실행** · v1 baseline artifacts + service-layer alimtalk flow E2E + AlimtalkTemplateVariables PRESENT @ 4c74f84(TSR 79차 독립 검증 PASS) ✓ (이관 규율 5·6 PASS). **신규 Open 0건** — 판정 **BLOCK**(merge 게이트 14커밋 단일). -->
<!-- tester-sync: TSR 77차 2026-06-07T23:30 UTC (frontend) — test `@4f71543` **불변** · `npm test` **58/18 PASS** · build **86 modules** · audit **0** (독립 재실측 CONFIRMED) · develop `4957bd3`(+2 vs 76차 `c5708c7`: `9863312` UXD-40 US-F01 활력징후 비정상 범위 입력 경고·정상 범위 단일 원천 · `4957bd3` FAQ Q154 건강·NHIS API 본문 정합) CLEAN · develop `npm test` **130/44 PASS** · build **123 modules** · audit **0** · develop **11커밋 ahead** · 이관 규율 5 PRESENT · SEC-005 **0건** · **신규 Open 0건** · **PASS**(v1.1). 잔여 BLOCK = backend merge(13) only. -->
<!-- tester-sync: TSR 78차 2026-06-07T23:20 UTC (backend) — develop HEAD **`32a1f8f`**(+1커밋 vs 76차 `0832fbf`: `feat(v2/J03): add service-layer alimtalk flow E2E tests` — `J03AlimtalkServiceFlowE2eTest`(357 lines — attendance·health·billing 도메인 액션을 `NotificationService` 경유로 wire·check-out dispatch·US-J03 커버리지)·`AttendanceServiceTest`(+67 lines)) · working tree **CLEAN** · **`mvn test` develop 185/185 PASS**(51 suites, 76차 179 → +6: `J03AlimtalkServiceFlowE2eTest` + `AttendanceServiceTest` check-out dispatch) · test `2799e29` **79/79 PASS**(23 suites, Boot 3.3.1, JAR 76,466,058 B) · develop **13커밋 ahead** of test · merge **미실행**. **v1 baseline artifacts + service-layer alimtalk flow E2E PRESENT @ 32a1f8f(TSR 78차 독립 검증 PASS)** ✓ (이관 규율 5·6 PASS). **신규 Open 0건** — 판정 **BLOCK**(merge 게이트 13커밋 단일). -->
<!-- tester-sync: TSR 76차 2026-06-07T22:27 UTC (frontend) — test `@4f71543` **불변** · `npm test` **58/18 PASS** · build **86 modules** · audit **0** (독립 재실측 CONFIRMED) · develop `c5708c7`(+1 vs 75차 `a627c6d`: UXD-39 Must 흐름 UI 보강) CLEAN · develop `npm test` **115/40 PASS** · build **120 modules** · audit **0** · develop **9커밋 ahead** · 이관 규율 5 PRESENT · SEC-005 **0건** · **신규 Open 0건** · **PASS**(v1.1). 잔여 BLOCK = backend merge(12) only. -->
<!-- tester-sync: TSR 76차 2026-06-07T22:23 UTC (backend) — develop HEAD **`0832fbf`**(+1커밋 vs 74차 `8ce1151`: `feat(v2/J03): dispatch DAILY_CARE notifications for vitals`) · working tree **CLEAN** · **`mvn test` develop 179/179 PASS**(74차 178 → +1: `HealthRecordServiceTest` vitals dispatch) · test `2799e29` **79/79 PASS**(23 suites, Boot 3.3.1, JAR 76,466,058 B) · develop **12커밋 ahead** of test · merge **미실행**. **v1 baseline artifacts + vitals dispatch PRESENT @ 0832fbf(TSR 76차 독립 검증 PASS)** ✓ (이관 규율 5·6 PASS). **신규 Open 0건** — 판정 **BLOCK**(merge 게이트 12커밋 단일). -->
<!-- tester-sync: TSR 75차 2026-06-07T21:24 UTC (frontend) — test `@4f71543` **불변** · `npm test` **58/18 PASS** · build **86 modules** · audit **0** (독립 재실측 CONFIRMED) · develop `a627c6d`(+2 vs 73차 `9bdf59f`: `6f3f746` 수기 출석(US-E01·E02) · `a627c6d` US-E03 QR·US-E05 출석 통계 API) CLEAN · develop `npm test` **110/36 PASS** · build **117 modules** · audit **0** · develop **8커밋 ahead** of test · 이관 규율 5 — ProtectedRoute·services.js·SideNav·pilotChecklist·liveConfig·AuthContext **PRESENT** · SEC-005 **0건** · **신규 Open 0건** · **PASS**(v1.1). -->
<!-- tester-sync: TSR 74차 2026-06-07T21:20 UTC (backend) — develop HEAD **`8ce1151`**(+1커밋 vs 72차 `c53dd3b`: `feat(v2/J03): add notification history query index (V46)` — `V46__notification_history_query_index.sql`(9 lines — idx_notifications_org_recipient_created)) CLEAN · `mvn test` **178/178 PASS**(50 suites, V46 tests 없음) · test `2799e29` **79/79 PASS**(23 suites, Boot 3.3.1, JAR 76,466,058 B) · develop **11커밋 ahead** of test · merge **미실행** · v1 baseline + V45 + V46 + notification history APIs develop HEAD PRESENT(TSR 74차 독립 검증 PASS) · **신규 Open 0건** · BLOCK(merge 게이트 11커밋 단일). -->
<!-- tester-sync: TSR 73차 2026-06-07T20:21 UTC (frontend) — test `@4f71543` **불변** · `npm test` **58/18 PASS** · build **86 modules** · audit **0** · develop `9bdf59f`(+2 vs 52차 `42f48e1`: `a68f150` GuardianCheckinPage DS FilterChips · `9bdf59f` P0 CRUD E2E·입금 모달·보호자 초대/수정) CLEAN · develop **6커밋 ahead** of test · 이관 규율 5 — ProtectedRoute·services.js·SideNav·pilotChecklist·liveConfig·AuthContext **PRESENT** · SEC-005 **0건** · **신규 Open 0건** · **PASS**(v1.1). -->
<!-- tester-sync: TSR 72차 2026-06-07T20:10 UTC (backend) — develop HEAD **`c53dd3b`**(+1커밋 vs 70차 `78e8928`: `feat(v2/J03): add guardian and staff notification history APIs`) · working tree **CLEAN** · **`mvn test` develop 178/178 PASS**(70차 171 → +7: `NotificationHistoryServiceTest` + `MustApiEndpointRoutingTest` 알림 이력 케이스) · test `2799e29` **79/79 PASS**(23 suites, Boot 3.3.1, JAR 76,466,058 B) · develop **10커밋 ahead** of test · merge **미실행**. **v1 baseline artifacts + 신규 notification history API PRESENT @ c53dd3b(TSR 독립 검증 PASS)**: `pilot/PilotChecklistJwtE2eTest`·`routing/MustApiEndpointRoutingTest`·`security/ProductionSecretValidatorTest`·`security/SevenRoleJwtLoginE2eTest`·`security/RoleBasedControllerAccessTest`·`auth/domain/AuthRateLimitService`+Test·`V45`·`notification/domain/NotificationAlimtalkDispatchE2eTest`·`notification/config/NotificationConfigTest`·`health/domain/HealthRecordServiceTest`·`notification/api/GuardianNotificationHistoryController`·`notification/api/StaffClientNotificationHistoryController`·`notification/domain/NotificationHistoryService`+Test **전부 PRESENT** ✓ (이관 규율 5·6 PASS). **신규 Open 0건** — 판정 **BLOCK**(merge 게이트 10커밋 단일). -->
<!-- tester-sync: TSR 71차 2026-06-07T19:20 UTC (frontend) — test `@4f71543` **불변** · `npm test` **58/18 PASS** · build **86 modules** · audit **0** · develop `42f48e1`(+2 vs 69차 `e0eaf32`: `0d83a42` UXD 15 missing pages(US-D01·E03-E05·F04·G01-G07·H01-H04·B01·A01) · `42f48e1` P0 page-flow tests·module coverage KPI·title 정렬) CLEAN · `npm test` **89/28 PASS** · build **114 modules** · audit **0** · 이관 규율 5 — ProtectedRoute·services.js·SideNav·pilotChecklist·liveConfig·AuthContext **PRESENT** · SEC-005 **0건** · **신규 Open 0건** · **PASS**(v1.1). -->
<!-- tester-sync: TSR 70차 2026-06-07T19:05 UTC (backend) — develop HEAD **`78e8928`**(+1커밋 vs 68차 `44e0f02`: `feat(v2/J03): dispatch DAILY_CARE alimtalk on medication records`) · working tree **CLEAN** · **`mvn test` develop 171/171 PASS**(68차 170 → +1: `HealthRecordServiceTest` DAILY_CARE dispatch) · test `2799e29` **79/79 PASS**(23 suites) · develop **9커밋 ahead** of test · merge **미실행**. **v1 baseline artifacts PRESENT @ 78e8928(TSR 독립 검증 PASS)**: `pilot/PilotChecklistJwtE2eTest`·`routing/MustApiEndpointRoutingTest`·`security/ProductionSecretValidatorTest`·`security/SevenRoleJwtLoginE2eTest`·`security/RoleBasedControllerAccessTest`·`auth/domain/AuthRateLimitService`+Test·`V45`·`notification/domain/NotificationAlimtalkDispatchE2eTest`·`notification/config/NotificationConfigTest`·`health/domain/HealthRecordServiceTest` **전부 PRESENT** ✓ (이관 규율 5·6 PASS). **신규 Open 0건** — 판정 **BLOCK**(merge 게이트 9커밋 단일). -->
<!-- tester-sync: TSR 69차 2026-06-07T18:12 UTC (frontend) — v1.1 merge 완료 test `@4f71543` · `npm ci`+`npm test` **58/18 PASS** · build **86 modules** · audit **0** · develop `e0eaf32`(+2 v1.2 CLEAN) · develop `npm test` **82/27 PASS** · ROADMAP v1.1 **merged** · 이관 규율 5 PRESENT · Open 0 · **PASS**(v1.1). -->
<!-- tester-sync: TSR 68차 2026-06-07T18:07 UTC (backend) — develop HEAD **`44e0f02`**(+1커밋 vs 66차 `c221531`: `Ensure quiet hours clock is provided and add coverage`) · working tree **CLEAN** · **`mvn test` develop 170/170 PASS**(66차 169 → +1: `NotificationConfigTest`) · test `2799e29` **79/79 PASS**(23 suites) · develop **8커밋 ahead** of test · merge **미실행**. **v1 baseline artifacts PRESENT @ 44e0f02(TSR 독립 검증 PASS)**: `pilot/PilotChecklistJwtE2eTest`·`routing/MustApiEndpointRoutingTest`·`security/ProductionSecretValidatorTest`·`security/SevenRoleJwtLoginE2eTest`·`security/RoleBasedControllerAccessTest`·`auth/domain/AuthRateLimitService`+Test·`V45`·`notification/domain/NotificationAlimtalkDispatchE2eTest`·`notification/config/NotificationConfigTest` **전부 PRESENT** ✓ (이관 규율 5·6 PASS). **신규 Open 0건** — 판정 **BLOCK**(merge 게이트 8커밋 단일). -->
<!-- tester-sync: TSR 67차 2026-06-07T17:31 UTC (frontend) — develop `4f71543`(+2 vs `d592a17`) CLEAN · build 86 · npm test 58/18 · audit 0 · 13 ahead · ROADMAP ready · merge 미실행 · Open 0 · BLOCK(B03/SEC-D14). -->
<!-- tester-sync: TSR 66차 2026-06-07T17:22 UTC (backend) — develop HEAD **`c221531`**(+1커밋 vs 64차 `80bdb1e`: `c221531` v2/J03 daily care·emergency health alimtalk E2E) · working tree **CLEAN** · **`mvn test` develop 169/169 PASS**(64차 158 → +11: `NotificationAlimtalkDispatchE2eTest` 7·`AttendanceServiceTest` +1·`BillingServiceTest` +1) · test `2799e29` **79/79 PASS**(23 suites) · develop **7커밋 ahead** of test · merge **미실행**. **v1 baseline artifacts PRESENT @ c221531(TSR 독립 검증 PASS)**: `pilot/PilotChecklistJwtE2eTest`·`routing/MustApiEndpointRoutingTest`·`security/ProductionSecretValidatorTest`·`security/SevenRoleJwtLoginE2eTest`·`security/RoleBasedControllerAccessTest`·`auth/domain/AuthRateLimitService`+Test·`V45` **전부 PRESENT** ✓ (이관 규율 5·6 PASS). **신규 Open 0건** — 판정 **BLOCK**(merge 게이트 7커밋 단일). -->
<!-- tester-sync: TSR 65차 2026-06-07T16:50 UTC (frontend) — develop HEAD **`d592a17`**(+3커밋 vs 63차 `bb0cec4`: `7170b2a` guardian portal REST+J01/J02 tests·`449cd4f` tone Alert live region·PublicAuthLayout h1/skip-link(US-J01)·`d592a17` **FE-22** Must P1–P8·J01/J02 live E2E harness) · working tree **CLEAN** · develop `npm run build` **75 modules PASS**(vite 6.4.3, JS 209.19 kB) · develop `npm test` **46/13 PASS**(vitest 4.1.8, 63차 37/9 → +9/+4) · develop `npm audit` **0 vulnerabilities** · test `@e5fd48d` build **36 PASS**·npm test **N/A**·audit **2 moderate** · develop **11커밋 ahead** of test · merge **미실행**. **이관 규율 5 PASS @ `d592a17`**: `git cat-file -e HEAD:` `services.js`·`GuardianPortalPage.jsx`(+test)·`ClientDetailPage.jsx`·`Alert.jsx`·`PublicAuthLayout.jsx`·`pilotChecklist`·`pilotPageFlows`·`sevenRoleRouteMatrix`·`ProtectedRoute.jsx` + `src/e2e/pilotLiveApi.e2e.test.js`·`pilotLivePages.e2e.test.jsx`·`guardianLiveApi.e2e.test.js`·`liveConfig.js`·`vitest.live.config.js` **전부 PRESENT**. SEC-005 localStorage/sessionStorage **0건**. **FE-22 게이팅**: `src/e2e/**` 는 `vite.config.js` test `exclude` → 기본 `npm test` 제외, 별도 `test:live-e2e`(`LIVE_E2E=1`)로만 실행 — 실 live run 은 develop→test merge·backend v1 test 승격(SEC-D14) 후. **신규 Open 0건** — 판정 **BLOCK**(B03/SEC-D14 frontend merge 게이트 단일 — develop→test 11커밋 미머지 + Must·J01/J02 라이브 E2E run). -->
<!-- tester-sync: TSR 64차 2026-06-07T16:30 UTC (backend) — develop HEAD **`80bdb1e`**(+2커밋 vs 62차 `136239e`: `8d42bdd` BE-11 AuthRateLimitService·`80bdb1e` V45 v2 notification integrity) · working tree **CLEAN** · **`mvn test` develop 158/158 PASS**(+6 vs 62차 152 — BE-11 AuthRateLimitServiceTest·V45 포함) · test `2799e29` **79/79 PASS**(23 suites) · develop **6커밋 ahead** of test · merge **미실행**. **BE-11 develop HEAD Fixed(TSR 64차 독립 검증 PASS)**: `auth/domain/AuthRateLimitService`·`auth/domain/AuthRateLimitServiceTest` **PRESENT** @ `8d42bdd`(이관 규율 5·6 PASS). **V45 PRESENT** @ `80bdb1e` — `V45__v2_notification_prefs_integrity_and_users_phone_pair.sql` HEAD **PRESENT**. v1 baseline artifacts **전부 PRESENT** — `pilot/PilotChecklistJwtE2eTest`·`routing/MustApiEndpointRoutingTest`·`security/ProductionSecretValidatorTest`·`security/SevenRoleJwtLoginE2eTest`·`security/RoleBasedControllerAccessTest`. **신규 Open 0건** — 판정 **BLOCK**(merge 게이트 6커밋 단일). **SEC-20260608-014(BE-11) Planned→Fixed** @ `8d42bdd`. -->
# 테스트 리포트 (TEST_REPORT)

> **작성**: tester (`TSR`)  
> **검증 브랜치**: backend `test` worktree (`src/backend-test`), frontend `test` worktree (`src/frontend-test`)  
> **ROADMAP 기준**: v1 backend (`merge_status: merged`), v1.1 frontend (`merge_status: merged`)  
> **CURRENT BASELINE**: backend develop `1ec538b` (v1.3-A client transport profile US-T01, 92차 backend) · frontend test `c510f5c` (v1.2 merged) · frontend develop `637b9b3` (v1.3-A pilotPageFlows T01~T03 E2E + UXD-49 HQ 대시보드 건강 이상 지점명, 92차 frontend)

> **92차 재검증 (2026-06-08T09:13 UTC, frontend) — test `@c510f5c` 불변·143/46 PASS·125 modules·audit 0·develop `637b9b3`(+2 UXD-49·v1.3-A T01~T03 E2E CLEAN)·189/60 PASS·766 modules·PASS(v1.2)·v1.3 pending·v3 develop-only**:
> - **frontend test HEAD `c510f5c`** 불변(v1.2 merged) — working tree **CLEAN**. ROADMAP v1.2 frontend `merge_status: merged` 부합.
> - **`src/frontend-test` `npm test`**: **143 tests/46 files PASS** (vitest 4.1.8) — 92차 독립 실측 (91차와 동일).
> - **`src/frontend-test` `npm run build`**: **125 modules SUCCESS** (vite 6.4.3, JS 320.10 kB gzip 91.25 kB, CSS 31.03 kB gzip 5.84 kB) — 92차 독립 실측.
> - **`src/frontend-test` `npm audit`**: **0 vulnerabilities** — 92차 독립 실측.
> - **`git cat-file -e HEAD:`** (test) `ProtectedRoute.jsx`·`services.js`·`SideNav.jsx`·`pilotChecklist.js`·`AuthContext.jsx`·`ReconciliationPage.jsx` **전부 PRESENT** ✓ (이관 규율 5 PASS). SEC-005 localStorage/sessionStorage **0건**.
> - **frontend develop HEAD `637b9b3`** (+2 vs 91차 `8a764df`: `00375f6` `feat(uxd-49): HQ 통합 대시보드 건강 이상 목록 지점명 표시 (US-H02)` · `637b9b3` `feat(v1.3-A): pilotPageFlows transport US-T01~T03 E2E + pilotChecklist T01~T03`), working tree **CLEAN** (0 dirty).
> - **`8a764df..637b9b3` 변경**(추가 2커밋): UXD-49 HQ 통합 대시보드 건강 이상 목록 지점명 표시(US-H02) + v1.3-A transport US-T01~T03 pilotPageFlows E2E·pilotChecklist T01~T03.
> - develop `npm test`: **189/60 PASS**(vitest 4.1.8, +6/0 vs 91차 183/60: v1.3-A transport pilotPageFlows T01~T03 회귀) · develop `npm run build`: **766 modules SUCCESS**(vite 6.4.3, JS 756.46 kB gzip 210.03 kB, CSS 34.96 kB — **vite >500 kB 경고, non-blocking LOW**) · develop `npm audit`: **0 vulnerabilities** — 92차 실측.
> - **v1.3-A·v3·UXD-49·T01~T03 E2E 산출물 develop HEAD PRESENT** ✓ · KAKAO 키 `import.meta.env.VITE_KAKAO_MAP_JS_KEY`(하드코딩 0) · `MAX_TRANSPORT_STOPS=15`.
> - develop **12커밋 ahead** of test (91차 10 → +2) — v1.3-A·v3 WIP, non-blocking.
> - **신규 Open 0건** — 판정 **PASS**(v1.2). **v1.3 이관 게이트 미충족(pending)** — backend transport API(test 미승격)·US-T01~T03 live E2E 잔여(pilotPageFlows develop PRESENT). **v3(+UXD-48·UXD-49) develop-only** — ROADMAP merge 게이트 미설정(정상). 잔여 BLOCK = backend merge(21) + SEC-D14 + post-merge live E2E(결정 73).

> **92차 재검증 (2026-06-08T09:00 UTC, backend) — develop `1ec538b` CLEAN·v1.3-A client transport profile(US-T01)·231/231 PASS·test 79/79·21커밋 ahead·BLOCK(merge 게이트 단일)**:
> - **develop HEAD `1ec538b`** (+1커밋 vs 91차 `767d977`: `feat(v1.3-A): expose client transport profile on Clients API (US-T01)`) — working tree **CLEAN** (0 dirty).
> - **변경 파일 6종** (+286/-6): `ClientResponse.java`(+5 — usesTransport·pickupAddress·pickupContact·defaultPickupTime 필드)·`CreateClientRequest.java`(+7)·`UpdateClientRequest.java`(+7)·`ClientService.java`(+52 — transport profile create/update 처리·pickup geocode 캐시 무효화)·`ClientServiceTest.java`(+176 — 기존 7→9 @Test, transport profile 단위 테스트)·`PilotChecklistJwtE2eTest.java`(+45 — transport roster·run detail endpoint 라우팅 smoke test).
> - **`mvn test` (develop HEAD)**: **231/231 PASS** (62 suites, 91차 226 → +5: `ClientServiceTest` +2·`PilotChecklistJwtE2eTest` +3) — 92차 독립 실측.
> - **`mvn test` (test `@2799e29`)**: **79/79 PASS** (23 suites, Boot 3.3.1, JAR 76,466,058 B) — 불변.
> - **develop 21커밋 ahead** of test (`f47ffa1`~`1ec538b`) — merge **미실행**.
> - **artifact PRESENT (이관 규율 5·6)**: `pilot/PilotChecklistJwtE2eTest`·`routing/MustApiEndpointRoutingTest`·`security/ProductionSecretValidatorTest`·`security/SevenRoleJwtLoginE2eTest`·`security/RoleBasedControllerAccessTest`·`transport/api/TransportController`·`transport/domain/TransportService`·`transport/domain/TransportServiceTest`·`transport/api/TransportControllerRoutingTest`·`meals/api/MealController`·`programs/api/ProgramController`·`db/migration/V47`·`V48`·`V49`·`clients/api/ClientResponse`(transport profile)·`clients/domain/ClientService`(geocode 캐시 무효화)·`clients/domain/ClientServiceTest`(9 @Test) **전부 PRESENT** ✓.
> - **US-T01 backend 완료**: Clients API 에 usesTransport·pickupAddress·pickupContact·defaultPickupTime 노출 — frontend에서 transport roster 설정 가능. US-T02(unconfirm UI 연동)·US-T03 live E2E 잔여.
> - **신규 Open 0건** — 판정 **BLOCK** (merge 게이트 21커밋 단일). v3 develop-only(ROADMAP v3 미정의).

> **91차 재검증 (2026-06-08T08:05 UTC, frontend) — test `@c510f5c` 불변·143/46 PASS·125 modules·audit 0·develop `8a764df`(+1 UXD-48 CLEAN)·183/60 PASS·766 modules·PASS(v1.2)·v1.3 pending·v3 develop-only**:
> - **frontend test HEAD `c510f5c`** 불변(v1.2 merged) — working tree **CLEAN**. ROADMAP v1.2 frontend `merge_status: merged` 부합.
> - **`src/frontend-test` `npm test`**: **143 tests/46 files PASS** (vitest 4.1.8) — 91차 독립 실측 (90차와 동일).
> - **`src/frontend-test` `npm run build`**: **125 modules SUCCESS** (vite 6.4.3, JS 320.10 kB gzip 91.25 kB, CSS 31.03 kB gzip 5.84 kB) — 91차 독립 실측.
> - **`src/frontend-test` `npm audit`**: **0 vulnerabilities** — 91차 독립 실측.
> - **`git cat-file -e HEAD:`** (test) `ProtectedRoute.jsx`·`services.js`·`SideNav.jsx`·`pilotChecklist.js`·`AuthContext.jsx`·`ReconciliationPage.jsx` **전부 PRESENT** ✓ (이관 규율 5 PASS). SEC-005 localStorage/sessionStorage **0건**.
> - **frontend develop HEAD `8a764df`** (+1 vs 90차 `73f7d39`: `feat(uxd-48): Recharts 차트 레이어 복원·대시보드/출석/건강 연동 (US-H01/E05/F04/H02)` — `ChartContainer`(+test)·`AttendanceRateChart`(+test)·`BranchCompareChart`·`HealthTrendChart`·`chartColors.js`·`DashboardPage`·`AttendanceStatsPage`·`HealthDetailPage`), working tree **CLEAN** (0 dirty).
> - **`73f7d39..8a764df` 변경 내역**(17 files, +877/-16): UXD-48 Recharts 차트 컴포넌트·대시보드/출석통계/건강 상세 페이지 연동.
> - develop `npm test`: **183/60 PASS**(vitest 4.1.8, 90차 179/58 → +4/+2: `ChartContainer`·`AttendanceRateChart` 회귀) · develop `npm run build`: **766 modules SUCCESS**(vite 6.4.3, JS 756.06 kB gzip 209.97 kB, CSS 34.91 kB gzip 6.37 kB — **vite >500 kB 경고, non-blocking LOW**) · develop `npm audit`: **0 vulnerabilities** — 91차 실측.
> - **v1.3-A·v3·unconfirm·Recharts 산출물 develop HEAD PRESENT** ✓ — Transport·Meals/Programs·StaffPage·TransportUnconfirmModal·ChartContainer·KAKAO 키 `import.meta.env.VITE_KAKAO_MAP_JS_KEY`(하드코딩 0) · `MAX_TRANSPORT_STOPS=15`.
> - develop **10커밋 ahead** of test (90차 9 → +1) — v1.3-A·v3 WIP, non-blocking(v1.2 검증에 무영향).
> - **신규 Open 0건** — 판정 **PASS**(v1.2 test `c510f5c` 검증 완료).
> - **v1.3 이관 게이트 미충족(pending)**: backend v1.3-A transport API(develop `767d977` PRESENT·**test 미승격**)·US-T01~T03 **라이브 E2E** 잔여. unconfirm UI develop HEAD **PRESENT** @ `73f7d39`. **v3(+UXD-48 Recharts) develop-only** — ROADMAP v3 merge 게이트 미정의(planner 정의 대기, 정상).
> - 잔여 BLOCK: backend develop→test merge(20) + SEC-D14 + post-merge live E2E(결정 73). frontend v1.2 = **PASS**, v1.3 = **pending**, v3 = **develop-only**.

> **91차 재검증 (2026-06-08T08:00 UTC, backend) — develop `767d977` 불변·CLEAN·develop 226/226·test 79/79·develop 20커밋 ahead·merge 미실행·BLOCK(merge 게이트 단일)**:
> - **backend develop HEAD `767d977`** (89차 대비 **불변** — `fix(v1.3-A): align transport unconfirm route with PATCH contract`), working tree **CLEAN** (0 dirty).
> - **`src/backend` develop HEAD `mvn test`**: **226/226 PASS** (62 suites, 0 failures) — 91차 독립 실측.
> - **`src/backend-test` test `@2799e29`** 불변 — `mvn test` **79/79 PASS** (23 suites, Spring Boot 3.3.1) · JAR **76,466,058 B** — 91차 독립 실측.
> - **`git cat-file -e HEAD:`** v1 baseline + v1.3-A transport(unconfirm PATCH+POST) + v3 meals/programs artifacts **전부 PRESENT** ✓ (이관 규율 5·6 PASS).
> - develop **20커밋 ahead** of test — develop→test merge **미실행**.
> - **신규 Open 0건** — 판정 **BLOCK**(merge 게이트 20커밋 단일). 잔여: develop→test merge(20) + SEC-D14.
> - **교차 관측(frontend 90차)**: `TransportUnconfirmModal`·US-T02 unconfirm UI develop `73f7d39` **PRESENT** — backend test 미승격·US-T01~T03 live E2E 잔여.
> - **v3 develop-only** — ROADMAP v3 버전·merge 게이트 미정의(planner 정의 대기, 정상).

> **90차 재검증 (2026-06-08T07:08 UTC, frontend) — test `@c510f5c` 불변·143/46 PASS·125 modules·audit 0·develop `73f7d39`(+1 UXD-47 CLEAN)·179/58 PASS·143 modules·PASS(v1.2)·v1.3 pending·v3 develop-only**:
> - **frontend test HEAD `c510f5c`** 불변(v1.2 merged) — working tree **CLEAN**. ROADMAP v1.2 frontend `merge_status: merged` 부합.
> - **`src/frontend-test` `npm test`**: **143 tests/46 files PASS** (vitest 4.1.8) — 90차 독립 실측 (88차와 동일).
> - **`src/frontend-test` `npm run build`**: **125 modules SUCCESS** (vite 6.4.3, JS 320.10 kB gzip 91.25 kB, CSS 31.03 kB gzip 5.84 kB) — 90차 독립 실측.
> - **`src/frontend-test` `npm audit`**: **0 vulnerabilities** — 90차 독립 실측.
> - **`git cat-file -e HEAD:`** (test) `ProtectedRoute.jsx`·`services.js`·`SideNav.jsx`·`pilotChecklist.js`·`AuthContext.jsx`·`ReconciliationPage.jsx` **전부 PRESENT** ✓ (이관 규율 5 PASS). SEC-005 localStorage/sessionStorage **0건**.
> - **frontend develop HEAD `73f7d39`** (+1 vs 88차 `fe33e7c`: `fix(uxd-47): StaffPage 접근성·배차 확정 취소 UI (US-T02)` — `TransportUnconfirmModal`(+test)·`StaffRoleSelect`(+test)·`config/staff.js`·`StaffPage` a11y·`TransportRunDetailPage` hq_admin unconfirm 흐름·`services.js` transport unconfirm API), working tree **CLEAN** (0 dirty).
> - **`fe33e7c..73f7d39` 변경 내역**(12 files, +471/-25): UXD-47 StaffPage DS 표준 필드 검증·`StaffRoleSelect`·`TransportUnconfirmModal`(hq_admin 배차 확정 취소 US-T02)·`TransportRunDetailPage` unconfirm 연동·`TransportRunDetailPage.test.jsx`(+104 lines).
> - develop `npm test`: **179/58 PASS**(vitest 4.1.8, 88차 170/55 → +9/+3: `TransportUnconfirmModal`·`StaffRoleSelect`·`TransportRunDetailPage`·`StaffPage` 회귀) · develop `npm run build`: **143 modules SUCCESS**(vite 6.4.3, JS 354.29 kB gzip 99.15 kB, CSS 34.02 kB gzip 6.28 kB) · develop `npm audit`: **0 vulnerabilities** — 90차 실측.
> - **v1.3-A·v3·unconfirm 산출물 develop HEAD PRESENT** ✓ — Transport·Meals/Programs·StaffPage·**TransportUnconfirmModal**·KAKAO 키 `import.meta.env.VITE_KAKAO_MAP_JS_KEY`(하드코딩 0) · `MAX_TRANSPORT_STOPS=15`.
> - develop **9커밋 ahead** of test (88차 8 → +1) — v1.3-A·v3 WIP, non-blocking(v1.2 검증에 무영향).
> - **신규 Open 0건** — 판정 **PASS**(v1.2 test `c510f5c` 검증 완료).
> - **v1.3 이관 게이트 미충족(pending)**: backend v1.3-A transport API(develop `767d977` PRESENT·**test 미승격**)·US-T01~T03 **라이브 E2E** 잔여. unconfirm UI develop HEAD **PRESENT** @ `73f7d39`(88차 잔여 항목 진전). **v3(+staff·unconfirm UI) develop-only** — ROADMAP v3 merge 게이트 미정의(planner 정의 대기, 정상).
> - 잔여 BLOCK: backend develop→test merge(20) + SEC-D14 + post-merge live E2E(결정 73). frontend v1.2 = **PASS**, v1.3 = **pending**, v3 = **develop-only**.

> **89차 재검증 (2026-06-08T07:02 UTC, backend) — develop `767d977` CLEAN·v1.3-A transport unconfirm PATCH·develop 226/226·test 79/79·develop 20커밋 ahead·merge 미실행·BLOCK(merge 게이트 단일)**:
> - **backend develop HEAD `767d977`** (+1커밋 vs 87차 `0d8968d`: `fix(v1.3-A): align transport unconfirm route with PATCH contract`), working tree **CLEAN** (0 dirty).
> - **`767d977` 변경 내역**(3 files, +15/-1): `TransportController.java`(+11 — `PATCH /api/v1/transport/runs/{runId}/unconfirm` v1.3 API 계약 정합·`POST` legacy alias 유지)·`TransportControllerRoutingTest.java`(+3 — PATCH·POST dual-method RBAC)·`MustApiEndpointRoutingTest`(+2 transport unconfirm PATCH routing).
> - **`src/backend` develop HEAD `mvn test`**: **226/226 PASS** (62 suites, 0 failures, 87차 불변 — routing assertion 확장만) — 89차 독립 실측.
> - **`src/backend-test` test `@2799e29`** 불변 — `mvn test` **79/79 PASS** (23 suites, Spring Boot 3.3.1) · JAR **76,466,058 B** — 89차 독립 실측.
> - **`git cat-file -e HEAD:`** v1 baseline + v1.3-A transport(unconfirm PATCH+POST) + v3 meals/programs artifacts **전부 PRESENT** ✓ (이관 규율 5·6 PASS).
> - develop **20커밋 ahead** of test (87차 19 → +1 `767d977`) — develop→test merge **미실행**.
> - **신규 Open 0건** — 판정 **BLOCK**(merge 게이트 20커밋 단일). 잔여: develop→test merge(20) + SEC-D14.
> - **v1.3-A transport unconfirm PATCH develop-only** — frontend unconfirm UI·US-T01~T03 live E2E 잔여. **v3 develop-only** — ROADMAP v3 버전·merge 게이트 미정의(planner 정의 대기, 정상).

> **88차 재검증 (2026-06-08T06:10 UTC, frontend) — test `@c510f5c` 불변·143/46 PASS·125 modules·audit 0·develop `fe33e7c`(+8 v1.3-A·v3·UXD-46·staff CLEAN)·170/55 PASS·140 modules·PASS(v1.2)·v1.3 pending·v3 develop-only**:
> - **frontend test HEAD `c510f5c`** 불변(v1.2 merged) — working tree **CLEAN**. ROADMAP v1.2 frontend `merge_status: merged` 부합.
> - **`src/frontend-test` `npm test`**: **143 tests/46 files PASS** (vitest 4.1.8) — 88차 독립 실측 (86차와 동일).
> - **`src/frontend-test` `npm run build`**: **125 modules SUCCESS** (vite 6.4.3, JS 320.10 kB gzip 91.25 kB, CSS 31.03 kB gzip 5.84 kB) — 88차 독립 실측.
> - **`src/frontend-test` `npm audit`**: **0 vulnerabilities** — 88차 독립 실측.
> - **`git cat-file -e HEAD:`** (test) `ProtectedRoute.jsx`·`services.js`·`SideNav.jsx`·`pilotChecklist.js`·`AuthContext.jsx`·`ReconciliationPage.jsx` **전부 PRESENT** ✓ (이관 규율 5 PASS). SEC-005 localStorage/sessionStorage **0건**.
> - **frontend develop HEAD `fe33e7c`** (+8 vs `c510f5c`: 86차 `362dbf0` 대비 +2 — `762b5a8` `fix(uxd-46): 누락 CSS 유틸·인라인 style 제거·체크인 라우트 접근성` · `fe33e7c` `feat(v3): add staff management UI flow for frontend`), working tree **CLEAN** (0 dirty).
> - **`362dbf0..fe33e7c` 변경 내역**(21 files, +443/-34): UXD-46 `components.css` ds 유틸 추가·`AttendancePage`·`MealsPage`·`ProgramsPage`·`GuardianDetailPage` 인라인 style 제거·체크인 라우트 접근성 + v3 `StaffPage.jsx`(+test 75 lines)·`services.js`(+12 staff API)·`App.jsx`·`navConfig`·`roleNav`·`sevenRoleRouteMatrix`·`pilotPageFlows` staff 흐름 확장.
> - develop `npm test`: **170/55 PASS**(vitest 4.1.8, 86차 164/54 → +6/+1: `StaffPage.test.jsx`·`AttendancePage.test.jsx` UXD-46 회귀) · develop `npm run build`: **140 modules SUCCESS**(vite 6.4.3, JS 351.51 kB gzip 98.38 kB, CSS 33.97 kB gzip 6.28 kB) · develop `npm audit`: **0 vulnerabilities** — 88차 실측.
> - **v1.3-A·v3·staff 산출물 develop HEAD PRESENT** ✓ — Transport·Meals/Programs·`StaffPage`·KAKAO 키 `import.meta.env.VITE_KAKAO_MAP_JS_KEY`(하드코딩 0) · `MAX_TRANSPORT_STOPS=15`.
> - develop **8커밋 ahead** of test (86차 6 → +2) — v1.3-A·v3 WIP, non-blocking(v1.2 검증에 무영향).
> - **신규 Open 0건** — 판정 **PASS**(v1.2 test `c510f5c` 검증 완료).
> - **v1.3 이관 게이트 미충족(pending)**: backend v1.3-A transport API(develop `0d8968d` PRESENT·**test 미승격**)·US-T01~T03 라이브 E2E·transport unconfirm UI 잔여. **v3(식사·프로그램·직원) develop-only** — ROADMAP v3 버전·merge 게이트 미정의(planner 정의 대기, 정상).
> - 잔여 BLOCK: backend develop→test merge(19) + SEC-D14 + post-merge live E2E(결정 73). frontend v1.2 = **PASS**, v1.3 = **pending**, v3 = **develop-only**.

> **87차 재검증 (2026-06-08T05:58 UTC, backend) — develop `0d8968d` CLEAN·v1.3-A transport run unconfirm·develop 226/226·test 79/79·develop 19커밋 ahead·merge 미실행·BLOCK(merge 게이트 단일)**:
> - **backend develop HEAD `0d8968d`** (+1커밋 vs 85차 `dfd9be2`: `feat(v1.3-A): support transport run unconfirm flow for hq_admin`), working tree **CLEAN** (0 dirty).
> - **`0d8968d` 변경 내역**(6 files, +102 insertions): `TransportController.java`(+9 — `POST /api/v1/transport/runs/{runId}/unconfirm` hq_admin RBAC)·`TransportService.java`(+31 — `unconfirmRun` CONFIRMED→DRAFT·`unconfirmedAt`/`unconfirmedBy` 기록)·`TransportRunResponse.java`(+3)·`TransportServiceTest.java`(+46 — `unconfirmRunShouldRevertConfirmedToDraft`·`unconfirmRunShouldRejectDraftRun`)·`TransportControllerRoutingTest.java`(+7)·`MustApiEndpointRoutingTest`(+6 transport unconfirm RBAC).
> - **`src/backend` develop HEAD `mvn test`**: **226/226 PASS** (62 suites, 0 failures, 85차 224 → +2: `TransportServiceTest` unconfirm 2건) — 87차 독립 실측.
> - **`src/backend-test` test `@2799e29`** 불변 — `mvn test` **79/79 PASS** (23 suites, Spring Boot 3.3.1) · `mvn -q -DskipTests package` **SUCCESS** JAR **76,466,058 B** — 87차 독립 실측.
> - **`git cat-file -e HEAD:`** v1 baseline + v1.3-A transport(unconfirm 포함) + v3 meals/programs artifacts **전부 PRESENT** ✓ (이관 규율 5·6 PASS).
> - develop **19커밋 ahead** of test (85차 18 → +1 `0d8968d`) — develop→test merge **미실행**.
> - **신규 Open 0건** — 판정 **BLOCK**(merge 게이트 19커밋 단일). 잔여: develop→test merge(19) + SEC-D14.
> - **v1.3-A transport unconfirm develop-only** — frontend unconfirm UI·US-T01~T03 live E2E 잔여(planner/coder 후속). **v3 develop-only** — ROADMAP v3 버전·merge 게이트 미정의(planner 정의 대기, 정상).

> **85차 재검증 (2026-06-08T04:55 UTC, backend) — develop `dfd9be2` CLEAN·v3 meals/programs REST API·Flyway V49·develop 224/224·test 79/79·develop 18커밋 ahead·merge 미실행·BLOCK(merge 게이트 단일)**:
> - **backend develop HEAD `dfd9be2`** (+1커밋 vs 83차 `53a1ffe`: `feat(v3): add meals and programs REST API with Flyway V49 schema`), working tree **CLEAN** (0 dirty).
> - **`dfd9be2` 변경 내역**(28 files, +2265 insertions): `meals/api/MealController.java`(54)·`meals/domain/MealService.java`(179)·`meals/persistence/MealMenuEntity.java`(132)·`MealRecordEntity.java`(154)+Repository 2종·meals DTO 6종·`programs/api/ProgramController.java`(56)·`programs/domain/ProgramService.java`(249)·`programs/persistence/ActivityProgramEntity.java`(155)·`ProgramParticipationEntity.java`(143)+Repository 2종·programs DTO 6종·`db/migration/V49__meals_programs_v3_schema.sql`(403 — meal_menus·meal_records·activity_programs·program_participations)·`meals/domain/MealServiceTest.java`(146)·`meals/api/MealControllerRoutingTest.java`(67)·`programs/domain/ProgramServiceTest.java`(171)·`programs/api/ProgramControllerRoutingTest.java`(67)·`routing/MustApiEndpointRoutingTest.java`(+100 meals/programs RBAC nested).
> - **`src/backend` develop HEAD `mvn test`**: **224/224 PASS** (62 suites, 0 failures, 83차 212 → +12: `MealServiceTest` + `MealControllerRoutingTest` + `ProgramServiceTest` + `ProgramControllerRoutingTest` + `MustApiEndpointRoutingTest` meals/programs) — 85차 독립 실측 (surefire 집계).
> - **`src/backend-test` test `@2799e29`** 불변 — `mvn test` **79/79 PASS** (23 suites, Spring Boot 3.3.1) · `mvn -q -DskipTests package` **SUCCESS** JAR **76,466,058 B** — 85차 독립 실측.
> - **`git cat-file -e HEAD:`** v1 baseline(`pilot/PilotChecklistJwtE2eTest`·`routing/MustApiEndpointRoutingTest`·`security/ProductionSecretValidatorTest`·`security/SevenRoleJwtLoginE2eTest`·`security/RoleBasedControllerAccessTest`) + v1.3-A(`transport/api/TransportController`·`transport/domain/TransportService`·`transport/domain/KakaoGeocodeClient`·`V47`·`V48`) + v3(`meals/api/MealController`·`meals/domain/MealService`·`meals/domain/MealServiceTest`·`meals/api/MealControllerRoutingTest`·`programs/api/ProgramController`·`programs/domain/ProgramService`·`programs/domain/ProgramServiceTest`·`programs/api/ProgramControllerRoutingTest`·`V49`) **전부 PRESENT** ✓ (이관 규율 5·6 PASS).
> - develop **18커밋 ahead** of test (83차 17 → +1 `dfd9be2`) — develop→test merge **미실행**.
> - **신규 Open 0건** — 판정 **BLOCK**(merge 게이트 18커밋 단일). 잔여: develop→test merge(18) + SEC-D14.
> - **v3(식사·프로그램) develop-only** — ROADMAP v3 `status`/`merge_status`·완료 기준·merge 게이트 **미정의**(planner 정의 대기). 이제 v3 backend API(`dfd9be2`) + v3 frontend UI 셸(`7ef1083` MealsPage·ProgramsPage)이 양 스트림 develop에 존재 → planner: ROADMAP v3 버전·USER_STORIES(식사 §3-5·프로그램 §3-6)·API_SPEC v3 정의 + 연동 E2E 계획 권장. 현 단계 정상(결함 아님).
>
> **83차 재검증 (2026-06-08T03:40 UTC, backend) — develop `53a1ffe` CLEAN·v1.3-A transport API·Flyway V47/V48·Kakao geocode proxy·develop 212/212·test 79/79·develop 17커밋 ahead·merge 미실행·BLOCK(merge 게이트 단일)**:
> - **backend develop HEAD `53a1ffe`** (+1커밋 vs 82차 `52e0621`: `feat(v1.3-A): add transport API, Flyway schema, and Kakao geocode proxy`), working tree **CLEAN** (0 dirty).
> - **`53a1ffe` 변경 내역**(30 files, +2233 insertions): `TransportController.java`(98 lines — roster·runs CRUD·confirm RBAC·15-stop 검증)·`TransportService.java`(409 lines)·`KakaoGeocodeClient.java`(103 lines — Kakao geocode proxy)·`TransportGeocodeService.java`(124 lines)·`TransportRunEntity.java`(165 lines)·`TransportRunStopEntity.java`(155 lines)·DTOs 8종·`TransportConfig`/`TransportProperties`·`V47__transport_v1_3_a.sql`(326 lines — transport_runs·stops·geocode_cache)·`V48__client_ltc_grade_history.sql`(85 lines)·`ClientEntity.java`(145 lines, ltcGrade 추가)·`ClientRepository.java`(+15)·`TransportServiceTest.java`(210 lines)·`TransportControllerRoutingTest.java`(100 lines — DRAFT/CONFIRMED RBAC 라우팅)·`MustApiEndpointRoutingTest`(+79 — TransportRouting nested class)·`application.yml`(+2 kakao.geocode).
> - **`src/backend` develop HEAD `mvn test`**: **212/212 PASS** (56 suites, 0 failures, 82차 202 → +10: `TransportServiceTest` + `TransportControllerRoutingTest` + `MustApiEndpointRoutingTest$TransportRouting`) — 83차 독립 실측.
> - **`src/backend-test` test `@2799e29`** 불변 — `mvn test` **79/79 PASS** (23 suites, Spring Boot 3.3.1) · `mvn -q -DskipTests package` **SUCCESS** JAR **76,466,058 B** — 83차 독립 실측.
> - **`git cat-file -e HEAD:`** v1 baseline(`PilotChecklistJwtE2eTest`·`MustApiEndpointRoutingTest`·`ProductionSecretValidatorTest`·`SevenRoleJwtLoginE2eTest`·`RoleBasedControllerAccessTest`) + `AuthRateLimitService`+Test + `V45`·`V46` + notification history/dispatch + `AlimtalkTemplateVariables`·`AlimtalkFallbackText`+Test + `NotificationEventType`·`NotificationTemplateCodes` + `BillingService`+Test + `TransportController`·`TransportService`·`KakaoGeocodeClient`·`V47`·`V48`·`TransportServiceTest`·`TransportControllerRoutingTest` **전부 PRESENT** ✓ (이관 규율 5·6 PASS).
> - develop **17커밋 ahead** of test (82차 16 → +1 `53a1ffe`) — develop→test merge **미실행**.
> - **신규 Open 0건** — 판정 **BLOCK**(merge 게이트 17커밋 단일). 잔여: develop→test merge(17) + SEC-D14. planner: `53a1ffe` v1.3-A transport backend API 완료 → ROADMAP v1.3·US-T01~T03·API_SPEC v1.3-A 갱신 권장 (frontend UI 셸 `e8d1854` 기 연동 준비 완료).

> **82차 재검증 (2026-06-08T02:30 UTC, backend) — develop `52e0621` CLEAN·v2/J03 copay claim PAID alimtalk dispatch·develop 202/202·test 79/79·develop 16커밋 ahead·merge 미실행·BLOCK(merge 게이트 단일)**:
> - **backend develop HEAD `52e0621`** (+1커밋 vs 80차 `ac17ad8`: `feat(v2/J03): dispatch alimtalk when copay claim is marked PAID`), working tree **CLEAN** (0 dirty).
> - **`52e0621` 변경 내역**(11 files, +159/-16): `NotificationEventType.java`(+1 — `BILLING_PAYMENT_RECEIVED` 이벤트 타입, `notifyBilling` consent 재사용)·`NotificationTemplateCodes.java`(+1)·`application.yml`(+1 — `KAKAO_TPL_BILLING_PAYMENT` 템플릿 매핑)·`BillingService.java`(+17 — copay claim CONFIRMED→PAID 전환 시 보호자 `BILLING_PAYMENT_RECEIVED` 알림톡 디스패치)·`AlimtalkFallbackText.java`(+25 — 결제 수신 SMS fallback 본문)·`AlimtalkTemplateVariables.java`(+3)·`BillingServiceTest.java`(+62)·`AlimtalkFallbackTextTest.java`(+12)·`AlimtalkTemplateVariablesTest.java`(+16)·`J03AlimtalkServiceFlowE2eTest.java`(+34).
> - **`src/backend` develop HEAD `mvn test`**: **202/202 PASS** (53 suites, 0 failures, 80차 198 → +4: `BillingServiceTest` copay PAID dispatch + alimtalk 변수·fallback·service-flow E2E 확장) — 82차 독립 실측.
> - **`src/backend-test` test `@2799e29`** 불변 — `mvn test` **79/79 PASS** (23 suites, Spring Boot 3.3.1) · `mvn -q -DskipTests package` **SUCCESS** JAR **76,466,058 B** — 82차 독립 실측.
> - **`git cat-file -e HEAD:`** v1 baseline(`PilotChecklistJwtE2eTest`·`MustApiEndpointRoutingTest`·`ProductionSecretValidatorTest`·`SevenRoleJwtLoginE2eTest`·`RoleBasedControllerAccessTest`) + `AuthRateLimitService`+Test + `V45`·`V46` + notification history/dispatch + `AlimtalkTemplateVariables`·`AlimtalkFallbackText`+Test + `NotificationEventType`·`NotificationTemplateCodes` + `BillingService`+Test **전부 PRESENT** ✓ (이관 규율 5·6 PASS).
> - develop **16커밋 ahead** of test (80차 15 → +1 `52e0621`) — develop→test merge **미실행**.
> - **신규 Open 0건** — 판정 **BLOCK**(merge 게이트 16커밋 단일). 잔여: develop→test merge(16) + SEC-D14. planner: `52e0621` BILLING_PAYMENT_RECEIVED copay-claim PAID alimtalk dispatch → ROADMAP·USER_STORIES(US-J03)·API_SPEC v2/J03 follow-up 갱신 권장.

> **82차 재검증 (2026-06-08T02:37 UTC, frontend) — v1.2 develop→test merge 완료·test `c510f5c`·143/46 PASS·125 modules·audit 0·develop `e8d1854`(+2 v1.3-A CLEAN)·150/50 PASS·133 modules·PASS(v1.2)·v1.3 in_progress(pending)**:
> - **frontend test HEAD `c510f5c`** (81차 `4f71543` → **v1.2 develop→test merge 완료**), working tree **CLEAN**. ROADMAP v1.2 frontend `merge_status: merged` 부합(59차 baseline).
> - **`src/frontend-test` `npm ci`**: 0 vulnerabilities · **`npm test`**: **143 tests/46 files PASS** (vitest 4.1.8) — 82차 독립 실측 (81차 test 58/18 → v1.2 흡수 후 +85/+28).
> - **`src/frontend-test` `npm run build`**: **125 modules SUCCESS** (vite 6.4.3, JS 320.10 kB gzip 91.25 kB, CSS 31.03 kB gzip 5.84 kB) — 82차 독립 실측.
> - **`src/frontend-test` `npm audit`**: **0 vulnerabilities** — 82차 독립 실측.
> - **`git cat-file -e HEAD:`** (test `c510f5c`) `ProtectedRoute.jsx`·`services.js`·`SideNav.jsx`·`pilotChecklist.js`·`liveConfig.js`·`AuthContext.jsx`·`ReconciliationPage.jsx` **전부 PRESENT** ✓ (이관 규율 5 PASS). SEC-005 `AuthContext.jsx` localStorage/sessionStorage **0건**.
> - **frontend develop HEAD `e8d1854`** (+2 vs 81차 `c510f5c`: `f01e3a8` `feat(uxd-43): US-G06 UNMATCHED 후보 이용자 검색 UI 보강` · `e8d1854` `feat(v1.3): add transport pickup dispatch UI shell (US-T01~T03)`), working tree **CLEAN** (0 dirty).
> - **`c510f5c..e8d1854` 변경 내역**(20 files, +1483/-11): v1.3-A `src/pages/TransportPage.jsx`(+test)·`TransportRunNewPage.jsx`·`TransportRunDetailPage.jsx`·`transportUtils.js`(+test)·`src/components/transport/KakaoTransportMap.jsx`·`TransportStopList.jsx`(+test)·`TransportDisclaimer.jsx`·`src/config/transport.js`·`navConfig.js`·`roleNav.js`·`App.jsx`·`services.js`(+41)·`sevenRoleRouteMatrix.js`·`components.css`(+150) + US-G06 `ReconciliationPage.jsx`(+test) UNMATCHED 후보 검색.
> - develop `npm test`: **150/50 PASS**(vitest 4.1.8, test 143/46 → +7/+4: TransportPage·TransportStopList·transportUtils·ReconciliationPage UNMATCHED 회귀) · develop `npm run build`: **133 modules SUCCESS**(vite 6.4.3, JS 334.18 kB gzip 94.86 kB, CSS 33.35 kB) · develop `npm audit`: **0 vulnerabilities** — 82차 실측.
> - **v1.3-A 산출물 develop HEAD PRESENT** ✓ — `TransportPage`·`TransportRunNewPage`·`TransportRunDetailPage`·`KakaoTransportMap`·`TransportDisclaimer`·`transport.js`·`transportUtils` 전부 `git cat-file -e HEAD:` PASS. 운영 고지 배너(BNK-7 §10-3 「운영 편의용·이동서비스비 청구·평가 일지(G15) 미포함」 + BNK-8 「케어포 이동서비스 지도보기 동등·경로 최적화 v1.3-B」) PRESENT · `MAX_TRANSPORT_STOPS=15` 상수 · Kakao 지도 키 `import.meta.env.VITE_KAKAO_MAP_JS_KEY`(하드코딩 0건·키 누락 시 graceful 처리).
> - develop **2커밋 ahead** of test — v1.3-A WIP, non-blocking(v1.2 검증에 무영향).
> - **신규 Open 0건** — 판정 **PASS**(v1.2 test `c510f5c` 검증 완료).
> - **v1.3 이관 게이트 미충족(pending)**: ROADMAP v1.3 `status: in_progress`·`merge_status: pending`. v1.3-A develop는 **frontend UI 셸 한정** — 완료 기준 중 DBA `transport_runs`/`stops` 스키마·roster/runs CRUD·**confirm** API·RBAC(DRAFT=hq_admin/CONFIRMED=직원 read)·Geocoding **서버 프록시**·US-T01~T03 라이브 E2E **미완**(backend 의존). v1.3 merge는 backend v1.3-A API 동반 완료 후 — 현 단계 정상(결함 아님).
> - 잔여 BLOCK: backend develop→test merge(16) + SEC-D14 + post-merge live E2E(결정 73 권장). frontend v1.2 = **PASS**, v1.3 = **pending**(in_progress).

> **81차 재검증 (2026-06-08T01:35 UTC, frontend) — test `@4f71543` 불변·58/18 PASS·86 modules·audit 0·develop `c510f5c`(+2 v1.2 CLEAN)·15 ahead·develop 143/46 PASS·PASS**:
> - **frontend test HEAD `4f71543`** 불변 — working tree **CLEAN**.
> - **`src/frontend-test` `npm test`**: **58 tests/18 files PASS** (vitest 4.1.8) — 81차 독립 실측.
> - **`src/frontend-test` `npm run build`**: **86 modules SUCCESS** (vite 6.4.3, JS 210.46 kB gzip 66.20 kB, CSS 27.27 kB) — 81차 독립 실측.
> - **`src/frontend-test` `npm audit`**: **0 vulnerabilities** — 81차 독립 실측.
> - **`git cat-file -e HEAD:`** `ProtectedRoute.jsx`·`services.js`·`SideNav.jsx`·`pilotChecklist.js`·`liveConfig.js`·`vitest.live.config.js`·`AuthContext.jsx` **전부 PRESENT** ✓ (이관 규율 5 PASS). SEC-005 localStorage/sessionStorage **0건**.
> - **frontend develop HEAD `c510f5c`** (+2 vs 80차 `95b92b9`: `fd4e8f3` `feat(ux): US-G06 DISCREPANCY 청구 라인 비교 링크·접근성 재점검` · `c510f5c` `test(v1.2): US-G06 DISCREPANCY compare pilotPageFlows E2E`), working tree **CLEAN** (0 dirty).
> - develop `npm test`: **143/46 PASS**(vitest 4.1.8, 80차 137/45 → +6/+1: US-G06 DISCREPANCY 비교 회귀) · develop `npm audit`: **0 vulnerabilities** — 81차 실측.
> - develop **15커밋 ahead** of test (80차 13 → +2) — v1.2 WIP, non-blocking.
> - **ROADMAP v1.1 `merge_status: merged`** — test 브랜치 검증 **PASS** (69차 이후 불변).
> - **신규 Open 0건** — 판정 **PASS**(v1.1). 잔여: backend merge(15) + post-merge live E2E(결정 73 권장) + v1.2 develop +15 ahead.

> **80차 재검증 (2026-06-08T00:30 UTC, frontend) — test `@4f71543` 불변·58/18 PASS·86 modules·audit 0·develop `95b92b9`(+2 v1.2 CLEAN)·13 ahead·develop 137/45 PASS·124 modules·PASS**:
> - **frontend test HEAD `4f71543`** 불변 — working tree **CLEAN**.
> - **`src/frontend-test` `npm test`**: **58 tests/18 files PASS** (vitest 4.1.8) — 80차 독립 재실측.
> - **`src/frontend-test` `npm run build`**: **86 modules SUCCESS** (vite 6.4.3, JS 210.46 kB gzip 66.20 kB, CSS 27.27 kB) — 80차 독립 재실측.
> - **`src/frontend-test` `npm audit`**: **0 vulnerabilities** — 80차 독립 재실측.
> - **`git cat-file -e HEAD:`** `ProtectedRoute.jsx`·`services.js`·`SideNav.jsx`·`pilotChecklist.js`·`liveConfig.js`·`vitest.live.config.js`·`AuthContext.jsx` **전부 PRESENT** ✓ (이관 규율 5 PASS). SEC-005 localStorage/sessionStorage **0건**.
> - **frontend develop HEAD `95b92b9`** (+2 vs 77차 `4957bd3`: `3ec8206` `feat(uxd-41): US-F03 낙상·사고·특이사항 이벤트 기록 UI 신설` · `95b92b9` `fix(v1.2): US-F03 incident API 본문 detail 필드 정합 (Q154)`), working tree **CLEAN** (0 dirty).
> - develop `npm test`: **137/45 PASS**(vitest 4.1.8, 77차 130/44 → +7/+1: US-F03 이벤트 기록 회귀) · develop `npm run build`: **124 modules SUCCESS**(vite 6.4.3, JS 316.89 kB gzip 90.47 kB, CSS 30.85 kB) · develop `npm audit`: **0 vulnerabilities** — 80차 실측.
> - develop **13커밋 ahead** of test (77차 11 → +2) — v1.2 WIP, non-blocking.
> - **ROADMAP v1.1 `merge_status: merged`** — test 브랜치 검증 **PASS** (69차 이후 불변).
> - **신규 Open 0건** — 판정 **PASS**(v1.1). 잔여: backend merge(14) + post-merge live E2E(결정 73 권장) + v1.2 develop +13 ahead.

> **77차 재검증 (2026-06-07T23:30 UTC, frontend) — test `@4f71543` 불변·58/18 PASS·86 modules·audit 0·develop `4957bd3`(+2 v1.2 CLEAN)·11 ahead·develop 130/44 PASS·123 modules·PASS**:
> - **frontend test HEAD `4f71543`** 불변 — working tree **CLEAN**.
> - **`src/frontend-test` `npm test`**: **58 tests/18 files PASS** (vitest 4.1.8) — 77차 독립 재실측.
> - **`src/frontend-test` `npm run build`**: **86 modules SUCCESS** (vite 6.4.3, JS 210.46 kB gzip 66.20 kB, CSS 27.27 kB) — 77차 독립 재실측.
> - **`src/frontend-test` `npm audit`**: **0 vulnerabilities** — 77차 독립 재실측.
> - **`git cat-file -e HEAD:`** `ProtectedRoute.jsx`·`services.js`·`SideNav.jsx`·`pilotChecklist.js`·`liveConfig.js`·`vitest.live.config.js`·`AuthContext.jsx` **전부 PRESENT** ✓ (이관 규율 5 PASS, test·develop HEAD 양쪽). SEC-005 localStorage/sessionStorage **0건**.
> - **frontend develop HEAD `4957bd3`** (+2 vs 76차 `c5708c7`: `9863312` `feat(uxd-40): US-F01 활력징후 비정상 범위 입력 경고·정상 범위 단일 원천` · `4957bd3` `fix(v1.2): FAQ Q154 건강·NHIS API 본문 정합`), working tree **CLEAN** (0 dirty).
> - **`c5708c7..4957bd3` 변경 내역**(15 files, +572/-75): 신규 `src/utils/vitalsRanges.js`(+test)·`src/utils/healthRecords.js`(+test) — 활력징후 정상 범위 단일 원천·비정상 경고 로직 + `VitalsRecordForm`·`HealthPage`/`HealthDetailPage` 연동·FAQ Q154 API 본문 정합.
> - develop `npm test`: **130/44 PASS**(vitest 4.1.8, 76차 115/40 → +15/+4: vitalsRanges·healthRecords 회귀) · develop `npm run build`: **123 modules SUCCESS**(vite 6.4.3, JS 313.51 kB gzip 89.67 kB, CSS 30.85 kB) · develop `npm audit`: **0 vulnerabilities** — 77차 실측.
> - develop **11커밋 ahead** of test (76차 9 → +2) — v1.2 WIP, non-blocking.
> - **ROADMAP v1.1 `merge_status: merged`** — test 브랜치 검증 **PASS** (69차 이후 불변).
> - **신규 Open 0건** — 판정 **PASS**(v1.1). 잔여: backend merge(13) + post-merge live E2E(결정 73 권장) + v1.2 develop +11 ahead.

> **80차 재검증 (2026-06-08T01:25 UTC, backend) — develop `4c74f84`→`ac17ad8`(+1커밋)·v2/J03 Korean SMS fallback text for alimtalk relay·develop 198/198 PASS·test 79/79·15커밋 ahead·merge 미실행·BLOCK(merge 게이트)**:
> - **backend develop HEAD `ac17ad8`**(+1커밋 vs 79차 `4c74f84` — `feat(v2/J03): add Korean SMS fallback text for alimtalk relay`), working tree **CLEAN**(0 dirty).
> - **`ac17ad8` 변경 내역**(7 files, +225/-2): `AlimtalkFallbackText.java`(89 lines — 알림 payload를 Solapi 한국어 SMS fallback 메시지로 매핑하는 도메인 모델, 카카오 알림톡 전달 실패 시 가독성 있는 SMS 본문 생성)·`AlimtalkTemplateVariables.java`(+3 — `incidentType` 를 emergency 카테고리 alias 로 지원)·`SolapiKakaoAlimtalkProvider.java`(+3 — fallback text 전달)·`SolapiSmsProvider.java`(+6 — SMS fallback 본문 적용)·`AlimtalkFallbackTextTest.java`(64 lines — fallback 텍스트 매핑 단위 테스트)·`AlimtalkTemplateVariablesTest.java`(+31 — incidentType alias 커버리지)·`SolapiKakaoAlimtalkProviderTest.java`(+31 — fallback text 커버리지).
> - **`git cat-file -e HEAD:`** v1 baseline + V45 + V46 + notification history + vitals dispatch + service-layer alimtalk flow E2E + AlimtalkTemplateVariables + `AlimtalkFallbackText`·`AlimtalkFallbackTextTest`·`SolapiSmsProvider` artifacts **전부 PRESENT** ✓ (이관 규율 5·6 PASS — 79차 PASS 유지, 신규 fallback text 산출물 포함).
> - **test branch (`src/backend-test @ 2799e29`) `mvn test`**: **79/79 PASS**(23 suites, 0 fail, Boot 3.3.1, JAR 76,466,058 B) — 80차 실측.
> - **develop HEAD (`src/backend @ ac17ad8`, committed) `mvn test`**: **198/198 PASS**(53 suites, 0 fail) — 79차 191 → +7: `AlimtalkFallbackTextTest` + `AlimtalkTemplateVariablesTest` incidentType alias + `SolapiKakaoAlimtalkProviderTest` fallback text.
> - develop **15커밋 ahead** of test (`f47ffa1`·`cf6116c`·`3f9264f`·`136239e`·`8d42bdd`·`80bdb1e`·`c221531`·`44e0f02`·`78e8928`·`c53dd3b`·`8ce1151`·`0832fbf`·`32a1f8f`·`4c74f84`·`ac17ad8`) — merge **미실행**.
> - **신규 Open 0건** — 판정 **BLOCK**(merge 게이트 15커밋 단일). 「테스트 PASS ≠ 이관 PASS」 — merge 완료 후 test 재검증 필수.

> **79차 재검증 (2026-06-08T00:18 UTC, backend) — develop `32a1f8f`→`4c74f84`(+1커밋)·v2/J03 alimtalk payload Solapi 변수 매핑·develop 191/191 PASS·test 79/79·14커밋 ahead·merge 미실행·BLOCK(merge 게이트)**:
> - **backend develop HEAD `4c74f84`**(+1커밋 vs 78차 `32a1f8f` — `feat(v2/J03): map alimtalk payload to Solapi template variables`), working tree **CLEAN**(0 dirty).
> - **`4c74f84` 변경 내역**(6 files, +197/-5): `AlimtalkTemplateVariables.java`(74 lines — 카카오 알림톡 프로덕션 템플릿 변수 매핑 도메인 모델, `template_id`·`kakao_pf_id`·variables Map 빌더 패턴)·`SolapiKakaoAlimtalkProvider.java`(+9 — `kakaoOptions.variables` 주입으로 실제 Kakao 템플릿 전달 완성)·`SolapiMessageClient.java`(+11 — variables 필드 추가)·`AlimtalkTemplateVariablesTest.java`(67 lines — 빌더·직렬화 단위 테스트)·`J03AlimtalkServiceFlowE2eTest.java`(+35 — medication·note daily-care dispatch 경로 확장)·`SolapiKakaoAlimtalkProviderTest.java`(+6 — variables 주입 커버리지).
> - **`git cat-file -e HEAD:`** v1 baseline + V45 + V46 + notification history + vitals dispatch + service-layer alimtalk flow E2E + AlimtalkTemplateVariables artifacts **전부 PRESENT** ✓ (이관 규율 5·6 PASS — 78차 PASS 유지, 신규 `AlimtalkTemplateVariables`·`AlimtalkTemplateVariablesTest`·`SolapiKakaoAlimtalkProvider` 포함).
> - **test branch (`src/backend-test @ 2799e29`) `mvn test`**: **79/79 PASS**(23 suites, 0 fail, Boot 3.3.1, JAR 76,466,058 B) — 79차 실측.
> - **develop HEAD (`src/backend @ 4c74f84`, committed) `mvn test`**: **191/191 PASS**(51+ suites, 0 fail) — 78차 185 → +6: `AlimtalkTemplateVariablesTest` + `J03AlimtalkServiceFlowE2eTest` medication·note path + `SolapiKakaoAlimtalkProviderTest` variables.
> - develop **14커밋 ahead** of test (`f47ffa1`·`cf6116c`·`3f9264f`·`136239e`·`8d42bdd`·`80bdb1e`·`c221531`·`44e0f02`·`78e8928`·`c53dd3b`·`8ce1151`·`0832fbf`·`32a1f8f`·`4c74f84`) — merge **미실행**.
> - **신규 Open 0건** — 판정 **BLOCK**(merge 게이트 14커밋 단일). 「테스트 PASS ≠ 이관 PASS」 — merge 완료 후 test 재검증 필수.

> **78차 재검증 (2026-06-07T23:20 UTC, backend) — develop `0832fbf`→`32a1f8f`(+1커밋)·v2/J03 service-layer alimtalk flow E2E·develop 185/185 PASS·test 79/79·13커밋 ahead·merge 미실행·BLOCK(merge 게이트)**:
> - **backend develop HEAD `32a1f8f`**(+1커밋 vs 76차 `0832fbf` — `feat(v2/J03): add service-layer alimtalk flow E2E tests`), working tree **CLEAN**(0 dirty).
> - **`32a1f8f` 변경 내역**(2 files, +424): `J03AlimtalkServiceFlowE2eTest.java`(357 lines — attendance·health·billing 도메인 액션을 `NotificationService` 경유로 wire, check-out dispatch 검증, US-J03 알림톡 흐름 service-layer E2E)·`AttendanceServiceTest.java`(+67 — check-out 시 알림 디스패치 커버리지).
> - **`git cat-file -e HEAD:`** v1 baseline + V45 + V46 + notification history + vitals dispatch + service-layer alimtalk flow E2E artifacts **전부 PRESENT** ✓ (이관 규율 5·6 PASS — 76차 PASS 유지, 신규 `J03AlimtalkServiceFlowE2eTest`·`AttendanceServiceTest` 포함).
> - **test branch (`src/backend-test @ 2799e29`) `mvn test`**: **79/79 PASS**(23 suites, 0 fail, Boot 3.3.1, JAR 76,466,058 B) — 78차 실측.
> - **develop HEAD (`src/backend @ 32a1f8f`, committed) `mvn test`**: **185/185 PASS**(51 suites, 0 fail) — 76차 179 → +6: `J03AlimtalkServiceFlowE2eTest` + `AttendanceServiceTest` check-out dispatch.
> - develop **13커밋 ahead** of test (`f47ffa1`·`cf6116c`·`3f9264f`·`136239e`·`8d42bdd`·`80bdb1e`·`c221531`·`44e0f02`·`78e8928`·`c53dd3b`·`8ce1151`·`0832fbf`·`32a1f8f`) — merge **미실행**.
> - **신규 Open 0건** — 판정 **BLOCK**(merge 게이트 13커밋 단일). 「테스트 PASS ≠ 이관 PASS」 — merge 완료 후 test 재검증 필수.

> **76차 재검증 (2026-06-07T22:27 UTC, frontend) — test `@4f71543` 불변·58/18 PASS·86 modules·audit 0·develop `c5708c7`(+1 v1.2 CLEAN)·9 ahead·develop 115/40 PASS·120 modules·PASS**:
> - **frontend test HEAD `4f71543`** 불변 — working tree **CLEAN**.
> - **`src/frontend-test` `npm test`**: **58 tests/18 files PASS** (vitest 4.1.8) — 76차 독립 재실측.
> - **`src/frontend-test` `npm run build`**: **86 modules SUCCESS** (vite 6.4.3, JS 210.46 kB gzip 66.20 kB, CSS 27.27 kB) — 76차 독립 재실측.
> - **`src/frontend-test` `npm audit`**: **0 vulnerabilities** — 76차 독립 재실측.
> - **`git cat-file -e HEAD:`** `ProtectedRoute.jsx`·`services.js`·`SideNav.jsx`·`pilotChecklist.js`·`liveConfig.js`·`vitest.live.config.js`·`AuthContext.jsx` **전부 PRESENT** ✓ (이관 규율 5 PASS, test·develop HEAD 양쪽). SEC-005 localStorage/sessionStorage **0건**.
> - **frontend develop HEAD `c5708c7`** (+1 vs 75차 `a627c6d`: `feat(uxd-39): Must 흐름 UI 보강 — guardian/checkin·건강·NHIS·접근성`), working tree **CLEAN** (0 dirty).
> - **`a627c6d..c5708c7` 변경 내역**(17 files, +748/-91): `MedicationRecordForm.jsx`(+test)·`VitalsRecordForm.jsx`·`NhisReconciliationTable.jsx`(+test)·`MedicationDuplicateAlert.jsx`(+test)·`HealthPage.jsx`·`HealthDetailPage.jsx`(+test)·`ReconciliationPage.jsx`·`GuardianPortalPage.jsx`·`navConfig.js`·`components.css`.
> - develop `npm test`: **115/40 PASS**(vitest 4.1.8, 75차 110/36 → +5/+4) · develop `npm run build`: **120 modules SUCCESS**(vite 6.4.3, JS 310.33 kB gzip 88.52 kB, CSS 30.77 kB) · develop `npm audit`: **0 vulnerabilities** — 76차 실측.
> - develop **9커밋 ahead** of test (75차 8 → +1) — v1.2 WIP, non-blocking.
> - **ROADMAP v1.1 `merge_status: merged`** — test 브랜치 검증 **PASS** (69차 이후 불변).
> - **신규 Open 0건** — 판정 **PASS**(v1.1). 잔여: backend merge(12) + post-merge live E2E(결정 73 권장) + v1.2 develop +9 ahead.

> **76차 재검증 (2026-06-07T22:23 UTC, backend) — develop `8ce1151`→`0832fbf`(+1커밋)·v2/J03 DAILY_CARE vitals dispatch·develop 179/179 PASS·test 79/79·12커밋 ahead·merge 미실행·BLOCK(merge 게이트)**:
> - **backend develop HEAD `0832fbf`**(+1커밋 vs 74차 `8ce1151` — `feat(v2/J03): dispatch DAILY_CARE notifications for vitals`), working tree **CLEAN**(0 dirty).
> - **`0832fbf` 변경 내역**(2 files, +96): `HealthRecordService.java`(+44 — 활력징후 기록 생성 시 `NotificationService` 통해 보호자 DAILY_CARE 알림톡 디스패치, `formatVitalsDetail` 헬퍼)·`HealthRecordServiceTest.java`(+53 — vitals dispatch payload 단위 테스트). US-J03 v2/J03 follow-up (medication dispatch @ `78e8928` 후속).
> - **`git cat-file -e HEAD:`** v1 baseline + V45 + V46 + notification history + vitals dispatch artifacts **전부 PRESENT** ✓ (이관 규율 5 PASS — 74차 PASS 유지).
> - **test branch (`src/backend-test @ 2799e29`) `mvn test`**: **79/79 PASS**(23 suites, 0 fail, Boot 3.3.1, JAR 76,466,058 B) — 76차 실측.
> - **develop HEAD (`src/backend @ 0832fbf`) `mvn test`**: **179/179 PASS**(50 suites, 74차 178 → +1: `HealthRecordServiceTest` vitals dispatch) — 76차 실측.
> - develop **12커밋 ahead** of test — merge **미실행**.
> - **신규 Open 0건** — 판정 **BLOCK**(develop→test merge 게이트 12커밋 단일).

> **75차 재검증 (2026-06-07T21:24 UTC, frontend) — test `@4f71543` 불변·58/18 PASS·86 modules·audit 0·develop `a627c6d`(+2 v1.2 CLEAN)·8 ahead·develop 110/36 PASS·117 modules·PASS**:
> - **frontend test HEAD `4f71543`** 불변 — working tree **CLEAN**.
> - **`src/frontend-test` `npm test`**: **58 tests/18 files PASS** (vitest 4.1.8) — 75차 독립 재실측.
> - **`src/frontend-test` `npm run build`**: **86 modules SUCCESS** (vite 6.4.3, JS 210.46 kB gzip 66.20 kB, CSS 27.27 kB) — 75차 독립 재실측.
> - **`src/frontend-test` `npm audit`**: **0 vulnerabilities** — 75차 독립 재실측.
> - **`git cat-file -e HEAD:`** `ProtectedRoute.jsx`·`services.js`·`SideNav.jsx`·`pilotChecklist.js`·`liveConfig.js`·`vitest.live.config.js`·`AuthContext.jsx` **전부 PRESENT** ✓ (이관 규율 5 PASS, test·develop HEAD 양쪽). SEC-005 localStorage/sessionStorage **0건**.
> - **frontend develop HEAD `a627c6d`** (+2 vs 73차 `9bdf59f`: `6f3f746` 수기 출석 체크인/아웃·결석 흐름(US-E01·E02) · `a627c6d` US-E03 QR 저장·US-E05 출석 통계 API 통합), working tree **CLEAN** (0 dirty).
> - **`9bdf59f..a627c6d` 변경 내역**(14 files, +767/-47): `services.js`(+18)·`AttendanceAbsentModal.jsx`(+test)·`CheckoutModal.jsx`(+test)·`AttendancePage.jsx`(+243)(+test)·`AttendanceStatsPage.jsx`(+test)·`QrGeneratePage.jsx`(+test)·`utils/downloadDataUrl.js`(+test)·`components/ui/index.js`.
> - develop `npm test`: **110/36 PASS**(vitest 4.1.8, 71차 89/28 → +21/+8) · develop `npm run build`: **117 modules SUCCESS**(vite 6.4.3, JS 303.24 kB gzip 86.86 kB, CSS 30.33 kB) · develop `npm audit`: **0 vulnerabilities** — 75차 실측.
> - develop **8커밋 ahead** of test (73차 6 → +2) — v1.2 WIP, non-blocking.
> - **ROADMAP v1.1 `merge_status: merged`** — test 브랜치 검증 **PASS** (69차 이후 불변).
> - **신규 Open 0건** — 판정 **PASS**(v1.1). 잔여: backend merge(12) + post-merge live E2E(결정 73 권장) + v1.2 develop +8 ahead.

> **73차 재검증 (2026-06-07T20:21 UTC, frontend) — test `@4f71543` 불변·58/18 PASS·86 modules·audit 0·develop `9bdf59f`(+2 v1.2 CLEAN)·6 ahead·PASS**:
> - **frontend test HEAD `4f71543`** 불변 — working tree **CLEAN**.
> - **`src/frontend-test` `npm test`**: **58 tests/18 files PASS** (vitest 4.1.8) — 73차 독립 실측.
> - **`src/frontend-test` `npm run build`**: **86 modules SUCCESS** (vite 6.4.3, JS 210.46 kB gzip 66.20 kB, CSS 27.27 kB) — 73차 독립 실측.
> - **`src/frontend-test` `npm audit`**: **0 vulnerabilities** — 73차 독립 실측.
> - **`git cat-file -e HEAD:`** `ProtectedRoute.jsx`·`services.js`·`SideNav.jsx`·`pilotChecklist.js`·`liveConfig.js`·`AuthContext.jsx` **전부 PRESENT** ✓ (이관 규율 5 PASS). SEC-005 localStorage/sessionStorage **0건**.
> - **frontend develop HEAD `9bdf59f`** (+2 vs 71차 `42f48e1`: `a68f150` GuardianCheckinPage DS FilterChips(US-E04) · `9bdf59f` P0 CRUD E2E·입금 모달·보호자 초대/수정 수정), working tree **CLEAN** (0 dirty).
> - develop **6커밋 ahead** of test (71차 4 → +2) — v1.2 WIP, non-blocking.
> - **ROADMAP v1.1 `merge_status: merged`** — test 브랜치 검증 **PASS** (69차 이후 불변).
> - **신규 Open 0건** — 판정 **PASS**(v1.1). 잔여: backend merge(10) + post-merge live E2E(결정 73 권장) + v1.2 develop +6 ahead.

> **74차 재검증 (2026-06-07T21:20 UTC, backend) — develop `c53dd3b`→`8ce1151`(+1커밋)·V46 notification history query index·develop 178/178 PASS·test 79/79·11커밋 ahead·merge 미실행·BLOCK(merge 게이트)**:
> - **backend develop HEAD `8ce1151`**(+1커밋 vs 72차 `c53dd3b` — `feat(v2/J03): add notification history query index (V46)`), working tree **CLEAN**(0 dirty).
> - **`8ce1151` 변경 내역**(1 file, +9): `db/migration/V46__notification_history_query_index.sql` — `CREATE INDEX idx_notifications_org_recipient_created ON notifications (organization_id, recipient_user_id, created_at DESC)`. tenant-scoped pagination 성능 최적화 (API_SPEC §11-5 notification history 조회 쿼리 대응). 신규 @Test 없음.
> - **`git cat-file -e HEAD:`** `pilot/PilotChecklistJwtE2eTest`·`routing/MustApiEndpointRoutingTest`·`security/ProductionSecretValidatorTest`·`security/SevenRoleJwtLoginE2eTest`·`security/RoleBasedControllerAccessTest`·`auth/domain/AuthRateLimitService`·`auth/domain/AuthRateLimitServiceTest`·`V45`·`V46`·`notification/domain/NotificationAlimtalkDispatchE2eTest`·`notification/config/NotificationConfigTest`·`health/domain/HealthRecordServiceTest`·`notification/api/GuardianNotificationHistoryController`·`notification/api/StaffClientNotificationHistoryController`·`notification/domain/NotificationHistoryService`·`notification/domain/NotificationHistoryServiceTest` **전부 PRESENT** ✓ (이관 규율 5 PASS — 72차 PASS 유지 + V46 신규).
> - **test branch (`src/backend-test @ 2799e29`) `mvn test`**: **79/79 PASS**(23 suites, 0 fail, Boot 3.3.1, JAR 76,466,058 B) — 74차 실측.
> - **test branch `mvn -q -DskipTests package`**: **SUCCESS** — `backend-0.0.1-SNAPSHOT.jar` **76,466,058 B** — test 브랜치 변경 없음.
> - **develop HEAD (`src/backend @ 8ce1151`) `mvn test`**: **178/178 PASS**(50 suites, 72차 178 불변 — V46은 SQL 마이그레이션 파일만, 신규 @Test 없음) — 74차 실측.
> - develop **11커밋 ahead** of test (`f47ffa1`·`cf6116c`·`3f9264f`·`136239e`·`8d42bdd`·`80bdb1e`·`c221531`·`44e0f02`·`78e8928`·`c53dd3b`·`8ce1151`) — merge **미실행**.
> - **신규 Open 0건** — 판정 **BLOCK**(develop→test merge 게이트 11커밋 단일).

> **72차 재검증 (2026-06-07T20:10 UTC, backend) — develop `78e8928`→`c53dd3b`(+1커밋)·v2/J03 guardian·staff 알림 이력 API·develop 178/178 PASS·test 79/79·10커밋 ahead·merge 미실행·BLOCK(merge 게이트)**:
> - **backend develop HEAD `c53dd3b`**(+1커밋 vs 70차 `78e8928` — `feat(v2/J03): add guardian and staff notification history APIs`), working tree **CLEAN**(0 dirty).
> - **`c53dd3b` 변경 내역**(8 files, +514): `notification/api/GuardianNotificationHistoryController.java`(34 — 보호자 본인 알림 이력 조회)·`notification/api/StaffClientNotificationHistoryController.java`(38 — 직원의 이용자 알림 이력 조회)·`notification/api/NotificationHistoryResponse.java`(15)·`notification/api/NotificationHistoryPageResponse.java`(12)·`notification/domain/NotificationHistoryService.java`(187 — 테넌트·역할 스코프 페이지네이션 이력 조회)·`notification/persistence/NotificationRepository.java`(+14 조회 쿼리)·`notification/domain/NotificationHistoryServiceTest.java`(168 — 이력·스코프·페이지 단위 테스트)·`routing/MustApiEndpointRoutingTest.java`(+46 — 알림 이력 라우팅 RBAC). US-J03 v2/J03 follow-up.
> - **`git cat-file -e HEAD:`** `pilot/PilotChecklistJwtE2eTest`·`routing/MustApiEndpointRoutingTest`·`security/ProductionSecretValidatorTest`·`security/SevenRoleJwtLoginE2eTest`·`security/RoleBasedControllerAccessTest`·`auth/domain/AuthRateLimitService`·`auth/domain/AuthRateLimitServiceTest`·`V45`·`notification/domain/NotificationAlimtalkDispatchE2eTest`·`notification/config/NotificationConfigTest`·`health/domain/HealthRecordServiceTest`·`notification/api/GuardianNotificationHistoryController`·`notification/api/StaffClientNotificationHistoryController`·`notification/domain/NotificationHistoryService`·`notification/domain/NotificationHistoryServiceTest` **전부 PRESENT** ✓ (이관 규율 5 PASS — 70차 PASS 유지 + 신규 알림 이력 API).
> - **test branch (`src/backend-test @ 2799e29`) `mvn test`**: **79/79 PASS**(23 suites, 0 fail, Boot 3.3.1) — 72차 실측.
> - **test branch `mvn -q -DskipTests package`**: **SUCCESS** — `backend-0.0.1-SNAPSHOT.jar` **76,466,058 B** — 72차 실측.
> - **develop HEAD (`src/backend @ c53dd3b`) `mvn test`**: **178/178 PASS**(50 suites, 70차 171 → +7: `NotificationHistoryServiceTest` + `MustApiEndpointRoutingTest` 알림 이력) — 72차 실측.
> - develop **10커밋 ahead** of test (`f47ffa1`·`cf6116c`·`3f9264f`·`136239e`·`8d42bdd`·`80bdb1e`·`c221531`·`44e0f02`·`78e8928`·`c53dd3b`) — merge **미실행**.
> - **신규 Open 0건** — 판정 **BLOCK**(develop→test merge 게이트 10커밋 단일).

> **71차 재검증 (2026-06-07T19:20 UTC, frontend) — test `@4f71543` 불변·58/18 PASS·86 modules·audit 0·develop `42f48e1`(+2 vs 69차)·89/28 PASS·114 modules·audit 0·PASS**:
> - **frontend test HEAD `4f71543`**(69차 불변), working tree **CLEAN**.
> - **`src/frontend-test` `npm test`**: **58 tests/18 files PASS**(vitest 4.1.8) — 71차 실측.
> - **`src/frontend-test` `npm run build`**: **86 modules SUCCESS**(vite 6.4.3, JS 210.46 kB gzip 66.20 kB, CSS 27.27 kB) — 71차 실측.
> - **`src/frontend-test` `npm audit`**: **0 vulnerabilities** — 71차 실측.
> - **`git cat-file -e HEAD:`** `ProtectedRoute.jsx`·`services.js`·`SideNav.jsx`·`pilotChecklist.js`·`liveConfig.js`·`AuthContext.jsx` **전부 PRESENT** ✓ (이관 규율 5 PASS). SEC-005 localStorage/sessionStorage **0건**.
> - **frontend develop HEAD `42f48e1`**(+2 vs 69차 `e0eaf32`: `0d83a42` feat(ux) 15 missing pages · `42f48e1` fix(v1.2) P0 page-flow tests·module coverage KPI·title 정렬), working tree **CLEAN**.
> - develop `npm test`: **89/28 PASS**(vitest 4.1.8, 69차 82/27 → +7/+1: `competitorModuleCoverage.test.js` 3건·pilotPageFlows 강화) — 71차 실측.
> - develop `npm run build`: **114 modules SUCCESS**(vite 6.4.3, JS 295.02 kB gzip 84.80 kB, CSS 30.23 kB) — 71차 실측.
> - develop `npm audit`: **0 vulnerabilities** — 71차 실측.
> - **ROADMAP v1.1 `merge_status: merged`** — test 브랜치 검증 **PASS**(69차 이후 불변).
> - **신규 Open 0건** — 판정 **PASS**(v1.1). 잔여: backend merge(9) + post-merge live E2E(결정 73 권장) + v1.2 develop +4 ahead.

> **70차 재검증 (2026-06-07T19:05 UTC, backend) — develop `44e0f02`→`78e8928`(+1커밋)·v2/J03 DAILY_CARE medication dispatch·develop 171/171 PASS·test 79/79·9커밋 ahead·merge 미실행·BLOCK(merge 게이트)**:
> - **backend develop HEAD `78e8928`**(+1커밋 vs 68차 `44e0f02` — `feat(v2/J03): dispatch DAILY_CARE alimtalk on medication records`), working tree **CLEAN**(0 dirty).
> - **`78e8928` 변경 내역**: `HealthRecordService.java`(+20 — `createMedication` 시 `NotificationService` 통해 보호자 DAILY_CARE 알림톡 디스패치 연동, `formatMedicationDetail` 헬퍼)·`HealthRecordServiceTest.java`(+60 — dispatch payload 단위 테스트). US-J03, PLAN_NOTES round 65 후속.
> - **`git cat-file -e HEAD:`** `pilot/PilotChecklistJwtE2eTest`·`routing/MustApiEndpointRoutingTest`·`security/ProductionSecretValidatorTest`·`security/SevenRoleJwtLoginE2eTest`·`security/RoleBasedControllerAccessTest`·`auth/domain/AuthRateLimitService`·`auth/domain/AuthRateLimitServiceTest`·`V45`·`notification/domain/NotificationAlimtalkDispatchE2eTest`·`notification/config/NotificationConfigTest`·`health/domain/HealthRecordServiceTest` **전부 PRESENT** ✓ (이관 규율 5 PASS — 68차 PASS 유지).
> - **test branch (`src/backend-test @ 2799e29`) `mvn test`**: **79/79 PASS**(23 suites, Boot 3.3.1, JAR 76,466,058 B) — 70차 실측.
> - **develop HEAD (`src/backend @ 78e8928`) `mvn test`**: **171/171 PASS**(48 suites, 68차 170 → +1: `HealthRecordServiceTest`) — 70차 실측.
> - develop **9커밋 ahead** of test (`f47ffa1`·`cf6116c`·`3f9264f`·`136239e`·`8d42bdd`·`80bdb1e`·`c221531`·`44e0f02`·`78e8928`) — merge **미실행**.
> - **신규 Open 0건** — 판정 **BLOCK**(develop→test merge 게이트 9커밋 단일).

> **69차 재검증 (2026-06-07T18:12 UTC, frontend) — v1.1 merge 완료·test `@4f71543`·58/18 PASS·86 modules·audit 0·develop +2 v1.2·PASS**:
> - **frontend test HEAD `4f71543`**(v1.1 merged — 67차 `e5fd48d` stale → merge 완료), working tree **CLEAN**.
> - **`src/frontend-test` `npm ci`+`npm test`**: **58 tests/18 files PASS**(vitest 4.1.8) — 69차 실측.
> - **`src/frontend-test` `npm run build`**: **86 modules SUCCESS**(vite 6.4.3, JS 210.46 kB gzip 66.20 kB, CSS 27.27 kB).
> - **`src/frontend-test` `npm audit`**: **0 vulnerabilities**.
> - **`git cat-file -e HEAD:`** `ProtectedRoute.jsx`·`services.js`·`SideNav.jsx`·`pilotChecklist.js`·`pilotPageFlows.test.jsx`·`liveConfig.js`·`vitest.live.config.js`·`AuthContext.jsx` **전부 PRESENT** ✓ (이관 규율 5 PASS). SEC-005 localStorage/sessionStorage **0건**.
> - **frontend develop HEAD `e0eaf32`**(+2 v1.2 vs test: `64468a3` UXD 35 P0 UI · `e0eaf32` guardians RBAC), working tree **CLEAN**, `npm test` **82/27 PASS**.
> - **ROADMAP v1.1 `merge_status: merged`** — test 브랜치 검증 **PASS**.
> - **신규 Open 0건** — 판정 **PASS**(v1.1). 잔여: backend merge(8) + post-merge live E2E(결정 73 권장) + v1.2 develop +2 ahead.

> **68차 재검증 (2026-06-07T18:07 UTC, backend) — develop `c221531`→`44e0f02`(+1커밋)·NotificationConfig quiet hours·develop 170/170 PASS·test 79/79·8커밋 ahead·merge 미실행·BLOCK(merge 게이트)**:
> - **backend develop HEAD `44e0f02`**(+1커밋 vs 66차 `c221531` — `Ensure quiet hours clock is provided and add coverage`), working tree **CLEAN**(0 dirty).
> - **`44e0f02` 변경 내역**: `NotificationConfig.java`(quiet hours clock provider)·`NotificationConfigTest.java`(1 @Test — quiet hours coverage)·`GlobalExceptionHandler.java`·`SecurityConfig.java` 정리.
> - **`git cat-file -e HEAD:`** `pilot/PilotChecklistJwtE2eTest`·`routing/MustApiEndpointRoutingTest`·`security/ProductionSecretValidatorTest`·`security/SevenRoleJwtLoginE2eTest`·`security/RoleBasedControllerAccessTest`·`auth/domain/AuthRateLimitService`·`auth/domain/AuthRateLimitServiceTest`·`V45`·`notification/domain/NotificationAlimtalkDispatchE2eTest`·`notification/config/NotificationConfigTest` **전부 PRESENT** ✓ (이관 규율 5 PASS — 66차 PASS 유지).
> - **test branch (`src/backend-test @ 2799e29`) `mvn test`**: **79/79 PASS**(23 suites, Boot 3.3.1, JAR 76,466,058 B) — 68차 실측.
> - **develop HEAD (`src/backend @ 44e0f02`) `mvn test`**: **170/170 PASS**(48 suites, 66차 169 → +1: `NotificationConfigTest`) — 68차 실측.
> - develop **8커밋 ahead** of test (`f47ffa1`·`cf6116c`·`3f9264f`·`136239e`·`8d42bdd`·`80bdb1e`·`c221531`·`44e0f02`) — merge **미실행**.
> - **신규 Open 0건** — 판정 **BLOCK**(develop→test merge 게이트 8커밋 단일).

> **67차 재검증 (2026-06-07T17:31 UTC, frontend) — develop `4f71543`(+2)·UXD SideNav·FE-22 liveConfig preconditions·58/18 PASS·86 modules·13 ahead·ROADMAP ready·BLOCK(B03/SEC-D14)**:
> - **frontend develop HEAD `4f71543`**(+2 vs 65차 `d592a17`: `f64e1dd` SideNav·AppShell · `4f71543` liveConfig fail-fast), working tree **CLEAN**.
> - develop `npm run build` **86 modules PASS** · `npm test` **58/18 PASS** · audit **0**.
> - test `@e5fd48d`: build **36 PASS** · npm test **N/A** · audit **2 moderate**.
> - develop **13 commits ahead** — merge **미실행**. **Open 0** — **BLOCK**(merge 게이트).

> **66차 재검증 (2026-06-07T17:22 UTC, backend) — develop `80bdb1e`→`c221531`(+1커밋)·v2/J03 daily care·emergency alimtalk E2E·develop 169/169 PASS·test 79/79·7커밋 ahead·merge 미실행·BLOCK(merge 게이트)**:
> - **backend develop HEAD `c221531`**(+1커밋 vs 64차 `80bdb1e` — `feat(v2/J03): wire daily care·emergency health notifications and alimtalk E2E tests`), working tree **CLEAN**(0 dirty).
> - **`c221531` 변경 내역**: `NotificationAlimtalkDispatchE2eTest.java`(7 @Test — `DailyCareNotificationDispatchTest`·`EmergencyHealthEventDispatchTest`·`NotificationAlimtalkIntegrationTest` v2/J03 E2E); `AttendanceServiceTest`(+1 @Test 일일돌봄 알림 트리거)·`BillingServiceTest`(+1 @Test 청구 알림 연동). v2 J03 카카오 알림톡 일일돌봄·긴급건강이벤트 알림 디스패치 E2E.
> - **`git cat-file -e HEAD:`** `pilot/PilotChecklistJwtE2eTest`·`routing/MustApiEndpointRoutingTest`·`security/ProductionSecretValidatorTest`·`security/SevenRoleJwtLoginE2eTest`·`security/RoleBasedControllerAccessTest`·`auth/domain/AuthRateLimitService`·`auth/domain/AuthRateLimitServiceTest`·`V45` **전부 PRESENT** ✓ (이관 규율 5 PASS — 64차 PASS 유지).
> - **test branch (`src/backend-test @ 2799e29`) `mvn test`**: **79/79 PASS**(23 suites, Boot 3.3.1, JAR 76,466,058 B) — 66차 실측.
> - **develop HEAD (`src/backend @ c221531`) `mvn test`**: **169/169 PASS**(64차 158 → +11: `NotificationAlimtalkDispatchE2eTest` 7 + `AttendanceServiceTest` +1 + `BillingServiceTest` +1) — 66차 실측.
> - develop **7커밋 ahead** of test (`f47ffa1`·`cf6116c`·`3f9264f`·`136239e`·`8d42bdd`·`80bdb1e`·`c221531`) — merge **미실행**.
> - **신규 Open 0건** — 판정 **BLOCK**(develop→test merge 게이트 7커밋 단일).

> **65차 재검증 (2026-06-07T16:50 UTC, frontend) — develop `bb0cec4`→`7170b2a`→`449cd4f`→`d592a17`(+3커밋)·guardian REST+J01/J02·tone Alert a11y·FE-22 live E2E harness·develop 46/13 PASS·75 modules·audit 0·test 36 PASS/N/A·11커밋 ahead·merge 미실행·BLOCK(B03/SEC-D14 merge 게이트 단일)**:
> - **frontend develop HEAD `d592a17`**(+3커밋 vs 63차 `bb0cec4`), working tree **CLEAN**(0 dirty).
> - **`7170b2a`**: guardian portal(J02) REST 연동·`ClientDetailPage`(J01) REST + `GuardianPortalPage.test.jsx`·`GuardianInvitationAcceptPage.test.jsx`·`GuardianInvitationList.test.jsx` 회귀. **`449cd4f`**: tone 기반 `Alert` live region(aria-live)·`PublicAuthLayout` h1·skip-link (US-J01 a11y). **`d592a17`**: **FE-22** — `src/e2e/pilotLiveApi.e2e.test.js`·`pilotLivePages.e2e.test.jsx`·`guardianLiveApi.e2e.test.js`·`liveConfig/liveSession/liveAuthStub`·`vitest.live.config.js`·`test:live-e2e` script·`vite.config.js` test `exclude: src/e2e/**` (369 insertions).
> - **`git cat-file -e HEAD:`** `services.js`·`GuardianPortalPage.jsx`(+test)·`ClientDetailPage.jsx`·`Alert.jsx`·`PublicAuthLayout.jsx`·`pilotChecklist`·`pilotPageFlows`·`sevenRoleRouteMatrix`·`ProtectedRoute.jsx`·`src/e2e/*`·`vitest.live.config.js` **전부 PRESENT** ✓ (이관 규율 5 PASS). SEC-005 AuthContext localStorage/sessionStorage **0건**.
> - **test branch (`src/frontend-test @ e5fd48d`)**: `npm run build` **36 modules PASS**(vite 5.4.21, JS 165.43 kB) · `npm test` **N/A**(Missing script) · `npm audit` **0 high·2 moderate**.
> - **develop HEAD (`src/frontend @ d592a17`) `npm run build`**: **75 modules SUCCESS**(vite 6.4.3, JS 209.19 kB gzip 65.68 kB, CSS 24.45 kB).
> - **develop HEAD `npm test`(vitest 4.1.8)**: **46 tests/13 files PASS**(63차 37/9 → +9/+4 — GuardianPortalPage·GuardianInvitationAcceptPage·GuardianInvitationList·guardian REST 회귀; `src/e2e/**` 는 exclude).
> - **develop HEAD `npm audit`**: **0 vulnerabilities**(high·all).
> - develop **11커밋 ahead** of test (`7c0ecdc`·`1d9a701`·`e043eac`·`f506c90`·`c3b863e`·`b87a8f5`·`811aef3`·`bb0cec4`·`7170b2a`·`449cd4f`·`d592a17`) — merge **미실행**.
> - **v1.1 ROADMAP 완료 기준 갱신**: R-04 H04 Must API·**J02 GuardianPortal REST** **PASS** · R-05 P1–P8 + **R-07 J01/J02 live E2E harness 추가**(FE-22, develop HEAD PRESENT) **PARTIAL**(실 LIVE_E2E run 은 merge·backend 후) · M01 **PARTIAL**(46/13) · SEC-008 **PASS**(audit 0) · **R-12 merge_status `pending`(B03/SEC-D14) FAIL** 단일.
> - **신규 Open 0건** — 판정 **BLOCK**(B03/SEC-D14 frontend merge 게이트 단일 — Must·J01/J02 라이브 E2E run·develop→test merge 11커밋).

> **64차 재검증 (2026-06-07T16:30 UTC, backend) — develop `136239e`→`80bdb1e`(+2커밋)·BE-11 AuthRateLimitService·V45·develop 158/158 PASS·test 79/79·6커밋 ahead·merge 미실행·BLOCK(merge 게이트 단일)**:
> - **backend develop HEAD `80bdb1e`**(+2커밋 vs 62차 `136239e` — `8d42bdd` BE-11 AuthRateLimitService · `80bdb1e` V45 v2 notification prefs integrity), working tree **CLEAN**(0 dirty).
> - **`8d42bdd` 변경 내역**: `AuthRateLimitService.java`(IP+email 슬라이딩 윈도우 60s, login·refresh·password-reset, 429 RATE_LIMITED 응답)·`AuthRateLimitServiceTest.java` + `DEPLOYMENT_GUIDE` `AUTH_*_RATE_LIMIT_*` 환경변수 — **SEC-D13 credential stuffing 방어**. **BE-11 완료**.
> - **`80bdb1e` 변경 내역**: `V45__v2_notification_prefs_integrity_and_users_phone_pair.sql` — users `phone_encrypted`/`phone_masked` pair, notifications `sent_at` NOT NULL/CHECK, `guardian_notification_preferences` tenant FK+role guard, `guardian_invitations` pending email 인덱스. v2 J03 follow-up.
> - **`git cat-file -e HEAD:`** `auth/domain/AuthRateLimitService.java`·`auth/domain/AuthRateLimitServiceTest.java` **PRESENT** ✓ (BE-11 Fixed — 이관 규율 5·6 PASS). `V45__v2_notification_prefs_integrity_and_users_phone_pair.sql` **PRESENT** ✓. v1 baseline — `pilot/PilotChecklistJwtE2eTest`·`routing/MustApiEndpointRoutingTest`·`security/ProductionSecretValidatorTest`·`security/SevenRoleJwtLoginE2eTest`·`security/RoleBasedControllerAccessTest` **전부 PRESENT** ✓ (이관 규율 5 PASS).
> - **test branch (`src/backend-test @ 2799e29`) `mvn test`**: **79/79 PASS**(23 suites, Boot 3.3.1, JAR 76,466,058 B) — 62차 이후 변동 없음 (64차 실측).
> - **develop HEAD (`src/backend @ 80bdb1e`) `mvn test`**: **158/158 PASS**(62차 152 → +6: `AuthRateLimitServiceTest`·V45 마이그레이션 참조 테스트 포함) — 64차 실측.
> - develop **6커밋 ahead** of test (`f47ffa1`·`cf6116c`·`3f9264f`·`136239e`·`8d42bdd`·`80bdb1e`) — merge **미실행**.
> - **SEC-20260608-014 (BE-11) Planned → Fixed**: `AuthRateLimitService` develop HEAD PRESENT @ `8d42bdd` — **QA_FEEDBACK Planned→Fixed 이동**.
> - **신규 Open 0건** — 판정 **BLOCK**(develop→test merge 게이트 6커밋 단일).

> **63차 재검증 (2026-06-07T15:40 UTC, frontend) — develop `e043eac`→`811aef3`(+2커밋)·Must API pages·pilotChecklist·7-role·pilotPageFlows·SEC-008 develop HEAD 반영·CLEAN·35/9 PASS·74 modules·audit 0·7커밋 ahead·merge 미실행·BLOCK(B03 merge 게이트)**:
> - **frontend develop HEAD `811aef3`**(baseline `c3b863e` 대비 +2커밋: `b87a8f5` US-J01 초대 행 스크린리더 레이블·**`811aef3`** `feat(v1.1): Must API pages, pilot checklist, 7-role tests, SEC-008`), working tree **CLEAN**(0 dirty).
> - **`811aef3` 변경 내역**(22 files +1968/-752): Must API pages(`AttendancePage`·`BillingPage`·`ClientDetailPage`·`ClientListPage`·`HealthPage`·`NHISImportPage`·`ReconciliationPage`·`DashboardPage` REST 연동)·`src/api/services.js`(+144)·`pilotChecklist.js`(+test, P1–P8 fetch-mock)·`pilotPageFlows.test.jsx`(페이지 단위 RTL E2E)·`sevenRoleJwtLogin.test.jsx`·`sevenRoleRouteGuard.test.jsx`·`sevenRoleRouteMatrix.js`·`setupTests.js` + `package.json`/`package-lock.json`(vite `^6.4.3`·vitest `^4.1.8` — SEC-008).
> - **`git cat-file -e HEAD:`** `src/api/services.js`·`pilotChecklist.js`(+test)·`pilotPageFlows.test.jsx`·`sevenRoleJwtLogin.test.jsx`·`sevenRoleRouteGuard.test.jsx`·`sevenRoleRouteMatrix.js`·Must pages·`src/auth/ProtectedRoute.jsx`·`AuthContext.jsx` **전부 PRESENT** ✓ (이관 규율 5 PASS — H04·R-04a·R-05·SEC-008 develop HEAD 반영). SEC-005 AuthContext localStorage/sessionStorage **0건**.
> - **test branch (`src/frontend-test @ e5fd48d`)**: `npm run build` **36 modules PASS**(vite 5.4.21, JS 165.43 kB) · `npm test` **N/A**(Missing script) · `npm audit` **0 high·2 moderate**.
> - **develop HEAD (`src/frontend @ 811aef3`) `npm run build`**: **74 modules SUCCESS**(vite 6.4.3, JS 205.76 kB gzip 65.05 kB, CSS 24.45 kB).
> - **develop HEAD `npm test`(vitest 4.1.8)**: **35 tests/9 files PASS**(61차 6/2 → +29/+7 — pilotChecklist·pilotPageFlows·sevenRoleJwtLogin·sevenRoleRouteGuard·roleHomePaths·ProtectedRoute·MaskedPhone 등).
> - **develop HEAD `npm audit`**: **0 vulnerabilities**(high·all) — **SEC-008 develop HEAD 해소**(61차 4 vuln/1 critical → 0; vite 6.4.3·vitest 4.1.8 upgrade 반영).
> - develop **7커밋 ahead** of test (`7c0ecdc`·`1d9a701`·`e043eac`·`f506c90`·`c3b863e`·`b87a8f5`·`811aef3`) — merge **미실행**.
> - **v1.1 ROADMAP 완료 기준 갱신**: R-04 H04 Must API **PASS**(`services.js`·Must pages develop HEAD) · R-05 P1–P8 **PARTIAL**(fetch-mock·pilotPageFlows; 라이브 E2E는 merge·backend 후) · R-04a 7-role **PARTIAL**(vitest 자동화) · M01 **PARTIAL**(35/9; 전체 회귀 잔여) · SEC-008 **PASS**(audit 0) · R-07 J01 **PARTIAL**(UI HEAD PRESENT·백엔드 초대 API 스텁) · **R-12 merge_status `pending`(B03) FAIL** 단일.
> - **61차 FAIL/ABSENT 해소**: 61차 H04(ModulePage placeholder)·M01(6 tests)·R-05/R-07·SEC-008(4 vuln) → 63차 `811aef3` **develop HEAD 반영**.
> - **추가 관측 (15:46, coder 동시 진행)**: 검증 직후 develop **`811aef3`→`bb0cec4`**(+1커밋 `fix(v1.1): restrict billing route access to admin roles` — billing 라우트 admin RBAC·`roleNav` `STAFF_NAV`(staff)/`BRANCH_ADMIN_NAV` 분리). develop HEAD `bb0cec4` working tree **CLEAN**·`npm test` **37/9 PASS**(+2)·`npm run build` **74 modules**·`npm audit` **0**·develop **8커밋 ahead** of test. HEAD Fixed(`811aef3` 산출물) 규율 5 유효 — 판정 **BLOCK** 불변. **coder 동시 진행 중 — HEAD 추가 진전 가능**.
> - **신규 Open 0건** — 판정 **BLOCK**(B03 merge 게이트 단일 — Must 라이브 E2E·J01 백엔드 API·develop→test merge 8커밋).

> **62차 재검증 (2026-06-07T15:30 UTC, backend) — develop HEAD `136239e` CLEAN·v2/J03 Solapi alimtalk 추가·152/152 PASS·test 79/79 PASS·4커밋 ahead·merge 미실행·BLOCK(merge 게이트)**:
> - **backend develop HEAD `136239e`**(+1커밋 vs 60차 `3f9264f` — `feat(v2/J03): Solapi alimtalk provider, guardian phone storage, billing notify`), working tree **CLEAN**(0 dirty).
> - **`136239e` 변경 내역**: `SolapiKakaoAlimtalkProvider.java`(Solapi REST client 구현)·`GuardianPhoneStorage.java`·`BillingNotifyService.java`·`PhoneMaskingUtil.java`·`SolapiKakaoAlimtalkProviderTest.java`·`NotificationServiceTest.java`·`PhoneMaskingUtilTest.java` — 7+ files, v2 US-J03 카카오 알림톡 실제 provider 구현.
> - **`git cat-file -e HEAD:`** `pilot/PilotChecklistJwtE2eTest`·`routing/MustApiEndpointRoutingTest`·`security/ProductionSecretValidatorTest`·`security/SevenRoleJwtLoginE2eTest`·`security/RoleBasedControllerAccessTest`·`SolapiKakaoAlimtalkProvider` **전부 PRESENT** ✓ (v1 baseline artifacts + v2/J03 Solapi 이관 규율 5·6 PASS).
> - **test branch (`src/backend-test @ 2799e29`) `mvn test`**: **79/79 PASS**(23 suites, Boot 3.3.1, JAR 76,466,058 B) — 60차 이후 변동 없음.
> - **develop HEAD (`src/backend @ 136239e`) `mvn test`**: **152/152 PASS**(+5 vs 60차 147 — `SolapiKakaoAlimtalkProviderTest`+`NotificationServiceTest`+`PhoneMaskingUtilTest`+`NotificationPreferenceServiceTest` 확장).
> - develop **4커밋 ahead** of test (`f47ffa1`·`cf6116c`·`3f9264f`·`136239e`) — merge **미실행**.
> - **v2/J03 Solapi 상태**: develop `136239e` CLEAN·152/152 PASS — 신규 이슈 없음.
> - **신규 Open 0건** — 판정 **BLOCK**(merge 게이트 4커밋 단일).

> **planner 44차 참고 (2026-06-08T16:00 UTC, frontend COD 진전 — TSR 62차 대기)**: develop HEAD **`c3b863e`**(+2 vs TSR 61 `e043eac`: `f506c90` FE-18/FE-19 · `c3b863e` favicon), WT **CLEAN**, `npm test` **9/9 PASS**, build **70 modules PASS**, develop **5 ahead** of test. FE-18 산출물 HEAD PRESENT. v1.1 H04·P1–P8·J01 live E2E **잔여**. 판정 **BLOCK**(merge + B03).

> **61차 재검증 (2026-06-07T15:00 UTC, frontend) — baseline 43차 대비 +2커밋·develop CLEAN·6/6 PASS·test stale·merge 3커밋·BLOCK(B03)**:
> - **frontend develop HEAD `e043eac`**(+2 vs baseline `7c0ecdc`: `1d9a701` route guard·MaskedPhone tests · `e043eac` vitest restore), working tree **CLEAN**(0 dirty).
> - **`git cat-file -e HEAD:`** `ProtectedRoute.jsx`·`AuthContext.jsx`·`App.jsx`(ProtectedRoute 래핑)·`http.js`·`authApi.js`·`MaskedPhone.test.jsx`·`ProtectedRoute.test.jsx` **PRESENT** ✓ (SEC-D12·43차 baseline **유효**).
> - develop HEAD `npm run build`: **65 modules PASS**(vite 5.4.21, JS 177.97 kB gzip 58.35 kB, CSS 24.46 kB).
> - develop HEAD `npm test`(vitest 1.6.1): **6/6 PASS** — `ProtectedRoute.test.jsx` 3 · `MaskedPhone.test.jsx` 3 (**MaskedPhone 마스킹 `010-****-5678` 정합 — FE-19 MaskedPhone 범위 충족**).
> - develop `npm audit`: **4 vulnerabilities**(3 moderate·1 critical, esbuild GHSA·vite≤6.4.1·vitest dev chain) — **SEC-008 `ed1bf22` lineage 미적용**(신규 baseline 관측, merge BLOCK 아님·planner 추적).
> - **test branch (`src/frontend-test @ e5fd48d`)**: `npm ci`+`npm run build` **36 modules PASS** · `npm test` **N/A**(Missing script) · `npm audit` **0 high·2 moderate**.
> - develop **3 commits ahead** of test (`7c0ecdc`·`1d9a701`·`e043eac`) — merge **미실행**.
> - **v1.1 ROADMAP 완료 기준**: H03·SEC-003 **PARTIAL PASS**(ProtectedRoute·roleNav) · H04 Must API **FAIL**(ModulePage placeholder·`services.js` ABSENT) · M01 **PARTIAL**(6 tests vs Must E2E·pilotPageFlows ABSENT) · R-05/R-07 J01 **FAIL** · SEC-008 **FAIL**(audit 4 vuln).
> - **TSR57 Planned(B07 #6·H05 d5654c0 lineage)**: develop **CLEAN**·MaskedPhone test PASS — **d5654c0 전용 dirty-tree/FAIL 사유 소멸**. FE-18(J01 UI·GuardianInvitationList 등) **`7c0ecdc` 위 재구현 잔여**.
> - **신규 Open 0건** — 판정 **BLOCK**(B03 merge 게이트 + v1.1 완료 기준 미충족).

> **60차 재검증 (2026-06-07T14:55 UTC, backend) — BE-10 develop 반영 확인·v2/J03 NotificationService 추가·develop 147/147 PASS·test 79/79 PASS·develop 3커밋 ahead·merge 미실행·BLOCK(merge 게이트)**:
> - **backend**: 58차(`f47ffa1` develop CLEAN 89/89·test `2799e29` 79/79·QA-B10 Open) 대비 develop HEAD **`3f9264f`**(+2커밋 — `cf6116c` BE-10 restore·`3f9264f` v2/J03 NotificationService), working tree **CLEAN**(0 dirty). 
> - **`cf6116c` (BE-10 option 2)**: `ProductionSecretValidator.java`·`PilotChecklistJwtE2eTest.java`(`pilot/`)·`MustApiEndpointRoutingTest.java`(`routing/`)·`ProductionSecretValidatorTest.java`·`RoleBasedControllerAccessTest.java`·`SevenRoleJwtLoginE2eTest.java`·`GlobalExceptionHandler` AccessDeniedException→403 — 7 files +893 lines.
> - **`3f9264f` (v2/J03)**: `NotificationService` dispatch skeleton·stub Kakao/SMS providers·`NotificationRepository`·`AttendanceService` hook — 13 files, v2 US-J03 알림톡 E2E 향.
> - **`git cat-file -e HEAD:`** `pilot/PilotChecklistJwtE2eTest`·`routing/MustApiEndpointRoutingTest`·`security/ProductionSecretValidatorTest`·`security/RoleBasedControllerAccessTest`·`security/SevenRoleJwtLoginE2eTest` **전부 PRESENT** ✓ (**QA-B10 develop HEAD 반영 확인 — BE-10 Fixed**). develop WT **CLEAN**(이관 규율 5·6 PASS).
> - **test branch (`src/backend-test @ 2799e29`) `mvn test`**: **79/79 PASS**(23 suites, Boot 3.3.1, JAR 76,466,058 B) — 60차 실측.
> - **develop HEAD (`src/backend @ 3f9264f`) `mvn test`**: **147/147 PASS**(suites: 이전 89 + BE-10 신규 58) — 60차 실측. `PilotChecklistJwtE2eTest` **8 @Test**·`MustApiEndpointRoutingTest` **24+ @Test**·`SevenRoleJwtLoginE2eTest` **7 @Test**·`RoleBasedControllerAccessTest` 7+4=11 @Test·`ProductionSecretValidatorTest` **5 @Test** PASS.
> - develop **3커밋 ahead** of test (`f47ffa1`·`cf6116c`·`3f9264f`) — merge **미실행**.
> - **QA-B10 상태 갱신**: develop HEAD `3f9264f`에 v1 baseline artifacts(`PilotChecklistJwt`·`MustApiEndpointRouting`·`ProductionSecretValidator`·`SevenRoleJwtLogin`·`RoleBasedControllerAccess`) **PRESENT** → **develop HEAD Fixed**. test branch 반영은 develop→test merge 후 완료.
> - **SEC-D11 상태 갱신**: develop history drift 해소 — develop `3f9264f`는 TSR56 `428ba7d` lineage 포함(J01·V41–V43·BE-10). test `2799e29` stale은 merge 후 해소.
> - **신규 Open 0건** — 60차 backend 신규 이슈 없음. 판정 **BLOCK**(merge 게이트 3커밋 단일).
> - **frontend**(참고 — 59차 baseline): develop·test **`e5fd48d`** 동일(스켈레톤)·develop WT DIRTY(7M+8U auth WIP)·SEC-D12·QA-B11·QA-B07 #6·QA-H05 — 판정 **BLOCK**.

> **59차 재검증 (2026-06-08T02:05, frontend) — workspace submodule baseline 단절·TSR57 재현 불가·SEC-D12·신규 QA-B11·test build 36 PASS·npm test N/A·BLOCK**:
> - **frontend**: develop HEAD **`e5fd48d`** · test HEAD **`e5fd48d`** — **동일 커밋**(TSR57 기대 develop `d5654c0`·test 18 behind **불일치**). develop WT **DIRTY** — 6M + 5 untracked(`src/auth/`·`src/components/`·`ForbiddenPage`·`styles/`·`theme.js`). **`git show HEAD:src/App.jsx`** — `/platform`·`/settings`·`/guardian`·`/dashboard/hq` **무방비**(SEC-D12). WT `App.jsx` — `ProtectedRoute` 래핑 **미커밋**(규율 5·6). **`git cat-file -e HEAD:`** `ProtectedRoute`·`AuthContext`·vitest·`LogoutButton`·`pilotPageFlows` **전부 ABSENT**. test `@e5fd48d`(src/frontend-test) `npm ci`+`npm run build` **36 modules PASS**(vite 5.4.21, JS 165.43 kB)·`npm test` **N/A**·`npm audit` **2 moderate**. develop WT build/test **미실행**(v1.1 deps·vitest 부재). **신규 Open 1건(BLOCK)**: **QA-B11**. **Open 합계 4건(BLOCK)**: QA-B10·SEC-D11·SEC-D12·QA-B11. TSR57 B07 #6·H05 **재검증 불가**. 판정 **BLOCK**.

> **58차 재검증 (2026-06-07T14:00, backend) — workspace 전환·B09·SEC-D8 Fixed·v1 baseline 회귀·merge 1커밋·Open 2·BLOCK**:
> - **backend**: develop HEAD **`f47ffa1`**(+1커밋 — J01·notification·V35–V43), working tree **CLEAN**. test HEAD **`2799e29`** — ROADMAP merged 기대 **`e8750d2`** **미달**. test `mvn test` **79/79 PASS**(23 suites, Boot **3.3.1**, JAR **76,466,058 B**) · develop `mvn test` **89/89 PASS**. **`git cat-file -e HEAD:`** `GuardianInvitationController`·V43·V41–V42·`NotificationPreferenceServiceTest` **PRESENT** · `PilotChecklistJwtE2eTest`·`ProductionSecretValidator`·`MustApiEndpointRoutingTest` **ABSENT** (**QA-B10**). develop **1커밋 ahead** — merge **미실행**. **QA-B09·SEC-D8 Fixed**. **신규 Open 2건(BLOCK)**: **QA-B10** · **SEC-D11**. 판정 **BLOCK**(merge + history regression).

> **57차 재검증 (2026-06-07T10:11, frontend) — B07 #6 18→20 files·FE-7 회귀(209/210 FAIL)·758 modules·신규 Open H05·BLOCK(B03+B07 #6)**:
> - **frontend**: 56차(`d5654c0`·18 files·205/42 PASS) 대비 develop HEAD **`d5654c0` 불변**·working tree **DIRTY 확대** — **14M+6U=20 files**. 신규: `ClientPhotoField.test.jsx`·`GuardianListCard.test.jsx`(untracked)·`ClientFormPage.jsx`(modified). **이관 규율 5 — HEAD Fixed 유지**: `LogoutButton`·`GuardianInvitationAcceptPage`·`GuardianInvitationAcceptForm`·`PublicAuthLayout`·`BillingPage.layout.test`·`services.js` **PRESENT** · WT-only `DateInput`·`GuardianInvitationList`·`GuardianListCard.test` **HEAD ABSENT**. SEC-005 AuthContext localStorage/sessionStorage **0건**. develop WT `npm run build`(vite 6.4.3) **758 modules SUCCESS**(3 청크: react-vendor 166.34·index 190.72·recharts 393.53 kB, CSS 52.85 kB)·`npm test`(vitest 4.1.8) **209 tests/44 files — 1 FAIL**(`GuardianListCard.test.jsx` — MaskedPhone `010-****-5678` vs 기대 `/010-1234-5678/`, **FE-7 회귀**)·`npm audit` **0 vulnerabilities**. test `@e5fd48d`(src/frontend-test) build **36 modules PASS**·`npm test` **N/A**·**18 behind**·audit 0h/2mod. **신규 Open 1건(HIGH)**: **QA-20260607-H05**. Planned BLOCK **B03 + B07 #6**. 판정 **BLOCK**(dirty-tree·test FAIL PASS 금지).

> **56차 재검증 (2026-06-07T10:01, 양 스트림) — backend 54차 CLEAN→DIRTY 재오염(J01 guardian_invitations WIP·27 files·신규 BLOCK QA-B09) + frontend B07 #6 확대(15→18 files)·HEAD Fixed 유지·Open 1·BLOCK(merge+B09+B07 #6)**:
> - **backend**: 54차(`428ba7d` CLEAN·253/253·merge 3커밋 ahead) 대비 develop HEAD **`428ba7d` 불변**·working tree **CLEAN→DIRTY** — **15M+12U=27 files**. 신규 WIP: **`GuardianInvitationController.java`**·**`GuardianInvitationService.java`**·**`InvitationTokenService.java`**·**`InvitationExpiredException.java`**·**`GuardianInvitationEntity.java`**·**`GuardianInvitationRepository.java`**·**`AcceptGuardianInvitationRequest.java`**·**`AcceptGuardianInvitationResponse.java`**·**`CreateGuardianInvitationRequest.java`**·**`GuardianInvitationResponse.java`**·**`V43__guardian_invitations.sql`**·**`GuardianInvitationServiceTest.java`**(J01 `guardian_invitations` 백엔드 API WIP); modified `ClientController.java`·`ClientResponse.java`·`ClientService.java`·`GlobalExceptionHandler.java`·`SecurityConfig.java` + 10 test files. **이관 규율 5 — HEAD Fixed @ `428ba7d` 유지**: `git cat-file -e HEAD:` `PilotChecklistJwtE2eTest`·`V41`·`V42`·`notification/`·`NotificationPreferenceServiceTest` **PRESENT** · `GuardianInvitationController`·`V43` **HEAD ABSENT**(이관 규율 6·8 위반). test `mvn test`(@`e8750d2`) **213/213 PASS**(75 suites)·JAR **82,868,029 B**·Spring Boot 3.5.3·SEC-007 `ProductionSecretValidator` PRESENT. develop **3커밋 ahead of test** — merge **미실행**. **신규 Open 1건(BLOCK)**: **QA-B09**(backend J01 WIP·27 files dirty-tree). 판정 **BLOCK**(dirty-tree PASS 금지).
> - **frontend**(교차): develop HEAD **`d5654c0` 불변**(55차 대비)·working tree **DIRTY 확대** — 55차 11M+4U=15 → **14M+4U=18 files**(신규 modified: `PaymentRecordModal.jsx`(+test)·`index.js`). B07 #6 **Planned 확대** — HEAD Fixed @ `d5654c0` 규율 5 유효. test `@e5fd48d` build 36·`npm test` N/A·18 behind.

> **55차 재검증 (2026-06-07T09:29, frontend) — 53차 CLEAN→DIRTY(B07 recurrence #6)·HEAD Fixed 유지·WT 205/42·758 modules·Open 1·BLOCK(B03+B07 #6)**:
> - **frontend**: 53차(`d5654c0` CLEAN·199/40·B03 단일) 대비 develop HEAD **`d5654c0` 불변**·working tree **CLEAN→DIRTY** — **11M+4U=15 files**. 신규 WIP: **`DateInput.jsx`(+test)**·**`GuardianInvitationList.jsx`(+test — J01 초대 목록 UI)** + modified `ClientDetailPage`(+98)·`GuardianInviteModal`·`GuardianListCard`·`LoginHistoryPanel`·`AuditLogPanel`·`ClientPhotoField`·`services.js`·`GuardianInvitationAcceptPage`(+test)·`components.css`. **이관 규율 5 — HEAD Fixed @ `d5654c0` 유지**: `git cat-file -e HEAD:` `LogoutButton`·`GuardianInvitationAcceptPage`·`GuardianInvitationAcceptForm`·`PublicAuthLayout`·`BillingPage.layout.test`·`services.js`(acceptGuardianInvitationApi) **PRESENT** · WT-only `DateInput`·`GuardianInvitationList` **HEAD ABSENT**. SEC-005 AuthContext localStorage/sessionStorage **0건**. develop WT `npm run build`(vite 6.4.3) **758 modules SUCCESS**(3 청크: react-vendor 166.34·index 190.55·recharts 393.53 kB, CSS 52.85 kB)·`npm test`(vitest 4.1.8) **205 tests/42 files PASS**(53차 HEAD 199/40 → WT +6/+2, FE-7 회귀 없음)·`npm audit` **0 vulnerabilities**(high·all). test `@e5fd48d`(src/frontend-test) build **36 modules PASS**·`npm test` **N/A**(Missing script)·**18 behind**·audit 0h/2mod. **신규 Open 1건(BLOCK)**: **QA-B07 recurrence #6**. Planned BLOCK **B03 + B07 #6**. 판정 **BLOCK**(dirty-tree PASS 금지).
> - **backend**(교차 — 54차 baseline): develop `428ba7d` CLEAN·253/253·merge 3커밋·Open 0. 변경 없음.

> **54차 재검증 (2026-06-07T18:23, backend) — COD 36 `428ba7d` B02 #6·B08 #2 Fixed·develop CLEAN·253/253 HEAD·merge 3커밋·Open 0·BLOCK(merge 단일)**:
> - **backend**: 53차(`c3b8716` DIRTY·213/213·253/253 WT) 대비 develop HEAD `c3b8716`→**`428ba7d`**(+1커밋 COD 36차 `feat(v2): V42 consent CHECK·temporal + NotificationPreferenceServiceTest`, 2 files +215), working tree **DIRTY→CLEAN**. **B02 #6·B08 #2 Fixed — TSR 독립 검증 PASS**: `git -C src/backend status --porcelain` **0줄**, `git cat-file -e HEAD:` V42·`NotificationPreferenceServiceTest`(4 @Test) **PRESENT**(이관 규율 5·6·8). test `mvn test`(@`e8750d2`) **213/213 PASS**(75 suites)·develop HEAD `mvn test` **253/253 PASS**(92 suites)·`package` SUCCESS **82,868,029 B**·Spring Boot 3.5.3·SEC-007 `ProductionSecretValidator` **PRESENT**. develop **3커밋 ahead of test** — merge **미실행**. **신규 Open 0건** — dirty-tree **소멸**, Planned BLOCK = **merge 게이트 단일**. 판정 **BLOCK**.

> **53차 재검증 (2026-06-07T08:36, frontend) — COD 35차 `d5654c0` FE-17 J01 수락 UI·LogoutButton·레이아웃 회귀 커밋·working tree CLEAN·B07 recurrence #5 Fixed·잔여 BLOCK = B03 merge 게이트 단일·Open 0**:
> - **frontend**: 52차(`0b9b001` DIRTY 20 files·B07 #5 Open) 대비 develop HEAD `0b9b001`→**`d5654c0`**(+1커밋 COD 35차 `feat(v1.1): FE-17 J01 보호자 초대 수락 UI·LogoutButton·레이아웃 회귀 (B07 #5)`, 25 files +823/-57, origin/develop **18 ahead**), develop working tree **CLEAN**(0 dirty — 52차 DIRTY 20 files **일괄 커밋·B07 #5 소멸**). **QA-B07 recurrence #5 Fixed 확정 — TSR 53차 독립 검증 PASS**: `git -C src/frontend status` **0 lines**, `git cat-file -e HEAD:` `src/components/ui/LogoutButton.jsx`·`src/pages/GuardianInvitationAcceptPage.jsx`·`src/components/ui/GuardianInvitationAcceptForm.jsx`·`src/components/ui/PublicAuthLayout.jsx`·`src/pages/BillingPage.layout.test.jsx` **전부 PRESENT**(이관 규율 5 PASS). SEC-005 AuthContext localStorage/sessionStorage **0건**. `acceptGuardianInvitationApi` → `src/api/services.js`(+19 lines) **HEAD PRESENT**. develop HEAD(clean) `npm run build`(vite 6.4.3) **756 modules SUCCESS**(3 청크: react-vendor 166.34·index 186.68·recharts 393.53 kB, CSS 52.52 kB)·`npm test`(vitest 4.1.8) **199 tests/40 files PASS**(52차 WT 194/38 → HEAD 199/40, FE-7 회귀 없음)·`npm audit` **0 vulnerabilities**(high·all). test `@e5fd48d`(src/frontend-test) build **36 modules PASS**·`npm test` **N/A**(Missing script)·**18 behind**. **신규 Open 0건** — B07 #5 소멸·잔여 Planned BLOCK = **B03 merge 게이트 단일**(v1.1 `merge_status: pending`·develop→test 18 commits 미머지·v1.1 잔여 완료 기준: Must 라이브 E2E·J01 백엔드 API·`merge_status: ready`). 판정 **BLOCK**(B03 단일).
> - **backend**(교차 — 53차 backend baseline 불변): develop `c3b8716` DIRTY·253/253 WT·213/213 test·B02 #6·B08 #2 Planned. 변경 없음.

> **53차 재검증 (2026-06-07T17:32, backend) — 51차 대비 HEAD·dirty-tree·merge 불변·WT 253/253(+1)·Open 0·BLOCK 유지**:
> - **backend**: 51차(`c3b8716` DIRTY·213/213·252/252 WT) 대비 **변화 최소** — develop HEAD **`c3b8716` 불변**·working tree **DIRTY 불변**(2 untracked: V42 54 lines + `NotificationPreferenceServiceTest` **8050 B/4 @Test**). **이관 규율 5 — HEAD Fixed 유지**: `git cat-file -e HEAD:` `PilotChecklistJwtE2eTest`·`V41`·`notification/` 9 java **PRESENT** · V42·domain test **HEAD ABSENT**. test `mvn test`(@`e8750d2`) **213/213 PASS**(75 suites)·`package` SUCCESS **82,868,029 B**·Spring Boot 3.5.3·SEC-007 `ProductionSecretValidator` **PRESENT**. develop WT `mvn test` **253/253 PASS**(92 suites, +1 vs 51차 252 — domain test 3→4 @Test). develop **2커밋 ahead of test** — merge **미실행**. **신규 Open 0건** — B02 #6·B08 #2 **Planned 유지**. Planned BLOCK = **merge(2커밋) + B02 #6 + B08 #2**. 판정 **BLOCK**(dirty-tree PASS 금지).
> - **frontend**(교차 — 52차 baseline): develop `0b9b001` DIRTY·194/38·B07 #5 Planned. 변경 없음.

> **52차 재검증 (2026-06-07T08:03, frontend) — 50차 CLEAN→DIRTY(B07 recurrence #5)·HEAD Fixed 유지·WT 194/38 PASS·Open 1**:
> - **frontend**: 50차(`0b9b001` CLEAN·187/35·B03 merge 게이트) 대비 develop HEAD **`0b9b001` 불변**·working tree **CLEAN→DIRTY** — **15M+5U=20 files**. 신규 untracked: **`LogoutButton.jsx`(+test)**·**`BillingPage.layout.test.jsx`**·**`GuardianInvitationAcceptPage.jsx`(+test — J01 수락 UI WIP)**. modified: `App.jsx`·`AuthContext`(+test)·`AppShell`·Recharts 3종·`BillingPage`·`GuardianDetailPage`·`PaymentPage`·`services.js`·스타일. **이관 규율 5 — HEAD Fixed 유지**: `git cat-file -e HEAD:` `ChartContainer`·`AttendancePage.layout.test.jsx`·`vite.config.js`·`AuthContext`·`pilotChecklist` **PRESENT** · WT-only **HEAD ABSENT**. develop WT `npm run build` **754 modules PASS**(+2 vs 752)·`npm test`(vitest 4.1.8) **194 tests/38 files PASS**(+7/+3 vs 187/35, FE-7 회귀 없음)·`npm audit` **0건**. test `@e5fd48d` build **36 modules PASS**·`npm test` **N/A**·**17 behind**. **신규 Open 1건(BLOCK)**: **QA-B07 recurrence #5**. Planned BLOCK **B03 + B07 #5**. 판정 **BLOCK**(dirty-tree PASS 금지).
> - **backend**(교차 — 51차 baseline): develop `c3b8716` DIRTY·252/252 WT·213/213 test·B02 #6·B08 #2 Planned. 변경 없음.

> **51차 재검증 (2026-06-07T07:58, backend) — 50차 대비 상태 완전 불변·dirty-tree·merge 게이트 BLOCK·ROADMAP COD 35 false Fixed·Open 0**:
> - **backend**: 50차(`c3b8716` DIRTY·213/213·252/252 WT) 대비 **변화 0건** — develop HEAD **`c3b8716` 불변**·working tree **DIRTY 불변**(2 untracked: V42 consent CHECK + `NotificationPreferenceServiceTest` 3 @Test). **이관 규율 5 — HEAD Fixed 유지**: `git cat-file -e HEAD:` `PilotChecklistJwtE2eTest`·`V41`·`notification/` 9 java **PRESENT** · V42·domain test **HEAD ABSENT**. test `mvn test`(@`e8750d2`) **213/213 PASS**(75 suites)·`package` SUCCESS **82,868,029 B**·Spring Boot 3.5.3. develop WT `mvn test` **252/252 PASS**(92 suites, +3). develop **2커밋 ahead of test** — merge **미실행**. **⚠ ROADMAP COD 35 Fixed 주장 TSR FAIL** — planner `[x]` 철회 필요. **신규 Open 0건** — B02 #6·B08 #2 Planned 유지. Planned BLOCK = **merge(2커밋) + B02 #6 + B08 #2**. 판정 **BLOCK**(dirty-tree PASS 금지).
> - **frontend**(교차 — 50차 baseline): develop `0b9b001` CLEAN·187/35·B03 merge 게이트. 변경 없음.

> **50차 재검증 (2026-06-07T07:17, frontend) — COD 34차 `0b9b001` (+1커밋·AttendancePage 레이아웃 회귀·ds-* 유틸리티 전환)·working tree CLEAN·잔여 BLOCK = B03 merge 게이트 단일·Open 0**:
> - **frontend**: 49차(`c98f98d` CLEAN·186/34·B03 merge 게이트) 대비 develop HEAD `c98f98d`→**`0b9b001`**(+1커밋 COD 34차 `fix(v1.1): Must 페이지 UXD ds-* 유틸리티 전환·AttendancePage 레이아웃 회귀 테스트`, **17 ahead**). develop working tree **CLEAN**(0 dirty). **이관 규율 5 PASS** — `git -C src/frontend status --porcelain` **0줄**, `git cat-file -e HEAD:` `ChartContainer`·`FeeScheduleTable`·`AuthContext`·`pilotChecklist`·`chartColors`·`vite.config.js`·`sevenRoleJwtLogin.test.jsx`·`sevenRoleRouteMatrix.js` **전부 PRESENT**. SEC-005 AuthContext localStorage/sessionStorage **0건**. 신규 커밋 변경 범위: `AttendanceAbsentModal`·`BatchProgressSteps`·`CheckoutModal`·`FeeRateHistoryPanel`·`HealthAbnormalBanner`·`MedicationDuplicateAlert`·`PasswordResetRequestModal`·`PlatformOrgDetailModal`·`SessionTimeoutModal` — 인라인 style→ds-* 유틸리티 전환(B07 예방) + `AttendancePage.layout.test.jsx` 레이아웃 회귀 자동화 추가. develop HEAD(clean) `npm run build` **752 modules PASS**(vite 6.4.3, 3청크: react-vendor 166.34·index 181.88·recharts 393.53 kB, CSS 52.95 kB)·`npm test`(vitest 4.1.8) **187 tests/35 files PASS**(49차 186/34 → +1/+1 `AttendancePage.layout.test.jsx`)·`npm audit` **0건**. test `@e5fd48d` build 36·npm test N/A·**17 behind**. **신규 Open 0건** — B03 merge 게이트 단일·FE-15·B07 #3·#4 소멸. 판정 **BLOCK**(B03).
> - **backend**(교차 — 50차 backend baseline): develop `c3b8716` DIRTY(V42 consent·`NotificationPreferenceServiceTest` 3 @Test — B02 recurrence #6·B08 #2)·test `e8750d2` stale·213/213·develop WT 252/252·**Open 1건(BLOCK)**. 변경 없음.

> **50차 재검증 (2026-06-07T16:15, backend) — 48차 CLEAN→DIRTY 재오염(V42 + NotificationPreferenceServiceTest 3 @Test)·HEAD Fixed 유지·merge 게이트 + dirty-tree BLOCK·Open 1**:
> - **backend**: 48차(`c3b8716` CLEAN·B02 #5·B08 Fixed·249/249 committed) 대비 develop HEAD **`c3b8716` 불변**·working tree **CLEAN→DIRTY** — 2 untracked: ① `V42__guardian_notification_preferences_consent_temporal.sql`(consent CHECK·temporal monotonicity — v2 B08 follow-up, API_SPEC §11-3) ② `NotificationPreferenceServiceTest.java`(128 lines, **3 @Test**). **이관 규율 5 — HEAD Fixed 유지**: `git cat-file -e HEAD:` `PilotChecklistJwtE2eTest`·`V41`·`notification/` 9 java **PRESENT** · V42·domain test **HEAD ABSENT**. test `mvn test`(@`e8750d2`) **213/213 PASS**(75 suites, 0 fail)·`package` SUCCESS **82,868,029 B**·Spring Boot 3.5.3. develop WT `mvn test` **252/252 PASS**(92 suites, +3 vs committed 249). develop **2커밋 ahead of test** — merge **미실행**. **신규 Open 1건(BLOCK)**: QA-B02 recurrence #6 + B08 v2 follow-up WIP. Planned BLOCK = **merge(2커밋) + B02 #6 + B08 #2**. 판정 **BLOCK**(dirty-tree PASS 금지).
> - **frontend**(교차 — 49차 baseline): develop `c98f98d` CLEAN·186/34·B03 merge 게이트. 변경 없음.

> **49차 재검증 (2026-06-07T15:45, frontend) — B07 #4 신호 해소(COD 33차 `c98f98d`)·FE-15 코드 스플릿 Fixed·working tree CLEAN·잔여 BLOCK = B03 merge 게이트 단일·Open 0**:
> - **frontend**: 47차(`4be0938` CLEAN·비차단 LOW JS 744.95 kB) + TSR 48차 backend 라운드 교차 관측(frontend `4be0938` 재오염 5 files — B07 recurrence #4 신호) 대비 develop HEAD `4be0938`→**`c98f98d`**(+1커밋 `fix(v1.1): UXD 인라인 style 제거·FE-15 코드 스플릿·레이아웃 회귀 테스트`, 7 files +145/-23, origin/develop 대비 **16 ahead**). develop working tree **CLEAN**(0 dirty — 재오염 5 files `c98f98d` 일괄 커밋, **B07 #4 신호 소멸·정식 Open 미등록**). **이관 규율 5 PASS** — `git -C src/frontend status --porcelain` **0줄**, `git cat-file -e HEAD:` `ChartContainer`·`FeeScheduleTable`·`AuthContext`·`pilotChecklist`·`chartColors`·`vite.config.js` **전부 PRESENT**. SEC-005 AuthContext localStorage/sessionStorage **0건**. **FE-15 코드 스플릿 정식 Fixed** — `vite.config.js` `build.rollupOptions.output.manualChunks` 추가 → 47차 단일 JS 청크 **744.95 kB**(>500 kB vite 경고) → **3 청크 분리**(`react-vendor` 166.34 kB gzip 54.31·`index` 182.52 kB gzip 48.17·`recharts` 393.53 kB gzip 107.68, 최대 청크 **393.53 kB < 500 kB**) — vite 경고 **해소**. develop HEAD(clean) `npm run build` **752 modules PASS**(vite 6.4.3, CSS 52.04 kB)·`npm test`(vitest 4.1.8) **186 tests/34 files PASS**(47차 185/33 → +1/+1 `ClientDetailPage.layout.test.jsx` 레이아웃 회귀)·`npm audit` **0 vulnerabilities**(high·all). test `@e5fd48d`(src/frontend-test) build **36 modules PASS**·`npm test` **N/A**(Missing script)·`npm audit` 0 high·2 moderate·**16 behind**. **신규 Open 0건** — B07 #4 신호·FE-15 LOW 사유 **소멸**, 잔여 Planned BLOCK = **B03 merge 게이트 단일**(v1.1 `merge_status: pending`·develop→test 16 commits 미머지·잔여 완료 기준 Must 라이브 E2E·J01 백엔드 API). 판정 **BLOCK**(B03 단일).
> - **backend**(교차 — 48차 baseline): develop `c3b8716`·test `e8750d2`·**B02 #5·B08 Fixed**(TSR 독립 검증 PASS)·working tree CLEAN·test 213/213·develop committed 249/249·develop 2커밋 ahead(merge 미실행). 판정 **BLOCK**(merge 게이트).

> **48차 재검증 (2026-06-07T15:35, backend) — COD 32차 B02 #5·B08 정식 Fixed TSR 독립 검증 PASS·dirty-tree 소멸·잔여 merge 게이트 단일·Open 0**:
> - **backend**: 46차(dirty-tree 3M+4U·COD false Fixed) 대비 develop HEAD `e8750d2`→**`c3b8716`**(+2커밋 COD 32차 — `feac558` B08 notification·`c3b8716` B02 #5 PilotChecklistJwtE2eTest), develop working tree **DIRTY(3M+4U)→CLEAN**. **QA-B02 #5·B08 정식 Fixed — TSR 독립 검증 PASS**: `git -C src/backend status --porcelain` **0줄**, `git cat-file -e HEAD:` `security/PilotChecklistJwtE2eTest.java`·`db/migration/V41__guardian_notification_preferences.sql`·`notification/` 9 java(`NotificationPreferenceService`·`GuardianNotificationPreferenceController`·`StaffGuardianNotificationPreferenceController`·`NotificationPreferenceEntity`·`Repository`·DTO 2·controller test 2) **전부 PRESENT**(이관 규율 5·6·8 PASS — 46차 false Fixed 패턴과 대조). develop committed `mvn test`(@`c3b8716`, clean) **249/249 PASS**(91 suites, 0 fail) — 46차 WT-only 249가 **HEAD 커밋으로 전환**. test `mvn test`(@`e8750d2`) **213/213 PASS**(75 suites)·`package` SUCCESS **82,868,029 B**·Spring Boot 3.5.3. develop HEAD `@Test` grep **235**(surefire 249). **develop 2커밋 ahead of test** — develop→test merge **미실행**. **신규 Open 0건** — backend dirty-tree·false Fixed 사유 **전부 소멸**, 잔여 BLOCK = **develop→test merge 게이트 단일**(test에 B02 #5 v1 P1–P8 live E2E·B08 미반영). **backend 30+회 dirty-tree/false-Fixed 정체 종결**. 판정 **BLOCK**(merge 게이트 단일).
> - **frontend**(교차 관측, LOW): develop HEAD `4be0938`(47차 Fixed) working tree **재오염 5 files**(`ClientDetailPage`·`ClientFormPage`·`GuardiansPage`·`PlatformPage`·`components.css`) — **B07 recurrence #4 신호**(HEAD Fixed 유효, frontend 라운드 확인 필요). frontend-test `@e5fd48d` stale(16 behind).

> **47차 재검증 (2026-06-07T14:45, frontend) — B07 #3 Fixed TSR 독립 검증 PASS(COD 31차 `4be0938`)·잔여 BLOCK = B03 merge 게이트 단일·Open 0**:
> - **frontend**: 45차(`3fdc266` DIRTY 76 files) 대비 develop HEAD `3fdc266`→**`4be0938`**(+1커밋 COD 31차 `feat(v1.1/v1.2): Recharts·플랫폼·청구·건강·운영/보안 UI 일괄 커밋 (B07 #3)`, origin/develop 대비 **15 ahead**). develop working tree **DIRTY 76 files → CLEAN**(0 dirty). **QA-B07 recurrence #3 정식 Fixed — TSR 독립 검증 PASS**: `git status --porcelain` **0줄**, `git cat-file -e HEAD:` `ChartContainer`·`AttendanceRateChart`·`HealthTrendChart`·`FeeScheduleTable`·`CopayRateTable`·`HealthAlertList`·`NhisImportGuidePanel`·`BillingStatusConfirmModal`·`GuardianDailySummary`·`FeeRateHistoryPanel`·`AuditLogPanel`·`BackupSettingsPanel`·`LoginHistoryPanel`·`PasswordChangeModal`·`chartColors.js`·`dashboardWidgets.js`·`pilotChecklist.js`·`sevenRoleRouteMatrix.js` **전부 PRESENT**(이관 규율 5 PASS — backend B02 #5·B08 false Fixed 패턴과 대조). SEC-005: `AuthContext.jsx` localStorage/sessionStorage **0건**(메모리 세션 유효). develop HEAD(clean) `npm test`(vitest 4.1.8) **185 tests/33 files PASS**·`npm run build`(vite 6.4.3) **752 modules SUCCESS**(JS 744.95 kB gzip 211.42 kB, CSS 51.49 kB)·`npm audit` **0 vulnerabilities**(high·all). `recharts ^2.15.4` 커밋 반영. test `@e5fd48d`(src/frontend-test) build **36 modules PASS**·`npm test` **N/A**(Missing script)·**15 behind**. **신규 Open 0건** — B07 #3 dirty 사유 **소멸**, 잔여 Planned BLOCK = **B03 merge 게이트 단일**(v1.1 `merge_status: pending`·develop→test 15 commits 미머지·잔여 완료 기준 Must 라이브 E2E·J01 백엔드 API). **비차단 관측(LOW)**: 단일 JS 청크 744.95 kB(>500 kB vite 경고) — `manualChunks` 코드 스플릿 권고, merge BLOCK 아님. 판정 **BLOCK**(B03 단일).
> - **backend**(교차 — 46차 baseline): develop·test `@e8750d2`·dirty-tree 3M+4U(B02 #5·B08)·COD Fixed FAIL·test 213/213·WT 249/249. Planned BLOCK B02 #5 + B08. 판정 **BLOCK**.

> **46차 재검증 (2026-06-07T14:30, backend) — 44·45차 대비 dirty-tree 확대(3M+4U)·WT 249/249 PASS(+6)·BLOCK 유지·Open 0**:
> - **backend**: develop·test HEAD **`@e8750d2` 동일**(0 commits diff), test working tree **CLEAN**. `mvn test`(test) **213/213 PASS**(75 suites)·JAR **82,868,029 B**. develop working tree **DIRTY 확대** — 44차 1M+4U → **3M+4U**: ① `.gitignore` +`data/backups/` 1M ② **modified** `MustApiEndpointRoutingTest`(+64 lines, B08 notification routing) · `RoleBasedControllerAccessTest`(+93 lines, B08 RBAC) ③ untracked B02 #5 `PilotChecklistJwtE2eTest`(22 @Test) + B08(V41 + 7 java + **8 @Test**). **COD Fixed(B02 #5·B08) TSR 독립 검증 FAIL** — HEAD ABSENT(이관 규율 5). develop WT `mvn test` **249/249 PASS**(91 suites, +6 vs 44차). HEAD `@Test` **199**·WT surefire **249**. **신규 Open 0**·Planned BLOCK **B02 #5 + B08 + frontend B03·B07 #3**. 판정 **BLOCK**.

> **45차 재검증 (2026-06-07T14:02, frontend) — 43차 대비 B07 #3 dirty-tree 확대(72→76 files)·WT 181/30 PASS·B03 BLOCK 유지·Open 0**:
> - **frontend**: develop HEAD **`3fdc266` 불변**(43차 대비), working tree **확대** — 43차 38M+34U=72 → **40M+36U=76 files**. 신규 WIP: **`FeeScheduleTable`(+test)** + 기존 Recharts·청구·copay·보호자·건강·NHIS·설정 WIP. 이관 규율 5 — HEAD Fixed(`pilotPageFlows`·`FeeRateHistoryPanel`·api·AuthContext) **PRESENT**·WT-only(`ChartContainer`·`FeeScheduleTable`·`BillingStatusConfirmModal` 등) **HEAD ABSENT**. WT `npm run build` **749 modules PASS**(+1)·`npm test` **181/30 PASS**(+2/+1)·`npm audit` **0건**(FE-7). test `@e5fd48d`(src/frontend-test) build **36 modules PASS**·`npm test` **N/A**·14 behind·audit 0h/2mod. **B07 #3 Planned 범위 확대** — **신규 Open 0**. Planned BLOCK **B03 + B07 #3**. 판정 **BLOCK**.

> **44차 재검증 (2026-06-07T04:59, backend) — 42·43차 대비 상태 불변·test 213/213·WT 243/243 PASS·BLOCK 유지·Open 0**:
> - **backend**: develop·test HEAD **`@e8750d2` 동일**(0 commits diff), test working tree **CLEAN**. `mvn test`(test) **213/213 PASS**(75 suites)·JAR **82,868,029 B**. develop working tree **DIRTY 불변** — ① `.gitignore` +`data/backups/` 1M ② B02 #5 `PilotChecklistJwtE2eTest`(634 lines/22 @Test) ③ B08 notification WIP(V41 + 7 java + **8 @Test**). **COD Fixed(B02 #5·B08) TSR 독립 검증 FAIL** — HEAD ABSENT(이관 규율 5). develop WT `mvn test` **243/243 PASS**(88 suites). HEAD `@Test` **199**·WT **229**(+30). **신규 Open 0**·Planned BLOCK **B02 #5 + B08 + frontend B03·B07 #3**. 판정 **BLOCK**.

> **43차 재검증 (2026-06-07T13:27, frontend) — B07 #3 dirty-tree 확대(61→72 files)·WT 179/29 PASS·merge 게이트 BLOCK 유지·Open 0건**: develop HEAD **`3fdc266` 불변**(41차 대비), working tree **확대** — 41차 37M+24U=61 → **38M+34U=72 files**. 신규 WIP: `BillingStatusConfirmModal`·`CopayRateTable`·`GuardianDailySummary`·`HealthAlertList`·`NhisImportGuidePanel`(+tests) + 기존 Recharts·Platform·감사·설정 WIP. 이관 규율 5 — HEAD Fixed(`pilotPageFlows`·`FeeRateHistoryPanel`·api·AuthContext) **PRESENT**·WT-only(`ChartContainer`·`LoginHistoryPanel`·신규 5종) **HEAD ABSENT**. WT `npm run build` **748 modules PASS**(+5)·`npm test` **179/29 PASS**(+10/+5)·`npm audit` **0건**(FE-7). test `@e5fd48d`(src/frontend-test) build **36 modules PASS**·`npm test` **N/A**·14 behind·audit 0h/2mod. **B07 #3 Planned 범위 확대** — 신규 Open 0. Planned BLOCK **B03 + B07 #3**. 판정 **BLOCK**.

> **42차 재검증 (2026-06-07T13:25, backend) — 40·41차 대비 상태 불변·WT 243/243 PASS(+3)·B08 @Test 8·BLOCK 유지·Open 0**:
> - **backend**: develop·test HEAD **`@e8750d2` 동일**(0 commits diff), test working tree **CLEAN**. `mvn test`(test) **213/213 PASS**(75 suites)·JAR **82,868,029 B**. develop working tree **DIRTY 불변** — ① `.gitignore` +`data/backups/` 1M ② B02 #5 `PilotChecklistJwtE2eTest`(634 lines/22 @Test) ③ B08 notification WIP(V41 + 7 java + **8 @Test**, 40차 5→42차 8). **COD Fixed(B02 #5·B08) TSR 독립 검증 FAIL** — HEAD ABSENT(이관 규율 5). develop WT `mvn test` **243/243 PASS**(88 suites, +3). HEAD `@Test` **199**·WT **229**(+30). **신규 Open 0**·Planned BLOCK **B02 #5 + B08 + frontend B03·B07 #3**. 판정 **BLOCK**.

> **41차 재검증 (2026-06-07T12:52, frontend) — 39차 대비 상태 불변(±1 modified)·WT 169/24 PASS·merge 게이트 BLOCK 유지·Open 0건**: develop HEAD **`3fdc266` 불변**, working tree **37M+24U=61 files**(39차 36M+24U=60 — `pilotPageFlows.test.jsx`·`package.json`/`package-lock.json` 등 1 modified 추가). Recharts·Platform·감사·백업·비밀번호·로그인이력 WIP **동일 범위**. 이관 규율 5 — HEAD Fixed(`pilotPageFlows`·`FeeRateHistoryPanel`·api·AuthContext) **PRESENT**·WT-only(`ChartContainer`·`LoginHistoryPanel`) **HEAD ABSENT**. WT `npm run build` **743 modules PASS**·`npm test` **169/24 PASS**·`npm audit` **0건**(FE-7). test `@e5fd48d`(src/frontend-test) build **36 modules PASS**·`npm test` **N/A**·14 behind·audit 0h/2mod. **B07 #3 Planned 유지** — 신규 Open 0. Planned BLOCK **B03 + B07 #3**. 판정 **BLOCK**.

> **40차 재검증 (2026-06-07T12:45, backend) — COD false Fixed 재확인·`.gitignore` 부분 진전·WT 240/240 PASS·BLOCK 유지·Open 0**:
> - **backend**: develop·test HEAD **`@e8750d2` 동일**(38차 대비), test working tree **CLEAN**. `mvn test`(test) **213/213 PASS**(75 suites)·JAR **82,868,029 B**. develop working tree **DIRTY** — ① **1 modified** `.gitignore`(+`data/backups/`, 미커밋) ② **4 untracked** B02 #5 `PilotChecklistJwtE2eTest`(22 @Test) + B08 notification(6 java + V41 + 5 @Test). **COD Fixed(B02 #5·B08) TSR 독립 검증 FAIL** — HEAD ABSENT(이관 규율 5). develop WT `mvn test` **240/240 PASS**(+27). HEAD `@Test` **199**·WT **226**. **신규 Open 0**·Planned BLOCK **B02 #5 + B08 + frontend B03·B07 #3**. 판정 **BLOCK**.

> **39차 재검증 (2026-06-07T12:09, frontend) — B07 #3 dirty-tree 확대(44→60 files)·WT 169/24 PASS·B03 BLOCK 유지·Open 0**:
> - **frontend**: develop HEAD **`3fdc266` 불변**(37차 대비), working tree **확대** — 37차 26M+18U=44 → **36M+24U=60 files**. 신규 WIP: `LoginHistoryPanel`(+test)·`PasswordChangeModal`(+test)·`PasswordResetRequestModal`(+test)·`PlatformOrgDetailModal`(+test)·`SettingsPage.test.jsx`·`HealthTrendChart.test.jsx` + 기존 Recharts·감사·백업·FilterChips. 이관 규율 5 — HEAD Fixed(`pilotPageFlows`·`FeeRateHistoryPanel`·api·AuthContext 등) **PRESENT 유효**. WT `npm run build` **743 modules PASS**(+2)·`npm test` **169/24 PASS**(+8/+4)·`npm audit` **0건**(FE-7). test `@e5fd48d` build 36·npm test N/A·14 behind. **B07 #3 Planned 범위 확대** — 신규 Open 0. Planned BLOCK **B03 + B07 #3**. 판정 **BLOCK**.

> **37차 재검증 (2026-06-07T11:30, frontend) — B07 #3 dirty-tree 확대(26→44 files)·WT 161/20 PASS·B03 BLOCK 유지**:
> - **frontend**: develop HEAD **`3fdc266` 불변**, working tree **확대** 35차 18M+8U=26 → **26M+18U=44 files**(`AuditLogPanel`·`BackupSettingsPanel`·`PasswordChangeModal`·`FilterChips.test` + Recharts·Platform WIP). WT `npm run build` **741 modules PASS**(+3)·`npm test` **161/20 PASS**(+17/+7)·`npm audit` **0건**. test `@e5fd48d` build 36·npm test N/A·14 behind. 이관 규율 5 HEAD Fixed PRESENT. **Open 0건(frontend)** — Planned BLOCK **B03 + B07 #3**(범위 확대). 판정 **BLOCK**.

> **38차 재검증 (2026-06-07T12:05, backend) — 36·37차 대비 상태 불변·Maven 213/213 재현·Open 0·BLOCK 유지**:
> - **backend**: develop·test HEAD **`@e8750d2` 동일**(0 commits diff), test working tree **CLEAN**. `mvn test`(test) **213/213 PASS**(75 suites, 0 fail, Spring Boot 3.5.3)·`package` SUCCESS(**82,868,029 B**). SEC-007: test `ProductionSecretValidator` **PRESENT**. develop working tree **DIRTY 불변** — untracked 5 entries: ① B02 #5 `PilotChecklistJwtE2eTest`(634 lines/22 @Test, Planned) ② B08 v2 `notification_preferences` WIP(6 java + V41 + 5 @Test, Planned) ③ `data/backups/` manifest(로컬 산출물). HEAD `@Test` **199**·WT **226**(+27). 이관 규율 5 — `PilotChecklistJwtE2eTest`·notification·V41 **HEAD ABSENT**. **Open 0건**·Planned BLOCK **B02 #5 + B08 + frontend B03·B07 #3**. 판정 **BLOCK**.

> **36차 재검증 (2026-06-07T11:25, backend) — 34·35차 대비 상태 불변·Maven 213/213 재현·Open 0·BLOCK 유지**:
> - **backend**: develop·test HEAD **`@e8750d2` 동일**(0 commits diff), test working tree **CLEAN**. `mvn test`(test) **213/213 PASS**(75 suites, 0 fail, Spring Boot 3.5.3)·`package` SUCCESS(**82,868,029 B**). SEC-007: test `ProductionSecretValidator` **PRESENT**. develop working tree **DIRTY 불변** — untracked 5 entries: ① B02 #5 `PilotChecklistJwtE2eTest`(634 lines/22 @Test, Planned) ② B08 v2 `notification_preferences` WIP(V41 + 7 java + 5 @Test, Planned) ③ `data/backups/` manifest(로컬 산출물). HEAD `@Test` **199**·WT **226**(+27). 이관 규율 5 — `PilotChecklistJwtE2eTest`·notification **HEAD ABSENT**. **Open 0건**·Planned BLOCK **B02 #5 + B08 + frontend B03·B07 #3**. 판정 **BLOCK**.

> **35차 재검증 (2026-06-07T01:50, frontend) — B07 #3 dirty-tree 확대(18→26 files)·WT 144/13 PASS·merge 게이트 BLOCK 유지**:
> - **frontend**: develop HEAD **`3fdc266` 불변**(33·31차), working tree **확대** — 33차 13M+5U=18 → **18M+8U=26 files**(`BatchProgressSteps`·`PlatformOrgDetailModal`·Platform/NHIS/Reconciliation/Forbidden 페이지 WIP 추가). → **B07 recurrence #3 Planned 범위 확대**(신규 Open 0). 이관 규율 5 — HEAD `3fdc266` Fixed(`pilotPageFlows`·`FeeRateHistoryPanel`·`chartColors`·api·AuthContext) **PRESENT**. WT `npm run build` **738 modules PASS**(+2 vs 33차 736)·`npm test` **144/13 PASS**(+2/+1, `BatchProgressSteps.test.jsx`)·`npm audit` **0건**(FE-7). test `@e5fd48d`(frontend-test) `npm run build` **36 modules PASS**·`npm test` **N/A**·audit 0h·2mod(stale, **14 behind**). ROADMAP v1 `merged`·B05 Fixed. 잔여 Planned BLOCK = **B03 + B07 #3**. **Open 0건(frontend)**. 판정 **BLOCK**.
> - **backend**(교차 — 34차 baseline): develop·test `@e8750d2` merged·Maven 213/213·B08 Open·B02 #5 Planned. 판정 **BLOCK**.

> **34차 재검증 (2026-06-07T01:45, backend) — v1 merge 완료·Maven 213/213·SEC-007 해소·notification WIP B08 Open**:
> - **backend**: develop·test HEAD **동일 `@e8750d2`** — v1 develop→test **merge 완료**(33차 test `@2799e29` stale 해소). `mvn test`(test, clean) **213/213 PASS**(75 suites, Spring Boot 3.5.3)·JAR **82,868,029 B**. SEC-007: test `ProductionSecretValidator` **PRESENT**. develop working tree **DIRTY 8 files** — ① `PilotChecklistJwtE2eTest`(634 lines, 22 @Test, B02 #5 Planned) ② **v2 notification WIP**(V41 + 6 java + 4 @Test, **B08 Open 신규**). HEAD `@Test` **199**·WT **225**. **Open 1건(B08 BLOCK)**. 판정 **BLOCK**(dirty-tree).
> - **frontend**(교차 — 33차 baseline): develop `3fdc266` DIRTY 18 files(B07 #3 Planned). Planned BLOCK B03·B07 #3. 판정 **BLOCK**.

> **33차 재검증 (2026-06-07T01:16, frontend 중심) — B07 recurrence #3(Recharts 차트 WIP 18 files)·WT build/test PASS·merge 게이트 BLOCK 유지**:
> - **frontend**: develop HEAD **`3fdc266` 불변**(31차), working tree **DIRTY** — 13 modified + 5 untracked = **18 files**(`recharts ^2.15.4`·`ChartContainer`·`AttendanceRateChart`·`BranchCompareChart`·`HealthTrendChart`·`ChartContainer.test.jsx` + Dashboard·Health·AttendanceStats·FeeSchedule·ClientDetail·chartColors·pilotPageFlows 등) → **QA-B07 recurrence #3 Open**(이관 규율 6·7). 이관 규율 5 — HEAD `3fdc266` Fixed 산출물(`pilotPageFlows`·`FeeRateHistoryPanel`·sevenRoleJwt·api·routeAccess·AuthContext 등) **PRESENT 유효**. WT `npm run build` **736 modules PASS**(+623 vs HEAD 113, recharts 번들)·`npm test` **142/12 PASS**(+2/+1 vs 31차 140/11, FE-7 회귀 없음)·`npm audit` **0건**. test `@e5fd48d`(frontend-test) `npm run build` **36 modules PASS**·`npm test` **N/A**·`npm audit` 0 high·2 moderate(stale, **14 behind**). ROADMAP v1 `merged` → **B05 선행 게이트 해소**. 잔여 Planned BLOCK = **B03 단일**(v1.1 완료 기준 미충족·develop→test merge 미실행). **Open 1건(frontend B07 #3, BLOCK)**. 판정 **BLOCK**.
> - **backend**(교차): test `@e8750d2` = develop HEAD(merge 완료, 32차 stale 해소). develop 1 untracked `PilotChecklistJwtE2eTest` — B02 #5 Open(32차 유지). 판정 **BLOCK**(B02 dirty-tree).

> **32차 재검증 (2026-06-07T01:30, backend 중심) — B02 recurrence #5(PilotChecklistJwtE2eTest 미커밋)·merge ready·merge 미실행·Maven 79/79 PASS·BLOCK 유지**:
> - **backend**: develop HEAD **`e8750d2` 불변**(COD 21차), working tree **DIRTY** — 1 untracked `PilotChecklistJwtE2eTest.java`(634 lines, **22 @Test**, P1–P8 live Bearer JWT E2E WIP) → **QA-B02 recurrence #5 Open**(이관 규율 6 위반). `git cat-file -e HEAD:PilotChecklistJwtE2eTest` **ABSENT** — ROADMAP v1 REQUIREMENTS §6·P1–P8 `[x]` **false [x] 규율 5 위반**. ROADMAP `merge_status: **ready**`(planner 22차)이나 develop→test merge **미실행** — test `@2799e29` stale(8 ahead). develop HEAD `@Test` **199**; WT 합계 **221**(+22). `mvn test`(test, clean) **79/79 PASS**(23 suites)·`mvn -q -DskipTests package` SUCCESS(76,466,058 B) 재현(32차 실측). test SEC-007: `ProductionSecretValidator` **ABSENT**·Boot 3.3.1·`DB_PASSWORD:ogada` 잔존. **Open 1건(B02 #5 BLOCK)**. Planned BLOCK = merge 실행(B01 ready→merged·SEC-007) + frontend B03·B05. 판정 **BLOCK**.
> - **frontend**(교차 — 31차 baseline): develop `3fdc266` CLEAN·140/11 PASS. Planned BLOCK B03·B05. 판정 **BLOCK**.

> **31차 재검증 (2026-06-07T00:43, frontend 중심) — COD `3fdc266` P1–P8 페이지 단위 E2E·UXD 14차 `a42d6fb`·140/11 PASS·merge 게이트 BLOCK 유지**:
> - **frontend**: develop HEAD `57ff3c0`→`a42d6fb`→**`3fdc266`**(+2커밋, **14 ahead**), working tree **CLEAN**. ① **`a42d6fb feat(ux/14차)`**(8 files +335/-8): `BATCH_STATUS` 공유 상수(`Badge.jsx`)·`FeeRateHistoryPanel.jsx`(US-G00a)·`chartColors.js`·Recharts 토큰(`tokens.css`)·`FeeSchedulePage` 이력 모달. ② **`3fdc266 test(v1.1): P1–P8·J01/J02 Must 화면 페이지 단위 E2E 자동화`**(1 file +433: `pilotPageFlows.test.jsx` — AttendancePage·DashboardPage·HealthPage·BillingPage·NHISImportPage·ReconciliationPage·ClientDetailPage·GuardianPage RTL fetch-mock JWT API 호출 검증). 이관 규율 5 — `git cat-file -e HEAD:` `pilotPageFlows.test.jsx`·`FeeRateHistoryPanel.jsx`·`chartColors.js`·기존 Fixed 산출물 **PRESENT**. HEAD `npm run build` **113 modules PASS**(vite 6.4.3, JS 316.47 kB gzip 92.50 kB, CSS 45.71 kB)·`npm test`(vitest 4.1.8) **130/10→140/11 PASS**(+10/+1, FE-7 회귀 없음)·`npm audit` **0건**. test `@e5fd48d`(in `src/frontend-test`) `npm run build` **36 modules PASS**·`npm test` **N/A**·`npm audit` 0 high·2 moderate(stale). **R-05 Must API P1–P8 페이지 단위 E2E PARTIAL 강화** — 라이브 백엔드 연동·J01 백엔드 API 잔여. 잔여 BLOCK = **merge 게이트 단일(B03·B05)**. 판정 **BLOCK**.
> - **backend**(교차 확인 — 30차 baseline): develop HEAD `e8750d2` CLEAN·B02 #4 Fixed·test `2799e29` stale, Maven 79/79 PASS(30차 유효). Planned BLOCK B01·SEC-007. 판정 **BLOCK**.
> - QA_FEEDBACK **Open 0건**. Planned BLOCK **4건**(B01·B03·B05·SEC-007 merge 게이트 단일) 불변.

> **30차 재검증 (2026-06-07T00:28, backend 중심) — COD 21차 `e8750d2` SevenRoleJwtLoginE2eTest 커밋·B02 recurrence #4 Fixed·develop CLEAN·merge 게이트 BLOCK 유지**:
> - **backend**: develop HEAD **`e8750d2`**(COD 21차 신규 — `test(v1): 7역할 JWT 로그인·RBAC live filter-chain E2E (SevenRoleJwtLoginE2eTest)`, **8커밋 ahead**, working tree **CLEAN**). `SevenRoleJwtLoginE2eTest.java` — Spring Security filter chain·`JwtTokenService` live Bearer JWT 7역할 발급/검증·RBAC 허용/거부 E2E — develop HEAD **PRESENT** 확인(`git cat-file -e HEAD:… PRESENT`). `@Test` grep **199**(c3f3146 183→+16: SevenRoleJwtLoginE2eTest 추가). `mvn test`(test `@2799e29`, clean) **79/79 PASS**(23 suites)·`mvn package` SUCCESS(76,466,058 B) 재현(30차 실측). test SEC-007: `ProductionSecretValidator` **ABSENT**·`DB_PASSWORD:ogada` 잔존(merge 미실행). **QA-B02 recurrence #4 정식 Fixed 확정**(TSR 30차 독립 검증 — `git -C src/backend status` clean @ `e8750d2`, SevenRoleJwtLoginE2eTest PRESENT — 이관 규율 5·6 PASS). **develop→test merge 미실행** → `merge_status: pending`(B01) 유지. → **backend Open 0건** — Planned BLOCK **4건**(B01·B03·B05·SEC-007 merge 게이트 단일). 이관 판정 **BLOCK(B01·SEC-007)**.
> - **frontend**(교차 확인 — 29차 baseline): develop HEAD `57ff3c0` CLEAN·`npm test` 130/10·build 112·audit 0건(29차 유효). Planned BLOCK B03·B05. 판정 **BLOCK**.
> - **QA-B02 recurrence #4 Fixed**: 29차·28차 DIRTY(SevenRoleJwtLoginE2eTest.java 384 lines untracked) → 30차 COD 21차 커밋 → **CLEAN 회복**. ROADMAP v1 QA-B02 `[x]` 복원·BE-6 패턴 recurrence #4 **종결**. Planned BLOCK **5건→4건**(B02 #4 Fixed, B01·B03·B05·SEC-007 잔존).
> - **잔여 v1 완료 기준** — `[ ]` 항목: ① `REQUIREMENTS §6 Must·§6-2 P0–P1 체크리스트 충족`(coder 자체 점검 대기), ② `USER_STORIES P1–P8 live E2E`(develop→test merge 후 — 단위 자동화 충족), ③ `SEC-007`(merge 동반). → coder가 ①을 `[x]`로 판단·`merge_status: ready` 설정 후 merge 트리거 가능. **merge ready 게이트 판정: coder 결정 대기**.

> **29차 재검증 (2026-06-06T23:31, frontend 중심) — COD 20차 `57ff3c0` 7역할 JWT 로그인·라우트 가드 E2E 자동화·130/10 PASS·merge 게이트 BLOCK 유지**:
> - **frontend**: develop HEAD `07fd305`→**`57ff3c0`**(+1커밋 COD 20차 신규, **12커밋 ahead**), working tree **CLEAN**. `test(v1.1): 7역할 JWT 로그인·라우트 가드 E2E 자동화` — ① `src/auth/sevenRoleJwtLogin.test.jsx`(132 lines): AuthProvider login() 7역할 JWT 메모리 세션·홈 경로 검증(platform_admin→/platform, hq_admin→/dashboard/hq, branch_admin·social_worker·caregiver→/dashboard, guardian·client_user→/guardian, sysadmin→/settings) + LoginPage JWT 폼 submit 7역할 Vitest 자동화 ② `src/auth/sevenRoleRouteGuard.test.jsx`(83 lines): ProtectedRoute 7역할 허용·거부 매트릭스 E2E ③ `src/auth/sevenRoleRouteMatrix.js`(75 lines): 7역할 라우트 접근 매트릭스 모듈 ④ `roleHomePaths.test.jsx`(+26 lines). 이관 규율 5 — `git cat-file -e HEAD:` `sevenRoleJwtLogin.test.jsx`·`sevenRoleRouteGuard.test.jsx`·`sevenRoleRouteMatrix.js`·`roleHomePaths.test.jsx` + 기존 Fixed 산출물 **PRESENT**. HEAD `npm run build` **112 modules PASS**(vite 6.4.3, JS 314.56 kB gzip 92.06)·`npm test`(vitest 4.1.8) **37/8→130 tests/10 files PASS**(+93/+2, FE-7 회귀 없음)·`npm audit` **0 vulnerabilities**. test `@e5fd48d` build 36 PASS·npm test N/A·audit 0h·2mod(stale). **R-04 7역할 JWT 로그인·라우트 가드 Vitest 자동화 진전** — 라이브 backend E2E는 backend v1 test 승격 후. 잔여 BLOCK = **merge 게이트 단일(B03·B05)**. 판정 **BLOCK**.
> - **backend**(교차 확인 — 28차 baseline): develop HEAD `c3f3146` 불변(COD 18차), working tree **DIRTY** 1 untracked(`SevenRoleJwtLoginE2eTest.java` 384 lines — B02 recurrence #4 Open), Maven 79/79 PASS(28차 실측). 판정 **BLOCK(B01·SEC-007·B02 recurrence #4)**.
> - QA_FEEDBACK **Open 1건(backend B02 recurrence #4, BLOCK)**. Planned BLOCK **4건**(B01·B03·B05·SEC-007 merge 게이트 단일 — 불변).

> **28차 재검증 (2026-06-06T23:19, 양 스트림) — backend B02 recurrence #4(`SevenRoleJwtLoginE2eTest` 미커밋) + frontend UXD 13차 `07fd305` CLEAN·37/8 PASS·merge 게이트 BLOCK 유지**:
> - **backend**: develop HEAD **`c3f3146`**(불변, COD 18차), develop working tree **DIRTY** — 1 untracked `src/test/java/com/ogada/backend/security/SevenRoleJwtLoginE2eTest.java`(384 lines, 7역할 JWT 로그인 E2E 테스트 WIP) → **QA-B02 recurrence #4 Open**(이관 규율 6 위반). 이관 규율 5 — develop HEAD `c3f3146` Fixed 산출물(PilotChecklistApiAccessTest·MustApiEndpointRoutingTest·RoleBasedControllerAccessTest·ProductionSecretValidator·NhisExcelParser·V39·V40) **PRESENT 유효** — HEAD Fixed 영향 없음(untracked만). `mvn -q test`(test `@2799e29`, clean) **79/79 PASS**(23 suites)·`package` SUCCESS(76,466,058 B) 재현(28차 실측). test SEC-007: `ProductionSecretValidator` **ABSENT**·`DB_PASSWORD:ogada` 잔존. **develop→test merge 미실행** → B01·SEC-007 Planned 유지. → **backend Open 1건(B02 recurrence #4, BLOCK)**. 판정 **BLOCK(B01·SEC-007·B02 recurrence #4)**.
> - **frontend**: develop HEAD `cc34f23`→**`07fd305`**(+1커밋 UXD 13차 `feat(ux): 전사 설정 Switch 컴포넌트·셀프 체크인 토글`, **11커밋 ahead**, working tree **CLEAN**). Switch WAI-ARIA 패턴(role=switch·aria-checked·44px·forced-colors)·SettingsPage 토글 컨트롤·`Switch.test.jsx` 5건. develop HEAD `npm run build` **112 modules PASS**(vite 6.4.3, JS 314.56 kB gzip 92.06 kB, CSS 42.67 kB)·`npm test`(vitest 4.1.8) **37 tests/8 files PASS**(27차 32/7 → +5/+1: Switch.test.jsx 5건 추가, FE-7 회귀 없음)·`npm audit` **0건**. test `@e5fd48d` build 36 PASS·npm test N/A·audit 0h·2mod(stale). 이관 규율 5 — HEAD `07fd305` 기존 Fixed 산출물 **PRESENT 유효**. 잔여 BLOCK = **merge 게이트 단일(B03·B05)** — 불변. 판정 **BLOCK(B03·B05)**.
> - QA_FEEDBACK **Open 1건(backend B02 recurrence #4, BLOCK)**. Planned BLOCK **4건**(B01·B03·B05·SEC-007 merge 게이트).

> **27차 재검증 (2026-06-06T22:40, frontend 중심) — COD 19차 `cc34f23` 파일럿 P1–P8·J01/J02 Must API JWT 라우팅 자동화·working tree CLEAN 유지·merge 게이트 BLOCK 유지**:
> - **frontend**: develop HEAD `404a30e`→**`cc34f23`**(+1커밋 COD 19차 신규, **10커밋 ahead**), working tree **CLEAN**. `src/api/pilotChecklist.js`(211)·`pilotChecklist.test.js`(104)·`src/components/ui/GuardianInviteModal.test.jsx`(81) 3 files +396 — USER_STORIES §13 P1–P8 시나리오를 `services.js` 경로에 매핑하고 Vitest fetch mock으로 JWT·HTTP 메서드·경로 검증 + 보호자 초대 UI 회귀 4건. 이관 규율 5 — `git cat-file -e HEAD:` `pilotChecklist.js/.test.js`·`GuardianInviteModal.test.jsx`·api·routeAccess·AuthContext(localStorage 0건)·favicon·dashboardWidgets·`LoginPage.jsx`·`Modal.jsx` **PRESENT**. HEAD `npm run build` **111 modules PASS**(vite 6.4.3, JS 313.68 kB gzip 91.78)·`npm test`(vitest 4.1.8) **13/5 → 32/7 PASS**(+19 tests/+2 files, FE-7 회귀 없음)·`npm audit --audit-level=high` **0건**. test `@e5fd48d` build 36 PASS·npm test N/A·audit 0 high·2 moderate(stale). **R-05 Must API P1–P8·R-07 J01/J02 라우팅 fetch-mock 자동화 진전**(라이브 7역할 JWT E2E·J01 백엔드 초대 API 잔여). 잔여 BLOCK = **merge 게이트 단일(B03·B05)**. 판정 **BLOCK**.
> - **backend**(교차 확인): 26차 baseline 유효 — develop `c3f3146` CLEAN·@Test 183·test `2799e29` stale, Maven 79/79 PASS. 판정 **BLOCK(B01·SEC-007)**.
> - QA_FEEDBACK **Open 0건**. Planned BLOCK **4건**(B01·B03·B05·SEC-007 merge 게이트 단일 — 불변).

> **26차 재검증 (2026-06-06T22:20, 양 스트림) — COD 18차 `c3f3146` PilotChecklistApiAccessTest·UXD 12차 `404a30e` LoginPage DS·접근성·merge 게이트 BLOCK 유지**:
> - **backend**: develop HEAD `aa71412`→**`c3f3146`**(+1커밋 COD 18차 신규, 7커밋 ahead), working tree **CLEAN**. `PilotChecklistApiAccessTest.java`(697 lines, 29 @Test — USER_STORIES §13 P1–P8·REQUIREMENTS §7 7역할 @WebMvcTest @PreAuthorize 29건 자동화, "merge ready 선행") 커밋. develop `@Test` 154→**183**(+29). `mvn -q test`(test `@2799e29`) **79/79 PASS**(23 suites)·package SUCCESS(76,466,058 B) 재현. 이관 규율 5 — `git cat-file -e c3f3146:` `PilotChecklistApiAccessTest`·`MustApiEndpointRoutingTest`·`RoleBasedControllerAccessTest`·`ProductionSecretValidator`·`NhisExcelParser`·V39·V40 **PRESENT**. ROADMAP v1 R-04 **진전**: @WebMvcTest 65건(36 RBAC + 29 Pilot); 7역할 JWT 로그인 live E2E 잔여 → **PARTIAL 유지**. test SEC-007: `ProductionSecretValidator` **ABSENT**. 잔여 BLOCK = **merge 게이트(B01·SEC-007) 단일**. 판정 **BLOCK**.
> - **frontend**: develop HEAD `ed1bf22`→**`404a30e`**(+1커밋 UXD 12차 신규, 9커밋 ahead), working tree **CLEAN**. `LoginPage.jsx`·`Modal.jsx`·`components.css`(3 files +183/-28 — DS Field/TextInput/Button·모노그램 카드·Modal 포커스 트랩·`forced-colors`·`prefers-contrast` WCAG 1.4.11). 이관 규율 5 — `git cat-file -e HEAD:` `LoginPage.jsx`·`Modal.jsx`·`components.css`·api·routeAccess·AuthContext(localStorage 0건)·favicon·dashboardWidgets **PRESENT**. HEAD `npm run build` **111 modules PASS**(vite 6.4.3)·`npm test`(vitest 4.1.8) **13/5 PASS**(FE-7 회귀 없음)·`npm audit --audit-level=high` **0건**. test `@e5fd48d` build 36 PASS·npm test N/A·audit 0 high·2 moderate(stale). 잔여 BLOCK = **merge 게이트 단일(B03·B05)**. 판정 **BLOCK**.
> - QA_FEEDBACK **Open 0건**. Planned BLOCK **4건**(B01·B03·B05·SEC-007 merge 게이트 단일 — dirty-tree·B02·B07·SEC-008 사유 모두 소멸).

> **25차 재검증 (2026-06-06T21:32, frontend 중심) — COD 17차 B07 recurrence #2·SEC-008 Fixed·working tree CLEAN·merge 게이트 단일(B03·B05) 잔존**:
> - **frontend**: develop HEAD `2d742b3`→`a84473f`→**`ed1bf22`**(+2커밋 COD 17차, origin/develop 대비 **8 ahead**), test `e5fd48d` **불변**. ① `a84473f`(US-M02 대시보드 실데이터 위젯, 8 files +636/-170) — 23·24차 미커밋이던 WIP 8 files **일괄 커밋** → develop working tree **DIRTY 8 files → CLEAN**, **QA-B07 recurrence #2 정식 Fixed**. ② `ed1bf22`(SEC-008 — vite `^6.4.3`·vitest `^4.1.8`·`overrides.esbuild ^0.25.0`) → develop **`npm audit` 0 vulnerabilities**(24차 5 vuln/1 critical → 0), **SEC-008 정식 Fixed**. 이관 규율 5 — `git cat-file -e HEAD:` api·routeAccess·AuthContext(localStorage 0건)·favicon·ThemeToggle·tokens.css·**dashboardWidgets.js/.test.js(신규 커밋)** **PRESENT**. develop HEAD(clean) `npm run build` **111 modules PASS**(vite 6.4.3, JS 313.14 kB gzip 91.58)·`npm test`(vitest 4.1.8) **13 tests/5 files PASS**. test `@e5fd48d` build 36 PASS·npm test N/A·audit 0 high·2 moderate(stale). 판정 **BLOCK(B03·B05 merge 게이트 단일 — dirty-tree·SEC-008 사유 소멸)**.
> - **backend**(교차 확인): 24차 baseline 유효 — develop `aa71412` CLEAN·@Test 154·test `2799e29` stale, Maven 79/79 PASS. 판정 **BLOCK(B01·SEC-007)**.
> - QA_FEEDBACK **Open 0건**(B07 recurrence #2·SEC-008 모두 Fixed). Planned BLOCK **4건**(B01·B03·B05·SEC-007 merge 게이트).

> **24차 재검증 (2026-06-06T21:13) — COD 16차·UXD 11차·npm audit 에스컬레이션·양 스트림 BLOCK 유지**:
> - **backend**: develop HEAD `aa71412`→**`aa71412`**(COD 16차 신규: `MustApiEndpointRoutingTest`+459·`RoleBasedControllerAccessTest`+148·`ProductionSecretValidatorTest`+59, 6커밋 ahead), working tree **CLEAN**. `@Test` 120→**154**(+34). `mvn -q test`(test `@2799e29`) **79/79 PASS**(23 suites)·package SUCCESS(76,466,058 B) 재현. 이관 규율 5 — MustApiEndpointRoutingTest·SEC·NHIS·guardian·V39·V40 **PRESENT**. ROADMAP v1 **R-02 Must API 라우팅 [x] 승격**(22차 PARTIAL). test SEC-007 `ProductionSecretValidator` **ABSENT**. 잔여 BLOCK = **merge 게이트(B01·SEC-007)** — 잔여 완료 기준: 7역할 E2E·P1–P8 E2E. 판정 **BLOCK**.
> - **frontend**: develop HEAD `5656e19`→**`2d742b3`**(UXD 11차 dark mode: ThemeToggle·tokens.css·AppShell·theme.js — 7 files +280/-1, 6 ahead). 그러나 develop working tree **DIRTY 8 files 지속**(B07 recurrence #2 Planned — 대시보드 실데이터 WIP 동일). WT `npm run build` **114 modules PASS**(23차 112→+2)·`npm test` **13/5 PASS**(FE-7 회귀 없음). 이관 규율 5 — HEAD `2d742b3` api·routeAccess·AuthContext(localStorage 0건)·favicon·ThemeToggle·tokens.css **PRESENT**. test `e5fd48d` build 36 PASS·npm test N/A(stale). **신규 SEC-008**: npm audit **5 vulnerabilities(4 moderate·1 critical)** — esbuild/vite/vitest dev chain(23차 2 moderate에서 에스컬레이션; prod 번들 무관, devDep 전용). 판정 **BLOCK(B03·B05 merge 게이트 + B07 Planned + SEC-008 MEDIUM Open)**.
> - QA_FEEDBACK Open **1건(SEC-008 MEDIUM)** + Planned BLOCK **5건(B01·B03·B05·B07 recurrence #2·SEC-007)**.

> **23차 재검증 (2026-06-06T20:17, frontend 중심) — B07 recurrence #2·WT build/test PASS·merge 게이트 BLOCK 유지**:
> - **frontend**: develop HEAD `3fc549a`→**`5656e19`**(+1커밋 UXD 10차 `feat(ux): 이용자 본인 계정 발급 필드·CopayTypeSelect·브랜드색`, origin/develop 대비 **5 ahead**), test `e5fd48d` **불변**. develop working tree **CLEAN→DIRTY** — 6 modified(`src/api/services.js`·`GuardianListCard.jsx`·`AttendancePage.jsx`·`ClientFormPage.jsx`·`DashboardPage.jsx`·`GuardiansPage.jsx`) + 2 untracked(`src/pages/dashboardWidgets.js`·`dashboardWidgets.test.js`) = **8 files**(+471/-170, v1.2 P0 **대시보드 실데이터** WIP 미커밋, 이관 규율 6·7 위반) → **QA-B07 recurrence #2 Open**. 이관 규율 5 — `git cat-file -e HEAD:` api·routeAccess·AuthContext(localStorage 0건)·favicon·`package.json` test·`*.test.jsx`×4 **PRESENT**(HEAD Fixed 유효). develop **working tree** `npm run build` **112 modules PASS**(JS 297.15 kB gzip 90.29)·`npm test`(`vitest run`) **13 tests/5 files PASS**(신규 `dashboardWidgets.test.js` 3, FE-7 회귀 없음). test `@e5fd48d` `npm run build` **36 modules PASS**·`npm test` **N/A**·`npm audit` 0 high·2 moderate. 판정 **BLOCK(B03·B05 merge 게이트 + B07 recurrence #2)**.
> - **backend**(교차 확인): 22차 baseline 유효 — develop `4274459` CLEAN·test `2799e29` stale, Open 0. 판정 **BLOCK(B01·SEC-007)**.
> - QA_FEEDBACK Open **1건(frontend B07 recurrence #2, BLOCK)**. Planned BLOCK: B01·SEC-007(backend)·B03·B05(frontend).

> **22차 재검증 (2026-06-06T20:11, backend 중심) — B02 recurrence #3 Fixed·develop CLEAN·merge 게이트 BLOCK 단일**:
> - **backend**: develop HEAD `b5d70a8`→**`4274459`**(+1커밋, COD 15차), develop working tree **DIRTY→CLEAN**, develop `@Test` 98→**120**. 이관 규율 5 — `BillingControllerRoutingTest`·`NhisImportServiceTest`(확장)·`RoleBasedControllerAccessTest`(확장)·SEC·NHIS·guardian·V39·V40 **PRESENT**. `mvn -q test`(test `@2799e29`) **79/79 PASS**(23 suites)·`package` SUCCESS(76,466,058 B) 재현. test SEC-007: `ProductionSecretValidator` **ABSENT**. **QA-B02 recurrence #3 Fixed**. 잔여 BLOCK = **merge 게이트 단일(B01·SEC-007)** — dirty-tree·B02 사유 소멸. 판정 **BLOCK(B01·SEC-007)**.
> - **frontend**(교차): 21차 baseline 유효 — develop `3fc549a` CLEAN, 판정 **BLOCK(B03·B05)**.
> - QA_FEEDBACK Open **0건**. Planned BLOCK: B01·SEC-007(backend)·B03·B05(frontend).

> **21차 재검증 (2026-06-06T19:22, frontend 중심) — B07 recurrence Fixed·working tree CLEAN·merge 게이트 단일 잔존**:
> - **frontend**: develop HEAD `998ac87`→`a72e249`→**`3fc549a`**(+2커밋, origin/develop 대비 **4 ahead**), develop working tree **DIRTY(42 files)→CLEAN**. ① `a72e249 feat(v1.2-p0)`(42 files +3863/-311) — 19·20차 미커밋 v1.2 P0 산출물(`GuardiansPage`·`PaymentPage`·`OverduePage`·`SideNav` 2단·`routeAccess.js`·`SessionTimeoutProvider` 등) **일괄 커밋** → **QA-B07 recurrence 해소**. ② `3fc549a feat(v1.1): ClientDetailPage US-D03`(2 files). 이관 규율 5·6·7 — `git cat-file -e HEAD:` api·routeAccess·AuthContext(localStorage 0건)·favicon **PRESENT**, working tree clean. develop HEAD(clean) `npm test`(`vitest run`) **10 tests/4 files PASS**·`npm run build` **110 modules PASS**(JS 289.39 kB gzip 88.07). test `@e5fd48d` `npm run build` **36 modules PASS**·`npm test` **N/A**(merge 미실행). **QA-B07 Planned→Fixed**. 잔여 BLOCK = **merge 게이트 단일(B03·B05)** — dirty-tree 사유 소멸. ⚠ v1.2 P0가 v1.1 merge 전 선행 커밋 → 범위 결정 필요. 판정 **BLOCK(B03·B05)**.
> - **backend**(교차 확인): 20차 baseline 유효 — develop `b5d70a8`·test `2799e29` 불변, working tree **DIRTY 3 files**(B02 recurrence #3). 판정 **BLOCK(B01·SEC-007·B02 recurrence #3)**.
> - QA_FEEDBACK Open **1건(backend B02 recurrence #3, BLOCK)** — frontend Open 0. Planned BLOCK: B01·SEC-007(backend)·B03·B05(frontend). B07 21차 Fixed.

> **20차 재검증 (2026-06-06T19:12, backend 중심) — B02 recurrence #3·Maven 79/79 재현·merge 게이트 BLOCK 유지**:
> - **backend**: develop HEAD `b5d70a8`·test `2799e29` **불변**(develop 4커밋 앞섬). 18차 CLEAN 대비 develop working tree **재오염 #3** — 2 modified(`NhisImportServiceTest.java` +56, `RoleBasedControllerAccessTest.java` +239/-4) + 1 untracked(`billing/api/BillingControllerRoutingTest.java`, 3 `@Test`) = **3 files** 미커밋(신규 테스트 WIP, 이관 규율 6 위반). 이관 규율 5 — develop HEAD SEC·NHIS·guardian·`RoleBasedControllerAccessTest`·V39·V40 **PRESENT**(`@Test` 98). `mvn test`(test `@2799e29`, clean) **79/79 PASS**(23 suites)·`package` SUCCESS(76,466,058 B) **재현**. test SEC-007: `ProductionSecretValidator` **ABSENT**·`DB_PASSWORD:ogada`·Boot 3.3.1 잔존. **develop→test merge 미실행**(B01). **QA-B02 Open 복귀**(recurrence #3). 판정 **BLOCK — merge 게이트(B01·SEC-007) + B02 recurrence #3**.
> - **frontend**(교차 확인): develop HEAD `998ac87`·test `e5fd48d` 불변. develop working tree **35→42 files**(18 mod + 24 untracked, v1.2 P0 WIP 추가) — B07 recurrence 확대. 판정 **BLOCK(B03·B05·B07)**.
> - QA_FEEDBACK Open **1건(B02 recurrence #3, backend BLOCK)**. Planned BLOCK: B01·SEC-007(backend)·B03·B05·B07(frontend).

> **19차 재검증 (2026-06-06T18:45, frontend 중심) — WT build/test PASS 회복·dirty tree 확대·merge 게이트 BLOCK 유지**:
> - **frontend**: develop HEAD `998ac87`·test `e5fd48d` **불변**. develop working tree **확대** — 14 modified + 21 untracked(**35 files**, 16차 29→35). 이관 규율 5 — HEAD Fixed 산출물 **PRESENT**. develop working tree `npm test` **10 tests/4 files PASS**·`npm run build` **107 modules PASS**(16차 FAIL **회복**). test `@e5fd48d` `npm run build` **36 modules PASS**·`npm test` **N/A**. **B07 Planned** — dirty-tree·규율 6·7 위반 지속(WT 품질 회귀 해소). merge 게이트 B03·B05 불변. 신규 Open **0건**. 판정 **BLOCK(B03·B05·B07)**.
> - **backend**: 18차 baseline 유효 — develop `b5d70a8` CLEAN, 판정 **BLOCK(B01·SEC-007)**.

> **18차 재검증 (2026-06-06T18:42, backend 중심) — 상태 불변·Maven 79/79 재현·merge 게이트 BLOCK 유지**:
> - **backend**: develop HEAD `b5d70a8`·test `2799e29` **불변**, develop working tree **CLEAN**. `mvn -q test`(test `@2799e29`) **79/79 PASS**(23 suites)·`package` SUCCESS(76,466,058 B) **재현**. develop HEAD `@Test` 98·규율 5 PRESENT(SEC·NHIS·guardian·RBAC·V39·V40). test SEC-007: `ProductionSecretValidator` **ABSENT**·`DB_PASSWORD:ogada` 잔존. **develop→test merge 미실행** → `merge_status: pending`(B01) 유지. 신규 Open **0건**. 판정 **BLOCK — merge 게이트 단일(B01·SEC-007 동반)**.
> - **frontend**: 17차 baseline 유효 — develop HEAD `998ac87`·working tree DIRTY(29 files, B07 recurrence Planned, WT build/test FAIL).

> **17차 재검증 (2026-06-06T18:34, backend 중심) — B02 recurrence Fixed·merge 게이트 단일 잔존**:
> - **backend**: develop HEAD `fac3d07`→**`b5d70a8`**(+1커밋, `test(v1): guardian/client_user RBAC WebMvcTest 확장`), develop working tree **DIRTY→CLEAN 복원**. COD 14차 `b5d70a8`로 15차 미커밋 +74 lines 커밋 → **QA-B02 recurrence 정식 Fixed 확정**(TSR 독립 검증: `git -C src/backend status` clean, `git cat-file -e develop:` SEC·NHIS·guardian·`RoleBasedControllerAccessTest`·V39·V40 PRESENT — 이관 규율 5·6 PASS, develop HEAD `@Test` 98). develop 이 test 대비 **4커밋 앞섬**. `mvn -q test`(test `@2799e29`, clean) **79/79 PASS**(23 suites)·`package` SUCCESS(76,466,058 B). test SEC-007: `ProductionSecretValidator` **ABSENT**. **develop→test merge 미실행** → `merge_status: pending`(B01) 유지. 판정 **BLOCK — 잔여 merge 게이트 단일(B01·SEC-007 동반), dirty-tree·B02 recurrence 사유 소멸**.
> - **frontend**: 16차 baseline 유효 — develop HEAD `998ac87`·working tree DIRTY(29 files, B07 recurrence Planned, WT build/test FAIL).
> - QA_FEEDBACK Open **0건**(backend B02 recurrence → Fixed). Planned BLOCK: B01·SEC-007(backend)·B03·B05·B07(frontend).

> **16차 재검증 (2026-06-06T18:07, frontend 중심) — B07 악화·WT build/test FAIL·merge 게이트 BLOCK 유지**:
> - **frontend**: develop HEAD `998ac87`·test `e5fd48d` 불변. develop working tree **악화** — 14 modified + 15 untracked(**29 files**, 14차 19→29). v1.2 P0 WIP 확대(`BillingDetailPage`·`AttendanceAbsentModal`·`GuardianInviteModal`·`ClientPhotoField` 등). 이관 규율 5 — HEAD Fixed 산출물 **PRESENT**. develop working tree `npm test` **FAIL**(6 passed/3 files, `routeAccess.test.jsx` duplicate symbol)·`npm run build` **FAIL**(`routeAccess.js` duplicate `ROUTE_ACCESS`). test `@e5fd48d` `npm run build` **36 modules PASS**·`npm test` **N/A**. **B07 Planned 강화**(WT 품질 회귀). 판정 **BLOCK(B03·B05·B07)**.
> - **backend**: 15차 baseline 유효 — develop `fac3d07` DIRTY(B02 recurrence Open), 판정 **BLOCK(B01·SEC-007·B02)**.
> - QA_FEEDBACK Open **1건(B02 recurrence, backend BLOCK)** — frontend Open 0.

> **15차 재검증 (2026-06-06T18:04, backend 중심) — B02 재발·merge 게이트 BLOCK 유지**:
> - **backend**: develop HEAD `fac3d07` 불변·test `2799e29` 불변. develop working tree **재오염**(1 modified — `RoleBasedControllerAccessTest.java` +74 lines, guardian/client_user RBAC 3 tests 미커밋). 이관 규율 5 — HEAD Fixed 산출물 **PRESENT**. `mvn -q test`(test `@2799e29`) **79/79 PASS**·package SUCCESS. test SEC-007: `ProductionSecretValidator` **ABSENT**. **QA-B02 Open 복귀**. 판정 **BLOCK(B01·SEC-007·B02 recurrence)**.
> - **frontend**: 14차 baseline 유효 — develop HEAD `998ac87`·working tree DIRTY(19 files, B07 recurrence Planned).
> - QA_FEEDBACK Open **1건(B02 recurrence, BLOCK)**.

> **14차 재검증 (2026-06-06T17:35, frontend 중심) — B07 재발·merge 게이트 BLOCK 유지**:
> - **frontend**: develop HEAD `998ac87` 불변·test `e5fd48d` 불변. develop working tree **재오염**(9 mod + 10 untracked = 19 files — v1.2 P0: `GuardiansPage`·`PaymentPage`·`OverduePage`·`GradeHistoryTimeline`·`DashboardWidgetGrid`·`SideNav` 2단·`routeAccess.js`). 이관 규율 5 — HEAD Fixed 산출물 **PRESENT**. develop working tree `npm test` **10/4 PASS**·`npm run build` **96 modules**. test `npm run build` **36 modules PASS**·`npm test` **N/A**. **QA-B07 Open 복귀**. 판정 **BLOCK(B03·B05·B07)**.
> - **backend**: 13차 baseline 유효 — develop `fac3d07` clean, 판정 **BLOCK(B01·SEC-007)**.
> - QA_FEEDBACK Open **1건(B07 recurrence, BLOCK)**.

> **13차 재검증 (2026-06-06T17:30, backend 중심) — develop `fac3d07` 전진·merge 게이트 BLOCK 유지**:
> - **backend**: develop HEAD `4d476c6`→**`fac3d07`**(guardian billing·NHIS guidance·7-role RBAC tests), develop working tree **CLEAN**. develop 이 test 대비 **3커밋 앞섬**. 이관 규율 5 — SEC·NHIS·guardian·`NhisImportGuidance`·`RoleBasedControllerAccessTest` **PRESENT**. `mvn -q test`(test `@2799e29`) **79/79 PASS**. develop HEAD @Test ~94(미실행). ROADMAP R-04·R-11 **부분 진전**. **develop→test merge 미실행** → SEC-007(test P0 미패치) 유지. 판정 **BLOCK(B01·SEC-007)**.
> - **frontend**: 12차(16:55) baseline 유효 — develop `998ac87` clean, 판정 **BLOCK(B03·B05)**.
> - QA_FEEDBACK 신규 Open 0건.

> **12차 재검증 (2026-06-06T16:55, frontend 중심) — COD `998ac87` 독립 검증·dirty-tree·false Fixed 블로커 해소**:
> - **frontend**: develop HEAD `f1c89d9`→**`998ac87`**(신규 커밋 `feat(v1.1): API client layer, memory JWT session, Vitest, favicon`), develop working tree **CLEAN**(9차 22 mod + 20 untracked → 0) — 6~11차 dirty-tree 블로커 **QA-B07·B04 해소**. 이관 규율 5(`git cat-file -e develop:<path>`)·6 — COD 11차 `Fixed` 주장 **전부 develop HEAD PRESENT**: `src/api/http.js`·`services.js`(H04, `ClientListPage`/`ReconciliationPage` 실 fetch), `package.json` `"test":"vitest run"`·`vite.config.js` test·`src/test/setupTests.js`·`*.test.jsx`×3(M01), `AuthContext.jsx` 메모리 세션(SEC-005, localStorage/sessionStorage 부재), `public/favicon.*`·`index.html` 링크(US-UX-01). **develop HEAD `npm test` → 6 tests/3 files PASS**, `npm run build` **87 modules**(test 스켈레톤 36 대비). → **QA-H04·M01·SEC-005·B07·B04 정식 Fixed 확정**(false Fixed 0건), frontend **Open BLOCK 1→0·HIGH 0·MEDIUM 0**. **잔여 블로커는 ① v1.1 `merge_status: pending`(B03 — 7역할 E2E·Must API E2E·보호자 초대 J01 미충족), ② 선행 v1 backend `merged` 미충족(B05) 단일** — develop→test merge 미실행으로 test 브랜치 stale(`e5fd48d`). 판정 **BLOCK(merge 게이트)**.
> - **backend**(교차 확인): 11차(16:40) `4d476c6` clean baseline 유효 — Open BLOCK 0(B06·B02 Fixed), 잔여 `B01`(merge 게이트)·SEC-007(B01 동반). 판정 **BLOCK**.
> - QA_FEEDBACK 신규 Open 0건 — frontend Planned 9차 대비 **B07·B04·H04·M01·SEC-005 Fixed 이동**, 잔여 Planned BLOCK B03·B05(merge 게이트).

> **11차 재검증 (2026-06-06T16:40, backend 중심)**: 8~10차 대비 **backend develop 전진·dirty-tree 블로커 해소**.
> - **backend**: develop HEAD `7d9d2eb`→`4d476c6`(신규 커밋 `feat(v1): primaryGuardian 필수 연결·guardian_link_status(V39)`), develop working tree **CLEAN** — 6회 연속 coder를 막던 **QA-B06·B02(dirty tree) 해소**. develop 이 test 대비 **2커밋 앞섬**(`7d9d2eb`·`4d476c6`, 29 files +1032/-62). 이관 규율 5(`git cat-file -e develop:<path>`) — `AuthRateLimitService`·`ProductionSecretValidator`·`NhisExcelParser`·`PrimaryGuardianLinkRequest`·V35–V40·Spring Boot 3.5.3 **전부 PRESENT**, `createClient` `primaryGuardian` 필수(`@NotNull @Valid`) 계약 develop HEAD 반영(규율 6 PASS). `mvn -q test`(test 브랜치 `2799e29`, clean) **79/79 PASS**(23 suites) 재현. **단 develop→test merge 미실행** → test stale(`2799e29`·Spring Boot 3.3.1·V34·SEC 미패치), `merge_status: pending`(B01) → 판정 **BLOCK(잔여 사유 B01 단일)**.
> - **QA_FEEDBACK 변화**: backend Open BLOCK **1→0**(B06 해소→Fixed, TSR 규율 5 검증). 잔여 backend 블로커는 **B01(Planned)** + SEC-007(Open, B01 보안 영향 관점) — 둘 다 **merge 미실행**이 유일 원인(기능 갭 아님).
> - **frontend**: 11차 미재검(backend 라운드) — 9차(15:45) `f1c89d9` dirty(22 mod + 20 untracked) baseline 유효, 판정 **BLOCK** 유지.

> **9차 재검증 (2026-06-06T15:45, frontend 중심)**: 8차(15:38) 대비 **상태 완전 불변, coder 미조치, 신규 결함 0건**.
> - **frontend**: develop `f1c89d9`·test `e5fd48d` 동일. develop dirty 그대로 22 modified + 20 untracked. `npm run build` **SUCCESS**(36 modules, JS 165.43 kB) 재현, test 브랜치 `npm test` **N/A**(`Missing script: "test"`), `npm audit` 0 high·2 moderate. 규율 5 — `ProtectedRoute.jsx`·`App.jsx` PRESENT(H03·SEC-003 Fixed 유지), `src/api/*`·`src/test/setupTests.js`·`ProtectedRoute.test.jsx`·`package.json` test 스크립트 ABSENT, `AuthContext.jsx` localStorage 잔존(H04·M01·SEC-005 미해소). **신규 관측**: develop **working tree(미커밋)** `vitest run` **6 tests/3 files PASS** — 자동 테스트가 로컬에 완성돼 있으나 develop HEAD 미커밋(M01·B07 강화). 판정 **BLOCK**.
> - **backend**(교차 확인, frontend 라운드): develop `7d9d2eb`(dirty/B06, 6 mod + 2 untracked)·test `2799e29`(clean stale) 동일 — 8차 대비 불변. Maven 미재실행(frontend 라운드), 8차 79/79 PASS 결과 유효. 판정 **BLOCK**.
> - QA_FEEDBACK 신규 Open 0건 — Planned 항목(B01·B03·B04·B05·B06·B07·H04·M01·SEC-005) coder 미조치로 전부 잔존.

> **8차 재검증 (2026-06-06T15:38)**: 14:45/14:55 대비 **회귀·이관 상태 불변, 신규 결함 0건**.
> - **backend**: develop `7d9d2eb`(dirty/QA-B06)·test `2799e29`(clean stale) 동일. `mvn -q test` **79/79 PASS** (23 suites) 재현. 규율 5(`git cat-file -e develop:<path>`) — SEC·NHIS·V35–V38·SB 3.5.3 PRESENT, V39 ABSENT. `merge_status: pending`(B01). 판정 **BLOCK**.
> - **frontend**: develop `f1c89d9`·test `e5fd48d` 동일. develop dirty **확대** 22 mod + **20 untracked**(신규 `AttendanceStatsPage`·`BranchesPage`, QA-B07 악화). H03·SEC-003 PRESENT(Fixed 유지), H04·M01·SEC-005 develop HEAD 미반영 지속. 판정 **BLOCK**.
> - QA_FEEDBACK 신규 Open 0건 — Planned 항목(B01·B03·B04·B05·B06·B07·H04·M01·SEC-005) coder 미조치 상태로 잔존.

---

## 1. 실행 요약 (backend — 2026-06-07T14:00 58차 재검증)

| 항목 | 값 |
|------|-----|
| 실행 일시 | 2026-06-07T14:00:00+00:00 |
| 환경 | OpenJDK 17.0.19, Spring Boot **3.3.1** |
| 검증 worktree | `src/backend-test` (test `@2799e29`, clean) |
| develop HEAD | `f47ffa1` — working tree **CLEAN** (B09 Fixed) |
| ROADMAP merge_status | **`merged`** (문서) — workspace test **미반영** ✗ |
| 명령 | `mvn test` · `mvn -q -DskipTests package` |
| 결과 (test) | **PASS** — **79 tests** / 23 suites, 0 failures |
| develop HEAD `mvn test` | **89/89 PASS** — J01(5 @Test) + notification(4 @Test) |
| develop vs test | **develop 1커밋 ahead** (`f47ffa1`) — merge 미실행 |
| QA_FEEDBACK Open | **2건 BLOCK** — QA-B10 · SEC-D11 |
| v1 baseline artifacts | PilotChecklistJwt·ProductionSecretValidator·MustApi routing **ABSENT** |
| 이관 판정 | **BLOCK** (merge 게이트 + v1 history regression) |

> **56차 대비 변화(58차)**: ① develop HEAD `428ba7d`→**`f47ffa1`** · dirty-tree **27→0 CLEAN** · **B09 Fixed** ② test 여전히 **`2799e29`** (79 tests) — ROADMAP **`e8750d2`** 미달 (**QA-B10 Open**) ③ merge gap **3→1 commit** ④ **SEC-D8 Fixed** @ `f47ffa1`.

## 1-56. 실행 요약 (backend — 2026-06-07T07:58 51차 재검증, 이력)

| 항목 | 값 |
|------|-----|
| 실행 일시 | 2026-06-07T07:58:46+00:00 |
| 환경 | OpenJDK 17.0.19, Spring Boot **3.5.3** |
| 검증 worktree | `src/backend-test` (test `@e8750d2`, clean) |
| develop HEAD | `c3b8716` — working tree **DIRTY** (48차 CLEAN → **2 untracked**) |
| ROADMAP merge_status | **`merged`** ✓ (v1 baseline @e8750d2) |
| 명령 | `mvn test` · `mvn -q -DskipTests package` (in `src/backend-test`) |
| 결과 (test) | **PASS** — **213 tests** / 75 suites, 0 failures |
| develop HEAD `mvn test` (committed) | **249/249 PASS** (91 suites) — HEAD 불변 |
| develop WT `mvn test` | **252/252 PASS** (92 suites, +3 untracked domain tests) |
| develop @Test (HEAD) | grep **238** / surefire **249** (committed) |
| COD Fixed 검증 (규율 5) | B02 #5·B08 @HEAD — **PASS** ✓ (HEAD PRESENT) · working tree — **FAIL** ✗ (B02 #6) |
| develop vs test | **develop 2커밋 ahead** (`feac558`·`c3b8716`) — merge 미실행 |
| QA_FEEDBACK Open | **0건** (B02 #6·B08 #2 **Planned** — 50차 Open→Planned 유지) |
| ROADMAP COD 35 | **false Fixed** — `[x]` 주장 TSR FAIL (HEAD 불변·dirty-tree) |
| 이관 판정 | **BLOCK** (merge 게이트 + dirty-tree — **PASS 금지**) |

> **50차 대비 변화(51차)**: **신규 변화 0건** — develop·test HEAD·dirty-tree·Maven 결과 **완전 동일**. coder 미조치 지속. ROADMAP COD 35 `[x]` **false Fixed** 관측(planner 철회 필요). **테스트 PASS ≠ 이관 PASS**.

> **48차 대비 변화(50차)**: ① develop HEAD **불변**(`c3b8716`), ② working tree **CLEAN→DIRTY**(2 untracked — V42 consent CHECK + `NotificationPreferenceServiceTest` 3 @Test), ③ test **213/213 재현**·develop WT **252/252**(+3), ④ **신규 Open 1건(BLOCK)**, ⑤ HEAD Fixed(B02 #5·B08) **유효 유지** — recurrence는 v2 follow-up 미커밋만. **테스트 PASS ≠ 이관 PASS**.

## 1-48. 실행 요약 (backend — 2026-06-07T15:35 48차 재검증, 이력)

| 항목 | 값 |
|------|-----|
| 실행 일시 | 2026-06-07T06:23:53+00:00 |
| 환경 | OpenJDK 17.0.19, Spring Boot **3.5.3** |
| 검증 worktree | `src/backend-test` (test `@e8750d2`, clean) |
| develop HEAD | `c3b8716` — working tree **CLEAN** (46차 3M+4U → 0) |
| ROADMAP merge_status | **`merged`** ✓ (v1 baseline @e8750d2) |
| 명령 | `mvn test` · `mvn -q -DskipTests package` (in `src/backend-test`) |
| 결과 (test) | **PASS** — **213 tests** / 75 suites, 0 failures |
| develop HEAD `mvn test` (committed, clean) | **249/249 PASS** (91 suites) — WT-only → **HEAD 커밋 전환** |
| develop @Test (HEAD) | grep **235** / surefire **249** (committed) |
| COD Fixed 검증 (규율 5) | B02 #5·B08 — **PASS** ✓ (HEAD PRESENT, working tree CLEAN) |
| develop vs test | **develop 2커밋 ahead** (`feac558`·`c3b8716`) — merge 미실행 |
| 이관 판정 | **BLOCK** (develop→test merge 게이트 단일 — dirty-tree·false Fixed 소멸, Open 0) |

> **46차 대비 변화(48차)**: ① develop HEAD `e8750d2`→**`c3b8716`**(+2커밋 COD 32차), ② dirty-tree **3M+4U → CLEAN**, ③ **B02 #5·B08 정식 Fixed**(이관 규율 5 PASS — HEAD PRESENT), ④ develop **249 committed**(WT-only → HEAD 전환), ⑤ 잔여 BLOCK = **merge 게이트 단일**(dirty-tree·false Fixed 소멸). **backend 30+회 정체 종결**. **테스트 PASS ≠ 이관 PASS**(test에 B02 #5·B08 미반영).

## 1-46. 실행 요약 (backend — 2026-06-07T14:30 46차 재검증, 이력)

| 항목 | 값 |
|------|-----|
| 실행 일시 | 2026-06-07T05:29:10+00:00 |
| 환경 | OpenJDK 17.0.19, Spring Boot **3.5.3** (test = develop HEAD) |
| 검증 worktree | `src/backend-test` (test `@e8750d2`, clean) |
| develop HEAD | `e8750d2` — working tree **DIRTY 확대** (3M + B02 #5 + B08 untracked) |
| ROADMAP merge_status | **`merged`** ✓ |
| 명령 | `mvn test` · `mvn -q -DskipTests package` (in `src/backend-test`) |
| 결과 | **PASS** — **213 tests** / 75 suites, 0 failures |
| develop WT `mvn test` | **249/249 PASS** (91 suites; +6 vs 44차 243/243) |
| develop @Test (HEAD) | **199** committed; WT surefire **249** (+36 vs test) |
| COD Fixed 검증 (규율 5) | B02 #5·B08 — **FAIL** (HEAD ABSENT, WT/modified only) |
| 이관 판정 | **BLOCK** (dirty-tree B02 #5 + B08 Planned — Open 0) |

> **44·45차 대비 변화(46차)**: ① dirty-tree **1M+4U → 3M+4U** — B08 WIP **modified** `MustApiEndpointRoutingTest`(+64)·`RoleBasedControllerAccessTest`(+93), ② develop WT **243→249 PASS**(+6), ③ HEAD `@e8750d2`·test 213/213 **불변**, ④ **COD Fixed FAIL·Open 0** 유지. **테스트 PASS ≠ 이관 PASS**.

## 1-44. 실행 요약 (backend — 2026-06-07T04:59 44차 재검증, 이력)

| 항목 | 값 |
|------|-----|
| 실행 일시 | 2026-06-07T04:58:15+00:00 |
| 환경 | OpenJDK 17.0.19, Spring Boot **3.5.3** (test = develop HEAD) |
| 검증 worktree | `src/backend-test` (test `@e8750d2`, clean) |
| develop HEAD | `e8750d2` — working tree **DIRTY** (1M `.gitignore` + B02 #5 + B08 untracked) |
| ROADMAP merge_status | **`merged`** ✓ |
| 명령 | `mvn test` · `mvn -q -DskipTests package` (in `src/backend-test`) |
| 결과 | **PASS** — **213 tests** / 75 suites, 0 failures |
| develop WT `mvn test` | **243/243 PASS** (88 suites; 42차와 동일) |
| develop @Test (HEAD) | **199** committed; WT **229** (+30 untracked) |
| COD Fixed 검증 (규율 5) | B02 #5·B08 — **FAIL** (HEAD ABSENT, WT only) |
| 이관 판정 | **BLOCK** (dirty-tree B02 #5 + B08 Planned — Open 0) |

> **42·43차 대비 변화(44차)**: **신규 변화 0건** — develop·test HEAD·dirty-tree·Maven 결과 **완전 동일**. coder 미조치 지속. **테스트 PASS ≠ 이관 PASS**.

> **40차 대비 변화(42차)**: ① develop·test HEAD·dirty-tree **구조 불변**, ② develop WT `mvn test` **240→243 PASS**(+3, B08 notification @Test 5→8), ③ **COD Fixed FAIL·Open 0** 유지. **테스트 PASS ≠ 이관 PASS**.

## 1-40. 실행 요약 (backend — 2026-06-07T12:45 40차 재검증, 이력)

## 1-38. 실행 요약 (backend — 2026-06-07T12:05 38차 재검증, 이력)

| 항목 | 값 |
|------|-----|
| 실행 일시 | 2026-06-07T03:04:53+00:00 |
| 환경 | OpenJDK 17.0.19, Spring Boot **3.5.3** (test = develop HEAD) |
| 검증 worktree | `src/backend-test` (test `@e8750d2`, clean) |
| develop HEAD | `e8750d2` — working tree **DIRTY** (B02 #5 + B08 Planned + `data/backups/`) |
| ROADMAP merge_status | **`merged`** ✓ |
| 명령 | `mvn test` · `mvn -q -DskipTests package` (in `src/backend-test`) |
| 결과 | **PASS** — **213 tests** / 75 suites, 0 failures |
| develop @Test (HEAD) | **199** committed; WT **226** (+27 untracked) |
| 이관 판정 | **BLOCK** (dirty-tree B02 #5 + B08 Planned — Open 0) |

> **36·37차 대비 변화(38차)**: **신규 변화 0건** — develop·test HEAD·dirty-tree WIP·Maven 결과 **완전 동일**. coder 미조치 지속.

## 1-36. 실행 요약 (backend — 2026-06-07T11:25 36차 재검증, 이력)

| 항목 | 값 |
|------|-----|
| 실행 일시 | 2026-06-07T02:22:44+00:00 |
| 환경 | OpenJDK 17.0.19, Spring Boot **3.5.3** (test = develop HEAD) |
| 검증 worktree | `src/backend-test` (test `@e8750d2`, clean) |
| develop HEAD | `e8750d2` — working tree **DIRTY** (B02 #5 + B08 Planned + `data/backups/`) |
| ROADMAP merge_status | **`merged`** ✓ |
| 명령 | `mvn test` · `mvn -q -DskipTests package` (in `src/backend-test`) |
| 결과 | **PASS** — **213 tests** / 75 suites, 0 failures |
| develop @Test (HEAD) | **199** committed; WT **226** (+27 untracked) |
| 이관 판정 | **BLOCK** (dirty-tree B02 #5 + B08 Planned — Open 0) |

> **34차 대비 변화(36차)**: **신규 변화 0건** — develop·test HEAD·dirty-tree WIP·Maven 결과 **완전 동일**. `data/backups/` manifest untracked **신규 관측**(로컬 백업 산출물, dirty-tree 동반). coder 미조치 지속.

## 1-34. 실행 요약 (backend — 2026-06-07T01:45 34차 재검증, 이력)

| 항목 | 값 |
|------|-----|
| 실행 일시 | 2026-06-07T01:45:00+00:00 |
| 환경 | OpenJDK 17.0.19, Spring Boot **3.5.3** (test = develop HEAD) |
| 검증 worktree | `src/backend-test` (test `@e8750d2`, clean) |
| develop HEAD | `e8750d2` — working tree **DIRTY** (8 untracked: B02 #5 + B08 notification WIP) |
| ROADMAP merge_status | **`merged`** ✓ |
| 명령 | `mvn test` · `mvn -q -DskipTests package` (in `src/backend-test`) |
| 결과 | **PASS** — **213 tests** / 75 suites, 0 failures |
| develop @Test (HEAD) | **199** committed; WT **225** (+26 untracked) |
| 이관 판정 | **BLOCK** (B08 Planned + B02 #5 Planned dirty-tree) |

> **33차 대비 변화(34차)**: ① test `@2799e29`→**`e8750d2`** v1 merge 완료, ② Maven **79→213** PASS, ③ SEC-007 test **해소**, ④ develop dirty **1→8 files**(notification v2 WIP 신규 B08), ⑤ JAR 76.4MB→**82.9MB**.

## 1-32. 실행 요약 (backend — 2026-06-07T01:30 32차 재검증, 이력)

| 항목 | 값 |
|------|-----|
| 실행 일시 | 2026-06-07T01:30:00+00:00 |
| 환경 | OpenJDK 17.0.19, Spring Boot 3.3.1 (test) / 3.5.3 (develop HEAD) |
| 검증 worktree | `src/backend-test` (test `@2799e29`, clean) |
| develop HEAD | `e8750d2` (COD 21차) — working tree **DIRTY** (1 untracked: PilotChecklistJwtE2eTest.java) |
| ROADMAP merge_status | **ready** (planner 22차) — develop→test merge **미실행** |
| 명령 | `mvn test` · `mvn -q -DskipTests package` (in `src/backend-test`) |
| 결과 | **PASS** — 79 tests / 23 suites, 0 failures |
| develop @Test (HEAD) | **199** (committed); WT **221** (+22 untracked PilotChecklistJwtE2eTest) |
| 이관 판정 | **BLOCK** (B02 recurrence #5 Open + merge 미실행·SEC-007 test 미패치) |

> **30차 대비 변화(32차)**: ① develop HEAD **불변**(`e8750d2`), ② working tree **CLEAN→DIRTY**(1 untracked `PilotChecklistJwtE2eTest.java` 634 lines/22 @Test), ③ ROADMAP `merge_status` **pending→ready**(planner 22차)이나 test **여전히 stale**, ④ **QA-B02 recurrence #5 Open**, ⑤ Maven 79/79 PASS 재현. planner B01/SEC-007 Fixed(ready 게이트) vs TSR: merge·test 승격 **미완료** → 이관 PASS 불가.

## 1-30. 실행 요약 (backend — 2026-06-07T00:28 30차 재검증, 이력)

| 항목 | 값 |
|------|-----|
| 실행 일시 | 2026-06-06T23:19:00+00:00 |
| 환경 | OpenJDK 17.0.19, Spring Boot 3.3.1 (test) / 3.5.3 (develop HEAD) |
| 검증 worktree | `src/backend-test` (test `@2799e29`, clean) |
| develop HEAD | `c3f3146` — working tree **DIRTY** (1 untracked: `SevenRoleJwtLoginE2eTest.java` 384 lines — B02 recurrence #4) |
| 명령 | `mvn -q test` · `mvn -q -DskipTests package` (in `src/backend-test`) |
| 결과 | **PASS** — 79 tests / 23 suites, 0 failures |
| develop @Test (HEAD) | **183** (c3f3146 불변, untracked 미포함) |
| 이관 판정 | **BLOCK** (B02 recurrence #4 Open + merge 게이트 B01·SEC-007) |

## 1-26. 실행 요약 (backend — 2026-06-06T22:20 26차 재검증, 이력)

| 항목 | 값 |
|------|-----|
| 실행 일시 | 2026-06-06T22:20:00+00:00 |
| 환경 | OpenJDK 17.0.19, Spring Boot 3.3.1 (test) / 3.5.3 (develop HEAD) |
| 검증 worktree | `src/backend-test` (test `@2799e29`, clean) |
| develop HEAD | `c3f3146` — working tree **CLEAN** (COD 18차, 7커밋 앞섬) |
| 명령 | `mvn -q test` · `mvn -q -DskipTests package` (in `src/backend-test`) |
| 결과 | **PASS** — 79 tests / 23 suites, 0 failures |
| develop @Test (HEAD) | **183** (`@Test` grep, read-only) — committed (+29 vs 24차) |
| 이관 판정 | **BLOCK** (merge 미실행 B01 + SEC-007 동반 — dirty-tree·B02·R-02 사유 소멸, R-04 @WebMvcTest 65건 진전) |

> **24차 대비 변화(26차)**: ① develop HEAD `aa71412`→**`c3f3146`**(+1커밋 COD 18차), ② develop `@Test` 154→**183**(+29: `PilotChecklistApiAccessTest` P1–P8·7역할 @WebMvcTest @PreAuthorize 29건), ③ R-04 **RBAC @WebMvcTest 65건 진전**(36 RBAC + 29 Pilot), ④ develop 6→7커밋 앞섬, ⑤ Maven 79/79 PASS·package SUCCESS 재현. 잔여 BLOCK = merge 게이트 B01·SEC-007 **단일**.
## 1′. 실행 요약 (backend — 2026-06-06T21:13 24차 재검증, 이력)

| 항목 | 값 |
|------|-----|
| 실행 일시 | 2026-06-06T21:13:00+00:00 |
| 환경 | OpenJDK 17.0.19, Spring Boot 3.3.1 (test) / 3.5.3 (develop HEAD) |
| 검증 worktree | `src/backend-test` (test `@2799e29`, clean) |
| develop HEAD | `aa71412` — working tree **CLEAN** (COD 16차, 6커밋 앞섬) |
| 명령 | `mvn -q test` · `mvn -q -DskipTests package` (in `src/backend-test`) |
| 결과 | **PASS** — 79 tests / 23 suites, 0 failures |
| develop @Test (HEAD) | **154** (`@Test` grep, read-only) — committed (+34 vs 22차) |
| 이관 판정 | **BLOCK** (merge 미실행 B01 + SEC-007 동반 — dirty-tree·B02·R-02 사유 소멸) |

> **22차 대비 변화(24차)**: ① develop HEAD `4274459`→**`aa71412`**(+1커밋 COD 16차), ② develop `@Test` 120→**154**(+34: MustApiEndpointRoutingTest 26+ tests·RoleBasedControllerAccessTest 확장·ProductionSecretValidatorTest), ③ **R-02 Must API 라우팅 PARTIAL→[x]**, ④ develop 5→6커밋 앞섬, ⑤ Maven 79/79 PASS·package SUCCESS 재현. 잔여 BLOCK = merge 게이트 B01·SEC-007 **단일**.

## 1′. 실행 요약 (backend — 2026-06-06T20:11 22차, 이력)

| 항목 | 값 |
|------|-----|
| 실행 일시 | 2026-06-06T20:11:41+00:00 |
| 환경 | OpenJDK 17.0.19, Spring Boot 3.3.1 (test) / 3.5.3 (develop HEAD) |
| 검증 worktree | `src/backend-test` (test `@2799e29`, clean) |
| develop HEAD | `4274459` — working tree **CLEAN** (B02 recurrence #3 Fixed, 5커밋 앞섬) |
| 명령 | `mvn -q test` · `mvn -q -DskipTests package` (in `src/backend-test`) |
| 결과 | **PASS** — 79 tests / 23 suites, 0 failures |
| develop @Test (HEAD) | 120 (`@Test` grep, read-only) — committed |
| 이관 판정 | **BLOCK** (merge 미실행 B01 + SEC-007 동반 — dirty-tree·B02 사유 소멸) |

> **20차 대비 변화**: ① develop HEAD `b5d70a8`→**`4274459`**(+1커밋), ② working tree **DIRTY→CLEAN**, ③ **QA-B02 recurrence #3 Fixed**, ④ develop `@Test` 98→**120**, ⑤ Maven 79/79 PASS·package SUCCESS 재현. 잔여 BLOCK = merge 게이트 B01·SEC-007 **단일**.

---

## 1″. 실행 요약 (backend — 2026-06-06T19:12 20차, 이력)

| 항목 | 값 |
|------|-----|
| 실행 일시 | 2026-06-06T17:28:18+00:00 |
| 환경 | OpenJDK 17.0.19, Spring Boot 3.3.1 (test) / 3.5.3 (develop HEAD) |
| 검증 worktree | `src/backend-test` (test `@2799e29`, clean) |
| develop HEAD | `fac3d07` — working tree **CLEAN** (3커밋 앞섬) |
| 명령 | `mvn -q test` (in `src/backend-test`) |
| 결과 | **PASS** — 79 tests / 23 suites, 0 failures |
| develop @Test 추정 | ~94 (read-only grep, Maven 미실행) |
| 이관 판정 | **BLOCK** (merge 미실행 B01·SEC-007 test P0 미패치) |

> **11차 대비 변화**: develop `fac3d07` +1커밋 — `NhisImportGuidance`·`RoleBasedControllerAccessTest`·guardian billing API. ROADMAP 7역할·롱텀2026 안내 **부분 충족**. merge 게이트 불변.

---

## 1′. 실행 요약 (backend — 2026-06-06T16:40 11차, 이력)

| 항목 | 값 |
|------|-----|
| 실행 일시 | 2026-06-06T16:42:00+00:00 |
| 환경 | OpenJDK 17.0.19, Spring Boot 3.3.1 (test 브랜치) / 3.5.3 (develop HEAD) |
| 검증 worktree | `src/backend-test` (test 브랜치 `2799e29`, working tree clean) |
| develop HEAD | `4d476c6` — working tree **CLEAN** (QA-B06·B02 해소, 2커밋 앞섬) |
| 명령 | `mvn -q test` (in `src/backend-test`) |
| 결과 | **PASS** — 79 tests / 23 suites, 0 failures |
| 이관 판정 | **BLOCK** (테스트 PASS ≠ 이관 PASS — **merge 미실행(B01) 단일 사유**, dirty-tree 사유 소멸) |

> **8~10차 대비 변화**: ① develop HEAD `7d9d2eb`→`4d476c6` — client↔guardian(primaryGuardian 필수·V39·V40) **커밋** → develop working tree **CLEAN**(6회 연속 dirty-tree 블로커 QA-B06·B02 **해소**), ② develop 2커밋 앞섬, ③ develop→test merge **여전히 미실행** — test 브랜치 stale, ④ 잔여 BLOCK 사유는 **B01(merge 게이트) 단일**.

---

## 2. Maven Surefire 상세

### 2-1. test 브랜치 (src/backend-test @ `e8750d2`, clean — 34차)

```
Tests run: 213, Failures: 0, Errors: 0, Skipped: 0   (75 suites)
```

> v1 merge 후 test 브랜치. JAR: `backend-0.0.1-SNAPSHOT.jar` **82,868,029 bytes** (Spring Boot 3.5.3). 32차 stale baseline 79/79 대비 +134 tests.

### 2-1′. test 브랜치 (src/backend-test @ `2799e29`, clean — 32차 이력)

```
Tests run: 79, Failures: 0, Errors: 0, Skipped: 0   (23 suites)
```

> test 브랜치는 develop fix(`7d9d2eb`) 미반영 baseline. JAR: `backend-0.0.1-SNAPSHOT.jar` 76,466,058 bytes (Spring Boot 3.3.1).

### 2-2. develop HEAD (`4d476c6`) — 이관 규율 5 검증

`git cat-file -e develop:<path>` 로 산출물 존재 확인 — **PASS**:
- `auth/domain/AuthRateLimitService.java` (SEC-001), `security/ProductionSecretValidator.java` (SEC-002/006)
- `billing/domain/NhisExcelParser.java` 선행열 skip (QA-H01), Flyway V35–V40, Spring Boot 3.5.3 (SEC-004)
- `clients/api/PrimaryGuardianLinkRequest.java`·V39·`CreateClientRequest.primaryGuardian`(`@NotNull @Valid`)·`ClientServiceTest` (QA-B06/US-D01)
- develop HEAD는 read-only·**working tree clean(11차)** 이나 checkout 금지로 Maven **미실행** — merge 후 test 브랜치 clean tree 재검증 (선행열·rate limit·secret validator·primaryGuardian 추가로 79+α 예상).

### 2-3. 테스트 클래스 (test 브랜치 23 suites)

| 영역 | 클래스 | 비고 |
|------|--------|------|
| 앱 기동 | `OgadaBackendApplicationTests` | Spring context load |
| 인증 | `AuthServiceTest` | `AuthRateLimitServiceTest`·`ProductionSecretValidatorTest`는 develop `7d9d2eb`에만 — test 브랜치 미반영 |
| 이용자 | `ClientServiceTest`, `ClientServiceDischargeTest`, `ClientServiceRevealTest`, `ClientControllerRoutingTest` | |
| 출석 | `AttendanceServiceTest`, `AttendanceControllerRoutingTest`, `GuardianCheckinServiceTest`, `GuardianPortalServiceTest` | |
| 건강 | `HealthRecordServiceTest`, `HealthAlertEvaluatorTest` | |
| 청구 | `BillingServiceTest`, `NhisExcelParserTest`, `NhisImportServiceTest`, `NhisReconciliationMatcherTest` | |
| 대시보드 | `DashboardServiceTest` | |
| 조직 | `PlatformOrganizationServiceTest` | |
| 설정 | `SettingsServiceTest`, `BackupRunServiceTest` | |
| 보안 | `JwtScopeResolverTest`, `ResidentRegistrationMaskerTest` | |
| 공통 | `GlobalExceptionHandlerTest` | |

---

## 3. 패키지 빌드 (test 브랜치)

| 항목 | 값 |
|------|-----|
| 명령 | `mvn -q -DskipTests package` (in `src/backend-test`) |
| 결과 | SUCCESS |
| 산출물 | `target/backend-0.0.1-SNAPSHOT.jar` (76,466,058 bytes, Spring Boot 3.3.1) |

---

## 4. ROADMAP v1 회귀 대조 (검증 기준 = test @ `e8750d2` — 34차)

| ROADMAP 항목 | 자동 테스트 | 수동/E2E | 판정 |
|--------------|-------------|----------|------|
| Maven test 전체 PASS | test **213/213**; develop HEAD **199** @Test | — | **PASS** |
| **API_SPEC Must 엔드포인트** | `MustApiEndpointRoutingTest` §1–§9 | — | **PASS ✓** |
| Flyway V35–V40 | test V40 committed | V41 WT only (B08) | **PASS** |
| **7역할 RBAC + JWT live E2E** | RBAC 36 + Pilot 29 + SevenRole 16+ @Test | — | **PASS [x]** |
| NHIS reconciliation | `NhisImportServiceTest` | UI N/A | PARTIAL |
| NHIS `처리상태` skip (QA-H01) | `NhisExcelParserTest` | — | PASS |
| SEC-001/002/004 (QA-H02) | test PRESENT | — | PASS |
| US-D01 대표 보호자 (QA-B06) | V39·CreateClientRequest | — | PASS |
| **develop working tree clean (QA-B02 #5)** | **CLEAN** (`c3b8716`) | — | **PASS ✓** (48차) |
| REQUIREMENTS §6·P1–P8 live E2E | PilotChecklistJwt **develop HEAD PRESENT** (`c3b8716`) | test 미머지 | **PASS @develop** (test 미반영) |
| **SEC-007 test P0** | test `ProductionSecretValidator` **PRESENT** | — | **PASS ✓** (34차) |
| **merge_status merged (QA-B01)** | v1 merged `@e8750d2`; B02 #5·B08 develop 2커밋 ahead | — | **PARTIAL** (재 merge 필요) |

---

## 5. 미실행·후속 검증

- [x] v1 develop→test merge @e8750d2 (34차)
- [x] test Maven 213/213 PASS + SEC-007 재검증 (34차)
- [x] `PilotChecklistJwtE2eTest.java` develop 커밋 (B02 #5 — `c3b8716`, 48차 PASS)
- [x] notification v2 develop 커밋 (B08 — `feac558`, 48차 PASS)
- [x] develop clean tree Maven 재테스트 (committed **249/249 PASS** @ `c3b8716`, 48차)
- [ ] **develop→test merge 실행** — `c3b8716`(B02 #5)·`feac558`(B08) test 반영 (planner merge 라운드 결정)
- [ ] merge 후 test clean tree Maven 재테스트 (249 예상)
- [ ] NHIS 롱텀 2026 샘플 엑셀 E2E
- [ ] `PATCH /billing/imports/nhis/.../rows/{id}/match` 수동 매칭 API 통합

---

## 6. 참조 산출물

- `transfer/backend/checklists/test.md` — 이관 체크리스트 (판정: **BLOCK** — QA-B10 + merge 1커밋, 58차)
- `transfer/backend/manifests/latest.yaml` — 커밋·Flyway·빌드 메타 (58차)
- `transfer/backend/packages/develop-test-diff-20260608.md` — develop/test diff (58차)
- `docs/qa/QA_FEEDBACK.md` — Open **2 BLOCK** (QA-B10·SEC-D11); B09·SEC-D8 Fixed

---

---

# Frontend stream (v1.1)

> **검증 worktree**: `src/frontend-test` → `test` (read-only)  
> **develop 참고**: `src/frontend` → `develop` (read-only)  
> **ROADMAP**: v1.1 (`merge_status: pending`, 선행 v1 `pending`)

## F-1. 실행 요약 (2026-06-07T08:36:21+00:00 53차 재검증)

| 항목 | 값 |
|------|-----|
| 실행 일시 | 2026-06-07T08:36:21+00:00 |
| 환경 | Node v18.17.0, Vite 6.4.3, React 18.3.1, Vitest 4.1.8 (develop HEAD) / Vite 5.4.21 (test stale) |
| 검증 worktree | `src/frontend-test` (test `@e5fd48d`, working tree **clean**, **18 behind**) |
| develop HEAD | `d5654c0` — working tree **CLEAN** (COD 35차 FE-17 J01 수락 UI·LogoutButton·레이아웃 회귀, 25 files +823/-57) |
| 명령 | `npm run build`·`npm test`·`npm audit` (test + develop HEAD) |
| build 결과 | test **PASS** (36 modules, Vite 5.4.21) / develop HEAD **PASS** (**756 modules**, 3 청크: react-vendor 166.34·index 186.68·recharts 393.53 kB, CSS 52.52 kB) |
| 단위 테스트 | test **N/A** / develop HEAD **`npm test` 199 tests/40 files PASS** (+5/+2 vs 52차 WT 194/38, FE-7 회귀 없음) |
| npm audit | test 0 high·2 moderate(stale) / develop HEAD **0 vulnerabilities** ✓ |
| FE-15 코드 스플릿 | **Fixed @ HEAD** — 최대 청크 393.53 kB(<500 kB) |
| B07 recurrence #5 | **Fixed** — COD 35차 `d5654c0` 25 files 커밋·CLEAN·이관 규율 5·6·7·8 PASS |
| 이관 판정 | **BLOCK** (B03 merge 게이트 단일 — B07 #5 소멸) |

> **52차(08:03) 대비 변화**: ① develop HEAD **`0b9b001`→`d5654c0`**(+1커밋 COD 35차 FE-17, 25 files +823/-57, 18 ahead), ② working tree **DIRTY 20 files→CLEAN**(0 — B07 #5 Fixed), ③ develop HEAD `npm test` **194/38→199/40 PASS**(+5/+2: FE-17 신규 `LogoutButton.test`·`BillingPage.layout.test`·`GuardianInvitationAcceptPage.test` 등 커밋 반영), ④ develop HEAD build **754→756 modules**(+2), ⑤ test `@e5fd48d` 불변(stale, 18 behind). 이관 규율 5 — **HEAD d5654c0 Fixed 전부 PRESENT**(`LogoutButton.jsx`·`GuardianInvitationAcceptPage.jsx`·`GuardianInvitationAcceptForm.jsx`·`PublicAuthLayout.jsx`·`BillingPage.layout.test.jsx`·`services.js`(acceptGuardianInvitationApi) PRESENT). SEC-005 AuthContext localStorage/sessionStorage **0건**. **Open 0건** — B07 #5 소멸. 판정 **BLOCK**(B03 단일).

## F-1-52. 실행 요약 (2026-06-07T08:03:37+00:00 52차 재검증, 이력)

| 항목 | 값 |
|------|-----|
| 실행 일시 | 2026-06-07T08:03:37+00:00 |
| 환경 | Node v18.17.0, Vite 6.4.3, React 18.3.1, Vitest 4.1.8 (develop WT) / Vite 5.4.21 (test stale) |
| 검증 worktree | `src/frontend-test` (test `@e5fd48d`, working tree **clean**, **17 behind**) |
| develop HEAD | `0b9b001` — working tree **DIRTY 20 files** (15M+5U — B07 recurrence #5) |
| 명령 | `npm run build`·`npm test`·`npm audit` (test + develop WT read-only) |
| build 결과 | test **PASS** (36 modules, Vite 5.4.21) / develop WT **PASS** (**754 modules**, 3 청크: react-vendor 166.34·index 185.35·recharts 393.53 kB, CSS 52.24 kB) |
| 단위 테스트 | test **N/A** / develop WT **`npm test` 194 tests/38 files PASS** (+7/+3 vs 50차 187/35) |
| npm audit | test 0 high·2 moderate(stale) / develop WT **0 vulnerabilities** ✓ |
| FE-15 코드 스플릿 | **Fixed @ HEAD** — 최대 청크 393.53 kB(<500 kB) |
| 이관 판정 | **BLOCK** (B03 merge 게이트 + **B07 recurrence #5 dirty-tree**) |

> **50차(07:17) 대비 변화**: ① develop HEAD **불변**(`0b9b001`), ② working tree **CLEAN→DIRTY**(0→**20 files** — B07 recurrence #5), ③ develop WT `npm test` **187/35→194/38 PASS**(+7/+3: `LogoutButton.test`·`BillingPage.layout.test`·`GuardianInvitationAcceptPage.test` 등), ④ develop WT build **752→754 modules**(+2), ⑤ test `@e5fd48d` 불변(stale, 17 behind). 이관 규율 5 — HEAD Fixed **PRESENT 유지**·WT-only WIP **HEAD ABSENT**. **신규 Open 1건(BLOCK)**: B07 #5. **테스트 PASS ≠ 이관 PASS**.

## F-1-50. 실행 요약 (2026-06-07T07:17:37+00:00 50차 재검증, 이력)

| 항목 | 값 |
|------|-----|
| 실행 일시 | 2026-06-07T07:17:37+00:00 |
| 환경 | Node v18.17.0, Vite 6.4.3, React 18.3.1, Vitest 4.1.8 (develop) / Vite 5.4.21 (test stale) |
| 검증 worktree | `src/frontend-test` (test `@e5fd48d`, working tree **clean**, **17 behind**) |
| develop HEAD | `0b9b001` — working tree **CLEAN** (COD 34차 ds-* 유틸리티 전환·AttendancePage 레이아웃 회귀 테스트) |
| 명령 | `npm run build`·`npm test`·`npm audit` (test + develop HEAD) |
| build 결과 | test **PASS** (36 modules, Vite 5.4.21) / develop HEAD **PASS** (**752 modules**, 3 청크: react-vendor 166.34·index 181.88·recharts 393.53 kB, CSS 52.95 kB) |
| 단위 테스트 | test **N/A** / develop HEAD **`npm test` 187 tests/35 files PASS** (+1/+1 `AttendancePage.layout.test.jsx` vs 49차) |
| npm audit | test 0 high·2 moderate(stale) / develop HEAD **0 vulnerabilities** ✓ |
| FE-15 코드 스플릿 | **Fixed** (49차) — 최대 청크 393.53 kB(<500 kB), vite 경고 해소 |
| 이관 판정 | **BLOCK** (B03 merge 게이트 단일 — B07 #3·#4·FE-15 사유 소멸) |

> **49차(15:45) 대비 변화**: ① develop HEAD `c98f98d`→**`0b9b001`**(+1커밋 COD 34차 — `fix(v1.1): Must 페이지 UXD ds-* 유틸리티 전환·AttendancePage 레이아웃 회귀 테스트`), ② working tree **CLEAN 유지**(0 dirty), ③ HEAD `npm test` **186/34→187/35 PASS**(+1/+1 `AttendancePage.layout.test.jsx`), ④ HEAD build **752 modules 유지**·CSS 52.95 kB·audit 0건, ⑤ develop 16→**17 commits ahead**·test `@e5fd48d` 불변(stale, 17 behind). 이관 규율 5 — HEAD `0b9b001` 기존 Fixed + 신규 산출물 PRESENT. **신규 Open 0건** — B03 merge 게이트 단일.

## F-1-49. 실행 요약 (2026-06-07T15:45 49차 재검증, 이력)

| 항목 | 값 |
|------|-----|
| 실행 일시 | 2026-06-07T06:36:45+00:00 |
| 환경 | Node v18.17.0, Vite 6.4.3, React 18.3.1, Vitest 4.1.8 (develop) / Vite 5.4.21 (test stale) |
| 검증 worktree | `src/frontend-test` (test `@e5fd48d`, working tree **clean**, **16 behind**) |
| develop HEAD | `c98f98d` — working tree **CLEAN** (47차 0 + 48차 교차 5 files → `c98f98d` 커밋, B07 #4 신호 소멸) |
| 명령 | `npm run build`·`npm test`·`npm audit` (test + develop HEAD read-only) |
| build 결과 | test **PASS** (36 modules) / develop HEAD **PASS** (**752 modules**, FE-15 **3 청크 분리**: react-vendor 166.34·index 182.52·recharts 393.53 kB) |
| 단위 테스트 | test **N/A** / develop HEAD **`npm test` 186 tests/34 files PASS** (+1/+1 layout 회귀 vs 47차) |
| npm audit | test 0 high·2 moderate(stale) / develop HEAD **0 vulnerabilities** ✓ |
| FE-15 코드 스플릿 | **Fixed** — 단일 744.95 kB → 최대 청크 393.53 kB(<500 kB), vite 경고 해소 |
| 이관 판정 | **BLOCK** (B03 merge 게이트 단일 — B07 #4 신호·FE-15 LOW 사유 소멸) |

> **47차(14:45) 대비 변화**: ① develop HEAD `4be0938`→**`c98f98d`**(+1커밋 COD 33차), ② TSR 48차 backend 교차 관측 재오염 5 files(B07 #4 신호)가 `c98f98d`로 일괄 커밋 → working tree **CLEAN 유지**(신호 소멸·정식 Open 미등록), ③ **FE-15 코드 스플릿 Fixed**(`manualChunks` — 단일 744.95 kB → 3 청크), ④ HEAD `npm test` **185/33→186/34 PASS**(+1/+1 `ClientDetailPage.layout.test.jsx`), ⑤ HEAD build **752 modules 유지**·audit 0건, ⑥ develop 15→**16 commits ahead**·test `@e5fd48d` 불변(stale, 16 behind). 이관 규율 5 — HEAD `c98f98d` 기존 Fixed + 신규 산출물 PRESENT.

## F-1-45. 실행 요약 (2026-06-07T14:02 45차 재검증, 이력)

| 항목 | 값 |
|------|-----|
| 실행 일시 | 2026-06-07T05:02:14+00:00 |
| develop HEAD | `3fdc266` — working tree **DIRTY** (76 files, B07 recurrence #3) |
| build / test | WT **749 modules**·**181/30 PASS**·audit 0 |
| 이관 판정 | **BLOCK** (B07 recurrence #3 + B03 merge 게이트) |

## F-1-43. 실행 요약 (2026-06-07T13:27 43차 재검증, 이력)

| 항목 | 값 |
|------|-----|
| 실행 일시 | 2026-06-07T04:27:22+00:00 |
| develop HEAD | `3fdc266` — working tree **DIRTY** (38M+34U=**72 files**) |
| build / test | WT **748 modules**·**179/29 PASS**·audit 0 |
| 이관 판정 | **BLOCK** (B07 #3 + B03) |

> **41차(12:52) 대비 변화**: ① develop HEAD **불변**(`3fdc266`), ② working tree **61→72 files 확대**(신규 `BillingStatusConfirmModal`·`CopayRateTable`·`GuardianDailySummary`·`HealthAlertList`·`NhisImportGuidePanel` +tests), ③ WT build **743→748 modules**·WT `npm test` **169/24→179/29 PASS**, ④ B07 #3 **Planned 범위 확대**(신규 Open 0), ⑤ test `@e5fd48d` 불변(stale, 14 behind). HEAD Fixed @ `3fdc266` 규율 5 **유효**.

## F-1-41. 실행 요약 (2026-06-07T12:52 41차 재검증, 이력)

| 항목 | 값 |
|------|-----|
| 실행 일시 | 2026-06-07T03:09:08+00:00 |
| 환경 | Node v18.17.0, Vite 6.4.3, React 18.3.1, Vitest 4.1.8 (develop WT) / Vite 5.4.21 (test stale) |
| 검증 worktree | `src/frontend-test` (test `@e5fd48d`, working tree **clean**) |
| develop HEAD | `3fdc266` — working tree **DIRTY** (36M+24U=**60 files**, B07 recurrence #3 **범위 확대**) |
| 명령 | `npm run build`·`npm test`·`npm audit` (test + develop WT read-only) |
| build 결과 | test **PASS** (36 modules) / develop WT **PASS** (**743 modules**, recharts+설정·보안 패널 번들) |
| 단위 테스트 | test **N/A** / develop WT **`npm test` 169 tests/24 files PASS** (+8/+4 vs 37차) |
| npm audit | test 0 high·2 moderate(stale) / develop WT **0 vulnerabilities** ✓ |
| 이관 판정 | **BLOCK** (B07 recurrence #3 + B03 merge 게이트) |

> **37차(11:30) 대비 변화**: ① develop HEAD **불변**(`3fdc266`), ② working tree **44→60 files 확대**(신규 `LoginHistoryPanel`·`PasswordChangeModal`·`PasswordResetRequestModal`·`PlatformOrgDetailModal`(+tests)·`SettingsPage.test.jsx` + 10 modified), ③ WT build **741→743 modules**·WT `npm test` **161/20→169/24 PASS**, ④ B07 #3 **Planned 범위 확대**(신규 Open 0), ⑤ test `@e5fd48d` 불변(stale, 14 behind). HEAD Fixed @ `3fdc266` 규율 5 **유효**.

## F-1-37. 실행 요약 (2026-06-07T11:30 37차 재검증, 이력)

| 항목 | 값 |
|------|-----|
| 실행 일시 | 2026-06-07T02:27:54+00:00 |
| develop HEAD | `3fdc266` — working tree **DIRTY** (26M+18U=44 files) |
| build / test | WT **741 modules**·**161/20 PASS**·audit 0 |
| 이관 판정 | **BLOCK** (B07 #3 + B03) |

## F-1-35. 실행 요약 (2026-06-07T01:50 35차 재검증, 이력)

| 항목 | 값 |
|------|-----|
| 실행 일시 | 2026-06-07T01:50:00+00:00 |
| develop HEAD | `3fdc266` — working tree **DIRTY** (18M+8U=26 files) |
| build / test | WT **738 modules**·**144/13 PASS**·audit 0 |
| 이관 판정 | **BLOCK** (B07 #3 + B03) |

## F-1-33. 실행 요약 (2026-06-07T01:16 33차 재검증, 이력)

| 항목 | 값 |
|------|-----|
| 실행 일시 | 2026-06-07T01:16:00+00:00 |
| 환경 | Node v18.17.0, Vite 6.4.3, React 18.3.1, Vitest 4.1.8 (develop WT) / Vite 5.4.21 (test stale) |
| 검증 worktree | `src/frontend-test` (test `@e5fd48d`, working tree **clean**) |
| develop HEAD | `3fdc266` — working tree **DIRTY** (13M+5U=18 files, B07 recurrence #3) |
| 명령 | `npm run build`·`npm test`·`npm audit` (test + develop WT read-only) |
| build 결과 | test **PASS** (36 modules) / develop WT **PASS** (**736 modules**, recharts 번들) |
| 단위 테스트 | test **N/A** / develop WT **`npm test` 142 tests/12 files PASS** (+2/+1 vs 31차) |
| npm audit | test 0 high·2 moderate(stale) / develop WT **0 vulnerabilities** ✓ |
| 이관 판정 | **BLOCK** (B07 recurrence #3 + B03 merge 게이트) |

> **31차(00:43) 대비 변화**: ① develop HEAD **불변**(`3fdc266`), ② working tree **CLEAN→DIRTY 18 files**(Recharts 차트·대시보드·건강·출석 WIP), ③ WT build **113→736 modules**·WT `npm test` **140/11→142/12 PASS**, ④ **QA-B07 recurrence #3 Open**, ⑤ ROADMAP v1 `merged` → **B05 선행 해소**, ⑥ test `@e5fd48d` 불변(stale, 14 behind). HEAD Fixed @ `3fdc266` 규율 5 **유효**.

## F-1-31. 실행 요약 (2026-06-07T00:43 31차 재검증, 이력)

| 항목 | 값 |
|------|-----|
| 실행 일시 | 2026-06-07T00:43:00+00:00 |
| 환경 | Node/npm, Vite 6.4.3, React 18.3.1, Vitest 4.1.8 (develop) / Vite 5.4.21 (test stale) |
| 검증 worktree | `src/frontend-test` (test `@e5fd48d`, working tree **clean**) |
| develop HEAD | `3fdc266` (COD page E2E + UXD 14차) — working tree **CLEAN** (14 ahead) |
| 명령 | `npm run build`·`npm test`·`npm audit` (test 브랜치) + develop HEAD read-only 검증 |
| build 결과 | test **PASS** (36 modules, JS 165.43 kB) / develop HEAD **PASS** (**113 modules**, JS 316.47 kB, vite 6.4.3) |
| 단위 테스트 | test **N/A** / develop HEAD **`npm test` 140 tests/11 files PASS** (vitest 4.1.8, 29차 130/10 → +10/+1) |
| npm audit | test 0 high·2 moderate(stale) / develop HEAD **0 vulnerabilities** ✓ |
| 이관 판정 | **BLOCK** (B03·B05 merge 게이트 단일 — 불변) |

> **29차(23:31) 대비 변화**: ① develop HEAD `57ff3c0`→`a42d6fb`→**`3fdc266`**(+2커밋), ② working tree **CLEAN 유지**, ③ `pilotPageFlows.test.jsx`(433 lines — P1–P8 Must 화면 페이지 단위 RTL E2E)·UXD 14차 `FeeRateHistoryPanel`·`chartColors.js`·`BATCH_STATUS` 추가, ④ HEAD build **112→113 modules**·HEAD `npm test` **130/10→140/11 PASS**(+10/+1, FE-7 회귀 없음)·audit 0건, ⑤ develop 12→**14 commits ahead**. 이관 규율 5 — HEAD `3fdc266` 기존 Fixed + 신규 산출물 PRESENT. **R-05 P1–P8 페이지 단위 E2E PARTIAL 강화** — 라이브 백엔드·J01 API 잔여. test `e5fd48d` 불변(stale). 잔여 BLOCK = **merge 게이트(B03·B05) 단일**.

## F-1-29. 실행 요약 (2026-06-06T23:31 29차 재검증, 이력)

| 항목 | 값 |
|------|-----|
| 실행 일시 | 2026-06-06T23:31:00+00:00 |
| 환경 | Node/npm, Vite 6.4.3, React 18.3.1, Vitest 4.1.8 (develop) / Vite 5.4.21 (test stale) |
| 검증 worktree | `src/frontend-test` (test `@e5fd48d`, working tree **clean**) |
| develop HEAD | `57ff3c0` (COD 20차) — working tree **CLEAN** (12 ahead) |
| 명령 | `npm run build`·`npm test`·`npm audit` (test 브랜치) + develop HEAD read-only 검증 |
| build 결과 | test **PASS** (36 modules, JS 165.43 kB) / develop HEAD **PASS** (**112 modules**, JS 314.56 kB, vite 6.4.3) |
| 단위 테스트 | test **N/A** / develop HEAD **`npm test` 130 tests/10 files PASS** (vitest 4.1.8, 28차 37/8 → +93/+2) |
| npm audit | test 0 high·2 moderate(stale) / develop HEAD **0 vulnerabilities** ✓ |
| 이관 판정 | **BLOCK** (B03·B05 merge 게이트 단일 — 불변) |

> **28차(23:19) 대비 변화**: ① develop HEAD `07fd305`→**`57ff3c0`**(+1커밋 COD 20차), ② working tree **CLEAN 유지**, ③ `sevenRoleJwtLogin.test.jsx`(132: AuthProvider login 7역할 JWT 세션·홈 경로 + LoginPage 폼 submit)·`sevenRoleRouteGuard.test.jsx`(83: ProtectedRoute 7역할 허용·거부 매트릭스)·`sevenRoleRouteMatrix.js`(75: 라우트 접근 매트릭스) 추가, ④ HEAD build **112 modules 동일**·HEAD `npm test` **37/8→130/10 PASS**(+93 tests/+2 files, FE-7 회귀 없음)·audit 0건, ⑤ 이관 규율 5 — HEAD `57ff3c0` 기존 Fixed 산출물 + 신규 7역할 JWT E2E 파일 PRESENT 유효. **R-04 7역할 로그인·라우트 가드 Vitest 자동화 진전(+93/+2)** — 라이브 backend E2E는 backend v1 test 승격 후. test `e5fd48d` 불변(stale, 12 behind). 잔여 BLOCK = **merge 게이트(B03·B05) 단일**.

## F-1-28. 실행 요약 (2026-06-06T23:19 28차 재검증, 이력)



| 항목 | 값 |
|------|-----|
| 실행 일시 | 2026-06-06T22:40:00+00:00 |
| 환경 | Node/npm, Vite 6.4.3, React 18.3.1, Vitest 4.1.8 (develop) / Vite 5.4.21 (test stale) |
| 검증 worktree | `src/frontend-test` (test `@e5fd48d`, working tree **clean**) |
| develop HEAD | `cc34f23` (COD 19차) — working tree **CLEAN** (10 ahead) |
| 명령 | `npm run build`·`npm test`·`npm audit` (test 브랜치) + develop HEAD read-only 검증 |
| build 결과 | test **PASS** (36 modules, JS 165.43 kB) / develop HEAD **PASS** (**111 modules**, JS 313.68 kB, vite 6.4.3) |
| 단위 테스트 | test **N/A** / develop HEAD **`npm test` 32 tests/7 files PASS** (vitest 4.1.8, 26차 13/5 → +19/+2) |
| npm audit | test 0 high·2 moderate(stale) / develop HEAD **0 vulnerabilities** ✓ |
| 이관 판정 | **BLOCK** (B03·B05 merge 게이트 단일 — dirty-tree·SEC-008 사유 소멸) |

> **26차(22:20) 대비 변화**: ① develop HEAD `404a30e`→**`cc34f23`**(+1커밋 COD 19차), ② working tree **CLEAN 유지**, ③ `pilotChecklist.js`(211: USER_STORIES §13 P1–P8 → `services.js` 경로 매핑)·`pilotChecklist.test.js`(104: Vitest fetch mock JWT·메서드·경로)·`GuardianInviteModal.test.jsx`(81: 보호자 초대 UI 회귀 4건) 3 files +396, ④ HEAD `npm test` 13/5 → **32/7 PASS**(+19 tests/+2 files)·build 111·audit 0건 **회귀 없음**, ⑤ 이관 규율 5 — `pilotChecklist.js/.test.js`·`GuardianInviteModal.test.jsx` + 기존 Fixed 산출물 전부 PRESENT. **R-05 Must API P1–P8·R-07 J01/J02 라우팅 fetch-mock 자동화 진전**(라이브 E2E·J01 백엔드 API 잔여). test `e5fd48d` 불변(stale, 10 behind). 잔여 BLOCK = **merge 게이트(B03·B05) 단일**.

## F-1′. 실행 요약 (2026-06-06T21:32 25차 재검증, 이력)

| 항목 | 값 |
|------|-----|
| 실행 일시 | 2026-06-06T21:32:00+00:00 |
| 환경 | Node/npm, Vite 6.4.3, React 18.3.1, Vitest 4.1.8 (develop) / Vite 5.4.21 (test stale) |
| 검증 worktree | `src/frontend-test` (test `@e5fd48d`, working tree **clean**) |
| develop HEAD | `ed1bf22` (COD 17차 SEC-008) — working tree **CLEAN** (24차 8 files → 0, 8 ahead) |
| 명령 | `npm run build`·`npm test`·`npm audit` (test 브랜치) + develop HEAD read-only 검증 |
| build 결과 | test **PASS** (36 modules, JS 165.43 kB) / develop HEAD **PASS** (**111 modules**, JS 313.14 kB, vite 6.4.3) |
| 단위 테스트 | test **N/A** / develop HEAD **`npm test` 13 tests/5 files PASS** (vitest 4.1.8) |
| npm audit | test 0 high·2 moderate(stale) / develop HEAD **0 vulnerabilities** ✓ (SEC-008 Fixed) |
| 이관 판정 | **BLOCK** (B03·B05 merge 게이트 단일 — dirty-tree·SEC-008 사유 소멸) |

> **24차(21:13) 대비 변화**: ① develop HEAD `2d742b3`→`a84473f`→**`ed1bf22`**(+2커밋 COD 17차), ② working tree **DIRTY 8 files → CLEAN**(`a84473f` 대시보드 실데이터 일괄 커밋 — **QA-B07 recurrence #2 Fixed**), ③ **SEC-008 Fixed**(`ed1bf22` vite 6.4.3·vitest 4.1.8·esbuild override → npm audit `5 vuln(1 critical)` → **0**), ④ HEAD build 114(WT)→**111**(vite 6 트랜스폼)·`npm test` 13/5 PASS 유지, ⑤ 이관 규율 5 — HEAD `ed1bf22` Fixed 산출물 + `dashboardWidgets.js/.test.js` 신규 커밋 PRESENT. test `e5fd48d` 불변(stale, 8 behind). 잔여 BLOCK = **merge 게이트(B03·B05) 단일**.

## F-1‹. 실행 요약 (2026-06-06T21:13 24차, 이력)

| 항목 | 값 |
|------|-----|
| 실행 일시 | 2026-06-06T21:13:00+00:00 |
| develop HEAD | `2d742b3` (UXD 11차 dark mode) — working tree **DIRTY** (8 files, B07 recurrence #2, 6 ahead) |
| build 결과 | test **PASS** (36 modules) / develop WT **PASS** (114 modules) |
| 단위 테스트 | test **N/A** / develop WT **13/5 PASS** |
| npm audit | develop WT **5 vulnerabilities (1 critical)** ⚠ ESCALATION (SEC-008) |
| 이관 판정 | **BLOCK** (B03·B05 + B07 recurrence #2 Planned + SEC-008 MEDIUM) |

## F-1′. 실행 요약 (2026-06-06T20:17 23차, 이력)

| 항목 | 값 |
|------|-----|
| 실행 일시 | 2026-06-06T20:16:30+00:00 |
| 환경 | Node/npm, Vite 5.4.21, React 18.3.1, Vitest 2.1.9 |
| 검증 worktree | `src/frontend-test` (test `@e5fd48d`, working tree **clean**) |
| develop HEAD | `5656e19` (UXD 10차) — working tree **DIRTY** (6 modified + 2 untracked = **8 files**, v1.2 P0 대시보드 실데이터 WIP, 5 ahead) |
| 명령 | `npm run build`·`npm test`·`npm audit` (test 브랜치) + develop working tree read-only 검증 |
| build 결과 | test **PASS** (36 modules, JS 165.43 kB) / develop working tree **PASS** (112 modules, JS 297.15 kB) |
| 단위 테스트 | test **N/A** / develop working tree **`npm test` 13 tests/5 files PASS** (+`dashboardWidgets.test.js` 3) |
| 이관 판정 | **BLOCK** (B03·B05 merge 게이트 + **B07 recurrence #2** dirty-tree) |

> **21차(19:22) 대비 변화**: ① develop HEAD `3fc549a`→**`5656e19`**(+1커밋 UXD 10차 — `ClientUserAccountField`·`CopayTypeSelect`·브랜드색·favicon), ② working tree **CLEAN→DIRTY 8 files**(v1.2 P0 대시보드 실데이터 WIP 미커밋) → **QA-B07 recurrence #2 Open 복귀**(이관 규율 6·7), ③ WT build 110→**112 modules**·`npm test` 10/4→**13/5 PASS**(FE-7 품질 게이트 충족·회귀 없음), ④ 이관 규율 5 — HEAD `5656e19` Fixed 산출물(api·routeAccess·AuthContext localStorage 0건·favicon·test) PRESENT **유효 유지**, ⑤ 잔여 BLOCK = **merge 게이트(B03·B05) + B07 recurrence #2**. test `e5fd48d` 불변(stale).

## F-1‷. 실행 요약 (2026-06-06T19:22 21차, 이력)

| 항목 | 값 |
|------|-----|
| 실행 일시 | 2026-06-06T19:21:00+00:00 |
| 검증 worktree | `src/frontend-test` (test `@e5fd48d`, working tree **clean**) |
| develop HEAD | `3fc549a` — working tree **CLEAN** (`998ac87`→`a72e249`→`3fc549a`, 4 ahead; v1.2 P0 `a72e249` 커밋) |
| build 결과 | test **PASS** (36 modules) / develop HEAD **PASS** (110 modules, JS 289.39 kB) |
| 단위 테스트 | test **N/A** / develop HEAD **`npm test` 10 tests/4 files PASS** |
| 이관 판정 | **BLOCK** (B03·B05 merge 게이트 단일 — B07 dirty-tree 21차 해소) |

## F-1‶. 실행 요약 (2026-06-06T18:45 19차, 이력)

| 항목 | 값 |
|------|-----|
| 실행 일시 | 2026-06-06T18:44:30+00:00 |
| 환경 | Node/npm, Vite 5.4.21, React 18.3.1, Vitest 2.1.9 |
| 검증 worktree | `src/frontend-test` (test `@e5fd48d`, working tree **clean**) |
| develop HEAD | `998ac87` — working tree **DIRTY** (14 mod + 21 untracked = **35 files**, v1.2 P0 미커밋) |
| 명령 | `npm run build`·`npm test`·`npm audit` (test 브랜치) + develop working tree read-only 검증 |
| build 결과 | test **PASS** (36 modules, JS 165.43 kB) / develop working tree **PASS** (107 modules, JS 276.04 kB) |
| 단위 테스트 | test **N/A** / develop working tree **`npm test` 10 tests/4 files PASS** (`routeAccess.test.jsx` 4 포함) |
| 이관 판정 | **BLOCK** (B03·B05 merge 게이트 + **B07 Planned** dirty-tree 35 files) |

> **16차(18:07) 대비 변화**: ① develop HEAD·test HEAD 불변, ② working tree **29→35 files**(v1.2 WIP 추가), ③ working tree build **FAIL→PASS**·test **FAIL→10/4 PASS**(FE-7 품질 회귀 해소), ④ B07 Planned — dirty-tree·규율 6·7 위반 **지속**. merge 게이트 B03·B05 불변.

## F-1‵. 실행 요약 (2026-06-06T18:07 16차, 이력)

| 항목 | 값 |
|------|-----|
| 실행 일시 | 2026-06-06T18:06:40+00:00 |
| 환경 | Node/npm, Vite 5.4.21, React 18.3.1, Vitest 2.1.9 |
| 검증 worktree | `src/frontend-test` (test `@e5fd48d`, working tree **clean**) |
| develop HEAD | `998ac87` — working tree **DIRTY** (14 mod + 15 untracked = **29 files**, v1.2 P0 미커밋) |
| 명령 | `npm run build`·`npm test`·`npm audit` (test 브랜치) + develop working tree read-only 검증 |
| build 결과 | test **PASS** (36 modules) / develop working tree **FAIL** (`routeAccess.js` duplicate `ROUTE_ACCESS`, 21 modules partial) |
| 단위 테스트 | test **N/A** / develop working tree **`npm test` FAIL** (6 passed/3 files; `routeAccess.test.jsx` suite FAIL duplicate symbol) |
| 이관 판정 | **BLOCK** (B03·B05 merge 게이트 + **B07 Planned** dirty-tree·WT build/test FAIL) |

> **14차(17:35) 대비 변화**: ① develop HEAD·test HEAD 불변, ② working tree **19→29 files**(v1.2 WIP 확대), ③ working tree build **PASS→FAIL**·test **10/4 PASS→FAIL**, ④ B07 Planned **강화**(WT 품질 회귀). merge 게이트 B03·B05 불변.

## F-1‴. 실행 요약 (2026-06-06T17:35 14차, 이력)

| 항목 | 값 |
|------|-----|
| 실행 일시 | 2026-06-06T17:33:07+00:00 |
| 환경 | Node/npm, Vite 5.4.21, React 18.3.1, Vitest 2.1.9 |
| 검증 worktree | `src/frontend-test` (test `@e5fd48d`, working tree **clean**) |
| develop HEAD | `998ac87` — working tree **DIRTY** (9 mod + 10 untracked, v1.2 P0 미커밋) |
| 명령 | `npm run build`·`npm test`·`npm audit` (test 브랜치) + develop working tree read-only 검증 |
| build 결과 | test **PASS** (36 modules) / develop working tree **PASS** (96 modules, HEAD 87 대비 +9) |
| 단위 테스트 | test **N/A** / develop working tree **`npm test` 10 tests/4 files PASS** (+`routeAccess.test.jsx` 4) |
| 이관 판정 | **BLOCK** (B03·B05 merge 게이트 + **B07 재발** dirty-tree) |

> **12차(16:55) 대비 변화**: ① develop HEAD 불변, ② working tree **clean→DIRTY**(19 files, v1.2 P0 선행 미커밋 — ROADMAP v1.2 `planned`, 규율 6), ③ working tree `npm test` 6→**10**·build 87→**96 modules**, ④ **QA-B07 Open 복귀**. merge 게이트 B03·B05 불변.

## F-1″. 실행 요약 (2026-06-06T16:55 12차, 이력)

| 항목 | 값 |
|------|-----|
| 실행 일시 | 2026-06-06T16:51:00+00:00 |
| 환경 | Node/npm, Vite 5.4.21, React 18.3.1, Vitest 2.1.9 |
| 검증 worktree | `src/frontend-test` (test 브랜치 `e5fd48d`, working tree **clean**) |
| develop HEAD | `998ac87` (COD 11차) — working tree **CLEAN** (미커밋 0, 9차 22 mod + 20 untracked → 0) |
| 명령 | `npm run build`·`npm test`·`npm audit` (test 브랜치) + `npm run build`·`npm test` (develop HEAD read-only 검증) |
| build 결과 | test 브랜치 **PASS** (36 modules) / develop HEAD **PASS** (87 modules, JS 247.32 kB) |
| 단위 테스트 | test 브랜치 **N/A**(`Missing script: "test"`) / **develop HEAD `npm test` 6 tests/3 files PASS** (M01 Fixed 실측) |
| 이관 판정 | **BLOCK** (merge 게이트 — 선행 v1 `pending`(B05) + v1.1 `merge_status: pending`(B03). dirty-tree·false Fixed 사유 소멸) |

> **9차(15:45) 대비 변화**: ① develop HEAD `f1c89d9`→`998ac87` — API 클라이언트·메모리 JWT 세션·Vitest·favicon **일괄 커밋**(49 files), develop working tree **CLEAN** → **QA-B07·B04 해소**, ② 이관 규율 5 — H04(`src/api/*`·페이지 fetch)·M01(test 스크립트·`*.test.jsx`·`npm test` 6 PASS)·SEC-005(`AuthContext` localStorage 부재) **전부 develop HEAD PRESENT** → **false Fixed 3건 정식 Fixed 확정**, ③ US-UX-01 favicon·reconciliation API 연동 PRESENT, ④ develop→test merge **여전히 미실행** — test 브랜치 stale, 잔여 BLOCK 사유 **B03·B05(merge 게이트) 단일**.

## F-1′. 9차(2026-06-06T14:55) baseline (이력 보존)

> develop `f1c89d9` dirty(22 mod + 20 untracked), false Fixed 3건(H04·M01·SEC-005 develop HEAD 미반영) — 12차에 `998ac87` 커밋으로 전부 해소. 상세 이력은 `transfer/frontend/packages/develop-test-diff-20260606.md` 9차 블록.

## F-2. 빌드·산출물

### F-2-1. test 브랜치 `e5fd48d` (merge 대상, in `src/frontend-test`)

| 항목 | 값 |
|------|-----|
| build 명령 | `npm run build` |
| dist JS | `index-BdwQifrL.js` — 165.43 kB (gzip 54.13 kB) |
| 모듈 수 | 36 transformed (스켈레톤 — v1.1 미머지) |
| `npm test` | **N/A** (`Missing script: "test"`) |
| npm audit (high+) | 0 high — moderate 2 (esbuild dev server, prod 무관) |

### F-2-2. develop `5656e19` working tree (read-only 검증, in `src/frontend` — 23차, DIRTY 8 files)

| 항목 | 값 |
|------|-----|
| build 명령 | `npm run build` |
| 결과 | **PASS** — 112 modules, JS 297.15 kB (gzip 90.29 kB), CSS 36.79 kB |
| `npm test` (`vitest run`) | **PASS** — 13 passed/5 files (`dashboardWidgets` 3·`routeAccess` 4·`ProtectedRoute` 3·`AuthContext` 2·`roleHomePaths` 1) |
| dirty files | **8** (6 modified + 2 untracked — v1.2 P0 대시보드 실데이터 WIP, **B07 recurrence #2**) |
| 이관 규율 5 (HEAD) | `git cat-file -e HEAD:` api·routeAccess·AuthContext(localStorage 0건)·favicon·test·`*.test.jsx`×4 **PRESENT** — HEAD Fixed 유효 |

### F-2-2″. develop HEAD `3fc549a` (read-only 검증 — 21차, working tree CLEAN, 이력)

| 항목 | 값 |
|------|-----|
| build 명령 | `npm run build` |
| 결과 | **PASS** — 110 modules, JS 289.39 kB (gzip 88.07 kB), CSS 36.70 kB |
| `npm test` (`vitest run`) | **PASS** — 10 passed/4 files |
| dirty files | **0** (clean — v1.2 P0 `a72e249` 커밋, B07 21차 해소) |

### F-2-2′. develop working tree (16차, 이력)

| 항목 | 값 |
|------|-----|
| build 명령 | `npm run build` |
| 결과 | **FAIL** — `src/auth/routeAccess.js:29` duplicate `ROUTE_ACCESS` (21 modules partial transform) |
| `npm test` (`vitest run`) | **FAIL** — 6 passed/3 files; `routeAccess.test.jsx` duplicate import/symbol (esbuild transform error) |
| dirty files | 14 modified + 15 untracked = **29** |

### F-2-3. develop HEAD `998ac87` (read-only 검증, in `src/frontend` — merge 후 test 예상치)

| 항목 | 값 |
|------|-----|
| build 명령 | `npm run build` |
| dist JS | 247.32 kB (gzip 76.57 kB) |
| dist CSS | 26.56 kB (gzip 4.88 kB) |
| 모듈 수 | **87 transformed** (전체 앱 — 21 페이지·UI·스타일) |
| `npm test` (`vitest run`) | **6 passed / 3 files** — `AuthContext.test.jsx`(2)·`ProtectedRoute.test.jsx`(3)·`roleHomePaths.test.jsx`(1) |

> test 브랜치 36 modules vs develop 87 modules 차이 = v1.1 산출물 미머지. merge 후 동등 재현 예상.

## F-3. develop HEAD vs Fixed 정합 (이관 규율 5 검증 — `git cat-file -e HEAD:<path>` @ `5656e19`)

| 산출물 | develop HEAD `5656e19` | QA Fixed | 판정 |
|--------|------------------------|----------|------|
| `ProtectedRoute.jsx` + `App.jsx` 7역할 가드 | PRESENT | H03·SEC-003 | **PASS** |
| `src/api/http.js`(`VITE_API_BASE_URL || /api/v1`)·`services.js` | PRESENT | H04 | **PASS** |
| 페이지 API 연동 (`ClientListPage`·`ReconciliationPage`·`ClientDetailPage` 건강·출석 탭) | PRESENT | H04·US-D03 | **PASS** |
| `package.json` `"test":"vitest run"`·`vite.config.js` test·`*.test.jsx`×4 | PRESENT | M01 | **PASS** |
| `AuthContext.jsx` 메모리 세션 (localStorage/sessionStorage 0건) | PRESENT | SEC-005 | **PASS** |
| `public/favicon.{svg,ico}`·`apple-touch-icon.png`·`index.html` link·theme-color | PRESENT | US-UX-01 | **PASS** |
| `src/auth/routeAccess.js` 중앙 가드 (`a72e249`) | PRESENT | v1.2 P0 | **PASS** |
| develop working tree clean | **DIRTY** (8 files — 대시보드 실데이터 WIP) | B07 | **FAIL** (recurrence #2) |

> **23차**: HEAD `5656e19`(UXD 10차) Fixed 산출물은 규율 5로 **유효 유지**(false Fixed 0건). 단 working tree 재오염 8 files(`dashboardWidgets.js/.test.js`·`DashboardPage`·`AttendancePage`·`ClientFormPage`·`GuardiansPage`·`services.js`·`GuardianListCard`) → **QA-B07 recurrence #2 Open**(이관 규율 6·7). WT build 112 modules·`npm test` 13/5 PASS(FE-7 회귀 없음).

## F-4. ROADMAP v1.1 회귀 대조 (검증 기준 = develop HEAD `57ff3c0` — 29차)

| ROADMAP 항목 | 자동 | 수동/E2E | 판정 |
|--------------|------|----------|------|
| `npm run build` SUCCESS | test 36 / develop HEAD 112 modules PASS | — | PASS |
| 7역할 화면·메뉴·권한 | 라우팅 가드 테스트·routeAccess | 7역할 로그인 E2E 미실행 | **PARTIAL** |
| **7역할 JWT 로그인·라우트 가드 E2E** | **`sevenRoleJwtLogin.test.jsx`·`sevenRoleRouteGuard.test.jsx` Vitest 자동화 130/10** | 라이브 backend E2E 미실행 | **PARTIAL 진전** (COD 20차 +93/+2) |
| ProtectedRoute·역할 가드 develop 커밋 (H03) | `ProtectedRoute.test.jsx` PASS | develop HEAD 가드 확인 | PASS |
| Must 화면 REST API 연동 (H04) | — | `src/api/*` 커밋·페이지 fetch | **PASS** |
| Vitest `npm test` (M01) | develop HEAD **130/10 PASS** | — | **PASS** |
| JWT localStorage 제거·메모리 세션 (SEC-005) | `AuthContext.test.jsx` | AuthContext HEAD localStorage 0건 | **PASS** |
| 파비콘·앱 아이콘 (US-UX-01) | — | favicon·index.html link | **PASS** |
| NHIS reconciliation UI | — | `ReconciliationPage` 행 매칭·후보 API 연동 | **PASS** |
| LoginPage DS·Modal 포커스 트랩·고대비 (WCAG 1.4.11) | — | `LoginPage.jsx`·`Modal.jsx`·`components.css` HEAD PRESENT (UXD 12차) | **PASS** |
| Must 화면 API E2E (P1–P8) | **`pilotChecklist.test.js` 라우팅 fetch-mock 자동화** (cc34f23) | 라이브 백엔드 v1 test 미승격 — live E2E 불가 | **PARTIAL** (cc34f23 라우팅 자동화 진전) |
| 보호자 초대·명세 (US-J01·J02) | **`GuardianInviteModal.test.jsx` 회귀 4건** (cc34f23) | J02 명세 API; **J01 초대 백엔드 API 미구현·스텁** | **PARTIAL** |
| develop working tree clean (QA-B07·B04) | **CLEAN** (유지) | HEAD build/test PASS | **PASS** |
| npm audit (SEC-008) | develop **0 vulnerabilities** | — | **PASS** |
| merge_status ready → merge (QA-B03) | `pending` | — | **FAIL** (잔여 BLOCK) |
| 선행 v1 merged (QA-B05) | backend v1 `pending` | — | **FAIL** (잔여 BLOCK) |

## F-5. 미실행·후속 검증

- [x] develop 산출물(api·테스트·신규 페이지·favicon) develop 커밋 후 회귀 (QA-B07·B04 — `998ac87` HEAD 확인, 12차)
- [x] **(23차 B07 recurrence #2)** develop working tree clean 회복 — `a84473f`(COD 17차 일괄 커밋)으로 CLEAN 회복·이관 규율 6·7 준수 (25차 Fixed)
- [x] develop HEAD 기준 `npm test`(Vitest) ProtectedRoute·역할 라우팅 회귀 (M01 — 130/10 @ `57ff3c0`)
- [ ] **(21차 신규)** planner: v1.2 P0 선행 커밋(`a72e249`) 범위 결정 — v1.1 흡수 vs 분리
- [ ] 7역할 JWT 로그인 → API `/api/v1/auth/login` **live E2E** (백엔드 v1 test 승격 후; Vitest 자동화는 `57ff3c0` 완료)
- [ ] Must 화면 API E2E P1–P8 (백엔드 v1 test 승격 후 라이브 연동)
- [ ] 보호자 초대 J01 — 백엔드 초대 API 구현 후 E2E (J02 명세는 연동 완료)
- [ ] v1 merged 후 develop → test merge, clean tree 재빌드(112 modules)·재테스트(130/10 PASS)

## F-6. 참조 산출물

- `transfer/frontend/checklists/test.md` — 이관 체크리스트 (판정: **BLOCK**)
- `transfer/frontend/manifests/latest.yaml` — 커밋·빌드 메타
- `transfer/frontend/packages/develop-test-diff-20260606.md` — develop/test diff

---

## 7. 서명

| 역할 | id | Backend Maven | Backend 이관 | Frontend build | Frontend 이관 | 일시 |
|------|-----|---------------|--------------|----------------|---------------|------|
| QA·이관 | TSR | (51차 baseline) test `@e8750d2` **213/213**·develop DIRTY B02 #6+B08 #2 | **BLOCK (merge+dirty-tree)** | develop `0b9b001` **DIRTY 20 files**·WT **194/38**·754 modules·**Open 1(B07 #5)** | **BLOCK (B03+B07 #5)** | 2026-06-07T08:03:37+00:00 |
| QA·이관 | TSR | test `@e8750d2` **213/213**·develop `@c3b8716` DIRTY(2U)·WT **252/252**·2커밋 ahead·ROADMAP COD35 false Fixed | **BLOCK (merge+dirty-tree)** | (교차) frontend `0b9b001` CLEAN·187/35 | **BLOCK (B03)** | 2026-06-07T07:58:46+00:00 |
| QA·이관 | TSR | (48차 baseline) test `@e8750d2` **213/213**·develop `@c3b8716` committed **249/249**·CLEAN·2커밋 ahead | **BLOCK (merge 게이트 단일)** | develop `c98f98d` **CLEAN**(B07 #4 신호 소멸)·HEAD build **752**(FE-15 3청크)·npm test **186/34**·audit 0 | **BLOCK (B03 단일)** | 2026-06-07T06:36:45+00:00 |
| QA·이관 | TSR | test `@e8750d2` **213/213**·develop `@c3b8716` committed **249/249**·**B02 #5·B08 Fixed**(규율 5 PASS)·**CLEAN**·2커밋 ahead | **BLOCK (merge 게이트 단일)** | (교차) `4be0938` 재오염 5 files(B07 #4 신호) | **BLOCK (B03)** | 2026-06-07T06:25:00+00:00 |
| QA·이관 | TSR | test `@e8750d2` **213/213**·WT **249/249**(+6)·COD Fixed **FAIL**·DIRTY **3M+4U** B02 #5+B08 | **BLOCK** | (45차 baseline) frontend B07 #3 76 files | **BLOCK (B07 #3 + B03)** | 2026-06-07T05:30:00+00:00 |
| QA·이관 | TSR | (44차 baseline) backend 213/213·WT 243/243·DIRTY B02 #5+B08 | **BLOCK** | develop `3fdc266` DIRTY **76 files**·WT **181/30**·749 modules | **BLOCK (B07 #3 + B03)** | 2026-06-07T05:02:36+00:00 |
| QA·이관 | TSR | test `@e8750d2` **213/213**·WT **243/243**·COD Fixed **FAIL**·DIRTY B02 #5+B08 | **BLOCK** | (43차 baseline) frontend B07 #3 | **BLOCK** | 2026-06-07T04:59:37+00:00 |
| QA·이관 | TSR | (42차 baseline) backend 213/213·WT 243/243 | **BLOCK** | develop `3fdc266` DIRTY **72 files**·WT **179/29**·748 modules | **BLOCK (B07 #3 + B03)** | 2026-06-07T04:27:22+00:00 |
| QA·이관 | TSR | test `@e8750d2` **213/213**·WT **240/240**·COD Fixed **FAIL**·DIRTY B02 #5+B08 | **BLOCK** | (39차 baseline) frontend B07 #3 | **BLOCK** | 2026-06-07T03:45:21+00:00 |
| QA·이관 | TSR | (38차 baseline) backend 213/213·DIRTY B02 #5+B08 | **BLOCK** | develop `3fdc266` DIRTY **60 files**·WT **169/24**·743 modules | **BLOCK (B07 #3 + B03)** | 2026-06-07T03:09:08+00:00 |
| QA·이관 | TSR | (36차 baseline) backend 213/213·DIRTY B02 #5+B08 | **BLOCK** | develop `3fdc266` DIRTY **44 files**·WT **161/20**·741 modules | **BLOCK (B07 #3 + B03)** | 2026-06-07T02:27:54+00:00 |
| QA·이관 | TSR | test `@e8750d2` **213/213 PASS**·develop **DIRTY** B02 #5+B08·Open 0 | **BLOCK** | (35차 baseline) frontend B07 #3 | **BLOCK** | 2026-06-07T02:22:44+00:00 |
| QA·이관 | TSR | test `@e8750d2` **213/213 PASS**·SEC-007 PASS·develop **DIRTY 8**(B02 #5+B08) | **BLOCK** | (33차 baseline) develop `3fdc266` DIRTY B07 #3 | **BLOCK (B07 #3 + B03)** | 2026-06-07T01:45:00+00:00 |
| QA·이관 | TSR | (30차 유효) develop `e8750d2` CLEAN·Maven 79/79 PASS | **BLOCK (B01·SEC-007 merge 게이트 단일)** | develop `3fdc266` **CLEAN**·build **113**·npm test **140/11**·audit 0 | **BLOCK (B03·B05)** | 2026-06-07T00:43:00+00:00 |
| QA·이관 | TSR | develop `e8750d2` **CLEAN**(COD 21차 — SevenRoleJwtLoginE2eTest 커밋·B02 #4 Fixed)·@Test **199**(+16), Maven 79/79 PASS | **BLOCK (B01·SEC-007 merge 게이트 단일 — B02 #4 Fixed)** | (29차 baseline 유효) develop `57ff3c0` CLEAN·build 112·npm test 130/10 PASS·audit 0건 | **BLOCK (B03·B05 merge 게이트 단일)** | 2026-06-07T00:28:00+00:00 |
| QA·이관 | TSR | (28차 유효) develop `c3f3146` DIRTY·@Test 183, Maven 79/79 PASS, B02 recurrence #4 Open | **BLOCK (B01·SEC-007·B02 recurrence #4)** | develop `57ff3c0` **CLEAN**(COD 20차 — 7역할 JWT 로그인·라우트 가드 Vitest E2E 자동화)·HEAD build **112**·npm test **130/10 PASS**(+93/+2)·audit 0건 | **BLOCK (B03·B05 merge 게이트 단일)** | 2026-06-06T23:31:00+00:00 |
| QA·이관 | TSR | develop `c3f3146` DIRTY·@Test 183, B02 recurrence #4 Open | **BLOCK (B01·SEC-007·B02 recurrence #4)** | develop `07fd305` **CLEAN**(UXD 13차 — Switch.jsx WAI-ARIA·Switch.test.jsx 5건)·HEAD build **112**·npm test **37/8 PASS**·audit 0건 | **BLOCK (B03·B05 merge 게이트 단일)** | 2026-06-06T23:19:00+00:00 |
| QA·이관 | TSR | (26차 유효) develop `c3f3146` CLEAN·@Test 183, Maven 79/79 PASS | **BLOCK (B01·SEC-007 merge 게이트 단일)** | develop `cc34f23` **CLEAN**(COD 19차 — 파일럿 P1–P8·J01/J02 Must API 라우팅 자동화)·HEAD build **111**·npm test **32/7 PASS**·audit 0건 | **BLOCK (B03·B05 merge 게이트 단일)** | 2026-06-06T22:40:00+00:00 |
| QA·이관 | TSR | develop `c3f3146` CLEAN·@Test **183**(+29 PilotChecklist), Maven 79/79 PASS, R-04 65건 진전 | **BLOCK (B01·SEC-007 merge 게이트 단일)** | develop `404a30e` **CLEAN**(UXD 12차 — LoginPage DS·Modal 포커스 트랩·고대비)·HEAD build **111**·npm test 13/5 PASS·audit 0건 | **BLOCK (B03·B05 merge 게이트 단일)** | 2026-06-06T22:20:00+00:00 |
| QA·이관 | TSR | (24차 유효), develop `aa71412` CLEAN·@Test 154 | **BLOCK (B01·SEC-007 merge 게이트 단일)** | develop `ed1bf22` **CLEAN**(B07 #2 Fixed `a84473f`)·HEAD build **111**·npm test 13/5 PASS·**npm audit 0건**(SEC-008 Fixed) | **BLOCK (B03·B05 merge 게이트 단일)** | 2026-06-06T21:32:00+00:00 |
| QA·이관 | TSR | PASS (test 79/79), develop `aa71412` **CLEAN**·@Test **154**·R-02 [x]·COD 16차 | **BLOCK (B01·SEC-007 merge 게이트 단일)** | develop `2d742b3` **DIRTY 8 files**(B07 recurrence #2 Planned)·WT build **114**·npm test 13/5 PASS·**npm audit 5 vuln(1 critical) ⚠** | **BLOCK (B03·B05 + B07 Planned + SEC-008 MEDIUM)** | 2026-06-06T21:13:00+00:00 |
| QA·이관 | TSR | (22차 유효), develop `4274459` CLEAN·B02 Fixed·@Test 120 | **BLOCK (B01·SEC-007 merge 게이트 단일)** | develop `5656e19` **DIRTY 8 files**(B07 recurrence #2)·WT build 112·npm test 13/5 PASS·HEAD Fixed 규율 5 PRESENT | **BLOCK (B03·B05 + B07 recurrence #2)** | 2026-06-06T20:17:00+00:00 |
| QA·이관 | TSR | PASS (test 79/79), develop `4274459` **CLEAN**·B02 Fixed·@Test 120 | **BLOCK (B01·SEC-007 merge 게이트 단일)** | develop `3fc549a` CLEAN·HEAD build 110·npm test 10/4 PASS | **BLOCK (B03·B05 merge 게이트 단일)** | 2026-06-06T20:11:41+00:00 |
| QA·이관 | TSR | (20차 유효), develop `b5d70a8` DIRTY·B02 recurrence #3 | **BLOCK (B01·SEC-007·B02)** | develop `3fc549a` **CLEAN**·HEAD build 110·npm test 10/4 PASS·B07 해소 | **BLOCK (B03·B05 merge 게이트 단일)** | 2026-06-06T19:22:00+00:00 |
| QA·이관 | TSR | PASS (test 79/79), develop `b5d70a8` **DIRTY**·B02 recurrence #3 | **BLOCK (B01·SEC-007·B02)** | dirty 42 files (35→42) | **BLOCK (B03·B05·B07)** | 2026-06-06T19:12:00+00:00 |
| QA·이관 | TSR | PASS (82/79) | BLOCK | PASS | BLOCK | 2026-06-06T07:42:00+00:00 |
| QA·이관 | TSR | PASS (test 79/79) | BLOCK | (frontend 미재검) | BLOCK | 2026-06-06T14:45:00+00:00 |
| QA·이관 | TSR | (backend 미재검) | BLOCK | PASS (test build, N/A test) | BLOCK | 2026-06-06T14:55:00+00:00 |
| QA·이관 | TSR | PASS (test 79/79) | BLOCK | dirty 확대(20U) | BLOCK | 2026-06-06T15:38:00+00:00 |
| QA·이관 | TSR | (8차 유효 79/79) | BLOCK | PASS (build), N/A test | BLOCK | 2026-06-06T15:45:00+00:00 |
| QA·이관 | TSR | PASS (test 79/79), develop `4d476c6` clean·B06/B02 해소 | BLOCK (B01 단일) | (11차 미재검) | BLOCK | 2026-06-06T16:40:00+00:00 |
| QA·이관 | TSR | (13차 유효) | BLOCK (B01·SEC-007) | PASS (test 36·develop WT 96 modules·npm test 10/4) | **BLOCK (B03·B05·B07)** | 2026-06-06T17:35:00+00:00 |
| QA·이관 | TSR | (15차 유효) | BLOCK (B01·SEC-007·B02) | WT build/test **FAIL**·29 dirty files | **BLOCK (B03·B05·B07)** | 2026-06-06T18:07:00+00:00 |
| QA·이관 | TSR | PASS (test 79/79), develop `b5d70a8` **CLEAN**·B02 recurrence Fixed | **BLOCK (B01·SEC-007 — merge 게이트 단일)** | (16차 유효) | BLOCK (B03·B05·B07) | 2026-06-06T18:34:00+00:00 |
| QA·이관 | TSR | (18차 유효) | BLOCK (B01·SEC-007) | WT build/test **PASS**·35 dirty files | **BLOCK (B03·B05·B07)** | 2026-06-06T18:45:00+00:00 |
| QA·이관 | TSR | PASS (test 79/79), develop `b5d70a8` CLEAN·상태 불변 | **BLOCK (B01·SEC-007 — merge 게이트 단일)** | (17차 유효) | BLOCK (B03·B05·B07) | 2026-06-06T18:42:16+00:00 |
| QA·이관 | TSR | PASS (test 79/79), develop `fac3d07` DIRTY·B02 recurrence | BLOCK (B01·SEC-007·B02) | (14차 유효) | BLOCK | 2026-06-06T18:04:00+00:00 |
| QA·이관 | TSR | PASS (test 79/79), develop `fac3d07` clean·fac3d07 RBAC/guidance | BLOCK (B01·SEC-007) | (12차 유효) | BLOCK | 2026-06-06T17:30:00+00:00 |
| QA·이관 | TSR | (11차 유효 79/79, develop `4d476c6` clean) | BLOCK (B01) | PASS (develop 87 modules·`npm test` 6/6; test 36 skel), develop `998ac87` clean·B07/B04/H04/M01/SEC-005 해소 | BLOCK (B03·B05 merge 게이트) | 2026-06-06T16:55:00+00:00 |
