<!-- doc:owner=TWR doc:audience=PLN,COD,TSR,UXD,DBA,BNK updated=2026-06-21T08:48:00+09:00 -->
# ogada 운영 문서 (docs/ops/)

> **작성**: tech_writer 에이전트  
> **생성일**: 2026-06-13  
> **상태**: MVP v1 개발 중 — **290차 자동 동기화 완료** (BE `0c9518a`·FE `580a86b`·V1–V166·108 route·87 page·G21 dashboard NHIS gap ✅·G15 Kakao quota widget ✅·merge gate 614)  
> **최종 갱신**: 2026-06-21 (291차 TWR — README §6-§7 동기화, 스테이 사항 최신화)

---

## 📚 문서 네비게이션

이 디렉토리(`docs/ops/`)는 ogada 도입·운영·관리를 위한 **실무 문서**를 제공합니다.  
역할·목적별로 읽을 문서를 아래에서 선택하세요.

---

## 1. 새로운 고객사·센터를 위한 문서

### 🚀 **DEPLOYMENT_GUIDE.md** — 배포·인프라·초기 설정

**대상**: DevOps, IT 인프라 담당자

**포함 내용**:
- 클라우드 배포 환경 설정 (Docker, PostgreSQL, Spring Boot 실행)
- 데이터베이스 마이그레이션 (Flyway V1–V166, G21 NHIS 비교·G32 케이스관리·G42 민원상담 스키마)
- 환경 변수·시크릿 관리 (API 키, JWT 시크릿, Kakao 배차 API, CMS 연동)
- SSL/HTTPS 설정
- 모니터링·로그 수집
- 백업·복구

**최신 항목** (2026-06-21, 290차):
- **Q594** — **G21 NHIS 비교 갭** — 대시보드 StatCard — `nhisComparisonGapCount` 위젯
- **Q595** — **G15 카카오 API 잔여** — HQ 통합 관리자 대시보드 — `transportKakaoQuotaSummary` widget
- **Q596** — **live E2E bootstrap-error blocker** — 파생 seed/schema blocker 생략
- **Q597** — **live E2E cash-receipt guard** — 현금영수증 suite 게이트

**관련 링크**: FAQ §Q594–Q597 · API_SPEC §9-16/9-17/9-18 · REQUIREMENTS §7-2·§7-8·§3-13

---

## 2. 현장 사용자 (센터장·요양보호사·사회복지사·보호자)

### 📖 **USER_MANUAL.md** — 일상 사용 절차서

**대상**: 센터장(`branch_admin`), 요양보호사(`caregiver`), 사회복지사(`social_worker`), 보호자(`guardian`)

**포함 내용**:
- 로그인·계정 관리
- 역할별 홈 화면·메뉴 구조
- **이용자 관리**: 등록, 상세 프로필(§2-2 기본정보·컬럼 설명)
- **출석 관리**: 수기 체크인/아웃, **QR B방식 셀프 스캔** (보호자 동반 도착/귀가)
- **건강 기록**: 일일 체크(혈압·체온·혈당·산소포화도), 투약, 특이사항, 이력 조회
- **청구·정산**: 수가표 관리, 월별 청구서 생성, 본인부담금 계산, **NHIS 엑셀 import**
- **대시보드**: 지점별·통합 현황·통계

**최신 항목** (2026-06-21, 290차):
- **Q594** — **G21 NHIS 비교 갭** — 지점 대시보드 통계 위젯 — 공단 일정 미등록/불일치 통계
- **Q595** — **G15 카카오 API 잔여** — HQ 관리자 대시보드 — 배차 API 호출량 모니터링
- **Q551** — **보호자 인증 blocker 분리** — guardian-credentials-missing vs default
- **Q550** — **수동 배차 개선** — 이전 배차 불러오기 · 희망 시각 경고

**사용 시나리오**:
1. 현금 수납 입력 → 자동 표시 **발급 Modal**에서 NTS 발급번호 입력 (Q531)
2. 아침 대시보드에서 **「발급 지연」** 1건 이상 → **우선 처리** (Q532)
3. 작년분 청구 발급 시 **warning Alert** 확인 (Q533)
4. HQ 관리자 → **`/billing/cash-receipts`** 전 지점 미발급·지연 한눈에 확인 (Q533)
5. **G21 지점** → 대시보드 **「공단 일정 불일치」** StatCard로 미등록 방문 확인 (Q594)

**관련 링크**: FAQ.md Q530–Q535·Q594–Q597 · API_SPEC G-CASH-RECEIPT-LOG·G21 dashboard · ADMIN_GUIDE §1-4·§10-4

---

## 3. 센터 운영/IT 담당 (통합 관리자·시스템 관리자)

### 🛠️ **ADMIN_GUIDE.md** — 플랫폼·계정·기술 관리

**대상**: 통합 관리자(`hq_admin`), 시스템 관리자(`sysadmin`)

**포함 내용**:
- **계정 관리**: 직원 계정 생성·역할 배정, 비밀번호 초기화
- **지점 관리**: 다지점 설정, 지점별 관리자 배정
- **청구·정산 설정**:
  - 수가표 관리 (등급별·연도별, **G9-COG 인지지원 5칸** + 표준 25칸)
  - 본인부담률 설정 (4구분: GENERAL/REDUCED_40/REDUCED_60/MEDICAID)
  - 청구시작 기준금액(G33) 설정 (선납/미납 반영)
  - NHIS 엑셀 import & reconciliation
- **기술 설정**: 백업, 감사 로그, API 키, LDAP 연동
- **보안 정책**: 세션 타임아웃, IP 화이트리스트, 로그인 이력
- **V166 DB 스키마**: `ltc_grade`, `grievance_counseling_records`, `case_management_records` 등

**최신 항목** (2026-06-21, 290차):
- **G21 NHIS 비교** — 대시보드 widget · 공단 일정 미등록/불일치 통계 (Q594)
- **G15 Kakao quota** — HQ 대시보드 widget · API 호출량 모니터링 (Q595)
- **G32 사례관리** — 보호자별 의견 기록 · 다중 선택 · V165 (Q520)
- **live E2E bootstrap blocker** — 파생 blocker 생략 · 신뢰성 향상 (Q596)

**운영 체크리스트**:
1. 신규 Tenant 개통 → `platform_admin` 역할 필요 (별도)
2. 첫 `hq_admin` 계정 발급 후 지점·수가표 설정 → ADMIN_GUIDE §1–§3
3. 월말 청구 전 NHIS import & reconciliation → ADMIN_GUIDE §6-3·FAQ Q264
4. 현금 수납 입력 후 **현금영수증 발급 이력 등록** → `/billing/cash-receipts` (Q530·Q531)
5. 아침 대시보드 **「발급 지연」** 확인 (Q532)

**관련 링크**: FAQ Q530–Q533 · API_SPEC G-CASH-RECEIPT-LOG·G32 · DEPLOYMENT_GUIDE §1-3

---

## 4. 자주 묻는 질문 & 빠른 답변

### ❓ **FAQ.md** — Q&A 색인 (590+ 항목)

**대상**: 모든 사용자 (현장·운영·기술·플랫폼)

**구성**:
- **§1–§10**: 서비스 개요, 계정, 역할, 기능별 FAQ
- **§11–§20**: 청구·정산, 공단·NHIS, 보호자, 배차, 청구 리포트 등
- **§21+**: 최신 기능 (인지지원·CMS·고충상담·HR lifecycle·G21 NHIS·G15 배차·G32 사례관리·G42 민원상담 등)

**최신 엔트리** (2026-06-21, 290차):
- **Q594**: **G21 NHIS 비교 갭** — 대시보드 StatCard · `nhisComparisonGapCount` widget
- **Q595**: **G15 카카오 API 잔여** — HQ dashboard · `transportKakaoQuotaSummary` widget
- **Q596**: **live E2E bootstrap-error** — 파생 seed/schema blocker 생략
- **Q597**: **live E2E cash-receipt** — `liveCashReceiptDescribe` suite guard
- **Q589**: **Must 갭: 출석 roster API** — 확정 필요 (coder 백로그)
- **Q590**: **Must 갭: QR 생성 payload·이미지** — 확정 필요 (coder 백로그)
- **Q587**: **G-BILLING appliedFilters** — 필터 현황 echo (closure)
- **Q588**: **UXD-148 billing report a11y** — aria-live·aria-busy (closure)

**사용 팁**:
- 현금영수증 관련 → Q530–Q535 참고
- G32 사례관리 관련 → Q516–Q523 참고
- G21 NHIS 비교 → Q594 참고
- G15 배차 및 Kakao → Q595 참고
- 기능 찾기 → Ctrl+F로 검색 (예: "CASH", "attendee", "대시보드", "NHIS", "Kakao")
- "P2 Planned" / "P3 out-of-scope" = ROADMAP.md 참고

**최근 엔트리 (2026-06-21, 290차)** — Q594–Q597 신규 추가·Q587–Q590 갱신·"Must 갭" 명시

---

## 5. 기술 정보 & 설계

### 📋 **REQUIREMENTS.md** — 요구사항 명세 (기획·설계 문서)

**대상**: 기획자, 개발자, QA

**포함 내용**:
- 프로젝트 개요, 기술 스택, 사업 모델
- 7개 역할 정의 & RBAC 규칙
- 기능 요구사항 (이용자·출석·건강·청구·배차 등)
- MVP v1 범위, 로드맵 (v2, v3, v3.1)
- 벤치마킹 (케어포·이지케어·엔젤·공단)

**관련 링크**: `docs/planning/FLOWCHART.md` · `docs/technical/API_SPEC.md` · `docs/planning/USER_STORIES.md`

---

### 🏗️ **CHANGELOG.md** — 버전 변경 이력

**대상**: 개발자, QA, 기획자 (구현 진전 추적)

**구성**:
- `[Unreleased]`: 현재 개발 중 (v1 Must 기능 + P2 Planned)
- `[0.0.1]`: v1 RC (마지막 테스트)
- `[0.0.0]`: 초기 설계

**최신** (2026-06-13):
- BE `8bb6583` · FE `a5c2736` · V99 DB
- **902/902 `mvn test` PASS** · **1022/1022 Vitest PASS**
- **merge gate FULLY UNBLOCKED**
- **14개 P2 Planned** 항목 (FAQ21824 wizard·G34 SMS·건강검진 파일함 등)

---

## 6. 문서 상태 & 구현 진행도

### 현재 상태 (2026-06-21, 290차, develop HEAD `0c9518a`/`580a86b`, V1–V166)

| 문서 | 상태 | 마지막 갱신 | 커버리지 |
|------|------|-----------|---------|
| **USER_MANUAL.md** | ✅ 현행 | 2026-06-13 (143차) | MVP Must + G9-COG 인지지원 + Q309-Q313 최신화 |
| **FAQ.md** | ✅ 현행 | 2026-06-13 (143차) | 315+ Q&A · Q309-Q313 Fixed · **P2 Planned 14개 명시** |
| **ADMIN_GUIDE.md** | ✅ 현행 | 2026-06-13 (최근) | V99 마이그레이션 · G42 pending-approval · US-R03 lifecycle · G2 CMS · **14개 P2 갭 명시** |
| **DEPLOYMENT_GUIDE.md** | ✅ 현행 | 2026-06-13 (최근) | V99 마이그레이션 · ENV 설정 · LCMS/CMS 연동 · 모니터링 |
| **CHANGELOG.md** | ✅ 현행 | 2026-06-13 (143차) | BE `8bb6583`·FE `a5c2736` · V99 · **902/1022 PASS** · merge gate FULLY UNBLOCKED |
| **README.md** (본 문서) | 🆕 신규 | 2026-06-13 | 문서 네비게이션 · 역할별 가이드 · 최신 진행도 |

---

### 구현 커버리지

| 영역 | 상태 | 비고 |
|------|------|------|
| **백엔드 API** | 78.28% | Must + G9-COG + G42 + G34b + G40b + G40 + FAQ21806 + G2 + US-R03/R02 · **902/902 test PASS** |
| **데이터베이스** | V99 | `ltc_grade` 0–5 · `grievance_counseling_records` · V93–V99 마이그레이션 완료 |
| **프론트엔드** | 65 라우트 | G9-COPAY-NAMING + FAQ21824 + G9-COG 30칸 + Q309-Q313 반영 · **1022/1022 test PASS** |
| **문서화** | Must + P2 갭 | USER_MANUAL·FAQ·ADMIN_GUIDE·DEPLOYMENT 최신화 · **P2 Planned 14개 명시** |

---

## 7. 로드맵 & 다음 단계

### v1.2.1 현황 (2026-06-13)

**완료**:
- ✅ G9-COG 인지지원등급 수가 (30칸 수가표, import gate)
- ✅ Q309–Q313 최신화 (정식 용어, workflow, lifecycle)
- ✅ 902/1022 test PASS · **merge gate FULLY UNBLOCKED**

**P2 Planned** (이후 버전):
- FAQ21824 **단일 wizard** — 계약→청구 자동화
- 건강검진 **결과통보서 파일함** — PDF 저장소
- **LCMS CMS 3-method** — 가상계좌·카드·다계좌
- **G34 SMS live OTP** — 전자결재 인증
- **G42 결재함 UI** — pending-approval 전용 화면
- G-Payroll 직원 급여 관리 (v3)

**자세히**: [ROADMAP.md](../planning/ROADMAP.md) 참고

---

## 8. 추가 자료

### 기획·설계 문서
- **REQUIREMENTS.md** — 요구사항 전문
- **FLOWCHART.md** — 화면 흐름도
- **USER_STORIES.md** — Epic별 사용자 스토리
- **PLAN_NOTES.md** — 설계 의사결정 이력

### 기술 문서
- **API_SPEC.md** — REST API 상세 명세
- **ERD.md** — 데이터베이스 엔티티 관계도

### 벤치마킹·연구
- **BENCHMARK_REPORT.md** — 경쟁사 분석
- **COMPETITOR_MATRIX.md** — 케어포·이지케어·엔젤 기능 비교

---

## 🎯 도움말

**Q. 어느 문서를 먼저 읽어야 하나요?**

| 상황 | 추천 순서 |
|------|---------|
| 신규 센터 도입 | DEPLOYMENT_GUIDE.md → USER_MANUAL.md → FAQ.md |
| 센터 관리자 | ADMIN_GUIDE.md → USER_MANUAL.md (§8) → FAQ.md (§3–§8) |
| 현장 직원 | USER_MANUAL.md → FAQ.md |
| 개발자 | REQUIREMENTS.md → API_SPEC.md → DEPLOYMENT_GUIDE.md |
| 기능 찾기 | FAQ.md Ctrl+F 검색 |

**Q. "P2 Planned"가 무엇인가요?**

아직 구현되지 않은 예정 기능입니다. 다음 버전에서 추가될 예정입니다. 자세히는 각 문서의 **P2 섹션** 또는 FAQ.md에서 검색하세요.

**Q. 최신 정보는 어디서 확인하나요?**

- **구현 진전**: CHANGELOG.md `[Unreleased]` 섹션
- **개발 상태**: 각 문서 최상단 메타 (`updated=` 날짜 확인)
- **의사결정 이력**: PLAN_NOTES.md

---

## 문서 소유 & 연락처

| 역할 | 담당자 | 역할 | 채널 |
|------|--------|-----|------|
| 문서 작성·갱신 | TWR (tech_writer) | 모든 ops 문서 | GitHub Issues · PLAN_NOTES.md |
| 기획·설계 | PLN (planner) | REQUIREMENTS.md, ROADMAP.md | GitHub Issues · 의사결정 기록 |
| 코드·API | COD (coder) | API_SPEC.md, 구현 상태 | 커밋 메시지 · 테스트 결과 |
| 운영·배포 | TSR (tester/operator) | DEPLOYMENT_GUIDE.md 재검증 | 배포 결과 · 로그 |

---

*Last updated: 2026-06-13 by tech_writer (TWR) — ogada v1 개발 중*
