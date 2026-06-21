<!-- doc:owner=TWR doc:audience=PLN,COD,UXD,DBA updated=2026-06-21T08:48:00+09:00 -->

# ogada 문서 계층 (docs/)

> **최종 갱신**: 2026-06-21 (290차 — TWR 동기화 · BE `0c9518a` / FE `580a86b` · V1–V166·108 route·87 page·merge gate 614)  
> **작성**: tech_writer  
> **대상**: 기획자, 개발자, UX 설계자, 운영자  
> **주요 업데이트**: ops 문서 모두 290차 동기화·G21 NHIS dashboard·G15 Kakao quota·G32 사례관리·G42 민원상담 반영·API_SPEC resync 진행 중

---

## 📚 문서 구조

```
docs/
├── README.md                      ← 이 파일 (문서 계층 안내)
│
├── planning/                      ← 기획·설계 산출물 (기획자/개발자)
│   ├── REQUIREMENTS.md            ← ⭐ Must 기능 명세 (기본 읽을거리)
│   ├── USER_STORIES.md            ← 사용자 스토리 (Epic A–M)
│   ├── FLOWCHART.md               ← 역할별 화면 흐름도
│   ├── ROADMAP.md                 ← 릴리스 계획 (v1/v1.1/v1.2...)
│   ├── PLAN_NOTES.md              ← 기획 회고·의사결정·Q&A (플래너 관리)
│   └── research/
│       ├── BENCHMARK_REPORT.md    ← 경쟁사 조사 (케어포/이지케어)
│       └── COMPETITOR_MATRIX.md   ← 기능 비교표
│
├── technical/                     ← 기술 설계 (개발자)
│   ├── API_SPEC.md                ← ⭐ REST API 명세 (`/api/v1/*` 전체)
│   ├── ERD.md                     ← 데이터 모델 (ER 다이어그램)
│   ├── FLOWCHART.md               ← 기술 흐름도 (인증·출석·청구)
│   └── (미포함) 아키텍처 가이드 — DEPLOYMENT_GUIDE.md §1-3 참고
│
├── ops/                           ← 운영 문서 (운영자/현장 사용자)
│   ├── USER_MANUAL.md             ← ⭐ 현장 사용 가이드 (필수 읽을거리)
│   ├── ADMIN_GUIDE.md             ← 시스템·플랫폼 관리자 가이드
│   ├── DEPLOYMENT_GUIDE.md        ← ⭐ 배포·마이그레이션 가이드
│   ├── DEV_ACCOUNTS.md            ← 로컬·스테이징 테스트 계정 (역할별)
│   ├── FAQ.md                     ← 자주 묻는 질문 (149개, 기술·운영 혼합)
│   ├── CHANGELOG.md               ← 버전별 변경 이력 (Keep a Changelog 형식)
│   ├── DATA_RETENTION_POLICY.md   ← 데이터 보관·파기 정책
│   └── README.md                  ← ops/ 폴더별 가이드 (선택 읽을거리)
│
├── product/                       ← 프로덕트·디자인 (UX/UI)
│   ├── DESIGN_SYSTEM.md           ← 디자인 시스템 (색·타이포·컴포넌트)
│   └── (미포함) 프로토타입·스크린샷 — 향후 추가
│
├── qa/                            ← QA·테스트 (테스터/개발자)
│   ├── QA_FEEDBACK.md             ← QA 피드백·버그 목록
│   ├── TEST_REPORT.md             ← 테스트 결과 리포트
│   ├── VITEST_CONCURRENCY.md      ← ⭐ Vitest 동시 실행 방지 (에이전트·개발자 필독)
│   └── (미포함) 테스트 케이스 — 향후 추가
│
├── security/                      ← 보안 (보안 담당/CISO)
│   ├── THREAT_MODEL.md            ← 위협 모델 (STRIDE)
│   ├── SECURITY_AUDIT.md          ← 보안 감시 체크리스트
│   ├── SECURITY_CHECKLIST.md      ← 구현 보안 체크리스트
│   └── (미포함) 침투 테스트 리포트
│
└── AGENT_USAGE.md                 ← 에이전트 역할·협업 규칙
```

---

## 🎯 역할별 필독 문서

### 👥 **사용자 (현장 센터 직원·보호자)**
1. **`ops/USER_MANUAL.md`** — 로그인, 이용자 등록, 출석, 건강 기록, 청구 조회 등 **일상 업무 절차**
2. **`ops/FAQ.md`** (선택) — 자주 묻는 기술/운영 질문

### 📋 **기획자 (planner)**
1. **`planning/REQUIREMENTS.md`** — 기능 요구사항, 7역할 RBAC, 청구·정산 명세 **필독**
2. **`planning/ROADMAP.md`** — v1/v1.1/v1.2 릴리스 계획
3. **`planning/USER_STORIES.md`** — Epic별 사용자 스토리
4. **`planning/PLAN_NOTES.md`** — 의사결정 이력, 미확정 사항

### 👨‍💻 **개발자 (backend/frontend/devops)**
1. **`technical/API_SPEC.md`** — REST API 명세 (`/api/v1/*` 전체) **필독**
2. **`ops/DEPLOYMENT_GUIDE.md`** — 로컬 환경 구성, 환경변수, DB 마이그레이션 **필독**
3. **`ops/DEV_ACCOUNTS.md`** — 로컬·스테이징 테스트 계정 (역할별 이메일·비밀번호)
4. **`qa/VITEST_CONCURRENCY.md`** — `npm test` 동시 실행 금지·정리 방법 **필독** (에이전트 환경)
5. **`planning/REQUIREMENTS.md`** (선택) — 비기능 요구사항 (보안, 성능)
6. **`ops/FAQ.md`** (선택) — API 경로 불일치, 구현 상태 관련 Q&A

### 🎨 **UX/UI 설계자 (ux_designer)**
1. **`product/DESIGN_SYSTEM.md`** — 디자인 시스템, 컴포넌트 **필독**
2. **`planning/FLOWCHART.md`** — 역할별 화면 흐름도
3. **`planning/USER_STORIES.md`** (선택) — 화면별 사용자 스토리

### 🔒 **보안 담당 (CISO/security team)**
1. **`security/SECURITY_CHECKLIST.md`** — 구현 보안 체크리스트 **필독**
2. **`security/THREAT_MODEL.md`** — 위협 모델 분석
3. **`ops/DEPLOYMENT_GUIDE.md` §2–§3** — 시크릿 관리, 암호화 설정

### 🛠️ **운영자 (platform_admin / sysadmin)**
1. **`ops/DEPLOYMENT_GUIDE.md`** — 배포, 환경 구성 **필독**
2. **`ops/ADMIN_GUIDE.md`** — Tenant 온보딩, RBAC 설정, 모니터링
3. **`ops/DATA_RETENTION_POLICY.md`** — 데이터 보관·파기 정책
4. **`ops/FAQ.md`** (선택) — 기술 트러블슈팅

---

## 📝 문서별 상세 설명

| 문서 | 대상 | 범위 | 상태 |
|------|------|------|------|
| **REQUIREMENTS.md** | 기획/개발 | Must 기능, RBAC, 청구·정산, 비기능 요구사항 | ✅ 완료 (46차 갱신) |
| **API_SPEC.md** | 개발 | REST `/api/v1/*` 전체, 인증, NHIS import, 대사, G17/G32/G42 케이스관리 | ✅ 완료 (248차 갱신 — **G17/G32/G42 3개 섹션 추가**) |
| **USER_MANUAL.md** | 사용자/개발 | 로그인~월말 청구, 역할별 업무 절차 | ✅ 완료 (30차 갱신) |
| **DEPLOYMENT_GUIDE.md** | 개발/운영 | 로컬 환경, 배포, 환경변수, **V43–V44** | ✅ 완료 (31차 갱신) |
| **ADMIN_GUIDE.md** | 운영 | Tenant 관리, 지점 설정, 백업, 감사 | ✅ 완료 (30차 갱신) |
| **FAQ.md** | 전역 | 590+ 기술·운영 Q&A · Q594–Q597 신규 · Must 갭 명시 (Q589–Q590) | ✅ 완료 (290차 갱신, Q594–Q597 포함) |
| **ROADMAP.md** | 기획/개발 | v1/v1.1/v1.2 릴리스 계획, 우선순위 | ✅ 완료 |
| **PLAN_NOTES.md** | 기획 | 의사결정, Q&A, 미확정 사항 | ✅ 관리 중 |
| **DESIGN_SYSTEM.md** | UX/개발 | 디자인 토큰, 컴포넌트, 접근성 | ✅ 완료 |
| **CHANGELOG.md** | 개발/운영 | 버전별 변경 (Keep a Changelog) | ✅ 완료 (30차 갱신) |
| **SECURITY_CHECKLIST.md** | 보안/개발 | 구현 보안 체크리스트 | ✅ 완료 |
| **ERD.md** | 개발/DBA | 데이터 모델, Flyway V1–V44 | ✅ 완료 |

> 상태: ✅ = 현재 구현 상태 동기화 완료 (2026-06-08)

---

## 🚀 시작하기

### 1️⃣ **처음 오시는 분?**
→ **`REQUIREMENTS.md`** + **`USER_MANUAL.md`** 부터 읽으세요.

### 2️⃣ **개발 환경 구성**
→ **`DEPLOYMENT_GUIDE.md` §3**에서 로컬 환경 설정 + **`API_SPEC.md`** REST 엔드포인트 확인.

### 3️⃣ **특정 기능 찾기**
→ **`FAQ.md`** 에서 키워드 검색 (예: "QR", "출석", "청구", "배차") — **172개 Q&A** 포함 (2026-06-08 49차).

### 4️⃣ **배포·운영 준비**
→ **`DEPLOYMENT_GUIDE.md`** + **`ADMIN_GUIDE.md`** + **`DATA_RETENTION_POLICY.md`** 순서.

---

## 📌 현재 구현 상태 스냅샷 (2026-06-08 develop HEAD `c7941e9` / frontend `1d910c2`)

| 영역 | 상태 | 상세 |
|------|------|------|
| **백엔드** | ✅ Must + v1.1 | REST API Must + **V41–V44** (보호자 초대, 알림, 휴대폰 암호화). **`mvn test` 152/152 PASS**. J03 Solapi 옵션. |
| **프론트엔드** | ✅ Must API baseline | `App.jsx` **14 라우트**, JWT 메모리 전용. Vitest **11파일/40건**. P1–P8·J01·J02 연동. **`/platform`·`/settings`만 `ModulePage`**. |
| **DB** | ✅ V1–V44 | Flyway 자동 마이그레이션. V43 보호자 초대, V44 휴대폰 암호화. |
| **문서** | ✅ 동기화 완료 | REQUIREMENTS·API_SPEC·USER_MANUAL·DEPLOYMENT·ADMIN_GUIDE·FAQ·CHANGELOG 모두 최신화. |

---

## 🔗 관련 링크

- **Git 저장소**: `/home/ubuntu/ogada`
- **백엔드**: `src/backend/` (Spring Boot 3.x, Java 17)
- **프론트엔드**: `src/frontend/` (React 18 + Vite 6)
- **에이전트 규칙**: `.agents/rules.md` (범용 코딩 규칙)

---

## ❓ 질문·피드백

1. **기획 관련**: `docs/planning/PLAN_NOTES.md` **「추가 질문」** 섹션
2. **기술 관련**: `docs/ops/FAQ.md` — 149개 기술 Q&A 검색
3. **보안 관련**: `docs/security/SECURITY_CHECKLIST.md`

---

*이 문서는 tech_writer 에이전트가 관리합니다. 새 문서 추가 시 이 README를 함께 갱신하세요.*
