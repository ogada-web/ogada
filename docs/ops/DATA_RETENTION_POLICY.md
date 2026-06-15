<!-- doc:owner=DBA doc:audience=COD,PLN,TSR updated=2026-06-15T09:55:00+09:00 -->
# 데이터 보존·파기 정책 (ops/DATA_RETENTION_POLICY.md)

> **작성**: db_architect 에이전트
> **최초 작성일**: 2026-06-05
> **상태**: MVP v1 기준 (법령·센터 내부 규정 확정 전 운영 가이드)
> **근거**: `docs/planning/REQUIREMENTS.md` §3-2-1, §4, 개인정보보호법(PIPA), 노인장기요양보험법

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
| 준식별정보 | `clients.phone_encrypted`, `address_encrypted`, `branches.phone_encrypted`, `users.phone_encrypted`(V44 guardian) | **암호화 권장**, 부분 마스킹 |
| 민감정보 | `health_records` (건강·투약·낙상) | TLS 전송, RBAC, audit |
| 간호급여 기록 | `pressure_ulcer_assessments`·`pressure_ulcer_care_records`·`nursing_vital_checks`·`nursing_weight_records`·`nursing_oral_care_checks`·`nursing_emergency_records`·`nursing_service_records`·`nursing_excretion_tube_records` (V114–V119·V123·V124) | v3.1 G-NURSING/L03 — `treatment_notes`·`assessment_notes`·`notes`·`action_taken`·`nursing_notes`·`medication_notes`·`medical_notes`·`management_detail` 본문은 평문(준식별·민감 가능). `medical_institution`(의료기관 방문 기록)·`tube_type`/`tube_size`(경관·유치도뇨 관리)도 준식별. `recorded_by` audit 추적(V117/V121/V125 partial index) |
| 운영 식별자 | `ltc_cert_no`, `copay_type`, `ltc_grade`(0=인지지원등급·1–5=요양등급, V99 G9-COG), UUID | 평문 (검색·청구 키) |
| 인증 정보 | `users.password_hash`, `refresh_tokens` | 해시·토큰 hash, 만료·폐기 |
| 직원 인사·근로 | `users.lifecycle_status`·`hired_at`·`terminated_at`·`onboarding_completed`·`reporting_completed`·`contract_signed_at`·`lifecycle_checklist`(V86) | 직원 입사~퇴사 lifecycle(US-R03) — 근로기준법 인사기록. `lifecycle_checklist` JSONB에는 **PII·민감정보 저장 금지**(체크리스트 키·완료 bool만), 평문 운영 데이터 |
| 직원 교육일지 | `staff_training_logs`(V104/V105/**V106**/V107) | US-S02 FAQ21807/21828·G41b func.php 8-7 5종 — `attendee_names`·`training_content` 본문은 평문(준식별 가능). 신규직원 오리엔테이션은 `new_hire_user_id`로 식별자만 보관 |
| 고충상담 기록 | `grievance_counseling_records`(V97/V98/**V102**) | G42/US-T14 고충상담 — 인사·민원 증빙. `counseling_content`/`follow_up_notes` 본문은 평문(준식별·민감 가능), **V102** `recurrence_confirmed`(재발 여부 bool)은 사후관리 시 1회 적재. `target_type=CLIENT`·`CAREGIVER`는 각각 `client_id`/`staff_user_id`로 식별자만 보관. 익명함(`receipt_channel='ANONYMOUS_BOX'`) 채널은 `target_type=OTHER`로 강제되어 식별자 미저장. 결재·사후관리 행위자(`created_by`/`approved_by`)는 audit 추적 |
| 보수교육 이수증 | `staff_refresher_training_certificates`(V88/V90) | US-S02 8-7-1 — PDF/JPEG/PNG(`storage_key` 오브젝트). compliance bool은 `lifecycle_checklist['refresher-training']` 유지 |
| 직원 HR 파일함 | `staff_hr_files`(V91/V92) | US-R03 FAQ21806 — 입사~퇴사 서류 PDF/PNG/JPEG(`storage_key` 오브젝트). `lifecycle_checklist` document_type 키와 앱 연동 |
| 직원 건강검진 | `staff_health_checkups`(V89/V90) | US-R02 8-10 — FAQ21799 5영역 checklist·`result_notes`(민감 시 앱 마스킹). P2 파일함 첨부는 별도 테이블 보류 |
| 감사·로그 | `audit_logs`, `login_history` | PII 마스킹, 내부 UUID 위주 |
| 청구·회계 | `billing_claims`, `billing_claim_items`, `nhis_import_*` | Tenant 격리, 확정 후 불변 |
| 백업 메타 | `backup_runs`, `organizations.backup_enabled` | Tenant별 백업 이력 (API §9) |
| Tenant 운영 설정 | `organizations.claim_generation_basis` (V63), `allow_client_self_checkin`, `audit_retention_days` | 비개인정보·비PII 운영 플래그 — Tenant 해지 시 `organizations` 행과 함께 삭제, 별도 보존 기간 없음 |
| G33 청구시작 기준금액 | `organizations.billing_start_balance_*` (V76/V77) | 비PII 운영 금액·월·메모 — Tenant 해지 시 `organizations`와 동일. settlement 입금일·수단은 **DB 미저장**(앱 응답만, 최소 수집) |
| 참조 마스터 | `region_sidos`, `region_sigungus`, `region_dongs` (V51 행안부 법정동), `branches.region_dong_code`/`service_type`/`branch_code` | **비개인정보·비테넌트** 행정구역 코드 — 평문, 파기 대상 아님(코드 개정 시 갱신·비활성 플래그) |

---

## 3. 보존 기간 (기본값)

> 법령·계약이 상이하면 **긴 기간 우선**. 센터별 내부 규정은 Tenant 설정으로 추후 확장 가능.

| 데이터 유형 | 보존 기간 | 근거·비고 |
|-------------|-----------|-----------|
| 이용자 기본정보(PII 포함) | **퇴소 후 5년** | 장기요양·회계 증빙 일반 관행; 법정 최소 확인 후 조정 |
| 출석·건강·투약 기록 | **퇴소 후 5년** | 급여 제공 기록·분쟁 대응 |
| 간호급여 — 욕창·바이탈·체중·구강·응급·제공기록·배설/경관 (`pressure_ulcer_*`, `nursing_vital_checks`, `nursing_weight_records`, `nursing_oral_care_checks`, `nursing_emergency_records`, `nursing_service_records`, `nursing_excretion_tube_records`, v3.1 — V114–V119·V123·V124) | **퇴소 후 5년** | 출석·건강과 동일 — 급여 제공·MOHW 증빙. purge: V117/V121/**V125** `idx_*_client_purge` + list index cohort 접두어 |
| 식사·프로그램 기록 (`meal_records`, `program_participations`, v3 — V49·**V113 G17b**) | **퇴소 후 5년** | 출석·건강과 동일 — purge: `idx_meal_records_client_date`·`idx_program_participations_client_date`. **V113** `skip_reason`·**V112** `functional_recovery_plans.cognitive_activity_*`는 동일 cohort(급여 제공·MOHW 제32조 증빙) |
| 기능회복훈련 연간 계획 (`functional_recovery_plans`, v2 G17 — V72/V74) | **퇴소 후 5년** | 급여 제공·평가 지표 증빙 — purge: `idx_functional_recovery_plans_client_purge`(V74) |
| 사례관리 회의록 (`case_management_meetings`, v2 G32 — V73/V74/V75) | **퇴소 후 5년** | 지표 43 분기별 회의 기록 + `case_management_plan`(V75 사례관리 계획) — purge: `idx_case_management_meetings_client_purge`(V74) |
| 급여제공결과평가 (`provision_result_evaluations`, v2 G39 — V80/V81) | **퇴소 후 5년** | 지표 44 연간 평가(수급자×연도 UK) — 급여 제공·평가 지표 증빙. purge: `idx_provision_result_evaluations_client_purge`(V81) + UK `(org, client_id, evaluation_year)` cohort 접두어 |
| 선임 요양보호사 업무수행일지 (`lead_caregiver_work_logs`, v2 G34 — V82/V83) | **퇴소 후 5년** | 급여 제공·전자서명 증빙(케어포 8-1-2·US-S01) — purge: `idx_lead_caregiver_work_logs_client_purge`(V83) + UK `(org, client_id, log_date)` cohort 접두어 |
| 정기 욕구사정 (`client_needs_assessments`, v1.2.1 G24 — V84/V85) | **퇴소 후 5년** | 연 1회 욕구사정·가정방문 기록(US-T09·BNK-124) — 급여 제공·사정 증빙. purge: `idx_client_needs_assessments_client_purge`(V85) + UK `(org, client_id, fiscal_year)` cohort 접두어 |
| 신규입소 위험도평가 (`client_risk_assessments`, v2 G40 — V93/V94) | **퇴소 후 5년** | silverangel 지표21 낙상·욕창·인지기능 3종 스크리닝(US-T11·BNK-150) — 급여 제공·입소 증빙. purge: `idx_client_risk_assessments_client_purge`(V93) + UK `(org, client_id, assessment_type)` cohort 접두어 |
| 반기 기초평가 위험도 (`client_periodic_risk_assessments`, v2 G40b — V95/V96) | **퇴소 후 5년** | 이지케어 지표16·FAQ21811 낙상·욕창·인지 **반기 1회** 재평가(US-T12·BNK-153~154) — G40(입소 1회)과 주기 분리. purge: `idx_client_periodic_risk_assessments_client_purge`(V95) + UK `(org, client_id, fiscal_year, fiscal_half, assessment_type)` cohort 접두어 |
| 고충상담 기록 (`grievance_counseling_records`, v2 G42 — V97/V98/**V102**) | **접수일(`counseled_at`) 기준 5년** | FAQ21814 지표7 고충상담·전자결재·**사후관리(`follow_up_recorded_at`)** 증빙(US-T14·BNK-161). 사후관리는 결재 후 1회만 기록(V102 CHECK·앱 `recordFollowUp`). target=CLIENT cohort는 이용자 퇴소 purge 시 동반 삭제(`idx_grievance_counseling_records_client_purge` V98). target=CAREGIVER cohort는 직원 퇴사 후 3년 보존(인사기록)과 별도로 본 행 5년 우선 적용(`idx_grievance_counseling_records_org_staff_user` V98). 익명함(`ANONYMOUS_BOX`·`target_type=OTHER`)·target=OTHER는 식별자 없이 본 cohort로 별도 cutoff |
| 모니터링 자체점검 (`monitoring_self_diagnoses`, v2 G30 — V100/V101) | **점검월 기준 5년** | FAQ21841 지점 월별 자체점검표(항목 1~15) — 평가·감사 증빙. 이용자 비참조(지점 단위) — 지점 폐쇄 시 cohort 정리. 작성자(`created_by`) audit 추적(`idx_monitoring_self_diagnoses_org_created_by` V101) |
| 모니터링 전화상담 (`monitoring_phone_consultations`, v2 G30 — V100/V101) | **상담월 기준 5년** | FAQ21836 지점×월×이용자 안부전화 기록(`consultation_notes` 본문 준식별·민감 가능) — 급여 외 사례관리 증빙. 이용자 퇴소 purge 시 동반 삭제(`idx_monitoring_phone_consultations_client_purge` V101) + UK `(org, branch, year, month, client_id)` cohort 접두어 |
| 식단·프로그램 일정 (`meal_menus`, `activity_programs`, v3 — V49) | **일정일 기준 2년** | 운영 참조용 — purge: `idx_meal_menus_org_branch_date`·`idx_activity_programs_org_branch_date` |
| 청구서·명세·공단 import | **청구 연도 기준 5년** | 세무·회계 보존 관행. `nhis_import_rows.match_status_reason`(V54)은 사용자 안내용 보류 사유만 저장하고 내부 예외·스택·원본 파일 경로는 저장 금지 |
| 본인부담금 환불 메타 (`billing_claims.refunded_*`, V71/V74) | **청구 연도 기준 5년** | 수납·환불 증빙 — `billing_claims` 행과 동일 cohort. purge: `idx_billing_claims_org_branch_status_refunded_at`(V71) |
| 수가표·본인부담률 이력 | **영구(또는 10년)** | 과거 청구 재현·감사 |
| 감사 로그 (`audit_logs`) | **3년** (기본 `organizations.audit_retention_days=1095`, 30–3650 조정 가능) | 보안·개인정보 접근 추적 — `idx_audit_logs_org_created` |
| 로그인 이력 | **1년** | 보안 모니터링 — `idx_login_history_created`(V15)로 purge 스캔 |
| refresh·비밀번호 재설정 토큰 | **만료 즉시·최대 30일** | 기술적 최소 보관 — `idx_refresh_tokens_expires`·`idx_password_reset_tokens_expires`(V14)로 만료 스캔; 폐기(`revoked_at`) 후 30일 purge는 `idx_refresh_tokens_revoked`(V15); **사용(`used_at`) 후 7일** purge는 `idx_password_reset_tokens_used`(V16) |
| 지점 QR 토큰 | **유효일 종료 후 7일** | 운영·분쟁 조회 후 삭제 — `idx_branch_qr_tokens_expires`(V13)로 만료 스캔 |
| 알림 발송 이력 (`notifications`) | **1년** | v1 이후 채널 연동 시 — `idx_notifications_created`(V15)로 purge 스캔 |
| 보호자 알림 수신 설정 (`guardian_notification_preferences`, v2 — V41 `feac558` + V42 `428ba7d` 커밋) | **계정 유효 기간 + 1년** | 채널 on/off·`consent_at` — PIPA 마케팅성 수신 동의 증빙. kakao/sms 채널 on은 `consent_at` 필수(V42 `chk_…_kakao_consent`·`…_sms_consent`). 보호자 계정 비활성·연결 해제 후 1년 보관 후 purge |
| 보호자 초대 (`guardian_invitations`, v1.1 — V43) | **만료·수락·취소·무효화 후 30일** | 이메일 초대 토큰·`recipient_email_encrypted` — PIPA 준식별. purge 스캔: `idx_guardian_invitations_expires`·partial `idx_guardian_invitations_pending_expires`·partial `idx_guardian_invitations_revoked`·`idx_guardian_invitations_accepted`(V43). `token_hash` UK 행은 purge 시 DELETE |
| DB·애플리케이션 백업 | **일 1회, 30일 롤링** | REQUIREMENTS §4 비기능; `backup_runs`에 실행 메타 기록 |
| 백업 실행 이력 (`backup_runs`) | **90일** (메타) | `storage_location`·`size_bytes` 등; 실제 스냅샷은 30일 롤링과 연동 — purge 스캔 `idx_backup_runs_created`(V16). 종료 상태(`SUCCESS`/`FAILED`)는 `completed_at` 필수(V20)이므로 purge 컷오프는 `completed_at` 기준 가능; `FAILED`는 `error_message` 함께 보존(V20) |
| 퇴소·비활성 계정 | **동일 기간 후 파기 배치** | `is_active=false` ≠ 즉시 삭제 |
| 직원 lifecycle 인사기록 (`users.lifecycle_status`·`hired_at`·`terminated_at` 등, v2 US-R03 — V86/V87) | **퇴사(`terminated_at`) 후 3년** | 근로기준법 §42 근로자명부·임금대장 3년 보존. `lifecycle_status='TERMINATED'`는 `terminated_at` 필수(V87) — purge 배치는 `terminated_at` 기준 cutoff, `idx_users_org_lifecycle_status`(V86)로 Tenant별 TERMINATED 스캔. 보존 경과 후 PII(이메일·전화) 익명화는 §4-3 |
| 직원 교육일지 신규직원 행 (`staff_training_logs.new_hire_user_id`, v1.2.1 US-S02/G41b — V104–V107) | **퇴사(`terminated_at`) 후 3년** | 오리엔테이션 일지는 인사기록 증빙 — purge: `idx_staff_training_logs_new_hire_user_purge`(V105) + `new_hire_user_id IN (TERMINATED cohort)`. 지점 연간·반기 일지(신규직원 미참조)는 상단 5년 정책 우선 |
| 직원 보수교육 compliance 메타 (`users.lifecycle_checklist['refresher-training']`, v2 US-S02 8-7-1 — V86) | **직원 lifecycle 인사기록과 동일** | bool 완료 플래그 — purge는 `users` TERMINATED cohort와 동일 |
| 보수교육 이수증 (`staff_refresher_training_certificates`, v2 US-S02 — V88/V90) | **퇴사(`terminated_at`) 후 3년** | 근로기준법 인사기록과 동일. purge: `idx_staff_refresher_training_certificates_user_purge`(V90) + `storage_key` 오브젝트 삭제 |
| 직원 HR 파일함 (`staff_hr_files`, v2 US-R03 — V91/V92) | **퇴사(`terminated_at`) 후 3년** | FAQ21806 입사~퇴사 서류·근로기준법 인사기록과 동일. purge: `idx_staff_hr_files_user_purge`(V92) + `storage_key` 오브젝트 삭제 |
| 직원 교육일지 (`staff_training_logs`, v1.2.1 US-S02/G41b — V104–V107) | **교육 실시일(`trained_at`) 기준 5년** | FAQ21807 노인인권·FAQ21828 운영규정·G41b 3종(재난·소화설비·직원권익) 지점 교육 증빙 — `attendee_names`·`training_content` 본문은 평문(준식별 가능). 신규직원 오리엔테이션(`new_hire_user_id`) 행은 퇴사 cohort 3년 우선 적용 후 삭제 가능(`idx_staff_training_logs_new_hire_user_purge` V105). 지점 단위 연간·반기 일지 purge: `idx_staff_training_logs_org_branch_year_type`(V104) cohort |
| 직원 건강검진 (`staff_health_checkups`, v2 US-R02 — V89/V90) | **퇴사(`terminated_at`) 후 3년** | 근로기준법 인사기록·건강검진 증빙. purge: `idx_staff_health_checkups_user_purge`(V90) |
| 배차 운행 (`transport_runs`·`transport_run_stops`, v1.3-A — V47) | **운행일 기준 2년** | 운영 편의용(G15·G16 법정 일지 제외). purge: `idx_transport_runs_org_branch_date` |
| 배차 자동제안 로그 (`transport_suggest_events`, v1.3-B — V120·V122) | **90일** | PoC suggest 상한 집계·운영 감사 — PII 미저장(`run_date`·actor UUID만). purge: `idx_transport_suggest_events_org_branch_date` |
| 지점 배차 설정 (`branch_transport_settings`, v1.3-B — V120) | **지점 운영 기간** | 비PII 운영 파라미터(시간창·가중치) — 지점 폐쇄 시 `branches` cohort와 동반 삭제 |
| 지점 도입 후 관리 체크리스트 (`branch_onboarding_support`, v2 G-ONBOARD-SUPPORT — V126/**V127**) | **지점 운영 기간** | 비PII 운영 체크리스트(`opened_on`·`session_state` JSONB 1~4회차 완료 항목·메모) — silverangel businessSupport parity (BNK-186/212). `notes`는 운영 메모 텍스트로 PII 저장 금지(앱 가이드). 지점 폐쇄 시 `branches` cohort와 동반 삭제. **V127** Tenant 앵커 + actor backstop + `(org, updated_by)` partial 인덱스로 직원 퇴사 시 actor purge 추적 |
| 수급자 외출 (`client_outings`, v1.3-C G15 — V67·V70) | **퇴소 후 5년** | 출석·건강과 동일 — 급여 제공·안전 기록. purge: `idx_client_outings_client_purge`(V70) + `client_id` cohort |
| 이동서비스비 청구 (`transport_service_fee_records`, v1.3-C G16 — V68·V70) | **청구 연도 기준 5년** | 이동서비스비 수납·공단 증빙 — `billing_claims`와 동일 관행. purge: `idx_transport_service_fee_records_client_purge`(V70) |
| 이동서비스비 수가 (`transport_service_fee_rates`, v1.3-C G16 — V68) | **영구(또는 10년)** | 과거 fee record 재현·감사 — `fee_schedules`와 동일 |
| 차량 마스터 (`vehicles`, v1.3-C G16 — V69·V70) | **비활성(`active=false`) 후 2년** | 운영 참조용 — `transport_runs` 2년 보존과 연동. purge: 지점 cohort + `idx_vehicles_org_branch_active` 스캔 |
| 이동서비스 이용 계약서 (`transport_service_contracts`, v1.3-C G15 — V64·V65) | **퇴소 후 5년** | 이용자 기본정보·급여 제공 증빙과 동일 — 보호자·기관 서명·5종 수칙 체크리스트. purge: `idx_transport_service_contracts_client_purge`(V65) + `client_id` cohort |
| 등급 변동 이력 (`client_ltc_grade_history`, v1.2 P0 — V48) | **퇴소 후 5년** | 이용자 기본정보와 동일. purge: `idx_client_ltc_grade_history_org_client_changed` + `client_id` cohort |
| 인정기간 계획서 첨부 (`client_ltc_grade_history_attachments`, v2 G37 — V78·V79) | **퇴소 후 5년** | 등급 이력과 동일 cohort — 케어플랜 PDF/PNG(`storage_key` 오브젝트 포함). 이력 행 삭제 시 V79 `(org,client_id,history_id)` FK `ON DELETE CASCADE`로 자동 제거. purge: `idx_client_ltc_grade_history_attachments_client_purge`(V79) + `client_id` cohort. **오브젝트 스토리지 파일은 DB 행 purge와 함께 별도 삭제**(`storage_key` 기준 배치) |
| 급여계약 파일함 첨부 (`client_benefit_contract_attachments`, v1.2.1 G14 — V84/V85) | **퇴소 후 5년** | 이용자 기본정보·급여 제공 증빙과 동일 — 계약서·동의서 PDF/PNG(`storage_key` 오브젝트, ≤10MB·V84 CHECK). 이용자 행 삭제 시 `client_id ON DELETE CASCADE`로 자동 제거(US-T10·BNK-124). purge: `idx_client_benefit_contract_attachments_client_purge`(V85) + `client_id` cohort. **오브젝트 스토리지 파일은 DB 행 purge와 함께 별도 삭제**(`storage_key` 기준 배치) |
| 방문요양 일정 (`visit_schedules`, v2 G21 — V53) | **방문일 기준 5년** | 급여 제공 기록(계획/청구 이중 일정·체크인/아웃) — 출석과 동일 분쟁 대응. 이용자 cohort purge: `idx_visit_schedules_org_client_date`(`(org, client_id, visit_date DESC)`) |
| CMS 자동출금 동의 (`cms_enrollments`, v2 G2 — V59 `2c6e57e`) | **동의 해지(`CANCELLED`)·이용자 퇴소 후 5년** | 효성 FCMS 자동출금 — 회계 증빙. 최소 수집 원칙(§2): 전체 계좌번호 대신 `account_last4`만 저장, `bank_code`·`payer_name`·`fcms_member_id`만 보관(전체 계좌·CVC·비밀번호 저장 금지). Tenant 무결성은 V60 복합 FK(`(org, branch_id\|client_id\|guardian_user_id)`)로 보장. purge: `idx_cms_enrollments_org_client_status` + `client_id` cohort |
| CMS 출금 요청 (`cms_debit_requests`, v2 G2 — V59) | **청구 연도 기준 5년** | 청구·수납 증빙과 동일(`(org, claim_id)` UK로 청구당 1건). `failure_reason`은 사용자 안내용 사유만 저장하고 FCMS 내부 코드·스택 원문은 저장 금지. purge: 청구 cohort + V60 `idx_cms_debit_requests_org_enrollment` |
| 본인부담금 간편결제 (`easy_pay_requests`, v2 G2 7-5 — V108/V109/**V110/V111**) | **청구 연도 기준 5년** | 케어포 view.npay_manage parity 본인부담금 PG 간편결제(BNK-189). 청구·수납 증빙과 동일 cohort(`(org, claim_id)` UK V108로 청구당 1건, FAILED→재시도 UPDATE). **최소 수집(§2)**: `pg_order_id`·`pg_transaction_id`는 PG가 발급한 외부 결제 식별자만 저장(카드번호·CVC·계좌번호·비밀번호 저장 금지 — stub provider 페이로드 미저장). `payment_url`은 PG redirect URL(P2: 만료 후 마스킹 또는 NULL 처리 검토). `failure_reason`은 사용자 안내용 사유만 저장(PG 내부 코드·스택 원문 저장 금지). Tenant 무결성은 **V110** 복합 FK 5건(`(org, branch_id\|claim_id\|client_id\|guardian_user_id)`)·`trg_easy_pay_requests_set_org`·`trg_easy_pay_requests_guard_active_client`(INSERT 시 퇴소·비활성 이용자 차단)와 **V111** `trg_easy_pay_requests_validate_guardian_link`(보호자 결제 시 `guardian` 역할 + `guardian_clients` 이용자 연결 필수)로 보장. 보호자 결제 행(`guardian_user_id`)은 보호자 계정 비활성 후 청구 cohort 우선 적용. purge: 청구 cohort + `idx_easy_pay_requests_client_purge`(V110) `client_id IN (…)` 일괄 삭제·`idx_easy_pay_requests_org_guardian`(V110) partial로 보호자 cohort 추적 |
| 행정구역 마스터 (`region_sidos`·`region_sigungus`·`region_dongs`, V51) | **영구(파기 없음)** | 행안부 법정동 코드 — 비개인정보·비테넌트 참조 데이터. 코드 개정 시 갱신·`region_dongs.is_active=false`로 폐지 표시(물리 삭제 시 `branches.region_dong_code` FK 무결성 유지) |

---

## 4. 파기·익명화 절차

### 4-1. 이용자 퇴소 (`clients.discharged_at` 설정)

1. 퇴소 즉시: UI 목록에서 비활성(`is_active=false`), 신규 출석·건강·방문일정·업무수행일지·욕구사정·위험도평가(G40/G40b)·계약 첨부 입력 차단(V10/V13/**V55**/**V83**/**V85**/**V93**/**V95**).
2. 보존 기간 경과 후 배치(`discharged_at` 기준, `idx_clients_org_discharged_at` V32 스캔):
   - PII 컬럼: NULL 또는 토큰화·익명화 (이름 → `퇴소이용자-{내부ID}`).
   - `resident_registration_no_encrypted` **완전 삭제**.
   - 사진 스토리지 객체 삭제.
3. 출석·건강·청구·보호자 연결: 법정 보존 기간까지 유지 후 집계용 통계만 남기고 상세 삭제(정책 확정 시). purge 시 `idx_attendance_client_purge` / `idx_health_records_client_purge` / `idx_billing_claim_items_client_purge`(V33) / `idx_meal_records_client_date` / `idx_program_participations_client_date`(V49) / `idx_functional_recovery_plans_client_purge`(V74) / `idx_case_management_meetings_client_purge`(V74) / `idx_provision_result_evaluations_client_purge`(V81) / `idx_lead_caregiver_work_logs_client_purge`(V83) / `idx_visit_schedules_org_client_date`(V53) / `idx_transport_service_contracts_client_purge`(V65) / `idx_client_outings_client_purge`(V70) / `idx_transport_service_fee_records_client_purge`(V70) / `idx_client_ltc_grade_history_attachments_client_purge`(V79) / `idx_client_needs_assessments_client_purge`(V85) / `idx_client_risk_assessments_client_purge`(V93) / `idx_client_periodic_risk_assessments_client_purge`(V95) / `idx_grievance_counseling_records_client_purge`(V98 partial — target=CLIENT cohort) / `idx_monitoring_phone_consultations_client_purge`(V101) / `idx_client_benefit_contract_attachments_client_purge`(V85) / `idx_easy_pay_requests_client_purge`(V110) / `idx_guardian_clients_client`(V2) / `guardian_invitations`(V43 `client_id ON DELETE CASCADE`)로 `client_id IN (…)` 일괄 삭제·익명화. `guardian_clients`는 `ON DELETE CASCADE`이므로 이용자 행 **물리 삭제** 시 자동 제거; 익명화(행 유지) 시에는 연결 행을 앱·배치에서 명시 삭제.

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
| `guardian_invitations` | `ACCEPTED`/`CANCELLED`/`REVOKED` 또는 `PENDING`+만료 후 30일 내 삭제 — `idx_guardian_invitations_expires`·partial `idx_guardian_invitations_pending_expires`·partial revoked/accepted(V43) |
| `users` 퇴직 | `lifecycle_status='TERMINATED'`(+`terminated_at`, V86/V87)·`is_active=false`(앱이 TERMINATED 전이 시 동시 적재). 근로기준법 3년 보존(§3) 경과 후 이메일 익명화(재가입 UK 충돌 방지) — cutoff는 `terminated_at` 기준 |
| `users.phone_*` (guardian, V44) | 보호자 계정 비활성·연결 해제 후 **1년** — `phone_encrypted` 삭제·`phone_masked` NULL. V45 `chk_users_phone_pair`로 쌍 삭제 |

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
| 퇴소 후 방문일정 | `visit_schedules` INSERT 거부 (**V55** `trg_visit_schedules_guard_active_client`) — 기존 DRAFT/확정 행 UPDATE(체크인/아웃)는 허용 |
| 동의 | `consent_collected_at`·주민번호 컬럼 모두 NULL 허용(2단계 등록). 동의 후에만 RRN 저장 (`chk_clients_rrn_consent`, `chk_clients_rrn_pair` — encrypted/masked 쌍 규칙) |
| guardian/client_user 연결 | `guardian_clients`·`clients.user_id` INSERT/UPDATE 시 역할 CHECK 트리거(V13) — 잘못된 역할 계정 연결 차단 |
| guardian_clients Tenant | `guardian_clients.organization_id`는 **연결 `clients`에서 복사** — V23 트리거가 자동 설정 (V5 Tenant FK 보완) |
| 결석 출석 | `POST /attendance/absence` — `check_out_at`·`transport_type` NULL, `check_in_method=manual` (V14 CHECK) |
| actor Tenant FK | `created_by`·`recorded_by`·`generated_by`·`imported_by`·**`payment_recorded_by`**(V52)는 JWT `organization_id`와 일치하는 사용자만 (V14 복합 FK; V52가 `billing_claims.payment_recorded_by`를 동일 규약으로 정렬) |
| actor 자동 적재 | V32 `trg_attendance_set_created_by`·`trg_billing_claims_set_generated_by`·V33 `trg_health_records_set_recorded_by`·`trg_nhis_batches_set_imported_by`·V35 `trg_fee_schedules_set_created_by`·`trg_branch_qr_tokens_set_created_by`·**V52 `trg_billing_claims_set_payment_recorded_by`**(PAID 전이 시)·**V55 `trg_visit_schedules_set_actors`**(create/confirm/cancel) — 쓰기 트랜잭션에서 `DbSessionContext.setActorUserId` 호출 시 NULL actor 컬럼 자동 채움 |
| 본인부담금 수납 (v2 US-L01) | `POST /billing/claims/{id}/payments` — **`copayAmount` NULL 거부**(`1af5b1f`, Q257) · `CONFIRMED→PAID` 전이 시 `paid_at`·`payment_method`(`CASH|BANK_TRANSFER`)·`payment_recorded_by`(`requireActorUserId`) 적재. **`updateClaimStatus`→`PAID`** 동일 copayAmount 가드(`923e610`) · `chk_billing_claims_paid_requires_metadata`(V50)가 수납 메타 없는 PAID 거부, V52 Tenant FK·backstop이 actor 무결성 보장. 미납 목록 `GET /billing/overdue` → `idx_billing_claims_org_branch_status_year_month`(V50). 수납 메타는 `billing_claims` 컬럼이므로 청구 5년 보존(§3)에 포함 |
| 퇴소 purge 스캔 | `@Scheduled` + `idx_clients_org_discharged_at`(V32) — Tenant별 `discharged_at IS NOT NULL AND discharged_at < cutoff`; 자식 행은 V33 `idx_*_client_purge`로 `client_id IN (…)`. **지점 단위** 정리(지점 폐쇄·부분 rollback)는 V34 `idx_clients_org_branch_discharged_at`로 `(organization_id, branch_id, discharged_at < cutoff)` |
| 퇴소 ↔ 활성 정합 | V5 `chk_clients_discharge_active`(`discharged_at IS NULL OR is_active = FALSE`) + V34 `chk_clients_discharged_after_created`(`discharged_at >= created_at`) — `ClientService.discharge()`는 두 컬럼을 동시 적재해야 하며, raw SQL로 한쪽만 토글하거나 backdated discharge로 시간 역전 시 DB가 거부 |
| 동의·인정 시간 정합 | V36 `chk_clients_consent_after_created`(`consent_collected_at >= created_at`)·`chk_clients_ltc_cert_valid_from_after_birth`(`ltc_cert_valid_from >= birth_date`) — 2단계 동의 수집(`collectConsent`)·LTC 인정서 등록 시 backdated 시각 거부. PII 이관·잘못된 backfill·typo 입력 1차 방어 |
| 청구 생성 기준 (US-M03, V63) | `GET/PATCH /settings/billing` — `organizations.claim_generation_basis`(`ATTENDANCE_SCHEDULE`|`NHIS_IMPORT`). `NHIS_IMPORT` 모드에서 import 선행·매칭 행만 집계는 **앱 검증**(`BillingService.resolveNhisServiceDaysByClient`) — DB CHECK로 강제하지 않음(PLAN_NOTES #97). 전월 미납 가드는 `idx_billing_claims_org_branch_status_year_month`(V50) |
| 청구 생성 시간 정합 | V36 `chk_billing_claims_generated_after_created`(`generated_at >= created_at`) — `BillingService.generateClaim`은 `now()` 적재로 항상 충족; raw SQL 직접 UPDATE·이력 backdate 거부. V8 status 단방향 트리거(`DRAFT→CONFIRMED→PAID`)와 결합해 청구 audit timeline 단조성 보장 |
| 은행 입금 엑셀 bulk import (US-L01) | `POST /billing/imports/bank-deposits` — `billing_claims` PAID 전이(V50/V52) 재사용 + `audit_logs` INSERT(`bank_deposit_import`). 입금 내역 전용 테이블 없음 — 감사 로그 3년 보존(§3) |
| row lifecycle UPDATE 정합 | V37 `chk_attendance_updated_after_created`·`chk_attendance_checkin_after_created`·`chk_clients_updated_after_created`·`chk_billing_claims_updated_after_created` — 체크아웃·PATCH·상태 전이 UPDATE 시 `updated_at`/`check_in_at >= created_at`. JPA `@UpdateTimestamp`·`OffsetDateTime.now()` 흐름은 항상 충족; raw SQL backdate 1차 방어 |
| NHIS row Tenant 앵커 | V37 `uq_nhis_import_rows_org_id` — `PATCH /billing/imports/nhis/rows/{rowId}/match` Tenant 격리. 배치 claim 목록은 `idx_nhis_import_batches_org_branch_claim_created`(V37); 지점 전체 목록은 `idx_nhis_import_batches_org_branch_created`(V38) |
| 토큰 purge | `@Scheduled` + `idx_refresh_tokens_expires` / `idx_password_reset_tokens_expires` / `idx_branch_qr_tokens_expires` / `idx_refresh_tokens_revoked` / `idx_password_reset_tokens_used` |
| 로그인·알림·백업 purge | `@Scheduled` + `idx_login_history_created` / `idx_notifications_created` / `idx_backup_runs_created` — Tenant별 또는 전역 cutoff `created_at` |
| 감사 로그 purge | `@Scheduled` + `idx_audit_logs_org_created` — Tenant별 `organizations.audit_retention_days`(기본 1095일) |
| 청구 라인 INSERT | `billing_claim_items.organization_id`는 **부모 `billing_claims`에서 복사** — V21 트리거가 자동 설정, FK가 Tenant·이용자 일치 강제 (V16) |
| NHIS import 매칭 | `nhis_import_rows.client_id` 설정 시 이용자 지점 = 배치 지점 (V21 트리거). 배치↔청구 연결 시 지점·월 일치 (V17/V21) |
| NHIS import 행 INSERT | `nhis_import_rows.organization_id`는 **부모 `nhis_import_batches`에서 복사** — V22 트리거가 자동 설정 (V8 Tenant FK 보완) |
| 이용자 프로필 탭 | 출석·건강·청구 탭은 `idx_attendance_org_client_date` / `idx_health_records_org_client_recorded` / `idx_billing_claim_items_org_client_created`(V25) 또는 `idx_billing_claim_items_client_created`(V16) 활용 — Tenant `organization_id` 필수 |
| 보호자 포털 청구 탭 | `GET /guardian/clients/{clientId}/billing` — `BillingService.listClientBillingHistoryForPortal`이 직원 이용자 탭과 **동일** `findByOrganizationIdAndClientIdOrderByCreatedAtDesc`(V25 `idx_billing_claim_items_org_client_created`)를 사용. 보호자 연결 검증은 `existsByOrganizationIdAndGuardianUserIdAndClientId`(V25 `idx_guardian_clients_org_guardian_client`); `client_user`는 `clients.user_id` 1:1 매칭(V23 `idx_clients_org_user`). 청구 헤더 join은 `BillingClaimRepository.findAllById` PK 조회 + Tenant 방어 필터(V8 `uq_billing_claims_org_id` Tenant 앵커로 데이터 정합 보장) |
| 이용자 목록 | `GET /clients` — `idx_clients_org_branch_active_created`(V33) partial + trigram name/cert(V12/V26) when `q` present |
| 청구 라인 무결성 | V23 `positive_days` + V24 `days_implies_amount` CHECK 쌍 — `attendance_days ≥ 1` ⇔ `total_amount > 0` (0일·0원 라인만 허용). V26 `(claim_id, client_id)` UK — 청구서당 이용자 1라인 |
| NHIS import 매칭 | `findByOrganizationIdAndBranchIdAndLtcCertNo` — `idx_clients_org_branch_ltc_cert`(V27) + `(organization_id, ltc_cert_no)` UK(V4) |
| NHIS import 보류 상태 | G7 대기/보류 행은 `nhis_import_rows.match_status='PENDING_REVIEW'` + 공백 아닌 `match_status_reason`(V54)으로 저장. `match_status_reason`은 사용자 조치 문구만 허용하고 파서 stack trace·DB 세부·파일시스템 경로는 저장하지 않는다. 미처리 목록·대시보드는 `idx_nhis_import_rows_org_pending_review` 사용 |
| 청구 상세 라인 | `GET /billing/claims/{id}` — `idx_billing_claim_items_org_claim_created`(V27) Tenant 스코프 + `created_at` 정렬 |
| 로그인·비밀번호 재설정 | `POST /auth/login`·`/auth/password/reset-request` — `idx_users_email_lower`(V28). cross-tenant 이메일 조회 후 단일 active 계정 검증 |
| 재설정 토큰 무효화 | `invalidateActiveTokensForUser` — `idx_password_reset_tokens_user_active`(V28). `used_at` partial + `idx_password_reset_tokens_used`(V16) purge |
| NHIS import 배치 행 | import 응답 — `idx_nhis_import_rows_batch_created`(V28). cert 매칭은 `idx_nhis_import_rows_batch_ltc`(V26) |
| 백업 스케줄러 | `BackupRunService` — `idx_organizations_active_backup`(V28). `backup_runs` INSERT는 V9/V20 CHECK 준수 |
| 직원 지점 배정 조회 | `AuthService.resolveBranchIds`·`UserService.loadUserBranches` — `idx_user_branches_user_id`(V29). 지점 필터는 `idx_user_branches_branch_user`(V25) |
| 플랫폼 Tenant 검색 | `GET /platform/organizations` — `idx_organizations_name_trgm`(V27) + `idx_organizations_business_no_trgm`(V29), `business_no` exact는 UK |
| 청구 라인 claim 조회 | `findByClaimIdOrderByCreatedAtAsc` — `idx_billing_claim_items_claim_created`(V29). Tenant 스코프 상세는 `idx_billing_claim_items_org_claim_created`(V27) |
| Tenant 이메일 UK | `POST /users`·`existsByOrganizationIdAndEmailIgnoreCase` — `uq_users_org_email_lower`(V30). 저장 시 `lower(email)` 정규화 권장 |
| 비밀번호 변경 세션 | `resetPassword` 성공 후 `RefreshTokenRepository.revokeAllActiveForUser`로 활성 refresh 일괄 `revoked_at` — `idx_refresh_tokens_user_active`(V30, `AuthService` 구현 완료) |
| 청구 목록 상태 필터 | `GET /billing/claims?status=` — `idx_billing_claims_org_branch_status_generated`(V31). 미구현 시 `BillingClaimRepository`에 status 파라미터 추가 |
| 대표 보호자 재지정 | `clearPrimaryForClient` — `idx_guardian_clients_org_client_primary`(V31) partial 인덱스 활용 |
| 청구 상태 이력 | no-op 전이(`from_status = to_status`)는 DB 거부(V31 CHECK) — 앱은 실제 변경 시에만 PATCH |
| 출석 일자 정합 | 체크인/아웃 시 `attendance_date` = **Asia/Seoul** 달력일 (V15 CHECK) — QR·수기 모두 동일 규칙 |
| 마스킹 | API 응답 DTO에서 masked 필드만 노출 |
| 보호자 초대 (v1.1 J01) | `GuardianInvitationService` — `recipient_email_encrypted` 저장·목록은 `recipient_email_masked`만 반환. 재발송 시 동일 `(org, client_id)`의 다른 `PENDING`→`REVOKED`(partial idx V43). accept는 `token_hash` UK 조회 후 `ACCEPTED`+`users`+`guardian_clients` 단일 TX. `DbSessionContext.setActorUserId` on create/resend/cancel |
| 알림 발송 이력 (v2 J03) | `NotificationService.dispatchClientEvent` — `guardian_notification_preferences`(V41 UK, V45 Tenant FK+role) 조회 후 `notifications` INSERT(`PENDING`→provider→`SENT`/`FAILED`). channel `kakao`/`sms`는 V3 CHECK·V42 consent backstop. **V45** `SENT ⇒ sent_at` CHECK. Solapi 발송 시 `GuardianPhoneResolver`가 V44 `users.phone_encrypted` Tenant 스코프 복호화. 카카오 실패 시 `AlimtalkFallbackText`→SMS relay(develop `ac17ad8`)는 앱 레이어 — DB 스키마 변경 없음. quiet hours(22:00–08:00 KST)는 앱에서 emergency 제외 skip. purge `@Scheduled` + `idx_notifications_created`(V15) — 1년 보존(§3) |
| 알림 이력 조회 (v2 §11-5) | `GET /guardian/notifications`·`GET /clients/{clientId}/notifications` — `NotificationHistoryService`가 `NotificationRepository.findByOrganizationIdAndRecipientUserIdOrderByCreatedAtDesc`·`…RecipientUserIdInOrderByCreatedAtDesc` 사용. **V46** `idx_notifications_org_recipient_created` Tenant 스코프 페이지네이션. 직원 API는 `guardian_clients`(V24)로 수신자 ID 목록 선정 후 IN 조회. PII 미포함 응답 |
| 미납 목록 reminder 집계 (v2 US-L02) | `GET /billing/overdue` — `BillingService.loadLastBillingReminderAt`이 `NotificationRepository.findLatestBillingReminderAtByClaimIds`(native DISTINCT ON `payload.claimId`, `template_code='BILLING_STATEMENT'`) 사용. **V58** `idx_notifications_org_template_claim_reminder` partial. purge는 기존 `idx_notifications_created`(V15) — 1년 보존(§3) |
| 보호자 서류 이메일 (v2 G2, `f77a268`/`0854fbd`) | `POST /clients/{clientId}/notifications/care-provision-record`·`/home-newsletter`·`/elder-abuse-prevention-guideline` — `GuardianDocumentNotificationService.dispatchDocument`가 `clients`/`branches` 조회 후 `dispatchClientEvent`로 `notifications` INSERT(`channel='email'`·`template_code` ∈ `CARE_PROVISION_RECORD`·`HOME_NEWSLETTER`·`ELDER_ABUSE_PREVENTION_GUIDELINE`, SMTP). elder-abuse는 `notify_daily_care` 동의 재사용(`NotificationEventType` @ `0854fbd`). 신규 DB 스키마 없음(template_code 자유 VARCHAR·channel CHECK V3 `email` 허용). payload는 요약·연월 등 비-PII 텍스트만; purge·보존은 기존 `notifications` 1년 정책(§3)·`idx_notifications_created`(V15) 공유 |
| 수납 영수증 알림 (v2 G2, `588b8e6`/`0854fbd`) | `POST /billing/claims/{id}/payments`·CMS PAID 전이 시 `BILLING_PAYMENT_RECEIVED` dispatch — payload에 `paidAt`·`paymentMethod`·`copayAmount` 포함. `notify_billing` 동의·V50/V52 수납 메타·`notifications` INSERT만 사용 — 신규 DDL 없음. 입금액 `> 0` 검증은 앱(`4109680`); DB는 V4 `copay_amount >= 0`만 보유 |
| 보호자 휴대폰 (V44) | 초대 수락 `POST /guardian/invitations/{token}/accept` — `applyGuardianPhone`이 `phone_encrypted`+`phone_masked` 쌍 저장. V45 `chk_users_phone_pair`. staff UI는 masked만 표시; 복호화는 알림 provider·audit 대상 |
| 배차 API (v1.3-A, V47) | `TransportService` — run 생성/확정/해제(unconfirm PATCH·POST alias, `767d977`) 시 `DbSessionContext.setActorUserId`(`confirmed_by`·`unconfirmed_by` actor 감사). `CONFIRMED` 직원 조회는 앱 RBAC; DB는 명단 자격·15명 상한만 강제. 주소 복호화·지오코딩은 서버 프록시 only |
| 등급 이력 (V48) | `ClientService` 등록 시 `client_ltc_grade_history` 초기 1행 INSERT 권장(`previous_grade=NULL`). 이후 `ltc_grade` PATCH는 트리거가 append — 앱 중복 INSERT 금지 |
| 인정기간 계획서 첨부 (v2 G37, V78/V79) | 첨부 INSERT 시 `history_id`는 **동일 이용자**의 등급 이력만 — **V79** `(org,client_id,history_id)` 복합 FK가 cross-client 연결을 DB에서 차단(앱 `findBy…IdAndClientIdAndHistoryId` 검증과 정합). `uploaded_by`는 `DbSessionContext.setActorUserId` 미설정 시 **V79** `trg_…_set_uploaded_by` backstop이 세션 actor로 채움. content_type PDF/PNG·≤10MB는 V78 CHECK + 앱 검증 이중. 파일 본체는 오브젝트 스토리지(`storage_key`)에 저장 — 퇴소 purge·이력 CASCADE 시 DB 행과 함께 스토리지 오브젝트도 삭제 |
| 정기 욕구사정·계약 파일함 (v1.2.1 G24/G14, V84/V85) | `ClientNeedsAssessmentService`(`PUT /clients/{id}/needs-assessments` upsert)·`ClientBenefitContractAttachmentService`(`POST …/benefit-contract-attachments` upload) — **V85** `trg_*_guard_active_client`가 퇴소·비활성 이용자 INSERT를 DB에서 차단(V10/V49/V83 패턴). `recorded_by`/`uploaded_by`는 `DbSessionContext.setActorUserId` 미설정 시 **V85** `trg_*_set_recorded_by`/`_set_uploaded_by` backstop이 세션 actor로 채움. `organization_id`/`branch_id`는 **V85** `trg_*_set_org_branch`가 `client_id`에서 동기화(cross-tenant 차단은 V84 복합 FK 정합). 욕구사정은 수급자×회계연도 1건(V84 UK)·`fiscal_year` 2000–2100 CHECK; 계약 첨부는 content_type PDF/PNG·0<크기≤10MB·`document_type` CONTRACT/CONSENT/OTHER CHECK(V84). 파일 본체는 오브젝트 스토리지(`storage_key`) — 퇴소 purge·이용자 CASCADE 시 DB 행과 함께 삭제 |
| CMS 자동출금 (v2 G2, V59/V60) | `cms_enrollments`·`cms_debit_requests` INSERT 시 항상 동일 `organization_id`로 적재 — **V60** 복합 Tenant FK(`(org, branch_id\|client_id\|guardian_user_id)→branches/clients/users`, `(org, claim_id\|enrollment_id)→billing_claims/cms_enrollments`)가 cross-tenant 연결을 DB에서 차단(앱은 항상 충족, repository·DTO 변경 불필요). 계좌는 `account_last4`만 저장(최소 수집), `failure_reason`은 사용자 안내 사유만. FK backing: V60 `idx_cms_enrollments_org_branch`·`_org_guardian`·`idx_cms_debit_requests_org_enrollment` |
| 방문일정 (V53/V55/V56/V66) | `VisitService` create/confirm/cancel/check-in 트랜잭션에서 `DbSessionContext.setActorUserId` 호출 — V55 backstop이 `created_by`/`confirmed_by`/`cancelled_by` 방어. 퇴소 이용자 신규 일정은 V55 INSERT 가드로 DB 차단 — UI에서도 목록 제외 권장. **V56**: `POST /visits`·`POST /visits/imports/nhis`의 `createPairedBillingSchedule` 페어(`paired_schedule_id`)는 `idx_visit_schedules_org_paired`(partial)로 self-FK 검증·페어 조회 backing; 배정 요양보호사 일정은 `idx_visit_schedules_org_assigned_date`(partial). **V66**: NHIS import 재실행 시 중복 슬롯 skip(`hasExistingVisitSchedule`) — `idx_visit_schedules_org_branch_client_slot_duplicate` partial. 퇴소 cohort purge는 변동 없이 `idx_visit_schedules_org_client_date`(V53) 사용 |
| 이동서비스 계약서 (v1.3-C G15, V64/V65) | `PUT /transport/contracts/{clientId}` — `TransportContractService.saveContract`가 `DbSessionContext.setActorUserId` 후 upsert. **V65** `trg_transport_service_contracts_guard_client`가 `uses_transport`·활성·미퇴소·지점 일치를 DB에서 강제(앱 `requireWritableClient`와 정합). 5종 수칙 rule id·전체 완료 여부는 앱 검증; 서명일·서명자 이름 쌍은 V65 CHECK. 퇴소 purge는 `idx_transport_service_contracts_client_purge`(V65) — 보존 5년(§3) |
| 수급자 외출 (v1.3-C G15, V67/V70) | `ClientOutingService` create/depart/return/cancel — **V70** `trg_client_outings_guard_active_client`가 퇴소 이용자 INSERT 차단(V10/V49 패턴). 상태 전이(PLANNED→OUT→RETURNED)는 앱 `BusinessRuleException`; `actual_departure_at <= actual_return_at`은 V67 CHECK. 퇴소 purge: `idx_client_outings_client_purge`(V70) |
| 이동서비스비 (v1.3-C G16, V68/V70/**V103**) | `TransportServiceFeeService.generate` — CONFIRMED `transport_runs`·계약 서명·**UK** `(org, client_id, service_date)` 1일1회. **V70** `trg_transport_service_fee_records_guard_client`가 `uses_transport`/활성/지점 일치 DB 강제. 수가는 `transport_service_fee_rates` Tenant catalog(V68 시드, **V103** BNK-174 RU_3/RU_4 정본 보정). purge: `idx_transport_service_fee_records_client_purge`(V70) |
| 차량 마스터 (v1.3-C G16, V69/V70) | `VehicleService` — **UK** `(org, plate_number)` + 앱 `existsBy…IgnoreCase`. **V70** `trg_vehicles_set_recorded_by` actor backstop. `TransportService.resolveVehicleId` + **V70** `trg_transport_runs_guard_vehicle_branch`가 운행↔차량 지점 일치 이중 방어 |
| 연말정산 의료비공제 (v2 G26, `7f10449`/`970f547`) | `GET …/medical-expense-deduction` — `billing_claim_items`·`billing_claims`(V25 client history + PK) read-only 집계. CMS·EASY_PAY 제외는 앱 필터(US-L04). 신규 테이블 없음 — 청구·수납 보존 기간(§3)과 동일 |
| 본인부담금 환불 (v2 US-M03 7-9, V71/V74) | `POST /billing/claims/{id}/refunds` — PAID→REFUNDED 전이 시 `refunded_at`·`refund_amount`·`refund_reason`·`refund_recorded_by` 적재. **V74** `chk_billing_claims_refund_amount_positive`·`chk_billing_claims_refunded_after_paid`·`trg_billing_claims_set_refund_recorded_by`(V52 대칭). 환불 대장 `GET /billing/reports/refunds` → V71 partial 인덱스 |
| 기능회복훈련 계획 (v2 G17, V72/V74) | `FunctionalRecoveryService` — **V74** 퇴소 INSERT 가드·org/branch sync·`created_by` backstop. 퇴소 purge: `idx_functional_recovery_plans_client_purge` |
| 사례관리 회의 (v2 G32, V73/V74/V75) | `CaseManagementService` — 참석자 ≥2명·지표29 평가실시는 앱 검증. **V74** `chk_case_management_meetings_date_year_quarter`·퇴소 guard·actor backstop. **V75** `case_management_plan` NOT NULL + nonempty CHECK. 퇴소 purge: `idx_case_management_meetings_client_purge` |
| 급여제공결과평가 (v2 G39, V80/V81) | `ProvisionResultEvaluationService` — 수급자×연도 1건(UK), 4-pillar compliance(주1·월1·연1·30일)는 `attendance`·`program_participations` 집계로 앱 검증. **V80** summary/evaluator nonempty·year range·`updated_at≥created_at` CHECK·Tenant 복합 FK. **V81** org/branch sync·퇴소 INSERT 가드(`trg_*_guard_active_client`)·`created_by` actor backstop(`DbSessionContext.setActorUserId`). 퇴소 purge: `idx_provision_result_evaluations_client_purge` |
| 직원 lifecycle (v2 US-R03, V86/V87) | `PATCH /users/{userId}` — `UserService.validateLifecycleState()`가 입사 완료(계약 서명/`employment-contract` 체크리스트)·퇴사 증빙(`reporting_completed`/`offboarding-report`)·`terminated_at >= hired_at`·TERMINATED→`is_active=false`를 `BusinessRuleException`으로 강제. **V87** `chk_users_terminated_after_hired`·`chk_users_terminated_requires_date`가 동일 날짜 정합을 DB 레벨로 방어(raw SQL·잘못된 backfill 1차 차단, V36 패턴). lifecycle 조회·필터는 `idx_users_org_lifecycle_status`(V86, partial `organization_id` NOT NULL). 퇴사 후 3년 보존(§3)·익명화(§4-3)는 `terminated_at` 기준 |
| 보수교육 이수증 (v2 US-S02, V88/**V90 WT**) | `POST /staff/refresher-training/users/{userId}/certificates` — `branch_id`는 `user_branches` 배정 지점(`resolveBranchId`). **V90** `(org,user_id,branch_id)→user_branches` FK·org sync·`uploaded_by` backstop — **develop HEAD `1817c36` 미커밋**. 업로드 시 `lifecycle_checklist['refresher-training']=true`·삭제 시 잔여 0건이면 false. purge: `user_id IN (TERMINATED cohort)` + 스토리지 삭제 |
| 직원 건강검진 (v2 US-R02, V89/**V90 WT**) | `POST /staff/health-checkups/users/{userId}` — 5영역 최소 1·미래일 앱 검증 + **V90** DB CHECK(`checkup_date_not_future`). **V90** `recorded_by` backstop·배정 FK — **develop HEAD `1817c36` 미커밋**. lifecycle checklist `health-checkup`/`health-checkup-initial` 갱신. purge: `idx_staff_health_checkups_user_purge` |
| 고충상담 (v2 G42 US-T14, V97/V98/**V102**) | `POST/PATCH /staff/grievance-counselings` — DRAFT CRUD + `POST …/{id}/submit`·`approve` 전자결재 + **`POST …/{id}/follow-up` 사후관리 1회**(`GrievanceCounselingService.recordFollowUp`). `DbSessionContext.setActorUserId` 호출 → **V98** `trg_*_set_created_by` backstop. **V102** `chk_*_follow_up_fields`가 notes·`recurrence_confirmed`·`follow_up_recorded_at` pair·`approved_at` 시각 정합을 DB에서 강제. 사후관리 대기 큐는 **V102** `idx_*_pending_follow_up` partial. 재기록 차단은 앱(`followUpRecordedAt != null` → `BusinessRuleException`). 익명함·활성 가드·결재 시각 정합은 V97/V98과 동일. 보존 5년 — target=CLIENT은 `idx_grievance_counseling_records_client_purge`(V98) |
| 모니터링 자체점검·전화상담 (v2 G30, V100/V101) | `GET/POST/PATCH /monitoring/self-diagnoses`·`/monitoring/phone-consultations`(`MonitoringService`). `created_by`는 앱이 명시 적재 + **V101** `trg_monitoring_self_diagnoses_set_created_by`·`trg_monitoring_phone_consultations_set_created_by` backstop이 raw SQL INSERT에서도 세션 actor 채움. 전화상담은 앱(`findByIdAndOrganizationIdAndActiveTrue`)이 활성 이용자만 허용 + **V101** `trg_monitoring_phone_consultations_guard_active_client`가 DB 레벨로 퇴소·비활성 이용자 INSERT 거부(V93 패턴 — 자체점검표는 이용자 비참조로 가드 미해당). 월 단위 UK가 중복 점검·상담 1행 강제. 보존 5년 cohort purge는 §3 monitoring 행 — 전화상담은 `idx_monitoring_phone_consultations_client_purge`(V101)로 §4-1 이용자 cohort 동반 삭제 |
| 직원 교육일지 (v1.2.1 US-S02/G41b, V104–V107) | `POST/PATCH /api/v1/staff/training-logs` — `StaffTrainingLogService`가 `DbSessionContext.setActorUserId` 후 INSERT/UPDATE. **V105** org sync·actor backstop·배정 FK·`trained_at` 연도 CHECK. **V106** 5종 `training_type`. **V107** G41b 연간 3종 `reference_half` NULL CHECK. 신규직원 7일 오리엔테이션·반기/연간 compliance는 앱 검증. purge: 지점 일지 5년(`trained_at`)·오리엔테이션 `idx_staff_training_logs_new_hire_user_purge`(V105) 3년 |
| 지점 도입 후 관리 (v2 G-ONBOARD-SUPPORT, V126/**V127**) | `GET/PUT /branches/{branchId}/onboarding-support`·`PATCH …/sessions/{roundNumber}` — `BranchOnboardingSupportService`가 `JwtScopeResolver.requireActorUserId()` 호출 후 `findByOrganizationIdAndBranchId`(V126 UK `branch_id`) upsert. **V127** `trg_branch_onboarding_support_set_updated_by` backstop이 raw SQL UPDATE에서도 `ogada_read_actor_user_id()`로 actor 채움(V52/V122 `branch_transport_settings` 패턴). `(org, branch_id)→branches`·`(org, updated_by)→users` 복합 FK가 cross-tenant drift DB 차단. SLA 회차·due-date·완료여부는 인메모리 `BranchOnboardingSupportCatalog`(168줄·1~4회차 항목 정의·근로기준법·산재·복지부 운영매뉴얼 체크포인트) — 회차 정의 변경 시 마이그레이션 영향 없음. `session_state` JSONB는 `{round: {completedItemKeys: [], completedAt, notes}}` 구조; PII 저장 금지(앱 가이드, BNK-186/212). 보존: 지점 운영 기간(§3); 직원 퇴사 시 `(org, updated_by)` partial 인덱스로 actor 식별자 익명화 cohort 추적 |
| 본인부담금 간편결제 (v2 G2 7-5, V108/V109/**V110/V111**) | `POST/GET /billing/easy-pay/claims/{id}` — `EasyPayService`가 `requireSingleClientClaim`·copay > 0·전월 미납 가드 검증 후 `EasyPayRequestRepository.findByOrganizationIdAndClaimId`(V108 UK) upsert. 청구당 1행 — FAILED는 재시도 시 동일 row UPDATE(SUCCEEDED·새 PENDING으로 전이). organization_id는 JWT scope에서 적재(코드 동기) + **V110** `trg_easy_pay_requests_set_org`이 raw SQL INSERT도 `branch_id`에서 동기화. **V110** `trg_easy_pay_requests_guard_active_client`가 INSERT 시 퇴소·비활성 이용자 DB 차단(V10/V93 패턴 — 실시간 결제 invariant) — UPDATE는 미적용(FAILED 재시도 허용). lifecycle CHECK 5건(V110) — REQUESTED는 transient(persist 미존재), PENDING/SUCCEEDED/FAILED 전이 시 앱이 `completed_at`/`pg_order_id`/`pg_transaction_id`/`failure_reason` 모두 적재해 DB CHECK 충족. SUCCEEDED 시 `recordCopayPayment(claimId, EASY_PAY)` 호출 → `billing_claims.payment_method='EASY_PAY'`·`paid_at`·`payment_recorded_by`(V50/V52). stub provider(`StubEasyPayProvider`) payload는 DB 미저장. 보존 5년(§3) cohort purge는 `idx_easy_pay_requests_client_purge`(V110) `client_id IN (TERMINATED cohort)` 또는 청구 cohort 우선 적용. 현재 API 권한은 `hq_admin`/`branch_admin`; 보호자 셀프 결제 확장 시 앱 `guardian_clients` 조회 + **V111** DB guard로 본인 `guardian` 역할과 이용자 연결을 검증 후 동일 흐름 |

---

## 9. 미확정·추후 확정

| # | 항목 | 현재 가정 |
|---|------|-----------|
| 1 | 센터별 내부 보존 규정 | 본 문서 기본값 적용 |
| 2 | 이용자 퇴소 후 상세 기록 완전 삭제 vs 익명화 | 5년 후 익명화 우선 |
| 3 | 공단 엑셀 원본 파일 스토리지 보존 | import 후 1년, `nhis_import_batches` 메타만 장기 |

> 확정 필요 시 `docs/planning/PLAN_NOTES.md` §추가 질문 23에 기록.

---

*법령 개정·고객 계약 변경 시 planner·security_auditor와 함께 갱신한다.*
