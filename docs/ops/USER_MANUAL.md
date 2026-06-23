<!-- doc:owner=TWR doc:audience=PLN,COD updated=2026-06-23T19:00:00Z -->
# ogada 사용자 매뉴얼 (ops/USER_MANUAL.md)

> **작성**: tech_writer 에이전트  
> **최초 작성일**: 2026-06-05  
> **최종 갱신**: 2026-06-23 (336차 TWR 자동 동기화 — **BE `c4e6bcb`/FE `426d63a`·V1–V175·111 route·90 page·모듈 KPI 78.79%·merge gate 719 carry·V175 leave-ledger integrity ✅**)  
> **대상 독자**: 주간보호센터 현장 사용자 — **통합 관리자**, **센터장**, **요양보호사**, **사회복지사**, **보호자**  
> **기준 문서**: `docs/planning/REQUIREMENTS.md`, `docs/technical/API_SPEC.md`, `docs/planning/FLOWCHART.md`, `docs/planning/USER_STORIES.md`  
> **기술 스택**: Java Spring Boot 3.x + React (Vite SPA) + PostgreSQL

---

## 1. 이 매뉴얼에 대하여

### 1-1. 목적

ogada는 전국 주간보호센터·요양기관을 위한 **B2B SaaS 운영 관리 웹 시스템**입니다.  
이 문서는 현장에서 매일 사용하는 **통합 관리자(`hq_admin`)**, **센터장(`branch_admin`)**, **요양보호사(`caregiver`)**, **사회복지사(`social_worker`)**, **보호자(`guardian`)**를 대상으로, 로그인부터 일상 업무·월말 청구까지의 화면 흐름과 조작 방법을 설명합니다.

### 1-2. 문서 범위

| 포함 | 제외 |
|------|------|
| MVP v1 Must 기능 (이용자·출석·건강·청구·대시보드·배차·**간호급여**·욕창 케어) | ogada 내부 `platform_admin` 운영 |
| 역할별 메뉴·권한·업무 절차 | `sysadmin` 기술 설정 상세 (→ `ADMIN_GUIDE.md`) |
| 보호자 QR 셀프 체크인 (B방식) | `caregiver`·`social_worker` 전용 **식단·일정 등록** (관리자만, §5-9) |

### 1-3. 구현 상태 안내 (2026-06-23 develop HEAD `c4e6bcb` / frontend `426d63a` 기준 — 336차 baseline)

| 영역 | 상태 | 비고 |
|------|------|------|
| 백엔드 API | **Must + … + V175 ✅** @ `c4e6bcb` **SYNCED** · **V175 leave-ledger integrity ✅** · **SOCIAL_WORKER users read RBAC ✅** · **client address road-level masking ✅** · … | BE Test **1846** (Q668) |
| 데이터베이스 | Flyway **V1–V175** | **V175** leave-ledger memo·user_branch FK · **V174** `staff_leave_ledger_entries` · **V173** annual-leave integrity · **V172** roster table |
| 프론트엔드 | **111 route · 90 page** @ `426d63a` **SYNCED** | **`/staff/leave-ledger` ✅ full-stack + UXD-157 a11y** (Q667) · **QA-B268 Fixed** (Q664) · **FE WT DIRTY** |
| UI 연동 완료 | **Must 기능 full-stack ✅** — 출석·청구·QR·직원 출퇴근·연차 roster·**연차·유급휴일 대장**·HR cross-link 등 | **M6 6-1 `/meals` LIVE** (Q660) |
| UI API 갭 | **Must 갭 0** (기존 Must) | **P3**: **G-COMM-CALLER-AUTH** · 카메라 QR · NFC · **7-5 live PG** · **M6 6-2~6-4 `/safety/*`** |
| **P2 Planned** | **L03 간호급여 잔여 5 leaf·7-5 live PG·J03 Solapi live dispatch·LCMS CMS 3-method·G34 SMS live·G-Payroll·G30 live E2E** | **G-STAFF-WELFARE P3**(FAQ21796) · **8-12 PDF 공식 서식**(Q315) · **선임 업무수행일지 템플릿 카탈로그** P3 (Q635 잔여) |
| JWT 저장 | **access 메모리 + refresh `sessionStorage`** (SEC-005, 결정 96) | **같은 탭** 새로고침·뒤로가기 시 **`restoreSession()`** 으로 유지. **탭 닫기**·로그아웃 시 재로그인. **30분 idle** 시 SessionTimeoutModal (Q112) |
| 본 매뉴얼 | **연동 UI + Swagger 병기 · Q326~Q329·Q321·Q325·Q320 반영** | **G2/7-5 stub PG** — 실제 카드·카카오 결제는 live PG 후속 |

> 파일럿 현장(지점 2, 센터장 1, 요양보호사 5)은 **`branch_admin` + `caregiver`** 수기 출석·건강 기록 중심으로 검증합니다.

### [TWR] 1-4. Must API·화면 빠른 점검표 (운영 우선순위)

매일 운영 점검 시 아래 4개만 먼저 확인하면 Must 기능 누락을 빠르게 발견할 수 있습니다.

| 우선순위 | 화면 | 확인 API | 확인 포인트 |
|----------|------|----------|-------------|
| 1 | `/clients/needs-assessments` | `GET /api/v1/clients/needs-assessments/compliance` | `gapCount`·`gradeChangeReassessmentDue` |
| 2 | `/branches` (통합재가 지점) | `GET /api/v1/branches/integrated-home/provider-discovery` | `ltcAdminKindChoiceYn8=Y`·`06/07` 코드 |
| 3 | `/staff/training-logs` | `GET /api/v1/staff/training-logs/compliance` | 반기/연간 미이수 건수 |
| 4 | `/billing/easy-pay` | `GET /api/v1/billing/easy-pay/claims/{claimId}/payment` | 전월 미입금 가드·요청 상태 |

### [TWR] 1-5. 미문서화 위험 Must 기능 추가 점검 (G17/G32/G42/G21)

아래 5개는 최근 구현이 누적되어 현장 인수 시 누락되기 쉬운 Must 기능입니다.

| 구분 | 화면(프론트) | 핵심 API(백엔드) | 운영 확인 포인트 |
|------|--------------|------------------|------------------|
| 기능회복훈련 (G17) | `/programs/functional-recovery` | `GET/POST/PATCH /api/v1/programs/functional-recovery/plans` · `.../records` · `GET .../compliance` | 계획 수립률·30일 내 시작·월 1회 이상 급여제공 기록 |
| 사례관리 (G32) | `/case-management/meetings` | `GET/POST/PATCH /api/v1/case-management/meetings` · `GET .../compliance` | 회의/평가 누락, 참석자별 의견 누락, 회의 결과 반영 누락 |
| 민원상담 (G42) | `/staff/grievance-counselings` | `GET/POST/PATCH /api/v1/staff/grievance-counselings` · `POST .../submit` · `POST .../approve` · `POST .../follow-up` | 결재 대기 건수, 승인 후 60일 내 사후관리 준수율 |
| 방문요양 NHIS 비교 (G21) | `/visits` (batch-confirm 모달) | `GET /api/v1/visits/confirm-readiness` · `GET /api/v1/visits/nhis-comparison` · `POST /api/v1/visits/batch-confirm` | 동일 월 비교 여부, PLAN/BILLING 분리 readiness, 확인 체크 후 일괄확정 |
| 청구 생성 가드 | `/dashboard`, `/dashboard/hq` | `GET /api/v1/dashboard/branch` · `GET /api/v1/dashboard/hq` | `claimGenerationGuardBlocked=true` 시 전월 미납 해결 전 신규 청구 생성 금지 |
| 공단 요양보호사 일괄 요청 (G-STAFF-NHIS-EXCEL-IMPORT) | `/staff` | `POST /api/v1/staff/imports/nhis-caregivers/preview` · `POST …/nhis-caregivers` | 미리보기 `APPLIED` 행 체크·선택 등록·`onImported` refresh · 빈 선택 `422` (Q573·Q576) |
| 은행 입금 형식·dry-run (G-BANK-EXCEL-8) | `/billing/payments` | `GET /api/v1/billing/imports/bank-deposits/formats` · `POST …/preview` · `POST …/bank-deposits` | **「미리보기」→ `APPLIED` 체크→「선택 행 등록」** · 8종 은행 헤더 (Q572·Q576) |
| 직원 휴직 lifecycle (G-STAFF-LEAVE-STATUS) | `/staff` · `/staff/{userId}` | `GET /api/v1/staff/lifecycle-summary` · `PATCH /api/v1/users/{userId}` | **`StaffLifecycleSummaryPanel`** `onLeaveCount` · **`StaffLifecyclePanel`** 「휴직」·복직 (Q584) |
| 입금·수납 대장 반월·이중기준 (G-BILLING) | `/billing/reports/deposits` · `/receipts` | `GET /api/v1/billing/reports/deposits?period=` · `GET …/receipts?basis=` | **`BillingReportPage`** **「입금 구간」**·**「집계 기준」** · **「적용 조건:」** summary · 응답 **`appliedFilters`** (Q585·Q587·Q588) |
| 방문요양 NHIS 불일치 대시보드 (G21) | `/dashboard` · `/dashboard/hq` | `GET /api/v1/dashboard/branch` · `GET /api/v1/dashboard/hq` | **`nhisComparisonGapCount`** · **「공단 일정 불일치」** StatCard · home-visit-like 지점만 (`0796821`/`fe7df60`, Q594) |
| 카카오 API 잔여 대시보드 (G15) | `/dashboard/hq` · `/dashboard` | `GET /api/v1/transport/kakao-api-status` | **`hq_admin`·`sysadmin`** **「카카오 API 잔여」** StatCard · **`/settings` 링크** (`580a86b`, Q595) |
| 목욕 일정 전월 복사 (G-BATHING) | `/care/bathing-schedules` | `POST /api/v1/care/bathing-schedules/copy-from-previous-month` | **「전월 일정 복사」** · `SCHEDULED`/`COMPLETED`만 · `createdCount`/`skippedCount` (`9a957fb`, Q598) |
| 미납 독려·조정 (G-BILLING-OVERDUE-ADJUSTMENT) | `/billing/overdue` | `GET/POST …/overdue/claims/{claimId}/management-records` · `GET/POST …/adjustments` | **「관리」** Modal — 독려기록·조정처리 · SMS 자동기록 scope guard (`f6266ec`) · **V168** 빈 note/reason DB 거부 (`399c698`, Q605) · UXD-150 a11y (`751c593`, Q606) |
| 직원 서류관리 repository (G-STAFF-DOCUMENT-REPOSITORY) | `/staff/{userId}?tab=files` | `GET /api/v1/staff/hr-files/users/{userId}/repository-progress` | **FAQ21825 21슬롯** · **「모바일 촬영」** 전폭 버튼 (`6bde24a`/`9812ac4`, Q608·Q611) |
| **이용자 당일 출석 roster (G-ATTENDANCE-ROSTER-STATUS)** | `/attendance` · `/attendance/boarding` · `/attendance/on-site` | `GET /api/v1/attendance?transportMode=` | **활성 이용자 전원** · **`clientName`·`status`·`usesTransport`** · pending **`id=null`** · FE **`fetchAttendanceApi` 단일 호출** (`8383f8d`, Q609) |
| **직원 출퇴근 (G-STAFF-WORK-ATTENDANCE, 8-4)** | `/staff/attendance` | `GET /api/v1/staff/work-attendance` · `POST …/check-in` · `POST …/check-out` | **활성 직원 전원** · **출근 방식 `MANUAL`/`MOBILE`/`NFC`** · **수동 출근/퇴근** · **`BranchScopeNotice`**·**API `surfaceKind`·`relatedSurfaces` cross-link 패널** (Q651·Q653·Q657, `83a26e7`/`949e9bf`) · **당일만** (`5fd468b`/`a6eb8b7`, Q612) |
| **선행입금 입금 순서 (G-BILLING-DEPOSIT-ORDER-GUARD)** | `/billing/payments` | `POST /api/v1/billing/claims/{claimId}/payments` · `POST …/imports/bank-deposits` | **이전 미납 청구 선행** · 은행 import **가장 이른 월 우선** (`a6eb8b7`, Q614) |
| **청구 대장 필터 저장 (G-BILLING-REPORT-FILTER-PERSISTENCE, Q621)** | `/billing/reports/deposits` · `/receipts` · … | `GET/PUT /api/v1/billing/reports/filters` | **마운트 시 hydrate** · **「조회」PUT persist** · **4-variant** (`77b1ea8`, Q621) |
| **월별 출석 통계 (G-ATTENDANCE-STATS, US-E05)** | `/attendance/stats` | `GET /api/v1/attendance/stats/monthly?from=&to=&branchId=` | **지점·월 집계** BE+FE ✅ (`dffd726`, Q615) — StatCard·6개월 추이·다지점 표 |
| **지점 QR 생성 (US-E03, Q624)** | `/attendance/qr/generate` | `POST /api/v1/branches/{branchId}/qr` | **`qrToken` → PNG preview** · **「이미지 저장」**·인쇄 (`250619e`, Q624) |
| **이용자 상세 출석 이력 (US-D03, Q628)** | `/clients/:id` **「출석」** 탭 | `GET /api/v1/clients/{id}/attendance?from=&to=` | **`fetchClientAttendanceHistoryApi`** · 날짜·상태·입소·귀가·결석 사유 (`d058e43`, Q628) |
| **공단 평가지표 cross-walk legend (G30-LEGEND, Q629)** | `/compliance/monitoring` | `GET /api/v1/compliance/monitoring/items` (템플릿) | **`MonitoringOfficialIndicatorLegendPanel`** — ogada 15문항 ↔ 공단 1~15 매핑 · **#6↔15** · **#15↔12-14** (`fdc135b`, Q629) |
| **운영주기별 워크플로 카탈로그 (G34-WORKFLOW-CATALOG, Q635)** | `/compliance/workflow-catalog` | *(FE 정적 cross-walk)* | **`EzcareWorkflowCatalogPanel`** — ezCare FAQ **21795–21828** 28건 · **16/28 ogada 인용** · 주기·인용 **FilterChips** (`9f110a5`, Q635) |
| **CMS 지점 등록 roster (G2, Q637·Q638·Q662)** | `/billing/cms` **등록 관리** · `/billing/payments` | `GET /api/v1/billing/cms/enrollments?branchId=&status=` | **이용자 미선택** 시 활성 지점 roster · **FilterChips**·**이용자 deep link** · **입금 화면 CMS 등록 열** · **`status` trim·uppercase API 방어** (`f1225b0`, Q662) |
| **직원 연차휴가 (G-STAFF-ANNUAL-LEAVE, US-R03e, Q639)** | `/staff/annual-leaves` | `GET /api/v1/staff/annual-leaves/roster?year=&branchId=` · `PUT …/users/{userId}` | **지점 roster** · **`BranchScopeNotice`**·**관련 화면 패널** — 출퇴근 링크·대장 cross-link **API AVAILABLE** (Q650·Q657·Q663) · **multi-branch activeBranch fallback** (Q656) · **정수·0~31·비고 30자 `422`** (Q641·Q642) · **V173 DB CHECK/FK** (Q645) |
| **연차·유급휴일 대장 (US-R01-c, Q663·Q665·Q666·Q667·Q668)** | `/staff/leave-ledger` | `GET /api/v1/staff/leave-ledger?year=&branchId=` · `POST …/users/{userId}` · `PUT …/entries/{entryId}` · `DELETE …/entries/{entryId}` | **건별 canonical ledger** · **V175 DB integrity** (Q668) · **`StaffLeaveLedgerPage`** CRUD · **`social_worker` 등록** · **`hq_admin` 조회만** (`426d63a`/`c4e6bcb`) |

---

## 2. 시작하기

### 2-1. 접속 환경

| 항목 | 권장 사양 |
|------|----------|
| 기기 | PC, 태블릿, 스마트폰 (반응형 웹) |
| 브라우저 | Chrome, Safari, Edge 최신 2버전 |
| 네트워크 | HTTPS 연결 (센터 Wi-Fi 또는 LTE) |
| 보호자 QR 스캔 | 스마트폰 카메라 또는 브라우저 QR 스캔 |

> **로딩 성능 (2026-06-07 FE-15)**: ogada는 React·차트 라이브러리를 **별도 파일**로 나눠 배포합니다. 첫 접속 시 여러 파일을 받을 수 있으나, 각 파일 크기가 작아져 **저사양 기기·모바일**에서 체감 속도가 개선됩니다 (FAQ Q138). 브라우저 캐시 이후 재방문은 더 빠릅니다.

### 2-2. 로그인

1. ogada 접속 URL을 브라우저에 입력합니다.
2. **로그인 화면**(`/`)에서 ogada 브랜드 카드 안에 **이메일**과 **비밀번호**를 입력합니다.
3. **로그인** 버튼을 누르면 역할에 맞는 **홈 화면**으로 이동합니다.

> **현재 UI 상태 (FE `949e9bf`)**: **110 route · 89 page** · **`/staff/annual-leaves`** — **연차 roster**·**`BranchScopeNotice`**·**관련 화면 패널(출퇴근·대장)** (Q650·Q657) · **`/staff/attendance`** — **출퇴근 roster**·**`BranchScopeNotice`**·**API 메타 기반 역방향 패널(연차휴가·대장)** (Q651·Q653·Q657) · **`/billing/cms`** — **지점 CMS roster**·**FilterChips**·**`?clientId=` deep link** (Q637·Q638) · **`/compliance/workflow-catalog`** — **ezCare FAQ cross-walk** (G34, Q635)

> **로그아웃 방법**: AppShell **로그아웃** 버튼 · **브라우저 탭 종료** · 다른 탭에서 로그아웃 시 refresh token 폐기.

> **세션 유지 (Q396, SEC-005 예외)**: **같은 탭**에서 페이지 **새로고침·뒤로가기** 후에도 **`restoreSession()`** 이 refresh token(`sessionStorage`)으로 access token을 재발급해 **로그인 상태를 복원**합니다. **탭을 닫으면** refresh token이 사라져 **다시 로그인**해야 합니다. access token은 **메모리 전용** — localStorage에는 저장하지 않습니다.

> **로그인 시도 제한**: 짧은 시간에 반복 로그인·비밀번호 재설정 요청 시 `429 RATE_LIMITED`(「요청이 너무 많습니다. 잠시 후 다시 시도해주세요.」)가 반환될 수 있습니다. 1분 후 재시도하세요.

| 역할 | 로그인 후 홈 |
|------|-------------|
| 통합 관리자 (`hq_admin`) | `/dashboard/hq` 통합 대시보드 |
| 센터장 (`branch_admin`) | `/dashboard` 지점 대시보드 |
| 요양보호사 (`caregiver`) | `/dashboard` 지점 대시보드 |
| 사회복지사 (`social_worker`) | `/dashboard` 지점 대시보드 |
| 보호자 (`guardian`) | `/guardian` 보호자 포털 |

4. **페이지를 새로고침하면** **같은 탭**에서는 **`restoreSession()`** 으로 로그인이 **유지**됩니다 (FAQ **Q396**). **탭을 닫거나** 로그아웃하면 refresh token이 제거되어 **다시 로그인**해야 합니다. 공용 PC 사용 후에는 **로그아웃**하거나 **탭을 닫**으세요.

### 2-3. 비밀번호 재설정

비밀번호를 잊은 경우 **센터 `hq_admin`·`branch_admin`**에게 계정 확인을 요청하거나, IT 담당이 재설정 API를 호출합니다.

> **UI (FE `75fc91e`, SEC-D17)**: 로그인 화면 **「재설정 요청」**·`/settings` **보안** 탭에서 **`POST /auth/password/reset-request`**(Q126)와 **`POST /auth/change-password`**(Q122)가 모두 동작합니다. `mustChangePassword` true 시 로그인 직후 **`PasswordChangeModal`** 이 필수로 표시됩니다.
>
> | API | 용도 |
> |-----|------|
> | `POST /api/v1/auth/password/reset-request` | 등록 이메일로 재설정 링크 발송 |
> | `POST /api/v1/auth/password/reset` | 토큰으로 새 비밀번호 설정 |
> | `POST /api/v1/auth/change-password` | 로그인 중 새 비밀번호 설정 (**Fixed**, Q122) |

> **재설정 완료 후**: 비밀번호 변경이 완료되면 **기존 로그인 세션(refresh 토큰)이 모두 무효화**됩니다. 다른 기기·브라우저에서 사용 중이었다면 **새 비밀번호로 다시 로그인**해야 합니다.

### 2-4. 지점 선택 (다지점 센터장)

2곳 이상 지점을 관리하는 센터장은 화면 상단 **지점 선택기(Branch Switcher)**로 작업 지점을 바꿉니다.

1. 지점 선택기를 클릭합니다.
2. 작업할 지점(예: 「○○점」, 「△△점」)을 선택합니다.
3. 선택이 적용되면 이용자·출석·건강·대시보드가 **해당 지점 데이터만** 표시됩니다.

> **주의**: 다른 지점의 데이터는 조회·수정할 수 없습니다. 지점을 바꾼 뒤 작업 대상이 맞는지 항상 확인하세요.

> **표시 (FE `a627c6d`)**: `AppShell` 상단 **BranchSwitcher**가 모든 Must 화면에 표시됩니다. `branches` prop 미전달 시 JWT `branchIds`를 UUID 라벨로 폴백할 수 있습니다 (FAQ Q89). 지점 전환 API(`POST /auth/active-branch`)는 정상입니다.

---

## 3. 화면 구성 (공통)

### 3-1. 주요 메뉴 (`navConfig.js`, v1.2 P0 SideNav)

역할에 따라 **AppShell 좌측 2단 SideNav**(운영·출석·기록·청구·**이동**)가 표시됩니다 (FAQ Q84·Q149·Q159).

> **SideNav 준수 지표 라벨 (Q553, FE `acc5933`)**: 대시보드 StatCard와 구분하기 위해 SideNav 항목명에 **준수 지표 코드**가 붙습니다 — **운영 → 「모니터링 자가진단 (G30)」** · **「운영주기별 워크플로 (G34)」** · **기록 → 「급여제공결과 평가 (G39)」**. 화면 URL·기능은 **`/compliance/monitoring`** · **`/compliance/workflow-catalog`** · **`/programs/provision-result-evaluations`** 그대로입니다.

> **그룹 토글 (US-UX-05 Fixed, FE `1e111be`·`edfba7f`·`3845f0c`, Q331)**: **운영·이동·출석·기록·청구** 5개 그룹명을 클릭하면 하위 메뉴가 **접히거나 펼쳐집니다**.
> - **그룹 헤더 클릭** → 해당 그룹 하위 메뉴 표시/숨김 (`aria-expanded`·`aria-controls`)
> - **초기 상태**: 모든 그룹 **접혀 있음** — **현재 route가 속한 부모 그룹만** 자동 펼침 (예: `/clients` → **운영**만 펼침)
> - **route 변경 시** 활성 그룹 펼침 상태 **재계산** — 사용자가 **수동으로 펼친 다른 그룹은 유지** (`edfba7f`)
> - **세션 유지 (`3845f0c`)**: **`sessionStorage`** 키 **`ogada:sidenav-expanded:{role}`** — **탭을 닫기 전까지** 수동 펼침 상태 **복원** (페이지 remount·새로고침 시 JWT는 소멸하나 SideNav 펼침은 세션 동안 유지)
> - **다중 펼침 허용**: 여러 그룹을 **동시에** 펼칠 수 있음 (한 그룹을 열어도 다른 그룹이 자동으로 닫히지 않음)
> - **모바일·PC 동일** · **`SideNav.test`** · FAQ **Q331** · **UXD-132 (`f8321c7`, Q476)**: 그룹 토글 **`aria-label`「{그룹명} 메뉴 그룹, N개 항목」** · 현재 route가 속한 그룹 **`ds-sidenav__group--active` accent** · 항목 수는 **`aria-hidden` badge** 로 시각 표시

| 그룹 | 주요 항목 | `branch_admin` | `hq_admin` | `staff` | `guardian` |
|------|----------|:--------------:|:----------:|:-------:|:----------:|
| **운영** | 대시보드·지점·이용자·**급여계획 통보 (G38)**·**모니터링 자가진단 (G30)**·**운영주기별 워크플로 (G34)**·**정기욕구평가 현황 (G40b)**·보호자·**직원** | ✅ | ✅ | ✅(G38·G30·G34·G40b·보호자 제외) | 포털만 |

> **직원 모듈 in-page 네비 (`StaffContextNav`, UXD-86·UXD-92)**: **직원 관리** · **연차휴가 (US-R03e G-STAFF-ANNUAL-LEAVE)** · **출퇴근 (8-4 G-STAFF-WORK-ATTENDANCE)** · **교육일지 (8-7 G41)** · **보수교육 (8-7-1)** · **건강검진 (8-10)** · **직원현황 리포트 (8-12 US-R02)** · **고충상담 (8-8 G42)** · **선임 업무수행일지** 9화면 상단에서 **서브 탭**으로 전환합니다 (Q639·Q612·Q321·Q294·Q296·Q305·Q308·`02cbd05`). **연차휴가**는 **`/staff/annual-leaves`** · **출퇴근**은 **`/staff/attendance`** · **교육일지**는 **`/staff/training-logs`** · **직원현황 리포트**는 **`/staff/reports/status`** · **고충상담**은 **`/staff/grievance-counselings`** · **건강검진**은 **`/staff/health-checkups`** · **보수교육**은 **`/staff/training`** · **선임 업무수행일지**는 **`/staff/lead-caregiver-log`** 로 직접 진입합니다.
| **출석** | 현황·**탑승(차량)**·**현장 출석**·수기 체크인·통계·QR | ✅ | ✅ | ✅ | — |
| **기록** | 건강·**요양급여 제공기록 (L02_M01)**·**집중배설관찰 (L02_M02)**·**목욕 일정·제공현황 (L02_M03)**·**통합식사도움기록 (L02_M13)**·**간호급여 제공기록 (L02_M14)**·**병의원 진료내역 리포트 (L03_M09)**·**투약제공 리포트 (L03_M10)**·**요양급여 특이사항 (L02_M15)**·**식사 선호도 조사 (L02_M16)**·**신체제재 기록 (L02_M07)**·**요양/식사/화장실 리포트 (L02_M04)**·**목욕도움 리포트 (L02_M05)**·**체위변경 리포트 (L02_M06)**·**집중배설 리포트 (L02_M17)**·**수급자별 급여제공 리포트 (L02_M11)**·**급여제공 서비스 집계 (L02_M12)**·**식사**·**프로그램**·**기능회복훈련**·**급여제공결과 평가**·**방문 일정**·**사례관리 회의록**·**통합 바이탈 (L03_M11)**·**체중 기록 (L03_M14)**·**구강상태 점검 (L03_M13)**·**응급상황 기록 (L03_M04)**·**욕창 케어 (US-O03)**·**선임 업무수행일지** | ✅ | ✅ | ✅(사례관리 제외) | — |
| **청구** | 청구·NHIS·입금·미납·**간편결제**·CMS·**본인부담 통계 (G26)**·수가표·**청구/입금/수납/환불 대장**·**현금영수증 발급목록 (G-CASH-RECEIPT-LOG)** | ✅ | ✅ | — | — |

> **청구 리포트 in-page 네비 (`BillingReportsContextNav`, G26, Q379·Q380·Q530)**: **청구대장** · **입금대장** · **수납대장** · **현금영수증 발급목록** · **환불대장** · **본인부담 통계** · **간편계산기** 7화면 상단에서 **서브 탭**으로 전환합니다 — SideNav **청구 → 본인부담 통계**(`/billing/reports/statistics`)·**현금영수증 발급목록**(`/billing/cash-receipts`)와 병행합니다.
| **이동** | **배차·이동경로** · **수칙·계약 (G15)** · **차량 관리** · **이동서비스비 청구** · **외출 관리** · **외출 리포트** (`/transport`, `/transport/compliance`, `/transport/vehicles`, `/transport/service-fees`, `/transport/outings`, `/reports/client-outings`) | ✅ | ✅ | ✅ | — |

> **기록 모듈 in-page 네비 (`RecordsContextNav`, UXD-75)**: 건강·식사·프로그램·**기능회복훈련**·**급여제공결과 평가**·방문 일정·**사례관리 회의록**·**선임 업무수행일지** 8화면 상단에서 **서브 탭**으로 전환합니다 — SideNav **기록** 그룹과 병행 (Q248·Q262·Q263·Q276·**Q284**). **선임 업무수행일지**는 **`/staff/lead-caregiver-log`** 로 직접 진입합니다 (G34, `6d6b426`).

> **L02↔L03 care nav (`careLeafParity.js`·`navConfig.js`, BNK-262/273, Q378·Q386)**: SideNav **기록** 그룹에서 케어포 demo **2-x ↔ 3-x** parity를 지원합니다.
>
> | SideNav 라벨 | pamcode | 경로 | 비고 |
> |-------------|---------|------|------|
> | **간호급여 제공기록 (L03_M01)** | L03_M01 | **`/nursing/service`** | **입력** — 케어포 `view.nursing_service` (Q395: 중복 L02_M14 항목 제거 @ `5ebaade`) |
> | **통합 간호제공 리포트 (L02_M14)** | L02_M14 | **`/care/reports/nursing-service`** | **집계 리포트** — care-scoped API (`58ee122`) |
> | **병의원 진료내역 리포트 (L02·L03_M09)** | L03_M09 | **`/care/reports/hospital-visits`** | `medicalVisit=true` 필터 리포트 |
> | **투약제공 리포트 (L02·L03_M10)** | L03_M10 | **`/care/reports/medication-delivery`** | `medicationProvided=true` 필터 리포트 |
>
> 기존 **`/nursing/service/reports/*`** 경로도 유지됩니다 (FAQ Q350). 케어포 **2-8.건강상태 평가 리포트(삭제예정)**(L02_M09)는 ogada v1.2.1 **Won't** — **`/health` 건강 기록**으로 대체합니다.

> **간호급여 in-page 네비 (`NursingContextNav`, L03_M11~M04·US-O03)**: **통합 바이탈** · **체중 기록** · **구강상태 점검** · **응급상황 기록** · **위험평가** · **예방계획** · **간호 기록** · **분기 리포트** **8화면** 상단에서 **서브 탭**으로 전환합니다 — SideNav **기록 → 통합 바이탈 (L03_M11)** · **체중 기록 (L03_M14)** · **구강상태 점검 (L03_M13)** · **응급상황 기록 (L03_M04)** · **욕창 케어 (US-O03)** 와 병행 (Q340~Q346·Q336~Q339). **`aria-label="간호급여 하위 메뉴"`**. **`/nursing/pressure-ulcer`** 접속 시 **`/nursing/pressure-ulcer/assessment`** 로 자동 이동합니다.

> **이동 모듈 in-page 네비 (`TransportContextNav`, Q397)**: **배차·이동경로** · **수칙·계약** 2탭(「배차·이동경로」그룹)과 **차량·이동서비스비·외출·외출 리포트** 4탭(「이동서비스 운영」그룹)으로 전환합니다. SideNav **이동** 그룹에도 **「수칙·계약 (G15)」**(`/transport/compliance`)가 등록되어 있습니다 (`84e75ec`).

> **출석 모듈 in-page 네비 (`AttendanceContextNav`, UXD-73, Q242)**: 출석 현황·탑승·현장·수기 체크인·통계·QR 화면 상단에서 **서브 탭**으로 전환합니다 — SideNav를 다시 열 필요가 없습니다.

> **SideNav에 없는 Must 화면**: NHIS reconciliation·이용자 상세·청구 상세(`/billing/claims/:id`)·건강 추이(`/health/:clientId`)는 **목록 링크**로 진입.

> **API 경로 갭**: 지점·플랫폼·수가표·설정·QR·등록 폼 등 — FAQ **Q151**. **Recharts 차트**는 UXD-48에서 **연동 Fixed**(Q118). **출석 roster·status** — **BE Fixed** (Q609) · QR·통계 갭은 Q109·Q106.

### 3-2. UI 접근성 (2026-06-07 UXD 2·11·12차)

ogada 프론트는 WCAG 2.1 AA를 목표로 다음 패턴을 적용합니다. 상세 토큰·컴포넌트는 [`DESIGN_SYSTEM.md`](product/DESIGN_SYSTEM.md)를 참고하세요.

| 패턴 | 현장에서의 의미 |
|------|----------------|
| 키보드 포커스 링 | Tab 이동 시 버튼·링크 위치가 보입니다 |
| Modal ESC·**포커스 트랩** (UXD 12차) | 결석·체크아웃·세션 만료·NHIS 매칭 등 **모든 `Modal`**에서 Tab/Shift+Tab이 다이얼로그 **내부만** 순환합니다. ESC·배경 클릭으로 닫을 수 있습니다 |
| **`prefers-contrast`·`forced-colors`** (Q115·Q168) | Windows **고대비**·브라우저「색 대비 높임」설정 시 경계선·포커스 링이 강화됩니다. **배차 화면**(UXD-50) — 지도·정차 카드·마커·순번 Badge·강조 정차 **outline**도 동일 규칙 적용 |
| `role="alert"` | 출석·건강·청구 오류 메시지가 스크린리더에 즉시 전달됩니다 |
| 건강 수치 비정상 경고 (UXD-40, Q155) | `/health` **`VitalsRecordForm`** 입력 시 정상 범위를 벗어나면 **필드 아래 경고** — **저장은 가능** (`vitalsRanges.js` 단일 원천) |
| 주민번호 마스킹 | 기본 `******-*******`, **[열람]** 클릭 시에만 복호화 (감사 로그) |
| 터치 타깃 44px | 보호자·요양보호사 모바일 조작에 맞춘 버튼 크기 |
| **ThemeToggle** (Q114) | 상단 **라이트/다크** 전환 — 야간 근무·저조도 환경. `aria-pressed`·텍스트 라벨 병행 |
| **`Switch` 설정 토글** (Q116) | `/settings` **일반** 탭 — **이용자 셀프 QR 체크인 허용** on/off. Checkbox(동의)와 구분 — 즉시 적용 설정용 |
| **ds-* 레이아웃 유틸리티** (Q140) | `ds-form-row`·`ds-action-bar`·`ds-month-input` — 폼·목록 상단·월 선택 일관 레이아웃 (FE-16) |
| **정식 Modal·StatusBadge** (Q170) | 청구 확정·비밀번호 변경·플랫폼 Tenant 상세 등 — `window.confirm`·raw 상태코드 대신 **접근성 Modal·Badge** (UXD-51) |
| **`BranchScopeNotice`** (Q173·Q657) | 출석·출석 통계·QR 생성·배차·**연차휴가·직원 출퇴근** 화면 상단 **「조회 지점: ○○점」** — `role="status"` · `hq_admin`은 **BranchSwitcher** 전환 후 재조회 (UXD-53/54·US-R01 HR roster) |
| **보호자 명세 인쇄** (Q175) | `/guardian` **`GuardianBillingDetailModal`** — 표 `caption`·`scope=row`·본인부담금 행 텍스트+색 강조 · **「인쇄」** 시 명세만 출력 (`ds-statement-printing`, UXD-55) |
| **NHIS 대기 보류 안내** (Q181·Q182) | **`ReconciliationPage`** — 상단 **StatCard**(일치·차이·미매칭·대기) · **`NhisPendingReviewGuide`** 3단계 조치 · 표 **「보류 사유」**열 (UXD-58) |
| **`DateInput` 날짜 필드** (Q201·Q422·Q430, UXD-64) | **`DatePickerCalendar`** 달력 팝오버 — 이용자 등록(**생년월일 `viewAnchor`**)·수납일·**배차 운행일**·**가산율 제공일(G11)**·**이동계약 서명일(G15)**·건강·방문일정 등 — **`Field` + `DateInput`** (`ea5d896`/`ab4de83`/`7b8c7b9`) · **Esc·바깥 클릭** 닫기 · **키보드**: **←→↑↓**(±1일/±1주)·**Home/End**(주 시작/끝)·**PageUp/PageDown**(±1월) · **roving tabindex** — Tab으로 날짜 42개를 순회하지 않아도 됨 (Q430) · raw `<input type="date">` 금지 (Q281) |
| **`TimeInput` 시각 필드** (Q422, UXD) | 시·분 **Select** 드롭다운 — **배차 출발 시각**(`TransportRunNewPage`) · **일지 실제 픽업/하차** · 5분 단위 · **`pickerDate.js`** 단일 원천 |
| **`AttendanceContextNav`** (Q242, UXD-73) | 출석 6화면 상단 **서브 네비** — `aria-current="page"` 로 현재 탭 표시 · SideNav **출석** 그룹과 병행 |
| **`RecordsContextNav`** (UXD-75) | 건강·식사·프로그램·방문 4화면 상단 **서브 네비** — `aria-label="기록 관리 하위 메뉴"` · SideNav **기록** 그룹과 병행 |
| **`SideNav` collapsed a11y** (UXD-75) | 모바일에서 접힌 서브메뉴에 **`aria-hidden={!isOpen}`** — 스크린리더가 숨겨진 항목을 읽지 않음 |
| **`Field` 필수 입력 `aria-required`** (Q245, FE `1f71335`) | **`required` prop** 시 자식 입력에 **`aria-required="true"`** — 시각 `*`는 `aria-hidden` · **전 폼 일괄 적용** (WCAG 1.3.1·3.3.2) |
| **L02 care report table·StatCard a11y** (Q377·Q378, FE `25291b3`) | **L02_M11/M12/M17/M06** 리포트 4화면 — 표 **`captionVisuallyHidden`** · StatCard 요약 **`role="group" aria-label`** — 스크린리더 표·요약 탐색 (WCAG 1.3.1) |
| **G21 청구반영 Badge a11y** (Q376, FE `25291b3`) | **`/visits`** — Badge **텍스트 라벨**(청구반영·미반영·페어 없음) 병행 · Alert에서 **색상만 설명 제거** · **`ds-badge--dark` forced-colors outline** (WCAG 1.4.1·1.4.11) |

### 3-3. 이용자 상세 (`/clients/:id`)

목록에서 이용자를 클릭하면 **`ClientDetailPage`**로 이동합니다 (FE `a627c6d`).

| 영역 | 화면 | 백엔드 API |
|------|------|-----------|
| **계약→청구 lifecycle (FAQ21824, Q312)** | **「기본정보」** 탭 상단 — **`ClientFaq21824LifecyclePanel`** — 4단 checklist·관련 화면 링크 | G14·G38·방문·청구·출석 API **병렬 조회** (`58256c6`) |
| 기본 정보 | 이용자 ID·등급·**보호자 연결 상태** (`guardianLinkStatus`) | `GET /api/v1/clients/{id}` |
| **기초평가 (US-T09, G24)** | **「기초평가」** 탭 — **`ClientNeedsAssessmentPanel`** — 8항목 욕구사정·이전 연도 비교 | **`GET/PUT /clients/{id}/needs-assessments*`** (Q286) |
| **위험도평가 (US-T11/T12, G40·G40b)** | **「위험도평가」** 탭 — **`ClientRiskAssessmentPanel`**(신규입소) + **`ClientPeriodicRiskAssessmentPanel`**(반기) — 3종·compliance StatCard | **`GET/PUT …/risk-assessments*`** (Q301) · **`GET/PUT …/periodic-risk-assessments*`** (Q302) |
| **급여계약 (US-T10, G14)** | **「급여계약」** 탭 — **`ClientBenefitContractPanel`** — lifecycle 안내·**계약서 PDF/PNG 파일함** | **`GET/POST/DELETE …/benefit-contract-attachments*`** (Q285) |
| **급여계획서 (US-T08b, G14-NHIS-PLAN-FORM)** | **「급여계획서」** 탭 — **`ClientCarePlanForm`** — NHIS **10항목** 연도별 저장 | **`GET/PUT /clients/{id}/care-plan-forms*`** (Q557, V164) |
| **등급 이력 (US-M01)** | **「등급 이력」** 탭 — **`GradeHistoryTimeline`** + **인정기간 첨부 (G37, Q274)** | **`GET /clients/{id}/ltc-grade-history`** · **`…/attachments*`** |
| **보호자 초대 (US-J01)** | 이메일·관계 입력 → **초대 발송** · **`GuardianInvitationList`**(재발송·취소) | `POST/GET …/guardians/invitations` |
| **보호자 알림 이력 (US-J03-h)** | **「보호자 알림 이력 (US-J03)」** 카드 — **`NotificationHistoryPanel`** (발송 시각·채널·유형·상태) | **`GET /clients/{id}/notifications`** (Q152·Q187) |
| **외출 (G15 2-1-1, Q240)** | **「외출」** 탭 — **`ClientOutingPanel`** (예정 등록·출발·복귀·취소) | **`GET/POST/PATCH /clients/{id}/outings*`** |
| **급여제공 (G15 3-1, Q243)** | **「급여제공」** 탭 — **`CareProvisionRecordPanel`** (월간 출석·이동서비스·차량번호 대조) | **`GET /clients/{id}/care-provision-records/{yearMonth}`** |
| **건강·출석** | **「건강」·「출석」** 탭 — 건강 요약·**출석 이력 테이블** (상세 입력은 `/health`·`/attendance` 메뉴) | `GET /clients/{id}/health` · **`GET /clients/{id}/attendance`** (Q628) |
| **청구·연말정산 (G26, Q252)** | **「청구」** 탭 — 청구 이력 + **`MedicalExpenseDeductionPanel`** (귀속 연도별 **PAID** 납입 집계·인쇄·CSV) | **`GET /clients/{id}/medical-expense-deduction?taxYear=`** |

#### FAQ21824 계약→청구 lifecycle (BNK-165 Fixed · Q312)

이지케어 [**FAQ 21824**](https://ezcare.easyms.co.kr/help/faq.ez?rowid=21824&type=web) **재가 수급자 4단 업무흐름**을 **단일 wizard 없이** 이용자 상세에서 checklist로 확인합니다.

1. 이용자 목록에서 이름을 클릭해 **`/clients/:id`** 로 이동합니다.
2. 기본 탭 **「기본정보」** 상단 **「계약→청구 업무흐름 (FAQ21824)」** 카드를 확인합니다.
3. **`LifecycleWorkflowPanel`** 4단 — **① 계약·안내문(G14)** · **② 공단등록·계획통보(G38)** · **③ 서비스·RFID 확인(G21/출석)** · **④ 월말 청구·수납(7-x)** — 각 단계 **상태 Badge**·설명·증빙 모듈을 표시합니다.
4. 미완료 단계가 있으면 warning **「미완료 단계 N건 — 아래 연결 화면에서 이어서 처리하세요.」** 가 표시됩니다.
5. 하단 **바로가기** 링크 — **급여계약 탭(G14)** · **등급 이력(G37)** · **급여계획 통보** · **방문일정** · **청구** — 로 해당 화면으로 이동합니다.
6. **④ 월말 청구** 단계는 **전월 미입금·G33 미정산** 시 **`claimGuardBlocked`** 로 **OVERDUE** 표시 — **`/billing`** **ClaimGenerationGuardBanner**(Q310)와 연동됩니다.

> **P2 잔여**: FAQ21824 **단일 wizard UI** · RFID↔공단계획 **자동 대조(P2)** · **9종 안내문 일괄 출력** — REQUIREMENTS FAQ21824 Epic.

#### 기초평가 탭 (US-T09, G24 + G24b Fixed · FAQ21800)

1. 이용자 상세에서 **「기초평가」** 탭을 선택합니다.
2. 상단 **`LifecycleWorkflowPanel`** 에서 연간 욕구사정 단계(가정방문·8항목 기록·이전 연도 비교)를 확인합니다.
3. **가정방문 일자**와 **욕구사정 항목**을 **`ClientNeedsAssessmentForm`** 에 입력합니다.
   - **기본 8항목**(V84): 신체·인지·가족·경제·사회·서비스 필요·가정방문 대면 기록·만족도
   - **G24b 확장 5항목**(V128, Q354): **질병상태**·**의사소통**·**영양상태**·**환경상태**·**자원이용 욕구** — 이지케어 FAQ21800 **8-area parity**
4. **저장** — `PUT /api/v1/clients/{clientId}/needs-assessments` 로 **회계연도별 upsert** 됩니다. 동일 연도 기록이 있으면 갱신됩니다.
5. **이전 회계연도 비교** — 전년도 기록이 있으면 **`ClientNeedsAssessmentCompare`** 가 항목별 변화를 표시합니다. 변경 행에는 **「변경」** Badge가 붙고, 표에는 **`<caption>`**(스크린리더 전용)이 제공됩니다 (`8989bf4`).
6. **G24b 5항목**은 **`role="group"`** **`G24b 확장 5항목 (FAQ 21810)`** 로 묶여 스크린리더가 영역을 구분합니다 (`8989bf4`).
7. **회계연도·가정방문 일자** — FE **`4e4bdf6`·`479e064`** 에서 fiscal-year 파싱이 강화되어, 선택 연도와 가정방문 일자·비교 연도가 일관됩니다.
8. **가정방문 일자**는 해당 **회계연도(1/1~12/31)** 범위를 벗어나면 서버가 `422`(`가정방문 일자는 회계연도… 범위 내여야 합니다.`)로 거부합니다 (BE `b238779`).

> **권한**: **조회** — `hq_admin`·`branch_admin`·`social_worker`·`caregiver`. **작성·저장** — `branch_admin`·`social_worker`만. **G34b 불러오기**(Q303) 시 G24b 5항목도 업무수행일지 초안에 포함됩니다 (`45fb6d9`).
>
> **연간 compliance (Q355·Q356·Q357, BE `98002d4` / FE `ca0b627`/`b5af5fa`)**: **`GET /clients/needs-assessments/compliance?fiscalYear=&branchId=`** 로 지점별 **연간 욕구사정 미완료 인원**을 조회합니다. **`/dashboard`** StatCard 또는 SideNav **「연간 욕구사정 현황 (G24b)」** → **`/clients/needs-assessments`** 에서 **회계연도·필터·이용자별 gap 표**를 확인합니다. 기록은 이용자 상세 **「기초평가」** 탭에서 합니다.
>
> **P2 잔여**: FAQ21800 **연간 리포트 일괄 출력**.

#### [TWR] G24b/G19 Must 운영 체크 (센터장·사회복지사)

Must 운영에서 누락이 잦은 두 화면은 아래 순서로 점검하면 됩니다.

1. **연간 욕구사정 준수 점검(G24b)**: `/dashboard` → **연간 욕구사정 미준수 StatCard** → `/clients/needs-assessments`에서 회계연도·지점 필터 확인.
2. **미준수 이용자 보완 입력**: 목록에서 이용자 상세로 이동해 **「기초평가」** 탭에서 가정방문 일자 + 13항목(G24 8 + G24b 5) 저장.
3. **통합재가 기관 탐색(G19)**: `/branches` 지점 등록/수정에서 급여종을 `INTEGRATED_HOME`으로 선택하면 **`IntegratedHomeProviderDiscoveryPanel`** 이 표시됨.
4. **공단 포털 코드 확인**: 안내 패널의 `ltcAdminKindChoiceYn8=Y`, `searchAdminKindCd=06/07` 코드를 그대로 사용해 기관 검색.
5. **주의**: G19는 v1에서 자동 가산 계산/청구가 아니므로, 기관 등록 확인 후 월 가산(10만원/인)은 내부 절차에 따라 수동 검증.

#### 신규입소 위험도평가 탭 (US-T11, G40 Fixed · Q301)

**G24 욕구사정(지표20)** 과 별도로, 급여개시 전 **낙상·욕창·인지기능** 3종 스크리닝을 기록합니다.

1. 이용자 상세에서 **「위험도평가」** 탭을 선택합니다.
2. **`LifecycleWorkflowPanel`**에서 silverangel 지표21 **3종 스크리닝** 진행 단계를 확인합니다.
3. **StatCard** **「3종 위험도평가 완료 (N / 3)」** 로 완료 현황을 확인합니다.
4. **급여개시일(`ltcCertValidFrom`) 이전** 3종 평가가 미완료면 warning Alert가 표시됩니다.
5. 각 평가 유형(**낙상**·**욕창**·**인지기능**)에서 **「평가 등록」** 또는 **「수정」**을 클릭합니다.
6. **평가일**(필수)·**위험도 등급** `LOW`/`MODERATE`/`HIGH`(필수)·**척도 점수**(선택)·**특이사항**(선택)을 입력하고 **저장**합니다.
7. 저장 시 **`PUT /api/v1/clients/{clientId}/risk-assessments`**로 유형별 upsert 됩니다. 기존 기록이 있으면 갱신됩니다.

| 항목 | 내용 |
|------|------|
| 평가 3종 | 낙상(`FALL_RISK`) · 욕창(`PRESSURE_ULCER`) · 인지(`COGNITIVE_FUNCTION`) |
| 준수 | **`ltcCertValidFrom`(급여개시일) 이전** 3종 모두 **`assessedOn` 기록** |
| 지점 compliance API | **`GET /clients/admission-risk-assessments/compliance?branchId=`** — **`admissionComplete`**·`missingTypes[]` |

> **권한**: **조회** — `hq_admin`·`branch_admin`·`social_worker`·`caregiver`. **등록·수정** — `branch_admin`·`social_worker`만. FAQ **Q301** · ADMIN_GUIDE §6-2-7

> **대시보드**: **`/dashboard`**·**`/dashboard/hq`** 에 **「신규입소 위험도평가 미완료」** 위젯이 표시됩니다 — 급여개시일(`ltcCertValidFrom`) 설정 이용자 중 3종 미완료 **인원 수** · 1명 이상이면 **danger** 톤 · 클릭 시 **`/clients`** (Q301·`2f5af63`)

> **P2 잔여**: 급여개시 전 **알림**(push/이메일) (Q301)

#### 반기 기초평가 위험도 (US-T12, G40b Fixed · Q302)

**G40 신규입소(지표21)** 와 별도로, 급여 수급 중 이용자는 **반기 1회** 낙상·욕창·인지기능 위험도를 재평가합니다 (이지케어 FAQ21811·silverangel **지표16**).

1. 이용자 상세 **「위험도평가」** 탭 하단 **`ClientPeriodicRiskAssessmentPanel`** 에서 **현재 반기**(상/하반기) 라벨을 확인합니다.
2. **StatCard** **「반기 3종 위험도평가 완료 (N / 3)」** 로 해당 반기 완료 현황을 확인합니다.
3. 미완료 시 warning Alert — **`periodicComplete=false`** · **`missingTypes[]`** 표시.
4. 각 평가 유형에서 **「평가 등록」** 또는 **「수정」**을 클릭합니다 (스크린리더: **「낙상 위험도 반기 평가 등록」** 등 유형·반기 컨텍스트 **`aria-label`**, UXD-91).
5. **평가일**·**위험도 등급**·**척도 점수**·**특이사항**을 입력하고 **저장** — **`PUT /api/v1/clients/{clientId}/periodic-risk-assessments`** (`fiscalYear`·`fiscalHalf` query 포함).
6. **평가일**은 **`max(반기 시작일, 급여개시일)` ~ 반기 종료일** 범위여야 합니다. 급여개시일 미등록 이용자는 저장 불가.

| 항목 | 내용 |
|------|------|
| 평가 3종 | G40과 동일 — **`FALL_RISK`** · **`PRESSURE_ULCER`** · **`COGNITIVE_FUNCTION`** |
| 반기 | **`fiscalYear`**(2000~2100) · **`fiscalHalf`**(1=1~6월, 2=7~12월) — 유형·반기당 **1건** upsert |
| 준수 | 급여 수급 중 활성 이용자 · **해당 반기 윈도우 내 3종 완료** · **`periodicComplete`** |
| 지점 compliance | **`GET /clients/periodic-risk-assessments/compliance?fiscalYear=&fiscalHalf=&branchId=`** |

> **권한**: **조회·등록** — `hq_admin`·`branch_admin`·`social_worker`. **`caregiver`** — 조회만. FAQ **Q302** · ADMIN_GUIDE §6-2-8

> **정기욕구평가 현황 화면**: SideNav **운영 → 「정기욕구평가 현황 (G40b)」** (`/clients/periodic-risk-assessments`) — 이지케어 **2.2 정기욕구평가현황** 패리티. **회계연도·반기** 선택 · StatCard(대상·완료·미완료) · 미완료 이용자 표 · **「이용자 상세」** 링크로 **「위험도평가」** 탭 이동 (`7b68f54`).

> **대시보드**: **`/dashboard`**·**`/dashboard/hq`** — **「반기 기초평가 위험도 미완료」** StatCard — **`periodicRiskAssessmentGapCount`** — 현재 반기 3종 미완료 인원 · 클릭 **`/clients/periodic-risk-assessments`** (`22325f4`).

> **G40과 구분**: **G40** = 급여개시 **전** 1회(지표21) · **G40b** = **반기 1회** 재평가(지표16). 동일 **「위험도평가」** 탭에 **두 패널**이 표시됩니다.

> **P2 잔여**: G40/G40b **live API E2E run** (Q302)

#### 급여계약 탭 (US-T10, G14 Partial Fixed · FAQ21805)

1. 이용자 상세에서 **「급여계약」** 탭을 선택합니다.
2. **`LifecycleWorkflowPanel`** 과 **계약 이력 타임라인**에서 계약 단계(최초 계약·갱신·변경) 안내를 확인합니다 — **상태 전이 API는 P2**입니다.
3. **급여계약서 파일함** (`ClientBenefitContractAttachmentPanel`):
   - **`branch_admin`·`social_worker`·`hq_admin`**: **PDF** 또는 **PNG**(최대 **10MB**) 선택 → **업로드**.
   - **미리보기** — Modal에서 인라인 표시 · **삭제** — 확인 후 제거.
   - **`caregiver`**: 목록·미리보기 **조회만**(업로드·삭제 버튼 없음).
4. **「수급자 파일함 전체 보기」** 링크로 `/clients/{id}/files` 에 접근할 수 있습니다.

> **등급 이력과의 구분**: **「등급 이력」** 탭(G14/US-M01)은 **등급 변동·인정기간 첨부(G37)** 를, **「급여계약」** 탭(US-T10)은 **계약서 PDF/PNG 파일함**을 관리합니다. FAQ21805 **비정기 갱신·해지·전자서명** workflow는 P2 (Q285).

#### 급여계획서 탭 (US-T08b, G14-NHIS-PLAN-FORM Fixed · FAQ21802 · Q557)

케어포 **별지 제21호**·이지케어 [**FAQ 21802**](https://ezcare.easyms.co.kr/help/faq.ez?rowid=21802&type=web) **NHIS 10-field 급여제공계획서**를 이용자×**계획 연도**별로 구조화 저장합니다. **이용계획서 PDF**는 **「등급 이력」** 탭(G37) 첨부, **본 탭**은 **10항목 본문·통보 일시** 기록용입니다.

1. 이용자 상세 **「급여계획서」** 탭(또는 **`/clients/:id/care-plan-form`**)을 선택합니다.
2. **계획 연도**를 고릅니다 — 저장 이력이 있으면 **「저장된 연도: …」** 로 표시됩니다.
3. **10항목**을 입력합니다.

| 필드 | 필수 | 설명 |
|------|:----:|------|
| 급여종류 | ✅ | 주야간보호·방문요양·방문목욕·방문간호·단기보호·통합재가 |
| 수급자명 | — | 비우면 이용자 기본 이름이 **스냅샷**으로 저장 (개명 후에도 작성 시점 이름 보존) |
| 작성일 | ✅ | **계획 연도 1/1~12/31** 범위 — 벗어나면 `422` |
| 작성자 | ✅ | 작성 담당자 성명 |
| 세부목표·필요내용·세부제공내용·종합의견 | ✅ | 다줄 텍스트 |
| 횟수·시간 | ✅ | 서비스 빈도·1회 제공 시간 |
| 통보 일시 | — | 수급자·보호자 통지 시각 (미통지 시 비움) |

4. **저장** — `PUT /api/v1/clients/{clientId}/care-plan-forms` 로 **이용자×연도 1건** upsert 됩니다 (V164 UK).
5. SideNav **「급여계획 통보 (G38)」**(`/clients/care-plan-notifications`)에서 **5·11개월 milestone**·미반영 이용자를 확인하고, 목록 **「급여계획서」** 링크로 해당 이용자 탭으로 이동할 수 있습니다.

> **권한**: **조회** — `hq_admin`·`branch_admin`·`social_worker`·`caregiver`. **작성·저장** — `branch_admin`·`social_worker`만. **퇴소·비활성 이용자**는 **신규 작성** 불가(DB guard) — 기존 연도 **수정**은 가능.
>
> **G38 연계**: 통보 모니터링은 **G37 인정기간 첨부**·**본 탭 `notifiedAt`** 과 병행합니다. FAQ **Q277·Q557** · ADMIN_GUIDE §6-2-2·§6-2-2a.

#### 등급 이력 탭 (US-M01, G14 Fixed · G37 US-M01-g)

1. 이용자 상세에서 **「등급 이력」** 탭을 선택합니다.
2. **`GradeHistoryTimeline`**이 `GET /api/v1/clients/{clientId}/ltc-grade-history`를 호출해 **최신순** 이력을 표시합니다 (FE `6d0a03a`·`e026ae9`, BE `15e41e3`·`0325d95`).
3. 각 행: **이전 등급** → **변경 등급**, **변경 일시**, **사유**, **변경자**(표시명).
4. 이용자 등록 시 최초 등급·이후 `PATCH`로 등급 변경 시 **V48 트리거**가 자동으로 이력을 추가합니다 — 수동 중복 등록은 불필요합니다.
5. **인정기간 첨부 (G37, Q274)** — 각 이력 행 아래 **「인정기간 첨부 (N)」** 를 펼칩니다.
   - **`branch_admin`·`social_worker`**: **PDF** 또는 **PNG**(최대 **10MB**) 선택 → **「업로드」**.
   - 일부 브라우저는 MIME을 비우거나 `application/octet-stream`으로 보냅니다 — 이 경우 **파일명 `.pdf`/`.png` 확장자**로 형식을 판별합니다 (`12d3b7f`).
   - **모든 조회 역할**(`hq_admin` 포함): 첨부 목록·**「미리보기」** · **`caregiver`** 는 **조회만**(업로드·삭제 버튼 없음).
   - **「삭제」** — 업로드 권한 역할만. 삭제 전 확인 Modal이 표시됩니다.
6. API 오류(404 제외) 시 안내 메시지가 표시됩니다. Swagger로 동일 API를 확인할 수 있습니다 (FAQ Q176·Q274).

> **운영 참고**: 첨부 파일은 서버 디스크에 저장됩니다. 백업·용량은 IT(`sysadmin`)가 `DEPLOYMENT_GUIDE.md` §4-8을 따릅니다.

#### 출석 이력 탭 (US-D03, Q628 Fixed · `d058e43`)

이용자별 **일별 출석·결석 이력**을 조회합니다. 당일 입소·귀가·결석 **입력**은 **`/attendance`** 출석 관리에서 처리합니다 (Q609).

1. 이용자 상세 **`/clients/:id`** 에서 **「출석」** 탭을 선택합니다.
2. **`fetchClientAttendanceHistoryApi(clientId)`** 가 **`GET /api/v1/clients/{clientId}/attendance`** 를 호출합니다 (`apiFetch` · `services.js`).
3. **출석 이력** 테이블에 **날짜**·**상태**(`CHECKED_IN`/`CHECKED_OUT`/`ABSENT` 등) · **입소 시각** · **귀가 시각** · **결석 사유**가 표시됩니다.
4. 기록이 없으면 **「출석 기록 없음」** — **`/attendance`** 링크로 당일 체크인을 안내합니다.
5. API 오류 시 Alert가 표시됩니다. **`from`/`to`** 쿼리로 기간 필터가 가능합니다 (Swagger·FAQ Q628).

| 항목 | 내용 |
|------|------|
| BE API | **`GET /clients/{id}/attendance?from=YYYY-MM-DD&to=YYYY-MM-DD`** |
| RBAC | **`hq_admin`·`branch_admin`·`social_worker`·`caregiver`** |
| 당일 처리 | **`/attendance`** — roster·입소·귀가·결석 (G-ATTENDANCE-ROSTER-STATUS, Q609) |

> **307차 이전**: 존재하지 않는 `client.attendanceRecords` 필드를 읽어 **항상 빈 목록**이었습니다 — Q102·Q628 참고.

#### 보호자 초대 절차 (US-J01, v1.1)

1. 이용자 상세 **「보호자 초대」** 카드에서 **보호자 이메일**·**관계**(예: 자녀)를 입력합니다.
2. **초대 발송** — `channel: EMAIL` 고정 (Q145).
3. 초대 이력에서 **PENDING**·만료일·**재발송**·**취소**를 확인합니다.
4. 보호자가 메일 링크 → **§8-5 수락 화면** — 이름·**연락처**·비밀번호 입력 (연락처는 V44 알림 수신용, Q148).

> v1.1 초대 채널은 **이메일 단일**. 신규 등록은 SideNav **이용자 → 등록**(`/clients/new`) — **API 본문 불일치** 시 Swagger (Q113·Q151).

#### 급여제공 탭 (G15 v1.3-C, Q243 Fixed)

1. 이용자 상세 **「급여제공」** 탭을 선택합니다.
2. **대상 월**(`MonthInput`)을 고르고 **조회** — **`GET /api/v1/clients/{clientId}/care-provision-records/{yearMonth}`** 호출.
3. 상단 **월간 요약**: 출석 일수 · 이동서비스 제공 일수 · **주 사용 차량** · 이동서비스 이용 여부.
4. **일별 표**: 일자 · 출석 · 이동서비스 제공 · **차량번호** — **확정 배차**에 이용자가 포함되고 배차에 **`vehicleId`** 가 지정된 경우 번호판이 표시됩니다 (Q241).
5. **`usesTransport=false`** 이면 안내 Alert가 표시되고 이동서비스 제공 일수가 0일 수 있습니다.
6. 보호자 **이메일 발송**은 **Swagger** — §4-7-3 (Q216). 발송 시 본문에 **이동서비스 제공 여부·차량번호**가 자동 포함됩니다 (`8bdead6`).

> **권한**: API는 **`branch_admin`·`social_worker`·`caregiver`** — **`hq_admin`** 은 이 탭 API **403** 가능. 통합 관리자는 Swagger 또는 후속 RBAC 확장을 사용하세요.

#### 청구·연말정산 의료비공제 탭 (G26 / US-L04, Q252·Q254·Q255 Fixed)

1. 이용자 상세 **「청구」** 탭을 선택합니다.
2. 상단 **청구 이력** 카드에서 월별 청구 상태를 확인합니다.
3. 하단 **「연말정산 의료비공제 (G26)」** 카드 — **`MedicalExpenseDeductionPanel`**:
   - **귀속 연도**(2000~올해)를 입력합니다 — **입력 중에는 API가 호출되지 않습니다** (Q255).
   - **「조회」** 를 누르면 해당 연도 납입 내역을 불러옵니다.
   - **`PAID`** 이고 **입금일·입금수단**이 기록된 본인부담금 중 **`CASH`·`BANK_TRANSFER`만** 집계됩니다 — **`CMS`·`EASY_PAY`는 제외** (케어포 7-4·7-5, Q254). 패널 상단 **안내 문구**에도 동일 내용이 표시됩니다 (`c1d9788`).
   - **인쇄** — 연말정산 신고 참고용 납입증명 영역만 출력.
   - **CSV 다운로드** — UTF-8 BOM 파일 (청구월·금액·입금일·수단).
   - **국세청 엑셀 다운로드** — NTS 제출용 `.xlsx` (공제대상여부·CMS/간편결제 비고 열, Q258).
4. 해당 연도 **집계 대상** 납입이 없으면 **「납입 내역 없음」** 안내가 표시됩니다.

> **선행**: **현금·계좌이체** 입금 시 **입금일(`paidAt`)** 을 반드시 기록하세요 — 미기록 청구는 집계에서 제외됩니다 (Q250). **CMS 자동이체 수납분은 연말정산 의료비공제 대상이 아닙니다** (Q254). 보호자용 동일 기능은 §8-2 **「연말정산」** 탭.

---

## 4. 센터장 (`branch_admin`) 매뉴얼

센터장은 **소속 지점 1곳**(또는 다지점 권한 시 선택 지점)의 운영을 총괄합니다. 이용자 등록, 출석·건강 관리, 월말 청구, 지점 대시보드 확인이 주요 업무입니다.

### 4-1. 일과 개요

```
[오전] 대시보드 확인 → 출석 현황 점검 → (필요 시) 수기 체크인 보조
[낮]   이용자 등록·수정, 건강 이상 알림 확인
[귀가] 출석 퇴소 완료 여부 확인
[월말] 청구서 생성 → 공단 엑셀 import → 본인부담금 명세서 확정
```

### 4-2. 지점 대시보드 (`/dashboard`)

로그인 후 첫 화면입니다. **`DashboardWidgetGrid`**·**`HealthAlertList`**가 API 실데이터와 연동됩니다 (Q85·**Q177**).

| 영역 | 설명 |
|------|------|
| 운영 위젯 | 오늘 **입소**·**결석**·**미처리**·건강 알림·**미매칭 NHIS**·**NHIS 대기(보류)** 6종 + **home-visit-like 「공단 일정 불일치」** (Q594) + **`hq_admin`·`sysadmin` 「카카오 API 잔여」** (Q595) + **`hq_admin`·`branch_admin`·`social_worker` 전용 「사례관리 30일 미반영」** (`0821ce8`, Q263) · **「참석자별 의견 미기록」** (`b9e0947`·`e55ae96`, Q518) · **준수지표·청구·현금영수증·근로재계약** StatCard 등 (아래 각주) |
| 건강 이상 알림 | `healthAlerts[]` 목록 — 이용자명·이상 유형·기록 시각 (**지점 Badge 없음** — 단일 지점 스코프) |
| API | `GET /api/v1/dashboard/branch` — **`nhisComparisonGapCount`** (Q594, `0796821`) · **`nhisUnmatchedCount`·`pendingReviewCount`·`overdueCount`·`monthlyCapWarningCount`** (Q282) · **`cashReceiptPendingCount`·`cashReceiptOverdueCount`** (Q532) · **`claimGenerationGuardBlocked`·`unpaidPriorMonthClaimCount`** (Q571) · **G17/G32/G38/G39 준수지표 스냅샷** (Q280) — 도메인별 스냅샷 우선 · 누락 시 **`Promise.all` 병렬 폴백** (`f72da41`) |

> **공단 일정 불일치 위젯 (G21, Q594, BE `0796821`·FE `fe7df60`/`c01b880`/`ebc9f28`)**: **home-visit-like** 지점(`HOME_VISIT` 등) 또는 **통합 대시보드**에 **「공단 일정 불일치」** StatCard가 표시됩니다. **`nhisComparisonGapCount`** — 당월 PLAN vs NHIS import **불일치·누락·extra** 합계. 1건 이상 **danger** 톤. 클릭 **`/visits`**. **주야간-only** 지점 branch dashboard에서는 **숨김**. 구버전 API는 **`confirm-readiness` 폴백**.
>
> **카카오 API 잔여 위젯 (G15-KAKAO-QUOTA-DASH, Q595, FE `580a86b`)**: **`hq_admin`·`sysadmin`** 에 **「카카오 API 잔여」** StatCard — **`GET /transport/kakao-api-status`** · **500건 이하 warning** · 클릭 **`/settings`「카카오 API」** (Q554). ogada **in-memory 카운트** — 재기동 시 리셋.
>
> **NHIS 대기(보류) 위젯 (BNK-19, Q183)**: 1건 이상이면 **warning** 톤 StatCard. 클릭 시 `/billing/imports/nhis` — §4-6-1·Q181·Q182 참고.
>
> **사례관리 30일 미반영 위젯 (G32, Q263)**: `hq_admin`·`branch_admin`·`social_worker`에 표시. **`fetchCaseManagementComplianceApi`** 현재 분기 compliance에서 **회의록은 있으나 30일 이내 급여반영이 없는 이용자 수**를 집계합니다. 1명 이상이면 **danger** 톤. 클릭 시 **`/case-management/meetings`**.
>
> **참석자별 의견 미기록 위젯 (G32, FAQ21797, Q518, `b9e0947`·`e55ae96`)**: 동일 역할에 **「참석자별 의견 미기록」** StatCard가 표시됩니다. **현재 분기**에 회의록은 있으나 **참석자별 의견(`attendeeOpinionsMet`)이 미충족**인 이용자 수를 집계합니다. 1명 이상이면 **warning** 톤. 클릭 시 **`/case-management/meetings`** — §5-9에서 참석자별 의견을 보완합니다. 대시보드 응답에 **`caseManagementAttendeeOpinionGapCount`** 가 없으면 compliance API에서 **`countCaseManagementAttendeeOpinionGaps`** 로 **병렬 폴백**합니다.
>
> **사례관리 평가 위젯 (G32 지표29, Q266, UXD-79)**: 동일 역할에 **「사례관리 평가 미실시」**(gap 건수, warning) · **「사례관리 평가실시」**(충족/미충족/대상없음) 위젯이 추가되었습니다. **`evaluationConductedMet`** — 회의 후 30일 내 **기능회복훈련 출석** 또는 **계획 갱신** 여부입니다.
>
> **기능회복 지표27 위젯 (G17, Q271, BNK-101~102)**: **`hq_admin`·`branch_admin`·`social_worker`** 에 **「급여제공 시작일까지 계획 미충족」**·**「급여제공 시작일까지 계획」** gap·상태 위젯이 표시됩니다 (silverangel row3 verbatim). 1명 이상 미충족 시 **danger/warning** 톤. 클릭 시 **`/programs/functional-recovery`**.
>
> **급여제공결과 평가 지표44 위젯 (G39, Q276, BNK-107/109)**: 동일 역할에 **지표44 4-pillar gap 4종** — **「주간 상태변화 미기록」**·**「월간 기록지 미제공」**·**「급여제공결과 평가 미등록」**·**「평가 30일 미반영」** — 과 **상태 StatCard 4종**(**「주간 상태변화」**·**「월간 기록지 제공」**·**「급여제공결과 평가」**·**「평가 반영」**)이 표시됩니다 (`8e66ae8`). 1명 이상 미충족 시 **warning** 톤. 클릭 시 **`/programs/provision-result-evaluations`**.
>
> **급여계획 통보 지표 G38 위젯 (Q277, BNK-106)**: **`hq_admin`·`branch_admin`·`social_worker`** 에 **「급여 5개월 경과」**·**「급여 11개월 경과」**(warning) · **「이용계획서 재발급 미반영」**(danger) 위젯이 표시됩니다. 클릭 시 **`/clients/care-plan-notifications`**. compliance API만 실패하면 **「일부 준수지표를 불러오지 못했습니다: 급여계획 통보 모니터링」** warning Alert가 나타나고 나머지 위젯은 유지됩니다 (`4b2b082`).
>
> **신규입소 위험도평가 위젯 (G40, Q301, `2f5af63`)**: **`hq_admin`·`branch_admin`·`social_worker`** 에 **「신규입소 위험도평가 미완료」** 위젯이 표시됩니다. **`ltcCertValidFrom`(급여개시일)이 설정된 활성 이용자** 중 낙상·욕창·인지 3종 평가가 **급여개시일 이전에 완료되지 않은 인원 수**를 집계합니다. 1명 이상이면 **danger** 톤. 클릭 시 **`/clients`** — 해당 이용자 상세 **「위험도평가」** 탭에서 보완합니다. 대시보드 스냅샷에 **`admissionRiskAssessmentGapCount`** 가 없으면 **`GET /clients/admission-risk-assessments/compliance`** 로 **병렬 폴백**합니다. API 실패 시 **「일부 준수지표를 불러오지 못했습니다: 신규입소 위험도평가」** warning Alert.
>
> **반기 기초평가 위험도 위젯 (G40b, Q302, `22325f4`)**: 동일 역할에 **「반기 기초평가 위험도 미완료」** 위젯이 표시됩니다. **현재 반기**(상/하반기) 급여 수급 이용자 중 **낙상·욕창·인지 3종 재평가**가 미완료인 인원 수 — **`periodicRiskAssessmentGapCount`**. 1명 이상이면 **danger** 톤. 클릭 시 **`/clients/periodic-risk-assessments`** — **정기욕구평가 현황** 화면에서 회계연도·반기별 미완료 목록을 확인합니다. 스냅샷 누락 시 **`GET /clients/periodic-risk-assessments/compliance`** 병렬 폴백. API 실패 시 **「…반기 기초평가 위험도」** warning Alert.
>
> **연간 욕구사정 위젯 (G24b, Q355·Q356·Q357, `ca0b627`/`b5af5fa`)**: **`hq_admin`·`branch_admin`·`social_worker`** 에 **「연간 욕구사정 미완료」**·**「등급변경 재사정 필요」** StatCard 2종이 표시됩니다. 미완료 1명 이상 **danger** · 재사정 1명 이상 **warning**. 클릭 **`/clients/needs-assessments`** — 이용자별 gap 표에서 **「욕구사정」** 링크로 상세 **「기초평가」** 탭 보완. 스냅샷 누락 시 **`fetchNeedsAssessmentComplianceApi`** 병렬 폴백.
>
> **직원교육 미충족 위젯 (G41, Q461, `9e91e6a`)**: 동일 역할에 **「직원교육 미충족」** StatCard가 표시됩니다. **노인인권 상·하반기**·**운영규정 연간**·**G41b 3종 연간**·**신규 7일 오리엔테이션**·**FAQ21808 주제** 중 미충족 항목 수를 **`countStaffTrainingComplianceGaps`** 로 집계합니다. 1건 이상이면 **danger** 톤. 클릭 **`/staff/training-logs`**. 대시보드 스냅샷에 **`staffTrainingComplianceGapCount`** 가 없으면 **`GET /staff/training-logs/compliance`** 로 **병렬 폴백**합니다. API 실패 시 **「일부 준수지표를 불러오지 못했습니다: 직원교육 준수」** warning Alert.
>
> **근로재계약 미충족 위젯 (FAQ21823, US-R03, Q540, FE `f31c346`)**: **`hq_admin`·`branch_admin`** 에 **「근로재계약 미충족」** StatCard가 표시됩니다. **재직·입사 진행** 직원 중 **재계약 기한 초과** 또는 **근로계약서 서명일 미등록** 인원 수를 **`countEmploymentContractRenewalGaps`** 로 집계합니다. 1명 이상이면 **warning** 톤. 클릭 시 **`/staff`** — §5-3 **FAQ21823 목록 집계**에서 상세를 확인합니다. 대시보드 스냅샷에 **`employmentContractRenewalGapCount`** 가 없으면 **`GET /users`**(페이지 0·size 200)로 **병렬 폴백**합니다. API 실패 시 **「일부 준수지표를 불러오지 못했습니다: 근로재계약 준수」** warning Alert.
>
> **근로(재)계약 갱신 알림 목록 (FAQ21823, US-R03, Q547·Q552, FE `033b319`/`bd6e1c2`)**: StatCard 아래 **`EmploymentContractRenewalAlertsPanel`** (**「근로(재)계약 갱신 알림 (FAQ 21823)」**) 이 **1건 이상** 있을 때 표시됩니다. **`computeEmploymentContractRenewalDueAlerts`** 로 **기한 초과(overdue)** · **서명일 미등록(missing)** · **기한 임박(due-soon, 30일 이내)** 직원을 나열합니다. **재계약 기한**은 **`<time dateTime>`** 으로 읽히며, 직원명 링크는 **`/staff/{userId}?tab=lifecycle`** (**`aria-label`「{이름} 근로(재)계약 lifecycle 보기」**, Q552). Badge 톤: **기한 초과=warning** · **서명일 미등록=danger** · **기한 임박=info**.
>
> **현금영수증 미발급·발급 지연 위젯 (G-CASH-RECEIPT-LOG, FAQ21716, Q532, BE `fe54af8`·FE `221458e`)**: **`hq_admin`·`branch_admin`** 에 **「현금영수증 미발급」**·**「현금영수증 발급 지연」** StatCard 2종이 표시됩니다. **`PAID`+`CASH`** 수납 중 **NTS 발급 이력이 없는 건수**(`cashReceiptPendingCount`)와 **수납일+7일 SLA 초과** 건수(`cashReceiptOverdueCount`)를 집계합니다. 미발급 1건 이상 **warning** · 지연 1건 이상 **danger** 톤. 클릭 시 **`/billing/cash-receipts`** — §5-10-1에서 발급 등록을 진행합니다. 통합 대시보드(`/dashboard/hq`)는 **전 지점 합산**입니다.
>
> **청구 생성 제한 위젯 (G-BILLING-PRIOR-DEPOSIT-GUARD, Q571, BE `80b9619`·FE `d723d5a`)**: **`hq_admin`·`branch_admin`** 에 **「청구 생성 제한 (7-1 선행입금 가드)」** StatCard가 표시됩니다. 대시보드 응답 **`claimGenerationGuardBlocked=true`** 이면 **전월 미입금 청구 건수**(`unpaidPriorMonthClaimCount`)를 **danger** 톤으로 표시합니다. 차단이 없으면 **0건·default** 톤입니다. 클릭 시 **`/billing/payments`** — 전월 **`CONFIRMED`** 청구에 **입금일(`paidAt`)** 을 입력해 선행입금을 완료하세요. **`/billing`** 화면의 **`ClaimGenerationGuardBanner`**·**`GET /billing/claims/generation-guard`** 와 **동일 규칙**입니다 (Q310). **G33 도입 전 미납(청구시작 기준금액)** 미정산도 생성을 막을 수 있습니다 — §5-5-1·§5-10 참고.
>
> **미납 본인부담 위젯 (US-L02, Q202)**: `branch_admin`·`hq_admin`만 표시. 1건 이상이면 **danger** 톤. 클릭 시 **`/billing/overdue`**. 당월 이전 확정·미수납 건수와 동일합니다 (Q197).
>
> **Recharts (UXD-48)**: 대시보드 하단 **월별 출석률 추이**(`AttendanceRateChart`, US-H01)가 `monthlyAttendanceRates[]` 데이터로 표시됩니다 (US-M02 nested 매핑, Q177·Q118). 데이터가 없으면 「월별 출석률 데이터가 아직 없습니다」 안내가 나타납니다.

### 4-3. 이용자 관리 (`/clients`)

#### 이용자 목록·상세 (BNK-19 + BE `a49e496` + FE `0baabe9`)

1. **이용자** 메뉴 → 목록(`/clients`) — `GET /api/v1/clients` — **10열 Table**: 이름·나이·성별·지역·등급·**배차 이용**·인정번호·**연락처**·보호자·**보호자 연락처** (Q191·**Q417**, 결정 96).
2. 상단 **검색** — 이용자명·**지역**·**보호자명**·**연락처(`phoneMasked`)**·인정번호·성별 필터.
3. **연락처**·**보호자 연락처** 열은 **`MaskedPhone`** 컴포넌트로 **마스킹 표시**만 합니다 — 전체 번호·통화 링크는 **노출하지 않습니다** (PII 보호). 목록·상세의 비링크 `span`은 **화면에 보이는 마스킹 문자열**이 스크린리더 접근 이름이며, **중복 `aria-label`은 사용하지 않습니다** (`05535a4`, Q420).
4. 이름 링크 → **이용자 상세**(`/clients/:id`) — 기본 정보 **연락처(`phoneMasked`)**·**보호자 초대**(§3-3).
5. **거주지·픽업 주소** — **`hq_admin`·`platform_admin`·`sysadmin`** 만 **전체 주소**를 봅니다. **센터장·사회복지사·요양보호사** 등은 **시·구·도로명(동)까지** 표시되고 **상세 번호는 `***`** 로 마스킹됩니다 — 배차 roster와 **동일 정책** (`c4e6bcb`, Q669·SEC-D9).

#### 연간 욕구사정 현황 (G24b, US-T09 · Q357)

SideNav **이용자 → 「연간 욕구사정 현황 (G24b)」** 또는 대시보드 **「연간 욕구사정 미완료」**·**「등급변경 재사정 필요」** StatCard 클릭 → **`/clients/needs-assessments`**.

1. **회계연도**(2000~2100)를 입력합니다. 기본값은 **현재 연도**입니다.
2. StatCard — **전체 이용자**·**연간 완료 (FAQ 21800)**·**연간 미완료 (FAQ 21800)**·**등급변경 재사정 필요 (FAQ 21810)** 인원을 확인합니다 (`d499130`, Q391 — G30 FAQ21841 StatCard 패턴과 동일).
3. 미완료·재사정 대상이 있으면 danger Alert가 표시됩니다.
4. 필터 **「조치 필요만」** / **「전체 이용자」** 로 목록을 좁힙니다.
5. 표에서 **가정방문 일자**·**연간 사정**·**등급변경 재사정**·**미기록 G24b 항목**을 확인합니다.
6. **「욕구사정」** 링크 → **`/clients/:id`** **「기초평가」** 탭에서 기록을 보완합니다.
7. **`hq_admin`** 은 **전 지점** 집계를 조회합니다. **`branch_admin`·`social_worker`** 는 **활성 지점** 기준입니다.

> **API**: **`GET /clients/needs-assessments/compliance?fiscalYear=&branchId=`** · FAQ **Q355·Q357**

#### 정기욕구평가 현황 (G40b, US-T12 · Q302)

SideNav **운영 → 「정기욕구평가 현황 (G40b)」** 또는 대시보드 **「반기 기초평가 위험도 미완료」** 위젯 클릭 → **`/clients/periodic-risk-assessments`**.

1. **회계연도**·**반기**(상반기 1~6월 / 하반기 7~12월)를 선택합니다. 기본값은 **현재 반기**입니다.
2. StatCard — **대상 이용자**·**반기 완료**·**미완료** 인원을 확인합니다.
3. 필터 **「미완료만」** / **「전체 이용자」** 로 목록을 좁힙니다.
4. 미완료 행의 **「이용자 상세」** 링크 → **`/clients/:id`** **「위험도평가」** 탭 **`ClientPeriodicRiskAssessmentPanel`** 에서 3종 평가를 등록합니다.
5. **`hq_admin`** 은 지점 선택기 없이 **전 지점** 집계를 조회합니다. **`branch_admin`·`social_worker`** 는 **활성 지점** 기준입니다.

> **API**: **`GET /clients/periodic-risk-assessments/compliance?fiscalYear=&fiscalHalf=&branchId=`** · FAQ **Q302**

| 목록 열 | API 필드 |
|--------|---------|
| 나이 | `ageYears` 또는 `birthDate` 폴백 |
| 지역 | `regionLabel` |
| 보호자 | `primaryGuardianName` |

#### 신규 이용자 등록

**FE `42f48e1`** — SideNav **이용자** 또는 목록 **신규 등록** → **`ClientFormPage`**(`/clients/new`). **`hq_admin`·`branch_admin`·`social_worker`** 가 등록할 수 있습니다 (BE `208b37e`, Q267).

| 단계 | 화면·API |
|------|----------|
| 1 | **`hq_admin`** — 먼저 **지점 선택기**로 작업 지점을 선택합니다 (활성 지점 미선택 시 저장 **403**) |
| 2 | 이름·생년월일·등급·본인부담·주민번호 동의·**대표 보호자(`primaryGuardian`)** 입력 후 **저장** → `POST /api/v1/clients` — **서버 필수** (`0441a07`, Q268) |
| 3 | **API 갭** — `birthdate`·`ssn` 등 필드명 불일치 시 저장 실패 — FAQ **Q151**·Swagger |
| 4 | (선택) Swagger `POST /clients/{id}/client-user`·`POST …/photo` |

#### 배차(픽업) 프로필 설정 (US-T01, UI 연동 Fixed)

이동 서비스를 이용하는 이용자는 **배차 명단**에 포함되도록 픽업 정보를 등록해야 합니다 (FE `3c55339`, FAQ **Q166**).

1. **`ClientFormPage`**(`/clients/new` 또는 `/clients/:id/edit`) 하단 **「배차·픽업 정보」** 카드로 이동합니다.
2. **이동서비스(픽업 배차) 이용** 을 체크합니다.
3. 아래 필드를 입력하고 **저장**합니다.

| 화면 필드 | API 필드 | 설명 |
|----------|---------|------|
| 이동서비스 이용 | `usesTransport` | `true` — **`GET /transport/roster`** 명단 포함 |
| 픽업 주소 | `pickupAddress` | 미입력 시 **거주지 주소** 사용 · 저장 시 암호화 |
| 픽업 연락처 | `pickupContact` | 미입력 시 **이용자 연락처** 사용 |
| 희망 탑승 시각 | `desiredBoardingTime` | `type="time"` — **승차(PICKUP)** 명단·정차 기본 시각 (Q400). 미입력 시 기존 `defaultPickupTime`과 동기화 |
| 희망 하차 시각 | `desiredDropoffTime` | `type="time"` — **하차(DROPOFF)** 명단·정차 기본 시각 (Q400) |

> **레거시 필드** — API·DB에는 `defaultPickupTime`이 남아 있으며, **희망 탑승 시각** 저장 시 함께 갱신됩니다.

> **수정 모드** — 기존 암호화 값은 입력란에 표시하지 않고, help 텍스트에 **`pickupAddressMasked`·`pickupContactMasked`** 로 안내합니다. 변경하지 않으려면 해당 필드를 **비워 두세요**.
>
> **주소 변경** — 픽업 주소를 바꾸면 **geocode 캐시가 무효화**되어 다음 배차 시 좌표를 다시 조회합니다.
>
> **API 갭** — 등록·수정 **기본 정보** 본문(`birthdate`·`primaryGuardian` 등) 불일치 시 저장 실패 — FAQ **Q151**·Swagger 우회.

> **수정** — 상세 **「수정」** → `/clients/:id/edit`. 보호자 변경은 상세·`POST /clients/{id}/guardians`.

#### 급여계획 통보 모니터링 (`/clients/care-plan-notifications`, G38, BNK-106)

이지케어 FAQ 21802 대응 — **급여인정 시작 후 5·11개월 milestone**·**재발급 인정기간 첨부 미반영**을 지점 단위로 모니터링합니다 (BE `5fd35a6`·`03211e6` + FE `28c22b0`, FAQ **Q277 Fixed**).

1. SideNav **운영 → 급여계획 통보 (G38)** 로 이동합니다 (`hq_admin`·`branch_admin`·`social_worker`만 표시).
2. 상단 StatCard 4종 — **전체 이용자** · **급여 5개월 경과** · **급여 11개월 경과** · **이용계획서 재발급 미반영** — 을 확인합니다.
3. **황갈색(WARNING)** — 5·11개월 경과 안내 · **빨간색(CRITICAL)** — 최신 등급 이력에 **인정기간 첨부(G37) 없음**.
4. **표시** 드롭다운 — **알림 대상만**(기본) 또는 **전체 이용자**.
5. 표에서 **알림** Badge·**이용계획서 첨부** 열을 확인하고, **「등급 이력」** 링크로 이용자 상세 **등급 이력** 탭(Q274)에서 PDF/PNG를 업로드합니다.
6. **`/dashboard`** 에서도 동일 3종 gap 위젯으로 빠르게 확인할 수 있습니다.

| API | 용도 |
|-----|------|
| `GET /api/v1/clients/care-plan-notifications/compliance` | 활성 지점 스코프 compliance 집계 |
| `GET …/compliance?branchId=` | JWT 스코프 내 **특정 지점** 조회 (BE `03211e6`, Swagger·연동 테스트용) |

> **`hq_admin`**: 지점 선택기로 **활성 지점**을 고른 뒤 조회합니다. **`caregiver`** 는 이 메뉴에 접근할 수 없습니다.

#### 모니터링 자가진단·유선상담 (`/compliance/monitoring`, G30, BNK-169~171·181)

이지케어 FAQ **21836**(유선상담)·**21841**(월별 자체점검)·**21842**(직전 6개월 자가진단)·**21838~21842**(통합 checklist)에 대응합니다. 지점 단위 **15문항 자가진단표**·**월 5명 유선상담**·**통합 checklist 8문항 자동 집계**를 기록·준수 여부를 확인합니다 (BE `6a72b70`·`b1dfd34` + FE `574bd08`, FAQ **Q314·Q320 Fixed**).

1. SideNav **운영 → 모니터링 자가진단 (G30)** 로 이동합니다 (`hq_admin`·`branch_admin`·`social_worker`만 표시).
2. 상단 **모니터링 근거 안내** 패널(`MonitoringEvidenceContextPanel`, FE `7d2cb4a`, Q391)에서 **FAQ21838~21842 문항 6~15** 연계 증빙 기간과 **정기욕구평가(G24b)·일정·청구(G21)·본인부담 통계(G26)** 화면으로 이동하는 링크를 확인합니다. 선택 **연·월** 기준 **전전월 ±2개월** 증빙 기간이 표시됩니다.
3. **공단 평가지표 ↔ ogada 문항 매핑 (G30-LEGEND)** 패널(`MonitoringOfficialIndicatorLegendPanel`, FE `fdc135b`, Q629)에서 **ogada 15문항 번호**와 **공단 평가지표 1~15** 대응 관계를 확인합니다. ogada 문항 순서와 공단 번호가 **1:1로 일치하지 않으므로** 평가 준비 시 이 표를 참고하세요. **직접 매핑** 예: ogada **#6**(6개월 자가진단) ↔ 공단 **#15** · ogada **#15**(유선상담 5명·60%) ↔ 공단 **#12~14**.
4. **통합 모니터링 checklist** 패널에서 선택 **연·월** 기준 **FAQ21838~21842 문항 6~15** 준수 현황을 확인합니다 (Q320). **증빙 수집 기간(FAQ21838 전전월 ±2개월)** 이 패널 상단에 표시됩니다 — 예: 2026년 6월 모니터링 → **2026-02-01 ~ 2026-06-30** (`MonitoringEvidenceWindow`, BE `73df04d` / FE `73094f9`). **충족·일부 충족·미충족·수동 점검** StatCard와 8행 표가 표시됩니다. **RFID(문항 10)** 는 **수동 점검(MANUAL)** 로만 표시됩니다.
5. **연·월** 선택 후 **조회**합니다. **`BranchSwitcher`** 로 선택한 지점 기준 데이터가 표시됩니다.
6. **6개월 자가진단 준수** StatCard — FAQ21842 **직전 6개월** 중 기록이 없는 월 수를 확인합니다.
7. **월별 자가진단 (15문항)** — **점검 문항** 선택 시 **점검방향·관련근거·점검기준·점검결과·점검방법** 5필드가 템플릿으로 채워집니다. **관련근거**는 FAQ21836 **고시·세부사항 조문** fallback이 기본값으로 들어갑니다 (`0da41c6`).
8. 등록된 행 **「수정」** 으로 같은 월·문항을 갱신할 수 있습니다. **문항당 월 1건**만 허용됩니다 (V100 UK).
9. **유선상담 (월 5명·60% 만족, FAQ21841)** — **유선상담 실시**·**만족(Y) 비율** StatCard로 **등록 건수·만족 비율**을 확인합니다 (`9ad8346`, Q365). 5명 미달·60% 미달 시 **warning Alert**가 표시됩니다. **추천 대상** 목록에서 이용자를 고른 뒤 **이용자·상담일·상담 내용·만족(Y/N)** 을 입력해 등록합니다. **이용자×월 1건** 제한 · **퇴소·비활성 이용자**는 등록 불가 (V101·V138).
10. **`caregiver`·`guardian`** 은 이 화면에 접근할 수 없습니다.

| API | 용도 |
|-----|------|
| `GET /api/v1/compliance/monitoring/checklist?referenceYear=&referenceMonth=` | **통합 checklist** 8문항 자동 집계 (FAQ21838~21842, Q320) |
| `GET /api/v1/compliance/monitoring/items` | 15문항 점검 템플릿 |
| `GET /api/v1/compliance/monitoring/self-diagnoses?referenceYear=&referenceMonth=` | 월별 자가진단 목록 |
| `POST /api/v1/compliance/monitoring/self-diagnoses` | 자가진단 등록 |
| `PATCH /api/v1/compliance/monitoring/self-diagnoses/{diagnosisId}` | 자가진단 수정 |
| `GET /api/v1/compliance/monitoring/self-diagnoses/compliance?referenceDate=` | **6개월** rolling compliance |
| `GET /api/v1/compliance/monitoring/phone-consultations/suggestions` | **월 5명** 추천 이용자 |
| `POST /api/v1/compliance/monitoring/phone-consultations` | 유선상담 등록 |
| `GET /api/v1/compliance/monitoring/phone-consultations/compliance` | 월 유선상담 준수 |

> **P2 잔여**: FAQ21812 **관리자 라운딩** · **live E2E verify** — FAQ **Q314·Q320** 참고.

#### 운영주기별 워크플로 카탈로그 (`/compliance/workflow-catalog`, G34-WORKFLOW-CATALOG, BNK-507)

이지케어 FAQ **21795–21828**(운영주기별 업무흐름)과 ogada 화면·컴포넌트 **인용 현황**을 한눈에 비교하는 **cross-walk 카탈로그**입니다 (FE `77cfc38`/`9f110a5`, FAQ **Q635 Fixed**). 평가 준비 시 **미인용** 항목을 우선 보완하세요.

1. SideNav **운영 → 운영주기별 워크플로 (G34)** 로 이동합니다 (`hq_admin`·`branch_admin`·`social_worker`).
2. 상단 **컴플라이언스 관련 화면** 링크에서 **모니터링 자가진단 (G30)**·**연간 욕구사정 (G24b)** 등으로 이동할 수 있습니다.
3. **StatCard** — **전체 28건** · **ogada 인용 16건** · **미인용 12건** · **인용률 57.1%** 를 확인합니다.
4. **운영 주기 필터** — **일일/수시·주간·월간·분기·반기·연간·비정기** 중 선택합니다. 각 칩에 **건수**가 표시됩니다.
5. **인용 상태 필터** — **ogada 인용** / **미인용** 으로 좁힐 수 있습니다.
6. 표에서 **FAQ** 열의 링크를 누르면 **ezCare FAQ 원문**(새 창)이 열립니다.
7. **ogada 화면** 열의 내부 링크를 누르면 해당 **Route**로 이동합니다. route가 없는 항목은 텍스트만 표시됩니다.

| 항목 | 내용 |
|------|------|
| 데이터 소스 | **`ezcareWorkflowCatalog.js`** — FE 정적 카탈로그 (서버 API 없음) |
| 인용 기준 | ogada 화면·컴포넌트가 FAQ 업무흐름을 **verbatim** 반영하면 **ogada 인용 ✅** |
| 잔여 P3 | **선임 업무수행일지 재사용 템플릿** 설정 UI는 별도 Epic — Q635 참고 |

> 관련: Q635 · USER_MANUAL §3-5 · ADMIN_GUIDE §1-4

#### 지점 관리 (`/branches`, `hq_admin`·`branch_admin`)

SideNav **운영 → 지점** → **`BranchesPage`** (FE `1794e1c`, Q184): 목록·검색·페이지네이션·등록/수정 모달.

| 필드 | UI | API |
|------|-----|-----|
| 지점명·급여종 | `TextInput`·`Select` (`DAY_CARE`·`HOME_VISIT`·`INTEGRATED_HOME`) | `POST/PATCH /branches` `serviceType` |
| 행정구역 | **`RegionSelector`** — 시·도→시·군·구→읍·면·동 3단 | `GET /regions/sidos` 등 → `regionDongCode` |
| 주소·연락처·활성 | 폼 필드 | `addressLine1`·`phone`·`active` |
| **통합재가 가산 안내** | **`INTEGRATED_HOME` 선택 시** warning `Alert` (G19, Q223) | v1 **자동 청구·정산 미지원** — MOHW 제55조의2 안내 문구만 |

> API 오류 시 Swagger `GET/POST/PATCH /branches`. 지점명 UK — FAQ Q146. **통합재가 월 가산 100,000원/인**은 v1에서 **수동 확인** — FAQ Q223.

#### 지점 도입 후 관리 체크list (G-ONBOARD-SUPPORT, US-O05, Q353)

silverangel **businessSupport 1~4회차**와 동일한 **신규 지점 도입 SLA 체크list**입니다. **직원 입사 7종 서류(FAQ21806·Q300)** 와는 **별도 기능**입니다 — 지점 단위·회차별 운영 점검용입니다.

| 역할 | 오픈일 설정 | 회차 체크·메모 저장 |
|------|:-----------:|:------------------:|
| **`hq_admin`** | ✅ | ✅ |
| **`branch_admin`** | ✅ | ✅ |
| **`social_worker`** | ❌ (읽기만) | ✅ |

1. SideNav **운영 → 지점** → **`/branches`** 로 이동합니다.
2. 대상 지점 행의 **「도입 체크list」** 버튼을 누릅니다 (`aria-label`에 지점명 포함).
3. Modal **`BranchOnboardingSupportPanel`** 이 열립니다.
4. **`hq_admin`·`branch_admin`** — **지점 오픈일**을 **`DateInput`** 으로 설정·저장합니다. 오픈일이 없으면 SLA 기한(1~4회차)이 계산되지 않습니다.
   - **오픈일 검증 (QA-B94, `43c4b08`)**: **미래일**·**2000-01-01 이전**·**2099-12-31 이후** 날짜는 `422 BUSINESS_RULE`(`기관 개시일은 미래일 수 없습니다.` / `…2000-01-01부터 2099-12-31 사이여야 합니다.`)로 거부됩니다.
5. 오픈일 저장 후 **1~4회차** 목록이 표시됩니다. 각 회차는 **역할별 `fieldset`**(경영·관리·간호·복지·요양·재활·공통)로 항목이 그룹화됩니다.
6. **`Checkbox`** 로 완료 항목을 표시하고, 필요 시 **회차 메모**(`Textarea`)를 입력한 뒤 **「N회차 저장」** 버튼으로 저장합니다.
7. 상단 **StatCard** — **완료 회차**·**기한 초과 회차** 요약 · **`StatusBadge`** — 회차별 **대기·진행중·기한 초과·완료** 상태.

| 회차 | SLA 기준 (오픈일 기준) | 대표 점검 항목 |
|------|----------------------|---------------|
| **1회차** | 오픈 **+10일** | 직원 ID·권한·간호·프로그램·욕구사정·급여계획·기록지 활용 등 **20항목** |
| **2회차** | 1회차 사후관리 **+10일** | 1차 지도 완수·유선상담·집중배설·사례관리회의·보고서 활용 등 **13항목** |
| **3회차** | 오픈 **+6주** | **직무교육 실시** |
| **4회차** | 직무교육일 **+10일** | 묻고 답하기·기록지 점검·KPI·계획평가달력 활용 |

| API | 용도 |
|-----|------|
| `GET /api/v1/branches/{branchId}/onboarding-support` | 1~4회차·SLA·완료 상태 조회 |
| `PUT /api/v1/branches/{branchId}/onboarding-support` | **`openedOn`** 설정·변경 (`hq_admin`·`branch_admin`) |
| `PATCH …/onboarding-support/sessions/{roundNumber}` | 회차별 **`completedItemKeys`**·**`notes`** 저장 |

> **기한 초과**: `dueDate` 경과·미완료 회차는 **좌측 경고 보더**·**「기한 초과」** Badge로 표시됩니다. **메모에는 PII(주민번호·연락처 등)를 적지 마세요** — 운영 메모만 기록합니다 (DATA_RETENTION §3).

> 관련: FAQ **Q353** · ADMIN_GUIDE §6-2-10 · USER_STORIES US-O05

#### 보호자 관리 (`/guardians`)

SideNav **운영 → 보호자** → **`GuardiansPage`** (FE `6db762a`, UXD-59):

| 기능 | UI | API |
|------|-----|-----|
| 목록·검색 | 보호자 테이블·페이지네이션 | `GET /guardians` **미구현** — 404 시 Swagger `GET /users?branchId=` (Q107) |
| **보호자 초대** | **「보호자 초대」** → `GuardianInviteModal` — 이용자 선택·이메일·관계 | `POST /clients/{clientId}/guardians/invitations` |
| 상세 | `/guardians/:id` — **`GuardianClientLinks`**(연결 이용자·대표 보호자, Q185) · **수정** 모달 | `GET /guardians/{id}` · 대표 지정 API **후속** |

> 이용자별 초대는 **§3-3 이용자 상세**에서도 동일 API를 사용합니다.

### 4-4. 출석 관리 (`/attendance`)

**FE `8383f8d` + BE `0c69060`/`61e1970` (US-E01·E02 + G-ATTENDANCE-ROSTER-STATUS, Q609)** — 당일 **활성 이용자 전원** 목록 + **이름·상태·미처리 행** + 수기 **입소·귀가·결석** UI. **`AttendancePage`** 는 **`fetchAttendanceApi()`** 만 호출해 roster를 표시합니다(별도 `/clients` 병합 없음). 화면 상단 **`AttendanceContextNav`** 로 출석 현황·탑승·현장·수기 체크인·통계·QR을 전환합니다 (Q242). 카드 상단에 **`BranchScopeNotice`** 로 **조회 지점**이 표시됩니다 (Q173).

#### G15 탑승/현장 출석 분리 (케어포 2-2·2-3, Q232)

이동서비스(차량) 이용 여부(`usesTransport`)에 따라 출석 화면을 **3가지**로 나눕니다.

| 경로 | SideNav | 대상 이용자 | API `transportMode` |
|------|---------|------------|---------------------|
| `/attendance` | **출석 현황** | 전체 | `all`(기본) |
| `/attendance/boarding` | **탑승(차량)** | `usesTransport=true` | `boarding` |
| `/attendance/on-site` | **현장 출석** | `usesTransport=false` | `on_site` |

1. SideNav **출석** 그룹에서 **탑승(차량)** 또는 **현장 출석**을 선택합니다.
2. 화면 제목·안내 문구가 **케어포 2-2(탑승)** / **2-3(현장)** 에 맞게 표시됩니다.
3. 목록은 **`GET /api/v1/attendance?transportMode=boarding|on_site`** 로 서버 필터링되며, FE에서도 `usesTransport` 프로필로 한 번 더 정합합니다.
4. **입소·귀가·결석** 조작은 **전체 출석 화면과 동일**합니다 — 차량 이용자는 **탑승 출석** 화면에서, 미이용자는 **현장 출석** 화면에서 처리하세요.

> **이용자 프로필**: `usesTransport` 는 **이용자 등록·수정** 화면 **「배차·픽업 정보」**에서 설정합니다 (§4-3, Q166). 변경 후 출석 화면을 **새로고침**하세요.

| 작업 | UI | API | 비고 |
|------|-----|-----|------|
| 목록·요약 | ✅ StatCard(입소·귀가·결석·**미처리**) + 테이블 | `GET /attendance?transportMode=` | **`clientName`·`status`·활성 이용자 전원** · FE API 단일 호출 (`8383f8d`, Q609) |
| 체크인 | ✅ **입소** 버튼 (미처리·`status=null`) | `POST /attendance/check-in` | 응답에 **`clientName`·`status=CHECKED_IN`** |
| 체크아웃 | ✅ **귀가** → `CheckoutModal`(교통편) | `POST /attendance/check-out` | **`transportType`** (Q96) |
| 결석 | ✅ **결석** → `AttendanceAbsentModal` | `POST /attendance/absence` | **`status=ABSENT`** |

> **roster (Q609)**: **`GET /attendance`** 가 지점 **활성 이용자 전원**을 반환합니다. 출석 기록이 없으면 **`id=null`**, **`status=null`(미처리)** — **입소·결석** 버튼이 표시됩니다. **`AttendanceStatusSupport.deriveStatus()`** 가 입소·귀가·결석 상태를 파생합니다.
>
> **roster 응답 필드 (310차+)**: 
>
>> | 필드 | 타입 | 설명 | 예시 |
>> |------|------|------|------|
>> | `clientId` | UUID | 이용자 식별자 (출석 기록 있을 때만) | `uuid-abc` |
>> | `clientName` | string | **이용자 이름** — FE 단일 호출로 clientName 표시 | `홍길동` |
>> | `status` | enum | 출석 상태 (`CHECKED_IN`\|`CHECKED_OUT`\|`ABSENT`\|`null`) | `CHECKED_IN` |
>> | `checkInTime` | timestamp | 입소 시각 (Asia/Seoul, nullable) | `2026-06-22T09:00:00+09:00` |
>> | `checkOutTime` | timestamp | 귀가 시각 (nullable) | `2026-06-22T16:00:00+09:00` |
>> | `absenceReason` | string | 결석 사유 (nullable) | `질병` |
>> | `contact` | string | 이용자 본인 전화 (**`hq_admin`만 전체**, 기타 역할 마스킹) | `010-1234-5678` |
>> | `guardianContact` | string | 대표 보호자 전화 (마스킹 규칙 동일) | `010-9999-0000` |
>> | `usesTransport` | boolean | 이동서비스 이용 여부 (탑승/현장 필터 기준) | `true` |
>
> **주의**: Swagger의 `GET /attendance` 우회 불필요 — FE가 **`clientName`** 을 자동 병합하므로 `/clients` 추가 호출 없음.

#### 잔여 P3 — 출석 QR 카메라 스캔 (Q109)

| 증상 | 원인 | 조치 |
|------|------|------|
| 보호자 **카메라 스캔 불가** | **`GuardianCheckinPage`** 카메라 UI **P3** | **토큰 수동 입력** 또는 `/guardian/checkin` (Q109) |
| **`/attendance/stats` 숫자 비음** | 해당 월·지점 **출석 기록 없음** 또는 **활성 이용자 0명** | **`/attendance`**(Q609)에서 출석 입력 후 재조회 · **`hq_admin`** BranchSwitcher 확인 (Q173) |
| 귀가 **교통편 미저장** | *(Fixed `dffd726`)* — FE **`transportMethod` → BE `transportType`** | FAQ Q96 |

**보조 화면**

| 경로 | UI | 비고 |
|------|-----|------|
| `/attendance/boarding` | **`AttendancePage`** — 탑승(차량 이용) 전용 (G15, Q232) | `transportMode=boarding` |
| `/attendance/on-site` | **`AttendancePage`** — 현장 출석(차량 미이용) 전용 (G15, Q232) | `transportMode=on_site` |
| `/attendance/stats` | **`AttendanceStatsPage`** + `MonthInput` + **`AttendanceRateChart`** + **`BranchScopeNotice`** (US-E05, UXD-48·53) | **✅ full-stack** (`dffd726`, Q615) — 월별 StatCard·6개월 추이·다지점 표 |
| `/attendance/qr/generate` | **`QrGeneratePage`** — `generateBranchQrApi`·**PNG 미리보기·「이미지 저장」·인쇄**(US-E03) | **✅ full-stack** (`250619e`, Q624) — `branchQrCode.js`·`qrcode` |
| `/attendance/checkin/qr` | **`GuardianCheckinPage`** — `checkin-targets`·`scanQrAttendanceApi`·입소/귀가 `FilterChips` (US-E04) | **Fixed** (Q109) — 카메라 스캔 **P3** |

#### 월별 출석 통계 (`/attendance/stats`, US-E05, Q615)

SideNav **출석 → 출석 통계** 또는 **`AttendanceContextNav`** 로 이동합니다.

1. **대상 월**을 **`MonthInput`** 으로 선택하고 **「조회」** 를 누릅니다.
2. **`BranchScopeNotice`** 로 **조회 지점**을 확인합니다 — `hq_admin`은 **BranchSwitcher** 전환 후 **재조회**하세요 (Q173).
3. StatCard **「활성 이용자」「출석 일수」「출석률」** 과 **최근 6개월 출석률 추이** 차트가 표시됩니다.
4. **HQ(`hq_admin`)** 는 **지점별 표**에서 같은 월의 지점 간 비교가 가능합니다.

| API 필드 | 화면 표시 |
|----------|-----------|
| `activeClientCount` | **활성 이용자** (명) |
| `attendedDays` | **출석 일수** (일) |
| `attendanceRate` | **출석률** (0~1 → %, 예: 0.50 = 50.0%) |

> **P3 한계**: **일별·이용자별 breakdown** 은 MVP 범위 외 — 월·지점 집계만 제공합니다.

> 관련: FAQ **Q106·Q613·Q615·Q624** · ADMIN_GUIDE §6-2-21

#### QR 생성·게시 (US-E03, Q624)

| 단계 | 조작 |
|------|------|
| 1 | **출석 → QR 생성**(`/attendance/qr/generate`) — **`BranchScopeNotice`** 로 지점 확인 |
| 2 | **입소** 또는 **귀가** 선택 → **「QR 생성」** |
| 3 | **PNG 미리보기** 확인 → **「이미지 저장」** 또는 **「인쇄」** 로 입구 게시 |
| 4 | 보호자는 **`/guardian/checkin`** 에서 QR 스캔(또는 토큰 입력) |

> **기술**: BE **`POST /branches/{branchId}/qr`** `{ direction, expiresInMinutes }` → **`qrToken`** · FE **`branchQrCode.js`** 가 **`qrcode`** 로 PNG data URL 생성 (`250619e`).

### 4-5. 건강 기록 (`/health`)

**FE `1d5747d` (케어포 3-1 segment nav · UXD-39·UXD-40·UXD-41, US-F01·F02·F03)** — 이용자 선택 후 **일일 건강·투약·낙상·특이사항 입력·저장 UI**가 제공됩니다. 상단 **`CareProvisionSegmentNav`** 로 식사·간호·목욕·프로그램 등 **급여제공 전용 화면**으로 이동합니다 (Q524, v1.2.1 P1).

1. **기록 → 건강 기록**(`/health`)으로 이동합니다.
2. **`RecordsContextNav`** 아래 **「급여제공 기록 (케어포 3-1)」** 세분화 메뉴에서 필요한 급여제공 화면으로 이동할 수 있습니다 — 식사·식사도움·간호·목욕·프로그램·특이사항 (Q524).
3. **이용자** 드롭다운에서 대상을 선택합니다 (`GET /clients`).
4. 비정상 수치가 있으면 **`HealthAbnormalBanner`**가 표시됩니다.
5. 탭으로 기록 유형을 선택합니다.

| 세분화 링크 | 경로 | 비고 |
|------------|------|------|
| 식사 관리 | `/meals` | 일자별 식사 |
| 식사 도움 | `/care/meal-assistance-records` | L02_M13 |
| 간호 제공 | `/nursing/service` | L03_M01 |
| 목욕 일정 | `/care/bathing-schedules` | L02_M03 |
| 프로그램 | `/programs` | 프로그램 참여 |
| 특이사항 | `/care/service-special-notes` | L02_M15 |

| 탭 | UI | API | 비고 |
|----|-----|-----|------|
| **일일 건강** | `VitalsRecordForm` — 혈압·체온·혈당·SpO2 + **비정상 경고**(Q155) | `POST …/health/vitals` | **`healthApiPayload.js`** — `bloodGlucose`·`recordedAt` **정합 Fixed** (Q154) |
| **투약 기록** | `MedicationRecordForm` — 약품명·용량·시간 + **중복 경고** | `POST …/health/medications` | **`administeredAt`·`administeredBy`·`recordedAt` Fixed** (Q95) |
| **낙상·특이사항** | **`IncidentRecordForm`** — 유형(낙상/사고/특이사항/기타)·내용·발생 시각 | `POST …/health/incidents` | **`detail`·`recordedAt`·`incidentType` Fixed** (UXD-41, Q154) |
| **기록 이력** | 당일 바이탈·투약·**사고** 목록 | `GET /clients/{id}/health` | **`healthRecords.js`** — `payload` 파싱 |

> **바이탈 저장 성공 시** 연결 보호자에게 J03 **`DAILY_CARE` 알림 dispatch** 시도 (preference on, stub 환경은 DB 이력만, Q147).

> **낙상(`FALL`) 기록 시** J03 **`EMERGENCY` 알림 dispatch** — 방해 금지(22:00–08:00) **우회**(Q147·Q156). 즉시 센터장에게도 구두 보고하세요.

> **자유 메모(특이사항 텍스트)** — `POST …/health/notes` API는 UI **미포함**. Swagger 사용 (Q95).

**건강 추이** — `/health/:clientId` **`HealthDetailPage`**: **`HealthTrendChart`**(혈압·체온·혈당·SpO₂) + 7일·30일 **`FilterChips`** + **표 이력** (`healthRecords.js`, UXD-48, US-F04). **기간 변경 시 API `?days=` 미호출** — Q165.

### 4-6. 청구·정산 (`/billing`)

ogada 청구는 **2단계 모델**입니다 (케어포 벤치마킹).

```
[① ogada 내부] 출석·등급·수가표 → 급여·본인부담금 자동 계산 → 명세서 생성
[② 공단 포털]  장기요양정보시스템(롱텀)에서 공단 급여 청구·전송 (ogada 밖)
[③ ogada 연동] 공단 「청구내역상세」엑셀 import → 대조
```

> MVP에서는 공단 포털 **직접 전송**은 지원하지 않습니다. **본인부담금 CMS 자동이체(7-4)**·**간편결제(7-5)** 는 v2 **UI·API skeleton Fixed**(stub FCMS·stub PG, Q206–Q208·Q326)이며, **보호자 포털에서의 결제**는 범위 밖입니다.

#### 월말 청구 절차

**사전 준비** (최초 1회 또는 수가 개정 시 — 통합 관리자 `hq_admin`이 설정)

- 등급별·연도별 **수가표** 등록
- 본인부담 **비율표** 확인 (기본값 제공)

**월말 작업** (센터장)

1. **청구·정산**(`/billing`) 메뉴로 이동합니다.
2. 상단 **「월별 청구 생성」** 카드(`ClaimGenerationPanel`)에서 **대상 월**(예: 2026-05)을 선택합니다.
3. **전월 미입금 가드** — 전월에 **확정·미수납(`CONFIRMED`)** 청구가 있거나 **G33 미정산**이 있으면 **`ClaimGenerationGuardBanner`** warning과 **`LifecycleWorkflowPanel`**(케어포 **7-2→7-1** 단계)이 표시되고 **「월별 청구 생성」** 버튼이 비활성화됩니다 (`338c014`, Q310). **G33**은 **적용 시작월(`effectiveMonth`)이 대상 청구월 이전·동월**이고 **양수 미납**이 남아 있으면 차단됩니다 (BE `21eb0af`, Q270). 배너의 **입금 처리**·**미납 관리**·**(해당 시) 청구시작 기준금액 정산** 링크로 선행 작업을 완료하세요. **가드 API 오류** 시에도 생성이 차단됩니다 (`60dc5d0`, Q225).
4. **(선택) 월한도 초과 경고** — **`/billing`** 상단 **`MonthlyBenefitCapGuardPanel`** 이 선택한 **대상 월** 기준으로 초과 이용자를 표시합니다. 초과가 **없으면** **`MonthlyBenefitCapGuardBanner`** 가 **「재가급여 월한도 점검 완료」** success 메시지를 표시합니다 (`62f022d`, Q226). 초과가 있으면 `role="alert"` 경고·이용자 미리보기가 표시됩니다 — **차단하지 않습니다**. **`/dashboard`** 에도 동일 패널이 노출됩니다 (US-M04). 청구 상세(`/billing/claims/:id`)에서는 **`MonthlyBenefitCapBanner`** 로 이용자별 한도·초과액을 확인할 수 있습니다.
5. 가드가 통과되면 **「월별 청구 생성」**을 클릭합니다 (`POST /api/v1/billing/claims/generate`). 패널 상단에 **가산 자동 반영 안내**가 표시됩니다 (`CLAIM_GENERATION_SURCHARGE_NOTE`, Q229).
   - **기본(출석 기준)**: 조직 설정이 **`ATTENDANCE_SCHEDULE`** 일 때 — **출석일마다** 등급별 1일 수가에 **입·퇴소 시각·휴일** 기준 **MOHW 가산율 1종**을 자동 반영한 합계 (`d7475fd`, Q229). 중복 가산 없음.
   - **공단 엑셀 기준**: 조직 설정이 **`NHIS_IMPORT`** 이면 해당 월 **NHIS import** 일수 × 기준 1일 수가 — **가산 없음** · import 없으면 생성 거부 (Q224).
   - `본인부담금 = 총액 × 이용자 본인부담 구분 비율` · `공단부담 = 총액 − 본인부담금`
6. 생성된 청구 목록에서 이용자별 명세를 검토합니다.
   - **상태 필터 (`FilterChips`, Q128)**: 화면 상단 **전체·작성중·확정·수납완료** 칩을 클릭해 목록을 좁힙니다. API `?status=DRAFT|CONFIRMED|PAID`와 연동됩니다.
   - **(선택) NHIS 사전 대조** — **`DRAFT`** 청구 상세(`/billing/claims/:id`)의 **「공단 명세 비교」** 카드(`BillingNhisComparisonPanel`, BNK-87·BNK-91 P2, Q264)에서 **이용자별 서비스일수·공단부담금·본인부담금**을 최신 NHIS import와 비교합니다. 상단 StatCard **일치·불일치·공단 미매칭** 건수와 이용자별 비교 표를 확인합니다. 공단 청구액 불일치 시 **「공단 초과」**·**「공단 부족」** Badge가 표시됩니다. 불일치가 있으면 패널의 **NHIS reconciliation** 링크로 이동해 보정한 뒤 확정하세요. **확정·수납 청구**에서는 패널이 표시되지 않습니다 (`18f5173`). NHIS import 배치가 없으면 안내 메시지가 표시됩니다 — 먼저 §4-6-1에서 공단 엑셀을 업로드하세요.
   - **상태 변경**: 행의 **확정**·**수납완료** 버튼 → **`BillingStatusConfirmModal`** — 금액·되돌릴 수 없음 경고 확인 후 제출 (Q128).
   - **대상 월 컬럼**: API는 `yearMonth`를 반환하지만 UI는 `billingMonth`를 표시해 **빈 칸**일 수 있습니다 (FAQ Q98). 월은 Swagger 응답 또는 생성 시 선택한 월로 확인하세요.
7. 상태를 **작성중(`DRAFT`) → 확정(`CONFIRMED`) → 수납완료(`PAID`)** 순으로 변경합니다. 동일 상태로의 변경(no-op)은 거부됩니다. 과오납 등으로 **환불**이 필요하면 **`PAID`** 청구 상세에서 **「환불 처리」** 로 **`REFUNDED`** 전환합니다 (§5-10, Q261).
8. **명세서 PDF**를 출력·보관합니다.
9. 공단 포털에서 받은 **청구내역상세 엑셀**을 **import**하여 ogada 데이터와 대조합니다.
10. **`UNMATCHED`(매칭 실패)** 행이 있으면 후보 이용자 검색 후 **수동 연결**합니다 (아래 §4-6-1).

> **청구 생성 기준 변경** — 통합 관리자(`hq_admin`)는 **조직 설정**(`/organization/settings`) → **「청구·정산」** 에서 **급여일정(출석)** vs **공단 엑셀** 기준을 선택합니다 (§5-5, Q224).

#### 입금·미납·보호자 발송 (v2, US-L01·L02·G2)

SideNav **청구** 그룹 — **`PaymentPage`·`OverduePage`·`EasyPayPage`·`CmsPage`** + 상단 **`BillingContextNav`**(입금↔미납↔CMS↔간편결제 전환, Q203) + 청구 상세 **보호자 발송** (Q107·Q134·Q174·Q196).

| 화면 | UI | 백엔드 |
|------|-----|--------|
| 입금 처리 (`/billing/payments`) | **`BillingContextNav`** + **`PaymentPage`** — **이용자명**·월·검색·**`Pagination`** · **CMS 등록** 열(ACTIVE Badge·미등록 deep link, Q638) · **`PaymentRecordModal`** · **현금 수납 후 `CashReceiptRegisterModal`** (Q531) | **`POST /claims/{id}/payments` Fixed** · 목록은 **`GET /billing/claims` 클라이언트 필터** (전용 목록 API 미구현, Q174·Q198) |
| 미납 관리 (`/billing/overdue`) | **`BillingContextNav`** + **`OverdueSummaryBar`** + 보호자 **`MaskedPhone`** + **「안내 발송」** + **「관리」** + **`Pagination`** | **`GET /billing/overdue?page&size&q=` Fixed** (Q197) · **`POST /claims/{id}/notify` Fixed** (Q196) · **독려·조정 Modal** (Q602, `0420e6b`) |
| **간편결제 (7-5)** (`/billing/easy-pay`) | **`BillingContextNav`** + **`EasyPayPage`** — **`EasyPayPanel`** — 청구 선택·**CARD/카카오페이**·보호자(선택)·**전월 미입금 가드 배너** | **`POST/GET /billing/easy-pay/claims/{id}/payment` Fixed** (BNK-189, Q326·Q327) |
| 청구 상세 (`/billing/claims/:id`) | **`BillingDetailPage`** — **`DRAFT`** 시 **「공단 명세 비교」** (`BillingNhisComparisonPanel`, Q264) · **`CONFIRMED`/`PAID`** 시 **「명세 4채널 발송」** (`BillingStatementDispatchPanel`, Q364) · **「명세 인쇄 산출물 (7-1)」** (`BillingStatementPrintPanel`, Q475) · **「보호자 발송」** · **「납부확인서 발송」** (`PAID`+`paidAt`+`paymentMethod`, Q221·Q249) · **「환불 처리」** (`PAID`+`paidAt`, Q261) | **`GET/POST …/statement-dispatches`** · **`PATCH …/statement-dispatches/{id}`** · **`GET …/statement-pdf`** (명세 PDF) · **`GET /claims/{id}/nhis-comparison`** · **`POST /claims/{id}/notify`** · **`POST /claims/{id}/payment-receipt-notify`** · **`POST /claims/{id}/refunds`** |
| CMS 자동이체 (`/billing/cms`) | **`CmsPage`** — **등록 관리**·**CMS 출금** 2탭 · **`CmsEnrollmentForm`·`CmsEnrollmentTable`·`CmsDebitPanel`** | **`POST/GET/DELETE /billing/cms/enrollments*`** · **`POST/GET /billing/cms/claims/{id}/debit`** |

**입금 처리 절차 (UI, FE `dd72ff8`)**

1. **청구 → 입금 처리**로 이동합니다.
2. **기준 월**·이용자 검색 후 **조회**합니다. 표에 **이용자명**·**CMS 등록**·청구액·본인부담금·수납 상태가 표시됩니다 (Q198·Q638). *(전용 목록 API 없음 — 확정·수납 청구를 claims에서 필터, Q174)*
   - **CMS 등록** 열 — **ACTIVE** CMS 자동이체가 있으면 **등록완료** Badge · 없으면 **「미등록 · CMS 등록」** 링크 → **`/billing/cms?clientId=`** (Q638).
3. 목록이 많으면 하단 **페이지**를 넘깁니다.
4. 미수납 행 **「수납」** → **`PaymentRecordModal`**에서 **입금일(`DateInput`)**·금액·수단(현금/계좌이체) 입력 후 **저장**합니다 — **입금일 미입력 시 서버 `422`** (`4001510`, Q250).
   - **현금(`CASH`)** 선택 시 Modal 상단에 **법정 안내**(FAQ 21716 — 납입 즉시 발급)와 **「현금영수증 발급목록」** 링크가 표시됩니다 (Q531, FE `a17f148`).
   - **현금 수납 저장 성공** 시 **「국세청 현금영수증 발급을 등록해 주세요」** 안내와 함께 **`CashReceiptRegisterModal`** 이 **자동으로 열립니다** — 해당 청구가 미리 선택된 상태이며, **국세청 발급번호**·식별자를 입력해 저장할 수 있습니다. Modal을 닫아도 **청구 → 현금영수증 발급목록**에서 나중에 등록할 수 있습니다 (Q531).
   - 기본 금액은 **미납 본인부담금 전액**으로 채워집니다 (`normalizeAmount`, Q220).
   - **0원 이하** 또는 **본인부담금 초과(과납)** 금액은 저장되지 않습니다 — 필드 아래 오류 메시지가 표시됩니다 (Q218).
   - **더 이른 월 미납**이 남아 있으면 **「이전 미납 청구(YYYY-MM) 입금 선행이 필요합니다.」** 로 저장이 거부됩니다 — **오래된 월부터** 입금하세요 (Q614, BE `a6eb8b7`).
   - 서버가 **본인부담금 미설정(`copayAmount` NULL)** 청구를 거부하면 「본인부담금이 설정되지 않아…」 오류가 표시됩니다 — 청구 **재생성** 또는 IT 문의 (Q257).

**은행 거래내역 엑셀 일괄입금 (케어포 7-2, US-L01 — Q227·Q572)**

> **UI Fixed (`9105332`, G-BANK-EXCEL-8 full-stack + UXD-146 `a7d9a2f`)** — **`/billing/payments`** 하단 **`BankDepositImportPanel`** 이 JWT **활성 지점(`activeBranchId`)** 을 **`branchId`** 로 전송합니다. **다지점 `hq_admin`** 은 업로드 전 **BranchSwitcher**로 작업 지점을 선택하세요 (Q228). **미리보기 없이 바로 반영하지 않습니다** — 아래 5~7단계 순서를 따르세요. 미리보기 표는 **행별 `aria-label`**·요약 **`aria-live="polite"`** 로 스크린리더 접근이 보강되었습니다 (Q581).

1. **청구 → 입금 처리**(`/billing/payments`)로 이동합니다.
2. (다지점) 상단 **지점 선택기**에서 대상 지점을 선택합니다.
3. 하단 **「은행 입금 엑셀 일괄 등록」** 카드에서 **적용 월**을 선택합니다.
4. 은행 인터넷뱅킹에서 받은 **입금 내역 xlsx**(.xlsx)를 선택합니다.
   - **「지원 은행 8종 엑셀 형식 (케어포 7-2 p.88)」** 을 펼치면 KB국민·우리·NH농협·신한·하나·부산·대구·광주 **컬럼 예시**를 확인할 수 있습니다 (Q258). 기동 시 **`GET …/bank-deposits/formats`** catalog도 자동 조회합니다 (Q572).
   - 각 은행 행의 **「샘플」** 버튼으로 **최소 컬럼 레이아웃** `.xlsx`를 내려받아 형식을 확인할 수 있습니다 (`b9845ac`, Q258).
5. **「미리보기」**를 클릭합니다. 실제 수납 없이 **행별 매칭 결과**가 표시됩니다 — **`APPLIED`(자동 매칭 가능)** 행은 **자동 체크**됩니다 (Q572).
6. 미리보기 표에서 **적용할 행**을 확인·조정합니다.
   - **`APPLIED`** 행만 체크 가능 · **`UNMATCHED`/`SKIPPED`** 는 체크 불가
   - **「자동 매칭 가능 행 전체 선택」** 체크박스로 일괄 선택/해제
   - 선택 0건 상태에서 **「선택 행 등록」** 을 누르면 **「적용할 행을 최소 1건 이상 선택해 주세요.」** (Q576)
7. **「선택 행 등록 (N건)」**을 클릭합니다. 성공 시 **적용·미매칭·건너뜀 건수**(`appliedCount` 등)가 표시되고 수납 목록이 갱신됩니다.
   - 동일 이용자·금액이 **여러 월 청구**에 매칭 가능하면 **가장 이른 청구월**에 우선 반영됩니다 (Q614, BE `a6eb8b7`).
8. (IT 담당·API 직접 호출) Swagger **`POST /api/v1/billing/imports/bank-deposits`** — `multipart/form-data` — **`branchId`** + `file` + `yearMonth` + (선택) **`rowNumbers`**.
   - **`rowNumbers` 생략** 시 매칭 가능한 **모든 행**을 일괄 반영합니다. **빈 배열 `[]`·0·음수만 포함** → **`422`「선택된 행이 없습니다.」** (Q576, BE `e3b74a0`·`7d29a38`).
   - **미리보기·파싱 결과에 없는 행 번호** → **`422`「선택한 행 번호를 엑셀에서 찾을 수 없습니다: …」** (Q579, BE `6ed7cd4`). **미리보기와 동일 xlsx** 로 등록하세요.
9. 응답·미리보기 `rows[]`에서 행별 **`status`** 를 확인합니다.

| 행 상태 | 의미 | 조치 |
|---------|------|------|
| `APPLIED` | 자동 수납 완료 (`PAID`·`BANK_TRANSFER`) | — |
| `SKIPPED` | 다수 이용자 청구·이미 수납·금액 오류 등 | **`/billing/payments`** 수동 수납 |
| `UNMATCHED` | 이름·금액 불일치 또는 **동월 중복** | 이용자명·청구월 확인 후 수동 수납 |

**매칭 팁**: 입금자명이 **이용자명**과 같거나 포함 관계일 때 매칭됩니다. 동일 이름·금액 청구가 **여러 달**이면 **거래일의 월**로 자동 선택됩니다 (`95bb34d`).

**연말정산 의료비공제 (케어포 7-2-1, G26 / US-L04 — Q252·Q254)**

> **직원** — 이용자 상세 **「청구」** 탭 · **보호자** — 포털 **「연말정산」** 탭 (§8-2). **`MedicalExpenseDeductionPanel`** 이 **`PAID`+입금일·수단** 본인부담금 중 **현금·계좌이체만** **귀속 연도**별로 집계합니다.

1. **집계 대상** — **`CASH`·`BANK_TRANSFER`** 수납 완료 청구. **`CMS`·`EASY_PAY`는 제외** (Q254).
2. **`/billing/payments`**·은행 일괄입금 시 **입금일**을 빠짐없이 기록하세요 (Q250). CMS 출금 수납은 의료비공제에 **포함되지 않습니다**.
3. **귀속 연도**는 **입금일(`paidAt`)의 연도**(KST)입니다. 화면에서는 **「조회」** 로 연도를 확정한 뒤 목록을 불러옵니다 (Q255).
4. **인쇄**·**CSV**·**국세청 엑셀**로 보호자에게 전달하거나 연말정산 자료로 활용합니다 (Q258).
5. (IT) Swagger: `GET /api/v1/clients/{clientId}/medical-expense-deduction?taxYear=2026`.

**미납 관리 절차 (UI, FE `1462396`, US-L02)**

1. **청구 → 미납 관리**로 이동합니다.
2. 상단 **미납 요약**(`OverdueSummaryBar`)에서 건수·금액을 확인합니다.
3. **이용자 검색** 후 **검색** — 서버 **`q`** 파라미터로 필터됩니다 (Q197).
4. 표에서 **경과일**·**보호자 연락처(마스킹)**·**마지막 안내** 시각을 확인합니다.
5. **퇴소 이용자**도 미수납 청구가 남아 있으면 **이름이 표시**됩니다 (BE `a401537`, Q205).
6. 행별 **「안내 발송」** → **`POST /claims/{id}/notify`** (Q196). **22:00~08:00 (Asia/Seoul) 조용한 시간대**에는 버튼이 **비활성**되고 상단 Alert가 표시됩니다 (Q329, `111f056`). **G33 청구시작 기준금액** 행(`OPENING_BALANCE`)은 **청구 ID가 없어 발송 버튼이 표시되지 않습니다** (Q269, `7564c2a`).
7. 행별 **「관리」** → **`OverdueManagementModal`** (`0420e6b`/`751c593`, Q602·Q606) — **독려기록** 탭(전화·문자·기타 연락·**관리 내용 필수**)과 **조정처리** 탭(부분 조정·전액 조정·**사유 필수**)에서 미납 CRM·금액 조정을 기록합니다. 기록 시각은 **`<time dateTime>`** 으로 표시됩니다. **공백만** 입력하면 API·DB(**V168**, Q605) 모두 거부합니다. **「안내 발송」** 성공 시 SMS 독려기록이 **자동 등록**될 수 있습니다 (BE `4d92844`/`f6266ec`) — **동일 청구·이용자·SMS 자동기록은 1회만** (`a45c040`, Q607).
8. 건수가 많으면 하단 **페이지**를 넘깁니다.

**보호자 명세 발송 (G2)**

1. **청구·정산** 목록에서 청구서를 클릭해 **상세**(`/billing/claims/:id`)로 이동합니다.
2. 상태가 **확정** 또는 **수납완료**이면 **「보호자 발송」**을 누릅니다.
3. 성공 시 **「보호자 N건에게 명세 안내를 발송했습니다.」** 메시지가 표시됩니다 — **N은 연결 이용자 수**(동일 이용자 중복 라인은 1회만 발송, Q219). stub 환경은 `notifications` 이력만 생성 — **email·kakao·sms** 채널별, Q147·Q204).
4. **미납 관리**(`/billing/overdue`)에서도 행별 **「안내 발송」**으로 동일 API를 호출합니다.

> **조용한 시간대 (Q329, FE `111f056` / BE `39f5f4e`)**: **22:00~08:00 (Asia/Seoul)** 에는 **「보호자 발송」·「안내 발송」·「납부확인서 발송」** 버튼이 **비활성**됩니다. UI 우회 호출을 하더라도 BE가 수동 청구 발송 API(`POST /billing/claims/{id}/notify`, `POST /billing/claims/{id}/statement-dispatches`)를 **`422 BUSINESS_RULE`** 로 차단합니다(메시지: `현재 22:00~08:00 (Asia/Seoul) 조용한 시간대입니다...`). **긴급(`EMERGENCY`)** 알림(예: 낙상)은 **우회**됩니다 (Q147). **08:00 이후** 재시도하세요.

**납부확인서 재발송 (G2, FE `eedcc80`, Q221)**

1. 청구 상태가 **수납완료(`PAID`)** 이고 **입금일(`paidAt`)**·**입금 수단(`paymentMethod`)** 이 기록된 경우에만 **「납부확인서 발송」** 버튼이 표시됩니다 (Q249).
2. 버튼을 누르면 **`POST /billing/claims/{id}/payment-receipt-notify`** 가 호출되어 연결 보호자에게 **`BILLING_PAYMENT_RECEIVED`** 알림(이메일·알림톡·SMS preference별)을 **재발송**합니다.
3. 본문에는 **수납일·수납 수단(`CASH`/`BANK_TRANSFER`/`CMS`)·본인부담금**이 포함됩니다 (`588b8e6`).
4. **확정(`CONFIRMED`)만** 된 청구에서는 버튼이 **표시되지 않습니다** — 수납 완료 후 사용하세요.
5. 수납 직후 **자동 발송**(J03)이 이미 나갔어도, 보호자 요청 시 **수동 재발송**할 수 있습니다.

#### CMS 자동이체 (v2, US-L03, G2)

SideNav **청구** 그룹 — **`/billing/cms`** + 상단 **`BillingContextNav`**(입금↔미납↔CMS, Q203·Q208). **`hq_admin`·`branch_admin`** 전용.

| 화면 | UI | 백엔드 |
|------|-----|--------|
| CMS 자동이체 (`/billing/cms`) | **`CmsPage`** — **등록 관리**·**CMS 출금** 2탭 · **`CmsEnrollmentForm`·`CmsEnrollmentTable`·`CmsDebitPanel`** | **`POST/GET/DELETE /billing/cms/enrollments*`** · **`POST/GET /billing/cms/claims/{id}/debit`** |

**CMS 등록 절차 (UI, FE `9a6fdb6`·`d361833`·`3ece965`)**

1. **청구 → CMS 자동이체**로 이동합니다.
2. 상단 **`BranchScopeNotice`** 에서 **활성 지점**을 확인합니다 — 다지점 `hq_admin` 은 **BranchSwitcher**로 지점을 먼저 선택하세요 (Q638).
3. **등록 관리** 탭에서 **이용자**를 선택합니다.
   - **이용자를 선택하지 않으면** 활성 지점의 **CMS 등록 roster**가 표시됩니다 (케어포 7-4, Q637). **등록 상태 FilterChips**로 **전체·활성·해지·대기**를 전환합니다 (기본 **활성**, Q638).
   - roster 모드에서는 **이용자**·**예금주**·**은행**·**계좌**·**상태**·**등록일시** 열이 표시됩니다. **이용자명**을 클릭하면 해당 이용자 등록 화면(`?clientId=`)으로 이동합니다 (Q638). **ACTIVE** 행에서 **해지**할 수 있습니다.
   - **`/billing/payments`** 목록의 **「미등록 · CMS 등록」** 링크로도 동일 화면에 진입할 수 있습니다 (Q638).
4. **연결 보호자**·**예금주명**·**은행**·**계좌번호 끝 4자리**를 입력합니다 — ogada는 **전체 계좌번호를 저장하지 않습니다** (Q207).
5. **CMS 자동이체 등록**을 클릭합니다. 성공 시 하단 **등록 이력**에 **등록완료** Badge가 표시됩니다.
6. 보호자 **서면 자동이체 동의서**는 센터가 별도 보관합니다.
7. 동일 이용자에 **다른 보호자**로 이미 **ACTIVE** 등록이 있으면 **거부**됩니다 — 기존 등록을 **해지**한 뒤 재등록하세요 (Q299).

> **활성 지점 없음**: **「활성 지점을 먼저 선택한 후 CMS roster를 조회하세요.」** (Q638)  
> **Swagger — CMS 목록 (roster)**: **`GET /api/v1/billing/cms/enrollments?branchId=<uuid>&status=ACTIVE|CANCELLED|PENDING`** — **`clientId` 생략** 시 지점 roster · 응답에 **`clientName`** 포함 (Q637·Q638). **`status`** 는 서버에서 trim·uppercase 정규화 — **` pending `** 도 허용 (Q662).

**CMS 해지 절차 (UI, FE `9a6fdb6`, Q299)**

1. **등록 관리** 탭에서 이용자를 선택합니다.
2. **등록 이력** 표에서 **등록완료(`ACTIVE`)** 행의 **해지**를 클릭합니다.
3. **CMS 자동이체 해지** Modal에서 예금주·은행·계좌 끝 4자리를 확인하고 **해지 확인**을 누릅니다.
4. 성공 시 해당 행 상태가 **해지완료(`CANCELLED`)** 로 바뀝니다. **해지된 이력은 목록에 유지**됩니다 (감사·재등록 추적).
5. **출금 요청이 진행 중(`REQUESTED`)** 인 등록은 해지할 수 없습니다 — 출금 완료·실패 후 재시도하세요 (Q299).

> **재등록**: 해지 후 **동일 보호자·계좌**로 다시 등록하면 **기존 DB 행이 재활성화**됩니다 — 최초 등록 시각(`created_at`)은 보존됩니다 (Q207·`fee710d`).

**CMS 출금 절차 (UI, FE `6c6dc7a`·`c0a01b4`)**

1. **CMS 출금** 탭으로 전환합니다.
2. **확정(`CONFIRMED`)** 상태 청구 중 **ACTIVE CMS 등록**이 있는 이용자 건을 선택합니다.
3. **CMS 출금 요청**을 클릭합니다.
4. 성공 시 청구 **`PAID`**·`payment_method=CMS` (V59) · 보호자 **`BILLING_PAYMENT_RECEIVED`** 알림 (J03, Q147·Q272).
5. 출금에 성공한 청구는 **확정 목록에서 자동 제외**됩니다 (`c0a01b4`).
6. **실패 시** — 하단 **출금 상태**에 **출금실패** Badge·**실패 사유**가 표시됩니다. 청구는 **CONFIRMED 유지**이며 **재요청**할 수 있습니다 (Q256, `838a7f6`).

> **stub 환경 (Q208)**: **`FCMS_PROVIDER=stub`** — 실제 은행 출금 없이 **`StubFcmsClient`** 가 즉시 성공합니다. 패널 상단에 stub 안내가 표시됩니다. 효성 FCMS **실연동**은 운영 배포 시 `FCMS_*` 설정 후 활성화 (DEPLOYMENT §4-6).

> **Swagger — CMS 등록**

```json
POST /api/v1/billing/cms/enrollments
{
  "clientId": "<uuid>",
  "guardianUserId": "<uuid>",
  "payerName": "홍길동",
  "bankCode": "004",
  "accountLast4": "1234"
}
```

> **Swagger — CMS 해지**: **`DELETE /api/v1/billing/cms/enrollments/{enrollmentId}`** — **ACTIVE** 등록만 · 진행 중 출금 시 **`422`**.

> **Swagger — CMS 출금**: **`POST /api/v1/billing/cms/claims/{claimId}/debit`** — 선행: 이용자 **ACTIVE CMS 등록** · 청구 **CONFIRMED**.

#### 간편결제 (v2, US-L06, G2/7-5, BNK-189)

SideNav **청구** 그룹 — **`/billing/easy-pay`** + 상단 **`BillingContextNav`**(입금↔미납↔CMS↔간편결제, Q203·Q326). **`hq_admin`·`branch_admin`** 전용. 케어포 **7-5**(view.npay_manage)에 대응합니다.

| 화면 | UI | 백엔드 |
|------|-----|--------|
| 간편결제 (`/billing/easy-pay`) | **`EasyPayPage`** — **`EasyPayPanel`** — 확정 청구 선택 · **카드(CARD)·카카오페이(KAKAO_PAY)** · 연결 보호자(선택) · 결제 상태 **`StatusBadge`** · **필드 단위 검증·접근성**(US-L06) | **`POST/GET /billing/easy-pay/claims/{claimId}/payment`** · **alias `/claims/{claimId}`** (`438f5c7`·`8f9ad0c`·`9a4ab8e`) |

**간편결제 절차 (UI, FE `c9baca2`·`51f2505`)**

1. **청구 → 간편결제**(`/billing/easy-pay`)로 이동합니다.
2. **청구서** 드롭다운에서 **확정(`CONFIRMED`)**·미수납 청구를 선택합니다 — 이용자명·청구월·본인부담금이 표시됩니다. 미선택 시 **청구서** 필드 아래에 오류가 표시됩니다 (Q328).
3. 청구 선택 시 **선행입금 사전 점검**이 실행됩니다. **전월 미입금(`CONFIRMED`)** 또는 **G33 미정산**이 있으면 **`ClaimGenerationGuardBanner`**(「간편결제 제한 (7-5 선행입금 가드)」)가 표시되고 **「간편결제 요청」** 버튼이 **비활성**됩니다 (Q327). **입금 처리**·**미납 관리** 링크로 선행 수납을 완료하세요 — 월별 청구 생성 가드(Q310)와 **동일 규칙**입니다.
4. **결제 수단** — **카드** 또는 **카카오페이**를 선택합니다. 미선택 시 **결제 수단** 필드 아래에 오류가 표시됩니다.
5. (선택) **보호자** — 연결 보호자를 지정할 수 있습니다. 미지정 시 `guardianUserId` 없이 요청합니다.
6. **간편결제 요청**을 클릭합니다. 버튼은 stub 안내·가드 배너와 **`aria-describedby`** 로 연결되어 있습니다 (스크린 리더 사용자용, Q328).
7. **성공(`SUCCEEDED`)** 시 청구 **`PAID`**·`payment_method=EASY_PAY` · 보호자 **`BILLING_PAYMENT_RECEIVED`** 알림(J03). 하단 **「결제 상태」** 섹션에 PG 주문 ID·**요청·완료 시각**(`<time>` 요소)이 표시됩니다.
8. **실패(`FAILED`)** 시 — **실패 사유**가 표시됩니다. 청구는 **CONFIRMED 유지**이며 **재요청**할 수 있습니다 (이전 **`FAILED`** 건은 덮어씁니다).

> **stub 환경 (Q326)**: 현재 PG 연동은 **`StubEasyPayProvider`** — 실제 카드·카카오페이 결제창 없이 **즉시 성공** 시뮬레이션합니다. 패널 상단 footnote(`role="note"`)에 stub 안내가 표시됩니다. **live PG 벤더 연동**은 P2 후속(DEPLOYMENT §4-6-1).

> **퇴소·비활성 이용자 (Q328)**: 백엔드 **V110** DB 가드로 **퇴소·비활성 이용자** 청구에 대한 **신규** 간편결제 INSERT가 차단됩니다. UI 목록에는 확정 청구만 노출되므로 일반 운영에서는 해당되지 않습니다.

> **연말정산**: 간편결제(`EASY_PAY`) 수납분은 **의료비공제 집계에서 제외**됩니다 — CMS와 동일(Q254).

> **Swagger — 간편결제 요청**

```json
POST /api/v1/billing/easy-pay/claims/{claimId}/payment
{
  "provider": "CARD",
  "guardianUserId": "<uuid or null>"
}
```

> **provider 값**: API는 **`CARD`·`KAKAO_PAY`** 를 기대합니다. **허용 alias** — 대소문자·공백·하이픈(`" card "`, `"kakao pay"`, `"kakao-pay"`, `"KAKAOPAY"`, 전각 `ｋａｋａｏ pay`) → canonical 저장. **거부** — `card1`·`kakao/pay`·`카카오페이` 등 (Q328, `0cd8ea8`·`3dd94e6`·`745a2f6`·`82054f1`). FE **`normalizeEasyPayProvider`** 가 전송 전 정규화·검증합니다. **SUCCEEDED 재조회** 시 DB 비정규 provider **자동 정규화**됩니다 (QA-B93).

> **Swagger — 간편결제 상태**: **`GET /api/v1/billing/easy-pay/claims/{claimId}/payment`** — 선행: 청구 **CONFIRMED** · **단일 이용자** · **copay > 0** · **전월 미입금 없음**.

> **Swagger 우회 — 본인부담금 수납 (US-L01, BE Fixed)**

1. `/billing`에서 **확정(`CONFIRMED`)** 상태 청구의 `claimId`를 확인합니다.
2. Swagger **`POST /api/v1/billing/claims/{claimId}/payments`**:

```json
{
  "paidAt": "2026-06-08",
  "paymentMethod": "CASH",
  "amount": 150000
}
```

3. 성공 시 청구 **`PAID`** 전환·`paid_at`·`payment_method` 저장(V50) · 보호자 **`BILLING_PAYMENT_RECEIVED`** 알림 dispatch (J03, Q159).
4. **`amount` 생략** 시 본인부담금 전액 수납으로 처리합니다. **`amount` ≤ 0** 또는 **본인부담금과 불일치** 시 `422 BUSINESS_RULE` 거부됩니다 (Q218). **`DRAFT` 청구는 거부**됩니다.

> **미납 조회 (US-L02, Q197)**: Swagger **`GET /api/v1/billing/overdue?branchId=<uuid>&page=0&size=20&q=`** — 당월 이전 **`CONFIRMED`** 미수납 건. 응답 `items[]`: `claimId`, `clientName`, `yearMonth`, `copayAmount`, `daysOverdue`, `guardianPhoneMasked`, `lastReminderAt`.

> **우회 (기존)**: Swagger **`PATCH /api/v1/billing/claims/{id}/status`** `{ "status": "PAID" }` 또는 `/billing` 목록 **수납완료** 버튼(Q128) — 메타데이터(`paid_at`·`payment_method`) 없이 PAID만 전환.

청구 **상세**(`/billing/claims/:claimId`) — **`BillingDetailPage`** — **`DRAFT`** 시 **「공단 명세 비교」** (`BillingNhisComparisonPanel`, Q264) · **`CONFIRMED`/`PAID`** 시 **「명세 4채널 발송」** 카드 — **`BillingStatementDispatchPanel`** (케어포 PDF p.87 ①, G-7-1-4CHANNEL, Q364) · **「명세 인쇄 산출물 (7-1)」** 카드 — **`BillingStatementPrintPanel`** (케어포 PDF p.87 ②, G-7-1, Q475) · 요약·급여 항목에 **이용시간대** 표시 — **`resolveClaimDurationBand`** · 확정·수납 시 **「보호자 발송」**(Q196)·상태 변경·인쇄.

#### 4-6-0. 본인부담금 명세 4채널 발송 (G-7-1-4CHANNEL, Q364)

케어포 **7-1** 「본인부담금 명세서 발송」에 대응합니다. 청구가 **확정(`CONFIRMED`) 또는 수납완료(`PAID`)** 이고 급여 항목이 있을 때만 표시됩니다 (`1fd1434`).

1. **청구** 목록에서 해당 월 청구 **상세**로 이동합니다.
2. **「명세 4채널 발송」** 카드에서 **발송 채널**을 선택합니다 — **우편** · **문자** · **이메일** · **직접수령**.
3. 청구에 포함된 **이용자**를 체크하고 **일괄 발송**을 누릅니다.
4. **우편** 채널만 **발송일**을 지정·수정할 수 있습니다. **문자·이메일**은 발송 시점이 자동 기록되며 이후 수정할 수 없습니다.
5. **J03 quiet-hours**(22:00~08:00 KST) 중 **문자·이메일** 발송은 비활성화됩니다 — 우편·직접수령은 가능합니다 (Q329).

> **보호자 일괄 알림**(`POST /claims/{id}/notify`, Q196)과 **별도** — 4채널 발송은 **명세서 전달 경로** 기록용입니다.

#### 4-6-0-1. 본인부담금 명세 인쇄 산출물 (G-7-1, Q475)

케어포 **7-1** 「본인부담금 청구관리」의 **② 인쇄 산출물**에 대응합니다. **4채널 발송(§4-6-0)** 과 **별도 카드**이며, **인쇄·PDF 다운로드 전용**입니다 (`50d330d`).

1. **청구** 목록에서 **확정(`CONFIRMED`) 또는 수납완료(`PAID`)** 청구 **상세**로 이동합니다.
2. **「명세 인쇄 산출물 (7-1)」** 카드에서 이용자별 인쇄 데이터를 불러옵니다 (급여 항목·이용자 주소).
3. 아래 버튼 중 필요한 산출물을 선택합니다:
   - **주소라벨 인쇄** — 보호자 수신·우편 주소 라벨
   - **급여비용명세서 인쇄** — 이용자별 본인부담·공단부담·등급·이용시간대 표
   - **영수증 인쇄** — **`PAID`+`paidAt`** 청구만 가능 (미수납 시 버튼 비활성·info Alert·스크린 리더 **`aria-describedby`** 연결, Q485, `265fc42`)
   - **청구리스트 인쇄** — 당월 청구 이용자 목록
   - **전체 일괄 인쇄** — 주소라벨·명세서·청구리스트(+ **수납 완료 시 영수증**)를 한 번에 Print Dialog로 출력. **`CONFIRMED`(미수납)** 청구는 버튼 라벨이 **「전체 일괄 인쇄 (영수증 제외)」** 로 표시되며, **영수증 불가 안내 Alert**와 **`aria-describedby`** 로 연결됩니다 (Q478·Q485, `f5639df`/`265fc42`).
   - **명세서 PDF 다운로드** — 서버 생성 PDF 파일 저장 (`downloadBillingClaimStatementPdfApi`). 스크린 리더용 **`aria-label`「급여비용명세서 PDF 다운로드」** (Q538, UXD-140, FE `501fedc`).
5. **Excel(CSV) 다운로드** (케어포 PDF p.87 ② **엑셀다운로드**, Q535, FE `58d6694`·BE `e454d3b`):
   - 인쇄 버튼 아래 **「명세 Excel 다운로드」** 행에서 **주소라벨·급여비용명세서·영수증·청구리스트·전체 Excel** 중 선택합니다.
   - **미수납(`CONFIRMED`)** 청구는 **영수증 Excel**이 비활성이며, **전체 Excel** 라벨은 **「(영수증 제외)」** 로 표시됩니다 (인쇄와 동일 규칙).
   - 파일은 **UTF-8 CSV(BOM)** 이며 Excel에서 바로 열 수 있습니다.
6. 브라우저 **인쇄 대화상자**(`Ctrl+P` / `Cmd+P`)에서 프린터·용지를 선택합니다.

> **발송 vs 인쇄**: **4채널 발송**은 우편·문자·이메일·직접수령 **기록** · **인쇄 산출물**은 **물리 출력·PDF 보관**용입니다. 두 패널을 **동시에** 사용할 수 있습니다 (Q475).

| 대사 상태 | 의미 | 조치 |
|----------|------|------|
| `MATCHED` | 공단 데이터와 ogada 이용자·청구 일치 | — |
| `UNMATCHED` | 이용자 자동 매칭 실패 | 인정번호·이름 확인 → **수동 연결** |
| `DISCREPANCY` | 이용자는 매칭되었으나 일수·금액 불일치 | 출석·등급 재점검 · **「비교」** Modal |
| `PENDING_REVIEW` | 공단 처리 **대기·보류** (G7, Q181) | 심사 완료 후 **엑셀 재import** — 수동 연결 불가 |

#### 4-6-1. NHIS `UNMATCHED` 수동 매칭

자동 매칭(인정번호·이름·생년월일)에 실패한 공단 엑셀 행을 이용자와 연결하는 절차입니다.

> **UI (FE `c30aaac`·`42f48e1`·`190b2b1`·`1220bfb`·`2b6024a`·`0abf164`, BE `9a97a1c`·`970c7af`·`8f208e4`·`2edbdc4`)**: `/billing/imports/nhis` — 월·파일 업로드 + **`NhisImportGuidePanel`**(Chrome/Edge·4단계 + **`GET /billing/imports/nhis/guidance` 실서버 안내**, QA-B24, Q133) + **`NhisScheduleConfirmLockGuide`** + **`FeeScheduleYearGuardBanner`**(US-G04, Q260) + **`fetchFeeScheduleYearCoverageApi`** 서버 사전 점검 + 배치 목록·대사 (`ReconciliationPage`). guidance API 일시 실패 시 **기존 실서버 안내 문구 유지** (`Promise.allSettled`).

> **처리상태 헤더 (BE `2edbdc4`, Q582)**: 롱텀 export xlsx의 **「처리상태」** 열(BOM·탭·영문 alias 포함)은 **`NhisExcelParser`** 가 자동 매핑합니다. `대기`·`보류` 행은 **`PENDING_REVIEW`** 로 표시되며 수동 연결 전 **공단 심사 완료 후 재import** 하세요 (Q181).

> **PC 에이전트 불필요 (G7, Q405)**: ogada는 이지케어 **「이지링크(EzLink)」** 같은 **설치형 공단 연동 프로그램 없이**, 롱텀 등에서 다운로드한 **엑셀을 브라우저에서 업로드**하는 **web-first** 방식입니다.

0. **청구 확정 잠금 (G21, Q209)**: 선택 **청구 월**에 **확정·수납(`CONFIRMED`/`PAID`)** 청구가 있으면 **업로드가 비활성**됩니다. 안내 패널 **「청구 확정 잠금 (주간보호)」** — 롱텀 엑셀 → import·대사 → 금액 확인 → **`/billing` 확정** → 재import 주의(이지케어 FAQ 21474). 재업로드가 필요하면 **대사 보정** 또는 해당 월 청구 상태를 IT와 협의하세요.

0-1. **수가표 연도 가드 (US-G04, Q260·Q392)**: 선택 **청구 월의 연도**에 **등급(1~5)×이용시간대 25칸** 수가표가 모두 등록되지 않으면 **`FeeScheduleYearGuardBanner`** warning이 표시되고 **업로드가 비활성**됩니다. 배너·업로드 차단 오류는 **`GET /billing/fee-schedules/year-coverage?year=`** 응답 **`message`** 를 **우선 표시**합니다 — 예: `{year}년 수가표가 {n}/25칸만 등록되어 있습니다` (`57114b8`, Q392). **인지지원등급(ltcGrade 0) 5칸**은 **별도 집계**(`cognitiveRegistered`/`cognitiveComplete`, Q311) — **NHIS import gate는 표준 25칸만** 검사합니다. API **로딩 중·오류** 시에도 업로드를 차단합니다. **「수가표 등록」** 링크(`/billing/fee-schedules`)에서 **「공단 2026 수가 시드」** 또는 셀별 등록 후 재시도하세요. **`POST /billing/imports/nhis`** 도 동일 규칙으로 **`422`**를 반환합니다 (`970c7af`·`8f208e4`).

1. **청구**(`/billing`) → **「NHIS 엑셀 import (P7)」** → `/billing/imports/nhis`.
2. **청구 월**·엑셀 파일 선택 후 **업로드** (0·0-1번 조건 충족 시).
3. import **배치 목록**에서 해당 배치 링크 → **reconciliation** (`/billing/imports/nhis/:batchId`).
4. **`NhisScheduleConfirmLockGuide`** 로 해당 배치 월의 **확정·수납 청구 건수**를 확인합니다 — locked 시 **재import 경고**만 표시되며, 아래 **수동 매칭은 계속** 가능합니다 (Q209).
5. 상단 **매칭 상태 요약**(StatCard)에서 **일치·차이·미매칭·대기(보류)** 건수를 확인합니다 (UXD-58, Q182).
6. **대기(보류) 행**이 1건 이상이면 **`NhisPendingReviewGuide`** 안내가 표시됩니다 — 공단 심사 완료 후 엑셀을 **재import**하세요. 수동 연결은 **미매칭** 행에서만 진행합니다 (Q181).
7. **`UNMATCHED`** 행이 있으면 하단 **수동 연결** 폼을 사용합니다 (FE `f01e3a8`, UXD-43).
   - **미매칭 행** 드롭다운에서 대상 행 선택.
   - **후보 이용자 검색**(`SearchInput`)에 이름·인정번호 입력 → `GET …/candidates?q=` 후보 목록 갱신.
   - **매칭 이용자** 선택 후 **수동 연결** — `PATCH …/rows/{rowId}/match`.
   - **`NhisReconciliationTable`** — `MATCHED`/`DISCREPANCY`/`UNMATCHED`/**`PENDING_REVIEW`** **상태 Badge**·**「보류 사유」**열(`matchStatusReason`)·차이 금액·일수 강조 (UXD-39·UXD-58, G7 Q181). **`PENDING_REVIEW`** 행은 안내 문구만 표시하고 수동 연결·비교 버튼이 없습니다.
8. **`DISCREPANCY`**(일수·금액 불일치) 행은 **「비교」** 버튼을 눌러 **`DiscrepancyComparePanel`** Modal을 엽니다 (US-G06, FE `fd4e8f3`).
   - 공단(NHIS) vs ogada **청구액·이용일수**를 표로 비교합니다. 차이는 **「공단 초과/부족」** 텍스트 Badge와 함께 표시됩니다 (색상만으로 구분하지 않음).
   - `claimId`가 연결된 행은 Modal 하단 **「ogada 청구 라인 상세 보기」** 링크로 `/billing/claims/{claimId}` 이동이 가능합니다.
   - 숫자가 `-`로 비면 API 필드 매핑 갭(Q101) — 출석·등급을 재점검하세요.

> **주의**: 수동 연결은 **단일 트랜잭션**으로 처리됩니다. 다른 지점 소속 이용자는 연결할 수 없습니다 (V21 지점 일치 검증).

| API 상태 코드 | 화면 표기 | 의미 |
|--------------|----------|------|
| `DRAFT` | 작성중 | 검토·수정 가능 |
| `CONFIRMED` | 확정 | 명세서 출력·공단 청구 기준 확정 |
| `PAID` | 수납완료 | 본인부담금 수납 처리 완료 |

### 4-7. 직원·계정 (`/staff`, v3 §3-8)

센터장·통합 관리자는 SideNav **운영 → 직원 관리**(`/staff`)에서 소속 지점 **직원 목록 조회**와 **계정 생성 요청**이 가능합니다 (FE `22718d0`, FAQ **Q555**). **즉시 계정 생성은 ogada 플랫폼 승인 후** 이루어집니다.

1. **직원 관리** 화면에서 등록된 직원 목록(이름·이메일·역할·소속 지점·lifecycle)을 확인합니다.
2. **+ 계정 생성 요청**을 눌러 모달에서 **이름**·**이메일**·**역할**(`StaffRoleSelect` — 요양보호사·사회복지사·지점장·통합 관리자)을 입력합니다. **소속 지점**은 미입력 시 현재 활성 지점이 적용됩니다.
3. 제출하면 **「계정 생성 요청이 접수되었습니다. ogada 승인 후 발급됩니다.」** 안내가 표시됩니다. 하단 **「계정 생성 요청」** 카드에서 **대기·승인·반려** 상태를 확인합니다.
4. 이름·이메일 미입력 시 **필드 아래 오류**가 표시됩니다. 저장 중에는 버튼에 **요청 중** 스피너가 표시됩니다.
5. 퇴직 처리·역할 변경은 **직원 상세** 또는 Swagger `PATCH /api/v1/users/{id}` 사용 (ADMIN_GUIDE §6-4).

| API | 용도 |
|-----|------|
| `GET /api/v1/users?page=0&size=50` | 직원 목록 |
| `GET /api/v1/users/account-requests` | 본 Tenant 계정 요청 목록 |
| `POST /api/v1/users/account-requests` | 계정 생성 요청 (`displayName`·`roleCode`·`branchIds`) |
| `POST /api/v1/staff/imports/nhis-caregivers/preview` | 공단 요양보호사 엑셀 **미리보기** (`branchId` + `file`, Q573) |
| `POST /api/v1/staff/imports/nhis-caregivers` | 미리보기 후 **선택 행** 계정 요청 등록 (`rowNumbers` 선택, Q573) |

#### 4-7-0. 공단 요양보호사 엑셀 일괄 계정 요청 (G-STAFF-NHIS-EXCEL-IMPORT, Q573)

케어포 **8-1-2** 와 같이 공단(NHIS)에서 받은 **요양보호사 정보 엑셀**로 직원 계정 요청을 한꺼번에 등록할 수 있습니다 (`hq_admin`·`branch_admin`).

1. **운영 → 직원 관리**(`/staff`) 상단 **「공단 요양보호사 엑셀 업로드」** 카드를 확인합니다.
2. **요양보호사 엑셀 (.xlsx)** 파일을 선택하고 **「미리보기」**를 클릭합니다.
3. 표에서 **행·성명·생년월일·인력번호·이메일·상태**를 확인합니다.

| 미리보기 상태 | 의미 | 조치 |
|--------------|------|------|
| `APPLIED` (등록 가능) | 신규 계정 요청 가능 | 체크박스 선택 후 **「선택 행 등록」** |
| `MATCHED` (기등록) | 동일 이메일·이미 `users` 존재 | — |
| `PENDING` (요청 대기) | 동일 이메일·승인 대기 중 | 플랫폼 승인 후 재시도 |
| `SKIPPED` / `INVALID` / `DUPLICATE` | 필수값 누락·형식 오류·중복 | 엑셀 수정 후 재업로드 |

4. **「등록 가능 행 전체 선택」** 또는 개별 체크 후 **「선택 행 등록 (N건)」** — **`POST /api/v1/staff/imports/nhis-caregivers`** 가 **`user_account_requests` PENDING** 으로 적재합니다 (V162·**V165** integrity). 등록 성공 시 **계정 요청 탭 목록이 자동 갱신**됩니다 (`onImported`, Q577).
5. 이후 **`ogada_platform_admin`** 이 **`/platform`** 에서 승인하면 계정이 발급됩니다 (§4-7·Q555).

> **주의**: 미리보기 없이 일괄 등록하지 마세요. **선택 행이 0건**이면 화면에 **「등록할 행을 최소 1개 이상 선택해 주세요.」** 가 표시되고, API에 빈 `rowNumbers`를내면 **`422`「선택된 행이 없습니다.」** (Q576). **이메일 형식·역할(`caregiver`)** 은 서버가 검증하며, 실패 행은 `message` 열에 사유가 표시됩니다. 미리보기 표·체크박스는 **UXD-146** (`a7d9a2f`) — 행별 **`aria-label`**·**`aria-busy`** (Q581).

> **`ogada_platform_admin` 역할은 생성·요청 불가** (Q556). **`displayName`·`roleCode`** 필드명은 BE DTO와 **동기화 Fixed** (Q162 closure @ `22718d0`).

#### 4-7-0a. 직원 연차휴가 현황 (G-STAFF-ANNUAL-LEAVE, US-R03e, Q639)

이지케어 **worker-b100 tab01 「연차휴가 현황」** 과 동일하게, 지점 직원의 **연차 부여·월별 사용·잔여일**을 한 화면에서 관리합니다 (`3902dba`/`41fb84f`).

1. **운영 → 직원 관리** 상단 **`StaffContextNav`** 에서 **「연차휴가 (US-R03e)」** 를 선택하거나 **`/staff/annual-leaves`** 로 직접 이동합니다. 페이지 제목(AppShell `<h1>`)은 **「직원 연차휴가」** 입니다 (`STAFF_ANNUAL_LEAVE_PAGE_TITLE`, Q643).
2. **`StaffContextNav`** 아래 **`BranchScopeNotice`** 로 **조회 지점**을 확인합니다 — 다지점 `hq_admin`·`branch_admin` 은 **지점 선택기** 전환 후 **「조회」** 하세요 (Q657, `949e9bf`).
3. 표 상단 **「연차휴가 관련 화면」** 패널을 확인합니다 (`StaffAnnualLeaveRelatedSurfacesPanel` → **`RelatedSurfacesPanel`**, Q650·Q657). **「이 화면은 월별 사용일 스냅샷입니다…」** 안내 아래 **「출퇴근 기록」** 링크로 **`/staff/attendance`** · **「연차·유급휴일 대장」** 링크로 **`/staff/leave-ledger`** 로 이동할 수 있습니다 (Q666).
4. **기준 연도**를 선택하고 **「조회」** 를 누릅니다 (전년·당해·익년 선택 가능).
5. 표에서 **직원명·소속·입사일·1~12월 사용·연차 부여·사용 합계·잔여·비고**를 확인합니다. 상단 StatCard에 **대상 직원·사용 합계·잔여 합계**가 표시됩니다.
6. **`branch_admin`·`social_worker`** 는 행 **「수정」** 으로 Modal을 열어 **연차 부여(일)** · **월별 사용(일)**(12칸 **fieldset** 그룹) · **비고**를 입력 후 **저장**합니다. **`hq_admin`** 은 **조회만** 가능합니다. 상단 **안내 문구(`ds-help-text`)** 와 **조회·저장 `aria-busy`** 로 로딩 상태를 확인할 수 있습니다 (UXD-155, Q646).
7. 입력 오류(음수·소수·합계 초과·비고 초과)는 **해당 필드 아래**에, 서버 **`422`** 는 Modal 상단 **Alert** 또는 **필드별 오류**로 표시됩니다. 값을 수정하면 해당 필드 오류가 **자동으로 지워지고**, **마지막 필드 오류가 해제되면 Alert도 함께 사라집니다** — **비고(`memo`) 입력 시에도 동일** (Q647·`96e9d25`).
8. 저장 성공 시 **「{직원명} 연차휴가를 저장했습니다.」** 안내가 표시되고 roster가 갱신됩니다.

| API | 용도 |
|-----|------|
| `GET /api/v1/staff/annual-leaves/roster?year=2026&branchId=` | 지점 활성 직원 roster · **`surfaceKind=ANNUAL_LEAVE_USAGE_SNAPSHOT`** · **`relatedSurfaces[]`** US-R01 cross-link (Q648) |
| `GET /api/v1/staff/annual-leaves/users/{userId}?year=2026` | 1명 연간 레코드 · **동일 `surfaceKind`·`relatedSurfaces[]`** (Q650, `6ab3760`) |
| `GET /api/v1/staff/annual-leaves/roster?year=2026` | **`branchId` 생략** — JWT **활성 지점(`activeBranchId`)** roster · **다지점 `branch_admin`** 도 **`TenantContext.activeBranchId`** fallback (`6b84bcd`·`40ab9e7`, Q639·Q656) |
| `PUT /api/v1/staff/annual-leaves/users/{userId}` | `{ year, monthlyUsage[], totalEntitlement, memo }` 저장 · 응답에 **cross-link 메타** 포함 (Q650) |

> **연관 화면 (Q648·Q650·Q651·Q652·Q653·Q663·Q666)**: roster는 **월별 사용 스냅샷**입니다. 패널의 **출퇴근 기록**은 **`/staff/attendance`**, **연차·유급휴일 대장**은 **`/staff/leave-ledger`** 로 canonical 데이터가 분리됩니다 — roster만으로 대장 전체를 대체하지 않습니다.

#### 4-7-0b. 직원 HR 화면 역할 분리·양방향 탐색 (US-R01·US-R03e, Q652)

출퇴근·연차·대장은 **서로 다른 데이터**를 담습니다. 현장에서 「어느 화면에 무엇을 입력해야 하나?」를 빠르게 판단할 때 아래 표를 사용하세요.

| 업무 | 이동 경로 | 입력·조회 내용 | 관련 링크 패널 |
|------|----------|----------------|----------------|
| **오늘 출근·퇴근 기록** | `/staff/attendance` | 직원별 당일 출근/퇴근 시각·출근 방식 | **「연차휴가 현황」** → `/staff/annual-leaves` |
| **연차 부여·월별 사용** | `/staff/annual-leaves` | 연차 부여일·1~12월 사용·잔여·비고 | **「출퇴근 기록」** → `/staff/attendance` |
| **건별 휴가·유급휴일 대장** | **`/staff/leave-ledger`** | canonical leave-ledger (`bb9df48`/`8057c1e`, Q663·Q666) | **연차·출퇴근 패널 AVAILABLE 링크** · **`StaffContextNav` 3탭** |

**양방향 탐색 흐름**

1. **출퇴근 → 연차**: `/staff/attendance` 상단 **「출퇴근 관련 화면」** — **「연차휴가 현황」** 클릭 (Q651).
2. **연차 → 출퇴근**: `/staff/annual-leaves` 상단 **「연차휴가 관련 화면」** — **「출퇴근 기록」** 클릭 (Q650).
3. **대장**: **`/staff/leave-ledger`** — **「항목 등록」** 으로 건별 휴가·유급휴일 등록 (Q666). **`branch_admin`/`social_worker`** 만 등록·수정·삭제 가능. 월별 roster만으로 대장을 대체하지 마세요.

| 안내 문구 (화면별) | 상수 |
|-------------------|------|
| 연차 화면 | **`STAFF_ANNUAL_LEAVE_SNAPSHOT_HELP`** — 「이 화면은 월별 사용일 스냅샷입니다…」 |
| 출퇴근 화면 | **`STAFF_WORK_ATTENDANCE_CROSS_LINK_HELP`** — 「일별 출퇴근은 이 화면에서 기록합니다…」 |

| API `surfaceKind` | 화면 | cross-link 출처 |
|-------------------|------|----------------|
| **`ANNUAL_LEAVE_USAGE_SNAPSHOT`** | `/staff/annual-leaves` | roster·yearly GET/PUT (`bbf333c`/`6ab3760`, Q648·Q650) |
| **`DAILY_WORK_ATTENDANCE_ROSTER`** | `/staff/attendance` | **`GET /staff/work-attendance`** (`83a26e7`, Q653) |

> 관련: FAQ **Q648·Q650·Q651·Q652·Q653** · ADMIN_GUIDE §1-4·§6-2-20·§6-2-23 · USER_MANUAL §5-3

#### 4-7-0c. 연차·유급휴일 대장 (US-R01 · US-R01-c, Q655·Q659·Q663·Q666·Q667)

**화면 `/staff/leave-ledger`와 백엔드 API가 연동**되었습니다 (`8057c1e`/`bd1d0ad`/`5fd12dd`, Q666·Q667). Swagger-only fallback은 API 장애 시에만 사용하세요.

**정보 모델 분리 (중복 입력 금지)**

| 유형 | 화면 / API | 저장 내용 |
|------|------------|----------|
| **월별 스냅샷** | `/staff/annual-leaves` | 1~12월 **사용일 합계**·부여·잔여·비고 (`ANNUAL_LEAVE_USAGE_SNAPSHOT`) |
| **일별 출퇴근** | `/staff/attendance` | 당일 출근·퇴근·방식 (`DAILY_WORK_ATTENDANCE_ROSTER`) |
| **건별 대장** | **`/staff/leave-ledger`** | 휴가·유급휴일 **건별 원장** (`CANONICAL_LEAVE_LEDGER`) |

연차·출퇴근 화면 패널의 **「연차·유급휴일 대장」** 링크는 **`/staff/leave-ledger`** 로 이동합니다 (Q666).

**화면 조작 (센터장·사회복지사)**

1. **`/staff/leave-ledger`** — **`StaffContextNav`「연차·유급휴일 대장」** 또는 연차·출퇴근 패널 cross-link.
2. 상단 **`BranchScopeNotice`** 로 조회 지점을 확인합니다.
3. **「기준 연도」** 선택 → **「조회」** — 해당 연도·지점 건별 목록 **`StaffLeaveLedgerTable`**.
4. **`branch_admin`/`social_worker`** — **「항목 등록」**:
   - **직원** · **휴가 유형**(연차/유급휴일) · **`DateInput` 시작일** · **`DateInput` 종료일**(선택) · **사용일수** · **비고**
   - FE **`validateStaffLeaveLedgerForm`** 이 필드 오류를 Modal에 표시 · 서버 **`422`** 는 필드별 매핑
5. Table **「수정」/「삭제」** — 삭제 시 **`StaffLeaveLedgerDeleteModal`** 로 확인합니다 (`window.confirm` 미사용, UXD-157, Q667).
6. **`hq_admin`** — 목록 **조회만** (등록·수정·삭제 버튼 없음, Q665).
7. **`caregiver`** — 대장 API **403** (Route 접근 제한).

**접근성 (UXD-157, Q667)**: 표에 **시각적으로 숨긴 caption**이 있어 스크린리더가 「연도 직원 연차·유급휴일 대장」임을 안내합니다. 날짜 열은 **`<time>`** 요소로 읽힙니다. 직원명 링크·행 버튼에는 **맥락 `aria-label`** 이 붙습니다.

**관련 화면 패널**: **`StaffLeaveLedgerRelatedSurfacesPanel`** — **「연차휴가 현황」** · **「출퇴근 기록」** 링크.

**Swagger 조작 요약 (API 장애·통합 관리자 감사 시)**

1. **Authorize** — `branch_admin` 또는 `social_worker` JWT.
2. **목록** — `GET /api/v1/staff/leave-ledger?year=2026&branchId=<uuid>`.
3. **등록** — `POST /api/v1/staff/leave-ledger/users/{userId}`:

```json
{
  "leaveType": "ANNUAL_LEAVE",
  "leaveDate": "2026-06-10",
  "endDate": "2026-06-10",
  "daysUsed": 1,
  "memo": "개인사유"
}
```

4. **수정** — `PUT /api/v1/staff/leave-ledger/entries/{entryId}` · **삭제** — `DELETE …/entries/{entryId}` (**204**).

| 검증 오류 | 메시지 예 |
|-----------|----------|
| 미지원 `leaveType` | **`422`「휴가 유형은 연차(ANNUAL_LEAVE) 또는 유급휴일(PAID_HOLIDAY)이어야 합니다.」** |
| `endDate` 역전 | **`422`「종료일은 시작일보다 빠를 수 없습니다.」** |
| `daysUsed` 범위 | **`422`「사용일수는 0보다 커야 합니다.」** 등 |

> 관련: FAQ **Q667·Q666·Q663·Q655·Q654** · USER_MANUAL §4-7-0b·§4-7-0d · REQUIREMENTS US-R01-c

#### 4-7-0d. 연차·유급휴일 대장 API 상세 (US-R01-c, Q663·Q665·Q668)

| API | 권한 | 설명 |
|-----|------|------|
| `GET /api/v1/staff/leave-ledger?year=&branchId=` | `hq_admin`·`branch_admin`·`social_worker` | 지점·연도별 건별 목록 · **`entryCount`** · **`surfaceKind=CANONICAL_LEAVE_LEDGER`** |
| `GET /api/v1/staff/leave-ledger/users/{userId}?year=` | 동일 | 직원 1명 연간 대장 |
| `POST /api/v1/staff/leave-ledger/users/{userId}` | `branch_admin`·`social_worker` | 건별 행 생성 — **`hq_admin`·`caregiver` → 403** |
| `PUT /api/v1/staff/leave-ledger/entries/{entryId}` | 동일 | 행 수정 |
| `DELETE /api/v1/staff/leave-ledger/entries/{entryId}` | 동일 | 행 삭제 |

> **역할 안내 (Q665·Q669)**: **통합 관리자(`hq_admin`)** 는 **조회·감사만** 가능하고 등록·수정·삭제는 **센터장·사회복지사**가 수행합니다. **사회복지사**는 **`GET /api/v1/users`** 로 **직원 목록 조회**가 가능합니다(등록·수정 불가). **요양보호사(`caregiver`)** 는 대장 API에 접근할 수 없습니다.

**응답 항목 (`items[]`)**: `id` · `userId` · `displayName` · `leaveType` · `leaveDate` · `endDate` · `daysUsed` · `memo` · `recordedBy` · `updatedAt`

**DB**: Flyway **V174** `staff_leave_ledger_entries` — org/branch/user FK · `leave_type` CHECK · `days_used` 0<≤99.9 CHECK · **V175** — **`memo` 공백-only 거부 CHECK** · **`user_branches` 배정 FK** (`c4e6bcb`, Q668).

> **V175 운영**: 직원이 **해당 지점에 배정되지 않으면** 대장 행 저장이 **DB에서 거부**됩니다 — **`/staff`** 에서 지점 배정을 먼저 확인하세요. **비고**는 공백만 입력하지 마세요.

> 관련: FAQ Q663·Q665·Q668·Q669 · ADMIN_GUIDE §6-2-24 · DEPLOYMENT_GUIDE §1-4

> **검증**: **월별 사용일수가 0 미만**이면 **`422`「월별 사용일수는 0 이상이어야 합니다.」** (`a45745c`, FAQ Q639). **소수점**(예: 0.5)이면 **`422`「월별 사용일수는 정수여야 합니다.」** (Q641) — Modal **`validateStaffAnnualLeaveForm`** 이 필드별로 먼저 표시합니다 (Q647). **비고(`memo`) 31자 이상**이면 **`422`「비고는 30자 이하여야 합니다.」** (Q642). 월별 사용 합계가 **연차 부여일을 초과**하면 **`422`「월별 사용일 합계가 연차 총 부여일수를 초과할 수 없습니다.」** (FAQ Q639). **다지점 `branch_admin`** 이 지점을 선택하지 않으면 **`branchId` 생략 시 `422`** — FAQ Q639. **Flyway V172** `staff_annual_leave_yearly` + **V173** defense-in-depth CHECK/FK (Q645)에 persist됩니다.

- **보호자 알림 수신 설정 대리 변경** — §4-7-1 참고 (**API만**, UI 후속, FAQ Q137-1).

#### 4-7-1. 보호자 알림 수신 설정 대리 (B08, API-only)

보호자가 스마트폰·이메일 알림을 받을 채널을 **센터 직원이 대신 설정**할 수 있습니다. v1.1에서는 **화면 UI가 없으며** Swagger 또는 Postman으로 호출합니다.

| 항목 | 내용 |
|------|------|
| 권한 | `branch_admin`, `social_worker` (연결된 이용자·보호자·지점 스코프 검증) |
| 조회 | `GET /api/v1/clients/{clientId}/guardians/{guardianUserId}/notification-preferences` |
| 저장 | `PUT /api/v1/clients/{clientId}/guardians/{guardianUserId}/notification-preferences` |

**설정 절차 (Swagger)**

1. 이용자 상세에서 **연결 보호자 UUID**(`guardianUserId`)를 확인합니다.
2. Swagger **Authorize**에 `branch_admin` 또는 `social_worker` JWT를 입력합니다.
3. **GET**으로 현재 설정을 조회합니다 — 채널: 인앱·Web Push·이메일·카카오 알림톡·SMS.
4. **PUT** 본문 예시:

```json
{
  "channelInApp": true,
  "channelPush": false,
  "channelEmail": true,
  "channelKakao": false,
  "channelSms": false,
  "notifyAttendance": true,
  "notifyDailyCare": true,
  "notifyBilling": false,
  "notifyEmergency": true
}
```

5. **카카오·SMS를 켤 때**는 보호자 **동의 시각(`consent_at`)**이 DB에 기록되어야 합니다 (V42 CHECK, FAQ Q142).
6. 보호자 본인은 `GET/PUT /api/v1/guardian/notification-preferences`로 자가 설정할 수 있습니다.

> **발송**: 출석·**바이탈·투약**·청구 기록 시 **J03** `NotificationService`가 연결 보호자에게 dispatch 시도 — **`channelEmail`**(BE `fbedcc3`, Q204) · **알림톡/SMS stub provider**(실제 외부 발송 없음, FAQ Q147·Q148).

#### 4-7-2. 알림 발송 이력 조회 (J03, US-J03-h Fixed)

보호자·직원이 **알림톡/SMS 발송 이력**을 화면에서 확인할 수 있습니다 (FE `e39164d`, BNK-22, FAQ **Q152·Q187**).

| 대상 | 화면 | API | 권한 |
|------|------|-----|------|
| 보호자 본인 | `/guardian` → **「알림 이력」** 탭 | `GET /api/v1/guardian/notifications?page=0&size=20` | `guardian` |
| 직원(이용자별) | `/clients/:id` → **「보호자 알림 이력 (US-J03)」** 카드 | `GET /api/v1/clients/{clientId}/notifications?page=0&size=20` | `branch_admin`, `social_worker` |

**표시 항목**: 발송 시각 · 채널(**EMAIL**·KAKAO·SMS) · 유형(출석·일일 케어·**급여제공기록지**·**가정통신문**·본인부담금·입금 확인·긴급) · 상태. **수신 연락처는 개인정보 보호를 위해 표시하지 않습니다.**

1. 보호자는 포털 하단 **「알림 이력」** 탭을 선택합니다.
2. 직원은 이용자 상세 **기본정보** 탭 아래 **「보호자 알림 이력」** 카드를 확인합니다.
3. stub 환경·알림톡 미연동 시 목록이 비어 있을 수 있습니다 — 출석 체크인 후 다시 조회하세요 (Q147).
4. API 오류 시 Swagger로 동일 엔드포인트를 확인할 수 있습니다.

#### 4-7-3. 보호자 서류 이메일 발송 (G2)

케어포·엔젤 패리티 **보호자 서류 5종** 중 **노인학대예방 지침·가정통신문·급여제공기록지**는 이용자 상세 **`GuardianDocumentNotifyPanel`** 에서 발송합니다 (FE `d1149a5`, FAQ **Q217·Q222·Q517 Fixed**). **납부확인서**는 청구 상세 **「납부확인서 발송」**(Q221).

| 서류 | 화면 | API | 템플릿 |
|------|------|-----|--------|
| 급여제공기록지 | **「급여제공」탭 조회** (Q243) · **기본정보 탭 발송** (Q517) | `GET …/care-provision-records/{yearMonth}` · `POST …/notifications/care-provision-record` | `CARE_PROVISION_RECORD` |
| 가정통신문 | **`GuardianDocumentNotifyPanel`** — 문서 유형 **가정통신문** | `POST /api/v1/clients/{clientId}/notifications/home-newsletter` | `HOME_NEWSLETTER` |
| **노인학대예방 및 대응지침** | **`GuardianDocumentNotifyPanel`** — 문서 유형 **노인학대예방** | `POST /api/v1/clients/{clientId}/notifications/elder-abuse-prevention-guideline` | `ELDER_ABUSE_PREVENTION_GUIDELINE` |
| **납부확인서** | **`/billing/claims/:id`** — **「납부확인서 발송」** (`PAID`+`paidAt`) | `POST /api/v1/billing/claims/{claimId}/payment-receipt-notify` | `BILLING_PAYMENT_RECEIVED` |

**공통 요청 본문**

```json
{
  "yearMonth": "2026-06",
  "summary": "이번 달 급여제공 요약 또는 가정통신문 본문 (500자 이하)"
}
```

**보호자 서류 발송 절차 (UI, FE `d1149a5`)**

1. **이용자 상세**(`/clients/:id`) → **기본정보** 탭 하단 **「보호자 서류 발송 (G2)」** 카드를 엽니다.
2. **문서 유형**을 선택합니다 — **노인학대예방 및 대응지침** · **가정통신문** · **급여제공기록지**.
3. **대상 연월**(`MonthInput`)을 선택하고, 필요 시 **요약**(최대 500자)을 입력합니다.
   - **급여제공기록지** — 요약을 비우면 서버가 **이동서비스 요약**을 본문에 자동 병합합니다 (Q216).
4. 유형별 발송 버튼(**지침 이메일 발송** / **가정통신문 이메일 발송** / **급여제공기록지 이메일 발송**)을 클릭합니다 — 성공 시 초록색 안내가 표시됩니다.
5. **22:00~08:00 (KST) 조용한 시간대**에는 발송이 **서버에서 거부**됩니다 — **「현재 22:00~08:00 (Asia/Seoul) 조용한 시간대입니다…」** danger Alert가 표시되면 **08:00 이후 재시도**하세요 (Q329·Q539, BE `71b2d32`). 청구 화면과 달리 **버튼은 비활성화되지 않으며**, API 오류 메시지로 안내됩니다.
6. 보호자 **`channelEmail=true`** · **`users.email`** 등록이 필요합니다 (Q204). 동의는 **`notify_daily_care`** preference를 재사용합니다 (Q222).

> **본인부담금 명세**는 청구 상세 **「보호자 발송」**(`POST /billing/claims/{id}/notify`, Q196)으로 발송합니다. **납부확인서**는 **「납부확인서 발송」**(Q221) 또는 수납 시 **자동** `BILLING_PAYMENT_RECEIVED`(J03)입니다.

---

## 5. 통합 관리자 (`hq_admin`) 매뉴얼

통합 관리자는 **다지점 운영법인 전체**를 조회·집계하고, 지점·직원·수가표·청구 정책을 관리합니다. 일상 CRUD는 **지점 선택기**로 `active_branch_id`를 고른 뒤 해당 지점에서만 수행합니다.

### 5-1. 권한 요약

| 기능 | `hq_admin` | `branch_admin` |
|------|:----------:|:--------------:|
| 전 지점 출석·이용자 **조회·집계** | ✅ | 소속 1지점만 |
| 지점·직원·계정 CRUD | ✅ | 소속 지점 범위 |
| 수가표·본인부담 비율표 관리 | ✅ | ❌ |
| 지점별 청구 생성·확정 | ✅ (지점 선택 후) | ✅ |
| 이용자·출석·건강 **쓰기** | ✅ (`active_branch_id` 지점만) | ✅ 소속 지점 |
| 전사 정책 (`allow_client_self_checkin`) | ✅ | ❌ |

### 5-2. 통합 대시보드 (`/dashboard/hq`)

**`hq_admin` 대시보드 전환 (US-H01, Q574)**: `/dashboard`·`/dashboard/hq` 상단 **`DashboardContextNav`** 로 **「통합 대시보드」** 와 **「지점 대시보드」** 를 전환합니다. 지점 대시보드는 **BranchSwitcher 활성 지점** 기준입니다.

| 영역 | 설명 |
|------|------|
| 전 지점 출석 카드 | 지점별 오늘 입소·결석·퇴소 요약 + **NHIS 대기(보류)**·미매칭·**미납 본인부담** 집계 + **「공단 일정 불일치」** home-visit 지점 합산 (Q594) + **「카카오 API 잔여」** (Q595) |
| **지점별 운영 요약·drill-down** | **`HqBranchSummaryTable`** — 행 **「지점 대시보드」** 클릭 시 해당 지점으로 **활성 지점 전환** 후 `/dashboard` 이동 (US-H01) |
| 지점 비교 | **`BranchCompareChart`** — 지점별 출석률·이용자 수 막대 비교 (UXD-48, US-H01) |
| 건강 이상 통합 목록 | 전 지점 이상 수치 이용자 — **`HealthAlertList`** 에 **지점명 Badge** 표시 (UXD-49, US-H02, Q167) |
| 기간·지점 필터 | 조회 기간·특정 지점 필터 |

**활용 팁**: 아침에 **통합 대시보드**로 2지점 이상 현황을 한눈에 확인한 뒤, **지점별 운영 요약** 표에서 조치가 필요한 지점의 **drill-down**으로 지점 대시보드로 전환하거나, 건강 이상 Badge의 **지점명**으로 우선순위를 정하고 **지점 선택기**로 상세 작업을 진행하세요.

> **현재 UI 상태 (Q594·Q595, BE `0796821`·FE `580a86b`)**: **`GET /api/v1/dashboard/hq`** — **`nhisComparisonGapCount`** 전 지점 합산 · **`hq_admin`·`sysadmin`** **「카카오 API 잔여」** StatCard — **`fetchTransportKakaoApiStatusApi`**. (이하 US-M02 carry) `/dashboard/hq`가 **`/dashboard/hq/alerts`** 와 연동되어 전 지점 `todayAttendance`·건강 알림 집계를 표시합니다. **G17/G32/G38/G39 준수지표 위젯**은 **`/dashboard/hq` 스냅샷**에서 **도메인별 우선** 로드됩니다 (FE `8fa9f3d`). **`BranchCompareChart`**·건강 이상 **`branchName` Badge** (Q167).

### 5-3. 지점·직원 관리

#### 지점 등록 (`/branches`)

1. 사이드 메뉴 **지점 관리**(`/branches`)로 이동합니다. (`hq_admin`·`branch_admin`)
2. **+ 신규 지점**을 클릭해 등록 모달을 엽니다 (FE `1794e1c`).
3. **지점명**·**급여종(`serviceType`)**·**행정구역**·주소·연락처를 입력하고 **저장**합니다.
4. **급여종**: `DAY_CARE`(주야간) · `HOME_VISIT`(방문요양) · `INTEGRATED_HOME`(통합재가) — **방문요양 일정**은 `HOME_VISIT`·`INTEGRATED_HOME`만 (Q180).
5. **`INTEGRATED_HOME`(통합재가)** 선택 시 **warning 안내**와 **롱텀 포털 기관 검색 패널**이 표시됩니다 (G19, Q223·Q357).
   - **가산 안내**: 주·야간보호형 월 가산(100,000원/인, 고시 제55조의2) — v1 **자동 청구·정산하지 않음**
   - **기관 검색 안내**: **`IntegratedHomeProviderDiscoveryPanel`** — 국민건강보험공단 **장기요양기관 검색** 링크(통합재가 필터 `ltcAdminKindChoiceYn8=Y`·주야간 `06`·단기 `07` 코드) — ogada는 공단 포털을 **대체하지 않음**
6. **행정구역**: **`RegionSelector`** 로 시·도 → 시·군·구 → 읍·면·동 순 선택 (Q184). 상위 미선택 시 하위 Select는 비활성입니다.
7. **지점명은 Tenant 내 대소문자 무시 유일** — V40, FAQ Q146.
8. 기존 지점은 행 **수정**·**비활성** (`active: false`, 데이터 보존).

#### 직원 계정 (`/staff`)

1. SideNav **운영 → 직원 관리**(`/staff`)로 이동합니다 (`hq_admin`·`branch_admin`).
2. 목록 **상단** **「입사·퇴사·휴직 현황 (FAQ 21720)」** 패널(`StaffLifecycleSummaryPanel`, Q584)에서 **입사 진행·재직·휴직·퇴사 진행·퇴사 완료** StatCard를 확인합니다. **휴직 1명 이상**이면 info Alert — 「복직 시 직원 상세 lifecycle 탭에서 진행 상태를 재직으로 변경」 안내가 표시됩니다.
3. **「입사 처리 compliance 현황」** 패널(`StaffOnboardingCompliancePanel`, Q300)에서 **대상·완료·진행 중·기한 초과** StatCard와 **FAQ21806 6단계 workflow**를 확인합니다.
4. **+ 계정 생성 요청**으로 요양보호사(`caregiver`)·사회복지사(`social_worker`)·센터장(`branch_admin`) 등 **역할**과 **소속 지점**을 지정해 **ogada 승인 요청**을 등록합니다 (Q555).
5. **`ogada_platform_admin` 역할**은 생성·요청할 수 없습니다 (Q556).
6. **이메일은 Tenant 내에서 대소문자 구분 없이 유일**해야 합니다 (V30, FAQ Q146).
7. 하단 **「계정 생성 요청」** 카드에서 **승인 대기·승인·반려** 이력을 확인합니다.
8. 목록 **「lifecycle」** 열·상단 **lifecycle 필터**·**`/staff/{userId}`** 상세 — §4-7·§5-3 lifecycle 절차와 동일 (Q290·Q584).

> **Swagger 대체**: UI 요청 실패 시 `POST /api/v1/users/account-requests` — `{ "email", "displayName", "roleCode", "branchIds": ["<uuid>"] }` (Q555). **즉시 생성**(`POST /users`)은 **플랫폼 승인 workflow 이전** 레거시 경로 — 운영 정책상 **요청→승인**을 사용하세요.

#### 직원 출퇴근 (8-4, G-STAFF-WORK-ATTENDANCE, US-R03, Q612)

케어포 **PDF p.100 「8-4. 출퇴근·근무일지」** — 지점 **활성 직원**의 **일일 출근·퇴근**을 확인하고 **수동 체크인/아웃**을 기록합니다. **이용자(수급자) 출석**(`/attendance`, Q609)과 **별도** 화면·API입니다.

1. SideNav **운영 → 직원**(`/staff`) 진입 후 **`StaffContextNav`** **「출퇴근 (8-4)」** 또는 URL **`/staff/attendance`** 로 이동합니다 (`5fd468b`).
2. **`StaffContextNav`** 아래 **「출퇴근 관련 화면」** 패널(`StaffAnnualLeaveRelatedSurfacesPanel` → **`RelatedSurfacesPanel`**, Q651·Q657)을 확인합니다. **「일별 출퇴근은 이 화면에서 기록합니다…」** 안내 아래 **「연차휴가 현황」** 링크로 **`/staff/annual-leaves`** · **「연차·유급휴일 대장」** 링크로 **`/staff/leave-ledger`** 로 이동할 수 있습니다 (Q666·Q667). 패널 항목은 roster 조회 응답의 **`relatedSurfaces[]`** 를 우선 표시합니다 (Q653, `95f55aa`).
3. **`BranchScopeNotice`** 로 **조회 지점**을 확인합니다 — 다지점 관리자는 **지점 선택기** 전환 후 **「조회」** 하세요 (Q657, `949e9bf`).
4. **일일 출퇴근 로스터** 카드에서 **근무일**을 선택하고 **「조회」** 를 누릅니다 — **`fetchStaffWorkAttendanceApi`** (`services.js`)가 **`GET /api/v1/staff/work-attendance?date=&branchId=`** 를 호출합니다. 응답에는 **`surfaceKind=DAILY_WORK_ATTENDANCE_ROSTER`** 와 **cross-link 메타**가 포함됩니다 (`83a26e7`, Q653).
5. **「출근 방식」** 에서 **수동·모바일·NFC** 중 하나를 선택합니다 — 출근 시 **`checkInMethod`** 로 전송됩니다 (`5fd468b`).
6. 상단 StatCard에서 **출근·퇴근·미출근** 건수를 확인합니다.
7. 직원 목록 테이블에서 **직원명**(상세 링크)·**역할**·**상태 Badge**·**출근 방식**·**출근/퇴근 시각**을 확인합니다.

| Badge | 의미 | 처리 버튼 |
|-------|------|-----------|
| **출근** (`CHECKED_IN`) | 출근만 완료 | **「퇴근」** |
| **퇴근** (`CHECKED_OUT`) | 퇴근 완료 | **「완료」** (버튼 없음) |
| **미출근** (`status=null`) | 기록 없음 | **「출근」** |

8. **「출근」** — **`staffWorkAttendanceCheckInApi`** → **`POST /api/v1/staff/work-attendance/check-in`** — `{ userId, checkInMethod }` — 선택한 **출근 방식**(`MANUAL`/`MOBILE`/`NFC`)이 전송됩니다.
9. **「퇴근」** — **`staffWorkAttendanceCheckOutApi`** → **`POST /api/v1/staff/work-attendance/check-out`** — `{ userId }`. **출근 기록 없이 퇴근**하거나 **퇴근 시각이 출근보다 이르면** **`422`** 거부됩니다 (Q622, BE `35e6c52`).
10. 처리 성공 시 목록이 **자동 refresh** 됩니다. 처리 중에는 버튼에 **Spinner**·**`aria-busy`** 가 표시됩니다 (UXD-152, Q623).

| 권한 | 조회 | 출근/퇴근 |
|------|:----:|:---------:|
| `hq_admin` | ✅ | ✅ |
| `branch_admin` | ✅ | ✅ |
| `social_worker` | ✅ | ✅ |
| `caregiver` | ❌ | ❌ |

> **당일만 처리**: 출근·퇴근 API는 **Asia/Seoul 기준 오늘**만 기록합니다. 과거·미래 **근무일 조회**는 가능하나 **버튼 처리는 당일**에만 유효합니다.  
> **대상 직원**: 지점에 배정된 **활성 직원**(요양보호사·사회복지사·지점장 등) — **퇴사 완료(`TERMINATED`)** 제외.  
> **P3 잔여**: NFC/MOBILE **하드웨어 단말 연동** · 월간 통계·CSV export · QR/NFC 단말 자동 체크인.

| API | 용도 |
|-----|------|
| `GET /api/v1/staff/work-attendance?date=&branchId=` | 일일 로스터 + **`surfaceKind`·`relatedSurfaces[]`** (Q653) |
| `POST /api/v1/staff/work-attendance/check-in` | 수동 출근 |
| `POST /api/v1/staff/work-attendance/check-out` | 수동 퇴근 |

> **DB**: **Flyway V169** `staff_work_attendance` — `(organization_id, branch_id, user_id, work_date)` UNIQUE.  
> 관련: FAQ **Q612·Q589·Q651·Q652·Q653** · USER_MANUAL §4-7-0b · ADMIN_GUIDE §6-2-20

#### 직원 lifecycle — 입사~퇴사 (US-R03, FAQ21825·FAQ21806, Q290·Q298)

이지케어 FAQ21825 **4단계**(입사·신고·근로활동·퇴사)를 **체크리스트**로 관리합니다. **입사/퇴사 서류 스캔**은 **「HR 파일함」** 탭에서 업로드할 수 있습니다(Q298). 체크리스트 **수동 체크**와 **파일 업로드**는 동일 checklist id로 연동됩니다.

1. **`/staff/{userId}`** 에서 **「입사~퇴사」** 탭을 선택합니다.
2. 상단 **`LifecycleWorkflowPanel`** 에서 4단계 진행 상황을 확인합니다. **`computeStaffLifecycleProgress`** 로 단계별 **완료율(%)** 이 표시됩니다 (`37dc785`). FAQ21806 **③ 신규직원교육** — **입사일 + 7일** 이내 완료 안내가 표시됩니다 (`bc3c967`).
3. **진행 상태**를 선택합니다 — `입사 진행` · `재직` · **`휴직`** · `퇴사 진행` · `퇴사 완료` (`2581347`, Q584).
4. **휴직** 선택 시 warning Alert — 「복직 시 진행 상태를 재직으로 변경하세요. 퇴사일 입력란은 비활성화됩니다.」 — **입사일 필수**·**퇴사일 입력 불가** (UXD-147 `1a614c9`).
5. **입사일**·**퇴사일**(해당 시)·**근로계약서 서명일**을 입력합니다 — 서명일은 **`DateInput`** 표준 컴포넌트를 사용합니다 (`b3e59e2`).
6. 단계별 체크리스트를 표시합니다.
   - **① 입사**: 신분증·자격증·통장·건강검진·치매교육·근로계약서·범죄경력조회
   - **② 신고**: 인력변경·RFID·배상책임보험·4대보험 취득
   - **③ 근로**: 급여명세서·임금대장·보수교육·법정의무교육·건강검진 갱신
   - **④ 퇴사**: 사직서·퇴사보고·4대보험 상실·퇴직정산·인수인계
7. **입사 완료**·**신고 완료** 토글을 필요에 따라 켭니다.
8. **저장** — `PATCH /api/v1/users/{userId}` 로 서버에 반영됩니다. 저장 중 패널에 **`aria-busy="true"`** 가 설정되어 스크린리더에 진행 상태가 전달됩니다 (`b3e59e2`).

| 상황 | 동작 |
|------|------|
| **입사 진행** 중 | 상단 warning — 「근로계약서 서명 전 현장 배치 제한」 안내 |
| **휴직** 중 | warning — 「복직 시 재직으로 변경」·**퇴사일 입력란 disabled** (Q584) |
| **퇴사 진행** 중 | 「4대보험 상실·인수인계 확인」 안내 |
| **퇴사 완료** | **`terminatedAt`(퇴사일) 필수** + **「신고 완료」** 토글 또는 **「퇴사보고」** 체크 — 미충족 시 **`422`** · 서버가 계정 **`active=false`** 자동 처리 (`c976f55`) |
| **날짜 정합** | **퇴사일은 입사일 이후**여야 합니다 — 위반 시 **`422 BUSINESS_RULE`** (앱·**V87** DB CHECK, Q293) |
| **휴직** | **`lifecycleStatus=ON_LEAVE`** — **`hiredAt` 필수** · **`terminatedAt` 금지** · **`active=false`** — **`StaffLifecyclePanel`** UI·**`GET /staff/lifecycle-summary`** 집계 (`2581347`/`1d7cee2`, Q584) |
| **입사 완료** | **근로계약서 서명일** 또는 **「근로계약서」** 체크 필요 — 미충족 시 저장 거부 |

> **P2 잔여**: 급여명세·퇴직금 **G-Payroll 연동**, G34 수준 **전자서명 잠금** — FAQ **Q290·Q296·Q298·Q300·Q444·Q540** 참고. **대시보드·목록 FAQ21823 재계약 위젯**은 Q540 @ `10585b9`/`f31c346`에서 **Fixed**.

#### FAQ21806 입사 처리 compliance 집계 (`/staff`, Q300)

이지케어 FAQ21806 **입사 6단계·7종 서류** 준수를 **지점 단위(목록)** 와 **직원별(상세)** 로 확인합니다. 개별 서류 업로드는 **「HR 파일함」** 탭(Q298)에서, 상세 checklist는 **「입사~퇴사」** 탭(Q290)에서 관리합니다.

**지점 집계 (`/staff` 목록)**

1. **`/staff`** 목록 **상단** **`StaffOnboardingCompliancePanel`** 이 로드됩니다 (`e76ca06`).
2. **StatCard** — **대상 직원** · **입사 완료** · **진행 중** · **기한 초과** 건수를 확인합니다.
3. **기한 초과**가 1명 이상이면 warning Alert — 「신규직원교육 7일 기한 또는 입사서류 미비」 안내가 표시됩니다.
4. **`LifecycleWorkflowPanel`** — FAQ21806 workflow(자격확인·근로계약·신규교육·신고·파일함·건강검진) 단계별 요약을 봅니다.
5. **compliance 목록 표** — 직원별 **서류(7종)** · **신규교육 마감일** · **미비 서류** · **상태 Badge**를 확인합니다.
6. **이름** 링크 → **`/staff/{userId}`** — 아래 **직원별 카드**·**「HR 파일함」**에서 보완합니다.

**직원별 (`/staff/{userId}` → 「입사~퇴사」, `4efa168`)**

1. **`StaffMemberOnboardingComplianceCard`** — 해당 직원의 **상태 Badge**·**입사서류 진행(7종)**·**신규교육 마감일**·**미비 서류**를 표시합니다.
2. **기한 초과** warning Alert — 「HR 파일함에서 서류를 보완하고 lifecycle 체크리스트를 완료하세요.」
3. **미비 서류** 행의 **「○○ 업로드」** 버튼 — **「HR 파일함」** 탭으로 이동하며 해당 문서 유형이 **미리 선택**됩니다.
4. **「HR 파일함 열기」** 버튼 — 같은 탭 전환(미비 유형 우선).
5. **`LifecycleWorkflowPanel`** — FAQ21806 **6단계** 직원별 진행(하단 **「입사~퇴사 lifecycle」** 패널과 checklist id 공유).
6. HR 파일 업로드·삭제 후 compliance 카드가 **자동 갱신**됩니다 (`complianceReloadToken`).

| 상태 Badge | 의미 |
|-----------|------|
| **입사 완료** | `onboardingComplete=true` 또는 7종 서류·교육 기한 충족 |
| **진행 중** | 일부 서류·체크리스트만 제출 |
| **기한 초과** | **입사일+7일** 신규교육 마감 초과 **및** 미비 서류 존재 |
| **미착수** | 제출 서류 없음 |

> **다지점 `hq_admin`**: **지점 선택기**로 활성 지점을 바꾼 뒤 패널이 해당 지점 직원만 집계합니다. API: `GET /api/v1/staff/hr-files/onboarding-compliance?branchId=`

#### FAQ21823 근로(재)계약·임금협의 집계 (`/staff` 목록, Q540)

이지케어 FAQ21823 **연간 임금협의·근로(재)계약** 준수를 **직원 목록 상단**에서 먼저 확인합니다. **별도 BE API 없음** — 로드된 직원 목록과 **`contractSignedAt`** 기준 **FE 계산**입니다 (`10585b9`).

1. **`/staff`** 직원 관리 화면을 엽니다.
2. 목록 **상단** **`StaffEmploymentContractRenewalSummaryPanel`** (**「근로(재)계약·임금협의 (FAQ 21823)」**) 을 확인합니다.
3. **StatCard** — **재직·입사 대상** · **재계약 기한 초과** · **서명일 미등록** · **예정** 인원 수를 봅니다.
4. **기한 초과** 또는 **서명일 미등록**이 1명 이상이면 warning Alert — 「직원 상세 lifecycle 탭에서 재계약 안내와 HR 파일함을 확인하세요.」
5. **확인 필요 목록** 표 — **이름** 링크 → **`/staff/{userId}`** (스크린리더: **「{이름} 근로(재)계약 lifecycle 보기」**, Q544) · **서명일** · **다음 재계약** · **상태 Badge**(기한 초과·서명일 미등록)를 확인합니다.
6. **대시보드**(`/dashboard`·`/dashboard/hq`) **「근로재계약 미충족」** StatCard(`f31c346`)를 클릭해도 같은 **`/staff`** 화면으로 이동합니다.

| 상태 Badge | 의미 |
|-----------|------|
| **기한 초과** | 서명일 **+1년** 재계약·임금협의 기한 경과 |
| **서명일 미등록** | **`contractSignedAt`** 없음 — lifecycle **「입사~퇴사」** 탭에서 입력 |
| **예정** | 서명일 등록·재계약 기한 **이내** (목록에는 미표시, StatCard **예정**만 집계) |

> **퇴사 완료** 직원은 집계에서 **제외**됩니다. **급여명세·G-Payroll 연동**은 P2 잔여입니다.

#### FAQ21823 근로(재)계약·임금협의 안내 (`/staff/{userId}`, Q540)

이지케어 FAQ21823 **연간 임금협의·근로(재)계약**을 **직원 상세 「입사~퇴사」** 탭에서 확인합니다. **급여명세·G-Payroll 연동**은 P2 잔여입니다.

1. **`/staff/{userId}` → 「입사~퇴사」** 탭을 엽니다.
2. **`StaffMemberOnboardingComplianceCard`** 아래 **`StaffEmploymentContractRenewalPanel`** (**「근로(재)계약·임금협의 (FAQ 21823)」**) 을 확인합니다.
3. **근로계약서 서명일** — **「입사~퇴사 lifecycle」** 패널의 **`DateInput`** 과 동일 값이 표시됩니다. 미등록 시 **「서명일 등록 후 1년」** 안내가 나옵니다.
4. **다음 재계약·임금협의** — 서명일 **+1년** 날짜가 자동 계산됩니다. 기한이 지나면 **warning Alert**·**「기한 초과」** Badge가 표시됩니다.
5. **보관 기한(3년)** — 서명일 기준 **+3년** 날짜가 표시됩니다 (근로계약서·임금협의 기록 보관).
6. **2026 최저임금 참고** — **10,320원/시간** 안내값이 표시됩니다 (법정 최저임금 변경 시 앱 업데이트 필요).
7. **「근로계약서 파일함」** 버튼 — **「HR 파일함」** 탭으로 이동하며 문서 유형 **`employment-contract`** 가 미리 선택됩니다. 기한 초과 시 버튼이 **warning Alert** 와 **`aria-describedby`** 로 연결됩니다 (Q544, UXD-141).
8. **필수 기재 5항 (FAQ 21823)** — **임금·소정근로시간·휴일·연차유급휴가·근로조건** ordered checklist를 확인합니다 (Q546, `1b6d2b1`).
9. **연간 갱신 절차** — **① 임금협의 → ② 근로(재)계약서 작성 → ③ 보관·등록(HR 파일함)** 3단계 안내를 따릅니다 (Q546).
10. **「근로계약서 서식 보기」** — Modal에서 **출력·필기용 서식**을 확인합니다. 작성 후 **기관·근로자 각 1부** 보관하고 스캔본을 HR 파일함에 등록하세요 (Q546). **BE PDF 자동 생성 ❌** (P2).
11. **「재계약 완료 기록」** (`branch_admin`·`social_worker`만, Q547, `033b319`) — 연간 임금협의·근로(재)계약 완료 후 **재계약 서명일**을 저장합니다.
    1. **「재계약 완료 기록」** 버튼을 누릅니다.
    2. Modal에서 **재계약 서명일**(`DateInput`)을 입력합니다.
    3. **저장** — **`PATCH /api/v1/users/{userId}`** (`updateUserApi`) — **`contractSignedAt`** 갱신 + **`lifecycleChecklist["employment-contract"]=true`** 자동 반영.
    4. 저장 성공 시 **「재계약 서명일을 저장했습니다. HR 파일함에 스캔본을 등록하세요.」** success Alert — **다음 재계약 기한**은 새 서명일 **+1년**으로 자동 갱신됩니다.
    5. 스캔본은 **「근로계약서 파일함」** 에 업로드하세요.
12. **퇴사 완료(`TERMINATED`)** 직원에게는 패널이 **표시되지 않습니다**.

| 항목 | 내용 |
|------|------|
| **법적 안내** | 임금·소정근로·휴일·연차·근로조건 **5항** 포함 근로계약서 · 기관·근로자 **각 1부** 보관 |
| **필수 5항 checklist (Q546)** | **`EMPLOYMENT_CONTRACT_REQUIRED_CLAUSES`** — 각 항목별 상세 설명 |
| **연간 갱신 workflow (Q546)** | **`EMPLOYMENT_CONTRACT_RENEWAL_WORKFLOW`** — 임금협의·작성·보관 3단계 |
| **서식 Modal (Q546)** | **`EMPLOYMENT_CONTRACT_RENEWAL_TEMPLATE`** — 2026 최저임금 placeholder 포함 |
| **스캔 보관** | HR 파일함 **「근로계약서」** (`employment-contract`) 에 PDF·이미지 업로드 |
| **입사 완료 가드** | **서명일** 또는 checklist **「근로계약서」** 체크 없이 **입사 완료** 저장 불가 (기존 Q290) |
| **재계약 기록 (Q547)** | **「재계약 완료 기록」** Modal — **`updateUserApi`** — 서명일+checklist 동시 저장 · **대시보드 due-date Alert** (30일 임박 포함) |
| **P2 잔여** | **전자서명 workflow** · **서식 PDF 자동 생성** · **G-Payroll 급여명세 연동** |

> 관련: Q290 · Q298 · Q300 · Q546 · Q547 · FAQ21825 · FAQ21806

#### 직원 HR 파일함 (US-R03, FAQ21806·FAQ21825, Q298)

이지케어 FAQ21806 **입사 8종 서류**·FAQ21825 퇴사 서류를 **직원별**로 스캔 보관합니다. 보수교육 **이수증**·건강검진 **실시 이력**도 같은 탭에서 조회·관리합니다.

1. **`/staff`** 목록에서 직원 **이름** 또는 **「상세」** → **`/staff/{userId}`** 로 이동합니다.
2. **「HR 파일함」** 탭을 선택합니다 (`bc3c967`).
3. **서류관리 repository (G-STAFF-DOCUMENT-REPOSITORY, Q604, FE `fd15a2f`/`751c593`)** — 상단 **`StaffDocumentRepositoryPanel`** 에서 FAQ21825 **21 lifecycle 슬롯** 진행률을 확인합니다. 진행률은 **`GET /staff/hr-files/users/{userId}/repository-progress`** API 단일 소스입니다 (client-side merge 없음). phase·슬롯은 스크린리더 **`aria-label`** 로 구분됩니다 (UXD-150, Q606).

| 요약 StatCard | 의미 |
|---------------|------|
| **진행률** | 완료 슬롯 / **21** (`progressLabel`) |
| **케어포 parity** | 완료 슬롯 / **20** — PDF p.96 zone③ 「서류 20개」 대비 (`careforParityLabel`) |
| **파일 업로드** | HR 파일함에 등록된 **8종** 업로드 유형 건수 |
| **체크list** | lifecycle 탭에서 수동 체크한 항목 수 |

4. **phase별 슬롯** — **입사(①)·신고(②)·근로활동(③)·퇴사(④)** 4단계로 미비 항목 Badge를 확인합니다. **업로드 지원** 슬롯(8종)은 **「업로드 선택」** 또는 **「모바일 촬영」** (`6bde24a`, Q608) — 스마트폰 후면 카메라로 **PNG/JPEG** 촬영 후 **`uploadStaffHrFileApi`** 로 즉시 등록합니다. 모바일에서는 두 버튼이 **행 전체 너비**로 표시됩니다 (`9812ac4`, UXD-151, Q611).
5. **완료 판정** — checklist **수동 체크** 또는 **HR 파일 업로드** 중 하나면 해당 슬롯 **완료** (`completionSource`: `checklist` / `file`).
6. **「lifecycle 탭 열기」** — checklist만으로 보완할 항목은 **「입사~퇴사」** 탭으로 이동합니다.

> **모바일 촬영 (Q608·Q611)**: **`StaffHrFilePanel`**·**`StaffRefresherCertificatePanel`** 의 **`FileUpload`** 에도 **「카메라 촬영」** 버튼이 있습니다. xlsx·PDF는 **파일 선택**을 사용하세요. 버튼이 좁게 보이면 FE HEAD **`9812ac4`+** 확인 (FAQ Q611).

7. **직원 일반 파일함 (US-R03)** — 문서 유형을 고른 뒤 **PDF/PNG/JPEG(≤10MB)** 파일을 업로드합니다.

| 문서 유형 | checklist id | 비고 |
|----------|--------------|------|
| 신분증 | `id-card` | FAQ21806 ① |
| 자격증 | `certificate` | |
| 통장 사본 | `bank-account` | |
| 건강검진 결과 | `health-check` | checklist 연동 · **`/staff/health-checkups`** **「서류 업로드」** deep link (Q444, `b6ce301`) |
| 치매교육 이수 | `dementia-training` | |
| 근로계약서 | `employment-contract` | 서명일은 **「입사~퇴사」** 탭에서 별도 입력 |
| 범죄경력조회 | `criminal-record` | |
| 사직서 | `resignation` | 퇴사 ④ |

8. **같은 문서 유형**을 다시 업로드하면 **기존 파일을 교체**합니다(유형당 1건).
9. 목록에서 **미리보기**·**삭제**할 수 있습니다. 삭제 시 해당 checklist 항목이 **false**로 되돌아갑니다.
10. 하단 **보수교육 이수증**·**건강검진 이력** 패널에서 직원별 증빙·기록을 관리합니다 — 목록 화면(`/staff/training`·`/staff/health-checkups`)과 **동일 API**입니다.

| 권한 | HR 파일함 업로드·삭제 | 조회·미리보기 |
|------|:--------------------:|:------------:|
| `branch_admin` | ✅ | ✅ |
| `social_worker` | ✅ | ✅ |
| `hq_admin` | ❌ (UI 숨김) | ✅ |
| `caregiver` | ❌ | ❌ |

| API | 용도 |
|-----|------|
| `GET /api/v1/staff/hr-files/users/{userId}/repository-progress` | **21-slot** 서류관리 진행률 (`b583c11`, Q604) |
| `GET /api/v1/staff/hr-files/users/{userId}` | HR 파일 목록 |
| `POST /api/v1/staff/hr-files/users/{userId}` | multipart — `documentType` + `file` |
| `GET /api/v1/staff/hr-files/users/{userId}/{fileId}` | 미리보기/다운로드 |
| `DELETE /api/v1/staff/hr-files/users/{userId}/{fileId}` | 삭제 |

> **DB**: **Flyway V91** `staff_hr_files` — 문서 유형·크기·MIME CHECK · `(organization_id, user_id, document_type)` **유형당 1건**.

#### 직원 보수교육 (8-7-1, US-S02, FAQ21825, Q294·Q295)

케어포 **8-7-1** 「요양보호사 보수교육」 — **입사일 기준 2년마다** 이수 여부를 관리합니다.

1. SideNav **운영 → 직원**(`/staff`) 진입 후 **`StaffContextNav`** **「보수교육 (8-7-1)」** 또는 URL **`/staff/training`** 으로 이동합니다 (`314b380`).
2. 상단 **StatCard**(`ds-stat-grid`)에서 **전체·이수 완료·이수 필요·이수 예정·입사일 미등록** 건수를 확인합니다. **입사일 미등록** 직원도 **이수 필요(`requiredCount`)** 집계에 포함되어 누락 없이 표시됩니다 (`50bdb6e`, Q294). **이수 필요** 직원이 있으면 warning **`Alert`** 가 표시됩니다.
3. **`LifecycleWorkflowPanel`** — 보수교육 **2단계 lifecycle**(주기 확인 → 이수 기록)을 확인합니다.
4. 목록에서 **직원·역할·입사일·다음 이수 예정일·상태 Badge**를 확인합니다.
5. **「이수증」** — Modal에서 **PDF/PNG/JPEG(≤10MB)** 파일을 업로드합니다. 업로드 성공 시 **`lifecycleChecklist["refresher-training"]=true`** 가 **자동 반영**됩니다 (`0a7fe16`, Q295). 등록된 이수증은 **미리보기**(PDF 새 탭·이미지 Modal)·**삭제**할 수 있습니다.
6. **「이수 완료」** — 이수증 없이 체크만 기록할 때 사용합니다. **`POST /api/v1/staff/refresher-training/compliance`** 로 `{ "userId": "<uuid>", "completed": true }` 를 저장합니다 (`510dbd1`, Q294). 구버전 BE에서는 **`PATCH /api/v1/users/{userId}`** lifecycle fallback이 사용됩니다. **`StaffLifecyclePanel`** ③ 근로 **「보수교육 (8-7-1)」** 체크와 **동일 id**입니다.
7. **「엑셀 다운로드 (8-7-1)」** — 목록 우측 버튼으로 **케어포 8-7-1 보수교육 리포트** CSV를 내려받습니다. 직원별 **입사일·다음 이수 예정일·상태**가 포함됩니다 (Q460, `caa215f`). 목록이 비어 있으면 버튼이 비활성화됩니다.
8. **권한**: **`hq_admin`·`branch_admin`·`social_worker`** 가 조회·미리보기 가능합니다. **업로드·삭제**는 **`branch_admin`·`social_worker`만** (`51477bd`). 대상 역할은 **요양보호사·사회복지사·지점장**입니다.

| API | 용도 |
|-----|------|
| `GET /api/v1/staff/refresher-training/compliance?branchId=&referenceDate=` | 지점·기준일별 **보수교육 compliance 집계** (BE, `9c9fd5b`) |
| `POST /api/v1/staff/refresher-training/compliance` | **이수 완료** 기록 — `{ userId, completed: true }` (BE·FE, `510dbd1`) |
| `GET/POST/DELETE /api/v1/staff/refresher-training/users/{userId}/certificates*` | **이수증 목록·업로드·삭제** · `GET …/{certificateId}` 미리보기 (BE, `51477bd`) |

> **P2 잔여**: **교육기관 API 연동** — FAQ **Q294·Q295·Q460** 참고. **대시보드 위젯**은 **234차 Fixed** (Q461).

#### 기관 교육일지 (8-7, G41/G41b, US-S04, FAQ21807/21828, Q321)

케어포 **func.php `8-7.교육일지`** — **노인인권·운영규정·재난·소화·직원권익** 지점 교육 기록입니다. **보수교육(8-7-1)** 과 **별도 화면**입니다.

1. SideNav **운영 → 직원**(`/staff`) 진입 후 **`StaffContextNav`** **「교육일지 (8-7)」** 또는 URL **`/staff/training-logs`** 로 이동합니다 (`f5658de`·`45a724a`).
2. **연도·교육 유형** 필터로 목록을 좁힙니다. **기준 연도 필터**는 **4자리·2000~2100**만 API에 전달됩니다 — `abcd`·범위 밖 입력 시 **`Field error`** 「기준 연도는 2000~2100 사이 4자리 숫자여야 합니다.」가 표시되고 **`referenceYear` 없이** 목록만 조회하며 **compliance 요약 StatCard는 숨깁니다** · **compliance API도 호출하지 않습니다** (Q489·Q503, `f26e075`/`28e5525`/`cefb7c7`). 유효 입력 시 help **「2000~2100 사이 4자리. 유효하지 않으면 준수 현황이 숨겨집니다.」** 가 **`aria-describedby`** 로 연결됩니다 (Q493·Q504, UXD-134/135). G41b **재난·소화·직원권익** 3종도 필터·등록 가능합니다 (V106).
3. 상단 **StatCard**에서 **노인인권 상·하반기** · **운영규정 연간** · **G41b 3종 연간** · **신규직원 7일 오리엔테이션** compliance를 확인합니다 (`GET …/compliance`, BNK-185 `0f11158`). G41b StatCard는 **BE compliance API 우선** · API 필드 누락 시에만 목록 건수 fallback (`38d24b6`). **재난·소화** StatCard에는 미충족 시 **「미작성」** unit이 표시됩니다 (Q459, `caa215f`).
4. **PDF 8-7 필수 교육 미작성 Alert** — **재난상황대응**·**소화·경보설비** 중 **연간 미작성** 항목이 있으면 상단 warning Alert가 표시됩니다. Alert **`id="staff-training-mandatory-alert"`** — 스크린리더가 **필수 교육 누락**을 먼저 읽을 수 있습니다 (Q459·Q462, `caa215f`/`7f94654`). **「교육일지 등록」** 으로 보완합니다.
5. **「교육일지 등록」** — Modal에서 **기준 연도·교육 유형·교육일·방법·강사·참석자·교육내용**을 입력합니다. 모든 입력은 **`Field` render-prop**으로 label·help·오류가 input에 **`aria-describedby`** 로 연결됩니다 (Q504, UXD-135 `40d0ca3`). **기준 연도**는 **4자리·2000~2100**만 허용 — 유효하지 않으면 **「기준 연도는 2000~2100 사이 4자리 숫자여야 합니다.」** 필드 오류가 표시되고 저장되지 않습니다 (Q489, `f26e075`).
   - **노인인권교육**: **반기(상/하반기)** · **교육내용** 필수 — **유일하게 `referenceHalf` 포함**.
   - **운영규정 — 연간 교육**: 반기·신규직원 플래그 없이 등록 (**`referenceHalf` 없음**, V107).
   - **G41b 3종(재난·소화·직원권익)**: **연 1회** — **`referenceHalf` 없음** (V107, Q325).
   - **운영규정 — 신규직원 오리엔테이션**: **신규직원 교육** 체크 + **대상 직원** 선택 — **입사 후 7일 이내** 교육일만 허용 (`422` 가드). help 문구는 **API `newHireItems` 기준** (`e14ba10`).
6. 목록 **「수정」** — 동일 Modal에서 **PATCH** 저장합니다.
7. **신규직원 오리엔테이션 현황** 표(해당 연도·**지점 스코프** 신규 채용자)에서 **기한·충족 여부**를 확인합니다. 동일 직원에 여러 오리엔테이션 기록이 있으면 **가장 이른 교육일** 기준으로 집계됩니다 (BNK-187).
8. **권한**: **`hq_admin`·`branch_admin`·`social_worker`** 가 조회·등록·수정 가능합니다 (`6191b91`).

| 교육 유형 | 코드 | 주기 |
|----------|------|------|
| 노인인권교육 (지표14) | `ELDERLY_HUMAN_RIGHTS` | **상·하반기 각 1회** |
| 운영규정 (지표5) | `OPERATING_REGULATION` | **연 1회** + **신규 7일** |
| 재난상황대응 (G41b) | `DISASTER_RESPONSE` | **연 1회** |
| 소화·경보설비 (G41b) | `FIRE_SAFETY_EQUIPMENT` | **연 1회** |
| 직원권익 (G41b) | `STAFF_RIGHTS` | **연 1회** |

> **G41 FAQ21808 확장 (Q356, BE V129 `b1c92e1`)**: API·DB는 **운영규정 11항목**(`OP_REG_*`)·**급여제공지침 12종**(`GUIDELINE_*`) 등 **합계 28종** `training_type` 을 수용합니다. **현재 FE 등록 Modal 드롭다운은 위 5종**만 표시 — 세부 23종 UI는 **P2**입니다. API로 직접 등록하거나 IT 연동 시 V129 enum을 사용합니다.

| API | 용도 |
|-----|------|
| `GET /api/v1/staff/training-logs?branchId=&referenceYear=&trainingType=` | 목록 |
| `POST /api/v1/staff/training-logs` | 등록 |
| `PATCH /api/v1/staff/training-logs/{logId}` | 수정 |
| `GET /api/v1/staff/training-logs/compliance?branchId=&referenceYear=` | FAQ21807/21828 compliance |

> **P2 잔여**: **G41 FAQ21808 23종 세부 UI** · **공식 PDF 서식**(현재는 브라우저 인쇄·BE CSV) · **live E2E** — FAQ **Q308·Q315·Q321** 참고. **대시보드 위젯**·**PDF 8-7 필수 Alert**·**8-7-1 CSV**는 **234차 Fixed** (Q459·Q460·Q461).

#### 직원 건강검진 (8-10, US-R02, FAQ21799, Q296·Q435)

케어포 **8-10** 「건강검진관리」·이지케어 FAQ21799 **지표9** — 직원 **건강검진 실시일**과 **5개 영역** 이수 여부를 관리합니다. **신규 직원**은 **근무 시작일(입사일) 기준 1년 이내** 검진 실시일·결과통보서 확인이 필요합니다 (FAQ21799, `8e6310a`).

1. SideNav **운영 → 직원**(`/staff`) 진입 후 **`StaffContextNav`** **「건강검진 (8-10)」** 또는 URL **`/staff/health-checkups`** 으로 이동합니다 (`604787f`).
2. 상단 **StatCard**에서 **대상 직원·검진 완료·검진 필요·신규 서류 미확인** 건수를 확인합니다. **검진 필요** 또는 **신규 서류 미확인** 직원이 있으면 warning **`Alert`** 가 표시됩니다.
3. **`LifecycleWorkflowPanel`** — 건강검진 **2단계 lifecycle**(주기 확인 → 실시 기록)을 확인합니다.
4. 목록에서 **직원·역할·최근 검진일·다음 검진 기준·주기·5영역 진행·입사일·신규 서류·상태 Badge**를 확인합니다.
   - **신규 서류** Badge: **1년 이내 확인** · **서류 필요** · **입사일 미등록** — 입사일과 최근 검진일을 대조한 결과입니다. **해당 없음(NA)** 은 **「—」** 로 표시합니다 (Q435·Q442).
5. **「검진 기록」** — Modal에서 **실시일**·**5개 영역 Checkbox**(신체계측·요검사·혈액·영상·결과판정)·**사무직 여부**·**소견**을 입력합니다. **최소 1개 영역** 체크가 필요합니다.
   - **첫 검진** 등록 시 실시일은 **입사일 기준 1년 이내**(입사일 당일 포함·입사일 −365일 이후)여야 합니다. 범위 밖이면 필드 오류가 표시됩니다.
6. **「이력」** — 해당 직원의 과거 검진 기록과 **건강검진 결과통보서(파일함)** 등록 여부를 **`StaffHealthCheckupRecordsPanel`** 로 조회합니다 (Q444, `b6ce301`). 파일이 없으면 **「파일함에서 업로드」** 링크로 **`/staff/{userId}?tab=files&doc=health-check`** HR 파일함에 바로 이동합니다.
7. **「서류 업로드」** — **신규 서류 필요** Badge가 있는 직원 행에서 목록 **「서류 업로드」** 링크를 누르면 동일 HR 파일함 탭으로 이동합니다. 스캔본(PDF·이미지)을 **`health-check`** 유형으로 등록하세요 (FAQ21799·FAQ21806, Q444).
8. **주기**: **일반 직원 1년** · **사무직 2년** (입사일·최근 검진일 기준).
9. **권한**: **`hq_admin`·`branch_admin`·`social_worker`** 가 조회·이력 확인 가능합니다. **기록 등록**은 **`branch_admin`·`social_worker`만** (`f1268c6`).

| API | 용도 |
|-----|------|
| `GET /api/v1/staff/health-checkups/compliance?branchId=&referenceDate=` | 지점·기준일별 **건강검진 compliance 집계** (BE, `f1268c6`) |
| `GET /api/v1/staff/health-checkups/users/{userId}` | 직원별 **검진 이력 목록** |
| `POST /api/v1/staff/health-checkups/users/{userId}` | **검진 실시 기록** 등록 |
| `GET /api/v1/users` (페이지 순회) | compliance 행에 **`hiredAt`** 병합 — 신규 서류 판정 (FE, `8e6310a`) |

> **lifecycle 연동**: **`StaffLifecyclePanel`** ① 입사 **「건강검진」**(`health-check`)·③ 근로 **「건강검진 갱신」**(`health-check-renewal`) 체크리스트와 **동일 도메인**입니다. 검진 기록 시 checklist 자동 반영은 **후속** — 현재는 compliance 집계·수동 체크 병행.

> **P2 잔여**: **대시보드 위젯** · checklist **자동 반영** — FAQ **Q296·Q435·Q444** 참고. (결과통보서 **HR 파일함 업로드**는 Q444에서 **부분 Fixed**)

#### 직원현황 리포트 (8-12, US-R02, BNK-142~171, Q308·Q315)

케어포 **8-12** 「직원현황 리포트」에 대응합니다. **입사 처리(FAQ21806)** · **보수교육(8-7-1)** · **건강검진(8-10)** compliance를 **한 화면**에서 집계합니다 (BE `aaa16f8`·`bc927f7`·FE `488f547`·`5bba7a2`).

1. SideNav **운영 → 직원**(`/staff`) 진입 후 **`StaffContextNav`** **「직원현황 리포트 (8-12)」** 또는 URL **`/staff/reports/status`** 로 이동합니다.
2. **기준일**(`DateInput`)을 선택하고 **조회**합니다. 서버가 **`referenceDate`** 기준으로 compliance를 **한 번에** 집계합니다.
3. 상단 **StatCard**에서 **대상 직원**·**조치 필요**·**입사 기한 초과**·**보수교육 미이수**·**건강검진 필요** 건수를 확인합니다.
4. **`LifecycleWorkflowPanel`** — **직원현황 lifecycle (8-12)** 단계별 **지연 건수**를 Badge와 함께 확인합니다.
5. **출력물 7종** — 케어포 PDF p.106 대응 **명부·사진게시·연락처·월간명부·입퇴사**는 **인쇄**, **엑셀**은 **서버 CSV 다운로드**합니다 (`exportStaffStatusReportCsvApi`, Q315). **인쇄 레이아웃 가독성**은 `e3e6964`·**인쇄 종료 cleanup**은 `a4ea2d5`에서 개선되었습니다 — **`afterprint`/`setTimeout` fallback** 으로 print body class·blob URL이 정리되고 **다중 페이지 표** 간격을 확인한 뒤 출력하세요. 연락처·입퇴사·사진게시·인쇄 5종은 **`GET /users`를 페이지 단위로 순회**(size=200, 최대 50페이지)해 **전 직원 프로필**을 불러온 뒤 enrich합니다 (`ff173af`). 인쇄 전 행 데이터가 안정화됩니다 (`5bba7a2`).
6. 하단 표에서 **직원별** **입사 처리·보수교육·건강검진·종합** 상태를 확인합니다. 직원 이름 → **`/staff/{userId}`** 상세.
7. **권한**: **`hq_admin`·`branch_admin`·`social_worker`** 가 조회 가능합니다 (`caregiver`·`guardian` **403**).

| API | 용도 |
|-----|------|
| `GET /api/v1/staff/reports/status?branchId=&referenceDate=` | **aggregated** 직원현황 — items[] + summary (BE `aaa16f8`) |
| `GET /api/v1/staff/reports/status/export?branchId=&referenceDate=&outputType=excel` | **CSV 다운로드** — UTF-8 BOM (BE `bc927f7`) |

> **P2 잔여**: **대시보드 위젯** · **공식 PDF 서식**(현재는 브라우저 인쇄·BE CSV) · **live E2E** — FAQ **Q308·Q315** 참고.

### 5-4. 수가표·본인부담 비율 (`/billing` 설정)

청구 계산의 기준이 되는 **전사 공통 테이블**입니다. 센터장이 월말 청구 전에 반드시 유효한 수가가 등록되어 있어야 합니다.

#### 수가표 (`fee_schedules`, G9·G9-COG)

| 항목 | 설명 |
|------|------|
| 키 | **적용연도** × **장기요양등급** × **이용시간 밴드** (`duration_band`) |
| 등급 | **1~5등급**(표준 25칸) + **인지지원등급 `ltcGrade=0`**(보조 5칸, G9-COG, Q311) |
| 값 | 1일당 수가 (원) |
| 밴드 | `H3_6`·`H6_8`·`H8_10`·`H10_13`(파일럿 기본)·`H13_PLUS` — FAQ Q210 |
| NHIS import gate | **표준 25칸 항상** 필수 — 지점에 **활성 인지지원등급(`ltcGrade=0`) 이용자**가 있으면 **인지지원 5칸도** 필수 (`8bb6583`, Q260·Q311) |
| 버전 | 연도·개정 시 **새 행 추가** 또는 수정(이력 보존). **새 적용일은 기존 버전 이후만** 허용 (Q48). 과거 확정 청구는 당시 수가·**이용시간대 스냅샷** 유지 (V62, Q213) |

1. **청구·정산** → **수가표 관리**(`/billing/fee-schedules`)로 이동합니다 (`hq_admin` 전용).
2. 상단 **`FeeScheduleMatrix`** — **등급(1~5 + 인지지원)×이용시간대 2차원 표**(총 **30칸**)에서 셀을 클릭해 등록·수정합니다 (FE `6ef671b`, Q311).
3. **보기 연도**를 바꾼 뒤, 미등록 셀이 있으면 **「공단 2026 수가 시드 (N건)」** 으로 MOHW 2026 공식 **미등록 셀만** 일괄 등록할 수 있습니다 — **표준·인지지원 모두** 포함 (`2efc557`·`6ef671b`). Swagger·자동화는 **`POST /billing/fee-schedules/apply-nhis-seeds?year=`** 로 동일 일괄 등록 가능 (`edd2771`).
4. **+ 수가 등록** 또는 목록 행 **수정** — **연도·등급·이용시간대·1일 수가·시행일** (`DurationBandSelect`). **인지지원등급**은 **`ltcGrade=0`** (V99).
5. 하단 **`FeeScheduleTable`** — 등급·밴드·수가·시행일 (`GET /billing/fee-schedules`, Q91).
6. **이력 보기** → `FeeRateHistoryPanel` — 연도·등급·**밴드**별 시행 이력 (`GET /billing/fee-schedules/history?year=`).
7. 등록·수정 시 **등록자 UUID**(`fee_schedules.created_by`)가 자동 기록됩니다 (V35).
8. 하단 **`FeeSurchargeGuidePanel`** (G11, Q229) — MOHW 2026 **가산율 참고표**(야간 20%·심야 30%·주말·공휴일 30%·유급휴일 50%) · **유형별 가산 미리보기** · **제공일(`DateInput`)·입·퇴소 시각 미리보기**(`POST /billing/fee-surcharge-preview`, API 연동, Q281) · **계획일정 vs 청구일정 차이** 8종 안내. **출석 기반 청구 생성** 시 가산이 **일별 자동 반영**됩니다 — **`NHIS_IMPORT`** 기준은 가산 없음. 참고표는 **`GET /billing/fee-surcharge-rates`** 와 동일합니다.

**이용자 밴드** — 이용자 등록·수정에서 **이용시간대**를 지정합니다. **신규** 청구 생성 시 이용자 밴드와 일치하는 수가가 적용되며, 생성 시점 밴드는 **`duration_band_snapshot`** 으로 청구 라인에 고정됩니다 (Q213). 미등록 시 기본 **`H10_13`**.

> **등록 본문 예시** — `POST /api/v1/billing/fee-schedules`
>
> ```json
> { "year": 2026, "ltcGrade": 3, "durationBand": "H10_13", "dailyRate": 68000, "effectiveFrom": "2026-01-01" }
> ```
>
> **인지지원등급 예시** — `{ "year": 2026, "ltcGrade": 0, "durationBand": "H10_13", "dailyRate": 56360, "effectiveFrom": "2026-01-01" }` (Q311)

#### 본인부담 비율표 (`copay_rates`)

| 구분 코드 | UI 약칭 | 정식 용어 (G9-COPAY-NAMING) | 대표 비율 |
|-----------|---------|----------------------------|----------|
| `GENERAL` | 일반 | 일반 (감경 없음) | 15% |
| `REDUCED_40` | 감경 40% | **100분의 40 감경** | 9% |
| `REDUCED_60` | 감경 60% | **100분의 60 감경** | 6% |
| `MEDICAID` | 기초수급 | 의료급여 (본인부담 면제) | 0% |

법·제도 개정 시 비율 수치만 테이블에서 수정합니다. 이용자별 구분은 이용자 프로필의 `copayType`에 저장됩니다. **`CopayTypeSelect`**·**`CopayRateTable`** 에서 정식 용어가 help·설명에 병기됩니다 (Q313·`e77b7e4`).

> **주의**: 「감경 40%」는 **본인부담률 40%**가 아닙니다. FAQ **Q313** 참고.

1. **청구·정산** → **본인부담 비율**(`/copay-rates`)로 이동합니다. *(2026-06-07 UXD 21차: **`CopayRateTable`** 구분별 비율 편집 표. **저장 API 미연동** — FAQ Q131)*
2. 구분별 **비율(%)**을 수정하고 **저장**을 클릭합니다. *(현재 로컬 성공 메시지만 — Swagger `PATCH /billing/copay-rates` 우회)*

### 5-5. 전사 운영 정책·청구 생성 기준 (US-M03)

통합 관리자(`hq_admin`)는 **이용자 본인 QR 셀프 체크인** 허용 여부와 **월별 청구명세서 생성 기준**(케어포 9-1)을 설정합니다.

#### 화면 (`/organization/settings`)

1. 사이드 메뉴 **조직 설정**(`/organization/settings`, **`OrganizationSettingsPage`**)으로 이동합니다. (**`hq_admin` 전용** — FAQ Q178)
2. **「운영 정책」** 카드 — **「이용자 셀프 QR 체크인 허용」** `Switch`를 켜거나 끕니다.
3. 토글이 **즉시 서버에 저장**됩니다 — `GET /api/v1/organization` 로드 · `PATCH /api/v1/organization/settings` 저장 (FE `f749311`, Q116 **Fixed**).
4. **「청구·정산」** 카드 — **`BillingSettingsPanel`** 에서 **청구명세서 생성 기준**을 선택하고 **저장**합니다 (FE `ac23529`, Q224). 레거시 DB 값 **`ATTENDANCE`/`NHIS`** 는 화면에서 **`ATTENDANCE_SCHEDULE`/`NHIS_IMPORT`** 로 자동 정규화됩니다.
5. (기존 ERP 이관 시) 같은 카드 하단 **「청구시작 기준금액 (G33)」** 에서 **도입 전 미납·선납**을 **1회만** 설정합니다 (§5-5-1, Q269).
6. **「알림 채널 준비 상태」** 카드 — **`NotificationChannelReadinessPanel`** (Q318, `6b1258c`·`76b5ff0`) — Solapi·SMTP·필수 알림톡 템플릿 **설정 여부**와 **라이브 발송 준비**·**조용한 시간대(22:00~08:00 KST)** 를 확인합니다. 각 설정 표 앞에 **섹션 제목(`<h3>`)** 이 표시되어 시각적으로 구분됩니다(UXD-97). API 키 등 **비밀값은 표시되지 않습니다**. **`branch_admin`** 은 **대시보드**(`/dashboard`) 하단 동일 패널에서도 확인할 수 있습니다.
7. **「배차·카카오 API」** 카드 (Q554, FE `138ac26`/`ba74bb5`) — **`TransportKakaoApiStatusPanel`** — **`GET /api/v1/transport/kakao-api-status`** — REST 키 설정 여부 · **Geocode·Directions** 연결 상태 Badge · **「오늘 API 사용량 (ogada 백엔드 기준)」** 테이블 — **좌표(Geocode)·경로(단일)·경로(다중경유)** 각 **오늘 사용·일일 한도·잔여 추정** · **한도 초과** warning · [Kakao Developers 콘솔](https://developers.kakao.com/console/app) 링크 **(새 탭)** (UXD-143). **브라우저 JS SDK·콘솔 Quota와 다를 수 있음** 안내가 표시됩니다.

| 설정 | 기본값 | 설명 |
|------|--------|------|
| `allowClientSelfCheckin` | **꺼짐** | 켜짐 — `client_user` 계정·본인 QR 체크인 허용 (Q113) · 꺼짐 — **보호자만** QR |
| `claimGenerationBasis` | **`ATTENDANCE_SCHEDULE`** | **급여일정(출석) 기반** 월별 청구 생성 |
| `claimGenerationBasis` | **`NHIS_IMPORT`** | **공단 청구내역 엑셀** import 일수 기반 — 해당 월 import **선행 필수** |

**`NHIS_IMPORT` 선택 시** — 패널에 **NHIS import** 링크 안내가 표시됩니다. 중도퇴소·조기정산 등 **공단 청구 일수와 출석 일수가 다른** 센터에서 사용합니다.

#### 5-5-1. 청구시작 기준금액 (G33, BNK-94~98, Q269·Q270)

ogada **도입 직후** 기존 수기·타 ERP에서 이관한 **미수·선납 본인부담금**을 반영합니다 (케어포 PDF **「7-3.청구시작 금액설정」**).

1. **`hq_admin`** 으로 **조직 설정**(`/organization/settings`) → **「청구·정산」** 카드를 내립니다.
2. **「청구시작 기준금액 (G33)」** 섹션에서 아직 설정하지 않았다면 **「1회만 설정 가능」** warning 안내(`BillingStartBalanceOneTimeWarning`, Q273)와 입력 폼이 표시됩니다.
3. **기준금액(원)** — **양수(+)** 는 **도입 전 미납**, **음수(-)** 는 **도입 전 선납**입니다 (서버 규칙).
4. **적용 시작월**(`YYYY-MM`) — ogada에서 본인부담금 추적을 **시작하는 달**입니다.
5. (선택) **메모** — 예: 「2026-03까지 엑셀 미수」.
6. **「기준금액 설정」** — 성공 시 **설정 완료** 요약(금액·적용월·설정 일시)과 **잠금 안내**(`BillingStartBalanceLockedNotice`, Q273)만 표시되며 **다시 변경할 수 없습니다** (`0ba2b68` — 백엔드가 `locked` 플래그를 생략해도 스냅샷으로 폼이 닫힙니다).

| 반영 위치 | 동작 |
|----------|------|
| **청구대장** | **적용 시작월** 조회 시 표 **맨 위** **「청구시작 기준금액 (G33)」** 행 (`OPENING_BALANCE`) |
| **미납 관리** | **양수 미납**이고 적용월이 **당월 이전**이면 목록에 표시 — **보호자 안내 발송 없음** |
| **청구 생성 가드** | **미정산 G33 미납**이 있으면 **`GET /billing/claims/generation-guard`**·`/billing` 배너에서 **생성 차단** (Q270) |
| **정산** | **`POST /settings/billing/start-balance/settle`** — **BE+FE Fixed** (`359cf0c`, Q270) — 아래 **화면 절차** |

> **주의**: 잘못 입력하면 **DB 직접 수정 없이는 되돌릴 수 없습니다**. 온보딩 전 **엑셀·장부와 금액·월을 대조**하세요.

> **화면 라벨**: 요약 표의 「(미납)/(선납)」 괄호는 **서버 부호와 반대**로 보일 수 있습니다. **금액 부호·미납 목록**을 기준으로 확인하세요 (Q270).

**G33 미납 정산 (화면, `hq_admin`·`branch_admin`, Q270 Fixed)**

1. **조직 설정**(`/organization/settings`) → **「청구·정산」** — G33 요약에 **미납 잔액**이 있으면 **「미납 정산」** 을 클릭합니다.
2. 또는 **청구 → 미납 관리**(`/billing/overdue`) — **「청구시작 기준금액 (G33)」** 행의 **「미납 정산」** 을 클릭합니다.
3. **`BillingStartBalanceSettlementModal`** 에서 **입금 금액**(기본=잔액 전액)·**입금일**·**수단**(현금/계좌이체)을 입력하고 저장합니다.
4. 성공 시 **잔여 미납**이 갱신됩니다. 정산 응답에 G33 스냅샷이 없어도 패널이 **설정 API를 재조회**해 잔액을 동기화합니다 (`eb48879`, Q273). **0원**이면 미납 목록·청구 생성 가드에서 G33 조건이 해소됩니다.
5. **부분 정산** — 금액을 잔액보다 작게 입력하면 **일부만** 차감됩니다.

> **CMS 정산**: API는 **`CMS`** 수단을 지원하나, **현재 화면 UI는 현금·계좌이체만** 제공합니다. CMS 정산은 Swagger를 사용하세요.

**G33 미납 정산 (Swagger 대안)**

1. **`POST /api/v1/settings/billing/start-balance/settle`**
2. 본문 예: `{ "paidAt": "2026-06-10", "paymentMethod": "BANK_TRANSFER", "amount": 50000 }`
3. **`amount` 생략** — 잔여 미납 **전액** 정산.
4. 성공 시 **`remainingAmount`** 가 **0**이면 미납 목록·청구 생성 가드에서 G33 조건이 해소됩니다.
5. **선납(음수)** 잔액은 정산 API 대상이 **아닙니다**.

> **`/settings` vs `/organization/settings` (Q178·Q201·Q554)**: **`sysadmin`** — SideNav **시스템 설정**(`/settings`) — **5탭**(보안·**카카오 API**·로그인 이력·감사·백업) · **「카카오 API」** 탭 — **`TransportKakaoApiStatusPanel`** — **`GET /transport/kakao-api-status`** (Q554) · **보안** 탭 **「비밀번호 변경」** → **`PasswordChangeModal`** (`POST /auth/change-password`, Q122). **`hq_admin`** — SideNav **조직 설정**(`/organization/settings`) — 셀프 체크인·**청구 생성 기준**·**「배차·카카오 API」** 카드(동일 패널, Q554). `hq_admin`이 `/settings`에 접근하면 **권한 없음**(`/forbidden`)입니다.

#### API (IT·Swagger)

| API | 권한 | 본문 |
|-----|------|------|
| `GET /api/v1/organization` | `hq_admin` | 현재 `allowClientSelfCheckin` 조회 |
| `PATCH /api/v1/organization/settings` | `hq_admin` | `{ "allowClientSelfCheckin": true }` |
| `GET /api/v1/settings/billing` | `hq_admin`·`branch_admin` | `{ "claimGenerationBasis": "ATTENDANCE_SCHEDULE" }` |
| `PATCH /api/v1/settings/billing` | `hq_admin` | `{ "claimGenerationBasis": "NHIS_IMPORT" }` |
| `GET /api/v1/billing/claims/generation-guard` | `hq_admin`·`branch_admin` | `?branchId=&yearMonth=` — 전월 미입금 사전 점검 (Q225) |
| `GET /api/v1/billing/monthly-benefit-caps` | `hq_admin`·`branch_admin`·`social_worker` | `?year=2026` — 등급별 재가급여 월한도 참조표 (Q226) |
| `GET /api/v1/billing/claims/monthly-cap-guard` | `hq_admin`·`branch_admin` | `?branchId=&yearMonth=` — 월한도 초과 **경고**(non-blocking, Q226) |
| `GET /api/v1/billing/fee-surcharge-rates` | `hq_admin`·`branch_admin`·`social_worker` | G11 가산율 catalog (Q229) |
| `POST /api/v1/billing/fee-surcharge-preview` | `hq_admin`·`branch_admin`·`social_worker` | ① `{ "baseAmount", "surchargeCode" }` 또는 ② `{ "baseAmount", "serviceStartAt", "serviceEndAt" }` — 가산 미리보기 (Q229) |
| `POST /api/v1/settings/billing/start-balance` | `hq_admin` | G33 **1회** 기준금액 설정 (Q269) |
| `POST /api/v1/settings/billing/start-balance/settle` | `hq_admin`·`branch_admin` | G33 **미납 정산** — `paidAt`·`paymentMethod`·`amount`(선택) (Q270) |
| `POST /api/v1/billing/imports/bank-deposits` | `hq_admin`·`branch_admin` | `multipart` `branchId` + `file` — 은행 일괄입금 (Q227) |

### 5-6. 청구·NHIS 엑셀 대조

센터장과 동일하게 `/billing`에서 청구서를 생성·확정할 수 있습니다. 추가로 **전 지점 청구 현황 조회**, **상태 필터**(`?status=CONFIRMED` 등), **공단 엑셀 import 대사**를 수행합니다.

1. 롱텀에서 받은 **청구내역상세** 엑셀을 업로드합니다.
2. import 결과에서 행별 상태를 확인합니다.

| 대사 상태 | 의미 |
|----------|------|
| `MATCHED` | 공단 데이터와 ogada 이용자·청구 일치 |
| `UNMATCHED` | 이용자 매칭 실패 — 인정번호·이름 확인 필요 |
| `DISCREPANCY` | 이용자는 매칭되었으나 일수·금액 불일치 — **「비교」** Modal로 공단 vs ogada 확인 후 출석·등급 재점검 (Q135) |
| `PENDING_REVIEW` | 공단 처리 **대기·보류** — 심사 완료 후 **엑셀 재import** (G7, Q181). 수동 연결·비교 **불가** · **「보류 사유」**열 확인 (Q182) |

#### NHIS `DISCREPANCY` 비교 (US-G06)

`DISCREPANCY` 행에서 **「비교」** 를 누르면 청구액·이용일수를 공단 데이터와 ogada 내부 청구 라인으로 나란히 확인할 수 있습니다.

1. 대사 상세(`/billing/imports/nhis/:batchId`)에서 **`DISCREPANCY`** 행의 **「비교」** 를 클릭합니다.
2. Modal에서 **공단(NHIS)** · **ogada 청구** · **차이** 열을 확인합니다.
3. 차이가 있으면 **「공단 초과」** 또는 **「공단 부족」** Badge와 함께 금액·일수가 표시됩니다.
4. 하단 **「ogada 청구 라인 상세 보기」** 로 청구 명세를 열어 출석·등급을 재점검합니다 (`claimId` 연결 시).

> **접근성**: 비교 표는 스크린리더용 `caption`·열/행 `scope`를 제공합니다. Tab으로 Modal 내부만 이동·ESC로 닫을 수 있습니다 (USER_MANUAL §3-2).

#### NHIS 수동 매칭

센터장과 동일하게 `UNMATCHED` 행에 대해 **후보 이용자 검색**(`SearchInput`·`?q=`)·**수동 연결** UI를 사용할 수 있습니다 (§4-6-1, FE `f01e3a8`). 전 지점 import 배치는 `GET /api/v1/billing/imports/nhis?branchId=&yearMonth=`로 조회합니다.

### 5-7. 지점 QR 생성·게시 (`/attendance/qr/generate`)

센터장·통합 관리자는 보호자 셀프 체크인용 **입소·귀가 QR**을 발급·게시합니다 (US-E03, Q624).

1. **출석** → **QR 생성**(`/attendance/qr/generate`)으로 이동합니다.
2. 상단 **`BranchScopeNotice`** 에서 **조회 지점**을 확인합니다 (Q173). 다지점 `hq_admin`은 **지점 선택기** 전환 후 QR을 발급하세요.
3. **입소** 또는 **귀가** 유형을 선택합니다 (기본 유효 시간 **480분**).
4. **「QR 생성」**을 누르면 **PNG QR 이미지**가 표시됩니다.
5. **「이미지 저장」** 또는 **「인쇄」**로 지점 입구에 게시합니다.
6. 유효 시간이 지나면 새 QR을 생성해 교체합니다.

> **API (Fixed, FE `250619e`)**: **`POST /api/v1/branches/{branchId}/qr`** — `{ "direction": "in"|"out", "expiresInMinutes": 480 }` → **`qrToken`** · FE **`branchQrCode.js`** 가 **`qrcode`** 라이브러리로 PNG data URL을 생성합니다.

**보호자 체크인 (US-E04)**

1. 보호자가 **`/guardian/checkin`** 에 로그인합니다.
2. **대상 이용자**를 선택하고 **입소/귀가**를 고릅니다.
3. 스마트폰으로 게시된 QR을 스캔하거나, **`qrToken`** 을 입력합니다.
4. **`POST /api/v1/attendance/qr/scan`** — `{ "qrToken": "...", "clientId": "<uuid>" }` 로 출석이 기록됩니다.

> **P3**: **`GuardianCheckinPage`** **카메라 스캔 UI**는 후속입니다 — 현재는 **토큰 수동 입력** 또는 외부 QR 앱 스캔 후 토큰 복사를 사용합니다 (FAQ Q109).

### 5-8. 배차·이동경로 (`/transport`, v1.3-A / IA 154차 / US-T02)

통합 관리자·직원이 **당일 승차·하차 운행 루트·배차 명단·수동·자동 배차**를 한 화면에서 관리합니다 (BE `114411f` + FE `d3bef42`, US-T01~T03). **이동서비스 수칙·계약(G15)** 은 **`/transport/compliance`** 로 분리되었습니다 (§5-8-0, Q397). 화면 상단 **`TransportContextNav`** 로 **배차·수칙·차량·청구·외출·월간 리포트**를 전환합니다.

| 화면 | 경로 | 역할 | 조작 |
|------|------|------|------|
| 배차 홈 | `/transport` | 직원 4역할 | **운행 방향**(승차/하차) → **운행 루트** → **배차 명단** → **`hq_admin`** 자동(승차만)·수동 배차 |
| **수칙·계약 (G15)** | `/transport/compliance` | 직원 4역할(저장: 관리 3역할) | §5-8-0 — 5항목 수칙·계약서·제18호 안내 |
| **월간 리포트 (G15 2-7/2-8)** | `/reports/transport-monthly` | `hq_admin`·`branch_admin`·`social_worker` | §5-8-0-2 — 변동현황·입소자·일정·서비스 집계 |
| **차량 관리** | `/transport/vehicles` | 조회: 직원 4역할 · 등록/수정: `hq_admin`·`branch_admin` | §5-8-3 (G16, Q241·Q402) |
| 이동서비스비 청구 | `/transport/service-fees` | `hq_admin`·`branch_admin`·`social_worker` | §5-8-1 (G16, Q239) |
| 외출 관리 | `/transport/outings` | 직원 4역할 | §5-8-2 (G15, Q240) |
| 외출 리포트 | `/reports/client-outings` | `hq_admin`·`branch_admin`·`social_worker` | §5-8-2 |
| 수동 배차 생성 | `/transport/runs/new` | **`hq_admin` only** | 방향(승차/하차) · 명단 **다중 선택** → **차량** → **`TransportRouteSplitView`** 순서·**지점 추가** → **임시 저장(DRAFT)** |
| 루트 상세 | `/transport/runs/:runId` | `hq_admin`(편집·확정·**DRAFT 삭제**·확정 취소) · 직원(**확정 루트만** 조회) | split-view 정차·지도·**차량**·**배차 확정**·**삭제(Q403)**·**확정 취소** |

1. SideNav **이동 → 배차·이동경로**로 이동합니다 (또는 **`TransportContextNav`** **배차·이동경로** 탭).
2. **`BranchScopeNotice`** 로 **조회 지점**을 확인합니다 (Q173).
3. 상단 **`TransportDisclaimer`** 를 읽습니다 — **운영 편의용**이며 이동서비스비 청구(G16)는 **`/transport/service-fees`** 입니다.
4. **「운행 방향」** — **승차(PICKUP)** / **하차(DROPOFF)** segmented control로 전환합니다 (Q399). 운행 루트·명단·수동 배차가 **선택한 방향**에 맞게 갱신됩니다. **자동 배차 제안**은 **승차**에서만 표시됩니다.
5. **「운행 루트」** 카드 — **운행일** `DateInput` 선택 → 당일 **선택 방향**의 **DRAFT/CONFIRMED** 루트 목록(상태·정차 수·차량·확정 시각) · **보기** → `/transport/runs/{runId}`. **`branch_admin`·요양보호사·사회복지사**는 **CONFIRMED** 루트만 표시됩니다.
6. **「배차 신청 인원 명단」** — 당일 roster · **연락처**(`contact`)·**보호자 연락처**(`guardianContact`, Q398) · **희망 탑승 시각**·**희망 하차 시각** (Q400) · **배차 루트** — 확정 루트에 배정된 이용자는 **「N번 정차」** 링크로 **`/transport/runs/:runId`** 바로가기 (Q433, `e35efb2`) · **계획 픽업**(승차) / **계획 하차**(하차) — 확정 루트 정차의 계획 시각 · **자동 배차 제안 직후**에는 **DRAFT 제안 루트의 반영도착 ETA**도 명단에 **「계획 픽업」** 으로 표시됩니다 (Q553, `acc5933`) · 희망 시각보다 늦으면 **「지연」** Badge (Q433) · **`TransportPickupContact`** — **`hq_admin`** 만 전체 번호·`tel:` 링크, 그 외 **`010-****-5678`** 마스킹 (Q171·Q172).
7. **`hq_admin` only — 배차 생성 (승차, v1.3-B, Q424)** — 화면 하단 **「배차 생성」** 영역에서 **자동·수동 배차**가 **나란히** 표시됩니다 (`96db8bf`). **승차** 방향일 때만 왼쪽 **「자동 배차 제안」** 카드가 보입니다 — **`TransportSuggestPanel`** 안에 **최적화 설정**(`BranchTransportSettingsPanel` **embedded**) · 픽업 허용 ±분 · OR-Tools 가중치(안정성·공정성·거리) · **필드 tooltip** · **0.1 단위** 입력 · **「설정 저장」** — 빈 가중치는 **저장 전 필드 오류**로 차단됩니다 (`transportSettingsForm.js`, Q424). **「자동 배차 제안」** 클릭 시 버튼·Spinner가 **「자동 배차·경로 계산 중…」** 으로 표시됩니다 (Q553). **`POST /api/v1/transport/runs/suggest`** · **일 10회** 상한 · 제안 DRAFT는 **출발·복귀 지점(BRANCH) 정차 포함** · BE suggest 응답에 **`legDurationsSeconds`·`routePath`·거리·소요** 가 포함되어 FE가 **즉시 ETA·지도 polyline** 을 채웁니다 (Q554, `e2b764b`). **「반영도착」** 열 — 경로 legs가 없으면 **「경로 미확인」** (Q554). **「DRAFT 검토」** 링크는 **경로 미리보기 결과**를 루트 상세로 전달해 **지도·정차 time chip** 을 즉시 채웁니다. **운행 루트**에서 검토 (Q347·Q424).
8. **`hq_admin` only — 수동 배차** — 오른쪽 **「승차/하차 수동 배차」** 카드 — **「승차/하차 수동 배차 생성」** → `/transport/runs/new` (방향·운행일 state 전달) · 해당 방향에 **이미 확정 배차에 포함된 이용자**는 선택 불가. **하차(DROPOFF)** 방향에서는 **수동 배차 카드만** 표시됩니다.
8a. **이전 배차 불러오기 (Q550, FE `4681b5a`)** — **`/transport/runs/new`** 상단 **「이전 배차 불러오기」** → **`TransportLoadPreviousRunModal`** — **과거 운행일**·**차량** 선택 → **CONFIRMED/DRAFT** 루트의 **정차 순서·지점·경유지**를 **당일 roster** 기준으로 복원합니다. **퇴소·확정 배차 포함·15명 초과** 이용자는 **건너뛰기 목록**에 표시됩니다 (`buildStopsFromPreviousRun`).
9. 수동 배차 화면 상단 **「출발 시각」** (`Field` + **`TimeInput`**, Q418·Q422) — 기본값 **08:00** · 5분 단위 시·분 선택 · **`POST /api/v1/transport/runs`** 시 **`plannedDepartureTime`**(HH:mm:ss)로 저장 (**V150**). **DRAFT 루트 상세**에서도 **`PATCH /api/v1/transport/runs/{id}`** 로 **`plannedDepartureTime`** 수정 가능 (Q550, BE `48eea95`).
10. 수동 배차 화면 **`TransportRouteSplitView`** (Q401·**Q418·Q420·Q421·Q458·Q550**) — **상단 경로 지도** · **하단 정차 목록**(드래그 순서 변경) — **세로 배치** (`fde098f`). **`지점 추가`**(**BRANCH**) · **`경유지 추가`**(**WAYPOINT**, `bf73c4c`) · **DRAFT 루트 상세** — **`명단에서 추가`**(**`TransportAddRosterModal`**, Q550) — 당일 roster에서 **미포함 이용자**를 **다중 선택** 추가 · **이미 확정 배차에 포함된 이용자**는 선택 불가. **공백만 입력한 주소는 저장되지 않습니다** (V155 DB `btrim` guard, Q458). 정차 **time chip** — **희망 탑승/하차** · **예상 도착** · **희망 반영** — 희망보다 늦으면 **지연 강조**. **`legDurationsSeconds`** + 출발 시각 → **`transportMapEtas.js`**.
11. **`TransportVehicleSelect`** 로 **지점 차량**을 지정합니다 — 차량 **기본 운전자명**이 라벨에 표시됩니다 (Q402). 정차 수가 차량 **정원(capacity)** 을 초과하면 경고가 표시됩니다 (Q241).
12. **지도 제외 주소**(geocode `FAILED` 또는 **좌표 미보유**)가 있으면 상단 **경고 Alert**가 표시되고 **임시 저장·순서 저장·배차 확정**이 **차단**됩니다 (QA-B19, Q233).
13. **퇴소·비활성 이용자**는 roster·수동 배차 명단에 **표시되지 않습니다**. 퇴소 직전에 만든 **DRAFT** 루트에 해당 정차가 남아 있으면 **저장·확정이 거부**됩니다 — 정차를 **삭제**하거나 roster를 갱신하세요 (**V152 Fixed** @ `dd2fa2c`, FAQ **Q423**·**Q235**).
14. **희망 탑승 시각 검증 (Q550, FE `4681b5a`/BE `48eea95`)** — **배차 확정** 클릭 시 **`TransportConfirmWarningModal`** 이 **예상 도착 지연**·**정차 순서·희망 시각 불일치**를 표시합니다. **지점 배차 설정**의 **픽업 ±(분)**(`pickupToleranceMinutes`, 기본 15분) 허용 범위를 반영합니다. **「그래도 확정」** 으로 진행하거나 **취소** 후 순서·시각을 조정합니다. 서버는 **정차 순서에 맞지 않는 희망 시각**을 **`422 BUSINESS_RULE`** 로 거부합니다 — 「정차 순서에 맞지 않는 희망 탑승 시각이 있습니다…」.
15. **임시 저장** 후 루트 상세에서 순서·지도·**차량**·**출발 시각**을 확인하고 **배차 확정**(`CONFIRMED`)합니다.
16. 확정 루트 상세 **`TransportServiceLogPanel`** (G15, Q236·**Q407·Q411**, BE `0cfa970`/`aaaeb10`/`aa42b9c` / FE `088e906`/`dff2f32`) — **별지 제22호 이동서비스일지**:
   - **CONFIRMED** 루트는 **`GET /api/v1/transport/runs/{runId}/service-log`** 로 일지를 불러옵니다 — **차량번호**·**운전자**는 배차·차량 마스터에서 **읽기 전용** 표시
   - **동승 직원**(`companionName`)·정차별 **실제 픽업 시각**·**동승 여부**·**하차 시각** 입력 — 정차가 여러 명이면 **Field 라벨에 이용자명**이 포함됩니다 (QA-B116)
   - 계획 픽업 대비 **15분 이내** **`StatusBadge`「준수」** / 초과 **「지연」** / 미입력 **「미기록」** (평가 지표 42, **`TransportTimeCompliance`** — 색상만으로 구분하지 않음)
   - **「일지 보관·감사 추적」** — 배차 확정 시각 · **DB 저장 기록** 건수 · **마지막 저장** 시각 · **저장 상태**(미저장 변경·일부 미기록 경고)
   - **법정 보관 안내** — 시행규칙 제34조 일지 작성·보관 의무 · **`/transport/compliance`** 링크
   - **「일지 기록 저장」** — **`PUT /api/v1/transport/runs/{runId}/service-log`** 로 서버에 영속화 (**V148**) — 성공 시 **`TRANSPORT_SERVICE_LOG_UPSERT`** 감사 로그 기록 (`aa42b9c`)
   - **「인쇄」** / **「텍스트 저장」** — **미저장 변경** 또는 **일부 정차 미기록** 시 **차단** · 저장 후에만 보관용 출력 권장
   - **미확정(DRAFT)** 루트는 **미리보기**만 — **서버 저장 버튼 없음** · 제출용 출력은 **확정 후** 권장
17. **`hq_admin`** 이 확정 루트를 되돌려야 하면 루트 상세 하단 **「확정 취소」** → **`TransportUnconfirmModal`** 확인으로 `DRAFT` 복원 후 **순서 저장** → **배차 확정** 재실행합니다 (UXD-47, FAQ **Q163**).
18. **`hq_admin`** 이 **임시 저장(DRAFT)** 루트를 버리려면 루트 상세 **「삭제」** → **`TransportDeleteRunModal`** 확인으로 삭제합니다 (Q403, BE `1d1a71f` / FE `45bd923`). 모달에는 **운행일**·**정차 수**가 표시되고 **「삭제한 배차는 복구할 수 없습니다」** 경고가 나타납니다. **확정 루트는 삭제할 수 없습니다** — 확정 취소 후 편집하세요.
19. 직원(`branch_admin`·요양보호사·사회복지사)은 **`CONFIRMED`(확정)** 상태 루트만 조회합니다 — `DRAFT`는 목록에서 숨겨집니다. 확정 루트 상세에는 **「읽기 전용」** 안내(US-T03)가 표시되며, 정차 목록·지도·geocode **Badge**로 좌표 변환 상태를 확인할 수 있습니다 (UXD-48). **픽업 주소**는 **`hq_admin`이 아닌 역할**에게 **시·구 수준 마스킹**(`e7d4cf6`, `서울시 중구 ***` 등, Q169).
20. **Windows 고대비 모드**(Q115·Q168) — 지도 캔버스·정차 카드·마커에 **경계선**이 표시되고, 활성 마커·순번 Badge·강조 정차는 **Highlight outline**으로 식별됩니다. 색상만으로 순서를 구분하지 않습니다 (UXD-50).
21. **도로 경로 미리보기 (Q370·Q394·Q395·Q401·Q404·Q418·Q553, FE `10489a7`/`5ebaade`/`0e46b37`/`acc5933`)** — **`KakaoTransportMap`** 이 **`loadKakaoMapSdk`** 로 Kakao Maps **JavaScript SDK**를 로드하고, **`kakaoMapInstance.js`**·**`useKakaoMap`** 으로 지도 인스턴스를 관리합니다. **`KakaoTransportMapView`** 에서 **번호 마커**·정차 **도로 폴리라인**·**하이라이트 동기화**를 표시하며, **route-preview 응답 전**에도 좌표가 있으면 **seed markers**로 마커를 먼저 표시합니다. **지점 핀**은 스크린리더에 **「지점(센터) 정차」** 로 읽히고, 하단 **범례**에 **파란 선=도로 경로·회색 점선=정차 안내선·「센」=지점** 이 표시됩니다 (Q404). **`POST /api/v1/transport/route-preview`** 로 **실제 도로 경로**·**구간별 소요 `legDurationsSeconds[]`** 를 받으며, 정차 좌표는 **`pickupLat`/`pickupLng`** 또는 geocode 결과를 사용합니다 — **건물번호 일치** 시 Kakao 후보 우선 (`1d1a71f`). **동일 주소 geocode**·**동일 정차 시그니처 route-preview** 는 **탭 세션 in-memory 캐시**로 재사용되어 suggest→DRAFT 검토·수동 배차 화면 전환 시 **중복 API 호출**을 줄입니다 (Q553, `transportRunPreviewCache.js`·`kakaoMapGeocoder.js`). 지도 캔버스는 **`role="application"`**·**`aria-label`** 로 스크린리더에 구역을 알리고, 상단 **거리·예상 소요 시간** 요약은 **`role="status" aria-live="polite"`** 라이브 영역입니다. **`VITE_KAKAO_MAP_JS_KEY`** 미설정·SDK 로드 실패 시 **Spinner 대신 경고 Alert**가 표시되고 **정차 목록은 계속** 확인할 수 있습니다 (FAQ **Q394·Q395**). **`/transport`** 목록 로딩은 **`AbortController`** 로 이전 요청을 취소해 **로딩 stuck** 을 방지합니다 (`fde098f`, Q420).

> **G16 Partial Fixed (Q239)**: ogada는 **확정 배차 기반 이동서비스비 청구 기록 생성·확정**까지 지원합니다 — **공단 포털 제18·19·20호 자동 제출**은 **미지원** (Q237). §5-8-1 참고.

| API | 용도 |
|-----|------|
| `GET /api/v1/transport/roster?runDate=&direction=PICKUP\|DROPOFF` | 당일 배차 명단 — **`contact`·`guardianContact`·`desiredBoardingTime`·`desiredDropoffTime`** (Q398·Q400, `114411f`) |
| `POST /api/v1/transport/runs` | DRAFT 루트 생성 (`hq_admin`) — `direction` · optional **`plannedDepartureTime`** (Q418, `0e46b37`, **V150**) · `stops[]` with **`stopKind` CLIENT/BRANCH/WAYPOINT** (US-T02, Q421) — WAYPOINT 시 **`waypointAddress`**(필수)·**`waypointLabel`**(선택) · optional `vehicleId` |
| `PATCH /api/v1/transport/runs/{id}` | DRAFT 정차 순서·**`plannedDepartureTime`**·차량 수정 (Q550, `48eea95`) — **희망 시각 순서 검증** |
| `POST /api/v1/transport/runs/{id}/confirm` | 배차 확정 |
| `PATCH /api/v1/transport/runs/{id}/unconfirm` | 확정 취소 → DRAFT (`hq_admin`, Q163·Q164) |
| `DELETE /api/v1/transport/runs/{id}` | **DRAFT 루트 삭제** (`hq_admin`, Q403, `1d1a71f`) — **204** · CONFIRMED 시 **422** |
| `GET /api/v1/transport/runs/{runId}/service-log` | **별지 제22호 일지 조회** (Q407, `0cfa970`) — 확정·DRAFT 모두 조회 가능 · **`TransportServiceLogResponse`** |
| `PUT /api/v1/transport/runs/{runId}/service-log` | **일지 준수 기록 저장** (Q407, `aaaeb10`) — **CONFIRMED only** · 동승 직원·정차별 실제 픽업·동승·하차 시각 · **`TRANSPORT_SERVICE_LOG_UPSERT` audit** (`aa42b9c`, Q411) |
| `GET /api/v1/transport/runs/{runId}/service-log/audit-trail` | **일지 저장 이력 조회** (Q411, `5994d15`) — 최근 **50건** · `runDate`·정차 갱신·준수 요약 |
| `GET /api/v1/transport/reports/monthly-service-variation?yearMonth=` | **월간 서비스 변동현황** (G15 2-7, Q410, `5d27ad3`) — 신규·퇴소·계약 변동 |
| `GET /api/v1/transport/reports/monthly-resident-status?yearMonth=` | **월간 입소자·일정·서비스 현황** (G15 2-8, Q410, `5d27ad3`) — 확정 배차·탑승 정차·계약 서명 |
| `POST /api/v1/transport/runs/{id}/unconfirm` | 위와 동일 (레거시 alias — 현재 FE 호출) |
| `POST /api/v1/transport/geocode` | 주소 → 좌표 (Kakao REST proxy) |
| `POST /api/v1/transport/route-preview` | **도로 경로 미리보기** — 지점·정차 좌표 → polyline·거리·시간·**`legDurationsSeconds[]`** (Q370·**Q418**, `e8b8398`/`0e46b37`) |
| `GET /api/v1/transport/contracts/{clientId}` | 이동서비스 계약서 조회 (Q231) |
| `PUT /api/v1/transport/contracts/{clientId}` | 수칙 5항목·이중 서명 저장 (Q231) |
| `POST /api/v1/transport/runs/suggest` | **v1.3-B** 자동 배차 제안 — **`hq_admin` only** · **PICKUP** · 응답 **`legDurationsSeconds`·`routePath`·`routeDistanceMeters`·`routeDurationSeconds`** (Q554) · **`TransportSuggestPanel`** (Q347, FE `2ffe59f`) |
| `GET /api/v1/transport/kakao-api-status` | **Kakao REST API 상태·ogada 오늘 사용량** — **`hq_admin`·`sysadmin`** · **`TransportKakaoApiStatusPanel`** (Q554, `e2b764b`/`ba74bb5`) |
| `GET /api/v1/transport/settings` | **v1.3-B** 지점 배차 최적화 설정 조회 — **`hq_admin` only** |
| `PUT /api/v1/transport/settings` | **v1.3-B** 픽업 허용분·OR-Tools 가중치 저장 — **`BranchTransportSettingsPanel`** |
| `GET/POST/PATCH /api/v1/transport/vehicles*` | 차량 마스터 CRUD — **`VehiclesPage`** (Q241) |
| `GET /api/v1/clients/{id}/care-provision-records/{yearMonth}` | 월간 급여제공·이동서비스·차량 대조 (Q243) |

> **명단이 비어 있을 때**: 이용자 **`usesTransport=true`** (V47)인 경우만 roster에 표시됩니다. **이용자 등록·수정** 화면 **「배차·픽업 정보」**에서 설정하세요 (§4-3, Q166). 저장 후 **`/transport`** 에서 운행일을 새로고침합니다.
>
> **지도가 안 보일 때**: (1) **`/organization/settings`·`/settings` → 「배차·카카오 API」** — REST 키·Geocode·Directions 상태 확인 (Q554) (2) 서버 **`KAKAO_REST_KEY`** — geocode·경로 API (3) 프론트 **`VITE_KAKAO_MAP_JS_KEY`** — **`loadKakaoMapSdk`** (4) JS 키 **Web 도메인**에 접속 URL 등록 (FAQ **Q370·Q394·Q395·Q554**, DEPLOYMENT §4-7).

#### 5-8-0. 수칙·계약 (`/transport/compliance`, G15, Q397)

**2026 평가 지표 41·42** 대응 **이동서비스 수칙·계약·일지 안내** 전용 화면입니다 (FE `84e75ec`, **`TransportCompliancePage`**). 배차 화면(`/transport`)과 **분리**되어 수칙·계약 업무에 집중할 수 있습니다.

1. SideNav **이동 → 수칙·계약 (G15)** 또는 **`TransportContextNav` → 수칙·계약** 으로 이동합니다.
2. 당일 **배차 명단**이 자동 로드됩니다 — **`GET /transport/roster`** (운행일 = 오늘, PICKUP).
3. **`TransportServiceLogLegalGuide`** (Q446, FE `0df6902`) — **「법정 이동서비스일지 입력 서식 (별지 제22호)」** 카드 — NHIS **고시 제34조 ④**·별지 제22호 **필수 입력 항목** 안내 · **「확정 배차 선택」** → 아래 일지 작성 목록 · **「배차 화면으로 이동」** → `/transport`.
4. **`TransportCompliancePanel`** (Q230·Q231) — **이동서비스 수칙 체크리스트**(5항목) · **계약서 템플릿** Modal · **별지 제22호 일지 예시** Modal. **이동서비스 이용(`usesTransport=true`)·활성·미퇴소** 이용자만 저장 가능 (V65, Q235). **이용자 선택** → 5항목 체크 → **보호자·기관 서명**·**서명일(`DateInput`, Q281)** → **저장**(`PUT /api/v1/transport/contracts/{clientId}`). **`hq_admin`·`branch_admin`·`social_worker`** 만 저장 · **`caregiver`** 조회만.
5. **`TransportServiceLogRunsPanel`** (Q426, FE `b93e098`) — **「이동서비스일지 작성 (별지 제22호)」** 카드 — 당일 **승차·하차 확정(`CONFIRMED`)** 배차 목록(방향·차량·정차 수·확정 시각) · 각 행 **「일지 작성·보관」** 링크 → **`/transport/runs/:runId`** 운행 상세 **`TransportServiceLogPanel`** (배차 화면 경유 없이 일지④ 진입). 확정 배차가 없으면 **「배차·이동경로로 이동」** 안내.
6. **`TransportForm18GuidePanel`** (Q237) — **별지 제18·19·20호** 공단 포털 **선행 신청 5단계** · **3분리 신청 유형** · **등록상태 4단**. ogada는 **자동 제출하지 않습니다** — 수칙·계약 → **제22호 일지**(§5-8-0-1) → **공단 포털 제18호** → **제19·20호** → **G16 청구**(§5-8-1) 순서.

> **G15 일지 (Q407/Q411/Q426, v1.3-C full stack)**: 확정 루트 **`TransportServiceLogPanel`** 에서 **서버 저장·감사 추적·보관 안내·인쇄·텍스트 다운로드**가 모두 지원됩니다. **수칙·계약 화면(`/transport/compliance`)** 에서도 확정 배차별 **일지 작성·보관** 링크로 바로 이동할 수 있습니다 (Q426). 수칙·계약(§5-8-0 step 3) 완료 후 일지를 기록하세요.

#### 5-8-0-1. 이동서비스 일지 기록 (별지 제22호, G15, Q407·Q411)

**2026 평가 지표 41·42** 대응 **이동서비스 일지(별지 제22호)** 기록·저장·보관·인쇄입니다 (BE `0cfa970`·`aaaeb10`·`aa42b9c`·`5994d15` + FE `088e906`/`dff2f32`/`3cc5a08`, **v1.3-C G15 full stack**, Q407·Q411).

**일일 일지 기록**

**경로 A — 수칙·계약 화면에서 바로가기 (Q426, 권장)**

1. SideNav **이동 → 수칙·계약 (G15)** 또는 **`/transport/compliance`** 로 이동합니다.
2. **「이동서비스일지 작성 (별지 제22호)」** 카드에서 당일 **확정 배차** 목록을 확인합니다.
3. 해당 운행 행의 **「일지 작성·보관」** 을 누르면 **`/transport/runs/:runId`** 로 이동합니다.
4. 아래 **step 4~7** 과 동일하게 **`TransportServiceLogPanel`** 에서 입력·저장합니다.

**경로 B — 배차 화면에서 진입**

1. SideNav **이동 → 배차** 또는 **`/transport`** 로 이동합니다.
2. **조회 기간**(기본: 오늘)과 **방향**(승차/하차, 분리 표시)을 선택 후 **운행 목록**에서 **확정(`CONFIRMED`)** 운행만 표시됩니다.
3. 확정 운행 **행을 클릭** → **상세 모달** → **「일지 기록」** 탭으로 이동합니다.
4. **`TransportServiceLogPanel`** — **별지 제22호 형식 표 진입**:
   - **운행 정보**: 운행일, 차량, 기사(read-only), **동승 직원**(`companionName`, 선택 입력)
   - **운전자 서명 (Q445·Q450, FE `f51e365`/`bfe0283` / BE `bc3a35c`)**: **「운전자 서명」** `fieldset` 안 **「서명 성명」**·**「서명일」** — **둘 다 입력**해야 **저장·인쇄·텍스트 다운로드**가 가능합니다. **감사 요약**에 **운전자 서명: 완료/미완료** 가 표시됩니다. 서명일은 **운행일 이후·오늘 이전**이어야 합니다.
   - **정차별 실적** (Q466·Q468, FE `7de5a6f`/`07be394` — 입력 폼이 **인쇄·텍스트 다운로드 표와 동일 열** 구성): 각 정차(이용자) `fieldset`마다 — **운행 방향**(`PICKUP` 승차 / `DROPOFF` 하차)에 따라 Field 라벨이 자동 전환됩니다:
     - **「탑승 장소」/「하차 장소」** (read-only): 배차·이용자 프로필의 **픽업 주소** — 별지 제22호 **주소란** 대응 (Q463·Q470). **하차(DROPOFF)** 루트는 **「하차 장소」** 로 표시됩니다. 주소가 없으면 help에 **「픽업 주소가 없습니다…」** 안내
     - **「계획 픽업」/「계획 하차」** (read-only): 배차 계획 시각
     - **「실제 픽업」/「실제 하차」**: 실제 탑승(또는 하차) 시각 (시:분) — 입력 시 **「시간 준수」** 값이 즉시 갱신
     - **「시간 준수」** (read-only): 계획 대비 **±15분** 허용 오차 기준 **`StatusBadge`「준수」/「지연」** — 인쇄·텍스트 다운로드 표와 **동일 Badge 패턴** (Q466·Q476, `7de5a6f`/`f8321c7`) — help에 허용 분 표시 (`TRANSPORT_TIME_COMPLIANCE_TOLERANCE_MINUTES`)
     - **「동승 여부」**: 예/아니오
     - **「하차 시각」**: 실제 드롭오프 시각 (시:분)
     - **「비고」** (read-only, Q468): API `note`에서 **픽업/하차 주소와 중복되는 `픽업:`/`하차:` prefix** 는 자동 제거 (Q471 — **DROPOFF** 루트는 **`하차:`** prefix) — 탑승/하차 장소 Field와 겹치지 않게 표시. 특이사항이 없으면 help **「픽업 주소 외 특이사항이 없습니다.」**
   - **요약**: 상단 **「시간 준수 N/M건」** 집계 — 정차별 read-only **「시간 준수」** 와 동일 기준

5. **법정 필드 검증 (Q439·Q443·Q445, FE `b4644e8`/`f51e365` / BE `ac1d43f`/`bc3a35c`)**: 정차별 **실제 픽업 시각**·**동승 여부(예/아니오)**·**하차 시각**과 **운전자 서명 성명·서명일**을 **모두** 입력해야 **저장·인쇄·텍스트 다운로드**가 가능합니다. 미입력 시 **`Field` 오류**와 「법정 보관 전…」 안내가 표시됩니다. 하차 시각이 픽업보다 이르면 저장되지 않습니다. API 직접 호출 시에도 서버가 동일 규칙으로 **`422`** 를 반환합니다.

6. **저장**: **`PUT /api/v1/transport/runs/{runId}/service-log`** — **CONFIRMED 운행만** 저장 가능. 본문에 **`driverSignatoryName`·`driverSignedOn`** 포함 (Q445).
   - **법정 필드 미입력** — 「실제 픽업 시각을 입력하세요.」·「동승 여부를 선택하세요.」·「하차 시각을 입력하세요.」·「하차 시각은 실제 픽업 시각 이후여야 합니다.」(Q443, BE `ac1d43f`)
   - **운전자 서명 불완전** — 「운전자 서명자명과 서명일을 함께 입력하세요.」·「운전자 서명일은 운행일 이전일 수 없습니다.」·「운전자 서명일은 오늘 이후일 수 없습니다.」(Q445, BE `bc3a35c`)
   - **동일 `clientId` 중복** — 「일지 대상 이용자가 중복되었습니다.」(Q440, BE `52e3340`)
   - 저장 성공 시 **`TRANSPORT_SERVICE_LOG_UPSERT`** 감사 로그가 기록됩니다.

7. **저장 이력 확인**:
   - **운행 상세 패널** — **「일지 보관·감사 추적」** 아래 **「일지 저장 이력」** 표에서 **일시·작업·내용**(운행일·정차 갱신·실제 기록·시간 준수) 확인 (`GET …/service-log/audit-trail`, `5994d15`/`3cc5a08`)
   - **테넌트 감사 로그** — **`sysadmin`·`hq_admin`** 은 **`/settings` → 감사 로그** 탭에서 동일 **`TRANSPORT_SERVICE_LOG_UPSERT`** 항목 확인 (Q411)

8. **보관·출력**:
   - **「일지 보관·감사 추적」** 패널에서 **배차 확정 시각**·**DB 저장 건수**·**마지막 저장**·**저장 상태**·**일지 저장 이력** 확인
   - **인쇄** — **법정 필드 미입력** · **미저장 변경** · **일부 정차 미기록** 시 경고 후 **차단** · 저장 완료 후 Print Dialog (`Ctrl+P` / `Cmd+P`) 또는 **「인쇄」** 버튼 (`ds-transport-log-printing`) — **기관(지점)명·주소·지역 경로·대표 연락처** 헤더 (Q469) — **대표 연락처**는 **`tel:` 링크**로 연결 (Q476, UXD-132) · 정차별 **픽업 주소**·**비고** 열 포함 (Q463·Q468)
   - **텍스트 다운로드** — 동일 가드 적용 후 **`.txt`** 파일 (기관 연락처·시간 준수 요약·**픽업 주소**·**비고** 포함, Q463·Q469)

**조회·확인**

- **`GET /api/v1/transport/runs/{runId}/service-log`** — 저장된 일지 조회 (응답: **`direction`** 승차/하차 Q471 · **`branchName`·`branchAddress`·`branchRegionPath`·`branchPhone`** 기관 연락처 Q469 · **`driverSignatoryName`·`driverSignedOn`·`driverSignatureComplete`** · 정차별 **`pickupAddress`** Q470 · 전체 정차·시간 정보·준수 요약, Q445)
- **`GET /api/v1/transport/runs/{runId}/service-log/audit-trail`** — 해당 운행의 **저장 이력** (최근 50건, 최신순)
- **일지 기록이 없으면**: 「일지 기록 안 함」 표시, 내용 비워두고 진행 가능
- **시간 기록 오류**: 15분 범위 벗어나면 **`StatusBadge`「지연」** — 내용은 저장되지만 준수 현황 표시

**권한 및 범위**

- **저장/수정**: **`hq_admin`·`branch_admin`·`social_worker`·`caregiver`** (모두 확정 운행에만 접근)
- **조회**: 동일 권한 + **`guardian`·`client_user`** (읽기만, 운행 미노출)
- **다지점 `hq_admin`**: 활성 지점(`active_branch_id`) 운행만 저장 가능 (BNK-300)

**갭 / 후속 (v2)**

- GPS 위치 자동 기록 (현재 수기 시간 기준)
- 근무 시간 규정 자동 검증

#### 5-8-0-2. 이동서비스 월간 리포트 (`/reports/transport-monthly`, G15 2-7/2-8, Q410)

**케어포 func.php 2-7·2-8** 대응 — 지점·월별 **이동서비스 변동**과 **입소자·일정·서비스 현황**을 집계합니다 (BE `5d27ad3` + FE `6a18dfd`). 기존 roster·runs·stops·contract 데이터를 **집계**하므로 **별도 DB 마이그레이션은 없습니다**.

1. SideNav **이동 → 배차·이동경로** 또는 **`TransportContextNav` → 월간 리포트** 로 **`/reports/transport-monthly`** 에 접속합니다.
2. **`BranchScopeNotice`** 로 **활성 지점**을 확인합니다 — 지점이 없으면 조회할 수 없습니다.
3. **「대상 월」** `MonthInput`으로 `YYYY-MM`을 선택하고 **「조회」** 를 누릅니다.
4. **월간 서비스 변동현황 (2-7)** — StatCard **신규 등록**·**퇴소**·**계약 변동**·**대상 월** · 표에 이용자별 **변동 유형**(신규 등록·퇴소·계약 신규·계약 갱신)·**발생일**·**내용**
5. **월간 입소자·일정·서비스 현황 (2-8)** — StatCard **이동 대상**·**확정 배차**·**서비스 이용**·**탑승 정차**·**계약 서명** · 표에 이용자별 **등급**·**확정 배차일**·**탑승 정차 수**·**계약 서명** 여부
6. **「인쇄」** — 화면 인쇄(`ds-billing-report-print-zone`)로 월간 점검 자료를 출력합니다.

| API | 용도 |
|-----|------|
| `GET /api/v1/transport/reports/monthly-service-variation?yearMonth=YYYY-MM` | 2-7 변동현황 — `summary`·`rows[]` |
| `GET /api/v1/transport/reports/monthly-resident-status?yearMonth=YYYY-MM` | 2-8 입소자 현황 — `summary`·`rows[]` |

> **권한**: **`hq_admin`·`branch_admin`·`social_worker`** 만 조회 가능 — **`caregiver`** 는 **403** (FAQ **Q410**).
>
> **활용**: 월말 **이동서비스 운영 점검**·계약 미서명 이용자·신규·퇴소 변동 추적에 사용합니다. 상세 일지는 §5-8-0-1 · 배차는 §5-8을 참고하세요.

#### [TWR] 5-8-0-3. 월간 리포트 수치가 예상과 다를 때 (운영 점검)

`/reports/transport-monthly` 수치가 내부 집계표와 다르면 아래 순서로 원인을 먼저 분리합니다.

1. **대상 월 확인**: 조회 월(`YYYY-MM`)과 실제 점검 월이 일치하는지 확인합니다.
2. **활성 지점 확인**: 상단 `BranchScopeNotice`의 지점과 운영자가 점검하려는 지점이 같은지 확인합니다.
3. **확정 상태 확인**: `2-8`의 확정 배차 수치는 **CONFIRMED 운행**만 집계되므로 DRAFT 운행은 제외됩니다.
4. **계약 서명 확인**: `2-8`의 계약 서명 수는 `G15 수칙·계약`의 저장 완료 건만 반영됩니다.
5. **변동 유형 확인**: `2-7`은 `NEW_TRANSPORT`·`DISCHARGED`·`CONTRACT_CREATED`·`CONTRACT_UPDATED`만 집계합니다.

> 운영 팁: 월말 마감 전에는 먼저 `2-7`에서 변동 원인을 확인하고, 이어서 `2-8`에서 확정·서명 누락을 점검하면 재집계 요청을 줄일 수 있습니다.

#### [TWR] 5-8-0-4. 일지 감사 이력이 안 보일 때 (권한/저장 분리 점검)

`/transport/runs/:runId`에서 일지 저장 이력 표가 비어 있거나 조회가 막히면 아래 순서로 점검합니다.

1. **권한 확인**: `service-log/audit-trail` 조회는 `hq_admin`·`branch_admin`·`social_worker`만 가능합니다. `caregiver`는 일지 저장은 가능하지만 감사 이력 조회는 403일 수 있습니다.
2. **저장 여부 확인**: 조회만으로는 이력이 생성되지 않습니다. **`PUT /api/v1/transport/runs/{runId}/service-log`** 성공 호출이 있어야 `TRANSPORT_SERVICE_LOG_UPSERT`가 남습니다.
3. **운행 상태 확인**: `DRAFT` 운행은 저장 자체가 422로 거부될 수 있으므로 먼저 `CONFIRMED` 상태를 확인합니다.
4. **감사 로그 교차 확인**: `/settings` 감사 로그에서 동일 `runId` 이벤트(`TRANSPORT_SERVICE_LOG_UPSERT`)가 있는지 확인합니다.

> 운영 팁: 월마감 표본 점검은 run 3건을 지정해 `summary.recorded == summary.total`과 감사 이력 존재 여부를 함께 확인하세요.

#### 5-8-1. 이동서비스비 청구 (`/transport/service-fees`, G16, Q239)

**케어포 2-5** 대응 — 확정 배차를 기반으로 **이동서비스비 청구 기록**을 생성·확정합니다 (BE `88d4c59` + FE `9dfef92`, BNK-25).

1. **`TransportContextNav`** → **「이동서비스비 청구」** (또는 `/transport/service-fees` 직접 접속).
2. **조회 기간**(기본: 당월)을 설정하고 **거리구간 수가표**(RU_1 830원 ~ RU_4 6,230원)와 **「수급자별 1일 1회」** 안내를 확인합니다.
3. **`TransportForm18GuidePanel`** — 공단 **별지 제18·19·20호** 선행 절차 5단계·**3분리 신청 유형**·**등록상태 4단**을 읽습니다 (Q237).
4. **「확정 배차에서 생성」** — 기간 내 **CONFIRMED** 운행의 정차별 **DRAFT** 기록을 만듭니다.
5. 각 행에서 **거리구간(RU_1~RU_4)** · **왕복/편도**(편도 = 50%)를 조정하고 **「확정」**으로 `CONFIRMED` 상태로 바꿉니다. **다지점** `hq_admin`은 **BranchSwitcher** 작업 지점과 기록 지점이 일치해야 수정됩니다 (Q247).

| 스킵 사유 (UI 표시) | 의미 |
|---------------------|------|
| 동일 일자 기록 존재 | **1일 1회** 규칙 — UNIQUE `(client, serviceDate)` |
| 계약서 미서명 | 보호자·기관 **이중 서명** 필수 (Q231) |

| API | 용도 |
|-----|------|
| `GET /api/v1/transport/service-fee-rates` | BNK-25 거리구간 수가 catalog |
| `GET /api/v1/transport/service-fees?fromDate=&toDate=` | 기간별 청구 기록 |
| `POST /api/v1/transport/service-fees/generate` | 확정 배차 기반 일괄 생성 |
| `PATCH /api/v1/transport/service-fees/{recordId}` | DRAFT 수정·확정 |

> **권한**: **`caregiver`** 는 `/transport/*` 라우트는 열리지만 **API 403** — 화면이 오류로 보일 수 있습니다 (Q239). **`hq_admin`·`branch_admin`·`social_worker`** 만 생성·확정하세요.
>
> **갭**: 공단 포털 **자동 제출 없음** · 거리구간 **자동 산출 미연동**(기본 RU_1).

#### 5-8-2. 이동서비스비 청구 (`/transport/service-fees`, G16, Q239)

**케어포 2-5** 대응 — 확정 배차를 기반으로 **이동서비스비 청구 기록**을 생성·확정합니다 (BE `88d4c59` + FE `9dfef92`, BNK-25).

1. **`TransportContextNav`** → **「이동서비스비 청구」** (또는 `/transport/service-fees` 직접 접속).
2. **조회 기간**(기본: 당월)을 설정하고 **거리구간 수가표**(RU_1 830원 ~ RU_4 6,230원)와 **「수급자별 1일 1회」** 안내를 확인합니다.
3. **`TransportForm18GuidePanel`** — 공단 **별지 제18·19·20호** 선행 절차 5단계·**3분리 신청 유형**·**등록상태 4단**을 읽습니다 (Q237).
4. **「확정 배차에서 생성」** — 기간 내 **CONFIRMED** 운행의 정차별 **DRAFT** 기록을 만듭니다.
5. 각 행에서 **거리구간(RU_1~RU_4)** · **왕복/편도**(편도 = 50%)를 조정하고 **「확정」**으로 `CONFIRMED` 상태로 바꿉니다. **다지점** `hq_admin`은 **BranchSwitcher** 작업 지점과 기록 지점이 일치해야 수정됩니다 (Q247).

| 스킵 사유 (UI 표시) | 의미 |
|---------------------|------|
| 동일 일자 기록 존재 | **1일 1회** 규칙 — UNIQUE `(client, serviceDate)` |
| 계약서 미서명 | 보호자·기관 **이중 서명** 필수 (Q231) |

| API | 용도 |
|-----|------|
| `GET /api/v1/transport/service-fee-rates` | BNK-25 거리구간 수가 catalog |
| `GET /api/v1/transport/service-fees?fromDate=&toDate=` | 기간별 청구 기록 |
| `POST /api/v1/transport/service-fees/generate` | 확정 배차 기반 일괄 생성 |
| `PATCH /api/v1/transport/service-fees/{recordId}` | DRAFT 수정·확정 |

> **권한**: **`caregiver`** 는 `/transport/*` 라우트는 열리지만 **API 403** — 화면이 오류로 보일 수 있습니다 (Q239). **`hq_admin`·`branch_admin`·`social_worker`** 만 생성·확정하세요.
>
> **갭**: 공단 포털 **자동 제출 없음** · 거리구간 **자동 산출 미연동**(기본 RU_1).

#### 5-8-3. 외출 관리·리포트 (G15 2-1-1·2-9, Q240)

이용자 **외출 예정·출발·복귀**를 기록하고, 월간 **외출 리포트**를 출력합니다 (BE `7dfcc9e` + FE `a0dcfc0`).

**일상 (2-1-1)**

1. SideNav **이동 → 외출 관리**(`/transport/outings`) 또는 이용자 상세 **「외출」** 탭.
2. **이용자 선택** → **외출 예정 등록** — 일자·예정 출발/복귀 시각·사유·동행인(선택).
3. 실제 **출발** 시 **「출발」** → **복귀** 시 **「복귀」** 버튼을 누릅니다.
4. **「취소」** — `PLANNED` 또는 `OUT` 상태에서만 가능. **`PLANNED` 상태에서만** 예정 수정 가능.

| 상태 | 의미 |
|------|------|
| `PLANNED` | 예정 등록 |
| `OUT` | 출발 기록됨 |
| `RETURNED` | 복귀 완료 |
| `CANCELLED` | 취소 |

**월간 (2-9)**

1. SideNav **이동 → 외출 리포트**(`/reports/client-outings`).
2. **대상 월** `MonthInput` 선택 → **조회** (`aria-busy` 로딩 표시, Q240).
3. **StatCard** 요약(**「월간 외출 리포트 요약」** `role="group"`) — 외출 건수·이용자 수.
4. **외출 목록 표** — 이용자명·일시·사유·상태 확인.
5. **「인쇄」** — 브라우저 인쇄(`window.print()`). `CANCELLED` 행은 **제외**됩니다.

> **live E2E 검증 (`3a0110f`, Q240)**: staging에서 **`clientOutingReportLiveApi.e2e.test.js`** 가 **`GET /reports/client-outings?branchId=&yearMonth=`** 응답의 `branchId`·`yearMonth`·`totalOutings`·`items[]` contract를 검증합니다. 데이터가 없으면 **빈 목록**(`totalOutings=0`)도 정상입니다.

| API | 용도 |
|-----|------|
| `GET/POST/PATCH /clients/{id}/outings` | 외출 CRUD·lifecycle |
| `POST …/outings/{id}/depart` · `return` · `cancel` | 상태 전이 |
| `GET /reports/client-outings?branchId=&yearMonth=` | 월간 리포트 (`caregiver` **403**) |

#### 5-8-4. 차량 마스터 (`/transport/vehicles`, G16, Q241·Q402)

**케어포 2-4** 대응 — 지점별 **차량번호·정원·기본 운전자명**을 등록하고 배차·급여제공 기록에 연결합니다 (BE `114411f` + FE `d3bef42`).

1. **`TransportContextNav`** → **「차량 관리」** (또는 SideNav **이동 → 차량 관리**).
2. **`BranchScopeNotice`** 로 조회 지점을 확인합니다.
3. **`hq_admin`·`branch_admin`** — **차량 등록** Modal: **차량번호** · **정원**(1–15) · **별칭**(선택) · **기본 운전자명**(한글 성명, Q402) · **활성** 토글.
4. 목록에서 **수정** — 동일 필드 편집. 스크린리더는 **`{차량번호} 차량 수정`** 으로 읽습니다 (UXD-76, Q253). **비활성** 차량은 배차 선택 목록(`activeOnly`)에서 제외됩니다.
5. 등록한 차량은 **수동 배차**·**루트 상세** **`TransportVehicleSelect`** 에 **기본 운전자명**과 함께 표시됩니다 (Q402).
6. 확정 배차 + `vehicleId` → 이용자 **「급여제공」** 탭 일별 **차량번호** · 이메일 발송 payload (Q243).

| API | 용도 |
|-----|------|
| `GET /api/v1/transport/vehicles?activeOnly=true` | 활성 차량 목록 (배차 선택) — **`defaultDriverName`** 포함 |
| `POST /api/v1/transport/vehicles` | 신규 등록 — `defaultDriverName` |
| `PATCH /api/v1/transport/vehicles/{vehicleId}` | 수정·비활성 |

> **중복 차량번호** — Tenant 내 UK 위반 시 **422**. **정차 수 > capacity** — 배차 화면 경고(저장은 API에서 추가 검증 가능).

### 5-9. 식사·프로그램 관리 (`/meals`, `/programs`, v3)

요양보호사·사회복지사가 **일일 식사 섭취량**·**프로그램 참여**를 기록하고, **`hq_admin`·`branch_admin`** 이 식단·일정을 등록하는 화면입니다 (BE `dfd9be2` + FE `1794e1c`, REQUIREMENTS §3-5·§3-6 **Should**). **조회·기록·등록 API FE·BE 연동 완료**(FAQ **Q160**·**Q161 Fixed**).

> **M6 위생·시설관리 (v3.1 P1, Q660)** — **6-1 식사 `/meals`만 LIVE**입니다. **6-2~6-4 안전·위생 점검**(`/safety/*`) Route는 **후속 Planned** — REQUIREMENTS 190차 재확인 · 신규 core 갭 0.

#### 식사 관리 (`/meals`)

1. SideNav **기록 → 식사 관리**로 이동합니다.
2. **기록일**을 선택하면 당일 **아침·점심·간식** 식단이 표시됩니다 (`GET /api/v1/meals/menus?date=`).
3. **`hq_admin`·`branch_admin`** — 식단이 비어 있으면 **`MealMenuForm`** 에서 식사 구분·메뉴명·칼로리(선택)를 입력하고 **등록**합니다 (`POST /api/v1/meals/menus`).
4. `GET /api/v1/meals/records?date=` 로 이용자별 기존 섭취 기록을 확인합니다.
5. **`MealRecordForm`** 에서 이용자·식사 구분·섭취량(`WELL`/`NORMAL`/`LESS`)·식이 제한·영양사 소견을 입력하고 **저장**합니다 (`POST /api/v1/meals/records`).

| API | 용도 |
|-----|------|
| `GET /api/v1/meals/menus?date=YYYY-MM-DD` | 당일 식단 조회 |
| `POST /api/v1/meals/menus` | 식단 등록 (`hq_admin`·`branch_admin`) |
| `GET /api/v1/meals/records?date=YYYY-MM-DD` | 섭취 기록 목록 |
| `POST /api/v1/meals/records` | 섭취 기록 생성·갱신 |

#### 프로그램 관리 (`/programs`)

1. SideNav **기록 → 프로그램 관리**로 이동합니다.
2. **기록일**을 선택하면 당일 프로그램 일정이 표시됩니다 (`GET /api/v1/programs/schedule?date=`).
3. **`hq_admin`·`branch_admin`** — 일정이 비어 있으면 **`ProgramScheduleForm`** 에서 프로그램명·시간 등을 입력하고 **등록**합니다 (`POST /api/v1/programs/schedule`).
4. `GET /api/v1/programs/participations?date=` 로 참여 기록을 확인합니다. 목록 표에 **「미제공 사유 (G17b)」** 열이 표시됩니다 — **인지활동형(`COGNITIVE`)** 프로그램 **불참** 건만 사유 라벨이 채워집니다 (FE `487416d`, Q334).
5. **`ProgramParticipationForm`** 에서 이용자·프로그램·참여/불참·만족도를 입력하고 **저장**합니다 (`POST /api/v1/programs/participations`).
   - **참여(`ATTENDED`)** — 만족도(1~5) **필수** · **미제공 사유 입력 불가** (BE `3bd6a43`)
   - **불참(`ABSENT`)** — 만족도 **미입력** · **일반 프로그램**은 사유 없음
   - **인지활동형 프로그램 + 불참 (G17b, Q333)** — **「인지활동형 미제공 사유 (G17b)」** 선택 **필수** — 미선택 시 필드 오류 「인지활동형 프로그램 미제공 사유를 선택하세요.」

| 미제공 사유 코드 | 화면 라벨 |
|----------------|----------|
| `STAFF_SHORTAGE` | 인력 부족 |
| `EQUIPMENT_FAILURE` | 시설·장비 장애 |
| `CLIENT_REFUSAL` | 수급자 거부 |
| `OTHER` | 기타 |

> **법적 근거**: MOHW 2025-247 **제32조** — 주야간보호 **인지활동형 프로그램 미제공** 시 급여제공기록지 **사유 기재** (FAQ Q333).

| API | 용도 |
|-----|------|
| `GET /api/v1/programs/schedule?date=YYYY-MM-DD` | 당일 프로그램 일정 |
| `POST /api/v1/programs/schedule` | 일정 등록 (`hq_admin`·`branch_admin`) — `programType`에 **`COGNITIVE`** 지정 가능 |
| `GET /api/v1/programs/participations?date=YYYY-MM-DD` | 참여 기록 목록 — **`skipReason`** 포함 |
| `POST /api/v1/programs/participations` | 참여·만족도·**`skipReason`** 등록·갱신 |

> **식단·일정이 비어 있을 때**: **`caregiver`·`social_worker`** 는 등록 폼이 없습니다 — **`hq_admin`·`branch_admin`** 에게 등록을 요청하세요 (Q161).
>
> **MVP 범위**: v3 **Should** — Must 파일럿 검증 대상 **외**. 퇴소 이용자에게는 기록 저장이 거부됩니다(V49 가드).

#### 기능회복훈련 (`/programs/functional-recovery`, G17, US-T06)

MOHW **평가 지표 25–27**(기능회복 프로그램·연간 실시·개인별 계획·제공·기록·급여시작 전 수립) 대응 화면입니다 (BE `0048105`·`e820b28` + FE `21b1855`·`7450161`, FAQ **Q262·Q271 Fixed**).

1. SideNav **기록 → 기능회복훈련 (G17)** 또는 **`RecordsContextNav`** **「기능회복훈련」** 으로 이동합니다.
2. 상단 **지표 준수 현황** StatCard에서 **지표25**(급여계획 포함)·**지표26**(연 1회 실시)·**지표27**(개인별 계획) · **지표27 — 기능회복훈련 제공·기록** · **지표27 — 급여제공 시작일까지 기능회복훈련 계획 수립**(silverangel verbatim, BNK-102) 을 확인합니다.
3. StatCard 아래 **`LifecycleWorkflowPanel`** — **기능회복훈련 준수 lifecycle** 단계(지표25~27)를 **완료/지연** Badge와 함께 확인합니다 — 증빙 목록·단계별 설명 제공 (**UI Fixed**, `22bd6b7`, Q287). **선임 업무수행일지(G34) 입력 화면이 아닙니다** (Q284).
4. 미충족 시 warning **`Alert`** — 「프로그램 참여·기록 없음」·「급여제공 시작일까지 기능회복훈련 계획이 수립되지 않은 이용자가 있습니다」 안내 (Q271).
5. **조회 연도**를 바꾸면 해당 연도 **계획 목록**이 갱신됩니다.
6. **`hq_admin`·`branch_admin`·`social_worker`** — 하단 **기능회복훈련 계획 등록** 폼에서 이용자·연도·계획 내용·**급여계획 포함** 여부·**인지활동형 프로그램 제공 여부(G17b)**·실시일을 입력하고 **저장**합니다 (`POST /api/v1/programs/functional-recovery/plans`). **급여시작일이 지난 이용자**는 **신규 등록** 폼이 **비활성**됩니다 (FE 사전 차단, BNK-102).
   - **인지활동형 프로그램 제공 (G17b, Q335)** — Switch **「제공」/「미제공」** (기본 **제공**)
   - **미제공** 선택 시 — **「인지활동형 미제공 사유 (G17b)」** Textarea **필수** — placeholder 「장기요양법 제32조 — 인지활동형 프로그램 미제공 사유를 기재하세요」 · 공백만 입력 시 저장 거부
   - **제공**으로 되돌리면 사유 필드가 **자동 비워집니다**
7. 계획 목록 표에 **「인지활동형 (G17b)」** 열 — **제공** / **미제공** Badge로 표시됩니다 (FE `c26cfa7`).
8. 목록에서 **수정**을 누르면 동일 폼으로 기존 계획이 로드되고 **`PATCH …/{planId}`** 가 호출됩니다 — **이용자·연도 필드는 잠금** · **급여시작 create guard는 수정 시 생략** · 요청 본문에 **`clientId` 미포함** (`26499b3`·`2cd2cd8`, Q279·Q283).
9. **`caregiver`** — 조회만 가능합니다. 등록·수정이 필요하면 사회복지사·센터장에게 요청하세요.

> **급여시작일 가드 (Q271)**: 이용자 **급여인정 유효 시작일(`ltcCertValidFrom`) 당일 이후**에는 **신규 계획 등록이 거부**됩니다 — 「급여제공 시작일 이전에 기능회복훈련 계획을 수립해야 합니다.」(BE `422` · FE `isFunctionalRecoveryPlanCreateBlocked`). **기존 계획 수정**은 허용됩니다 (Q279).

| API | 용도 |
|-----|------|
| `GET /api/v1/programs/functional-recovery/plans?year=` | 연간 계획 목록 |
| `POST /api/v1/programs/functional-recovery/plans` | 계획 등록 |
| `PATCH /api/v1/programs/functional-recovery/plans/{planId}` | 계획 수정 (**UI Fixed**, Q279) |
| `GET /api/v1/programs/functional-recovery/compliance?year=` | 지표 25–27 + **`provisionRecordedMet`** · **`planEstablishedBeforeBenefitStartMet`** 충족 요약 (Q271) |

> **중복 등록**: 동일 이용자·연도에 계획이 이미 있으면 서버가 **422** 로 거부합니다.

#### 사례관리 회의록 (`/case-management/meetings`, G32, US-T07)

MOHW **평가 지표 43**(분기별 사례관리 회의·참석자 2인 이상·회의록 보관) 대응 화면입니다 (BE `2225a7a` + FE `0821ce8`, FAQ **Q263**).

1. SideNav **기록 → 사례관리 회의록 (G32)** 또는 **`RecordsContextNav`** **「사례관리 회의록」** 으로 이동합니다 (`caregiver` 메뉴 **미표시**).
2. 상단 **지표43·지표29·참석자별 의견 준수 현황** — 분기 충족·참석자 2인 이상·**참석자별 의견 기록**·30일 급여반영·**지표29 평가 실시** StatCard를 확인합니다 (UXD-79, Q266·Q516). **대시보드**(`/dashboard`·`/dashboard/hq`)의 **「참석자별 의견 미기록」** 위젯(Q518)으로 분기 전체 미충족 인원을 먼저 점할 수 있습니다.
3. StatCard 아래 **`LifecycleWorkflowPanel`** — **사례관리 준수 lifecycle** 단계(분기 회의·참석자·30일 반영·평가 실시)를 확인합니다 (**UI Fixed**, `22bd6b7`, Q287).
4. **연도·분기** 필터로 회의록 목록을 조회합니다.
5. **`hq_admin`·`branch_admin`·`social_worker`** — **사례관리 회의록 등록** 폼에서 다음을 입력합니다 (FE `443f379`·`b272a7b`, Q265·Q516 Fixed).
   - 이용자 · **회의 일자** · **선정 사유** · **회의 내용** · **회의 결과** · **사례관리 계획** · **참석자**(**쉼표·세미콜론·슬래시** 구분, **최소 2인**)
   - **참석자 2인 이상**이면 **`fieldset`「참석자별 의견 (FAQ21797)」** 이 표시됩니다 — 각 참석자의 **이름·직종(선택)·의견**을 입력합니다. 의견 미입력 시 저장이 차단됩니다.
   - **참석자 이름 중복**(대소문자 무시, 예: 「김사복, 김사복」)은 FE에서 즉시 오류가 표시되고, 서버도 **422**로 거부합니다 (Q520, `c7fb69a`·`eed39ab`).
6. **저장** 시 `POST /api/v1/case-management/meetings` 가 호출됩니다 — body에 **`attendeeOpinions[]`** 가 포함됩니다 (`5222a8f`·`b272a7b`, Q516). FE·BE 모두 참석자 구분자를 정규화합니다 (`7eebd8c`·`2225a7a`, QA-B40). **참석자·의견 작성자 중복**·**의견 수 불일치** 시 **422** (Q520). 동일 이용자·분기에 이미 회의록이 있으면 **422**(`해당 분기 사례관리 회의 기록이 이미 존재합니다.`)가 반환됩니다.
7. 목록에서 **수정**을 누르면 동일 폼으로 기존 회의록이 로드되고 **`PATCH …/{meetingId}`** 가 호출됩니다 — **이용자 필드는 잠금** · 요청 본문에 **`clientId` 미포함** (`26499b3`·`2cd2cd8`, Q279·Q283). **참석자별 의견**도 수정·저장할 수 있으며, **중복 참석자·의견 작성자** 규칙은 등록과 동일합니다 (Q520·Q522, `510d2f3`).

> **지표29 「평가 실시」 (Q266, BE `11277b9`·FE `fa2ad1e`)**: **「지표29 — 평가 실시」** StatCard와 대시보드 **「사례관리 평가 미실시」**·**「평가실시」** 위젯에서 **`evaluationConductedMet`** 를 확인합니다. 미충족 시 화면에 warning Alert가 표시됩니다.

| API | 용도 |
|-----|------|
| `GET /api/v1/case-management/meetings?year=&quarter=&clientId=` | 회의록 목록 |
| `POST /api/v1/case-management/meetings` | 회의록 등록 |
| `PATCH /api/v1/case-management/meetings/{meetingId}` | 회의록 수정 (**UI Fixed**, Q279) |
| `GET /api/v1/case-management/compliance?year=&quarter=` | 지표43·30일 급여반영 compliance |

> **30일 급여반영**: compliance API는 회의일 기준 **30일 이내** 프로그램 참여 또는 청구 변경이 있는지도 집계합니다. **미반영 이용자 수**는 **`/dashboard`** **「사례관리 30일 미반영」** 위젯과 회의록 화면 StatCard에서 확인합니다 (Q263).

#### 급여제공결과 평가 (`/programs/provision-result-evaluations`, G39, US-T08)

MOHW **평가 지표 44**(주 1회 상태변화·월 1회 급여제공기록지·연 1회 평가·30일 이내 반영) 대응 화면입니다 (BE `f082933` + FE `1c99bcd`·`a16e1fe`, FAQ **Q276 Fixed**).

1. SideNav **기록 → 급여제공결과 평가 (G39)** 또는 **`RecordsContextNav`** **「급여제공결과 평가」** 로 이동합니다 (`caregiver` **조회만**).
2. 상단 **연도** 필터로 대상 연도를 선택합니다.
3. **지표44 준수 현황** StatCard 4종을 확인합니다.
   - **지표44 — 주 1회 상태변화 기록**
   - **지표44 — 월 1회 급여제공기록지 보호자 제공**
   - **지표44 — 연 1회 급여제공결과 평가**
   - **지표44 — 30일 이내 평가 반영**
4. 미충족 시 warning **`Alert`** — 「연 1회 급여제공결과 평가가 등록되지 않은 이용자…」·「평가 결과가 30일 이내…」 안내 (BNK-107).
5. **`hq_admin`·`branch_admin`·`social_worker`** — 하단 **급여제공결과 평가 등록** 폼에서 **이용자**·**평가 일자**·**총평**·**작성자**를 입력하고 **저장**합니다 (`POST /api/v1/provision-result-evaluations`).
6. 목록에서 **수정**을 누르면 동일 폼으로 **`PATCH …/{evaluationId}`** 가 호출됩니다. **이용자·연도당 1건** — 중복 등록 시 **422**(`해당 연도의 급여제공결과 평가가 이미 등록되어 있습니다.`).
7. **`/dashboard`** **지표44 gap·상태 위젯 8종**(주간·월간·연간·30일, `8e66ae8`)에서 지점 전체 준수 현황을 확인할 수 있습니다.
8. **`hq_admin`·`branch_admin`·`social_worker`** — compliance에서 **「월간 기록지 미제공」** 이용자가 있으면 하단 **「지표44 — 월 1회 급여제공기록지 보호자 제공」** 패널이 표시됩니다 (Q358, `4d1a4f2`).
   - **발송 대상 연월**(`MonthInput`, `YYYY-MM`)을 선택합니다.
   - 미제공 이용자 표에서 **「기록지 발송」** 을 누르면 **`POST /api/v1/clients/{clientId}/notifications/care-provision-record`** 로 보호자에게 **월간 급여제공기록지** 알림이 발송됩니다.
   - 발송 성공 시 **success Alert**가 표시되고 compliance 목록이 갱신됩니다.
   - **J03 quiet-hours(22:00~08:00 KST)** 에는 발송이 차단될 수 있습니다 — FAQ Q329.

| API | 용도 |
|-----|------|
| `GET /api/v1/provision-result-evaluations?year=&clientId=` | 연간 평가 목록 |
| `POST /api/v1/provision-result-evaluations` | 평가 등록 |
| `PATCH /api/v1/provision-result-evaluations/{evaluationId}` | 평가 수정 |
| `GET /api/v1/provision-result-evaluations/compliance?year=` | 지표44 4-pillar compliance |
| `POST /api/v1/clients/{clientId}/notifications/care-provision-record` | **월간 급여제공기록지 보호자 발송** (G39 pillar 2, Q358) |

> **30일 반영 집계**: compliance API는 평가일 기준 **30일 이내** 기능회복 계획 갱신·프로그램 참여·건강 기록 존재 여부를 집계합니다. **미반영 건수**는 평가 화면 StatCard·대시보드 위젯에서 확인합니다 (Q276).
>
> **월간 기록지 발송 (Q358)**: 이용자 상세 **「급여제공」** 탭(Q243)에서 **조회**만 가능했던 기록지를, 평가 화면에서 **보호자 발송**까지 한 번에 처리할 수 있습니다. 발송 이력은 **`CARE_PROVISION_RECORD`** 알림 타입으로 집계되어 지표44 pillar 2 compliance에 반영됩니다.

> **G38 급여계획 통보 모니터링 (Q277 Fixed)**: **`/clients/care-plan-notifications`** 화면·대시보드 위젯에서 **5·11개월 milestone**·**재발급 첨부 미반영**을 확인합니다. **인정기간 첨부** 등록은 이용자 상세 **「등급 이력」** 탭(Q274) — §4-3 참고.

#### 선임 요양보호사 업무수행일지 (`/staff/lead-caregiver-log`, G34, US-S01)

케어포 **func.php `8-1-2`** 「선임 요양보호사 업무수행일지」에 대응하는 **일별 업무 기록·전자서명** 화면입니다 (BE `559648f` + FE `6d6b426`, FAQ **Q284 Fixed**).

1. **`RecordsContextNav`** **「선임 업무수행일지」** 또는 URL **`/staff/lead-caregiver-log`** 로 이동합니다.
2. 상단 **팀장급 자격 compliance** 패널(`TeamLeadQualificationCompliancePanel`, Q319)에서 **대상·자격 충족·실무경력 미달·입사일 미등록** StatCard와 직원별 표를 확인합니다. **이름** 클릭 시 **`/staff/{userId}`** HR 화면으로 이동해 **`hiredAt`** 을 등록할 수 있습니다 (`574bd08`·`9a8bd2a`).
3. **등록 일지**·**서명 완료**·**서명 대기** StatCard로 일지 현황을 확인합니다.
4. **`LifecycleWorkflowPanel`** — **G34 lifecycle** 단계(일지 등록 → 선임 요양보호사 지정 → 업무 내용 기록 → 전자서명)를 확인합니다 (Q287).
5. **조회 일자**(`DateInput`)를 바꾸면 해당 일자 일지 목록이 갱신됩니다.
6. **`hq_admin`·`branch_admin`·`social_worker`·`caregiver`** — 하단 **업무수행일지 등록** 폼에서 다음을 입력하고 **저장**합니다.
   - **이용자** · **기록 일자** · **선임 요양보호사**(활성 직원) · **업무 수행 내용**(필수) · **특이사항**(선택)
   - **선임 지정 시** FAQ21837 **팀장급 자격(실무경력 5년)** 미충족·입사일 미등록이면 **저장이 차단**됩니다 — FE 폼 가드 + BE **`422 BUSINESS_RULE`**(API 직접 호출도 거부) — HR **「입사~퇴사」** 탭에서 `hiredAt`을 먼저 등록하세요 (Q319)
   - **(선택) 욕구사정·계획 불러오기 (G34b, Q303, `0ce04ad`)** — 이용자를 선택한 뒤 **「욕구사정·계획 불러오기」** 를 누르면, **기록 일자 회계연도**의 **G24 욕구사정**·**G17 기능회복훈련 계획**을 읽어 **업무 수행 내용·특이사항** 초안을 채웁니다. 이미 입력된 내용이 있으면 **아래에 추가**됩니다. (FE 클라이언트 병합 또는 **`GET /staff/lead-caregiver-logs/import-draft?source=needs_assessment`**, BE `8487667`)
   - **(선택) 전월 일지 복제 (G34b, Q306, `1b5fabe`)** — **「전월 일지 복제」** 를 누르면 선택 이용자의 **전월 최신 일지** 내용을 **append**합니다. **`caregiver`** 는 FAQ21813에 따라 **인지·정서·인지활동** 구간이 **자동 제외**됩니다 — **`social_worker`·센터장**만 해당 항목 포함. (FE 클라이언트 병합 또는 **`GET …/import-draft?source=previous_month`**, BE `8487667`)
7. 동일 이용자·일자에 이미 일지가 있으면 **422**(`해당 이용자의 동일 일자 업무수행일지가 이미 존재합니다.`)가 반환됩니다.
8. 목록에서 **수정**을 누르면 **`PATCH /api/v1/staff/lead-caregiver-logs/{logId}`** 로 **DRAFT** 일지만 수정할 수 있습니다 — **이용자·기록 일자 필드는 잠금**.
9. **전자서명** — 목록 행 **「전자서명」** 을 누르면 **`SignLeadCaregiverWorkLogModal`** 이 열립니다 (`314b380`, Q288).
   - **서명 방식** — `직접 서명`(`DIRECT`) 또는 `문자 인증`(`SMS_VERIFIED`)
   - **「서명 후에는 일지 내용을 수정할 수 없습니다」** 안내 확인
   - **`SMS_VERIFIED`** 선택 시 **「문자 인증 확인」Checkbox** 필수 (live OTP **미연동**)
   - **「서명 확정」** — **`POST …/{logId}/sign`** · 서명 중 **`aria-busy`**
10. 서명 완료(`SIGNED`) 후에는 **수정 불가**합니다.
11. 목록 **서명자**·**서명 시각** 열에서 **`DIRECT`·`SMS_VERIFIED`** 서명 감사 메타데이터를 확인합니다 (`8ccd287`).
12. **`caregiver`** — 등록·수정·서명이 가능합니다. 지점 스코프 내 이용자만 대상입니다.

| API | 용도 |
|-----|------|
| `GET /api/v1/staff/team-lead-qualification/compliance?branchId=&referenceDate=` | **팀장급 자격 compliance** 지점별 집계 (FAQ21837, Q319, `9a8bd2a`) |
| `GET /api/v1/staff/lead-caregiver-logs?date=&clientId=` | 일자·이용자별 일지 목록 |
| `GET /api/v1/staff/lead-caregiver-logs/import-draft?clientId=&logDate=&source=` | **불러오기·전월 복제 초안** — `source=needs_assessment` \| `previous_month` (BE, `8487667`, Q303·Q306) |
| `POST /api/v1/staff/lead-caregiver-logs` | 일지 등록 — **`caregiver`** 인지활동 구간 **서버 거부** (`b6ecc35`, Q306) · **팀장급 자격 미충족 `422`** (`726b3de`, Q319) |
| `PATCH /api/v1/staff/lead-caregiver-logs/{logId}` | DRAFT 일지 수정 — 선임 변경 시 **동일 자격 검증** (Q319) |
| `POST /api/v1/staff/lead-caregiver-logs/{logId}/sign` | 전자서명 확정 |
| `GET /api/v1/clients/{clientId}/needs-assessments?fiscalYear=` | **불러오기(FE)** — G24 욕구사정 (Q303) |
| `GET /api/v1/functional-recovery/plans?year=&clientId=` | **불러오기(FE)** — G17 기능회복훈련 계획 (Q303) |

> **P2 잔여 (Q288·Q303·Q306)**: **`SMS_VERIFIED`** live OTP · **FAQ21813 30일 rolling** · **K-MMSE·인쇄** 미구현.

#### 고충상담 기록 (`/staff/grievance-counselings`, G42, US-T14, FAQ21814)

케어포 **func.php `8-8`** ·이지케어 **지표7** 「고충상담기록지」에 대응합니다 (BE `bcdc411`·`bcb1d9f` + FE `6012044`·`892450a`, FAQ **Q305 Partial+ Fixed**).

1. **`StaffContextNav`** **「고충상담 (8-8 G42)」** 또는 URL **`/staff/grievance-counselings`** 로 이동합니다.
2. **`hq_admin`·`branch_admin`·`social_worker`** — 상단 **고충상담 등록** 폼에서 다음을 입력하고 **저장**합니다.
   - **접수 경로** — 서면·전화·문자·내방·**익명함**
   - **익명함 선택 시 (FE `8a8b930`, Q305 Partial+ Fixed)** — **대상 유형·이용자/직원 선택·대상명 입력란이 숨겨집니다** — 서버 payload는 **`targetType=OTHER`·`targetName=익명`** 으로 자동 저장 · 폼 하단에 **「익명함 접수」** 안내 표시
   - **그 외 접수 경로** — **대상 유형**(`CLIENT`·`CAREGIVER`·`OTHER`) · **대상** 선택 · **대상명**
   - **상담 일시** · **상담 내용**(필수) · **사후관리 메모**(선택)
3. 목록에서 **익명함** 접수는 대상명이 **「익명」** 으로 마스킹되어 표시됩니다 (`4b54da5`, FAQ21814 PII 보호).
4. **`hq_admin`·`branch_admin`** — 상단 **결재 대기** StatCard·표에서 **`SUBMITTED`** 건을 확인하고 **「결재 승인」** 합니다 (Q309).
5. **DRAFT** 기록의 **「결재 요청」** — **`POST …/{id}/submit`** → 상태 **`SUBMITTED`**
6. **`hq_admin`·`branch_admin`** — **「결재 승인」** — **`POST …/{id}/approve`** → **`APPROVED`**
7. **`APPROVED`** 후 **사후관리 대기** 건 — **「사후관리 기록」** → **`GrievanceFollowUpModal`** 에서 내용·재발 확인 입력 (Q316).
8. **`caregiver`** — 등록 권한 없음 · 목록 **조회만** 가능합니다.

| API | 용도 |
|-----|------|
| `GET /api/v1/staff/grievance-counselings?from=&to=&targetType=` | 기간·유형별 목록 |
| `GET /api/v1/staff/grievance-counselings/pending-approval` | **`SUBMITTED`** 결재 대기 목록 (`hq_admin`·`branch_admin`, Q309) |
| `GET /api/v1/staff/grievance-counselings/follow-up/pending` | **사후관리 대기** 목록 (Q316) |
| `GET /api/v1/staff/grievance-counselings/follow-up/compliance` | 사후관리 compliance 집계 |
| `POST /api/v1/staff/grievance-counselings` | 기록 등록 (`DRAFT`) |
| `PATCH /api/v1/staff/grievance-counselings/{id}` | **DRAFT** 수정 |
| `POST …/{id}/submit` | 전자결재 요청 |
| `POST …/{id}/approve` | 결재 (`hq_admin`·`branch_admin`) |
| `POST …/{id}/follow-up` | 사후관리 기록 (`followUpNotes`·`recurrenceConfirmed`) |

> **P2 잔여 (Q305)**: FAQ21814 **서류함 PDF** · **결재함 전용 별도 라우트** · **익명함 별도 라우트**

### 5-10. 본인부담 리포트·간편계산기 (US-M03, UXD-56)

케어포 7-6~7-10에 대응하는 **청구·입금·수납·환불 대장**과 **본인부담금 간편계산기**입니다 (`hq_admin`·`branch_admin`).

| 화면 | 경로 | 설명 |
|------|------|------|
| 청구대장 | `/billing/reports/charges` | 월별 청구 내역 집계 |
| 입금대장 | `/billing/reports/deposits` | 월별 입금(수납) 내역 |
| 수납대장 | `/billing/reports/receipts` | 월별 수납 완료 내역 |
| **현금영수증 발급목록** | `/billing/cash-receipts` | NTS 발급 이력·수급자별 발급정보 (이지케어 2.10, Q530) |
| **환불대장** | `/billing/reports/refunds` | 월별 환불 내역 (`REFUNDED`, Q179) |
| 간편계산기 | `/billing/calculator` | 등급·출석일수·본인부담 구분으로 예상 본인부담금 계산 |

#### 청구·입금·수납·환불 대장

1. SideNav **청구** 그룹에서 **청구대장**·**입금대장**·**수납대장**·**현금영수증 발급목록**·**환불대장** 중 하나를 선택합니다. 각 대장·**간편계산기**·**현금영수증 발급목록** 화면 상단 **`BillingReportsContextNav`** 로 **7개 화면을 서브 탭** 전환할 수 있습니다 (UXD-81, Q273·Q530).
2. **`MonthInput`**으로 **대상 월**을 선택하고 **조회**합니다.
3. (선택) **이용자 검색**(`q`) — 이름·인정번호로 필터합니다.
4. **입금대장**(`/billing/reports/deposits`) — **「입금 구간」** segmented control으로 **월간**(기본) · **1~15일** · **16~말일** 을 선택합니다 (Q585, FE `e38ccfd`). 케어포 PDF p.91 ② 반월 split에 대응합니다.
5. **수납대장**(`/billing/reports/receipts`) — **「집계 기준」** segmented control으로 **수납기준**(기본) · **청구기준** 을 선택합니다 (Q585). **수납기준**은 `paidAt` 월·**청구기준**은 청구월(`yearMonth`) 기준입니다.
6. 조회 후 **「적용 조건:」** 행에서 서버가 적용한 **대상 월**·**입금 구간/집계 기준** 라벨을 확인합니다 — API **`appliedFilters`** echo를 화면·인쇄 헤더에 반영합니다 (Q587, FE `c6a412f`/`e2f1246`, Q588).
   - **필터 자동저장·복원 (Q621·Q626, FE `77b1ea8`·BE `fd0a3b3`/`99d03fa`)**: 화면 **진입 시** **`GET /billing/reports/filters`** 로 **마지막 조건**(검색어·입금 구간·집계 기준)이 **자동 복원**됩니다. **「조회」** 클릭 시 **`PUT`** 으로 명시 저장되며, 대장 **GET** 조회 시에도 서버 **auto-save (non-blocking)** 됩니다 — **타 지점 조회 시에도 403 없이** 조회됩니다 (Q623·Q626).
7. 상단 **StatCard** 요약을 확인합니다.
   - **청구대장**: 청구 건수·총 급여·본인부담 합계·공단부담 합계
   - **입금·수납대장**: 내역 건수·입금(수납) 합계
   - **환불대장**: 환불 건수·환불 금액 합계
8. **`BillingLedgerTable`**에 이용자·청구월·금액·상태·수납일·결제수단·**환불일·환불 사유**(환불대장) 등이 표시됩니다.
   - **청구대장** — **적용 시작월** 조회 시 **「청구시작 기준금액 (G33)」** opening balance 행이 **맨 위**에 표시됩니다 (Q269). 메모는 **인정번호** 열에 표시될 수 있습니다.
9. **인쇄** 버튼으로 대장만 인쇄합니다 (`ds-billing-report-print-zone`). 인쇄 헤더에 **「적용 조건:」** 과 동일한 월·구간/기준 라벨이 포함됩니다 (Q587).
10. 건수가 많으면 하단 **페이지네이션**으로 이동합니다.

> **API (BE `de49b21`·`b96d038`·`375fb9d`·`14935a3`·`7b99313`·FE `e38ccfd`·`c6a412f`·`e2f1246`, Q179·Q261·Q585·Q586·Q587 Fixed)**: `GET /api/v1/billing/reports/{charges|deposits|receipts|refunds}?month=YYYY-MM&branchId=&q=&page=&size=` — **`hq_admin`·`branch_admin`** 전용. 응답 **`appliedFilters`** — `variant`·`month`·variant별 `depositPeriod`/`receiptBasis`·한글 라벨 (`14935a3`).
>
> **입금·수납 대장 추가 필터 (BE `b96d038`·`14935a3`·FE `e38ccfd`·`c6a412f`, Q585 full-stack · Q587 FE wire)**:
> - **입금대장** — **`period=FULL`**(기본) · **`FIRST_HALF`**(1~15일) · **`SECOND_HALF`**(16~말일) — 입금일(`paidAt`) 기준 반월 split · **`billingReportFilters.js`** **`buildBillingReportQueryParams`**
> - **수납대장** — **`basis=PAYMENT`**(기본, 수납기준) · **`CLAIM`**(청구기준)
> - **variant 불일치** — **`charges`/`refunds`** 에 `period`·`basis` 지정 → **`422`** (Q585)
> - **잘못된 enum** — `period=MID_MONTH` · `basis=invoice` → **`422`** (Q585)
> - **잘못된 월** — `month=2026-99` 등 → **`422`「대상 월 형식이 올바르지 않습니다.」** (Q586, `375fb9d`)
> - **필터 저장 API (Q621, BE `479995e`/`fd0a3b3`·FE `77b1ea8`)**: **`GET/PUT /api/v1/billing/reports/filters?month=YYYY-MM`** — **V170** `billing_report_filters` · **hydrate on mount** · 대장 조회 시 **auto-save (read scope)**

#### 5-10-1. 현금영수증 발급목록 (G-CASH-RECEIPT-LOG, Q530·Q532·Q533·Q536·Q537·Q538 — BE `4432558`/`fe54af8`/`ab5708b`/`58ff35e`/`298bcdf`/`35d1560`/`4da0ca8`·FE `cfc4b04`/`a17f148`/`221458e`/`17374f1`/`a2ef127`/`8aebe55`/`99b795a`/`501fedc`)

이지케어 **「2.수급자 > 2.10 현금영수증 발급목록」**·**「현금영수증 발급정보 관리」**에 대응합니다. **수납대장**은 내부 수납 ledger이고, 이 화면은 **국세청(NTS) 발급 이력**을 별도로 관리합니다 (`hq_admin`·`branch_admin`).

| 화면 | 경로 | 설명 |
|------|------|------|
| 현금영수증 발급목록 | `/billing/cash-receipts` | 발급 목록 조회·등록·미발급 현금수납 집계 |
| 입금 처리 (연동) | `/billing/payments` | **현금 수납 후** **`CashReceiptRegisterModal`** 자동 표시 (Q531, FE `a17f148`) |
| 지점·통합 대시보드 | `/dashboard` · `/dashboard/hq` | **「현금영수증 미발급」**·**「발급 지연」** 위젯 (Q532, FE `221458e`) |

**대시보드 due-gate (Q532, FAQ 21716)**

1. 아침 **`/dashboard`**(또는 **`/dashboard/hq`**)에서 **「현금영수증 미발급」**·**「현금영수증 발급 지연」** StatCard를 확인합니다 — **`hq_admin`·`branch_admin`** 전용.
2. 1건 이상이면 StatCard를 클릭해 **`/billing/cash-receipts`** 로 이동합니다.
3. **발급 지연**은 **수납일+7일** SLA(FAQ 21716 「납입 즉시 발급」)를 초과한 미발급 건입니다.

**화면 구성**

- 상단 **`CashReceiptLegalAlerts`** — FAQ **21716**(납입 즉시 발급)·**21717**(작년분 연말정산 안내)
- **`BillingReportsContextNav`** — 대장·통계·간편계산기와 **서브 탭** 연동
- **「발급 목록」** / **「수급자별 발급정보」** 2탭

**발급 목록 탭**

1. **발급 월**·이용자·발급번호·**휴대폰·사업자번호**(하이픈 유무 무관)로 **조회**합니다 (Q537, BE `298bcdf`).
2. **미발급 현금수납 목록** API가 실패하면 상단 **warning Alert** 「미발급 현금수납 목록을 불러오지 못했습니다…」가 표시됩니다 — Alert에 **`id`** 가 부여되며 **「발급 등록」** 버튼이 **`aria-describedby`** 로 연결되어 스크린 리더가 안내를 함께 읽습니다 (Q537·Q538, FE `99b795a`/`501fedc`). 발급 목록은 조회 가능하나 **페이지 새로고침** 또는 재시도를 권장합니다.
3. 상단 StatCard — **발급 건수** · **미발급 현금수납**(warning) 건수를 확인합니다.
4. 표 열 — 이용자·청구월·**국세청 발급번호**·식별자(휴대폰/사업자)·발급일·금액·**즉시발급**(수납일+7일 이내 「충족」/초과 「지연」).
5. **「발급 등록」** — **`CashReceiptRegisterModal`**:
   - **미발급** `PAID`+`CASH` 청구만 선택 가능 — **`GET …/cash-receipt-issuances/pending`** (다지점 **`hq_admin`** 은 **`branchId` 생략** 시 전 지점 집계, Q533) — **작년분** 청구는 선택 목록에 **「· 작년분」** 표시 (Q537)
   - **발급 대상 0건**이면 **warning Alert**가 표시되고 **「발급 저장」** 버튼이 비활성화됩니다 (Q536, FE `a2ef127`)
   - **작년 청구월**(`yearMonth` 연도 < 올해)이면 **연말정산 불가 warning Alert** 표시 — submit 버튼과 **`aria-describedby`** 연결 (FAQ 21717, Q533·Q536, UXD-139)
   - 이용자 **휴대폰**이 있으면 **식별자 자동 제안** (`GET …/cash-receipt-profile`) — 프로필 로드 중 식별자 필드에 **`aria-busy`** 가 표시됩니다 (Q544, UXD-141, FE `965e569`)
   - **국세청 발급번호**·**식별자 유형**(휴대폰/사업자)·**발급일**·**금액**(본인부담금과 일치) 입력 후 저장 — **하이픈·공백은 자동 제거**되며 **숫자만 허용** · **휴대폰 10~11자리·사업자 10자리** 미달·**문자만 입력** 시 **필드 오류**(FE `76a462d`) 또는 **서버 오류** (Q537) · **V159 DB CHECK**로 raw SQL 적재도 차단 (Q543, BE `15061a9`)
6. 발급 목록 **「즉시발급」** 열 — **수납일+7일 이내 「충족」** / 초과 **「지연」** Badge (Q536, **`CASH_RECEIPT_IMMEDIATE_STATUS`**)

**수급자별 발급정보 탭**

1. 이용자명으로 **검색** 후 선택합니다 — 검색 중 **「검색」** 버튼에 **`aria-busy`** 가 표시됩니다 (Q538, FE `501fedc`).
2. **권장 식별자**(등록 휴대폰)와 **최근 발급 이력**(최대 20건)을 확인합니다.

> **주의 (Q531)**: ogada는 **발급 이력 등록**을 지원합니다. **홈택스·NTS 자동 발급**·**수납 Modal 내 동시 발급 체크박스**(이지케어 FAQ21702)는 후속(**G-CASH-RECEIPT-NTS-API**)입니다. **현금 수납 직후 발급 등록 Modal 안내**는 제공됩니다 (FE `a17f148`). 현장에서는 NTS 발급 후 **발급번호를 등록**하세요.

> **API**: `GET /api/v1/billing/cash-receipt-issuances?month=&q=&page=&size=` — **`q` 휴대폰·사업자번호 digit 검색** (Q537) · `GET /api/v1/billing/cash-receipt-issuances/pending?branchId=` — **`branchId` 생략 시 다지점 `hq_admin` 전 지점 집계** · **`items[]` — `branchId`·`priorYearIssuanceEligible`** (Q533) · `POST /api/v1/billing/cash-receipt-issuances` — **PHONE 10~11자리·BIZ 10자리·숫자만 식별자 검증** (Q537) · **V159** `identifier_value` numeric/length CHECK (Q543) · `GET /api/v1/billing/clients/{clientId}/cash-receipt-profile` · **`GET /api/v1/dashboard/branch`**·**`/dashboard/hq`** — **`cashReceiptPendingCount`·`cashReceiptOverdueCount`** — **V158** `cash_receipt_issuances` 테이블.

#### 5-10-2. 지점별 연말정산·본인부담 통계 (G26 / L07_M09, Q379·Q380·Q381·Q382·Q534·Q538 — FE `09e4ec1`/`19ed7f3`/`501fedc`·BE `903f462`/`6d10e0d`/`3672bbe`/`ceeaeb9`)

케어포 **7-2-1 연말정산 의료비공제 통계**·**PDF p.92 7-8 ② 본인부담금 월별 통계**·**func module 2 이동서비스비 월별 통계**에 대응하는 **지점 집계 화면**입니다 (FE `09e4ec1`/`d8f1fdf`·BE `903f462`/`6d10e0d`/`3672bbe`·pilot E2E `30f03e8`).

**화면 진입**

1. SideNav **청구 → 본인부담 통계**(`/billing/reports/statistics`)로 이동합니다.
2. 또는 **청구대장·입금대장·수납대장·환불대장** 화면 상단 **`BillingReportsContextNav`** 에서 **「본인부담 통계」** 탭을 선택합니다.
3. **`hq_admin`·`branch_admin`** 만 접근 가능합니다.

**조회 절차**

1. **조회 연도**를 입력합니다 (2000~올해). 잘못된 연도는 **필드 아래 오류**로 표시되며 API를 호출하지 않습니다 (Q381, FE `31544cf`).
2. (선택) **이용자 검색** — 이름·인정번호로 ① 의료비공제 통계 목록을 필터합니다.
3. **「조회」** 를 누르면 **① 국세청 의료비공제 통계**·**② 본인부담금 월별 통계**·**③ 이동서비스비 월별 통계**가 **동시에** 로드됩니다 (Q382).
4. ① 섹션에서 **집계 기준** — **「수납년도」**(`PAID_YEAR`, 기본) 또는 **「청구년도」**(`CLAIM_YEAR`, 케어포 7-8) — 을 선택합니다 (Q534, FE `19ed7f3`·BE `ceeaeb9`). **Windows 고대비(forced-colors)** 모드에서도 segmented control 테두리가 보이도록 스타일이 보강되었습니다 (Q538, UXD-140, FE `501fedc`). 선택 변경 시 ① 목록이 **자동 재조회**됩니다.
5. ① 섹션 **「국세청 CSV」** 로 현재 집계 기준·조회 연도·(선택) 검색어에 맞는 **지점 batch CSV**를 다운로드합니다 — 국세청 홈택스 **의료비 공제 batch 업로드**용 (Q534). **국세청 자동 제출**은 미지원입니다.
6. **「인쇄」** 로 현재 집계를 인쇄합니다 (`ds-billing-report-print-zone`).

**① 국세청 의료비공제 통계**

| 표시 | 설명 |
|------|------|
| 요약 StatCard | **대상 이용자** · **납입 합계** · **납입 건수** |
| 이용자 표 | 이용자·인정번호·납입 합계·납입 건수 |
| 집계 규칙 | Q252·Q254와 동일 — **`PAID`+`paidAt` 또는 `yearMonth` 연도** · **`CASH`·`BANK_TRANSFER`만** · **CMS·간편결제 제외** · **`yearBasis=PAID_YEAR|CLAIM_YEAR`** (Q534) |
| batch export | **「국세청 CSV」** — **`GET …/reports/medical-deduction/export?taxYear=&yearBasis=&q=`** (Q534) |
| 페이지네이션 | 이용자가 많으면 하단에서 페이지 이동 |

**② 본인부담금 월별 통계**

| 표시 | 설명 |
|------|------|
| 섹션 안내 | 케어포 PDF p.92 7-8 ② — **모니터링 자가진단(G30 FAQ21836/21842)** 근거 항목과 함께 활용 (`d499130`, Q391) |
| 요약 StatCard | **연간 청구 건수** · **청구 총액** · **입금 총액** · **미수금 총액** |
| 월별 표 | 대상 월·청구건수·전월대비증감·청구총액·증감(원)·입금총액·미수금총액 (케어포 PDF p.92 7-8 ② 6필드) |
| 집계 규칙 | 청구 상태 **`CONFIRMED`·`PAID`·`REFUNDED`** · **`PAID`** → 입금 · **`CONFIRMED`** → 미수 |

**③ 이동서비스비 월별 통계**

| 표시 | 설명 |
|------|------|
| 섹션 안내 | 케어포 func module 2 — **연간 욕구사정(G24b FAQ 21800/21810)** 이동서비스 항목과 연계 확인 (`d499130`, Q391) |
| 요약 StatCard | **연간 건수** · **합계 금액** · **확정 금액** · **임시 금액** |
| 월별 표 | 대상 월·건수·전월대비증감·합계금액·증감(원)·확정금액·임시금액 (케어포 func module 2) |
| 집계 규칙 | **`/transport/service-fees`** 기록 · 서비스일(`serviceDate`) 기준 월별 · **`CONFIRMED`** → 확정 · **`DRAFT`** → 임시 |
| 선행 작업 | **이동 → 이동서비스비 청구**(`/transport/service-fees`)에서 배차 기반 청구 생성·확정 후 집계에 반영 (§5-8) |

> **개별 이용자 상세**는 이용자 상세 **「청구」** 탭 **`MedicalExpenseDeductionPanel`** (Q252)을 사용하세요. **이용자별 NTS xlsx**는 Q258 · **지점 batch CSV**는 본 화면 ① **「국세청 CSV」**(Q534)입니다.

| API (참고) | 용도 |
|------------|------|
| **`GET /api/v1/billing/reports/medical-deduction?taxYear=&yearBasis=&branchId=&q=&page=&size=`** | ① 이용자별 PAID copay 집계 — **`yearBasis`** `PAID_YEAR`(수납년도, 기본) \| `CLAIM_YEAR`(청구년도) |
| **`GET /api/v1/billing/reports/medical-deduction/export?taxYear=&yearBasis=&branchId=&q=`** | ① **국세청 batch CSV** (Q534) |
| **`GET /api/v1/billing/reports/copay-monthly-statistics?year=&branchId=`** | ② 1~12월 청구·입금·미수 집계 |
| **`GET /api/v1/billing/reports/transport-service-fee-statistics?year=&branchId=`** | ③ 1~12월 이동서비스비 확정·임시 집계 |

> **`taxYear`/`year`가 2000 미만·올해 초과**이면 **`422`** — 조회 연도 입력을 확인하세요 (BE `92ae60b`/`30f03e8`).

#### 본인부담금 환불 처리 (US-M03 7-9, Q261)

과오납·중복 수납 등으로 **이미 `PAID` 처리된 청구**를 되돌릴 때 사용합니다.

1. **청구** 목록 또는 **입금 처리**에서 해당 청구 **상세**(`/billing/claims/:claimId`)로 이동합니다.
2. 요약에 **수납일·결제수단**이 표시되는 **`PAID`** 청구인지 확인합니다.
3. **「환불 처리」** 버튼을 누릅니다.
4. **`RefundRecordModal`**에서 **환불일**·**환불 금액**(본인부담금과 **동일**해야 함)·**환불 사유**(선택)를 입력하고 저장합니다.
5. 상태가 **`REFUNDED`** 로 바뀌고 요약에 **환불일·환불 금액·사유**가 표시됩니다.
6. **환불대장**에서 해당 월 내역을 확인합니다.

> **주의**: 부분 환불은 지원하지 않습니다. **연말정산 의료비공제** 집계에서 해당 청구는 **자동 제외**됩니다 (Q252).

#### 간편계산기

1. **청구 → 간편계산기**(`/billing/calculator`)로 이동합니다.
2. **장기요양등급**·**본인부담 구분**(`CopayTypeSelect`)·**출석(이용) 일수**·**적용 연도**를 입력합니다.
3. **`CopayCalculatorPanel`**이 `GET /billing/fee-schedules`·`GET /billing/copay-rates` 데이터로 **예상 본인부담금**을 계산합니다 (클라이언트 `copayCalculator.js`).
4. 결과는 **참고용**이며, 확정 청구는 `/billing`에서 월별 청구서 생성 후 확정하세요.

### 5-11. 방문요양 일정 (`/visits`, Epic V, G21)

방문요양·통합재가 지점에서 **계획·청구 이중 일정**을 달력으로 관리합니다 (FE `371794f` lineage, BE V53, FAQ Q180).

> **지점 제한**: 지점 **급여종**이 **`HOME_VISIT`(방문요양)만** 허용됩니다 (BE `e304fd3`). `DAY_CARE`(주야간)·`INTEGRATED_HOME`(통합재가) 지점에서는 화면·API 모두 「방문요양 일정은 방문요양 지점에서만 등록할 수 있습니다.」 — §5-3 지점 등록 시 급여종을 확인하세요 (FAQ Q180).

#### 화면 구성

| 영역 | 설명 |
|------|------|
| **`VisitCalendar`** | 월간 달력 — 날짜별 방문 건수 **텍스트 배지**·`aria-label` (색상만으로 의미 전달 안 함, US-V01) |
| **`VisitsContextNav` (Q480, FE `3a27303`)** | **계획 일정** · **청구 일정** · **계획·청구 분할 비교** cross-link — URL **`?kind=PLAN|BILLING`** · **`?split=1`** 로 **북마크·공유** 가능 (이지케어 이중 일정 nav parity) |
| **계획/청구 탭** | `PLAN`(계획 일정) \| `BILLING`(청구 일정) — 탭 전환 시 해당 `scheduleKind`만 조회 · **분할 비교 모드**에서는 탭 숨김 |
| **RFID split-view (Q377·Q480, FE `55fdbd0`/`3a27303`)** | **`Switch`「계획·청구 분할 비교 (RFID split-view)」** 또는 **`VisitsContextNav`「계획·청구 분할 비교」** — 켜면 **`?split=1`** · 선택 날짜 **계획·청구 일정 나란히** (`ds-visits-split-compare`) · 청구 열에만 **「청구반영」** 표시 |
| **당일 목록** | 선택 날짜의 이용자·시간·상태·**청구반영**·처리 버튼 |
| **`VisitScheduleForm`** | 이용자·담당 직원·시작/종료 시각·페어 청구 일정 생성 |
| **청구반영 상태 (Q376, FE `25ca88e`·a11y `25291b3`)** | **`GET /visits`** 응답 **`billingClaimReflectionStatus`** — 당일 목록 **「청구반영」** 열 **`StatusBadge`**: **청구반영**(`REFLECTED`) · **미반영**(`NOT_REFLECTED`) · **페어 없음**(`UNPAIRED`). **청구 일정** 탭 또는 **split-view** 청구 열에서 확인. **텍스트 라벨** 병행 — 색상만으로 의미 전달하지 않음 |

#### 일정 등록·확정 (`branch_admin`, `social_worker`)

1. SideNav **기록 → 방문 일정**(`/visits`)으로 이동합니다.
2. 상단 **`BranchScopeNotice`** 로 **조회 지점**을 확인합니다 (Q173).
3. **`NhisScheduleConfirmLockGuide`** — 달력 **표시 월** 기준 **본인부담 청구 확정·수납** 건이 있으면 **warning** 안내 (G21 billing-side lock, Q209). **방문 일정 import 차단**(Q195)과 **별도**입니다.
4. **계획 일정** 또는 **청구 일정** 탭을 선택합니다.
5. 달력에서 **날짜**를 클릭하면 당일 목록이 갱신됩니다.
6. 하단 **방문 일정 등록** 폼에서 이용자·담당 직원·시간을 입력하고 저장합니다 (`POST /api/v1/visits`). **`scheduleKind`** 는 **`PLAN`/`BILLING`** 대문자를 권장하나, API는 **`plan`/`billing` 소문자·공백**도 정규화해 수용합니다 (Q275, `e8de0eb`).
7. `DRAFT` 상태 행에서 **확정**을 눌러 `CONFIRMED`로 전환합니다 (`POST …/confirm`). **페어(PLAN↔BILLING)가 연결되어 있고 페어가 `DRAFT`이면 양쪽 모두 확정**됩니다 (Q259).
8. `DRAFT` 페어 일정을 **수정**하면 연결된 PLAN/BILLING **양쪽 필드**(담당·날짜·시간·제공분)가 **동기화**됩니다 (G21, Q199). **확정 이후**에는 페어 필드 동기화가 적용되지 않습니다.
9. **동일 이용자·일자·종류·시간** 일정을 중복 등록·수정하면 **「동일한 방문일정이 이미 등록되어 있습니다.」** 오류가 표시됩니다 (Q234·Q259).
10. 필요 시 **취소**로 일정을 `CANCELLED` 처리합니다. **페어(계획↔청구) 일정**이 연결되어 있으면 **양쪽 모두 취소**됩니다 (US-V02, Q194). 이미 **완료**된 페어는 건드리지 않습니다.

#### 계획·청구 화면 전환 (VisitsContextNav, G21, Q480, FE `3a27303`)

이지케어 **이중 일정** 화면 전환과 동일하게, **`/visits`** 상단 **`VisitsContextNav`** 로 **계획·청구·분할 비교** 뷰를 바꿉니다.

| 링크 | URL | 설명 |
|------|-----|------|
| **계획 일정** | `/visits?kind=PLAN` | `PLAN` 일정만 달력·목록 조회 |
| **청구 일정** | `/visits?kind=BILLING` | `BILLING` 일정만 조회 · **청구반영** 열 표시 |
| **계획·청구 분할 비교** | `/visits?split=1` | RFID split-view — 아래 § **계획·청구 분할 비교** 와 동일 |

> **북마크**: 링크를 즐겨찾기하면 **월말 점검 루틴**(계획 입력 → 청구 확인 → split-view)을 빠르게 반복할 수 있습니다. **`Switch`** 로 분할 비교를 켜도 URL이 **`?split=1`** 로 동기화됩니다.

#### 계획·청구 분할 비교 (RFID split-view, G21, Q377, FE `55fdbd0`)

이지케어 **change_work** 패턴에 맞춰 **계획·청구 일정을 한 화면에서 나란히** 비교합니다. NHIS 일괄확정(Q330) 전 **페어 불일치**를 빠르게 찾을 때 사용합니다.

1. **`/visits`** 상단 **`VisitsContextNav`「계획·청구 분할 비교」** 를 누르거나, **`Switch`「계획·청구 분할 비교 (RFID split-view)」** 를 켭니다.
2. **계획/청구 탭**이 숨겨지고, 달력 아래 **왼쪽=계획 일정 · 오른쪽=청구 일정** 2열 목록이 표시됩니다.
3. 달력에서 **날짜**를 선택하면 양쪽 목록이 동시에 갱신됩니다.
4. **청구반영 현황** chip 3종 — 선택 날짜 청구 일정 기준 **청구반영·미반영·페어 없음 건수**가 한눈에 표시됩니다 (`4c9103d`, Q387).
5. **미반영**·**페어 없음**이 있으면 **「청구반영 후속 확인」** 목록에 이용자·시간·상태가 나열됩니다 — 바로 페어 수정(Q199) 또는 재import 후 일괄확정하세요 (`cb457b7`, Q387).
6. **청구 일정** 열(오른쪽)에서 **「청구반영」** Badge를 확인합니다.
7. **공단 명세 사전 비교** — split-view ON 시 **계획·청구 NHIS 패널이 각각** 표시됩니다 (Q526, `9b80505`) — § **공단 명세 사전 비교** 참고. 탭 전환 없이 **양 track** 대조 후 일괄확정하세요.
8. 분할 비교를 끄면 기존 **계획/청구 탭** UI로 돌아갑니다.

> **접근성**: split-view 안내 Alert는 **텍스트 라벨**(청구반영·미반영·페어 없음)로 상태를 설명합니다 — 색상(검은/빨간)만으로 의미를 전달하지 않습니다 (`25291b3`, DESIGN_SYSTEM §1-2). NHIS 패널 그룹은 **`role="group" aria-label="계획·청구 공단 명세 분할 비교"`** (Q526·Q527).

#### 청구반영 상태 확인 (G21, Q376, FE `25ca88e`·a11y `25291b3`)

NHIS **청구 일정**과 **계획 일정** 페어가 일치하는지 **일괄확정(Q330) 전**에 확인합니다.

1. **청구 일정** 탭을 선택하거나 **RFID split-view**를 켭니다 — 상단 **안내 Alert**에서 Badge 의미를 확인합니다.
2. 달력에서 **날짜**를 클릭해 당일 목록을 엽니다.
3. **「청구반영」** 열을 확인합니다:
   - **청구반영** — PLAN/BILLING **5필드**(날짜·시작·종료·제공분·담당) 일치
   - **미반영** — 페어는 있으나 슬롯 불일치 — **DRAFT** 상태에서 페어 수정(Q199) 또는 재import
   - **페어 없음** — `pairedScheduleId` 없거나 **페어 엔티티가 누락** — 페어 생성·import 재검토 (`e54a699`, Q388)
4. **미반영**이 남아 있으면 **일괄확정**을 실행하지 마세요 — 공단 청구명세서와 불일치 위험이 있습니다.

> **색상 접근성**: Badge는 **라벨 텍스트**와 함께 표시됩니다 — 색상만으로 의미를 구분하지 않습니다 (DESIGN_SYSTEM §1-2).

#### 공단 명세 사전 비교 (VisitNhisComparisonPanel, G21, Q486·Q526, FE `797c529`/`9b80505`)

이지케어 **schedule-fix `chk-ltm-fix`** 와 동일하게, **일괄확정 전**에 달력 표시 월·선택 탭(`PLAN`/`BILLING`) 기준으로 **ogada 방문일정**과 **최신 NHIS import 명세**를 대조합니다.

1. **`/visits`** 화면에서 달력 **표시 월**·**계획/청구 탭**을 비교 대상과 맞춥니다.
   - **RFID split-view ON** (`?split=1`, Q526) — **「계획 공단 명세 사전 비교」** · **「청구 공단 명세 사전 비교」** 패널이 **위아래로 2개** 표시됩니다. 탭을 바꿀 필요 없이 **양 track**을 점검합니다.
   - **단일 모드** — 활성 탭(`PLAN` 또는 `BILLING`)에 맞는 패널 **1개**만 표시됩니다.
2. **일괄확정** 패널 위 **공단 명세 사전 비교** 섹션(`VisitNhisComparisonPanel`)을 확인합니다. 제목은 **「{계획|청구} 공단 명세 사전 비교」** 로 구분됩니다 (Q527).
3. **StatCard 4종** — **일치·불일치·NHIS 누락·일정 외 NHIS** 건수가 표시됩니다.
4. import 배치가 없으면 info Alert — **공단 청구내역 import** 후 **「비교 새로고침」** 을 누르세요.
5. **전 라인 일치** 시 success Alert · **불일치·누락** 시 warning Alert가 표시됩니다.
6. 불일치가 있으면 **「수급자별 상세 보기」** 를 눌러 **이용자별 일정 일수 vs 공단 일수** 표를 확인합니다 (Q487, `VisitNhisComparisonDetail`). 버튼은 **불일치 Alert**와 **`aria-describedby`** 로 연결되어 있고, 상세 영역은 **`h4`「수급자별 공단 명세 비교 상세」** region heading으로 스크린리더에 안내됩니다 (Q493, UXD-134).
7. 보정 후 **「비교 새로고침」** 으로 재확인한 뒤 § **방문일정 일괄확정** 을 진행합니다.

> **IT 참고**: **`GET /api/v1/visits/nhis-comparison`** — **동일 월** `from`/`to` 필수 (Q479). Modal 사전 점검의 **`nhisComparisonSummary`** embed(Q481)와 **동일 집계**입니다.

#### 방문일정 일괄확정 (G21 batch-confirm, US-V04, FAQ21782, Q330)

이지케어 **「4.일정확정」6단** — 공단 청구명세서 비교·변경이력 확인 후 **월간 DRAFT 일정을 한 번에 확정**합니다 (`VisitBatchConfirmPanel`, FE `d5ff3f8`·BE `0b807d8`).

1. **`/visits`** 화면에서 달력 **표시 월**·**계획/청구 탭**(`scheduleKind`)을 일괄확정 대상과 맞춥니다.
2. **`VisitBatchConfirmPanel`** **「일괄확정 시작」** 을 누릅니다.
   - **활성 지점이 없으면** (다지점 `hq_admin` 등) **「활성 지점이 없습니다. 지점을 선택한 뒤 다시 시도해 주세요.」** 가 즉시 표시되고 Modal이 **「사전 점검 중」** 에 **갇히지 않습니다** (Q508, `5743333`) — **지점 선택기**로 작업 지점을 먼저 고르세요 (§2-4).
3. Modal에서 **사전 점검** 결과를 확인합니다:
   - 상단 **요약 Alert** — **DRAFT 건수**·**이미 확정 건수**·**담당자 미배정**·**페어 불일치** (전체 합계)
   - **계획·청구 유형별 StatCard** (`f9ed97d`, Q477) — **계획(PLAN) DRAFT/확정** · **청구(BILLING) DRAFT/확정** · 각 track **「확정 가능」**(가능/차단) · 페어 불일치·담당 미배정 건수(해당 시만 표시). API **`readyPlan`·`readyBilling`** 과 **동일** — 클라이언트 재계산 없음.
   - **공단 명세 비교** (`68a4e35`/`ad18606`, Q484·Q487) — **`nhisComparisonSummary`** embed — **일치·불일치·NHIS 누락·일정 외 NHIS** StatCard · import 배치 없으면 info Alert · **전 라인 일치** 시 success Alert · **불일치·누락** 시 warning Alert — **불일치 시「수급자별 상세 보기」** 로 이용자별 표 drill-down (`VisitNhisComparisonDetail`) — Modal 집계는 **별도 API 호출 없음**(embed), 상세는 **`GET /visits/nhis-comparison`** on-demand
   - **차단·안내 사유(blockers)** 목록 — **페어 불일치·담당 미배정** 등 **확정 차단** 메시지 외, **공단 import 배치 없음·명세 불일치 건수** 등 **정보성 NHIS 안내**가 포함될 수 있습니다 (`4046046`, Q483) — **`ready=true`와 공존** 가능 · Checkbox 확인 전 **내용을 읽고** 조치하세요.
4. **확정 차단 사유**가 있으면 — **DRAFT 없음** · **페어 PLAN/BILLING 확정 상태 불일치** · **담당자 미배정** — 목록·개별 **확정**으로 먼저 정리한 뒤 재시도합니다. **담당 미배정**은 **`ready`/`readyPlan`/`readyBilling` = false** 및 **`422`** 「담당자가 미배정된 방문일정이 있어 일괄확정할 수 없습니다.」 로 **일괄확정을 차단**합니다 (`5f710e3`, Q477).
5. **공단 명세 대조** — Modal **「공단 명세 비교」** StatCard로 **동일 월 집계**를 확인합니다 (Q484). 불일치 시 **「수급자별 상세 보기」** 로 이용자별 일수를 확인합니다 (Q487). 일괄확정 전 **「공단 명세 사전 비교」** 패널(Q486)에서도 동일 API로 선행 점검할 수 있습니다. **동일 월 범위**만 허용.
6. 아래 **확인 Checkbox 2종**을 **모두** 체크합니다 (UXD-102·UXD-147 **`aria-describedby`** 연결):
   - **「공단 청구명세서와 비교했습니다.」** (`nhisComparisonAcknowledged`) — **`visit-batch-confirm-nhis-comparison`** StatCard region과 **`aria-describedby`** 로 연결 — 스크린리더가 **일치·불일치·누락 집계**를 Checkbox와 함께 안내 (Q506, `0002943`)
   - **「공단조회 변경이력을 확인했습니다.」** (`changeHistoryChecked`)
7. **「일괄확정 실행」** — **`POST /api/v1/visits/batch-confirm`** — 해당 월·종류의 **모든 DRAFT** 가 **`CONFIRMED`** 로 전환됩니다 (페어 확정 규칙은 개별 확정과 동일, Q259). 응답에 **`confirmedPlanCount`·`confirmedBillingCount`** 가 포함됩니다 (Q477, BE `28860ae`).
8. Checkbox 미체크·사전 점검 미충족·**`fromDate`/`toDate` 누락`**·**담당 미배정 DRAFT** 시 **`422 BUSINESS_RULE`** — Modal에 **「일괄확정 기간(시작일/종료일)을 입력해주세요.」** · **「담당자가 미배정된 방문일정이 있어 일괄확정할 수 없습니다.」** 등 오류가 표시됩니다 (`230659a`·`5f710e3`, Q330·Q477).

| API | 용도 |
|-----|------|
| `GET /api/v1/visits/confirm-readiness?from=&to=&scheduleKind=&branchId=` | 일괄확정 **사전 점검** — `ready`·**`readyPlan`·`readyBilling`** · `blockers[]` (확정 차단 + **정보성 NHIS**, Q483) · **PLAN/BILLING split** · **per-kind blockers** (Q474·Q477) · **담당 미배정 시 `ready*` false** (`5f710e3`) · **`nhisComparisonSummary`** — **`yearMonth`·`overallMatch`·`matchedLineCount`·`discrepancyLineCount`·`missingNhisLineCount`·`extraNhisLineCount`·`nhisBatchPresent`** (Q481·Q483, `8a8c5b3`/`4046046`) |
| `GET /api/v1/visits/nhis-comparison?from=&to=&scheduleKind=&branchId=` | **공단 명세 대조** — 이용자별 **`visitDayCount`** vs NHIS import **`nhisServiceDays`** · **`matchedLineCount`·`discrepancyLineCount`·`missingNhisLineCount`·`extraNhisLineCount`** · **동일 월만** (Q479, BE `03a052a`) |
| `POST /api/v1/visits/batch-confirm` | `{ fromDate, toDate, scheduleKind, branchId, nhisComparisonAcknowledged: true, changeHistoryChecked: true }` — 응답 **`confirmedPlanCount`·`confirmedBillingCount`** (Q477) |

> **권한**: **`branch_admin`·`social_worker`** — **`caregiver`** 는 batch-confirm **거부** (Q330). **IT/staging**: G21 live E2E는 **`liveG21Describe`** gate로 **operation + PLAN/BILLING/NHIS seed 준비 시에만** 실행됩니다 (Q495~Q497·Q512).

#### 현장 체크인/아웃 (`social_worker`, `caregiver`)

1. 당일 목록에서 **`CONFIRMED`** 일정의 **체크인**을 누릅니다 (`POST …/check-in`, `method: MOBILE`). Swagger 연동 시 **`mobile`/`manual` 소문자**도 허용됩니다 (Q275).
2. **`assignedUserId`(담당 직원)** 가 배정된 일정에서 **`caregiver`** 가 **다른 직원 배정 일정**을 체크인·체크아웃하려 하면 **「배정된 요양보호사만 체크인·체크아웃할 수 있습니다.」** 오류가 표시됩니다 (Q307, `b459f4c`). **`hq_admin`·`branch_admin`·`social_worker`** 는 감독 역할로 **배정 직원이 활성·해당 지점 소속**이면 체크인·체크아웃 가능합니다.
3. 배정 직원이 **퇴사·비활성**이거나 **해당 지점 소속이 아니면** 체크인·체크아웃 시 **「퇴사 또는 비활성화된 직원은 배정할 수 없습니다.」** 또는 **「해당 지점 직원만 방문일정에 배정할 수 있습니다.」** 오류가 표시됩니다 — **담당 재배정** 또는 **일정 취소 후 재등록**이 필요합니다 (Q453, `0db1e68`).
4. 방문 완료 후 **체크아웃**을 눌러 종료 시각을 기록합니다 (`POST …/check-out`).
5. **페어(계획↔청구)** 일정이 연결되어 있으면, 한쪽 체크인·체크아웃 시 **페어 일정의 상태·시각도 동기화**됩니다 (G21, Q238) — **페어가 `CONFIRMED`→`IN_PROGRESS`→`COMPLETED` 허용 전이에 해당할 때만** (`6bfc745`). **페어 일정이 없거나 상태가 맞지 않으면** 「연결된 계획/청구 일정…」 **`422` 오류**로 **한쪽만 진행되지 않습니다** (`45b8147`).
6. 완료된 일정은 **완료**로 표시되며 추가 버튼이 없습니다.

| API | 용도 |
|-----|------|
| `GET /api/v1/visits?from=&to=&scheduleKind=` | 월간 일정 조회 — **`billingClaimReflectionStatus`** 포함 (Q376) |
| `POST /api/v1/visits` | 일정 등록 (`visitDate`, `clientId`, `staffUserId`, `plannedStartTime`, `plannedEndTime`, `scheduleKind`) |
| `POST /api/v1/visits/{id}/confirm` | 확정 |
| `POST /api/v1/visits/{id}/check-in` | 체크인 |
| `POST /api/v1/visits/{id}/check-out` | 체크아웃 |
| `POST /api/v1/visits/{id}/cancel` | 취소 |
| `POST /api/v1/visits/imports/nhis` | 공단 급여계획·청구일정 xlsx **일괄 import** (**UI Fixed**, Q189) |

#### 공단 방문일정 엑셀 import (US-V04, Q189)

방문요양 지점에서 롱텀·공단에서 받은 **급여계획·청구일정** 스프레드시트를 한 번에 등록할 수 있습니다.

1. SideNav **기록 → 방문 일정**(`/visits`)으로 이동합니다.
2. 지점 급여종이 **`HOME_VISIT`** 인지 확인합니다 (Q180).
3. 달력·목록에 **확정(`CONFIRMED`) 일정**이 1건 이상이면 import 패널이 **비활성**되고 이지케어 FAQ 21473 안내가 표시됩니다 (BNK-26, Q195). 해당 일정을 **취소**한 뒤 재시도하세요.
4. 화면 하단 **「공단 방문일정 엑셀 import」** 패널에서:
   - **일정 종류** — `PLAN`(계획) 또는 `BILLING`(청구)
   - **방문일정 엑셀** — **`.xlsx` 파일만** 선택 (Chrome·Edge에서 공단 파일 다운로드 권장). **`.xls`·CSV·PDF는 거부**됩니다 (Q278, `3c7b247`·`18e2b4c`). **`application/vnd.ms-excel`** MIME도 허용됩니다.
   - **계획** 선택 시 — **「청구 일정도 함께 생성」** 토글으로 페어 BILLING 자동 생성 여부 선택
5. **엑셀 import** 를 누르면 업로드 후 **등록·미매칭·건너뜀** 건수가 표시됩니다.
6. 결과 표에서 행별 **인정번호·방문일·시간·결과 Badge·사유**를 확인합니다.
7. `IMPORTED` 일정은 **`DRAFT`** 상태 — §5-11 절차대로 **확정**·체크인을 진행합니다.
8. `UNMATCHED` — ogada에 **동일 인정번호** 이용자가 없음 → 이용자 등록 후 재import.
9. `SKIPPED` — 제공시간 **1–480분** 범위 밖·퇴소·비활성·**날짜·시간 파싱 실패**(Q200)·**확정 계획일정으로 청구 import 차단**(Q195)·**동일 방문일정 중복**(Q234)·**파일 형식 오류**(`.xlsx` 아님·`Content-Type` 불일치, Q278) 등 — 사유 확인 후 조치. 공단 엑셀의 `20260609`·`년월일`·`오전 930` 형식은 **자동 정규화**됩니다.

> **IT/Swagger**: 동일 API — `POST /api/v1/visits/imports/nhis` multipart — `branchId`·`scheduleKind`·`createPairedBillingSchedule`·`file`.

#### RFID 전송 엑셀 vs 계획 일정 비교 (G21, Q452·Q456·Q482·Q514, BE `eeac205` / FE `27c9de3`/`4a112fe`/`570912e`/`f232285`/`b881883`, **UI Fixed**)

이지케어 **schedule-rfid** 매트릭스(COMP_01~09)에 맞춰 **공단 급여계획 엑셀**과 **RFID 전송 엑셀**을 업로드해 **7종 차이 코드**를 한 번에 집계합니다.

1. SideNav **기록 → 방문 일정**(`/visits`)으로 이동합니다.
2. 화면 하단 **「RFID 계획·태그 비교 (7-code)」** 패널(`VisitRfidDiffComparePanel`)을 찾습니다.
3. 상단 **info Alert** 에서 **RFID 특이사항란 = 별지 서식 동등** 안내를 확인합니다 (Q514, FAQ21817) — 불일치 시 **`/care/weekly-service-records`·`/care/service-special-notes`** 에서 보정하세요.
4. **급여계획 엑셀 (planFile)** — 공단 방문요양 급여계획 xlsx를 선택합니다.
5. **RFID 전송 엑셀 (rfidFile)** — RFID 태그 전송 내역 xlsx를 선택합니다.
6. **엑셀 비교**를 누르면 **계획·RFID 행 수**·**7-code 집계 chip**·**행별 diff 표**(인정번호·방문일·계획·태그·차이 코드)가 표시됩니다.
7. **차이 코드**는 **COMP_01~09** 외 **소문자·공백·`COMP_4`/`comp-4` 변형**·**쉼표 구분 문자열**도 **표준 `COMP_04` 등으로 정규화**해 badge·집계 chip에 표시됩니다 (`570912e`, Q456).
8. **차이가 0건**이면 **초록 success Alert** 「업로드한 급여계획과 RFID 전송 내역 사이에 차이가 없습니다.」가 표시됩니다 (`f232285`, Q482).
9. **RFID split-view**(Q377)로 화면상 페어를 확인한 뒤, 월말 **엑셀 대조**로 공단 제출 전 오류를 일괄 점검합니다.

| 항목 | 내용 |
|------|------|
| API | **`POST /api/v1/visits/imports/rfid/compare`** — multipart — `branchId`·`planFile`·`rfidFile` |
| 권한 | **`branch_admin`·`social_worker`** — **`caregiver`** 거부 |
| 응답 | **`planRowCount`·`tagRowCount`·`comparedRowCount`·`diffCodeCounts`** · 행별 **`diffCodes[]`** |
| 차이 코드 | **COMP_01** 태그 없음 · **COMP_03** 종료 태그 없음 · **COMP_04~06** 시작·종료·인정시간 불일치 · **COMP_07** 담당 불일치 · **COMP_08** 직접입력 · **COMP_09** 계획 없음 |

> **IT/Swagger**: 동일 API — **`/swagger-ui.html`** → Visits → **compare RFID transmission**.

> **페어 일정**: 계획·청구 일정이 연결되면 목록에 **(페어)** 가 표시됩니다. 상세 API는 `pairedScheduleId` 필드를 참고하세요.

### 5-12. 직원 자격 기준 및 모니터링 (`/staff/team-lead-qualification`)

선임 요양보호사(팀장급)는 **법정 자격 기준**을 만족해야 합니다. ogada는 실무경력을 기반으로 **자동 검증**하고 대시보드에 통계를 표시합니다.

#### 자격 기준 (이지케어 FAQ21837, 고시 48~58조)

**팀장급 요양보호사** — 다음 중 **1가지 이상**:
- 실무경력 **5년 이상** (월 60시간 기준 60개월)
- 직원 생일 기준 **`생년월일 + 5년`** 이후 `trained_at` 보유

#### 화면 및 권한

| 기능 | `hq_admin`/`branch_admin` | 설명 |
|------|:------------------------:|------|
| **자격 통계** (`/staff/team-lead-qualification`) | ✅ | StatCard — 전체·적격·부적격·진행 중 직원 수 |
| **적격 팀장 명단** | ✅ | 테이블 — 실무경력·교육이력·리더십 검증 상태 |
| **선임 배정** (`/staff/lead-caregiver-log`) | ✅ | 선임 요양보호사 **업무수행일지 필수 배정**(`selectLeadCaregiver` → 자격 5년 자동 검증) |

#### 모니터링 체크리스트 (`/compliance/monitoring`, G30)

지점별 **월 1회 이상** 자가진단 및 감시 활동을 기록합니다.

| 문항 | 체크 기준 | 용도 |
|------|:--------:|------|
| **직전 6개월 매월 자가진단** | FAQ21842 · 6개월 rolling | 모니터링 readiness |
| **월 1회 관리자 라운딩** | FAQ21812 · `AdminRoundingCheckPanel` | 운영 현황 점검 |
| **업무수행일지** | FAQ21813 · `/staff/lead-caregiver-log` | 선임 요양보호사 기록 |
| **팀장급 자격 충족** | FAQ21837 · 5년 기준 | 리더십 자동 검증 |
| **시정 기한(3개월)** | `complianceIssues` | 개선 추적 |

**활용 팁**: 모니터링 체크리스트의 **integrated checklist panel**에서 **8문항 자동 집계**를 확인하고, 부족한 항목을 지점별로 보완하세요. **공단 평가지표 ↔ ogada 문항 매핑 (G30-LEGEND)** legend(Q629, `fdc135b`)에서 ogada 문항 번호와 공단 평가지표 번호 대응을 먼저 확인하면 평가 준비 시 혼동을 줄일 수 있습니다.

### 5-13. 주기별 업무 가이드 및 준수 (`/compliance/monitoring`, G30 full)

ogada는 **2026년 공단 평가 기준**(장기요양보험법 시행규칙 제정 기준)에 따라 센터의 월/반기/연 주기 업무를 **가이드**하고 **준수 상태**를 통합 모니터링합니다.

#### 주요 정기 업무 (반기·연 기준)

| 업무 | 주기 | 담당 | 화면/API | 통계 |
|------|:----:|------|---------|------|
| **욕구사정** | **연 1회** | `social_worker` | `/clients/:id` · 기본정보 탭 | G24·V48 |
| **기초평가** | **반기 1회** | `social_worker` | `/health/risk-assessment` | G40b·V95/V96 |
| **급여제공계획** | **월 1회** | `social_worker` | `/clients/:id` · 케어플랜 탭 | G32·V75 |
| **급여제공 기록** | **일일** | `caregiver` | `/health` · 기록 입력 | G37·V79 |
| **급여제공 평가** | **연 1회** | `social_worker` | `/care-results/evaluations` | G39·V80 |
| **교육(인권·운영규정)** | **반기/연** | 직원 | `/staff/training-logs` | G41·V104 |

#### 모니터링 패널 활용

**`MonitoringIntegratedChecklistPanel`** (`/compliance/monitoring`)에서:

1. **자가진단** 통계 — 직전 6개월 월별 완료율
2. **업무수행일지** — 선임 요양보호사 월간 작성 현황
3. **팀장급 자격** — 5년 이상 실무경력·교육 이수 검증
4. **라운딩** — 관리자 월 1회 방문 기록
5. **개선 추적** — 3개월 내 시정 여부

**API**: `GET /api/v1/compliance/monitoring/checklist` — 8문항 자동 집계 (FAQ21838/21839/21841/21842).

### 5-14. 직원 교육 및 준수 기록 (`/staff/training-logs`, G41/G41b)

#### 기관 교육일지 개요 (FAQ21807·FAQ21828)

센터는 **법정 의무 교육**을 연·반기 주기로 실시하고 **교육일지를 작성·보관**해야 합니다. ogada는 **5가지 교육 유형**을 등록하고, **`GET /staff/training-logs/compliance`** 로 **지점 단위 준수 현황**을 자동 집계합니다 (BNK-185~188).

#### 5가지 교육 유형

| 유형 | 코드 | 최소 주기 | 신규직원 | 설명 |
|------|:----:|:-------:|:------:|------|
| **노인인권** | `ELDERLY_HUMAN_RIGHTS` | **반기 1회** | ✅ 필수 | 학대·방임·차별 예방 |
| **운영규정** | `OPERATING_REGULATION` | **연 1회** | ✅ 7일 내 | 센터 규칙·직무 안내 |
| **재난대응** | `DISASTER_RESPONSE` | **연 1회** | ✅ | 화재·지진·긴급 대처 |
| **소화기 안전** | `FIRE_SAFETY_EQUIPMENT` | **연 1회** | ✅ | 소화기·비상구·피난 |
| **직원권익** | `STAFF_RIGHTS` | **연 1회** | ✅ | 고충·권리 보호 |

#### 화면 구성 (`/staff/training-logs`)

| 영역 | 설명 |
|------|------|
| **PDF 8-7 필수 Alert** | **재난·소화** 미작성 시 warning Alert — **`id="staff-training-mandatory-alert"`** (Q459·Q462, `caa215f`/`7f94654`) |
| **연간 이수 현황** | StatCard — 총 직원·이수 완료·미이수·기한 초과 · G41b **재난·소화** 미충족 시 **「미작성」** unit (Q459) |
| **기준 연도 필터** | **4자리·2000~2100** — invalid 입력 시 **`Field error`** · API **`referenceYear` 생략** · **compliance 요약 숨김** (Q489, `28e5525`) |
| **교육 유형별 필터** | 드롭다운 — 5가지 유형별로 목록 필터링 |
| **직원별 교육 기록** | 테이블 — 이름·직책·교육 유형·교육일·교육 기관·시간·비고 |
| **등록/수정 모달** | **기준 연도**·유형·교육일·내용·기관 입력 → **선검증 후** 저장 (Q489) |
| **삭제** | 실수 입력 시 행 삭제 (감사 로그 기록) |

#### 사용 절차

1. **`hq_admin` 또는 `branch_admin`** 이 `/staff/training-logs` 이동
2. 상단 StatCard에서 **연간 이수 현황** 확인 — 미이수 직원이 있으면 warning 표시
3. **+ 교육 등록** 버튼 클릭 → 모달 오픈
4. **직원 선택** (요양보호사 · 사회복지사 · 센터장 모두 가능)
5. **교육 유형** — `ELDERLY_HUMAN_RIGHTS` / `OPERATING_REGULATION` / `DISASTER_RESPONSE` / `FIRE_SAFETY_EQUIPMENT` / `STAFF_RIGHTS` 선택 — **노인인권만 `referenceHalf`(반기) 포함** · G41b·운영규정 연간은 **반기 없음** (V107, Q325)
6. **교육 실시일** — 달력 선택 (필수)
7. **교육 기관** · **시간(분)** · **비고** 입력
8. **저장** → 해당 직원의 기록 행에 추가
9. **기한 확인** — 신규입사자는 **입사일 + 7일** 이내 `OPERATING_REGULATION` + **신규직원 교육** 체크 (§5-3, FAQ21828). compliance는 **가장 이른 교육일**·**지점 스코프** 기준 (BNK-187)

#### 법정 기준 (공단 지표)

| 교육 | 이지케어 FAQ | 공단 지표 | ogada 자동 집계 |
|------|:----------:|:-------:|:---------------:|
| 노인인권 | 21807 | — | StatCard 연간 현황 |
| 운영규정 | 21828 | 지표 11 | **신규 7일 + 연 1회** |
| 재난·소화·직원권익 | — | 지표 10(훈련) | **연 1회 이상** |
| 전자서명 | 2974fadd | — | **비고 필드 또는 별도 서명 UI** |

#### API

| 엔드포인트 | 메서드 | 설명 |
|-----------|:------:|------|
| `/api/v1/staff/training-logs` | GET | 전체 교육 기록 (필터: `staffUserId`, `trainingType`, `referenceYear`) |
| — | POST | 교육 기록 신규 등록 |
| `/{id}` | PATCH | 교육 기록 수정 |
| — | DELETE | 교육 기록 삭제 |
| `/compliance` | GET | 지점 compliance — 노인인권 반기·운영규정·**G41b 3종 연간**·신규 7일 (`disasterResponseAnnualMet` 등, BNK-185) |

#### 현장 팁

- **신규입사자**: 입사 처리 후 7일 내 **운영규정 교육** 필수 (§5-3 입사 처리 compliance 참고)
- **G41b 연간 3종**: StatCard는 **BE compliance API 우선** — 목록 건수는 fallback (`38d24b6`)
- **반기 노인인권**: 상반기(1~6월)·하반기(7~12월) — `referenceHalf=1|2` (Q321)
- **외부 교육기관**: 온라인·오프라인 교육 모두 등록 가능 (비고 필드에 URL 기록)
- **감사·지표**: 모든 기록은 `created_by`·`updated_at` 감사 로그 자동 저장

---

### 5-15. 욕창 케어 lifecycle (`/nursing/pressure-ulcer/*`, US-O03, G-NURSING-PRESSURE-ULCER)

silverangel **「욕창위험도 연 1회+」**·**「14일 6대 수칙」**·케어포 demo L03 **간호급여 4 leaf** 패리티 — **위험평가 → 예방계획 → 일별 간호 기록 → 분기 코호트 리포트** 4단 lifecycle (BNK-203~204, v3.1 Must 6번째).

> **G40·G40b와 구분**: 이용자 상세 **「위험도평가」** 탭의 **욕창(`PRESSURE_ULCER`)** 은 **입소 1회(G40)·반기 1회(G40b)** 스크리닝입니다. 본 화면은 **간호급여 욕창 케어 전용 lifecycle** — Braden 척도·예방 6대 수칙·일별 처치·분기 집계 (FAQ Q336).

#### 화면 구성

| 경로 | 탭 | 설명 |
|------|-----|------|
| `/nursing/pressure-ulcer/assessment` | **위험평가** | Braden 점수·위험도 등급·평가일 등록 |
| `/nursing/pressure-ulcer/plan` | **예방계획** | 6대 수칙·장기요양이용계획서 반영 |
| `/nursing/pressure-ulcer/records` | **간호 기록** | 부위·NPUAP 단계·처치·예방 조치 일별 기록 |
| `/nursing/pressure-ulcer/reports` | **분기 리포트** | 분기별 코호트 집계·StatCard·인쇄 |
| `/nursing/pressure-ulcer/reports/provision` | **욕창 제공 리포트 (L03_M15)** | 일별 욕창간호 제공 기록 집계·인쇄 (`efa4472`) |

상단 **`NursingContextNav`** — **12탭** 서브 네비(통합 바이탈·체중·구강·응급·제공기록·제공 리포트·배설·경관·욕창 4단·욕창 제공 리포트) · **`LifecycleWorkflowPanel`** — 4단 진행 상태 · **`aria-label="간호급여 하위 메뉴"`**

#### 권한

| 역할 | 위험평가·예방계획 | 간호 기록 | 분기 리포트 |
|------|:----------------:|:--------:|:----------:|
| `hq_admin`·`branch_admin`·`social_worker` | ✅ 등록·수정 | ✅ 등록·수정 | ✅ 조회 |
| `caregiver` | ✅ 조회만 | ✅ 등록·수정 | ❌ |
| `guardian` | ❌ | ❌ | ❌ |

#### 1단 — 위험평가 (`PressureUlcerAssessmentForm`)

1. SideNav **기록 → 욕창 케어 (US-O03)** 또는 **`/nursing/pressure-ulcer/assessment`** 로 이동합니다.
2. **`PressureUlcerAssessmentForm`** 에서 **이용자**·**평가일**(필수)을 선택합니다.
3. **위험도 등급**(필수) — **`LOW`**(Braden 19~23) · **`MODERATE`**(15~18) · **`HIGH`**(6~14) — Badge 색상으로 표시됩니다.
4. **Braden 점수**(선택) — **6~23** 범위. 범위 밖이면 필드 오류가 표시됩니다.
5. **특이사항**(선택)을 입력하고 **저장** — **`POST /api/v1/nursing/pressure-ulcer/assessments`**
6. 동일 이용자·**동일 평가일** 중복 등록 시 **「해당 일자 욕창위험도 평가가 이미 존재합니다.」** (`422 BUSINESS_RULE`).

> **연 1회 이상** 평가 권장 — silverangel 평가지표. **G40b 반기 욕창 위험도**와 **별도 기록**입니다 (§3-3, Q301·Q302).

#### 2단 — 예방계획 (`PressureUlcerPlanForm`)

1. **`/nursing/pressure-ulcer/plan`** 탭으로 이동합니다.
2. **이용자**를 선택합니다 — **해당 이용자의 위험평가가 선행**되어야 합니다. 없으면 **「선택한 이용자의 위험평가가 없습니다.」** 오류.
3. **6대 수칙** Checkbox — 2시간 체위변경·피부 관찰·습기 관리·영양·압력 분산·교육 (`PRESSURE_ULCER_PREVENTION_RULES`).
4. **예방계획 내용**·**적용 시작일**·**장기요양이용계획서 반영 여부**를 입력하고 **저장** — **`POST /api/v1/nursing/pressure-ulcer/plans`**
5. **high-risk** 이용자는 **평가 후 14일 이내** 6대 수칙 교육·계획 수립을 권장합니다 (silverangel).

#### 3단 — 일별 간호 기록 (`PressureUlcerCareRecordForm`)

1. **`/nursing/pressure-ulcer/records`** 탭으로 이동합니다.
2. **이용자**·**기록일**·**부위**(천골·좌골·발뒤꿈치 등)를 선택합니다.
3. **NPUAP 단계** — 1~4단계·미분류·심부조직·욕창 없음 — **`StatusBadge`** 로 색+텍스트 병행 (색상만으로 의미 전달 안 함).
4. **처치 내용**(필수)·**예방 조치**·**중재 유형**(체위변경·드레싱·세정·영양·의뢰 등)을 입력하고 **저장** — **`POST /api/v1/nursing/pressure-ulcer/records`**
5. **요양보호사(`caregiver`)** 도 **간호 기록 등록** 가능 — 위험평가·예방계획·분기 리포트는 **조회만** 또는 **거부**.

> 동일 이용자·**동일 날짜·동일 부위** 중복 시 **`422`**. **NPUAP 1~4단계**만 DB 정수 저장 — FE enum과 정합 (`d638493` input guard).

#### 4단 — 분기 코호트 리포트 (`PressureUlcerCohortReportPanel`)

1. **`/nursing/pressure-ulcer/reports`** 탭으로 이동합니다 (`hq_admin`·`branch_admin`·`social_worker`만).
2. **연도·분기**(Q1~Q4)를 선택하고 **조회** — **`GET /api/v1/nursing/pressure-ulcer/reports?year=&quarter=`**
3. **StatCard** — 대상·평가 완료·예방계획 수립·기록 보유·미완료 인원.
4. **코호트 표** — 이용자별 위험도·Braden·최근 단계·예방계획 여부.
5. **인쇄** 버튼 — 브라우저 인쇄 대화상자 (`aria-label`에 연도·분기 포함).

#### 5단 — 욕창간호 제공 리포트 (L03_M15, `PressureUlcerProvisionReportPanel`)

케어포 **view.provide_YC_nursing** 대응 — **일별 욕창간호 제공 기록**을 기간·이용자별로 조회합니다 (BNK-217, `75bddee`/`efa4472`).

1. **`/nursing/pressure-ulcer/reports/provision`** 또는 **`NursingContextNav` → 욕창 제공 리포트** 로 이동합니다.
2. **기간(`fromDate`·`toDate`)**·**이용자**(선택)를 지정하고 **조회** — **`GET /api/v1/nursing/pressure-ulcer/reports/provision`**
3. **StatCard** — 총 제공 건수.
4. **제공 기록 표** — 이용자·기록일·부위·NPUAP 단계·처치 내용.
5. **인쇄** — 브라우저 인쇄 (`aria-busy` 로딩 표시, `671a704` a11y).

> 관련: FAQ **Q351** · ADMIN_GUIDE §6-2-9i

#### API 요약

| 엔드포인트 | 메서드 | 용도 |
|-----------|:------:|------|
| `/api/v1/nursing/pressure-ulcer/assessments` | GET | 분기·이용자별 위험평가 목록 |
| — | POST | 위험평가 등록 |
| `/assessments/{id}` | PATCH | 위험평가 수정 |
| `/plans` | GET·POST | 예방계획 조회·upsert |
| `/records` | GET·POST | 간호 기록 목록·등록 |
| `/records/{id}` | PATCH | 간호 기록 수정 |
| `/reports` | GET | 분기 코호트 compliance 집계 |
| `/reports/provision` | GET | 욕창간호 제공 리포트 (L03_M15) — `fromDate`·`toDate`·`clientId` |

> **P2 잔여**: L03 간호급여 **잔여 leaf**(M02·M03·M05·M08·M12) · **G-NURSING live E2E** (`LIVE_E2E=1`) · **PDF 공식 서식**

> 관련: FAQ **Q336~Q339** · ADMIN_GUIDE §6-2-9 · BENCHMARK_REPORT §204 · G40(Q301)·G40b(Q302) §3-3

---

### 5-16. 통합 바이탈 점검 (`/nursing/vital-checks`, L03_M11, G-NURSING)

케어포 **view.total_vital_check** 패리티 — 혈압·맥박·호흡·체온·SpO₂·체중·혈당을 **한 화면에서** 기록합니다 (BNK-207, v3.1 L03 9 leaf 중 1번째 closure).

> **`/health` 건강 기록과 구분**: `/health` 는 일반 건강·투약·사건 기록입니다. 본 화면은 **간호급여 통합 바이탈 전용** — 케어포 L03_M11 서식 대응 (FAQ Q340).

#### 화면 구성

| 영역 | 설명 |
|------|------|
| **`NursingContextNav`** | **통합 바이탈** · **체중** · **구강** · **응급** · **제공기록** · **제공 리포트** · **배설·경관** · 욕창 4단·**욕창 제공 리포트** **12탭** |
| **등록·수정 폼** | **`NursingVitalCheckForm`** — `Field` render-prop으로 label·id·필드 오류 연결 |
| **최근 기록 표** | 기본 **최근 30일** 목록 — 이용자·일시·혈압·맥박·호흡·체온·SpO₂ · **행별 수정 `Button variant=tertiary`** · **`aria-label`「{이용자} {점검일} 통합 바이탈 수정」** (Q509, UXD-137 `f86c76c`) |

#### 등록 절차

1. SideNav **기록 → 통합 바이탈 (L03_M11)** 또는 **`/nursing/vital-checks`** 로 이동합니다.
2. **이용자**·**점검일**·**점검 시각**을 선택합니다 (`DateInput`·`type="time"`). **점검일은 오늘 이후 입력 불가** (Q344).
3. **수축기·이완기 혈압**(mmHg)·**맥박**(회/분)·**호흡수**(회/분)·**체온**(°C)·**SpO₂**(% )를 입력합니다 — **필수**.
4. **체중**(kg)·**혈당**(mg/dL)·**특이사항**은 선택 입력입니다.
5. 정상 범위를 벗어나면 **`vitalsRanges.js`** 기준 **필드 아래 경고**가 표시되나 **저장은 가능**합니다 (건강 기록과 동일, Q155).
6. **저장** — **`POST /api/v1/nursing/vital-checks`**

#### 수정·중복 방지

1. 우측 목록에서 **수정**을 클릭하면 좌측 폼에 기존 값이 채워집니다 — 이용자·점검일·시각은 수정 시 **변경 불가**. 스크린리더·키보드 사용자는 **「{이용자명} {점검일} 통합 바이탈 수정」** 버튼으로 행을 구분합니다 (Q509).
2. **저장** — **`PATCH /api/v1/nursing/vital-checks/{checkId}`**
3. 동일 이용자·**동일 점검일·시각** 중복 등록 시 **「해당 일시 통합 바이탈 기록이 이미 존재합니다.」** (`422 BUSINESS_RULE`).

#### 권한

| 역할 | 조회·등록·수정 |
|------|:-------------:|
| `hq_admin`·`branch_admin`·`social_worker`·`caregiver` | ✅ |
| `guardian` | ❌ |

#### API 요약

| 엔드포인트 | 메서드 | 용도 |
|-----------|:------:|------|
| `/api/v1/nursing/vital-checks` | GET | `fromDate`·`toDate`·`clientId` 필터 목록 |
| — | POST | 통합 바이탈 등록 |
| `/{checkId}` | PATCH | 통합 바이탈 수정 |

> **P2 잔여**: 나머지 L03 leaf(구강·응급·배설관리·병의원·투약 rpt 등) · **`LIVE_E2E=1`** live harness

> 관련: FAQ **Q340~Q344** · ADMIN_GUIDE §6-2-9a · §5-15 욕창 케어 · §5-17 체중 기록 · BENCHMARK_REPORT L03

---

### 5-17. 체중 기록 (`/nursing/weight-records`, L03_M14, G-NURSING)

케어포 **view.nursing_weight_manage** 패리티 — 이용자별 **측정일·체중·신장·BMI·목표 체중**을 관리합니다 (BNK-209, v3.1 L03 9 leaf 중 2번째 closure).

> **통합 바이탈과 구분**: §5-16 통합 바이탈 폼의 **선택 체중** 필드와 **별도 테이블·화면**입니다. 체중 추이·BMI·목표 체중 관리는 본 화면을 사용하세요 (FAQ Q343).

#### 화면 구성

| 영역 | 설명 |
|------|------|
| **`NursingContextNav`** | §5-16과 동일 **12탭** — **체중 기록** 탭이 두 번째 |
| **등록·수정 폼** | **`NursingWeightRecordForm`** — `Field` render-prop으로 label·id·필드 오류 연결 · **체중 `Field help`** — 「유효 범위 20–200 kg」(`8d00f5d`) |
| **최근 기록 표** | 이용자·측정일·체중·**BMI Badge**·**전회 대비 변화량 Badge** · **수정** 버튼 |

#### 등록 절차

1. SideNav **기록 → 체중 기록 (L03_M14)** 또는 **`/nursing/weight-records`** 로 이동합니다.
2. **이용자**·**측정일**을 선택합니다. **측정일은 오늘 이후 입력 불가** (Q344).
3. **체중(kg)** 을 입력합니다 — **필수**, **20~200 kg** 범위.
4. **신장(cm)**·**목표 체중(kg)**·**특이사항**은 선택 입력입니다 (신장 100~220 cm).
5. 범위를 벗어나면 **필드 아래 경고**가 표시되나 **저장은 가능**합니다.
6. **저장** — **`POST /api/v1/nursing/weight-records`**

#### 수정·중복 방지

1. 우측 목록에서 **수정**을 클릭하면 좌측 폼에 기존 값이 채워집니다 — 이용자·측정일은 수정 시 **변경 불가**.
2. **저장** — **`PATCH /api/v1/nursing/weight-records/{recordId}`**
3. 동일 이용자·**동일 측정일** 중복 등록 시 **「해당 측정일 체중 기록이 이미 존재합니다.」** (`422 BUSINESS_RULE`).

#### 권한

| 역할 | 조회·등록·수정 |
|------|:-------------:|
| `hq_admin`·`branch_admin`·`social_worker`·`caregiver` | ✅ |
| `guardian` | ❌ |

#### API 요약

| 엔드포인트 | 메서드 | 용도 |
|-----------|:------:|------|
| `/api/v1/nursing/weight-records` | GET | `fromDate`·`toDate`·`clientId` 필터 목록 |
| — | POST | 체중 기록 등록 |
| `/{recordId}` | PATCH | 체중 기록 수정 |

> **P2 잔여**: 나머지 L03 leaf · **`LIVE_E2E=1`** live harness

> 관련: FAQ **Q343~Q344** · ADMIN_GUIDE §6-2-9b · §5-16 통합 바이탈 · §5-18 구강상태 · BENCHMARK_REPORT L03_M14

---

### 5-18. 구강상태 점검 (`/nursing/oral-care-checks`, L03_M13, G-NURSING)

케어포 **view.oral_care_check** 패리티 — 이용자별 **점검일·양치 도움·구강상태·틀니 착용**을 기록합니다 (BNK-209, v3.1 L03 9 leaf 중 3번째 closure).

> **`/health` 건강 기록과 구분**: 일반 건강·투약 기록과 별도입니다. MOHW 간호급여 **구강상태 점검관리** 전용 화면입니다 (FAQ Q345).

#### 화면 구성

| 영역 | 설명 |
|------|------|
| **`NursingContextNav`** | §5-16과 동일 **12탭** — **구강상태 점검** 탭이 세 번째 |
| **등록·수정 폼** | **`NursingOralCareCheckForm`** — `Field` render-prop으로 label·id·필드 오류 연결 |
| **최근 기록 표** | 이용자·점검일·구강상태 Badge·양치(자립/도움 필요)·틀니(착용/미착용) |

#### 등록 절차

1. SideNav **기록 → 구강상태 점검 (L03_M13)** 또는 **`/nursing/oral-care-checks`** 로 이동합니다.
2. **이용자**·**점검일**을 선택합니다. **점검일은 오늘 이후 입력 불가** (Q344).
3. **양치 도움 필요** Checkbox — 체크 시 「도움 필요」, 미체크 시 「자립」.
4. **구강상태** — **양호(`GOOD`)**·**보통(`FAIR`)**·**불량(`POOR`)** 중 선택 — **필수**.
5. **틀니 착용** — 선택(착용/미착용/미입력).
6. **특이사항**은 선택 입력입니다.
7. **저장** — **`POST /api/v1/nursing/oral-care-checks`**

#### 수정·중복 방지

1. 우측 목록에서 **수정**을 클릭하면 좌측 폼에 기존 값이 채워집니다.
2. **저장** — **`PATCH /api/v1/nursing/oral-care-checks/{checkId}`**
3. 동일 이용자·**동일 점검일** 중복 등록 시 **「해당 일자 구강상태 점검 기록이 이미 존재합니다.」** (`422 BUSINESS_RULE`).

#### 권한

| 역할 | 조회·등록·수정 |
|------|:-------------:|
| `hq_admin`·`branch_admin`·`social_worker`·`caregiver` | ✅ |
| `guardian` | ❌ |

#### API 요약

| 엔드포인트 | 메서드 | 용도 |
|-----------|:------:|------|
| `/api/v1/nursing/oral-care-checks` | GET | `fromDate`·`toDate`·`clientId` 필터 목록 |
| — | POST | 구강상태 점검 등록 |
| `/{checkId}` | PATCH | 구강상태 점검 수정 |

> 관련: FAQ **Q345·Q344** · ADMIN_GUIDE §6-2-9c · §5-16 통합 바이탈 · BENCHMARK_REPORT L03_M13

---

### 5-19. 응급상황 기록 (`/nursing/emergency-records`, L03_M04, G-NURSING)

케어포 **view.emergency_history** 패리티 — 이용자 **응급 발생일·유형·조치·보호자 통보**를 기록합니다 (BNK-211, v3.1 L03 9 leaf 중 4번째 closure).

> **`/health` 낙상·사건 기록과 구분**: 일반 건강 **incident** 기록과 **별도 테이블·화면**입니다. 간호급여 **응급상황 기록** 전용입니다 (FAQ Q346). J03 **긴급(`EMERGENCY`) 알림** 발송과는 별개로, **현장 증빙 기록**을 목적합니다.

#### 화면 구성

| 영역 | 설명 |
|------|------|
| **`NursingContextNav`** | §5-16과 동일 **12탭** — **응급상황 기록** 탭이 네 번째 |
| **등록·수정 폼** | **`NursingEmergencyRecordForm`** — `Field` render-prop · **조치내용** 필수 |
| **최근 기록 표** | 이용자·발생일·응급 유형 Badge·조치내용 요약·보호자 통보 여부 |

#### 등록 절차

1. SideNav **기록 → 응급상황 기록 (L03_M04)** 또는 **`/nursing/emergency-records`** 로 이동합니다.
2. **이용자**·**발생일**을 선택합니다. **발생일은 오늘 이후 입력 불가** (Q344).
3. **응급 유형** — **낙상·기도폐쇄·심장·호흡·경련·출혈·기타** 중 선택 — **필수**.
4. **조치내용** — **필수** (빈 문자열 저장 불가).
5. **상세 내용**·**보호자 통보** Checkbox·**특이사항**은 선택 입력입니다.
6. **저장** — **`POST /api/v1/nursing/emergency-records`**

#### 수정

1. 우측 목록에서 **수정**을 클릭하면 좌측 폼에 기존 값이 채워집니다.
2. **저장** — **`PATCH /api/v1/nursing/emergency-records/{recordId}`**
3. 동일 이용자·**동일 발생일**에 **여러 건** 등록 가능합니다 (통합 바이탈·구강상태와 달리 일자 UNIQUE 없음).

#### 권한

| 역할 | 조회·등록·수정 |
|------|:-------------:|
| `hq_admin`·`branch_admin`·`social_worker`·`caregiver` | ✅ |
| `guardian` | ❌ |

#### API 요약

| 엔드포인트 | 메서드 | 용도 |
|-----------|:------:|------|
| `/api/v1/nursing/emergency-records` | GET | `fromDate`·`toDate`·`clientId` 필터 목록 |
| — | POST | 응급상황 기록 등록 |
| `/{recordId}` | PATCH | 응급상황 기록 수정 |

> 관련: FAQ **Q346·Q344** · ADMIN_GUIDE §6-2-9d · §5-16 통합 바이탈 · BENCHMARK_REPORT L03_M04

### 5-20. 간호급여 제공기록 (L03_M01, `/nursing/service`)

케어포 **view.nursing_service** (3-1 간호급여 제공기록)에 대응합니다. **이용자×제공일** 단위로 **간호·투약·진료(외래)** 제공 여부를 기록합니다 (BNK-215/217, FE `12591d4`).

#### 화면 구성

| 영역 | 설명 |
|------|------|
| **`NursingContextNav`** | **제공기록** 탭 활성 — 12탭 서브 네비 |
| **등록·수정 폼** | **`NursingServiceRecordForm`** — `Field` render-prop · 3-flag Checkbox |
| **최근 제공기록 표** | 기본 **최근 90일** — **`toDate` 기준** 역산 (과거 월 조회 시 종료일만 지정해도 해당 90일, Q352) |

#### 등록 절차

1. SideNav **기록 → 간호급여 제공기록 (L03_M01)** 또는 **`/nursing/service`** 로 이동합니다.
2. **이용자**·**제공일**을 선택합니다. **제공일은 오늘 이후 입력 불가**.
3. **간호 제공**·**투약 제공**·**병의원 진료** 중 **최소 1개**를 선택합니다 — 각 항목별 메모 입력 가능.
4. **진료** 선택 시 **의료기관명**(`medicalInstitution`)을 입력합니다.
5. **저장** — **`POST /api/v1/nursing/service-records`**

#### 수정

1. 우측 목록에서 **수정**을 클릭하면 좌측 폼에 기존 값이 채워집니다.
2. **저장** — **`PATCH /api/v1/nursing/service-records/{recordId}`**

#### 기록 항목

| 필드 | 설명 |
|------|------|
| `serviceDate` | 제공일 — **오늘 이후 입력 불가** |
| `nursingProvided` · `nursingNotes` | 간호 제공 여부·메모 |
| `medicationProvided` · `medicationNotes` | 투약 제공 여부·메모 |
| `medicalVisit` · `medicalInstitution` · `medicalNotes` | 진료(외래) 여부·의료기관·메모 |
| `notes` | 종합 메모(선택) |

| 규칙 | 내용 |
|------|------|
| UNIQUE | **동일 이용자·동일 제공일 1건** — 중복 시 **「해당 일자 간호급여 제공 기록이 이미 존재합니다.」** |
| CHECK | **간호·투약·진료 중 최소 1개** 선택 필수 |
| 권한 | **`hq_admin`·`branch_admin`·`social_worker`·`caregiver`** — `guardian` **403** |

#### API 요약

| 엔드포인트 | 메서드 | 용도 |
|-----------|:------:|------|
| `/api/v1/nursing/service-records` | GET | `fromDate`·`toDate`·`clientId` 필터 목록 — **`toDate` 미지정=오늘** · **`fromDate` 미지정=`toDate−90일`** (Q352) |
| — | POST | `{ clientId, serviceDate, nursingProvided, … }` 등록 |
| `/{recordId}` | PATCH | 동일 필드 수정 |

> 관련: FAQ **Q348·Q352** · ADMIN_GUIDE §6-2-9f · §5-22 제공 리포트 · BENCHMARK_REPORT L03_M01

### 5-21. 배설·경관·유치도뇨 관리 (L03_M06, `/nursing/excretion-tubes`)

케어포 **view.excretion_hose** (3-2 배설·경관 관리)에 대응합니다. **배설 관리·비위관(경관영양)·유치도뇨관** 3종 관리 기록을 등록합니다 (BNK-216/217, FE `12591d4`, V124).

#### 화면 구성

| 영역 | 설명 |
|------|------|
| **`NursingContextNav`** | **배설·경관** 탭 활성 |
| **등록·수정 폼** | **`NursingExcretionTubeRecordForm`** — 관 종류·규격·삽입일·교체 예정일 |
| **리포트 패널** | **`NursingExcretionTubeReportPanel`** — 유형별 건수 StatCard·목록 |
| **최근 기록 표** | 이용자·기록일·관 종류·규격·교체 예정일 |

#### 등록 절차

1. SideNav **기록 → 배설·경관 관리 (L03_M06)** 또는 **`/nursing/excretion-tubes`** 로 이동합니다.
2. **이용자**·**기록일**·**관 종류**를 선택합니다.

| 관 종류 (`tubeType`) | 설명 |
|---------------------|------|
| `EXCRETION` | 배설 관리 |
| `NG_TUBE` | 비위관(경관영양) |
| `URINARY_CATHETER` | 유치도뇨관 |

3. **규격**(`tubeSize`)·**삽입일**·**교체 예정일**·**관리 내용**을 입력합니다.
4. **저장** — **`POST /api/v1/nursing/excretion-tube-records`**

#### 수정·리포트

- 목록 **수정** → **`PATCH /api/v1/nursing/excretion-tube-records/{recordId}`**
- 상단 리포트 — **`GET /api/v1/nursing/excretion-tube-records/reports`** — 유형별 집계

| 규칙 | 내용 |
|------|------|
| 권한 | **`hq_admin`·`branch_admin`·`social_worker`·`caregiver`** |
| 기록일 | **오늘 이후 입력 불가** (injectable `Clock`) |

> 관련: FAQ **Q349** · ADMIN_GUIDE §6-2-9g

### 5-22. 간호급여 제공 리포트 (L03_M07/M09/M10, `/nursing/service/reports/*`)

L03_M01 제공기록을 기반으로 **3종 리포트**를 조회합니다 (FE `2a05271`, `NursingServiceReportsPage`).

> **care-scoped 리포트 (권장, Q386)**: SideNav **기록** 그룹의 **`/care/reports/nursing-service`**·**`/hospital-visits`**·**`/medication-delivery`** 가 동일 집계를 **L02 RBAC**(`hq_admin`·`branch_admin`·`social_worker`)으로 제공합니다 — §5-36 참고. 아래 **`/nursing/service/reports/*`** 경로는 **간호 모듈 컨텍스트**에서도 계속 사용할 수 있습니다.

#### 화면·탭

| 경로 | PAM | 설명 |
|------|-----|------|
| `/nursing/service/reports/total` | **L03_M07** | 통합 간호제공 — 간호·투약·진료 건수 집계 |
| `/nursing/service/reports/hospital-visits` | **L03_M09** | 병의원 진료내역 — `medicalVisit=true` 필터 |
| `/nursing/service/reports/medication-delivery` | **L03_M10** | 투약제공 — `medicationProvided=true` 필터 |

상단 **`NursingServiceReportNav`** — 3탭 전환 · **`NursingContextNav` → 제공 리포트** 진입.

#### 조회 절차

1. **`/nursing/service/reports/total`**(또는 병의원·투약 탭)로 이동합니다.
2. **기간(`fromDate`·`toDate`)**·**이용자**(선택)를 지정하고 **조회**합니다.
3. **StatCard** — 총 건수·유형별 건수(통합 리포트).
4. **제공 기록 표** — 이용자·제공일·제공 항목·의료기관·**비고**. BE가 **snake_case**(`nursing_notes` 등)만 반환해도 FE가 camelCase·snake_case를 모두 읽어 비고 열에 표시합니다 (`c97706b`).
5. 조회 실패 시 **이전 데이터가 남지 않도록** 목록이 초기화됩니다 (`89dc52d`).

#### API 요약

| 엔드포인트 | PAM | 용도 |
|-----------|-----|------|
| `GET /api/v1/nursing/service-records/reports/total` | L03_M07 | 통합 간호제공 리포트 |
| `GET …/reports/hospital-visits` | L03_M09 | 병의원 진료내역 |
| `GET …/reports/medication-delivery` | L03_M10 | 투약제공 리포트 |

> 관련: FAQ **Q350** · ADMIN_GUIDE §6-2-9h · §5-20 제공기록

### 5-23. 집중배설관찰 (L02_M02, v3.1 Must — **화면 연동 완료**)

케어포 **2-2 집중배설관찰**(`view.care_excretion`)에 대응하는 **요양기록** 화면입니다 (FE `1264c16`, BE `fd42b7e`, **V130**). SideNav **기록 → 집중배설관찰 (L02_M02)** 또는 **`/care/intensive-excretion`** 으로 이동합니다 (FAQ **Q359**).

#### 대상·권한

| 역할 | 조회 | 등록·수정 |
|------|:----:|:--------:|
| `hq_admin`·`branch_admin`·`social_worker`·`caregiver` | ✅ | ✅ |
| `guardian` | ❌ | ❌ |

> **활성 지점 필수**: `hq_admin`은 **지점 선택기**로 작업 지점을 고른 뒤 사용하세요. 미선택 시 **403**(`활성 지점이 선택되지 않았습니다.`).

#### 등록·수정 절차

1. **기록** 그룹에서 **「집중배설관찰 (L02_M02)」** 를 선택합니다.
2. 하단 **「새 관찰 기록」** 카드에서 **`IntensiveExcretionObservationForm`** 을 작성합니다.
3. 필수 항목을 입력하고 **저장**을 누릅니다.

| 필드 | 필수 | 설명 |
|------|:----:|------|
| 이용자 | ✅ | 드롭다운 — 활성 지점 소속 이용자 |
| 관찰일 | ✅ | **오늘 이후 불가** |
| 관찰 시각 | — | `HH:mm` |
| 배설 유형 | ✅ | 소변 · 대변 · 소변+대변 (`URINATION`·`DEFECATION`·`BOTH`) |
| 배변 상태 | — | 정상·묽음·딱딱함·혈변·기타 — **소변 관찰 시 입력 불가** |
| 양·빈도 | — | 자유 텍스트 |
| 관찰 내용 | △ | **조치 내용과 둘 중 하나 이상** 필수 |
| 조치 내용 | △ | 관찰 후 취한 조치 |
| 비고 | — | 추가 메모 |

4. 목록 표에서 행을 선택하면 **수정** 모드로 전환됩니다.
5. 서버 오류는 **필드 단위**로 표시됩니다 (`Field` render-prop).

#### 조회

- 화면 진입 시 **최근 90일** 기록이 자동 로드됩니다 (`GET /api/v1/care/intensive-excretion-observations`).
- 목록에는 이용자명·관찰일·유형·배변 상태·관찰/조치 요약이 표시됩니다.

> **건강 기록(`/health`)·간호 배설기록(L03_M06 `/nursing/excretion-tubes`)과 구분**: L02_M02는 **요양기록 집중배설관찰** 전용입니다. L03_M06은 **경관·유치도뇨 등 간호급여** 기록입니다.

> 관련: FAQ **Q359** · ADMIN_GUIDE §6-2-13 · REQUIREMENTS L02 v3.1 Must

### 5-24. 신체제재 기록 (L02_M07, v3.1 Must — **화면 연동 완료**)

케어포 **2-4 신체제재**(`view.care_sanction`)에 대응하는 **요양기록** 화면입니다 (FE `14a2bb9`/`4a47675`, BE `ea6092a`, **V131**). SideNav **기록 → 신체제재 기록 (L02_M07)** 또는 **`/care/body-restraint`** 으로 이동합니다 (FAQ **Q361**·**Q454**).

> **API 응답 정규화 (Q454, FE `4a47675`)**: 이용자·기록 목록 API가 **`client_id`/`client_name` snake_case** 또는 **`items[]` 래핑** 형태여도 등록·조회가 동작합니다. 응답 형식 오류 시 **빈 목록 대신 명확한 Alert**가 표시됩니다.

> **func.php 2-4(차량관리)와 무관** — 케어포 demo-work `view.care_sanction` 번호 체계만 대응합니다.

#### 대상·권한

| 역할 | 조회 | 등록·수정 |
|------|:----:|:--------:|
| `hq_admin`·`branch_admin`·`social_worker`·`caregiver` | ✅ | ✅ |
| `guardian` | ❌ | ❌ |

#### 등록·수정 절차

1. **기록** 그룹에서 **「신체제재 기록 (L02_M07)」** 를 선택합니다.
2. 하단 **「새 제재 기록」** 카드에서 **`BodyRestraintRecordForm`** 을 작성합니다.
3. 필수 항목(이용자·제한일·시작 시각·제한 방법·제한 사유)을 입력하고 **저장**을 누릅니다.
4. 목록에서 **수정**을 누르면 동일 폼으로 PATCH 합니다.

#### 폼 필드

| 필드 | 필수 | 설명 |
|------|:----:|------|
| 이용자 | ✅ | 활성 지점 소속 이용자 |
| 제한일 | ✅ | **오늘 이후 불가** |
| 시작 시각 | ✅ | `HH:MM` |
| 종료 시각 | — | `startedAt` 이후만 허용 |
| 제한 방법 | ✅ | 침대 난간 · 조끼형 · 의자·테이블 · 손싸개 · 안전벨트 · 기타 |
| 제한 부위 | — | 자유 입력 |
| 제한 사유 | ✅ | 공백 불가 (인권 기록 요건) |
| 대체 시도 | — | 대체 수단 시도 내용 |
| 보호자 통지 | — | 체크박스 (기본 미통지) |
| 해제 사유 | — | 제재 해제 시 |
| 비고 | — | 자유 입력 |

#### API 요약

| API | 용도 |
|-----|------|
| `GET /api/v1/care/body-restraint-records?fromDate=&toDate=&clientId=` | 기간·이용자별 목록 — 생략 시 **최근 90일** |
| `POST /api/v1/care/body-restraint-records` | 신규 등록 |
| `PATCH /api/v1/care/body-restraint-records/{recordId}` | 수정 |

> **L02_M02(`/care/intensive-excretion`)·L03_M06(`/nursing/excretion-tubes`)과 구분**: L02_M07은 **신체제재 인권 기록** 전용입니다.

> 관련: FAQ **Q361** · ADMIN_GUIDE §6-2-14 · REQUIREMENTS L02 v3.1 Must

### 5-25. 요양급여 주간 제공기록 (L02_M01, v3.1 Must — **화면 연동 완료**)

케어포 **2-1 요양급여 제공기록**(`view.care_service_weekly`)에 대응하는 **요양기록** 화면입니다 (FE `41b2123`, BE `13b8a37`, **V134**). SideNav **기록 → 요양급여 제공기록 (L02_M01)** 또는 **`/care/weekly-service-records`** 로 이동합니다 (FAQ **Q362**).

#### 대상·권한

| 역할 | 조회 | 등록·수정 |
|------|:----:|:--------:|
| `hq_admin`·`branch_admin`·`social_worker`·`caregiver` | ✅ | ✅ |
| `guardian` | ❌ | ❌ |

#### 등록·수정 절차

1. **기록** 그룹에서 **「요양급여 제공기록 (L02_M01)」** 을 선택합니다.
2. **「새 주간 기록」** 카드에서 **`CareServiceWeeklyRecordForm`** 을 작성합니다.
3. **이용자**와 **주 시작일(월요일)** 을 선택하고, 7개 영역 중 **1개 이상** 내용을 입력한 뒤 **저장**합니다.
4. 목록에서 **수정**을 누르면 동일 폼으로 PATCH 합니다.

#### 상태변화 기록 7일 SLA 안내 (FAQ21817, G39, Q513, FE `b881883`)

목록 로딩 후 **warning Alert** 가 표시되면 **상태변화 기록(`stateChangeNotes`)** 이 **주 1회 이상·7일 이내** 작성되지 않은 이용자입니다.

| Alert 상태 | 의미 | 조치 |
|------------|------|------|
| **상태변화 기록 없음** | 해당 이용자 **`stateChangeNotes` 미작성** | **새 주간 기록** 등록 |
| **이번 주 작성 필요** | 마지막 기록 후 **7일 이내**이나 **이번 주 미작성** | **이번 주(월요일 시작) 기록** 작성 |
| **기한 초과 (N일 경과)** | 마지막 주 종료 후 **7일 초과** | **즉시 `stateChangeNotes` 보완** |

> **법적 근거**: 이지케어 FAQ21817 · 시행규칙 별지 — **요양보호사 상태변화 기록지** 주 1회 이상·7일 이내. 대시보드 **지표44「주간 상태변화」** 위젯(Q276)과 병행 확인하세요.

#### 폼 필드 (7 note 영역)

| 필드 | 필수 | 설명 |
|------|:----:|------|
| 이용자 | ✅ | 활성 지점 소속 이용자 |
| 주 시작일 | ✅ | **월요일만** 허용 (`week_start_date` CHECK) |
| 신체활동 | — | `physicalCareNotes` |
| 인지활동 | — | `cognitiveActivityNotes` |
| 식사 | — | `mealAssistanceNotes` |
| 간호 | — | `nursingNotes` |
| 프로그램 | — | `programParticipationNotes` |
| 상태변화 | — | `stateChangeNotes` — **주 1회 이상·7일 이내** (FAQ21817, Q513) |
| 특이사항 | — | `specialNotes` — **RFID 태그 전송 시 별지 서식과 동등** (FAQ21817, Q514) |
| 비고 | — | 자유 입력 |

> **7개 note 중 최소 1개**는 공백이 아니어야 저장됩니다.

#### API 요약

| API | 용도 |
|-----|------|
| `GET /api/v1/care/weekly-service-records?fromDate=&toDate=&clientId=` | 기간·이용자별 목록 |
| `POST /api/v1/care/weekly-service-records` | 신규 등록 |
| `PATCH /api/v1/care/weekly-service-records/{recordId}` | 수정 |

> 관련: FAQ **Q362** · FAQ **Q513** · FAQ **Q514** · ADMIN_GUIDE §6-2-15 · REQUIREMENTS L02 v3.1 Must

### 5-26. 목욕 일정·제공현황 (L02_M03, v3.1 Must — **화면 연동 완료**)

케어포 **2-3 목욕일정 및 제공현황**(`view.care_bath_manage`)에 대응합니다 (FE `9a957fb`/`d2815d2`, BE `49a1721`/`e703252`, **V136**). SideNav **기록 → 목욕 일정·제공현황 (L02_M03)** 또는 **`/care/bathing-schedules`** (FAQ **Q363·Q598**).

#### 대상·권한

| 역할 | 조회 | 등록·수정 | 전월 복사 |
|------|:----:|:--------:|:--------:|
| `hq_admin`·`branch_admin`·`social_worker`·`caregiver` | ✅ | ✅ | `hq_admin`·`branch_admin`·`social_worker`만 |
| `guardian` | ❌ | ❌ | ❌ |

#### 등록·수정 절차

1. **기록** 그룹에서 **「목욕 일정·제공현황 (L02_M03)」** 을 선택합니다.
2. 상단 **「대상 월」** 을 선택하고 **조회**합니다.
3. **「새 목욕 일정」** 카드에서 **`BathingScheduleForm`** 을 작성합니다.
4. 이용자·예정일·목욕 유형·제공 상태를 입력하고 **저장**합니다.
5. 상태를 **제공 완료**로 바꿀 때는 **제공 내용**(`provisionNotes`)이 필수입니다.
6. **취소**·**미제공** 처리 시 **비고(사유)**(`notes`)가 필수입니다 (`47a4e25`).

#### 전월 일정 복사 (G-BATHING, Q598)

월초에 전월 패턴을 당월로 일괄 생성할 때 사용합니다 (케어포 3-3 전월 일정 불러오기).

1. **대상 월**을 복사 **받을** 월(예: `2026-07`)로 설정합니다.
2. **「전월 일정 복사」** 를 클릭합니다 — 확인 대화상자에서 **전월(`2026-06`)의 예정·완료 일정**이 대상 월로 복사됨을 확인합니다. 복사 API 호출 중 버튼에 **`aria-busy="true"`** 가 설정됩니다 (UXD-150, Q606).
3. 성공 시 **「전월(…) 일정 N건을 …로 복사했습니다. (건너뜀 M건)」** 메시지가 표시됩니다.
4. **복사 규칙** — 전월 **`SCHEDULED`·`COMPLETED`** 만 복사 · **`CANCELLED`·`SKIPPED` 제외** · 대상 월 **같은 이용자·같은 날짜**에 기존 일정이 있으면 **건너뜀** · 복사된 일정은 **`SCHEDULED`** 로 생성 · **목욕 유형·시간·비고**는 유지 · **날짜는 전월과 동일 일(day-of-month)** 로 매핑(말일 보정 포함)

#### 목욕 유형·상태

| 목욕 유형 | 코드 |
|----------|------|
| 전신 목욕 | `FULL_BATH` |
| 부분 목욕 | `PARTIAL_BATH` |
| 족욕 | `FOOT_BATH` |
| 샴푸만 | `SHAMPOO_ONLY` |

| 제공 상태 | 의미 |
|----------|------|
| `SCHEDULED` | 예정 |
| `COMPLETED` | 제공 완료 — **제공 내용 필수** |
| `CANCELLED` | 취소 — **사유 필수** |
| `SKIPPED` | 미제공 — **사유 필수** |

#### API 요약

| API | 용도 |
|-----|------|
| `GET /api/v1/care/bathing-schedules?fromDate=&toDate=&clientId=` | 목록 |
| `POST /api/v1/care/bathing-schedules` | 신규 등록 |
| `PATCH /api/v1/care/bathing-schedules/{recordId}` | 수정 |
| `POST /api/v1/care/bathing-schedules/copy-from-previous-month` | **전월 `SCHEDULED`/`COMPLETED` → 대상 월 일괄 복사** (Q598) |

> **L02_M01(`/care/weekly-service-records`)·L03 간호기록과 구분**: L02_M03은 **목욕 일정·제공 현황** 전용입니다.

> 관련: FAQ **Q363·Q598** · ADMIN_GUIDE §6-2-16 · REQUIREMENTS L02 v3.1 Must

### 5-27. 통합식사도움기록 (L02_M13, v3.1 Must — **화면 연동 완료**)

케어포 **2-1-1 통합식사도움기록**(`view.total_meal`)에 대응합니다 (BE `81a2223` / FE `9ad8346`/`38642e2`/`1c8f236`, **V140**). SideNav **기록 → 통합식사도움기록 (L02_M13)** 또는 **`/care/meal-assistance-records`** 로 이동합니다 (FAQ **Q366·Q442·Q449**).

> **API 오류 표시 (Q442)**: 조회 API가 **배열·`items[]` 형식이 아니면** 빈 목록 대신 **「통합식사도움기록 조회 응답 형식이 올바르지 않습니다.」** Alert가 표시됩니다. IT 담당에게 **`GET /care/meal-assistance-records`** 응답을 확인해 달라고 요청하세요.

> **이용자 선택 (Q449)**: 이용자 목록 API가 **`client_id`/`client_name` snake_case** 또는 **`{ items: [...] }`** 형태여도 **등록 폼 이용자 드롭다운**이 정상 표시됩니다. 이용자를 고른 뒤 저장하면 **`clientId`** 가 서버로 전달됩니다.

#### 대상·권한

| 역할 | 조회 | 등록·수정 |
|------|:----:|:--------:|
| `hq_admin`·`branch_admin`·`social_worker`·`caregiver` | ✅ | ✅ |
| `guardian` | ❌ | ❌ |

#### 등록·수정 절차

1. **기록** 그룹에서 **「통합식사도움기록 (L02_M13)」** 을 선택합니다.
2. **「통합식사도움기록 등록」** 카드에서 **`MealAssistanceRecordForm`** 을 작성합니다.
3. **이용자**·**기록일**·**식사 구분**·**섭취량**·**식이 제한**·**도움 내용**을 입력하고 **저장**합니다.
4. 목록 **「수정」** 으로 동일 폼에서 PATCH 합니다.

#### 폼 필드

| 필드 | 필수 | 설명 |
|------|:----:|------|
| `clientId` | ✅ | 활성 지점 소속 이용자 |
| `recordDate` | ✅ | **오늘 이후 불가** |
| `mealType` | ✅ | `BREAKFAST`(아침) · `LUNCH`(점심) · `SNACK`(간식) |
| `intakeLevel` | ✅ | `WELL`(잘 먹음) · `NORMAL`(보통) · `LESS`(적게) |
| `dietRestriction` | ✅ | `NONE` · `LOW_SALT` · `DIABETIC` · `SOFT` · `OTHER` (기본 `NONE`) |
| `assistanceDetail` | ✅ | 식사 도움 내용 — 공백 불가 |
| `nutritionistNote` | — | 영양사 메모 |

> **(이용자, 기록일, 식사 구분)** 조합은 **1건**만 허용됩니다. 중복 시 `422` — 「해당 일자·식사 구분에 이미 통합식사도움 기록이 있습니다.」

#### API 요약

| API | 용도 |
|-----|------|
| `GET /api/v1/care/meal-assistance-records?fromDate=&toDate=&clientId=` | 기간·이용자별 목록 — 생략 시 **최근 90일** |
| `POST /api/v1/care/meal-assistance-records` | 신규 등록 |
| `PATCH /api/v1/care/meal-assistance-records/{recordId}` | 수정 |

> **L02_M01 주간 기록의 `mealAssistanceNotes`·식사 모듈(`/meals`)과 구분**: L02_M13은 **일별·식사 구분별 통합 식사 도움** 전용 기록입니다.

> 관련: FAQ **Q366** · ADMIN_GUIDE §6-2-18 · REQUIREMENTS L02 v3.1 Must

### 5-28. 요양급여 특이사항 (L02_M15, v3.1 Must — **화면 연동 완료**)

케어포 **2-1-3 요양급여 특이사항 관리**(`view.care_service_bigo_all`)에 대응합니다 (FE `3549896`, V134 **`special_notes`**). SideNav **기록 → 요양급여 특이사항 (L02_M15)** 또는 **`/care/service-special-notes`** 로 이동합니다 (FAQ **Q368**).

> **L02_M01 주간 제공기록과 동일 API**(`weekly-service-records`)를 사용하되, 이 화면은 **`specialNotes` 필드**만 편집·목록에 **특이사항이 있는 주간 기록**만 표시합니다.

#### 대상·권한

| 역할 | 조회 | 등록·수정 |
|------|:----:|:--------:|
| `hq_admin`·`branch_admin`·`social_worker`·`caregiver` | ✅ | ✅ |
| `guardian` | ❌ | ❌ |

#### 등록·수정 절차

1. **기록** 그룹에서 **「요양급여 특이사항 (L02_M15)」** 을 선택합니다.
2. **「특이사항 등록」** 카드에서 **`CareServiceSpecialNotesForm`** 을 작성합니다.
3. **이용자**·**주 시작일(월요일)** · **특이사항**을 입력하고 **저장**합니다.
4. **신규 등록** 시 해당 주에 L02_M01 주간 기록이 없으면 **POST**로 생성하고, 있으면 **PATCH**로 **`specialNotes`만** 갱신합니다 (다른 7개 note 영역은 유지).

#### 폼 필드

| 필드 | 필수 | 설명 |
|------|:----:|------|
| 이용자 | ✅ (신규) | 활성 지점 소속 이용자 |
| 주 시작일 | ✅ | **월요일만** 허용 |
| 특이사항 | ✅ | `specialNotes` — 공백 불가 · **RFID↔별지 동치 help** (Q514) |

#### API 요약

| API | 용도 |
|-----|------|
| `GET /api/v1/care/weekly-service-records?fromDate=&toDate=&clientId=` | 주간 기록 목록 (특이사항 필터는 FE) |
| `POST /api/v1/care/weekly-service-records` | 신규 주간 기록 + 특이사항 |
| `PATCH /api/v1/care/weekly-service-records/{recordId}` | 특이사항 수정 (다른 note 보존) |

> 관련: FAQ **Q368** · USER_MANUAL §5-25 · ADMIN_GUIDE §6-2-19 · REQUIREMENTS L02 v3.1 Must

---

### 5-29. 케어 리포트 — 요양·식사·배설 통계 (L02_M04, `/care/reports/meal-excretion`)

케어포 **2-5.요양/식사(조치사항)/화장실 리포트**(`view.care_meal_excretion`)에 대응합니다. **기간별 집계 리포트**로 통합식사도움·집중배설관찰·주간 요양 메모를 한 화면에서 확인합니다 (BE `c655743`/`27b40cd` + FE `c5f82a6`/`d2145b0`, Q369).

> **상태 (2026-06-16)**: backend ✅ · frontend ✅ — SideNav **기록 → 요양/식사/화장실 리포트 (L02_M04)**

#### 접근 · 화면

1. SideNav **기록** → **「요양/식사/화장실 리포트 (L02_M04)」** (또는 `/care/reports/meal-excretion`).
2. 상단 **`CareReportContextNav`** in-page 네비에서 **L02_M04·M05·M06·M17** 리포트를 전환할 수 있습니다 (`fa20943`).
3. **조회 조건** — **시작일·종료일·이용자(선택)** → **「조회」** (`Field` render-prop, Q369).
4. **StatCard** — 식사도움·배설관찰·주간 요양 메모 **건수** 요약.
5. 하단 **3개 표** — 통합식사도움 · 집중배설관찰 · 주간 요양 메모 상세.
6. **「인쇄」** — 브라우저 인쇄 (`window.print()`, `ds-care-report-print-root`, Q369).

#### 조회 대상·권한

| 역할 | 권한 |
|------|------|
| `hq_admin` | 전 지점 (Branch Switcher 활성 지점) |
| `branch_admin` | 자기 지점 |
| `social_worker` | 자기 지점 |
| `caregiver` | **접근 불가** — API **`403`** (BE `2495753`, Q383). SideNav에 메뉴가 보여도 **조회 시 오류** — 센터장·사회복지사에게 요청하세요. **P2**: FE nav `roles` 정합 |

#### API 요약

| API | 용도 |
|-----|------|
| **`GET /api/v1/care/reports/care-meal-excretion?fromDate=2026-06-01&toDate=2026-06-30&clientId=<uuid>`** | **L02_M04 리포트** — 기간·이용자별 집계 |

> **`fromDate`/`toDate` 생략** 시 BE가 기록 데이터 기준으로 기간을 자동 설정합니다 (`27b40cd`).

**응답 예시**:

```json
{
  "fromDate": "2026-06-01",
  "toDate": "2026-06-30",
  "mealRecordCount": 28,
  "excretionObservationCount": 20,
  "weeklyCareNoteCount": 4,
  "mealRecords": [],
  "excretionObservations": [],
  "weeklyCareNotes": []
}
```

---

### 5-30. 목욕 리포트 (L02_M05, `/care/reports/bath-help`)

케어포 **2-6.목욕도움 리포트**(`view.bath_help`)에 대응합니다. **기간별 목욕 일정·제공 현황**을 StatCard·표로 확인합니다 (FE `c5f82a6`, Q369).

> **상태 (2026-06-16)**: backend ✅ · frontend ✅ — SideNav **기록 → 목욕도움 리포트 (L02_M05)**

#### 조회 절차

1. SideNav **기록** → **「목욕도움 리포트 (L02_M05)」** (또는 `/care/reports/bath-help`).
2. **시작일·종료일·이용자** 필터 → **「조회」**.
3. **StatCard** — 예정·완료·취소·스킵 **건수**.
4. **목욕 일정 표** — 일자·시간·목욕 유형·상태 Badge.
5. **「인쇄」** — §5-29와 동일 (`d2145b0`).

#### API 요약

| API | 용도 |
|-----|------|
| **`GET /api/v1/care/reports/bath-help?fromDate=2026-06-01&toDate=2026-06-30&clientId=<uuid>`** | **L02_M05 리포트** — 목욕 일정 집계 |

**응답 예시**:

```json
{
  "fromDate": "2026-06-01",
  "toDate": "2026-06-30",
  "totalSchedules": 12,
  "completedCount": 11,
  "scheduledCount": 0,
  "cancelledCount": 1,
  "skippedCount": 0,
  "items": []
}
```

---

#### FAQ & 제약

- **기간 필터**: 기본값은 **당월 1일 ~ 오늘**. hq_admin은 Branch Switcher로 지점을 확인하세요.
- **개별 이용자**: 이용자 드롭다운으로 1명만 조회 가능.
- **출력**: **인쇄** Fixed · **CSV 다운로드** P2.
- **관련**: REQUIREMENTS L02 v3.1 Must · FAQ Q369 · API_SPEC §10-7

---

### 5-31. 집중배설 리포트 (L02_M17, `/care/reports/intensive-excretion`)

케어포 **2-8.집중배설관찰 리포트**(`view.total_excretion`)에 대응합니다. **L02_M02 집중배설관찰** 기록을 기간별로 집계하는 **read-only 리포트**입니다 (BE `ae7e744` + FE `fa20943`, Q371).

> **상태 (2026-06-16)**: backend ✅ · frontend ✅ — SideNav **기록 → 집중배설 리포트 (L02_M17)**

#### 접근 · 화면

1. SideNav **기록** → **「집중배설 리포트 (L02_M17)」** (또는 `/care/reports/intensive-excretion`).
2. **`CareReportContextNav`** — M04·M05·M06·M17 리포트 간 전환.
3. **조회 조건** — **시작일·종료일·이용자(선택)** → **「조회」** (`Field` render-prop).
4. **StatCard** — 총 관찰·배뇨·배변·양쪽·중재 **건수** 요약.
5. **관찰 상세 표** — 일자·시간·배설 유형·양·중재 여부.
6. **「인쇄」** — `window.print()` · `ds-care-report-print-root` (§5-29와 동일).

#### API 요약

| API | 용도 |
|-----|------|
| **`GET /api/v1/care/reports/intensive-excretion?fromDate=2026-06-01&toDate=2026-06-30&clientId=<uuid>`** | **L02_M17 리포트** — 배뇨·배변·양쪽·중재 건수 집계 |

**응답 예시**:

```json
{
  "fromDate": "2026-06-01",
  "toDate": "2026-06-30",
  "totalObservationCount": 42,
  "urinationCount": 18,
  "defecationCount": 15,
  "bothCount": 6,
  "interventionCount": 3,
  "items": []
}
```

| 역할 | 권한 |
|------|------|
| `hq_admin`·`branch_admin`·`social_worker` | 조회 |
| `caregiver` | **403** (Q383) |

> **`fromDate`/`toDate` 생략** 시 BE가 데이터 기준으로 기간을 자동 설정합니다 (`27b40cd` 패턴).  
> 입력 원본: §5-23 **`/care/intensive-excretion`** (L02_M02).  
> 관련: FAQ Q371 · ADMIN_GUIDE §6-2-21 · REQUIREMENTS L02 v3.1 rpt cluster

---

### 5-32. 체위변경 대상자 리포트 (L02_M06, `/care/reports/position-change`)

케어포 **2-7.체위변경 대상자 관리 리포트**(`view.position_YC_report`)에 대응합니다. **US-O03 욕창 위험평가·체위변경 케어** 기록을 기간별로 집계합니다 (BE `9cc0c1d` + FE `fa20943`, Q372).

> **상태 (2026-06-16)**: backend ✅ · frontend ✅ — SideNav **기록 → 체위변경 대상자 리포트 (L02_M06)**

#### 접근 · 화면

1. SideNav **기록** → **「체위변경 대상자 리포트 (L02_M06)」** (또는 `/care/reports/position-change`).
2. **`CareReportContextNav`** — 4개 요양 리포트 간 전환.
3. **조회 조건** — **시작일·종료일·이용자(선택)** → **「조회」**.
4. **StatCard** — 위험등급(고·중·저)·대상자·예방계획·케어 기록 **건수**.
5. **위험평가 표** — 평가일·Braden 점수·위험 Badge·예방계획 여부.
6. **체위변경 케어 표** — 케어일·부위·욕창 단계·예방 조치.
7. **「인쇄」** — §5-29와 동일.

#### API 요약

| API | 용도 |
|-----|------|
| **`GET /api/v1/care/reports/position-change?fromDate=2026-06-01&toDate=2026-06-30&clientId=<uuid>`** | **L02_M06 리포트** — 위험등급·대상자·예방계획·케어 기록 집계 |

**응답 예시**:

```json
{
  "fromDate": "2026-06-01",
  "toDate": "2026-06-30",
  "totalAssessmentCount": 8,
  "highRiskCount": 2,
  "moderateRiskCount": 3,
  "lowRiskCount": 3,
  "targetClientCount": 5,
  "preventionPlanCount": 4,
  "careRecordCount": 12,
  "preventionMeasureCount": 10,
  "assessments": [],
  "careRecords": []
}
```

| 역할 | 권한 |
|------|------|
| `hq_admin`·`branch_admin`·`social_worker` | 조회 |
| `caregiver` | **403** (Q383) |

> 입력 원본: **`/nursing/pressure-ulcer`** (US-O03, §5-16~§5-19).  
> 관련: FAQ Q372 · ADMIN_GUIDE §6-2-22 · REQUIREMENTS L02 v3.1 rpt cluster

---

### 5-33. 수급자별 급여제공 리포트 (L02_M11, `/care/reports/patient-service`)

케어포 **수급자별 급여제공**(`view.patient_service`)에 대응합니다. **1명의 이용자**에 대해 L02_M01·M13·M03·M02·M07 입력을 **한 화면**에서 조회·인쇄하는 read-only 리포트입니다 (BE `2cf0908` + FE `ff9c8c5`, Q373).

#### 조회 절차

1. SideNav **기록** → **「수급자별 급여제공 리포트 (L02_M11)」** (또는 `/care/reports/patient-service`).
2. **`CareReportContextNav`** 6탭 중 **L02_M11** 탭으로 이동할 수 있습니다.
3. **기간**(시작일·종료일)·**이용자**를 선택하고 **조회**합니다.
4. 상단 **StatCard** — 주간 요양·식사도움·목욕·집중배설·신체제재 건수·합계.
5. 하단 **5종 상세 표** — 주간 제공기록·식사도움·목욕·집중배설·신체제재 목록.
6. **「인쇄」** — `window.print()` · **`ds-care-report-print-root`** CSS (L02_M04/M05와 동일 패턴).

| API | 용도 |
|-----|------|
| **`GET /api/v1/care/reports/patient-service?fromDate=2026-06-01&toDate=2026-06-30&clientId=<uuid>`** | **L02_M11 리포트** — 이용자 1명 cross-source 집계 |

| 역할 | 권한 |
|------|------|
| `hq_admin`·`branch_admin`·`social_worker` | 조회·인쇄 |
| `caregiver` | **403** (Q383) |

> **`fromDate`/`toDate` 생략** 시 기록 데이터 기준 자동 기간. **`clientId`** 미선택 시 API 오류 — 이용자 선택 필수.  
> 관련: FAQ Q373 · ADMIN_GUIDE §6-2-23 · REQUIREMENTS L02 v3.1 rpt cluster

---

### 5-34. 급여제공 서비스 집계 리포트 (L02_M12, `/care/reports/service-summary`)

케어포 **급여제공 서비스 집계**(`view.service`)에 대응합니다. **활성 지점 전체 이용자**의 L02 입력 건수를 **이용자별 행**으로 집계하는 read-only 리포트입니다 (BE `2cf0908` + FE `ff9c8c5`, Q374).

#### 조회 절차

1. SideNav **기록** → **「급여제공 서비스 집계 리포트 (L02_M12)」** (또는 `/care/reports/service-summary`).
2. **`CareReportContextNav`** **L02_M12** 탭.
3. **기간** 선택 후 **조회** — **`clientId` 필터 없음**(지점 전체).
4. 상단 **StatCard** — 이용자 수·5종 합계·`totalServiceEntries`.
5. **이용자별 집계 표** — 이름순 `rows[]`.
6. **「인쇄」** 버튼.

| API | 용도 |
|-----|------|
| **`GET /api/v1/care/reports/service-summary?fromDate=2026-06-01&toDate=2026-06-30`** | **L02_M12 리포트** — 지점별 이용자 집계 표 |

| 역할 | 권한 |
|------|------|
| `hq_admin`·`branch_admin`·`social_worker` | 조회·인쇄 (활성 지점 스코프) |
| `caregiver` | **403** (Q383) |

> 관련: FAQ Q374 · ADMIN_GUIDE §6-2-24 · REQUIREMENTS L02 v3.1 rpt cluster · **P2**: CSV export

---

### 5-35. 식사(간식) 선호도 조사 (L02_M16, `/care/meal-preference-surveys`)

케어포 **2-1-4 식사(간식) 선호도 조사 및 반영**(`view.meal_satisfaction`, G-MEAL-PREFERENCE)에 대응합니다. 이용자별 **식사 만족도·선호·비선호 음식·식단 반영 여부**를 기록합니다 (BE `f33252a` + FE `8b804fc`, **V142**, Q375).

#### 등록·조회 절차

1. SideNav **기록** → **「식사 선호도 조사 (L02_M16)」** (또는 `/care/meal-preference-surveys`).
2. 좌측 **`MealPreferenceSurveyForm`** — **`Field` render-prop** 으로 label·id 연결:
   - **이용자** (필수)
   - **조사일** (필수)
   - **식사 구분** — `BREAKFAST`(아침) · `LUNCH`(점심) · `SNACK`(간식)
   - **만족도** — `SATISFIED`(만족) · `NORMAL`(보통) · `DISSATISFIED`(불만족) — Badge 색상 병행
   - **선호 음식**·**비선호 음식**·**반영 내용** (자유 텍스트)
   - **식단 반영 여부** — Checkbox
3. **저장** — `POST /api/v1/care/meal-preference-surveys`.
4. 우측 **최근 조사 목록** — 만족도 Badge·식단 반영 여부·**수정** 버튼 → `PATCH …/{surveyId}`.
5. **동일 이용자·조사일·식사 구분** 중복 등록 시 서버 **`422`** — 기존 행 **수정**을 사용하세요.

| API | 용도 |
|-----|------|
| `GET /api/v1/care/meal-preference-surveys?fromDate=&toDate=&clientId=` | 목록 조회 |
| `POST /api/v1/care/meal-preference-surveys` | 신규 등록 |
| `PATCH /api/v1/care/meal-preference-surveys/{surveyId}` | 수정 |
| `GET /api/v1/care/reports/meal-preference?fromDate=&toDate=&clientId=` | 기간별 만족도 집계 리포트(API 전용, Q385) |

| 역할 | 등록·수정 | 조회 |
|------|:---------:|:----:|
| `hq_admin`·`branch_admin`·`social_worker`·`caregiver` | ✅ | ✅ |
| `guardian` | ❌ | ❌ |

> **퇴소·비활성 이용자**에는 신규 등록이 거부됩니다 (V142 trigger).  
> **리포트 API (Q385)**: `GET /care/reports/meal-preference` 는 L02_M16 입력을 만족/보통/불만족 건수로 집계하는 **서버 제공 API**입니다. 현재 FE 전용 화면은 없으며, 운영 점검·연동 검증은 Swagger/API 클라이언트로 수행합니다.
> 관련: FAQ Q375 · ADMIN_GUIDE §6-2-25 · REQUIREMENTS G-MEAL-PREFERENCE

---

### 5-36. L02 care-scoped 간호 리포트 (L02_M14/M09/M10, `/care/reports/nursing-*`)

케어포 **2-11~2-13** 간호 리포트를 **기록** 메뉴에서 **L02 RBAC**으로 조회하는 화면입니다 (BE `002e3eb` + FE `58ee122`, Q386). L03 간호 모듈 API를 **care proxy**로 노출하여 SideNav **기록** 그룹과 일관된 경로·권한을 제공합니다.

#### 화면·탭

| 경로 | PAM | 설명 |
|------|-----|------|
| `/care/reports/nursing-service` | **L02_M14** | 통합 간호제공 — 간호·투약·진료 건수 집계 |
| `/care/reports/hospital-visits` | **L03_M09** | 병의원 진료내역 — `medicalVisit=true` 필터 |
| `/care/reports/medication-delivery` | **L03_M10** | 투약제공 — `medicationProvided=true` 필터 |

상단 **`CareNursingServiceReportNav`** — 3탭 전환 · **`CareNursingServiceReportPage`** 공통 패널. 서브 탭은 **`.ds-context-nav--sub`** 스타일(작은 글꼴·연한 배경)로 상위 **`CareReportContextNav`** 와 시각적으로 구분됩니다 (`8ed937c`, Q390).

하단 **`CareNursingParityPanel`** (**「L02·L03 간호 리포트 연계」**, `140bf92`, Q412) — care-scoped 리포트 화면에서 **관련 화면** 링크를 제공합니다.

| 현재 화면 | 연계 링크 |
|----------|----------|
| `/care/reports/nursing-service` 등 | **간호급여 제공기록 (L03_M01)** (`/nursing/service`) |
| care-scoped 리포트 | 대응 **L03 간호 리포트** (`/nursing/service/reports/*`) |
| L03 간호 리포트 | 대응 **L02 care-scoped 리포트** (`/care/reports/*`) |

> L02_M09(건강상태 평가 리포트 삭제예정)은 케어포 demo **Won't** — **`/health` 건강 기록**으로 안내합니다 (`careLeafParity.js`).

#### 조회 절차

1. SideNav **기록** → **「통합 간호제공 리포트 (L02_M14)」** 등 해당 항목을 선택합니다.
2. **기간(`fromDate`·`toDate`)**·**이용자**(선택)를 지정하고 **조회**합니다.
3. **StatCard** — 총 건수·유형별 건수(통합 리포트).
4. **제공 기록 표** — 이용자·제공일·제공 항목·의료기관·**비고**.
5. **「인쇄」** 버튼.

| API | PAM | 용도 |
|-----|-----|------|
| `GET /api/v1/care/reports/nursing-service` | L02_M14 | 통합 간호제공 리포트 |
| `GET /api/v1/care/reports/hospital-visits` | L03_M09 | 병의원 진료내역 |
| `GET /api/v1/care/reports/medication-delivery` | L03_M10 | 투약제공 리포트 |

| 역할 | 권한 |
|------|------|
| `hq_admin`·`branch_admin`·`social_worker` | 조회·인쇄 |
| `caregiver` | **403** (L02 care report RBAC, Q383) |

> **입력 vs 리포트**: **L02_M14 제공기록 입력**은 **`/nursing/service`** (§5-20) · **집계 리포트**는 본 절 **`/care/reports/*`** 입니다.  
> **L02↔L03 연계 (Q412)**: **`CareNursingParityPanel`** — care-scoped ↔ L03 리포트·제공기록 **상호 링크** · **`careNursingReportsLiveApi.e2e.test.js`** live harness (`5533ef5`).  
> **검증 (BNK-280, Q389)**: BE **`CareNursingReportsPilotServiceFlowE2eTest`** (`2ba2761`) — 3 endpoint delegation chain·aggregate field contracts · FE **`pilotPageFlows.test`** (`6b34d31`).  
> 관련: FAQ **Q386·Q389·Q390·Q412** · ADMIN_GUIDE §6-2-26 · §5-22(간호 모듈 경로) · REQUIREMENTS L02/L03 parity

---

## 6. 요양보호사 (`caregiver`) 매뉴얼

요양보호사는 소속 지점에서 **수기 출석**과 **건강 기록 입력**이 핵심 업무입니다. 파일럿 현장의 주 사용 역할입니다.

### 6-1. 권한 요약

| 기능 | 요양보호사 | 센터장 |
|------|:----------:|:------:|
| 지점 대시보드 조회 | ✅ | ✅ |
| 이용자 목록 조회 | ✅ | ✅ |
| 이용자 등록·수정 | ❌ | ✅ |
| 수기 체크인/아웃 | ✅ | ✅ |
| 건강 기록 입력 | ✅ | ✅ |
| **통합 바이탈 기록** (`/nursing/vital-checks`) | ✅ | ✅ (§5-16) |
| **체중 기록** (`/nursing/weight-records`) | ✅ | ✅ (§5-17) |
| **구강상태 점검** (`/nursing/oral-care-checks`) | ✅ | ✅ (§5-18) |
| **응급상황 기록** (`/nursing/emergency-records`) | ✅ | ✅ (§5-19) |
| **간호급여 제공기록 (L03_M01)** (`/nursing/service`) | ✅ | ✅ (§5-20) |
| **요양급여 주간 제공기록 (L02_M01)** (`/care/weekly-service-records`) | ✅ | ✅ (§5-25) |
| **집중배설관찰 (L02_M02)** (`/care/intensive-excretion`) | ✅ | ✅ (§5-23) |
| **목욕 일정·제공현황 (L02_M03)** (`/care/bathing-schedules`) | ✅ | ✅ (§5-26) |
| **통합식사도움기록 (L02_M13)** (`/care/meal-assistance-records`) | ✅ | ✅ (§5-27) |
| **식사 선호도 조사 (L02_M16)** (`/care/meal-preference-surveys`) | ✅ | ✅ (§5-35) |
| **요양급여 특이사항 (L02_M15)** (`/care/service-special-notes`) | ✅ | ✅ (§5-28) |
| **신체제재 기록 (L02_M07)** (`/care/body-restraint`) | ✅ | ✅ (§5-24) |
| **배설·경관 관리 (L03_M06)** (`/nursing/excretion-tubes`) | ✅ | ✅ (§5-21) |
| **간호급여 제공 리포트** (`/nursing/service/reports/*`) | ✅ 조회 | ✅ (§5-22) |
| **욕창간호 일일 기록** (`/nursing/pressure-ulcer/records`) | ✅ | ✅ (§5-15) |
| 청구·정산 | ❌ | ✅ |
| QR 생성 | ❌ | ✅ |

### 6-2. 일과 개요 (파일럿 기준)

```
[도착] 대시보드에서 오늘 출석 현황 확인
[입소] 수기 체크인 — 이용자별 입소 시각 기록
[낮]   건강 체크(혈압·체온 등)·투약·특이사항 입력
[귀가] 수기 체크아웃 — 교통편 선택 가능
[결석] 결석 사유 입력 (해당 시)
```

### 6-3. 수기 출석 (`/attendance/checkin`)

1. **출석** → **수기 처리**(`/attendance` 또는 `/attendance/checkin`)로 이동합니다.
2. 상단 StatCard에서 입소·귀가·결석·미처리 인원을 확인합니다.
3. 이용자 행에서 **입소**·**귀가**·**결석** 버튼으로 처리합니다 (US-E01·E02).
4. **귀가** 시 `CheckoutModal`에서 교통편(차량 서비스·보호자 동행·자가용·기타)을 선택합니다.
5. 이미 입소된 이용자에게 중복 체크인을 시도하면 오류가 표시됩니다 — 센터장에게 확인하세요.
6. **결석** 시 사유를 입력합니다.

> **API 갭 (Q94)**: 목록에 이용자 이름·상태가 비거나 **미처리 이용자가 안 보이면** §4-4 **Swagger 우회 절차**(입소·귀가·결석)를 사용하세요. 귀가 교통편 미저장 시 FAQ **Q96**.

> 출석·건강 기록에는 **입력한 직원 UUID**(`attendance.created_by`/`health_records.recorded_by`)가 자동 저장됩니다. 수가표 등록·QR 발급에도 동일 actor 감사가 적용됩니다 (V32–V35). 감사·분쟁 대응 시「누가 기록·등록했는지」추적할 수 있습니다.

> QR 셀프 체크인은 보호자·이용자가 처리합니다. 직원은 **지점 QR 생성·게시**만 담당합니다 (센터장 권한).

### 6-3-1. 방문요양 현장 체크인 (`/visits`)

방문요양·통합재가 지점 소속 요양보호사·사회복지사는 **기록 → 방문 일정**에서 당일 확정 일정의 **체크인**·**체크아웃**을 수행합니다 (§5-11, Q180).

| 역할 | 체크인·체크아웃 |
|------|----------------|
| **`caregiver`** | **본인 배정 일정만** — 다른 담당 배정 시 **`422`** (Q307) |
| **`social_worker`·`branch_admin`·`hq_admin`** | **감독 역할** — 배정 직원 **활성·지점 소속**이면 담당과 무관하게 가능 (Q455, `78cfb8a`) |
| **공통** | 배정 직원 **퇴사·비활성·지점 미소속** 시 **`422`** (Q453, `0db1e68`) |

1. `/visits`에서 오늘 날짜를 선택합니다.
2. **청구 일정** 탭에서 **「청구반영」** 열이 **청구반영**인지 확인합니다 (Q376).
3. **`CONFIRMED`** 행의 **체크인** → 방문 시작.
4. 서비스 종료 후 **체크아웃** → 완료 처리.

> **주야간 지점** 요양보호사에게 이 메뉴가 보이더라도, 지점 급여종이 `DAY_CARE`이면 일정 등록·체크인 API가 거부됩니다.

### 6-4. 건강 기록 (`/health`)

센터장·사회복지사와 동일하게 다음을 입력합니다. 상단 **「급여제공 기록 (케어포 3-1)」** 세분화 메뉴로 식사·간호·목욕·프로그램·특이사항 화면에 바로 이동할 수 있습니다 (Q524, `1d5747d`).

| 기록 유형 | 입력 항목 |
|----------|----------|
| 일일 건강 체크 | 혈압, 체온, 혈당, SpO2 |
| 투약 | 약품명, 용량, 시간 |
| 낙상·사고 | 유형, 내용, 발생 시각 |
| 특이사항 | 자유 메모 |

**주의**: 퇴소 처리된 이용자에게는 새 건강 기록을 입력할 수 없습니다.

> **건강·투약·사고 저장** — `/health` **4탭 UI**에서 저장 가능 (Q154·UXD-41). 실패 시 FAQ Q95. **자유 메모(notes)** 는 Swagger.

### 6-5. 일일 체크리스트

- [ ] 지점 선택기가 올바른 지점인지 확인 (다지점 권한 시)
- [ ] 미입소·결석 이용자 센터장에게 공유
- [ ] 담당 이용자 건강·투약 기록 누락 없는지 확인
- [ ] 이상 수치(대시보드 알림) 즉시 보고

---

## 7. 사회복지사 (`social_worker`) 매뉴얼

사회복지사는 소속 지점에서 **이용자 관리**와 **건강·케어 기록**을 담당합니다. 직원 계정 관리·청구 확정·지점 설정은 할 수 없습니다.

### 7-1. 권한 요약

| 기능 | 사회복지사 | 센터장 |
|------|:----------:|:------:|
| 지점 대시보드 조회 | ✅ | ✅ |
| 이용자 등록·수정 | ✅ | ✅ |
| 이용자 퇴소 처리 | ❌ | ✅ |
| 출석 수기 입력 | ❌ | ✅ (요양보호사도 가능) |
| 출석 현황 조회 | ✅ | ✅ |
| 건강 기록 입력 | ✅ | ✅ |
| 청구·정산 | ❌ | ✅ |
| 직원 계정 관리 | ❌ | ✅ |

### 7-2. 일과 개요

```
[오전] 대시보드·출석 현황 확인 → 담당 이용자 건강·특이사항 점검
[낮]   신규 이용자 등록·정보 수정, 케어 관련 기록 입력
[상시] 낙상·사고·특이사항 메모, 보호자 연결 정보 확인
```

### 7-3. 이용자 관리

센터장과 동일한 등록·수정 흐름을 따릅니다. (`/clients`, `/clients/new`, `/clients/:id`)

**사회복지사만의 주의사항**

- **퇴소 처리**는 센터장만 가능합니다. 퇴소가 필요하면 센터장에게 요청하세요.
- 주민등록번호 입력 시 **별도 동의** 체크가 필수입니다. 동의서를 오프라인으로 받은 뒤 시스템에 반영하세요.
- 보호자 연결은 최소 1명 이상 등록하는 것을 권장합니다.

### 7-4. 출석

- **출석 현황**(`/attendance`)은 **조회만** 가능합니다.
- 수기 체크인/아웃은 **요양보호사** 또는 **센터장**이 처리합니다.
- 결석·미입소 이용자를 확인한 뒤 현장에 공유하세요.

### 7-5. 건강 기록

이용자별로 다음 기록을 입력·수정합니다.

1. **건강** 메뉴(`/health`)로 이동합니다.
2. 필요 시 상단 **「급여제공 기록 (케어포 3-1)」** 링크로 식사·간호·목욕 등 **급여제공 전용 화면**으로 이동합니다 (Q524).
3. 이용자를 선택한 뒤 탭으로 기록 유형을 선택합니다.
   - **일일 건강** — 혈압, 체온, 혈당, SpO2 (`VitalsRecordForm`)
   - **투약 기록** — 약품명, 용량, 시간 (`MedicationRecordForm`)
   - **낙상·특이사항** — 이벤트 유형, 내용, 발생 시각 (`IncidentRecordForm`, US-F03)
4. **저장**합니다. **기록 이력** 탭에서 당일 입력을 확인할 수 있습니다.

**활용 팁**

- 비정상 범위 수치는 화면에 강조 표시되며 대시보드 알림에 반영됩니다.
- 투약 기록 시 동일 시간대 중복 입력 경고가 나타나면 내용을 확인하세요.
- 낙상·사고 기록은 즉시 센터장과 공유하는 것을 권장합니다.

### 7-6. 건강 이력·추이

- **`/health/:clientId`**에서 **`HealthTrendChart`**(혈압·체온·혈당·SpO₂ 추이)와 7일·30일 **`FilterChips`** + **표 이력**을 확인합니다 (UXD-48, US-F04).
- API `GET /clients/{id}/health` — **`healthRecords.js`** 가 `items[].recordType`·`payload`를 flat 필드로 파싱합니다 (`4957bd3`).
- **기간 FilterChips**는 UI만 제공 — API **`?days=` 미호출** 시 차트·표가 동일해 보일 수 있습니다 (FAQ **Q165**). Swagger로 `?days=30` 확인하세요.

---

## 8. 보호자 (`guardian`) 매뉴얼

보호자는 **연결된 이용자(어르신)**의 일일 기록을 열람하고, 지점 입구 **QR 스캔**으로 입소·귀가 출석을 처리합니다. 모바일 화면에 최적화되어 있습니다.

### 8-1. 권한 요약

| 기능 | 보호자 |
|------|:------:|
| 연결 이용자 출석·건강·**식사** 요약 열람 | ✅ (식사는 UI만, API `meals[]` 후속 — Q188) |
| QR 셀프 체크인/아웃 | ✅ |
| 이용자 정보 수정 | ❌ |
| 건강 기록 입력 | ❌ |
| 본인부담금 명세 **열람·인쇄** (연결 이용자) | ✅ (열람 전용, US-J02) |
| 청구·수납 처리 | ❌ (센터 직원 권한) |

### 8-2. 로그인·홈 화면 (`/guardian`)

1. 센터에서 발급받은 보호자 계정으로 로그인합니다 (초대 수락 직후에도 동일, §8-5).
2. **보호자 포털**(`/guardian`, `GuardianPortalPage`)이 홈 화면입니다.
3. **연결 이용자** 드롭다운에서 대상을 선택합니다 (`GET /guardian/checkin-targets`).
4. **일일 기록 (US-I02)** 탭 — **`GuardianDailySummary`** — 출석 상태·체크인/아웃 시각·혈압·체온·투약 건수·**식사**(구분+섭취량 Badge, UXD-62)·건강 알림 (`GET /guardian/daily-records`). **식사**는 API `meals[]` 반환 전까지 **「—」** 일 수 있습니다 (Q188).
5. **본인부담금 명세 (US-J02, UXD-55, Q192·Q212·Q220·Q251)** — **「명세·청구」** 탭에 **`CONFIRMED`·`PAID`** 청구만 표시 (`DRAFT` 미노출 — FE·**BE `3def542` 서버 필터**). 월별 목록 · **「더 보기」** 페이지 병합(중복 제거) · 금액은 API 문자열(`"150000"`)도 **원화 표기** (`normalizeAmount`) · 로드 실패 시 **「다시 시도」** · **이용자 전환 시 이전 오류 자동 초기화** (`189a00d`, Q251) · **느린 네트워크 out-of-order 응답 무시** (`bed612c`, Q251).
6. **「연말정산」(G26 / US-L04, Q252·Q254·Q255·Q258)** — **`MedicalExpenseDeductionPanel`** — 연결 이용자 선택 후 **귀속 연도 입력 → 「조회」** — **현금·계좌이체** 수납분만 납입 내역·합계 · **인쇄**·**CSV**·**국세청 엑셀** (`758e590`). 이용자 미선택 시 안내 EmptyState.
7. **「상세」** 클릭 → **`GuardianBillingDetailModal`** — **이용시간대**(`resolveDurationBand` 스냅샷 우선, Q213)·총 급여·공단부담·본인부담률·본인부담금·수납 정보·**「인쇄」** (Q175·Q213).
8. **「알림 이력」** 탭 — **`NotificationHistoryPanel`** — 출석·일일 케어·본인부담금·입금 확인 등 **발송 이력** 조회 (US-J03-h, Q187). 수신 연락처는 표시되지 않습니다.
9. **QR 셀프 체크인** — **「QR 셀프 체크인 (US-E04)」** 링크 → `/guardian/checkin` (토큰 직접 입력, 카메라 **준비 중**, Q109).

> **현재 UI (`b272a7b`)** — **`GuardianDailySummary`**(출석·건강·**식사**, UXD-62) + **명세 CONFIRMED/PAID 필터·더 보기·금액 정규화·이용시간대 스냅샷**(Q212·Q213·Q220) + **`GuardianBillingDetailModal`** 상세·인쇄 **Fixed**. **알림 발송 이력 탭 Fixed**(BNK-22). **식사 실데이터**는 **`daily-records` BE `meals[]` 후속**(Q188). 직원 측 **보호자 서류 3종**(노인학대예방·가정통신문·급여제공기록지)은 **`GuardianDocumentNotifyPanel`** UI **Fixed**(Q217·Q222·Q517) — **납부확인서**는 §4-6·Q221. **CMS·알림톡 실발송**은 **stub/후속** — **`/billing/cms`** (Q207·Q208).

> **알림(J03)** — 출석·청구·**서류 발송** 시 보호자 **이메일**(`channelEmail`, Q204 — **명세·기록지·가정통신문** 3종 템플릿, stub 기본, live SMTP는 DEPLOYMENT §4-8)·휴대폰(V44) 알림톡/SMS **발송 가능**(preference on, Q147·Q148). dev/stub 환경에서는 DB 이력만 생성됩니다. **발송 이력 조회** — **「알림 이력」** 탭 또는 §4-7-2 (Q152·Q187).

### 8-3. 일일 기록·명세 열람

1. 포털에서 **이용자 선택** 드롭다운으로 대상을 고릅니다.
2. **일일 기록** 탭에서 출석·건강·**식사** 요약을 확인합니다 (`GuardianDailySummary`, US-I02·FLOWCHART §9). 식사는 **아침·점심·간식** 구분과 **잘 먹음/보통/적게** Badge로 표시됩니다. 센터가 `/meals`에서 기록을 저장해도 API 연동 전에는 **「—」** 로 보일 수 있습니다 (Q188).
3. **본인부담금 명세** 표에서 월별 본인부담금·상태(**`CONFIRMED`/`PAID`만**, `DRAFT` 미표시)를 확인합니다.
4. 행의 **「상세」** 를 누르면 **`GuardianBillingDetailModal`**이 열립니다 — 이용일수·총 급여비용·공단부담금·본인부담률·본인부담금을 확인합니다 (US-J02, Q132·Q175).
5. **「인쇄」** 를 누르면 브라우저 인쇄 대화상자가 열리고 **명세서 영역만** 출력됩니다 (`window.print()`, `ds-statement-printing`).

> 명세는 **열람 전용**입니다. 수납·CMS·알림톡 발송은 센터 **`/billing`**(직원)에서 처리합니다. 센터용 **명세서 PDF**는 `GET /billing/claims/{id}/statement` (Swagger)를 사용하세요.

### 8-4. QR 셀프 체크인/아웃 (B방식)

보호자(또는 센터 설정 시 이용자 본인)가 **지점 입구 QR**을 스캔하여 출석을 처리합니다.

#### 사전 조건

- 보호자 계정이 이용자와 **연결**되어 있어야 합니다.
- 센터 직원이 당일 유효한 **입소/귀가 QR**을 지점 입구에 게시해 두어야 합니다.

#### 체크인 절차

1. 스마트폰으로 ogada에 **보호자 계정 로그인** 상태를 유지합니다.
2. **QR 체크인**(`/attendance/checkin/qr` 또는 `/guardian/checkin`)으로 이동합니다. *(FE `99f2f3e`: **입소/귀가 `FilterChips`** 선택 후 토큰 입력 — 카메라 스캔 **준비 중**, FAQ Q109)*
3. 지점 입구 QR 코드를 **스캔**하거나 토큰을 **직접 입력**합니다.
   - 카메라 권한 허용이 필요할 수 있습니다.
4. 연결 이용자가 **1명**이면 **이용자 이름**(대표 보호자면 **「(대표)」**)이 자동 표시됩니다.
5. 연결 이용자가 **여러 명**이면 **`QrCheckinTargetsPanel`**(US-E04, Q406)에서 어르신을 고릅니다.
   - **마우스·터치**: 이용자 이름 버튼을 누릅니다. **「대표」** Badge가 붙은 이용자가 대표 보호자 연결 대상입니다.
   - **키보드**: **←→↑↓** 로 이동 · **Home/End** 로 처음/끝 · **Space/Enter** 로 선택합니다.
6. **입소** 또는 **귀가**를 확인하고 제출합니다.
7. 완료 메시지와 기록 시각을 확인합니다.

#### 오류가 날 때

| 메시지·상황 | 조치 |
|------------|------|
| QR 만료 | 센터 직원에게 새 QR 게시 요청 |
| 이미 체크인됨 | 중복 체크인 — 센터 데스크에 문의 |
| 연결 이용자 없음 | 센터에 보호자 연결 등록 요청 |
| 로그인 만료 | 다시 로그인 후 재시도 |

#### 이용자 본인 계정 (`client_user`)

- 일부 센터는 어르신이 직접 스마트폰으로 QR을 스캔하도록 **이용자 본인 계정**을 발급합니다.
- 이 기능은 센터 설정(`allow_client_self_checkin`)이 **켜져 있을 때만** 사용할 수 있습니다.
- 보호자와 동일한 `/guardian` UI를 사용하며, **본인 1명** 출석만 가능합니다.

### 8-5. 보호자 초대 수락 (US-J01, v1.1)

센터가 보호자를 **이메일·링크로 초대**하는 흐름의 수락 단계입니다.

1. 보호자가 초대 링크를 열면 **`/guardian/invitations/<토큰>/accept`** 공개 화면이 표시됩니다 (**로그인 불필요**, FAQ Q139).
2. **이름**·**연락처**(휴대폰)·**비밀번호**를 입력합니다 (`GuardianInvitationAcceptPage`).
3. **초대 수락**을 클릭합니다 — `POST /api/v1/guardian/invitations/{token}/accept`.
4. 성공 시 **`/guardian` 보호자 포털**로 이동합니다 — 연결 이용자·오늘 기록·본인부담금 명세 열람 (US-J02).

> **연락처(V44)** — 수락 시 입력한 휴대폰은 암호화 저장되며, 출석·청구 알림(J03) 수신 번호로 사용됩니다 (Q148). 초대 자체는 **이메일만**(Q145).

---

## 9. 역할별 일일·월말 체크리스트

### 9-1. 센터장 — 일일

- [ ] 지점 선택기가 올바른 지점인지 확인
- [ ] 대시보드 출석·건강 이상 확인
- [ ] 미입소·결석 이용자 후속 조치
- [ ] (필요 시) QR 코드 갱신·게시 확인

### 9-2. 센터장 — 월말

- [ ] 월별 출석 통계·이용자 등급 변경 반영 확인
- [ ] `/billing`에서 청구서 생성·검토
- [ ] 청구 상태 **확정** 및 명세서 PDF 출력
- [ ] 공단 청구내역 엑셀 import·대조
- [ ] 본인부담금 수납 후 **수납완료** 처리

### 9-3. 요양보호사 — 일일

- [ ] 수기 체크인/아웃 완료 여부 확인
- [ ] 건강·투약·특이사항 기록 입력
- [ ] 결석·미입소 이용자 센터장 공유

### 9-4. 사회복지사 — 일일

- [ ] 담당 이용자 출석·건강 상태 확인
- [ ] 건강·투약·특이사항 기록 입력
- [ ] 신규·변경 이용자 정보 등록 (동의서 수령 확인)

### 9-5. 보호자 — 방문 시

- [ ] 보호자 계정 로그인
- [ ] 입소 시: 입구 QR 스캔 → 체크인 완료 확인
- [ ] 귀가 시: 귀가 QR 스캔 → 체크아웃 완료 확인
- [ ] (선택) 포털에서 당일 건강·출석 기록 확인

---

## 10. 개인정보·보안 안내

### 10-1. 주민등록번호

- 공단 급여 청구를 위해 **수집·암호화 저장**됩니다.
- 화면·목록에는 `******-*******`로만 표시됩니다.
- 수집·이용 **별도 동의** 없이는 저장할 수 없습니다.

### 10-2. 공용 PC 사용 시

- **30분 무활동** 시 `SessionTimeoutModal`이 뜨고, 60초 내 **연장**하지 않으면 자동 로그아웃됩니다 (Q112).
- **새로고침** 시 JWT가 메모리에서 사라져 재로그인이 필요합니다 (Q82).
- 업무 종료 후 **로그아웃**하고 브라우저를 닫으세요.
- 주민등록번호 등 민감 정보가 보이는 화면을 방치하지 마세요.

### 10-3. 보호자 계정

- 보호자 계정은 **연결된 이용자 정보·출석**만 열람할 수 있습니다.
- 비밀번호를 타인과 공유하지 마세요.

---

## 11. 자주 묻는 질문 (역할별)

| 질문 | 답변 |
|------|------|
| 지점을 바꿨는데 이용자가 안 보여요 | 지점 선택기에서 올바른 지점을 선택했는지 확인하세요. 이용자는 지점별로 분리됩니다. |
| 사회복지사인데 청구 메뉴가 없어요 | 청구·정산은 센터장(또는 통합 관리자) 권한입니다. |
| QR 스캔이 안 돼요 | QR 유효 시간이 지났을 수 있습니다. 센터 직원에게 새 QR을 요청하세요. |
| 보호자인데 이용자가 목록에 없어요 | 센터에 보호자–이용자 **연결 등록**을 요청하세요. |
| 공단 청구는 ogada에서 하나요? | **아니요.** 공단 급여 청구는 장기요양정보시스템(롱텀)에서 합니다. ogada는 내부 계산·명세서·엑셀 대조를 지원합니다. |
| 대시보드 숫자가 실제와 달라요 | 위젯·건강 알림 API(Q85). 출석률 `%` 과소 표기 가능(Q118) |
| 건강 추이 기간이 안 바뀌어요 | `/health/:clientId` — **차트+표 Fixed**(Q119). **FilterChips `?days=` 갭**(Q165) |
| 건강·투약·사고 저장이 실패해요 | **Q154 Fixed** — 필수 항목·세션 확인. 비정상 수치 **노란 경고는 저장 차단 아님**(Q155). **자유 메모(notes)** 는 Swagger |
| 지점 등록이 「이미 존재」 오류 | 대소문자만 다른 지점명 — V40 UK. FAQ **Q146** |
| 보호자 초대·수락이 실패해요 | 발송·수락 API 미구현 — `POST /users`+`/guardians` 우회 (Q123·Q139) |
| 비밀번호 변경 모달만 뜨고 저장 안 돼요 | **`POST /auth/change-password` Fixed** (Q122) — 8자 이상·기존과 다른 비밀번호 입력 |
| 설정 감사·백업 탭이 비어요 | **조회 API Fixed**(Q121) — 수동 백업·감사 필터 API 갭 잔존 |
| 폼 필드 아래 빨간 오류가 보여요 | 서버 **`fieldErrors`** 매핑 정상 (Q190) — 입력값 수정 후 재시도 |
| 결석 버튼이 없어요 | 배포 HEAD **`0c69060`+** 확인 (Q609). **`status=null`** 미처리 행이면 버튼 표시 — 그래도 없으면 FAQ **Q94** |
| 지점 선택기에 UUID만 보여요 | `/dashboard`·`/attendance`·`/guardians`는 지점명 표시(Q89). `/billing` 등 일부 화면은 UUID 폴백 |
| 셀프 체크인 스위치가 저장 안 돼요 | `/settings` Switch UI만(Q116). `PATCH /organization/settings` Swagger 사용 |
| 청구 목록 월 필터가 안 맞아요 | 프론트 `yearMonth` 쿼리가 백엔드에서 무시됩니다 (FAQ Q83). |
| 출석 통계 숫자가 비어 있어요 | FE/BE **contract 불일치** (FAQ **Q106·Q613**). Swagger로 `GET /attendance/stats/monthly?branchId=&from=&to=` 확인. 당일은 **`/attendance`** (Q609). |
| QR·체크인이 API 오류로 실패해요 | **출석 roster ✅** (Q609). QR payload·이미지 갭은 FAQ **Q109·Q590** · 교통편은 **Q96** |
| 세션 만료 경고 모달이 떠요 | **SessionTimeoutProvider** — 60초 전 경고, **연장** 또는 재로그인 (Q112). |
| 공단 엑셀은 어떤 브라우저로 받나요? | **Chrome/Edge** 필수. `GET /billing/imports/nhis/guidance` (FAQ Q111). |
| 이용자 본인 계정·사진이 저장 안 돼요 | 등록 UI만 있고 API 미연동 (FAQ Q113). |
| 비밀번호 찾기가 없어요 | 로그인 UI 미구현 (FAQ Q90). |

상세 FAQ는 [`docs/ops/FAQ.md`](ops/FAQ.md)를 참고하세요.

---

## 12. 관련 문서

| 문서 | 내용 |
|------|------|
| `docs/planning/REQUIREMENTS.md` | 기능·역할·정책 전체 명세 |
| `docs/technical/API_SPEC.md` | REST API 상세 (개발·연동 참고) |
| `docs/planning/FLOWCHART.md` | 화면·업무 흐름도 |
| `docs/planning/USER_STORIES.md` | 역할별 사용자 스토리·인수 조건 |
| `docs/ops/ADMIN_GUIDE.md` | 플랫폼·시스템 관리자 가이드 |
| `docs/ops/DEPLOYMENT_GUIDE.md` | 배포·운영 |
| `docs/ops/FAQ.md` | 자주 묻는 질문 |
| `docs/product/DESIGN_SYSTEM.md` | UI 토큰·컴포넌트·접근성 (개발·UX 참고) |
| `docs/ops/CHANGELOG.md` | 버전별 변경 이력 |

---

## 13. 변경 이력

| 날짜 | 변경 내용 |
|------|----------|
| 2026-06-21 | **301차** — §1-3·§1-5·§4-6·§5-3 **G-BILLING-DEPOSIT-ORDER-GUARD**·**G-STAFF 출근방식**·**Q614**·`a6eb8b7`·`5fd468b` |
| 2026-06-21 | **299차** — §1-3·§1-5·§4-4 **G-ATTENDANCE-STATS contract**·**Q613**·baseline carry |
| 2026-06-21 | **298차** — §1-3·§1-5·§3-1·§5-3 **G-STAFF-WORK-ATTENDANCE full-stack**·**Q612**·`560057f`·`53d65a0` |
| 2026-06-21 | **297차** — §1-3·§5-3 **UXD-151 mobile capture CSS**·**Q611**·`61e1970`·`9812ac4` |
| 2026-06-21 | **296차** — §1-3·§1-5·§4-4 **G-ATTENDANCE-ROSTER-STATUS FE wire full-stack**·**Q609·Q610**·`61e1970`·`8383f8d` |
| 2026-06-21 | **295차** — §1-3·§1-5·§4-4 **G-ATTENDANCE-ROSTER-STATUS**·**Q609**·**Q94 closure**·`61e1970`·`3bffb17` |
| 2026-06-21 | **294차** — §1-3·§1-5·§2-2·§4-2·§5-3 **mobile HR capture**·**duplicate SMS guard**·**8-12 print cleanup**·**Q607–Q608**·`56cb5d9`·`6bde24a` |
| 2026-06-21 | **293차** — §1-3·§1-5·§2-2·§4-2·§5-3·§5-26 **V168 overdue integrity**·**UXD-150 a11y**·**repository API wire**·**Q605–Q606**·`20485f1`·`751c593` |
| 2026-06-21 | **292차** — §1-3·§1-5·§5-3 **G-STAFF-DOCUMENT-REPOSITORY**·**overdue SMS auto-record guard**·**Q604·Q602 deepen**·`b583c11`·`03d0d43` |
| 2026-06-21 | **290차** — §1-3·§1-5·§2-2·§4-2·§5-2 **G21 dashboard NHIS gap**·**G15 Kakao quota widget**·**Q594–Q597**·`0c9518a`·`580a86b` |
| 2026-06-21 | **288차** — §1-3·§2-2·§5-10 **G-BILLING appliedFilters FE wire**·**UXD-148 a11y**·**Q580 feature-scoped blockers**·**Q588**·`7b99313`·`e2f1246` |
| 2026-06-21 | **287차** — §1-3·§1-5·§2-2·§5-10 **G-BILLING appliedFilters echo**·**Q580 snake_case blocker**·**Q587**·`14935a3`·`33e9e1a` |
| 2026-06-21 | **286차** — §1-3·§1-5·§2-2·§5-10 **G-BILLING report FE wire**·**invalid month guard**·**Q585 closure·Q586**·`375fb9d`·`e38ccfd` |
| 2026-06-21 | **285차** — §1-3·§1-5·§2-2·§5-3·§5-10 **G-STAFF-LEAVE-STATUS full-stack**·**G-BILLING deposit half-month·receipt dual-basis**·**Q584·Q585**·`b96d038`·`1a614c9` |
| 2026-06-21 | **284차** — §1-3·§5-3 **G-STAFF-LEAVE-STATUS ON_LEAVE**·**live E2E placeholder token bootstrap**·**Q584**·`68d4457`·`82a542c` |
| 2026-06-21 | **283차** — §1-3·§2-2·§4-6-1 **NHIS header normalize**·**live E2E stale token recovery**·**Q582–Q583**·`2edbdc4`·`b60c622` |
| 2026-06-21 | **282차** — §1-3·§2-2·§4-4·§4-6·§4-7-0 **G-BANK invalid rowNumbers**·**UXD-146**·**출석 Must 갭**·**Q579–Q581**·`6ed7cd4`·`9105332` |
| 2026-06-21 | **281차** — §1-3·§4-6 **G-BANK-EXCEL-8 full-stack**·**Q572·Q576**·`7d29a38`·`a18b30e` |
| 2026-06-21 | **280차** — §1-3·§4-6·§4-7-0 **G-STAFF-NHIS-EXCEL-IMPORT full-stack**·**bulk import rowNumbers**·**Q576–Q577**·`e3b74a0`·`4315ee2` |
| 2026-06-21 | **278차** — §1-3·§1-5·§2-2·§4-2 **baseline `80b9619`/`d723d5a`**·**G32 경로 정정**·**청구 생성 가드 StatCard (Q571)**·Must 빠른 점검 §1-5 |
| 2026-06-21 | **277차** — §1-3·§2-2·§3-3·§4-2 **G14 NHIS 10-field care plan form**·**Q557**·`07a03c0`·`08a8b9f` |
| 2026-06-21 | **274차** — §1-3·§2-2·§4-7·§5-3·§5-8 **V160 ogada_platform_admin**·**Kakao per-API quota**·**staff account request workflow**·**Q554 갱신·Q555~Q556**·`3023c9e`·`380be3c` |
| 2026-06-21 | **273차** — §1-3·§2-2·§5-5·§5-8 **v1.3-A Kakao API status+usage probe**·**suggest route-preview embed**·**TransportKakaoApiStatusPanel**·**Q554**·`e2b764b`·`ba74bb5` |
| 2026-06-21 | **272차** — §1-3·§2-2·§3-1·§5-8 **v1.3-A transport preview cache+roster ETA**·**G30/G39 nav label**·**Q553**·`acc5933` |
| 2026-06-21 | **270차** — §1-3·§2-2·§4-2·§5-3 **FAQ21823 renewal record+due alerts**·**live E2E readiness centralization**·**Q547~Q549**·`bfad37d`·`16afd4c` |
| 2026-06-21 | **269차** — §1-3·§2-2·§5-3 **FAQ21823 clauses checklist+template modal**·**G21 not-applicable live E2E**·**Q546**·`091c372`·`1b6d2b1` |
| 2026-06-21 | **268차** — §1-3·§2-2·§4-2·§5-3·§5-10-1 **V159 identifier CHECK**·**UXD-141 FAQ21823 a11y**·**Q543~Q545**·`1139e79`·`202c1fe` |
| 2026-06-21 | **267차** — §1-3·§2-2·§4-2·§5-3 **US-R03 FAQ21823 list+dashboard renewal widgets**·**Q540 갱신**·`10585b9`·`f31c346` |
| 2026-06-20 | **266차** — §1-3·§2-2·§5-3 **US-R03 FAQ21823 employment contract renewal panel**·**live E2E unsupported branch seed**·**Q540·Q541**·`7a9d7a5`·`f62402f` |
| 2026-06-20 | **265차** — §1-3·§2-2·§4-7-3·§5-10-1 **J03 guardian document quiet-hours**·**G-CASH-RECEIPT-LOG FE identifier pre-submit validation**·**Q537 갱신·Q539**·`7e4c07e`·`0038846` |
| 2026-06-20 | **264차** — §1-3·§2-2·§4-6-0-1·§5-10-1·§5-10-2 **G-CASH-RECEIPT-LOG numeric-only identifier**·**UXD-140 a11y**·**Q537 갱신·Q538**·`4da0ca8`·`501fedc` |
| 2026-06-20 | **263차** — §1-3·§2-2·§5-10-1 **G-CASH-RECEIPT-LOG identifier normalize+validation**·**pending load error guard**·**Q537**·`298bcdf`·`35d1560`·`99b795a` |
| 2026-06-20 | **262차** — §1-3·§2-2·§4-6-0-1·§5-10-1·§5-10-2 **G26 yearBasis+NTS CSV**·**G-7-1 Excel export**·**UXD-139 a11y**·**Q534~Q536**·`ceeaeb9`·`19ed7f3`·`e454d3b`·`58d6694` |
| 2026-06-20 | **261차** — §1-3·§2-2·§5-10-1 **G-CASH-RECEIPT-LOG 4-계층 closure**·**HQ pending**·**prior-year advisory**·**Q533**·`58ff35e`·`8aebe55` |
| 2026-06-20 | **260차** — §1-3·§2-2·§4-2·§5-10-1 **G-CASH-RECEIPT-LOG dashboard due-gate**·**pending issuance API**·**Q532**·`ab5708b`·`221458e` |
| 2026-06-20 | **259차** — §1-3·§2-2·§5-10·§5-10-1 **G-CASH-RECEIPT-LOG payment bridge**·**Q531 partial**·`a17f148`·`8e6e0c6` |
| 2026-06-20 | **258차** — §1-3·§2-2·§3-1·§5-10-1 **G-CASH-RECEIPT-LOG full-stack**·**V158**·**Q530·Q531**·`4432558`·`cfc4b04`·`f79a19e` |
| 2026-06-19 | **257차** — §1-3·§2-2·§5-11 **G21 split-view dual NHIS**·**UXD-138 a11y**·**G-CASH-RECEIPT gap**·**Q526~Q530**·`7848b0f`·`d354a0e` |
| 2026-06-19 | **256차** — §1-3·§2-2·§4-5·§6-4 **케어포 3-1 `CareProvisionSegmentNav`**·G32 **probe·stale runtime guard**·**Q524~Q525**·`45d95ea`·`1d5747d` |
| 2026-06-19 | **255차** — §1-3·§2-2·§5-9 G32 **FAQ21797 live E2E harness·PATCH attendeeOpinions**·**Q522~Q523**·`510d2f3`·`3f871d7` |
| 2026-06-19 | **254차** — §1-3·§2-2·§5-9 G32 **V157·중복 참석자 차단**·**Q519~Q521**·`eed39ab`·`c7fb69a` |
| 2026-06-19 | **253차** — §1-3·§2-2·§4-2·§5-9 G32 **dashboard attendee-opinion gap widget**·**Q518**·`b9e0947`·`e55ae96` |
| 2026-06-20 | **252차** — §1-3·§2-2·§4-7-3·§5-9 G32 **FAQ21797 attendee opinions**·G2 **guardian document 3-type panel**·**Q515~Q517**·`5222a8f`·`b272a7b`·`d1149a5` |
| 2026-06-19 | **251차** — §1-3·§2-2·§5-11·§5-25·§5-28 G39 **FAQ21817 7-day SLA**·**RFID equivalence**·health **G21 branch blocker**·FE **billing gate**·**Q511~Q514**·`bc754a0`·`c3b6a5c`·`b881883` |
| 2026-06-19 | **250차** — §1-3·§2-2·§5-11·§5-16 G21 **cross-branch seed scope**·QA-B147 **batch-confirm loading**·UXD-136/137 **L03 edit a11y**·**Q507~Q510**·`02a2eb8`·`f86c76c` |
| 2026-06-19 | **249차** — §1-3·§2-2·§5-11 G21 **probe branch-missing blocker**·UXD-147 **batch-confirm NHIS ack a11y**·**Q505~Q506**·`7898aa5`·`0002943` |
| 2026-06-19 | **248차** — §1-3·§2-2·§5-3 G21 **paired PLAN/BILLING seed**·G41 **filter-year load guard**·UXD-135 **modal a11y**·**Q500~Q504**·`191703f`·`cefb7c7` |
| 2026-06-19 | **247차** — §1-3·§2-2·§5-11 G21 **seed readiness**·**liveG21Describe gate**·**Q495~Q497**·`c0403b0`·`d61ab5e` |
| 2026-06-19 | **246차** — §1-3·§2-2·§5-11·§5-14 live E2E **health/probe alignment**·UXD-134 **NHIS·G41 a11y**·**Q491~Q494**·`8fe1ccd`·`cf85003` |
| 2026-06-19 | **245차** — §1-3·§2-2·§5-3·§5-14 G41 **filter-year inline error**·live E2E **probe default-credentials blocker**·**Q489·Q490**·`f932fd3`·`28e5525` |
| 2026-06-19 | **244차** — §1-3·§2-2·§5-3·§5-14 G41 **reference-year input guard**·**Q489**·`b73e5f4`·`f26e075` |
| 2026-06-18 | **243차** — §1-3·§2-2·§5-11 G21 **NHIS comparison panel+per-client drill-down FE closure**·live E2E **NHIS import seed**·**Q479·Q484 갱신·Q486~Q488**·`b73e5f4`·`797c529` |
| 2026-06-18 | **242차** — §1-3·§2-2·§4-6-0-1·§5-11 G21 **NHIS summary deepen+Modal StatCard FE wire**·UXD-133 **print a11y**·**Q479·Q481 갱신·Q483~Q485**·`39fa41a`·`68a4e35` |
| 2026-06-18 | **241차** — §1-3·§2-2·§5-11 G21 **confirm-readiness NHIS summary embed**·**RFID no-diff success alert**·**Q479 갱신·Q481~Q482**·`8a8c5b3`·`f232285` |
| 2026-06-18 | **240차** — §1-3·§2-2·§5-11 G21 **visit NHIS comparison API**·**unassigned batch-confirm gate**·**VisitsContextNav URL sync**·**RFID diff normalize deepen**·**Q477·Q456 갱신·Q479~Q480**·`03a052a`·`570912e`·`3a27303`·`5f710e3` |
| 2026-06-18 | **239차** — §1-3·§2-2·§4-6-0-1·§5-11 G21 **per-kind readiness deepen+FE StatCard**·G-7-1 **unpaid all-print label**·**Q474·Q475 갱신·Q477~Q478**·`f26abb0`·`f9ed97d`·`f5639df` |
| 2026-06-19 | **238차** — §1-3·§2-2·§3-1·§4-6·§5-8-0-1·§5-11 G21 **readiness split**·G-7-1 **print bundle**·UXD-132 **a11y**·**Q474~Q476**·`6aeafe7`·`50d330d`·`f8321c7` |
| 2026-06-18 | **237차** — §1-3·§2-2·§5-8-0-1 G15 **service log direction API**·live E2E **probe·guardian align**·**Q471~Q473**·`72124f7`·`8cf09d8`·`94c65e2` |
| 2026-06-18 | **236차** — §1-3·§2-2·§5-8-0-1 G15 **별지 제22호 form completion·branch contact export·pickupAddress API**·**Q468~Q470**·`07be394`·`b1a16ff`·`e358f2d` |
| 2026-06-18 | **235차** — §1-3·§2-2·§5-8-0-1 G15 **per-stop form·print column parity**·V155 **waypoint test deepen**·**Q466~Q467**·`7de5a6f`·`a179256` |
| 2026-06-18 | **234차** — §1-3·§2-2·§4-2·§5-3·§5-8·§5-8-0-1·§5-14 V155 **waypoint**·G41 **PDF 8-7·dashboard widget·8-7-1 export**·G15 **print pickup**·**Q458~Q465**·`64c4c80`·`caa215f` |
| 2026-06-18 | **232차** — §1-3·§2-2·§5-11·§6-3-1 G21 **RFID diff rendering**·visit check-in **supervisory role**·live E2E **HOME_VISIT seed**·**Q455~Q457**·`4a112fe`·`78cfb8a`·`9e050b1` |
| 2026-06-18 | **231차** — §1-3·§2-2·§5-11·§5-24 G21 **RFID compare UI**·visit check-in **assigned-user guard**·L02_M07 **body restraint normalization**·**Q452·Q453·Q454**·`27c9de3`·`0db1e68`·`4a47675` |
| 2026-06-18 | **230차** — §1-3·§2-2·§5-8-0-1·§5-11 UXD-130 **driver signature fieldset**·live E2E **guardian suite gate**·G21 **RFID compare API**·**Q450~Q452**·`bfe0283`·`7424c30`·`eeac205` |
| 2026-06-18 | **229차** — §1-3·§2-2·§5-27 L02_M13 **create client normalization**·live E2E **bootstrap error blockers**·**Q448·Q449**·`d7f1a9a`·`1c8f236` |
| 2026-06-18 | **228차** — §1-3·§5-8-0·§5-8-0-1 G15 **driver signature**·**service-log legal guide**·**Q445·Q446·Q447**·`bc3a35c`·`f51e365` |
| 2026-06-18 | **227차** — §1-3·§5-3·§5-8-0-1 G15 **server legal field guard**·staff **health checkup HR file hub wire**·**Q443·Q444**·`ac1d43f`·`b6ce301` |
| 2026-06-18 | **226차** — §1-3·§5-3·§5-8-0-1·§5-27 G15 **legal field guard**·**duplicate rejection**·L02_M13 **malformed API**·UXD-129 **a11y**·**Q439~Q442**·`b4644e8`·`52e3340` |
| 2026-06-18 | **225차** — §1-3·§5-3 staff **new-hire health checkup document window**·**Q435**·`8e6310a` |
| 2026-06-18 | **224차** — §1-3·§5-8 transport **roster planned pickup hub**·**Q433**·`e35efb2`·`101aaee` |
| 2026-06-18 | **223차** — §1-3·§3-2 QA-B131 **`test:live-e2e` script path**·**DatePicker keyboard a11y**·V153·G15 service log harness·**Q429~Q432**·`8882d9f`·`4c5d3bc` |
| 2026-06-17 | **222차** — §1-3·§4-3 G30 **`MonitoringEvidenceContextPanel`**·**Q391·Q428**·`7d2cb4a`·`09df8c7` |
| 2026-06-17 | **221차** — §1-3·§5-8-0·§5-8-0-1 G15 **compliance→일지 hub**·**Q426·Q427**·`b93e098`·`b2c09e1`·`844227a` |
| 2026-06-17 | **220차** — §1-3 live E2E **nested bootstrap payload**·**Q425**·`fc916db` |
| 2026-06-18 | **219차** — §1-3·§2-2·§3-2 **`/actuator/healthz`**·DateInput/TimeInput **QA-B127**·**`viewAnchor` 생년월일**·ETA chip Fixed·Q413·Q422·`2157df5`·`ab4de83` |
| 2026-06-18 | **218차** — §1-3·§5-8 배차 **compact dispatch layout**·**embedded settings validation**·V152 **Fixed**·Q424·`dd2fa2c`·`96db8bf` |
| 2026-06-17 | **217차** — §1-3·§5-8 V152 **퇴소·비활성 이용자 배차 가드**·staff bootstrap guardian tokens·Q423·`73cffc5` |
| 2026-06-18 | **216차** — §1-3·§2-2·§3-2·§5-8 배차 **경유지 FE closure**·**DatePicker+TimeInput**·ETA time chip·Q421·Q422·`bf73c4c`·`ea5d896` |
| 2026-06-17 | **215차** — §1-3·§2-2·§5-8 배차 **임의 주소 경유지(WAYPOINT)**·Q421·`de3474d`·FE WT |
| 2026-06-18 | **214차** — §1-3·§2-2·§4-3·§5-8 배차 **계획 출발·정차 ETA**·split-view 세로 배치·`MaskedPhone` a11y·Q418·Q420·`0e46b37`·`fde098f` |
| 2026-06-18 | **213차** — §1-3·§4-3 이용자 목록·상세 **연락처(`phoneMasked`)** 열·검색·Q417·`0baabe9`·`f0e52b8` |
| 2026-06-18 | **211차** — §1-3·§2-2·§5-8-3 G15 outing live E2E·actuator health probe deepen·Q240·Q413·`3a0110f`·`b48252a`·`30243f7` |
| 2026-06-18 | **210차** — §1-3·§2-2·§5-8-3·§5-36 L02/L03 CareNursingParityPanel·outing report a11y·live E2E deepen·Q240·Q412·`140bf92`·`5533ef5`·`9641ab1` |
| 2026-06-18 | **209차** — §1-3·§2-2·§5-8·§5-8-0-1 G15 audit trail read API full stack·live E2E cross-tenant bootstrap·Q411·Q409·`5994d15`·`3cc5a08`·`2d6c063` |
| 2026-06-17 | **208차** — §1-3·§2-2·§5-8·§5-8-0-1·§5-8-0-2 G15 일지 감사·보관 UX·월간 리포트 2-7/2-8·Q410·Q411·`aa42b9c`·`6a18dfd` |
| 2026-06-17 | **207차** — §1-3 QA-B95 bootstrap client fallback·guardian token reuse·Q409·`c13800c`·`af4d7f8` |
| 2026-06-17 | **206차** — §1-3·§2-2·§5-8·§5-8-0 G15 service log API full stack·V148·Q407·`aaaeb10`·`7a4b310` |
| 2026-06-17 | **189차** — §1-3 baseline sync·G26 pilot E2E·live E2E prod guard·Q384·`aa6816a`·`14d210c` |
| 2026-06-17 | **204차** — §1-3 QA-B95 staff clientId·probe·login fallback·pilot E2E stabilize·`d8d51a7`·`6f2a4eb` |
| 2026-06-16 | **203차** — §1-3 QA-B95 live E2E deepen·V147 guardian trigger·`b1a6aff`·`4e99ae1` |
| 2026-06-17 | **202차** — §1-3·§2-2·§5-8 QA-B116 direction-aware runs·TransportDeleteRunModal FE closure·Q399·Q403 갱신·`1d1a71f`·`45bd923` |
| 2026-06-16 | **201차** — §1-3·§2-2·§5-8 QA-B117 DELETE draft runs·geocode scoring·US-T02 map pin a11y·Q403~Q404·`1d1a71f`·`10489a7` |
| 2026-06-17 | **200차** — §1-3·§2-2·§4-3·§5-8·§5-8-3 US-T02 branch waypoints·DROPOFF·desired times·defaultDriverName·Q399~Q402·`114411f`·`d3bef42` |
| 2026-06-17 | **199차** — §1-3·§2-2·§3-1·§5-8·§5-8-0 BNK-288 transport compliance split·SEC-005 tab session·roster guardianContact·Q396~Q398·`35e03ef`·`84e75ec` |
| 2026-06-17 | **198차** — §1-3·§2-2·§3-1·§5-8 QA-B114 Kakao map instance refactor·SideNav L02_M14 dedup·Q370·Q394·Q395·`7ac0a46`·`5ebaade` |
| 2026-06-17 | **197차** — §1-3·§2-2·§5-8 QA-B113 Kakao Maps JS SDK preview·QA-B95 role-mismatch seed guard·Q370·Q393·Q394·`7ac0a46`·`b000d92` |
| 2026-06-17 | **196차** — §1-3 QA-B95 guardian bootstrap·live API routing E2E·Q393·`ec142db`·`b3bd0cc` |
| 2026-06-17 | **195차** — §1-3·§4-2·§4-6-1·§5-10·§5-36 L02 nursing BE pilot E2E·G26/G24b monitoring labels·G7 year-coverage message·Q391~Q392·`2ba2761`·`d499130` |
| 2026-06-17 | **194차** — §1-3·§2-2·§5-36 live E2E bootstrap fix·CareNursingServiceReportNav sub-nav·Q389~Q390·`304bb2a`·`8ed937c` |
| 2026-06-17 | **193차** — §1-3·§3-1·§5-11·§5-22·§5-36 L02 care-scoped nursing reports·G21 split-view summary+follow-up·Q386~Q388·`002e3eb`·`58ee122` |
| 2026-06-17 | **187차** — §1-3·§2-2·§3-1·§5-10 G26 statistics dashboard FE full stack·Q379·Q380·Q381·`3481eb8`·`31544cf` |
| 2026-06-16 | **186차** — §1-3·§5-10 G26 dual statistics E2E harness·Q379·Q380·`92ae60b` |
| 2026-06-16 | **185차** — §1-3·§5-10 G26 branch billing reports·Q379·Q380·`903f462`·`6d10e0d` |
| 2026-06-16 | **184차** — §1-3·§3-1·§3-2·§5-11 G21 RFID split-view·L02 care nav cross-links·L02/G21 a11y·Q377·Q378·`b38c6f7`·`6759bf6` |
| 2026-06-16 | **183차** — §1-3·§3-1·§5-11·§6-3-1 G21 claim reflection FE·Q376·`b38c6f7`·`25ca88e` |
| 2026-06-16 | **182차** — §1-3·§3-1·§5-11·§5-33~§5-35 L02_M11/M12 FE·L02_M16·G21 claim reflection·Q373~Q376·`6da49aa`·`8b804fc` |
| 2026-06-16 | **181차** — §1-3·§3-1·§5-29~§5-34 L02_M17/M06 report FE·L02_M11/M12 BE·Q371~Q374·`2cf0908`·`40684a9` |
| 2026-06-16 | **180차** — §1-3·§3-1·§5-8·§5-31·§5-32 L02_M17/M06 report BE·transport a11y·Q371·Q372·`9cc0c1d`·`1daeda7` |
| 2026-06-16 | **179차** — §1-3·§3-1·§5-8·§5-29·§5-30 L02_M04/M05 report FE·print·route-preview·Q369·Q370·`3eeac92`·`46971e1` |
| 2026-06-16 | **178차** — §1-3·§3-1·§4-3·§5-27·§5-28·§6-1 L02_M13·L02_M15·G30 phone panel·Q366·Q368·Q365·`c655743`·`3549896`·`9ad8346` |
| 2026-06-15 | **177차** — §1-3·§3-1·§5-27·§6-1 L02_M13 BE·V139/V140·J03 blockers·L02 a11y·Q366~Q367·`81a2223`·`15b09df`·1437/1441·1284/1284 |
| 2026-06-16 | **176차** — §1-3·§3-1·§4-6-0·§5-25·§5-26·§6-1 L02_M01/M03·G-7-1-4CHANNEL·Q362~Q365·`344a28b`·`1fd1434`·1432/1432·1272/1272 |
| 2026-06-16 | **175차** — §1-3·§3-1·§5-24·§6-1 L02_M07 FE·V132·health databaseStatusDetail·Q361·Q360·`8b7e476`·`10f32c4`·1393/1393·1231/1231 |
| 2026-06-16 | **174차** — §1-3·§5-23·§5-24 L02_M02 FE·L02_M07 BE·health ping·Q359·Q361·`df14e15`·`95e7e96`·1381/1381·1228/1228 |
| 2026-06-15 | **173차** — §1-3·§5-23 L02_M02 BE API·G19/G30/G39 a11y·Q359·Q360·`fd42b7e`·`5f17beb`·1367/1367·1214/1214 |
| 2026-06-15 | **172차** — §1-3·§4-3·§5-9 G39 dispatch·G30 evidence window·Q358·Q320·`4d1a4f2`·`73094f9`·`73df04d`·1357/1357·1201/1201 |
| 2026-06-15 | **171차** — §1-3·§4-2·§4-3·§5-3 G24b status·G19 discovery·Q357·`b5af5fa`·`9afa30e`·`41d8de5`·1355/1355·1197/1197 |
| 2026-06-15 | **170차** — §1-3·§4-2·§4-3·§5-3 G24b dashboard·G41 V129·7-5 alias·Q356·Q355·`ca0b627`·`b1c92e1`·`3cbe582`·`1e21b20`·1347/1347·1192/1192 |
| 2026-06-15 | **169차** — §1-3·§2-2·§4-3·§5-22 G24b compliance·a11y·L03 notes·Q355·`8989bf4`·`c97706b`·`98002d4`·1325/1327·1182/1182 |
| 2026-06-15 | **168차** — §1-3·§2-2·§3-3·§4-3 G24b 8-area·QA-B94 openedOn·Q354·Q353·`49fbf67`·`45fb6d9`·1323/1323·1173/1173 |
| 2026-06-15 | **167차** — §1-3·§2-2·§4-3 G-ONBOARD FE wire·Q353·`79d593c`·`4c1fd43`·1320/1320·1171/1171 |
| 2026-06-15 | **166차** — §1-3·§3-1·§5-20 US-UX-05 sessionStorage·L03 date window·Q331·Q352·`3845f0c`·`6b0238a`·`548f670`·1315/1316·1162/1162 |
| 2026-06-15 | **165차** — §1-3·§5-15·§5-20~§5-22·§6-1 L03_M01/M06/M07/M09/M10/M15 FE·Q348~Q351·`12591d4`·`671a704`·1315/1315·246/246 |
| 2026-06-15 | **164차** — §1-3·§5-8·§5-14·§5-20 v1.3-B FE wire·L03_M01 BE·Q347·Q348·`9bd1660`·`edfba7f`·1274/1274·1131/1131 |
| 2026-06-14 | **163차** — §1-3·§5-8·§5-11·§5-17 G21 기간 가드·v1.3-B suggest API·L03_M14 Field help·Q330·Q347·`230659a`·`c865d2b`·1267/1267·1121/1121 |
| 2026-06-14 | **162차** — §1-3·§3-1·§5-18·§5-19·§6-1 L03_M13 구강상태·L03_M04 응급상황 FE wire·Q344~Q346·`090b2d7`·`97108f2`·1261/1263·1115/1115 |
| 2026-06-14 | **161차** — §1-3·§3-1·§5-16·§5-17·§6-1 L03_M14 체중 기록 FE wire·미래일자 가드·Q343~Q344·`63cb193`·`962858b`·1228/1228 |
| 2026-06-14 | **159차** — §1-3·§3-1·§5-15·§6-1 G-NURSING-PRESSURE-ULCER 욕창 케어 lifecycle·Q336~Q339·`24a1c5c`·`024e720`·1073/1192 |
| 2026-06-14 | **158차** — §1-3·§2-2·§5-9 G17b 인지활동형 미제공 사유(프로그램·기능회복)·Q333~Q335·`3bd6a43`·`487416d`·1060/1164 |
| 2026-06-14 | **157차** — §1-3·§2-2·§3-1·§5-3·§5-11 G21 batch-confirm·G42 익명함 intake·US-UX-05 SideNav·Q330~Q332·`ba7d84f`·`c26cfa7`·1060/1160 |
| 2026-06-14 | **154차** — §1-3·§2-2·§4-6 J03 quiet-hours billing UI·7-5 provider deepen·Q329·`9a4ab8e`·`111f056`·1030/1141 |
| 2026-06-14 | **153차** — §1-3·§4-6 G2/7-5 V110·US-L06 a11y·Q328·`16a0734`·`51f2505`·1024/1133 |
| 2026-06-14 | **152차** — §1-3·§3-1·§4-6 G2/7-5 easy payment·전월 가드·Q326·Q327·`b893e97`·`bebd874`·1023/1126 |
| 2026-06-14 | **151차** — §1-3·§2-2·§5-3·§5-14 G41b compliance API wire·V107·Q321·Q325·`0f11158`·`45a724a`·246/1110 |
| 2026-06-14 | **148차** — §1-3·§2-2·§4-3·§5-3·§5-9 G30 checklist·G34-QUAL panel·US-S02 POST·Q320·Q319·Q294·`b1dfd34`·`574bd08`·989/1088 |
| 2026-06-14 | **147차** — §1-3·§2-2·§5-3·§5-5·§5-9 G34-QUAL BE guard·UXD-97 J03 a11y·Q318·Q319·`726b3de`·`76b5ff0`·975/1084 |
| 2026-06-14 | **146차** — §1-3·§2-2·§5-3·§5-5·§5-9 J03 readiness UI·8-12 pagination·G34-QUAL·Q318·Q319·`fffd355`·`443efca`·968/1081 |
| 2026-06-14 | **145차** — §1-3·§2-2·§5-3 8-12 BE CSV·G42 결재·사후관리·Q309·Q315·Q316·`bc927f7`·`6012044`·`488f547`·960/1071 |
| 2026-06-13 | **144차** — §1-3·§2-2·§3-1·§4-3·§5-3 G30 모니터링·8-12 aggregated·export 7종·Q308·Q314·Q315·`5692662`·`07956f5`·935/1051 |
| 2026-06-13 | **142차** — §1-3·§2-2·§5-4 G9-COG import gate·V99·apply-nhis-seeds·G9-COPAY-NAMING·Q260·Q311·Q313·`8bb6583`·`a5c2736`·902/1022 |
| 2026-06-13 | **141차** — §1-3·§2-2·§3-3·§4-6·§5-4 G9-COG·FAQ21824·G-7x-1 YearMonth·Q311·Q312·`2efc557`·`6ef671b`·894/1017 |
| 2026-06-13 | **140차** — §1-3·§2-2·§3-1·§4-6·§5-3·§5-9 G42 pending-approval·G-7x-1-guard·US-T14 익명함·Q309·Q310·`6f6094d`·`338c014`·886/1009 |
| 2026-06-13 | **139차** — §1-3·§2-2·§3-1·§5-3·§5-9 US-R02 직원현황 리포트·G34b import-draft API·Q308·`8487667`·`02cbd05`·882/1001 |
| 2026-06-13 | **138차** — §1-3·§2-2·§3-1·§5-3·§5-9·§5-11 G42 고충상담·G34b 전월 복제·G21 check-in guard·Q305·Q306·Q307·`b0a9e06`·872/989 |
| 2026-06-13 | **137차** — §1-3·§2-2·§5-9 G34b 업무수행일지 불러오기·G21 assignedUser guard·Q303·Q304·`0ce04ad`·850/960 |
| 2026-06-13 | **136차** — §1-3·§3-1·§3-3·§4-2·§4-3 G40b 반기 기초평가·정기욕구평가 현황·V95/V96·Q302·`a7b4a39`·`fad6df1`·845/948 |
| 2026-06-13 | **135차** — §1-3·§3-3·§4-2 G40 대시보드 widget·V94·Q301 갱신·`2589b94`·`e89175e`·831/931 |
| 2026-06-13 | **134차** — §1-3·§3-3 G40 FE 위험도평가 UI·QA-B62·Q301 Fixed·`686d686`·`9f80082`·830/925 |
| 2026-06-13 | **133차** — §1-3·§5-3 G40 BE-only·US-R03 per-staff compliance·G21 MIME·Q300·Q301·`22d736b`·`4efa168`·827/917 |
| 2026-06-14 | **132차** — §1-3·§5-3 FAQ21806 onboarding compliance·V92·Q300·`d4ee057`·`e76ca06`·813/908 |
| 2026-06-13 | **131차** — §1-3·§4-6 G2 CMS 해지·이력·duplicate guard·Q299·`4a622ab`·`9a6fdb6`·807/900 |
| 2026-06-13 | **129차** — §1-3·§5-3 G21 xls Content-Type casing·US-S02 입사일 미등록 StatCard·Q294·Q297·`1817c36`·`50bdb6e`·786/883 |
| 2026-06-13 | **128차** — §1-3·§3-1·§5-3 US-R02 staff health checkup 8-10·`StaffContextNav` 4탭·Q296·`604787f`·785/883 |
| 2026-06-13 | **127차** — §1-3·§5-3 US-S02 refresher training certificate upload·이수증 Modal·Q295·`0a7fe16`·764/871 |
| 2026-06-13 | **126차** — §1-3·§3-1·§5-3·§5-9 US-S02 refresher training·G34 sign modal·US-R03 lifecycle UX·`21b5d2d`·755/866 |
| 2026-06-13 | **125차** — §1-3·§5-3 US-R03 V87 date integrity·lifecycle Badge·`b3e59e2`·743/853 |
| 2026-06-13 | **124차** — §1-3·§5-3·§5-9 US-R03 offboarding guard·G21 draft sync·G34 signature audit·QA-B55·741/844 |
| 2026-06-13 | **123차** — §1-3·§5-3 US-R03 staff lifecycle BE+FE·G21 `588bfb1`·Q290 Partial Fixed·731/843 |
| 2026-06-12 | **122차** — §1-3·§3-3·§5-3 G21 legacy paired guard·G24 fiscal-year parsing·BNK-125~127·Q289~Q292·724/827 |
| 2026-06-12 | **121차** — §1-3·§3-3 G24-G14 기초평가·급여계약 탭 BE+FE·lifecycle hydrate·Q285·Q286·722/823 |
| 2026-06-12 | **118차** — §1-3·§3-1·§5-9 G34 선임 업무수행일지 BE+FE·G21 paired linkage guard·Q284·Q288·689/800 |
| 2026-06-12 | **117차** — §1-3·§5-9·§5-11 LifecycleWorkflowPanel G17/G32·G21 paired visit guard·Q238·Q283~Q287·675/782 |
| 2026-06-12 | **116차** — §1-3·§4-2·§5-9 QA-B49 parallel fallback·G17/G32 edit-flow pilot E2E·Q283·672/778 |
| 2026-06-12 | **112차** — §1-3·§3-1·§4-2·§4-3 G38 monitoring UI·branch-scoped compliance·Q277 Fixed·661/765 |
| 2026-06-12 | **115차** — §1-3·§4-2·§5-2 QA-B49 billing/NHIS snapshot·FE compliance snapshot-first·Q280·Q282·667/773 |
| 2026-06-12 | **114차** — §1-3·§3-2·§4-2·§5-2·§5-4·§5-8 G17/G32/G38/G39 dashboard compliance snapshot·DateInput G11/G15·Q280·Q281·667/772 |
| 2026-06-12 | **113차** — §1-3·§4-2·§5-9 G17/G32 edit UI·G39 dashboard 4-pillar·dashboard compliance counts·Q279·666/769 |
| 2026-06-12 | **111차** — §1-3·§3-1·§4-2·§5-9·§5-11 G38·G39·G21 import validation·Q276~Q278·659/751 |
| 2026-06-12 | **110차** — §1-3·§3-3·§5-11 G21 visit enum normalize·G37 attachment E2E·Q275·642/735 |
| 2026-06-12 | **109차** — §1-3·§3-3 G37 grade history attachments·BNK-105·Q274·637/725 |
| 2026-06-12 | **108차** — §1-3·§4-6·§5-5-1·§5-9·§5-10 J03 primary guardian·UXD-81·BNK-102·CMS FAILED·Q272·Q273·623/705 |
| 2026-06-12 | **102차** — §1-3·§4-2·§5-5-1·§5-9 G33 settle UI·G17 BNK-101·Q270 Fixed·Q271·608/693 |
| 2026-06-11 | **101차** — §1-3·§5-5-1 G33 settle API·claim guard·Q270·604/682 |
| 2026-06-11 | **100차** — §1-3·§4-6·§5-5·§5-5-1·§5-10 G33 BNK-94 billing start balance·Q269·603/679 |
| 2026-06-11 | **99차** — §1-3·§4-2·§4-3·§5-9 UXD-79 지표29 StatCard·파일럿 fixture·US-D01 primaryGuardian·Q266 Fixed·Q268·584/662 |
| 2026-06-11 | **98차** — §1-3·§4-3·§5-9 BNK-92 G32 plan FE·지표29 compliance·hq_admin 이용자 등록·Q265 Fixed·Q266·Q267·581/654 |
| 2026-06-11 | **97차** — §1-3·§4-6·§5-9 BNK-91 P2 NHIS copay·discrepancy UX·G32 `caseManagementPlan` API·Q264·Q265·577/649 |
| 2026-06-11 | **96차** — §1-3·§4-6 BNK-87 NHIS comparison FE UI(`BillingNhisComparisonPanel`)·Q264 Fixed·576/646 |
| 2026-06-11 | **95차** — §1-3·§4-2·§4-6·§5-9 BNK-87 NHIS comparison API·V74·G17/G32 compliance·dashboard 30일 widget·Q264·576/631 |
| 2026-06-11 | **94차** — §1-3·§3-1·§5-9 G17·G32 FE·G32 case management API·Q262 Fixed·Q263·569/626 |
| 2026-06-11 | **93차** — §1-3·§4-6·§5-10 US-M03 7-9 copay refund·환불대장 FE·G17 API·Q261·Q262·559/614 |
| 2026-06-11 | **92차** — §1-3·§4-6-1·§5-10 US-M03 billing ledger report API·US-G04 year-coverage pre-check·Q179 Fixed·Q260·491/607 |
| 2026-06-11 | **91차** — §1-3·§2-2·§4-6·§4-6-1 US-G04 fee schedule year guard·US-L01 bank sample xlsx·Q258·Q260·532/602 |
| 2026-06-11 | **90차** — §1-3·§2-2·§3-3·§4-6·§5-11·§8-2 G26 NTS xlsx·US-L01 8-bank guide·G21 visit slot guards·Q258–Q259·528/593 |
| 2026-06-11 | **89차** — §1-3·§3-3·§4-6 G2 copayAmount null guard·G26 UI exclusion guidance·UXD-77·Q257·521/574 |
| 2026-06-11 | **88차** — §1-3·§3-3·§4-6·§8-2 G26 CMS·EASY_PAY 의료비공제 제외·G2 CMS debit integrity·US-L04 조회 UX·Q254–Q256·519/569 |
| 2026-06-11 | **87차** — §1-3·§3-3·§4-6·§5-8-3·§8-2 G26 medical expense deduction API·US-L04 UI·UXD-76 VehiclesPage a11y·Q252–Q253·514/567 |
| 2026-06-11 | **86차** — §1-3·§4-6·§8-2 G2 recordCopayPayment paidAt guard·US-J02 guardian portal race guards·Q250–Q251·509/555 |
| 2026-06-11 | **85차** — §1-3·§2-2·§3-1·§3-2 G21 HOME_CARE alias·G2 paymentMethod guard·UXD-75 RecordsContextNav·SideNav service-fees·Q248–Q249·508/553 |
| 2026-06-11 | **84차** — §1-3·§4-6-1·§5-8·§5-8-1 G7 guidance API restore·G16 cross-branch fee guard·Form18 3-way workflow·Q111·Q133·Q237·Q247·503/547 |
| 2026-06-11 | **83차** — §1-3·§3-2·§4-6-1·§8-2 QA-B24 NHIS guidance UI·Field aria-required·guardian DRAFT BE filter·Q133·Q212·Q245–Q246·498/543 |
| 2026-06-11 | **82차** — §1-3·§2-2·§3-3·§4-7-3·§5-8·§5-8-3 G15 care-provision·G16 VehiclesPage·G2 paidAt·Q243–Q244·497/534 |
| 2026-06-10 | **81차** — §1-3·§2-2·§3-1·§3-3·§4-4·§5-8·§5-8-1·§5-8-2 G16 service-fee·G15 outings·UXD-73·V66–V69·Q239–Q242·482/524 |
| 2026-06-11 | **80차** — §1-3·§2-2·§5-8·§5-11 G15 Form22 log·Form18 guide·time compliance·G21 paired check-in sync·Q236–Q238·459/508 |
| 2026-06-11 | **79차** — §1-3·§2-2·§4-6·§5-8·§5-11 V65 transport contract integrity·G21 duplicate visit import·QA-B19 geocode guard 강화·Q234·Q235·457/485 |
| 2026-06-11 | **78차** — §1-3·§3-1·§4-4·§5-8 G15 출석 transportMode 이원화·QA-B19 geocode 저장 차단·Q232·Q233·455/484 |
| 2026-06-10 | **76차** — §1-3·§5-8 G15 transport contract API·FE 연동·V64·Q230·Q231·444/472 |
| 2026-06-10 | **75차** — §1-3·§5-4·§5-8 G11 가산율 안내·G15 이동서비스 수칙 UI·US-M04 cap success banner·Q226·Q229–Q230·434/467 |
| 2026-06-10 | **74차** — §1-3·§2-2·§4-6 G27 인지지원 월한도 BE·US-L01 bank branchId Fixed·Q226·Q227·Q228·420/451 |
| 2026-06-10 | **73차** — §1-3·§2-2·§4-6 BNK-49 US-M04 월한도 UI·US-L01 bank UI·Q226·Q227·Q228·414/447 |
| 2026-06-10 | **72차** — §1-3·§2-2·§4-6·§5-5 BNK-47 월한도 가드·BNK-48 은행 일괄입금·BillingSettings alias·Q226–Q227·401/432 |
| 2026-06-10 | **71차** — §1-3·§2-2·§4-6·§5-5 US-M03 청구 생성 기준·전월 미납 가드·V63·Q224–Q225·390/428 |
| 2026-06-10 | **70차** — §1-3·§2-2·§4-6·§4-7-3·§5-3·§8-2 G2 templates 5종·납부확인서·노인학대예방 UI·G19·Q221–Q223·383/413 |
| 2026-06-10 | **69차** — §1-3·§2-2·§4-6·§8-2 US-L01 payment guard·normalizeAmount·Q218–Q220·377/408 |
| 2026-06-10 | **68차** — §1-3·§4-6·§4-7-2·§4-7-3·§8-2 G2 email templates 3종·resolveDurationBand·Q204·Q213·Q216–Q217·371/402 |
| 2026-06-10 | **67차** — §1-3·§5-4·§4-6·§8-2 G9 V62 snapshot·FeeScheduleMatrix·NHIS 2026 seed·Q213–Q215·365/382 |
| 2026-06-10 | **66차** — §1-3·§5-4·§8-2 G9 duration_band·수가표 API·US-J02 guardian billing·Q210–Q212·363/373 |
| 2026-06-10 | **65차** — §1-3·§4-6-1·§5-11·§8-2 G21 confirm-lock UX·G2 SMTP email·Q204·Q209·361/367 |
| 2026-06-10 | **64차** — §1-3·§4-6 US-L03 CMS·FCMS stub·V59/V60·Q206–Q208·353/358 |
| 2026-06-10 | **63차** — §1-3·§4-6·§4-7·§8-2 US-J03 email channel·US-L02 discharged names·Q204–Q205·342/350 |
| 2026-06-10 | **62차** — §1-3·§4-2·§4-6·§5-2 US-M02 dashboard counts·US-L02 overdue widget·BillingContextNav·V58·Q202–Q203·335/346 |
| 2026-06-09 | **61차** — §1-3·§2-2·§3-2·§4-6·§5-11 US-L02 overdue pagination·US-L01 payment names·G21 paired sync·UXD-64·Q197–Q201·334/340 |
| 2026-06-09 | **54차** — §1-3·§3-2·§4-6-1·§5-6 UXD-58 NHIS 대기 보류 UI·Q181·Q182·288/288·81/267 |
| 2026-06-09 | **53차** — §1-3·§3-1·§4-6·§5-6·§5-11·§6-3-1 Epic V `/visits` UI·G7 PENDING_REVIEW·V54·Q180 Fixed·Q181·269/269·80/259 |
| 2026-06-09 | **60차** — §1-3·§2-2·§4-4·§4-6·§5-11 G2 notify·US-L01/L02·US-V02 cascade·BNK-26·Q109·Q174·Q194–Q196·329/323 |
| 2026-06-09 | **59차** — §1-3·§2-3·§5-11·§8-2 change-password·UXD-63 visit import UI·US-J02 pagination·Q122·Q189·Q192·311/316 |
| 2026-06-09 | **58차** — §1-3·§2-3·§4-3·§5-11·§11 G21 visit import·SEC-D17 settings·fieldErrors·Q189–Q191·306/306·90/298 |
| 2026-06-10 | **57차** — §1-3·§8-1·§8-2·§8-3 UXD-62 GuardianDailySummary 식사·FLOWCHART §9·Q188·288/288·89/289 |
| 2026-06-10 | **56차** — §1-3·§3-3·§4-7-2·§8-2 BNK-22 US-J03-h NotificationHistoryPanel·Q152 Fixed·Q187·288/288·89/287 |
| 2026-06-10 | **55차** — §1-2·§1-3·§4-2·§4-3·§5-3·§5-9 BNK-19 US-M02-b·UXD-59 Epic K·L·Q161 Fixed·Q183–Q186·294/294·86/277 |
| 2026-06-09 | **52차** — §1-3·§3-3·§4-2·§5-2·§5-5·§5-10·§8-2 v1.2.1 G14·US-M01~M03·설정 RBAC·V51–V53·Q176–Q180·264/264·235/235 |
| 2026-06-09 | **51차** — §1-3·§3-2·§8-1·§8-2·§8-3 UXD-55 GuardianBillingDetailModal·GuardianPortalPage 명세 인쇄·Q132·Q175·217/217 |
| 2026-06-08 | **50차** — §1-3·§3-2·§4-4·§4-6·§5-7·§5-8 BE v2 copay payment·overdue·UXD-53/54 BranchScopeNotice·Q173·Q174·246/246·214/214 |
| 2026-06-08 | **49차** — §1-3·§2-2·§4-4·§5-7·§5-8 BE pickup contact masking·pilotPageFlows T03·Q94·Q109 Swagger·Q172·241/241·208/211 |
| 2026-06-08 | **48차** — §1-3·§2-2·§4-3·§5-8 ClientForm transport UI·UXD-52·Q166 Fixed·Q171·241/241·68/208 |
| 2026-06-08 | **47차** — §1-3·§3-2·§5-4·§5-5·§5-8 transport pickup masking·UXD-51·Q169·Q170·241/241·65/199 |
| 2026-06-08 | **46차** — §1-3·§3-2·§5-8 transport pilot E2E·RBAC·UXD-50 forced-colors a11y·Q168·240/240·60/189 |
| 2026-06-08 | **45차** — §1-3·§4-2·§4-3·§5-2·§5-8 US-T01 Client transport profile API·UXD-49 HQ 지점명·Q166·Q167·231/231·60/189 |
| 2026-06-08 | **44차** — §1-3·§4-2·§4-4·§4-5·§5-2·§5-8·§7-6 UXD-48 Recharts 복원·Q118·Q119·Q165·226/226·60/183 |
| 2026-06-08 | **43차** — §1-3·§4-7·§5-8 UXD-47 transport unconfirm UI·StaffPage a11y·PATCH contract·Q163·Q164·226/226·58/179 |
| 2026-06-08 | **42차** — §1-3·§3-1·§4-7·§5-3·§5-8 v3 §3-8 StaffPage·transport unconfirm·Q162·Q163·226/226·55/170 |
| 2026-06-08 | **41차** — §1-3·§5-9 v3 meals/programs API·V49·FE·BE 연동·Q160 Fixed·Q161·224/224·54/164 |
| 2026-06-08 | **40차** — §1-3·§3-1·§5-8·§5-9 v1.3-A transport API·식사·프로그램 UI shell·Q159·Q160·212/212·53/157 |
| 2026-06-08 | **39차** — §1-3·§3-1·§4-6-1·§5-8 PAID 수납 알림·UNMATCHED 후보 검색·배차 UI shell·Q135·Q159·202/202·50/150 |
| 2026-06-08 | **38차** — §1-3·§2-2·§4-6-1·§5-6 US-G06 DISCREPANCY compare·Q135·Q158·198/198·46/143 |
| 2026-06-08 | **37차** — §1-3·§4-5·§6-4·§7-5·§11 UXD-41 US-F03 IncidentRecordForm·Q157·191/191·45/137 |
| 2026-06-08 | **36차** — §1-3·§3-2·§4-5·§7-6·§11 Q154 Fixed·UXD-40 vitalsRanges·Q155·185/185·44/130 |
| 2026-06-08 | **35차** — §1-3·§4-5·§4-6-1·§7-6·§8-2 UXD-39 건강·NHIS UI·J03 vitals DAILY_CARE·Q154·179/179·40/115 |
| 2026-06-07 | **34차** — §1-3·§4-4·§5-7·§6-3·§8-4 US-E01~E05 출석 UI·V46·Q94·Q96·Q109·178/178·36/110 |
| 2026-06-07 | **32차** — §1-3·§3-1·§4-3–§4-5·§4-6 UXD 15 Must 화면·ModulePage 제거·Q151·171/171·28/89 |
| 2026-06-08 | **31차** — §1-3·§2-2·§3-1·§4-2·§10-2 v1.2 P0 shell·SideNav·SessionTimeout·V45·170/170·27/82 |
| 2026-06-08 | **29차** — §1-3·§3-3·§8-5 Must API FE·Solapi J03·V44·152/152·40/40 |
| 2026-06-08 | **28차** — §1-3·§4-7-1 V43 Fixed·J03·프론트 baseline·B08 API 필드명 |
| 2026-06-07 | **26차** — §1-3·§3-3·§4-3 TSR 56–57 V43·FE-18·결정 59 이메일 초대 (Q144–Q145), 테스트 253/209·758 modules |
| 2026-06-07 | **25차** — §1-3·§3-3 COD 36 V42·GuardianListCard·MaskedPhone WIP (Q142–Q143), 테스트 253/209·758 modules |
| 2026-06-07 | **24차** — §1-3·§2-2·§3-1·§3-3·§8-5 COD 35차 FE-17 LogoutButton·PublicAuthLayout·GuardianInvitationAcceptForm (Q141), Vitest 40/199 |
| 2026-06-07 | **23차** — §1-3·§3-2·§3-3·§8-5 COD 34차 GuardianInvitationAcceptPage·FE-16 ds-* (Q139–Q140) |
| 2026-06-07 | **21차** — §1-3·§3-1·§4-6·§4-6-1 UXD 22차 PaymentRecordModal·ReconciliationSummaryBar·DiscrepancyComparePanel·MonthInput (Q134–Q136) |
| 2026-06-07 | **20차** — §1-3·§4-2·§4-6·§4-6-1·§5-4·§8-2·§8-3 UXD 20–21차 FilterChips·BillingStatusConfirmModal·HealthAlertList·GuardianDailySummary·FeeScheduleTable·CopayRateTable·NhisImportGuidePanel (Q128–Q133) |
| 2026-06-07 | **19차** — §1-3·§2-2·§2-3·§5-5 SettingsPage 5탭·LoginHistoryPanel·PasswordResetRequestModal (Q125–Q126) |
| 2026-06-07 | **18차** — §1-3·§2-2·§3-3·§4-2·§4-5·§4-6·§5-5·§7-6 Recharts·BatchProgressSteps·보호자 초대·설정 패널·PasswordChangeModal (Q118–Q123) |
| 2026-06-07 | **17차** — §1-3·§5-4 수가표 이력 보기 UI(Q117 UXD 14차) |
| 2026-06-07 | **16차** — §5-5 Switch 셀프 체크인 토글(Q116)·§3-2·§11 갱신 |
| 2026-06-07 | **13차** — §4-3 이용자 등록 UXD 10차(primaryGuardian·CopayTypeSelect·client_user UI Q113)·§1-3 갱신 |
| 2026-06-06 | **12차** — US-D03 건강·출석 탭(Q102), SessionTimeout US-B03(Q112), NHIS guidance(Q111), §1-3·§2-2·§3-3·§4-6-1 |
| 2026-06-06 | **11차** — SideNav US-UX-02·v1.2 보호자/입금/미납(Q107)·V39·QR 부분(Q109)·보호자 청구 API(Q108) |
| 2026-06-06 | **10차** — 출석 통계(`/attendance/stats`) UI 응답 불일치 안내(Q106), V39 보호자 연결 필수 정정 |
| 2026-06-08 | §1-3·§3-1·§4-4·§7-6·§8-4 App.jsx 2차 라우트(QR·체크인·건강 추이·수가표·설정)·BranchesPage 미등록 (FAQ Q104–Q105) |
| 2026-06-07 | §1-3·§3-3·§4-3·§4-6-1 NHIS import·대사 필드·이용자 상세 탭·`/clients/:id/edit` (FAQ Q100–Q103) |
| 2026-06-07 | §4-4·§4-5·§4-6·§6-3·§6-4·§8-2 출석 roster·교통편·건강 투약/사고·청구 yearMonth·보호자 필드 (FAQ Q94–Q99) |
| 2026-06-07 | §2-3·§2-4·§3-1·§4-3·§5-4 비밀번호 UI·BranchSwitcher UUID·미등록 라우트·퇴소/사진·수가표 API-only (FAQ Q87–Q91) |
| 2026-06-07 | §3-2 접근성(UXD)·§4-2·§5-2 대시보드 API-only·§4-4·§6-3 결석 API·SideNav 진입·FAQ Q85–Q86 |
| 2026-06-06 | §3-2 이용자 상세 탭·주민번호 [열람]·§8 보호자 포털 탭·API 경로 정합 안내 (FAQ Q83) |
| 2026-06-06 | 프론트 Must 화면 JWT·API 연동 반영 — §1-3·§2-2·§4-6·§4-6-1·건강·QR·보호자 UI 상태 갱신 |
| 2026-06-06 | V36–V37: 동의·인정 시작일·lifecycle temporal sanity, 프론트 디자인 시스템·ProtectedRoute·로그인 rate limit 안내 |
| 2026-06-06 | V35: 수가표·QR actor backstop(`created_by`), §4-4·§5-4·§6-3 감사 안내 |
| 2026-06-06 | §1-3 Must UI 미구현 경로 목록 추가 (API-only 검증 안내) |
| 2026-06-06 | V34: 퇴소 시각 무결성·지점별 purge 인덱스, NHIS UNMATCHED 수동 매칭 절차(§4-6-1) |
| 2026-06-06 | V32–V33: actor 감사·청구 상태 필터 API(`?status=`)·퇴소 purge 인덱스 반영 |
| 2026-06-06 | V29–V31: 사업자번호 검색·이메일 UK·대표 보호자·비밀번호 재설정 세션 폐기 |
| 2026-06-06 | 이용자 탭 API·주민번호 복호화·QR 유효시간(60분)·보호자 daily-records 반영, Flyway V28 |
| 2026-06-06 | `hq_admin`·`caregiver` 매뉴얼 추가, 백엔드 구현 상태·NHIS 대사 반영 |
| 2026-06-05 | 초안 작성 — 센터장·사회복지사·보호자 역할별 매뉴얼 |

---

## [TWR] 부록 — 현장 운영 절차 (실시간 가이드)

### A1. 월말 청구 및 수납 확인 체크리스트

**대상 역할**: `hq_admin`, `branch_admin`

**사전 조건**: 모든 당월 출석·건강 기록이 완료되어야 함

| 단계 | 작업 | 확인 지점 | API/화면 |
|------|------|----------|---------|
| 1 | **출석 일괄확정** | `/visits` → 「일괄확정」 전 **공단 비교** 필수 (Q570) | `GET /api/v1/visits/confirm-readiness` |
| 2 | **청구 생성 가능 검증** | 대시보드 → **전월 미납 가드** 확인 (Q48·Q310) | `GET /api/v1/billing/claims/generation-guard` |
| 3 | **청구 생성** | 「청구 생성」 클릭 → 월별/기준 선택 (Q601) | `POST /api/v1/billing/claims/generate` |
| 4 | **수납 입력** | 입금 계좌 확인 → 수납 기록 입력 | `POST /api/v1/billing/claims/.../record-copay-payment` |
| 5 | **공단 제출** | NTS 수동 제출 또는 자동화 대기 (Q600) | Manual or `POST /api/v1/billing/nts/submit` (P3) |
| 6 | **대사 완료** | 청구-공단-수납 금액 3자 대조 | `GET /api/v1/billing/claims/{claimId}/nhis-comparison` |

**트러블슈팅**:
- **청구 생성 버튼 비활성화** → Q310·Q571 참고 (전월 미납 확인)
- **출석 일괄확정 실패** → Q570 참고 (공단 비교 필수)

### A2. 출석 명단 생성 및 QR 배포 프로세스

**대상 역할**: `branch_admin`, `caregiver`, `social_worker`

**월초 작업 (약 30분)**:

1. **월간 출석 일정 계획**
   - `/visits` → 「신규 생성」 → 클라이언트·요양보호사·시간 입력
   - 또는 **월간 반복 패턴 적용** (향후 FE 개발)

2. **보호자 QR 생성** (현장 배포용)
   - Swagger UI → `GET /api/v1/visits/{visitId}/qr-token`
   - 응답의 `qrPayload` 복사 → 온라인 QR 생성 서비스 (goQR.me)
   - **이미지 다운로드** → 센터 게시판 또는 카톡 배포
   - **유효기간**: 24시간 (당일 체크인만 가능)

3. **명단 인쇄** (보호자·가족용)
   - `/visits` → CSV Export 또는 PDF 인쇄
   - 포함 정보: 날짜·시간·담당 요양보호사·이동 정보

**일상 운영**:
- 보호자 체크인 → 「셀프 체크인」 버튼 또는 **QR 스캔**
- 요양보호사 기록 → 「체크 아웃」 시간 입력 (Q94)

> **Q94·Q109·Q599** 참고.

### A3. 건강 기록 및 위험도 모니터링

**대상 역할**: `caregiver`, `social_worker`, `hq_admin`

**일간 점검** (아침 또는 저녁):

| 항목 | 확인 방법 | 임계값 | 대응 |
|------|----------|--------|------|
| **혈압** | `/clients/{id}/health-records` → 「혈압」 탭 | 수축 140 이상 | 의료진 상담 필수 |
| **당뇨** | 「혈당」 탭 | 공복 126 이상 | 모니터링 강화 |
| **사고·낙상** | 「사건 기록」 탭 | 발생 시 즉시 | 보호자 통지 (Q326~329) |
| **욕창** | 「욕창 기록」 탭 | 1단계 이상 | 간호 계획 수립 (FAQ21768) |

**주간 리뷰** (금요일):
- 대시보드 → **「건강 경고」** StatCard (hq_admin만)
- 주간 건강 변화 추이 확인
- 고위험 이용자 리스트 세그먼트

> **§5·§6 건강·사고 기록** 참고.

### A4. 목욕 서비스 월간 일정 복사

**대상 역할**: `hq_admin`·`branch_admin`·`social_worker`

**월초 작업 (약 2분)**:

1. **`/care/bathing-schedules`** 로 이동합니다.
2. **「대상 월」** 을 복사 받을 월로 설정하고 **조회**합니다.
3. **「전월 일정 복사」** 를 클릭 → 확인 → 완료 메시지의 **생성·건너뜀 건수**를 확인합니다.

**API (Swagger·자동화)**:

```bash
# 2026년 7월 목욕 일정을 전월(6월)에서 복사
curl -X POST http://localhost:8080/api/v1/care/bathing-schedules/copy-from-previous-month \
  -H "Authorization: Bearer <access_token>" \
  -H "Content-Type: application/json" \
  -d '{"targetYearMonth": "2026-07"}'

# 응답 예
{
  "targetYearMonth": "2026-07",
  "sourceYearMonth": "2026-06",
  "createdCount": 12,
  "skippedCount": 2,
  "created": [ ... ]
}
```

> **Q598·BNK-466** 참고.

### A5. 청구 명세 필터 해석

**대상 역할**: `hq_admin`, `branch_admin`

청구 조회 시 반환되는 필터 조건 해석:

```json
{
  "appliedFilters": {
    "depositPeriodLabel": "1~15일",        // 입금 기간
    "receiptBasisLabel": "청구기준",       // 청구 기준
    "branchName": "본점"                   // 지점명
  }
}
```

**사용 사례**:
- **인쇄 헤더**: 「조회 조건: 1~15일 · 청구기준 · 본점」 명시
- **월별 대시보드**: 반월별(1~15일/16~말일)로 분리해 비교
- **감사**: 적용된 필터를 기록해 추후 대조 시 근거 제시

> **Q601·API_SPEC §8-4** 참고.

---

*이 문서는 tech_writer 에이전트가 관리합니다. UI 구현 완료 시 화면 캡처·버튼 명칭을 동기화하세요.*
