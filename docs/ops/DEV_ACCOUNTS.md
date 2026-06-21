<!-- doc:owner=TWR doc:audience=COD,PLN updated=2026-06-21T23:30:00+09:00 -->

# ogada 개발(dev) 계정 목록

> **작성**: 2026-06-20  
> **환경**: 로컬 백엔드 `http://127.0.0.1:8080` · 프론트 `http://127.0.0.1:5173`

로컬·스테이징 개발용입니다. **운영(prod) 비밀번호와 다릅니다.**

API 호출 시 지점 헤더: `X-Branch-Id: 00010101-0001-4000-8000-000000000001`  
(브라우저 UI 로그인은 기본 지점이 자동 선택됩니다.)

## 조직·지점

| 항목 | 이름 | UUID |
|------|------|------|
| 조직 | 테스트요양기관 | `00000001-0001-4000-8000-000000000001` |
| 기본 지점 | 서울 강남 주간보호센터 | `00010101-0001-4000-8000-000000000001` |

## 역할별 계정

> **ogada 내부 직원** 역할은 코드·계정 이메일에 `ogada_` 접두사를 붙여 센터(테넌트) 역할과 구분합니다.

| 역할 | 한글 | 소속 | 이메일 | 비밀번호 | 홈 화면 |
|------|------|------|--------|----------|---------|
| **ogada_platform_admin** | 플랫폼 관리자 | **ogada** | *(시드 없음 — 아래 참고)* | — | /platform |
| hq_admin | 통합 관리자 | 센터 | test@test.com | ogada1234 | /dashboard/hq |
| sysadmin | 시스템 관리자 | 센터 IT | sysadmin@ogada.test | ogada1234 | /settings |
| branch_admin | 지점장 | 지점 | badmin@test.com | ogada1234 | /dashboard |
| social_worker | 사회복지사 | 지점 | social@ogada.test | ogada1234 | /dashboard |
| caregiver | 요양보호사 | 지점 | caregiver@ogada.test | ogada1234 | /dashboard |
| guardian | 보호자 | 연결 이용자 | live-e2e-guardian@ogada.test | ogada-guardian-e2e | /guardian |
| client_user | 이용자 본인 | 본인 | client@ogada.test | ogada1234 | /guardian |

## sysadmin 참고

- 시스템 설정: `/settings`
- 카카오 API 사용량·한도: `/settings` → 「카카오 API」 탭
- hq_admin도 동일 API 상태는 `/organization/settings` → 「배차·카카오 API」에서 조회 가능

## ogada_platform_admin (플랫폼 운영자)

- **역할 코드**: `ogada_platform_admin` (구 `platform_admin`)
- **하는 일**: 전국 Tenant 등록, 첫 `hq_admin` 발급 (`/platform`)
- **조직 소속 없음** (`organization_id` NULL) — 센터 계정과 DB·JWT에서 분리
- dev DB에 **기본 시드 계정 없음** — 운영 DB에만 수동 발급 또는 bootstrap
- 권장 이메일 패턴: `ogada_platform@ogada.test` (또는 `ogada_*@ogada.test`)
- `hq_admin`의 직원 생성 API로는 **만들 수 없음** (`UserService` 정책)

## Live E2E 기본값

실행용 env는 [`scripts/dev-live-e2e.env.example`](../../scripts/dev-live-e2e.env.example) 참고.

| 용도 | 이메일 | 비밀번호 |
|------|--------|----------|
| staff (hq_admin) | test@test.com | ogada1234 |
| guardian | live-e2e-guardian@ogada.test | ogada-guardian-e2e |

## 계정 재생성

`hq_admin`(`test@test.com`)으로 로그인 후 직원 관리 또는 `POST /api/v1/users`로 위 역할 계정을 다시 만들 수 있습니다.  
`sysadmin`은 `branchIds`에 기본 지점 UUID가 필요합니다 (API 검증상 빈 배열 불가).

## 관련 문서

- [ADMIN_GUIDE.md §1-3 관리자 역할 구분](./ADMIN_GUIDE.md#1-3-관리자-역할-구분) — `ogada_platform_admin` / `sysadmin` / `hq_admin` 비교
- [REQUIREMENTS.md §2-2 역할 정의](../planning/REQUIREMENTS.md#2-2-역할-정의) — 8역할 전체 표
- [USER_MANUAL.md](./USER_MANUAL.md) — 센터 현장 역할(운영) 안내
- [DEPLOYMENT_GUIDE.md §3 로컬 개발 환경](./DEPLOYMENT_GUIDE.md#3-로컬-개발-환경)
- [DEPLOYMENT_GUIDE.md §3-7 live E2E](./DEPLOYMENT_GUIDE.md#3-7-프론트엔드-테스트빌드)
