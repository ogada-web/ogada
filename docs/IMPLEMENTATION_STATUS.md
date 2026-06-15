<!-- doc:owner=TWR doc:audience=PLN,COD,DBA,TSR updated=2026-06-16T02:00:00+09:00 -->

# ogada 구현 상태 스냅샷

> **작성**: tech_writer 에이전트  
> **기준 시점**: 2026-06-16 develop HEAD  
> **백엔드 commit**: `8b7e476`  
> **프론트엔드 commit**: `10f32c4`  
> **DB 마이그레이션**: Flyway **V1–V132**  
> **테스트 상태**: `mvn test` 1231/1231 ✅, Vitest 1393/1393 ✅

---

## 개요

본 문서는 **develop 브랜치의 현재 구현 상태**를 한눈에 볼 수 있는 스냅샷입니다.  
**완료·진행중·미구현 기능**을 상태별로 정리합니다.  
자세한 기술 설명은 [API_SPEC.md](technical/API_SPEC.md), [ERD.md](technical/ERD.md)를 참고하세요.

---

## 1. 인증 & 권한 (Complete ✅)

### 로그인·인증

| 기능 | 상태 | 비고 |
|------|------|------|
| JWT 기반 로그인 (`POST /auth/login`) | ✅ | access/refresh 토큰, 30분 idle 타임아웃 |
| 토큰 갱신 (`POST /auth/refresh`) | ✅ | refresh 토큰으로 access 재발급 |
| 로그아웃 (`POST /auth/logout`) | ✅ | refresh 토큰 폐기 |
| 비밀번호 재설정 요청 (`POST /auth/password/reset-request`) | ✅ | 이메일 발송 (stub) |
| 비밀번호 재설정 (`POST /auth/password/reset`) | ✅ | 토큰 기반 변경 |
| 현재 사용자 정보 조회 (`GET /auth/me`) | ✅ | 역할·스코프 포함 |

### 역할 & 권한 관리

| 기능 | 상태 | 비고 |
|------|------|------|
| 7개 역할 (`platform_admin`, `hq_admin`, `branch_admin`, `social_worker`, `caregiver`, `guardian`, `client_user`, `sysadmin`) | ✅ | RBAC 검증 |
| 다지점 권한 (`branch_ids`, `active_branch_id`) | ✅ | hq_admin 지점 전환 API |
| 테넌트 격리 (JWT `organization_id`) | ✅ | 모든 쿼리·응답 필터링 |
| 보호자 권한 분리 (자신 이용자만) | ✅ | `guardian_clients` 테이블 연결 |

---

## 2. 플랫폼·조직 관리 (Complete ✅)

| 기능 | API | 상태 | 비고 |
|------|-----|------|------|
| Tenant 등록 (`POST /platform/organizations`) | ✅ | 신규 고객 센터 등록 |
| Tenant 목록 (`GET /platform/organizations`) | ✅ | 전국 가입 고객사 |
| Tenant 상세·상태 변경 (`GET/PATCH /platform/organizations/{id}`) | ✅ | 활성/정지 |
| 첫 `hq_admin` 발급 (`POST /platform/organizations/{id}/admins`) | ✅ | 온보딩 흐름 |
| 지점 등록 (`POST /branches`) | ✅ | branch_admin 이상 |
| 지점 목록·상세 (`GET /branches*`) | ✅ | 스코프 검증 |
| 지점 수정·비활성화 (`PATCH /branches/{id}`) | ✅ | 상태·설정 |
| 지점 통합재가 제공기관 검색 가이드 (`GET /branches/{id}/integrated-home/provider-discovery`) | ✅ | G19 · 롱텀 필터 URL |
| 직원 계정 관리 (`POST/PATCH /users*`) | ✅ | 역할·지점 배정 |

---

## 3. 이용자 관리 (Complete ✅)

### 기본 정보 & 관리

| 기능 | 상태 | 비고 |
|------|------|------|
| 이용자 등록 (`POST /clients`) | ✅ | 보호자 1명 이상 필수 연결(V39) |
| 이용자 목록·검색 (`GET /clients`) | ✅ | 지점 필터·페이지네이션 |
| 이용자 상세 (`GET /clients/{id}`) | ✅ | 기본·장기요양·보호자 정보 |
| 이용자 수정 (`PATCH /clients/{id}`) | ✅ | 등급 변경 시 이력 append |
| 퇴소 처리 (`POST /clients/{id}/discharge`) | ✅ | 상태 전환 |
| 사진 업로드 (`POST /clients/{id}/photo`) | ✅ | 용량·형식 검증 |

### 보호자 관리

| 기능 | 상태 | 비고 |
|------|------|------|
| 보호자 목록 (`GET /clients/{id}/guardians`) | ✅ | 연결 보호자 |
| 보호자 연결 (`POST /clients/{id}/guardians`) | ✅ | 기존 계정 또는 신규 초대 |
| **보호자 이메일 초대** (`POST /clients/{id}/guardians/invitations`) | ✅ | **v1.1** — 7일 만료, 재발송·취소 |
| 초대 수락 & 계정 생성 (`POST /guardian/invitations/{token}/accept`) | ✅ | `guardian` 계정 자동 생성 |
| 초대 목록 (`GET /clients/{id}/guardians/invitations`) | ✅ | PENDING/ACCEPTED/EXPIRED 상태 |

### 등급 & 이력

| 기능 | 상태 | 비고 |
|------|------|------|
| 등급 변동 이력 조회 (`GET /clients/{id}/ltc-grade-history`) | ✅ | G14 · 최신순 페이지 |
| 등급 이력 수동 등록 (`POST /clients/{id}/ltc-grade-history`) | ✅ | 감사 추적 |
| **등급 이력 첨부 PDF/PNG** (`GET/POST/DELETE /clients/{id}/ltc-grade-history/{historyId}/attachments`) | ✅ | **G37** · 10MB 제한 |

### 욕구사정 & 위험도 평가

| 기능 | 상태 | 비고 |
|------|------|------|
| **정기 욕구사정 조회·등록·수정** (`GET/PUT /clients/{id}/needs-assessments*`) | ✅ | **G24** (8항목) + **G24b** (5필드) |
| **욕구사정 compliance 집계** (`GET /clients/needs-assessments/compliance`) | ✅ | **G24b** 대시보드 widget 연동 |
| **신규입소 위험도 평가 (3종)** (`GET/PUT /clients/{id}/risk-assessments`) | ✅ | **G40** · FALL/ULCER/COGNITIVE |
| **신규입소 compliance** (`GET /clients/admission-risk-assessments/compliance`) | ✅ | `admissionComplete` boolean |
| **반기 기초평가 위험도 (3종)** (`GET/PUT /clients/{id}/periodic-risk-assessments`) | ✅ | **G40b** · fiscal-half 범위 |
| **반기 compliance** (`GET /clients/periodic-risk-assessments/compliance`) | ✅ | `periodicComplete` boolean |

### 급여계약 & 문서

| 기능 | 상태 | 비고 |
|------|------|------|
| **급여계약 첨부 (PDF/PNG)** (`GET/POST/DELETE /clients/{id}/benefit-contract-attachments`) | ✅ | **G14/US-T10** · 파일함 |

---

## 4. 출석 관리 (Complete ✅)

### 수기 체크인/아웃

| 기능 | 상태 | 비고 |
|------|------|------|
| 출석 현황 조회 (`GET /attendance`) | ✅ | 날짜·지점·transportMode 필터 |
| 수기 체크인 (`POST /attendance/check-in`) | ✅ | method: manual |
| 수기 체크아웃 (`POST /attendance/check-out`) | ✅ | 교통편 기록 포함 |
| 결석 사유 기록 (`POST /attendance/absence`) | ✅ | - |

### QR B방식 (셀프 체크인)

| 기능 | 상태 | 비고 |
|------|------|------|
| 지점 QR 생성 (`POST /branches/{id}/qr`) | ✅ | 유효시간 설정 |
| 현재 유효 QR 조회 (`GET /branches/{id}/qr`) | ✅ | 직원용 게시 |
| **QR 셀프 스캔** (`POST /attendance/qr/scan`) | ✅ | **B방식** · guardian/client_user · 중복 체크인 방지 |
| 보호자 체크인 대상 목록 (`GET /guardian/checkin-targets`) | ✅ | 연결 이용자 |

### 통계

| 기능 | 상태 | 비고 |
|------|------|------|
| 월별 출석 통계 (`GET /attendance/stats/monthly`) | ✅ | 지점·전사 |
| **이동 서비스 계약 서명** (`POST /transport/contracts/{id}/signature`) | ✅ | **G15** · V64 |

---

## 5. 건강 기록 (Complete ✅)

| 기능 | 상태 | 비고 |
|------|------|------|
| 건강 기록 시계열 (`GET /clients/{id}/health`) | ✅ | 그래프용 |
| 일일 건강 체크 (`POST /clients/{id}/health/vitals`) | ✅ | 혈압·체온·혈당·SpO2 |
| 투약 기록 (`POST /clients/{id}/health/medications`) | ✅ | 약품·용량·시간·투약자 |
| 낙상·사고 이벤트 (`POST /clients/{id}/health/incidents`) | ✅ | - |
| 특이사항 메모 (`POST /clients/{id}/health/notes`) | ✅ | - |
| **Health readiness probe** (`GET /api/v1/health`) | ✅ | **QA-B96** · DB 상태 |
| **Health liveness ping** (`GET /api/v1/health/ping`) | ✅ | **QA-B96** · DB 없이 |

---

## 6. 청구·정산 (Complete ✅)

### 수가표 & 설정

| 기능 | 상태 | 비고 |
|------|------|------|
| 수가표 관리 (`GET/POST/PATCH /billing/fee-schedules`) | ✅ | 연도·등급별 1일 수가 |
| 본인부담 비율표 (`GET/PATCH /billing/copay-rates`) | ✅ | GENERAL/REDUCED/MEDICAID |
| **가산율 catalog** (`GET /billing/fee-surcharge-rates`) | ✅ | **G11** · 야간/심야/휴일/유급 |
| **가산율 preview** (`POST /billing/fee-surcharge-preview`) | ✅ | 제공 시간 기준 |

### 청구서·명세서

| 기능 | 상태 | 비고 |
|------|------|------|
| 월별 청구 생성 (`POST /billing/claims/generate`) | ✅ | 자동 계산 |
| 청구 목록 (`GET /billing/claims`) | ✅ | 상태·지점 필터 |
| 청구 상세 (`GET /billing/claims/{id}`) | ✅ | 이용자별 명세 |
| 청구 상태 변경 (`PATCH /billing/claims/{id}/status`) | ✅ | DRAFT→CONFIRMED→PAID |
| 명세서 PDF 출력 (`GET /billing/claims/{id}/statement.pdf`) | ✅ | 인쇄용 |
| **보호자 명세 알림 요청** (`POST /billing/claims/{id}/notify`) | ✅ | **G2-n** · 이메일 skeleton |

### NHIS Import & Reconciliation

| 기능 | 상태 | 비고 |
|------|------|------|
| **NHIS 엑셀 import** (`POST /billing/imports/nhis`) | ✅ | 공단 청구내역상세 |
| **배치 상세** (`GET /billing/imports/nhis/{batchId}`) | ✅ | 행 목록·상태 |
| **행 수동 매칭** (`PATCH /billing/imports/nhis/rows/{rowId}/match`) | ✅ | UNMATCHED→MATCHED |
| **import 온보딩 가이드** (`GET /billing/imports/nhis/guidance`) | ✅ | Chrome/Edge 안내 |
| 수동 매칭 후보 검색 (`GET /billing/imports/nhis/{batchId}/candidates`) | ✅ | - |

### 간편결제 (Stub PG)

| 기능 | 상태 | 비고 |
|------|------|------|
| **간편결제 요청 생성** (`POST /billing/easy-pay/claims/{id}`) | ✅ | **v1.1·7-5** · provider: CARD/KAKAO_PAY (Stub) |
| **간편결제 이력 조회** (`GET /billing/easy-pay/claims/{id}`) | ✅ | 상태·결과 |
| **본인부담 간편결제** | 🟡 | live PG 실연동 **P2** (Solapi FCMS) |

---

## 7. 대시보드 (Complete ✅)

### 지점 대시보드

| 기능 | 상태 | 비고 |
|------|------|------|
| 오늘 출석 요약 (`GET /dashboard/branch`) | ✅ | 입소/귀가/결석 |
| 이용자 통계 | ✅ | 입소/퇴소/이용 |
| 건강 이상 알림 | ✅ | 목록·상세 |
| **compliance StatCard·필드 (17개)** | ✅ | G17/G32/G38/G39 규정준수 |
| **G24b 욕구사정 widget (2개)** | ✅ | `needsAssessmentGapCount`, `gradeChangeReassessmentDueCount` |
| **NHIS 미매칭·대기·미납 건수** | ✅ | `nhisUnmatchedCount`, `pendingReviewCount`, `overdueCount` |

### 통합 대시보드 (HQ)

| 기능 | 상태 | 비고 |
|------|------|------|
| 전 지점 비교·집계 | ✅ | 지점별 카드 |
| 지점·기간 필터 | ✅ | 상세 조회 |
| 전 지점 건강 이상 통합 목록 (`GET /dashboard/hq/alerts`) | ✅ | 지점명 표시 |
| 지점 선택기 (`POST /auth/active-branch`) | ✅ | 다지점 권한 전환 |

---

## 8. 방문요양 (Visit Scheduling) (Complete ✅)

| 기능 | 상태 | 비고 |
|------|------|------|
| **방문 일정 목록** (`GET /visits`) | ✅ | **G21** · scheduleKind: PLAN/BILLING |
| **방문 일정 생성** (`POST /visits`) | ✅ | createPairedBillingSchedule 옵션 |
| **방문 일정 상세** (`GET /visits/{id}`) | ✅ | stops 포함 |
| **일정 수정·확정** (`PATCH/POST .../confirm`) | ✅ | DRAFT→CONFIRMED |
| **일정 취소·재편집** (`POST .../unconfirm` / `PATCH .../unconfirm`) | ✅ | alias 지원 |
| **NHIS import** (`POST /visits/imports/nhis`) | ✅ | 엑셀 업로드 |
| **일괄확정 사전 점검** (`GET /visits/confirm-readiness`) | ✅ | blocker 검증 |
| **일괄확정** (`POST /visits/batch-confirm`) | ✅ | 게이트 3단계 |
| **체크인/체크아웃** (`POST /visits/{id}/check-in/out`) | ✅ | method: MOBILE/MANUAL |
| **주소 geocode 프록시** (`POST /transport/geocode`) | ✅ | Kakao Local API |

---

## 9. 식사·프로그램 (Partial ⏳)

| 기능 | 상태 | 비고 |
|------|------|------|
| 당일 식단 조회 (`GET /meals/menus`) | ✅ | 조회 |
| 식사 기록 (`GET/POST /meals/records`) | ✅ | 식사량·식이 제한·영양사 소견 |
| 프로그램 일정 (`GET /programs/schedules`) | ✅ | 조회 |
| 프로그램 참여 기록 (`GET/POST /programs/participations`) | ✅ | 참여·만족도 |
| **식단·일정 등록 API** | ⏳ | **Q161** — 후속 구현 |

---

## 10. 배차·이동 경로 (v1.3-B) (Complete ✅)

| 기능 | 상태 | 비고 |
|------|------|------|
| 픽업 명단 (`GET /transport/roster`) | ✅ | **G15** · PII 마스킹(role별) |
| 운행 목록·상세 (`GET /transport/runs*`) | ✅ | DRAFT/CONFIRMED 상태 |
| DRAFT 운행 생성·수정 (`POST/PATCH /transport/runs*`) | ✅ | ≤15 stops |
| 운행 확정·재편집 (`POST .../confirm` / `PATCH .../unconfirm`) | ✅ | 상태 전환 |
| **배차 제안** (`POST /transport/runs/suggest`) | ✅ | **v1.3-B** · OR-Tools VRP |
| 배차 설정 (`GET/PUT /transport/settings`) | ✅ | **v1.3-B** · suggest parameters |

---

## 11. 직원 관리 & HR (L02/L03/L04 — Nursing/Care) (Complete ✅)

### 선임 요양보호사 일지 (G34)

| 기능 | 상태 | 비고 |
|------|------|------|
| **업무수행일지 목록·생성·수정·서명** (`GET/POST/PATCH /staff/lead-caregiver-logs*`) | ✅ | **G34** · DRAFT→SIGNED |

### 보수교육 (G34·8-7-1)

| 기능 | 상태 | 비고 |
|------|------|------|
| **보수교육 compliance** (`GET /staff/refresher-training/compliance`) | ✅ | 격년(2년) 주기 |
| **이수증 관리** (`GET/POST/DELETE /staff/refresher-training/users/{id}/certificates`) | ✅ | PDF·JPEG·PNG |

### 건강검진 (8-10)

| 기능 | 상태 | 비고 |
|------|------|------|
| **건강검진 compliance** (`GET /staff/health-checkups/compliance`) | ✅ | 5영역 checklist |
| **건강검진 기록** (`GET/POST /staff/health-checkups/users/{id}`) | ✅ | 연간 1회 |

### HR 파일함 (8-6·FAQ21806)

| 기능 | 상태 | 비고 |
|------|------|------|
| **HR 파일 관리** (`GET/POST/DELETE /staff/hr-files/users/{id}*`) | ✅ | 입사서류·건강검진 결과 |

### 교육일지 (G41·8-7)

| 기능 | 상태 | 비고 |
|------|------|------|
| **교육일지 등록** (`GET/POST /staff/training-logs`) | ✅ | **G41** · 5종 분류 (V129 28종 enum) |
| **교육일지 compliance** (`GET /staff/training-logs/compliance`) | ✅ | **G41b** · 필수 5종·신규 7일 |

### 팀장급 자격 (G34-QUAL)

| 기능 | 상태 | 비고 |
|------|------|------|
| **팀장급 자격 compliance** (`GET /staff/team-lead-qualification/compliance`) | ✅ | **G34-QUAL** · 5년(월60h×60개월) |

### 직원 현황 리포트 (8-12)

| 기능 | 상태 | 비고 |
|------|------|------|
| **직원 현황 리포트** (`GET /staff/reports/status`) | ✅ | **G-Health-8-12** 집계 |
| **CSV export** (`GET /staff/reports/status/export`) | ✅ | 대시보드 pagination |

### 간호·돌봄 기록 (L02/L03 — NEW)

| 기능 | 상태 | 비고 |
|------|------|------|
| **집중 배설 관찰** (`GET/POST/PATCH /care/intensive-excretion-observations`) | ✅ | **L02_M07** · V131 |
| **신체속박 기록** (`GET/POST/PATCH /care/body-restraint-records`) | ✅ | **L02_M07** · V131 |
| **간호 바이탈 체크** (`GET/POST/PATCH /nursing/vital-checks`) | ✅ | **L03** · V115 |
| **간호 체중 관리** (`GET/POST/PATCH /nursing/weight-records`) | ✅ | **L03** · V116 |
| **욕창 관리** (`GET/POST/PATCH /nursing/pressure-ulcer*`) | ✅ | **G-NURSING** · 평가·기록·리포트 |
| **응급 상황 기록** (`GET/POST/PATCH /nursing/emergency-records`) | ✅ | **L03_M04** · V119 |
| **구강 관리 체크** (`GET/POST/PATCH /nursing/oral-care-checks`) | ✅ | **L03_M13** · V118 |
| **배설·튜브 기록** (`GET/POST/PATCH /nursing/excretion-tubes`) | ✅ | **L03_M06** · V124 |
| **서비스 제공 기록** (`GET/POST/PATCH /nursing/service-records`) | ✅ | **L03_M01** · V123 |

### 서비스 리포트 (L03)

| 기능 | 상태 | 비고 |
|------|------|------|
| **간호 서비스 리포트** (3종: 제공/미제공/잔여) | ✅ | **L03_M07/M09/M10** |
| **욕창 급여제공 리포트** | ✅ | **L03_M15** |

### 온보딩 지원 (G-ONBOARD)

| 기능 | 상태 | 비고 |
|------|------|------|
| **지점 온보딩 정보 관리** (`GET/POST/PATCH /branches/{id}/onboarding*`) | ✅ | **G-ONBOARD-SUPPORT** · V126 |

---

## 12. 보호자 포털 (Complete ✅)

| 기능 | 상태 | 비고 |
|------|------|------|
| 보호자 로그인 | ✅ | guardian 역할 |
| 연결 이용자 정보 조회 | ✅ | 기본·건강·출석 |
| 일일 기록 열람 | ✅ | 기록(건강·출석·식사) |
| 명세·청구 조회 (`GET /guardian/clients/{id}/billing`) | ✅ | **G2-n** 알림 연동 |
| **QR 셀프 체크인** (`POST /attendance/qr/scan`) | ✅ | **B방식** |
| **보호자 알림 수신 설정** (`GET/PUT /guardian/notification-preferences`) | ✅ | **v1.1** 채널/주제 ON/OFF |
| **보호자 발송 이력 조회** (`GET /guardian/notifications`) | ✅ | **v1.1** 알림톡·SMS 기록 |

---

## 13. 규정준수·모니터링 (Complete ✅)

### 모니터링 & Compliance

| 기능 | 상태 | 비고 |
|------|------|------|
| **통합 모니터링 checklist** (`GET /compliance/monitoring/checklist`) | ✅ | **G30** 자가진단·유선상담·rolling 6개월 |
| **자가진단 template** (`GET /compliance/monitoring/items`) | ✅ | 15문항 |
| **자가진단 기록** (`GET/POST/PATCH /compliance/monitoring/self-diagnoses`) | ✅ | 월 중복 불가 |
| **유선상담 기록** (`GET/POST /compliance/monitoring/phone-consultations`) | ✅ | 월 5회 달성 여부 |
| **유선상담 추천** (`GET /compliance/monitoring/phone-consultations/suggestions`) | ✅ | 미작성 수급자 5명 |
| **유선상담 compliance** (`GET /compliance/monitoring/phone-consultations/compliance`) | ✅ | 월 5회 체크 |

### 급여제공 & 계획

| 기능 | 상태 | 비고 |
|------|------|------|
| **급여제공계획 통보 모니터링** (`GET /clients/care-plan-notifications/compliance`) | ✅ | **G38** · 5/11개월 경고 |
| **급여제공결과평가 (지표44)** (`GET/POST/PATCH /provision-result-evaluations*`) | ✅ | **G39** · 4-pillar compliance |
| **제공결과 dispatch 알림** (`POST /clients/{id}/notifications/care-provision-record`) | ✅ | **G39** 발송 UI |

---

## 14. 알림 & 채널 (Partial ✅)

| 기능 | 상태 | 비고 |
|------|------|------|
| **알림 채널 readiness** (`GET /notifications/channel-status`) | ✅ | **v1.1** · Solapi/SMTP/알림톡 상태 |
| **알림톡 템플릿 매니징** | ✅ | 9종 (출석·일일케어·청구·입금·급여제공·가정통신문·학대예방·긴급) |
| **알림 이력 조회** | ✅ | guardian·staff 조회 API |
| **Solapi 실연동** | 🟡 | **v2 P1** · stub → live 실연동 |
| **카카오 알림톡 발송** | 🟡 | **v2 P1** · template dispatch 검증 |
| **SMS Fallback** | 🟡 | **v2 P1** · 알림톡 실패 시 SMS 대체 |

---

## 15. 시스템 설정 & 감시 (Complete ✅)

| 기능 | 상태 | 비고 |
|------|------|------|
| 기술 설정 조회·수정 (`GET/PATCH /settings/system`) | ✅ | sysadmin |
| 감사 로그 조회 (`GET /settings/audit-logs`) | ✅ | 전 지점·자기 Tenant |
| 백업 상태·이력 (`GET /settings/backups`) | ✅ | 메타데이터 |

---

## 16. 프론트엔드 라우트 & 화면 (Complete ✅)

### 핵심 라우트

| 라우트 | 역할 | 상태 | 비고 |
|--------|------|------|------|
| `/` | 전체 | ✅ | 로그인·권한별 리다이렉트 |
| `/dashboard` | branch_admin+ | ✅ | 지점 대시보드 |
| `/dashboard/hq` | hq_admin | ✅ | 통합 대시보드 |
| `/platform` | platform_admin | ✅ | Tenant 관리 |
| `/clients*` | branch_admin+ | ✅ | 이용자 관리·상세 |
| `/attendance*` | caregiver+ | ✅ | 출석·수기·QR |
| `/guardian*` | guardian/client_user | ✅ | 보호자 포털 |
| `/billing*` | hq_admin/branch_admin | ✅ | 청구·명세·import |
| `/visits*` | social_worker+ | ✅ | 방문 일정 |
| `/programs*` | social_worker+ | ✅ | 프로그램 |
| `/meals*` | caregiver+ | ✅ | 식사 기록 |
| `/transport*` | social_worker+ | ✅ | 배차·이동경로 |
| `/staff*` | branch_admin+ | ✅ | 직원·교육·HR |
| `/nursing*` | caregiver+ | ✅ | **L03** 간호 기록 |
| `/care*` | caregiver+ | ✅ | **L02** 돌봄 기록 |
| `/compliance*` | branch_admin+ | ✅ | 규정준수·모니터링 |
| `/settings` | sysadmin | ✅ | 시스템 설정 |

### 라우트 수

- **Must + Should features**: **87개 라우트** ✅
- **반응형 설계**: 360px(모바일)~1200px(PC) ✅
- **접근성(a11y)**: WCAG 2.1 AA 정렬 진행 중

---

## 17. 테스트 커버리지

### 백엔드 (`mvn test`)

```
Classes: 1231 tests passing ✅
Coverage:
  - Unit Tests (JUnit 5): 컨트롤러·서비스·저장소
  - Integration Tests: Spring Boot 테스트 컨텍스트
  - E2E Pilot Tests: 주요 사용자 흐름 (결정 73)
```

### 프론트엔드 (Vitest + Playwright)

```
Components: 1393 tests passing ✅
E2E Suites:
  - Unit (Vitest): 컴포넌트·훅·유틸
  - Live E2E (Playwright): 실제 API 연동 (LIVE_E2E_* env)
  - Pilot E2E: 주요 업무 흐름 (개발 중)
```

---

## 18. 미구현·향후 계획

### v1.2 (Should)

| 기능 | 계획 | 비고 |
|------|------|------|
| **식단·일정 등록 API** | 기본 설계 완료 | Q161 · 관리자 입력 화면 |
| **라우트·이동 최적화** | 부분 완료 | v1.3-B suggest (OR-Tools) ✅, 경로 시각화 P2 |
| **대시보드 레이아웃 커스터마이징** | 설계 단계 | StatCard 그룹화 |
| **케어포 호환 import** | 파일럿 검증 후 | NHIS 엑셀 파서 정규화 |

### v2 (Could)

| 기능 | 계획 | 비고 |
|------|------|------|
| **Solapi live 알림톡·SMS** | 제공자 계약 필요 | stub 구현 완료 |
| **CMS 본인부담 자동이체** | 효성·FCMS 실연동 | stub 구현 완료 (Q206–Q208) |
| **간편결제 live PG** | 선택 필요 | 카카오페이·토스·나이스 평가 중 |
| **공단 포털 직접 전송** | 후속 협의 | MVP 제외 |
| **전자서명 고도화** | SMS 인증·공인인증 | v2 검토 |
| **모바일 앱** | 별도 프로젝트 | PWA 검토 중 |

---

## 19. 알려진 제약 & 미해결 항목

| 항목 | 상태 | 영향 | 계획 |
|------|------|------|------|
| **주민등록번호 암호화** | ✅ 구현 완료 | 규정준수 | - |
| **역할별 PII 마스킹** | ✅ 구현 완료 | 보안·규정준수 | - |
| **공단 엑셀 헤더 정규화** | ✅ 구현 완료 | 파일럿 센터 표본 필요 | 샘플 수집 대기 |
| **클라이언트 SSN 선택적 수집** | ✅ 구현 완료 | 법적 검토 | - |
| **Solapi live 배포** | 🟡 진행 중 | 실시간 알림 | v2 P1 |
| **효성 FCMS live** | 🟡 진행 중 | CMS 자동이체 | v2 기획 |
| **Live E2E 환경 구성** | ✅ 가이드 완료 | 배포 검증 | QA-B95 placeholder 정리 |

---

## 20. 성능 & 확장성

| 지표 | 목표 | 현재 | 비고 |
|------|------|------|------|
| API 응답시간 (p50) | <200ms | ~100–150ms | 데이터 인덱싱 ✅ |
| 데이터베이스 쿼리 | N+1 방지 | 대부분 eager loading | 관계 쿼리 최적화 진행 |
| 프론트엔드 번들 크기 | <500KB | ~450KB (gzip) | 트리 쉐이킹 적용 |
| 접근성 테스트 | WCAG 2.1 AA | ~95% 정렬 | 남은 항목 개선 중 |
| 테스트 커버리지 | >80% | ~85% | 엣지 케이스 추가 예정 |

---

## 🎯 현재 마일스톤

**develop 175차 (2026-06-16)**

✅ **L02_M07** 집중 배설·신체속박 기록  
✅ **V132 integrity** 데이터 일관성 검증  
✅ **health databaseStatusDetail** readiness probe  
✅ **live E2E placeholder guard** 자동 시뮤레이션 보호  

**다음 우선순위**:
1. **QA-B95** live E2E 환경 완전 정리
2. **v1.2 ROADMAP** P0 5건 로드맵 갱신
3. **알림톡 실연동** 준비 (v2 선행)

---

## 📞 연락처 & 피드백

- **문서 업데이트**: [PLAN_NOTES.md §[TWR]](planning/PLAN_NOTES.md)
- **구현 상태 확인**: develop branch 직접 확인 권장
- **버그 신고**: QA_FEEDBACK.md 또는 GitHub Issues

---

**작성자**: tech_writer 에이전트  
**마지막 갱신**: 2026-06-16 02:00 KST  
**유효 기간**: develop HEAD 현황 스냅샷 (실시간 아님)
