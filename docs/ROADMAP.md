# ogada 구현 로드맵

> **작성·유지**: `planner`  
> **구현**: `coder`는 `status: in_progress` 버전 **하나만** 작업  
> **검증**: `tester`는 `merge_status: merged` 이후 `test` 브랜치에서 검증  
> **피드백**: `tester` → `docs/QA_FEEDBACK.md` → `planner` 반영 → `coder` 수정

---

## 버전 상태 값

| 필드 | 값 | 의미 |
|------|-----|------|
| `status` | `planned` / `in_progress` / `done` | 구현 진행 상태 |
| `merge_status` | `pending` / `ready` / `merged` | develop → test merge 준비 |

**merge 규칙**: coder가 해당 버전 **완료 기준을 모두 충족**하면 `merge_status: ready`로 변경 → 다음 build 시 `develop`이 자동으로 `test`에 merge → `merged`로 갱신.

---

## v1 — MVP 핵심 (Must)

- **status**: in_progress
- **merge_status**: pending
- **stream**: backend
- **목표**: 인증·다지점·이용자·출석·건강·청구·대시보드 (REQUIREMENTS §6 Must)

### 범위

1. Spring Boot + PostgreSQL + Flyway 멀티테넌트 골격
2. JWT + 6역할 RBAC + 지점 스코프
3. 이용자 CRUD, 출석(수기+QR), 건강 기록
4. 청구·정산(내부계산 + NHIS import reconciliation)
5. HQ/지점 대시보드 실데이터

### 완료 기준

- [ ] `src/backend` Maven test 전체 PASS
- [ ] API_SPEC Must 엔드포인트 구현 (인증·이용자·출석·건강·청구·대시보드)
- [ ] Flyway 마이그레이션 ERD와 정합
- [ ] 6역할 로그인·메뉴·권한 분리
- [ ] REQUIREMENTS §6 Must 체크리스트 충족

### test merge

- develop 완료 후 coder가 위 체크리스트를 `[x]`로 표시하고 `merge_status: ready` 설정

---

## v1.1 — 프론트엔드 MVP

- **status**: planned
- **merge_status**: pending
- **stream**: frontend
- **목표**: React SPA — 로그인·이용자·출석·건강·청구·대시보드 화면

### 범위

1. Vite+React SPA, JWT 클라이언트, 역할별 라우팅
2. 이용자·출석·건강·청구 UI (API_SPEC 연동)
3. HQ/지점 대시보드 차트·집계

### 완료 기준

- [ ] `npm run build` 성공
- [ ] 6역할 화면·메뉴·권한 분리
- [ ] Must 화면 API 연동 E2E 수동 시나리오 PASS

---

## v2 — 보호자·알림·결제

- **status**: planned
- **merge_status**: pending
- **stream**: backend
- **목표**: 보호자 풀 포털, 알림톡/SMS, CMS·간편결제 (REQUIREMENTS Should/Could)

### 범위

1. 보호자 포털 (명세·기록 열람)
2. 알림 채널 연동 (카카오/SMS)
3. 본인부담금 CMS·간편결제

### 완료 기준

- [ ] USER_STORIES 보호자·알림 스토리 구현
- [ ] QA_FEEDBACK v2 범위 항목 0건 OPEN

---

## v3 — 확장 모듈

- **status**: planned
- **merge_status**: pending
- **stream**: backend
- **목표**: 식사·프로그램·직원·서류 자동 생성

### 범위

- Should/Could 모듈 (REQUIREMENTS §6)

### 완료 기준

- [ ] planner·REQUIREMENTS v3 범위 확정 후 갱신

---

## 변경 이력

| 날짜 | 변경 |
|------|------|
| 2026-06-06 | 초안 — v1~v3 단계 분리, merge_status 규칙 정의 |
