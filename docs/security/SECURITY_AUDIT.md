<!-- doc:owner=SEC doc:audience=COD,PLN,TSR updated=2026-06-23T17:00:00+09:00 -->
# 보안 감사 보고서 (security/SECURITY_AUDIT.md)

> **작성**: security_auditor (`SEC`)  
> **감사일**: 2026-06-23 (23차 일일 재점검)  
> **범위**: `src/backend` (Spring Boot 3.3.1, **develop HEAD `5fd12dd`**, **WT DIRTY 9M+1U**), `src/frontend` (React 18 + Vite 6.4.3, **develop HEAD `426d63a`**, **WT DIRTY 38M+11U**), PostgreSQL  
> **baseline**: workspace **git 실측** — backend develop **`5fd12dd`**(+530 vs origin/test) · origin/test **`598d108`**(**530 unpushed**) · frontend develop **`426d63a`**(+187 vs origin/test) · origin/test **`ab4de83`**(**187 unpushed**)  
> **원격 test**: backend **`origin/test` `598d108`** · frontend **`origin/test` `ab4de83`** — **P0 전부 포함**(SEC-D14 Fixed 유지) · develop **530+187 ahead**(신규 기능·보안 통제 누락 아님·origin push 미실행)  
> **워킹트리**: backend **DIRTY**(ClientService 주소 마스킹·LiveE2eBootstrap 테넌트 격리·application.yml·V175 untracked) · frontend **DIRTY**(US-R01-c leave-ledger wire WIP) — **TSR QA-B272/B273 BLOCK(merge pending·dirty)·기능 게이트**  
> **기준**: OWASP Top 10 (2021), 개인정보보호법(PIPA), `docs/ops/DATA_RETENTION_POLICY.md`, `docs/technical/API_SPEC.md`  
> **코드 변경**: 없음 (읽기 전용 점검)

---

## 1. 요약

| 구분 | 결과 |
|------|------|
| 전체 위험도 | **Low~Medium (develop)** — develop `d0c0d12`/`947312c` 기준 **P0 통제 유지** + 21차 이후 **+15 BE / +22 FE** 커밋(**V169 staff_work_attendance 출퇴근 API·V170 billing_report_filters·V171 defense-in-depth integrity + readiness probe·G-BILLING-DEPOSIT-ORDER-GUARD prior-deposit guard·G2 branch-scoped CMS roster API·CMS enrollment input service-layer hardening·US-E03 branch QR PNG 렌더(서명 토큰)·US-D03 client attendance tab·G34-WORKFLOW-CATALOG ezCare FAQ cross-walk·G30-LEGEND** 등) **운영 API 전부 RBAC·tenant-safe Pass**. BE 양 스트림 **SYNCED**(local test=develop) · FE 양 스트림 **SYNCED**(local test=develop). **`origin/test` push 미실행**(514 BE/167 FE unpushed). SEC-D17·D19·D23·D24·D14 Fixed 유지. **★ 22차 신규 audit Open 0건**(BLOCK 없음). **★ 진전**: V171 `staff_work_attendance.check_out_at >= check_in_at` 시간성 CHECK + `billing_report_filters` Tenant FK pairs(org+branch / org+user)·temporal CHECK·`search_query` non-empty CHECK(defense-in-depth) · `V171DefenseInDepthSchemaReadinessProbe`로 `/health`·live-e2e readiness에 미적용 마이그레이션 fail-fast · CMS `normalizePayerName/BankCode/AccountLast4` 서비스 레이어 강제(컨트롤러 우회 방어·보안 긍정) · CMS/easy-pay에 `assertCopayDepositOrder` prior-month guard 적용(외부 PG 호출 전 차단·보안 긍정) · staff attendance checkout-before-checkin 서비스 레이어 가드(`35e6c52`) · QR 코드 클라이언트 렌더링은 **서버 서명 토큰만** `qrcode@1.5.4`로 PNG 인코딩(시크릿 미노출). **유지**: SEC-D33·D34(Low)·SEC-D4(**4 파서**·poi 5.3.0)·SEC-D32 at-rest 평문·SEC-D29 Mitigated·SEC-D26 dev 1 HIGH·SEC-D22(WT만)·SEC-D28·D25·D30·D31·A06-1·origin push gap(SEC-D18 514+167). |
| OWASP Top 10 | develop HEAD: **0건 High**(prod 배포 경로), **5건 Medium**, **나머지 Pass/Low**. `origin/test`: P0 포함(develop 기능 514+167 behind) |
| 의존성 취약점 | Backend: Boot **3.3.1**(A06-1), poi-ooxml **5.3.0**(CVE-2025-31672 — **NHIS·은행입금·RFID·요양보호사 4 파서 표면**, 미해소). OWASP dependency-check **NVD 429 rate-limit으로 미실행**(pom 버전 실측). Frontend: npm audit prod **0건**(신규 `qrcode@1.5.4` 포함) · dev **1건 HIGH**(form-data CRLF GHSA-hmw2-7cc7-3qxx — SEC-D26, dev-only) |
| 즉시 조치 | ① poi-ooxml 5.4.0+(SEC-D4·**4 파서** 회귀) ② Spring Boot 3.3.x 패치(A06-1) ③ CSV export 수식 prefix sanitize(SEC-D33) ④ 요양보호사 import 확장자/Content-Type 검증(SEC-D34) ⑤ parent repo `.gitignore` `*.env`/`scripts/*.env` **커밋**(SEC-D22 WT-only) ⑥ 첨부 magic-byte(SEC-D25) ⑦ form-data `npm audit fix`(SEC-D26) ⑧ **`origin/test` push**(514 BE/167 FE unpushed·SEC-D18) ⑨ prod 간편결제 실 PG(SEC-D28) ⑩ prod `application-prod.yml`(SEC-D5)·health 마스킹(SEC-D30) ⑪ Kakao Maps appkey 도메인 제한(SEC-D31) ⑫ 현금영수증 식별자 at-rest 암호화 검토(SEC-D32·SEC-D21 패턴) |

### 긍정적 통제 (이미 구현됨)

- JWT RS256, refresh 토큰 SHA-256 해시·회전, bcrypt 비밀번호
- **`AuthRateLimitService`** — login·refresh·password-reset IP+account 슬라이딩 윈도우(SEC-D13 Fixed @ `8d42bdd` lineage)
- PII AES-GCM 암호화, API 마스킹, transport pickup 주소·연락처 non-HQ 마스킹, RRN reveal audit
- JPA·JdbcClient 파라미터 바인딩 (SQL Injection 방어)
- `GlobalExceptionHandler` — 500 응답에 스택 트레이스 미노출
- `@PreAuthorize` + `JwtScopeResolver` 멀티테넌트·지점 스코프
- 로그인 실패·비밀번호 재설정 응답 통일 (계정 열거 완화)

---

## 1.25 일일 재점검 델타 (2026-06-23 23차) [SEC]

> 이번 호출에서 **workspace 실측**(`git -C src/backend rev-parse HEAD/origin/test` · `git -C src/frontend …` · `git log d0c0d12..5fd12dd`(+16) / `git log 947312c..426d63a`(+22) · `git status`(양 스트림 **DIRTY**) · `npm audit`/`npm audit --omit=dev` · `pom.xml`(poi 5.3.0 · Boot 3.3.1) · `StaffAnnualLeaveController/Service.java`·`StaffLeaveLedgerController/Service.java`·`SaveStaffAnnualLeaveRequest.java`·`CreateStaffLeaveLedgerEntryRequest.java`·`V172/V173/V174__*.sql`·`V175__staff_leave_ledger_entries_integrity_us_r01c.sql`(untracked)·`NotificationConfig.java`·`NotificationChannelReadinessService.java`(j03 diff)·`ClientService.java`·`application.yml`·`LiveE2eBootstrapService.java` diff)를 22차 `d0c0d12`/`947312c` 기준선과 대조. backend develop **+16 커밋** · frontend develop **+22 커밋** 전진. **양 스트림 WT DIRTY**(22차 CLEAN → 23차 DIRTY).

### (A) 상태 변화 — develop 추가 전진 · 양 스트림 WT DIRTY · origin/test stale 악화

| 스트림 | 22차 develop | 23차 develop HEAD | origin/test | WT |
|--------|--------------|-------------------|-------------|----|
| backend | `d0c0d12` | **`5fd12dd`**(+530 vs origin/test: V172 staff_annual_leave_yearly roster·V173 defense-in-depth + readiness probe·V174 staff_leave_ledger canonical·US-R01/R03e 교차링크·G2 CMS roster status filter·j03 solapi placeholder 거부) | `598d108`(불변·**530 unpushed**) | **DIRTY 9M+1U**(ClientService 주소 마스킹·LiveE2eBootstrap 테넌트 격리·application.yml·live-e2e 테스트·**V175 untracked**) |
| frontend | `947312c` | **`426d63a`**(+187 vs origin/test: US-R01-c leave-ledger 페이지/API client·US-R01 HR roster branch scope·G-STAFF-ANNUAL-LEAVE 페이지·qa-b95 default credential blocker normalize·G2-CMS roster) | `ab4de83`(불변·**187 unpushed**) | **DIRTY 38M+11U**(US-R01-c wire WIP) |

→ **판정**: `origin/test` 양 스트림 P0 통제 유지(SEC-D14 Fixed) — **원격 배포 산출물 보안 회귀 없음**. develop↔origin/test 격차 **530+187**(신규 기능·보안 통제 누락 아님) → **BLOCK 아님**(SEC-D18·악화). QA Open BLOCK은 **QA-B272(BE merge pending·WT DIRTY)·QA-B273(FE WT DIRTY)** — **기능/git-hygiene 게이트**·**보안 BLOCK 없음**.

### (B) ✅ 신규 기능 보안 검토 — 전부 RBAC·tenant-safe Pass

| 기능 (커밋) | 판정 | 근거 |
|-------------|------|------|
| **V172 staff_annual_leave_yearly + roster/yearly/save API** (`41fb84f`·`6b84bcd`) | **Pass · 보안 긍정** | `StaffAnnualLeaveController` GET roster·GET users/{id}=`@PreAuthorize(HQ/BRANCH/SOCIAL_WORKER)` · PUT users/{id}=`@PreAuthorize(BRANCH/SOCIAL_WORKER)` · `requireOrganizationId` + `resolveReadableBranchId`(hq_admin은 branchId 필수·non-hq는 active/단일 branch fallback + allowlist 교차검증) · `requireWritableStaffUser`=`validateBranchWriteScope` + STAFF_ROLE_CODES 4종 + `isActive` 가드 · roster는 `scopedStaffUsers`로 branch 배정 교차 필터 |
| **G-STAFF-ANNUAL-LEAVE 입력 검증 강화** (`a45745c`·`f88e8b1`·`6b35fb5`) | **Pass · 보안 긍정** | year 2000~2100·`MONTHLY_USAGE_MAX=99.9`·`TOTAL_ENTITLEMENT_MAX=999.9`·소수점 1자리 precision·`sum(month) ≤ totalEntitlement`·monthlyUsage ≤12개월 검증 · DTO `@Min/@Max/@Size(max=12)`·memo `@Size(max=2000)`(overlong payload 거부) |
| **V173 staff_annual_leave_yearly defense-in-depth** (`8c5dd65`) | **Pass · defense-in-depth(T-T8 완화)** | month_NN≤99.9·total_entitlement≤999.9·sum≤entitlement·memo non-empty(`btrim>0`)·**user_branch_assignment 3-way FK**(`org+user+branch`→`user_branches`) 5종 CHECK/FK 추가 — raw SQL·향후 일괄 import cross-tenant·교차지점·상한초과 적재 차단 · single-additive ALTER(0행 backfill) |
| **V173 readiness probe** (`8c5dd65`) | **Pass · 보안 긍정** | `V173StaffAnnualLeaveYearlyIntegrityReadinessProbe` — V171 패턴 동일·미적용 마이그레이션 시 `/health`·live-e2e fail-fast(SEC-D24 lineage) |
| **V174 staff_leave_ledger_entries + per-event API** (`bb9df48`) | **Pass · 보안 긍정** | `StaffLeaveLedgerController` list/listForUser=`@PreAuthorize(HQ/BRANCH/SOCIAL_WORKER)` · create/update/delete=`@PreAuthorize(BRANCH/SOCIAL_WORKER)` · `requireWritableStaffUser`·`validateBranchWriteScope`·`requireActorUserId`=`recorded_by` · update/delete는 `findByOrganizationIdAndId`(org 격리) 후 writable 재검증 · leaveType allowlist(ANNUAL_LEAVE/PAID_HOLIDAY)·date order·daysUsed 0<x≤99.9 precision 검증 · V174 스키마: Tenant FK pair 3종(user_org·branch_org·recorded_by_org)·leave_type/days_used/end_date_order/updated_after_created CHECK·UK(org,id) |
| **V175 leave_ledger defense-in-depth** (`untracked` WIP) | **Pass(WIP) · defense-in-depth** | memo non-empty CHECK + user_branch_assignment 3-way FK — V173 패턴 미러 · **단 미커밋(WT untracked)** — 커밋·push 전까지 submodule 재clone 시 유실 위험(SEC-D18 lineage·아래 (C) 참조) |
| **j03 solapi placeholder 거부** (`19ffa84`) | **Pass · 보안 긍정(fail-closed 강화)** | `NotificationConfig.validateSolapiConfiguration`·`NotificationChannelReadinessService`가 `isLiveConfigured`로 `stub/default/placeholder/change-me/replace-me` 마커 값을 **non-live 취급** — placeholder credential 로 live-alimtalk readiness 오보고·bootstrap 방지(SEC-D15/D20 lineage). `contains(marker)` 는 over-rejection(fail-closed)이라 안전 측 동작 |
| **ClientService 주소 마스킹** (WT diff) | **Pass · PII 긍정** | list/detail 응답의 `addressEncrypted`·`pickupAddressEncrypted`를 `maskOptionalDecrypt`(전체 복호) → `maskAddressEncrypted`(시·구·도로명까지·상세번지 `***`)로 변경 — **PII 최소노출 개선**(배차 roster 정책 정합). 커밋 시 SEC-D 신규 긍정 항목 등재 예정 |
| **live-e2e 테넌트 격리** (`application.yml`·`LiveE2eBootstrapService` WT diff) | **Pass · 데이터 격리 긍정** | live-e2e 기본 테넌트 UUID를 `00000001…` → `e2e0000…` 로 분리 — `scripts/seed-dev-fixtures.sql`(00000001/00010101/00000002) 와 **비중첩** 강제 · password 기본값(`ogada1234`) 불변·`ProductionSecretValidator`/`@ConditionalOnProperty` prod 거부 유지(SEC-D29) |
| **US-R01/R03e 교차링크·G2 CMS roster status filter** (`83a26e7`·`6ab3760`·`f1225b0`·`40ab9e7`) | **Pass** | 출퇴근·연차·CMS roster 응답에 relatedSurfaces 메타 추가·status filter allowlist 정규화 — 외부 입력 normalize·tenant scope 동일·새 PII 표면 없음 |
| **FE US-R01-c leave-ledger·HR roster branch scope·qa-b95** (`8057c1e`·`949e9bf`·`a170f9c`·`6fcd750`) | **Pass** | `services.js` leave-ledger API는 `apiFetch` 경유(Bearer·refresh·raw fetch 없음·SEC-D17 유지) · HR roster branch scope 표시는 백엔드 `@PreAuthorize` 최종 방어 · qa-b95 default credential blocker normalize=진단 일관성(보안 가시성 개선) |

### (C) 신규·갱신 이슈

| ID | 항목 | Severity | 상태 | 근거 |
|----|------|----------|------|------|
| — | **23차 신규 BLOCK급 audit Open 0건** | — | — | 신규 leave-ledger/annual-leave API 전부 RBAC·tenant-safe Pass · V173/V174/V175 defense-in-depth · j03·ClientService·live-e2e 격리는 보안 긍정 · 신규 dep 0건(prod audit 0) |
| SEC-D35 | **leave-ledger 무결성 마이그레이션(V175) 미커밋 + 양 스트림 WT DIRTY** | **Low(process)** | **Open(Monitor)** | V175(memo non-empty·user_branch FK) 는 **untracked**(WT만) · BE 9M+1U / FE 38M+11U DIRTY — 커밋·push 전 submodule 재clone 시 무결성 제약·WIP 유실 위험. `rules.md §6`(작업 완료 시 반드시 커밋·push) 위반. **TSR QA-B272/B273 BLOCK**(기능 게이트)과 동일 원인 · **보안 BLOCK 아님** |
| SEC-D18 | origin/test push 미실행 | Low | **Monitor(악화)** | origin/test **530 BE/187 FE unpushed**(22차 514/167 → 23차 530/187·**+16 BE/+20 FE**) |
| SEC-D4 | poi-ooxml **5.3.0** — **4 파서** | **Medium** | **Open** | `pom.xml:64` 5.3.0 — CVE-2025-31672 미해소(신규 파서 추가 없음·4 파서 유지) |
| A06-1 | Spring Boot **3.3.1** | **Medium** | **Open** | `pom.xml:9` 3.3.1 — 패치 라인 업그레이드 검토 |
| SEC-D33 | 명세·NTS CSV export 수식 인젝션 | **Low** | **Open(Monitor)** | 22차와 동일 — `csvEscape` prefix 미중화 |
| SEC-D34 | 요양보호사 import 확장자 미검증 | **Low** | **Open(Monitor)** | 22차와 동일 |
| SEC-D32 | 현금영수증 식별자 at-rest 평문 | **Low** | **Open(Monitor)** | 22차와 동일 |
| SEC-D26 | npm audit dev form-data CRLF | High(dev-only) | **Open(dev)** | prod **0건** · dev **1 HIGH** GHSA-hmw2-7cc7-3qxx(23차 실측 불변) |
| SEC-D29 | live-e2e bootstrap | Low~Medium | **Mitigated** | 테넌트 UUID 격리(WT)로 dev seed 충돌 추가 완화 · validator·password 0 유지 |
| SEC-D22 | `scripts/*.env` gitignore parent HEAD | Low | **Mitigated** | WT `.gitignore` ☑ · parent repo 커밋 대기 |

### (D) ✅ 유지 — Fixed/Pass 재확인

| 항목 | 23차 재확인 |
|------|-------------|
| SEC-D17 raw fetch | **Fixed 유지** — 신규 leave-ledger/annual-leave FE API 전부 `apiFetch` 경유 |
| SEC-D19 error handler | **Fixed 유지** — V173 probe도 exception swallow→`false`(스택 미노출) |
| SEC-D23 PilotFixturePanel | **Fixed 유지** |
| SEC-D24 SecurityConfig 필터 | **Fixed 유지** — V173 readiness probe로 fail-fast 게이트 확장 |
| SEC-D14 origin/test P0 | **Fixed 유지** — `598d108`/`ab4de83` P0 포함 |
| SEC-008 npm audit prod | **Fixed 유지** — prod **0건**(23차 실측) |
| JWT session (SEC-005) | **Pass** — access 메모리 + refresh `sessionStorage` |

### (E) 우선순위 (23차)

| 순위 | ID | Severity | 조치 |
|------|-----|----------|------|
| P1 | SEC-D4 | Medium | poi-ooxml 5.4.0+ — **4 파서** 회귀 |
| P1 | A06-1 | Medium | Spring Boot 3.3.x 패치 라인 |
| P2 | SEC-D35 | Low(process) | **V175 커밋 + develop 커밋·push**(양 스트림 WT clean화) — 무결성 제약 유실 방지 |
| P2 | SEC-D18 | Low(악화) | **origin/test push**(530 BE/187 FE) |
| P2 | SEC-D33 | Low | CSV export 수식 prefix sanitize |
| P2 | SEC-D34 | Low | 요양보호사 import 확장자/Content-Type 검증 |
| P2 | SEC-D26 | High(dev·1건) | form-data `npm audit fix` |
| P2 | SEC-D22 | Low | parent repo `.gitignore` `*.env` 커밋 |
| P2 | SEC-D25 | Low~Medium | 첨부 magic-byte |
| P2 | SEC-D32 | Low | identifier at-rest 암호화 검토 |
| ✅ | V172/V173/V174/V175·readiness probe·j03 placeholder 거부·ClientService 주소 마스킹·live-e2e 격리·SEC-D17·D19·D24·D14 | — | 23차 Pass/Fixed/보안 긍정 |

---

## 1.24 일일 재점검 델타 (2026-06-22 22차) [SEC]

> 이번 호출에서 **workspace 실측**(`git -C src/backend rev-parse HEAD/origin/test/test` · `git -C src/frontend …` · `git log 61e1970..d0c0d12`(+15) / `git log 8383f8d..947312c`(+22) · `git status` · `npm audit`/`npm audit --omit=dev` · `npm ls qrcode` · `pom.xml` · `StaffWorkAttendanceController/Service.java`·`V169__staff_work_attendance_g_staff_work_attendance.sql`·`V170__billing_report_filters.sql`·`V171__staff_work_attendance_and_billing_report_filters_integrity.sql`·`V171DefenseInDepthSchemaReadinessProbe.java`·`HealthController.java`·`BillingReportFilterService.java`·`BillingController.java`·`CmsController/Service.java`·`branchQrCode.js`·`ezcareWorkflowCatalog.js`·`EzcareWorkflowCatalogPanel.jsx`)를 21차 `61e1970`/`8383f8d` 기준선과 대조. backend develop **+15 커밋** · frontend develop **+22 커밋** 전진. **양 스트림 WT CLEAN**. BE develop=test **SYNCED** · FE local test **SYNCED**(21차 +3 behind → 22차 catch-up).

### (A) 상태 변화 — develop 추가 전진 · WT CLEAN · 양 스트림 local test SYNCED · origin/test stale

| 스트림 | 21차 develop | 22차 develop HEAD | local test / origin/test | WT |
|--------|--------------|-------------------|--------------------------|----|
| backend | `61e1970` | **`d0c0d12`**(+514 vs origin/test: V169 staff_work_attendance + manual check-in/out·V170 billing_report_filters·V171 defense-in-depth + readiness probe·prior-deposit guard CMS+easy-pay·G2 branch-scoped CMS roster·CMS input service-layer hardening·attendance checkout temporal guard·live-e2e bootstrap blocker normalize) | local **`d0c0d12`**(SYNCED) / origin **`598d108`**(불변·**514 unpushed**) | **CLEAN** |
| frontend | `8383f8d` | **`947312c`**(+167 vs origin/test: US-D03 client attendance tab·US-E03 branch QR PNG 렌더·US-E05 monthly stats trend·G-BILLING-REPORT-FILTER-PERSISTENCE wire·G-BILLING-DEPOSIT-ORDER-GUARD UI·G-STAFF-WORK-ATTENDANCE 페이지·G34-WORKFLOW-CATALOG ezCare FAQ cross-walk·G30-LEGEND·G2-CMS-ENROLLMENT-ROSTER UI·a11y/QA-B222·vitest serial pool) | local **`947312c`**(SYNCED) / origin **`ab4de83`**(불변·**167 unpushed**) | **CLEAN** |

→ **판정**: `origin/test` 양 스트림 P0 통제 유지(SEC-D14 Fixed) — **원격 배포 산출물 보안 회귀 없음**. develop↔origin/test 격차 **514+167**(신규 기능·보안 통제 누락 아님) → **BLOCK 아님**(SEC-D18). QA Open BLOCK은 **QA-B248(BE develop→test merge pending 1·기능 게이트)** — **보안 BLOCK 없음**.

### (B) ✅ 신규 기능 보안 검토 — 전부 RBAC·tenant-safe Pass

| 기능 (커밋) | 판정 | 근거 |
|-------------|------|------|
| **V169 staff_work_attendance + manual check-in/out API** (`560057f`·`10c0daf`·`61e1970`) | **Pass · 보안 긍정** | `StaffWorkAttendanceController` 3 endpoint 전부 `@PreAuthorize(HQ_ADMIN,BRANCH_ADMIN,SOCIAL_WORKER)` · `requireOrganizationId` + `resolveBranchScope`(`validateBranchReadScope`) · roster=활성 지점 직원 only(`StaffHealthCheckupCompliance.STAFF_ROLE_CODES`·`!TERMINATED` 필터) · 체크인 시 `requireStaffInScope(write=true)` + `validateBranchWriteScope` + `validateStaffBranchAssignment`(user_branches 일치 강제) + `normalizeCheckInMethod` allowlist(`MANUAL/MOBILE/NFC`) · V169 스키마: `org_id` NOT NULL + Tenant FK pair 3종(user_org / branch_org / **user_branch_assignment** 3-way) + `chk_method` enum + `chk_checkout_after_checkin`(pairing) + UK `(org, branch, user, work_date)` |
| **V170 billing_report_filters + GET/PUT /billing/reports/filters** (`479995e`·`fd0a3b3`·`99d03fa`) | **Pass · 보안 긍정** | `BillingController` `/reports/filters` GET·PUT 양쪽 `@PreAuthorize(HQ_ADMIN,BRANCH_ADMIN)` · `BillingReportFilterService.saveFilter`=write scope 강제(`validateBranchWriteScope`) · **read-path autosave** `recordFromReportQuerySafely`는 write scope **skip**(report read는 이미 read scope로 인가됨)+RuntimeException **catch+log**(읽기 응답 흐름 비차단) · 사용자별 `userId=requireActorUserId` + `(org, branch, user, year_month, variant)` UK로 cross-user pollution 방지 · `normalizeVariant` allowlist(`charges/deposits/receipts/refunds`)·`normalizeYearMonth` regex `\d{4}-\d{2}` + `YearMonth.parse`·`normalizeSearchQuery` trim+255 truncate·variant별 filter 조합 검증(`deposits`만 period·`receipts`만 basis) |
| **V171 defense-in-depth integrity** (`6be0c79`·`175d9cb`) | **Pass · defense-in-depth(T-S/T-T8 완화)** | V171에서 (a) `staff_work_attendance.chk_checkout_not_before_checkin`(시간성 `check_out_at >= check_in_at` — 기존 `chk_checkout_after_checkin`은 pairing만) (b) `billing_report_filters` Tenant FK pair 2종(`fk_..._branch_org`·`fk_..._user_org`) — 본 테이블만 누락된 org+branch/user 복합 FK · `chk_updated_after_created`·`chk_search_query_nonempty`(`btrim`>0) 추가 — raw SQL·향후 모바일/NFC 일괄 sync로 cross-tenant 참조·역시각·빈 검색 적재 차단 · single-additive ALTER만(0행 backfill 불요) · 5/5 constraint 확인 |
| **V171DefenseInDepthSchemaReadinessProbe + /health·live-e2e 게이트** (`dce9bf1`·`175d9cb`) | **Pass · 보안 긍정** | `pg_constraint` 5 row 정확 일치(CTE `required_constraints` JOIN COUNT=`EXPECTED_CONSTRAINT_COUNT=5`) 만 ready · `LiveE2eOperationReadinessSupport.v171DefenseInDepthIntegrityCheckReady` `HealthController` `liveE2eOperationBlocker` 게이트 — **미적용 마이그레이션 시 운영 fail-fast**(SEC-D24·D29 lineage 강화) · DataAccessException/RuntimeException catch→false(noisy logging 회피·정보 누출 없음) |
| **G-BILLING-DEPOSIT-ORDER-GUARD CMS+easy-pay prior-deposit guard** (`a6eb8b7`·`abddbee`) | **Pass · 보안 긍정** | `BillingService.assertCopayDepositOrder(claimId)` `CmsService.requestClaimDebit`·`EasyPayService` **FCMS/PG 호출 전** 적용 — 동일 이용자의 과거월 미납 청구가 있으면 자동결제 차단(외부 PG 부수효과 방지·중복 출금·잘못된 입금순서 방어) · 기존 RBAC/tenant scope 동일 |
| **G2 branch-scoped CMS enrollment roster API** (`d361833`·`d0c0d12`) | **Pass** | `CmsController` GET `/cms/enrollments` `@PreAuthorize(HQ_ADMIN,BRANCH_ADMIN)` · `clientId` 있으면 `listClientEnrollments`(client+branch read scope) · 없으면 `listBranchEnrollments`(`resolveBranchScope` validate read · `branchId` 없으면 `TenantContext.activeBranchId` fallback) · `normalizeEnrollmentStatusFilter` allowlist(`ACTIVE/CANCELLED/PENDING`) · response=enrollment + `clientName`(`loadClientNames(organizationId, ids)` tenant 격리) — bankCode/accountLast4/payerName/fcmsMemberId는 **billing 권한자(HQ/BRANCH_ADMIN) 한정** 노출(SEC-D21 패턴 잔존) |
| **CMS enrollment input service-layer hardening** (`9db0bbb`) | **Pass · 보안 긍정** | `CmsService.normalizePayerName/BankCode/AccountLast4`로 컨트롤러 validation 우회(서비스 직접 호출·미래 batch import)에도 강제 — `BANK_CODE_PATTERN=\\d{3}`·`ACCOUNT_LAST4_PATTERN=\\d{4}` regex 엄격 검증 + non-blank · 잘못된 입력 시 BusinessRuleException으로 FCMS 호출/persistence 차단 |
| **staff attendance checkout temporal guard** (`35e6c52`) | **Pass · 보안 긍정** | `StaffWorkAttendanceService.assertCheckoutAtNotBeforeCheckIn` — V171 DB CHECK과 동일 invariant 앱 레이어 명시(BusinessRuleException 메시지로 명확) · timezone consistency(`Asia/Seoul` `OffsetDateTime`) |
| **live-e2e bootstrap blocker reporting normalize** (`24d25f1`·`018a781`·`56cb5d9`) | **Pass · SEC-D29 강화** | bootstrap error suffix hard blocker priority 정규화 — readiness 진단 일관성·noisy DEGRADED 감소(보안 가시성 개선) |
| **US-E03 branch QR PNG 렌더(서명 토큰)** FE (`250619e`·`qrcode@1.5.4`) | **Pass — 안전** | `QrGeneratePage`는 **백엔드 서명 `qrToken`을 클라이언트에서 PNG로만 인코딩**(`branchQrCode.qrTokenToDataUrl`) — 비밀키·토큰 생성 로직 없음 · `qrcode@1.5.4` `npm audit --omit=dev` **0 vuln** · `accept`·`capture`·`alt` 의미 보존 · `target/rel` 미해당(외부 링크 아님) |
| **G34-WORKFLOW-CATALOG ezCare FAQ cross-walk** FE (`77cfc38`·`9f110a5`) | **Pass — 안전** | `EzcareWorkflowCatalogPanel`의 외부 FAQ 링크는 **`target="_blank"` + `rel="noopener noreferrer"`** 적용(tabnabbing/Referer 누출 방어) · `buildEzcareFaqUrl(rowid)` 상수 카탈로그 기반(사용자 입력 없음·URL 인젝션 표면 없음) · 응답에 백엔드 호출 없음(정적 메타) |
| **US-D03 client attendance tab·US-E05 monthly stats trend** FE (`d058e43`·`dffd726`) | **Pass** | `services.js` `fetchClientAttendanceHistoryApi`/`fetchMonthlyAttendanceStatsApi` 신규 — `apiFetch` 경유(Bearer 첨부·refresh 처리) · `from`/`to`/`branchId` 쿼리 직렬화 `toQuery`로 안전 · raw `fetch()` 미사용(SEC-D17 유지) |
| **G-BILLING-DEPOSIT-ORDER-GUARD CmsDebitPanel UI** FE (`dfa981c`) | **Pass** | UI는 백엔드 결정에 따른 표시만 — 인가는 백엔드 최종 방어 |
| **G-STAFF-WORK-ATTENDANCE 페이지 + roster API wire** FE (`53d65a0`·`5fd468b`·`8383f8d`·`947312c`) | **Pass** | `StaffWorkAttendancePage`·`StaffContextNav` 라우트는 `ProtectedRoute` 및 백엔드 `@PreAuthorize` 최종 방어 · check-in method enum FE/BE 일치 |
| **G30-LEGEND official indicator cross-walk** FE (`fdc135b`) | **Pass** | 정적 메타데이터 표시 · 외부 호출 없음 |
| **G2-CMS-ENROLLMENT-ROSTER UI deepen(FilterChips·payment deep links)** FE (`df9ec6c`·`947312c`) | **Pass** | `CmsEnrollmentTable`·`CmsPage`·`PaymentPage` 파라미터 직렬화는 `services.js` 경유 — 백엔드 `branchId`/`status` allowlist 가드와 일치 |
| **vitest serial pool / a11y 재점검** FE (`8383f8d`·`eff8505`·`ebdf737`·`50548ff`·`9812ac4`·`751c593`·`df7f308`·`da34daf`) | **Pass · 영향 없음(테스트 인프라/접근성)** | `vite.config.js` `pool=forks/maxWorkers=1/isolate=true/sequence.concurrent=false` — VITEST_CONCURRENCY 정책 부합 · 보안 코드 변경 없음 |

### (C) 신규·갱신 이슈

| ID | 항목 | Severity | 상태 | 근거 |
|----|------|----------|------|------|
| — | **22차 신규 Open 0건** | — | — | 신규 기능 전부 RBAC·tenant-safe Pass · BLOCK급 회귀 없음 · 신규 dep `qrcode@1.5.4`도 prod audit 0건 |
| SEC-D33 | 명세·NTS CSV export 수식 인젝션 | **Low** | **Open(Monitor)** | 21차와 동일 — `csvEscape` prefix 미중화 |
| SEC-D34 | 요양보호사 import 확장자 미검증 | **Low** | **Open(Monitor)** | 21차와 동일 |
| SEC-D4 | poi-ooxml **5.3.0** — **4 파서** | **Medium** | **Open** | `pom.xml:64` 5.3.0 — CVE-2025-31672 미해소 |
| SEC-D32 | 현금영수증 식별자 at-rest 평문 | **Low** | **Open(Monitor)** | V159 CHECK 유지 · at-rest 평문 잔존 |
| SEC-D29 | live-e2e bootstrap | Low~Medium | **Mitigated** | 22차 V171 readiness probe 추가로 schema fail-fast 게이트 확장 |
| SEC-D26 | npm audit dev form-data CRLF | High(dev-only) | **Open(dev)** | prod **0건**(신규 `qrcode@1.5.4` 포함) · dev **1 HIGH** GHSA-hmw2-7cc7-3qxx |
| SEC-D22 | `scripts/*.env` gitignore parent HEAD | Low | **Mitigated** | WT `.gitignore`에 `*.env`/`scripts/*.env`·`!*.env.example` ☑ · `git check-ignore scripts/dev-backend.env` 통과 · **`git show HEAD:.gitignore`는 `.env`/`.env.*`만**(`M .gitignore` 미커밋) |
| SEC-D18 | origin/test push 미실행 | Low | **Monitor(악화)** | 양 스트림 local test SYNCED · origin/test **514 BE/167 FE unpushed**(21차 500/147 → 22차 514/167·**+14 BE/+20 FE**) |

### (D) ✅ 유지 — 21차 Fixed/Pass 재확인

| 항목 | 22차 재확인 |
|------|-------------|
| SEC-D17 raw fetch | **Fixed 유지** — 앱 코드 raw `fetch()`는 `src/api/http.js` + e2e harness 전용 · 신규 `services.js` 추가분(reportFilters/attendance/cmsRoster/branchQr) 전부 `apiFetch` |
| SEC-D19 error handler | **Fixed 유지** — `GlobalExceptionHandler` 고정 메시지 · V171 probe도 exception swallow→`false`만 반환(스택 미노출) |
| SEC-D23 PilotFixturePanel | **Fixed 유지** — DEV/VITE 게이트 |
| SEC-D24 SecurityConfig 필터 | **Fixed 유지** — tenant filter after BearerToken · 신규 V171 probe로 readiness fail-fast 강화 |
| SEC-D14 origin/test P0 | **Fixed 유지** — backend `598d108`·frontend `ab4de83` P0 포함 |
| SEC-008 npm audit prod | **Fixed 유지** — prod **0건**(22차 실측 · 신규 `qrcode@1.5.4` 포함 prod 77 deps 0 vuln) |
| JWT session (SEC-005) | **Pass** — access 메모리 + refresh `sessionStorage` (`session.js`) |

### (E) 우선순위 (22차)

| 순위 | ID | Severity | 조치 |
|------|-----|----------|------|
| P1 | SEC-D4 | Medium | poi-ooxml 5.4.0+ — **4 파서** 회귀 |
| P1 | A06-1 | Medium | Spring Boot 3.3.x 패치 라인 |
| P2 | SEC-D33 | Low | CSV export 수식 prefix sanitize |
| P2 | SEC-D34 | Low | 요양보호사 import 확장자/Content-Type 검증 |
| P2 | SEC-D26 | High(dev·1건) | form-data `npm audit fix` |
| P2 | SEC-D22 | Low | parent repo `.gitignore` `*.env` **커밋** |
| P2 | SEC-D25 | Low~Medium | 첨부 magic-byte(HR mobile capture 포함) |
| P2 | SEC-D18 | Low(악화) | **origin/test push**(514 BE/167 FE — 21차 대비 +14/+20) |
| P2 | SEC-D32 | Low | identifier at-rest 암호화 검토 |
| P2 | SEC-D28·D30·D31·D5 | Low | prod easy-pay·health·Kakao·application-prod.yml |
| ✅ | V169/V170/V171·readiness probe·deposit-order guard·CMS input hardening·attendance checkout guard·QR signed token render·SEC-D17·D19·D23·D24·D14 | — | 22차 Pass/Fixed/보안 긍정 |

---

## 1.23 일일 재점검 델타 (2026-06-21 21차) [SEC]

> 이번 호출에서 **workspace 실측**(`git -C src/backend rev-parse HEAD/origin/test/test` · `git -C src/frontend …` · `git log 6f7f145..61e1970`(+30) / `git log a0f051d..8383f8d`(+36) · `git status` · `npm audit`/`npm audit --omit=dev` · `pom.xml` · `OverdueManagementService.java`·`V168__billing_overdue_management_and_adjustments_integrity.sql`·`AttendanceController/Service.java`·`BathingScheduleController.java`·`StaffHrFileController/Service.java`·`StaffDocumentRepositoryPanel.jsx`·`FileUpload.jsx`)를 20차 `6f7f145`/`a0f051d` 기준선과 대조. backend develop **+30 커밋** · frontend develop **+36 커밋** 전진. **양 스트림 WT CLEAN**. BE develop=test **SYNCED** · FE local test **+3 behind develop**.

### (A) 상태 변화 — develop 추가 전진 · WT CLEAN · BE test SYNCED · origin/test stale

| 스트림 | 20차 develop | 21차 develop HEAD | local test / origin/test | WT |
|--------|--------------|-------------------|--------------------------|----|
| backend | `6f7f145` | **`61e1970`**(+500 vs origin/test: overdue CRM/adjustment·V168 integrity·attendance roster·bathing prev-month copy·staff doc repository·SMS guard) | local **`61e1970`**(SYNCED) / origin **`598d108`**(불변·**500 unpushed**) | **CLEAN** |
| frontend | `a0f051d` | **`8383f8d`**(+147 vs origin/test: overdue UI·attendance roster wire·bathing prev-month·staff doc repository·mobile camera capture·vitest serial pool) | local **`a4ea2d5`**(+3 behind develop) / origin **`ab4de83`**(불변·**147 unpushed**) | **CLEAN** |

→ **판정**: `origin/test` 양 스트림 P0 통제 유지(SEC-D14 Fixed) — **원격 배포 산출물 보안 회귀 없음**. develop↔origin/test 격차 **500+147**(신규 기능·보안 통제 누락 아님) → **BLOCK 아님**(SEC-D18). **보안 BLOCK 없음**.

### (B) ✅ 신규 기능 보안 검토 — 전부 RBAC·tenant-safe Pass

| 기능 (커밋) | 판정 | 근거 |
|-------------|------|------|
| **G-BILLING-OVERDUE-ADJUSTMENT** BE API+FE wire + live RBAC tests (`4d92844`·`0420e6b`·`c17097d`) | **Pass — 보안 긍정** | `@PreAuthorize(HQ_ADMIN,BRANCH_ADMIN)` only · `requireOrganizationId`·`validateBranchWriteScope` · `requireOverdueClaim`/`requireClaimItem` org+claim+client 교차 검증 · 조정 시 `copayAmount` 감소만 허용 · audit `recordedBy=requireActorUserId()` |
| **V168 overdue integrity** (`399c698`) | **Pass — defense-in-depth** | `billing_overdue_management_records`·`billing_overdue_adjustments`에 **note/reason non-empty CHECK** · `recorded_at >= created_at` · **Tenant FK pairs**(org+branch/claim/client/recorded_by) · purge/audit backing index — raw SQL·batch import 우회 차단(T-T8 완화) |
| **Overdue SMS auto-record guard** (`f6266ec`·`a45c040`) | **Pass — 보안 긍정** | `recordAutomaticSmsRemindersForClaim`: CONFIRMED+과거 청구월만 · org scope · `existsBy…AutoGeneratedIsTrue` **중복 방지** · branch write scope |
| **attendance roster daily list** clientName+status (`0c69060`·`61e1970`) | **Pass** | `@PreAuthorize(HQ/BRANCH/SOCIAL_WORKER/CAREGIVER)` · `resolveBranchScope`·`requireOrganizationId` · roster=**활성 지점 수급자 전원**(clientName은 지점 스코프 내 PII·역할 허용 범위) · derived status(`CHECKED_IN/CHECKED_OUT/ABSENT`) 서버 계산 |
| **G-BATHING 전월복사** (`49a1721`·`9a957fb`) | **Pass** | `@PreAuthorize(HQ/BRANCH/SOCIAL_WORKER)` bulk copy — caregiver 제외(일괄 생성 권한 분리) · tenant+branch scope 기존 BathingScheduleService 경유 |
| **G-STAFF-DOCUMENT-REPOSITORY** 21-slot progress (`b583c11`·`03d0d43`) | **Pass** | `@PreAuthorize(HQ/BRANCH/SOCIAL_WORKER)` read · upload=`BRANCH_ADMIN/SOCIAL_WORKER` · `requireReadableStaffUser`/`requireWritableStaffUser` org+branch 교차 · 기존 `StaffHrFileStorageService` Content-Type allowlist(SEC-D25 표면) |
| **US-R03 mobile camera capture** (`6bde24a`·`StaffDocumentRepositoryPanel`/`FileUpload`) | **Pass · SEC-D25 표면 유지** | 클라이언트 `<input capture="environment" accept="image/*">`만 추가 — **서버 업로드 경로 동일**(`StaffHrFileController` multipart) · Content-Type 화이트리스트·크기 제한·UUID storage key 서버 생성(SEC-D25 magic-byte 미검증은 잔존) |
| **live-e2e bootstrap/readiness hardening** (`20485f1`·`018a781`·`56cb5d9`) | **Pass · SEC-D29 강화** | bootstrap error suffix hard blocker · operation blocker priority · password 필드 0·prod validator 유지 |

### (C) 신규·갱신 이슈

| ID | 항목 | Severity | 상태 | 근거 |
|----|------|----------|------|------|
| — | **21차 신규 Open 0건** | — | — | 신규 기능 전부 RBAC·tenant-safe Pass · BLOCK급 회귀 없음 |
| SEC-D33 | 명세·NTS CSV export 수식 인젝션 | **Low** | **Open(Monitor)** | 20차와 동일 — `csvEscape` prefix 미중화 |
| SEC-D34 | 요양보호사 import 확장자 미검증 | **Low** | **Open(Monitor)** | 20차와 동일 |
| SEC-D4 | poi-ooxml **5.3.0** — **4 파서** | **Medium** | **Open** | `pom.xml:64` 5.3.0 — CVE-2025-31672 미해소 |
| SEC-D32 | 현금영수증 식별자 at-rest 평문 | **Low** | **Open(Monitor)** | V159 CHECK 유지 · at-rest 평문 잔존 |
| SEC-D29 | live-e2e bootstrap | Low~Medium | **Mitigated** | 21차 readiness/blocker 게이트 추가로 강화 |
| SEC-D26 | npm audit dev form-data CRLF | High(dev-only) | **Open(dev)** | prod **0건** · dev **1 HIGH** GHSA-hmw2-7cc7-3qxx |
| SEC-D22 | `scripts/*.env` gitignore parent HEAD | Low | **Mitigated** | WT `.gitignore`에 `*.env`/`scripts/*.env` ☑ · **`git show HEAD:.gitignore`는 `.env`/`.env.*`만**(`M .gitignore` 미커밋) |
| SEC-D18 | origin/test push 미실행 | Low | **Monitor** | BE test SYNCED · FE test +3 behind · origin/test **500 BE/147 FE unpushed** |

### (D) ✅ 유지 — 20차 Fixed/Pass 재확인

| 항목 | 21차 재확인 |
|------|-------------|
| SEC-D17 raw fetch | **Fixed 유지** — 앱 코드 raw `fetch()`는 `http.js` + e2e harness 전용 |
| SEC-D19 error handler | **Fixed 유지** — `GlobalExceptionHandler` 고정 메시지 |
| SEC-D23 PilotFixturePanel | **Fixed 유지** — DEV/VITE 게이트 |
| SEC-D24 SecurityConfig 필터 | **Fixed 유지** — tenant filter after BearerToken |
| SEC-D14 origin/test P0 | **Fixed 유지** — backend `598d108`·frontend `ab4de83` P0 포함 |
| SEC-008 npm audit prod | **Fixed 유지** — prod **0건**(21차 실측) |
| JWT session (SEC-005) | **Pass** — access 메모리 + refresh `sessionStorage` (`session.js`) |

### (E) 우선순위 (21차)

| 순위 | ID | Severity | 조치 |
|------|-----|----------|------|
| P1 | SEC-D4 | Medium | poi-ooxml 5.4.0+ — **4 파서** 회귀 |
| P1 | A06-1 | Medium | Spring Boot 3.3.x 패치 라인 |
| P2 | SEC-D33 | Low | CSV export 수식 prefix sanitize |
| P2 | SEC-D34 | Low | 요양보호사 import 확장자/Content-Type 검증 |
| P2 | SEC-D26 | High(dev·1건) | form-data `npm audit fix` |
| P2 | SEC-D22 | Low | parent repo `.gitignore` `*.env` **커밋** |
| P2 | SEC-D25 | Low~Medium | 첨부 magic-byte(HR mobile capture 포함) |
| P2 | SEC-D18 | Low | **origin/test push**(500 BE/147 FE) |
| P2 | SEC-D32 | Low | identifier at-rest 암호화 검토 |
| P2 | SEC-D28·D30·D31·D5 | Low | prod easy-pay·health·Kakao·application-prod.yml |
| ✅ | overdue CRM/adjustment·V168·attendance roster·bathing copy·staff doc repo·mobile capture·SEC-D17·D19·D23·D24·D14 | — | 21차 Pass/Fixed/보안 긍정 |

---

## 1.22 일일 재점검 델타 (2026-06-20 20차) [SEC]

> 이번 호출에서 **workspace 실측**(`git -C src/backend rev-parse HEAD/origin/test/test/origin/develop` · `git -C src/frontend …` · `git log f79a19e..6f7f145`(+37) / `git log d80f9dc..a0f051d`(+41) · `git status` · `npm audit`/`npm audit --omit=dev` · `pom.xml` · `StaffNhisCaregiverImportController/Service/ExcelParser.java`·`UserAccountRequestController/PlatformUserAccountRequestController/Service.java`·`UserService.java`·`BillingController.java`·`BillingStatementExportService.java`·`BillingService.exportMedicalExpenseDeductionNtsCsv`·`V159`·`V160`·`V161`·`V162`·`NhisImportService.validateFile`)를 19차 `f79a19e`/`d80f9dc` 기준선과 대조. backend develop **+37 커밋** · frontend develop **+41 커밋** 전진. **양 스트림 WT CLEAN**. FE develop=test **SYNCED** · BE local test **+1 behind develop**.

### (A) 상태 변화 — develop 추가 전진 · WT CLEAN · FE test SYNCED · origin/test stale

| 스트림 | 19차 develop | 20차 develop HEAD | local test / origin/test | WT |
|--------|--------------|-------------------|--------------------------|----|
| backend | `f79a19e` | **`6f7f145`**(+470 vs origin/test: G-STAFF-NHIS-EXCEL-IMPORT·staff account-request workflow·platform_admin rename·G-7-1/g26 CSV export·g14 care plan·전국 법정동 seed·V159) | local **`07a85a3`**(+1 behind develop) / origin **`598d108`**(불변·**470 unpushed**) | **CLEAN** |
| frontend | `d80f9dc` | **`a0f051d`**(+111 vs origin/test: US-R03 근로재계약·US-H01 HQ drill-down·G-7-1/G26 export UI·현금영수증 identifier 검증·branch road address·transport roster) | local **`a0f051d`**(SYNCED) / origin **`ab4de83`**(불변·**111 unpushed**) | **CLEAN** |

→ **판정**: `origin/test` 양 스트림 P0 통제 유지(SEC-D14 Fixed) — **원격 배포 산출물 보안 회귀 없음**. develop↔origin/test 격차 **470+111**(신규 기능·보안 통제 누락 아님) → **BLOCK 아님**(SEC-D18). **보안 BLOCK 없음**.

### (B) ✅ 신규 기능 보안 검토 — 전부 RBAC·tenant-safe Pass

| 기능 (커밋) | 판정 | 근거 |
|-------------|------|------|
| **tenant staff account-request workflow** `UserAccountRequestController`·`PlatformUserAccountRequestController`·`UserAccountRequestService` + V161/V162 (`5e1b656`) | **Pass — 보안 긍정** | submit=`@PreAuthorize(HQ/BRANCH)`·`requireOrganizationId`·branch scope · approve/reject=`@PreAuthorize(OGADA_PLATFORM_ADMIN)` only · **`enforceRolePolicy` 권한상승 차단**(`isOgadaOnlyRole`=`ogada_*`/`sysadmin`/`platform_admin` 거부·`hq_admin` tenant API 차단·branch_admin allowlist) · approve 시 `provisionApprovedAccount`가 enforceRolePolicy **재검증** + `passwordEncoder.encode`(bcrypt) · 이메일 중복·branch 소속 검증 · **V161 org당 hq_admin 1명 UNIQUE** · 직접 `createUser` 경로는 BusinessRuleException으로 봉인(승인 경유만) |
| **platform_admin → ogada_platform_admin rename** V160 + `AuthService`·controllers (`3023c9e`) | **Pass — 보안 긍정** | V160 마이그레이션 **제약 DROP→UPDATE→ADD→인덱스 교체** 안전 순서(기존 배포 데이터 호환) · `@PreAuthorize("hasRole('OGADA_PLATFORM_ADMIN')")`·`AuthService` redirect/elevation 분기·`chk_users_role_code` allowlist·전역 email 부분 인덱스 모두 신규 role_code 정렬 · 잔여 `platform_admin` 문자열은 **과거 마이그레이션(V2/V3/V5/V8/V28/V30) 이력**과 `UserService.OGADA_ONLY_ROLES` deny-list(구·신 동시 차단)뿐 — **인가 우회 갭 없음** |
| **G-STAFF-NHIS-EXCEL-IMPORT** `StaffNhisCaregiverImportController`·`Service`·`ExcelParser` (`6f7f145`) | **Pass · SEC-D4 표면 +1 · SEC-D34 신규** | `@PreAuthorize(HQ/BRANCH)` preview/import · `requireOrganizationId`·`validateBranchRead/WriteScope` · 생성 역할 **`caregiver` 하드코딩**(권한상승 불가) → account-request 경유(직접 user 생성 아님) · audit_logs **건수만**(이름·전화 미로깅) · **POI `WorkbookFactory`**(untrusted xlsx — CVE-2025-31672 **4번째 파서**) · **확장자/Content-Type 미검증**(`NhisImportService.validateFile`의 `.xlsx` 체크 부재 — SEC-D34 Low) · 파싱 PII(이름·생년월일·전화)는 **요청 응답(HQ/BRANCH 인가)·account-request(email·name만)**로 한정 |
| **G-7-1 billing statement CSV export** `BillingStatementExportService` (`e454d3b`) | **Pass · SEC-D33 신규** | `@PreAuthorize(HQ/BRANCH)`·org+branch write scope · CONFIRMED/PAID만·영수증은 PAID만 · **PII 최소화**(보호자 전화 `getPhoneMasked()`·주소는 region label 2토큰만·RRN 없음) · UTF-8+BOM CSV · **`csvEscape`가 `"`/`,`/`\n`만 quote — 수식 prefix(`=`/`+`/`-`/`@`) 미중화**(SEC-D33 CWE-1236 Low) |
| **g26 의료비공제 NTS CSV export** `BillingService.exportMedicalExpenseDeductionNtsCsv` (`ceeaeb9`·`58ff35e`) | **Pass · SEC-D33 동일** | `@PreAuthorize(HQ/BRANCH)`·tenant scope · 출력=이용자명·**인증번호(장기요양인정번호·RRN 아님)**·청구월·금액·공제대상 · 동일 `csvEscape` 수식 미중화(SEC-D33) |
| **V159 현금영수증 identifier 숫자 CHECK** (`15061a9`·`4da0ca8`·`35d1560`) | **Pass — SEC-D32 무결성 보강** | `chk_..._identifier_value_format` = `~ '^[0-9]+$'` + PHONE 10~11·BIZ 10 길이 — 앱 `normalize/validateIdentifierValue` 계약을 **DB-level**로 다층 방어 · **단 at-rest 평문(숫자) 잔존**(SEC-D32 Low 유지) |
| **g14 급여제공계획서(V164)·전국 법정동 seed(V163)·transport Kakao usage·j03 quiet-hours** | **Pass** | g14·care plan 기존 client RBAC 경유 · V163 region seed는 참조 데이터(PII 없음) · KakaoApi usage tracker 카운터 메타만 · j03 quiet-hours는 발송 게이트 강화(보안 긍정) |

### (C) 신규·갱신 이슈

| ID | 항목 | Severity | 상태 | 근거 |
|----|------|----------|------|------|
| **SEC-D33** | **명세·NTS CSV export 수식(formula) 인젝션 미방어** | **Low** | **Open(Monitor)** | `BillingStatementExportService.csvEscape`·`BillingService.csvEscape` 모두 `"`/`,`/`\n`만 quote · 이용자명·보호자명 등 사용자 입력이 `=`/`+`/`-`/`@`(또는 탭·CR)로 시작하면 Excel/Calc에서 수식·DDE 실행 가능(CWE-1236) · 작성자=인증된 tenant 사용자·열람 시 Excel 경고 필요로 영향 제한 → **권장**: 위험 prefix를 `'`(apostrophe) 또는 공백으로 escape |
| **SEC-D34** | **요양보호사 import 확장자/Content-Type 미검증** | **Low** | **Open(Monitor)** | `StaffNhisCaregiverImportService.buildImportBatch`는 `file.isEmpty()`만 확인하고 `WorkbookFactory.create` 자동판별에 의존 — 기존 `NhisImportService.validateFile`(`.xlsx` 강제)·POI 5.3.0 CVE-2025-31672 표면(4번째)과 정합 위해 확장자/Content-Type pre-check 추가 권장(SEC-D25/C-5 패턴) |
| SEC-D4 | poi-ooxml **5.3.0** — **4 파서 표면** | **Medium** | **Open** | `pom.xml:64` 5.3.0 — CVE-2025-31672 미해소 · NHIS·은행입금·RFID(G21)·**요양보호사(신규)** 4 파서 |
| SEC-D32 | 현금영수증 식별자 at-rest 평문 | **Low** | **Open(Monitor)** | V159로 **숫자/길이 무결성** DB CHECK 추가(긍정)되었으나 값은 평문 숫자 저장 · API `maskIdentifier()`·HQ/BRANCH RBAC로 영향 제한 — SEC-D21 패턴으로 암호화 검토 |
| SEC-D29 | live-e2e 무인증 bootstrap | Low~Medium | **Mitigated** | `ProductionSecretValidator` prod 거부 · 응답 password 0 · blank credential fail-fast(trim) · 20차 추가 live-e2e 강화(`1283153`·`8b3f66d`·`1134b2d` readiness 게이트) |
| SEC-D26 | npm audit dev form-data CRLF | High(dev-only) | **Open(dev)** | prod `--omit=dev` **0건** · dev **1 HIGH** GHSA-hmw2-7cc7-3qxx — 19차와 동일 |
| SEC-D22 | `scripts/*.env` gitignore parent HEAD | Low | **Mitigated** | WT `.gitignore` `*.env`/`scripts/*.env` · `git check-ignore scripts/dev-backend.env` 통과 · **`git show HEAD:.gitignore`는 `.env`/`.env.*`만**(`*.env` 미반영·parent `M .gitignore` 미커밋) |
| SEC-D18 | origin/test push 미실행 | Low | **Monitor** | FE test SYNCED · BE test +1 behind · origin/test **470 BE/111 FE unpushed** |
| SEC-D25·D28·D30·D31·D27·A06-1 | 첨부 magic-byte·easy-pay·health·Kakao·NHIS xls·Boot 3.3.1 | Low~Medium | Monitor/Open | 19차와 동일 |

### (D) ✅ 유지 — 19차 Fixed/Pass 재확인

| 항목 | 20차 재확인 |
|------|-------------|
| SEC-D17 raw fetch | **Fixed 유지** — 앱 코드 raw `fetch()`는 `src/api/http.js` + e2e harness 전용 |
| SEC-D19 error handler | **Fixed 유지** — `GlobalExceptionHandler` 고정 메시지 |
| SEC-D23 PilotFixturePanel | **Fixed 유지** — `import.meta.env.DEV \|\| VITE_ENABLE_PILOT_FIXTURE` |
| SEC-D24 SecurityConfig 필터 | **Fixed 유지** — tenant filter after BearerToken |
| SEC-D14 origin/test P0 | **Fixed 유지** — backend `598d108`·frontend `ab4de83` P0 포함 |
| SEC-008 npm audit prod | **Fixed 유지** — prod **0건**(20차 실측) |

### (E) 우선순위 (20차)

| 순위 | ID | Severity | 조치 |
|------|-----|----------|------|
| P1 | SEC-D4 | Medium | poi-ooxml 5.4.0+ — **NHIS·은행입금·RFID·요양보호사** 4 파서 회귀 |
| P1 | A06-1 | Medium | Spring Boot 3.3.x 패치 라인 |
| P2 | SEC-D33 | Low | CSV export 수식 prefix sanitize(`'` escape) — 명세·NTS 공통 |
| P2 | SEC-D34 | Low | 요양보호사 import 확장자/Content-Type 검증 |
| P2 | SEC-D26 | High(dev·1건) | form-data `npm audit fix` |
| P2 | SEC-D22 | Low | parent repo `.gitignore` `*.env` **커밋** |
| P2 | SEC-D25 | Low~Medium | 첨부 magic-byte 검증 |
| P2 | SEC-D18 | Low | **origin/test push**(470 BE/111 FE) |
| P2 | SEC-D32 | Low | identifier at-rest 암호화 검토(V159 무결성은 보강됨) |
| P2 | SEC-D28·D30·D31·D5 | Low | prod easy-pay·health 마스킹·Kakao 도메인·application-prod.yml |
| ✅ | staff account-request·platform_admin rename·G-STAFF-NHIS·G-7-1/g26 export·V159·SEC-D17·D19·D23·D24·D14 | — | 20차 Pass/Fixed/보안 긍정 |

---

## 1.21 일일 재점검 델타 (2026-06-19 19차) [SEC]

> 이번 호출에서 **workspace 실측**(`git -C src/backend rev-parse HEAD/origin/test/test` · `git -C src/frontend …` · `git log 28860ae..f79a19e` / `git log 50d330d..d80f9dc` · `git status` · `npm audit`/`npm audit --omit=dev` · `pom.xml` · `CashReceiptIssuanceService.java`·`BillingController.java`·`V158__cash_receipt_issuances.sql`·`CaseManagementController.java`·`CaseManagementService.java`·`V157`·`LiveE2eBootstrapService.java`·`SecurityConfig.java`)을 18차 `28860ae`/`50d330d` 기준선과 대조. backend develop **+34 커밋** · frontend develop **+38 커밋** 전진. **양 스트림 WT CLEAN**. BE develop=test **SYNCED** · FE develop **+3 ahead of local test**.

### (A) 상태 변화 — develop 추가 전진 · WT CLEAN · BE test SYNCED · origin/test stale

| 스트림 | 18차 develop | 19차 develop HEAD | local test / origin/test | WT |
|--------|--------------|-------------------|--------------------------|----|
| backend | `28860ae` | **`f79a19e`**(+433 vs origin/test: G32 attendee opinions·G-CASH-RECEIPT-LOG·live-e2e G32 readiness·credential trim) | local **`f79a19e`**(SYNCED) / origin **`598d108`**(불변·**433 unpushed**) | **CLEAN** |
| frontend | `50d330d` | **`d80f9dc`**(+71 vs origin/test: G21 split NHIS·G32 UI·G-CASH-RECEIPT page·UXD-138 a11y·QA-B153 test fix) | local **`9b80505`**(+3 behind develop) / origin **`ab4de83`**(불변·**71 unpushed**) | **CLEAN** |

→ **판정**: `origin/test` 양 스트림 P0 통제 유지(SEC-D14 Fixed) — **원격 배포 산출물 보안 회귀 없음**. develop↔origin/test 격차 **433+71**(신규 기능·보안 통제 누락 아님) → **BLOCK 아님**(SEC-D18). QA Open BLOCK은 **QA-B153(FE develop 단위 회귀·기능)** — **보안 BLOCK 없음**.

### (B) ✅ 신규 기능 보안 검토 — 전부 RBAC·tenant-safe Pass

| 기능 (커밋) | 판정 | 근거 |
|-------------|------|------|
| **G32 attendee opinions** `CaseManagementController` + V157 JSONB CHECK (`8835aa2`·`5222a8f`·`eed39ab`) | **Pass — 보안 긍정** | `@PreAuthorize(HQ/BRANCH/SOCIAL_WORKER)` write · `requireOrganizationId`·branch scope · `normalizeAttendeeOpinions`·`validateAttendeeOpinions`(참석자 1:1·중복 거부·최소 2명) · V157 `jsonb_typeof = 'array'` DB-level 가드 · `AttendeeOpinionsCodec` malformed JSON 거부(테스트 커버) |
| **G32 dashboard gap count** · **live-e2e G32 schema readiness** (`b9e0947`·`45d95ea`·`caeac0d`) | **Pass** | read RBAC · tenant scope · probe는 compliance 집계 메타만(PII 없음) · `attendeeOpinionsArrayCheckReady` 운영 readiness 게이트 |
| **G-CASH-RECEIPT-LOG** `BillingController` cash-receipt endpoints + V158 (`4432558`·`f79a19e`) | **Pass · SEC-D32 신규** | `@PreAuthorize(HQ_ADMIN\|BRANCH_ADMIN)` only · `requireOrganizationId`·`validateBranchRead/WriteScope` · PAID+CASH 청구만·1청구 1발급·금액=본인부담금 검증 · 응답 `maskIdentifier()` · **at-rest `identifier_value` 평문**(SEC-D32 Low) · profile `suggestedIdentifierValue`는 암호화된 client phone 복호화 후 **HQ/BRANCH_ADMIN 전용** prefill |
| **live-e2e credential trim** `LiveE2eBootstrapService` (`7848b0f`) | **Pass — 강화** | staff/guardian credential **trim** 후 readiness·seed reconciliation — whitespace-padded env로 인한 오탐 bootstrap 실패 방어(SEC-D29 긍정) |
| **G21 split NHIS comparison panel** (FE `9b80505`·`d354a0e`) | **Pass** | 기존 visit RBAC·`apiFetch`·`validateImportFile` 경유 · 신귀 공개 endpoint 없음 |
| **FE CashReceiptIssuancePage** (`cfc4b04`) | **Pass** | `fetchCashReceiptIssuancesApi`·`createCashReceiptIssuanceApi` **`services.js`/`apiFetch`** · `ProtectedRoute` · 역할 가드는 백엔드 최종 방어 |

### (C) 신규·갱신 이슈

| ID | 항목 | Severity | 상태 | 근거 |
|----|------|----------|------|------|
| **SEC-D32** | **현금영수증 발급 식별자 at-rest 평문** | **Low** | **Open(Monitor)** | `V158` `cash_receipt_issuances.identifier_value VARCHAR(32)` 평문 저장(PHONE/BIZ) · API 응답은 `maskIdentifier()`(010****1234) · SEC-D21 `cms_enrollments.payer_name` 패턴과 동일 갭. HQ/BRANCH_ADMIN RBAC·tenant 격리로 영향 제한 |
| SEC-D4 | poi-ooxml **5.3.0** — **3 파서 표면** | **Medium** | **Open** | `pom.xml:64` 5.3.0 — CVE-2025-31672 미해소 · G21 xlsx 표면 변동 없음 |
| SEC-D29 | live-e2e 무인증 bootstrap | Low~Medium | **Mitigated** | `7848b0f` credential trim 강화 · `ProductionSecretValidator` prod 거부 · 응답 password 0 · probe default guardian cred 허용(non-prod) |
| SEC-D26 | npm audit dev form-data CRLF | High(dev-only) | **Open(dev)** | prod `--omit=dev` **0건** · dev **1 HIGH** GHSA-hmw2-7cc7-3qxx — 18차와 동일 |
| SEC-D22 | `scripts/*.env` gitignore parent HEAD | Low | **Mitigated** | WT `.gitignore` `*.env`/`scripts/*.env` · `git check-ignore scripts/dev-backend.env` 통과 · **`git show HEAD:.gitignore` 미반영**(parent `M .gitignore` 미커밋) |
| SEC-D18 | origin/test push 미실행 | Low | **Monitor** | BE test SYNCED · FE test +3 behind · origin/test **433 BE/71 FE unpushed** |
| SEC-D25·D28·D30·D31·D27·A06-1 | 첨부 magic-byte·easy-pay·health·Kakao·NHIS xls·Boot 3.3.1 | Low~Medium | Monitor/Open | 18차와 동일 |

### (D) ✅ 유지 — 18차 Fixed/Pass 재확인

| 항목 | 19차 재확인 |
|------|-------------|
| SEC-D17 raw fetch | **Fixed 유지** — 앱 코드 raw `fetch()`는 `src/api/http.js` + e2e harness 전용 |
| SEC-D19 error handler | **Fixed 유지** — `GlobalExceptionHandler` 고정 메시지 |
| SEC-D23 PilotFixturePanel | **Fixed 유지** — `import.meta.env.DEV \|\| VITE_ENABLE_PILOT_FIXTURE` |
| SEC-D24 SecurityConfig 필터 | **Fixed 유지** — tenant filter after BearerToken |
| SEC-D14 origin/test P0 | **Fixed 유지** — backend `598d108`·frontend `ab4de83` P0 포함 |
| SEC-008 npm audit prod | **Fixed 유지** — prod **0건**(19차 실측) |

### (E) 우선순위 (19차)

| 순위 | ID | Severity | 조치 |
|------|-----|----------|------|
| P1 | SEC-D4 | Medium | poi-ooxml 5.4.0+ — **NHIS·은행입금·RFID(G21)** 3 파서 회귀 |
| P1 | A06-1 | Medium | Spring Boot 3.3.x 패치 라인 |
| P2 | SEC-D26 | High(dev·1건) | form-data `npm audit fix` |
| P2 | SEC-D22 | Low | parent repo `.gitignore` `*.env` **커밋** |
| P2 | SEC-D25 | Low~Medium | 첨부 magic-byte 검증 |
| P2 | SEC-D18 | Low | **origin/test push**(433 BE/71 FE) |
| P2 | SEC-D32 | Low | `cash_receipt_issuances.identifier_value` at-rest 암호화 검토(SEC-D21 패턴) |
| P2 | SEC-D28·D30·D31·D5 | Low | prod easy-pay·health 마스킹·Kakao 도메인·application-prod.yml |
| ✅ | G32·G-CASH-RECEIPT·live-e2e trim·G21 split NHIS·SEC-D17·D19·D23·D24·D14 | — | 19차 Pass/Fixed/Mitigated |

---

## 1.20 일일 재점검 델타 (2026-06-18 18차) [SEC]

> 이번 호출에서 **workspace 실측**(`git -C src/backend rev-parse HEAD/origin/test/test` · `git -C src/frontend …` · `git log 73cffc5..28860ae` / `git log ea5d896..50d330d` · `git status` · `npm audit`/`npm audit --omit=dev` · `pom.xml` · `LiveE2eBootstrapService.java`·`LiveE2eBootstrapResponse.java`·`SecurityConfig.java`·`VisitController.java`·`RfidTransmissionExcelParser.java`·`V152~V155`)을 17차 `73cffc5`/`ea5d896` 기준선과 대조. backend develop **+32 커밋** · frontend develop **+36 커밋** 전진. **양 스트림 WT CLEAN**. TSR 1016~1017차 기준 **로컬 test merge 다수 완료**(BE test `6aeafe7`·FE test `50d330d`)이나 **origin/test push 미실행**.

### (A) 상태 변화 — develop 추가 전진 · WT CLEAN · 로컬 test SYNCED · origin/test stale

| 스트림 | 17차 develop | 18차 develop HEAD | local test / origin/test | WT |
|--------|--------------|-------------------|--------------------------|----|
| backend | `73cffc5` | **`28860ae`**(+399 vs origin/test: G21 RFID diff·G15 driver signature·live-e2e QA-B95·V152~V155·G21 check-in guard·plan-billing readiness) | local **`6aeafe7`**(+1 behind develop) / origin **`598d108`**(불변·**399 unpushed**) | **CLEAN** |
| frontend | `ea5d896` | **`50d330d`**(+33 vs origin/test: G15 service-log UI·G21 RFID UI·G41 PDF 8-7·billing print bundle·live-e2e harness) | local **`50d330d`**(SYNCED) / origin **`ab4de83`**(불변·**33 unpushed**) | **CLEAN** |

→ **판정**: `origin/test` 양 스트림 P0 통제 유지(SEC-D14 Fixed) — **원격 배포 산출물 보안 회귀 없음**. develop↔origin/test 격차 **399+33**(신규 기능·보안 통제 누락 아님) → **BLOCK 아님**(SEC-D18). **로컬 test는 TSR merge로 대부분 동기화**됐으나 origin push 미실행으로 **검증 코드 ≠ 원격 CI 산출물** 갭 잔존(운영 게이트·Low). QA Open BLOCK **0건**(기능 이슈만·보안 BLOCK 없음).

### (B) ✅ 신규 기능 보안 검토 — 전부 RBAC·tenant-safe Pass

| 기능 (커밋) | 판정 | 근거 |
|-------------|------|------|
| **G21 RFID plan-vs-tag diff compare** `VisitController` `/imports/rfid/compare` (`eeac205`·`RfidTransmissionExcelParser`) | **Pass** · **SEC-D4 표면 +1** | `@PreAuthorize(BRANCH_ADMIN\|SOCIAL_WORKER)` · `requireOrganizationId`·`validateBranchWriteScope`·`requireHomeVisitBranch` · plan+rfid xlsx `validateImportFile` · **POI `WorkbookFactory`**(untrusted xlsx — CVE-2025-31672 동일 클래스·3번째 파서) · 응답은 diff code·일정 메타(집계) |
| **G15 driver signature** V154 + service-log legal/export deepen (`bc3a35c`·`72124f7`·`TransportController`) | **Pass** | 기존 service-log RBAC(4역할) 유지 · V154 pair-CHECK(`btrim` non-empty) · 서명자 **성명+일자 텍스트**(생체 이미지 아님) · export에 branch contact·pickupAddress·direction — tenant scope read |
| **V152~V155 transport 무결성** (`V152`~`V155`) | **Pass — 보안 긍정** | V152 `is_active` 트리거 회귀 수정 · V155 waypoint `btrim(address)<>''` · V154 driver signature pair-CHECK — 비활성 client·공백 경유지·불완전 서명 DB-level 차단 |
| **G21 visit check-in guard** `VisitService` (`0db1e68`·`78cfb8a`) | **Pass — 강화** | assigned caregiver **active·branch 일치** 서버 검증 · supervisory role code 정규화 — 무단 체크인·퇴사 직원 IDOR 방어 |
| **live-e2e QA-B95 seed 보강** (다수 `fix(v2/live-e2e)`) | **Mitigated(SEC-D29)** | `@ConditionalOnProperty` 기본 off · `ProductionSecretValidator` prod 거부 · `bootstrap()` blank credential fail-fast 유지 · 응답 record **password 필드 0** · probe가 default guardian cred **허용**(QA-B95 dev/E2E 설계·non-prod only) |
| **G41 PDF 8-7 alerts/export** · **billing statement print bundle** (FE `caa215f`·`50d330d`) | **Pass** | 기존 staff-training·billing RBAC·`apiFetch` 경유 · 신귀 공개 endpoint 없음 |

### (C) 신규·갱신 이슈

| ID | 항목 | Severity | 상태 | 근거 |
|----|------|----------|------|------|
| **SEC-D4** | poi-ooxml **5.3.0** — **3 파서 표면** | **Medium** | **Open(표면 확대)** | 17차 2표면(NHIS·은행입금) → **18차 3표면**: `NhisExcelParser`·`BankDepositExcelParser`·**`RfidTransmissionExcelParser`**(G21 compare·`WorkbookFactory`). `pom.xml:64` 5.3.0 — CVE-2025-31672 미해소 |
| SEC-D29 | live-e2e 무인증 bootstrap | Low~Medium | **Mitigated** | 변동 소폭 — QA-B95 lineage가 probe/readiness에서 **default guardian cred 허용**(`guardianCredentialsUsable \|\| defaultGuardianCredentials`) · bootstrap 응답 password 0 · prod validator 유지 · misconfiguration 시에만 위험 |
| SEC-D26 | npm audit dev form-data CRLF | High(dev-only) | **Open(dev)** | prod `--omit=dev` **0건** · dev **1 HIGH** GHSA-hmw2-7cc7-3qxx — 17차와 동일 |
| SEC-D22 | `scripts/*.env` gitignore parent HEAD | Low | **Mitigated** | WT `.gitignore`에 `*.env`/`scripts/*.env` 추가·`git check-ignore scripts/dev-backend.env` 통과 · **`git show HEAD:.gitignore` 미반영**(parent `M .gitignore` 미커밋) |
| SEC-D18 | origin/test push 미실행 | Low | **Monitor(로컬 merge 진전)** | 로컬 test BE `6aeafe7`/FE `50d330d` SYNCED(TSR 1016~1017) · origin/test **399 BE/33 FE unpushed** |
| SEC-D25 | 첨부 magic-byte 미검증 | Low~Medium | Open | 변동 없음 — G21 xlsx는 POI 파싱만(첨부 저장 아님) |
| SEC-D28·D30·D31·D27·A06-1 | easy-pay stub·health 노출·Kakao appkey·NHIS xls MIME·Boot 3.3.1 | Low~Medium | Monitor/Open | 17차와 동일 |

### (D) ✅ 유지 — 17차 Fixed/Pass 재확인

| 항목 | 18차 재확인 |
|------|-------------|
| SEC-D17 raw fetch | **Fixed 유지** — 앱 코드 raw `fetch()`는 `src/api/http.js` + e2e 테스트 전용 |
| SEC-D19 error handler | **Fixed 유지** — `GlobalExceptionHandler` 고정 메시지·raw cause 미echo |
| SEC-D23 PilotFixturePanel | **Fixed 유지** — `import.meta.env.DEV \|\| VITE_ENABLE_PILOT_FIXTURE` |
| SEC-D24 SecurityConfig 필터 | **Fixed 유지** — tenant filter after BearerToken |
| SEC-D14 origin/test P0 | **Fixed 유지** — backend `598d108`·frontend `ab4de83` P0 포함 |
| SEC-008 npm audit prod | **Fixed 유지** — prod **0건**(18차 실측) |

### (E) 우선순위 (18차)

| 순위 | ID | Severity | 조치 |
|------|-----|----------|------|
| P1 | SEC-D4 | Medium↑ | poi-ooxml 5.4.0+ — **NHIS·은행입금·RFID(G21)** 3 파서 회귀 |
| P1 | A06-1 | Medium | Spring Boot 3.3.x 패치 라인 |
| P2 | SEC-D26 | High(dev·1건) | form-data `npm audit fix` |
| P2 | SEC-D22 | Low | parent repo `.gitignore` `*.env` **커밋** |
| P2 | SEC-D25 | Low~Medium | 첨부 magic-byte 검증 |
| P2 | SEC-D18 | Low | **origin/test push**(399 BE/33 FE) |
| P2 | SEC-D28·D30·D31·D5 | Low | prod easy-pay·health 마스킹·Kakao 도메인·application-prod.yml |
| ✅ | G21 RFID·G15 signature·V152~V155·check-in guard·live-e2e·SEC-D17·D19·D23·D24·D14 | — | 18차 Pass/Fixed/Mitigated |

---

## 1.19 일일 재점검 델타 (2026-06-17 17차) [SEC]

> 이번 호출에서 **workspace 실측**(`git -C src/backend rev-parse HEAD/origin/test` · `git -C src/frontend …` · `git log 7ac0a46..73cffc5` / `git log b000d92..ea5d896` · `git status` WT · `npm audit`/`npm audit --omit=dev` · `pom.xml` · `LiveE2eBootstrapResponse.java`·`LiveE2eGuardianBootstrapResponse.java`·`LiveE2eBootstrapService.java`·`SecurityConfig.java`·`HealthController.java`·`KakaoDirectionsClient.java`·`TransportController.java`·`V152` 신규 마이그레이션)을 16차 `7ac0a46`/`b000d92` 기준선과 대조. backend develop **+35 커밋** 전진(v1.3-C G15 이동서비스일지·v2 transport waypoints/geocode·transport 월간 리포트·live-e2e bootstrap 보강), frontend develop **+44 커밋** 전진(transport 지도/ETA·DS date-picker·live-e2e harness). origin/test 양 스트림 불변(P0 포함)이나 **로컬 test 머지 다수·origin push 미실행**(366 BE/52 FE unpushed).

### (A) 상태 변화 — develop 추가 전진 · WT DIRTY · origin/test 불변 · 보안 회귀 없음

| 스트림 | 16차 develop | 17차 develop HEAD | local test / origin/test | WT |
|--------|--------------|-------------------|--------------------------|----|
| backend | `7ac0a46` | **`73cffc5`**(+367 vs origin/test: v1.3-C G15 service-log·v2 transport waypoints/geocode/route-leg·월간 리포트·live-e2e bootstrap 강화) | local `704478f` / origin `598d108`(불변, P0 포함·**366 unpushed**) | **DIRTY 1U**(`V152` Flyway 트리거 회귀 수정) |
| frontend | `b000d92` | **`ea5d896`**(+53 vs origin/test: transport split-view/지도/ETA·DS date-picker·client phone 컬럼·live-e2e harness) | local `bf73c4c` / origin `7106106`(불변, P0 포함·**52 unpushed**) | **DIRTY ~9M**(QA-B127 transport map/date-picker 단위 회귀 WIP) |

→ **판정**: `origin/test` 양 스트림 16차와 동일(P0 통제 전부 포함) — **배포 산출물 보안 회귀 없음**(SEC-D14 Fixed 유지). develop↔origin/test 격차 **367+53 ahead**(전부 v2/v1.2.1/v1.3 신규 기능·보안 통제 누락 아님) → **BLOCK 아님**(SEC-D18, Low). 단 **로컬 test 머지는 진행됐으나 origin/test push 미실행**(검증 코드 ≠ 원격 배포 산출물 갭은 TSR/OPS merge-push 게이트, 보안 BLOCK 아님). QA Open BLOCK은 **QA-B127(FE develop 단위 회귀)·QA-B128(BE)** — **기능 이슈·보안 이슈 아님**.

### (B) ✅ 신규 v1.3-C/v2 기능 보안 검토 — 전부 RBAC·tenant-safe Pass

| 기능 (커밋) | 판정 | 근거 |
|-------------|------|------|
| **v1.3-C G15 이동서비스일지(별지 제22호)** `TransportController` service-log export/upsert/audit-trail (`0cfa970`·`aaaeb10`·`5994d15`) | **Pass** | 3 메서드 `@PreAuthorize(HQ/BRANCH/SOCIAL_WORKER/CAREGIVER)` · tenant·branch scope · 감사 추적(audit-trail) read-only · 텍스트/일자 필드(파일 업로드 아님) |
| **v2 transport 임의 경유지·출발시각·route-leg 영속화** `TransportController`/`TransportService` (`de3474d`·`0e46b37`·`1d1a71f`·`114411f`·`f5b2b42`) | **Pass** | create/update/suggest/delete `@PreAuthorize(HQ_ADMIN)` · read 4역할 · 경유지 좌표 숫자형·`KakaoDirectionsClient` **고정 호스트**(`apis-navi.kakaomobility.com`)·scheme/path 상수·REST key env-only → **SSRF 없음** · waypoint name은 JSON 본문(URL 미주입) |
| **v2 transport 월간 리포트** service-variation·resident-status (`5d27ad3`) | **Pass** | read RBAC · tenant scope · 집계 데이터 |
| **v1.3-A roster guardian mapping / Kakao geocode depot** (`35e03ef`·`c1f1428`) | **Pass** | branch depot 지오코딩도 고정 호스트 Kakao API·env key · roster contact는 기존 transport 마스킹 정책 |
| **live-e2e staff/guardian bootstrap 보강** (`73cffc5`·다수 `fix(v2/live-e2e)`) | **Mitigated(SEC-D29)** | `@ConditionalOnProperty` 기본 off 유지 · credential 미설정 fail-fast **커밋됨**(`89d6400`) · 응답 record 2종 모두 password 필드 없음 · guardian token 노출은 harness 설계(인증 우회 아님) |
| **V152 transport_run_stops 트리거 회귀 수정** (`V152` WT) | **Pass — 보안 긍정** | V143/V151 트리거가 잘못된 컬럼명(`active`) 참조 → `is_active` 정정 + `uses_transport`/`discharged_at`/branch 일치 가드 복원 = 비활성·퇴소·크로스브랜치 client INSERT DB-level 차단 회복 |

### (C) 신규·갱신 이슈

| ID | 항목 | Severity | 상태 | 근거 |
|----|------|----------|------|------|
| **SEC-D29** | **live-e2e 무인증 bootstrap — prod 노출** | **Low~Medium** | **Mitigated(거의 Fixed)** | **진전**: `89d6400` — `bootstrap()`·`bootstrapGuardian()`이 `hasConfiguredCredentials()`/`hasConfiguredGuardianCredentials()` false 시 `LIVE_E2E_BOOTSTRAP_CREDENTIALS_MISSING` **fail-fast 커밋됨**(staff/guardian 양 경로 테스트 포함) · `LiveE2eBootstrapResponse`·`LiveE2eGuardianBootstrapResponse` **둘 다 password 필드 없음**(실측) · `ProductionSecretValidator` prod 거부 유지 · `usesDefaultCredentials()`/`usesDefaultGuardianCredentials()` 기본값 탐지 보유. **잔존**: `SecurityConfig` `/api/v1/system/live-e2e/*` `permitAll`(ConditionalOnProperty 비활성이 1차 방어) — prod misconfiguration 시에만 위험 |
| **SEC-D26** | npm audit dev — form-data CRLF만 잔존 | **High(dev-only)** | **Open(dev·축소)** | 16차 dev **4 HIGH** → **17차 dev 1 HIGH**: esbuild GHSA-gv7w-rqvm-qjhr·vite·@vitejs/plugin-react **해소**(FE 의존성 갱신). form-data 4.0.0–4.0.5 GHSA-hmw2-7cc7-3qxx(CRLF injection via unescaped multipart field names)만 잔존 · `npm audit fix` 가능. prod `--omit=dev` **0건** — SEC-008 Fixed 유지 |
| **SEC-D30** | 공개 health 엔드포인트 정보 노출(확대) | Low | **Monitor** | `HealthController`가 `activeProfiles`·`databaseStatusDetail`에 더해 **operation readiness 필드 다수**(`liveE2eOperationReady`·`liveE2eOperationBlocker`·`liveE2eCredentialsConfigured`·`liveE2eDefaultCredentials` 등) 노출 + 신규 actuator 별칭(`/actuator/livez`·`/readyz`·`/actuator/health/*`) permitAll. 운영 probe 기능 목적이나 prod에서는 프로필·readiness 상세 마스킹 권고 |
| SEC-D31 | Kakao Maps JS SDK appkey 빌드 노출 | Low | **Monitor** | 변동 없음 — FE transport 지도 작업 지속(`KakaoTransportMap*`). appkey는 `VITE_KAKAO_MAPS_JS_API_KEY` env→번들(디자인상 공개). 운영 도메인 제한 Kakao Dev Console 게이트 미확인 |
| SEC-D28 | 간편결제 stub provider prod 기본값 | Low | Monitor | 변동 없음 — `EasyPayConfig` `matchIfMissing=true` |
| SEC-D25 | 첨부 업로드 magic-byte 미검증 | Low~Medium | **Open** | 변동 없음 — 신규 첨부 표면 없음(G15 service-log는 텍스트/일자) |
| SEC-D27 | NHIS legacy xls MIME 완화 | Low | **Monitor** | 변동 없음 |
| SEC-D22 | `scripts/*.env` gitignore parent HEAD 미반영 | Low | **Mitigated** | 변동 없음 — WT `.gitignore` `*.env` 무시·HEAD 미커밋 |
| SEC-D4 | poi-ooxml **5.3.0** | Medium | Open | `pom.xml:64` 5.3.0 — CVE-2025-31672 미해소 |
| A06-1 | Spring Boot **3.3.1** | Medium | Open | `pom.xml:9` — 3.3.x 패치 라인 |
| SEC-D18 | develop→test merge·origin/test push 미실행 | Low | Monitor | develop **367+53 ahead** · origin/test 366 BE/52 FE unpushed · TSR/OPS merge-push gate |

### (D) ✅ 유지 — 16차 Fixed/Pass 재확인

| 항목 | 17차 재확인 |
|------|-------------|
| SEC-D17 raw fetch | **Fixed 유지** — raw `fetch()`는 `src/api/http.js`(apiFetch 래퍼)뿐 |
| SEC-D19 error handler | **Fixed 유지** — `GlobalExceptionHandler` 변동 없음 |
| SEC-D23 PilotFixturePanel | **Fixed 유지** — `import.meta.env.DEV \|\| VITE_ENABLE_PILOT_FIXTURE` 게이트 |
| SEC-D24 SecurityConfig 필터 | **Fixed 유지** — `addFilterAfter(tenantContextFilter, BearerTokenAuthenticationFilter.class)` |
| SEC-D14 origin/test P0 | **Fixed 유지** — backend `598d108`·frontend `7106106` P0 포함(ProtectedRoute·memory JWT·AuthRateLimitService·ProductionSecretValidator) |
| SEC-008 npm audit prod | **Fixed 유지** — prod **0건**(17차 실측) |

### (E) 우선순위 (17차)

| 순위 | ID | Severity | 조치 |
|------|-----|----------|------|
| P1 | SEC-D4 | Medium | poi-ooxml 5.4.0+ |
| P1 | A06-1 | Medium | Spring Boot 3.3.x 최신 패치 라인 업그레이드 |
| P2 | SEC-D26 | High(dev·1건) | form-data `npm audit fix`(GHSA-hmw2-7cc7-3qxx) 또는 CI 격리 |
| P2 | SEC-D22 | Low | parent repo `.gitignore` `*.env` **커밋** |
| P2 | SEC-D25 | Low~Medium | 첨부 magic-byte 검증 |
| P2 | SEC-D18 | Low | develop→test merge(367+53)·**origin/test push** |
| P2 | SEC-D28 | Low | prod easy-pay 실 PG 필수·startup 검증 |
| P2 | SEC-D30 | Low | prod health `activeProfiles`·readiness 상세 마스킹 |
| P2 | SEC-D31 | Low | Kakao Maps JS appkey 운영 도메인 제한 게이트 확인 |
| ✅ | SEC-D29(credential fail-fast 커밋·password 필드 0)·V152 트리거 회귀 수정·G15 service-log·transport waypoints·SEC-D17·D19·D23·D24·D14 | — | 17차 Pass/Fixed/Mitigated 확인 |

---

## 1.18 일일 재점검 델타 (2026-06-16 16차) [SEC]

> 이번 호출에서 **workspace 실측**(`git -C src/backend rev-parse HEAD/origin/test` · `git -C src/frontend …` · `git log 344a28b..7ac0a46` / `git log 1fd1434..b000d92` · `git diff HEAD` WT 검토 · `npm audit` · `pom.xml` · `LiveE2eBootstrapResponse.java` · `ProductionSecretValidator.java` · `SecurityConfig.java`)을 15차 `344a28b`/`1fd1434` 기준선과 대조. backend develop **+37 커밋** 전진(G26 통계·L02 care보고서·live-e2e guardian bootstrap 등). frontend develop **+9 커밋** 전진(Kakao map refactor·live-e2e harness). frontend **origin/test `7106106`로 업데이트**(BNK-276 FE batch merge live). 양 스트림 **WT DIRTY**(WIP).

### (A) 상태 변화 — develop 추가 전진 · WT DIRTY · origin/test 부분 갱신 · 보안 회귀 없음

| 스트림 | 15차 develop | 16차 develop HEAD | local/origin test | WT |
|--------|--------------|-------------------|-------------------|----|
| backend | `344a28b` | **`7ac0a46`**(+331 vs test: G26 통계 3종·L02 care보고서·G-MEAL-PREFERENCE·G21 배지·live-e2e guardian bootstrap 보강) | `598d108`(불변, P0 포함) | **DIRTY 2M**(`LiveE2eBootstrapService.java`+Test — SEC-D29 credential guard WIP) |
| frontend | `1fd1434` | **`b000d92`**(+9 vs test `7106106`: Kakao map instance refactor·live-e2e harness 보강) | **`7106106`**(BNK-276 FE batch merge live, P0 포함) | **DIRTY 5M+2U**(Kakao map instance refactor — QA-B113 Fixed·QA-B114 WIP) |

→ **판정**: `origin/test` backend `598d108` 불변·frontend `7106106`로 업데이트됨. 양 스트림 모두 **P0 통제 포함**(ProtectedRoute·memory JWT·AuthRateLimitService·ProductionSecretValidator 확인) — **SEC-D14 Fixed 유지**. develop↔test 격차 **331+9 ahead**(전부 v2/v1.2.1/v1.3 신규 기능·보안 통제 누락 아님) → **BLOCK 아님**(SEC-D18, Low).

### (B) ✅ 신규 v2/v1.2.1/v1.3 기능 보안 검토 — 전부 RBAC·tenant-safe Pass

| 기능 (커밋) | 판정 | 근거 |
|-------------|------|------|
| **G26 copay monthly statistics** `BillingController`/`BillingService` (`6d10e0d`) | **Pass** | `@PreAuthorize(HQ/BRANCH/SOCIAL_WORKER)` · tenant+branch scope · 집계 데이터(PII 미포함·금액 합산만) |
| **G26 medical expense deduction statistics** `BillingController`/`Service` (`903f462`) | **Pass** | `@PreAuthorize(HQ/BRANCH/SOCIAL_WORKER)` · tenant+branch scope · **CMS·간편결제 본인부담 공제 제외**(이중공제 방지) |
| **G26 transport service fee statistics** `TransportServiceFeeStatisticsController`/`Service` (`3672bbe`) | **Pass** | `@PreAuthorize(HQ/BRANCH/SOCIAL_WORKER)` · tenant scope · 집계 데이터 |
| **G-MEAL-PREFERENCE survey** `MealPreferenceSurveyController`/`Service` (`f33252a`) | **Pass** | `@PreAuthorize(HQ/BRANCH/SOCIAL_WORKER)` · V142 트리거(org/branch 파생·active-client 가드·actor backstop) |
| **L02 care report proxy APIs** (patient-service·service-summary·meal-preference 등 8종) `CareReportController` (`002e3eb`) | **Pass** | 전 메서드 `@PreAuthorize(HQ/BRANCH/SOCIAL_WORKER)` · tenant scope · 읽기 전용 집계·PII 미포함 |
| **G21 billing claim reflection badges** `VisitController`/`Service` (`6da49aa`) | **Pass** | 기존 방문 RBAC 유지 · read-only 집계(NHIS 대사 상태만) |
| **live-e2e guardian bootstrap** `LiveE2eController.bootstrapGuardian()` (`f5205e3`) | **Mitigated(SEC-D29)** | `@ConditionalOnProperty` 기본 off · `permitAll` 유지 · **`LiveE2eBootstrapResponse` password 필드 완전 제거됨**(커밋) · `ProductionSecretValidator` prod 거부 커밋됨 · WIP: credential 미설정 fail-fast WT dirty |
| **live-e2e role-collision guard** (`7ac0a46`) | **Pass(보안 강화)** | 역할 불일치 seed 계정 재사용 방지 — bootstrap org 내 타 사용자 충돌 방어 |
| **J03 quiet-hours billing dispatch reject** (`39f5f4e`) | **Pass** | 야간(22:00~08:00 KST) 수동 청구 발송 서버측 거부 강화 |

### (C) 신규·갱신 이슈

| ID | 항목 | Severity | 상태 | 근거 |
|----|------|----------|------|------|
| **SEC-D29** | **live-e2e 무인증 bootstrap — prod 노출** | **Medium** | **Mitigated(부분)** | **진전**: `aa6816a` — `ProductionSecretValidator` prod에서 `LIVE_E2E_BOOTSTRAP_ENABLED`/`LIVE_E2E` **startup 거부 커밋됨** · `LiveE2eBootstrapResponse`에서 **password 필드 완전 제거 커밋됨** · **WIP**: `bootstrap()`/`bootstrapGuardian()`에 `hasConfiguredCredentials()` fail-fast 추가(WT dirty·미커밋). **잔존**: `SecurityConfig` `/api/v1/system/live-e2e/*` `permitAll` 유지(ConditionalOnProperty 비활성이 1차 방어) · `LiveE2eGuardianBootstrapResponse` password 필드 확인 필요 |
| **SEC-D26** | npm audit dev **4건 HIGH** — form-data CRLF 신규 | **High(dev-only)** | **Open(dev)** | 15차 dev 3 HIGH → **16차 dev 4 HIGH**: form-data GHSA-hmw2-7cc7-3qxx(CRLF injection via unescaped multipart field names) 신규 추가. esbuild GHSA-gv7w-rqvm-qjhr · vite · @vitejs/plugin-react 유지. prod `--omit=dev` **0건** — SEC-008 Fixed 유지 |
| SEC-D31 | Kakao Maps JS SDK appkey 빌드 노출 | Low | **Monitor** | FE WT dirty — `KakaoBareMap.jsx`·`kakaoMapInstance.js`·`useKakaoMap.js` 신규·`KakaoTransportMap.jsx` refactor. appkey는 `VITE_KAKAO_MAPS_JS_API_KEY` env → 빌드 번들 포함(디자인상 공개). 운영 도메인 제한 Kakao Dev Console 게이트 미확인 |
| SEC-D28 | 간편결제 stub provider prod 기본값 | Low | Monitor | 변동 없음 — `EasyPayConfig` `matchIfMissing=true` |
| SEC-D25 | 첨부 업로드 magic-byte 미검증 | Low~Medium | **Open** | 변동 없음 |
| SEC-D27 | NHIS legacy xls MIME 완화 | Low | **Monitor** | 변동 없음 |
| SEC-D22 | `scripts/*.env` gitignore parent HEAD 미반영 | Low | **Mitigated** | 변동 없음 — WT `.gitignore` `*.env` 무시·HEAD 미커밋 |
| SEC-D4 | poi-ooxml **5.3.0** | Medium | Open | `pom.xml` 5.3.0 — CVE-2025-31672 미해소 |
| A06-1 | Spring Boot **3.3.1** | Medium | Open | `pom.xml` — 3.3.x 패치 라인 |
| SEC-D18 | develop→test merge 미실행 | Low | Monitor | develop **331+9 ahead** · TSR merge gate |

### (D) ✅ 유지 — 15차 Fixed/Pass 재확인

| 항목 | 16차 재확인 |
|------|-------------|
| SEC-D17 raw fetch | **Fixed 유지** — raw `fetch()`는 `src/api/http.js`(apiFetch 래퍼)뿐 |
| SEC-D19 error handler | **Fixed 유지** — `GlobalExceptionHandler` 변동 없음 |
| SEC-D23 PilotFixturePanel | **Fixed 유지** — `import.meta.env.DEV \|\| VITE_ENABLE_PILOT_FIXTURE` 게이트 |
| SEC-D24 SecurityConfig 필터 | **Fixed 유지** — `addFilterAfter(tenantContextFilter, BearerTokenAuthenticationFilter.class)` |
| SEC-D14 origin/test P0 | **Fixed 유지** — backend `598d108` 불변·frontend `7106106` P0 포함 확인(ProtectedRoute·memory JWT·AuthRateLimitService) |
| SEC-008 npm audit prod | **Fixed 유지** — prod **0건**(16차 실측) |

### (E) 우선순위 (16차)

| 순위 | ID | Severity | 조치 |
|------|-----|----------|------|
| P1 | SEC-D4 | Medium | poi-ooxml 5.4.0+ |
| P1 | A06-1 | Medium | Spring Boot 3.3.x 최신 패치 라인 업그레이드 |
| P1 | SEC-D29 | Medium | backend WT clean — `bootstrap()` credential fail-fast 커밋 · `LiveE2eGuardianBootstrapResponse` password 필드 미포함 확인 |
| P2 | SEC-D22 | Low | parent repo `.gitignore` `*.env` **커밋** |
| P2 | SEC-D25 | Low~Medium | 첨부 magic-byte 검증 |
| P2 | SEC-D26 | High(dev) | esbuild/vite/form-data dev 체인 패치 또는 CI 격리 |
| P2 | SEC-D18 | Low | develop→test merge(331+9) |
| P2 | SEC-D28 | Low | prod easy-pay 실 PG 필수·startup 검증 |
| P2 | SEC-D30 | Low | prod health `activeProfiles` 마스킹 |
| P2 | SEC-D31 | Low | Kakao Maps JS appkey 운영 도메인 제한 게이트 확인 |
| ✅ | G26 통계·G-MEAL-PREFERENCE·L02 care reports·G21 배지·live-e2e guardian bootstrap·SEC-D17·D19·D23·D24·D14 | — | 16차 Pass/Fixed 확인 |

---

## 1.17 일일 재점검 델타 (2026-06-15 15차) [SEC]

> 이번 호출에서 **workspace 실측**(`git -C src/backend rev-parse HEAD/origin/test` · `git -C src/frontend …` · `git log 63cb193..HEAD`/`962858b..HEAD` · `npm audit` · `pom.xml` · `git check-ignore` · `git diff HEAD -- .gitignore`)을 14차 `63cb193`/`962858b` 기준선과 대조. develop 양 스트림이 v2/v1.2.1/v1.3 다수 기능과 함께 **추가 전진**(BE +50 / FE +60 vs 14차, 각각 origin/test 대비 **292 / 355 ahead**). 양 스트림 **WT CLEAN**. 신규 보안 표면을 소스 직접 정적 분석.

### (A) 상태 변화 — develop 추가 전진 · WT CLEAN · origin/test 불변 · 보안 회귀 없음

| 스트림 | 14차 develop | 15차 develop HEAD | local/origin test | WT |
|--------|--------------|-------------------|-------------------|-----|
| backend | `63cb193` | **`344a28b`**(+292 vs test: L02 V132~V137·G-7-1-4CHANNEL·G30 만족도·G19·L03 V118~V125·G24b·G-ONBOARD V127·v1.3-B transport·live-e2e bootstrap/health) | `598d108`(불변, P0 포함) | **CLEAN** |
| frontend | `962858b` | **`1fd1434`**(+355 vs test: 위 기능 UI·live-e2e harness·G19 URL guard·L03/L02 a11y·~70 route) | `c7c8f07`(불변) | **CLEAN** |

→ **판정**: `origin/test`는 14차와 동일(P0 통제 전부 포함) — **배포 산출물 보안 회귀 없음**(SEC-D14 Fixed 유지). develop↔test 격차가 **292/355로 추가 대형화**했으나 전부 **v2/v1.2.1/v1.3 신규 기능**(보안 통제 누락 아님) → **BLOCK 아님**(SEC-D18, Low). QA Open **0건**(TSR 786차) — **보안 BLOCK 없음**.

### (B) ✅ 신규 v2/v1.2.1/v1.3 기능 보안 검토 — 전부 RBAC·tenant-safe Pass

| 기능 (커밋) | 판정 | 근거 |
|-------------|------|------|
| **G-7-1-4CHANNEL 청구서 4채널** `BillingStatementDispatchService`/`BillingController` (`3a2e82e`) | **Pass — 강함** | batch/list/patch 3메서드 `@PreAuthorize(HQ_ADMIN\|BRANCH_ADMIN)` · CONFIRMED/PAID 청구만 · tenant·branch scope · **문자·이메일 채널은 `NotificationQuietHoursPolicy` 서버측 거부**(J03 lineage) · 우편 발송일만 PATCH 허용 |
| **L02_M01 주간 제공기록** `CareServiceWeeklyRecordController`/`Service` (V134~V135, `13b8a37`) | **Pass** | 3메서드 `@PreAuthorize`(HQ/BRANCH/SOCIAL_WORKER/CAREGIVER) · V135 트리거(org/branch 파생·active-client·recorded_by backstop) |
| **L02_M02 집중배설관찰** `IntensiveExcretionObservationController`/`Service` (V132, `fd42b7e`) | **Pass** | 3메서드 `@PreAuthorize` · V132 트리거 · tenant·branch scope |
| **L02_M03 목욕일정** `BathingScheduleController`/`Service` (V136~V137, `e703252`~`47a4e25`) | **Pass — 강함** | 3메서드 `@PreAuthorize` · V137 트리거 · **미제공(SKIPPED) 시 사유 필수** 서버 검증(`47a4e25`) |
| **L02_M07 신체제재** `BodyRestraintRecordController`/`Service` (V131, `ea6092a`) | **Pass** | 3메서드 `@PreAuthorize` · V132 트리거 · restraint date input guard |
| **G30 전화상담 만족도** `MonitoringService` (V138, `344a28b`) | **Pass** | 기존 phone-consultation 4메서드 `@PreAuthorize(HQ/BRANCH/SOCIAL_WORKER)` 유지 · `satisfied` boolean 서버 저장·**60% 만족도 임계값 서버 계산**(FAQ21841) · PII 필드 추가 없음 |
| **G19 통합재가 발굴** `BranchController`/`BranchService` (`f44ee73`~`8cb8789`) | **Pass** | provider discovery `@PreAuthorize(HQ/BRANCH)` · 필터값 서버 중앙화 · FE malformed URL guard(`95e7e96`) |
| **L03 간호 8종** `Nursing*Controller`/`Service` (V118~V125, `3540b4f`~`75bddee`) | **Pass — 강함** | 각 컨트롤러 `@PreAuthorize` · V119~V125 트리거 · **injectable KST `Clock` 미래일자 거부**(`090b2d7` lineage) · branch scoping 테스트 |
| **G24b 욕구사정 컴플라이언스** `NeedsAssessmentComplianceController` (`98002d4`~`f4c8beb`) | **Pass** | read `@PreAuthorize`(HQ/BRANCH/SOCIAL_WORKER) · fiscal year 서버 검증 |
| **G-ONBOARD-SUPPORT** `BranchOnboardingSupportController` (V127, `735dd53`~`43c4b08`) | **Pass** | HQ/BRANCH · V127 트리거 · `openedOn` 날짜 검증 |
| **v1.3-B transport suggest-run** `TransportController` (`db94a65`) | **Pass** | `@PreAuthorize(HQ/BRANCH)` · Kakao REST key env-only · 주소 PII는 기존 transport 마스킹 정책 |
| **V132~V137 무결성 마이그레이션** | **Pass — 강함** | L02 care 전 테이블 **org/branch 서버측 파생 + active-client 가드 + actor backstop** |

### (C) 신규·갱신 이슈

| ID | 항목 | Severity | 상태 | 근거 |
|----|------|----------|------|------|
| **SEC-D29** | **live-e2e 무인증 bootstrap — hq_admin 시드·토큰·평문 비밀번호 반환** | **Medium** | **Open** | `LIVE_E2E_BOOTSTRAP_ENABLED=true`(또는 `LIVE_E2E=true`) 시 `SecurityConfig`가 `/api/v1/system/live-e2e/bootstrap`·`/status` **permitAll** · `LiveE2eBootstrapService.bootstrap()`이 **인증 없이** org/branch/**hq_admin** 생성·`issueTokensForUser` · 응답에 **access·refresh·email·password(평문)** 포함(`LiveE2eBootstrapResponse`) · 기본 role `hq_admin`·기본 비밀번호 `ogada1234` · **`ProductionSecretValidator`에 prod 금지 검증 없음** · 기본값 `false`이므로 prod misconfiguration 시에만 위험 |
| **SEC-D30** | **공개 health 엔드포인트 정보 노출** | **Low** | **Monitor** | `GET /api/v1/health`·`/ping` permitAll · `activeProfiles`·`databaseStatusDetail`(예외 클래스명 sanitize)·live-e2e 활성 시 `liveE2eStatusDetail` 노출(`HealthController`) · 배포 프로필·DB 장애 유형 추론 가능 — 기능적 필요( live E2E probe )이나 prod에서는 프로필 마스킹 권고 |
| SEC-D28 | 간편결제 stub provider prod 기본값 | Low | Monitor | 14차와 동일 — `EasyPayConfig` `matchIfMissing=true` |
| SEC-D26 | npm audit dev 3건 HIGH — esbuild GHSA-gv7w-rqvm-qjhr | High(dev-only) | **Open(dev)** | 15차 `npm audit --omit=dev` **0건** · dev **3 HIGH** — 14차와 동일 |
| SEC-D25 | 첨부 업로드 magic-byte 미검증 | Low~Medium | **Open** | 신규 첨부 표면 없음 — Content-Type+크기만 검증 패턴 유지 |
| SEC-D27 | NHIS legacy xls MIME 완화 | Low | **Monitor** | 변동 없음 |
| SEC-D22 | `scripts/*.env` gitignore parent HEAD 미반영 | Low | **Mitigated** | WT `.gitignore`에 `*.env`/`scripts/*.env` 추가·`git check-ignore` 통과 · **`git diff HEAD -- .gitignore` 미커밋**(parent repo) |
| SEC-D4 | poi-ooxml **5.3.0** | Medium | Open | `pom.xml:64` — CVE-2025-31672 미해소 |
| A06-1 | Spring Boot **3.3.1** | Medium | Open | `pom.xml:9` |
| SEC-D18 | develop→test merge 미실행 | Low | Monitor | develop **292+355 ahead** · TSR merge gate FULLY UNBLOCKED · merge pending 647 |

### (D) ✅ 유지 — 14차 Fixed/Pass 재확인

| 항목 | 15차 재확인 |
|------|-------------|
| SEC-D17 raw fetch | **Fixed 유지** — 앱 코드 raw `fetch()`는 `src/api/http.js:190·224`(apiFetch 래퍼)뿐 · e2e `liveGlobalSetup.js`·`pilotLiveApi.e2e.test.js`·`liveBackendProbe.js`는 테스트 전용 |
| SEC-D19 error handler | **Fixed 유지** — `GlobalExceptionHandler` 변동 없음 |
| SEC-D23 PilotFixturePanel | **Fixed 유지** — DEV/`VITE_ENABLE_PILOT_FIXTURE` 게이트 |
| SEC-D24 SecurityConfig 필터 | **Fixed 유지** — tenant filter after BearerToken |
| SEC-D14 origin/test P0 | **Fixed 유지** — `598d108`/`c7c8f07` 불변 |
| SEC-008 npm audit prod | **Fixed 유지** — prod **0건** |

### (E) 우선순위 (15차)

| 순위 | ID | Severity | 조치 |
|------|-----|----------|------|
| P1 | SEC-D4 | Medium | poi-ooxml 5.4.0+ |
| P1 | A06-1 | Medium | Spring Boot 3.3.x 패치 라인 |
| P1 | SEC-D29 | Medium | prod profile에서 `LIVE_E2E_BOOTSTRAP_ENABLED` **startup 거부** · bootstrap 응답에서 password 제거 · IP allowlist 또는 dev profile 전용 |
| P2 | SEC-D22 | Low | parent repo `.gitignore` `*.env` **커밋** |
| P2 | SEC-D25 | Low~Medium | 첨부 magic-byte 검증 |
| P2 | SEC-D26 | High(dev) | esbuild/vite dev 체인 패치 |
| P2 | SEC-D18 | Low | develop→test merge(292+355) |
| P2 | SEC-D28 | Low | prod easy-pay 실 PG 필수 |
| P2 | SEC-D30 | Low | prod health에서 `activeProfiles` 마스킹 |
| P2 | SEC-D5 | Low | `application-prod.yml` hardening |
| ✅ | L02·G-7-1-4CHANNEL·G30·L03·G19·V132~V137·SEC-D17·D19·D23·D24·D14 | — | 15차 Pass/Fixed 확인 |

---

## 1.16 일일 재점검 델타 (2026-06-14 14차) [SEC]

> 이번 호출에서 **workspace 실측**(`git -C src/backend rev-parse HEAD/origin/test` · `git -C src/frontend …` · `git diff bcb1d9f..HEAD`/`14124d6..HEAD` · `npm audit` · `pom.xml` · `git check-ignore` · `git show HEAD:.gitignore`)을 13차 `bcb1d9f`/`14124d6` 기준선과 대조. develop 양 스트림이 v2/v1.2.1/v1.3 다수 기능과 함께 **추가 전진**(BE +44 / FE +54 vs 13차, 각각 origin/test 대비 **242 / 295 ahead**). 양 스트림 **WT CLEAN**. 신규 보안 표면을 소스 직접 정적 분석.

### (A) 상태 변화 — develop 추가 전진 · WT CLEAN · origin/test 불변 · 보안 회귀 없음

| 스트림 | 13차 develop | 14차 develop HEAD | local/origin test | WT |
|--------|--------------|-------------------|-------------------|-----|
| backend | `bcb1d9f` | **`63cb193`**(+242 vs test: G2/7-5 간편결제·G41/G41b 교육일지·G-NURSING V114~V117·G17b·G21 batch·J03 quiet-hours·US-R02 CSV·V104~V117) | `598d108`(불변, P0 포함) | **CLEAN** |
| frontend | `14124d6` | **`962858b`**(+295 vs test: 위 기능 UI·간편결제·교육일지·욕창 4-step·nursing vital/weight·~70 route) | `c7c8f07`(불변) | **CLEAN** |

→ **판정**: `origin/test`는 13차와 동일(P0 통제 전부 포함) — **배포 산출물 보안 회귀 없음**(SEC-D14 Fixed 유지). develop↔test 격차가 **242/295로 추가 대형화**했으나 전부 **v2/v1.2.1/v1.3 신규 기능**(보안 통제 누락 아님) → **BLOCK 아님**(SEC-D18, Low). QA Open **0건**(TSR 670차) — **보안 이슈 아님**.

### (B) ✅ 신규 v2/v1.2.1/v1.3 기능 보안 검토 — 전부 RBAC·tenant-safe Pass

| 기능 (커밋) | 판정 | 근거 |
|-------------|------|------|
| **G2/7-5 간편결제** `EasyPayController`/`Service` (V108~V111, `438f5c7`~`b893e97`) | **Pass — 강함** | 2 메서드 `@PreAuthorize(HQ/BRANCH)` · `requireOrganizationId`+`validateBranchWriteScope` · CONFIRMED 청구만 · **guardian↔client 링크 검증**(app+`trg_easy_pay_requests_validate_guardian_link`) · provider `CARD`/`KAKAO_PAY` allowlist·locale 정규화 · prior-month copay guard · 금액·단일 client 가드 · **최소 수집**(pg_order_id·transaction_id만·카드번호 미저장) |
| **G41/G41b 교육일지** `StaffTrainingLogController`/`Service` (V104~V107, `6191b91`~`ee42e5d`) | **Pass** | 4 메서드 `@PreAuthorize(HQ/BRANCH/SOCIAL_WORKER)` · V105~V107 무결성 트리거(org/branch 파생·actor backstop) · V107 annual no-half CHECK |
| **G-NURSING 욕창** `PressureUlcerController`/`Service` (V114·V117, `edda491`~`d638493`) | **Pass — 강함** | 9 메서드 `@PreAuthorize`(read=4역할·write=HQ/BRANCH/SOCIAL_WORKER) · V117 트리거(org/branch 서버측 파생·active-client 가드·recorded_by backstop) · input guard(미래일자·범위) |
| **L03_M11 통합 바이탈** `NursingVitalCheckController`/`Service` (V115·V117, `80c0bd5`) | **Pass** | 3 메서드 `@PreAuthorize` · tenant·branch scope · future measure-date 거부(`1a822d2` lineage) |
| **L03_M14 체중관리** `NursingWeightRecordController`/`Service` (V116·V117, `e95df4c`~`63cb193`) | **Pass** | 3 메서드 `@PreAuthorize` · tenant·branch scope · future measure-date 거부 |
| **G17b 인지활동 미제공 사유** `ProgramService`/`FunctionalRecoveryService` (V112·V113, `6b7e6cb`~`ba7d84f`) | **Pass** | 기존 programs RBAC 유지 · skip-reason enum 강제·absent satisfaction 명시 거부 |
| **G21 방문 일괄확정** `VisitService`/`VisitController` (V53 lineage, `0b807d8`~`c22a5dc`) | **Pass — 강함** | batch confirm NHIS gate · assigned caregiver check-in guard 강화(`c16f4fe`·QA-B73 Fixed) · readiness draft ID 노출은 인가 관리자 한정 |
| **J03 quiet-hours** `NotificationService`/`NotificationQuietHoursPolicy` (`9652bf0`~`a057739`) | **Pass — 강함** | 22:00~08:00 KST staff-initiated billing notify **서버측 거부** · FE UI 동기 차단 · channel-status API는 **boolean 플래그만**(시크릿 미노출) |
| **US-R02 8-12 CSV export** `StaffStatusReportController` (`bc927f7`~`c4dbe43`) | **Pass** | read=HQ/BRANCH/SOCIAL_WORKER · UTF-8 BOM · `outputType` allowlist · 집계 데이터(displayName·compliance status만·RRN 미포함) |
| **G30/G34-QUAL checklist** `MonitoringController`/`TeamLeadQualificationController` (V100~V103 lineage) | **Pass** | 기존 13차 Pass 유지 · checklist compliance read-only 집계 |
| **V104~V117 무결성 마이그레이션** | **Pass — 강함** | easy_pay·staff_training·nursing 전부 **org/branch 서버측 파생 + active-client 가드 + actor backstop** |

### (C) 신규·갱신 이슈

| ID | 항목 | Severity | 상태 | 근거 |
|----|------|----------|------|------|
| **SEC-D28** | **간편결제 stub provider prod 기본값** | **Low** | **Monitor** | `EasyPayConfig` `@ConditionalOnProperty(..., havingValue="stub", matchIfMissing=true)` — prod에서 `ogada.easy-pay.provider` 미설정 시 **StubEasyPayProvider** 자동 활성(실 PG 미연동·자동 결제 성공 시뮬레이션). 금융 사고는 아니나 **운영 misconfiguration** 시 청구 PAID 전이 가능. SEC-D20(FCMS stub)과 동일 클래스. 권고: prod profile에서 실 provider 필수 + `ProductionSecretValidator` 연동 |
| SEC-D26 | npm audit dev 3건 HIGH — esbuild GHSA-gv7w-rqvm-qjhr | High(dev-only) | **Open(dev)** | 14차 `npm audit` dev **3 HIGH** · `npm audit --omit=dev` **0건** — 13차와 동일 |
| SEC-D25 | 첨부 업로드 magic-byte 미검증 | Low~Medium | **Open** | 신규 첨부 표면 없음 — 기존 HR·보수교육·급여계약서·등급이력·사진·NHIS·은행입금과 동일 갭 유지 |
| SEC-D27 | NHIS legacy xls MIME 완화 | Low | **Monitor** | 13차와 동일 — 변동 없음 |
| SEC-D22 | `scripts/dev-backend.env` 시크릿 비-gitignore(HEAD) | Low | **Mitigated** | WT `.gitignore`에 `*.env`/`scripts/*.env` 추가 → `git check-ignore scripts/dev-backend.env` **통과**. 단 `git show HEAD:.gitignore`에 `*.env`·`scripts/*.env` **미반영**(`M .gitignore` parent repo 미커밋) |
| SEC-D4 | poi-ooxml **5.3.0** — 2개 파싱 표면 | Medium | Open | `pom.xml:64` 5.3.0. NHIS + 은행입금. CVE-2025-31672 미해소 |
| A06-1 | Spring Boot **3.3.1** | Medium | Open | `pom.xml:9` — 3.3.x 패치 라인 업그레이드 검토 |
| SEC-D18 | v2/v1.2.1/v1.3 develop→test merge 미실행 | Low | Monitor | develop **242+295 ahead** · `origin/test` P0 포함 · TSR merge gate FULLY UNBLOCKED·merge pending 537 |

### (D) ✅ 유지 — 13차 Fixed/Pass 재확인

| 항목 | 14차 재확인 |
|------|-------------|
| SEC-D17 raw fetch | **Fixed 유지** — `rg "[^a-zA-Z.]fetch\("` 실측: 앱 코드 raw `fetch()`는 `src/api/http.js:190·224`(apiFetch/refresh 래퍼)뿐 · e2e `pilotLiveApi.e2e.test.js` 1곳 |
| SEC-D19 error handler | **Fixed 유지** — `GlobalExceptionHandler` 변동 없음(13차 이후 diff 없음) |
| SEC-D23 PilotFixturePanel | **Fixed 유지** — `import.meta.env.DEV \|\| VITE_ENABLE_PILOT_FIXTURE` 게이트 |
| SEC-D24 SecurityConfig 필터 | **Fixed 유지** — `addFilterAfter(tenantContextFilter, BearerTokenAuthenticationFilter.class)` |
| SEC-D14 origin/test P0 | **Fixed 유지** — `598d108`/`c7c8f07` 불변·P0 포함 |
| SEC-008 npm audit prod | **Fixed 유지** — prod **0건**(14차 실측) |

### (E) 우선순위 (14차)

| 순위 | ID | Severity | 조치 |
|------|-----|----------|------|
| P1 | SEC-D4 | Medium | poi-ooxml 5.4.0+ — NHIS+은행입금 2경로 회귀 |
| P1 | A06-1 | Medium | Spring Boot 3.3.x 최신 패치 라인 업그레이드 |
| P2 | SEC-D22 | Low | parent repo `.gitignore` `*.env` 변경 **커밋** |
| P2 | SEC-D25 | Low~Medium | 첨부 magic-byte 검증 공통 유틸 |
| P2 | SEC-D26 | High(dev) | esbuild/vite dev 체인 패치 또는 CI 격리 |
| P2 | SEC-D18 | Low | develop→test merge(242+295)·TSR 승격 |
| P2 | SEC-D28 | Low | prod `ogada.easy-pay.provider` 실 PG 필수·startup 검증 |
| P2 | SEC-D5 | Low | `application-prod.yml` `format_sql:false`·`management.exposure:health` |
| ✅ | 신규 컨트롤러 RBAC·V104~V117·J03 quiet-hours·G21 guard·SEC-D17·D19·D23·D24·D14·SEC-008 prod | — | 14차 Pass/Fixed 확인 |

---

## 1.15 일일 재점검 델타 (2026-06-13 13차) [SEC]

> 이번 호출에서 **workspace 실측**(`git -C src/backend rev-parse HEAD/origin/test` · `git -C src/frontend …` · `git diff 61336df..HEAD`/`b3e59e2..HEAD` · `npm audit` · `pom.xml` · `git check-ignore` · `git show HEAD:.gitignore`)을 12차 `61336df`/`b3e59e2` 기준선과 대조. develop 양 스트림이 v2/v1.2.1/v1.3 다수 기능과 함께 **추가 전진**(BE +46 / FE +55 vs 12차, 각각 origin/test 대비 **198 / 241 ahead**). 양 스트림 **WT CLEAN**. 신규 보안 표면을 소스 직접 정적 분석.

### (A) 상태 변화 — develop 추가 전진 · WT CLEAN · origin/test 불변 · 보안 회귀 없음

| 스트림 | 12차 develop | 13차 develop HEAD | local/origin test | WT |
|--------|--------------|-------------------|-------------------|-----|
| backend | `61336df` | **`bcb1d9f`**(+198 vs test: G40/G40b 위험평가·G42 고충상담·G30 모니터링·US-R03 HR 파일·US-R02 8-12·G21 배정 가드·G9-COG·CMS 취소·G34b·V92~V101) | `598d108`(불변, P0 포함) | **CLEAN** |
| frontend | `b3e59e2` | **`14124d6`**(+241 vs test: 위 기능 UI·G42 결재함·직원현황 리포트·모니터링·HR 파일 허브·67 route) | `c7c8f07`(불변) | **CLEAN** |

→ **판정**: `origin/test`는 12차와 동일(P0 통제 전부 포함) — **배포 산출물 보안 회귀 없음**(SEC-D14 Fixed 유지). develop↔test 격차가 **198/241로 추가 대형화**했으나 전부 **v2/v1.2.1/v1.3 신규 기능**(보안 통제 누락 아님) → **BLOCK 아님**(SEC-D18, Low). QA Open은 TSR **QA-B72**(FE 테스트 중복 버튼) 1건 — **보안 이슈 아님**.

### (B) ✅ 신규 v2/v1.2.1/v1.3 기능 보안 검토 — 전부 RBAC·tenant-safe Pass

| 기능 (커밋) | 판정 | 근거 |
|-------------|------|------|
| **G40/G40b 위험평가** `ClientController`/`ClientRiskAssessmentService` (V94·V96, `22d736b`~`84e59d2`) | **Pass** | admission·periodic read/write `@PreAuthorize`(4역할·write=HQ/BRANCH/SOCIAL_WORKER) · V94/V96 트리거(org/branch 파생·active-client 가드·actor backstop) · `RoleBasedControllerAccessTest` 회귀 |
| **G42 고충상담** `GrievanceCounselingController`/`Service` (V98, `bcdc411`~`bcb1d9f`) | **Pass — 강함** | 9 메서드 `@PreAuthorize`(read=HQ/BRANCH/SOCIAL_WORKER·결재=HQ/BRANCH) · V98 무결성 트리거 · **익명함(`ANONYMOUS_BOX`)은 수납 채널 enum**(인증 직원이 기록 — 공개 endpoint 아님) · 결재·사후관리 follow-up audit |
| **G30 모니터링** `MonitoringController`/`Service` (V101, `6a72b70`~`f4c8558`) | **Pass** | 9 메서드 `@PreAuthorize`(HQ/BRANCH/SOCIAL_WORKER) · V101 트리거 · 자가진단·전화상담 compliance read-only 집계 |
| **US-R03 HR 파일** `StaffHrFileController`/`Service` (V92, `bbb8e35`~`d4ee057`) | **Pass** | 5 메서드 `@PreAuthorize` · upload=BRANCH/SOCIAL_WORKER · V92 트리거 · **첨부 검증 갭은 SEC-D25**(Content-Type만·magic-byte 없음) |
| **US-R02 8-12 직원현황** `StaffStatusReportController` (V99 lineage, `aaa16f8`~`5692662`) | **Pass** | read=HQ/BRANCH/SOCIAL_WORKER · 집계 리포트(PII 마스킹·tenant scope) |
| **G21 배정 요양보호사 가드** `VisitService` (`dc48933`~`b459f4c`) | **Pass — 강함** | create/update/check-in/out 시 **배정 caregiver 검증** · DAY_CARE 분기 거부 · 페어 방문 linkage 재검증 — IDOR·무단 체크인 방어 강화 |
| **G9-COG 인지지원** `BillingController`/seed (V97 lineage, `2efc557`~`8bb6583`) | **Pass** | NHIS import gate=HQ/BRANCH · 수가표 불완전 시 import 거부(데이터 무결성) |
| **G2 CMS 취소** `CmsController`/`Service` (`72aff00`~`a34d0eb`) | **Pass** | `@PreAuthorize(HQ/BRANCH)` · CONFIRMED 청구만 · 중복 active enrollment 가드 유지 |
| **G34b 업무일지 import-draft** `LeadCaregiverWorkLogController` (`8487667`) | **Pass** | 기존 G34 RBAC·V83 불변성 유지 · cognitive role guard |
| **V92~V101 무결성 마이그레이션** | **Pass — 강함** | HR 파일·위험평가·고충상담·모니터링 전부 **org/branch 서버측 파생 + active 가드 + actor backstop** |

### (C) 신규·갱신 이슈

| ID | 항목 | Severity | 상태 | 근거 |
|----|------|----------|------|------|
| **SEC-D26** | **npm audit dev 3건 HIGH — esbuild GHSA-gv7w-rqvm-qjhr** | **High(dev-only)** | **Open(dev)** | `npm audit` dev **3 HIGH**(esbuild 0.25.12·vite 6.4.3·@vitejs/plugin-react 4.7.0). `npm audit --omit=dev` **0건**. 12차 SEC-008(0건) 대비 **dev 회귀** — Deno 모듈 binary integrity 미검증 RCE(CI/dev 서버 노출 시). prod 빌드·런타임 무관. 권고: esbuild ≥패치 또는 vite 체인 업그레이드·Vitest UI/CI 네트워크 격리 |
| **SEC-D27** | **NHIS legacy xls MIME 완화** | **Low** | **Monitor** | `VisitService` `ALLOWED_IMPORT_CONTENT_TYPES`에 `application/vnd.ms-excel`·`application/octet-stream`·charset 변형 허용(`b864272` lineage). 인증 HQ/BRANCH/SOCIAL_WORKER 한정·POI 파싱 표면은 SEC-D4와 동일. 호환성 개선이나 untrusted xlsx 입력 범위 소폭 확대 |
| SEC-D25 | 첨부 업로드 magic-byte 미검증 | Low~Medium | **Open(표면 확대)** | 12차에 이어 **직원 HR 파일**(`StaffHrFileStorageService`)·**보수교육 증명서**(`StaffRefresherTrainingCertificateStorageService`) 동일 패턴(Content-Type+크기만·UUID 저장 키). 기존 사진·급여계약서·등급이력·NHIS·은행입금과 합산 |
| SEC-D22 | `scripts/dev-backend.env` 시크릿 비-gitignore(HEAD) | Low | **Mitigated** | WT `.gitignore`에 `*.env`/`scripts/*.env` 추가 → `git check-ignore scripts/dev-backend.env` **통과**. 단 `git show HEAD:.gitignore`에 `*.env` **미반영**(`M .gitignore` parent repo 미커밋) |
| SEC-D4 | poi-ooxml **5.3.0** — 2개 파싱 표면 | Medium | Open | `pom.xml:64` 5.3.0. NHIS + 은행입금. CVE-2025-31672 미해소 |
| A06-1 | Spring Boot **3.3.1** | Medium | Open | `pom.xml:9` — 3.3.x 패치 라인 업그레이드 검토 |
| SEC-D18 | v2/v1.2.1/v1.3 develop→test merge 미실행 | Low | Monitor | develop 198+241 ahead · `origin/test` P0 포함 · TSR merge 게이트 |
| SEC-D5/D20/D21 | prod `application-prod.yml`·FCMS·`payer_name` | Low | Open/Monitor | 12차와 동일 |

### (D) ✅ 유지 — 12차 Fixed/Pass 재확인

| 항목 | 13차 재확인 |
|------|-------------|
| SEC-D17 raw fetch | **Fixed 유지** — `rg "[^a-zA-Z.]fetch\("` 실측: 앱 코드 raw `fetch()`는 `src/api/http.js:190·224`(apiFetch/refresh 래퍼)뿐 · e2e `pilotLiveApi.e2e.test.js` 1곳 |
| SEC-D19 error handler | **Fixed 유지** — `GlobalExceptionHandler` 변동 없음 |
| SEC-D23 PilotFixturePanel | **Fixed 유지** — `import.meta.env.DEV \|\| VITE_ENABLE_PILOT_FIXTURE` 게이트 |
| SEC-D24 SecurityConfig 필터 | **Fixed 유지** — `addFilterAfter(tenantContextFilter, BearerTokenAuthenticationFilter.class)` |
| SEC-D14 origin/test P0 | **Fixed 유지** — `598d108`/`c7c8f07` 불변·P0 포함 |
| SEC-008 npm audit prod | **Fixed 유지** — prod **0건**(13차 실측) |

### (E) 우선순위 (13차)

| 순위 | ID | Severity | 조치 |
|------|-----|----------|------|
| P1 | SEC-D4 | Medium | poi-ooxml 5.4.0+ — NHIS+은행입금 2경로 회귀 |
| P1 | A06-1 | Medium | Spring Boot 3.3.x 최신 패치 라인 업그레이드 |
| P2 | SEC-D22 | Low | parent repo `.gitignore` `*.env` 변경 **커밋** |
| P2 | SEC-D25 | Low~Medium | 첨부 magic-byte 검증(HR·보수교육 증명서 포함) |
| P2 | SEC-D26 | High(dev) | esbuild/vite dev 체인 패치 또는 CI 격리 |
| P2 | SEC-D18 | Low | develop→test merge(198+241)·TSR 승격 |
| P2 | SEC-D27 | Low | NHIS xls MIME 완화 모니터(POI 상향과 연동) |
| P2 | SEC-D5 | Low | `application-prod.yml` `format_sql:false`·`management.exposure:health` |
| ✅ | 신규 컨트롤러 RBAC·V92~V101·G21 caregiver guard·SEC-D17·D19·D23·D24·D14·SEC-008 prod | — | 13차 Pass/Fixed 확인 |

---

## 1.14 일일 재점검 델타 (2026-06-12 12차) [SEC]

> 이번 호출에서 **workspace 실측**(`git -C src/backend rev-parse HEAD/origin/test` · `git -C src/frontend …` · `git diff 208b37e..HEAD` · `npm audit` · `pom.xml` · `git check-ignore` · `git show HEAD:.gitignore`)을 11차 `208b37e`/`37e6b00` 기준선과 대조. develop 양 스트림이 v2/v1.3 다수 기능과 함께 **추가 전진**(BE +49 / FE +57 vs 11차, 각각 origin/test 대비 **152 / 186 ahead**). 11차 WT DIRTY가 **양 스트림 모두 커밋되어 WT CLEAN** 전환. 신규 보안 표면을 소스 직접 정적 분석.

### (A) 상태 변화 — develop 추가 전진 · WT 정리(CLEAN) · origin/test 불변 · 보안 회귀 없음

| 스트림 | 11차 develop | 12차 develop HEAD | local/origin test | WT |
|--------|--------------|-------------------|-------------------|-----|
| backend | `208b37e`(WT DIRTY 1) | **`61336df`**(+152 vs test: G33 기초잔액·G34 업무일지·G37 등급이력 첨부·G39 제공결과 평가·G24-G14 욕구사정/급여계약서·US-R03 직원 lifecycle·V76~V87) | `598d108`(불변, P0 포함) | **CLEAN** |
| frontend | `37e6b00`(WT DIRTY 10+1U) | **`b3e59e2`**(+186 vs test: 위 기능 UI·US-R03 직원 lifecycle 패널/배지·G34 업무일지·dashboard 컴플라이언스) | `c7c8f07`(불변) | **CLEAN** |

→ **판정**: `origin/test`는 11차와 동일(P0 통제 전부 포함) — **배포 산출물 보안 회귀 없음**(SEC-D14 Fixed 유지·T-T5 Low). develop↔test 격차가 **152/186으로 추가 대형화**했으나 전부 **v2/v1.3 신규 기능**(보안 통제 누락 아님) → **BLOCK 아님**(SEC-D18, Low). 11차 WT DIRTY(SecurityConfig 필터 순서·case-mgmt/dashboard UI)는 **전부 커밋되어 WT CLEAN** — SEC-D24 커밋 완료.

### (B) ✅ 신규 v2/v1.3 기능 보안 검토 — 전부 RBAC·tenant-safe Pass

| 기능 (커밋) | 판정 | 근거 |
|-------------|------|------|
| **US-R03 직원 입사~퇴사 lifecycle** `UserController`/`UserService` (V86·V87, `75440bc`~`61336df`) | **Pass — 강함** | 컨트롤러 클래스 레벨 `@PreAuthorize(HQ_ADMIN\|BRANCH_ADMIN)` · `UserService.enforceRolePolicy`가 **`platform_admin` 생성 차단**(권한상승 방지) + **branch_admin 역할 부여 allowlist**(branch_admin/social_worker/caregiver/guardian/client_user만) · `requireOrganizationId`+branch scope · 비밀번호 `passwordEncoder` 해시 · V87 CHECK 제약(`terminated_at >= hired_at`·TERMINATED 시 날짜 필수)·퇴사 시 offboarding 증빙 강제(`c976f55`) |
| **G24-G14 욕구사정·급여계약서 첨부** `ClientNeedsAssessmentService`/`ClientBenefitContractAttachmentService`/`ClientController` (V84·V85, `6f3315a`~`b238779`) | **Pass** | 메서드별 `@PreAuthorize` · V85 트리거(client에서 org/branch **서버측 파생**·active-client 가드·recorded_by actor backstop) · 첨부 저장 키 `UUID.randomUUID()` 서버 생성(경로 traversal 차단) · home-visit 일자 검증 |
| **G34 책임요양보호사 업무일지** `LeadCaregiverWorkLogController`/`Service` (V82·V83, `559648f`~`ec4cdf6`) | **Pass** | 4 메서드 `@PreAuthorize`(HQ/BRANCH/SOCIAL_WORKER/CAREGIVER) · V83 트리거(org/branch 파생·active-client 가드·created_by backstop·**서명 후 불변성**) · 서명 audit 필드 |
| **G33 청구 기초잔액** `BillingSettingsController`/`BillingSettingsService` (V76·V77, `7ba18c1` 등) | **Pass** | read=HQ/BRANCH · 설정 변경/start-balance=**HQ_ADMIN 단독** · settle=HQ/BRANCH · tenant·branch scope · V77 무결성 |
| **G39 제공결과 평가** `ProvisionResultEvaluationController`/`Service` (V80·V81) | **Pass** | read=4역할·write=HQ/BRANCH/SOCIAL_WORKER·compliance=HQ/BRANCH/SOCIAL_WORKER · V81 무결성 트리거 |
| **G37 등급이력 첨부** `LtcGradeHistoryAttachmentService`/`StorageService` (V78·V79) | **Pass** | 등급이력 read RBAC 유지 · V79 트리거 · 첨부 저장 키 UUID 서버 생성 |
| **G21 페어 방문 링크 검증 강화** `VisitService` (`b7cfc92`~`82bdbcd`) | **Pass** | 페어 방문 상태 전이·체크인/아웃·draft sync 전 linkage 검증 — 무결성 강화(보안 표면 무변동) |
| **V76~V87 무결성 마이그레이션** | **Pass — 강함** | 신규 테이블 전부 **org/branch 서버측 파생 트리거 + active-client 가드 + actor backstop** 일괄 적용 · V87 users lifecycle CHECK 제약 — 크로스테넌트·퇴소 client INSERT·actor 위조 DB-level 차단 |

### (C) ✅ 해소 — 11차 Open 이슈 종결

| ID | 11차 상태 | 12차 develop | 근거 |
|----|-----------|--------------|------|
| **SEC-D23** | Open(Medium) — PilotFixturePanel prod 노출 | **Fixed** | `PilotFixturePanel.jsx` `isPilotFixtureEnabledByEnv()` = **`import.meta.env.DEV \|\| import.meta.env.VITE_ENABLE_PILOT_FIXTURE === "true"`** — prod 빌드(DEV=false·flag 미설정)에서 패널 미렌더. 커밋 `c89a82b`(TSR 346차 Fixed 확인) |
| **SEC-D24** | Pass(WT) — SecurityConfig 필터 순서 | **Fixed (committed)** | `SecurityConfig.java` `addFilterAfter(tenantContextFilter, BearerTokenAuthenticationFilter.class)` **커밋 완료**(WT CLEAN) · permitAll은 health/JWKS·`POST /api/v1/guardian/invitations/*/accept` 단일 경로로 한정 |

### (D) 신규·갱신 이슈

| ID | 항목 | Severity | 상태 | 근거 |
|----|------|----------|------|------|
| **SEC-D25** | **신규 첨부 업로드 magic-byte 미검증** | **Low~Medium** | **Open** | `BenefitContractAttachmentStorageService`·`LtcGradeHistoryAttachmentStorageService`가 **Content-Type 화이트리스트(pdf/png)+크기 제한(10MB)만** 검증, **magic-byte(파일 시그니처) 미검증**. 저장 키는 `UUID.randomUUID()` 서버 생성이라 **경로 traversal·확장자 위조 영향 제한**. 기존 A08-1(사진·NHIS·은행입금)과 동일 클래스 갭 — 업로드 표면 추가. 권고: 공통 magic-byte 검증 유틸(COD) |
| **SEC-D22** | `scripts/dev-backend.env` 시크릿 비-gitignore | **Low (완화·커밋 대기)** | **Mitigated** | parent repo **WT `.gitignore`에 `*.env`·`scripts/*.env`·`scripts/*.env.*`+`!*.env.example` 추가됨** → `git check-ignore scripts/dev-backend.env` **통과**(exit 0). 단 `git show HEAD:.gitignore`에는 **미반영**(WT-only, `M .gitignore` 미커밋) → 커밋 시 종결. 현재 `dev-backend.env` untracked·유출 없음 |
| SEC-D4 | poi-ooxml **5.3.0** — 2개 파싱 표면 | Medium | Open | `pom.xml:63` 5.3.0. NHIS + 은행입금 import. CVE-2025-31672 미해소 |
| A06-1 | Spring Boot **3.3.1** | Medium | Open | `pom.xml:9` — 3.3.x 패치 라인 업그레이드 검토(T-E3) |
| SEC-D18 | v2/v1.3 develop→test merge 미실행 | Low | Monitor | develop 152+186 ahead · `origin/test` P0 포함(보안 회귀 없음) · 대형 batch TSR merge 게이트 |
| SEC-D5/D20/D21 | prod `application-prod.yml`·FCMS validator·`payer_name` 암호화 | Low | Open/Monitor | 11차와 동일 — 변동 없음 |

### (E) ✅ 유지 — 11차 Fixed/Pass 재확인

| 항목 | 12차 재확인 |
|------|-------------|
| SEC-D17 raw fetch | **Fixed 유지** — `rg "[^a-zA-Z.]fetch\("` 실측: 앱 코드 raw `fetch()`는 `src/api/http.js:115·149`(apiFetch/refresh 래퍼)뿐 · 그 외는 e2e 테스트 파일 1곳 |
| SEC-D19 error handler | **Fixed 유지** — `GlobalExceptionHandler` 변동 없음 |
| SEC-D14 origin/test P0 | **Fixed 유지** — `598d108`/`c7c8f07` 불변·P0 포함 |
| SEC-008 npm audit | **Fixed 유지** — prod·dev **0건**(12차 실측) |

### (F) 우선순위 (12차)

| 순위 | ID | Severity | 조치 |
|------|-----|----------|------|
| P1 | SEC-D4 | Medium | poi-ooxml 5.4.0+ — NHIS+은행입금 2경로 회귀 |
| P1 | A06-1 | Medium | Spring Boot 3.3.x 최신 패치 라인 업그레이드 |
| P2 | SEC-D22 | Low | parent repo `.gitignore` `*.env` 변경 **커밋**(WT 추가 완료) |
| P2 | SEC-D25 | Low~Medium | 첨부 업로드 magic-byte 검증(사진·NHIS·은행입금·급여계약서·등급이력 공통) |
| P2 | SEC-D18 | Low | develop→test merge(v2/v1.3 대형 batch)·TSR 승격 |
| P2 | SEC-D5 | Low | `application-prod.yml` `format_sql:false`·`management.exposure:health` |
| ✅ | SEC-D23·D24·신규 컨트롤러 RBAC·UserService 권한상승 차단·V76~V87·SEC-D17·D19·D14·SEC-008 | — | 12차 Fixed/Pass 확인 |

---

## 1.13 일일 재점검 델타 (2026-06-11 11차) [SEC]

> 이번 호출에서 **workspace 실측**(`git -C src/backend rev-parse HEAD/origin/test` · `git -C src/frontend …` · `git diff`/`git show` · `npm audit` · `pom.xml` · `git check-ignore`)을 10차 `d6d7e7f`/`6c4c151` 기준선과 대조. develop 양 스트림이 v2/v1.3 다수 기능과 함께 **대폭 전진**(BE +44 / FE +50 vs 10차, 각각 origin/test 대비 **103 / 129 ahead**). backend WT **DIRTY 1**(`SecurityConfig.java`), frontend WT **DIRTY 10+1U**(case-mgmt/dashboard UI). 신규 보안 표면을 소스 직접 정적 분석.

### (A) 상태 변화 — develop 대형 전진 · origin/test 불변 · 보안 회귀 없음

| 스트림 | 10차 develop | 11차 develop HEAD | local/origin test | WT |
|--------|--------------|-------------------|-------------------|-----|
| backend | `d6d7e7f` | **`208b37e`**(+103 vs test: G16 차량/이송료·G17 기능회복·G26 의료비공제·G32 사례관리·US-M03 환불/원장·US-G04 수가연도·NHIS 비교·V61~V75) | `598d108`(불변, P0 포함) | **DIRTY 1**(`SecurityConfig.java` — SEC-D24) |
| frontend | `6c4c151` | **`37e6b00`**(+129 vs test: 위 기능 UI·G7 NHIS 비교 패널·pilot fixture 도구) | `c7c8f07`(불변) | **DIRTY 10+1U**(case-mgmt/dashboard compliance UI) |

→ **판정**: `origin/test`는 10차와 동일(P0 통제 전부 포함) — **배포 산출물 보안 회귀 없음**(SEC-D14 Fixed 유지·T-T5 Low). develop↔test 격차가 **103/129로 추가 대형화**했으나 전부 **v2/v1.3 신규 기능**(보안 통제 누락 아님) → **BLOCK 아님**(SEC-D18, Low). frontend WT DIRTY 10은 G17/G32 compliance·dashboard 위젯 UI diff뿐 — **fetch·토큰·인가 무관**(정적 확인). backend WT DIRTY 1은 SecurityConfig 필터 순서 **보안 강화**(SEC-D24).

### (B) ✅ 신규 v2/v1.3 기능 보안 검토 — 전부 RBAC·tenant-safe Pass

| 기능 (커밋) | 판정 | 근거 |
|-------------|------|------|
| **G32 사례관리 회의** `CaseManagementController`/`Service` (V73·V75, `55fae99`~`11277b9`) | **Pass** | 4 메서드 `@PreAuthorize`(read=4역할·write=HQ/BRANCH/SOCIAL_WORKER) · V74 트리거: org/branch를 **client에서 서버측 파생**(클라 입력 무시)·퇴소/비활성 client 가드·`created_by` actor backstop · quarter 파라미터 범위 검증(`fea28b8`) |
| **G17 기능회복 계획** `FunctionalRecoveryController`/`Service` (V72, `73e169a`) | **Pass** | 4 메서드 `@PreAuthorize` · V74 트리거(org/branch 파생·active client 가드·`created_by` backstop) · 서버 검증오류 field 매핑(`b58429d`) |
| **US-M03 본인부담 환불·원장 리포트** `BillingController` `/refunds`·`/reports/{variant}` (V71, `de49b21`~`0af6526`) | **Pass** | `@PreAuthorize(HQ/BRANCH)` · V74 `refund_recorded_by` actor 트리거 · `paidAt`/`copayAmount` null·no-op 전이 가드(`4001510`·`970f547`·`923e610`) |
| **G26 의료비 세액공제** `BillingService`/`ClientController`/`GuardianCheckinController` (`7f10449`) | **Pass** | `@PreAuthorize` · **CMS·간편결제 본인부담은 공제 대상 제외**(`970f547` — 중복 공제 방지) · 보호자/직원 경로 tenant 스코프 |
| **US-G04 수가연도 커버리지** `BillingController` `/fee-schedules/year-coverage` (`8f208e4`·`970c7af`) | **Pass** | `@PreAuthorize(HQ/BRANCH)` · 수가표 연도 그리드 불완전 시 NHIS import 거부(데이터 무결성) |
| **NHIS 청구 비교 API** `BillingController` `/claims/{id}/nhis-comparison` (`2225a7a`) | **Pass** | `@PreAuthorize(HQ/BRANCH)` · 신규 파싱 표면 없음(기존 POI 경로 동일·SEC-D4 별개) |
| **G15 외출관리** `ClientOutingController`/`Report` (V67·V70, `7dfcc9e`) | **Pass** | 메서드별 `@PreAuthorize`(report=HQ/BRANCH/SOCIAL_WORKER) · V70 복합 테넌트 FK `(org,branch,client)` REFERENCES clients · org/branch 트리거 파생·active client 가드·`recorded_by` backstop |
| **G16 차량/이송료** `VehicleController`/`TransportController` (V68·V69·V70, `bd375e6`·`88d4c59`) | **Pass** | 메서드별 `@PreAuthorize`(create/update=HQ/BRANCH) · **크로스-브랜치 이송료 갱신 차단**(`b5218a9`) · V70 트리거(client에서 org/branch 파생·`uses_transport`/active/branch 일치 가드) |
| **client 생성 RBAC 확대** `ClientController` POST `/clients` (`208b37e`, HEAD) | **Pass** | `BRANCH_ADMIN,SOCIAL_WORKER` → **`HQ_ADMIN` 추가** · 역할 매트릭스 정합(hq_admin = active_branch PII 쓰기 ☑) · service층 tenant·branch 스코프 유지 · `RoleBasedControllerAccessTest` +71 회귀 보강 |
| **J03 Solapi 승인 템플릿 강제** `NotificationConfig` (`98e40a3`) | **Pass** | 승인된 템플릿 매핑만 허용(임의 본문 alimtalk 차단) — 알림 무결성 강화 |
| **V61~V74 무결성 마이그레이션** (`622b5e5` 등) | **Pass — 강함** | V70/V74가 신규 테이블에 **org/branch 서버측 파생 트리거 + 복합 테넌트 FK + active-client 가드 + actor backstop** 일괄 적용 — 크로스테넌트·퇴소 이용자 INSERT·actor 위조 DB-level 차단 |

### (C) 신규·갱신 이슈

| ID | 항목 | Severity | 상태 | 근거 |
|----|------|----------|------|------|
| **SEC-D22** | **`scripts/dev-backend.env` 시크릿 비-gitignore** | **Medium** | **Open** | `git check-ignore scripts/dev-backend.env` → **미일치**(exit 1). 파일에 `DB_PASSWORD`·`PII_ENCRYPTION_KEY`·`QR_TOKEN_SECRET` **평문** 보유. `.gitignore`는 `.env`·`.env.*` 패턴만 — `dev-backend.env`(접두 `.env` 아님)는 **미포함**. 현재 untracked(미커밋, 유출 아님)이나 `git add .` 시 **시크릿 커밋 위험**. 권고: `.gitignore`에 `*.env` 또는 `scripts/*.env` 추가(parent repo·COD/OPS). QA Open `[SEC]` 기록 |
| **SEC-D23** | **PilotFixturePanel — dev/pilot 데이터 시딩 도구가 prod 빌드 노출** | **Medium** | **Open** | `PilotFixturePanel.jsx`(`37e6b00` 커밋)가 **`import.meta.env.DEV` 게이트 없이** 역할(`hq_admin`/`branch_admin`)만으로 `OrganizationSettingsPage`에 렌더. `runPilotFixtureSetup`이 인증 API로 더미 client(합성 RRN `450315-…` 등) 일괄 생성·샘플 xlsx 다운로드 → **prod 테넌트에 더미 PII 오염** 가능. RBAC 바인딩이라 침해/크로스테넌트 아님이나 insecure design. develop 커밋됨 → merge 시 test/prod 유입. 권고: DEV/feature-flag 게이트(merge 전·QA-B43 후속) |
| **SEC-D24** | SecurityConfig 필터 순서 — tenantContextFilter를 `BearerTokenAuthenticationFilter` 뒤로 이동 | — | **Pass (보안 강화·WT)** | 기존 `addFilterAfter(…, UsernamePasswordAuthenticationFilter)`는 JWT 인증(`BearerTokenAuthenticationFilter`) **이전** 실행 → `SecurityContext` 미설정 상태에서 `TenantContext` 미채움(잠재 결함). 변경 후 **인증 후 실행**되어 JWT principal로 org/branch 정확히 설정. 우회 도입 없음·permitAll 경로 영향 없음. WT-only → 커밋 게이트 |
| SEC-D4 | poi-ooxml **5.3.0** — 2개 파싱 표면 | Medium | Open | `pom.xml:64` 5.3.0 고정. NHIS + 은행입금 import. CVE-2025-31672 미해소 |
| A06-1 | Spring Boot **3.3.1** | Medium | Open | `pom.xml:9` — 3.3.x 패치 라인 업그레이드 검토(T-E3) |
| SEC-D18 | v2/v1.3 develop→test merge 미실행 | Low | Monitor | develop 103+129 ahead · `origin/test` P0 포함(보안 회귀 없음) · 대형 batch TSR merge 게이트 |
| SEC-D5/D20/D21 | prod `application-prod.yml`·FCMS validator·`payer_name` 암호화 | Low | Open/Monitor | 10차와 동일 — 변동 없음 |

### (D) ✅ 유지 — 10차 Fixed/Pass 재확인

| 항목 | 11차 재확인 |
|------|-------------|
| SEC-D17 raw fetch | **Fixed 유지** — `rg "[^a-zA-Z.]fetch\("` 실측: raw `fetch()`는 `src/api/http.js:115`(apiFetch 래퍼) **1곳뿐**. pilot fixture 도구도 `services.js` 경유 |
| SEC-D19 error handler | **Fixed 유지** — `GlobalExceptionHandler` 변동 없음 |
| SEC-D14 origin/test P0 | **Fixed 유지** — `598d108`/`c7c8f07` 불변·P0 포함 |
| SEC-008 npm audit | **Fixed 유지** — prod·dev **0건**(11차 실측) |

### (E) 우선순위 (11차)

| 순위 | ID | Severity | 조치 |
|------|-----|----------|------|
| P1 | SEC-D22 | Medium | `.gitignore`에 `*.env`/`scripts/*.env` 추가 — 시크릿 커밋 차단(COD/OPS) |
| P1 | SEC-D4 | Medium | poi-ooxml 5.4.0+ — NHIS+은행입금 2경로 회귀 |
| P1 | A06-1 | Medium | Spring Boot 3.3.x 최신 패치 라인 업그레이드 |
| P2 | SEC-D23 | Medium | PilotFixturePanel `import.meta.env.DEV` 게이트(merge 전) |
| P2 | SEC-D24 | — | SecurityConfig 필터 순서 변경 커밋(보안 강화·WT clean 게이트) |
| P2 | SEC-D18 | Low | develop→test merge(v2/v1.3 대형 batch)·TSR 승격 |
| P2 | SEC-D5 | Low | `application-prod.yml` `format_sql:false`·`management.exposure:health` |
| ✅ | 신규 컨트롤러 RBAC·V70/V74·SEC-D17·D19·D14·SEC-008 | — | 11차 Pass/Fixed 확인 |

---

## 1.12 일일 재점검 델타 (2026-06-10 10차) [SEC]

> 이번 호출에서 **workspace 실측**(`git -C src/backend rev-parse HEAD/origin/test` · `git -C src/frontend …` · `git status --porcelain` · `npm audit` · `pom.xml`)을 9차 `dd49204`/`ac5638e` 기준선과 대조. develop 양 스트림이 v2(G2 결제/CMS·이메일)·v1.3(G15 이동서비스) 다수 기능과 함께 **대폭 전진**(BE +59 / FE +74 vs `origin/test`). backend WT **CLEAN**, frontend WT **DIRTY 4**(transport UI). 신규 보안 표면을 `git show`/소스 직접 정적 분석.

### (A) 상태 변화 — develop 대형 전진 · origin/test 불변 · 보안 회귀 없음

| 스트림 | 9차 develop | 10차 develop HEAD | local/origin test | WT |
|--------|-------------|-------------------|-------------------|-----|
| backend | `dd49204` | **`d6d7e7f`**(+59 vs test: v2 G2 결제/CMS·SMTP·은행입금·G11 가산·월한도·G15 transport) | `598d108`(불변, P0 포함) | **CLEAN** |
| frontend | `ac5638e` | **`6c4c151`**(+74 vs test: CMS UI·은행입금·G9 수가·G11/G15 패널·a11y) | `c7c8f07`(불변) | **DIRTY 4**(transport UI) |

→ **판정**: `origin/test`는 9차와 동일(P0 통제 전부 포함) — **배포 산출물 보안 회귀 없음**(SEC-D14 Fixed 유지·T-T5 Low). develop↔test 격차가 **59/74로 대형화**했으나 전부 **v2/v1.3 신규 기능**(보안 통제 누락 아님) → **BLOCK 아님**(SEC-D18, Low). frontend WT DIRTY 4는 `countGeocodeFailures` 표시용 UI diff뿐 — **fetch·토큰·인가 무관**(정적 확인). backend WT CLEAN.

### (B) ✅ 신규 v2/v1.3 기능 보안 검토 — 전부 RBAC·tenant-safe Pass

| 기능 (커밋) | 판정 | 근거 |
|-------------|------|------|
| **CMS/FCMS 자동이체** `CmsController`/`CmsService` (US-L03·G2, `2c6e57e`·`a4a1393`) | **Pass — 강함** | 4 메서드 전부 `@PreAuthorize(HQ_ADMIN\|BRANCH_ADMIN)` · `requireOrganizationId`+`validateBranchWrite/ReadScope` · `guardianClientRepository.existsBy…`(연결 보호자만 등록) · CONFIRMED 청구만·단일이용자 청구 가드·REQUESTED/SUCCEEDED 멱등 · **최소 수집**(payer_name·bank_code·**account_last4 4자리만**·FCMS member_id — 전체 계좌번호 미저장) |
| **CMS 테넌트 무결성** `V59`+`V60` (DBA round 96) | **Pass — 강함** | V60이 V59 단일 FK 위에 **복합 테넌트 FK**(organization_id, branch_id\|client_id\|guardian_user_id\|claim_id\|enrollment_id) 추가 → 타 테넌트 청구↔CMS 위임 교차참조 차단(금융 PII 격리). FK backing index 동반 |
| **은행 입금 Excel import** `BankDepositImportService`/`BankDepositExcelParser` (US-L01, `e50533f`·`95bb34d`) | **Pass** | `@PreAuthorize(HQ_ADMIN\|BRANCH_ADMIN)`(BillingController)·`validateBranchWriteScope` · 매칭 후보 **org+branch 스코프**(`findByOrganizationIdAndBranchId…` — 크로스테넌트 없음) · audit log는 **건수만**(입금자/이용자명 미로깅) · 응답의 입금자/이용자명은 업로더(인가 관리자) 한정 |
| **SMTP 이메일** `SmtpEmailProvider`/`NotificationConfig` (G2/J03, `6ed48ff`·`f23f15a`) | **Pass** | 로그에 이메일 `maskEmail`(`a***@domain`)·**본문/payload 미로깅** · from-address fail-fast 검증 · `validateSmtpConfiguration`이 host/port 누락 시 startup fail(fail-closed) |
| **G15 이동서비스 계약서** `TransportContractService` (`3c8f9fe`) | **Pass** | read=4역할·save=HQ/BRANCH/SOCIAL_WORKER · `requireOrganizationId`+branch scope · `usesTransport` 가드 · 서명은 **서명자 성명+날짜 텍스트**(생체 이미지 아님) · `recordedBy` actor 기록 |
| **G11 가산·월한도** (`904072b`·`a92e625`) | **Pass** | 청구 생성 RBAC 유지 · `RoleBasedControllerAccessTest`·CMS billing RBAC 테스트(`399bc22`) 회귀 보강 |

### (C) ✅ 해소 — 9차 잔존 이슈 종결

| ID | 9차 상태 | 10차 develop | 근거 |
|----|----------|--------------|------|
| **SEC-D17** | Open(부분 해소) Medium | **Fixed** | `rg "[^a-zA-Z]fetch\("` 실측 — raw `fetch()`는 **`src/api/http.js`(apiFetch 래퍼) 1곳뿐**. 9차 지목 `SettingsPage`(`changePasswordApi`)·`PlatformPage`·`BackupSettingsPanel`·`LoginHistoryPanel`·`AuditLogPanel` 전부 `services.js`/`apiFetch` 경유로 전환(`3803247`·`e1320f4` lineage). A07-6·T-I9 해소 |
| **SEC-D19** | Monitor(WT) Low | **Fixed (committed)** | `GlobalExceptionHandler` 커밋 완료(WT 아님). DB 핸들러(`InvalidDataAccessResourceUsage`·`DataAccessException`·`DataIntegrityViolation`)는 `getMostSpecificCause()`를 **substring 매칭에만** 사용하고 응답엔 **고정 한국어 메시지만** echo · 전부 `log.error` 서버 기록. 잔여 caveat(스키마 드리프트·이메일 중복 힌트, 인증 한정)는 Low로 A09-5 유지 |

### (D) 신규·갱신 이슈

| ID | 항목 | Severity | 상태 | 근거 |
|----|------|----------|------|------|
| SEC-D4 | poi-ooxml **5.3.0** — 이제 **2개 파싱 표면** | **Medium (상향)** | Open | `pom.xml:64` 고정 5.3.0. NHIS import(`NhisImportService`)에 더해 **은행 입금 import**(`BankDepositExcelParser` `new XSSFWorkbook`)가 신규 untrusted xlsx 표면 추가. CVE-2025-31672 노출 경로 2배 → 우선순위 상향 |
| SEC-D20 | **FCMS prod credential startup 검증 없음** | Low | Monitor | `FcmsProperties`(`ogada.fcms.api-key`/`merchant-id`) `ProductionSecretValidator` 미포함. 단 `FcmsConfig`는 stub 클라이언트만 `@ConditionalOnProperty(stub, matchIfMissing)` — 실 provider 설정 시 매칭 bean 부재로 startup fail(fail-closed). 실 FCMS 연동은 skeleton(stub). credential 미설정 데이터 유출 없음 |
| SEC-D21 | `cms_enrollments.payer_name` 평문 저장(예금주명 — 금융 PII) | Low | Monitor | `V59` `payer_name VARCHAR(100)` 평문 · `account_last4`(4자리)·`bank_code`는 저자극. RRN/전화의 AES-GCM 대비 일관성 갭. 전체 계좌번호는 미저장이라 영향 제한. PII 정책 정합 위해 향후 암호화 검토 |
| SEC-D32 | `cash_receipt_issuances.identifier_value` 평문 저장(휴대폰/사업자번호) | Low | Open(Monitor) | `V158` `identifier_value VARCHAR(32)` 평문 · API `maskIdentifier()` 마스킹 · `@PreAuthorize(HQ/BRANCH_ADMIN)`·tenant scope · SEC-D21과 동일 at-rest 갭 패턴(19차 신규) |
| SEC-D15 | Solapi/SMTP prod credential — **config-time 검증으로 개선** | Low | **Partial Fixed** | `NotificationConfig.validateSolapiConfiguration`(apiKey·apiSecret·senderId·kakaoPfId) + `validateSmtpConfiguration`(host·port) **bean 생성 시 startup fail**(provider 명시 활성 시). `ProductionSecretValidator` 미포함이나 fail-closed 보강됨. FCMS만 SEC-D20으로 잔존 |
| A06-1 | Spring Boot **3.3.1** | Medium | Open | `pom.xml:9` — 3.3.x 패치 라인 업그레이드 검토(T-E3). 9차 §1.5의 3.5.3(`7d9d2eb`)은 baseline 재설정으로 폐기·현 develop은 3.3.1 |
| SEC-D18 | v2/v1.3 develop→test merge 미실행 | Low | Monitor | develop 59+74 ahead · `origin/test` P0 포함(보안 회귀 없음) · 대형 batch이므로 TSR merge·회귀 검증 게이트 |

### (E) 우선순위 (10차)

| 순위 | ID | Severity | 조치 |
|------|-----|----------|------|
| P1 | SEC-D4 | Medium↑ | poi-ooxml 5.4.0+ — **NHIS + 은행입금** 두 import 경로 회귀 테스트 |
| P1 | A06-1 | Medium | Spring Boot 3.3.x 최신 패치 라인 업그레이드(전 모듈 회귀) |
| P2 | SEC-D18 | Low | develop→test merge(v2/v1.3 대형 batch)·TSR 승격 검증 |
| P2 | SEC-D5 | Low | `application-prod.yml` `format_sql:false`·`management.exposure:health` |
| P2 | SEC-D20/D21 | Low | FCMS credential validator(선택)·payer_name 암호화 검토 |
| P2 | A05-2/3 | Medium | CORS allowlist·보안 헤더(HSTS/CSP) 명시 |
| ✅ | SEC-D17·D19·CMS·은행입금·SMTP·G15·SEC-D14·SEC-008 | — | 10차 Fixed/Pass 확인 |

---

## 1.5 일일 재점검 델타 (2026-06-07 3차) [SEC]

> 이번 호출에서 `src/backend`(develop HEAD `7d9d2eb`)·`src/frontend`(develop HEAD `f1c89d9`)의 **커밋(develop) / 워킹트리 / test 브랜치** 3축을 `git show develop:<path>` 기준으로 직접 대조.

### (A) ✅ 해소 — 백엔드 P0 패치 develop 커밋 완료 (2차 §1.5-A CRITICAL 종결)

2차 점검의 최상위 이슈(P0 패치 워킹트리만·develop 미커밋)가 develop `7d9d2eb`("fix(v1): … SEC rate limit·prod secret 검증 develop 반영")로 **커밋되어 해소**됐다. `git show develop:` 기준 직접 확인:

| 항목 | develop `2799e29` (이전) | develop `7d9d2eb` (현재 커밋) | 근거 |
|------|------|------|------|
| DB 기본 비밀번호 | `DB_PASSWORD:ogada` 잔존 | **`${DB_PASSWORD:}`** (기본값 제거) | `application.yml:14` |
| JWT prod 시크릿 검증 | 없음(ephemeral 폴백) | **prod 미설정 시 startup fail** | `security/JwtKeyConfig.java:51` |
| QR prod 시크릿 검증 | 없음 | **prod 미설정 시 startup fail** | `attendance/domain/QrTokenService.java:31-33` |
| `ProductionSecretValidator` | 부재 | **커밋됨** (JWT·QR·**PII**·DB 검증, 기본값 `ogada` 거부) | `security/ProductionSecretValidator.java:38-50` |
| auth rate limit | 부재 | **`AuthRateLimitService` 연동** (login·refresh·reset) | `auth/domain/AuthService.java:115·156·267·305` |
| Spring Boot | 3.3.1 | **3.5.3** | `pom.xml:9` |

→ **판정**: develop 기준 **A02-1·A02-2·A04-1·A05-1 해소**, A06-1(Boot) 상향 완료(§(C) SEC-D3 참조). 또한 2차 신규 이슈 **SEC-D2(PII 키 startup 검증) 해소** — `ProductionSecretValidator`가 `PII_ENCRYPTION_KEY` requireNonBlank 포함(QA `SEC-20260606-006` Fixed와 정합).

### (A′) ⚠ 잔존 — develop만 패치, test/operation 미승격 (배포 산출물 여전히 취약)

해소는 **develop 한정**이다. 배포 경로의 다음 단계는 여전히 패치 이전 상태:

| 브랜치/워크트리 | backend HEAD | 보안 상태 |
|----------------|--------------|-----------|
| `develop` | `7d9d2eb` | P0 패치 **포함** ✓ |
| `test` (`src/backend-test`) | **`2799e29`** | P0 패치 **전부 부재** (ephemeral key·기본 DB 비번·rate limit 없음) |
| `operation`/prod | 미승격 | 〃 |

→ develop→test merge가 미실행(TSR `QA-20260606-B01`)이라, **현재 test/operation에서 빌드되는 산출물은 모든 P0 취약점을 그대로 포함**한다. SEC 관점에서 "검증 코드 ≠ 배포 코드" 무결성 갭은 **위치만 이동**(워킹트리→브랜치 승격 단계)했을 뿐 해소되지 않음 → **T-T5 유지**, `[SEC]` Open `SEC-20260606-007`로 기록.

### (B) 진전 유지 — 프론트 라우트 가드 (변동 없음)

`src/frontend` develop `f1c89d9`의 `ProtectedRoute.jsx`·`App.jsx` 역할 allow 목록은 2차와 동일하게 커밋 유지(`/platform`=platform_admin, `/dashboard/hq`=hq_admin·platform_admin, `/settings`=sysadmin·hq_admin·platform_admin, `/guardian`=guardian·client_user). A01-1·T-S4 클라이언트 레이어 완화 유지. **클라이언트 가드는 보안 경계가 아님** — 백엔드 JWT가 실경계.

### (B′) 프론트 실인증·메모리 토큰 — 워킹트리만 (SEC-D1 develop 미해소)

긍정: 워킹트리 `auth/AuthContext.jsx`가 **메모리 전용 세션(useState)**으로 전환됐고(주석 `SEC-20260606-005: keep JWT tokens in memory only`), 실 JWT 연동(`src/api/http.js`·`services.js`, Bearer)·로그인 API가 구현됨. **그러나 develop `f1c89d9` 커밋본은 여전히 `localStorage` 역할 데모 인증**(`git show develop:src/auth/AuthContext.jsx` → `localStorage.getItem/setItem(STORAGE_KEY)`), `src/api/`는 untracked.

→ **SEC-D1/SEC-D5(토큰 저장)은 develop 기준 Open 유지**, 워킹트리 한정 완화. QA `SEC-20260606-005`(Open/Planned)와 정합.

### (C) 신규/갱신 취약점

| ID | 항목 | Severity | 상태 | 근거 |
|----|------|----------|------|------|
| SEC-D1 | 프론트 토큰 저장 — develop 커밋본 `localStorage` 데모 인증 | **High** | Open(develop) / 워킹트리 완화 | develop `AuthContext.jsx`는 localStorage, 메모리 세션은 워킹트리만 (§B′) |
| SEC-D3 | Spring Boot **3.5.3** 채택 (권고했던 3.3.19 LTS 아님) | Medium | Monitor | develop `pom.xml:9` 커밋 — 3.3.1 CVE는 해소(신버전). 단 3.5.x 유지보수 라인·전 모듈 회귀 검증 필요(TSR `mvn test` 79/79 PASS는 develop 워킹트리 기준) |
| SEC-D4 | `poi-ooxml` 여전히 **5.3.0** | Medium | Open | develop `pom.xml:60` 명시 고정 — Boot 3.5.3 BOM 자동 상향 아님. CVE-2025-31672 미해소(A06-2·§5) |
| SEC-D5 | prod `format_sql: true`·`management.exposure: health,info` 오버라이드 부재 | Low | Open | develop `application.yml` — prod 프로필 오버라이드 없음. `info` 엔드포인트 빌드/git 메타 노출 가능 |
| SEC-D6 | **frontend dev 의존성 `vitest` Critical** (UI 서버 임의 파일 read/exec) | High(dev-only) | Open(dev) | `npm audit` — GHSA(vitest UI). prod 빌드 무관, **Vitest UI 미노출·CI 격리 시 영향 제한**. esbuild·vite moderate 동반 |
| SEC-D7 | (검토) 신규 client↔guardian primary-link 기능 | — | **Pass(tenant-safe)/미커밋** | 워킹트리 `ClientService.linkGuardianInternal`·`GuardianClientRepository.countByOrganizationIdAndClientId`·`V39` — org/branch 스코프·`@NotNull`·relationship sanitize·파라미터화 트리거. 신규 IDOR/크로스테넌트 갭 없음. 단 develop 미커밋(TSR `B06`) |

### (D) 권고 (우선순위)

1. **develop→test→operation 승격** — develop `7d9d2eb` P0 패치를 test로 merge해야 배포 산출물이 비로소 안전 (TSR `B01`). 승격 전 test/operation은 prod 배포 금지.
2. SEC-D1: 프론트 실인증(`src/api/`)·메모리 세션 `AuthContext`를 develop 커밋 (QA `SEC-005`·`H04`).
3. SEC-D4: `mvn dependency:tree`로 POI 실버전 재확인 후 `poi-ooxml` 5.4.0+ 명시 고정.
4. SEC-D6: `vitest`/`vite` 업그레이드 또는 CI에서 Vitest UI 비활성·네트워크 격리. prod 영향 없음이나 CI 러너 노출 주의.
5. SEC-D5: prod 프로필 `application-prod.yml`에 `format_sql:false`·`management.exposure: health` 오버라이드.

---

## 1.6 일일 재점검 델타 (2026-06-07 4차) [SEC]

> 이번 호출에서 `transfer/backend/develop-test-diff-20260607.md`(56차, 10:01 UTC), `transfer/frontend/develop-test-diff-20260607.md`(57차, 10:11 UTC), `docs/qa/QA_FEEDBACK.md` Open 항목을 기준으로 3차 대비 변화 추적.

### (A″) ✅ 최종 해소 — develop→test 승격 완료 (SEC-007 종결)

3차 §1.5-A′에서 "배포 경로 무결성 갭"으로 지적된 test 브랜치 미승격이 **TSR 34차(17:10 KST)에 완전 해소**됐다.

| 브랜치 | HEAD (4차 기준) | 보안 상태 |
|--------|----------------|-----------|
| `develop` | `428ba7d` | P0 패치 + B02·B08 기능 포함 ✓ |
| `test` | **`e8750d2`** | **P0 패치 전부 포함** ✓ (`ProductionSecretValidator` PRESENT, Boot 3.5.3, rate limit, prod secret 가드) |
| `operation`/prod | 미승격 | test→operation 승격 잔여 |

→ SEC-007 **Fixed**. T-T5 SEC 패치 기준 해소. `QA_FEEDBACK.md` SEC-20260606-007 Fixed 이동.

### (B″) ✅ 해소 — npm audit dev 0건 (SEC-D6 / SEC-008)

`package.json` `overrides.esbuild ^0.25.0` + `vitest ^4.1.8` + `vite ^6.4.3` 업그레이드(develop `ed1bf22`)로 TSR 25차 검증 시 `npm audit --audit-level=high` **0건**. 3차에서 Critical로 기록한 Vitest UI arbitrary file read/exec CVE 해소.

→ SEC-D6 **Fixed**. SEC-008 Fixed.

### (C″) 신규 이슈 (4차)

| ID | 항목 | Severity | 상태 | 근거 |
|----|------|----------|------|------|
| SEC-D8 | J01 WIP `SecurityConfig.java` 미커밋 — guardian invitation public endpoint 허용 범위 미확인 | **Medium** | **Open (WIP)** | QA-B09 범위 `SecurityConfig.java` modified (develop WT, HEAD ABSENT). `POST /guardian/invitations/{token}/accept` 비인증 endpoint 허용 목록 추가 추정. 범위 과잉 시 인증 우회 가능. `InvitationTokenService` 단일 사용·만료·rate limit 미확인 |
| SEC-D9 | `GuardianListCard.jsx` MaskedPhone 마스킹 테스트 회귀 — PII 전화번호 표시 정책 불일치 | **Medium(pending)** | **Open (WIP)** | QA-20260607-H05: WT `npm test` **209/210 FAIL** — `GuardianListCard.test.jsx` 기대 `010-1234-5678`(평문) vs 실제 컴포넌트 `010-****-5678`(마스킹). 컴포넌트 마스킹 유지 중으로 관측. WIP 미커밋 상태 — commit 전 마스킹 정상 동작 확인 필수(FE-7 게이트) |

### (D″) QA-B09 보안 관점 분석

56차(10:01 UTC) 기준 develop WT에 `SecurityConfig.java`·`GlobalExceptionHandler.java` 수정 및 `GuardianInvitationController.java`·`InvitationTokenService.java` untracked. 보안 검토 항목:

1. **SecurityConfig 허용 목록**: `POST /guardian/invitations/{token}/accept`를 `permitAll()`에 추가하는 경우 경로 패턴이 정확히 한정되어야 함 (`/guardian/invitations/**` 식 과잉 허용 금지).
2. **InvitationTokenService**: 토큰은 ① UUID/Random 128-bit 이상 엔트로피, ② 단일 사용(used_at 플래그 또는 V43 스키마), ③ 만료(exp 컬럼 또는 TTL), ④ 발급·수락·만료 audit 필수.
3. **GlobalExceptionHandler 변경**: `InvitationExpiredException` 등 신규 예외가 스택·토큰 값을 응답에 노출하지 않는지 확인.

→ J01 WIP 커밋 전 위 3개 항목을 코드 리뷰 게이트로 삽입 권고. QA-B09 Fixed 조건에 SEC-D8 체크리스트 포함 요청.

### (E″) 잔존 이슈 우선순위 (4차 재정렬)

| 순위 | ID | Severity | 조치 |
|------|-----|----------|------|
| P0 | — | — | 모든 P0 **test 포함 해소** ✓ |
| P1 | SEC-D1 | High | 프론트 develop 커밋 시 `AuthContext` localStorage 0건 확인 (SEC-005 유지) |
| P1 | SEC-D8 | Medium | J01 SecurityConfig 코드 리뷰 (허용 경로 최소화·토큰 단일사용·만료) |
| P1 | SEC-D4 | Medium | `poi-ooxml` 5.4.0+ 명시 상향 |
| P2 | SEC-D9 | Medium(pending) | MaskedPhone 마스킹 commit 시 FE-7 게이트 확인 |
| P2 | SEC-D5 | Low | prod `format_sql: false`·`management.exposure: health` 오버라이드 |
| P2 | A05-2/3 | Medium | CORS allowlist·보안 헤더 명시 |

---

## 1.7 일일 재점검 델타 (2026-06-08 5차) [SEC]

> 이번 호출에서 **workspace 실측**(`git -C src/backend rev-parse HEAD` · `git -C src/frontend rev-parse HEAD` · `status --porcelain`)을 4차 TSR 기준선과 대조. 4차 결론은 TSR/develop checkout(`428ba7d`/`d5654c0`) 기준이며, **현재 ogada workspace submodule HEAD와 불일치**.

### (A‴) ⚠ BLOCK — workspace submodule checkout 드리프트 (SEC-D10)

| 스트림 | workspace develop HEAD | TSR/develop 기준선 | 격차 |
|--------|------------------------|-------------------|------|
| backend | **`2799e29`** (`feat: Spring Boot 3.x 백엔드 초기 구현`) | **`428ba7d`** (V42·NotificationPreference·B02/B08 Fixed) | P0 패치·Boot 3.5.3·rate limit·`ProductionSecretValidator` **전부 ABSENT** |
| frontend | **`e5fd48d`** (`feat: React Vite SPA 초기 스켈레톤`) | **`d5654c0`** (FE-17 J01·ProtectedRoute·199 tests) | 라우트 가드·AuthContext·`src/api/`·SEC-008 업그레이드 **전부 ABSENT** |

→ **판정**: SEC 4차 §1.6-A″(SEC-007 종결)·B″(SEC-008 Fixed)·C″(SEC-D8/D9)는 **TSR 검증 checkout 기준**이며 workspace에서 **재현 불가**. 보안 감사·배포 게이트는 checkout 동기화 선행 필수 → `QA_FEEDBACK` **SEC-20260608-011 Open**.

### (B‴) workspace backend HEAD `2799e29` — P0 통제 전면 부재 (SEC-D11)

`git show HEAD:` 및 소스 직접 확인:

| 통제 | workspace HEAD | TSR `428ba7d` | 근거 |
|------|----------------|---------------|------|
| JWT prod 키 필수 | ✗ ephemeral 폴백 | ✓ startup fail | `JwtKeyConfig.java:43-44` warn + `generateEphemeralKeyPair()` |
| QR prod 시크릿 | ✗ UUID 랜덤 폴백 | ✓ prod 가드 | `QrTokenService.java:24-26` |
| DB 기본 비밀번호 | ✗ `ogada` 기본값 | ✓ `${DB_PASSWORD:}` + validator | `application.yml:14` |
| auth rate limit | ✗ 부재 | ✓ `AuthRateLimitService` | `AuthService.java` — rate limit 호출 0건 |
| PII/JWT/QR startup 검증 | ✗ 부재 | ✓ `ProductionSecretValidator` | grep 0건 |
| Spring Boot | **3.3.1** | **3.5.3** | `pom.xml:9` |
| poi-ooxml | **5.3.0** | 5.3.0(동일) | `pom.xml:60` — CVE-2025-31672 잔존 |

**긍정(유지)**: `@PreAuthorize` 컨트롤러 RBAC · `PiiCryptoService` fail-closed · `GlobalExceptionHandler` 500 스택 미노출 · RRN reveal `@PreAuthorize` + audit · JPA 파라미터 바인딩.

**워킹트리(9 untracked)**: `V35`~`V43` migration — **HEAD ABSENT**. `V43__guardian_invitations.sql` 정적 검토: `token_hash` SHA-256 저장·`expires_at`·상태 lifecycle·tenant FK 트리거 — **스키마 설계 양호**. Java `GuardianInvitationController`/`InvitationTokenService`/`SecurityConfig` 변경은 workspace에 **미존재** → SEC-D8 **workspace에서 검증 불가**(Planned 유지).

### (C‴) workspace frontend HEAD `e5fd48d` — 라우트 보호 전무 (SEC-D12)

| 항목 | workspace HEAD | TSR `d5654c0` |
|------|----------------|---------------|
| `ProtectedRoute` | ✗ 없음 | ✓ |
| `AuthContext` / JWT | ✗ 없음 | ✓ 메모리 세션 |
| `/platform`·`/settings`·`/dashboard/hq` | **무방비 공개** | 역할 allow |
| `npm audit` dev | **2 moderate**(esbuild/vite) | 0건(SEC-008) |
| `npm audit` prod | 0건 | 0건 |

`App.jsx:6-14` — 모든 대시보드·플랫폼·설정·보호자 경로가 인증 없이 렌더. 4차 SEC-D1(localStorage)보다 **심각** — 인증 계층 자체 부재 → `QA_FEEDBACK` **SEC-20260608-012 Open**.

### (D‴) SEC-D8·SEC-D9 workspace 관측

| ID | 4차 상태 | 5차 workspace |
|----|----------|---------------|
| SEC-D8 | Planned (develop WT J01 WIP) | **N/A** — `GuardianInvitation*` Java·`SecurityConfig` 변경 workspace 부재. V43 migration만 untracked |
| SEC-D9 | Planned (MaskedPhone FE-7) | **N/A** — `GuardianListCard`·Vitest workspace 부재 |

→ develop WIP checkout(`428ba7d`+dirty) 복원 후 SEC-D8/D9 재검증 필요. Planned 항목 **유지**.

### (E‴) 우선순위 재정렬 (5차)

| 순위 | ID | Severity | 조치 |
|------|-----|----------|------|
| P0 | SEC-D10 | **BLOCK** | `git -C src/backend checkout 428ba7d` · `git -C src/frontend checkout d5654c0` — workspace↔TSR 동기화 |
| P0 | SEC-D11 | **BLOCK** | checkout 동기화 또는 P0 패치 재적용(JWT·QR·DB·rate limit·`ProductionSecretValidator`·Boot 3.5.3) |
| P0 | SEC-D12 | **BLOCK** | 프론트 ProtectedRoute·AuthContext·실 JWT 연동 — 스켈레톤 배포 금지 |
| P1 | SEC-D4 | Medium | poi-ooxml 5.4.0+ |
| P1 | SEC-D8 | Medium | develop WIP checkout 후 J01 SecurityConfig 코드 리뷰(Planned) |
| P2 | SEC-D9 | Medium | develop WIP checkout 후 MaskedPhone FE-7(Planned) |
| P2 | SEC-D5 | Low | prod `format_sql`·management exposure |

---

## 1.8 일일 재점검 델타 (2026-06-08 6차) [SEC]

> 이번 호출에서 **workspace baseline**(`136239e`/`7170b2a`, WT CLEAN)과 **test 브랜치**(`2799e29`/`e5fd48d`)를 5차 stale checkout 대비 직접 대조.

### (A⁗) ✅ 해소 — workspace baseline 확정·5차 BLOCK 종결 (SEC-D10·D11·D12)

| ID | 5차 상태 | 6차 develop HEAD | 근거 |
|----|----------|------------------|------|
| SEC-D10 | BLOCK — `2799e29`/`e5fd48d` stale | **Fixed** | `.agents/workspace_baseline.yaml` · 실측 HEAD `136239e`/`7170b2a` · WT 0 dirty |
| SEC-D11 | BLOCK — P0 통제 부재 | **Partial Fixed** | `ProductionSecretValidator`·`ProductionSecretValidatorTest` PRESENT(`cf6116c`) · prod JWT/QR/PII/DB startup fail ✓ · **auth rate limit 부재**(SEC-D13) |
| SEC-D12 | BLOCK — 라우트 무방비 | **Fixed** | `ProtectedRoute.jsx`·`AuthContext.jsx`·`session.js` 메모리 JWT · `App.jsx` 전 운영 경로 래핑 · SEC-005 localStorage 0건(JWT) |

### (B⁗) ✅ 유지 — J01·PII·의존성 (4~5차 Fixed 항목 재확인)

| 항목 | 상태 | 근거 |
|------|------|------|
| SEC-D8 J01 accept | **Pass** | `SecurityConfig` POST `/api/v1/guardian/invitations/*/accept` 단일 permitAll · `InvitationTokenService` 128-bit·SHA-256 · `InvitationAcceptRateLimiter` |
| SEC-D9 MaskedPhone | **Pass** | `PhoneMaskingUtil.maskMobile` → `010-****-5678` · `GuardianInvitationService.applyGuardianPhone` masked 저장 |
| SEC-008 npm audit | **Fixed** | `npm audit` prod·dev **0건** — vite `^6.4.3`·vitest `^4.1.8`·esbuild override |
| v2/J03 Solapi relay | **Pass(dev)** | `SOLAPI_*` env 주입 · `SolapiAuthHeaders` HMAC · 로그에 API key/전화번호 미노출 · 미설정 시 fail-closed 반환 |
| Guardian phone PII | **Pass** | `V44__users_guardian_phone.sql` · `phone_encrypted` AES-GCM · `GuardianPhoneResolver` tenant 스코프 복호화 |

### (C⁗) 신규·잔존 이슈

| ID | 항목 | Severity | 상태 | 근거 |
|----|------|----------|------|------|
| SEC-D13 | **인증 API rate limiting 부재** | **High** | **Open** | `AuthService` rate limit 0건 · `AuthRateLimitService` grep 0건 · J01 accept만 `InvitationAcceptRateLimiter` → QA `SEC-20260608-014` |
| SEC-D14 | **develop→test 보안 패치 미승격** | **BLOCK** | **Open** | test backend `2799e29`(P0 전부 ABSENT) · test frontend `e5fd48d`(ProtectedRoute ABSENT) · develop 4·9 ahead → QA `SEC-20260608-013` |
| SEC-D4 | poi-ooxml **5.3.0** | Medium | Open | `pom.xml:60` — CVE-2025-31672 |
| SEC-D5 | prod `format_sql`·`management.info` | Low | Open | `application-prod.yml` 부재 · `application.yml` 기본 `format_sql:true`·`health,info` |
| SEC-D15 | Solapi prod credential startup 검증 없음 | Low | Monitor | `ProductionSecretValidator`에 SOLAPI 미포함 · 미설정 시 알림 실패만(데이터 유출 없음) |

### (D⁗) develop vs test 보안 격차 (SEC-D14 상세)

| 통제 | develop `136239e` | test `2799e29` |
|------|-------------------|----------------|
| `ProductionSecretValidator` | ✓ | ✗ |
| JWT prod 키 필수 | ✓ (prod profile) | ✗ ephemeral 폴백 |
| Guardian invitation + rate limit | ✓ | ✗ |
| `PhoneMaskingUtil` / V44 | ✓ | ✗ |
| Solapi provider | ✓ | ✗ |

| 통제 | develop `7170b2a` | test `e5fd48d` |
|------|-------------------|----------------|
| `ProtectedRoute` | ✓ | ✗ |
| AuthContext + 메모리 JWT | ✓ | ✗ |
| Must API pages + 7-role tests | ✓ | ✗ |
| npm audit 0 | ✓ | N/A (스켈레톤) |

### (E⁗) 우선순위 재정렬 (6차)

| 순위 | ID | Severity | 조치 |
|------|-----|----------|------|
| P0 | SEC-D14 | **BLOCK** | develop→test merge · TSR 승격 검증 · test 배포 금지 유지 |
| P1 | SEC-D13 | **High** | `AuthRateLimitService` — login·refresh·reset IP+email 슬라이딩 윈도우 |
| P1 | SEC-D4 | Medium | poi-ooxml 5.4.0+ |
| P2 | SEC-D5 | Low | `application-prod.yml` — `format_sql:false`·`management.exposure:health` |
| P2 | SEC-D15 | Low | Solapi prod credential validator (선택) |
| ✅ | SEC-D10·D12·D8·D9·SEC-008 | — | develop HEAD Fixed 확인 |

---

## 1.11 일일 재점검 델타 (2026-06-09 9차) [SEC]

> 이번 호출에서 **workspace 실측**(`git -C src/backend rev-parse HEAD/origin/test` · `git -C src/frontend …` · `git diff` · `npm audit` · `pom.xml`)을 8차 `2012945`/`f749311` 기준선과 대조. develop 양 스트림이 신규 기능 다수와 함께 전진했고 **WT가 DIRTY**(coder WIP)로 전환됨.

### (A⁂) 상태 변화 — develop 전진 + WT DIRTY + origin/test 불변

| 스트림 | 8차 develop | 9차 develop HEAD | local/origin test | WT |
|--------|-------------|------------------|-------------------|-----|
| backend | `2012945` | **`dd49204`**(+6: G21 visits·G7 NHIS 대기·G14 등급이력) | `598d108`(불변, P0 포함) | **DIRTY**(meals/programs API·V55·error handler) |
| frontend | `f749311` | **`ac5638e`**(+12: Epic V `/visits`·NHIS 대기 UI·보호자 식사·알림 이력) | `c7c8f07`(불변) | **DIRTY**(http.js·formErrors) |

→ **판정**: `origin/test`는 8차와 동일(P0 통제 전부 포함) — **배포 산출물 보안 회귀 없음**. develop↔test 격차는 **v1.2.1/v2 신규 기능 한정 merge 게이트**(보안 통제 누락 아님)이므로 **BLOCK 아님**(T-T5 Low 유지). develop WT DIRTY는 **커밋 전 TSR/merge 게이트**(SEC-D16 패턴) — 보안 검토는 WT 정적 분석 기준.

### (B⁂) ✅ 신규 기능 보안 검토 — 전부 RBAC·tenant-safe Pass

| 기능 (커밋) | 판정 | 근거 |
|-------------|------|------|
| Epic V 방문요양 `VisitController`/`VisitService` (G21, `d768820`·`1812165`·V53) | **Pass** | 7개 메서드 전부 `@PreAuthorize` 역할 스코프(list/get=4역할·create/update/confirm/cancel=BRANCH_ADMIN·SOCIAL_WORKER·check-in/out=SOCIAL_WORKER·CAREGIVER) · `requireOrganizationId`·`validateBranchWriteScope/ReadScope`·`requireHomeVisitBranch`(service_type 가드)·`requireClientInScope` |
| `LtcGradeHistoryService` 등급 변경 이력 (G14, `15e41e3`) | **Pass** | tenant `requireOrganizationId` + `validateBranchReadScope` · 페이지 크기 상한 100 · `changedBy` org 스코프 내 resolve · PII는 등급값만(RRN 무관) |
| NHIS PENDING_REVIEW 재조정 (G7, `4cc328d`·V54) | **Pass** | 상태 enum 추가만 · 신규 입력 파싱 표면 없음(POI 5.3.0 동일·SEC-D4 별개) |
| `MealController`/`ProgramController` (WIP) | **Pass (WT)** | 전 메서드 `@PreAuthorize`(읽기=4역할·쓰기=HQ/BRANCH_ADMIN) — HEAD ABSENT, 커밋 전 게이트 |
| `V55__visit_schedules_integrity_triggers.sql` (WIP) | **Pass — 무결성 강화** | 퇴소/비활성 이용자 INSERT 가드(V10 parity, org+branch 스코프) + session-actor backstop(created_by/confirmed_by/cancelled_by, V47 parity) — 감사 추적 강화 |
| `RoleBasedControllerAccessTest.java` (신규) | **긍정** | 역할별 컨트롤러 접근 회귀 테스트 추가 — A-2-5/H-3 커버리지 진전 |

### (C⁂) 신규·잔존 이슈

| ID | 항목 | Severity | 상태 | 근거 |
|----|------|----------|------|------|
| SEC-D19 | **WIP `GlobalExceptionHandler` 신규 핸들러 정보노출** | **Low** | **Monitor (WT)** | `HttpMessageNotReadable`·`InvalidDataAccessResourceUsage`·`DataAccessException`·`DataIntegrityViolation` 추가. **긍정**: 전부 `log.error`로 원인 서버측 기록·응답엔 **고정 한국어 메시지만**(raw `getMostSpecificCause()` 미echo, T-I2 유지). 잔여 caveat: ① `InvalidDataAccessResourceUsage`→503 "마이그레이션 필요" = 스키마 드리프트 노출(인증 사용자, Low) ② `DataIntegrityViolation`→"이미 사용 중인 이메일"(`uq_users_org_email_lower`) = **인증된 관리자 한정** 계정 열거 벡터(공개 가입 아님, Low). 커밋 전 raw detail echo 0건 재확인 게이트 |
| SEC-D17 | **프론트 raw `fetch()` JWT Bearer 누락** | Medium | **Open(부분 해소)** | 8차 지목 `OrganizationSettingsPage` → `apiFetch` **전환 완료** ✓. 잔여 ~14파일 raw `fetch()`(`SettingsPage` 비번변경·`PlatformPage`·`AuditLogPanel`·`LoginHistoryPanel`·`BackupSettingsPanel`·billing/guardian 페이지). 단 `PasswordResetRequestModal`·`GuardianCheckinPage`(QR scan)는 **공개 endpoint로 의도적 비인증**(정상) |
| SEC-D4 | poi-ooxml **5.3.0** | Medium | Open | `pom.xml:60` — CVE-2025-31672 미해소 |
| SEC-D5 | prod `format_sql`·`management.info` | Low | Open | `application-prod.yml` 부재 |
| SEC-D15 | Solapi prod credential startup 검증 없음 | Low | Monitor | `ProductionSecretValidator` SOLAPI 미포함 |
| SEC-D18 | v1.2.1/v2 develop→test merge 미실행 | Low | Monitor | develop 6+12 ahead · `origin/test` P0 포함(보안 회귀 없음) · develop WT clean 선행 후 TSR merge 게이트 |

### (D⁂) 우선순위 (9차)

| 순위 | ID | Severity | 조치 |
|------|-----|----------|------|
| P1 | SEC-D4 | Medium | poi-ooxml 5.4.0+ (NHIS import 회귀 테스트) |
| P1 | SEC-D17 | Medium | 잔여 ~14파일 raw fetch → `apiFetch`(공개 endpoint 제외) |
| P2 | SEC-D19 | Low | 커밋 전 error handler raw detail echo 0건 게이트(현재 안전) |
| P2 | SEC-D5 | Low | `application-prod.yml` `format_sql:false`·`management.exposure:health` |
| P2 | SEC-D18 | Low | develop WT 커밋 후 v1.2.1/v2 develop→test merge(TSR) |
| ✅ | Epic V·G14·G7·meals/programs·V55·SEC-008 | — | 9차 Pass/Fixed 확인 |

---

## 1.10 일일 재점검 델타 (2026-06-09 8차) [SEC]

> 이번 호출에서 **workspace 실측**(`git rev-parse HEAD` · `origin/test` · `npm audit`)을 7차 `598d108`/`c7c8f07` 기준선과 대조.

### (A⁕) ✅ 해소 — SEC-D14 `origin/test` 동기화 (SEC-20260608-015 Fixed)

| 스트림 | develop | local test | `origin/test` | 보안 상태 |
|--------|---------|------------|---------------|-----------|
| backend | **`2012945`** | **`598d108`**(1 behind) | **`598d108`** ✓ | P0 패치·rate limit·v2 copay·regions/V51/V52 ✓(develop) |
| frontend | **`f749311`** | **`c7c8f07`**(1 behind) | **`c7c8f07`** ✓ | ProtectedRoute·메모리 JWT·RBAC settings 분리 ✓(develop) |

→ **판정**: 7차 BLOCK(원격 STALE) **종결**. QA `SEC-20260608-015` Fixed. v1.2.1 커밋 2건은 develop-only — TSR merge 게이트(정상).

### (B⁕) ✅ 해소 — SEC-D16 V51/V52 WIP 커밋 (`2012945`)

| 항목 | 7차 | 8차 `2012945` | 근거 |
|------|-----|---------------|------|
| SEC-D16 regions·V51·V52 | Monitor(WT DIRTY) | **Fixed** | `RegionController` `@PreAuthorize(isAuthenticated())` read-only · V52 `payment_recorded_by` tenant FK+trigger(무결성 강화) · WT **CLEAN** |

### (C⁕) ✅ 신규 기능 보안 검토 — v1.2.1 @ `2012945`/`f749311`

| 항목 | 판정 | 근거 |
|------|------|------|
| `GET /api/v1/regions/*` | **Pass** | `@PreAuthorize(isAuthenticated())` · 참조 데이터(PII 없음) · 파라미터 바인딩 |
| V51 branch profile (service_type·region_dong) | **Pass** | `BranchService` tenant·branch scope · `BranchServiceType` enum sanitize |
| V52 billing payment actor FK | **Pass** | tenant-scoped FK · session-actor trigger — 감사 추적 강화 |
| `/settings` → sysadmin only | **Pass** | `sevenRoleRouteMatrix` · `sevenRoleRouteGuard.test.jsx` — platform_admin·hq_admin 거부 |
| `/organization/settings` → hq_admin | **Pass** | `OrganizationController` PATCH `@PreAuthorize(HQ_ADMIN)` · route guard 일치 |
| `OrganizationSettingsPage` API 호출 | **Medium** | raw `fetch()` — Bearer 미첨부(§SEC-D17) |

### (D⁕) 신규·잔존 이슈

| ID | 항목 | Severity | 상태 | 근거 |
|----|------|----------|------|------|
| SEC-D17 | **프론트 raw `fetch()` JWT Bearer 누락** | **Medium** | **Open** | `OrganizationSettingsPage`·`SettingsPage`·`PlatformPage` 등 15+ 파일이 `apiFetch`/`http.js` 미사용 → 서버 fail-closed(401)이나 설정·감사 UI prod 동작 불가·패턴 불일치 |
| SEC-D4 | poi-ooxml **5.3.0** | Medium | Open | `pom.xml:60` — CVE-2025-31672 |
| SEC-D5 | prod `format_sql`·`management.info` | Low | Open | `application-prod.yml` 부재 |
| SEC-D15 | Solapi prod credential startup 검증 없음 | Low | Monitor | `ProductionSecretValidator` SOLAPI 미포함 |
| SEC-D18 | v1.2.1 develop→test merge 미실행 | Low | Monitor | develop 1+1 ahead · `origin/test`는 이전 develop 동기화 — TSR merge 게이트 |

### (E⁕) 우선순위 (8차)

| 순위 | ID | Severity | 조치 |
|------|-----|----------|------|
| P1 | SEC-D17 | Medium | `OrganizationSettingsPage`·설정/플랫폼 페이지 → `apiFetch` 통일 |
| P1 | SEC-D4 | Medium | poi-ooxml 5.4.0+ |
| P2 | SEC-D5 | Low | `application-prod.yml` |
| P2 | SEC-D18 | Low | develop→test merge(v1.2.1) · TSR |
| ✅ | SEC-D14·D16·D13·D10·D12·D8·D9·SEC-008 | — | 8차 Fixed/Pass 확인 |

---

## 1.9 일일 재점검 델타 (2026-06-08 7차) [SEC]

> 이번 호출에서 **workspace 실측**(`git -C src/backend rev-parse HEAD` · `git -C src/frontend rev-parse HEAD` · `origin/test` 대조 · `npm audit`)을 6차 `136239e`/`7170b2a` 기준선과 대조.

### (A‴‴) ✅ 해소 — SEC-D13 auth rate limit (SEC-20260608-014 Fixed)

| ID | 6차 상태 | 7차 develop `598d108` | 근거 |
|----|----------|------------------------|------|
| SEC-D13 | **Open (High)** | **Fixed** | `AuthRateLimitService`·`AuthRateLimitServiceTest` PRESENT · `AuthService` login·refresh·reset 4경로 연동 · `application.yml` `auth-*-rate-limit-*` 설정 |

→ A04-1·T-D1 **develop 기준 Pass**. QA `SEC-20260608-014` Fixed @ `8d42bdd` lineage 유지.

### (B‴‴) ⚠ 진전·잔존 — SEC-D14 develop→test (로컬 merge · origin STALE)

| 스트림 | develop | local test | `origin/test` | 보안 상태 |
|--------|---------|------------|---------------|-----------|
| backend | **`598d108`** | **`598d108`**(=develop) | **`2799e29`**(26 behind) | 로컬: P0 패치·rate limit·v2 copay·transport masking ✓ · **원격: P0 전부 ABSENT** |
| frontend | **`c7c8f07`** | **`c510f5c`**(22 ahead) | **`e5fd48d`**(50 behind) | develop: ProtectedRoute·메모리 JWT·마스킹 UI ✓ · test/origin: v1.2 이후 22~50커밋 미승격 |

→ **판정**: backend **로컬 merge 완료**(TSR 100차)이나 **`origin/test` push 미실행**(QA-B12) — operation·원격 CI·submodule 재clone 시 **검증 코드 ≠ 배포 산출물** 갭 **잔존**. QA `SEC-20260608-015` Open.

### (C‴‴) ✅ 신규 기능 보안 검토 — v2 copay payment @ `598d108`

| 항목 | 판정 | 근거 |
|------|------|------|
| `POST /billing/claims/{id}/payments` | **Pass** | `@PreAuthorize(HQ_ADMIN\|BRANCH_ADMIN)` · tenant·`validateBranchWriteScope` · CONFIRMED→PAID만 · 금액 일치 검증 · `payment_recorded_by` actor |
| `GET /billing/overdue` | **Pass** | 동일 RBAC·branch scope |
| `GET /guardian/clients/{id}/billing` | **Pass** | `validateGuardianClientAccess` — guardian↔client 링크 검증 |
| `GuardianBillingDetailModal` (US-J02) | **Pass** | 열람 전용·인쇄 스코프(`ds-statement-printing`) · API 경유 데이터만 표시 |
| v2 PAID 알림톡 dispatch | **Pass** | 기존 Solapi HMAC·consent·로그 PII 미노출 패턴 유지 |

### (D‴‴) WIP — backend dirty tree (SEC-D16 Monitor)

| 항목 | Severity | 상태 | 근거 |
|----|----------|------|------|
| SEC-D16 | Medium(pending) | **Monitor** | WT 11M+3U: `regions/`·`V51`(행정구역 마스터·branch profile)·`V52`(payment_recorded_by FK+trigger). `RegionController` `@PreAuthorize(isAuthenticated())` — 참조 데이터 read-only 양호. V52는 **보안 강화**(actor 무결성). **HEAD ABSENT** — 커밋 전 TSR·merge 게이트 |

### (E‴‴) 잔존·우선순위 (7차)

| 순위 | ID | Severity | 조치 |
|------|-----|----------|------|
| P0 | SEC-D14 | **BLOCK** | `git_merge_to_test.sh` → **`origin/test` push**(QA-B12) · frontend develop→test merge(22) |
| P1 | SEC-D4 | Medium | poi-ooxml 5.4.0+ |
| P2 | SEC-D5 | Low | `application-prod.yml` |
| P2 | SEC-D15 | Low | Solapi prod credential validator |
| P2 | SEC-D16 | Medium(pending) | V51/V52·regions WIP 커밋 전 RBAC·Flyway 검증 |
| ✅ | SEC-D13·D10·D12·D8·D9·SEC-008 | — | develop `598d108`/`c7c8f07` Fixed 확인 |

---

## 2. OWASP Top 10 점검

> **주**: 아래 표는 **develop HEAD `28860ae`/`50d330d`** 기준. **`origin/test`**(`598d108`/`ab4de83`)는 P0 통제 전부 포함(SEC-D14 Fixed) — develop 신규 기능 399+33 behind(보안 회귀 없음). 18차 변화: **SEC-D4 표면 2→3 파서**(G21 `RfidTransmissionExcelParser`) · **V152~V155** transport 무결성 긍정 · **G21 check-in guard** 강화 · **로컬 test merge 진전**(origin push 미실행) · SEC-D26·D22·D29·D25 유지.

### A01:2021 — Broken Access Control

| ID | 항목 | Severity | 상태 | 근거 |
|----|------|----------|------|------|
| A01-1 | 프론트 역할별 라우트 무방비 | **High** | **Mitigated (develop)** / Low (`origin/test`) | develop `f749311` — `/settings`=sysadmin · `/organization/settings`=hq_admin ✓ · `origin/test` `c7c8f07` 동일 lineage |
| A01-2 | `AuthController` 메서드 `@PreAuthorize` 부재 | Medium | Open | `authenticated()`만 의존 (`/me`, `/logout`, `/login-history`) |
| A01-3 | 테넌트 격리 앱 레이어 단독 | Medium | Accepted risk | PostgreSQL RLS 미적용; `JwtScopeResolver` + FK 트리거로 보완 |
| A01-4 | RRN reveal 권한 범위 | Medium | Monitor | `HQ_ADMIN`/`BRANCH_ADMIN`/`SOCIAL_WORKER` — 목적 코드 검증 없음 |
| A01-5 | QR 체크인 IDOR 방어 | — | **Pass** | `AttendanceService` 보호자·이용자 소유권 검증 |

### A02:2021 — Cryptographic Failures

| ID | 항목 | Severity | 상태 | 근거 |
|----|------|----------|------|------|
| A02-1 | JWT 키 미설정 시 ephemeral 생성 | **High** | **Mitigated (develop prod)** / Low (`origin/test`) | dev: ephemeral 폴백 · **prod**: `ProductionSecretValidator` ✓ · `origin/test` `598d108`: prod 가드 포함 |
| A02-2 | QR HMAC 시크릿 미설정 시 랜덤 | **High** | **Mitigated (develop prod)** / Low (`origin/test`) | dev: UUID 폴백 · prod: validator ✓ · `origin/test` `598d108`: prod 가드 포함 |
| A02-3 | QR `token_value` DB 평문 저장 | Medium | Open | `BranchQrTokenEntity` — DB 유출 시 즉시 악용 가능 |
| A02-4 | PII AES-GCM | — | **Pass** | `PiiCryptoService` — 키 없으면 fail-closed |
| A02-5 | Refresh·reset 토큰 해시 저장 | — | **Pass** | SHA-256 at rest |

### A03:2021 — Injection

| ID | 항목 | Severity | 상태 | 근거 |
|----|------|----------|------|------|
| A03-1 | SQL Injection | — | **Pass** | Native query·JPA·JdbcClient 모두 바인딩 파라미터 |
| A03-2 | XSS (프론트) | Low | Pass | `dangerouslySetInnerHTML` 미사용; React JSX 이스케이프 |
| A03-3 | Excel 악성 OOXML — **NHIS·은행입금·RFID(G21) 3 파서** | Medium | Open | POI 5.3.0 — CVE-2025-31672. `NhisExcelParser` + `BankDepositExcelParser` + **`RfidTransmissionExcelParser`**(SEC-D4 18차 표면 확대) |

### A04:2021 — Insecure Design

| ID | 항목 | Severity | 상태 | 근거 |
|----|------|----------|------|------|
| A04-1 | 인증 API 레이트 리밋 없음 | **High** | **Pass (develop)** / Low (`origin/test`) | `AuthRateLimitService` ✓ · `origin/test` `598d108` 포함 |
| A04-2 | 계정 잠금 정책 없음 | Medium | Open | 실패 기록만 (`login_history`), lockout 없음 |
| A04-3 | 비밀번호 재설정 토큰 60분 TTL | Low | Monitor | `password-reset-ttl-minutes: 60` |
| A04-4 | 멀티테넌트 SaaS 설계 | — | **Pass** | JWT claim 기반 org/branch 스코프 |

### A05:2021 — Security Misconfiguration

| ID | 항목 | Severity | 상태 | 근거 |
|----|------|----------|------|------|
| A05-1 | DB 기본 자격증명 `ogada/ogada` | **High** | **Mitigated (develop prod)** / Low (`origin/test`) | dev 기본값 잔존 · **prod**: validator ✓ · `origin/test` `598d108`: validator 포함 |
| A05-2 | CORS 명시 설정 없음 | Medium | Open | `SecurityConfig` — `Customizer.withDefaults()` |
| A05-3 | 보안 헤더 명시 설정 없음 | Medium | Open | HSTS·CSP·Referrer-Policy 미정의 |
| A05-4 | `hibernate.format_sql: true` | Low | Open | prod 로그에 SQL·PII 조건 노출 가능 |
| A05-5 | CSRF 비활성화 | Low | Accepted | Bearer JWT API — 쿠키 인증 도입 시 재검토 |
| A05-6 | 공개 health·JWKS | Low | Monitor | `/api/v1/health`, `/.well-known/jwks.json` |
| A05-7 | `scripts/dev-backend.env` 시크릿 비-gitignore | Low | **Mitigated (커밋 대기)** | SEC-D22 — `.gitignore` WT에 `*.env`/`scripts/*.env` 추가 → `git check-ignore` 통과 · `HEAD:.gitignore` 미반영(커밋 대기) · 현재 untracked·유출 없음 |
| A05-8 | PilotFixturePanel prod 빌드 노출 | — | **Fixed** | SEC-D23 — `isPilotFixtureEnabledByEnv()` `import.meta.env.DEV \|\| VITE_ENABLE_PILOT_FIXTURE` 게이트 커밋(`c89a82b`) · prod 빌드 미렌더 |

### A06:2021 — Vulnerable and Outdated Components

| ID | 항목 | Severity | 상태 | 근거 |
|----|------|----------|------|------|
| A06-1 | Spring Boot 3.3.1 | Medium | Open | `pom.xml:9` **3.3.1** — 패치 라인 업그레이드 검토(T-E3) |
| A06-2 | poi-ooxml 5.3.0 (NHIS·은행입금·RFID 3 파서) | Medium | Open | `pom.xml:64` — CVE-2025-31672 (SEC-D4 18차 3표면) |
| A06-3 | form-data dev (multipart) | High(dev) | **Open(dev·축소)** | npm audit dev **1 HIGH**(form-data GHSA-hmw2-7cc7-3qxx·SEC-D26 4→1). esbuild·vite·@vitejs/plugin-react **해소**. prod **0건**(SEC-008 Fixed) |
| A06-4 | 간편결제 stub provider prod 기본값 | Low | **Monitor** | `EasyPayConfig` `matchIfMissing=true` stub — SEC-D28 |

### A07:2021 — Identification and Authentication Failures

| ID | 항목 | Severity | 상태 | 근거 |
|----|------|----------|------|------|
| A07-1 | Access TTL 30분 | — | **Pass** | `JWT_ACCESS_TTL_SECONDS: 1800` |
| A07-2 | Refresh 7일 | Low | Monitor | 장기 세션 — 로그아웃·revoke로 보완 |
| A07-3 | 로그인 비밀번호 복잡도 미검증 | Low | Open | `LoginRequest` — `@NotBlank`만 |
| A07-4 | 프론트 실인증 미구현 | **High** | **Pass (develop)** / Low (`origin/test`) | develop `6c4c151` — `AuthContext`·`authApi`·`http.js` ✓ · `origin/test` `c7c8f07` 동일 |
| A07-5 | access·refresh JWT 저장 | **High** | **Pass (develop)** | `session.js` 메모리 전용(SEC-005) · `theme.js` localStorage는 테마만 |
| A07-6 | 설정·플랫폼 API raw fetch JWT 누락 | Medium | **Fixed (develop)** | SEC-D17 해소 — raw `fetch()`는 `src/api/http.js`(apiFetch 래퍼) 1곳뿐(10차 `rg` 실측). 설정·플랫폼·감사·billing/guardian 전부 `services.js`/`apiFetch` 경유 |

### A08:2021 — Software and Data Integrity Failures

| ID | 항목 | Severity | 상태 | 근거 |
|----|------|----------|------|------|
| A08-1 | 파일 업로드 magic-byte 검증 없음 | Medium | Open | Content-Type 화이트리스트만 — 사진·**직원 HR**·**보수교육 증명서**·급여계약서·등급이력(SEC-D25). 저장 키 UUID 서버 생성(traversal 차단) |
| A08-2 | xlsx 확장자만 검사 — NHIS·은행입금·G21 RFID | Medium | Open | `NhisImportService` · `BankDepositImportService` · **`VisitService.compareRfidTransmission`**(plan+rfid multipart·POI 5.3.0) |
| A08-3 | Flyway 마이그레이션 | — | **Pass** | `ddl-auto: validate` |

### A09:2021 — Security Logging and Monitoring Failures

| ID | 항목 | Severity | 상태 | 근거 |
|----|------|----------|------|------|
| A09-1 | 감사 로그·로그인 이력 | — | **Pass** | `audit_logs`, `login_history` |
| A09-2 | RRN reveal audit | — | **Pass** | `CLIENT_RRN_REVEALED` 이벤트 |
| A09-3 | 실시간 보안 알림·SIEM 연동 | Medium | Planned | 중앙 모니터링 미정의 |
| A09-4 | 백업 실패 `error_message` 노출 | Medium | Open | SYSADMIN API — 내부 경로 유출 가능 |
| A09-5 | DB 예외 핸들러 메시지 | Low | Pass(committed) | SEC-D19 Fixed — `GlobalExceptionHandler` 커밋됨 · DB 핸들러 raw cause 미echo(고정 메시지) · 스키마 드리프트·이메일 중복 힌트만(인증 한정·Low) |

### A10:2021 — Server-Side Request Forgery (SSRF)

| ID | 항목 | Severity | 상태 | 근거 |
|----|------|----------|------|------|
| A10-1 | 외부 URL fetch | — | **N/A** | 사용자 제어 URL 호출 패턴 미발견 |

---

## 3. 백엔드 상세 (Java Spring Boot)

### 3-1. 인증·인가

```
SecurityConfig → JWT Resource Server → TenantContextFilter → @PreAuthorize
```

- **강점**: RS256, 역할 claim → `ROLE_*`, refresh 회전, 비밀번호 reset 시 refresh 전량 revoke. **develop `63cb193`**: prod startup 검증·`AuthRateLimitService` · SecurityConfig 필터 순서(SEC-D24) · **G2/7-5·G-NURSING·G41·G17b·G21·J03** 전부 `@PreAuthorize`+V104~V117 트리거 · `RoleBasedControllerAccessTest` 회귀 보강
- **잔존**: `AuthController` `@PreAuthorize` 갭(A01-2)·SEC-D4 poi-ooxml(2 표면)·A06-1 Boot 3.3.1·SEC-D25/26 첨부 magic-byte·dev esbuild CVE·SEC-D28 easy-pay stub·v2/v1.3 develop→test 대형 merge 게이트(242+295)

### 3-2. PII·민감 데이터

| 데이터 | 저장 | API 응답 | 로그 |
|--------|------|----------|------|
| 주민등록번호 | AES-GCM (`resident_registration_no_encrypted`) | 마스킹 + reveal API | 미로깅 확인 |
| 전화·주소 | AES-GCM | `********` | 미로깅 확인 |
| 비밀번호 | bcrypt hash | 미반환 | 미로깅 확인 |

`docs/ops/DATA_RETENTION_POLICY.md` §2 분류와 구현 정합성 **양호**.

### 3-3. 파일 업로드

| 유형 | 제한 | 검증 갭 |
|------|------|---------|
| 이용자 사진 | 5MB, image/jpeg·png·webp | magic-byte·AV 스캔 없음 |
| NHIS Excel | 10MB, `.xlsx` | Content-Type·POI zip bomb 대응 부족 |
| 은행 입금 Excel | multipart limit | 신규(US-L01) — POI 5.3.0·magic-byte 미검증·zip bomb 대응 부족 |
| 급여계약서 첨부 | 10MB, pdf·png | SEC-D25 — Content-Type만·magic-byte 미검증 |
| 등급이력 첨부 | 10MB, 화이트리스트 | SEC-D25 — Content-Type만·magic-byte 미검증 |
| 직원 HR 파일 | 10MB, pdf·png·jpeg | 신규(US-R03·SEC-D25) — Content-Type만·magic-byte 미검증 · UUID 저장 키 |
| 보수교육 증명서 | 10MB, 화이트리스트 | 신규(US-S02·SEC-D25) — Content-Type만·magic-byte 미검증 · UUID 저장 키 |

### 3-4. 에러 처리

`GlobalExceptionHandler` — 미처리 예외는 `"요청 처리 중 오류가 발생했습니다."` + `traceId`. API_SPEC §0-3 준수.

---

## 4. 프론트엔드 상세 (React + Vite)

| 영역 | develop `962858b` | test `c7c8f07` / `origin/test` | 위험 |
|------|-------------------|--------------------------------|------|
| 라우트 가드 | `ProtectedRoute`·역할 allow · ~70 route ✓ | v2/v1.3 295커밋 미승격 | Low |
| 인증 | AuthContext·`authApi` JWT ✓ | 동일 lineage | Pass |
| 토큰 저장 | `session.js` 메모리(SEC-005) ✓ | SEC-005 0건 | Pass |
| API 호출 | **모든 페이지 `services.js`/`apiFetch`** ✓ · raw `fetch()`는 `http.js` 래퍼뿐(SEC-D17 Fixed) | N/A @ test | **Pass** |
| 에러 처리 | `http.js` `parseApiErrorPayload`·field 오류 표시 | N/A @ test | Pass |
| pilot 도구 | `PilotFixturePanel` `import.meta.env.DEV` 게이트(SEC-D23 Fixed) | N/A @ test | **Pass** |
| PII UI | transport·guardian billing·CMS(account_last4)·직원 lifecycle 마스킹/스코프 ✓ | develop-only delta | Pass |
| dev audit | prod **0건** · dev **3 HIGH**(SEC-D26) | prod 0건 | Low(dev) |

**판정**: develop HEAD **배포 가능**(SEC-D17·D23 Fixed). **`origin/test` P0 동기화 유지**(SEC-D14 Fixed) — v2/v1.3 대형 merge 후 재검증.

---

## 5. 의존성 취약점 스캔

### 5-1. 스캔 방법

| 도구 | 대상 | 결과 (2026-06-18 18차 실측) |
|------|------|------|
| `npm audit --omit=dev` (prod) | `src/frontend` @ `50d330d` | **0 vulnerabilities** ✓ |
| `npm audit` (dev 포함) | `src/frontend` @ `50d330d` | **1 HIGH**(form-data GHSA-hmw2-7cc7-3qxx — SEC-D26, dev-only) |
| `pom.xml` | `src/backend` @ `28860ae` | Spring Boot **3.3.1** · poi-ooxml **5.3.0**(NHIS·은행입금·RFID 3 파서) |
| `origin/test` | `598d108`/`ab4de83` | P0 패치 포함 · develop 399+33 ahead · origin push 미실행 |

> **권장**: CI에 `dependency-check-maven` + NVD API 키 또는 캐시 미러 구성. 로컬 재실행:  
> `mvn org.owasp:dependency-check-maven:check -DfailBuildOnCVSS=7`

### 5-2. Frontend — npm audit (2026-06-18, develop `50d330d`)

> **prod 0건**(18차 `npm audit --omit=dev` 실측) — SEC-008 Fixed 유지.  
> **dev 1 HIGH**(18차 `npm audit` 실측) — form-data GHSA-hmw2-7cc7-3qxx만 잔존. prod 빌드·런타임 무관.

### 5-3. Backend — 수동 CVE 매핑 (develop HEAD `28860ae`)

| 컴포넌트 | develop 버전 | test `6aeafe7` | 알려진 CVE | Fix |
|----------|--------------|----------------|------------|-----|
| spring-boot-starter-parent | **3.3.1** | 3.3.1 | 3.3.x CVE | Boot 패치 라인 업그레이드 |
| poi-ooxml | **5.3.0** | 5.3.0 | CVE-2025-31672 (**NHIS·은행입금·RFID 3 파서**) | **5.4.0+** |

> `pom.xml` 줄번호: Boot `version` line 9 · poi-ooxml line 64 (18차 실측).

---

## 6. 규정·정책 정합성

| 요구 | 구현 상태 | 갭 |
|------|-----------|-----|
| PIPA 최소 수집 | RRN 동의 후만 저장 (DB constraint) | 양호 |
| DATA_RETENTION purge | 인덱스·배치 설계 문서화 | 배치 구현 검증 필요 (TSR) |
| WCAG 2.1 AA | 프론트 미구현 | UXD 영역 |
| 감사 로그 3년 | `audit_retention_days` 설정 가능 | 양호 |

---

## 7. 권장 조치 (우선순위)

| P | 조치 | 담당 | 완료 기준 |
|---|------|------|-----------|
| P1 | poi-ooxml **5.4.0+** (SEC-D4) | COD | **NHIS + 은행입금 + RFID(G21)** 3 파서 회귀 테스트 |
| P1 | Spring Boot 3.3.x 최신 패치 라인 업그레이드 (A06-1) | COD | 전 모듈 `mvn test` 회귀 |
| P2 | form-data dev 패치 (SEC-D26 1 HIGH) | COD | `npm audit fix`(GHSA-hmw2-7cc7-3qxx) 또는 CI 네트워크 격리 |
| P2 | **parent repo `.gitignore` `*.env` 변경 커밋** (SEC-D22) | OPS/COD | `git show HEAD:.gitignore`에 `*.env`/`scripts/*.env` 포함 |
| P2 | 첨부 업로드 magic-byte 검증 (SEC-D25) | COD | HR·보수교육·사진·NHIS·은행입금·급여계약서·등급이력 공통 |
| P2 | **origin/test push** (SEC-D18) | COD/TSR/OPS | 로컬 test merge 완료 후 origin push(399 BE/33 FE unpushed) |
| P2 | prod 간편결제 실 PG provider (SEC-D28) | COD/OPS | prod `ogada.easy-pay.provider`≠stub·credential startup 검증 |
| P2 | prod `application-prod.yml` (SEC-D5) | COD | `format_sql:false`·`management.exposure:health`·health readiness 상세 마스킹(SEC-D30) |
| P2 | CORS allowlist·보안 헤더 | COD | SecurityConfig 통합 테스트 |
| P2 | Kakao Maps JS appkey 운영 도메인 제한 (SEC-D31) | COD/OPS | Kakao Dev Console 도메인 제한 설정 확인 |
| ✅ | G21 RFID·G15 signature·V152~V155·check-in guard·live-e2e·SEC-D17·D19·D23·D24·D14·SEC-008 prod | — | 18차 Pass/Fixed/Mitigated 확인 |

---

## 8. 재감사 일정

| 항목 | 주기 |
|------|------|
| OWASP 정적 점검 | 일 1회 (agents.yaml workflow) |
| dependency-check + npm audit | 주 1회 (CI) |
| 치명적 이슈 재점검 | `QA_FEEDBACK` Open → Fixed 후 |

---

*다음 갱신: poi-ooxml 상향(SEC-D4·3 파서)·Spring Boot 패치(A06-1)·form-data dev 패치(SEC-D26)·`.gitignore` `*.env` 커밋(SEC-D22)·첨부 magic-byte(SEC-D25)·origin/test push(399+33·SEC-D18) 또는 신규 src 변경 후*
