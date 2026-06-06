<!-- doc:owner=PLN doc:audience=COD,TSR,UXD,DBA,BNK,TWR updated=2026-06-06T19:00:00+09:00 -->
# ogada 구현 로드맵

> **작성·유지**: `planner`  
> **구현**: `coder`는 `status: in_progress` 버전 **하나만** 작업  
> **검증**: `tester`는 `merge_status: merged` 이후 `test` 브랜치에서 검증  
> **피드백**: `tester` → `docs/QA_FEEDBACK.md` → `planner` 반영 → `coder` 수정  
> **벤치마크 입력**: `docs/BENCHMARK_REPORT.md`, `docs/COMPETITOR_MATRIX.md`, `memory/decisions.md`

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
- **목표**: 인증·다지점·이용자·출석·건강·청구(reconciliation 포함)·대시보드 (REQUIREMENTS §6 Must)
- **벤치마크 기준**: 케어포 2단계 청구(내부계산 + 롱텀 + 엑셀 import + 본인부담) — `BENCHMARK_REPORT.md` §4-1; NHIS 엑셀 **`처리상태` 선행열 스킵·정규화** (3차 §4-1 C-1)

### 범위

1. Spring Boot + PostgreSQL + Flyway 멀티테넌트 골격 (`platform_admin` Tenant 개통 — 경쟁사 대비 차별화)
2. JWT + **7역할** RBAC + 지점 스코프 + Branch Switcher
3. 이용자 CRUD(주민번호 암호화·copay 구분), 출석(수기+QR B), 건강 기록
4. 청구·정산: 수가표 B·copay·월별 명세 + **NHIS 엑셀 import + reconciliation UI** (`MATCHED`/`DISCREPANCY`/`UNMATCHED`)
5. HQ/지점 대시보드 실데이터 (다지점 HQ — 경쟁사 공개 자료 동등 기능 미확인, 파일럿 핵심)

### 구현 우선순위 (v1 내부 — REQUIREMENTS §6-2)

| 단계 | 범위 | 완료 신호 |
|------|------|----------|
| **P0** | Tenant·Branch·7역할·출석(수기)·건강·청구(수가·copay·명세·NHIS import·**`처리상태`열 정규화**)·대시보드 | 파일럿 1주차 — `branch_admin`+`caregiver` E2E |
| **P1** | QR B + `guardian`/`client_user` + **NHIS reconciliation UI** | 케어포 4단계 UX 동등 (US-G06) |
| **P2** | 보호자 **기록 열람**(알림 없음) + 청구 `?status=` 필터 | v1 백엔드 — G1·G8 **초대·명세**는 v1.1 |
| **P3** | — (Should 모듈) | v1.1로 이관 |

> P0 완료 전 P1 착수 금지 (품질·차별화 우선 — 결정 18).

### 완료 기준

- [ ] `src/backend` Maven test 전체 PASS
- [ ] API_SPEC Must 엔드포인트 구현 (인증·이용자·출석·건강·청구·**NHIS reconciliation**·대시보드)
- [ ] Flyway 마이그레이션 ERD와 정합 (V19+ reconciliation 제약 포함)
- [ ] **7역할** 로그인·메뉴·권한 분리 (`platform_admin` 포함)
- [ ] NHIS import: 배치 상세·수동 매칭(`PATCH .../rows/{id}/match`)·지점 일치 검증·**`처리상태` 선행열 스킵 파서**
- [ ] 롱텀 2026 export 안내: Chrome/Edge 필수(IE 불가) — import UI·온보딩 가이드
- [ ] REQUIREMENTS §6 Must·§6-2 P0–P1 체크리스트 충족
- [ ] USER_STORIES 파일럿 체크리스트 P1–P8 PASS (수기 출석·월말 청구·**reconciliation**)

### test merge

- develop 완료 후 coder가 위 체크리스트를 `[x]`로 표시하고 `merge_status: ready` 설정

---

## v1.1 — 프론트엔드 MVP + 보호자 확장

- **status**: planned
- **merge_status**: pending
- **stream**: frontend
- **목표**: React SPA — v1 백엔드 API 전면 연동 + 보호자 **초대·명세 열람**(G8·EZCARE 패턴) + 알림 골격 (G1)
- **선행**: v1 `merge_status: merged`

### 범위

1. Vite+React SPA, JWT 클라이언트, **7역할** 라우팅·Branch Switcher
2. 이용자·출석(수기+QR)·건강·청구·**NHIS reconciliation** UI (API_SPEC §7-3·§7-4)
3. HQ/지점 대시보드 차트·집계 (다지점 비교 — ogada 차별화)
4. 보호자 **초대 온보딩** + **명세·청구서 모바일 탭** (G8 — 이지케어 EZCARE·케어포 가족돌봄앱 패리티)
5. 보호자 포털 열람 강화 + 알림 채널 설계 (SMS/알림톡 — Should, 구현은 v2 일부 가능)

### 완료 기준

- [ ] `npm run build` 성공
- [ ] 7역할 화면·메뉴·권한 분리
- [ ] Must 화면 API 연동 E2E 수동 시나리오 PASS (파일럿 P1–P8 프론트 재현)
- [ ] `/billing/imports/nhis/{batchId}` reconciliation 행 매칭·수동 연결 UI
- [ ] 보호자 **초대·명세 열람** E2E (US-J01·J02 — G8)

---

## v2 — 보호자·알림·결제

- **status**: planned
- **merge_status**: pending
- **stream**: backend
- **목표**: 보호자 풀 포털, 알림톡/SMS, CMS·간편결제 (BENCHMARK G1·G2 — 케어포·엔젤 패리티; 엔젤 CMS **월 30,000원+건당 수수료** TCO 벤치마크)
- **선행**: v1.1 프론트 MVP

### 범위

1. 보호자 풀 포털 (명세·기록·사진 열람 — 케어포 가족돌봄앱 수준)
2. 알림 채널 연동 (카카오 알림톡/SMS — 이지케어·케어포)
3. 본인부담금 **CMS·간편결제** (엔젤 LCMS 벤치마크)

### 완료 기준

- [ ] USER_STORIES Epic J·K 스토리 구현 (보호자 알림·결제)
- [ ] QA_FEEDBACK v2 범위 항목 0건 OPEN
- [ ] 본인부담금 보호자 발송·수납 E2E (MVP에서 제외했던 §3-9-3 후속)

---

## v3 — 확장 모듈

- **status**: planned
- **merge_status**: pending
- **stream**: backend
- **목표**: 식사·프로그램·이동서비스·직원·평가·서류 (BENCHMARK G3·G5 — 케어포 주야간 전 모듈 패리티)

### 범위

- Should/Could 모듈 (REQUIREMENTS §3-5~§3-8, §3-10)
- **제외 유지**: 재무회계·세무·4대보험 (이지케어 G4 — Won't, 별도 연동 검토)
- **제외 유지**: NFC/RFID 출석 (G6 — QR B방식 차별화)

### 완료 기준

- [ ] planner·REQUIREMENTS v3 범위 확정 후 갱신
- [ ] 공단 평가 2026 지표 자동화 여부 결정 (Could — 영업 차별 아님)

---

## 변경 이력

| 날짜 | 변경 |
|------|------|
| 2026-06-06 | 초안 — v1~v3 단계 분리, merge_status 규칙 정의 |
| 2026-06-06 | 벤치마크 2차 동기화 — v1 P0–P3·NHIS reconciliation 완료 기준, v1.1 보호자 확장, v2 CMS·v3 갭 매핑 |
| 2026-06-06 | 자동 동기화 3차 — QA Open 0건 재확인(범위 변경 없음), 문서 식별자 `PLA→PLN`·audience role-code 정렬 |
| 2026-06-06 | 벤치마크 3차 동기화 — G8(보호자 초대·명세 v1.1), NHIS `처리상태` 파서·롱텀2026 Chrome/Edge, 엔젤 CMS TCO |
