<!-- doc:owner=TWR doc:audience=PLN,COD updated=2026-06-15T14:00:00+09:00 -->
# ogada 배포 가이드 (ops/DEPLOYMENT_GUIDE.md)

> **작성**: tech_writer 에이전트  
> **최초 작성일**: 2026-06-05  
> **최종 갱신**: 2026-06-15 (164차 — v1.3-B 배차 FE wire·L03_M01 V123 · BE `9bd1660`/FE `edfba7f` · Vitest 1274/1274 · `mvn test` 1131/1131 PASS)  
> **상태**: 초안 (Draft)  
> **대상 독자**: **DevOps·인프라 담당**, **ogada 플랫폼 운영자** (`platform_admin` 협업), **고객 센터 IT** (`sysadmin` 협업)  
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
| 데이터베이스 | PostgreSQL | `pgcrypto` 확장, Flyway V1–V123 |
| 인증 | JWT (RS256) + RBAC | access 30분, refresh 7일 |
| 멀티테넌트 | Organization → Branch | `organization_id` 강제 격리 |

> **구현 상태 (2026-06-15 develop HEAD `9bd1660` / frontend `edfba7f` 기준)**:
> - **백엔드**: Must API + **V41–V123**. **L03_M01** nursing service records (`9bd1660`) · **v1.3-B** `POST /transport/runs/suggest`·`GET/PUT /transport/settings` (`db94a65`) · **G21** batch-confirm date guard (`230659a`) · **L03** V115–V119 · **injectable `Clock` future-date guard** (`090b2d7`) · **G-NURSING-PRESSURE-ULCER** V114 · **G17b** V112/V113 · **G2/7-5** · **J03 `NotificationQuietHoursPolicy`**.
> - **프론트엔드**: **77 라우트**. **`TransportSuggestPanel`**·**`BranchTransportSettingsPanel`** (`2ffe59f`) · **`NursingOralCareCheckPage`** · **`NursingEmergencyRecordPage`** · **`NursingContextNav`** 8탭 · Vitest **1274/1274 PASS** (`edfba7f` SideNav deepen).
> - **merge gate**: develop→test **552 pending** — BE·FE **FULLY UNBLOCKED**.
> - **마이그레이션**: V43 … **V114** pressure ulcer · **V115–V116** vital·weight · **V117** nursing integrity · **V118** oral care · **V119** emergency records · **V120** transport v1.3-B · **V121** nursing V118/V119 integrity · **V122** transport integrity · **V123** nursing service records. Flyway 자동 실행. **V118–V123** — additive·기존 데이터 영향 없음.
> - **프로덕션 주의**: Solapi·FCMS·SMTP·**PG(stub)** 미사용 시 **`NOTIFICATION_PROVIDER=stub`** · **`NOTIFICATION_EMAIL_PROVIDER=stub`** · **`FCMS_PROVIDER=stub`** 기본값 유지. 배차 지도는 **`KAKAO_REST_KEY`** (§4-7). v1.3-B suggest는 **`ogada.transport.suggest-daily-limit-per-branch`**(기본 10). §4-3·§4-6·§4-6-1·§4-8 참고.

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
| Spring Boot API | `8080` | `/api/v1/*`, `/actuator/health`, `/.well-known/jwks.json` |
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
| API 헬스 | `curl http://localhost:8080/api/v1/health` | `{"status":"UP","service":"ogada-backend",...}` |
| Actuator | `curl http://localhost:8080/actuator/health` | `{"status":"UP"}` |
| JWKS | `curl http://localhost:8080/.well-known/jwks.json` | RSA 공개키 JWK Set |
| Flyway | 애플리케이션 로그 | `V1`~`V42` 마이그레이션 성공 |

Flyway는 `spring.flyway.enabled=true`, `classpath:db/migration` 경로의 SQL을 **애플리케이션 기동 시 자동 적용**합니다. `spring.jpa.hibernate.ddl-auto=validate`이므로 스키마는 Flyway만 변경합니다.

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
| **US-L03 CMS (G2)** | **`CmsServiceTest`** · **`CmsCopayLifecycleE2eTest`** — enrollment→debit→PAID·`payment_method=CMS` · **cancel enrollment**·**duplicate active guard**·**cancelled history list** (`a34d0eb`·`72aff00`·`4a622ab`, Q299) · **FAILED response(422 아님)** (`838a7f6`, Q256) · **`CmsPilotServiceFlowE2eTest`** retry·cancel lifecycle (BNK-104) · **`CmsPage.test`** · **`CmsEnrollmentTable.test`** · **`StubFcmsClientTest`** · **`MustApiEndpointRoutingTest$CmsRouting`** · **`RoleBasedControllerAccessTest$CmsAccess`** (Q208) |
| **G21 batch-confirm (BNK-197~198·213, Q330)** | **`VisitServiceTest`** confirm-readiness·ack gates·**date range required** (`230659a`)·batch confirm · **`VisitControllerRoutingTest`** · **`RoleBasedControllerAccessTest$VisitAccess`** · **`MustApiEndpointRoutingTest$VisitRouting`** · **`VisitBatchConfirmPanel.test`** · **`VisitsPage.test`** · **`pilotPageFlows`** G21 E2E |
| **v1.3-B transport suggest (BNK-212~214, Q347)** | **`TransportControllerRoutingTest`** · **`RoleBasedControllerAccessTest$TransportAccess.suggestRuns*`** · **`MustApiEndpointRoutingTest$TransportRouting`** · FE **`TransportSuggestPanel.test`**·**`BranchTransportSettingsPanel.test`**·**`transportSuggestServices.test`** · **V120**·**V122** |
| **L03_M01 nursing service provision (BNK-215, Q348)** | **`NursingServiceRecordServiceTest`** · **`NursingServiceRecordPilotServiceFlowE2eTest`** · **`MustApiEndpointRoutingTest$NursingServiceRecordRouting`** · **`RoleBasedControllerAccessTest$NursingServiceRecordAccess`** · **V123** · **P2**: FE wire |
| **G-NURSING-PRESSURE-ULCER (BNK-203~204, Q336~Q339, US-O03)** | **`PressureUlcerServiceTest`** · **`PressureUlcerPilotServiceFlowE2eTest`** 4-step (`24a1c5c`) · **`MustApiEndpointRoutingTest$PressureUlcerRouting`** · **`RoleBasedControllerAccessTest$PressureUlcerAccess`** · FE **`PressureUlcerPage.test`**·**`pressureUlcerServices.test`**·**`PressureUlcerCohortReportPanel.test`** · **`pressureUlcerLiveApi.e2e.test.js`** (`LIVE_E2E=1`) · **`pilotPageFlows`** US-O03 · V114 |
| **L03_M11 integrated vital check (BNK-207, Q340~Q342)** | **`NursingVitalCheckServiceTest`** · **`NursingVitalCheckPilotServiceFlowE2eTest`** · **`MustApiEndpointRoutingTest$NursingVitalCheckRouting`** · **`RoleBasedControllerAccessTest$NursingVitalCheckAccess`** · FE **`NursingVitalCheckPage.test`**·**`nursingVitalCheckServices.test`**·**`NursingContextNav.test`** · **`nursingVitalCheckLiveApi.e2e.test.js`** (`LIVE_E2E=1`) · V115 |
| **L03_M14 weight management (BNK-207~209, Q343~Q344)** | **`NursingWeightRecordServiceTest`** · **`NursingWeightRecordPilotServiceFlowE2eTest`** · **`MustApiEndpointRoutingTest$NursingWeightRecordRouting`** · **`RoleBasedControllerAccessTest$NursingWeightRecordAccess`** · FE **`NursingWeightRecordPage.test`**·**`NursingWeightRecordForm.test`** · **future measure-date guard** · V116 |
| **L03_M13 oral care check (BNK-209, Q345)** | **`NursingOralCareCheckServiceTest`** · **`NursingOralCareCheckPilotServiceFlowE2eTest`** · **`MustApiEndpointRoutingTest$NursingOralCareCheckRouting`** · **`RoleBasedControllerAccessTest$NursingOralCareCheckAccess`** · FE **`NursingOralCareCheckPage.test`**·**`NursingOralCareCheckForm.test`**·**`nursingOralCareCheckLiveApi.e2e.test.js`** · **future check-date guard** · V118 |
| **L03_M04 emergency record (BNK-211, Q346)** | **`NursingEmergencyRecordServiceTest`** · **`NursingEmergencyRecordPilotServiceFlowE2eTest`** · **`MustApiEndpointRoutingTest$NursingEmergencyRecordRouting`** · **`RoleBasedControllerAccessTest$NursingEmergencyRecordAccess`** · FE **`NursingEmergencyRecordPage.test`**·**`NursingEmergencyRecordForm.test`**·**`nursingEmergencyRecordLiveApi.e2e.test.js`** · **injectable `Clock` future-date guard** · V119 |
| **G17b cognitive activity skip reason (BNK-198~203, Q333~Q335)** | **`ProgramServiceTest`** skipReason·ABSENT satisfaction guard (`3bd6a43`) · **`ProgramControllerRoutingTest`** · **`ProgramCompliancePilotServiceFlowE2eTest`** · **`ProgramParticipationForm.test`** · **`ProgramsPage.test`** · **`FunctionalRecoveryPage.test`** · **`pilotPageFlows`** G17b program+functional recovery E2E · V112–V113 |
| **G2/7-5 easy payment (BNK-189, Q326~Q328)** | **`EasyPayServiceTest`**(provider normalize) · **`EasyPayPilotServiceFlowE2eTest`** — CARD/KAKAO·retry·failed PG·**prior-month guard** · **`RoleBasedControllerAccessTest$EasyPayAccess`** · **`MustApiEndpointRoutingTest$EasyPayRouting`** · **`EasyPayPage.test`** · **`EasyPayPanel.test`** · **`easyPay.test`** · **`billingGuardianPlatformServices.test`** · **`pilotPageFlows`** 7-5 E2E · V108–V111 |
| **J03 primary guardian dispatch** | **`NotificationServiceTest`** · **`J03PrimaryGuardianDispatchE2eTest`** — primary 우선·secondary fallback·1명 발송 (`555a19f`·`d86405c`, Q272) |
| **Dashboard billing/NHIS snapshot (QA-B49)** | **`DashboardServiceTest`** — **`monthlyCapWarningCount`** on branch · HQ **`nhisUnmatchedCount`·`overdueCount`·`monthlyCapWarningCount`** aggregate (`15b3c7e`, Q282) |
| **G17/G32/G38/G39 dashboard compliance snapshot** | **`DashboardServiceTest`** — G17/G32/G38/G39 **count·met 필드** on **`GET /dashboard/branch`**·**`/dashboard/hq`** (`7ba18c1`·`70d76a4`, Q280) |
| **BNK-112 G38/G39 pilot E2E** | **`CarePlanProvisionCompliancePilotServiceFlowE2eTest`** — G38 branch-scoped compliance + G39 indicator-44 create/list/compliance/duplicate guard · **`PilotChecklistJwtE2eTest`** (`a9f8bda`) |
| **G39 provision result evaluation (BNK-107)** | **`ProvisionResultEvaluationServiceTest`** · **`MustApiEndpointRoutingTest$ProvisionResultRouting`** · **`RoleBasedControllerAccessTest$ProvisionResultAccess`** (`f082933`, V80/V81, Q276) |
| **G38 care-plan notification compliance (BNK-106)** | **`CarePlanNotificationComplianceServiceTest`** — branch-scoped query · **`MustApiEndpointRoutingTest`** · **`RoleBasedControllerAccessTest`** (`5fd35a6`·`03211e6`, Q277) |
| **G21 NHIS import file validation** | **`VisitServiceTest`** — reject text/plain · allow octet-stream · **allow ms-excel** · **parameterized Content-Type strip** · **uppercase/mixed casing** (`Application/VND.MS-EXCEL; charset=UTF-8`, `1817c36`) · empty file (`3c7b247`·`18e2b4c`·`e21c12f`·`3f444a1`, Q278·Q297) |
| **G37 grade history attachments (BNK-105)** | **`LtcGradeHistoryAttachmentServiceTest`** · **`LtcGradeHistoryAttachmentStorageServiceTest`** · **`LtcGradeHistoryServiceTest`** attachmentCount · **`MustApiEndpointRoutingTest`** attachment routes · **`RoleBasedControllerAccessTest$ClientAccess`** (`0325d95`, V78/V79, Q274) |
| **G21 visit enum normalize** | **`VisitServiceTest`** — `scheduleKind`·`checkInMethod` trim+uppercase · **`VisitControllerRoutingTest`** (`225b104`·`e8de0eb`, Q275) |
| **BNK-103 program compliance pilot** | **`ProgramCompliancePilotServiceFlowE2eTest`** — G17 indicator27·G32 evaluationConductedMet · **`PilotChecklistJwtE2eTest`** G33 start-balance·visit routing |
| **G2 copayAmount null guard** | **`BillingServiceTest.recordCopayPaymentShouldRejectMissingCopayAmountOnClaim`** · **`updateClaimStatusShouldRejectPaidWhenCopayAmountMissing`** (`1af5b1f`·`923e610`, Q257) |
| **G26 medical expense exclusion** | **`BillingServiceTest.getMedicalExpenseDeductionShouldExcludeCmsAndEasyPayPayments`** — `CMS`·`EASY_PAY` 제외 (`970f547`, Q254) |
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
| **G15 Form22 service log (FE)** | **`TransportServiceLogPanel.test`** · **`transportServiceLog.test`** · **`transportTimeCompliance.test`** (`7389884`·`eef07e5`, Q236) |
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
| **G41/G41b staff training logs (8-7, Q321·Q325, BNK-184~188)** | **`StaffTrainingLogServiceTest`** · **`StaffTrainingLogPilotServiceFlowE2eTest`** · **`MustApiEndpointRoutingTest$StaffTrainingLogRouting`** · **`StaffTrainingLogPage.test`** · **`staffTrainingLogLiveApi.e2e.test.js`** (`LIVE_E2E=1`, BNK-186) · V104–V107 |
| **US-R03 staff lifecycle (BNK-129)** | **`UserServiceTest`** — lifecycle status·checklist merge·offboarding guard·termination date ≥ hire date · **`StaffLifecyclePilotServiceFlowE2eTest`** · **`StaffPage.test`** — lifecycle **필터** · **`StaffLifecyclePanel.test`** — **진행률·날짜 정규화** (`37dc785`·`bb4c1af`, V86–V87, Q290·Q293) |
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

```bash
# 루트에서 일괄 실행 (권장)
./scripts/run-live-e2e.sh

# 개별 harness
./scripts/run-live-e2e.sh src/e2e/transportLiveApi.e2e.test.js
./scripts/run-live-e2e.sh src/e2e/programComplianceLiveApi.e2e.test.js
./scripts/run-live-e2e.sh src/e2e/leadCaregiverWorkLogLiveApi.e2e.test.js
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

스테이징 스모크: JWT 로그인(빈 이메일·비밀번호 시 **필드 오류** 표시 확인, Q190) → **`/dashboard`**·**`/dashboard/hq`** — NHIS 대기·미매칭 집계(Q183) · **Recharts**(Q118) → **`/clients`** — 보호자·지역·나이 열(Q191) → **`sysadmin` `/settings`** — 백업·감사·로그인 이력 탭(Q121) · **비밀번호 변경·재설정**(Q122·Q126) → SideNav **운영 → 직원 관리**(`/staff`) — 등록 모달 **fieldErrors**(Q190) → SideNav **기록 → 건강 기록** → 바이탈/투약/**낙상·특이사항** 저장 → **`/health/:clientId`** — **HealthTrendChart** + 표(Q119) → **`/attendance/stats`** — 월별 막대 차트(Q118) → SideNav **청구 → 청구대장**(`/billing/reports/charges`) — **StatCard** 요약·표·인쇄(Q179) → **`/billing/imports/nhis`** — **year-coverage** 배너·25칸 미완비 업로드 차단(Q260) → `/billing/imports/nhis/:batchId` **StatCard·`NhisPendingReviewGuide`**(Q182) · **`UNMATCHED` 후보 검색**(Q135) → **`DISCREPANCY` 「비교」 Modal** → Swagger **`PATCH /clients/{id}`** — `usesTransport`·픽업 주소(Q166) → SideNav **이동 → 배차·이동경로** — roster·confirm·unconfirm(Q159·Q163) · **G15 계약서 저장**(Q230·Q231) · **별지 제18호 안내**(Q237) · 확정 루트 **`TransportServiceLogPanel`** 인쇄·시간 준수(Q236) → SideNav **기록 → 식사·프로그램** — **`MealMenuForm`·`ProgramScheduleForm`**(Q161) → **`HOME_VISIT` 지점 `/visits`** — **`VisitNhisImportPanel`** xlsx 업로드(Q189) · **페어 체크인 동기화**(Q238) → `/guardians` **보호자 초대** → SideNav **청구 → CMS 자동이체**(`/billing/cms`) — 등록·**CONFIRMED** 청구 CMS 출금 stub(Q207·Q208) → 청구 **`PAID`** 후 **알림 이력**(Q152·Q187) → **`guardian` `/guardian`** **「명세·청구」 더 보기**(Q192) · **「일일 기록」** 식사 행(Q188) — FAQ Q154·Q107·Q112·Q165.

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
>
> **기동 검증 (`18ee9b6`·`98e40a3`)**: `NOTIFICATION_PROVIDER=solapi` 선택 시 **`SOLAPI_API_KEY`·`SOLAPI_API_SECRET`·`SOLAPI_SENDER_ID`·`KAKAO_PF_ID` 누락** 또는 **`KAKAO_TPL_*` 값이 내부 placeholder**(내부 코드명과 동일)이면 **기동 실패**합니다. live 전환 전 Solapi 콘솔 **승인 templateId**를 각 `KAKAO_TPL_*`에 매핑하세요 (FAQ Q266). dev/staging은 **`NOTIFICATION_PROVIDER=stub`** 유지를 권장합니다.

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
8. UI **`/billing/cms`** **등록 관리** — **해지** Modal → **해지완료** Badge · **재등록** 시 **행 UPDATE**·`created_at` 보존 (Q207·Q299)

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

### 4-7. 배차 지도·Geocoding (v1.3-A, 선택 — FAQ Q159)

| 변수 | 설명 | 기본값 |
|------|------|--------|
| `KAKAO_REST_KEY` | Kakao Local REST API 키 — `POST /api/v1/transport/geocode` proxy | (빈 값 — geocode **비활성**) |

- `application.yml`: `ogada.transport.kakao-rest-key: ${KAKAO_REST_KEY:}`
- **미설정 시**: transport roster·runs CRUD는 동작하나 **지도 마커·좌표 변환 불가**.
- **보안**: REST 키는 **서버 환경변수만** — 프론트에 노출하지 않습니다 (Kakao REST proxy 패턴).
- **스테이징 스모크**: `hq_admin` JWT → `POST /transport/geocode` `{ "address": "서울특별시 …" }` → `lat`/`lng` 응답 확인.

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
   - **BNK-48 bank deposit**: `POST /billing/imports/bank-deposits` — 샘플 xlsx + **`branchId`** 업로드 → `APPLIED`/`UNMATCHED` 행 확인 (Q227)
   - **BNK-49 FE bank UI**: `/billing/payments` — **`BankDepositImportPanel`** — UI에서 **`branchId` 전송 Fixed** · `appliedCount` 요약 확인 (Q227·Q228, `f4bb171`)
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
| `GET /api/v1/health` | 애플리케이션 UP/DOWN | ✅ 권장 |
| `GET /actuator/health` | Spring Actuator (DB 포함 가능) | ✅ |
| `GET /.well-known/jwks.json` | JWT 키 배포 확인 | 진단용 |

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
