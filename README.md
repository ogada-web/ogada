<!-- doc:owner=TWR doc:audience=DEV,PLN,UXD,COD,DBA updated=2026-06-16T02:00:00+09:00 -->

# ogada — 주간보호센터·요양기관 운영 시스템

> **og** (온수) + **ada** (따뜻한) — 따뜻한 돌봄의 디지털화

ogada는 **전국 주간보호센터·요양기관**을 위한 **B2B SaaS 멀티테넌트 웹 시스템**입니다.

이용자 관리, 출석(수기·QR B방식), 건강 기록, 청구·정산, 다지점 대시보드, 보호자 포털 등 일상 운영 업무를 클라우드 기반으로 지원합니다.

---

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

## 🚀 빠른 시작

### 사전 요구사항

- **Git** — `git clone` & 서브모듈 관리
- **Docker & Docker Compose** — 로컬 DB·Redis 컨테이너
- **Java 21+** — Spring Boot 3.x 컴파일·실행
- **Node.js 18+** — React 프론트엔드 번들링
- **Maven 3.9+** — 백엔드 빌드
- **npm 9+** — 프론트엔드 패키지 관리

### 로컬 개발 환경 구성

#### 1. 저장소 클론 (서브모듈 포함)

```bash
git clone --recursive https://github.com/yourorg/ogada.git
cd ogada
```

#### 2. 백엔드 설정

```bash
cd src/backend

# 환경변수 설정 (.env.example 참고)
cp .env.example .env

# PostgreSQL + Redis 시작 (Docker Compose)
docker-compose up -d

# Flyway 마이그레이션 + Spring Boot 실행
./mvnw clean spring-boot:run
# 또는 IDE에서 `OgadaApplication.main()` 실행
```

**Backend URL**: `http://localhost:8080`  
**Health Check**: `GET http://localhost:8080/api/v1/health`

#### 3. 프론트엔드 설정

```bash
cd src/frontend

# 의존성 설치
npm install

# 개발 서버 시작 (Vite)
npm run dev
```

**Frontend URL**: `http://localhost:5173` (자동 열림)

#### 4. 테스트 실행

**백엔드**:
```bash
cd src/backend
./mvnw clean test  # 단위·통합 테스트 (~5min)
```

**프론트엔드**:
```bash
cd src/frontend
npm run test       # Vitest 단위 테스트
npm run test:e2e   # Playwright E2E 테스트 (로컬 dev 서버 필요)
```

---

## 📂 프로젝트 구조

```
ogada/
├── README.md (this file)
├── docs/
│   ├── README.md
│   ├── ops/
│   │   ├── USER_MANUAL.md
│   │   ├── ADMIN_GUIDE.md
│   │   ├── FAQ.md
│   │   ├── DEPLOYMENT_GUIDE.md
│   │   └── CHANGELOG.md
│   ├── planning/
│   │   ├── REQUIREMENTS.md
│   │   ├── FLOWCHART.md
│   │   ├── USER_STORIES.md
│   │   ├── ROADMAP.md
│   │   └── research/
│   │       ├── BENCHMARK_REPORT.md
│   │       └── COMPETITOR_MATRIX.md
│   ├── technical/
│   │   ├── API_SPEC.md
│   │   └── ERD.md
│   ├── qa/
│   │   └── QA_FEEDBACK.md
│   ├── security/
│   │   └── (보안 정책 & 감시 로그)
│   └── IMPLEMENTATION_STATUS.md (⭐ 현재 구현 스냅샷)
├── src/
│   ├── backend/          # Spring Boot 백엔드 (서브모듈)
│   │   ├── src/
│   │   ├── pom.xml
│   │   ├── Dockerfile
│   │   └── docker-compose.yml
│   ├── frontend/         # React 프론트엔드 (서브모듈)
│   │   ├── src/
│   │   ├── package.json
│   │   ├── vite.config.js
│   │   └── Dockerfile
│   └── migrations/       # Flyway DB 스크립트 (공유)
├── scripts/              # 운영 스크립트
│   ├── run-agent.py      # 에이전트 실행
│   ├── git_merge_to_test.sh
│   └── ...
├── transfer/            # 파일럿 테스트 산출물
│   ├── backend/
│   ├── frontend/
│   └── ...
├── memory/
│   └── decisions.md      # 아키텍처·디자인 결정 이력
├── .agents/             # 에이전트 구성
│   ├── agents.yaml
│   ├── rules.md
│   ├── workspace_baseline.yaml
│   └── branches.yaml
└── tests/               # 테스트 리소스
    └── README.md
```

---

## 👥 역할 & 권한

| 역할 | 코드 | 범위 | 주요 업무 |
|------|------|------|----------|
| **플랫폼 관리자** | `platform_admin` | 전국(ogada 내부) | 신규 Tenant 등록, 첫 `hq_admin` 발급 |
| **통합 관리자** | `hq_admin` | 자기 Tenant | 다지점 통합 관리, 지점·직원·청구 |
| **지점장** | `branch_admin` | 자기 지점 | 지점 운영 총괄, 이용자·직원 관리 |
| **사회복지사** | `social_worker` | 자기 지점 | 이용자·건강 기록, 프로그램 관리 |
| **요양보호사** | `caregiver` | 자기 지점 | 수기 출석, 건강 기록 입력 |
| **보호자** | `guardian` | 연결 이용자 | 일일 기록 열람, 청구 명세, QR 체크인 |
| **이용자 본인** | `client_user` | 자신 | 출석 현황, 기록 조회, QR 체크인(옵션) |
| **시스템 관리자** | `sysadmin` | 자기 Tenant | 기술 설정, 백업, 감시 로그 |

---

## 🔒 보안

### 핵심 정책

- **테넌트 격리**: 모든 쿼리에 `organization_id` 필수. 테넌트 간 데이터 접근 불가.
- **역할 기반 접근 제어(RBAC)**: JWT의 `role`, `branch_ids` 검증. 비인증 요청 `401`, 권한 없음 `403`.
- **민감정보 암호화**: 주민등록번호, 연락처 → 저장 시 암호화, 응답·로그 시 마스킹.
- **환경변수 관리**: API 키·DB 비밀번호 → `.env` (깃 무시) + 배포 환경 시크릿 주입.
- **SQL 인젝션 방지**: 파라미터 바인딩·ORM(`JPA`) 우선. 원본 SQL 금지.

자세한 보안 가이드는 [ADMIN_GUIDE.md §2](docs/ops/ADMIN_GUIDE.md)를 참고하세요.

---

## 📞 지원 & 피드백

- **문서 오류/개선 제안**: [GitHub Issues](https://github.com/yourorg/ogada/issues)
- **기술 지원**: [Discord Community](https://discord.gg/yourserver) 또는 ogada 지원팀
- **보안 취약점 신고**: security@ogada.kr (절대 공개 이슈 금지)

---

## 📄 라이선스

Proprietary — ogada 저작권 보유. 허가 없이 복제·수정·배포 금지.

---

## 🙏 감사

- **UI/UX**: Tailwind CSS, Recharts, React Router
- **DB**: PostgreSQL, Flyway
- **테스트**: JUnit, Vitest, Playwright
- **CI/CD**: GitHub Actions

---

**최종 갱신**: 2026-06-16  
**현재 버전**: v1 (MVP)  
**개발 branch**: `develop`  
**배포 branch**: `operation` (→ production)

문서 소유자: `tech_writer` (`TWR`)
