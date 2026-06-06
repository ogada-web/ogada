<!-- doc:owner=PLN doc:audience=COD,TSR,UXD,DBA,BNK,TWR updated=2026-06-06T19:00:00+09:00 -->
# 주간보호센터 웹 시스템 — REST API 명세 (API_SPEC.md)

> **작성**: planner 에이전트
> **최초 작성일**: 2026-06-05
> **최종 갱신**: 2026-06-06 (NHIS `처리상태` 파서·롱텀2026 안내)
> **상태**: 초안 (Draft) — 사용자 승인 전
> **범위**: MVP v1 (Must) — 인증, 플랫폼, 조직·지점, 이용자, 출석, 건강, 청구, 대시보드
> **기준 문서**: `REQUIREMENTS.md`, `USER_STORIES.md`

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
| PATCH | `/branches/{branchId}` | 지점 수정·비활성 | hq_admin |
| GET | `/users` | 직원 계정 목록(지점 필터) | hq_admin, branch_admin |
| POST | `/users` | 직원 계정 생성·역할·지점 배정 | hq_admin, branch_admin |
| PATCH | `/users/{userId}` | 계정 수정·역할 변경·퇴직 처리 | hq_admin, branch_admin |

**PATCH `/organization/settings`**

```json
{ "allowClientSelfCheckin": true }
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
  "copayType": "GENERAL"
}
```

> **보안**: `residentRegistrationNo`(주민등록번호)는 고유식별정보 → **저장 시 암호화**, 응답·로그·목록에는 **마스킹**(`******-*******`)만 노출. 수집 여부는 §보안 미확정(아래 메모) 확정 후 반영.
> **`copayType`**: `GENERAL`(일반) | `REDUCED_40`(감경) | `REDUCED_60`(감경) | `MEDICAID`(기초·의료급여) — 실제 비율은 `copay_rates` 테이블 참조(§7).

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
| GET | `/billing/claims` | 청구 내역 목록 — `?branchId=&status=DRAFT\|CONFIRMED\|PAID` (V31 인덱스) |
| GET | `/billing/claims/{id}` | 청구서 상세(이용자별 명세) |
| PATCH | `/billing/claims/{id}/status` | 상태 변경(작성중→확정→수납완료) — 확정 후 금액 불변(V8) |
| GET | `/billing/claims/{id}/statement.pdf` | 급여비용 명세서 출력(PDF) |
| POST | `/billing/imports/nhis` | 공단 청구내역상세 **엑셀 import** (multipart) |

**GET `/billing/claims` 쿼리**

- `branchId` (optional): 토큰 스코프 내 지점 필터
- `status` (optional): `DRAFT` | `CONFIRMED` | `PAID` — US-G07, `idx_billing_claims_org_branch_status_generated`

**POST `/billing/claims/generate`**

```json
{ "branchId": "uuid", "yearMonth": "2026-05" }
```

> **계산 규칙**: 이용자별 `총 급여비용 = 등급 수가(7-1) × 출석일수`, `본인부담금 = 총액 × 이용자 copayType 비율(7-2)`, `공단부담 = 총액 − 본인부담금`. 과거 청구는 당시 수가·비율 버전 유지.

### 7-4. NHIS Import Reconciliation — §3-9-4, US-G04/G06

케어포 4단계(공단 엑셀 업로드 → 행별 대조) 벤치마크. 배치·행 매칭 상태는 `MATCHED` | `DISCREPANCY` | `UNMATCHED`.

| 메서드 | 경로 | 설명 |
|--------|------|------|
| POST | `/billing/imports/nhis` | 엑셀 업로드 — `branchId`, `yearMonth`, `claimId`(optional), `file` (multipart) |
| GET | `/billing/imports/nhis` | 배치 목록 — `?branchId=&yearMonth=&claimId=` |
| GET | `/billing/imports/nhis/{batchId}` | 배치 상세 + reconciliation 행 목록 |
| GET | `/billing/imports/nhis/{batchId}/candidates` | `UNMATCHED` 행 수동 매칭 후보 이용자 검색 — `?q=&page=&size=` |
| PATCH | `/billing/imports/nhis/rows/{rowId}/match` | 수동 매칭 — `{ "clientId": "uuid" }` → `MATCHED`/`DISCREPANCY` 전이 |

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
- 수동 매칭: `client_id` + 상태 전이 **단일 트랜잭션** (부분 업데이트 금지)
- 매칭 이용자 `branch_id` = 배치 `branch_id` (V21 `trg_nhis_rows_client_branch`)

**PATCH `/billing/imports/nhis/rows/{rowId}/match`**

```json
{ "clientId": "uuid" }
```

> UI 안내: 「공단 [longtermcare.or.kr](https://www.longtermcare.or.kr/)에서 청구 전송 후 청구내역상세 엑셀을 다운로드하세요」— 공단 직접 전송 API는 MVP 제외.  
> **롱텀 2026**: IE 접속 불가 — 엑셀 export 전 **Chrome/Edge** 사용 안내(온보딩·import 화면).

---

## 8. 대시보드 (Dashboard) — §3-11

| 메서드 | 경로 | 설명 | 권한 |
|--------|------|------|------|
| GET | `/dashboard/branch` | 지점 대시보드(오늘 출석·이용자 통계·건강 이상 알림) | branch_admin 이하 |
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

## 10. 미확정 (구현 전 확정 필요)

- ~~주민등록번호 수집·암호화~~ → **확정** (REQUIREMENTS §3-2-1)
- 공단 청구내역상세 **엑셀 컬럼 스펙**(샘플) — 파일럿 센터 확보 전 가정 컬럼 + **`처리상태` 스킵** 구현 (PLAN_NOTES #27, BENCHMARK G7)
- 본인부담 구분 4→3 통폐합 여부 — 파일럿 분포 확인 (PLAN_NOTES #30)
- 알림(SMS/알림톡) 엔드포인트 — v2
- CMS·간편결제 API — v2 (BENCHMARK G2)
- 식사·프로그램·직원 관리 API — v3(Should)

---

*이 문서는 planner 에이전트가 관리합니다. 엔드포인트 확정 시 coder·db_architect와 동기화하세요.*
