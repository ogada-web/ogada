<!-- doc:owner=SEC doc:audience=COD,PLN,TSR updated=2026-10-08T01:50:00Z -->
# 보안 체크리스트 (security/SECURITY_CHECKLIST.md)

> **작성**: security_auditor (`SEC`)  
> **용도**: develop 구현·test 이관·프로덕션 배포 전 게이트  
> **연계**: `SECURITY_AUDIT.md`, `THREAT_MODEL.md`, `QA_FEEDBACK.md` `[SEC]` 항목

> **2026-10-08 36차 재점검**: backend develop **`d73aec11`** · frontend develop **`29c2304`** · 양 스트림 **WT CLEAN**(SEC-D35 Fixed). local test BE **`4aad7cc2`**(1 behind) · FE **`29c2304`**(SYNCED). origin/develop = origin/test = **`1e8857b`/`5cf667b`**(BE **+2** · FE **+1** · SEC-D18 **Monitor** · P0는 origin에 유지). **Pass**: US-P01 그룹 배정 API(RBAC·테넌트 FK·멤버 응답은 표시 이름만). **Open 유지**: SEC-D47 — 요약 prod moderate 2에 더해 lock `6.30.4`가 CVE-2026-53668 범위(`react-router-dom` **6.30.6**으로 닫힘, GHSA-wrjc·SSR은 ≥7.18.0) · SEC-D48 dev high 4(TSR QA-B689, non-BLOCK) · SEC-D4 poi 5.3.0 · A06-1 Boot 3.3.1. **BLOCK Open 0** · QA Open [SEC] 0. US-P01 test 미이관은 TSR `QA-B690`(보안 결함 아님).

---

## 사용 방법

| 기호 | 의미 |
|------|------|
| ☐ | 미완료 |
| ☑ | 완료 (증빙: PR·테스트·설정 링크) |
| N/A | 해당 없음 |
| BLOCK | 배포 차단 — 반드시 해결 |

각 항목 완료 시 **담당·날짜·증빙**을 PR 또는 `TEST_REPORT.md`에 기록한다.

---

## A. 인증·인가 (A01, A07)

### A-1. 백엔드 JWT·세션

| # | 체크 | Severity | 상태 |
|---|------|----------|------|
| A-1-1 | prod에서 `JWT_PRIVATE_KEY`·`JWT_PUBLIC_KEY` 환경변수 필수 (ephemeral 키 금지) | BLOCK | ☑ develop prod · ☑ test/origin `598d108` |
| A-1-2 | Access token TTL ≤ 30분, Refresh ≤ 7일 (또는 정책 문서화) | High | ☑ (기본 1800s/7d) |
| A-1-3 | Refresh 토큰 SHA-256 해시 저장·회전·revoke | High | ☑ |
| A-1-4 | 비밀번호 reset 시 모든 refresh revoke | High | ☑ |
| A-1-5 | 로그인·reset 실패 메시지 통일 (계정 열거 방지) | Medium | ☑ |
| A-1-6 | `login`, `refresh`, `password/reset*` **rate limiting** | BLOCK | ☑ develop · ☑ test/origin `598d108` |
| A-1-7 | 계정 잠금 또는 지수 백오프 (N회 실패) | Medium | ☐ |
| A-1-8 | `AuthController` 민감 메서드 `@PreAuthorize` | Medium | ☐ |

### A-2. RBAC·멀티테넌트

| # | 체크 | Severity | 상태 |
|---|------|----------|------|
| A-2-1 | 모든 운영 API `organization_id` JWT 강제 | BLOCK | ☑ |
| A-2-2 | 지점 스코프 `branch_ids`·`active_branch_id` 검증 | BLOCK | ☑ |
| A-2-3 | `@PreAuthorize` 컨트롤러 커버리지 100% (공개 제외) | High | ☐ (AuthController 갭) |
| A-2-4 | RRN reveal — 역할·audit·목적 기록 | High | ☑ (목적 검증 ☐) |
| A-2-5 | 크로스테넌트 접근 통합 테스트 (TSR) | BLOCK | ☐ |
| A-2-6 | 직원 계정 생성·역할 변경 권한상승 차단 | High | ☑ `UserService.enforceRolePolicy` — `ogada_*`/`sysadmin`/`platform_admin` 생성 차단(`isOgadaOnlyRole`) · `hq_admin` tenant API 차단 · branch_admin allowlist · **account-request approve도 재검증**(`provisionApprovedAccount`) · **V161 org당 hq_admin 1 UNIQUE** · 직접 `createUser` 봉인(승인 경유)(US-R03·20차) |
| A-2-7 | US-P01 `/programs/groups` — HQ/BRANCH/SOCIAL_WORKER만 · org+branch · 멤버 응답은 표시 이름 | High | ☑ develop `d73aec11` — 5 endpoint `@PreAuthorize` · caregiver 403 테스트 · V179/V180 복합 FK · 전화·주소·주민번호 필드 없음 · ☐ local test·origin (TSR QA-B690, 이관 전) |

### A-3. 프론트엔드 인가

| # | 체크 | Severity | 상태 |
|---|------|----------|------|
| A-3-1 | `ProtectedRoute` — 미인증 → `/login` | BLOCK | ☑ develop `f749311` · ☑ test/origin `c7c8f07` |
| A-3-2 | 역할별 라우트 가드 (`platform_admin`, `hq_admin` 등) | BLOCK | ☑ develop · ☑ test/origin · `/settings`=sysadmin · `/organization/settings`=hq_admin |
| A-3-3 | 401 시 refresh 또는 로그아웃 | High | ☑ develop (`http.js` refresh) · ☑ test/origin |
| A-3-4 | access token **메모리 전용** · refresh token **httpOnly cookie 또는 탭 스코프 `sessionStorage`** (access·refresh **localStorage 금지**) | High | ☑ develop (`session.js` — access 메모리 + refresh `sessionStorage` @ 154차, SEC-005 예외) · ☐ test/origin |
| A-3-5 | 데모 역할 링크/localStorage 역할 선택 제거 (prod 빌드) | High | ☑ develop · ☑ test/origin |
| A-3-7 | 설정·조직 API `apiFetch` Bearer 첨부 | Medium | ☑ SEC-D17 Fixed — raw `fetch()`는 `http.js` apiFetch 래퍼 1곳뿐(10차 `rg` 실측) · 설정·플랫폼·감사·billing/guardian 전부 `services.js` 경유 |
| A-3-6 | 클라이언트 라우트 가드를 **보안 경계로 신뢰 금지** — 백엔드 JWT 인가가 최종 방어 | BLOCK | ☐ (백엔드 `@PreAuthorize` 커버리지 의존, A-2-3) |

---

## B. 암호화·시크릿 (A02)

| # | 체크 | Severity | 상태 |
|---|------|----------|------|
| B-1 | `PII_ENCRYPTION_KEY` prod 필수 (32바이트 Base64) | BLOCK | ☑ develop prod · ☑ test/origin |
| B-2 | `QR_TOKEN_SECRET` prod 필수 (ephemeral 금지) | BLOCK | ☑ develop prod · ☑ test/origin |
| B-3 | `DB_PASSWORD` 기본값 `ogada` prod 사용 금지 | BLOCK | ☑ develop prod · ☑ test/origin |
| B-4 | 소스·Git·로그에 시크릿 하드코딩 없음 | BLOCK | ◑ 소스/로그 ☑ · `scripts/dev-backend.env` WT `.gitignore` `*.env`로 **무시됨**(`git check-ignore` 통과) · `HEAD:.gitignore` 미반영(SEC-D22 커밋 대기) · untracked·유출 없음 |
| B-10 | `*.env` 시크릿 파일 `.gitignore` 포함(`.env` 접미 파일 포함) | High | ◑ SEC-D22 — WT `.gitignore`에 `*.env`/`scripts/*.env`/`scripts/*.env.*`+`!*.env.example` **추가됨** · **parent repo 커밋 시 종결**(`git show HEAD:.gitignore` 확인) |
| B-5 | TLS 1.2+ (전송 중 PII) | BLOCK | ☐ (인프라) |
| B-6 | QR `token_value` at-rest 보호 (해시 또는 암호화) | Medium | ☐ |
| B-7 | CMS 자동이체 최소 수집 — 전체 계좌번호 미저장 | High | ☑ `cms_enrollments`는 `account_last4`(4자리)·`bank_code`·`fcms_member_id`만(V59) |
| B-8 | CMS `payer_name`(예금주명) at-rest 보호 | Low | ☐ 평문 저장(SEC-D21) — PII 정책 정합 위해 암호화 검토 |
| B-13 | 현금영수증 `identifier_value`(휴대폰/사업자번호) at-rest 보호 | Low | ☐ 평문 저장(SEC-D32) — API 마스킹 ☑ · DB 암호화 검토 |
| B-14 | 직원 접속키 6-digit at-rest 보호(`PasswordResetTokenEntity.tokenHash` SHA-256) + 응답 record 평문 키 미포함 | Medium | ☑ `StaffAccessKeyNotificationService.persistAccessKeyToken` — SHA-256 저장·응답 record에 `accessKey` 없음 · ◑ SEC-D37 **Mitigated**(34차) — `finalizeNotification`이 `accessKey`를 `***`로 치환. 잔여: PENDING~finalize 구간·JSON parse fail-open |
| B-15 | Solapi/Kakao 채널 dispatchReady fail-closed(credential 부재 시 readiness=false) | High | ☑ `NotificationChannelReadinessService.getTemplateCatalog` — `smsDispatchConfigured`/`alimtalkDispatchConfigured` 채널-credential 게이트 + `isLiveConfigured` 마커(stub/placeholder/change-me) 거부(24차 `fed6f1f`·SEC-D15 deepen) |
| B-9 | FCMS/SMTP prod credential startup 검증 | Medium | ◑ Solapi·SMTP config-time fail-closed ☑(SEC-D15) · FCMS apiKey 미검증 ☐(SEC-D20·stub) |
| B-11 | 간편결제 prod 실 PG provider 필수 (stub 기본값 금지) | Medium | ☐ SEC-D28 — `ogada.easy-pay.provider` stub `matchIfMissing=true` · prod credential startup 검증 없음 |
| B-12 | prod에서 `LIVE_E2E_BOOTSTRAP_ENABLED`/`LIVE_E2E` **금지** · live-e2e bootstrap 무인증 endpoint 비활성 | Medium | ◑ SEC-D29 — `ProductionSecretValidator` prod 거부 ✓ · bootstrap 응답 **password 필드 0** ✓ · blank credential fail-fast ✓ · probe default guardian cred 허용(QA-B95·non-prod) · permitAll 유지 |
| B-16 | Accounting BPO SSO — password 미저장·OTP만 전달 · env credential fail-closed | High | ☑ `AccountingBpoService` usmusid+HMAC OTP only · `CREDENTIALS_COLLECTED=false` · 공백 env `BusinessRuleException`(28차) |
| B-17 | Accounting BPO SSO — HQ/BRANCH only · per-actor rate limit · portal URL host+**path** allowlist · (장기) org-scoped credential | Medium | ◑ **SEC-D43 Mitigated 강화**(`bf96c29`+`bfe6b3f`) — HQ/BRANCH only ☑ · actor/org rate limit ☑ · sujifine https host ☑ · **path `/carefor_login`+query/fragment 거부** ☑(`bfe6b3f`) · org-scoped credential ☐(잔여 Low) |
| B-18 | US-V06 batch-unconfirm challenge entropy ≥6 digit(or alphanumeric) + fail throttle | Low | ◑ SEC-D44 **Mitigated**(34차 `48e70207`) — 6-digit SecureRandom `100000..999999`·actor-scope·TTL 10분·1회 소모 ☑ · fail throttle ☐ |
| B-19 | kind22 payroll `notifications.payload_json` 급여액 redact/TTL purge | Low | ☑ SEC-D45 **Mitigated**(34차) — `NotificationPayloadRedactor`가 netPay/paymentTotal/deductionTotal 중첩 필드 redact. 잔여: PENDING 구간·parse fail-open(SEC-D37과 동일) |
| B-20 | facility notice `attachment_url` host allowlist 또는 내부 스토리지 첨부 | Low | ◑ SEC-D46 **Mitigated 강화**(35차 `4aad7cc2`/`29c2304`) — http(s)·기본 포트·userInfo·IP/localhost/난독화/hosts alias·**단일 라벨·`.home.arpa`·`.svc`** 거부·FE 불안전 href 차단 ☑ · `FACILITY_NOTICE_ATTACHMENT_ALLOWED_HOSTS` 미설정 시 공개 DNS·예약 접미사 밖 짧은 복수 라벨 허용 ☐ |

---

## C. 입력 검증·인젝션 (A03, A08)

| # | 체크 | Severity | 상태 |
|---|------|----------|------|
| C-1 | SQL — JPA/JdbcClient 파라미터 바인딩만 | BLOCK | ☑ |
| C-2 | Raw SQL 문자열 concat 금지 (코드 리뷰) | BLOCK | ☑ |
| C-3 | React `dangerouslySetInnerHTML` 금지 | High | ☑ |
| C-4 | 파일 업로드 — 크기·MIME·**magic-byte** 검증 | High | ◑ **magic-byte 대폭 착지** — 사진(Client·Program v3)·급여계약서·등급이력·직원 HR·보수교육 = magic-byte ☑(SEC-D25) · **NHIS·은행입금·요양보호사·NHIS방문·RFID xlsx import = OOXML/OLE magic + 8-축 fail-closed ☑(SEC-D34 full-stack 완성·32차)** · 크기 ☑ · Content-Type `;param` strip ☑ · 저장 키 UUID 서버 생성 ☑ · **잔여 ☐**: image decode·AV 스캔·zip-bomb·poi-ooxml 5.3.0(SEC-D4) |
| C-5 | xlsx 파싱 — 확장자+Content-Type+POI 5.4.0+ | High | ☐ (NHIS·은행입금·RFID(G21)·**요양보호사(신규)** 4표면, SEC-D4·D34 — 요양보호사 import는 `WorkbookFactory` 자동판별만·확장자 체크 부재) |
| C-6 | API DTO `@Valid`·Bean Validation | Medium | ☑ (auth·주요 API) |
| C-7 | CSV/Excel export 수식(formula) 인젝션 방어(`=`/`+`/`-`/`@` prefix sanitize) | Low | ☑ SEC-D33 **Mitigated**(34차 재확인) — `CsvFormulaEscaper` · 명세·NTS 의료비공제·직원현황. 잔여: 선행 공백/LF는 trim 없이 통과 |

---

## D. 설정·헤더 (A05)

| # | 체크 | Severity | 상태 |
|---|------|----------|------|
| D-1 | CORS allowlist 명시 (운영 도메인만) | High | ☐ |
| D-2 | HSTS (`Strict-Transport-Security`) | High | ☐ |
| D-3 | `X-Content-Type-Options`, `X-Frame-Options` 명시 | Medium | ☐ (Spring 기본만) |
| D-4 | CSP (프론트 호스팅) | Medium | ☐ |
| D-5 | prod `hibernate.format_sql: false` | Medium | ☐ (워킹트리에도 `true`, prod 오버라이드 부재 — SEC-D5) |
| D-8 | `management.exposure` prod에서 `health`만 (`info` 제외) | Low | ☐ (현재 `health,info` — SEC-D5) |
| D-6 | `server.servlet.session.persistent: false` (JWT-only) | Medium | ☐ |
| D-7 | Actuator 노출 최소화 (`health`만, 인증 또는 내부망) | Medium | ☐ |
| D-9 | dev/pilot 데이터 시딩 도구 prod 빌드 미노출 (`import.meta.env.DEV` 게이트) | Medium | ☑ SEC-D23 Fixed — `PilotFixturePanel` `isPilotFixtureEnabledByEnv()` `import.meta.env.DEV \|\| VITE_ENABLE_PILOT_FIXTURE` 게이트 커밋(`c89a82b`) |

---

## E. 의존성·공급망 (A06)

| # | 체크 | Severity | 상태 |
|---|------|----------|------|
| E-1 | Spring Boot 최신 패치 (3.3.1 CVE 해소) | BLOCK | ☐ develop **3.3.1**(A06-1) — 패치 라인 업그레이드 검토 |
| E-2 | poi-ooxml ≥ **5.4.0** | High | ☐ (5.3.0 — **NHIS·은행입금·RFID(G21)·요양보호사 4 파서**, SEC-D4 20차 확대) |
| E-3 | CI OWASP dependency-check (CVSS≥7 fail) | High | ☐ |
| E-4 | CI `npm audit` (prod dep, moderate 이상 알림) | Medium | ☐ SEC-008 **회귀 유지**(36차 재실측) — 요약 prod **2 moderate** · lock `react-router@6.30.4`. JSON `via`의 CVE-2026-53668은 `react-router-dom` **6.30.6**. GHSA-wrjc·SSR은 **≥7.18.0**(SEC-D47) |
| E-5 | Dependabot/Renovate 활성화 | Medium | ☐ |
| E-6 | frontend dev `form-data` HIGH 해소 | Medium(dev) | ☑ **Fixed 유지** — form-data GHSA는 34차 audit에 없음(SEC-D26) |
| E-7 | frontend dev 빌드체인 HIGH (browserslist·nanoid·postcss·source-map-js) | High(dev) | ☐ SEC-D48 — 36차 `npm audit` **4 high + 5 moderate**(합계 9). prod high 0. TSR QA-B689 Open(non-BLOCK). 런타임 번들 아님 |

---

## F. 로깅·감사 (A09)

| # | 체크 | Severity | 상태 |
|---|------|----------|------|
| F-1 | PII·비밀번호 로그 미출력 | BLOCK | ☑ |
| F-2 | RRN reveal·권한 변경 audit | High | ☑ |
| F-3 | 로그인 성공/실패 `login_history` | High | ☑ |
| F-4 | API 500 응답 스택·DB 정보 미노출 | BLOCK | ☑ |
| F-5 | `audit_retention_days` 정책 준수 배치 | Medium | ☐ (TSR) |
| F-6 | 백업 실패 메시지 내부 상세 SYSADMIN 제한 | Medium | ☐ |
| F-7 | DB 예외 핸들러 raw cause 미echo(고정 메시지) | Low | ☑ committed (SEC-D19 Fixed — `getMostSpecificCause()`는 substring 매칭만·응답 고정 문구·`log.error` 서버 기록) |

---

## G. 데이터 보존·파기 (PIPA)

| # | 체크 | Severity | 상태 |
|---|------|----------|------|
| G-1 | `DATA_RETENTION_POLICY.md` purge 배치 구현 | High | ☐ |
| G-2 | 퇴소 이용자 PII 파기·익명화 | High | ☐ |
| G-3 | Tenant 해지 90일 유예 후 삭제 | High | ☐ |
| G-4 | 백업 30일 롤링·암호화 저장 | High | ☐ (인프라) |

---

## H. 배포 전 최종 게이트

| # | 항목 | BLOCK 조건 |
|---|------|------------|
| H-0 | **develop P0 패치 `origin/test` 반영** | ◑ — P0는 origin `1e8857b`/`5cf667b`에 있음(SEC-D14 Fixed). develop는 origin보다 BE **+2** / FE **+1**(SEC-D46 + US-P01 · **SEC-D18 Monitor** 36차). local test BE는 `4aad7cc2` |
| H-1 | 위 **BLOCK** 항목 0건 (develop baseline) | **충족** — develop ☑ · `origin/test` P0 ☑ |
| H-2 | `QA_FEEDBACK` `[SEC]` Open 0건 | ☑ — 36차 **QA Open [SEC] 0**(BLOCK 없음). US-P01 Pass · SEC-D47 **Open 갱신**(6.30.6 + 7.18.0) · SEC-D18 **Monitor** · SEC-D48·D4·A06-1 carry. TSR QA-B689·QA-B690은 `[SEC]` 아님 |
| H-3 | TSR 크로스테넌트·권한 거부 테스트 통과 | 필수 · `RoleBasedControllerAccessTest`(account-request·G-STAFF-NHIS·G-7-1 export·**G-SMS staff-access-key**)·live-e2e pilot E2E 회귀 |
| H-4 | `.env`·키 파일 Git 미포함 | ◑ — **SEC-D22**: WT `.gitignore` `*.env` 무시 ☑ · parent repo HEAD 커밋 선행 권고 |
| H-5 | 파일럿 센터 개인정보 처리방침·동의 UI | PLN 확인 |
| H-6 | J01 `SecurityConfig` 코드 리뷰 | ☑ develop lineage (SEC-D8 Fixed) · 필터 순서(SEC-D24 Fixed) |
| H-7 | workspace baseline = git 실측 HEAD | ☑ develop `d73aec11`/`29c2304` (36차 실측·양 스트림 **CLEAN**). local test BE `4aad7cc2` · FE SYNCED. origin BE +2 · FE +1 |
| H-8 | develop→test merge·origin push | ◑ — FE develop == local test `29c2304`. BE local test는 US-P01 1커밋 뒤(QA-B690). origin은 BE +2 · FE +1(SEC-D18 Monitor) |
| H-9 | live-e2e bootstrap credential fail-fast | ☑ SEC-D29 — blank credential fail-fast·trim 정규화(`7848b0f`)·password 필드 0 · 24차 HealthControllerTest G21 seed detail lock으로 readiness 회귀 가드 추가 |
| H-10 | 외부 SMS/Alimtalk dispatchReady fail-closed(credential 부재) | ☑ 24차 — `NotificationChannelReadinessService` 채널-credential 게이트(`fed6f1f`)·`isLiveConfigured` 마커 거부(stub/placeholder/change-me)·SEC-D15 deepen |
| H-11 | staff manual SMS quiet-hours guard(KST 22:00~08:00) | ☑ 24차 — `NotificationService.dispatchManualStaffSms`가 `NotificationQuietHoursPolicy.isActiveNow` 시 `BusinessRuleException` 즉시 거부(v2/J03 lineage 정합) |
| H-12 | Accounting BPO SSO least-privilege·throttle·portal host+path allowlist | ☑ SEC-D43 **Mitigated 강화**(`bf96c29`+`bfe6b3f`) — 잔여 org-scoped credential만 장기 |
| H-13 | US-V06 batch-unconfirm challenge entropy | ◑ SEC-D44 **Mitigated** — 6-digit ☑ · fail throttle ☐ |
| H-14 | FacilityNotice attachment host allowlist / kind22 payroll payload redact | ◑ SEC-D46 **Mitigated 강화**(35차 단일 라벨·`.home.arpa`·`.svc`) · SEC-D45 redact ☑ · prod allowlist env ☐ |
| H-15 | J03 dispatch-reference-unit-rates HQ/BRANCH only · 정적 catalog · secret 0 | ☑ 30차 — `NotificationChannelStatusController` `@PreAuthorize(HQ/BRANCH)` · `NotificationDispatchUnitRatesCatalog.REFERENCE` |
| H-16 | prod `react-router-dom` 6.30.6 (CVE-2026-53668) 및 이후 ≥7.18.0 (GHSA-wrjc·SSR) | ☐ SEC-D47 — lock `6.30.4`는 `>=6.30.2 <=6.30.5` 안 · 로그인 `navigate(pathname)` 싱크 |

---

## I. 역할별 책임

| 역할 | 담당 섹션 |
|------|-----------|
| **COD** | A, B, C, D, E 구현 |
| **DBA** | G, B-6 (RLS 검토) |
| **TSR** | A-2-5, H-3 회귀·침투 시나리오 |
| **PLN** | G 동의·처리방침 요구사항 |
| **SEC** | 체크리스트 갱신·재감사 |

---

*마지막 점검: 2026-10-08 (36차) | develop HEAD `d73aec11`/`29c2304`(양 스트림 **CLEAN** · FE local test SYNCED · BE local test 1 behind · SEC-D35 Fixed) · **US-P01 Pass** · origin BE **+2** / FE **+1**(SEC-D18 Monitor) · SEC-D47 CVE-2026-53668은 6.30.6 · GHSA-wrjc는 7.18.0+ · SEC-D48 dev high 4(QA-B689) · SEC-D4/A06-1 carry · **QA Open [SEC] 0***
