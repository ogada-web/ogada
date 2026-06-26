<!-- doc:owner=TWR doc:audience=PLN,COD,TSR,UXD,DBA,BNK updated=2026-06-26T10:00:00+09:00 -->
# ogada 운영 문서 (docs/ops/)

> **작성**: tech_writer 에이전트  
> **생성일**: 2026-06-13  
> **상태**: MVP v1 개발 중 — **377차 자동 동기화 완료** (BE `d06e3f1`·FE `4bbd54a`·V1–V180·118 route·93 page·**Q722 recovered-auth readiness hints**)  
> **최종 갱신**: 2026-06-26 (377차 TWR — **Q722·Q713 deepen · baseline 정합**)

---

## 📚 문서 네비게이션

이 디렉토리(`docs/ops/`)는 ogada 도입·운영·관리를 위한 **실무 문서**를 제공합니다.  
역할·목적별로 읽을 문서를 아래에서 선택하세요.

---

## 1. 새로운 고객사·센터를 위한 문서

### 🚀 **DEPLOYMENT_GUIDE.md** — 배포·인프라·초기 설정

**대상**: DevOps, IT 인프라 담당자

**포함 내용**:
- 클라우드 배포 환경 설정 (Docker, PostgreSQL, Spring Boot 실행)
- 데이터베이스 마이그레이션 (Flyway **V1–V180**, G21 NHIS 비교·G32 케이스관리·**V180 program group integrity**·**V179 프로그램 그룹**·**V178 CMS·목욕 CHECK**·**V177 목욕 전후관찰**)
- 환경 변수·시크릿 관리 (API 키, JWT 시크릿, Kakao 배차 API, CMS 연동)
- SSL/HTTPS 설정
- 모니터링·로그 수집
- 백업·복구

**최신 항목** (2026-06-26, 377차):
- **Q722** — **QA-B95 recovered-auth readiness hints** — **`liveE2eBootstrapEnableHint`** BE expose (`d06e3f1`) · FE parse·neutral filter (`4bbd54a`)
- **Q713 deepen** — allow-recovered-auth + hint **full-stack align**
- **baseline 정합** — FAQ·DEPLOYMENT·ADMIN **`d06e3f1`/`4bbd54a`** · **118 route · 93 page**

**이전 항목** (2026-06-26, 376차):
- **Q719** — **G21 seed `service-unavailable` vs `disabled` 분리** — health **`liveE2eG21SeedStatusDetail`** precision (`42a369e`)
- **Q720** — **QA-B95 neutral operation blocker filter** — **`none`/`ok` placeholder 제외** (`7e7c296`)
- **Q721** — **V180 program_client_groups integrity** — 3-way FK·active-client guard (`42a369e`)
- **UXD-165** — **`StaffMonthlySchedulePage` a11y** · **`.ds-refund-fee-preview` CSS** (`bee97b9`)
- **baseline 정합** — FAQ·DEPLOYMENT·ADMIN **`42a369e`/`7e7c296`** · **118 route · 93 page**

**이전 항목** (2026-06-26, 375차):
- **Q717** — **G-STAFF-MONTHLY-SCHEDULE-FE-WIRE** — **`/staff/schedules`** PLAN visit aggregation · G-SMS message_kind=21 (`33944e4`)
- **Q718** — **QA-B95 singular operation blocker merge** — **`liveE2eOperationBlocker`** fallback (`b7004ca`)
- **Q713 deepen** — **BE `allow-recovered-auth`** health/probe align (`3342938`)
- **baseline 정합** — FAQ·DEPLOYMENT·ADMIN **`3342938`/`b7004ca`** · **118 route · 93 page**

**이전 항목** (2026-06-26, 374차):
- **Q716** — **QA-B95 string-form operation blocker normalize** — health·probe state comma/semicolon/newline split (`2c9abd6`·`bd3253a`)
- **Q713 deepen** — persisted **`.live-backend-state.json`** string blocker parsing (`bd3253a`)
- **baseline 정합** — FAQ·DEPLOYMENT·ADMIN **`49fe2e7`/`bd3253a`**

**이전 항목** (2026-06-26, 373차):
- **Q714 deepen** — **5-9 group-history** V179 membership 집계 · **`groupConfigAvailable=true`** (`337453d`)
- **Q715** — program reports optional **`branchId`** query · JWT scope (`49fe2e7`)
- **Q713 deepen** — **`liveBackendProbe`** health **`reason`** surfacing (`f74a6e7`)
- **baseline 정합** — FAQ·DEPLOYMENT·ADMIN **`49fe2e7`/`f74a6e7`**

**이전 항목** (2026-06-26, 372차):
- **Q713 deepen** — **`bootstrapServiceAvailable` probe field** — disabled vs bean-missing 분리 (`0e55f3b`)
- **Q713 deepen** — **`bootstrap-unavailable` blocker auth-recovery filter** (`75c0f51`)
- **baseline 정합** — FAQ·DEPLOYMENT·ADMIN **`0e55f3b`/`75c0f51`**

**최신 항목** (2026-06-25, 371차):
- **Q714** — **G-REPORT-DENSITY M5 program reports** — **`/programs/reports/*`** 5-7~5-10 · **BE `650801b` · FE `15a3b7f`**
- **baseline 정합** — FAQ·DEPLOYMENT **`650801b`/`15a3b7f`** · **117 route · 92 page**

**최신 항목** (2026-06-25, 370차):
- **Q705 deepen** — **목욕 FE full-stack ✅** 정합 — USER_MANUAL §1-5·§5-26
- **Q712 deepen** — **M7 7-9 lifecycle** — §5-10-0 환불 수수료 cross-ref
- **baseline 정합** — FAQ·DEPLOYMENT **`9f67954`/`5914b2f`**

**최신 항목** (2026-06-25, 369차):
- **Q709 deepen** — **`EasyPayProviderCatalogPanel`** FE wire (`5914b2f`)
- **Q710 deepen** — **`TransportParityRulesPanel`** page mount (`5914b2f`)
- **Q713 deepen** — **`enforce-bootstrap-readiness`** env · health **`liveE2eBootstrapReadinessEnforced`** (`9f67954`)

**최신 항목** (2026-06-25, 368차):
- **Q712 deepen** — **`feePolicyCode` `@Pattern` Bean Validation** — invalid code **`400`** (`79725eb`)
- **Q713** — **QA-B95 effective operation readiness** — **`liveE2eEffectiveOperationReady`** after auth recovery (`e070c45`)

**최신 항목** (2026-06-25, 367차):
- **Q712 deepen** — **7-9 refund fee full-stack** — **`RefundRecordModal`** · **`feePolicyCode` net validation** (`cadd74a`·`aeecc1b`)

**최신 항목** (2026-06-25, 366차):
- **Q712** — **7-9 copay refund fee catalog** — KCP **3.3%/500원** · **`GET/POST /billing/copay/refund-fee-*`** (`2adae59`)
- **Q705 deepen** — **목욕 FE full-stack** — **`BathingScheduleIndicator27Panel`** · **전·후 관찰 폼** (`3d7f13b`)

**최신 항목** (2026-06-25, 365차):
- **Q711** — **연차 `branchName` 공백 fallback** — **`BranchScopeNotice` trim·지점 ID 라벨** (`58f3858`)
- **Q709 deepen** — **`EasyPayControllerRoutingTest`** — provider-catalog **routing·RBAC lock** (`5a5174a`)

**최신 항목** (2026-06-25, 364차 — **369차에서 FE closure 완료**):
- **Q709** — **7-5 easy-pay provider-catalog** — **`GET /billing/easy-pay/provider-catalog`** CARD·KAKAO_PAY · **FE wire ✅** (`5914b2f`, 369차)
- **Q710** — **G16 `TransportParityRulesPanel`** — **`/transport/service-fees` mount ✅** (`5914b2f`, 369차)
- **V178** — **CMS collection·목욕 관찰 DB CHECK** — defense-in-depth (`3c1fdce`)

**최신 항목** (2026-06-25, 363차):
- **Q708** — **CMS catalog EmptyState** — 빈 **`entries[]`** 시 **「카탈로그 정보 없음」** · **수납 탭은 독립 동작** (`9a583ec`)
- **Q706·Q707** — **NHIS 자동 매칭 의사결정표** — USER_MANUAL §4-6-1 · alt-key Badge spot-check
- **Q705** — **목욕 전·후 관찰·지표27** — USER_MANUAL §5-26 (**FE ✅ `3d7f13b`**)
- **Q703** — **G16 parity-rules `description`/`bodyKo` fallback** — USER_MANUAL §5-8-1

**최신 항목** (2026-06-25, 362차):
- **Q707** — **G-NHIS-ALT-KEY-AUDIT-BADGE** — **`altKeyMatched`** API·UI Badge · **`4963535`/`5bb84a6`**
- **Q706** — **G-NHIS-MASKED-NAME-FALLBACK** — 마스킹 수급자명 alt-key · **`37416ac`**

**최신 항목** (2026-06-25, 360차):
- **Q703** — **G16 parity-rules API spec + RBAC** — 응답 **`code`·`label`·`description`** · **`social_worker` 403** · **`e4f83af`**
- **Q578** — **live E2E placeholder casing·whitespace 정규화** — **`5afef2d`**

**최신 항목** (2026-06-25, 359차):
- **Q701·Q704** — **G2b CMS 5/5 full-stack** — **`CmsCollectionPanel`** 가상계좌·다계좌 탭 · **M7 7-4 coverage 1.0** · **`9aeedfe`**
- **Q703** — **G16 parity-rules FE wire** — **`TransportServiceFeePanel`** · **`fetchTransportServiceFeeParityRulesApi`**
- **Q705** — **US-O01 목욕 전·후 관찰 + 평가지표 27 compliance API** · **`GET /care/bathing-schedules/indicator-27-compliance`** · **V177** · **`e12b084`**
- **Q704** — **G2b CMS collection methods closure** — **가상계좌·다계좌 정산** BE API · **FE `CmsCollectionPanel` full-stack** · **V176** · **`dac8ebd`/`9aeedfe`**
- **Q703 신규** — **G16 NHIS #44 parity-rules API** · **`GET /transport/service-fee-parity-rules`** · 4-rule catalog (`bd1e87e`)
- **Q702 신규** — **live E2E bootstrap** · **`OGADA_LIVE_E2E_BOOTSTRAP_ENABLED`** toggle (`670756a`/`c3c6272`)

**최신 항목** (2026-06-24, 356차):
- **Q701** — **G2b CMS payment-method-catalog** — **`/billing/cms`** 5-method catalog panel · **수납 5/5 완성** (`dac8ebd`)
- **Q703** — **G16 NHIS #44 parity rules API** — **`GET /transport/service-fee-parity-rules`** · 4-rule catalog · **`oneWayRatio=0.5`** (`bd1e87e`)
- **Q702** — **live E2E bootstrap** — **`OGADA_LIVE_E2E_BOOTSTRAP_ENABLED`** · QA-B95 blocker gating · skip dedupe (`670756a`/`64a7648`/`c3c6272`)

**최신 항목** (2026-06-24, 352차):
- **Q699** — **G-SMS dispatch success label** — 발송 성공 Alert **괄호 한글명** · **`formatGsmDispatchSuccessMessage`** (`c7d0982`)
- **Q692 갱신** — **staff dispatch `ezcareMessageKind`** — 접속키(1)·일정표-직원(21) API parity (`2f83563`)

**최신 항목** (2026-06-24, 351차):
- **Q696** — **UXD-161 G-SMS form-stack** — **`GuardianDocumentNotifyPanel`**·**`StaffNotificationDispatchPanel`** 필드 간격 (`4adeb1c`)
- **Q697** — **readiness fallback label sync** — ezCare **본인부담 안내·급여제공내역·직원인권보호** (`3f686e3`)
- **Q698** — **health `liveE2eG21SeedStatusDetail`** — bootstrap disabled contract test lock (`88a58d9`)

**최신 항목** (2026-06-24, 349차):
- **Q692** — **발송 API `ezcareMessageKind` 응답** — catalog crosswalk 11·12·13·19·21·1 (`ef8bb4e`)
- **Q686·Q690 갱신** — **`dispatchReady` 채널 자격** — SMS key/secret/sender · ALIMTALK + PF ID (`fed6f1f`)
- **message_kind 11·13·19 UI** — **`GuardianDocumentNotifyPanel`**·**`BillingDetailPage`** ezCare 라벨 (`5a6d42c`)

**최신 항목** (2026-06-24, 348차):
- **Q691** — **STAFF_ACCESS_KEY SMS dispatch** — **`POST …/staff/notifications/staff-access-key`** · catalog **6/6 dispatchImplemented** (`1d5d441`)
- **Q687·Q689 FE wire** — **`GuardianDocumentNotifyPanel`** 일정표-수급자 · **`StaffNotificationDispatchPanel`** 일정표-직원·접속키 (`9c25d44`)

**최신 항목** (2026-06-24, 347차):
- **Q689** — **STAFF_MONTHLY_SCHEDULE alimtalk dispatch** — **`POST …/staff/notifications/staff-monthly-schedule`** · catalog **5/6 dispatchImplemented** (`b9d0599`)
- **Q690** — **발송 대기 UI** — readiness 패널 **「발송 대기 N종」** Alert·목록 (`c04968c`)

**최신 항목** (2026-06-24, 346차):
- **Q687** — **CLIENT_MONTHLY_SCHEDULE alimtalk dispatch** — **`POST …/client-monthly-schedule`** · catalog **4/6 dispatchImplemented** (`8631d1e`)
- **Q688** — **UXD-160 a11y** — catalog Alert·FAQ21823 보관 Alert·재계약 버튼 (`15f2195`/`068049b`)
- **Q686 deepen** — **`dispatchReadyCount`** 집계 · 패널 **「발송 구현 N종 중 M종 발송 가능」** Alert (`fb323ae`/`15f2195`)

**최신 항목** (2026-06-24, 345차):
- **Q686 deepen** — **G-SMS-TEMPLATE-CATALOG full-stack** — **`NotificationChannelReadinessPanel`** ezCare 6종 catalog · **`dispatchReady`** (`b6c9b16`/`c9cf03b`)

**최신 항목** (2026-06-24, 344차):
- **Q686** — **G-SMS-TEMPLATE-CATALOG BE** — **`GET /notifications/template-catalog`** 6종 parity · **`dispatchReady`** (`b6c9b16`)
- **Q540·Q685 갱신** — **FAQ21823 compliance API** — 대시보드 **3 StatCard** · 목록·Alert **`fetchStaffEmploymentContractComplianceApi`** (`9aaefa0`/`d682562`)

**최신 항목** (2026-06-24, 343차):
- **Q685** — **FAQ21823 3년 보관 D-day·서식 인쇄** — **`EMPLOYMENT_CONTRACT_RETENTION_WARNING_DAYS=90`** · **`window.print`** (`a43bcb7`)
- **Q684 deepen** — **live E2E `liveE2eOperationReason`** health·probe BE canonical (`d11263b`)
- **Q684** — **live E2E bootstrap service-unavailable** — disabled vs bean-missing 진단 분리 · health hint · FE **`liveE2eOperationReason`** probe (`0494334`/`cba9ff8`)
- **Q12 정정** — **caregiver 수정 ✅** · **신규 등록 social_worker+** (Q675와 정합)

**최신 항목** (2026-06-24, 341차):
- **Q677~Q683** — **addressDetail-only PATCH** · **G16 NHIS #44 UI** · **Solapi fail-closed** · **bootstrap hint** · **leave-ledger·employment-contract harness** · **UXD-159 a11y**

**최신 항목** (2026-06-23, 338차):
- **Q675** — **client RBAC hierarchy** — **`caregiver` PATCH ✅** · **create social_worker+** · **`clientPermissions.js`** (`01edba7`/`77584a0`)
- **Q676** — **`addressSearch`·`addressDetail` read API** — 수정 화면 prefill (`deda5b4`)

**최신 항목** (2026-06-23, 337차):
- **Q671** — **US-D01/D02 Korean address** — **`addressSearch`+`addressDetail`** · **`KoreanAddressFields` Kakao postcode** · **거주지 전체 표시** (`642ea11`/`0606a3b`)
- **Q672** — **`/clients` column filters** — **`TableColumnFilter`** 등급·성별·배차·지점 (`7e048c0`)
- **Q673** — **거주지 vs 픽업 마스킹 분리** — list/detail **전체 거주지** · **픽업 road-level** (`642ea11`)
- **Q674** — **HR `branchName` → `BranchScopeNotice`** — annual-leaves·leave-ledger (`64584f4`)

**최신 항목** (2026-06-23, 336차):
- **Q668** — **V175 leave-ledger DB integrity** — memo nonempty CHECK · **user_branches FK** (`c4e6bcb`)
- **Q669** — **`SOCIAL_WORKER` users read RBAC** · **client address road-level masking** — transport roster 정책 정합
- **Q670** — **live-e2e `e2e*` tenant UUID** — dev seed `00000001` 계열과 **분리**

**최신 항목** (2026-06-23, 335차):
- **Q667** — **US-R01-c leave-ledger UXD-157 a11y** — **`StaffLeaveLedgerTable`**·**`StaffLeaveLedgerDeleteModal`**·**`DateInput`** · **BNK-551 AVAILABLE sync** (`bd1d0ad`/`426d63a`)
- **Q666 deepen** — 대장 화면 조작·pilot checklist·live routing harness (`8057c1e`/`5fd12dd`)

**최신 항목** (2026-06-23, 334차):
- **Q666** — **US-R01-c leave-ledger FE full-stack** — **`StaffLeaveLedgerPage`**(`/staff/leave-ledger`) · **`pilotChecklist` R01c-a/b/c/d** · **`StaffLeaveLedgerLiveApiRoutingE2eTest`** (`8057c1e`/`5fd12dd`)
- **Q665** — **US-R01-c leave-ledger RBAC+pilot test** — **`RoleBasedControllerAccessTest.StaffLeaveLedgerAccess`** · **`StaffLeaveLedgerPilotServiceFlowE2eTest`** · **`hq_admin` CUD 403** (`62fce23`)
- **Q663 deepen** — 대장 API RBAC 표·역할별 운영 가이드

**최신 항목** (2026-06-23, 332차):
- **Q663** — **US-R01-c canonical leave-ledger BE API** — **`GET/POST/PUT/DELETE /staff/leave-ledger*`** · **V174** · **`relatedSurfaces` PLANNED→AVAILABLE** (`bb9df48`)
- **Q664** — **live E2E suite guard `liveCashReceiptDescribe`** — **QA-B268 Fixed** (`b7101d5`)
- **Q655·Q659 갱신** — 대장 **BE API ✅** · **FE Route 후속**

**최신 항목** (2026-06-23, 331차):
- **Q662** — **G2 CMS roster `status` filter normalization** — trim·uppercase · `ACTIVE`/`CANCELLED`/`PENDING` · unsupported → `422` (`f1225b0`)
- **Q658·Q661 갱신** — **QA-B266 Fixed** @ `949e9bf` (2049/2049 PASS) · Vitest pollution 재발 방지 규칙 유지

**최신 항목** (2026-06-23, 330차):
- **Q661** — **Vitest 동시 실행·full-suite pollution 운영 대응** — `npm-test-locked.sh`·`vitest-stop.sh`·**QA-B266** merge gate 절차

**최신 항목** (2026-06-23, 329차):
- **Q658** — **QA-B266 Open** — develop `npm test` **2048/2049 FAIL** · `StaffAnnualLeavePage` branch scope · isolated **8/8 PASS** · merge **BLOCK**
- **Q659** — **US-R01-c `/staff/leave-ledger` P1 candidate** — monthly snapshot vs canonical ledger 분리 · **PLANNED** cross-link contract
- **Q660** — **M6 v3.1** — **`/meals` LIVE** · **`/safety/*` PLANNED** (6-2~6-4)

**최신 항목** (2026-06-23, 328차):
- **Q656** — **G-STAFF-ANNUAL-LEAVE multi-branch activeBranch fallback** — **`branchId` 생략** 시 **`TenantContext.activeBranchId`** roster (`40ab9e7`)
- **Q657** — **US-R01 HR roster UX** — **`RelatedSurfacesPanel`·UXD-156** · **`BranchScopeNotice`** on **`/staff/annual-leaves`·`/staff/attendance`** (`c183ebd`/`949e9bf`)

**최신 항목** (2026-06-23, 327차):
- **Q654** — **G-COMM-CALLER-AUTH P3** — Solapi **발신번호 본인인증은 ogada 범위 밖** · `SOLAPI_SENDER_ID` **외부 인증** 필수
- **Q655** — **US-R01 `/staff/leave-ledger` PLANNED** — v3 Must 대장 · **cross-link contract** · 대장 출시 전 **중복 입력 금지**

**최신 항목** (2026-06-23, 326차):
- **Q653** — **G-STAFF-WORK-ATTENDANCE API cross-link metadata** — **`GET /staff/work-attendance`** **`surfaceKind`·`relatedSurfaces[]`** · FE **`normalizeStaffWorkAttendanceResponse`** (`83a26e7`/`95f55aa`)
- **Q651·Q652 deepen** — **양방향 HR nav API contract** — 연차 ↔ 출퇴근 roster **대칭 메타**

**최신 항목** (2026-06-23, 325차):
- **Q652** — **HR 화면 역할 분리 통합 참조** — 출퇴근(8-4)·연차(US-R03e)·대장(US-R01) **데이터 중복 금지** · Q648·Q650·Q651 단일 운영 표
- **ADMIN_GUIDE §1-4** — baseline **`6ab3760`/`2040571`** 정정 · HR nav 양방향 smoke 안내

**최신 항목** (2026-06-23, 324차):
- **Q651** — **G-STAFF-WORK-ATTENDANCE reverse cross-links** — **`/staff/attendance`** → **「연차휴가 현황」** · **`StaffAnnualLeaveRelatedSurfacesPanel` `helpText`** (`2040571`)
- **Q648·Q650 deepen** — **양방향 HR nav** — 연차 ↔ 출퇴근 cross-link closure

**최신 항목** (2026-06-23, 323차):
- **Q650** — **G-STAFF-ANNUAL-LEAVE related surfaces panel** — 출퇴근 링크·대장 (준비 중) · yearly GET/PUT cross-link (`6ab3760`/`0b0d7ba`)
- **Q648 deepen** — yearly 응답에도 **`surfaceKind`·`relatedSurfaces`** 포함

**최신 항목** (2026-06-23, 322차):
- **Q648** — **G-STAFF-ANNUAL-LEAVE roster cross-link** — `surfaceKind`·`relatedSurfaces` US-R01 (`bbf333c`)
- **Q649** — **live API harness·PILOT_CHECKLIST** — `staffAnnualLeaveLiveApi.e2e.test.js`·R03e/E05 (`96e9d25`/`e296387`)

**최신 항목** (2026-06-22, 317차):
- **Q639 deepen** — **G-STAFF-ANNUAL-LEAVE** — 음수 월별 사용 **`422`「월별 사용일수는 0 이상이어야 합니다.」** (`a45745c`)
- **Q640 deepen** — **live E2E default-credential variant recovery** — `default-staff-credentials`·placeholder wording (`a170f9c`)

**최신 항목** (2026-06-22, 316차):
- **Q640** — **live E2E default-credential blocker recovery** — auth ready 시 `*-credentials-default` skip 제외 (`6fcd750`)
- **Q639 deepen** — **G-STAFF-ANNUAL-LEAVE** — `branchId` 생략 activeBranch fallback · RBAC·pilot tests (`6b84bcd`)

**최신 항목** (2026-06-22, 315차):
- **Q639** — **G-STAFF-ANNUAL-LEAVE** — `/staff/annual-leaves` · V172 · ezCare worker-b100 tab01 parity
- **Q638** — **G2-CMS-ENROLLMENT-ROSTER deepen** — FilterChips·`?clientId=` deep link·`/billing/payments` CMS 등록 열
- **Q637** — **G2 CMS branch roster** — `GET /billing/cms/enrollments` without `clientId` (Q638에서 deepen)
- **Q635** — **G34-WORKFLOW-CATALOG** — `/compliance/workflow-catalog` ezCare FAQ 21795–21828 cross-walk

**관련 링크**: FAQ §Q594–Q597 · API_SPEC §9-16/9-17/9-18 · REQUIREMENTS §7-2·§7-8·§3-13

---

## 2. 현장 사용자 (센터장·요양보호사·사회복지사·보호자)

### 📖 **USER_MANUAL.md** — 일상 사용 절차서

**대상**: 센터장(`branch_admin`), 요양보호사(`caregiver`), 사회복지사(`social_worker`), 보호자(`guardian`)

**포함 내용**:
- 로그인·계정 관리
- 역할별 홈 화면·메뉴 구조
- **이용자 관리**: 등록, 상세 프로필(§2-2 기본정보·컬럼 설명)
- **출석 관리**: 수기 체크인/아웃, **QR B방식 셀프 스캔** (보호자 동반 도착/귀가)
- **건강 기록**: 일일 체크(혈압·체온·혈당·산소포화도), 투약, 특이사항, 이력 조회
- **청구·정산**: 수가표 관리, 월별 청구서 생성, 본인부담금 계산, **NHIS 엑셀 import**
- **대시보드**: 지점별·통합 현황·통계

**최신 항목** (2026-06-25, 369차):
- **Q709** — **7-5 provider-catalog FE** — **`EasyPayProviderCatalogPanel`** · §4-6 (`5914b2f`)
- **Q710** — **G16 parity panel mount** — **`TransportParityRulesPanel`** · §5-8-1 (`5914b2f`)

**최신 항목** (2026-06-25, 368차):

**최신 항목** (2026-06-25, 367차):
- **Q712 deepen** — **환불 수수료 full-stack** — **`RefundRecordModal`** policy·preview · §5-10 (`cadd74a`)

**최신 항목** (2026-06-25, 366차):
- **Q705 deepen** — **목욕 FE full-stack** — **`BathingScheduleIndicator27Panel`** · **전·후 관찰 폼** (`3d7f13b`) · §5-26
- **Q712** — **7-9 KCP 환불 수수료 catalog** — Swagger preview · §5-10 (`2adae59`)

**최신 항목** (2026-06-24, 349차):
- **Q692** — **발송 API `ezcareMessageKind`** — 청구·보호자 서류 crosswalk (`ef8bb4e`)
- **§4-6·§4-7-3** — **본인부담 안내·급여제공·인권보호** 알림톡 라벨 (`5a6d42c`)

**최신 항목** (2026-06-24, 348차):
- **Q691** — **직원 접속키 SMS** — **`POST …/staff/notifications/staff-access-key`** · catalog **6/6** (`1d5d441`)
- **§4-7-3·§4-7-4** — **GuardianDocumentNotifyPanel** 일정표-수급자 · **StaffNotificationDispatchPanel** 일정표-직원·접속키 (`9c25d44`)

**최신 항목** (2026-06-24, 347차):
- **Q594** — **G21 NHIS 비교 갭** — 지점 대시보드 통계 위젯 — 공단 일정 미등록/불일치 통계
- **Q595** — **G15 카카오 API 잔여** — HQ 관리자 대시보드 — 배차 API 호출량 모니터링
- **Q551** — **보호자 인증 blocker 분리** — guardian-credentials-missing vs default
- **Q550** — **수동 배차 개선** — 이전 배차 불러오기 · 희망 시각 경고

**사용 시나리오**:
1. 현금 수납 입력 → 자동 표시 **발급 Modal**에서 NTS 발급번호 입력 (Q531)
2. 아침 대시보드에서 **「발급 지연」** 1건 이상 → **우선 처리** (Q532)
3. 작년분 청구 발급 시 **warning Alert** 확인 (Q533)
4. HQ 관리자 → **`/billing/cash-receipts`** 전 지점 미발급·지연 한눈에 확인 (Q533)
5. **G21 지점** → 대시보드 **「공단 일정 불일치」** StatCard로 미등록 방문 확인 (Q594)

**관련 링크**: FAQ.md Q530–Q535·Q594–Q597 · API_SPEC G-CASH-RECEIPT-LOG·G21 dashboard · ADMIN_GUIDE §1-4·§10-4

---

## 3. 센터 운영/IT 담당 (통합 관리자·시스템 관리자)

### 🛠️ **ADMIN_GUIDE.md** — 플랫폼·계정·기술 관리

**대상**: 통합 관리자(`hq_admin`), 시스템 관리자(`sysadmin`)

**포함 내용**:
- **계정 관리**: 직원 계정 생성·역할 배정, 비밀번호 초기화
- **지점 관리**: 다지점 설정, 지점별 관리자 배정
- **청구·정산 설정**:
  - 수가표 관리 (등급별·연도별, **G9-COG 인지지원 5칸** + 표준 25칸)
  - 본인부담률 설정 (4구분: GENERAL/REDUCED_40/REDUCED_60/MEDICAID)
  - 청구시작 기준금액(G33) 설정 (선납/미납 반영)
  - NHIS 엑셀 import & reconciliation
- **기술 설정**: 백업, 감사 로그, API 키, LDAP 연동
- **보안 정책**: 세션 타임아웃, IP 화이트리스트, 로그인 이력
- **V166 DB 스키마**: `ltc_grade`, `grievance_counseling_records`, `case_management_records` 등

**최신 항목** (2026-06-25, 369차):
- **Q709·Q710** — **7-5 catalog FE** · **G16 parity panel** — §10-14 · G16 섹션 (`5914b2f`)
- **Q713 deepen** — **`enforce-bootstrap-readiness`** — live E2E harness checklist (`9f67954`)

**최신 항목** (2026-06-21, 290차):
- **G21 NHIS 비교** — 대시보드 widget · 공단 일정 미등록/불일치 통계 (Q594)
- **G15 Kakao quota** — HQ 대시보드 widget · API 호출량 모니터링 (Q595)
- **G32 사례관리** — 보호자별 의견 기록 · 다중 선택 · V165 (Q520)
- **live E2E bootstrap blocker** — `-not-ready` only · detail로 root cause · health·probe 동기화 (Q631, supersedes Q596 `-error` codes)

**운영 체크리스트**:
1. 신규 Tenant 개통 → `platform_admin` 역할 필요 (별도)
2. 첫 `hq_admin` 계정 발급 후 지점·수가표 설정 → ADMIN_GUIDE §1–§3
3. 월말 청구 전 NHIS import & reconciliation → ADMIN_GUIDE §6-3·FAQ Q264
4. 현금 수납 입력 후 **현금영수증 발급 이력 등록** → `/billing/cash-receipts` (Q530·Q531)
5. 아침 대시보드 **「발급 지연」** 확인 (Q532)

**관련 링크**: FAQ Q530–Q533 · API_SPEC G-CASH-RECEIPT-LOG·G32 · DEPLOYMENT_GUIDE §1-3

---

## 4. 자주 묻는 질문 & 빠른 답변

### ❓ **FAQ.md** — Q&A 색인 (590+ 항목)

**대상**: 모든 사용자 (현장·운영·기술·플랫폼)

**구성**:
- **§1–§10**: 서비스 개요, 계정, 역할, 기능별 FAQ
- **§11–§20**: 청구·정산, 공단·NHIS, 보호자, 배차, 청구 리포트 등
- **§21+**: 최신 기능 (인지지원·CMS·고충상담·HR lifecycle·G21 NHIS·G15 배차·G32 사례관리·G42 민원상담·G-SMS 템플릿 카탈로그 등)

**최신 엔트리** (2026-06-25, 369차):
- **Q709 deepen**: **7-5 provider-catalog FE wire** — **`EasyPayProviderCatalogPanel`** (`5914b2f`)
- **Q710 deepen**: **G16 parity panel mount** — **`TransportParityRulesPanel`** (`5914b2f`)
- **Q713 deepen**: **bootstrap readiness enforcement** — **`LIVE_E2E_ENFORCE_BOOTSTRAP_READINESS`** (`9f67954`)

**최신 엔트리** (2026-06-25, 368차):
- **Q712 deepen**: **`feePolicyCode` `@Pattern` validation** — invalid code **`400`** (`79725eb`)
- **Q713**: **QA-B95 effective operation readiness** — auth recovery 후 **`liveE2eEffectiveOperationReady`** (`e070c45`)

**최신 엔트리** (2026-06-25, 367차):
- **Q712 deepen**: **7-9 refund fee full-stack** — **`RefundRecordModal`** + **`feePolicyCode`** validation (`cadd74a`·`aeecc1b`)

**최신 엔트리** (2026-06-25, 366차):
- **Q712**: **7-9 copay refund fee catalog** — KCP 3.3%/500원 · preview API (`2adae59`)
- **Q705 deepen**: **목욕 전·후 관찰·지표27** — FE full-stack closure (`3d7f13b`)

**최신 엔트리** (2026-06-24, 349차):
- **Q692**: **`ezcareMessageKind`** — 발송 API 응답 crosswalk (`ef8bb4e`)
- **Q686·Q690 갱신**: **`dispatchReady` 채널 자격** — PF ID·SMS sender (`fed6f1f`)
- **message_kind 11·13·19**: UI 라벨 ezCare parity (`5a6d42c`)

**최신 엔트리** (2026-06-24, 348차):
- **Q691**: **STAFF_ACCESS_KEY** — 직원 접속키 SMS API·UI (`1d5d441`/`9c25d44`)
- **Q687·Q689 갱신**: **message_kind 12·21** — 이용자·직원 상세 발송 UI (`9c25d44`)
- **Q686 갱신**: catalog **6/6 dispatchImplemented** closure

**최신 엔트리** (2026-06-24, 347차):
- **Q613**: **G-ATTENDANCE-STATS contract** — `/attendance/stats` · `GET /attendance/stats/monthly?from=&to=` vs FE `yearMonth`/`dailyRates` 갭
- **Q612**: **G-STAFF-WORK-ATTENDANCE full-stack** — `/staff/attendance` · `GET/POST /staff/work-attendance*` (케어포 8-4)
- **Q589**: **정정** — 직원 출퇴근 vs 이용자 출석 API 분리·실측 API 경로 반영

**이전 엔트리** (2026-06-21, 297차):
- **Q611**: **UXD-151 mobile capture CSS** — `.ds-btn` 전폭 버튼·FE-16 회귀 해소
- **Q608**: **모바일 HR 촬영** — `StaffDocumentRepositoryPanel` mobile capture (UXD-151 deepen)

**이전 엔트리** (2026-06-21, 296차):
- **Q610**: **Vitest serial pool** — OOM/hang 완화·flock·`vitestConfig.test.js` (QA-B222)
- **Q609**: **G-ATTENDANCE-ROSTER-STATUS full-stack** — `GET /attendance` + **`AttendancePage` FE wire** (closure)
- **Q94**: **출석 roster closure** — 미처리 행·입소·결석 버튼 (갱신)
- **Q590**: **Must 갭: QR 생성 payload·이미지** — coder 백로그

**이전 엔트리** (2026-06-21, 295차):
- **Q607**: **중복 SMS 자동 독려기록 guard**

**사용 팁**:
- 현금영수증 관련 → Q530–Q535 참고
- G32 사례관리 관련 → Q516–Q523 참고
- G21 NHIS 비교 → Q594 참고
- G15 배차 및 Kakao → Q595 참고
- 기능 찾기 → Ctrl+F로 검색 (예: "CASH", "attendee", "대시보드", "NHIS", "Kakao")
- "P2 Planned" / "P3 out-of-scope" = ROADMAP.md 참고

**최근 엔트리 (2026-06-21, 290차)** — Q594–Q597 신규 추가·Q587–Q590 갱신·"Must 갭" 명시

---

## 5. 기술 정보 & 설계

### 📋 **REQUIREMENTS.md** — 요구사항 명세 (기획·설계 문서)

**대상**: 기획자, 개발자, QA

**포함 내용**:
- 프로젝트 개요, 기술 스택, 사업 모델
- 7개 역할 정의 & RBAC 규칙
- 기능 요구사항 (이용자·출석·건강·청구·배차 등)
- MVP v1 범위, 로드맵 (v2, v3, v3.1)
- 벤치마킹 (케어포·이지케어·엔젤·공단)

**관련 링크**: `docs/planning/FLOWCHART.md` · `docs/technical/API_SPEC.md` · `docs/planning/USER_STORIES.md`

---

### 🏗️ **CHANGELOG.md** — 변경 기록 (사람용)

**대상**: 운영·기획 담당자 — 에이전트가 무엇을 했는지, 화면에 무엇이 바뀌었는지

**구성**:
- **최근 7일 요약** + **날짜별 카드** (에이전트 축약명 · 한 일 · 내 화면/업무에 영향 · 상태)
- 3개월 지난 날짜는 삭제 (아카이브 없음)
- 기술 상세는 각 카드의 「자세히」만

---

## 6. 문서 상태 & 구현 진행도

### 현재 상태 (2026-06-26, 377차, develop HEAD `d06e3f1`/`4bbd54a`, V1–V180)

| 문서 | 상태 | 마지막 갱신 | 커버리지 |
|------|------|-----------|---------|
| **USER_MANUAL.md** | ✅ 현행 | 2026-06-26 (377차) | MVP Must full-stack · **8-2 근무일정표** · M5 program reports · baseline sync |
| **FAQ.md** | ✅ 현행 | 2026-06-26 (377차) | 700+ Q&A · **Q722 recovered-auth hint · Q719·Q720·Q721 · Q713 deepen** |
| **ADMIN_GUIDE.md** | ✅ 현행 | 2026-06-26 (377차) | live E2E harness Q722 · **§6-2-21 근무일정표** · V180 · M5 reports API |
| **DEPLOYMENT_GUIDE.md** | ✅ 현행 | 2026-06-26 (377차) | §1-4 Q722 smoke · §11-3 recovered-auth hint · Must API smoke |
| **CHANGELOG.md** | ✅ 현행 | 2026-06-26 | 날짜별 카드 형식 (에이전트 작업 일지) |
| **README.md** (본 문서) | ✅ 현행 | 2026-06-26 (377차) | 문서 네비게이션 · 역할별 가이드 · 최신 진행도 |

---

### 구현 커버리지

| 영역 | 상태 | 비고 |
|------|------|------|
| **백엔드 API** | Must + V180 ✅ | @ `d06e3f1` · **QA-B95 recovered-auth hint ✅** · **G-REPORT-DENSITY M5 reports+** · BE Test **271 suites** |
| **데이터베이스** | V1–V180 | V180 program group integrity · V179 프로그램 그룹·멤버십 · V178 CMS·목욕 CHECK |
| **프론트엔드** | 118 route · 93 page | @ `4bbd54a` · **StaffMonthlySchedulePage** · **ProgramReportsPage** · FE test **479+** |
| **문서화** | Must 갭 0 | **P2**: 5-9 그룹 CRUD UI · program reports FE `branchId` · 7-5 live PG · M6 safety |

---

## 7. 로드맵 & 다음 단계

### v1.2.1 현황 (2026-06-25)

**완료**:
- ✅ M7 본인부담 **7-4 CMS 5/5** · **7-5 catalog FE** · **7-9 refund fee full-stack**
- ✅ US-O01 목욕 **평가지표 27 FE wire**
- ✅ G16 NHIS #44 **parity panel mount**
- ✅ merge gate **802** · cross-stream **SYNCED**

**P2 Planned** (이후 버전):
- **7-5 live PG** — 실제 카드·카카오페이 벤더 연동 (현재 stub)
- **J03 Solapi live dispatch** — 알림톡·SMS 실발송
- **M6 6-2~6-4 `/safety/*`** — 안전점검 서브폼
- **L03 간호급여 잔여 5 leaf**
- **G34 SMS live OTP** · **G-Payroll** (v3)

**자세히**: [ROADMAP.md](../planning/ROADMAP.md) 참고

---

## [TWR] 310차 — live E2E bootstrap blocker normalize & FAQ Q631 (2026-06-22)

**배경**: develop HEAD baseline (**BE `24d25f1`** / FE `fdc135b` carry) — BE **+1 commit** since 309차. **live E2E bootstrap blocker reporting normalize** (QA-B95).

**310차 문서 갱신**:

| Q번 | 기능 | 상태 | 변경 |
|-----|------|------|------|
| **Q631** | **bootstrap blocker normalize** | **✅ BE** | `-error`/`bootstrap-error` 제거 · `-not-ready` only · detail로 root cause (`24d25f1`) |
| **Q596** | **derived blocker suppression** | **갱신** | Q631과 병기 — triage 표 정정 |
| **Q448** | **bootstrap not-ready vs error** | **갱신** | blocker/error 구분 → **status detail** 기준 |

**sysadmin·DevOps 다음 액션**:
1. staging `./scripts/run-live-e2e.sh` — probe **`operationBlockers`** 에 `-error` 코드 **없음** 확인
2. bootstrap 실패 triage — **`liveE2eStatusDetail`** · **`liveE2eGuardianStatusDetail`** 우선

---

## [TWR] 307차 — US-D03 이용자 상세 출석 탭 FE wire & FAQ Q628 (2026-06-22)

**배경**: develop HEAD baseline (`9db0bbb`/`d058e43`) — FE **+1 commit** since 306차. **US-D03 client detail attendance tab** full-stack closure.

**307차 문서 갱신**:

| Q번 | 기능 | 상태 | 변경 |
|-----|------|------|------|
| **Q628** | **이용자 상세 출석 탭** (`/clients/:id`) | **✅ BE+FE** | `fetchClientAttendanceHistoryApi` · `GET /clients/{id}/attendance` (`d058e43`) |
| **Q102** | **건강·출석·청구 탭** | **출석 ✅ closure** | 건강·청구 갭 잔존 |

**coder 다음 액션** (우선순위순):
1. **G-CASH-RECEIPT-NTS-API** P3 · **L03_M15 말기 돌봄** · **7-5 live PG**
2. **보호자 QR 카메라 스캔 UI** P3 · **직원 NFC/MOBILE 단말** P3

---

## [TWR] 304차 — 청구 필터 full-stack·직원 퇴근 guard & FAQ Q622·Q623 (2026-06-22)

**배경**: develop HEAD baseline (`fd0a3b3`/`77b1ea8`) — **BNK-493 후속** 반영. **G-BILLING-REPORT-FILTER-PERSISTENCE FE wire closure** 및 **Must 갭 1건**(QR 이미지)으로 축소.

**304차 문서 갱신**:

| Q번 | 기능 | 상태 | 변경 |
|-----|------|------|------|
| **Q618·Q621** | **청구 필터 저장** | **✅ BE+FE** | `BillingReportPage` hydrate·`saveBillingReportFilterApi` (`77b1ea8`) |
| **Q623** | **필터 autosave read-scope·UXD-152** | **✅ BE+FE** | HQ 타 지점 대장 403 방지 (`fd0a3b3`) · a11y (`df7f308`) |
| **Q622** | **직원 퇴근 guard** | **✅ BE** | checkout-before-checkin (`35e6c52`) |
| **Q616** | **QR 생성·다운로드** | **API ✅ · FE 갭** | *(Must 유일 잔존)* |

**coder 다음 액션** (우선순위순):
1. **QR 이미지 생성** — base64 PNG 렌더 · 다운로드 · 모바일 스캔 테스트 (Q616)
2. **G-CASH-RECEIPT-NTS-API** P3 · **L03_M15 말기 돌봄** · **7-5 live PG**

---

## [TWR] 303차 — 출석 통계 full-stack·청구 필터 BE & FAQ Q621 (2026-06-22) [이력]

**배경**: develop HEAD baseline (`6be0c79`/`dffd726`) 단계에서 **BNK-493** 반영 — **출석 통계 contract 정합 full-stack closure** 및 **청구 대장 필터 BE auto-save** 추가. **미해결 Must 갭 2건**으로 축소.

**303차 문서 갱신**:

| Q번 | 기능 | 상태 | 변경 |
|-----|------|------|------|
| **Q615·Q613·Q106** | **출석 통계** (`/attendance/stats`) | **✅ BE+FE** | `monthlyAttendanceStats.js` · StatCard·6개월 추이 (`dffd726`) |
| **Q618·Q621** | **청구 필터 저장** | **△ BE ✅ · FE bootstrap ❌** | V170 `billing_report_filters` · `GET/PUT /reports/filters` (`479995e`) |
| **Q616** | **QR 생성·다운로드** | **API ✅ · FE 갭** | *(변경 없음)* |
| **Q617** | **결석 처리** | **✅ FE+BE** | `AttendanceAbsentModal` · `markAbsentApi` contract 정정 (`dffd726`) |
| **Q619·Q620** | **직원 출퇴근·당일 roster** | **✅ 완료** | *(carry)* |

**coder 다음 액션** (우선순위순):
1. **QR 이미지 생성** — base64 PNG 렌더 · 다운로드 · 모바일 스캔 테스트 (Q616)
2. **청구 필터 FE bootstrap** — `BillingReportPage` 마운트 시 `GET /reports/filters` (Q621)
3. **출석 통계 P3** — 일별·이용자별 breakdown API (선택)

---

## [TWR] 302차 — 미해결 Must API 갭 정리 & FAQ Q615–Q620 신규 추가 (2026-06-22) [이력]

**배경**: develop HEAD baseline (`a6eb8b7`/`5fd468b`) 단계에서 **4개 Must 기능**이 **API 또는 FE 구현 갭** 상태입니다. 현장 인수 전 **우선순위·상태·우회 방법**을 명시하여 **운영 중단 위험** 최소화.

**신규 FAQ 추가** — Q615–Q620:

| Q번 | 기능 | 상태 | 문서 이슈 | 현장 우회 |
|-----|------|------|----------|---------|
| **Q615** | **출석 통계** (`/attendance/stats`) | **API ✅** · **FE contract 갭** | `yearMonth` ↔ `from/to` 필드 정합 필요 · coder 체크리스트 | 대시보드·당일 roster로 현황 확인 (낮음) |
| **Q616** | **QR 생성·다운로드** | **API ✅** · **FE 갭** | `qrcode.js` 렌더·다운로드 미구현 | 수기 체크인·B방식 QR 스캔 (낮음) |
| **Q617** | **결석 처리 버튼** | **API ✅** · **FE 갭** | `/attendance` 모달·버튼 미구현 · UXD-152 미확정 | check-out 후 사유 기록 (낮음) |
| **Q618** | **청구 필터 저장 API** | **FE ✅** · **BE 갭** | 저장 API 미구현 · Swagger 우회 가능 | 매월 수동 재입력 (중간) |
| **Q619** | **직원 출퇴근 (8-4)** | **✅ 완료** | Q612 반영 완료 · **V169** · **`/staff/attendance`** 정상 | 정상 동작 |
| **Q620** | **당일 출석 roster (Q609)** | **✅ 완료** | **`/attendance`** · **`fetchAttendanceApi` 단일 호출** | 정상 동작 |

**coder 다음 액션** (우선순위순):
1. **출석 통계 FE wire** — `GET /api/v1/attendance/stats/monthly` 응답 필드 정합 · 차트/테이블 렌더
2. **QR 이미지 생성** — base64 PNG 렌더 · 다운로드 · 모바일 스캔 테스트
3. **결석 버튼 UX** — UXD-152 명세 후 모달 구현
4. **청구 필터 저장 API** — `BillingReportFilterService` 구현 · `GET /billing/reports/filters?month=YYYY-MM`

---

## 8. 추가 자료

### 기획·설계 문서
- **REQUIREMENTS.md** — 요구사항 전문
- **FLOWCHART.md** — 화면 흐름도
- **USER_STORIES.md** — Epic별 사용자 스토리
- **PLAN_NOTES.md** — 설계 의사결정 이력

### 기술 문서
- **API_SPEC.md** — REST API 상세 명세
- **ERD.md** — 데이터베이스 엔티티 관계도

### 벤치마킹·연구
- **BENCHMARK_REPORT.md** — 경쟁사 분석
- **COMPETITOR_MATRIX.md** — 케어포·이지케어·엔젤 기능 비교

---

## 🎯 도움말

**Q. 어느 문서를 먼저 읽어야 하나요?**

| 상황 | 추천 순서 |
|------|---------|
| 신규 센터 도입 | DEPLOYMENT_GUIDE.md → USER_MANUAL.md → FAQ.md |
| 센터 관리자 | ADMIN_GUIDE.md → USER_MANUAL.md (§8) → FAQ.md (§3–§8) |
| 현장 직원 | USER_MANUAL.md → FAQ.md |
| 개발자 | REQUIREMENTS.md → API_SPEC.md → DEPLOYMENT_GUIDE.md |
| 기능 찾기 | FAQ.md Ctrl+F 검색 |

**Q. "P2 Planned"가 무엇인가요?**

아직 구현되지 않은 예정 기능입니다. 다음 버전에서 추가될 예정입니다. 자세히는 각 문서의 **P2 섹션** 또는 FAQ.md에서 검색하세요.

**Q. 최신 정보는 어디서 확인하나요?**

- **구현 진전**: CHANGELOG.md 「최근 7일 요약」
- **개발 상태**: 각 문서 최상단 메타 (`updated=` 날짜 확인)
- **의사결정 이력**: PLAN_NOTES.md

---

## 문서 소유 & 연락처

| 역할 | 담당자 | 역할 | 채널 |
|------|--------|-----|------|
| 문서 작성·갱신 | TWR (tech_writer) | 모든 ops 문서 | GitHub Issues · PLAN_NOTES.md |
| 기획·설계 | PLN (planner) | REQUIREMENTS.md, ROADMAP.md | GitHub Issues · 의사결정 기록 |
| 코드·API | COD (coder) | API_SPEC.md, 구현 상태 | 커밋 메시지 · 테스트 결과 |
| 운영·배포 | TSR (tester/operator) | DEPLOYMENT_GUIDE.md 재검증 | 배포 결과 · 로그 |

---

*Last updated: 2026-06-13 by tech_writer (TWR) — ogada v1 개발 중*
