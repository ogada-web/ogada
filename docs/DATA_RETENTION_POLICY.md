<!-- doc:owner=DBA doc:audience=COD,PLN,TSR updated=2026-06-06T12:00:00+09:00 -->
# 데이터 보존·파기 정책 (DATA_RETENTION_POLICY.md)

> **작성**: db_architect 에이전트  
> **최초 작성일**: 2026-06-05  
> **상태**: MVP v1 기준 (법령·센터 내부 규정 확정 전 운영 가이드)  
> **근거**: `docs/REQUIREMENTS.md` §3-2-1, §4, 개인정보보호법(PIPA), 노인장기요양보험법

---

## 1. 목적·범위

| 항목 | 내용 |
|------|------|
| 적용 대상 | ogada SaaS가 처리하는 Tenant(Organization) 전체 데이터 |
| 목적 | 최소 수집·최소 보관, 법정 보존 준수, 퇴소·해지 시 파기 절차 명확화 |
| 책임 | Tenant `hq_admin`·`sysadmin` — 운영 정책 확인, ogada — 플랫폼 기술 보존·백업 |

---

## 2. 데이터 분류

| 분류 | 예시 테이블·컬럼 | 보안 처리 |
|------|------------------|-----------|
| 고유식별정보 | `clients.resident_registration_no_encrypted` | **동의 후 암호화 저장**, 미동의 시 NULL, 마스킹 표시, 복호화 audit |
| 준식별정보 | `clients.phone_encrypted`, `address_encrypted`, `branches.phone_encrypted` | **암호화 권장**, 부분 마스킹 |
| 민감정보 | `health_records` (건강·투약·낙상) | TLS 전송, RBAC, audit |
| 운영 식별자 | `ltc_cert_no`, `copay_type`, UUID | 평문 (검색·청구 키) |
| 인증 정보 | `users.password_hash`, `refresh_tokens` | 해시·토큰 hash, 만료·폐기 |
| 감사·로그 | `audit_logs`, `login_history` | PII 마스킹, 내부 UUID 위주 |
| 청구·회계 | `billing_claims`, `billing_claim_items`, `nhis_import_*` | Tenant 격리, 확정 후 불변 |
| 백업 메타 | `backup_runs`, `organizations.backup_enabled` | Tenant별 백업 이력 (API §9) |

---

## 3. 보존 기간 (기본값)

> 법령·계약이 상이하면 **긴 기간 우선**. 센터별 내부 규정은 Tenant 설정으로 추후 확장 가능.

| 데이터 유형 | 보존 기간 | 근거·비고 |
|-------------|-----------|-----------|
| 이용자 기본정보(PII 포함) | **퇴소 후 5년** | 장기요양·회계 증빙 일반 관행; 법정 최소 확인 후 조정 |
| 출석·건강·투약 기록 | **퇴소 후 5년** | 급여 제공 기록·분쟁 대응 |
| 청구서·명세·공단 import | **청구 연도 기준 5년** | 세무·회계 보존 관행 |
| 수가표·본인부담률 이력 | **영구(또는 10년)** | 과거 청구 재현·감사 |
| 감사 로그 (`audit_logs`) | **3년** (기본 `organizations.audit_retention_days=1095`, 30–3650 조정 가능) | 보안·개인정보 접근 추적 — `idx_audit_logs_org_created` |
| 로그인 이력 | **1년** | 보안 모니터링 — `idx_login_history_created`(V15)로 purge 스캔 |
| refresh·비밀번호 재설정 토큰 | **만료 즉시·최대 30일** | 기술적 최소 보관 — `idx_refresh_tokens_expires`·`idx_password_reset_tokens_expires`(V14)로 만료 스캔; 폐기(`revoked_at`) 후 30일 purge는 `idx_refresh_tokens_revoked`(V15); **사용(`used_at`) 후 7일** purge는 `idx_password_reset_tokens_used`(V16) |
| 지점 QR 토큰 | **유효일 종료 후 7일** | 운영·분쟁 조회 후 삭제 — `idx_branch_qr_tokens_expires`(V13)로 만료 스캔 |
| 알림 발송 이력 (`notifications`) | **1년** | v1 이후 채널 연동 시 — `idx_notifications_created`(V15)로 purge 스캔 |
| DB·애플리케이션 백업 | **일 1회, 30일 롤링** | REQUIREMENTS §4 비기능; `backup_runs`에 실행 메타 기록 |
| 백업 실행 이력 (`backup_runs`) | **90일** (메타) | `storage_location`·`size_bytes` 등; 실제 스냅샷은 30일 롤링과 연동 — purge 스캔 `idx_backup_runs_created`(V16). 종료 상태(`SUCCESS`/`FAILED`)는 `completed_at` 필수(V20)이므로 purge 컷오프는 `completed_at` 기준 가능; `FAILED`는 `error_message` 함께 보존(V20) |
| 퇴소·비활성 계정 | **동일 기간 후 파기 배치** | `is_active=false` ≠ 즉시 삭제 |

---

## 4. 파기·익명화 절차

### 4-1. 이용자 퇴소 (`clients.discharged_at` 설정)

1. 퇴소 즉시: UI 목록에서 비활성(`is_active=false`), 신규 출석·건강 입력 차단.
2. 보존 기간 경과 후 배치(`discharged_at` 기준, `idx_clients_org_discharged_at` V32 스캔):
   - PII 컬럼: NULL 또는 토큰화·익명화 (이름 → `퇴소이용자-{내부ID}`).
   - `resident_registration_no_encrypted` **완전 삭제**.
   - 사진 스토리지 객체 삭제.
3. 출석·건강·청구·보호자 연결: 법정 보존 기간까지 유지 후 집계용 통계만 남기고 상세 삭제(정책 확정 시). purge 시 `idx_attendance_client_purge` / `idx_health_records_client_purge` / `idx_billing_claim_items_client_purge`(V33) / `idx_guardian_clients_client`(V2)로 `client_id IN (…)` 일괄 삭제·익명화. `guardian_clients`는 `ON DELETE CASCADE`이므로 이용자 행 **물리 삭제** 시 자동 제거; 익명화(행 유지) 시에는 연결 행을 앱·배치에서 명시 삭제.

### 4-2. Tenant(Organization) 해지

1. `organizations.is_active=false` → 전 계정 로그인 차단.
2. **90일 유예** (데이터 반출·분쟁 대응).
3. 유예 후: Tenant 스코프 데이터 논리 삭제 → 백업 보존 기간(30일) 경과 후 물리 삭제.
4. `platform_admin` 감사 로그에 해지·파기 이벤트 기록.

### 4-3. 계정·토큰

| 대상 | 파기 조건 |
|------|-----------|
| `refresh_tokens` | 만료 또는 로그아웃 시 `revoked_at` 설정, 30일 후 물리 삭제 |
| `password_reset_tokens` | `used_at` 또는 만료 후 7일 내 삭제 |
| `users` 퇴직 | `is_active=false`, 1년 후 이메일 익명화(재가입 UK 충돌 방지) |

---

## 5. 백업·복구

| 항목 | 정책 |
|------|------|
| 주기 | **일 1회** 전체 DB 스냅샷 (REQUIREMENTS §4) |
| 보관 | **30일** 롤링 (클라우드 스토리지) |
| 암호화 | 백업 파일 at-rest 암호화 (KMS·환경변수 키) |
| 복구 RTO/RPO | RPO 24시간, RTO 4시간 (목표 — 인프라 구현 시 확정) |
| Tenant 복구 | `sysadmin` 요청·`audit_logs` 기록 후 ops 절차 |
| 백업 내 PII | 운영 DB와 동일 암호화 상태 유지, 백업 접근 권한 최소화 |

---

## 6. 로그·감사

- 로그에 주민번호·전체 전화번호 **기록 금지** — `client_id`, `user_id` UUID 사용.
- `audit_logs` 필수 기록:
  - PII 복호화 열람
  - 청구 확정·상태 변경
  - Tenant·지점·권한 변경
  - 대량 export·NHIS import
- `sysadmin`: `/settings/audit-logs` 조회, **삭제 불가**(append-only).

---

## 7. 교차 테넌트·접근 통제

- 쿼리·API에 `organization_id` **강제** — 타 Tenant 데이터 조회·파기 명령 불가.
- `platform_admin`: Tenant 메타데이터만, 이용자 PII 기본 비접근.
- 데이터 반출: Tenant `hq_admin` 승인 + audit, 암호화 파일·만료 링크 권장.

---

## 8. 구현 메모 (coder)

| 항목 | 권장 구현 |
|------|-----------|
| 파기 배치 | Spring `@Scheduled` + `purged_at` / `retention_until` 컬럼 (v2+) |
| 암호화 | AES-GCM, 키는 환경변수·KMS — rules.md §3 |
| 백업 API | `GET /settings/backups` — `backup_runs` 조회; 백업 잡 성공/실패 시 INSERT. 종료 시 `completed_at` 반드시 채우고 `FAILED`는 `error_message` 동반(V20 CHECK). `SUCCESS`로 INSERT/UPDATE 시 `error_message`는 반드시 NULL |
| 청구 상태 이력 | `PATCH /billing/claims/{id}/status` 전 `SET LOCAL ogada.actor_user_id` — V10/V21 트리거가 `billing_claim_status_history`에 `organization_id`·`changed_by` 자동 기록 |
| 퇴소 후 출석 | `POST /clients/{id}/discharge` 후 해당 이용자 `attendance` INSERT는 DB 거부 (V10) — UI에서 목록 제외 권장 |
| 퇴소 후 건강 | 동일하게 `health_records` INSERT 거부 (V13) — 기존 이력 UPDATE는 허용 |
| 동의 | `consent_collected_at`·주민번호 컬럼 모두 NULL 허용(2단계 등록). 동의 후에만 RRN 저장 (`chk_clients_rrn_consent`, `chk_clients_rrn_pair` — encrypted/masked 쌍 규칙) |
| guardian/client_user 연결 | `guardian_clients`·`clients.user_id` INSERT/UPDATE 시 역할 CHECK 트리거(V13) — 잘못된 역할 계정 연결 차단 |
| guardian_clients Tenant | `guardian_clients.organization_id`는 **연결 `clients`에서 복사** — V23 트리거가 자동 설정 (V5 Tenant FK 보완) |
| 결석 출석 | `POST /attendance/absence` — `check_out_at`·`transport_type` NULL, `check_in_method=manual` (V14 CHECK) |
| actor Tenant FK | `created_by`·`recorded_by`·`generated_by`·`imported_by`는 JWT `organization_id`와 일치하는 사용자만 (V14 복합 FK) |
| actor 자동 적재 | V32 `trg_attendance_set_created_by`·`trg_billing_claims_set_generated_by`·V33 `trg_health_records_set_recorded_by`·`trg_nhis_batches_set_imported_by`·V35 `trg_fee_schedules_set_created_by`·`trg_branch_qr_tokens_set_created_by` — 쓰기 트랜잭션에서 `DbSessionContext.setActorUserId` 호출 시 NULL actor 컬럼 자동 채움 |
| 퇴소 purge 스캔 | `@Scheduled` + `idx_clients_org_discharged_at`(V32) — Tenant별 `discharged_at IS NOT NULL AND discharged_at < cutoff`; 자식 행은 V33 `idx_*_client_purge`로 `client_id IN (…)`. **지점 단위** 정리(지점 폐쇄·부분 rollback)는 V34 `idx_clients_org_branch_discharged_at`로 `(organization_id, branch_id, discharged_at < cutoff)` |
| 퇴소 ↔ 활성 정합 | V5 `chk_clients_discharge_active`(`discharged_at IS NULL OR is_active = FALSE`) + V34 `chk_clients_discharged_after_created`(`discharged_at >= created_at`) — `ClientService.discharge()`는 두 컬럼을 동시 적재해야 하며, raw SQL로 한쪽만 토글하거나 backdated discharge로 시간 역전 시 DB가 거부 |
| 토큰 purge | `@Scheduled` + `idx_refresh_tokens_expires` / `idx_password_reset_tokens_expires` / `idx_branch_qr_tokens_expires` / `idx_refresh_tokens_revoked` / `idx_password_reset_tokens_used` |
| 로그인·알림·백업 purge | `@Scheduled` + `idx_login_history_created` / `idx_notifications_created` / `idx_backup_runs_created` — Tenant별 또는 전역 cutoff `created_at` |
| 감사 로그 purge | `@Scheduled` + `idx_audit_logs_org_created` — Tenant별 `organizations.audit_retention_days`(기본 1095일) |
| 청구 라인 INSERT | `billing_claim_items.organization_id`는 **부모 `billing_claims`에서 복사** — V21 트리거가 자동 설정, FK가 Tenant·이용자 일치 강제 (V16) |
| NHIS import 매칭 | `nhis_import_rows.client_id` 설정 시 이용자 지점 = 배치 지점 (V21 트리거). 배치↔청구 연결 시 지점·월 일치 (V17/V21) |
| NHIS import 행 INSERT | `nhis_import_rows.organization_id`는 **부모 `nhis_import_batches`에서 복사** — V22 트리거가 자동 설정 (V8 Tenant FK 보완) |
| 이용자 프로필 탭 | 출석·건강·청구 탭은 `idx_attendance_org_client_date` / `idx_health_records_org_client_recorded` / `idx_billing_claim_items_org_client_created`(V25) 또는 `idx_billing_claim_items_client_created`(V16) 활용 — Tenant `organization_id` 필수 |
| 이용자 목록 | `GET /clients` — `idx_clients_org_branch_active_created`(V33) partial + trigram name/cert(V12/V26) when `q` present |
| 청구 라인 무결성 | V23 `positive_days` + V24 `days_implies_amount` CHECK 쌍 — `attendance_days ≥ 1` ⇔ `total_amount > 0` (0일·0원 라인만 허용). V26 `(claim_id, client_id)` UK — 청구서당 이용자 1라인 |
| NHIS import 매칭 | `findByOrganizationIdAndBranchIdAndLtcCertNo` — `idx_clients_org_branch_ltc_cert`(V27) + `(organization_id, ltc_cert_no)` UK(V4) |
| 청구 상세 라인 | `GET /billing/claims/{id}` — `idx_billing_claim_items_org_claim_created`(V27) Tenant 스코프 + `created_at` 정렬 |
| 로그인·비밀번호 재설정 | `POST /auth/login`·`/auth/password/reset-request` — `idx_users_email_lower`(V28). cross-tenant 이메일 조회 후 단일 active 계정 검증 |
| 재설정 토큰 무효화 | `invalidateActiveTokensForUser` — `idx_password_reset_tokens_user_active`(V28). `used_at` partial + `idx_password_reset_tokens_used`(V16) purge |
| NHIS import 배치 행 | import 응답 — `idx_nhis_import_rows_batch_created`(V28). cert 매칭은 `idx_nhis_import_rows_batch_ltc`(V26) |
| 백업 스케줄러 | `BackupRunService` — `idx_organizations_active_backup`(V28). `backup_runs` INSERT는 V9/V20 CHECK 준수 |
| 직원 지점 배정 조회 | `AuthService.resolveBranchIds`·`UserService.loadUserBranches` — `idx_user_branches_user_id`(V29). 지점 필터는 `idx_user_branches_branch_user`(V25) |
| 플랫폼 Tenant 검색 | `GET /platform/organizations` — `idx_organizations_name_trgm`(V27) + `idx_organizations_business_no_trgm`(V29), `business_no` exact는 UK |
| 청구 라인 claim 조회 | `findByClaimIdOrderByCreatedAtAsc` — `idx_billing_claim_items_claim_created`(V29). Tenant 스코프 상세는 `idx_billing_claim_items_org_claim_created`(V27) |
| Tenant 이메일 UK | `POST /users`·`existsByOrganizationIdAndEmailIgnoreCase` — `uq_users_org_email_lower`(V30). 저장 시 `lower(email)` 정규화 권장 |
| 비밀번호 변경 세션 | `resetPassword` 성공 후 `refresh_tokens` 활성 행 일괄 `revoked_at` — `idx_refresh_tokens_user_active`(V30) |
| 청구 목록 상태 필터 | `GET /billing/claims?status=` — `idx_billing_claims_org_branch_status_generated`(V31). 미구현 시 `BillingClaimRepository`에 status 파라미터 추가 |
| 대표 보호자 재지정 | `clearPrimaryForClient` — `idx_guardian_clients_org_client_primary`(V31) partial 인덱스 활용 |
| 청구 상태 이력 | no-op 전이(`from_status = to_status`)는 DB 거부(V31 CHECK) — 앱은 실제 변경 시에만 PATCH |
| 출석 일자 정합 | 체크인/아웃 시 `attendance_date` = **Asia/Seoul** 달력일 (V15 CHECK) — QR·수기 모두 동일 규칙 |
| 마스킹 | API 응답 DTO에서 masked 필드만 노출 |

---

## 9. 미확정·추후 확정

| # | 항목 | 현재 가정 |
|---|------|-----------|
| 1 | 센터별 내부 보존 규정 | 본 문서 기본값 적용 |
| 2 | 이용자 퇴소 후 상세 기록 완전 삭제 vs 익명화 | 5년 후 익명화 우선 |
| 3 | 공단 엑셀 원본 파일 스토리지 보존 | import 후 1년, `nhis_import_batches` 메타만 장기 |

> 확정 필요 시 `docs/PLAN_NOTES.md` §추가 질문 23에 기록.

---

*법령 개정·고객 계약 변경 시 planner·security_auditor와 함께 갱신한다.*
