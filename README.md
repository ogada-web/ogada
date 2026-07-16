<!-- doc:owner=TWR doc:audience=DEV,PLN,UXD,COD,DBA updated=2026-07-16T18:50:00Z -->

# ogada — 주간보호센터·요양기관 운영 시스템

> **og** (온수) + **ada** (따뜻한) — 따뜻한 돌봄의 디지털화

ogada는 **전국 주간보호센터·요양기관**을 위한 **B2B SaaS 멀티테넌트 웹 시스템**입니다.

이용자 관리, 출석(수기·QR B방식), 건강 기록, 청구·정산, 다지점 대시보드, 보호자 포털 등 일상 운영 업무를 클라우드 기반으로 지원합니다.

---

## ✅ 현재 상태 (2026-06-28 TWR 396차 최종 동기화)

| 항목 | 상태 |
|------|------|
| **Backend baseline** | **`7fcdfde`** — V1–V183 · 275 test suites · 1999 @Test · Must ✅ |
| **Frontend baseline** | **`e19328a`** — 118 routes · 93 pages · Module KPI **~80.86%** |
| **방문일정 import 안내·결과 (G-NHIS-SCHEDULE-IMPORT + G-NHIS-IMPORT-ERROR-STATUS-SURFACE, Q731–Q742)** | ✅ FULL-STACK — PLAN/BILLING 4단계 · outcome Alert · guidance 7단계 · 미매칭 수급자 찾기 · branch filter |
| **급여제공 변경계약서 일괄 출력 (G-CLIENT-CONTRACT-BULK-PRINT, Q726·Q734)** | ✅ FULL-STACK — `/clients/care-plan-forms/bulk-export` · branchId·clientIds normalize · V183 index |
| **위원회·보호자 회의록 (G-STAFF-COMMITTEE-MEETING-LOG, Q723–Q725)** | ✅ FULL-STACK — `/staff/committee-meetings` · 3종 유형 · DRAFT→FINALIZED · 확정 plain-text · V182 CHECK |
| **프로그램 리포트 (G-REPORT-DENSITY M5, Q714–Q715)** | ✅ FULL-STACK — 4 routes · optional branchId · V179 group history |
| **이동서비스비 parity-rules (G16 Q743)** | ✅ FE wire — **`ONE_PER_DAY.description` 우선** · static cascade · TransportParityRulesPanel |
| **bootstrap service-unavailable (QA-B95 Q744)** | ✅ health lock — enabled·bean missing matrix · HealthControllerTest +1 |
| **live E2E G21 seed (QA-B95 Q733·Q736·Q737)** | ✅ — 3축 component code · null normalize · probe state persistence |
| **Must 갭** | **0** — 기존 Must 완전 안정화 · G16 9단계 parity chain |
| **P2 Planned** | program reports FE `branchId` · 7-5 live PG · J03 Solapi · M6 `/safety/*` |
| **Merge gate** | **865+** · cross-stream BLOCK · QA Open 1(active) |

## 🎯 주요 기능 (MVP v1)

| 영역 | 설명 |
|------|------|
| **인증·권한** | 7개 역할(`platform_admin`, `hq_admin`, `branch_admin`, `social_worker`, `caregiver`, `guardian`, `client_user`) + 테넌트 격리 |
| **이용자 관리** | 기본·장기요양·보호자 정보, 등급 변동 이력, 욕구사정, 위험도 평가 |
| **출석 기록** | 수기 체크인/아웃, QR 셀프 체크인(보호자/이용자), 일일·월별 통계 |
| **건강 기록** | 혈압·체온·혈당·SpO2, 투약 기록, 낙상·사고 이벤트, 특이사항 메모 |
| **청구·정산** | 수가표·본인부담 비율 관리, 월별 청구 자동 계산, 공단 엑셀 import·reconciliation |
| **대시보드** | 지점 현황(오늘 출석, 이용자 통계, 건강 알림), 통합 대시보드(HQ 비교·집계) |
| **보호자 포털** | 일일 기록 열람, 명세 조회, QR 체크인 |
| **직원 관리** | 계정·역할·지점 배정, 보수교육, 건강검진, HR 파일함 |
| **시스템 설정** | 기술 설정, 감사 로그, 백업 관리(`sysadmin`) |

---

## 📋 문서

### 프로젝트 관계자용

- **[docs/README.md](docs/README.md)** — 문서 구조 개요
- **[docs/ops/USER_MANUAL.md](docs/ops/USER_MANUAL.md)** — 현장 사용자 조작 가이드
- **[docs/ops/ADMIN_GUIDE.md](docs/ops/ADMIN_GUIDE.md)** — 시스템·플랫폼 관리자 가이드
- **[docs/ops/FAQ.md](docs/ops/FAQ.md)** — 자주 묻는 질문
- **[docs/ops/DEPLOYMENT_GUIDE.md](docs/ops/DEPLOYMENT_GUIDE.md)** — 배포·인프라 관리
- **[docs/ops/CHANGELOG.md](docs/ops/CHANGELOG.md)** — 버전 이력·주요 변경사항

### 기술 설계 & 계획

- **[docs/technical/API_SPEC.md](docs/technical/API_SPEC.md)** — REST API 명세 (Must/Should features)
- **[docs/technical/ERD.md](docs/technical/ERD.md)** — 데이터베이스 스키마
- **[docs/planning/REQUIREMENTS.md](docs/planning/REQUIREMENTS.md)** — 기능 요구사항 (§1-§6)
- **[docs/planning/FLOWCHART.md](docs/planning/FLOWCHART.md)** — 화면 흐름도 (Mermaid)
- **[docs/planning/USER_STORIES.md](docs/planning/USER_STORIES.md)** — 사용자 스토리 (Epic·US 맵핑)
- **[docs/planning/ROADMAP.md](docs/planning/ROADMAP.md)** — v1–v2 로드맵
- **[docs/qa/QA_FEEDBACK.md](docs/qa/QA_FEEDBACK.md)** — QA 피드백 & 결함
- **[docs/IMPLEMENTATION_STATUS.md](docs/IMPLEMENTATION_STATUS.md)** — 현재 구현 상태 스냅샷 ⭐ NEW

### 연구 & 벤치마크

- **[docs/planning/research/BENCHMARK_REPORT.md](docs/planning/research/BENCHMARK_REPORT.md)** — 경쟁사 기능 분석
- **[docs/planning/research/COMPETITOR_MATRIX.md](docs/planning/research/COMPETITOR_MATRIX.md)** — 케어포·이지케어·엔젤 비교

---

## 🛠️ 기술 스택

### 백엔드

```
Java Spring Boot 3.x
PostgreSQL 15+
Flyway (DB 마이그레이션)
JUnit 5 + Mockito (테스트)
```

### 프론트엔드

```
React 18.x (Vite SPA)
Tailwind CSS (스타일링)
React Router v6 (라우팅)
Vitest (단위 테스트)
Playwright (E2E 테스트)
```

### 인프라

```
Docker Compose (로컬 개발)
PostgreSQL 15
Redis (캐시 등)
Kubernetes (배포 준비 중)
```

---

## 🚀 로컬 개발 시작

### 1. 저장소 복제 & 서브모듈 초기화

```bash
git clone https://github.com/ogada/ogada.git
cd ogada
git submodule update --init --recursive
```

### 2. 환경 설정

```bash
# .env 파일 생성 (template: .env.example)
cp .env.example .env

# PostgreSQL, Redis 컨테이너 시작
docker-compose -f docker-compose.dev.yml up -d
```

### 3. 백엔드 빌드 & 실행

```bash
cd src/backend
mvn clean install -DskipTests
mvn spring-boot:run
```

**백엔드 기본 포트**: `http://localhost:8080`

### 4. 프론트엔드 개발 서버 시작

```bash
cd src/frontend
npm install
npm run dev
```

**프론트엔드 개발 서버**: `http://localhost:5173`

### 5. 테스트 실행

**백엔드 테스트**

```bash
cd src/backend
mvn test
```

**프론트엔드 테스트**

```bash
cd src/frontend
npm test                    # 단위 테스트
npm run test:e2e           # E2E 테스트
```

**⚠️ 주의**: 프론트엔드 Vitest는 한 번에 **1개만** 실행하세요. 자세한 내용은 `docs/qa/VITEST_CONCURRENCY.md`를 참고하세요.

---

## 🔑 주요 API 엔드포인트

### 인증

- `POST /api/v1/auth/login` — 로그인
- `POST /api/v1/auth/refresh` — 토큰 갱신
- `GET /api/v1/auth/me` — 현재 사용자 정보

### 이용자 관리

- `GET /api/v1/clients` — 이용자 목록
- `POST /api/v1/clients` — 이용자 등록
- `PATCH /api/v1/clients/{clientId}` — 이용자 수정

### 청구·정산

- `GET /api/v1/billing/claims` — 청구 목록
- `POST /api/v1/billing/claims` — 청구 생성
- `GET /api/v1/billing/reports/deposits` — 입금 대장

### 공단 연동

- `GET /api/v1/visits/imports/nhis/guidance` — NHIS import 안내 (Q731)
- `POST /api/v1/visits/imports/nhis` — NHIS 방문일정 동기화
- `GET /api/v1/visits/imports/nhis-caregivers/preview` — 요양보호사 excel import 미리보기

전체 API 스펙은 [`docs/technical/API_SPEC.md`](docs/technical/API_SPEC.md)를 참고하세요.

---

## 📊 아키텍처

### 데이터베이스 스키마

- **조직·지점 격리**: `organization_id`, `branch_id` 멀티테넌트
- **감사 추적**: `created_at`, `created_by`, `updated_at`, `updated_by`
- **데이터 보존**: PII 암호화, 감사 로그 유지 (자세히: `docs/ops/DATA_RETENTION_POLICY.md`)

Flyway 마이그레이션 이력: `V1–V183` (신규 DB 마이그레이션은 `V184`부터)

### 권한 제어 (RBAC)

| 역할 | 데이터 범위 | 주요 기능 |
|------|-----------|---------|
| `platform_admin` | 전국 Tenant 메타 | 신규 고객 등록, `hq_admin` 발급 |
| `hq_admin` | 자기 Tenant 전체 | 지점·직원·이용자·청구 관리 |
| `branch_admin` | 자신의 지점만 | 지점 운영, 이용자·출석 관리 |
| `caregiver` | 배정 이용자만 | 건강 기록, 출석 체크인 |
| `guardian` | 자신의 이용자만 | 기록 열람, QR 체크인 |

### 개발 워크플로우

```
main (stable)
 ├── origin/main (원격, protected)
 └── develop (작업 브랜치)
      ├── src/backend (submodule)
      ├── src/frontend (submodule)
      └── docs/ (마크다운 문서)

작업 순서:
1. develop에서 feature/fix 브랜치 생성
2. src/backend, src/frontend 각각 develop branch에서 코드 작성
3. 작업 완료 후 root docs/ 업데이트 (TWR — .agents/rules.md §6)
4. git commit (root + submodule)
5. PR → code review → merge to test → merge to main
```

자세한 git 워크플로우는 `.agents/agents.yaml`과 `.agents/rules.md` §6을 참고하세요.

---

## 📞 지원 & 문의

- **Slack**: #ogada-ops (팀 채널)
- **이슈 추적**: GitHub Issues
- **배포 지원**: DEPLOYMENT_GUIDE.md §10

---

## 📄 라이선스

TBD (조직 내부 정책에 따름)

---

**최종 갱신**: 2026-06-28 396차 baseline · `BE 7fcdfde` / `FE e19328a` · **Must ✅** · Merge gate **865+**
