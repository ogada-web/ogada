<!-- doc:owner=SEC doc:audience=COD,PLN,TSR updated=2026-07-18T02:21:00+09:00 -->
# 위협 모델 (security/THREAT_MODEL.md)

> **작성**: security_auditor (`SEC`)  
> **방법**: STRIDE + 데이터 흐름 기반  
> **시스템**: ogada — 주간보호센터 B2B SaaS (멀티테넌트)  
> **스택**: React SPA ↔ Spring Boot API ↔ PostgreSQL  
> **2026-07-18 31차 갱신**: develop **`a742788`/`592a483`**(양 스트림 **CLEAN** · SEC-D35 Fixed) · `origin/test`=`598d108`/`592a483`(P0·SEC-D14·**735 BE + 0 FE** unpushed·SEC-D18: BE +30 · FE **★ FULLY SYNCED**). **★ v3 program schedule photo**(§2.25) · **★ SEC-D43 path allowlist deepen** · J03 Kakao template-catalog · **31차 신규 BLOCK급 audit Open 0건**. SEC-D4·D25(+1)·D41·D42·D44~D46 carry. 상세 `SECURITY_AUDIT.md` §1.33.

---

## 1. 시스템 개요

### 1-1. 신뢰 경계

```mermaid
flowchart TB
    subgraph untrusted [비신뢰 영역]
        Browser[보호자·직원 브라우저]
        Attacker[외부 공격자]
    end

    subgraph dmz [DMZ / Edge]
        CDN[정적 호스팅 CDN]
        LB[TLS 종료 LB]
    end

    subgraph trusted [신뢰 영역 — Tenant 격리]
        API[Spring Boot API]
        DB[(PostgreSQL)]
        FS[파일 스토리지<br/>사진·백업·NHIS]
    end

    Browser --> CDN
    Browser --> LB
    LB --> API
    API --> DB
    API --> FS
    Attacker -.-> Browser
    Attacker -.-> LB
```

### 1-2. 자산 (가치 순)

| 순위 | 자산 | 분류 | 보호 요구 |
|------|------|------|-----------|
| 1 | 주민등록번호·건강기록 | 고유식별·민감정보 | 암호화·RBAC·audit |
| 2 | JWT·refresh·QR 토큰 | 인증 자격증명 | 단기·해시·rate limit |
| 3 | 청구·NHIS 데이터 | 영업·행정 | Tenant 격리·무결성 |
| 4 | 감사 로그 | 컴플라이언스 | 변조 방지·3년 보존 |
| 5 | 직원 계정·비밀번호 | 인증 | bcrypt·lockout |

### 1-3. 역할·권한 매트릭스 (요약)

| 역할 | 테넌트 | 지점 | PII 쓰기 | RRN reveal | 플랫폼 |
|------|--------|------|----------|------------|--------|
| ogada_platform_admin | 전체 | — | — | — | ☑ (구 `platform_admin`·V160 rename) |
| hq_admin | 자기 org | active_branch 쓰기 | ☑ | ☑ | — |
| branch_admin | 자기 org | 할당 지점 | ☑ | ☑ | — |
| social_worker | 자기 org | 할당 지점 | ☑ | ☑ | — |
| caregiver | 자기 org | 할당 지점 | 제한 | — | — |
| guardian | 자기 org | 연결 이용자 | 읽기 | — | — |
| client_user | 자기 org | 본인 | 읽기 | — | — |
| sysadmin | 자기 org | — | 설정 | — | — |

---

## 2. 데이터 흐름 (DFD)

### 2-1. 로그인·JWT 발급

```
[사용자] --email/password--> [POST /auth/login]
    --> [AuthService] --bcrypt--> [users]
    --> [JwtTokenService] --RS256--> access JWT + opaque refresh
    --> [클라이언트] AuthContext + session.js (메모리 JWT)
```

**위협**: credential stuffing, JWT 키 탈취, refresh 탈취

### 2-2. 이용자 PII CRUD

```
[직원] --Bearer JWT--> [ClientController]
    --> [JwtScopeResolver] org/branch 검증
    --> [ClientService] --AES-GCM--> [clients.*_encrypted]
    --> 마스킹된 DTO 응답
```

**위협**: IDOR, 크로스테넌트, RRN 무단 reveal

### 2-3. NHIS Excel Import

```
[관리자] --multipart xlsx--> [BillingController]
    --> [NhisImportService] --Apache POI--> 파싱
    --> [billing_claims] 매칭·저장
```

**위협**: 악성 OOXML (CVE-2025-31672), zip bomb, 잘못된 청구 데이터 주입

### 2-4. QR 출석 체크인

```
[보호자 앱] --QR 스캔--> [AttendanceController]
    --> [QrTokenService] HMAC 검증
    --> [AttendanceService] 소유권·지점 검증
    --> [attendance] 기록
```

**위협**: QR 토큰 위조, 재생 공격, IDOR

### 2-5. 보호자 알림 (Solapi alimtalk/SMS, v2/J03)

```
[BillingNotifyService] --tenant scope--> [GuardianPhoneResolver]
    --> [PiiCryptoService] decrypt phone_encrypted
    --> [SolapiMessageClient] HMAC auth --> Solapi API
    --> (외부) 카카오/SMS 전달
```

**위협**: 크로스테넌트 전화번호 유출, API credential 탈취, 로그 PII 노출

### 2-6. 방문요양 일정 (Epic V, v2/G21)

```
[직원] --Bearer JWT--> [VisitController @PreAuthorize]
    --> [VisitService] requireOrganizationId · validateBranchWriteScope
    --> requireHomeVisitBranch(service_type 가드) · requireClientInScope
    --> [visit_schedules] (V53 + V55 무결성 트리거: 퇴소/비활성 가드·actor backstop)
```

**위협**: 비-방문요양 지점 일정 생성, 크로스테넌트 client 연결, 퇴소 이용자 일정, actor 위조 — **V55 트리거 + 앱 스코프로 완화**

### 2-7. CMS 자동이체 등록·출금 (v2 G2/US-L03, FCMS)

```
[관리자] --Bearer JWT--> [CmsController @PreAuthorize(HQ/BRANCH)]
    --> [CmsService] requireOrganizationId · validateBranchWriteScope
    --> guardianClientRepository.existsBy…(연결 보호자 검증)
    --> [FcmsClient] registerMember / requestDebit (외부 Hyosung FCMS)
    --> [cms_enrollments / cms_debit_requests]
        (V59 + V60 복합 테넌트 FK: org+branch/client/guardian/claim/enrollment)
    --> 성공 시 billingService.recordCopayPayment(CONFIRMED→PAID)
```

**위협**: 크로스테넌트 청구↔CMS 위임 교차참조(**V60 복합 FK로 차단**), 전체 계좌번호 유출(**last4만 저장**), FCMS credential 탈취(env·stub default·fail-closed), 중복 출금(REQUESTED/SUCCEEDED 멱등 가드)

### 2-8. 은행 입금 Excel 일괄 처리 (v2 US-L01)

```
[관리자] --multipart xlsx--> [BillingController @PreAuthorize(HQ/BRANCH)]
    --> [BankDepositImportService] requireOrganizationId · validateBranchWriteScope
    --> [BankDepositExcelParser] --Apache POI XSSF--> 파싱(입금자·금액·일자)
    --> org+branch 스코프 CONFIRMED 청구 매칭(이용자명·금액)
    --> billingService.recordCopayPayment(BANK_TRANSFER)
    --> audit_logs(건수만 — 입금자/이용자명 미로깅)
```

**위협**: 악성 OOXML(CVE-2025-31672 — **NHIS와 함께 2번째 POI 표면**), zip bomb, 크로스테넌트 매칭(**org+branch 스코프로 차단**), 입금자명(PII) 로그 노출(건수만 기록)

### 2-8b. 본인부담금 간편결제 (v2 G2/7-5, BNK-189)

```
[관리자] --Bearer JWT--> [EasyPayController @PreAuthorize(HQ/BRANCH)]
    --> [EasyPayService] requireOrganizationId · validateBranchWriteScope
    --> guardianClientRepository.existsBy…(연결 보호자 검증)
    --> prior-month copay guard · CONFIRMED 청구만 · provider allowlist(CARD/KAKAO_PAY)
    --> [EasyPayProvider] createOrder / confirmPayment (stub 또는 실 PG)
    --> [easy_pay_requests] (V108~V111: org/branch/client/guardian 복합 FK·guardian link 트리거)
    --> billingService.recordCopayPayment(CONFIRMED→PAID, EASY_PAY)
```

**위협**: 크로스테넌트 guardian↔client 위조(**V111 트리거+앱 검증**), stub provider prod misconfiguration(**SEC-D28** — 자동 PAID 시뮬레이션), PG credential 탈취, 중복 결제(REQUESTED/PENDING/SUCCEEDED 멱등 가드), 카드번호 저장(**미저장** — pg_order_id·transaction_id만)

### 2-9. G21 RFID plan-vs-tag diff compare (v2 G21, ezCare matrix)

```
[사회복지사/지점관리자] --Bearer JWT--> [VisitController POST /imports/rfid/compare @PreAuthorize]
    --> [VisitService] requireOrganizationId · validateBranchWriteScope · requireHomeVisitBranch
    --> [NhisVisitScheduleExcelParser] + [RfidTransmissionExcelParser] --Apache POI WorkbookFactory-->
    --> [VisitRfidDiffMatcher] diff code 집계 응답 (PII 최소 — 일정·인정번호 메타)
```

**위협**: 악성 OOXML(CVE-2025-31672 — **3번째 POI 파서 표면**), zip bomb, 크로스테넌트 branchId(**앱 스코프로 차단**)

### 2-9a. G32 사례관리 회의 attendee opinions (FAQ21797)

```
[사회복지사/지점관리자] --Bearer JWT--> [CaseManagementController @PreAuthorize]
    --> [CaseManagementService] requireOrganizationId · branch scope
    --> normalizeAttendeeOpinions · validateAttendeeOpinions(참석자 1:1·중복 거부)
    --> [case_management_meetings.attendee_opinions JSONB] (V157 array CHECK)
```

**위협**: 크로스테넌트 meeting IDOR(**org scope로 차단**), malformed JSON injection(**AttendeeOpinionsCodec+CHECK**), 참석자 불일치 데이터(**서버 검증**)

### 2-9b. G-CASH-RECEIPT-LOG 현금영수증 발급 (FAQ21701)

```
[본부/지점관리자] --Bearer JWT--> [BillingController @PreAuthorize(HQ/BRANCH)]
    --> [CashReceiptIssuanceService] requireOrganizationId · validateBranchWriteScope
    --> PAID+CASH 청구 검증 · 1청구 1발급 · 금액=본인부담금
    --> [cash_receipt_issuances] (V158: identifier_value 평문 at-rest — SEC-D32)
    --> 응답 maskIdentifier(010****1234)
```

**위협**: 크로스테넌트 청구 연결(**org+branch scope**), 비현금 청구 발급(**payment_method 가드**), DB 침해 시 휴대폰/사업자번호 노출(**SEC-D32 Low** — API 마스킹·RBAC 제한)

### 2-10. 직원 입사~퇴사 lifecycle (v2 US-R03)

```
[HQ/BRANCH 관리자] --Bearer JWT--> [UserController @PreAuthorize(HQ/BRANCH)]
    --> [UserService] requireOrganizationId · branch scope
    --> enforceRolePolicy(생성/변경 역할 검증 — platform_admin 차단·branch_admin allowlist)
    --> passwordEncoder.encode(비밀번호 해시)
    --> [users] lifecycle_status·hired_at·terminated_at·lifecycle_checklist
        (V86 컬럼 + V87 CHECK: terminated_at >= hired_at · TERMINATED 시 날짜 필수)
```

**위협**: 권한상승(상위 역할 부여 — **enforceRolePolicy로 차단**), 크로스테넌트 직원 변조(org/branch scope), 비밀번호 평문 노출(bcrypt 해시), 비정상 lifecycle 상태(CHECK 제약·퇴사 시 증빙 강제)

### 2-11. 직원 계정 발급 요청·승인 (v2 staff account-request)

```
[HQ/BRANCH 관리자] --Bearer JWT--> [UserAccountRequestController POST @PreAuthorize(HQ/BRANCH)]
    --> [UserAccountRequestService.submit] requireOrganizationId · branch scope
    --> validateAssignableRoleForTenantRequest(enforceRolePolicy — ogada_*/sysadmin/hq_admin 차단·branch_admin allowlist)
    --> [user_account_requests] PENDING (V162: org+requester FK)
[ogada_platform_admin] --Bearer JWT--> [PlatformUserAccountRequestController approve @PreAuthorize(OGADA_PLATFORM_ADMIN)]
    --> [UserAccountRequestService.approve] provisionApprovedAccount(enforceRolePolicy 재검증 · bcrypt encode)
    --> [users] (V161: org당 hq_admin 1 UNIQUE)
```

**위협**: 권한상승(상위/ogada 역할 자가발급 — **enforceRolePolicy 이중 검증**), 크로스테넌트 요청 변조(org scope·V162 FK), 비밀번호 평문(bcrypt), tenant 직접 user 생성 우회(**`createUser` 봉인·승인 경유만**), org 다중 hq_admin(**V161 UNIQUE**)

### 2-12. 요양보호사 NHIS Excel → 계정요청 (v2 G-STAFF-NHIS-EXCEL-IMPORT)

```
[HQ/BRANCH 관리자] --multipart xlsx--> [StaffNhisCaregiverImportController @PreAuthorize(HQ/BRANCH)]
    --> [StaffNhisCaregiverImportService] requireOrganizationId · validateBranchWriteScope
    --> [StaffNhisCaregiverExcelParser] --Apache POI WorkbookFactory--> 파싱(인력번호·성명·생년월일·전화·이메일)
    --> caregiver 역할 하드코딩 account-request submit(권한상승 불가)
    --> audit_logs(건수만 — 이름·전화 미로깅)
```

**위협**: 악성 OOXML(CVE-2025-31672 — **4번째 POI 파서 표면**·SEC-D4), zip bomb, **확장자/Content-Type 미검증**(SEC-D34 — `WorkbookFactory` 자동판별 의존), 권한상승(**caregiver 고정·account-request 경유**로 차단), 크로스테넌트 branch(앱 스코프 차단)

### 2-13. 본인부담금 명세·NTS 의료비공제 CSV export (v2 G-7-1 / g26)

```
[HQ/BRANCH 관리자] --Bearer JWT--> [BillingController GET .../statement-export · /reports/medical-deduction/export @PreAuthorize(HQ/BRANCH)]
    --> [BillingStatementExportService / BillingService] requireOrganizationId · validateBranchWriteScope
    --> CONFIRMED/PAID 청구만 · 보호자 전화 maskedphone · 주소 region label · RRN 없음(NTS는 인정번호)
    --> UTF-8+BOM CSV (csvEscape: quote만 — 수식 prefix 미중화)
```

**위협**: 크로스테넌트 청구 export(org+branch scope 차단), PII 과다 노출(**전화 마스킹·주소 region label·RRN 미포함**으로 완화), **CSV/수식 인젝션**(이용자명·보호자명 `=`/`+`/`-`/`@` prefix → Excel 수식·DDE 실행·**SEC-D33 Low**)

### 2-14. 미납 회수 CRM·금액 조정 (v2 G-BILLING-OVERDUE-ADJUSTMENT, 케어포 p.89)

```
[본부/지점관리자] --Bearer JWT--> [BillingController /overdue/claims/* @PreAuthorize(HQ/BRANCH)]
    --> [OverdueManagementService] requireOrganizationId · validateBranchWriteScope
    --> requireOverdueClaim · requireClaimItem(org+claim+client)
    --> ②③ management records · ④ adjustments(copayAmount 감소만)
    --> [billing_overdue_management_records / billing_overdue_adjustments]
        (V167 + V168: note/reason non-empty CHECK · Tenant FK pairs · recorded_by org scope)
    --> SMS 자동 등록: recordAutomaticSmsRemindersForClaim(중복·과거 청구월·CONFIRMED guard)
```

**위협**: 크로스테넌트 claim/client 연결(**org scope+requireClaimItem**), 권한 없는 caregiver 접근(**HQ/BRANCH only**), 빈 note/reason·cross-tenant actor(**V168 CHECK+FK pairs**), SMS 중복 audit(**existsBy autoGenerated guard**), 금액 조정 악용(**adjustedAmount < previousAmount** 서버 검증)

### 2-15. 출석 roster 일일 목록 (v2 attendance, BNK-479)

```
[직원] --Bearer JWT--> [AttendanceController GET /attendance @PreAuthorize(HQ/BRANCH/SOCIAL_WORKER/CAREGIVER)]
    --> [AttendanceService] requireOrganizationId · resolveBranchScope
    --> 활성 지점 수급자 roster + derived status(CHECKED_IN/OUT/ABSENT)
    --> clientName(지점 스코프 내) · transportMode 필터
```

**위협**: 크로스테넌트 roster(**branch scope**), caregiver 타 지점 수급자 열람(**validateBranchReadScope**), clientName PII 과다(**역할·지점 범위 내 업무 필요 최소**)

### 2-16. 직원 HR 모바일 카메라 촬영 업로드 (v1.2.1 US-R03)

```
[지점관리자/사회복지사] --multipart image--> [StaffHrFileController POST /users/{userId} @PreAuthorize(BRANCH/SOCIAL_WORKER)]
    --> (클라이언트) <input capture="environment" accept="image/*"> — FileUpload/StaffDocumentRepositoryPanel
    --> [StaffHrFileService] requireWritableStaffUser · validateDocumentType
    --> [StaffHrFileStorageService] Content-Type allowlist · size limit · UUID storage key
```

**위협**: 확장자/MIME 위장(**Content-Type allowlist·SEC-D25 magic-byte 미검증**), 크로스테넌트 staff file(**org+branch user scope**), 카메라 캡처 악성 payload(**서버 검증 동일 경로**)

### 2-17. 직원 연차휴가 연간 현황 (v2 US-R03e / G-STAFF-ANNUAL-LEAVE, ezCare worker-b100 tab01)

```
[HQ/BRANCH/사회복지사] --Bearer JWT--> [StaffAnnualLeaveController @PreAuthorize]
    --> [StaffAnnualLeaveService] requireOrganizationId · resolveReadableBranchId(allowlist 교차검증)
    --> requireWritableStaffUser(STAFF_ROLE_CODES·isActive·validateBranchWriteScope) · requireActorUserId
    --> 입력 검증: year 2000~2100 · month≤99.9 · entitlement≤999.9 · sum≤entitlement · precision 1자리 · ≤12개월
    --> [staff_annual_leave_yearly] (V172 + V173: month_max·entitlement_max·used_within·memo nonempty·user_branch 3-way FK)
    --> [V173 readiness probe] 미적용 시 /health·live-e2e fail-fast
```

**위협**: 크로스테넌트 직원 연차 변조(**org scope + user_branch 3-way FK**), 권한 없는 caregiver write(**PUT=BRANCH/SOCIAL_WORKER only**), 상한초과·합계초과·빈 memo 적재(**V173 CHECK + 앱 검증**), 미적용 마이그레이션 운영(**readiness probe fail-fast**)

### 2-18. 직원 연차·유급휴일 per-event 대장 (v3 US-R01-c / 케어포 8-13, BNK-532)

```
[HQ/BRANCH/사회복지사] --Bearer JWT--> [StaffLeaveLedgerController @PreAuthorize]
    --> [StaffLeaveLedgerService] requireOrganizationId · resolveReadableBranchId / requireWritableStaffUser
    --> update/delete: findByOrganizationIdAndId(org 격리) 후 writable 재검증
    --> 입력 검증: leaveType allowlist(ANNUAL_LEAVE/PAID_HOLIDAY) · date order · 0<daysUsed≤99.9 · precision
    --> [staff_leave_ledger_entries] (V174 Tenant FK pairs·CHECK + V175 memo nonempty·user_branch FK·**24차 커밋 완료·SEC-D35 Mitigated**)
```

**위협**: 크로스테넌트 휴가 항목 IDOR(**org 격리 조회 + V174 Tenant FK**), 권한 없는 write(**create/update/delete=BRANCH/SOCIAL_WORKER only**), 잘못된 유형·음수 일수(**allowlist + CHECK**), 빈 memo·교차지점 적재(**V175 커밋·SEC-D35 Mitigated**)

### 2-19. 직원 모바일 접속키 SMS 발송 (v2 G-SMS-TEMPLATE-CATALOG message_kind=1, ezCare mobile-sendW)

```
[HQ/BRANCH/사회복지사] --Bearer JWT--> [POST /api/v1/staff/notifications/staff-access-key
                                       @PreAuthorize('HQ_ADMIN','BRANCH_ADMIN','SOCIAL_WORKER')]
    --> [StaffAccessKeyNotificationService] requireOrganizationId
    --> 직원 검증: findByIdAndOrganizationId + isActive + terminatedAt==null + STAFF_ROLE_CODES allowlist
        + GuardianPhoneResolver.resolveMobileDigits 존재 강제
    --> branch 해석: activeBranchId or userBranches(org 매치) fallback → validateBranchWriteScope
    --> 키 생성: SecureRandom 6-digit(100_000..999_999, 키스페이스 10^6 — SEC-D36 Monitor)
    --> at-rest: PasswordResetTokenEntity { tokenHash=SHA-256(accessKey), expiresAt=now+60min }
                 invalidateActiveTokensForUser(userId) 선행(단일활성 강제·기존 reset/access key 토큰 회전)
    --> payload: GuardianNotificationPayloadBuilder.staffAccessKeyPayload
                 { staffUserId, staffName, centerName, accessKey, expiresAt } JSON
    --> [NotificationService.dispatchManualStaffSms] quiet-hours(KST 22:00~08:00) 시 BusinessRuleException 거부
        --> NotificationEntity(channel=SMS, payload_json=평문 accessKey 포함 — SEC-D37 Monitor)
        --> SolapiMessageClient (외부) → 직원 휴대전화
    --> 응답: StaffAccessKeyNotifyResponse { staffUserId, templateCode=STAFF_ACCESS_KEY,
                                              expiresAt, ezcareMessageKind=1 } — accessKey 필드 없음
[직원] --SMS 수신 6-digit 키--> [POST /api/v1/auth/password/reset]
    --> AuthRateLimitService (ip 20/min · token 8/min)
    --> AuthService.resetPassword → tokenHash 매칭(SHA-256) → 비밀번호 변경 + token 소비
```

**위협**:
- 인사이더 abuse(SOCIAL_WORKER가 동일 branch 직원에게 무단 발송) — **branch write scope + audit_logs + quiet-hours guard**로 완화
- 6-digit 키 brute force — `/auth/password/reset` rate limit(token 8/min)로 60분 480 시도 vs 키스페이스 10^6 = P(match)≈0.048% 매우 낮음 — **Low (SEC-D36 Monitor)**
- 응답 본문 키 유출(JWT 탈취·MITM) — **응답 record `accessKey` 필드 없음**으로 차단(SMS 채널 전용)
- DB 침해 시 만료 전 키 유출 — `notifications.payload_json`에 평문 accessKey 60분 잔존(SEC-D37 Monitor — payload redact 또는 dispatch 후 purge 권고). `PasswordResetTokenEntity.tokenHash`는 SHA-256만 저장
- 키 재발급 race(이전 키 사용 중 신규 발급으로 잘못된 키 적용) — `invalidateActiveTokensForUser`로 단일활성 강제(한 직원에 활성 토큰 1건만 유효)
- 야간 무차별 발송으로 인한 직원 SMS 폭주 — `NotificationQuietHoursPolicy`(22:00~08:00 KST) 서버 거부 + 운영 정책

### 2-20. 안전점검·감염관리·시설운영일지 (v2 US-Q01, carefor M6)

```
[HQ/BRANCH/사회복지사] --Bearer JWT--> [SafetyCheckController @PreAuthorize(HQ/BRANCH/SOCIAL_WORKER)]
    GET /api/v1/safety/{daily-checks|periodic-checks|infection-control|operation-logs}?branchId=
        --> [SafetyCheckRecordService] requireOrganizationId · resolveBranchScope(write=false)
        --> validateBranchReadScope(branchId 또는 TenantContext.activeBranchId)
        --> repository.findByOrg+Branch+RecordType (ALL rows — ⚠ SEC-D41 pagination 없음)
        --> payload_json 역직렬화 → DTO 응답(inspectorName/authorName/clientName 포함)

    POST /api/v1/safety/{daily-checks|periodic-checks|infection-control|operation-logs}
        --> [SafetyCheckRecordService] requireOrganizationId · resolveBranchScope(write=true)
        --> validateBranchWriteScope · sanitizeChecklistItems(allowedItemIds allowlist)
        --> normalizeSubFormCode/normalizeSymptomCode/normalizeActionCode(enum valueOf allowlist)
        --> requireDate · requireNonBlank · trimToEmpty · normalizeVisitorCount(≥0)
        --> saveRecord → dbSessionContext.setActorUserId(V184 trg_set_created_by)
        --> [safety_check_records] (V184: org+branch 복합 FK · org+created_by 복합 FK
                                        record_type/result_code enum CHECK · actor backstop trigger)
                                   (V185: payload_json object · sub_form_code PERIODIC enum shape
                                        result_code DAILY/PERIODIC NOT NULL shape)
    
    GET /api/v1/safety/check-template-catalog
        --> [SafetyCheckTemplateCatalog.catalog()] 정적 immutable payload — PII·secret 0
```

**위협**:
- 크로스테넌트 안전점검 기록 열람 — `requireOrganizationId`+`validateBranchReadScope`로 차단
- 권한 없는 caregiver/guardian 기록 — `@PreAuthorize` HQ/BRANCH/SOCIAL_WORKER 전용
- 알 수 없는 체크리스트 항목 ID 주입 — `sanitizeChecklistItems(allowedItemIds)` 허용목록 차단
- sub_form_code 임의 문자열 주입 — `SafetyPeriodicSubFormCode.valueOf` + V185 enum CHECK
- 음수 방문자 수·null 날짜·빈 점검자명 — 서버 검증 레이어 차단
- payload_json scalar/array 적재(raw SQL) — V185 `jsonb_typeof='object'` CHECK
- **무제한 GET 응답(데이터 누적 시 DoS/bulk PII 노출)** — **SEC-D41 Low~Medium · date range 가드 권고**
- **payload_json 내 clientName(수급자 이름)·inspectorName/authorName(직원명) 평문 저장** — **SEC-D42 Low · RBAC+scope 가시성 제어 · P3 UUID 전환 검토**

### 2-21. 재무회계 BPO SSO OTP handoff (v2 US-ACCOUNTING-M12 / carefor open_sujifine)

```
[HQ/BRANCH만] --Bearer JWT--> [AccountingBpoController]
    GET /api/v1/billing/accounting/bpo-launch  @PreAuthorize(HQ/BRANCH/SOCIAL_WORKER)
        --> catalog + ssoAvailability (secret 0)

    POST /api/v1/billing/accounting/bpo-sso-handoff  @PreAuthorize(HQ/BRANCH only)  ★ SEC-D43
        --> AccountingBpoSsoHandoffRateLimiter(actor 10/min · org 30/min)
        --> portalUrlAllowlisted? https + sujifine.co.kr|www.sujifine.co.kr
        --> hasCredentials? ACCOUNTING_BPO_USMUSID + OTP_SECRET
            공백/비허용 → BusinessRuleException fail-closed
        --> mintOtp = HmacSHA256(otpSecret, usmusid + "|" + floor(epoch/300)) hex[0..16]
        --> { usmusid, otp, ssoPortalUrl } — password 0
[브라우저] --hidden form POST--> [sujifine carefor_login]
```

**위협**:
- 시설 비밀번호 탈취/저장 — **비밀번호 미수집·미저장·미반환**으로 차단(설계 긍정)
- OTP 재사용/예측 — HMAC + 300s window · secret 없이 OTP 위조 불가
- 인사이더/과다 권한 — **SEC-D43 Mitigated**: SOCIAL_WORKER handoff 제거
- handoff flood — **SEC-D43 Mitigated**: per-actor/org sliding window
- portal URL phishing — **SEC-D43 Mitigated 강화**: https host + **path `/carefor_login`** + query/fragment/userInfo 거부(`bfe6b3f`)
- **시설 전역 env credential**: multi-tenant JVM 공유 시 A org→동일 SSO — **SEC-D43 Residual**(장기 org-scope)
- Health 정보 노출 — `accountingBpoSsoReady` bool only(secret 0)

### 2-22. 직원 급여 preview · 가정통신문 발송 이력 (v2 M11 / G2)

```
[HQ/BRANCH/사회복지사] --Bearer JWT--> [StaffPayrollController]
    POST /api/v1/staff/payroll/{ledger|simple-payment|labor-cost|retirement}-preview
        --> requireOrganizationId · findByIdAndOrganizationId(userId)
        --> validateStaffBranchAssignment + validateBranchReadScope
        --> basePay/allowances/deductions = request body preview(DB 급여 평문 저장 아님)

[HQ/BRANCH/사회복지사] --Bearer JWT--> [NotificationChannelStatusController]
    GET /api/v1/notifications/home-newsletter/dispatch-history?page&size&yearMonth&status&q
        --> requireOrganizationId · resolveBranchScope
        --> PageRequest(default 20, max 100) — ★ SEC-D41 대조 긍정
        --> payload_json → clientName/centerName/summary (SEC-D42 family PII)
```

**위협**:
- 크로스테넌트 급여 preview — org+branch+staff assignment 검증으로 차단
- 대용량 history — pagination max100
- payload PII — SEC-D42 family

### 2-23. FacilityNotice · 연계기록 · 월단위 확정취소 · RFID/급여명세 발송 (v2+ 29차)

```
[HQ/BRANCH/사회복지사] --Bearer JWT--> [FacilityNoticeController]
    CRUD /api/v1/notifications/facility-notices
        --> page max100 · attachment_url http(s)+≤500 · V193 DB CHECK
        --> DRAFT 수정/삭제 · PUBLISHED 본문 불변

[HQ/BRANCH/사회복지사] --Bearer JWT--> [ClientLinkageRecordController|/report]
    CRUD+dispatch · report page max100
        --> V196 length CHECK · 3-way client×branch FK · org/branch sync trigger

[BRANCH/사회복지사] --Bearer JWT--> [VisitController]
    GET /batch-unconfirm-preview → 4-digit challenge(actor-scope·TTL10m)
    POST /batch-unconfirm → consume-once + cascade ack
    POST /imports/rfid/care-provision-dispatch → home-visit only · org/branch/client 검증 → SMS kind13

[HQ/BRANCH/사회복지사] --Bearer JWT--> [StaffNotificationController]
    POST /staff/notifications/staff-payroll-statement → preview 금액 → alimtalk kind22
        --> notifications.payload_json에 netPay 등 평문 (SEC-D45)
```

**위협**:
- attachment `javascript:`/`ftp:` — app+V193 차단 · **SEC-D46**: host allowlist 부재(인사이더 phishing)
- linkage summary PII — RBAC+tenant · length 상한
- **batch-unconfirm 4-digit brute** — JWT+branch+TTL+consume · **SEC-D44** entropy 권고
- RFID/SMS flood · payroll 금액 at-rest — quiet-hours·scope · **SEC-D45** redact/purge

### 2-24. J03 dispatch 단가 참고 · QA-B95 HTML decode · G17 dual-numbering (v1.2.1+ 30차)

```
[HQ/BRANCH] --Bearer JWT--> [NotificationChannelStatusController]
    GET /dispatch-reference-unit-rates
        --> NotificationDispatchUnitRatesCatalog.REFERENCE (정적 app10/SMS20/MMS50)
        --> Health notificationDispatchReferenceUnitRates 동일 surface · secret 0

[Health/live-e2e probe] --GET /health|bootstrap blockers-->
    [LiveE2eOperationReadinessSupport.decodeHtmlEntityDetailToken]
        --> 5-pass bounded HTML entity decode · bidi/mark strip · numeric bounds
        --> FE notificationChannelStatus.js / liveBackendProbe.js parity
        --> 목적: gateway HTML-escape로 operationReady 우회 방지 (fail-closed)

[HQ/BRANCH/사회복지사/요양보호사] --Bearer JWT-->
    [FunctionalRecoveryController|BathingScheduleController]
        --> dualNumberingNoteKo / essentialDutySerial27Label (read-only guardrail)
        --> indicator 27 혼동 방지 · tenant scope 불변
```

**위협**:
- unit-rates 정보 노출 — HQ/BRANCH only · 비밀·실청구 아님 · **Low**
- HTML decode ReDoS/우회 — bounded 5-pass·codePoint 상한 · **Low** — SEC-D29 **긍정**
- dual-numbering — read-only metadata · RBAC 유지 · **Pass**

### 2-25. 프로그램 일정 활동 사진 업로드 · SSO path allowlist (v3 31차)

```
[HQ/BRANCH/사회복지사/요양보호사] --Bearer JWT + multipart-->
    [ProgramController POST /programs/schedule/{programId}/photo]
        --> findByIdAndOrganizationId + validateBranchWriteScope
        --> ProgramPhotoStorageService: ≤5MB · jpeg/png/webp Content-Type(+;param strip)
        --> storage key = programs/{orgId}/{programId}/{uuid}.ext (서버 생성)
        --> activity_programs.photo_storage_key 갱신 · 공개 serve endpoint 없음

[HQ/BRANCH] --Bearer JWT--> [AccountingBpoService.createSsoHandoff]
        --> isAllowlistedPortalUrl: https · sujifine hosts · path=/carefor_login
        --> query/fragment/userInfo/non-443 거부 (SEC-D43 deepen)
```

**위협**:
- MIME 위장 악성 업로드 — Content-Type allowlist·크기·UUID key · **magic-byte 미검증** → **SEC-D25 표면 +1** · 공개 serve 없어 XSS 유예
- 크로스테넌트/타지점 사진 덮어쓰기 — org+branch write scope 차단
- SSO phishing URL 오설정 — path allowlist deepen으로 완화 · **잔여**: process-wide env credential(SEC-D43 Residual)

---

## 3. STRIDE 위협 분석

### 3-1. Spoofing (위장)

| ID | 위협 | 공격 시나리오 | 현재 통제 | 잔여 위험 | 조치 |
|----|------|---------------|-----------|-----------|------|
| T-S1 | JWT 위조 | stolen private key | RS256, JWKS, prod validator | **Low (develop prod)** · **Low (origin/test `598d108`)** |
| T-S2 | QR 토큰 위조 | HMAC secret 추측 | HMAC-SHA256, prod validator | **Low (develop prod)** · **Low (origin/test)** |
| T-S3 | 보호자 계정 탈취 | 피싱·reuse password | bcrypt | Medium | MFA (v2) |
| T-S4 | 프론트 역할 스푸핑 | `/platform` 직접 URL | `ProtectedRoute` (develop) | **Low (develop)** · **Low (origin/test)** — settings/org 분리 @ `f749311` |
| T-J1 | 보호자 초대 토큰 위조·재생 | 만료 토큰 재사용 | 128-bit·SHA-256·rate limit·single-use | **Low** — SEC-D8 Fixed @ `f47ffa1` |
| T-S10 | workspace baseline 불일치 | 잘못된 HEAD 배포 | `workspace_baseline.yaml` | **Low** — SEC-D10 Fixed (`136239e`/`7170b2a`) |

### 3-2. Tampering (변조)

| ID | 위협 | 공격 시나리오 | 현재 통제 | 잔여 위험 | 조치 |
|----|------|---------------|-----------|-----------|------|
| T-T1 | API 요청 org_id 변조 | body에 타 tenant ID | JWT claim만 신뢰 | Low | 유지 |
| T-T2 | xlsx 변조 (NHIS·은행입금·RFID·요양보호사) | duplicate zip entry | POI 5.3.0 (**4 파서**) | Medium | POI 5.4.0 (SEC-D4 20차 확대·요양보호사 확장자 검증 SEC-D34) |
| T-T3 | 감사 로그 삭제 | DB 직접 접근 | 앱 RBAC | Medium | DB 권한 분리 |
| T-T4 | 청구 금액 변조 | 확정 후 수정 API | 비즈니스 규칙 | Low | TSR 검증 |
| T-T5 | 검증된 코드 ≠ 배포 산출물 | merge/push 미실행 | git 이관 규율 | **Low** — `origin/test`=`598d108`/`c7c8f07` P0 포함 ✓ · v2/v1.3 develop 152+186 ahead(feature only·SEC-D18) · 양 스트림 WT CLEAN |
| T-T6 | visit_schedules 직접 변조 | raw SQL·비서비스 경로 | V55 트리거(퇴소 가드·actor backstop) | **Low** — DB-level 무결성 강화 |
| T-T7 | 크로스테넌트 CMS 위임 변조 | 타 테넌트 청구↔CMS 위임 연결 | V60 복합 테넌트 FK + 앱 스코프 | **Low** — DB-level 차단(org+claim/enrollment 복합 FK) |
| T-T8 | 신규 테이블 크로스테넌트/퇴소 client INSERT | raw SQL·body org/branch 변조 | V70/V74 트리거 + V168 overdue + **V173 연차·V174/V175 휴가대장 Tenant FK + user_branch 3-way FK** | **Low** — outings·기능회복·사례관리·미납·연차/휴가대장 DB-level 무결성(V175 24차 커밋 완료·SEC-D35 Mitigated) |
| T-T9 | tenant context 미설정 우회 | 인증 전 필터 실행으로 org/branch null | SecurityConfig 필터를 `BearerTokenAuthenticationFilter` 뒤로(SEC-D24) | **Low** — 인증 후 JWT principal로 TenantContext 정확 설정 · **커밋 완료(WT CLEAN)** |
| T-T10 | 신규 첨부(급여계약서·등급이력·**HR·보수교육**) 크로스테넌트/퇴소 INSERT | raw SQL·body org/branch 변조 | V85/V79/V92 트리거(client 파생·active 가드·actor backstop) | **Low** — DB-level 무결성 강화 |
| T-T11 | G21 무단 체크인/아웃(배정 외 caregiver) | 타 caregiver ID로 check-in | `VisitService` 배정 caregiver·active·branch 가드(`0db1e68`~`78cfb8a`) | **Low** — 방어 강화 |
| T-T12 | G42 익명함 공개 접수 오해 | 비인증 익명 제보 endpoint | **없음** — `ANONYMOUS_BOX`는 수납 채널 enum·전 API `@PreAuthorize` | **Low** — 공개 endpoint 아님 |

### 3-3. Repudiation (부인)

| ID | 위협 | 공격 시나리오 | 현재 통제 | 잔여 위험 | 조치 |
|----|------|---------------|-----------|-----------|------|
| T-R1 | PII 조회 부인 | RRN reveal 후 부인 | audit_logs | Low | 목적 필드 강화 |
| T-R2 | 로그인 부인 | 공유 계정 | login_history | Low | 계정 공유 금지 정책 |

### 3-4. Information Disclosure (정보 노출)

| ID | 위협 | 공격 시나리오 | 현재 통제 | 잔여 위험 | 조치 |
|----|------|---------------|-----------|-----------|------|
| T-I1 | 크로스테넌트 데이터 | scope bypass bug | JwtScopeResolver | Medium | RLS + TSR |
| T-I2 | 에러 스택 노출 | 500 응답 | GlobalExceptionHandler | Low | 유지 |
| T-I3 | 백업 error_message | SYSADMIN API | 역할 제한 | Medium | 메시지 sanitize |
| T-I4 | SQL 로그 PII | format_sql | prod off 필요 | Low | 설정 |
| T-I5 | XSS·무방비 UI | URL 직접 접근·XSS | React escape · ProtectedRoute (develop) | **Low (develop)** · **Low (origin/test)** |
| T-I9 | 설정 API JWT 미첨부 | raw fetch 401·기능 불능 | `apiFetch` Bearer | **Low** — SEC-D17 **Fixed**(raw fetch는 `http.js` 래퍼 1곳뿐·전 페이지 `services.js`) |
| T-I10 | DB 예외 메시지 노출 | 스키마 드리프트·이메일 중복 힌트 | 고정 메시지(raw cause 미echo) | **Low** — SEC-D19 **Fixed(committed)** · 인증 사용자 한정 힌트만 |
| T-I11 | 계좌·예금주명 유출 | DB 침해·로그 | last4만 저장·payer_name 평문 | **Low** — 전체 계좌번호 미저장(SEC-D21 payer_name 암호화 검토) |
| T-I12 | dev 시크릿 파일 Git 유출 | `git add .` → `dev-backend.env` 커밋 | WT `.gitignore` `*.env`/`scripts/*.env` 무시 | **Low** — SEC-D22 완화 · `git check-ignore` 통과 · parent repo 커밋 대기 |
| T-I13 | pilot 더미 데이터 prod 시딩 | hq_admin이 prod에서 PilotFixturePanel 실행 | `import.meta.env.DEV` 게이트 커밋 | **Low** — SEC-D23 **Fixed** · prod 빌드 미렌더 |
| T-I14 | 첨부 파일 위장(확장자/MIME 위조) | png/pdf/webp 위장한 악성 파일 업로드 | Content-Type 화이트리스트+크기·저장 키 UUID 서버 생성 | **Low~Medium** — SEC-D25 · HR·보수교육·**프로그램 일정 사진(v3)** 표면 추가 · magic-byte 미검증 |
| T-I15 | dev 빌드 체인 RCE | 악의적 NPM registry로 esbuild binary 치환 | overrides `esbuild ^0.25.0` | **Low(dev)** — SEC-D26 GHSA-gv7w-rqvm-qjhr · prod 0건 · CI 격리 권고 |
| T-I16 | health·live-e2e 상태 정보 노출 | `GET /api/v1/health`로 activeProfiles·DB 장애 유형·live-e2e readiness 추론 | permitAll health · DB probe detail sanitize | **Low** — SEC-D30 · prod profile 마스킹 권고 |
| T-I17 | CSV/수식 인젝션 | 이용자명·보호자명에 `=`/`+`/`-`/`@` 삽입 → 명세·NTS export CSV를 Excel로 열 때 수식·DDE 실행 | org+branch RBAC export · `csvEscape` quote(`"`/`,`/`\n`) | **Low** — SEC-D33 · 수식 prefix sanitize(`'` escape) 권고(CWE-1236) |
| T-I18 | staff access key 응답 본문 평문 노출 | 발송 응답 JSON에 6-digit accessKey 포함 시 JWT 탈취·MITM·브라우저 콘솔 캡처 시 유출 | `StaffAccessKeyNotifyResponse`에 `accessKey` 필드 없음 — SMS 채널 전용 전달 | **Low** — 24차 설계 시점부터 응답 record에서 제외 |
| T-I19 | staff access key payload_json at-rest 잔존 | DB 침해/덤프 시 `notifications.payload_json` 평문 accessKey 60분 잔존 노출 | `PasswordResetTokenEntity.tokenHash`는 SHA-256만 저장 · `notifications` 행 60분 TTL 만료 후에도 purge 정책 미정의 | **Low** — SEC-D37 · payload redact 또는 dispatch 완료 시 purge 권고 |
| T-I6 | DB 백업 유출 | 스토리지 침해 | — | **High** | 백업 암호화 |
| T-I7 | PII 전화번호 마스킹 회귀 | 마스킹 제거 빌드 배포 | `PhoneMaskingUtil`·`MaskedPhone` | **Low** — SEC-D9 Fixed · `010-****-5678` 유지 |
| T-I8 | Solapi relay credential 노출 | env 누락·로그 유출 | env 주입·HMAC 헤더 | **Low** — 미설정 fail-closed · 로그에 key/전화 미노출 |

### 3-5. Denial of Service (서비스 거부)

| ID | 위협 | 공격 시나리오 | 현재 통제 | 잔여 위험 | 조치 |
|----|------|---------------|-----------|-----------|------|
| T-D1 | 로그인 flood | mass POST /login | `AuthRateLimitService` (60s window) | **Low (develop)** · **Low (origin/test `598d108`)** |
| T-D2 | 대용량 업로드 | 10MB×N 동시 | multipart limit | Medium | WAF·conn limit |
| T-D3 | xlsx 파싱 CPU | zip bomb xlsx (NHIS·은행입금·RFID·요양보호사 4표면) | multipart limit | Medium | POI 5.4.0+ 업그레이드(SEC-D4 상향) |
| T-D4 | staff access key SMS flood | 인사이더가 직원 N명에게 반복 발송으로 Solapi 비용·SMS 폭주 유발 | `NotificationQuietHoursPolicy`(KST 22:00~08:00 거부) · branch write scope · `@PreAuthorize` HQ/BRANCH/SOCIAL_WORKER만 · `invalidateActiveTokensForUser`로 신규 발급 시 이전 무효화(중복 가치 감소) · audit_logs | **Low** — 추가 rate limit(per-actor·per-staff) 권고(현행 미적용·24차 carry) |
| T-D5 | Accounting BPO SSO handoff flood | 인증된 직원이 handoff 반복 호출로 OTP harvesting·외부 POST | JWT+**HQ/BRANCH only**·`AccountingBpoSsoHandoffRateLimiter`(actor 10/min·org 30/min)·300s OTP window | **Low** — SEC-D43 **Mitigated** |
| T-D6 | US-V06 batch-unconfirm challenge brute | JWT 탈취자가 4-digit challenge를 TTL 내 대량 시도 | actor+org+branch+yearMonth scope·TTL10m·consume-once·SecureRandom · JWT+branch write | **Low** — SEC-D44 entropy 상향 권고 |

### 3-6. Elevation of Privilege (권한 상승)

| ID | 위협 | 공격 시나리오 | 현재 통제 | 잔여 위험 | 조치 |
|----|------|---------------|-----------|-----------|------|
| T-E1 | branch_admin → hq_admin | role 변경 API | `UserService.enforceRolePolicy` (US-R03) | **Low** — branch_admin 역할 부여 allowlist · `platform_admin` 생성 차단 |
| T-E2 | guardian → staff 데이터 | 잘못된 branch_ids | JWT 발급 시 검증 | Low | 유지 |
| T-E3 | ApplicationTemp (CVE) | 동일 호스트 공격자 | Boot **3.3.1** | **Medium** — 패치 라인 업그레이드 검토 | Boot CVE 스캔 |
| T-E4 | 직원 생성 시 상위 역할 부여 | account-request role=ogada_*/hq_admin | `enforceRolePolicy` allowlist(submit+approve 이중)·`createUser` 봉인·`@PreAuthorize` | **Low** — ogada_*/sysadmin/hq_admin 차단·branch_admin allowlist·V161 hq_admin UNIQUE (US-R03·account-request 20차) |
| T-E5 | live-e2e bootstrap 무인증 hq_admin | `LIVE_E2E_BOOTSTRAP_ENABLED=true` 노출 환경 | `@ConditionalOnProperty` 기본 off · `ProductionSecretValidator` prod 거부 · password 필드 0 · blank credential fail-fast · probe default cred 허용(QA-B95) · 24차 HealthControllerTest G21 seed detail lock 추가 | **Low** — SEC-D29 **Mitigated** |
| T-E6 | staff access key brute force | 직원 휴대전화 미보유 공격자가 `/auth/password/reset`에 6-digit 키 시도 | `AuthRateLimitService` ip 20/min·token 8/min · `PasswordResetTokenEntity` 단일활성(invalidateActiveTokensForUser) · 60분 TTL · SHA-256 hash 비교 · 키스페이스 10^6 | **Low** — SEC-D36 Monitor(키 길이/charset 확장 검토·현행 rate limit으로 P(match)≈0.05%/60분/토큰) |
| T-E7 | Accounting BPO SSO 과다 권한·공유 credential | SOCIAL_WORKER·타 org이 동일 시설 SSO mint | **HQ/BRANCH only** · portal **host+path** allowlist · rate limit · JWT·password 미저장·env fail-closed | **Low** — SEC-D43 **Mitigated 강화**(잔여: process-wide env · org-scope 장기) |
| T-E8 | FacilityNotice 첨부 URL 피싱 | 권한 직원이 https://evil.com 게시 → 클릭 유도 | scheme http(s)+≤500 app+V193 · RBAC | **Low** — SEC-D46 host allowlist/내부첨부 권고 |

---

## 4. 공격 트리 (우선 시나리오)

### 시나리오 1: 크로스테넌트 이용자 정보 유출

```
목표: Tenant A 직원이 Tenant B 이용자 PII 조회
├── [1] JWT organization_id 변조 → 실패 (서명 검증)
├── [2] API에 타 org UUID 전달 → 실패 (JWT scope)
├── [3] SQLi로 RLS 우회 → 실패 (파라미터 바인딩)
└── [4] 앱 버그 — scope 검증 누락 엔드포인트 → **가능** (회귀 테스트 필수)
```

**완화**: TSR 크로스테넌트 테스트, 코드 리뷰 체크리스트, (선택) PostgreSQL RLS

### 시나리오 2: 인증 API 브루트포스

```
목표: 유효 계정 비밀번호 탈취
├── [1] POST /auth/login 대량 시도 → **차단**(AuthRateLimitService — develop·`origin/test` 모두 포함)
├── [2] 동일 메시지로 계정 존재 여부 확인 → 어려움 (통일 메시지)
└── [3] reset-request로 이메일 열거 → 어려움 (generic 응답)
```

**완화**: `AuthRateLimitService` ✓(develop·`origin/test` 공통·SEC-D14 Fixed), CAPTCHA (v2), account lockout

### 시나리오 3: 악성 NHIS Excel 업로드

```
목표: 잘못된 청구 데이터 주입 또는 서버 장애
├── [1] duplicate zip entry xlsx → POI 5.3.0 비일관 파싱 (CVE-2025-31672)
├── [2] oversized xlsx → 10MB 제한으로 완화
└── [3] 매크로/외부 링크 → POI 기본 비활성
```

**완화**: POI 5.4.0+, 업로드 전 파일 시그니처, 신뢰 공단 파일만 허용 정책

### 시나리오 4: 프론트엔드 권한 우회 (현재)

```
목표: 미인증 사용자가 /platform 접근
└── [1] URL 직접 입력 → **차단**(develop `ProtectedRoute` 역할 가드 커밋) — 단 클라이언트 가드는 우회 가능
```

**완화**: ProtectedRoute(커밋 완료) + 백엔드 `@PreAuthorize`가 최종 방어 (이중 검증, A-2-3 커버리지 필수)

---

## 5. 신뢰 수준·가정

| 가정 | 신뢰도 | 비고 |
|------|--------|------|
| TLS 종료 LB 정상 구성 | 필수 | 인프라 팀 |
| PostgreSQL 네트워크 격리 | 필수 | API만 접속 |
| 운영 시크릿은 시크릿 매니저 | **부분 충족** (develop prod: `ProductionSecretValidator` / test stale) | test merge + 시크릿 매니저 |
| 파일럿 사용자 기기 무악성 | 낮음 | 보호자 모바일 고려 |
| Spring Boot 단일 JVM 또는 키 공유 | **부분 충족** (develop prod 키 필수; test stale) | test merge |
| 검증 코드 = 배포 산출물 | **충족** — `origin/test`=`598d108`/`ab4de83` P0 포함 · v2/v1.2.1/v1.3 feature merge 잔여(606+286·SEC-D18 더 악화 +14/+20 vs 26차) | SEC-D18 develop→test TSR merge + origin push |

---

## 6. 위협 우선순위 매트릭스

```
영향 ↑
  │  T-E3 CVE        T-I6 백업
  │  T-S1 JWT key    T-S4 프론트
  │  T-D1 brute      T-I1 cross-tenant
  │  T-S2 QR         T-T2 NHIS
  └────────────────────────→ 가능성
```

| 순위 | Threat ID | DREAD (1-10) | 조치 우선 |
|------|-----------|--------------|-----------|
| 1 | T-T2/T-D3 / SEC-D4 | 6 | POI 5.4.0+ — **NHIS·은행입금·RFID·요양보호사** 4 파서 회귀 테스트 |
| 2 | T-E3 / A06-1 | 5 | Spring Boot 패치 라인 업그레이드 |
| 3 | T-I14 / SEC-D25 | 4 | 첨부 magic-byte(HR·보수교육·사진·**프로그램 일정 사진**·xlsx·급여계약서·등급이력·요양보호사) |
| 4 | T-I17 / SEC-D33 | 3 | CSV export 수식 prefix sanitize(명세·NTS) |
| 5 | T-T2 / SEC-D34 | 3 | 요양보호사 import 확장자/Content-Type 검증 |
| 6 | T-I15 / SEC-D26 | 3 | form-data dev 패치 또는 CI 격리(1 HIGH) |
| 7 | T-I12 / SEC-D22 | 3 | parent repo `.gitignore` `*.env` 커밋 |
| 8 | T-E5 / SEC-D29 | 2 | live-e2e prod misconfiguration 방지 — 25차 3-form env 봉인(SEC-D29 진전)·SEC-D38 신규(enforce-readiness 오설정) |
| 9 | T-I6 백업 암호화 | 4 | 인프라 백업 암호화 |
| 10 | T-I11 / SEC-D21·D32 | 2 | `payer_name`·현금영수증 `identifier_value` at-rest 암호화 |
| 11 | T-I16 / SEC-D30 | 2 | prod health `activeProfiles` 마스킹 |
| 12 | SEC-D37 | 2 | `notifications.payload_json` 평문 access key purge·redact 정책(24차 carry) |
| 13 | SEC-D36 | 2 | staff access key 키 길이/charset 확장 검토(현행 rate limit 의존·24차 carry) |
| 14 | SEC-D38 | 2 | **(NEW 25차)** prod `OGADA_LIVE_E2E_ENFORCE_BOOTSTRAP_READINESS=true` 명시·운영 가이드 문서화 |
| 15 | SEC-D39 | 2 | **(NEW 25차)** CMS 가상계좌 번호 guardian 확장 시 last4 마스킹 설계 사전 검토 |
| 16 | SEC-D18 (비대칭) | 2 | **origin/test**: BE **735** push · FE **0**(**★ FULLY SYNCED**) |
| 17 | **SEC-D41** | 3 | SafetyCheck GET date range 가드 |
| 18 | **SEC-D42** | 2 | safety `payload_json` PII 평문 — P3 UUID/암호화 |
| 19 | SEC-D43 residual | 2 | **Mitigated 강화** — path allowlist 착지 · 잔여 org-scoped BPO credential 장기 |
| 20 | **SEC-D44** | 2 | US-V06 batch-unconfirm 4-digit → 6~8 digit/alphanumeric |
| 21 | **SEC-D45** | 2 | kind22 payroll netPay payload redact/purge(SEC-D37 family) |
| 22 | **SEC-D46** | 2 | FacilityNotice attachment host allowlist |
| ✅ | SEC-D35 WT CLEAN · program photo Pass · SEC-D43 path · QA-B95 decode · SEC-D17·D19·D14·D23·D24 | ↓ | develop `a742788`/`592a483` Pass/Mitigated/Fixed |

---

## 7. 모니터링·탐지

| 이벤트 | 탐지 방법 | 대응 |
|--------|-----------|------|
| 로그인 실패 급증 | `login_history` 집계 | IP 차단·알림 |
| RRN reveal 급증 | `audit_logs` `CLIENT_RRN_REVEALED` | 계정 정지·조사 |
| 401/403 급증 | API 로그 | 스캔·권한 오류 조사 |
| NHIS import 실패 | `billing` import 로그 | 파일 격리·분석 |
| 비정상 Tenant 접근 | scope exception 로그 | SEC 에스컬레이션 |

---

## 8. 미해결 질문

> 불확실 항목 — `docs/planning/PLAN_NOTES.md` `### [SEC] 보안 감사 질문` 참조

1. 프로덕션 TLS 종료 지점 (LB vs 앱) — HSTS 적용 주체
2. 백업 스토리지 암호화·접근 제어 상세 (S3/OCI 등)
3. 파일럿 배포 시 MFA 요구 여부

---
*다음 갱신: BE origin/test push(SEC-D18 **735**)·Safety GET date range(SEC-D41)·magic-byte(SEC-D25·program photo 포함)·batch-unconfirm entropy(SEC-D44)·payroll payload redact(SEC-D45)·FacilityNotice host allowlist(SEC-D46)·org-scoped BPO credential(SEC-D43 residual)·safety payload_json PII(SEC-D42·P3)·poi-ooxml 상향(SEC-D4)·CSV 수식 sanitize(SEC-D33)·요양보호사 import(SEC-D34)·Spring Boot 패치(A06-1)·form-data dev(SEC-D26)·`.gitignore` `*.env`(SEC-D22) 또는 신규 src 변경 후*
