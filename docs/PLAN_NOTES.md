# 기획 메모 (PLAN_NOTES.md)

> **작성**: planner 에이전트  
> **최종 갱신**: 2026-06-06 (벤치마크 2차 조사 → 자동 기획 동기화)  
> **상태**: 초안 (사용자 승인 전)

---

## 사용자 입력 요약

주간보호센터 운영 관리 **앱/웹**을 구현한다.

| 항목 | 사용자 명시 |
|------|------------|
| 백엔드 | **Java** |
| 프론트엔드 | **React** |
| 추가 요청 | 타 주간보호센터 관리 웹 **벤치마킹 전담 에이전트** 추가 |
| 1주차 목표 | **관리자 대시보드 출력**까지 완료 |
| MVP v1 범위 | Must 전체: 인증, 이용자, 출석, 건강기록, 대시보드 |
| 레거시 코드 | `src/backend`(Python/FastAPI) **전부 폐기**, Java 신규 시작 |
| 기술 세부 | Spring Boot 3.x, Vite+React, PostgreSQL, JWT+RBAC |
| 출석 방식 | **수기 + QR 모두** 지원 |
| 운영 모델 | **다지점** — 지점별 관리 + 통합 관리 구분 |
| MVP 역할 | **6개 역할 전부** 별도 UI·권한으로 구현 |
| hq_admin 쓰기 | `active_branch_id` 선택 시 해당 지점만 CRUD (B방식) |
| QR 스캔 | **B방식** — 보호자/이용자가 지점 QR 스캔 (A방식은 MVP 제외) |
| 사업 모델 | **전국 판매 B2B SaaS** (개인용 아님) |
| 1주차 범위 | 6역할 로그인·화면·권한 **전부** 포함 (골격만 X) |
| QR 계정 정책 | **안 3** — guardian + client_user(센터별 on/off) |
| 배포 클라우드 | **벤더 무관** |
| 목표 일정 | **일정 무관** (런칭 시점 제약 없음) |
| 파일럿 센터 | **있음** — 실제 운영 센터에서 테스트 |
| 신규 고객 등록 | **확정: A** — ogada 직원 (`platform_admin`, `/platform`) |
| 청구·정산 | **MVP v1 포함** (케어포 벤치마킹 기반 2단계 모델) |
| 벤치마킹 참고 | **케어포** (carefor.co.kr) |
| 파일럿 인원 | 센터장 1 + 요양보호사 5, **지점 2곳** |
| 수가표 관리 | **B방식** — `hq_admin`이 화면에서 등급별·연도별 수가 입력·관리 (코드 고정 X) |
| 본인부담률 | **이용자별 구분 관리** — 일반15%/감경9%/감경6%/기초수급0%, 테이블화 |

---

## 확인된 결정 사항

1. **기술 스택 변경**: `.agents/agents.yaml` 초기 설정(Python/FastAPI + Vanilla JS) 대신 **Java 백엔드 + React 프론트엔드**로 진행한다.
2. **도메인**: 주간보호센터 운영 관리 (이용자·출석·건강·청구 등).
3. **플랫폼**: 웹 기반, 모바일·PC 반응형 (기존 요구사항 유지).
4. **벤치마킹 에이전트**: 경쟁·유사 서비스 분석을 기획 단계에 포함한다. (`benchmark_researcher` — agents.yaml·run_agent.py 반영 완료, 3시간 loop)
5. **1주차 완료 목표** (2026-06-05 확정): 로그인 → 이용자·출석·건강 데이터 입력 → **관리자 대시보드(`/dashboard`) 실데이터 출력**까지.
6. **MVP v1 기능 범위** (2026-06-05 확정): Must 5개 모듈 전부 포함 — 인증, 이용자 관리, 출석 관리, 건강 기록, 관리자 대시보드. Should/Could는 v1 이후.
7. **레거시 코드 처리** (2026-06-05 확정): 기존 `src/backend`(Python/FastAPI) **전부 폐기**. Java 백엔드로 신규 구현. 마이그레이션·병행 없음.
8. **기술 스택 세부** (2026-06-05 확정): Spring Boot 3.x, Vite+React(SPA), PostgreSQL, JWT+RBAC.
9. **출석 방식** (2026-06-05 확정): 수기 체크인/아웃 **와** QR 코드 체크인/아웃 **모두** MVP에 포함. `check_in_method`로 구분.
10. **다지점 운영** (2026-06-05 확정): 여러 지점 운영 전제. **지점별 관리**(Branch Scope)와 **통합 관리**(HQ Scope) 체계 분리. MVP에 Organization-Branch 계층·이중 대시보드 포함.
11. **MVP 역할 범위** (2026-06-05 확정): `hq_admin`, `branch_admin`, `social_worker`, `caregiver`, `guardian`, `sysadmin` **6개 역할 모두** 별도 화면·메뉴·권한으로 구현.
12. **hq_admin 쓰기 권한** (2026-06-05 확정): 전 지점 조회·집계 기본, **수정·등록은 `active_branch_id` 선택 시 해당 지점만** (B방식).
13. **QR 출석 방식** (2026-06-05 확정): **B방식** — 보호자/이용자가 **지점 입구 QR**을 스캔. 수기(직원)와 병행. A방식(직원이 이용자 QR 스캔)은 MVP 제외.
14. **사업 모델** (2026-06-05 확정): **전국 판매용 B2B SaaS**. 고객 1법인 = Organization(Tenant). 테넌트 간 데이터 완전 격리.
15. **1주차 완료 범위** (2026-06-05 확정): 6역할 로그인·메뉴·권한·홈 화면 **전부** 1주차 완료 기준에 포함.
16. **QR 스캔 계정 정책** (2026-06-05 확정): **안 3** — `guardian` 항상 + `client_user`(이용자 본인) 조건부, Organization `allow_client_self_checkin` 설정.
17. **배포 클라우드** (2026-06-05 확정): AWS/GCP/NCP 등 **벤더 무관**, 구현 단계에서 선택.
18. **목표 런칭 일정** (2026-06-05 확정): **일정 무관** — 특정 출시 데드라인 없음.
19. **파일럿 운영 센터** (2026-06-05 확정): **있음** — 실제 운영 센터에서 테스트·피드백 수집 예정.
20. **신규 고객 등록** (2026-06-05 확정): **A — ogada 직원** (`platform_admin`). `/platform` 화면 MVP 포함.
21. **청구·정산** (2026-06-05 확정): MVP v1 **포함** (급여 계산, 월별 청구서).
22. **파일럿 현장 사용** (2026-06-05 확정): 지점 **2곳**, 센터장 **1명**, 요양보호사 **5명**.
23. **벤치마킹 참고 서비스** (2026-06-05): **케어포** (사용자 지정). 이지케어·엔젤시스템·롱텀 비교 조사 (REQUIREMENTS §1-5).
24. **청구 MVP 방식** (2026-06-05 확정): 케어포식 2단계 (내부계산+엑셀import).
25. **파일럿 참여 역할** (2026-06-05 확정): 센터장 + 요양보호사만.
26. **수가표 관리 방식** (2026-06-05 확정): **B방식** — `hq_admin`이 화면에서 등급별·연도별 수가를 입력·수정. 코드 고정 금지, 버전 이력 보존. (`fee_schedules` 엔티티)
27. **본인부담률 관리** (2026-06-05 확정): **이용자별 구분 저장** — 일반 15% / 감경 9% / 감경 6% / 기초수급 0%. 비율은 테이블화(`copay_rates`)하고 이용자는 구분 코드(`clients.copay_type`) 보유. 청구 계산 시 이용자별 비율 적용.
28. **주민등록번호 처리** (2026-06-05 확정): **수집함**. 근거 = 공단 청구명세서 법정 필수 항목(노인장기요양보험법 시행규칙). 정책 = ① 암호화 저장(PIPA §24-2) ② 화면·목록·로그 마스킹 ③ 별도 수집·이용 동의 ④ 청구·법정 목적 외 사용 금지·접근 audit_log. (REQUIREMENTS §3-2-1)

---

## 제안: 벤치마킹 에이전트 (`benchmark_researcher`)

| 항목 | 내용 |
|------|------|
| 역할 | Competitive Research / Benchmark Analyst |
| 목적 | 국내외 주간보호·요양기관 관리 웹/앱의 기능·UX·가격·차별점을 조사해 기획·설계에 반영 |
| 주요 산출물 | `docs/BENCHMARK_REPORT.md`, `docs/COMPETITOR_MATRIX.md`, `memory/decisions.md` (벤치마킹 기반 결정) |
| 협업 시점 | Phase 1(기획) 선행 또는 병행 — REQUIREMENTS·USER_STORIES·DESIGN_SYSTEM 작성 전 |
| 조사 관점 | 핵심 기능 커버리지, 보호자 포털 UX, 출석·건강 기록 흐름, 알림 연동, 청구/급여 모듈, 접근성·모바일 UX |

> **참고**: `benchmark_researcher` 에이전트가 `docs/BENCHMARK_REPORT.md`, `docs/COMPETITOR_MATRIX.md` 를 유지하고, planner(build --role planner)가 이를 읽어 기획을 갱신한다. 3시간 loop: `./scripts/agent_planning_start.sh`

---

### DB 설계 질문 (db_architect, 2026-06-05)

V1–V17 커버리지 점검 중 식별한, **DB로 강제하지 않고 애플리케이션/테스트에 위임**하기로 결정한 항목. 정책 확정 시 제약 추가 검토.

1. **`users.active_branch_id` ∈ `user_branches`** — 현재 V8은 활성 지점이 동일 Tenant인지만 FK로 보장한다. "사용자가 실제 배정받은 지점만 활성화" 규칙은 DB로 강제하지 않았다. 사유: `hq_admin`이 `user_branches` 행 없이 전 지점 활성화하는 운영 모델(전 지점 묵시적 접근)인지, 명시적 배정 모델인지 미확정. **coder는 `POST /auth/active-branch`에서 토큰 `branch_ids` 내 값만 허용**하도록 검증. 명시적 배정 모델로 확정되면 `(user_id, active_branch_id) → user_branches` 복합 FK 추가.
2. **`billing_claim_items` 라인 산술 ↔ 스냅샷 비율** — V6은 행 단위 `total = nhis + copay`만 보장한다. `copay_amount = round(total_amount × copay_rate_snapshot)`, `total_amount = daily_rate_snapshot × attendance_days`의 정확한 반올림은 CHECK로 강제하지 않았다(반올림 규칙 충돌 위험). **coder는 청구 계산 서비스에서 단일 반올림 규칙(예: `RoundingMode.HALF_UP`, 원 단위)을 적용하고 tester가 회귀 테스트로 검증**. 확정 반올림 규칙은 §3-9-2 보강 시 문서화.
3. **`nhis_import_rows` 매칭 이용자의 지점 일치** (2026-06-06, V21 마감) — V21 `trg_nhis_rows_client_branch`로 `client_id` 설정 시 `clients.branch_id = nhis_import_batches.branch_id`를 DB에서 강제한다. V21 `trg_nhis_batches_claim_branch`로 배치↔청구 연결 시 지점도 일치. **가정**: ogada는 지점 단위 import·reconciliation(파일럿 2지점). 공단 엑셀이 **법인(Tenant) 단위 일괄**로 확정되면 V21 #4 트리거 완화 또는 `branch_id` 비정규화 검토(추가질문 27).
4. **`nhis_import_rows.organization_id` 자동 복사** (2026-06-06, V22) — V22 `trg_nhis_import_rows_set_org`가 부모 배치에서 Tenant를 자동 설정(V21 청구 라인 패턴). 앱은 여전히 명시 설정 권장.
5. **`guardian_clients.organization_id` 자동 복사** (2026-06-06, V23) — V23 `trg_guardian_clients_set_org`가 연결 `clients`에서 Tenant 자동 설정. 보호자 연결 INSERT 시 앱이 `organization_id`를 생략해도 FK·QR 스캔 Tenant 검증과 정합.
6. **청구 라인 출석일·금액 쌍 CHECK** (2026-06-06, V24) — V23 `chk_billing_claim_items_positive_days`(`total > 0 → days ≥ 1`)와 V24 `chk_billing_claim_items_days_implies_amount`(`days ≥ 1 → total > 0`)로 DB 레벨 쌍방 방어. 반올림·산술 정확성은 여전히 앱·테ster 책임(항목 2).
7. **NHIS import `ltc_cert_no` 공백 CHECK** (2026-06-06, V25) — V25 `chk_nhis_import_rows_ltc_cert_nonempty`가 NULL·공백 문자열 행을 DB에서 거부. 엑셀 파서는 앱에서 빈 행 skip 권장.
8. **`billing_claim_items` 청구서당 1라인 UK** (2026-06-06, V26) — V26 `uq_billing_claim_items_claim_client`가 `(claim_id, client_id)` 중복을 DB에서 거부. `BillingService.generateClaim`은 이용자당 1행만 생성하며, NHIS reconciliation의 `findByClaimIdAndClientId` 전제와 일치. 수동 SQL·버그로 인한 중복 라인 방어.
9. **V2 중복 UK 정리** (2026-06-06, V27) — V2 `uq_claim_item_client`와 V26 `uq_billing_claim_items_claim_client`가 동일 컬럼 UK. V27에서 V2 이름 제거, V26 이름만 유지.
10. **cross-tenant 이메일 로그인 인덱스** (2026-06-06, V28) — `idx_users_email_lower`가 `findAllByEmailIgnoreCase`를 지원. 동일 이메일 다중 Tenant 계정은 **앱에서 거부**(`AuthService` BusinessRuleException) — DB UK는 `(organization_id, email)` Tenant 스코프만. 전역 이메일 UK는 SaaS 다 Tenant 동일 이메일 정책 미확정으로 DB 강제하지 않음.
11. **NHIS 배치 행 정렬 인덱스** (2026-06-06, V28) — `idx_nhis_import_rows_batch_created`가 import 응답 행 순서를 지원. `(batch_id, ltc_cert_no)` UK는 엑셀 중복 행 허용을 위해 추가하지 않음 — reconciliation UI는 앱에서 중복 표시.
12. **user_branches user_id 역조회** (2026-06-06, V29) — `idx_user_branches_user_id`가 `findByUserId`/`findByUserIdIn`을 지원. V25 `(branch_id, user_id)`는 `GET /users?branchId=` 지점 필터 전용.
13. **플랫폼 사업자번호 검색** (2026-06-06, V29) — `idx_organizations_business_no_trgm`이 `businessNoContainingIgnoreCase`를 지원. exact match는 `organizations.business_no` UK(V1).
14. **청구 라인 claim_id 정렬** (2026-06-06, V29) — `idx_billing_claim_items_claim_created`가 `findByClaimIdOrderByCreatedAtAsc`를 지원. V2 `idx_billing_claim_items_claim` 대체; Tenant 스코프 조회는 V27 `(organization_id, claim_id, created_at)` 병행.
15. **Tenant 이메일 case-insensitive UK** (2026-06-06, V30) — V30 `uq_users_org_email_lower`가 `(organization_id, lower(email))` UK로 V1 case-sensitive `uq_user_email_per_org`를 대체. **coder는 `users.email` 저장 시 trim+소문자 정규화 권장** — DB UK와 앱 `existsByOrganizationIdAndEmailIgnoreCase` 정합. cross-tenant 로그인은 V28 `idx_users_email_lower` + 앱 단일 active 계정 검증 유지.
16. **비밀번호 변경 refresh 폐기** (2026-06-06, V30) — V30 `idx_refresh_tokens_user_active`가 `(user_id) WHERE revoked_at IS NULL` partial 인덱스. **현재 `AuthService.resetPassword`는 refresh 미폐기** — 보안 강화 시 `revokeAllActiveForUser(userId)` 추가 권장(V30 인덱스 활용). password_reset_tokens는 V28 `idx_password_reset_tokens_user_active` 기존 패턴.
17. **청구 목록 status 필터 인덱스** (2026-06-06, V31) — V31 `idx_billing_claims_org_branch_status_generated`가 `(organization_id, branch_id, status, generated_at DESC)` 지원. API_SPEC §7-3 상태 필터는 **coder가 `BillingClaimRepository`·`BillingService.listClaims`에 status 쿼리 파라미터 추가** 시 활용.
18. **청구 상태 이력 no-op CHECK** (2026-06-06, V31) — V31 `chk_claim_status_history_distinct_transition`이 `from_status = to_status` 이력 INSERT를 DB에서 거부. `trg_billing_claims_status_history`(V10/V21)는 실제 전이만 적재하므로 기존 데이터 무영향.
19. **대표 보호자 partial 인덱스** (2026-06-06, V31) — V31 `idx_guardian_clients_org_client_primary`가 `clearPrimaryForClient` UPDATE 스캔 지원. UK `uq_guardian_clients_primary`(V7)와 병행.
20. **`attendance.created_by` 미설정** (2026-06-06, V31 점검 → **V32 마감**) — V32 `trg_attendance_set_created_by`가 `ogada.actor_user_id` 세션 변수로 INSERT 시 `created_by` 자동 적재. **coder는** `AttendanceService` check-in/absence/QR 트랜잭션에서 `DbSessionContext.setActorUserId` 호출(청구 status PATCH와 동일). DB NOT NULL CHECK는 세션 미설정 legacy 행 허용을 위해 보류.
21. **`billing_claims.generated_by` 미설정** (2026-06-06, V32) — V32 `trg_billing_claims_set_generated_by`가 session actor로 INSERT 시 자동 적재. **coder는** `BillingService.generateClaim`에서 `dbSessionContext.setActorUserId` 호출 권장.
22. **NHIS COMPLETED `imported_at` backstop** (2026-06-06, V32) — V32 `trg_nhis_batches_set_imported_at`가 COMPLETED + NULL `imported_at` 시 `created_at`/NOW() 설정. JPA `@PrePersist`와 병행; raw SQL 방어.
23. **퇴소 purge 인덱스** (2026-06-06, V32) — `idx_clients_org_discharged_at` partial 인덱스. retention 배치 구현 시 Tenant 스코프 cutoff 쿼리 활용.
24. **건강·NHIS actor backstop** (2026-06-06, V33) — V33 `trg_health_records_set_recorded_by`·`trg_nhis_batches_set_imported_by`가 session `ogada.actor_user_id`로 NULL actor 컬럼 자동 적재. `HealthRecordService`·`NhisImportService`는 앱에서 JWT subject 설정하나 V32 출석 패턴과 동일하게 DB 방어. **coder는** `DbSessionContext.setActorUserId`를 출석·청구·건강·NHIS 쓰기 트랜잭션 공통 호출 권장.
25. **퇴소 child purge 인덱스** (2026-06-06, V33) — V33 `idx_attendance_client_purge`·`idx_health_records_client_purge`·`idx_billing_claim_items_client_purge`가 `client_id IN (discharged cohort)` bulk DELETE/익명화 스캔 지원 (DATA_RETENTION §4-1).
26. **활성 이용자 목록 pagination** (2026-06-06, V33) — V33 `idx_clients_org_branch_active_created` partial 인덱스. `ClientRepository.searchByScope` query=null 시 branch+active 필터 + created_at 정렬.
27. **이용자 생애주기 정합 + 지점 단위 retention purge** (2026-06-06, V34) — V5 `chk_clients_discharge_active`(`discharged_at IS NULL OR is_active = FALSE`)와 V34 `chk_clients_discharged_after_created`(`discharged_at >= created_at`)가 쌍을 이뤄 `clients.is_active` ↔ `discharged_at` 양방향 무결성을 완성한다. `ClientService.discharge()`는 두 컬럼을 동시 적재(`setActive(false) + setDischargedAt(NOW())`)하므로 항상 통과. **coder가 추후** 일괄 reactivation·backfill 스크립트를 추가하면 CHECK가 1차 방어. 또한 V34 `idx_clients_org_branch_discharged_at` partial 인덱스가 지점 단위 retention purge(지점 폐쇄·부분 Tenant rollback) 시 cohort 선정 비용을 낮춤 — Tenant 스코프(V32 `idx_clients_org_discharged_at`)와 병행.

### 추가 질문

다음 항목이 확정되기 전까지 상세 스펙·일정·구현 범위는 가정으로만 기재한다.

#### 타겟·운영 범위

1. ~~**대상 센터 규모**~~ → **확정**: **다지점** 운영, 지점별·통합 관리 구분
2. ~~**MVP 사용자**~~ → **확정**: 6개 역할 **전부** 별도 UI·권한 구현
3. ~~**파일럿 운영 센터**~~ → **확정**: **있음**
3-1. ~~파일럿 인원·지점~~ → **확정**: 지점 2, 센터장 1, 요양보호사 5
3-2. ~~파일럿 참여 역할~~ → **확정**: **센터장(`branch_admin`) + 요양보호사(`caregiver`)만**
4. ~~**규모 가정**~~ → **가정 확정**: 전국 SaaS 기준 1년차 ~50법인/~150지점, 3년차 ~500법인/~2,000지점 (REQUIREMENTS §1-2)
5. ~~**hq_admin 쓰기 권한**~~ → **확정**: `active_branch_id` 선택 시 해당 지점 CRUD (B방식)
6. ~~**신규 고객 등록**~~ → **확정**: **A — ogada 직원** (`platform_admin`)

#### 기술 스택 세부

7. ~~**Java 프레임워크**~~ → **확정**: Spring Boot 3.x
8. ~~**React 구성**~~ → **확정**: Vite + React (SPA)
9. ~~**데이터베이스**~~ → **확정**: PostgreSQL
10. ~~**인증 방식**~~ → **확정**: JWT + RBAC (지점 스코프)
11. ~~**기존 `src/backend` 처리**~~ → **확정**: 전부 폐기, Java 신규 시작

#### 기능·우선순위

12. ~~**MVP 기능 범위**~~ → **확정**: Must 전체 + 다지점·조직 관리
13. ~~**청구·정산 v1**~~ → **확정**: MVP v1 **포함**
13-1. ~~청구 MVP~~ → **확정**: 케어포 동일 (**내부계산+명세서+공단엑셀import**)
14. **보호자 알림** 채널 우선순위는? (카카오 알림톡 / SMS / 앱 푸시) — MVP v1 제외
15. ~~**QR 출석**~~ → **확정**: 수기 + QR **모두** MVP 포함
16. ~~**QR 스캔 주체**~~ → **확정**: **B방식** (보호자/이용자 → 지점 QR). A방식 MVP 제외
17. ~~**QR 스캔 계정 정책**~~ → **확정**: **안 3** (`guardian` + `client_user`, `allow_client_self_checkin` on/off)

#### 벤치마킹

18. ~~**벤치마킹 참고**~~ → **확정**: **케어포** (carefor.co.kr). §1-5 1차 조사 반영
19. 벤치마킹 시 **가장 중시하는 비교 축**은? (기능 완성도 / UX / 가격 / 규정 준수 / 모바일 UX)
20. **국내 장기요양 포털·공단 시스템**과의 연동·호환 요구가 있나?

#### 비기능·제약

21. ~~**배포 클라우드**~~ → **확정**: 벤더 **무관** (구현 단계 선택)
22. ~~**동시 접속 규모**~~ → **가정 확정**: 1년차 ~500 / 3년차 ~5,000 (REQUIREMENTS §1-2)
23. **개인정보·의료 데이터** 보관 기간·암호화 정책에 센터 내부 규정이 있나?
24. ~~**예산·일정**~~ → **확정**: 목표 런칭 **일정 무관**
25. **접근성·다국어** 요구는 한국어 단일 + WCAG 2.1 AA로 충분한가?

#### 빌드 전 잔여 공백 (2026-06-05 신규 식별)

26. ~~**청구·정산 계산 규칙 구체화**~~ → **확정** (2026-06-05):
    - 수가 = **관리자 입력 테이블(B방식)**, `hq_admin` 관리, 연도별 버전 (§3-9-1)
    - 본인부담률 = **이용자별 구분**(일반15%/감경9%·6%/기초수급0%) (§3-9-2)
    - 가산·식대·비급여: 수가표 부가 항목으로 **선택 입력** 가능하게 구조화 (세부 항목은 구현 시 확정)
27. **공단 청구내역상세 엑셀 포맷**: import할 엑셀의 실제 컬럼 스펙(샘플 파일) 확보 필요. 없으면 v1은 표준 컬럼 가정으로 진행.
28. ~~**PII 암호화 대상 컬럼 확정**~~ → **확정** (2026-06-05): 주민번호 **수집** + 암호화·마스킹·별도동의 (결정 28, REQUIREMENTS §3-2-1).
    - **경쟁사·법령 조사 (2026-06-05)**: 경쟁사(케어링 등)는 수급자 **주민등록번호를 필수 수집**. 이유는 **노인장기요양보험법 시행규칙상 청구명세서에 "수급자 성명 및 주민등록번호" 기재가 법정 필수**이기 때문. 개인정보보호법 §24-2: **암호화 보관 의무**.
    - **케어포 수급분류 실제**: `일반(15%) / 경감·의료(7.5%) / 기초(0%)` — `copay_rates` 테이블로 대응.
    - ~~잔여: 추가 암호화 대상 범위~~ → **확정** (2026-06-05): 주민번호 **암호화 필수**, 연락처·주소 **암호화 권장**, 인정번호·등급·copayType **평문**, 건강·투약은 TLS+접근통제. build 가이드로 REQUIREMENTS §3-2-1에 박음.
29. ~~**미작성 기획 산출물**~~ → `docs/API_SPEC.md` **초안 작성 완료** (2026-06-05). `docs/FLOWCHART.md` **작성 완료** (2026-06-05).

---

---

## 다음 액션 (사용자 승인 대기)

1. ✅ **CHANGELOG** — V29–V31 마이그레이션, 비밀번호 재설정 refresh 폐기·청구 status 필터 gap 반영 (2026-06-06)
2. ✅ **FAQ** — V29–V31 Q&A 추가 (Q64–Q68: 이메일 UK·재설정 세션·청구 필터·대표 보호자, 2026-06-06)
3. ✅ **USER_MANUAL** — 대표 보호자·비밀번호 재설정 세션·청구 상태 필터(예정)·이메일 UK 반영 (2026-06-06)
4. ✅ **ADMIN_GUIDE** — 사업자번호 검색·Tenant 이메일 UK·비밀번호 재설정 보안 (2026-06-06)
5. ✅ **DEPLOYMENT_GUIDE** — Flyway V29–V31·테스트 21클래스 반영 (2026-06-06)
6. 프론트엔드 개발 시작 우선순위: ① 로그인·JWT ② 이용자 목록 ③ 수기 출석 ④ 건강 기록 ⑤ 청구서 ⑥ 대시보드
7. coder 후속: `GET /billing/claims?status=` API 파라미터 (V31 인덱스 활용, API_SPEC §7-3)
8. 파일럿 준비: 지점 2곳, 센터장 1명, 요양보호사 5명 참여 (실제 운영 센터)
9. 요구사항 사용자 승인 (`<!-- approved-by-user: true -->` — REQUIREMENTS.md, USER_STORIES.md)

---

*이 문서는 tech_writer 에이전트가 관리합니다. 변경 시 `memory/decisions.md`에 이력을 남겨주세요.*
<!-- modified-by-tech-writer: 2026-06-06 -->
