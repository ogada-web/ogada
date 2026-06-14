<!-- doc:owner=TWR doc:audience=PLN,COD updated=2026-06-15T14:00:00+09:00 -->
# ogada 관리자 가이드 (ops/ADMIN_GUIDE.md)

> **작성**: tech_writer 에이전트  
> **최초 작성일**: 2026-06-05  
> **최종 갱신**: 2026-06-15 (164차 — v1.3-B 배차 FE wire·L03_M01 간호급여 제공기록 BE · BE `9bd1660`/FE `edfba7f` · Vitest 1274/1274 · `mvn test` 1131/1131 PASS)  
> **상태**: 초안 (Draft)  
> **대상 독자**: **ogada 플랫폼 운영자** (`platform_admin`), **고객 센터 IT·시스템 관리자** (`sysadmin`)  
> **기준 문서**: `docs/planning/REQUIREMENTS.md`, `docs/technical/API_SPEC.md`, `docs/planning/FLOWCHART.md`, `docs/ops/DATA_RETENTION_POLICY.md`  
> **기술 스택**: Java Spring Boot 3.x + React (Vite SPA) + PostgreSQL

---

## 1. 이 가이드에 대하여

### 1-1. 목적

ogada는 전국 주간보호센터·요양기관을 위한 **B2B SaaS 멀티테넌트** 운영 관리 시스템입니다.  
이 문서는 **시스템·플랫폼 관리자**가 신규 고객 온보딩, 테넌트 기술 설정, 백업·감사, 보안 키 관리, 장애 대응을 수행할 때 필요한 절차와 권한 경계를 설명합니다.

### 1-2. 문서 범위

| 포함 | 제외 |
|------|------|
| `platform_admin` — 신규 Tenant 등록·첫 `hq_admin` 발급 | 현장 일상 업무 (→ `USER_MANUAL.md`) |
| `sysadmin` — 기술 설정·백업·감사 로그 | 인프라 배포·CI/CD 상세 (→ `DEPLOYMENT_GUIDE.md`) |
| 역할·테넌트 격리·PII 암호화 정책 | 식단·일정 등록 API·알림톡 live 연동 (후속) |
| 계정·권한 관리 개요 (`hq_admin` 협업) | 공단 포털 직접 전송 (후속) · **CMS live FCMS** (stub Fixed, Q206–Q208) · **7-5 live PG** (stub Fixed, Q326) |

### 1-3. 관리자 역할 구분

ogada에는 **두 종류의「시스템 관리자」**가 있습니다. 혼동을 피하기 위해 역할·데이터 범위를 먼저 구분합니다.

| 역할 | 코드 | 소속 | 홈 화면 | 데이터 범위 | 주요 책임 |
|------|------|------|---------|------------|----------|
| **플랫폼 관리자** | `platform_admin` | ogada 내부 | `/platform` | 전국 Tenant **메타데이터** | 신규 고객 센터 등록, 첫 `hq_admin` 발급, 요금제·활성 상태 |
| **시스템 관리자** | `sysadmin` | 고객 센터(Tenant) | `/settings` | **자기 Tenant** 기술 영역 | 백업·감사 로그·기술 설정, 보안 모니터링 |
| **통합 관리자** | `hq_admin` | 고객 센터(Tenant) | `/dashboard/hq` | 자기 Tenant **운영 전반** | 지점·직원·이용자·청구 (본 가이드 §6 참고) |

**할 수 있는 일 / 없는 일 (요약)**

| 행동 | `platform_admin` | `sysadmin` | `hq_admin` |
|------|:----------------:|:----------:|:----------:|
| 새 센터 법인(Tenant) 등록 | ✅ | ❌ | ❌ |
| 전국 가입 고객사 목록 조회 | ✅ | ❌ | ❌ |
| 자기 회사 백업·기술 설정 | ❌ | ✅ | ❌ |
| 자기 회사 이용자·출석 CRUD | ❌ | ❌ | ✅ (지점 스코프) |
| 다른 센터 이용자 데이터 조회 | ❌ | ❌ | ❌ |

> **비유**: `platform_admin`은 통신사 매장의 **회선 개통** 담당, `sysadmin`은 고객사 IT의 **내부 시스템·백업** 담당, `hq_admin`은 센터 **운영 총괄** 담당입니다. (REQUIREMENTS §1-3)

### 1-4. 구현 상태 안내 (2026-06-15 develop HEAD `9bd1660` / frontend `edfba7f`, 164차)

| 영역 | 상태 | 비고 |
|------|------|------|
| **v1.3-B transport suggest-run FE (Q347, BNK-214)** | **BE·FE Fixed** | **`TransportSuggestPanel`**·**`BranchTransportSettingsPanel`** on **`TransportPage`** — **`suggestTransportRunsApi`**·**`fetchBranchTransportSettingsApi`**·**`updateBranchTransportSettingsApi`** (`2ffe59f`) · BE **`POST /transport/runs/suggest`**·**`GET/PUT /transport/settings`** (`db94a65`) |
| **L03_M01 nursing service provision (Q348, BNK-215)** | **BE Fixed · FE P2** | **V123** `nursing_service_records` (`9bd1660`) · **`NursingServiceRecordController`** 3 endpoints · **`NursingServiceRecordPilotServiceFlowE2eTest`** · **P2**: FE wire |
| **US-UX-05 SideNav manual expand preserve (Q331)** | **FE Fixed** | **`SideNav`** — route 변경 시 **수동 펼침 유지** (`edfba7f`) · **`SideNav.test`** |
| **v1.3-B transport suggest-run (Q347, BNK-212)** | **BE Fixed** | **`POST /transport/runs/suggest`** — **`TransportSuggestService`**·**`TransportRunOptimizer`**(OR-Tools VRP) · **V120**·**V122** · **≤10회/지점/일** · **`hq_admin` only** (`db94a65`) |
| **G21 batch-confirm date guard (Q330, BNK-213)** | **BE Fixed** | **`VisitService.batchConfirm`** — **`fromDate`·`toDate` 필수** — **`BATCH_CONFIRM_DATE_REQUIRED_MESSAGE`** (`230659a`) · **`VisitServiceTest`** |
| **L03_M14 weight form UX (Q343, UXD)** | **FE Fixed** | **`NursingWeightRecordForm`** — 체중 **`Field help`** · **`aria-describedby`** 정합 (`8d00f5d`) |
| **L03_M13 oral care check (Q345, BNK-209)** | **BE·FE Fixed** | **V118** `nursing_oral_care_checks` (`3540b4f`/`090b2d7`) · **`NursingOralCareCheckController`** 3 endpoints · **future check-date guard** · **`NursingOralCareCheckPilotServiceFlowE2eTest`** · FE **`NursingOralCareCheckPage`**·**`NursingOralCareCheckForm`**·**`nursingOralCareCheckServices`** (`bb3dee8`/`97108f2`) · **`NursingContextNav`** 8탭 · **`NursingOralCareCheckPage.test`**·**`nursingOralCareCheckLiveApi.e2e.test.js`** |
| **L03_M04 emergency situation record (Q346, BNK-211)** | **BE·FE Fixed** | **V119** `nursing_emergency_records` (`81bca68`/`090b2d7`) · **`NursingEmergencyRecordController`** 3 endpoints · **injectable `Clock` future-date guard** · **`NursingEmergencyRecordPilotServiceFlowE2eTest`** · FE **`NursingEmergencyRecordPage`**·**`NursingEmergencyRecordForm`** (`97108f2`) · **`NursingEmergencyRecordPage.test`**·**`nursingEmergencyRecordLiveApi.e2e.test.js`** |
| **L03_M11 integrated vital check (Q340~Q342, BNK-207)** | **BE·FE Fixed** | **V115** `nursing_vital_checks` · **`NursingVitalCheckController`** 3 endpoints · **future check-date guard** (`090b2d7`) · FE **`NursingContextNav`** 8탭 |
| **L03_M14 weight management (Q343~Q344, BNK-207~209)** | **BE·FE Fixed** | **V116** `nursing_weight_records` · **`NursingWeightRecordController`** 3 endpoints · **future measure-date guard** · FE **`NursingWeightRecordPage`**·**`NursingWeightRecordForm`** (`8a8fe98`/`97108f2`) |
| **G-NURSING-PRESSURE-ULCER (Q336~Q339, BNK-203~204, US-O03)** | **BE·FE Fixed** | **V114** `pressure_ulcer_assessments`·`pressure_ulcer_care_records` (`edda491`) · **`PressureUlcerController`** 9 endpoints · **`PressureUlcerPilotServiceFlowE2eTest`** 4-step (`24a1c5c`) · FE **`PressureUlcerPage`** 4탭 · **`pressureUlcerServices`** (`024e720`) · **P2**: 나머지 L03 leaf · live E2E |
| **G17b cognitive activity skip reason (Q333~Q335, BNK-198~203)** | **BE·FE Fixed** | **V112** `functional_recovery_plans.cognitive_activity_*` (`6b7e6cb`) · **V113** `program_participations.skip_reason` (`ba7d84f`) · **`ProgramService.resolveSkipReason`** · ABSENT satisfaction 가드 (`3bd6a43`) · FE **`ProgramParticipationForm`**·**`ProgramsPage`** skipReason 표 (`c26cfa7`/`487416d`) · **`FunctionalRecoveryPage`** cognitive switch+reason (`c26cfa7`) · **`ProgramServiceTest`**·**`pilotPageFlows`** G17b E2E |
| **G21 batch-confirm (BNK-197~198·213, Q330)** | **BE·FE Partial+ Fixed** | **`GET /visits/confirm-readiness`** · **`POST /visits/batch-confirm`** — NHIS·변경이력 ack gate (`0b807d8`·`c22a5dc`) · **`fromDate`/`toDate` 필수** (`230659a`) · FE **`VisitBatchConfirmPanel`**·**UXD-102 a11y** (`d5ff3f8`) · **`VisitServiceTest`**·**`RoleBasedControllerAccessTest$VisitAccess`** · **P2**: live E2E |
| **US-UX-05 SideNav toggle (Q331, BNK-198)** | **FE Fixed** | **`SideNav`** — **`buildNavGroupExpandedState`** — 활성 route 부모 그룹만 초기 펼침 · route 변경 재계산 (`4ba7ea6`) · **`SideNav.test`** |
| **G42 anonymous box intake (Q305, BNK-198)** | **FE Partial+ Fixed** | **`ComplaintConsultationForm`** — **`ANONYMOUS_BOX`** 시 대상 필드 숨김 · **`targetType=OTHER`·`targetName=익명`** (`8a8b930`) · **P2**: 별도 라우트·PDF |
| **V111 easy-pay guardian link (BNK-196, Q332)** | **BE Fixed** | **`trg_easy_pay_requests_validate_guardian_link`** — guardian role·client link (`dbecd72`) |
| **J03 NotificationQuietHoursPolicy (BNK-195, Q332)** | **BE Fixed** | **`NotificationQuietHoursPolicy`** — dispatch·readiness·manual billing notify **단일 정책** (`a057739`) |
| **G2/7-5 copay easy payment (BNK-189~193, Q326~Q328)** | **BE·FE Fixed (stub PG)** | **`EasyPayController`** — **`POST/GET …/payment`** + **alias `/claims/{claimId}`** (`8f9ad0c`) · **provider `Locale.ROOT`·NFKC alias** (`82054f1`·`745a2f6`·`7ec7cd4`) · **V110 integrity** · **US-L06 a11y** · **`mvn test` 1060/1060** |
| **J03 quiet-hours billing UI (BNK-193, Q329)** | **BE·FE Fixed** | **`NotificationService.isQuietHoursAt`** — **22:00~08:00 KST** · **`NotificationServiceTest`** boundary (`328874d`·`9a4ab8e`) · FE **`BillingDetailPage`·`OverduePage`** 버튼 비활성 (`111f056`) |
| **G41/G41b staff training logs (8-7, Q321·Q325, BNK-184~188)** | **BE·FE Fixed** | **`GET …/compliance`** G41b 3종 `*AnnualMet` (`0f11158`) · **V107** annual no-half (`ee42e5d`) · FE **BE compliance wire** (`38d24b6`) · **신규 7일 지점 스코프·earliest date** (`299d21f`·`32f87f1`) |
| **G30 integrated monitoring checklist (BNK-181, Q320)** | **BE·FE Fixed** | **`GET /compliance/monitoring/checklist`** — FAQ21838~21842 **8문항** · **`MonitoringIntegratedChecklistPanel`** (`b1dfd34`·`574bd08`) · **`MonitoringPilotServiceFlowE2eTest`** |
| **G34-QUAL team lead qualification compliance (Q319, BNK-180~182)** | **BE·FE Fixed** | **`GET /staff/team-lead-qualification/compliance`** (`9a8bd2a`) · **`TeamLeadQualificationCompliancePanel`** (`574bd08`) · create/update **`422` guard** (`726b3de`) · **`TeamLeadQualificationPilotServiceFlowE2eTest`** (`997831c`) |
| **US-S02 refresher POST compliance (Q294, `510dbd1`)** | **FE Fixed** | **`POST /staff/refresher-training/compliance`** — **`completeStaffRefresherTrainingComplianceApi`** primary write · lifecycle PATCH fallback 유지 |
| **J03 notification channel readiness UI (Q318, BNK-177)** | **BE·FE Fixed** | **`GET /notifications/channel-status`** — **`liveAlimtalkDispatchReady`·`liveEmailDispatchReady`·`quietHoursActive`** (`fffd355`·`229f84c`) · FE **`NotificationChannelReadinessPanel`** — **UXD-97** `.ds-dl-grid`·`<h3>` 섹션 제목 (`76b5ff0`) · **`/organization/settings`**·**`DashboardPage`** (`6b1258c`·`d695923`) |
| **US-R02 staff status report profile pagination (8-12, Q315)** | **FE Fixed** | **`StaffStatusReportPage`** — **`ensureStaffProfiles`** page-through `GET /users` size=200 (`ff173af`) |
| **G34-QUAL team lead qualification gate (Q319)** | **BE·FE Fixed** | BE **`TeamLeadQualificationCompliance`**·**`requireEligibleLeadCaregiver`** (`726b3de`) · FE **`TeamLeadQualificationCompliancePanel`**·**`teamLeadQualificationCompliance.js`** (`574bd08`·`443efca`) |
| **G42 approval queue·follow-up UI (BNK-174, Q309·Q316)** | **BE·FE Partial+ Fixed** | **`ComplaintConsultationPanel`** 결재·사후관리 섹션 (`6012044`) · **`GrievanceFollowUpModal`** · follow-up API (`bcb1d9f`) · **P2**: 별도 결재함 라우트 |
| **#44 transport fee seed V103 (BNK-174, Q317)** | **BE Fixed** | **RU_3 5,230** · **RU_4 8,630** — NHIS lawImg 정본 (`39ee679`) |
| **US-R02 staff status report CSV export (8-12, Q315)** | **BE·FE Fixed** | **`GET /staff/reports/status/export`** UTF-8 BOM (`bc927f7`) · FE **`exportStaffStatusReportCsvApi`** (`488f547`) · 인쇄 안정화 (`5bba7a2`) |
| **G30 monitoring self-diagnosis·phone consultation·integrated checklist (BNK-169~171·181, Q314·Q320)** | **BE·FE Fixed** | **`MonitoringController`** — **`/compliance/monitoring/*`** · **`GET …/checklist`** · V100/V101 · **`MonitoringSelfDiagnosisPage`** · **P2**: live E2E |
| **G9-COG cognitive support fee schedule (BNK-166, Q311·Q260)** | **BE·FE Fixed** | V99·import gate·30칸 matrix · **`8bb6583`/`edd2771`** |
| **G9-COPAY-NAMING statutory labels (BNK-166 §166-3, Q313)** | **FE Fixed** | **`CopayTypeSelect`**·**`CopayRateTable`** — **`statutoryLabel`**·**`copayTypeStatutoryLabel`** — longterm 503·법 제40조 용어 병기 (`e77b7e4`) · **UXD-94** `aria-describedby` (`a5c2736`) |
| **FAQ21824 client billing lifecycle (BNK-165, Q312)** | **FE Fixed** | **`ClientFaq21824LifecyclePanel`** on **`ClientDetailPage`** **「기본정보」** — 4단 G14→G38→G21→7-x · **`faq21824Lifecycle.js`** (`58256c6`) · **P2**: 단일 wizard |
| **G-7x-1 G33 YearMonth guard (Q270)** | **BE Fixed** | **`BillingService.getClaimGenerationGuard`** — G33 **`effectiveMonth`** vs **대상 청구월 `YearMonth`** (`21eb0af`) · FE workflow는 Q310 Fixed |
| **G42 pending-approval API (BNK-161, Q309)** | **BE·FE Fixed** | **`GET /staff/grievance-counselings/pending-approval`** (`6f6094d`) · FE **결재 대기** 패널 (`6012044`) |
| **G42 follow-up API·UI (BNK-174, Q316)** | **BE·FE Fixed** | **`POST …/follow-up`** · **`GET …/follow-up/pending`** · **`GET …/follow-up/compliance`** (`bcb1d9f`) · **`GrievanceFollowUpModal`** (`6012044`) |
| **G-7x-1-guard claim generation UX (BNK-160, Q310)** | **FE Fixed** | **`ClaimGenerationGuardBanner`** — **`claimGenerationGuard.js`** — 7-2→7-1 **`LifecycleWorkflowPanel`** · G33 미정산 분기 · **`/billing/payments`·`/overdue`·`/organization/settings`** 링크 (`338c014`) |
| **US-T14 anonymous grievance masking (Q305)** | **FE Partial+ Fixed** | **`complaintSubjectDisplay`** — **`ANONYMOUS_BOX`** → **「익명」** (`4b54da5`) · **익명함 intake 폼** — 대상 필드 숨김 (`8a8b930`) · **P2**: 별도 라우트·PDF |
| **US-R02 staff status report (8-12, Q308)** | **BE·FE Partial+ Fixed** | **`StaffStatusReportPage`** — aggregated API·**BE CSV export** (`488f547`) · **P2 잔여**: 대시보드 위젯·PDF 공식 서식 |
| **G34b import-draft API (BNK-157, Q303·Q306)** | **BE Fixed** | **`GET /staff/lead-caregiver-logs/import-draft`** — **`source=needs_assessment`·`previous_month`** · **`LeadCaregiverWorkLogImportPilotServiceFlowE2eTest`** (`8487667`) · **cognitive role guard BE** (`b6ecc35`) |
| **G42 grievance counseling (BNK-161~174, Q305)** | **BE·FE Partial+ Fixed** | **`GrievanceCounselingService`** — CRUD·submit·approve·**follow-up** (`bcdc411`·`bcb1d9f`) · **FE** **`GrievanceCounselingPage`**·**`ComplaintConsultationPanel`**·**`GrievanceFollowUpModal`** (`6012044`·`892450a`) · **P2 잔여**: 익명함 전용 폼·서류함 PDF |
| **G34b lead caregiver work log clone (BNK-160, Q306)** | **BE·FE Fixed** | **`LeadCaregiverWorkLogPage`** — **「전월 일지 복제」** · **`buildPreviousMonthCloneDraft`** · **인지활동 role guard**(`COGNITIVE_EDIT_ROLES`, FE `1b5fabe`·BE `b6ecc35`) · **불러오기**(`0ce04ad`, Q303) |
| **G40b periodic risk assessment (BNK-153~154, Q302)** | **BE·FE Fixed** | **`ClientPeriodicRiskAssessmentService`** — silverangel **지표16**·FAQ21811 **반기 3종** — **`GET/PUT /clients/{clientId}/periodic-risk-assessments*`** · **`GET /clients/periodic-risk-assessments/compliance`** (`84e59d2`·V95/V96) · **FE** **`ClientPeriodicRiskAssessmentPanel`**·**`PeriodicRiskAssessmentStatusPage`**·dashboard widget (`22325f4`·`7b68f54`) · **UXD-91** **`aria-label`**(`fad6df1`) |
| **G40 admission risk assessment (BNK-150~152, Q301)** | **BE·FE Fixed** | **`ClientRiskAssessmentService`** — silverangel **지표21** 3종 — **`GET/PUT /clients/{clientId}/risk-assessments*`** · **`GET /clients/admission-risk-assessments/compliance?branchId=`** — **`ltcCertValidFrom` 이전 3종 필수** (`22d736b`·route test `686d686`) · **duplicate earliest pick**(`2589b94`) · **Flyway V93** `client_risk_assessments` · **V94** integrity(`f0752b6`) · **FE** **`ClientRiskAssessmentPanel`** on **`ClientDetailPage`** **「위험도평가」** (`328d697`) · **`DashboardPage`** **「신규입소 위험도평가 미완료」** widget (`2f5af63`) |
| **FAQ21806 onboarding compliance (US-R03, Q300)** | **BE·FE Fixed** | **`GET /staff/hr-files/onboarding-compliance`** — 7종 서류·신규교육 7일 집계 (`d4ee057`·`60789d6` batch scope) · **`StaffOnboardingCompliancePanel`** on **`StaffPage`** · **`StaffMemberOnboardingComplianceCard`** on **`StaffDetailPage`** (`4efa168`) · **Flyway V92** integrity |
| **G2 CMS enrollment cancel (US-L03, Q299)** | **BE·FE Fixed** | **`DELETE /billing/cms/enrollments/{enrollmentId}`** — **`CmsService.cancelEnrollment`** · FCMS unregister · **REQUESTED 출금 중 해지 거부** (`a34d0eb`) · **이용자별 ACTIVE·CANCELLED 이력** (`4a622ab`) · **다른 보호자 ACTIVE 중복 거부** (`72aff00`) · **`CmsPage`** 해지 Modal (`9a6fdb6`·UXD-90 `9ba4956`) · **`CmsPilotServiceFlowE2eTest`** |
| **US-R03 staff HR file hub (FAQ21806, BNK-139)** | **BE·FE Fixed** | **`StaffHrFileController`** — **`GET/POST/DELETE /staff/hr-files/users/{userId}*`** · **`GET …/{fileId}`** download (`bbb8e35`, Q298) · **8종 documentType** · **Flyway V91** · **`StaffDetailPage`** **「HR 파일함」** 탭 |
| **G2 CMS enrollment reactivation timestamp** | **BE Fixed** | **`CmsService.createEnrollment`** — **`CANCELLED`** 재등록 시 **최초 `created_at` 보존** (`fee710d`) |
| **US-R02 staff health checkup (8-10, FAQ21799)** | **BE·FE Partial Fixed** | **`StaffHealthCheckupController`** — compliance·CRUD (`f1268c6`, Q296) · **V89** · **`StaffHealthCheckupsPage`** · **`StaffHealthCheckupRecordsPanel`** on StaffDetail · **P2 잔여**: 결과통보서 **파일함**·대시보드 위젯 |
| **US-S02 staff refresher training (8-7-1, FAQ21825)** | **BE·FE Fixed** | certificate CRUD (`51477bd`, Q295) · **V88** · **`StaffRefresherTrainingPage`** · **`StaffRefresherCertificatePanel`** on StaffDetail · UXD-89 **`.ds-attachment-list*`** (`b599d8f`) |
| **G-Staff-LC staff lifecycle (US-R03, FAQ21825·FAQ21806)** | **BE·FE Partial Fixed** | **`UserService.getUser`·`updateUser`** — lifecycle (`75440bc`·Q290) · **FAQ21806 7일 신규교육** guard (`bc3c967`) · **HR 파일함 연동** (`bbb8e35`·Q298) · **compliance 집계 API+UI** (`d4ee057`·`e76ca06`·Q300) · **V86–V92** · **P2 잔여**: G-Payroll·전자서명 workflow |
| **G24 needs assessment (US-T09)** | **BE·FE Fixed** | **`ClientNeedsAssessmentService`** — **`GET/PUT /clients/{clientId}/needs-assessments*`** (`6f3315a`·`b238779`, Q286) · **`ClientNeedsAssessmentForm`** — 8항목 저장·이전 연도 비교 · **fiscal-year parsing** (`4e4bdf6`·`479e064`) · **Flyway V84/V85** · **P2 잔여**: FAQ21800 연간 리포트·지표15 자동화 |
| **G14 benefit contract attachments (US-T10)** | **BE·FE Partial Fixed** | **`ClientBenefitContractAttachmentService`** — **`GET/POST/DELETE …/benefit-contract-attachments*`** (`6f3315a`, Q285) · **`ClientBenefitContractAttachmentPanel`** — PDF/PNG ≤10MB (`2642838`) · **P2 잔여**: FAQ21805 갱신·해지·전자서명 workflow |
| **G34 lead caregiver work log (US-S01)** | **BE·FE Fixed** | **`LeadCaregiverWorkLogController`** — **`GET/POST/PATCH /staff/lead-caregiver-logs*`** · **`POST …/{logId}/sign`** (`559648f`, Q284) · **`LeadCaregiverWorkLogPage`** · **`SignLeadCaregiverWorkLogModal`** (`314b380`, Q288) · **G34b 불러오기** (`0ce04ad`, Q303) · **서명자·서명 시각 감사 열**(`8ccd287`) · **Flyway V82–V83** · **P2 잔여**: **SMS live OTP** · **FAQ21813 30일 rolling** · **K-MMSE** · **인쇄** |
| **G2 CMS / LCMS 3-method (BNK-127)** | **stub Fixed · P2 Planned** | ogada **CMS 자동이체 단일** (`/billing/cms`, Q206–Q208) · **FCMS live**·**계좌+카드+가상계좌** 다중결제 **P2** (Q291) |
| **G-UX-Autosave (BNK-127)** | **P3 Planned** | DESIGN_SYSTEM 큰폰트·터치 ✅ · **debounced autosave** ❌ (Q292) |
| **LifecycleWorkflowPanel (UX/a11y, G17/G32/G34)** | **FE Fixed** | **`FunctionalRecoveryPage`**·**`CaseManagementPage`**·**`LeadCaregiverWorkLogPage`** — **`build*LifecycleSteps`** (`c70b908`·`22bd6b7`·`6d6b426`, Q287) · **QA-B50** label dedupe (`352968b`) · **QA-B52** React key (`c8c727e`) |
| **G21 paired visit linkage guard** | **BE Fixed** | **`VisitService`** — 페어 **허용 전이만** 동기화(`6bfc745`) · 체크인/아웃 **상태 불일치 `422`** (`45b8147`) · **연결 무결성·확정 상태 가드** (`209f05d`·`b7cfc92`, Q238) · **레거시 슬롯 `hasSameVisitSlot`** (`728339e`·`588bfb1`, Q289) · **DRAFT sync `isValidPairedScheduleLink`** (`82bdbcd`) · **assignedUserId guard** (`dc48933`, Q304) · **check-in/out assigned caregiver guard** (`b459f4c`, Q307) · **레거시 `.xls` NHIS import** (`3f444a1`, Q297) · **`mvn test` 872/872** |
| **G17/G32 edit-flow pilot E2E** | **BE·FE Fixed** | **`pilotPageFlows`** · **`ProgramCompliancePilotServiceFlowE2eTest`** · **`PilotChecklistJwtE2eTest`** (`0ed781f`·`3ad2a90`·`2cd2cd8`, Q283) |
| **QA-B49 parallel compliance fallback** | **FE Fixed** | **`DashboardPage`** — 스냅샷 **누락 도메인만** compliance API **병렬 폴백** (`f72da41`, Q280) · Vitest **782건 PASS** |
| **Dashboard billing/NHIS snapshot (QA-B49)** | **BE Fixed · FE Partial** | **`BranchDashboardResponse`** — **`monthlyCapWarningCount`** 추가 · **`HqDashboardResponse`** — 전 지점 **`nhisUnmatchedCount`·`pendingReviewCount`·`overdueCount`·`monthlyCapWarningCount`** 집계 (`15b3c7e`, Q282) · FE는 NHIS·미납·월한도 **병렬 API 유지** |
| **G17/G32/G38/G39 dashboard compliance snapshot (QA-B49)** | **BE·FE Fixed** | **`BranchDashboardResponse`**·**`HqDashboardResponse`** — G17/G32/G38/G39 **준수지표 count·met 필드 전체** — **`GET /dashboard/branch`**·**`/dashboard/hq`** (`7ba18c1`·`70d76a4`, Q280) · **`DashboardPage`** 도메인별 스냅샷 우선·부분 폴백 (`8fa9f3d`, Q282) · **`DashboardServiceTest`** +163 · **`DashboardPage.test`** +2 |
| **DateInput G11/G15 (FE-16)** | **FE Fixed** | **`FeeSurchargeGuidePanel`**·**`TransportCompliancePanel`** — raw `type="date"` → **`DateInput`** (`4903173`, Q281) |
| **G17/G32 edit UI (BNK-112 FE)** | **FE Fixed** | **`FunctionalRecoveryPage`**·**`CaseManagementPage`** — 목록 **「수정」** → **`PATCH`** (`26499b3`, Q279) |
| **G39 dashboard 4-pillar (BNK-107/109)** | **FE Fixed** | **`DashboardPage`** — 지표44 gap·상태 위젯 **8종** (`8e66ae8`, Q276) · **도메인별 스냅샷 우선 로드**(Q280·Q282) |
| **G39 provision result evaluation (BNK-107/109)** | **BE·FE Fixed** | **`GET/POST/PATCH /provision-result-evaluations*`** · **`ProvisionResultEvaluationPage`** · **지표44 dashboard widgets** (`f082933`·`1c99bcd`·`8e66ae8`, Q276) · **V80/V81** |
| **G38 care-plan notification compliance (BNK-106)** | **BE·FE Fixed** | **`GET /clients/care-plan-notifications/compliance`** · **`?branchId=`** 지점 필터 (`5fd35a6`·`03211e6`) · **`CarePlanNotificationPage`** · **G38 dashboard widgets** · partial-load warning (`28c22b0`·`4b2b082`, Q277) |
| **G21 NHIS visit import validation** | **BE Fixed** | **`.xlsx` 확장자·Content-Type guard** — `text/plain` 거부 · **`application/vnd.ms-excel`**·`octet-stream` 허용 · **parameterized Content-Type strip** (`3c7b247`·`18e2b4c`·`e21c12f`, Q278) |
| **G37 grade history attachments (BNK-105/106)** | **BE·FE Fixed** | **`GET/POST/DELETE …/ltc-grade-history/{historyId}/attachments*`** · **`GradeHistoryAttachmentPanel`** (`0325d95`·`e9d1178`, Q274) · **V78** metadata · **V79** integrity (`c4b230b`) · **pilot·live E2E** · **MIME 없음/`octet-stream`일 때만** 확장자 fallback |
| **G21 visit enum normalize** | **BE Fixed** | **`scheduleKind`·`checkInMethod`** trim+uppercase — 소문자·공백 입력 허용 (`225b104`·`e8de0eb`, Q275) · **`VisitControllerRoutingTest`** |
| **G33 billing start balance (BNK-94~99)** | **BE·FE Fixed** | **1회 설정** · **1회/잠금 안내**(`BillingStartBalanceNotice`, Q273) · **청구대장·미납 OPENING_BALANCE** · **settle API+UI+reload Fixed** (`70e6191`·`359cf0c`·`eb48879`, Q270) · **claim guard G33 포함 Fixed** · **V77 integrity** (`42bc06e`) · **lock fallback Fixed** (`0ba2b68`) |
| 플랫폼·Must API | **백엔드 구현됨** | Tenant CRUD·이용자·출석·건강·청구·대시보드 |
| **US-G04 fee schedule year guard (BNK-79·BNK-166)** | **BE·FE Fixed** | **`FeeScheduleYearCoverage`** — NHIS import 전 **25칸** 완비 검증 + **인지지원 5칸 조건부 gate**(활성 `ltcGrade=0` 이용자, `8bb6583`, Q260·Q311) · **`FeeScheduleYearGuardBanner`** — 업로드 차단 (`5c0d83d`) |
| **G26 medical expense deduction (US-L04)** | **BE·FE Fixed** | **`GET …/medical-expense-deduction`** — **`CASH`·`BANK_TRANSFER`만 집계** · **`CMS`·`EASY_PAY` 제외** (Q254) · **NTS xlsx export** (`e2c2ffe`·`fd569d7`, Q258) · **「조회」 제출 UX** (Q255) |
| **BNK-48·49 은행 일괄입금 (US-L01)** | **BE·FE Fixed** | **`BankDepositImportPanel`** — **`activeBranchId` → `branchId`** (Q227·Q228) · **8-bank format guide** (`758e590`, Q258) · **은행별 샘플 xlsx** (`b9845ac`, Q258) |
| **G2 copayAmount null guard (US-L01)** | **BE Fixed** | **`recordCopayPayment`**·**`updateClaimStatus`→`PAID`** — **`copayAmount` NULL → `422`** (`1af5b1f`·`923e610`, Q257) |
| **G2 CMS debit integrity** | **BE Fixed** | **copay ≤ 0 거부** · **FCMS 실패·금액 불일치 → `FAILED` 응답 반환(422 아님)** (`838a7f6`, Q256) · **`SUCCEEDED` 재조회 무결성** (`6bf51c8`) · **FAILED 이력 DB 보존·UI 재시도** (`c5a6cec`·`CmsDebitPanel`) |
| **J03 primary guardian dispatch** | **BE Fixed** | **`NotificationService`** — **대표 보호자 우선 1명** 발송 · 부 보호자 fallback (`555a19f`, Q272) |
| **UXD-81 G33·대장 nav** | **FE Fixed** | **`BillingStartBalanceNotice`** · **`BillingReportsContextNav`** · 정산 후 settings reload (`63361c0`·`eb48879`, Q273) |
| **BNK-102 indicator27 verbatim** | **FE Fixed** | silverangel row3 라벨·**`isFunctionalRecoveryPlanCreateBlocked`** (`7450161`, Q271) |
| **G2 recordCopayPayment paidAt guard** | **BE Fixed** | **`recordCopayPayment`** — **`paidAt` NULL → `422`**(`입금일을 입력해주세요.`, `4001510`, Q250) |
| **G21 HOME_CARE alias (G21)** | **BE Fixed** | **`HOME_CARE` → `HOME_VISIT` 정규화** — 지점 등록·방문일정 guard (`894e246`, Q248) |
| **G2 paymentMethod PAID guard** | **BE Fixed** | **`updateClaimStatus`→`PAID`**·**`notifyPaymentReceipt`** — **`paymentMethod` 필수** (`64ebf6e`, Q249) |
| **US-J02 guardian portal guards** | **FE Fixed** | **`GuardianPortalPage`** — out-of-order 응답 무시·**`billingError` 초기화** (`189a00d`, Q251) · **연말정산 탭** (`7e5c806`, Q252) |
| **UXD-76 VehiclesPage a11y** | **FE Fixed** | 행별 **`aria-label="{plateNumber} 차량 수정"`** (`04f2f89`, Q253) |
| **UXD-75 RecordsContextNav** | **FE Fixed** | 건강·식사·프로그램·**기능회복훈련**·**급여제공결과 평가**·방문·**사례관리** 7화면 **in-page sub-nav** (`1c99bcd`, Q262·Q263·Q276) |
| **G7 NHIS guidance API (QA-B24)** | **BE·FE Fixed** | **`GET /billing/imports/nhis/guidance`** 복원 (`9a97a1c`, Q111) · **`NHISImportPage`** — **`fetchNhisImportGuidanceApi()`** · partial-failure 시 안내 유지 (`0abf164`, Q133) |
| **V70 G15/G16 integrity** | **BE Fixed** | **`client_outings`·`transport_service_fee_records`·`vehicles`·`transport_runs`** Tenant·지점·활성 guard (`ba4c9d9`, Q246) |
| **US-J02 guardian billing filter** | **BE·FE Fixed** | **`listGuardianClientBillingHistory`** — **`CONFIRMED`·`PAID`만** (`3def542`, Q212) |
| **G15 care-provision (3-1)** | **BE·FE Partial Fixed** | **`GET /clients/{id}/care-provision-records/{yearMonth}`** (`8bdead6`, Q243) · **`CareProvisionRecordPanel`** · 이메일 payload transport·vehicle 보강 — **발송 UI Swagger** (Q216) |
| **G16 service-fee·vehicles (v1.3-C)** | **BE·FE Fixed** | **`TransportServiceFeePage`** (Q239) · **cross-branch PATCH 차단** (`b5218a9`, Q247) · **`VehiclesPage`**(`/transport/vehicles`, Q241) · **`TransportVehicleSelect`** · **V69** |
| **G15 client outings (2-1-1·2-9)** | **BE·FE Fixed** | **`ClientOutingService`** · **V67** · **`ClientOutingsPage`·`ClientOutingReportPage`** (`a0dcfc0`, Q240) |
| **G15 출석 transportMode (BNK-58)** | **BE·FE Fixed** | **`GET /attendance?transportMode=all|boarding|on_site`** (`d6d7e7f`) · **`/attendance/boarding`·`/attendance/on-site`** (`6c4c151`, Q232) |
| **G11 가산율 catalog·자동 반영 (BNK-20·56)** | **BE·FE Fixed** | **`GET/POST /billing/fee-surcharge-*`** · **`ATTENDANCE_SCHEDULE` 청구 생성 시 일별 자동 가산** (`d7475fd`) · **`FeeSurchargeGuidePanel`** preview API (`f987b9d`, Q229) |
| **G15 이동서비스 수칙·계약·일지 (v1.3-C partial)** | **BE·FE Fixed** | **`GET/PUT /transport/contracts/{clientId}`** (`3c8f9fe`, V64) · **V65 integrity guard** (`24733c7`, Q235) · **`TransportCompliancePanel`** API 연동 (`9e3cab5`, Q230·Q231) · **`TransportServiceLogPanel`** 제22호 export·시간 준수 (`7389884`·`eef07e5`, Q236) · **`TransportForm18GuidePanel`** 5단계·3분리 신청·등록상태 4단 (`fcf713a`, Q237) · **geocode 저장 차단** (`318411d`·`48d90d5`, Q233) |
| **BNK-47·49·51 월한도 가드 (US-M04, G27)** | **BE·FE Fixed** | **`MonthlyBenefitCapGuardPanel`** · **초과 0건 success banner** (`62f022d`) (Q226·Q228) |
| **v2 G2 email templates** | **BE·FE Partial Fixed** | **`EmailNotificationContent`** **5종** · **납부확인서·노인학대예방 UI Fixed**(Q221·Q222) · **급여제공 조회 UI Fixed**(Q243) · **가정통신문 발송 API-only**(Q217) · **`updateClaimStatus` PAID `paidAt` Fixed**(Q244) · **`paymentMethod` PAID guard Fixed**(Q249) |
| **G19 통합재가 라벨** | **FE Fixed (안내만)** | **`BranchesPage`** `INTEGRATED_HOME` 가산 warning (Q223) — 자동 청구 **Won't v1** |
| **v2 G9 duration_band** | **BE·FE Fixed** | **`DurationBand`** · **V61–V62** · **`resolveDurationBand` 스냅샷 우선** (Q210–Q213) · **`FeeScheduleMatrix`**·NHIS 2026 seed (Q214) |
| **v2 G2 CMS (US-L03)** | **BE·FE Fixed (stub FCMS)** | **`/billing/cms`** · **`CmsController`** · V59–V60 (Q206–Q208) |
| **G21 NHIS confirm-lock** | **FE Fixed · BE upload 미강제** | **`NhisScheduleConfirmLockGuide`** · billing import UI block (Q209) |
| **J03 email channel** | **BE Partial Fixed (stub + SMTP)** | **`StubEmailProvider`** · **`SmtpEmailProvider`** (`6ed48ff`·`f23f15a`, Q204) |
| **v1.2.1 G14 등급 이력** | **BE·FE Fixed** | **`GET /clients/{id}/ltc-grade-history`** · **`GradeHistoryTimeline`** (Q176) · **G37 인정기간 첨부** (`GradeHistoryAttachmentPanel`, Q274) |
| **v1.2.1 US-M02·M03·M04** | **BE·FE Fixed** | **`GET /dashboard/branch`** NHIS·미납 집계(Q202) · **청구 생성 기준·전월 가드 Fixed**(Q224·Q225, V63) · **월한도 가드 UI Fixed**(Q226) · **청구·입금·수납·환불 대장 API·UI Fixed**(Q179, `de49b21`·`212e010`) · **환불 처리 Fixed**(Q261, V71) |
| **BNK-87 NHIS claim comparison (US-M03)** | **BE·FE Fixed** | **`GET /billing/claims/{claimId}/nhis-comparison`** · **`BillingNhisComparisonPanel`** — `DRAFT` 전용 · **본인부담 열·공단 초과/부족 Badge** (`18f5173`, BNK-91 P2, Q264) |
| **G17 functional recovery (US-T06)** | **BE·FE Fixed** | **`FunctionalRecoveryPage`** — compliance DTO 정합 (`0821ce8`, V72, Q262) · **지표27 `provisionRecordedMet`·`planEstablishedBeforeBenefitStartMet`** (`0048105`·`e820b28`·`21b1855`·`7450161`, Q271) · **대시보드 gap 위젯** · **FE create guard** (BNK-102) |
| **G32 case management (US-T07)** | **BE·FE Fixed** | **`CaseManagementPage`** — **7필드 폼·목록**(Q265) · **지표29 StatCard**(Q266, UXD-79 `fa2ad1e`) · **대시보드 30일·평가 widget** (`7f2289b`, Q263·Q266) |
| **US-D01 primaryGuardian** | **BE Fixed** | **`CreateClientRequest.primaryGuardian`** **`@NotNull`** — 미전송 **400** (`0441a07`, Q268) |
| **Pilot fixture panel** | **FE Fixed (dev/flag)** | **`PilotFixturePanel`** — **`/organization/settings`** — **`VITE_ENABLE_PILOT_FIXTURE`** (`37e6b00`·`c89a82b`, Q268) |
| **Tenant context filter** | **BE Fixed** | **`TenantContextFilter`** — JWT **`BearerTokenAuthenticationFilter` 이후** (`cbb7f55`) |
| **US-L03 CMS re-register** | **BE Fixed** | **`CmsService.createEnrollment`** — **`CANCELLED`** 건 재등록 시 **기존 행 UPDATE** (`8431b5c`, Q207) |
| **설정 RBAC·패널** | **FE Fixed** | **`/settings`** `sysadmin` **4탭** · **`PasswordChangeModal` 활성**(Q201) |
| **v2 G21 방문요양** | **BE·FE Fixed** | **`VisitsPage`** · **`HOME_CARE` alias** (Q248) · paired DRAFT sync(Q199) · **paired confirm on confirm**(Q259, `aacf20b`) · **duplicate slot guard**(Q234·Q259, `ff12473`) · paired check-in/out sync(Q238) · NHIS parse(Q200) · cascade cancel(Q194) · duplicate import skip(Q234) |
| **US-L01·L02 billing** | **BE·FE Fixed** | overdue pagination(Q197) · **퇴소 이용자명 Fixed**(Q205) · notify(Q196) · **수납 금액·입금일·copayAmount 검증**(Q218·Q250·Q257) · **notify dedupe**(Q219) · **은행 일괄입금 UI+API Fixed**(Q227·Q228) |
| **G2 보호자 명세 발송** | **BE·FE Fixed** | **`POST /billing/claims/{id}/notify`** · **email channel dispatch**(Q204) |
| **US-L03 CMS 자동이체** | **BE·FE Fixed (stub)** | **`/billing/cms/*`** · **`StubFcmsClient`** · **`payment_method=CMS`** (Q206–Q208) |
| **J03 email channel** | **BE Partial Fixed** | **`StubEmailProvider`**(default) · **`SmtpEmailProvider`**(live, Q204) · **`GuardianEmailResolver`** · **`EmailNotificationContent`** · **`J03EmailServiceFlowE2eTest`** · **`SmtpEmailProviderTest`** |
| **G7 NHIS pending review** | **BE·FE Fixed** | V54 · 대시보드·대사 **패리티**(Q181·Q182·Q183) |
| **V51 지점 프로필** | **BE·FE Fixed** | **`RegionSelector`·`BranchesPage`** (Q184) |
| **v3 meals/programs** | **BE·FE Fixed** | **`POST /meals/menus`·`POST /programs/schedule`** + **POST 폼 FE 연결**(Q161·US-N01d/N02d) |
| **검증 오류** | **BE·FE Fixed** | **`ApiError.fieldErrors`** · **`applyApiErrorToForm`** (Q190) |
| **이용자 목록** | **BE·FE Fixed** | `primaryGuardianName`·`regionLabel`·`ageYears` (Q191) |
| **`hq_admin` 이용자 등록** | **BE Fixed** | **`POST /clients`** — **`hq_admin`** 허용 · **활성 지점(`active_branch_id`) 필수** (`208b37e`, Q267) |
| **J03 Solapi template guard** | **BE Fixed** | **`KAKAO_TPL_*` placeholder 기동 거부** — 승인 templateId 필수 (`98e40a3`, Q266) |
| **BNK-22·UXD-62** | **알림 이력 Fixed · 식사 BE 갭** | Q152·Q187 · Q188 `meals[]` 미반환 |
| **v2 copay·transport·G9** | **BE·FE 연동** | V50·V52 · **V61–V64** duration_band·snapshot·claim basis·**transport contract** · **V58** reminder lookup · transport Q159·Q231 · **`mvn test` 450/450** · Vitest **126/476** |
| Must 업무 UI | **화면 + API 갭** | QR 이미지(Q109)·전용 수납 목록 GET(Q174)·roster(Q94)·가정통신문 발송 UI(Q217) · **NHIS 청구 사전 대조 UI Fixed**(Q264) |

> 화면·버튼 이름은 UI 구현 완료 시 갱신합니다. 본 문서는 **구현된 API**와 **MVP 목표 동작**을 함께 기술합니다.

---

## 2. 아키텍처 개요

### 2-1. 멀티테넌트 계층

```
Organization (Tenant)     ← platform_admin이 생성
  └── Branch (지점)       ← hq_admin이 등록
        ├── users         ← 직원 계정 (역할·지점 배정)
        ├── clients       ← 이용자 (PII 암호화)
        ├── attendance    ← 출석
        ├── health_records
        └── billing_claims
```

- **테넌트 격리**: 모든 운영 데이터는 `organization_id`로 분리됩니다. API·DB 쿼리 모두 JWT의 `organization_id`를 강제합니다.
- **지점 격리**: 이용자·출석·건강 등은 추가로 `branch_id`로 소속 지점이 식별됩니다.
- **JWT 클레임**: `role`, `organization_id`, `branch_ids[]`, `active_branch_id` (API_SPEC §0-2)

### 2-2. 기술 스택

| 계층 | 기술 | 관리자 관점 |
|------|------|------------|
| 백엔드 | Spring Boot 3.x REST (`/api/v1`) | 환경변수·헬스체크·로그 |
| 프론트 | React Vite SPA | 정적 빌드 배포, HTTPS 필수 (**Vite 6**, Vitest 4 — SEC-008) |
| DB | PostgreSQL + Flyway 마이그레이션 | 백업·복구 대상 |
| 인증 | JWT + RBAC | 30분 비활성 만료, 역할별 `@PreAuthorize` |
| PII | AES-GCM (`PII_ENCRYPTION_KEY`) | 키 로테이션·시크릿 관리 |

### 2-3. 환경변수 (관리자 필수 확인)

백엔드 `application.yml` 기준. **비밀값은 코드·Git에 저장하지 않습니다.**

| 변수 | 용도 | 미설정 시 |
|------|------|----------|
| `DB_URL` | PostgreSQL JDBC URL | 기본 `localhost:5432/ogada` |
| `DB_USERNAME` / `DB_PASSWORD` | DB 인증 | 개발 기본값 (운영 시 반드시 변경) |
| `PII_ENCRYPTION_KEY` | 주민번호·연락처·주소 암호화 | **이용자 등록·복호화 실패** |
| `QR_TOKEN_SECRET` | 지점 QR 토큰 서명 | QR 체크인 불가 |
| `JWT_PRIVATE_KEY` / `JWT_PUBLIC_KEY` | JWT RSA PEM | 미설정 시 ephemeral 키(재시작 시 무효) |
| `BACKUP_STORAGE_DIR` | Tenant 백업 manifest 저장 경로 | `./data/backups` |
| `BACKUP_SCHEDULER_ENABLED` | 일 1회 백업 스케줄러 | `true` |
| `SERVER_PORT` | API 포트 | 8080 |
| `AUTH_LOGIN_IP_RATE_LIMIT_PER_MINUTE` | 로그인 IP당 분당 한도 | `30` |
| `AUTH_LOGIN_ACCOUNT_RATE_LIMIT_PER_MINUTE` | 로그인 계정당 분당 한도 | `10` |
| `AUTH_REFRESH_IP_RATE_LIMIT_PER_MINUTE` | refresh IP당 분당 한도 | `40` |
| `AUTH_PASSWORD_RESET_REQUEST_IP_RATE_LIMIT_PER_MINUTE` | 비밀번호 재설정 요청 IP 한도 | `20` |

```bash
# 운영 예시 (값은 환경에 맞게 설정)
export PII_ENCRYPTION_KEY="<Base64 인코딩 32바이트 키>"
export QR_TOKEN_SECRET="<충분히 긴 랜덤 시크릿>"
export DB_URL="jdbc:postgresql://db.internal:5432/ogada"
```

> 키 생성·로테이션 절차는 §8을 참고하세요.

> **`prod` 프로필**: `ProductionSecretValidator`가 기동 시 `JWT_PRIVATE_KEY`, `JWT_PUBLIC_KEY`, `QR_TOKEN_SECRET`, `DB_PASSWORD`를 검증합니다. 기본값 `ogada` DB 비밀번호는 **거부**됩니다.

---

## 3. 플랫폼 관리자 (`platform_admin`)

ogada 영업·운영 직원이 **신규 고객 센터를 개통**할 때 따르는 절차입니다.

### 3-1. 접속·권한

1. ogada 관리 URL에 `platform_admin` 계정으로 로그인합니다.
2. 로그인 성공 시 **`/platform`** 플랫폼 관리 화면으로 이동합니다.
3. 이 역할은 **운영 데이터(이용자·출석 등)에 접근할 수 없습니다.** Tenant 메타데이터와 초기 계정 발급만 가능합니다.

### 3-2. 신규 고객 온보딩 절차

**시나리오**: 「행복주간보호센터」가 ogada 구매 → 월요일부터 사용.

```
[ogada 직원]                    [고객 센터]
  ① Tenant 등록        →
  ② hq_admin 발급       →  ③ 센터장 로그인
                            ④ 지점·직원 등록
                            ⑤ 운영 시작
```

| 순서 | 화면·API | 작업 | 결과 |
|------|----------|------|------|
| 1 | `/platform` → **고객 등록** 모달 | 법인명·사업자번호·요금제 입력 | Organization 생성 |
| 2 | 목록 행 → **관리자 발급** 모달 | 센터장 이메일·이름·초기 비밀번호 | `hq_admin` 계정 1개 |
| 3 | — (고객 전달) | 로그인 정보를 센터장에게 **안전한 채널**로 전달 | 고객 자체 운영 시작 |
| 4 | — | 센터장이 지점·직원·이용자 등록 | 파일럿·운영 개시 |

> **UI (2026-06-07 TSR 39차)**: `/platform`에서 Tenant **등록 모달**·목록 행 **「관리」** → **`PlatformOrgDetailModal`**(법인 메타·관리자 발급 폼, FAQ **Q127**)이 동작합니다. **목록 빈 테이블**·**발급 실패**는 `items` vs `List`·발급 `{email}` vs `password`+`displayName` 불일치(Q97). **검색** `?q=` vs `?query=`(Q83).

#### API 호출 예시

**① 신규 Tenant 등록** — `POST /api/v1/platform/organizations`

```json
{
  "name": "행복주간보호센터",
  "businessNo": "123-45-67890",
  "plan": "standard"
}
```

**② 첫 `hq_admin` 발급** — `POST /api/v1/platform/organizations/{orgId}/admins`

```json
{
  "email": "kim@happy-care.com",
  "displayName": "김센터장",
  "password": "<초기 비밀번호 — 전달 후 변경 권고>"
}
```

> 구현 확인: `PlatformOrganizationController`는 `@PreAuthorize("hasRole('PLATFORM_ADMIN')")`로 보호됩니다. `platform_admin` 역할은 Tenant API로 **생성 불가**합니다 (`UserService` 정책).

### 3-3. 기존 고객 관리

| 작업 | API | 설명 |
|------|-----|------|
| 전국 고객 목록 | `GET /platform/organizations` | 가입 법인 목록·요금제·활성 상태 |
| 고객 검색 | `GET /platform/organizations?query=행복` | **법인명·사업자번호** 부분 일치 검색 (V27·V29 trigram 인덱스) |
| 고객 상세 | `GET /platform/organizations/{orgId}` | Tenant 메타데이터 조회 |
| 요금제·상태 변경 | `PATCH /platform/organizations/{orgId}` | `plan`, `active`(정지/재개) |

> **프론트 주의 (2026-06-07)**: `PlatformPage`는 `?q=`를 전송합니다. 검색이 동작하지 않으면 `?query=`로 직접 호출하세요 (FAQ Q83). 목록은 백엔드가 **페이지네이션 없는 `List`**를 반환하는데 UI는 `result.items`를 읽어 **빈 테이블**이 될 수 있습니다 (FAQ Q97). Swagger `GET /platform/organizations`로 배열을 직접 확인하세요.

**Tenant 정지 (`active: false`) 시**

- 해당 Organization 소속 **전 계정 로그인 차단** (구현 시 `is_active` 검증).
- 운영 데이터는 즉시 삭제하지 않습니다. 해지·파기 절차는 `DATA_RETENTION_POLICY.md` §4-2를 따릅니다.

### 3-4. 플랫폼 관리자 운영 체크리스트

- [ ] 신규 등록 시 **사업자등록번호 중복** 확인 (API가 `409`/`BUSINESS_RULE` 반환)
- [ ] 기존 고객 조회 시 `?query=`로 **법인명·사업자번호** 동시 검색 활용 (V29)
- [ ] 초기 비밀번호는 **1회용**으로 안내, 센터장에게 첫 로그인 후 변경 요청
- [ ] 로그인 정보는 이메일·전화 등 **평문 채팅에 남기지 않음**
- [ ] 계약 해지 시 Tenant 정지 → 90일 유예 → 파기 절차 ops 팀과 연계
- [ ] 플랫폼 작업은 `audit_logs`에 기록 (Tenant 해지·파기 이벤트 포함)

---

## 4. 시스템 관리자 (`sysadmin`)

고객 센터 IT 담당자가 **자기 법인(Tenant)의 기술·보안·백업**을 관리할 때 사용합니다.

### 4-1. 접속·권한

1. 센터에서 발급한 `sysadmin` 계정으로 로그인합니다.
2. 로그인 성공 시 **`/settings`** 시스템 설정 화면으로 이동합니다.
3. **운영 데이터 CRUD 불가** — 이용자·출석·청구 화면에는 접근하지 않습니다.
4. **다른 Tenant 데이터 조회·설정 불가** — JWT `organization_id`로 자동 격리됩니다.

### 4-2. `/settings` 화면 구성 (`sysadmin` 전용, 4탭)

| 탭 (프론트) | 대상 역할 | API (FE `3803247`) | 설명 |
|-------------|----------|-------------------|------|
| **보안** | `sysadmin` | `POST /auth/change-password` (**Fixed**, Q122), `POST /auth/password/reset-request` (**Fixed**) | 비밀번호 변경·재설정 모달 (Q122·Q126) |
| **백업** | `sysadmin` | `GET /settings/backups`, `PATCH /settings/system` `{ backupEnabled }` | `BackupSettingsPanel` — **조회·토글 Fixed** (Q121) · 수동 트리거 미구현 |
| **감사** | `sysadmin` | `GET /settings/audit-logs?page=&size=` | `AuditLogPanel` — **목록 Fixed** · UI 날짜·유형 필터는 클라이언트 측 |
| **로그인 이력** | `sysadmin` | `GET /auth/login-history` | `LoginHistoryPanel` — **목록 Fixed** · UI 역할·기간 필터는 클라이언트 측 (Q125) |

> **조직 운영 정책**(`allowClientSelfCheckin`)은 **`hq_admin` 전용** **`/organization/settings`** (`OrganizationSettingsPage`, Q178) — §6-3 참고.

| API (백엔드) | 설명 |
|-------------|------|
| `GET /settings/system` | Tenant명, 플랜, `backupEnabled`, `auditRetentionDays`, JWT issuer·access TTL |
| `PATCH /settings/system` | `backupEnabled`, `auditRetentionDays` 변경 (감사 로그 `SYSTEM_SETTINGS_UPDATED` 기록) |
| `GET /settings/audit-logs` | PII 접근·권한 변경·청구 확정·NHIS import 등 (페이지네이션) |
| `GET /settings/backups` | 일일 백업 실행 이력 (`status`, `completedAt`, `sizeBytes`, `errorMessage`) |

**`PATCH /settings/system` 요청 예시**

```json
{
  "backupEnabled": true,
  "auditRetentionDays": 1095
}
```

> **백엔드**: `SettingsController`는 `@PreAuthorize("hasRole('SYSADMIN')")`로 보호됩니다. **프론트엔드 UI**(`75fc91e`)는 백업·감사·로그인 이력 **조회·백업 토글**·**비밀번호 변경**(Q122)이 연동되었습니다. **수동 백업**은 Swagger 우회(Q121).

> **역할 분리 (FE `f749311`, FAQ Q178 Fixed)**: **`/settings`** — **`sysadmin` only** (`SettingsController` `@PreAuthorize`). **`hq_admin`** — SideNav **조직 설정** **`/organization/settings`** — `GET/PATCH /organization/settings` **UI 저장 연동 Fixed**(Q116).

### 4-3. 감사 로그 (`audit_logs`)

감사 로그는 보안·개인정보 컴플라이언스의 핵심입니다. `sysadmin`은 **조회만** 가능하며, 로그 **삭제·수정은 불가**(append-only)합니다.

**필수 기록 대상** (DATA_RETENTION_POLICY §6)

| 이벤트 | `action` 예시 | 비고 |
|--------|--------------|------|
| 주민등록번호 복호화 열람 | `PII_DECRYPT_VIEW` | `POST /clients/{id}/resident-registration/reveal` 호출 시 |
| 청구서 상태 변경 | `BILLING_STATUS_CHANGE` | 작성중→확정→수납완료 |
| Tenant·지점·권한 변경 | `ORG_UPDATE`, `USER_ROLE_CHANGE` | |
| 대량 export·NHIS import | `NHIS_IMPORT`, `DATA_EXPORT` | |

**엔티티 행위자 컬럼** (V32–V35, `audit_logs`와 별도)

| 테이블 | 컬럼 | 기록 시점 |
|--------|------|----------|
| `attendance` | `created_by` | 수기·QR·결석 INSERT |
| `health_records` | `recorded_by` | 건강·투약·사고 기록 INSERT |
| `billing_claims` | `generated_by` | 월별 청구서 생성 |
| `nhis_import_batches` | `imported_by` | 공단 엑셀 import 완료 |
| `fee_schedules` | `created_by` | 수가표 신규 버전 INSERT (`hq_admin`, V35 backstop) |
| `branch_qr_tokens` | `created_by` | 지점 QR 발급 INSERT (`branch_admin` 이상, V35 backstop) |

앱은 쓰기 트랜잭션에서 `DbSessionContext.setActorUserId(JWT subject)`를 호출하며, 누락 시 DB 트리거가 `ogada.actor_user_id` 세션 변수로 backstop합니다. `BillingService.createFeeSchedule`은 앱에서 `createdBy`를 설정하지 않으므로 V35 트리거가 필수입니다. QR 발급은 `AttendanceService`가 JWT subject를 명시 설정하나, raw SQL 방어를 위해 V35가 동일 패턴을 적용합니다.

**조회 API** — `GET /settings/audit-logs`

```
?page=0&size=20
```

> 날짜·`action` 필터는 API_SPEC §9 기준이며, UI 필터는 후속 구현입니다.

**응답 필드 (스키마 기준)**

| 필드 | 설명 |
|------|------|
| `organization_id` | Tenant (자동 필터) |
| `branch_id` | 관련 지점 (nullable) |
| `actor_user_id` | 행위자 UUID (PII 대신 UUID) |
| `action` | 행위 코드 |
| `target_type` / `target_id` | 대상 리소스 |
| `details` | JSONB 부가 정보 (민감값 제외) |
| `created_at` | 발생 시각 |

**보존 기간**: **3년** (DATA_RETENTION_POLICY §3)

### 4-4. 백업·복구

| 항목 | 정책 |
|------|------|
| 주기 | **일 1회** 전체 DB 스냅샷 |
| 보관 | **30일** 롤링 |
| 암호화 | 백업 파일 at-rest 암호화 (KMS·환경변수 키) |
| RPO / RTO 목표 | 24시간 / 4시간 (인프라 구현 시 확정) |

**`sysadmin` 역할**

1. `/settings` → **백업** 탭(또는 `GET /settings/backups`)에서 최근 백업 성공 여부·시각을 확인합니다.
2. `backupEnabled`가 `false`이면 해당 Tenant는 스케줄러 대상에서 제외됩니다.
3. 복구가 필요하면 ogada ops(또는 자체 인프라 담당)에 **Tenant ID·장애 시각·증상**을 전달합니다.

**MVP 백업 실행 방식**

| 항목 | 내용 |
|------|------|
| 스케줄 | 기본 매일 02:00 (`BACKUP_DAILY_CRON`) |
| 실행체 | `FileTenantBackupExecutor` — Tenant별 `manifest.json` 생성 |
| 저장 경로 | `BACKUP_STORAGE_DIR/{organizationId}/` |
| 이력 | `backup_runs` 테이블 (V9, V20 무결성 제약) |
| 프로덕션 | `pg_dump` 또는 Managed DB 스냅샷으로 교체 예정 |

> 백업 인프라(PG dump, 클라우드 스냅샷 등) 상세는 `DEPLOYMENT_GUIDE.md` §8-2를 참고하세요.

### 4-5. 로그인 이력

| 항목 | 내용 |
|------|------|
| API | `GET /auth/login-history` (본인 또는 Tenant 관리자 역할) |
| UI | `/settings` → **로그인 이력** 탭 — `LoginHistoryPanel` (Q125) |
| DB 테이블 | `login_history` (V2 마이그레이션) |
| 보존 | **1년** |
| 활용 | 비정상 로그인·역할 오남용 탐지 |

`sysadmin`은 Tenant 소속 계정의 로그인 패턴을 모니터링하고, 의심 세션 발견 시 해당 계정 비활성화를 `hq_admin`에 요청합니다.

> **UI 주의 (Q125)**: 패널은 역할·기간 필터·마스킹 표를 제공하나, 프론트가 `GET /settings/login-history`를 호출합니다. 오류 시 Swagger `GET /api/v1/auth/login-history`로 확인하세요. 응답 `success`(boolean)와 UI `result` Badge 매핑은 후속입니다.

### 4-6. 시스템 관리자 일상 점검

| 주기 | 점검 항목 |
|------|----------|
| 매일 | 백업 성공 여부, API 헬스 (`/actuator/health`) |
| 매주 | 감사 로그 이상 패턴(PII 대량 열람, 권한 변경) |
| 매월 | `PII_ENCRYPTION_KEY`·`QR_TOKEN_SECRET` 로테이션 일정 확인 |
| 수시 | 신규 직원 `sysadmin` 계정 발급·퇴직 시 즉시 비활성화 |

---

## 5. 보안·개인정보 (관리자 공통)

### 5-1. PII 암호화 정책

| 데이터 | 분류 | 저장 처리 | 화면·로그 |
|--------|------|----------|----------|
| 주민등록번호 | 고유식별정보 | **AES-GCM 암호화** (`*_encrypted`) | 마스킹 `******-*******` |
| 연락처·주소 | 준식별정보 | **암호화 권장** | 부분 마스킹 |
| 장기요양인정번호 | 운영 식별자 | 평문 | 표시 가능 |
| 건강·투약 기록 | 민감정보 | TLS + RBAC | 접근 시 audit |

**구현**: `PiiCryptoService` — `ogada.security.pii-encryption-key` 환경변수(Base64, 32바이트) 필수.

**관리자 주의사항**

- 주민번호 **평문을 로그·티켓·이메일에 기록하지 않습니다.**
- 복호화 열람은 법정 목적(청구 등)에 한하며, `audit_logs`에 남습니다.
- 이용자 등록 시 **별도 수집·이용 동의**(`consent_collected_at`) 없으면 저장이 차단됩니다.

### 5-2. RBAC·지점 스코프

| 규칙 | 내용 |
|------|------|
| 역할 분리 | MVP **7역할** + `client_user` 각각 별도 화면·API 권한 |
| 지점 스코프 | `branch_admin` 이하는 `branch_ids` 내만 CRUD |
| `hq_admin` 쓰기 | `active_branch_id` 선택 지점만 CRUD, 전 지점 조회·집계 |
| API 강제 | `@PreAuthorize` + `JwtScopeResolver` 이중 검증 |
| 금지 | `platform_admin`을 Tenant API로 생성 시도 → 거부 |

### 5-3. QR 토큰 보안

- 지점 QR은 `QR_TOKEN_SECRET`으로 **서명·만료**된 토큰입니다.
- 만료·위조 QR 스캔 시 `422 BUSINESS_RULE` 오류.
- QR 토큰 메타 보존: 유효일 종료 후 **7일** (DATA_RETENTION_POLICY §3).

### 5-4. 에러·로그 노출 정책

- API 에러 응답에 **스택 트레이스·DB 스키마·키 경로를 노출하지 않습니다.**
- 클라이언트에는 `error.code`, `error.message`, `traceId`만 반환 (API_SPEC §0-3).
- 인증 rate limit 초과 시 `429` + `RATE_LIMITED` — 「요청이 너무 많습니다. 잠시 후 다시 시도해주세요.」

---

## 6. 계정·조직 관리 (관리자 협업)

일상 계정·지점 관리는 **`hq_admin`**(통합 관리자) 또는 **`branch_admin`**(지점장)이 수행합니다. `sysadmin`·`platform_admin`은 아래를 **참고·감독**합니다.

### 6-1. `sysadmin` 계정 발급

1. `hq_admin`이 **직원 계정 생성** 화면 또는 `POST /api/v1/users`로 발급합니다.
2. `roleCode`에 `sysadmin`을 지정합니다.
3. `sysadmin`은 지점 배정(`branchIds`) 없이 Tenant 전체 기술 설정만 담당합니다.

```json
{
  "email": "it@happy-care.com",
  "displayName": "박IT",
  "password": "<초기 비밀번호>",
  "roleCode": "sysadmin",
  "branchIds": []
}
```

### 6-2. 역할별 생성 권한

| 생성자 | 생성 가능 역할 |
|--------|---------------|
| `platform_admin` | `hq_admin` (Tenant당 최초 1회 API) |
| `hq_admin` | `branch_admin`, `social_worker`, `caregiver`, `guardian`, `client_user`, `sysadmin` |
| `branch_admin` | `branch_admin`, `social_worker`, `caregiver`, `guardian`, `client_user` |
| **공통 금지** | `platform_admin` — 어떤 API로도 생성 불가 |

**이메일 정책 (V30)**

- Tenant 내 직원 이메일은 **대소문자 무시 UK** — `Kim@center.com`과 `kim@center.com` 중복 불가.
- `UserService`가 저장 시 `trim().toLowerCase()` 정규화를 적용합니다.
- cross-tenant 동일 이메일은 DB UK로 막지 않으며, 로그인 시 **단일 active 계정**만 허용합니다 (`AuthService`).

**비밀번호 재설정 보안 (V30)**

- `POST /auth/password/reset` 성공 시 해당 사용자의 **활성 refresh 토큰 전부 폐기** (`revokeAllActiveForUser`).
- 재설정 링크·기존 세션 무효화로 탈취 계정의 지속 접속을 차단합니다.

### 6-2-1. G37 등급 인정기간 첨부 (BNK-105, `sysadmin`·`hq_admin` 참고)

장기요양 **인정기간별 장기요양이용계획서** PDF/PNG를 등급 이력 행에 보관합니다 (이지케어 FAQ 49a778e8 벤치마크).

| 항목 | 내용 |
|------|------|
| API | `GET/POST/GET(download)/DELETE /api/v1/clients/{clientId}/ltc-grade-history/{historyId}/attachments*` |
| 업로드 RBAC | **`branch_admin`·`social_worker`** |
| 조회 RBAC | **`hq_admin`·`branch_admin`·`social_worker`·`caregiver`** |
| 형식·크기 | PDF·PNG · **≤10MB** (V78 CHECK + 앱 검증). FE는 **MIME 없음·`application/octet-stream`일 때만** **`.pdf`/`.png` 확장자 fallback** (`e9d1178`) — **`text/plain` 등 잘못된 MIME은 거부** |
| DB | **V78** `client_ltc_grade_history_attachments` · **V79** `(organization_id, client_id, history_id)` FK — **타 이용자 이력에 첨부 연결 DB 차단** |
| 파일 저장 | **`LtcGradeHistoryAttachmentStorageService`** — `ogada.storage.ltc-grade-attachments.storage-dir` (기본 `./data/ltc-grade-attachments`) |
| 보존 | 등급 이력과 동일 cohort — **퇴소 후 5년** (`DATA_RETENTION_POLICY` §2-1) · 이력 CASCADE 삭제 시 DB 행 제거 — **디스크 오브젝트는 purge 배치에서 `storage_key` 기준 별도 삭제** |
| 백업 | Tenant manifest 백업에 **첨부 디렉터리 포함** 권장 — 미포함 시 복구 시 파일 유실 |
| 테스트 | **`LtcGradeHistoryAttachmentServiceTest`** · **`LtcGradeHistoryAttachmentStorageServiceTest`** · **`GradeHistoryAttachmentPanel.test.jsx`** · **`pilotPageFlows`** · **`gradeHistoryAttachmentLiveApi.e2e.test.js`** (BNK-106) |

> 현장 UI: USER_MANUAL §3-3 · FAQ Q274

### 6-2-2. G38 급여계획 통보 모니터링 (BNK-106, BE·FE Fixed)

이지케어 FAQ 21802 대응 — **급여인정 시작 후 5·11개월 milestone**·**재발급 인정기간 첨부 미반영**을 이용자별로 집계합니다.

| 항목 | 내용 |
|------|------|
| API | `GET /api/v1/clients/care-plan-notifications/compliance` — 선택 **`?branchId=`** (JWT 스코프 내, `03211e6`) |
| RBAC | **`hq_admin`·`branch_admin`·`social_worker`** — 활성 지점 스코프 · `caregiver` **403** |
| 집계 | `fiveMonthsElapsed` · `elevenMonthsElapsed` · `reissueNotReflected` · `alertLevel` (`NONE`/`WARNING`/`CRITICAL`) |
| CRITICAL | 최신 `ltc_grade_history` 행에 **G37 첨부 0건** |
| WARNING | 급여시작 **≥5개월** 또는 **≥11개월** — 첨부는 있음 |
| FE UI | **`CarePlanNotificationPage`**(`/clients/care-plan-notifications`) — StatCard·필터·표 · **`DashboardPage`** G38 위젯 3종 · compliance 실패 시 **partial-load warning** (`28c22b0`·`4b2b082`, Q277) |
| 연계 | **G37 첨부 업로드** — §6-2-1 · **`CarePlanNotificationComplianceServiceTest`** · **`CarePlanNotificationPage.test.jsx`** · **`pilotPageFlows`** · **`programComplianceLiveApi.e2e.test.js`** |

> 현장: USER_MANUAL §4-3 · 인정기간 첨부 §3-3 · FAQ Q274·Q277

### 6-2-3. US-S02 보수교육 이수증 첨부 (8-7-1, BNK-136, BE·FE Fixed)

케어포 **8-7-1**·FAQ21825 **③ 근로활동** 「보수교육」 이수 **증빙 파일**을 직원별로 보관합니다.

| 항목 | 내용 |
|------|------|
| API | `GET/POST /api/v1/staff/refresher-training/users/{userId}/certificates` · `GET …/{certificateId}` inline download · `DELETE …/{certificateId}` |
| RBAC | **조회·미리보기**: `hq_admin`·`branch_admin`·`social_worker` · **업로드·삭제**: `branch_admin`·`social_worker` **만** |
| 형식 | **PDF** · **PNG** · **JPEG** — **≤10MB** (FE·BE·V88 CHECK) |
| DB | **Flyway V88** `staff_refresher_training_certificates` — Tenant·지점·직원 FK · **V90** user-branch composite FK·actor backstop·purge index (`a206508`) |
| 스토리지 | **`staff-refresher-training-certificates/{organizationId}/{userId}/{uuid}.ext`** — G37 첨부와 **동일 로컬 스토리지 디렉터리** (`ogada.storage.ltc-grade-attachments`) |
| lifecycle | 업로드 성공 시 **`lifecycleChecklist["refresher-training"]=true`** 자동 저장 — compliance 집계·**`StaffLifecyclePanel`** ③ 근로와 동일 |
| FE UI | **`StaffRefresherTrainingPage`** — 목록 **「이수증」** Modal · **`FileUpload`** · PDF 새 탭·이미지 Modal 미리보기 · **StatCard 입사일 미등록·requiredCount** (`0a7fe16`·`50bdb6e`) |
| 테스트 | **`StaffRefresherTrainingCertificateServiceTest`** · **`StaffRefresherTrainingCertificateStorageServiceTest`** · **`staffRefresherTrainingServices.test.js`** · **`StaffRefresherTrainingPage.test`** · **`pilotPageFlows`** certificate E2E |
| 보관 | 직원 lifecycle 인사기록과 동일 cohort — `DATA_RETENTION_POLICY` §3 (퇴사 후 3년·익명화) |

> 현장: USER_MANUAL §5-3 · FAQ Q294·Q295 · compliance API §6-2-3 상위 `GET /staff/refresher-training/compliance`

### 6-2-4. US-R02 직원 건강검진 (8-10, BNK-138, BE·FE Partial Fixed)

케어포 **8-10**·이지케어 FAQ21799 **지표9** — 직원 **건강검진 실시일**·**5개 영역** checklist를 Tenant·지점 스코프로 보관합니다.

| 항목 | 내용 |
|------|------|
| API | `GET /api/v1/staff/health-checkups/compliance?branchId=&referenceDate=` · `GET /api/v1/staff/health-checkups/users/{userId}` · `POST /api/v1/staff/health-checkups/users/{userId}` |
| RBAC | **조회·이력**: `hq_admin`·`branch_admin`·`social_worker` · **기록 등록**: `branch_admin`·`social_worker` **만** |
| 5개 영역 | `bodyMeasurementCompleted` · `urinalysisCompleted` · `bloodTestCompleted` · `imagingCompleted` · `resultAssessmentCompleted` — **최소 1개 true** (V89 CHECK) |
| 주기 | **일반 1년** · **사무직 2년** (`is_office_worker`) |
| DB | **Flyway V89** `staff_health_checkups` — Tenant·지점·직원 FK · **V90** `chk_staff_health_checkups_checkup_date_not_future`·`recorded_by` backstop (`a206508`) |
| lifecycle | checklist id **`health-check`**(입사) · **`health-check-renewal`**(갱신) — `StaffLifecycleChecklist` 허용 목록 · **자동 checklist 반영은 P2** |
| FE UI | **`StaffHealthCheckupsPage`** — StatCard·**`LifecycleWorkflowPanel`** · **「검진 기록」**·**「이력」** Modal (`604787f`) |
| 테스트 | **`StaffHealthCheckupServiceTest`** · **`StaffHealthCheckupComplianceTest`** · **`StaffHealthCheckupPilotServiceFlowE2eTest`** · **`staffHealthCheckupLiveApi.e2e.test.js`** · **`StaffHealthCheckupsPage.test`** |
| 보관 | 직원 인사기록 cohort — `DATA_RETENTION_POLICY` §3 (퇴사 후 3년) |

> 현장: USER_MANUAL §5-3 · FAQ Q296 · compliance API §6-2-4

**직원현황 리포트 (8-12, US-R02, BNK-142~175, BE·FE Partial+ Fixed)**

케어포 **8-12** — onboarding·refresher·health compliance를 **서버 aggregated API**로 집계하고, FE에서 **출력물 7종**(인쇄 6 + BE CSV)을 제공합니다.

| 항목 | 내용 |
|------|------|
| BE API | **`GET /api/v1/staff/reports/status?branchId=&referenceDate=`** — **`StaffStatusReportService`** (`aaa16f8`) · items[] + summary |
| BE CSV | **`GET /api/v1/staff/reports/status/export?branchId=&referenceDate=&outputType=excel`** — UTF-8 BOM (`bc927f7`·`c4dbe43`) |
| FE UI | **`StaffStatusReportPage`** — **`/staff/reports/status`** (`488f547`·`5bba7a2`) · **`fetchStaffStatusReportApi`** · **`exportStaffStatusReportCsvApi`** |
| export | **`staffStatusReportExports.js`** — 인쇄 6종 + **BE CSV** (`488f547`, Q315) |
| RBAC | **`hq_admin`·`branch_admin`·`social_worker`** — **`StaffStatusReportPilotServiceFlowE2eTest`** · **`RoleBasedControllerAccessTest$StaffStatusReportAccess`** |
| 테스트 | **`StaffStatusReportPage.test`** · **`StaffStatusReportServiceTest`** · **`StaffStatusReportPilotServiceFlowE2eTest`** |

| P2 잔여 | **대시보드 위젯** · **공식 PDF 서식** · **live E2E** |

> 현장: USER_MANUAL §5-3 · FAQ Q308·Q315

### 6-2-11. G30 모니터링 자가진단·유선상담·통합 checklist (FAQ21836/21841/21842/21838~21842, BNK-169~171·181, BE·FE Fixed)

이지케어 FAQ **21836**(안부전화)·**21841**(월별 자체점검 15항목)·**21842**(직전 6개월 자가진단)·**21838~21842**(통합 checklist)에 대응합니다. **지점 단위** 기록 — 이용자 PII는 **유선상담 notes**에만 포함됩니다.

| 항목 | 내용 |
|------|------|
| BE API | **`MonitoringController`** — Base **`/api/v1/compliance/monitoring`** (`6a72b70`·`b1dfd34`) |
| integrated checklist | **`GET …/checklist?referenceYear=&referenceMonth=`** — **`MonitoringIntegratedChecklist.build`** — FAQ21838~21842 **문항 6~15** · **`MET`·`PARTIAL`·`UNMET`·`MANUAL`** |
| self-diagnosis | **`GET/POST/PATCH …/self-diagnoses*`** · **`GET …/self-diagnoses/compliance`** — **rolling 6 months** |
| phone consultation | **`GET/POST …/phone-consultations*`** · **`GET …/suggestions`** — **5 clients/month** · **`GET …/compliance`** |
| templates | **`GET …/items`** — **15 item codes** · 5-field form (FAQ21836) |
| DB | **Flyway V100** `monitoring_self_diagnoses`·`monitoring_phone_consultations` · **V101** integrity — active-client guard·`created_by` backstop·purge index (`f4c8558`) |
| RBAC | **`hq_admin`·`branch_admin`·`social_worker`** — **`MonitoringPilotServiceFlowE2eTest`** · **`RoleBasedControllerAccessTest$MonitoringAccess`** |
| FE UI | **`MonitoringSelfDiagnosisPage`** — **`MonitoringIntegratedChecklistPanel`** · **`navConfig`** **「모니터링 자가진단 (G30)」** · **`monitoringCompliance.js`** · FAQ21836 **`DEFAULT_MONITORING_RELATED_BASIS`** (`0da41c6`) |
| 보관 | **5년** — `DATA_RETENTION_POLICY` §3 (지점 cohort / 이용자 purge 연동) |

| P2 잔여 | FAQ21812 **관리자 라운딩** · **live E2E verify** |

> 현장: USER_MANUAL §4-3 · FAQ Q314·Q320

### 6-2-12. G41/G41b 기관 교육일지 (8-7, FAQ21807/21828, BNK-184, BE·FE Fixed)

케어포 **func.php `8-7.교육일지`** — **노인인권·운영규정·재난·소화·직원권익** 지점 교육 증빙입니다. **보수교육(8-7-1)** 은 §6-2-3과 **별도 도메인**입니다.

| 항목 | 내용 |
|------|------|
| BE API | **`StaffTrainingLogController`** — Base **`/api/v1/staff/training-logs`** (`6191b91`·`613b6af`) |
| list | **`GET …?branchId=&referenceYear=&trainingType=`** — **`StaffTrainingLogListResponse`** |
| create/update | **`POST …`** · **`PATCH …/{logId}`** — **`CreateStaffTrainingLogRequest`** / **`UpdateStaffTrainingLogRequest`** |
| compliance | **`GET …/compliance?branchId=&referenceYear=`** — 노인인권 **반기** · 운영규정 **연간** · **신규직원 7일** orientation rows |
| trainingType | **`ELDERLY_HUMAN_RIGHTS`** · **`OPERATING_REGULATION`** · **`DISASTER_RESPONSE`** · **`FIRE_SAFETY_EQUIPMENT`** · **`STAFF_RIGHTS`** (V106) |
| guards | 노인인권 — **referenceHalf·trainingContent 필수** · 신규 오리엔테이션 — **`newHireUserId` + hiredAt+7일** · **trainedAt.year = referenceYear** |
| DB | **Flyway V104** `staff_training_logs` · **V105** org sync·actor backstop·new_hire FK · **V106** G41b CHECK |
| RBAC | **`hq_admin`·`branch_admin`·`social_worker`** — **`MustApiEndpointRoutingTest$StaffTrainingLogRouting`** · **`RoleBasedControllerAccessTest$StaffTrainingLogAccess`** |
| FE UI | **`StaffTrainingLogPage`**(`/staff/training-logs`) — StatCard·필터·Modal CRUD · **`StaffContextNav`** **「교육일지 (8-7)」** · **`staffTrainingLogs.js`** |
| G41b FE | 재난·소화·직원권익 **연간 StatCard** — **목록 기준 FE 집계** (BE compliance **미포함**) |
| 테스트 | **`StaffTrainingLogServiceTest`** · **`StaffTrainingLogPage.test`** · **`PilotChecklistJwtE2eTest`** |
| 보관 | **교육 실시일 5년** · **신규 오리엔테이션 행 3년**(퇴사 cohort) — `DATA_RETENTION_POLICY` §3 |

| P2 잔여 | **G41b 3종 BE compliance API** · **대시보드 위젯** · **인쇄** |

> 현장: USER_MANUAL §5-3 · FAQ Q321 · 보수교육 §6-2-3(8-7-1)

### 6-2-5. US-R03 직원 HR 파일함 (FAQ21806·FAQ21825, BNK-139, BE·FE Fixed)

이지케어 FAQ21806 **입사 8종 서류**·퇴사 **사직서** 스캔을 직원별로 보관합니다. **`lifecycle_checklist`** 와 **documentType** id가 1:1로 연동됩니다.

| 항목 | 내용 |
|------|------|
| API | `GET/POST /api/v1/staff/hr-files/users/{userId}` · `GET …/{fileId}` inline download · `DELETE …/{fileId}` |
| RBAC | **조회·다운로드**: `hq_admin`·`branch_admin`·`social_worker` · **업로드·삭제**: `branch_admin`·`social_worker` **만** |
| documentType | `id-card` · `certificate` · `bank-account` · `health-check` · `dementia-training` · `employment-contract` · `criminal-record` · `resignation` |
| 형식 | **PDF** · **PNG** · **JPEG** — **≤10MB** (FE·BE·V91 CHECK) |
| 교체 | `(organization_id, user_id, document_type)` **UNIQUE** — 재업로드 시 기존 `storage_key` 삭제 후 교체 |
| checklist | upload → **`lifecycleChecklist[documentType]=true`** · delete → **false** (`StaffHrFileService`) |
| DB | **Flyway V91** `staff_hr_files` — V90 **user-branch assignment FK** · org sync · `uploaded_by` backstop |
| 스토리지 | **`staff-hr-files/{organizationId}/{userId}/…`** — G37·G14 첨부와 **동일 로컬 스토리지 디렉터리** |
| FE UI | **`StaffDetailPage`** **「HR 파일함」** — **`StaffHrFilePanel`** + **`StaffRefresherCertificatePanel`** + **`StaffHealthCheckupRecordsPanel`** (`bc3c967`) |
| FAQ21806 | **`StaffLifecyclePanel`** — **입사일 + 7일** 신규직원교육 deadline (`NEW_HIRE_TRAINING_DEADLINE_DAYS`) |
| 테스트 | **`StaffHrFileServiceTest`** · **`StaffHrFilePilotServiceFlowE2eTest`** · **`StaffHrFilePanel.test`** · **`staffHrFileServices.test`** |
| 보관 | 직원 인사기록 cohort — 퇴사 후 3년 (`DATA_RETENTION_POLICY` §3, V91 purge index 후속) |

> 현장: USER_MANUAL §5-3 · FAQ Q298 · lifecycle Q290

### 6-2-6. FAQ21806 입사 처리 compliance 집계 (US-R03, BNK-146, BE·FE Fixed)

이지케어 FAQ21806 **입사 7종 서류**·**신규직원교육 7일** 준수를 **지점 스코프**로 집계합니다. 개별 파일 업로드는 §6-2-5, per-staff checklist는 lifecycle API(`UserService.updateUser`)와 연동됩니다.

| 항목 | 내용 |
|------|------|
| API | **`GET /api/v1/staff/hr-files/onboarding-compliance?branchId=&referenceDate=`** |
| RBAC | **`hq_admin`·`branch_admin`·`social_worker`** — `caregiver`·`guardian` **403** |
| 대상 역할 | `hq_admin`·`branch_admin`·`social_worker`·`caregiver` (스코프 내 직원) |
| 7종 documentType | `id-card` · `certificate` · `bank-account` · `health-check` · `dementia-training` · `employment-contract` · `criminal-record` |
| 집계 규칙 | **`lifecycleChecklist[documentType]=true`** **OR** `staff_hr_files` 업로드 존재 → **제출 인정** |
| 상태 | **`COMPLETED`**(onboardingComplete 또는 전부 충족) · **`IN_PROGRESS`** · **`OVERDUE`**(교육 기한 초과+미비) · **`DRAFT`** |
| 교육 기한 | **`hiredAt + 7일`** — `referenceDate`(기본 오늘) 초과 시 `newHireTrainingOverdue=true` |
| 응답 | `items[]` — `userId`·`displayName`·`roleCode`·`status`·`uploadedDocumentCount`/`requiredDocumentCount`(7) · `missingDocumentTypes[]` · `newHireTrainingDeadline` · `totalCount`·`completedCount`·`inProgressCount`·`overdueCount`·`hasOverdue` |
| DB | **Flyway V92** — `staff_hr_files` org sync trigger · `uploaded_by` backstop · `chk_staff_hr_files_uploaded_at_sane` · purge index |
| FE UI | **`StaffPage`** — **`StaffOnboardingCompliancePanel`** — StatCard·`LifecycleWorkflowPanel`·compliance 표 (`e76ca06`) · **`StaffDetailPage`** — **`StaffMemberOnboardingComplianceCard`** — per-staff compliance·HR 파일함 점프 (`4efa168`) |
| 테스트 | **`StaffHrFileOnboardingComplianceTest`** · **`StaffHrFileServiceTest`**(batch branch, `60789d6`) · **`StaffOnboardingCompliancePanel.test`** · **`StaffMemberOnboardingComplianceCard.test`** · **`StaffPage.test`** |
| 보관 | §6-2-5 `staff_hr_files` 와 동일 — 퇴사 후 3년 |

> 현장: USER_MANUAL §5-3 · FAQ Q300 · HR 파일함 Q298

### 6-2-7. G40 신규입소 위험도평가 (silverangel 지표21, BNK-150~152, BE·FE Fixed)

엔젤 silverangel **「신규입소시」** 급여개시 전 **낙상·욕창·인지기능** 3종 스크리닝을 API·UI로 기록·집계합니다. **G24 욕구사정(지표20)** 과 별도 도메인입니다.

| 항목 | 내용 |
|------|------|
| FE UI — 이용자 상세 | **`ClientDetailPage`** **「위험도평가」** 탭 — **`ClientRiskAssessmentPanel`** — 3종 폼·**StatCard (N/3)** · **`LifecycleWorkflowPanel`** · **`admissionComplete`** warning (`328d697`) |
| FE UI — 대시보드 | **`DashboardPage`**(`/dashboard`·`/dashboard/hq`) — **「신규입소 위험도평가 미완료」** StatCard — **`admissionRiskAssessmentGapCount`** — 스냅샷 우선·누락 시 **`fetchAdmissionRiskAssessmentComplianceApi`** 병렬 폴백 · 클릭 **`/clients`** (`2f5af63`) |
| 평가 유형 | **`FALL_RISK`** · **`PRESSURE_ULCER`** · **`COGNITIVE_FUNCTION`** — 이용자·유형당 **1건** upsert |
| CRUD | **`GET /api/v1/clients/{clientId}/risk-assessments`** · **`GET …/{assessmentType}`** · **`PUT /api/v1/clients/{clientId}/risk-assessments`** |
| 요청 본문 | **`UpsertClientRiskAssessmentRequest`** — `assessmentType` · `assessedOn`(DATE) · `scaleScore`(≥0, optional) · `riskLevel`(`LOW`/`MODERATE`/`HIGH`) · `notes` |
| compliance | **`GET /api/v1/clients/admission-risk-assessments/compliance?branchId=`** — 활성 이용자 중 **`ltcCertValidFrom` 설정** 대상 · **`admissionComplete`** · `missingTypes[]` · `lateTypes[]`(급여개시일 **이후** 평가) — 동일 유형 중복 시 **가장 이른 `assessedOn`/`recordedAt`** (`2589b94`) |
| 검증 | **`assessedOn` ≤ `ltcCertValidFrom`** 권장 — 지연 유형은 compliance **gap** · 퇴소·비활성 이용자 **저장 거부**(V93 trigger) |
| RBAC | **`hq_admin`·`branch_admin`·`social_worker`** — upsert · **`caregiver`** — read-only · **`guardian`** — **403** |
| DB | **Flyway V93** `client_risk_assessments` — org·branch·client composite FK · `(organization_id, client_id, assessment_type)` UNIQUE · **V94** — org·branch listing index · **`chk_client_risk_assessments_recorded_at_after_created`** |
| 테스트 | **`ClientRiskAssessmentServiceTest`**(+54 duplicate regression, `2589b94`) · **`MustApiEndpointRoutingTest$ClientRouting`** · **`RoleBasedControllerAccessTest$ClientAccess`** · **`PilotChecklistJwtE2eTest`** · **`ClientRiskAssessmentPanel.test`** · **`DashboardPage.test`** · **`admissionRiskAssessmentCompliance.test`** |

> Swagger: **`/swagger-ui.html`** → Clients · Admission risk assessments. 현장은 **이용자 상세 「위험도평가」** 탭 우선 — Swagger는 IT·일괄 연동용.

> 관련: FAQ Q301 · USER_MANUAL §3-3 · BENCHMARK_REPORT §152 · G24(Q286)와 구분 · **G40b(Q302)** — §6-2-8

### 6-2-8. G40b 반기 기초평가 위험도 (silverangel 지표16·FAQ21811, BNK-153~154, BE·FE Fixed)

이지케어 **「2.2 정기욕구평가현황」**·silverangel **지표16** — 급여 수급 중 이용자의 **반기 1회** 낙상·욕창·인지기능 재평가. **G40(지표21, 입소 1회)** 과 **주기·API·테이블이 분리**됩니다.

| 항목 | 내용 |
|------|------|
| FE UI — 이용자 상세 | **`ClientDetailPage`** **「위험도평가」** 탭 — **`ClientPeriodicRiskAssessmentPanel`** — 반기 라벨·3종 폼·**StatCard (N/3)** · G40 패널 **하단** (`22325f4`) |
| FE UI — 지점 현황 | **`PeriodicRiskAssessmentStatusPage`** — **`/clients/periodic-risk-assessments`** — 회계연도·반기·StatCard·미완료 표 · SideNav **「정기욕구평가 현황 (G40b)」** (`7b68f54`) |
| FE UI — 대시보드 | **`DashboardPage`** — **「반기 기초평가 위험도 미완료」** — **`periodicRiskAssessmentGapCount`** — 스냅샷 우선·**`fetchPeriodicRiskAssessmentComplianceApi`** 병렬 폴백 · 클릭 **`/clients/periodic-risk-assessments`** (`22325f4`) |
| 평가 유형 | **`FALL_RISK`** · **`PRESSURE_ULCER`** · **`COGNITIVE_FUNCTION`** — `(organization_id, client_id, fiscal_year, fiscal_half, assessment_type)` **UNIQUE** |
| CRUD | **`GET /api/v1/clients/{clientId}/periodic-risk-assessments?fiscalYear=&fiscalHalf=`** · **`PUT …/periodic-risk-assessments`** |
| compliance | **`GET /api/v1/clients/periodic-risk-assessments/compliance?fiscalYear=&fiscalHalf=&branchId=`** — **`periodicComplete`** · `missingTypes[]` · `gapCount` |
| 검증 | 급여개시일 미등록 **저장 거부** · **`assessedOn`** ∈ **`max(반기시작, ltcCertValidFrom)` ~ 반기종료** · 퇴소·비활성 **저장 거부**(V95 trigger) |
| RBAC | **`hq_admin`·`branch_admin`·`social_worker`** — upsert · **`caregiver`** — read-only |
| DB | **Flyway V95** `client_periodic_risk_assessments` · **V96** — org·branch listing index · **`chk_client_periodic_risk_assessments_recorded_at_after_created`** |
| 테스트 | **`ClientPeriodicRiskAssessmentServiceTest`** · **`MustApiEndpointRoutingTest$ClientRouting`** · **`RoleBasedControllerAccessTest$ClientAccess`** · **`RiskAssessmentPilotServiceFlowE2eTest`**(G40+G40b pilot, `a7b4a39`) · **`ClientPeriodicRiskAssessmentPanel.test`** · **`PeriodicRiskAssessmentStatusPage.test`** · **`periodicRiskAssessmentCompliance.test`** · **`DashboardPage.test`** |
| 접근성 | UXD-91 — **`ClientRiskAssessmentPanel`**·**`ClientPeriodicRiskAssessmentPanel`** 액션 **`aria-label`** 유형·「반기」 컨텍스트 (`fad6df1`) |
| 보관 | **퇴소 후 5년** — `DATA_RETENTION_POLICY.md` · G40(입소 1회)과 cohort 분리 |

> Swagger: **`/swagger-ui.html`** → Clients · Periodic risk assessments. 현장은 **이용자 상세 「위험도평가」**·**정기욕구평가 현황** 우선.

> 관련: FAQ Q302 · USER_MANUAL §3-3·§4-3 · API_SPEC §9-9 · G40(Q301) §6-2-7

### 6-2-9. G-NURSING-PRESSURE-ULCER 욕창 케어 lifecycle (US-O03, BNK-203~204, BE·FE Fixed)

silverangel **욕창위험도·6대 수칙**·케어포 demo L03 **4 leaf** dual-source — **위험평가 → 예방계획 → 일별 간호 기록 → 분기 코호트** 4단 lifecycle. **G40·G40b 위험도평가(지표21·16)** 와 **API·테이블 분리** (v3.1 Must 6번째).

| 항목 | 내용 |
|------|------|
| FE UI | **`PressureUlcerPage`** — **`/nursing/pressure-ulcer/{assessment,plan,records,reports}`** · **`NursingContextNav`** 8탭(통합 바이탈·체중·구강·응급 선행) · **`LifecycleWorkflowPanel`** · **`PressureUlcerAssessmentForm`**·**`PressureUlcerPlanForm`**·**`PressureUlcerCareRecordForm`**·**`PressureUlcerCohortReportPanel`** (`e214da1`/`3ec39f6`) |
| FE services | **`pressureUlcerServices`** — **`fetchPressureUlcerAssessmentsApi`**·**`createPressureUlcerAssessmentApi`**·**`upsertPressureUlcerPreventionPlanApi`**·**`fetchPressureUlcerCareRecordsApi`**·**`createPressureUlcerCareRecordApi`**·**`fetchPressureUlcerComplianceReportApi`** — **`apiFetch` only** (`024e720`) |
| BE API | **`PressureUlcerController`** — **`GET/POST/PATCH /api/v1/nursing/pressure-ulcer/assessments*`** · **`GET/POST /plans`** · **`GET/POST/PATCH /records*`** · **`GET /reports?year=&quarter=`** (`edda491`) |
| 위험평가 | **`CreatePressureUlcerAssessmentRequest`** — `clientId`·`assessedOn`·`riskLevel`(`LOW`/`MODERATE`/`HIGH`)·`scaleScore`(6~23, optional) · **이용자·평가일 UNIQUE** per org |
| 예방계획 | **`UpsertPressureUlcerPreventionPlanRequest`** — `assessmentId`·`preventionPlan`·`planEffectiveFrom`·`carePlanReflected` · **선행 assessment 필수** |
| 간호 기록 | **`CreatePressureUlcerCareRecordRequest`** — `careDate`·`bodySite`·`ulcerStage`(1~4) · **`treatmentNotes` 필수** · **client·date·site UNIQUE** |
| 분기 리포트 | **`PressureUlcerComplianceResponse`** — cohort `items[]`·`assessedCount`·`planEstablishedCount`·`recordedCount`·`gapCount` |
| RBAC | assessments/plans **write**: `hq_admin`·`branch_admin`·`social_worker` · records **write**: +`caregiver` · reports: `hq_admin`·`branch_admin`·`social_worker` · **`guardian` 403** |
| DB | **Flyway V114** — `pressure_ulcer_assessments`·`pressure_ulcer_care_records` — org·branch·client composite FK · risk_level CHECK · scale_score 6~23 · plan pair CHECK · **`d638493`** input guard deepen |
| 테스트 | **`PressureUlcerServiceTest`** · **`PressureUlcerPilotServiceFlowE2eTest`**(4-step, `24a1c5c`) · **`MustApiEndpointRoutingTest$PressureUlcerRouting`** · **`RoleBasedControllerAccessTest$PressureUlcerAccess`** · FE **`PressureUlcerPage.test`**·**`pressureUlcerServices.test`**·**`pressureUlcerLiveApi.e2e.test.js`** · **`pilotPageFlows`** US-O03 |
| 보관 | **퇴소 후 5년** — `DATA_RETENTION_POLICY.md` · G40/G40b risk assessment cohort와 분리 |

> Swagger: **`/swagger-ui.html`** → Nursing · Pressure ulcer. 현장은 **SideNav 기록 → 욕창 케어 (US-O03)** 우선.

> 관련: FAQ Q336~Q339 · USER_MANUAL §5-15 · BENCHMARK_REPORT §204 · G40(Q301) §6-2-7 · G40b(Q302) §6-2-8 · **P2**: L03 나머지 leaf

### 6-2-9a. L03_M11 통합 바이탈 점검 (BNK-207, BE·FE Fixed)

케어포 **view.total_vital_check** — 혈압·맥박·호흡·체온·SpO₂·체중·혈당 **통합 기록**. **G-NURSING 욕창 lifecycle(§6-2-9)** 과 **API·테이블 분리**.

| 항목 | 내용 |
|------|------|
| FE UI | **`NursingVitalCheckPage`** — **`/nursing/vital-checks`** · **`NursingContextNav`** 첫 탭 · **`NursingVitalCheckForm`** · **future check-date guard** (`8570fa2`/`246df56`/`962858b`) |
| FE services | **`nursingVitalCheckServices`** — **`fetchNursingVitalChecksApi`**·**`createNursingVitalCheckApi`**·**`updateNursingVitalCheckApi`** — **`apiFetch` only** |
| BE API | **`NursingVitalCheckController`** — **`GET/POST /api/v1/nursing/vital-checks`** · **`PATCH /{checkId}`** (`80c0bd5`) |
| 요청 필드 | **`CreateNursingVitalCheckRequest`** — `clientId`·`checkDate`·`checkTime` · `systolic`·`diastolic`·`pulse`·`respirationRate`·`temperature`·`spo2` 필수 · `weightKg`·`bloodGlucose`·`notes` 선택 |
| 중복 가드 | **이용자·점검일·시각** UNIQUE per org — 「해당 일시 통합 바이탈 기록이 이미 존재합니다.」 |
| 미래일자 가드 | FE **`validateCheckDateNotFuture`** · BE **`NursingVitalCheckService`** — 「점검일은 오늘 이후로 입력할 수 없습니다.」 (Q344) |
| RBAC | **`hq_admin`·`branch_admin`·`social_worker`·`caregiver`** — list·create·update · **`guardian` 403** |
| DB | **Flyway V115** — `nursing_vital_checks` — org·branch·client composite FK · 범위 CHECK 8종 |
| 테스트 | **`NursingVitalCheckServiceTest`** · **`NursingVitalCheckPilotServiceFlowE2eTest`** · **`MustApiEndpointRoutingTest$NursingVitalCheckRouting`** · **`RoleBasedControllerAccessTest$NursingVitalCheckAccess`** · FE **`NursingVitalCheckPage.test`**·**`nursingVitalCheckServices.test`**·**`nursingVitalCheckLiveApi.e2e.test.js`** |
| 보관 | **퇴소 후 5년** — `DATA_RETENTION_POLICY.md` |

> Swagger: **`/swagger-ui.html`** → Nursing · vital-checks. 현장은 **SideNav 기록 → 통합 바이탈 (L03_M11)** 우선.

> 관련: FAQ Q340~Q342 · USER_MANUAL §5-16 · BENCHMARK_REPORT L03_M11

### 6-2-9b. L03_M14 체중 관리 (BNK-207~209, BE·FE Fixed)

케어포 **view.nursing_weight_manage** — 이용자별 **측정일·체중·신장·목표체중** 기록. **L03_M11 통합 바이탈의 선택 체중 필드와 별도 테이블**.

| 항목 | 내용 |
|------|------|
| FE UI | **`NursingWeightRecordPage`** — **`/nursing/weight-records`** · **`NursingContextNav`** 두 번째 탭 · **`NursingWeightRecordForm`** (`a7f97a6`/`962858b`) |
| FE services | **`fetchNursingWeightRecordsApi`**·**`createNursingWeightRecordApi`**·**`updateNursingWeightRecordApi`** — **`apiFetch` only** (`services.js`) |
| BE API | **`NursingWeightRecordController`** — **`GET/POST /api/v1/nursing/weight-records`** · **`PATCH /{recordId}`** (`e95df4c`/`1a822d2`) |
| 요청 필드 | **`CreateNursingWeightRecordRequest`** — `clientId`·`measureDate`·`weightKg` 필수 · `heightCm`·`goalWeightKg`·`notes` 선택 |
| 중복 가드 | **이용자·측정일** UNIQUE per org |
| 미래일자 가드 | FE **`validateMeasureDateNotFuture`** · BE **`NursingWeightRecordService`** — 「측정일은 오늘 이후로 입력할 수 없습니다.」 (Q344) |
| RBAC | **`hq_admin`·`branch_admin`·`social_worker`·`caregiver`** — list·create·update |
| DB | **Flyway V116** — `nursing_weight_records` |
| 테스트 | **`NursingWeightRecordServiceTest`** · **`NursingWeightRecordPilotServiceFlowE2eTest`** · **`MustApiEndpointRoutingTest$NursingWeightRecordRouting`** · **`RoleBasedControllerAccessTest$NursingWeightRecordAccess`** · FE **`NursingWeightRecordPage.test`**·**`NursingWeightRecordForm.test`** |

> Swagger: **`/swagger-ui.html`** → Nursing · weight-records. 현장은 **SideNav 기록 → 체중 기록 (L03_M14)** 우선.

> 관련: FAQ Q343~Q344 · USER_MANUAL §5-17 · L03_M11 §6-2-9a · §6-2-9c·§6-2-9d

### 6-2-9c. L03_M13 구강상태 점검 (BNK-209, BE·FE Fixed)

케어포 **view.oral_care_check** — 이용자별 **점검일·양치 도움·구강상태·틀니 착용** 기록.

| 항목 | 내용 |
|------|------|
| FE UI | **`NursingOralCareCheckPage`** — **`/nursing/oral-care-checks`** · **`NursingContextNav`** 세 번째 탭 · **`NursingOralCareCheckForm`** (`bb3dee8`/`97108f2`) |
| FE services | **`fetchNursingOralCareChecksApi`**·**`createNursingOralCareCheckApi`**·**`updateNursingOralCareCheckApi`** — **`apiFetch` only** (`services.js`) |
| BE API | **`NursingOralCareCheckController`** — **`GET/POST /api/v1/nursing/oral-care-checks`** · **`PATCH /{checkId}`** (`3540b4f`/`090b2d7`) |
| 요청 필드 | **`CreateNursingOralCareCheckRequest`** — `clientId`·`checkDate`·`brushingAssisted`·`oralConditionStatus`(`GOOD`/`FAIR`/`POOR`) 필수 · `dentureWorn`·`notes` 선택 |
| 중복 가드 | **이용자·점검일** UNIQUE per org — 「해당 일자 구강상태 점검 기록이 이미 존재합니다.」 |
| 미래일자 가드 | FE **`validateCheckDateNotFuture`** · BE **`NursingOralCareCheckService`** · injectable `Clock` (`090b2d7`) — Q344 |
| RBAC | **`hq_admin`·`branch_admin`·`social_worker`·`caregiver`** — list·create·update |
| DB | **Flyway V118** — `nursing_oral_care_checks` |
| 테스트 | **`NursingOralCareCheckServiceTest`** · **`NursingOralCareCheckPilotServiceFlowE2eTest`** · **`MustApiEndpointRoutingTest$NursingOralCareCheckRouting`** · **`RoleBasedControllerAccessTest$NursingOralCareCheckAccess`** · FE **`NursingOralCareCheckPage.test`**·**`NursingOralCareCheckForm.test`**·**`nursingOralCareCheckLiveApi.e2e.test.js`** |

> Swagger: **`/swagger-ui.html`** → Nursing · oral-care-checks. 현장은 **SideNav 기록 → 구강상태 점검 (L03_M13)** 우선.

> 관련: FAQ Q345·Q344 · USER_MANUAL §5-18 · §6-2-9a·§6-2-9b

### 6-2-9d. L03_M04 응급상황 기록 (BNK-211, BE·FE Fixed)

케어포 **view.emergency_history** — **발생일·응급 유형·조치내용·보호자 통보** 기록. **`/health` incident API와 테이블 분리**.

| 항목 | 내용 |
|------|------|
| FE UI | **`NursingEmergencyRecordPage`** — **`/nursing/emergency-records`** · **`NursingContextNav`** 네 번째 탭 · **`NursingEmergencyRecordForm`** (`97108f2`) |
| FE services | **`fetchNursingEmergencyRecordsApi`**·**`createNursingEmergencyRecordApi`**·**`updateNursingEmergencyRecordApi`** — **`apiFetch` only** |
| BE API | **`NursingEmergencyRecordController`** — **`GET/POST /api/v1/nursing/emergency-records`** · **`PATCH /{recordId}`** (`81bca68`/`090b2d7`) |
| 요청 필드 | **`CreateNursingEmergencyRecordRequest`** — `clientId`·`occurrenceDate`·`incidentCategory`·`actionTaken` 필수 · `detail`·`guardianNotified`·`notes` 선택 |
| 유형 CHECK | `FALL`·`CHOKING`·`CARDIAC`·`SEIZURE`·`BLEEDING`·`OTHER` |
| 중복 | **일자 UNIQUE 없음** — 동일 이용자·동일 발생일 **다건** 허용 |
| 미래일자 가드 | FE **`validateOccurrenceDateNotFuture`** · BE **`NursingEmergencyRecordService`** · Asia/Seoul `Clock` — Q344 |
| RBAC | **`hq_admin`·`branch_admin`·`social_worker`·`caregiver`** — list·create·update |
| DB | **Flyway V119** — `nursing_emergency_records` |
| 테스트 | **`NursingEmergencyRecordServiceTest`** · **`NursingEmergencyRecordPilotServiceFlowE2eTest`** · **`MustApiEndpointRoutingTest$NursingEmergencyRecordRouting`** · **`RoleBasedControllerAccessTest$NursingEmergencyRecordAccess`** · FE **`NursingEmergencyRecordPage.test`**·**`NursingEmergencyRecordForm.test`**·**`nursingEmergencyRecordLiveApi.e2e.test.js`** |

> Swagger: **`/swagger-ui.html`** → Nursing · emergency-records. 현장은 **SideNav 기록 → 응급상황 기록 (L03_M04)** 우선.

> 관련: FAQ Q346·Q344 · USER_MANUAL §5-19 · §6-2-9a~§6-2-9c

### 6-2-9f. L03_M01 간호급여 제공기록 (BNK-215, BE Fixed · FE P2)

케어포 **view.nursing_service** (3-1 간호급여 제공기록) — **일별** 간호·투약·진료 제공 여부. **G-NURSING 바이탈·체중·구강·응급 API와 테이블 분리**.

| 항목 | 내용 |
|------|------|
| BE API | **`NursingServiceRecordController`** — **`GET/POST /api/v1/nursing/service-records`** · **`PATCH /{recordId}`** (`9bd1660`) |
| 필드 | **`nursingProvided`·`medicationProvided`·`medicalVisit`** 3-flag + notes · **`medicalInstitution`**(200자) |
| 가드 | **이용자×`serviceDate` UNIQUE** · **3-flag 최소 1 true** · **`serviceDate` future guard** (injectable `Clock`) |
| RBAC | **`hq_admin`·`branch_admin`·`social_worker`·`caregiver`** — **`RoleBasedControllerAccessTest$NursingServiceRecordAccess`** |
| DB | **Flyway V123** — `nursing_service_records` · composite FK·active-client guard |
| FE UI | **없음 (P2)** — Swagger·**`NursingServiceRecordPilotServiceFlowE2eTest`** only |
| 테스트 | **`NursingServiceRecordServiceTest`** · **`MustApiEndpointRoutingTest$NursingServiceRecordRouting`** · **`mvn test` 1131/1131** |

> Swagger: **`/swagger-ui.html`** → Nursing · service-records. **P2**: SideNav **기록 → 간호급여 제공기록** FE wire.

> 관련: FAQ Q348 · USER_MANUAL §5-20 · BENCHMARK_REPORT L03_M01

### 6-2-9e. G34-QUAL 팀장급 자격 검증 (FAQ21837, BNK-179~182, BE·FE Fixed)

이지케어 [**FAQ 21837**](https://ezcare.easyms.co.kr/help/faq.ez?rowid=21837&type=web) **팀장급 요양보호사 자격기준(실무경력 5년)** — 선임 업무수행일지(G34) **선임 지정** 시 FE·BE **이중 검증** + **지점별 compliance 집계 API·패널**입니다.

| 항목 | 내용 |
|------|------|
| 기준 | FAQ21837·고시 제48~58조 — **60개월** 근사 · v1은 **`users.hiredAt`** vs **`logDate`** |
| compliance API | **`GET /api/v1/staff/team-lead-qualification/compliance?branchId=&referenceDate=`** — **`TeamLeadQualificationSummaryResponse`** (`9a8bd2a`) |
| BE save guard | **`TeamLeadQualificationCompliance.deriveStatus`** · **`LeadCaregiverWorkLogService.requireEligibleLeadCaregiver`** — **`POST/PATCH /staff/lead-caregiver-logs*`** — 미충족 **`422 BUSINESS_RULE`** (`726b3de`) |
| FE panel | **`TeamLeadQualificationCompliancePanel`** — StatCard 4종·직원별 표·**`/staff/{id}`** 링크 · **`LeadCaregiverWorkLogPage`** (`574bd08`) |
| FE form guard | **`teamLeadQualificationCompliance.js`** · 선임 지정 **저장 차단** (`443efca`) |
| 입사일 없음 | **`STATUS_UNKNOWN`** — 「입사일이 없어… 확인할 수 없습니다」 — HR lifecycle **`hiredAt`** 등록 필요 |
| 테스트 | **`TeamLeadQualificationComplianceTest`** · **`TeamLeadQualificationPilotServiceFlowE2eTest`** (`997831c`) · **`TeamLeadQualificationCompliancePanel.test`** |

| P2 잔여 | **자격증·교육이수 서류 파일함** · **실무경력 서류 기반 정밀 검증** |

> 관련: FAQ Q319 · USER_MANUAL §5-9 · G34b §6-2-9 · API_SPEC G34

### 6-2-9. G34b 업무수행일지 불러오기·import-draft (FAQ21813, BNK-157, BE·FE Fixed)

이지케어 [**FAQ 21813**](https://ezcare.easyms.co.kr/help/faq.ez?rowid=21813&type=web) **「불러오기」** — 선임 업무수행일지 작성 시 **G24 욕구사정**·**G17 기능회복훈련 계획**·**전월 일지**를 읽어 초안을 채웁니다.

| 항목 | 내용 |
|------|------|
| FE UI | **`LeadCaregiverWorkLogPage`** — **「욕구사정·계획 불러오기」** · **「전월 일지 복제」** — **`leadCaregiverWorkLogImport.js`** (`0ce04ad`·`1b5fabe`) |
| BE import-draft | **`GET /api/v1/staff/lead-caregiver-logs/import-draft?clientId=&logDate=&source=`** — **`LeadCaregiverWorkLogService.buildImportDraft`** (`8487667`) |
| `source` | **`needs_assessment`** — G24 8항목 + G17 최신 계획 · **`previous_month`** — 전월 최신 일지 (`IMPORT_SOURCE_*`) |
| 회계연도 | **`fiscalYearFromLogDate(logDate)`** — 기록 일자 기준 |
| 병합 | **`mergeLeadCaregiverWorkLogImport`**(FE) · draft response **`workContent`·`careNotes`** (BE) — 기존 입력 **append** |
| **cognitive role guard** | FAQ21813 — **`COGNITIVE_EDIT_ROLES`**(`hq_admin`·`branch_admin`·`social_worker`) — import-draft·clone·**create/update** 시 **`caregiver`** 인지·정서·인지활동 구간 **제거/거부** (`b6ecc35`·`994f5ea`, Q306) |
| 테스트 | **`LeadCaregiverWorkLogServiceTest`** · **`LeadCaregiverWorkLogImportPilotServiceFlowE2eTest`** · **`LeadCaregiverWorkLogPage.test`** · **`leadCaregiverWorkLogImport.test`** · **`MustApiEndpointRoutingTest`** · **`RoleBasedControllerAccessTest$LeadCaregiverWorkLogAccess`** |

| P2 잔여 | FAQ21813 **30일 rolling 자동 반영** · FAQ21812 **관리자 라운딩** · K-MMSE·인쇄 |

> 관련: FAQ Q303·Q306 · G34 §1-4 · USER_MANUAL §5-9 · BENCHMARK_REPORT §157

### 6-2-10. G42 — 고충상담 기록 (US-T14, FAQ21814, 케어포 8-8)

이지케어 [**FAQ 21814**](https://ezcare.easyms.co.kr/help/faq.ez?rowid=21814&type=web) **고충상담(수급자/요보사)** · silverangel **지표7** — 접수·상담·**전자결재**·사후관리 기록입니다.

| 항목 | 내용 |
|------|------|
| BE | **`GrievanceCounselingController`** — **`GET/POST/PATCH /staff/grievance-counselings*`** · **`GET …/pending-approval`**(Q309) · **`POST …/{counselingId}/submit`** · **`POST …/{counselingId}/approve`** · **`POST …/{counselingId}/follow-up`** · **`GET …/follow-up/pending`** · **`GET …/follow-up/compliance`** (`bcdc411`·`bcb1d9f`) |
| 결재 | **`DRAFT`** → **`SUBMITTED`**(submit) → **`APPROVED`**(approve) → **사후관리**(follow-up) — **APPROVED 후 수정 불가** |
| 접수 enum | `WRITTEN`·`PHONE`·`SMS`·`IN_PERSON`·`ANONYMOUS_BOX` |
| 대상 enum | `CLIENT`(clientId) · `CAREGIVER`(staffUserId) · `OTHER`(이름만) |
| RBAC | 목록·등록·수정·submit·follow-up — **`hq_admin`·`branch_admin`·`social_worker`** · approve·pending-approval — **`hq_admin`·`branch_admin`** |
| DB | **Flyway V97** `grievance_counseling_records` · **V98** integrity (`6f6094d`) — org·branch composite FK · approval CHECK |
| FE | **`GrievanceCounselingPage`** — **`ComplaintConsultationPanel`**(결재·사후관리 섹션) · **`ComplaintConsultationForm`** — **`ANONYMOUS_BOX` intake** (`8a8b930`) · **`GrievanceFollowUpModal`** (`6012044`·`892450a`·`a7a6004`) |
| 테스트 | **`GrievanceCounselingServiceTest`** · **`GrievanceCounselingPilotServiceFlowE2eTest`** · **`PilotChecklistJwtE2eTest`** · **`ComplaintConsultationPanel.test`** · **`GrievanceFollowUpModal.test`** |

| P2 잔여 | FAQ21814 **서류함 PDF** · **결재함 전용 라우트** · **익명함 별도 라우트** |

> 관련: FAQ Q305 · USER_MANUAL §5-3 · BENCHMARK_REPORT §161 · COMPETITOR_MATRIX G42

### 6-2-11. FAQ21824 — 이용자 계약→청구 lifecycle checklist (BNK-165, Q312)

이지케어 [**FAQ 21824**](https://ezcare.easyms.co.kr/help/faq.ez?rowid=21824&type=web) **재가 수급자 4단 업무흐름**을 **단일 wizard 없이** 모듈별 checklist로 연결합니다 (REQUIREMENTS FAQ21824 Epic · **P2: wizard UI 잔여**).

| 항목 | 내용 |
|------|------|
| FE | **`ClientFaq21824LifecyclePanel`** — **`ClientDetailPage`** **「기본정보」** 탭 상단 (`58256c6`) |
| 단계 | **① 계약·안내문(G14)** · **② 공단등록·계획통보(G38/G37)** · **③ 서비스·RFID(G21/출석)** · **④ 월말 청구·수납(7-x)** |
| 유틸 | **`buildFaq21824LifecycleSteps`** · **`findCarePlanNotificationForClient`** · **`analyzeClientVisitServiceContext`** · **`analyzeClientBillingContext`** |
| hydrate | G14 계약 상태·G38 compliance item·방문일정·청구 이력·출석·**`GET /billing/claims/generation-guard`** 병렬 |
| 링크 | G14·G37·G38·G21·`/billing` **in-page nav** |
| 테스트 | **`faq21824Lifecycle.test`** · **`ClientDetailPage.test`** |

| P2 잔여 | FAQ21824 **단일 wizard** · RFID↔공단계획 **자동 대조** · **9종 안내문 일괄 출력** |

> 관련: FAQ Q312 · Q269 · Q270 · USER_MANUAL §3-3 · REQUIREMENTS FAQ21824

### 6-3. 전사 운영 설정 (`hq_admin` 전담)

`sysadmin`이 아닌 **`hq_admin`**이 변경하는 정책입니다. IT 담당자는 변경 내역을 감사 로그로 확인합니다.

| 설정 | API | 기본값 | 설명 |
|------|-----|--------|------|
| 이용자 본인 QR 체크인 | `PATCH /organization/settings` | `false` | `allowClientSelfCheckin` |
| **청구명세서 생성 기준** | `GET/PATCH /settings/billing` | `ATTENDANCE_SCHEDULE` | `claimGenerationBasis` — 출석 vs NHIS import (US-M03, V63, Q224) |

```json
{ "allowClientSelfCheckin": true }
```

```json
{ "claimGenerationBasis": "NHIS_IMPORT" }
```

#### UI (`/organization/settings`, FE `25f3225`)

| 항목 | 내용 |
|------|------|
| 운영 정책 | WAI-ARIA **`Switch`** — 「이용자 셀프 QR 체크인 허용」 |
| **청구·정산** | **`BillingSettingsPanel`** — **`FilterChips`** 로 **출석 기준** / **공단 엑셀** 선택 · `PATCH /settings/billing` 저장 (Q224) · **「청구시작 기준금액 (G33)」** 1회 설정 — **`BillingStartBalanceOneTimeWarning`·`BillingStartBalanceLockedNotice`** (Q273) · **「미납 정산」** + 정산 후 settings reload (`359cf0c`·`eb48879`, Q270·Q273) |
| 접근 | **`hq_admin` only** — `/settings` 접근 시 `/forbidden` |
| **저장** | 셀프 체크인 — **`GET /organization`** · **`PATCH /organization/settings`** (Q116·Q178) · 청구 기준 — **`GET/PATCH /settings/billing`** · G33 — **`POST /settings/billing/start-balance`** (잠금 후 변경 불가) |

**온보딩 체크리스트**

1. `hq_admin` **조직 설정** 화면에서 셀프 체크인 토글·**청구 생성 기준** 저장 (또는 Swagger).
2. (기존 ERP 이관 시) **G33 청구시작 기준금액** — 엑셀·장부와 대조 후 **1회** 설정 (Q269). 잘못 입력 시 **재설정 불가**.
3. `allowClientSelfCheckin=true`일 때만 `POST /clients/{id}/client-user`·QR 본인 체크인 허용 (Q56·Q113).
4. **`NHIS_IMPORT`** 센터 — 월말 청구 전 해당 월 **NHIS import** 완료 여부 확인 (Q224).
5. **전월 미입금·G33 가드** — `GET /billing/claims/generation-guard` 또는 `/billing` UI 배너로 **CONFIRMED** 잔존 청구·**미정산 G33 미납** 확인 (Q225·Q270).
6. **G33 미납 정산** — **`POST /settings/billing/start-balance/settle`** · **`BillingStartBalanceSettlementModal`** (`359cf0c`, Q270) — **`/organization/settings`** 또는 **`/billing/overdue`** · **`hq_admin`·`branch_admin`**
7. 변경 이력은 `audit_logs`·Organization·billing settings 조회로 확인.

### 6-3-1. 수가표·본인부담 비율 (`hq_admin`)

`/billing/fee-schedules`는 **G9 이용시간 밴드**·**2차원 매트릭스**·**등록·수정·목록·이력**·**NHIS 2026 시드**가 **화면 연동 Fixed** (`FeeSchedulePage`, FE `3f96d95`, FAQ Q91·Q210–Q214). `/billing/copay-rates`는 **조회 UI만** — **저장 미연동**.

| 작업 | API | 본문 예시 |
|------|-----|----------|
| 수가 조회 | `GET /billing/fee-schedules` | 전체 목록 — `FeeScheduleMatrix`·`FeeScheduleTable` |
| 수가 이력 | `GET /billing/fee-schedules/history?year=` | 연도별 버전 — `FeeRateHistoryPanel` |
| 수가 등록 | `POST /billing/fee-schedules` | `{ "year": 2026, "ltcGrade": 3, "durationBand": "H10_13", "dailyRate": 68000, "effectiveFrom": "2026-01-01" }` · **`ltcGrade: 0`** 인지지원등급 (Q311·V99) |
| NHIS seed payloads | `GET /billing/fee-schedules/nhis-seed-payloads?year=` | 미등록 셀 NHIS 참조 payload — **`Nhis2026DaycareRateCatalog`** (`2efc557`, Q311) |
| NHIS seed 일괄 등록 | `POST /billing/fee-schedules/apply-nhis-seeds?year=` | 미등록 **표준+인지지원** 셀 bulk create — **`FeeScheduleSeedApplyResponse`** (`edd2771`, Q311) |
| NHIS 2026 시드 | UI **「공단 2026 수가 시드 (N건)」** | 미등록 **표준+인지지원** 셀 — UI는 셀별 `POST` 반복 · API는 **`apply-nhis-seeds`** 동일 (`edd2771`) |
| NHIS import 선행 | **`FeeScheduleYearCoverage`** (US-G04, Q260) | **`GET /billing/fee-schedules/year-coverage?year=`** — **표준 25칸 gate(항상)** + **인지지원 5칸 gate(활성 `ltcGrade=0` 이용자 있을 때)** · **`POST /billing/imports/nhis` → `422`** (`8bb6583`) |
| 수가 수정 | `PATCH /billing/fee-schedules/{id}` | 이력 보존 — **새 적용일 > 기존 적용일** (forward-only, Q48) |
| 이용자 밴드 | `POST/PATCH /clients` | `{ "durationBand": "H10_13" }` — **신규** 청구 수가 키 |
| 청구 라인 스냅샷 | (자동) | `billing_claim_items.duration_band_snapshot` — V62 · API `durationBandSnapshot` (Q213) |
| 부담 비율 조회 | `GET /billing/copay-rates` | 4구분 기본값 |
| 부담 비율 수정 | `PATCH /billing/copay-rates/{copayType}` | `{ "rate": 0.15 }` — **UI 저장 미연동** |

등록 시 `fee_schedules.created_by`에 행위자 UUID가 V35 트리거로 기록됩니다. Flyway **V61** — `fee_schedules`·`clients`에 `duration_band` CHECK·EXCLUDE 제약. **V62** — 청구 라인 `duration_band_snapshot` + BEFORE INSERT backstop. **지점 관리**(`/branches`)는 `BranchesPage`·SideNav에서 접근 가능합니다 (FAQ Q104). **직원 관리**는 **`/staff`**(`StaffPage`, FE `73f7d39`) — **`StaffRoleSelect`**·필드 검증·목록·등록 UI. **DTO 필드 갭**(`role` vs `roleCode`, `name` vs `displayName`) 시 Swagger 사용 (FAQ Q162).

**이용자·보호자 온보딩 (API-only, Q92)**

| 순서 | API | 담당 |
|------|-----|------|
| 1 | `POST /users` — `roleCode: "guardian"` (보호자 계정 **선행** 생성) | `hq_admin`, `branch_admin` |
| 2 | `POST /clients` — `consentToCollectResidentRegistrationNo: true` + **`primaryGuardian` 필수**(`@NotNull`, `0441a07`, Q268) → `guardian_link_status=LINKED` (V39) | `hq_admin`, `branch_admin`, `social_worker` — **`hq_admin`은 활성 지점 필수** (`208b37e`, Q267) |
| 3 | (선택) `POST /clients/{id}/guardians` — 추가 보호자·대표(`is_primary`) 지정 | 동일 |

V39 DB 트리거: `guardian_clients` INSERT 시 **`LINKED`**, 마지막 연결 DELETE 시 **`PENDING`**. 미연결 활성 이용자는 partial 인덱스 `idx_clients_guardian_link_pending`로 온보딩 감사에 활용합니다.

프론트 `/clients/new`는 2~3단계를 **자동 수행하지 않습니다**. **데모·QA** 시 **`/organization/settings`** **파일럿 테스트 데이터** 카드로 프론트 API 일괄 준비 가능 (FAQ **Q268** — 운영 빌드 기본 비노출). 파일럿 센터 온보딩은 Swagger 체크리스트로 검증하세요 (FAQ Q110).

### 6-4. 지점·계정 비활성화

| 대상 | 처리 | 담당 |
|------|------|------|
| 퇴직 직원 | `PATCH /users/{id}` → `is_active: false` | `hq_admin` / `branch_admin` |
| 폐지 지점 | `PATCH /branches/{id}` → 비활성 | `hq_admin` |
| 해지 Tenant | `PATCH /platform/organizations/{id}` → `active: false` | `platform_admin` |

비활성화 ≠ 즉시 삭제. 보존·파기 일정은 `DATA_RETENTION_POLICY.md`를 따릅니다.

#### 6-4-1. 지점명 중복 정책 (V40)

| 항목 | 내용 |
|------|------|
| DB 제약 | `uq_branches_org_name_lower (organization_id, lower(name))` — V1 case-sensitive UK 대체 |
| 앱 검증 | `BranchService` — `existsByOrganizationIdAndNameIgnoreCase` (등록·수정 시 선행 검사) |
| 현장 의미 | 같은 법인(Tenant) 안에서 **`○○점`과 `○○점`(대소문자만 다름)은 등록 불가** |
| 대칭 정책 | Tenant 이메일 UK `lower(email)` (V30) — FAQ Q146 |

중복 시 API는 `409 CONFLICT` — 「이미 같은 이름의 지점이 있습니다」류 메시지. UI(`/branches`)에서도 동일 오류가 표시됩니다.

---

## 7. 장애 대응·모니터링

### 7-1. 헬스체크

| 엔드포인트 | 용도 | 인증 |
|------------|------|------|
| `GET /api/v1/health` | 애플리케이션 생존 확인 | 불필요 |
| `GET /actuator/health` | Spring Actuator (health, info) | 운영 시 접근 제한 권장 |

### 7-2. 자주 발생하는 증상

| 증상 | 가능 원인 | 조치 |
|------|----------|------|
| 이용자 등록 실패 | `PII_ENCRYPTION_KEY` 미설정 | 환경변수 설정 후 API 재기동 |
| QR 체크인 실패 | `QR_TOKEN_SECRET` 미설정·만료 토큰 | 시크릿 확인, 지점 QR 재생성 |
| 403 `FORBIDDEN_SCOPE` | 역할·지점 스코프 불일치 | JWT `branch_ids`, `active_branch_id` 확인 |
| 401 `UNAUTHENTICATED` | JWT 만료(30분) | 재로그인 또는 refresh |
| 429 `RATE_LIMITED` | 로그인·refresh·비밀번호 재설정 과다 시도 | 1분 후 재시도, IP·계정별 한도 확인 |
| 타 Tenant 데이터 노출 의심 | 테넌트 필터 버그 | 즉시 ops 보고, `TenantContextFilter`·감사 로그 확인 |

### 7-3. 보안 사고 대응 (요약)

1. **격리**: 의심 계정 즉시 비활성화 (`is_active: false`).
2. **증거**: `audit_logs`, `login_history`, `traceId` 수집.
3. **키 로테이션**: 유출 의심 시 `PII_ENCRYPTION_KEY`, `QR_TOKEN_SECRET`, JWT 키 순차 교체.
4. **통보**: Tenant `hq_admin`·ogada security 담당에 보고 (개인정보 유출 시 법정 통지 절차).

---

## 8. 암호화 키 관리

### 8-1. 키 생성

```bash
# 32바이트 랜덤 키 → Base64 (PII_ENCRYPTION_KEY용)
openssl rand -base64 32
```

### 8-2. 키 보관 원칙

- 환경변수 또는 클라우드 **시크릿 매니저**(AWS Secrets Manager, GCP Secret Manager 등)에만 저장.
- `.env`, 소스코드, Slack·이메일에 **저장·공유 금지**.
- 운영·스테이징·개발 **키 분리**.

### 8-3. 키 로테이션 (권장 절차)

1. 새 키를 시크릿 매니저에 등록 (이중 키 기간 운영 — 구현 시).
2. 유지보수 시간대에 애플리케이션 재기동·키 전환.
3. 기존 암호화 데이터 **재암호화 배치** 실행 (v2+ 기능).
4. `audit_logs`에 `KEY_ROTATION` 이벤트 기록.

> MVP v1은 단일 키 운영. 로테이션·재암호화 자동화는 후속 구현입니다.

---

## 9. 데이터 보존·파기 (관리자 참고)

상세 정책은 `docs/ops/DATA_RETENTION_POLICY.md`를 따릅니다. 관리자가 자주 확인하는 항목만 요약합니다.

| 데이터 | 보존 기간 |
|--------|----------|
| 이용자 PII·출석·건강 | 퇴소 후 **5년** |
| 청구·명세 | 청구 연도 기준 **5년** |
| 감사 로그 | **3년** |
| 로그인 이력 | **1년** |
| DB 백업 | **30일** 롤링 |

**Tenant 해지 시**: 정지 → **90일 유예** → 논리 삭제 → 백업 만료 후 물리 삭제.

**퇴소 이용자 purge (배치 후속)**

| 단계 | DB 지원 | 비고 |
|------|---------|------|
| 퇴소 cohort 스캔 | V32 `idx_clients_org_discharged_at` | Tenant 단위 `discharged_at IS NOT NULL` |
| 지점별 cohort 스캔 | V34 `idx_clients_org_branch_discharged_at` | 지점 폐쇄·부분 rollback purge |
| 퇴소 시각 무결성 | V34 `chk_clients_discharged_after_created` | `discharged_at >= created_at` |
| child 행 삭제·익명화 | V33 `idx_*_client_purge` | `attendance`·`health_records`·`billing_claim_items` by `client_id` |
| 배치 실행 | **미구현** | `@Scheduled` retention job 후속 (`DATA_RETENTION_POLICY` §4-1) |

---

## 10. API 빠른 참조 (관리자)

Base URL: `/api/v1` | 인증: `Authorization: Bearer <access_token>`

### 10-1. 플랫폼 (`platform_admin`)

| 메서드 | 경로 | 설명 |
|--------|------|------|
| GET | `/platform/organizations` | Tenant 목록 (`?query=` 검색 지원) |
| POST | `/platform/organizations` | Tenant 생성 |
| GET | `/platform/organizations/{orgId}` | Tenant 상세 |
| PATCH | `/platform/organizations/{orgId}` | 요금제·활성 상태 |
| POST | `/platform/organizations/{orgId}/admins` | 첫 `hq_admin` 발급 |

### 10-2. 시스템 설정 (`sysadmin` — 구현됨)

| 메서드 | 경로 | 설명 |
|--------|------|------|
| GET | `/settings/system` | 기술 설정 조회 |
| PATCH | `/settings/system` | `backupEnabled`, `auditRetentionDays` 변경 |
| GET | `/settings/audit-logs` | 감사 로그 (page, size) |
| GET | `/settings/backups` | 백업 실행 이력 |

### 10-3. 조직 (`hq_admin` / `sysadmin` 조회)

| 메서드 | 경로 | 설명 |
|--------|------|------|
| GET | `/organization` | 현재 Tenant 정보 |
| PATCH | `/organization/settings` | 전사 정책 (`hq_admin` only) |

### 10-4. 청구 (`hq_admin` / `branch_admin` — 구현됨)

| 메서드 | 경로 | 설명 |
|--------|------|------|
| GET | `/billing/claims` | 청구 목록 (`?branchId=`, `?status=` — `DRAFT`/`CONFIRMED`/`PAID`) |
| GET | `/billing/claims/generation-guard` | 전월 미입금 사전 점검 (`?branchId=`, `?yearMonth=`, US-M03, Q225) |
| GET | `/billing/monthly-benefit-caps` | **2026 재가급여 월한도액** 참조표 (`?year=`, BNK-47, Q226) |
| GET | `/billing/claims/monthly-cap-guard` | 월한도 초과 **경고**(non-blocking, `?branchId=`, `?yearMonth=`, Q226) |
| GET | `/billing/fee-surcharge-rates` | **G11 가산율 catalog** — MOHW 2026 참조표 (Q229) |
| POST | `/billing/fee-surcharge-preview` | **G11 가산 미리보기** — `{ baseAmount, surchargeCode }` (Q229) |
| POST | `/billing/claims/generate` | 월별 청구서 생성 — **`claimGenerationBasis`**·전월 가드 적용 (Q224·Q225) |
| POST | `/billing/imports/bank-deposits` | 은행 입금 엑셀 **일괄 수납** (`multipart`, 케어포 7-2, Q227) |
| PATCH | `/billing/claims/{claimId}/status` | 상태 전이 (DRAFT→CONFIRMED→PAID) |
| GET | `/settings/billing` | 청구 생성 기준 조회 (`hq_admin`·`branch_admin`, Q224) |
| PATCH | `/settings/billing` | 청구 생성 기준 변경 (`hq_admin`, V63) |
| POST | `/billing/imports/nhis` | 공단 엑셀 import — **귀속 연도 수가표 25칸 완비 필수** (US-G04, `FeeScheduleYearCoverage`, Q260) |
| GET | `/billing/fee-schedules/year-coverage` | NHIS import **사전 점검** — `?year=` → `{ registered, expected, complete, message }` (US-G04, `8f208e4`, Q260) |
| GET | `/billing/reports/{variant}` | **본인부담 대장** — `variant`: `charges` \| `deposits` \| `receipts` \| `refunds` · `?month=YYYY-MM&branchId=&q=&page=&size=` (US-M03, `de49b21`, Q179) |
| GET | `/billing/claims/{claimId}/nhis-comparison` | **NHIS 사전 대조** — 청구 라인별 **서비스일수·공단부담금·본인부담금** vs 최신 import (`2225a7a`·`18f5173`, BNK-87·BNK-91 P2, Q264) — **`BillingDetailPage` `DRAFT` 패널만** |
| POST | `/billing/claims/{claimId}/refunds` | **본인부담 환불** — `{ refundedAt, amount?, reason? }` · **`PAID`→`REFUNDED`** · 금액=본인부담금 일치 필수 (US-M03 7-9, V71, Q261) |

**NHIS 청구 사전 대조 (BNK-87, Q264)**

| 응답 | 의미 |
|------|------|
| `nhisBatchPresent` | 해당 청구월 NHIS import 배치 존재 |
| `matchedLineCount` / `discrepancyLineCount` / `missingNhisLineCount` | 일치·불일치·NHIS 미매칭 라인 수 |
| `items[]` | 이용자별 `internalServiceDays`·`nhisServiceDays`·`internalNhisAmount`·`nhisImportAmount`·**`internalCopayAmount`**·`nhisMatchStatus` |

권한: **`hq_admin`·`branch_admin`**. FE: **`BillingNhisComparisonPanel`** — `DRAFT` 전용(확정 청구 **패널 미렌더**) · StatCard·비교 표 · **공단 초과/부족 Badge** · reconciliation 링크 · `nhisBatchPresent=false` 안내. 테스트: **`BillingServiceTest.getClaimNhisComparison*`** · **`BillingNhisComparisonPanel.test`** · **`BillingDetailPage.test`** · **`pilotPageFlows`** · **`RoleBasedControllerAccessTest$BillingAccess`**.

**환불 상태 전이 (V71)**

| from | to | 비고 |
|------|-----|------|
| `PAID` | `REFUNDED` | `paidAt`·`paymentMethod`·`refund_*` 메타데이터 필수 |
| `REFUNDED` | — | 금액·월·지점 **불변** (트리거) |

환불 후 **`getMedicalExpenseDeduction`** 집계에서 **제외**됩니다 (G26, Q252).

### 10-5. NHIS reconciliation (`hq_admin` / `branch_admin` — 구현됨)

| 메서드 | 경로 | 설명 |
|--------|------|------|
| GET | `/billing/imports/nhis/guidance` | **import 온보딩 안내** — 롱텀 2026 Chrome/Edge 필수·export 절차·「처리상태」열 안내 (정적, DB 미사용) |
| GET | `/billing/imports/nhis` | import 배치 목록 (`?branchId=&yearMonth=&claimId=`) |
| GET | `/billing/imports/nhis/{batchId}` | 배치 상세 + 행별 `matchStatus` (`yearMonth`, `rowCount`, `matchedCount`, `rows[]`) |
| GET | `/billing/imports/nhis/{batchId}/candidates` | `UNMATCHED` 행 수동 매칭 후보 검색 |
| PATCH | `/billing/imports/nhis/rows/{rowId}/match` | `{ "clientId" }` — `UNMATCHED` → `MATCHED`/`DISCREPANCY` |

**행별 `matchStatus` (G7, V54, FAQ Q181)**

| 상태 | 의미 | 수동 매칭 |
|------|------|----------|
| `MATCHED` | 일치 | — |
| `UNMATCHED` | 이용자 미매칭 | `PATCH …/match` 가능 |
| `DISCREPANCY` | 금액·일수 불일치 | 비교 Modal (FE) |
| `PENDING_REVIEW` | 공단 처리 대기·보류 | **불가** — `match_status_reason` 안내 후 재import |

엑셀 **「처리상태」** 열이 `대기`·`보류`·`pending`·`검토중` 등이면 `NhisReconciliationMatcher`가 `PENDING_REVIEW`로 분류합니다. DB CHECK·`match_status_reason` NOT NULL은 **V54**입니다.

**프론트 UXD-58 (FAQ Q181·Q182)**: **`ReconciliationPage`** — 상단 **StatCard** 4종(일치·차이·미매칭·대기) · **`NhisPendingReviewGuide`**(대기 행 ≥1) · **`NhisReconciliationTable`** **「보류 사유」**열. 배치 응답 **`pendingReviewCount`** 우선 사용.

**프론트 필드 정합 (FAQ Q100–Q101)**: 목록·대사 UI는 `targetMonth`·`billingDays`·`billingAmount` 등을 기대하나 API는 `yearMonth`·`serviceDays`·`nhisAmount`·`amountDifference`를 반환합니다. 수동 매칭 API는 정상 동작합니다.

**롱텀 export 안내 (FAQ Q111)**: `GET /billing/imports/nhis/guidance` 응답 예 — `browserRequirement`(Chrome/Edge 필수), `exportSteps[]`, `leadingStatusColumnNote`(처리상태 열 자동 스킵). import 화면 UI는 아직 미연동.

### 10-7. 보호자 알림 수신 설정 (`guardian` / `client_user` / 직원 대리 — V41 + V42, B08 Fixed)

| 구분 | 메서드 | 경로 | 권한 |
|------|--------|------|------|
| **보호자 본인** | `GET` / `PUT` | `/guardian/notification-preferences` | `guardian`, `client_user` |
| **직원 대리** | `GET` / `PUT` | `/clients/{clientId}/guardians/{guardianUserId}/notification-preferences` | `branch_admin`, `social_worker` |

채널: `channelInApp`·`channelPush`·`channelEmail`·`channelKakao`·`channelSms`. 이벤트: `notifyAttendance`·`notifyDailyCare`·`notifyBilling`·`notifyEmergency`. 카카오·SMS on 시 V42 `consent_at` 자동 기록 (FAQ Q142). **방해 금지**는 preference가 아닌 **NotificationService** 22:00–08:00 KST (FAQ Q147).

### 10-8. 보호자 알림 발송 (J03, `c53dd3b`)

| 항목 | 내용 |
|------|------|
| 서비스 | `NotificationService.dispatchClientEvent` |
| 트리거 | `AttendanceService`(체크인/아웃) · **`BillingService`** · **`HealthRecordService`** — **`createVitals`·`createMedication`·`createNote` → DAILY_CARE**, `createIncident`(긴급) → **EMERGENCY** |
| 이벤트 | `ATTENDANCE_CHECK_IN` · `ATTENDANCE_CHECK_OUT` · **`BILLING`** · **`BILLING_PAYMENT_RECEIVED`** (`CONFIRMED`→`PAID`, `52e0621`) · **`DAILY_CARE`** · **`EMERGENCY`** |
| 수신자 | **자동 이벤트** — **대표 보호자 우선 1명** · 부 보호자 fallback (`resolveDispatchTarget`, Q272) · **`GuardianPhoneResolver`** — V44 `users.phone_encrypted` (알림톡/SMS) · **`GuardianEmailResolver`** — `users.email` (email, Q204) |
| Provider | **`stub`**(기본) — **`StubEmailProvider`**(email, default) · **`SmtpEmailProvider`**(email, `NOTIFICATION_EMAIL_PROVIDER=smtp`, Q204) · **`SolapiKakaoAlimtalkProvider`**·**`SolapiSmsProvider`**(kakao/sms) |
| **이메일 본문** | **`EmailNotificationContent`** — `[ogada]` subject · 출석·DAILY_CARE·EMERGENCY·**엔젤 패리티 5종**(명세·급여제공기록지·가정통신문·**학대예방 지침**·**납부확인서**) — **`formatWon`** · **`paidAt`·`paymentMethod`** (`588b8e6`, Q221) |
| **서류 수동 발송** | **`GuardianDocumentNotificationService`** — care-provision · home-newsletter · **elder-abuse-prevention-guideline** — **`GuardianDocumentNotifyPanel`** UI (Q222) |
| **납부확인서 재발송** | **`BillingService.notifyPaymentReceipt`** — **`POST /billing/claims/{id}/payment-receipt-notify`** — **`PAID`+`paidAt` 필수** · **`BillingDetailPage`** UI (Q221) |
| **SMTP 검증** | **`f23f15a`** — guardian email 형식 불량 → dispatch skip · blank/invalid **`NOTIFICATION_EMAIL_FROM`**·**`NOTIFICATION_EMAIL_REPLY_TO`** → **기동 실패** |
| **Solapi 템플릿 검증** | **`98e40a3`** — `NOTIFICATION_PROVIDER=solapi` 시 **`KAKAO_TPL_*` 값이 내부 코드명 placeholder**(예: `ATTENDANCE_ARRIVAL` 그대로)이면 **기동 실패** — Solapi 승인 **templateId** 필수 (Q266, DEPLOYMENT §4-3) |
| **채널 readiness** | **`GET /notifications/channel-status`** — Solapi·SMTP **configured 여부**·**`liveAlimtalkDispatchReady`·`liveEmailDispatchReady`**·**`quietHoursActive`**(KST 22:00–08:00)·필수 템플릿 누락 — **비밀값 미노출** (`fffd355`·`229f84c`, Q318) |
| **조용한 시간대 (quiet hours)** | **`NotificationService.isQuietHoursAt`** — **22:00 ≤ 시각 < 08:00 Asia/Seoul** · **non-emergency dispatch skip** · **`EMERGENCY` bypass** · 경계 **22:00·07:59** 단위 테스트 (`328874d`·`9a4ab8e`, Q329) |
| **청구 UI quiet-hours guard** | **`BillingDetailPage`**·**`OverduePage`** — **`notificationQuietHours.js`** — 발송 버튼 **비활성** + Alert · **`interpretBillingNotifyResult`** (`111f056`, Q329) |
| **readiness UI** | **`NotificationChannelReadinessPanel`** — **`/organization/settings`**(`hq_admin`) · **`DashboardPage`**(`hq_admin`·`branch_admin`) — **`notificationChannelStatus.js`** (`6b1258c`·`d695923`) · **UXD-97** — **`.ds-dl-grid`** · Solapi/SMTP/템플릿 **`<h3>` 섹션 제목** (`76b5ff0`) |
| **RBAC** | **`@PreAuthorize("hasAnyRole('HQ_ADMIN','BRANCH_ADMIN')")`** — `sysadmin` **403** |
| **템플릿 변수** | **`AlimtalkTemplateVariables`** — `notifications.payload` → Solapi `kakaoOptions.variables` (출석·DAILY_CARE·EMERGENCY·청구·**수납**, Q157·Q159). **`incidentType` → `category`** alias (`ac17ad8`) |
| **SMS fallback** | **`AlimtalkFallbackText`** — 알림톡 실패 시 **한국어 SMS relay 본문** 생성 — 내부 templateCode·UUID **미노출** (Q158) |
| 설정 | `NOTIFICATION_PROVIDER` · `NOTIFICATION_EMAIL_PROVIDER` · `NOTIFICATION_EMAIL_FROM` · `NOTIFICATION_EMAIL_REPLY_TO` · `SMTP_*` · `SOLAPI_*` · `KAKAO_PF_ID` · `KAKAO_TPL_*` |
| 이력 저장 | `notifications` — V45 `sent_at` CHECK (FAQ Q150) |
| **이력 조회** | **`GET /guardian/notifications`** · **`GET /clients/{clientId}/notifications`** — `NotificationHistoryService` · **`NotificationHistoryPanel`** UI (FAQ Q152·Q187) |
| 테스트 | **`NotificationServiceTest`**(+quiet-hours boundary, Q329) · **`NotificationServiceTest`**(+91 primary dispatch, Q272) · `SolapiKakaoAlimtalkProviderTest` · **`AlimtalkTemplateVariablesTest`** · **`AlimtalkFallbackTextTest`** · **`NotificationAlimtalkDispatchE2eTest`** · **`J03AlimtalkServiceFlowE2eTest`** · **`J03EmailServiceFlowE2eTest`** · **`EmailNotificationContentTest`** · **`GuardianDocumentNotificationServiceTest`** · **`StubEmailProviderTest`** · **`SmtpEmailProviderTest`** · **`NotificationHistoryServiceTest`** · FE **`notificationQuietHours.test`** · **`BillingDetailPage.test`** · **`OverduePage.test`** |

스테이징 스모크 (stub): preference **`channelEmail=true`** 또는 `notifyAttendance=true` → 체크인 → `notifications` 1건·`channel=email` 또는 `kakao`·`sent_at` NOT NULL → **`GET /guardian/notifications`** 로 이력 확인 (DEPLOYMENT §8-1). **live SMTP** — DEPLOYMENT §4-8. **EMERGENCY**는 방해 금지(22:00–08:00) **우회**(FAQ Q147).

### 10-9. 알림 발송 이력·서류 이메일 API (J03 + G2, `c53dd3b`·`f77a268`)

| 구분 | 메서드 | 경로 | 권한 |
|------|--------|------|------|
| 보호자 본인 | `GET` | `/guardian/notifications?page=&size=` | `guardian` |
| 직원(이용자별) | `GET` | `/clients/{clientId}/notifications?page=&size=` | `branch_admin`, `social_worker` |
| **급여제공기록지 발송** | `POST` | `/clients/{clientId}/notifications/care-provision-record` | `branch_admin`, `social_worker` |
| **가정통신문 발송** | `POST` | `/clients/{clientId}/notifications/home-newsletter` | `branch_admin`, `social_worker` |
| **노인학대예방 지침 발송** | `POST` | `/clients/{clientId}/notifications/elder-abuse-prevention-guideline` | `branch_admin`, `social_worker` |
| **납부확인서 재발송** | `POST` | `/billing/claims/{claimId}/payment-receipt-notify` | `hq_admin`, `branch_admin` |

**서류 발송 요청 (`GuardianDocumentNotifyRequest`)**

```json
{ "yearMonth": "2026-06", "summary": "요약 본문 (500자 이하, 선택)" }
```

- **Tenant 격리**: JWT `organization_id` + 지점 스코프(직원 API).
- **응답**: 이력 — `NotificationHistoryPageResponse` · 발송 — `GuardianDocumentNotifyResponse` (`clientId`, `templateCode`, `yearMonth`).
- **프론트**: **`NotificationHistoryPanel`** — 보호자 `/guardian` **「알림 이력」** 탭 · 직원 `/clients/:id` **「보호자 알림 이력」** 카드 — **연락처 비표시**(PIPA, Q187). **`GuardianDocumentNotifyPanel`** — 노인학대예방 지침 **UI Fixed**(Q222). **`BillingDetailPage`** — 납부확인서 **UI Fixed**(Q221). 급여제공기록지·가정통신문 **UI 후속** (Q216·Q217). Vitest **`GuardianDocumentNotifyPanel.test`**·**`BillingDetailPage.test`**.

### 10-10. 배차·이동경로 API (v1.3-A + v1.3-B suggest, `53a1ffe`·`db94a65`, V47·V120·V122)

| 메서드 | 경로 | 설명 | 권한 |
|--------|------|------|------|
| GET | `/transport/roster?runDate=&direction=PICKUP` | 당일 배차 명단 (`uses_transport=true`) | `hq_admin`·`branch_admin`·`social_worker`·`caregiver` |
| GET | `/transport/runs?runDate=&direction=PICKUP` | 운행 루트 목록 | 동일 4역할 |
| POST | `/transport/runs` | DRAFT 루트 생성 | **`hq_admin` only** |
| **POST** | **`/transport/runs/suggest`** | **v1.3-B 자동 배차 제안** — OR-Tools VRP · **PICKUP only** · DRAFT runs 생성 (`db94a65`, Q347) | **`hq_admin` only** |
| **GET** | **`/transport/settings`** | **v1.3-B 지점 배차 최적화 설정** 조회 | **`hq_admin` only** |
| **PUT** | **`/transport/settings`** | 픽업 허용분·OR-Tools 가중치 저장 | **`hq_admin` only** |
| GET | `/transport/runs/{runId}` | 루트 상세 | 동일 4역할 (`CONFIRMED`만 직원 조회) |
| PATCH | `/transport/runs/{runId}` | DRAFT 정차 순서 수정 | **`hq_admin` only** |
| POST | `/transport/runs/{runId}/confirm` | DRAFT → **CONFIRMED** | **`hq_admin` only** |
| PATCH | `/transport/runs/{runId}/unconfirm` | **CONFIRMED** → DRAFT (재편집 허용) | **`hq_admin` only** |
| POST | `/transport/runs/{runId}/unconfirm` | 위와 동일 (**레거시 alias**, Q164) | **`hq_admin` only** |
| POST | `/transport/geocode` | Kakao REST 주소→좌표 proxy | **`hq_admin` only** |
| GET | `/transport/contracts/{clientId}` | G15 이동서비스 계약서 조회 | `hq_admin`·`branch_admin`·`social_worker`·`caregiver` |
| PUT | `/transport/contracts/{clientId}` | G15 수칙 5항목·이중 서명 저장 | `hq_admin`·`branch_admin`·`social_worker` |

| 규칙 | 내용 |
|------|------|
| 정차 상한 | **15명** (`MAX_TRANSPORT_STOPS`) — 초과 시 `422 BUSINESS_RULE` |
| 상태 | `DRAFT`(hq_admin 편집) → `CONFIRMED`(직원 읽기 전용) · **unconfirm**으로 DRAFT 복원 (Q163) |
| 스키마 | **V47** — `clients.uses_transport`·픽업 주소·좌표·`transport_runs`·`transport_run_stops`·`unconfirmed_at`/`unconfirmed_by` · **V64** — `transport_service_contracts` (Q231) · **V65** — contract integrity guard·서명 CHECK·purge 인덱스 (Q235) · **V120** — `branch_transport_settings`·`transport_suggest_events`·`clients.transport_notes` · **V122** — suggest integrity·v1.3-A null-vehicle UK |
| **v1.3-B suggest (Q347)** | **`TransportSuggestService.suggestRuns`** — roster geocode 필수 · **지점당 일 10회** (`ogada.transport.suggest-daily-limit-per-branch`) · **`RoleBasedControllerAccessTest$TransportAccess.suggestRunsShouldAllowHqAdmin`** · **`MustApiEndpointRoutingTest$TransportRouting`** · **FE Fixed** (`TransportSuggestPanel`·`BranchTransportSettingsPanel`, `2ffe59f`) |
| 지도 | **`KAKAO_REST_KEY`** 미설정 시 geocode 비활성 — DEPLOYMENT §4-6 |
| 이용자 프로필 | **`POST/PATCH /clients`** — `usesTransport`·`pickupAddress`·`pickupContact`·`defaultPickupTime` **Fixed** (`1ec538b`, Q166) · **`ClientFormPage`·`ClientTransportProfileSection` UI Fixed** (`3c55339`) · 응답 `pickupAddressMasked`·`pickupContactMasked` · 주소 변경 시 geocode 캐시 무효화 |
| **PII 마스킹** | **non-`hq_admin`** roster·확정 run detail — `pickupAddress` **시·구 + ` ***`** (`e7d4cf6`) · `pickupContact` **`010-****-5678`** (`c7941e9`, Q169) · `hq_admin` 편집 응답은 평문 |
| **geocode 실패 가드 (QA-B19)** | **`countGeocodeFailures`** — `geocode_status=FAILED` **또는 `lat`/`lng` 미보유** 정차 시 **임시 저장·순서 저장·배차 확정 차단** · **`Alert id=transport-geocode-warning`** · `aria-describedby` (`318411d`·`48d90d5`, Q233) |
| 프론트 | **`TransportUnconfirmModal`** + 루트 상세 **「확정 취소」** (`hq_admin`, UXD-47, Q163) · **배차 forced-colors a11y**(UXD-50, Q168) · **`TransportPickupContact`** 역할별 `tel:` 링크(UXD-52, Q171) · **`pilotPageFlows` T03 E2E**(Q172) |
| RBAC | **`RoleBasedControllerAccessTest$TransportAccess`** — roster `caregiver` 허용·`guardian` 거부 · create/unconfirm **`hq_admin` only** · get/list `caregiver` 허용 (Q168) |

| **G15 compliance** | **`TransportCompliancePanel`** — 5항목 수칙·계약서 Modal · **`fetchTransportContractApi`·`saveTransportContractApi`** (`9e3cab5`, Q230·Q231) · **V65** — 퇴소·비활성·비이동서비스·지점 불일치 거부 (Q235) · **`caregiver` 저장 불가** |
| **G15 service log (FE)** | **`TransportServiceLogPanel`** — 확정 배차 **별지 제22호** 인쇄·`.txt` 다운로드 (`7389884`) · 정차별 실제 픽업·동승·**15분 준수** 집계 (`eef07e5`, Q236) · **클라이언트 메모리 only** — 서버 영속화 미구현 |
| **G15 Form18 guide (FE)** | **`TransportForm18GuidePanel`** — **5단계** + **3분리 신청 유형** + **등록상태 4단** (`fcf713a`, Q237) · **`transportForm18.js`** · **`/transport`** + **`/transport/service-fees`** · **자동 제출 없음** |
| **G16 service-fee (BE·FE partial)** | **`TransportServiceFeeService`** — BNK-25 RU_1~4 seed · **1일 1회** UNIQUE · contract signed guard · **cross-branch update guard** (`b5218a9`, Q247) · **V68** · **`TransportServiceFeePanel`** (`88d4c59`·`9dfef92`, Q239) |
| **G16 vehicles** | **`VehicleService`** · **`VehiclesPage`** · **`TransportVehicleSelect`** — plate UK · capacity 1–15 · run assignment (`bd375e6`·`107bfb3`·`08dbcf0`, Q241) |
| **G15 care-provision** | **`CareProvisionRecordService`** — 확정 배차·출석·차량 조인 · **`CareProvisionRecordPanel`** (`8bdead6`·`08dbcf0`, Q243) |
| **G15 outings (BE·FE)** | **`ClientOutingService`** — PLANNED→OUT→RETURNED lifecycle · **`GET /reports/client-outings`** · **V67** · **`ClientOutingPanel`** (`7dfcc9e`·`a0dcfc0`, Q240) |
| **G2 paidAt on PAID** | **`BillingService.updateClaimStatus`** — `paidAt`·`paymentRecordedBy` 자동 (`e16534c`, Q244) |
| 테스트 | **`NhisImportGuidanceTest`** · **`TransportServiceFeeServiceTest`**(cross-branch) · **`CareProvisionRecordServiceTest`** · **`TransportServiceTest`** · **`mvn test` 503/503** · Vitest **144/547** |

> **운영 편의용** — v1.3-A **배차·지도** + v1.3-C **계약·일지·G16 청구·외출·차량·급여제공 조회** Fixed + v1.3-B **suggest API·FE wire** (Q347). **공단 포털 자동 제출·급여제공 발송 UI**는 후속 (Q237·Q216).

### 10-11. 식사·프로그램 API (v3, `dfd9be2`, V49)

| 메서드 | 경로 | 설명 | 권한 |
|--------|------|------|------|
| GET | `/meals/menus?date=` | 당일 식단 (`BREAKFAST`/`LUNCH`/`SNACK`) | `hq_admin`·`branch_admin`·`social_worker`·`caregiver` |
| POST | `/meals/menus` | 식단 등록 — `menuDate`·`mealType`·`menuName`·`calories`(선택) | **`hq_admin`·`branch_admin`** |
| GET | `/meals/records?date=` | 이용자별 섭취 기록 | 동일 4역할 |
| POST | `/meals/records` | 섭취량·식이 제한·영양사 소견 기록 | 동일 4역할 |
| GET | `/programs/schedule?date=` | 당일 프로그램 일정 | 동일 4역할 |
| POST | `/programs/schedule` | 일정 등록 — `scheduleDate`·`programName`·시간 등 | **`hq_admin`·`branch_admin`** |
| GET | `/programs/participations?date=` | 참여·만족도·**`skipReason`** 기록 | 동일 4역할 |
| POST | `/programs/participations` | 참여(`ATTENDED`/`ABSENT`)·만족도(1~5)·**`skipReason`**(G17b) 등록 | 동일 4역할 |

| 규칙 | 내용 |
|------|------|
| 스키마 | **V49** — `meal_menus`·`meal_records`·`activity_programs`·`program_participations` · **V113** — `skip_reason`·`COGNITIVE` program_type |
| UK | 섭취: `client_id`×`record_date`×`meal_type` · 참여: `client_id`×`program_id`×`record_date` |
| 만족도 | `ATTENDED` → `satisfaction` 1~5 **필수** · `ABSENT` → `satisfaction` **NULL** (`3bd6a43` — ABSENT에 satisfaction 입력 **거부**) |
| **G17b skipReason** | **`COGNITIVE` + `ABSENT`** → `skipReason` **`STAFF_SHORTAGE`·`EQUIPMENT_FAILURE`·`CLIENT_REFUSAL`·`OTHER` 중 1 필수** · 그 외 status/type 조합에 skipReason 입력 **거부** (`ProgramService.resolveSkipReason`, Q333) |
| 퇴소 가드 | V49 트리거 — 비활성·퇴소 이용자 INSERT **거부** |
| actor | `recorded_by`·`created_by` — V49 session actor backstop |
| FE UI | **`MealMenuForm`·`ProgramScheduleForm`** — `hq_admin`·`branch_admin` 조건부 (FE `1794e1c`, Q161 Fixed) · **`ProgramParticipationForm`** G17b Field (`c26cfa7`) · **`ProgramsPage`** skipReason 열 (`487416d`, Q334) |
| 테스트 | **`MealServiceTest`** · **`MealControllerRoutingTest`** POST 포함 · **`ProgramServiceTest`**(+skipReason·ABSENT satisfaction, `3bd6a43`) · **`ProgramControllerRoutingTest`** · **`MustApiEndpointRoutingTest$MealsRouting`**·**`$ProgramsRouting`** · FE **`ProgramParticipationForm.test`**·**`ProgramsPage.test`**·**`pilotPageFlows`** G17b |

> **운영**: **`hq_admin`·`branch_admin`** 은 `/meals`·`/programs` 화면에서 당일 식단·일정을 등록합니다. USER_MANUAL §5-9 참고.

#### 10-11-1. 기능회복 훈련 API (G17, US-T06, `73e169a`·`0821ce8`·`0048105`·`e820b28`, V72) — **FE UI Fixed**

MOHW **평가 지표 25–27** 대응. **`FunctionalRecoveryPage`**(`/programs/functional-recovery`)에서 StatCard·계획 목록·등록 폼을 제공합니다. **`mapFunctionalRecoveryComplianceView`** 가 API count 필드를 UI StatCard에 매핑합니다 (`0821ce8`·`21b1855`·`7450161`). **`DashboardPage`** 에 지표27 gap·상태 위젯이 silverangel **row3 verbatim** 라벨로 연동됩니다 (`7450161`, Q271).

| 메서드 | 경로 | 설명 | 권한 |
|--------|------|------|------|
| GET | `/programs/functional-recovery/plans?year=&clientId=` | 이용자별 **연간 기능회복 계획** 목록 | `hq_admin`·`branch_admin`·`social_worker`·`caregiver`(조회) |
| POST | `/programs/functional-recovery/plans` | 계획 등록 — `clientId`·`planYear`·`planContent`·`includesCarePlan`·**`cognitiveActivityProvided`**·**`cognitiveActivityNotProvidedReason`**·`annualExecutionDate` | `hq_admin`·`branch_admin`·`social_worker` |
| PATCH | `/programs/functional-recovery/plans/{planId}` | 계획 수정 — 동일 필드 | 동일 3역할 |
| GET | `/programs/functional-recovery/compliance?year=` | 지표 25–27 + **`provisionRecordedMet`** · **`planEstablishedBeforeBenefitStartMet`** 충족 요약 | `hq_admin`·`branch_admin`·`social_worker` |

| 규칙 | 내용 |
|------|------|
| 스키마 | **V72** — `functional_recovery_plans` · **`activity_programs.program_type`** `GENERAL` \| `FUNCTIONAL_RECOVERY` \| **`COGNITIVE`** (V113) · **V112** — `cognitive_activity_provided`(default TRUE) · `cognitive_activity_not_provided_reason` |
| UK | `organization_id`×`client_id`×`plan_year` — 이용자·연도당 계획 1건 |
| **G17b cognitive (V112)** | **`cognitiveActivityProvided=true`** → reason **NULL** · **`false`** → **`cognitiveActivityNotProvidedReason` trim>0 필수** — DB CHECK + FE `Field` 검증 (Q335) |
| **지표27 row 2** | **`provisionRecordedMet`** — 해당 연도 **기능회복훈련 출석·기록** 존재 (`e820b28`) |
| **지표27 row 3** | **`planEstablishedBeforeBenefitStartMet`** — plan `createdAt` **< `ltcCertValidFrom`** (`0048105`) |
| **등록 가드** | **오늘 ≥ `ltcCertValidFrom`** 이면 **`POST …/plans` → `422`** (`e820b28`) · FE **`isFunctionalRecoveryPlanCreateBlocked`** 사전 비활성 (BNK-102) — **수정(`PATCH`) 시 생략** (Q279) |
| FE UI | **`FunctionalRecoveryPage`** — **G17b cognitive Switch+Textarea** (`c26cfa7`, Q335) · 목록 **「인지활동형 (G17b)」** Badge · **「수정」** → **`PATCH`** (`26499b3`, Q279) · **`RecordsContextNav`** · **`DashboardPage`** gap 위젯 · **`functionalRecoveryCompliance.js`** verbatim 라벨 · **`FunctionalRecoveryPage.test`**·**`dashboardSummary.test`** · **`pilotPageFlows`** G17b functional recovery E2E (FAQ Q262·Q271·Q333 Fixed) |
| 테스트 | **`FunctionalRecoveryServiceTest`**(+65 BNK-100) · **`ProgramCompliancePilotServiceFlowE2eTest`** (BNK-103) · **`CarePlanProvisionCompliancePilotServiceFlowE2eTest`** (BNK-112, `a9f8bda`) · **`RoleBasedControllerAccessTest$FunctionalRecoveryAccess`** · **`MustApiEndpointRoutingTest$FunctionalRecoveryRouting`** · FE **`programComplianceLiveApi.e2e.test.js`** |

#### 10-11-2. 사례관리 회의록 API (G32, US-T07, `2225a7a`·`0821ce8`, V73·V74) — **FE UI Fixed**

MOHW **평가 지표 43·29** 대응. **`CaseManagementPage`**(`/case-management/meetings`)에서 분기별 회의록·compliance를 제공합니다. **`DashboardPage`** 에 **「사례관리 30일 미반영」**·**「평가 미실시」**·**「평가실시」** 위젯이 연동됩니다 (`0821ce8`·`7f2289b`).

| 메서드 | 경로 | 설명 | 권한 |
|--------|------|------|------|
| GET | `/case-management/meetings?year=&quarter=&clientId=` | 분기별 **사례관리 회의록** 목록 | `hq_admin`·`branch_admin`·`social_worker`·`caregiver`(조회) |
| POST | `/case-management/meetings` | 회의록 등록 — **7필드**(이용자·일자·선정사유·내용·결과·**`caseManagementPlan`**·참석자 ≥2) | `hq_admin`·`branch_admin`·`social_worker` |
| PATCH | `/case-management/meetings/{meetingId}` | 회의록 수정 | 동일 3역할 |
| GET | `/case-management/compliance?year=&quarter=` | 지표43·30일 급여반영·**지표29 평가 실시** compliance | `hq_admin`·`branch_admin`·`social_worker` |

| 규칙 | 내용 |
|------|------|
| 스키마 | **V73** — `case_management_meetings` · **V75** — `case_management_plan` (`0a270a2`, Q265) |
| UK | `organization_id`×`client_id`×`meeting_year`×`meeting_quarter` — 이용자·분기당 1건 |
| 참석자 | **2인 이상** — FE·BE 검증 · **`,;/\n·` 구분자** 정규화 (`7eebd8c`·`2225a7a`, QA-B40) |
| 30일 반영 (지표43) | compliance — 회의일+30일 이내 **프로그램 참여** 또는 **청구 라인** 변경 · **`reflectionWithin30DaysMet`** → 대시보드 위젯 |
| 평가 실시 (지표29) | **`evaluationConductedMet`** — 회의일+30일 이내 **기능회복훈련 출석** 또는 **계획 갱신** (`11277b9`, Q266) · **`evaluationConductedMetCount`** 집계 |
| FE UI | **`CaseManagementPage`** — **7필드 폼·목록·「수정」→`PATCH`**(Q265·Q279, `26499b3`) · **지표29 StatCard**(Q266, UXD-79) · **`DashboardPage`** 30일·평가 widget (Q263·Q266) · **`CaseManagementPage.test`**·**`DashboardPage.test`**·**`pilotPageFlows`** US-T07 · SideNav **`caregiver` 제외** |
| DB | **V74** — V73 integrity 트리거·CHECK (V70/V52 패턴, `622b5e5`) |
| 테스트 | **`CaseManagementServiceTest`** · **`RoleBasedControllerAccessTest$CaseManagementAccess`** · **`MustApiEndpointRoutingTest$CaseManagementRouting`** |

> **보관**: 퇴소 후 5년 — `DATA_RETENTION_POLICY.md` §2 `case_management_meetings`.

#### 10-11-3. 급여제공결과 평가 API (G39, US-T08, `f082933`·`1c99bcd`·`a16e1fe`, V80·V81) — **FE UI Fixed**

MOHW **평가 지표 44** 대응. **`ProvisionResultEvaluationPage`**(`/programs/provision-result-evaluations`)에서 StatCard·연간 평가 목록·등록·수정 폼을 제공합니다. **`DashboardPage`** 에 지표44 gap·상태 위젯 4종이 연동됩니다 (UXD-83/BNK-109, Q276).

| 메서드 | 경로 | 설명 | 권한 |
|--------|------|------|------|
| GET | `/provision-result-evaluations?year=&clientId=` | **연간 급여제공결과 평가** 목록 | `hq_admin`·`branch_admin`·`social_worker`·`caregiver`(조회) |
| POST | `/provision-result-evaluations` | 평가 등록 — `clientId`·`evaluationDate`·`overallSummary`·`evaluatorName` | `hq_admin`·`branch_admin`·`social_worker` |
| PATCH | `/provision-result-evaluations/{evaluationId}` | 평가 수정 | 동일 3역할 |
| GET | `/provision-result-evaluations/compliance?year=` | **지표44 4-pillar** compliance | `hq_admin`·`branch_admin`·`social_worker` |

| 규칙 | 내용 |
|------|------|
| 스키마 | **V80** — `provision_result_evaluations` · **V81** — Tenant·지점·활성 이용자 integrity·UK `(org, client_id, evaluation_year)` |
| UK | 이용자·**평가 연도(`evaluationDate.year`)** 당 1건 — 중복 **`422`** |
| **지표44 pillar 1** | **`weeklyStateChangeMet`** — 당주 **건강 기록** 1건 이상 |
| **지표44 pillar 2** | **`monthlyProvisionRecordProvidedMet`** — 당월 **`CARE_PROVISION_RECORD`** 알림 발송 이력 |
| **지표44 pillar 3** | **`annualEvaluationConductedMet`** — 해당 연도 **평가 행 존재** |
| **지표44 pillar 4** | **`evaluationReflectedWithin30DaysMet`** — 평가일+30일 이내 **기능회복 계획 갱신·프로그램 참여·건강 기록** |
| FE UI | **`ProvisionResultEvaluationPage`** · **`RecordsContextNav`** · **`provisionResultCompliance.js`** silverangel verbatim · **`DashboardPage`** — gap·상태 위젯 **8종** (`8e66ae8`) · **`ProvisionResultEvaluationPage.test`**·**`dashboardSummary.test`**·**`programComplianceServices.test`** |
| 테스트 | **`ProvisionResultEvaluationServiceTest`** · **`MustApiEndpointRoutingTest$ProvisionResultRouting`** · **`RoleBasedControllerAccessTest$ProvisionResultAccess`** · **`DashboardServiceTest`** (G17/G32/G38/G39 snapshot + billing/NHIS, `7ba18c1`·`70d76a4`·`15b3c7e`, Q280·Q282) · **`CarePlanProvisionCompliancePilotServiceFlowE2eTest`** (BNK-112) · **`DashboardPage.test`** snapshot-first (`8fa9f3d`) |

> **보존**: 퇴소 후 5년 — `DATA_RETENTION_POLICY` §2-1 G39 · USER_MANUAL §5-9 · FAQ Q276

### 10-12. 방문요양 일정·NHIS import API (G21, `ee3fa3a`, V53)

| 메서드 | 경로 | 설명 | 권한 |
|--------|------|------|------|
| GET | `/visits?from=&to=&scheduleKind=` | 월간 일정 조회 | 스코프 내 |
| POST | `/visits` | 일정 등록 (`DRAFT`) | `branch_admin`, `social_worker` |
| POST | `/visits/{id}/confirm` | 확정 — **페어 DRAFT 동시 CONFIRMED** (`confirmPairedSchedule`, Q259, `aacf20b`) | 동일 |
| POST | `/visits/{id}/check-in` | 체크인 — **`checkInMethod` `MOBILE`/`MANUAL` 소문자 정규화** (Q275) · **페어 PLAN/BILLING 진행 동기화** (Q238, `9d7c17f`) | `social_worker`, `caregiver` |
| POST | `/visits/{id}/check-out` | 체크아웃 — **페어 완료 동기화** | 동일 |
| POST | `/visits/{id}/cancel` | 취소 — **페어 PLAN/BILLING 연쇄 취소** (US-V02, Q194) | `branch_admin`, `social_worker` |
| **POST** | **`/visits/imports/nhis`** | **공단 xlsx 일괄 import** (multipart) | `branch_admin`, `social_worker` |
| **GET** | **`/visits/confirm-readiness`** | **일괄확정 사전 점검** — `ready`·`blockers[]`·`draftVisitIds[]` (Q330, `0b807d8`) | `branch_admin`, `social_worker` |
| **POST** | **`/visits/batch-confirm`** | **DRAFT 일괄 확정** — **`nhisComparisonAcknowledged`·`changeHistoryChecked` 필수 `true`** | `branch_admin`, `social_worker` |

| import 파라미터 | 설명 |
|----------------|------|
| `branchId` | **`HOME_VISIT` 지점만** (`e304fd3`) |
| `scheduleKind` | `PLAN`(기본) \| `BILLING` — **소문자·공백 trim 후 대문자 정규화** (`225b104`, Q275) |
| `createPairedBillingSchedule` | PLAN import 시 페어 BILLING 자동 생성 |
| `file` | **`.xlsx` only** — `NhisVisitScheduleExcelParser` · **`validateImportFile`** — 확장자·Content-Type 사전 검증 (`3c7b247`, Q278) |

| **파일 검증 (`validateImportFile`)** | |
|-------------------------------------|--|
| 빈 파일 | **`422`** 「업로드할 엑셀 파일이 필요합니다.」 |
| 확장자 | **`.xlsx` 필수** |
| Content-Type | **`application/vnd.openxmlformats-officedocument.spreadsheetml.sheet`** · **`application/octet-stream`** 허용 — **`text/plain` 등 거부** |

| 행 `importStatus` | 처리 |
|-------------------|------|
| `IMPORTED` | `DRAFT` 일정 생성 |
| `UNMATCHED` | 인정번호 미매칭 |
| `SKIPPED` | 퇴소·비활성·시간 오류·**제공시간 1–480분 범위 밖**(Q193) · **확정 계획일정으로 청구 import 차단**(Q195) · **동일 방문일정 중복**(Q234, `9aafa3e`) |

| **수기 등록·수정** | **`ensureNoDuplicateVisitSlot`** — 동일 슬롯 **`422`** 「동일한 방문일정이 이미 등록되어 있습니다.」 (`ff12473`, Q259) |

| **담당 직원 배정 (`assignedUserId`, Q304, `dc48933`)** | |
|-----------------------------------------------------|--|
| 검증 시점 | **`POST /visits`** · **`PATCH /visits/{id}`** — `assignedUserId` **non-null** 일 때 |
| 거부 | **404** 「배정할 직원을 찾을 수 없습니다.」 · **422** 「퇴사 또는 비활성화된 직원은 배정할 수 없습니다.」 · **422** 「해당 지점 직원만 방문일정에 배정할 수 있습니다.」 |

| **batch-confirm gates (Q330, `0b807d8`·`c22a5dc`·`230659a`)** | |
|-----------------------------------------------------|--|
| ack 필수 | **`nhisComparisonAcknowledged=true`** · **`changeHistoryChecked=true`** — 미충족 **`422 BUSINESS_RULE`** |
| **기간 필수 (BNK-213)** | **`fromDate`·`toDate` non-null** — 누락 **「일괄확정 기간(시작일/종료일)을 입력해주세요.」** · **`to < from`** 거부 |
| readiness | **`ready=false`** when **DRAFT 0건** or **페어 불일치** — **`pairedDivergedCount`** · **`unassignedDraftCount`** 경고만 |
| RBAC | **`RoleBasedControllerAccessTest$VisitAccess`** — **`caregiver` batch-confirm 거부** |
| FE | **`VisitBatchConfirmPanel`** on **`VisitsPage`** — **`fetchVisitConfirmReadinessApi`**·**`batchConfirmVisitsApi`** · **UXD-102** (`d5ff3f8`) |

| **체크인·체크아웃 담당자 가드 (Q307, `b459f4c`)** | |
|------------------------------------------------|--|
| 대상 | **`caregiver`** — **`assignedUserId` ≠ actor** 시 **`422`** 「배정된 요양보호사만 체크인·체크아웃할 수 있습니다.」 |
| 예외 | **`hq_admin`·`branch_admin`·`social_worker`** — 감독 역할, 가드 생략 |
| 시점 | **`POST …/check-in`** · **`POST …/check-out`** · **confirm 시 재검증** |
| 테스트 | **`VisitServiceTest`** assigned check-in/out cases |

| 페어 동기화 | **DRAFT 수정** — `syncPairedDraftScheduleOnUpdate` (Q199) · **확정** — `confirmPairedSchedule` (Q259) · **체크인/아웃** — `syncPairedScheduleProgress` — 페어가 완료·취소가 아니면 `IN_PROGRESS`/`COMPLETED`·시각·`checkInMethod` 동기화 (Q238) |
| 테스트 | **`NhisVisitScheduleExcelParserTest`** · **`VisitServiceTest`**(normalize·duplicate·paired) · **`VisitControllerRoutingTest`** · **`VisitPilotServiceFlowE2eTest`** · **`VisitNhisImportPanel.test`** · **`RoleBasedControllerAccessTest$VisitAccess`** |

> **FE UI**: **`VisitsPage`** — **`VisitNhisImportPanel`** import 업로드 **Fixed** (UXD-63, Q189) · 확정 일정 존재 시 **UI 차단** (BNK-26, Q195). USER_MANUAL §5-11.

#### G2 — 보호자 명세 수동 발송 (`84f3441`)

| 메서드 | 경로 | 설명 | 권한 |
|--------|------|------|------|
| **POST** | **`/billing/claims/{claimId}/notify`** | 연결 보호자에게 **본인부담금 명세** 알림 dispatch | `hq_admin`, `branch_admin` |

| 규칙 | 내용 |
|------|------|
| 대상 상태 | **`CONFIRMED`·`PAID`만** — `DRAFT` → `422` |
| **dedupe** | 동일 **`clientId` 중복 라인** → **이용자당 1회** dispatch · `dispatchedCount` = unique 이용자 수 (Q219, `40567a2`) |
| 응답 | `{ claimId, dispatchedCount }` |
| 알림 | J03 **`BILLING_STATEMENT`** — stub 환경은 `notifications` 이력만 |
| FE | **`BillingDetailPage`** **「보호자 발송」** · **`OverduePage`** **「안내 발송」** (Q196) |
| 테스트 | **`BillingServiceTest`** · **`J03AlimtalkServiceFlowE2eTest`** notify→payment · **dedupe·amount guard** (`40567a2`·`4109680`) |

#### US-L01 — 본인부담금 수납 (`recordCopayPayment`, `4109680`)

| 메서드 | 경로 | 설명 | 권한 |
|--------|------|------|------|
| **POST** | **`/billing/claims/{claimId}/payments`** | **`CONFIRMED` → `PAID`** · 입금 메타 저장 | `hq_admin`, `branch_admin` |

| 규칙 | 내용 |
|------|------|
| 본문 | `{ paidAt, paymentMethod, amount? }` — `paymentMethod`: `CASH` \| `BANK_TRANSFER` |
| **금액** | **`amount` ≤ 0 거부** · **`copayAmount` NULL 거부** · **본인부담금과 불일치 거부** · 생략 시 전액 (Q218·Q257) |
| FE | **`PaymentRecordModal`** — **과납·0원 차단** (`dd72ff8`) · **`normalizeAmount`** (Q220) |
| CMS | **`CmsService`** 성공 시 동일 **`recordCopayPayment`** 호출 (Q208) |
| 알림 | J03 **`BILLING_PAYMENT_RECEIVED`** dispatch |
| 테스트 | **`BillingServiceTest.recordCopayPaymentShouldRejectNonPositiveAmount`** · **`PaymentRecordModal.test`** |

#### US-L01 — 은행 거래내역 엑셀 일괄입금 (`e50533f`·`95bb34d`, BNK-48)

| 메서드 | 경로 | 설명 | 권한 |
|--------|------|------|------|
| **POST** | **`/billing/imports/bank-deposits`** | 은행 **입금 내역 xlsx** 업로드 → 매칭 **`CONFIRMED` 단일 라인** 청구에 **`recordCopayPayment`** | `hq_admin`, `branch_admin` |

| 규칙 | 내용 |
|------|------|
| 요청 | `multipart/form-data` — `branchId`(UUID) + `file`(xlsx) |
| 파서 | **`BankDepositExcelParser`** — `거래일`·`입금자`·`입금액` 등 **한국 은행 헤더 유연 매칭** · 출금 행·0원 제외 |
| 매칭 | **입금자명 ≈ 이용자명** + **금액 = copayAmount** · **단일 이용자 청구만** 자동 적용 |
| 월 구분 | 동명·동액 **다월** 청구 → **거래일 `YearMonth`** 로 자동 선택 (`95bb34d`) |
| 동월 중복 | 같은 달 2건 이상 → **`UNMATCHED`** — 수동 수납 |
| 행 상태 | `APPLIED` · `SKIPPED` · `UNMATCHED` — 응답 `rows[]` |
| 감사 | `audit_logs` — `BANK_DEPOSIT_IMPORT` |
| FE | **`BankDepositImportPanel`** on **`/billing/payments`** — **`activeBranchId` → `branchId`** · **`appliedCount`** 요약 · **8-bank format `<details>`** + 은행별 **「샘플」** xlsx (`758e590`·`b9845ac`, Q258) |
| 테스트 | **`BankDepositExcelParserTest`** · **`BankDepositImportServiceTest`** · **`BankDepositCopayLifecycleE2eTest`** · **`BankDepositImportPanel.test`** · **`BankDepositImportPanel.formats.e2e.test`** · **`MustApiEndpointRoutingTest`** · **`RoleBasedControllerAccessTest`** |

#### G26 / US-L04 — 연말정산 의료비공제 (`970f547`·`7f10449`·`13272bc`, 케어포 7-2-1)

| 메서드 | 경로 | 설명 | 권한 |
|--------|------|------|------|
| **GET** | **`/clients/{clientId}/medical-expense-deduction`** | 이용자별 **귀속 연도** `PAID` 본인부담 납입 집계 | `hq_admin`, `branch_admin`, `social_worker`, `caregiver` |
| **GET** | **`/guardian/clients/{clientId}/medical-expense-deduction`** | 보호자 연결 이용자 동일 집계 | `guardian`, `client_user` |

| 규칙 | 내용 |
|------|------|
| 쿼리 | **`taxYear`** (필수) — 2000 ~ 현재 연도, 초과·미만 → **`422`** |
| 집계 기준 | **`paidAt` 연도** = `taxYear` · 상태 **`PAID`** · **`paymentMethod` ∈ {`CASH`, `BANK_TRANSFER`}** |
| **제외** | **`CMS`·`EASY_PAY`** — 케어포 7-4·7-5 (`MEDICAL_EXPENSE_EXCLUDED_PAYMENT_METHODS`, `970f547`, Q254) |
| 응답 | `clientId`, `clientName`, `taxYear`, `totalPaidAmount`, `paymentCount`, `items[]` (`claimId`, `yearMonth`, `copayAmount`, `paidAt`, `paymentMethod`) |
| FE | **`MedicalExpenseDeductionPanel`** — **CMS·간편결제 제외 안내** (Q254) · **「조회」 submit fetch** (Q255) · **인쇄·CSV·국세청 xlsx** (`e2c2ffe`·`fd569d7`, Q258) · **`ClientDetailPage`** **「청구」** · **`GuardianPortalPage`** **「연말정산」** |
| 테스트 | **`BillingServiceTest`** aggregate·exclude CMS/EASY_PAY · **`MustApiEndpointRoutingTest`** · **`MedicalExpenseDeductionPanel.test`** · **`medicalExpenseDeduction.test`** xlsx |

> **운영**: **현금·계좌이체** 입금 시 **`paidAt` 누락** 청구는 집계 제외 — Q250·Q252. **CMS 수납분은 의료비공제 대상 아님** — Q254. **NTS xlsx**는 클라이언트 생성 **간소화 양식** — 국세청 **전자신고 자동 제출**은 **미지원**(Could).

#### BNK-47·49·51 — 재가급여 월한도 가드 (`a92e625`·`20bc1be`·`fba5ea8`)

| 메서드 | 경로 | 설명 | 권한 |
|--------|------|------|------|
| **GET** | **`/billing/monthly-benefit-caps`** | 등급별 **월한도액** 참조 (2026: 1등급 2,512,900원 …) | `hq_admin`, `branch_admin`, `social_worker` |
| **GET** | **`/billing/claims/monthly-cap-guard`** | 청구 생성 **전** `nhisAmount` > 월한도 이용자 **경고 목록** | `hq_admin`, `branch_admin` |

| 규칙 | 내용 |
|------|------|
| 카탈로그 | **`MonthlyBenefitCapCatalog`** — MOHW 제2025-247호 · **2026년만** · **1~5등급 + `COGNITIVE_SUPPORT` 676,320** (`20bc1be`, G27) |
| 동작 | **non-blocking** — `warningCount`·`exceededClients[]`·`message` 반환 · 생성 API **차단 안 함** |
| FE | **`MonthlyBenefitCapGuardPanel`** (`/billing`·`/dashboard`) · **`MonthlyBenefitCapGuardBanner`** — 초과 0건 **success** (`62f022d`) · **`MonthlyBenefitCapBanner`** (청구 상세) · BE·FE **인지지원등급 parity** (Q226·Q228) |
| 테스트 | **`MonthlyBenefitCapCatalogTest`** · **`BillingServiceTest`** cap guard · **`MonthlyBenefitCapGuardPanel.test`** · **`MonthlyBenefitCapGuardBanner.test`** · **`MonthlyBenefitCapBanner.test`** |

#### G11 — MOHW 급여 가산율 catalog·자동 반영 (`904072b`·`d7475fd`·`f987b9d`)

| 메서드 | 경로 | 설명 | 권한 |
|--------|------|------|------|
| **GET** | **`/billing/fee-surcharge-rates`** | 야간·심야·주말·공휴일·유급휴일 **가산율 참조표** + 운영 안내 문구 | `hq_admin`, `branch_admin`, `social_worker` |
| **POST** | **`/billing/fee-surcharge-preview`** | 단일 가산율 **미리보기** — `surchargeCode` 또는 `serviceStartAt`+`serviceEndAt` | 동일 |

| 규칙 | 내용 |
|------|------|
| 카탈로그 | **`FeeSurchargeRateCatalog`** — NIGHT 20% · LATE_NIGHT 30% · WEEKEND_HOLIDAY 30% · PAID_HOLIDAY 50% |
| preview 본문 | ① `{ "baseAmount", "surchargeCode" }` 또는 ② `{ "baseAmount", "serviceStartAt", "serviceEndAt" }` — `baseAmount` **양수 필수** |
| preview 응답 | `baseAmount`·`surchargeCode`·`surchargeLabel`·`surchargePercent`·`surchargedAmount` |
| **자동 청구** | **`claimGenerationBasis=ATTENDANCE_SCHEDULE`** 시 **`POST /billing/claims/generate`** — 출석 **입·퇴소·휴일**로 **일별 가산 자동 반영** (`BillingService.buildClaimLineTotalsFromAttendances`) |
| **가산 미적용** | **`NHIS_IMPORT`** — import 일수 × 기준 1일 수가 (가산 없음) |
| 중복 | **가산 1종만** — `noStackingNote` |
| FE | **`FeeSurchargeGuidePanel`** — catalog 시드 + **preview API** · **`ClaimGenerationPanel`** 가산 안내 (Q229) |
| 테스트 | **`FeeSurchargeRateCatalogTest`** · **`BillingServiceTest`** preview·**attendance surcharge generate** · **`MustApiEndpointRoutingTest`** · **`RoleBasedControllerAccessTest`** — `caregiver` 403 |

#### Flyway V56 — visit_schedules FK backing indexes

| 인덱스 | 용도 |
|--------|------|
| `idx_visit_schedules_org_paired` | PLAN↔BILLING `paired_schedule_id` self-FK·페어 조회 |
| `idx_visit_schedules_org_assigned_date` | `assigned_user_id` FK·담당 요양보호사 일정 조회 |

> G21 follow-up to V53/V55. DEPLOYMENT §8-1 · DATA_RETENTION_POLICY §4-1.

#### Flyway V57 — visit_schedules confirmed-plan blocking index

| 인덱스 | 용도 |
|--------|------|
| `idx_visit_schedules_org_branch_client_plan_blocking` | `POST /visits/imports/nhis` BILLING·paired import 시 **확정 PLAN EXISTS** 가드 — `org+branch+client+visit_date` partial (`schedule_kind=PLAN`, status IN CONFIRMED/IN_PROGRESS/COMPLETED) |

> G21 NHIS import guard performance @ `469d08c`. FAQ Q200 · DEPLOYMENT §8-1.

#### Flyway V58 — notifications billing reminder lookup index

| 인덱스 | 용도 |
|--------|------|
| `idx_notifications_org_template_claim_reminder` | `GET /billing/overdue` 페이지네이션 시 **`lastReminderAt`** 조회 — `template_code=BILLING_STATEMENT` · `payload.claimId` equality |

> US-L02 overdue list performance @ `c67ff1e`. FAQ Q202 · DEPLOYMENT §8-1.

### 10-13. CMS 자동이체 (US-L03, Hyosung FCMS, `2c6e57e`)

| 메서드 | 경로 | 설명 | 권한 |
|--------|------|------|------|
| **POST** | **`/billing/cms/enrollments`** | 보호자 CMS 자동이체 **등록** (FCMS member) | `hq_admin`, `branch_admin` |
| **GET** | **`/billing/cms/enrollments?clientId=`** | 이용자별 **ACTIVE·CANCELLED** 등록 **이력** (`4a622ab`, Q299) | `hq_admin`, `branch_admin` |
| **DELETE** | **`/billing/cms/enrollments/{enrollmentId}`** | **ACTIVE** CMS 자동이체 **해지** (FCMS unregister) | `hq_admin`, `branch_admin` |
| **POST** | **`/billing/cms/claims/{claimId}/debit`** | **확정** 청구 CMS **출금 요청** | `hq_admin`, `branch_admin` |
| **GET** | **`/billing/cms/claims/{claimId}/debit`** | 출금 요청 **상태** 조회 | `hq_admin`, `branch_admin` |

| 규칙 | 내용 |
|------|------|
| 등록 본문 | `{ clientId, guardianUserId, payerName, bankCode, accountLast4 }` — **연결 보호자만** · **계좌 끝 4자리만** 저장 |
| 중복 | 동일 이용자 **다른 보호자 ACTIVE** 등록 **거부** (`72aff00`, Q299) · 동일 보호자 **ACTIVE** 재등록 **거부** · **`CANCELLED`** 재등록 **행 UPDATE** (`8431b5c`·`fee710d`, Q207) |
| 해지 | **ACTIVE**만 · **REQUESTED 출금 진행 중** **`422`** · **`status=CANCELLED`** · FCMS **`unregisterMember`** (`a34d0eb`, Q299) |
| 출금 대상 | **`CONFIRMED`** 청구만 · **ACTIVE CMS 등록** 필수 · **단일 이용자** 라인만 (`requireSingleClientClaim`, Q215) · **copay > 0** (`27f20de`, Q256) |
| 성공 | `cms_debit_requests.status=SUCCEEDED` → FCMS 응답 **금액 = 청구 copay** 확인 후 **`BillingService.recordCopayPayment`** → **`PAID`·`payment_method=CMS`** · J03 **`BILLING_PAYMENT_RECEIVED`** (Q256) |
| **무결성** | FCMS 실패·금액 불일치 → **`FAILED` 응답(HTTP 200)**·`failureReason`·청구 **CONFIRMED 유지** (`838a7f6`, Q256) · **`SUCCEEDED` 재조회** 시 청구 **`PAID`·`CMS`·금액 일치** 검증 (`6bf51c8`) |
| **연말정산** | CMS 수납분은 **`GET …/medical-expense-deduction` 집계 제외** (Q254) |
| FCMS | **`FCMS_PROVIDER=stub`**(기본) — **`StubFcmsClient`** · live 연동 후속 (DEPLOYMENT §4-6) |
| FE | **`CmsPage`** · **`CmsEnrollmentTable`** **「해지」**·Modal · **`BillingContextNav`** CMS 링크 · 출금 후 **확정 목록 갱신** (`c0a01b4`) |
| 테스트 | **`CmsServiceTest`** — cancel·duplicate guardian·amount mismatch · **`CmsCopayLifecycleE2eTest`** · **`CmsPilotServiceFlowE2eTest`** cancel lifecycle · **`MustApiEndpointRoutingTest$CmsRouting`** · **`RoleBasedControllerAccessTest$CmsAccess`** · **`CmsPage.test`** · **`CmsEnrollmentTable.test`** (`a34d0eb`·`9a6fdb6`, Q299) · **`StubFcmsClientTest`** |

#### Flyway V59 — CMS enrollment·debit schema

| 객체 | 용도 |
|------|------|
| `cms_enrollments` | 이용자·보호자별 FCMS member · `account_last4`·`bank_code`·`payer_name` · `status` ACTIVE/CANCELLED |
| `cms_debit_requests` | 청구당 1건 UK `(org, claim_id)` · `REQUESTED`/`SUCCEEDED`/`FAILED` |
| `chk_billing_claims_payment_method` | **`CMS`** 수단 추가 (V59) |

#### Flyway V60 — CMS composite Tenant FK

| 제약·인덱스 | 용도 |
|------------|------|
| `fk_cms_enrollments_*_org` | branch·client·guardian **composite Tenant FK** — cross-tenant CMS 등록 차단 |
| `fk_cms_debit_requests_*_org` | claim·enrollment **composite Tenant FK** |
| `idx_cms_enrollments_org_branch` · `_org_guardian` · `idx_cms_debit_requests_org_enrollment` | FK backing · purge cohort (DATA_RETENTION §2) |

> FAQ Q206–Q208·**Q299** · USER_MANUAL §4-6 · DEPLOYMENT §4-6·§8-1.

### 10-14. 본인부담금 간편결제 (US-L06, G2/7-5, BNK-189~193, `438f5c7`·`9a4ab8e`)

| 메서드 | 경로 | 설명 | 권한 |
|--------|------|------|------|
| **POST** | **`/billing/easy-pay/claims/{claimId}/payment`** · **alias `/claims/{claimId}`** | **확정** 청구 **7-5 간편결제** 요청 (케어포 view.npay_manage) | `hq_admin`, `branch_admin` |
| **GET** | **`/billing/easy-pay/claims/{claimId}/payment`** · **alias `/claims/{claimId}`** | 간편결제 **상태** 조회 | `hq_admin`, `branch_admin` |

| 규칙 | 내용 |
|------|------|
| 요청 본문 | `{ provider: CARD\|KAKAO_PAY, guardianUserId? }` — **`provider`** — BE **`Locale.ROOT`** uppercase · FE **NFKC·alias** (`82054f1`·`745a2f6`·`7ec7cd4`, Q328) · **malformed 거부** · **`guardianUserId`** 는 **`guardian_clients` 연결** 검증 |
| 출금 대상 | **`CONFIRMED`** 청구만 · **단일 이용자** 라인만 (`requireSingleClientClaim`, Q215와 동일 패턴) · **copay > 0** |
| **선행입금 가드** | **`getClaimGenerationGuard(branchId, claim.yearMonth)`** — 전월 **`CONFIRMED` 미수납**·**G33 미정산** 시 **`422`** (`b893e97`, Q327) — Q310과 **동일 규칙** |
| 진행 중 | **`REQUESTED`·`PENDING`** 재요청 **`422`** — **`SUCCEEDED`** 재조회는 **청구 `PAID`·`EASY_PAY`·금액 일치** 검증 |
| 성공 | `easy_pay_requests.status=SUCCEEDED` → PG confirm **금액 = 청구 copay** 확인 후 **`BillingService.recordCopayPayment`** → **`PAID`·`payment_method=EASY_PAY`** · J03 **`BILLING_PAYMENT_RECEIVED`** |
| **무결성** | PG order/confirm 실패·금액 불일치 → **`FAILED`·`failureReason`**·청구 **CONFIRMED 유지** · **`FAILED`** 건 **재요청** 허용 |
| **연말정산** | **`EASY_PAY` 수납분은 `GET …/medical-expense-deduction` 집계 제외** (Q254) |
| PG | **`StubEasyPayProvider`**(기본) — order+confirm **즉시 성공** · **live PG 벤더** P2 (DEPLOYMENT §4-6-1) |
| FE | **`EasyPayPage`** · **`EasyPayPanel`**(US-L06 a11y) · **`BillingContextNav`** **「간편결제」** · **`ClaimGenerationGuardBanner`** prior-month UI · **`normalizeEasyPayProvider`** (`745a2f6`·`7ec7cd4`) |
| 테스트 | **`EasyPayServiceTest`**(provider normalize·`Locale.ROOT`) · **`EasyPayPilotServiceFlowE2eTest`** · **`MustApiEndpointRoutingTest$EasyPayRouting`**(alias path) · **`RoleBasedControllerAccessTest$EasyPayAccess`** · **`EasyPayPage.test`** · **`EasyPayPanel.test`** · **`easyPay.test`** · **`billingGuardianPlatformServices.test`** · **`pilotPageFlows`** 7-5 E2E |

#### Flyway V108 — easy pay request schema

| 객체 | 용도 |
|------|------|
| `easy_pay_requests` | 청구당 1건 UK `(org, claim_id)` · `provider` CARD/KAKAO_PAY · `status` REQUESTED/PENDING/SUCCEEDED/FAILED/CANCELLED |
| `chk_billing_claims_payment_method` | **`EASY_PAY`** 수단 추가 (V108) |

#### Flyway V109 — failed PG order nullable

| 변경 | 용도 |
|------|------|
| `pg_order_id` nullable | PG order 생성 **실패** 건도 **`easy_pay_requests`** 이력 보존 (`70b3fb8`) |

#### Flyway V110 — easy pay request integrity (`16a0734`)

| 객체 | 용도 |
|------|------|
| `uq_easy_pay_requests_org_id` | Tenant anchor — composite FK target |
| `fk_easy_pay_requests_*_org` | 복합 FK 5건 — branch·claim·client·guardian cross-tenant 차단 |
| `trg_easy_pay_requests_set_org` | branch_id → organization_id 동기화 (V60/V74 패턴) |
| `trg_easy_pay_requests_guard_active_client` | INSERT 시 **퇴소·비활성 이용자** 차단 (V10/V93 패턴) |
| lifecycle CHECK | PENDING↔`pg_order_id` · SUCCEEDED↔`pg_transaction_id` · FAILED↔`failure_reason` · temporal sanity |
| purge index | `idx_easy_pay_requests_client_purge` · `idx_easy_pay_requests_org_guardian` partial |

#### Flyway V111 — easy pay guardian link guard (`dbecd72`)

| 객체 | 용도 |
|------|------|
| pre-migration check | 기존 **`easy_pay_requests.guardian_user_id`** orphan 행 있으면 **마이그레이션 중단** |
| `trg_easy_pay_requests_validate_guardian_link` | INSERT/UPDATE 시 **`users.role_code=guardian`** · **`guardian_clients`** 동일 client link **필수** |

#### Flyway V112 — functional recovery cognitive activity reason G17b (`6b7e6cb`)

| 객체 | 용도 |
|------|------|
| `functional_recovery_plans.cognitive_activity_provided` | BOOLEAN NOT NULL DEFAULT **TRUE** — 인지활동형 프로그램 제공 여부 |
| `functional_recovery_plans.cognitive_activity_not_provided_reason` | TEXT — 미제공 시 **자유 서술 사유** |
| `chk_functional_recovery_plans_cognitive_activity_reason` | 제공=TRUE ⇒ reason NULL · 제공=FALSE ⇒ reason **trim>0** |

> MOHW 2025-247 **제32조** — 기능회복훈련 계획에 인지활동형 미제공 사유 기록 (FAQ Q335).

#### Flyway V113 — program participation skip reason G17b (`ba7d84f`)

| 객체 | 용도 |
|------|------|
| `activity_programs.program_type` CHECK | **`GENERAL`·`FUNCTIONAL_RECOVERY`·`COGNITIVE`** (V113 확장) |
| `program_participations.skip_reason` | VARCHAR(30) — **`STAFF_SHORTAGE`·`EQUIPMENT_FAILURE`·`CLIENT_REFUSAL`·`OTHER`** |
| `chk_program_participations_attended_skip_reason` | **`ATTENDED`** ⇒ `skip_reason` **NULL** |
| 앱 계층 | **`COGNITIVE` + `ABSENT`** 시 skip_reason **필수** — `ProgramService.resolveSkipReason` (DB trigger 미적용, PLAN_NOTES #130) |

#### Flyway V114 — pressure ulcer care lifecycle G-NURSING (`edda491`)

| 객체 | 용도 |
|------|------|
| `pressure_ulcer_assessments` | 욕창 위험평가 — `assessed_on`·`scale_score`(6~23) · `risk_level`(`LOW`/`MODERATE`/`HIGH`) · `prevention_plan`·`plan_effective_from` pair CHECK |
| `pressure_ulcer_care_records` | 일별 간호 기록 — `care_date`·`body_site` · `ulcer_stage`(1~4) · `treatment_notes` NOT NULL |
| UNIQUE | `(organization_id, client_id, assessed_on)` · `(organization_id, client_id, care_date, body_site)` |
| composite FK | org·branch·client·recorded_by — tenant 격리·active client guard |
| 앱 계층 | **`PressureUlcerService`** — duplicate date guard · Braden range · plan-assessment linkage (`d638493`) |

#### Flyway V115 — integrated nursing vital checks L03_M11 (`80c0bd5`)

| 객체 | 용도 |
|------|------|
| `nursing_vital_checks` | 통합 바이탈 — `check_date`·`check_time` · `systolic`·`diastolic`·`pulse`·`respiration_rate`·`temperature`·`spo2` NOT NULL · `weight_kg`·`blood_glucose`·`notes` optional |
| UNIQUE | `(organization_id, client_id, check_date, check_time)` |
| CHECK | 혈압·맥박·호흡·체온·SpO₂·체중·혈당 범위 · `systolic > diastolic` |
| 앱 계층 | **`NursingVitalCheckService`** — duplicate datetime guard · client branch scope |

#### Flyway V116 — nursing weight records L03_M14 (`e95df4c`)

| 객체 | 용도 |
|------|------|
| `nursing_weight_records` | 체중 관리 — `measure_date` · `weight_kg` NOT NULL · `height_cm`·`goal_weight_kg`·`notes` optional |
| UNIQUE | `(organization_id, client_id, measure_date)` |
| CHECK | 체중 20~200 · 신장 100~220 · 목표체중 20~200 |
| FE | **`NursingWeightRecordPage`** — **`/nursing/weight-records`** · **`NursingWeightRecordForm`** (`8a8fe98`/`97108f2`) |

#### Flyway V118 — nursing oral care checks L03_M13 (`3540b4f`)

| 객체 | 용도 |
|------|------|
| `nursing_oral_care_checks` | 구강상태 — `check_date` · `brushing_assisted` · `oral_condition_status`(`GOOD`/`FAIR`/`POOR`) NOT NULL · `denture_worn`·`notes` optional |
| UNIQUE | `(organization_id, client_id, check_date)` |
| composite FK | org·branch·client·recorded_by — tenant 격리 |

#### Flyway V119 — nursing emergency records L03_M04 (`81bca68`)

| 객체 | 용도 |
|------|------|
| `nursing_emergency_records` | 응급상황 — `occurrence_date` · `incident_category` · `action_taken` NOT NULL · `detail`·`guardian_notified`·`notes` optional |
| CHECK | `incident_category` 6종 · `action_taken` non-blank |
| composite FK | org·branch·client·recorded_by — tenant 격리 · **일자 UNIQUE 없음** |

#### Flyway V120 — transport v1.3-B suggest PoC (`db94a65`)

| 객체 | 용도 |
|------|------|
| `branch_transport_settings` | 지점별 픽업 허용분·최적화 가중치(stability/fairness/distance) |
| `transport_suggest_events` | suggest 호출 로그 — **≤10회/지점/일** 상한 집계 |
| `clients.transport_notes` | 배차 메모(선택, 500자) |
| `transport_runs` UK | **차량당 1 run** — `uq_transport_runs_org_branch_date_direction_vehicle` |

#### Flyway V121 — nursing V118/V119 integrity (`090b2d7` follow-up)

| 객체 | 용도 |
|------|------|
| triggers | `nursing_oral_care_checks`·`nursing_emergency_records` — org/branch sync·active-client guard·`recorded_by` backstop |

#### Flyway V122 — transport v1.3-B integrity (`db94a65`)

| 객체 | 용도 |
|------|------|
| `transport_runs` | v1.3-A **vehicle_id NULL** 단일 운행 UK 보존 |
| `transport_suggest_events` | Tenant anchor·`created_by` actor backstop |
| `branch_transport_settings` | `updated_by` actor backstop |

#### Flyway V123 — nursing service provision L03_M01 (`9bd1660`)

| 객체 | 용도 |
|------|------|
| `nursing_service_records` | **이용자×`service_date` UNIQUE** · **3-flag provision CHECK** · composite FK·active-client guard |
| 인덱스 | `idx_nursing_service_records_org_branch_service_date` — 지점·기간 목록 |

> FAQ **Q326~Q348** · USER_MANUAL §4-6·§5-8·§5-9·§5-15~§5-20 · DEPLOYMENT §3-6·§4-6-1·§8-1 · DATA_RETENTION §2·§4 V110–V123.

### 10-6. Must FE·API 갭 (v1.2 P1 + v1.3-A + v3, `c0a01b4`)

| 기능 | API | FE `37be0a3` |
|------|-----|-------------|
| **직원 관리 (§3-8)** | `GET/POST /users` (`roleCode`·`displayName`) | **`StaffPage`** — **`StaffRoleSelect`**·필드 검증 · **`role`·`name` DTO 불일치 잔존**(Q162) |
| 지점·통합 대시보드 | `GET /dashboard/branch` — **`nhisUnmatchedCount`·`pendingReviewCount`·`overdueCount`** + `/hq` | **6~7위젯**(NHIS 대기 Q183 · **미납 Q202**) + HealthAlertList + Recharts — HQ **`branchName` Badge**(Q167) |
| **이용자 배차 프로필 (US-T01)** | **`POST/PATCH /clients`** — `usesTransport`·픽업 주소·연락처·시각 | **`ClientFormPage`·`ClientTransportProfileSection` UI Fixed** (Q166) |
| **건강 기록 입력** | `POST …/health/vitals`, `…/medications`, **`…/incidents`** | **`HealthPage`** — **`healthApiPayload.js` 정합 Fixed** · **`IncidentRecordForm`**(UXD-41) · **비정상 경고**(Q155) |
| **NHIS DISCREPANCY 비교** | 대사 행 `claimId`·금액·일수 필드 | **`ReconciliationPage`** — **`DiscrepancyComparePanel`** + **`NhisReconciliationTable` 「비교」** (US-G06, Q135) |
| **NHIS UNMATCHED 후보 검색** | `GET …/candidates?q=` · `PATCH …/match` | **`ReconciliationPage`** — `SearchInput`·후보 드롭다운·수동 연결 폼 (UXD-43, Q135) |
| **배차·이동경로** | **`/api/v1/transport/*` Fixed** (§10-10) · **non-HQ 주소·연락처 마스킹**(Q169) | **`TransportPage`**·`TransportRunNewPage`·`TransportRunDetailPage` — **FE·BE 연동** · **unconfirm UI Fixed**(Q163) · **forced-colors a11y**(UXD-50, Q168) · **`TransportPickupContact`**(UXD-52, Q171) |
| **식사·프로그램 (v3 Should)** | **`POST /meals/menus`·`POST /programs/schedule` Fixed** (§10-11) | **`MealMenuForm`·`ProgramScheduleForm`** — **Q161 Fixed** |
| **건강 추이** | `GET /clients/{id}/health?days=` | **`HealthDetailPage`** — **`HealthTrendChart`** + 표 + FilterChips — **`?days=` 미호출**(Q165, Q119) |
| 보호자 알림 설정 | `GET/PUT /guardian/notification-preferences` + 직원 대리 API | **UI 없음** — Swagger (Q124) |
| **알림 발송 이력** | **`GET /guardian/notifications`**, **`GET /clients/{id}/notifications`** | **`NotificationHistoryPanel`** — 보호자·직원 UI **Fixed** (Q152·Q187) |
| 보호자 초대·수락 | V43 + FE | **연동** — `ClientDetailPage`·**`GuardiansPage` 초대**·공개 수락 (Q143·Q139) |
| 보호자 포털 | `GET /guardian/daily-records`, `/clients/{id}/billing` | **연동** — `GuardianPortalPage` + **`GuardianDailySummary`**(출석·건강·**식사 UI**, UXD-62, Q188) + **명세 「더 보기」 페이지네이션**(Q192) + **`GuardianBillingDetailModal`** 상세·인쇄 (UXD-55, J02, Q175) |
| **입금 처리** | **`POST /claims/{id}/payments` Fixed** · **`POST /imports/bank-deposits` Fixed**(Q227) · **`amount` ≤ 0·불일치 거부**(Q218) · `GET /billing/payments` 미구현 | **`PaymentPage`** + **`PaymentRecordModal`** + **`BankDepositImportPanel`** — **`branchId` 전송 Fixed** (`f4bb171`, Q228) · 목록 claims 필터 **우회** (Q174) |
| **보호자 명세 발송 (G2)** | **`POST /claims/{id}/notify` Fixed** | **`BillingDetailPage`·`OverduePage`** — **「안내 발송」Fixed** (Q196) |
| **미납 관리** | **`GET /billing/overdue?page&size&q=` Fixed** | **`OverduePage`** + **`BillingContextNav`** — **`OverdueSummaryBar`**·**`Pagination`** (Q197·Q203) · **대시보드 위젯**(Q202) |
| **CMS 자동이체 (US-L03)** | **`/billing/cms/*` Fixed (stub FCMS)** | **`CmsPage`** — 등록·출금 2탭 · **`BillingContextNav`** CMS 링크 (Q207·Q208) |
| **간편결제 (US-L03, 7-5)** | **`/billing/easy-pay/*` Fixed (stub PG)** | **`EasyPayPage`** — **`EasyPayPanel`** · **`BillingContextNav`** 간편결제 링크 (Q326·Q327) |
| **보호자 목록·연결** | `GET /users?branchId=` · `GET /guardians/{id}` | **`GuardiansPage`** · **`GuardianClientLinks`** (Q185) — `GET /guardians` 목록 **404** (Q107) |
| 이용자 등록·수정 | `POST/PATCH /clients` | **`ClientFormPage`** — 본문 **불일치** (Q151) |
| 지점 CRUD | `/branches` + `/regions/*` | **`BranchesPage`** + **`RegionSelector`** — **Q184 Fixed** |
| Tenant 온보딩 | `/platform/organizations` | **`PlatformPage`** — `?q=` vs `?query=` (Q97) |
| 수가표·설정 | `/billing/fee-schedules`, `/organization/settings`, `/settings/*` | **`FeeScheduleTable`·`SettingsPage` 4탭**(Q201) — **UXD-51 정식 UI**(Q170) · **`DateInput`**(UXD-64) |
| QR·출석 통계 | `/branches/{id}/qr`, `/attendance/stats/monthly` | **`QrGeneratePage`(저장·인쇄 US-E03)·`AttendanceStatsPage`(US-E05)** — 본문·쿼리 갭 (Q109·Q106) |
| **출석 transportMode** | `GET /attendance?transportMode=all\|boarding\|on_site` | **Fixed** (`d6d7e7f`·`6c4c151`) — **`/attendance/boarding`·`/attendance/on-site`** · `usesTransport` 필터 (Q232) |
| 수기 체크인/결석 | `POST /attendance/check-in`, `/check-out`, `/absence` | **입소·귀가·결석 버튼 + 모달(US-E01·E02)** — roster·`status`·`transportType` 갭 (Q94·Q96) |
| NHIS import·reconciliation | P7/P8 | **연동** — `/billing/imports/nhis` + **`NhisReconciliationTable`**(Badge·행 강조, Q101) |
| JWT·세션 | in-memory + SessionTimeout | 새로고침 = 재로그인, 30분 idle 경고 (Q82·Q112) |

**출석 통계 API 응답 (참고)**

```json
{
  "from": "2026-01-01",
  "to": "2026-06-06",
  "branches": [{
    "branchId": "uuid",
    "branchName": "○○점",
    "months": [{
      "yearMonth": "2026-06",
      "activeClientCount": 10,
      "attendedDays": 150,
      "attendanceRate": 0.50
    }]
  }]
}
```

`attendanceRate`는 0~1(×100=%)이며, `attendedDays`는 **지점 전체 출석 행 수**입니다.

전체 명세: `docs/technical/API_SPEC.md`

---

### 10-12. 기관 교육일지 compliance 설정 (G41, sysadmin 참고)

기관 교육일지(`/staff/training-logs`, §5-14 USER_MANUAL)는 **공단 평가 기준**에 따라 센터의 법정 의무 교육을 추적합니다. `sysadmin`이 센터 compliance 규칙을 설정하면, 시스템이 자동으로 신규직원 기한을 계산하고 모니터링 체크리스트에 반영합니다.

#### API 엔드포인트 (Flyway V104–V107, BE `6191b91`·`0f11158`·`ee42e5d`)

| 엔드포인트 | 메서드 | 권한 | 설명 |
|-----------|:----:|:---:|------|
| `/api/v1/staff/training-logs` | GET | `hq_admin`, `branch_admin`, `social_worker` | 조회 — `trainingType`, `referenceYear`, `branchId` |
| — | POST | `hq_admin`, `branch_admin`, `social_worker` | 등록 — **annual 유형은 `referenceHalf` 생략** (V107) |
| `/{id}` | PATCH | 동일 | 수정 |
| `/compliance` | GET | `hq_admin`, `branch_admin`, `social_worker`, `sysadmin` | **지점 compliance** — G41b `disasterResponseAnnualMet` 등 · `newHireItems` |

#### compliance 응답 (BNK-185~187)

`StaffTrainingLogComplianceResponse` 주요 필드:

| 필드 | 의미 |
|------|------|
| `elderlyHumanRightsFirstHalfMet` / `SecondHalfMet` | 노인인권 반기 |
| `operatingRegulationAnnualMet` | 운영규정 연 1회 |
| `disasterResponseAnnualMet` · `fireSafetyEquipmentAnnualMet` · `staffRightsAnnualMet` | G41b 3종 |
| `newHireOrientationMetCount` / `newHireStaffCount` | 신규 7일 — **지점 스코프** |
| `newHireItems[]` | 직원별 — **가장 이른 오리엔테이션일** 기준 MET (BNK-187) |

#### V107 annual no-half (BNK-188)

```
POST/PATCH payload
  ELDERLY_HUMAN_RIGHTS → referenceHalf: 1|2 ✅
  OPERATING_REGULATION (연간) → referenceHalf 생략 ✅
  DISASTER_RESPONSE · FIRE_SAFETY_EQUIPMENT · STAFF_RIGHTS → referenceHalf 생략 ✅
  referenceHalf 포함 시 → 422 (앱) + V107 CHECK (DB)
```

#### 자동 기한 계산 (V104–V105)

신규직원 입사 시 시스템은 자동으로 **운영규정 교육 기한**을 계산합니다.

```
신규직원 입사 처리 → created_at (입사일) 기록
                    ↓
시스템 자동 계산: 기한 = created_at + 7일
                    ↓
/staff 목록에서 기한 초과 시 warning 배지 표시
                    ↓
sysadmin이 /staff/training-logs에서 교육 등록 → 자동 기한 해제
```

**CHECK 규칙** (V104–V105):
- `trained_at` 입사일 <= 신규직원 기한 (created_at + 7일) ✅
- `trained_at` 연도 = `reference_year` (필수)
- `trainingType = OPERATING_REGULATION` + `newHireOrientation=true` (신규 7일 전용)

#### 모니터링 체크리스트 통합 (G30 integrated checklist)

`sysadmin`은 `/compliance/monitoring` 에서 기관 교육 이수율을 확인합니다.

**API**: `GET /api/v1/compliance/monitoring/checklist` (V101–V106)

| 문항 | 자동 집계 | 수동 입력 | 데이터 출처 |
|------|:-------:|:-------:|---------|
| 신규직원 운영규정 교육 | ✅ | — | `staff_training_logs` + `created_at` 기한 검증 |
| 연간 노인인권·재난·소화·권익 | ✅ | — | `staff_training_logs` 유형별 count |
| 관리자 라운딩 | — | ✅ | `/compliance/monitoring` 직접 입력 |
| 6개월 자가진단 | — | ✅ | 센터 자체 진행·기록 |
| 팀장급 자격 | ✅ | — | `staff_training_logs` + 실무경력 5년 검증 |
| 선임 업무수행일지 | ✅ | — | `/staff/lead-caregiver-log` 월 작성 여부 |
| 시정 기한 추적 | ✅ | — | compliance API 자동 추적 |

#### 모니터링 대시보드 팁 (sysadmin)

1. **월별 교육 현황** — `/compliance/monitoring` 상단 **integrated checklist card**에서 실시간 집계
2. **기한 초과 경고** — `/staff` 목록에서 warning 배지 확인 → **7일 기한 내 운영규정 교육 등록**
3. **연간 이수율** — `GET /api/v1/staff/training-logs/compliance` — G41b `*AnnualMet` · `allNewHiresOriented`
4. **live E2E** — `staffTrainingLogLiveApi.e2e.test.js` (`LIVE_E2E=1`, BNK-186)

---

## 11. 관련 문서

| 문서 | 대상 |
|------|------|
| `USER_MANUAL.md` | 센터장·사회복지사·보호자 현장 매뉴얼 |
| `DEPLOYMENT_GUIDE.md` | 인프라·Docker·배포 |
| `CHANGELOG.md` | 버전별 변경 이력 |
| `DATA_RETENTION_POLICY.md` | 보존·파기·백업 정책 |
| `API_SPEC.md` | REST API 전체 명세 |
| `FLOWCHART.md` | 화면·역할 흐름도 |
| `REQUIREMENTS.md` | 기능·비기능 요구사항 |

---

## 12. 용어집

| 용어 | 설명 |
|------|------|
| Tenant | SaaS 고객 1법인 = `Organization` 1개 |
| Branch | Tenant 소속 주간보호센터 지점 1곳 |
| RBAC | 역할 기반 접근 제어 (JWT `role` + 지점 스코프) |
| PII | 개인식별정보 (주민번호·연락처·주소 등) |
| NHIS import | 공단 청구내역상세 엑셀 업로드 연동 |
| Branch Switcher | 다지점 권한 사용자의 `active_branch_id` 전환 UI |

---

## 13. 변경 이력

| 날짜 | 변경 내용 |
|------|----------|
| 2026-06-09 | **51차** — §1-4·§10-6 UXD-55 GuardianBillingDetailModal·GuardianPortalPage·Q132·Q175·217/217 |
| 2026-06-08 | **50차** — §1-4·§10-6 BE v2 copay payment·overdue·V50·UXD-53/54·Q173·Q174·246/246·214/214 |
| 2026-06-08 | **49차** — §1-4·§10-10 BE `c7941e9` pickup contact masking·pilotPageFlows T03·Q172·241/241·208/211 |
| 2026-06-08 | **48차** — §1-4·§10-6·§10-10 ClientForm transport UI·UXD-52·Q166 Fixed·Q171·241/241·68/208 |
| 2026-06-08 | **47차** — §1-4·§10-6·§10-10 transport pickup masking·UXD-51·Q169·Q170·241/241·65/199 |
| 2026-06-08 | **46차** — §1-4·§10-6·§10-10 transport pilot E2E·RBAC·UXD-50 forced-colors a11y·Q168·240/240·60/189 |
| 2026-06-08 | **45차** — §1-4·§10-6·§10-10 US-T01 Client transport profile API·UXD-49 HQ 지점명·Q166·Q167·231/231·60/189 |
| 2026-06-08 | **44차** — §1-4·§10-6 UXD-48 Recharts 복원·대시보드/출석/건강 연동·Q118·Q119·Q165·226/226·60/183 |
| 2026-06-11 | **92차** — §1-4·§6-3-1·§10-4 US-M03 billing ledger report API·US-G04 year-coverage pre-check·Q179 Fixed·Q260·491/607 |
| 2026-06-11 | **91차** — §1-4·§6-3-1·§10-5 US-G04 fee schedule year guard·US-L01 bank sample xlsx·Q258·Q260·532/602 |
| 2026-06-11 | **90차** — §1-4·§10-6·§10-12·§10-13 G26 NTS xlsx·US-L01 8-bank guide·G21 visit slot guards·Q258–Q259·528/593 |
| 2026-06-11 | **89차** — §1-4·§10-6 G2 copayAmount null guard·G26 UI exclusion guidance·Q257·521/574 |
| 2026-06-11 | **88차** — §1-4·§10-6·§10-13 G26 CMS·EASY_PAY 의료비공제 제외·G2 CMS debit integrity·US-L04 조회 UX·Q254–Q256·519/569 |
| 2026-06-11 | **87차** — §1-4·§10-6 G26 medical expense deduction API·US-L04 UI·UXD-76 VehiclesPage a11y·Q252–Q253·514/567 |
| 2026-06-11 | **86차** — §1-4 G2 recordCopayPayment paidAt guard·US-J02 guardian portal race guards·Q250–Q251·509/555 |
| 2026-06-11 | **85차** — §1-4 G21 HOME_CARE alias·G2 paymentMethod guard·UXD-75 RecordsContextNav·Q248–Q249·508/553 |
| 2026-06-11 | **84차** — §1-4·§10-10 G7 guidance API restore·G16 cross-branch fee guard·Form18 3-way workflow·Q111·Q133·Q237·Q247·503/547 |
| 2026-06-11 | **83차** — §1-4·§10-6 QA-B24 NHIS guidance UI·V70 integrity·guardian DRAFT filter·Q133·Q212·Q245–Q246·498/543 |
| 2026-06-11 | **82차** — §1-4·§10-10 G15 care-provision·G16 VehiclesPage·G2 paidAt·Q243–Q244·497/534 |
| 2026-06-11 | **80차** — §1-4·§10-10·§10-12 G15 Form22 log·Form18 guide·time compliance·G21 paired check-in sync·Q236–Q238·459/508 |
| 2026-06-13 | **142차** — §1-4·§6-3-1 G9-COG import gate·V99·apply-nhis-seeds·G9-COPAY-NAMING·Q260·Q311·Q313·`8bb6583`·`a5c2736`·902/1022 |
| 2026-06-13 | **141차** — §1-4·§6-2-11·§6-3-1 G9-COG·FAQ21824·G-7x-1 YearMonth·Q311·Q312·`2efc557`·`6ef671b`·894/1017 |
| 날짜 | 변경 내용 |
|------|----------|
| 2026-06-15 | **164차** — §1-4·§6-2-9f·§10-10·§10-14 v1.3-B FE wire·L03_M01 V123·Q347·Q348·`9bd1660`·`edfba7f`·1274/1274·1131/1131 |
| 2026-06-14 | **163차** — §1-4·§10-10·§10-14 G21 기간 가드·v1.3-B suggest API·V120~V122·Q330·Q347·`230659a`·`c865d2b`·1267/1267·1121/1121 |
| 2026-06-14 | **162차** — §1-4·§6-2-9c·§6-2-9d·§10-14 L03_M13·L03_M04 FE wire·Q344~Q346·`090b2d7`·`97108f2`·1261/1263·1115/1115 |
| 2026-06-14 | **161차** — §1-4·§6-2-9a·§6-2-9b·§10-14 L03_M14 FE wire·미래일자 가드·Q343~Q344·`63cb193`·`962858b`·1228/1228 |
| 2026-06-14 | **160차** — §1-4·§6-2-9a·§6-2-9b·§10-14 L03_M11 V115·L03_M14 V116·Q340~Q343·`e95df4c`·`5780c65`·1209/1209 |
| 2026-06-14 | **159차** — §1-4·§6-2-9·§10-14 G-NURSING V114·Q336~Q339·`24a1c5c`·`024e720`·1073/1192 |
| 2026-06-14 | **158차** — §1-4·§10-11·§10-11-1·§10-14 G17b V112/V113·Q333~Q335·`3bd6a43`·`487416d`·1060/1164 |
| 2026-06-14 | **157차** — §1-4·§6-2-10·§10-12·§10-14 G21 batch-confirm·G42 익명함 intake·US-UX-05·V111·Q330~Q332·`ba7d84f`·`c26cfa7`·1060/1160 |
| 2026-06-14 | **154차** — §1-4·§10-8·§10-14 J03 quiet-hours billing UI·7-5 provider deepen·Q329·`9a4ab8e`·`111f056`·1030/1141 |
| 2026-06-14 | **153차** — §1-4·§10-14 G2/7-5 V110·US-L06·Q328·`16a0734`·`51f2505`·1024/1133 |
| 2026-06-14 | **152차** — §1-4·§10-14 G2/7-5 easy payment·V108–V109·Q326·Q327·`b893e97`·`bebd874`·1023/1126 |
| 2026-06-14 | **151차** — §1-4·§10-12 G41b compliance API·V107·Q325·`0f11158`·`ee42e5d`·246/1110 |
| 2026-06-14 | **148차** — §1-4·§6-2-9a·§6-2-11 G30 checklist·G34-QUAL panel·US-S02 POST·Q320·Q319·Q294·`b1dfd34`·`574bd08`·989/1088 |
| 2026-06-14 | **147차** — §1-4·§6-2-9a·§10-8 G34-QUAL BE guard·UXD-97 J03 a11y·Q318·Q319·`726b3de`·`76b5ff0`·975/1084 |
| 2026-06-14 | **146차** — §1-4·§10-8 J03 readiness UI·email·quiet-hours·8-12 pagination·G34-QUAL·Q318·Q319·`fffd355`·`443efca`·968/1081 |
| 2026-06-14 | **145차** — §1-4·§6-2-4·§6-2-10·§10-8 8-12 BE CSV·G42 결재·사후관리·#44 V103·J03 channel-status·Q316~Q318·`bc927f7`·`6012044`·960/1071 |
| 2026-06-13 | **140차** — §1-4·§6-2-10·§6-3 G42 pending-approval·G-7x-1-guard·US-T14 익명함·Q309·Q310·`6f6094d`·`338c014`·886/1009 |
| 2026-06-13 | **139차** — §1-4·§6-2-4·§6-2-9 US-R02 직원현황 리포트·G34b import-draft API·Q308·`8487667`·`02cbd05`·882/1001 |
| 2026-06-13 | **138차** — §1-4·§6-2-10·§10-12 G42 고충상담·G34b 전월 복제·G21 check-in guard·Q305·Q306·Q307·`0460e9b`·872/989 |
| 2026-06-13 | **137차** — §1-4·§6-2-9·§10-12 G34b 업무수행일지 불러오기·G21 assignedUser guard·Q303·Q304·`0ce04ad`·850/960 |
| 2026-06-13 | **136차** — §1-4·§6-2-8 G40b 반기 기초평가·V95/V96·Q302·`a7b4a39`·`fad6df1`·845/948 |
| 2026-06-13 | **135차** — §1-4·§6-2-7 G40 대시보드 widget·V94·duplicate compliance·`2589b94`·`e89175e`·831/931 |
| 2026-06-13 | **134차** — §1-4·§6-2-7 G40 FE 위험도평가 UI·QA-B62·`686d686`·`9f80082`·830/925 |
| 2026-06-13 | **133차** — §1-4·§6-2-6·§6-2-7 G40 admission risk assessment·V93·US-R03 per-staff compliance·Q300·Q301·827/917 |
| 2026-06-14 | **132차** — §1-4·§6-2-6 FAQ21806 onboarding compliance·V92·Q300·813/908 |
| 2026-06-13 | **131차** — §1-4·§10-13 G2 CMS cancel·history·duplicate guard·Q299·807/900 |
| 2026-06-13 | **130차** — §1-4·§6-2-3~5 US-R03 HR file hub·V90/V91·FAQ21806·G2 CMS reactivation·Q298·797/898 |
| 2026-06-13 | **129차** — §1-4·§6-2-3 G21 xls Content-Type casing·US-S02 입사일 미등록 StatCard·V90 WT·Q294·Q297·786/883 |
| 2026-06-13 | **128차** — §1-4·§6-2-4 US-R02 staff health checkup 8-10·V89·G21 legacy xls·Q296·Q297·785/883 |
| 2026-06-13 | **127차** — §1-4·§6-2-3 US-S02 refresher training certificate upload·V88·Q295·764/871 |
| 2026-06-13 | **126차** — §1-4 US-S02 refresher training·G34 sign modal·US-R03 lifecycle UX·G21 import MIME·Q294·755/866 |
| 2026-06-13 | **125차** — §1-4 US-R03 V87 date integrity·lifecycle Badge·Q293·743/853 |
| 2026-06-13 | **124차** — §1-4 US-R03 offboarding guard·G21 draft sync·G34 signature audit·QA-B55·741/844 |
| 2026-06-13 | **123차** — §1-4 US-R03 staff lifecycle BE+FE·G21 `588bfb1`·Q290 Partial Fixed·731/843 |
| 2026-06-12 | **122차** — §1-4 G21 legacy paired guard·G24 fiscal-year parsing·G34 live E2E·BNK-125~127·Q289~Q292·724/827 |
| 2026-06-12 | **118차** — §1-4 G34 lead caregiver work log BE+FE·G21 paired linkage guard·Q284·Q288·689/800 |
| 2026-06-12 | **117차** — §1-4 LifecycleWorkflowPanel G17/G32·G21 paired visit guard·Q238·Q283~Q287·675/782 |
| 2026-06-12 | **116차** — §1-4 QA-B49 parallel fallback·G17/G32 edit-flow pilot E2E·Q283·672/778 |
| 2026-06-12 | **115차** — §1-4 QA-B49 billing/NHIS snapshot·FE compliance snapshot-first·Q280·Q282·667/773 |
| 2026-06-12 | **114차** — §1-4 G17/G32/G38/G39 dashboard compliance snapshot·DateInput G11/G15·Q280·Q281·667/772 |
| 2026-06-12 | **113차** — §1-4·§10-11-1~3 G17/G32 edit UI·G39 dashboard 4-pillar·dashboard compliance counts·Q279·666/769 |
| 2026-06-12 | **112차** — §1-4·§6-2-2 G38 monitoring UI·branch-scoped compliance·dashboard partial-load·Q277 Fixed·661/765 |
| 2026-06-12 | **111차** — §1-4·§6-2-2·§10-11-3·§10-12 G38·G39·G21 import validation·G37 MIME tighten·Q276~Q278·659/751 |
| 2026-06-12 | **110차** — §1-4·§10-12 G21 visit enum normalize·G37 attachment E2E·Q275·642/735 |
| 2026-06-12 | **109차** — §1-4·§6-2-1 G37 grade history attachments·BNK-105·V78/V79·Q274·637/725 |
| 2026-06-12 | **108차** — §1-4·§6-3·§10-8·§10-11-1·§10-13 J03 primary guardian·CMS FAILED response·UXD-81·BNK-102~104·Q272·Q273·623/705 |
| 2026-06-12 | **102차** — §1-4·§6-3·§10-11-1 G33 settle UI·G17 BNK-100/101·CMS failed debit·Q270 Fixed·Q271·608/693 |
| 2026-06-11 | **101차** — §1-4·§6-3 G33 settle API·V77·claim guard·Q270·604/682 |
| 2026-06-11 | **100차** — §1-4·§6-3 G33 BNK-94 billing start balance·온보딩 체크리스트·Q269·603/679 |
| 2026-06-11 | **99차** — §1-4·§6-2·§10-11-2 UXD-79 지표29 StatCard·파일럿 fixture·US-D01 primaryGuardian·tenant filter·Q266 Fixed·Q268·584/662 |
| 2026-06-11 | **98차** — §1-4·§6-2·§10-8·§10-11-2 BNK-92 G32 plan FE·지표29 compliance·hq_admin 이용자 등록·Solapi template guard·Q265 Fixed·Q266·Q267·581/654 |
| 2026-06-11 | **97차** — §1-4·§10-4·§10-11-2 BNK-91 P2 NHIS copay·discrepancy UX·G32 plan field·CMS re-register·Q264·Q265·577/649 |
| 2026-06-11 | **96차** — §1-4·§10-4 BNK-87 NHIS comparison FE UI·Q264 Fixed·576/646 |
| 2026-06-11 | **95차** — §1-4·§10-4·§10-11-1·§10-11-2 BNK-87 NHIS comparison API·V74·G17/G32 compliance·dashboard 30일 widget·Q264·576/631 |
| 2026-06-11 | **94차** — §1-4·§10-11-1·§10-11-2 G17·G32 FE·G32 case management API·Q262 Fixed·Q263·569/626 |
| 2026-06-11 | **93차** — §1-4·§10-4·§10-11-1 US-M03 7-9 copay refund·G17 functional recovery API·Q261·Q262·559/614 |
| 2026-06-11 | **79차** — §1-4·§10-10·§10-12 V65 transport contract integrity·G21 duplicate visit import·QA-B19 geocode guard 강화·Q234·Q235·457/485 |
| 2026-06-11 | **78차** — §1-4·§10-10 G15 출석 transportMode 이원화·QA-B19 geocode 저장 차단·Q232·Q233·455/484 |
| 2026-06-10 | **77차** — §1-4·§10-4 G11 출석 기반 자동 가산·preview API·가드 보강·Q225·Q229·450/476 |
| 2026-06-10 | **76차** — §1-4·§10-10 G15 transport contract API·FE 연동·V64·Q230·Q231·444/472 |
| 2026-06-10 | **75차** — §1-4·§10-4·§10-10 G11 가산율 catalog·G15 수칙 UI·US-M04 cap success banner·Q226·Q229–Q230·434/467 |
| 2026-06-10 | **74차** — §1-4·§10-4·§10-13 G27 인지지원 월한도 BE·US-L01 bank branchId Fixed·Q226·Q227·Q228·420/451 |
| 2026-06-10 | **73차** — §1-4·§10-4·§10-13 BNK-49 US-M04·US-L01 bank FE UI·Q226·Q227·Q228·414/447 |
| 2026-06-10 | **72차** — §1-4·§10-4·§10-13 BNK-47 월한도 가드·BNK-48 은행 일괄입금·Q226–Q227·401/432 |
| 2026-06-10 | **71차** — §1-4·§6-3·§10-4 US-M03 청구 생성 기준·전월 미납 가드·V63·Q224–Q225·390/428 |
| 2026-06-10 | **70차** — §1-4·§10-8·§10-9 G2 templates 5종·납부확인서·노인학대예방 UI·G19·Q221–Q223·383/413 |
| 2026-06-10 | **69차** — §1-4·§10-6·§10-13 US-L01 payment guard·notify dedupe·CMS RBAC·Q218–Q220·377/408 |
| 2026-06-10 | **68차** — §1-4·§10-8·§10-9 G2 email templates 3종·resolveDurationBand·Q204·Q213·Q216–Q217·371/402 |
| 2026-06-10 | **67차** — §1-4·§6-3-1·§10-13 G9 V62 snapshot·FeeScheduleMatrix·CMS 단건 guard·Q213–Q215·365/382 |
| 2026-06-10 | **66차** — §1-4·§6-3-1 G9 duration_band·수가표 API·US-J02·Q210–Q212·363/373 |
| 2026-06-10 | **65차** — §1-4·§10-8 G21 confirm-lock UX·G2 SMTP email·Q204·Q209·361/367 |
| 2026-06-10 | **64차** — §1-4·§10-6·§10-13 US-L03 CMS·FCMS stub·V59/V60·Q206–Q208·353/358 |
| 2026-06-10 | **63차** — §1-4·§10-8 US-J03 email channel·US-L02 discharged names·Q204–Q205·342/350 |
| 2026-06-10 | **62차** — §1-4·§10-6 US-M02 dashboard counts·US-L02 overdue widget·BillingContextNav·V58·Q202–Q203·335/346 |
| 2026-06-09 | **61차** — §1-4·§10-6·§10-12 US-L02 overdue pagination·US-L01 payment names·G21 paired sync·V57·UXD-64·Q197–Q201·334/340 |
| 2026-06-09 | **60차** — §1-4·§10-6·§10-12 G2 notify·US-L01/L02·US-V02 cascade·BNK-26·Q109·Q174·Q194–Q196·329/323 |
| 2026-06-09 | **59차** — §1-4·§4-2·§10-12 change-password·UXD-63 visit import UI·V56·Q122·Q189·Q192·311/316 |
| 2026-06-09 | **58차** — §1-4·§4-2·§10-12 G21 visit import·SEC-D17 settings·fieldErrors·Q189–Q191·306/306·90/298 |
| 2026-06-10 | **57차** — §1-4 UXD-62 GuardianDailySummary 식사·Q188·288/288·89/289 |
| 2026-06-10 | **56차** — §1-4·§10-6·§10-9 BNK-22 US-J03-h NotificationHistoryPanel·Q152 Fixed·Q187·288/288·89/287 |
| 2026-06-10 | **55차** — §1-4·§10-6·§10-11 BNK-19 US-M02-b·UXD-59·Q161 Fixed·Q183–Q186·294/294·86/277 |
| 2026-06-09 | **54차** — §1-4·§10-5 UXD-58 NHIS 대기 보류 UI·Region 테스트·Q181·Q182·288/288·81/267 |
| 2026-06-09 | **53차** — §1-4·§10-5 Epic V `/visits` UI·G7 PENDING_REVIEW·V54·Q180 Fixed·Q181·269/269·80/259 |
| 2026-06-09 | **52차** — §1-4·§4-2·§6-3 v1.2.1 G14·US-M01~M03·설정 RBAC·V51–V53·Q176–Q180·264/264·235/235 |
| 2026-06-08 | **43차** — §1-4·§6-3-1·§10-6·§10-10 UXD-47 transport unconfirm UI·StaffPage a11y·PATCH contract·Q163·Q164·226/226·58/179 |
| 2026-06-08 | **42차** — §1-4·§6-3-1·§10-6·§10-10 v3 §3-8 StaffPage·transport unconfirm·Q162·Q163·226/226·55/170 |
| 2026-06-08 | **41차** — §1-4·§10-6·§10-11 v3 meals/programs API·V49·Q160 Fixed·Q161·224/224·54/164 |
| 2026-06-08 | **40차** — §1-4·§10-6·§10-10 v1.3-A transport API·V47·식사·프로그램 shell·Q159·Q160·212/212·53/157 |
| 2026-06-08 | **39차** — §1-4·§10-6·§10-8 PAID 수납 알림·UNMATCHED 후보 검색·배차 shell·Q135·Q159·202/202·50/150 |
| 2026-06-08 | **38차** — §1-4·§10-6·§10-8 US-G06 DISCREPANCY compare·AlimtalkFallbackText·Q135·Q158·198/198·46/143 |
| 2026-06-08 | **37차** — §1-4·§10-6·§10-8 UXD-41 IncidentRecordForm·AlimtalkTemplateVariables·Q157·191/191·45/137 |
| 2026-06-08 | **36차** — §1-4·§10-6·§10-8 Q154 Fixed·UXD-40·J03 service E2E·Q155·Q156·185/185·44/130 |
| 2026-06-08 | **35차** — §1-4·§10-6 UXD-39 건강·NHIS UI·J03 vitals DAILY_CARE·Q154·179/179·40/115 |
| 2026-06-07 | **34차** — §1-4·§10-6 US-E01~E05 출석 UI·V46·178/178·36/110·Q94·Q96·Q109 |
| 2026-06-07 | **24차** — §1-4 COD 35차 FE-17 LogoutButton·PublicAuthLayout·GuardianInvitationAcceptForm (Q141) |
| 2026-06-07 | **23차** — §1-4·§10-6 COD 34차 GuardianInvitationAcceptPage·FE-16 ds-* (Q139–Q140) |
| 2026-06-07 | **27차** — §6-4-1 V40 지점명 case-insensitive UK (Q146) |
| 2026-06-08 | **29차** — §1-4·§10-6·§10-8 Must FE·Solapi J03·V44·152/152·40/40 |
| 2026-06-08 | **28차** — §1-4·§10-6·§10-7·§10-8 V43 Fixed·J03·프론트 baseline·147/147 |
| 2026-06-07 | **25차** — §1-4·§10-6·§10-7 COD 36 V42 consent CHECK·GuardianListCard WIP (Q142–Q143), 테스트 253/253 |
| 2026-06-07 | **21차** — §1-4 UXD 22차 PaymentRecordModal·ReconciliationSummaryBar·DiscrepancyComparePanel·MonthInput (Q134–Q136) |
| 2026-06-07 | **19차** — §1-4·§3-2·§4-2·§4-5 PlatformOrgDetailModal·SettingsPage 5탭·LoginHistoryPanel·PasswordReset (Q125–Q127) |
| 2026-06-07 | **18차** — §1-4·§4-2·§10-6·§10-7 Recharts·설정 패널·V41 notification·PasswordChange·GuardianInvite (Q118–Q124) |
| 2026-06-07 | **17차** — §1-4·§6-3-1 수가표 이력 보기 UI(Q117 UXD 14차) |
| 2026-06-07 | **16차** — §6-3 Switch 셀프 체크인 토글 UI(Q116)·§1-4 `/settings` 상태 갱신 |
| 2026-06-07 | **13차** — §1-4 ClientFormPage UXD 10차(primaryGuardian·CopayTypeSelect·Q113 client_user/사진 UI-only) |
| 2026-06-06 | **12차** — NHIS guidance API §10-5·US-D03 상세 탭(Q102)·SessionTimeout(Q112)·테스트 28/127 |
| 2026-06-06 | **11차** — v1.2 SideNav·보호자/입금/미납·QR 부분 연동·V39·§10-6 출석 통계 (FAQ Q107–Q110) |
| 2026-06-06 | **10차** — CHANGELOG V38–V39·라우트 등록·API 최신화, §1-4 구현 상태 갱신, Q104 정정·Q106 |
| 2026-06-08 | §1-4·§6-3·§10-6 App.jsx 2차 라우트·BranchesPage 미등록·UI 골격 (FAQ Q104–Q105) |
| 2026-06-07 | §1-4·§10-5 NHIS import·대사 필드 불일치·`/clients/:id/edit`·상세 탭 (FAQ Q100–Q103) |
| 2026-06-07 | §1-4·§3 플랫폼 목록 `List` vs `items`·hq_admin 발급 본문 불일치 (FAQ Q97) |
| 2026-06-07 | §6-3-1 수가표 API-only·§10-6 Must API-only·§4-2 설정 역할 불일치·§3-3 표 서식·미등록 라우트 (FAQ Q87–Q91) |
| 2026-06-07 | §1-4·§3 대시보드 API-only·플랫폼 검색 `?query=`·§3-2 표 서식 수정 |
| 2026-06-06 | ClientDetail·Guardian·Reconciliation UI·API 경로 불일치(FAQ Q83) — §1-4 |
| 2026-06-06 | `/platform` UI API 연동 반영 — §1-4·§3-2 Tenant 등록·관리자 발급 화면 |
| 2026-06-06 | V36–V37: lifecycle temporal sanity·NHIS claimId 인덱스·인증 rate limit·ProductionSecretValidator |
| 2026-06-06 | V35: 수가표·QR actor backstop 트리거·§4-3 actor 컬럼 확장 |
| 2026-06-06 | V34: 퇴소 시각 CHECK·지점별 purge 인덱스·NHIS 수동 매칭 API §10-5 |
| 2026-06-06 | V32–V33: actor backstop 트리거·퇴소 purge 인덱스·청구 상태 필터 API·§4-3 actor 컬럼 |
| 2026-06-06 | V29–V31: 사업자번호 검색·Tenant 이메일 UK·비밀번호 재설정 세션 폐기·청구 상태 DB 인덱스 |
| 2026-06-06 | 플랫폼 Tenant 검색·주민번호 복호화 API·Flyway V27–V28 성능 인덱스 반영 |
| 2026-06-06 | 설정 API·백업 스케줄러 구현 반영, 환경변수·NHIS 대사 보강 |
| 2026-06-05 | 초안 작성 — `platform_admin`·`sysadmin` 가이드 |

---

*이 문서는 tech_writer 에이전트가 관리합니다. API·UI 변경 시 §1-4 구현 상태를 동기화하세요.*
