<!-- doc:owner=UXD doc:audience=PLN,COD,TSR updated=2026-06-23T09:00:00+09:00 -->
# ogada 디자인 시스템 (product/DESIGN_SYSTEM.md)

> **작성**: ux_designer 에이전트 (`UXD`)
> **최초 작성일**: 2026-06-06
> **최종 갱신**: 2026-06-23 (155차 — **G-STAFF-ANNUAL-LEAVE Page wire-up 접근성 재점검 + `.ds-help-text`·`.ds-fieldset` FE-16 승격 + §78** — 154차(§77)·UXD-154(`5353991`) 이후 coder 신규 커밋 6건(`3902dba` Page·API wire·`80613c3`/`8434435`/`971c7f1` validation·title) 미점검 a11y·FE-16 갭 해소. ① **`StaffAnnualLeavePage`** — 저장 성공 `Alert role=status`·수정 modal `form aria-label`·표 섹션 `aria-busy`. ② **`.ds-help-text`·`.ds-fieldset`** — coder가 사용했으나 미정의였던 2 클래스 승격(`StaffWorkAttendancePage`·`StaffHealthCheckupsPage` 공유). ③ **§78** 신규. 회귀 +2. `npm test`·build PASS.)
> **이전 갱신**: 2026-06-22 (154차 — **G2-CMS-ROSTER·G34-WORKFLOW-CATALOG·G30-LEGEND 접근성 재점검 + G-STAFF-ANNUAL-LEAVE UI 셸 신규 + §77** — 153차(§76)·UXD-153(`da34daf`) 이후 coder 신규 커밋 6건(`77cfc38`/`9f110a5` G34·`fdc135b` G30-LEGEND·`df9ec6c`→`3ece965` G2 CMS roster) 미점검 a11y·US-R03e 컴포넌트 갭 해소. ① **`CmsEnrollmentTable`** — `enrolledAt` `<time dateTime>`·이용자 링크 `aria-label`. ② **`EzcareWorkflowCatalogPanel`·`MonitoringOfficialIndicatorLegendPanel`** — `Table caption` 추가. ③ **`StaffAnnualLeaveTable`** — ezCare worker-b100 tab01 14-field parity UI 셸·`staffAnnualLeave.js` 유틸·`.ds-staff-annual-leave*` CSS. ④ **§77** 신규. 회귀 +6. `npm test`·build PASS.)
> **이전 갱신**: 2026-06-22 (153차 — **US-D03 이용자 출석 탭·G-BILLING-REPORT-FILTER-PERSISTENCE·US-E03 QR 이미지 접근성 재점검 + §76 신규** — 152차(§75)·UXD-152(`df7f308`) 이후 coder 신규 기능 커밋 5건(`d058e43` US-D03 출석 이력 탭·`250619e` US-E03 QR 이미지·`8aabeae` chore·`daaba4b` QA-B233·`77b1ea8` G-BILLING-REPORT-FILTER-PERSISTENCE) 미점검 a11y·FE-16 갭 해소. ① **`BillingReportPage`** — `hydrateFiltersAndFetch` 필터 복원 비동기 구간(loadSavedFilters 호출~fetchReport 시작)에서 `loading=false` 상태로 버튼 `aria-busy` 미전달 갭 → `setLoading(true)` 선행 추가(WCAG 4.1.3). ② **`QrGeneratePage`** — `validUntil` 표시 시각 `toLocaleTimeString` 평문 → `<time dateTime={qrData.validUntil}>` 래핑(WCAG 1.3.1·88차 `StaffDetailPage` 날짜 의미론 패턴). ③ **US-D03 `ClientDetailPage` 출석 탭** — `Table` caption·`<time dateTime>`·`StatusBadge ATTENDANCE_STATUS`·`EmptyState`·`Spinner role=status` 모두 표준 준수(변경 불요). ④ **§76** 신규. 회귀 +2. `npm test`·build PASS.)
> **이전 갱신**: 2026-06-22 (152차 — **G-STAFF-WORK-ATTENDANCE·G-BILLING-DEPOSIT-ORDER-GUARD·US-E05 출석 통계 접근성 재점검 + §75 신규** — 151차(§74)·UXD-151(`9812ac4`) 이후 coder 신규 커밋 3종(`StaffWorkAttendancePage`·`CmsDebitPanel`·`AttendanceStatsPage`) 미점검 a11y 갭 해소. ① **`StaffWorkAttendancePage`** — 조회 `aria-busy`·StatCard `role=group aria-label`·출근·퇴근 반복 행 버튼 `aria-label`에 직원명·`aria-busy`·출퇴근 시각 `<time dateTime>`. ② **`AttendanceStatsPage`** — 조회 `aria-busy`·StatCard `role=group aria-label`. ③ **`CmsDebitPanel`** — 요청·완료 일시 `<time dateTime>`·상태 컨테이너 `<div>`→`<section aria-labelledby>` + `h3 id`. ④ **§75** 신규. 회귀 +4. `npm test`·build PASS.)
> **이전 갱신**: 2026-06-21 (151차 — **US-R03 모바일 서류 촬영 업로드 접근성 재점검 + `.ds-button` 미정의 셀렉터 회귀 해소 + §74 신규** — 150차(§73)·UXD-150(`751c593`) 이후 coder 신규 기능 커밋 `6bde24a`(feat US-R03 — 케어포 p.96 모바일 서류 촬영: `FileUpload.enableMobileCapture`·`StaffDocumentRepositoryPanel` 슬롯별 「모바일 촬영」·`StaffHrFilePanel`·`StaffRefresherCertificatePanel`) 미점검 a11y·FE-16 갭 해소. ① **모바일 촬영 a11y 확인** — 숨김 카메라 input(`capture="environment"`)은 `aria-hidden`·`tabIndex={-1}`로 트리거 버튼만 활성화·슬롯별 「모바일 촬영」 버튼 `${slot.label} 모바일 촬영 업로드` `aria-label`·`aria-busy`·「업로드 중…」 텍스트 상태(색 비의존)·실패 `Alert role=alert`·`section aria-busy` 모두 표준 준수(변경 불요). ② **`.ds-button` 미정의 셀렉터 회귀 해소(FE-16)** — `6bde24a`의 모바일 전폭 규칙 `@media(max-width:640px) .ds-staff-document-repository .ds-inline-actions .ds-button`이 본 코드베이스 `Button`(`.ds-btn` 렌더)과 불일치하는 **미정의 `.ds-button`**(전 CSS 유일 사용)을 타깃해 적용되지 않던 80·90·119차 패턴 회귀를 `.ds-btn`으로 정합(모바일 버튼 전폭 스택 복구·시각/동작 불변). ③ **§74** 신규. `StaffDocumentRepositoryPanel.test.jsx`·`FileUpload.test.jsx` 8/8 PASS·build PASS.)
> **이전 갱신**: 2026-06-21 (150차 — **G-BILLING-OVERDUE-ADJUSTMENT·G-STAFF-DOCUMENT-REPOSITORY·G-BATHING 전월 복사 접근성 재점검 + §73 신규** — 149차(§72)·UXD-149(`b969570`) 이후 coder 신규 커밋(`0420e6b` `OverdueManagementModal`·`03d0d43`/`fd15a2f` `StaffDocumentRepositoryPanel`·`9a957fb` `BathingSchedulePage` 전월 복사) 미점검 a11y·FE-16 갭 해소. ① **`OverdueManagementModal`** — 일시 `<time dateTime>`·폼 `aria-label` 2종. ② **`StaffDocumentRepositoryPanel`** — 업로드·lifecycle 링크 `${슬롯명}` `aria-label`·`aria-busy`·로딩 `role=status`·**`.ds-staff-document-repository*`** CSS 승격·`forced-colors` 요약 경계선. ③ **`BathingSchedulePage`** — 조회·전월 복사 `aria-busy`. ④ **§73** 신규. 회귀 +3. `npm test`·build PASS.)
> **이전 갱신**: 2026-06-21 (149차 — **G21 공단 일정 불일치·G15 카카오 API 잔여 대시보드 위젯 접근성 재점검 + §72 신규** — 148차(§71)·UXD-148(`e2f1246`) 이후 coder 신규 기능 커밋(`fe7df60`/`c01b880`/`ebc9f28` G21 nhisComparisonGap StatCard·`580a86b` G15 카카오 API 잔여 StatCard) 미점검 a11y·대비 갭 해소. ① **두 신규 위젯** — `StatCard` 값 텍스트(건수·「미설정」/「정상」/「확인」)+tone 병행으로 색 의존 없음·링크 sr-only·로딩 `role=status`·비표시 분기 모두 기존 `DashboardWidgetGrid` 패턴 준수(변경 불요). ② **강제 색상 모드 대비(WCAG 1.4.11)** — 앱 내 모든 `.ds-stat` 클러스터가 `forced-colors` 경계선을 명시하나 **주 US-M02 위젯 그리드만 누락** → `.ds-dashboard-widgets__item .ds-stat` `ButtonText` 경계선 신규(G21·카카오 위젯으로 그리드 조밀해져 효과 ↑). ③ **§72** 신규. CSS-only 대비 보강(JS 회귀 불요). build PASS.)
> **이전 갱신**: 2026-06-21 (148차 — **G-BILLING 입금·수납 대장 필터 UI 접근성 재점검 + §71 신규** — 147차(§70)·UXD-147(`1a614c9`) 이후 coder 신규 커밋(`e38ccfd` 입금 구간·수납 집계 기준 필터·`c6a412f` appliedFilters echo) 미점검 a11y·FE-16 갭 해소. ① **`BillingReportPage`** — 조회 `aria-busy={loading}`(WCAG 4.1.3·`BillingStatisticsReportPage` 패턴). ② **적용 조건 요약** — `role=status aria-live=polite`·대상월 `<time dateTime>`. ③ **`.ds-billing-report__applied-filters`** — 미정의 클래스 승격(FE-16)·`forced-colors`. ④ **§71** 신규. 회귀 +1. `npm test`·build PASS.)
> **이전 갱신**: 2026-06-21 (147차 — **G-STAFF-LEAVE-STATUS 휴직 상태 UI 접근성 재점검 + §70 신규** — 146차(§69)·UXD-146(`a7d9a2f`) 이후 coder 신규 커밋(`2581347` ON_LEAVE Badge·`StaffLifecycleSummaryPanel`·`StaffLifecyclePanel` 분기) 미점검 a11y 갭 해소. ① **`StaffLifecyclePanel`** ON_LEAVE `warning` Alert — "퇴사일 입력란은 비활성화됩니다." 문구 추가(disabled 입력 SR 미도달 보완·WCAG 4.1.2·1.3.1). ② **`StaffLifecycleSummaryPanel`** 신규 패널 — `section aria-labelledby`+`h2.ds-section-title`+`ds-stat-grid role=group`+`Alert role=status` 패턴 준수 확인(변경 불요). ③ **`Badge ON_LEAVE`** — tone=warning+"휴직" 텍스트 병행(WCAG 1.4.1). ④ **§70** 신규. `StaffLifecyclePanel.test.jsx` 11/11 PASS. `npm test` PASS.)
> **이전 갱신**: 2026-06-20 (146차 — **G-BANK-EXCEL-8·G-STAFF-NHIS-EXCEL-IMPORT preview·행 선택 UI 접근성 재점검 + §69 신규** — 145차(§68)·UXD-145(`a2f599c`) 이후 coder 신규 커밋(`a18b30e` 은행 입금 preview·행 선택·`4315ee2` 공단 요양보호사 import panel) 미점검 a11y·FE-16 갭 해소. ① **`BankDepositImportPanel`** — 폼 `aria-label`·미리보기 `role=group`·요약 `role=status aria-live=polite`·행 Checkbox `${예금주명} N행 선택`·입금일 `<time dateTime>`. ② **`StaffNhisCaregiverImportPanel`** — 동일 preview 패턴·`${성명} N행 선택`·생년월일 `<time dateTime>`. ③ **`.ds-bank-deposit-formats`** 미정의 클래스 승격(FE-16)·**`.ds-import-preview*`** 공통 레이어. ④ **§69** 신규·§68-4 잔여 FE wire 해소 표기. 회귀 +2. `npm test`·build PASS.)
> **이전 갱신**: 2026-06-20 (145차 — **G-BILLING-PRIOR-DEPOSIT-GUARD·US-H01 HQ 듀얼 대시보드 접근성 재점검 + §68 신규** — 144차(§67)·UXD-144(`08a8b9f`) 이후 coder 신규 커밋(`0d233b9` 청구 생성 선행입금 가드 StatCard·`c1ebaaf` HQ 듀얼 대시보드 nav·지점 요약 표·드릴다운·`a0f051d` L02_M15 테스트 안정화) 미점검 a11y·FE-16 갭 해소. ① **`HqBranchSummaryTable`** — 드릴다운 진행 중 조치 버튼 3종 `aria-busy={drilling}`(WCAG 4.1.3·`AttendancePage` 조회 패턴). ② **`HealthAlertList`** — HQ 지점 보기 버튼 `aria-busy={branchActionDisabled}`. ③ **`.ds-health-alert-list__action`** — 미정의 클래스 승격(FE-16)·`forced-colors` 목록 항목 경계선. ④ **`BranchCompareChart`** — 클릭 드릴다운 시 키보드 대안 안내(위 지점 요약 표 「지점 보기」·WCAG 2.1.1). ⑤ **`DashboardContextNav`**·**`CLAIM_GENERATION_GUARD_WIDGET_LABEL` StatCard** — `ds-context-nav`·`DashboardWidgetGrid` 표준 패턴 준수 확인(변경 불요). ⑥ **§68** 신규. 회귀 +2. `npm test`·build PASS.)
> **이전 갱신**: 2026-06-20 (144차 — **G14 급여제공계획서·직원 계정 요청 UI 접근성 재점검 + §67 신규** — 143차(§66)·UXD-143(`4e7d01d`) 이후 coder 신규 커밋(`22718d0` 직원 계정 생성 요청 흐름·`380be3c` 플랫폼 관리자 발급 폼 강화·`8ac0d01` 지역 선택기 검색 UX·`c37228d` 지점 주소 검증·`ce422e3` G14 급여제공계획서 10항목 폼·`d723d5a` 브랜치 스위처 인증 + 타이포그래피 토큰 조정) 미점검 a11y·FE-16 갭 해소. ① **`StaffPage` 계정 생성 요청 표** — `REQUEST_STATUS_LABELS` 평문 → **`StatusBadge`+`ACCOUNT_REQUEST_STATUS`**(승인 대기/승인됨/반려됨, 색+텍스트 병행·WCAG 1.4.1). ② **`StaffPage` 요청일 날짜 의미론** — `new Date().toLocaleString()` 평문 → **`<time dateTime>`**(88·89차 `StaffDetailPage` 패턴 정합·WCAG 1.3.1). ③ **`ClientCarePlanForm` 미정의 CSS 승격(FE-16)** — `.ds-care-plan-form`(최대 폭 래퍼)·`.ds-care-plan-form__heading`(lg 세미볼드 제목)·`.ds-care-plan-form__year-row`(연도 행 정렬)·`forced-colors` 경계선. ④ **`ds-form-grid--2` 신규** — 2열 고정 그리드 변형(`ClientCarePlanForm` 횟수·시간 2-필드 쌍 등). ⑤ **`ACCOUNT_REQUEST_STATUS`** — `Badge.jsx` + barrel `index.js` 추가. ⑥ **§3 타이포 토큰 실측 갱신** — `d723d5a`에서 `--font-size-*` 전체 소폭 상향(xs 0.75→0.8125 rem 등). ⑦ **§2-3 `ACCOUNT_REQUEST_STATUS` 매핑 추가**. ⑧ **§67** 신규. 회귀 없음(1866/369 PASS). `npm test`·build PASS.)
> **이전 갱신**: 2026-06-20 (143차 — **v1.3-A 이동서비스 배차 도구 접근성 재점검 + §66 신규** — 141차(§65)·UXD-142(`bd6e1c2`) 이후 coder 신규 커밋(`4681b5a` roster tools·ETA guardrails·`acc5933` route preview cache·compliance labels·`ba74bb5` Kakao map WIP·QA-B167/B170) 미점검 a11y·FE-16 갭 해소. ① **`TransportKakaoApiStatusPanel`** — Kakao Developers 콘솔 외부 링크 `target=_blank` 새 탭 안내 `ds-sr-only`(WCAG 3.2.5·G201·IntegratedHomeProviderDiscoveryPanel 패턴). ② **`TransportSuggestPanel`** — 동일 텍스트 「DRAFT 검토」행 링크에 차량번호 `aria-label` 부여(WCAG 2.4.4·StaffPage 목록 패턴). ③ 신규 모달(`TransportAddRosterModal`·`TransportConfirmWarningModal`·`TransportLoadPreviousRunModal`)·`KakaoTransportMapView`(marker `aria-label`·`role=application`·live summary) a11y 점검 — 변경 불요. ④ **§66** 신규. 회귀 +2. `npm test`·build PASS.)
> **이전 갱신**: 2026-06-20 (141차 — **FAQ21823 갱신 알림·CRUD·미정의 CSS 승격 + §65 신규** — 140차(§64)·UXD-141(`965e569`/`debe6dd`) 이후 coder 신규 커밋(`033b319` EmploymentContractRenewalAlertsPanel·재계약 CRUD·대시보드 due alerts·`1b6d2b1` 필수항목/서식 modal) 미점검 a11y·FE-16 갭 해소. ① **`EmploymentContractRenewalAlertsPanel`** — due-date `<time dateTime>`·알림 목록 `role=group`. ② **`StaffEmploymentContractRenewalPanel`** — 재계약 modal 저장 `aria-busy`·form `aria-label`. ③ **`.ds-section-title`·`.ds-subsection-title`·`.ds-checklist*`·`.ds-staff-employment-contract__template`** — StaffHrFilePanel·FAQ21823 미정의 클래스 승격. ④ **§65** 신규. 회귀 +2. `npm test`·build PASS.)
> **이전 갱신**: 2026-06-20 (140차 — **US-R03 FAQ21823 근로재계약 UI·현금영수증 identifier 검증 접근성 재점검 + §64 신규** — 139차(§63)·UXD-140(`501fedc`) 이후 coder 신규 커밋(`f62402f`·`10585b9`·`f31c346` FAQ21823 renewal panel/summary/dashboard widget·`76a462d` identifier digit validation) 미점검 a11y·FE-16 갭 해소. ① **`StaffEmploymentContractRenewalPanel`** — 기한 초과 Alert `id`+파일함 버튼 `aria-describedby`·`${직원명} 근로계약서 파일함` `aria-label`. ② **`StaffEmploymentContractRenewalSummaryPanel`** — 확인 필요 목록 링크 `${이름} 직원 상세` `aria-label`(StaffPage 패턴). ③ **`CashReceiptRegisterModal`** — 프로필 로드 중 발급 식별자 `aria-busy`. ④ **§64** 신규. 회귀 +4. `npm test`·build PASS.)
> **이전 갱신**: 2026-06-20 (139차 — **G26 yearBasis·G-7-1 Excel·현금영수증 pending guard 접근성 재점검 + §63 신규** — 138차(§62)·UXD-139(`17374f1`) 이후 coder 신규 커밋(`19ed7f3` G26 yearBasis+NTS CSV·`58d6694` G-7-1 Excel export·`99b795a`/`a2ef127` pending load guard) 미점검 a11y·FE-16 갭 해소. ① **`CashReceiptIssuancePage`** — pending load 실패 Alert `id`+「발급 등록」`aria-describedby`·수급자 탭 검색 `aria-busy`. ② **`BillingStatisticsReportPage`** — 의료비공제 StatCard `ds-grid--stats`·`.ds-segmented` `forced-colors`. ③ **`BillingStatementPrintPanel`** — PDF 버튼 `aria-label` 정합. ④ **`MedicalExpenseDeductionPanel`** — 조회 `aria-busy`. ⑤ **§63** 신규. 회귀 +3. `npm test`·build PASS.)
> **이전 갱신**: 2026-06-19 (138차 — **G-CASH-RECEIPT-LOG 4-계층 UI 접근성 재점검 + §62 신규** — 137차(§61) 이후 coder 신규 커밋(`cfc4b04`·`a17f148`·`221458e`·`8aebe55`) 미점검 a11y·FE-16 갭 해소. ① **`CashReceiptRegisterModal`** — 폼 Alert 검증→`Field error`+`aria-invalid`·form `aria-label`·작년분 경고 `id`+submit `aria-describedby`. ② **`CashReceiptIssuancePage`** — `StatusBadge`+`CASH_RECEIPT_IMMEDIATE_STATUS`·조회 `aria-busy`·`<time dateTime>`·`Select`·`ds-grid--stats`. ③ **`PaymentRecordModal`** — 현금 FAQ 21716 경고 `id`+submit `aria-describedby`. ④ **`CashReceiptLegalAlerts`** — FAQ 안내 `id`·`.ds-cash-receipt-legal-alerts`. ⑤ **§62** 신규. 회귀 +5. `npm test`·build PASS.)
> **이전 갱신**: 2026-06-19 (137차 — **G21 split-view NHIS comparison·G32 FAQ21797·G2 법정서식·케어포 3-1 nav + 미정의 CSS 승격 + §61 신규** — 136차(§60) 이후 coder 신규 커밋(`9b80505` G21 split-view NHIS comparison·`1d5747d` CareProvisionSegmentNav·`b272a7b` G32 attendee opinions·`d1149a5` G2 home newsletter/care record·`b881883` G39 SLA alerts) 미점검 a11y·FE-16 갭 해소. ① **`VisitNhisComparisonPanel`** — split-view PLAN/BILLING 2패널 동시 노출 시 h3「공단 명세 사전 비교」중복 → `{kindLabel} 공단 명세 사전 비교`(WCAG 2.4.6). ② **`VisitsPage`** — 분할 비교 래퍼 `role=group`+`aria-label`. ③ **`CaseManagementPage`** — 미정의 `ds-field__hint`→`ds-field__help`·폼 `aria-describedby`·참석자 fieldset hint 연결·행 수정 `aria-label`에 이용자명. ④ **`GuardianDocumentNotifyPanel`** — 서식 설명 `id`+submit `aria-describedby`·form `aria-label`. ⑤ **`DurationBandSelect`** — `ds-field__hint`→`ds-field__help`. ⑥ **`.ds-form-grid__full`** — FE-16 grid-column 전폭 span 승격. ⑦ **§61** 신규. 회귀 +4. `npm test`·build PASS.)
> **이전 갱신**: 2026-06-19 (136차 — **L03 간호기록 5종 행 수정 버튼 `Button` 컴포넌트 정합 + §60 신규** — 135차(§59) 이후 전수 점검에서 발견한 **미정의 `ds-table__action-btn` 잔여 5종** 해소. `NursingServiceRecordPage`·`NursingEmergencyRecordPage`·`NursingExcretionTubeRecordPage`·`NursingOralCareCheckPage`·`NursingWeightRecordPage`의 행 수정 버튼이 §35(110차)이 확립한 raw `ds-table__action-btn`→`Button variant=tertiary size=sm` 패턴을 따르지 않아 미정의 클래스로 포커스 링·`forced-colors`·hover 토큰을 못 받던 회귀를 해소(FE-16·WCAG 4.1.2). `aria-label`·동작 불변. 회귀 +5(`ds-btn` 클래스 단언). 5파일 32 tests PASS. **§60** 신규.)
> **이전 갱신**: 2026-06-19 (135차 — **G41 filter-year Field controlProps 전달 + RFID no-diff SR 중복 제거 + G-7-1 인쇄 패널 CSS + §59 신규** — 134차(§58) 이후 잔여 a11y·FE-16 갭 해소. ① **`StaffTrainingLogPage`** — invalid filter year 시 `Field help`(준수 현황 숨김 안내)를 error와 **동시 노출**·`aria-describedby` 병합(134차 help 조건부 제거 회귀 해소·WCAG 3.3.2). ② **`VisitRfidDiffComparePanel`** — no-diff 시 info+success 이중 `role=status` 제거→단일 success Alert(`id=visit-rfid-diff-no-diff-alert`·행 수+no-diff 병합). ③ **`.ds-billing-statement-print`** — 미정의 베이스 클래스 승격(상단 구분선·`forced-colors`). ④ **`BillingStatementPrintPanel`** PDF 버튼 `aria-label`. ⑤ **§59** 신규. 회귀 +2. `npm test`·build PASS.)
> **이전 갱신**: 2026-06-19 (134차 — **G21 standalone NHIS comparison panel·G41 filter-year 접근성 재점검 + 미정의 CSS 승격 + §58 신규**
> **이전 갱신**: 2026-06-18 (132차 — **G15 별지 제22호 branch contact·입력 폼 compliance Badge + SideNav §8-2 비주얼 deepen 문서화 + §56 신규**
> **이전 갱신**: 2026-06-18 (130차 — **G15 이동서비스일지 운전자 서명 fieldset 그룹화 + 미정의 `ds-transport-log__*` CSS 클래스 해소 + §54 신규** — 129차(§53) 이후 coder 신규 커밋(`b6ce301` 건강검진 HR파일허브 연결·`b4644e8` 법정 서류 필드 검증·`0df6902` 이동서비스일지 법정 가이드·`f51e365` 운전자 서명 persist·`1c8f236` 식사기록 클라이언트 정규화) 미점검 갭 해소. ① **`TransportServiceLogPanel` 운전자 서명 `fieldset`/`legend`(WCAG 1.3.1)** — 「서명 성명」·「서명일」두 필드가 서로 의존하는 쌍이지만 그룹 시맨틱 없이 독립 `Field`로 나열돼 SR이 어떤 서명인지 맥락 없이 식별해야 했던 갭을, `fieldset.ds-transport-log__signature-group`+`legend="운전자 서명"`으로 그룹화(Field 라벨은 「서명 성명」·「서명일」로 단축·중복 제거). ② **`components.css` 미정의 클래스 해소(FE-16)** — `TransportServiceLogPanel`이 사용하나 CSS에 없던 `ds-transport-log__document`(본문 래퍼 패딩·보더·배경)·`ds-transport-log__heading`(별지 제22호 제목)·`ds-transport-log__summary`(운행 메타 dl 그리드)·`ds-transport-log__footnote`(보관 각주)·`ds-transport-log__no-print`(인쇄 숨김 유틸)·`ds-transport-log__actions`(액션 바 상단 여백)·`ds-transport-log__meta`(메타 폼 row)·`ds-transport-log__signature-group`(서명 fieldset 리셋) 8종 정의. ③ `forced-colors` — `ds-transport-log__document`에 `ButtonText` 경계선 추가. ④ **§54** 신규. 회귀 +2(`TransportServiceLogPanel.test.jsx` 서명 fieldset 라벨 갱신). `npm test` **1677/344** PASS · build PASS.)
> **이전 갱신**: 2026-06-18 (129차 — **US-T05 배차 명단 계획 픽업·US-R02 FAQ21799 신규 서류·L02_M13 malformed 응답 접근성 재점검 + §53 신규** — 128차(§52) 이후 coder 신규 커밋(`e35efb2` 배차 명단 확정 루트·계획 픽업·지연 Badge·`8e6310a` FAQ21799 신규직원 건강검진 1년 서류·`38642e2` L02_M13 malformed API 응답) 미점검 갭 해소. ① **`TransportPage` 명단 표** — 배차 루트 `Link`에 `${이용자명} N번 정차` `aria-label`(WCAG 2.4.6·다중 행 동일 링크 텍스트 구분)·계획 픽업 지연 시 `title` 툴팁 제거→가시 **「지연」** Badge+`aria-label` 병행(§51 `TransportStopList` 패턴)·`.ds-inline-cluster` 신규 정의(FE-16). ② **`StaffHealthCheckupsPage`** — `NEW_HIRE_DOCUMENT_STATUS.NA` 분기가 `aria-hidden`으로 SR에서 숨기던 결함을 `ds-text-muted` 「—」로 정합(WCAG 4.1.2). ③ **`MealAssistanceRecordPage`** — 미정의 `ds-help-text`→`ds-text-muted`·`ds-visually-hidden`→`ds-sr-only`(표 작업 열 헤더). ④ **§53** 신규. 회귀 +2. `npm test`·build PASS.)
> **이전 갱신**: 2026-06-17 (127차 — **커스텀 DateInput/TimeInput 피커 + G15 경유지·ETA 칩 접근성 재점검 + §51 신규** — 126차(§50) 이후 coder 신규 커밋(`ea5d896` 커스텀 date/time picker·`bf73c4c` 경유지 모달·ETA 칩·`96db8bf` 배차 레이아웃) 미점검 갭 해소. ① **`DateInput`/`DatePickerCalendar`** — 팝오버 열림 시 선택일(또는 오늘) 포커스·닫힘 시 트리거 복귀·`Field` `labelId`→dialog `aria-labelledby`·이전/다음 달 **비표시 일자 `disabled`**(혼동 방지). ② **`TimeInput`** — `role="group" aria-labelledby` 복합 필드·시/분 `Select`에 개별 `id`·`aria-describedby`는 그룹 단위. ③ **`Field`** — `<label id>`·`labelId` controlProps·단일 React 자식 `cloneElement`로 `aria-*` 자동 전달(render-prop 미사용 페이지 정합). ④ **`TransportAddWaypointModal`** — 주소 미입력 시 폼 상단 `Alert`→**`Field error`**+`aria-invalid`(WCAG 3.3.1). ⑤ **`TransportStopList`** — 지연 ETA 칩에 가시 **「지연」** 텍스트 라벨 추가(색+텍스트·WCAG 1.4.1). ⑥ **CSS** — `.ds-transport-stop__time-chip-status`·`forced-colors` date/time picker·지연 칩 경계선. 회귀 +5. `npm test`·build PASS.)
> **이전 갱신**: 2026-06-17 (126차 — **`MaskedPhone` 비대화형 span `aria-label` 안티패턴 제거 (WCAG 4.1.2·1.3.1·결정 96 회귀)** — 125차(§50) 이후 coder 신규 커밋 `0baabe9`(결정 96 — 이용자 목록·상세에 본인 연락처 `phoneMasked`·대표 보호자 연락처 컬럼 노출) 미점검 갭 해소. 신규로 `ClientListPage` 표(컬럼 헤더 「연락처」·「보호자 연락처」)와 `ClientDetailPage` `<dl>`(`<dt>연락처</dt>`·`<dt>보호자 연락처</dt>`)에서 `MaskedPhone withLink={false}`가 다수 사용됐는데, 이 분기는 **비대화형 `<span>`(role=generic)에 `aria-label="연락처 {번호}"`를 하드코딩**하고 있었다. ① **ARIA 안티패턴(WCAG 4.1.2)** — `aria-label`은 role 없는 generic `<span>`에서 스크린리더 노출이 보장되지 않아(ARIA 1.1 — 대화형/role 보유 요소에서만 신뢰) 의도한 라벨이 전달되지 않을 수 있고, ② **중복·불일치(WCAG 1.3.1)** — 라벨 컨텍스트는 이미 표 `scope="col"` 헤더(「연락처」·「보호자 연락처」)·`<dt>`(「전화번호」 등)가 제공하므로 「연락처 …」 하드코딩 라벨은 **본인 연락처에선 중복**, **보호자 연락처 열·`GuardianDetailPage` 「전화번호」 `<dt>`에선 불일치**(span은 일괄 「연락처」만 노출). 가시 마스킹 텍스트(`010-****-1234`)가 이미 접근 가능한 콘텐츠이므로, no-link span 분기의 `aria-label`을 제거해 주변 시맨틱 라벨이 컨텍스트를 제공하도록 정합(`tel:` 링크 분기의 「전화 걸기 …」 dialing 라벨은 `<a>`에서 유효 — 유지). 컴포넌트 단일 원천 수정이라 6개 소비처(`ClientListPage`·`ClientDetailPage`·`GuardiansPage`·`GuardianDetailPage`·`TransportPickupContact` 등) 전체에 일관 적용. 순수 접근성 정합 리팩터로 가시 텍스트·마스킹·동작·`tel:` 링크 불변. 회귀 +1(`MaskedPhone.test.jsx` — no-link span `aria-label` 부재 단언). `npm test` 1612/1612 PASS·build PASS.)
> **이전 갱신**: 2026-06-17 (125차 — **G15 이동서비스일지 감사추적 + 모니터링/간호 연계 패널 토큰 정합 + §50 신규** — 124차(§49) 이후 coder 신규 커밋(`3cc5a08` G15 일지 감사추적 read API·`8b68fdb` `MonitoringEvidenceContextPanel`(BNK-273)·`140bf92` `CareNursingParityPanel`) 미점검 갭 해소. 신규 패널 2종은 `aside`/`nav` landmark·`aria-label`·`role="status"`·`ul/li`를 이미 갖춰 접근성 결함 없음 — 잔여는 **토큰 단일 원천(§1-4·FE-16) 회귀 2건**. ① **`TransportServiceLogPanel` 미정의 클래스 제거** — 감사·본문 빈 상태 안내 `<p>`가 `components.css` **미정의 `ds-empty-hint`**(소비자 이 컴포넌트 단 1곳)로 색·`forced-colors` 토큰을 못 받던 80·90·97차 패턴 회귀를, 정의된 **`ds-text-muted`**(`--color-text-muted` 4.76:1 + `forced-colors`에서 `--color-text-secondary` 승격)로 교체(2곳). ② **신규 패널 CSS raw rem → `--space-*` 토큰** — `.ds-monitoring-evidence-context*`·`.ds-care-nursing-parity*`의 `gap: 0.5rem`·`0.75rem 1rem`을 `var(--space-2)`·`var(--space-3) var(--space-4)`로 교체(118·120차 토큰화 패턴 정합). 순수 정합 리팩터로 동작·데이터 불변. `npm test` 1605/1605 PASS·build PASS.)
> **이전 갱신**: 2026-06-17 (124차 — **US-T05 G15 이동서비스 월간 리포트(2-7/2-8) `TransportMonthlyReportsPage` 접근성 재점검 + §49 신규** — 123차(§48) 이후 coder `6a18dfd`(G15 2-7/2-8 월간 변동·입소자 현황 신규 페이지) 미점검 갭 해소. 같은 시기 신설 `BillingStatisticsReportPage`(G26)와 구조가 동일한 리포트 페이지인데 그 페이지가 확립한 표준을 따르지 않아 발생한 회귀 3건 정합. ① **섹션 헤딩 레벨(WCAG 1.3.1·2.4.6)** — 두 섹션 제목이 `Card` `h2` 내부에서 `h2`로 중복돼(§44/116차 패턴 회귀) AppShell `h1` → Card `h2` → 섹션 **`h3`**로 정정. ② **StatCard 요약 그룹 시맨틱(WCAG 1.3.1)** — 변동현황·입소자현황 StatCard 래퍼 `div` 2건에 `role="group" aria-label="…요약"` 부여(§42·93차 패턴). ③ **조회 버튼 `aria-busy`(WCAG 4.1.3)** — `disabled`만 있고 진행 상태를 SR에 전달하지 못하던 갭을 `aria-busy={loading}`로 보강(`BillingStatisticsReportPage` 정합). ④ **그리드 정합** — StatCard 그리드 `ds-grid--stats`(160px·5칸 입소자 요약 정렬) + `.ds-transport-monthly-report__summary` `forced-colors` 경계선 신규. ⑤ **§49** 신규. 순수 접근성 정합 리팩터로 데이터·API·동작 불변. 회귀 — `TransportMonthlyReportsPage.test.jsx` heading level 3·StatCard group 단언 추가. `npm test` 1596/1596 PASS·build PASS.)
> **이전 갱신**: 2026-06-17 (123차 — **US-T05 G15 TransportServiceLogPanel PUT wire 접근성 재점검 + `TRANSPORT_TIME_COMPLIANCE_STATUS` Badge + §48 신규** — 122차(§47) 이후 coder `7a4b310` G15 별지 제22호 일지④ `PUT /transport/runs/{runId}/service-log` FE wire 미점검 갭(QA-B116) 해소. ① **정차별 필드 `aria-label` 컨텍스트(WCAG 2.4.6)** — 복수 `fieldset`에서 「실제 픽업」·「동승 여부」 라벨이 중복돼 SR이 대상 수급자를 식별 못 하던 결함을 `${clientName} 실제 픽업` 등 이용자명 포함 라벨로 보강. ② **시간 준수 열 색 의존 제거(§1-2)** — `td` 색상 클래스(`ds-transport-log__compliance--*`) → **`StatusBadge`+`TRANSPORT_TIME_COMPLIANCE_STATUS`**(준수/지연/미기록/계획없음, 색+텍스트·`forced-colors` 경계선). ③ **미확정 배차 가드 `aria-describedby`** — 인쇄·텍스트 저장 버튼을 `#transport-log-unconfirmed-warning`에 연결. ④ **기록 섹션 시맨틱** — `section`+sr-only `h3`「정차별 실제 기록」·요약 `role=status`·표 `captionVisuallyHidden`. ⑤ **CSS** — `legend` `font-weight: 600` → `var(--font-weight-semibold)`·`forced-colors` fieldset 경계선·미사용 compliance 색 클래스 제거. ⑥ **§48** 신규. 회귀 +1. `npm test`·build PASS.)
> **이전 갱신**: 2026-06-17 (122차 — **US-E04 QrCheckinTargetsPanel + §44 공통 클래스 페이지 연동 + `--color-accent` 토큰 + US-T02 split-view·정차 목록 a11y 재점검 + §47 신규** — QA-B115 transport split-view(`d3bef42` map pins/Korean geocode) 이후 미점검 갭 해소. ① **지점(센터) 핀 스크린리더 라벨 결함(WCAG 1.1.1·4.1.2)** — 마커 핀 `aria-label`이 `${pinLabel}번 정차`로 일괄 생성돼, `orderNumber`가 없는 **지점 핀**(`markerPinLabel`이 배지 텍스트 「센」 반환)이 SR에 「**센번 정차**」라는 무의미한 이름으로 읽히던 결함을, `markerPinAriaLabel(point)`로 분리해 지점 핀은 「지점(센터) 정차」·번호 정차는 「N번 정차」로 노출. ② **배지 텍스트 SR 중복 제거** — 핀 내부 시각 배지(`__badge` 「센」/숫자)에 `aria-hidden="true"`를 부여해 버튼 `aria-label`만 읽히도록 정합(시각 표기 불변). ③ **범례 색·기호 의미 정합(§1-2·WCAG 1.4.1)** — 정적 범례가 「파란 선 = 도로 경로」로 고정돼 도로 경로 미리보기가 없을 때 실제 표시되는 **회색 점선 정차 안내선**(`paintStopGuideLine`)과 불일치하고, 지도에 등장하는 「센」 지점 핀을 설명하지 못하던 갭을, `roadPath` 유무에 따라 「파란 선 = 도로 경로」/「회색 점선 = 정차 안내선」을 분기하고 「숫자 핀 = 정차 순서 · "센" 핀 = 지점(센터)」를 명시해 시각·SR 모두 기호 의미를 식별하도록 보강. 순수 접근성 정합 리팩터로 지도 동작·마커 위치·시각 배지 불변. 회귀 +1(`KakaoTransportMap.test.jsx` — 지점/번호 핀 `aria-label`·「센번 정차」 부재·범례 텍스트 검증). 단독 `KakaoTransportMap.test.jsx` 4/4 PASS·build PASS. **주의**: 본 변경은 committed `d3bef42`(WT clean 파일)만 수정 — coder QA-B115 transport WT dirty(14M+1untracked: `TransportRouteSplitView`·`TransportStopList`·`components.css` 등)는 coder commit→push 영역이라 미수정.)
> **이전 갱신**: 2026-06-16 (120차 — **US-T02 Kakao map instance 중앙화 + 비교 레이아웃 CSS + 토큰 위반 해소 + §46 신규** — QA-B114 WIP(coder `b000d92` 이후 dirty tree) 맥락에서 미점검 갭 해소. ① **`ds-transport-map__canvas` `background: #f2f2f2` raw hex → `var(--color-surface-muted)` 교체(FE-16·§1 단일 원천 복구)**. ② **`.ds-transport-map-compare__label` `font-weight: 600` → `var(--font-weight-semibold)` 토큰화**. ③ **신규 CSS 4클래스** — `ds-transport-map__canvas-wrap`·`ds-transport-map-compare`·`ds-transport-map-compare__pane`·`ds-transport-map-compare__label`·`ds-transport-map-compare__status`. ④ **`KakaoTransportMapView.mapEnabled` prop** — SDK ready 이전 렌더링 방지·`seedMarkers` 좌표 기반 선행 마커 표시 패턴 문서화. ⑤ **`KakaoBareMap`·`kakaoMapInstance.js`·`useKakaoMap`** 신규 컴포넌트·훅 패턴. ⑥ **§46** 신규. 회귀 — 1537/1538 PASS(1 pre-existing jsdom 오염 — 단독 PASS·본 변경 무관)·build PASS.)
> **이전 갱신**: 2026-06-16 (119차 — **L03 care-scoped 간호 리포트 서브 네비 + G21 split-view 후속 UI 접근성 재점검 + §45 신규** — 118차(§44) 이후 coder 신규 커밋(`58ee122` L03_M09/M10/M14 `CareNursingServiceReportPage`·`CareNursingServiceReportNav`·`4c9103d` G21 청구반영 요약 칩·`cb457b7` G21 미반영 후속 확인 목록) 미점검 갭 해소. ① **`.ds-context-nav--sub` 미정의 클래스 해소(FE-16·§1 단일 원천)** — `CareNursingServiceReportNav`가 `ds-context-nav--sub` 클래스를 사용했으나 `components.css` 미정의였던 갭을, 서브 링크 `xs` 글자크기·`control-height-sm` 최소 높이·`surface-muted` 기본 배경으로 정의해 상위 컨텍스트 네비 대비 시각 계층 분리(80차 `.ds-text-input` 패턴 회귀 해소). ② **`CareNursingServiceReportPage`** — 필터 폼 `aria-label`·조회 `aria-busy`·`NursingServiceReportPanel`(`role=group` StatCard·`captionVisuallyHidden` 3표·`scope=col`) 정합 확인(변경 불요). ③ **`VisitsPage` G21 split-view** — 청구반영 요약 `role=group aria-label` + 후속 확인 `section aria-label`+`ul/li`+상태 텍스트 라벨 병행(색만 의존 금지) 정합 확인(변경 불요). ④ **§45** 신규. 회귀 — `npm test` 1526/1526 PASS·build PASS.)
> **이전 갱신**: 2026-06-16 (118차 — **USER_STORIES 미완료 화면군 공통 스타일 보강 + 토큰 변수 불일치 회귀 해소 + §44 신규** — 117차(§43) 이후 USER_STORIES 미완료 항목(US-A01 `/platform`, US-H01 `/dashboard`, US-E01 `/attendance/checkin`, US-E04 `/guardian/checkin`) 대비 공통 스타일 보강. ① **토큰 변수 정합** — `.ds-transport-log__*`에 남아 있던 비표준 `--ds-*` 변수 11건을 `--space-*`·`--font-size-*`·`--color-*`·`--radius-*`로 교체(단일 토큰 원천 복구). ② **누락 화면군용 공통 레이어** — `.ds-role-home-grid`·`.ds-role-home-card*`(역할별 대시보드 카드), `.ds-attendance-actions`(수기 출석 액션), `.ds-qr-checkin-targets*`(보호자 QR 대상 선택), `.ds-platform-org-form__group`(플랫폼 온보딩 폼 그룹) 추가. ③ **문서 동기화** — §44에 적용 범위·접근성 기준·coder 전달 메모 반영.)
> **이전 갱신**: 2026-06-16 (116차 — **L02_M11/M12/M06/M17/M16·G21 리포트 접근성 재점검 + §42 신규** — 115차(§41) 이후 coder 신규 커밋(`ff9c8c5` L02_M11/M12·`fa20943` L02_M06/M17·`8b804fc` L02_M16·`25ca88e` G21 청구반영 배지) 미점검 갭 해소. ① **신규 리포트 4종 `Table` caption 보강(WCAG 1.3.1)** — `PatientServiceReportPage`(5표)·`IntensiveExcretionReportPage`(1표)·`PositionChangeReportPage`(2표)·`ServiceSummaryReportPage`(1표) 각 `<Table>` 컴포넌트가 `caption` 없이 렌더돼 스크린리더 표 탐색 시 이름이 없던 갭을, 각 카드 제목과 대응하는 `captionVisuallyHidden caption` 부여로 해소(`NursingServiceReportPanel`·`MonitoringSelfDiagnosisPage` 패턴). ② **StatCard 요약 그룹 `role="group"`** — 4개 리포트 페이지의 StatCard 래퍼 `div`가 그룹 시맨틱 없이 독립 카드들을 나열해 SR이 집계 목적을 식별 못 하던 갭을, `role="group" aria-label="{리포트명} 요약"`으로 보강(93차 `StaffStatusReportPage`·`ComplaintConsultationPanel` 패턴). ③ **`VisitsPage` 청구반영 상태 Alert 색 의존 제거(§1-2)** — G21 청구반영 배지 안내 `Alert`가 「검은 배지」·「빨간 배지」라는 **색상 명칭**으로 상태를 설명해 색 의존 금지 원칙(WCAG 1.4.1) 위반이던 갭을, 색 언급을 제거하고 배지 텍스트 라벨(「청구반영」·「미반영」·「페어 없음」)만으로 안내하도록 수정(배지 자체는 이미 텍스트+색 병행 `BILLING_CLAIM_REFLECTION_STATUS`). ④ **`ds-badge--dark` `forced-colors` 경계선** — 새 `tone="dark"` 배지가 `forced-colors` 모드에서 배경 소거 시 텍스트와 구분이 안 되던 갭을, `outline: 1px solid ButtonText` + `forced-color-adjust: none`으로 다른 Badge 토큰과 정합. ⑤ **`VisitsPage.test.jsx` 회귀** — G21 테스트가 이전 색 명칭을 단언하던 1건을 새 텍스트 라벨(`/청구반영 상태 안내:/`·`getAllByText`)로 갱신. ⑥ **§42** 신규. 회귀 — `VisitsPage` 10/10 PASS·보고서 4종 8/8 PASS·전체 `npm test` 1490/1490 PASS·build PASS.
> **이전 갱신**: 2026-06-16 (115차 — **v1.3-A 배차 Kakao 경로 미리보기 지도 + L02_M04/M05 리포트 인쇄 a11y 재점검 + §41 신규** — 114차(§40) 이후 coder 신규 커밋(`0c523cd`/`15e9b64`/`d46688d` 배차 Kakao route-preview 지도·`d2145b0` L02_M04/M05 리포트 인쇄) 미점검 갭 해소. ① **`.ds-transport-map__summary` 신규 정의(FE-16·§1 단일 원천)** — `KakaoTransportMap`이 도로 경로 거리·소요시간 요약을 이 클래스로 렌더하나 `components.css` **미정의** → `ds-text-secondary`로 색만 받고 상단 여백·글자크기 토큰을 못 받던 80차 `.ds-text-input` 패턴 회귀를, `margin`·`--font-size-sm` 정의 + `:empty{display:none}`로 해소. ② **경로 요약 라이브 영역(WCAG 4.1.3)** — 지도 캔버스는 `role="img" aria-label="배차 경로 지도"`라 비시각 사용자에게 도로 거리·소요시간을 전달하지 못했고, 요약 `<p>`가 **조건부 마운트**라 비동기 경로 계산 완료 시 안내되지 않던 갭을, 71차 `FeeSurchargeGuidePanel` 패턴대로 **상시 상주 `role="status" aria-live="polite"`** 컨테이너로 전환(`:empty` 숨김으로 빈 상태 시각 회귀 방지). ③ **L02_M04/M05 인쇄 출력(`d2145b0`) 점검** — 인쇄 전용 헤더 `aria-hidden="true"`·`.ds-care-report-print-only`/`__filters`/`-print-root` 정의·필터 폼 `aria-label`·`Button aria-busy`·StatCard·Table `scope=col` 정합 확인(변경 불요). ④ **§41** 신규. 회귀 — transport 13파일 40 PASS. `npm test` 1457/1460 PASS(3 pre-existing 전체실행 jsdom 오염 — 단독 PASS·본 변경 무관)·build PASS.)
> **이전 갱신**: 2026-06-16 (114차 — **통합식사도움·특이사항·요양 리포트 a11y 재점검(§40)** — coder `9ad8346`(L02_M13)·`3549896`(L02_M15)·`c5f82a6`(L02_M04/M05) wire 직후 `MealAssistanceRecordForm` `applyApiErrorToForm` 객체 시그니처 교정·`<form aria-label>`·`.ds-care-special-notes-form__intro` 신규 정의·`.ds-muted`→`.ds-text-muted` 정합.)
> **이전 갱신**: 2026-06-16 (113차 — **L02_M01·L02_M03·G-7-1-4CHANNEL UI 접근성 재점검 + 미정의 디자인 토큰 클래스 보강 + §37~§39 신규** — 112차 이후 coder 신규 커밋(`41b2123` L02_M01 주간 제공기록·`950415d` L02_M03 목욕 일정·`1fd1434` G-7-1-4CHANNEL 명세 발송) 미점검 갭 해소. ① **`.ds-care-weekly-form__intro`**·**`.ds-bathing-schedule-form__intro`** — §36 `.ds-body-restraint-form__intro`와 동일 전폭 스팬 정의. ② **`CareServiceWeeklyRecordForm`·`BathingScheduleForm`** — 제출 `aria-busy` 보강(§35·§36 패턴). ③ **`BillingStatementDispatchPanel`** — quiet-hours 가드 `aria-describedby`를 비활성 발송 버튼에 연결(101차 `BillingDetailPage` 패턴)·페이지 가드 `id` 전달 시 중복 Alert 제거·행별 「발송일 수정/저장/취소」`aria-label`에 이용자명 포함·발송일 `<time dateTime>`·우편 발송일 `DateInput max=오늘`·`applyApiErrorToForm` 객체 시그니처 정합. ④ **`.ds-billing-statement-dispatch*`** CSS·`forced-colors` Badge 경계선. ⑤ **§37~§39** 신규. 회귀 +4. `npm test`·build PASS.)
> **이전 갱신**: 2026-06-16 (112차 — **L02_M07 신체제재 기록 UI 접근성 재점검 + 미정의 디자인 토큰 클래스 보강 + §36 신규** — 111차 이후 coder 신규 커밋(`14a2bb9` L02_M07 신체제재 wire) 미점검 갭 해소. ① **`.ds-body-restraint-form__intro`** — `BodyRestraintRecordForm`이 참조하나 `components.css` **미정의** → L02_M02 `.ds-nursing-excretion-form__intro`와 동일하게 `grid-column: 1 / -1` 전폭 스팬 정의(인트로 안내 배너가 `ds-form-grid` 단일 컬럼에 갇히던 시각 회귀 해소). ② **`BodyRestraintRecordForm`** 제한일 `DateInput max=오늘`(미래 일자 차단·L02_M02 패턴 정합·인권 기록 정합성). ③ **§36** 신규. `npm test`·build PASS.)
> **이전 갱신**: 2026-06-15 (111차 — **L02_M02 집중배설관찰 UI 접근성 재점검 + 기록 화면 공통 레이아웃 CSS 승격 + §35 신규** — 110차 이후 coder 신규 커밋(`1264c16` L02_M02 집중배설관찰 wire) 미점검 갭 해소. ① **`IntensiveExcretionObservationPage`** — 수정 행 raw `<button className="ds-table__action-btn">` → **`Button variant=tertiary size=sm`** 전환(110차 `CareProvisionRecordPanel` 패턴 정합·WCAG 4.1.2). ② **기록 화면 공통 레이아웃 CSS 승격(FE-16·§1 단일 원천)** — `ds-page-stack`·`ds-page-grid`·`ds-page-grid--sidebar`·`ds-page-loading`·`ds-table__row--highlighted`가 L02_M02·L03_M01·L03_M06·L03_M08·L03_M09·L03_M10·L03_M14 등 다수 기록 페이지에서 사용됐으나 `components.css` 미정의(`forced-colors` `outline` 포함). ③ **§35** 신규. 회귀 +1(`IntensiveExcretionObservationPage.test.jsx` — 수정 버튼 `ds-btn` 클래스·`aria-label` 검증). `npm test`·build PASS.)
> **이전 갱신**: 2026-06-15 (110차 — **G19 통합재가 기관 검색 패널 + G39 기록지 발송 + G30 증빙 기간 접근성 재점검 + §32~§34 신규** — 109차 이후 coder 신규 커밋(`9afa30e` G19·`4d1a4f2`/`73094f9` G39 dispatch·`73094f9` G30 evidence window) 미점검 갭 해소. ① **`IntegratedHomeProviderDiscoveryPanel`** — 미정의 `__meta` div 래퍼 제거 → **`.ds-dl-grid`**(FE-16)·`code.ds-mono`·외부 링크 `aria-label`+sr-only 「(새 탭)」·`.ds-integrated-home-discovery` CSS·`forced-colors` 경계선. ② **`ProvisionResultDispatchPanel`** — 행별 발송 `Button` **`aria-label`에 이용자명·연월 포함**(WCAG 2.4.6)·상태 열 **`Badge tone=warning`「미제공」**(색+텍스트). ③ **`CareProvisionRecordPanel`** — raw `<button>` → **`Button`**·조회 `aria-busy`·일자 `<time dateTime>`. ④ **`MonitoringIntegratedChecklistPanel`** — 증빙 수집 기간 `id`+`role=status`·`.ds-monitoring-checklist__evidence-window`. ⑤ **§32~§34** 신규. 회귀 +5. `npm test`·build PASS.)
> **이전 갱신**: 2026-06-15 (109차 — **US-T09 G24b 연간 욕구사정 현황 페이지 신설(`NeedsAssessmentStatusPage`) + 대시보드 위젯 목적지 연결 + §31 신규**
> **이전 갱신**: 2026-06-15 (108차 — **US-T09 G24b 욕구사정 8+5항목 폼 접근성 재점검 + §30 신규** — 107차 이후 coder 신규 커밋(`49fbf67` G24b 5필드 FE wire) 미점검 갭 해소. ① **`ClientNeedsAssessmentForm`** — FAQ 21800·G24b FAQ 21810 **`fieldset`/`legend` 2그룹 분리**(WCAG 1.3.1)·`Field help`→`aria-describedby`·제출 `aria-busy`·폼 `h3` `aria-labelledby`. ② **`ClientNeedsAssessmentPanel`** — outer `section` `aria-label` 정합(`ClientBenefitContractPanel` 패턴)·필드 안내 `role=region`. ③ **`ClientNeedsAssessmentCompare`** — 변경 행 **`Badge`「변경」**(색+텍스트)·`.ds-table__row--changed` 좌측 보더·`forced-colors` outline. ④ **CSS** — `.ds-needs-assessment-form*`·`.ds-needs-assessment-compare*`. ⑤ **§30** 신규. 회귀 +4. `npm test`·build PASS.)
> **이전 갱신**: 2026-06-15 (107차 — **US-O05 G-ONBOARD-SUPPORT 지점 도입 체크list UI 신설 + §29 신규 + §2-3 `ONBOARDING_SESSION_STATUS`** — planner 140차 P2 갭(US-O05 BE @ `735dd53`·FE wire ❌) 해소. ① **`BranchOnboardingSupportPanel`** — silverangel businessSupport 1~4회차 checklist·오픈일 `DateInput`+`Field`·역할별 `fieldset`/`legend`·`Checkbox`·회차별 `PATCH`·`ONBOARDING_SESSION_STATUS` Badge(색+텍스트)·기한 초과 좌측 보더·`ds-grid ds-grid--stats` 요약. ② **`BranchesPage`** — 행별 「도입 체크list」`Modal`(hq_admin·branch_admin·social_worker)·`aria-label`에 지점명. ③ **API** — `fetchBranchOnboardingSupportApi`·`upsertBranchOnboardingSupportApi`·`updateBranchOnboardingSupportSessionApi`. ④ **CSS** — `.ds-branch-onboarding-support*`. ⑤ **§29** 신규. 회귀 +4. `npm test`·build PASS.)
> **이전 갱신**: 2026-06-14 (106차 — **L03_M07/M09/M10·L03_M15 리포트 UI 접근성 재점검 + §27·§28 신규 + §8-1 간호 라우트 보강** — 105차 이후 coder 신규 커밋(`2a05271`·`75bddee`·`efa4472`·`89dc52d` L03_M07/M09/M10 `NursingServiceReportsPage`·L03_M15 `PressureUlcerProvisionReportPanel`·`NursingContextNav` 12링크) 미점검 갭 해소. ① **`PressureUlcerProvisionReportPanel`** — `aria-labelledby` 대상 **`h3` 누락** 회귀 해소·`aria-busy`·로딩 중 EmptyState 미노출·`<time dateTime>`·NPUAP 단계 `StatusBadge`(숫자·코드 정규화)·`ds-grid ds-grid--stats`+`role=group`. ② **`NursingServiceReportPanel`/`Nav`** — forced-colors StatCard 경계선·서브 네비 landmark 회귀. ③ **CSS** — `.ds-nursing-service-report*`·`.ds-pressure-ulcer-provision-report*`. ④ **§8-1** — `/nursing/*` 14경로 추가. ⑤ **§27 L03_M07/M09/M10**·**§28 L03_M15** 신규. 회귀 +4. `npm test`·build PASS.)
> **이전 갱신**: 2026-06-14 (105차 — **US-O04 L03_M01·L03_M06 간호급여 제공기록·배설/경관 UI 신설 + §25·§26 신규** — planner 138차 P1 갭(L03_M01/M06 FE wire ❌) 해소. ① **L03_M01** — `NursingServiceRecordForm`(3-flag `fieldset`+`legend`·최소 1개 제공 검증)·`NursingServiceRecordPage`·`/nursing/service`·`services.js` CRUD. ② **L03_M06** — `NursingExcretionTubeRecordForm`·`NursingExcretionTubeReportPanel`(StatCard×4)·`NursingExcretionTubeRecordPage`·`/nursing/excretion-tubes`·report API. ③ **`NursingContextNav`** — 제공기록·배설·경관 2링크 추가(10 route). ④ **CSS** — `.ds-nursing-service-form__provision*`·`.ds-nursing-excretion-*`·`forced-colors`. ⑤ **§25 L03_M01**·**§26 L03_M06** 신규. 회귀 +18. `npm test`·build PASS.)
> **이전 갱신**: 2026-06-14 (104차 — **L03_M14 체중 기록 폼 `aria-describedby` 덮어쓰기 회귀 해소(WCAG 3.3.1·1.3.1·FE-16)** — 103차 이후 coder 신규 커밋(`a7f97a6`·`962858b`·`c60d7e5`·`8a8fe98` L03_M14 `NursingWeightRecordPage`·`8570fa2` 통합 바이탈·`bb3dee8` 구강상태·`97108f2` 응급상황 FE wire) 미점검 갭 해소. 신규 4개 간호 기록 폼 중 **`NursingWeightRecordForm`** 「체중 (kg)」 필드만 결함을 가지고 있었다 — 유효 범위 안내문을 `Field` 밖 분리된 `<p id="nwr-weight-hint" className="ds-field__hint">`로 렌더하고 `TextInput`에 **`aria-describedby="nwr-weight-hint"`를 `{...p}` 뒤에 직접 지정**해, `Field`가 계산한 `aria-describedby`(오류·경고 id 포함)를 **덮어써** ① 체중 범위 오류(`체중은 20~200 kg 사이로…`)·② 비정상 범위 경고를 스크린리더가 안내하지 못하던 갭(코드베이스 표준 — 80·90·94차에서 확립한 「안내문은 `Field` `help` prop → `.ds-field__help` 전역 클래스로 전달, describedby에 오류·경고와 함께 병합」과 불일치, 일회성 `.ds-nursing-weight-form .ds-field__hint` 선택자 사용). ① **안내문을 `Field` `help` prop으로 전환** — 분리 `<p>`·수기 `aria-describedby` 제거, `Field`가 help·error·warning id를 모두 `aria-describedby`로 병합(SR이 범위 안내와 오류를 함께 안내). ② **일회성 CSS 제거(FE-16·§1 단일 원천)** — 미정의에 가까운 폼 전용 `.ds-nursing-weight-form .ds-field__hint` 삭제, 전역 `.ds-field__help` 사용. 다른 3개 폼(`NursingVitalCheckForm`·`NursingOralCareCheckForm`·`NursingEmergencyRecordForm`)·`NursingContextNav`는 표준 `Field`·`ds-context-nav` 패턴 준수 확인(변경 없음). 순수 접근성 정합 리팩터로 안내문 텍스트·동작 불변. 회귀 +1(`NursingWeightRecordForm.test.jsx` — 체중 입력 `aria-describedby`에 help id 포함·범위 오류 시 help+error id 동시 유지·`aria-invalid`). `npm test` 1267중 1265 PASS(2 pre-existing 실패 — `PressureUlcerPage.test.jsx`, 전체 실행 시에만 발생하는 테스트 오염, 단독 실행 5/5 PASS·본 변경 무관)·build PASS.)
> **이전 갱신**: 2026-06-14 (103차 — **US-O03 G-NURSING-PRESSURE-ULCER 욕창 케어 UI 골격 + G17b Field help `aria-describedby` 재점검 + §22·§23 신규** — 102차 이후 planner 135차 신규 P1 갭(US-O03 BE/FE 0건)·G17b ✅ full coder 산출물 미문서화 갭 해소. ① **US-O03 presentational UI** — `NursingContextNav`(4 route)·`PressureUlcerAssessmentForm`·`PressureUlcerPlanForm`(6대 수칙 fieldset)·`PressureUlcerCareRecordForm`(부위·NPUAP 단계·처치)·`PressureUlcerCohortReportPanel`(분기 StatCard+표)·`config/pressureUlcer.js`·`pressureUlcerCompliance.js`·`PRESSURE_ULCER_STAGE` Badge. ② **G17b a11y** — `ProgramParticipationForm`·`FunctionalRecoveryPage` 미제공 사유 `Field help`→`aria-describedby` 연결(MOHW 제32조). ③ **CSS** — `.ds-pressure-ulcer-form*`·`.ds-pressure-ulcer-report*`·`forced-colors`. ④ **§22 G17b**·**§23 US-O03** 신규. 회귀 +11. `npm test`·build PASS.)
> **이전 갱신**: 2026-06-14 (101차 — **US-J03 7-5 조용한 시간대(quiet-hours) 알림 발송 가드 접근성 재점검 — `title` 툴팁 → `aria-describedby` 가드 배너 연결** — 100차 이후 coder 신규 커밋(`111f056` fix(v2/J03): block billing notify UI during quiet hours 22:00~08:00 KST) 미점검 갭 해소. 새 가드는 `BillingDetailPage`(보호자 발송·납부확인서 발송)·`OverduePage`(행별 「미납 안내 발송」) 버튼을 조용한 시간대(Asia/Seoul 22:00~08:00)에 `disabled` 처리하고 그 사유를 **`title` 툴팁**으로만 노출했으나, ① **`title`은 `disabled` 버튼에서 키보드·스크린리더 사용자에게 노출되지 않음**(WCAG 1.4.13·4.1.2 — disabled 버튼은 hover/포커스 불가, `title`은 마우스 hover에만 의존)이고, ② 페이지 상단 quiet-hours 경고 `Alert`에 **`id`가 없어** 버튼과 프로그램적으로 연결되지 않아, 코드베이스 표준(73·78차 `ClaimGenerationPanel`·`FeeScheduleYearGuardBanner` — 가드 `Alert`에 `id` 부여 + 가드된 버튼 `aria-describedby`→배너 `id`)과 불일치했다. ① **quiet-hours 경고 `Alert`에 안정적 `id` 부여** — `billing-notify-quiet-hours-warning`(BillingDetailPage)·`overdue-reminder-quiet-hours-warning`(OverduePage). ② **가드된 발송 버튼 `aria-describedby`** — 조용한 시간대일 때 버튼을 경고 배너에 연결(SR이 비활성 사유를 함께 안내). ③ **`title` 툴팁 제거** — 키보드·SR 비노출 단서 의존 배제(`ClaimGenerationPanel` 정합). 순수 접근성 정합 리팩터로 disabled 동작·시각·메시지 불변. 회귀 +2(`BillingDetailPage.test.jsx`·`OverduePage.test.jsx` — `aria-describedby`=배너 id·`title` 부재·배너 id 텍스트 검증). `npm test` 1145중 1143 PASS(2 pre-existing 실패 — 아래 coder 인계)·build PASS. **coder 인계**: `pilotPageFlows.test.jsx` US-L02 미납 안내 2건이 **111f056 커밋부터 실패**(stash 검증으로 본 변경과 무관 확인). 원인 — `111f056`이 `OverduePage` 발송 성공 메시지를 `interpretBillingNotifyResult`(「보호자 N건에게 명세 안내를 발송했습니다.」)로 교체했으나 `pilotPageFlows` E2E는 이전 문구(「보호자에게 명세 안내가 발송되었습니다.」)를 여전히 단언. 메시지 계약·E2E 와이어링은 coder 영역이라 미수정.)
> **이전 갱신**: 2026-06-14 (100차 — **US-L06 7-5 간편결제 EasyPayPanel 접근성 재점검 + §20 신규 + §8-1 라우트 보강** — coder 신규 4커밋(`c9baca2`·`bebd874`·`3848af6`·`easyPay.js`: `/billing/easy-pay`·`EasyPayPanel`·prior-month guard·provider normalization) 미점검 갭 해소. ① **필드 단위 검증(WCAG 3.3.1)** — 청구서·결제 수단 미선택 시 폼 상단 `Alert` 대신 `Field error`+`aria-invalid`로 전환·입력 시 오류 자동 해제(`ComplaintConsultationForm` 패턴). ② **요청 버튼 `aria-describedby`** — 스텁 PG 안내(`#easy-pay-stub-note`)·선행입금 가드 배너(`#easy-pay-prior-month-guard-warning`)를 결합해 SR이 제약 맥락을 함께 안내. ③ **결제 상태 섹션** — `.ds-cms-debit-status` 재사용 대신 `.ds-easy-pay-status`+`section`+`aria-labelledby` h3·요청/완료일시 `<time dateTime>`·실패 사유 `role=alert`. ④ **CSS** — `.ds-easy-pay-status`·`__heading`·`forced-colors` 경계선(`.ds-cms-debit-status`와 공유 선택자). ⑤ **§2-3 `EASY_PAY_STATUS`**·**§8-1 `/billing/easy-pay`**·**§20** 신규. US-L03→US-L06 스토리 ID 오기 수정. 회귀 +3. `npm test`·build PASS.)
> **이전 갱신**: 2026-06-14 (99차 — **G41b 교육일지 4분류 compliance StatCard 접근성 재점검 + §19 정확화 + `ds-grid` 누락 수정** — coder 신규 4커밋(`38d24b6`·`a4ab0c2`·`76fe2fb`·`e14ba10`: G41b 재난·소화·직원권익 3종 연간 compliance BE wiring · live E2E harness · QA-B77 fix · 신규직원 window 하드코딩 제거) 미점검 갭 해소. ① **`StaffTrainingLogPage` `ds-grid` 누락 수정(FE-16)** — compliance StatCard 그리드가 `className="ds-grid--stats"`만 있고 기본 `ds-grid`(`display:grid`·`gap`)가 없어 카드들이 세로 블록 나열되던 결함을 `ds-grid ds-grid--stats` 조합으로 정정(`StaffStatusReportPage`·`ComplaintConsultationPanel` 정합). ② **§19-1 `StatCard` 수 정정** — G41b 3종 추가로 최대 7개(기존 표기 `×4` → `×4~7`). ③ **§19-1 A11y `Card h2` 패턴 명확화** — `compliance section+sr-only h2` 오기 → `Card ds-card__title h2` 가시 헤딩. ④ **§19-1 상수 모듈 G41b 항목 보강** — `G41B_ANNUAL_TYPES`·`mapG41bComplianceCards`·`isG41bAnnualTrainingType`·`countTrainingLogsByType` 추가. ⑤ **§19-1 coder 메모 G41b 필드 보강** — 6필드 명세. ⑥ **`newHireOrientation` 필드명 오기 수정** — DESIGN_SYSTEM 문서 `isNewHireTraining`→`newHireOrientation`. 회귀 없음(`ds-grid` 클래스 추가는 동작 불변·기존 테스트 PASS). `npm test`·build PASS.)
> **이전 갱신**: 2026-06-14 (98차 — **US-S04 G41 기관 교육일지 화면 신규 와이어 (`StaffTrainingLogPage`)** — G41 `FE wire ❌` 갭 해소. §19 신규 절·CSS 7개 클래스·API 4개·라우트 등록.)
> **이전 갱신**: 2026-06-14 (97차 — **US-J03 G/BNK-177 알림 채널 readiness 패널 — 미정의 클래스 제거 + 표 가시 헤딩 보강** — 96차 이후 coder 신규 3커밋(`6b1258c`·`d695923` `NotificationChannelReadinessPanel`(BNK-177)·`443efca` refresher compliance API·G34-QUAL gate) 미점검 갭 해소. 신규 패널이 `DashboardPage`·`OrganizationSettingsPage` 두 곳에 `Card`(h2) 하위로 임베드되나 두 가지 결함을 가지고 있었다. ① **미정의 클래스(FE-16·§1 단일 원천)** — 패널 컨테이너/제공자 요약이 CSS에 **정의되지 않은** `.ds-kv-list`·`.ds-kv-list__row`(소비자 이 패널 단 1곳)를 사용해 공유 토큰(grid 정렬·`dt`/`dd` 시맨틱 색·간격)을 못 받던 80차 `.ds-text-input`·90차 `.ds-help-text` 패턴 회귀를, 코드베이스 표준 정의 클래스 **`.ds-dl-grid`**(BillingDetailPage·ClientDetailPage 등 광범위 사용)로 전환하고 `__row` div 래퍼를 제거(grid 직계 `dt`/`dd`). ② **시각적으로 구분되지 않는 3연속 표(WCAG 1.3.1·2.4.6)** — `Solapi 연동 설정`·`이메일(SMTP) 연동 설정`·`필수 알림톡 템플릿` 3개 `Table`이 모두 `captionVisuallyHidden`(SR 전용 caption)에 **동일한 「항목 \| 상태」 컬럼**이라, 가시 헤딩이 없어 sighted 사용자가 어느 표가 무엇인지 식별할 수 없고(readiness Alert의 「아래 Solapi·템플릿 항목 확인」 지시 대상 모호), 44차/89차에서 확립한 「가시 `h3` + `captionVisuallyHidden`」 표 라벨 패턴과 불일치했다. 각 표 앞에 가시 `h3.ds-notification-channel-panel__subheading`(h1 페이지→h2 Card→h3 섹션 계층)을 추가해 시각·SR 모두 표를 식별. ③ **CSS 신규** — `.ds-notification-channel-panel__note`(정의 추가)·`.ds-notification-channel-panel__subheading`(secondary 색·md 굵게·`ds-section-gap` 상단 여백 정합). 순수 정합·접근성 리팩터로 동작·데이터 불변. 회귀 +1(`NotificationChannelReadinessPanel.test.jsx` — 3개 가시 `h3` level-3 헤딩 검증). **coder 인계**: `pilotPageFlows.test.jsx` US-S02 refresher(8-7-1) 1건이 **96차 이전부터 실패**(stash 검증) — `/staff/training` 초기 로드가 `443efca`에서 `fetchStaffRefresherTrainingComplianceApi`로 재배선되며 테스트가 기대하는 `/api/v1/users` 초기 fetch가 더는 호출되지 않음(`updateUserApi`는 「이수 완료」클릭 시에만 호출). API 와이어링·해당 테스트는 coder 영역이라 미수정. `npm test` 1081/228 PASS(1 pre-existing 실패)·build PASS.)
> **이전 갱신**: 2026-06-14 (96차 — **US-T14 G42 사후관리 모달·결재 대기함 접근성 + 8-12 사진게시 forced-colors** — 95차 이후 coder 신규 4커밋(`14124d6`~`a7a6004`: G42 `GrievanceFollowUpModal`·결재 대기함·사후관리 checklist·`StaffStatusReportPage` HR 사진게시) 미점검 갭 해소. ① **`GrievanceFollowUpModal`** — 필수값 검증을 폼 상단 `Alert`에서 **`Field error`+`aria-invalid`**(WCAG 3.3.1·`IncidentRecordForm` 패턴)로 전환·입력 시 오류 자동 해제·API 실패 `submitError`를 **모달 본문 `Alert`**에 노출(열린 dialog 뒤 페이지 오류 노출 방지, UXD-90 `CmsPage` 정합)·제출 중 overlay/Escape 닫기 차단. ② **`GrievanceCounselingPage`** — follow-up API 실패 시 페이지 `error` state 대신 모달에 위임. ③ **`ComplaintConsultationPanel`** — StatCard 요약 `role="group"`·사후관리 완료 Badge에 sr-only 「사후관리 완료」접두(색+텍스트)·`.ds-complaint-consultation-panel__queue` 경계선·`forced-colors`. ④ **`StaffStatusReportPage` 사진게시** — 사진 없음 placeholder sr-only 「{이름} 직원 사진 없음」·photo card `forced-colors` 경계선. ⑤ barrel `GrievanceFollowUpModal` export. 회귀 +3. `npm test`·build 검증.)
> **이전 갱신**: 2026-06-13 (95차 — **US-T15 G30 모니터링 자가진단 접근성 + US-R02 8-12 출력물 busy 상태** — 94차 이후 coder 신규 4커밋(`6f6915f`~`07956f5`: G30 MonitoringSelfDiagnosisPage·FAQ21836 basis fallback·8-12 export 7종·referenceDate filter) 미점검 갭 해소. ① **`MonitoringSelfDiagnosisPage`(G30)** — 자가진단·유선상담 `Table` `captionVisuallyHidden`(WCAG 1.3.1)·행별 「수정」버튼 `${itemCode} ${inspectionDirection}` 컨텍스트 `aria-label`(WCAG 2.4.6·91차 ClientRiskAssessmentPanel 패턴)·양 폼 `aria-label`·제출 `aria-busy`·연도 필터 `.ds-input--year`(FE-16)·유선상담 일자 `<time dateTime>`·오류 `role=alert`. ② **`.ds-monitoring-compliance`** — G30 StatCard 섹션 margin·`forced-colors` 경계선. ③ **`StaffStatusReportPage` 8-12 출력** — 기준일 「조회」·출력물 7종 버튼 `aria-busy`(export/loading 진행 SR 안내). 순수 접근성·정합 리팩터로 시각·동작 불변. 회귀 +3(`MonitoringSelfDiagnosisPage.test.jsx` 2·`StaffStatusReportPage.test.jsx` 1). `npm test`·build 검증.)
> **이전 갱신**: 2026-06-13 (94차 — **StaffStatusReportPage lifecycle 헤딩 prop 회귀 + CopayTypeSelect 안내문 `aria-describedby` 연결** — 93차 이후 coder 신규 5커밋(`02cbd05`~`e77b7e4`: G-7x-1 선행입금 가드·FAQ21824 lifecycle·G9-COG 인지지원등급·G9-COPAY-NAMING) 미점검 갭 해소. ① **`StaffStatusReportPage` 헤딩 회귀(WCAG 1.3.1·2.4.6)** — 직원현황 lifecycle 패널에 `heading="직원현황 lifecycle (8-12)"`를 전달했으나 `LifecycleWorkflowPanel`은 `title` prop만 받아 **무시**돼, 패널이 기본 제목 「업무 lifecycle」로 렌더되고 `aria-labelledby`도 그 일반 제목을 가리키던 결함을 `title`로 정정(의도한 8-12 컨텍스트 헤딩 복원). ② **`CopayTypeSelect` 안내문 연결(WCAG 1.3.1)** — 선택 시 노출되는 본인부담률 안내(「100분의 40 감경 · 본인부담률 9% …」)가 `Field` 밖 분리된 `<p className="ds-field__help">` 자식으로 렌더돼 컨트롤과 `aria-describedby`로 **연결되지 않던** 갭을, `DurationBandSelect` 패턴대로 `Field`의 `help` prop으로 전달해 select↔안내문을 연결(스크린리더가 선택 시 본인부담률을 함께 안내). 순수 접근성 정합 리팩터로 시각·동작·옵션 라벨(G9-COPAY-NAMING 법령 용어 병기) 불변. 회귀 +2(`StaffStatusReportPage.test.jsx` lifecycle 헤딩·`CopayTypeSelect.test.jsx` help `aria-describedby`). `npm test` **1022/222 PASS**·build PASS.)
> **이전 갱신**: 2026-06-13 (93차 — **US-R02 8-12 StaffStatusReportPage 접근성 + US-T14 G42 익명함 마스킹 + `.ds-grid--stats` 승격** — 92차 이후 coder 신규 `StaffStatusReportPage` @ `02cbd05`·`GrievanceCounselingPage` API 연동 @ `b0a9e06` 미점검 갭 해소. ① **`StaffStatusReportPage`** — StatCard 요약 `role="group"`·표 `captionVisuallyHidden`(「직원별 compliance 현황」)·행 링크 `${displayName} 직원 상세` `aria-label`·하위 메뉴 cross-link `aria-label`·오류 `Alert.ds-page-alert`(WCAG 2.4.6·1.3.1). ② **`.ds-grid--stats`** — 5열 StatCard 그리드 `minmax(160px,1fr)` 유틸 승격(FE-16 — coder가 사용했으나 CSS 미정의 회귀 해소). ③ **`.ds-staff-status-report__summary`** — `forced-colors` StatCard 경계선. ④ **G42 익명함(FAQ21814)** — `complaintSubjectDisplay`·`complaintApprovalContextLabel`(`config/complaintConsultations.js`) — `ANONYMOUS_BOX` 목록 대상 「익명」·결재 `aria-label` 「익명함 …」·실명 비노출. 회귀 +2. `npm test`·build 검증.)
> **이전 갱신**: 2026-06-13 (92차 — **US-T12 G40b·G38 ClientsContextNav + 회계연도 Field/TextInput 표준화 + US-T14 G42 고충상담 UI 골격 + US-R02 건강검진 패널 접근성** — 91차 이후 coder 신규 구현 `PeriodicRiskAssessmentStatusPage`·`CarePlanNotificationPage`·`StaffHealthCheckupRecordsPanel`(US-R02 8-10 HR 파일함 연동 @ `d41546f`) 및 USER_STORIES US-T14 G42(FE 0건) 갭 해소. ① **`ClientsContextNav`** — `/clients`↔`/clients/care-plan-notifications`(G38)↔`/clients/periodic-risk-assessments`(G40b) cross-page `nav`·`aria-current`(StaffContextNav 패턴). ② **회계연도·반기 필터 표준화(FE-16)** — `PeriodicRiskAssessmentStatusPage`·`ClientDetailPage` 반기 패널의 raw `<input className="ds-input">`/`<select className="ds-input">`·독립 `<label>`을 **`Field`+`TextInput`(`ds-input--year`)·`Select`(`ds-select--inline`)**로 전환(FunctionalRecoveryPage·CaseManagementPage 패턴 정합). ③ **표 행 링크 접근성(WCAG 2.4.6)** — G40b 「위험도평가」·G38 「등급 이력」 링크에 `${clientName} …` `aria-label`·G38 표 `captionVisuallyHidden`. ④ **`StaffHealthCheckupRecordsPanel`** — 파일함·기록 링크/버튼에 `${displayName}` 컨텍스트 `aria-label`. ⑤ **US-T14 `ComplaintConsultationForm`+`ComplaintConsultationPanel`** — FAQ21814 접수(서면·전화·문자·내방·익명함)·대상·`DateInput` 상담일·사후관리·`COMPLAINT_CONSULTATION_STATUS` Badge·행별 「결재 요청」`aria-label`(API·Route·`SignLeadCaregiverWorkLogModal` 재사용은 coder). ⑥ **CSS** — `.ds-fiscal-period-filters`·`.ds-staff-health-checkup-records`·`.ds-health-checkup-file-status`·`.ds-complaint-consultation*`. 회귀 +8. `npm test`·build 검증.)
> **이전 갱신**: 2026-06-13 (91차 — **US-T11 G40·G40b 위험도평가 패널 반복 액션 버튼 `aria-label` 컨텍스트(WCAG 2.4.6·4.1.2)** — 90차 접근성 패스 이후 coder가 신규 구현한 신규입소 위험도평가(`ClientRiskAssessmentPanel` @ `328d697`)·반기 기초평가(`ClientPeriodicRiskAssessmentPanel` @ `22325f4`)가 미점검이던 갭 해소. 두 패널은 각각 낙상·욕창·인지기능 3종 섹션마다 「수정」/「평가 등록」 트리거 버튼을 렌더하고, `ClientDetailPage` 「위험도평가」 탭에 **두 패널이 같은 탭에 동시 노출**돼 동일 접근성 이름의 버튼이 **최대 6개** 생겨 스크린리더가 어느 평가 유형·시점을 편집하는지 식별 못 하던 결함(코드베이스 반복 행/섹션 액션 표준 — `GuardianInvitationList`·`StaffPage`·`LeadCaregiverWorkLogPage` 정합). ① **신규입소 패널** — 버튼 `aria-label`을 `${typeLabel} 평가 수정`/`${typeLabel} 평가 등록`(예: 「낙상 위험도 평가 등록」)으로 부여. ② **반기 패널** — `${typeLabel} 반기 평가 수정`/`등록`(예: 「낙상 위험도 반기 평가 등록」)으로 부여해 신규입소 패널과 **같은 탭에서 명확히 구분**(「반기」 토큰). 시각 텍스트(「수정」/「평가 등록」)·동작은 불변. 회귀 +2(`ClientRiskAssessmentPanel.test.jsx`·`ClientPeriodicRiskAssessmentPanel.test.jsx` — 유형별 컨텍스트 라벨·중복 무맥락 라벨 0건), `pilotPageFlows`(US-T11) 트리거 조회를 컨텍스트 라벨로 정합. `npm test` **948/210 PASS**·build PASS.)
> **이전 갱신**: 2026-06-13 (90차 — **US-L03 CMS 자동이체 해지 모달 파괴적 액션 정합 + 모달 내 오류 노출 + 미정의 클래스 제거** — 119차 coder 신규 구현 CMS 해지 UI(`9a6fdb6`)가 마지막 UXD 접근성 패스(89차) 이후 추가돼 미점검이던 갭 3종 해소. ① **파괴적 확인 버튼 정합** — `CmsPage` 해지 확인 모달의 「해지 확인」버튼이 `variant="primary"`였으나, 코드베이스 파괴적 확인 표준(`TransportUnconfirmModal`「확정 취소」)과 정합되게 **`variant="danger"`**로 전환(색+의미 일치, 비가역 동작 시각 신호). ② **모달 내 오류 노출(WCAG 4.1.3·focus 맥락)** — 해지 실패 오류가 페이지 상단(`error`)에 렌더돼 **열린 모달 뒤**에 표시되던 갭을, `cancelError` 분리 state로 **모달 본문 안 `Alert tone=danger`**에 노출(focus가 갇힌 dialog 안에서 즉시 인지·assertive 안내) — 모달은 열린 채 유지, 닫기/취소·해지 진행 중에는 닫힘 차단. ③ **미정의 클래스 제거(FE-16·§1 단일 원천)** — 해지 안내 문구가 CSS에 **정의되지 않은** `.ds-help-text`(소비자 `CmsPage` 단 1곳)로 스타일 토큰을 못 받던 80차 `.ds-text-input` 패턴 회귀를, 상단 문구는 `.ds-modal-intro`·제약 안내는 **`Alert tone=warning`**(색+텍스트 병행, `TransportUnconfirmModal` 정합)으로 전환해 정의 클래스만 사용. 순수 정합·접근성 리팩터로 성공 동작 불변. 회귀 +1(`CmsPage.test.jsx` — 해지 실패 시 dialog 내 오류·모달 잔존). `npm test` **901/203 PASS**·build PASS(audit: esbuild GHSA-gv7w-rqvm-qjhr 신규 권고 — vite 메이저 필요·범위 외).)
> **이전 갱신**: 2026-06-13 (89차 — **US-R02 건강검진·US-S02 보수교육 화면 접근성 재점검 + 첨부 목록 CSS 공유 유틸 승격** — coder 신규 구현 `/staff/health-checkups`(US-R02 8-10)·`/staff/training` 이수증 관리(US-S02 8-7-1)를 접근성 패스. ① **`.ds-attachment-list*`** — `StaffRefresherTrainingPage`·`ClientBenefitContractAttachmentPanel`이 모듈 경계를 넘어 차용하던 grade-history 전용 `.ds-grade-history-attachments__{list,item,meta,filename,detail,preview-image}`를 도메인 중립 공유 유틸로 승격(FE-16·§1 단일 원천), 소비자 3종 전환·`forced-colors` 셀렉터 이동·grade-history 컨테이너(`__summary/__count/__body/__empty/__upload`)만 잔존. ② **날짜 의미론 회귀 해소** — 두 페이지 목록·이력 날짜(검진일·다음 기준·입사일)를 88차 `StaffDetailPage` 패턴과 정합되게 `<time dateTime>` 래핑. ③ 접근성 확인 — StatCard `role="group"`·표 `caption`·행 액션 직원명/파일명 `aria-label`·`fieldset/legend`·`aria-busy`·이수증 PDF 새 탭/이미지 Modal `alt`. 순수 정합 리팩터로 동작 불변. §9 유틸 표·§15 신규 절 추가. `npm test`·build·audit 검증.)
> **이전 갱신**: 2026-06-13 (88차 — **US-R03 직원 lifecycle 목록·상세 상태 Badge + 근로계약서 서명일 DateInput + 접근성 재점검** — USER_STORIES 116차 US-R03 core partial 인수 조건 중 목록·상세에서 lifecycle 상태를 한눈에 식별하지 못하던 갭 해소. ① **`STAFF_LIFECYCLE_STATUS`**(`Badge.jsx`) — `ONBOARDING`/`ACTIVE`/`OFFBOARDING`/`TERMINATED` 4상태 tone+한국어 라벨(색+텍스트 병행). ② **`StaffPage`** — 「입사~퇴사」열 `StatusBadge`·`resolveStaffLifecycleStatus`·상세 링크 `aria-label` 유지(WCAG 2.4.6). ③ **`StaffDetailPage`** 기본정보 탭 — lifecycle `StatusBadge`·입사일·퇴사일 `<time dateTime>`. ④ **`StaffLifecyclePanel`** — 근로계약서 서명일 `DateInput`·제출 `aria-busy`. ⑤ **`staffLifecycleCompliance.resolveStaffLifecycleStatus`** — 목록 배지 단일 원천. 회귀 +4. `npm test`·build·audit 검증.)
> **이전 갱신**: 2026-06-12 (87차 — **US-R03 직원 lifecycle FAQ21825 + StaffDetailPage + 접근성 재점검** — USER_STORIES 115차 신규 P2 Epic G-Staff-LC(이지케어 FAQ21825 입사~퇴사)가 frontend 0건이던 갭을 client lifecycle(G24/G14)과 대칭 surface로 해소. ① **`staffLifecycleCompliance.js`** — FAQ 21825 4단계(입사·신고·근로·퇴사)·서류 체크리스트·`buildStaffLifecycleSteps`. ② **`StaffLifecyclePanel`** — `LifecycleWorkflowPanel`+단계별 `region` 체크리스트·보수교육 `/staff/training` 링크(US-S02 후속)·입사/퇴사 `role=alert` 경고. ③ **`StaffDetailPage`** `/staff/:id` — 기본정보·입사~퇴사 `Tabs`·`StaffContextNav`·breadcrumb. ④ **`StaffPage`** — 이름·상세 링크 `aria-label`에 직원명 포함(WCAG 2.4.6). ⑤ **`.ds-staff-lifecycle-panel*`** CSS·`forced-colors`는 client 패널 선택자 공유. 회귀 +7. `npm test`·build·audit 검증.)
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
| `--color-accent` / `-text` | cyan-600 / 700 | 지점(센터) 정차·분기 UI (122차) |
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
| 이동시간 준수 (G15, US-T05) | `준수` | success | 준수 |
| | `지연` | danger | 지연 |
| | `미기록` | neutral | 미기록 |
| | `계획없음` | neutral | 계획없음 |
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
| 직원 lifecycle (US-R03) | `ONBOARDING` | info | 입사 진행 |
| | `ACTIVE` | success | 재직 |
| | `OFFBOARDING` | warning | 퇴사 진행 |
| | `TERMINATED` | neutral | 퇴사 완료 |
| lifecycle 상태 (G34·US-T09·US-T10) | `DRAFT` | neutral | 작성중 |
| **욕창 단계 (US-O03)** | `STAGE_1` | warning | 1단계 |
| | `STAGE_2` | warning | 2단계 |
| | `STAGE_3` | danger | 3단계 |
| | `STAGE_4` | danger | 4단계 |
| | `UNSTAGEABLE` | neutral | 미분류 |
| | `DEEP_TISSUE` | danger | 심부조직 |
| | `NONE` | success | 없음 |
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
| 간편결제 (US-L06 7-5) | `REQUESTED` | info | 요청됨 |
| | `PENDING` | info | 결제진행중 |
| | `SUCCEEDED` | success | 결제성공 |
| | `FAILED` | danger | 결제실패 |
| 도입 후 관리 회차 (US-O05) | `PENDING` | neutral | 대기 |
| | `IN_PROGRESS` | info | 진행중 |
| | `OVERDUE` | danger | 기한 초과 |
| | `COMPLETED` | success | 완료 |
| 계정 생성 요청 (StaffPage) | `PENDING` | neutral | 승인 대기 |
| | `APPROVED` | success | 승인됨 |
| | `REJECTED` | danger | 반려됨 |

> 매핑 객체는 `components/ui/Badge.jsx`의 `BILLING_STATUS`·`MATCH_STATUS`·`ATTENDANCE_STATUS`·`BRANCH_STATUS`·`BATCH_STATUS`·**`INVITATION_STATUS`**·**`STAFF_LIFECYCLE_STATUS`**(US-R03)·**`LIFECYCLE_STATUS`**·**`ONBOARDING_SESSION_STATUS`**(US-O05)·**`ACCOUNT_REQUEST_STATUS`**(StaffPage 계정 요청·144차)로 코드화 → `<StatusBadge status map>` 사용. `BATCH_STATUS`는 14차에 NHISImportPage 로컬 정의 → Badge 모듈로 승격. **`VISIT_STATUS`**(방문 일정, US-V01)는 도메인 상수와 함께 `config/visits.js`에 정의해 `<StatusBadge map={VISIT_STATUS}>`로 사용(57차). **`OUTING_STATUS`**·**`VEHICLE_STATUS`**(77차)는 `config/outingStatus.js`에 정의. **`EASY_PAY_STATUS`**(US-L06 7-5)는 `config/easyPay.js`에 정의(100차).

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

| 토큰 | 크기(실측 · 144차) | 용도 |
|------|------|------|
| `--font-size-xs` | 13px (0.8125rem) | 캡션·뱃지·도움말 |
| `--font-size-sm` | 15px (0.9375rem) | 보조 본문·표 |
| `--font-size-md` | 17px (1.0625rem) | **기본 본문·입력(모바일 16px+ 충족)** |
| `--font-size-lg` | 19px (1.1875rem) | 카드 부제 |
| `--font-size-xl` | 21px (1.3125rem) | 섹션/카드 제목 |
| `--font-size-2xl` | 26px (1.625rem) | 페이지 제목 `h1` |
| `--font-size-3xl` | 32px (2rem) | 대시보드 지표 숫자 |

> **144차 실측**: `d723d5a`에서 전 토큰 소폭 상향. 모바일 자동 줌 방지(≥16px)는 md(17px)에서 충족. 대비비 변화 없음.

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
| `/billing/easy-pay` | `EasyPayPage` | branch_admin, hq_admin | **US-L06** (7-5 간편결제) |
| `/billing/reports/charges` | `BillingReportPage` | branch_admin, hq_admin | **US-M03** (청구대장 7-6) |
| `/billing/reports/deposits` | `BillingReportPage` | branch_admin, hq_admin | **US-M03** (입금대장 7-7) |
| `/billing/reports/receipts` | `BillingReportPage` | branch_admin, hq_admin | **US-M03** (수납대장 7-8) |
| `/billing/reports/statistics` | `BillingStatisticsReportPage` | branch_admin, hq_admin | **G26** (의료비공제·본인부담 통계 7-8) |
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
| `/nursing/vital-checks` | `NursingVitalCheckPage` | branch_admin, social_worker, caregiver, hq_admin | **US-O04 L03_M11** |
| `/nursing/weight-records` | `NursingWeightRecordPage` | branch_admin, social_worker, caregiver, hq_admin | **US-O04 L03_M14** |
| `/nursing/oral-care-checks` | `NursingOralCareCheckPage` | branch_admin, social_worker, caregiver, hq_admin | **US-O04 L03_M13** |
| `/nursing/emergency-records` | `NursingEmergencyRecordPage` | branch_admin, social_worker, caregiver, hq_admin | **US-O04 L03_M04** |
| `/nursing/service` | `NursingServiceRecordPage` | branch_admin, social_worker, caregiver, hq_admin | **US-O04 L03_M01** |
| `/nursing/service/reports/total` | `NursingServiceReportsPage` | branch_admin, social_worker, caregiver, hq_admin | **US-O04 L03_M07** |
| `/nursing/service/reports/hospital-visits` | `NursingServiceReportsPage` | branch_admin, social_worker, caregiver, hq_admin | **US-O04 L03_M09** |
| `/nursing/service/reports/medication-delivery` | `NursingServiceReportsPage` | branch_admin, social_worker, caregiver, hq_admin | **US-O04 L03_M10** |
| `/nursing/excretion-tubes` | `NursingExcretionTubeRecordPage` | branch_admin, social_worker, caregiver, hq_admin | **US-O04 L03_M06** |
| `/nursing/pressure-ulcer/assessment` | `PressureUlcerPage` | branch_admin, social_worker, caregiver, hq_admin | **US-O03** |
| `/nursing/pressure-ulcer/plan` | `PressureUlcerPage` | branch_admin, social_worker, caregiver, hq_admin | **US-O03** |
| `/nursing/pressure-ulcer/records` | `PressureUlcerPage` | branch_admin, social_worker, caregiver, hq_admin | **US-O03** |
| `/nursing/pressure-ulcer/reports` | `PressureUlcerPage` | branch_admin, hq_admin | **US-O03 L03_M05** |
| `/nursing/pressure-ulcer/reports/provision` | `PressureUlcerPage` | branch_admin, hq_admin | **US-O03 L03_M15** |
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
| 청구 | 청구·정산, **공단 엑셀 import**, **입금**, **미납**, **CMS 자동이체**, **간편결제(7-5)**, 수가표·본인부담 비율(hq), **청구·입금·수납 대장**, **간편계산기** |

> 실제 정의는 `src/frontend/src/layout/navConfig.js` `NAV_GROUPS`(운영·이동·출석·기록·청구 5그룹). 본 표는 요약이며, 라우트 전수는 §8-1을 단일 원천으로 본다.

> **그룹 토글 (US-UX-05 ✅, 2026-06-14)**: 각 그룹 헤더(`button.ds-sidenav__toggle`) 클릭 시 하위 메뉴 접힘/펼침. **초기: 전 그룹 접힘 + 현재 route 부모 그룹만 auto-expand**(`buildNavGroupExpandedState`·`findNavGroupIdForPath`). **모바일·데스크톱 동일 규칙**. 접근성: `aria-expanded`·`aria-controls`·`aria-label="{그룹} 메뉴 그룹, {N}개 항목"`·접힌 `ul`에 `aria-hidden={!isOpen}`. 상세: `USER_STORIES US-UX-05` · `REQUIREMENTS §3-0` · `SideNav.test.jsx`.

> **비주얼 deepen (154차 PLAN_NOTES #5 ✅, 132차 문서화)**: Linear/Stripe 스타일 — ① **브랜드 블록** `.ds-sidenav__brand`(모노그램 `O`·`ogada`·`주간보호 운영` tagline). ② **그룹 아이콘** `layout/sideNavIcons.jsx` 20×20 stroke SVG(`aria-hidden`). ③ **활성 그룹 좌측 액센트** `.ds-sidenav__toggle--active` 3px primary border + nested `.ds-nav-item--active` border-left. ④ **무한 스크롤 방지** — `html/body/#root { overflow: hidden }` · 본문 `.ds-main` · SideNav `.ds-sidenav__scroll` 각 `overflow-y: auto` + `overscroll-behavior: contain`. ⑤ **그룹 카드** `.ds-sidenav__group--open` surface-muted 배경·item count pill.

> **구현 (US-UX-02 + US-UX-05)**: 5그룹(운영·이동·출석·기록·청구)·역할별 `navGroupsForRole` 필터·`EXACT_MATCH_PATHS` 활성 매칭(§8-2 하단).

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
| `.ds-visit-batch-confirm` | 방문일정 일괄확정 패널 구분선 (G21, §21) |
| `.ds-pressure-ulcer-form*` | 욕창 위험평가·계획·기록 폼 (US-O03, §23) |
| `.ds-pressure-ulcer-report*` | 분기 코호트 리포트 패널 (US-O03, §23) |
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
| `.ds-stat-grid` | **전역** 준수 현황·요약 StatCard 그리드 (`auto-fit minmax(200px,1fr)`). 80차에 스코프별 중복 정의 통합 — `role="group"` 카드 그리드 표준 |
| `.ds-functional-recovery-compliance` | 기능회복훈련 지표25·26·27 준수 섹션 여백 (78차, US-T06 G17) |
| `.ds-case-management-compliance` | 사례관리 회의록 지표43 준수 섹션 여백 (78차, US-T07 G32) |
| `.ds-care-plan-notification-compliance` | 급여계획 통보 G38 준수 섹션 여백 (80차) |
| `.ds-attachment-list` / `__item`·`__meta`·`__filename`·`__detail`·`__preview-image` | **공유** 첨부 파일 목록 — 업로드 파일명·형식·크기·미리보기 행(`forced-colors` 경계선). 89차에 `.ds-grade-history-attachments__*`(grade-history 전용 네이밍)에서 분리·승격 — `GradeHistoryAttachmentPanel`(US-M01-g)·`StaffRefresherTrainingPage`(US-S02 이수증)·`ClientBenefitContractAttachmentPanel`(US-T10) 공통 사용 |
| `.ds-grade-history-attachments` / `__summary`·`__count`·`__body`·`__empty`·`__upload` | 등급 이력 첨부 `<details>` 컨테이너·요약·업로드 (82차, US-M01-g G37 — 목록 행은 공유 `.ds-attachment-list*`) |

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

## 14. `.ds-stat-grid` 전역 통합 & 준수 카드 고대비 (80차) [UXD]

> **80차 UXD (2026-06-12)** — 준수 현황 StatCard 그리드 회귀 수정 + 접근성 재점검.

### 14-1. 배경 (회귀)

`.ds-stat-grid`(준수 현황 `role="group"` StatCard 그리드)는 78·79차에 **컴포넌트/페이지별로 스코프된 중복 규칙**으로만 정의되어 있었다(`.ds-functional-recovery-compliance .ds-stat-grid`, `.ds-case-management-compliance .ds-stat-grid`, `.ds-provision-result-compliance .ds-stat-grid`, `.ds-billing-nhis-comparison .ds-stat-grid`).

그 결과 **래퍼 없이 `.ds-stat-grid` 만 사용**하던 4개 화면의 StatCard가 그리드 레이아웃을 적용받지 못하고 세로로 쌓였다.

| 화면/컴포넌트 | 위치 | 래퍼 |
|--------------|------|------|
| `StaffRefresherTrainingPage` (보수교육 8-7-1) | `/staff/training` | 없음 → 미적용 |
| `LeadCaregiverWorkLogPage` (선임 업무수행일지 G34) | `/staff/lead-caregiver-log` | 없음 → 미적용 |
| `CarePlanNotificationPage` (급여계획 통보 G38) | `/programs/care-plan-notification` | `.ds-care-plan-notification-compliance`(규칙 부재) → 미적용 |
| `CareProvisionRecordPanel` (재가급여 기록 월간 요약) | `ClientDetailPage` | 없음 → 미적용 |

### 14-2. 조치

- `.ds-stat-grid` 를 **단일 전역 유틸리티**(`display:grid; auto-fit minmax(200px,1fr); gap var(--space-3)`)로 승격 — 위 4개 화면 그리드 회귀 즉시 해소.
- 동일했던 스코프 규칙 3종(기능회복·사례관리·급여제공결과) 제거, 컨테이너 클래스는 **섹션 여백**(`margin-block-end`)만 유지.
- `.ds-billing-nhis-comparison .ds-stat-grid` 의 `minmax(160px,1fr)` 만 **의도적 override**로 보존.
- `.ds-care-plan-notification-compliance` 섹션 여백 규칙 추가.

### 14-3. 접근성 (WCAG 1.4.11)

- `forced-colors: active`에서 `.ds-provision-result-compliance .ds-stat-grid .ds-stat` 에만 있던 고대비 윤곽선을 **`.ds-stat-grid .ds-stat` 전역**으로 확대 — 모든 준수 현황 카드가 고대비 모드에서 경계선으로 구분된다(색만으로 의미 전달 금지).
- 변경은 **CSS 전용** — 페이지/컴포넌트 JSX·`role="group"`·`aria-label` 구조 변경 없음. 빌드(897 modules)·`npm test`(866/195) PASS.

---

## 15. 직원 건강검진·보수교육 화면 + 첨부 목록 공유 유틸 (US-R02 · US-S02, 89차) [UXD]

> **89차 UXD (2026-06-13)** — coder가 새로 구현한 `/staff/health-checkups`(US-R02 8-10)·`/staff/training` 이수증 관리(US-S02 8-7-1)를 접근성 패스하고, 세 모듈에서 중복되던 첨부 목록 CSS를 단일 유틸리티로 승격.

### 15-1. 첨부 목록 CSS 공유 유틸 승격 (FE-16·§1 단일 원천)

- **배경**: `StaffRefresherTrainingPage`(이수증)·`ClientBenefitContractAttachmentPanel`(급여계약서)가 등급 이력 전용으로 명명된 `.ds-grade-history-attachments__list/__item/__meta/__filename/__detail/__preview-image`를 **모듈 경계를 넘어 차용**하고 있었다(82차 grade-history 네이밍에 결합).
- **조치**: 행 레이아웃(목록·항목·메타·파일명·상세·미리보기 이미지)을 도메인 중립 **`.ds-attachment-list*`** 로 승격. grade-history 전용(`__summary`·`__count`·`__body`·`__empty`·`__upload` = `<details>` 컨테이너)만 `.ds-grade-history-attachments*`에 잔존. `forced-colors` 경계선 셀렉터도 `.ds-attachment-list__item`으로 이동.
- **소비자 3종** 모두 공유 클래스로 전환 — `GradeHistoryAttachmentPanel`(US-M01-g)·`StaffRefresherTrainingPage`(US-S02)·`ClientBenefitContractAttachmentPanel`(US-T10). 순수 스타일 정합 리팩터로 시각·동작 불변(클래스 단언 테스트 0건 확인).

### 15-2. 접근성 재점검 — `StaffHealthCheckupsPage`·`StaffRefresherTrainingPage`

| 점검 | 결과 |
|------|------|
| 준수 현황 StatCard | `section[aria-labelledby]` + `.ds-stat-grid role="group"` — 색만 의존 금지(라벨 텍스트 상주), 완료/필요 tone success/warning ✅ |
| 표 접근성 이름 | `Table caption captionVisuallyHidden`(`scope="col"`) ✅ |
| 행 액션 라벨 | 이력·검진 기록·이수증·삭제·미리보기 버튼에 **직원명/파일명 포함 `aria-label`**(WCAG 2.4.6·4.1.2) ✅ |
| 폼 필드 오류 | `Field error`(`aria-invalid`+`role="alert"`)·검진 영역 `fieldset/legend`·제출 `aria-busy` ✅ |
| 날짜 의미론 | **회귀 해소** — 목록·이력 날짜(최근 검진일·다음 기준·입사일)를 88차 `StaffDetailPage` 패턴과 정합되도록 `<time dateTime>`로 래핑(머신 판독 가능, 값 없으면 `-`) |
| 이수증 미리보기 | PDF는 새 탭(`noopener`), PNG/JPEG는 `Modal`+`<img alt>`·미지원 형식 `role="status"` 안내 ✅ |

### 15-3. coder 전달 메모

- 향후 신규 첨부 업로드 UI는 `.ds-grade-history-attachments*`를 재사용하지 말고 **`.ds-attachment-list*`** 만 사용(목록 행) — `<details>` 토글이 필요하면 grade-history 컨테이너 패턴을 참고하되 별도 컨테이너 클래스를 두기.
- 직원 모듈 신규 화면은 `StaffContextNav`(직원/보수교육/건강검진/선임 업무수행일지) 상단 연동 유지.

---

## 16. G40 신규입소 위험도평가 패널 (US-T11, 90차) [UXD]

> **90차 UXD (2026-06-13)** — silverangel 지표21 급여개시 전 3종 위험도 스크리닝(낙상·욕창·인지기능) 패널 신규 구현.

### 16-1. 신규 컴포넌트 — `ClientRiskAssessmentPanel`

| 항목 | 상세 |
|------|------|
| 파일 | `src/frontend/src/components/ui/ClientRiskAssessmentPanel.jsx` |
| 위치 | `ClientDetailPage` — "위험도평가" 탭 |
| 연결 API | `fetchClientRiskAssessmentsApi` · `upsertClientRiskAssessmentApi` · `fetchAdmissionRiskAssessmentComplianceApi` |
| 상태 | `saving` → 저장 중 (`aria-busy`) / `error` → `Alert(tone=danger)` / 미완료 → `Alert(tone=warning)` 배너 |
| 준수 StatCard | `role="group"` `.ds-stat-grid` — tone success(완료) / warning(미완료) |
| 입력 폼 | `Field` render-prop — 평가일(`DateInput`) + 위험도 등급(`RiskLevelSelect`) + 메모(`Textarea`) |
| 평가 등급 | `RISK_LEVEL_STATUS` (Badge) — LOW success/MODERATE warning/HIGH danger |

### 16-2. 수정 파일

| 파일 | 변경 내용 |
|------|----------|
| `Badge.jsx` | `RISK_LEVEL_STATUS` 상수 추가 (LOW/MODERATE/HIGH → tone·label) |
| `clientLifecycleCompliance.js` | `RISK_ASSESSMENT_TYPES`, `RISK_ASSESSMENT_TYPE_LABELS`, `buildRiskAssessmentLifecycleSteps` 추가 |
| `services.js` | `fetchClientRiskAssessmentsApi`, `upsertClientRiskAssessmentApi`, `fetchAdmissionRiskAssessmentComplianceApi` 추가 |
| `components/ui/index.js` | `ClientRiskAssessmentPanel` export 추가 |
| `ClientDetailPage.jsx` | "위험도평가" 탭 + 상태(`riskAssessments`, `riskAssessmentAdmissionComplete`) + `useEffect` 추가 |
| `styles/components.css` | `.ds-risk-assessment-panel*` 스코핑 CSS + `forced-colors` 추가 |

### 16-3. 접근성 (WCAG 2.1 AA)

| 점검 | 결과 |
|------|------|
| 섹션 이름 | `<section aria-labelledby="risk-assessment-heading">` ✅ |
| 평가 유형 패널 | `<section aria-labelledby="ra-{type}-heading">` — 각 유형별 독립 랜드마크 ✅ |
| 폼 이름 | `<form aria-label="{typeLabel} 위험도평가 등록">` — `getByRole("form", { name })` 식별 가능 ✅ |
| 필드 오류 | `Field error`(`aria-invalid` + `role="alert"`) — 평가일·위험도 등급 필수 검증 ✅ |
| 저장 중 | 저장 버튼 `aria-busy="true"` — 스크린리더 "저장 중" 안내 ✅ |
| 색상만 의존 금지 | 등급 Badge — 라벨 텍스트(낮음/중간/높음) + tone 색상 병행 ✅ |
| `forced-colors` | `.ds-risk-assessment-panel__type-section` 고대비 윤곽선 ✅ |
| 기록 미존재 | "기록 없음" 텍스트 표시(색만으로 상태 전달하지 않음) ✅ |

### 16-4. `RiskLevelSelect` 내부 컴포넌트

`Select` 컴포넌트는 `children` 기반 `<option>` 렌더링만 지원한다. `options` 배열 prop 패턴은 `Select`에 없으므로, `RiskLevelSelect` 래퍼를 `ClientRiskAssessmentPanel.jsx` 내부에 두어 `<option>` children으로 변환한다. 향후 동일 패턴 재사용 시 이 컴포넌트를 별도 파일로 분리 가능.

### 16-5. coder 전달 메모

- 백엔드 API `/api/v1/clients/{id}/risk-assessments` (GET·PUT) · `/api/v1/clients/admission-risk-assessments/compliance` (GET) 구현 필요 (P2).
- PUT 페이로드: `{ assessmentType: "FALL_RISK"|"PRESSURE_ULCER"|"COGNITIVE_FUNCTION", assessedOn: "YYYY-MM-DD", riskLevel: "LOW"|"MODERATE"|"HIGH", notes?: string }`.
- GET 응답: 배열 `[{ assessmentType, assessedOn, riskLevel, notes }]` — `normalizeList` 처리됨.
- compliance GET 응답: `{ allCompleted: boolean, completedCount: number, totalCount: number }`.
- `buildRiskAssessmentLifecycleSteps` 는 API 연동 전 presentational scaffolding — API 완성 시 실제 완료 날짜로 `completedAt` 갱신 가능.

---

## 17. 직원현황 리포트·고충상담 익명함 (US-R02 8-12 · US-T14 G42, 93차) [UXD]

> **93차 UXD (2026-06-13)** — coder `StaffStatusReportPage` @ `02cbd05`·`GrievanceCounselingPage` @ `b0a9e06` 접근성 재점검.

### 17-1. StaffStatusReportPage (`/staff/reports/status`)

| 항목 | 상세 |
|------|------|
| 역할 | hq_admin·branch_admin·social_worker (StaffContextNav 연동) |
| 컴포넌트 | `StaffContextNav`, `StatCard` ×5, `LifecycleWorkflowPanel`, `Table`, `Badge`, `Alert`, `Spinner` |
| A11y | 요약 `role="group"` · 표 `captionVisuallyHidden` · 직원 링크 `${displayName} 직원 상세` · cross-link `aria-label` · 기준일 「조회」·출력물 7종 `aria-busy` (95차) |
| CSS | `.ds-grid--stats`(5열 StatCard) · `.ds-staff-status-report__summary` · `forced-colors` StatCard 경계 · `@media print` 7종 출력 zone |

### 17-2. G42 익명함 마스킹 (FAQ21814)

| 항목 | 상세 |
|------|------|
| 헬퍼 | `complaintSubjectDisplay` · `complaintApprovalContextLabel` (`config/complaintConsultations.js`) |
| 규칙 | `ANONYMOUS_BOX` — 목록 대상 「익명」·결재 버튼 「익명함 …」·실명(`targetName`) 미노출 |
| 폼 | `ComplaintConsultationForm` — 익명함 선택 시 대상 유형 자동 `OTHER` + 안내 `Alert` (92차 유지) |

---

## 19. 기관 교육일지 (US-S04 G41/G41b · func.php 8-7 · FAQ21807/21828, 98~99차) [UXD]

> **98차 UXD (2026-06-14)** — G41 FE 와이어 신규 구현. 노인인권교육(지표14)·운영규정 교육일지(지표5) + 신규직원 7일 이내 이수 집계.  
> **99차 UXD (2026-06-14)** — G41b 3종(재난·소화·직원권익) compliance BE wiring 접근성 재점검·§19 정확화.

### 19-1. StaffTrainingLogPage (`/staff/training-logs`)

| 항목 | 상세 |
|------|------|
| 역할 | hq_admin·branch_admin·social_worker (StaffContextNav 「교육일지 (8-7)」 링크) |
| 컴포넌트 | `StaffContextNav` · `StatCard` ×**4~7**(상반기·하반기·운영규정 연간·신규직원 + G41b 3종 조건부) · `Select`(연도·교육유형 필터) · `Table`(교육일·유형·방법·강사·참석자·신규직원 여부·관리) · `Modal`(등록/수정) · `Field`+`DateInput`/`Select`/`TextInput`/`Textarea` · `Badge tone=neutral`(유형) · `Badge tone=info`(신규직원) · `Alert` · `Spinner` · `EmptyState` |
| **G41 교육 유형** | 노인인권교육(`ELDERLY_HUMAN_RIGHTS` — 반기 1회·상/하반기 구분) · 운영규정(`OPERATING_REGULATION` — 연 1회·신규직원 7일 이내) |
| **G41b 교육 유형** | 재난상황대응(`DISASTER_RESPONSE`) · 소화·경보설비(`FIRE_SAFETY_EQUIPMENT`) · 직원권익(`STAFF_RIGHTS`) — 모두 **연 1회** 집계 (`G41B_ANNUAL_TYPES`) |
| 신규직원 | `newHireOrientation` 체크박스 — 운영규정 유형 선택 시 노출. 체크 시 `.ds-staff-training-log__newhire-section` 신규직원 `Select` 펼침(직원 목록 `GET /users`) |
| Compliance 집계 | `GET /api/v1/staff/training-logs/compliance` → 4개 핵심 StatCard + G41b 3개 조건부 StatCard. BE 응답 없으면 목록 기반 fallback(`countTrainingLogsByType`) |
| A11y | compliance `Card`+`ds-card__title h2`(가시 헤딩, AppShell h1→Card h2→신규직원현황 h3 계층) · `ds-grid--stats role="group" aria-label="교육 준수 현황 요약"` · 신규직원현황 표 `captionVisuallyHidden`(「신규직원 오리엔테이션 현황」) · 목록 표 `captionVisuallyHidden`(「기관 교육일지 목록」) · 행 「수정」 `${trainedAt} ${typeShortLabel} 교육일지 수정` `aria-label` · 폼 `aria-label`(「교육일지 등록/수정」) · 제출 `aria-busy` · 연도 `.ds-input--year` · 교육일 `<time dateTime>` |
| CSS 신규 | `.ds-staff-training-log__header`(제목+버튼 행 `flex` `space-between`) · `__subheading`(secondary color · md bold · section-gap 상단) · `__newhire-badge`(목록 유형 배지 inline 여백) · `__attendees`(20ch ellipsis) · `__content-field`(grid full-width) · `__newhire-check`(checkbox+label inline `flex`) · `__newhire-section`(상단 border + `forced-colors`) |
| 상수 모듈 | `src/frontend/src/config/staffTrainingLogs.js` — `TRAINING_LOG_TYPE`(5종) · `G41B_ANNUAL_TYPES`(3종 배열) · `TRAINING_LOG_TYPE_LABELS`/`SHORT` · `isSemiAnnualTrainingType` · `isOperatingRegulationType` · `isG41bAnnualTrainingType` · `mapG41bComplianceCards` · `countTrainingLogsByType`(fallback) · `TRAINING_METHODS`(5종) · `HALF_LABELS` · `REQUIRED_SEMI_ANNUAL=1` · `REQUIRED_ANNUAL=1` · `NEW_HIRE_WINDOW_DAYS=7` |
| API 서비스 | `services.js` — `fetchStaffTrainingLogsApi`·`createStaffTrainingLogApi`·`updateStaffTrainingLogApi`·`fetchStaffTrainingLogComplianceApi` |

### 19-2. coder 전달 메모

- 백엔드 `StaffTrainingLogController`(G41/G41b ✅ partial+) — `GET /api/v1/staff/training-logs`·`POST`·`PATCH /{logId}`·`GET /compliance` 4개 엔드포인트.
- FE `StaffTrainingLogResponse` 매핑 필드: `id`·`branchId`·`trainingType`·`trainedAt`·`trainingMethod`·`trainingContent`·`instructorName`·`attendeeNames`·`newHireOrientation`·`newHireUserId`·`referenceYear`·`referenceHalf`.
- `StaffTrainingLogComplianceResponse` 핵심 필드: `elderlyHumanRightsFirstHalfCount`/`…Met`·`…SecondHalf…`·`operatingRegulationAnnualCount`/`…Met`·`newHireStaffCount`/`newHireOrientationMetCount`/`allNewHiresOriented`·`newHireItems[]`(userId·displayName·daysSinceHire·orientationMet).
- **G41b compliance 필드**: `disasterResponseAnnualCount`/`disasterResponseRequiredPerYear`/`disasterResponseAnnualMet`·`fireSafetyEquipmentAnnualCount`/`…RequiredPerYear`/`…Met`·`staffRightsAnnualCount`/`…RequiredPerYear`/`…Met`. 없으면 FE 목록 fallback.
- 테스트 `StaffTrainingLogPage.test.jsx`·`staffTrainingLogs.test.js`·`pilotPageFlows.test.jsx` US-S04·`staffTrainingLogLiveApi.e2e.test.js` — `npm test` PASS.
- 라우트: `App.jsx` `/staff/training-logs` → lazy `StaffTrainingLogPage`. `navConfig.js` `EXACT_MATCH_PATHS` 등록.

---

## 18. 모니터링 자가진단·유선상담 (US-T15 G30, 95차) [UXD]

> **95차 UXD (2026-06-13)** — coder `MonitoringSelfDiagnosisPage` @ `6f6915f`·FAQ21836 basis fallback @ `0da41c6` 접근성 재점검.

### 18-1. MonitoringSelfDiagnosisPage (`/compliance/monitoring`)

| 항목 | 상세 |
|------|------|
| 역할 | hq_admin·branch_admin·social_worker |
| 컴포넌트 | `StatCard`(6개월 자가진단·유선상담 준수) · 5-field `Field`+`Select`/`TextInput`/`Textarea`/`DateInput` · `Table` ×2 · `Alert` |
| 준수 위젯 | 6개월 rolling 자가진단(`rollingComplete`) · 월 5명 유선상담(`REQUIRED_PHONE_CONSULTATIONS=5`) · FAQ21841 추천 대상 목록 |
| A11y | compliance `section`+sr-only `h2` · `StatCard role="group"` · 표 `captionVisuallyHidden` · 행 「수정」 `${itemCode} ${inspectionDirection}` `aria-label` · 폼 `aria-label` · 제출 `aria-busy` · 연도 `.ds-input--year` · 유선상담 일자 `<time dateTime>` |
| CSS | `.ds-monitoring-compliance` · `forced-colors` StatCard 경계 |

### 18-2. coder 전달 메모

- G30 live E2E verify는 tester(TSR) — fetch-mock 회귀는 `MonitoringSelfDiagnosisPage.test.jsx` 8건.
- FAQ21812~13(모니터링 checklist v2 Epic)은 별도 Route·`RecordsContextNav` 확장 검토 — 본 95차 범위 외.

---

## 20. 본인부담 간편결제 (US-L06 7-5 · 케어포 npay_manage, 100차) [UXD]

> **100차 UXD (2026-06-14)** — coder `EasyPayPage`·`EasyPayPanel` @ `c9baca2`/`bebd874`·prior-month guard·`config/easyPay.js` provider normalization 접근성 재점검.

### 20-1. EasyPayPage (`/billing/easy-pay`)

| 항목 | 상세 |
|------|------|
| 역할 | branch_admin·hq_admin (`BillingContextNav` 4항목: 입금·미납·CMS·**간편결제**) |
| 컴포넌트 | `BillingContextNav` · `EasyPayPanel` · `ClaimGenerationGuardBanner`(선행입금 가드 재사용) · `Alert` · `Spinner` |
| 결제 수단 | `EASY_PAY_PROVIDERS` — `CARD`(카드결제)·`KAKAO_PAY`(카카오페이). `normalizeEasyPayProvider()` — 공백/하이픈 정규화·`KAKAOPAY`→`KAKAO_PAY` |
| 선행입금 가드 | 청구서 선택 시 `fetchClaimGenerationGuardApi({ branchId, yearMonth })` → `priorMonthGuard` prop. 차단 시 `ClaimGenerationGuardBanner`(`title`·`fallbackAction`·`footerHint` 7-5 맥락) + 요청 버튼 `disabled` |
| A11y | 청구서·결제 수단 `Field error`+`aria-invalid`(필수 미선택) · 스텁 PG 안내 `#easy-pay-stub-note`+가드 배너 `aria-describedby` 결합 · 요청 `aria-busy`·`${clientName} 청구서 간편결제 요청` `aria-label` · 결제 상태 `section`+`h3#easy-pay-status-heading`+`aria-live=polite` · `StatusBadge map={EASY_PAY_STATUS}`(색+텍스트) · 요청/완료일시 `<time dateTime>` · API 실패는 폼 상단 `Alert`+상태 패널 텍스트 병행(중복 `role=alert` 금지) |
| CSS | `.ds-easy-pay-status` · `__heading` · `.ds-cms-debit-status`와 공유 패널 스타일·`forced-colors` 경계선 |
| 상수 모듈 | `src/frontend/src/config/easyPay.js` — `EASY_PAY_PROVIDERS` · `EASY_PAY_STATUS` · `normalizeEasyPayProvider` · `easyPayProviderLabel` |
| API 서비스 | `services.js` — `requestEasyPayPaymentApi`(`POST /billing/easy-pay/claims/{claimId}/payment`) · `fetchEasyPayStatusApi`(`GET` 동일 경로) |

### 20-2. coder 전달 메모

- v2 P2 **Stub PG** — 실연동 전까지 `role=note` 스텁 안내 유지. live PG(BNK-190 P2) 시 `#easy-pay-stub-note` 문구만 교체.
- `priorMonthGuard`는 `ClaimGenerationPanel`·`EasyPayPage`가 동일 `fetchClaimGenerationGuardApi` 사용 — BE enforce와 FE surface 정합 유지.
- QA-B78/B79 provider normalization — `normalizeEasyPayProvider` 단일 원천(`easyPay.js`). payload는 항상 `CARD`/`KAKAO_PAY` enum.
- 테스트 — `EasyPayPanel.test.jsx` 5건·`easyPay.test.js`·`EasyPayPage.test.jsx`·`easyPayPilot.e2e.test.js`·`pilotPageFlows` US-L06.

---

## 21. 방문일정 일괄확정 (G21 · US-V04 deepen · FAQ 21782, 102차) [UXD]

> **102차 UXD (2026-06-14)** — coder `VisitBatchConfirmPanel` @ `13e691e`·`VisitsPage` 연동·`fetchVisitConfirmReadinessApi`/`batchConfirmVisitsApi` 접근성 재점검.

### 21-1. VisitBatchConfirmPanel (`VisitsPage` — PLAN/BILLING 탭)

| 항목 | 상세 |
|------|------|
| 역할 | branch_admin·social_worker (`canSchedule` — 일정 등록·확정과 동일 RBAC) |
| 위치 | `VisitScheduleForm`·`NhisScheduleConfirmLockGuide` 아래 · `VisitNhisImportPanel` 위 |
| 워크플로 | 「일괄확정 시작」→ Modal → `GET /visits/confirm-readiness` → ack 2종 체크 → `POST /visits/batch-confirm` |
| Ack 체크리스트 | ① 공단 청구명세서 비교 ② 공단조회 변경이력 확인 — 이지케어 「4.일정확정」6단 |
| 사전 점검 | `draftCount`·`confirmedCount`·`unassignedDraftCount`·`pairedDivergedCount`·`blockers[]`·`ready` |
| A11y | 사전 점검 `Alert` `id=visit-batch-confirm-readiness-status`·차단 `id=visit-batch-confirm-blockers-warning`·ack 요구 `role=note` `id=visit-batch-confirm-ack-requirement`·비활성 submit `aria-describedby` 결합·ack `Checkbox` 차단 시 `aria-describedby`→차단 배너·제출 `aria-busy`·오류 `id=visit-batch-confirm-submit-error`·Modal 제출 중 닫기 차단 |
| CSS | `.ds-visit-batch-confirm` — import 패널과 시각 구분·`forced-colors` 상단 경계선 |
| API 서비스 | `services.js` — `fetchVisitConfirmReadinessApi` · `batchConfirmVisitsApi` |

### 21-2. coder 전달 메모

- `NhisScheduleConfirmLockGuide`(주간 청구 확정 잠금)와 `VisitNhisImportPanel`(확정 시 import 차단)은 G21 일괄확정과 **동일 월·동일 scheduleKind** 맥락 — `confirmedVisitCount`·`confirmedClaimCount` prop 정합 유지.
- live E2E P1 — `pilotPageFlows` 「batch-confirms draft visit schedules after NHIS ack gates」·`VisitBatchConfirmPanel.test.jsx` 2건.
- RFID split-view·확정 lock deepen은 ROADMAP P2 — 본 패널은 DRAFT→CONFIRMED 일괄 전환 surface만 담당.

---

## 22. 인지활동형 미제공 사유 (G17b · MOHW 2025-247 §32, 103차) [UXD]

> **103차 UXD (2026-06-14)** — coder G17b ✅ full @ `3bd6a43`/`487416d` — 프로그램 참여·기능회복훈련 계획 surface 접근성 재점검.

### 22-1. 적용 화면

| 화면 | 컴포넌트 | 트리거 |
|------|----------|--------|
| `/programs` | `ProgramParticipationForm` | `programType=COGNITIVE` + `status=ABSENT` |
| `/programs/functional-recovery` | `FunctionalRecoveryPage` 폼 | `cognitiveActivityProvided=false` |

### 22-2. 접근성 (WCAG 1.3.1)

| 항목 | 패턴 |
|------|------|
| 미제공 사유 필드 | `Field help` → `aria-describedby` — 「장기요양법 제32조 …」 법적 근거 SR 안내 |
| 프로그램 참여 | `Select` + `COGNITIVE_ACTIVITY_SKIP_REASONS` — 코드→한국어 라벨 |
| 기능회복 계획 | `Textarea` + `aria-required` — 미제공 시 사유 필수·제공 시 초기화 |
| 목록 | `ProgramsPage` 「미제공 사유 (G17b)」열 — `formatSkipReason` 텍스트 라벨 |

### 22-3. coder 전달 메모

- BE `ProgramService.resolveSkipReason`·V113 — payload `skipReason` enum·`cognitiveActivityNotProvidedReason` 문자열 정합 유지.
- `COGNITIVE_ACTIVITY_SKIP_REASONS` 단일 원천 — `config/programs.js`.

---

## 23. 욕창 케어 lifecycle (US-O03 · G-NURSING-PRESSURE-ULCER, 103차) [UXD]

> **103차 UXD (2026-06-14)** — planner 135차 P1 신규 갭. G40b 반기 PRESSURE_ULCER ✅ carry → **상시 평가·예방·일별기록·분기 리포트** 4 route surface.

### 23-1. 라우트·컨텍스트 네비

| Route | UI | 역할 |
|-------|-----|------|
| `/nursing/pressure-ulcer/assessment` | `PressureUlcerAssessmentForm` | branch_admin·social_worker·caregiver·hq_admin |
| `/nursing/pressure-ulcer/plan` | `PressureUlcerPlanForm` | 동일 |
| `/nursing/pressure-ulcer/records` | `PressureUlcerCareRecordForm` | 동일 |
| `/nursing/pressure-ulcer/reports` | `PressureUlcerCohortReportPanel` | branch_admin·hq_admin |

`NursingContextNav` — `BillingContextNav` 패턴 · `aria-label="욕창 케어 하위 메뉴"` · 44px 터치 · `forced-colors`.

### 23-2. 컴포넌트·상수

| 파일 | 용도 |
|------|------|
| `config/pressureUlcer.js` | 부위·NPUAP 단계·6대 수칙·처치·route 상수 |
| `utils/pressureUlcerCompliance.js` | `buildPressureUlcerLifecycleSteps` — `LifecycleWorkflowPanel` 연동 |
| `Badge.jsx` `PRESSURE_ULCER_STAGE` | 단계 tone·짧은 라벨(표·Badge) |
| `PressureUlcerAssessmentForm` | Braden 6~23 검증·`DateInput`·`Field error` |
| `PressureUlcerPlanForm` | `fieldset`+`legend` 6대 수칙 Checkbox·care plan ref |
| `PressureUlcerCareRecordForm` | 부위·단계·크기(cm)·처치·드레싱 |
| `PressureUlcerCohortReportPanel` | 분기 필터·StatCard×4·`Table captionVisuallyHidden` |

### 23-3. 접근ability (WCAG 2.1 AA)

| 점검 | 결과 |
|------|------|
| 필드 검증 | `Field error`+`aria-invalid` — 필수 미입력 차단 ✅ |
| 6대 수칙 | `fieldset`/`legend`+Checkbox `label` — SR 그룹 식별 ✅ |
| 단계 표시 | `StatusBadge`+`PRESSURE_ULCER_STAGE` — 색+텍스트 병행 ✅ |
| 코호트 요약 | `StatCard role="group"` — 고위험 danger·3단계 warning ✅ |
| `forced-colors` | `.ds-pressure-ulcer-form__rules`·report StatCard 경계선 ✅ |

### 23-4. coder 전달 메모

- **Route·Page·API 미구현** — 본 103차는 presentational UI+상수만. `App.jsx` 4 route·SideNav 기록 그룹 항목·`services.js` CRUD는 coder.
- DB `pressure_ulcer_assessments`·`pressure_ulcer_care_records` — API_SPEC §v3.1 추가 후 FE wire.
- G40b `ClientPeriodicRiskAssessmentPanel` PRESSURE_ULCER — 본 모듈 assessment와 **데이터 동기화** 검토(P2).
- US-O04 간호급여 9 leaf(`/nursing/vitals` 등) — 별도 Epic · 본 §23 범위 외.

---

---

## 24. 체중 기록 (L03_M14 · BNK-209, 104차) [UXD]

<!-- doc:owner=UXD doc:audience=PLN,COD,TSR updated=2026-06-14 -->

> **104차 UXD (2026-06-14)** — L03_M14 `FE wire ❌` 갭 해소. `GET/POST/PATCH /api/v1/nursing/weight-records` (V116) 완전 연결. `NursingWeightRecordPage` + `NursingWeightRecordForm` 신규 구현.

### 24-1. 라우트·컨텍스트 네비

| Route | UI | 역할 |
|-------|-----|------|
| `/nursing/weight-records` | `NursingWeightRecordPage` (page) | branch_admin·social_worker·caregiver·hq_admin |

`NursingContextNav` — "체중 기록" 링크 추가 (통합 바이탈 다음 순서). `navConfig.js` `EXACT_MATCH_PATHS` + `RECORD_ITEMS`에 `/nursing/weight-records` 등록.

### 24-2. 컴포넌트·파일 목록

| 파일 | 용도 |
|------|------|
| `pages/NursingWeightRecordPage.jsx` | 체중 기록 목록+폼 통합 화면 |
| `pages/NursingWeightRecordPage.test.jsx` | Vitest 통합 테스트 8건 |
| `components/ui/NursingWeightRecordForm.jsx` | 체중 기록 등록·수정 폼 |
| `components/ui/NursingWeightRecordForm.test.jsx` | 폼 단위 테스트 7건 |
| `config/nursingWeightRecord.js` | `NURSING_WEIGHT_RECORD_ROUTES` 상수 |
| `api/services.js` | `fetchNursingWeightRecordsApi` · `createNursingWeightRecordApi` · `updateNursingWeightRecordApi` 추가 |
| `styles/components.css` | `.ds-nursing-weight-form__intro` · `.ds-field__hint` · `forced-colors` 경계선 |

### 24-3. 폼 필드 스펙 (V116 DTO 기준)

| 필드 | 타입 | 필수 | 유효 범위 | 표시 |
|------|------|------|-----------|------|
| `clientId` | Select | ✅ | — | 이용자 선택 (수정 시 비활성) |
| `measureDate` | DateInput | ✅ | 날짜 | 측정일 |
| `weightKg` | TextInput number | ✅ | 20–200 kg | 체중 (kg) · hint + clamp 경고 |
| `heightCm` | TextInput number | ✗ | 100–220 cm | 신장 (cm) · clamp 경고 |
| `goalWeightKg` | TextInput number | ✗ | 20–200 kg | 목표 체중 (kg) |
| `notes` | Textarea | ✗ | — | 메모 |

**목록 표시 응답 필드:** `clientName`, `measureDate`, `weightKg`, `bmi`(서버 계산), `weightChangeKg`(이전 기록 대비), `goalWeightKg`.

### 24-4. 접근성 (WCAG 2.1 AA)

| 점검 | 결과 |
|------|------|
| 폼 레이블 | `Field` render-prop → `htmlFor` 연결 ✅ |
| 필수 필드 | `required` → `Field` 레이블 · submit 차단 ✅ |
| 범위 오류 | 클라이언트 검증 + `fieldErrors` per-field ✅ |
| 힌트 텍스트 | `aria-describedby="nwr-weight-hint"` — 20–200 kg 범위 SR 안내 ✅ |
| 저장 중 | `aria-busy={submitting}` on submit button ✅ |
| 성공 알림 | `role="status"` Alert — `live` 영역 SR 읽힘 ✅ |
| 수정 버튼 | `aria-label="${clientName} ${date} 체중 기록 수정"` — 행 특정 컨텍스트 ✅ |
| BMI/변화량 | `Badge` tone + 텍스트 병행 — 색만으로 의미 전달 금지 ✅ |
| `forced-colors` | `.ds-nursing-weight-form` 경계선 fallback ✅ |
| 키보드 네비 | 폼 탭 순서 선형 · 수정 취소 버튼 포커스 가능 ✅ |

### 24-5. BMI · 변화량 Badge 규칙

| 값 | tone | 의미 |
|----|------|------|
| BMI < 18.5 | `warning` | 저체중 |
| BMI 18.5–24.9 | `success` | 정상 |
| BMI ≥ 25.0 | `warning` | 과체중·비만 |
| 변화량 < 0 | `warning` | 체중 감소 (케어주의) |
| 변화량 ≥ 0 | `success` | 유지·증가 |
| null | — | "—" 텍스트 |

### 24-6. coder 전달 메모

- FE 구현 완료 — `App.jsx` route·`services.js` CRUD·`NursingContextNav`·`navConfig.js` 모두 반영.
- `updateNursingWeightRecordApi(recordId, payload)` — `clientId` 제외한 payload 전송 (`PATCH` DTO에 clientId 없음).
- `heightCm`·`goalWeightKg`·`notes` — `null` 전송 허용 (선택 필드).
- `bmi`·`weightChangeKg` — 서버 계산값, FE 연산 불필요.
- `measureDate` — 미래 날짜 차단 로직은 서버 단에서 처리 (L03_M11 `validateCheckDateNotFuture` 패턴 불필요).
- 테스트: `npm test -- NursingWeightRecord` 로 실행 확인.

---

## 25. 간호급여 제공기록 (L03_M01 · BNK-215, 105차) [UXD]

<!-- doc:owner=UXD doc:audience=PLN,COD,TSR updated=2026-06-14 -->

> **105차 UXD (2026-06-14)** — US-O04 L03_M01 `FE wire ❌` 갭 해소. `GET/POST/PATCH /api/v1/nursing/service-records` (V123) 완전 연결.

### 25-1. 라우트·컨텍스트 네비

| Route | UI | 역할 |
|-------|-----|------|
| `/nursing/service` | `NursingServiceRecordPage` | branch_admin·social_worker·caregiver·hq_admin |

`NursingContextNav` — "제공기록" 링크 추가 (응급상황 기록 다음). `navConfig.js` `EXACT_MATCH_PATHS` + `RECORD_ITEMS`에 `/nursing/service` 등록.

### 25-2. 컴포넌트·파일 목록

| 파일 | 용도 |
|------|------|
| `pages/NursingServiceRecordPage.jsx` | 제공기록 목록+폼 통합 화면 |
| `components/ui/NursingServiceRecordForm.jsx` | 3-flag 제공기록 등록·수정 폼 |
| `config/nursingServiceRecord.js` | `NURSING_SERVICE_RECORD_ROUTES`·`NURSING_SERVICE_PROVISION_LABELS` |
| `api/services.js` | `fetchNursingServiceRecordsApi` · `create` · `update` |

### 25-3. 폼 필드 스펙 (V123 DTO 기준)

| 필드 | 타입 | 필수 | 표시 |
|------|------|------|------|
| `clientId` | Select | ✅ | 이용자 (수정 시 비활성) |
| `serviceDate` | DateInput | ✅ | 제공일 (미래 차단) |
| `nursingProvided` | Checkbox | △ | 간호 제공 (3중 최소 1) |
| `nursingNotes` | Textarea | ✗ | 간호 내용 (체크 시 노출) |
| `medicationProvided` | Checkbox | △ | 투약 제공 |
| `medicationNotes` | Textarea | ✗ | 투약 내용 |
| `medicalVisit` | Checkbox | △ | 병의원 진료 |
| `medicalInstitution` | TextInput | ✗ | 의료기관명 |
| `medicalNotes` | Textarea | ✗ | 진료 내용 |
| `notes` | Textarea | ✗ | 메모 |

### 25-4. 접근성 (WCAG 2.1 AA)

| 점검 | 결과 |
|------|------|
| 제공 항목 그룹 | `fieldset`/`legend` 「제공 항목」 — SR 그룹 식별 ✅ |
| 최소 1개 검증 | `role="alert"` provision 오류 + `aria-describedby` on fieldset ✅ |
| 조건부 필드 | 체크 시에만 notes/institution 노출 — DOM 변화 SR 인지 ✅ |
| 필드 검증 | `Field error`+`aria-invalid` per-field ✅ |
| 목록 Badge | 제공 항목 「간호·투약·진료」텍스트+색 병행 ✅ |
| 수정 버튼 | `aria-label="${clientName} ${date} 제공기록 수정"` ✅ |
| `forced-colors` | `.ds-nursing-service-form__provision` 경계선 ✅ |

### 25-5. coder 전달 메모

- BE `validateNoProvisionSelected` — FE도 동일 검증(3-flag 모두 false 차단).
- `updateNursingServiceRecordApi` — `clientId` 제외 payload (`PATCH` DTO).
- UK `(org, client, service_date)` — 동일 일자 중복 시 서버 오류 → `applyApiErrorToForm` 처리.
- L03_M07·M09·M10 reports — **§27** 참조.

---

## 26. 배설·경관·유치도뇨 관리 (L03_M06 · BNK-216, 105차) [UXD]

<!-- doc:owner=UXD doc:audience=PLN,COD,TSR updated=2026-06-14 -->

> **105차 UXD (2026-06-14)** — US-O04 L03_M06 `FE wire ❌` 갭 해소. `GET/POST/PATCH /api/v1/nursing/excretion-tube-records` + `/reports` (V124).

### 26-1. 라우트·컨텍스트 네비

| Route | UI | 역할 |
|-------|-----|------|
| `/nursing/excretion-tubes` | `NursingExcretionTubeRecordPage` | branch_admin·social_worker·caregiver·hq_admin |

`NursingContextNav` — "배설·경관" 링크 추가. `navConfig.js` 등록.

### 26-2. 컴포넌트·파일 목록

| 파일 | 용도 |
|------|------|
| `pages/NursingExcretionTubeRecordPage.jsx` | 리포트+목록+폼 통합 화면 |
| `components/ui/NursingExcretionTubeRecordForm.jsx` | 관리 기록 등록·수정 폼 |
| `components/ui/NursingExcretionTubeReportPanel.jsx` | 종류별 StatCard×4 + 표 |
| `config/nursingExcretionTubeRecord.js` | `EXCRETION_TUBE_TYPE_LABELS`·routes |
| `api/services.js` | list·report·create·update API 4종 |

### 26-3. 폼 필드 스펙 (V124 DTO 기준)

| 필드 | 타입 | 필수 | 표시 |
|------|------|------|------|
| `clientId` | Select | ✅ | 이용자 |
| `recordDate` | DateInput | ✅ | 기록일 |
| `tubeType` | Select | ✅ | EXCRETION·NG_TUBE·URINARY_CATHETER |
| `tubeSize` | TextInput | ✗ | 관 크기 (예: 14Fr) |
| `insertionDate` | DateInput | ✗ | 삽입일 |
| `replacementDueDate` | DateInput | ✗ | 교체 예정일 |
| `managementDetail` | Textarea | ✅ | 관리 내용 |
| `notes` | Textarea | ✗ | 메모 |

### 26-4. 접근성 (WCAG 2.1 AA)

| 점검 | 결과 |
|------|------|
| 관리 종류 help | `Field help` → `aria-describedby` (UK 안내) ✅ |
| 필수 검증 | `Field error`+`aria-invalid` — managementDetail 필수 ✅ |
| 리포트 StatCard | `role="group"` 「관리 종류별 건수」 — 색+텍스트 ✅ |
| 표 날짜 | `<time dateTime>` 의미론 ✅ |
| 종류 Badge | `EXCRETION_TUBE_TYPE_LABELS` 텍스트 라벨 ✅ |
| 수정 버튼 | `aria-label`에 이용자명·날짜·종류 포함 ✅ |
| `forced-colors` | report StatCard 경계선 ✅ |

### 26-5. coder 전달 메모

- UK `(org, client, record_date, tube_type)` — 동일 일자·종류 중복 시 서버 오류.
- `fetchNursingExcretionTubeReportApi` — `totalRecords`·`excretionCount`·`ngTubeCount`·`urinaryCatheterCount` 집계.
- 기간 필터 UI — 본 105차는 기본 30일 윈도우(서버 default) 사용, 날짜 필터는 P2.
- `pilotPageFlows` L03_M01/M06 E2E harness 연동 검토.

---

## 27. 간호급여 제공 리포트 (L03_M07/M09/M10 · BNK-217~218, 106차) [UXD]

<!-- doc:owner=UXD doc:audience=PLN,COD,TSR updated=2026-06-14 -->

> **106차 UXD (2026-06-14)** — US-O04 L03_M07/M09/M10 `FE wire ❌` 갭 해소. `GET /api/v1/nursing/service-records/reports/{total,hospital-visits,medication-delivery}` (V123) 연결.

### 27-1. 라우트·컨텍스트 네비

| Route | UI | pamcode |
|-------|-----|---------|
| `/nursing/service/reports/total` | `NursingServiceReportsPage` | L03_M07 |
| `/nursing/service/reports/hospital-visits` | `NursingServiceReportsPage` | L03_M09 |
| `/nursing/service/reports/medication-delivery` | `NursingServiceReportsPage` | L03_M10 |

`NursingContextNav` — 「제공 리포트」→ total 경로. `NursingServiceReportNav` — 3종 서브 `nav`·`aria-current`. `navConfig.js` `EXACT_MATCH_PATHS` 4경로 등록.

### 27-2. 컴포넌트·파일 목록

| 파일 | 용도 |
|------|------|
| `pages/NursingServiceReportsPage.jsx` | 기간·이용자 필터 + 리포트 패널 |
| `components/ui/NursingServiceReportPanel.jsx` | variant별 StatCard·표 |
| `components/ui/NursingServiceReportNav.jsx` | 리포트 종류 cross-page nav |
| `config/nursingServiceRecord.js` | `NURSING_SERVICE_REPORT_*` 상수 |
| `api/services.js` | `fetchNursingServiceTotalReportApi` 등 3종 |

### 27-3. 접근성 (WCAG 2.1 AA)

| 점검 | 결과 |
|------|------|
| 섹션 헤딩 | `section`+`h3`+`aria-labelledby` ✅ |
| StatCard 요약 | `ds-grid ds-grid--stats`+`role=group`+variant별 `aria-label` ✅ |
| 표 | `captionVisuallyHidden`·`<time dateTime>` ✅ |
| 제공 항목 Badge | `NURSING_SERVICE_PROVISION_LABELS` 텍스트+색 ✅ |
| 로딩 | `aria-busy` on section ✅ |
| 오류 재시도 | `Alert`+「다시 시도」버튼(stale 데이터 클리어 @ `89dc52d`) ✅ |
| `forced-colors` | `.ds-nursing-service-report .ds-stat` 경계선 ✅ |

### 27-4. coder 전달 메모

- 필터 폼 `aria-label="리포트 조회 조건"`·조회 `aria-busy`.
- variant 전환 시 `useEffect` 재조회 — 이전 variant 행 잔존 방지는 페이지 state 관리 유지.
- live E2E harness @ `2966447`·`75c6c76` — UI 계약 본 §27-3과 정합.

---

## 28. 욕창간호 제공 리포트 (L03_M15 · BNK-218, 106차) [UXD]

<!-- doc:owner=UXD doc:audience=PLN,COD,TSR updated=2026-06-14 -->

> **106차 UXD (2026-06-14)** — US-O03 L03_M15 `FE wire ❌` 갭 해소 + **106차 a11y 회귀 해소**. `GET /api/v1/nursing/pressure-ulcer/reports/provision` (V125) 연결.

### 28-1. 라우트·컨텍스트 네비

| Route | UI | 역할 |
|-------|-----|------|
| `/nursing/pressure-ulcer/reports/provision` | `PressureUlcerPage`(mode=provision) | branch_admin·hq_admin |

`PressureUlcerReportNav` — 「분기 코호트」↔「제공 리포트」 서브 nav. `NursingContextNav` — 「욕창 제공 리포트」12번째 링크.

### 28-2. 컴포넌트·파일 목록

| 파일 | 용도 |
|------|------|
| `components/ui/PressureUlcerProvisionReportPanel.jsx` | StatCard + 제공 기록 표 |
| `components/ui/PressureUlcerReportNav.jsx` | 코호트·제공 리포트 전환 |
| `pages/PressureUlcerPage.jsx` | provision mode 필터·API 연동 |
| `api/services.js` | `fetchPressureUlcerProvisionReportApi` |

### 28-3. 접근성 (WCAG 2.1 AA)

| 점검 | 결과 |
|------|------|
| 섹션 헤딩 | **`h3#pu-provision-report-heading`** — 106차 이전 `aria-labelledby` orphan 회귀 해소 ✅ |
| StatCard | `ds-grid ds-grid--stats`+`role=group` 「제공 기록 건수」 ✅ |
| NPUAP 단계 | API 숫자(2)↔`STAGE_2` 정규화 + `StatusBadge`/`PRESSURE_ULCER_STAGE` (색+텍스트) ✅ |
| 부위 | `PRESSURE_ULCER_BODY_SITE_LABELS` 한국어 ✅ |
| 날짜 | `<time dateTime>` ✅ |
| 로딩 | `aria-busy`·로딩 중 EmptyState/표 숨김 ✅ |
| `forced-colors` | `.ds-pressure-ulcer-provision-report`·`.ds-stat` 경계선 ✅ |

### 28-4. coder 전달 메모

- BE `ulcerStage` — 정수(1~4) 또는 `STAGE_*` 코드 혼재 가능 → FE `normalizeUlcerStageCode` 단일 원천.
- provision 필터 — cohort와 동일 `DateInput`+`Select` 패턴(`Field` render-prop).
- live E2E @ `pressureUlcerLiveApi.e2e.test.js` — 본 §28-3 필드명 정합 유지.

---

## 29. 지점 도입 후 관리 체크list (US-O05 · G-ONBOARD-SUPPORT · BNK-223, 107차) [UXD]

<!-- doc:owner=UXD doc:audience=PLN,COD,TSR updated=2026-06-15 -->

> **107차 UXD (2026-06-15)** — US-O05 `FE wire ❌` 갭 해소. BE `GET/PUT/PATCH /api/v1/branches/{branchId}/onboarding-support` @ `735dd53` 연결.

### 29-1. 진입·역할

| 진입 | UI | 역할 |
|------|-----|------|
| `/branches` 행 「도입 체크list」 | `BranchesPage` → `Modal` → `BranchOnboardingSupportPanel` | hq_admin·branch_admin·social_worker (조회·회차 저장) |

- 오픈일 설정/변경 — hq_admin·branch_admin (`PUT`)
- 회차 항목·메모 저장 — hq_admin·branch_admin·social_worker (`PATCH /sessions/{roundNumber}`)
- SLA due-date — BE `BranchOnboardingSupportCatalog` (오픈+10일·1회차+10일·+6주·직무교육+10일)

### 29-2. 컴포넌트·파일 목록

| 파일 | 용도 |
|------|------|
| `components/ui/BranchOnboardingSupportPanel.jsx` | 1~4회차 checklist·오픈일·요약 StatCard |
| `config/branchOnboardingSupport.js` | 역할 카테고리 라벨·항목 그룹핑 |
| `components/ui/Badge.jsx` | `ONBOARDING_SESSION_STATUS` |
| `pages/BranchesPage.jsx` | 행 액션·Modal 연동 |
| `api/services.js` | onboarding-support API 3종 |

### 29-3. 접근성 (WCAG 2.1 AA)

| 점검 | 결과 |
|------|------|
| 오픈일 | `Field` render-prop + `DateInput`·필수 오류 `aria-invalid` ✅ |
| 회차 헤딩 | `h3` + `aria-labelledby` section ✅ |
| 상태 | `ONBOARDING_SESSION_STATUS` Badge (색+텍스트)·`OVERDUE` 좌측 보더 ✅ |
| 체크list | 역할별 `fieldset`/`legend`·`Checkbox` 라벨 연결 ✅ |
| 행 액션 | `${지점명} 도입 체크list`·`${지점명} N회차 저장` `aria-label` ✅ |
| 날짜 | 오픈일·기한·완료일 `<time dateTime>` ✅ |
| 저장 | `aria-busy`·회차별 오류 `role=alert` ✅ |
| `forced-colors` | `.ds-branch-onboarding-support__session*` 경계선 ✅ |

### 29-4. coder 전달 메모

- `platform_admin` — BE `@PreAuthorize`에 미포함(HQ/BRANCH/SOCIAL_WORKER만). `/platform` 조직 상세에서 동 패널 임베드는 후속 검토.
- checklist 항목 정의는 BE catalog 단일 원천 — FE는 API `items[]`만 렌더(중복 상수 금지).
- pilot/live E2E harness — post-merge `BranchesPage` modal flow 권장.

---

## 30. 정기 욕구사정 G24b 확장 (US-T09 · G24/G24b · BNK-226, 108차) [UXD]

<!-- doc:owner=UXD doc:audience=PLN,COD,TSR updated=2026-06-15 -->

> **108차 UXD (2026-06-15)** — US-T09 G24b `FE wire` @ `49fbf67` 접근성 재점검. BE V128 5컬럼 + FAQ 21810 1:1.

### 30-1. 진입·역할

| 진입 | UI | 역할 |
|------|-----|------|
| `/clients/:id` → 「기초평가」탭 | `ClientNeedsAssessmentPanel` → `ClientNeedsAssessmentForm` | branch_admin·social_worker (작성) · caregiver (조회) |

- FAQ 21800 8항목 + FAQ 21810 G24b 5항목(질병·의사소통·영양·거주환경·자원이용)
- 가정방문 대면 일자 필수 · G24b 5항목은 선택(경제·사회와 동일)

### 30-2. 컴포넌트·파일 목록

| 파일 | 용도 |
|------|------|
| `components/ui/ClientNeedsAssessmentPanel.jsx` | lifecycle + 필드 안내 + 폼 임베드 |
| `components/clients/ClientNeedsAssessmentForm.jsx` | 작성·저장·`upsertClientNeedsAssessmentApi` |
| `components/clients/ClientNeedsAssessmentCompare.jsx` | 전년 대비 diff 표 |
| `utils/needsAssessmentForm.js` | 필드 맵·검증·diff 빌더 |
| `utils/clientLifecycleCompliance.js` | `NEEDS_ASSESSMENT_FIELDS`·`NEEDS_ASSESSMENT_G24B_FIELDS` |

### 30-3. 접근성 (WCAG 2.1 AA)

| 점검 | 결과 |
|------|------|
| 필드 그룹 | FAQ 21800 / G24b **`fieldset`+`legend`** 2분리 ✅ |
| 라벨·힌트 | `Field` render-prop → `aria-describedby` help·error 병합 ✅ |
| 필수값 | `required` + `aria-required` + 필드 단위 `Field error` ✅ |
| 저장 | 제출 `aria-busy`·API 오류 `Alert role=alert` ✅ |
| 비교 표 | `caption` sr-only·`scope=col/row`·변경 행 **`Badge`「변경」**+`.ds-table__row--changed` ✅ |
| 패널 landmark | outer `aria-label`·필드 안내 `role=region`+`h3` ✅ |
| `forced-colors` | fieldset·compare changed row outline ✅ |

### 30-4. coder 전달 메모

- G24b 필드 BE snake_case ↔ FE camelCase — `NEEDS_ASSESSMENT_FIELD_MAP` 단일 원천 유지.
- live API E2E run(결정 96) — `ClientNeedsAssessmentForm` 가정방문+8항목+G24b payload 검증 권장.
- `LeadCaregiverWorkLogPage` needs-assessment import(BNK-157) — 저장된 G24b 필드 노출 여부 후속 확인.

---

## 31. 연간 욕구사정 현황 페이지 (US-T09 · G24b · BNK-228, 109차) [UXD]

<!-- doc:owner=UXD doc:audience=PLN,COD,TSR updated=2026-06-15 -->

> **109차 UXD (2026-06-15)** — coder `ca0b627`(G24b compliance 대시보드 위젯)이 `href="/clients"`(일반 목록)로 연결돼 대상 이용자 식별 불가 + `mapNeedsAssessmentComplianceView` util production 소비자 0건 갭 해소. `PeriodicRiskAssessmentStatusPage`(§·G40b) 패턴 정합 전용 현황 페이지 신설.

### 31-1. 진입·역할

| 진입 | UI | 역할 |
|------|-----|------|
| SideNav 운영 그룹 「연간 욕구사정 현황 (G24b)」 / `ClientsContextNav` / 대시보드 위젯 클릭 | `NeedsAssessmentStatusPage` (`/clients/needs-assessments`) | hq_admin · branch_admin · social_worker |

- 대시보드 위젯 「연간 욕구사정 미완료」·「등급변경 재사정 필요」 → 본 페이지로 연결(이전 `/clients` 일반 목록 대체).
- 비-HQ는 `activeBranchId` 스코프, HQ는 전 지점 조회.

### 31-2. 컴포넌트·파일 목록

| 파일 | 용도 |
|------|------|
| `pages/NeedsAssessmentStatusPage.jsx` | 회계연도 필터·StatCard 4종·수급자별 현황 표 |
| `utils/needsAssessmentCompliance.js` | `mapNeedsAssessmentComplianceView`·`formatMissingG24bFields`(신규)·`count*` |
| `components/ui/ClientsContextNav.jsx` | 이용자 모듈 4링크(목록·G38·G40b·G24b) |
| `layout/navConfig.js` | `/clients/needs-assessments` EXACT_MATCH + 운영 그룹 항목 |

### 31-3. 접근성 (WCAG 2.1 AA)

| 점검 | 결과 |
|------|------|
| StatCard 요약 | `role=group`+sr-only `h2`·tone(danger/warning) **+ 텍스트 라벨 병행** ✅ |
| 표 | `Table caption`·`scope=col`·연간 사정/재사정 `Badge`(색+텍스트) ✅ |
| 행 액션 | 「욕구사정」링크 `aria-label`에 **이용자명 포함**(WCAG 2.4.6) ✅ |
| 미기록 항목 | `formatMissingG24bFields` 한국어 라벨(코드 비노출) ✅ |
| 필터 | `Select` 시각 라벨 연결(`label htmlFor`) ✅ |
| 권한 | 미허용 역할 `Alert tone=warning` 안내 ✅ |
| `forced-colors` | 전역 `.ds-stat-grid .ds-stat` 윤곽선 재사용(신규 CSS 0) ✅ |

### 31-4. coder 전달 메모

- 표 컬럼: 이용자·가정방문 일자·연간 사정·등급변경 재사정·미기록 항목·조치. BE `NeedsAssessmentComplianceResponse` snake/camel 모두 `normalizeNeedsAssessmentComplianceItem`로 흡수.
- live API E2E(결정 96) — `GET /clients/needs-assessments/compliance?fiscalYear=&branchId=` 응답으로 본 페이지 행/StatCard 검증 권장(`e2e/needsAssessmentComplianceLiveApi.e2e.test.js` 연계).
- `findNeedsAssessmentComplianceForClient`는 ClientDetailPage 기초평가 탭 배지화 시 소비 가능(후속 P3).

---

## 32. 통합재가 기관 검색 안내 (G19 · MOHW 제55조의2 · BNK-44, 110차) [UXD]

<!-- doc:owner=UXD doc:audience=PLN,COD,TSR updated=2026-06-15 -->

> **110차 UXD (2026-06-15)** — coder `9afa30e`(G19 integrated-home provider discovery UI) 미점검 갭 해소. v1 Won't: 자동 청구·정산 미지원, 롱텀 포털 검색 안내만.

### 32-1. 진입·역할

| 진입 | UI | 역할 |
|------|-----|------|
| `/branches` 지점 등록·수정 모달 → 서비스 유형 `INTEGRATED_HOME` | `IntegratedHomeProviderDiscoveryPanel` | hq_admin |

- `INTEGRATED_HOME_SURCHARGE_NOTICE` Alert와 함께 노출.
- API: `GET /api/v1/branches/integrated-home/provider-discovery`

### 32-2. 컴포넌트·파일 목록

| 파일 | 용도 |
|------|------|
| `components/branches/IntegratedHomeProviderDiscoveryPanel.jsx` | 필터 파라미터·외부 검색 링크 |
| `config/branches.js` | `BRANCH_SERVICE_TYPES`·`INTEGRATED_HOME_SURCHARGE_NOTICE` |
| `pages/BranchesPage.jsx` | 조건부 패널 임베드 |

### 32-3. 접근성 (WCAG 2.1 AA)

| 점검 | 결과 |
|------|------|
| landmark | `aside` `aria-label`·`aria-busy` 로딩 ✅ |
| 메타데이터 | **`.ds-dl-grid`** `dt`/`dd` 시맨틱(미정의 `__meta` div 래퍼 제거) ✅ |
| 외부 링크 | `target=_blank`·`rel=noopener`·`aria-label` 「(새 탭)」 ✅ |
| `forced-colors` | `.ds-integrated-home-discovery` 경계선 ✅ |

### 32-4. coder 전달 메모

- 롱텀 포털 URL·필터 파라미터는 BE discovery 응답 단일 원천 — FE 하드코딩 금지.
- `platform_admin` 지점 등록 UI는 후속 검토(현재 hq_admin 전용).

---

## 33. 월간 급여제공기록지 보호자 발송 (G39 · 지표44 pillar 2 · BNK-235, 110차) [UXD]

<!-- doc:owner=UXD doc:audience=PLN,COD,TSR updated=2026-06-15 -->

> **110차 UXD (2026-06-15)** — coder `4d1a4f2`/`73094f9`(G39 monthly care record guardian dispatch) 접근성 재점검.

### 33-1. 진입·역할

| 진입 | UI | 역할 |
|------|-----|------|
| `/programs/provision-result-evaluations` | `ProvisionResultDispatchPanel` | hq_admin · branch_admin · social_worker |

- `monthlyProvisionRecordProvidedMet === false` 이용자만 표·발송 버튼 노출.
- API: `POST /clients/{id}/notifications/care-provision-record`

### 33-2. 접근성 (WCAG 2.1 AA)

| 점검 | 결과 |
|------|------|
| 표 | `captionVisuallyHidden`·`scope=col` ✅ |
| 상태 | **`Badge tone=warning`「미제공」**(색+텍스트) ✅ |
| 행 액션 | 발송 `Button` **`aria-label`=`${이용자명} ${연월} 급여제공기록지 발송`**(WCAG 2.4.6) ✅ |
| 필드 | `MonthInput`+`Field error`·제출 `aria-busy` ✅ |
| 결과 | 성공/실패 `Alert role=status|alert` ✅ |

### 33-3. coder 전달 메모

- J03 quiet-hours 가드 적용 시 `BillingDetailPage` 패턴(`aria-describedby`→배너 id) 재사용 권장.
- live API E2E — `careProvisionRecordDispatchLiveApi.e2e.test.js` 연계.

---

## 34. 모니터링 증빙 수집 기간 (G30 · FAQ21838 evidence window · BNK-235, 110차) [UXD]

<!-- doc:owner=UXD doc:audience=PLN,COD,TSR updated=2026-06-15 -->

> **110차 UXD (2026-06-15)** — coder `73094f9`(monitoring evidence window) UI 노출 접근성 재점검.

### 34-1. 진입·역할

| 진입 | UI | 역할 |
|------|-----|------|
| `/compliance/monitoring` | `MonitoringIntegratedChecklistPanel` | hq_admin · branch_admin · social_worker |

- `resolveMonitoringEvidenceWindow(referenceYear, referenceMonth)` — 실시 월 전전월 anchor ±2개월.
- checklist API 응답 `evidenceWindowStart`/`evidenceWindowEnd`와 동기.

### 34-2. 접근성 (WCAG 2.1 AA)

| 점검 | 결과 |
|------|------|
| 헤딩 | `section`+`h2` `aria-labelledby` ✅ |
| 증빙 기간 | `id=monitoring-evidence-window`·**`role=status`**·`.ds-monitoring-checklist__evidence-window` ✅ |
| StatCard | `role=group`·tone+텍스트 라벨 ✅ |
| 표 | `captionVisuallyHidden`·상태 `Badge`(색+텍스트) ✅ |

### 34-3. coder 전달 메모

- evidence window 계산은 `utils/monitoringCompliance.js` 단일 원천 — UI·live E2E 공유.
- RFID(문항10) `MANUAL` 상태는 v2 범위 — 패널 안내 문구 유지.

---

## 35. 집중배설관찰 (US-O06 · L02_M02 · BNK-238, 111차) [UXD]

<!-- doc:owner=UXD doc:audience=PLN,COD,TSR updated=2026-06-15 -->

> **111차 UXD (2026-06-15)** — coder `1264c16`(L02_M02 집중배설관찰 wire) 접근성 재점검 + 기록 화면 공통 레이아웃 CSS 승격. 선행: US-O06 인수조건(L02_M02 ✅ · L02_M07 △ BE WIP).

### 35-1. 진입·역할

| 진입 | UI | 역할 |
|------|-----|------|
| `/care/intensive-excretion` | `IntensiveExcretionObservationPage` | hq_admin · branch_admin · social_worker · caregiver |

- API: `GET/POST /api/v1/care/intensive-excretion-observations` · `PATCH /api/v1/care/intensive-excretion-observations/{id}` (V130, BE `fd42b7e`)
- 조회는 전 역할, 등록·수정은 `MANAGE_ROLES`(caregiver 포함)만.

### 35-2. 컴포넌트·파일 목록

| 파일 | 용도 |
|------|------|
| `pages/IntensiveExcretionObservationPage.jsx` | 목록 조회·등록·수정 화면 |
| `components/ui/IntensiveExcretionObservationForm.jsx` | 집중배설관찰 입력 폼 |
| `config/intensiveExcretionObservation.js` | `EXCRETION_TYPE_LABELS`·`STOOL_CONSISTENCY_LABELS` 상수 |
| `api/services.js` | `fetchIntensiveExcretionObservationsApi`·`createIntensiveExcretionObservationApi`·`updateIntensiveExcretionObservationApi` |

**공통 레이아웃 CSS 클래스** (기록 화면 공통 — `components.css` §35 승격):

| 클래스 | 용도 |
|--------|------|
| `.ds-page-stack` | 기록 페이지 수직 섹션 스택(flex column gap-6) |
| `.ds-page-loading` | 초기 로딩 중앙 정렬 영역 |
| `.ds-page-grid` | 기록 페이지 그리드 컨테이너 |
| `.ds-page-grid--sidebar` | 모바일 단열 → 태블릿+ 폼(좌)·목록(우) 2열 |
| `.ds-table__row--highlighted` | 수정 중인 행 배경+테두리 강조 |

### 35-3. 접근성 (WCAG 2.1 AA)

| 점검 | 결과 |
|------|------|
| 폼 레이블 | `Field` render-prop — `label`·`id` 자동 연결 ✅ |
| 필수값 | `required` + `aria-required` + `Field error` 필드 단위 차단 ✅ |
| 관찰내용/조치내용 상호의존 | `Field help` 안내·필드 단위 오류 동시 노출 ✅ |
| 배변 상태 조건 노출 | `URINATION` 선택 시 stool 필드 숨김(SR도 미노출) ✅ |
| 저장 | 제출 `aria-busy` · API 오류 `Alert ds-page-alert` ✅ |
| 목록 표 | `Table captionVisuallyHidden`·`scope=col`·관찰일 `<time dateTime>` ✅ |
| 수정 버튼 | **`Button variant=tertiary size=sm`** + `aria-label` 이용자명·날짜 포함(WCAG 2.4.6) ✅ |
| 수정 중 행 강조 | `.ds-table__row--highlighted` 배경+테두리(색+outline 병행) ✅ |
| `forced-colors` | `.ds-table__row--highlighted td` outline `Highlight` ✅ |
| 재시도 버튼 | 오류 Alert 내 `Button tertiary sm` ✅ |

### 35-4. coder 전달 메모

- `excretionType === "URINATION"` → `stoolConsistency`는 API 페이로드에서 `null`로 명시 전달(BE V130 제약 정합).
- **L02_M07 신체제재 (G-BODY-RESTRAINT)** — `14a2bb9`에서 본 폼 패턴 재사용해 FE wire 완료. 접근성 재점검은 **§36** 참조.
- `ds-page-stack`·`ds-page-grid--sidebar` CSS는 §35에서 단일 원천 승격 — L03_M01·L03_M06·L03_M08·L03_M09·L03_M10·L03_M14 등 기존 간호 기록 페이지도 동일 클래스 사용 중(이미 정상 동작, CSS 정의만 부재였음).

---

## 36. 신체제재 기록 (US-O06 · L02_M07 · BNK-239, 112차) [UXD]

<!-- doc:owner=UXD doc:audience=PLN,COD,TSR updated=2026-06-16 -->

> **112차 UXD (2026-06-16)** — coder `14a2bb9`(L02_M07 신체제재 wire) 접근성 재점검 + 미정의 디자인 토큰 클래스 보강. §35(L02_M02) 폼 패턴을 그대로 계승한 **인권 기록** 화면이라 동일 a11y 기준 적용.

### 36-1. 진입·역할

| 진입 | UI | 역할 |
|------|-----|------|
| `/care/body-restraint` | `BodyRestraintRecordPage` | hq_admin · branch_admin · social_worker · caregiver |

- API: `GET/POST /api/v1/care/body-restraint-records` · `PATCH /api/v1/care/body-restraint-records/{id}` (V131)
- 조회는 전 역할, 등록·수정은 `MANAGE_ROLES`(caregiver 포함)만.

### 36-2. 컴포넌트·파일 목록

| 파일 | 용도 |
|------|------|
| `pages/BodyRestraintRecordPage.jsx` | 목록 조회·등록·수정 화면 |
| `components/ui/BodyRestraintRecordForm.jsx` | 신체제재 입력 폼 |
| `config/bodyRestraintRecord.js` | `BODY_RESTRAINT_METHOD_LABELS`(6 enum) 상수 |
| `api/services.js` | `fetchBodyRestraintRecordsApi`·`createBodyRestraintRecordApi`·`updateBodyRestraintRecordApi` |

**디자인 토큰 클래스** (112차 보강):

| 클래스 | 용도 |
|--------|------|
| `.ds-body-restraint-form__intro` | 인트로 안내 `Alert`를 `ds-form-grid` **전폭(`grid-column: 1 / -1`)** 스팬 — §35 `.ds-nursing-excretion-form__intro` 패턴 정합. **이전 미정의로 단일 컬럼에 갇히던 시각 회귀 해소.** |

### 36-3. 접근성 (WCAG 2.1 AA)

| 점검 | 결과 |
|------|------|
| 폼 레이블 | `Field` render-prop — `label`·`id` 자동 연결 ✅ |
| 필수값 | `required` + `aria-required` + `Field error` 필드 단위 차단(이용자·제한일·시작시각·제한방법·제한사유) ✅ |
| 제한일 미래 차단 | `DateInput max=오늘` — 미래 일자 입력 방지(L02_M02 정합·인권 기록 정합성) ✅ |
| 보호자 통보 토글 | `Field`+`Checkbox`(label `for`/`id` 연결) — §35 nursing 폼 동일 패턴 ✅ |
| 저장 | 제출 `aria-busy` · API 오류 `Alert ds-page-alert` · 필드 오류 `applyApiErrorToForm` ✅ |
| 인트로 안내 | `Alert tone=info role=note` **전폭 스팬**(`.ds-body-restraint-form__intro`) ✅ |
| 목록 표 | `Table captionVisuallyHidden`·`scope=col`·제한일 `<time dateTime>`·방법 `Badge`(색+텍스트) ✅ |
| 수정 버튼 | `Button variant=tertiary size=sm` + `aria-label` 이용자명·날짜 포함(WCAG 2.4.6) ✅ |
| 수정 중 행 강조 | `.ds-table__row--highlighted`(색+outline 병행, `forced-colors` 대응) ✅ |
| 재시도 버튼 | 오류 Alert 내 `Button tertiary sm` ✅ |

### 36-4. coder 전달 메모

- 인트로/오류 `Alert`처럼 `ds-form-grid` 전폭으로 보여야 하는 요소는 **반드시 전폭 스팬 클래스**(`.ds-body-restraint-form__intro` 등)를 부여한다 — 신규 폼에서 `ds-*` 클래스를 참조할 때 `components.css` 정의 동반 여부를 확인할 것(미정의 시 단일 컬럼 회귀).
- `restraintMethod`는 `BODY_RESTRAINT_METHOD_LABELS` 6 enum 기반 `Select` — BE V131 enum과 키 일치 유지.
- 선택 필드(`endedAt`·`bodyPart`·`alternativeAttempted`·`releaseReason`·`notes`)는 빈 값일 때 페이로드에서 `null` 전달(§35 패턴 정합).

---

## 37. 요양급여 주간 제공기록 (US-O06 · L02_M01 · BNK-240, 113차) [UXD]

<!-- doc:owner=UXD doc:audience=PLN,COD,TSR updated=2026-06-16 -->

> **113차 UXD (2026-06-16)** — coder `41b2123`(L02_M01 주간 제공기록 wire) 접근성 재점검. §35~§36 기록 폼 패턴 계승.

### 37-1. 진입·역할

| 진입 | UI | 역할 |
|------|-----|------|
| `/care/weekly-service-records` | `CareServiceWeeklyRecordPage` | hq_admin · branch_admin · social_worker · caregiver |

- API: `GET/POST /api/v1/care/weekly-service-records` · `PATCH /api/v1/care/weekly-service-records/{id}` (V134)

### 37-2. 컴포넌트·디자인 토큰

| 파일 | 용도 |
|------|------|
| `pages/CareServiceWeeklyRecordPage.jsx` | 목록·등록·수정(사이드바 레이아웃) |
| `components/ui/CareServiceWeeklyRecordForm.jsx` | 7개 주간 항목 + 비고 폼 |
| `config/careServiceWeeklyRecord.js` | `WEEKLY_NOTE_FIELD_KEYS`·`WEEKLY_NOTE_FIELD_LABELS` |

| 클래스 | 용도 |
|--------|------|
| `.ds-care-weekly-form__intro` | 인트로 `Alert` 전폭 스팬(`grid-column: 1 / -1`) |

### 37-3. 접근성

| 점검 | 결과 |
|------|------|
| 주간 시작일 | `DateInput max=오늘` · 월요일 검증 · `Field help`에 이번 주 월요일 안내 ✅ |
| 필수 항목 | 이용자·주간 시작일·7개 항목 중 1개 이상 — `Field error` 필드 단위 ✅ |
| 제출 | `aria-busy` · API 오류 `applyApiErrorToForm` ✅ |
| 목록 | `Table captionVisuallyHidden` · 주간 `<time dateTime>` · 수정 `aria-label` 이용자명·주간 포함 ✅ |

---

## 38. 목욕 일정·제공현황 (US-O06 · L02_M03 · BNK-241, 113차) [UXD]

<!-- doc:owner=UXD doc:audience=PLN,COD,TSR updated=2026-06-16 -->

> **113차 UXD (2026-06-16)** — coder `950415d`(L02_M03 목욕 일정 wire) 접근성 재점검.

### 38-1. 진입·역할

| 진입 | UI | 역할 |
|------|-----|------|
| `/care/bathing-schedules` | `BathingSchedulePage` | hq_admin · branch_admin · social_worker · caregiver |

- API: `GET/POST /api/v1/care/bathing-schedules` · `PATCH /api/v1/care/bathing-schedules/{id}` (V136)

### 38-2. 컴포넌트·디자인 토큰

| 파일 | 용도 |
|------|------|
| `pages/BathingSchedulePage.jsx` | 목록·등록·수정 |
| `components/ui/BathingScheduleForm.jsx` | 일정·유형·상태·제공내용 폼 |
| `config/bathingSchedule.js` | `BATH_TYPE_*`·`BATH_SCHEDULE_STATUS_*` |

| 클래스 | 용도 |
|--------|------|
| `.ds-bathing-schedule-form__intro` | 인트로 `Alert` 전폭 스팬 |

### 38-3. 접근성

| 점검 | 결과 |
|------|------|
| 상태별 조건부 필드 | `COMPLETED` → 제공 내용 필수 · `CANCELLED`/`SKIPPED` → 사유 필수 — `Field error` ✅ |
| 예정일 | `COMPLETED` 시 `DateInput max=오늘` ✅ |
| 상태 Badge | 목록 `Badge` tone+텍스트(완료/취소/미제공/예정) — 색만 의존 금지 ✅ |
| 제출 | `aria-busy` ✅ |
| 수정 버튼 | `aria-label` 이용자명·예정일 포함 ✅ |

---

## 39. 청구 명세 4채널 발송 (US-G02 · G-7-1-4CHANNEL · BNK-242, 113차) [UXD]

<!-- doc:owner=UXD doc:audience=PLN,COD,TSR updated=2026-06-16 -->

> **113차 UXD (2026-06-16)** — coder `1fd1434`(G-7-1-4CHANNEL 명세 발송 wire) 접근성 재점검. 101차 quiet-hours·110차 `ProvisionResultDispatchPanel` 행 액션 패턴 정합.

### 39-1. 진입·역할

| 진입 | UI | 역할 |
|------|-----|------|
| `/billing/claims/:id` (확정·수납완료) | `BillingStatementDispatchPanel` | hq_admin · branch_admin |

- API: `GET/POST /billing/claims/{id}/statement-dispatches` · `PATCH .../statement-dispatches/{dispatchId}`

### 39-2. 채널·UI

| 채널 | UI 동작 |
|------|---------|
| `POSTAL` | 우편 발송일 `DateInput` 필수 · 발송 후 행별 발송일 수정 가능 |
| `SMS` · `EMAIL` | 발송일 서버 자동 · 조용한 시간대(22:00~08:00 KST) 발송 버튼 `disabled` |
| `KAKAO_ALIMTALK` | 동일 quiet-hours 가드 |

### 39-3. 접근성

| 점검 | 결과 |
|------|------|
| quiet-hours | `BillingDetailPage` 상단 `Alert id` → 발송 버튼 `aria-describedby`(패널 단독 사용 시 `statement-dispatch-quiet-hours-warning`) ✅ |
| 발송 대상 | `Checkbox` `role=group` + `aria-label` ✅ |
| 발송 내역 표 | `Table captionVisuallyHidden` · 채널 `Badge`(색+텍스트) · 발송일 `<time dateTime>` ✅ |
| 행 액션 | 「발송일 수정/저장/취소」`aria-label`에 **이용자명** 포함(WCAG 2.4.6) ✅ |
| 우편 발송일 수정 | `DateInput max=오늘` ✅ |
| `forced-colors` | `.ds-billing-statement-dispatch .ds-badge` outline ✅ |

### 39-4. coder 전달 메모

- `quietHoursGuardId`는 `BillingDetailPage`의 `billing-notify-quiet-hours-warning`을 그대로 전달 — 패널 내 중복 Alert 금지.
- `applyApiErrorToForm`은 **객체 시그니처**(`{ setFormError, setFieldErrors, fieldMap }`)만 사용.
- 우편(`POSTAL`)만 `dispatchedAtEditable` — 전자 채널 행은 발송일 수정 UI 미노출.

---

## 40. 통합식사도움·특이사항·요양 리포트 a11y 재점검 (US-O06 · L02_M13/M15/M04/M05, 114차) [UXD]

<!-- doc:owner=UXD doc:audience=PLN,COD,TSR updated=2026-06-16 -->

> **114차 UXD (2026-06-16)** — coder `9ad8346`(L02_M13 식사도움)·`3549896`(L02_M15 특이사항)·`c5f82a6`(L02_M04/M05 요양 리포트) wire 직후 접근성·일관성 재점검. §37(주간기록)·§38(목욕) 폼 패턴 정합.

### 40-1. 진입·역할

| 진입 | UI | 역할 |
|------|-----|------|
| `/care/meal-assistance-records` | `MealAssistanceRecordPage` + `MealAssistanceRecordForm` | caregiver 이상 |
| `/care/service-special-notes` | `CareServiceSpecialNotesPage` + `CareServiceSpecialNotesForm` | caregiver 이상 |
| `/care/reports/meal-excretion` | `CareMealExcretionReportPage` | hq_admin · branch_admin · social_worker · caregiver |
| `/care/reports/bath-help` | `BathHelpReportPage` | hq_admin · branch_admin · social_worker · caregiver |

- API: `GET/POST/PATCH /api/v1/care/meal-assistance-records` · 특이사항은 V134 `weekly-service-records` `special_notes` · 리포트는 `care_meal_excretion`·`bath_help` 뷰.

### 40-2. 재점검·보강 항목

| 파일 | 조치 | 근거 |
|------|------|------|
| `components/ui/MealAssistanceRecordForm.jsx` | **`applyApiErrorToForm` 객체 시그니처로 교정** (기존 위치 인자 `(err, FIELD_MAP)` + `mapped.message`/`mapped.fieldErrors` 참조 → 런타임 throw로 `Alert role="alert"` 미표시) | §39-4 객체 시그니처 단일 원칙 · 38개 호출부 중 유일한 위반 |
| `components/ui/MealAssistanceRecordForm.jsx` | `<form aria-label>` 추가(등록/수정) | §37·§38 폼과 동일 SR 컨텍스트 |
| `styles/components.css` | **`.ds-care-special-notes-form__intro` 신규 정의**(미정의 클래스 — 인트로 `Alert` 전폭 스팬 누락) | `.ds-bathing-schedule-form__intro`·`.ds-care-weekly-form__intro` 패턴 |
| `pages/CareMealExcretionReportPage.jsx` | 미정의 `.ds-muted` → 정의된 `.ds-text-muted`(§21) | 단일 원천 토큰 유틸 |

### 40-3. 접근성 (WCAG 2.1 AA)

| 점검 | 결과 |
|------|------|
| 폼 라벨 | 모든 입력 `Field` render-prop label·id 연결(`htmlFor`/`error`/`required`) ✅ |
| 오류 피드백 | `MealAssistanceRecordForm` 저장 실패 → `Alert tone="danger" role="alert"` 정상 노출(교정 후) ✅ |
| 필드 단위 오류 | API `fieldErrors` → `FIELD_MAP` snake→camel 매핑 후 `Field error` ✅ |
| 특이사항 폼 | 주간 시작일 월요일 검증·`max=오늘`·`help` 이번 주 월요일 안내 ✅ |
| 리포트 표 | `<th scope="col">` · 상태 `Badge`(색+텍스트) · 빈 상태 `EmptyState`/`.ds-text-muted` ✅ |
| 리포트 네비 | `nav aria-label` + `aria-current="page"` 컨텍스트 링크 ✅ |
| 조회 폼 | `form aria-label` + `Button aria-busy` ✅ |
| 제출 | 폼 `aria-busy={submitting}` ✅ |

### 40-4. coder 전달 메모

- 폼 오류 처리는 **반드시** `applyApiErrorToForm(err, { setFormError, setFieldErrors, fieldMap, fallbackMessage })` 객체 시그니처만 사용 — 위치 인자·반환값 참조 금지(함수는 `void`).
- 신규 케어 폼은 `<form>`에 `aria-label`(등록/수정)·`aria-busy`를 항상 지정한다.
- 보조 텍스트는 `.ds-text-muted`(정의됨)만 사용 — `.ds-muted`는 미정의.

### 40-5. 검증

- `npm test` 대상: `MealAssistanceRecordPage`·`CareServiceSpecialNotesPage`·`CareMealExcretionReportPage`·`BathHelpReportPage` 단위 PASS · ESLint 0.
- 전체 스위트의 일부 "create" 테스트는 병렬 jsdom 고부하 시 `waitFor`(기본 1000ms) 타임아웃으로 **간헐 실패** — 본 변경과 무관(미변경 `CareServiceWeeklyRecordPage`에서도 동일 재현). tester 소유 테스트이므로 본 패스에서 미수정.

---

## 41. 배차 Kakao 경로 미리보기 지도 + 요양 리포트 인쇄 a11y 재점검 (v1.3-A 배차 · L02_M04/M05, 115차) [UXD]

<!-- doc:owner=UXD doc:audience=PLN,COD,TSR updated=2026-06-16 -->

> **115차 UXD (2026-06-16)** — coder `0c523cd`/`15e9b64`/`d46688d`(배차 Kakao route-preview 지도·`POST /api/v1/transport/route-preview`·geocoder 폴백, QA-B102)·`d2145b0`(L02_M04/M05 요양 리포트 인쇄) wire 직후 접근성·미정의 토큰 클래스 재점검.

### 41-1. 대상 화면·컴포넌트

| 컴포넌트 | 위치 | 비고 |
|----------|------|------|
| `components/transport/KakaoTransportMap.jsx` | `TransportRunNewPage`·`TransportRunDetailPage`·`TransportPage` 배차 지도 | 번호 마커 + 도로 경로 폴리라인 + 거리·소요시간 요약 |
| `pages/CareMealExcretionReportPage.jsx` | `/care/reports/meal-excretion` | 인쇄 버튼·인쇄 전용 헤더 |
| `pages/BathHelpReportPage.jsx` | `/care/reports/bath-help` | 인쇄 버튼·인쇄 전용 헤더 |

### 41-2. 재점검·보강 항목

| 파일 | 조치 | 근거 |
|------|------|------|
| `styles/components.css` | **`.ds-transport-map__summary` 신규 정의** — `margin: 0 0 var(--space-2)`·`font-size: var(--font-size-sm)`·`:empty{display:none}` | FE-16·§1 단일 원천 — `KakaoTransportMap`이 참조하나 미정의(`ds-text-secondary`로 색만 적용·간격/글자크기 토큰 누락). 80차 `.ds-text-input` 회귀 패턴 |
| `components/transport/KakaoTransportMap.jsx` | 경로 요약 `<p>`를 **조건부 마운트 → 상시 상주 `role="status" aria-live="polite"`** 라이브 영역으로 전환 | WCAG 4.1.3 — 지도는 `role="img"`라 비시각 사용자에게 도로 거리·소요시간 미전달. 71차 `FeeSurchargeGuidePanel` 패턴 |

### 41-3. 접근성 (WCAG 2.1 AA)

| 점검 | 결과 |
|------|------|
| 지도 대체 텍스트 | 캔버스 `role="img" aria-label="배차 경로 지도"` ✅ |
| 도로 경로 요약 | 상시 `role="status"` 라이브 영역 — 비동기 계산 완료 시 「자동차 경로 약 N km · N분」 SR 안내, `:empty` 시각 숨김 ✅ |
| 마커 | DOM `<button type="button">` + `aria-label="정차 {라벨}"`·활성 마커 색+위치 ✅ |
| 지도 로드 실패 | `Alert tone="warning"` + 「정차 목록은 계속 확인」 폴백 안내 ✅ |
| 인쇄 전용 헤더 | `.ds-care-report-print-only` + `aria-hidden="true"`(화면 중복 방지) ✅ |
| 리포트 인쇄 버튼 | `Button aria-label`(변형별 인쇄 라벨)·`disabled={loading}` ✅ |
| 인쇄 영역 격리 | `@media print` — `.ds-care-report-print-root` 내 네비·필터·Alert·로딩 숨김, 표만 출력 ✅ |

### 41-4. coder 전달 메모

- 지도 보조 정보(거리·소요시간 등)는 **상시 상주 `role="status"` 라이브 영역**에 렌더하고, 빈 상태는 `:empty{display:none}`로 숨긴다(조건부 마운트 라이브 영역 금지 — 71차 결정).
- 지도 컴포넌트에서 사용하는 CSS 클래스는 **반드시 `components.css`에 정의**한다(FE-16·§1) — `ds-text-secondary`/`ds-text-muted`만으로 색을 받고 간격·크기 토큰을 누락하지 않는다.
- 인쇄 출력은 `.ds-care-report-print-root`(루트)·`.ds-care-report-print-only`(인쇄 전용·`aria-hidden`)·`@media print` 숨김 셀렉터 3종 패턴을 따른다(billing report print zone과 동일 원칙).

### 41-5. 검증

- `npx vitest run` transport 관련 13파일 **40 PASS** · `KakaoTransportMap` 단위 테스트 없음(Kakao SDK 의존 — jsdom 미지원).
- `npm test` **1457/1460 PASS** — 3 pre-existing 실패(`NursingServiceRecordPage` 등)는 전체 스위트 병렬 jsdom 고부하 `waitFor` 타임아웃 오염으로, 단독 실행 시 PASS·본 변경과 무관(§40-5와 동일 현상).
- `npm run build` PASS · ESLint 0.

---

## 42. 요양 리포트 4종 + G21 청구반영 배지 접근성 재점검 (L02_M11/M12/M06/M17/M16 · G21, 116차) [UXD]

<!-- doc:owner=UXD doc:audience=PLN,COD,TSR updated=2026-06-16 -->

> **116차 UXD (2026-06-16)** — coder `ff9c8c5`(L02_M11 수급자별 급여제공·L02_M12 급여제공 집계)·`fa20943`(L02_M06 체위변경·L02_M17 집중배설)·`8b804fc`(L02_M16 식사 선호도 조사)·`25ca88e`(G21 청구반영 배지) wire 직후 접근성 재점검.

### 42-1. 대상 화면·컴포넌트

| 컴포넌트 | 위치 | 비고 |
|----------|------|------|
| `pages/PatientServiceReportPage.jsx` | `/care/reports/patient-service` (L02_M11) | 수급자별 급여제공 리포트 — 5종 표 |
| `pages/ServiceSummaryReportPage.jsx` | `/care/reports/service-summary` (L02_M12) | 급여제공 집계 리포트 — 이용자별 집계 표 |
| `pages/PositionChangeReportPage.jsx` | `/care/reports/position-change` (L02_M06) | 체위변경·욕창 리포트 — 2종 표 |
| `pages/IntensiveExcretionReportPage.jsx` | `/care/reports/intensive-excretion` (L02_M17) | 집중배설 관찰 리포트 — 1종 표 |
| `pages/MealPreferenceSurveyPage.jsx` | `/care/meal-preference-surveys` (L02_M16) | 식사 선호도 조사 — caption 이미 정합 ✅ |
| `pages/VisitsPage.jsx` | `/visits` | G21 청구반영 상태 배지 안내 |
| `components/ui/CareReportContextNav.jsx` | 위 리포트 모든 페이지 상단 | 요양 리포트 cross-nav |
| `styles/components.css` | `.ds-badge--dark` | G21 신규 `tone="dark"` 배지 |

### 42-2. 재점검·보강 항목

| 파일 | 조치 | 근거 |
|------|------|------|
| `PatientServiceReportPage.jsx` | **5종 `<Table>` → `captionVisuallyHidden caption`** 부여 (요양급여 주간 제공기록·통합식사도움·목욕 일정·집중배설 관찰·신체제재 기록) | WCAG 1.3.1 — 시각 Card 제목이 있어도 SR 표 탐색(`T`)에 caption 필요 |
| `PatientServiceReportPage.jsx` | StatCard 래퍼 **`role="group" aria-label="수급자별 급여제공 요약"`** | WCAG 1.3.1 — SR이 집계 목적을 그룹으로 식별 (93차 패턴) |
| `ServiceSummaryReportPage.jsx` | `<Table>` → `captionVisuallyHidden caption="이용자별 급여제공 집계 목록"` | 위 동일 |
| `ServiceSummaryReportPage.jsx` | StatCard **`role="group" aria-label="급여제공 집계 요약"`** | 위 동일 |
| `PositionChangeReportPage.jsx` | **2종 `<Table>`** → caption 부여 (욕창 위험도 평가·체위변경·욕창 간호 기록) | 위 동일 |
| `PositionChangeReportPage.jsx` | StatCard **`role="group" aria-label="체위변경 대상자 요약"`** | 위 동일 |
| `IntensiveExcretionReportPage.jsx` | `<Table>` → `captionVisuallyHidden caption="집중배설 관찰 상세 목록"` | 위 동일 |
| `IntensiveExcretionReportPage.jsx` | StatCard **`role="group" aria-label="집중배설 관찰 요약"`** | 위 동일 |
| `VisitsPage.jsx` | 청구반영 상태 `Alert` — **「검은 배지」·「빨간 배지」 색 명칭 제거**, 텍스트 라벨(「청구반영」·「미반영」·「페어 없음」)만 사용 | §1-2 색상만으로 의미 전달 금지(WCAG 1.4.1) — 배지 자체는 이미 텍스트+색 병행 `BILLING_CLAIM_REFLECTION_STATUS` |
| `styles/components.css` | **`.ds-badge--dark` `forced-colors` 경계선** — `outline: 1px solid ButtonText; forced-color-adjust: none` | WCAG 1.4.11 — 고대비 모드에서 배경 소거 시 badge 경계 유지 |
| `pages/VisitsPage.test.jsx` | G21 테스트 — 이전 색 명칭(`/검은 배지/`) 단언 → 새 문구(`/청구반영 상태 안내:/`·`getAllByText`) | 회귀 갱신 |

### 42-3. `CareReportContextNav` 패턴

새 `CareReportContextNav`는 기존 `AttendanceContextNav`·`NursingContextNav` 패턴을 따른다:
- `<nav className="ds-context-nav" aria-label="요양 리포트">` landmark
- `Link aria-current="page"` 활성 표시
- 정의 클래스 `.ds-context-nav__link--active`(§0 단일 원천)

### 42-4. 접근성 (WCAG 2.1 AA)

| 점검 | 결과 |
|------|------|
| 리포트 표 caption | 9종 표 모두 `captionVisuallyHidden caption` ✅ (MealPreferenceSurveyPage는 기존 정합) |
| StatCard 그룹 의미론 | 4 리포트 × `role="group" aria-label` ✅ |
| 청구반영 상태 안내 색 의존 | 제거 — 텍스트 라벨만 사용 ✅ |
| `ds-badge--dark` forced-colors | `outline` 경계선 보강 ✅ |
| `CareReportContextNav` landmark | `nav` + `aria-label` + `aria-current` ✅ |
| `MealPreferenceSurveyForm` | `Field`·`DateInput`·`Checkbox`·`aria-busy`·`aria-invalid`·필드 단위 오류 ✅(기존 정합) |

### 42-5. coder 전달 메모

- 새 리포트 페이지에 `<Table>` 추가 시 항상 `captionVisuallyHidden caption="{카드 제목} 목록"` 부여할 것 — 시각 h2/h3가 있어도 SR 표 탐색에 별도 caption 필요.
- StatCard 집계 그룹은 **`role="group" aria-label="{화면명} 요약"`** 래퍼가 필수(93차 패턴).
- 새 `tone="dark"` Badge: `forced-colors` 경계선이 `components.css`에 정의됨 — 다른 `dark` 배지 추가 시 별도 CSS 불요.
- `BILLING_CLAIM_REFLECTION_STATUS` 설명 Alert에서 색 명칭(검은/빨간 등) 사용 금지 — 배지 텍스트 라벨을 그대로 인용할 것.

### 42-6. 검증

- `VisitsPage.test.jsx` **10/10 PASS** · 보고서 4종 **8/8 PASS**.
- `npm test` **1490/1490 PASS** · `npm run build` PASS.

---

## 43. G26 본인부담 통계 + G21 RFID split-view 접근성 재점검 (117차) [UXD]

<!-- doc:owner=UXD doc:audience=PLN,COD,TSR updated=2026-06-16 -->

> **117차 UXD (2026-06-16)** — coder `d8f1fdf`(G26 `BillingStatisticsReportPage`·`BillingReportsContextNav` statistics 링크)·`55fdbd0`(G21 RFID split-view)·`6759bf6`(L03_M09/M10 care nav cross-links) wire 직후 접근성 재점검.

### 43-1. 대상 화면·컴포넌트

| 컴포넌트 | 위치 | 비고 |
|----------|------|------|
| `pages/BillingStatisticsReportPage.jsx` | `/billing/reports/statistics` (G26) | 케어포 PDF p.92 7-8 2축 통계 |
| `components/ui/BillingReportsContextNav.jsx` | 대장·계산기 cross-nav | 「본인부담 통계」6번째 항목 |
| `pages/VisitsPage.jsx` | `/visits` | G21 RFID split-view 모드 |
| `styles/components.css` | `.ds-billing-report__summary`·`.ds-visits-split-compare` | forced-colors 보강 |

### 43-2. 재점검·보강 항목

| 파일 | 조치 | 근거 |
|------|------|------|
| `BillingStatisticsReportPage.jsx` | 조회 연도 검증 — 페이지 `Alert` → **`Field error`+`aria-invalid`**·입력 시 오류 자동 해제 | WCAG 3.3.1 — 어느 필드가 잘못됐는지 SR 식별 (`BillingReportPage`·`EasyPayPanel` 패턴) |
| `BillingStatisticsReportPage.jsx` | 조회 `Button` **`aria-busy={loading}`** | WCAG 4.1.3 — 비동기 조회 진행 SR 안내 |
| `BillingStatisticsReportPage.jsx` | ①·② 섹션 StatCard **`role="group" aria-label`**·`<Table captionVisuallyHidden>` | 116차·81차 패턴 정합 — coder wire 시 이미 부분 구현, 연도 검증만 보강 |
| `VisitsPage.jsx` | RFID split-view `Alert` — **「검은/빨간 배지」 색 명칭 제거** → 텍스트 라벨만 사용 | §1-2·WCAG 1.4.1 — 116차 단일 탭 모드 수정 후 split-view **회귀** 해소 |
| `VisitsPage.jsx` | split-view 열 — **`<section aria-labelledby>`+`h4 id`** (계획/청구) | WCAG 1.3.1 — 2열 비교 landmark 식별 |
| `styles/components.css` | **`.ds-billing-report__summary .ds-stat` `forced-colors` 경계선** | WCAG 1.4.11 — G26 StatCard 고대비 식별 |
| `styles/components.css` | **`.ds-visits-split-compare`** — `h4` 타이포·열 `section` `forced-colors` 경계선 | split-view 시각·고대비 정합 |

### 43-3. `BillingReportsContextNav` 확장

G26 추가로 `REPORTS_LINKS` 6항목 — 청구·입금·수납·환불·**본인부담 통계**·간편계산기. 기존 `.ds-context-nav`·`NavLink`·`aria-current="page"` 패턴 유지(81차).

### 43-4. 접근성 (WCAG 2.1 AA)

| 점검 | 결과 |
|------|------|
| G26 연도 필드 검증 | `Field error`+`aria-invalid` ✅ |
| G26 조회 busy | `aria-busy` ✅ |
| G26 StatCard·표 | `role="group"`·`captionVisuallyHidden` ✅ |
| split-view 색 의존 | 제거 — 텍스트 라벨만 ✅ |
| split-view landmark | `section`+`aria-labelledby` ✅ |
| forced-colors StatCard·split 열 | 경계선 보강 ✅ |

### 43-5. coder 전달 메모

- G26·대장류 신규 리포트 페이지는 **`BillingReportsContextNav`** 상단 연동 + `.ds-billing-report-print-zone` 인쇄 스코프 재사용.
- `VisitsPage` 청구반영 안내는 **모든 모드**(단일 탭·RFID split-view)에서 색 명칭 금지 — `BILLING_CLAIM_REFLECTION_STATUS` 텍스트 라벨만 인용.
- RFID split-view 열 추가 시 `<section aria-labelledby>`+고유 `h4 id` 필수.

### 43-6. 검증

- `BillingStatisticsReportPage.test.jsx` **4/4 PASS** · `VisitsPage.test.jsx` **11/11 PASS**.
- `npm test`·`npm run build` PASS.

---

## 44. USER_STORIES 미완료 화면군 공통 스타일 보강 + 토큰 정합 (118차) [UXD]

<!-- doc:owner=UXD doc:audience=PLN,COD,TSR updated=2026-06-16 -->

> **118차 UXD (2026-06-16)** — USER_STORIES 미완료 항목 중 화면 공통 레이어가 필요한 구간(US-A01 `/platform`, US-H01 `/dashboard`, US-E01 `/attendance/checkin`, US-E04 `/guardian/checkin`) 대비로 `components.css`를 보강하고, CSS 토큰 일관성 회귀를 수정.

### 44-1. 대상 스타일

| 파일 | 범위 |
|------|------|
| `styles/components.css` | `.ds-transport-log__*` 토큰 변수 정합 |
| `styles/components.css` | `.ds-role-home-grid`·`.ds-role-home-card*` |
| `styles/components.css` | `.ds-attendance-actions` |
| `styles/components.css` | `.ds-qr-checkin-targets*` |
| `styles/components.css` | `.ds-platform-org-form__group` |

### 44-2. 보강 내용

| 항목 | 조치 | 근거 |
|------|------|------|
| 토큰 단일 원천 | `--ds-*` 비표준 변수(`--ds-space-3`, `--ds-color-border` 등) 11건을 표준 토큰(`--space-*`, `--color-*`, `--radius-*`)으로 교체 | §1-4 토큰 단일 원천, CSS 테마/고대비 일관성 |
| 역할별 홈 카드 레이어 | `.ds-role-home-grid`, `.ds-role-home-card`, `.ds-role-home-card__meta` 추가 | US-H01/H02 대시보드 카드형 정보 구조 재사용 |
| 수기 출석 액션 그룹 | `.ds-attendance-actions` 추가 | US-E01 행 액션 버튼 묶음 일관화 |
| 보호자 QR 대상 선택 | `.ds-qr-checkin-targets`, `__item` 추가 | US-E04 다중 연결 이용자 선택 리스트 일관화 |
| 플랫폼 온보딩 폼 그룹 | `.ds-platform-org-form__group` 추가 | US-A01 조직 생성 폼 `fieldset` 대체 컨테이너 스타일 |

### 44-3. 접근성 재점검

| 점검 | 결과 |
|------|------|
| 터치 타깃 | 액션 컨테이너가 기존 `.ds-btn` 최소 높이(44px) 규칙과 충돌 없음 ✅ |
| 정보 구조 | 카드/리스트 레이어는 시맨틱 태그(`section`/`ul`/`li`) 적용 시 즉시 사용 가능 ✅ |
| 색 의존 | 신규 클래스는 상태 색 대신 구조·여백·경계선 중심으로 정의, 텍스트 라벨 전제 유지 ✅ |
| 다크/고대비 | 신규 클래스가 전부 시맨틱 토큰 사용(`var(--color-*)`) ✅ |

### 44-4. coder 전달 메모

- US-A01/H01/E01/E04 화면 구현 시 신규 공통 클래스를 우선 재사용하고 도메인별 변형만 최소 확장할 것.
- `styles/components.css`에 `--ds-*` 접두 변수를 새로 추가하지 말고 기존 토큰 체계(`--space-*`, `--color-*`, `--font-size-*`)만 사용할 것.
- QR 대상 선택 UI는 `ul/li + Button` 조합으로 구현해 키보드 포커스 흐름을 유지할 것.

### 44-5. 검증

- 스타일 레이어 변경으로 런타임 동작 영향 없음(구조 클래스 추가 + 토큰 치환).
- 구현 연계 시 `npm test`·`npm run build`로 화면 연결 회귀를 확인.

---

## 45. 요양 간호 리포트 care-scoped 서브 네비 + G21 split-view 후속 UI 접근성 재점검 (119차) [UXD]

<!-- doc:owner=UXD doc:audience=PLN,COD,TSR updated=2026-06-16 -->

> **119차 UXD (2026-06-16)** — coder `58ee122`(L03_M09/M10/M14 `CareNursingServiceReportPage` + `CareNursingServiceReportNav`)·`4c9103d`(G21 split-view 청구반영 요약 칩)·`cb457b7`(G21 split-view 미반영 후속 확인 목록) wire 직후 접근성 재점검 및 `.ds-context-nav--sub` 미정의 클래스 해소.

### 45-1. 대상 화면·컴포넌트

| 컴포넌트 | 위치 | 비고 |
|----------|------|------|
| `pages/CareNursingServiceReportPage.jsx` | `/care/reports/nursing-service`·`/care/reports/hospital-visits`·`/care/reports/medication-delivery` (L03_M09/M10/M14) | 3경로 공유 care-scoped 간호급여 리포트 |
| `components/ui/CareNursingServiceReportNav.jsx` | 위 3경로 서브 네비 | `ds-context-nav--sub` |
| `components/ui/NursingServiceReportPanel.jsx` | 위 리포트 패널 | StatCard·Table |
| `pages/VisitsPage.jsx` | `/visits` | G21 청구반영 요약 칩 + 미반영 후속 확인 목록 |
| `styles/components.css` | `.ds-context-nav--sub*` | 서브 컨텍스트 네비 신규 정의 |

### 45-2. 재점검·보강 항목

| 파일 | 조치 | 근거 |
|------|------|------|
| `styles/components.css` | **`.ds-context-nav--sub` 신규 정의** — 서브 네비 링크 `font-size: xs`, `min-height: control-height-sm`, `background: surface-muted`로 상위 컨텍스트 네비와 시각 계층 분리 | FE-16 · §1 단일 원천 — `CareNursingServiceReportNav`가 `ds-context-nav--sub` 클래스를 사용하나 CSS **미정의** 상태였음(80차 `.ds-text-input` 패턴 회귀 해소) |
| `CareNursingServiceReportPage.jsx` | 필터 폼 `aria-label="요양 간호 리포트 조회 조건"` ✅ · 조회 버튼 `aria-busy` ✅ · `NursingServiceReportPanel`에 위임(a11y 포함) ✅ | WCAG 4.1.3 · 3.3.2 — 비동기 진행·입력 오류 SR 안내 |
| `CareNursingServiceReportNav.jsx` | `nav aria-label="요양 간호 리포트 종류"` ✅ · `NavLink` `aria-current="page"` ✅ | WCAG 4.1.2 · 2.4.6 — 서브 네비 landmark·활성 경로 명확화 |
| `NursingServiceReportPanel.jsx` | `role="group" aria-label` StatCard 래퍼 ✅ · `Table captionVisuallyHidden caption` 3종 ✅ · `th scope="col"` ✅ | WCAG 1.3.1 — 116차·81차 패턴 정합, coder wire 시 이미 구현 |
| `VisitsPage.jsx` | 청구반영 요약 `div role="group" aria-label="청구반영 현황"` ✅ | 116차 패턴 정합 |
| `VisitsPage.jsx` | 미반영 후속 확인 `section aria-label="청구반영 후속 확인 목록"` + `h3` + `ul/li` ✅ · 상태 라벨은 텍스트(`statusLabel`) 병행(색만 의존 금지) ✅ | WCAG 1.4.1 · 1.3.1 · 2.4.6 |

### 45-3. `ds-context-nav--sub` 스타일 정의

2단 컨텍스트 네비(`CareNursingServiceReportNav` 등)가 상위 컨텍스트 네비(`CareReportContextNav`) 아래에 배치될 때 시각 계층을 명확히 분리한다:

- 링크 글자크기 `xs(12px)` — 상위 `sm(14px)` 대비 축소
- 최소 높이 `control-height-sm(36px)` — 상위 `touch-target-min(44px)` 대비 축소 (터치 타깃 주요 화면이 아닌 보조 탐색)
- 기본 배경 `surface-muted` — 상위 `surface(white)` 대비 회색 배경으로 계층 시각화
- 활성 상태 `primary-soft` + `primary` 경계·색 — 상위 컨텍스트 네비와 동일 패턴 유지
- `forced-colors` 별도 선택자 불요 — 부모 `.ds-context-nav__link` 선택자가 이미 `ButtonText` 경계선 적용

### 45-4. 접근성 (WCAG 2.1 AA)

| 점검 | 결과 |
|------|------|
| 서브 네비 landmark | `nav aria-label="요양 간호 리포트 종류"` ✅ |
| 서브 네비 활성 경로 | `aria-current="page"` (`NavLink` 기본) ✅ |
| 서브 네비 시각 계층 | `ds-context-nav--sub` CSS 정의로 해소 ✅ |
| 서브 네비 강제 색상 | 상위 `.ds-context-nav__link` forced-colors 선택자 상속 ✅ |
| 리포트 StatCard 그룹 | `role="group" aria-label` ✅ (NursingServiceReportPanel) |
| 리포트 표 caption | `captionVisuallyHidden caption` 3종 ✅ |
| G21 반영 현황 칩 | `role="group" aria-label` + 텍스트 라벨 병행 ✅ |
| G21 후속 확인 목록 | `section aria-label` + `ul/li` + 상태 텍스트 라벨 ✅ |
| 색만으로 의미 전달 | 반영/미반영 상태는 `statusLabel` 텍스트 병행(색 단독 금지) ✅ |

### 45-5. coder 전달 메모

- care-scoped 서브 네비 추가 시 **`ds-context-nav--sub`** 클래스를 상위 `ds-context-nav`와 함께 사용하면 단일 CSS 정의로 시각 계층이 분리된다(별도 인라인 style 금지).
- G21 split-view 확장 시 상태 라벨은 **`BILLING_CLAIM_REFLECTION_STATUS[status].label`** 텍스트만 사용 — 배지 색/위치 명칭 금지(42차 결정).
- 후속 확인 목록 `section`에 `aria-label` 대신 `aria-labelledby`를 쓸 경우 `h3`에 안정적인 `id`를 부여할 것(현재 `aria-label` 방식도 유효).

### 45-6. 검증

- `npm test` **1526/1526 PASS** (319 test files) · `npm run build` PASS.
- `CareNursingServiceReportPage.test.jsx`·`VisitsPage.test.jsx` 기존 회귀 유지.

---

## 46. US-T02 Kakao map instance 중앙화·비교 레이아웃 CSS + 토큰 위반 해소 (120차) [UXD]

<!-- doc:owner=UXD doc:audience=PLN,COD,TSR updated=2026-06-16 -->

> **120차 UXD (2026-06-16)** — coder `b000d92`(QA-B113 Kakao map SDK preview) 이후 dirty tree(`KakaoBareMap`·`kakaoMapInstance.js`·`useKakaoMap.js` 리팩터, QA-B114 WIP) 접근성·토큰 정합 재점검.

### 46-1. 대상 화면·컴포넌트

| 컴포넌트 | 위치 | 비고 |
|----------|------|------|
| `components/transport/KakaoTransportMap.jsx` | 배차 경로 미리보기 컨테이너 | `sdkReady` state·`seedMarkers` 선행 마커 |
| `components/transport/KakaoTransportMapView.jsx` | 카카오맵 SDK 렌더 뷰 | `mapEnabled` prop·`role="application"` |
| `components/transport/KakaoBareMap.jsx` (신규) | SDK 도메인 확인용 최소 지도 | `role="application"` |
| `lib/kakaoMapInstance.js` (신규) | 지도 인스턴스 팩토리·유틸리티 | 좌표 정규화·뷰포트 추정·폴리라인 단순화 |
| `lib/useKakaoMap.js` (신규) | 컨테이너당 지도 1회 생성 훅 | cleanup·`ready` 상태 노출 |
| `styles/components.css` | `.ds-transport-map-compare*`·`.ds-transport-map__canvas-wrap` | 비교 레이아웃·토큰 정합 |

### 46-2. 접근성 재점검 결과

| 파일 | 조치 | 근거 |
|------|------|------|
| `KakaoTransportMapView.jsx` | `role="application" aria-label="배차 경로 카카오맵"` ✅ | WCAG 4.1.2 — 지도 캔버스 역할 명시 |
| `KakaoTransportMapView.jsx` | 경로 요약 `<p role="status" aria-live="polite">` ✅ | WCAG 4.1.3 — 비동기 경로 계산 완료 시 SR 안내(71차 `FeeSurchargeGuidePanel` 패턴 정합) |
| `KakaoTransportMapView.jsx` | `:empty` 숨김으로 비어 있는 요약 `<p>` 시각 회귀 방지 ✅ | §1 원칙 — 빈 라이브 영역 노출 방지 |
| `KakaoBareMap.jsx` | `role="application" aria-label="카카오 기본 지도"` ✅ | WCAG 4.1.2 |
| `KakaoTransportMap.jsx` | SDK 미설정 시 `Alert tone="warning"` 대체 렌더 → SR 즉시 인지 ✅ | WCAG 4.1.3 — 에러 상태 assertive 알림 |
| `KakaoTransportMap.jsx` | `seedMarkers`로 SDK ready 이전에도 좌표 기반 초기 마커 표시 ✅ | §1 — 로딩 중 빈 화면 방지 |
| `styles/components.css` | `background: #f2f2f2` → `background: var(--color-surface-muted)` (**토큰 위반 해소**) | FE-16·§1 단일 원천 — 다크 모드·고대비 모드 자동 전환 복구 |
| `styles/components.css` | `font-weight: 600` → `font-weight: var(--font-weight-semibold)` (`.ds-transport-map-compare__label`) | FE-16·§1 단일 원천 |
| `styles/components.css` | `.ds-transport-map__canvas img` `max-width/max-height: none !important` ✅ | 전역 `max-width` 규칙에 의한 Kakao Maps 타일 렌더 깨짐 방지(카카오 SDK 제약) |

### 46-3. 신규 CSS 클래스

| 클래스 | 역할 |
|--------|------|
| `.ds-transport-map__canvas-wrap` | 지도 캔버스 비율 고정 컨테이너(`320px / min 280px`) |
| `.ds-transport-map-compare` | 2열 비교 그리드(`gap: space-4`, 960px+ 2열, 모바일 단열) |
| `.ds-transport-map-compare__pane` | 비교 열 `min-width: 0` 오버플로 방지 |
| `.ds-transport-map-compare__label` | 비교 열 제목(`font-size: sm`, `font-weight: semibold`, `color: text-secondary`) |
| `.ds-transport-map-compare__status` | 비교 열 상태 텍스트(`font-size: sm`) |

> **`forced-colors`**: `.ds-transport-map__canvas`는 기존 `CanvasText` 경계선 선택자에 이미 포함돼 있으므로 비교 레이아웃 컨테이너 `.ds-transport-map-compare__pane`에 추가 forced-colors 규칙 불요(내부 canvas가 경계선을 가짐).

### 46-4. `kakaoMapInstance.js` 유틸리티 설계 결정

- **단일 인스턴스 팩토리** — `createKakaoMapInstance(kakao, container, center, level)` 하나로 지도 생성·컨테이너 바인딩을 중앙화. 컴포넌트별 `new kakao.maps.Map(...)` 직접 호출 금지.
- **좌표 정규화** — `normalizeMapPoint`가 `lat/lng`를 `Number.isFinite` 검사 후 통과시켜 NaN·null 좌표로 인한 SDK 오류를 방지.
- **폴리라인 단순화** — `simplifyMapPath(path, maxPoints)` 경로 점 수를 상한(120)으로 줄여 모바일에서 렌더 성능 확보.
- **뷰포트 자동 추정** — `estimateMapLevelForPoints`로 정차 범위에 맞는 초기 줌 레벨 계산(생성 후 `setBounds/setLevel` 연속 호출 회피).

### 46-5. `useKakaoMap` 훅 패턴

```jsx
// 컨테이너 당 Map 1회만 생성, ready=true 이후 오버레이 페인팅
const { ready } = useKakaoMap(containerRef, { center, level });
```

- `mapEnabled=false` 상태에서는 컨테이너를 마운트만 하고 SDK 초기화를 보류(`KakaoTransportMapView`와 동일 패턴 공유 예정).
- cleanup 함수에서 `clearLayer` + `mapRef.current = null` 처리해 컴포넌트 unmount 시 SDK 메모리 누수 방지.

### 46-6. 접근성 (WCAG 2.1 AA)

| 점검 | 결과 |
|------|------|
| 지도 캔버스 역할 명시 | `role="application"` + `aria-label` ✅ |
| 경로 요약 라이브 영역 | `role="status" aria-live="polite"` 상시 상주 ✅ |
| SDK 미설정 대체 텍스트 | `Alert tone="warning"` ✅ |
| 색 의존 없음 | 경로 요약은 텍스트(`summaryText`) — 폴리라인 색 단독 의존 금지 ✅ |
| 토큰 단일 원천 | raw hex 0건 ✅ |
| 다크 모드 | `var(--color-surface-muted)` 자동 반전 ✅ |
| `forced-colors` | canvas 기존 `CanvasText` 경계선 적용 유지 ✅ |

### 46-7. coder 전달 메모

- `KakaoBareMap`·`KakaoTransportMapView` 모두 `createKakaoMapInstance`만 사용하고 `new kakao.maps.Map(...)` 직접 호출은 `kakaoMapInstance.js` 내부에서만 허용.
- `useKakaoMap` 훅은 준비 완료 후 `ready=true`를 반환하므로 오버레이(마커·폴리라인) 페인팅은 `ready` 확인 이후 수행.
- `.ds-transport-map__canvas-wrap` 높이(`320px`)를 페이지 레이아웃 상황에 따라 변경할 경우 `components.css` 토큰 방식으로 변경하고 인라인 `style` 사용 금지.
- QA-B114 해소 후 `pilotPageFlows` transport E2E에 지도 인스턴스 1회 생성 회귀를 추가할 것.

### 46-8. 검증

- `npm test` **1537/1538 PASS**(1 pre-existing jsdom 오염 — `BodyRestraintRecordPage.test.jsx` 단독 PASS·본 변경 무관) · `npm run build` PASS.
- CSS 토큰 위반 0건(raw hex · 하드코딩 font-weight 모두 제거).

---

## 47. US-E04 QR 대상 선택 + §44 공통 클래스 연동 + `--color-accent` + US-T02 split-view a11y (122차) [UXD]

<!-- doc:owner=UXD doc:audience=PLN,COD,TSR updated=2026-06-17 -->

> **122차 UXD (2026-06-17)** — 118차(§44)에서 추가한 공통 CSS가 페이지에 연결되지 않았고, `--color-accent` 미정의·US-T02 split-view 정차 목록 SR 중복 라벨 잔여를 해소.

### 47-1. 대상 화면·컴포넌트

| 컴포넌트 | 위치 | 비고 |
|----------|------|------|
| `components/ui/QrCheckinTargetsPanel.jsx` | 보호자 QR 체크인 | US-E04 복수 이용자 선택 |
| `pages/GuardianCheckinPage.jsx` | `/guardian/checkin` | 1명 자동 선택 · 2명+ 패널 |
| `pages/AttendancePage.jsx` | `/attendance/checkin` | `.ds-attendance-actions` |
| `pages/PlatformPage.jsx` | `/platform` | `.ds-platform-org-form__group` |
| `components/transport/TransportRouteSplitView.jsx` | 배차 편집 | landmark `section` + `h4` |
| `components/transport/TransportStopList.jsx` | 정차 목록 | SR 중복 라벨 제거 |
| `styles/tokens.css` | `--color-accent*` | branch pin · stop 라벨 |
| `styles/components.css` | `.ds-qr-checkin-targets*` · `.ds-transport-route-split` | 선택 상태 · 2열 그리드 |

### 47-2. 접근성 재점검 결과

| 파일 | 조치 | 근거 |
|------|------|------|
| `QrCheckinTargetsPanel` | `role="radiogroup"` + `role="radio"` + `aria-checked` + `Field error`/`role=alert` | WCAG 4.1.2 · 3.3.1 — FLOWCHART §5-2 복수 이용자 대상 선택 |
| `GuardianCheckinPage` | 1명 연결 시 `role=status` 단일 표시(자동 선택) · 2명+ 패널 | US-E04 인수 조건 |
| `TransportStopList` | `<li aria-label>` 제거 — 내부 `button aria-label`만 유지 | WCAG 4.1.2 — SR 중복 낭독 방지 |
| `TransportRouteSplitView` | `section aria-labelledby` + `h4` 「경로 지도」/「정차 목록」 | WCAG 1.3.1 — Card `h2` → section `h3` → split `h4` 계층 |
| `tokens.css` | `--color-accent` 시맨틱 토큰(l/d) | FE-16 — `.ds-transport-map-pin--branch` raw hex fallback 제거 |
| `components.css` | `.ds-qr-checkin-targets__item[aria-checked=true]` · `forced-colors` Highlight | WCAG 1.4.1 — 선택 상태 색+경계선 병행 |

### 47-3. coder 전달 메모

- 보호자 QR 대상 선택은 **Select 대신 `QrCheckinTargetsPanel`**(2명+)을 사용 — 모바일 44px 터치·radiogroup 키보드 탐색 일관.
- `--color-accent`는 **지점(센터) 정차** 전용 — 일반 info tone과 구분해 branch pin·branch stop name에만 사용.
- `.ds-role-home-grid` / `.ds-role-home-card*`는 대시보드 역할별 홈 카드 레이아웃용 — `DashboardPage`·`HqDashboardPage` 신규 위젯 추가 시 재사용.

### 47-4. 검증

- `QrCheckinTargetsPanel.test.jsx` 3 · `TransportRouteSplitView.test.jsx` 1 · `GuardianCheckinPage.test.jsx` 갱신.
- `npm test` · `npm run build` PASS.

---

## 48. US-T05 G15 TransportServiceLogPanel 일지④ 접근성 (123차) [UXD]

<!-- doc:owner=UXD doc:audience=PLN,COD,TSR updated=2026-06-17 -->

> **123차 UXD (2026-06-17)** — coder `7a4b310` G15 별지 제22호 이동서비스일지④ `PUT` persistence wire 직후 `TransportServiceLogPanel` 미점검 갭(QA-B116) 해소.

### 48-1. 대상 화면·컴포넌트

| 컴포넌트 | 위치 | 비고 |
|----------|------|------|
| `components/transport/TransportServiceLogPanel.jsx` | `TransportRunDetailPage` 탭 | G15 별지 제22호 · `upsertTransportServiceLogApi` |
| `components/ui/Badge.jsx` | `TRANSPORT_TIME_COMPLIANCE_STATUS` | 준수/지연/미기록/계획없음 tone |
| `styles/components.css` | `.ds-transport-log__record` | `forced-colors`·토큰화 legend |

### 48-2. 접근성 재점검 결과

| 파일 | 조치 | 근거 |
|------|------|------|
| `TransportServiceLogPanel` | 정차별 `Field` 라벨에 **이용자명 컨텍스트**(`${name} 실제 픽업` 등) | WCAG 2.4.6 — 복수 fieldset 동일 라벨 SR 식별 불가 |
| `TransportServiceLogPanel` | 시간 준수 열 **`StatusBadge`**(`TRANSPORT_TIME_COMPLIANCE_STATUS`) | WCAG 1.4.1 — 색상 클래스만으로 상태 구분 금지 |
| `TransportServiceLogPanel` | 미확정 경고 `id` + 인쇄·다운로드 `aria-describedby` | WCAG 1.3.1 — 미리보기 맥락 SR 전달 |
| `TransportServiceLogPanel` | 기록 `section`+sr-only `h3`·요약 `role=status`·표 `captionVisuallyHidden` | WCAG 1.3.1·4.1.3 |
| `components.css` | `legend` semibold 토큰·`forced-colors` fieldset 경계선 | FE-16·WCAG 1.4.11 |

### 48-3. coder 전달 메모

- 일지④ 저장은 **확정(CONFIRMED) 배차 + `runId`** 일 때만 `upsertTransportServiceLogApi` 호출 — DRAFT는 로컬 미리보기·인쇄만.
- 시간 준수 Badge는 `transportTimeCompliance.js`의 한국어 라벨(`준수`/`지연`/`미기록`/`계획없음`)과 **키 일치** 유지.
- 인쇄 스코프는 기존 `body.ds-transport-log-printing` + `.ds-transport-log__document` 패턴 재사용.

### 48-4. 검증

- `TransportServiceLogPanel.test.jsx` **8/8 PASS** (+1 contextual label·badge·guard).
- `npm test` · `npm run build` PASS.

---

## 49. US-T05 G15 이동서비스 월간 리포트(2-7/2-8) 접근성 재점검 (124차) [UXD]

<!-- doc:owner=UXD doc:audience=PLN,COD,TSR updated=2026-06-17 -->

> **124차 UXD (2026-06-17)** — 123차(§48) 이후 coder 신규 커밋 `6a18dfd`(G15 2-7/2-8 월간 이동서비스 변동·입소자 현황 리포트 신규 페이지 `TransportMonthlyReportsPage`) 미점검 갭 해소. 같은 시기 신설된 `BillingStatisticsReportPage`(G26)와 구조가 거의 동일한 리포트 페이지인데, 그 페이지에서 이미 확립한 ① 섹션 헤딩 레벨, ② StatCard 요약 그룹 시맨틱, ③ 조회 버튼 `aria-busy` 표준을 따르지 않아 발생한 회귀 3건을 정합.

### 49-1. 대상 화면·컴포넌트

| 컴포넌트 | 위치 | 비고 |
|----------|------|------|
| `pages/TransportMonthlyReportsPage.jsx` | `/transport/monthly-reports` | G15 2-7·2-8 · 케어포 func.php 2-7/2-8 |
| `styles/components.css` | `.ds-transport-monthly-report__summary` | StatCard `forced-colors` 경계선 |

### 49-2. 접근성 재점검 결과

| 파일 | 조치 | 근거 |
|------|------|------|
| `TransportMonthlyReportsPage` | 섹션 제목 `h2`→**`h3`**(AppShell `h1` → Card `h2` → 섹션 `h3`) | WCAG 1.3.1·2.4.6 — Card `h2` 내부 섹션이 동일 레벨로 중복(§44/116차 패턴 회귀) |
| `TransportMonthlyReportsPage` | StatCard 래퍼 `div`에 **`role="group" aria-label="…요약"`** 2건 | WCAG 1.3.1 — 집계 카드 묶음 SR 식별(§42·93차 패턴) |
| `TransportMonthlyReportsPage` | 「조회」버튼 **`aria-busy={loading}`** | WCAG 4.1.3 — 조회 진행 SR 안내(`BillingStatisticsReportPage` 정합) |
| `TransportMonthlyReportsPage` | StatCard 그리드 `ds-grid--stats`(160px) 정렬 + `.ds-transport-monthly-report__summary` | 5칸 입소자 요약 컬럼 정합·`forced-colors` 경계선 |

### 49-3. coder 전달 메모

- 본 변경은 committed `6a18dfd` 파일만 수정(순수 접근성 정합 — 데이터·API·동작 불변).
- 신규 리포트 페이지는 `BillingStatisticsReportPage`(G26) 골격을 **단일 원천 패턴**으로 따를 것 — 섹션 `h3.ds-card__title`, StatCard 그리드 `ds-grid ds-grid--stats … __summary role=group`, 조회 버튼 `aria-busy`.
- 변동 유형 Badge는 `transportMonthlyReports.js`의 `TRANSPORT_VARIATION_TYPE` 라벨과 키 일치 유지(색+텍스트 병행).

### 49-4. 검증

- `TransportMonthlyReportsPage.test.jsx` **1/1 PASS** (+heading level 3·StatCard group 단언 추가).
- `npm test` **1596/1596 PASS** · `npm run build` PASS.

---

## 50. G15 이동서비스일지 감사추적 + 모니터링/간호 연계 패널 토큰 정합 (125차) [UXD]

<!-- doc:owner=UXD doc:audience=PLN,COD,TSR updated=2026-06-17 -->

> **125차 UXD (2026-06-17)** — 124차(§49) 이후 coder 신규 커밋(`3cc5a08` G15 이동서비스일지 감사추적 read API wire·`8b68fdb` G30/G24b/G21/G26 모니터링 근거 일관 패널 `MonitoringEvidenceContextPanel`·`140bf92` L02·L03 간호 리포트 연계 패널 `CareNursingParityPanel`) 미점검 갭 해소. 신규 패널 2종(`8b68fdb`·`140bf92`)은 `aside`/`nav` landmark·`aria-label`·`role="status"`·`ul/li` 시맨틱을 이미 갖춰 접근성 결함은 없었고, 잔여는 **토큰 단일 원천(§1-4·FE-16) 회귀 2건**.

### 50-1. 대상 화면·컴포넌트

| 컴포넌트 | 위치 | 비고 |
|----------|------|------|
| `components/transport/TransportServiceLogPanel.jsx` | `/transport/runs/:id` 탭 | G15 별지 제22호 일지 + 감사추적 표(`3cc5a08`) |
| `components/monitoring/MonitoringEvidenceContextPanel.jsx` | G30·G24b·G21·G26 페이지 | BNK-273 모니터링 근거 연계 `aside`(`8b68fdb`) |
| `components/ui/CareNursingParityPanel.jsx` | L02·L03 간호 리포트 페이지 | 제공기록 연계 `aside`(`140bf92`) |
| `styles/components.css` | `.ds-monitoring-evidence-context*`·`.ds-care-nursing-parity*` | 간격 토큰 정합 |

### 50-2. 접근성·정합 재점검 결과

| 파일 | 조치 | 근거 |
|------|------|------|
| `TransportServiceLogPanel` | 감사·본문 빈 상태 안내 `className`을 **미정의 `ds-empty-hint` → 정의된 `ds-text-muted`**로 교체(2곳) | FE-16·§1 단일 원천 — `ds-empty-hint`는 `components.css` 미정의로 색·`forced-colors` 토큰을 못 받던 80·90·97차 패턴 회귀. `ds-text-muted`는 `--color-text-muted`(4.76:1) + `forced-colors`에서 `--color-text-secondary`로 승격(line 2400) |
| `MonitoringEvidenceContextPanel`·`CareNursingParityPanel` CSS | `gap: 0.5rem`·`0.75rem 1rem` 등 raw rem → **`var(--space-2)`·`var(--space-3) var(--space-4)`** | §1-4·§4 — 컴포넌트 간격은 토큰만 사용(118·120차 raw 값 → 토큰 패턴) |
| `MonitoringEvidenceContextPanel` | `aside aria-label`·`nav aria-label`·증빙기간 `role="status"`·`ul/li` — 정합 확인(변경 불요) | WCAG 1.3.1·4.1.3 |
| `CareNursingParityPanel` | `aside aria-label`·`nav aria-label`·`ul/li` — 정합 확인(변경 불요) | WCAG 1.3.1 |
| `TransportServiceLogPanel` 감사추적 | `section aria-labelledby` + 가시 `h3`·이력 `Table` `captionVisuallyHidden`·`<time dateTime>`·미저장 상태 텍스트+색 병행 — 정합 확인(변경 불요) | WCAG 1.3.1·1.4.1 |

### 50-3. coder 전달 메모

- 빈 상태/도움말 muted 안내문은 일회성 클래스 신설 대신 **`ds-text-muted`**(또는 표 안이면 `ds-table-empty`)를 사용할 것 — 색·`forced-colors` 대비가 단일 원천에서 일관 적용됨.
- 신규 패널 CSS는 `--space-*` 토큰만 사용(raw rem 금지) — `MonitoringEvidenceContextPanel`·`CareNursingParityPanel`이 기준 패턴.
- `MonitoringEvidenceContextPanel`/`CareNursingParityPanel`은 배경·테두리가 없는 텍스트+링크 `aside`라 `forced-colors` 경계선이 불필요(링크 색은 시스템 색으로 유지).

### 50-4. 검증

- `TransportServiceLogPanel.test.jsx`·`MonitoringEvidenceContextPanel.test.jsx`·`CareNursingParityPanel.test.jsx` **14/14 PASS**.
- `npm test` **1605/1605 PASS** · `npm run build` PASS.

---

## 51. 커스텀 DateInput/TimeInput 피커 + G15 경유지·ETA 칩 접근성 (127차) [UXD]

<!-- doc:owner=UXD doc:audience=PLN,COD,TSR updated=2026-06-17 -->

> **127차 UXD (2026-06-17)** — 126차(§50) 이후 coder 신규 커밋(`ea5d896` native `type=date|time` 대체 커스텀 피커·`bf73c4c` `TransportAddWaypointModal`·`TransportStopList` ETA 칩·`96db8bf` 배차 compact layout) 미점검 갭 해소.

### 51-1. 대상 화면·컴포넌트

| 컴포넌트 | 위치 | 비고 |
|----------|------|------|
| `components/ui/DateInput.jsx` | 전역 폼 | `DatePickerCalendar` 팝오버 |
| `components/ui/DatePickerCalendar.jsx` | DateInput 내부 | `ds-calendar` 토큰 재사용 |
| `components/ui/TimeInput.jsx` | `TransportRunNewPage` 등 | 시·분 `Select` 복합 필드 |
| `components/ui/Field.jsx` | 전역 | `labelId`·단일 자식 `cloneElement` |
| `components/transport/TransportAddWaypointModal.jsx` | 배차 편집 | 경유지 주소 입력 |
| `components/transport/TransportStopList.jsx` | 배차 split-view | ETA·지연 칩 |
| `styles/components.css` | `.ds-date-picker*`·`.ds-time-picker*`·`.ds-transport-stop__time-chip-status` | `forced-colors` |

### 51-2. 접근성·정합 재점검 결과

| 파일 | 조치 | 근거 |
|------|------|------|
| `DateInput` | 팝오버 열림 시 선택일/오늘 버튼 포커스·닫힘 시 트리거 복귀 | WCAG 2.4.3 — 키보드 포커스 맥락 유지 |
| `DateInput` | `labelId`→dialog `aria-labelledby` (없으면 `aria-label="날짜 선택"`) | WCAG 1.3.1·4.1.2 — 필드 라벨과 달력 대화상자 연결 |
| `DatePickerCalendar` | 이전/다음 달 **비표시 일자 `disabled`** | WCAG 3.3.2 — 잘못된 월 선택 방지 |
| `TimeInput` | 시 `Select`에 `Field` `htmlFor` `id`·분 `Select` `aria-label="분"`·`aria-describedby`는 시 선택에 연결 | WCAG 1.3.1 — `role=group`+`htmlFor` 이중 라벨 회귀 방지 |
| `Field` | `<label id={fieldId-label}>`·`labelId` controlProps·단일 React 자식 `cloneElement` | render-prop 미사용 `TransportRunNewPage` 등 정합 |
| `TransportAddWaypointModal` | 주소 미입력 **`Field error`**+`aria-invalid` (폼 상단 `Alert` 제거) | WCAG 3.3.1 — 필드 단위 오류 식별 |
| `TransportStopList` | 지연 ETA 칩 가시 **「지연」** 텍스트 + 기존 `aria-label` | WCAG 1.4.1 — 색만 의존 금지 |
| `components.css` | date/time picker·지연 칩 `forced-colors` 경계선 | WCAG 1.4.11 |

### 51-3. coder 전달 메모

- 신규 날짜·시간 입력은 **native `type=date|time` 금지** — `DateInput`/`TimeInput`+`Field`만 사용(28·64차 규율 유지).
- `Field`에 단일 UI 자식을 직접 넣어도 `cloneElement`로 `id`·`labelId`·`aria-describedby`가 전달됨 — render-prop과 동등.
- `TimeInput`은 첫 `Select`(시)에 `Field` `htmlFor` `id`를 부여 — `role=group`+`aria-labelledby`와 `htmlFor`를 동시에 쓰지 말 것(중복 accessible name).
- ETA 지연 표시는 **`.ds-transport-stop__time-chip-status`「지연」** 텍스트 필수 — danger 색 클래스만으로 상태 전달 금지.

### 51-4. 검증

- `DateInput.test.jsx` **5/5** · `TransportAddWaypointModal.test.jsx` **2/2** · `TransportStopList.test.jsx` 갱신.
- `npm test` · `npm run build` PASS.

---

## 52. DatePickerCalendar 키보드 방향키 내비게이션 + roving tabindex (128차) [UXD]

<!-- doc:owner=UXD doc:audience=PLN,COD,TSR updated=2026-06-17 -->

> **128차 UXD (2026-06-17)** — §51(127차)에서 도입한 커스텀 `DateInput` 달력 팝오버는 포커스 진입·복귀·`aria-labelledby`는 갖췄으나, WAI-ARIA *date picker dialog* 패턴의 핵심인 **그리드 키보드 이동**이 없어 키보드 사용자가 날짜를 고르려면 최대 42개 날짜 버튼을 일일이 `Tab` 해야 했다. 이 갭을 roving tabindex + 방향키 내비게이션으로 해소.

### 52-1. 키보드 인터랙션 (달력 그리드)

| 키 | 동작 | 헬퍼 |
|----|------|------|
| `←` / `→` | 1일 이전/다음 | `addDaysToIso(iso, ∓1)` |
| `↑` / `↓` | 1주 이전/다음 | `addDaysToIso(iso, ∓7)` |
| `Home` / `End` | 현재 주의 일요일 / 토요일 | `startOfWeekIso` / `endOfWeekIso` |
| `PageUp` / `PageDown` | 1개월 이전/다음(말일 보정) | `addMonthsToIso(iso, ∓1)` |
| `Enter` / `Space` / 클릭 | 포커스한 날짜 선택 | 날짜 버튼 기본 동작(중복 핸들러 없음) |
| `Esc` | 팝오버 닫고 트리거 복귀 | §51 기존 동작 |

- 이동 결과가 `min`/`max` 경계를 벗어나면 포커스를 옮기지 않는다(스크롤 방지 `preventDefault`는 적용).
- 월 경계를 넘는 이동은 `DateInput.moveFocusTo`가 표시 월을 자동 전환하고, 새 월의 해당 날짜 버튼으로 포커스를 옮긴다.

### 52-2. roving tabindex (포커스 단일화)

| 항목 | 조치 | 근거 |
|------|------|------|
| `DatePickerCalendar` | 그리드에서 `tabindex=0` 날짜 **1개**, 나머지 `-1` | WCAG 2.4.3 — composite widget 단일 탭 스톱 |
| 포커스 대상(`rovingIso`) | `focusDate` → 선택일 → 오늘 → 첫 활성일(현재 월에 보이는 날짜만) | 빈 값·경계에서도 항상 1개 보장 |
| `DateInput` | `focusDate` 상태 + `moveFocusTo`(표시 월 동기화) · 이전/다음 달 버튼도 `addMonthsToIso`로 같은 일자 유지 | 방향키·버튼 내비게이션 일관 |
| 그리드 `<table>` `onKeyDown` | 방향키만 가로채고 선택은 버튼 기본 동작 위임 | 중복 키 핸들러·이중 이벤트 방지 |
| `<caption>`(sr-only) | "…날짜 선택 — 방향키로 이동, Enter로 선택" | WCAG 1.3.1 — 조작 방법 사전 안내 |

### 52-3. coder 전달 메모

- 신규 순수 헬퍼는 **`lib/pickerDate.js`** 에 위치(`addDaysToIso`·`addMonthsToIso`·`startOfWeekIso`·`endOfWeekIso`) — 날짜 산술이 필요하면 `new Date` 직접 사용 대신 재사용할 것(로컬 기준·월/연 경계 자동 처리).
- `DatePickerCalendar`는 `focusDate`·`onFocusDate` props를 받는 **제어 컴포넌트** — 단독 사용 시 부모가 `focusDate`와 표시 월(`year`/`monthIndex`)을 함께 갱신해야 roving 포커스가 정상 동작한다.
- 날짜 선택 로직은 기존대로 버튼 `onClick`(=`onSelectDate`)에 유지 — 그리드 `onKeyDown`에 `Enter`/`Space` 처리를 추가하지 말 것(버튼 기본 동작과 충돌).

### 52-4. 검증

- `DateInput.test.jsx` **9/9**(+4: roving 단일 `tabindex`·방향키 이동+Enter 선택(2026-06-25)·`PageUp` 월 점프(2026-05-17)·`max` 경계 차단).
- 소비처 회귀 — `FeeSurchargeGuidePanel`·`ComplaintConsultationForm`·`TransportCompliancePanel`·`StaffLifecyclePanel` PASS.
- `npm test`(locked) · `npm run build` PASS.

---

## 53. 배차 명단 계획 픽업·직원 건강검진 신규 서류·식사기록 오류 접근성 (129차) [UXD]

<!-- doc:owner=UXD doc:audience=PLN,COD,TSR updated=2026-06-18 -->

> **129차 UXD (2026-06-18)** — §52(128차) 이후 coder 신규 커밋(`e35efb2`·`8e6310a`·`38642e2`) 미점검 갭 해소.

### 53-1. 대상 화면·컴포넌트

| 컴포넌트 | 위치 | 비고 |
|----------|------|------|
| `pages/TransportPage.jsx` | `/transport` 명단 표 | 확정 루트·계획 픽업·지연 Badge (`e35efb2`) |
| `pages/StaffHealthCheckupsPage.jsx` | `/staff/health-checkups` | FAQ 21799 신규 서류 열·StatCard (`8e6310a`) |
| `pages/MealAssistanceRecordPage.jsx` | L02_M13 | malformed API 응답 오류 (`38642e2`) |
| `styles/components.css` | `.ds-inline-cluster` | 인라인 시각·텍스트 클러스터 유틸 |

### 53-2. 접근성·정합 재점검 결과

| 파일 | 조치 | 근거 |
|------|------|------|
| `TransportPage` 배차 루트 `Link` | `aria-label={`${item.name} ${dispatch.stopOrder}번 정차`}` | WCAG 2.4.6 — 동일 「N번 정차」 링크 텍스트 다중 행 구분 |
| `TransportPage` 계획 픽업 지연 | `title` 툴팁 제거 · 가시 「지연」`Badge` + 지연 시 `aria-label` | WCAG 1.4.1·1.4.13 — 색+텍스트·`title`만 의존 금지(§51 `TransportStopList` 정합) |
| `.ds-inline-cluster` | `inline-flex`·`gap: var(--space-2)`·`forced-colors` Badge 경계선 | FE-16 — 클래스 미정의 회귀(80차 `.ds-text-input` 패턴) |
| `StaffHealthCheckupsPage` `newHireDocumentBadge(NA)` | `aria-hidden` 「—」→`ds-text-muted` 가시 대시 | WCAG 4.1.2 — 비대화형 generic에 SR 콘텐츠 숨김 금지 |
| `MealAssistanceRecordPage` 오류 빈 목록 | `ds-help-text`(미정의)→`ds-text-muted`+`role=status` | FE-16·WCAG 4.1.3 |
| `MealAssistanceRecordPage` 표 작업 열 | `ds-visually-hidden`→`ds-sr-only` | 단일 sr-only 유틸(§0·`.ds-sr-only`) |

### 53-3. coder 전달 메모

- 배차 명단 표 **반복 링크·버튼**은 이용자명을 `aria-label`에 포함할 것(`TransportPage`·`GuardianInvitationList` 패턴).
- 상태·지연 표시는 **`title` 툴팁 단독 금지** — 가시 텍스트 Badge 또는 `aria-label` 병행.
- 신규 서류·상태 열에서 **해당 없음(—)** 은 `aria-hidden`으로 숨기지 말고 `ds-text-muted` 텍스트로 노출.
- 인라인 시각 클러스터(시각+Badge)는 **`.ds-inline-cluster`** 사용.

### 53-4. 검증

- `TransportPage.test.jsx`·`StaffHealthCheckupsPage.test.jsx`·`MealAssistanceRecordPage.test.jsx` 회귀.
- `npm test`(locked) · `npm run build` PASS.

---

---

## 54. G15 이동서비스일지 운전자 서명 fieldset + 미정의 transport-log CSS 해소 (130차) [UXD]

<!-- doc:owner=UXD doc:audience=PLN,COD,TSR updated=2026-06-18 -->

> **130차 UXD (2026-06-18)** — §53(129차) 이후 coder 신규 커밋(`b6ce301`·`b4644e8`·`0df6902`·`f51e365`·`1c8f236`) 미점검 갭 해소.

### 54-1. 대상 화면·컴포넌트

| 컴포넌트 | 위치 | 비고 |
|----------|------|------|
| `TransportServiceLogPanel` | `components/transport/` | 운전자 서명 쌍 `fieldset` + CSS 정의 (`f51e365`) |
| `TransportServiceLogLegalGuide` | `components/transport/` | 신규 법정 가이드 카드 (`0df6902`) |
| `StaffHealthCheckupsPage` | `pages/` | HR 파일허브 연결 (`b6ce301`) |
| `TransportCompliancePage` | `pages/` | 법정 가이드 연동 (`0df6902`) |
| `styles/components.css` | `styles/` | `ds-transport-log__*` 8클래스 신규 정의 |

### 54-2. 접근성·정합 재점검 결과

| 파일 | 조치 | 근거 |
|------|------|------|
| `TransportServiceLogPanel` 운전자 서명 | `fieldset.ds-transport-log__signature-group` + `legend="운전자 서명"` — 「서명 성명」·「서명일」두 필드 그룹화 | WCAG 1.3.1 — 의존 쌍 필드는 그룹 시맨틱으로 관계 명시 |
| `ds-transport-log__document` | 본문 래퍼 standalone 정의: 패딩·보더·`border-radius`·`surface-muted` 배경 | FE-16 — `@media print`에만 참조돼 일반 뷰에서 토큰 미수신 |
| `ds-transport-log__heading` | `font-size-lg`·`font-weight-semibold`·하단 여백 | FE-16 — 별지 제22호 제목 스타일 미정의 |
| `ds-transport-log__summary` | dl 그리드(`minmax(7rem,auto) 1fr`)·dt `text-muted`·dd `sm` | FE-16 — 운행 메타 요약 레이아웃 미정의 |
| `ds-transport-log__footnote` | `font-size-xs`·`color-text-muted`·상단 여백 | FE-16 — 보관 각주 스타일 미정의 |
| `ds-transport-log__no-print` | 정상 표시·`@media print` 숨김 규칙 추가 | FE-16 — 입력 전용 영역 인쇄 제어 누락 |
| `ds-transport-log__actions` | standalone `margin-top` 정의 | FE-16 — 인쇄 zone 컨텍스트에만 참조돼 독립 레이아웃 미수신 |
| `ds-transport-log__meta` | standalone meta container 정의 | FE-16 |
| `ds-transport-log__signature-group` | `fieldset` 리셋(margin·padding·border 제거)·`legend` sm 스타일 | 기존 `ds-form-row` 레이아웃 보존 |
| `ds-transport-log__document` `forced-colors` | `ButtonText` 경계선 | WCAG 1.4.11 |
| `TransportServiceLogLegalGuide` | `ds-list-compact`·`ds-text-secondary`·`ds-btn--outline-primary` — 기정의 클래스 확인(변경 불요) | FE-16 확인 PASS |
| `StaffHealthCheckupsPage` | `ds-stat-grid`·`ds-inline-actions--start`·`ds-fieldset` — 기정의 클래스 확인(변경 불요) | FE-16 확인 PASS |

### 54-3. coder 전달 메모

- **운전자 서명 쌍** — `fieldset.ds-transport-log__signature-group`+`legend="운전자 서명"` 안에 `Field label="서명 성명"`·`Field label="서명일"` 배치(이전 독립 라벨 「운전자 서명 성명」·「운전자 서명일」에서 단축). 테스트에서 `getByLabelText` 쿼리를 「서명 성명」·「서명일」로 갱신했으니 맞춰 유지.
- **`ds-transport-log__document`** — 일반 뷰에서 `surface-muted` 배경·보더로 서식지 본문임을 시각적으로 구분. 인쇄 시 기존 `@media print` 규칙 그대로.
- 신규 `ds-transport-log__*` 8종은 기존 transport log CSS 블록(§48·§50·§51) 직후에 위치.

### 54-4. 검증

- `TransportServiceLogPanel.test.jsx` 회귀 갱신(`getByLabelText` 서명 필드 라벨).
- `npm test` **1677/344 PASS** · `npm run build` PASS.

---

## 55. G41 PDF 8-7 필수 교육 알림·8-7-1 리포트·대시보드 위젯 + G21 RFID diff fallback 라벨 (131차) [UXD]

<!-- doc:owner=UXD doc:audience=PLN,COD,TSR updated=2026-06-18 -->

> **131차 UXD (2026-06-18)** — §54(130차) 이후 coder 신규 커밋(`9e91e6a`·`caa215f`·`4a112fe`·`27c9de3`) 미점검 갭 해소.

### 55-1. 대상 화면·컴포넌트

| 컴포넌트 | 위치 | 비고 |
|----------|------|------|
| `StaffTrainingLogPage` | `pages/` | PDF 8-7 필수 미작성 Alert·`formatMandatoryTrainingWriteStatus` StatCard unit (`caa215f`) |
| `StaffRefresherTrainingPage` | `pages/` | 8-7-1 CSV export 버튼 (`caa215f`) |
| `DashboardPage` | `pages/` | `staffTrainingComplianceGapCount` 위젯 (`9e91e6a`) |
| `VisitRfidDiffComparePanel` | `components/visits/` | RFID 7-code diff compare·unknown code fallback (`4a112fe`) |
| `config/visits.js` | `config/` | `resolveVisitRfidDiffCode` 단일 원천 |

### 55-2. 접근성·정합 재점검 결과

| 파일 | 조치 | 근거 |
|------|------|------|
| `StaffTrainingLogPage` 연 1회 안내 | 미정의 `ds-field-help` 분리 `<p>` 제거 → `Field help` prop(교육 유형·연 1회 선택 시) | FE-16·WCAG 1.3.1 — `aria-describedby` 자동 연결 |
| `StaffTrainingLogPage` 신규직원 체크 | raw `<input type=checkbox>` → `Checkbox` 컴포넌트 | DS 표준·키보드·라벨 연결 일관 |
| `StaffTrainingLogPage` 필수 미작성 Alert | `id="staff-training-mandatory-alert"` + 등록 버튼 `aria-describedby` | WCAG 1.3.1 — 비활성 아닌 등록 버튼이 경고 맥락을 SR에 전달 |
| `StaffRefresherTrainingPage` export | `aria-busy`·`disabled` during download · `role="status"`/`role="alert"` on Alerts | WCAG 4.1.3 |
| `StaffRefresherTrainingPage` 이수증 업로드 | 제출 `aria-busy={certificateUploading}` | WCAG 4.1.3 |
| `resolveVisitRfidDiffCode` | 미등록 code → `{ tone: neutral, label: "차이 {code}" }` | WCAG 1.4.1 — raw code만 노출 금지 |
| `VisitRfidDiffComparePanel` 집계 칩 | `aria-label="{label} {count}건"` · count `aria-hidden` | SR 중복 읽기 방지 |
| `.ds-visits-reflection-chip` | `forced-colors` `ButtonText` 경계선 | WCAG 1.4.11 |

### 55-3. coder 전달 메모

- **PDF 8-7 필수 유형** — `PDF_MANDATORY_TRAINING_TYPES`(재난·소방만) 미작성 Alert·StatCard unit 「미작성」은 coder `caa215f` 로직 유지. 직원권익은 Alert 대상 아님.
- **대시보드 위젯** — `STAFF_TRAINING_COMPLIANCE_GAP_WIDGET_LABEL`·`/staff/training-logs` 링크·`countStaffTrainingComplianceGaps` 집계는 변경 불요.
- **RFID unknown code** — BE가 `COMP_11` 등 신규 code를 추가하면 `VISIT_RFID_DIFF_CODES`에 한국어 라벨 등록. 그 전까지 fallback `차이 {code}` 유지.
- **8-7-1 CSV** — `buildRefresherTrainingReportCsv`·`downloadRefresherTrainingReportCsv`는 utils 레이어 — UI는 export 버튼만 `aria-busy` 보강.

### 55-4. 검증

- `StaffTrainingLogPage.test.jsx` — mandatory Alert `aria-describedby` 단언 +1.
- `VisitRfidDiffComparePanel.test.jsx` — unknown code `차이 COMP_11` 라벨 갱신.
- `visits.test.js` — `resolveVisitRfidDiffCode` +1.
- `npm test`·build PASS.

---

## 56. G15 별지 제22호 branch contact·입력 compliance Badge + SideNav §8-2 비주얼 (132차) [UXD]

<!-- doc:owner=UXD doc:audience=PLN,COD,TSR updated=2026-06-18 -->

> **132차 UXD (2026-06-18)** — §55(131차) 이후 coder 신규 커밋(`a1d6e32`·`7de5a6f`·`07be394`·`b1a16ff`·`b1a16ff` G15 별지 제22호 print/input/export·branch contact) 미점검 갭 해소.

### 56-1. 대상 화면·컴포넌트

| 컴포넌트 | 위치 | 비고 |
|----------|------|------|
| `TransportServiceLogPanel` | `components/transport/` | branch contact dl·탑승/하차 direction 라벨·정차 입력 폼 |
| `SideNav` | `layout/SideNav.jsx` | US-UX-05 visual deepen (154차 #5) |
| `sideNavIcons.jsx` | `layout/` | 6그룹 stroke SVG |
| `.ds-sidenav__*` | `components.css` | 브랜드·스크롤·액센트·nested active |

### 56-2. 접근성·정합 재점검 결과

| 파일 | 조치 | 근거 |
|------|------|------|
| `TransportServiceLogPanel` 정차 「시간 준수」 | read-only `TextInput` → `StatusBadge` in `role=status` div + `Field` label | §48 표준과 정합·색+텍스트(WCAG 1.4.1) |
| 감사추적 「미저장 변경 있음」·「미완료」 | `.ds-transport-log__audit-warning` span → `Badge tone=warning` | 색+텍스트 병행 |
| 기관 `tel:` 링크 | `aria-label="대표 연락처 {번호} 전화 걸기"` | WCAG 2.4.6 |
| 인쇄 본문 래퍼 | `div aria-label` → `section`+sr-only `h3`「이동서비스일지 본문」 | WCAG 1.3.1 landmark |
| `SideNav` 그룹 토글 | `aria-label`「{그룹} 메뉴 그룹, {N}개 항목」 | WCAG 2.4.6·그룹 크기 SR 안내 |
| `.ds-sidenav__toggle--active` | 좌측 3px primary accent border | 154차 비주얼·활성 그룹 식별 |

### 56-3. coder 전달 메모

- **별지 제22호 API** — `branchAddress`·`branchRegionPath`·`branchPhone`·`direction`(PICKUP/DROPOFF) 필드명·`transportServiceLogFieldLabels()` 라벨 분기는 coder 커밋 유지.
- **입력 폼 vs 인쇄 표** — compliance는 입력·표 모두 `StatusBadge`+`TRANSPORT_TIME_COMPLIANCE_STATUS` 단일 원천.
- **SideNav** — `navConfig.js` 그룹 id ↔ `SIDE_NAV_GROUP_ICONS` key 일치 필수(`clientOps`·`staffOps`·`transport`·`attendance`·`records`·`billing`).

### 56-4. 검증

- `TransportServiceLogPanel.test.jsx` — compliance Badge·tel `aria-label` 갱신.
- `SideNav.test.jsx` — brand block·group icon·항목 수 `aria-label` +1.
- `npm test`·build PASS.

---

## 57. G-7-1 명세 인쇄·G21 Visits 네비·일괄확정 분할·RFID no-diff + 기록 페이지 sr-only 정합 (133차) [UXD]

<!-- doc:owner=UXD doc:audience=PLN,COD,TSR updated=2026-06-18 -->

> **133차 UXD (2026-06-18)** — §56(132차) 이후 coder 신규 커밋(`50d330d`·`f5639df`·`f9ed97d`·`3a27303`·`f232285`·`570912e`) 미점검 갭 해소.

### 57-1. 대상 화면·컴포넌트

| 컴포넌트 | 위치 | 비고 |
|----------|------|------|
| `BillingStatementPrintPanel` | `components/ui/` | G-7-1 주소라벨·명세서·영수증·청구리스트 인쇄 (`50d330d`) |
| `VisitsContextNav` | `components/visits/` | 계획·청구·분할 비교 cross-link (`3a27303`) |
| `VisitBatchConfirmPanel` | `components/visits/` | PLAN/BILLING per-kind readiness StatCard (`f9ed97d`) |
| `VisitRfidDiffComparePanel` | `components/visits/` | no-diff success Alert·diff code normalize (`f232285`·`570912e`) |
| L02/L03 기록 페이지 11종 | `pages/` | 표 작업 열 sr-only 헤더 |

### 57-2. 접근성·정합 재점검 결과

| 파일 | 조치 | 근거 |
|------|------|------|
| `BillingStatementPrintPanel` 영수증 가드 | `id="billing-statement-print-receipt-unavailable"` `Alert` + disabled 버튼 `aria-describedby` | WCAG 1.3.1 — `disabled` 버튼 `title` 비노출(101차 패턴) |
| `BillingStatementPrintPanel` 인쇄 로딩 | 개별 인쇄 버튼 `aria-busy={loadingClients}` | WCAG 4.1.3 |
| `BillingStatementPrintPanel` 인쇄 표 합계 행 | 본인부담금·수납 금액 `th`에 `ds-sr-only` 강조 접두 | WCAG 1.4.1 — `GuardianBillingDetailModal` 정합 |
| `.ds-billing-claim-print*` | `font-weight`·`font-size` 토큰화 + `forced-colors` 경계선 | FE-16·§1 단일 원천 |
| `.ds-visit-batch-confirm__kind-stats .ds-stat` | `forced-colors` `ButtonText` 경계선 | WCAG 1.4.11 |
| 기록 페이지 11종 표 작업 열 | `ds-visually-hidden`(미정의) → `ds-sr-only` | FE-16·§53 패턴 회귀 해소 |
| `VisitsContextNav`·`VisitBatchConfirmPanel`·`VisitRfidDiffComparePanel` | coder 구현(landmark·`aria-current`·`role=group`·Field error·no-diff Alert) 확인 — 추가 변경 불요 | — |

### 57-3. coder 전달 메모

- **G-7-1 인쇄** — `BILLING_CLAIM_PRINT_BODY_CLASS`=`ds-billing-claim-printing`·`buildClaimPrintRows`·`canPrintBillingReceipt` 로직 유지. 영수증은 `PAID` 상태에서만 활성.
- **VisitsContextNav** — `visitScheduleNavLinks()`·URL `kind`/`split` query sync는 `VisitsPage` `updateScheduleView`와 단일 원천 유지.
- **일괄확정** — BE `draftPlanCount`·`readyBilling` 등 per-kind 필드명 변경 시 `buildKindReadinessStats`만 동기화.
- **RFID compare** — `normalizeVisitRfidDiffCode` 신규 variant는 `config/visits.js` `VISIT_RFID_DIFF_CODES`에 등록. no-diff 시 success Alert + 표 「일치」 텍스트 병행 유지.

### 57-4. 검증

- `BillingStatementPrintPanel.test.jsx` — receipt `aria-describedby`·가드 배너 id +1.
- `npm test`·build PASS.

---

## 58. G21 standalone NHIS comparison·G41 filter-year + 공통 CSS 승격 (134차) [UXD]

<!-- doc:owner=UXD doc:audience=PLN,COD,TSR updated=2026-06-19 -->

> **134차 UXD (2026-06-19)** — §57(133차) 이후 coder 신규 커밋(`797c529`·`ad18606`·`68a4e35`·`f26e075`·`28e5525`) 미점검 갭 해소.

### 58-1. 대상 화면·컴포넌트

| 컴포넌트 | 위치 | 비고 |
|----------|------|------|
| `VisitNhisComparisonPanel` | `components/visits/` | VisitsPage 월간 사전 비교 standalone (`797c529`) |
| `VisitNhisComparisonDetail` | `components/visits/` | per-client drill-down·batch confirm embed (`ad18606`) |
| `StaffTrainingLogPage` | `pages/` | G41 filter-year validation UI (`f26e075`·`28e5525`) |
| `.ds-form-actions--between`·`.ds-subheading` | `components.css` | FE-16 미정의 클래스 승격 |

### 58-2. 접근성·정합 재점검 결과

| 파일 | 조치 | 근거 |
|------|------|------|
| `VisitNhisComparisonPanel` 이중 Spinner | 초기 로드(`!data`)만 섹션 Spinner·새로고침은 버튼 `aria-busy`만 | WCAG 4.1.3 — 동일 라벨 SR 중복 방지 |
| `VisitNhisComparisonPanel` 상세 토글 | 불일치 Alert `id` + expand `aria-describedby` | WCAG 1.3.1 — 101차 quiet-hours 패턴 |
| `VisitNhisComparisonDetail` | 가시 `h4.ds-subheading` + `aria-labelledby` on `role=region` | WCAG 1.3.1·2.4.6 |
| `.ds-visit-nhis-comparison-*` | panel border·StatCard·warning row `forced-colors` | WCAG 1.4.11 |
| `.ds-subheading` | `font-size`·`font-weight` 토큰화 — `VisitBatchConfirmPanel` h4 등 기존 소비자 정합 | FE-16 |
| `StaffTrainingLogPage` filter year | `Field help` 유효 범위·준수 현황 숨김 안내 | WCAG 3.3.2·1.3.1 |

### 58-3. coder 전달 메모

- **standalone vs batch embed** — `VisitNhisComparisonPanel`은 `fetchVisitNhisComparisonApi` 직접 호출·`VisitNhisComparisonDetail`에 `data` prop으로 재사용(중복 fetch 방지). batch confirm 모달은 `expanded`만 true·`data` 미전달 시 자체 fetch.
- **Alert id** — `visit-nhis-comparison-gap-alert`는 panel standalone 전용. batch confirm 모달 NHIS 섹션 id는 기존 `visit-batch-confirm-nhis-comparison` 유지.
- **G41 filter year** — `parseStaffTrainingReferenceYear`·`staffTrainingReferenceYearFieldError` 단일 원천 유지. invalid year 시 compliance Card 미노출·API `referenceYear` omit은 coder 로직 불변.

### 58-4. 검증

- `VisitNhisComparisonPanel.test.jsx` — expand `aria-describedby` +1.
- `VisitNhisComparisonDetail.test.jsx` — h4 heading level 4 +1.
- `npm test`·build PASS.

---

## 59. G41 filter-year help·error 병행 + G21 RFID no-diff SR + G-7-1 print CSS (135차) [UXD]

<!-- doc:owner=UXD doc:audience=PLN,COD,TSR updated=2026-06-19 -->

> **135차 UXD (2026-06-19)** — §58(134차) 이후 134차 `Field help` 조건부 제거·RFID no-diff 이중 Alert·`.ds-billing-statement-print` 미정의 잔여 갭 해소.

### 59-1. 대상 화면·컴포넌트

| 컴포넌트 | 위치 | 비고 |
|----------|------|------|
| `StaffTrainingLogPage` | `pages/` | G41 filter-year invalid 시 compliance 숨김 안내 |
| `VisitRfidDiffComparePanel` | `components/visits/` | no-diff success Alert 단일화 |
| `BillingStatementPrintPanel` | `components/ui/` | `.ds-billing-statement-print` CSS |
| `.ds-billing-statement-print` | `components.css` | FE-16 베이스 클래스 승격 |

### 59-2. 접근성·정합 재점검 결과

| 파일 | 조치 | 근거 |
|------|------|------|
| `StaffTrainingLogPage` filter year | `{...controlProps}` spread로 help·error `aria-describedby` 전달 + invalid year에서도 help 유지 | WCAG 3.3.2·1.3.1 — 134차 render-prop 누락 회귀 해소 |
| `VisitRfidDiffComparePanel` no-diff | info(0건)+success 이중 `role=status` → 단일 success Alert(`visit-rfid-diff-no-diff-alert`) | WCAG 4.1.3 — 중복 live region 방지 |
| `.ds-billing-statement-print` | border-top·padding·`forced-colors` ButtonText | FE-16 — 발송 패널과 인쇄 패널 시각·고대비 구분 |

### 59-3. coder 전달 메모

- **G41 filter year** — `staffTrainingReferenceYearFieldError`·compliance Card 조건부 렌더 로직 불변. help 문구 변경 시 Field `help` prop만 수정.
- **RFID no-diff** — diff 있을 때만 info Alert(건수 포함). no-diff는 success Alert 단일 원천.
- **G-7-1 print** — `.ds-billing-statement-print`는 `BillingDetailPage` 발송 패널 하단 구분선용. 인쇄 zone(`.ds-billing-claim-print-zone`)과 분리 유지.

### 59-4. 검증

- `StaffTrainingLogPage.test.jsx` — invalid filter year help `aria-describedby` +1.
- `VisitRfidDiffComparePanel.test.jsx` — no-diff alert id·0건 info 부재 +1.
- `npm test`·build PASS.

---

## §60. L03 간호기록 5종 행 수정 버튼 `Button` 컴포넌트 정합 (136차)

<!-- doc:owner=UXD doc:audience=PLN,COD,TSR updated=2026-06-19 -->

> **136차 UXD (2026-06-19)** — §59(135차) 이후 전수 점검에서 발견한 **미정의 `ds-table__action-btn` 잔여 5종** 해소. §35(110차)이 `IntensiveExcretionObservationPage`에서 확립한 「raw `ds-table__action-btn` → `Button variant=tertiary size=sm`」 패턴이 동시기 신설된 L03 간호기록 페이지 5종에는 적용되지 않아 회귀로 남아 있었다.

### 60-1. 대상 화면·컴포넌트

| 컴포넌트 | 위치 | 비고 |
|----------|------|------|
| `NursingServiceRecordPage` | `pages/` | L03 간호급여 제공기록 행 수정 |
| `NursingEmergencyRecordPage` | `pages/` | L03_M04 응급상황 기록 행 수정 |
| `NursingExcretionTubeRecordPage` | `pages/` | 유치도뇨관 관리 기록 행 수정 |
| `NursingOralCareCheckPage` | `pages/` | L03_M13 구강상태 점검 행 수정 |
| `NursingWeightRecordPage` | `pages/` | 체중 기록 행 수정 |

### 60-2. 접근성·정합 재점검 결과

| 문제 | 조치 | 근거 |
|------|------|------|
| 행 수정 버튼이 raw `<button className="ds-table__action-btn">` — 해당 클래스는 `components.css`에 **미정의**(전수 grep 결과 위 5개 파일에서만 사용) | `Button variant="tertiary" size="sm"`로 교체(§35 패턴 정합) | FE-16 단일 토큰 원천 — 미정의 클래스라 포커스 링·`forced-colors` outline·hover 토큰 미적용, 브라우저 기본 스타일로 렌더 |
| 동일 액션이 다른 행과 컴포넌트 일관성 없이 raw `<button>` | 디자인 시스템 `ds-btn` 단일 컴포넌트 사용 | WCAG 4.1.2 — 동일 역할 컨트롤의 일관된 시맨틱·시각 |

> `aria-label`(이용자명·일자·기록 유형 포함)·`onClick`·`type="button"`은 기존과 동일하게 유지. 데이터·API·동작 불변, 순수 접근성·정합 리팩터.

### 60-3. coder 전달 메모

- 신설 기록 페이지에서 행 액션 버튼은 **반드시 `Button` 컴포넌트**(`variant="tertiary" size="sm"`)를 사용한다 — `ds-table__action-btn` 등 미정의 클래스로 raw `<button>`을 만들지 않는다.
- 표 행 수정/삭제 등 행 단위 액션 `aria-label`에는 대상 이용자명·일자를 포함해 다중 행에서 동일 라벨 중복(WCAG 2.4.6)을 방지한다(기존 라벨 유지).

### 60-4. 검증

- `NursingServiceRecordPage.test.jsx`·`NursingEmergencyRecordPage.test.jsx`·`NursingExcretionTubeRecordPage.test.jsx`·`NursingOralCareCheckPage.test.jsx`·`NursingWeightRecordPage.test.jsx` — 수정 버튼 `ds-btn` 클래스 단언 +5(기존 edit-mode 테스트 보강).
- 5개 파일 32 tests PASS(locked `npm test`).

---

## §61. G21 split-view NHIS·G32 FAQ21797·G2 법정서식·케어포 3-1 nav + 미정의 CSS 승격 (137차)

<!-- doc:owner=UXD doc:audience=PLN,COD,TSR updated=2026-06-19 -->

> **137차 UXD (2026-06-19)** — §60(136차) 이후 coder 신규 커밋(`9b80505`·`1d5747d`·`b272a7b`·`d1149a5`·`b881883`) 미점검 a11y·FE-16 갭 해소.

### 61-1. 대상 화면·컴포넌트

| 컴포넌트 | 위치 | 비고 |
|----------|------|------|
| `VisitNhisComparisonPanel` | `components/visits/` | G21 split-view PLAN/BILLING 2패널 (`9b80505`) |
| `VisitsPage` | `pages/` | 분할 비교 래퍼 |
| `CareProvisionSegmentNav` | `components/ui/` | 케어포 3-1 급여제공 세분화 nav (`1d5747d`) |
| `CaseManagementPage` | `pages/` | G32 FAQ21797 참석자별 의견 (`b272a7b`) |
| `GuardianDocumentNotifyPanel` | `components/ui/` | G2 가정통신문·급여제공기록지 (`d1149a5`) |
| `CareServiceWeeklyRecordPage` | `pages/` | G39 FAQ21817 7일 SLA Alert (`b881883`) — 점검 확인(변경 불요) |
| `.ds-form-grid__full` | `components.css` | FE-16 미정의 클래스 승격 |

### 61-2. 접근성·정합 재점검 결과

| 파일 | 조치 | 근거 |
|------|------|------|
| `VisitNhisComparisonPanel` h3 | `{kindLabel} 공단 명세 사전 비교`(예: 「계획 일정 공단 명세 사전 비교」) — split-view 2패널 동시 노출 시 제목 구분 | WCAG 2.4.6 — 동일 h3 중복 |
| `VisitsPage` 분할 비교 래퍼 | `role="group" aria-label="계획·청구 공단 명세 분할 비교"` | WCAG 1.3.1 — generic div `aria-label` 단독 불충분 |
| `CaseManagementPage` | `ds-field__hint`(미정의)→`ds-field__help`·폼 `aria-describedby=cm-form-hint`·fieldset `aria-describedby`·행 수정 `aria-label`에 이용자명 | FE-16·WCAG 3.3.2·2.4.6 |
| `GuardianDocumentNotifyPanel` | 서식 설명 `#guardian-document-notify-description`·submit `aria-describedby`·form `aria-label` | WCAG 1.3.1 — 서식 유형별 설명 SR 전달 |
| `DurationBandSelect` | `ds-field__hint`→`ds-field__help` | FE-16 단일 원천 |
| `.ds-form-grid__full` | `grid-column: 1 / -1` 정의 | FE-16 — `CaseManagementPage`·`ProvisionResultEvaluationPage` 소비 |
| `CareProvisionSegmentNav` | `nav`·`aria-current`·`ds-context-nav--sub` — 119차 패턴 확인(변경 불요) | — |
| `CareServiceWeeklyRecordPage` SLA Alert | `aria-labelledby`+`ul/li` — 113차 패턴 확인(변경 불요) | — |

### 61-3. coder 전달 메모

- **G21 split-view NHIS** — PLAN/BILLING 2패널 동시 마운트 시 각 패널 h3에 `{SCHEDULE_KIND_LABELS[kind]}` 접두 유지. 단일 패널 모드는 기존과 동일.
- **G32 attendee opinions** — fieldset legend「참석자별 의견 (FAQ21797)」+ hint id `cm-attendee-opinions-hint` 패턴 유지. 행 수정 버튼은 `${clientName} 사례관리 회의록 수정` aria-label 필수.
- **G2 guardian documents** — `GUARDIAN_DOCUMENT_NOTIFY_TYPES` 추가 시 description id·submit `aria-describedby` 동기화.
- **케어포 3-1 nav** — `CARE_PROVISION_SEGMENT_LINKS`·`/health` 상단 `CareProvisionSegmentNav` 배치 유지. 신규 segment route 추가 시 nav config·test 동반.

### 61-4. 검증

- `VisitNhisComparisonPanel.test.jsx` — PLAN heading level 3 +1.
- `CaseManagementPage.test.jsx` — edit button context aria-label +1.
- `GuardianDocumentNotifyPanel.test.jsx` — submit `aria-describedby` +1.
- `npm test`·build PASS.

---

## §62. G-CASH-RECEIPT-LOG 발급목록·수납 prompt·대시보드 due-gate 접근성 (138차)

<!-- doc:owner=UXD doc:audience=PLN,COD,TSR updated=2026-06-19 -->

> **138차 UXD (2026-06-19)** — §61(137차) 이후 coder G-CASH-RECEIPT-LOG 4-계층 커밋(`cfc4b04`·`a17f148`·`221458e`·`8aebe55`) 미점검 a11y·FE-16 갭 해소.

### 62-1. 대상 화면·컴포넌트

| 컴포넌트 | 위치 | 비고 |
|----------|------|------|
| `CashReceiptIssuancePage` | `/billing/cash-receipts` | FAQ 21701 발급목록·수급자별 발급정보 (`cfc4b04`) |
| `CashReceiptRegisterModal` | `components/ui/` | NTS 발급 등록 모달 |
| `CashReceiptLegalAlerts` | `components/ui/` | FAQ 21716/21717 법정 안내 |
| `PaymentRecordModal` | `components/ui/` | 현금 수납 후 발급 prompt (`a17f148`) |
| `CASH_RECEIPT_IMMEDIATE_STATUS` | `Badge.jsx` | 즉시발급 준수 MET/DELAYED |
| `.ds-cash-receipt-legal-alerts` · `.ds-cash-receipt-issuance__summary` | `components.css` | gap·StatCard forced-colors |

### 62-2. 접근성·정합 재점검 결과

| 파일 | 조치 | 근거 |
|------|------|------|
| `CashReceiptRegisterModal` | 필수값 검증 → `Field error`+`aria-invalid`·API 실패만 Alert·form `aria-label`·작년분 `id`+submit `aria-describedby` | WCAG 3.3.1·1.3.1 (IncidentRecordForm 패턴) |
| `CashReceiptIssuancePage` | 즉시발급 `StatusBadge`·조회 `aria-busy`·발급일 `<time>`·`Select` 컴포넌트·`ds-grid--stats` | WCAG 1.4.1·4.1.3·FE-16 |
| `PaymentRecordModal` | 현금 FAQ 21716 경고 `#payment-cash-receipt-warning`·submit `aria-describedby` | WCAG 1.3.1 (ClaimGenerationPanel 패턴) |
| `CashReceiptLegalAlerts` | FAQ 21716/21717 Alert `id`·`.ds-cash-receipt-legal-alerts` gap 토큰 | FE-16·cross-link 준비 |

### 62-3. coder 전달 메모

- **발급 등록** — `createCashReceiptIssuanceApi` payload 필드명(`billingClaimId`·`ntsReceiptNo`·`identifierType`·`identifierValue`·`issuedAt`·`amount`) 유지. `priorYearIssuanceEligible` claim 시 modal 경고+submit `aria-describedby` 동기화.
- **즉시발급 열** — backend `immediateIssuanceMet` boolean → `CASH_RECEIPT_IMMEDIATE_STATUS` MET/DELAYED. 색+텍스트 Badge 필수.
- **수납대장 vs 발급목록** — `/billing/reports/receipts`(수납 ledger)와 `/billing/cash-receipts`(NTS 발급 이력) UI·nav 라벨 혼동 금지(`BillingReportsContextNav` 7항목 유지).

### 62-4. 검증

- `CashReceiptRegisterModal.test.jsx` 3 — field `aria-invalid`·prior-year `aria-describedby`·submit payload.
- `CashReceiptIssuancePage.test.jsx` — Badge 「충족」 +1.
- `PaymentRecordModal.test.jsx` — CASH `aria-describedby` +1.
- `npm test`·build PASS.

---

## §63. G26 yearBasis·G-7-1 Excel·현금영수증 pending guard 접근성 (139차)

<!-- doc:owner=UXD doc:audience=PLN,COD,TSR updated=2026-06-20 -->

> **139차 UXD (2026-06-20)** — §62(138차)·UXD-139(`17374f1`) 이후 coder 신규 커밋(`19ed7f3`·`58d6694`·`99b795a`·`a2ef127`) 미점검 a11y·FE-16 갭 해소.

### 63-1. 대상 화면·컴포넌트

| 컴포넌트 | 위치 | 비고 |
|----------|------|------|
| `BillingStatisticsReportPage` | `/billing/reports/statistics` | G26 ① yearBasis 수납/청구년도 토글·NTS CSV (`19ed7f3`) |
| `BillingStatementPrintPanel` | `BillingDetailPage` | G-7-1 Excel export 5종 (`58d6694`) |
| `CashReceiptIssuancePage` | `/billing/cash-receipts` | pending load guard·empty list modal (`99b795a`/`a2ef127`) |
| `MedicalExpenseDeductionPanel` | `ClientDetailPage`·`GuardianPortalPage` | US-L04 조회 busy |
| `.ds-segmented` | `components.css` | TransportPage·G26 공유 segmented toggle |

### 63-2. 접근성·정합 재점검 결과

| 파일 | 조치 | 근거 |
|------|------|------|
| `BillingStatisticsReportPage` | yearBasis `role=tablist`+`aria-labelledby`·CSV `aria-busy`+`aria-label`·StatCard `ds-grid--stats` | WCAG 4.1.3·FE-16 (TransportPage·StaffTrainingLogPage 패턴) |
| `BillingStatementPrintPanel` | Excel 5종 `aria-busy`·`aria-describedby`(영수증 가드)·PDF `aria-label` | WCAG 1.3.1·2.4.6 (§59 인쇄 패널 패턴) |
| `CashReceiptIssuancePage` | `CASH_RECEIPT_PENDING_ERROR_ID`+「발급 등록」`aria-describedby`·수급자 검색 `aria-busy` | WCAG 1.3.1 (ClaimGenerationPanel·FeeScheduleYearGuardBanner 패턴) |
| `MedicalExpenseDeductionPanel` | 조회 `aria-busy={loading}` | WCAG 4.1.3 |
| `.ds-segmented` | `forced-colors` 경계선·선택 탭 outline | WCAG 1.4.11 (FilterChips·Badge 패턴) |

### 63-3. coder 전달 메모

- **G26 yearBasis** — `MEDICAL_EXPENSE_YEAR_BASIS.PAID_YEAR`/`CLAIM_YEAR` API query param 유지. 탭 전환 시 `page=1` 리셋·`fetchMedicalExpenseDeductionReportApi`만 재조회(②③ 월별 통계는 연도만 의존).
- **G-7-1 Excel** — `GET /billing/claims/{id}/statement-export?kind=` (`address-label`·`statement`·`receipt`·`claim-list`·`all`). 미수납 시 receipt/all에서 영수증 제외 — `#billing-statement-print-receipt-unavailable` `aria-describedby` 유지.
- **현금영수증 pending guard** — `fetchPendingCashReceiptIssuancesApi` 실패 시 목록 Alert+등록 버튼 `aria-describedby`. 모달 빈 claims 시 submit `disabled`+`role=status` 안내(UXD-139).
- **BNK-412 identifier 검증** — BE `@35d1560` 서버 검증. FE는 `Field error`+`aria-invalid`로 API 400 메시지 표면화만(coder).

### 63-4. 검증

- `CashReceiptIssuancePage.test.jsx` — pending error `id`+register `aria-describedby` +1.
- `BillingStatementPrintPanel.test.jsx` — PDF `aria-label` 갱신 +1.
- `npm test`·build PASS.

---

## §64. US-R03 FAQ21823 근로재계약 UI·현금영수증 identifier 검증 접근성 (140차)

<!-- doc:owner=UXD doc:audience=PLN,COD,TSR updated=2026-06-20 -->

> **140차 UXD (2026-06-20)** — §63(139차)·UXD-140(`501fedc`) 이후 coder 신규 커밋(`f62402f`·`10585b9`·`f31c346` FAQ21823 renewal panel/summary/dashboard widget·`76a462d` identifier digit validation) 미점검 a11y·FE-16 갭 해소.

### 64-1. 대상 화면·컴포넌트

| 컴포넌트 | 위치 | 비고 |
|----------|------|------|
| `StaffEmploymentContractRenewalPanel` | `StaffDetailPage` lifecycle 탭 | FAQ21823 개별 직원 재계약 안내 (`f62402f`) |
| `StaffEmploymentContractRenewalSummaryPanel` | `StaffPage` | FAQ21823 목록 요약·확인 필요 표 (`10585b9`) |
| `DashboardPage` | `/dashboard` | 「근로재계약 미충족」위젯 (`f31c346`) |
| `CashReceiptRegisterModal` | `CashReceiptIssuancePage` | BNK-412 identifier digit/length FE 검증 (`76a462d`) |

### 64-2. 접근성·정합 재점검 결과

| 파일 | 조치 | 근거 |
|------|------|------|
| `StaffEmploymentContractRenewalPanel` | 기한 초과 Alert `STAFF_EMPLOYMENT_CONTRACT_RENEWAL_OVERDUE_ALERT_ID`·파일함 버튼 `aria-describedby`+`${직원명} 근로계약서 파일함` `aria-label` | WCAG 1.3.1·2.4.6 (ClaimGenerationPanel·StaffPage 패턴) |
| `StaffEmploymentContractRenewalSummaryPanel` | 확인 필요 표 링크 `${이름} 직원 상세` `aria-label` | WCAG 2.4.6 (StaffPage 목록 링크 패턴) |
| `CashReceiptRegisterModal` | 프로필 hint 로드 중 발급 식별자 `aria-busy={profileLoading}` | WCAG 4.1.3 (MedicalExpenseDeductionPanel·CashReceiptIssuancePage 패턴) |
| `DashboardPage` | 위젯 StatCard — 기존 `DashboardWidgetGrid` loading·tone 패턴 준수 | 변경 불요 |

### 64-3. coder 전달 메모

- **FAQ21823 partial** — 갱신 CRUD·급여대장 연동·due-date 알림은 module 11 payroll out-of-scope(USER_STORIES P2 잔여). 현 UI는 read-only guidance+HR 파일함 deep-link.
- **대시보드 위젯** — `countEmploymentContractRenewalGaps(staffMembers)` = overdue+missing 합산. `/staff` 링크로 summary panel 유도.
- **현금영수증 identifier** — FE는 digit normalize+length guard만. BE `@35d1560` 서버 검증 400 → `Field error` 표면화 유지.

### 64-4. 검증

- `StaffEmploymentContractRenewalPanel.test.jsx` — overdue Alert `id`·파일함 `aria-describedby`·직원명 `aria-label` +2.
- `StaffEmploymentContractRenewalSummaryPanel.test.jsx` — 링크 `aria-label` 갱신 +1.
- `CashReceiptRegisterModal.test.jsx` — profile load `aria-busy` +1.
- `npm test`·build PASS.

---

## §65. FAQ21823 갱신 알림·CRUD·checklist CSS 승격 접근성 (141차)

<!-- doc:owner=UXD doc:audience=PLN,COD,TSR updated=2026-06-20 -->

> **141차 UXD (2026-06-20)** — §64(140차)·UXD-141(`965e569`/`debe6dd`) 이후 coder 신규 커밋(`033b319`·`1b6d2b1`) 미점검 a11y·FE-16 갭 해소.

### 65-1. 대상 화면·컴포넌트

| 컴포넌트 | 위치 | 비고 |
|----------|------|------|
| `EmploymentContractRenewalAlertsPanel` | `DashboardPage` | due/overdue/missing 알림 목록 (`033b319`) |
| `StaffEmploymentContractRenewalPanel` | `StaffDetailPage` lifecycle | 재계약 CRUD modal·필수항목/절차 checklist·서식 modal (`033b319`/`1b6d2b1`) |
| `.ds-section-title`·`.ds-subsection-title` | `components.css` | StaffPage·Dashboard alerts·Card 내부 h3 |
| `.ds-checklist*` | `components.css` | `StaffHrFilePanel`·FAQ21823 ordered checklist |
| `.ds-staff-employment-contract__template` | `components.css` | 근로계약서 `<pre>` 서식 미리보기 |

### 65-2. 접근성·정합 재점검 결과

| 파일 | 조치 | 근거 |
|------|------|------|
| `EmploymentContractRenewalAlertsPanel` | due-date `<time dateTime>`·알림 `ul` `role=group aria-label` | WCAG 1.3.1 (StaffEmploymentContractRenewalPanel·Billing 패턴) |
| `StaffEmploymentContractRenewalPanel` | 재계약 modal 저장 `aria-busy`·form `aria-label` | WCAG 4.1.3 (IncidentRecordForm·Modal 패턴) |
| `.ds-checklist*` | FE-16 미정의 클래스 승격·`forced-colors` item 경계선 | StaffHrFilePanel·FAQ21823 checklist 시각·SR 정합 |
| `.ds-staff-employment-contract__template` | mono·scroll·`forced-colors` 경계선 | `ds-transport-compliance__template` 패턴 |

### 65-3. coder 전달 메모

- **FAQ21823 P2** — `updateUserApi` 재계약 서명일 CRUD·`computeEmploymentContractRenewalDueAlerts` 대시보드 알림 **HEAD PRESENT**. 급여대장 연동·module 11 payroll은 USER_STORIES P2 잔여(out-of-scope).
- **대시보드 이중 surface** — StatCard 위젯(`employmentContractRenewalGapCount`) + `EmploymentContractRenewalAlertsPanel`(상세 알림). 위젯은 `/staff` 링크, 알림은 lifecycle deep-link.
- **`.ds-checklist`** — HR 입사서류 7종(`StaffHrFilePanel`)과 FAQ21823 필수항목/절차가 **동일 유틸** 공유. ordered variant는 `ol.ds-checklist--ordered`.

### 65-4. 검증

- `EmploymentContractRenewalAlertsPanel.test.jsx` — `time datetime`·`role=group` +1.
- `StaffEmploymentContractRenewalPanel.test.jsx` — 저장 `aria-busy` +1.
- `npm test`·build PASS.

---

## §66. v1.3-A 이동서비스 배차 도구 접근성 재점검 (142차)

<!-- doc:owner=UXD doc:audience=PLN,COD,TSR updated=2026-06-20 -->

> **142차 UXD (2026-06-20)** — §65(141차)·UXD-142(`bd6e1c2`) 이후 coder 신규 커밋(`4681b5a` roster tools·ETA guardrails·`863b135` run spies·`acc5933` route preview cache·compliance labels·`ba74bb5` Kakao map WIP·QA-B167/B170) 미점검 a11y·FE-16 갭 해소.

### 66-1. 대상 화면·컴포넌트

| 컴포넌트 | 위치 | 비고 |
|----------|------|------|
| `TransportKakaoApiStatusPanel` | `SettingsPage`·`OrganizationSettingsPage` | Kakao REST API 상태·사용량(`acc5933`) |
| `TransportSuggestPanel` | `TransportPage` | 자동 배차 제안 DRAFT 루트 표 |
| `TransportAddRosterModal` | `TransportRouteSplitView` | 명단에서 인원 추가(`4681b5a`) |
| `TransportConfirmWarningModal` | `TransportRunDetailPage` | 희망 탑승 시각 위반 경고(`4681b5a`) |
| `TransportLoadPreviousRunModal` | `TransportRunNewPage` | 이전 배차 불러오기(`4681b5a`) |
| `KakaoTransportMapView`·`KakaoTransportMap` | 배차 경로 미리보기 | 마커·경로·요약(`ba74bb5`) |

### 66-2. 접근성·정합 재점검 결과

| 파일 | 조치 | 근거 |
|------|------|------|
| `TransportKakaoApiStatusPanel` | Kakao Developers 콘솔 외부 링크(`target=_blank`)에 `<span class="ds-sr-only"> (새 탭)</span>` 추가 — 새 창 열림 사전 안내 | WCAG 3.2.5·G201 (`IntegratedHomeProviderDiscoveryPanel` 패턴) |
| `TransportSuggestPanel` | 표 행마다 동일한 「DRAFT 검토」링크 → `${차량번호} DRAFT 검토` `aria-label` 부여 (목적 구분) | WCAG 2.4.4 (StaffPage·UXD-140 목록 링크 패턴) |
| `TransportConfirmWarningModal` | Alert `tone=warning`/`info` 기본 live-region·`aria-busy`·`<ul>` 목록 — 변경 불요 | Alert §6 패턴 준수 |
| `TransportAddRosterModal`·`TransportLoadPreviousRunModal` | `Field htmlFor`·`PageLoading label`·Alert `tone=danger`(role=alert) `actionError`·submit `aria-busy` — 변경 불요 | Field render-prop·Modal 패턴 준수 |
| `KakaoTransportMapView` | marker `<button aria-label>`·`role=application aria-label`·요약 `role=status aria-live` — 변경 불요 | WCAG 1.1.1·4.1.3 |

### 66-3. coder 전달 메모

- **외부 링크 새 탭 안내** — 신규 외부 `target=_blank` 링크는 `ds-sr-only`「(새 탭)」 또는 `aria-label` 후행으로 통일한다(IntegratedHomeProviderDiscoveryPanel·본 패널 동일). raw `window.open` 금지.
- **반복 행 링크** — 같은 텍스트(「DRAFT 검토」·「상세」 등)가 표/목록 여러 행에 반복되면 행 식별자(차량번호·이름)를 `aria-label` 접두로 부여한다. SuggestPanel·StaffPage·StaffEmploymentContractRenewalSummaryPanel 동일.
- **지도 a11y** — `KakaoTransportMapView`는 marker `aria-label`·`role=application`·`role=status` 요약을 이미 갖춘다. 핀 텍스트(순번/「센」)는 `aria-hidden`, 의미는 `aria-label`로 전달하므로 색·번호만으로 의미를 싣지 말 것.
- **v1.3-A 잔여** — roster CRUD·ETA guardrail 토스트는 현재 Alert 인라인으로 충분. 토스트 도입 시 `--z-toast`·`role=status` 토큰 사용.

### 66-4. 검증

- `TransportSuggestPanel.test.jsx` — 「DRAFT 검토」링크 name `12가3456 DRAFT 검토` 갱신.
- `TransportKakaoApiStatusPanel.test.jsx` — 콘솔 링크 name `Kakao Developers 콘솔 (새 탭)`·`target=_blank` +1.
- `npm test`(2 files·5 tests PASS)·lint PASS.

---

## §67. G14 급여제공계획서·직원 계정 요청 UI 접근성 재점검 (144차)

<!-- doc:owner=UXD doc:audience=PLN,COD,TSR updated=2026-06-20 -->

> **144차 UXD (2026-06-20)** — 143차(§66)·UXD-143(`4e7d01d`) 이후 coder 신규 커밋 6건 미점검 갭 해소.

### 67-1. 대상 화면·컴포넌트

| 컴포넌트 | 위치 | 커밋 |
|----------|------|------|
| `StaffPage` 계정 생성 요청 표 | `pages/StaffPage.jsx` | `22718d0` |
| `PlatformOrgDetailModal` 관리자 발급 폼 | `components/ui/PlatformOrgDetailModal.jsx` | `380be3c` |
| `RegionSelector` 시·군·구/읍·면·동 검색 | `components/branches/RegionSelector.jsx` | `8ac0d01` |
| `ClientCarePlanForm` G14 10항목 폼 | `components/clients/ClientCarePlanForm.jsx` | `ce422e3` |
| `tokens.css` 타이포 토큰 조정 | `styles/tokens.css` | `d723d5a` |

### 67-2. 접근성·정합 재점검 결과

| 파일 | 결함 | 조치 | 근거 |
|------|------|------|------|
| `StaffPage` 계정 요청 상태 열 | `REQUEST_STATUS_LABELS` 평문 → 색만 의존 가능성 | **`StatusBadge`+`ACCOUNT_REQUEST_STATUS`** (색+텍스트 병행) | WCAG 1.4.1 |
| `StaffPage` 요청일 열 | `new Date().toLocaleString()` 평문 | **`<time dateTime>`** 래핑 | WCAG 1.3.1 (88차 패턴) |
| `ClientCarePlanForm` CSS | `.ds-care-plan-form`·`__heading`·`__year-row` 미정의(FE-16) | `components.css` **승격** | FE-16·§1 단일 원천 |
| `ds-form-grid--2` | `ds-form-grid` 2열 고정 변형 미정의(FE-16) | `components.css` **신규** | FE-16 |
| `PlatformOrgDetailModal` 발급 폼 | 이름·이메일·비밀번호 3 `Field` + `aria-busy` 제출 — 변경 불요 | Field render-prop·Modal 패턴 준수 | ✅ |
| `RegionSelector` 검색 입력 | `SearchInput hideLabel` + `label` prop — 시각적 레이블 숨김·SR 전달 — 변경 불요 | SearchInput 컴포넌트 표준 패턴 준수 | ✅ |
| `ClientCarePlanForm` 폼 구조 | `form aria-labelledby` h3·`Field` render-prop·`DateInput`·`aria-busy` — 변경 불요 | 표준 패턴 준수 | ✅ |
| `tokens.css` font-size 상향 | xs 0.75→0.8125rem 등 소폭 상향 — 접근성 개선(큰 글자) | §3 표 실측값 갱신 | WCAG 1.4.4 |

### 67-3. 신규 상수

| 상수 | 위치 | 값 |
|------|------|-----|
| `ACCOUNT_REQUEST_STATUS` | `components/ui/Badge.jsx` + barrel `index.js` | `PENDING`(neutral·승인 대기)·`APPROVED`(success·승인됨)·`REJECTED`(danger·반려됨) |

### 67-4. CSS 신규 클래스

| 클래스 | 스타일 | 용도 |
|--------|--------|------|
| `.ds-form-grid--2` | `grid-template-columns: repeat(2, 1fr)` | 2열 고정 폼 그리드 변형 |
| `.ds-care-plan-form` | `max-width: 720px` | G14 계획서 폼 래퍼 |
| `.ds-care-plan-form__heading` | `font-size-lg`·`font-weight-semibold` | 폼 내부 h3 제목 |
| `.ds-care-plan-form__year-row` | `align-items: flex-end`·`gap: space-4` | 연도 선택 + 저장 이력 행 |

### 67-5. coder 전달 메모

- **계정 요청 상태**: `ACCOUNT_REQUEST_STATUS` Badge 사용 — `StaffPage` 이미 적용. 추후 `PlatformPage` 관리자 검토 화면에서도 같은 상수를 재사용할 것.
- **반복 날짜**: 목록 표의 날짜 셀은 반드시 `<time dateTime={ISO8601}>` 래핑한다(88·89차 공통 패턴).
- **2열 폼**: `ds-form-grid ds-form-grid--2` 조합 사용. `ds-form-grid--2` 단독 사용 불가(`ds-form-grid`가 `display:grid` 선언).

### 67-6. 검증

- `StaffPage.test.jsx` — `ACCOUNT_REQUEST_STATUS` Badge 단언·`<time dateTime>` 존재 — 기존 1866/369 전체 PASS.
- `npm test` 1866/369 PASS · build PASS.

---

## §68. G-BILLING-PRIOR-DEPOSIT-GUARD·US-H01 HQ 듀얼 대시보드 접근성 재점검 (145차)

<!-- doc:owner=UXD doc:audience=PLN,COD,TSR updated=2026-06-20 -->

> **145차 UXD (2026-06-20)** — 144차(§67)·UXD-144(`08a8b9f`) 이후 coder 신규 커밋 3건 미점검 갭 해소.

### 68-1. 대상 화면·컴포넌트

| 컴포넌트 | 위치 | 커밋 | 스토리 |
|----------|------|------|--------|
| `claimGenerationGuard` StatCard 위젯 | `pages/DashboardPage.jsx` | `0d233b9` | G-BILLING-PRIOR-DEPOSIT-GUARD |
| `DashboardContextNav` | `components/dashboard/DashboardContextNav.jsx` | `c1ebaaf` | US-H01 |
| `HqBranchSummaryTable` | `components/dashboard/HqBranchSummaryTable.jsx` | `c1ebaaf` | US-H01 |
| `useBranchDrilldown` | `hooks/useBranchDrilldown.js` | `c1ebaaf` | US-H01 |
| `HealthAlertList` HQ 드릴다운 | `components/ui/HealthAlertList.jsx` | `c1ebaaf` | US-H02 |
| `BranchCompareChart` 클릭 드릴다운 | `components/ui/BranchCompareChart.jsx` | `c1ebaaf` | US-H02 |

### 68-2. 접근성·정합 재점검 결과

| 파일 | 결함 | 조치 | 근거 |
|------|------|------|------|
| `HqBranchSummaryTable` 조치 버튼 | `disabled={drilling}`만 있고 진행 상태 SR 미전달 | **`aria-busy={drilling}`** 3버튼 | WCAG 4.1.3 |
| `HealthAlertList` 지점 보기 | `branchActionDisabled` 시 SR 진행 상태 미전달 | **`aria-busy={branchActionDisabled}`** | WCAG 4.1.3 |
| `.ds-health-alert-list__action` | `HealthAlertList`가 참조하나 CSS 미정의(FE-16) | `components.css` **승격** + `forced-colors` 항목 경계선 | FE-16·§1 |
| `BranchCompareChart` 클릭 드릴다운 | 막대 클릭만 가능·키보드 대안 없음 | `ChartContainer` **description**에 표 「지점 보기」 대안 안내 | WCAG 2.1.1 |
| `DashboardContextNav` | `nav`·`aria-label`·`NavLink` `aria-current` | 변경 불요 — `ds-context-nav` 표준 | ✅ |
| `CLAIM_GENERATION_GUARD_WIDGET_LABEL` StatCard | `tone=danger`·링크 `/billing/payments` | 변경 불요 — `DashboardWidgetGrid` 표준 | ✅ |

### 68-3. CSS 신규·보강 클래스

| 클래스 | 스타일 | 용도 |
|--------|--------|------|
| `.ds-health-alert-list__action` | `margin-left: auto`·`flex-shrink: 0` | HQ 건강 알림 행 지점 드릴다운 버튼 정렬 |
| `.ds-health-alert-list__item` (`forced-colors`) | `border: 1px solid ButtonText` | 고대비 모드 목록 항목 식별 |

### 68-4. coder 전달 메모

- **HQ 드릴다운**: `useBranchDrilldown` → `switchActiveBranch` + `navigate`. 새 지점 액션 UI는 반드시 **`${지점명} …` `aria-label`** + 진행 중 **`aria-busy`**.
- **청구 선행입금 가드 위젯**: `CLAIM_GENERATION_GUARD_WIDGET_LABEL`·`analyzeClaimGenerationGuard` 단일 원천 — 대시보드·`ClaimGenerationPanel` 라벨 불일치 금지.
- **차트 드릴다운**: Recharts 막대는 포인터 전용 — 키보드·SR 대안은 **`HqBranchSummaryTable`** 조치 열 또는 별도 `Button` 목록으로 제공.
- **잔여 P2 FE wire**(coder): ~~G-BANK-EXCEL-8·G-STAFF-NHIS-EXCEL-IMPORT~~ → **146차 UXD wire+a11y 완료** (`a18b30e`·`4315ee2`·§69).

### 68-5. 검증

- `HqBranchSummaryTable.test.jsx` — `drilling` 시 `aria-busy`·`disabled` 단언 +1.
- `HealthAlertList.test.jsx` — `branchActionDisabled` 시 `aria-busy` 단언 +1.
- `npm test` · build PASS.

---

## §69. G-BANK-EXCEL-8·G-STAFF-NHIS-EXCEL-IMPORT preview·행 선택 접근성 재점검 (146차)

<!-- doc:owner=UXD doc:audience=PLN,COD,TSR updated=2026-06-20 -->

> **146차 UXD (2026-06-20)** — 145차(§68)·UXD-145(`a2f599c`) 이후 coder 신규 커밋 2건 미점검 갭 해소.

### 69-1. 대상 화면·컴포넌트

| 컴포넌트 | 위치 | 커밋 | 스토리 |
|----------|------|------|--------|
| `BankDepositImportPanel` preview·행 선택 | `components/ui/BankDepositImportPanel.jsx` | `a18b30e` | G-BANK-EXCEL-8 · US-L01 |
| `StaffNhisCaregiverImportPanel` | `components/staff/StaffNhisCaregiverImportPanel.jsx` | `4315ee2` | G-STAFF-NHIS-EXCEL-IMPORT |
| `StaffPage` 연동 | `pages/StaffPage.jsx` | `4315ee2` | G-STAFF-NHIS-EXCEL-IMPORT |

### 69-2. 접근성·정합 재점검 결과

| 파일 | 결함 | 조치 | 근거 |
|------|------|------|------|
| 두 import 패널 미리보기 폼 | `form` 접근성 이름 없음 | **`aria-label`**(은행/요양보호사 구분) | WCAG 1.3.1 |
| 미리보기 결과 영역 | 그룹 시맨틱 없음 | **`role=group` + `aria-label`** | WCAG 1.3.1 |
| 미리보기 요약 `<p>` | 비동기 로드 후 SR 무음 | **`role=status` + `aria-live=polite`** | WCAG 4.1.3 |
| 행 선택 `Checkbox` | 「N행 선택」만 — 다중 행 SR 식별 불가 | **`${예금주명\|성명} N행 선택`** | WCAG 2.4.6 |
| 입금일·생년월일 | 날짜 의미론 없음 | **`<time dateTime>`** | WCAG 1.3.1 |
| `.ds-bank-deposit-formats` | `details` 래퍼 CSS 미정의(FE-16) | **`components.css` 승격** + `forced-colors` | FE-16·§1 |
| `Badge`+`ROW_STATUS_MAP` | 색+텍스트 라벨 병행 | 변경 불요 | §1-2 ✅ |
| `FileUpload`·`aria-busy`·성공 `Alert role=status` | 기존 import 패턴 준수 | 변경 불요 | ✅ |

### 69-3. CSS 신규·보강 클래스

| 클래스 | 스타일 | 용도 |
|--------|--------|------|
| `.ds-bank-deposit-formats` | muted 배경·border·`summary` semibold | 은행 8종 형식 `<details>` |
| `.ds-import-preview` | 상단 구분선·`padding-top` | Excel import 미리보기 공통 래퍼 |
| `.ds-import-preview__summary` | 하단 여백 | 요약 status 문구 |

### 69-4. coder 전달 메모

- **Preview→Import 2단계**: `preview*Api` → APPLIED 행 기본 선택 → `import*Api({ rowNumbers })`. 새 import UI는 **동일 2단계·행 Checkbox·전체 선택** 패턴 재사용.
- **행 Checkbox `aria-label`**: 반드시 **도메인 식별자(예금주명·성명·인정번호 등) + 행 번호** 포함 — 「N행 선택」 단독 금지.
- **은행 8종 샘플**: `downloadBankDepositSampleXlsx(format)` — 버튼 `${은행명} … 샘플 엑셀 다운로드` `aria-label` 유지.
- **Staff import 성공**: `onImported(result)` → `StaffPage` 계정 요청 목록 재조회 — API 필드 `appliedCount`·`pendingCount` StatCard/Badge 연동 시 §67 `ACCOUNT_REQUEST_STATUS` 재사용.

### 69-5. 검증

- `BankDepositImportPanel.test.jsx` — contextual checkbox·`<time dateTime>` +1.
- `StaffNhisCaregiverImportPanel.test.jsx` — contextual checkbox·`<time dateTime>` +1.
- `npm test` · build PASS.

---

## §70. G-STAFF-LEAVE-STATUS 휴직 상태 UI 접근성 재점검 (147차)

<!-- doc:owner=UXD doc:audience=PLN,COD,TSR updated=2026-06-21 -->

> **147차 UXD (2026-06-21)** — 146차(§69)·UXD-146(`a7d9a2f`) 이후 coder 신규 커밋 1건(live-e2e 수정 5건 제외) 미점검 a11y 갭 해소.

### 70-1. 대상 화면·컴포넌트

| 컴포넌트 | 위치 | 커밋 | 스토리 |
|----------|------|------|--------|
| `StaffLifecycleSummaryPanel` (신규) | `components/staff/StaffLifecycleSummaryPanel.jsx` | `2581347` | G-STAFF-LEAVE-STATUS · FAQ 21720 |
| `StaffLifecyclePanel` ON_LEAVE 분기 | `components/ui/StaffLifecyclePanel.jsx` | `2581347` | US-R03b |
| `Badge.jsx` `STAFF_LIFECYCLE_STATUS` | `components/ui/Badge.jsx` | `2581347` | — |
| `StaffPage` lifecycle 필터 | `pages/StaffPage.jsx` | `2581347` | — |

### 70-2. 접근성·정합 재점검 결과

| 파일 | 결함 | 조치 | 근거 |
|------|------|------|------|
| `StaffLifecyclePanel` `terminatedAt` disabled | `Field help` "퇴사일 설정 불가" 안내가 `disabled` 입력 → focus 제거 → SR 미도달 | `LifecycleWorkflowPanel` `warning` Alert에 **"퇴사일 입력란은 비활성화됩니다."** 문구 병합 — SR이 form-level Alert에서 제약 인지 | WCAG 4.1.2·1.3.1 |
| `StaffLifecycleSummaryPanel` section 구조 | `section aria-labelledby` + `h2.ds-section-title` + `div.ds-stat-grid role=group aria-label` + `Alert role=status` — 변경 불요 | `StaffOnboardingCompliancePanel` 동일 구조 준수 ✅ | ✅ |
| `StaffLifecycleSummaryPanel` StatCard 라벨 | "전체·입사 진행·재직·휴직·퇴사 진행·퇴사 완료" 한국어 — 변경 불요 | WCAG 1.3.1 ✅ | ✅ |
| `StaffLifecycleSummaryPanel` `onLeaveCount Alert` | `role="status"` polite·SR 안내 — 변경 불요 | WCAG 4.1.3 ✅ | ✅ |
| `Badge ON_LEAVE` | `{ tone: "warning", label: "휴직" }` — 색(amber)+텍스트 병행 | 변경 불요 | WCAG 1.4.1 ✅ |
| `StaffPage` lifecycle 필터 `Select` | "휴직" `option` 추가 — `Field htmlFor`·SR 접근 정상 | 변경 불요 | ✅ |
| `StaffPage` 목록 `StatusBadge` | `map={STAFF_LIFECYCLE_STATUS}` → "ON_LEAVE" 키 조회 → "휴직" 텍스트+amber tone | 변경 불요 | ✅ |

### 70-3. 수정 파일

| 파일 | 변경 내용 |
|------|-----------|
| `src/components/ui/StaffLifecyclePanel.jsx` | ON_LEAVE `warning` 문자열에 "퇴사일 입력란은 비활성화됩니다." 문구 추가 |

### 70-4. coder 전달 메모

- **휴직 상태 `disabled` 필드**: 비활성화 사유·제약은 **form-level Alert(warning)** 에 명시한다. `Field help` 만으로는 `disabled` 입력 Tab 탐색 제외 시 SR이 읽지 못할 수 있다.
- **ON_LEAVE 복직 흐름**: 복직 시 `lifecycleStatus` 를 `ACTIVE` 로 전환 — `terminatedAt` 은 유지·갱신 불필요. UI는 `warning` Alert 안내 참조.
- **`StaffLifecycleSummaryPanel` StatCard 0건 분기**: `totalCount === 0` 시 `null` 반환 → 직원 없는 지점에서 패널 미표시 — 의도 동작이므로 유지.
- **`STAFF_LIFECYCLE_STATUS_OPTIONS` value 타입**: 현재 `value: STAFF_LIFECYCLE_STATUS.ON_LEAVE` (object)가 `<option value>` 에 직렬화되어 `event.target.value` = `"[object Object]"` 가 될 수 있음 — lifecycle 필터·폼 Select가 예상대로 동작하지 않을 수 있다. 수정 시 `value: "ON_LEAVE"` 문자열 키로 통일 권고(coder 영역).

### 70-5. 검증

- `StaffLifecyclePanel.test.jsx` `shows ON_LEAVE warning and saves with cleared terminatedAt` — warning 문구 갱신 반영, **11/11 PASS**.
- `npm test StaffLifecyclePanel` · build 이상 없음.

---

## §71. G-BILLING 입금·수납 대장 필터 UI 접근성 재점검 (148차)

<!-- doc:owner=UXD doc:audience=PLN,COD,TSR updated=2026-06-21 -->

> **148차 UXD (2026-06-21)** — 147차(§70)·UXD-147(`1a614c9`) 이후 coder 신규 커밋 2건(live-e2e 수정 5건 제외) 미점검 a11y·FE-16 갭 해소.

### 71-1. 대상 화면·컴포넌트

| 컴포넌트 | 위치 | 커밋 | 스토리 |
|----------|------|------|--------|
| `BillingReportPage` 입금 구간 필터 | `pages/BillingReportPage.jsx` | `e38ccfd` | US-M03 · G-BILLING · 케어포 PDF p.91 ② |
| `BillingReportPage` 수납 집계 기준 필터 | `pages/BillingReportPage.jsx` | `e38ccfd` | US-M03 · 케어포 PDF p.91 ③ |
| `appliedFilters` echo 요약 | `pages/BillingReportPage.jsx` | `c6a412f` | G-BILLING |
| `billingReportFilters.js` | `api/billingReportFilters.js` | `e38ccfd`/`c6a412f` | — |

### 71-2. 접근성·정합 재점검 결과

| 파일 | 결함 | 조치 | 근거 |
|------|------|------|------|
| `BillingReportPage` 「조회」 | `disabled={loading}` 만 있고 진행 상태 SR 미전달 | `aria-busy={loading}` 추가 | WCAG 4.1.3 · `BillingStatisticsReportPage` 정합 |
| `BillingReportPage` 적용 조건 요약 | `role=status` 만 — 구간·기준 탭 전환 후 SR 갱신 불확실 | `aria-live="polite"` 추가 | WCAG 4.1.3 · `BankDepositImportPanel` preview 패턴 |
| `BillingReportPage` 대상월 | 평문 `2026-05` | `<time dateTime={printMonthLabel}>` 래핑 | WCAG 1.3.1 · 날짜 의미론 |
| `.ds-billing-report__applied-filters` | `components.css` **미정의**(FE-16) | secondary 색·sm 글자·상단 여백·`forced-colors` 정의 | FE-16 · §1 단일 원천 |
| 입금·수납 `ds-segmented` tablist | `role=tablist`·`aria-labelledby`·`aria-selected`·로딩 중 `disabled` — 변경 불요 | `TransportPage`·`BillingStatisticsReportPage` 동일 패턴 ✅ | ✅ |
| `BillingReportsContextNav`·`StatCard role=group`·`BillingLedgerTable` | 기존 56·81·139차 패턴 준수 — 변경 불요 | ✅ | ✅ |

### 71-3. 수정 파일

| 파일 | 변경 내용 |
|------|-----------|
| `src/pages/BillingReportPage.jsx` | 조회 `aria-busy` · 적용 조건 `aria-live` · `<time dateTime>` |
| `src/styles/components.css` | `.ds-billing-report__applied-filters` 신규 정의 |
| `src/pages/BillingReportPage.test.jsx` | `aria-busy` 회귀 · appliedFilters `<time>` 단언 갱신 |

### 71-4. coder 전달 메모

- **입금 구간·수납 집계 탭**: 탭 클릭 시 즉시 `fetchReport` — 「조회」 버튼 없이도 필터가 적용된다. SR 사용자는 **적용 조건** `role=status aria-live=polite` 영역에서 서버 `appliedFilters` echo(또는 클라이언트 fallback 라벨)를 확인한다.
- **인쇄 헤더**: `.ds-care-report-print-only` 블록은 `aria-hidden="true"` — 화면 요약(`적용 조건`)과 인쇄 전용 헤더를 분리 유지.
- **API query param**: deposits → `period`(FULL/FIRST_HALF/SECOND_HALF), receipts → `basis`(PAYMENT/CLAIM) — `buildBillingReportQueryParams` 단일 원천.

### 71-5. 검증

- `BillingReportPage.test.jsx` — appliedFilters echo · `aria-busy` +1.
- `npm test BillingReportPage` · build PASS.

---

## §72. G21 공단 일정 불일치·G15 카카오 API 잔여 대시보드 위젯 접근성 재점검 (149차)

<!-- doc:owner=UXD doc:audience=PLN,COD,TSR updated=2026-06-21 -->

> **149차 UXD (2026-06-21)** — 148차(§71)·UXD-148(`e2f1246`) 이후 coder 신규 기능 커밋(live-e2e·test 수정 제외) 미점검 a11y·대비(contrast) 갭 해소.
> ① **G21 `nhisComparisonGap` StatCard**(`fe7df60`·`c01b880`·`ebc9f28`) — 공단 일정 비교 불일치 건수 위젯·방문요양형 지점만 노출.
> ② **G15 `kakaoApiQuota` StatCard**(`580a86b`) — HQ 대시보드 카카오 API 잔여 위젯(hq_admin·sysadmin).

### 72-1. 대상 화면·컴포넌트

| 위젯 | 위치 | 커밋 | 스토리 |
|------|------|------|--------|
| `nhisComparisonGap`「공단 일정 불일치」 | `pages/DashboardPage.jsx` | `fe7df60`/`c01b880`/`ebc9f28` | v2 G21 · BNK-14 |
| `kakaoApiQuota`「카카오 API 잔여」 | `pages/DashboardPage.jsx` | `580a86b` | v1.3-A G15 |
| `buildTransportKakaoQuotaDashboardWidget` | `utils/transportKakaoQuotaSummary.js` | `580a86b` | — |
| `countNhisComparisonGapLines`·`NHIS_COMPARISON_GAP_WIDGET_LABEL` | `utils/visitNhisComparison.js` | `fe7df60` | — |

### 72-2. 접근성·대비 재점검 결과

| 항목 | 점검 | 결과 |
|------|------|------|
| 색만 의존 금지(§1-2 · WCAG 1.4.1) | 두 위젯 모두 `StatCard` 값이 **텍스트**(건수·「미설정」/「정상」/「확인」)로 의미를 전달, tone(`danger`/`warning`/`success`/`default`)은 보조 강조 | ✅ 변경 불요 |
| 위젯 링크 SR 보조 텍스트(WCAG 2.4.4) | `DashboardWidgetGrid` Link `ds-sr-only "{label} 상세 보기"`·HQ 집계는 `nhisComparisonGap` href 억제(드릴다운=표) | ✅ 변경 불요 |
| 로딩 상태(WCAG 4.1.3) | 위젯 로딩 시 `role="status"`+`Spinner`(`kakaoApiQuota`는 로드 완료 후 append) | ✅ 변경 불요 |
| 비표시 분기(WCAG 1.3.1) | `nhisComparisonGap`은 비-방문요양 지점에서 위젯 자체 제외(`includeNhisComparisonGap`)·`kakaoApiQuota`는 role 게이트 | ✅ 변경 불요 |
| **강제 색상 모드 대비(WCAG 1.4.11)** | **`.ds-dashboard-widgets__item .ds-stat` 에 `forced-colors` 경계선 미정의** — 앱 내 다른 모든 `.ds-stat` 클러스터(billing report·monitoring·staff status·nursing report 등)는 `ButtonText` 경계선을 명시하나 **주(主) US-M02 위젯 그리드만 누락** | **보강(아래 72-3)** |

### 72-3. 수정 파일

| 파일 | 변경 내용 |
|------|-----------|
| `src/styles/components.css` | `@media (forced-colors: active) .ds-dashboard-widgets__item .ds-stat { border: 1px solid ButtonText }` 신규 — 강제 색상 모드에서 인접 위젯 카드 구분 보장. G21·카카오 위젯 추가로 hq_admin·sysadmin 그리드가 조밀해져 효과 ↑ |

> 순수 대비(contrast) 보강 — JSX·동작·데이터·시각(일반 모드) 불변. 모든 `.ds-stat` 클러스터의 `forced-colors` 경계선 컨벤션과 정합(§71 이전 ~10개 절 동일 패턴).

### 72-4. coder 전달 메모

- **카카오 위젯 값 의미**: `buildTransportKakaoQuotaDashboardWidget` — `restKeyConfigured=false`→「미설정」(warning)·`quotaExceeded`→`0`건(danger)·usage rows 0건+probe OK→「정상」(success)·그 외→최소 `remainingToday`(≤500 warning). 모두 **텍스트 + tone** 병행이라 색 의존 없음.
- **G21 위젯 노출 조건**: `isHomeVisitLikeServiceType(activeBranchServiceType)` 또는 HQ 집계·serviceType 미상일 때만. 비-방문요양 지점에서 **위젯 자체 미렌더**(빈 0 위젯 노출 안 함) — `buildWidgets({ includeNhisComparisonGap })`·`HQ_BRANCH_SCOPED_WIDGET_IDS` 단일 원천.
- 신규 위젯에 **별도 라벨/링크 변경 불요** — 기존 `DashboardWidgetGrid`·`StatCard` 패턴 그대로 a11y 충족.

### 72-5. 검증

- `npm test`(DashboardPage·transportKakaoQuotaSummary·visitNhisComparison 포함) — coder 기존 회귀 유지(본 변경은 CSS-only `forced-colors`로 JS 회귀 추가 불요).
- build PASS.

---

## §73. G-BILLING-OVERDUE-ADJUSTMENT·G-STAFF-DOCUMENT-REPOSITORY·G-BATHING 전월 복사 접근성 재점검 (150차)

<!-- doc:owner=UXD doc:audience=PLN,COD,TSR updated=2026-06-21 -->

> **150차 UXD (2026-06-21)** — 149차(§72)·UXD-149(`b969570`) 이후 coder 신규 기능 커밋 미점검 a11y·FE-16 갭 해소.
> ① **G-BILLING-OVERDUE-ADJUSTMENT** `OverdueManagementModal`(`0420e6b`).
> ② **G-STAFF-DOCUMENT-REPOSITORY** `StaffDocumentRepositoryPanel`(`03d0d43`/`fd15a2f`).
> ③ **G-BATHING** `BathingSchedulePage` 전월 복사(`9a957fb`).

### 73-1. 대상 화면·컴포넌트

| 컴포넌트 | 위치 | 커밋 | 스토리 |
|----------|------|------|--------|
| `OverdueManagementModal` | `components/ui/` | `0420e6b` | US-L02 · G-BILLING-OVERDUE-ADJUSTMENT |
| `StaffDocumentRepositoryPanel` | `components/staff/` | `03d0d43`/`fd15a2f` | US-R03c · G-STAFF-DOCUMENT-REPOSITORY |
| `BathingSchedulePage` 전월 복사 | `pages/` | `9a957fb` | US-O01 · G-BATHING |

### 73-2. 접근성·FE-16 재점검 결과

| 항목 | 대상 | 결과 |
|------|------|------|
| 날짜 의미론(WCAG 1.3.1) | `OverdueManagementModal` 독려·조정 일시 | `toLocaleString` 평문 → `<time dateTime>` |
| 폼 식별(WCAG 1.3.1) | 독려기록·조정 폼 | `aria-label="미납 독려기록 추가"`·`aria-label="미납 조정"` |
| 반복 행 액션(WCAG 2.4.6) | 서류 슬롯 업로드·lifecycle 링크 | `${slot.label} 파일 업로드 선택`·`${slot.label} lifecycle 체크` |
| 로딩 상태(WCAG 4.1.3) | repository 패널 | `section aria-busy`·`role=status` Spinner 래퍼 |
| 진행 버튼(WCAG 4.1.3) | 목욕 일정 조회·전월 복사 | `aria-busy={loading}`·`aria-busy={copying}` |
| 미정의 CSS(FE-16) | `.ds-staff-document-repository*` | 베이스·phase·summary·`forced-colors` 경계선 승격 |

### 73-3. 수정 파일

| 파일 | 변경 내용 |
|------|-----------|
| `OverdueManagementModal.jsx` | `RecordedAtCell`·폼 `aria-label` |
| `StaffDocumentRepositoryPanel.jsx` | `aria-busy`·`aria-label`·로딩 `role=status` |
| `BathingSchedulePage.jsx` | 조회·전월 복사 `aria-busy` |
| `components.css` | `.ds-staff-document-repository*`·`forced-colors` |

### 73-4. coder 전달 메모

- **`OverdueManagementModal`** — 탭·표·`Field error`·제출 `aria-busy`는 coder 구현 시 이미 표준 패턴 준수. `OverduePage` 행 「관리」버튼 `${이용자명} 미납 관리` `aria-label` 유지.
- **`StaffDocumentRepositoryPanel`** — 21슬롯 Badge(「첨부됨」/「체크됨」/「미비」)는 텍스트+색 병행. `onSelectUploadType(slot.id)` wire는 `StaffDetailPage` HR 파일함과 연동(coder 영역).
- **`BathingSchedulePage`** — 전월 복사 성공 메시지는 기존 `Alert role=status`·`aria-label="전월 목욕 일정 복사"` 패턴 유지.

### 73-5. 검증

- `OverdueManagementModal.test.jsx` — `<time dateTime>` 단언 +1.
- `StaffDocumentRepositoryPanel.test.jsx` — 컨텍스트 `aria-label` 단언 갱신.
- `npm test`(해당 3종 + `BathingSchedulePage`)·build PASS.

---

## §74. US-R03 모바일 서류 촬영 업로드 접근성 재점검 + `.ds-button` 미정의 셀렉터 회귀 해소 (151차)

<!-- doc:owner=UXD doc:audience=PLN,COD,TSR updated=2026-06-21 -->

> **151차 UXD (2026-06-21)** — 150차(§73)·UXD-150(`751c593`) 이후 coder 신규 기능 커밋 `6bde24a`(feat US-R03 — 케어포 p.96 모바일 서류 촬영 업로드: `FileUpload` `enableMobileCapture`·`StaffDocumentRepositoryPanel` 슬롯별 「모바일 촬영」·`StaffHrFilePanel`·`StaffRefresherCertificatePanel`) 미점검 a11y·FE-16 갭 해소.

### 74-1. 대상 화면·컴포넌트

| 컴포넌트 | 위치 | 커밋 | 스토리 |
|----------|------|------|--------|
| `FileUpload` `enableMobileCapture` | `components/ui/` | `6bde24a` | US-R03 P2 모바일 촬영 |
| `StaffDocumentRepositoryPanel` 슬롯 「모바일 촬영」 | `components/staff/` | `6bde24a` | US-R03c · G-STAFF-DOCUMENT-REPOSITORY |
| `StaffHrFilePanel` · `StaffRefresherCertificatePanel` | `components/staff/` | `6bde24a` | US-R03 · US-S02 |

### 74-2. 접근성 재점검 결과 (변경 불요로 확인된 항목)

| 항목 | 대상 | 결과 |
|------|------|------|
| 숨김 카메라 input | `FileUpload`·`StaffDocumentRepositoryPanel` | `capture="environment"` input에 `aria-hidden="true"`·`tabIndex={-1}` — 트리거 버튼으로만 활성화(중복 탭 정지점 없음·WCAG 4.1.2) |
| 반복 행 액션 라벨(WCAG 2.4.6) | 슬롯별 「모바일 촬영」 | `${slot.label} 모바일 촬영 업로드` `aria-label`·진행 중 `aria-busy` |
| 진행/오류 상태(WCAG 4.1.3) | repository 패널 | 업로드 중 `section aria-busy`·실패 `Alert role=alert`·버튼 `aria-busy` |
| 색 비의존(WCAG 1.4.1) | 「모바일 촬영」 버튼 | 「업로드 중…」 텍스트 라벨 전환으로 상태 노출 |

### 74-3. 회귀 수정 — `.ds-button` 미정의 셀렉터 (FE-16·§1 단일 토큰 원천)

- **결함**: `6bde24a`가 추가한 `@media (max-width: 640px)` 규칙이 서류함 슬롯 액션 버튼(「업로드 선택」·「모바일 촬영」)을 모바일에서 전폭(`width: 100%`)으로 스택하려고 `.ds-staff-document-repository .ds-inline-actions .ds-button` 셀렉터를 사용했으나, 본 코드베이스의 `Button` 컴포넌트는 **`.ds-btn`** 클래스를 렌더한다(`.ds-button`은 전 CSS에서 이 한 곳만 사용된 **미정의 클래스**). 따라서 의도한 모바일 전폭 규칙이 적용되지 않던 80·90·119차에서 반복 추적한 「미정의 클래스」 회귀와 동일 패턴.
- **수정**: 셀렉터 `.ds-button` → **`.ds-btn`**(`components.css`). 컨테이너 `flex-direction: column; align-items: stretch`와 함께 버튼이 모바일에서 일관되게 전폭 스택되도록 복구. 시각·동작·DOM 불변(순수 CSS 정합).

### 74-4. 수정 파일

| 파일 | 변경 내용 |
|------|-----------|
| `components.css` | `.ds-staff-document-repository .ds-inline-actions .ds-button` → `.ds-btn`(모바일 전폭 규칙 복구) |

### 74-5. coder 전달 메모

- **`FileUpload.enableMobileCapture`** — 카메라 input은 `accept="image/*" capture="environment"`로 모바일에서 후면 카메라를 연다. 데스크톱은 `capture` 무시·파일 선택기로 폴백되므로 별도 분기 불요.
- **포커스 관리(잔여 관찰)** — 「모바일 촬영」 업로드 성공 시 해당 슬롯이 `slot.uploaded=true`가 되어 버튼 블록이 사라지며 포커스가 `body`로 유실될 수 있다. 성공은 하단 요약 `Alert role=status`(미비 건수→충족 전환)로 안내되나, 추후 업로드 성공 시 슬롯 행/상태로 포커스 이동을 고려할 수 있음(coder 영역·동작 변경 수반).

### 74-6. 검증

- `StaffDocumentRepositoryPanel.test.jsx`(4)·`FileUpload.test.jsx`(4) — 8/8 PASS.
- `npm run build` PASS(CSS 컴파일 오류 없음).

---

---

## §75. G-STAFF-WORK-ATTENDANCE·G-BILLING-DEPOSIT-ORDER-GUARD·US-E05 출석 통계 접근성 재점검 (152차)

<!-- doc:owner=UXD doc:audience=PLN,COD,TSR updated=2026-06-22 -->

> **152차 UXD (2026-06-22)** — 151차(§74)·UXD-151(`9812ac4`) 이후 coder 신규 기능 커밋 미점검 a11y·FE-16 갭 해소.
> ① **G-STAFF-WORK-ATTENDANCE** `StaffWorkAttendancePage`(`53d65a0`/`5fd468b`) — 직원 출퇴근 (8-4) 신규 페이지.
> ② **G-BILLING-DEPOSIT-ORDER-GUARD** `CmsDebitPanel`(`dfa981c`) — 선행입금 가드 CMS 출금 패널 업데이트.
> ③ **US-E05** `AttendanceStatsPage`(`dffd726`) — 출석 통계 API 정렬 및 결석 체크아웃 와이어.

### 75-1. 대상 화면·컴포넌트

| 컴포넌트 | 위치 | 커밋 | 스토리 |
|----------|------|------|--------|
| `StaffWorkAttendancePage` | `pages/` | `53d65a0`/`5fd468b` | G-STAFF-WORK-ATTENDANCE · 케어포 8-4 |
| `CmsDebitPanel` | `components/ui/` | `dfa981c` | US-L03 · G-BILLING-DEPOSIT-ORDER-GUARD |
| `AttendanceStatsPage` | `pages/` | `dffd726` | US-E05 · 월별 출석 통계 |
| `StaffContextNav` | `components/ui/` | `5fd468b` | US-S01 · `/staff/attendance` 링크 추가 |

### 75-2. 접근성·FE-16 재점검 결과

| 파일 | 결함 | 조치 | 근거 |
|------|------|------|------|
| `StaffWorkAttendancePage` 「조회」 | `disabled={loading}` 만 있고 진행 상태 SR 미전달 | `aria-busy={loading}` 추가 | WCAG 4.1.3 · `BillingReportPage` 정합 |
| `StaffWorkAttendancePage` StatCard 그룹 | `section.ds-stat-grid`에 시맨틱 그룹 없음 | `role="group" aria-label="직원 출퇴근 현황 요약"` | WCAG 1.3.1 · §93 `StaffStatusReportPage` 패턴 |
| `StaffWorkAttendancePage` 출근·퇴근 버튼 | 다중 행에서 동일 「출근」/「퇴근」 텍스트 — SR이 대상 직원 식별 불가 | `aria-label="${row.userName} 출근"` / `"퇴근"` + `aria-busy={busy}` | WCAG 2.4.6 · §91 `ClientRiskAssessmentPanel` 패턴 |
| `StaffWorkAttendancePage` 출근·퇴근 시각 | `formatTimestamp()` 평문 | `<time dateTime={row.checkInAt}>` / `<time dateTime={row.checkOutAt}>` (값 있을 때만) | WCAG 1.3.1 · §88 `StaffDetailPage` 날짜 의미론 패턴 |
| `AttendanceStatsPage` 「조회」 | `disabled={loading}` 만 있고 진행 상태 SR 미전달 | `aria-busy={loading}` 추가 | WCAG 4.1.3 |
| `AttendanceStatsPage` StatCard 그룹 | `div.ds-grid.ds-grid--gap-bottom`에 시맨틱 그룹 없음 | `role="group" aria-label="출석 통계 요약"` | WCAG 1.3.1 · §116 `TransportMonthlyReportsPage` 패턴 |
| `CmsDebitPanel` 요청·완료 일시 | `formatDateTime()` 평문 | `<time dateTime={debit.requestedAt}>` / `<time dateTime={debit.completedAt}>` (값 있을 때만) | WCAG 1.3.1 · 날짜 의미론 |
| `CmsDebitPanel` 출금 상태 컨테이너 | `<div role="status">` — `h3` 제목과 프로그램적 연결 없음 | `<section aria-labelledby="cms-debit-status-heading">` + `h3 id="cms-debit-status-heading"` | WCAG 1.3.1 · §100 `EasyPayPanel.ds-easy-pay-status` 패턴 |
| `StaffContextNav` `/staff/attendance` 링크 | NavLink `aria-current="page"` — NavLink 자동 적용 · 변경 불요 | ✅ | ✅ |

### 75-3. 수정 파일

| 파일 | 변경 내용 |
|------|-----------|
| `src/pages/StaffWorkAttendancePage.jsx` | 조회 `aria-busy` · StatCard `role=group` · 출근·퇴근 버튼 `aria-label`+`aria-busy` · 시각 `<time dateTime>` |
| `src/pages/AttendanceStatsPage.jsx` | 조회 `aria-busy` · StatCard 그룹 `role=group aria-label` |
| `src/components/ui/CmsDebitPanel.jsx` | 일시 `<time dateTime>` · 상태 컨테이너 `<section aria-labelledby>` + `h3 id` |

### 75-4. coder 전달 메모

- **`StaffWorkAttendancePage` 출근·퇴근 버튼 `aria-busy`** — `actionUserId === row.userId` 조건 활용. Spinner는 시각 사용자에게 진행 상태를 보여주나 `aria-busy`로 SR에도 전달.
- **`StaffWorkAttendancePage` `<time dateTime>`** — `row.checkInAt`/`row.checkOutAt`은 ISO 8601 타임스탬프(`2026-06-22T08:30:00Z` 형태). 값이 falsy이면 「—」 평문으로 폴백 유지.
- **`CmsDebitPanel` `<section role="status">`** — `role="status"` + `aria-live="polite"` 유지. 상태 갱신(출금 요청 후 `setDebit`) 시 `aria-live` 영역이 SR에 상태 변화를 안내. `h3 id`는 섹션 `aria-labelledby`만 위해 추가 — 외부 영역에서 참조 불요.
- **`StaffContextNav`** — `/staff/attendance` 링크 추가로 8-4 페이지가 직원 컨텍스트 네비에 등재됨. `aria-current` NavLink 자동 처리 확인.

### 75-5. 검증

- `StaffWorkAttendancePage.test.jsx` — `aria-busy` · `role=group` · 출근 버튼 `aria-label` 직원명 포함 · `<time dateTime>` 단언 +4.
- `AttendanceStatsPage.test.jsx` — `aria-busy` · `role=group aria-label` +2.
- `CmsDebitPanel.test.jsx` (기존 없음) — `section[aria-labelledby]` · `time[dateTime]` 확인.
- `npm test` · build PASS.

---

---

## §76. US-D03 이용자 출석 탭·G-BILLING-REPORT-FILTER-PERSISTENCE·US-E03 QR 이미지 접근성 재점검 (153차)

<!-- doc:owner=UXD doc:audience=PLN,COD,TSR updated=2026-06-22 -->

> **153차 UXD (2026-06-22)** — 152차(§75)·UXD-152(`df7f308`) 이후 coder 신규 기능 커밋 미점검 a11y·FE-16 갭 해소.
> ① **US-D03 `ClientDetailPage` 출석 탭**(`d058e43`) — 이용자 상세 출석 이력 탭 API 연동.
> ② **G-BILLING-REPORT-FILTER-PERSISTENCE** `BillingReportPage`(`77b1ea8`) — 청구 대장 필터 복원 API 연동.
> ③ **US-E03 QR 이미지** `QrGeneratePage`(`250619e`) — 지점 QR 코드 PNG 데이터 URL 렌더.

### 76-1. 대상 화면·컴포넌트

| 컴포넌트 | 위치 | 커밋 | 스토리 |
|----------|------|------|--------|
| `ClientDetailPage` 출석 탭 | `pages/ClientDetailPage.jsx` | `d058e43` | US-D03 |
| `BillingReportPage` 필터 복원 | `pages/BillingReportPage.jsx` | `77b1ea8` | G-BILLING-REPORT-FILTER-PERSISTENCE |
| `QrGeneratePage` QR PNG | `pages/QrGeneratePage.jsx` | `250619e` | US-E03 |
| `branchQrCode.js` | `utils/branchQrCode.js` | `250619e` | — |

### 76-2. 접근성·FE-16 재점검 결과

| 파일 | 결함 | 조치 | 근거 |
|------|------|------|------|
| `BillingReportPage` 필터 복원 | `hydrateFiltersAndFetch` — `loadSavedFilters` 호출 중 `loading=false` 상태라 버튼 `aria-busy` 미전달 | `setLoading(true)` 를 `loadSavedFilters` 호출 **앞에** 선행 추가 | WCAG 4.1.3 · §71 패턴 정합 |
| `QrGeneratePage` 유효 시간 | `qrData.validUntil` → `new Date(...).toLocaleTimeString()` 평문 | `<time dateTime={qrData.validUntil}>` 래핑 | WCAG 1.3.1 · §88 날짜 의미론 |
| `ClientDetailPage` 출석 탭 — 로딩 | `attendanceHistoryLoading ? <Spinner label="출석 이력 불러오는 중" />` | `Spinner role="status" aria-label` — 탭 자동 로드 패턴·변경 불요 | ✅ |
| `ClientDetailPage` 출석 탭 — 날짜 | `entry.attendanceDate` / `entry.checkInAt` / `entry.checkOutAt` | `<time dateTime>` 래핑 구현됨·변경 불요 | ✅ |
| `ClientDetailPage` 출석 탭 — 상태 | `StatusBadge` `ATTENDANCE_STATUS` — 색+텍스트 병행 | 표준 패턴 준수·변경 불요 | ✅ |
| `ClientDetailPage` 출석 탭 — 표 | `Table caption={이용자명 출석 이력}`·`th scope="col"` | 표준 패턴 준수·변경 불요 | ✅ |
| `ClientDetailPage` 출석 탭 — 빈 상태 | `EmptyState title="출석 기록 없음"` | 빈 table tbody 대신 EmptyState — 표준 패턴 준수 | ✅ |
| `QrGeneratePage` `alt` | `alt={지점 ${directionLabel} QR 코드}` — `branchQrDirectionLabel` 동적 변환 | 변경 불요 | ✅ |
| `QrGeneratePage` `figure aria-labelledby` | `<figure aria-labelledby="qr-preview-caption">` + `<figcaption id="qr-preview-caption">` | 표준 패턴 준수·변경 불요 | ✅ |
| `BillingReportPage` 필터 탭 `role=tablist` | `aria-labelledby`·`aria-selected`·로딩 중 `disabled` — §71 검토 기준 | 변경 불요 | ✅ |

### 76-3. 수정 파일

| 파일 | 변경 내용 |
|------|-----------|
| `src/pages/BillingReportPage.jsx` | `hydrateFiltersAndFetch` 내 `setLoading(true)` 선행 추가 — 필터 복원 구간 `aria-busy` 커버 |
| `src/pages/QrGeneratePage.jsx` | `validUntil` `toLocaleTimeString` → `<time dateTime={qrData.validUntil}>` 래핑 |

### 76-4. coder 전달 메모

- **`BillingReportPage` 로딩 흐름**: 이제 `hydrateFiltersAndFetch` 진입 즉시 `loading=true` → 버튼 `aria-busy`·`disabled` 활성 → 필터 복원 완료 후 `fetchReport` 호출 → 보고서 응답 후 `loading=false`. 중간에 `fetchReport`도 `setLoading(true)`를 호출하므로 중복 없음.
- **`QrGeneratePage` `validUntil`**: ISO 8601 타임스탬프(`expiresAt`)를 `dateTime` 속성으로 전달. `toLocaleTimeString("ko-KR")` 표시 텍스트는 그대로 유지.
- **`branchQrCode.js`**: `buildBranchQrGenerateRequest`·`mapBranchQrGenerateResponse`·`qrTokenToDataUrl` — `QrGeneratePage`·`services.js`와 결합 단일 원천. 신규 유틸이라 별도 a11y 적용 대상 없음.
- **`ClientDetailPage` 출석 탭 접근성 흐름**: 탭 전환 → `useEffect` 발화 → `Spinner role="status"` 안내 → API 응답 → `EmptyState` 또는 `Table caption`. 모두 코드베이스 표준 패턴 준수.

### 76-5. 검증

- `BillingReportPage.test.jsx` — 필터 복원 구간 `aria-busy` 상태 확인(기존 회귀 유지).
- `QrGeneratePage.test.jsx` — `<time dateTime>` 속성 단언 +1.
- `npm test` · build PASS.

---

## §77. G2-CMS-ROSTER·G34·G30-LEGEND 접근성 재점검 + G-STAFF-ANNUAL-LEAVE UI 셸 (154차)

<!-- doc:owner=UXD doc:audience=PLN,COD,TSR updated=2026-06-22 -->

> **154차 UXD (2026-06-22)** — 153차(§76)·UXD-153(`da34daf`) 이후 coder 신규 기능 커밋 미점검 a11y·US-R03e 컴포넌트 갭 해소.
> ① **G2-CMS-ENROLLMENT-ROSTER** `CmsEnrollmentTable`(`df9ec6c`→`3ece965`).
> ② **G34-WORKFLOW-CATALOG** `EzcareWorkflowCatalogPanel`(`77cfc38`/`9f110a5`).
> ③ **G30-LEGEND** `MonitoringOfficialIndicatorLegendPanel`(`fdc135b`).
> ④ **G-STAFF-ANNUAL-LEAVE P3** `StaffAnnualLeaveTable` UI 셸 신규(BNK-516 · US-R03e).

### 77-1. 대상 화면·컴포넌트

| 컴포넌트 | 위치 | 커밋 | 스토리 |
|----------|------|------|--------|
| `CmsEnrollmentTable` | `components/ui/` | `df9ec6c`→`3ece965` | G2-CMS-ENROLLMENT-ROSTER · US-L03 |
| `EzcareWorkflowCatalogPanel` | `components/compliance/` | `77cfc38`/`9f110a5` | G34-WORKFLOW-CATALOG · US-T16 |
| `MonitoringOfficialIndicatorLegendPanel` | `components/monitoring/` | `fdc135b` | G30-LEGEND |
| `StaffAnnualLeaveTable` | `components/ui/` | **신규** | G-STAFF-ANNUAL-LEAVE · US-R03e |

### 77-2. 접근성·FE-16 재점검 결과

| 파일 | 결함 | 조치 | 근거 |
|------|------|------|------|
| `CmsEnrollmentTable` 등록일시 | `formatDateTime()` 평문 | `<time dateTime={row.enrolledAt}>` (`DateTimeCell`) | WCAG 1.3.1 · §88 날짜 의미론 |
| `CmsEnrollmentTable` 이용자 링크 | roster 모드에서 링크 텍스트만으로 대상 식별 | `aria-label="${clientName} CMS 등록 관리"` | WCAG 2.4.4 |
| `EzcareWorkflowCatalogPanel` 표 | `Table` caption 누락 | `caption="운영주기별 워크플로 카탈로그" captionVisuallyHidden` (h2와 중복 방지) | WCAG 1.3.1 · §76 `ClientDetailPage` 패턴 |
| `MonitoringOfficialIndicatorLegendPanel` 표 | `Table` caption 누락 | `caption="공단 평가지표 ogada 문항 매핑" captionVisuallyHidden` | WCAG 1.3.1 |
| `EzcareWorkflowCatalogPanel` 외부 FAQ 링크 | `aria-label`에 「새 창」 포함 | 변경 불요 | ✅ |
| `EzcareWorkflowCatalogPanel` FilterChips·StatCard | radiogroup·`role=group`·`aria-live` | 변경 불요 | ✅ |

### 77-3. G-STAFF-ANNUAL-LEAVE UI 셸 (US-R03e · P3 candidate)

ezCare [**worker-b100**](https://www.ezcare.easyms.co.kr/new.ez?PGID=worker-b100) tab01 「연차휴가 현황」 jqGrid 14-field parity를 위한 **presentational 컴포넌트**. API·Route는 coder 영역.

| ezCare 필드 | ogada prop | 비고 |
|-------------|-----------|------|
| wCode | `staffCode` | 직원코드 |
| wName | `staffName` + `staffId` | `staffId` 있으면 `/staff/:id` 링크 |
| wGroup | `staffGroup` | 소속·직군 |
| date_enter | `hiredAt` | `<time dateTime>` |
| month_1~12 | `monthlyUsed` | 배열 또는 `{1:…,12:…}` |
| annual_vacation | `annualEntitlement` | 연차 부여일 |
| vacation_total | `usedTotal` | 미제공 시 월별 합산 |
| (잔여) | `remainingTotal` | 미제공 시 `entitlement - used` |
| memo | `memo` | 비고 |

**권장 Route**: `/staff/annual-leaves` · **권장 Page**: `StaffAnnualLeavePage` + `StaffContextNav` 「연차휴가 (8-13)」 링크 추가 · **연계**: US-R01 `/staff/leave-ledger` cross-link.

### 77-4. CSS·토큰

| 클래스 | 용도 |
|--------|------|
| `.ds-staff-annual-leave` | 섹션 그리드·`gap: var(--space-3)` |
| `.ds-staff-annual-leave__table` | 12개월 열 포함 wide table (`ds-table-wrap` 가로 스크롤) |
| `.ds-staff-annual-leave__month-col` | 월별 열 중앙 정렬·`min-width: 2.75rem`·`forced-colors` 경계선 |

### 77-5. 수정·신규 파일

| 파일 | 변경 내용 |
|------|-----------|
| `CmsEnrollmentTable.jsx` | `DateTimeCell`·이용자 링크 `aria-label` |
| `EzcareWorkflowCatalogPanel.jsx` | `Table caption` |
| `MonitoringOfficialIndicatorLegendPanel.jsx` | `Table caption` |
| `StaffAnnualLeaveTable.jsx` | **신규** — 연차 현황 표·요약 StatCard |
| `staffAnnualLeave.js` | **신규** — 월별 정규화·요약 유틸 |
| `components.css` | `.ds-staff-annual-leave*` |
| `index.js` | `StaffAnnualLeaveTable` export |

### 77-6. coder 전달 메모

- **`StaffAnnualLeaveTable`** — `rows` prop만 연결하면 표시 가능. `year`·`loading`·`showSummary`·`staffDetailBasePath` 지원.
- **API 후보** — `GET /api/v1/staff/annual-leaves?branchId=&year=` branch-scoped roster (BNK-516 · backend 미구현 P3).
- **`StaffContextNav`** — Route·RBAC 확정 후 `{ to: "/staff/annual-leaves", label: "연차휴가 (8-13)" }` 추가(현재 링크 없음·404 방지).
- **US-R01 연계** — 페이지 하단에 `/staff/leave-ledger` 안내 링크 권장(연차 대장과 역할 분리: 현황 조회 vs 대장 CRUD).

### 77-7. 검증

- `CmsEnrollmentTable.test.jsx` — `time[dateTime]`·링크 `aria-label` +2.
- `StaffAnnualLeaveTable.test.jsx` — 요약·월별 열·직원 링크 3건.
- `staffAnnualLeave.test.js` — 정규화·요약 2건.
- `npm test` · build PASS.

---

## §78. G-STAFF-ANNUAL-LEAVE Page wire-up 접근성 재점검 + 공통 form CSS (155차)

<!-- doc:owner=UXD doc:audience=PLN,COD,TSR updated=2026-06-23 -->

> **155차 UXD (2026-06-23)** — 154차(§77)·UXD-154(`5353991`) 이후 coder가 `StaffAnnualLeavePage`·API·validation·pilot title을 wire(`3902dba`→`971c7f1`)한 뒤 미점검 a11y·FE-16 갭 해소.

### 78-1. 대상 화면·커밋

| 화면/파일 | 커밋 | 스토리 |
|-----------|------|--------|
| `StaffAnnualLeavePage` | `3902dba`→`971c7f1` | G-STAFF-ANNUAL-LEAVE · US-R03e |
| `StaffContextNav` annual-leaves 링크 | `3902dba` | US-S01 · Staff HR cluster |
| `staffAnnualLeave.js` validation | `80613c3` | BNK-525/526 BE 정합 |

### 78-2. 접근성·FE-16 재점검 결과

| 파일 | 결함 | 조치 | 근거 |
|------|------|------|------|
| `StaffAnnualLeavePage` 저장 성공 | `Alert` tone만, SR live 미전달 | `role="status"` + `ds-page-alert` | WCAG 4.1.3 · §75 `StaffWorkAttendancePage` 패턴 |
| `StaffAnnualLeavePage` 수정 modal | `<form>` 이름 없음 | `aria-label="${직원명} 연차휴가 수정"` | WCAG 4.1.2 · `StaffTrainingLogPage` 패턴 |
| `StaffAnnualLeavePage` 표 영역 | 로딩 중 busy 미표시 | `<section aria-busy={loading}>` | WCAG 4.1.3 |
| `StaffAnnualLeavePage`·`StaffWorkAttendancePage` | `.ds-help-text` 미정의 | **신규 CSS** — muted 안내 문구 | FE-16 |
| `StaffAnnualLeavePage`·`StaffHealthCheckupsPage` | `.ds-fieldset` 미정의 | **신규 CSS** — 그룹 fieldset·legend·`forced-colors` | FE-16 |
| `StaffAnnualLeaveTable`·`StaffContextNav`·조회 버튼 | caption·nav·`aria-busy` | 변경 불요 | ✅ (154차·coder wire 준수) |

### 78-3. CSS·토큰 (신규)

| 클래스 | 용도 |
|--------|------|
| `.ds-help-text` | 카드 상단 안내 — `font-size-sm`·`color-text-muted`·하단 `space-4` |
| `.ds-fieldset` | modal/폼 fieldset — `surface-muted` 배경·`radius-md`·legend semibold |

### 78-4. coder 전달 메모

- **US-R01 leave-ledger cross-link** — `/staff/leave-ledger` Route 미구현 → 링크 추가 보류(USER_STORIES US-R03e 잔여 항목).
- **pilot Must-page title** — `STAFF_ANNUAL_LEAVE_PAGE_TITLE = "직원 연차휴가"` story-id suffix 금지 유지(BNK-527).
- **`StaffAnnualLeaveTable`** — Page에서 `PageLoading` + 표 컴포넌트 분리 패턴 유지(coder wire 그대로).

### 78-5. 검증

- `StaffAnnualLeavePage.test.jsx` — `form` `aria-label`·성공 `role=status` +2.
- `npm test` · build PASS.

---

*이 문서는 ux_designer 에이전트(UXD)가 관리합니다. 토큰·컴포넌트 변경 시 본 문서와 `memory/decisions.md`를 동기화하세요.*
