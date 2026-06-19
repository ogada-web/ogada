<!-- doc:owner=PLN,TWR doc:audience=COD,TSR,UXD,DBA,BNK updated=2026-06-19T16:00:00+09:00 -->
<!-- tech_writer-sync: TWR 248차 2026-06-19T16:00:00 UTC — API_SPEC resync (246차→248차) — **G17 기능회복훈련, G32 케이스관리, G42 민원상담 3개 섹션 추가** · BE `429661e` / FE `40d0ca3` · §9-16/9-17/9-18 MUST docs 신규 추가 · next: FAQ G17/G32/G42 온보딩 가이드 → FAQ Q500+ · docs/ops/README 동기화 -->
# 주간보호센터 웹 시스템 — REST API 명세 (technical/API_SPEC.md)

> **작성**: planner, tech_writer 에이전트
> **최초 작성일**: 2026-06-05
> **최종 갱신**: 2026-06-19 (TWR 248차 — **API_SPEC 신규 섹션 추가** — §9-16 케이스관리/G32, §9-17 기능회복훈련/G17, §9-18 민원상담/G42 · 구현 완료 기능 문서화 · BE `429661e` / FE `40d0ca3`)
> **상태**: 초안 (Draft) — 사용자 승인 전
> **범위**: MVP v1 (Must) + v1.1~v2 주요 API — 인증, 플랫폼, 조직·지점, 이용자, 출석, 건강, 청구, 대시보드, 선임보호사 일지, 욕구사정, 급여계약 첨부, NHIS 일정 동기화, 이동서비스 기록, 간호 급여, **케이스관리·기능회복훈련·민원상담**, 시스템 헬스체크
> **기준 문서**: `REQUIREMENTS.md`, `USER_STORIES.md`, `CHANGELOG.md` · **backend** `429661e` / **frontend** `40d0ca3`

---

## 0. 공통 규약

### 0-1. 기본

| 항목 | 값 |
|------|------|
| Base URL | `/api/v1` |
| 백엔드 | Spring Boot 3.x (REST) |
| 포맷 | JSON (요청·응답 `application/json; charset=utf-8`) |
| 인증 | `Authorization: Bearer <access_token>` (JWT) |
| 시간 | ISO 8601, UTC 저장 / 응답은 `Asia/Seoul` 표기 |
| 날짜 | `YYYY-MM-DD`, 일시 `YYYY-MM-DDTHH:mm:ss+09:00` |
| ID | 외부 노출 식별자는 UUID (로그·URL에 PII 미노출) |

### 0-2. 멀티테넌트·스코프 (REQUIREMENTS §2-3)

- 모든 운영 데이터 API는 JWT의 `organization_id`로 **테넌트 격리**를 강제한다.
- 지점 스코프 역할은 `branch_ids` 범위만 접근, `hq_admin` 쓰기는 `active_branch_id` 선택 시 해당 지점만.
- `organization_id` / `branch_id`는 **요청 본문이 아닌 토큰**에서 취득한다 (위변조 방지). 목록 조회 시 `branchId` 쿼리는 토큰 스코프 내에서만 허용.

### 0-3. 공통 응답·에러

성공 목록 응답(페이지네이션):

```json
{
  "items": [],
  "page": 0,
  "size": 20,
  "totalElements": 0,
  "totalPages": 0
}
```

에러 응답(스택·DB 정보 미노출 — rules.md §3):

```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "사용자에게 보여줄 한국어 메시지",
    "traceId": "uuid"
  }
}
```

| HTTP | code 예시 | 의미 |
|------|----------|------|
| 400 | `VALIDATION_ERROR` | 입력 검증 실패 |
| 401 | `UNAUTHENTICATED` | 토큰 없음·만료 |
| 403 | `FORBIDDEN_SCOPE` | 역할·지점·테넌트 스코프 위반 |
| 404 | `NOT_FOUND` | 리소스 없음 |
| 409 | `CONFLICT` | 중복·상태 충돌 |
| 422 | `BUSINESS_RULE` | 업무 규칙 위반(예: 중복 체크인) |

### 0-4. 페이지네이션·검색 공통 쿼리

`?page=0&size=20&sort=createdAt,desc&q=검색어&branchId=<uuid>`

### 0-5. 역할 코드

`platform_admin`, `hq_admin`, `branch_admin`, `social_worker`, `caregiver`, `guardian`, `client_user`, `sysadmin`

---

## 1. 인증 (Auth) — §3-1

| 메서드 | 경로 | 설명 | 권한 |
|--------|------|------|------|
| POST | `/auth/login` | 이메일·비밀번호 로그인 → 토큰 발급 | 공개 |
| POST | `/auth/refresh` | refresh 토큰으로 access 재발급 | 공개(refresh) |
| POST | `/auth/logout` | refresh 토큰 폐기 | 인증 |
| POST | `/auth/password/reset-request` | 비밀번호 재설정 메일 발송 | 공개 |
| POST | `/auth/password/reset` | 토큰으로 비밀번호 변경 | 공개(reset token) |
| GET | `/auth/me` | 현재 사용자·역할·스코프 조회 | 인증 |
| POST | `/auth/active-branch` | `active_branch_id` 전환(지점 선택기) | 다지점 권한 |
| GET | `/auth/login-history` | 로그인 이력 | 본인/관리자 |

**POST `/auth/login` 요청·응답**

```json
// 요청
{ "email": "kim@happy-care.com", "password": "********" }

// 응답
{
  "accessToken": "jwt...",
  "refreshToken": "jwt...",
  "expiresIn": 1800,
  "user": {
    "id": "uuid",
    "name": "김센터장",
    "role": "hq_admin",
    "organizationId": "uuid",
    "branchIds": ["uuid-a", "uuid-b"],
    "activeBranchId": "uuid-a"
  }
}
```

**JWT 클레임**: `sub`, `role`, `organization_id`, `branch_ids[]`, `active_branch_id`, `exp`(30분).

---

## 2. 플랫폼 관리 (Platform) — §1-3, `platform_admin` 전용

> ogada 직원이 신규 고객 센터(Tenant)와 첫 `hq_admin`을 생성. 운영 데이터 CRUD 없음.

| 메서드 | 경로 | 설명 |
|--------|------|------|
| GET | `/platform/organizations` | 전국 가입 고객사(Tenant) 목록 |
| POST | `/platform/organizations` | 신규 고객 Organization 등록 |
| GET | `/platform/organizations/{orgId}` | 고객사 상세 |
| PATCH | `/platform/organizations/{orgId}` | 요금제·상태 변경(활성/정지) |
| POST | `/platform/organizations/{orgId}/admins` | 첫 `hq_admin` 계정 발급 |

**POST `/platform/organizations`**

```json
{ "name": "행복주간보호센터", "businessNo": "123-45-67890", "plan": "standard" }
```

---

## 3. 조직·지점 (Organizations / Branches) — §3-12

| 메서드 | 경로 | 설명 | 권한 |
|--------|------|------|------|
| GET | `/organization` | 자기 Tenant 정보·설정 | hq_admin, sysadmin |
| PATCH | `/organization/settings` | 전사 설정(`allow_client_self_checkin` 등) | hq_admin |
| GET | `/branches` | 지점 목록 | hq_admin(전체), 그 외(소속) |
| POST | `/branches` | 지점 등록 | hq_admin |
| GET | `/branches/{branchId}` | 지점 상세 | 스코프 내 |
| GET | `/branches/integrated-home/provider-discovery` | 통합재가 제공기관 검색 가이드(롱텀 portal) | hq_admin, branch_admin |
| PATCH | `/branches/{branchId}` | 지점 수정·비활성 | hq_admin |
| GET | `/users` | 직원 계정 목록(지점 필터) | hq_admin, branch_admin |
| POST | `/users` | 직원 계정 생성·역할·지점 배정 | hq_admin, branch_admin |
| PATCH | `/users/{userId}` | 계정 수정·역할 변경·퇴직 처리 | hq_admin, branch_admin |

**PATCH `/organization/settings`**

```json
{ "allowClientSelfCheckin": true }
```

### 3-1. 통합재가 제공기관 탐색 (G19) — v2

> **목적**: 통합재가 제공기관 검색 시 롱텀케어 포털의 필터 파라미터·코드를 FE에 전달한다.  
> **참고**: FAQ 610(통합재가 안내)·longterm provider search `menuId=npe0000002783` (`ltcAdminKindChoiceYn8=Y`, `searchAdminKindCd=06|07`, 월 10만원 가산 공지).

**GET `/branches/integrated-home/provider-discovery`**

| 필드 | 타입 | 설명 |
|------|------|------|
| `providerSearchUrl` | string | 롱텀케어 제공기관 검색 URL(`selectLtcoSrch.web?menuId=npe0000002783`) |
| `integratedHomeFilterParam` | string | 통합재가 필터 파라미터 키(`ltcAdminKindChoiceYn8`) |
| `integratedHomeFilterValue` | string | 통합재가 필터 값(`Y`) |
| `daytimeAndShortTermServiceCodeParam` | string | 서비스 유형 코드 파라미터(`searchAdminKindCd`) |
| `daytimeCareServiceCode` | string | 주야간보호 코드(`06`) |
| `shortTermCareServiceCode` | string | 단기보호 코드(`07`) |
| `monthlyAddonNotice` | string | 「주·야간보호형: 수급자 1인당 월 10만원 지급」 안내 문구 |

**예시 응답**

```json
{
  "providerSearchUrl": "https://www.longtermcare.or.kr/npbs/r/a/201/selectLtcoSrch.web?menuId=npe0000002783",
  "integratedHomeFilterParam": "ltcAdminKindChoiceYn8",
  "integratedHomeFilterValue": "Y",
  "daytimeAndShortTermServiceCodeParam": "searchAdminKindCd",
  "daytimeCareServiceCode": "06",
  "shortTermCareServiceCode": "07",
  "monthlyAddonNotice": "주·야간보호형: 수급자 1인당 월 10만원 지급"
}
```

---

## 4. 이용자 (Clients) — §3-2

| 메서드 | 경로 | 설명 | 권한 |
|--------|------|------|------|
| GET | `/clients` | 이용자 목록(지점 필터·검색·페이지) | 스코프 내 조회 |
| POST | `/clients` | 이용자 등록(소속 `branchId` 필수) | branch_admin, social_worker |
| GET | `/clients/{clientId}` | 이용자 상세 | 스코프 내 |
| PATCH | `/clients/{clientId}` | 이용자 수정 | branch_admin, social_worker |
| POST | `/clients/{clientId}/discharge` | 퇴소 처리 | branch_admin |
| POST | `/clients/{clientId}/photo` | 사진 업로드(검증·용량 제한) | branch_admin, social_worker |
| GET | `/clients/{clientId}/guardians` | 연결 보호자 목록 | 스코프 내 |
| POST | `/clients/{clientId}/guardians` | 보호자 연결 | branch_admin, social_worker |
| POST | `/clients/{clientId}/client-user` | 이용자 본인 계정 발급(`client_user`) | branch_admin |

### 4-1. 보호자 초대 (Guardian Invitations) — US-J01, v1.1

> **채널**: v1.1 = **`EMAIL` 단일**(결정 59). SMS·카카오·FCM은 v2(US-J03).  
> **만료**: 초대 토큰 **7일**(PLAN_NOTES #35 가정 — 사용자 확정 전). 재발송 시 **기존 PENDING 토큰 무효화**.  
> **DB**: Flyway **`V43__guardian_invitations.sql`** (56차 WT 관측).  
> **구현 상태**: develop WT WIP — **BE-8 Planned**(Controller·Service·test HEAD ABSENT @ `428ba7d`).

| 메서드 | 경로 | 설명 | 권한 |
|--------|------|------|------|
| POST | `/clients/{clientId}/guardians/invitations` | 보호자 **이메일 초대** 발송 | branch_admin, social_worker |
| GET | `/clients/{clientId}/guardians/invitations` | 이용자별 초대 **목록** | branch_admin, social_worker, hq_admin(스코프) |
| POST | `/guardian/invitations/{token}/accept` | 초대 **수락** — `guardian` 계정 생성·`guardian_clients` 연결 | 공개(토큰) 또는 `guardian`(로그인) |
| POST | `/clients/{clientId}/guardians/invitations/{invitationId}/resend` | 만료 전 **재발송**(기존 PENDING 무효화) | branch_admin, social_worker |
| DELETE | `/clients/{clientId}/guardians/invitations/{invitationId}` | PENDING 초대 **취소** | branch_admin, social_worker |

**POST `/clients/{clientId}/guardians/invitations` 요청**

```json
{
  "email": "guardian@example.com",
  "relationship": "자녀",
  "channel": "EMAIL"
}
```

> `channel`은 v1.1에서 **`EMAIL`만 허용** — 다른 값은 `400`.

**POST `/clients/{clientId}/guardians/invitations` 응답 (`GuardianInvitationResponse`)**

```json
{
  "id": "uuid",
  "clientId": "uuid",
  "email": "g***@example.com",
  "relationship": "자녀",
  "channel": "EMAIL",
  "status": "PENDING",
  "expiresAt": "2026-06-14T23:59:59+09:00",
  "createdAt": "2026-06-07T12:00:00+09:00"
}
```

**POST `/guardian/invitations/{token}/accept` 요청 (`AcceptGuardianInvitationRequest`)**

```json
{
  "name": "홍보호",
  "phone": "010-1234-5678",
  "password": "********"
}
```

**POST `/guardian/invitations/{token}/accept` 응답 (`AcceptGuardianInvitationResponse`)**

```json
{
  "guardianUserId": "uuid",
  "clientId": "uuid",
  "accessToken": "jwt...",
  "refreshToken": "jwt..."
}
```

> **에러**: 만료 토큰 → `410`(`InvitationExpiredException`). 이미 수락/취소 → `409`. 타 Tenant 토큰 → `404`(정보 최소 노출).

**보안 게이트 (SEC-D8, BE-8 commit/merge 전 필수 — `SECURITY_CHECKLIST` H-6)**

| 항목 | 요구사항 |
|------|----------|
| `SecurityConfig` 공개 endpoint | `POST /guardian/invitations/{token}/accept` **단일 경로만** `permitAll` — 과잉 허용 시 인증 우회 BLOCK |
| 토큰 정책 | `InvitationTokenService` — **단일사용**(used_at/상태 전환)·**만료**(7일)·**128-bit 엔트로피** |
| 에러 응답 | `GlobalExceptionHandler` — 응답에 **토큰 값·내부 스키마·키 경로 미노출** |
| rate limit | 초대 accept endpoint — IP·email 기준 **rate limit** 적용(브루트포스·재시도 남용 방지) |

> SEC-D8 미해소 시 J01 backend API **commit/merge 금지** (`docs/security/SECURITY_AUDIT.md` §1.6-C″).

### 4-2. 등급 변동 이력 (LTC Grade History) — US-M01, v1.2.1 (G14)

> **벤치마크**: 케어포 func.php 1-9 · BNK-14.  
> **DB**: Flyway **`V48__client_ltc_grade_history.sql`** @ backend `2012945` — 테이블 `client_ltc_grade_history` + 트리거 append.  
> **구현 상태 (79차 git 실측)**: frontend **UI ✅** @ `6d0a03a` (`GradeHistoryTimeline`) · backend **GET API ✅** @ `15e41e3` (`ClientController`·`LtcGradeHistoryService`·`LtcGradeHistoryServiceTest` 4 @Test).

| 메서드 | 경로 | 설명 | 권한 |
|--------|------|------|------|
| GET | `/clients/{clientId}/ltc-grade-history` | 이용자 **등급 변동 이력** 목록(최신순·페이지) | 스코프 내 조회 |
| POST | `/clients/{clientId}/ltc-grade-history` | 등급 이력 **수동 등록**(선택 — 감사 추적) | branch_admin, social_worker |

**이력 append 규칙 (PATCH `/clients/{clientId}` 연동)**

- `ltcGrade` 필드가 **이전값과 다를 때** `ltc_grade_history`에 **append-only** INSERT.
- 동일 요청 내 `ltcGrade` 미변경 시 이력 **생성하지 않음**.
- `clients.ltc_grade`는 **현행 등급** 단일값 유지 — 이력 테이블과 정합.

**`ltc_grade_history` 스키마 (초안)**

| 컬럼 | 타입 | 설명 |
|------|------|------|
| `id` | UUID | PK |
| `organization_id` | UUID | 테넌트 격리 |
| `client_id` | UUID | FK → `clients(id)` ON DELETE CASCADE |
| `previous_grade` | SMALLINT NULL | 이전 등급(1~5, 최초 등록 시 NULL) |
| `new_grade` | SMALLINT | 변경 후 등급 |
| `changed_at` | TIMESTAMPTZ | 변경 시각(기본 `now()`) |
| `reason` | VARCHAR(500) NULL | 변경 사유(선택) |
| `changed_by_user_id` | UUID NULL | 변경 수행자 |

**GET `/clients/{clientId}/ltc-grade-history` 응답 (`LtcGradeHistoryPage`)**

```json
{
  "items": [
    {
      "id": "uuid",
      "previousGrade": 4,
      "newGrade": 3,
      "changedAt": "2026-05-15T10:30:00+09:00",
      "reason": "재평가",
      "changedBy": { "userId": "uuid", "displayName": "김사회" }
    }
  ],
  "page": 0,
  "size": 20,
  "totalElements": 1
}
```

> **PII**: 응답에 주민번호·인증번호 미포출. 로그에는 `client_id` UUID만 사용.

### G37 — 등급 인정기간별 첨부 PDF (BNK-105)

> **벤치마크**: 이지케어 Channel.io 49a778e8 · BNK-105.  
> **DB**: Flyway **`V78__ltc_grade_history_attachments.sql`** @ backend `0325d95`.  
> **구현 상태 (109차 git 실측)**: backend **CRUD API ✅** @ `0325d95`/`c4b230b`(V78+V79) · frontend **UI ✅ Fixed** @ `e026ae9`/`23bcd8c` · **live E2E harness ✅** @ `6875af5` · **MIME fallback guard ✅** @ `e9d1178` (QA-B46 Fixed · `GradeHistoryAttachmentPanel`, Q274).

| 메서드 | 경로 | 설명 | 권한 |
|--------|------|------|------|
| GET | `/clients/{clientId}/ltc-grade-history/{historyId}/attachments` | 등급 이력 행 **첨부 목록** | HQ_ADMIN, BRANCH_ADMIN, SOCIAL_WORKER, CAREGIVER |
| POST | `/clients/{clientId}/ltc-grade-history/{historyId}/attachments` | **PDF/PNG 업로드** (`multipart/form-data`, field `file`) | BRANCH_ADMIN, SOCIAL_WORKER |
| GET | `/clients/{clientId}/ltc-grade-history/{historyId}/attachments/{attachmentId}` | 첨부 **다운로드/미리보기** (inline) | HQ_ADMIN, BRANCH_ADMIN, SOCIAL_WORKER, CAREGIVER |
| DELETE | `/clients/{clientId}/ltc-grade-history/{historyId}/attachments/{attachmentId}` | 첨부 **삭제** | BRANCH_ADMIN, SOCIAL_WORKER |

**업로드 제약 (초안)**

- 허용 MIME: `application/pdf`, `image/png`
- 최대 크기: 환경변수 `ltc-grade-attachment.max-bytes` (기본 10MB)
- 저장: 로컬 파일시스템 (`LtcGradeHistoryAttachmentStorageService`) — 운영 시 S3 등 후속 검토

**`LtcGradeHistoryAttachmentResponse` (POST 201)**

```json
{
  "id": "uuid",
  "historyId": "uuid",
  "originalFilename": "care-plan-2026.pdf",
  "contentType": "application/pdf",
  "sizeBytes": 102400,
  "uploadedAt": "2026-06-11T10:00:00+09:00",
  "uploadedBy": { "userId": "uuid", "displayName": "김사회" }
}
```

> **FE (US-M01-g, Fixed @ `e026ae9`/`e9d1178`)**: `GradeHistoryTimeline` 행별 **`GradeHistoryAttachmentPanel`** — `<details>` 펼침 시 lazy load · PDF/PNG **`FileUpload`** · Modal 미리보기 · **`canUpload`=`branch_admin`|`social_worker`**. FAQ Q274 · USER_MANUAL §3-3.

### G30 — 모니터링 자가진단 · 유선상담 · 통합 checklist (BNK-169~184)

> **벤치마크**: 이지케어 [FAQ 21836](https://ezcare.easyms.co.kr/help/faq.ez?rowid=21836&type=web) 자가점검 5필드 · [FAQ 21841](https://ezcare.easyms.co.kr/help/faq.ez?rowid=21841&type=web) 월 5회 유선상담 · [FAQ 21842](https://ezcare.easyms.co.kr/help/faq.ez?rowid=21842&type=web) rolling 6개월.  
> **구현 상태 (2026-06-14 git 실측)**: backend **self-diagnosis+phone consultation ✅** @ `6a72b70`/`b8e92bf` · **integrated checklist API ✅** @ `b1dfd34`/`997831c` · frontend **UI ✅ full** @ `6f6915f`/`400c835`/`5146895` — `/compliance/monitoring`·`IntegratedMonitoringChecklistPanel`·pilot E2E · **잔여 P1**: live API E2E verify.

| 메서드 | 경로 | 설명 | 권한 |
|--------|------|------|------|
| GET | `/api/v1/compliance/monitoring/checklist` | FAQ21838/21839/21841/21842 **통합 aggregate** compliance | HQ_ADMIN, BRANCH_ADMIN, SOCIAL_WORKER |
| GET | `/api/v1/compliance/monitoring/items` | FAQ21836 15문항 템플릿(5필드) 조회 | HQ_ADMIN, BRANCH_ADMIN, SOCIAL_WORKER |
| GET | `/api/v1/compliance/monitoring/self-diagnoses` | 월별 자가진단 목록 (`branchId?`, `referenceYear?`, `referenceMonth?` 기본=오늘) | HQ_ADMIN, BRANCH_ADMIN, SOCIAL_WORKER |
| POST | `/api/v1/compliance/monitoring/self-diagnoses` | 자가진단 등록 — **문항당 월 1회** 중복 불가 | HQ_ADMIN, BRANCH_ADMIN, SOCIAL_WORKER |
| PATCH | `/api/v1/compliance/monitoring/self-diagnoses/{diagnosisId}` | 자가진단 수정 | HQ_ADMIN, BRANCH_ADMIN, SOCIAL_WORKER |
| GET | `/api/v1/compliance/monitoring/self-diagnoses/compliance` | 최근 **6개월 rolling** 기록 여부 집계 (`referenceDate?` 기본=오늘) | HQ_ADMIN, BRANCH_ADMIN, SOCIAL_WORKER |
| GET | `/api/v1/compliance/monitoring/phone-consultations` | 월별 유선상담 목록 (`branchId?`, `referenceYear?`, `referenceMonth?`) | HQ_ADMIN, BRANCH_ADMIN, SOCIAL_WORKER |
| GET | `/api/v1/compliance/monitoring/phone-consultations/suggestions` | 해당 월 상담 미작성 수급자 **최대 5명 추천** | HQ_ADMIN, BRANCH_ADMIN, SOCIAL_WORKER |
| POST | `/api/v1/compliance/monitoring/phone-consultations` | 유선상담 등록 — **수급자당 월 1회** 중복 불가 | HQ_ADMIN, BRANCH_ADMIN, SOCIAL_WORKER |
| GET | `/api/v1/compliance/monitoring/phone-consultations/compliance` | 월 상담 **5회 달성 여부** 집계 | HQ_ADMIN, BRANCH_ADMIN, SOCIAL_WORKER |

**`CreateMonitoringSelfDiagnosisRequest` (POST)**

```json
{
  "referenceYear": 2026,
  "referenceMonth": 6,
  "itemCode": 6,
  "inspectionDirection": "모니터링 자가진단",
  "relatedBasis": "장기요양급여 모니터링 지침",
  "inspectionCriteria": "매월 작성 여부",
  "inspectionResult": "양호",
  "inspectionMethod": "현장 확인"
}
```

**`MonitoringSelfDiagnosisResponse`**

```json
{
  "id": "uuid",
  "branchId": "uuid",
  "referenceYear": 2026,
  "referenceMonth": 6,
  "itemCode": 6,
  "inspectionDirection": "모니터링 자가진단",
  "relatedBasis": "장기요양급여 모니터링 지침",
  "inspectionCriteria": "매월 작성 여부",
  "inspectionResult": "양호",
  "inspectionMethod": "현장 확인"
}
```

**`MonitoringSelfDiagnosisComplianceResponse` (GET /self-diagnoses/compliance)**

```json
{
  "rollingMonthWindow": 6,
  "recordedMonthCount": 4,
  "requiredMonthCount": 6,
  "rollingComplete": false,
  "months": [
    { "referenceYear": 2026, "referenceMonth": 2, "recorded": true, "itemCount": 15 }
  ]
}
```

**`CreateMonitoringPhoneConsultationRequest` (POST)**

```json
{
  "referenceYear": 2026,
  "referenceMonth": 6,
  "clientId": "uuid",
  "consultedAt": "2026-06-12",
  "consultationNotes": "보호자 유선상담 실시"
}
```

**`MonitoringPhoneConsultationResponse`**

```json
{
  "id": "uuid",
  "branchId": "uuid",
  "referenceYear": 2026,
  "referenceMonth": 6,
  "clientId": "uuid",
  "clientName": "김수급",
  "consultedAt": "2026-06-12",
  "consultationNotes": "보호자 유선상담 실시"
}
```

**`MonitoringPhoneConsultationComplianceResponse` (GET /phone-consultations/compliance)**

```json
{
  "referenceYear": 2026,
  "referenceMonth": 6,
  "recordedCount": 3,
  "requiredCount": 5,
  "complete": false
}
```

> **제약/검증**: `branchId` 생략 시 활성 지점 필수(`TenantContext`), 요청 지점 읽기 스코프 검증. 자가진단·유선상담 모두 **월 중복 불가**. 필드 문자열은 공백 제거 후 저장, 비어 있으면 400(BusinessRuleException). 유선상담 목록·추천은 **활성 수급자**만 포함.

### G38 — 급여제공계획서 통보 모니터링 (BNK-106)

> **벤치마크**: 이지케어 [FAQ 21802](https://ezcare.easyms.co.kr/help/faq.ez?rowid=21802&type=web) — 황갈색=5·11개월 경과·빨간색=이용계획서 재발급 미반영.  
> **구현 상태 (109차 git 실측)**: backend **compliance API ✅** @ `5fd35a6` · frontend **StatCard/monitoring UI P2** (미구현).

| 메서드 | 경로 | 설명 | 권한 |
|--------|------|------|------|
| GET | `/clients/care-plan-notifications/compliance` | 수급자별 **5·11개월 마일스톤**·최신 등급 행 care-plan 첨부 누락·재발급 미반영 집계 | HQ_ADMIN, BRANCH_ADMIN, SOCIAL_WORKER |

**`CarePlanNotificationComplianceResponse` (200)**

```json
{
  "totalClients": 42,
  "fiveMonthsWarningCount": 3,
  "elevenMonthsWarningCount": 1,
  "reissueNotReflectedCount": 2,
  "items": [
    {
      "clientId": "uuid",
      "clientName": "홍길동",
      "monthsSinceCertification": 6,
      "alertLevel": "WARNING",
      "latestGradeHistoryId": "uuid",
      "carePlanAttachmentMissing": true,
      "reissueNotReflected": false
    }
  ]
}
```

> **`alertLevel`**: `OK` | `WARNING`(5·11개월) | `CRITICAL`(재발급 미반영). FE P2: dashboard StatCard·G37 첨부 패널 연계 surface.

### G39 — 급여제공결과평가 (지표44, BNK-107)

> **벤치마크**: silverangel [daycareEssentialWork 지표44](https://www.silverangel.kr/newSilverangel/daycare/daycareEssentialWork.do) — ①주1 상태변화 ②월1 기록지 ③연1 평가 ④30일 계획 재작성.  
> **DB**: Flyway **`V80__provision_result_evaluations_g39.sql`** @ backend `f082933`.  
> **구현 상태 (109차 git 실측)**: backend **CRUD+compliance API ✅** @ `f082933` · frontend **`ProvisionResultEvaluationPage` ✅** @ `1c99bcd` · **dashboard StatCard P2**.

| 메서드 | 경로 | 설명 | 권한 |
|--------|------|------|------|
| GET | `/provision-result-evaluations` | 연간 평가 목록 (`year`, `clientId` query) | HQ_ADMIN, BRANCH_ADMIN, SOCIAL_WORKER, CAREGIVER |
| POST | `/provision-result-evaluations` | 연간 평가 **등록** | HQ_ADMIN, BRANCH_ADMIN, SOCIAL_WORKER |
| PATCH | `/provision-result-evaluations/{evaluationId}` | 연간 평가 **수정** | HQ_ADMIN, BRANCH_ADMIN, SOCIAL_WORKER |
| GET | `/provision-result-evaluations/compliance` | **지표44 4-pillar** 준수 집계 (`year` query) | HQ_ADMIN, BRANCH_ADMIN, SOCIAL_WORKER |

**`CreateProvisionResultEvaluationRequest` (POST)**

```json
{
  "clientId": "uuid",
  "evaluationDate": "2026-06-01",
  "overallSummary": "급여제공 결과 총평",
  "evaluatorName": "김사회"
}
```

**`ProvisionResultComplianceResponse` (GET /compliance)**

```json
{
  "evaluationYear": 2026,
  "totalClients": 40,
  "weeklyStateChangeMetCount": 38,
  "monthlyProvisionRecordProvidedCount": 35,
  "annualEvaluationConductedCount": 12,
  "evaluationReflectedWithin30DaysCount": 10,
  "items": []
}
```

> **FE (US-T08, Fixed @ `1c99bcd`)**: `/programs/provision-result-evaluations` · `Field` render-prop 폼 · `services.js` G39 API helpers. dashboard StatCard **P2**.

---

**POST `/clients` 요청 (PII 처리 — §보안 주석 참고)**

```json
{
  "branchId": "uuid",
  "name": "홍길동",
  "birthDate": "1945-03-02",
  "gender": "M",
  "address": "서울시 ...",
  "phone": "010-0000-0000",
  "residentRegistrationNo": "암호화 저장 대상(수집 시)",
  "ltcGrade": 3,
  "ltcCertNo": "L0000000000",
  "ltcCertValidFrom": "2026-01-01",
  "ltcCertValidTo": "2027-12-31",
  "copayType": "GENERAL",
  "primaryGuardian": {
    "guardianUserId": "uuid",
    "relationship": "자녀"
  }
}
```

> **보안**: `residentRegistrationNo`(주민등록번호)는 고유식별정보 → **저장 시 암호화**, 응답·로그·목록에는 **마스킹**(`******-*******`)만 노출. 수집 여부는 §보안 미확정(아래 메모) 확정 후 반영.
> **`copayType`**: `GENERAL`(일반) | `REDUCED_40`(감경) | `REDUCED_60`(감경) | `MEDICAID`(기초·의료급여) — 실제 비율은 `copay_rates` 테이블 참조(§7).
> **`primaryGuardian` (필수 — 결정 19·US-D01, 2026-06-06 7차 명세화)**: 활성 이용자는 **보호자 1명 이상 연결이 필수**다. 등록 요청에 **기존 `guardian` 계정의 `guardianUserId`**(+ 관계)를 포함하면 `clients` INSERT와 동시에 `guardian_clients` 연결·대표(primary) 지정이 **단일 트랜잭션**으로 처리되고, `clients.guardian_link_status`가 `LINKED`로 설정된다(V39). 누락 시 `400`(`guardian_link_status=PENDING` 잔존 금지). 등록 후 추가 보호자는 `POST /clients/{clientId}/guardians`로 연결. *(구현: `CreateClientRequest.primaryGuardian`·`PrimaryGuardianLinkRequest` — develop `4d476c6` HEAD 정합.)*

---

## 5. 출석 (Attendance) — §3-3

| 메서드 | 경로 | 설명 | 권한 |
|--------|------|------|------|
| GET | `/attendance` | 출석 현황(날짜·지점 필터) | 스코프 내 조회 |
| POST | `/attendance/check-in` | 수기 체크인 | caregiver 이상 |
| POST | `/attendance/check-out` | 수기 체크아웃(교통편 기록) | caregiver 이상 |
| POST | `/attendance/absence` | 결석 사유 기록 | caregiver 이상 |
| GET | `/attendance/stats/monthly` | 월별 출석 통계(지점/통합) | 조회 |
| POST | `/branches/{branchId}/qr` | 지점 QR 생성(입소/귀가, 유효시간) | branch_admin 이상 |
| GET | `/branches/{branchId}/qr` | 현재 유효 QR 조회·출력 | branch_admin 이상 |
| POST | `/attendance/qr/scan` | QR 셀프 체크인/아웃 | guardian, client_user |
| GET | `/guardian/checkin-targets` | (보호자) 체크인 대상 이용자 목록 | guardian |
| GET | `/guardian/clients/{clientId}/billing` | (보호자) 연결 이용자 청구·명세 이력 | guardian, client_user |

**POST `/attendance/check-in`**

```json
{ "clientId": "uuid", "checkInMethod": "manual" }
```

**POST `/attendance/qr/scan`** (B방식 — 지점 QR 토큰 + 대상 선택)

```json
{ "qrToken": "지점·날짜·유효시간 서명 토큰", "clientId": "uuid", "direction": "in" }
```

> QR 토큰은 **서명·만료** 포함. `clientId`는 스캔 계정에 연결된 이용자만 허용. 중복 체크인은 `422 BUSINESS_RULE`.

---

## 6. 건강 기록 (Health) — §3-4

| 메서드 | 경로 | 설명 | 권한 |
|--------|------|------|------|
| GET | `/clients/{clientId}/health` | 건강 기록 이력(그래프용 시계열) | 스코프 내 |
| POST | `/clients/{clientId}/health/vitals` | 일일 건강 체크(혈압·체온·혈당·SpO2) | caregiver 이상 |
| POST | `/clients/{clientId}/health/medications` | 투약 기록(약품·용량·시간·투약자) | caregiver 이상 |
| POST | `/clients/{clientId}/health/incidents` | 낙상·사고 이벤트 기록 | caregiver 이상 |
| POST | `/clients/{clientId}/health/notes` | 특이사항 메모 | caregiver 이상 |

**POST `.../health/vitals`**

```json
{
  "recordedAt": "2026-06-05T09:30:00+09:00",
  "systolic": 130, "diastolic": 80,
  "temperature": 36.5, "bloodGlucose": 110, "spo2": 97
}
```

---

## 7. 청구·정산 (Billing) — §3-9 (B방식 수가표 + 이용자별 본인부담)

### 7-1. 수가표 (`fee_schedules`) — §3-9-1, `hq_admin`

| 메서드 | 경로 | 설명 |
|--------|------|------|
| GET | `/billing/fee-schedules` | 수가표 목록(연도별·등급별) |
| POST | `/billing/fee-schedules` | 수가 등록(연도·등급·1일 수가·부가항목) |
| PATCH | `/billing/fee-schedules/{id}` | 수가 수정(이력 보존) |

```json
// POST 예시
{ "year": 2026, "ltcGrade": 3, "dailyRate": 68000, "extras": { "meal": 0 } }
```

### 7-1-b. 가산율 catalog (`fee_surcharge_rates`) — G11, BNK-53 @ `904072b`

| 메서드 | 경로 | 설명 | 역할 |
|--------|------|------|------|
| GET | `/billing/fee-surcharge-rates` | MOHW 2026 가산율 4종 catalog (야간20·심야30·휴일30·유급휴일50%) | `hq_admin`, `branch_admin`, `social_worker` |
| POST | `/billing/fee-surcharge-preview` | 제공 시간 기준 가산율 1종 preview (중복불가 정책) | `hq_admin`, `branch_admin`, `social_worker` |

**GET `/billing/fee-surcharge-rates` 응답** (요약):

```json
{
  "rates": [
    { "code": "NIGHT", "label": "야간", "percent": 20, "timeRange": "18:00~22:00" },
    { "code": "LATE_NIGHT", "label": "심야", "percent": 30, "timeRange": "22:00~06:00" },
    { "code": "WEEKEND_HOLIDAY", "label": "휴일", "percent": 30 },
    { "code": "PAID_HOLIDAY", "label": "유급휴일", "percent": 50 }
  ],
  "noStackingNote": "야간·심야·휴일 가산은 중복 적용하지 않습니다. 제공 시간 기준으로 가장 높은 가산율 1종만 적용합니다.",
  "v1Notice": "v1에서는 catalog·가이드만 제공하며, 청구 자동 가산 적용은 v2에서 도입합니다."
}
```

**POST `/billing/fee-surcharge-preview`** — `{ "serviceStartAt": "ISO8601", "serviceEndAt": "ISO8601" }` → 적용 가산율 1종 + base/preview 금액. **v2 ✅**: `POST /billing/claims/generate` 시 자동 반영 @ `d7475fd` (BNK-56·58).

### 출석 transportMode (v1.3-C G15 — BNK-58)

| Method | Path | 설명 | RBAC |
|--------|------|------|------|
| GET | `/attendance` | `?transportMode=all\|boarding\|on_site` — `usesTransport` 프로필 기반 필터 | branch roles |

**`transportMode` 값**: `all`(기본) · `boarding`(케어포 2-2 탑승) · `on_site`(케어포 2-3 현장). FE Route: `/attendance/boarding` · `/attendance/on-site` @ `6c4c151`.

### 이동서비스 계약 서명 (v1.3-C G15 — BNK-58)

| Method | Path | 설명 | RBAC |
|--------|------|------|------|
| POST | `/transport/contracts/{clientId}/signature` | 수급자/기관 서명 영속화 · V64 | `hq_admin`, `branch_admin` |

**상태**: backend @ `3c8f9fe` · FE `TransportCompliancePanel` wiring @ `9e3cab5` **PRESENT**.

### 7-2. 본인부담 비율표 (`copay_rates`) — §3-9-2, `hq_admin`

| 메서드 | 경로 | 설명 |
|--------|------|------|
| GET | `/billing/copay-rates` | 본인부담 구분별 비율 |
| PATCH | `/billing/copay-rates/{copayType}` | 구분별 비율 수정(개정 대응) |

```json
// 예시 (비율은 개정 시 수정 가능)
[
  { "copayType": "GENERAL",    "rate": 0.15 },
  { "copayType": "REDUCED_40", "rate": 0.09 },
  { "copayType": "REDUCED_60", "rate": 0.06 },
  { "copayType": "MEDICAID",   "rate": 0.0  }
]
```

### 7-3. 청구서·명세서 (`billing`)

| 메서드 | 경로 | 설명 |
|--------|------|------|
| POST | `/billing/claims/generate` | 월별 청구 자동 계산·생성(지점·월 기준) |
| GET | `/billing/claims` | 청구 내역 목록 — `?branchId=&status=DRAFT\|CONFIRMED\|PAID` (V31·V149 인덱스) |
| GET | `/billing/claims/{id}` | 청구서 상세(이용자별 명세) |
| PATCH | `/billing/claims/{id}/status` | 상태 변경(작성중→확정→수납완료) — 확정 후 금액 불변(V8) |
| POST | `/billing/claims/{id}/notify` | 보호자 명세·청구 **알림 요청** (staff-initiated, G2-n) — `notifyBilling` consent 확인 | `branch_admin`, `hq_admin` |
| GET | `/billing/claims/{id}/statement.pdf` | 급여비용 명세서 출력(PDF) |
| POST | `/billing/imports/nhis` | 공단 청구내역상세 **엑셀 import** (multipart) |

**POST `/billing/claims/{id}/notify`** (BNK-28 @ `84f3441`, **email skeleton** @ `fbedcc3`/`6eba2ef`): 청구서 확정 후 보호자에게 명세 안내 알림을 **요청**한다. `guardian_notification_preferences.notify_billing` 동의 필수. `StubEmailProvider`로 email 채널 **skeleton dispatch** — **SMTP/메일벤더 실연동 v2 잔여**. frontend billing 상세 **「보호자 알림」** UI @ `c48fb67`.

**GET `/billing/claims` 쿼리**

- `branchId` (optional): 토큰 스코프 내 지점 필터
- `status` (optional): `DRAFT` | `CONFIRMED` | `PAID` — US-G07, `idx_billing_claims_org_branch_status_generated`(V31)·`idx_billing_claims_org_branch_month_status_generated`(V149, 월+상태 복합)

**POST `/billing/claims/generate`**

```json
{ "branchId": "uuid", "yearMonth": "2026-05" }
```

> **계산 규칙**: 이용자별 `총 급여비용 = 등급 수가(7-1) × 출석일수`, `본인부담금 = 총액 × 이용자 copayType 비율(7-2)`, `공단부담 = 총액 − 본인부담금`. 과거 청구는 당시 수가·비율 버전 유지.

### 7-4. NHIS Import Reconciliation — §3-9-4, US-G04/G06

케어포 4단계(공단 엑셀 업로드 → 행별 대조) 벤치마크. 행 매칭 상태는 `MATCHED` | `DISCREPANCY` | `UNMATCHED` | **`PENDING_REVIEW`**(대기/보류, V54 @ `4cc328d`, BNK-17).

| 메서드 | 경로 | 설명 |
|--------|------|------|
| POST | `/billing/imports/nhis` | 엑셀 업로드 — `branchId`, `yearMonth`, `claimId`(optional), `file` (multipart) |
| GET | `/billing/imports/nhis` | 배치 목록 — `?branchId=&yearMonth=&claimId=` |
| GET | `/billing/imports/nhis/{batchId}` | 배치 상세 + reconciliation 행 목록 |
| GET | `/billing/imports/nhis/{batchId}/candidates` | `UNMATCHED` 행 수동 매칭 후보 이용자 검색 — `?q=&page=&size=` |
| PATCH | `/billing/imports/nhis/rows/{rowId}/match` | 수동 매칭 — `{ "clientId": "uuid" }` → `MATCHED`/`DISCREPANCY` 전이 |
| GET | `/billing/imports/nhis/guidance` | import 온보딩 안내(롱텀 2026 **Chrome/Edge 필수**, export 절차) — `hq_admin`, `branch_admin` |

**POST `/billing/imports/nhis`** (multipart/form-data)

| 필드 | 필수 | 설명 |
|------|------|------|
| `branchId` | ✅ | 지점 단위 import (V21 지점 일치) |
| `yearMonth` | ✅ | `YYYY-MM` — 연결 청구와 동일 월(V17) |
| `claimId` | — | reconciliation 대상 청구(선택, 업로드 후 연결 가능) |
| `file` | ✅ | 공단 「청구내역상세」엑셀 |

**엑셀 파서 정규화** (3차 벤치마크 — 케어포 [44438](https://www.carefor.co.kr/cs/view_notice.php?calmgno=44438))

- 첫 열이 **`처리상태`**(또는 공단 변형 헤더)이면 **자동 스킵** 후 표준 컬럼 매핑
- 헤더명 공백·대소문자 **정규화** — 알 수 없는 선행 열은 무시(파일럿 샘플로 화이트리스트 확장, PLAN_NOTES #27)
- 파싱 실패 시 배치 `FAILED` + 사용자 메시지(내부 스택 미노출)

**배치 상태**: `PENDING` → `PROCESSING` → `COMPLETED` | `FAILED`. `COMPLETED` 시 `imported_at` 필수(V19/V32).

**행 매칭 규칙**

- 자동 매칭 키: `ltc_cert_no`(인정번호) + 이름·생년월일
- `MATCHED`/`DISCREPANCY`: `client_id` **필수** (`chk_nhis_import_rows_match_requires_client`, V19)
- `UNMATCHED`만 `client_id` NULL 허용
- **`PENDING_REVIEW`**: 자동 매칭 보류·운영자 검토 대기 — `match_status_reason`에 안내 문구(V54). 케어포 **「대기」** 3상태 패리티(BNK-15·17)
- 수동 매칭: `client_id` + 상태 전이 **단일 트랜잭션** (부분 업데이트 금지)
- 매칭 이용자 `branch_id` = 배치 `branch_id` (V21 `trg_nhis_rows_client_branch`)

**PATCH `/billing/imports/nhis/rows/{rowId}/match`**

```json
{ "clientId": "uuid" }
```

> UI 안내: 「공단 [longtermcare.or.kr](https://www.longtermcare.or.kr/)에서 청구 전송 후 청구내역상세 엑셀을 다운로드하세요」— 공단 직접 전송 API는 MVP 제외.  
> **롱텀 2026**: IE 접속 불가 — 엑셀 export 전 **Chrome/Edge** 사용 안내(온보딩·import 화면).

### 7-5. 본인부담/의료비공제 통계 리포트 (G26 7-8) — US-L07, BNK-263~268 @ `903f462`/`6d10e0d`/`3481eb8`

케어포 PDF p.92 7-8 dual-function 통계. FE `/billing/reports/statistics` @ `d8f1fdf`.

| 메서드 | 경로 | 설명 | 권한 |
|--------|------|------|------|
| GET | `/billing/reports/medical-expense-deduction-statistics` | **① 의료비공제 통계** — `?branchId=&yearMonth=` (지점·월별 집계) | `branch_admin`, `hq_admin` |
| GET | `/billing/reports/copay-monthly-statistics` | **② 본인부담 월별 통계** — `?branchId=&yearMonth=` · 6필드(청구건수·전월대비증감·청구총액·증감·입금총액·미수금) PDF p.92 verbatim | `branch_admin`, `hq_admin` |

**GET `/billing/reports/copay-monthly-statistics` 응답 필드** (케어포 PDF p.92 7-8 1:1):

| 필드 | 설명 |
|------|------|
| `claimCount` | 청구건수 |
| `claimCountChangeFromPriorMonth` | 전월대비증감 |
| `claimTotalAmount` | 청구총액 |
| `claimTotalAmountChange` | 증감(원) |
| `depositTotalAmount` | 입금총액 |
| `outstandingTotalAmount` | 미수금총액 |

> CMS·간편결제 제외 규칙은 G26 7-2-1(US-L04)과 동일. **이동서비스비 통계 leaf**는 별도 P1 검토(BNK-268).

---

## 8. 대시보드 (Dashboard) — §3-11

| 메서드 | 경로 | 설명 | 권한 |
|--------|------|------|------|
| GET | `/dashboard/branch` | 지점 대시보드(오늘 출석·이용자 통계·건강 이상 알림·NHIS 미매칭) | branch_admin 이하 |

**`GET /dashboard/branch` 응답 (v1.2.1 — BNK-19·33·35)**:

| 필드 | 타입 | 설명 | 상태 |
|------|------|------|------|
| `nhisUnmatchedCount` | integer | NHIS 미매칭 건수 | ✅ @ `6d0a03a` |
| `pendingReviewCount` | integer | NHIS **대기(보류)** 건수 (`PENDING_REVIEW`) | ✅ @ `1794e1c` (US-M02-b) |
| `overdueCount` | integer | 본인부담 **미납** 건수 | ✅ @ `f755428` (US-M02-c) |
| GET | `/dashboard/hq` | 통합 대시보드(전 지점 비교·집계) | hq_admin |
| GET | `/dashboard/hq/alerts` | 전 지점 건강 이상 통합 목록 | hq_admin |

`?date=2026-06-05&from=2026-05-01&to=2026-05-31&branchId=<uuid>`

---

## 9. 시스템 설정 (Settings) — `sysadmin`

| 메서드 | 경로 | 설명 |
|--------|------|------|
| GET | `/settings/system` | 자기 Tenant 기술 설정 조회 |
| PATCH | `/settings/system` | 기술 설정 변경 |
| GET | `/settings/audit-logs` | 감사 로그 조회(전 지점, 자기 Tenant) |
| GET | `/settings/backups` | 백업 상태·이력 |

---

## 10. 요양급여 제공기록 (Care Services) — L02 · §3-7

> **상태**: backend **`c655743`** — V130–V141 제공기록 4종 테이블·6 API endpoint **✅ PRESENT**. frontend **`3549896`/`9ad8346`** — `/care/weekly-service-records`·`/care/bathing-schedules`·`/care/meal-assistance-records`·`/care/service-special-notes` ✅ **완전 구현**. L02_M04/M05 **케어 리포트** — backend `c655743` ✅ · **FE P2 dirty tree**. REQUIREMENTS §3-7·USER_STORIES US-O01.

### 10-1. 요양급여 제공기록 (Weekly Service Records) — L02_M01

> **DB**: Flyway **V130–V132** `weekly_service_records`·`weekly_service_record_details` · 주간 일차별 서비스 유형·시간·비고.

| 메서드 | 경로 | 설명 | 권한 |
|--------|------|------|------|
| GET | `/api/v1/care/weekly-service-records` | 수급자별 주간 제공기록 목록 (`clientId`, `weekStartDate` query) | hq_admin, branch_admin, social_worker, caregiver |
| POST | `/api/v1/care/weekly-service-records` | 주간 제공기록 생성·저장 | branch_admin, social_worker, caregiver |
| PATCH | `/api/v1/care/weekly-service-records/{recordId}` | 주간 기록 수정 | branch_admin, social_worker, caregiver |
| DELETE | `/api/v1/care/weekly-service-records/{recordId}` | 주간 기록 삭제 | branch_admin, social_worker |

**POST 요청 (CreateWeeklyServiceRecordRequest)**:

```json
{
  "clientId": "uuid",
  "weekStartDate": "2026-06-08",
  "details": [
    {
      "dayOfWeek": 1,
      "serviceType": "PERSONAL_HYGIENE",
      "startTime": "09:00",
      "endTime": "10:30",
      "minutes": 90,
      "notes": "목욕 도움"
    }
  ]
}
```

**응답 (WeeklyServiceRecordResponse)**:

```json
{
  "id": "uuid",
  "clientId": "uuid",
  "weekStartDate": "2026-06-08",
  "weekEndDate": "2026-06-14",
  "details": [],
  "recordedAt": "2026-06-08T10:00:00+09:00",
  "recordedBy": { "userId": "uuid", "displayName": "김요양" }
}
```

### 10-2. 목욕 일정·제공현황 (Bathing Schedules & Service Records) — L02_M03

> **DB**: Flyway **V133** `bathing_schedules`·`bathing_service_records` · 월간 목욕 일정 + 실제 서비스 제공 기록.

| 메서드 | 경로 | 설명 | 권한 |
|--------|------|------|------|
| GET | `/api/v1/care/bathing-schedules` | 지점 목욕 일정 월간 조회 (`yearMonth` query) | hq_admin, branch_admin, social_worker, caregiver |
| POST | `/api/v1/care/bathing-schedules` | 월간 목욕 일정 등록·수정 (bulk upsert) | branch_admin, social_worker |
| GET | `/api/v1/care/bathing-schedules/{clientId}/monthly` | 수급자별 월간 목욕 일정·서비스 현황 | hq_admin, branch_admin, social_worker, caregiver |
| POST | `/api/v1/care/bathing-service-records` | 목욕 서비스 제공 기록 | branch_admin, social_worker, caregiver |

**POST 요청 (CreateBathingScheduleRequest, bulk)**:

```json
{
  "yearMonth": "2026-06",
  "schedules": [
    {
      "clientId": "uuid",
      "scheduledDate": "2026-06-10",
      "plannedMinutes": 30,
      "notes": "월요일 오후"
    }
  ]
}
```

### 10-3. 통합 식사도움 기록 (Meal Assistance Records) — L02_M13

> **DB**: Flyway **V134–V135** `meal_assistance_records`·지원 유형(전체·부분·감시) · 식이제한 · 불편 사항.

| 메서드 | 경로 | 설명 | 권한 |
|--------|------|------|------|
| GET | `/api/v1/care/meal-assistance-records` | 수급자별 식사도움 기록 (`clientId`, `from`, `to` query) | hq_admin, branch_admin, social_worker, caregiver |
| POST | `/api/v1/care/meal-assistance-records` | 식사도움 기록 등록 | branch_admin, social_worker, caregiver |
| PATCH | `/api/v1/care/meal-assistance-records/{recordId}` | 식사도움 기록 수정 | branch_admin, social_worker, caregiver |

**POST 요청**:

```json
{
  "clientId": "uuid",
  "recordedDate": "2026-06-10",
  "assistanceType": "FULL_ASSISTANCE",
  "dietaryRestrictions": "저염식",
  "notes": "쉽게 씹히는 음식 선호"
}
```

### 10-4. 집중배설관찰 (Intensive Excretion Observations) — L02_M02

> **DB**: Flyway **V136** `intensive_excretion_observations` · 배뇨·배변 상태·양 · 비정상 증상.

| 메서드 | 경로 | 설명 | 권한 |
|--------|------|------|------|
| GET | `/api/v1/care/intensive-excretion` | 수급자별 관찰 기록 목록 | hq_admin, branch_admin, social_worker, caregiver |
| POST | `/api/v1/care/intensive-excretion` | 배설 관찰 기록 | branch_admin, social_worker, caregiver |
| PATCH | `/api/v1/care/intensive-excretion/{recordId}` | 관찰 기록 수정 | branch_admin, social_worker, caregiver |

**POST 요청**:

```json
{
  "clientId": "uuid",
  "observedDate": "2026-06-10",
  "urineStatus": "NORMAL",
  "urineVolume": "적정",
  "fecesStatus": "NORMAL",
  "abnormalSymptoms": "특이사항 없음"
}
```

### 10-5. 신체제재 기록 (Body Restraint Records) — L02_M07

> **DB**: Flyway **V137** `body_restraint_records` · 제재 방법·시간·사유·감시 내용.

| 메서드 | 경로 | 설명 | 권한 |
|--------|------|------|------|
| GET | `/api/v1/care/body-restraint` | 수급자별 신체제재 기록 | hq_admin, branch_admin, social_worker, caregiver |
| POST | `/api/v1/care/body-restraint` | 신체제재 기록 | branch_admin, social_worker, caregiver |
| PATCH | `/api/v1/care/body-restraint/{recordId}` | 신체제재 기록 수정 | branch_admin, social_worker, caregiver |

**POST 요청**:

```json
{
  "clientId": "uuid",
  "recordedDate": "2026-06-10",
  "restraintMethod": "벨트 보안",
  "startTime": "14:00",
  "endTime": "15:00",
  "reason": "안전 위험 회피",
  "monitoringNotes": "분 5분 확인"
}
```

### 10-6. 요양급여 특이사항 (Service Special Notes) — L02_M15

> **DB**: Flyway **V138–V141** `service_special_notes` · 일일 특이사항·사건·수정/취소 기록.

| 메서드 | 경로 | 설명 | 권한 |
|--------|------|------|------|
| GET | `/api/v1/care/service-special-notes` | 수급자별 특이사항 기록 (`clientId`, `from`, `to`) | hq_admin, branch_admin, social_worker, caregiver |
| POST | `/api/v1/care/service-special-notes` | 특이사항 기록 | branch_admin, social_worker, caregiver |
| PATCH | `/api/v1/care/service-special-notes/{noteId}` | 특이사항 수정 (수정 이력 자동 기록) | branch_admin, social_worker, caregiver |

**POST 요청**:

```json
{
  "clientId": "uuid",
  "recordedDate": "2026-06-10",
  "noteType": "INCIDENT",
  "content": "오후 2시 경 넘어짐. 의사 진단 결과 이상 무.",
  "severity": "LOW"
}
```

### 10-7. 케어 리포트 (Care Reports) — L02_M04·M05

> **상태**: backend **`c655743`** — 2 엔드포인트 ✅ · **`GET /care/reports/care-meal-excretion`** · **`GET /care/reports/bath-help`**. frontend **P2 dirty tree** — `/care/reports/meal-excretion`·`/care/reports/bath-help` FE UI 미구현.

| 메서드 | 경로 | 설명 | 권한 |
|--------|------|------|------|
| GET | `/api/v1/care/reports/care-meal-excretion` | L02_M04 — 요양·식사·배설 월간 통합 리포트 (`branchId?`, `yearMonth`, `clientId?` query) | hq_admin, branch_admin, social_worker |
| GET | `/api/v1/care/reports/bath-help` | L02_M05 — 목욕도움 월간 리포트 (`branchId?`, `yearMonth`, `clientId?`) | hq_admin, branch_admin, social_worker |

**응답** (L02_M04 `CareReportResponse`):

```json
{
  "reportType": "CARE_MEAL_EXCRETION",
  "yearMonth": "2026-06",
  "generatedAt": "2026-06-30T18:00:00+09:00",
  "items": [
    {
      "clientId": "uuid",
      "clientName": "홍길동",
      "totalCareMinutes": 450,
      "mealAssistanceDays": 28,
      "excretionObservationDays": 20,
      "notes": "월간 통계"
    }
  ]
}
```

---

## 11. 보호자 알림 수신 설정 (Guardian Notification Preferences) — v2

> **상태**: develop `feac558` 반영 (QA-B08 Fixed) — V41 `guardian_notification_preferences`·`NotificationPreferenceService`·`GuardianNotificationPreferenceController`·`StaffGuardianNotificationPreferenceController` 커밋. v1.1 무료 채널(인앱·FCM·이메일) 골격과 연계, **카카오톡 알림톡·SMS는 v2 발송 API**에서 사용.

### 11-1. 데이터 모델 (V41)

| 필드 | 타입 | 설명 |
|------|------|------|
| `id` | UUID | PK |
| `guardian_id` | UUID | FK → `guardians` |
| `organization_id` | UUID | 테넌트 격리 |
| `channel_in_app` | boolean | 인앱 알림 (기본 true) |
| `channel_push` | boolean | FCM Web Push |
| `channel_email` | boolean | 이메일 |
| `channel_kakao` | boolean | 카카오톡 알림톡 (v2) |
| `channel_sms` | boolean | SMS fallback (v2) |
| `notify_attendance` | boolean | 출석(도착/귀가) |
| `notify_daily_care` | boolean | 일일 케어 리포트 |
| `notify_billing` | boolean | 명세·청구 |
| `notify_emergency` | boolean | 긴급 알림 |
| `updated_at` | timestamptz | 최종 수정 |

- 보호자 1명당 Organization 스코프 **1행** (UNIQUE `guardian_id` + `organization_id`).
- PII(이메일·전화)는 `guardians` 테이블 참조 — preferences에는 채널 on/off만 저장.

### 11-2. API

| 메서드 | 경로 | 설명 | 권한 |
|--------|------|------|------|
| GET | `/guardian/notification-preferences` | 연결 보호자 본인 수신 설정 조회 | `guardian` |
| PUT | `/guardian/notification-preferences` | 본인 수신 설정 일괄 갱신 | `guardian` |
| GET | `/clients/{clientId}/guardians/{guardianId}/notification-preferences` | 직원이 특정 보호자 설정 조회 | `branch_admin`, `social_worker` |
| PUT | `/clients/{clientId}/guardians/{guardianId}/notification-preferences` | 직원이 보호자 대리 설정(온보딩) | `branch_admin`, `social_worker` |

**PUT 요청 본문**

```json
{
  "channelInApp": true,
  "channelPush": true,
  "channelEmail": false,
  "channelKakao": true,
  "channelSms": false,
  "notifyAttendance": true,
  "notifyDailyCare": true,
  "notifyBilling": true,
  "notifyEmergency": true
}
```

**응답**: 동일 스키마 + `guardianId`·`updatedAt`.

### 11-3. 검증·보안

- `guardian` 역할은 JWT의 `guardian_id`와 경로/본문의 보호자 ID **일치** 필수.
- 직원 API는 `clientId`↔`guardianId` **`guardian_clients` 연결** 및 지점 스코프 검증.
- 알림톡·SMS 채널 on 시 **수신 동의**(`consent_at`) 기록 — PLAN_NOTES #33 채널 결정 대기 시 가정 스키마.

### 11-4. 테스트

- `GuardianNotificationPreferenceControllerTest` — 4 @Test (조회·갱신·RBAC·테넌트 격리).
- `StaffGuardianNotificationPreferenceControllerTest` — 4 @Test (직원 조회·갱신·RBAC).
- `MustApiEndpointRoutingTest` §notification — 2 @Test (guardian/staff 라우팅).
- `RoleBasedControllerAccessTest` — 4 @Test (guardian/staff RBAC).
- develop HEAD `feac558` **PRESENT** — B08 Fixed.

### 11-5. 알림 이력 조회 (Notification History) — v2 follow-up

> **상태**: develop **`c53dd3b`** 반영 (TSR 72) — `GuardianNotificationHistoryController`·`StaffClientNotificationHistoryController`·`NotificationHistoryService`·`NotificationHistoryServiceTest`·`MustApiEndpointRoutingTest` 알림 이력 RBAC. **프론트 UI 연동 잔여**.

| 메서드 | 경로 | 설명 | 권한 |
|--------|------|------|------|
| GET | `/guardian/notifications` | 연결 보호자 본인 알림톡/SMS 발송 이력 (페이지네이션) | `guardian` |
| GET | `/clients/{clientId}/notifications` | 이용자 연결 보호자 대상 발송 이력 (페이지네이션) | `branch_admin`, `social_worker` |

**쿼리 파라미터**: `page`(기본 0), `size`(기본 20).

**응답** (`NotificationHistoryPageResponse`):

```json
{
  "items": [
    {
      "id": "uuid",
      "channel": "KAKAO_ALIMTALK",
      "templateCode": "DAILY_CARE",
      "eventType": "DAILY_CARE",
      "status": "SENT",
      "sentAt": "2026-06-08T10:00:00+09:00",
      "createdAt": "2026-06-08T10:00:00+09:00"
    }
  ],
  "page": 0,
  "size": 20,
  "totalElements": 1,
  "totalPages": 1
}
```

### 11-6. 검증·보안 (이력)

- `guardian` 역할은 JWT `guardian_id` 기준 **본인 수신 이력만** 조회.
- 직원 API는 `clientId` 지점 스코프·`guardian_clients` 연결 검증.
- PII(전화번호)는 응답에 **미포함** — `notifications` 테이블 메타만 반환.

### 11-7. 테스트 (이력)

- `NotificationHistoryServiceTest` — guardian·staff·RBAC·테넌트 격리.
- `MustApiEndpointRoutingTest` — 알림 이력 라우팅·RBAC.
- develop HEAD `c53dd3b` **PRESENT** — TSR 72 Fixed.

### 11-8. 본인부담 입금 확인 알림 (Billing Payment Received) — v2 follow-up

> **상태**: develop **`52e0621`** 반영 (TSR 82) — copay claim 상태 **CONFIRMED→PAID** 전환 시 `NotificationEventType.BILLING_PAYMENT_RECEIVED` dispatch. `notifyBilling` consent 재사용. **live Solapi·프론트 UI 잔여**.

| 항목 | 값 |
|------|-----|
| 이벤트 | `BILLING_PAYMENT_RECEIVED` |
| 템플릿 코드 | `BILLING_PAYMENT_RECEIVED` (`KAKAO_TPL_BILLING_PAYMENT` env) |
| 트리거 | `BillingService` copay claim PAID 마킹 |
| 수신 동의 | `guardian_notification_preferences.notify_billing` |
| SMS fallback | `AlimtalkFallbackText` — 결제 수신 한국어 본문 |

**페이로드 (알림톡 variables, 요약)**:

```json
{
  "claimId": "uuid",
  "clientId": "uuid",
  "yearMonth": "2026-06",
  "copayAmount": "45000.00",
  "event": "BILLING_PAYMENT_RECEIVED"
}
```

### 11-9. 테스트 (copay PAID)

- `BillingServiceTest` — PAID 전환 시 dispatch 호출 검증.
- `J03AlimtalkServiceFlowE2eTest` — `BILLING_PAYMENT_RECEIVED` template·event 정합.
- `AlimtalkFallbackTextTest`·`AlimtalkTemplateVariablesTest` — 결제 수신 fallback·variables.
- develop HEAD `52e0621` **PRESENT** — TSR 82 Fixed.

### 11-10. 알림 채널 readiness (US-J03 / J03-readiness) — v2 partial+

> **상태**: backend **`d4acab7`/`fffd355`** — `NotificationChannelReadinessService`·`GET /api/v1/notifications/channel-status`. frontend **`6b1258c`/`d695923`** — `NotificationChannelReadinessPanel`(`DashboardPage`·`OrganizationSettingsPage`) · REQUIREMENTS J03-readiness · USER_STORIES US-J03 · **잔여 P2**: live Solapi E2E·quiet-hours dispatch BE enforce.

| 메서드 | 경로 | 설명 | 권한 |
|--------|------|------|------|
| GET | `/api/v1/notifications/channel-status` | Solapi·SMTP·알림톡 템플릿·live dispatch readiness·quiet-hours | `hq_admin`, `branch_admin` |

**응답 필드 (요약, 시크릿 비노출)**:

| 필드 | 의미 |
|------|------|
| `solapiApiKeyConfigured` / `solapiApiSecretConfigured` / `solapiSenderNumberConfigured` / `kakaoChannelIdConfigured` | Solapi 4항 configured boolean |
| `smtpHostConfigured` / `liveEmailDispatchReady` | SMTP 호스트·이메일 live 발송 준비 |
| `liveAlimtalkDispatchReady` | 9 필수 알림톡 템플릿 + Solapi 게이트 종합 |
| `quietHoursActive` | **22:00~08:00 Asia/Seoul** 조용한 시간대 (readiness 표시; dispatch BE enforce **P2**) |
| `requiredAlimtalkTemplates[]` | 9 템플릿(출석 입/퇴·일일케어·청구명세·입금·급여제공·가정통신문·학대예방·긴급) — code·configured |

**semantics**:

- 케어포 func **`10-7.안내발송내역(문자, 이메일)`** — 발송 **이력** 중심(ogada `NotificationHistoryPanel` ✅) · readiness 게이트 **ogada 차별화**
- `isQuietHoursActive()`: `!now.isBefore(22:00) || now.isBefore(08:00)` (Asia/Seoul) @ `fffd355`
- FE `fetchNotificationChannelStatusApi` · **`NotificationChannelReadinessPanel`** — configured boolean only(키·시크릿 미노출)

---

## 12. 배차·이동경로 (Transport) — v1.3-A implemented

> **상태**: backend **`5994d15`** — V47·`/api/v1/transport/*`·geocode proxy·**unconfirm PATCH+POST alias**·**non-HQ pickup address·contact masking**·**★ G15 service-log GET+PUT** @ `0cfa970`/`aaaeb10` · **★ G15 service-log audit trail read** @ `5994d15` · **★ monthly reports read** @ `5d27ad3`. frontend transport UI @ `6a18dfd` — **`TransportUnconfirmModal`**·**`ClientFormPage` 픽업 프로필**·**`TransportPickupContact`**·**`TransportServiceLogPanel` 편집**·**`TransportMonthlyReportsPage`** **PRESENT**. REQUIREMENTS §3-13·USER_STORIES US-T01~T05.

| 메서드 | 경로 | 설명 | 권한 |
|--------|------|------|------|
| GET | `/transport/roster` | 당일 픽업 명단 (`runDate`, `direction=PICKUP`) | `hq_admin`, `branch_admin`, `social_worker`, `caregiver` |
| GET | `/transport/runs` | 운행 목록 (`runDate`, `direction`) | `hq_admin`(전체), 직원(`CONFIRMED`만) |
| POST | `/transport/runs` | DRAFT run 생성 (≤15 stops) | `hq_admin` |
| GET | `/transport/runs/{id}` | run 상세·stops | `hq_admin` / 직원(`CONFIRMED`만) |
| PATCH | `/transport/runs/{id}` | DRAFT stops 순서·인원 수정 | `hq_admin` |
| POST | `/transport/runs/{id}/confirm` | DRAFT→CONFIRMED 확정 | `hq_admin` |
| PATCH | `/transport/runs/{id}/unconfirm` | CONFIRMED→DRAFT (재편집 허용) | `hq_admin` |
| POST | `/transport/runs/{id}/unconfirm` | 위와 동일 (**레거시 alias**) | `hq_admin` |
| POST | `/transport/geocode` | 주소→좌표 프록시 (Kakao Local, 서버 캐시) | `hq_admin` |
| GET | `/transport/runs/{runId}/service-log` | **별지 제22호 이동서비스일지** export (CONFIRMED run) | `hq_admin`, `branch_admin`, `social_worker`, `caregiver` |
| PUT | `/transport/runs/{runId}/service-log` | **별지 제22호 일지④** 입력·저장 (upsert) | `hq_admin`, `branch_admin`, `social_worker`, `caregiver` |
| GET | `/transport/runs/{runId}/service-log/audit-trail` | **일지④ 감사 trail** read-only (수정 이력) | `hq_admin`, `branch_admin`, `social_worker` |
| GET | `/transport/reports/monthly-service-variation` | **케어포 2-7** 월간 서비스 변동현황 (`yearMonth=YYYY-MM`) | `hq_admin`, `branch_admin`, `social_worker` |
| GET | `/transport/reports/monthly-resident-status` | **케어포 2-8** 월간 입소자/일정/서비스 현황 (`yearMonth=YYYY-MM`) | `hq_admin`, `branch_admin`, `social_worker` |

**G15 service-log (157차 @ `0cfa970`/`aaaeb10`/`7a4b310`, BNK-300~302)**: CONFIRMED run에 대해 GET은 run/stop·시간 준수 데이터를 **별지 제22호** 형식으로 반환(인쇄/export). PUT은 일지④ 필드(운행·탑승·시간 등)를 **upsert** — FE `TransportServiceLogPanel`·`upsertTransportServiceLogApi`·`TransportTimeCompliance` 15분 tolerance. **잔여 P2**: 인쇄·보관 UX·**FE audit UI**.
- `GET /transport/runs/{runId}/service-log` 응답은 기관 정보(센터 주소·지역 경로·대표 연락처), 차량/기사·동승자, 운전자 서명 여부, 정차별 시간 준수 요약을 포함한다 — 별지 제22호 인쇄 시 그대로 노출된다.

**G15 monthly reports (158차 @ `5d27ad3`/`6a18dfd`, BNK-304~306)**: `yearMonth=YYYY-MM` query · Asia/Seoul TZ · **schema migration 0**(기존 transport roster·runs·contract 데이터 재활용). 2-7 `variationType` enum: `NEW_TRANSPORT`·`DISCHARGED`·`CONTRACT_CREATED`·`CONTRACT_UPDATED`. FE `TransportMonthlyReportsPage` route `/reports/transport-monthly` — StatCard `newTransportClients`·`dischargedTransportClients`·`contractChanges` + 변동·현황 테이블 · `apiFetch` `Promise.all`.

**G15 audit trail read (158차 @ `5994d15`, BNK-306)**: 일지④ 수정 이력 read-only API — **FE wire 미완(P2)**.

**제약**: 정차 **최대 15명** · `CONFIRMED` 후 수정 불가 · v1.3-A는 **운영 시각화 한정**(G15·G16 제외, BNK-7·BNK-8 — **★ G15 service-log는 v1.3-C closure 후보**).

**PII·마스킹 (70차 @ `e7d4cf6`/`c7941e9`, **154차 roster 컬럼 확장**)**: `GET /transport/roster`·`GET /transport/runs`·`GET /transport/runs/{id}` 응답의 `pickupAddress`·정차 주소·`pickupContact` 필드는 **`hq_admin`·`platform_admin`·`sysadmin`만 전체 노출**. `branch_admin`·`social_worker`·`caregiver` 역할에는 **마스킹**(SEC-D9·`010-****-5678` 패턴). frontend **`TransportPickupContact`** @ `1d910c2` — non-HQ 역할 tel 링크 없음·`pilotPageFlows` T03 E2E 검증.

**Roster 항목 (`GET /transport/roster` → `items[]`, 154차)** — PLAN_NOTES 결정 96:

| 필드 | 설명 | UI(명단 테이블) |
|------|------|----------------|
| `contact` | 이용자 본인 전화(`clients.phone` 복호화) | 「연락처」 |
| `guardianContact` | 대표 보호자(`primaryGuardian`) 전화 | 「보호자 연락처」 |
| `pickupContact` | 픽업 연락처(미입력 시 이용자 연락처) | **명단 미표시**(호환 유지) · 정차 `stops[]`는 계속 노출 |

`contact`·`guardianContact`도 non-HQ 역할에 **동일 `maskPhone` 규칙** 적용.

---

## 13. 식사·프로그램 (Meals·Programs) — v3 implemented

> **상태**: backend **`dfd9be2`** + **V49** — `/api/v1/meals/*`·`/programs/*` **PRESENT**. frontend **`362dbf0`**+ — `/meals`·`/programs` UI·API 클라이언트 **PRESENT**. **식단·일정 등록 API 미구현**(FAQ Q161). REQUIREMENTS §3-5·§3-6·USER_STORIES US-N01·N02.

| 메서드 | 경로 | 설명 | 권한 |
|--------|------|------|------|
| GET | `/meals/menus` | 당일 식단 (`date`) | `branch_admin`, `social_worker`, `caregiver`, `hq_admin` |
| GET | `/meals/records` | 이용자별 식사 기록 (`date`) | 동일 |
| POST | `/meals/records` | 식사량·식이 제한·영양사 소견 기록 | `branch_admin`, `social_worker`, `caregiver` |
| GET | `/programs/schedules` | 당일 프로그램 일정 | 동일 |
| GET | `/programs/participations` | 참여·만족도 기록 | 동일 |
| POST | `/programs/participations` | 참여·만족도 등록 | `branch_admin`, `social_worker`, `caregiver` |

> **가정**: 엔드포인트는 frontend `services.js` 클라이언트와 정합 — DBA·BE 구현 시 본 절 확정.

---

## 14. 방문요양 일정 (Visits) — v2/G21 implemented (backend)

> **상태**: backend **`8a8c5b3`** + frontend **`f232285`**(167차) — `/api/v1/visits/*`·PLAN/BILLING 이중 일정·체크인/아웃·**NHIS import**·**확정차단**(`hasBlockingConfirmedPlan`)·**paired cancel/sync**·**일괄확정 게이트**(`confirm-readiness`/`batch-confirm`)·**readiness PLAN/BILLING split + per-kind ready**(BNK-365 @ `f26abb0`/`5f710e3`)·**NHIS 명세 사전비교**(`nhis-comparison` + `nhisComparisonSummary` embed·G-SCHEDULE-FIX-LTM-COMPARE BE ✅ @ `03a052a`/`8a8c5b3`·BNK-366~367)·**RFID 7-code diff compare**(`imports/rfid/compare`·normalize @ `570912e`) **PRESENT** (`VisitServiceTest`·`MustApiEndpointRoutingTest`). frontend `/visits` UI **partial+** @ `f232285` — `VisitNhisImportPanel`·paired cancel UX · **`VisitBatchConfirmPanel` PLAN/BILLING split wire ✅** @ `f9ed97d` · **`VisitRfidDiffComparePanel` ✅** · **NHIS comparison summary StatCard wire 잔여 △ P2** · **US-V04/V05 live E2E 잔여**. REQUIREMENTS G21·USER_STORIES US-V01~V05.

| 메서드 | 경로 | 설명 | 권한 |
|--------|------|------|------|
| GET | `/visits` | 방문 일정 목록 (`from`, `to`, `scheduleKind`, `branchId`) | `hq_admin`, `branch_admin`, `social_worker`, `caregiver` |
| POST | `/visits` | DRAFT 일정 생성 (`createPairedBillingSchedule` 옵션) | `branch_admin`, `social_worker` |
| GET | `/visits/{visitId}` | 일정 상세 | `hq_admin`, `branch_admin`, `social_worker`, `caregiver` |
| PATCH | `/visits/{visitId}` | DRAFT 일정 수정 | `branch_admin`, `social_worker` |
| POST | `/visits/{visitId}/confirm` | DRAFT→CONFIRMED | `branch_admin`, `social_worker` |
| GET | `/visits/confirm-readiness` | 일괄확정 사전 점검 (`from`, `to`, `scheduleKind`, `branchId`) | `branch_admin`, `social_worker` |
| GET | `/visits/nhis-comparison` | 일정 수량 vs 최신 NHIS import 명세 사전 비교 (`from`, `to`, `branchId`) | `branch_admin`, `social_worker` |
| POST | `/visits/batch-confirm` | NHIS 비교·변경이력 확인 후 DRAFT 일괄확정 | `branch_admin`, `social_worker` |
| POST | `/visits/{visitId}/cancel` | 일정 취소 | `branch_admin`, `social_worker` |
| POST | `/visits/{visitId}/check-in` | 체크인 (`method`: `MOBILE` \| `MANUAL`) | `social_worker`, `caregiver` |
| POST | `/visits/{visitId}/check-out` | 체크아웃·방문 완료 | `social_worker`, `caregiver` |
| POST | `/visits/imports/nhis` | NHIS 방문일정 엑셀 import (`multipart/form-data`) | `branch_admin`, `social_worker` |
| POST | `/visits/imports/rfid/compare` | NHIS 계획일정 vs RFID 전송 엑셀 7-code diff 비교 (`multipart/form-data`) | `branch_admin`, `social_worker` |

**NHIS import (`POST /visits/imports/nhis`)**: `branchId`(UUID), `scheduleKind`(기본 `PLAN`), `createPairedBillingSchedule`(기본 `false`), `file`(엑셀). 응답 `NhisVisitScheduleImportResponse` — 생성·스킵·오류 건수. **`HOME_VISIT` 지점만** 허용 @ `ee3fa3a`. **확정 PLAN 존재 시 import 차단** @ `84f3441` — FE `VisitNhisImportPanel`·확정↔import 가이드 @ `bf3d40d`/`311c7c0`.

**`scheduleKind`**: `PLAN`(계획·안내) \| `BILLING`(청구·정산). `POST /visits` 본문에 `createPairedBillingSchedule: true` 시 PLAN 생성과 함께 **페어 BILLING** 일정 자동 생성 — `pairedScheduleId`로 연결(이지케어 계획/청구 이중 import 대응, BNK-10·14).

**생성 본문 (`CreateVisitScheduleRequest`)**: `clientId`, `assignedUserId`, `visitDate`, `plannedStartTime`, `plannedEndTime`, `serviceMinutes`(1–480), `scheduleKind`, `notes`, `createPairedBillingSchedule`.

**일괄확정 (`GET /visits/confirm-readiness` + `POST /visits/batch-confirm`)** @ `0b807d8` — 이지케어 FAQ 21782 「4.일정확정」6단 게이트 패리티:

- **`GET /visits/confirm-readiness`**: `from`·`to`(필수), `scheduleKind`(선택), `branchId`(선택). 응답 `VisitConfirmReadinessResponse` — `draftCount`, `pairedDivergedCount`, `unassignedDraftCount`, `confirmedCount`, `ready`, `blockers[]`. **PLAN/BILLING split**(BNK-365 @ `f26abb0`/`5f710e3`): `draftPlanCount`/`draftBillingCount`, `pairedDivergedPlanCount`/`...BillingCount`, `unassignedDraftPlanCount`/`...BillingCount`, `confirmedPlanCount`/`...BillingCount`, **`readyPlan`/`readyBilling`** per-kind 플래그(미배정 draft = not ready). **`nhisComparisonSummary`**(BNK-367 @ `8a8c5b3`): 동일 월 범위면 `matchedLineCount`/`discrepancyLineCount`/`missingNhisLineCount`/`extraNhisLineCount` embed(별도 `/visits/nhis-comparison` round-trip 불필요)·cross-month `null`.
- **`GET /visits/nhis-comparison`**(BNK-366~367 @ `03a052a` — G-SCHEDULE-FIX-LTM-COMPARE·이지케어 `schedule-fix` `chk-ltm-fix` parity): `from`·`to`(필수·**동일 월**), `branchId`(선택). 일정 서비스 일수를 **최신 `NhisImportBatch`+`NhisImportRow`** client별로 대조. 응답 `VisitNhisComparisonResponse` — `items[]`(`VisitNhisComparisonItemResponse`: client별 `visitDayCount`↔`nhisServiceDays`·`serviceDaysMatch`·`nhisMatchStatus`)·집계 `matchedLineCount`/`discrepancyLineCount`/`missingNhisLineCount`/`extraNhisLineCount`·`overallMatch`. 비동일 월 → `400` `NHIS_COMPARISON_SAME_MONTH_MESSAGE` 「공단 명세서 비교는 동일 월 범위에서만 가능합니다.」. **FE `VisitBatchConfirmPanel` summary StatCard wire 잔여 △ P2**(BNK-367).
- **`POST /visits/batch-confirm`**: 본문 `BatchConfirmVisitSchedulesRequest` — `fromDate`, `toDate`, `scheduleKind`(선택), `branchId`(선택), **`nhisComparisonAcknowledged`**(필수 `true`), **`changeHistoryChecked`**(필수 `true`). 응답 `BatchConfirmVisitSchedulesResponse` — `confirmedCount`, `confirmedVisitIds[]`.
- **게이트**: `nhisComparisonAcknowledged=false` → `400` 「공단 청구명세서 비교 확인 후…」 · `changeHistoryChecked=false` → `400` 「공단조회 변경이력 확인 후…」 · 페어 PLAN/BILLING 상태 불일치 → `400` · **미배정 draft**(직원 미배정) → not ready·거부 @ `5f710e3` · DRAFT 0건 → `400`.

**체크인/체크아웃 가드 (`POST /visits/{visitId}/check-in` · `check-out`)** @ `0db1e68`/`78cfb8a`:

- 배정 직원(`assignedUserId`)이 있으면 **활성·지점 소속** 여부를 검증한다. 비활성/퇴사·타 지점 배정 시 `400` — `ASSIGNED_USER_INACTIVE_MESSAGE` / `ASSIGNED_USER_BRANCH_GUARD_MESSAGE`.
- `caregiver` 역할은 **본인 배정 일정만** 체크인/아웃 가능 (`ASSIGNED_USER_CHECK_IN_GUARD_MESSAGE`). `hq_admin`·`branch_admin`·`social_worker`는 감독 역할로 우회(역할 코드는 대소문자·공백 무시).

**RFID diff compare (`POST /visits/imports/rfid/compare`)** @ `eeac205` — ezCare `schedule-rfid` 7-code matrix (BNK-346 · G21 P1):

- **요청** (`multipart/form-data`): `branchId`(UUID), `planFile`(NHIS 계획일정 엑셀), `rfidFile`(RFID 전송 엑셀).
- **응답** (`VisitRfidDiffCompareResponse`): `branchId`, `planFileName`, `rfidFileName`, `planRowCount`, `tagRowCount`, `comparedRowCount`, `diffCodeCounts`(Map), `rows[]`(`VisitRfidDiffRowResponse`).
- **diff 코드** (`COMP_01`~`COMP_09`, `COMP_02` 없음): `COMP_01` 태그없음 · `COMP_03` 종료태그없음 · `COMP_04`/`COMP_05` 시작/종료 60분 초과 · `COMP_06` 인정시간 30분 초과 · `COMP_07` 제공자불일치 · `COMP_08` 직접입력 · `COMP_09` 계획없음.
- **제약**: `HOME_VISIT` 지점만 허용. 하드웨어 RFID 실시간 연동은 범위 외(엑셀 2-file 비교).

**제약**: `HOME_CARE` 지점(`branches.service_types`)만 허용(가정). RFID 태그 실시간 연동은 **v2 후속**(이지케어 FAQ 21647 — QR/수기 우선).

---

## 9-1. 선임 요양보호사 업무수행일지 (Lead Caregiver Work Logs) — G34 / US-S01

> **상태**: backend **`559648f`** — V82 `lead_caregiver_work_logs`·`LeadCaregiverWorkLogController`·목록·생성·수정·전자서명 **PRESENT**. frontend **`LeadCaregiverWorkLogPage` ✅** @ `6d6b426` · **GET 상세·DELETE 미구현**. REQUIREMENTS §3-8-a·USER_STORIES US-S01.

| 메서드 | 경로 | 설명 | 권한 |
|--------|------|------|------|
| GET | `/staff/lead-caregiver-logs` | 활성 지점의 선임 요양보호사 업무수행일지 목록 | hq_admin, branch_admin, social_worker, caregiver |
| POST | `/staff/lead-caregiver-logs` | 일별 업무수행일지 생성 | 동일 |
| PATCH | `/staff/lead-caregiver-logs/{logId}` | 초안(DRAFT) 업무수행일지 수정 | 동일 |
| POST | `/staff/lead-caregiver-logs/{logId}/sign` | 초안 전자서명 후 잠금 (DRAFT→SIGNED) | 동일 |

**쿼리 파라미터 (GET)**: `date` (LocalDate, 선택), `clientId` (UUID, 선택)

**POST 요청**:

```json
{
  "clientId": "uuid",
  "logDate": "2026-06-12",
  "leadCaregiverUserId": "uuid",
  "workContent": "오늘의 업무 수행 내용 서술",
  "careNotes": "특이사항 (선택)"
}
```

**응답** (`LeadCaregiverWorkLogResponse`):

```json
{
  "id": "uuid",
  "clientId": "uuid",
  "clientName": "홍길동",
  "logDate": "2026-06-12",
  "leadCaregiverUserId": "uuid",
  "workContent": "업무 수행 내용",
  "careNotes": "특이사항",
  "signatureStatus": "DRAFT | SIGNED",
  "signatureMethod": "DIRECT | SMS_VERIFIED",
  "signedByUserId": "uuid (null if DRAFT)",
  "signedAt": "2026-06-12T14:30:00+09:00 (null if DRAFT)",
  "createdAt": "2026-06-12T10:00:00+09:00",
  "updatedAt": "2026-06-12T10:00:00+09:00"
}
```

**POST `/staff/lead-caregiver-logs/{logId}/sign` 요청**:

```json
{
  "signerUserId": "uuid",
  "signatureMethod": "DIRECT | SMS_VERIFIED"
}
```

---

## 9-2. 정기 욕구사정 (Needs Assessment) — US-T09 / G24 / G24b

> **상태**: backend **`6f3315a`·`b238779`·`45fb6d9`·`98002d4`·`f4c8beb`** — GET 목록·상세, PUT upsert, **GET compliance ✅** — 가정방문 일자 회계연도 범위 검증·G24b 5필드(V128)·fiscal-year compliance 집계. frontend **`ClientNeedsAssessmentForm` ✅** @ `2642838`/`5be9070`/`49fbf67` — 8항목 저장·이전 연도 비교 **PRESENT** · **`DashboardPage` compliance StatCard ✅** @ `ca0b627`/`baa6d6d`. REQUIREMENTS §3-2-1·USER_STORIES US-T09·US-H01.

| 메서드 | 경로 | 설명 | 권한 |
|--------|------|------|------|
| GET | `/clients/{clientId}/needs-assessments` | 이용자별 정기 욕구사정 목록 (회계연도 내림차순) | hq_admin, branch_admin, social_worker, caregiver |
| GET | `/clients/{clientId}/needs-assessments/{fiscalYear}` | 특정 회계연도 욕구사정 상세 | 동일 |
| PUT | `/clients/{clientId}/needs-assessments` | 회계연도별 욕구사정 생성 또는 갱신 | branch_admin, social_worker |
| GET | `/clients/needs-assessments/compliance` | **지점 활성 이용자** 연간 욕구사정 준수 집계 (G24b·등급변경 재사정 due) | hq_admin, branch_admin, social_worker |

**GET `/clients/needs-assessments/compliance` 쿼리 파라미터**:

| 파라미터 | 타입 | 필수 | 설명 |
|----------|------|------|------|
| `fiscalYear` | int | 선택 | 회계연도 (기본=KST 오늘 연도) |
| `branchId` | UUID | 선택 | 지점 스코프 (hq_admin만 지정 가능; 미지정 시 active branch) |

**응답** (`NeedsAssessmentComplianceResponse`):

```json
{
  "fiscalYear": 2026,
  "totalClients": 42,
  "compliantCount": 36,
  "gapCount": 6,
  "items": [
    {
      "clientId": "uuid",
      "clientName": "홍길동",
      "fiscalYear": 2026,
      "hasRecord": true,
      "homeVisitDate": "2026-03-15",
      "homeVisitComplete": true,
      "gradeChangeReassessmentDue": false,
      "missingG24bFields": [],
      "annualComplete": true
    }
  ]
}
```

**compliance semantics**:

- `annualComplete`: 회계연도 기록 존재 + `homeVisitDate` 존재 + `missingG24bFields` 비어 있음
- `gradeChangeReassessmentDue`: 회계연도 내 등급변경이 `recordedAt` 이후 발생 (시행령 제13조제5항)
- `missingG24bFields`: `disease`·`communication`·`nutrition`·`livingEnvironment`·`resourceUtilization` 중 미입력 키 목록

**PUT 요청** (G24 + G24b 확장 필드):

```json
{
  "fiscalYear": 2026,
  "homeVisitDate": "2026-06-12",
  "physical": "신체 기능 평가 결과",
  "cognitive": "인지 기능 평가 결과",
  "family": "가족 상황 및 지원",
  "economic": "경제적 상황",
  "social": "사회적 역할",
  "serviceNeeds": "필요 서비스",
  "homeVisitNotes": "방문 기록 및 의견",
  "satisfaction": "서비스 만족도",
  "disease": "G24b 질병상태",
  "communication": "G24b 의사소통",
  "nutrition": "G24b 영양상태",
  "livingEnvironment": "G24b 환경상태",
  "resourceUtilization": "G24b 자원이용 욕구"
}
```

**응답** (`ClientNeedsAssessmentResponse`):

```json
{
  "id": "uuid",
  "clientId": "uuid",
  "fiscalYear": 2026,
  "homeVisitDate": "2026-06-12",
  "physical": "...",
  "cognitive": "...",
  "family": "...",
  "economic": "...",
  "social": "...",
  "serviceNeeds": "...",
  "homeVisitNotes": "...",
  "satisfaction": "...",
  "disease": "...",
  "communication": "...",
  "nutrition": "...",
  "livingEnvironment": "...",
  "resourceUtilization": "...",
  "recordedAt": "2026-06-12T10:30:00+09:00"
}
```

**대시보드 FE 연동 (§9-4)**: `DashboardPage`는 `GET /clients/needs-assessments/compliance` 응답에서 `gapCount`·`gradeChangeReassessmentDue` 건수를 계산해 StatCard `needsAssessmentGapCount`·`gradeChangeReassessmentDueCount`에 표시한다 (backend `BranchDashboardResponse` 필드 아님).

---

## 9-3. 급여계약 첨부 (Benefit Contract Attachments) — US-T10 / G14

> **상태**: backend **`6f3315a`** — GET 목록·다운로드, POST 업로드, DELETE **PRESENT** — Flyway **V84/V85**. frontend **`ClientBenefitContractAttachmentPanel` ✅** @ `2642838`·`5be9070` — 파일함·업로드·미리보기·삭제 **PRESENT**. **P2**: FAQ21805 갱신·해지·전자서명 workflow. REQUIREMENTS §3-2·USER_STORIES US-T10.

| 메서드 | 경로 | 설명 | 권한 |
|--------|------|------|------|
| GET | `/clients/{clientId}/benefit-contract-attachments` | 급여계약서 파일함 목록 | hq_admin, branch_admin, social_worker, caregiver |
| POST | `/clients/{clientId}/benefit-contract-attachments` | 급여계약서 PDF·PNG 업로드 | branch_admin, social_worker |
| GET | `/clients/{clientId}/benefit-contract-attachments/{attachmentId}` | 첨부파일 인라인 미리보기·다운로드 | hq_admin, branch_admin, social_worker, caregiver |
| DELETE | `/clients/{clientId}/benefit-contract-attachments/{attachmentId}` | 첨부파일 삭제 | branch_admin, social_worker |

**POST (multipart/form-data)**:

```
Content-Type: multipart/form-data
form-data:
  file: <binary PDF or PNG, max 10MB>
```

**응답** (`ClientBenefitContractAttachmentResponse`):

```json
{
  "id": "uuid",
  "clientId": "uuid",
  "originalFilename": "contract_2026-06.pdf",
  "contentType": "application/pdf",
  "fileSizeBytes": 245632,
  "documentType": "CONTRACT",
  "uploadedAt": "2026-06-12T10:30:00+09:00"
}
```

**제약**: 파일 타입 = PDF·PNG, 크기 ≤ 10MB. PATCH(수정) **미구현** — 삭제 후 재업로드.

---

## 9-4. 대시보드 확장 필드 — G17 / G32 / G38 / G39 / G24b compliance snapshot

> **상태**: backend **`559648f`** — `BranchDashboardResponse`·`HqDashboardResponse`에 G17/G32/G38/G39 규정준수 필드 **PRESENT**. frontend dashboard StatCard·panel `ded6573`·**G24b compliance widget ✅** @ `ca0b627`/`baa6d6d` — `needsAssessmentGapCount`·`gradeChangeReassessmentDueCount`는 **FE가 `GET /clients/needs-assessments/compliance`에서 계산**. REQUIREMENTS §3-11·USER_STORIES US-M02·US-T06·US-T07·US-T08·US-H01·US-T09.

**`GET /dashboard/branch` 응답 추가 필드 (v1.2.1)**:

| 필드 | 타입 | 설명 | Epic |
|------|------|------|------|
| `functionalRecoveryProvisionGapCount` | int | 기능회복훈련 급여제공 미기록 수 | G17 |
| `functionalRecoveryBenefitStartGapCount` | int | 기능회복훈련 계획 미구성 수 | G17 |
| `functionalRecoveryPlansRecorded` | int | 기능회복훈련 계획 수립 건수 | G17 |
| `functionalRecoveryProvisionMet` | boolean | 기능회복훈련 급여제공 준수율 = 100% | G17 |
| `functionalRecoveryBenefitStartMet` | boolean | 기능회복훈련 계획 준수율 = 100% | G17 |
| `caseManagementReflectionGapCount` | int | 사례관리 회의 결과 반영 미기록 수 | G32 |
| `caseManagementEvaluationGapCount` | int | 사례관리 평가 미기록 수 | G32 |
| `caseManagementMeetingsRecorded` | int | 사례관리 회의 기록 건수 | G32 |
| `caseManagementEvaluationMet` | boolean\|null | 사례관리 평가 준수율 = 100% (null if meetings=0) | G32 |
| `carePlanFiveMonthWarningCount` | int | 급여제공계획 5개월 경고 건수 | G38 |
| `carePlanElevenMonthWarningCount` | int | 급여제공계획 11개월 경고 건수 | G38 |
| `carePlanReissueGapCount` | int | 급여제공계획 재발급 미적용 건수 | G38 |
| `provisionResultWeeklyStateChangeGapCount` | int | 급여제공결과평가 주간 상태변화 미기록 | G39 |
| `provisionResultMonthlyRecordGapCount` | int | 급여제공결과평가 월간 기록 미제공 | G39 |
| `provisionResultAnnualEvaluationGapCount` | int | 급여제공결과평가 연간 평가 미기록 | G39 |
| `provisionResultReflectionGapCount` | int | 급여제공결과평가 반영 미기록 | G39 |
| `provisionResultTotalClients` | int | 급여제공결과평가 대상 이용자 수 | G39 |
| `provisionResultWeeklyStateChangeMet` | boolean\|null | 주간 상태변화 준수율 = 100% (null if totalClients=0) | G39 |
| `provisionResultMonthlyRecordMet` | boolean\|null | 월간 기록 제공 준수율 = 100% (null if totalClients=0) | G39 |
| `provisionResultAnnualEvaluationMet` | boolean\|null | 연간 평가 준수율 = 100% (null if totalClients=0) | G39 |
| `provisionResultReflectionMet` | boolean\|null | 반영 준수율 = 100% (30일 내 반영 기준) | G39 |

**FE 전용 StatCard (G24b — backend dashboard JSON 필드 아님)**:

| StatCard 키 | 소스 API | 설명 | Epic |
|-------------|----------|------|------|
| `needsAssessmentGapCount` | `GET /clients/needs-assessments/compliance` → `gapCount` | 연간 욕구사정 미준수 이용자 수 | G24b |
| `gradeChangeReassessmentDueCount` | 동일 API → `items[].gradeChangeReassessmentDue` 집계 | 등급변경 후 재사정 필요 건수 | G24b |

**`GET /dashboard/hq` 응답**:

- **동일 필드** (21개 compliance) — 전 지점 집계 합산
- `branches[]` 내각 지점의 집계 요약도 동일 필드 포함

**semantics of `*Met` 필드**:

- `functionalRecoveryProvisionMet`: `functionalRecoveryProvisionGapCount == 0`
- `functionalRecoveryBenefitStartMet`: `functionalRecoveryBenefitStartGapCount == 0`
- `caseManagementEvaluationMet`: `caseManagementEvaluationGapCount == 0` (meetings > 0 일 때만 = true)
- `provisionResultWeeklyStateChangeMet`: `provisionResultWeeklyStateChangeGapCount == 0` (totalClients > 0 일 때만 = true, else null)
- `provisionResultMonthlyRecordMet`: `provisionResultMonthlyRecordGapCount == 0` (totalClients > 0 일 때만 = true, else null)
- `provisionResultAnnualEvaluationMet`: `provisionResultAnnualEvaluationGapCount == 0` (totalClients > 0 일 때만 = true, else null)
- `provisionResultReflectionMet`: `provisionResultReflectionGapCount == 0`

---

## 9-5. 요양보호사 보수교육 compliance (8-7-1) — G34 / US-S02

> **상태**: backend **`51477bd`**/`1817c36` — `StaffRefresherTrainingController`·compliance+certificate API **✅**. frontend **`StaffRefresherTrainingPage` ✅** @ `0a7fe16`/`46f1ac0`/`50bdb6e` — cert upload/preview/delete·pagination·UNKNOWN hire date · REQUIREMENTS G34·USER_STORIES US-S02.

| 메서드 | 경로 | 설명 | 권한 |
|--------|------|------|------|
| GET | `/staff/refresher-training/compliance` | 활성 지점 직원 보수교육(격년 2년) compliance 요약 | hq_admin, branch_admin, social_worker |
| GET | `/staff/refresher-training/users/{userId}/certificates` | 직원 이수증 목록 | hq_admin, branch_admin, social_worker |
| POST | `/staff/refresher-training/users/{userId}/certificates` | 이수증 업로드 (multipart `file`) | branch_admin, social_worker |
| GET | `/staff/refresher-training/users/{userId}/certificates/{certificateId}` | 이수증 inline 미리보기/다운로드 | hq_admin, branch_admin, social_worker |
| DELETE | `/staff/refresher-training/users/{userId}/certificates/{certificateId}` | 이수증 삭제 | branch_admin, social_worker |

**쿼리 파라미터 (GET compliance)**: `branchId` (UUID, 선택 — 기본 active branch) · `referenceDate` (ISO date, 선택)

**응답 (GET compliance — `StaffRefresherTrainingSummaryResponse`)**:

```json
{
  "items": [
    {
      "userId": "uuid",
      "displayName": "김요양",
      "roleCode": "CAREGIVER",
      "status": "COMPLETED | OVERDUE | UPCOMING | UNKNOWN",
      "hiredAt": "2020-03-01 (nullable)",
      "nextDueDate": "2026-06-01 (nullable)",
      "completed": true
    }
  ],
  "totalCount": 12,
  "completedCount": 8,
  "overdueCount": 2,
  "upcomingCount": 1,
  "hasOverdue": true
}
```

**응답 (certificate — `StaffRefresherTrainingCertificateResponse`)**:

```json
{
  "id": "uuid",
  "userId": "uuid",
  "originalFilename": "certificate.pdf",
  "contentType": "application/pdf",
  "fileSizeBytes": 102400,
  "uploadedAt": "2026-06-12T09:00:00+09:00"
}
```

**semantics**:

- `status=UNKNOWN` — 입사일 미등록(`hiredAt` null) · FE `@50bdb6e` 별도 안내
- `status=OVERDUE` — 격년(2년) 주기 초과·이수증 미등록
- `status=UPCOMING` — 90일 이내 만료 예정
- 업로드 허용 MIME: PDF·JPEG·PNG (FE `staffRefresherTrainingCertificates.js` 검증)
- 업로드 시 lifecycle checklist key `refresher-training` 완료 처리
- **잔여 P2**: 교육일지·케어포 8-7-1 리포트 leaf (BNK-137~138)

---

## 9-6. 직원 건강검진 (8-10) — US-R02 / FAQ21799

> **상태**: backend **`f1268c6`**/`bad88f5` — V89 `StaffHealthCheckupController`·5영역 checklist **partial ✅**. frontend **`StaffHealthCheckupsPage` ✅** @ `604787f` · branch scope guard @ `bad88f5` · REQUIREMENTS G-Health-8-10·USER_STORIES US-R02.

| 메서드 | 경로 | 설명 | 권한 |
|--------|------|------|------|
| GET | `/staff/health-checkups/compliance` | 지점 직원 건강검진 compliance 요약 | hq_admin, branch_admin, social_worker |
| GET | `/staff/health-checkups/users/{userId}` | 직원 건강검진 이력 목록 | hq_admin, branch_admin, social_worker |
| POST | `/staff/health-checkups/users/{userId}` | 건강검진 기록 등록 (5영역 checklist) | branch_admin, social_worker |

**쿼리 파라미터 (GET compliance)**: `branchId` (UUID, 선택) · `referenceDate` (ISO date, 선택)

**요청 (POST — `CreateStaffHealthCheckupRequest`)**:

```json
{
  "checkupDate": "2026-06-01",
  "bodyMeasurementCompleted": true,
  "urinalysisCompleted": true,
  "bloodTestCompleted": true,
  "imagingCompleted": false,
  "resultAssessmentCompleted": true,
  "officeWorker": false,
  "resultNotes": "특이사항 없음 (nullable)"
}
```

**응답 (compliance item — `StaffHealthCheckupComplianceItemResponse`)**:

```json
{
  "userId": "uuid",
  "displayName": "김요양",
  "roleCode": "CAREGIVER",
  "status": "COMPLETED | OVERDUE | UPCOMING | NOT_APPLICABLE",
  "lastCheckupDate": "2025-06-01 (nullable)",
  "nextDueDate": "2026-06-01 (nullable)",
  "officeWorker": false,
  "completedAreaCount": 5
}
```

**semantics**:

- FAQ21799 **5영역**: 신체계측·요검사·혈액검사·영상검사·결과판정 — `completedAreaCount` 0~5
- `officeWorker=true` — 사무직(검진 주기·필수 영역 상이)
- POST 성공 시 lifecycle checklist key `health-checkup`·`health-checkup-initial` 갱신
- **Route 정본**: func.php **`8-10.건강검진관리`** (케어포 PDF `8-10.현황 리포트`와 번호 충돌 — PLAN_NOTES BNK-138)
- **잔여 P2**: 직원 파일함 PDF/jpg 첨부 deepen · ~~케어포 **8-12 직원현황 리포트**~~ → **§9-11 ✅ partial+** @ `bf6dd25`/`07956f5` (PDF 7종·엑셀 P2)

---

## 9-7. 직원 HR 파일함 (US-R03 / FAQ21806) — G-Staff-LC

> **상태**: backend **`bbb8e35`** — V91 `StaffHrFileController`·onboarding document types **partial ✅**. frontend **`StaffHrFilePanel` ✅** @ `bc3c967`/`57ed2db` (QA-B60 Fixed) · REQUIREMENTS G-Staff-LC·USER_STORIES US-R03.

| 메서드 | 경로 | 설명 | 권한 |
|--------|------|------|------|
| GET | `/staff/hr-files/users/{userId}` | 직원 HR 파일 목록 (documentType별) | hq_admin, branch_admin, social_worker |
| POST | `/staff/hr-files/users/{userId}` | HR 파일 업로드 (pdf/png/jpeg) | branch_admin, social_worker |
| GET | `/staff/hr-files/users/{userId}/{fileId}` | HR 파일 메타·다운로드 URL | hq_admin, branch_admin, social_worker |
| DELETE | `/staff/hr-files/users/{userId}/{fileId}` | HR 파일 삭제 | branch_admin, social_worker |

**semantics**:

- FAQ21806 **입사서류 8종**·건강검진 결과서 등 documentType catalog (V91)
- FAQ21799 건강검진 **5영역 checklist**와 파일함 연계 — compliance UI @ §9-6
- lifecycle checklist key `onboarding-documents` 등과 연동
- **잔여 P2**: FAQ21806 **6단계 workflow CRUD**(자격확인→근로계약→신규교육 7일→인력변경→입사서류→건강검진) (BNK-142~150)

---

## 9-8. 신규입소 위험도평가 (US-T11 / G40) — silverangel 지표21

> **상태**: backend **`686d686`/`2589b94`** — V93/V94 `ClientRiskAssessmentService`·3종 **✅ partial+**. frontend **`72676a5`/`e89175e`** — `ClientRiskAssessmentPanel`·ClientDetail tab·dashboard widget **✅ partial+** · REQUIREMENTS G40 · USER_STORIES US-T11 · **live E2E run 잔여**.

| 메서드 | 경로 | 설명 | 권한 |
|--------|------|------|------|
| GET | `/api/v1/clients/{clientId}/risk-assessments` | 수급자별 3종 위험도평가 조회 | hq_admin, branch_admin, social_worker |
| PUT | `/api/v1/clients/{clientId}/risk-assessments` | 위험도평가 upsert (type별) | branch_admin, social_worker |
| GET | `/api/v1/clients/admission-risk-assessments/compliance` | 급여개시 전 3종 완료 compliance (`admissionComplete`) | hq_admin, branch_admin, social_worker |

**필드** (`assessed_on`, `scale_score`, `risk_level`: LOW/MODERATE/HIGH, `notes`):

- **types**: `FALL_RISK`(낙상) · `PRESSURE_ULCER`(욕창) · `COGNITIVE_FUNCTION`(인지기능)
- **compliance**: `ltc_cert_valid_from`(급여개시일) 이전 3종 완료 가드 · `admissionComplete` boolean
- **잔여 P2**: live API E2E run (post-merge 권장 · 결정 96)

---

## 9-9. 반기 기초평가 위험도 (US-T12 / G40b) — silverangel 지표16

> **상태**: backend **`84e59d2`/`bdfc140`/`a7b4a39`** — V95/V96 `client_periodic_risk_assessments`·fiscal-half compliance·integrity+pilot **✅ full**. frontend **`7b68f54`/`6657d90`/`22325f4`** — `ClientPeriodicRiskAssessmentPanel`·`PeriodicRiskAssessmentStatusPage`·dashboard widget **✅ full** · REQUIREMENTS G40b · USER_STORIES US-T12 · **live E2E run 잔여**.

| 메서드 | 경로 | 설명 | 권한 |
|--------|------|------|------|
| GET | `/api/v1/clients/{clientId}/periodic-risk-assessments` | 수급자별 반기 3종 위험도평가 조회 (`fiscalYear`·`fiscalHalf` query) | hq_admin, branch_admin, social_worker |
| PUT | `/api/v1/clients/{clientId}/periodic-risk-assessments` | 반기 위험도평가 upsert (type별·반기 UNIQUE) | branch_admin, social_worker |
| GET | `/api/v1/clients/periodic-risk-assessments/compliance` | 반기 3종 완료 compliance (`periodicComplete`) | hq_admin, branch_admin, social_worker |

**필드** (G40 admission과 동일 3종 + 반기 컨텍스트):

- **types**: `FALL_RISK` · `PRESSURE_ULCER` · `COGNITIVE_FUNCTION`
- **반기**: `fiscalYear`(2000~2100) · `fiscalHalf`(1=1~6월, 2=7~12월)
- **compliance**: 급여 수급 중 이용자 · 반기 윈도우 내 3종 완료 · `periodicComplete` boolean
- **가드**: 급여개시일 미등록 이용자 기록 불가 · 평가일은 `max(반기시작, 급여개시일)` ~ 반기종료
- **잔여 P2**: live API E2E run (post-merge 권장 · 결정 96)

---

## 9-10. 업무수행일지 불러오기 (US-T13 / G34b) — FAQ21813

> **상태**: frontend **`0ce04ad`/`d41546f`** — needs-assessment→lead caregiver work log import **✅ partial** · REQUIREMENTS G34b · USER_STORIES US-T13 · **잔여 P2**: 월별 clone-from-previous·인지활동 role guard.

**semantics**:

- 이지케어 FAQ21813 **불러오기** — 욕구사정·급여계획 요약 템플릿을 `LeadCaregiverWorkLogPage`에 pre-fill
- G34 lead work log CRUD·sign modal @ §9-1과 연동
- **잔여 P2**: 전월 일지 clone · 프로그램관리자 role guard (FAQ21813 verbatim) — **125차**: clone @ `1b5fabe` · role guard @ `994f5ea`/`b6ecc35` · import-draft @ `8487667` **✅ partial+**

---

## 9-11. 직원 현황 리포트 (US-R02 / G-Health-8-12) — 케어포 8-12

> **상태**: backend **`bc927f7`/`229f84c`** — `GET /api/v1/staff/reports/status` aggregated · **`GET /api/v1/staff/reports/status/export` CSV export ✅** @ `bc927f7`/`c4dbe43`(UTF-8 BOM·outputType guard). frontend **`488f547`/`ff173af`/`443efca`** — `/staff/reports/status`·PDF 7종 FE·live E2E harness·**BE CSV FE wire ✅** @ `488f547`·**pagination ✅** @ `ff173af` · REQUIREMENTS G-Health-8-12 · USER_STORIES US-R02 · **잔여 P2**: print layout·live run.

| 메서드 | 경로 | 설명 | 권한 |
|--------|------|------|------|
| GET | `/api/v1/staff/reports/status` | 직원 현황 aggregated 리포트 (`branchId?`, `referenceDate?`) | hq_admin, branch_admin, social_worker |
| GET | `/api/v1/staff/reports/status/export` | 직원 현황 CSV export (`branchId?`, `referenceDate?`, `outputType?`) | hq_admin, branch_admin, social_worker |

**semantics**:

- 케어포 func **`8-12.현황 리포트`** · PDF p.106 출력물 7종 pack — **FE ✅** @ `07956f5` · **BE CSV FE wire ✅** @ `488f547` · **잔여 P2**: print layout
- FE `referenceDate` filter·export actions @ `07956f5`
- HR report pack — G41(8-7 교육일지)과 동일 Epic R 묶음

---

## 9-12. 통합 모니터링 checklist (US-T15 / G30) — FAQ21838~21842

> **상태**: backend **`b1dfd34`/`997831c`** — `GET /api/v1/compliance/monitoring/checklist` aggregate **✅** @ `b1dfd34`. frontend **`400c835`/`5146895`** — `IntegratedMonitoringChecklistPanel`·pilot E2E **✅ full** · REQUIREMENTS G30 · USER_STORIES US-T15 · **잔여 P1**: live API E2E verify.

| 메서드 | 경로 | 설명 | 권한 |
|--------|------|------|------|
| GET | `/api/v1/compliance/monitoring/checklist` | FAQ21838(RFID)·21839(20분)·21841(유선5명)·21842(rolling 6개월) **통합 aggregate** | hq_admin, branch_admin, social_worker |

**semantics**:

- BNK-181 발견→183 BE→184 FE **3-cycle 폐루프 완전 닫힘**
- §G30 self-diagnosis·phone consultation API와 complement (단일 checklist 뷰)
- **잔여 P1**: tester live API E2E verify (결정 96)

---

## 9-13. 팀장급 자격 compliance (US-S01 / G34-QUAL) — FAQ21837

> **상태**: backend **`726b3de`/`9a8bd2a`/`997831c`** — work-log enforce·`GET /api/v1/staff/team-lead-qualification/compliance` **✅ partial+**. frontend **`443efca`/`574bd08`** — FE gate·`TeamLeadQualificationCompliancePanel`·`LeadCaregiverWorkLogPage` embed **✅ partial+** · REQUIREMENTS G34-QUAL · USER_STORIES US-S01 · **잔여 P3**: StaffPage admin summary.

| 메서드 | 경로 | 설명 | 권한 |
|--------|------|------|------|
| GET | `/api/v1/staff/team-lead-qualification/compliance` | 팀장급 요양보호사 5년(월60h×60개월) 충족/미충족 요약 | hq_admin, branch_admin |

**응답 필드 (요약)**:

```json
{
  "eligibleCount": 3,
  "ineligibleCount": 1,
  "hasIneligible": true,
  "items": [
    { "userId": "uuid", "displayName": "김요양", "eligible": false, "monthsEmployed": 48 }
  ]
}
```

**semantics**:

- FAQ21837 verbatim「실무경력 5년(월 60시간×60개월) 이상」
- BNK-177→180→182→183 **4-cycle 폐루프** — BE enforce on lead caregiver work log create/update
- **잔여 P3**: StaffPage 전체 직원 자격 요약 위젯

---

## 9-15. 본인부담 간편결제 7-5 (US-L06 / G2) — BNK-189~190

> **상태**: backend **`b893e97`** · frontend **`bebd874`** — `EasyPayController`·V108 `easy_pay_requests_g7_5.sql`·`POST/GET /api/v1/billing/easy-pay/claims/{claimId}` **✅ partial+** (Stub PG·pilot E2E·prior-month guard) · FE `/billing/easy-pay`·`EasyPayPage`·`EasyPayPanel` **✅** · **잔여 P2**: provider normalization commit(QA-B78/B79) · live PG provider · G2b.

| 메서드 | 경로 | 설명 | 권한 |
|--------|------|------|------|
| POST | `/api/v1/billing/easy-pay/claims/{claimId}` | 간편결제 요청 생성 (provider: `CARD` \| `KAKAO_PAY`) | hq_admin, branch_admin |
| GET | `/api/v1/billing/easy-pay/claims/{claimId}` | 간편결제 요청 이력 조회 | hq_admin, branch_admin |

**요청 본문 (POST, 요약)**:

```json
{
  "provider": "CARD",
  "amount": 150000
}
```

**semantics**:

- **Stub PG** — `StubEasyPayProvider` (BNK-189) · live PG = P2
- **prior-month copay guard** — 전월 본인부담 미입금 시 결제 차단 @ `b893e97` (BNK-189 deepen)
- **provider normalization WIP** — case/whitespace `@Pattern` @ WT dirty (QA-B78)
- pilot E2E: `EasyPaymentPilotServiceFlowE2eTest` @ `1231389` · FE `easyPayPilot.e2e.test.js` @ `3848af6`

---

## 9-14. 기관 교육일지 8-7 (US-S04 / G41) — FAQ21807/21828

> **상태**: backend **`32f87f1`** · frontend **`e14ba10`** — `stafftraininglog/`·V104~V106·`GET/POST /api/v1/staff/training-logs`·`GET /api/v1/staff/training-logs/compliance` **✅ partial+** (G41b 5종 CHECK·aggregate·orientation min-date·branch scope) · FE `/staff/training-logs`·`StaffTrainingLogPage`·StatCard·`staffTrainingLogLiveApi.e2e.test.js` **✅** · REQUIREMENTS G41/G41b · USER_STORIES US-S04 · **잔여 P2**: `LIVE_E2E=1` manual verify·발송 템플릿 UI.

| 메서드 | 경로 | 설명 | 권한 |
|--------|------|------|------|
| GET | `/api/v1/staff/training-logs` | 교육일지 목록 (`branchId?`, `trainingType?`, `referenceYear?`) | hq_admin, branch_admin, social_worker |
| POST | `/api/v1/staff/training-logs` | 교육일지 등록 (4필드·신규직원 7일 가드) | branch_admin, social_worker |

**`trainingType` (V104~V106 CHECK, BNK-184·BNK-185)**:

- `ELDERLY_HUMAN_RIGHTS` — FAQ21807 노인인권 (반기 1회)
- `OPERATING_REGULATION` — FAQ21828 운영규정 (연 1회 + 신규 7일)
- `DISASTER_RESPONSE` — 케어포 8-7 재난상황대응 (연 1회)
- `FIRE_SAFETY_EQUIPMENT` — 케어포 8-7 소화설비·경보설비 (연 1회)
- `STAFF_RIGHTS` — 케어포 8-7 직원권익 (연 1회)

**잔여 (G41b P2)**:

- `LIVE_E2E=1` manual verify (harness @ `a4ab0c2` · post-merge)
- 발송 템플릿/심사 UI (optional deepen)

---

## 15. 간호급여 (Nursing Services) — L03 · §3-8

> **상태**: backend **`c655743`** — V114–V140 간호 데이터 모델·8 엔드포인트 **✅ PRESENT**. frontend **`3549896`** — `/nursing/*` 8개 화면 **✅ 완전 구현** · **분기 리포트 P2**. REQUIREMENTS §3-8·USER_STORIES US-O02.

### 15-1. 통합 바이탈 체크 (Integrated Vital Checks) — L03_M11

> **DB**: Flyway **V114** `nursing_vital_checks` · 혈압·체온·맥박·혈당·SpO2·호흡수 일일 기록.

| 메서드 | 경로 | 설명 | 권한 |
|--------|------|------|------|
| GET | `/api/v1/nursing/vital-checks` | 수급자별 바이탈 기록 (`clientId`, `from`, `to` query) | hq_admin, branch_admin, social_worker, caregiver |
| POST | `/api/v1/nursing/vital-checks` | 바이탈 기록 등록 | branch_admin, social_worker, caregiver |
| PATCH | `/api/v1/nursing/vital-checks/{recordId}` | 바이탈 기록 수정 | branch_admin, social_worker, caregiver |

**POST 요청**:

```json
{
  "clientId": "uuid",
  "recordedDate": "2026-06-10",
  "systolicBp": 130,
  "diastolicBp": 80,
  "temperature": 36.5,
  "bloodGlucose": 105,
  "spo2": 98,
  "respiratoryRate": 18,
  "notes": "정상 범위"
}
```

### 15-2. 체중 기록 (Weight Records) — L03_M14

> **DB**: Flyway **V115** `weight_records` · 주간·월간 체중 추이·변화 감지.

| 메서드 | 경로 | 설명 | 권한 |
|--------|------|------|------|
| GET | `/api/v1/nursing/weight-records` | 수급자별 체중 기록 목록 | hq_admin, branch_admin, social_worker, caregiver |
| POST | `/api/v1/nursing/weight-records` | 체중 기록 등록 | branch_admin, social_worker, caregiver |
| PATCH | `/api/v1/nursing/weight-records/{recordId}` | 체중 기록 수정 | branch_admin, social_worker, caregiver |

**POST 요청**:

```json
{
  "clientId": "uuid",
  "recordedDate": "2026-06-10",
  "weightKg": 65.2,
  "notes": "최근 감소 추세 주목"
}
```

### 15-3. 구강상태 점검 (Oral Care Checks) — L03_M13

> **DB**: Flyway **V116** `oral_care_checks` · 점검 항목(충치·잇몸·유연·의치 상태) · 조치 기록.

| 메서드 | 경로 | 설명 | 권한 |
|--------|------|------|------|
| GET | `/api/v1/nursing/oral-care-checks` | 수급자별 구강 점검 기록 | hq_admin, branch_admin, social_worker, caregiver |
| POST | `/api/v1/nursing/oral-care-checks` | 구강 점검 기록 | branch_admin, social_worker, caregiver |
| PATCH | `/api/v1/nursing/oral-care-checks/{recordId}` | 구강 기록 수정 | branch_admin, social_worker, caregiver |

**POST 요청**:

```json
{
  "clientId": "uuid",
  "checkedDate": "2026-06-10",
  "cavitiesPresent": false,
  "gumStatus": "NORMAL",
  "dentureStatus": "FITTED",
  "actionTaken": "칫솔질 도움",
  "notes": "잇몸 부기 주의"
}
```

### 15-4. 응급상황 기록 (Emergency Records) — L03_M04

> **DB**: Flyway **V117** `emergency_records` · 응급 사건·증상·대응·의료 조치 기록.

| 메서드 | 경로 | 설명 | 권한 |
|--------|------|------|------|
| GET | `/api/v1/nursing/emergency-records` | 수급자별 응급 기록 | hq_admin, branch_admin, social_worker, caregiver |
| POST | `/api/v1/nursing/emergency-records` | 응급 상황 기록 | branch_admin, social_worker, caregiver |
| PATCH | `/api/v1/nursing/emergency-records/{recordId}` | 응급 기록 수정 | branch_admin, social_worker, caregiver |

**POST 요청**:

```json
{
  "clientId": "uuid",
  "incidentDate": "2026-06-10",
  "incidentType": "FALL",
  "symptoms": "좌측 무릎 통증",
  "actionTaken": "의료 센터 내원 의뢰",
  "medicalResponse": "X-ray 촬영, 골절 없음 확인",
  "notes": "보호자 연락 완료"
}
```

### 15-5. 간호 서비스 기록 (Nursing Service Records) — L03_M01·M06

> **DB**: Flyway **V118–V119** `nursing_service_records`·`nursing_service_items` · 간호 서비스 유형·시간·내용.

| 메서드 | 경로 | 설명 | 권한 |
|--------|------|------|------|
| GET | `/api/v1/nursing/service-records` | 수급자별 간호 서비스 기록 | hq_admin, branch_admin, social_worker, caregiver |
| POST | `/api/v1/nursing/service-records` | 간호 서비스 기록 | branch_admin, social_worker, caregiver |
| PATCH | `/api/v1/nursing/service-records/{recordId}` | 서비스 기록 수정 | branch_admin, social_worker, caregiver |

**POST 요청**:

```json
{
  "clientId": "uuid",
  "serviceDate": "2026-06-10",
  "serviceType": "CATHETER_CARE",
  "duration": 30,
  "notes": "카테터 교체 완료"
}
```

### 15-6. 배설관 기록 (Excretion Tube Records) — L03_M06

> **DB**: Flyway **V120** `excretion_tube_records` · 위관·유루관·장루 관리·교체 기록.

| 메서드 | 경로 | 설명 | 권한 |
|--------|------|------|------|
| GET | `/api/v1/nursing/excretion-tube-records` | 수급자별 배설관 기록 | hq_admin, branch_admin, social_worker, caregiver |
| POST | `/api/v1/nursing/excretion-tube-records` | 배설관 기록 | branch_admin, social_worker, caregiver |
| PATCH | `/api/v1/nursing/excretion-tube-records/{recordId}` | 배설관 기록 수정 | branch_admin, social_worker, caregiver |

**POST 요청**:

```json
{
  "clientId": "uuid",
  "recordedDate": "2026-06-10",
  "tubeType": "URINARY_CATHETER",
  "action": "REPLACEMENT",
  "notes": "교체 후 정상 배뇨 확인"
}
```

### 15-7. 욕창 평가·예방·기록 (Pressure Ulcer Management) — US-O03 / G43

> **DB**: Flyway **V121–V127** pressure ulcer assessment·prevention plan·care records · lifecycle 추적.

| 메서드 | 경로 | 설명 | 권한 |
|--------|------|------|------|
| GET | `/api/v1/nursing/pressure-ulcer/assessments` | 수급자별 욕창 위험도 평가 | hq_admin, branch_admin, social_worker, caregiver |
| POST | `/api/v1/nursing/pressure-ulcer/assessments` | 욕창 위험도 평가 (BRADEN scale) | branch_admin, social_worker, caregiver |
| GET | `/api/v1/nursing/pressure-ulcer/prevention-plans` | 예방 계획 조회 | hq_admin, branch_admin, social_worker, caregiver |
| POST | `/api/v1/nursing/pressure-ulcer/prevention-plans` | 예방 계획 생성 | branch_admin, social_worker, caregiver |
| GET | `/api/v1/nursing/pressure-ulcer/care-records` | 욕창 케어 기록 | hq_admin, branch_admin, social_worker, caregiver |
| POST | `/api/v1/nursing/pressure-ulcer/care-records` | 욕창 케어 기록 | branch_admin, social_worker, caregiver |

**POST 요청 (Assessment)**:

```json
{
  "clientId": "uuid",
  "assessedDate": "2026-06-10",
  "bradenScore": 18,
  "riskLevel": "MODERATE",
  "assessmentNotes": "회음부 피부 발적 주의"
}
```

### 15-8. 분기별 간호 리포트 (Quarterly Nursing Report) — L03_M08

> **상태**: backend **`c655743`** API 미구현 (P2). frontend **`3549896`** 화면 미구현 (P2).

| 메서드 | 경로 | 설명 | 권한 |
|--------|------|------|------|
| GET | `/api/v1/nursing/reports/quarterly` | 분기별 간호 통합 리포트 (`branchId?`, `year`, `quarter` query) | hq_admin, branch_admin, social_worker |

**의도**: 바이탈·체중·응급·욕창 등 분기 통계 집계·출력.

---

## 9-16. 케이스관리 회의·평가 (Case Management) — US-T07 / G32

> **상태**: backend **`98e40a3`** — V95/V96 `case_management_meetings`·`case_management_evaluations`·기록·compliance·평가 5영역(G32b) **✅ full**. frontend **`e89175e`/`26499b3`** — `CaseManagementPage`·meetings/evaluations·compliance dashboard widget **✅ full** · REQUIREMENTS §3-8·USER_STORIES US-T07 · **live E2E run 잔여**.

|| 메서드 | 경로 | 설명 | 권한 |
||--------|------|------|------|
|| GET | `/api/v1/staff/case-management/meetings` | 이용자별 사례관리 회의 기록 목록 (`from`, `to`, `clientId` query) | hq_admin, branch_admin, social_worker |
|| POST | `/api/v1/staff/case-management/meetings` | 사례관리 회의 기록 등록 | branch_admin, social_worker |
|| PATCH | `/api/v1/staff/case-management/meetings/{meetingId}` | 회의 기록 수정 | branch_admin, social_worker |
|| GET | `/api/v1/staff/case-management/evaluations` | 이용자별 사례관리 평가 목록 (`from`, `to`, `clientId` query) | hq_admin, branch_admin, social_worker |
|| POST | `/api/v1/staff/case-management/evaluations` | 사례관리 평가 등록 (G32b 5영역) | branch_admin, social_worker |
|| PATCH | `/api/v1/staff/case-management/evaluations/{evaluationId}` | 평가 수정 | branch_admin, social_worker |
|| GET | `/api/v1/staff/case-management/compliance` | 사례관리 회의·평가 준수 집계 (`branchId?`, `referenceDate?`) | hq_admin, branch_admin, social_worker |

**POST `/api/v1/staff/case-management/meetings` 요청**:

```json
{
  "clientId": "uuid",
  "meetingDate": "2026-06-10",
  "participantsNames": "김사회, 이센터장",
  "caseManagementPlan": "케어플랜 요약",
  "reflectionNotes": "회의 결과 및 반영 사항"
}
```

**응답** (`CaseManagementMeetingResponse`):

```json
{
  "id": "uuid",
  "clientId": "uuid",
  "meetingDate": "2026-06-10",
  "participantsNames": "...",
  "caseManagementPlan": "...",
  "reflectionNotes": "...",
  "recordedAt": "2026-06-10T14:00:00+09:00"
}
```

**POST `/api/v1/staff/case-management/evaluations` 요청** (G32b 5영역):

```json
{
  "clientId": "uuid",
  "evaluationDate": "2026-06-10",
  "physicalFunctioning": "신체 기능 평가",
  "psychologicalState": "심리 상태 평가",
  "socialSupport": "사회적 지원 체계",
  "serviceeffectiveness": "서비스 효과",
  "clientSatisfaction": "클라이언트 만족도"
}
```

**응답** (`CaseManagementEvaluationResponse`):

```json
{
  "id": "uuid",
  "clientId": "uuid",
  "evaluationDate": "2026-06-10",
  "physicalFunctioning": "...",
  "psychologicalState": "...",
  "socialSupport": "...",
  "serviceEffectiveness": "...",
  "clientSatisfaction": "...",
  "recordedAt": "2026-06-10T14:00:00+09:00"
}
```

**GET `/api/v1/staff/case-management/compliance` 응답** (`CaseManagementComplianceResponse`):

```json
{
  "totalClients": 40,
  "meetingsRecordedCount": 35,
  "evaluationsRecordedCount": 32,
  "meetingsConducted": true,
  "evaluationsMet": true,
  "reflectionGapCount": 3
}
```

**semantics**:

- `meetingsConducted`: 지점 활성 이용자 중 월 회의 기록 비율 ≥ 80%
- `evaluationsMet`: 분기/연간 평가 완료 비율 ≥ 100% (G32 지표28)
- `reflectionGapCount`: 회의 결과 미반영 이용자 수

---

## 9-17. 기능회복훈련 계획·급여제공 (Functional Recovery) — US-T06 / G17

> **상태**: backend **`98e40a3`** — V97/V98 `functional_recovery_plans`·`functional_recovery_records`·compliance (3개 지표) **✅ full**. frontend **`e89175e`/`26499b3`** — `FunctionalRecoveryPage`·계획·기록·compliance dashboard widget **✅ full** · REQUIREMENTS §3-8·USER_STORIES US-T06 · **live E2E run 잔여**.

|| 메서드 | 경로 | 설명 | 권한 |
||--------|------|------|------|
|| GET | `/api/v1/programs/functional-recovery/plans` | 이용자별 기능회복훈련 계획 목록 (`clientId`, `from`, `to` query) | hq_admin, branch_admin, social_worker, caregiver |
|| POST | `/api/v1/programs/functional-recovery/plans` | 기능회복훈련 계획 등록 | branch_admin, social_worker |
|| PATCH | `/api/v1/programs/functional-recovery/plans/{planId}` | 계획 수정 | branch_admin, social_worker |
|| GET | `/api/v1/programs/functional-recovery/records` | 기능회복훈련 급여제공 기록 목록 | hq_admin, branch_admin, social_worker, caregiver |
|| POST | `/api/v1/programs/functional-recovery/records` | 급여제공 기록 등록 | branch_admin, social_worker, caregiver |
|| PATCH | `/api/v1/programs/functional-recovery/records/{recordId}` | 기록 수정 | branch_admin, social_worker, caregiver |
|| GET | `/api/v1/programs/functional-recovery/compliance` | 기능회복훈련 준수 집계 (G17 3개 지표) | hq_admin, branch_admin, social_worker |

**POST `/api/v1/programs/functional-recovery/plans` 요청**:

```json
{
  "clientId": "uuid",
  "planStartDate": "2026-06-01",
  "planContent": "관절 가동범위 훈련, 낙상예방 운동",
  "targetGoal": "일상생활 동작 개선"
}
```

**응답** (`FunctionalRecoveryPlanResponse`):

```json
{
  "id": "uuid",
  "clientId": "uuid",
  "planStartDate": "2026-06-01",
  "planContent": "...",
  "targetGoal": "...",
  "createdAt": "2026-06-01T09:00:00+09:00"
}
```

**POST `/api/v1/programs/functional-recovery/records` 요청**:

```json
{
  "clientId": "uuid",
  "recordedDate": "2026-06-05",
  "serviceMinutes": 60,
  "programContent": "관절 가동범위 훈련",
  "progressNotes": "좌측 팔 가동범위 증가 관찰"
}
```

**응답** (`FunctionalRecoveryRecordResponse`):

```json
{
  "id": "uuid",
  "clientId": "uuid",
  "recordedDate": "2026-06-05",
  "serviceMinutes": 60,
  "programContent": "...",
  "progressNotes": "...",
  "recordedAt": "2026-06-05T10:00:00+09:00"
}
```

**GET `/api/v1/programs/functional-recovery/compliance` 응답** (`FunctionalRecoveryComplianceResponse`):

```json
{
  "totalClients": 40,
  "plansRecordedCount": 38,
  "provisionsRecordedCount": 35,
  "benefitStartCount": 35,
  "provisionsCompletionRate": 0.875,
  "benefitStartConducted": true,
  "provisionsProvided": true,
  "gapCount": 3
}
```

**semantics** (G17 3개 지표):

- **Indicator 22**: 계획 수립률 ≥ 95% (`plansRecordedCount` / `totalClients`)
- **Indicator 23**: 급여제공 기록 ≥ 월 1회 이상
- **Indicator 24**: 생성 30일 내 시작 여부 (`benefitStartConducted` = 급여개시일 이후 30일 내 기록 여부)

---

## 9-18. 민원상담·사후관리 (Grievance Counseling) — US-S03 / G42

> **상태**: backend **`bcb1d9f`** — V99/V100 `grievance_counselings`·`grievance_follow_ups`·전자결재·사후관리 checklist·익명 상자 pilot E2E **✅ partial+**. frontend **`8a8b930`** — `GrievanceCounselingPage`·익명 상자·pending 결재함·팔로우업·compliance dashboard widget **✅ partial+** · REQUIREMENTS G42 (신규 Epic) · USER_STORIES US-S03 · **live E2E run 잔여**.

|| 메서드 | 경로 | 설명 | 권한 |
||--------|------|------|------|
|| GET | `/api/v1/staff/grievance-counselings` | 민원상담 기록 목록 (`from`, `to`, `targetType` query) | hq_admin, branch_admin, social_worker |
|| POST | `/api/v1/staff/grievance-counselings` | 민원상담 기록 등록 (DRAFT) | hq_admin, branch_admin, social_worker |
|| PATCH | `/api/v1/staff/grievance-counselings/{counselingId}` | 초안 수정 | hq_admin, branch_admin, social_worker |
|| POST | `/api/v1/staff/grievance-counselings/{counselingId}/submit` | 결재 요청 (DRAFT→PENDING) | hq_admin, branch_admin, social_worker |
|| POST | `/api/v1/staff/grievance-counselings/{counselingId}/approve` | 결재 승인 (PENDING→APPROVED) | hq_admin, branch_admin |
|| POST | `/api/v1/staff/grievance-counselings/{counselingId}/follow-up` | 사후관리 기록 (재발 확인) | hq_admin, branch_admin, social_worker |
|| GET | `/api/v1/staff/grievance-counselings/pending-approval` | 미승인 결재 목록 | hq_admin, branch_admin |
|| GET | `/api/v1/staff/grievance-counselings/follow-up/pending` | 사후관리 대기 기록 (승인됨 + 팔로우업 미실시) | hq_admin, branch_admin, social_worker |
|| GET | `/api/v1/staff/grievance-counselings/follow-up/compliance` | 사후관리 준수율 집계 (G42 지표52) | hq_admin, branch_admin, social_worker |

**POST `/api/v1/staff/grievance-counselings` 요청**:

```json
{
  "targetType": "CLIENT | STAFF | OTHER",
  "targetName": "홍길동 (대상자 이름 또는 익명)",
  "incidentDate": "2026-06-10",
  "grievanceContent": "민원 내용 상세 기록",
  "resolution": "해결 조치 내용"
}
```

**응답** (`GrievanceCounselingResponse`):

```json
{
  "id": "uuid",
  "targetType": "CLIENT",
  "targetName": "홍길동",
  "incidentDate": "2026-06-10",
  "grievanceContent": "...",
  "resolution": "...",
  "status": "DRAFT | PENDING | APPROVED",
  "submittedAt": "2026-06-11T09:00:00+09:00 (null if DRAFT)",
  "approvedAt": "2026-06-12T14:00:00+09:00 (null if not APPROVED)",
  "createdAt": "2026-06-10T15:00:00+09:00"
}
```

**POST `/api/v1/staff/grievance-counselings/{counselingId}/follow-up` 요청**:

```json
{
  "followUpDate": "2026-08-10",
  "followUpContent": "재발 여부 확인 기록"
}
```

**GET `/api/v1/staff/grievance-counselings/follow-up/compliance` 응답** (`GrievanceFollowUpComplianceResponse`):

```json
{
  "totalApprovedCount": 25,
  "followUpCompletedCount": 22,
  "pendingFollowUpCount": 3,
  "followUpCompletionRate": 0.88,
  "complianceMet": true
}
```

**semantics**:

- **G42 지표52**: 사후관리 준수율 ≥ 100% (60일 내 팔로우업 실시 비율)
- **상태 전환**: DRAFT → PENDING(제출) → APPROVED(승인) → FOLLOW_UP_RECORDED(사후관리)
- **익명 상자**: `targetName`이 익명 또는 비공개로 처리 가능 (PII 보호)

---

## 16. 미확정 (구현 전 확정 필요)

- ~~주민등록번호 수집·암호화~~ → **확정** (REQUIREMENTS §3-2-1)
- 공단 청구내역상세 **엑셀 컬럼 스펙**(샘플) — 파일럿 센터 확보 전 가정 컬럼 + **`처리상태` 스킵** 구현 (PLAN_NOTES #27, BENCHMARK G7)
- 본인부담 구분 4→3 통폐합 여부 — 파일럿 분포 확인 (PLAN_NOTES #30)
- ~~알림(SMS/알림톡) 엔드포인트~~ → **§11 preferences Fixed** · **§11-5 이력 조회 API Fixed @ `c53dd3b`**(발송 UI·중계 연동·프론트 잔여)
- CMS·간편결제 API — **v2 △ partial+** — CMS 등록+해지 @ `4a622ab`/`9a6fdb6` · **★ 7-5 easy-pay ✅ partial+** @ `438f5c7`/`c9baca2`→`b893e97`/`bebd874` (§9-15) · **FCMS·live PG 잔여** (BNK-190)
- ~~배차·이동경로 API~~ → **§12 transport implemented** @ `53a1ffe` · **unconfirm PATCH** @ `767d977`
- ~~식사·프로그램 API~~ → **§13 implemented** @ `dfd9be2` — **식단·일정 등록 API 후속**(Q161)
- ~~방문요양 API~~ → **§14 backend implemented** @ `3e4d3e6` — **frontend `/visits` partial** @ `311c7c0` · NHIS import **FE partial** · **US-V04 live E2E 잔여**
- ~~G34 선임 요양보호사 업무수행일지~~ → **§9-1 implemented** @ `559648f`·`6d6b426`
- ~~US-S02 보수교육(8-7-1) compliance~~ → **§9-5 BE+FE ✅** @ `51477bd`/`0a7fe16`/`50bdb6e` · **§9-14 G41/G41b ✅ partial+** @ `32f87f1`/`e14ba10`(5분류·compliance·live E2E harness) · P2: `LIVE_E2E` manual verify
- ~~G30 통합 checklist~~ → **§9-12 ✅ full** @ `b1dfd34`/`400c835`/`5146895` · P1: live API E2E verify
- ~~G34-QUAL 팀장급 자격~~ → **§9-13 ✅ partial+** @ `9a8bd2a`/`574bd08`/`997831c`
- ~~US-R02 건강검진(8-10)~~ → **§9-6 BE+FE partial ✅** @ `f1268c6`/`604787f`/`bad88f5` · **§9-7 HR file hub ✅ partial** @ `bbb8e35`/`bc3c967` · **§9-11 8-12 ✅ partial+** @ `488f547`/`ff173af` · P2: 파일함 deepen·print layout
- ~~US-R03 HR file hub~~ → **§9-7 BE+FE partial ✅** @ `bbb8e35`/`bc3c967`/`57ed2db`/`e76ca06`/`4efa168` · P2: FAQ21806 6단계 workflow CRUD
- ~~G40 신규입소 위험도평가~~ → **§9-8 ✅ partial+** @ `72676a5`/`686d686`/`e89175e` · P2: live E2E run
- ~~G40b 반기 기초평가 위험도~~ → **§9-9 ✅ full** @ `7b68f54`/`a7b4a39`/`22325f4` · P2: live E2E run
- ~~G34b 업무수행일지 불러오기~~ → **§9-10 ✅ partial** @ `0ce04ad` · P2: 월별 clone·role guard
- ~~US-T09 정기 욕구사정~~ → **§9-2 BE+FE implemented** @ `6f3315a`·`2642838`·`5be9070` · P2: 연간 리포트·지표15
- ~~US-T10 급여계약 첨부~~ → **§9-3 BE+FE file box implemented** @ `6f3315a`·`2642838` · P2: FAQ21805 lifecycle CRUD
- ~~대시보드 compliance snapshot~~ → **§9-4 backend implemented** @ `559648f` · frontend StatCard·panel **P2 일부 미구현**
- 직원 관리 API — v3(Should)

---

*이 문서는 planner 에이전트가 관리합니다. 엔드포인트 확정 시 coder·db_architect와 동기화하세요.*
