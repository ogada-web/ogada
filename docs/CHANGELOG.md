# ogada 변경 이력 (CHANGELOG.md)

> **작성**: tech_writer 에이전트  
> **최초 작성일**: 2026-06-05  
> **최종 갱신**: 2026-06-06 (V32–V33·청구 상태 필터 API·actor 감사 반영)  
> **상태**: 초안 (Draft)  
> **대상 독자**: 개발·운영·기획 담당자, 고객 센터 IT (`sysadmin`)  
> **기준 문서**: `docs/REQUIREMENTS.md`, `docs/API_SPEC.md`, `src/backend/`, `src/frontend/`  
> **기술 스택**: Java Spring Boot 3.x + React (Vite SPA) + PostgreSQL

이 문서는 [Keep a Changelog](https://keepachangelog.com/ko/1.1.0/) 형식을 따릅니다.  
버전 번호는 백엔드 `pom.xml`·프론트엔드 `package.json`의 `0.0.1` 계열과 동기화합니다.

---

## [Unreleased] — MVP v1 개발 중 (2026-06-06 업데이트)

### Added

#### 기획·설계 산출물
- `docs/REQUIREMENTS.md` — MVP v1 Must 범위, 7역할 RBAC, 다지점·SaaS 멀티테넌트, 청구·정산(케어포 벤치마킹) 확정
- `docs/API_SPEC.md` — `/api/v1` REST 엔드포인트 명세 (인증·플랫폼·이용자·출석·건강·청구·대시보드·설정)
- `docs/FLOWCHART.md` — 역할별 화면 흐름도
- `docs/USER_STORIES.md` — 사용자 스토리 초안
- `docs/ERD.md`, `docs/DATA_RETENTION_POLICY.md` — 데이터 모델·보관 정책
- `docs/USER_MANUAL.md`, `docs/ADMIN_GUIDE.md`, `docs/DEPLOYMENT_GUIDE.md` — 운영·배포 문서 초안

#### 백엔드 (Spring Boot 3.3.1, Java 17) — 2026-06-06 업데이트
- **프로젝트 골격**: Spring Security + OAuth2 Resource Server(JWT RSA), JPA, Flyway(V1–V27), PostgreSQL
- **인증 (`/api/v1/auth`)**: 로그인·토큰 갱신·로그아웃, `active_branch_id` 전환, `/me`, 로그인 이력, 비밀번호 재설정 요청·확인, **재설정 완료 시 활성 refresh 토큰 일괄 폐기** (V30)
- **플랫폼 (`/api/v1/platform/organizations`)**: Tenant 등록·목록·상세·상태 변경, **법인명·사업자번호 검색** (`?query=`, V29), 첫 `hq_admin` 계정 발급 (`platform_admin` 전용)
- **조직·지점 (`/api/v1/organization`, `/branches`)**: Tenant 정보·설정(`allow_client_self_checkin`), 지점 CRUD
- **직원 계정 (`/api/v1/users`)**: 목록·생성·수정 (`hq_admin`, `branch_admin`), **Tenant 내 이메일 대소문자 무시 중복 방지** (V30 UK, 저장 시 trim+소문자 정규화)
- **이용자 (`/api/v1/clients`)**: 등록·수정·퇴소, 목록 검색·페이지네이션, 보호자 연결, `client_user` 발급, 사진 업로드, **이용자별 출석·청구 이력** (`GET /{id}/attendance`, `GET /{id}/billing`), **주민등록번호 복호화 열람** (`POST /{id}/resident-registration/reveal`, 감사 로그 연동)
- **출석 (`/api/v1/attendance`)**: 수기 체크인/아웃, 결석 사유, QR 셀프 스캔(B방식), 지점 QR 생성, **월별 출석 통계** (`GET /attendance/stats/monthly`, 2026-06-06 추가)
- **보호자 포털 (`/api/v1/guardian`)**: 체크인 대상 목록 (`/checkin-targets`), **일일 기록 요약** (`GET /daily-records?clientId=&date=`), QR 스캔 핸들러
- **건강 기록 (`/api/v1/clients/{id}/health`)**: 바이탈·투약·사고·메모 CRUD
- **청구·정산 (`/api/v1/billing`)**: 수가표·본인부담 비율, 월별 청구서 생성·상태 변경, **청구 목록 상태 필터** (`GET /claims?status=DRAFT|CONFIRMED|PAID`, V31 인덱스 활용), 명세서 PDF, **공단 청구내역 엑셀 import·대사** (2026-06-06 기능화), **NHIS 배치 상태 이력** (V17–V20)
- **대시보드 (`/api/v1/dashboard`)**: 지점·통합 대시보드, 건강 이상 알림 통합 목록
- **시스템 설정 (`/api/v1/settings`)**: Tenant 기술 설정, 감사 로그·백업 이력 조회 (`sysadmin`)
- **보안·PII**: 주민등록번호 AES-GCM 암호화·마스킹, 연락처·주소 암호화, JWT 스코프 검증, 공통 에러 응답(`traceId`)
- **백업 스케줄러**: 일 1회 Tenant별 manifest 백업 (`BackupRunService`, `FileTenantBackupExecutor`), `backup_runs` 이력 기록, **완료 메타데이터 검증** (V20)
- **NHIS import 서비스**: 엑셀 파서, 행별 `MATCHED` / `DISCREPANCY` / `UNMATCHED` 상태 대사, **배치·행 지점 검증** (V21), **자동 Tenant 설정** (V22)
- **행위자(actor) 감사**: `DbSessionContext.setActorUserId` — 출석·건강·청구 생성·NHIS import 쓰기 트랜잭션에서 JWT subject를 DB 세션 변수(`ogada.actor_user_id`)로 전달 (V32–V33 트리거 backstop)
- **단위 테스트 21 클래스**: 인증, 이용자(마스킹·퇴소·복호화), 출석·보호자 QR·포털, 건강, 청구(상태 필터 포함)·NHIS 파서·대사·import, 대시보드·건강 알림, 설정·백업, 플랫폼 조직

#### 데이터베이스 (Flyway V1–V33)
- **V1**: 멀티테넌트 핵심 스키마 — `organizations`, `branches`, `users`, `clients`, `attendance`, `health_records`, `fee_schedules`, `copay_rates`, `billing_claims`, `audit_logs`
- **V2**: 보호자 연결, QR·인증 토큰, 청구 명세 라인, NHIS import, 이용자 퇴소·사진·`client_user` 링크, `platform_admin` 조직 NULL 허용, 청구 라인 클라이언트 unique 제약 (`uq_claim_item_client`)
- **V3–V4**: 인덱스·CHECK 제약, 주민번호 동의 규칙, 테넌트 FK·도메인 제약
- **V5–V6**: 참조 무결성, 청구·출석 산술 불변식, 감사 로그 인덱스
- **V7**: 보호자 primary 유일성, `client_user` 테넌트 일관성, 출석·청구 업무 규칙
- **V8**: `active_branch` 테넌트 FK, 확정 청구 불변성, NHIS 테넌트 격리
- **V9**: Tenant 기술 설정(`backup_enabled`, `audit_retention_days`), `backup_runs` 이력
- **V10**: NHIS 청구 Tenant FK, 상태 이력, 출석 가드
- **V11**: 출석 출석/결석 상호 배타, 청구 헤더·라인 합계 대사, NHIS 음수 방지
- **V12**: 청구 라인 등급·부담구분 도메인 검증, 출석일 상한, 이용자 이름 trigram 검색 인덱스, 백업 완료 시각 검증
- **V13**: 퇴소 이용자 건강 기록 INSERT 가드, `copay_rates`·`fee_schedules` 도메인 CHECK, 보호자·`client_user` 역할 일관성, QR 토큰 만료 인덱스
- **V14**: 출석 결석·행위자 Tenant FK, QR 토큰 보존·purge 인덱스
- **V15**: 출석 시간·교통편 도메인, 데이터 보존 purge 인덱스
- **V16**: 청구 라인 Tenant FK, 보존·purge 인덱스
- **V17**: NHIS 배치 청구 기간·상태 이력 도메인
- **V18**: 지점 QR 토큰 값 컬럼
- **V19**: NHIS 대사 `MATCHED`/`DISCREPANCY` 시 `client_id` 필수, 배치 `row_count`·`imported_at` 무결성
- **V20**: `backup_runs` 종료 상태 `completed_at`·`error_message` 규칙, NHIS `imported_at` 시간 정합
- **V21**: NHIS 매칭 시 이용자 지점 일치 강제 (`trg_nhis_rows_client_branch`, `trg_nhis_batches_claim_branch`)
- **V22**: NHIS 행 자동 Tenant 설정 (`trg_nhis_import_rows_set_org`)
- **V23**: 보호자 연결 자동 Tenant 설정 (`trg_guardian_clients_set_org`), 서비스 쿼리·보호자 업무 규칙 인덱스
- **V24**: 클라이언트·출석·청구 쿼리 성능 인덱스 (대시보드·리포트 속도 최적화)
- **V25**: NHIS import `ltc_cert_no` 공백 검증 (`chk_nhis_import_rows_ltc_cert_nonempty`)
- **V26**: 청구 명세 라인 중복 방지 (`uq_billing_claim_items_claim_client`)
- **V27**: NHIS import 지점·인정번호 조회, 청구 명세·수가표·플랫폼 Tenant명 검색 인덱스, V2 중복 UK 정리
- **V28**: 로그인·비밀번호 재설정 이메일 조회, NHIS 배치 행·백업 Tenant 스캔 성능 인덱스
- **V29**: `user_branches` user_id 역조회, 플랫폼 사업자번호 trigram 검색, 청구 라인 `(claim_id, created_at)` 정렬 인덱스
- **V30**: Tenant 이메일 `lower(email)` UK, 활성 refresh user_id partial, 직원 `(organization_id, is_active)` 목록 인덱스
- **V31**: 청구 목록 status+`generated_at` 인덱스, 상태 이력 no-op 전이 CHECK, 대표 보호자 partial 인덱스
- **V32**: `ogada_read_actor_user_id()` 공통 함수, 출석 `created_by`·청구 `generated_by` actor 자동 적재 트리거, NHIS COMPLETED `imported_at` backstop, 퇴소 purge partial 인덱스 (`idx_clients_org_discharged_at`)
- **V33**: 건강 `recorded_by`·NHIS `imported_by` actor backstop 트리거, 퇴소 후 child purge 인덱스(`attendance`/`health_records`/`billing_claim_items` by `client_id`), 활성 이용자 목록 pagination 인덱스

#### 프론트엔드 (React 18 + Vite 5)
- SPA 초기 골격: `/`, `/dashboard`, `/dashboard/hq`, `/platform`, `/guardian`, `/settings` 역할별 홈 라우팅
- 데모 역할 링크가 있는 로그인 화면 골격

### Changed
- **기술 스택 전환 (2026-06-05)**: 초기 에이전트 설정(Python/FastAPI + Vanilla JS) → **Java Spring Boot 3.x + React(Vite) + PostgreSQL** 로 확정. 레거시 Python 백엔드 **전부 폐기**, Java 신규 구현
- **사업 모델 확정**: 단일 센터 전용 → **전국 B2B SaaS 멀티테넌트** (`Organization` → `Branch` 계층, 테넌트 간 데이터 격리)
- **MVP 범위 확대**: 인증·이용자·출석·건강·대시보드에 **청구·정산**, **`platform_admin` 온보딩**, **7역할 UI** 포함
- **출석 방식**: 수기 + **QR B방식**(보호자/이용자 → 지점 QR) 확정. A방식(직원이 이용자 QR 스캔)은 MVP 제외
- **청구 설계**: 케어포 벤치마킹 **2단계 모델** — 내부 계산 + 명세서 + 공단 엑셀 import (공단 직접 전송·CMS는 후속)
- **수가표**: 코드 고정 → **`hq_admin` 화면 입력 테이블**(`fee_schedules`, 연도별 버전 이력)
- **본인부담률**: 이용자별 구분(`copay_type`) + 비율 테이블(`copay_rates`)
- **주민등록번호 정책**: 수집·암호화 저장·마스킹·별도 동의·복호화 감사 로그 (공단 청구 법정 필수)

### Deprecated
- `src/backend` 이하 **Python/FastAPI 레거시 코드 전체** — Java 백엔드로 대체, 참조·마이그레이션 없음

### Fixed
- **API 명세 대비 미구현 엔드포인트 보완** (2026-06-06): `GET /attendance/stats/monthly`, `GET /branches/{id}/qr`, `PATCH /billing/fee-schedules/{id}` 구현 완료
- **NHIS import 대사**: 행별 `MATCHED` / `UNMATCHED` / `DISCREPANCY` 상태 및 배치 완료 메타데이터 정합 (V19–V20)
- **백업 이력**: `backup_runs` SUCCESS/FAILED 시 `completed_at`·`error_message` 필수 (V20)
- **V21–V33 데이터·성능**: NHIS 지점 검증, 자동 Tenant 설정·actor backstop 트리거, 이용자·청구·플랫폼·인증·NHIS 배치 조회 인덱스, Tenant 이메일 UK·청구 상태 이력 무결성, 퇴소 purge·활성 이용자 목록 인덱스
- **청구 목록 상태 필터**: `GET /billing/claims?status=` 구현 — `DRAFT`/`CONFIRMED`/`PAID` 필터, 미지정 시 전체 목록 (V31 인덱스 활용)
- **비밀번호 재설정 보안**: `resetPassword` 성공 시 `refreshTokenRepository.revokeAllActiveForUser` 호출 (V30 인덱스 활용)
- **FAQ QR 유효시간 정정**: 기본 **60분** (`DEFAULT_QR_EXPIRES_MINUTES`, 생성 시 1–720분 설정 가능) — 24시간 설명 제거

### Security
- JWT(RSA) + RBAC 역할·지점 스코프 강제
- PII(주민등록번호) 암호화·마스킹, 복호화 시 `audit_log` 기록
- API 에러 응답에서 스택·DB 상세 미노출 (`GlobalExceptionHandler`)
- Flyway 마이그레이션 다단계 무결성·불변식으로 청구·출석 데이터 오염 방지

### Known gaps (미구현·진행 중)

| 영역 | 상태 | 비고 |
|------|------|------|
| 프론트엔드 업무 화면 | **SPA 라우팅 골격** | JWT 로그인, API 클라이언트, 역할별 메뉴 미구현. 홈 라우팅만 존재. 업무 CRUD UI 전무 |
| 백엔드 REST API | **Must 범위 완료** | 인증·플랫폼·이용자·출석·건강·청구(상태 필터 포함)·대시보드·설정 모두 구현. 테스트 21개 클래스 통과 |
| 퇴소 데이터 purge 배치 | **인덱스만 준비** | V32–V33 purge 인덱스 적용. `@Scheduled` retention 배치는 후속 구현 (`DATA_RETENTION_POLICY` §4-1) |
| 프론트엔드 우선순위 (v1 직전) | **대기** | ① 로그인·토큰 ② 이용자 목록 ③ 수기 출석 ④ 건강 기록 ⑤ 청구서(상태 필터 UI) ⑥ 대시보드 ⑦ 보호자 QR |
| 백업 실행체 | **MVP manifest** | `FileTenantBackupExecutor` — 프로덕션 `pg_dump` 교체 예정 |
| 이용자 사진·정적 파일 | **로컬 디스크** | `CLIENT_PHOTOS_DIR` — 오브젝트 스토리지 연동 후속 |
| 보호자 알림·식사·프로그램·직원 관리 | **v1 이후** | REQUIREMENTS Should/Could |
| 공단 포털 직접 전송·CMS·본인부담금 발송 | **후속** | MVP 기본 구조만 |

---

## [0.0.1] — 2026-06-05

> **태그**: 개발 스냅샷 (정식 릴리스 전)  
> **백엔드**: `com.ogada:backend:0.0.1-SNAPSHOT`  
> **프론트엔드**: `ogada-frontend@0.0.1`

MVP v1 **1주차 목표** 기준의 첫 통합 스냅샷. 백엔드 REST API·DB 스키마(Flyway V20)가 API 명세 Must 범위를 구현했으며, 프론트엔드는 역할별 라우팅 골격 단계이다.

### Added
- Spring Boot 백엔드 프로젝트 초기화 및 PostgreSQL 멀티테넌트 스키마 (Flyway V1)
- React(Vite) SPA 프로젝트 초기화 및 7역할 데모 라우팅
- 기획 문서 세트 초안 (`REQUIREMENTS`, `API_SPEC`, `FLOWCHART`, `USER_STORIES`)

### Changed
- 프로젝트 기술 스택을 Java + React + PostgreSQL로 확정 (§REQUIREMENTS 1-1)

---

## [0.0.0] — 2026-06-03

프로젝트 착수. 주간보호센터 운영 관리 웹 시스템 **ogada** 기획 시작.

### Added
- `.agents/agents.yaml` 기반 멀티 에이전트 워크플로우
- 초기 기술 가정: Python/FastAPI + Vanilla JS (이후 폐기)

---

## 버전 정책 (안)

| 구분 | 규칙 |
|------|------|
| **Major** (`1.0.0`) | MVP v1 프로덕션 GA, 하위 호환 깨는 API·스키마 변경 |
| **Minor** (`0.x.0`) | Must 기능 모듈 완성, 신규 API·화면 추가 |
| **Patch** (`0.0.x`) | 버그 수정, 마이그레이션 보강, 문서 갱신 |
| **SNAPSHOT** | 개발 중 빌드 (`0.0.1-SNAPSHOT`) — CHANGELOG `[Unreleased]`에 누적 |

정식 릴리스 시 `[Unreleased]` 항목을 버전 섹션으로 이동하고 날짜·태그를 기록합니다.

---

## 관련 문서

| 문서 | 용도 |
|------|------|
| `docs/REQUIREMENTS.md` | 기능·비기능 요구사항 원본 |
| `docs/API_SPEC.md` | REST API 상세 명세 |
| `docs/DEPLOYMENT_GUIDE.md` | 배포·마이그레이션·환경변수 |
| `docs/USER_MANUAL.md` | 현장 사용자 조작 가이드 |
| `docs/ADMIN_GUIDE.md` | 플랫폼·시스템 관리자 가이드 |

---

*이 문서는 tech_writer 에이전트가 관리합니다. 기능 머지·릴리스 시 `[Unreleased]`를 갱신하세요.*
