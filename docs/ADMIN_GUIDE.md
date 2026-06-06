# ogada 관리자 가이드 (ADMIN_GUIDE.md)

> **작성**: tech_writer 에이전트  
> **최초 작성일**: 2026-06-05  
> **상태**: 초안 (Draft)  
> **대상 독자**: **ogada 플랫폼 운영자** (`platform_admin`), **고객 센터 IT·시스템 관리자** (`sysadmin`)  
> **기준 문서**: `docs/REQUIREMENTS.md`, `docs/API_SPEC.md`, `docs/FLOWCHART.md`, `docs/DATA_RETENTION_POLICY.md`  
> **기술 스택**: Java Spring Boot 3.x + React (Vite SPA) + PostgreSQL

---

## 1. 이 가이드에 대하여

### 1-1. 목적

ogada는 전국 주간보호센터·요양기관을 위한 **B2B SaaS 멀티테넌트** 운영 관리 시스템입니다.  
이 문서는 **시스템·플랫폼 관리자**가 신규 고객 온보딩, 테넌트 기술 설정, 백업·감사, 보안 키 관리, 장애 대응을 수행할 때 필요한 절차와 권한 경계를 설명합니다.

### 1-2. 문서 범위

| 포함 | 제외 |
|------|------|
| `platform_admin` — 신규 Tenant 등록·첫 `hq_admin` 발급 | 현장 일상 업무 (→ `USER_MANUAL.md`) |
| `sysadmin` — 기술 설정·백업·감사 로그 | 인프라 배포·CI/CD 상세 (→ `DEPLOYMENT_GUIDE.md`) |
| 역할·테넌트 격리·PII 암호화 정책 | 식사·프로그램·알림톡 (v1 이후) |
| 계정·권한 관리 개요 (`hq_admin` 협업) | 공단 포털 직접 전송·CMS 결제 (후속) |

### 1-3. 관리자 역할 구분

ogada에는 **두 종류의「시스템 관리자」**가 있습니다. 혼동을 피하기 위해 역할·데이터 범위를 먼저 구분합니다.

| 역할 | 코드 | 소속 | 홈 화면 | 데이터 범위 | 주요 책임 |
|------|------|------|---------|------------|----------|
| **플랫폼 관리자** | `platform_admin` | ogada 내부 | `/platform` | 전국 Tenant **메타데이터** | 신규 고객 센터 등록, 첫 `hq_admin` 발급, 요금제·활성 상태 |
| **시스템 관리자** | `sysadmin` | 고객 센터(Tenant) | `/settings` | **자기 Tenant** 기술 영역 | 백업·감사 로그·기술 설정, 보안 모니터링 |
| **통합 관리자** | `hq_admin` | 고객 센터(Tenant) | `/dashboard/hq` | 자기 Tenant **운영 전반** | 지점·직원·이용자·청구 (본 가이드 §6 참고) |

**할 수 있는 일 / 없는 일 (요약)**

| 행동 | `platform_admin` | `sysadmin` | `hq_admin` |
|------|:----------------:|:----------:|:----------:|
| 새 센터 법인(Tenant) 등록 | ✅ | ❌ | ❌ |
| 전국 가입 고객사 목록 조회 | ✅ | ❌ | ❌ |
| 자기 회사 백업·기술 설정 | ❌ | ✅ | ❌ |
| 자기 회사 이용자·출석 CRUD | ❌ | ❌ | ✅ (지점 스코프) |
| 다른 센터 이용자 데이터 조회 | ❌ | ❌ | ❌ |

> **비유**: `platform_admin`은 통신사 매장의 **회선 개통** 담당, `sysadmin`은 고객사 IT의 **내부 시스템·백업** 담당, `hq_admin`은 센터 **운영 총괄** 담당입니다. (REQUIREMENTS §1-3)

### 1-4. 구현 상태 안내 (2026-06-06 기준, Flyway V33)

| 영역 | 상태 | 비고 |
|------|------|------|
| 플랫폼 API | **구현됨** | `PlatformOrganizationController` — Tenant CRUD, **법인명 검색**(`?query=`), 첫 `hq_admin` 발급 |
| 조직·지점·계정 API | **구현됨** | Organization, Branch, User API + RBAC |
| 인증 API | **구현됨** | 로그인·갱신·로그아웃·`active-branch`·비밀번호 재설정 |
| 청구 API | **구현됨** | `BillingController` — 청구 생성·상태 변경·**목록 상태 필터**(`?status=`) |
| PII 암호화 | **구현됨** | `PiiCryptoService` — 주민번호·연락처·주소 AES-GCM, **복호화 열람 API** + `audit_log` |
| Actor 감사 | **구현됨** | `DbSessionContext` + V32–V33 트리거 — 출석·건강·청구·NHIS import `*_by` 컬럼 자동 기록 |
| 시스템 설정 API | **구현됨** | `SettingsController` — `/settings/system`, `/audit-logs`, `/backups` |
| 백업 스케줄러 | **MVP 구현** | `BackupRunService` + `FileTenantBackupExecutor`(manifest). 프로덕션 `pg_dump` 교체 예정 |
| `/settings` 프론트 | **골격만** | `/settings` 홈 라우팅만 존재, 설정·감사·백업 UI 미구현 |

> 화면·버튼 이름은 UI 구현 완료 시 갱신합니다. 본 문서는 **구현된 API**와 **MVP 목표 동작**을 함께 기술합니다.

---

## 2. 아키텍처 개요

### 2-1. 멀티테넌트 계층

```
Organization (Tenant)     ← platform_admin이 생성
  └── Branch (지점)       ← hq_admin이 등록
        ├── users         ← 직원 계정 (역할·지점 배정)
        ├── clients       ← 이용자 (PII 암호화)
        ├── attendance    ← 출석
        ├── health_records
        └── billing_claims
```

- **테넌트 격리**: 모든 운영 데이터는 `organization_id`로 분리됩니다. API·DB 쿼리 모두 JWT의 `organization_id`를 강제합니다.
- **지점 격리**: 이용자·출석·건강 등은 추가로 `branch_id`로 소속 지점이 식별됩니다.
- **JWT 클레임**: `role`, `organization_id`, `branch_ids[]`, `active_branch_id` (API_SPEC §0-2)

### 2-2. 기술 스택

| 계층 | 기술 | 관리자 관점 |
|------|------|------------|
| 백엔드 | Spring Boot 3.x REST (`/api/v1`) | 환경변수·헬스체크·로그 |
| 프론트 | React Vite SPA | 정적 빌드 배포, HTTPS 필수 |
| DB | PostgreSQL + Flyway 마이그레이션 | 백업·복구 대상 |
| 인증 | JWT + RBAC | 30분 비활성 만료, 역할별 `@PreAuthorize` |
| PII | AES-GCM (`PII_ENCRYPTION_KEY`) | 키 로테이션·시크릿 관리 |

### 2-3. 환경변수 (관리자 필수 확인)

백엔드 `application.yml` 기준. **비밀값은 코드·Git에 저장하지 않습니다.**

| 변수 | 용도 | 미설정 시 |
|------|------|----------|
| `DB_URL` | PostgreSQL JDBC URL | 기본 `localhost:5432/ogada` |
| `DB_USERNAME` / `DB_PASSWORD` | DB 인증 | 개발 기본값 (운영 시 반드시 변경) |
| `PII_ENCRYPTION_KEY` | 주민번호·연락처·주소 암호화 | **이용자 등록·복호화 실패** |
| `QR_TOKEN_SECRET` | 지점 QR 토큰 서명 | QR 체크인 불가 |
| `JWT_PRIVATE_KEY` / `JWT_PUBLIC_KEY` | JWT RSA PEM | 미설정 시 ephemeral 키(재시작 시 무효) |
| `BACKUP_STORAGE_DIR` | Tenant 백업 manifest 저장 경로 | `./data/backups` |
| `BACKUP_SCHEDULER_ENABLED` | 일 1회 백업 스케줄러 | `true` |
| `SERVER_PORT` | API 포트 | 8080 |

```bash
# 운영 예시 (값은 환경에 맞게 설정)
export PII_ENCRYPTION_KEY="<Base64 인코딩 32바이트 키>"
export QR_TOKEN_SECRET="<충분히 긴 랜덤 시크릿>"
export DB_URL="jdbc:postgresql://db.internal:5432/ogada"
```

> 키 생성·로테이션 절차는 §8을 참고하세요.

---

## 3. 플랫폼 관리자 (`platform_admin`)

ogada 영업·운영 직원이 **신규 고객 센터를 개통**할 때 따르는 절차입니다.

### 3-1. 접속·권한

1. ogada 관리 URL에 `platform_admin` 계정으로 로그인합니다.
2. 로그인 성공 시 **`/platform`** 플랫폼 관리 화면으로 이동합니다.
3. 이 역할은 **운영 데이터(이용자·출석 등)에 접근할 수 없습니다.** Tenant 메타데이터와 초기 계정 발급만 가능합니다.

### 3-2. 신규 고객 온보딩 절차

**시나리오**: 「행복주간보호센터」가 ogada 구매 → 월요일부터 사용.

```
[ogada 직원]                    [고객 센터]
  ① Tenant 등록        →
  ② hq_admin 발급       →  ③ 센터장 로그인
                            ④ 지점·직원 등록
                            ⑤ 운영 시작
```

| 순서 | 화면·API | 작업 | 결과 |
|------|----------|------|------|
| 1 | `/platform` → 고객 등록 | 법인명·사업자번호·요금제 입력 | Organization 생성 |
| 2 | 고객 상세 → 관리자 발급 | 센터장 이메일·이름·초기 비밀번호 | `hq_admin` 계정 1개 |
| 3 | — (고객 전달) | 로그인 정보를 센터장에게 **안전한 채널**로 전달 | 고객 자체 운영 시작 |
| 4 | — | 센터장이 지점·직원·이용자 등록 | 파일럿·운영 개시 |

#### API 호출 예시

**① 신규 Tenant 등록** — `POST /api/v1/platform/organizations`

```json
{
  "name": "행복주간보호센터",
  "businessNo": "123-45-67890",
  "plan": "standard"
}
```

**② 첫 `hq_admin` 발급** — `POST /api/v1/platform/organizations/{orgId}/admins`

```json
{
  "email": "kim@happy-care.com",
  "displayName": "김센터장",
  "password": "<초기 비밀번호 — 전달 후 변경 권고>"
}
```

> 구현 확인: `PlatformOrganizationController`는 `@PreAuthorize("hasRole('PLATFORM_ADMIN')")`로 보호됩니다. `platform_admin` 역할은 Tenant API로 **생성 불가**합니다 (`UserService` 정책).

### 3-3. 기존 고객 관리

| 작업 | API | 설명 |
|------|-----|------|
| 전국 고객 목록 | `GET /platform/organizations` | 가입 법인 목록·요금제·활성 상태 |
| 고객 검색 | `GET /platform/organizations?query=행복` | **법인명·사업자번호** 부분 일치 검색 (V27·V29 trigram 인덱스) |
| 고객 상세 | `GET /platform/organizations/{orgId}` | Tenant 메타데이터 조회 |
| 요금제·상태 변경 | `PATCH /platform/organizations/{orgId}` | `plan`, `active`(정지/재개) |

**Tenant 정지 (`active: false`) 시**

- 해당 Organization 소속 **전 계정 로그인 차단** (구현 시 `is_active` 검증).
- 운영 데이터는 즉시 삭제하지 않습니다. 해지·파기 절차는 `DATA_RETENTION_POLICY.md` §4-2를 따릅니다.

### 3-4. 플랫폼 관리자 운영 체크리스트

- [ ] 신규 등록 시 **사업자등록번호 중복** 확인 (API가 `409`/`BUSINESS_RULE` 반환)
- [ ] 기존 고객 조회 시 `?query=`로 **법인명·사업자번호** 동시 검색 활용 (V29)
- [ ] 초기 비밀번호는 **1회용**으로 안내, 센터장에게 첫 로그인 후 변경 요청
- [ ] 로그인 정보는 이메일·전화 등 **평문 채팅에 남기지 않음**
- [ ] 계약 해지 시 Tenant 정지 → 90일 유예 → 파기 절차 ops 팀과 연계
- [ ] 플랫폼 작업은 `audit_logs`에 기록 (Tenant 해지·파기 이벤트 포함)

---

## 4. 시스템 관리자 (`sysadmin`)

고객 센터 IT 담당자가 **자기 법인(Tenant)의 기술·보안·백업**을 관리할 때 사용합니다.

### 4-1. 접속·권한

1. 센터에서 발급한 `sysadmin` 계정으로 로그인합니다.
2. 로그인 성공 시 **`/settings`** 시스템 설정 화면으로 이동합니다.
3. **운영 데이터 CRUD 불가** — 이용자·출석·청구 화면에는 접근하지 않습니다.
4. **다른 Tenant 데이터 조회·설정 불가** — JWT `organization_id`로 자동 격리됩니다.

### 4-2. `/settings` 화면 구성

| 메뉴 | API | 설명 |
|------|-----|------|
| 시스템 정보 | `GET /settings/system` | Tenant명, 플랜, `backupEnabled`, `auditRetentionDays`, JWT issuer·access TTL |
| 기술 설정 | `PATCH /settings/system` | `backupEnabled`, `auditRetentionDays` 변경 (감사 로그 `SYSTEM_SETTINGS_UPDATED` 기록) |
| 감사 로그 | `GET /settings/audit-logs` | PII 접근·권한 변경·청구 확정·NHIS import 등 (페이지네이션) |
| 백업 | `GET /settings/backups` | 일일 백업 실행 이력 (`status`, `completedAt`, `sizeBytes`, `errorMessage`) |

**`PATCH /settings/system` 요청 예시**

```json
{
  "backupEnabled": true,
  "auditRetentionDays": 1095
}
```

> **백엔드**: `SettingsController`는 `@PreAuthorize("hasRole('SYSADMIN')")`로 보호됩니다. **프론트엔드 UI**는 아직 골격 단계이며, 현재는 API 또는 Swagger로 조회·설정합니다.

### 4-3. 감사 로그 (`audit_logs`)

감사 로그는 보안·개인정보 컴플라이언스의 핵심입니다. `sysadmin`은 **조회만** 가능하며, 로그 **삭제·수정은 불가**(append-only)합니다.

**필수 기록 대상** (DATA_RETENTION_POLICY §6)

| 이벤트 | `action` 예시 | 비고 |
|--------|--------------|------|
| 주민등록번호 복호화 열람 | `PII_DECRYPT_VIEW` | `POST /clients/{id}/resident-registration/reveal` 호출 시 |
| 청구서 상태 변경 | `BILLING_STATUS_CHANGE` | 작성중→확정→수납완료 |
| Tenant·지점·권한 변경 | `ORG_UPDATE`, `USER_ROLE_CHANGE` | |
| 대량 export·NHIS import | `NHIS_IMPORT`, `DATA_EXPORT` | |

**엔티티 행위자 컬럼** (V32–V33, `audit_logs`와 별도)

| 테이블 | 컬럼 | 기록 시점 |
|--------|------|----------|
| `attendance` | `created_by` | 수기·QR·결석 INSERT |
| `health_records` | `recorded_by` | 건강·투약·사고 기록 INSERT |
| `billing_claims` | `generated_by` | 월별 청구서 생성 |
| `nhis_import_batches` | `imported_by` | 공단 엑셀 import 완료 |

앱은 쓰기 트랜잭션에서 `DbSessionContext.setActorUserId(JWT subject)`를 호출하며, 누락 시 DB 트리거가 `ogada.actor_user_id` 세션 변수로 backstop합니다.

**조회 API** — `GET /settings/audit-logs`

```
?page=0&size=20
```

> 날짜·`action` 필터는 API_SPEC §9 기준이며, UI 필터는 후속 구현입니다.

**응답 필드 (스키마 기준)**

| 필드 | 설명 |
|------|------|
| `organization_id` | Tenant (자동 필터) |
| `branch_id` | 관련 지점 (nullable) |
| `actor_user_id` | 행위자 UUID (PII 대신 UUID) |
| `action` | 행위 코드 |
| `target_type` / `target_id` | 대상 리소스 |
| `details` | JSONB 부가 정보 (민감값 제외) |
| `created_at` | 발생 시각 |

**보존 기간**: **3년** (DATA_RETENTION_POLICY §3)

### 4-4. 백업·복구

| 항목 | 정책 |
|------|------|
| 주기 | **일 1회** 전체 DB 스냅샷 |
| 보관 | **30일** 롤링 |
| 암호화 | 백업 파일 at-rest 암호화 (KMS·환경변수 키) |
| RPO / RTO 목표 | 24시간 / 4시간 (인프라 구현 시 확정) |

**`sysadmin` 역할**

1. `/settings` → **백업** 탭(또는 `GET /settings/backups`)에서 최근 백업 성공 여부·시각을 확인합니다.
2. `backupEnabled`가 `false`이면 해당 Tenant는 스케줄러 대상에서 제외됩니다.
3. 복구가 필요하면 ogada ops(또는 자체 인프라 담당)에 **Tenant ID·장애 시각·증상**을 전달합니다.

**MVP 백업 실행 방식**

| 항목 | 내용 |
|------|------|
| 스케줄 | 기본 매일 02:00 (`BACKUP_DAILY_CRON`) |
| 실행체 | `FileTenantBackupExecutor` — Tenant별 `manifest.json` 생성 |
| 저장 경로 | `BACKUP_STORAGE_DIR/{organizationId}/` |
| 이력 | `backup_runs` 테이블 (V9, V20 무결성 제약) |
| 프로덕션 | `pg_dump` 또는 Managed DB 스냅샷으로 교체 예정 |

> 백업 인프라(PG dump, 클라우드 스냅샷 등) 상세는 `DEPLOYMENT_GUIDE.md` §8-2를 참고하세요.

### 4-5. 로그인 이력

| 항목 | 내용 |
|------|------|
| API | `GET /auth/login-history` (본인 또는 관리자) |
| DB 테이블 | `login_history` (V2 마이그레이션) |
| 보존 | **1년** |
| 활용 | 비정상 로그인·역할 오남용 탐지 |

`sysadmin`은 Tenant 소속 계정의 로그인 패턴을 모니터링하고, 의심 세션 발견 시 해당 계정 비활성화를 `hq_admin`에 요청합니다.

### 4-6. 시스템 관리자 일상 점검

| 주기 | 점검 항목 |
|------|----------|
| 매일 | 백업 성공 여부, API 헬스 (`/actuator/health`) |
| 매주 | 감사 로그 이상 패턴(PII 대량 열람, 권한 변경) |
| 매월 | `PII_ENCRYPTION_KEY`·`QR_TOKEN_SECRET` 로테이션 일정 확인 |
| 수시 | 신규 직원 `sysadmin` 계정 발급·퇴직 시 즉시 비활성화 |

---

## 5. 보안·개인정보 (관리자 공통)

### 5-1. PII 암호화 정책

| 데이터 | 분류 | 저장 처리 | 화면·로그 |
|--------|------|----------|----------|
| 주민등록번호 | 고유식별정보 | **AES-GCM 암호화** (`*_encrypted`) | 마스킹 `******-*******` |
| 연락처·주소 | 준식별정보 | **암호화 권장** | 부분 마스킹 |
| 장기요양인정번호 | 운영 식별자 | 평문 | 표시 가능 |
| 건강·투약 기록 | 민감정보 | TLS + RBAC | 접근 시 audit |

**구현**: `PiiCryptoService` — `ogada.security.pii-encryption-key` 환경변수(Base64, 32바이트) 필수.

**관리자 주의사항**

- 주민번호 **평문을 로그·티켓·이메일에 기록하지 않습니다.**
- 복호화 열람은 법정 목적(청구 등)에 한하며, `audit_logs`에 남습니다.
- 이용자 등록 시 **별도 수집·이용 동의**(`consent_collected_at`) 없으면 저장이 차단됩니다.

### 5-2. RBAC·지점 스코프

| 규칙 | 내용 |
|------|------|
| 역할 분리 | MVP **7역할** + `client_user` 각각 별도 화면·API 권한 |
| 지점 스코프 | `branch_admin` 이하는 `branch_ids` 내만 CRUD |
| `hq_admin` 쓰기 | `active_branch_id` 선택 지점만 CRUD, 전 지점 조회·집계 |
| API 강제 | `@PreAuthorize` + `JwtScopeResolver` 이중 검증 |
| 금지 | `platform_admin`을 Tenant API로 생성 시도 → 거부 |

### 5-3. QR 토큰 보안

- 지점 QR은 `QR_TOKEN_SECRET`으로 **서명·만료**된 토큰입니다.
- 만료·위조 QR 스캔 시 `422 BUSINESS_RULE` 오류.
- QR 토큰 메타 보존: 유효일 종료 후 **7일** (DATA_RETENTION_POLICY §3).

### 5-4. 에러·로그 노출 정책

- API 에러 응답에 **스택 트레이스·DB 스키마·키 경로를 노출하지 않습니다.**
- 클라이언트에는 `error.code`, `error.message`, `traceId`만 반환 (API_SPEC §0-3).

---

## 6. 계정·조직 관리 (관리자 협업)

일상 계정·지점 관리는 **`hq_admin`**(통합 관리자) 또는 **`branch_admin`**(지점장)이 수행합니다. `sysadmin`·`platform_admin`은 아래를 **참고·감독**합니다.

### 6-1. `sysadmin` 계정 발급

1. `hq_admin`이 **직원 계정 생성** 화면 또는 `POST /api/v1/users`로 발급합니다.
2. `roleCode`에 `sysadmin`을 지정합니다.
3. `sysadmin`은 지점 배정(`branchIds`) 없이 Tenant 전체 기술 설정만 담당합니다.

```json
{
  "email": "it@happy-care.com",
  "displayName": "박IT",
  "password": "<초기 비밀번호>",
  "roleCode": "sysadmin",
  "branchIds": []
}
```

### 6-2. 역할별 생성 권한

| 생성자 | 생성 가능 역할 |
|--------|---------------|
| `platform_admin` | `hq_admin` (Tenant당 최초 1회 API) |
| `hq_admin` | `branch_admin`, `social_worker`, `caregiver`, `guardian`, `client_user`, `sysadmin` |
| `branch_admin` | `branch_admin`, `social_worker`, `caregiver`, `guardian`, `client_user` |
| **공통 금지** | `platform_admin` — 어떤 API로도 생성 불가 |

**이메일 정책 (V30)**

- Tenant 내 직원 이메일은 **대소문자 무시 UK** — `Kim@center.com`과 `kim@center.com` 중복 불가.
- `UserService`가 저장 시 `trim().toLowerCase()` 정규화를 적용합니다.
- cross-tenant 동일 이메일은 DB UK로 막지 않으며, 로그인 시 **단일 active 계정**만 허용합니다 (`AuthService`).

**비밀번호 재설정 보안 (V30)**

- `POST /auth/password/reset` 성공 시 해당 사용자의 **활성 refresh 토큰 전부 폐기** (`revokeAllActiveForUser`).
- 재설정 링크·기존 세션 무효화로 탈취 계정의 지속 접속을 차단합니다.

### 6-3. 전사 운영 설정 (`hq_admin` 전담)

`sysadmin`이 아닌 **`hq_admin`**이 변경하는 정책입니다. IT 담당자는 변경 내역을 감사 로그로 확인합니다.

| 설정 | API | 기본값 | 설명 |
|------|-----|--------|------|
| 이용자 본인 QR 체크인 | `PATCH /organization/settings` | `false` | `allowClientSelfCheckin` |

```json
{ "allowClientSelfCheckin": true }
```

### 6-4. 지점·계정 비활성화

| 대상 | 처리 | 담당 |
|------|------|------|
| 퇴직 직원 | `PATCH /users/{id}` → `is_active: false` | `hq_admin` / `branch_admin` |
| 폐지 지점 | `PATCH /branches/{id}` → 비활성 | `hq_admin` |
| 해지 Tenant | `PATCH /platform/organizations/{id}` → `active: false` | `platform_admin` |

비활성화 ≠ 즉시 삭제. 보존·파기 일정은 `DATA_RETENTION_POLICY.md`를 따릅니다.

---

## 7. 장애 대응·모니터링

### 7-1. 헬스체크

| 엔드포인트 | 용도 | 인증 |
|------------|------|------|
| `GET /api/v1/health` | 애플리케이션 생존 확인 | 불필요 |
| `GET /actuator/health` | Spring Actuator (health, info) | 운영 시 접근 제한 권장 |

### 7-2. 자주 발생하는 증상

| 증상 | 가능 원인 | 조치 |
|------|----------|------|
| 이용자 등록 실패 | `PII_ENCRYPTION_KEY` 미설정 | 환경변수 설정 후 API 재기동 |
| QR 체크인 실패 | `QR_TOKEN_SECRET` 미설정·만료 토큰 | 시크릿 확인, 지점 QR 재생성 |
| 403 `FORBIDDEN_SCOPE` | 역할·지점 스코프 불일치 | JWT `branch_ids`, `active_branch_id` 확인 |
| 401 `UNAUTHENTICATED` | JWT 만료(30분) | 재로그인 또는 refresh |
| 타 Tenant 데이터 노출 의심 | 테넌트 필터 버그 | 즉시 ops 보고, `TenantContextFilter`·감사 로그 확인 |

### 7-3. 보안 사고 대응 (요약)

1. **격리**: 의심 계정 즉시 비활성화 (`is_active: false`).
2. **증거**: `audit_logs`, `login_history`, `traceId` 수집.
3. **키 로테이션**: 유출 의심 시 `PII_ENCRYPTION_KEY`, `QR_TOKEN_SECRET`, JWT 키 순차 교체.
4. **통보**: Tenant `hq_admin`·ogada security 담당에 보고 (개인정보 유출 시 법정 통지 절차).

---

## 8. 암호화 키 관리

### 8-1. 키 생성

```bash
# 32바이트 랜덤 키 → Base64 (PII_ENCRYPTION_KEY용)
openssl rand -base64 32
```

### 8-2. 키 보관 원칙

- 환경변수 또는 클라우드 **시크릿 매니저**(AWS Secrets Manager, GCP Secret Manager 등)에만 저장.
- `.env`, 소스코드, Slack·이메일에 **저장·공유 금지**.
- 운영·스테이징·개발 **키 분리**.

### 8-3. 키 로테이션 (권장 절차)

1. 새 키를 시크릿 매니저에 등록 (이중 키 기간 운영 — 구현 시).
2. 유지보수 시간대에 애플리케이션 재기동·키 전환.
3. 기존 암호화 데이터 **재암호화 배치** 실행 (v2+ 기능).
4. `audit_logs`에 `KEY_ROTATION` 이벤트 기록.

> MVP v1은 단일 키 운영. 로테이션·재암호화 자동화는 후속 구현입니다.

---

## 9. 데이터 보존·파기 (관리자 참고)

상세 정책은 `docs/DATA_RETENTION_POLICY.md`를 따릅니다. 관리자가 자주 확인하는 항목만 요약합니다.

| 데이터 | 보존 기간 |
|--------|----------|
| 이용자 PII·출석·건강 | 퇴소 후 **5년** |
| 청구·명세 | 청구 연도 기준 **5년** |
| 감사 로그 | **3년** |
| 로그인 이력 | **1년** |
| DB 백업 | **30일** 롤링 |

**Tenant 해지 시**: 정지 → **90일 유예** → 논리 삭제 → 백업 만료 후 물리 삭제.

**퇴소 이용자 purge (배치 후속)**

| 단계 | DB 지원 | 비고 |
|------|---------|------|
| 퇴소 cohort 스캔 | V32 `idx_clients_org_discharged_at` | `discharged_at IS NOT NULL` + Tenant 필터 |
| child 행 삭제·익명화 | V33 `idx_*_client_purge` | `attendance`·`health_records`·`billing_claim_items` by `client_id` |
| 배치 실행 | **미구현** | `@Scheduled` retention job 후속 (`DATA_RETENTION_POLICY` §4-1) |

---

## 10. API 빠른 참조 (관리자)

Base URL: `/api/v1` | 인증: `Authorization: Bearer <access_token>`

### 10-1. 플랫폼 (`platform_admin`)

| 메서드 | 경로 | 설명 |
|--------|------|------|
| GET | `/platform/organizations` | Tenant 목록 (`?query=` 검색 지원) |
| POST | `/platform/organizations` | Tenant 생성 |
| GET | `/platform/organizations/{orgId}` | Tenant 상세 |
| PATCH | `/platform/organizations/{orgId}` | 요금제·활성 상태 |
| POST | `/platform/organizations/{orgId}/admins` | 첫 `hq_admin` 발급 |

### 10-2. 시스템 설정 (`sysadmin` — 구현됨)

| 메서드 | 경로 | 설명 |
|--------|------|------|
| GET | `/settings/system` | 기술 설정 조회 |
| PATCH | `/settings/system` | `backupEnabled`, `auditRetentionDays` 변경 |
| GET | `/settings/audit-logs` | 감사 로그 (page, size) |
| GET | `/settings/backups` | 백업 실행 이력 |

### 10-3. 조직 (`hq_admin` / `sysadmin` 조회)

| 메서드 | 경로 | 설명 |
|--------|------|------|
| GET | `/organization` | 현재 Tenant 정보 |
| PATCH | `/organization/settings` | 전사 정책 (`hq_admin` only) |

### 10-4. 청구 (`hq_admin` / `branch_admin` — 구현됨)

| 메서드 | 경로 | 설명 |
|--------|------|------|
| GET | `/billing/claims` | 청구 목록 (`?branchId=`, `?status=` — `DRAFT`/`CONFIRMED`/`PAID`) |
| POST | `/billing/claims/generate` | 월별 청구서 생성 |
| PATCH | `/billing/claims/{claimId}/status` | 상태 전이 (DRAFT→CONFIRMED→PAID) |
| POST | `/billing/nhis-import` | 공단 엑셀 import |

전체 명세: `docs/API_SPEC.md`

---

## 11. 관련 문서

| 문서 | 대상 |
|------|------|
| `USER_MANUAL.md` | 센터장·사회복지사·보호자 현장 매뉴얼 |
| `DEPLOYMENT_GUIDE.md` | 인프라·Docker·배포 |
| `CHANGELOG.md` | 버전별 변경 이력 |
| `DATA_RETENTION_POLICY.md` | 보존·파기·백업 정책 |
| `API_SPEC.md` | REST API 전체 명세 |
| `FLOWCHART.md` | 화면·역할 흐름도 |
| `REQUIREMENTS.md` | 기능·비기능 요구사항 |

---

## 12. 용어집

| 용어 | 설명 |
|------|------|
| Tenant | SaaS 고객 1법인 = `Organization` 1개 |
| Branch | Tenant 소속 주간보호센터 지점 1곳 |
| RBAC | 역할 기반 접근 제어 (JWT `role` + 지점 스코프) |
| PII | 개인식별정보 (주민번호·연락처·주소 등) |
| NHIS import | 공단 청구내역상세 엑셀 업로드 연동 |
| Branch Switcher | 다지점 권한 사용자의 `active_branch_id` 전환 UI |

---

## 13. 변경 이력

| 날짜 | 변경 내용 |
|------|----------|
| 2026-06-06 | V32–V33: actor backstop 트리거·퇴소 purge 인덱스·청구 상태 필터 API·§4-3 actor 컬럼 |
| 2026-06-06 | V29–V31: 사업자번호 검색·Tenant 이메일 UK·비밀번호 재설정 세션 폐기·청구 상태 DB 인덱스 |
| 2026-06-06 | 플랫폼 Tenant 검색·주민번호 복호화 API·Flyway V27–V28 성능 인덱스 반영 |
| 2026-06-06 | 설정 API·백업 스케줄러 구현 반영, 환경변수·NHIS 대사 보강 |
| 2026-06-05 | 초안 작성 — `platform_admin`·`sysadmin` 가이드 |

---

*이 문서는 tech_writer 에이전트가 관리합니다. API·UI 변경 시 §1-4 구현 상태를 동기화하세요.*
