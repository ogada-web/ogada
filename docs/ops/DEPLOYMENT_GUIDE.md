<!-- doc:owner=TWR doc:audience=PLN,COD updated=2026-06-23T19:00:00Z -->
# ogada 배포 가이드 (ops/DEPLOYMENT_GUIDE.md)

> **작성**: tech_writer 에이전트  
> **최초 작성일**: 2026-06-05  
> **최종 갱신**: 2026-06-23 (336차 TWR 자동 동기화 — **BE `c4e6bcb`/FE `426d63a`·V1–V175·111 route·90 page·모듈 KPI 78.79%·merge gate 719 carry·V175 leave-ledger integrity ✅**)  
> **상태**: 초안 (Draft)  
> **대상 독자**: **DevOps·인프라 담당**, **ogada 플랫폼 운영자** (`ogada_platform_admin` 협업), **고객 센터 IT** (`sysadmin` 협업)  
> **기준 문서**: `docs/planning/REQUIREMENTS.md` §1-4, §4, `docs/technical/API_SPEC.md`, `docs/ops/ADMIN_GUIDE.md`, `docs/ops/DATA_RETENTION_POLICY.md`  
> **기술 스택**: Java Spring Boot 3.x + React (Vite SPA) + PostgreSQL

---

## 1. 이 가이드에 대하여

### 1-1. 목적

ogada는 전국 주간보호센터·요양기관을 위한 **B2B SaaS 멀티테넌트** 웹 시스템입니다.  
이 문서는 **로컬 개발 환경 구성**, **스테이징·프로덕션 배포**, **데이터베이스 마이그레이션**, **보안 키 관리**, **백업·모니터링** 절차를 설명합니다.

### 1-2. 문서 범위

| 포함 | 제외 |
|------|------|
| Spring Boot 백엔드·React SPA·PostgreSQL 배포 | 현장 업무 조작 (→ `USER_MANUAL.md`) |
| 환경변수·시크릿·TLS·리버스 프록시 | Tenant 온보딩·RBAC 운영 (→ `ADMIN_GUIDE.md`) |
| Flyway DB 마이그레이션·백업·복구 | 식단·일정 등록 API·알림톡 live·공단 API 직접 연동 (후속) |
| 클라우드 벤더 무관 배포 패턴 (Docker 기준) | 특정 클라우드 벤더 단일 선택 (구현 단계에서 결정) |

### 1-3. 아키텍처 개요

```
[사용자 브라우저]
       │ HTTPS
       ▼
[리버스 프록시 / CDN]  ── 정적 파일 (React SPA dist/)
       │
       ├── /api/v1/*  ──► [Spring Boot 3.x] :8080
       │                      │
       │                      ├── JWT (RSA) + RBAC
       │                      ├── Flyway 마이그레이션
       │                      └── PII AES-GCM 암호화
       │
       └── /.well-known/jwks.json (JWT 공개키)
              │
              ▼
        [PostgreSQL 15+] :5432
              │
              └── 일 1회 백업 (30일 보관)
```

| 계층 | 기술 | 비고 |
|------|------|------|
| 프론트엔드 | React 18 + **Vite 6** SPA | 빌드 산출물 `src/frontend/dist/` |
| 백엔드 | Spring Boot **3.5.3**, Java **17** | REST API Base URL `/api/v1` |
| 데이터베이스 | PostgreSQL | `pgcrypto` 확장, Flyway V1–V175 |
| 인증 | JWT (RS256) + RBAC | access 30분, refresh 7일 |
| 멀티테넌트 | Organization → Branch | `organization_id` 강제 격리 |

> **구현 상태 (2026-06-23 develop HEAD `c4e6bcb` / frontend `426d63a` 기준 — 336차 baseline)**:
> - **백엔드**: Must API + **V1–V175** · **SYNCED @ `c4e6bcb`**. **V175 leave-ledger integrity ✅** (Q668) · **SOCIAL_WORKER users read RBAC ✅** (Q669) · **client address road-level masking ✅** (Q669) · **live-e2e `e2e*` tenant isolation ✅** (Q670) · …
> - **프론트엔드**: **111 route · 90 page** @ **`426d63a`** **SYNCED**. **`/staff/leave-ledger` ✅ full-stack + UXD-157 a11y** (Q667) · develop `npm test` **~2064 PASS** · **FE WT DIRTY** (uncommitted WIP)
> - **merge gate**: **719 carry** (FE **187** + BE **532** unpushed) · **cross-stream BLOCK(BE pending 1 · FE pending 3)** · **BE Test 1846** · **FE test ~2064 PASS**
> - **마이그레이션**: V43 … **V175** `staff_leave_ledger_entries` integrity (Q668) · **V174** per-event ledger (Q663) · **V173** `staff_annual_leave_yearly` integrity. Flyway 자동 실행. **V173 미적용 시 health `v173StaffAnnualLeaveYearlyIntegrityCheckReady=false`** · blocker **`v173-staff-annual-leave-yearly-constraint-missing`** (Q645). **V171 미적용 시 `v171-defense-in-depth-constraint-missing`** (Q625).
> - **프로덕션 주의**: Solapi·FCMS·SMTP·**PG(stub)** 미사용 시 **`NOTIFICATION_PROVIDER=stub`** · **`NOTIFICATION_EMAIL_PROVIDER=stub`** · **`FCMS_PROVIDER=stub`** 기본값 유지. §4-3·§4-6·§4-6-1·§4-8 참고.

### [TWR] 1-4. Must 기능 운영 검증용 API 스모크 목록

배포 직후 최소 검증으로 아래 API를 호출해 Must 운영 기능의 회귀를 빠르게 확인합니다.

| 영역 | 스모크 API | 기대 결과(요약) |
|------|-----------|-----------------|
| G17 기능회복훈련 | `GET /api/v1/programs/functional-recovery/compliance` | 200, 지표 필드(`plansRecordedCount`, `gapCount`) 반환 |
| G32 사례관리 | `GET /api/v1/case-management/compliance` | 200, `meetingsRecordedCount`, `reflectionGapCount` 반환 |
| G42 민원상담 | `GET /api/v1/staff/grievance-counselings/follow-up/compliance` | 200, `pendingFollowUpCount`·`followUpCompletionRate` 반환 |
| G21 방문요양 | `GET /api/v1/visits/confirm-readiness?from=YYYY-MM-DD&to=YYYY-MM-DD` | 200, `readyPlan`·`readyBilling`·`blockers[]` 반환 |
| G-STAFF-WORK-ATTENDANCE (Q612) | `GET /api/v1/staff/work-attendance?date=` | 200, `items[]` with `userName`·`status`·`checkInAt`·`checkInMethod` (`a6eb8b7`) |
| G-BILLING-DEPOSIT-ORDER-GUARD (Q614) | `POST /api/v1/billing/claims/{id}/payments` (이전 월 미납 존재 시) | **422**「이전 미납 청구(YYYY-MM) 입금 선행이 필요합니다.」 (`a6eb8b7`) |
| G-ATTENDANCE-STATS (Q615) | `GET /api/v1/attendance/stats/monthly?branchId=&from=YYYY-MM-01&to=YYYY-MM-last` | 200, `branches[].months[]` with `yearMonth`·`activeClientCount`·`attendanceRate` — **FE `/attendance/stats` ✅** (`dffd726`) |
| G-BILLING-REPORT-FILTER-PERSISTENCE (Q621·Q626) | `GET /api/v1/billing/reports/filters?month=2026-06&branchId=` | 200, `filters[]` 4-variant — **FE hydrate ✅** · autosave **safe non-blocking** (`99d03fa`) |
| V171 integrity readiness (Q625) | `GET /api/v1/system/health` | **`v171DefenseInDepthIntegrityCheckReady=true`** · blocker **`v171-defense-in-depth-constraint-missing`** 없음 |
| US-E03 QR (Q624) | `POST /api/v1/branches/{branchId}/qr` `{ "direction":"in", "expiresInMinutes":480 }` | 200, **`qrToken`** — FE **`/attendance/qr/generate`** PNG preview ✅ (`250619e`) |
| US-D03 client attendance (Q628) | `GET /api/v1/clients/{clientId}/attendance?from=2026-06-01&to=2026-06-30` | 200, **`clientId`·`items[]`** with `attendanceDate`·`status`·`checkInAt`·`checkOutAt` — FE **`/clients/:id` 출석 탭 ✅** (`d058e43`) |
| G30 monitoring items + legend (Q629) | `GET /api/v1/compliance/monitoring/items` | 200, **15 templates** with `itemCode`·`inspectionDirection` — FE **`/compliance/monitoring` G30-LEGEND legend ✅** (`fdc135b`, client-side cross-walk) |
| G34 workflow catalog (Q635) | UI **`/compliance/workflow-catalog`** | **200** SPA · **`EzcareWorkflowCatalogPanel`** 28-row table · **16 verbatim** StatCard (`9f110a5`, FE-only) |
| G2 CMS branch roster (Q637·Q638·Q662) | `GET /api/v1/billing/cms/enrollments?branchId=&status=ACTIVE` (no `clientId`) | 200, `[]` or items with **`clientName`**·`payerName`·`status` (`d361833`/`d0c0d12`) |
| G2 CMS status filter normalize (Q662) | `GET …/enrollments?branchId=&status= pending ` | 200, **`PENDING`** roster only · unsupported `status=EXPIRED` → **`422`** (`f1225b0`) |
| G2 CMS payment cross-link (Q638) | UI **`/billing/payments`** | **CMS 등록** 열 — ACTIVE Badge 또는 **미등록 deep link** (`df9ec6c`) |
| G-STAFF-ANNUAL-LEAVE (Q639·Q648·Q650·Q663) | `GET /api/v1/staff/annual-leaves/roster?year=2026&branchId=` | 200, `items[]` with **`displayName`·`monthlyUsage[]`·`remaining`** · **`surfaceKind=ANNUAL_LEAVE_USAGE_SNAPSHOT`** · **`relatedSurfaces[0].route=/staff/attendance`** · **`relatedSurfaces[1].route=/staff/leave-ledger`** · **`relatedSurfaces[1].availability=AVAILABLE`** (`bb9df48`) |
| G-STAFF-ANNUAL-LEAVE yearly (Q650) | `GET /api/v1/staff/annual-leaves/users/{userId}?year=2026` | 200, **`surfaceKind`·`relatedSurfaces[]`** roster와 동일 (`6ab3760`) · UI **`/staff/annual-leaves`** related surfaces panel ✅ (`0b0d7ba`) |
| G-STAFF-ANNUAL-LEAVE branch fallback (Q639) | `GET /api/v1/staff/annual-leaves/roster?year=2026` (no `branchId`) | 200, **`branchId`=JWT active branch** (`6b84bcd`) |
| G-STAFF-ANNUAL-LEAVE negative usage (Q639) | `PUT /api/v1/staff/annual-leaves/users/{userId}` with `monthlyUsage: [-0.5]` | **`422`「월별 사용일수는 0 이상이어야 합니다.」** (`a45745c`) |
| G-STAFF-ANNUAL-LEAVE decimal usage (Q641) | `PUT …/users/{userId}` with `monthlyUsage: [0.5, …]` | **`422`「월별 사용일수는 정수여야 합니다.」** (`f88e8b1`) |
| G-STAFF-ANNUAL-LEAVE overlong memo (Q642) | `PUT …/users/{userId}` with `memo` 31 chars | **`422`「비고는 30자 이하여야 합니다.」** (`6b35fb5`) |
| G-STAFF-ANNUAL-LEAVE save guard (Q639) | `PUT /api/v1/staff/annual-leaves/users/{userId}` (사용 합계 > 부여일) | **422**「월별 사용일 합계가 연차 총 부여일수를 초과할 수 없습니다.」 |
| G-STAFF-ANNUAL-LEAVE UI (Q639·Q643·Q646·Q647) | UI **`/staff/annual-leaves`** | roster table · **AppShell `<h1>`「직원 연차휴가」** · **`ds-help-text`/`ds-fieldset`** · **`branch_admin` 편집 Modal field errors** (`31ab1aa`/`085a85a`) |
| V173 annual leave integrity (Q645) | `GET /api/v1/health` | **`v173StaffAnnualLeaveYearlyIntegrityCheckReady=true`** · missing → **`v173-staff-annual-leave-yearly-constraint-missing`** (`8c5dd65`) |
| J03 Solapi placeholder readiness (Q644) | `GET /api/v1/notifications/channel-status` (placeholder `SOLAPI_*`) | **`liveAlimtalkDispatchReady=false`** · **`readinessBlockers`** includes **`MISSING_SOLAPI_CONFIG`** (`19ffa84`) |
| G-STAFF-WORK-ATTENDANCE API cross-link (Q653·Q663) | `GET /api/v1/staff/work-attendance?date=2026-06-21&branchId=` | 200, `items[]` · **`surfaceKind=DAILY_WORK_ATTENDANCE_ROSTER`** · **`relatedSurfaces[0].route=/staff/annual-leaves`** · **`relatedSurfaces[1].route=/staff/leave-ledger`** · **`relatedSurfaces[1].availability=AVAILABLE`** (`bb9df48`) |
| US-R01-c leave-ledger (Q663·Q666) | `GET /api/v1/staff/leave-ledger?year=2026&branchId=` | 200, **`surfaceKind=CANONICAL_LEAVE_LEDGER`** · **`items[]`** · **`relatedSurfaces[0].route=/staff/annual-leaves`** · **`relatedSurfaces[1].route=/staff/attendance`** · **FE `/staff/leave-ledger` ✅** (`8057c1e`) |
| US-R01-c leave-ledger CRUD (Q663) | `POST /api/v1/staff/leave-ledger/users/{userId}` | 200, **`leaveType`·`leaveDate`·`daysUsed`** · unsupported `leaveType` → **`422`** · `DELETE …/entries/{id}` → **204** |
| G-STAFF-WORK-ATTENDANCE UI cross-link (Q651·Q653) | UI **`/staff/attendance`** | **「출퇴근 관련 화면」** panel — API **`relatedSurfaces`** 기반 **「연차휴가 현황」→ `/staff/annual-leaves`** · **「연차·유급휴일 대장 (준비 중)」** (`95f55aa`) |
| G21 dashboard NHIS gap (Q594) | `GET /api/v1/dashboard/branch` · `GET /api/v1/dashboard/hq` | 200, **`nhisComparisonGapCount`** ≥ 0 (`0796821`) |
| G15 Kakao quota (Q595) | `GET /api/v1/transport/kakao-api-status` | 200, `restKeyConfigured`·`quotaUsage[]` (`580a86b` FE widget) |
| 청구 생성 가드 | `GET /api/v1/dashboard/branch` | 200, `claimGenerationGuardBlocked` 필드 반환 |
| 은행 입금 형식 (G-BANK-EXCEL-8) | `GET /api/v1/billing/imports/bank-deposits/formats` | 200, `formats[]` 8건 (KB·우리·NH·신한·하나·부산·대구·광주) |
| 은행 입금 preview (G-BANK-EXCEL-8) | `POST /api/v1/billing/imports/bank-deposits/preview` | 200, `rows[]`·`detectedFormatId` (multipart `branchId`+`file`) |
| 은행 입금 import (negative) | `POST …/bank-deposits` with `rowNumbers=[]` | **`422`「선택된 행이 없습니다.」** (Q576) |
| 공단 요양보호사 import | `POST /api/v1/staff/imports/nhis-caregivers/preview` | 200 또는 422, `rows[]`·`totalRows` (multipart `branchId`+`file`) |
| 공단 요양보호사 import (negative) | `POST …/nhis-caregivers` with `rowNumbers=[]` | **`422`「선택된 행이 없습니다.」** (Q576) |
| G-BILLING 입금 반월 (Q585) | `GET /api/v1/billing/reports/deposits?month=2026-06&period=FIRST_HALF` | 200, 반월 필터 집계 · **`appliedFilters.depositPeriod=FIRST_HALF`** (Q587) |
| G-BILLING 수납 이중기준 (Q585) | `GET /api/v1/billing/reports/receipts?month=2026-06&basis=CLAIM` | 200, 청구기준 집계 · **`appliedFilters.receiptBasis=CLAIM`** (Q587) |
| G-BILLING invalid month (Q586) | `GET …/deposits?month=2026-99` | **`422`「대상 월 형식이 올바르지 않습니다.」** (`375fb9d`) |
| G-BILLING invalid period enum (Q585) | `GET …/deposits?month=2026-06&period=MID_MONTH` | **`422`「period는 FULL, FIRST_HALF, SECOND_HALF만…」** |
| G-BILLING cross-variant guard (Q585) | `GET …/charges?month=2026-06&period=FIRST_HALF` | **`422`「period 필터는 입금대장(deposits)에서만…」** |
| G-BATHING copy-from-previous-month (Q598) | `POST /api/v1/care/bathing-schedules/copy-from-previous-month` body `{"targetYearMonth":"2026-06"}` | 200, **`createdCount`·`skippedCount`·`sourceYearMonth`** (`49a1721`) |
| G-BILLING-OVERDUE management records (Q602) | `GET /api/v1/billing/overdue/claims/{claimId}/management-records?clientId=` | 200, `items[]` (빈 배열 허용) |
| G-BILLING-OVERDUE adjustments (Q602) | `GET /api/v1/billing/overdue/claims/{claimId}/adjustments?clientId=` | 200, `items[]` audit trail |
| G-STAFF-DOCUMENT-REPOSITORY (Q604) | `GET /api/v1/staff/hr-files/users/{userId}/repository-progress` | 200, **`totalCount=21`** · **`slots[]`** · **`progressLabel`** · **`careforParityLabel`** (`b583c11`) |
| **G-ATTENDANCE-ROSTER-STATUS (Q609)** | `GET /api/v1/attendance?transportMode=all` | 200, **`items[]`** with **`clientName`·`status`·`usesTransport`** · pending **`id=null`** · **`status=null`** (`0c69060`) · FE **`/attendance`** **`fetchAttendanceApi` only** (`8383f8d`) |

---

## 2. 사전 요구사항

### 2-1. 소프트웨어

| 구성요소 | 최소 버전 | 용도 |
|----------|----------|------|
| JDK | **17** | Spring Boot 백엔드 빌드·실행 |
| Maven | 3.9+ | 백엔드 패키징 (`mvn package`) |
| Node.js | 20 LTS | 프론트엔드 빌드 |
| npm | 10+ | 의존성 설치·Vite 빌드 |
| PostgreSQL | **15+** | 운영 DB (dev/prod 동일 엔진) |
| Docker (선택) | 24+ | 컨테이너 배포 시 |
| OpenSSL (선택) | — | JWT RSA 키·시크릿 생성 |

### 2-2. 네트워크·포트 (기본값)

| 서비스 | 포트 | 경로 |
|--------|------|------|
| Spring Boot API | `8080` | `/api/v1/*`, `/actuator/health`, `/actuator/healthz`, `/actuator/health/liveness`, `/actuator/health/readiness`, `/actuator/livez`, `/actuator/readyz`, `/.well-known/jwks.json` |
| Vite 개발 서버 | `5173` | SPA (개발 전용) |
| PostgreSQL | `5432` | DB 연결 |

프로덕션에서는 **443(HTTPS) 단일 진입점**을 권장합니다. API와 SPA를 동일 도메인에서 서빙하면 CORS·쿠키 이슈를 줄일 수 있습니다.

### 2-3. 리소스 가이드 (초기·파일럿)

REQUIREMENTS §1-2 규모 가정 기준 **최소 권장**:

| 환경 | API 서버 | DB | 비고 |
|------|---------|-----|------|
| 로컬 개발 | 2 vCPU / 4 GB RAM | 1 vCPU / 2 GB RAM | 단일 인스턴스 |
| 파일럿 (2지점) | 2 vCPU / 4 GB RAM | 2 vCPU / 4 GB RAM | 동시 접속 ~20 |
| 1년차 (~50 Tenant) | 4 vCPU / 8 GB RAM × 2 | 4 vCPU / 16 GB RAM (HA) | 수평 확장 검토 |

---

## 3. 로컬 개발 환경

로컬·스테이징 **테스트 계정**(역할별 이메일·비밀번호·홈 경로)은 **[DEV_ACCOUNTS.md](./DEV_ACCOUNTS.md)** 를 참고하세요.  
Live E2E용 env 파일은 `scripts/dev-live-e2e.env.example` → `scripts/dev-live-e2e.env` (§3-7).

### 3-1. PostgreSQL 준비

```bash
# PostgreSQL 접속 후
CREATE DATABASE ogada;
CREATE USER ogada WITH ENCRYPTED PASSWORD 'ogada';
GRANT ALL PRIVILEGES ON DATABASE ogada TO ogada;

# ogada DB에 접속하여 (V1 마이그레이션에서 자동 실행되지만 수동 확인 시)
CREATE EXTENSION IF NOT EXISTS "pgcrypto";
```

기본 JDBC URL: `jdbc:postgresql://localhost:5432/ogada`

### 3-2. 보안 키 생성 (개발용)

프로덕션과 동일한 변수명을 사용하되, **개발·스테이징·프로덕션 키를 분리**합니다.

```bash
# PII 암호화 키 (AES-GCM, Base64, 32바이트 권장)
openssl rand -base64 32

# QR 토큰 서명 시크릿 (임의 문자열, 32바이트 이상 권장)
openssl rand -base64 32

# JWT RSA 키 쌍 (2048bit)
openssl genrsa -out jwt-private.pem 2048
openssl rsa -in jwt-private.pem -pubout -out jwt-public.pem
```

> **주의**: 키 미설정 시 `JwtKeyConfig`가 **임시(ephemeral) RSA 키**를 생성합니다. 재시작마다 기존 JWT가 무효화되므로 **개발 편의용**이며 프로덕션에서는 금지합니다.

### 3-3. 백엔드 환경변수 (개발)

`src/backend/` 디렉터리에서 아래 변수를 설정한 뒤 실행합니다.

| 변수 | 필수 (prod) | 기본값 | 설명 |
|------|:-----------:|--------|------|
| `DB_URL` | ✅ | `jdbc:postgresql://localhost:5432/ogada` | JDBC 연결 문자열 |
| `DB_USERNAME` | ✅ | `ogada` | DB 사용자 |
| `DB_PASSWORD` | ✅ | `ogada` | DB 비밀번호 |
| `SERVER_PORT` | — | `8080` | API 수신 포트 |
| `JWT_PRIVATE_KEY` | ✅ | (없음 → ephemeral) | RSA 개인키 PEM 전체 |
| `JWT_PUBLIC_KEY` | ✅ | (없음 → ephemeral) | RSA 공개키 PEM 전체 |
| `JWT_ISSUER` | ✅ | `http://localhost:8080` | JWT `iss` 클레임 |
| `JWT_ACCESS_TTL_SECONDS` | — | `1800` | access 토큰 TTL (30분) |
| `JWT_REFRESH_TTL_DAYS` | — | `7` | refresh 토큰 TTL |
| `PII_ENCRYPTION_KEY` | ✅ | (없음) | Base64 AES 키 (16/24/32바이트) |
| `QR_TOKEN_SECRET` | ✅ | (없음) | 지점 QR HMAC 서명 키 |
| `PASSWORD_RESET_TTL_MINUTES` | — | `60` | 비밀번호 재설정 토큰 TTL |
| `BACKUP_STORAGE_DIR` | — | `./data/backups` | Tenant 백업 manifest 저장 경로 |
| `BACKUP_SCHEDULER_ENABLED` | — | `true` | 일 1회 백업 스케줄러 on/off |
| `BACKUP_DAILY_CRON` | — | `0 0 2 * * *` | 백업 실행 cron (기본 02:00) |
| `CLIENT_PHOTOS_DIR` | — | `./data/client-photos` | 이용자 사진 업로드 경로 |
| `AUTH_LOGIN_IP_RATE_LIMIT_PER_MINUTE` | — | `30` | 로그인 IP당 분당 한도 |
| `AUTH_LOGIN_ACCOUNT_RATE_LIMIT_PER_MINUTE` | — | `10` | 로그인 계정당 분당 한도 |
| `AUTH_REFRESH_IP_RATE_LIMIT_PER_MINUTE` | — | `40` | refresh IP당 분당 한도 |
| `AUTH_REFRESH_TOKEN_RATE_LIMIT_PER_MINUTE` | — | `20` | refresh 토큰당 분당 한도 |
| `AUTH_PASSWORD_RESET_REQUEST_IP_RATE_LIMIT_PER_MINUTE` | — | `20` | 비밀번호 재설정 요청 IP 한도 |
| `AUTH_PASSWORD_RESET_REQUEST_ACCOUNT_RATE_LIMIT_PER_MINUTE` | — | `6` | 재설정 요청 계정당 한도 |
| `AUTH_PASSWORD_RESET_CONFIRM_IP_RATE_LIMIT_PER_MINUTE` | — | `20` | 재설정 확인 IP 한도 |
| `AUTH_PASSWORD_RESET_CONFIRM_TOKEN_RATE_LIMIT_PER_MINUTE` | — | `8` | 재설정 토큰당 한도 |
| `SPRING_PROFILES_ACTIVE` | prod 시 | — | `prod` 시 `ProductionSecretValidator` 필수 시크릿 검증 |
|| `NOTIFICATION_PROVIDER` | — | `stub` | 알림 중계 (v1.1): `stub` \| `solapi` |
|| `SOLAPI_API_KEY` | Solapi 시 | (없음) | Solapi 인증 API 키 (**`solapi` 시 필수**, `18ee9b6`) |
|| `SOLAPI_API_SECRET` | Solapi 시 | (없음) | Solapi 비밀 키 (**`solapi` 시 필수**) |
|| `SOLAPI_SENDER_ID` | Solapi 시 | (없음) | 발신 번호 (**`solapi` 시 필수**) |
|| `KAKAO_PF_ID` | Solapi 시 | (없음) | 카카오 비즈니스 채널 PF ID (**`solapi` 시 필수**, `18ee9b6`) |
|| `GUARDIAN_INVITATION_TOKEN_TTL_DAYS` | — | `7` | 보호자 초대 토큰 만료 기간 (V43) |
|| `GUARDIAN_NOTIFICATION_QUIET_HOURS_START` | — | `22` | 알림 조용한 시간 시작 (KST, 24h) |
|| `GUARDIAN_NOTIFICATION_QUIET_HOURS_END` | — | `8` | 알림 조용한 시간 종료 (KST, 24h) |
|| `FCMS_PROVIDER` | — | `stub` | CMS 자동이체 (v2 G2): `stub` \| live (후속) |
|| `FCMS_BASE_URL` | live FCMS 시 | `https://api.fcms.co.kr` | 효성 FCMS API 베이스 |
|| `FCMS_API_KEY` | live FCMS 시 | (없음) | FCMS API 키 |
|| `FCMS_MERCHANT_ID` | live FCMS 시 | (없음) | FCMS 가맹점 ID |
|| `NOTIFICATION_EMAIL_PROVIDER` | — | `stub` | email 채널: `stub` \| `smtp` (Q204) |
|| `NOTIFICATION_EMAIL_FROM` | smtp 시 | `no-reply@ogada.local` | 발신 From (유효 이메일 필수) |
|| `NOTIFICATION_EMAIL_REPLY_TO` | 선택 | (없음) | Reply-To (설정 시 유효 이메일) |
|| `SMTP_HOST` | smtp 시 | (없음) | SMTP 서버 호스트 |
|| `SMTP_PORT` | — | `587` | SMTP 포트 |
|| `SMTP_USERNAME` | smtp 시 | (없음) | SMTP 인증 사용자 |
|| `SMTP_PASSWORD` | smtp 시 | (없음) | SMTP 인증 비밀번호 |
|| `SMTP_AUTH` | — | `true` | SMTP AUTH 사용 |
|| `SMTP_STARTTLS_ENABLE` | — | `true` | STARTTLS |

환경변수 설정 예시:

```bash
export DB_URL="jdbc:postgresql://localhost:5432/ogada"
export DB_USERNAME="ogada"
export DB_PASSWORD="ogada"
export PII_ENCRYPTION_KEY="$(openssl rand -base64 32)"
export QR_TOKEN_SECRET="$(openssl rand -base64 32)"
export JWT_PRIVATE_KEY="$(cat jwt-private.pem)"
export JWT_PUBLIC_KEY="$(cat jwt-public.pem)"
export JWT_ISSUER="http://localhost:8080"
```

### 3-4. 백엔드 실행

```bash
cd src/backend
mvn spring-boot:run
```

| 확인 항목 | 명령·URL | 기대 결과 |
|----------|----------|----------|
| API 헬스 | `curl -s http://localhost:8080/api/v1/health \| jq` | `status: UP`, **`ready: true`**, `databaseStatus: UP` (HTTP **200**) |
| API 헬스 (DB down) | PostgreSQL 중지 후 동일 | `status: DEGRADED`, **`ready: false`**, HTTP **503** (`6bd16b9`) |
| Actuator | `curl http://localhost:8080/actuator/health` | `{"status":"UP"}` (DB down·probe exception 시 **503** + `DOWN`, `5d7be9f`/`3f32ae5` **`ActuatorHealthController`**) |
| Actuator liveness | `curl http://localhost:8080/actuator/health/liveness` | HTTP **200** · `{"status":"UP"}` — **DB probe 없음** (`911a1b9`, Q413) |
| Actuator liveness (livez) | `curl http://localhost:8080/actuator/livez` | **`/actuator/health/liveness`와 동일** (`c19206a`, Q413) |
| Actuator readiness | `curl http://localhost:8080/actuator/health/readiness` | **`/actuator/health`와 동일** — DB probe (`911a1b9`, Q413) |
| Actuator readiness (readyz) | `curl http://localhost:8080/actuator/readyz` | **`/actuator/health/readiness`와 동일** (`c19206a`, Q413) |
| Actuator readiness (healthz) | `curl http://localhost:8080/actuator/healthz` | **`/actuator/health`·`/readyz`와 동일** — DB probe (`2157df5`, Q413) |
| JWKS | `curl http://localhost:8080/.well-known/jwks.json` | RSA 공개키 JWK Set |
| Flyway | 애플리케이션 로그 | `V1`~`V42` 마이그레이션 성공 |

Flyway는 `spring.flyway.enabled=true`, `classpath:db/migration` 경로의 SQL을 **애플리케이션 기동 시 자동 적용**합니다. `spring.jpa.hibernate.ddl-auto=validate`이므로 스키마는 Flyway만 변경합니다.

#### [TWR] Must API 스모크 (G24b/G19/G41/7-5)

배포 직후 아래 2개 엔드포인트를 추가 확인하면 운영 누락을 조기에 탐지할 수 있습니다.

```bash
# G24b 연간 욕구사정 준수 집계 (권한 필요)
curl -sS -H "Authorization: Bearer <ACCESS_TOKEN>" \
  "http://localhost:8080/api/v1/clients/needs-assessments/compliance?fiscalYear=2026" | jq

# G19 통합재가 기관 탐색 안내 (권한 필요)
curl -sS -H "Authorization: Bearer <ACCESS_TOKEN>" \
  "http://localhost:8080/api/v1/branches/integrated-home/provider-discovery" | jq
```

기대 결과:
- G24b: `fiscalYear`, `gapCount`, `items[].missingG24bFields` 필드가 포함되어야 함
- G19: `providerSearchUrl`, `integratedHomeFilterParam`, `daytimeCareServiceCode` 필드가 포함되어야 함

추가 점검(운영 계정 권한 필요):

```bash
# G41 기관 교육일지 준수 집계
curl -sS -H "Authorization: Bearer <ACCESS_TOKEN>" \
  "http://localhost:8080/api/v1/staff/training-logs/compliance?referenceYear=2026" | jq

# 7-5 간편결제 상태 조회 (claimId 교체)
curl -sS -H "Authorization: Bearer <ACCESS_TOKEN>" \
  "http://localhost:8080/api/v1/billing/easy-pay/claims/<CLAIM_ID>/payment" | jq
```

- G41: `summary` 또는 `items`가 존재하고, training type별 준수 카운트가 반환되어야 함
- 7-5: `status`가 `PENDING`/`SUCCEEDED`/`FAILED` 중 하나로 반환되어야 함

### 3-5. 프론트엔드 실행

```bash
cd src/frontend
npm install
npm run dev
```

| 항목 | 값 |
|------|-----|
| 개발 URL | `http://localhost:5173` |
| 빌드 명령 | `npm run build` |
| 산출물 | `dist/` (정적 HTML·JS·CSS) |

프론트엔드 API Base URL은 `src/api/http.js`에서 **`VITE_API_BASE_URL`** 환경변수(빌드 시 주입) 또는 기본값 **`/api/v1`**(동일 오리진 상대 경로)을 사용합니다.

```bash
# 개발: 백엔드가 다른 포트일 때 (선택)
export VITE_API_BASE_URL="http://localhost:8080/api/v1"
npm run dev

# 프로덕션 빌드: API가 동일 도메인 /api/v1 이면 생략 가능
npm run build
```

로컬 개발 시 CORS·쿠키 이슈를 줄이려면 Vite 프록시를 추가할 수 있습니다 (`vite.config.js` — **저장소 미반영 시 수동 설정**):

```javascript
server: {
  port: 5173,
  proxy: {
    "/api": "http://localhost:8080",
    "/.well-known": "http://localhost:8080",
    "/actuator": "http://localhost:8080"
  }
}
```

프록시 사용 시 `VITE_API_BASE_URL`은 `/api/v1`(기본값)로 두면 됩니다.

### 3-6. 백엔드 테스트

```bash
cd src/backend
mvn test
```

CI 파이프라인에서도 동일 명령으로 단위·통합 테스트를 실행합니다.

| 항목 (2026-06-10 develop `0854fbd`) | 값 |
|--------------------------|-----|
| 테스트 클래스 | **~83 suites** |
| 테스트 건수 | **383 PASS** |
| G14 ltc-grade-history | **`LtcGradeHistoryServiceTest`** 4건 · **`ClientControllerRoutingTest`** |
| G21 visit schedules | **`VisitServiceTest`** 7건 · **`RoleBasedControllerAccessTest$VisitAccess`** 6건 · DAY_CARE guard |
| V51 region·branch profile | **`RegionLookupServiceTest`** · **`RegionControllerRoutingTest`** · **`RoleBasedControllerAccessTest`** regions RBAC · branch POST `serviceType`·`regionDongCode` |
| G7 NHIS pending review | **`NhisExcelParserTest`** 3-state pilot workbook · **`NhisFixtureExporter`** dev 샘플 · **`NhisReconciliationMatcherTest`** (Q181) |
| V52 payment actor | **`BillingServiceTest`** PAID `payment_recorded_by` trigger backstop |
| Client transport profile | **`ClientServiceTest`** — `usesTransport`·픽업 주소·연락처·`defaultPickupTime`·geocode 캐시 무효화 (Q166) |
| Pilot transport JWT | **`PilotChecklistJwtE2eTest`** — transport JWT 라우팅 (US-T01) |
| Transport pilot E2E | **`TransportPilotServiceFlowE2eTest`** — roster→create→confirm→caregiver read·DRAFT 거부 (US-T01~T03, Q168) |
| Transport RBAC | **`RoleBasedControllerAccessTest$TransportAccess`** 8건 — roster·create·get·unconfirm·list 역할 검증 (Q168) |
| v1.3-A transport | **`TransportServiceTest`** 8건 · **`TransportControllerRoutingTest`** PATCH·POST unconfirm · **`listRosterShouldMaskPickupAddressForNonHqRole`**(주소·연락처, `c7941e9`, Q169) · **`MustApiEndpointRoutingTest$TransportRouting`** (Q159·Q163·Q164) |
| J03 template variables | **`AlimtalkTemplateVariablesTest`** · Solapi `kakaoOptions.variables` 매핑 · **`incidentType` alias** (Q157) |
| J03 SMS fallback | **`AlimtalkFallbackTextTest`** · 한국어 relay 본문 · **`SolapiKakaoAlimtalkProviderTest`** fallback 검증 (Q158) |
| J03 notification history | `NotificationHistoryServiceTest` 5건 · `GET /guardian/notifications` · `GET /clients/{id}/notifications` (Q152) |
| J03 service flow E2E | **`J03AlimtalkServiceFlowE2eTest`** **8건** · **`J03EmailServiceFlowE2eTest`** — billing notify·copay payment email (Q204) |
| **US-L03 CMS (G2)** | **`CmsServiceTest`** · **`CmsCopayLifecycleE2eTest`** — enrollment→debit→PAID·`payment_method=CMS` · **cancel enrollment**·**duplicate active guard**·**cancelled history list** (`a34d0eb`·`72aff00`·`4a622ab`, Q299) · **branch roster fallback** (`d0c0d12`/`d3d4d2d`, Q638) · **FAILED response(422 아님)** (`838a7f6`, Q256) · **`CmsPilotServiceFlowE2eTest`** retry·cancel lifecycle·**roster e2e** (BNK-104·Q638) · **`CmsPage.test`** · **`CmsEnrollmentTable.test`** · **`PaymentPage.test`** (Q638) · **`StubFcmsClientTest`** · **`MustApiEndpointRoutingTest$CmsRouting`** · **`RoleBasedControllerAccessTest$CmsAccess`** (Q208) |
| **G21 batch-confirm (BNK-197~198·213, Q330·Q477·Q479·Q481·Q483·Q484·Q486·Q487)** | **`VisitServiceTest`** confirm-readiness·**per-kind ready/blockers** (`f26abb0`/`28860ae`/`5f710e3`)·**`getNhisComparisonShould*`** (`03a052a`)·**`getConfirmReadinessShouldExposeNhisComparisonSummary*`**·**informational NHIS blockers** (`4046046`)·ack gates·batch confirm · **`VisitPilotServiceFlowE2eTest`** (`39fa41a`) · **`VisitLiveApiRoutingE2eTest`** nhis-comparison routing (`b73e5f4`, Q488) · **`VisitControllerRoutingTest.confirmReadinessRouteShouldSerializeNhisComparisonSummary`** · **`RoleBasedControllerAccessTest$VisitAccess`** · **`MustApiEndpointRoutingTest$VisitRouting`** · **`VisitNhisComparisonPanel.test`**·**`visitNhisComparison.test`** (`797c529`, Q486) · **`VisitNhisComparisonDetail.test`** (`ad18606`, Q487) · **`VisitBatchConfirmPanel.test`** (**NHIS StatCard wire+drill-down**, `68a4e35`/`ad18606`·**StatCard split**, `f9ed97d`) · **`VisitsContextNav.test`**·**`visitScheduleNav.test`** (`3a27303`) · **`VisitsPage.test`** · **`visits.test`** (`570912e`) · **`VisitRfidDiffComparePanel.test`** (**no-diff alert**, `f232285`) · **`BillingStatementPrintPanel.test`** (**receipt a11y**, `265fc42`) · **`LiveE2eBootstrapServiceTest`** NHIS import seed (`b73e5f4`, Q488) · **`pilotPageFlows`** G21 E2E |
| **v1.3-A transport preview cache (Q553, FE `acc5933`)** | **`transportRunPreviewCache.test`** · **`kakaoMapGeocoder.test`** · **`transportRosterDispatch.test`** · **`TransportSuggestPanel.test`** · **`TransportRunNewPage.test`** · **`transportUtils.test`** |
| **v1.3-A Kakao API status+usage probe (Q554, BE `e2b764b`/FE `ba74bb5`)** | **`TransportKakaoApiStatusServiceTest`** · **`KakaoRestApiUsageTrackerTest`** · **`TransportSuggestServiceTest`**(route preview embed) · **`RoleBasedControllerAccessTest$TransportAccess`**(kakao-api-status) · **`KakaoDirectionsClientTest`**(probe) · FE **`TransportKakaoApiStatusPanel.test`** · **`transportRosterDispatch.test`**(hasRouteLegDurations) · **`KakaoTransportMap.test.jsx`** |
| **v1.3-B transport suggest (BNK-212~214, Q347)** | **`TransportControllerRoutingTest`** · **`RoleBasedControllerAccessTest$TransportAccess.suggestRuns*`** · **`MustApiEndpointRoutingTest$TransportRouting`** · FE **`TransportSuggestPanel.test`**·**`BranchTransportSettingsPanel.test`**·**`transportSuggestServices.test`** · **V120**·**V122** |
| **L03_M01 nursing service provision (BNK-215/217, Q348)** | **`NursingServiceRecordServiceTest`** — **date window relative to `toDate`** (`6b0238a`) · **`NursingServiceRecordPilotServiceFlowE2eTest`** · **`MustApiEndpointRoutingTest$NursingServiceRecordRouting`** · **`RoleBasedControllerAccessTest$NursingServiceRecordAccess`** · FE **`NursingServiceRecordPage.test`**·**`nursingServiceRecordLiveApi.e2e.test.js`** · **V123**·**V125** |
| **L03_M06 excretion/tube record (BNK-216/217, Q349)** | **`NursingExcretionTubeRecordServiceTest`** · **`NursingExcretionTubeRecordPilotServiceFlowE2eTest`** · **`MustApiEndpointRoutingTest$NursingExcretionTubeRecordRouting`** · FE **`NursingExcretionTubeRecordPage.test`**·**`nursingExcretionTubeLiveApi.e2e.test.js`** · **V124**·**V125** |
| **L03_M07/M09/M10 service reports (BNK-217, Q350)** | **`NursingServiceReportsPilotServiceFlowE2eTest`** (`a728f1b`) · **`NursingReportLiveApiRoutingE2eTest`** · FE **`NursingServiceReportsPage.test`**·**`nursingServiceReportsLiveApi.e2e.test.js`** (`b698871`) |
| **L03_M15 pressure ulcer provision report (BNK-217, Q351)** | **`PressureUlcerServiceTest.getProvisionReport*`** · **`NursingReportLiveApiRoutingE2eTest`** · FE **`PressureUlcerProvisionReportPanel.test`**·**`pressureUlcerLiveApi.e2e.test.js`** |
| **G-NURSING-PRESSURE-ULCER (BNK-203~204, Q336~Q339, US-O03)** | **`PressureUlcerServiceTest`** · **`PressureUlcerPilotServiceFlowE2eTest`** 4-step (`24a1c5c`) · **`MustApiEndpointRoutingTest$PressureUlcerRouting`** · **`RoleBasedControllerAccessTest$PressureUlcerAccess`** · FE **`PressureUlcerPage.test`**·**`pressureUlcerServices.test`**·**`PressureUlcerCohortReportPanel.test`** · **`pressureUlcerLiveApi.e2e.test.js`** (`LIVE_E2E=1`) · **`pilotPageFlows`** US-O03 · V114 |
| **L03_M11 integrated vital check (BNK-207, Q340~Q342)** | **`NursingVitalCheckServiceTest`** · **`NursingVitalCheckPilotServiceFlowE2eTest`** · **`MustApiEndpointRoutingTest$NursingVitalCheckRouting`** · **`RoleBasedControllerAccessTest$NursingVitalCheckAccess`** · FE **`NursingVitalCheckPage.test`**·**`nursingVitalCheckServices.test`**·**`NursingContextNav.test`** · **`nursingVitalCheckLiveApi.e2e.test.js`** (`LIVE_E2E=1`) · V115 |
| **L03_M14 weight management (BNK-207~209, Q343~Q344)** | **`NursingWeightRecordServiceTest`** · **`NursingWeightRecordPilotServiceFlowE2eTest`** · **`MustApiEndpointRoutingTest$NursingWeightRecordRouting`** · **`RoleBasedControllerAccessTest$NursingWeightRecordAccess`** · FE **`NursingWeightRecordPage.test`**·**`NursingWeightRecordForm.test`** · **future measure-date guard** · V116 |
| **L03_M13 oral care check (BNK-209, Q345)** | **`NursingOralCareCheckServiceTest`** · **`NursingOralCareCheckPilotServiceFlowE2eTest`** · **`MustApiEndpointRoutingTest$NursingOralCareCheckRouting`** · **`RoleBasedControllerAccessTest$NursingOralCareCheckAccess`** · FE **`NursingOralCareCheckPage.test`**·**`NursingOralCareCheckForm.test`**·**`nursingOralCareCheckLiveApi.e2e.test.js`** · **future check-date guard** · V118 |
| **L03_M04 emergency record (BNK-211, Q346)** | **`NursingEmergencyRecordServiceTest`** · **`NursingEmergencyRecordPilotServiceFlowE2eTest`** · **`MustApiEndpointRoutingTest$NursingEmergencyRecordRouting`** · **`RoleBasedControllerAccessTest$NursingEmergencyRecordAccess`** · FE **`NursingEmergencyRecordPage.test`**·**`NursingEmergencyRecordForm.test`**·**`nursingEmergencyRecordLiveApi.e2e.test.js`** · **injectable `Clock` future-date guard** · V119 |
| **G17b cognitive activity skip reason (BNK-198~203, Q333~Q335)** | **`ProgramServiceTest`** skipReason·ABSENT satisfaction guard (`3bd6a43`) · **`ProgramControllerRoutingTest`** · **`ProgramCompliancePilotServiceFlowE2eTest`** · **`ProgramParticipationForm.test`** · **`ProgramsPage.test`** · **`FunctionalRecoveryPage.test`** · **`pilotPageFlows`** G17b program+functional recovery E2E · V112–V113 |
| **G2/7-5 easy payment (BNK-189, Q326~Q328)** | **`EasyPayServiceTest`**(provider normalize·**stored provider QA-B93** `b45830d`·`41a6c23`) · **`EasyPayPilotServiceFlowE2eTest`** — CARD/KAKAO·retry·failed PG·**prior-month guard** · **`RoleBasedControllerAccessTest$EasyPayAccess`** · **`MustApiEndpointRoutingTest$EasyPayRouting`** · **`EasyPayPage.test`** · **`EasyPayPanel.test`** · **`easyPay.test`** · **`billingGuardianPlatformServices.test`** · **`pilotPageFlows`** 7-5 E2E · V108–V111 |
| **G-ONBOARD-SUPPORT branch onboarding (BNK-223, Q353, US-O05)** | **`BranchOnboardingSupportServiceTest`** — SLA due-date·OVERDUE·**openedOn guard QA-B94** (`43c4b08`) · **`BranchOnboardingSupportCatalogTest`** · FE **`BranchOnboardingSupportPanel.test`**·**`BranchesPage.test`** · **`branchOnboardingSupportLiveApi.e2e.test.js`** (`36264b5`, `LIVE_E2E=1`) · **V126**·**V127** |
| **L02_M02 intensive excretion observation (BNK-239, Q359)** | **`IntensiveExcretionObservationServiceTest`** · **`IntensiveExcretionObservationPilotServiceFlowE2eTest`** · **`MustApiEndpointRoutingTest$IntensiveExcretionObservationRouting`** · **`RoleBasedControllerAccessTest$IntensiveExcretionObservationAccess`** · FE **`IntensiveExcretionObservationPage.test`** · **`intensiveExcretionObservationLiveApi.e2e.test.js`** · **V130** |
| **L02_M07 body restraint record (BNK-241, Q361)** | **`MustApiEndpointRoutingTest$BodyRestraintRecordRouting`** · **`RoleBasedControllerAccessTest$BodyRestraintRecordAccess`** · FE **`BodyRestraintRecordPage.test`** · **`BodyRestraintRecordForm.test`** · **`bodyRestraintRecordLiveApi.e2e.test.js`** · **V131** · **V132 integrity** |
| **L02_M13 meal assistance record (BNK-248, Q366)** | **`MealAssistanceRecordServiceTest`** · **`MealAssistanceRecordPilotServiceFlowE2eTest`** · **`MealAssistanceRecordLiveApiRoutingE2eTest`** · FE **`MealAssistanceRecordPage.test`** · **`mealAssistanceRecordLiveApi.e2e.test.js`** · **V140** |
| **L02_M15 care service special notes (BNK-248, Q368)** | FE **`CareServiceSpecialNotesPage.test`** · **`careServiceSpecialNotesLiveApi.e2e.test.js`** · V134 **`special_notes`** |
| **L02_M04/M05 care reports (BNK-252, Q369)** | **`CareReportServiceTest`** · **`CareReportLiveApiRoutingE2eTest`** · **`RoleBasedControllerAccessTest$CareReportAccess`** · FE **`CareMealExcretionReportPage.test`** · **`BathHelpReportPage.test`** · **`pilotPageFlows`** · live E2E (`46971e1`) |
| **L02_M17 intensive excretion report (BNK-256, Q371)** | **`CareReportServiceTest.getIntensiveExcretionReport*`** · **`CareReportLiveApiRoutingE2eTest`** · FE **`IntensiveExcretionReportPage.test`** · **`intensiveExcretionReportLiveApi.e2e.test.js`** · **`pilotPageFlows`** (`fa20943`) |
| **L02_M06 position change report (BNK-256, Q372)** | **`CareReportServiceTest.getPositionChangeReport*`** · **`CareReportLiveApiRoutingE2eTest`** · FE **`PositionChangeReportPage.test`** · **`positionChangeReportLiveApi.e2e.test.js`** · US-O03 V114 backing |
| **L02_M11 patient service report (BNK-258, Q373)** | **`CareReportServiceTest.getPatientServiceReport*`** · **`CareReportLiveApiRoutingE2eTest`** · FE **`PatientServiceReportPage.test`** · **`patientServiceReportLiveApi.e2e.test.js`** · **`pilotPageFlows`** (`ff9c8c5`) |
| **L02_M12 service summary report (BNK-258, Q374)** | **`CareReportServiceTest.getServiceSummaryReport*`** · **`CareReportLiveApiRoutingE2eTest`** · FE **`ServiceSummaryReportPage.test`** · **`serviceSummaryReportLiveApi.e2e.test.js`** · **`pilotPageFlows`** |
| **L02_M16 meal preference survey (BNK-258, Q375)** | **`MealPreferenceSurveyServiceTest`** · **`MealPreferenceSurveyLiveApiRoutingE2eTest`** · **`RoleBasedControllerAccessTest$MealPreferenceSurveyAccess`** · FE **`MealPreferenceSurveyPage.test`** · **`mealPreferenceSurveyLiveApi.e2e.test.js`** |
| **G21 billing claim reflection (BNK-258, Q376)** | **`VisitServiceTest.resolveBillingClaimReflectionStatus*`** · **`VisitLiveApiRoutingE2eTest`** · **`VisitPilotServiceFlowE2eTest`** — **`billingClaimReflectionStatus`** in list response · FE **`VisitsPage.test`** G21 Badge assertions (`25ca88e`/`25291b3`) |
| **G21 RFID split-view (BNK-262, Q377)** | FE **`VisitsPage.test`** — split-view switch·PLAN/BILLING dual table load (`55fdbd0`) — **신규 BE test 없음** |
| **L02 care nav cross-links (BNK-262, Q378)** | FE **`careLeafParity.test`** · **`SideNav.test`** — L02_M14·L03_M09/M10 link exposure (`6759bf6`) |
| **L02 care-scoped nursing reports (BNK-273/280, Q386·Q389)** | **`CareReportServiceTest.getNursing*`** · **`CareReportLiveApiRoutingE2eTest`** nursing-* routing · **`CareNursingReportsPilotServiceFlowE2eTest`** (`2ba2761`) · **`RoleBasedControllerAccessTest$CareReportAccess`** · FE **`CareNursingServiceReportPage.test`** · **`careReportServices.test`** · **`pilotPageFlows.test`** (`002e3eb`/`58ee122`/`6b34d31`) |
| **G26/G24b monitoring basis labels (BNK-273, Q391)** | FE **`NeedsAssessmentStatusPage.test`** · **`BillingStatisticsReportPage.test`** — FAQ 21800/21810·G30 cross-ref lede (`d499130`) |
| **G7 year-coverage message surface (G7, Q392)** | FE **`FeeScheduleYearGuardBanner`**·**`NHISImportPage`** — backend `message` 우선 (`57114b8`) · **`BillingServiceTest.getFeeScheduleYearCoverage*`** · **`FeeScheduleYearCoverageTest`** |
| **Live E2E client seed conflict fallback (QA-B95, Q409, BE `c13800c`)** | **`LiveE2eBootstrapServiceTest`** — **`ensureClientWithFallback`** · reused dev DB **`LIVE-E2E-0001`** 충돌 시 기존 이용자 재사용 |
| **Live E2E guardian token reuse (QA-B95, Q409, FE `af4d7f8`)** | **`liveE2eHarness.test`** — staff bootstrap embedded **`guardianAccessToken`** 재사용 · **`bootstrap-guardian` 미호출** |
| **Live E2E staff bootstrap clientId (BNK-283·BNK-285, Q360·Q393, QA-B95)** | **`LiveE2eBootstrapServiceTest`** (+ client seed @ `d8d51a7`) · **`LiveE2eControllerTest`** · **`LiveE2eBootstrapLiveApiRoutingE2eTest`** (`440ed84`) — **`POST /bootstrap`** 응답 **`clientId`** · probe **`clientReady`/`seedClientId`** |
| **Live E2E bootstrap login fallback (QA-B95, Q360)** | FE **`liveE2eHarness.test`** (`ddd4489`) — bootstrap HTTP 오류 시 **`login-fallback-ok`** · **`liveGlobalSetup.js`** |
| **Pilot live page E2E stabilize (QA-B95, Q360)** | FE **`pilotLivePages.e2e.test.jsx`** (`6f2a4eb`) — **`AuthProvider` passthrough** · **118 passed / 0 unhandled errors** |
| **Live E2E guardian bootstrap deepen (BNK-283·BNK-285, Q393·Q394, QA-B95)** | **`LiveE2eBootstrapServiceTest`** (+ role-collision @ `7ac0a46` · legacy onboarding @ `b1a6aff`) · **`LiveE2eControllerTest`** · **`LiveE2eControllerRoutingTest`** — **`POST /bootstrap-guardian`** (`f5205e3`) · **`ClientEntityTest`** (V147 @ `22396e0`) · FE **`liveE2eHarness.test`** · **`guardianLiveApi.e2e.test.js`** (`4e99ae1`) |
| **Live API routing E2E harness (BNK-283, Q393)** | **`CareNursingReportsLiveApiRoutingE2eTest`** · **`BranchOnboardingSupportLiveApiRoutingE2eTest`** · **`StaffStatusReportLiveApiRoutingE2eTest`** (`ec142db`) |
| **Live E2E bootstrap HTTP 500 restore (QA-B95, Q360·Q389)** | **`GlobalExceptionHandlerTest`** · **`LiveE2eControllerRoutingTest`** — disabled bootstrap **`503`** (`304bb2a`/`f6f1756`) |
| **G21 split-view reflection summary+follow-up (BNK-273, Q387)** | FE **`VisitsPage.test`** — summary chip counts·follow-up list (`4c9103d`/`cb457b7`) |
| **G21 UNPAIRED null-pair (QA-B110, Q388)** | **`VisitServiceTest`** — missing paired entity → **`UNPAIRED`** (`e54a699`) |
| **Live E2E credential probe (Q360, QA-B96)** | **`LiveE2eControllerTest`**·**`HealthControllerTest`** — `credentialsConfigured` (`c5f1325`/`8a92179`) · FE **`liveE2eHarness.test`** placeholder guard (`7106106`·**`fffc2c1` access token deepen**, Q578) · **placeholder token bootstrap probing** (`82a542c`, Q578 deepen) · **auth blocker recovery** (`9105332`·`06c6bb5`·**`33e9e1a` snake_case normalize**, Q580) · **feature-scoped operation blocker filter** (`cb3fe3d`, Q580 deepen) · **stale token recovery** (`b60c622`, Q583) |
| **L02 report·G21 a11y (BNK-262, UXD)** | FE unit tests on **PatientServiceReportPage**·**IntensiveExcretionReportPage**·**PositionChangeReportPage**·**ServiceSummaryReportPage**·**VisitsPage** — caption·StatCard group·badge label (`25291b3`) |
| **v1.3-A Kakao map instance refactor (QA-B114, Q370·Q394·Q395, BNK-285)** | **`TransportRoutePreviewServiceTest`** · **`KakaoDirectionsClientTest`** · FE **`kakaoMapInstance.test`** · **`KakaoTransportMap.test.jsx`** · **`loadKakaoMapSdk`** integration (`5ebaade`) |
| **v1.3-A Kakao Maps JS SDK preview (QA-B113, Q370·Q394, BNK-285)** | **`TransportRoutePreviewServiceTest`** · **`KakaoDirectionsClientTest`** · FE **`KakaoTransportMap.test.jsx`** · **`loadKakaoMapSdk`** integration (`b000d92`) · a11y `1daeda7` |
| **Live E2E anonymous probe (SEC-D29, Q360)** | **`LiveE2eControllerTest`** (`221bde7`/`a25c9de`) — `organizationReady`·`branchReady`·`userReady`·`mappingReady` · FE **`liveE2eHarness.test.js`** · **`liveGlobalSetup.js`** (`4299914`/`3a14caf`) |
| **G30 phone consultation satisfaction (Q365, FAQ21841)** | BE **`MonitoringServiceTest`** · FE **`MonitoringSelfDiagnosisPage.test`** · **`monitoringCompliance.test`** · **V138** `satisfied` · **`monitoringLiveApi.e2e.test.js`** |
| **L02_M01 weekly care service provision (BNK-244, Q362)** | **`CareServiceWeeklyRecordServiceTest`** · **`CareServiceWeeklyRecordPilotServiceFlowE2eTest`** · **`MustApiEndpointRoutingTest$CareServiceWeeklyRecordRouting`** · FE **`CareServiceWeeklyRecordPage.test`** · **`careServiceWeeklyRecordLiveApi.e2e.test.js`** · **`pilotPageFlows`** · **V134** · **V135 integrity** · **a11y** (`15b09df`) |
| **L02_M03 bathing schedule (BNK-245, Q363)** | **`BathingScheduleServiceTest`** · **`BathingSchedulePilotServiceFlowE2eTest`** · **`BathingScheduleLiveApiRoutingE2eTest`** · FE **`BathingSchedulePage.test`** · **`bathingScheduleLiveApi.e2e.test.js`** · **V136** · **V137** · **V139** notes CHECK · **a11y** (`15b09df`) |
| **G-7-1-4CHANNEL billing statement dispatch (BNK-241, Q364)** | **`BillingStatementDispatchServiceTest`** · **`BillingStatementDispatchPilotServiceFlowE2eTest`** · **`MustApiEndpointRoutingTest$BillingStatementDispatchRouting`** · FE **`BillingStatementDispatchPanel.test`** · **`BillingDetailPage.test`** · **V133** · **V139** actor backstop · **a11y** (`15b09df`) |
| **G-7-1 billing statement Excel export (BNK-409, Q535)** | **`BillingStatementExportServiceTest`** · **`MustApiEndpointRoutingTest`** · **`RoleBasedControllerAccessTest`** · FE **`BillingStatementPrintPanel.test`** — **`GET …/statement-export?kind=`** (`e454d3b`/`58d6694`) |
| **G26 yearBasis+NTS batch CSV (BNK-407/408, Q534)** | **`MedicalExpenseDeductionYearBasisTest`** · **`BillingServiceTest.listMedicalExpenseDeductionReportShouldFilterByClaimYearBasis`** · **`G26StatisticsReportsLiveApiRoutingE2eTest`** · FE **`BillingStatisticsReportPage.test`** — **`yearBasis`**·**`exportMedicalExpenseDeductionReportCsvApi`** (`ceeaeb9`/`19ed7f3`) |
| **V139 billing/bathing integrity (BNK-248)** | Flyway **V139** — `dispatched_by` backstop · bathing cancelled/skipped notes CHECK (`e4c240f`) |
| **J03 notification readiness blockers (Q367, BNK-248)** | **`NotificationChannelReadinessServiceTest`** `readinessBlockers[]` (`de25b3e`) · **`NotificationChannelStatusPilotServiceFlowE2eTest`** |
| **Health readiness probe harden (Q360, QA-B96)** | **`LiveReadinessProbeTest`** — null profile·non-DataAccess safe fallback (`e4c240f`) |
| **Health liveness ping (Q360, QA-B96)** | **`HealthControllerTest`** — `GET /api/v1/health/ping` 200 without DB (`df14e15`) |
| **Health readiness probe (Q360, QA-B96)** | **`OgadaBackendApplicationTests`** — `ready=true` 200 · `ready=false` 503 (`6bd16b9`) · **`databaseStatusDetail`** (`SELECT_1_OK`/`SELECT_1_FAILED`) (`8b7e476`) · FE **`liveE2eHarness.test.js`** · **`liveGlobalSetup.js`** · **`liveBackendProbe.js`** (`5f17beb`/`10f32c4`) |
| **G19 provider discovery pilot E2E (BNK-236, Q357)** | **`IntegratedHomeProviderDiscoveryPilotServiceFlowE2eTest`** (`4aac676`) · FE **`integratedHomeProviderDiscoveryLiveApi.e2e.test.js`**·**`integratedHomeProviderDiscovery.test.js`** (`98102c3`) |
| **G19/G30/G39 a11y (Q357·Q320·Q358)** | FE **`IntegratedHomeProviderDiscoveryPanel.test.jsx`**·**`ProvisionResultDispatchPanel.test.jsx`**·**`MonitoringIntegratedChecklistPanel.test.jsx`** (`85bfb4a`) |
| **G39 care-provision record dispatch (BNK-234, Q358)** | **`CareProvisionRecordDispatchPilotServiceFlowE2eTest`** (`73df04d`) · FE **`ProvisionResultDispatchPanel.test`**·**`careProvisionRecordDispatchLiveApi.e2e.test.js`** (`4d1a4f2`/`85bfb4a`) |
| **G30 monitoring evidence window (BNK-234, Q320)** | **`MonitoringEvidenceWindowTest`** · **`MonitoringService`** checklist window fields (`73df04d`) · FE **`monitoringCompliance.test`**·**`MonitoringIntegratedChecklistPanel.test`** · **`monitoringLiveApi.e2e.test.js`** (`73094f9`) |
| **live E2E harness defaults (QA-B96)** | FE **`0122bfe`** — guardian credential guard · env auto-source from `scripts/dev-live-e2e.env` · **`b3bd0cc`** guardian bootstrap fallback · **`4e99ae1`** **`resolveGuardianClientId`** · **`ddd4489`** bootstrap failure **login fallback** · **`6f2a4eb`** pilot page stabilize — **staging `./scripts/run-live-e2e.sh` RUN 확인 권장** |
| **G24b annual needs assessment compliance + dashboard + status (BNK-226~231, Q355·Q356·Q357)** | **`ClientNeedsAssessmentServiceTest.getCompliance*`** · FE **`DashboardPage.test`** · **`NeedsAssessmentStatusPage.test`** (`b5af5fa`) · **`needsAssessmentComplianceLiveApi.e2e.test.js`** · fiscal-year 2000~2100 guard (`f4c8beb`) |
| **G19 integrated-home provider discovery (BNK-231~235, Q357)** | **`BranchServiceTest.getIntegratedHomeProviderDiscovery*`** · **`IntegratedHomeProviderDiscoveryLiveApiRoutingE2eTest`** (`41d8de5`/`8cb8789`) · FE **`IntegratedHomeProviderDiscoveryPanel.test`**·**`BranchesPage.test`** · **`branchLiveApi.e2e.test.js`** (`9afa30e`) |
| **G41 FAQ21808 training type enum (BNK-229, Q356)** | **`StaffTrainingLogServiceTest`** V129 28종 · **V129** migration · **P2**: FE `staffTrainingLogs.js` dropdown |
| **7-5 easy-pay kakao alias + live routing (BNK-230, Q328)** | **`EasyPayServiceTest`**(`kakao-pay`·`KAKAOPAY`·self-heal `3dd94e6`) · **`EasyPayLiveApiRoutingE2eTest`** (`1e21b20`) · FE **`easyPay.test`** claimId validation (`3a17543`) |
| **G21 visit schedule live API harness (BNK-231)** | FE **`visitScheduleLiveApi.e2e.test.js`** (`3cbe582`) |
| **G24b needs assessment 8-area + a11y (BNK-225, Q354)** | **`ClientNeedsAssessmentServiceTest.upsertAssessmentShouldPersistG24bExtendedFields`** · **`ClientLifecyclePilotServiceFlowE2eTest`** · FE **`needsAssessmentForm.test`**·**`ClientNeedsAssessmentForm.test`**·**`ClientNeedsAssessmentCompare.test`** (`8989bf4`) · **`clientLifecycleLiveApi.e2e.test.js`** · **V128** |
| **G41 training type Locale.ROOT (Q321)** | **`StaffTrainingLogServiceTest`** Turkish locale regression (`345c0cb`) |
| **L03 nursing report notes snake_case (Q350)** | FE **`NursingServiceReportsPage.test`** snake_case notes fallback (`c97706b`) |
| **G-NURSING consolidated live E2E (BNK-225)** | FE consolidated harness (`8eed216`) · **`NursingServiceReportsPage`** full-suite flake harden |
| **G19/G30/G14 compliance consolidated live E2E (BNK-225)** | FE **`complianceConsolidatedLiveApi.e2e.test.js`** (`fcabed0`, `LIVE_E2E=1`) |
| **J03 primary guardian dispatch** | **`NotificationServiceTest`** · **`J03PrimaryGuardianDispatchE2eTest`** — primary 우선·secondary fallback·1명 발송 (`555a19f`·`d86405c`, Q272) |
| **J03 guardian document manual quiet-hours (Q539)** | **`J03GuardianDocumentManualNotifyQuietHoursE2eTest`** · **`NotificationServiceTest.dispatchManualClientEventShouldRejectDuringQuietHours`** — care-provision·home-newsletter·elder-abuse 3종 (`71b2d32`/`7e4c07e`) |
| **Live E2E allow-default-credentials (Q542)** | **`LiveE2eControllerTest.probeShouldAllowDefaultCredentialsWhenFlagEnabled`** · **`HealthControllerTest`** — **`ogada.live-e2e.allow-default-credentials=true`** default · **`false` 시 Q490 blockers** (`beef81e`) |
| **Live E2E G21 not-applicable unsupported branch (Q541)** | **`LiveE2eBootstrapServiceTest.g21SeedStatusShouldBlockWhenBranchUsesUnsupportedServiceType`** — non-`HOME_VISIT`/non-`DAY_CARE` **`serviceType`** → **`notApplicable()`** · **`liveE2eOperationReady=true`** · health **`g21-seed=not-applicable`** (`091c372`) · **`HealthControllerTest.healthShouldNotBlockWhenG21SeedIsNotApplicable`**
| **US-R03 FAQ21823 contract clauses checklist+template (Q546)** | **`StaffEmploymentContractRenewalPanel.test`** · **`staffEmploymentContract.test`** — 5항 checklist·workflow·Modal template (`1b6d2b1`)
| **US-R03 FAQ21823 employment contract renewal list+dashboard (Q540)** | **`StaffEmploymentContractRenewalSummaryPanel.test`** · **`StaffPage.test`** · **`DashboardPage.test`** · **`staffEmploymentContractCompliance.test`** · **`dashboardSummary.test`** (`10585b9`/`f31c346`) |
| **US-R03 FAQ21823 employment contract renewal detail (Q540)** | **`StaffEmploymentContractRenewalPanel.test`** · **`staffEmploymentContract.test`** · **`StaffDetailPage.test`** · **`StaffLifecyclePanel.test`** — renewal due·retention·overdue·HR file shortcut (`f62402f`) |
| **Dashboard billing/NHIS snapshot (QA-B49)** | **`DashboardServiceTest`** — **`monthlyCapWarningCount`** on branch · HQ **`nhisUnmatchedCount`·`overdueCount`·`monthlyCapWarningCount`** aggregate (`15b3c7e`, Q282) |
| **G17/G32/G38/G39 dashboard compliance snapshot** | **`DashboardServiceTest`** — G17/G32/G38/G39 **count·met 필드** on **`GET /dashboard/branch`**·**`/dashboard/hq`** (`7ba18c1`·`70d76a4`, Q280) |
| **BNK-112 G38/G39 pilot E2E** | **`CarePlanProvisionCompliancePilotServiceFlowE2eTest`** — G38 branch-scoped compliance + G39 indicator-44 create/list/compliance/duplicate guard · **`PilotChecklistJwtE2eTest`** (`a9f8bda`) |
| **G39 provision result evaluation (BNK-107)** | **`ProvisionResultEvaluationServiceTest`** · **`MustApiEndpointRoutingTest$ProvisionResultRouting`** · **`RoleBasedControllerAccessTest$ProvisionResultAccess`** (`f082933`, V80/V81, Q276) |
| **G38 care-plan notification compliance (BNK-106)** | **`CarePlanNotificationComplianceServiceTest`** — branch-scoped query · **`MustApiEndpointRoutingTest`** · **`RoleBasedControllerAccessTest`** (`5fd35a6`·`03211e6`, Q277) |
| **G21 NHIS import file validation** | **`VisitServiceTest`** — reject text/plain · allow octet-stream · **allow ms-excel** · **parameterized Content-Type strip** · **uppercase/mixed casing** (`Application/VND.MS-EXCEL; charset=UTF-8`, `1817c36`) · empty file (`3c7b247`·`18e2b4c`·`e21c12f`·`3f444a1`, Q278·Q297) |
| **G37 grade history attachments (BNK-105)** | **`LtcGradeHistoryAttachmentServiceTest`** · **`LtcGradeHistoryAttachmentStorageServiceTest`** · **`LtcGradeHistoryServiceTest`** attachmentCount · **`MustApiEndpointRoutingTest`** attachment routes · **`RoleBasedControllerAccessTest$ClientAccess`** (`0325d95`, V78/V79, Q274) · FE **`benefitContractAttachmentLiveApi.e2e.test.js`** (`548f670`, `LIVE_E2E=1`, G14) |
| **G21 visit enum normalize** | **`VisitServiceTest`** — `scheduleKind`·`checkInMethod` trim+uppercase · **`VisitControllerRoutingTest`** (`225b104`·`e8de0eb`, Q275) |
| **BNK-103 program compliance pilot** | **`ProgramCompliancePilotServiceFlowE2eTest`** — G17 indicator27·G32 evaluationConductedMet · **`PilotChecklistJwtE2eTest`** G33 start-balance·visit routing |
| **G2 copayAmount null guard** | **`BillingServiceTest.recordCopayPaymentShouldRejectMissingCopayAmountOnClaim`** · **`updateClaimStatusShouldRejectPaidWhenCopayAmountMissing`** (`1af5b1f`·`923e610`, Q257) |
| **G26 medical expense exclusion** | **`BillingServiceTest.getMedicalExpenseDeductionShouldExcludeCmsAndEasyPayPayments`** — `CMS`·`EASY_PAY` 제외 (`970f547`, Q254) |
| **G26 branch billing reports (BNK-263, Q379·Q380)** | **`BillingServiceTest.listMedicalExpenseDeductionReport*`** · **`listCopayMonthlyStatistics*`** · **`MedicalExpenseDeductionReportLiveApiRoutingE2eTest`** · **`CopayMonthlyStatisticsReportLiveApiRoutingE2eTest`** · **`G26StatisticsReportsLiveApiRoutingE2eTest`** — dual-function harness·invalid year **`422`** (`92ae60b`) · **`G26StatisticsReportsPilotServiceFlowE2eTest`** — **3-function** service flow (`30f03e8`) · **`MustApiEndpointRoutingTest`** · **`RoleBasedControllerAccessTest`** (`903f462`/`6d10e0d`/`1840640`) |
| **Live E2E bootstrap prod security (SEC, Q384, BNK-272)** | **`ProductionSecretValidatorTest`** — prod live E2E flags **fail-fast** (`aa6816a`) · **`LiveE2eBootstrapServiceTest`** · **`LiveE2eControllerTest`** — bootstrap response **password 미포함** |
| **Live E2E credential gating (QA-B96, Q360)** | FE **`liveE2eHarness.test.js`** — non-empty creds configured · login probe validation (`64f6753`) |
| **L03 nursing service save test (QA-B108)** | FE **`NursingServiceRecordPage.test`** — full-suite flake fix (`43d308a`) |
| **L02 meal preference create test (QA-B109)** | FE **`MealPreferenceSurveyPage.test`** — create flow timing fix (`14d210c`) |
| **G26 ③ transport service fee statistics (BNK-269, Q382)** | **`TransportServiceFeeServiceTest`** · **`G26StatisticsReportsLiveApiRoutingE2eTest`** — **3-endpoint** harness (`3672bbe`) · **`MustApiEndpointRoutingTest`** · **`RoleBasedControllerAccessTest`** |
| **G26 statistics dashboard (FE, BNK-268·269)** | **`BillingStatisticsReportPage.test`** · **`g26StatisticsReports.test`** — **3 API** normalize·year validation (`09e4ec1`/`d8f1fdf`/`31544cf`) |
| **L02 care report RBAC (BNK-270, Q383)** | **`RoleBasedControllerAccessTest$CareReportAccess`** — **`caregiver` 403** on **`GET /care/reports/*`** (`2495753`) |
| **G26 NTS xlsx export (FE)** | **`medicalExpenseDeduction.test`** — `buildMedicalExpenseDeductionXlsx`·NTS rows·filename (`e2c2ffe`·`fd569d7`, Q258) |
| **US-L04 medical expense UX (FE)** | **`MedicalExpenseDeductionPanel.test`** — invalid year no fetch·submit fetch·CMS exclusion guidance·xlsx download (`13272bc`·`c1d9788`·`e2c2ffe`, Q255·Q254·Q258) |
| **US-L01 payment guard** | **`BillingServiceTest.recordCopayPaymentShouldRejectNonPositiveAmount`** · **`notifyClaimGuardiansShouldDeduplicateDuplicateClientLineItems`** (Q218·Q219, `4109680`·`40567a2`) |
| **US-M03 claim basis·guard** | **`BillingSettingsServiceTest`** 2건 · **`BillingServiceTest`** generation-guard·prior-month reject·NHIS_IMPORT path (`857bd32`·`b953662`, Q224·Q225) |
| **BNK-47·51 monthly cap guard** | **`MonthlyBenefitCapCatalogTest`** · **`BillingServiceTest`** cap exceed·**`COGNITIVE_SUPPORT`** (`a92e625`·`20bc1be`, Q226·Q228) |
| **BNK-48 bank deposit import** | **`BankDepositExcelParserTest`** · **`BankDepositImportServiceTest`** · **`BankDepositCopayLifecycleE2eTest`** — match·month disambiguation·ambiguous skip (`e50533f`·`95bb34d`·`467cd70`, Q227) |
| **BNK-49 FE monthly cap·bank UI** | **`MonthlyBenefitCapGuardPanel.test`** · **`MonthlyBenefitCapBanner.test`** · **`BankDepositImportPanel.test`** · **`BankDepositImportPanel.formats.e2e.test`** — 8-bank xlsx upload (`758e590`, Q258) |
| **US-G04 fee schedule year guard** | **`FeeScheduleYearCoverageTest`** · **`NhisImportServiceTest`** — 25칸 미완비 import 거부 (`970c7af`, Q260) |
| **US-G04·US-L01 FE guard·sample** | **`FeeScheduleYearGuardBanner.test`** · **`NHISImportPage.test`** · **`bankDepositFormats.test`** — upload block·sample xlsx (`5c0d83d`·`b9845ac`, Q260·Q258) |
| **G2 SMTP startup guard** | **`NotificationConfigTest`** — `NOTIFICATION_EMAIL_PROVIDER=smtp` 시 **`SMTP_HOST`/`SMTP_PORT` 누락 기동 실패** (`5fc44ec`) |
| **G11 surcharge catalog·auto-apply** | **`FeeSurchargeRateCatalogTest`** · **`BillingServiceTest`** preview·**attendance generate surcharge** · **`MustApiEndpointRoutingTest`** · **`RoleBasedControllerAccessTest`** (`904072b`·`d7475fd`, Q229) |
| **US-V01 paired billing E2E** | **`VisitPilotServiceFlowE2eTest`** — NHIS plan import `createPairedBillingSchedule=true` (`3d8370a`) |
| **G11 FE preview·claim note** | **`FeeSurchargeGuidePanel.test`** · **`ClaimGenerationPanel.test`** guard API fail block · **`pilotPageFlows`** (`f987b9d`·`60dc5d0`, Q229·Q225) |
| **Solapi startup guard** | **`NotificationConfigTest`** — `NOTIFICATION_PROVIDER=solapi` 시 **`SOLAPI_API_KEY`·`SOLAPI_API_SECRET`·`SOLAPI_SENDER_ID`·`KAKAO_PF_ID` 누락 기동 실패** (`18ee9b6`) · **`KAKAO_TPL_*` placeholder(내부 코드명 그대로) 기동 실패** (`98e40a3`, Q266) |
| **G11·G15·bank FE E2E** | **`pilotPageFlows`** — `FeeSurchargeGuidePanel`·`TransportCompliancePanel`·`BankDepositImportPanel` (`4679f15`) |
| **G15 transport contract** | **`TransportContractServiceTest`** · **`TransportControllerRoutingTest`** GET/PUT · **`RoleBasedControllerAccessTest$TransportAccess`** · **`TransportCompliancePanel.test`** (`3c8f9fe`·`9e3cab5`, Q230·Q231) |
| **G15 attendance transportMode** | **`AttendanceServiceTest`** · **`MustApiEndpointRoutingTest`** `?transportMode=boarding` · **`AttendancePage.test`** · **`attendanceTransportMode.test`** · **`pilotPageFlows`** (`d6d7e7f`·`6c4c151`, Q232) |
| **QA-B19 geocode save guard** | **`transportUtils.test`** · **`TransportRunNewPage.test`** · **`TransportRunDetailPage.test`** — `countGeocodeFailures`(FAILED·좌표 미보유) · 저장 차단 (`318411d`·`48d90d5`, Q233) |
| **G21 duplicate visit import** | **`VisitServiceTest`** · **`VisitPilotServiceFlowE2eTest`** — `SKIPPED` + `IMPORT_SKIPPED_DUPLICATE_VISIT` (`9aafa3e`, Q234) |
| **G21 duplicate slot·paired confirm** | **`VisitServiceTest`** — manual create/update duplicate **`422`** · **`confirmPairedSchedule`** on confirm (`ff12473`·`aacf20b`, Q259) |
| **G15 Form22 service log (FE+BE)** | **`TransportServiceLogPanel.test`** · **`transportServiceLog.test`** · **`transportTimeCompliance.test`** (`7389884`·`eef07e5`·`7a4b310`, Q236·Q407) · BE **`TransportServiceTest`** · **`TransportTimeComplianceTest`** (`0cfa970`/`aaaeb10`) |
| **G21 HOME_CARE alias** | **`BranchServiceTypeTest`** · **`VisitServiceTest`** — `HOME_CARE` → `HOME_VISIT` (`894e246`, Q248) |
| **G2 recordCopayPayment paidAt guard** | **`BillingServiceTest.recordCopayPaymentShouldRejectNullPaidAt`** — null `paidAt` → `422` (`4001510`, Q250) |
| **G2 paymentMethod guard** | **`BillingServiceTest`** · **`J03AlimtalkServiceFlowE2eTest`** — PAID·납부확인서 dispatch 전 **`paymentMethod` 필수** (`64ebf6e`, Q249) |
| **US-J02 guardian portal guards (FE)** | **`GuardianPortalPage.test`** — out-of-order·stale billing error clear (`189a00d`·`bed612c`, Q251) |
| **UXD-75 RecordsContextNav (FE)** | **`RecordsContextNav.test`** · **`TransportContextNav.test`** — 기록·이동 in-page nav·SideNav service-fees (`a03a9f9`) |
| **G16 cross-branch fee guard** | **`TransportServiceFeeServiceTest`** — active branch scope on PATCH (`b5218a9`, Q247) |
| **G15 Form18 guide (FE)** | **`TransportForm18GuidePanel.test`** · **`transportForm18.test`** — 3-way application·registration states (`fcf713a`, Q237) |
| **V65 transport contract integrity** | **`TransportContractServiceTest`** — discharged·branch·signature guard (`24733c7`, Q235) |
| **G2 no-op claim status** | **`BillingServiceTest.updateClaimStatusShouldRejectNoOpTransition`** (`b0a88ac`, Q68) |
| **G21 paired check-in/out sync** | **`VisitServiceTest`** — `syncPairedScheduleProgress` on check-in/check-out (`9d7c17f`, Q238) |
| **G16 service-fee billing** | **`TransportServiceFeeServiceTest`** · **`TransportControllerRoutingTest`** · **`TransportServiceFeePanel.test`** (`88d4c59`·`9dfef92`, Q239) |
| **G16 vehicles master** | **`VehicleServiceTest`** · **`VehicleControllerRoutingTest`** · **`MustApiEndpointRoutingTest$VehicleRouting`** · **`VehiclesPage.test`** (`107bfb3`, Q241) |
| **US-M03 7-9 copay refund** | **`BillingServiceTest.recordCopayRefund*`** · **`CopayGuardianNotifyPaymentE2eTest`** refund·medical-expense exclusion · **`RoleBasedControllerAccessTest`**·**`MustApiEndpointRoutingTest`** · **`RefundRecordModal.test`** · **`BillingDetailPage.test`** · **`BillingReportPage.test`** refunds · **`pilotPageFlows`** refunds ledger (`de49b21`·`212e010`, Q261·Q179) |
| **G17 functional recovery (BNK-100~101)** | **`FunctionalRecoveryServiceTest`**(+65 indicator27) · **`RoleBasedControllerAccessTest$FunctionalRecoveryAccess`** · **`MustApiEndpointRoutingTest$FunctionalRecoveryRouting`** · **`FunctionalRecoveryPage.test`**(edit flow, `26499b3`) ·**`functionalRecoveryCompliance.test`** · **`DashboardPage.test`**·**`dashboardSummary.test`**·**`pilotPageFlows`** (`0048105`·`e820b28`·`21b1855`·`f1c60fe`, V72, Q271·Q279) |
| **BNK-87 NHIS claim comparison** | **`BillingServiceTest.getClaimNhisComparison*`** · **`RoleBasedControllerAccessTest$BillingAccess`** · **`MustApiEndpointRoutingTest`** · **`BillingNhisComparisonPanel.test`** · **`BillingDetailPage.test`** · **`pilotPageFlows`** (`2225a7a`·`18f5173`, Q264·BNK-91 P2) |
| **G33 billing start balance (BNK-94~99)** | **`BillingSettingsServiceTest`**(settle +4) · **`BillingServiceTest`** opening balance·overdue·**claim guard G33** · **`RoleBasedControllerAccessTest$BillingAccess`** · **`MustApiEndpointRoutingTest$SettingsRouting`** · **`BillingSettingsPanel.test`**(settlement reload, `eb48879`) · **`BillingStartBalanceNotice.test`** · **`BillingStartBalanceSettlementModal.test`** · **`billingStartBalance.test`** · **`OverduePage.test`** · **`pilotPageFlows`** G32/G33 (`1113caf`, Q269·Q270·Q273) |
| **UXD-81 billing reports nav (FE)** | **`BillingReportsContextNav.test`** · **`BillingNhisComparisonPanel.test`** import link · **`RecordsContextNav.test`** (`63361c0`, Q273) |
| **BNK-102 indicator27 verbatim (FE)** | **`functionalRecoveryCompliance.test`** · **`FunctionalRecoveryPage.test`** · **`DashboardPage.test`** (`7450161`, Q271) |
| **G37 grade history attachments (FE, US-M01-g)** | **`GradeHistoryAttachmentPanel.test.jsx`** · **`GradeHistoryTimeline.test.jsx`** · **`gradeHistoryAttachments.test.js`** · **`pilotPageFlows`** G37 E2E (`23bcd8c`) · **`gradeHistoryAttachmentLiveApi.e2e.test.js`** · **`gradeHistoryAttachmentServices.test.js`** (BNK-106, `6875af5`) · **MIME 없음/`octet-stream`일 때만 확장자 fallback** (`e9d1178`, Q274) |
| **G38 care-plan notification monitoring (FE, BNK-106)** | **`CarePlanNotificationPage.test.jsx`** · **`carePlanNotificationCompliance.test.js`** · **`DashboardPage.test.jsx`** G38 widgets · **`pilotPageFlows`** · **`programComplianceLiveApi.e2e.test.js`** (`28c22b0`·`4b2b082`·`87e6fae`, Q277) |
| **G17/G32 edit UI (FE)** | **`FunctionalRecoveryPage.test.jsx`** · **`CaseManagementPage.test.jsx`** — row **「수정」** → **`PATCH`** (`26499b3`, Q279) |
| **DateInput G11/G15 (FE-16)** | **`FeeSurchargeGuidePanel.test`** · **`TransportCompliancePanel.test`** — `.ds-date-input`·raw `type=date` 0건 (`4903173`, Q281) |
| **G39 provision result evaluation (FE, US-T08)** | **`ProvisionResultEvaluationPage.test.jsx`** · **`provisionResultCompliance.test.js`** · **`DashboardPage.test.jsx`**(4-pillar widgets + snapshot-first + partial fallback, `8e66ae8`·`8fa9f3d`, Q276·Q280·Q282) · **`dashboardSummary.test.js`** · **`programComplianceServices.test.js`** (`1c99bcd`·`8e66ae8`, Q276) |
| **BNK-75 NTS xlsx E2E (FE)** | **`pilotPageFlows`** — `ClientDetailPage` 청구 탭 NTS download (`48827b6`) |
| **program compliance live E2E (FE)** | **`programComplianceLiveApi.e2e.test.js`** — G17/G32 compliance read + optional write (`c413615`, BNK-103) |
| **FAQ21806 onboarding compliance (US-R03, BNK-146)** | **`StaffHrFileOnboardingComplianceTest`** · **`StaffHrFileServiceTest`**(batch branch, `60789d6`) · **`MustApiEndpointRoutingTest$StaffHrFileRouting`** · **`RoleBasedControllerAccessTest$StaffHrFileAccess`** · **`StaffOnboardingCompliancePanel.test`** · **`StaffMemberOnboardingComplianceCard.test`** · **`staffHrOnboardingCompliance.test`** · **`StaffPage.test`** (`d4ee057`·`4efa168`, Q300) |
| **G40b periodic risk assessment (BNK-153~154, Q302)** | **`ClientPeriodicRiskAssessmentServiceTest`** · **`MustApiEndpointRoutingTest$ClientRouting`** · **`RoleBasedControllerAccessTest$ClientAccess`** · **`RiskAssessmentPilotServiceFlowE2eTest`** (G40+G40b, `a7b4a39`, V95/V96) · **`ClientPeriodicRiskAssessmentPanel.test`** · **`PeriodicRiskAssessmentStatusPage.test`** · **`periodicRiskAssessmentCompliance.test`** · **`DashboardPage.test`** (`22325f4`·`7b68f54`) |
| **G40 admission risk assessment (BNK-150~152, Q301)** | **`ClientRiskAssessmentServiceTest`**(+54 duplicate regression, `2589b94`) · **`MustApiEndpointRoutingTest$ClientRouting`** · **`RoleBasedControllerAccessTest$ClientAccess`** · **`PilotChecklistJwtE2eTest`** (`22d736b`·`686d686`·`2589b94`, V93/V94) · **`ClientRiskAssessmentPanel.test`** (`328d697`) · **`DashboardPage.test`**·**`admissionRiskAssessmentCompliance.test`** (`2f5af63`) |
| **US-R03 staff HR file hub (FAQ21806, BNK-139)** | **`StaffHrFilePilotServiceFlowE2eTest`** · **`StaffHrFileServiceTest`** · **`MustApiEndpointRoutingTest$StaffHrFileRouting`** · **`RoleBasedControllerAccessTest$StaffHrFileAccess`** · **`StaffHrFilePanel.test`** · **`staffHrFileServices.test`** · **`pilotPageFlows`** HR file E2E (`bbb8e35`·`bc3c967`, Q298) |
| **US-S02 staff refresher training (8-7-1)** | **`StaffRefresherTrainingComplianceTest`** · **`StaffRefresherTrainingServiceTest`** · **`StaffRefresherTrainingCertificateServiceTest`** · **`StaffRefresherTrainingCertificateStorageServiceTest`** · **`MustApiEndpointRoutingTest$StaffRefresherTrainingRouting`** · **`RoleBasedControllerAccessTest$StaffRefresherTrainingAccess`** · **`StaffRefresherTrainingPage.test`** · **`staffRefresherTrainingServices.test`** · **`staffRefresherTrainingCompliance.test`** · **`pilotPageFlows`** refresher·certificate E2E (`51477bd`·`0a7fe16`, Q294·Q295) |
| **G41/G41b staff training logs (8-7, Q321·Q325·Q489, BNK-184~188)** | **`StaffTrainingLogServiceTest`** · **`StaffTrainingLogPilotServiceFlowE2eTest`** · **`MustApiEndpointRoutingTest$StaffTrainingLogRouting`** · **`StaffTrainingLogPage.test`** · **`staffTrainingLogs.test`** — **reference-year guard + filter inline error** (`f26e075`/`28e5525`, Q489) · **`staffTrainingLogLiveApi.e2e.test.js`** (`LIVE_E2E=1`, BNK-186) · V104–V107 |
| **US-R03 staff lifecycle (BNK-129)** | **`UserServiceTest`** · **`StaffLifecyclePilotServiceFlowE2eTest`** — **`ON_LEAVE`·ACTIVE 복귀** (`68d4457`, Q584) · **`StaffLifecycleSummaryServiceTest`** — **`onLeaveCount`** (`1d7cee2`) · **`StaffLifecyclePanel.test`**·**`StaffLifecycleSummaryPanel.test`** — **휴직 UI·집계** (`2581347`, Q584) · **`StaffPage.test`** — lifecycle **필터 5-state** |
| **G-BILLING deposit half-month·receipt dual-basis (Q585·Q586·Q587·Q588)** | **`BillingServiceTest`** — `period`·`basis` filter · **invalid calendar month rejection** (`375fb9d`) · **`appliedFilters` echo** (`14935a3`) · **receipt CLAIM basis regression** (`7b99313`, QA-B193) · **`BillingReportAppliedFiltersTest`** · **`BillingReportFilterEnumsTest`** · **`MustApiEndpointRoutingTest`** — **`billingDepositsReportRouteShouldAcceptHalfMonthPeriod`** · **`billingReportFilters.test`** · **`BillingReportPage.test`** (`e38ccfd`·`c6a412f`·`e2f1246`) |
| **G30 monitoring self-diagnosis·phone consultation (BNK-169~171, Q314)** | **`MonitoringPilotServiceFlowE2eTest`** · **`RoleBasedControllerAccessTest$MonitoringAccess`** · **`MonitoringSelfDiagnosisPage.test`** · **`programComplianceServices.test`** (V100/V101, `6a72b70`·`5692662`) |
| **US-R02 staff status report aggregated·CSV export (8-12, Q308·Q315)** | **`StaffStatusReportPilotServiceFlowE2eTest`** · **`StaffStatusReportServiceTest`** · **`StaffStatusReportPage.test`** — aggregated API·**BE CSV export** (`bc927f7`·`488f547`) |
| **G42 follow-up·pending-approval (BNK-174, Q309·Q316)** | **`GrievanceCounselingPilotServiceFlowE2eTest`** · **`PilotChecklistJwtE2eTest`** follow-up routes · **`ComplaintConsultationPanel.test`** · **`GrievanceFollowUpModal.test`** (`bcb1d9f`·`6012044`) |
| **J03 notification channel readiness (Q318)** | **`NotificationChannelReadinessServiceTest`** · **`NotificationChannelStatusPilotServiceFlowE2eTest`** · **`MustApiEndpointRoutingTest`** · **`RoleBasedControllerAccessTest$NotificationChannelStatusAccess`** (`fffd355`·`229f84c`) |
| **J03 readiness UI (Q318)** | **`NotificationChannelReadinessPanel.test`** · **`notificationChannelStatusLiveApi.e2e.test.js`** (`6b1258c`·`d695923`) |
| **#44 V103 transport fee seed (BNK-174, Q317)** | Flyway **V103** 적용 확인 · **`TransportServiceFeeServiceTest`** RU_3/RU_4 (`39ee679`) |
| **G-7x-1-guard claim generation UX (BNK-160, Q310)** | **`ClaimGenerationGuardBanner.test`** · **`claimGenerationGuard.test`** · **`ClaimGenerationPanel.test`** — 7-2→7-1 workflow·G33 분기 (`338c014`) |
| **G-7x-1 G33 YearMonth guard (Q270)** | **`BillingServiceTest`** — G33 **`effectiveMonth`** vs target claim month (`21eb0af`) |
| **G9-COG cognitive fee schedule (BNK-166, Q311·Q260)** | **`Nhis2026DaycareRateCatalogTest`** · **`FeeScheduleYearCoverageTest`** cognitive cells · **`NhisImportServiceTest`** cognitive gate · **`CognitiveSupportFeeSchedulePilotServiceFlowE2eTest`** · **`BillingServiceTest.applyMissingNhisSeedFeeSchedules*`** · **`FeeScheduleMatrix.test`** · **`feeSchedules.test`** (`8bb6583`·`edd2771`·`6ef671b`) |
| **G9-COPAY-NAMING (Q313)** | **`CopayTypeSelect.test`** · **`CopayRateTable.test`** (`e77b7e4`·`a5c2736`) |
| **FAQ21824 client lifecycle (BNK-165, Q312)** | **`faq21824Lifecycle.test`** · **`ClientDetailPage.test`** — 4-step checklist hydrate (`58256c6`) |
| **G42 pending-approval API (BNK-161, Q309)** | **`GrievanceCounselingServiceTest`** pending-approval · **`GrievanceCounselingPilotServiceFlowE2eTest`** · **`MustApiEndpointRoutingTest`** · **`RoleBasedControllerAccessTest`** (`6f6094d`, V98) |
| **US-T14 anonymous grievance masking (Q305)** | **`ComplaintConsultationPanel.test`** — **`ANONYMOUS_BOX`** display masking (`4b54da5`) |
| **G34b import-draft API (BNK-157, Q303·Q306)** | **`LeadCaregiverWorkLogImportPilotServiceFlowE2eTest`** · **`LeadCaregiverWorkLogServiceTest`** import-draft·cognitive guard · **`MustApiEndpointRoutingTest`** · **`RoleBasedControllerAccessTest$LeadCaregiverWorkLogAccess`** (`8487667`·`b6ecc35`) |
| **G42 grievance counseling (BNK-161, Q305)** | **`GrievanceCounselingServiceTest`** · **`GrievanceCounselingPilotServiceFlowE2eTest`** · **`PilotChecklistJwtE2eTest`** G42 routes · **`GrievanceCounselingPage.test`** · **`grievanceCounselingServices.test`** (`bcdc411`·`0460e9b`, V97) |
| **G34 lead caregiver work log + sign modal + import + clone (G34b)** | **`LeadCaregiverWorkLogServiceTest`** · **`SignLeadCaregiverWorkLogModal.test`** · **`LeadCaregiverWorkLogPage.test`** · **`leadCaregiverWorkLogImport.test`** · **`pilotPageFlows`** sign modal E2E · **전월 복제·cognitive guard** (`314b380`·`0ce04ad`·`1b5fabe`·`994f5ea`, Q288·Q303·Q306) |
| **G40/G40b live API harness (FE)** | **`riskAssessmentLiveApi.e2e.test.js`** — G40 admission·G40b periodic read-only live checks (`0ce04ad`, `LIVE_E2E=1`) |
| **G21 paired visit guard + assigned user + check-in guard** | **`VisitServiceTest`** — check-in/out sync·link integrity·legacy slot·**DRAFT sync guard**·**assignedUserId validation**·**assigned caregiver check-in/out** (`82bdbcd`·`588bfb1`·`dc48933`·`b459f4c`, Q238·Q289·Q304·Q307) |
| **G32 case management** | **`CaseManagementServiceTest`**(incl. `evaluationConductedMet`) · **`RoleBasedControllerAccessTest$CaseManagementAccess`** · **`MustApiEndpointRoutingTest$CaseManagementRouting`** · **`CaseManagementPage.test`**·**`caseManagementCompliance.test`**·**`pilotPageFlows`** US-T07 · **`DashboardPage.test`**·**`dashboardSummary.test`** (`11277b9`·`fa2ad1e`·`7f2289b`, V73·V74·V75, Q263·Q265·Q266) |
| **US-D01 primaryGuardian** | **`ClientServiceTest`** — `POST /clients` **`primaryGuardian` 필수** (`0441a07`, Q268) |
| **Pilot fixture panel (FE)** | **`PilotFixturePanel.test`** — dev/flag gate (`c89a82b`·`37e6b00`, Q268) |
| **Tenant context filter** | JWT 인증 후 **`TenantContextFilter`** 실행 (`cbb7f55`) — Tenant 격리 E2E 회귀 |
| **hq_admin client create** | **`RoleBasedControllerAccessTest$ClientAccess`** — `POST /clients` **`hq_admin`** 허용·활성 지점 스코프 (`208b37e`, Q267) |
| **US-L03 CMS re-register** | **`CmsServiceTest.createEnrollmentShouldReactivateCancelledEnrollmentWithoutCreatingNewRow`** (`8431b5c`, Q207) |
| **US-G04 year-coverage normalize** | **`NHISImportPage.test`** — coverage 응답 정규화·업로드 차단 (`53e4016`, Q260) |
| **US-M03 billing ledger reports** | **`BillingServiceTest`** listBillingReport charges·receipts·refunds · **`RoleBasedControllerAccessTest`**·**`MustApiEndpointRoutingTest`** · **`BillingReportPage.test`** · **`pilotPageFlows`** charges ledger (`22d82e2`·`c30aaac`, Q179) |
| **US-G04 year-coverage pre-check** | **`BillingServiceTest`** getFeeScheduleYearCoverage · **`NHISImportPage.test`** server coverage block (`8f208e4`·`c30aaac`, Q260) |
| **QA-B24 NHIS guidance UI** | **`NHISImportPage.test`** · **`NhisImportGuidePanel.test`** — partial-failure guidance retention (`1220bfb`·`2b6024a`·`0abf164`, Q133) |
| **Field aria-required** | **`Field.test.jsx`** — `aria-required` 회귀 7건 (`1f71335`, Q245) |
| **G15 care-provision** | **`CareProvisionRecordServiceTest`** · **`MustApiEndpointRoutingTest`** · **`CareProvisionRecordPanel.test`** (`8bdead6`·`08dbcf0`, Q243) |
| **V70 integrity** | Flyway **`V70__g15_g16_v67_v69_integrity.sql`** — outings·service-fee·vehicles·runs triggers (`ba4c9d9`, Q246) |
| **Guardian billing DRAFT filter** | **`BillingServiceTest`** — `listGuardianClientBillingHistory` CONFIRMED/PAID only (`3def542`, Q212) |
| **Billing RBAC regression** | **`RoleBasedControllerAccessTest$BillingAccess`** — notify·payment·overdue·bank-deposit (`dd7a580`) |
| **G2 paidAt on PAID status** | **`BillingServiceTest`** — `updateClaimStatus` PAID metadata (`e16534c`, Q244) |
| **G16 vehicle assignment** | **`TransportVehicleSelect.test`** · **`TransportRunDetailPage.test`** (`08dbcf0`, Q241) |
| **G15 client outings** | **`ClientOutingServiceTest`** · **`ClientOutingControllerRoutingTest`** · **`ClientOutingPanel.test`** · **`ClientOutingReportPage.test`** (`7dfcc9e`·`a0dcfc0`, Q240) |
| **V66 duplicate import index** | **`VisitServiceTest.importNhisShouldSkipDuplicateVisitRows`** · **`MustApiEndpointRoutingTest`** (`639ac91`, Q234) |
| **UXD-73 attendance context nav** | **`AttendanceContextNav.test`** — landmark·`aria-current` (`420b4d7`, Q242) |
| **US-M04 cap success banner** | **`MonthlyBenefitCapGuardBanner.test`** — `warningCount=0` success (`62f022d`, Q226) |
| **G2 payment receipt·elder abuse** | **`BillingServiceTest.notifyPaymentReceipt*`** · **`GuardianDocumentNotificationServiceTest.notifyElderAbusePreventionGuideline*`** · **`EmailNotificationContentTest`** · **`CopayGuardianNotifyPaymentE2eTest`** (Q221·Q222, `0854fbd`·`588b8e6`) |
| **G2 SMTP email** | **`SmtpEmailProviderTest`** 5건 — dispatch·invalid email·FROM validation (`6ed48ff`·`f23f15a`, Q204) |
| **G21 confirm-lock FE** | **`NhisScheduleConfirmLockGuide.test`** · **`NHISImportPage.test`** · **`pilotPageFlows`** G21 E2E (Q209) |
| J03 vitals DAILY_CARE | **`HealthRecordService.createVitals` dispatch** (`0832fbf`) + medication·note |
| J03 incident EMERGENCY | **`HealthRecordService.createIncident`** — `FALL` → **EMERGENCY** dispatch |
| J03 notification dispatch | `NotificationServiceTest` · `SolapiKakaoAlimtalkProviderTest` · **`NotificationAlimtalkDispatchE2eTest`** |
| B08 preference | `NotificationPreferenceServiceTest` |
| V44–V97 | `phone_encrypted` · transport V47 · … · **G37 attachments V78–V79** · **G39 V80–V81** · **G34 V82–V83** · **G24-G14 V84–V85** · **US-R03 V86–V92** · **G40 V93–V94** · **G40b V95–V96** · **G42 V97** `grievance_counseling_records` — FAQ Q148·…·**Q305–Q307** |
| v3 meals/programs | **`MealServiceTest`** 3건 · **`MealControllerRoutingTest`** 2건 · **`ProgramServiceTest`** 3건 · **`ProgramControllerRoutingTest`** 2건 · **`MustApiEndpointRoutingTest$MealsRouting`**·**`$ProgramsRouting`** (Q160) |

스테이징 승격 전 `mvn test` **764/764 PASS** · `npm test -- --run` **871/871 PASS** 를 확인하세요 (FAQ Q68·…·**Q285–Q295**).

### 3-7. 프론트엔드 테스트·빌드

```bash
cd src/frontend
npm ci
npm test          # Vitest — 192 files / 843 tests (840 PASS; userServices.test.js 3 FAIL @ f8f47e1)
npm run build     # dist/ — HEAD a018e71: US-R03 staff lifecycle + G24-G14 tabs + G34 lead caregiver log
```

#### live backend E2E (선택, `scripts/run-live-e2e.sh`)

Vitest 기본 실행(`npm test`)은 **`src/e2e/**`를 제외**합니다. 스테이징·로컬 백엔드가 기동 중일 때 **선택 검증**으로 실행합니다.

**환경 파일 준비 (QA-B95, 필수 1회)**:

```bash
# 루트에서 — 비밀값은 .gitignore 대상, 커밋 금지
cp scripts/dev-live-e2e.env.example scripts/dev-live-e2e.env
# 필요 시 LIVE_E2E_EMAIL·LIVE_E2E_PASSWORD·VITE_API_BASE 조정
```

`npm run test:live-e2e`(FE `eb16734`·…·`c3b6a5c`)는 **git root**의 **`scripts/dev-live-e2e.env`** 를 자동 source합니다 (`frontend-test` checkout 포함). 파일이 없으면 **`.example`** 을 fallback으로 읽습니다. **`LIVE_E2E_GUARDIAN_EMAIL`·`LIVE_E2E_GUARDIAN_PASSWORD`** 미설정 시 **`b3bd0cc`** — bootstrap enabled면 **`POST /api/v1/system/live-e2e/bootstrap-guardian`** 으로 guardian token·`LIVE_E2E_CLIENT_ID` 자동 발급. **`LIVE_E2E_CLIENT_ID` 미설정** 시 health probe **`liveE2eSeedClientId`** 로 자동 주입 (`689f377`, Q496). **G21 live suite**(`liveG21Describe`)는 **`liveE2eOperationReady` + G21 seed ready (PLAN + paired BILLING + NHIS)** 일 때만 실행 (`d61ab5e`/`c3b6a5c`, Q497·Q512). bootstrap endpoint **HTTP 500/503** 이더라도 env creds가 유효하면 **`ddd4489`** — **`login-fallback-ok`** 로 재로그인 시도 — FE default fallback은 **`live-e2e-guardian@ogada.test`/`ogada-guardian-e2e`** (`94c65e2`, Q473). **example placeholder** 값 그대로면 authenticated suite도 **skip** (`5c24e4e`/`7106106`).

**269차 US-R03 FAQ21823 clauses checklist+template modal · G21 not-applicable live E2E (`1b6d2b1`/`091c372`)**: FE **`StaffEmploymentContractRenewalPanel`** — **`EMPLOYMENT_CONTRACT_REQUIRED_CLAUSES`** 5항 · **`EMPLOYMENT_CONTRACT_RENEWAL_WORKFLOW`** · **「근로계약서 서식 보기」Modal** · **`staffEmploymentContract.js`**. BE **`LiveE2eBootstrapService.g21SeedStatus`** — unsupported **`serviceType`** → **`notApplicable()`** — **`liveE2eOperationReady` 유지** · health **`g21-seed=not-applicable`** · **`HealthControllerTest`**. FAQ **Q540·Q541 갱신·Q546 신규**.

**273차 v1.3-A Kakao API status+usage probe · suggest route-preview embed · TransportKakaoApiStatusPanel (`e2b764b`/`ba74bb5`)**: BE **`GET /transport/kakao-api-status`** · **`TransportKakaoApiStatusService`** · **`KakaoRestApiUsageTracker`** · suggest **`legDurationsSeconds`·`routePath`** · FE **`TransportKakaoApiStatusPanel`** · **`KakaoTransportMapView`** layer split · **`hasRouteLegDurations`** (Q554). FAQ **Q554 신규**.

**272차 v1.3-A transport preview cache+roster ETA merge · G30/G39 nav label disambiguation (`acc5933`)**: FE **`transportRunPreviewCache.js`** — suggest·DRAFT **route-preview 재사용** · **`kakaoMapGeocoder.js`** geocode cache · **`buildSuggestRunDispatchIndex`** — **자동 배차 ETA→명단「계획 픽업」** · **`TransportSuggestPanel`** **「반영도착」** 열 · **`navConfig.js`** **G30/G39** SideNav suffix (Q553). FAQ **Q553 신규**.

**271차 v1.3-A transport roster tools+ETA guardrails · guardian credential blocker separation · UXD-142 renewal a11y (`4681b5a`/`48eea95`/`520f10a`/`bd6e1c2`)**: FE **`TransportLoadPreviousRunModal`** · **`TransportAddRosterModal`** · **`TransportConfirmWarningModal`** — **`findDesiredBoardingViolations`** · **`pickupToleranceMinutes`** (Q550). BE **`UpdateTransportRunRequest.plannedDepartureTime`** · **`validateClientPickupTimeSequence`** (Q550). BE **`guardian-credentials-missing`/`guardian-credentials-default` 분리** (Q551). FE **`EmploymentContractRenewalAlertsPanel`** **`<time dateTime>`·checklist CSS** (Q552). FAQ **Q550~Q552 신규**.

**270차 US-R03 FAQ21823 renewal record+due alerts · live E2E operation readiness centralization (`033b319`/`bfad37d`/`4d4457f`/`16afd4c`)**: FE **`StaffEmploymentContractRenewalPanel`** — **「재계약 완료 기록」** Modal — **`updateUserApi`** — **`EmploymentContractRenewalAlertsPanel`** — dashboard **overdue·due-soon(30일)·missing** (Q547). BE **`LiveE2eOperationReadinessSupport`** — **`HealthController`**·**`LiveE2eController`** 공유 — **`cashReceiptIdentifierValueCheckReady`** probe alignment (Q548). FE **`liveConfig.js`** — legacy G21 seed flags without explicit applicability (Q549). FAQ **Q540·Q544 갱신·Q547~Q549 신규**.

**268차 V159 cash receipt identifier CHECK · health V159 probe · UXD-141 a11y · nested health readiness (`15061a9`/`1139e79`/`965e569`/`682d647`/`202c1fe`)**: BE **V159** **`chk_cash_receipt_issuances_identifier_value_format`** — digit-only + PHONE 10~11·BIZ 10 (Q543) · **`CashReceiptSchemaReadinessProbe`** — health **`cashReceiptIdentifierValueCheckReady`** · blocker **`cash-receipt-identifier-check-missing`** · **`HealthControllerTest`**. FE **`liveBackendProbe.extractLiveE2eHealthFields`** — nested **`liveE2e`** · snake_case (Q545) · **`StaffEmploymentContractRenewalPanel`**·**`StaffEmploymentContractRenewalSummaryPanel`**·**`CashReceiptRegisterModal`** a11y (Q544, UXD-141). FAQ **Q537·Q540 갱신·Q543~Q545 신규**.

**267차 US-R03 FAQ21823 list+dashboard renewal · live E2E allow-default-credentials (`10585b9`/`f31c346`/`beef81e`)**: FE **`StaffEmploymentContractRenewalSummaryPanel`** — **`/staff`** — **StatCard·확인 필요 표** · **`DashboardPage`「근로재계약 미충족」** · **`staffEmploymentContractCompliance.js`**. BE **`ogada.live-e2e.allow-default-credentials`** (기본 **`true`**) — health **`liveE2eAllowDefaultCredentials`** · **`LiveE2eControllerTest.probeShouldAllowDefaultCredentialsWhenFlagEnabled`**. FAQ **Q540 갱신·Q542 신규**.

**266차 US-R03 FAQ21823 employment contract renewal · live E2E unsupported branch seed (`f62402f`/`7a9d7a5`)**: FE **`StaffEmploymentContractRenewalPanel`** — **`/staff/{userId}`** — **서명일+1년·3년 보관·2026 최저임금·overdue Alert** · **`StaffEmploymentContractRenewalPanel.test`**. BE **`LiveE2eBootstrapService.isG21SeedApplicableBranch`** — **`HOME_VISIT`/legacy `DAY_CARE` 외 serviceType** → **`unsupportedServiceType()`** · **`LiveE2eBootstrapServiceTest.g21SeedStatusShouldBlockWhenBranchUsesUnsupportedServiceType`**. FAQ **Q540·Q541 신규**.

**265차 J03 guardian document quiet-hours · G-CASH-RECEIPT FE identifier validation (`7e4c07e`/`0038846`)**: BE **`GuardianDocumentNotificationService`** → **`dispatchManualClientEvent`** — quiet-hours **`422 BUSINESS_RULE`** · **`J03GuardianDocumentManualNotifyQuietHoursE2eTest`**. FE **`CashReceiptRegisterModal`** — submit 전 **digit·자릿수 `fieldErrors`** · **`CashReceiptRegisterModal.test`**. FAQ **Q537 갱신·Q539 신규**.

**264차 G-CASH-RECEIPT-LOG numeric-only identifier · UXD-140 a11y (`4da0ca8`/`501fedc`)**: BE **`normalizeIdentifierValue`** — digit 추출 후 **빈 문자열 거부** · **「발급 식별자(휴대폰/사업자번호)는 숫자만 입력해 주세요.」** · **`CashReceiptIssuanceServiceTest`**. FE **UXD-140** — **`CashReceiptIssuancePage`** **`CASH_RECEIPT_PENDING_ERROR_ID`·`aria-describedby`** · **`aria-busy`** · **`BillingStatementPrintPanel`** PDF **`aria-label`** · **`MedicalExpenseDeductionPanel`** 조회 **`aria-busy`** · **`ds-segmented` forced-colors**. FAQ **Q537 갱신·Q538 신규**.

**263차 G-CASH-RECEIPT-LOG identifier normalize+validation · pending load error guard (`298bcdf`/`35d1560`/`99b795a`)**: BE **`CashReceiptIssuanceService`** — **`q` digit-only identifier search** · **`normalizeIdentifierValue`·`validateIdentifierValue`** PHONE 10~11·BIZ 10 · **`CashReceiptIssuanceServiceTest`** · **`CashReceiptIssuanceLiveApiRoutingE2eTest`**. FE **`CashReceiptIssuancePage`** — **`pendingError` warning Alert** · **`CashReceiptRegisterModal`** **「· 작년분」** suffix · **`CashReceiptIssuancePage.test`**. FAQ **Q537 신규**.

**262차 G26 yearBasis+NTS CSV · G-7-1 Excel export · UXD-139 a11y (`19ed7f3`/`ceeaeb9`/`58d6694`/`e454d3b`)**: BE **`MedicalExpenseDeductionYearBasis`** · **`GET …/medical-deduction/export`** · **`BillingStatementExportService`** · **`MedicalExpenseDeductionYearBasisTest`**. FE **`BillingStatisticsReportPage`** — segmented control·**「국세청 CSV」** · **`BillingStatementPrintPanel`** Excel row · **`CashReceiptRegisterModal`** UXD-139·empty pending guard. FAQ **Q534~Q536 신규**.

**261차 G-CASH-RECEIPT-LOG 4-계층 closure · HQ pending · prior-year advisory (`8aebe55`/`58ff35e`)**: BE **`listPendingIssuances(null)`** — 다지점 **`hq_admin` 전 지점 집계** · **`priorYearIssuanceEligible`** — 청구연도 < 올해 · **`CashReceiptIssuanceServiceTest`**. FE **`CashReceiptRegisterModal`** — FAQ 21717 warning Alert · **`PaymentPage`** **`isPriorYearClaim`** · **`PaymentPage.test`**. FAQ **Q530·Q532 갱신·Q533 신규**. 지점 batch CSV는 **262차 Q534** closure.

**260차 G-CASH-RECEIPT-LOG dashboard due-gate·pending issuance API (`221458e`/`fe54af8`/`ab5708b`)**: BE **`BranchDashboardResponse`·`HqDashboardResponse`** — **`cashReceiptPendingCount`·`cashReceiptOverdueCount`** · **`GET /billing/cash-receipt-issuances/pending`** — **`PendingCashReceiptIssuanceListResponse`** · **`CashReceiptIssuanceServiceTest`** · **`DashboardServiceTest`**. FE **`DashboardPage`** — **「현금영수증 미발급」**·**「발급 지연」** StatCard · **`/billing/cash-receipts`** 링크 · **`dashboardSummary.test`**. FAQ **Q530 갱신·Q532 신규**.

**259차 G-CASH-RECEIPT-LOG payment bridge·live API harness (`a17f148`/`8e6e0c6`)**: FE **`PaymentPage`** — **`PaymentRecordModal`** CASH FAQ 21716 Alert · **수납 저장 후 `CashReceiptRegisterModal`** · **`cashReceiptIssuanceLiveApi.e2e.test.js`**. BE **`CashReceiptIssuanceLiveApiRoutingE2eTest`** — FE `fetchCashReceiptIssuancesApi`·`fetchClientCashReceiptProfileApi`·`createCashReceiptIssuanceApi` contract mirror · **`CashReceiptIssuanceServiceTest`** profile phone decrypt. FAQ **Q530·Q531 갱신**.

**258차 G-CASH-RECEIPT-LOG full-stack·V158 (`4432558`/`cfc4b04`/`f79a19e`)**: BE **`CashReceiptIssuanceService`** — **`GET/POST /billing/cash-receipt-issuances`** · **`GET …/clients/{id}/cash-receipt-profile`** · **V158** `cash_receipt_issuances` · **`immediateIssuanceMet`** 7일 SLA · **`pendingCashPaymentCount`** · **`CashReceiptIssuanceServiceTest`** · **`RoleBasedControllerAccessTest`**. FE **`CashReceiptIssuancePage`** — **`/billing/cash-receipts`** 2탭 · **`CashReceiptRegisterModal`** · **`CashReceiptLegalAlerts`** (FAQ 21716/21717) · **`BillingReportsContextNav`** 7탭. FAQ **Q530 갱신·Q531 NTS API gap**.

**257차 G21 split-view dual NHIS·health G32 alignment·credential trim·UXD-138 a11y (`9b80505`/`caeac0d`/`7848b0f`/`d354a0e`)**: FE **`VisitsPage`** — split-view 시 **`VisitNhisComparisonPanel`** PLAN·BILLING 각 1개 · **`role="group"`** landmark (Q526) · kind-specific heading·G32·G2 a11y (Q527). BE **`HealthController`** — **`liveE2eG32*FieldReady`** 3축 + blockers mirror probe (Q528) · **`LiveE2eBootstrapService.normalizeCredential`** trim (Q529). FAQ **Q525 갱신·Q526~Q530**.

**256차 G32 probe schema readiness·stale runtime guard·케어포 3-1 health segment nav (`c0a59aa`/`45d95ea`/`09912ba`/`1d5747d`)**: BE **`LiveE2eController`** — **`g32ComplianceAttendeeOpinionsFieldReady`·`g32DashboardAttendeeOpinionGapFieldReady`·`g32AttendeeOpinionsArrayCheckReady`** — blockers **`g32-compliance-field-missing`·`g32-dashboard-field-missing`·`g32-v157-constraint-missing`** · **`G32SchemaReadinessProbe`** pg_catalog V157 CHECK (Q525). FE **`programComplianceLiveApi.e2e.test.js`** — **`hasG32SchemaBlocker()`**·**`shouldSkipForMissingG32Field()`** stale runtime skip (Q525) · **`CareProvisionSegmentNav`** on **`/health`** (Q524). FAQ **Q523 갱신·Q524~Q525**.

**255차 G32 FAQ21797 live E2E harness deepen·pilot E2E extend (`510d2f3`/`3f871d7`)**: FE **`programComplianceLiveApi.e2e.test.js`** — create/update **`attendeeOpinions[]`** · compliance **`attendeeOpinionsMetCount`** · dashboard **`caseManagementAttendeeOpinionGapCount`** (Q522). BE **`ProgramCompliancePilotServiceFlowE2eTest`** · **`CaseManagementServiceTest`** update-path. FAQ **Q522~Q523**.

**254차 G32 V157 attendee_opinions array CHECK·unique per-attendee opinions·live E2E skip diagnostics (`8835aa2`/`eed39ab`/`c7fb69a`/`9969746`)**: BE **V157** — **`chk_case_management_meetings_attendee_opinions_array`** — **`jsonb_typeof(attendee_opinions) = 'array'`** (Q519) · **`CaseManagementService`** — 참석자·의견 작성자 **중복 거부** (Q520) · **`AttendeeOpinionsCodecTest`** (Q519). FE **`CaseManagementPage`** — **`buildDuplicateAttendeeNamesError`** 선검증 (Q520) · **`liveConfig.getLiveE2eSkipReasons`** — gated suite skip **actionable reasons** (Q521). FAQ **Q519~Q521**.

**253차 G32 FAQ21797 dashboard attendee-opinion gap widget (`b9e0947`/`e55ae96`)**: BE **`caseManagementAttendeeOpinionGapCount`** on **`GET /dashboard/branch`**·**`/dashboard/hq`** — HQ **`attendeeOpinionsMetCount` 합산 정정** (Q518). FE **`DashboardPage`** — **「참석자별 의견 미기록」** StatCard · compliance API 폴백. FAQ **Q518**.

**252차 G32 FAQ21797 attendee opinions·G2 guardian document 3-type panel·live E2E health diagnostics deepen (`5222a8f`/`b272a7b`/`d1149a5`/`12d1a7b`)**: BE **V156** `attendee_opinions` JSONB · **`CaseManagementService`** **`attendeeOpinionsMet`** compliance (Q516). FE **`CaseManagementPage`** per-speaker opinion fieldset · **`GuardianDocumentNotifyPanel`** 3-type **`Select`** (Q517). BE **`HealthController`** — **`liveE2eGuardianStatusDetail`·`liveE2eG21SeedStatusDetail`** (Q515). FAQ **Q515~Q517**.

**251차 G39 FAQ21817 7-day SLA·RFID equivalence·health G21 branch blocker·FE billing gate (`b881883`/`bc754a0`/`c3b6a5c`)**: FE **`computeStateChangeDueAlerts`** — **`CareServiceWeeklyRecordPage`** SLA Alert (Q513) · **`VisitRfidDiffComparePanel`** RFID↔별지 info Alert (Q514). BE **`HealthController`** — **`g21-branch-missing-or-inactive`** in health blockers (Q511) · FE **`isLiveG21SeedReady`** — **`liveE2eBillingVisitScheduleReady`** required (Q512). FAQ **Q511~Q514**.

**250차 G21 cross-branch seed scope·guardian bootstrap enrichment guard·QA-B147 batch-confirm loading·UXD-136/137 L03 edit a11y (`02a2eb8`/`02cf036`/`5743333`/`f86c76c`)**: BE **`LiveE2eBootstrapService.g21SeedStatus`** — resolved PLAN/BILLING visit schedule·NHIS import batch **`branchId` ≠ configured `LIVE_E2E_BRANCH_ID`** → ready flags **false** (Q507) · **`isUsableGuardianCredentialsConfigured()`** — default guardian creds only → staff bootstrap **guardian token skip** (Q510). FE **`VisitBatchConfirmPanel`** — missing **`branchId`** → **`setLoading(false)`** (Q508) · **L03 nursing 5종+통합 바이탈** 행 수정 **`Button variant=tertiary`** (Q509). FAQ **Q507~Q510**.

**249차 G21 probe branch-missing blocker·UXD-147 batch-confirm NHIS ack a11y (`7898aa5`/`0002943`)**: BE **`LiveE2eController`** — **`!g21SeedApplicable && !g21SeedOperationReady`** → **`g21-branch-missing-or-inactive`** in **`operationBlockers[]`** (Q505) — **251차 health 동기화** (`bc754a0`, Q511). FE **`VisitBatchConfirmPanel`** — NHIS ack Checkbox **`aria-describedby`** → **`visit-batch-confirm-nhis-comparison`** (Q506). FAQ **Q502 갱신·Q505~Q506**.

**248차 G21 paired PLAN/BILLING seed·billing readiness probe·legacy DAY_CARE guard·missing branch block·G41 filter-year load guard (`fd275f4`/`429661e`/`cc295ec`/`191703f`/`cefb7c7`)**: BE **`HealthController`**·**`LiveE2eController`** — **`liveE2eBillingVisitScheduleReady`·`liveE2eBillingVisitScheduleId`** · blockers **`billing-visit-schedule-missing`** (Q500) · **`ensureSampleVisitSchedules`** paired PLAN+BILLING upsert · legacy **`DAY_CARE`** G21 applicable until **`HOME_VISIT` upgrade** (Q501) · **`missingBranchOrInactive()`** multi-tenant guard (Q502). FE **`StaffTrainingLogPage`** — invalid filter **`load()` skip** (Q503) · UXD-135 Modal **`Field controlProps`** (Q504). FAQ **Q495·Q457 갱신·Q500~Q504**.

**247차 G21 seed readiness·scoped fallback IDs·NHIS row-batch linkage·liveG21Describe gate (`14582bf`/`c651b30`/`c0403b0`/`689f377`/`d61ab5e`)**: BE **`HealthController`**·**`LiveE2eController`** — **`liveE2eG21SeedApplicable`·`liveE2eVisitScheduleReady`·`liveE2eNhisImportReady`** + resolved IDs · **`operationReady`** includes G21 seed · blockers **`visit-schedule-missing`·`nhis-import-missing`** (Q495) · **`scopedFallbackId`** per-tenant deterministic fallback (Q498) · **row `batchId` = batch `id`** linkage (Q499). FE **`liveBackendProbe.extractLiveE2eHealthFields`** · **`isLiveG21ReadyForRun`** · **`liveG21Describe`** gate (Q496·Q497). FAQ **Q495~Q499**.

**213차 actuator readyz/livez·liveness/readiness split·이용자 연락처 (`f0e52b8`/`c19206a`/`911a1b9`/`0baabe9`)**: BE **`ActuatorHealthController`** — **`/actuator/livez`**·**`/actuator/readyz`** · liveness **항상 UP** · readiness **DB probe**. FE **`ClientListPage`** — **`phoneMasked`** 연락처 열. FAQ **Q413 갱신·Q417**.

**222차 G30 monitoring evidence panel·live E2E guardian default credentials (`7d2cb4a`/`92be918`/`09df8c7`)**: FE **`MonitoringSelfDiagnosisPage`** — **`MonitoringEvidenceContextPanel` `variant="g30"`** — FAQ21838 증빙 기간·G24b/G21/G26 cross-link · **`MonitoringSelfDiagnosisPage.test`**. BE **`LiveE2eBootstrapService`** — guardian env blank 시 **default creds fallback** · **`guardianStatus`**·staff bootstrap **`guardianEmail`** default align · probe **`defaultGuardianCredentials`** · health **`liveE2eDefaultGuardianCredentials`**. FAQ **Q391 갱신·Q428 신규**.

**224차 transport roster planned pickup hub·QA-B132 StaffLifecyclePanel test (`e35efb2`/`101aaee`)**: FE **`TransportPage`** — **`loadConfirmedRunDispatchIndex`** — 확정 루트 상세 병렬 조회 · 명단 **「배차 루트」**·**「계획 픽업/하차」**·**지연** Badge (Q433) · **`transportRosterDispatch.test`** · **`TransportPage.test`**. **`StaffLifecyclePanel.test`** — FAQ21806 **7일 신규교육** deadline mock (Q434). FAQ **Q433·Q434**.

**231차 G21 RFID compare UI·visit check-in guard·L02_M07 normalization (`27c9de3`/`0db1e68`/`4a47675`)**: FE **`VisitRfidDiffComparePanel`** on **`/visits`** — multipart plan·RFID xlsx · COMP_01~09 chips · diff table (Q452) · BE **`validateAssignedUserForCheckIn`** — assigned user inactive·branch guard at check-in/out (Q453) · FE **`BodyRestraintRecordPage`** snake_case·`items[]` normalization (Q454). FAQ **Q452·Q453·Q454**.

**230차 UXD-130 driver signature a11y·live E2E guardian suite gate·G21 RFID compare API (`bfe0283`/`7424c30`/`eeac205`)**: FE **`TransportServiceLogPanel`** — **`fieldset`「운전자 서명」**·**「서명 성명」/「서명일」**·**`ds-transport-log__*` CSS** (Q450) · **`liveGlobalSetup`** — global skip = backend **reachable·ready** only — guardian-only suites when staff auth absent (Q451) · BE **`POST /api/v1/visits/imports/rfid/compare`** — COMP_01~09 diff matrix (Q452). FAQ **Q450~Q452**.

**229차 live E2E bootstrap error blockers·L02_M13 meal assistance client normalization (`d7f1a9a`/`1c8f236`)**: BE **`HealthController`**·**`LiveE2eController`** — **`bootstrap=error`**·**`guardian-bootstrap=error`** 시 **`operationBlockers`** 에 **`staff-bootstrap-error`**·**`guardian-bootstrap-error`** (Q448) · FE **`MealAssistanceRecordPage`** — **`normalizeClient`** snake_case·`items[]` (Q449). FAQ **Q448·Q449**.

**228차 G15 driver signature·service-log legal guide·live E2E operationBlockers list (`bc3a35c`/`f51e365`/`0df6902`/`c5dd4f2`)**: BE **V154** driver signature · **`validateDriverSignature`** (Q445) · **`operationBlockers[]`** probe·health (Q447) · FE **`TransportServiceLogPanel`** driver signatory fields · **`TransportServiceLogLegalGuide`** on **`/transport/compliance`** (Q446). FAQ **Q445~Q447**.

**227차 G15 server legal field guard·staff health checkup HR file hub wire (`ac1d43f`/`b6ce301`)**: BE **`TransportService.validateServiceLogStopRecords`** — incomplete legal fields·dropoff-before-pickup **`422`** (Q443) · FE **`StaffHealthCheckupsPage`** — **`StaffHealthCheckupRecordsPanel`** 이력 Modal·**「서류 업로드」** HR 파일함 deep link (Q444). FAQ **Q443·Q444**.

**226차 G15 service log legal field guard·duplicate rejection·probe operation readiness·L02_M13 malformed API (`b4644e8`/`52e3340`/`40ef105`/`38642e2`)**: FE **`TransportServiceLogPanel`** — **`validateServiceLogRecords`** — 저장·인쇄·다운로드 전 **법정 필드 필수** (Q439) · BE **`validateServiceLogStopRecords`** — duplicate **`clientId` 422** (Q440) · **`LiveE2eProbeResponse`** — **`operationReady`·`operationBlocker`** (Q441) · **`MealAssistanceRecordPage`** malformed payload Alert (Q442). FAQ **Q439~Q442**.

**225차 staff health checkup new-hire document window·live E2E readiness/retry·QA-B133 DateInput test (`8e6310a`/`2e6c35f`/`a6dfaad`/`40d4284`)**: FE **`StaffHealthCheckupsPage`** — **`staffHealthCheckupCompliance.js`** — **`hiredAt` 병합** · StatCard **「신규 서류 미확인」** · **「신규 서류」** Badge · 첫 검진 **365일 창** 검증 (Q435) · **`staffHealthCheckupCompliance.test`**. BE **`HealthController`** — **default guardian creds → `liveE2eOperationReady` true** (Q437) · **`issueSeedTokensWithRetry`** stale seed **1회 재시도** (Q438) · **`LiveE2eBootstrapLiveApiRoutingE2eTest`** guardian token fields (Q438). FE **`DateInput.test`** — **「오늘」** selector optional (Q436). FAQ **Q435~Q438**.

**223차 QA-B131 live E2E script path·DatePicker keyboard a11y·V153·G15 service log harness (`8882d9f`/`7b8c7b9`/`c8ee85c`/`4c5d3bc`)**: FE **`package.json` `test:live-e2e`** → **`scripts/run-frontend-live-e2e.sh`** (Q429) · **`DatePickerCalendar`** keyboard arrow·PageUp/PageDown·roving tabindex (Q430) · **`liveE2eHarness.test`**. BE **V153** `idx_billing_claims_org_branch_status_paid_at` — G26 입금·수납·의료비공제 **`paid_at DESC`** (Q431) · **`TransportServiceLogLiveApiRoutingE2eTest`** — service-log GET/PUT/audit-trail (Q432). FAQ **Q422 갱신·Q429~Q432**.

**221차 G15 compliance→일지 hub·live E2E bootstrap/probe harden (`b93e098`/`b2c09e1`/`d68c4bf`/`844227a`)**: FE **`TransportServiceLogRunsPanel`** — **`/transport/compliance`** 확정 배차→**`/transport/runs/:runId`** 일지 링크 · **`liveGlobalSetup`** stale refresh token replace·placeholder guardian email hydration · **`liveE2eHarness.test`**. BE **`LiveE2eBootstrapService`** seed branch **`active=true`** · **`LiveE2eController.probe`** **`safeBoolean`** per-field credential check. FAQ **Q426·Q427·Q409 갱신**.

**220차 live E2E nested bootstrap payload (`fc916db`)**: FE **`liveGlobalSetup.js`** — **`pickBootstrapAccessToken`/`pickBootstrapRefreshToken`/`pickBootstrapEmail`/`pickBootstrapClientId`** — flat·nested **`staff`/`guardian`**·snake_case(`access_token`·`client_id`·`guardian_access_token` 등) bootstrap 응답 수용 · embedded guardian token 경로 확장 · **`liveE2eHarness.test`** regression. FAQ **Q409 갱신·Q425**.

**219차 actuator healthz·DateInput/TimeInput QA-B127 (`2157df5`/`ab4de83`/`188ce71`)**: BE **`GET /actuator/healthz`** readiness alias · **`OgadaBackendApplicationTests`** UP·DB-down. FE **`pickerTestUtils.js`** · **`DateInput` `viewAnchor`** · **78 Vitest suites** migrate · **`TransportStopList`** ETA chip Fixed. FAQ **Q413·Q422 갱신**.

**218차 transport settings validation·compact dispatch·V152 committed (`dd2fa2c`/`96db8bf`)**: BE **`BranchTransportSettingsService`** 가중치·픽업 허용분 검증 · **`TransportSuggestService`** BRANCH 정차 포함 · **V152 committed**. FE **`TransportPage`** compact dispatch grid · **`BranchTransportSettingsPanel embedded`** · **`transportSettingsForm.js`**. FAQ **Q347·Q423 갱신·Q424**.

**217차 staff bootstrap guardian tokens·V152 transport guard (`73cffc5`/V152 △)**: BE **`LiveE2eBootstrapResponse`** — optional **`guardianAccessToken`/`guardianRefreshToken`/`guardianEmail`/`guardianUserId`** on staff bootstrap when guardian-client seed ready · **`LiveE2eBootstrapServiceTest`**. **V152** — **`trg_transport_run_stops_guard_client`** `clients.is_active` fix (untracked). FAQ **Q409·Q393·Q423**.

**216차 transport waypoint FE closure·date/time picker·ETA chips·SMTP readiness (`bf73c4c`/`ea5d896`/`704478f`)**: FE **`TransportAddWaypointModal`** Fixed · **`DatePickerCalendar`**·**`TimeInput`** · **`TransportStopList`** ETA time chip·**`--eta-late`**. BE **`NotificationChannelReadinessServiceTest`** SMTP_HOST gap · **V152 △** `is_active` guard. FAQ **Q421·Q422·Q418·Q367**.

**215차 transport WAYPOINT persist·경유지 UI WIP (`de3474d`/FE develop WT)**: BE **V151** `waypoint_address`·`waypoint_label` · **`stopKind=WAYPOINT`** · **`TransportServiceTest`**. FE **`TransportAddWaypointModal`** · **`TransportRouteSplitView`「경유지 추가」** — commit 대기. FAQ **Q421**.

**214차 transport planned departure·live E2E operation readiness·split-view UX (`0e46b37`/`3908044`/`fde098f`)**: BE **V150** `planned_departure_time` · **`TransportRoutePreviewResponse.legDurationsSeconds`** · **`GET /api/v1/health` `liveE2eOperationReady`·`liveE2eOperationBlocker`**. FE **`TransportRunNewPage` 출발 시각** · **`TransportStopList` 예상 도착** · **`TransportRouteSplitView` 세로 stack** · **`TransportPage` AbortController**. FAQ **Q418·Q419·Q420**.

**211차 actuator liveness/readiness·health probe harden·G15 outing live E2E (`30243f7`/`3f32ae5`/`3a0110f`/`b48252a`)**: BE **`ActuatorHealthController`** — **`/actuator/health/liveness`**·**`/readiness`** alias · probe exception **503 graceful**. FE **`clientOutingReportLiveApi.e2e.test.js`** — **`GET /reports/client-outings`** live routing · **`pilotPageFlows.test`** G15 flow. FAQ **Q240·Q413 갱신**.

**210차 L02/L03 parity·actuator health·live E2E deepen (`140bf92`/`5533ef5`/`87f901d`/`5d7be9f`)**: FE **`CareNursingParityPanel`** — care-scoped ↔ L03 nursing report cross-links · **`careNursingReportsLiveApi.e2e.test.js`**. BE foreign-tenant seed UUID **safe client id allocation** · **`GET /actuator/health`** **`LiveReadinessProbe`** alias. FAQ **Q412·Q413·Q409 갱신**.

**209차 G15 audit trail read·cross-tenant bootstrap (`5994d15`/`3cc5a08`/`2d6c063`)**: BE **`GET /transport/runs/{runId}/service-log/audit-trail`** — **`TRANSPORT_SERVICE_LOG_UPSERT`** limit 50 · live E2E **cross-tenant seed ID/email collision guard**. FE **`TransportServiceLogPanel`** **「일지 저장 이력」** · **`fetchTransportServiceLogAuditTrailApi`**. FAQ **Q411·Q409 갱신**.

**208차 G15 audit·monthly reports·probe guard (`aa42b9c`/`6a18dfd`)**: BE **`TRANSPORT_SERVICE_LOG_UPSERT`** audit on service log PUT · **`GET /transport/reports/monthly-service-variation`**·**`monthly-resident-status`** (2-7/2-8) · probe **`resolveSeedClientId`** guard (`0b5657a`). FE **`TransportServiceLogPanel`** archive·audit UX · **`TransportMonthlyReportsPage`** **`/reports/transport-monthly`**. FAQ **Q410·Q411·Q409 갱신**.

**207차 QA-B95 bootstrap fallback·guardian token reuse (`c13800c`/`af4d7f8`)**: BE **`LiveE2eBootstrapService.ensureClientWithFallback`** — reused dev DB **`LIVE-E2E-0001`** insert 충돌 시 동일 tenant·지점 **기존 이용자 재사용** · **`LiveE2eBootstrapServiceTest`**. FE **`liveGlobalSetup.applyBootstrapTokens`** — staff bootstrap **embedded guardian token** 재사용 · **`bootstrap-guardian` 생략** · **`liveE2eHarness.test`**. FAQ **Q360·Q409**.

**206차 G15 service log API·QA-B119 harness (`0cfa970`/`aaaeb10`/`7a4b310`/`b69c8ae`)**: BE **`GET/PUT /api/v1/transport/runs/{runId}/service-log`** — **V148** compliance columns · **`TransportTimeComplianceTest`** · **`TransportServiceTest`**. FE **`TransportServiceLogPanel`** — **`fetchTransportServiceLogApi`/`upsertTransportServiceLogApi`** · **`TransportServiceLogPanel.test`**. **`liveE2eHarness.test`** — stale shell **`LIVE_E2E_*`** env isolation (QA-B119). FAQ **Q407·Q408·Q236**.

**205차 health seed metadata·staff clientId·QR a11y (`2926287`/`8a1f342`/`825c6b0`/`99f2f3e`)**: BE **`GET /api/v1/health`** — **`liveE2eClientReady`·`liveE2eSeedClientId`** · probe seed client before guardian (`8a1f342`) · **`HealthControllerTest`**. FE staff bootstrap **`clientId`** before guardian auth (`825c6b0`) · **`QrCheckinTargetsPanel`** US-E04 a11y (`99f2f3e`). FAQ **Q360·Q393·Q405·Q406**.

**204차 staff clientId·login fallback·pilot stabilize (`440ed84`/`d8d51a7`/`ddd4489`/`6f2a4eb`)**: BE staff bootstrap **`LiveE2eBootstrapResponse.clientId`** · **`ensureClient`** · probe **`clientReady`/`seedClientId`** · **`LiveE2eBootstrapLiveApiRoutingE2eTest`**. FE **`liveGlobalSetup.js`** bootstrap failure **login fallback** · **`pilotLivePages.e2e.test.jsx`** **`AuthProvider` passthrough** — **`npm run test:live-e2e` 118 passed / 0 errors**. FAQ **Q360·Q393**.

**203차 guardian bootstrap deepen (`22396e0`/`b1a6aff`/`4e99ae1`)**: BE **V147** — guardian link trigger **`updated_at ≥ created_at`** · **`LiveE2eBootstrapService`** legacy onboarding row reuse. FE **`liveConfig.resolveGuardianClientId`** — stale **`LIVE_E2E_CLIENT_ID`** vs guardian-linked client. FAQ **Q360·Q393**.

**198차 Kakao map instance refactor + SideNav dedup (`5ebaade`/`7ac0a46`)**: FE **`kakaoMapInstance.js`**·**`useKakaoMap`**·**`KakaoBareMap`** — 지도 인스턴스 중앙화 · **`KakaoTransportMap`** seed markers·SDK 미설정 **Alert** · **`KakaoTransportMapView`** **`mapEnabled`**·canvas **`role="application"`** · **`navConfig.js`** L02_M14 **`/nursing/service`** 중복 제거 · **`kakaoMapInstance.test`**. FAQ **Q370·Q394·Q395**.

**197차 Kakao Maps JS SDK preview + role-mismatch seed guard (`b000d92`/`7ac0a46`)**: FE **`loadKakaoMapSdk.js`** + **`KakaoTransportMapView.jsx`** — SVG fallback 제거 · **`pickupLat`/`pickupLng`** 정차 좌표 · **`KakaoTransportMap.test.jsx`**. BE **`LiveE2eBootstrapService.resolveScopedEmailMatch`** — bootstrap email fallback **expected role code** 한정 (`7ac0a46`). FAQ **Q370·Q393·Q394**.

**196차 guardian bootstrap (`f5205e3`/`b3bd0cc`/`ec142db`)**: BE **`POST /api/v1/system/live-e2e/bootstrap-guardian`** — guardian user·linked client·primary mapping seed · probe **`guardianReady`·`guardianBootstrapEndpoint`**. FE **`liveGlobalSetup.js`** — guardian env absent → bootstrap-guardian → **`/auth/me` probe**. **`ec142db`** — staff bootstrap **onboarding `openedOn`** seed + **`CareNursingReportsLiveApiRoutingE2eTest`** 등 routing harness 3종. FAQ **Q393·Q360·Q389**.

**189차 live E2E harden (`64f6753`/`aa6816a`)**: FE **`64f6753`** — **`liveConfig.js`**·**`liveGlobalSetup.js`** — **non-empty creds = configured** · login probe로 유효성 검증 (example default creds도 probe 통과 시 실행). BE **`aa6816a`** — **`ProductionSecretValidator`** — **`prod` 에서 live E2E bootstrap flags ON 시 기동 거부** · **`LiveE2eBootstrapResponse`** 평문 **password 제거** (FAQ **Q384**).

**194차 live E2E bootstrap fix (`304bb2a`/`f6f1756`)**: BE **`GlobalExceptionHandler`** — `ResponseStatusException` → **선언 HTTP status**(500 방지) · **`LiveE2eBootstrapService`** — `LIVE_E2E=1` env 조건 정렬 · **`LiveE2eControllerRoutingTest`** — disabled bootstrap **`503`** regression · **`GlobalExceptionHandlerTest`**. staff bootstrap **HTTP 500** 회귀 해소 — bootstrap enabled 상태에서 **`./scripts/run-live-e2e.sh`** RUN 확인 (FAQ **Q360·Q389**, QA-B95 잔여).

**186차 live E2E harden (`92ae60b`/`e10113f`)**: BE **`G26StatisticsReportsLiveApiRoutingE2eTest`** — G26 medical-deduction·copay-monthly **2 endpoint 동시** routing harness · invalid `taxYear`/`year` **`422`**. FE **`e10113f`** — **`liveGlobalSetup`**·**`loadLiveE2eEnvFiles`** — `scripts/dev-live-e2e.env` 내 **`export KEY=...`** · **`${VAR:-default}`** shell 구문을 Node에서 직접 파싱 (shell `source` 없이 Vitest globalSetup만으로 creds 로드).

**185차 live E2E harden (`472cb1d`/`9006a53`)**: BE **`LiveE2eBootstrapService`** — 시드 이메일이 **다른 Organization** 에 존재할 때 user **org 재할당 금지** (cross-tenant collision regression). FE **`9006a53`** — **`liveGlobalSetup`**·**`liveConfig.js`** — probe **`skipped`** 플래그 persist · setup이 skip으로 표시한 run에서 authenticated suite **실행 차단** · **`liveE2eHarness.test`**.

**181차 live E2E preflight (`a25c9de`)**: **`GET /api/v1/system/live-e2e/probe`** 응답에 **`organizationReady`·`branchReady`·`userReady`·`mappingReady`** 구조화 플래그가 추가되었습니다. bootstrap 실패 시 `detail` 문자열 파싱 없이 어떤 시드 컴포넌트가 누락됐는지 확인할 수 있습니다 (FAQ **Q360**).

**178차 live E2E preflight (`221bde7`/`3a14caf`/`4299914`)**: **`GET /api/v1/system/live-e2e/probe`** — 인증 없이 bootstrap enabled·ready·status/bootstrap endpoint 경로 확인 (`221bde7`). bootstrap 비활성 시 **`ready=false`·`detail=bootstrap=disabled`** (`a06a29a`). **`3a14caf`** — workspace `scripts/dev-live-e2e.env`·`.example` 자동 source. **`4299914`** — auth probe 실패 시 FAIL 대신 SKIP.

**177차 live E2E preflight (`61141a6`/`15b09df`)**: **`61141a6`** — `npm run test:live-e2e`가 `git rev-parse --show-toplevel`·`../../scripts` 폴백으로 env 파일을 탐색합니다. **health probe harden** (`e4c240f`) — null profile·비-DataAccess 오류 시 **503 안전 폴백**.

**176차 live E2E preflight (`e6944f1`/`7faccbd`/`1fd1434`)**: Vitest **`globalSetup`**(`liveGlobalSetup.js`)이 suite 시작 전 **`GET /api/v1/health`** readiness를 1회 호출합니다. `ready=false` 또는 **ECONNREFUSED** 이면 live suite 전체가 **SKIP** 됩니다. **추가로** `LIVE_E2E_EMAIL`/`PASSWORD`·`LIVE_E2E_CLIENT_ID`·guardian creds가 없거나 **placeholder** 이면 authenticated suite만 **SKIP** — FAIL 대신 (FAQ **Q360**). **`e6944f1`** 에서 staff/guardian **로그인 probe** 실패 시에도 SKIP 합니다. **`pilotPageFlows`** 및 L02 live harness는 **`6f53978`** 에서 deepen 되었습니다. 백엔드는 DB 연결 실패 시 **503** + `ready: false` + `databaseStatusDetail: SELECT_1_FAILED` 를 반환합니다 (`6bd16b9`/`8b7e476`). **liveness** 확인만 필요하면 **`GET /api/v1/health/ping`** (`df14e15`)을 사용합니다.

**`dev-live-e2e.env` 파일 자체가 없으면** live E2E suite가 **FAIL/skip** 될 수 있습니다 (QA-B95 Planned).

```bash
# 루트에서 일괄 실행 (권장)
./scripts/run-live-e2e.sh

# 또는 프론트엔드 package script (env auto-source; QA-B131 `8882d9f` — repo root scripts/ 위임)
cd src/frontend && npm run test:live-e2e

# 개별 harness
./scripts/run-live-e2e.sh src/e2e/careProvisionRecordDispatchLiveApi.e2e.test.js
./scripts/run-live-e2e.sh src/e2e/monitoringLiveApi.e2e.test.js
./scripts/run-live-e2e.sh src/e2e/branchLiveApi.e2e.test.js
./scripts/run-live-e2e.sh src/e2e/needsAssessmentComplianceLiveApi.e2e.test.js
./scripts/run-live-e2e.sh src/e2e/transportLiveApi.e2e.test.js
```

```bash
cd src/frontend
LIVE_E2E=1 \
LIVE_E2E_EMAIL=hq@pilot.example \
LIVE_E2E_PASSWORD='********' \
VITE_API_BASE=http://127.0.0.1:8080 \
npx vitest run --config vitest.live.config.js src/e2e/transportLiveApi.e2e.test.js
```

| 변수 | 용도 |
|------|------|
| `LIVE_E2E=1` | live E2E 활성화 (미설정 시 skip) |
| `LIVE_E2E_EMAIL` / `LIVE_E2E_PASSWORD` 또는 `LIVE_E2E_ACCESS_TOKEN` | staff JWT 세션 |
| `VITE_API_BASE` | API 베이스 (기본 `http://127.0.0.1:8080`) |
| `VITE_ENABLE_PILOT_FIXTURE` | `true` 시 **`PilotFixturePanel`** 표시 (운영 기본 **미설정** — FAQ Q268, `c89a82b`) |
| `LIVE_E2E_WRITE=1` | **US-T02**·**G17/G32** mutating flow — DRAFT 배차·기능회복 계획·사례관리 회의록 생성 (기본 **off**) |

**US-T01** roster · **US-T03** runs list/detail은 read-only. **`programComplianceLiveApi.e2e.test.js`**(BNK-103) — G17/G32/G33 compliance **read-only** + `LIVE_E2E_WRITE=1` 시 plan/meeting write. **`leadCaregiverWorkLogLiveApi.e2e.test.js`**(`479e064`, BNK-127) — G34 lead caregiver work log **live API harness** · **`riskAssessmentLiveApi.e2e.test.js`**(`0ce04ad`) — G40/G40b **live API harness** — merge 후 **`scripts/run-live-e2e.sh`** 실행 권장 (결정 96). **US-T02** write flow는 roster에 이용자가 있어야 하며, 실패 시 DB에 DRAFT run이 남을 수 있으므로 **스테이징 전용**으로 사용하세요.

스테이징 스모크: JWT 로그인(빈 이메일·비밀번호 시 **필드 오류** 표시 확인, Q190) → **`/dashboard`**·**`/dashboard/hq`** — NHIS 대기·미매칭 집계(Q183) · **Recharts**(Q118) → **`/clients`** — 보호자·지역·나이 열(Q191) → **`sysadmin` `/settings`** — 백업·감사·로그인 이력 탭(Q121) · **비밀번호 변경·재설정**(Q122·Q126) → SideNav **운영 → 직원 관리**(`/staff`) — 등록 모달 **fieldErrors**(Q190) → SideNav **기록 → 건강 기록** → 바이탈/투약/**낙상·특이사항** 저장 → **`/health/:clientId`** — **HealthTrendChart** + 표(Q119) → **`/attendance/stats`** — 월별 막대 차트(Q118) → SideNav **청구 → 청구대장**(`/billing/reports/charges`) — **StatCard** 요약·표·인쇄(Q179) → **`/billing/imports/nhis`** — **year-coverage** 배너·25칸 미완비 업로드 차단(Q260) → `/billing/imports/nhis/:batchId` **StatCard·`NhisPendingReviewGuide`**(Q182) · **`UNMATCHED` 후보 검색**(Q135) → **`DISCREPANCY` 「비교」 Modal** → Swagger **`PATCH /clients/{id}`** — `usesTransport`·픽업 주소(Q166) → SideNav **이동 → 배차·이동경로** — roster·confirm·unconfirm(Q159·Q163) · **G15 계약서 저장**(Q230·Q231) · **별지 제18호 안내**(Q237) · 확정 루트 **`TransportServiceLogPanel`** **일지 저장·인쇄**·시간 준수(Q236·Q407) → SideNav **기록 → 식사·프로그램** — **`MealMenuForm`·`ProgramScheduleForm`**(Q161) → **`HOME_VISIT` 지점 `/visits`** — **`VisitNhisImportPanel`** xlsx 업로드(Q189) · **페어 체크인 동기화**(Q238) → `/guardians` **보호자 초대** → SideNav **청구 → CMS 자동이체**(`/billing/cms`) — 등록·**CONFIRMED** 청구 CMS 출금 stub(Q207·Q208) → 청구 **`PAID`** 후 **알림 이력**(Q152·Q187) → **`guardian` `/guardian`** **「명세·청구」 더 보기**(Q192) · **「일일 기록」** 식사 행(Q188) — FAQ Q154·Q107·Q112·Q165.

---

## 4. 프로덕션 환경변수·시크릿

### 4-1. 원칙 (rules.md §3)

- 비밀값은 **환경변수** 또는 **시크릿 매니저**(AWS Secrets Manager, GCP Secret Manager, HashiCorp Vault 등)로만 관리합니다.
- `.env`·키 파일·인증서를 **Git에 커밋하지 않습니다**.
- 스테이징·프로덕션 키를 **절대 공유하지 않습니다**.
- `PII_ENCRYPTION_KEY` 변경 시 **기존 암호화 데이터 복호화 불가** — 키 로테이션 절차(§8-3)를 따릅니다.

### 4-2. 프로덕션 필수 변수

| 변수 | 설명 | 프로덕션 값 예시 |
|------|------|-----------------|
| `DB_URL` | Managed PostgreSQL 엔드포인트 | `jdbc:postgresql://db.internal:5432/ogada?sslmode=require` |
| `DB_USERNAME` / `DB_PASSWORD` | DB 자격증명 | 시크릿 매니저 참조 |
| `JWT_PRIVATE_KEY` / `JWT_PUBLIC_KEY` | RSA PEM (멀티 인스턴스 시 **동일 키** 필수) | 시크릿 매니저 |
| `JWT_ISSUER` | 공개 API URL | `https://api.ogada.example.com` |
| `PII_ENCRYPTION_KEY` | AES-GCM Base64 32바이트 | 시크릿 매니저 |
| `QR_TOKEN_SECRET` | QR HMAC 키 | 시크릿 매니저 |
| `SERVER_PORT` | 컨테이너 내부 포트 | `8080` |

### 4-3. 알림 중계 (J03, 선택 — FAQ Q148)

| 변수 | 설명 | 기본값 |
|------|------|--------|
| `NOTIFICATION_PROVIDER` | `stub`(dev) 또는 `solapi`(live) | `stub` |
| `SOLAPI_API_KEY` / `SOLAPI_API_SECRET` | Solapi API 자격증명 | (빈 값 — stub) |
| `SOLAPI_SENDER_ID` | 발신 번호 | — |
| `KAKAO_PF_ID` | 카카오 비즈니스 채널 PF ID | — |
| `SOLAPI_BASE_URL` | Solapi API 엔드포인트 | `https://api.solapi.com` |
| `KAKAO_TPL_ATTENDANCE_ARRIVAL` 등 | 내부 템플릿 코드 → Solapi 템플릿 ID | 내부 코드명 |
| `KAKAO_TPL_BILLING_PAYMENT` | **`BILLING_PAYMENT_RECEIVED`** — `CONFIRMED`→`PAID` 수납 알림 (`52e0621`, Q159) | `BILLING_PAYMENT_RECEIVED` |

> **stub** 환경에서는 `notifications` DB 이력만 생성되고 외부 발송은 없습니다. **email** 기본값 **`NOTIFICATION_EMAIL_PROVIDER=stub`** — **`StubEmailProvider`** 로 로그·DB 이력만 기록(Q204). **live SMTP** — §4-8. 프로덕션 전 Solapi 템플릿·발신번호 사전 등록이 필요합니다.

> **발신번호 본인인증 (Q654, G-COMM-CALLER-AUTH P3)**: ogada는 **`SOLAPI_SENDER_ID` env 값을 읽어 발송**할 뿐, **발신번호 등록·본인인증 workflow는 제공하지 않습니다**. live SMS·알림톡 전 **Solapi 콘솔**에서 해당 번호를 **사전 인증**하세요. placeholder·미인증 번호는 **`liveAlimtalkDispatchReady=false`** 또는 Solapi API 오류로 이어질 수 있습니다 (Q644·Q318). 자세한 운영 FAQ — **Q654**.
>
> **readiness 점검 (`de25b3e`·`19ffa84`, FAQ Q367·Q644)**: **`GET /api/v1/notifications/channel-status`** 응답 **`readinessBlockers[]`** 로 live 전환 전 누락 항목을 확인합니다 — `ALIMTALK_PROVIDER_NOT_SOLAPI` · `MISSING_SOLAPI_CONFIG` · `MISSING_TEMPLATE_MAPPING` · `EMAIL_PROVIDER_NOT_SMTP` · `MISSING_SMTP_CONFIG`. **placeholder marker**(`stub`·`default`·`placeholder`·`change-me`·`changeme`·`replace-me`)가 **Solapi key/template에 포함되면 live-alimtalk ready=false** (Q644). 비밀값은 노출하지 않습니다.
>
> **기동 검증 (`18ee9b6`·`98e40a3`·`19ffa84`)**: `NOTIFICATION_PROVIDER=solapi` 선택 시 **`SOLAPI_API_KEY`·`SOLAPI_API_SECRET`·`SOLAPI_SENDER_ID`·`KAKAO_PF_ID` 누락** · **`KAKAO_TPL_*` 값이 내부 placeholder**(내부 코드명과 동일) · **Solapi credential/template에 placeholder marker 포함**이면 **기동 실패 또는 live-alimtalk ready=false**입니다. live 전환 전 Solapi 콘솔 **승인 templateId**를 각 `KAKAO_TPL_*`에 매핑하세요 (FAQ Q266·Q644). dev/staging은 **`NOTIFICATION_PROVIDER=stub`** 유지를 권장합니다.

### 4-8. 이메일 발송 SMTP (J03 email, v2 G2 — FAQ Q204)

| 변수 | 설명 | 기본값 |
|------|------|--------|
| `NOTIFICATION_EMAIL_PROVIDER` | `stub`(dev) 또는 **`smtp`**(live) | `stub` |
| `NOTIFICATION_EMAIL_FROM` | 발신 From 주소 — **유효 이메일 필수** (`f23f15a`) | `no-reply@ogada.local` |
| `NOTIFICATION_EMAIL_REPLY_TO` | (선택) Reply-To — 설정 시 형식 검증 | (빈 값) |
| `SMTP_HOST` | SMTP 서버 | (빈 값 — stub) |
| `SMTP_PORT` | SMTP 포트 | `587` |
| `SMTP_USERNAME` / `SMTP_PASSWORD` | SMTP 인증 | (빈 값) |
| `SMTP_AUTH` | SMTP AUTH | `true` |
| `SMTP_STARTTLS_ENABLE` | STARTTLS | `true` |

> **`NOTIFICATION_EMAIL_PROVIDER=smtp`** 시 **`SmtpEmailProvider`** 가 **`JavaMailSender`** 로 plain-text 메일 발송. Kakao/SMS는 **`NOTIFICATION_PROVIDER`**(§4-3)와 **독립**. 보호자 **`users.email`** 미등록·형식 불량 시 **해당 건만 스킵** — 앱 기동은 계속.
>
> **기동 검증 (`5fc44ec`)**: `smtp` 프로바이더 선택 시 **`SMTP_HOST`·`SMTP_PORT` 누락이면 애플리케이션이 기동 실패**합니다 — 잘못된 SMTP 설정으로 **조용히 stub 폴백**되는 것을 방지합니다. dev/staging은 **`NOTIFICATION_EMAIL_PROVIDER=stub`** 유지를 권장합니다.

**지원 템플릿 (`EmailNotificationContent`, `f77a268`)**

| templateCode | 용도 | 트리거 |
|--------------|------|--------|
| `BILLING_STATEMENT` | 급여비용 명세 | `POST /billing/claims/{id}/notify` |
| `BILLING_PAYMENT_RECEIVED` | 본인부담금 수납 완료·**납부확인서** | `POST /billing/claims/{id}/payments`(자동) · **`POST …/payment-receipt-notify`**(수동, Q221) — payload `paidAt`·`paymentMethod` (`588b8e6`) |
| `CARE_PROVISION_RECORD` | 급여제공기록지 | `POST /clients/{id}/notifications/care-provision-record` (Q216) |
| `HOME_NEWSLETTER` | 가정통신문 | `POST /clients/{id}/notifications/home-newsletter` (Q217) |
| `ELDER_ABUSE_PREVENTION_GUIDELINE` | 노인학대예방 및 대응지침 | `POST /clients/{id}/notifications/elder-abuse-prevention-guideline` (Q222) |
| `DAILY_CARE_SUMMARY` | 일일 케어 기록 | 건강 기록 생성 훅 |
| 출석·긴급 | 도착·귀가·EMERGENCY | 출석·사고 기록 훅 |

스테이징 SMTP 스모크:

1. 유효 **`SMTP_*`** + **`NOTIFICATION_EMAIL_FROM`** 설정
2. 보호자 계정에 **`users.email`** 등록 · preference **`channelEmail=true`**
3. **`POST /api/v1/billing/claims/{id}/notify`** (CONFIRMED) 또는 **`POST /clients/{id}/notifications/home-newsletter`** `{ "yearMonth": "2026-06", "summary": "테스트" }` (Q217)
4. **`notifications.channel=email`** · `sent_at` NOT NULL · **`GET /guardian/notifications`** 이력 확인
5. (선택) 실제 수신함에서 `[ogada]` subject·**원화 금액**(`formatWon`) 수신 확인 — **deliverability·SPF/DKIM은 운영자 설정**

### 4-6. CMS 자동이체 (Hyosung FCMS, v2 G2 — FAQ Q206–Q208)

| 변수 | 설명 | 기본값 |
|------|------|--------|
| `FCMS_PROVIDER` | `stub`(dev) 또는 live provider (후속) | `stub` |
| `FCMS_BASE_URL` | 효성 FCMS API 베이스 URL | `https://api.fcms.co.kr` |
| `FCMS_API_KEY` | FCMS API 키 | (빈 값 — stub) |
| `FCMS_MERCHANT_ID` | FCMS 가맹점 ID | (빈 값 — stub) |

> **stub** 환경(`FCMS_PROVIDER=stub`)에서는 **`StubFcmsClient`** 가 member 등록·출금을 **즉시 성공** 시뮬레이션합니다. **`cms_enrollments`·`cms_debit_requests`** DB 이력과 청구 **`PAID`·`payment_method=CMS`** 전환은 정상 동작합니다. **FCMS 응답 금액 ≠ 청구 금액**이면 **`PAID` 미전환**·`FAILED` (`27f20de`, Q256). **실제 은행 출금은 없습니다** (USER_MANUAL §4-6).

> **연말정산**: CMS 수납분은 **`GET …/medical-expense-deduction`** 집계에서 **제외**됩니다 (Q254).

스테이징 CMS 스모크 (stub):

1. **`POST /api/v1/billing/cms/enrollments`** — 연결 보호자·`accountLast4` 4자리
2. 청구 **`CONFIRMED`** · **copay > 0** 확인
3. **`POST /api/v1/billing/cms/claims/{claimId}/debit`** — `cms_debit_requests.status=SUCCEEDED`
4. **`GET /api/v1/billing/claims/{claimId}`** — `status=PAID`, `paymentMethod=CMS`
5. **`GET /api/v1/clients/{clientId}/medical-expense-deduction?taxYear=`** — 해당 CMS 건 **items[] 미포함** (Q254)
6. UI **`/billing/cms`** **CMS 출금** 탭 — 해당 청구 **목록 제외** 확인 (`c0a01b4`)
7. **`DELETE /api/v1/billing/cms/enrollments/{enrollmentId}`** — **ACTIVE** 등록 **해지** · **`GET …/enrollments?clientId=`** — **CANCELLED** 이력 포함 확인 (Q299)
8. **`GET /api/v1/billing/cms/enrollments?branchId=<uuid>&status=ACTIVE`** — **`clientId` 생략** · **`clientName`** 포함 지점 roster (Q637·Q638)
9. UI **`/billing/cms`** **등록 관리** — **이용자 미선택** 시 roster·**FilterChips**·**`BranchScopeNotice`**·**이용자** 열 링크 확인 (Q637·Q638)
10. UI **`/billing/payments`** — **CMS 등록** 열 · **미등록 → CMS 등록** deep link 확인 (Q638)
11. UI **`/billing/cms?clientId=<uuid>`** — 이용자 **자동 선택** 확인 (Q638)
12. UI **`/billing/cms`** **등록 관리** — **해지** Modal → **해지완료** Badge · **재등록** 시 **행 UPDATE**·`created_at` 보존 (Q207·Q299)

**직원 연차휴가 스모크 (G-STAFF-ANNUAL-LEAVE, Q639·Q641·Q642·Q643·Q648·Q649·Q650)**:

1. **`GET /api/v1/staff/annual-leaves/roster?year=2026&branchId=<uuid>`** — **`items[]`·`staffCount`** · **`displayName`·`monthlyUsage[]`·`remaining`** · **`surfaceKind=ANNUAL_LEAVE_USAGE_SNAPSHOT`** · **`relatedSurfaces[]`** 2건 (`bbf333c`, Q648)
2. **`GET /api/v1/staff/annual-leaves/users/{userId}?year=2026`** — **`surfaceKind`·`relatedSurfaces[]`** roster와 동일 (`6ab3760`, Q650)
3. **`GET /api/v1/staff/annual-leaves/roster?year=2026`** — **`branchId` 생략** — JWT **active branch** roster (`6b84bcd`)
4. **`PUT /api/v1/staff/annual-leaves/users/{userId}`** — `{ "year": 2026, "monthlyUsage": [1,0,0,0,0,0,0,0,0,0,0,0], "totalEntitlement": 15, "memo": "테스트" }` — **200 upsert** · 응답 **`surfaceKind`·`relatedSurfaces[]`** (`6ab3760`)
5. (음수) **`monthlyUsage` < 0** → **`422`「월별 사용일수는 0 이상…」** (`a45745c`)
6. (소수) **`monthlyUsage: [0.5, …]`** → **`422`「월별 사용일수는 정수…」** (`f88e8b1`, Q641)
7. (비고) **`memo` 31자** → **`422`「비고는 30자 이하…」** (`6b35fb5`, Q642)
8. (합계) **`monthlyUsage` 합계 > `totalEntitlement`** → **`422`**
9. UI **`/staff/annual-leaves`** — **AppShell `<h1>`「직원 연차휴가」**·**관련 화면 패널** — **「출퇴근 기록」링크**·**「연차·유급휴일 대장 (준비 중)」** (`0b0d7ba`, Q650) · **기준 연도**·roster 표 · **`branch_admin`「수정」Modal** — field error·memo error clear·save **`422`** 표시 확인 (`96e9d25`/`31ab1aa`/`085a85a`, Q646·Q647)
10. UI **`/staff/attendance`** — **「출퇴근 관련 화면」** panel — API **`relatedSurfaces`** 기반 **「연차휴가 현황」→ `/staff/annual-leaves`** · **역방향 cross-link help text** (`95f55aa`, Q651·Q653)
11. **`GET /api/v1/staff/work-attendance?date=&branchId=`** — **`surfaceKind=DAILY_WORK_ATTENDANCE_ROSTER`** · **`relatedSurfaces[]`** 2건 (`83a26e7`, Q653)
10. **`GET /api/v1/health`** — **`v173StaffAnnualLeaveYearlyIntegrityCheckReady=true`** (Q645, `8c5dd65`)
11. **`hq_admin` JWT** — roster **200** · PUT → **403**
12. (staging) **`LIVE_E2E=1 npm test -- staffAnnualLeaveLiveApi`** — roster·yearly live harness PASS (`96e9d25`, Q649)
13. **`pilotChecklist.test`** — **R03e-a/b/c·E05** contract entries (`e296387`, Q649)

**J03 알림 채널 readiness 스모크 (Q644)**:

1. **`NOTIFICATION_PROVIDER=stub`** — **`GET /api/v1/notifications/channel-status`** — **`liveAlimtalkDispatchReady=false`** (정상)
2. placeholder Solapi env(`SOLAPI_API_KEY=stub` 등) — **`liveAlimtalkDispatchReady=false`** · **`readinessBlockers`** contains **`MISSING_SOLAPI_CONFIG`** (`19ffa84`)

### 4-6-1. 본인부담금 간편결제 (7-5, v2 G2 — FAQ Q326–Q329)

| 항목 | 설명 |
|------|------|
| PG | **`StubEasyPayProvider`**(기본) — order+confirm **즉시 성공** · **live PG 벤더** P2 |
| API | **`POST/GET /api/v1/billing/easy-pay/claims/{claimId}/payment`** · **alias `/claims/{claimId}`** (`8f9ad0c`) |
| 수단 | **`CARD`** · **`KAKAO_PAY`** — NFKC·alias 허용 · malformed 거부 (`745a2f6`·`7ec7cd4`·`82054f1`, Q328) |
| DB | **`easy_pay_requests`** (Flyway **V108**) · **`EASY_PAY`** payment_method CHECK · **V109** failed order `pg_order_id` nullable · **V110** composite FK·lifecycle CHECK·active client INSERT guard · **V111** guardian payer link trigger |

> **stub** 환경에서는 **`StubEasyPayProvider`** 가 PG order·confirm을 **즉시 성공** 시뮬레이션합니다. **`easy_pay_requests`** DB 이력과 청구 **`PAID`·`payment_method=EASY_PAY`** 전환은 정상 동작합니다. **전월 미입금·G33 미정산** 시 **`422`** (Q327). **퇴소·비활성 이용자** 신규 INSERT는 **V110** DB 가드로 차단 (Q328). **`guardian_user_id`** 지정 시 **V111** guardian role·client link 검증 (Q332). **실제 카드·카카오 결제창은 없습니다** (USER_MANUAL §4-6).

> **연말정산**: **`EASY_PAY` 수납분은 `GET …/medical-expense-deduction` 집계에서 제외** (Q254).

스테이징 간편결제 스모크 (stub):

1. 전월 **미수납 없음** 확인 — **`GET /api/v1/billing/claims/generation-guard?branchId=&yearMonth=`** · blocked=false (Q310·Q327)
2. 청구 **`CONFIRMED`** · **copay > 0** · **단일 이용자** 확인
3. **`POST /api/v1/billing/easy-pay/claims/{claimId}/payment`** — `{ "provider": "CARD" }` · **`{ "provider": " card " }`** · **`{ "provider": "kakao pay" }`** alias OK (Q328)
4. **`POST …/payment`** — `{ "provider": "card1" }` → **`400 VALIDATION_ERROR`** (malformed)
5. **`GET /api/v1/billing/easy-pay/claims/{claimId}/payment`** · **alias `GET …/claims/{claimId}`** — `status=SUCCEEDED` · `provider=KAKAO_PAY`(canonical)
6. **`GET /api/v1/billing/claims/{claimId}`** — `status=PAID`, `paymentMethod=EASY_PAY`
7. **`GET /api/v1/clients/{clientId}/medical-expense-deduction?taxYear=`** — 해당 건 **items[] 미포함** (Q254)
8. UI **`/billing/easy-pay`** — **전월 미입금 가드 배너**·버튼 비활성 · **필드 오류·결제 상태 `<time>`** (US-L06) 확인
9. (음성) 전월 **`CONFIRMED`** 청구 1건 남긴 뒤 **`POST …/payment`** → **`422`** · UI 가드 배너 표시
10. (J03) **22:00~08:00 KST** — **`/billing/claims/:id`** **「보호자 발송」**·**`/billing/overdue`** **「안내 발송」** 버튼 **비활성** (Q329)

### 4-4. JWT Issuer·CORS

- `JWT_ISSUER`는 실제 API 공개 URL과 일치해야 합니다.
- `SecurityConfig`는 Spring CORS 기본값(`Customizer.withDefaults()`)을 사용합니다. 프로덕션에서는 리버스 프록시 뒤 **동일 오리진** 배포를 우선하고, 별도 도메인 SPA 호스팅 시 허용 오리진을 명시적으로 제한합니다.

### 4-5. 공개 엔드포인트 (인증 불필요)

`SecurityConfig` 기준 permit-all 경로:

| 경로 | 용도 |
|------|------|
| `/api/v1/health` | L7 헬스체크 |
| `/actuator/health` | Spring Actuator 헬스 |
| `/.well-known/jwks.json` | JWT 공개키 배포 |
| `/api/v1/auth/login` | 로그인 |
| `/api/v1/auth/refresh` | 토큰 갱신 |
| `/api/v1/auth/password/reset-request` | 비밀번호 재설정 요청 |
| `/api/v1/auth/password/reset` | 비밀번호 재설정 확인 |

| `/api/v1/guardian/invitations/{token}/accept` | 보호자 초대 수락 (V43, FAQ Q139) |

> 수락 API는 **permit-all**·rate limit·토큰 만료 정책이 적용됩니다. 수락 본문 `phone`은 V44 암호화 저장(Q148).

그 외 `/api/v1/*`는 `Authorization: Bearer <access_token>` 필수입니다 (API_SPEC §0).

### 4-7. 배차 지도·Geocoding·경로 미리보기 (v1.3-A, 선택 — FAQ Q159·Q370·Q394)

| 변수 | 설명 | 기본값 |
|------|------|--------|
| `KAKAO_REST_KEY` | Kakao Local/Mobility REST API 키 — `POST /api/v1/transport/geocode` · `POST …/route-preview` | (빈 값 — geocode·경로 **비활성**) |
| `VITE_KAKAO_MAP_JS_KEY` | Kakao Maps **JavaScript SDK** 키 — 프론트 **`loadKakaoMapSdk`** → **`KakaoTransportMapView`** (빌드 시 주입) | (빈 값 — 지도 **Alert 경고**, 정차 목록은 동작) |

- `application.yml`: `ogada.transport.kakao-rest-key: ${KAKAO_REST_KEY:}`
- **미설정 시**: transport roster·runs CRUD는 동작하나 **지도 SDK·좌표 변환·도로 경로** 불가 — **`KakaoTransportMap`** 이 경고 Alert 표시 (FAQ **Q394**).
- **보안**: REST 키는 **서버 환경변수만** — 프론트에 노출하지 않습니다. JS 키는 **도메인 제한** Web 플랫폼 키를 사용하세요.
- **SDK 로드**: FE **`loadKakaoMapSdk.js`** — `https://dapi.kakao.com/v2/maps/sdk.js?libraries=services&autoload=false` 동적 주입 (`b000d92`). **`kakaoMapInstance.js`**·**`useKakaoMap`** — 지도 인스턴스 1회 생성·재사용 (`5ebaade`, Q395).
- **route-preview**: `hq_admin`·직원 4역할 JWT → `POST /transport/route-preview` `{ branch, stops[] }` — 정차 **`pickupLat`/`pickupLng`** 또는 geocode 좌표 → `path[]`·`distanceMeters`·`durationSeconds` (`e8b8398`). **`POST /transport/runs/suggest`** 응답에도 **`legDurationsSeconds`·`routePath`·`routeDistanceMeters`·`routeDurationSeconds`** 가 포함됩니다 (`e2b764b`, Q554). FE **`KakaoTransportMapView`** — **`mapEnabled=true`** 이후 overlay 렌더 · route-preview **전** 좌표 seed markers · **marker/route layer 분리**·**`pinsOnly`** (`ba74bb5`) · 경로 요약 **`role="status" aria-live="polite"`** · canvas **`role="application"`** (`5ebaade`). route-preview 실패 시 **마커만** 렌더 (SVG fallback **제거**).
- **Kakao API status (Q554)**: **`hq_admin`·`sysadmin`** → `GET /transport/kakao-api-status` — REST 키 설정·Geocode/Directions **probe** · **`quotaUsage[]`** — **Geocode·Directions(단일)·Directions(다중경유)** 각 **usedToday/dailyLimit/remainingToday** (`138ac26`) — **ogada 백엔드 in-memory 카운트**(재기동 시 리셋) · 일일 한도 기본값 **`ogada.transport.kakao-daily-limit-local=100000`** · **`…-navi-directions=10000`** · **`…-navi-waypoints=10000`** · FE **`/settings`「카카오 API」** · **`/organization/settings`「배차·카카오 API」** · **Kakao 콘솔 Quota와 다를 수 있음** · **비밀키 미노출**.
- **스테이징 스모크**: (1) geocode — `POST /transport/geocode` … (2) route-preview … (3) **kakao-api-status** — `GET /transport/kakao-api-status` → `geocodeStatus`/`directionsStatus`=`OK` · **`quotaUsage` 3행** (4) UI — Kakao API 패널 **API별 사용량 테이블** 로드.
- **도메인 오류**: JS SDK load failure — 카카오 개발자 콘솔 → 앱 → 플랫폼 → Web → **접속 origin** 등록 (FAQ **Q394**).

### 4-8. 등급 인정기간·급여계약서 첨부 저장 (G37 BNK-105 · G14 US-T10 — FAQ Q274·Q285)

| 설정 (`application.yml`) | 기본값 | 설명 |
|--------------------------|--------|------|
| `ogada.storage.ltc-grade-attachments.storage-dir` | `./data/ltc-grade-attachments` | PDF/PNG 파일 본체 저장 경로 |
| `ogada.storage.ltc-grade-attachments.max-bytes` | `10485760` (10MB) | 업로드 최대 크기 — V78·V84 CHECK와 동일 |

- **G37 등급 인정기간 첨부**와 **G14 급여계약서 파일함(US-T10)** 은 **동일 스토리지 설정**을 공유합니다 (`BenefitContractAttachmentStorageService` → `LtcGradeHistoryAttachmentProperties`). 디스크 키 prefix만 `benefit-contract-attachments/{orgId}/{clientId}/…` 로 구분됩니다.
- **프로덕션**: API 서버 **영속 볼륨**에 마운트하고 **Tenant manifest 백업**에 포함하세요. DB 행만 복구하면 파일은 유실됩니다.
- **퇴소 purge**: `client_ltc_grade_history`·`client_benefit_contract_attachments` CASCADE로 DB 메타는 제거되나, **디스크 `storage_key` 오브젝트는 별도 배치 삭제** 필요 (`DATA_RETENTION_POLICY` §2-1).
- **권한**: G37·G14 업로드 **`branch_admin`·`social_worker`** (`hq_admin`은 G14 업로드 허용) — `RoleBasedControllerAccessTest$ClientAccess` 회귀.
- **FE 검증**: **`gradeHistoryAttachmentLiveApi.e2e.test.js`** · **`clientLifecycleCompliance` pilot E2E** — `./scripts/run-live-e2e.sh` 선택 실행. MIME 없을 때 **`.pdf`/`.png` 확장자 fallback** (`12d3b7f`).

---

## 5. 빌드·패키징

### 5-1. 백엔드 JAR

```bash
cd src/backend
mvn -DskipTests package
# 산출물: target/backend-0.0.1-SNAPSHOT.jar
```

실행:

```bash
java -jar target/backend-0.0.1-SNAPSHOT.jar
```

### 5-2. 프론트엔드 정적 빌드

```bash
cd src/frontend
npm ci
npm run build
# 산출물: dist/
```

**FE-15 코드 스플릿 (TSR 49, `d484206` 복원)** — Recharts 추가(UXD-48)로 단일 청크 **756 kB** 회귀 후, `vite.config.js` `manualChunks`가 **재적용**되었습니다.

| 산출물 (`dist/assets/`) | 크기 (raw / gzip) | 내용 |
|-------------------------|-------------------|------|
| `react-vendor-*.js` | ~193 kB / 62 kB | React·React Router |
| `index-*.js` | ~208 kB / 51 kB | 앱·라우트·Must UI (UXD-51 포함) |
| `recharts-*.js` | ~367 kB / 101 kB | Recharts·d3 (대시보드·건강 차트) |
| `index-*.css` | ~35 kB / 6 kB | 디자인 토큰·컴포넌트 |

이전 단일 JS **756 kB**(>500 kB vite 경고) 대비 **최대 청크 367 kB** — CDN·브라우저 캐시 효율 개선 (FAQ Q138). Nginx 등 정적 서버는 `dist/assets/*` **전체**를 서빙해야 합니다.

프로덕션 API URL은 빌드 시점에 주입하는 것을 권장합니다 (구현 예정):

```bash
# 권장 패턴 (VITE_ 접두사 — coder 구현 후)
VITE_API_BASE_URL=https://api.ogada.example.com/api/v1 npm run build
```

동일 도메인 리버스 프록시 배포 시 상대 경로 `/api/v1`만 사용해도 됩니다.

---

## 5-1. 프로덕션 시크릿 관리 모범 사례 (2026-06-06 신규)

프로덕션 환경에서는 민감한 정보(DB 비밀번호, JWT 키, PII 암호화 키)를 **코드·환경 설정 파일에 직접 기록해서는 안 됩니다**. rules.md §3 준수:

| 방법 | 권장도 | 설명 |
|------|:-----:|------|
| **환경변수** (` .env` 파일) | ⚠️ | 개발 편의용, 프로덕션에서는 금지 (파일 노출 위험) |
| **OS 환경변수** (`export`) | ⚠️ | 프로세스 환경에만 적용, 다중 서버에서 관리 불편 |
| **클라우드 시크릿 서비스** | ✅ | **권장**: AWS Secrets Manager, GCP Secret Manager, NCP Secure Manager |
| **Kubernetes Secret** | ✅ | **권장**: K8s 환경에서 표준 방식 |

### 프로덕션 시크릿 목록

아래 변수는 **절대 코드·로그에 노출되어서는 안 됩니다**.

| 시크릿 | 용도 | 강도 요건 | 보관 위치 |
|------|------|----------|----------|
| `DB_PASSWORD` | PostgreSQL 접속 | 25자+, 특수문자 포함 | 클라우드 시크릿 서비스 |
| `JWT_PRIVATE_KEY` | JWT 서명 | RSA 2048bit | 클라우드 시크릿 서비스 |
| `JWT_PUBLIC_KEY` | JWT 검증 | RSA 2048bit (공개키 가능) | 코드 또는 `.well-known/jwks.json` |
| `PII_ENCRYPTION_KEY` | 주민번호·연락처 암호화 | AES-256 (32바이트 Base64) | 클라우드 시크릿 서비스 |
| `QR_TOKEN_SECRET` | QR 토큰 서명 | 32바이트 이상 | 클라우드 시크릿 서비스 |

### 클라우드 시크릿 서비스 연동 예시 (AWS 기준)

**1단계: Secrets Manager에 시크릿 저장**

```bash
aws secretsmanager create-secret --name /ogada/prod/db-password \
  --secret-string "$(openssl rand -base64 25)"

aws secretsmanager create-secret --name /ogada/prod/jwt-private-key \
  --secret-string "$(cat jwt-private.pem)"

aws secretsmanager create-secret --name /ogada/prod/pii-encryption-key \
  --secret-string "$(openssl rand -base64 32)"
```

**2단계: EC2/ECS 타스크 역할에 `SecretsManagerReadAccess` 권한 부여**

**3단계: 애플리케이션 시작 스크립트에서 시크릿 가져오기**

```bash
#!/bin/bash
export DB_PASSWORD=$(aws secretsmanager get-secret-value --secret-id /ogada/prod/db-password --query SecretString --output text)
export JWT_PRIVATE_KEY=$(aws secretsmanager get-secret-value --secret-id /ogada/prod/jwt-private-key --query SecretString --output text)
export PII_ENCRYPTION_KEY=$(aws secretsmanager get-secret-value --secret-id /ogada/prod/pii-encryption-key --query SecretString --output text)

cd /opt/ogada/backend && java -jar app.jar
```

### 보안 체크리스트

- [ ] `.env`, `secrets.yml` 등 시크릿 파일이 **Git 저장소에 포함되지 않음** (.gitignore 확인)
- [ ] 프로덕션 클라우드 시크릿 서비스에서 **자동 로테이션** 설정 (90일 권장)
- [ ] 시크릿 접근 시 **IAM 로그·감사 로그** 기록 확인
- [ ] 로그·에러 메시지에서 시크릿 값이 **절대 출력되지 않음** (GlobalExceptionHandler에서 검증)
- [ ] 개발·스테이징·프로덕션 시크릿을 **별도 관리** (크로스 환경 사용 금지)

---

## 6. Docker·컨테이너 배포 (권장 초안)

> 저장소에 Dockerfile이 **아직 없습니다**. 아래는 REQUIREMENTS §1-4「Docker + PostgreSQL 이식 가능 구조」에 따른 **권장 초안**입니다. 인프라 구현 시 `deploy/` 디렉터리로 코드화합니다.

### 6-1. docker-compose.yml (개발·스테이징 참고)

```yaml
services:
  db:
    image: postgres:16-alpine
    environment:
      POSTGRES_DB: ogada
      POSTGRES_USER: ogada
      POSTGRES_PASSWORD: ${DB_PASSWORD}
    volumes:
      - pgdata:/var/lib/postgresql/data
    ports:
      - "5432:5432"
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U ogada -d ogada"]
      interval: 10s
      timeout: 5s
      retries: 5

  api:
    build: ./src/backend
    environment:
      DB_URL: jdbc:postgresql://db:5432/ogada
      DB_USERNAME: ogada
      DB_PASSWORD: ${DB_PASSWORD}
      JWT_PRIVATE_KEY: ${JWT_PRIVATE_KEY}
      JWT_PUBLIC_KEY: ${JWT_PUBLIC_KEY}
      JWT_ISSUER: ${JWT_ISSUER:-http://localhost:8080}
      PII_ENCRYPTION_KEY: ${PII_ENCRYPTION_KEY}
      QR_TOKEN_SECRET: ${QR_TOKEN_SECRET}
    ports:
      - "8080:8080"
    depends_on:
      db:
        condition: service_healthy

  web:
    build: ./src/frontend
    ports:
      - "80:80"
    depends_on:
      - api

volumes:
  pgdata:
```

### 6-2. 백엔드 Dockerfile (권장 초안)

```dockerfile
# src/backend/Dockerfile
FROM eclipse-temurin:17-jre-alpine
WORKDIR /app
COPY target/backend-0.0.1-SNAPSHOT.jar app.jar
EXPOSE 8080
ENTRYPOINT ["java", "-jar", "app.jar"]
```

멀티스테이지 빌드 시 `maven:3.9-eclipse-temurin-17`로 `mvn package` 후 JAR만 복사합니다.

### 6-3. 프론트엔드 Dockerfile (권장 초안)

```dockerfile
# src/frontend/Dockerfile
FROM node:20-alpine AS build
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

FROM nginx:alpine
COPY --from=build /app/dist /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf
EXPOSE 80
```

### 6-4. Nginx 리버스 프록시 (권장)

SPA와 API를 **단일 도메인**으로 서빙하는 `nginx.conf` 예시:

```nginx
server {
    listen 80;
    server_name ogada.example.com;

    # React SPA
    location / {
        root /usr/share/nginx/html;
        try_files $uri $uri/ /index.html;
    }

    # Spring Boot API
    location /api/ {
        proxy_pass http://api:8080;
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }

    location /.well-known/ {
        proxy_pass http://api:8080;
    }

    location /actuator/health {
        proxy_pass http://api:8080;
    }
}
```

프로덕션에서는 **TLS 종료**(Let's Encrypt, ACM, Cloud Load Balancer)를 앞단에 둡니다. REQUIREMENTS §4: **HTTPS 필수**.

---

## 7. 클라우드 배포 패턴 (벤더 무관)

REQUIREMENTS §1-4: AWS / GCP / NCP 등 **벤더 무관**. 공통 패턴만 기술합니다.

### 7-1. 권장 토폴로지

```
[Internet]
    │
[CDN / WAF] (선택)
    │
[Load Balancer] ── TLS 종료
    │
    ├── [Web] Nginx + React dist (또는 S3+CloudFront / GCS+CDN)
    │
    └── [API] Spring Boot × N (오토스케일)
              │
              └── [Managed PostgreSQL] Primary (+ Read Replica, HA)
```

### 7-2. 벤더별 매핑 (참고)

| 역할 | AWS | GCP | NCP |
|------|-----|-----|-----|
| 컴퓨팅 | ECS Fargate / EKS | Cloud Run / GKE | NKS / Server |
| DB | RDS PostgreSQL | Cloud SQL PostgreSQL | Cloud DB for PostgreSQL |
| 시크릿 | Secrets Manager | Secret Manager | Secret Manager |
| 정적 호스팅 | S3 + CloudFront | GCS + Cloud CDN | Object Storage + CDN |
| 백업 | RDS 스냅샷 + S3 | Cloud SQL 백업 + GCS | DB 백업 + Object Storage |

### 7-3. 멀티테넌트 운영 고려

- **단일 DB·단일 스키마** + `organization_id` 행 수준 격리 (현재 구현).
- API 인스턴스는 **무상태(stateless)** — JWT 검증만으로 스케일 아웃 가능.
- `JWT_PRIVATE_KEY`는 모든 API 인스턴스에서 **동일**해야 합니다.
- 파일 업로드(이용자 사진 등) 도입 시 **오브젝트 스토리지** + Tenant별 경로 접두사를 사용합니다.

---

## 8. 데이터베이스 운영

### 8-1. Flyway 마이그레이션

| 버전 | 파일 | 주요 내용 |
|------|------|----------|
| V1 | `V1__init_multi_tenant_schema.sql` | Organization·Branch·User·Client 기본 스키마, `pgcrypto` |
| V2 | `V2__mvp_complement_schema.sql` | MVP 보완 테이블 (보호자·QR·NHIS·청구 라인) |
| V3~V12 | `V3`~`V12` | 인덱스·제약·청구·출석·감사·백업 무결성 |
| V13~V15 | `V13`~`V15` | 건강·copay·QR 도메인, 출석·보존 purge |
| V16~V18 | `V16`~`V18` | 청구 Tenant FK, NHIS 배치 도메인, QR 토큰 값 |
| V19~V20 | `V19`~`V20` | NHIS 대사·백업 종료 상태 무결성 |
| V21~V26 | `V21`~`V26` | NHIS 지점 정렬·Tenant 트리거·청구·출석·보호자 조회 인덱스 |
| V27~V28 | `V27`~`V28` | NHIS·플랫폼·인증·백업 스케줄 조회 성능 인덱스 |
| V29~V31 | `V29`~`V31` | 직원 지점 역조회·사업자번호 검색·이메일 UK·청구 상태·보호자 인덱스 |
| V32~V33 | `V32`~`V33` | actor backstop 트리거·NHIS imported_at·퇴소 purge·활성 이용자 목록 인덱스 |
| V34 | `V34__clients_lifecycle_integrity_and_branch_purge.sql` | 퇴소 시각 ≥ 등록 시각 CHECK, 지점별 `discharged_at` purge 인덱스 |
| V35 | `V35__fee_schedule_qr_actor_backstop_and_guardian_purge.sql` | 수가표·QR `created_by` actor 세션 자동 적재 (V32/V33 패턴 확장) |
| V36 | `V36__clients_billing_temporal_sanity.sql` | 이용자 동의·인정 시작일·청구 `generated_at` temporal CHECK |
| V37 | `V37__attendance_billing_row_lifecycle_and_nhis_query.sql` | 출석·이용자·청구 lifecycle CHECK, NHIS 행 Tenant UK·claimId 인덱스 |
| V38 | `V38__nhis_batch_branch_list_query_index.sql` | NHIS 배치 지점 전체 목록 `(org, branch, created_at DESC)` 인덱스 |
| V39 | `V39__client_guardian_link_status.sql` | `guardian_link_status` (PENDING/LINKED) + 보호자 연결 트리거·미연결 이용자 인덱스 |
| V40 | `V40__branch_name_case_insensitive_unique.sql` | 지점명 **대소문자 무시** Tenant 내 UK — `uq_branches_org_name_lower (organization_id, lower(name))` (V30 이메일 UK 패턴, FAQ Q146) |
| V41 | `V41__guardian_notification_preferences.sql` | 보호자 알림 수신 설정(채널 on/off·`quiet_hours`) — B08 v2 골격 |
| V42 | `V42__guardian_notification_preferences_consent_temporal.sql` | 카카오·SMS on 시 `consent_at` 필수 CHECK, temporal monotonicity — B08 follow-up (FAQ Q142) |
| V43 | `V43__guardian_invitations.sql` | 보호자 이메일 초대 토큰·상태·Tenant 격리 — **Fixed** (FAQ Q144) |
| V44 | `V44__users_guardian_phone.sql` | `users.phone_encrypted`·`phone_masked` — 알림톡/SMS 수신자 (FAQ Q148) |
| V45 | `V45__v2_notification_prefs_integrity_and_users_phone_pair.sql` | phone pair CHECK·notifications `sent_at`·preference Tenant FK·pending 초대 인덱스 (FAQ Q150) |
| V46 | `V46__notification_history_query_index.sql` | `idx_notifications_org_recipient_created` — `(organization_id, recipient_user_id, created_at DESC)` 알림 이력 조회 인덱스 (FAQ Q153) |
| V47 | `V47__transport_v1_3_a.sql` | `clients.uses_transport`·픽업 주소·좌표·`transport_runs`·`transport_run_stops` — v1.3-A 배차 (FAQ Q159) |
| V48 | `V48__client_ltc_grade_history.sql` | `client_ltc_grade_history` — 등급 변동 append-only·`clients.ltc_grade` UPDATE 트리거 (US-M01, API 후속) |
| V49 | `V49__meals_programs_v3_schema.sql` | `meal_menus`·`meal_records`·`activity_programs`·`program_participations` — v3 식사·프로그램 (FAQ Q160·Q161) |
| V50 | `V50__billing_copay_payment_metadata.sql` | `billing_claims.paid_at`·`payment_method`·`payment_recorded_by` — v2 본인부담금 수납 메타·PAID CHECK·상태 인덱스 (FAQ Q174) |
| V51 | `V51__admin_regions_and_branch_profile.sql` | `region_sidos`·`region_sigungus`·`region_dongs` — 행정구역 마스터·`branches.service_type`·`region_dong_code`·`branch_code` (FAQ Q180) |
| V52 | `V52__billing_payment_recorded_by_actor_integrity.sql` | `payment_recorded_by` Tenant FK·PAID actor backstop trigger (FAQ Q174) |
| V53 | `V53__visit_schedules_v2.sql` | `visit_schedules` — PLAN/BILLING 이중 일정·체크인/아웃·상태 5종·4 조회 인덱스 (FAQ Q180) |
| V54 | `V54__nhis_pending_review_status.sql` | `nhis_import_rows` — `PENDING_REVIEW` match_status·`match_status_reason`·pending review partial 인덱스 (FAQ Q181) |

**V27–V54 요약 (2026-06-06~09)**

| 버전 | 주요 내용 |
|------|----------|
| V27 | NHIS import 인정번호·지점 조회, 청구 명세·수가표·Tenant명 검색 인덱스 |
| V28 | 이메일 로그인·비밀번호 재설정 조회, NHIS 배치 행·백업 Tenant 스캔 인덱스 |
| V29 | `user_branches` user_id 역조회, 플랫폼 사업자번호 trigram, 청구 라인 정렬 인덱스 |
| V30 | Tenant `lower(email)` UK, 활성 refresh partial, 직원 `(org, is_active)` 인덱스 |
| V31 | 청구 status+`generated_at` 인덱스, 상태 이력 no-op CHECK, 대표 보호자 partial |
| V32 | `ogada_read_actor_user_id()`, 출석·청구 actor 트리거, NHIS `imported_at` backstop, 퇴소 purge partial |
| V33 | 건강·NHIS actor 트리거, client_id purge 인덱스, 활성 이용자 `(org, branch, created_at)` partial |
| V34 | `chk_clients_discharged_after_created`, `idx_clients_org_branch_discharged_at` (지점별 퇴소 cohort) |
| V35 | `trg_fee_schedules_set_created_by`, `trg_branch_qr_tokens_set_created_by` — 수가 등록·QR 발급 actor backstop |
| V36 | `chk_clients_consent_after_created`, `chk_clients_ltc_cert_valid_from_after_birth`, `chk_billing_claims_generated_after_created` |
| V37 | attendance/clients/billing_claims lifecycle CHECK, `uq_nhis_import_rows_org_id`, `idx_nhis_import_batches_org_branch_claim_created` |
| V38 | `idx_nhis_import_batches_org_branch_created` — `GET /billing/imports/nhis?branchId=` 최신순 |
| V39 | `clients.guardian_link_status`, `trg_guardian_clients_refresh_link_status`, `idx_clients_guardian_link_pending` |
| V40 | `uq_branches_org_name_lower` — Tenant 내 지점명 `lower(name)` functional UK (case-sensitive UK `uq_branch_name_per_org` 제거) |
| V41 | `guardian_notification_preferences` — Tenant+보호자 UK, 채널 5종·방해 금지 시간 쌍 CHECK |
| V42 | `chk_guardian_notification_preferences_*_consent` — 알림톡·SMS on ⇒ `consent_at` NOT NULL; `updated_at`/`consent_at` ≥ `created_at` |
| V46 | `idx_notifications_org_recipient_created` — J03 알림 이력 `(org, recipient, created_at DESC)` 조회 인덱스 (Q153) |
| V47 | `uses_transport`·`transport_runs`·`transport_run_stops`·geocode CHECK·15-stop domain — v1.3-A (Q159) |
| V48 | `client_ltc_grade_history` + `trg_clients_ltc_grade_history` — 등급 변동 이력 (US-M01) |
| V49 | `meal_menus`·`meal_records`·`activity_programs`·`program_participations` — actor backstop·퇴소 가드·UK (Q160) |
| V50 | `billing_claims` copay payment metadata — `paid_at`·`payment_method`·`payment_recorded_by`·PAID CHECK (Q174) |
| V51 | `region_*` tables + `branches.service_type`·`region_dong_code`·`branch_code` (Q180) |
| V52 | `payment_recorded_by` composite FK + PAID actor trigger (Q174) |
| V53 | `visit_schedules` — v2 방문요양 G21 (Q180) |
| V54 | `nhis_import_rows` — G7 `PENDING_REVIEW` + `match_status_reason` (Q181) |
| V59 | `cms_enrollments`·`cms_debit_requests` — CMS auto-debit · `payment_method=CMS` CHECK (Q206) |
| V60 | CMS composite Tenant FK — `fk_cms_enrollments_*_org` · `fk_cms_debit_requests_*_org` (Q207) |
| V61 | `fee_schedules.duration_band`·`clients.duration_band` — G9 EXCLUDE·`uq_fee_schedule_current` 재정의 · CHECK 5밴드 (Q210) |
| V62 | `billing_claim_items.duration_band_snapshot` — 청구 라인 밴드 고정 · BEFORE INSERT backstop · 기존 행 backfill `H10_13` (Q213) |
| V63 | `organizations.claim_generation_basis` — `ATTENDANCE_SCHEDULE` \| `NHIS_IMPORT` CHECK · default 출석 기준 (US-M03, Q224) |
| V64 | `transport_service_contracts` — G15 이용자별 계약서·수칙 5항목·이중 서명 · Tenant+client UK (Q231) |
| V65 | `transport_service_contracts` integrity — `trg_transport_service_contracts_guard_client` · dual-signature CHECK · purge 인덱스 (Q235) |
| V66 | `idx_visit_schedules_org_branch_client_slot_duplicate` — G21 NHIS import duplicate slot lookup (Q234) |
| V67 | `client_outings` — G15 2-1-1 lifecycle · status CHECK · reason non-empty (Q240) |
| V68 | `transport_service_fee_rates`·`transport_service_fee_records` — BNK-25 seed · **1일 1회** UNIQUE (Q239) |
| V69 | `vehicles` · `transport_runs.vehicle_id` FK — plate UK · capacity 1–15 (Q241) |
| V70 | **G15/G16 integrity** — `client_outings`·`transport_service_fee_records`·`vehicles`·`transport_runs` Tenant·지점·활성 이용자 guard · purge 인덱스 (Q246) |

**배포 순서**

1. DB 백업 수행 (§8-2)
2. API 인스턴스 기동 → Flyway 자동 마이그레이션
3. 로그에서 `Successfully applied` 확인
4. `/api/v1/health` 및 핵심 API 스모크 테스트
   - `GET /api/v1/billing/claims?status=CONFIRMED` — 청구 상태 필터 (V31 인덱스)
   - `GET /api/v1/billing/imports/nhis/{batchId}` — NHIS 배치 상세·행 매칭 상태
   - 출석·건강 기록 INSERT 후 `created_by`/`recorded_by` NOT NULL 확인 (V32–V33 트리거)
   - 수가표·QR INSERT 후 `created_by` NOT NULL 확인 (V35 트리거)
   - 이용자 동의·인정 시작일 temporal CHECK 위반 시 INSERT 거부 확인 (V36)
   - `GET /billing/imports/nhis?claimId=` — claimId 필터 (V37 인덱스)
   - `GET /guardian/notification-preferences` — V41 보호자 수신 설정 (guardian JWT)
   - `POST /branches` — 동일 Tenant에 `Test`·`test` 지점명 중복 시 `409` 확인 (V40 UK, FAQ Q146)
   - 카카오·SMS 채널 PUT 후 `consent_at` NOT NULL 확인 (V42 CHECK, FAQ Q142)
   - **V43**: `POST /clients/{id}/guardians/invitations` 발송 → `guardian_invitations` 행·이메일 링크 확인 (FAQ Q144·Q145)
   - **J03**: preference **`channelEmail=true`** 또는 `notifyAttendance=true` → `POST /attendance/check-in` → `notifications` 행·`channel=email|kakao`·`sent_at` NOT NULL (stub, FAQ Q147·Q150·Q204)
   - **J03 이력**: `GET /guardian/notifications` — `items[]` 1건 이상·`channel`·`eventType`·`sentAt` 확인 (FAQ Q152). **UI**: `/guardian` **「알림 이력」** 탭 또는 `/clients/:id` **「보호자 알림 이력」** 카드 (Q187)
   - **V45**: `SENT` notification에 `sent_at` NULL INSERT 거부 확인
   - **V44**: 초대 수락 `phone` 입력 → `users.phone_masked` 표시 확인 (FAQ Q148)
   - **V53**: `POST /visits` on `HOME_VISIT` branch → `DRAFT` row · `DAY_CARE` branch → `422` (FAQ Q180)
   - **V54**: NHIS import 행 with 처리상태 `대기` → `match_status='PENDING_REVIEW'` + non-empty `match_status_reason` (FAQ Q181)
   - **G14**: `GET /clients/{id}/ltc-grade-history` — 등급 변경 후 `items[]` 1건 이상 (FAQ Q176)
   - **V59–V60 CMS**: `POST /billing/cms/enrollments` → `POST /billing/cms/claims/{claimId}/debit` → claim `PAID`·`paymentMethod=CMS` (stub, FAQ Q206–Q208)
   - **V61 G9**: `POST /billing/fee-schedules` with `durationBand: "H10_13"` → 청구 생성 시 밴드별 수가 조회 (FAQ Q210–Q211)
   - **V62 G9**: 청구 생성 후 `GET /billing/claims/{id}` · `items[].durationBandSnapshot` NOT NULL · 보호자 billing 동일 필드 (FAQ Q213)
   - **CMS guard**: 혼합 이용자 청구 `POST /billing/cms/claims/{id}/debit` → `422` (FAQ Q215)
   - **FE 시드 스모크**: `/billing/fee-schedules` — **「공단 2026 수가 시드」** 후 매트릭스 25셀 채움 (FAQ Q214)
   - **V63 US-M03**: `PATCH /settings/billing` `{ "claimGenerationBasis": "NHIS_IMPORT" }` → `GET /settings/billing` 반영 · `GET /billing/claims/generation-guard?yearMonth=` 전월 `CONFIRMED` 존재 시 `blocked=true` (FAQ Q224·Q225)
   - **FE US-M03**: `/billing` **ClaimGenerationGuardBanner** · `/organization/settings` **BillingSettingsPanel** 저장 (Q224·Q225)
   - **BNK-47·51 monthly cap**: `GET /billing/monthly-benefit-caps?year=2026` — **6등급(1~5+인지지원)** cap 반환 · `COGNITIVE_SUPPORT` **676,320** (`20bc1be`) · `GET /billing/claims/monthly-cap-guard?yearMonth=` — `warningCount`·`exceededClients[]` (Q226·Q228)
   - **BNK-49 FE monthly cap UI**: `/billing`·`/dashboard` — **`MonthlyBenefitCapGuardBanner`** 초과 시 `role="alert"` · `/billing/claims/:id` — **`MonthlyBenefitCapBanner`** (Q226)
   - **BNK-48 bank deposit**: `GET /billing/imports/bank-deposits/formats` → 8종 확인 · `POST …/preview` dry-run · `POST /billing/imports/bank-deposits` — 샘플 xlsx + **`branchId`** → `APPLIED`/`UNMATCHED` (Q227·Q572)
   - **G-STAFF-NHIS-EXCEL-IMPORT**: `POST /staff/imports/nhis-caregivers/preview` → `APPLIED` 행 확인 · 선택 `POST …/nhis-caregivers` → `/platform` 승인 대기 (Q573)
   - **BNK-49 FE bank UI**: `/billing/payments` — **`BankDepositImportPanel`** — **「미리보기」·행 선택·「선택 행 등록」** · `branchId` 전송 · `appliedCount` 요약 (Q572·Q227·Q228, `a18b30e`)
   - **G2 SMTP guard**: `NOTIFICATION_EMAIL_PROVIDER=smtp` + `SMTP_HOST` 누락 시 **기동 실패** 확인 (`5fc44ec`)
   - **V64 G15 transport contract**: `PUT /api/v1/transport/contracts/{clientId}` — 5항목·이중 서명 → `GET` 동일 응답 · `fullySigned=true` (Q230·Q231)
   - **V65 contract integrity**: 퇴소·비이동서비스·지점 불일치 저장 거부 · 서명 쌍 CHECK (Q235)
   - **FE G15**: `/transport` **`TransportCompliancePanel`** — 이용자 선택·저장 후 새로고침 시 체크·서명 유지 (Q231)
   - **V66 duplicate import**: 동일 slot NHIS xlsx 재업로드 → 행 `SKIPPED` + duplicate reason (Q234)
   - **V67 outings**: `POST /clients/{id}/outings` → `depart` → `return` · `GET /reports/client-outings?yearMonth=` 1건 (Q240)
   - **V68 G16 service-fee**: `POST /transport/service-fees/generate` — CONFIRMED run 기간 내 DRAFT 생성 · 동일 client+date 재생성 **skip** (Q239)
   - **V69 vehicles**: `POST /transport/vehicles` — plate+capacity · `POST /transport/runs` with `vehicleId` · duplicate plate **422** (Q241)
   - **FE G16 vehicles**: `/transport/vehicles` — **`VehiclesPage`** 등록·수정 · 배차 **`TransportVehicleSelect`** (Q241)
   - **G15 care-provision**: `GET /clients/{id}/care-provision-records/{yearMonth}` — 확정 배차+출석 조인 · FE `/clients/:id` **「급여제공」** 탭 (Q243)
   - **V70 integrity**: 퇴소 이용자 `client_outings` INSERT 거부 · cross-branch `vehicleId` on run 거부 (Q246)
   - **Guardian billing**: `GET /guardian/clients/{id}/billing` — **`DRAFT` 미포함** 확인 (`3def542`, Q212)
   - **G7 NHIS guidance API**: `GET /billing/imports/nhis/guidance` — `message`·`exportSteps[]` 200 (`9a97a1c`, Q111)
   - **NHIS guidance UI**: `/billing/imports/nhis` — **「실서버 안내」** Alert 표시 · guidance API 실패 시 **기존 안내 유지** (`0abf164`, Q133)
   - **G16 cross-branch fee guard**: `PATCH /transport/service-fees/{id}` — **다른 지점** 기록 → `403 FORBIDDEN_SCOPE` (`b5218a9`, Q247)
   - **G2 paidAt**: `PATCH /billing/claims/{id}` status `PAID` — `paidAt`·`paymentRecordedBy` 자동 (`e16534c`, Q244)
   - **FE G16**: `/transport/service-fees` — generate·confirm UI · **`TransportForm18GuidePanel`** 5단계·3분리 신청·등록상태 4단 (`fcf713a`, Q237·Q239)
   - **FE UXD-73**: `/attendance` — **`AttendanceContextNav`** 6탭 전환·`aria-current` (Q242)

**롤백**: Flyway는 **down 마이그레이션 미포함**. 롤백은 **백업 복원** 또는 **수동 역방향 SQL**로 처리합니다. 스키마 변경 PR에는 롤백 시나리오를 함께 기록합니다.

### 8-2. 백업·복구

| 항목 | 정책 (REQUIREMENTS §4, DATA_RETENTION_POLICY §3) |
|------|--------------------------------------------------|
| 주기 | **일 1회** 전체 DB 스냅샷 |
| 보관 | **30일** 롤링 |
| 암호화 | at-rest 암호화 (KMS·환경변수 키) |
| RPO / RTO | 24시간 / 4시간 (인프라 구현 시 확정) |

**수동 pg_dump 예시**

```bash
pg_dump -h <db-host> -U ogada -Fc ogada > ogada_$(date +%Y%m%d).dump
```

**복구 예시**

```bash
pg_restore -h <db-host> -U ogada -d ogada --clean --if-exists ogada_20260605.dump
```

**ogada 내장 스케줄러** (`BackupRunService`, `BACKUP_SCHEDULER_ENABLED=true`)는 `backupEnabled=true`인 Tenant에 대해 manifest 백업을 실행하고 `backup_runs`에 이력을 남깁니다 (V9, V20).

**프로덕션 권장**: Managed PostgreSQL 자동 스냅샷 + `pg_dump`를 주 백업으로 사용하고, ogada manifest는 보조·점검용으로 운영합니다. `sysadmin`은 `GET /settings/backups`로 이력을 확인합니다.

### 8-3. PII 암호화 키 로테이션

`PII_ENCRYPTION_KEY` 변경은 **재암호화(re-encrypt) 배치** 없이는 기존 데이터를 읽을 수 없습니다.

권장 절차:

1. 유지보수 창구 공지
2. 전체 DB 백업
3. 새 키로 **컬럼 단위 재암호화** 배치 실행 (별도 스크립트·마이그레이션)
4. 애플리케이션 환경변수를 새 키로 전환
5. 검증 후 구 키 폐기

운영 전까지 키 변경 빈도는 **연 1회 이하**를 권장합니다 (`ADMIN_GUIDE.md` §4-6).

---

## 9. 모니터링·헬스체크

### 9-1. 헬스 엔드포인트

| URL | 용도 | LB 프로브 |
|-----|------|----------|
| `GET /api/v1/health/ping` | **Liveness** — 프로세스 생존 (DB probe 없음) | ✅ 권장 (liveness probe) |
| `GET /api/v1/health` | **Readiness** — 애플리케이션 UP/DOWN + **DB readiness** | ✅ **권장** (`ready` 필드 사용) |
| `GET /actuator/health` | Spring Actuator alias — DB readiness **`UP`/`DOWN`** | ✅ |
| `GET /actuator/healthz` | **`/actuator/health`·`/readyz`와 동일** — DB readiness (`2157df5`, Q413) | ✅ k8s/LB readiness |
| `GET /actuator/health/liveness` | Actuator liveness — **프로세스 도달성** · **항상 `UP`** (`911a1b9`, Q413) | ✅ k8s liveness |
| `GET /actuator/livez` | **`/actuator/health/liveness`와 동일** (`c19206a`, Q413) | ✅ k8s liveness |
| `GET /actuator/health/readiness` | Actuator readiness — **DB probe** (`911a1b9`, Q413) | ✅ k8s readiness |
| `GET /actuator/readyz` | **`/actuator/health/readiness`와 동일** (`c19206a`, Q413) | ✅ k8s readiness |
| `GET /.well-known/jwks.json` | JWT 키 배포 확인 | 진단용 |

**`GET /api/v1/health/ping` 응답 (174차, `df14e15`)** — DB 연결 없이 항상 HTTP 200:

```json
{"status":"UP","service":"ogada-backend","timestamp":"2026-06-16T00:45:00+09:00"}
```

**`GET /api/v1/health` 응답 (175차, `8b7e476`)**:

| 필드 | 정상 (HTTP 200) | DB 장애 (HTTP 503) |
|------|----------------|-------------------|
| `status` | `UP` | `DEGRADED` |
| `ready` | `true` | `false` |
| `databaseStatus` | `UP` | `DOWN` |
| `databaseStatusDetail` | `SELECT_1_OK` | `SELECT_1_FAILED` · probe exception 시 **`SELECT_1_FAILED_PROBE_EXCEPTION`** (`3f32ae5`, Q413) |
| `service` | `ogada-backend` | 동일 |
| `activeProfiles` | 배열 | 동일 |
| `timestamp`·`checkedAt` | ISO-8601 | 동일 |
| `liveE2eClientReady` | bootstrap enabled 시 **시드 이용자 존재** (`true`/`false`) | bootstrap disabled·오류 시 `false` (`2926287`, Q360) |
| `liveE2eSeedClientId` | 시드 이용자 UUID 문자열 | 미시드·오류 시 `null` (`2926287`, Q360) |
| `liveE2eStaffBootstrapReady` | staff bootstrap **ready + credentials configured** | bootstrap disabled·오류 시 `false` (`3908044`, Q419) |
| `liveE2eGuardianBootstrapReady` | guardian bootstrap **ready + credentials configured (not default) + seed client** | bootstrap disabled·오류 시 `false` (`3908044`/`8fe1ccd`, Q419·Q491) |
| **`liveE2eGuardianStatusDetail`** | `guardian-bootstrap=ready` · `guardian-bootstrap=disabled` · `guardian-bootstrap=error` | guardian bootstrap **human-readable status** (`12d1a7b`, Q515) |
| **`liveE2eG21SeedStatusDetail`** | `g21-seed=applicable visit-schedule=present billing-visit-schedule=present nhis-import=present` · `g21-seed=branch-missing-or-inactive` · `g21-seed=disabled` | G21 seed **3축 진단 문자열** (`12d1a7b`, Q515) — **`operationBlockers[]`와 병행** |
| `liveE2eDefaultGuardianCredentials` | guardian creds가 **시드 기본값**(`live-e2e-guardian@ogada.test`) 사용 중 | env에 명시 creds 설정 시 `false` (`09df8c7`, Q428) — **health·probe 모두** **`guardian-credentials-default` blocker** (`8fe1ccd`/`f932fd3`, Q491·Q490) |
| `liveE2eOperationReady` | **`staffBootstrapReady && guardianBootstrapReady && g21SeedStatus.operationReady()`** — live E2E **운영 가능** 단일 플래그 | bootstrap disabled·오류 시 `false` (`3908044`, Q419) · **default creds 사용 시 health·probe 모두 false** (`8fe1ccd`/`f932fd3`, Q491·Q490) · **G21 seed 미준비 시 false** (`14582bf`/`429661e`, Q495·Q500) · **branch missing/inactive 시 false** (`191703f`, Q502) |
| `liveE2eG21SeedApplicable` | 시드 지점이 **방문요양(`HOME_VISIT`) 계열** 또는 **legacy `DAY_CARE`** 이면 `true` | legacy **`DAY_CARE`** 는 bootstrap **`HOME_VISIT` 승격 전**에도 applicable (Q501, `cc295ec`) · 주야간-only(해당 없음)는 `false` |
| `liveE2eVisitScheduleReady` | resolved **PLAN 방문일정 UUID**가 해당 org에 존재 · **configured `branchId` 소속** | applicable && missing/cross-branch → **`visit-schedule-missing`** blocker (`14582bf`/`02cf036`, Q495·Q507) |
| `liveE2eBillingVisitScheduleReady` | **paired BILLING** 일정 존재 · PLAN과 **`pairedScheduleId` 양방향 연결** · **configured branch 소속** | applicable && missing/mismatch/cross-branch → **`billing-visit-schedule-missing`** blocker (`429661e`/`02cf036`, Q500·Q507) |
| `liveE2eNhisImportReady` | **NHIS import batch + row** 존재 · **row `batchId` = batch `id`** · **batch `branchId` = configured branch** | applicable && missing/mismatch/cross-branch → **`nhis-import-missing`** blocker (`14582bf`/`c0403b0`/`02cf036`, Q495·Q499·Q507) |
| `liveE2eVisitScheduleId`·`liveE2eBillingVisitScheduleId`·`liveE2eNhisImportBatchId`·`liveE2eNhisImportRowId` | bootstrap이 resolve한 G21 시드 ID | **`POST /system/live-e2e/bootstrap`** 응답에도 동일 (`fd275f4`/`429661e`, Q500) |
| `liveE2eG32ComplianceAttendeeOpinionsFieldReady` | **`CaseManagementComplianceResponse`** 에 **`attendeeOpinionsMetCount`** 존재 | false → **`g32-compliance-field-missing`** (`caeac0d`, Q528) |
| `liveE2eG32DashboardAttendeeOpinionGapFieldReady` | **`BranchDashboardResponse`** 에 **`caseManagementAttendeeOpinionGapCount`** 존재 | false → **`g32-dashboard-field-missing`** (`caeac0d`, Q528) |
| `liveE2eG32AttendeeOpinionsArrayCheckReady` | V157 **`chk_case_management_meetings_attendee_opinions_array`** | false → **`g32-v157-constraint-missing`** (`caeac0d`, Q528) |
| **`cashReceiptIdentifierValueCheckReady`** | V159 **`chk_cash_receipt_issuances_identifier_value_format`** | false → **`cash-receipt-identifier-check-missing`** — **health·probe 동기화** (`LiveE2eOperationReadinessSupport`, Q548, `bfad37d`/`4d4457f`) |
| **`v171DefenseInDepthIntegrityCheckReady`** | V171 **5 CHECK/FK** on `staff_work_attendance`·`billing_report_filters` | false → **`v171-defense-in-depth-constraint-missing`** (Q625, `dce9bf1`/`175d9cb`) |
| `liveE2eOperationBlocker` | … · **`g32-compliance-field-missing`·`g32-dashboard-field-missing`·`g32-v157-constraint-missing`** · **`cash-receipt-identifier-check-missing`** · **`v171-defense-in-depth-constraint-missing`** (**health·probe**, Q625) · **`g21-branch-missing-or-inactive`** (**health·probe**, Q505·Q511) · **`bootstrap-disabled`** | QA-B95 preflight 진단 · **health·probe credential/G21/G32/G-CASH-RECEIPT/V171 blocker 집합** (Q525·Q528·Q548·Q625) |
| `liveE2eOperationBlockers` | … · G32 stale → **`["g32-compliance-field-missing", …]`** · V159 missing → **`["cash-receipt-identifier-check-missing"]`** (Q543·Q548) · branch missing/inactive 시 **`["g21-branch-missing-or-inactive"]`** (**health·probe**, Q505·Q511) | **`LiveE2eOperationReadinessSupport.resolveOperationBlockers`** — health·probe **동일 로직** (`bfad37d`) · FE **`liveBackendProbe`** nested/snake_case parse (Q545·Q549, `682d647`/`16afd4c`) |

**readiness + live E2E operation 예** (`ready=true`, bootstrap enabled, HTTP 200):

```json
{
  "status": "UP",
  "ready": true,
  "databaseStatus": "UP",
  "databaseStatusDetail": "SELECT_1_OK",
  "liveE2eClientReady": true,
  "liveE2eSeedClientId": "00000005-0005-4000-8000-000000000001",
  "liveE2eStaffBootstrapReady": true,
  "liveE2eGuardianBootstrapReady": true,
  "liveE2eDefaultGuardianCredentials": false,
  "liveE2eOperationReady": true,
  "liveE2eOperationBlocker": "none"
}
```

**readiness + live E2E seed 예** (`ready=true`, bootstrap enabled, HTTP 200):

```json
{
  "status": "UP",
  "ready": true,
  "databaseStatus": "UP",
  "databaseStatusDetail": "SELECT_1_OK",
  "liveE2eClientReady": true,
  "liveE2eSeedClientId": "00000005-0005-4000-8000-000000000001"
}
```

로드밸런서는 **liveness**(`GET /api/v1/health/ping` · **`GET /actuator/health/liveness`** · **`GET /actuator/livez`**)와 **readiness**(`GET /api/v1/health`, `ready === true` · **`GET /actuator/health/readiness`** · **`GET /actuator/readyz`**)를 분리하세요. **liveness는 DB 장애 시에도 `UP`** 이어야 프로세스가 불필요하게 재시작되지 않습니다 (`911a1b9`, Q413). live E2E harness는 **`ready === true`** (또는 레거시 호환 `status === "UP"` + HTTP 200)일 때만 테스트를 허용합니다. DB만 일시 중단·probe runtime exception 시 **503** 으로 인스턴스를 드레인할 수 있습니다 (FAQ **Q360**·**Q413**).

`management.endpoints.web.exposure.include=health,info` (application.yml 기준).

### 9-2. 로그·알림

| 항목 | 권장 |
|------|------|
| 로그 수집 | stdout → CloudWatch / Cloud Logging / Loki |
| PII | 로그에 주민번호·연락처 **평문 금지** — UUID·마스킹만 |
| 알림 | 5xx 급증, 헬스 실패, DB 연결 실패, 백업 실패 |
| 감사 | `audit_logs` 테이블 + `GET /settings/audit-logs` |

### 9-3. SLA 목표

REQUIREMENTS §4: 가용성 **99.5%** 이상. 월 ~3.6시간 이하 다운타임 허용 범위입니다.

---

## 10. CI/CD 개요

저장소에 파이프라인 정의는 **아직 없습니다**. 권장 단계:

```
[PR] → lint/test (mvn test, npm build)
         │
[merge main] → build JAR + dist
         │
[staging] → Flyway migrate → smoke test (/api/v1/health, POST /auth/login)
         │
[production] → blue-green 또는 rolling deploy → 헬스 확인
```

| 단계 | 검증 |
|------|------|
| 빌드 | `mvn -B test` (31 테스트 클래스, 213 tests), `npm ci && npm test && npm run build` (13 files / 144 tests) |
| 스테이징 | Flyway V1~V42 적용, E2E 로그인·Tenant 격리·청구·NHIS·`primaryGuardian`·V41 notification preferences·V42 consent CHECK·actor backstop·rate limit |
| 프로덕션 | 헬스·JWKS·백업 스케줄·`BACKUP_STORAGE_DIR` 쓰기 권한 확인 |

---

## 11. 배포 후 검증 체크리스트

### 11-1. 인프라

- [ ] HTTPS 인증서 유효, HTTP → HTTPS 리다이렉트
- [ ] `GET /api/v1/health` → `status: UP`
- [ ] `GET /actuator/health` → `UP`
- [ ] `GET /.well-known/jwks.json` → RSA JWK 반환
- [ ] PostgreSQL TLS (`sslmode=require`) 연결
- [ ] 일 1회 백업 스케줄 동작·30일 보관 확인

### 11-2. 보안

- [ ] `JWT_PRIVATE_KEY`·`PII_ENCRYPTION_KEY`·`QR_TOKEN_SECRET`이 시크릿 매니저에만 존재
- [ ] ephemeral JWT 키 **미사용** (로그에 warn 없음)
- [ ] 에러 응답에 스택·DB 스키마 미노출 (API_SPEC §0-3)
- [ ] 공개 엔드포인트만 permit-all, 나머지 401/403 정상

### 11-3. 기능 스모크 (MVP)

- [ ] `POST /api/v1/auth/login` — 테스트 계정 로그인
- [ ] `GET /api/v1/auth/me` — JWT·역할·`organization_id` 확인
- [ ] `platform_admin` — Tenant 생성 E2E (파일럿 전)
- [ ] 테넌트 A 토큰으로 테넌트 B 데이터 접근 **403** 확인
- [ ] `GET /api/v1/care/reports/meal-preference?fromDate=&toDate=&clientId=` — L02_M16 만족도 집계 응답(`totalSurveyCount`·`satisfiedCount`) 확인
- [ ] `GET /api/v1/care/reports/nursing-service?fromDate=&toDate=` — L02_M14 통합 간호제공 집계 응답 확인 (`002e3eb`)
- [ ] `GET /api/v1/care/reports/hospital-visits` · `…/medication-delivery` — L03_M09/M10 care proxy 라우팅·RBAC(`caregiver` 403) 확인
- [ ] **`CareNursingReportsPilotServiceFlowE2eTest`** — care-scoped nursing 3 endpoint delegation·aggregate contracts (`2ba2761`, Q389)
- [ ] `/clients/needs-assessments` — G24b StatCard **FAQ 21800/21810** suffix 표시 (`d499130`, Q391)
- [ ] `/compliance/monitoring` — **`MonitoringEvidenceContextPanel`** FAQ21838 증빙 기간·G24b/G21/G26 cross-link (`7d2cb4a`, Q391)
- [ ] `/billing/reports/statistics` — G26 ① **수납년도/청구년도** segmented control·**「국세청 CSV」** (`19ed7f3`/`ceeaeb9`, Q534)
- [ ] `/billing/claims/:id` — **G-7-1 Excel(CSV) export** row on **`BillingStatementPrintPanel`** (`58d6694`/`e454d3b`, Q535)
- [ ] `/billing/reports/statistics` — G26 ②③ section lede **G30/G24b FAQ cross-ref** (`d499130`, Q391)
- [ ] `/billing/imports/nhis` — 수가표 미완비 시 **`year-coverage.message`** 배너·업로드 차단 동일 문구 (`57114b8`, Q392)
- [ ] **`LiveE2eBootstrapServiceTest`** — staff bootstrap **`ensureClient`** · **`LiveE2eBootstrapResponse.clientId`** (`d8d51a7`/`440ed84`, Q360·Q393)
- [ ] **`GET /api/v1/system/live-e2e/probe`** — **`clientReady`·`seedClientId`** 필드 존재 (`d8d51a7`, Q360)
- [ ] **`LiveE2eBootstrapLiveApiRoutingE2eTest`** — probe/bootstrap contract harness (`440ed84`)
- [ ] FE **`liveE2eHarness.test`** — bootstrap failure **`login-fallback-ok`** (`ddd4489`, Q360)
- [ ] **`pilotLivePages.e2e.test.jsx`** — **`AuthProvider` passthrough** · jsdom race 없음 (`6f2a4eb`, Q360)
- [ ] **`LiveE2eBootstrapServiceTest`** — **legacy onboarding support** row reuse·`organizationId` backfill (`b1a6aff`, Q393)
- [ ] **`ClientEntityTest`** — **V147** guardian link trigger **`updated_at`** 제약 (`22396e0`, Q393)
- [ ] FE **`liveE2eHarness.test`** — **`resolveGuardianClientId`** linked-client 우선 (`4e99ae1`, Q360·Q393)
- [ ] **`guardianLiveApi.e2e.test.js`** · **`pilotLivePages.e2e.test.jsx`** — guardian client resolution·page probe stabilize (`4e99ae1`)
- [ ] `POST /api/v1/system/live-e2e/bootstrap` — bootstrap disabled 시 **`503`**(500 아님, `304bb2a`) · enabled 시 **`200`** 또는 구조화 오류
- [ ] **`GET /api/v1/transport/roster?runDate=&direction=PICKUP`** — 응답 **`contact`·`guardianContact`·`desiredBoardingTime`·`desiredDropoffTime`** · **`hq_admin`** vs 그 외 마스킹 (`114411f`, Q398·Q400)
- [ ] **`GET /api/v1/transport/roster?runDate=&direction=DROPOFF`** — 하차 명단·희망 하차 시각 (`114411f`, Q399)
- [ ] **`POST /api/v1/transport/runs`** — `stops[]` with **`stopKind=BRANCH`** 지점 경유 · **`stopKind=WAYPOINT`** + **`waypointAddress`**·optional **`waypointLabel`** (`de3474d`, Q421)
- [ ] **`TransportServiceTest`** — waypoint geocode persist·주소 없음 reject (`de3474d`, Q421)
- [ ] **`/transport/runs/new`** — **「경유지 추가」** → 주소·표시 이름 입력 · 정차 목록 **`(경유지)`** 라벨 (`bf73c4c`, Q421)
- [ ] **`TransportAddWaypointModal.test`** · **`transportUtils.test`** · **`TransportRouteSplitView.test`** — waypoint payload·modal (`bf73c4c`, Q421)
- [ ] **`LiveE2eBootstrapServiceTest`** — guardian env blank 시 **default creds fallback** · **`guardianStatus`** ready with defaults (`92be918`/`09df8c7`, Q428)
- [ ] **`GET /api/v1/system/live-e2e/probe`** — **`defaultGuardianCredentials=true`** when env guardian creds blank (`09df8c7`, Q428) · **`defaultCredentials=true`** when staff env blank
- [ ] **`GET /api/v1/system/live-e2e/probe`** — **`liveE2eAllowDefaultCredentials`** (또는 probe payload) 확인 · **`ogada.live-e2e.allow-default-credentials=false`** 일 때 default staff/guardian creds → **`operationReady=false`** · **`staff-credentials-default`/`guardian-credentials-default`** blockers (Q490·Q542, `beef81e`) · **기본 `true`** 이면 default creds **허용**
- [ ] **`GET /api/v1/health`** — **`liveE2eAllowDefaultCredentials`** · probe와 **동일 default-creds 규칙** (Q491·Q542)
- [ ] **`LiveE2eControllerTest`** — default staff credentials block operation probe (`f932fd3`, Q490)
- [ ] **`HealthControllerTest`** — default staff/guardian credentials block operation readiness (`8fe1ccd`, Q491)
- [ ] **`LiveE2eBootstrapServiceTest`** — foreign-tenant visit schedule·NHIS seed ID fallback (`54d7f36`, Q492)
- [ ] **`GET /api/v1/health`** — **G21 seed fields** — **`liveE2eG21SeedApplicable`·`liveE2eVisitScheduleReady`·`liveE2eBillingVisitScheduleReady`·`liveE2eNhisImportReady`** + resolved IDs (`429661e`, Q500)
- [ ] **`GET /api/v1/health`** — HOME_VISIT branch · missing visit schedule → **`visit-schedule-missing`** · **`liveE2eOperationReady=false`** (`14582bf`, Q495)
- [ ] **`GET /api/v1/health`** — PLAN only · missing paired BILLING → **`billing-visit-schedule-missing`** · **`liveE2eOperationReady=false`** (`429661e`, Q500)
- [ ] **`GET /api/v1/health`** — legacy **`DAY_CARE`** seed branch → **`liveE2eG21SeedApplicable=true`** until bootstrap upgrade (`cc295ec`, Q501)
- [ ] **`LiveE2eBootstrapServiceTest`** — **`serviceType` padded whitespace trim** before G21 applicable check (`b11e29a`, Q577)
- [ ] **`StaffNhisCaregiverImportServiceTest`** — empty `rowNumbers` → **`422`「선택된 행이 없습니다.」** (`2f6f3bc`, Q576)
- [ ] **`NhisExcelParserTest`** — BOM·whitespace·alias processing-status header normalize (`2edbdc4`, Q582)
- [ ] **`BankDepositImportServiceTest`** — empty·non-positive `rowNumbers` rejection·**invalid rowNumbers vs parsed spreadsheet** (`e3b74a0`·`7d29a38`·`6ed7cd4`, Q576·Q579)
- [ ] **`/billing/payments`** — **`BankDepositImportPanel`** preview·select·import·**UXD-146 a11y** (`a18b30e`·`a7d9a2f`, Q572·Q581)
- [ ] **`liveE2eHarness.test`** — **ignores recovered staff/guardian auth blockers** when auth ready (`9105332`·`06c6bb5`·**`33e9e1a` snake_case**, Q580) · **ignores `*-credentials-default` + wording variant blockers when auth recovered** (`6fcd750`/`a170f9c`, Q640) · **filters unrelated auth blockers by suite contract** (`5f1815f`, Q580 deepen) · **filters feature-scoped blockers** (`cb3fe3d` — G21·G32·cash-receipt·V165 when not required) · **`liveCashReceiptDescribe` suite guard** (`cd6891f`, Q597) · **stale token credential fallback** (`b60c622`, Q583) · **placeholder token bootstrap probing** (`82a542c`, Q578 deepen)
- [ ] **`StaffAnnualLeaveServiceTest.saveYearlyRecordShouldRejectNegativeMonthlyUsage`** · **`validateMonthlyUsageShouldRejectDecimal`** · **`saveYearlyRecordShouldRejectOlongMemo`** · **`getRosterShouldUseActiveBranchWhenBranchIdMissing`** · **`RoleBasedControllerAccessTest.StaffAnnualLeaveAccess`** · **`StaffAnnualLeavePilotServiceFlowE2eTest`** (`6b84bcd`/`a45745c`/`f88e8b1`/`6b35fb5`, Q639·Q641·Q642)
- [ ] **`StaffAnnualLeaveSupportTest`** · **`MustApiEndpointRoutingTest`** — roster·yearly **`surfaceKind`·`relatedSurfaces`** (`bbf333c`/`6ab3760`, Q648·Q650)
- [ ] **`StaffAnnualLeavePage.test`** — isolated **`npx vitest run src/pages/StaffAnnualLeavePage.test.jsx`** **8/8 PASS** · full `npm test` **2049/2049 PASS** (`949e9bf`, Q658) — **QA-B266 Fixed**
- [ ] **develop `@949e9bf` / test SYNCED** — post-merge **2049/2049 PASS** (TSR 1311, Q658)
- [ ] **`StaffAnnualLeaveServiceTest.getRosterShouldUseTenantActiveBranchForMultiBranchScope`** — multi-branch **`branch_admin`**·`branchId` 생략 → **`TenantContext.activeBranchId`** fallback (`40ab9e7`, Q656·Q659)
- [ ] **`/staff/annual-leaves`** · **`/staff/attendance`** — **`BranchScopeNotice`** **「조회 지점」** · API **`resolvedBranchId`** 정합 (`949e9bf`, Q657)
- [ ] **`RelatedSurfacesPanel.test`** — AVAILABLE 링크·PLANNED **`Badge`「준비 중」** · surface별 **`aside` `aria-label`** (`c183ebd`, Q657·UXD-156)
- [ ] **`StaffAnnualLeaveRelatedSurfacesPanel.test`** · **`StaffAnnualLeavePage.test`** — **출퇴근 링크·대장 (준비 중)** panel (`0b0d7ba`/`c183ebd`, Q650·Q657)
- [ ] **`staffAnnualLeaveLiveApi.e2e.test.js`** — US-R03e roster·yearly live harness (`96e9d25`, Q649)
- [ ] **`pilotChecklist.test`** — **R03e-a/b/c·E05** service contract (`e296387`, Q649)
- [ ] **`/staff/annual-leaves`** — **`STAFF_ANNUAL_LEAVE_PAGE_TITLE`** AppShell `<h1>`·**`pilotPageFlows.test`** Must heading (`971c7f1`, Q643) · **related surfaces panel** (`0b0d7ba`, Q650) · **Modal field·memo error clear** (`96e9d25`/`31ab1aa`, Q647) · **UXD-155 `ds-fieldset`** (`085a85a`, Q646)
- [ ] **`V173StaffAnnualLeaveYearlyIntegrityReadinessProbeTest`** · **`GET /health`** — **`v173StaffAnnualLeaveYearlyIntegrityCheckReady=true`** (`8c5dd65`, Q645)
- [ ] **`NotificationChannelReadinessServiceTest.placeholderSolapiCredentialsShouldRemainNotReady`** · **`placeholderTemplateMappingShouldRemainNotReady`** · **`NotificationConfigTest`** — Solapi placeholder credential/template guard (`19ffa84`, Q644)
- [ ] **`GET /api/v1/notifications/channel-status`** — placeholder Solapi env → **`liveAlimtalkDispatchReady=false`** · **`readinessBlockers`** contains **`MISSING_SOLAPI_CONFIG`** or **`MISSING_TEMPLATE_MAPPING`** (Q644)
- [ ] **`LiveE2eOperationReadinessSupportTest`** — **bootstrap error suppresses derived blockers** (`0c9518a`, Q596) · **bootstrap error detail suffix match** (`20485f1`, Q596 deepen) · **bootstrap blocker normalize — `-not-ready` only** (`24d25f1`, Q631) · **no `-error`/`bootstrap-error` in blockers**
- [ ] **`GET /api/v1/system/live-e2e/probe`** — bootstrap error → **`operationBlockers`** = **`staff-bootstrap-not-ready` + `guardian-bootstrap-not-ready`** only · detail **`bootstrap=error`** (`24d25f1`, Q631)
- [ ] **`GET /api/v1/health`** — **`liveE2eOperationBlockers`** mirrors probe · **no `bootstrap-error`/`staff-bootstrap-error`** (`24d25f1`, Q631)
- [ ] Flyway **V169** applied — **`staff_work_attendance`** table · org/branch/user/date UNIQUE · checkout-after-checkin CHECK (`a6eb8b7`, Q612)
- [ ] **`StaffWorkAttendanceServiceTest`** (+ check-in method validation, `10c0daf`) · **`StaffWorkAttendanceStatusSupportTest`** · **`StaffWorkAttendanceLiveApiRoutingE2eTest`** — roster·check-in/out·RBAC (`a6eb8b7`, Q612)
- [ ] **`StaffWorkAttendanceSupportTest`** · **`StaffWorkAttendanceServiceTest`** — roster **`surfaceKind`·`relatedSurfaces`** assert (`83a26e7`, Q653)
- [ ] **`StaffWorkAttendancePage.test`** · **`staffAnnualLeave.test`** — roster load·**checkInMethod MANUAL/MOBILE**·check-out·403 error · **API metadata cross-links** (`95f55aa`, Q612·Q651·Q653)
- [ ] **`GET /api/v1/staff/work-attendance`** — **`surfaceKind=DAILY_WORK_ATTENDANCE_ROSTER`** · **`relatedSurfaces[0].route=/staff/annual-leaves`** · **`relatedSurfaces[1].route=/staff/leave-ledger`** · **`relatedSurfaces[1].availability=AVAILABLE`** (`bb9df48`, Q653·Q663)
- [ ] **`StaffLeaveLedgerServiceTest`** · **`StaffLeaveLedgerSupportTest`** · **`MustApiEndpointRoutingTest.StaffLeaveLedgerRouting`** — canonical ledger CRUD·`surfaceKind`·cross-link (`bb9df48`, Q663)
- [ ] **`StaffLeaveLedgerLiveApiRoutingE2eTest`** — list **`surfaceKind`·`relatedSurfaces`** · create contract (`5fd12dd`, Q666)
- [ ] **`StaffLeaveLedgerPilotServiceFlowE2eTest`** · **`RoleBasedControllerAccessTest.StaffLeaveLedgerAccess`** — list→create→update→delete pilot · **`hq_admin` CUD 403** · **`caregiver` list 403** (`62fce23`, Q665)
- [ ] **`GET /api/v1/staff/leave-ledger?year=2026&branchId=`** — **`surfaceKind=CANONICAL_LEAVE_LEDGER`** · **`items[]`** · **`relatedSurfaces[0].route=/staff/annual-leaves`** · **`relatedSurfaces[1].route=/staff/attendance`** (`bb9df48`, Q663)
- [ ] **`/staff/leave-ledger`** — **`StaffLeaveLedgerPage`** 연도 조회·**「항목 등록」** Modal · **`StaffLeaveLedgerTable`** 수정/삭제 · **`StaffLeaveLedgerDeleteModal`** (UXD-157) · **`DateInput`** · **`StaffLeaveLedgerRelatedSurfacesPanel`** cross-link · **`StaffLeaveLedgerPage.test`** · **`StaffLeaveLedgerTable.test`** · **`StaffLeaveLedgerDeleteModal.test`** · **`pilotPageFlows.test`** Must title (`8057c1e`/`bd1d0ad`, Q666·Q667)
- [ ] **`staffAnnualLeaveServices.test.js`** — roster **`relatedSurfaces[1].availability=AVAILABLE`** for `/staff/leave-ledger` (`426d63a`, BNK-551·Q667)
- [ ] Flyway **V174** applied — **`staff_leave_ledger_entries`** table · `leave_type` CHECK · `days_used` CHECK (`bb9df48`, Q663)
- [ ] Flyway **V175** applied — **`chk_staff_leave_ledger_entries_memo_nonempty`** · **`fk_staff_leave_ledger_entries_user_branch_assignment`** (`c4e6bcb`, Q668)
- [ ] **`GET /api/v1/users`** — **`social_worker` JWT → 200** · **`PATCH /users/{id}` → 403** (Q669)
- [ ] **live-e2e defaults** — **`LIVE_E2E_ORGANIZATION_ID`** 등이 dev seed **`00000001-*`** 와 **겹치지 않음** — 기본 **`e2e00001-*`** (`c4e6bcb`, Q670)
- [ ] **`liveE2eSuiteGuard.test.js`** — **`liveCashReceiptDescribe`** import·호출 guard (`b7101d5`, Q664)
- [ ] **`/staff/attendance`** — **근무일 조회** · **출근 방식 select** · StatCard **출근/퇴근/미출근** · **「출근」/「퇴근」** 버튼 · **API 기반「연차휴가 현황」·「연차·유급휴일 대장」cross-link panel** (`5fd468b`/`95f55aa`/`8057c1e`, Q612·Q651·Q653·Q666)
- [ ] **HR nav 삼방향 smoke (Q652·Q653·Q657·Q663·Q666·Q667)** — **`/staff/annual-leaves`** 패널 **「출퇴근 기록」** → `/staff/attendance` · **`/staff/attendance`** 패널 **「연차휴가 현황」** → `/staff/annual-leaves` · **`/staff/leave-ledger`** 패널 **연차·출퇴근 링크** · **`GET /staff/leave-ledger`** **`surfaceKind=CANONICAL_LEAVE_LEDGER`** · **`BranchScopeNotice`** 지점 일치 · **대장 삭제 Modal** 키보드 포커스
- [ ] **`BillingServiceTest`** — **`assertPriorDepositOrderForClients`** — 이전 월 미납 시 수납 **422** (`a6eb8b7`, Q614)
- [ ] **`AttendancePage.test`** — pending roster row **`id=null`·`status=null`** · checked-in **귀가** 버튼 · **`fetchAttendanceApi` mock only** (`8383f8d`, Q609)
- [ ] **`vitestConfig.test`** — serial fork pool policy assert (`8383f8d`, Q610)
- [ ] **`npm test`** — **`scripts/npm-test-locked.sh`** 경유 · **동시 2개 이상 실행 금지** (`docs/qa/VITEST_CONCURRENCY.md`, Q610·Q661) · full-suite 1 FAIL + isolated PASS 시 **`./scripts/vitest-stop.sh`** 후 재시도
- [ ] **G2 CMS roster status filter (Q662)** — `GET …/enrollments?status= pending ` → **PENDING** roster · `status=EXPIRED` → **`422`** (`f1225b0`)
- [ ] **`AttendanceStatusSupportTest`** · **`AttendanceServiceTest`** — roster **clientName·status·pending row** (`0c69060`, Q609)
- [ ] **`AttendanceRosterLiveApiRoutingE2eTest`** · **`RoleBasedControllerAccessTest$AttendanceAccess`** — JSON contract · **caregiver 200 / guardian 403** (`61e1970`, Q609)
- [ ] **`/attendance`** — **미처리 이용자** 목록·**입소·결석** 버튼 · StatCard **「미처리」** · API 단일 호출 (`8383f8d`, Q94·Q609)
- [ ] **`OverdueManagementServiceTest`** — **duplicate auto SMS guard** — existing auto record → skip (`a45c040`, Q607)
- [ ] **`StaffDocumentRepositoryPanel.test`** · **`FileUpload.test`** · **`StaffHrFilePanel.test`** — **mobile camera capture** upload (`6bde24a`, Q608) · **mobile full-width `.ds-btn` CSS** (`9812ac4`, Q611)
- [ ] **`StaffStatusReportPage.test`** — **print cleanup** (`afterprint`·blob revoke·empty export guard, `a4ea2d5`, Q315)
- [ ] **`/staff/{userId}?tab=files`** — **`StaffDocumentRepositoryPanel`** **「모바일 촬영」** · progress·phase Badge · **API authoritative source** · **모바일 전폭 버튼** (`fd15a2f`/`6bde24a`/`9812ac4`, Q604·Q608·Q611)
- [ ] **`DashboardServiceTest`** — **`nhisComparisonGapCount`** branch·HQ (`0796821`, Q594)
- [ ] **`DashboardPage.test`** · **`transportKakaoQuotaSummary.test`** — **NHIS gap StatCard** · **Kakao quota widget** (`fe7df60`·`580a86b`, Q594·Q595)
- [ ] Flyway **V166** applied — **`chk_users_lifecycle_status` includes `ON_LEAVE`** · on-leave hired_at·terminated_at CHECK (`68d4457`, Q584)
- [ ] Flyway **V167** applied — **`billing_overdue_management_records`·`billing_overdue_adjustments`** (`4d92844`, Q602)
- [ ] Flyway **V168** applied — overdue **note/reason nonempty**·**temporal**·**Tenant FK 8쌍** · purge·`recorded_by` indexes (`399c698`, Q605)
- [ ] **`BathingScheduleServiceTest`** · **`BathingScheduleLiveApiRoutingE2eTest`** — **copy-from-previous-month** (`49a1721`/`a426663`, Q598)
- [ ] **`/care/bathing-schedules`** — **「전월 일정 복사」** · `createdCount`/`skippedCount` toast · **`aria-busy`** (`9a957fb`/`751c593`, Q598·Q606)
- [ ] **`OverdueManagementServiceTest`** · **`OverdueManagementLiveApiRoutingE2eTest`** — management-records·adjustments API · **SMS auto-record scope guard** · **duplicate auto SMS guard** · **V168 integrity** (`4d92844`/`c17097d`/`f6266ec`/`399c698`/`a45c040`, Q602·Q605·Q607)
- [ ] **`/billing/overdue`** — **「관리」** `OverdueManagementModal` 2-tab wire · **UXD-150 a11y** (`0420e6b`/`751c593`, Q602·Q606)
- [ ] **`StaffDocumentRepositoryComplianceTest`** · **`StaffHrFileServiceTest`** · **`MustApiEndpointRoutingTest`** · **`staffHrFileServices.test`** — **repository-progress API** · **FE authoritative wire** (`b583c11`/`fd15a2f`, Q604)
- [ ] **`StaffDocumentRepositoryPanel.test`** · **`staffDocumentRepository.test`** — **21-slot FE parity** · **UXD-150 aria-label** · **mobile capture** (`fd15a2f`/`751c593`/`6bde24a`, Q604·Q606·Q608)
- [ ] **`/staff/{userId}?tab=files`** — **`StaffDocumentRepositoryPanel`** progress·phase Badge·upload·**mobile capture** · **API authoritative source** (`fd15a2f`/`6bde24a`, Q604·Q608)
- [ ] **`StaffLifecycleSummaryServiceTest`** · **`StaffLifecyclePanel.test`** · **`StaffLifecycleSummaryPanel.test`** — **G-STAFF-LEAVE-STATUS full-stack** (`1d7cee2`/`2581347`, Q584)
- [ ] **`BillingServiceTest`** · **`BillingReportAppliedFiltersTest`** · **`BillingReportFilterEnumsTest`** — **deposit `period`·receipt `basis`** filters · **invalid calendar month** (`375fb9d`, Q585·Q586) · **`appliedFilters` echo** (`14935a3`, Q587) · **receipt CLAIM basis** (`7b99313`, QA-B193)
- [ ] **`BillingReportPage.test`** · **`billingReportFilters.test`** — **`appliedFilters` FE wire** · **UXD-148 a11y** (`c6a412f`·`e2f1246`, Q587·Q588)
- [ ] **`/billing/reports/deposits`** — **「입금 구간」** segmented control · **`/billing/reports/receipts`** — **「집계 기준」** (`e38ccfd`, Q585)
- [ ] **`billingReportFilters.test`** · **`BillingReportPage.test`** — period/basis query params (`e38ccfd`, Q585)
- [ ] **`BillingReportFilterServiceTest`** — **`recordFromReportQuerySafely()`** non-blocking autosave (`99d03fa`, Q626) · filter hydrate FE (`77b1ea8`, Q621)
- [ ] **`/attendance/qr/generate`** — **`QrGeneratePage`** PNG preview·**「이미지 저장」**·인쇄 (`250619e`, Q624) · **`branchQrCode.test.js`**
- [ ] **`GET /api/v1/system/health`** — **`v171DefenseInDepthIntegrityCheckReady=true`** · V171 미적용 시 **`v171-defense-in-depth-constraint-missing`** (Q625, `dce9bf1`/`175d9cb`)
- [ ] **`V171DefenseInDepthSchemaReadinessProbeTest`** · **`HealthControllerTest`** — V171 probe (`dce9bf1`, Q625)
- [ ] **`CmsServiceTest`** — payerName·bankCode·accountLast4 normalization (`9db0bbb`, Q627)
- [ ] **`UserServiceTest`** · **`StaffLifecyclePilotServiceFlowE2eTest`** — **`ON_LEAVE` lifecycle**·**ACTIVE 복귀** (`68d4457`, Q584)
- [ ] **`/staff`** — **`StaffNhisCaregiverImportPanel`** preview·select·import·account-request refresh (`4315ee2`, Q573·Q577)
- [ ] **`GET /api/v1/health`** — configured branch missing/inactive/cross-org → **`liveE2eOperationReady=false`** (`191703f`, Q502)
- [ ] **`GET /api/v1/health`** — G21 seed visit schedule·NHIS batch **다른 branch 소속** → ready flags **false** · **`liveE2eOperationReady=false`** (`02cf036`, Q507)
- [ ] **`LiveE2eBootstrapServiceTest`** — **cross-branch visit schedule·NHIS batch rejection** (`02cf036`, Q507)
- [ ] **`LiveE2eBootstrapServiceTest`** — **default guardian creds → staff bootstrap guardian token skip** (`02a2eb8`, Q510)
- [ ] **`GET /api/v1/health`** — **`liveE2eGuardianStatusDetail`·`liveE2eG21SeedStatusDetail`** populated (`12d1a7b`, Q515)
- [ ] **`HealthControllerTest`** — guardian·G21 seed detail exposure (`12d1a7b`, Q515)
- [ ] Flyway **V157** applied — **`chk_case_management_meetings_attendee_opinions_array`** (`8835aa2`, Q519)
- [ ] **`AttendeeOpinionsCodecTest`** — malformed JSON → empty list · round-trip (`9ecd019`, Q519)
- [ ] **`CaseManagementServiceTest`** — **duplicate attendee names/opinions rejection** (`eed39ab`, Q520)
- [ ] **`CaseManagementPage.test`** · **`caseManagementCompliance.test`** — duplicate attendee FE guard (`c7fb69a`, Q520)
- [ ] **`liveE2eHarness.test`** — **`getLiveE2eSkipReasons`** actionable diagnostics (`9969746`, Q521)
- [ ] **`GET /api/v1/health`** — **`liveE2eG32ComplianceAttendeeOpinionsFieldReady`·`liveE2eG32DashboardAttendeeOpinionGapFieldReady`·`liveE2eG32AttendeeOpinionsArrayCheckReady`** — stale G32 → blockers mirror probe (`caeac0d`, Q528)
- [ ] **`HealthControllerTest`** — G32 readiness flags·blockers on health (`caeac0d`, Q528)
- [ ] **`LiveE2eBootstrapServiceTest`** — whitespace-padded credentials trim·whitespace-only rejection (`7848b0f`, Q529)
- [ ] **`VisitNhisComparisonPanel.test`** · **`VisitsPage.test`** — split-view dual PLAN+BILLING NHIS panels (`9b80505`, Q526)
- [ ] **`CaseManagementPage.test`** · **`GuardianDocumentNotifyPanel.test`** — UXD-138 a11y (`d354a0e`, Q527)
- [ ] **`GET /api/v1/system/live-e2e/probe`** — stale G32 runtime → **`operationBlockers`** contains **`g32-compliance-field-missing`·`g32-dashboard-field-missing`·`g32-v157-constraint-missing`** (`c0a59aa`/`45d95ea`, Q525)
- [ ] **`G32SchemaReadinessProbeTest`** — V157 **`chk_case_management_meetings_attendee_opinions_array`** detection (`45d95ea`, Q525)
- [ ] **`LiveE2eControllerTest`** — G32 probe readiness flags·blockers (`45d95ea`, Q525)
- [ ] **`programComplianceLiveApi.e2e.test.js`** — **`hasG32SchemaBlocker()`** graceful skip on stale runtime (`09912ba`, Q525)
- [ ] **`HealthPage.test`** · **`CareProvisionSegmentNav.test`** — 케어포 3-1 segment nav (`1d5747d`, Q524)
- [ ] **`GET /api/v1/dashboard/branch`** · **`/dashboard/hq`** — **`caseManagementAttendeeOpinionGapCount`** populated (`b9e0947`, Q518)
- [ ] **`DashboardServiceTest`** — branch·HQ attendee-opinion gap count (`b9e0947`, Q518)
- [ ] **`DashboardPage.test`** — **「참석자별 의견 미기록」** widget (`e55ae96`, Q518)
- [ ] **`dashboardSummary.test`** — **`caseManagementAttendeeOpinionGapCount`** mapping (`e55ae96`, Q518)
- [ ] Flyway **V156** applied — **`case_management_meetings.attendee_opinions`** JSONB (`5222a8f`, Q516)
- [ ] **`CaseManagementServiceTest`** — **`attendeeOpinionsMet`** compliance (`5222a8f`, Q516)
- [ ] **`CaseManagementPage.test`** — per-attendee opinion fieldset·validation (`b272a7b`, Q516)
- [ ] **`GuardianDocumentNotifyPanel.test`** — home-newsletter·care-provision-record dispatch (`d1149a5`, Q517)
- [ ] **`GET /api/v1/health`** — branch missing/inactive → **`operationBlockers`** contains **`g21-branch-missing-or-inactive`** (`bc754a0`, Q511)
- [ ] **`HealthControllerTest`** — **health G21 branch blocker exposure** (`bc754a0`, Q511)
- [ ] **`GET /api/v1/system/live-e2e/probe`** — branch missing/inactive → **`operationBlockers`** contains **`g21-branch-missing-or-inactive`** (`7898aa5`, Q505)
- [ ] **`LiveE2eBootstrapServiceTest`** — **paired PLAN/BILLING bootstrap seed** (`fd275f4`, Q500)
- [ ] **`GET /api/v1/health`** — NHIS row **`batchId` mismatch** → **`nhis-import-missing`** · **`liveE2eOperationReady=false`** (`c0403b0`, Q499)
- [ ] **`LiveE2eBootstrapServiceTest`** — **per-tenant scoped fallback IDs** deterministic (`c651b30`, Q498)
- [ ] **`LiveE2eBootstrapServiceTest`** — **NHIS row-batch linkage** mismatch regression (`c0403b0`, Q499)
- [ ] **`liveE2eHarness.test`** — **`isLiveG21ReadyForRun`** false when operation not ready (`d61ab5e`, Q497)
- [ ] **`liveE2eHarness.test`** — **`isLiveG21ReadyForRun`** false when **BILLING seed missing** (`c3b6a5c`, Q512)
- [ ] **`liveE2eHarness.test`** — **`isLiveG21ReadyForRun`** true when operation + G21 seed ready (`d61ab5e`, Q497)
- [ ] **`CareServiceWeeklyRecordPage.test`** — FAQ21817 **7-day SLA alert** (`b881883`, Q513)
- [ ] **`careServiceStateChangeDue.test`** — **`computeStateChangeDueAlerts`** missing/due/overdue (`b881883`, Q513)
- [ ] **`VisitRfidDiffComparePanel.test`** — **RFID special-notes equivalence guide** (`b881883`, Q514)
- [ ] **`VisitBatchConfirmPanel.test`** — missing branchId **loading clear** · NHIS ack **`aria-describedby`** (`5743333`/`0002943`, Q508·Q506)
- [ ] **`NursingVitalCheckPage.test`** · **`Nursing*Page.test`** — edit **`Button tertiary`·`ds-btn`·`aria-label`** (`f86c76c`/`6f07803`, Q509)
- [ ] **`GET /api/v1/health`** — **`liveE2eDefaultGuardianCredentials`** 필드 존재 (`09df8c7`, Q428)
- [ ] Flyway **V153** applied — **`idx_billing_claims_org_branch_status_paid_at`** partial index on PAID rows (`Q431`, `c8ee85c`)
- [ ] **`GET /api/v1/billing/reports/deposits`** · **`…/receipts`** — **`paid_at DESC`** 정렬 응답 (post-V153 smoke, Q431)
- [ ] **`/transport`** — roster **「배차 루트」** **「N번 정차」** link · **「계획 픽업」/「계획 하차」**·late **「지연」** Badge (`e35efb2`, Q433)
- [ ] **`transportRosterDispatch.test`** · **`TransportPage.test`** — confirmed run dispatch index·planned pickup late badge (`e35efb2`, Q433)
- [ ] **`StaffLifecyclePanel.test`** — FAQ21806 **NEW_HIRE_TRAINING_DEADLINE_DAYS** mock (`101aaee`, Q434)
- [ ] **`/staff/health-checkups`** — StatCard **「신규 서류 미확인」** · 목록 **「입사일」·「신규 서류」** Badge · 첫 검진 **365일 창** field error (`8e6310a`, Q435)
- [ ] **`staffHealthCheckupCompliance.test`** · **`StaffHealthCheckupsPage.test`** — new-hire document window (`8e6310a`, Q435)
- [ ] **`GET /api/v1/system/live-e2e/probe`** — **`operationReady`·`operationBlocker`·`staffBootstrapReady`·`guardianBootstrapReady`** 필드 존재 (`40ef105`, Q441)
- [ ] Flyway **V154** applied — **`service_log_driver_signatory_name`·`service_log_driver_signed_on`** pair constraint (`bc3a35c`, Q445)
- [ ] **`PUT /api/v1/transport/runs/{runId}/service-log`** — **`driverSignatoryName`·`driverSignedOn`** persist · partial pair **`422`** · **`driverSignatureComplete`** in GET (`bc3a35c`, Q445)
- [ ] **`TransportServiceTest.upsertServiceLogShouldPersistDriverSignature`** · **`upsertServiceLogShouldRejectPartialDriverSignature`** (`bc3a35c`, Q445)
- [ ] **`/transport/runs/:runId`** — **「운전자 서명」** `fieldset` **「서명 성명」·「서명일」** required before save/print · audit **운전자 서명: 완료/미완료** (`bfe0283`, Q450)
- [ ] **`TransportServiceLogPanel.test`** — **「서명 성명」·「서명일」** label queries · driver signature validation (`bfe0283`, Q450)
- [ ] **`liveE2eHarness.test`** — guardian-only suites run when **`staffAuthReady=false`** but backend ready (`7424c30`, Q451)
- [ ] **`LiveE2eBootstrapServiceTest`** — legacy **`DAY_CARE` seed branch → `HOME_VISIT` on activate (`9e050b1`, Q457)
- [ ] **`VisitLiveApiRoutingE2eTest`** — visit list/import·RFID compare routing harness (`9e050b1`, Q457)
- [ ] **`LiveE2eBootstrapServiceTest`** — **`ensureSampleNhisImportBatch`** 당월 NHIS import batch/row **`serviceDays=1`** (`b73e5f4`, Q488)
- [ ] **`VisitLiveApiRoutingE2eTest`** — **`GET /visits/nhis-comparison`** per-client routing · **`nhisBatchPresent=true`** after bootstrap (`b73e5f4`, Q488)
- [ ] **`VisitServiceTest.checkInShouldAllowSocialWorkerWithUppercaseRoleCode`** — supervisory **`roleCode` normalize** (`78cfb8a`, Q455)
- [ ] **`VisitRfidDiffComparePanel.test`** — unknown/comma **`diffCodes` badge rendering** (`4a112fe`, Q456)
- [ ] **`POST /api/v1/visits/imports/rfid/compare`** — **`planFile`·`rfidFile`** multipart · **`diffCodeCounts` COMP_01~09** (`eeac205`, Q452)
- [ ] **`VisitRfidDiffComparePanel.test`** — **`/visits`** multipart upload · COMP summary · diff table (`27c9de3`/`4a112fe`, Q452·Q456)
- [ ] **`VisitServiceTest.checkInShouldRejectWhenAssignedUserIsInactive`** · **`checkInShouldRejectWhenAssignedUserIsNotInBranch`** (`0db1e68`, Q453)
- [ ] **`BodyRestraintRecordPage.test`** — snake_case client payload · malformed response Alert (`4a47675`, Q454)
- [ ] **`VisitServiceTest.compareRfidTransmissionShouldReturnSevenCodeDiffMatrix`** · **`MustApiEndpointRoutingTest`** RFID compare routing (`eeac205`, Q452)
- [ ] **`TransportServiceLogPanel.test`** — driver signature validation before save/export (`f51e365`/`bfe0283`, Q445·Q450)
- [ ] **`/transport/compliance`** — **`TransportServiceLogLegalGuide`** card · **「확정 배차 선택」** anchor (`0df6902`, Q446)
- [ ] **`TransportServiceLogLegalGuide.test`** · **`TransportCompliancePage.test`** (`0df6902`, Q446)
- [ ] **`GET /api/v1/system/live-e2e/probe`** — bootstrap error → **`operationBlockers`** **`staff-bootstrap-not-ready`·`guardian-bootstrap-not-ready` only** · detail **`bootstrap=error`** (`24d25f1`, Q631; supersedes Q448 `-error` codes)
- [ ] **`GET /api/v1/transport/runs/{runId}/service-log`** — response includes **`branchAddress`·`branchRegionPath`·`branchPhone`** (`a8e2bb2`, Q469)
- [ ] **`TransportServiceTest`** — service log branch contact fields resolve from branch entity (`a8e2bb2`, Q469)
- [ ] **`GET …/service-log`** — response includes **`direction`** (`PICKUP`/`DROPOFF`) (`72124f7`, Q471)
- [ ] **`TransportServiceTest`** — DROPOFF service log rows use **`하차:`** note prefix (`72124f7`, Q471)
- [ ] **`TransportServiceLogLiveApiRoutingE2eTest`** — **`direction`** on service log response (`72124f7`, Q471)
- [ ] **`GET /api/v1/system/live-e2e/probe`** — bootstrap disabled → **`operationBlockers` = `["bootstrap-disabled"]` only** (`8cf09d8`, Q472)
- [ ] **`LiveE2eControllerTest`** — probe bootstrap-disabled single blocker contract (`8cf09d8`, Q472)
- [ ] **`liveGlobalSetup.js`** — default guardian fallback **`live-e2e-guardian@ogada.test`/`ogada-guardian-e2e`** (`94c65e2`, Q473)
- [ ] **`liveE2eHarness.test`** — guardian fallback login probe uses aligned creds (`94c65e2`, Q473)
- [ ] **`GET …/service-log`** — row **`pickupAddress`** dedicated field (not note-only) (`e358f2d`, Q470)
- [ ] **`TransportServiceLogLiveApiRoutingE2eTest`** — **`pickupAddress`** on first row (`e358f2d`, Q470)
- [ ] **`/transport/runs/:runId`** — DROPOFF direction uses **하차 장소·계획 하차·실제 하차** labels (`07be394`, Q468)
- [ ] **`TransportServiceLogPanel.test`** — remark read-only field·dropoff direction labels (`07be394`, Q468)
- [ ] **`transportServiceLog.test`** — **`formatServiceLogRemark`** deduplicates pickup prefix (`07be394`, Q468)
- [ ] **`/transport/runs/:runId`** — print·txt header shows **branch name·address·region·phone** (`b1a16ff`, Q469)
- [ ] **`TransportServiceLogPanel.test`** — branch contact in print layout (`b1a16ff`, Q469)
- [ ] Flyway **V155** applied — **`chk_transport_run_stops_waypoint_address_nonempty`** — WAYPOINT **`btrim(waypoint_address) <> ''`** (`64c4c80`, Q458)
- [ ] **`TransportServiceTest.updateRunShouldRejectBlankWaypointAddress`** · **`createRunShouldTrimWaypointAddressBeforePersist`** (`a179256`, Q467)
- [ ] **`TransportPilotServiceFlowE2eTest.usT02UpdateRunShouldRejectBlankWaypointAddress`** (`a179256`, Q467)
- [ ] **`/transport/runs/:runId`** — service log per-stop **read-only「탑승 장소」·「시간 준수」** fields mirror print columns (`7de5a6f`, Q466)
- [ ] **`TransportServiceLogPanel.test`** — per-stop pickup address·time compliance read-only labels (`7de5a6f`, Q466)
- [ ] **`/staff/training-logs`** — **PDF 8-7 필수 교육 미작성 Alert** · 재난·소화 StatCard **「미작성」** (`caa215f`, Q459)
- [ ] **`StaffTrainingLogPage.test`** — **reference-year guard** — invalid filter **`Field error`** · compliance hidden · invalid submit blocked (`f26e075`/`28e5525`, Q489)
- [ ] **`staffTrainingLogs.test`** — **`parseStaffTrainingReferenceYear`** · **`staffTrainingReferenceYearFieldError`** (`28e5525`, Q489)
- [ ] **`StaffTrainingLogPage.test`** — mandatory unwritten alerts for disaster and fire safety only (`caa215f`, Q459)
- [ ] **`/staff/training`** — **「엑셀 다운로드 (8-7-1)」** CSV export from compliance summary (`caa215f`, Q460)
- [ ] **`StaffRefresherTrainingPage.test`** — 8-7-1 report csv export (`caa215f`, Q460)
- [ ] **`/dashboard`** — **「직원교육 미충족」** widget · compliance API fallback (`9e91e6a`, Q461)
- [ ] **`DashboardPage.test`** — staff training compliance snapshot·partial failure warning (`9e91e6a`, Q461)
- [ ] **`VisitRfidDiffComparePanel`** — **`aria-label="RFID 계획·태그 엑셀 비교"`** · diff code Field labels (`7f94654`, Q462)
- [ ] **`/transport/runs/:runId`** — service log print·txt includes **픽업 주소** column (`a1d6e32`, Q463)
- [ ] **`TransportServiceLogPanel.test`** — pickup address in print layout (`a1d6e32`, Q463)
- [ ] **`LiveE2eBootstrapServiceTest`** — **당월 DRAFT PLAN visit upsert** on HOME_VISIT branch (`dac19d3`, Q464)
- [ ] **`LiveE2eBootstrapServiceTest`** — bootstrap client **`usesTransport`·pickup address/coords·default pickup time** (`2d98040`, Q465)
- [ ] **`GET /api/v1/health`** — **`liveE2eOperationBlockers`** mirrors probe · **`-not-ready` only on bootstrap error** (`24d25f1`, Q631)
- [ ] **`HealthControllerTest`** · **`LiveE2eControllerTest`** — bootstrap error blocker contract (`d7f1a9a`, Q448)
- [ ] **`MealAssistanceRecordPage.test`** — **`creates a record when client payload uses snake_case fields`** (`1c8f236`, Q449)
- [ ] **`GET /api/v1/system/live-e2e/probe`** — **`operationBlockers`** array · **`operationBlocker`** = first item (`c5dd4f2`, Q447)
- [ ] **`GET /api/v1/health`** — **`liveE2eOperationBlockers`** array exists (`c5dd4f2`, Q447)
- [ ] **`HealthControllerTest`** · **`LiveE2eControllerTest`** — operation blockers list contract (`c5dd4f2`, Q447)
- [ ] **`TransportServiceTest.upsertServiceLogShouldRejectIncompleteLegalFields`** — missing pickup·companion·dropoff·dropoff-before-pickup **`422`** (`ac1d43f`, Q443)
- [ ] **`/staff/health-checkups`** — **「서류 업로드」** link · **「이력」** Modal **`StaffHealthCheckupRecordsPanel`** · **`health-check`** HR 파일함 상태 (`b6ce301`, Q444)
- [ ] **`StaffHealthCheckupsPage.test`** — new-hire **서류 업로드** link·history modal HR file hub (`b6ce301`, Q444)
- [ ] **`TransportServiceLogPanel.test`** — **`validates required legal fields before save`** (`b4644e8`, Q439)
- [ ] **`TransportServiceTest.upsertServiceLogShouldRejectDuplicateClientRows`** — duplicate client **`422`** (`52e3340`, Q440)
- [ ] **`MealAssistanceRecordPage.test`** — malformed API payload Alert (`38642e2`, Q442)
- [ ] **`LiveE2eBootstrapServiceTest`** — **`issueSeedTokensWithRetry`** stale seed retry (`a6dfaad`, Q438)
- [ ] **`LiveE2eBootstrapLiveApiRoutingE2eTest`** — staff bootstrap **embedded guardian token fields** (`d02f78a`, Q438)
- [ ] **`DateInput.test`** — today button **`( 오늘)?` optional** selector (`40d4284`, Q436)
- [ ] **`TransportServiceLogLiveApiRoutingE2eTest`** — **`GET/PUT …/service-log`**·**`GET …/audit-trail`** routing harness (`4c5d3bc`, Q432)
- [ ] FE **`npm run test:live-e2e`** — **`scripts/run-frontend-live-e2e.sh`** delegation (`8882d9f`, Q429) · **`liveE2eHarness.test`**
- [ ] **`DateInput.test`** — keyboard arrow·PageUp/PageDown·roving tabindex (`7b8c7b9`, Q430)
- [ ] **`MonitoringSelfDiagnosisPage.test`** — **`MonitoringEvidenceContextPanel`** evidence window·cross-link nav (`7d2cb4a`, Q391)
- [ ] FE **`liveE2eHarness.test`** — nested·snake_case bootstrap payload token parse (`fc916db`, Q425)
- [ ] FE **`liveE2eHarness.test`** — stale refresh token replace·placeholder guardian email hydration (`b2c09e1`, Q427)
- [ ] **`GET /api/v1/system/live-e2e/probe`** — credential check throw 시 **HTTP 200** 유지·per-field **`credentialsConfigured`** fallback (`844227a`, Q427)
- [ ] **`LiveE2eBootstrapServiceTest`** — seed branch **`active=true`**·`serviceType`·`regionDongCode` (`d68c4bf`, Q409)
- [ ] **`/transport/compliance`** — **`TransportServiceLogRunsPanel`** 확정 배차 표·**「일지 작성·보관」** → **`/transport/runs/:runId`** (`b93e098`, Q426)
- [ ] **`TransportServiceLogRunsPanel.test`** · **`TransportCompliancePage.test`** — confirmed run link·empty state (`b93e098`, Q426)
- [ ] **`GET /actuator/healthz`** — **`/actuator/health`·`/readyz`와 동일** DB readiness · UP **200** · DB down **503** (`2157df5`, Q413)
- [ ] **`DateInput.test`** · **`pickerDate.test`** · **`pickerTestUtils.js`** — 달력·시간 피커·month-only·time select (`ea5d896`/`ab4de83`, Q422)
- [ ] **`/clients/new`** — 생년월일 **`DateInput`** 달력 **`viewAnchor`**(1940~50년대 근처 오픈) (`ab4de83`, Q422)
- [ ] **`/transport/runs/new`** — **`TimeInput` 출발 시각** · 정차 **ETA time chip** · 지연 시 **`--eta-late`** (`bf73c4c`/`ea5d896`, Q418)
- [ ] **`transportMapEtas.test`** · **`TransportStopList.test`** — `isEstimatedArrivalLate`·chip labels (`bf73c4c`, Q418)
- [ ] **`NotificationChannelReadinessServiceTest`** — **`SMTP_HOST` 누락 시 `MISSING_SMTP_CONFIG`만** · 알림톡 ready 유지 (`704478f`, Q367)
- [ ] **`POST /api/v1/system/live-e2e/bootstrap`** — 응답 optional **`guardianAccessToken`/`guardianRefreshToken`/`guardianEmail`/`guardianUserId`** when guardian-client seed ready (`73cffc5`, Q409)
- [ ] **`LiveE2eBootstrapServiceTest`** — **`tryIssueExistingGuardianTokens`** best-effort · guardian token failure does not fail staff bootstrap (`73cffc5`, Q409)
- [ ] Flyway **V152** applied — **`trg_transport_run_stops_guard_client`** rejects **inactive/discharged** client stops (`Q423`, `dd2fa2c`)
- [ ] **`PUT /api/v1/transport/settings`** — empty weight → **422** · weight sum **≤0** → **「가중치 합은 0보다 커야 합니다.」** (`dd2fa2c`, Q424)
- [ ] **`POST /api/v1/transport/runs/suggest`** — DRAFT `stops[]` includes **BRANCH** at start and end (`dd2fa2c`, Q424)
- [ ] **`/transport`** — **자동·수동 배차** side-by-side grid · **embedded settings** in suggest card · empty weight **field error before save** (`96db8bf`, Q424)
- [ ] **`BranchTransportSettingsPanel.test`** · **`transportSettingsForm.test`** · **`TransportSuggestPanel.test`** — embedded settings·validation (`96db8bf`, Q424)
- [ ] **`POST /api/v1/transport/runs`** — inactive/discharged client in `stops[]` → **DB trigger reject** (V152, Q423)
- [ ] **`POST /api/v1/transport/route-preview`** — 응답 **`legDurationsSeconds[]`** 길이 = 정차 수 − 1 (`0e46b37`, Q418)
- [ ] **`TransportServiceTest`** · **`TransportRoutePreviewServiceTest`** — planned departure persist·leg duration contract (`0e46b37`, Q418)
- [ ] **`/transport/runs/new`** — **출발 시각** **`TimeInput`** · 정차 목록 **ETA time chip** 표시 (`ea5d896`/`bf73c4c`, Q418·Q422)
- [ ] **`TransportRouteSplitView.test`** · **`TransportPage.test`** — 세로 stack·**AbortController** stale-load guard (`fde098f`, Q420)
- [ ] **`DELETE /api/v1/transport/runs/{runId}`** — **DRAFT only** · **`hq_admin`** · **204** · CONFIRMED **422** (`1d1a71f`, Q403)
- [ ] **`/transport/runs/:runId`** — DRAFT 상태 **「삭제」** → **`TransportDeleteRunModal`** 확인 · 삭제 후 **`/transport`** 복귀 (`45bd923`, Q403)
- [ ] **`TransportRunDetailPage.test`** · **`TransportPage.test`** — direction-aware runs·delete modal 회귀 (`45bd923`, QA-B116)
- [ ] **`GET /api/v1/transport/runs/{runId}/service-log`** — CONFIRMED run **rows·summary** · **15분 준수** 라벨 (`0cfa970`, Q407)
- [ ] **`PUT /api/v1/transport/runs/{runId}/service-log`** — 동승 직원·실제 픽업·동승·하차 저장 후 **GET 재조회** 일치 · DRAFT 시 **422** (`aaaeb10`, Q407)
- [ ] `GET /actuator/health` — **`{"status":"UP"}`** · PostgreSQL 중지 시 **503** + **`DOWN`** (`5d7be9f`/`3f32ae5`, Q413)
- [ ] **`GET /actuator/health/liveness`** · **`GET /actuator/livez`** — HTTP **200** · `{"status":"UP"}` — **DB 중지 시에도 UP** (`911a1b9`, Q413)
- [ ] **`GET /actuator/health/readiness`** · **`GET /actuator/readyz`** — **`/actuator/health`와 동일** · DB down 시 **503 DOWN** (`911a1b9`/`c19206a`, Q413)
- [ ] **`GET /api/v1/health`** — **`liveE2eOperationReady`**·**`liveE2eOperationBlocker`** 필드 존재 · bootstrap disabled 시 **`liveE2eOperationReady=false`** (`3908044`, Q419)
- [ ] **`HealthControllerTest`** — operation readiness·blocker reason matrix (`3908044`, Q419)
- [ ] **`GET /api/v1/health`** — probe runtime exception 시 **503** + `ready=false` · **`SELECT_1_FAILED_PROBE_EXCEPTION`** (500 아님, `3f32ae5`, Q413)
- [ ] **`/care/reports/nursing-service`** — **`CareNursingParityPanel`** **「L02·L03 간호 리포트 연계」** · L03 리포트·제공기록 링크 (`140bf92`, Q412)
- [ ] **`careNursingReportsLiveApi.e2e.test.js`** — L02_M14/M09/M10 **`GET /care/reports/*`** live routing (`5533ef5`, Q412)
- [ ] **`/reports/client-outings`** — 조회 form **`aria-label`** · StatCard **`role="group"`** · **`aria-busy`** (`9641ab1`, Q240)
- [ ] **`clientOutingReportLiveApi.e2e.test.js`** — **`GET /reports/client-outings?branchId=&yearMonth=`** live routing · `totalOutings`·`items[]` contract (`3a0110f`, Q240)
- [ ] **`LiveE2eBootstrapServiceTest`** — foreign-tenant seed UUID **safe client id** · **`LIVE_E2E_SEED_CLIENT_CONFLICT` 방지** (`87f901d`, Q409)
- [ ] **`GET /api/v1/transport/runs/{runId}/service-log/audit-trail`** — CONFIRMED run **items[]** · **`TRANSPORT_SERVICE_LOG_UPSERT`** · `runDate`·`stopUpdateCount`·`recorded`/`onTime`/`total` · **limit 50** (`5994d15`, Q411)
- [ ] **G15 audit-trail RBAC** — `caregiver` 토큰으로 `GET …/service-log/audit-trail` 시 **403**, `branch_admin` 토큰으로 동일 API **200** 확인
- [ ] **`/transport/runs/:runId`** — **`TransportServiceLogPanel`** **「일지 저장 이력」** 표 · 저장 후 자동 갱신 (`3cc5a08`, Q411)
- [ ] **`/settings` → 감사 로그** — 일지 저장 후 **`TRANSPORT_SERVICE_LOG_UPSERT`** 항목·`stopUpdateCount`·`summary` 확인 (`aa42b9c`, Q411)
- [ ] **`/transport/runs/:runId`** — **`TransportServiceLogPanel`** **미저장 변경 시 인쇄·텍스트 저장 차단** · **일지 보관·감사 추적** 패널 (`088e906`, Q411)
- [ ] **`GET /api/v1/transport/reports/monthly-service-variation?yearMonth=`** — `summary`·`rows` · **`caregiver` 403** (`5d27ad3`, Q410)
- [ ] **`GET /api/v1/transport/reports/monthly-resident-status?yearMonth=`** — 이동 대상·확정 배차·계약 서명 집계 (`5d27ad3`, Q410)
- [ ] **`/reports/transport-monthly`** — **2-7·2-8** StatCard·표 · **`TransportContextNav`「월간 리포트」** (`6a18dfd`, Q410)
- [ ] **월간 수치 대조** — `/reports/transport-monthly`의 `2-8 확정 배차` 수치가 `GET /transport/runs?direction=PICKUP&status=CONFIRMED` 집합과 일관한지 확인
- [ ] **일지 저장률 대조** — 샘플 run 3건에서 `GET /transport/runs/{runId}/service-log`의 `summary.recorded == summary.total` 확인 후 월간 리포트 검토
- [ ] **`GET /api/v1/system/live-e2e/probe`** — seed client lookup 실패 시 **200 + `clientReady=false`**(500 아님, `0b5657a`, Q409)
- [ ] **`/transport/runs/:runId`** — **`TransportServiceLogPanel`** **「일지 기록 저장」** · vehicle/driver **read-only** (`7a4b310`/`088e906`, Q407)
- [ ] **`liveE2eHarness.test`** — stale shell **`LIVE_E2E_*`** env **격리** (`b69c8ae`, QA-B119, Q408)
- [ ] **`LiveE2eBootstrapServiceTest`** — **cross-tenant seed ID·email collision** 회귀 (`2d6c063`, Q409)
- [ ] **`LiveE2eBootstrapServiceTest`** — client seed **conflict fallback** (`c13800c`, Q409)
- [ ] **`liveE2eHarness.test`** — staff bootstrap **embedded guardian token** 재사용 · **`bootstrap-guardian` 미호출** (`af4d7f8`, Q409)
- [ ] **`GET /api/v1/transport/roster`** — 확정 루트에 **`stopKind=null`** 레거시 정차가 있어도 **`confirmedDispatched=true`** (`1d1a71f`)
- [ ] **`PATCH /api/v1/transport/vehicles/{id}`** — **`defaultDriverName`** 저장·조회 (`114411f`, Q402)
- [ ] **`/transport`** — **승차/하차** segmented control · **방향별** 운행 루트·명단 카드 제목 (`45bd923`, Q399)
- [ ] **`/transport/runs/new`** — **`TransportRouteSplitView`** · **지점 추가** · 번호 마커 하이라이트 · **방향 state** 전달 (`45bd923`, Q401)
- [ ] **`MealAssistanceRecordPage.test`** — create flow **`waitForElementToBeRemoved`** · client option load (`45bd923`, QA-B116)
- [ ] **`koreanGeocode.test`** — region fallback·building-no scoring parity (`45bd923`, Q401)
- [ ] **`KakaoTransportMap.test.jsx`** — 지점 핀 **`aria-label`「지점(센터) 정차」** · 범례 도로/안내선 (`10489a7`, Q404)
- [ ] **`/transport/compliance`** — **`TransportCompliancePanel`**·**`TransportForm18GuidePanel`** 렌더 · **`TransportContextNav`** 수칙·계약 탭 (`84e75ec`, Q397)
- [ ] **`session.test.js`** — refresh token **`sessionStorage`** persist · **`restoreSession()`** reload (`84e75ec`, Q396)
- [ ] **`/transport/runs/new`** — **`VITE_KAKAO_MAP_JS_KEY`** 설정 시 **`KakaoTransportMapView`** 마커·폴리라인·seed markers 표시 · 미설정 시 **Alert**(Spinner 없음, Q394·Q395, `5ebaade`)
- [ ] **`kakaoMapInstance.test`** — 지도 인스턴스 생성·destroy 회귀 (`5ebaade`, Q395)
- [ ] `POST /api/v1/transport/route-preview` — 2곳 이상 정차 **`pickupLat`/`pickupLng`** 로 `status: OK` (`e8b8398`, Q370)
- [ ] `POST /api/v1/system/live-e2e/bootstrap-guardian` — guardian user·client·mapping seed · JWT·`clientId` 반환 (`f5205e3`, Q393)
- [ ] **`LiveE2eBootstrapServiceTest`** — 동일 tenant·동일 email·**다른 role** 계정 재사용 **차단** (`7ac0a46`, Q394)
- [ ] `GET /api/v1/system/live-e2e/probe` — **`guardianReady`·`guardianBootstrapEndpoint`** 필드 존재 (`f5205e3`)
- [ ] **`CareNursingReportsLiveApiRoutingE2eTest`** · **`BranchOnboardingSupportLiveApiRoutingE2eTest`** · **`StaffStatusReportLiveApiRoutingE2eTest`** — live API routing harness (`ec142db`)
- [ ] KST 22:00~08:00에 `POST /api/v1/billing/claims/{id}/notify` 호출 시 **`422 BUSINESS_RULE`**(quiet-hours 수동 발송 차단) 확인
- [ ] KST 22:00~08:00에 `POST /api/v1/clients/{clientId}/notifications/home-newsletter`(및 care-provision-record·elder-abuse-prevention-guideline) 호출 시 **`422 BUSINESS_RULE`** — **`NotificationQuietHoursPolicy.manualDispatchBlockedMessage()`** (Q539, `71b2d32`)
- [ ] **`scripts/dev-live-e2e.env`** 의 **`LIVE_E2E_BRANCH_ID`** 지점 **`serviceType`** 확인 — **`HOME_VISIT`(home-visit-like) 또는 legacy `DAY_CARE`** 이면 **`liveG21Describe`** suite 실행 · **그 외(예: 시설급여 전용)** 는 **`liveE2eG21SeedApplicable=false`** · **`g21-seed=not-applicable`** — **general live E2E는 `liveE2eOperationReady=true` 유지** (Q541, `091c372`)
- [ ] **`/transport/runs/new`** — **「이전 배차 불러오기」** Modal · **`TransportLoadPreviousRunModal`** (Q550, `4681b5a`)
- [ ] **`/transport/runs/:runId`** DRAFT — **「명단에서 추가」** · **확정 전 `TransportConfirmWarningModal`** — **`pickupToleranceMinutes`** 반영 (Q550, `4681b5a`/`48eea95`)
- [ ] **`PATCH /api/v1/transport/runs/{id}`** — **`plannedDepartureTime`** · **희망 시각 순서 역전 시 `422`** (Q550, `48eea95`)
- [ ] **`GET /api/v1/health`**·**`GET /api/v1/system/live-e2e/probe`** — **`guardian-credentials-missing`** vs **`guardian-credentials-default`** **분리** (Q551, `520f10a`) · **`allow-default-credentials=true`**(기본) 시 default creds **blocker 없음** (Q542)
- [ ] **`/staff/{userId}` → 「입사~퇴사」** — **`StaffEmploymentContractRenewalPanel`** — **「재계약 완료 기록」** Modal · checklist·서식 Modal (Q546·Q547, `033b319`/`1b6d2b1`)
- [ ] **`GET /api/v1/health`**·**`GET /api/v1/system/live-e2e/probe`** — **`liveE2eOperationBlockers[]`** 동일 — **`LiveE2eOperationReadinessSupport`** (Q548, `bfad37d`)
- [ ] **`/staff`** — **`StaffEmploymentContractRenewalSummaryPanel`** — **재계약 기한 초과·서명일 미등록** StatCard·확인 필요 표 (Q540, `10585b9`)
- [ ] **`/dashboard`·`/dashboard/hq`** — **「근로재계약 미충족」** StatCard → **`/staff` 링크** (Q540, `f31c346`)
- [ ] **`/staff/{userId}` → 「입사~퇴사」** — **`StaffEmploymentContractRenewalPanel`** — 서명일 등록 시 **+1년 재계약 기한**·**+3년 보관**·기한 초과 **warning Alert** (Q540, `f62402f`)
- [ ] `GET /api/v1/visits?scheduleKind=BILLING` — `pairedScheduleId` 있으나 페어 누락 시 **`billingClaimReflectionStatus=UNPAIRED`** (`e54a699`)
- [ ] `GET /api/v1/system/live-e2e/probe` — `credentialsConfigured` 필드 존재·env 미설정 시 `false` (`c5f1325`)

---

## 12. 장애 대응·트러블슈팅

| 증상 | 가능 원인 | 조치 |
|------|----------|------|
| 기동 실패 `JWT RSA key configuration is invalid` | PEM 형식 오류 | `JWT_PRIVATE_KEY`/`JWT_PUBLIC_KEY` PEM 헤더·줄바꿈 확인 |
| 기동 실패 Flyway | 마이그레이션 충돌·DB 버전 불일치 | `flyway_schema_history` 확인, 백업 후 수동 정합 |
| `500` PII 관련 | `PII_ENCRYPTION_KEY` 미설정·길이 오류 | Base64 32바이트 키 설정 (16/24/32 허용) |
| 로그인 후 즉시 401 | JWT issuer 불일치·키 변경 | `JWT_ISSUER`와 토큰 `iss` 일치, 키 영구 설정 |
| QR 스캔 실패 | `QR_TOKEN_SECRET` 불일치·만료 | 동일 시크릿·서버 시각(NTP) 확인 |
| 기동 실패 `prod 프로필에서는 ... 환경변수가 필수` | `prod` 시크릿 미설정 | `ProductionSecretValidator` — JWT·QR·DB_PASSWORD 설정 |
| 기동 실패 `LIVE_E2E_BOOTSTRAP_ENABLED/LIVE_E2E must be disabled in prod` | prod에 live E2E bootstrap 플래그 ON | **`aa6816a`** — prod에서 **`LIVE_E2E`·bootstrap flags OFF** (FAQ **Q384**) |
| `429 RATE_LIMITED` | 인증 rate limit 초과 | 1분 대기 후 재시도, `AUTH_*_RATE_LIMIT_*` 조정 |
| CORS 오류 | SPA·API 도메인 분리 | §6-4 동일 오리진 프록시 또는 CORS 허용 목록 |
| 느린 응답 | DB 커넥션·인덱스 | PostgreSQL slow query, V3/V6 인덱스 적용 확인 |

장애 시 `sysadmin`은 증상·시각·Tenant ID를 ogada ops에 전달하고, 복구 전후 `audit_logs`에 기록합니다 (`ADMIN_GUIDE.md` §4-4).

---

## 13. 관련 문서

| 문서 | 내용 |
|------|------|
| `docs/planning/REQUIREMENTS.md` | 비기능 요구·배포 원칙 |
| `docs/technical/API_SPEC.md` | REST API·인증 규약 |
| `docs/ops/ADMIN_GUIDE.md` | Tenant 온보딩·백업·보안 키 운영 |
| `docs/ops/DATA_RETENTION_POLICY.md` | 백업 보존·파기 정책 |
| `docs/planning/FLOWCHART.md` | 역할별 화면 흐름 |
| `src/backend/src/main/resources/application.yml` | 런타임 설정 기준 |

---

## 14. 변경 이력

| 날짜 | 변경 내용 |
|------|----------|
| 2026-06-23 | **336차** — §1-3·§11-3 **V175 leave-ledger integrity (Q668)**·**SOCIAL_WORKER users RBAC (Q669)**·**live-e2e tenant isolation (Q670)**·baseline **`c4e6bcb`/`426d63a`** |
| 2026-06-23 | **335차** — §1-3·§11-3 **US-R01-c leave-ledger UXD-157 a11y (Q667)**·**BNK-551 AVAILABLE sync**·baseline **`5fd12dd`/`426d63a`** |
| 2026-06-23 | **334차** — §1-3·§1-4·§11-3 **US-R01-c leave-ledger FE full-stack (Q666)**·**live routing harness**·baseline **`5fd12dd`/`8057c1e`** |
| 2026-06-23 | **333차** — §1-3·§11-3 **US-R01-c leave-ledger RBAC+pilot test (Q665)**·baseline **`62fce23`/`b7101d5`** |
| 2026-06-23 | **332차** — §1-3·§1-4 **US-R01-c leave-ledger BE API (Q663)**·§11-3 **V174·QA-B268 guard (Q664)**·baseline **`bb9df48`/`b7101d5`** |
| 2026-06-23 | **331차** — §1-3·§1-4 **baseline sync (331차)**·§11-3 **QA-B266 Fixed·G2 CMS Q662 smoke**·baseline **`f1225b0`/`949e9bf`** |
| 2026-06-23 | **330차** — §1-3 **baseline sync (330차)**·§11-3 **Vitest Q661 checklist**·**Q661 FAQ cross-ref**·baseline **`40ab9e7`/`949e9bf`** carry |
| 2026-06-23 | **329차** — §11-3 **QA-B266 full-suite test checklist (Q658)**·**US-R01-c leave-ledger P1 (Q659)**·**M6 v3.1 (Q660)**·merge gate **713 carry**·baseline **`40ab9e7`/`949e9bf`** |
| 2026-06-23 | **328차** — §11-3 **annual-leave multi-branch activeBranch fallback (Q656)**·**RelatedSurfacesPanel UXD-156·HR BranchScopeNotice (Q657)**·baseline **`40ab9e7`/`949e9bf`** |
| 2026-06-23 | **327차** — §4-3 **Solapi 발신번호 본인인증 외부 처리 (Q654)**·baseline **`83a26e7`/`95f55aa`** carry |
| 2026-06-23 | **326차** — §11-3 **work-attendance API `surfaceKind`·`relatedSurfaces` smoke (Q653)**·**HR nav 양방향 API closure**·baseline **`83a26e7`/`95f55aa`** |
| 2026-06-23 | **325차** — §11-3 **HR nav 양방향 smoke (Q652)**·**역할 분리 통합 참조**·baseline **`6ab3760`/`2040571`** carry |
| 2026-06-23 | **324차** — §1-3·§4-3·§11-3 **G-STAFF-WORK-ATTENDANCE reverse cross-links**·**Q651**·**Q648·Q650 deepen**·baseline **`6ab3760`/`2040571`** |
| 2026-06-23 | **323차** — §1-3·§4-3·§11-3 **yearly cross-link metadata·related surfaces FE panel**·**Q648 deepen·Q650**·baseline **`6ab3760`/`0b0d7ba`** |
| 2026-06-23 | **322차** — §1-3·§4-3·§11-3 **US-R01 roster cross-link metadata**·**live API harness·PILOT_CHECKLIST R03e/E05**·**Q648·Q649**·baseline **`bbf333c`/`e296387`** |
| 2026-06-23 | **321차** — §1-3·§4-3·§11-3 **V173 annual leave integrity probe**·**G-STAFF-ANNUAL-LEAVE UXD-155 a11y·Modal errors**·**Q645·Q646·Q647**·baseline **`8c5dd65`/`31ab1aa`** |
| 2026-06-22 | **320차** — §1-3·§4-3·§11-3 **J03 Solapi placeholder readiness guard**·**G-STAFF-ANNUAL-LEAVE validation·page title constant**·**Q641·Q642·Q643·Q644**·baseline **`19ffa84`/`971c7f1`** |
| 2026-06-22 | **317차** — §1-3·§1-4·§11-3 **G-STAFF-ANNUAL-LEAVE negative usage guard**·**live E2E credential variant recovery**·**Q639·Q640 deepen**·baseline **`a45745c`/`a170f9c`** |
| 2026-06-22 | **316차** — §1-3·§1-4·§11-3 **G-STAFF-ANNUAL-LEAVE test deepen**·**live E2E default-credential blocker recovery**·**Q640**·**Q639·Q580 갱신**·baseline **`6b84bcd`/`6fcd750`** |
| 2026-06-22 | **310차** — §1-3·§1-4·§11-3 **live E2E bootstrap blocker normalize**·**Q631**·**Q596·Q448 갱신**·baseline **`24d25f1`/`fdc135b`** |
| 2026-06-21 | **301차** — §1-3·§1-4·§11-3 **G-BILLING-DEPOSIT-ORDER-GUARD**·**G-STAFF 출근방식**·**Q614**·`a6eb8b7`·`5fd468b` |
| 2026-06-21 | **299차** — §1-3·§1-4 **G-ATTENDANCE-STATS**·**Q613**·baseline carry |
| 2026-06-21 | **298차** — §1-3·§1-4·§11-3 **G-STAFF-WORK-ATTENDANCE**·**V169**·**Q612**·`560057f`·`53d65a0` |
| 2026-06-21 | **297차** — §1-3·§11-3 **UXD-151 mobile capture CSS**·**Q611**·`61e1970`·`9812ac4` |
| 2026-06-21 | **296차** — §1-3·§1-4·§11-3 **G-ATTENDANCE-ROSTER-STATUS FE wire**·**Vitest serial pool**·**Q609·Q610**·`61e1970`·`8383f8d` |
| 2026-06-21 | **295차** — §1-3·§1-4·§11-3 **G-ATTENDANCE-ROSTER-STATUS**·**Q609**·**Q94 closure**·`61e1970`·`3bffb17` |
| 2026-06-21 | **294차** — §1-3·§11-3 **mobile HR capture**·**duplicate SMS guard**·**live E2E blocker priority**·**8-12 print cleanup**·**Q607–Q608**·`56cb5d9`·`6bde24a` |
| 2026-06-21 | **293차** — §1-3·§1-4·§11-3 **V168 overdue integrity**·**UXD-150 a11y**·**bootstrap error suffix**·**repository API wire**·**Q605–Q606**·`20485f1`·`751c593` |
| 2026-06-21 | **292차** — §1-3·§1-4·§11-3 **G-STAFF-DOCUMENT-REPOSITORY**·**overdue SMS auto-record guard**·**Q604·Q602 deepen**·`b583c11`·`03d0d43` |
| 2026-06-21 | **291차** — §1-3·§1-4·§11-3 **G-BATHING copy-from-previous-month**·**G-BILLING-OVERDUE-ADJUSTMENT**·**V167**·**Q598·Q602–Q603**·`c17097d`·`d2815d2` |
| 2026-06-21 | **290차** — §1-3·§1-4·§11-3 **G21 dashboard NHIS gap**·**G15 Kakao quota widget**·**bootstrap-error blocker suppression**·**Q594–Q597**·`0c9518a`·`580a86b` |
| 2026-06-21 | **288차** — §1-3·§1-4·§11-3 **G-BILLING appliedFilters FE wire**·**UXD-148 a11y**·**Q580 feature-scoped blockers**·**Q588**·`7b99313`·`e2f1246` |
| 2026-06-21 | **287차** — §1-3·§1-4·§11-3 **G-BILLING appliedFilters echo**·**Q580 snake_case blocker**·**Q587**·`14935a3`·`33e9e1a` |
| 2026-06-21 | **286차** — §1-3·§1-4·§11-3 **G-BILLING report FE wire**·**invalid month guard**·**Q585 closure·Q586**·`375fb9d`·`e38ccfd` |
| 2026-06-21 | **285차** — §1-3·§11-3 **G-STAFF-LEAVE-STATUS full-stack**·**G-BILLING deposit half-month·receipt dual-basis**·**Q584·Q585**·`b96d038`·`1a614c9` |
| 2026-06-21 | **284차** — §1-3·§11-3 **G-STAFF-LEAVE-STATUS ON_LEAVE**·**live E2E placeholder token bootstrap**·**Q584**·`68d4457`·`82a542c` |
| 2026-06-21 | **283차** — §1-3·§11-3 **NHIS header normalize**·**live E2E stale token recovery**·**Q582–Q583**·`2edbdc4`·`b60c622` |
| 2026-06-21 | **281차** — §1-3·§1-4·§3-7 **G-BANK-EXCEL-8 full-stack**·**live E2E placeholder guard**·**Q572·Q576·Q578**·`7d29a38`·`a18b30e` |
| 2026-06-21 | **280차** — §1-3·§1-4·§11-3 **G-STAFF-NHIS-EXCEL-IMPORT full-stack**·**bulk import rowNumbers**·**live E2E G21 trim**·**Q576–Q577**·`e3b74a0`·`4315ee2` |
| 2026-06-21 | **279차** — §1-3·§1-4·§11-3 **V165**·**G-BANK-EXCEL-8**·**G-STAFF-NHIS-EXCEL-IMPORT**·**US-H01**·**Q572–Q575**·`3bbfc00`·`a2f599c` |
| 2026-06-21 | **277차** — §1-3 **V161–V164**·**G14 care plan form**·**dashboard claimGenerationGuard**·**Q557**·`07a03c0`·`08a8b9f` |
| 2026-06-21 | **274차** — §1-3·§3-7·§4-7·§11-3 **V160 ogada_platform_admin**·**Kakao per-API quota**·**staff account request**·**Q554 갱신·Q555~Q556**·`3023c9e`·`380be3c` |
| 2026-06-21 | **273차** — §1-3·§3-7·§4-7·§11-3 **v1.3-A Kakao API status+usage probe**·**suggest route-preview embed**·**TransportKakaoApiStatusPanel**·**Q554**·`e2b764b`·`ba74bb5` |
| 2026-06-21 | **272차** — §1-3·§3-7·§11-3 **v1.3-A transport preview cache+roster ETA**·**G30/G39 nav label**·**Q553**·`48eea95`·`acc5933` |
| 2026-06-21 | **271차** — §1-3·§3-7·§11-3 **v1.3-A transport roster/ETA**·**guardian credential blockers**·**UXD-142 renewal a11y**·**Q550~Q552**·`48eea95`·`863b135` |
| 2026-06-21 | **270차** — §1-3·§3-7·§11-3 **FAQ21823 renewal record+due alerts**·**live E2E operation readiness centralization**·**Q547~Q549**·`bfad37d`·`16afd4c` |
| 2026-06-21 | **269차** — §1-3·§3-7·§11-3 **FAQ21823 clauses checklist+template modal**·**G21 not-applicable live E2E**·**Q546**·`091c372`·`1b6d2b1` |
| 2026-06-21 | **268차** — §1-3·§3-7·§11-3 **V159 identifier CHECK**·**health V159 probe**·**UXD-141 a11y**·**nested health parse**·**Q543~Q545**·`1139e79`·`202c1fe` |
| 2026-06-21 | **267차** — §1-3·§3-7·§11-3 **US-R03 FAQ21823 list+dashboard renewal**·**live E2E allow-default-credentials**·**Q540 갱신·Q542**·`beef81e`·`f31c346` |
| 2026-06-20 | **266차** — §1-3·§3-7·§11-3 **US-R03 FAQ21823 employment contract renewal**·**live E2E unsupported branch seed**·**Q540·Q541**·`7a9d7a5`·`f62402f` |
| 2026-06-20 | **265차** — §1-3·§3-7 **J03 guardian document quiet-hours**·**G-CASH-RECEIPT-LOG FE identifier validation**·**Q537 갱신·Q539**·`7e4c07e`·`0038846` |
| 2026-06-20 | **264차** — §1-3·§3-7 **G-CASH-RECEIPT-LOG numeric-only identifier**·**UXD-140 a11y**·**Q537 갱신·Q538**·`4da0ca8`·`501fedc` |
| 2026-06-20 | **263차** — §1-3·§3-7 **G-CASH-RECEIPT-LOG identifier normalize+validation**·**pending load error guard**·**Q537**·`298bcdf`·`35d1560`·`99b795a` |
| 2026-06-20 | **262차** — §1-3·§3-7 **G26 yearBasis+NTS CSV**·**G-7-1 Excel export**·**UXD-139 a11y**·**Q534~Q536**·`ceeaeb9`·`19ed7f3`·`e454d3b`·`58d6694` |
| 2026-06-20 | **261차** — §1-3·§3-7 **G-CASH-RECEIPT-LOG 4-계층 closure**·**HQ pending**·**prior-year advisory**·**Q533**·`58ff35e`·`8aebe55` |
| 2026-06-20 | **260차** — §1-3·§3-7 **G-CASH-RECEIPT-LOG dashboard due-gate**·**pending issuance API**·**Q532**·`ab5708b`·`221458e` |
| 2026-06-20 | **259차** — §1-3·§3-7 **G-CASH-RECEIPT-LOG payment bridge**·**live API harness**·**Q531 partial**·`a17f148`·`8e6e0c6` |
| 2026-06-20 | **258차** — §1-3 **G-CASH-RECEIPT-LOG full-stack**·**V158**·**Q530·Q531**·`4432558`·`cfc4b04`·`f79a19e` |
| 2026-06-19 | **257차** — §1-3·§3-7·§9-1 **G21 split-view dual NHIS**·**health G32 alignment**·**credential trim**·**UXD-138 a11y**·**Q526~Q530**·`7848b0f`·`d354a0e` |
| 2026-06-19 | **256차** — §1-3·§3-7·§9-1 G32 **probe schema readiness·stale runtime guard**·**케어포 3-1 health segment nav**·**Q524~Q525**·`45d95ea`·`1d5747d` |
| 2026-06-19 | **255차** — §1-3·§3-7·§9-1 G32 **FAQ21797 live E2E harness·pilot E2E extend**·**Q522~Q523**·`510d2f3`·`3f871d7` |
| 2026-06-19 | **254차** — §1-3·§9-1·§11-3 G32 **V157·중복 참석자·live E2E skip diagnostics**·**Q519~Q521**·`eed39ab`·`c7fb69a` |
| 2026-06-19 | **253차** — §1-3·§11-3 G32 **dashboard attendee-opinion gap widget**·**Q518**·`b9e0947`·`e55ae96` |
| 2026-06-20 | **252차** — §1-3·§3-7·§9-1·§11-3 G32 **FAQ21797 attendee opinions**·G2 **guardian document 3-type panel**·live E2E **health diagnostics**·**Q515~Q517**·`5222a8f`·`b272a7b`·`d1149a5` |
| 2026-06-19 | **251차** — §1-3·§3-7·§9-1·§11-3 G39 **FAQ21817 7-day SLA**·**RFID equivalence**·health **G21 branch blocker**·FE **billing gate**·**Q511~Q514**·`bc754a0`·`c3b6a5c`·`b881883` |
| 2026-06-19 | **250차** — §1-3·§9-1·§11-3 G21 **cross-branch seed scope**·**guardian bootstrap guard**·QA-B147 **batch-confirm loading**·UXD-136/137 **L03 edit a11y**·**Q507~Q510**·`02a2eb8`·`f86c76c` |
| 2026-06-19 | **249차** — §1-3·§9-1·§11-3 G21 **probe branch-missing blocker**·UXD-147 **batch-confirm NHIS ack a11y**·**Q505~Q506**·`7898aa5`·`0002943` |
| 2026-06-19 | **248차** — §1-3·§3-7·§9-1·§11-3 G21 **paired PLAN/BILLING seed**·**billing readiness probe**·**legacy DAY_CARE guard**·G41 **filter-year load guard**·**Q500~Q504**·`191703f`·`cefb7c7` |
| 2026-06-19 | **247차** — §1-3·§3-7·§9-1·§11-3 G21 **seed readiness**·**scoped fallback IDs**·**NHIS row-batch linkage**·**liveG21Describe gate**·**Q495~Q499**·`c0403b0`·`d61ab5e` |
| 2026-06-19 | **246차** — §1-3·§3-6·§11-3 live E2E **health/probe alignment**·**org-scoped bootstrap IDs**·UXD-134 **a11y**·**LIVE_E2E_CLIENT_ID whitespace guard**·**Q491~Q494**·`8fe1ccd`·`cf85003` |
| 2026-06-19 | **245차** — §1-3·§3-6·§11-3 live E2E **probe default-credentials blocker**·G41 **filter-year inline error**·**Q489·Q490**·`f932fd3`·`28e5525` |
| 2026-06-19 | **244차** — §1-3·§3-6 G41 **reference-year input guard**·**Q489**·`b73e5f4`·`f26e075` |
| 2026-06-18 | **243차** — §1-3·§3-6·§11-3 G21 **NHIS comparison panel+per-client drill-down FE closure**·live E2E **NHIS import seed**·**Q479·Q484 갱신·Q486~Q488**·`b73e5f4`·`797c529` |
| 2026-06-18 | **242차** — §1-3·§3-6 G21 **NHIS summary deepen+Modal StatCard FE wire**·UXD-133 **print a11y**·**Q479·Q481 갱신·Q483~Q485**·`39fa41a`·`68a4e35` |
| 2026-06-18 | **241차** — §1-3·§3-6 G21 **confirm-readiness NHIS summary embed**·**RFID no-diff success alert**·**Q479 갱신·Q481~Q482**·`8a8c5b3`·`f232285` |
| 2026-06-18 | **240차** — §1-3·§3-6 G21 **visit NHIS comparison API**·**unassigned batch-confirm gate**·**VisitsContextNav URL sync**·**RFID diff normalize deepen**·**Q477·Q456 갱신·Q479~Q480**·`03a052a`·`570912e`·`3a27303`·`5f710e3` |
| 2026-06-18 | **239차** — §1-3 G21 **per-kind readiness deepen+FE StatCard**·G-7-1 **unpaid all-print label**·**Q477~Q478**·`f26abb0`·`f9ed97d`·`f5639df` |
| 2026-06-19 | **238차** — §1-3 G21 **readiness split**·G-7-1 **print bundle**·UXD-132 **a11y**·**Q474~Q476**·`6aeafe7`·`50d330d`·`f8321c7` |
| 2026-06-18 | **237차** — §1-3·§9-1·§11-3 G15 **service log direction**·live E2E **probe bootstrap-disabled·guardian FE align**·**Q471~Q473**·`72124f7`·`8cf09d8`·`94c65e2` |
| 2026-06-18 | **236차** — §1-3·§11-3 G15 **별지 제22호 form completion·branch contact·pickupAddress API**·**Q468~Q470**·`07be394`·`b1a16ff`·`e358f2d` |
| 2026-06-18 | **235차** — §1-3·§11-3 G15 **per-stop form parity**·V155 **waypoint test deepen**·**Q466~Q467**·`7de5a6f`·`a179256` |
| 2026-06-18 | **234차** — §1-3·§11-3 V155 **waypoint**·G41 **PDF 8-7·dashboard widget·8-7-1 export**·G15 **print pickup**·live E2E **visit·transport seed**·**Q458~Q465**·`64c4c80`·`caa215f` |
| 2026-06-18 | **232차** — §1-3·§11-3 G21 **RFID diff rendering**·visit check-in **supervisory role**·live E2E **HOME_VISIT seed**·**Q455~Q457**·`4a112fe`·`78cfb8a`·`9e050b1` |
| 2026-06-18 | **231차** — §1-3·§3-6·§11-3 G21 **RFID compare UI**·visit check-in **assigned-user guard**·L02_M07 **body restraint normalization**·**Q452·Q453·Q454**·`27c9de3`·`0db1e68`·`4a47675` |
| 2026-06-18 | **230차** — §1-3·§3-6·§11-3 UXD-130 **driver signature fieldset**·live E2E **guardian suite gate**·G21 **RFID compare API**·**Q450~Q452**·`bfe0283`·`7424c30`·`eeac205` |
| 2026-06-18 | **229차** — §1-3·§3-6·§11-3 live E2E **bootstrap error blockers**·L02_M13 **create client normalization**·**Q448·Q449**·`d7f1a9a`·`1c8f236` |
| 2026-06-18 | **228차** — §1-3·§3-7·§11-3 G15 **driver signature**·**service-log legal guide**·live E2E **operationBlockers**·**Q445~Q447**·`bc3a35c`·`f51e365` |
| 2026-06-18 | **227차** — §1-3·§11-3 G15 **server legal field guard**·staff **health checkup HR file hub wire**·**Q443·Q444**·`ac1d43f`·`b6ce301` |
| 2026-06-18 | **226차** — §1-3·§3-6·§11-3 G15 **legal field guard**·**duplicate rejection**·probe **operation readiness**·L02_M13 **malformed API**·**Q439~Q442**·`b4644e8`·`52e3340` |
| 2026-06-18 | **225차** — §1-3·§3-6·§11-3 staff **new-hire health checkup document window**·live E2E **readiness/retry**·QA-B133 **DateInput test**·**Q435~Q438**·`8e6310a`·`2e6c35f` |
| 2026-06-18 | **224차** — §1-3·§11-3 transport **roster planned pickup hub**·QA-B132 **StaffLifecyclePanel test**·**Q433·Q434**·`e35efb2`·`101aaee` |
| 2026-06-18 | **223차** — §1-3·§3-6·§11-3 QA-B131 **`test:live-e2e` script path**·DatePicker **keyboard a11y**·**V153**·G15 service log harness·**Q429~Q432**·`8882d9f`·`4c5d3bc` |
| 2026-06-17 | **222차** — §1-3·§3-6·§11-3 G30 **`MonitoringEvidenceContextPanel`**·live E2E **guardian default credentials**·**Q391·Q428**·`7d2cb4a`·`09df8c7` |
| 2026-06-17 | **221차** — §1-3·§3-6·§11-3 G15 **compliance→일지 hub**·live E2E **bootstrap/probe harden**·**Q426·Q427**·`b93e098`·`b2c09e1`·`844227a` |
| 2026-06-17 | **220차** — §1-3·§3-6·§11-3 live E2E **nested bootstrap payload**·**Q409·Q425**·`fc916db` |
| 2026-06-18 | **219차** — §1-3·§2-2·§9-1·§11-3 **`/actuator/healthz`**·DateInput/TimeInput **QA-B127**·Q413·Q422·`2157df5`·`ab4de83` |
| 2026-06-18 | **218차** — §1-3·§11-3 transport **settings validation**·**compact dispatch**·V152 **committed**·Q424·`dd2fa2c`·`96db8bf` |
| 2026-06-17 | **217차** — §1-3·§9-1·§11-3 staff bootstrap **embedded guardian tokens**·V152 transport guard·Q409·Q423·`73cffc5` |
| 2026-06-18 | **216차** — §1-3·§3-7·§9-1·§11-3 경유지 FE·DatePicker+TimeInput·ETA chip·SMTP readiness·Q421·Q422·`bf73c4c`·`ea5d896`·`704478f` |
| 2026-06-17 | **215차** — §1-3·§9-1·§11-3 V151 WAYPOINT·경유지 smoke·Q421·`de3474d`·FE WT |
| 2026-06-18 | **214차** — §1-3·§9-1·§11-3 V150 planned departure·`liveE2eOperationReady`·transport ETA·split-view UX·Q418·Q419·Q420·`0e46b37`·`fde098f` |
| 2026-06-18 | **213차** — §1-3·§3-4·§9-1·§11-3 actuator readyz/livez·liveness/readiness split·Q413·`f0e52b8`·`0baabe9` |
| 2026-06-18 | **211차** — §1-3·§3-4·§9-1·§11-3 actuator liveness/readiness·health probe harden·G15 outing live E2E·Q240·Q413·`30243f7`·`3a0110f`·`b48252a` |
| 2026-06-18 | **210차** — §1-3·§3-4·§11-3 L02/L03 parity·actuator health·live E2E safe client id·Q240·Q412·Q413·`140bf92`·`5533ef5`·`87f901d`·`5d7be9f` |
| 2026-06-18 | **209차** — §1-3·§11-3 G15 audit trail read API·live E2E cross-tenant bootstrap·Q411·Q409·`5994d15`·`3cc5a08`·`2d6c063` |
| 2026-06-17 | **208차** — §1-3·§11-3 G15 일지 감사·보관 UX·월간 리포트 2-7/2-8·probe seed guard·Q410·Q411·`aa42b9c`·`6a18dfd` |
| 2026-06-17 | **207차** — §1-3·§3-6·§11-3 QA-B95 bootstrap client fallback·guardian token reuse·Q409·`c13800c`·`af4d7f8` |
| 2026-06-17 | **206차** — §1-3·§3-6·§11-3 G15 service log API full stack·V148·QA-B119 harness·Q407·Q408·`aaaeb10`·`7a4b310` |
| 2026-06-17 | **205차** — §1-3·§9-1·§11-3 QA-B95 health seed metadata·US-E04 QR a11y·Q360·Q393·Q405·Q406·`2926287`·`99f2f3e` |
| 2026-06-17 | **204차** — §1-3·§3-6·§11-3 QA-B95 staff clientId·probe·login fallback·pilot E2E stabilize·Q360·Q393·`d8d51a7`·`6f2a4eb` |
| 2026-06-16 | **203차** — §1-3·§3-6·§11-3 QA-B95 live E2E deepen·V147 guardian trigger·Q360·Q393·`b1a6aff`·`4e99ae1` |
| 2026-06-17 | **202차** — §1-3·§11-3 QA-B116 direction-aware runs·TransportDeleteRunModal FE closure·Q399·Q403·`1d1a71f`·`45bd923` |
| 2026-06-16 | **201차** — §1-3·§11-3 QA-B117 DELETE draft runs·geocode scoring·US-T02 map pin a11y·Q403~Q404·`1d1a71f`·`10489a7` |
| 2026-06-17 | **200차** — §1-3·§11-3 US-T02 branch waypoints·DROPOFF·desired times·defaultDriverName·Q399~Q402·`114411f`·`d3bef42` |
| 2026-06-17 | **199차** — §1-3·§11-3 BNK-288 transport compliance·SEC-005 tab session·roster guardianContact·Q396~Q398·`35e03ef`·`84e75ec` |
| 2026-06-17 | **198차** — §1-3·§3-6·§4-7·§11-3 QA-B114 Kakao map instance refactor·SideNav dedup·Q370·Q394·Q395·`7ac0a46`·`5ebaade` |
| 2026-06-17 | **197차** — §3-6·§4-7·§11-3 QA-B113 Kakao Maps JS SDK preview·QA-B95 role-mismatch seed guard·Q370·Q393·Q394·`7ac0a46`·`b000d92` |
| 2026-06-17 | **196차** — §1-3·§3-6·§11-3 QA-B95 guardian bootstrap·live API routing E2E·Q393·`ec142db`·`b3bd0cc` |
| 2026-06-17 | **195차** — §1-3·§3-6·§11-3 L02 nursing BE pilot E2E·G26/G24b monitoring labels·G7 year-coverage message·Q391~Q392·`2ba2761`·`d499130` |
| 2026-06-17 | **194차** — §1-3·§3-7·§11-3 live E2E bootstrap fix·pilot E2E·Q389~Q390·`304bb2a`·`8ed937c` |
| 2026-06-17 | **193차** — §1-3·§11-3 L02 care-scoped nursing reports·G21 UNPAIRED·live E2E probe·Q386~Q388·`002e3eb`·`58ee122` |
| 2026-06-17 | **188차** — §1-3·§3-6 G26 ③ transport fee statistics·L02 care report RBAC·Q382·Q383·`2495753`·`09e4ec1` |
| 2026-06-17 | **187차** — §1-3·§3-6 G26 statistics dashboard FE full stack·pilot E2E·Q379·Q380·Q381·`3481eb8`·`31544cf` |
| 2026-06-16 | **186차** — §1-3·§3-6·G26 dual statistics E2E harness·live E2E env parse·Q379·Q380·Q360·`92ae60b`·`e10113f` |
| 2026-06-16 | **185차** — §1-3·§3-6·live E2E G26 branch billing reports·Q379·Q380·Q360·`903f462`·`472cb1d`·`9006a53` |
| 2026-06-16 | **184차** — §1-3 G21 RFID split-view·L02 care nav cross-links·L02/G21 a11y·Q377·Q378·`b38c6f7`·`6759bf6` |
| 2026-06-16 | **183차** — §1-3 G21 claim reflection FE·pilot E2E·Q376·`b38c6f7`·`25ca88e` |
| 2026-06-16 | **182차** — §1-3·§3-6 L02_M11/M12 FE·L02_M16·G21 claim reflection·V142·Q373~Q376·`6da49aa`·`8b804fc` |
| 2026-06-16 | **181차** — §1-3·§3-6·§4-7 L02_M17/M06 report FE·L02_M11/M12 BE·probe flags·Q371~Q374·`2cf0908`·`40684a9` |
| 2026-06-16 | **180차** — §1-3·§3-6·§4-7 L02_M17/M06 report BE·transport a11y·Q371·Q372·`9cc0c1d`·`1daeda7` |
| 2026-06-16 | **179차** — §1-3·§3-6·§4-7 L02_M04/M05 FE·route-preview·Q369·Q370·`3eeac92`·`46971e1` |
| 2026-06-16 | **178차** — §1-3·§3-4·§3-6·§3-7·§4-3·§9-1 L02_M13·L02_M15·G30 phone panel·L02_M04/M05·live E2E probe·Q366·Q368·Q369·Q360·`c655743`·`3549896` |
| 2026-06-15 | **177차** — §1-3·§3-4·§3-6·§4-3·§9-1 L02_M13 BE·V139/V140·J03 blockers·health harden·live E2E root·Q366~Q367·`81a2223`·`15b09df`·1437/1441·1284/1284 |
| 2026-06-16 | **176차** — §1-3·§3-4·§3-6·§3-7·§9-1 L02_M01/M03·G-7-1-4CHANNEL·G30 satisfied·live E2E harness·Q362~Q365·`344a28b`·`1fd1434`·1432/1432·1272/1272 |
| 2026-06-16 | **175차** — §1-3·§3-4·§3-6·§3-7·§9-1 L02_M07 FE·V132·health databaseStatusDetail·live E2E placeholder guard·Q361·Q360·`8b7e476`·`10f32c4`·1393/1393·1231/1231 |
| 2026-06-16 | **174차** — §1-3·§3-4·§3-6·§3-7·§9-1 L02_M02 FE·L02_M07 BE·health ping·live E2E gating·Q359·Q361·`df14e15`·`95e7e96`·1381/1381·1228/1228 |
| 2026-06-15 | **173차** — §1-3·§3-4·§3-6·§3-7·§9-1 L02_M02·health readiness·G19 harness·live E2E probe·Q359·Q360·`fd42b7e`·`5f17beb`·1367/1367·1214/1214 |
| 2026-06-15 | **172차** — §1-3·§3-6·live E2E harness G39 dispatch·G30 evidence window·Q358·QA-B96·`4d1a4f2`·`73094f9`·`73df04d`·1357/1357·1201/1201 |
| 2026-06-15 | **171차** — §1-3·§3-6·live E2E env G24b status·G19 discovery·Q357·QA-B95·`b5af5fa`·`9afa30e`·`41d8de5`·1355/1355·1197/1197 |
| 2026-06-15 | **170차** — §1-3·§3-6 G24b dashboard·G41 V129·7-5 alias·Q356·Q355·`ca0b627`·`b1c92e1`·`3cbe582`·`1e21b20`·1347/1347·1192/1192 |
| 2026-06-15 | **169차** — §1-3·§3-6 G24b compliance API·G24b a11y·G41 Locale.ROOT·L03 notes·Q355·`345c0cb`·`c97706b`·1325/1327·1182/1182 |
| 2026-06-15 | **168차** — §1-3·§3-6·§4-6-1·§8-1 G24b V128·QA-B94 openedOn·live E2E harness·Q354·Q353·`45fb6d9`·`49fbf67`·1323/1323·1173/1173 |
| 2026-06-15 | **167차** — §1-3·§3-6·§4-6-1·§8-1 G-ONBOARD V126/V127·Q353·`735dd53`·`4c1fd43`·`79d593c`·1320/1320·1171/1171 |
| 2026-06-15 | **166차** — §1-3·§3-6·§4-6-1·§8-1 US-UX-05 sessionStorage·QA-B93·L03 date window·pilot E2E·Q331·Q352·`a728f1b`·`548f670`·1315/1316·1162/1162 |
| 2026-06-15 | **165차** — §1-3·§3-6·§4-6-1·§8-1 L03_M01/M06/M07/M09/M10/M15·V125·Q348~Q351·`5edc45c`·`671a704`·1315/1315·246/246 |
| 2026-06-15 | **164차** — §1-3·§3-6·§4-6-1·§8-1 v1.3-B FE wire·L03_M01 V123·Q347·Q348·`9bd1660`·`edfba7f`·1274/1274·1131/1131 |
| 2026-06-14 | **163차** — §1-3·§3-6·§4-6-1·§8-1 G21 기간 가드·v1.3-B suggest API·V120~V122·Q330·Q347·`230659a`·`c865d2b`·1267/1267·1121/1121 |
| 2026-06-14 | **162차** — §1-3·§3-6·§4-6-1·§8-1 L03_M13·L03_M04 FE wire·Q344~Q346·`090b2d7`·`97108f2`·1261/1263·1115/1115 |
| 2026-06-14 | **161차** — §1-3·§3-6·§4-6-1·§8-1 L03_M14 FE wire·미래일자 가드·Q343~Q344·`63cb193`·`962858b`·1228/1228·1095/1095 |
| 2026-06-14 | **160차** — §1-3·§3-6·§4-6-1·§8-1 L03_M11 V115·L03_M14 V116·Q340~Q343·`e95df4c`·`5780c65`·1209/1209 |
| 2026-06-14 | **159차** — §1-3·§3-6·§4-6-1·§8-1 G-NURSING V114·Q336~Q339·`24a1c5c`·`024e720`·1073/1192 |
| 2026-06-14 | **158차** — §1-3·§3-6·§4-6-1·§8-1 G17b V112/V113·Q333~Q335·`3bd6a43`·`487416d`·1060/1164 |
| 2026-06-14 | **157차** — §1-3·§3-6·§4-6-1·§8-1 G21 batch-confirm·V111·J03 shared quiet-hours·Q330~Q332·`ba7d84f`·`c26cfa7`·1060/1160 |
| 2026-06-14 | **154차** — §1-3·§3-6·§4-6-1·§8-1 J03 quiet-hours billing UI·7-5 provider deepen·Q329·`9a4ab8e`·`111f056`·1030/1141 |
| 2026-06-14 | **153차** — §1-3·§3-6·§4-6-1·§8-1 G2/7-5 V110·US-L06·Q328·`16a0734`·`51f2505`·1024/1133 |
| 2026-06-14 | **152차** — §1-3·§3-6·§4-6-1·§8-1 G2/7-5 easy payment·V108–V109·Q326·Q327·`b893e97`·`bebd874`·1023/1126 |
| 2026-06-14 | **151차** — §1-3·§3-6·§8-1 G41b compliance·V107·Q325·`ee42e5d`·`45a724a`·246/1110 |
| 2026-06-14 | **149차** — §1-3·§3-6·§8-1 G41/G41b 기관 교육일지·V104–V106·Q321·`6191b91`·`e69bf00`·1004/1099 |
| 2026-06-14 | **148차** — §1-3·§3-6·§8-1 G30 checklist·G34-QUAL panel·US-S02 POST·Q320·Q319·`b1dfd34`·`574bd08`·989/1088 |
| 2026-06-14 | **147차** — §1-3·§3-6·§8-1 G34-QUAL BE guard·UXD-97 J03 a11y·Q318·Q319·`726b3de`·`76b5ff0`·975/1084 |
| 2026-06-14 | **146차** — §1-3·§3-6·§8-1 J03 readiness deepen·UI·8-12 pagination·G34-QUAL·Q318·Q319·`fffd355`·`443efca`·968/1081 |
| 2026-06-14 | **145차** — §1-3·§3-6·§8-1 8-12 BE CSV·G42 follow-up·#44 V103·J03 channel-status·Q316~Q318·`bc927f7`·`6012044`·960/1071 |
| 2026-06-13 | **144차** — §1-3·§3-6·§8-1 G30 V100/V101·8-12 aggregated API·export 7종·Q314·Q315·`5692662`·`07956f5`·935/1051 |
| 2026-06-13 | **142차** — §1-3·§3-6·§8-1 G9-COG import gate·V99·apply-nhis-seeds·G9-COPAY-NAMING·Q260·Q311·Q313·`8bb6583`·`a5c2736`·902/1022 |
| 2026-06-13 | **141차** — §1-3·§3-6·§8-1 G9-COG·FAQ21824 lifecycle·G-7x-1 YearMonth·Q311·Q312·`2efc557`·`6ef671b`·894/1017 |
| 2026-06-13 | **140차** — §1-3·§3-6·§8-1 G42 pending-approval·G-7x-1-guard·US-T14 익명함·Q309·Q310·`6f6094d`·`338c014`·886/1009 |
| 2026-06-13 | **139차** — §1-3·§3-6·§8-1 US-R02 직원현황 리포트·G34b import-draft API·Q308·`8487667`·`02cbd05`·882/1001 |
| 2026-06-13 | **138차** — §1-3·§3-6·§8-1 G42 고충상담·G34b 전월 복제·G21 check-in guard·V97·Q305·Q306·Q307·`0460e9b`·872/989 |
| 2026-06-13 | **137차** — §1-3·§3-6·§8-1 G34b 업무수행일지 불러오기·G21 assignedUser guard·Q303·Q304·`0ce04ad`·850/960 |
| 2026-06-13 | **136차** — §1-3·§3-6·§8-1 G40b 반기 기초평가·V95/V96·Q302·`a7b4a39`·`fad6df1`·845/948 |
| 2026-06-13 | **135차** — §1-3·§3-6·§8-1 G40 대시보드 widget·V94·`2589b94`·`e89175e`·831/931 |
| 2026-06-13 | **134차** — §1-3·§3-6·§8-1 G40 FE 위험도평가 UI·QA-B62·`686d686`·`9f80082`·830/925 |
| 2026-06-13 | **133차** — §1-3·§3-6·§8-1 G40 admission risk assessment·V93·US-R03 per-staff compliance·G21 MIME·Q301·827/917 |
| 2026-06-14 | **132차** — §1-3·§3-6·§8-1 FAQ21806 onboarding compliance·V92·Q300·813/908 |
| 2026-06-13 | **131차** — §1-3·§3-6·§4-6·§8-1 G2 CMS 해지·이력·duplicate guard·Q299·807/900 |
| 2026-06-13 | **130차** — §1-3·§3-6·§8-1 US-R03 HR file hub·V90/V91·FAQ21806·G2 CMS reactivation·Q298·797/898 |
| 2026-06-13 | **129차** — §1-3·§3-6·§8-1 G21 xls Content-Type casing·US-S02 입사일 미등록 StatCard·V90 WT·Q294·Q297·786/883 |
| 2026-06-13 | **128차** — §1-3·§3-6·§8-1 US-R02 staff health checkup 8-10·V89·G21 legacy xls·Q296·Q297·785/883 |
| 2026-06-13 | **127차** — §1-3·§3-6·§8-1 US-S02 refresher training certificate upload·V88·Q295·764/871 |
| 2026-06-13 | **126차** — §1-3·§3-6·§8-1 US-S02 refresher training·G34 sign modal·US-R03 lifecycle UX·G21 import MIME·755/866 |
| 2026-06-13 | **125차** — §1-3·§3-6·§8-1 US-R03 V87 date integrity·lifecycle Badge·`b3e59e2`·743/853 |
| 2026-06-13 | **124차** — §1-3·§3-6·§3-7 US-R03 offboarding guard·G21 draft sync·G34 signature audit·QA-B55·741/844 |
| 2026-06-13 | **123차** — §1-3·§3-6·§8-1 US-R03 staff lifecycle·V86·G21 `588bfb1`·Q290 Partial Fixed·731/843 |
| 2026-06-12 | **122차** — §1-3·§3-6·§3-7 G21 legacy paired guard·G24 fiscal-year parsing·G34 live E2E harness·BNK-125~127·Q289~Q292·724/827 |
| 2026-06-12 | **121차** — §1-3·§3-6 G24-G14 needs assessment·contract attachments·V83–V85·Q285·Q286·722/823 |
| 2026-06-12 | **118차** — §1-3·§3-6·§3-7 G34 lead caregiver work log BE+FE·V82·G21 paired linkage guard·Q284·Q288·689/800 |
| 2026-06-12 | **117차** — §1-3·§3-6·§3-7 LifecycleWorkflowPanel·G21 paired visit guard·Q238·Q283~Q287·675/782 |
| 2026-06-12 | **116차** — §1-3·§3-6·§3-7 QA-B49 parallel fallback·G17/G32 edit-flow pilot E2E·672/778 |
| 2026-06-12 | **115차** — §1-3·§3-6·§3-7 QA-B49 billing/NHIS snapshot·FE compliance snapshot-first·Q282·667/773 |
| 2026-06-12 | **114차** — §1-3·§3-6·§3-7 G17/G32/G38/G39 dashboard compliance snapshot·DateInput G11/G15·Q280·Q281·667/772 |
| 2026-06-12 | **113차** — §1-3·§3-6·§3-7 G17/G32 edit UI·G39 dashboard 4-pillar·dashboard compliance counts·BNK-112 E2E·Q279·666/769 |
| 2026-06-12 | **112차** — §1-3·§3-6·§3-7 G38 monitoring UI·branch-scoped compliance·dashboard partial-load·Q277 Fixed·661/765 |
| 2026-06-12 | **111차** — §1-3·§3-6·§3-7 G38·G39·G21 import validation·V80/V81·Q276~Q278·659/751 |
| 2026-06-12 | **110차** — §1-3·§3-6·§3-7 G21 visit enum normalize·G37 attachment E2E·Q275·642/735 |
| 2026-06-12 | **109차** — §1-3·§3-6·§3-7·§4-8 G37 grade history attachments·BNK-105·V78/V79·Q274·637/725 |
| 2026-06-12 | **108차** — §1-3·§3-6·§3-7·§8-1 J03 primary guardian·CMS FAILED response·UXD-81·BNK-102~104·programComplianceLiveApi·Q272·Q273·623/705 |
| 2026-06-12 | **102차** — §1-3·§3-6·§3-7·§8-1 G33 settle UI·G17 BNK-100/101·CMS failed debit·Q270 Fixed·Q271·608/693 |
| 2026-06-11 | **101차** — §1-3·§3-6·§3-7·§8-1 G33 settle API·V77·claim guard·Q270·604/682 |
| 2026-06-11 | **100차** — §1-3·§3-6·§3-7·§8-1 G33 BNK-94 billing start balance·V76·Q269·603/679 |
| 2026-06-11 | **99차** — §1-3·§3-6·§3-7·§4-3·§8-1 UXD-79 지표29 StatCard·파일럿 fixture·US-D01 primaryGuardian·tenant filter·Q266 Fixed·Q268·584/662 |
| 2026-06-11 | **98차** — §1-3·§3-6·§3-7·§4-3·§8-1 BNK-92 G32 plan FE·지표29 compliance·hq_admin 이용자 등록·Solapi template guard·Q265 Fixed·Q266·Q267·581/654 |
| 2026-06-11 | **97차** — §1-3·§3-6·§3-7·§8-1 BNK-91 P2 NHIS copay·discrepancy UX·G32 plan field·CMS re-register·V75·Q264·Q265·577/649 |
| 2026-06-11 | **96차** — §1-3·§3-6·§3-7·§8-1 BNK-87 NHIS comparison FE UI·Q264 Fixed·576/646 |
| 2026-06-11 | **95차** — §1-3·§3-6·§3-7·§8-1 BNK-87 NHIS comparison API·V74·G17/G32 compliance·dashboard 30일 widget·Q264·576/631 |
| 2026-06-11 | **94차** — §1-3·§3-6·§3-7·§8-1 G17·G32 FE·G32 case management API·V73·Q262 Fixed·Q263·569/626 |
| 2026-06-11 | **92차** — §1-3·§3-6·§3-7 US-M03 billing ledger report API·US-G04 year-coverage pre-check·Q179 Fixed·Q260·491/607 |
| 2026-06-11 | **91차** — §1-3·§3-6·§3-7 US-G04 fee schedule year guard·US-L01 bank sample xlsx·Q258·Q260·532/602 |
| 2026-06-11 | **90차** — §1-3·§3-6·§3-7·§8-1 G26 NTS xlsx·US-L01 8-bank guide·G21 visit slot guards·Q258–Q259·528/593 |
| 2026-06-11 | **89차** — §1-3·§3-6·§3-7 G2 copayAmount null guard·G26 UI exclusion guidance·UXD-77·Q257·521/574 |
| 2026-06-11 | **88차** — §1-3·§3-6·§3-7·§4-6·§8-1 G26 CMS·EASY_PAY 의료비공제 제외·G2 CMS debit integrity·US-L04 조회 UX·Q254–Q256·519/569 |
| 2026-06-11 | **87차** — §1-3·§3-6·§3-7·§8-1 G26 medical expense deduction API·US-L04 UI·UXD-76 VehiclesPage a11y·Q252–Q253·514/567 |
| 2026-06-11 | **86차** — §1-3·§3-6·§3-7·§8-1 G2 recordCopayPayment paidAt guard·US-J02 guardian portal race guards·Q250–Q251·509/555 |
| 2026-06-11 | **85차** — §1-3·§3-6·§3-7·§8-1 G21 HOME_CARE alias·G2 paymentMethod guard·UXD-75 RecordsContextNav·Q248–Q249·508/553 |
| 2026-06-11 | **84차** — §1-3·§3-6·§3-7·§8-1 G7 guidance API restore·G16 cross-branch fee guard·Form18 3-way workflow·Q111·Q133·Q237·Q247·503/547 |
| 2026-06-11 | **83차** — §1-3·§3-6·§3-7·§8-1 QA-B24 guidance UI·V70 integrity·guardian DRAFT filter·Q133·Q212·Q245–Q246·498/543 |
| 2026-06-11 | **82차** — §1-3·§3-6·§3-7·§8-1 G15 care-provision·G16 VehiclesPage·G2 paidAt·Q243–Q244·497/534 |
| 2026-06-10 | **81차** — §1-3·§3-6·§3-7·§8-1 G16 service-fee·vehicles·G15 outings·V66–V69·UXD-73·Q239–Q242·482/524 |
| 2026-06-11 | **80차** — §1-3·§3-6·§3-7 G15 Form22 log·Form18 guide·time compliance·G21 paired check-in sync·Q236–Q238·459/508 |
| 2026-06-11 | **79차** — §1-3·§3-6·§3-7·§8-1 V65 transport contract integrity·G21 duplicate visit import·QA-B19 geocode guard 강화·Q234·Q235·457/485 |
| 2026-06-11 | **78차** — §1-3·§3-6·§3-7·§8-1 G15 출석 transportMode 이원화·QA-B19 geocode 저장 차단·Q232·Q233·455/484 |
| 2026-06-10 | **77차** — §1-3·§3-6·§3-7·§8-1 G11 출석 기반 자동 가산·preview API·가드 보강·Q225·Q229·450/476 |
| 2026-06-10 | **76차** — §1-3·§3-6·§3-7·§8-1 G15 transport contract API·FE 연동·V64·Q230·Q231·444/472 |
| 2026-06-10 | **75차** — §1-3·§3-6·§3-7·§4-3 G11 가산율 catalog·G15 수칙 UI·Solapi startup guard·US-M04 cap success banner·Q226·Q229–Q230·434/467 |
| 2026-06-10 | **74차** — §1-3·§3-6·§3-7·§4-8·§8-1 G27 인지지원 월한도 BE·US-L01 bank branchId Fixed·SMTP guard·Q226·Q227·Q228·420/451 |
| 2026-06-10 | **73차** — §1-3·§3-6·§3-7·§8-1 BNK-49 US-M04·US-L01 bank FE UI·Q226·Q227·Q228·414/447 |
| 2026-06-10 | **72차** — §1-3·§3-6·§3-7·§8-1 BNK-47 월한도 가드·BNK-48 은행 일괄입금·Q226–Q227·401/432 |
| 2026-06-10 | **71차** — §1-3·§3-6·§3-7·§8-1 US-M03 청구 생성 기준·전월 미납 가드·V63·Q224–Q225·390/428 |
| 2026-06-10 | **70차** — §1-3·§3-6·§3-7·§4-8·§8-1 G2 templates 5종·납부확인서·노인학대예방 UI·G19·Q221–Q223·383/413 |
| 2026-06-10 | **69차** — §1-3·§3-6·§3-7·§8-1 US-L01 payment guard·notify dedupe·normalizeAmount·Q218–Q220·377/408 |
| 2026-06-10 | **68차** — §1-3·§3-6·§3-7·§4-8·§8-1 G2 email templates 3종·resolveDurationBand·Q204·Q216–Q217·371/402 |
| 2026-06-10 | **67차** — §1-3·§3-6·§3-7·§8-1 G9 V62 snapshot·FeeScheduleMatrix·NHIS 2026 seed·Q213–Q215·365/382 |
| 2026-06-10 | **66차** — §1-3·§3-6·§3-7·§8-1 G9 duration_band·V61·수가표 API·US-J02·Q210–Q212·363/373 |
| 2026-06-10 | **65차** — §1-3·§3-6·§3-7·§4-3·§4-8·§8-1 G21 confirm-lock UX·G2 SMTP email·V60 CMS FK·Q204·Q209·361/367 |
| 2026-06-10 | **64차** — §1-3·§3-6·§3-7·§4-6·§8-1 US-L03 CMS·FCMS stub·V59/V60·Q206–Q208·353/358 |
| 2026-06-10 | **63차** — §1-3·§3-6·§3-7·§4-3·§8-1 US-J03 email channel·US-L02 discharged names·Q204–Q205·342/350 |
| 2026-06-10 | **62차** — §1-3·§3-6·§3-7·§8-1 US-M02 dashboard counts·US-L02 overdue widget·BillingContextNav·V58·Q202–Q203·335/346 |
| 2026-06-09 | **61차** — §1-3·§3-6·§3-7 US-L02 overdue pagination·US-L01 payment names·G21 paired sync·V57·UXD-64·Q197–Q201·334/340 |
| 2026-06-09 | **60차** — §1-3·§3-6·§3-7 G2 notify·US-L01/L02·US-V02 cascade·BNK-26·Q109·Q174·Q194–Q196·329/323 |
| 2026-06-09 | **59차** — §1-3·§3-6·§3-7 change-password·UXD-63 visit import UI·V56·Q122·Q189·Q192·311/316 |
| 2026-06-09 | **58차** — §1-3·§3-6·§3-7 G21 visit import·SEC-D17 settings·fieldErrors·Q189–Q191·306/306·90/298 |
| 2026-06-10 | **57차** — §1-3·§3-7 UXD-62 GuardianDailySummary 식사·Q188·288/288·89/289 |
| 2026-06-10 | **56차** — §1-3·§3-6·§3-7·§8-1 BNK-22 US-J03-h NotificationHistoryPanel·Q152 Fixed·Q187·288/288·89/287 |
| 2026-06-10 | **55차** — §1-3·§3-6·§3-7 BNK-19 US-M02-b·UXD-59·Q161 Fixed·Q183–Q186·294/294·86/277 |
| 2026-06-09 | **54차** — §1-3·§3-6·§3-7 UXD-58 NHIS 대기 보류 UI·Region/NHIS 테스트·Q182·288/288·81/267 |
| 2026-06-09 | **53차** — §1-3·§3-6·§3-7·§8-1 Epic V `/visits` UI·G7 PENDING_REVIEW·V54·Q180 Fixed·Q181·269/269·80/259 |
| 2026-06-09 | **52차** — §1-3·§3-6·§3-7·§8-1 v1.2.1 G14·US-M01~M03·V51–V53·설정 RBAC·Q176–Q180·264/264·235/235 |
| 2026-06-09 | **51차** — §1-3·§3-7 UXD-55 GuardianBillingDetailModal·Q132·Q175·217/217 |
| 2026-06-08 | **50차** — §1-3·§3-6·§3-7·§8-1 BE v2 copay payment·overdue·V50·UXD-53/54·Q173·Q174·246/246·214/214 |
| 2026-06-08 | **49차** — §1-3·§3-6·§3-7 BE `c7941e9` pickup contact masking·pilotPageFlows T03·Q172·241/241·208/211 |
| 2026-06-08 | **48차** — §1-3·§3-7 ClientForm transport UI·UXD-52·Q166 Fixed·Q171·241/241·68/208 |
| 2026-06-08 | **47차** — §1-3·§3-6·§3-7·§5-2 transport pickup masking·UXD-51·FE-15·transport live E2E·Q169·Q170·241/241·65/199 |
| 2026-06-08 | **46차** — §1-3·§3-6·§3-7 transport pilot E2E·RBAC·UXD-50 forced-colors a11y·240/240·60/189·Q168 |
| 2026-06-08 | **45차** — §1-3·§3-6·§3-7 US-T01 Client transport profile API·UXD-49 HQ 지점명·pilotPageFlows transport·231/231·60/189·Q166·Q167 |
| 2026-06-08 | **44차** — §1-3·§3-6·§3-7 UXD-48 Recharts 복원·대시보드/출석/건강 연동·226/226·60/183·Q118·Q119·Q165 |
| 2026-06-08 | **43차** — §1-3·§3-6·§3-7 UXD-47 transport unconfirm UI·StaffPage a11y·PATCH contract·226/226·58/179·Q163·Q164 |
| 2026-06-08 | **42차** — §1-3·§3-6·§3-7 v3 §3-8 StaffPage·transport unconfirm·226/226·55/170·Q162·Q163 |
| 2026-06-08 | **41차** — §1-3·§3-6·§3-7·§8-1 v3 meals/programs API·V49·224/224·54/164·Q160 Fixed·Q161 |
| 2026-06-08 | **40차** — §1-3·§3-6·§3-7·§4-6·§8-1 v1.3-A transport API·V47·V48·식사·프로그램 shell·212/212·53/157·Q159·Q160 |
| 2026-06-08 | **39차** — §1-3·§3-6·§3-7·§4-3 PAID 수납 알림·UNMATCHED 후보 검색·배차 shell·202/202·50/150·Q159 |
| 2026-06-08 | **38차** — §1-3·§3-6·§3-7 US-G06 DISCREPANCY compare·AlimtalkFallbackText·198/198·46/143·Q135·Q158 |
| 2026-06-08 | **37차** — §1-3·§3-6·§3-7 UXD-41 IncidentRecordForm·AlimtalkTemplateVariables·191/191·45/137·Q157 |
| 2026-06-08 | **36차** — §1-3·§3-6·§3-7 Q154 Fixed·UXD-40·J03 service E2E·185/185·44/130·Q155·Q156 |
| 2026-06-08 | **35차** — §1-3·§3-6·§3-7 UXD-39 건강·NHIS UI·J03 vitals DAILY_CARE·179/179·40/115·Q154 |
| 2026-06-07 | **34차** — §1-3·§8-1 US-E01~E05·V46·178/178·36/110·Q153 |
| 2026-06-07 | **27차** — §8-1 V40 지점명 UK·스모크 Q146 |
| 2026-06-08 | **29차** — §1-3·§3-6·§3-7·§4-3·§4-5·§8-1 Must FE·Solapi·V44·152/152·40/40·Q148 |
| 2026-06-08 | **28차** — §1-3·§3-6·§3-7·§8-1 V43 Fixed·J03 dispatch·147/147·프론트 baseline·Q144·Q147 |
| 2026-06-07 | **25차** — §1-3·§3-6·§3-7·§8-1 COD 36 V42·GuardianListCard WIP·테스트 253/209·758 modules·Q142–Q143 |
| 2026-06-07 | **24차** — §1-3·§3-7 COD 35차 FE-17 LogoutButton·PublicAuthLayout·GuardianInvitationAcceptForm·테스트 40/199·756 modules·Q141 |
| 2026-06-07 | **23차** — §1-3·§3-7 COD 34차 FE-16 ds-*·GuardianInvitationAcceptPage·layout tests·테스트 35/187·Q139–Q140 |
| 2026-06-07 | **22차** — §1-3·§3-6·§3-7·§5-2 TSR 48·49차 PilotChecklistJwtE2eTest·B08·FE-15 manualChunks·테스트 34/249·34/186·393.53 kB·Q137–Q138 |
| 2026-06-07 | **21차** — §1-3 UXD 22차 PaymentRecordModal·ReconciliationSummaryBar·MonthInput·테스트 33/185·752 modules·§3-7·Q134–Q136 |
| 2026-06-07 | **20차** — §1-3 UXD 20–21차 청구·NHIS·보호자 UI·테스트 30/181·33/243·749 modules·§3-7 |
| 2026-06-07 | **19차** — §1-3 TSR 39차 LoginHistoryPanel·PasswordResetRequestModal·PlatformOrgDetailModal·테스트 24/169·743 modules·§3-7 |
| 2026-06-07 | **18차** — §1-3·§8-1 V41·UXD 15–16차 Recharts·BatchProgressSteps·테스트 20/161·33/240·§3-7 |
| 2026-06-07 | **17차** — §1-3 UXD 14차 FeeRateHistoryPanel(Q117)·COD 21차 `pilotPageFlows`·프론트 13/144·§3-7 |
| 2026-06-07 | **16차** — §1-3 UXD 13차 Switch(Q116)·COD 20차 7역할 E2E·테스트 31/213·프론트 10/130·§3-7 |
| 2026-06-07 | **15차** — §1-3 UXD 12차(Q115)·SEC-008 Vite 6·테스트 30/190·프론트 7/32·§3-7 pilotChecklist·npm audit |
| 2026-06-07 | **13차** — §1-3 ClientFormPage UXD 10차(primaryGuardian·동의 정합·Q113 client_user/사진 UI-only) |
| 2026-06-06 | §1-3·§8-1 Flyway V38–V39·`/branches`·`/attendance/stats` 라우트·테스트 25/86 (FAQ Q104·Q106) |
| 2026-06-08 | §1-3 App.jsx 2차 라우트(20페이지·22 라우트)·BranchesPage 미등록·UI 골격 (FAQ Q104–Q105) |
| 2026-06-07 | §1-3 프론트 응답·본문 불일치 Q94–Q99 참조 추가 |
| 2026-06-07 | §3-7 프론트 Vitest·§1-3 Q87–Q91 갭 참조 |
| 2026-06-07 | §1-3 대시보드·결석 API-only·Q83 경로 갭·Q85–Q86 참조 갱신 |
| 2026-06-06 | §1-3 Must 13페이지·SideNav·API 경로 불일치(Q83) 구현 상태 갱신 |
| 2026-06-06 | §3-5 `VITE_API_BASE_URL`·프론트 JWT API 연동·프록시 권장안 갱신 |
| 2026-06-06 | Flyway V36–V37, Spring Boot 3.5.3, 인증 rate limit·ProductionSecretValidator·프론트 디자인 시스템 |
| 2026-06-06 | Flyway V35, 수가표·QR actor backstop 트리거·스모크 테스트 항목 |
| 2026-06-06 | Flyway V34, 퇴소 시각 CHECK·지점 purge·NHIS 수동 매칭 스모크 테스트 |
| 2026-06-06 | Flyway V32–V33, actor backstop·퇴소 purge·청구 상태 필터 스모크 테스트 |
| 2026-06-06 | Flyway V29–V31, Tenant 이메일 UK·청구 상태 DB·테스트 21클래스 반영 |
| 2026-06-06 | Flyway V21–V28, 조회 성능 인덱스·테스트 19클래스 반영 |
| 2026-06-06 | Flyway V13–V20, 백업·사진 환경변수, 내장 백업 스케줄러 반영 |
| 2026-06-05 | 초안 작성 — 로컬·프로덕션·Docker 권장 구성 |

---

*이 문서는 tech_writer 에이전트가 관리합니다. Dockerfile·CI 추가 시 본 문서와 동기화하세요.*
