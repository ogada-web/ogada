<!-- doc:owner=UXD doc:audience=PLN,COD,TSR updated=2026-06-12T22:30:00+09:00 -->
# ogada 디자인 시스템 (product/DESIGN_SYSTEM.md)

> **작성**: ux_designer 에이전트 (`UXD`)
> **최초 작성일**: 2026-06-06
> **최종 갱신**: 2026-06-12 (87차 — **US-R03 직원 lifecycle FAQ21825 + StaffDetailPage + 접근성 재점검** — USER_STORIES 115차 신규 P2 Epic G-Staff-LC(이지케어 FAQ21825 입사~퇴사)가 frontend 0건이던 갭을 client lifecycle(G24/G14)과 대칭 surface로 해소. ① **`staffLifecycleCompliance.js`** — FAQ 21825 4단계(입사·신고·근로·퇴사)·서류 체크리스트·`buildStaffLifecycleSteps`. ② **`StaffLifecyclePanel`** — `LifecycleWorkflowPanel`+단계별 `region` 체크리스트·보수교육 `/staff/training` 링크(US-S02 후속)·입사/퇴사 `role=alert` 경고. ③ **`StaffDetailPage`** `/staff/:id` — 기본정보·입사~퇴사 `Tabs`·`StaffContextNav`·breadcrumb. ④ **`StaffPage`** — 이름·상세 링크 `aria-label`에 직원명 포함(WCAG 2.4.6). ⑤ **`.ds-staff-lifecycle-panel*`** CSS·`forced-colors`는 client 패널 선택자 공유. 회귀 +7. `npm test`·build·audit 검증.)
> **이전 갱신**: 2026-06-12 (86차 — **US-T09·US-T10 ClientDetail 탭 + US-S01 StaffContextNav + G34 행 액션 접근성** — USER_STORIES 111~112차 P2 갭(정기 욕구사정 FAQ21800·급여계약 lifecycle FAQ21805)이 `ClientDetailPage` 탭 surface 없이 `LifecycleWorkflowPanel`만 존재하던 잔여를 해소. ① **`ClientNeedsAssessmentPanel`** — 기초평가 탭: 8항목 FAQ21800 필드 안내·이전 기록 비교 region·`buildNeedsAssessmentLifecycleSteps`. ② **`ClientBenefitContractPanel`** — 급여계약 탭: 등급이력과 분리·계약 타임라인·`buildBenefitContractLifecycleSteps`. ③ **`StaffContextNav`** — `/staff`↔`/staff/lead-caregiver-log` cross-page `nav`·`aria-current`(US-S01·G34). ④ **`LeadCaregiverWorkLogPage`** — 행별 수정·전자서명 `aria-label`에 이용자명 포함(WCAG 2.4.6). ⑤ **`navConfig`** — SideNav 기록 그룹에 선임 업무수행일지·`EXACT_MATCH_PATHS` 등록. ⑥ **`.ds-client-lifecycle-panel*`** CSS·`forced-colors` 경계선. 회귀 +7. `npm test`·build·audit 검증.)
> **이전 갱신**: 2026-06-12 (85차 — **G34·US-T09·US-T10 lifecycle 공통 UX 보강** — USER_STORIES 111차 신규 갭인 선임 요양보호사 업무수행일지(G34), 정기 욕구사정(FAQ21800), 수급자 급여계약 lifecycle(FAQ21805)은 모두 연/비정기 업무·기한·증빙·서명 상태를 동시에 보여줘야 하므로, API 확정 전 공통 presentational 컴포넌트 **`LifecycleWorkflowPanel`**을 신설. ① 단계별 상태 `LIFECYCLE_STATUS`(`DRAFT/SCHEDULED/IN_PROGRESS/DUE_SOON/OVERDUE/COMPLETED/SIGNED/RENEWED/TERMINATED`)를 `StatusBadge` 텍스트+색상 라벨로 표준화. ② 각 단계는 기한·완료일·담당·서명 필요/완료·증빙 목록을 텍스트로 노출하고, `OVERDUE`는 좌측 보더+danger soft+「기한 초과」Badge로 색상 의존을 피함. ③ `.ds-lifecycle*` CSS와 `forced-colors` 경계선·outline 보강. ④ barrel export + 회귀 3건(`LifecycleWorkflowPanel.test.jsx`). coder 메모: 실제 `/staff/lead-caregiver-log`, `ClientDetailPage` 기초평가/계약 탭은 이 패널을 붙이고 API·권한만 연결.)
> **이전 갱신**: 2026-06-12 (84차 — **G11·G15 폼 날짜 입력 `DateInput` 표준화 회귀 해소(FE-16·§1 단일 원천)** — 64차에서 확립한 「Must·도메인 폼 `type=date` raw input **0건** — `DateInput`/`MonthInput` 컴포넌트만 허용」 규율이, 이후 신설된 두 패널에서 회귀해 적용일 필드가 raw `<TextInput type="date">`로 남아 공유 날짜 입력 토큰(`.ds-date-input` 폭 캡)을 적용받지 못하던 갭을 해소(다른 날짜 폼 — `ClientFormPage` 생년월일·`PaymentRecordModal` 입금일·`VisitScheduleForm` 방문일 등과 시각·동작 불일치). ① **`FeeSurchargeGuidePanel`(G11 가산율 미리보기)** 「제공일」 필드를 `DateInput`으로 전환(시각/시간 필드는 `type=time`로 유지). ② **`TransportCompliancePanel`(G15 이동서비스 계약)** 「수급자(보호자) 서명일」·「기관 담당자 서명일」 2개 필드를 `DateInput`으로 전환 — `max={todayIsoDate()}` 미래 일자 차단·`disabled`·`Field` `error`(`aria-invalid`) 바인딩 보존. ③ raw `type=date` 잔존 컴포넌트 **0건** 재확인(스캔: `DateInput`/`MonthInput` 내부만 잔존). 순수 표준화 리팩터로 동작 불변. 회귀 +2(`FeeSurchargeGuidePanel.test.jsx`·`TransportCompliancePanel.test.jsx` — `.ds-date-input` 클래스·`type=date` 검증). `npm test` **772/176 PASS**·build PASS·audit 0.)
> **이전 갱신**: 2026-06-12 (83차 — **US-T08 G39 지표44 대시보드 위젯 + 접근성 재점검** — USER_STORIES US-T08(BNK-109) 인수 조건 「dashboard StatCard/widget — indicator-44 compliance widget on DashboardPage」 잔여 P2 해소. ① **`DashboardPage` 4개 위젯** — `fetchProvisionResultComplianceApi` 연동·`countProvisionResultAnnualEvaluationGaps`·`countProvisionResultReflectionGaps` 집계 — 「급여제공결과 평가 미등록」·「평가 30일 미반영」(gap, tone=warning)·「급여제공결과 평가」·「평가 반영」(status 충족/미충족/대상없음, `/programs/provision-result-evaluations` 링크). ② **`provisionResultCompliance.js`** — gap count·dashboard widget label 상수·view model `annualEvaluationGapCount`/`reflectionGapCount` 확장. ③ **`dashboardSummary.js`** — branch/HQ widget 필드 전달. ④ **`.ds-provision-result-compliance`** `forced-colors` StatCard 경계선. 회귀 +5. `npm test`·build·audit 검증.)
> **이전 갱신**: 2026-06-11 (82차 — **US-M01-g G37 등급 인정기간 첨부 UI + 접근성 재점검** — USER_STORIES US-M01-g·API_SPEC §4-2 G37·FLOWCHART §4 대비 **frontend 첨부 UI ❌ P1** 잔여 갭 해소(backend CRUD @ `0325d95`). ① **`GradeHistoryAttachmentPanel`** — `<details>`/`<summary>` lazy-load·`fetchLtcGradeHistoryAttachmentsApi`·`FileUpload`(PDF/PNG·10MB 클라이언트 가드)·미리보기(PDF `window.open`·PNG `Modal`)·삭제·행별 `aria-label`(등급 변경 문맥). ② **`GradeHistoryTimeline`** — `clientId`·`userRole` RBAC(branch_admin/social_worker 업로드·caregiver 읽기) 연동·`attachmentCount` 배지. ③ **`services.js`** — list/upload/delete/`apiFetchBlob` download. ④ **`.ds-grade-history-attachments*`** CSS·`forced-colors` 경계선. ⑤ **`config/gradeHistoryAttachments.js`** — MIME·크기 검증 단일 원천. `ClientDetailPage` 등급 탭 연동. 회귀 +9. `npm test`·build·audit 검증.)
> **이전 갱신**: 2026-06-11 (81차 — **US-L05 G33 1회 설정 UX + US-M03 대장 컨텍스트 네비 + US-T07 RecordsContextNav + NHIS 비교 링크·접근성 재점검** — USER_STORIES·FLOWCHART 잔여 갭 해소. ① **`BillingStartBalanceOneTimeWarning`**·**`BillingStartBalanceLockedNotice`** — G33 청구시작 기준금액 1회 설정 사전 경고(`role=status`·submit `aria-describedby`)·잠금 후 수정 불가 안내(적용월 문맥)·`BillingSettingsPanel` 연동(US-L05). ② **`BillingReportsContextNav`** — 청구·입금·수납·환불 대장 + 간편계산기 cross-page `nav`·`aria-current` — `BillingReportPage`·`CopayCalculatorPage` 연동(US-M03). ③ **`CaseManagementPage`** — `RecordsContextNav` 연동(US-T07·G32). ④ **`BillingNhisComparisonPanel`** — 깨진 `/billing/reconciliation` 링크 → `/billing/imports/nhis`(한국어 라벨). ⑤ **`navConfig` `EXACT_MATCH_PATHS`** — 청구 하위 11경로 추가(SideNav 활성 오매칭 방지). ⑥ **`.ds-billing-start-balance-notice`** `forced-colors` 경계선. 회귀 +6. `npm test`·build·audit 검증.)
> **이전 갱신**: 2026-06-11 (80차 — **미정의 `ds-text-input` 클래스 제거 + 인라인 너비 style → 유틸리티 클래스(FE-16·§1)** — `CaseManagementPage`(US-T07)·`FunctionalRecoveryPage`(US-T06) 필터·폼의 raw `<input className="ds-text-input">`가 **CSS에 정의되지 않은 클래스**여서 공유 입력 토큰(`.ds-input` 테두리·높이·포커스·`aria-invalid` 경계색)을 전혀 적용받지 못하고, 폭은 인라인 `style={{ width: "90px" }}`/`{{ width: "160px" }}`로만 지정되던 갭을 해소(FE-16 「인라인 style → ds-* 유틸리티」 회귀). ① 4개 raw `<input>`(연도·계획연도·참석자)을 **`TextInput`** 컴포넌트로 전환 — `.ds-input` 표준 스타일·`aria-describedby`/`aria-invalid` 전달 유지. ② **`.ds-input--year`**(`max-width: 6rem`)·**`.ds-select--inline`**(`max-width: 12rem`) 신규 유틸리티 승격 — `.ds-month-input`/`.ds-date-input` `max-width` 캡 패턴과 정합, 360px 반응형 축소 보존. ③ `CaseManagementPage` 분기 `Select` 인라인 `style` → `.ds-select--inline`. 순수 스타일 정합 리팩터로 동작 불변. 회귀 +1(`FunctionalRecoveryPage.test.jsx` — 연도 필터 `.ds-input`·`.ds-input--year` 클래스 검증). `npm test` 681/165 PASS·build 869 modules(max 465 kB)·audit 0.)
> **이전 갱신**: 2026-06-11 (79차 — **US-T07 지표29 평가 실시 StatCard + 대시보드 위젯 + StatCard tone 접근성** — USER_STORIES US-T07(BNK-93~94) 잔여 P1 해소. ① **`CaseManagementPage`** — `evaluationConductedMet` 4번째 compliance `StatCard`·미충족 시 `Alert`(지표29) — `mapCaseManagementComplianceView`·`countCaseManagementEvaluationGaps`. ② **`DashboardPage` 9번째 위젯** — 「사례관리 평가 미실시」(`caseManagementEvaluationGapCount`, tone=warning, `/case-management/meetings` 링크) — 지표43 30일 미반영 위젯과 쌍으로 G32 compliance 4기둥 대시보드 소비. ③ **`StatCard` tone 확장** — `success`·`warning`·`neutral` CSS(`--success-text`·`--warning-text`·`--text-secondary`) — `FunctionalRecoveryPage`·`CaseManagementPage` 준수 현황 카드 색+텍스트 병행. ④ **`caseManagementCompliance.js`** — evaluation gap 집계·view model. 회귀 +6. `npm test`·build·audit 검증.)
> **이전 갱신**: 2026-06-11 (78차 — **US-G04 NHIS import 연도 수가 업로드 가드 + NhisImportContextNav + 접근성 재점검** — USER_STORIES US-G04(QA-B37)·FLOWCHART §7-1 대비 잔여 갭 해소. ① **`NHISImportPage` 업로드 차단** — `feeScheduleYearCoverage()` 기반 불완전 25셀 그리드 시 제출 `disabled`·핸들러 이중 가드·에러 메시지(등록/기대 칸수). ② **`FeeScheduleYearGuardBanner`** — `id`·`title` prop·`Alert role=status` — 업로드 버튼 `aria-describedby` 연결(WCAG 1.3.1, `ClaimGenerationPanel` 패턴 정합). ③ **`NhisScheduleConfirmLockGuide`** — 확정 잠금 경고 `id`·`title` — 청구 잠금 시 업로드 버튼 `aria-describedby`. ④ **`NhisImportContextNav`**(신규) — `AttendanceContextNav` 패턴, `/billing`↔`/billing/imports/nhis`·reconciliation 하위 경로 `aria-current` — `NHISImportPage`·`ReconciliationPage` 연동. 회귀 +5. `npm test`·build·audit 검증.)
> **이전 갱신**: 2026-06-11 (77차 — **US-L04 의료비공제 UI + ClientOuting/CareProvision/TransportForm18 + Field aria-required + CSS 신규 클래스** — ① **`MedicalExpenseDeductionPanel`**(US-L04 G26) — `GET /clients/:id/billing/medical-expense-deduction?year=` / `GET /guardian/clients/:id/billing/medical-expense-deduction?year=` 연동, 귀속 연도 조회·인쇄·CSV 다운로드(`buildMedicalExpenseDeductionCsv`), `StatCard` 3종 요약(`role="group"`)·납입 내역 `Table`(`caption` sr-only)·합계 행 `ds-medical-expense-panel__total`, CMS·간편결제 제외 안내 `Alert tone=info`. staff variant → `ClientDetailPage` 청구 탭, guardian variant → `GuardianPortalPage`. ② **`ClientOutingPanel`**(G15 2-1-1 BNK-63) — 외출 CRUD(`PLANNED→OUT→RETURNED/CANCELLED`) + 출발·복귀 액션(행별 `aria-label` 이용자명 포함), `OUTING_STATUS`(§2-3). `ClientOutingsPage`(`/transport/outings`)·`ClientOutingReportPage`(`/reports/client-outings`)·`ClientDetailPage` 외출 탭 연동. ③ **`CareProvisionRecordPanel`**(G15/G16) — `GET /care-provision-records?clientId=` 재가급여 기록·방문요양/주간보호 분리 표 — `ClientDetailPage` 기본정보 탭 연동. ④ **`TransportVehicleSelect`**(G16) — 지점 차량 `Select`(`GET /transport/vehicles?branchId=`) — `TransportRunNewPage`·`TransportRunDetailPage` 차량 배정. ⑤ **`TransportForm18GuidePanel`**(G15 별지 제18호) — 신청 절차·공단 3분리 신청 유형(적용·변경·중단)·등록상태 4단·전제조건 안내 — `FeeSurchargeGuidePanel`(G11) 내 탭으로 통합. ⑥ **`TransportCompliancePanel`**(G15) — 이동서비스 수칙 체크리스트(`Checkbox` `aria-describedby` 연결)·서명·계약서·일지 서식 인라인 `Modal` — `TransportRunDetailPage` 탭 연동. ⑦ **`Field` `aria-required`**(WCAG 1.3.1·3.3.2) — `required` prop이 있는 모든 `Field`가 `aria-required="true"`를 하위 컨트롤에 전달(HTML `required` 대신 — 프론트 자체 검증 패턴과 일관). ⑧ **CSS 신규 클래스** 11종 승격 — `.ds-form-actions--start`·`.ds-list-plain`·`.ds-transport-form18__steps/__step`·`.ds-transport-compliance__rules/__progress/__template`·`.ds-medical-expense-panel/__summary/__filters/__total`·`.ds-billing-report-print-zone`(인쇄 영역). `npm test` 574/148 PASS·build PASS·audit 0.)
> **이전 갱신**: 2026-06-11 (76차 — **차량 관리(US-T05/G16) 표 행 액션 접근성 + §8-1 라우트 표 실측 정합** — `VehiclesPage` 차량 목록 행별 「수정」 `Button`이 동일 접근성 이름만 노출해 다중 행에서 스크린리더가 대상 차량을 식별 못 하던 갭(WCAG 2.4.6·4.1.2)을 차량번호 포함 `aria-label`(예: 「12가3456 차량 수정」)로 해소(31차 `GuardianInvitationList` 패턴 정합). §8-1 라우트 표에 누락됐던 `/attendance/boarding`·`/on-site`(US-E06)·`/transport/{vehicles,service-fees,outings}`·`/reports/client-outings`(US-T05/G16·BNK-63) 6경로 추가. 회귀 `VehiclesPage.test.jsx` 행 동작 라벨. `npm test` 558/146 PASS·audit 0.)
> **이전 갱신**: 2026-06-10 (75차 — **기록 모듈 컨텍스트 네비 + 이동 SideNav·접근성 재점검** — USER_STORIES US-F01·N01·N02·V01·G16·FLOWCHART §6·§3-5·§9b 대비 기록(건강·식사·프로그램·방문) 하위 화면 간 **cross-page 탐색**이 SideNav만으로는 부족하던 갭 해소. ① **`RecordsContextNav`** — `AttendanceContextNav`/`BillingContextNav` 패턴 재사용, `nav`(aria-label)·`NavLink` `aria-current="page"`·44px 터치·`forced-colors` — `HealthPage`·`MealsPage`·`ProgramsPage`·`VisitsPage` 상단 연동. ② **`navConfig`** — SideNav 이동 그룹에 **`/transport/service-fees`(G16)** 추가·`EXACT_MATCH_PATHS`에 service-fees·기록 4경로 등록(SideNav 활성 오매칭 방지). ③ **`TransportContextNav.test.jsx`**(+2) — 이동서비스 5경로 landmark·`aria-current` 회귀. ④ **`SideNav`** — 모바일 접힘 시 하위 `ul`에 **`aria-hidden={!isOpen}`** 부여(WCAG 4.1.2 — 접힌 그룹 SR 노출 차단). ⑤ **`BillingContextNav`** — `.ds-billing-context-nav*` → **`.ds-context-nav*`** 단일 클래스로 정합(스타일 공유 선택자와 일치). 회귀 +4. `npm test`·build·audit 검증.)
> **이전 갱신**: 2026-06-10 (73차 — **출석 모듈 컨텍스트 네비 + 청구 생성·법정서식 접근성 재점검** — USER_STORIES US-E01~E06·FLOWCHART §5 대비 출석 하위 화면(현황·탑승·현장·체크인·통계·QR) 간 **cross-page 탐색**이 SideNav만으로는 부족하던 갭 해소. ① **`AttendanceContextNav`** — `BillingContextNav`(US-L01·L02) 패턴 재사용, `nav`(aria-label)·`NavLink` `aria-current="page"`·44px 터치·`forced-colors` — `AttendancePage`·`AttendanceStatsPage`·`QrGeneratePage` 상단 연동. ② **`.ds-context-nav*`** CSS — `.ds-billing-context-nav*`와 공유 선택자 승격(모듈 컨텍스트 네비 단일 원천). ③ **`navConfig` `EXACT_MATCH_PATHS`** — `/attendance/boarding`·`/on-site`·`/checkin`·`/stats`·`/qr/generate` 추가(SideNav 활성 오매칭 방지). ④ **`ClaimGenerationPanel`** — 전월 미입금 가드 시 생성 버튼 `aria-describedby`→`ClaimGenerationGuardBanner` `id`·`aria-busy`·가드 오류 `id` 연결(WCAG 1.3.1, QA-B19·Transport geocode 패턴 정합). ⑤ **`GuardianDocumentNotifyPanel`** — `section`+`h3` `aria-labelledby`(US-G02 법정서식). 회귀 +3. `npm test`·build·audit 검증.)
> **이전 갱신**: 2026-06-10 (71차 — **G15·G11 신규 패널 접근성 재점검 + §8-1 라우트 표 실측 정합** — ① **`TransportCompliancePanel`(G15)** 5수칙 `Checkbox`에 `aria-describedby`로 상세 설명 `<p id>` 연결(WCAG 1.3.1 — SR이 라벨+상세 함께 안내). ② **`FeeSurchargeGuidePanel`(G11)** 가산 미리보기 결과를 조건부 마운트 `aria-live`에서 **상시 상주 `role="status"`·`aria-live="polite"`** 컨테이너로 전환(WCAG 4.1.3 — 라이브 영역 안내 신뢰성). ③ **§8-1 라우트 표** — 코드 실측 대비 누락됐던 `/billing/cms`·`/billing/reports/{charges,deposits,receipts}`·`/billing/calculator`·`/transport*`·`/meals`·`/programs`·`/staff`·`/organization/settings`·`/login` 추가, §8-2 그룹 표 **이동**그룹·운영 그룹 확장 반영(단일 원천=`navConfig.js`). 회귀 +3. `npm test`·build·audit 검증.)
> **이전 갱신**: 2026-06-10 (70차 — **US-M04 월한도 배너 + US-L01 은행 엑셀 일괄입금 패널 신설 + USER_STORIES·FLOWCHART 갭 재점검** — ① **`MonthlyBenefitCapBanner`**(US-M04 G27) 신설 — `GET /api/v1/billing/monthly-benefit-cap-guard` 연동, 초과 시 `role="alert"` danger, 90% 이상 시 `role="status"` warning, 정상 시 `role="note"` 안내. 등급 한국어 라벨 병행(색만 의존 금지). `BillingDetailPage` 청구서 정보 카드 상단에 연동(clientId·yearMonth·ltcGrade·totalAmount 전달). ② **`BankDepositImportPanel`**(US-L01 BNK-49) 신설 — `POST /api/v1/billing/imports/bank-deposits` multipart 연동. `FileUpload`·`MonthInput`·`Field error`(`aria-invalid`)·제출 `aria-busy`·결과 `role="status"` 패턴 재사용. `PaymentPage` 하단에 연동(`onImported` 목록 갱신). ③ **`services.js` API 3종 추가** — `fetchMonthlyBenefitCapsApi`·`fetchMonthlyBenefitCapGuardApi`(US-M04)·`importBankDepositsApi`(US-L01 bank). ④ **`.ds-benefit-cap-banner`·`.ds-benefit-cap-notice`·`.ds-bank-import-result`** CSS 승격. ⑤ 회귀 +7(`MonthlyBenefitCapBanner.test.jsx` 4·`BankDepositImportPanel.test.jsx` 3). `npm test`·build·audit 검증 완료.)
> **이전 갱신**: 2026-06-10 (69차 — **`FilterChips` WAI-ARIA radio group 키보드 패턴 정합(접근성 재점검)** — `FilterChips`(US-G07 상태 필터·US-E04 체크인 유형·US-F04 건강 기간 필터에서 재사용)가 `role="radiogroup"`+`role="radio"`+`aria-checked`는 갖췄으나 **키보드 상호작용이 WAI-ARIA radio group 규격에 미달**하던 갭을 해소. 기존엔 모든 칩이 독립 `<button>`(각 칩이 Tab 순서에 포함)으로 화살표 이동·선택이 없어, 같은 코드베이스의 `Tabs`(←/→·Home/End 구현)와 패턴이 불일치했다. ① **roving tabindex** — 그룹을 **단일 Tab 정지점**으로 만들어 선택된 칩만 `tabIndex=0`, 나머지는 `-1`(선택값 없으면 첫 칩이 진입점, WCAG 2.1.1·2.4.3). ② **방향키 이동·선택** — `ArrowRight`/`ArrowDown`은 다음, `ArrowLeft`/`ArrowUp`은 이전(양끝 wrap), `Home`/`End`는 처음/끝으로 이동하며 `onChange`로 즉시 선택(네이티브 라디오 버튼·`Tabs` 동작 정합). 순수 접근성 보강 리팩터로 클릭·`aria-checked`·counts 등 기존 동작·시각 불변. 회귀 +5(`FilterChips.test.jsx` 3→8 — roving tabindex 2·방향키 wrap 2·Home/End 1). `npm test` PASS·build PASS·audit 0.)
> **이전 갱신**: 2026-06-10 (68차 — **FE-14 보안 패널 회귀 테스트 추가 + USER_STORIES/FLOWCHART 갭 점검** — USER_STORIES §17 FE-14 「운영·보안·계정 보안·로그인 이력 UI」중 `AuditLogPanel`·`BackupSettingsPanel`·`LoginHistoryPanel` 3개 컴포넌트에 Vitest 회귀 테스트가 없어 접근성 동작·API 연동·마스킹이 검증되지 않던 갭을 해소. ① **`AuditLogPanel.test.jsx`** 4건 — API 행 렌더·빈 상태·오류 Alert·`eventType` 필터 전달. ② **`BackupSettingsPanel.test.jsx`** 4건 — Switch `aria-checked` off/on·`patchSettings` 호출·성공 메시지·백업 이력 행(`1.0 MB` 포맷). ③ **`LoginHistoryPanel.test.jsx`** 4건 — IP 마스킹(`192.168.***.***`)·실패 로그인 「실패」 라벨·빈 상태·`role` 필터 전달. 접근성 패스 확인: `BackupSettingsPanel` Switch는 기존 `role="switch"` + `aria-checked` 패턴(US-UX-03 정합), `AuditLogPanel`·`LoginHistoryPanel`은 `Table`(`caption`+`scope=col`)·`EmptyState`·`Field` 라벨 연결(`DateInput`+`TextInput`)·오류 `Alert tone=danger` 패턴 준수. `npm test` **402/113 PASS** · build PASS · audit 0.)
> **이전 갱신**: 2026-06-10 (67차 — **US-G00a G9 duration_band 5밴드 UI + US-J02 보호자 명세 보강 + 접근성 재점검** — USER_STORIES US-G00a 인수 조건 「등급×이용시간대(3~6h…13h+) 2차원 다밴드」·backend `DurationBand` @ `425a05f` 대비 frontend 미구현 갭 해소. ① **`config/feeSchedules.js`** — `DURATION_BANDS`(H3_6~H13_PLUS)·`DEFAULT_DURATION_BAND`(H10_13 파일럿)·`durationBandLabel`. ② **`DurationBandSelect`** — `Field`+`Select`·한국어 라벨·`role=note` 선택 안내·기본값 H10_13. ③ **`FeeScheduleTable`·`FeeRateHistoryPanel`·`FeeSchedulePage`** — 이용시간대 열·이력 필터·등록 폼·API payload `ltcGrade`+`durationBand` 정합. ④ **`ClientFormPage`** — 이용자 등록/수정에 이용시간대 필드(US-D01, 청구 수가 매칭). ⑤ **`GuardianPortalPage`** — US-J02 `isGuardianVisibleBillingStatus`·`mergeUniqueBillingRecords`·`handleRetryBilling`·오류 `Alert tone=warning`. 회귀 +5. `npm test`·build·audit 검증 예정.)
> **이전 갱신**: 2026-06-10 (66차 — **US-L03 CMS 자동이체 UI 신설 + 접근성 재점검** — USER_STORIES US-L03·FLOWCHART §7 본인부담 수납 lifecycle 대비 **frontend `/billing/cms` Route ❌** 잔여 갭 해소(backend `StubFcmsClient`·enrollment/debit API @ `2c6e57e` 구현 완료). ① **`CmsPage`** `/billing/cms` — `Tabs` 등록 관리·CMS 출금 분리·`BillingContextNav` 3항목(입금·미납·CMS) 연동. ② **`CmsEnrollmentForm`** — 이용자 연결 보호자·예금주·은행(`CMS_BANK_CODES`)·계좌 끝 4자리 필드 단위 `Field error`(`aria-invalid`+`role=alert`)·제출 `aria-busy`·PIPA 계좌 마스킹 안내. ③ **`CmsEnrollmentTable`** — `StatusBadge` `CMS_ENROLLMENT_STATUS`(등록완료/해지)·계좌 `****1234` 마스킹+`aria-label`. ④ **`CmsDebitPanel`** — 확정 청구서 선택·출금 요청·`CMS_DEBIT_STATUS` 상태 `role=status`·FCMS 스텁 `role=note` 안내. ⑤ **`config/cms.js`**·`services.js` CMS API 4종·SideNav·`navConfig` 청구 그룹 항목 추가. ⑥ **`.ds-cms-debit-status`** CSS·`forced-colors` 경계선. 회귀 +6(`CmsEnrollmentForm`·`CmsEnrollmentTable`·`CmsPage`·`BillingContextNav`). `npm test`·build·audit 검증 예정.)
> **이전 갱신**: 2026-06-10 (65차 — **US-L02 미납↔대시보드 연동 + 입금·미납 컨텍스트 네비 + 접근성 재점검** — USER_STORIES US-L02 인수 조건 「대시보드 미처리 위젯(US-M02)과 연동」·FLOWCHART §7 본인부담 수납 lifecycle 대비 잔여 갭 해소. ① **`DashboardPage` 7번째 위젯 `미납 본인부담`** — `fetchBillingOverduesApi({ page:1, size:1 })`의 `totalElements`를 `dashboardSummary.overdueCount`로 집계·`branch_admin`/`hq_admin`만 노출·`tone=danger`(`>0` 시)·`/billing/overdue` 링크(케어포 7-3 미납 대시보드 패리티). ② **`BillingContextNav`** — `/billing/payments`↔`/billing/overdue` 페이지 상단 `nav`(aria-label)·`NavLink` `aria-current="page"`·44px 터치·`forced-colors` 경계선 — 입금→미납 cross-page E2E(US-L01·L02) 보조. ③ **`OverduePage` 경과일** — `daysOverdue>0` 시 `Badge tone=warning`「N일 경과」텍스트 라벨 병행(색만 의존 금지). ④ **`.ds-billing-context-nav*`** CSS 승격. 회귀 +2(`BillingContextNav.test.jsx`·`dashboardSummary.test.js` overdueCount). `npm test` **342/98 PASS**·build **805 modules 3청크**(max **367 kB**)·audit **0**.)
> **이전 갱신**: 2026-06-09 (64차 — **수가표·본인부담률·방문일정 폼 날짜 입력 `DateInput` 표준화(US-G00a·G00b·V01) + 접근성 재점검** — 28차에서 확립한 「Must 화면 `type=date` raw input **0건** — `DateInput`·`MonthInput`만 허용」 규율이 51차(`FeeSchedulePage`·`CopayRatePage` 복원)·57차(`VisitScheduleForm` 신설) 산출물에서 회귀해, 세 폼의 적용일 필드가 raw `<TextInput type="date">`(또는 `type="date" className="ds-date-input"` 수기 지정)로 남아 있던 갭을 해소. ① **`FeeSchedulePage` 「적용 시작일」**(US-G00a)·**`CopayRatePage` 「적용 기준일」**(US-G00b)·**`VisitScheduleForm` 「방문 날짜」**(US-V01) 모두 `DateInput` 컴포넌트로 전환 — `Field` render-prop 라벨·`id`·`error` 바인딩과 `.ds-date-input` 폭 캡을 단일 원천(`components/ui/DateInput.jsx`)에서 일관 적용해 다른 날짜 폼(`ClientFormPage` 생년월일·`PaymentRecordModal` 입금일 등)과 시각·동작 정합. ② `VisitScheduleForm`은 수기 `className="ds-date-input"` 중복 지정을 제거(컴포넌트가 자동 부여). ③ raw `type="date"` 잔존 화면 **0건** 재확인(스캔 결과 `DateInput`·`MonthInput` 컴포넌트 내부만 잔존). 순수 표준화 리팩터로 동작 불변 — 기존 회귀 유지(`VisitScheduleForm.test.jsx`·`FeeScheduleTable`/`CopayRateTable` 페이지 테스트 라벨 기반 조회 PASS). `npm test` **326/93 PASS**·build **804 modules 3청크**(max **367 kB**)·audit **0**.)
> **이전 갱신**: 2026-06-09 (63차 — **US-V04 공단 방문일정 엑셀 import UI 신설 + 접근성 재점검** — USER_STORIES US-V04·FLOWCHART §9b·API_SPEC §14 「`/visits` import UI — 파일 업로드·미리보기·PLAN/BILLING 매핑」이 **frontend 미구현(잔여)** 이던 갭 해소(backend `POST /visits/imports/nhis` @ `ee3fa3a`·`NhisVisitScheduleImportResponse` 구현 완료, FE UI 부재). ① **`VisitNhisImportPanel`**(`components/visits/`) 신설 — 기존 NHIS import 패턴(`FileUpload`·`Field`·`Switch`) 재사용. **일정 종류 `Select`(PLAN/BILLING 매핑)** + 계획(PLAN)일 때만 **「청구 일정 동시 생성」 `Switch`**(이지케어 계획/청구 이중 import·BNK-10·14, `createPairedBillingSchedule`). 파일 미선택 시 **`FileUpload error`** 필드 단위 오류(WCAG 3.3.1), 제출 `aria-busy`. ② **결과 미리보기** — 업로드 응답(`totalRows`·`importedCount`·`unmatchedCount`·`skippedCount`)을 `Alert tone=info`(`role="status"`)로 SR에 건수 안내 + 행별 결과 `Table`(`caption` SR·인정번호·방문일·시간·결과·사유). 행 결과 상태는 **`VISIT_IMPORT_STATUS`**(`config/visits.js`, backend `IMPORTED`/`UNMATCHED`/`SKIPPED` 정합) `StatusBadge`로 **색 + 텍스트 라벨 병행**(§1-2). ③ **`VisitsPage`** — 일정 등록 폼 아래 `VisitNhisImportPanel` 연동(등록·확정 권한과 동일하게 `branch_admin`·`social_worker`만 노출, import API RBAC와 일치). import 성공 시 `onImported`로 달력 재조회. ④ **`services.js` `importVisitsNhisApi`**(multipart). 회귀 +4(`VisitNhisImportPanel.test.jsx` 3 — 파일 필수 검증·업로드 결과 렌더·BILLING 토글 숨김 · `VisitsPage.test.jsx` +1 import 패널 노출). `npm test` **315/92 PASS**·build **804 modules 3청크**(max **367 kB**)·audit **0**.)
> **이전 갱신**: 2026-06-09 (62차 — **보호자 포털 일일 기록에 식사(meal) 추가(US-I02·FLOWCHART §9) + 접근성 재점검** — FLOWCHART §9 보호자 포털 일일 기록이 「출석·건강·**식사** 기록」으로 정의돼 있고 식사 관리(US-N01, `MealsPage`)가 develop에 구현됐으나, `GuardianDailySummary`는 **출석·건강만** 노출하고 식사 기록이 누락된 갭을 해소. ① **`GuardianDailySummary` 「식사」 행 추가** — `dailyRecord.meals[]`(`mealType`·`intakeLevel`)를 `dl` 요약에 식사 구분 텍스트 라벨(`MEAL_TYPES`, 예: 점심·간식) + 식사량 `StatusBadge`(`MEAL_INTAKE_BADGE` — 잘 먹음/보통/적게, **텍스트 라벨 + 색 병행**, 색만 의존 금지)로 노출. 식사 기록 0건 시 `—`, 식사량 코드 부재 시 「기록 없음」. ② **`config/meals.js` 단일 원천 재사용** — `MealRecordForm` 입력 상수(`MEAL_TYPES`·`MEAL_INTAKE_BADGE`)를 그대로 보호자 열람에 사용(중복 정의 금지). ③ **`.ds-guardian-daily__meals`** CSS — 식사 항목 세로 목록(토큰 기반 gap·정렬). 회귀 +2(`GuardianDailySummary.test.jsx` — 식사 구분/식사량 라벨·빈 식사 `—`). `npm test`·build·audit 검증 완료.)
> **이전 갱신**: 2026-06-09 (61차 — **US-J03 알림 이력 UI + Modal 포커스 접근성 + 표 컴포넌트 정합** — USER_STORIES·FLOWCHART §9-1·API_SPEC §11-5 잔여 갭 해소. ① **`NotificationHistoryPanel`** — `GET /guardian/notifications`·`GET /clients/{id}/notifications` 연동, `NOTIFICATION_CHANNEL`·`NOTIFICATION_STATUS` Badge, `config/notifications.js` eventType 한국어 라벨(templateCode 미노출), `Pagination` 0-based API 변환. ② **`GuardianPortalPage`** — US-I02+J02 탭에 **「알림 이력」** 3번째 탭 추가. ③ **`ClientDetailPage`** — 기본정보 탭 보호자 알림 이력(직원 조회). ④ **`Modal`** — 폼 입력 중 부모 re-render 시 포커스 유지(`onCloseRef` 분리)·열릴 때 본문 첫 필드 포커스(닫기 버튼 대신) — `BranchesPage` 지점 등록 UX. ⑤ **`PlatformPage`·`BillingDetailPage`** raw `<table>` → `Table`(`caption` SR). 회귀 +5(`Modal.test.jsx` 2·`NotificationHistoryPanel.test.jsx` 2·`GuardianPortalPage` 1). `npm test`·build·audit 검증 예정.)
> **이전 갱신**: 2026-06-09 (60차 — **BNK-19 `pendingReviewCount` P1 위젯 + `RegionSelector` + 식사관리 폼 완성 + 접근성 재점검** — USER_STORIES·FLOWCHART BNK-19/US-M02/US-N01/US-D01 잔여 갭 해소. ① **`DashboardPage` 6번째 위젯 `nhisPendingReviewCount`**(BNK-19·US-M02 P1) — `sumNhisPendingReviewFromBatches`(배치 집계)·`DashboardWidgetGrid` 6축·tone=warning(`>0` 시)·`/billing/imports/nhis` 링크. `ReconciliationPage` StatCard와 동일 집계 기반으로 지점 대시보드·HQ 대시보드 동시 반영. ② **`RegionSelector`**(신규 `components/branches/`) — 시·도→시·군·구→읍·면·동 3단 연계 `Select`, DS `Field`+`Spinner` 패턴 재사용, 각 단계 `disabled` 직결(시·군·구 선택 전 읍·면·동 차단·`Field label required`), 로드 오류 `role="alert"`, `RegionSelector.test.jsx` 2건(초기 시·도 목록·하위 disabled 상태). ③ **`MealsPage` 식단 등록 폼 완성**(US-N01) — `canManageMenus`(`hq_admin`·`branch_admin`) 조건부 `MealMenuForm` 렌더, `handleMenuSubmit`→`createMealMenuApi`, 빈 식단 안내 문구 역할별 분기. ④ **`services.js` API 확장** — `fetchBranchesApi`·`createBranchApi`·`updateBranchApi`(US-C01)·`fetchRegionSidosApi`·`fetchRegionSigungusApi`·`fetchRegionDongsApi`(RegionSelector)·`createMealMenuApi`(US-N01)·`createProgramScheduleApi`(US-N02). ⑤ **`ClientListPage` 표 전환**(US-D02) — `ds-list` → `Table`(`caption` SR 이름)·나이·성별·지역·등급·인정번호·보호자·연락처 8열·검색 범위 확대(지역·보호자명·성별). `utils/clientDisplay.js` (`genderLabel`·`formatAge`) 추가. 회귀 +2(`RegionSelector.test.jsx` 2). `npm test`·build·audit 검증 완료.)
> **이전 갱신**: 2026-06-09 (59차 — **Epic K·L·J02 보호자·수납 UI 보강 + 접근성 재점검** — USER_STORIES·FLOWCHART §9-1 대비 잔여 갭 해소. ① **`GuardianClientLinks`**(US-K02) — 보호자 상세 연결 이용자 표·`Switch` 대표 보호자 지정(`.ds-switch--compact`·라벨 sr-only)·`PATCH /guardians/{id}/clients/{clientId}/primary` 연동 골격. ② **`OverdueSummaryBar`**(US-L02) — 미납 건수·총액 `StatCard` 요약(`role=group`)·`OverduePage` 경과일·`MaskedPhone` 보호자 연락처 열·v2 알림톡 제외 `role=note` 안내. ③ **`PaymentPage`/`OverduePage`/`GuardiansPage`** — raw `<table>` → `Table`·lede 스토리 ID 정합(US-L01/L02/K01)·`MaskedPhone` 연락처 마스킹. ④ **`GuardianPortalPage`** — US-I02+US-J02 **`Tabs`** 통합(일일 기록 / 명세·청구, FLOWCHART §9-1). ⑤ **`PaymentRecordModal`** 입금일 → **`DateInput`**. ⑥ **`.ds-switch--compact`** CSS. 회귀 +5. `npm test` **271/83 PASS**·build **795 modules 3청크**(max **367 kB**)·audit **0**.)
> **이전 갱신**: 2026-06-09 (58차 — **US-G06 PENDING_REVIEW 대기(보류) UI + 오류 원인 가이드 + 접근성 재점검** — USER_STORIES US-G06 인수 조건 「`PENDING_REVIEW` + 오류 원인 가이드」(케어포 4단계 패리티, BE @ `4cc328d`) frontend 잔여 해소. ① **`MATCH_STATUS.PENDING_REVIEW`** — `StatusBadge` tone=info·라벨 「대기」·행 강조 `.ds-row--info`(색+텍스트 병행). ② **`NhisReconciliationTable`** — `PENDING`/`PENDING_REVIEW` 정규화·보류 행 존재 시 **「보류 사유」열**에 API `matchStatusReason` 텍스트 노출(색만 의존 금지). ③ **`NhisPendingReviewGuide`** — 대기 행 1건 이상 시 `aside`(complementary)·3단계 재import 안내·`role=status` 푸터(수동 연결은 미매칭만). ④ **`ReconciliationPage`** — 매칭 상태 `StatCard` 4종 요약(일치·차이·미매칭·대기)·가이드 패널 연동. 회귀 +4. `npm test`·build·audit 검증 예정.)
> **이전 갱신**: 2026-06-09 (57차 — **Epic V 방문요양 일정 `/visits` 화면 신설(US-V01~V03) + 접근성 재점검** — USER_STORIES Epic V·FLOWCHART §9b 대비 **frontend `/visits` 누락 화면**을 보강(backend `/api/v1/visits` @ `d768820`·API_SPEC §14는 구현됐으나 UI 부재). ① **`VisitCalendar`**(신규 UI 컴포넌트) — 외부 캘린더 라이브러리 없이 `<table>`+`<caption>`(월 라벨)·요일 `scope="col"` 헤더로 구성한 접근성 월간 달력. 각 날짜는 `<button>`(키보드 Tab·Enter/Space)으로 선택 시 `aria-pressed`, 오늘은 `aria-current="date"`. **방문 건수는 색이 아닌 텍스트 배지 + 버튼 `aria-label`(「YYYY-MM-DD 오늘 방문 N건/일정 없음」)로 풀어 읽어** 색·시각 단서 의존을 배제(§1-2). 이전/다음 달 `aria-label`. ② **`VisitScheduleForm`**(`components/visits/`) — 이용자·방문 날짜·서비스 시간(1~480분) 필수 누락 시 **필드 단위 `Field error`(`aria-invalid`+`role="alert"`)**(WCAG 3.3.1·3.3.2), 제출 `aria-busy`. **계획(PLAN) 일정에서만** 「청구 일정 동시 생성」 토글 노출(이지케어 이중 일정·`createPairedBillingSchedule`, BNK-10·14). ③ **`VisitsPage`** `/visits` — `BranchScopeNotice`·HOME_CARE 안내 `Alert`·**계획/청구 `Tabs` 분리(US-V02)**·`VisitCalendar`(월 이동) + 선택일 목록 `Table`(`StatusBadge` `VISIT_STATUS`·페어 표시)·일정 확정/취소·**모바일 체크인/아웃(US-V03)** 액션(행별 `aria-label`에 이용자명 포함). 역할별 노출 — 등록·확정·취소 `branch_admin`·`social_worker`, 체크인/아웃 `social_worker`·`caregiver`. ④ **`config/visits.js`** — `VISIT_STATUS`·`SCHEDULE_KINDS`·달력 헬퍼(`buildMonthMatrix`·`monthRange`·`countVisitsByDate` 등) 단일 원천. ⑤ App 라우트·`navConfig`(기록 그룹)·`roleNav`(인가·flat nav) 연동. ⑥ `.ds-calendar*`·`.ds-visits-layout` CSS + `forced-colors` 대비 보존. API: `GET/POST/PATCH /api/v1/visits`·confirm/cancel/check-in/check-out(API_SPEC §14, 백엔드 구현 완료). 회귀 +19(`config/visits` 8·`VisitCalendar` 5·`VisitScheduleForm` 3·`VisitsPage` 3). `npm test` **259/80 PASS**·build **792 modules 3청크**(max **367 kB**)·audit **0**.)
> **이전 갱신**: 2026-06-09 (56차 — **US-M03 본인부담 대장 리포트·간편계산기 신설 + 접근성 재점검** — USER_STORIES US-M03(G22) 인수 조건 「청구·입금·수납 대장 + 간편계산기」가 미구현이던 갭 해소. ① **`BillingLedgerTable`** — variant `charges|deposits|receipts` 3종 대장 표(`caption`·`scope=col`·청구대장 본인부담 열 강조·상세 링크 `aria-label`). ② **`BillingReportPage`** — `/billing/reports/charges|deposits|receipts` 공통 페이지(월·검색 필터·`StatCard` 요약·인쇄·`Pagination`). ③ **`CopayCalculatorPanel`** + `utils/copayCalculator.js` — 등급·출석일수·본인부담 구분으로 즉시 계산(US-M03 7-10), 필드 단위 `Field error`·결과 `role=status`·본인부담금 행 색+sr-only 라벨 병행. ④ **`CopayCalculatorPage`** `/billing/calculator`. ⑤ **SideNav 청구 그룹** 4항목 추가. API: `GET /api/v1/billing/reports/{variant}` — coder 백엔드 구현 잔여. 회귀 +8. `npm test`·build·audit 검증 예정.)
> **이전 갱신**: 2026-06-09 (55차 — **US-J02 본인부담금 명세 상세·인쇄 UI 신설 + 접근성 재점검** — USER_STORIES US-J02 인수 조건 「월별 본인부담금 명세 목록·**상세(PDF/인쇄)**」 중 **상세/인쇄**가 미구현이던 갭 해소. `GuardianPortalPage`는 명세 **목록**만 `PaymentRecordModal` 읽기 전용(다용도 컴포넌트)으로 노출했고, §6 체크리스트(8차)에 문서화됐던 `GuardianBillingDetailModal`(US-J02)이 재이관 과정에서 소실됨. ① **`GuardianBillingDetailModal`** 신설 — `Modal`(role=dialog·focus trap)로 한 건 명세서 상세(청구월·이용자·이용일수·총 급여비용·공단부담금·본인부담률 + **본인부담금 강조 행**)를 `<table caption(sr-only)·scope=row>`로 노출. 본인부담금 행은 색 + 굵게 + `ds-sr-only` 「청구 본인부담금」 라벨 병행(색만 의존 금지). 보조 항목은 값이 있을 때만 행 렌더. 「열람 전용 — CMS·간편결제·알림 미지원」 안내(v1.1 범위). ② **인쇄(`window.print()`)** — 다른 인쇄 화면(QR·청구 상세)과 충돌하지 않도록 모달 열림 동안 `body.ds-statement-printing` 스코프 클래스를 부여하고, `@media print body.ds-statement-printing`에서 명세서만 `visibility: visible`로 노출(모달 헤더/푸터·배경 제거). ③ **`GuardianPortalPage`** — 「명세 보기」 모달 → **인라인 명세 목록 표**(이용자 선택 시 자동 로드, 청구월·본인부담금·상태 `StatusBadge`·행별 「상세」 `Button`(`aria-label`에 청구월 포함))로 전환. 행 「상세」 → `GuardianBillingDetailModal`. 읽기 전용 `PaymentRecordModal` 의존 제거(컴포넌트·테스트는 유지). 회귀 +3(`GuardianBillingDetailModal.test.jsx` 3 — null 렌더·강조 행·인쇄, `GuardianPortalPage.test.jsx` 갱신). `npm test` **217/70 PASS**·build **781 modules 3청크**(max **367 kB**)·audit **0**.)
> **이전 갱신**: 2026-06-08 (54차 — **US-UX-04 지점 스코프 안내 전면 연동 + 접근성 재점검** — PLAN_NOTES 72차·USER_STORIES US-UX-04 인수 조건 중 `QrGeneratePage`·배차 3화면 연동 잔여 해소. ① **`BranchScopeNotice`** — `QrGeneratePage`(US-E03)·`TransportPage`·`TransportRunNewPage`·`TransportRunDetailPage`(US-T01~T03)에 `role=status` 조회 범위 노출 — 출석·QR·배차 **6개 스코프 화면** 일관. ② **QR 전용 hint** — 「선택한 지점 기준 QR이 생성됩니다.」 ③ **`forced-colors`** — `.ds-branch-scope-notice` 경계선 추가. ④ **E2E** — `pilotPageFlows` US-UX-04 4경로(출석·통계·QR·배차) 회귀. 회귀 +3. `npm test` **214/69 PASS**·build **780 modules 3청크**(max **367 kB**)·audit **0**.)
> **이전 갱신**: 2026-06-08 (53차 — **US-E01/E05/E03/T03 접근성·지점 스코프 보강** — USER_STORIES·FLOWCHART 대비 잔여 UI 갭 해소. ① **`BranchScopeNotice`** — `active_branch_id` 조회 범위를 `role=status` 텍스트로 노출(US-B02·US-E02·US-E05) → `AttendancePage`·`AttendanceStatsPage`. ② **표 액션 44px 터치 타깃** — `.ds-table-actions .ds-btn`에 `--touch-target-min` 적용(파일럿 P2 수기 체크인 WCAG 2.5.5). ③ **`QrGeneratePage`** — QR 미리보기 `figure`/`figcaption`·인쇄 `@media print` 강화(US-E03). ④ **배차 모바일** — `.ds-tabs--sticky-mobile`·지도 `min-height: min(50vh,360px)`(US-T03). ⑤ **`AttendanceStatsPage`** raw `<table>` → `Table` 컴포넌트. 회귀 +3. `npm test`·build·audit 검증 예정.)
> **이전 갱신**: 2026-06-08 (52차 — **US-T03 배차 연락처 마스킹 UI + ClientTransportProfileSection 접근성** — USER_STORIES US-T03 인수 조건 「정차 명단·연락처 마스킹」·REQUIREMENTS §3-13 SEC-D9 후속 UI 갭 해소. ① **`TransportPickupContact`** — `hq_admin`은 전체 번호+`tel:` 링크, non-HQ는 API 마스킹값만(`MaskedPhone`·링크 없음). ② **`TransportPage`** 명단 표에 「픽업 연락처」열 추가. ③ **`TransportStopList`** 정차 카드에 연락처 행 추가(`showFullContact` prop). ④ **`ClientTransportProfileSection`** — `usesTransport` 펼침 시 `role=group`+sr-only 「픽업 상세 정보」(`aria-labelledby`). ⑤ **`.ds-transport-stop__contact`** CSS. 회귀 +5. `npm test`·build·audit 검증 예정.)
> **이전 갱신**: 2026-06-08 (51차 — **FE-13·FE-14 누락 UI 컴포넌트 복원 + 접근성 재점검** — DESIGN_SYSTEM 문서화만 있고 codebase에서 소실됐던 청구·설정·보호자·플랫폼 UI 11종 재구현. ① **`BillingStatusConfirmModal`**(US-G07 — `window.confirm` 대체·확정 후 불변 경고) → `BillingDetailPage`. ② **`GuardianDailySummary`**(US-I02 — `StatusBadge`+건강 알림) → `GuardianPortalPage`. ③ **`FeeScheduleTable`**+**`FeeRateHistoryPanel`**(US-G00a) → `FeeSchedulePage`. ④ **`CopayRateTable`**(US-G00b·`COPAY_TYPES`) → `CopayRatePage`. ⑤ **`AuditLogPanel`**·**`BackupSettingsPanel`**·**`LoginHistoryPanel`**·**`PasswordChangeModal`**·**`PasswordResetRequestModal`**(FE-14) → `SettingsPage`/`LoginPage`. ⑥ **`PlatformOrgDetailModal`**(US-A01/A02) → `PlatformPage`. ⑦ **`ATTENDANCE_STATUS`** `NOT_YET`·`PENDING` 추가. 회귀 +9. `npm test`·build·audit 검증 예정.)
> **이전 갱신**: 2026-06-08 (50차 — **배차·이동경로 forced-colors 접근성 + US-H02 BranchCompareChart 완료 확인** — `components.css` 배차 forced-colors·`BranchCompareChart` HQ 연동 확인. `npm test` **189/60 PASS**·build PASS·audit 0.)
> **이전 갱신**: 2026-06-08 (49차 — **HQ 통합 대시보드 「전 지점 건강 이상 통합 목록 — 지점명 표시」 보강(US-H02·FLOWCHART §8 HQ E3)** — FLOWCHART §8 HQ 노드 E3·USER_STORIES US-H02 인수 조건 「전 지점 건강 이상 통합 목록」이 **지점명 없이** 렌더되던 갭 해소. ① **`HealthAlertList`** — `item.branchName` 제공 시 이용자명 옆에 중립 `Badge`로 지점명 노출(`ds-health-alert-list__branch`, 우측 정렬). 스크린리더가 지점명 맥락을 식별하도록 `ds-sr-only` 「지점 」 접두 라벨 동반(색만 의존 금지·텍스트 병행 원칙). 지점 스코프 대시보드는 `branchName` 부재 → 미노출(하위 호환). ② **`DashboardPage` HQ variant** — 건강 이상 카드 제목·`HealthAlertList` `ariaLabel`·`emptyMessage`를 「전 지점 건강 이상 알림」으로 분기해 지점 대시보드와 구분되는 접근성 이름 제공. 회귀 +2(`HealthAlertList.test.jsx` — 지점명/ sr-only 라벨 노출·지점 스코프 미노출). `npm test` **185/60 PASS**·build **766 modules** PASS·audit 0.)
> **이전 갱신**: 2026-06-08 (48차 — **Recharts 차트 레이어 복원 + US-H01/E05/F04/H02·US-T03 접근성** — DESIGN_SYSTEM 문서화만 있고 codebase에서 소실됐던 차트 컴포넌트를 재구현. ① **`ChartContainer`**(`role=figure`·`figcaption`·sr-only 요약·빈 데이터 `role=status`)·**`AttendanceRateChart`**(line/bar)·**`HealthTrendChart`**(다중 라인)·**`BranchCompareChart`**(HQ 지점 비교) + `recharts@^2.15.4`·`useChartColors` MutationObserver 다크 전환. ② **페이지 연동** — `DashboardPage` 지점 월별 출석률(US-H01)·HQ `BranchCompareChart`(US-H02)·`AttendanceStatsPage` 일별 막대(US-E05)·`HealthDetailPage` 추이 차트+표(US-F04). ③ **US-T03 직원 읽기 전용** — `TransportRunDetailPage` 비-hq 확정 루트 안내 분리·`TransportStopList` geocode 경고 emoji→`Badge`「지도 제외」·정차 버튼 44px·`aria-label`. ④ **`.ds-chart*`** CSS 승격. 회귀 +4(`ChartContainer`·`AttendanceRateChart`·`TransportRunDetailPage` staff). `npm test` **183/60 PASS**·build PASS·audit 0.)
> **이전 갱신**: 2026-06-08 (47차 — **v3 StaffPage 접근성 보강 + US-T02 배차 확정 취소 UI** — USER_STORIES·FLOWCHART 대비 잔여 갭 해소. ① **`StaffRoleSelect`** + `config/staff.js`(`STAFF_ASSIGNABLE_ROLES`·`staffRoleLabel`) — 직원 등록 역할 raw `TextInput` → `Select` 한국어 라벨(요양보호사·사회복지사·지점장·통합 관리자). ② **`StaffPage` 폼 검증(WCAG 3.3.1·3.3.2)** — 이름·이메일 미입력 시 `Field error`(`aria-invalid`+`role=alert`)·입력 시 오류 자동 해제·제출 `aria-busy`·API 오류는 폼 상단 `Alert` 분리. 목록 역할 열 한국어 라벨. ③ **`TransportUnconfirmModal`** + `unconfirmTransportRunApi` — `hq_admin` 전용 CONFIRMED→DRAFT 확인 다이얼로그(운행일·정차 수·직원 화면 숨김 경고·`Button danger`). ④ **`TransportRunDetailPage`** — 확정 루트에 「확정 취소」버튼·모달 연동·`role=group` 배차 요약·Alert `.ds-page-alert` 통일. ⑤ **`.ds-action-bar--end`** CSS 승격(`StaffPage` 우측 정렬). 회귀 +7(`StaffRoleSelect`·`TransportUnconfirmModal`·`StaffPage`·`TransportRunDetailPage`). `npm test` **179/58 PASS**·build **354.29 kB**·audit 0.)
> **이전 갱신**: 2026-06-08 (46차 — **누락 CSS 유틸·Must 화면 인라인 style 제거 + US-E01 체크인 라우트 접근성** — USER_STORIES·FLOWCHART 대비 잔여 갭 해소. ① **미정의 클래스 승격** — `MealsPage`·`ProgramsPage`·`TransportPage` 등에서 사용 중이었으나 `components.css`에 없던 `.ds-stack`(세로 섹션 스택·구분선)·`.ds-filter-row`/`.ds-filter-row__actions`(필터 폼 행)·`.ds-section-gap--top`·`.ds-modal-section-title`(모달 내 h3)·`.ds-inline-actions--start`(dl 값 내 인라인 액션) 신설. ② **인라인 style 0건** — `PaymentPage`·`FeeSchedulePage`·`CopayRatePage`·`PlatformPage`·`GuardianDetailPage` 잔여 `style={{}}` 제거(FE-16 패턴). ③ **`/attendance/checkin` 라우트 차별화(US-E01)** — `AttendancePage`가 `/attendance`와 동일 UI였던 갭을 `useLocation`으로 해소: 체크인 경로에서 AppShell `h1`「수기 체크인」·카드 제목·lede 문구 분기, 요약 `StatCard`에 `role="group"`+`aria-label`. ④ **v3 페이지 Alert 정합** — `MealsPage`·`ProgramsPage` 오류/성공 `Alert`에 `.ds-page-alert` 적용(토큰 여백·live region 일관). ⑤ **`GuardianDetailPage` 재발송 버튼** — 보호자명 포함 `aria-label`. ⑥ **모듈 커버리지** — `competitorModuleCoverage` 프로그램 급여 `0→1`(US-N02). 회귀 +1(`AttendancePage.test.jsx` checkin 경로). `npm test` **165/54 PASS**·build **347.90 kB**·audit 0.)
> **이전 갱신**: 2026-06-08 (45차 — **v3 식사·프로그램 기록 폼(US-N01·N02) 접근성 재점검** — 61차 v3 UI shell(`MealsPage`·`ProgramsPage`·`MealRecordForm`·`ProgramParticipationForm` @ `7ef1083`)이 UXD 폼 검증 접근성 패스를 거치지 않아, 필수 입력 검증이 앱 표준 패턴(`IncidentRecordForm`)과 달리 **폼 상단 단일 `Alert`**로만 노출되던 갭을 해소(WCAG 3.3.1·3.3.2·4.1.2). ① **필드 단위 오류** — `MealRecordForm` 「이용자」·`ProgramParticipationForm` 「이용자」·「프로그램」 미선택 시 `Field error`(해당 컨트롤에 **`aria-invalid=true`** + `role="alert"` 오류 메시지 `aria-describedby` 연결)로 전환해, 스크린리더가 **어느 필드가 비었는지** 식별 가능. 폼 상단 `Alert`는 제출·API 실패 메시지 전용으로 분리. ② **필수 표시(`required`)** — 두 폼의 필수 `Select`에 시각적 `*` 표기(label) 추가 — 입력 전 필수 항목을 사전 식별. ③ **오류 자동 해제** — 사용자가 해당 필드를 선택하면 `aria-invalid`·오류 메시지를 즉시 제거(입력 중 SR 잔존 경고 방지). ④ **`aria-busy`** — 제출 `Button`에 `aria-busy={submitting}`로 저장 진행 상태를 SR에 전달(`IncidentRecordForm` 패턴 정합). 회귀 +3(`MealRecordForm.test.jsx` +1·신규 `ProgramParticipationForm.test.jsx` 2 — 필드 `aria-invalid`·오류 자동 해제). `npm test` **160/54 PASS**·build **347.60 kB**·audit 0.)
> **이전 갱신**: 2026-06-08 (44차 — **v1.3 배차·이동경로 UI(US-T01~T03) 접근성 재점검** — 60차 transport UI shell(`TransportPage`·`TransportRunNewPage`·`TransportRunDetailPage`)이 UXD 접근성 패스를 거치지 않아 남은 결함을 해소. ① **헤딩 계층(WCAG 1.3.1·2.4.6)** — `Card`(`ds-card__title`=`h2`) 내부 섹션 제목들이 `h2`로 마크업돼 카드 제목과 **동일 레벨로 중복**되던 것을 `h3`로 정정(`TransportPage` 「당일 배차 명단」·「운행 루트」, `TransportRunNewPage` 「배차 명단」·「정차 순서·지도」 → AppShell `h1` → Card `h2` → 섹션 `h3`). ② **표 접근성 이름** — `TransportPage` 명단·루트 표가 앱 내 유일하게 `<caption>` 없이 노출되던 갭을 해소. `Table`에 **`captionVisuallyHidden`** prop 추가(`<caption class="ds-sr-only">`) — 시각적 `h3` 제목과 중복 없이 스크린리더 표 탐색용 이름(「당일 배차 명단」·「운행 루트」)만 제공(`AttendancePage`·`HealthDetailPage` caption 패턴과 정합). ③ **상태 메시지(WCAG 4.1.3)** — `TransportRunNewPage` 「선택 N/15명」 카운터가 명단 선택 시 무음으로 갱신되던 것을 `role="status"`(aria-live polite)로 감싸 인원·상한 변화를 SR이 안내. 회귀 +2(`TransportPage.test.jsx` 헤딩 레벨·표 caption). `npm test` **152/50 PASS**·build **133 modules**·audit 0.)
> **이전 갱신**: 2026-06-08 (43차 — **US-G06 UNMATCHED 후보 이용자 검색 UI 보강 + 접근성 재점검** — USER_STORIES US-G06 인수 조건 「`UNMATCHED` 행은 **후보 이용자 검색**·수동 연결 UI」 중 검색이 미구현이던 갭 해소. 기존 `ReconciliationPage` 수동 매칭 폼은 후보를 항상 `q: ""` 고정으로 최대 20명만 `Select`에 노출해, 동명이인·다인원 지점에서 대상 이용자를 찾기 어려웠다. ① 미매칭 행 선택 시 **`SearchInput`**(시각 라벨 「후보 이용자 검색」·`type=search`) 노출 — 입력을 250ms 디바운스해 `fetchNhisMatchCandidatesApi(batchId, { q })`로 후보를 재조회(이름·인정번호 검색). ② 검색·행 변경 시에만 재조회하되, **현재 선택 이용자가 결과에 남아 있으면 선택 유지**(아니면 첫 후보로 리셋) — 입력 중 선택이 튀지 않음. ③ 결과 0건 시 「검색 조건에 맞는 후보 이용자가 없습니다」 `role="status"`(polite) 안내. ④ 「수동 연결」`Button`은 행·이용자 미선택 시 `disabled`(색만 의존 금지 — 비활성 상태). 행 미선택 시 `SearchInput`·후보 `Select` 모두 `disabled`. 회귀 +1(`ReconciliationPage.test.jsx` — 행 선택→후보 검색 q 전달). `npm test` **144/47 PASS**·build **125 modules**·audit 0.)
> **이전 갱신**: 2026-06-08 (42차 — **US-G06 DISCREPANCY 청구 라인 비교 링크 신설 + 접근성 재점검** — USER_STORIES US-G06 인수 조건 「`DISCREPANCY` 행은 강조 표시 + 차이 컬럼·**청구 라인 비교 링크**」 중 비교 링크가 미구현이던 갭을 해소(재이관 과정에서 8차 `DiscrepancyComparePanel`이 소실됨). ① **`DiscrepancyComparePanel`** 신설 — `Modal`(role=dialog·focus trap)로 **공단(NHIS) vs ogada 청구** 청구액·이용일수를 비교 표(`caption`·`scope=col`·항목 `scope=row`)로 노출. 차이는 `--color-warning-text` 색 + **「공단 초과/부족」텍스트 Badge 병행**(색만 의존 금지)·차이 0이면 「동일」텍스트. `claimHref` 있으면 ogada 청구 라인 상세 비교 링크 제공. ② **`NhisReconciliationTable` `onCompare` prop** — 제공 시 `DISCREPANCY` 행에만 「비교」`Button`(행별 `aria-label`에 **이용자명 포함** — 다중 행 SR 식별), 그 외 행은 `—`. `onCompare` 미제공 시 액션 열 미노출(하위 호환). ③ `ReconciliationPage` 연동(비교 모달 상태·`claimHref`). 회귀 +5(`DiscrepancyComparePanel.test.jsx` 3·`NhisReconciliationTable.test.jsx` 비교 버튼/미노출 2). `npm test` **142/46 PASS**·build **125 modules**·audit 0.)
> **이전 갱신**: 2026-06-08 (41차 — **US-F03 낙상·사고·특이사항 이벤트 기록 UI 신설 + 접근성 재점검** — USER_STORIES·FLOWCHART §6 대비 **누락 화면 보강**: 기존 `HealthPage`가 일일 건강·투약·이력 3탭뿐이라 **파일럿 Must 스토리 US-F03(낙상·특이사항)이 동작하지 않던 갭**을 해소. ① **`IncidentRecordForm`** 신설 — 이벤트 유형 `Select`(낙상/사고/특이사항/기타, **필수 — 빈 값 시 `Field error`(role=alert)·`aria-invalid` 차단**)·발생 시각 `TextInput type=time`(선택, 미입력 시 기록 시각)·내용 `Textarea`(**필수 차단**). `INCIDENT_TYPES` 상수 export. ② **`HealthPage` 「낙상·특이사항」탭 추가**(4탭) + 기록 이력 탭에 이벤트 항목 `[유형] 내용` 노출(유형 텍스트 라벨 병행). ③ **API 페이로드 정합** — `buildIncidentApiPayload`(`utils/healthApiPayload.js`, `recordedAt`·`occurredAt` KST ISO·`incidentType`·`description`)·`createIncidentApi`(`POST /clients/:id/health/incidents`)·`normalizeHealthResponse` `incident` recordType 파싱. 회귀 +4(`IncidentRecordForm.test.jsx` 3·`healthRecords.test.js` incident 파싱 1). `npm test` **134/45 PASS**·build **124 modules**·audit 0.)
> **이전 갱신**: 2026-06-07 (40차 — **US-F01 활력징후 비정상 범위 입력 경고 + 접근성 재점검** — ① 활력징후 정상 범위를 `utils/vitalsRanges.js`로 **단일 진실 원천화**(`VITALS_RANGES`·`evaluateVital`·`findFormVitalsAbnormalities`·`findAbnormalVitalRecords`) — `HealthPage.detectAbnormal` 매직 넘버 중복 제거. ② **`Field` `warning` prop 추가**(`role="status"` polite·`aria-describedby` 연결·`aria-invalid` 미설정 — 값은 여전히 저장 가능). ③ **`VitalsRecordForm`** 수축기 혈압·체온·혈당·SpO₂ 입력 시 정상 범위 이탈을 **인라인 경고(텍스트+색 병행)**로 표시(US-F01 「비정상 범위 시 표시」 충족). ④ **§8-1 라우트 표** — `/guardian/checkin`(US-E04)이 `guardian`/`client_user` 인가로 노출됨을 실측 반영(UXD-6 코드 해소 확인). 회귀 +9(`vitalsRanges.test.js` 5·`VitalsRecordForm.test.jsx` 4). `npm test` **124/42 PASS**·build **121 modules**·audit 0.)
> **이전 갱신**: 2026-06-07 (39차 — **USER_STORIES·FLOWCHART Must 흐름 보강 + 접근성 재점검** — ① **`/guardian/checkin` 라우트**(US-E04·FLOWCHART §5-2) + SideNav·`GuardianPortalPage` 링크 — 보호자 QR 셀프 체크인 canonical 경로. ② **`VitalsRecordForm`**(US-F01·파일럿 P3)·**`MedicationRecordForm`**+**`MedicationDuplicateAlert`**(US-F02 중복 경고) — `HealthPage` Tabs(건강/투약/이력). ③ **`NhisReconciliationTable`**(US-G06 MATCHED/DISCREPANCY/UNMATCHED 행 강조·StatusBadge) — `ReconciliationPage` 목록→표. ④ **`HealthDetailPage`** raw radio→`FilterChips`·`Table`(US-F04). ⑤ **`QrGeneratePage`** 인라인 style→`.ds-qr-preview*`. 회귀 +5(`MedicationDuplicateAlert`·`MedicationRecordForm`·`NhisReconciliationTable`·`HealthDetailPage`). `npm test` **115/40 PASS**·build **120 modules**·audit 0.)
> **이전 갱신**: 2026-06-07 (38차 — **수기 출석 체크인/아웃·결석 흐름 보강(US-E01·E02, 파일럿 P2)** — 재이관 baseline의 `AttendancePage`가 **읽기 전용 목록**뿐이라 파일럿 핵심 시나리오 P2(아침 수기 체크인)가 동작하지 않던 갭을 해소. ① **`CheckoutModal`**(귀가 교통편 `Select`·미선택 시 확인 `disabled`·`error` Alert) 신설. ② **`AttendanceAbsentModal`**(결석 사유 필수 — 빈 값 시 `Field error`(role=alert)·제출 차단) 신설. ③ `AttendancePage` — 당일 출석 요약 `StatCard` 4종(입소·귀가 완료·결석·미처리, US-E02) + 이용자별 `Table`에 **입소/귀가/결석** 액션(버튼 `aria-label`에 **이용자명** 포함 — 다중 행 SR 식별)·상태별 노출(미처리→입소·결석, 입소→귀가, 완료→안내). 기존 `checkInApi`·`checkOutApi`(미사용 상태)를 연결하고 `markAbsentApi`(`POST /attendance/absent`) 추가. ④ 회귀 — `CheckoutModal.test.jsx`(3)·`AttendanceAbsentModal.test.jsx`(2)·`AttendancePage.test.jsx`(3, 요약·체크인·교통편 귀가). `npm test` **105/33 PASS**·build **116 modules**·audit 0.)
> **이전 갱신**: 2026-06-07 (37차 — **`GuardianCheckinPage`(US-E04) 체크인 유형 접근성·DS 정합** — 인라인 `style`이 박힌 raw `<fieldset>`+`<input type=radio>`(입소/귀가)를 DS `FilterChips`(`role="radiogroup"`·44px·색상+텍스트·`forced-colors`)로 교체. 인라인 style 0건. `GuardianCheckinPage.test.jsx`(2건 — 기본 선택·전환·제출 라벨) 회귀 추가. **§8-1 라우트 표 실측 정합**: `/billing/claims/:claimId`·`/billing/imports/nhis(/:batchId)`·`/attendance/checkin/qr`·`GuardianPortalPage` 등 App.jsx 실제 경로로 갱신. **잔여(coder/planner)**: `/attendance/checkin/qr`가 staff 역할로 가드되어 guardian/client_user가 자기 QR 체크인 화면 접근 불가 — PLAN_NOTES `### [UXD]` UXD-6 기록. `npm test` 91/29 PASS.)
> **이전 갱신**: 2026-06-07 (36차 — **15개 누락 화면 전체 구현 완료** — ModulePage 스텁 → 실 구현 페이지 교체: `ClientFormPage`(US-D01)·`QrGeneratePage`(US-E03)·`GuardianCheckinPage`(US-E04)·`AttendanceStatsPage`(US-E05)·`HealthDetailPage`(US-F04)·`BillingDetailPage`(US-G02/G07)·`PaymentPage`(US-G04/G05)·`OverduePage`(US-G06)·`FeeSchedulePage`(US-G01)·`CopayRatePage`(US-G01)·`GuardiansPage`(US-H01-H04)·`GuardianDetailPage`(US-K02)·`BranchesPage`(US-B01-B04)·`PlatformPage`(US-A01/A02)·`SettingsPage`(US-I03). `App.jsx` 전체 라우트 신규 경로 추가(`/clients/new`, `/clients/:id/edit`, `/billing/claims/:id`, `/health/:clientId`, `/attendance/checkin/qr`, `/guardians/:id`). `npm run build` 114 modules PASS. `git push origin develop` 완료.)
> **이전 갱신**: 2026-06-07 (34차 — **USER_STORIES·FLOWCHART Must 페이지 연동 + 도메인 UI 보강 + 접근성 재점검** — ① **이용자 상세 탭**(US-D03 `Tabs`/`TabPanel` 기본·건강·출석·청구)·`MaskedRevealField`(US-D04 주민번호)·`GuardianInviteModal`(US-J01). ② **목록/대시보드/청구** — `ClientListPage` `SearchInput`+`Pagination`(US-D02)·`DashboardWidgetGrid`+`StatCard`(US-H01/M02)·`BillingPage` `FilterChips`+`MonthInput`(US-G07). ③ **NHIS/건강/세션** — `NhisImportGuidePanel`+`FileUpload`(US-G04)·`HealthAbnormalBanner`(US-F01)·`SessionTimeoutProvider`+`SessionTimeoutModal`(US-B03). ④ 페이지 오류 `Alert`+`.ds-page-alert` 통일(redundant `role=alert` 제거). 회귀 +11(`Switch`·`MaskedRevealField`·`NhisImportGuidePanel`·`FileUpload`·`ClientDetailPage` 탭/모달), `npm test` 69/22·build PASS)
> **이전 갱신**: 2026-06-07 (33차 — **USER_STORIES·FLOWCHART 대비 기반 UI·레이아웃 보강 + 접근성 재점검** — ① **2단 `SideNav`**(US-UX-02, `layout/navConfig.js`+`SideNav.jsx`) 운영·출석·기록·청구 4그룹·모바일 `aria-expanded` 토글. ② **Must 목록/상세 기반 컴포넌트** `StatCard`·`SearchInput`·`FilterChips`·`Pagination`·`Table`·`Tabs`/`TabPanel`·`BranchSwitcher`(US-B02)·`LogoutButton`(US-B03) 신설 + barrel export. ③ **`AppShell` 통합** — flat NavLink → `SideNav`+`LogoutButton`+`BranchSwitcher` topbar. ④ **`LoginPage` → `PublicAuthLayout`**(US-B01) 공개 인증 h1·skip 일관. ⑤ **누락 CSS** `.ds-list*`·`.ds-breadcrumb`·`.ds-form-grid`·`.ds-tabs*`·`.ds-pagination`·`.ds-sidenav__*`·`.ds-branch-switcher` 승격. 회귀 `FilterChips`·`Tabs`·`BranchSwitcher`·`LogoutButton`·`SideNav` test +12, `npm test` 58/18·build 86 modules PASS)
> **이전 갱신**: 2026-06-07 (32차 — **실측 baseline `7170b2a` 접근성 재점검** — ① **`Alert` 라이브 리전 정중도(politeness)를 tone 기준으로 분기**: `danger`/`warning`→`role="alert"`(assertive), `info`/`success`/`neutral`→`role="status"`(polite). 정적 안내(info)가 assertive로 스크린리더를 끊던 갭 해소, `role` 명시 override는 유지. ② **`PublicAuthLayout` 컴포넌트 신설**(§7-7n 문서화만 있고 재이관 baseline엔 부재) — skip link + 브랜드 + **페이지 `h1`** 제공. ③ **`GuardianInvitationAcceptPage`(US-J01) 헤딩 계층 결함 수정** — 기존엔 `<h1>` 없이 `Card` `<h2>`만 있던 공개 화면을 `PublicAuthLayout`로 전환해 단일 h1·skip link·브랜드 일관성 확보. `Alert.test.jsx`(4)·`PublicAuthLayout.test.jsx`(2) 추가, `npm test` 46/13·build 75 modules·audit 0 PASS)
> **이전 갱신**: 2026-06-07 (31차 — **실측 baseline `c3b863e` 접근성 재점검** — `GuardianInvitationList`(US-J01) 행별 재발송/취소 `Button`에 보호자명 포함 `aria-label` 추가(여러 행에서 SR이 동작 대상을 식별 가능)·`aria-busy` 처리, 회귀 테스트 `GuardianInvitationList.test.jsx` +1. `NavLink`는 활성 시 `aria-current="page"` 기본 적용 확인. `npm test` 10/10·build 70 modules PASS)
> **이전 갱신**: 2026-06-07 (30차 — **스켈레톤 재이관 baseline 위에 폼 입력·토글·연락처 마스킹 컴포넌트 보강** — `Switch`(US-I03·§3-3)·`DateInput`(US-D01·§3-1)·`MonthInput`(US-E05·G02/G04/G07)·`MaskedPhone`(US-K01·L02), `DashboardPage` AppShell skip-link/topbar 적용·존재하지 않는 `ds-stack*` 클래스 제거, `ForbiddenPage` `.ds-auth-page` 패턴 적용)
> **이전 갱신**: 2026-06-07 (29차 — **스켈레톤 재이관 후 CSS 토큰·컴포넌트 스타일·핵심 UI 초안** — `tokens.css`·`components.css`·`theme.js`·`chartColors.js`·`components/ui/` Button/Field/TextInput/Card/Alert/Badge/Modal/ThemeToggle 등 + `LoginPage` DS 적용)
> **이전 갱신**: 2026-06-08 (28차 — **`DateInput` 표준화 잔여**(US-D01 `ClientFormPage` 생년월일·인정유효일·US-L01 `PaymentRecordModal` 입금일)·**접근성 재점검**(`ClientPhotoField` 사진 버튼 `aria-label`·`GuardianInviteModal` `aria-busy`·`ClientDetailPage` 초대 Alert `ds-page-alert`))
> **이전 갱신**: 2026-06-08 (27차 — **`DateInput`**(§3-1 감사·로그인 이력 기간 필터)·**`GuardianInvitationList`**(US-J01 초대 이력·`INVITATION_STATUS`·재발송/취소 `aria-label`)·`GuardianListCard` 초대 이력 통합·`AuditLogPanel`/`LoginHistoryPanel`/`ClientPhotoField` raw input→`TextInput`/`DateInput`·만료 토큰 수락 폼 잠금)
> **이전 갱신**: 2026-06-08 (26차 — **US-J01 보호자 초대 수락 UI** `PublicAuthLayout`+`GuardianInvitationAcceptForm`(LoginPage 카드 패턴·AppShell 금지)·**`INVITATION_STATUS` Badge**(PENDING/SENT/ACCEPTED/EXPIRED/REVOKED)·`.ds-auth-page*` CSS·접근성 `autoComplete`·수락 완료 폼 잠금)
> **이전 갱신**: 2026-06-07 (23차 — **`ClientDetailPage`(US-D03/D04/M01) 잔여 인라인 style 전량 제거** → `.ds-inline-actions`·`.ds-client-summary*`·`.ds-dl-grid`·`.ds-section-gap`·`.ds-table-empty` 유틸 승격, `ClientFormPage` 폼 액션 `.ds-form-actions--end`, `PlatformPage` 사업자번호 `.ds-mono`, `GuardiansPage` `.ds-text-muted` — 다크/forced-colors 일관성·접근성 재점검)
> **이전 갱신**: 2026-06-07 (21차 — **`FeeScheduleTable`**(US-G00a)·**`BillingDetailPage` 상태 확인 모달**(US-G07)·**`StatCard tone=danger`**(US-L02)·텍스트 유틸(`.ds-text-*`·`.ds-mono`·`.ds-diff-amount`)·Must 페이지 **`ds-page-alert`** 잔여 통일·접근성 재점검)
> **이전 갱신**: 2026-06-07 (20차 — **`BillingStatusConfirmModal`**(US-G07)·**`NhisImportGuidePanel`**(US-G04)·**`CopayRateTable`**(US-G00b)·**`GuardianDailySummary`**·**`HealthAlertList`**(US-I02/H01)·Must 페이지 **`ds-page-alert`** 잔여 통일·접근성 재점검)
> **이전 갱신**: 2026-06-07 (19차 — **`SettingsPage` 보안 탭** `PasswordChangeModal`+`PasswordResetRequestModal` 통합·`token` useAuth 누락 버그 수정·`.ds-security-panel` CSS 신설·§8-3 미구현 현행화·접근성 재점검 완료)
> **이전 갱신**: 2026-06-07 (18차 — **`LoginHistoryPanel`**(REQUIREMENTS §3-1)·**`PasswordResetRequestModal`**(§3-1)·페이지 오류 **`Alert`+`ds-page-alert` 통일**·`PlatformOrgDetailModal.test.jsx`)
> **이전 갱신**: 2026-06-07 (17차 — **`AuditLogPanel`**·**`BackupSettingsPanel`**(US-I03)·**`PasswordChangeModal`**(US-A02)·**`FilterChips` counts**(US-G07)·페이지 `Alert`/`ds-link` 통일·`Modal` 필수 모드 props)
> **이전 갱신**: 2026-06-07 (15차 — **Recharts 접근성 차트 컴포넌트**(`ChartContainer`·`AttendanceRateChart`·`HealthTrendChart`·`BranchCompareChart`) 신설, 플레이스홀더→실차트 교체(US-F04/H01/E05/H02), `useChartColors` 테마 실시간 반영, `.ds-chart`·`.ds-link` CSS, UXD-1·UXD-4 완료)
> **이전 갱신**: 2026-06-07 (14차 — **`BATCH_STATUS` 공유 상수 승격**(NHISImportPage 로컬 정의 → Badge 모듈), **`FeeRateHistoryPanel`** 신설(US-G00a 수가 이력·연도별 그룹), **Recharts 차트 색상 토큰**(토큰·chartColors.js·다크 팔레트), **`ds-progress-steps`·`ds-fee-history`·`ds-fee-table-cell`** CSS, §2-3 BATCH_STATUS 도메인 매핑 추가, UXD-1·UXD-4 해소)
> **이전 갱신**: 2026-06-06 (13차 — **전사 설정 토글** 누락 보강: WAI-ARIA `switch` 패턴 `Switch` 컴포넌트 신설(`role="switch"`·`aria-checked`·키보드·44px·켜짐/꺼짐 텍스트 병행), `SettingsPage` `allow_client_self_checkin`(REQUIREMENTS §3-3·FLOWCHART §2) 정적 안내 → 실 토글 컨트롤로 교체, `forced-colors` 식별성)
> **이전 갱신**: 2026-06-06 (12차 — **로그인 진입 화면** 스타일 정비(미정의 `.ds-label` 해소·`.ds-login`), **Modal 포커스 트랩**(WAI-ARIA dialog), **고대비/강제 색상 모드**(`forced-colors`·`prefers-contrast`, WCAG 1.4.11) 지원)
> **이전 갱신**: 2026-06-06 (11차 — **다크 모드** 토큰·`ThemeToggle` 추가: agents.yaml design_principles 「다크모드 지원(운영자 야간 근무)」 구현, §2-4 다크 대비표·§10 해소)
> **이전 갱신**: 2026-06-06 (10차 — US-D01/FLOWCHART §4 이용자 본인(client_user) 계정 발급 필드, CopayTypeSelect 실적용, 대비비 실측 현행화)
> **상태**: 초안 (Draft)
> **대상**: planner(PLN) 검토 · coder(COD) 구현 · tester(TSR) 검증
> **근거 문서**: `docs/planning/REQUIREMENTS.md`(§4 비기능 — 접근성 WCAG 2.1 AA, 반응형), `docs/planning/USER_STORIES.md`, `docs/planning/FLOWCHART.md`

---

## 0. 산출물 위치 [UXD]

| 구분 | 경로 | 설명 |
|------|------|------|
| 디자인 토큰 | `src/frontend/src/styles/tokens.css` | 색상·타이포·간격·radius·shadow·터치 타깃 CSS 변수 (단일 진실 원천) |
| 컴포넌트 스타일 | `src/frontend/src/styles/components.css` | `.ds-*` 클래스 (BEM-lite), 토큰만 참조 |
| UI 컴포넌트 | `src/frontend/src/components/ui/` | React(JSX) 컴포넌트 + barrel `index.js` |
| 전역 베이스 | `src/frontend/src/styles.css` | body·링크·로그인 레이아웃 (토큰 기반) |
| 테마 유틸 | `src/frontend/src/theme.js` | 라이트/다크 결정·적용·저장 (`<html data-theme>`, 11차) |
| 페이지 스켈레톤 | `src/frontend/src/pages/` | 화면 구조 + 컴포넌트 조합 예시 (API 연동은 coder 담당) |

> **브랜치**: `src/frontend` submodule의 `develop`.
> **스택 메모**: 현재 `src/frontend`는 **JSX(JavaScript)** 로 구현. TS 전환 시 아래 §7 props 표를 인터페이스로 그대로 옮길 수 있다.

---

## 1. 디자인 원칙 [UXD]

1. **접근성 우선** — WCAG 2.1 AA. 모든 인터랙티브 요소는 키보드로 동작하고 포커스가 보인다.
2. **색상만으로 의미 전달 금지** — 상태(청구/매칭/출석)는 항상 **텍스트 라벨 + 색상**을 함께 제공.
3. **모바일 친화** — 터치 타깃 최소 44×44px, 입력 글자 16px(iOS 자동 줌 방지), 360px 폭 지원.
4. **토큰 단일 원천** — 컴포넌트는 raw hex 금지, 시맨틱 토큰(`--color-*` 등)만 사용.
5. **현장 사용자 배려** — 파일럿은 센터장·요양보호사. 큰 글자·명확한 라벨·낮은 인지 부하.

---

## 2. 색상 토큰 [UXD]

### 2-1. 시맨틱 토큰 (컴포넌트에서 사용)

| 토큰 | 값(primitive) | 용도 |
|------|--------------|------|
| `--color-bg` | gray-100 | 페이지 배경 |
| `--color-surface` | white | 카드·패널 표면 |
| `--color-surface-muted` | gray-50 | 표 헤더·비활성 입력 |
| `--color-text` | gray-900 | 기본 본문 |
| `--color-text-secondary` | gray-600 | 보조 텍스트 (on white 7.46:1) |
| `--color-text-muted` | gray-500 | 플레이스홀더 (on white 4.76:1) |
| `--color-primary` | blue-600 | 기본 액션 (on white 5.17:1) |
| `--color-primary-hover` | blue-700 | hover |
| `--color-focus-ring` | blue-600 | 키보드 포커스 링 |
| `--color-success` / `-text` | green-600 / 700 | 수납완료·일치 |
| `--color-warning` / `-text` | amber-600 / 700 | 차이(DISCREPANCY) |
| `--color-danger` / `-text` | red-600 / 700 | 미매칭·삭제·오류 |
| `--color-border-strong` | gray-400 | 입력 테두리 |

### 2-2. 대비비(WCAG AA) 확인

> **10차 실측 (2026-06-06)**: 아래 값은 `tokens.css`의 실제 hex로 재계산한 값이다(이전 표는 토큰을 darken 하기 전 보수적 추정치였음). 모든 시맨틱 조합이 AA(본문 4.5:1)를 충족하며, 실측값은 기존 표기보다 높다.

| 조합 (실제 토큰 hex) | 대비비(실측) | 기준 | 결과 |
|------|--------|------|------|
| text(gray-900 #0f172a) / white | ~17:1 | 4.5:1 | ✅ |
| text-secondary(gray-600 #475569) / white | 7.58:1 | 4.5:1 | ✅ |
| text-muted(gray-500 #64748b) / white | 4.76:1 | 4.5:1 | ✅ |
| on-primary(white) / primary(blue-600 #1d4ed8) | 6.70:1 | 4.5:1 | ✅ |
| primary-hover(blue-700 #1e40af) / white | 8.72:1 | 4.5:1 | ✅ |
| success(green-600 #15803d) / white | 5.02:1 | 4.5:1 | ✅ |
| warning(amber-600 #b45309) / white | 5.02:1 | 4.5:1 | ✅ |
| danger(red-600 #dc2626) / white | 4.83:1 | 4.5:1 | ✅ |
| info(info-600 #0e7490) / white | 5.36:1 | 4.5:1 | ✅ |
| success-text(green-700) / success-soft(green-50) (badge) | 6.77:1 | 4.5:1 | ✅ |
| warning-text(amber-700) / warning-soft(amber-50) (badge) | 6.84:1 | 4.5:1 | ✅ |
| danger-text(red-700) / danger-soft(red-50) (badge) | 5.91:1 | 4.5:1 | ✅ |
| neutral-text(gray-700) / neutral-soft(gray-100) (badge) | 9.45:1 | 4.5:1 | ✅ |

> 본문 텍스트(<18.66px)는 4.5:1, 큰 텍스트·UI 컴포넌트 경계는 3:1 기준. Badge 소프트 배경 위 `*-text` 토큰은 진한 색으로 대비 확보. 솔리드 뱃지(white on success/warning/danger-600)도 5.0:1 이상.

### 2-3. 상태 색상 매핑 (도메인)

| 도메인 | 코드 | tone | 라벨 |
|--------|------|------|------|
| 청구 상태 (US-G07) | `DRAFT` | neutral | 작성중 |
| | `CONFIRMED` | info | 확정 |
| | `PAID` | success | 수납완료 |
| NHIS 매칭 (US-G06) | `MATCHED` | success | 일치 |
| | `DISCREPANCY` | warning | 차이 |
| | `UNMATCHED` | danger | 미매칭 |
| | `PENDING_REVIEW` | info | 대기(보류) |
| 출석 상태 | `CHECKED_IN` | success | 입소 |
| | `CHECKED_OUT` | neutral | 귀가 |
| | `ABSENT` | warning | 결석 |
| Tenant 상태 | `active` | success | 활성 |
| | `inactive` | neutral | 비활성 |
| NHIS 배치 (US-G04) | `PENDING` | neutral | 대기 |
| | `PROCESSING` | info | 처리중 |
| | `COMPLETED` | success | 완료 |
| | `FAILED` | danger | 실패 |
| 보호자 초대 (US-J01) | `PENDING` | neutral | 대기 |
| | `SENT` | info | 발송됨 |
| | `ACCEPTED` | success | 수락됨 |
| | `EXPIRED` | warning | 만료 |
| | `REVOKED` | danger | 취소됨 |
| 알림 채널 (US-J03) | `KAKAO_ALIMTALK` | info | 알림톡 |
| | `SMS` | neutral | 문자 |
| 알림 상태 (US-J03) | `SENT` | success | 발송완료 |
| | `FAILED` | danger | 실패 |
| | `PENDING` | neutral | 대기 |
| lifecycle 상태 (G34·US-T09·US-T10) | `DRAFT` | neutral | 작성중 |
| | `SCHEDULED` / `IN_PROGRESS` | info | 예정 / 진행중 |
| | `DUE_SOON` | warning | 기한 임박 |
| | `OVERDUE` | danger | 기한 초과 |
| | `COMPLETED` / `SIGNED` / `RENEWED` | success | 완료 / 서명 완료 / 갱신 |
| | `TERMINATED` | danger | 해지 |
| 방문 일정 (US-V01) | `DRAFT` | neutral | 작성중 |
| | `CONFIRMED` | info | 확정 |
| | `IN_PROGRESS`/`CHECKED_IN` | info | 방문중 |
| | `COMPLETED` | success | 완료 |
| | `CANCELLED` | danger | 취소 |
| 외출 상태 (G15 2-1-1) | `PLANNED` | info | 예정 |
| | `OUT` | warning | 외출 중 |
| | `RETURNED` | success | 복귀 |
| | `CANCELLED` | neutral | 취소 |
| 차량 상태 (G16) | `active` (isActive=true) | success | 운행 |
| | `inactive` (isActive=false) | neutral | 비활성 |

> 매핑 객체는 `components/ui/Badge.jsx`의 `BILLING_STATUS`·`MATCH_STATUS`·`ATTENDANCE_STATUS`·`BRANCH_STATUS`·`BATCH_STATUS`·**`INVITATION_STATUS`**·**`LIFECYCLE_STATUS`**로 코드화 → `<StatusBadge status map>` 사용. `BATCH_STATUS`는 14차에 NHISImportPage 로컬 정의 → Badge 모듈로 승격. **`VISIT_STATUS`**(방문 일정, US-V01)는 도메인 상수와 함께 `config/visits.js`에 정의해 `<StatusBadge map={VISIT_STATUS}>`로 사용(57차). **`OUTING_STATUS`**·**`VEHICLE_STATUS`**(77차)는 `config/outingStatus.js`에 정의.

### 2-4. 다크 모드 토큰 (11차, 운영자 야간 근무) [UXD]

> agents.yaml `design_principles` 「다크모드 지원(운영자 야간 근무 고려)」 구현. 컴포넌트는 시맨틱 토큰만 참조하므로 **토큰 재정의만으로** 전 화면이 전환된다(컴포넌트 코드 변경 0). 활성화는 `<html data-theme="dark">` — `src/theme.js`/`ThemeToggle`가 설정.

**설계 원칙**: 다크에서는 `primary`/`danger`를 **더 밝은 색**으로 올리고 라벨 텍스트(`--color-on-primary`/`--color-on-danger`)를 **진한 남색(#0f172a)**으로 두어 버튼 대비를 확보한다. 상태 뱃지·알림은 반투명 틴트(`*-soft`) 위 **밝은 `*-text`** 조합.

| 다크 조합 | 대비비(계산) | 기준 | 결과 |
|------|--------|------|------|
| text(#f1f5f9) / surface(#1e293b) | ~12.8:1 | 4.5:1 | ✅ |
| text-secondary(#cbd5e1) / surface | ~9.6:1 | 4.5:1 | ✅ |
| text-muted(#94a3b8) / surface | ~5.1:1 | 4.5:1 | ✅ |
| text-link(#93c5fd) / surface | ~8.1:1 | 4.5:1 | ✅ |
| on-primary(#0f172a) / primary(#60a5fa) | ~6.7:1 | 4.5:1 | ✅ |
| on-danger(#0f172a) / danger(#f87171) | ~6.0:1 | 4.5:1 | ✅ |
| primary(#60a5fa) / primary-soft(다크 위) (nav active) | ~4.8:1 | 4.5:1 | ✅ |
| success-text(#86efac) / success-soft(badge) | ≥7:1 | 4.5:1 | ✅ |
| warning-text(#fcd34d) / warning-soft(badge) | ≥7:1 | 4.5:1 | ✅ |
| danger-text(#fca5a5) / danger-soft(badge) | ~5.7:1 | 4.5:1 | ✅ |

> 값은 `tokens.css` `[data-theme="dark"]` 실제 hex로 계산한 추정치. `color-scheme: dark`를 함께 설정해 스크롤바·네이티브 날짜선택기 등도 다크로 렌더한다. **tester 검증 권장**: 대시보드·청구 표·모달·뱃지를 다크에서 캡처해 대비 확인(자동 흐름 §6).

---

## 3. 타이포그래피 [UXD]

| 토큰 | 크기 | 용도 |
|------|------|------|
| `--font-size-xs` | 12px | 캡션·뱃지·도움말 |
| `--font-size-sm` | 14px | 보조 본문·표 |
| `--font-size-md` | 16px | **기본 본문·입력(모바일 최소)** |
| `--font-size-lg` | 18px | 카드 부제 |
| `--font-size-xl` | 20px | 섹션/카드 제목 |
| `--font-size-2xl` | 24px | 페이지 제목 `h1` |
| `--font-size-3xl` | 30px | 대시보드 지표 숫자 |

- Weight: `regular 400 / medium 500 / semibold 600 / bold 700`
- Line-height: `tight 1.25 / normal 1.5 / relaxed 1.7`
- Font: `Noto Sans KR` 우선(한국어), `Pretendard` 폴백 — 본문 16px 이상 권장.

---

## 4. 간격·radius·shadow·z-index [UXD]

- **Spacing**: 4px 베이스. `--space-1`(4) ~ `--space-16`(64). 컴포넌트 패딩·간격은 토큰만 사용.
- **Radius**: `sm 4 / md 8 / lg 12 / xl 16 / full`. 버튼·입력 `md`, 카드 `lg`, 뱃지 `full`.
- **Shadow**: `sm`(카드 기본) / `md`(드롭다운·토스트) / `lg`(모달).
- **z-index**: sticky 100 / overlay 1000 / modal 1100 / toast 1200.

---

## 5. 반응형 & 터치 [UXD]

| 브레이크포인트 | 폭 | 기준 |
|---------------|-----|------|
| 모바일 | 360px~ | 단일 컬럼, 카드 패딩 축소, 사이드바 → 수평 스크롤 탭 |
| 태블릿 | 768px~ | 2컬럼 그리드 |
| 데스크톱 | 1200px | 컨테이너 최대폭 + 240px 사이드바 |

- 터치 타깃: `--touch-target-min: 44px`. 버튼·탭·체크박스 래퍼·입력 모두 최소 44px 높이.
- 컨트롤 높이: `sm 36 / md 44(기본) / lg 52(모바일 주요 액션)`.
- `@media (prefers-reduced-motion: reduce)` → 트랜지션 0ms.
- 사이드바: 데스크톱 240px 고정. 모바일에서 수평 스크롤 탭으로 전환.

---

## 6. 접근성 체크리스트 (tester 검증 기준) [UXD]

> **76차 (2026-06-11)**: 차량 관리 표 행 액션 접근성 + §8-1 라우트 표 실측 정합 — coder가 `107bfb3`(G16)에서 추가한 `VehiclesPage`(US-T05/G16) 차량 목록 표의 **행별 「수정」 `Button`이 동일한 접근성 이름**만 노출해, 다중 차량 행에서 스크린리더 사용자가 **어느 차량을 수정하는지 식별 불가**하던 갭(WCAG 2.4.6·4.1.2)을 해소. 동일 코드베이스의 다른 표 행 액션(`AttendancePage`·`PaymentPage`·`BranchesPage`·`OverduePage`·`PlatformPage`·`VisitsPage`·`GuardianPortalPage`)은 모두 `aria-label`에 행 식별 정보를 포함하는데 `VehiclesPage`만 예외였다. 「수정」 버튼에 **`aria-label={\`${vehicle.plateNumber} 차량 수정\`}`**(예: 「12가3456 차량 수정」)을 부여해 차량번호로 동작 대상을 식별(시각 버튼 텍스트는 「수정」 유지, 접근성 이름만 컨텍스트 보강 — 31차 `GuardianInvitationList` 패턴 정합). 또한 **§8-1 라우트 표** 실측 정합 — 코드에는 있으나 표에 누락됐던 `/attendance/boarding`·`/attendance/on-site`(US-E06)·`/transport/vehicles`·`/transport/service-fees`·`/transport/outings`·`/reports/client-outings`(US-T05/G16·BNK-63) 6경로 추가(단일 원천=`App.jsx`/`navConfig.js`). 회귀: `VehiclesPage.test.jsx` 행 동작 라벨 검증(`12가3456 차량 수정`·caregiver 미노출). `npm test` 558/146 PASS·audit 0.
> **74차 (2026-06-10)**: `Field` 필수 입력 접근성 — `required` 필드가 시각적 `*`(aria-hidden)로만 필수 표기를 하고 컨트롤에 프로그램적으로 전달하지 않던 갭(WCAG 1.3.1·3.3.2)을 해소. `controlProps`에 `required` 시 **`aria-required="true"`**를 부여해 전 폼(`Field` 단일 원천)이 코드 변경 없이 스크린리더에 필수 상태를 안내한다. 네이티브 제약 검증을 피하려 HTML `required` 대신 `aria-required`만 사용(앱 자체 `Field error` 검증 유지). `Field.test.jsx`(+7) 회귀로 라벨 연결·`aria-required` 유무·`aria-invalid`+`role=alert`·경고 `role=status`·오류 우선·help describedby를 고정. 동반: US-G06 NHIS import 실서버 안내(`guidanceMessage` warning Alert) 완료 단위 커밋. `npm test` 542/144·build 848 modules·audit 0.
> **71차 (2026-06-10)**: G15·G11 신규 패널 접근성 재점검 + §8-1 라우트 표 실측 정합 — coder가 `3db8db3`에서 추가한 두 패널이 UXD 접근성 패스를 거치지 않아 남은 결함을 해소. ① **`TransportCompliancePanel`(G15)**: 5개 수칙 체크박스의 상세 설명(`rule.detail`)이 `<p>`로만 렌더돼 스크린리더가 체크박스에 도달해도 **짧은 라벨만 읽고 상세 맥락을 놓치던** 갭(WCAG 1.3.1)을 `aria-describedby`로 각 `Checkbox`↔설명 `<p id>` 연결해 해소(앱 `Field` describedby 패턴 정합). ② **`FeeSurchargeGuidePanel`(G11)**: 가산 미리보기 결과가 **조건부로 마운트되는** `aria-live` 영역이라 일부 스크린리더가 새로 삽입된 라이브 영역을 안내하지 못하던 갭(WCAG 4.1.3)을, 결과 컨테이너(`role="status"`·`aria-live="polite"`)를 **항상 DOM에 상주**시키고 텍스트만 토글하도록 전환해 해소. ③ **§8-1 라우트 표 실측 정합** — 코드에는 있으나 표에 누락됐던 `/billing/cms`(US-L03)·`/billing/reports/{charges,deposits,receipts}`·`/billing/calculator`(US-M03)·`/transport*`(US-T01~T03)·`/meals`·`/programs`(US-N01·N02)·`/staff`(§3-8)·`/organization/settings`(US-UX-03)·`/login` 추가, §8-2 그룹 표에 **이동**그룹·운영 그룹 확장 반영. 회귀 +3(`TransportCompliancePanel.test.jsx` aria-describedby 1·`FeeSurchargeGuidePanel.test.jsx` 상주 라이브 영역 1·미리보기 쿼리 정합 1). `npm test` PASS·build PASS·audit 0.
> **64차 (2026-06-09)**: 날짜 입력 `DateInput` 표준화 — `FeeSchedulePage`(US-G00a 적용 시작일)·`CopayRatePage`(US-G00b 적용 기준일)·`VisitScheduleForm`(US-V01 방문 날짜)의 raw `<TextInput type="date">`를 `DateInput`(`.ds-date-input` 폭·`Field` 라벨/오류 바인딩 단일 원천)으로 전환. 28차 「Must 화면 raw `type=date` 0건」 규율 회귀 해소 — raw `type="date"` 잔존 화면 0건 재확인(컴포넌트 내부만). 순수 표준화·동작 불변, 기존 회귀 PASS. `npm test` 326/93·build 804 modules·audit 0.
> **55차 (2026-06-09)**: US-J02 본인부담금 명세 상세·인쇄 — ① **`GuardianBillingDetailModal`** 신설: `Modal`(role=dialog·focus trap)로 월별 명세서 상세를 `<table caption(sr-only)·scope=row>`로 노출, **본인부담금 행** 색+굵게+`ds-sr-only` 라벨 병행(색만 의존 금지), 보조 항목(이용일수·총 급여비용·공단부담금·본인부담률)은 값 존재 시 행 렌더, 「열람 전용·CMS/알림 미지원」 안내. ② **인쇄**: `body.ds-statement-printing` 스코프 + `@media print`로 명세서만 노출(QR·청구 상세 인쇄 흐름과 비충돌). ③ **`GuardianPortalPage`**: 「명세 보기」 모달 → 인라인 명세 목록 표(자동 로드·`StatusBadge`·행별 「상세」 `aria-label` 청구월 포함) → 상세 모달 연동, 읽기 전용 `PaymentRecordModal` 의존 제거. `GuardianBillingDetailModal.test.jsx`·`GuardianPortalPage.test.jsx` 회귀 +3.
> **54차 (2026-06-08)**: US-UX-04 지점 스코프 안내 전면 연동 — ① **`BranchScopeNotice`**(`role=status`)를 `QrGeneratePage`(US-E03)·`TransportPage`·`TransportRunNewPage`·`TransportRunDetailPage`(US-T01~T03)에 연동해 출석·QR·배차 **6개 스코프 화면**에서 활성 지점명·hint를 텍스트로 노출(색만 의존 금지). ② QR 화면 전용 hint 「선택한 지점 기준 QR이 생성됩니다.」 ③ **`forced-colors`** — `.ds-branch-scope-notice` 경계선. `QrGeneratePage.test.jsx`·`TransportPage.test.jsx`·`pilotPageFlows` US-UX-04 4경로 회귀 +3.
> **44차 (2026-06-08)**: v1.3 배차·이동경로 UI(US-T01~T03) 접근성 재점검 — ① **헤딩 계층(WCAG 1.3.1·2.4.6)**: `Card` 내부 섹션 제목 `h2`→`h3`(AppShell `h1`→Card `h2`→섹션 `h3`)로 카드 제목과의 레벨 중복 제거 — `TransportPage`(당일 배차 명단·운행 루트)·`TransportRunNewPage`(배차 명단·정차 순서·지도). ② **표 접근성 이름**: `Table` `captionVisuallyHidden` prop 신설(`<caption class="ds-sr-only">`) — `TransportPage` 두 표에 시각 중복 없이 SR 전용 caption(당일 배차 명단·운행 루트) 부여. ③ **상태 메시지(WCAG 4.1.3)**: `TransportRunNewPage` 「선택 N/15명」 카운터 `role="status"`(aria-live polite)로 인원·상한 변화 SR 안내. `TransportPage.test.jsx` 헤딩 레벨·표 caption 회귀 +2.
> **42차 (2026-06-08)**: US-G06 DISCREPANCY 청구 라인 비교 링크·접근성 — ① **`DiscrepancyComparePanel`**: `Modal`(role=dialog·focus trap)로 공단(NHIS) vs ogada 청구 청구액·이용일수 비교 표(`caption`·`scope=col`·항목 `scope=row`). 차이는 `--color-warning-text` 색 + 「공단 초과/부족」`Badge` 텍스트 병행(색만 의존 금지), 차이 0 시 「동일」. `claimHref` 시 ogada 청구 라인 상세 `.ds-link`. ② **`NhisReconciliationTable` `onCompare`**: DISCREPANCY 행에만 「비교」`Button`(행별 `aria-label` 이용자명 포함), 그 외 `—`. 미제공 시 액션 열 미노출(하위 호환). ③ `ReconciliationPage` 비교 모달 배선. `.ds-compare-diff`·`.ds-compare-table th[scope=row]` CSS. `DiscrepancyComparePanel.test.jsx`·`NhisReconciliationTable.test.jsx` 회귀.
> **41차 (2026-06-08)**: US-F03 낙상·특이사항 이벤트 기록(파일럿 P3 동반) — ① **`IncidentRecordForm`**: 이벤트 유형 `Field`+`Select`(필수, 빈 값 시 `Field error`(role=alert)+`aria-invalid` 제출 차단)·발생 시각 `Field`+`TextInput type=time`(선택, help 「미입력 시 기록 시각」)·내용 `Field`+`Textarea`(필수 차단). 제출 중 `Button aria-busy`. 폼 `aria-label="낙상·특이사항 기록 입력"`. ② 이벤트 유형은 **코드+텍스트 라벨**(`INCIDENT_TYPES`)로 노출 — 이력 목록에서도 `[낙상] 내용` 텍스트 병행(색만 의존 금지). ③ `HealthPage` 4탭(일일 건강/투약/낙상·특이사항/이력) — 탭 전환은 기존 `Tabs` WAI-ARIA(좌우/Home/End) 재사용. `IncidentRecordForm.test.jsx`(필수 차단·payload 정합·시각 fallback 3건)·`healthRecords.test.js`(incident 파싱) 회귀.
> **40차 (2026-06-07)**: US-F01 활력징후 입력 경고·접근성 — ① 정상 범위 단일 원천 `utils/vitalsRanges.js`(`evaluateVital`/`findFormVitalsAbnormalities`/`findAbnormalVitalRecords`). ② **`Field` `warning` prop** — `role="status"`(polite)·`aria-describedby` 연결·`aria-invalid` 미설정(advisory, 저장 비차단). ③ `VitalsRecordForm` 비정상 입력 시 인라인 경고(텍스트+`--color-warning-text` 색 병행, 색만 의존 금지). ④ `HealthPage` 매직 넘버 제거(util 재사용). `vitalsRanges.test.js`·`VitalsRecordForm.test.jsx` 회귀.
> **38차 (2026-06-07)**: 수기 출석 체크인/아웃·결석 흐름(US-E01·E02, 파일럿 P2) — ① **`CheckoutModal`**: `Modal`(role=dialog·focus trap) + 귀가 교통편 `Field`+`Select`, 미선택 시 「귀가 확인」 `disabled`(색만 의존 금지), 실패 시 `Alert tone=danger`. ② **`AttendanceAbsentModal`**: 결석 사유 `Field`+`Textarea` 필수 — 빈 값 제출 시 `Field error`(role=alert)·`aria-invalid`로 차단. ③ **`AttendancePage`**: 당일 요약 `StatCard`(입소·귀가 완료·결석·미처리) + 이용자별 액션 `Table`(`caption`·`scope=col`), 행 액션 버튼 `aria-label`에 **이용자명 포함**(예: `홍길동 입소 처리`)으로 다중 행에서 SR 동작 대상 식별, 처리 중 `aria-busy`. 상태(입소/귀가/결석)는 `StatusBadge`+텍스트, 미처리/완료는 텍스트 라벨. `CheckoutModal.test.jsx`·`AttendanceAbsentModal.test.jsx`·`AttendancePage.test.jsx` 회귀.
> **39차 (2026-06-07)**: Must 흐름·접근성 — ① **`/guardian/checkin`**(US-E04) SideNav·포털 링크. ② **`VitalsRecordForm`**/`MedicationRecordForm`/`MedicationDuplicateAlert`(US-F01·F02) — Field 라벨·중복 `role=alert`. ③ **`NhisReconciliationTable`**(US-G06) — `ds-row--warning/danger`+StatusBadge. ④ **`HealthDetailPage`** `FilterChips` radiogroup(US-F04). ⑤ **`QrGeneratePage`** `.ds-qr-preview*`(인라인 style 0).
> **37차 (2026-06-07)**: `GuardianCheckinPage`(US-E04) 체크인 유형(입소/귀가) — 인라인 style raw radio `<fieldset>` → DS `FilterChips`(`role="radiogroup"`·`role="radio"`·`aria-checked`·44px·`forced-colors` 경계선). 색상만으로 의미를 전달하지 않도록 칩 텍스트(입소/귀가)+선택 버튼 라벨 변경(입소/귀가 처리) 병행. 인라인 `style` 0건. `GuardianCheckinPage.test.jsx` 회귀 2건.
> **35차 (2026-06-07)**: v1.2 P0 컴포넌트·SideNav 보강 — ① **`HealthAlertList`**(US-M02) Badge 「주의」+이름+사유, `aria-label` list. ② **`GuardianListCard`**(US-D01/K01) `MaskedPhone`·대표 Badge·`aria-label` 초대 버튼·`Card titleId`→`aria-labelledby`. ③ **`GradeHistoryTimeline`**(US-M01) `<ol aria-label="등급 변동 이력">`+sr-only 등급 변경. ④ **`BatchProgressSteps`**(US-G04) `nav`+sr-only 단계 상태·FAILED 처리. ⑤ **`CopayTypeSelect`**(US-D01) Field 라벨·비율 help. ⑥ **SideNav v1.2** — 지점·보호자·입금·미납·수가표 등 4그룹 하위 route 확장(US-UX-02 인수 조건 진전). `npm test` **78/27 PASS**·build **99 modules**.
> **34차 (2026-06-07)**: USER_STORIES·FLOWCHART Must 페이지 연동 — ① **ClientDetailPage** `Tabs`/`TabPanel`(US-D03 기본·건강·출석·청구)·`MaskedRevealField`(US-D04)·`GuardianInviteModal`(US-J01). ② **ClientListPage** `SearchInput`+`Pagination`(US-D02). ③ **DashboardPage** `DashboardWidgetGrid`+`StatCard`(US-H01/M02). ④ **BillingPage** `FilterChips`+`MonthInput`(US-G07). ⑤ **NHISImportPage** `NhisImportGuidePanel`+`FileUpload`(US-G04). ⑥ **HealthPage** `HealthAbnormalBanner`(US-F01). ⑦ **SessionTimeoutProvider**+`SessionTimeoutModal`(US-B03) `App.jsx` 배선. ⑧ Must 페이지 `Alert`+`.ds-page-alert` 통일. `Switch.test.jsx`·`MaskedRevealField.test.jsx`·`NhisImportGuidePanel.test.jsx`·`FileUpload.test.jsx` 회귀. `npm test` 69/22 PASS.
> **33차 (2026-06-07)**: USER_STORIES·FLOWCHART 대비 기반 UI 보강 — ① **2단 SideNav**(US-UX-02): `layout/SideNav.jsx`+`navConfig.js` 4그룹(운영·출석·기록·청구), `EXACT_MATCH_PATHS` prefix 충돌 방지, 모바일 그룹 토글 `aria-expanded`/`aria-controls`, 데스크톱 항상 펼침. ② **목록·상세 기반 컴포넌트**: `StatCard`(US-H01/M02)·`SearchInput`(US-D02)·`FilterChips`(US-G07 radiogroup+counts)·`Pagination`(nav+aria-current)·`Table`(caption 래퍼)·`Tabs`/`TabPanel`(WAI-ARIA 좌우/Home/End)·`BranchSwitcher`(US-B02, 2지점+ 시 노출)·`LogoutButton`(US-B03, `{이름} 로그아웃` aria-label). ③ **AppShell**: flat 1단 NavLink 제거 → `SideNav`+topbar `BranchSwitcher`+`LogoutButton`. ④ **LoginPage**: `PublicAuthLayout` 전환 — 공개 인증 화면 h1·skip·브랜드 일관(US-B01). ⑤ **CSS 갭 해소**: 페이지가 참조하던 `.ds-list`/`.ds-breadcrumb`/`.ds-form-grid` 미정의 → `components.css` 승격 + tabs·pagination·sidenav group·branch-switcher 스타일. `npm test` 58/18·build 86 modules PASS.
> **32차 (2026-06-07)**: 실측 baseline `7170b2a` 접근성 재점검 — ① **`Alert` 라이브 리전 정중도**: 기존 모든 tone이 `role="alert"`(assertive)이라 정적 info/success 배너가 스크린리더 흐름을 끊던 갭을 **tone 기준 분기**로 해소(`danger`/`warning`→`alert`, `info`/`success`/`neutral`→`status`). 호출부의 `role` 명시는 그대로 우선(override). ② **공개 인증 화면 헤딩 계층**: `GuardianInvitationAcceptPage`(US-J01)가 페이지 `<h1>` 없이 `Card` 제목(`<h2>`)만 노출하던 결함을 **`PublicAuthLayout`** 도입으로 수정 — 단일 h1·skip link(`#public-auth-content`)·브랜드 모노그램을 LoginPage와 일관되게 제공(미인증 화면은 AppShell/SideNav 금지 원칙 유지, §7-7n). `Alert.test.jsx`·`PublicAuthLayout.test.jsx` 회귀 추가.
> **31차 (2026-06-07)**: 실측 baseline `c3b863e` 접근성 재점검 — `GuardianInvitationList`(US-J01) 표 행의 「재발송」/「취소」`Button`이 동일 라벨이라 여러 행에서 SR이 **어느 보호자 동작인지 식별 불가**하던 갭을 보호자명 포함 `aria-label`(예: `홍보호 초대 재발송`)로 해소(27차 체크리스트 의도가 실측 baseline에 미반영이던 것을 반영). 동작 묶음 `aria-busy` 처리. `NavLink`(AppShell SideNav)는 활성 시 react-router 기본 `aria-current="page"` 노출 확인(색만 의존 아님). `GuardianInvitationList.test.jsx` 행 동작 라벨 회귀 +1.
> **30차 (2026-06-07)**: 스켈레톤 재이관(29차) 위 **폼 입력·토글·연락처 마스킹 컴포넌트 보강** — `Switch`(WAI-ARIA `role="switch"`·켜짐/꺼짐 텍스트 병행·44px·CSS 토큰 재사용, US-I03·§3-3), `DateInput`(US-D01 생년월일/인정유효일·US-L01 입금일·§3-1 기간 필터 — raw `<input type=date>` 차단), `MonthInput`(US-E05 통계·US-G02/G04/G07 청구·NHIS 대상월 — raw `<input type=month>` 차단), `MaskedPhone`(US-K01·L02 — `010-****-5678` 부분 마스킹 + `tel:` 링크 + `aria-label` 다이얼 안내). `DashboardPage` 미정의 `ds-stack*` 클래스 제거 → `.ds-app/.ds-topbar/.ds-main`+skip link 적용으로 키보드/SR 진입 흐름 수정. `ForbiddenPage` `.ds-auth-page`+`Card`로 LoginPage와 일관된 미인증 레이아웃.
> **5차 현행화 (2026-06-06)**: 구현 완료 항목을 `[x]`로 갱신.
> **6차 (2026-06-06)**: v1.2 P0 화면·컴포넌트 추가 — SideNav 2단 그룹, 등급 타임라인, 대시보드 위젯, 연락처 마스킹.
> **7차 (2026-06-06)**: USER_STORIES·FLOWCHART 대비 누락 보강 — `/billing/:id` 상세, 결석 사유 모달(US-E01), 이용자 사진+alt(US-D01), 보호자 초대 모달(US-J01), 청구 상태 이력 타임라인(US-G07), SideNav NHIS import, ClientPicker 키보드 탐색.
> **8차 (2026-06-06)**: FLOWCHART §5·§7·§9 갭 — `CheckoutModal`(US-E01 교통편), `DiscrepancyComparePanel`(US-G06), `GuardianBillingDetailModal`(US-J02), `ClientSelector`(복수 이용자 radiogroup), `CopayTypeSelect`(US-D01), `QrScanPanel`(US-E04), `branch_admin` SideNav 수기 체크인.
> **9차 (2026-06-06)**: USER_STORIES 잔여 갭 — `MedicationDuplicateAlert`(US-F02), `HealthAbnormalBanner`(US-F01), `SessionTimeoutProvider`(US-B03), 페이지 통합(GuardianPage·GuardianCheckinPage·AttendancePage·ReconciliationPage·HealthPage), `ToastProvider`/`SessionTimeoutProvider` 앱 루트 배선.
> **11차 (2026-06-06)**: **다크 모드** — `tokens.css` `[data-theme="dark"]` 토큰, `ThemeToggle`(AppShell topbar), `theme.js`. 다크 대비 AA 검증(§2-4).
> **12차 (2026-06-06)**: **로그인 진입 화면**(US-B01) 스타일 정비 — `LoginPage`가 참조하던 미정의 `.ds-label`로 라벨이 무스타일이던 문제를 `Field`/`TextInput`/`Button`(block·lg) 전환으로 해소, `.ds-login` 카드 레이아웃·브랜드 모노그램. **Modal 포커스 트랩**(Tab/Shift+Tab 순환). **고대비/강제 색상 모드**(`forced-colors`·`prefers-contrast: more`) — 배경 틴트 제거 시 경계선·시스템 강조색으로 식별성 보장.
> **13차 (2026-06-06)**: **전사 설정 토글 누락 보강**(US-I03·REQUIREMENTS §3-3·FLOWCHART §2) — `SettingsPage` 「조직 설정」의 `allow_client_self_checkin`이 정적 `<dl>` 설명 + `TODO`뿐이어서 조작 컨트롤이 없던 갭을 WAI-ARIA `switch` 패턴 `Switch` 컴포넌트로 해소. 켜짐/꺼짐 **텍스트 라벨 병행**(색·노브 위치만 의존 금지), 네이티브 `<button>` Enter/Space 토글, 44px 트랙, `forced-colors`에서 경계선+`Highlight` 채움으로 식별성.
> **16차 (2026-06-07)**: USER_STORIES·FLOWCHART 잔여 — `BatchProgressSteps`(US-G04), `PlatformOrgDetailModal`(US-A02), `PlatformPage` SearchInput·관리 모달, `ForbiddenPage` `ds-link`, 차트·진행단계 `forced-colors`.
> **17차 (2026-06-07)**: FLOWCHART §2·US-A02/I03/G07 — `AuditLogPanel`(sysadmin 감사 로그)·`BackupSettingsPanel`(백업 정책)·`PasswordChangeModal`(최초 로그인 필수 변경)·`FilterChips` 상태 카운트 배지·`LoginPage` 재설정 링크 스텁·`BillingPage`/`GuardianPage` raw `role=alert` → `Alert`·`Modal` `closeOnOverlay`/`closeOnEscape`/`showCloseButton`.
> **18차 (2026-06-07)**: REQUIREMENTS §3-1 잔여 — `LoginHistoryPanel`(sysadmin 로그인 이력 탭)·`PasswordResetRequestModal`(로그인 재설정 요청 UI)·Must 페이지 13곳 inline `role=alert` → `Alert tone=danger`+`.ds-page-alert` 통일(고대비 배경·경계선)·`GuardianCheckinPage` 피드백 `Alert tone=success|danger`·`PlatformOrgDetailModal.test.jsx` 회귀.
> **19차 (2026-06-07)**: `SettingsPage` security 탭 통합·`.ds-security-panel`·`token` useAuth 버그 수정.
> **20차 (2026-06-07)**: USER_STORIES·FLOWCHART 잔여 — `BillingStatusConfirmModal`·`NhisImportGuidePanel`·`CopayRateTable`·`GuardianDailySummary`·`HealthAlertList`·Must 페이지 `ds-page-alert` 잔여 5곳 통일.
> **21차 (2026-06-07)**: USER_STORIES·FLOWCHART 잔여 — `FeeScheduleTable`(US-G00a raw input 제거)·`BillingDetailPage` `BillingStatusConfirmModal` 연동(US-G07)·`StatCard tone=danger`(US-L02)·`.ds-text-secondary`·`.ds-mono`·`.ds-diff-amount`·`.ds-table-actions` 유틸·`HealthDetailPage`·`QrGeneratePage`·`ClientDetailPage` 탭·`ForbiddenPage` 접근성·Alert 통일.
> **22차 (2026-06-07)**: USER_STORIES·FLOWCHART 잔여 — `MonthInput`(US-E05·G04 raw month input 제거)·`PaymentRecordModal`(US-L01 PaymentPage 모달 추출)·`ReconciliationSummaryBar`(US-G06 `role=group`+sr-only 건수)·`ClientListPage` `SearchInput`·`NHISImportPage`/`AttendanceStatsPage`/`ReconciliationPage` 인라인 style→유틸 클래스·`.ds-page-alert` NHIS 업로드 오류.
> **23차 (2026-06-07)**: 인라인 style→유틸 클래스 잔여 정리 — Must 화면 `ClientDetailPage`(US-D03 탭·US-D04 주민번호 마스킹·US-M01 등급 이력)의 inline `style={{}}` 16건을 전량 제거하고 `.ds-inline-actions`(버튼·뱃지 중앙 정렬)·`.ds-client-summary*`(요약 헤더)·`.ds-dl-grid`(기본정보 정의 목록)·`.ds-section-gap`·`.ds-table-empty`로 승격. `ClientFormPage` 폼 하단 액션 `.ds-form-actions--end`(우측 정렬)·`PlatformPage` 사업자번호 `.ds-mono`·`GuardiansPage` 미지정 표시 `.ds-text-muted`. 토큰 기반이라 시각 동작 동일하나 다크/`forced-colors`에서 일관 적용 보장. `npm run build`·`npm test` 185/33 PASS(회귀 없음).
> **25차 (2026-06-08)**: USER_STORIES·FLOWCHART 잔여 — `BillingPage` raw month input → `MonthInput`(US-G02/G07)·`ChartContainer` `axisTextColor` prop + `.ds-chart__legend-label`(HealthTrendChart·BranchCompareChart 인라인 style 제거)·`PaymentPage` `.ds-section-gap`/`.ds-table-actions`·`GuardianDetailPage` 빈 상태 `EmptyState`(US-K02)·`LogoutButton` `aria-label` 회귀 테스트·`styles.css` 데모 `.role-link`/`.demo-grid` 제거·`.ds-input--month` → `.ds-month-input` 통합. `BillingPage.layout.test.jsx`·`LogoutButton.test.jsx`·`ChartContainer.test.jsx` axisTextColor 회귀.
> **26차 (2026-06-08)**: USER_STORIES·FLOWCHART **US-J01(FE-17) 잔여** — `GuardianInvitationAcceptPage`가 AppShell+SideNav를 사용하던 패턴을 **`PublicAuthLayout`**(LoginPage `.ds-login` 카드·skip link·브랜드) + **`GuardianInvitationAcceptForm`**(Field 라벨·`autoComplete` name/email/new-password·비밀번호/확인 구분·수락 완료 시 입력 잠금+「로그인하기」CTA)로 분리. **`INVITATION_STATUS`** Badge 상수(PENDING/SENT/ACCEPTED/EXPIRED/REVOKED). `.ds-auth-page*` CSS. `PublicAuthLayout.test.jsx`·`GuardianInvitationAcceptForm.test.jsx` 회귀.
> **27차 (2026-06-08)**: USER_STORIES·FLOWCHART **US-J01 초대 이력·§3-1 기간 필터** — **`DateInput`**(`MonthInput` 패턴, `AuditLogPanel`·`LoginHistoryPanel` raw `type=date` 제거)·**`GuardianInvitationList`**(`INVITATION_STATUS`+표 `caption`+재발송/취소 `aria-label`+`MaskedPhone`)·`GuardianListCard` 초대 이력 섹션·`ClientDetailPage` `guardianInvitations[]` 연동·`GuardianInvitationAcceptPage` 404/410 만료 시 `disabled` 폼 잠금·`ClientPhotoField` alt→`TextInput`·`GuardianInviteModal` `autoComplete`.
> **28차 (2026-06-08)**: USER_STORIES·FLOWCHART **DateInput·J01 접근성 잔여** — `ClientFormPage`(US-D01) 생년월일·인정 유효 시작일 raw `type=date` → **`DateInput`**·`PaymentRecordModal`(US-L01) 입금일 → **`DateInput`**·`ClientPhotoField` 사진 선택/변경/삭제 **`aria-label`**·`GuardianInviteModal` 발송 중 **`aria-busy`**·`ClientDetailPage` 초대 피드백 Alert **`ds-page-alert`** 통일. Must 화면 `type=date` raw input **0건**(DateInput·MonthInput만 허용).
> **24차 (2026-06-08)**: Must 페이지·모달 인라인 style 잔여 — `AttendancePage`(US-E01/E02 `.ds-page-lede`·`.ds-grid--gap-bottom`·`.ds-table-actions`)·`DashboardPage`(US-H01 `.ds-section-gap--lg`·`.ds-card-link`)·`GuardianPage`(US-J02 `.ds-card--mb`·`.ds-tab-panel-body`·`.ds-table-empty`)·`HealthPage`(US-F01~F03 `.ds-section-gap`)·`QrGeneratePage`(US-E03 `.ds-form-row__action`·`.ds-section-gap--bottom`)·`OverduePage`(US-L02 `.ds-page-footnote`+`.ds-link`)·`GuardianCheckinPage`(US-E04 `.ds-submit-block`)·모달 `CheckoutModal`/`AttendanceAbsentModal`/`SessionTimeoutModal`→`.ds-modal-intro`/`.ds-page-footnote`·`MedicationDuplicateAlert`/`HealthAbnormalBanner`→`.ds-alert-body*`·`PlatformOrgDetailModal`(US-A02 `.ds-mono`·`.ds-dl-grid--spaced`)·`BatchProgressSteps`/`FeeRateHistoryPanel` CSS 승격. `AttendancePage.layout.test.jsx` 회귀 추가.

- [x] 모든 폼 컨트롤에 `<label htmlFor>` 연결 — `Field` render-prop 패턴이 강제 (`htmlFor` ↔ `id` 자동 연결).
- [x] 오류는 색상 + 텍스트(`role="alert"`) + `aria-invalid`로 표기 — `Field error` prop 사용 시 자동 적용.
- [ ] 키보드만으로 로그인→대시보드→이용자 등록 핵심 흐름 완주 가능 — **tester E2E 검증 필요**.
- [x] `:focus-visible` 포커스 링이 모든 인터랙티브 요소에 보임 — `components.css §0` 전역 `:focus-visible` 규칙.
- [x] 탭(Tabs)은 WAI-ARIA 패턴(좌우/Home/End 키 이동, `aria-selected`, TabPanel `aria-labelledby` Context 연결).
- [x] 의미 있는 이미지에 `alt`, 장식 이미지에 `alt=""` — `ClientPhotoField`가 미리보기 `alt` 입력·플레이스홀더 `role="img"` 제공 (`ClientFormPage`).
- [x] 상태 뱃지는 색상만으로 의미를 전달하지 않음 — `StatusBadge`가 텍스트 라벨 + 색상을 항상 함께 출력.
- [x] 본문 바로가기(skip link) 제공 — `AppShell`의 `<a class="ds-skip-link" href="#main-content">`.
- [x] 색 대비 AA 충족 — §2-2 표 참조 (모든 시맨틱 조합 4.5:1 이상).
- [x] DISCREPANCY/UNMATCHED 표 행: 배경 + **좌측 4px 보더** (색상만 의존 금지).
- [x] Modal: `role="dialog"`, `aria-modal="true"`, `aria-labelledby` 연결 (인스턴스별 고유 ID — `useId()` 사용), ESC 닫기, 열림/닫힘 포커스 복원.
- [x] FileUpload: 숨겨진 input에 라벨·`aria-describedby` 연결. 드롭존 `role="button"` + Enter/Space 키.
- [x] Pagination: `<nav>`, 현재 페이지 `aria-current="page"`, 이전/다음 `aria-label`.
- [x] SideNav: `<nav aria-label="주 메뉴">`, 활성 링크 `.ds-nav-item--active`.
- [x] 주민번호 열람: `aria-label="주민번호 열람 (audit 기록됨)"` + 마스킹 표시(US-D04).
- [x] FilterChips: `role="radiogroup"` + `role="radio"` + `aria-checked` + **WAI-ARIA radio group 키보드 패턴(roving tabindex — 그룹 단일 Tab 정지점, ←/→/↑/↓·Home/End 이동·선택)** (US-G07·69차, `Tabs`와 동일 패턴).
- [x] 이동서비스 수칙 체크리스트(71차, US-T05/G15): `TransportCompliancePanel` — 각 `Checkbox`에 `aria-describedby`로 상세 설명(`<p id>`) 연결(SR이 라벨+상세 함께 안내, WCAG 1.3.1), 진행 카운터 `role="group"`+`aria-live="polite"`, 계약서·일지 `Modal`(focus trap).
- [x] 가산율 미리보기 라이브 영역(71차, US-M05/G11): `FeeSurchargeGuidePanel` — 결과 컨테이너를 `role="status"`·`aria-live="polite"`로 **상시 상주**(조건부 마운트 제거, WCAG 4.1.3), 가산표 `caption`(sr-only)·`scope=col`, 중복불가 안내 텍스트 병행.
- [x] 건강 수치 비정상 시 `aria-invalid="true"` + `role="alert"` 오류 메시지 — `HealthPage` `Field error` + `Alert` (US-F01).
- [x] 수동 매칭 모달(US-G06): 지점·Tenant 제약 안내 `Alert tone="warning"` 포함 — `ReconciliationPage`.
- [x] 지점 관리(US-C01): 등록/수정 `Modal`(role=dialog)·`Field` 라벨 연결, 지점명 빈 값 시 `Field error`(role="alert"·`aria-invalid`), 상태 `BRANCH_STATUS` 텍스트+색.
- [x] 월별 출석 통계(US-E05): `<input type="month">` `Field` 라벨 연결, 표 `caption`, 차트 `role="img"`+`aria-label`, 조회 오류 `role="alert"`.
- [x] 보호자 목록(US-D01·US-J01): `GuardianListCard` — `aria-labelledby` 섹션 제목, 전화번호 `<a href="tel:">` + `aria-label`, 초대 스텁 `aria-disabled="true"` + `title` 설명.
- [x] 2단 SideNav(US-UX-02): 그룹 토글 `aria-expanded`/`aria-controls`, 하위 항목 `.ds-nav-item--nested`, 데스크톱 항상 펼침·모바일 접힘/펼침.
- [x] 등급 이력(US-M01): `GradeHistoryTimeline` — `<ol aria-label="등급 변동 이력">`, 등급 변경 `sr-only` 텍스트, 화살표는 `aria-hidden`.
- [x] lifecycle 업무 패널(85차, G34·US-T09·US-T10): `LifecycleWorkflowPanel` — 단계 `ol`에 상태 `StatusBadge` 텍스트 라벨, 기한·완료일·담당·서명 필요/완료·증빙 목록을 텍스트로 노출. `OVERDUE`는 danger 색상 외 「기한 초과」Badge와 좌측 보더를 병행하고, `forced-colors`에서 outline으로 보강.
- [x] 연락처 마스킹(US-K01·L02): `MaskedPhone` — 부분 마스킹 + `tel:` 링크 + `aria-label`.
- [x] 보호자 연결(US-K02): `LinkedClientsCard` — 대표 보호자 `Checkbox` 라벨 연결, `aria-labelledby` 섹션 제목.
- [x] 입금 처리(US-L01): `PaymentPage` — `Field` 라벨·`type="date"`/`inputMode="numeric"`, Modal `useId()` 패턴 재사용.
- [x] 미납 목록(US-L02): `OverduePage` — `.ds-row--warning` 행 강조 + 「미납」텍스트 Badge(색상만 의존 금지).
- [x] 대시보드 위젯(US-M02): `DashboardWidgetGrid` — 위젯 링크 `sr-only` 보조 텍스트, 로딩 `role="status"`.
- [x] 청구 상세(US-G02): `BillingDetailPage` — 상태 이력 `ClaimStatusTimeline`, 확정 후 불변 `Alert`, 인쇄 `@media print` 사이드바 숨김.
- [x] 결석 처리(US-E01): `AttendanceAbsentModal` — 사유 `Field`+`role="alert"`, 미처리 행 「결석」버튼 `aria-label`.
- [x] 보호자 초대(US-J01): `GuardianInviteModal` — `Modal`+`Field` 라벨 연결, `ClientDetailPage`에서 재사용.
- [x] ClientPicker(US-G06): combobox `aria-activedescendant` + Arrow/Enter/Escape 키 탐색.
- [x] 지점 스코프 안내(54차, US-UX-04): `BranchScopeNotice` — `role="status"`·활성 지점명·hint 텍스트, 출석·QR·배차 6화면 일관(`AttendancePage`·`AttendanceStatsPage`·`QrGeneratePage`·`TransportPage`·`TransportRunNewPage`·`TransportRunDetailPage`), `forced-colors` 경계선.
- [x] 본인부담금 명세 상세·인쇄(55차, US-J02): `GuardianBillingDetailModal` — `Modal`(role=dialog·focus trap), 상세 `<table caption(sr-only)·scope=row>`, 본인부담금 행 색+굵게+`ds-sr-only` 라벨 병행(색만 의존 금지), `window.print()` + `body.ds-statement-printing` 스코프 `@media print`(명세서만 노출). `GuardianPortalPage` 인라인 목록 표(행별 「상세」 `aria-label` 청구월 포함) → 상세 모달.
- [x] 대시보드 NHIS 대기(보류) 위젯(60차, BNK-19·US-M02 P1): `DashboardPage` 6번째 위젯 `nhisPendingReviewCount` — tone=warning(`>0`), `/billing/imports/nhis` 링크, `sumNhisPendingReviewFromBatches` 집계(배치 `pendingReviewCount` 합산). `ReconciliationPage` `StatCard` 동일 원천 — 지점·HQ 대시보드 동시 반영.
- [x] 지역 선택기(60차, US-D01·US-C01): `RegionSelector`(`components/branches/`) — 시·도→시·군·구→읍·면·동 3단 연계 `Field`+`Select`, 로드 중 `Spinner`(`aria-label`), 상위 미선택 시 하위 `disabled`, 로드 오류 `role="alert"`. `RegionSelector.test.jsx` 2건.
- [x] 이용자 목록 표 전환(60차, US-D02): `ClientListPage` `ds-list` → `Table`(`caption` SR 이름) — 나이·성별·지역·등급·인정번호·보호자·연락처 8열, 검색 범위 확대(지역·보호자명·성별·`genderLabel`/`formatAge` 유틸).
- [x] 식단 등록 폼(60차, US-N01): `MealsPage` `canManageMenus` 조건부 `MealMenuForm` 렌더 + `handleMenuSubmit` — `hq_admin`·`branch_admin`만 「식단 등록」`<section aria-labelledby>` 노출, 빈 상태 안내 역할별 분기.
- [x] SideNav 그룹 토글: `aria-label="{그룹} 메뉴 그룹"` (모바일 접힘/펼침).
- [x] GuardianListCard·GuardianPage: 연락처 `MaskedPhone`, 청구 상태 `StatusBadge`+`BILLING_STATUS` (색상만 의존 금지).
- [x] CheckoutModal(US-E01): 귀가 교통편 `Field`+`Select` 라벨, 미선택 시 확인 버튼 `disabled`, 오류 `role="alert"`.
- [x] ClientSelector(US-E04·J02): `role="radiogroup"` + `role="radio"` + `aria-checked`, 1명일 때 `hideWhenSingle` 숨김.
- [x] DiscrepancyComparePanel(US-G06): 차이 컬럼 `Badge` 텍스트 라벨 + 좌측 4px `--color-compare-highlight` 보더.
- [x] GuardianBillingDetailModal(US-J02): `<table>` `caption`·`scope`, 본인부담금 행 강조, 인쇄 `@media print`.
- [x] QrScanPanel(US-E04): 카메라 `aria-busy`, 수동 입력 `Field` 라벨, 카메라 불가 `Alert` 안내.
- [x] CopayTypeSelect(US-D01): 구분별 비율 help 텍스트, `aria-invalid` 오류 연동.
- [x] MedicationDuplicateAlert(US-F02): 동일 시각 투약 `role="alert"` 경고 + 「확인 후 계속」 링크 버튼 — `HealthPage`.
- [x] HealthAbnormalBanner(US-F01): 비정상 수치 항목별 `Badge` 텍스트 라벨 + 값 목록.
- [x] SessionTimeoutProvider(US-B03): 30분 비활성 → 60초 전 `SessionTimeoutModal`, `App`+`AuthProvider` 하위 배치.
- [x] ClientUserAccountField(US-D01): 발급 토글 `Checkbox`(라벨 44px), 체크 시에만 로그인 이메일 `Field`(`type="email"`·`aria-invalid`) 노출, `allow_client_self_checkin` off면 `Alert tone="info"` 안내 — `ClientFormPage`.
- [x] 다크 모드(11차): `ThemeToggle` `aria-pressed`+아이콘(`aria-hidden`)+텍스트 라벨 병행, 44px. `[data-theme="dark"]` 토큰 전 조합 AA(§2-4). `color-scheme: dark`로 네이티브 위젯도 다크.
- [x] 로그인 화면(12차, US-B01): `LoginPage` → `Field`(label↔id 연결)·`TextInput`(`autoComplete` 보존)·`Button block size=lg`(44px↑)·오류 `Alert tone="danger"`(role=alert). 미정의 `.ds-label` 무스타일 라벨 제거.
- [x] Modal 포커스 트랩(12차): 열린 다이얼로그에서 Tab/Shift+Tab이 내부 포커스 가능 요소만 순환(`aria-modal` 보강). ESC 닫기·포커스 복원 유지.
- [x] 고대비/강제 색상(12차, WCAG 1.4.11): `forced-colors: active` 시 버튼·뱃지·카드·모달·표 주의행에 경계선 강제 + 포커스/활성 내비 `Highlight`. `prefers-contrast: more` 시 보조 텍스트 대비 상향·포커스 링 3px.
- [x] Switch(13차, US-I03·§3-3): `role="switch"` + `aria-checked`, 라벨 `aria-labelledby`·설명 `aria-describedby` 연결, 켜짐/꺼짐 텍스트 병행(색만 의존 금지), 네이티브 `<button>` 키보드 토글, 44px 트랙, `forced-colors`에서 트랙 경계선+`Highlight` 채움. `SettingsPage` `allow_client_self_checkin` 적용.
- [x] CopayTypeSelect 실적용(US-D01): `ClientFormPage` 본인부담 구분 raw `<Select>` → `CopayTypeSelect`(비율 help·`aria-invalid`).
- [x] GuardianPage(US-J02): `ClientSelector` radiogroup + 명세 행 「상세」→ `GuardianBillingDetailModal`.
- [x] GuardianCheckinPage(US-E04): `QrScanPanel`+`ClientSelector` 통합, 피드백 `.ds-feedback--success/danger`.
- [x] AttendancePage(US-E01): 「귀가」→ `CheckoutModal` (표 인라인 select 제거, 모바일 터치 우선).
- [x] ReconciliationPage(US-G06): DISCREPANCY 「비교」→ `DiscrepancyComparePanel` 모달, 수동 매칭 `ClientPicker`.
- [x] ToastProvider: `main.jsx` 루트 — API 피드백 전역 준비.
- [ ] 키보드만으로 로그인→대시보드→이용자 등록 핵심 흐름 완주 가능 — **tester E2E 검증 필요**.
- [x] NHIS 배치 상태(US-G04): `BATCH_STATUS` Badge 모듈로 승격(14차) — NHISImportPage 로컬 중복 제거, 색상+텍스트 라벨 일관성.
- [x] 수가 이력(US-G00a): `FeeRateHistoryPanel` — 표 `caption` 스크린리더 행 설명, 수가 숫자 `aria-label` 포함.
- [x] NHIS 배치 진행(US-G04): `.ds-progress-steps` — 단계별 텍스트 라벨(`ds-progress-steps__label`) 병행(색만 의존 금지), `ds-sr-only` 단계 설명 포함.
- [x] Recharts 차트(15차, US-F04/H01/E05/H02): `ChartContainer` — `role="figure"`+`figcaption`+`aria-describedby` sr-only 데이터 요약, 빈 데이터 `role="status"`. `HealthTrendChart` Legend 텍스트 라벨 병행(색만 의존 금지). `useChartColors` MutationObserver로 다크 전환 실시간 반영.
- [x] 수가표 1밴드 안내(15차, UXD-4): `FeeSchedulePage` Alert·Card actions에 「표준 이용시간 8~10h · 1밴드 고정」help 텍스트.
- [x] 인라인 링크(15차): `.ds-link` — `DashboardPage` `role-link` → `ds-link` 전환, `forced-colors` LinkText.
- [x] NHIS 배치 진행(16차, US-G04): `BatchProgressSteps` — `nav`+`aria-label`+`sr-only` 현재 단계 안내, 단계별 텍스트 라벨 병행, `FAILED` 시 처리중 단계 실패 표시.
- [x] 플랫폼 고객사(16차, US-A01/A02): `PlatformPage` `SearchInput` 라벨 연결, Tenant 상태 `StatusBadge`+`BRANCH_STATUS`, 「관리」`aria-label`, `PlatformOrgDetailModal` 관리자 발급 `Field`+`Alert`.
- [x] 403 페이지(16차): `ForbiddenPage` 로그인 링크 `ds-link` 통일.
- [x] 보호자 초대(16차): `GuardianListCard` 「초대 발송」`aria-label` 명시.
- [x] 차트·진행단계 고대비(16차): `forced-colors` 시 `.ds-chart__viewport`·`.ds-progress-steps__dot` 경계선 보강.
- [x] 배차·이동경로 고대비(50차, US-T01~T03): `forced-colors` 시 `.ds-transport-map__canvas`·`.ds-transport-stop`·`.ds-transport-map-marker` 경계선 + `.ds-transport-map-marker--active`·`.ds-transport-stop__order` `Highlight` 강제·정차 `box-shadow`→`outline` 전환(소거 방지).
- [x] BranchCompareChart(48차·50차 확인, US-H02): `DashboardPage` HQ variant에 `BranchCompareChart` 통합 완료 — `role="figure"`+`figcaption`+sr-only 요약, 빈 데이터 `role="status"`, Legend `ds-chart__legend-label` 텍스트 라벨 병행(색만 의존 금지).
- [x] 감사 로그(17차, US-I03): `AuditLogPanel` — `Field` 라벨·이벤트 `Badge` 텍스트 라벨·표 `caption`·PII `ds-masked`·로딩 `Spinner` `aria-label`.
- [x] 백업 설정(17차, US-I03): `BackupSettingsPanel` — `Switch` 자동 백업·상태 `Badge` 텍스트·수동 백업 `Button` `aria-busy`.
- [x] 최초 비밀번호 변경(17차, US-A02): `PasswordChangeModal` — 필수 모드 ESC/오버레이/✕ 차단·`Alert` 보안 안내·`Field`+`autoComplete=new-password`.
- [x] 청구 상태 카운트(17차, US-G07): `FilterChips` `counts` prop — 숫자 배지 + `aria-label` 「N건」 병행(색만 의존 금지).
- [x] 페이지 오류 표시(17차): `BillingPage`·`GuardianPage` inline `role=alert` → `Alert tone=danger` 통일.
- [x] 테이블 내 링크(17차): `BillingPage` 이용자명 `button.ds-link`(키보드·포커스 링 일관).
- [x] 로그인 이력(18차, §3-1): `LoginHistoryPanel` — `Field` 필터·표 `caption`·이메일/IP `ds-masked`·결과 `Badge` 텍스트 라벨·`SettingsPage` 「로그인 이력」탭.
- [x] 비밀번호 재설정(18차, §3-1): `PasswordResetRequestModal` — `Field`+`autoComplete=username`·요청 완료 `Alert tone=success`·`LoginPage` `button.ds-link` 진입.
- [x] 페이지 오류 표시(18차): Must 페이지 API 오류 — inline `<p role=alert>` 금지, `Alert tone=danger`+`.ds-page-alert` 통일(`forced-colors` 배경·테두리 포함). 대상: ClientList/Detail, Attendance/Stats, Health, Branches, Guardians/Detail, BillingDetail, Payment, Overdue, Reconciliation matchError, GuardianCheckin 피드백.
- [x] 보안 탭 통합(19차, §3-1): `SettingsPage` security 탭 — `PasswordChangeModal`(비밀번호 변경)·`PasswordResetRequestModal`(재설정 요청)을 LoginPage 진입 외 SettingsPage에서도 독립 접근 가능. `.ds-security-panel`(flex 컨테이너) 내 `Alert tone=info` 안내 + `ds-action-bar__actions` 버튼 그룹. sysadmin·hq_admin·platform_admin 역할만 노출, 외 역할은 `Alert tone=info` 권한 안내.
- [x] `token` 세션 버그(19차): `SettingsPage.jsx` `handlePasswordChange` 내 `token` 참조 — `useAuth()` 구조분해에 `token` 누락 → 수정 완료(`const { user, token } = useAuth()`). REQUIREMENTS §3-1 세션 만료 감지.
- [x] 청구 상태 전이 확인(20차, US-G07): `BillingStatusConfirmModal` — 확정(CONFIRMED) 시 「수정 불가」`Alert tone=warning`, `StatusBadge`+금액 요약 `dl`, `BillingPage` 목록 액션 전 확인 모달. `BILLING_STATUS_TRANSITIONS` 상수 export.
- [x] NHIS import 온보딩(20차, US-G04): `NhisImportGuidePanel` — Chrome/Edge `Alert`, 4단계 `ol`+`sr-only` 단계 번호, `처리상태` 선행열 안내, `NHISImportPage` 인라인 중복 제거.
- [x] 본인부담 비율표(20차, US-G00b): `CopayRateTable` — `TextInput type=number`+`aria-label`, `COPAY_TYPES` 기본값·변경 `sr-only` 안내, `CopayRatePage` raw `<input>` 제거.
- [x] 보호자 포털 요약(20차, US-I02): `GuardianDailySummary` — `ATTENDANCE_STATUS` 라벨 StatCard, `HealthAlertList` 연동, `GuardianPage` `EmptyState` 빈 연결 이용자.
- [x] 보호자 포털 식사 기록(62차, US-I02·FLOWCHART §9): `GuardianDailySummary` — `dailyRecord.meals[]`를 식사 구분(`MEAL_TYPES` 텍스트 라벨) + 식사량 `StatusBadge`(`MEAL_INTAKE_BADGE`, 텍스트+색 병행, 색만 의존 금지)로 노출, 빈 식사 `—`. `config/meals.js` 단일 원천 재사용.
- [x] 건강 이상 목록 공통(20차): `HealthAlertList` — `Badge tone=warning` 「주의」텍스트+색 병행, `DashboardPage`·`GuardianDailySummary` 재사용.
- [x] 페이지 오류 Alert 잔여(20차): `PlatformPage`·`BillingPage`·`DashboardPage`·`GuardianPage`·`CopayRatePage` → `Alert`+`.ds-page-alert` 패턴 통일.
- [x] 수가표 편집(21차, US-G00a): `FeeScheduleTable` — `TextInput`+`aria-label`+`caption`, `FeeSchedulePage` raw `<input>` 제거.
- [x] 청구 상세 상태 전이(21차, US-G07): `BillingDetailPage` topbar 「확정」/「수납완료」→ `BillingStatusConfirmModal` — 목록과 동일 패턴.
- [x] 미납 지표(21차, US-L02): `OverduePage` 인라인 danger 색상 → `StatCard tone=danger`+`.ds-stat__value--danger`(텍스트 라벨 병행).
- [x] NHIS reconciliation 차이(21차, US-G06): `ReconciliationPage` 차이 금액 `.ds-diff-amount`+`sr-only` 「차이」+`aria-label`, 인정번호 `.ds-mono`.
- [x] 페이지 오류 Alert 잔여(21차): `HealthDetailPage`·`QrGeneratePage`·`ClientDetailPage` 건강/출석 탭 → `Alert tone=danger`+`.ds-page-alert`.
- [x] 403 페이지(21차): `ForbiddenPage` 인라인 style → `.ds-forbidden-page__desc`·`__actions`+`.ds-link`.
- [x] 대상 월 입력(22차, US-E05·G04): `MonthInput` — `Field`+`TextInput type=month`+`.ds-month-input`, raw `<input class=ds-input>` 금지. `AttendanceStatsPage`·`NHISImportPage`.
- [x] 입금 기록(22차, US-L01): `PaymentRecordModal` — `Field` 라벨·`aria-invalid`·수단 `Select`·`.ds-modal-intro` 요약. `PaymentPage` 목록 「입금 기록」`aria-label`.
- [x] NHIS reconciliation 요약(22차, US-G06): `ReconciliationSummaryBar` — `role=group`·Badge 숫자+`sr-only` 「N건」·`.ds-summary-bar`. `ReconciliationPage`.
- [x] 이용자 검색(22차, US-D02): `ClientListPage` raw search → `SearchInput hideLabel` (`htmlFor`·`type=search`).
- [x] 인라인 style 잔여 제거(23차, US-D03/D04/M01): `ClientDetailPage` inline `style={{}}` 16건 → `.ds-inline-actions`·`.ds-client-summary*`·`.ds-dl-grid`·`.ds-section-gap`·`.ds-table-empty`. `ClientFormPage` `.ds-form-actions--end`·`PlatformPage` `.ds-mono`·`GuardiansPage` `.ds-text-muted`. 토큰 기반이라 `forced-colors`·다크에서 일관 적용.
- [x] 청구 목록 월 필터(25차, US-G02/G07): `BillingPage` `MonthInput`+`Field` — raw `ds-input--month` 제거.
- [x] 차트 범례 텍스트(25차): `ChartContainer` `axisTextColor` → `--chart-axis-text` CSS 변수, `.ds-chart__legend-label` — 다크/`forced-colors` 일관.
- [x] 입금 처리(25차, US-L01): `PaymentPage` 안내 `Alert` `.ds-section-gap`, 표 액션 `.ds-table-actions`.
- [x] 보호자 상세 빈 상태(25차, US-K02): `GuardianDetailPage` API 미응답 시 `EmptyState`+`ds-page-alert` — raw `role=status` 문단 제거.
- [x] 로그아웃 버튼(25차, US-B03): `LogoutButton` AppShell topbar — `aria-label="{이름} 로그아웃"`, 미인증 시 null 렌더.
- [x] 보호자 초대 수락(26차, US-J01): `PublicAuthLayout`+`GuardianInvitationAcceptForm` — 미인증 공개 화면은 **AppShell/SideNav 금지**, LoginPage와 동일 `.ds-login` 카드·skip link, Field+`autoComplete`, 비밀번호/확인 라벨 분리, 수락 완료 `Alert tone=success`+입력 `disabled`+「로그인하기」CTA, 만료 `Alert tone=danger`.
- [x] 보호자 초대 상태(26차, US-J01): `INVITATION_STATUS` — `StatusBadge` 텍스트+색(PENDING/SENT/ACCEPTED/EXPIRED/REVOKED).
- [x] 기간 필터 DateInput(27차, §3-1): `AuditLogPanel`·`LoginHistoryPanel` — raw `type=date`+`ds-input` → `DateInput`+`Field` 라벨 연결, `.ds-date-input` max-width.
- [x] 보호자 초대 이력(27차, US-J01): `GuardianInvitationList` — 표 `caption`·`scope`·`INVITATION_STATUS` Badge·`MaskedPhone`·재발송/취소 `Button` `aria-label`·`GuardianListCard` 「초대 이력」섹션.
- [x] 만료 초대 수락(27차, US-J01): `GuardianInvitationAcceptPage` API 404/410 → `GuardianInvitationAcceptForm disabled` 입력 잠금.
- [x] alt·사진 설명(27차, US-D01): `ClientPhotoField` alt 입력 raw `<input>` → `TextInput`+`Field`.
- [x] DateInput 표준화(28차, US-D01·US-L01): `ClientFormPage` 생년월일·인정 유효 시작일·`PaymentRecordModal` 입금일 — raw `TextInput type=date` → `DateInput`+`Field`. 신규 `type=date`는 **DateInput만** 사용(MonthInput과 대칭).
- [x] 사진 업로드 버튼(28차, US-D01): `ClientPhotoField` — 선택/변경/삭제 `Button`에 `aria-label`+`aria-controls`(숨김 file input id) 연결.
- [x] 보호자 초대 발송(28차, US-J01): `GuardianInviteModal` — 발송 중 `Button` `aria-busy`. `ClientDetailPage` 초대 성공/오류 `Alert`+`.ds-page-alert`.
- [x] Must 페이지 인라인 style 잔여(24차, US-E01~E04/H01/F01~F03/J02/L02/A02): `AttendancePage` `.ds-page-lede`·`.ds-grid--gap-bottom`·`.ds-table-actions`·`DashboardPage` `.ds-section-gap--lg`·`.ds-card-link`·`GuardianPage` `.ds-card--mb`·`.ds-tab-panel-body`·`.ds-table-empty`·`HealthPage` `.ds-section-gap`·`QrGeneratePage` `.ds-form-row__action`·`OverduePage` `.ds-page-footnote`·`GuardianCheckinPage` `.ds-submit-block`·모달 `.ds-modal-intro`/`.ds-alert-body*`. `AttendancePage.layout.test.jsx` 회귀.
- [ ] 키보드만으로 로그인→대시보드→이용자 등록 핵심 흐름 완주 가능 — **tester E2E 검증 필요** (중복 항목 — 구현 완료 후 tester 검증 대기).
- [x] Switch(30차, US-I03·§3-3): `Switch` 컴포넌트 재도입 — `role="switch"` + `aria-checked`, 라벨 `aria-labelledby`·설명 `aria-describedby` 연결, 켜짐/꺼짐 **텍스트 병행**(색·노브 위치만 의존 금지), `<button type=button>` 네이티브 키보드 토글, 44px 트랙 hit target, `forced-colors`에서 트랙 경계선+`Highlight` 채움(§9 CSS). `onChange(next)`가 다음 boolean 값을 인자로 받음(이벤트 객체 아님).
- [x] DateInput(30차, US-D01·US-L01·§3-1): `DateInput` 컴포넌트 재도입 — `Field` 안 `TextInput type=date` 래퍼 + `.ds-date-input` max-width. raw `<input type=date class=ds-input>` **금지**.
- [x] MonthInput(30차, US-E05·G02/G04/G07): `MonthInput` 컴포넌트 재도입 — `Field` 안 `TextInput type=month` 래퍼 + `.ds-month-input` max-width. raw `<input type=month>` **금지**.
- [x] MaskedPhone(30차, US-K01·L02): `MaskedPhone` 컴포넌트 — 가운데 그룹 마스킹(`010-****-5678`, 10자리·11자리·기타 포맷 허용)·`<a href="tel:">` 링크·`aria-label`로 SR 다이얼 안내. **PII 보호**: 시각 UI는 항상 마스킹 유지, `withLink=false`이면 `<span>` 정적 표시.
- [x] DashboardPage 골격(30차): 존재하지 않는 `.ds-stack*`/`.ds-gap-sm` 잔재 제거 → `.ds-app`+`.ds-topbar`(`ThemeToggle`+`로그아웃` `aria-label`)+`.ds-main`+skip link로 AppShell 패턴 확립. `<dl class=ds-dl-grid>`로 역할/세션/다음 단계 요약(색만 의존 금지).
- [x] ForbiddenPage(30차): `.ds-auth-page`+`Card` 사용으로 LoginPage와 동일한 미인증 카드 레이아웃, `aria-labelledby` 연결, 「로그인으로 이동」 primary 버튼.
- [x] 초대 이력 행 동작 라벨(31차, US-J01): `GuardianInvitationList` 표 「재발송」/「취소」`Button` — 보호자명 포함 `aria-label`(`{이름} 초대 재발송|취소`)로 다중 행에서 SR 동작 대상 식별, `ds-table-actions` `aria-busy={pending}`. 시각 버튼 텍스트는 「재발송」/「취소」 유지(공간 절약), 접근성 이름만 컨텍스트 보강. `GuardianInvitationList.test.jsx` 회귀.
- [x] SideNav 활성 표시(31차): `AppShell`의 react-router `NavLink`가 활성 시 `aria-current="page"`를 기본 출력 — 활성 메뉴를 색(`.ds-nav-item--active`) 외 SR/접근성 트리에도 노출(색만 의존 금지 원칙 충족).
- [x] Alert 라이브 리전 정중도(32차): `Alert` 기본 `role`을 tone 기준 분기 — `danger`/`warning`→`role="alert"`(assertive), `info`/`success`/`neutral`→`role="status"`(polite). 정적 안내가 스크린리더 흐름을 끊지 않도록 함. `role` prop 명시 시 그대로 우선. `Alert.test.jsx` 회귀.
- [x] 공개 인증 화면 헤딩 계층(32차, US-J01): `GuardianInvitationAcceptPage`를 `PublicAuthLayout`로 전환 — 페이지 단일 `<h1>`(화면 제목)·skip link(`#public-auth-content`)·브랜드 모노그램(LoginPage 일관). 기존 `Card`(`<h2>`)만 있던 헤딩 결함 해소. `PublicAuthLayout.test.jsx` 회귀.
- [x] 2단 SideNav(33차, US-UX-02): `SideNav`+`navConfig.js` — 운영·출석·기록·청구 4그룹, `aria-expanded`/`aria-controls` 모바일 토글, `NavLink` `aria-current="page"`, `EXACT_MATCH_PATHS` prefix 활성 충돌 방지. `SideNav.test.jsx` 회귀.
- [x] 목록·필터·페이지네이션(33차, US-D02/G07): `SearchInput`(`type=search`+`aria-label`)·`FilterChips`(`role=radiogroup`+counts `aria-label`)·`Pagination`(`nav`+`aria-current=page`+이전/다음 `aria-label`). `FilterChips.test.jsx`·`Pagination` 회귀는 Tabs/BranchSwitcher/LogoutButton 일괄.
- [x] 이용자 상세 탭 골격(33차, US-D03): `Tabs`/`TabPanel` — `role=tablist/tab/tabpanel`, `aria-selected`, Arrow/Home/End 키. `Tabs.test.jsx` 회귀.
- [x] 지점 선택기(33차, US-B02): `BranchSwitcher` — 2지점 이상 시만 노출, `Field`+`Select`, `aria-label=작업 지점 선택`. API `PATCH /auth/active-branch` 연동은 coder.
- [x] 로그아웃 접근성(33차, US-B03): `LogoutButton` — `aria-label="{이름} 로그아웃"`, 미인증 null. `AppShell` topbar 기본 탑재.
- [x] 로그인 PublicAuthLayout(33차, US-B01): `LoginPage` → `PublicAuthLayout` — 공개 인증 화면 단일 h1·skip·브랜드 일관.
- [x] 목록 CSS 갭(33차): `.ds-list`/`.ds-list__item`/`.ds-breadcrumb`/`.ds-form-grid` — Must 페이지 참조 클래스 `components.css` 정의.
- [x] 이용자 상세 탭(34차, US-D03): `ClientDetailPage` — `Tabs`/`TabPanel` 기본·건강·출석·청구, breadcrumb·요약 헤더.
- [x] 주민번호 열람(34차, US-D04): `MaskedRevealField` — 마스킹·`aria-label`·열람 버튼 `aria-label="주민번호 열람 (audit 기록됨)"`.
- [x] 보호자 초대 모달(34차, US-J01): `GuardianInviteModal` — `Modal`+`Field`+`aria-busy`, `ClientDetailPage`에서 사용.
- [x] 이용자 검색·페이지네이션(34차, US-D02): `ClientListPage` — `SearchInput hideLabel`+클라이언트 `Pagination`.
- [x] 대시보드 위젯(34차, US-M02): `DashboardWidgetGrid` — `StatCard` 5블록·링크 `sr-only`·로딩 `role=status`.
- [x] 청구 상태 필터(34차, US-G07): `BillingPage` — `FilterChips` counts+`MonthInput`.
- [x] NHIS import(34차, US-G04): `NhisImportGuidePanel` 4단계+Chrome/Edge 안내·`FileUpload` role=button+키보드.
- [x] 건강 비정상(34차, US-F01): `HealthAbnormalBanner` — `Badge` 「주의」+`role=alert`+항목 목록.
- [x] 세션 만료(34차, US-B03): `SessionTimeoutProvider` 30분 idle+60초 `SessionTimeoutModal`, `App.jsx` 배선.
- [x] Switch 회귀(34차, US-I03): `Switch.test.jsx` 5건 — ARIA·키보드·disabled·description.
- [x] 페이지 오류 Alert(34차): Must 페이지 redundant `role=alert` 제거 → `Alert tone=danger`+`.ds-page-alert` (tone 기본 role 사용).
- [x] 건강 알림 목록(35차, US-M02): `HealthAlertList` — Badge 「주의」+이름+사유, `aria-label` list. `DashboardPage` 연동.
- [x] 보호자 목록 카드(35차, US-D01/K01): `GuardianListCard` — `MaskedPhone`·대표 Badge·초대 `aria-label`. `ClientDetailPage` 연동.
- [x] 등급 이력(35차, US-M01): `GradeHistoryTimeline` — `<ol aria-label>`+sr-only 등급 변경. `ClientDetailPage` 「등급 이력」탭.
- [x] NHIS 배치 진행(35차, US-G04): `BatchProgressSteps` — `nav`+sr-only 단계·FAILED 표시. `NHISImportPage` 배치 행.
- [x] 본인부담 구분(35차, US-D01): `CopayTypeSelect` — 4구분+비율 help·`Field` 라벨. `COPAY_TYPES` export.
- [x] SideNav v1.2 메뉴(35차, US-UX-02): `navConfig` — 지점·보호자·수기 체크인·출석 통계·QR·입금·미납·수가표·copay 하위 route.
- [x] Card 섹션 제목(35차): `Card` `titleId` prop → `h2#id` for `aria-labelledby` 연결.
- [x] 수기 귀가 처리(38차, US-E01): `CheckoutModal` — `Modal`(role=dialog·focus trap), 귀가 교통편 `Field`+`Select`, 미선택 시 「귀가 확인」`disabled`, 실패 `Alert tone=danger`. `AttendancePage` 「귀가」행 액션.
- [x] 수기 결석 처리(38차, US-E01): `AttendanceAbsentModal` — 결석 사유 `Field`+`Textarea` 필수, 빈 값 제출 시 `Field error`(role=alert)+`aria-invalid` 차단.
- [x] 수기 체크인 표·요약(38차, US-E01·E02): `AttendancePage` — `Table`(`caption`·`scope=col`) 행 액션 버튼 `aria-label`에 이용자명 포함, 처리 중 `aria-busy`, 당일 요약 `StatCard`(입소·귀가 완료·결석·미처리), 상태 `StatusBadge`+텍스트(미처리/완료 텍스트 라벨).
- [x] UNMATCHED 후보 이용자 검색(43차, US-G06): `ReconciliationPage` 수동 매칭 폼 — 미매칭 행 선택 시 `SearchInput`(라벨 「후보 이용자 검색」·`type=search`) 노출, 250ms 디바운스 후 `fetchNhisMatchCandidatesApi({ q })` 재조회(이름·인정번호). 검색 결과에 현재 선택 이용자가 있으면 선택 유지, 0건 시 `role="status"` 안내. 행/이용자 미선택 시 검색·후보 `Select`·「수동 연결」 `Button` `disabled`(색만 의존 금지). `ReconciliationPage.test.jsx` 회귀.
- [x] DISCREPANCY 청구 라인 비교(42차, US-G06): `NhisReconciliationTable` `onCompare` → DISCREPANCY 행 「비교」`Button`(행별 `aria-label` 이용자명 포함, 다중 행 SR 식별)·그 외 행 `—`. `DiscrepancyComparePanel`(`Modal` role=dialog·focus trap) — 공단(NHIS)/ogada 청구 비교 표 `caption`·`th[scope=col]`·항목 `th[scope=row]`, 차이는 색(`ds-diff-amount`) + 「공단 초과/부족」 Badge **텍스트 병행**(색만 의존 금지), 동일 시 「동일」, `claimHref` 시 청구 라인 상세 `.ds-link`. `onCompare` 미제공 시 액션 열 미노출(기존 호출부 하위 호환).
- [x] 낙상·특이사항 이벤트 기록(41차, US-F03): `IncidentRecordForm` — 이벤트 유형 `Select`·내용 `Textarea` **필수**(빈 값 제출 시 `Field error`(role=alert)+`aria-invalid` 차단), 발생 시각 `type=time`(선택). 유형은 `INCIDENT_TYPES` 코드+텍스트 라벨 병행(색만 의존 금지). `HealthPage` 「낙상·특이사항」탭. payload `incidentType`·`description`·`occurredAt`/`recordedAt` KST ISO(`buildIncidentApiPayload`). 대시보드 「건강 이상」목록 반영은 `incident` recordType 파싱 후 coder가 `HealthAlertList` 연동(US-F03 2번 인수 조건).
- [x] 활력징후 비정상 범위 입력 경고(40차, US-F01): `VitalsRecordForm` — 수축기 혈압·체온·혈당·SpO₂ 입력 값이 `VITALS_RANGES` 정상 범위를 벗어나면 `Field warning`(`role="status"` polite·`aria-describedby` 연결)로 **텍스트 경고 + `--color-warning-text` 색 병행**(색만 의존 금지). advisory 경고이므로 `aria-invalid`는 설정하지 않고 저장은 차단하지 않음(요양보호사가 의도적 비정상 수치 기록 가능). 임계값은 `utils/vitalsRanges.js` 단일 원천(`HealthPage` 건강 이상 감지와 공유).

---

## 7. UI 컴포넌트 가이드 (coder 구현 메모) [UXD]

import: `import { Button, Card, Field, Modal, Pagination } from "../components/ui";`

### 7-1. 기존 컴포넌트

> **34차 baseline 현황 (2026-06-07)**: `components/ui/` **40종** — 34차 35종 + 35차 `HealthAlertList`·`GuardianListCard`·`GradeHistoryTimeline`·`BatchProgressSteps`·`CopayTypeSelect`. SideNav `navConfig.js` v1.2 P0 메뉴(지점·보호자·입금·미납·수가표 등) 반영. `npm test` **78/27 PASS**·build **99 modules**.
> **34차 baseline 현황 (2026-06-07)**: `components/ui/` **35종** — 33차 27종 + 34차 `SessionTimeoutModal`·`SessionTimeoutProvider`·`MaskedRevealField`·`GuardianInviteModal`·`FileUpload`·`NhisImportGuidePanel`·`HealthAbnormalBanner`·`DashboardWidgetGrid`. Must 페이지(`ClientDetailPage`·`ClientListPage`·`DashboardPage`·`BillingPage`·`NHISImportPage`·`HealthPage`) DS 컴포넌트 연동 완료.
> **33차 baseline 현황 (2026-06-07)**: `components/ui/` **27종** — 32차 18종 + 33차 `StatCard`·`SearchInput`·`FilterChips`·`Pagination`·`Table`·`Tabs`·`TabPanel`·`BranchSwitcher`·`LogoutButton`. 레이아웃: `layout/AppShell.jsx`(SideNav·BranchSwitcher·LogoutButton 통합)·`layout/SideNav.jsx`(US-UX-02 2단)·`layout/navConfig.js`. 아래 표 ⏳ COD 항목 중 도메인 특화(차트·모달·NHIS 등)는 coder가 페이지 연동 시 재사용.

| 컴포넌트 | 주요 props | 용도 / 화면 | baseline |
|----------|-----------|------------|---------|
| `Button` | `variant(primary/secondary/danger/ghost)`, `size(sm/md/lg)`, `block` | 전 화면 액션 | ✅ 29차 |
| `Field` | `label`, `required`, `help`, `error`, `children(render prop)` | 폼 라벨·오류 접근성 래퍼 (이용자 등록 §US-D01) | ✅ 29차 |
| `TextInput`/`Textarea`/`Select` | 네이티브 props 패스스루 | Field 안에서 사용 | ✅ 29차 |
| `Checkbox` | `label`, `checked`, `onChange` | **주민번호 수집 동의**(US-D04) 등 | ✅ 29차 |
| `Card` / `StatCard` | `title`,`actions` / `label`,`value`,`unit`,`tone?` | 카드 · 대시보드 지표(US-H01) | Card ✅ 29차 / StatCard ✅ 33차 |
| `Badge` / `StatusBadge` | `tone` / `status`,`map` | 청구·매칭·출석 상태 (`BILLING_STATUS`·`MATCH_STATUS`·`ATTENDANCE_STATUS`·`BATCH_STATUS`·`INVITATION_STATUS`) | ✅ 29차 |
| `LifecycleWorkflowPanel` | `title`,`description`,`steps[]`,`warning?` | 선임 업무수행일지·정기 욕구사정·급여계약 lifecycle 공통 패널(G34·US-T09·US-T10). 단계별 상태·기한·담당·서명·증빙 텍스트 노출 | ✅ 85차 |
| `Alert` | `tone`, `title` | 안내·경고(예: 롱텀 Chrome/Edge 안내 US-G04) | ✅ 29차 |
| `Modal` | `isOpen`,`onClose`,`title`,`size`,`footer`,`closeOnOverlay/Escape`,`showCloseButton` | 다이얼로그 — `useId()` 인스턴스별 고유 `aria-labelledby`, 포커스 트랩, ESC | ✅ 29차 |
| `Spinner` / `EmptyState` | — | 로딩·빈 목록 | ✅ 29차 |
| `ThemeToggle` | `className?` | 라이트/다크 전환 (다크모드 §2-4) | ✅ 29차 |
| `Tabs` / `TabPanel` | `tabs`,`activeId`,`onChange` | 이용자 상세 탭(기본/건강/출석/청구 US-D03) | ✅ 33차 |
| `Table` | `caption`, children + 행 강조 `ds-row--warning/danger` | 청구 목록·NHIS reconciliation 행(US-G06) | ✅ 33차 |
| `BranchSwitcher` | `branches`,`value`,`onChange` | 지점 전환(US-B02, `active_branch_id`) | ✅ 33차 |
| `SearchInput` | `value`,`onChange`,`label`,`hideLabel` | 이용자 목록 검색 (US-D02) | ✅ 33차 |
| `FilterChips` | `options`,`value`,`onChange`,`counts` | 청구 상태 필터 (US-G07) | ✅ 33차 |
| `Pagination` | `page`,`totalPages`,`onChange` | 목록 페이지 이동 | ✅ 33차 |
| `LogoutButton` | (없음 — `useAuth` 내부) | topbar 로그아웃 (US-B03) | ✅ 33차 |
| `AppShell` | `title`,`branches?`,`activeBranchId?`,`onBranchChange?` | 로그인 이후 공통 레이아웃 + SideNav + skip link | ✅ 33차 (`layout/AppShell.jsx`) |
| `SideNav` | `role` | 2단 그룹 네비 (US-UX-02) | ✅ 33차 (`layout/SideNav.jsx`) |

### 7-2. 신규·보강 컴포넌트 (2026-06-06)

| 컴포넌트 | 주요 props | 용도 / 화면 |
|----------|-----------|------------|
| `Modal` | `isOpen`,`onClose`,`title`,`size(sm/md/lg)`,`footer` | 확인 다이얼로그, NHIS 수동 매칭(US-G06), 고객사 등록(US-A01). **`useId()`로 인스턴스별 고유 `aria-labelledby` ID 생성** |
| `Pagination` | `page`,`totalPages`,`onChange` | 이용자·청구서 목록 페이지 이동(US-D02, US-G07) |
| `FileUpload` | `accept`,`label`,`help`,`onChange`,`error` | NHIS 엑셀 업로드(US-G04) |
| `EmptyState` | `title`,`description`,`action` | 빈 목록 안내 (모든 목록 화면) |
| `Spinner` / `LoadingOverlay` | `size(sm/md/lg)`,`label` | API 대기 상태 |
| `SideNav` | `role` | 역할별 사이드 네비게이션 자동 생성 |
| `FilterChips` | `options`,`value`,`onChange`,`label` | 청구 상태 필터 radiogroup (US-G07) |
| `SearchInput` | `value`,`onChange`,`label`,`placeholder` | 이용자 목록 검색 (US-D02) |
| `MaskedRevealField` | `maskedValue`,`revealed`,`onReveal`,`canReveal` | 주민번호 마스킹·열람 (US-D04) |
| `ClientPicker` | `candidates`,`value`,`onChange`,`onSearch` | NHIS 수동 매칭 이용자 선택 (US-G06) |
| `QrCodePanel` | `title`,`qrDataUrl`,`validUntil`,`onPrint` | 지점 QR 표시·인쇄 (US-E03) |
| `ToastProvider` / `useToast` | `success/warning/danger/info` | 저장·오류 피드백 (App 루트 감싸기) |
| `SessionTimeoutModal` | `isOpen`,`secondsLeft`,`onExtend`,`onLogout` | 30분 비활성 경고 (US-B03) |

### 7-3. 5차 보강 컴포넌트 (2026-06-06)

| 컴포넌트 | 주요 props | 용도 / 화면 |
|----------|-----------|------------|
| `GuardianListCard` | `guardians[]`,`canInvite` | 이용자 상세 기본정보 탭 — 연결 보호자 목록 표시(US-D01) + 초대 발송 스텁(US-J01, v1.1 disabled). `aria-labelledby` 섹션 제목, 전화번호 `tel:` 링크 |

### 7-4. 6차 보강 컴포넌트 (2026-06-06, v1.2 P0)

| 컴포넌트 | 주요 props | 용도 / 화면 |
|----------|-----------|------------|
| `GradeHistoryTimeline` | `entries[]`,`emptyMessage` | 이용자 상세 **등급 이력** 탭 (US-M01). `{ changedAt, previousGrade, newGrade, reason? }` |
| `DashboardWidgetGrid` | `widgets[]`,`ariaLabel` | 대시보드 실데이터 위젯 3블록+ (US-M02). `href`·`loading`·`badge` 지원 |
| `MaskedPhone` | `phone`,`masked` | 보호자·미납 목록 연락처 부분 마스킹 + `tel:` (US-K01, US-L02) |
| `GuardianClientLinks` | `clients[]`,`canEdit`,`onSetPrimary` | 보호자 상세 연결 이용자·대표 `Switch` 지정 (US-K02). `LinkedClientsCard` 명칭 → 59차 `GuardianClientLinks`로 구현 |
| `OverdueSummaryBar` | `count`,`totalAmount` | 미납 관리 요약 StatCard 2종 (US-L02) |
| `BillingContextNav` | `className?` | 입금↔미납 페이지 상단 컨텍스트 `nav`(US-L01·L02). `NavLink` `aria-current` |
| `SideNav` (2단) | `role` | **US-UX-02** — 운영·출석·기록·청구 그룹, `NAV_CONFIG` 그룹 구조 |

### 7-5. 7차 보강 컴포넌트 (2026-06-06, 누락·접근성)

| 컴포넌트 | 주요 props | 용도 / 화면 |
|----------|-----------|------------|
| `ClaimStatusTimeline` | `entries[]` | 청구서 상세 상태 전이 이력 (US-G07). `{ fromStatus?, toStatus, changedAt, changedBy? }` |
| `GuardianInviteModal` | `isOpen`,`form`,`onChange`,`onSubmit` | 보호자 초대 발송 폼 (US-J01). `ClientDetailPage`에서 사용 |
| `ClientPhotoField` | `photoUrl`,`altText`,`onPhotoChange`,`onAltChange` | 이용자 등록 사진+alt (US-D01). `ClientFormPage` |
| `AttendanceAbsentModal` | `client`,`reason`,`onConfirm` | 수기 출석 결석 사유 입력 (US-E01). `AttendancePage` |

### 7-6. 8차 보강 컴포넌트 (2026-06-06, FLOWCHART·USER_STORIES 갭)

| 컴포넌트 | 주요 props | 용도 / 화면 |
|----------|-----------|------------|
| `CheckoutModal` | `client`,`transport`,`onConfirm` | 귀가 교통편 선택 (US-E01). `AttendancePage` — 표 인라인 select 대체·모바일 권장 |
| `ClientSelector` | `clients[]`,`value`,`onChange`,`hideWhenSingle` | 복수 이용자 radiogroup (US-E04, US-J02). `GuardianPage`·`GuardianCheckinPage` |
| `CopayTypeSelect` | `value`,`onChange`,`error` | 본인부담 구분 4종+비율 help (US-D01). `ClientFormPage` |
| `DiscrepancyComparePanel` | `data{ nhis, ogada, diff }` | NHIS vs ogada 청구 비교 (US-G06). `ReconciliationPage` 모달 내부 |
| `GuardianBillingDetailModal` | `statement`,`isOpen` | 보호자 명세 상세·인쇄 (US-J02 v1.1). `GuardianPage` billing 탭 |
| `QrScanPanel` | `token`,`onTokenChange`,`onStartScan` | QR 카메라 placeholder + 수동 토큰 (US-E04). `GuardianCheckinPage` |

### 7-7. 9차 보강 컴포넌트 (2026-06-06, US-F02·US-B03·페이지 통합)

| 컴포넌트 | 주요 props | 용도 / 화면 |
|----------|-----------|------------|
| `MedicationDuplicateAlert` | `visible`,`duplicates[]`,`onDismiss` | 동일 시각 투약 중복 경고 (US-F02). `findMedicationDuplicates()` 헬퍼 export |
| `HealthAbnormalBanner` | `abnormalFields[]` | 건강 수치 비정상 요약 — Badge+값 목록 (US-F01). `HealthPage` |
| `SessionTimeoutProvider` | (children) | 30분 idle + 60초 경고 (US-B03). `App.jsx` AuthProvider 하위 |

### 7-7c. 11차 보강 컴포넌트 (2026-06-06, 다크 모드)

| 컴포넌트 | 주요 props | 용도 / 화면 |
|----------|-----------|------------|
| `ThemeToggle` | `className?` | 라이트/다크 전환 버튼. `aria-pressed` + 아이콘(`aria-hidden`)+텍스트 라벨 병행, 44px. `AppShell` topbar에 기본 탑재 — 전 화면 우상단 노출 |

> **테마 동작**: `src/theme.js`가 단일 진실 원천. 최초값 = **저장된 사용자 선택 > OS `prefers-color-scheme`**(기본 라이트). 명시 선택 전에는 OS 변경을 추종한다. `main.jsx`가 `import "./theme"`로 시작 시 적용(FOUC 최소화). 저장은 `localStorage["ogada-theme"]` — **비민감 UI 설정만**(JWT 등 민감정보는 메모리 세션, SEC-005).

### 7-7d. 13차 보강 컴포넌트 (2026-06-06, 전사 설정 토글)

| 컴포넌트 | 주요 props | 용도 / 화면 |
|----------|-----------|------------|
| `Switch` | `label`,`checked`,`onChange(next)`,`description?`,`onLabel?`,`offLabel?`,`disabled?` | 설정 on/off 토글 (WAI-ARIA `switch`). `SettingsPage` `allow_client_self_checkin`(US-I03·§3-3). **Checkbox(동의·선택)와 구분** — 즉시 적용되는 설정값에 사용 |

> **Switch vs Checkbox**: `Checkbox`는 폼 제출 시 반영되는 **동의/선택**(예: 주민번호 수집 동의 US-D04)에, `Switch`는 즉시 적용되는 **on/off 설정**(예: 전사 셀프 체크인 허용)에 쓴다. `Switch`는 `onChange`가 **다음 boolean 값**을 인자로 받는다(이벤트 객체 아님).

### 7-7h. 17차 보강 컴포넌트 (2026-06-07, Settings·비밀번호·상태 카운트)

| 컴포넌트 | 주요 props | 용도 / 화면 |
|----------|-----------|------------|
| `AuditLogPanel` | `entries[]`, `loading`, `eventFilter`, `onEventFilterChange`, `dateFrom/To`, `page`, `totalPages` | sysadmin 감사 로그 (US-I03). `AUDIT_EVENT_TYPES` 상수 export |
| `BackupSettingsPanel` | `autoBackupEnabled`, `onAutoBackupChange`, `lastBackupAt`, `lastBackupStatus`, `retentionDays`, `onManualBackup` | Tenant 백업 설정 (US-I03). `SettingsPage` backup 탭 |
| `PasswordChangeModal` | `isOpen`, `required`, `onSubmit({ newPassword })`, `loading`, `error` | 최초 로그인·비밀번호 변경 (US-A02). `LoginPage` + `AuthContext.mustChangePassword` |

> **FilterChips counts (US-G07)**: `counts={{ __all__: 12, DRAFT: 3, ... }}` — API `statusCounts` 응답을 `BillingPage`에서 매핑. **Modal 필수 모드**: `closeOnOverlay={false}`·`closeOnEscape={false}`·`showCloseButton={false}` — `PasswordChangeModal required` 패턴.

### 7-7k. 21차 보강 컴포넌트 (2026-06-07, 수가표·청구 상세·StatCard·텍스트 유틸)

| 컴포넌트 | 주요 props | 용도 / 화면 |
|----------|-----------|------------|
| `FeeScheduleTable` | `rows[]`, `onRowChange(grade, field, value)`, `disabled?` | 등급별 1일 수가 편집 (US-G00a). `FeeSchedulePage` — `CopayRateTable`과 동일 접근성 패턴 |
| `StatCard` (확장) | `tone?: 'default' \| 'danger'` | 미납 총액 등 위험 지표 강조 (US-L02). 라벨 텍스트 병행 — 색만 의존 금지 |

> **BillingDetailPage 상태 전이 (21차)**: topbar 「확정」/「수납완료」→ `BillingStatusConfirmModal` → `PATCH /billing/claims/:id/status`. `BillingPage`와 동일 UX.

> **텍스트 유틸 (21차)**: `.ds-text-secondary`·`.ds-text-muted`·`.ds-mono`·`.ds-diff-amount`·`.ds-table-actions`·`.ds-section-gap`·`.ds-table-empty` — 인라인 `style={{ color }}` 금지, `forced-colors` 대응 포함.

### 7-7l. 22차 보강 컴포넌트 (2026-06-07, MonthInput·입금·reconciliation 요약)

| 컴포넌트 | 주요 props | 용도 / 화면 |
|----------|-----------|------------|
| `MonthInput` | native `type=month` props | 대상 월 선택 (US-E05·US-G04). `Field` 안에서 `TextInput` 래퍼 — `.ds-month-input` max-width |
| `PaymentRecordModal` | `isOpen`, `claim`, `form`, `onFormChange(patch)`, `onSubmit`, `error` | 본인부담 입금 기록 (US-L01). `PAYMENT_METHODS` export. `PaymentPage` |
| `ReconciliationSummaryBar` | `batchId`, `branchName`, `targetMonth`, `batchStatus`, `stats` | NHIS 배치 매칭 요약 (US-G06). Badge+sr-only 건수. `ReconciliationPage` |

> **MonthInput (22차)**: `AttendanceStatsPage`·`NHISImportPage`의 raw `<input type=month class=ds-input>` 제거. coder 신규 월 필터도 `MonthInput`+`Field` 패턴 준수.
>
> **PaymentRecordModal (22차)**: `PaymentPage` 인라인 Modal 폼 → 컴포넌트 추출. API: `POST /billing/claims/:id/payments { paidAt, amount, method }`.

### 7-7j. 20차 보강 컴포넌트 (2026-06-07, 청구 확인·NHIS 가이드·copay·보호자 요약)

| 컴포넌트 | 주요 props | 용도 / 화면 |
|----------|-----------|------------|
| `BillingStatusConfirmModal` | `isOpen`, `onClose`, `claim`, `nextStatus`, `onConfirm`, `loading`, `error` | 청구 상태 전이 확인 (US-G07). `BILLING_STATUS_TRANSITIONS` export. `BillingPage`·`BillingDetailPage`(후속) |
| `NhisImportGuidePanel` | `className?` | 공단 엑셀 import 4단계 온보딩 + Chrome/Edge 안내 (US-G04). `NHISImportPage` |
| `CopayRateTable` | `rates[]`, `onRateChange(code, rate)`, `disabled?` | 본인부담 구분별 비율 편집 (US-G00b). `CopayRatePage` |
| `HealthAlertList` | `items[]`, `emptyMessage?`, `ariaLabel?` | 건강 이상 알림 — Badge 「주의」+이름+사유 (US-F01/H01/I02). `DashboardPage`·`GuardianDailySummary` |
| `GuardianDailySummary` | `dailyRecord`, `loading?`, `clientName?` | 보호자 포털 오늘 출석·건강·식사 지표 (US-I02·FLOWCHART §9). `GuardianPage` 일일 기록 탭 |

> **BillingPage 상태 전이 (20차)**: 목록 「확정」/「수납완료」 클릭 → `BillingStatusConfirmModal` → 확인 시 `PATCH /billing/claims/:id/status`. 즉시 PATCH 금지 — 되돌릴 수 없음(US-G07 V8) UX 보장.

### 7-7i. 18차 보강 컴포넌트 (2026-06-07, 인증·로그인 이력·오류 Alert 통일)

| 컴포넌트 | 주요 props | 용도 / 화면 |
|----------|-----------|------------|
| `LoginHistoryPanel` | `entries[]`, `loading`, `roleFilter`, `dateFrom/To`, `page`, `totalPages` | sysadmin 로그인 이력 (REQUIREMENTS §3-1). `LOGIN_RESULT_STATUS` export. `SettingsPage` login-history 탭 |
| `PasswordResetRequestModal` | `isOpen`, `onClose`, `onSubmit(email)`, `loading`, `error`, `submitted` | 비밀번호 재설정 요청 (§3-1). `LoginPage` 「재설정 요청」 |

> **페이지 오류 패턴 (18차)**: `{error && <Alert tone="danger" className="ds-page-alert">{error}</Alert>}`. raw `style={{ color: danger-text }}` + `<p role=alert>` **금지** — 고대비·다크에서 배경 틴트·경계선 일관.

### 7-7g. 16차 보강 컴포넌트 (2026-06-07, NHIS 배치 진행·플랫폼 고객사)

| 컴포넌트 | 주요 props | 용도 / 화면 |
|----------|-----------|------------|
| `BatchProgressSteps` | `status`(PENDING/PROCESSING/COMPLETED/FAILED), `ariaLabel?` | NHIS import 배치 처리 단계 (US-G04). `ReconciliationPage`·`NHISImportPage` |
| `PlatformOrgDetailModal` | `isOpen`,`onClose`,`org`,`onIssueAdmin(email)`,`issuing?`,`issueError?` | platform_admin 고객사 상세 + hq_admin 발급 (US-A02). `PlatformPage` |

### 7-7o. 27차 보강 컴포넌트 (2026-06-08, DateInput·초대 이력)

| 컴포넌트 | 주요 props | 용도 / 화면 |
|----------|-----------|------------|
| `DateInput` | native `type=date` props | 날짜 입력·기간 필터 (US-D01·US-L01·§3-1). `Field` 안 `TextInput` 래퍼 — `.ds-date-input`. `ClientFormPage`·`PaymentRecordModal`·`AuditLogPanel`·`LoginHistoryPanel` |
| `GuardianInvitationList` | `invitations[]`, `canManage`, `onResend`, `onRevoke`, `busyId` | 보호자 초대 이력·상태·재발송/취소 (US-J01). `GuardianListCard`·`ClientDetailPage` |

> **`GuardianListCard` 확장 (27차)**: `invitations` prop + 「초대 이력」하위 `GuardianInvitationList`. API: `GET /clients/:id` 응답 `guardianInvitations[]` — `{ id, guardianName, email?, phone?, status, expiresAt? }`. 재발송 `POST /guardian/invitations/{id}/resend`, 취소 `DELETE /guardian/invitations/{id}` (coder J01).
>
> **DateInput (27·28차)**: `MonthInput`과 동일 패턴. 신규 `type=date`는 **`DateInput`+`Field`만** 허용 — raw `<input class=ds-input type=date>` **금지**. 대상: 이용자 등록(생년월일·인정유효일)·입금일·감사/로그인 이력 기간 필터.

### 7-7n. 26차 보강 컴포넌트 (2026-06-08, US-J01 수락 UI)

| 컴포넌트 | 주요 props | 용도 / 화면 |
|----------|-----------|------------|
| `PublicAuthLayout` | `title`, `subtitle?`, `wide?`, `footer?` | 미인증 공개 인증 화면 레이아웃 (US-B01·US-J01). LoginPage `.ds-login` 카드 패턴 — **AppShell/SideNav 사용 금지** |
| `GuardianInvitationAcceptForm` | `form`, `onChange`, `onSubmit`, `onGoLogin`, `isSubmitting?`, `error?`, `success?`, `disabled?` | 보호자 초대 수락 폼 (US-J01). `/guardian/invitations/:token/accept` |

> **`INVITATION_STATUS` (26차)**: `Badge.jsx` export — 초대 목록·상세(향후 ClientDetailPage)에서 `StatusBadge status map={INVITATION_STATUS}` 사용.
>
> **GuardianInvitationAcceptPage 마이그레이션 (COD)**: 현재 WIP 페이지는 AppShell+SideNav — 아래 패턴으로 교체:
> ```jsx
> <PublicAuthLayout title="보호자 초대 수락" subtitle="센터에서 보낸 초대 링크로 계정을 활성화합니다." wide>
>   <GuardianInvitationAcceptForm form={form} onChange={setField} onSubmit={handleSubmit} onGoLogin={() => navigate("/")} ... />
> </PublicAuthLayout>
> ```

### 7-7m. 25차 보강 컴포넌트 (2026-06-08, MonthInput 잔여·로그아웃·차트 범례)

| 컴포넌트 | 주요 props | 용도 / 화면 |
|----------|-----------|------------|
| `LogoutButton` | (없음 — `useAuth` 내부) | AppShell topbar 공통 로그아웃 (US-B03). `aria-label="{이름} 로그아웃"`, `Button secondary size=sm` |

> **ChartContainer 확장 (25차)**: `axisTextColor` prop → viewport `--chart-axis-text` CSS 변수. 범례 라벨은 `.ds-chart__legend-label` 클래스 사용(인라인 `style={{ color }}` 금지).
>
> **MonthInput 잔여 (25차)**: `BillingPage` 조회 월 필터 — 22차 `AttendanceStatsPage`·`NHISImportPage`와 동일 패턴. `.ds-input--month` deprecated → `.ds-month-input`만 사용.

### 7-7f. 15차 보강 컴포넌트 (2026-06-07, Recharts 접근성 차트)

| 컴포넌트 | 주요 props | 용도 / 화면 |
|----------|-----------|------------|
| `ChartContainer` | `title`, `description?`, `height?`, `axisTextColor?`, `empty?`, `emptyMessage?`, `children` | Recharts 공통 래퍼 — `role="figure"`+`figcaption`+sr-only 요약 |
| `AttendanceRateChart` | `data[{label,rate}]`, `variant(line\|bar)`, `title?` | 월별 출석률 추이(US-H01 `DashboardPage`), 일자별 막대(US-E05 `AttendanceStatsPage`) |
| `HealthTrendChart` | `data[{date,systolic,diastolic,temperature,bloodSugar,spo2}]`, `metrics?` | 이용자 건강 추이 다중 라인(US-F04 `HealthDetailPage`) |
| `BranchCompareChart` | `branches[{branchName,attendanceRate,clientCount?}]` | HQ 지점별 출석률 비교 막대(US-H02 `DashboardPage` hq) |

> **의존성**: `recharts@^2.15` (package.json). 색상은 `useChartColors()` 훅으로 라이트/다크 자동 전환 — coder는 raw hex 금지.

### 7-7e. 14차 보강 컴포넌트 (2026-06-07, 수가 이력·Recharts 토큰)

| 컴포넌트 | 주요 props | 용도 / 화면 |
|----------|-----------|------------|
| `FeeRateHistoryPanel` | `entries[]`, `title?`, `emptyMessage?` | 수가 변경 이력 표시 (US-G00a). `{ year, grade, dailyRate, effectiveFrom, createdAt, createdByName? }`. `FeeSchedulePage` 「이력 보기」 모달 내부 |

> **Recharts 통합 (UXD-1 해소)**: 차트 색상은 `src/styles/chartColors.js`의 `CHART_COLORS`·`useChartColors()` 훅으로 주입. 다크 모드 대응은 `useChartColors()` 훅이 `html[data-theme]`를 읽어 팔레트 전환. `tokens.css`의 `--chart-color-*` 토큰과 1:1 동기화.

### 7-7b. 10차 보강 컴포넌트 (2026-06-06, US-D01 잔여 갭)

| 컴포넌트 | 주요 props | 용도 / 화면 |
|----------|-----------|------------|
| `ClientUserAccountField` | `enabled`,`onEnabledChange`,`loginId`,`onLoginIdChange`,`allowSelfCheckin`,`error` | 이용자 등록 시 **이용자 본인(`client_user`) 계정 발급·연결** (US-D01 선택, FLOWCHART §4 J). 토글 체크 시 로그인 이메일 `Field` 노출, `allow_client_self_checkin` off면 QR 셀프 비활성 `Alert` 안내. `ClientFormPage` |

> **CopayTypeSelect 실적용**: `ClientFormPage`의 본인부담 구분 입력을 raw `<Select>`에서 `CopayTypeSelect`로 교체 완료(§7-9 인계 메모 이행). 구분별 비율 help 텍스트·`aria-invalid`가 자동 적용된다.

### 7-7s. 47차 보강 컴포넌트 (2026-06-08, v3 직원·v1.3 배차 unconfirm)

| 컴포넌트 | 주요 props | 용도 / 화면 |
|----------|-----------|------------|
| `StaffRoleSelect` | native `Select` props | 직원 등록 역할 선택 (v3 §3-8). `STAFF_ASSIGNABLE_ROLES` 한국어 라벨. `StaffPage` |
| `TransportUnconfirmModal` | `isOpen`,`onClose`,`onConfirm`,`runDate?`,`stopCount?`,`confirming?`,`error?` | 배차 확정 취소 확인 (US-T02, v1.3-A). `hq_admin` only. `TransportRunDetailPage` |

> **`config/staff.js` (47차)**: `STAFF_ASSIGNABLE_ROLES`·`staffRoleLabel(role)` — 직원 목록·폼 공통. coder는 백엔드 허용 역할과 정합 확인.
>
> **Transport unconfirm (47차, US-T02)**: `POST /api/v1/transport/runs/{id}/unconfirm` → `unconfirmTransportRunApi`. 성공 시 `status=DRAFT`·정차 순서 재편집 가능·직원 목록에서 숨김. `TransportRunDetailPage` 확정 루트에만 「확정 취소」노출.

### 7-7r. 38차 보강 컴포넌트 (2026-06-07, 수기 출석 체크인/아웃·결석)

| 컴포넌트 | 주요 props | 용도 / 화면 |
|----------|-----------|------------|
| `CheckoutModal` | `isOpen`,`client`,`onClose`,`onConfirm({ transportMethod })`,`loading?`,`error?` | 귀가(체크아웃) 교통편 선택 (US-E01). `TRANSPORT_METHODS` export. `AttendancePage` 「귀가」 |
| `AttendanceAbsentModal` | `isOpen`,`client`,`onClose`,`onConfirm({ reason })`,`loading?`,`error?` | 결석 사유 입력 (US-E01). 사유 필수. `AttendancePage` 「결석」 |

> **AttendancePage 흐름 (38차, US-E01·E02)**: 당일 출석 목록을 `Table`로 표시하고, 상태에 따라 행 액션을 노출한다 — **미처리** → 「입소」(`checkInApi({ clientId, method:"manual" })`)·「결석」(`AttendanceAbsentModal` → `markAbsentApi({ clientId, reason })`), **입소(CHECKED_IN)** → 「귀가」(`CheckoutModal` → `checkOutApi({ clientId, transportMethod })`), **귀가/결석** → 「완료」 텍스트. 체크인/귀가/결석 시각은 백엔드가 자동 기록. 상단 `StatCard` 4종으로 당일 요약(US-E02). API 응답 스키마(`{ id, clientId, clientName, status }`)는 coder가 백엔드와 정합.
>
> **coder 인계 (38차)**: `markAbsentApi`(`POST /api/v1/attendance/absent { clientId, reason }`)는 `services.js`에 추가됨 — 백엔드 엔드포인트 구현·결석일수 청구 제외 로직 연동 필요. `checkInApi`·`checkOutApi`는 기존에 정의돼 있었으나 페이지에서 미사용이던 것을 38차에 연결.

### 7-7s. 41차 보강 컴포넌트 (2026-06-08, 낙상·특이사항 이벤트 기록)

| 컴포넌트 | 주요 props | 용도 / 화면 |
|----------|-----------|------------|
| `IncidentRecordForm` | `onSubmit(payload)`,`disabled?`,`className?` | 낙상·사고·특이사항 이벤트 기록 (US-F03). `INCIDENT_TYPES` 상수 export. `HealthPage` 「낙상·특이사항」탭 |

> **AttendancePage·HealthPage 흐름 (41차, US-F03)**: `HealthPage`는 일일 건강·투약·**낙상·특이사항**·이력 4탭. 「낙상·특이사항」탭의 `IncidentRecordForm`은 이벤트 유형(`INCIDENT_TYPES` — FALL/ACCIDENT/SYMPTOM/OTHER)·발생 시각(`type=time`, 선택)·내용(필수)을 받아 `buildIncidentApiPayload`로 `{ recordedAt, incidentType, description, occurredAt }`(KST ISO) 본문을 만든다. 발생 시각 미입력 시 `occurredAt = recordedAt`. 이력 탭은 `normalizeHealthResponse`의 `incidents[]`(recordType `incident`)를 `[유형] 내용` 형식으로 표시한다.
>
> **coder 인계 (41차)**: ① `createIncidentApi`(`POST /api/v1/clients/:id/health/incidents`)가 `services.js`에 추가됨 — 백엔드 엔드포인트(`HealthRecord` recordType `incident`) 구현 필요. **`incidentType` 코드값(FALL/ACCIDENT/SYMPTOM/OTHER)은 백엔드 enum과 정합** 후 `INCIDENT_TYPES`에 반영. ② **US-F03 2번 인수 조건(대시보드 「건강 이상」목록 반영)**: 낙상·사고 이벤트를 `GET /api/v1/dashboard/branch` 건강 알림 집계에 포함하고, `HealthAlertList` `items[]`(`{ clientName, reason }`)에 매핑. 현재 UI는 입력·이력 표시까지 — 대시보드 위젯 연동은 백엔드 집계 API 후 `DashboardPage`에서 coder가 배선.

### 7-7q. 32차 보강 컴포넌트 (2026-06-07, 공개 인증 레이아웃·Alert 정중도)

| 컴포넌트 | 주요 props | 용도 / 화면 |
|----------|-----------|------------|
| `PublicAuthLayout` | `title`(h1로 렌더), `subtitle?`, `wide?`, `children` | 미인증 공개 인증 화면 레이아웃 (US-B01·US-J01). LoginPage `.ds-login` 카드·브랜드 재사용 + skip link(`#public-auth-content`) + **페이지 h1**. **AppShell/SideNav 금지**. `GuardianInvitationAcceptPage` 적용 |

> **Alert 정중도 (32차)**: `Alert`의 기본 `role`은 이제 tone에서 파생된다 — `danger`/`warning`→`alert`(assertive), `info`/`success`/`neutral`→`status`(polite). 정적 안내(예: NHIS Chrome/Edge 가이드 info)가 스크린리더를 끊지 않는다. 긴급도를 직접 지정하려면 `role` prop으로 override(`<Alert tone="danger" role="status">`). 기존에 `role`을 명시하던 페이지는 동작 불변.
>
> **PublicAuthLayout (32차)**: 26차 §7-7n에 문서화됐으나 재이관 baseline에는 부재하던 컴포넌트를 실제 구현. 26차의 `GuardianInvitationAcceptForm`(별도 폼 컴포넌트)·`success`/`disabled`(만료 잠금) 패턴은 백엔드 J01 API live 연동 시점에 후속. 현재는 레이아웃(h1·skip·브랜드)만 우선 도입해 헤딩 계층 결함을 해소.

### 7-7p. 30차 보강 컴포넌트 (2026-06-07, 폼 입력·토글·연락처 마스킹)

| 컴포넌트 | 주요 props | 용도 / 화면 |
|----------|-----------|------------|
| `Switch` | `label`,`checked`,`onChange(next)`,`description?`,`onLabel?`,`offLabel?`,`disabled?`,`className?` | 즉시 적용 on/off 설정 (US-I03 — `allow_client_self_checkin` 등). WAI-ARIA `role="switch"` + `aria-checked` |
| `DateInput` | native `type=date` props 패스스루 | 날짜 입력·기간 필터 (US-D01·US-L01·§3-1). `Field` 안 `TextInput` 래퍼 — `.ds-date-input` |
| `MonthInput` | native `type=month` props 패스스루 | 대상 월 입력 (US-E05·US-G02/G04/G07). `Field` 안 `TextInput` 래퍼 — `.ds-month-input` |
| `MaskedPhone` | `phone`,`masked?`,`withLink?`,`className?` | 보호자·미납 목록 연락처 부분 마스킹 + `tel:` (US-K01·US-L02). `maskPhone(raw)` 헬퍼 export — 11자리 `010-****-5678`, 10자리 `02-***-5678` |

> **Switch vs Checkbox 재확인 (30차)**: `Checkbox`는 폼 제출 시 반영되는 **동의/선택**(US-D04 주민번호 수집 동의)에, `Switch`는 즉시 적용되는 **on/off 설정**(US-I03 셀프 체크인 허용)에 사용. `Switch.onChange`는 **다음 boolean 값**을 인자로 받는다(이벤트 객체 아님).
>
> **DateInput / MonthInput 사용 규칙 (30차)**: 신규 `type=date|month` 입력은 **`DateInput`/`MonthInput` + `Field`만** 허용 — raw `<input type="date" class="ds-input">` **금지**(접근성·다크/forced-colors 일관성·max-width 일관). 기존에 raw input을 사용한 페이지는 COD가 이 컴포넌트로 교체.
>
> **MaskedPhone PII (30차)**: 마스킹 결과는 시각 UI 기본값. `aria-label`은 마스킹된 값을 그대로 사용해 SR도 평문 노출 없음. `tel:` 링크의 href는 다이얼 가능한 raw digits(`01012345678`)로 — 모바일에서 「전화 걸기」를 트리거하기 위한 최소 노출이며, 백엔드는 이 컴포넌트에 가능한 한 **이미 마스킹된 값**을 전달해 클라이언트 메모리에 평문 잔류 시간을 줄인다(SEC).

```jsx
// 30차 사용 예시 — Switch (조직 설정)
<Switch
  label="이용자 본인 셀프 체크인 허용"
  description="QR 셀프 체크인 시 client_user 계정도 출석을 처리할 수 있습니다."
  checked={form.allowClientSelfCheckin}
  onChange={(next) => updateOrg({ allowClientSelfCheckin: next })}
/>
```

```jsx
// 30차 사용 예시 — DateInput / MonthInput / MaskedPhone
<Field label="생년월일" required error={err.birthdate}>
  {(p) => <DateInput {...p} value={form.birthdate} onChange={(e) => set({ birthdate: e.target.value })} />}
</Field>

<Field label="대상 월">
  {(p) => <MonthInput {...p} value={month} onChange={(e) => setMonth(e.target.value)} />}
</Field>

<MaskedPhone phone={guardian.phone} masked={guardian.phoneMasked} />
```

### 7-7aa. 77차 신규 컴포넌트 (2026-06-11, US-L04·G15·G16 오팅·케어프로비전·이동서비스 법정서식)

| 컴포넌트 | 주요 props | 용도 / 화면 |
|----------|-----------|------------|
| `MedicalExpenseDeductionPanel` | `clientId`,`clientName?`,`variant?("staff"\|"guardian")`,`className?` | 연말정산 의료비공제 본인부담 납입 집계 (US-L04 G26). 귀속 연도 조회·인쇄·CSV. `ClientDetailPage` 청구 탭(staff) / `GuardianPortalPage`(guardian) |
| `ClientOutingPanel` | `clientId`,`clientName?`,`className?` | 이용자별 외출 CRUD + 출발·복귀·취소 생애주기 (G15 BNK-63). `OUTING_STATUS` `StatusBadge`. `ClientDetailPage` 외출 탭 |
| `CareProvisionRecordPanel` | `clientId`,`className?` | 재가급여 기록 목록 — 방문요양/주간보호 분리 표 (G15/G16). `ClientDetailPage` 기본정보 탭 |
| `TransportVehicleSelect` | `branchId`,`value`,`onChange`,`disabled?`,`className?` | 지점 차량 `Select` (`GET /transport/vehicles?branchId=`). `TransportRunNewPage`·`TransportRunDetailPage` 차량 배정 |
| `TransportForm18GuidePanel` | `className?` | 별지 제18호 이동서비스비 신청 안내 — 절차·공단 3분리 신청 유형·등록상태 4단·전제조건 (G15 v1.3-C). `FeeSurchargeGuidePanel` 내 탭 |
| `TransportCompliancePanel` | `roster?`,`canSave?`,`className?` | 이동서비스 수칙 체크리스트(`Checkbox`·`aria-describedby`)·서명·계약서·일지 서식 (G15). `TransportRunDetailPage` 탭 |

> **Field aria-required (77차 WCAG 1.3.1·3.3.2)**: `Field`의 `required` prop이 하위 컨트롤에 `aria-required="true"` 전달 — HTML native `required` 대신 사용해 브라우저 기본 유효성 팝업 없이 보조 기술이 필수 입력을 인식. 기존 `aria-invalid` + `Field error` 패턴과 조합해 입력 전(aria-required) → 미입력 제출(aria-invalid + role=alert) 흐름을 완성.

> **MedicalExpenseDeductionPanel 접근성(77차, US-L04)**: 요약 `StatCard` 3종은 `role="group" aria-label="의료비공제 납입 요약"`으로 그룹. 납입 내역 `Table`은 `caption` sr-only(시각 h3 중복 방지). 합계 행(`ds-medical-expense-panel__total`)은 `th scope="row"`. 인쇄는 `window.print()`; 보호자 명세서 인쇄(`body.ds-statement-printing`)와 영역 충돌 없도록 `.ds-billing-report-print-zone` 스코프 클래스로 격리. CSV 다운로드 시 `aria-label` 명시.

> **ClientOutingPanel 생애주기(77차, G15 BNK-63)**: 행 액션 버튼(`출발`,`복귀`,`수정`,`취소`)에 이용자명 포함 `aria-label`(31·76차 패턴 정합). `OUTING_STATUS`: PLANNED→출발 버튼(`departClientOutingApi`) → `OUT`→복귀 버튼(`returnClientOutingApi`) → `RETURNED`. `CANCELLED`는 `PLANNED`/`OUT`에서만 가능. 행 `StatusBadge`는 색+텍스트 라벨 병행. `ClientOutingsPage`(`/transport/outings`)는 전 이용자 외출 목록·월 필터, `ClientOutingReportPage`(`/reports/client-outings`)는 월간 외출 리포트 인쇄용.

> **TransportCompliancePanel 접근성(77차, G15)**: 수칙 `Checkbox` 5종에 각 상세 설명 `<p id>`가 `aria-describedby`로 연결(WCAG 1.3.1 — 71차 패턴 재사용). 진행 현황은 `aria-live="polite"` `.ds-transport-compliance__progress` 텍스트(「N / 5 완료」). 계약서·일지는 `Modal`(focus trap) 내 `<pre>`.

### 7-8. 사용 예시

```jsx
// 이용자 등록 — 동의 없이는 저장 차단(US-D04)
<Field label="주민등록번호" required help="공단 청구 목적, 암호화 저장됩니다." error={err.ssn}>
  {(p) => <TextInput {...p} inputMode="numeric" placeholder="______-_______" />}
</Field>
<Checkbox label="주민등록번호 수집·이용에 동의합니다." checked={agree} onChange={...} />
<Button variant="primary" disabled={!agree}>저장</Button>
```

```jsx
// NHIS reconciliation 행 (US-G06)
<Table columns={["인정번호","이름","청구액","이용자","매칭상태"]} caption="공단 청구내역 매칭">
  {rows.map((r) => (
    <tr key={r.id} className={r.matchStatus === "DISCREPANCY" ? "ds-row--warning" : ""}>
      <td>{r.certNo}</td><td>{r.name}</td><td>{r.amount}</td><td>{r.clientName ?? "-"}</td>
      <td><StatusBadge status={r.matchStatus} map={MATCH_STATUS} /></td>
    </tr>
  ))}
</Table>
```

```jsx
// 수동 매칭 모달 (US-G06)
<Modal isOpen={open} onClose={onClose} title="이용자 수동 연결" size="md"
  footer={<><Button variant="secondary" onClick={onClose}>취소</Button><Button onClick={handleMatch}>연결</Button></>}
>
  <Select value={clientId} onChange={...}>...</Select>
  <Alert tone="warning" title="주의">동일 지점 이용자만 연결 가능합니다.</Alert>
</Modal>
```

```jsx
// AppShell + SideNav (로그인 후 전 화면)
<AppShell title="이용자 관리" nav={<SideNav role={user.role} />}
  topbarRight={<BranchSwitcher branches={...} value={activeBranch} onChange={...} />}
>
  {children}
</AppShell>
```

```jsx
// GuardianListCard — 이용자 상세 기본정보 탭 (US-D01, US-J01)
// client.guardians는 API GET /api/v1/clients/:id 응답에 포함되어야 함 (coder 담당)
<GuardianListCard
  guardians={client.guardians ?? []}
  canInvite={user?.role === "branch_admin" || user?.role === "hq_admin"}
/>
```

### 7-9. coder 인계 메모

- **지점 관리(US-C01)** — `BranchesPage`(`/branches`): 목록 표 + 등록/수정 `Modal`. 쓰기 액션은 hq_admin·branch_admin에 노출(백엔드가 최종 인가). API: `GET/POST /branches`, `PATCH /branches/{id}`(`isActive` 비활성). 상태는 `BRANCH_STATUS`.
- **월별 출석 통계(US-E05)** — `AttendanceStatsPage`(`/attendance/stats`): 대상 월(`<input type="month">`)·지점 필터 → `StatCard` 요약 + 일자별 출석률 `.ds-chart-placeholder` + 이용자별 출석 일수 표. API: `GET /attendance/stats/monthly?branchId=&yearMonth=`.
- **보호자 관리(US-K01~K02)** — `GuardiansPage`(`/guardians`), `GuardianDetailPage`(`/guardians/:id`). API: `GET /guardians`, `GET/PATCH/POST /guardians/:id/clients`. `MaskedPhone`·`LinkedClientsCard` 사용.
- **입금·미납(US-L01~L02)** — `PaymentPage`(`/billing/payments`), `OverduePage`(`/billing/overdue`). API: `POST /billing/claims/:id/payments`, `GET /billing/overdue`. CMS 제외(v2).
- **본인부담 대장·계산기(US-M03, G22)** — `BillingReportPage`(`/billing/reports/charges|deposits|receipts`) + `BillingLedgerTable`. API: `GET /api/v1/billing/reports/{variant}?month=&q=&page=` 응답 `{ items[], summary: { rowCount, totalAmount, totalCopay?, totalNhis? }, totalPages }`. **`CopayCalculatorPage`**(`/billing/calculator`) — 수가표·copay_rates 로드 후 `CopayCalculatorPanel` 클라이언트 계산(백엔드 불필요). 인쇄는 `@media print`로 필터·페이지네이션 숨김.
- **등급 이력(US-M01)** — `ClientDetailPage` 「등급 이력」탭. API: `GET /clients/:id` 응답에 `ltcGradeHistory: [{ changedAt, previousGrade, newGrade, reason? }]` 포함.
- **대시보드 실데이터(US-M02)** — `DashboardWidgetGrid` + `GET /api/v1/dashboard/branch|hq`. StatCard 데모 제거, 3블록: 출석·미납·건강/NHIS.
- **2단 SideNav(US-UX-02)** — `SideNav.jsx` `NAV_CONFIG` 그룹 구조. 청구 그룹에 **공단 엑셀 import**(`/billing/nhis-import`) 포함. 신규 route는 해당 그룹 `items`에 등록.
- **청구 상세(US-G02)** — `BillingDetailPage`(`/billing/:id`): `GET /billing/claims/:id`, items, status-history. 목록에서 이용자명 링크로 진입. `window.print()` + `@media print` 레이아웃.
- **결석(US-E01)** — `AttendanceAbsentModal` + `POST /attendance/absent`. 미처리(`PENDING`) 행에 「결석」버튼.
- **이용자 사진(US-D01)** — `ClientPhotoField` + `POST /clients/:id/photo` (multipart). `altText` 필수 when photo present.
- **보호자 초대(US-J01)** — `GuardianInviteModal` + `POST /clients/:id/guardian-invites`. v1.1 API 미준비 시 404/501 안내.
- **보호자 목록(US-D01·US-J01)** — `GET /clients/:id` 응답 `guardians[]`. `GuardianListCard` 초대 API는 v1.1.
- **귀가 처리(US-E01)** — `AttendancePage`: 「귀가」클릭 → `CheckoutModal` + `POST /attendance/checkout` `{ transportMethod }`. 표 교통편 컬럼은 저장 후 `transportMethod` 표시만.
- **NHIS 비교(US-G06)** — `ReconciliationPage` 「비교」버튼 → `Modal` + `DiscrepancyComparePanel`. API: `GET /billing/nhis-imports/:batchId/rows/:rowId/compare`.
- **NHIS 후보 검색(43차, US-G06)** — `ReconciliationPage` 미매칭 행 수동 연결 폼의 `SearchInput`은 250ms 디바운스 후 `fetchNhisMatchCandidatesApi(batchId, { q, page, size })`를 재호출한다. coder: 백엔드 `GET /api/v1/billing/imports/nhis/:batchId/candidates?q=` 가 **이름·인정번호 부분 일치** + **배치 지점 스코프**(`trg_nhis_rows_client_branch`) 필터를 지원해야 한다(빈 `q`는 지점 내 미연결 후보 상위 N). 매칭은 `PATCH .../rows/:rowId/match { clientId }` 단일 트랜잭션(V19).
- **보호자 명세(US-J02)** — `GuardianPage` billing 탭 행 클릭 → `GuardianBillingDetailModal`. API: `GET /guardian/clients/:id/billing/:claimId`.
- **본인부담 구분(US-D01)** — ✅ **10차 완료**: `ClientFormPage`의 copay `<Select>`를 `CopayTypeSelect`로 교체함. `COPAY_TYPES` 상수 공유.
- **이용자 본인 계정(US-D01·FLOWCHART §4 J)** — `ClientFormPage` 하단 「이용자 본인 계정」 섹션의 `ClientUserAccountField`. 폼 payload에 `issueClientUser`(boolean)·`clientUserLoginId`(발급 시 email)를 포함한다. 백엔드: `POST /api/v1/clients` 응답·요청에 이 두 필드 처리 — 발급 시 `client_user` 계정 생성 + 이용자 연결, 임시 비밀번호 메일. `allowSelfCheckin` 값은 Organization `allow_client_self_checkin` 설정(현재 `user.allowClientSelfCheckin` 가정 — coder가 실제 소스에 맞게 배선). QR 셀프 체크인은 설정 on일 때만 동작(§3-3, US-E04).
- **QR 체크인(US-E04)** — `GuardianCheckinPage`: `QrScanPanel` + `ClientSelector`. html5-qrcode는 `#qr-reader`를 `.ds-qr-scan__viewport` 내부에 마운트 (UXD-2).
- **투약 중복(US-F02)** — `HealthPage`: `GET /clients/:id/medications?date=today`로 `recentMedications` 초기화. API 409 시 `MedicationDuplicateAlert`와 동일 UX 유지.
- **낙상·특이사항(41차, US-F03)** — `HealthPage` 「낙상·특이사항」탭의 `IncidentRecordForm` + `createIncidentApi`(`POST /clients/:id/health/incidents`). 백엔드 `incident` recordType·`incidentType` enum 구현 후 정합. **대시보드 「건강 이상」 반영(인수 조건 2)**: 낙상·사고를 `/dashboard/*` 건강 알림 집계에 포함 → `HealthAlertList`로 표시(coder).
- **활력징후 정상 범위(40차, US-F01)** — `utils/vitalsRanges.js`가 단일 원천. 입력 폼 경고는 `evaluateVital(field, value)`, 건강 이상 배너 목록은 `findAbnormalVitalRecords(records)` 사용. 임계값(수축기 90–140·체온 35.5–37.5·혈당 70–200·SpO₂ ≥92)을 페이지에 재정의(하드코딩) 금지 — 백엔드 비정상 기준과 정합 필요 시 이 파일만 수정. advisory 경고는 `Field warning` prop(`role="status"`)으로 표시하며 저장을 차단하지 않는다.
- **전사 설정 토글(US-I03·§3-3)** — `SettingsPage` 「조직 설정」탭의 `Switch`(`allow_client_self_checkin`). 초기값은 `GET /api/v1/settings/organization`으로 주입(현재 `user.allowClientSelfCheckin` 가정 — coder가 실제 소스에 배선), 변경 시 `PATCH /api/v1/settings/organization { allowClientSelfCheckin }` 호출(낙관적 업데이트 또는 응답 후 확정). 이 값은 US-E04 QR 셀프 체크인(`client_user`) 허용과 `ClientUserAccountField`(US-D01) 안내에 연동된다.
- **의료비공제(77차, US-L04 G26)** — `MedicalExpenseDeductionPanel`의 `variant="staff"`는 `fetchClientMedicalExpenseDeductionApi(clientId, year)`(`GET /api/v1/clients/:id/billing/medical-expense-deduction?year=`), `variant="guardian"`은 `fetchGuardianMedicalExpenseDeductionApi(clientId, year)`(`GET /api/v1/guardian/clients/:id/billing/medical-expense-deduction?year=`). 응답 스키마: `{ clientName, taxYear, paymentCount, totalPaidAmount, items: [{ claimId, yearMonth, copayAmount, paidAt, paymentMethod }] }`. **CMS(`EASY_PAY`)·간편결제 제외** — 백엔드가 `paymentMethod` 필터(BANK_TRANSFER·CASH만)를 적용해야 함(BNK-73 `paidAt` 필드 선행).
- **외출 관리(77차, G15 BNK-63)** — `ClientOutingPanel` API: `GET /clients/:id/outings`, `POST .../outings`(`{ outingDate, plannedDepartureTime, plannedReturnTime, reason, companionName }`), `PATCH .../outings/:outingId`(수정), `POST .../outings/:outingId/depart`(출발), `POST .../outings/:outingId/return`(복귀), `POST .../outings/:outingId/cancel`(취소). `ClientOutingsPage`(`/transport/outings`) — 전 이용자 외출 목록(`GET /outings?branchId=&yearMonth=`). `ClientOutingReportPage`(`/reports/client-outings`) — 월간 외출 리포트(`GET /outings/report?branchId=&yearMonth=`).
- **차량 관리(77차, G16)** — `TransportVehicleSelect` prop: `branchId`, `value`(vehicleId), `onChange(vehicleId)`. API: `GET /api/v1/transport/vehicles?branchId=`. 응답: `[{ id, plateNumber, capacity, isActive }]`. `VehiclesPage`(`/transport/vehicles`) — 차량 CRUD(`GET/POST /transport/vehicles`, `PATCH .../vehicles/:id`).
- **이동서비스 수칙(77차, G15)** — `TransportCompliancePanel` API: `GET /transport/contracts?clientId=` → 기존 수칙 완료 체크·서명 로드. `saveTransportContractApi` → `POST /transport/contracts { clientId, completedRuleIds, guardianSignatoryName, guardianSignedOn, institutionSignatoryName, institutionSignedOn }`. `canSave` prop은 `branch_admin`·`social_worker`에서 `true`.
- **세션 만료(US-B03)** — `SessionTimeoutProvider`가 idle 감지. refresh 토큰 연장 API는 coder가 `onExtend`에 연동.
- **수가 이력(US-G00a)** — `FeeSchedulePage` 「이력 보기」 → `Modal` + `FeeRateHistoryPanel`. API: `GET /api/v1/billing/fee-schedules/history?year=` 응답에 `[{ year, grade, dailyRate, effectiveFrom, createdAt, createdByName? }]` 배열 포함. 현재 `historyEntries` 빈 배열 스켈레톤 — coder가 API 연동.
- **건강 추이 차트(US-F04)** — `HealthDetailPage`: `GET /api/v1/clients/:id/health?days=7|30` 응답을 `HealthTrendChart` `data` prop에 주입. 각 항목: `{ date, systolic, diastolic, temperature, bloodSugar, spo2 }`.
- **월별 출석률 차트(US-H01)** — `DashboardPage`: `branchDashboard.monthlyAttendanceRates[]` → `AttendanceRateChart` `data={ label: yearMonth, rate: attendanceRate }`.
- **일자별 출석률(US-E05)** — `AttendanceStatsPage`: `summary.dailyRates[]` → `AttendanceRateChart variant="bar"`. API 미포함 시 빈 상태 안내.
- **HQ 지점 비교(US-H02)** — `DashboardPage` hq: `hqDashboard.branches[]` → `BranchCompareChart`. 각 지점 `attendanceRate` 필수.
- **NHIS 배치 상태(US-G04)** — `BATCH_STATUS` 상수를 `import { BATCH_STATUS } from "../components/ui"` 로 가져온다(NHISImportPage 로컬 정의 제거·14차). coder는 모든 신규 페이지에서 Badge 모듈 상수를 사용.
- **플랫폼 고객사 관리(US-A01/A02)** — `PlatformPage` 「관리」→ `PlatformOrgDetailModal`. Tenant 상세 `dl` + `POST /api/v1/platform/organizations/:id/admins { email }` 발급. 목록 검색은 `SearchInput`, 상태는 `StatusBadge`+`BRANCH_STATUS`.
- **NHIS 배치 진행(US-G04)** — `BatchProgressSteps`로 PENDING→PROCESSING→COMPLETED 파이프라인 표시. `ReconciliationPage` 배치 카드 상단, `NHISImportPage` 미완료 배치 행에 인라인 표시. FAILED 시 처리중 단계 `--failed` 스타일.
- **감사 로그(US-I03)** — `SettingsPage` audit 탭 → `AuditLogPanel`. API: `GET /api/v1/settings/audit-logs?eventType=&from=&to=&page=`. `actorLabel`·`ipMasked`는 마스킹 문자열.
- **백업 설정(US-I03)** — `BackupSettingsPanel`. API: `GET/PATCH /api/v1/settings/backup`, `POST /api/v1/settings/backup/trigger`.
- **최초 비밀번호 변경(US-A02)** — `login()` 응답 `mustChangePassword` → `LoginPage` `PasswordChangeModal required`. API: `POST /api/v1/auth/change-password { newPassword }`. 완료 후 `clearMustChangePassword()` + 홈 이동.
- **청구 상태 카운트(US-G07)** — `GET /billing/claims` 응답 `statusCounts: { total, draft, confirmed, paid }` → `FilterChips counts`.
- **로그인 이력(§3-1)** — `SettingsPage` login-history 탭 → `LoginHistoryPanel`. API: `GET /api/v1/settings/login-history?role=&from=&to=&page=`. `emailMasked`·`ipMasked` 마스킹 문자열.
- **비밀번호 재설정(§3-1)** — `LoginPage` → `PasswordResetRequestModal`. API: `POST /api/v1/auth/password-reset/request { email }`. v1.1 실발송 전 스텁 UI.
- **페이지 오류 Alert(18·20차)** — 모든 Must 페이지 API 오류는 `Alert tone=danger`+`ds-page-alert`. coder 신규 페이지도 동일 패턴 준수. 20차 대상: `PlatformPage`·`BillingPage`·`DashboardPage`·`GuardianPage`·`CopayRatePage`.
- **청구 상태 확인(US-G07)** — `BillingPage` `openStatusConfirm(claim, nextStatus)` → `BillingStatusConfirmModal`. `BillingDetailPage` 상태 버튼도 동일 패턴 적용 권장.
- **NHIS 가이드(US-G04)** — `NhisImportGuidePanel`을 import 페이지 상단에 배치. 중복 Alert/ol 인라인 금지.
- **본인부담 비율(US-G00b)** — `CopayRateTable`+`PATCH /api/v1/billing/copay-rates`. `COPAY_TYPES`와 테이블 기본값 동기화.
- **보호자 포털(US-I02)** — `GuardianDailySummary`+`GET /guardian/clients/:id/summary`. `attendanceStatus`는 `ATTENDANCE_STATUS` 키.
- **건강 알림 공통** — 대시보드·보호자 포털 모두 `HealthAlertList` 사용. raw `<span class=ds-health-alert-list__badge>` 인라인 금지.
- **수가표 편집(US-G00a)** — `FeeScheduleTable`+`FeeSchedulePage`. raw `<input class=ds-input>` 인라인 금지 — `TextInput`+`aria-label` 패턴.
- **청구 상세 상태(US-G07)** — `BillingDetailPage` `openStatusConfirm` → `BillingStatusConfirmModal`. 목록 `BillingPage`와 동일.
- **미납 지표(US-L02)** — `OverduePage` `StatCard tone=danger`. 인라인 `color: danger-text` 금지.
- **페이지 오류 Alert(21차)** — `HealthDetailPage`·`QrGeneratePage`·`ClientDetailPage` 탭 오류도 `Alert tone=danger`+`.ds-page-alert`.
- **대상 월(22차)** — `MonthInput`+`Field`. raw month input 금지.
- **입금(22차)** — `PaymentRecordModal`+`PaymentPage`. inline Modal 폼 금지.
- **reconciliation 요약(22차)** — `ReconciliationSummaryBar`. inline flex summary 금지.
- **이용자 검색(22차)** — `SearchInput hideLabel`. action bar raw search 금지.
- **Must 페이지 레이아웃(24차)** — Card `className="ds-section-gap|ds-section-gap--lg|ds-card--mb"`·페이지 `.ds-page-lede`/`.ds-page-footnote`·표 빈 셀 `.ds-table-empty`·액션 `.ds-table-actions`. raw `style={{ marginTop/color }}` **금지** — ChartContainer `height`·`axisTextColor` prop 등 동적 값만 예외.
- **청구 월 필터(25차)** — `BillingPage` `MonthInput`+`Field`. raw `type=month`+`ds-input--month` **금지**.
- **차트 범례(25차)** — `HealthTrendChart`·`BranchCompareChart` Legend `formatter` → `<span className="ds-chart__legend-label">`. `ChartContainer`에 `axisTextColor={axisText}` 전달.
- **로그아웃(25차)** — `AppShell`이 `LogoutButton`을 topbar에 기본 탑재. 페이지별 로그아웃 버튼 중복 추가 금지.
- **보호자 초대 수락(26차, US-J01)** — `GuardianInvitationAcceptPage` → `PublicAuthLayout wide` + `GuardianInvitationAcceptForm`. AppShell/SideNav **금지**. API: `POST /guardian/invitations/{token}/accept`. 만료(404/410) → `error` Alert + `disabled`. 성공 → `success` + 폼 잠금 + `navigate("/")`. **`INVITATION_STATUS`** — 초대 목록 Badge.
- **보호자 초대 이력(27차, US-J01)** — `ClientDetailPage` `client.guardianInvitations[]` → `GuardianListCard` → `GuardianInvitationList`. 재발송/취소 API 연동 후 `handleResendInvitation`·`handleRevokeInvitation` 스텁 제거.
- **기간 필터(27·28차, §3-1·US-D01·US-L01)** — `AuditLogPanel`·`LoginHistoryPanel`·`ClientFormPage`·`PaymentRecordModal` `DateInput`+`Field`. raw `type=date` 금지.
- **사진 업로드(28차, US-D01)** — `ClientPhotoField` 트리거 버튼 `aria-label`+`aria-controls`. alt는 `TextInput`+`Field`.
- **보호자 초대 피드백(28차, US-J01)** — `ClientDetailPage` 초대 성공/오류 `Alert tone=success|warning`+`.ds-page-alert`. `GuardianInviteModal` 발송 `aria-busy`.
- **보호자 상세 빈 상태(25차)** — `GuardianDetailPage` API 실패/미응답 → `EmptyState`+`Alert tone=danger`+`ds-page-alert`.
- **ToastProvider** — `main.jsx`에서 `<BrowserRouter>` 안 `<App />`을 감싼다. `SessionTimeoutProvider`는 `App.jsx` `AuthProvider` **내부**.
- **FileUpload `accept`**: NHIS 엑셀은 `".xlsx,.xls"`.
- **Modal `aria-labelledby`**: `useId()` 기반 고유 ID — 동일 페이지에 Modal 복수 렌더 시 중복 ID 없음. React 18+ 필수.

---

## 8. 화면 목록 & 라우트 (develop 기준) [UXD]

### 8-1. 전체 라우트

| 경로 | 컴포넌트 | 허용 역할 | User Story |
|------|---------|---------|-----------|
| `/` | `LoginPage` | 공개 | US-B01 |
| `/dashboard` | `DashboardPage` | branch_admin, social_worker, caregiver, hq_admin | US-H01 |
| `/dashboard/hq` | `DashboardPage` | hq_admin | US-H02 |
| `/branches` | `BranchesPage` | hq_admin, branch_admin | US-C01 |
| `/clients` | `ClientListPage` | branch_admin, social_worker, caregiver, hq_admin | US-D02 |
| `/clients/new` | `ClientFormPage` | branch_admin, social_worker, hq_admin | US-D01 |
| `/clients/:id` | `ClientDetailPage` | branch_admin, social_worker, caregiver, hq_admin | US-D03, **US-M01** |
| `/guardians` | `GuardiansPage` | branch_admin, hq_admin, social_worker | **US-K01** |
| `/guardians/:id` | `GuardianDetailPage` | branch_admin, hq_admin, social_worker | **US-K02** |
| `/clients/:id/edit` | `ClientFormPage` | branch_admin, social_worker, hq_admin | US-D01 |
| `/attendance` | `AttendancePage` | branch_admin, social_worker, caregiver, hq_admin | US-E02 |
| `/attendance/checkin` | `AttendancePage` | branch_admin, social_worker, caregiver, hq_admin | US-E01 |
| `/attendance/boarding` | `AttendancePage` | branch_admin, social_worker, caregiver, hq_admin | **US-E06** (탑승 출석·`transportMode=boarding`) |
| `/attendance/on-site` | `AttendancePage` | branch_admin, social_worker, caregiver, hq_admin | **US-E06** (현장 출석·`transportMode=on_site`) |
| `/attendance/qr/generate` | `QrGeneratePage` | branch_admin, social_worker, caregiver, hq_admin | US-E03 |
| `/attendance/stats` | `AttendanceStatsPage` | branch_admin, social_worker, caregiver, hq_admin | US-E05 |
| `/health` | `HealthPage` | branch_admin, social_worker, caregiver, hq_admin | US-F01~F03 |
| `/health/:clientId` | `HealthDetailPage` | branch_admin, social_worker, caregiver, hq_admin | US-F04 |
| `/visits` | `VisitsPage` | branch_admin, social_worker, caregiver, hq_admin | **US-V01~V03** (등록·확정·취소 branch_admin/social_worker, 체크인/아웃 social_worker/caregiver) |
| `/billing` | `BillingPage` | branch_admin, hq_admin | US-G02, US-G07 |
| `/billing/claims/:claimId` | `BillingDetailPage` | branch_admin, hq_admin | **US-G02**, US-G07 |
| `/billing/payments` | `PaymentPage` | branch_admin, hq_admin | **US-L01** |
| `/billing/overdue` | `OverduePage` | branch_admin, hq_admin | **US-L02** |
| `/billing/imports/nhis` | `NHISImportPage` | branch_admin, hq_admin | US-G04 |
| `/billing/imports/nhis/:batchId` | `ReconciliationPage` | branch_admin, hq_admin | US-G06 |
| `/billing/fee-schedules` | `FeeSchedulePage` | hq_admin | US-G00a (G9 duration_band·G11 가산율 가이드) |
| `/billing/copay-rates` | `CopayRatePage` | hq_admin | US-G00b |
| `/billing/cms` | `CmsPage` | branch_admin, hq_admin | **US-L03** (CMS 자동이체) |
| `/billing/reports/charges` | `BillingReportPage` | branch_admin, hq_admin | **US-M03** (청구대장 7-6) |
| `/billing/reports/deposits` | `BillingReportPage` | branch_admin, hq_admin | **US-M03** (입금대장 7-7) |
| `/billing/reports/receipts` | `BillingReportPage` | branch_admin, hq_admin | **US-M03** (수납대장 7-8) |
| `/billing/calculator` | `CopayCalculatorPage` | branch_admin, hq_admin | **US-M03** (간편계산기 7-10) |
| `/platform` | `PlatformPage` | platform_admin | US-A01, US-A02 |
| `/guardian` | `GuardianPortalPage` | guardian, client_user | US-I02, US-J02 |
| `/guardian/checkin` | `GuardianCheckinPage` | guardian, client_user | **US-E04** (FLOWCHART §9 canonical) |
| `/attendance/checkin/qr` | `GuardianCheckinPage` | branch_admin, social_worker, caregiver, hq_admin | US-E04 (직원 QR 화면 — staff 경로) |
| `/guardian/invitations/:token/accept` | `GuardianInvitationAcceptPage` | **공개**(미인증) | **US-J01** |
| `/settings` | `SettingsPage` | sysadmin, hq_admin, platform_admin | US-I03 |
| `/organization/settings` | `OrganizationSettingsPage` | hq_admin | US-UX-03 (전사 정책·셀프 체크인 토글) |
| `/transport` | `TransportPage` | hq_admin, branch_admin, social_worker, caregiver | **US-T01·T03** (배차 명단·확정 조회) |
| `/transport/runs/new` | `TransportRunNewPage` | hq_admin | **US-T02** (루트 편집·확정) |
| `/transport/runs/:runId` | `TransportRunDetailPage` | hq_admin (편집), 직원 (확정 조회) | **US-T02·T03** (확정/취소·읽기 전용·G15 `TransportCompliancePanel`) |
| `/transport/vehicles` | `VehiclesPage` | hq_admin, branch_admin (관리), social_worker·caregiver (조회) | **US-T05** (차량 마스터·G16) |
| `/transport/service-fees` | `TransportServiceFeePage` | branch_admin, social_worker, caregiver, hq_admin | **US-T05** (이동서비스비 청구·G16) |
| `/transport/outings` | `ClientOutingsPage` | branch_admin, social_worker, caregiver, hq_admin | **US-T05** (외출 관리·BNK-63, 케어포 2-1-1) |
| `/reports/client-outings` | `ClientOutingReportPage` | branch_admin, social_worker, hq_admin | **US-T05** (외출 리포트·BNK-63, 케어포 2-9) |
| `/meals` | `MealsPage` | branch_admin, social_worker, caregiver, hq_admin | **US-N01** (식사 관리) |
| `/programs` | `ProgramsPage` | branch_admin, social_worker, caregiver, hq_admin | **US-N02** (프로그램 관리) |
| `/staff` | `StaffPage` | branch_admin, hq_admin | **§3-8** (직원 관리, v3) |
| `/staff/:id` | `StaffDetailPage` | branch_admin, hq_admin | **US-R03** (직원 lifecycle FAQ21825) |
| `/login` | `LoginPage` | 공개 | US-B01 (`/`는 `RootRedirect`) |
| `/forbidden` | `ForbiddenPage` | 공개 | — |

### 8-2. 사이드 네비게이션 (SideNav.jsx) — **2단 그룹 (US-UX-02)**

역할별 메뉴는 `SideNav.jsx`의 `NAV_CONFIG` **그룹 배열**에 정의. 각 그룹: `{ id, label, items: [{ label, path }] }`.

| 그룹 | 하위 예시 |
|------|----------|
| 운영 | 대시보드, 지점, 이용자, **직원 관리**, **보호자**, 플랫폼 관리(platform_admin), 전사 설정(hq), 시스템 설정(sysadmin), 보호자 포털·QR 체크인(guardian) |
| 이동 | 배차·이동경로(US-T01~T03) |
| 출석 | 현황, 수기 체크인, 통계, QR |
| 기록 | 건강, 식사, 프로그램, **방문 일정**(US-V01) |
| 청구 | 청구·정산, **공단 엑셀 import**, **입금**, **미납**, **CMS 자동이체**, 수가표·본인부담 비율(hq), **청구·입금·수납 대장**, **간편계산기** |

> 실제 정의는 `src/frontend/src/layout/navConfig.js` `NAV_GROUPS`(운영·이동·출석·기록·청구 5그룹). 본 표는 요약이며, 라우트 전수는 §8-1을 단일 원천으로 본다.

> **모바일**: 그룹별 접힘/펼침(`aria-expanded`). **데스크톱**: 항상 펼침(769px+).

> **active 매칭**: 동일 prefix의 하위 메뉴가 있는 경로(`/dashboard`, `/guardian`, `/attendance`, `/billing`)는 `EXACT_MATCH_PATHS`에 등록해 `NavLink end`로 **정확히 일치할 때만** 활성 처리한다(예: `/attendance/stats` 진입 시 「출석 관리」가 동시 활성화되지 않음).

| 역할 | 메뉴 항목 |
|------|---------|
| branch_admin | **운영**(대시보드·지점·이용자·보호자) · **출석** · **기록** · **청구**(입금·미납) |
| caregiver | 운영(대시보드) · 출석(체크인·QR) · 기록(건강) |
| social_worker | 운영(대시보드·이용자·보호자) · 출석(통계) · 기록(건강) |
| hq_admin | 운영(+통합/지점 대시보드) · 출석 · 기록 · **청구**(수가·copay·입금·미납) · 설정 |
| platform_admin | 고객사 관리, 시스템 설정 |
| guardian / client_user | 이용자 현황, QR 체크인 |

### 8-3. 미구현·후속 (coder TODO)

> **2026-06-07 36차**: 전체 15개 누락 페이지 UI 구현 완료. 아래는 coder가 API 연동해야 할 잔여 항목.

| 화면/기능 | 경로/파일 | 비고 |
|----------|-----------|------|
| 청구 상세 API | `BillingDetailPage` | US-G02 — `GET /billing/claims/:id` + items + status-history 응답 구조 확인 필요 |
| 결석 API | `AttendancePage` | US-E01 — `POST /attendance/absent` |
| 이용자 사진 API | `ClientFormPage` | US-D01 — `POST /clients/:id/photo` multipart |
| 등급 이력 API | `ClientDetailPage` grade 탭 | US-M01 — `ltcGradeHistory[]` |
| 대시보드 API | `DashboardPage` | US-M02 — `/dashboard/*` 통합 응답 |
| QR 카메라 스캔 | `GuardianCheckinPage` | `html5-qrcode` 라이브러리 연동 — 현재 수동 토큰 입력만 지원 (§10 UXD-2) |
| 건강·출석통계 차트 API | `HealthDetailPage`, `AttendanceStatsPage` | `HealthTrendChart`/`AttendanceRateChart` data prop에 API 응답 연동 |
| 낙상·특이사항 API | `HealthPage` 낙상·특이사항 탭 | US-F03 — `POST /clients/:id/health/incidents` + 대시보드 「건강 이상」집계 반영 |
| 로그인 이력 API | `SettingsPage` 감사 탭 | `GET /settings/login-history` |
| 방문요양 일정 API | `/visits` `VisitsPage` | **US-V01~V03** — backend `/api/v1/visits`·confirm/cancel/check-in/check-out **구현 완료(@ `d768820`)**. fetch-mock 회귀 PRESENT · **live backend E2E·HOME_CARE 지점 필터·NHIS 청구일정 import(US-V02)는 후속** |
| 직원 관리 API | `/staff` `StaffPage` | v3 §3-8 — UI·폼 검증·역할 Select **HEAD PRESENT** · `GET/POST /users` live 연동·자격·근태 **후속** |
| ~~배차 확정 취소 UI~~ | `TransportRunDetailPage` | ~~US-T02 frontend unconfirm UI 잔여~~ → **47차 `TransportUnconfirmModal` HEAD PRESENT** |

---

## 9. CSS 유틸리티 클래스 [UXD]

| 클래스 | 용도 |
|--------|------|
| `.ds-sr-only` | 스크린리더 전용 텍스트 (시각적 숨김) |
| `.ds-skip-link` | 본문 바로가기 키보드 링크 |
| `.ds-grid` | `auto-fit minmax(220px,1fr)` 대시보드 카드 그리드 |
| `.ds-form-row` | `auto-fit minmax(200px,1fr)` 폼 필드 그리드 |
| `.ds-form-section` | 폼 섹션 구분 박스 |
| `.ds-action-bar` | 목록 상단 검색/필터/액션 바 |
| `.ds-action-bar--end` | 액션 바 우측 정렬 (`StaffPage` 「+ 직원 등록」) |
| `.ds-consent-box` | 주민번호 수집 동의 안내 박스 (warning 배경) |
| `.ds-masked` | 마스킹 텍스트 (모노스페이스 + 연회색) |
| `.ds-avatar` | 이용자 이니셜 아바타 원형 |
| `.ds-status-dot` | 인라인 상태 점 (success/warning/neutral) |
| `.ds-row--warning` | 표 행 경고 강조 (DISCREPANCY) |
| `.ds-row--danger` | 표 행 위험 강조 (UNMATCHED) |
| `.ds-filter-chip` | 상태 필터 칩 (FilterChips) |
| `.ds-chart-placeholder` | 차트 연동 전 플레이스홀더 |
| `.ds-qr-panel` | QR 생성·인쇄 패널 |
| `.ds-client-picker` | NHIS 수동 매칭 combobox |
| `.ds-dl-grid` | 설정·상세 description list 그리드 |
| `.ds-linked-clients` | 보호자 상세 연결 이용자 카드 (US-K02) |
| `.ds-timeline` | 등급 변동 이력 타임라인 (US-M01) |
| `.ds-dashboard-widgets` | 대시보드 위젯 그리드 (US-M02) |
| `.ds-masked-phone` | 마스킹 연락처 + `tel:` 링크 (30차 — `MaskedPhone`) |
| `.ds-sidenav__sublist` | 2단 SideNav 하위 메뉴 (US-UX-02) |
| `.ds-grid--2` | 2열 폼 그리드 (초대 모달 등) |
| `.ds-photo-field` | 이용자 사진 업로드+미리보기 (US-D01) |
| `.ds-select--inline` | 표 내 인라인 select — 44px 터치 타깃 |
| `.ds-client-picker__option--active` | combobox 키보드 활성 옵션 |
| `.ds-timeline--compact` | 청구 상태 이력 등 컴팩트 타임라인 |
| `.ds-client-selector` | 복수 이용자 radiogroup (US-E04, US-J02) |
| `.ds-compare-panel` | NHIS vs ogada 청구 비교 패널 (US-G06) |
| `.ds-billing-statement` | 보호자 본인부담금 명세서 (US-J02) |
| `.ds-qr-scan` | QR 카메라 + 수동 토큰 입력 (US-E04) |
| `.ds-health-abnormal-list` | 건강 비정상 수치 목록 (US-F01) |
| `.ds-health-alert-list` | 보호자 포털 건강 알림 — 텍스트+배지 (US-I02) |
| `.ds-link-button` | Alert 내 텍스트 액션 링크 (투약 중복 확인) |
| `.ds-feedback--success/danger` | QR·폼 결과 피드백 (role=alert) |
| `.ds-client-user-account` | 이용자 본인 계정 발급 필드 묶음 (US-D01) |
| `.ds-topbar__actions` | 상단바 우측 액션 묶음 (테마 토글 + topbarRight) |
| `.ds-theme-toggle` | 라이트/다크 전환 버튼 (11차, 480px 이하 라벨 숨김) |
| `.ds-label` | 단독 라벨 (Field 래퍼 미사용 시, 12차) |
| `.ds-login` / `.ds-login__brand`·`__logo`·`__wordmark`·`__title`·`__subtitle`·`__error` | 로그인 진입 카드·브랜드 모노그램 (12차, US-B01) |
| `.ds-switch` / `.ds-switch__text`·`__label`·`__description`·`__control`·`__track`·`__thumb`·`__state` | 설정 on/off 토글 (13차, US-I03 — WAI-ARIA switch) |
| `.ds-progress-steps` / `__step`·`__dot`·`__label` / `--done`·`--active`·`--failed` | NHIS 배치 진행 단계 시각화 (14차, US-G04) |
| `.ds-fee-history` / `__title`·`__empty`·`__year-group`·`__year-label`·`__table` | 수가 이력 패널 (14차, US-G00a — FeeRateHistoryPanel) |
| `.ds-fee-table-cell` | 표 내 수가 인라인 입력 셀 (14차, FeeSchedulePage) |
| `.ds-chart` / `__title`·`__viewport`·`__empty`·`__hint`·`__legend-label` | Recharts 접근성 래퍼 (15차, ChartContainer; 25차 범례 라벨) |
| `.ds-link` | 인라인 텍스트 링크 — `role-link` 대체 (15차) |
| `.ds-audit-log` / `__filters`·`__loading` | 감사 로그 패널 (17차, AuditLogPanel) |
| `.ds-backup-settings` / `__summary`·`__actions`·`__note` | 백업 설정 패널 (17차) |
| `.ds-filter-chip__count` | FilterChips 상태 건수 배지 (17차, US-G07) |
| `.ds-login__footer` | 로그인 하단 재설정 링크 (17차) |
| `button.ds-link` | 표·목록·로그인 내 텍스트 링크 버튼 (17·18차) |
| `.ds-page-alert` | 페이지 상단/본문 API 오류·피드백 Alert 여백 (18차) |
| `.ds-login-history` / `__title`·`__help`·`__filters`·`__loading` | 로그인 이력 패널 (18차, LoginHistoryPanel) |
| `.ds-security-panel` | 보안 탭 PasswordChange·PasswordReset 액션 컨테이너 (19차, SettingsPage) |
| `.ds-billing-confirm__summary` | 청구 상태 확인 모달 요약 dl (20차) |
| `.ds-nhis-guide` / `__steps`·`__note`·`__intro` | NHIS import 온보딩 패널 (20차, US-G04) |
| `.ds-copay-rate-cell` / `__unit` | 본인부담 비율 입력 셀 (20차, US-G00b) |
| `.ds-guardian-summary` / `__stats`·`__alerts` | 보호자 포털 오늘 현황 (20차, US-I02) |
| `.ds-health-alert-list__empty`·`__reasons` | HealthAlertList 빈 상태·사유 (20차) |
| `.ds-action-bar__actions--start` | action-bar 좌측 정렬 (20차, CopayRatePage) |
| `.ds-text-secondary` / `.ds-text-muted` | 보조·플레이스홀더 텍스트 (21차) |
| `.ds-mono` | 인정번호·배치 ID 등 고정폭 (21차) |
| `.ds-diff-amount` | NHIS reconciliation 차이 금액 강조 (21차, US-G06) |
| `.ds-table-actions` | 표 내 액션 버튼 flex 래퍼 (21차) |
| `.ds-section-gap` | 카드·섹션 상단 여백 (21차) |
| `.ds-section-gap--top` | 섹션 상단 여백 (46차 — DiscrepancyComparePanel·GuardianPortalPage) |
| `.ds-stack` | 카드 내 세로 섹션 스택 + 구분선 (46차 — MealsPage·ProgramsPage·TransportPage) |
| `.ds-filter-row` / `.ds-filter-row__actions` | 필터 폼 가로 행·조회 버튼 우측 정렬 (46차 — PaymentPage) |
| `.ds-modal-section-title` | 모달 내 섹션 h3 (46차 — PlatformOrgDetailModal) |
| `.ds-inline-actions--start` | dl 값·인라인 배지+버튼 묶음 (46차 — GuardianDetailPage) |
| `.ds-table-empty` | 표 빈 상태 셀 (21차) |
| `.ds-stat__value--danger` | StatCard 위험 지표 값 색 (21차, US-L02) |
| `.ds-fee-schedule-hint` | 수가표 1밴드 안내 텍스트 (21차) |
| `.ds-forbidden-page__desc` / `__actions` | 403 페이지 본문·링크 (21차) |
| `.ds-summary-bar` / `.ds-summary-item` | NHIS reconciliation 배치 요약 (22차, US-G06) |
| `.ds-month-input` | 대상 월 입력 max-width (22차, US-E05·G04) |
| `.ds-modal-intro` | 모달 상단 요약 텍스트 (22차, US-L01) |
| `.ds-form-actions` | 카드·폼 하단 액션 버튼 여백 (22차) |
| `.ds-section-gap--lg` | 섹션 간 24px 여백 (22차) |
| `.ds-batch-progress-inline` | 표 셀 내 NHIS 진행 단계 (22차) |
| `.ds-summary-item__label` / `__value` | Reconciliation 배치 요약 항목 (21차) |
| `.ds-inline-actions` | 버튼·뱃지 수평 중앙 정렬 묶음 (23차, ClientDetailPage 등) |
| `.ds-client-summary` / `__avatar`·`__name`·`__meta` | 이용자 상세 요약 헤더 (23차, US-D03) |
| `.ds-form-actions--end` | 폼 하단 액션 버튼 우측 정렬 (23차, ClientFormPage) |
| `.ds-page-lede` | 페이지 상단 보조 텍스트(날짜·안내) (24차, AttendancePage) |
| `.ds-grid--gap-bottom` | StatCard 그리드 하단 여백 (24차, AttendancePage) |
| `.ds-card--mb` | Card 하단 간격 (24차, GuardianPage) |
| `.ds-form-row__action` | 폼 행 내 버튼 정렬 (24차, QrGeneratePage) |
| `.ds-page-footnote` | 페이지 하단 각주·v2 안내 (24차, OverduePage·SessionTimeoutModal) |
| `.ds-card-link` | 카드 내부 링크 여백 (24차, DashboardPage) |
| `.ds-dl-grid--spaced` | description list 하단 여백 (24차, PlatformOrgDetailModal) |
| `.ds-alert--stack` / `.ds-form--stack` | Alert·폼 스택 여백 (24차) |
| `.ds-tab-panel-body` / `.ds-submit-block` | 탭 패널·주요 CTA 상단 여백 (24차, GuardianPage·GuardianCheckinPage) |
| `.ds-alert-body` / `.ds-alert-body--flush` / `.ds-alert-action` | Alert 본문·액션 (24차, MedicationDuplicateAlert·HealthAbnormalBanner) |
| `.ds-tabular-nums` | 표 숫자 열 (24차, FeeRateHistoryPanel) |
| `.ds-progress-steps__list` | NHIS 배치 진행 ol (24차, BatchProgressSteps) |
| `.ds-section-gap--bottom` | 하단만 24px 여백 (24차, QrGeneratePage) |
| `.ds-context-nav` / `.ds-billing-context-nav` / `__list` / `__link` / `__link--active` | 모듈 컨텍스트 네비 — 출석(73차, US-E01~E06)·입금·미납(65차, US-L01·L02)·**기록(75차, US-F01·N01·N02·V01 `RecordsContextNav`)** |
| `.ds-auth-page` / `--wide` / `__lede` / `__actions` | 공개 인증 카드 (26차, US-J01 — LoginPage `.ds-login` 확장, AppShell 대체) |
| `.ds-date-input` | 기간 필터 date input max-width (27차, §3-1) |
| `.ds-guardian-card__subtitle` / `__invitations` | 보호자 카드 초대 이력 섹션 (27차, US-J01) |
| `.ds-guardian-invitations` | 초대 이력 표 overflow (27차) |
| `.ds-list` / `.ds-list__item` | Must 목록 ul/li 레이아웃 (33차) |
| `.ds-breadcrumb` | 상세 페이지 경로 (33차, ClientDetailPage) |
| `.ds-form-grid` | 폼 2열 그리드 (33차, ClientDetailPage·NHISImportPage) |
| `.ds-tabs__list` / `.ds-tab` / `.ds-tab--active` / `.ds-tabpanel` | WAI-ARIA 탭 (33차, US-D03) |
| `.ds-pagination` / `.ds-pagination__status` | 목록 페이지네이션 (33차) |
| `.ds-sidenav__group` / `__toggle` / `__sublist` / `__chevron` | 2단 SideNav 그룹 (33차, US-UX-02) |
| `.ds-branch-switcher` | topbar 지점 선택기 (33차, US-B02) |
| `.ds-branch-scope-notice` / `__label`·`__value`·`__hint` | 지점 스코프 조회 안내 (54차, US-UX-04 — `BranchScopeNotice` → 출석·QR·배차 6화면) |
| `.ds-tabs--sticky-mobile` | 모바일 배차 탭 sticky (53차, US-T03) |
| `.ds-form-actions--start` | 폼 액션 좌측 정렬 (77차) |
| `.ds-list-plain` | 마커 없는 플레인 목록 (77차) |
| `.ds-transport-form18__steps`/`__step` | 이동서비스비 별지 제18호 신청 절차 단계 목록 (77차, G15) |
| `.ds-transport-compliance__rules`/`__progress`/`__template` | 이동서비스 수칙 체크리스트·진행·서식 (77차, G15) |
| `.ds-medical-expense-panel`/`__summary`/`__filters`/`__total` | 의료비공제 납입 집계 패널 (77차, US-L04 G26) |
| `.ds-billing-report-print-zone` | 청구·의료비공제 인쇄 영역 격리 스코프 (77차, US-L04·US-M03) |
| `.ds-functional-recovery-compliance` / `.ds-stat-grid` | 기능회복훈련 지표25·26·27 준수 현황 StatCard 그리드 (78차, US-T06 G17) |
| `.ds-case-management-compliance` / `.ds-stat-grid` | 사례관리 회의록 지표43 준수 현황 StatCard 그리드 (78차, US-T07 G32) |

---

## 11. 브랜드·파비콘 (US-UX-01) [UXD]

> **2026-06-06 planner 지시**: v1.1 Must — 탭·북마크·모바일 홈추가 아이콘. COD 구현 전 **본 절 확정안** 따름.

### 11-1. 컨셉

| 항목 | 값 |
|------|-----|
| 브랜드명 | **ogada** (소문자, 로고 타입) |
| 심볼 | 원형 배경 + 흰색 **「o」** 모노그램 (주간보호·케어 연상) |
| Primary | `--color-primary` = blue-600 (`#1d4ed8`). ※ favicon `theme-color`도 동일 토큰값 사용 권장 (이전 표기 `#2563eb`는 blue-500 — 토큰 darken 후 불일치, `#1d4ed8`로 통일) |
| 배경 | Primary fill, 심볼 `#ffffff` |
| 톤 | 과도한 의료 적십자·하트 **금지** — B2B SaaS·신뢰·접근성 |

### 11-2. 파일·경로 (COD)

| 파일 | 크기 | 용도 |
|------|------|------|
| `public/favicon.svg` | 벡터 | 최신 브라우저 기본 |
| `public/favicon.ico` | 16+32 multi | 레거시 탭 |
| `public/apple-touch-icon.png` | 180×180 | iOS 홈 화면 |
| `index.html` | — | `<link rel="icon" href="/favicon.svg" type="image/svg+xml">`, `rel="apple-touch-icon"`, `<meta name="theme-color" content="#1d4ed8">` (= `--color-primary`) |

### 11-3. SVG 가이드 (COD 생성 기준)

- viewBox `0 0 32 32`, 원형 배경 radius 16, 중앙 「o」 sans-serif **700**, font-size ~18
- 32px에서 「o」 식별 가능 — 16px 축소 시 실루엣 유지
- 다크 모드: 동일 primary (후속 §10 다크 토큰과 별도 `media (prefers-color-scheme: dark)` 검토)

### 11-4. 완료 검증

- [ ] Chrome·Safari 탭에 ogada 파란 원 아이콘 표시
- [ ] iOS 「홈 화면에 추가」 180px 아이콘 선명
- [ ] `npm run build` 후 `dist/`에 favicon 자산 포함
- [ ] **(10차)** 브랜드 색을 `--color-primary`(`#1d4ed8`)로 통일 — `favicon.svg`·`theme-color` 반영 완료. 래스터 자산(`favicon.ico`·`apple-touch-icon.png`)은 **coder가 동일 색(`#1d4ed8`)으로 재생성** 필요(바이너리라 UXD가 직접 생성하지 않음).

---

## 10. 미해결·후속 (UX) [UXD]

- 아이콘 세트 미선정 — 의존성 추가는 coder/planner 협의 필요(현재 텍스트 기반).
- ~~차트(월별 출석률 US-H01/F04) — Recharts vs Chart.js 미선정~~ → **15차 UXD-1 완료**: **Recharts** 채택 + `ChartContainer`·`AttendanceRateChart`·`HealthTrendChart`·`BranchCompareChart` 구현. 플레이스홀더 제거. coder는 API data prop 연동만 남음.
- ~~NHIS 배치 진행 UI — CSS만 존재~~ → **16차 완료**: `BatchProgressSteps` React 컴포넌트 + `ReconciliationPage`/`NHISImportPage` 통합.
- ~~플랫폼 고객사 「관리」버튼 무기능~~ → **16차 완료**: `PlatformOrgDetailModal` + US-A02 관리자 발급 폼.
- QR 스캐너 — **html5-qrcode** vs native BarcodeDetector → #UXD-2. `GuardianCheckinPage`는 현재 토큰 수동입력 폴백 제공.
- ~~다크 모드 미정~~ → **11차 구현 완료**: `tokens.css` `[data-theme="dark"]` 토큰 오버라이드 + `ThemeToggle`(AppShell topbar) + `theme.js`. 컴포넌트가 시맨틱 토큰만 쓰므로 코드 변경 0. 대비 AA 검증 §2-4. 후속: 차트(Recharts 등) 도입 시 다크 팔레트 색 매핑 별도 확인.
- 미확정 사항은 `docs/planning/PLAN_NOTES.md`의 `### [UXD] UX 설계 질문` 섹션에 기록.
- Toast: `ToastProvider`를 `main.jsx`에 추가 후 `useToast()`로 API 연동 피드백. **9차 배선 완료**.
- SessionTimeoutModal: `SessionTimeoutProvider`가 AuthContext 30분 타이머와 연동 (US-B03). **9차 배선 완료**.
- 보호자 초대(US-J01 v1.1): `GuardianListCard` 「초대 발송」 버튼은 현재 `disabled` — v1.1 착수(v1 backend merged 이후) 시 활성화.
- **고대비/강제 색상(12차)**: `forced-colors`/`prefers-contrast` 규칙은 CSS만으로 동작(컴포넌트 코드 변경 0). **tester 검증 권장**: Windows 고대비 모드·`prefers-contrast: more`에서 로그인·대시보드·청구 표·모달 캡처해 경계선·포커스 식별성 확인.
- ~~`styles.css`의 데모 잔여 클래스(`.role-link`·`.demo-grid`)~~ → **25차 제거 완료**. 신규 링크는 `.ds-link`·`button.ds-link`만 사용.
- **33차 baseline 후속 (COD 우선순위)**:
  1. ~~`AppShell`·`SideNav`(2단)·`Table`/`Tabs`·`BranchSwitcher`·`StatCard`·`SearchInput`·`FilterChips`·`Pagination`·`LogoutButton`~~ → **33차 완료**.
  2. **페이지 연동**: `ClientDetailPage` raw 섹션 → `Tabs`/`TabPanel`(기본/건강/출석/청구 US-D03). `ClientListPage`·`BillingPage` → `SearchInput`·`Table`·`Pagination`·`FilterChips`. `DashboardPage` → `StatCard` 그리드(US-M02).
  3. **`BranchSwitcher` API**: `AppShell` `onBranchChange` → `PATCH /api/v1/auth/active-branch` + AuthContext `activeBranchId` 갱신.
  4. **`ToastProvider`·`SessionTimeoutProvider`·`SessionTimeoutModal`** — 30분 비활성(US-B03)·전역 피드백 (US-B03).
  5. 도메인 특화 컴포넌트(차트·NHIS·모달 등) — DESIGN_SYSTEM §7-2~7-7 카탈로그 참조, coder 페이지 연동.

---

---

## 12. 기능회복훈련·사례관리 화면 (US-T06 G17 · US-T07 G32) [UXD]

> **78차 UXD 추가** — BE 완료(SHA 73e169a / 55fae99), FE 누락분 구현.

### 12-1. FunctionalRecoveryPage (`/programs/functional-recovery`)

| 항목 | 상세 |
|------|------|
| 역할 | 조회: hq_admin·branch_admin·social_worker·caregiver / 등록: hq_admin·branch_admin·social_worker |
| 지표 | 지표25(급여계획포함 2점)·지표26(연1회실시 3점)·지표27(개인별계획수립) |
| 컴포넌트 | `AppShell`, `RecordsContextNav`, `StatCard` ×3, `Card`, `Table`, `EmptyState`, `Field`, `Select`, `Textarea`, `Switch`, `DateInput`, `Button`, `Alert`, `Spinner` |
| A11y | `aria-labelledby` 섹션 headings; `aria-busy` 저장버튼; `aria-invalid`/`aria-describedby` 필드 오류 연결; `role="group"` StatCard 영역 |
| 폼 필드 | `clientId`(필수), `planYear`(필수), `planContent`(필수), `includesCarePlan`(Switch), `annualExecutionDate`(DateInput) |
| API | `fetchFunctionalRecoveryPlansApi`, `createFunctionalRecoveryPlanApi`, `fetchFunctionalRecoveryComplianceApi` |

### 12-2. CaseManagementPage (`/case-management/meetings`)

| 항목 | 상세 |
|------|------|
| 역할 | 조회·등록: hq_admin·branch_admin·social_worker |
| 지표 | 지표43(분기1회이상, 참석자2인이상, 회의록보관) |
| 컴포넌트 | `AppShell`, `StatCard` ×3, `Card`, `Select`(분기필터), `Table`, `EmptyState`, `Field`, `Select`, `DateInput`, `Textarea` ×3, `Button`, `Alert`, `Spinner` |
| A11y | 분기 필터 `aria-label`; 참석자 2인 미만 시 `aria-invalid`·오류 메시지(지표43 근거 문구 포함); `role="group"` StatCard 영역 |
| 폼 필드 | `clientId`(필수), `meetingDate`(필수), `selectionReason`(필수), `meetingContent`(필수), `meetingResult`(필수), `attendeeNames`(쉼표구분·최소2인, 필수) |
| 검증 | `attendeeNames.split(",").filter(Boolean).length < 2` → 클라이언트 side 차단 |
| API | `fetchCaseManagementMeetingsApi`, `createCaseManagementMeetingApi`, `fetchCaseManagementComplianceApi` |

### 12-3. 네비게이션 변경

- `RecordsContextNav.jsx` — "기능회복훈련" (/programs/functional-recovery), "사례관리 회의록" (/case-management/meetings) 링크 추가
- `navConfig.js` `RECORD_ITEMS` — 동일 두 항목 추가 (사례관리는 caregiver 제외)
- `App.jsx` — 두 라우트 추가

---

## 13. 청구 추가 UI — 환불·NHIS 비교 (US-M03 · BNK-87) [UXD]

> **79차 UXD 추가 (2026-06-11)** — coder가 구현한 신규 컴포넌트 접근성 검토 및 CSS 보강.

### 13-1. RefundRecordModal (US-M03 7-9)

| 항목 | 상세 |
|------|------|
| 위치 | `src/components/ui/RefundRecordModal.jsx` |
| 사용 | `BillingDetailPage` — PAID 청구서의 「환불 처리」 버튼 |
| 컴포넌트 | `Modal`(role=dialog, aria-modal, aria-labelledby), `Field`, `TextInput`, `DateInput`, `Textarea`, `Button`, `Alert`, `Spinner` |
| 필드 | 환불 금액(필수), 환불일(필수, default 오늘), 환불 사유(선택) |
| A11y | `Modal` 공통 패턴 사용 — `role="dialog"` + `aria-labelledby="[titleId]"` + `aria-modal="true"` + 닫기 `aria-label="닫기"`. 저장 중 `aria-busy={submitting}`. 서버 오류 `role="alert"`. `Field` render-prop으로 label·id 자동 연결. |
| 금액 검증 | 0원 이하·환불 가능 금액 초과 시 Field 단위 오류 표시 |
| 테스트 | `RefundRecordModal.test.jsx` — 금액 검증·submit 흐름·오류 처리 포함 |

### 13-2. BillingNhisComparisonPanel (BNK-87)

| 항목 | 상세 |
|------|------|
| 위치 | `src/components/ui/BillingNhisComparisonPanel.jsx` |
| 사용 | `BillingDetailPage` — DRAFT 청구서 상세의 "공단 명세 비교" 탭/섹션 |
| 컴포넌트 | `section[aria-labelledby]`, `StatCard` ×3, `Table[caption]`, `StatusBadge`, `Alert`, `Spinner` |
| 상태 | `loading` → `Spinner`(label="공단 명세 비교 로딩 중") / `error` → `Alert(tone=danger)` / `data` → 요약 + 명세 테이블 |
| StatCard | 일치(success) / 불일치(danger if >0) / 공단 미매칭(warning if >0) — `role="group"` 그룹 |
| 테이블 | `<Table caption="이용자별 공단 명세 비교" captionVisuallyHidden>` + `scope="col"` th + 서비스일수 불일치 시 `.ds-sr-only` 보조 텍스트 추가 |
| A11y | `<section aria-labelledby="billing-nhis-comparison-heading">` / 불일치 행 `.ds-row--warning` + `forced-colors` 윤곽선 보강(CSS 추가) / 금액 열 `.ds-tabular-nums` |
| CSS | `components.css` 에 `.ds-billing-nhis-comparison` 스코핑 앵커 + `.ds-stat-grid` 그리드 + `forced-colors` 규칙 **79차 추가** |
| 테스트 | `BillingNhisComparisonPanel.test.jsx` — NHIS 배치 없음·불일치·일치 케이스 포함 |

### 13-3. G17/G32 대시보드 — 사례관리 30일 반영 갭 위젯

| 항목 | 상세 |
|------|------|
| 위치 | `DashboardPage.jsx` — `mapBranchDashboardSummary` / `mapHqDashboardSummary` |
| 데이터 | `fetchCaseManagementComplianceApi` → `countCaseManagementReflectionGaps` |
| StatCard | label="30일 미반영(사례관리)", tone=danger(>0)/default(0) |
| A11y | 기존 StatCard `ds-stat-grid` 그룹(`role="group"`) 내 추가 — 신규 a11y 변경 없음 |
| 테스트 | `dashboardSummary.test.js` — 30일 반영 갭 카운트 로직 커버 |

---

*이 문서는 ux_designer 에이전트(UXD)가 관리합니다. 토큰·컴포넌트 변경 시 본 문서와 `memory/decisions.md`를 동기화하세요.*
