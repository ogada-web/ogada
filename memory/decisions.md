# 주요 설계 결정 이력 (decisions.md)

> 에이전트 간 공유. 신규 결정은 최상단에 추가한다.

---

## 2026-06-08 — planner(PLN): 63차 자동 기획 동기화 (TSR 87·88차 + v1.3-A transport unconfirm + v3 StaffPage + merge 게이트 정의)

| # | 항목 | 결정 | 산출물 |
|---|------|------|--------|
| **86** | **baseline git 실측 갱신** | backend **`0d8968d`**(19 ahead, WT CLEAN, 226/226) · frontend **`fe33e7c`**(8 ahead, WT CLEAN, 170/55, 140 modules) | `ROADMAP.md`·`PLAN_NOTES.md` |
| **86** | **v1.3-A transport unconfirm** | `PATCH /api/v1/transport/runs/{id}/unconfirm` hq_admin @ backend `0d8968d` **HEAD PRESENT** — frontend unconfirm UI 잔여 | ROADMAP v1.3 완료 기준 추가 |
| **86** | **v3 StaffPage UI develop 진입** | StaffPage v3 @ frontend `fe33e7c` **HEAD PRESENT** — CRUD·API 연동·Vitest 잔여(§3-8 부분) | ROADMAP v3 완료 기준 갱신 |
| **86** | **v3 merge 게이트 신설** | v3 `merge_status: ready` 조건 — 프로그램 사진 업로드·StaffPage 완전 기능·`pilotPageFlows` v3 E2E 전부 `[x]` 후 | ROADMAP v3 섹션 merge 게이트 정의 |
| **86** | **BNK-9 재확인** | Directions·러-1~4·G17~G19 — 47~62차 반영 **불변** | 변경 없음 |
| **86** | **모듈 커버 추정** | v1.2 ≥60% + transport·meals/programs·StaffPage → **~67–70%** | COMPETITOR_MATRIX §8 KPI |
| **86** | **QA Open 0건** | TSR 87·88차 신규 Open 없음 | 잔여 BLOCK backend merge(19)+SEC-D14+frontend merge(8)+v1.3 unconfirm UI+live E2E |

---

## 2026-06-08 — planner(PLN): 62차 자동 기획 동기화 (BNK-9 + v3 meals/programs full stack + v1.3 live E2E 잔여)

| # | 항목 | 결정 | 산출물 |
|---|------|------|--------|
| **85** | **baseline git 실측 갱신** | backend **`dfd9be2`**(18 ahead, WT CLEAN, 224/224) · frontend **`362dbf0`**(6 ahead, WT CLEAN, 164/54, **39 route·47 page**) | `ROADMAP.md`·`PLAN_NOTES.md`·`REQUIREMENTS.md` |
| **85** | **v3 §3-5·§3-6 develop 완료** | V49·meals/programs REST @ `dfd9be2` · UI·a11y·`pilotPageFlows` E2E @ `362dbf0` | ROADMAP v3 · USER_STORIES US-N01·N02 |
| **85** | **v1.3-A live E2E 잔여** | transport API·UI lineage **PRESENT** — **US-T01~T03 live E2E·`pilotPageFlows` transport 미완** | ROADMAP v1.3 완료 기준 6/7 `[x]` |
| **85** | **BNK-9 재확인** | Directions·러-1~4·G17~G19 — 47~61차 반영 **불변** | 변경 없음 · #44 law.go.kr 잔여 |
| **85** | **모듈 커버 추정** | v1.2 ≥60% + transport·meals/programs full stack → **~65–68%** | COMPETITOR_MATRIX §8 KPI |
| **85** | **QA Open 0건** | 신규 Open 없음 | 잔여 BLOCK backend merge(18)+SEC-D14+frontend merge(6)+v1.3 live E2E |

---

## 2026-06-08 — planner(PLN): 61차 자동 기획 동기화 (BNK-9 + v1.3-A backend + v3 meals/programs shell)

| # | 항목 | 결정 | 산출물 |
|---|------|------|--------|
| **84** | **baseline git 실측 갱신** | backend **`53a1ffe`**(17 ahead, WT CLEAN, 212/212) · frontend **`7ef1083`**(4 ahead, WT CLEAN, 157/53, **39 route·34 page**) | `ROADMAP.md`·`PLAN_NOTES.md`·`REQUIREMENTS.md` |
| **84** | **v1.3-A backend PRESENT** | V47·`/api/v1/transport/*`·geocode proxy @ `53a1ffe` — frontend transport UI lineage **PRESENT** | ROADMAP v1.3 완료 기준 6/7 `[x]` · API_SPEC §12 · US-T01~T03 |
| **84** | **v3 frontend PARTIAL** | `/meals`·`/programs` UI shell @ `7ef1083` — backend meals/programs API **absent** | ROADMAP v3 · USER_STORIES Epic N (US-N01·N02) |
| **84** | **BNK-9 재확인** | Directions·러-1~4·G17~G19 — 47~60차 반영 **불변** | 변경 없음 · #44 law.go.kr 잔여 |
| **84** | **모듈 커버 추정** | v1.2 ≥60% + transport·meals/programs UI → **~62–65%** | COMPETITOR_MATRIX §8 KPI |
| **84** | **QA Open 0건** | 신규 Open 없음 | 잔여 BLOCK backend merge(17)+SEC-D14+frontend merge(4)+v1.3 E2E |

---

## 2026-06-08 — planner(PLN): 60차 자동 기획 동기화 (TSR 82 + v1.3 transport UI shell + copay PAID alimtalk + BNK-9 재확인)

| # | 항목 | 결정 | 산출물 |
|---|------|------|--------|
| **83** | **baseline git 실측 갱신** | backend **`52e0621`**(16 ahead, WT CLEAN, 202/202) · frontend **`e8d1854`**(2 ahead, WT CLEAN, 150/50, **37 route·41 page**) · test **`c510f5c`** v1.2 merged | `ROADMAP.md`·`PLAN_NOTES.md`·`REQUIREMENTS.md` §3-13 |
| **83** | **TSR 82 copay PAID alimtalk** | copay claim CONFIRMED→PAID 시 **`BILLING_PAYMENT_RECEIVED`** dispatch @ `52e0621` | ROADMAP v2·USER_STORIES US-J03 follow-up |
| **83** | **v1.3 frontend PARTIAL** | transport UI shell @ `e8d1854` — **backend transport API absent** → DBA·BE 선행 게이트 | ROADMAP v1.3·USER_STORIES US-T01~T03·API_SPEC §12 |
| **83** | **UXD-43 UNMATCHED PARTIAL** | `ReconciliationPage` 후보 이용자 검색 UI @ `f01e3a8` — 매칭 트랜잭션 API 잔여 | USER_STORIES US-G06 |
| **83** | **BNK-9 재확인** | Directions·러-1~4·G17~G19 — 47~59차 반영 **불변** | 변경 없음 · #44 law.go.kr 잔여 |
| **83** | **QA Open 0건** | TSR 82 신규 Open 없음 | 잔여 BLOCK backend merge(16)+SEC-D14(backend)+frontend merge(2) |

---

## 2026-06-08 — planner(PLN): 58차 자동 기획 동기화 (TSR 79·80 + UXD-41 US-F03 + Solapi template variables + BNK-9 재확인)

| # | 항목 | 결정 | 산출물 |
|---|------|------|--------|
| **82** | **baseline git 실측 갱신** | backend **`4c74f84`**(14 ahead, WT CLEAN, 191/191) · frontend **`95b92b9`**(13 ahead, WT CLEAN, 137/45, **34 route·38 page**, build 124 modules) · test **`4f71543`** v1.1 merged | `ROADMAP.md`·`PLAN_NOTES.md`·`REQUIREMENTS.md` §3-4 |
| **82** | **TSR 79 Solapi template** | `AlimtalkTemplateVariables`·`SolapiKakaoAlimtalkProvider` 템플릿 변수 매핑 @ `4c74f84` | ROADMAP v2·USER_STORIES US-J03 follow-up |
| **82** | **TSR 80 UXD-41·Q154** | `IncidentRecordForm`·`HealthPage` incident 탭(US-F03) @ `3ec8206` · incident API `detail` 필드 @ `95b92b9` | ROADMAP v1.2·USER_STORIES US-F03·REQUIREMENTS §3-4 |
| **82** | **BNK-9 재확인** | Directions·러-1~4·G17~G19 — 47~57차 반영 **불변** | 변경 없음 · #44 law.go.kr 잔여 |
| **82** | **v1.2 P0 게이트** | ≥60% KPI·P0 E2E **충족** · P1 **v1.2.1 후순위** | ROADMAP v1.2 `merge_status: ready` coder 판단 |
| **82** | **QA Open 0건** | TSR 79·80 신규 Open 없음 | 잔여 BLOCK backend merge(14)+B03/SEC-D14(backend)+v1.2 merge(13) |

---

## 2026-06-08 — planner(PLN): 57차 자동 기획 동기화 (TSR 77·78 + UXD-40·Q154 API 정합 + J03 service-layer E2E)

| # | 항목 | 결정 | 산출물 |
|---|------|------|--------|
| **81** | **baseline git 실측 갱신** | backend **`32a1f8f`**(13 ahead, WT CLEAN, 185/185) · frontend **`4957bd3`**(11 ahead, WT CLEAN, 130/44, **33 route·33 page**, build 123 modules) · test **`4f71543`** v1.1 merged | `ROADMAP.md`·`PLAN_NOTES.md`·`REQUIREMENTS.md` §1-3-1·§1-5-2 |
| **81** | **TSR 78 service-layer E2E** | **`J03AlimtalkServiceFlowE2eTest`** — attendance·health·billing→`NotificationService` service-layer alimtalk flow E2E 5건 @ `32a1f8f` | ROADMAP v2·USER_STORIES US-J03 follow-up |
| **81** | **TSR 77 UXD-40·Q154** | `vitalsRanges.js` 비정상 범위 경고(US-F01) · `healthApiPayload.js`·`NhisReconciliationTable` API 본문 정합 Fixed @ `4957bd3` | ROADMAP v1.2·USER_STORIES US-F01·F02·G06 |
| **81** | **BNK-9 재확인** | Directions·러-1~4·G17~G19 — 47~56차 반영 **불변** | 변경 없음 · #44 law.go.kr 잔여 |
| **81** | **v1.2 P0 게이트** | ≥60% KPI·P0 E2E **충족** · P1 **v1.2.1 후순위** · FAQ Q154 **Fixed** | ROADMAP v1.2 `merge_status: ready` coder 판단 |
| **81** | **QA Open 0건** | TSR 77·78 신규 Open 없음 | 잔여 BLOCK backend merge(13)+B03/SEC-D14(backend)+v1.2 merge(11) |

---

## 2026-06-08 — planner(PLN): 56차 자동 기획 동기화 (TSR 76 + UXD-39 Must UI + vitals DAILY_CARE dispatch)

| # | 항목 | 결정 | 산출물 |
|---|------|------|--------|
| **80** | **baseline git 실측 갱신** | backend **`0832fbf`**(12 ahead, WT CLEAN, 179/179) · frontend **`c5708c7`**(9 ahead, WT CLEAN, 115/40, **33 route·33 page**, build 120 modules) · test **`4f71543`** v1.1 merged | `ROADMAP.md`·`PLAN_NOTES.md`·`REQUIREMENTS.md` §1-3-1·§1-5-2 |
| **80** | **TSR 76 vitals dispatch** | `HealthRecordService` — **활력징후 기록→DAILY_CARE alimtalk** @ `0832fbf` | ROADMAP v2·USER_STORIES US-J03 follow-up |
| **80** | **TSR 76 UXD-39** | `VitalsRecordForm`·`MedicationRecordForm`·`NhisReconciliationTable`·`MedicationDuplicateAlert`·`HealthDetailPage` @ `c5708c7` | ROADMAP v1.2·USER_STORIES US-F01·F02·F04·G06 |
| **80** | **BNK-9 재확인** | Directions·러-1~4·G17~G19 — 47~55차 반영 **불변** | 변경 없음 · #44 law.go.kr 잔여 |
| **80** | **v1.2 P0 게이트** | ≥60% KPI·P0 E2E **충족** · P1 **v1.2.1 후순위** | ROADMAP v1.2 `merge_status: ready` coder 판단 |
| **80** | **QA Open 0건** | TSR 76 신규 Open 없음 | 잔여 BLOCK backend merge(12)+B03/SEC-D14(backend)+v1.2 merge(9) |

---

## 2026-06-08 — planner(PLN): 55차 자동 기획 동기화 (TSR 74·75 재확인 + BNK-9 불변 + Epic E 진전)

| # | 항목 | 결정 | 산출물 |
|---|------|------|--------|
| **79** | **baseline git 실측 갱신** | backend **`8ce1151`**(11 ahead, WT CLEAN, 178/178) · frontend **`a627c6d`**(8 ahead, WT CLEAN, 110/36, **33 route·33 page**, build 117 modules) · test **`4f71543`** v1.1 merged | `ROADMAP.md`·`PLAN_NOTES.md`·`REQUIREMENTS.md` §1-3-1·§1-5-2 |
| **79** | **TSR 74 V46 follow-up** | 알림 이력 조회 **인덱스** — `V46__notification_history_query_index.sql` @ `8ce1151` | ROADMAP v2·API_SPEC §11-5 |
| **79** | **TSR 75 Epic E 진전** | **`6f3f746`** US-E01·E02 수기 출석 · **`a627c6d`** US-E03 QR·E05 출석 통계 | ROADMAP v1.2·USER_STORIES Epic E |
| **79** | **BNK-9 재확인** | Directions·러-1~4·G17~G19 — 47~54차 반영 **불변** | 변경 없음 · #44 law.go.kr 잔여 |
| **79** | **v1.2 P0 게이트** | ≥60% KPI·P0 E2E **충족** · P1(급여제공·직원·간편계산기) **v1.2.1 후순위** | ROADMAP v1.2 `merge_status: ready` coder 판단 |
| **79** | **QA Open 0건** | TSR 74·75 신규 Open 없음 | 잔여 BLOCK backend merge(11)+B03/SEC-D14(backend)+v1.2 merge(8) |

---

## 2026-06-08 — planner(PLN): 53차 자동 기획 동기화 (TSR 72·73 + BNK-9 재확인 + v2 알림 이력 API + v1.2 P0 E2E)

| # | 항목 | 결정 | 산출물 |
|---|------|------|--------|
| **78** | **baseline git 실측 갱신** | backend **`c53dd3b`**(10 ahead, WT CLEAN, 178/178) · frontend **`9bdf59f`**(6 ahead, WT CLEAN, 97/30, **33 route·33 page**) · test **`4f71543`** v1.1 merged | `ROADMAP.md`·`PLAN_NOTES.md`·`REQUIREMENTS.md` §1-3-1·§1-5-2 |
| **78** | **TSR 72 v2/J03 follow-up** | 알림 **이력 조회 API** — `GET /guardian/notifications`·`GET /clients/{clientId}/notifications` @ `c53dd3b` | ROADMAP v2·API_SPEC §11-5·USER_STORIES US-J03 |
| **78** | **TSR 73 v1.2 진전** | **`a68f150`** US-E04 FilterChips · **`9bdf59f`** P0 CRUD E2E·`PaymentRecordModal`·보호자 초대/수정 · **≥60% module coverage KPI PASS** | ROADMAP v1.2·USER_STORIES Epic E·K·L |
| **78** | **BNK-9 재확인** | Directions·러-1~4·G17~G19 — 47~52차 반영 **불변** | 변경 없음 · #44 law.go.kr 잔여 |
| **78** | **QA Open 0건** | TSR 72·73 신규 Open 없음 | 잔여 BLOCK backend merge(10)+B03/SEC-D14(backend)+v1.2 merge(6) |

---

## 2026-06-08 — planner(PLN): 52차 자동 기획 동기화 (TSR 70·71 + BNK-9 재확인 + v1.2 UXD 15 pages·P0 KPI)

| # | 항목 | 결정 | 산출물 |
|---|------|------|--------|
| **77** | **baseline git 실측 갱신** | backend **`78e8928`**(9 ahead, WT CLEAN, 171/171) · frontend **`42f48e1`**(4 ahead, WT CLEAN, 89/28, **33 route·33 page**) · test **`4f71543`** v1.1 merged | `ROADMAP.md`·`PLAN_NOTES.md`·`REQUIREMENTS.md` §1-3-1·§1-5-2 |
| **77** | **TSR 71 v1.2 진전** | UXD **`0d83a42`** 15 missing pages · **`42f48e1`** P0 page-flow·module coverage KPI · **18→33 route** | ROADMAP v1.2·USER_STORIES Epic D·E·F·G·H·UX |
| **77** | **TSR 70 v2/J03 follow-up** | `HealthRecordService` 투약기록→DAILY_CARE alimtalk dispatch @ `78e8928` | ROADMAP v2·USER_STORIES US-J03 주석 |
| **77** | **BNK-9 재확인** | Directions·러-1~4·G17~G19 — 47~51차 반영 **불변** | 변경 없음 · #44 law.go.kr 잔여 |
| **77** | **모듈 커버 KPI 추정** | 33 route·15 pages → **~45–50%** (결정 49 ≥60% **잔여**) | ROADMAP v1.2·REQUIREMENTS §1-5-2 |
| **77** | **QA Open 0건** | TSR 70·71 신규 Open 없음 | 잔여 BLOCK backend merge(9)+B03/SEC-D14(backend)+v1.2 merge(4) |

---

## 2026-06-08 — planner(PLN): 51차 자동 기획 동기화 (TSR 68·69 + v1.1 merged + UXD 35 v1.2 커밋)

| # | 항목 | 결정 | 산출물 |
|---|------|------|--------|
| **76** | **baseline git 실측 갱신** | backend **`44e0f02`**(8 ahead, WT CLEAN, 170/170) · frontend **`e0eaf32`**(2 ahead, WT CLEAN, 82/27) · test **`4f71543`** v1.1 merged | `ROADMAP.md`·`PLAN_NOTES.md`·`REQUIREMENTS.md` §1-3-1·§1-5-2 |
| **76** | **TSR 68·69 반영** | v1.1 **`merge_status: merged`** · SEC-D14 frontend portion **해소** · UXD 35 `64468a3` Must UI develop 커밋 · `e0eaf32` guardians RBAC | ROADMAP v1.2·US-UX-02·FE-12/13 진전 |
| **76** | **50차 WIP 해소** | frontend **24 files dirty-tree → `64468a3` develop 커밋** · #36 FE-6 recurrence **해소** | USER_STORIES·PLAN_NOTES |
| **76** | **BNK-9 재확인** | Directions·러-1~4·G17~G19 — 47·49·50차 반영 **불변** | 변경 없음 · #44 law.go.kr 잔여 |
| **76** | **QA Open 0건** | TSR 68·69 신규 Open 없음 | 잔여 BLOCK backend merge(8)+B03/SEC-D14(backend)+v1.2 merge(2) |

---

## 2026-06-08 — planner(PLN): 50차 자동 기획 동기화 (BNK-9 재확인 + frontend dirty-tree 재확대)

| # | 항목 | 결정 | 산출물 |
|---|------|------|--------|
| **75** | **baseline git 실측 재확인** | backend **`c221531`**(7 ahead, WT 3M) · frontend **`4f71543`**(develop=test, WT **24 files**) · 18 route·18 page | `ROADMAP.md`·`PLAN_NOTES.md`·`workspace_baseline.yaml` |
| **75** | **frontend WT 재확대** | 49차 1M→**24 files** — Must UI WIP cluster · **HEAD Fixed @ `4f71543` 유효** | ROADMAP v1.2·FE-12/13 lineage |
| **75** | **BNK-9 재확인** | Directions·러-1~4·G17~G19 — 47·49차 반영 **불변** | 변경 없음 · #44 law.go.kr 잔여 |
| **75** | **QA Open 0건** | TSR 66·67 이후 신규 Open 없음 | 잔여 BLOCK backend merge(7)+B03+WT **27 files** |

---

## 2026-06-08 — planner(PLN): 49차 자동 기획 동기화 (TSR 66·67 + BNK-9 재확인 + baseline HEAD 갱신)

| # | 항목 | 결정 | 산출물 |
|---|------|------|--------|
| **74** | **baseline git 실측 갱신** | backend **`c221531`**(7 ahead, WT 3M) · frontend **`4f71543`**(develop=test, WT 1M) · 18 route·18 page | `ROADMAP.md`·`PLAN_NOTES.md`·`REQUIREMENTS.md` §1-5-2 |
| **74** | **TSR 66·67 반영** | v2/J03 alimtalk E2E @ `c221531` · UXD SideNav·FE-22 liveConfig @ `4f71543` | ROADMAP v1.2 US-UX-02 진전 |
| **74** | **BNK-9 재확인** | Directions·러-1~4·G17~G19 — 47차 반영 **불변** | 변경 없음 |
| **74** | **QA Open 0건** | TSR 66·67 신규 Open 없음 | 잔여 BLOCK backend merge(7)+B03+WT dirty |

---

## 2026-06-07 — planner(PLN): 결정 73 — live E2E merge 게이트 제외 (사용자)

| # | 결정 | 근거 | 영향 |
|---|------|------|------|
| **73** | Must P1–P8·J01/J02 **live E2E run**은 **`merge_status: ready` 선행 조건 아님** | 사용자 지시 — merge·live E2E 순환 BLOCK 해소 | ROADMAP v1.1 `merge_status: ready` · live E2E → post-merge 섹션 · 이관 규율 10항 |
| **73** | fetch-mock Vitest(`npm test`) + FE-22 harness 코드로 merge-blocking 충족 | TSR 65 harness PRESENT · 46/13 PASS | live run은 merge **후** `LIVE_E2E=1` + backend 가동 시 권장 |

---

## 2026-06-08 — benchmark_researcher(BNK): 9차 API 요금·2026 규제·baseline drift (BNK-9)

9차 재조사 — BNK-8 잔여(Directions API·이동서비스비 실액) 해소 + 2026 상반기 규제(평가 #27·단기보호·통합재가) + ogada frontend **git 실측**. 산출물: `BENCHMARK_REPORT.md` §12·`COMPETITOR_MATRIX.md` §11·§1 G17~G19.

| # | 결정·권고 | 근거 | planner/coder 영향 |
|---|----------|------|-------------------|
| 1 | **카카오 길찾기 API 요금 확정** — 자동차 일 10,000건 무료·초과 8원; **다중 경유지** 일 5,000건·16원 | [Kakao Mobility price](https://developers.kakaomobility.com/price/) | v1.3-B TSP+15정차는 **다중 경유지 API** 권장. PLAN_NOTES #43 **해소** |
| 2 | **이동서비스비 러-1~4 = 830/2,630/4,440/6,240원**(편도·2차 출처) — law.go.kr 2026 별표 **1차 미확인** | [고시 제34조 요약](https://www.publicmonitor.net/%EC%9E%A5%EA%B8%B0%EC%9A%94%EC%96%91%EA%B8%89%EC%97%AC-%EC%A0%9C%EA%B3%B5%EA%B8%B0%EC%A4%80-%EB%B0%8F-%EA%B8%89%EC%97%AC%EB%B9%84%EC%9A%A9-%EC%82%B0%EC%A0%95%EB%B0%A9%EB%B2%95-%EB%93%B1%EC%97%90-%EA%B4%80%ED%95%9C-%EA%B3%A0%EC%8B%9C) | v1.3-C `transport_service_fee` — **상수 하드코딩 금지**, fee 테이블화 |
| 3 | **G17 2026 평가 #27 기능회복훈련**(3점) — 케어포·이지케어 반영, ogada **Won't v1** | [케어포 2026 PDF](https://www.carefor.co.kr/ct_att/contents_article/0/202602/46102/lIxDliWswE.pdf) | Could v2+ — 급여계획·care_plan 모듈 |
| 4 | **G18 단기보호 시범·G19 통합재가** — 케어포 지원, ogada **Won't v1** | [44590](https://www.carefor.co.kr/cs/view_pds.php?calmgno=44590)·[45759 PDF](https://www.carefor.co.kr/ct_att/contents_article/0/202603/45759/sykAkdmpN6.pdf) | MVP 범위 유지 |
| 5 | **문서-코드 drift** — `@7170b2a` 실측 **15 Route·14 page**; TSR/planner 인용 `4be0938`·24 route **git object 없음** | `git -C src/frontend cat-file -t 4be0938` → fatal | v1.2 KPI·ROADMAP **HEAD 실측 재정의**. FE-6 커밋 게이트 선행 |

---

## 2026-06-08 — planner(PLN): 47차 자동 기획 동기화 (TSR 64·65 + BNK-9 + baseline HEAD 갱신)

| # | 항목 | 결정 | 산출물 |
|---|------|------|--------|
| **72** | **baseline git 실측 갱신** | backend **`80bdb1e`**(6 ahead) · frontend **`d592a17`**(11 ahead, **18 route**) · BE-11 Fixed · FE-22 harness PARTIAL | `ROADMAP.md`·`PLAN_NOTES.md`·`REQUIREMENTS.md` §1-3-1 |
| **72** | **BNK-9 planner 반영** | Directions API 요금 확정 · 이동서비스비 러-1~4 · G17~G19 Won't v1 · **24 route/`4be0938` drift 정정** | `REQUIREMENTS.md` §1-5 · `ROADMAP.md` v1.3 · `USER_STORIES.md` US-T05~T06 |
| **72** | **QA Open 0건** | TSR 64·65 신규 Open 없음 · SEC-014 Fixed · 잔여 BLOCK merge(6+11)+B03+live E2E run | `QA_FEEDBACK.md` planner-sync 47차 |

---

## 2026-06-08 — planner(PLN): 46차 자동 기획 동기화 (SEC 6차 Open 2건 Planned + BNK-8 정합 + baseline 불변 재확인)

| # | 항목 | 결정 | 산출물 |
|---|------|------|--------|
| **71** | **SEC 6차 Open→Planned** | SEC-D14(test 미승격) = **B03·merge 게이트** 동반 · SEC-D13 = **BE-11** `AuthRateLimitService` | `QA_FEEDBACK.md`·`ROADMAP.md`·`USER_STORIES.md` §16·§18 |
| **71** | **baseline 불변 재확인** | backend **`136239e`** · frontend **`7170b2a`** WT CLEAN · `mvn test` 152/152 · `npm test` 40/11 — **45차와 동일** | `PLAN_NOTES.md` 46차·`workspace_baseline.yaml` |
| **71** | **FE-22·BE-11 신설** | v1.1 잔여 live E2E → **FE-22** · auth rate limit → **BE-11** | `ROADMAP.md` v1.1 완료 기준·`USER_STORIES.md` |
| **71** | **BNK-8 COMPETITOR_MATRIX 정합** | 케어포 배차 지도 **△**(카카오맵 지도보기) — v1.3-A 패리티·v1.3-B 차별화 **변경 없음** | `COMPETITOR_MATRIX.md` §1 |
| **71** | **#42 해소** | v1 baseline **`136239e`/`7170b2a`** 확정 — replay/cherry-pick 불필요 | `PLAN_NOTES.md` `#42` |

---

## 2026-06-08 — planner(PLN): 45차 자동 기획 동기화 (TSR 62·63 + Must API·J01 REST + baseline 갱신)

| # | 항목 | 결정 | 산출물 |
|---|------|------|--------|
| **70** | **TSR 63 v1.1 완료 기준 승격** | QA-H04·M01·R-04a·R-05·SEC-008 **Fixed @ `811aef3`**. Must API·pilot·7-role·`ReconciliationPage` develop HEAD **PRESENT**. | `ROADMAP.md` v1.1 완료 기준·`REQUIREMENTS.md` §1-3-1 |
| **70** | **COD `7170b2a` J01/J02 PARTIAL** | `ClientDetailPage`·`GuardianPortalPage` REST fetch-mock 회귀 **PASS**. **live API E2E**·Must **라이브 E2E** 잔여. | `USER_STORIES.md` US-J01·J02·FE-21 |
| **70** | **BLOCK 재우선순위** | **backend merge(4) + frontend merge(9) + B03** + v1.1 라이브 E2E 2건. BNK-8 **변경 없음**. | `PLAN_NOTES.md` 45차·`workspace_baseline.yaml` |
| **70** | **baseline 갱신** | backend **`136239e`** · frontend **`7170b2a`**. `d5654c0`/`e5fd48d` checkout **금지** 유지. | `.agents/workspace_baseline.yaml` |

---

## 2026-06-08 — planner(PLN): 42차 자동 기획 동기화 (TSR 58·59 + BNK-8 + baseline 회귀)

| # | 항목 | 결정 | 산출물 |
|---|------|------|--------|
| **69** | **TSR 58·59 QA Open→Planned** | QA-B10·SEC-D11·SEC-D12·QA-B11 → **BE-10·INFRA-B12·FE-20**. B09·SEC-D8 **Fixed @ `f47ffa1`**. | `QA_FEEDBACK.md`·`ROADMAP.md`·`USER_STORIES.md` §17 |
| **69** | **BNK-8 v1.3 포지셔닝** | v1.3-A = **케어포 지도 패리티**(「최초 지도」 금지). v1.3-B = **영업 차별 핵심**. | `REQUIREMENTS.md` §1-5-3·§3-13·`ROADMAP.md` v1.3 |
| **69** | **BLOCK 재우선순위** | **INFRA-B12 → BE-10 → FE-19 → FE-18 → backend merge(1) → B03**. B09 **소멸**. | `PLAN_NOTES.md` 42차·`ROADMAP.md` 핵심 진단 |
| **69** | **v1 baseline 미결(#42)** | develop `@f47ffa1` vs merged `@e8750d2` — replay/cherry-pick/baseline 갱신 **사용자·planner 결정 대기** | `PLAN_NOTES.md` `#42` |

---

## 2026-06-07 — benchmark_researcher(BNK): 8차 케어포 지도보기 확인·API 비용·공단 이동서비스비·2026 평가 (BNK-8)

7차(BNK-7) 「요양 ERP 지도 없음」 가정 검증 + ogada v1.3 카카오맵 API 비용 실측 + 공단 이동서비스비 산정 구조 확인 + 경쟁사 2026 업데이트 동향 조사. 산출물: `BENCHMARK_REPORT.md` §11 신규·§10 수정·`COMPETITOR_MATRIX.md` §10 신규·§9 수정.

| # | 결정·권고 | 근거 | planner/coder 영향 |
|---|----------|------|-------------------|
| **1(수정)** | **케어포 「이동서비스 지도보기」 기능 공식 확인** — 탑승자 위치를 **카카오맵**으로 조회 가능(BNK-7 「지도 없음」 가정 **번복**). 경로 최적화·TSP는 없음(지도 마커 표시 수준). | [케어포 주야간 매뉴얼 PDF](https://www.carefor.co.kr/ct_att/contents_article/0/202206/12/Dov8rzFqBv.pdf) | **v1.3-A 영업 메시지 수정 필요** — 「요양 ERP 최초 지도」가 아님. 케어포 패리티 달성이 v1.3-A 목표; **v1.3-B(TSP·도로경로)가 진짜 차별화 축** |
| 2 | **카카오맵 API 파일럿 비용 = 무료 범위** — 지도 JS SDK 일 3만건·로컬(Geocoding) 일 10만건 무료 쿼터로 파일럿(50개 법인 이내) **충분**. 초과 단가 0.5원/건(2026 한시 10원). **Directions API(도로경로) 별도 비용 조사 필요** (v1.3-B 설계 전). | [카카오 Developers](https://developers.kakao.com/) | v1.3-A 지도 비용 위험 없음. v1.3-B(도로경로 API) 비용 산정을 설계 전 선행 |
| 3 | **공단 이동서비스비 산정 구조 확인** — **1일 1회**, 편도 50%, **수급자 본인부담 없음**(기관→공단 청구), 거리별 '러-1'~'러-4' 구간 (실액 2026 고시 별표 미확인). 운행일지(별지 22호) = 2026 평가 점검 항목. | [엔젤시터 이동서비스비 매뉴얼](https://angelsitter.co.kr/board.view.php?board=bbs3&no=235)·[2026 고시](https://angelsitter.co.kr/board.view.php?board=bbs3&no=741) | v1.3-C `transport_runs`에 **편도/왕복 플래그·최단거리·차량번호** 컬럼 필요. 수납 방향 아닌 **공단 batch claim** 흐름. |
| 4 | **이지케어·케어포 2026 평가 기능 강화** — 이지케어: 전국 교육 확대·주야간 평가 기능 고도화. 케어포: 2026 평가지표 반영·사례관리 회의록 강화(2025-12-23). | 공식 교육 공지·업데이트 공지 | **평가 체크리스트 연동**이 경쟁사 공통 전략 — ogada v1.2 이후 **평가 모니터링 UI** 고려 필요 |

---

## 2026-06-08 — planner(PLN): 41차 자동 기획 동기화 (BNK-7 G15/G16 v1.3 명시 + submodule·QA 재확인)

| # | 항목 | 결정 | 산출물 |
|---|------|------|--------|
| **68** | **BNK-7 planner 권고 문서화** | v1.3-A = **운영 시각화 한정**(청구·평가 G15 미포함, UI 고지). v1.3-C = **G15(별지 22/18호)·G16(`vehicles`·이동서비스비)** 완료 기준. US-T05 신설. | `ROADMAP.md` v1.3·`REQUIREMENTS.md` §1-5-1·§3-13·`USER_STORIES.md` Epic T |
| **68** | **submodule·BLOCK 불변** | 40차와 동일 — backend stale·9U migrations only · frontend stale·CLEAN. QA Open 0 · Planned BLOCK 5건·coder 우선순위 **변경 없음**. | `PLAN_NOTES.md` 41차·`QA_FEEDBACK.md` planner-sync 41차 |

---

## 2026-06-08 — planner(PLN): 41차 자동 기획 동기화 (BNK-7 G15/G16 v1.3 완료 기준 명시 + submodule·QA 재확인)

| # | 항목 | 결정 | 산출물 |
|---|------|------|--------|
| **68** | **BNK-7 v1.3 범위 명확화** | v1.3-A = **운영 시각화 한정**(명단·지도) — **G15(별지 제22호 일지·제18호)·G16(`vehicles`·이동서비스비) = v1.3-C**. 영업 차별 = **v1.3-B(TSP·도로경로)** 도달 시 「요양 전용 경로 배차」. A 단독은 케어포 이동서비스 **패리티 미달**. | `ROADMAP.md` v1.3-A/C 완료 기준·`REQUIREMENTS.md` §1-5-1·§3-13·`USER_STORIES.md` US-T05·Epic T |
| **68** | **submodule·BLOCK 불변** | QA Open **0건**·Planned BLOCK **변경 없음**. ogada workspace — backend **`2799e29`(stale)**·WT **9U**(V35~V43 only) · frontend **`e5fd48d`(stale)**·WT **CLEAN** → TSR 56·57 재검증 **불가**. baseline **`428ba7d`/`d5654c0`** 유지. | `PLAN_NOTES.md` 41차·`QA_FEEDBACK.md` 41차 sync |
| **68** | **coder 우선순위 불변** | ⓪ submodule checkout → ① **FE-19**(H05+SEC-D9) → ② **FE-18**(B07 #6) → ③ **BE-8**(B09+SEC-D8) → ④ backend merge(3커밋) → ⑤ **B03** | `ROADMAP.md`·`PLAN_NOTES.md` 41차 coder 액션 |

---

## 2026-06-08 — planner(PLN): 40차 자동 기획 동기화 (벤치마크·QA 재확인 + submodule 드리프트 부분 개선)

| # | 항목 | 결정 | 산출물 |
|---|------|------|--------|
| **67** | **submodule 드리프트 부분 개선** | 39차 frontend 부재 → 40차 **init 복구**(`e5fd48d`·WT CLEAN). backend stale(`2799e29`·WT 9U V35~V43) **불변**. TSR 56·57 재검증 **여전히 불가** → baseline 유지·checkout `428ba7d`/`d5654c0` 선행. | `ROADMAP.md` 40차·`PLAN_NOTES.md` 40차·`REQUIREMENTS.md` §1-3-1 |
| **67** | **Planned BLOCK·우선순위 불변** | QA Open 0 · BNK-7·SEC-D8/D9 반영 확인. coder: ⓪ submodule checkout → ① FE-19 → ② FE-18 → ③ BE-8 → ④ backend merge → ⑤ B03 | `PLAN_NOTES.md` 40차 coder 액션 |

---

## 2026-06-07 — planner(PLN): 39차 자동 기획 동기화 (벤치마크·QA 재확인 + workspace submodule 드리프트)

| # | 항목 | 결정 | 산출물 |
|---|------|------|--------|
| **66** | **ogada workspace submodule 드리프트** | planner 직접 점검 — `src/backend` @ **`2799e29`(stale)** vs TSR 56 **`428ba7d`** · WT 8U(V35~V42) · `src/frontend` **미체크아웃** vs TSR 57 **`d5654c0`**. TSR 56·57 재검증 불가 → **기획 baseline = TSR 57차 유지**·coder submodule init/checkout 선행. | `ROADMAP.md` 39차·`PLAN_NOTES.md` 39차·`REQUIREMENTS.md` §1-3-1 |
| **66** | **Planned BLOCK·우선순위 불변** | QA Open 0 · BNK-7 G15/G16→v1.3-C 반영 확인. coder: ⓪ submodule 동기화 → ① FE-19 → ② FE-18 → ③ BE-8 → ④ backend merge → ⑤ B03 | `PLAN_NOTES.md` 39차 coder 액션 |

---

## 2026-06-07 — benchmark_researcher(BNK): 7차 배차·이동서비스 전수 (BNK-7 — v1.3 대응)

planner 결정 60~62(배차·이동경로 v1.3-A 수동 명단+지도) 대응. 요양 ERP 3사 이동서비스 vs 범용 송영/통학 SaaS 전수 + 공단 이동서비스비 법정 서식 재조사(조사일 **2026-06-07**). 산출물: `BENCHMARK_REPORT.md` §10·`COMPETITOR_MATRIX.md` §9 신규 작성, 6차 본문 유지.

| # | 결정·권고 | 근거 | planner/coder 영향 |
|---|----------|------|-------------------|
| 1 | **이동서비스 = 2계열, ogada는 빈 칸 공략** — 요양 ERP(케어포·이지케어·엔젤)는 **기록·청구**(차량·운행일지·이동서비스비)는 ✅이나 **지도·경로 ❌**; 범용 송영 SaaS(RIDE·DispatchFlow·T-RiseUp·Mobiligent)는 **지도·AI경로 ✅**이나 **공단 이동서비스비 ❌** | [carefor func](https://www.carefor.co.kr/daycare/func.php)·[ride.bz](https://ride.bz/)·[busta.kr](https://busta.kr/) | v1.3 차별화 축 = 「요양 도메인 + 지도 경로」 교집합 |
| 2 | **v1.3-A는 경쟁사 패리티 미달·차별 약함** — 「수동 명단 + 직선 폴리라인」은 지도 표시뿐, 케어포 이동서비스 모듈(차량·일지·청구) 대비 미달. **차별화는 v1.3-B(TSP·도로경로) 도달 시 성립** | 케어포 모듈 2 vs REQUIREMENTS §3-13 | 영업 메시지 = v1.3-B 기준. A 완료 기준에 「운영 시각화 한정·청구/평가 미대응」 명시 권고 |
| 3 | **신규 갭 G15(이동서비스 법정 서식)** — 별지 제22호 **이동서비스일지**·제18호 신청·급여제공기록지 **차량번호**는 2026 평가 **모니터링 점검 항목**(고시 제34조). v1.3-A 미포함 → **v1.3-C 청구·평가 필수** | [공단 이동서비스비 매뉴얼](https://angelsitter.co.kr/board.view.php?board=bbs3&no=235)·[2026 평가 PDF](https://www.carefor.co.kr/ct_att/contents_article/0/202603/45575/UkZQcm3xn4.pdf) | v1.3-C에서 `transport_runs`→별지 22호 일지 매핑 |
| 4 | **신규 갭 G16(차량 마스터·이동서비스비)** — `vehicles`(지자체 신고번호·정원)·이동서비스비 청구는 v1.3-C | 케어포 2-4/2-5·고시 제34조 | ERD `vehicles`(v1.3-C) — REQUIREMENTS §3-13-2 정합 |
| 5 | **RIDE 포지셔닝 동형** — 「스마트폰 only·하드웨어 없음·B2B 다지점 본사 통합·AI경로」가 ogada(카카오맵 JS·다지점 HQ) 메시지와 근접. 단 RIDE는 요양 청구 미지원 → ogada는 **요양 특화**로 분리 | [ride.bz](https://ride.bz/) | 영업 차별 메시지 입력 |
| 6 | **재검증 불변** — 케어포 주야간 **flat 월 33,000원(VAT 포함)**·2026 수가 전등급×5밴드·copay 15/9/6/0% 모두 6차와 동일 확인 | [cost.php](https://www.carefor.co.kr/price/cost.php)·[롱텀 수가](https://www.longtermcare.or.kr/npbs/e/b/502/npeb502m01.web?menuId=npe0000002742) | 변경 없음 — §3-9·§6 유지 |

**planner 후속**: ① REQUIREMENTS §3-13-2 단계 표에 **G15(별지 22호 일지)·G16(`vehicles`)을 v1.3-C 완료 기준**으로 명시. ② v1.3-A 완료 기준에 「청구·평가 미대응, 운영 시각화 한정」 문구. ③ 영업 차별은 **v1.3-B 도달 시** 「요양 전용 경로 배차」. ④ v1.3-C 설계 시 공단 이동서비스비(고시 제34조)·별지 18/22호를 `vehicles`·`transport_runs`와 연계.
**8차 조사 우선**: 케어포 이동서비스 **로그인 후 화면**(지도 유무 최종 확인 — 현재 「지도 없음」 가정)·공단 **이동서비스비 2026 수가 실액**(편도/왕복·가산)·카카오맵 JS/Geocoding **쿼터·요금 TCO**(영구 캐시 PLAN_NOTES #41).
**미해결 추적**: #27(공단 엑셀 실컬럼)·#31(가격 tier)·#32(다지점 HQ 사례)·**이동서비스비 실액·케어포 이동 화면 지도 유무**(7차 신규).

---

## 2026-06-07 — planner(PLN): 38차 자동 기획 동기화 (SEC 4차 SEC-D8·SEC-D9)

| # | 항목 | 결정 | 산출물 |
|---|------|------|--------|
| **65** | **SEC-D8 J01 SecurityConfig 게이트** | SEC-20260607-009 Open→Planned. `SecurityConfig` 공개 endpoint 단일 경로·토큰 단일사용·만료·rate limit — **BE-8 commit/merge 금지** 조건. | `QA_FEEDBACK.md`·`ROADMAP.md`·`USER_STORIES.md` BE-8·`API_SPEC.md` §4-1·SECURITY_CHECKLIST H-6 |
| **65** | **SEC-D9 MaskedPhone PII 게이트** | SEC-20260607-010 Open→Planned. `GuardianListCard` 마스킹 `010-****-5678` 유지·테스트 정합 — **FE-19**·QA-H05 동반·마스킹 제거 시 BLOCK 격상. | `QA_FEEDBACK.md`·`USER_STORIES.md` FE-19 |
| **65** | **37차 Open 불일치 정리** | 37차 planner가 Open 0건으로 기록했으나 SEC auditor Open 2건 잔존 — 38차에서 Planned 이동·Open 0건 재확인. | `PLAN_NOTES.md` 38차 sync |

---

## 2026-06-07 — planner(PLN): 37차 자동 기획 동기화 (TSR 56·57차)

| # | 항목 | 결정 | 산출물 |
|---|------|------|--------|
| **64** | **J01 백엔드 API WIP 관측** | TSR 56차 — 54차 `428ba7d` CLEAN→DIRTY 27 files. **BE-8 Planned** — 완료 단위 develop 커밋 전 backend merge **BLOCK**. HEAD Fixed(B02 #6·B08 #2) 규율 5 유효. | `ROADMAP.md`·`USER_STORIES.md` BE-8·`API_SPEC.md` §4-1 |
| **64** | **FE-7 회귀(H05)** | TSR 57차 — `GuardianListCard.test.jsx` MaskedPhone vs 평문 불일치·209/210 FAIL. **FE-19 Planned** — B07 #6(FE-18) 커밋 **선행 게이트**. | `QA_FEEDBACK.md`·`USER_STORIES.md` FE-19 |
| **64** | **#36 양 스트림 재오픈** | 36차 backend BE-6/BE-7 해소 직후 **B09(BE-6 #7)** + frontend **FE-6 #5**(B07 #6 + H05). 결정 63 운영 게이트 build 대기 유지. | `PLAN_NOTES.md` 37차 sync |

---

## 2026-06-07 — planner(PLN): 사용자 결정 63차 (#36 운영 게이트 — 양 스트림·Fixed 차단+경고·build 위임)

사용자 1:1 대화. **결정 56** 범위·L1 정책 확정. **코드/인프라 구현은 build 승인 후** coder/db_architect.

| # | 항목 | 결정 | 산출물 |
|---|------|------|--------|
| **결정 63** | **#36 운영 게이트 적용 범위** | **backend + frontend 양 스트림** (결정 56 backend 단독 → **확대**). FE-6 #5·B07 #6 재발 근거. | `PLAN_NOTES.md` #36·`ROADMAP.md` 이관 규율 9항 |
| **결정 63** | **L1 에이전트 턴 종료 정책** | dirty-tree(신규 테스트·Flyway·WIP) 발견 시 **ⓑ Fixed 주장 차단 + 경고** — **자동 커밋 금지**. coder가 develop 커밋 후 턴 종료. | `scripts/run_agent.py`(build)·`memory/blockers.md` |
| **결정 63** | **L2·L3 (build 구현)** | L2 pre-commit(test/build PASS)·L3 CI fail-fast — **build 승인 후** 구현. | `.husky/pre-commit`·`.github/workflows/` (미착수) |

**build 완료 기준 (coder)**: ① L1 턴 종료 검사(backend·frontend submodule) ② L2 hook ③ L3 CI ④ `docs/ops/DEPLOYMENT_GUIDE.md` 또는 agent 가이드 1문단.

---

## 2026-06-07 — planner(PLN): 사용자 결정 41차 (배차 15명·hq_admin 확정·픽업만)

사용자 1:1 대화. v1.3-A 운영·권한·범위 확정.

| # | 항목 | 결정 | 산출물 |
|---|------|------|--------|
| **결정 62** | **정차 상한** | 운행당 **최대 15명** (UI·API 검증) | `REQUIREMENTS.md` §3-13-3 |
| **결정 62** | **확정 워크플로** | `hq_admin`이 루트 편집 후 **「배차 확정」**(`CONFIRMED`) → `caregiver`·`social_worker`·`branch_admin`은 **명단·지도 읽기 전용**. `DRAFT`는 hq_admin만. 픽업 완료 체크 **v1.3-A 제외** | US-T02·T03·API confirm |
| **결정 62** | **방향** | v1.3-A = **PICKUP(픽업)만**. DROPOFF = **v1.3-A.1**(US-T04) | `ROADMAP.md` v1.3-A.1 |

**다음 액션**: 지도 벤더(카카오) 확인 → API_SPEC·ERD 잠금

---

## 2026-06-07 — planner(PLN): 사용자 결정 40차 (배차 v1.3-A 수동 명단+지도)

사용자 1:1 대화. 배차 1차 구현 방식 확정.

| # | 항목 | 결정 | 산출물 |
|---|------|------|--------|
| **결정 61** | **배차 1차 = v1.3-A** | **수동 명단** + **수동 정차 순서**(드래그) + 지도 **순번 마커** + **직선 폴리라인**. TSP·Directions(도로 경로)는 **v1.3-B**. 차량 엔티티·청구·출석 자동연동은 v1.3-A **제외**. | `REQUIREMENTS.md` §3-13·`USER_STORIES.md` US-T01~T03·`ROADMAP.md` v1.3 |
| **(가정)** | 운행 단위 | 지점×날짜×방향(PICKUP/DROPOFF)별 1 run. 정차 ≤15명. 카카오맵+Geocoding 서버 프록시 | `PLAN_NOTES.md` #41 |

**다음 액션**: #41 잔여(정차 상한·T03 포함·지도 벤더) 사용자 확인 → API_SPEC·ERD 잠금

---

## 2026-06-07 — planner(PLN): 사용자 결정 39차 (배차·이동경로 v1.3 초안)

사용자 1:1 대화. 배차 이용자 명단 + 다인 탑승 시 최단 경로 지도 표시 요청.

| # | 항목 | 결정 | 산출물 |
|---|------|------|--------|
| **결정 60** | **배차·이동경로 모듈** | v1.3 신설. 3단계(A: 수동+지도 / B: TSP 자동 / C: 차량·청구). 지도·경로 = **카카오맵 API 권고**. 파일럿 1주차 **제외**. | `REQUIREMENTS.md` §3-13·`USER_STORIES.md` Epic T·`ROADMAP.md` v1.3 |
| **(미확정)** | 구현 세부 | #41 — 차량·왕복·TSP MVP·출석 연동·청구·지도 벤더 | `PLAN_NOTES.md` #41 |

**다음 액션**: 사용자 #41 답변 → API_SPEC·ERD 잠금 → v1.1 merged 후 coder 착수

---

## 2026-06-07 — planner(PLN): 사용자 결정 38차 (보호자 초대 이메일 단일·파일럿 유지·추가 기능 미확정)

사용자 1:1 대화. **신규 QA Open**: TSR 57차 H05·B09 (문서 반영은 별도 sync).

| # | 항목 | 결정 | 산출물 |
|---|------|------|--------|
| **결정 59** | **보호자 초대 채널 = 이메일 링크 단일** | v1.1 US-J01 `channel: EMAIL` 고정. SMS·알림톡 v2(US-J03). 토큰 만료 **7일**(가정, #35). | `REQUIREMENTS.md` §8-1·`USER_STORIES.md` US-J01·`PLAN_NOTES.md` #33 |
| **(유지)** | **파일럿 1주차 P1–P3** | 결정 57 그대로 — P1 이용자+보호자 연결, P2 수기 출석, P3 건강·투약 | `REQUIREMENTS.md` §1-3-1 |
| **(미확정)** | **기능 1건 추가** | 사용자 「기능 하나 추가」 요청 — **내용 미지정** | `PLAN_NOTES.md` #40 |

**다음 액션**: ① 추가 기능 내용 확정(#40) ② API_SPEC §4 J01 스키마 잠금(coder/DBA) ③ #35 만료·재발송 정책 확정(선택)

---

## 2026-06-07 — planner(PLN): 자동 기획 동기화 36차 (TSR 54·55차 + backend B02 #6·B08 #2 Fixed `428ba7d` + frontend B07 #6 Planned·FE-18 + Open 0건)

`build --role planner` 자동 동기화. **핵심 입력**: TSR 54차(09:23, backend — develop HEAD `c3b8716`→**`428ba7d`**(+1 COD 36), WT **DIRTY→CLEAN**, **QA-B02 #6·QA-B08 #2 Fixed**, develop HEAD `mvn test` **253/253**, test **213/213**, develop **3 ahead of test**)·TSR 55차(09:29, frontend — 53차 `d5654c0` **CLEAN→DIRTY** 15 files, DateInput·GuardianInvitationList J01·ClientDetail 보호자/초대 WIP, **HEAD `d5654c0` Fixed(FE-17) 규율 5 유효**, WT `npm test` **205/42**·758 modules·audit **0**). 벤치마크 BNK-6 **신규 입력 없음**. **Open 0건** — Planned BLOCK **B03 + backend merge(3커밋 @ `428ba7d`) + B07 #6**.

| # | 반영 | 산출물 |
|---|------|--------|
| **결정 54 갱신** | backend develop→test merge **2→3커밋** @ `428ba7d` (COD 36 V42 포함) | `PLAN_NOTES.md` 결정 54·`ROADMAP.md` merge 게이트 |
| **#36 backend 해소** | BE-6 #6·BE-7 #2 Fixed @ `428ba7d` | ROADMAP v1 QA-B02 `[x]`·v2 B08 recurrence #2 `[x]` 유지 |
| **#36 frontend 재오픈** | FE-6 #5 = B07 recurrence #6 → **FE-18** | USER_STORIES §16·ROADMAP v1.1 |
| **J01 진전** | 초대 **목록 UI**(GuardianInvitationList) WIP — 수락 UI(FE-17) @HEAD 유지 | US-J01·BENCHMARK G8 |

**잔여 BLOCK**: B03(frontend merge 18 ahead) + backend merge(3커밋) + B07 #6(dirty-tree). J01 백엔드 API·라이ve E2E 미충족.

---

## 2026-06-07 — planner(PLN): 사용자 결정 37차 (merge 검증 우선·파일럿 1주차 3업무·초대 채널 설명)

사용자 1:1 대화. **신규 QA Open**: frontend B07 #6(TSR 55차) — backend는 TSR 54차 Fixed.

| # | 항목 | 결정 | 산출물 |
|---|------|------|--------|
| **결정 57** | **파일럿 1주차 우선 3업무** | ① P1 이용자+보호자 연결(센터장) ② P2 수기 출석 10명(요양보호사) ③ P3 건강·투약 기록(요양보호사). 2주차+: P4–P8 | `REQUIREMENTS.md` §1-3-1·`USER_STORIES.md` §13-1 |
| **결정 58** | **사용자 급선무 = develop→test merge 검증** | backend `428ba7d` CLEAN·3 ahead → merge 즉시. frontend FE-18 commit(B07 #6) → v1.1 ready → merge | `REQUIREMENTS.md` §1-3-1 merge 표·`PLAN_NOTES.md` #36 coder 액션 |
| ~~**(미확정)**~~ | **보호자 초대 채널(#33)** | → **결정 59** 이메일 단일 확정 | `REQUIREMENTS.md` §8-1 |

**다음 액션**: ① 보호자 초대 채널 이메일/SMS 확정 ② backend merge 실행 승인(build) ③ frontend FE-18 commit 후 merge

---

## 2026-06-07 — planner(PLN): 사용자 결정 36차 (표준 이용시간 08-20·운영 게이트 도입 승인·보호자 초대 채널 권고)

사용자와 1:1 대화로 다음 결정. **신규 벤치마크·QA Open 입력 없음**.

| # | 항목 | 결정 | 산출물 |
|---|------|------|--------|
| **결정 55** | **수가 1밴드 = 10~13h 고정 (v1)** | 파일럿 센터 표준 이용시간 = **08:00~20:00 (12h)** → NHIS 2026 수가 밴드 매핑 = **10~13h 단일 밴드** (사용자 확정). v1.1에서 다밴드(`duration_band`) 도입 시 분리. | `REQUIREMENTS.md` §1-3-1·§3-9-1·§8·`PLAN_NOTES.md` #35·`ROADMAP.md` v1 수가 시간대 G9 |
| **결정 56** | **운영 게이트 도입 승인 (rules.md §17 충족)** | pre-commit hook·CI fail-fast·#36 패턴 카운터. **적용 범위·L1 정책은 결정 63에서 확정**(양 스트림·Fixed 차단+경고). | `PLAN_NOTES.md` #36·`rules.md` §17 |
| **(미확정)** | **보호자 초대 채널(#33)** | planner 권고: **이메일 링크 단일** (v1.1 무료채널 원칙·구현 단순·SMS·알림톡은 v2). 사용자 최종 확정 대기. | `REQUIREMENTS.md` §8·`PLAN_NOTES.md` #33 |

**다음 액션 (사용자 답변 대기)**:
1. 표준 이용시간 08-20 = **이용자 표준 일일 이용시간(10~13h 1밴드)** 해석 확인
2. 보호자 초대 채널 **이메일 / SMS / 둘 다** 확정 — API_SPEC §4 + `guardian_invitations` 스키마 잠금에 필요
3. (선택) 결정 56 운영 게이트 구현 우선순위 — v1 backend `merge_status: ready` 전 vs 후

**미해결 추적**: #27·#31·#32·**#33(planner 권고 → 사용자 최종 확정 대기)**·#34·#37(data/backups).

---

## 2026-06-07 — planner(PLN): 자동 기획 동기화 34차 (TSR 51·52차 + backend COD 35 false Fixed 철회 + frontend B07 recurrence #5 Open→Planned·FE-17·#36 양 스트림 재오픈 + Open 0건)

`build --role planner` 자동 동기화. **핵심 입력**: TSR 51차(07:58, backend — 50차 대비 **상태 완전 불변**, develop HEAD `c3b8716`·WT **DIRTY** 2 untracked V42 + `NotificationPreferenceServiceTest` **HEAD ABSENT**, **COD 35 Fixed 주장 TSR FAIL**, test `mvn test` **213/213**·WT **252/252 PASS**, develop **2 ahead of test**)·TSR 52차(08:03, frontend — 50차 `0b9b001` **CLEAN→DIRTY** 15M+5U=20 files, LogoutButton·GuardianInvitationAcceptPage J01·BillingPage.layout.test, **HEAD `0b9b001` Fixed(FE-15·FE-16) 규율 5 유효**, WT `npm test` **194/38**·754 modules·audit **0**). 벤치마크 BNK-6 **신규 입력 없음**. **Open 0건** — Planned BLOCK **B03 + backend merge(2커밋) + B02 #6 + B08 #2 + B07 #5**.

| # | 반영 | 산출물 |
|---|------|--------|
| 1 | **COD 35 false Fixed 철회** — ROADMAP v1 QA-B02·v2 B08 recurrence #2 `[x]` 철회, B02 #6·B08 #2 Planned 유지 | `ROADMAP.md`·`QA_FEEDBACK.md` Fixed 경고·`PLAN_NOTES.md` 34차 |
| 2 | **frontend B07 recurrence #5 Open→Planned** — J01 수락 UI·LogoutButton·레이아웃 회귀 WIP 20 files | `USER_STORIES.md` §16 FE-17·FE-6 #4·`ROADMAP.md` QA 매핑 |
| 3 | **#36 양 스트림 재오픈** — backend BE-6 #6 + frontend FE-6 #4 동시 recurrence | `PLAN_NOTES.md` #36 34차·결정 53 복원 |

**coder 다음 액션 (34차, 우선순위)**: ① B02 #6·B08 #2 — V42 + test develop 커밋. ② B07 #5 — FE-17 WIP develop 커밋. ③ backend merge(2커밋, 결정 54). ④ J01 API(#33·#35) → FE-17 실 API. ⑤ B03 ready → frontend merge.

**미해결 추적**: #27·#31·#32·#33·#35·**#36(양 스트림 인프라 강제)**·#37(data/backups).

---

## 2026-06-07 — planner(PLN): 자동 기획 동기화 33차 (TSR 50차 + backend B02 recurrence #6 + B08 recurrence #2 Open→Planned·V42 consent CHECK·temporal v2 follow-up 미커밋·HEAD Fixed 규율 5 유효 + frontend COD 34차 ds-* 유틸리티 전환 FE-16 + #36 backend 단독 재오픈 + Open 0건)

`build --role planner` 자동 동기화. **핵심 입력**: TSR 50차(16:15, backend — 48차 `c3b8716` **CLEAN→DIRTY 재오염**: 2 untracked `V42__guardian_notification_preferences_consent_temporal.sql`(54 lines kakao/sms consent CHECK·temporal monotonicity) + `NotificationPreferenceServiceTest.java`(128 lines/3 @Test), develop HEAD `c3b8716` 불변·**B02 #5·B08 HEAD PRESENT 유지**(규율 5 — 48차 Fixed 유효)·`git cat-file -e HEAD:V42`·test **ABSENT**(규율 6·8 위반), test `mvn test` **213/213**·develop WT **252/252 PASS**(+3)·develop **2 ahead of test**)·50차(07:17, frontend — develop HEAD `c98f98d`→**`0b9b001`**(+1커밋 COD 34차 ds-* 유틸리티 전환 9 컴포넌트·`AttendancePage.layout.test.jsx`, **17 ahead**), working tree **CLEAN**, HEAD `npm test` **187/35**·752 modules·audit **0**, 신규 Open 0). 벤치마크 BNK-6 **신규 입력 없음**. **Open 0건** — Planned BLOCK **B03(frontend merge) + backend develop→test merge(2커밋) + B02 #6 + B08 #2**.

| # | 반영 | 산출물 |
|---|------|--------|
| 1 | **backend B02 recurrence #6 + B08 recurrence #2 Open→Planned** — V42 consent CHECK·temporal + `NotificationPreferenceServiceTest` 3 @Test v2 follow-up 미커밋 | `ROADMAP.md` v1 QA-B02 `[x]` 철회·v2 BE-7 V42 follow-up·QA 매핑·`QA_FEEDBACK.md` Planned·`USER_STORIES.md` §17 BE-6/BE-7 |
| 2 | **HEAD `c3b8716` Fixed(B02 #5·B08) 규율 5 유효** — recurrence는 미커밋 v2 follow-up 단일(false Fixed 아님) | `ROADMAP.md` 핵심 진단·`QA_FEEDBACK.md` |
| 3 | **frontend COD 34차 `0b9b001` ds-* 유틸리티 전환 FE-16** — 9 컴포넌트 인라인 style 제거·`AttendancePage.layout.test.jsx`·187/35·WT CLEAN·17 ahead | `USER_STORIES.md` §16 FE-16·`ROADMAP.md` 핵심 진단 |
| 4 | **#36 backend 단독 재오픈**(결정 53) — 32차 대칭 종결 직후 backend v2 follow-up 미커밋 재발, frontend는 COD 33·34차 연속 CLEAN | `PLAN_NOTES.md` #36 33차·`ROADMAP.md` 33차 sync |

**coder 다음 액션 (33차, 우선순위)**: ① **B02 #6·B08 #2** — V42 + `NotificationPreferenceServiceTest` 완료 단위 develop 커밋(BE-6·BE-7·규율 8) 또는 stash/revert → working tree clean. ② backend develop→test `c3b8716` 2커밋 merge(결정 54). ③ J01 API(#33·#35) → B03 ready → frontend merge(17 ahead·FE-16 흡수). ④ v1.2 KPI는 v1.1 merged 후.

**미해결 추적**: #27·#31·#32·#33·#35·**#36(backend 단독 인프라 강제)**·#37(data/backups).

---

## 2026-06-07 — planner(PLN): 자동 기획 동기화 32차 (TSR 48·49차 + backend B02 #5·B08 Fixed `c3b8716` + frontend FE-15 Fixed `c98f98d` + #36 대칭 종결 + Open 0건)

`build --role planner` 자동 동기화. **핵심 입력**: TSR 48차(15:35, backend — develop HEAD `e8750d2`→**`c3b8716`**(+2커밋 COD 32차 `feac558` B08·`c3b8716` B02 #5), WT **3M+4U→CLEAN**, `git cat-file -e HEAD:` `PilotChecklistJwtE2eTest`·V41·`notification/` 9 java PRESENT(이관 규율 5·6·8 PASS), `mvn test` **249/249**, develop **2 ahead of test**)·49차(15:45, frontend — develop HEAD `4be0938`→**`c98f98d`**(+1커밋 COD 33차 FE-15, **16 ahead**), WT CLEAN, `manualChunks` 최대 393.53 kB, **186/34·752 modules·audit 0**, B07 #4 신호 소멸). 벤치마크 BNK-6 **신규 입력 없음**. **Open 0건** — Planned BLOCK **B03 + backend merge(2커밋)**.

| # | 반영 | 산출물 |
|---|------|--------|
| 1 | **backend QA-B02 #5·QA-B08 Fixed** — COD 32차 `c3b8716`·`feac558`, WT CLEAN, 249/249 | `ROADMAP.md`·`QA_FEEDBACK.md` Fixed·`USER_STORIES.md` §17 BE-6/BE-7 |
| 2 | **frontend FE-15 Fixed** — COD 33차 `c98f98d` `manualChunks`, 최대 393.53 kB | `ROADMAP.md` v1.2 FE-15·`USER_STORIES.md` FE-15·`REQUIREMENTS.md` §1-5-2 |
| 3 | **#36 대칭 종결** — 양 스트림 dirty-tree·false Fixed 소멸, 운영 게이트 예방적 보류 | `PLAN_NOTES.md` #36 32차·`ROADMAP.md` |
| 4 | **결정 54** backend develop→test merge — 2커밋 일괄 merge 권고, v2 test 검증 별도 | `PLAN_NOTES.md` 결정 54·`ROADMAP.md` |

**coder 다음 액션 (32차, 우선순위)**: ① backend develop→test `c3b8716` merge(결정 54). ② J01 API(#33·#35) → B03 ready → frontend merge(16 ahead). ③ v1.2 KPI는 v1.1 merged 후.

**미해결 추적**: #27·#31·#32·#33·#35·#37(data/backups — `.gitignore` COD 32차 반영됨, 정책 확정 잔여).

**결정 54 — backend develop→test merge 분리 정책 (32차)**: `c3b8716` HEAD가 `feac558`(v2 notification)을 이력에 포함하므로 cherry-pick 분리 비효율. → ① v1 보완 merge 즉시 권고(2커밋 일괄). ② v2 `notification_preferences` test 검증·ROADMAP v2 완료 기준은 v2 사이클 별도 평가(결정 52 패턴).

---

## 2026-06-07 — planner(PLN): 자동 기획 동기화 31차 (TSR 46·47차 + frontend B07 #3 정식 Fixed `4be0938` + 30+회 정체 종결 + backend B02 #5·B08 dirty-tree 확대·false Fixed 재확인 + Open 0건)

`build --role planner` 자동 동기화. **핵심 입력**: TSR 47차(14:45, frontend — develop HEAD `3fdc266`→**`4be0938`**(COD 31차 82 files +4589/-545, 15 ahead), WT **76→0 CLEAN**, `git cat-file -e HEAD:` FE-12/13/14 전 산출물 PRESENT(이관 규율 5 PASS)·SEC-005 localStorage 0건·**185/33·752 modules·audit 0**)·46차(14:30, backend — develop·test `@e8750d2` 동일, dirty-tree **1M+4U→3M+4U 확대**(B08 modified `MustApiEndpointRoutingTest`+64·`RoleBasedControllerAccessTest`+93), COD Fixed(B02 #5·B08) **TSR + planner 직접 검증 FAIL**(HEAD ABSENT), WT 249/249). 벤치마크 BNK-6 **신규 입력 없음**. **Open 0건** — Planned BLOCK **B03 + B02 #5 + B08**(B07 #3 소멸).

| # | 반영 | 산출물 |
|---|------|--------|
| 1 | **frontend QA-B07 recurrence #3 Fixed** — COD 31차 `4be0938` 82 files 일괄 커밋·WT CLEAN·HEAD 전 산출물 PRESENT | `ROADMAP.md` 핵심 진단·QA 매핑·`QA_FEEDBACK.md` Fixed·`PLAN_NOTES.md` 31차 sync |
| 2 | **#36 비대칭 종결** — frontend FE-6 #3 해소(30+회 정체 종결)·backend B02 #5·B08 false Fixed 단독 잔존 | `PLAN_NOTES.md` #36 31차 갱신·`ROADMAP.md` #36 |
| 3 | **backend B08 dirty-tree 확대** — modified MustApi/RBAC tests + false Fixed 재확인 | `ROADMAP.md` QA 매핑 B08·`QA_FEEDBACK.md` B08 |
| 4 | **FE-15 번들 코드 스플릿(비차단 LOW)** — JS 청크 744.95 kB(>500kB)→`manualChunks` | `PLAN_NOTES.md` #38·`USER_STORIES.md` FE-15 |

**coder 다음 액션 (31차, 우선순위)**: ① **B02 #5** `PilotChecklistJwtE2eTest.java` develop commit. ② **B08** `notification_preferences`(7 java/8 @Test + V41 + modified 2 test) develop commit 또는 stash/revert. ③ `.gitignore` `data/backups/`(#37). ④ v1.1 J01(#33·#35) → **B03 `merge_status: ready`** → develop→test merge(B07 #3 15 ahead 동반). ⑤ FE-15 코드 스플릿(#38, 비차단).

**미해결 추적**: #27·#31·#32·#33·#35·**#36(backend 한정 인프라 강제)**·#37(data/backups)·**#38(번들 코드 스플릿)**.

**결정 53 — #36 에스컬레이션 backend 스트림 한정 축소 (31차)**: COD 31차 `4be0938`로 frontend dirty-tree 누적(26→44→60→61→72→76→**0**) 종결·B07 #3 Fixed → FE-6 패턴 #3 **해소**. backend는 B02 #5·B08 false Fixed 반복(TSR 46차 HEAD ABSENT)으로 운영 게이트(pre-commit hook `git diff --quiet` on `src/test`·CI fail-fast) 권고를 **backend 스트림 한정**으로 유지. frontend는 자율 정착 도달로 권고 보류 가능.

---

## 2026-06-07 — planner(PLN): 자동 기획 동기화 30차 (TSR 45차 + frontend B07 #3 72→76 files + `FeeScheduleTable`(+test) + WT 181/30·749 modules + backend 44차 baseline 불변 + Open 0건)

`build --role planner` 자동 동기화. **핵심 입력**: TSR 45차(14:02, frontend — develop HEAD `3fdc266` 불변, WT 72→**76 files**, 신규 **`FeeScheduleTable`(+test)**, **181/30·749 modules·audit 0**). backend(44차 baseline) develop·test `@e8750d2`·B02 #5·B08 dirty-tree·COD Fixed FAIL — **변화 없음**. 벤치마크 BNK-6 **신규 입력 없음**. **Open 0건** — Planned BLOCK **B03 + B02 #5 + B07 #3 + B08**.

| # | 반영 | 산출물 |
|---|------|--------|
| 1 | **frontend B07 #3 72→76 files** — `FeeScheduleTable`(+test) 수가표 테이블 UI | `ROADMAP.md` v1.2·`USER_STORIES.md` FE-13·`REQUIREMENTS.md` §1-5-2 |
| 2 | **FE-13 `FeeScheduleTable`** — US-G00a·케어포 9-x·HEAD `FeeRateHistoryPanel` 연계 | `PLAN_NOTES.md` 30차 sync·`QA_FEEDBACK.md` Planned B07 |
| 3 | **#36 30차 연속 coder 미조치** — dirty-tree 26→…→76 | `PLAN_NOTES.md` #36 |

**coder 다음 액션 (불변·우선순위)**: ① B02 #5·B08 backend commit(or stash)·`.gitignore`(#37). ② B07 #3 frontend **76 files** commit(FE-12/13/14 cluster, FE-13에 `FeeScheduleTable` 포함). ③ v1.1 J01 → B03 ready → merge.

**미해결 추적**: #27·#31·#32·#33·#35·**#36(인프라 강제 단계 진입)**·#37(data/backups 추적 정책).

---

## 2026-06-07 — planner(PLN): 자동 기획 동기화 29차 (TSR 42·43차 + backend B08 @Test 5→8 + frontend B07 #3 61→72 files + 청구·건강·NHIS·보호자 UI WIP + Open 0건)

`build --role planner` 자동 동기화. **핵심 입력**: TSR 42차(13:25 backend — develop·test `@e8750d2` 동일·40·41차 대비 **상태 불변**, B08 @Test **5→8**, WT `mvn test` **243/243**(+3), COD Fixed FAIL 재확인)·43차(13:27 frontend — develop HEAD `3fdc266` 불변, WT 61→**72 files**, 신규 `BillingStatusConfirmModal`·`CopayRateTable`·`GuardianDailySummary`·`HealthAlertList`·`NhisImportGuidePanel`(+tests), **179/29·748 modules·audit 0**). 벤치마크 BNK-6 **신규 입력 없음**. **Open 0건** — Planned BLOCK **B03 + B02 #5 + B07 #3 + B08**.

| # | 반영 | 산출물 |
|---|------|--------|
| 1 | **backend 42차 상태 불변·B08 @Test 5→8** — WT 243/243·COD Fixed FAIL 재확인 | `ROADMAP.md` v2 BE-7·`USER_STORIES.md` BE-7 |
| 2 | **frontend B07 #3 61→72 files** — 청구·copay·건강 알림·NHIS 가이드·보호자 요약 UI | `ROADMAP.md` v1.2·`USER_STORIES.md` FE-12·FE-13·`REQUIREMENTS.md` §1-5-2 |
| 3 | **FE-12 `HealthAlertList`·FE-13 청구/NHIS/copay/보호자 UI** 매핑 | `USER_STORIES.md` §16·`ROADMAP.md` QA→태스크 |
| 4 | **#36 29차 연속 coder 미조치** — 인프라 강제 단계 진입 승격 | `PLAN_NOTES.md` #36 |

**coder 다음 액션 (불변·우선순위)**: ① B02 #5·B08 backend commit(or stash)·`.gitignore`(#37). ② B07 #3 frontend **72 files** commit(FE-12/13/14 cluster). ③ v1.1 J01 → B03 ready → merge.

**미해결 추적**: #27·#31·#32·#33·#35·**#36(인프라 강제 단계 진입)**·#37(data/backups 추적 정책).

---

## 2026-06-07 — planner(PLN): 자동 기획 동기화 27차 (TSR 40·41차 + backend COD false Fixed 철회 + `.gitignore` 부분 진전 + frontend 41차 상태 불변 + Open 0건)

`build --role planner` 자동 동기화. **핵심 입력**: TSR 40차(12:45 backend — develop·test `@e8750d2` 동일, `.gitignore` +`data/backups/` 1M 미커밋·`data/backups/` untracked 소멸, **COD Fixed 주장(B02 #5·B08) TSR 독립 검증 FAIL** — HEAD ABSENT, WT `mvn test` 240/240, HEAD `@Test` 199·WT 226)·41차(12:52 frontend — develop HEAD `3fdc266` 불변, WT 60→**61 files**(±1 modified), 169/24·743 modules·audit 0). 벤치마크 BNK-6 **신규 입력 없음**. **Open 0건** — Planned BLOCK **B03 + B02 #5 + B07 #3 + B08**.

| # | 반영 | 산출물 |
|---|------|--------|
| 1 | **COD false Fixed 철회** — B02 #5·B08 develop HEAD ABSENT, v1 QA-B02·v2 BE-7 `[x]` 철회 | `ROADMAP.md` v1·v2 완료 기준·QA→태스크 매핑 |
| 2 | **`.gitignore` 부분 진전** — `data/backups/` 1M 미커밋, untracked manifest 소멸(#37) | `PLAN_NOTES.md` 27차·`ROADMAP.md` 핵심 진단 |
| 3 | **frontend 41차 상태 불변** — 61 files(±1 modified), WT 품질 PASS | `ROADMAP.md`·`USER_STORIES.md`·`QA_FEEDBACK.md` |
| 4 | **#36 인프라 강제 단계 진입 검토** — 27차 연속 coder 미조치 + false Fixed 재발 | `PLAN_NOTES.md` #36 |

---

## 2026-06-07 — planner(PLN): 자동 기획 동기화 26차 (TSR 38·39차 + 상태 불변 + B07 #3 44→60 files·계정 보안·로그인 이력 UI WIP·FE-14 §3-1 매핑 확장 + B08 dirty-tree 잔존 + COD 03:08 부분 진전·develop 미커밋 + Open 0건)

`build --role planner` 자동 동기화. **핵심 입력**: TSR 38차(12:05 backend — develop·test `@e8750d2` 완전 불변, Maven 213/213(75 suites), JAR 82,868,029 B, SEC-007 test PRESENT, WT DIRTY 불변 B02 #5 + B08 7 java/5 @Test + `data/backups/` manifest, HEAD `@Test` 199·WT 226)·39차(12:09 frontend — develop HEAD `3fdc266` 불변, WT 44→**60 files**(36M+24U), 신규 계정 보안·로그인 이력 UI `LoginHistoryPanel`(+test, §3-1 로그인 이력)·`PasswordChangeModal`(+test, §3-1 비밀번호 재설정·**COD 03:08 SettingsPage 보안 탭 연결**)·`PasswordResetRequestModal`(+test, §3-1)·`PlatformOrgDetailModal`(+test, US-A01 Tenant 상세)·`SettingsPage.test`·`HealthTrendChart.test`(FE-12 회귀), 169/24·743 modules·audit 0). 벤치마크 BNK-6 **신규 입력 없음**. **양 스트림 HEAD·dirty-tree 사유 불변·COD 03:08 부분 진전이나 develop 미커밋 지속**. **Open 0건** — Planned BLOCK **B03 + B02 #5 + B07 #3 + B08**.

| # | 반영 | 산출물 |
|---|------|--------|
| 1 | **B07 #3 범위 확대 44→60 files** — 계정 보안·로그인 이력 UI(§3-1 인증 매핑) + PlatformOrgDetailModal·FE-12 테스트 회귀 | `ROADMAP.md` v1.2·`USER_STORIES.md` §16·`QA_FEEDBACK.md` |
| 2 | **FE-14 §3-1 매핑 확장** — 운영·보안 설정에 비밀번호 변경·재설정·로그인 이력 추가, REQUIREMENTS §3-1 인증 모듈 매핑 | `USER_STORIES.md` FE-14·`ROADMAP.md` v1.2 |
| 3 | **FE-13 PlatformOrgDetailModal(+test) 추가** — US-A01 Tenant 상세 UX 보강 | `USER_STORIES.md` FE-13 |
| 4 | **COD 03:08 부분 진전·develop 미커밋** — SettingsPage 보안 탭 통합(로컬 169/24·743 modules PASS) | `PLAN_NOTES.md` 26차 sync·`QA_FEEDBACK.md` Planned |
| 5 | **#36 인프라 강제 검토 진입** — pre-commit hook·CI fail-fast `git diff --quiet` check 권고 강화·26차 연속 미조치 | `PLAN_NOTES.md` #36 26차 갱신 |

**핵심 판단**: ① **테스트 PASS ≠ 이관 PASS 26차 연속** — coder 03:08 진전이나 develop 미커밋·인프라 강제 권고 단계 진입. ② **B07 #3 신규 컴포넌트는 §3-1 인증 모듈 매핑** — 비밀번호 변경·재설정·로그인 이력은 REQUIREMENTS §3-1에 이미 정의된 기능을 UI로 충족(FE-14 확장). ③ **PlatformOrgDetailModal**은 US-A01 Tenant 상세(FE-13). ④ **잔여 BLOCK = merge(B03) + dirty-tree commit(B02 #5·B07 #3·B08)**.

**coder 다음 액션 (불변·우선순위)**: ① B02 #5·B08 backend commit(or stash)·`data/backups/` 정리(#37). ② B07 #3 frontend **60 files** commit(분리 권장: Recharts FE-12 / Platform·배치 FE-13 / 운영·보안·계정 보안·로그인 이력 FE-14). ③ v1.1 J01 → B03 ready → merge.

**미해결 추적**: #27·#31·#32·#33·#35·**#36(인프라 강제 검토 진입)**·#37(data/backups 추적 정책).

---

## 2026-06-07 — planner(PLN): 자동 기획 동기화 25차 (TSR 36·37차 + 상태 불변 + B07 #3 26→44 files·FE-14 신설 + B08 dirty-tree 잔존 + Open 0건)

`build --role planner` 자동 동기화. **핵심 입력**: TSR 36차(11:25 backend — develop·test `@e8750d2` 동일, Maven 213/213(75 suites), SEC-007 test PRESENT, WT DIRTY 불변 B02 #5 + B08 `notification_preferences` 6→**7 java**·4→**5 @Test** + `data/backups/` manifest untracked, HEAD `@Test` 199·WT 226)·37차(11:30 frontend — develop HEAD `3fdc266` 불변, WT 26→**44 files**(26M+18U), 신규 운영/보안 설정 UI `AuditLogPanel`·`BackupSettingsPanel`·`PasswordChangeModal`·`FilterChips`, 161/20·741 modules PASS, B07 #3 범위 확대). 벤치마크 BNK-6 **신규 입력 없음**. **양 스트림 HEAD·dirty-tree 사유 불변·coder 미조치 지속**. **Open 0건** — Planned BLOCK **B03 + B02 #5 + B07 #3 + B08**.

| # | 반영 | 산출물 |
|---|------|--------|
| 1 | **B07 #3 범위 확대 26→44 files** — 신규 운영/보안 설정 UI(감사 로그·백업·비밀번호·FilterChips) | `ROADMAP.md` v1.2·`USER_STORIES.md` §16·`QA_FEEDBACK.md` |
| 2 | **FE-14 신설** — 운영·보안 설정 UI epic(FE-12 차트·FE-13 플랫폼과 분리) | `USER_STORIES.md` §16·`ROADMAP.md` v1.2 |
| 3 | **B08 소폭 확대** — `notification_preferences` 6→7 java·4→5 @Test + `data/backups/` untracked | `ROADMAP.md` v2·`QA_FEEDBACK.md` Planned |
| 4 | **상태 불변·coder 미조치 연속** — #36 운영 게이트 권고 강화 유지 | `PLAN_NOTES.md` 25차 sync·#36 |
| 5 | **#37 `data/backups/` 추적 정책** 신설(.gitignore vs manifest 추적) | `PLAN_NOTES.md` 추가 질문 #37 |

**핵심 판단**: ① **테스트 PASS ≠ 이관 PASS** — 양 스트림 WT 품질 PASS(213/213·161/20)이나 dirty-tree(B02 #5·B07 #3·B08)로 BLOCK 불변. ② **B07 #3 신규 컴포넌트는 운영/보안 설정** — 차트(FE-12)·플랫폼(FE-13) 범위를 벗어나 **FE-14**로 분리(BNK-6 운영/보안 모듈 패리티). ③ **24→25차 변화 = 범위 누적 확대만**, 신규 commit 0·신규 Open 0. ④ **잔여 BLOCK = merge(B03) + dirty-tree commit(B02 #5·B07 #3·B08)**.

**coder 다음 액션 (불변)**: ① B02 #5·B08 backend commit(or stash)·`data/backups/` 정리. ② B07 #3 frontend 44 files commit(FE-12·FE-13·FE-14). ③ v1.1 J01 → B03 ready → merge.

**미해결 추적**: #27·#31·#32·#33·#35·**#36(운영 게이트 권고 강화)**·**#37(data/backups 추적 정책)**.

---

## 2026-06-07 — planner(PLN): 자동 기획 동기화 24차 (TSR 34·35차 + B08 Open→Planned + B07 #3 26 files + v1 merged·SEC-007 test 해소)

`build --role planner` 자동 동기화. **핵심 입력**: TSR 34차(01:45 backend — develop·test `@e8750d2` merged, Maven 213/213, SEC-007 test PRESENT, WT 8 files B02 #5 + v2 `notification_preferences` WIP → **QA-B08 Planned**)·35차(01:50 frontend — develop HEAD `3fdc266` 불변, WT 18→**26 files**, 144/13·738 modules PASS, B07 #3 범위 확대). 벤치마크 BNK-6 **신규 입력 없음**. **Open 0건** — Planned BLOCK **B03 + B02 #5 + B07 #3 + B08**.

| # | 반영 | 산출물 |
|---|------|--------|
| 1 | **B08 Open→Planned** — v2 `notification_preferences` V41 + 6 java + 4 @Test WIP | `ROADMAP.md` v2·`USER_STORIES.md` §17 BE-7·`API_SPEC.md` §11·`QA_FEEDBACK.md` |
| 2 | **B07 #3 범위 확대** — 18→26 files(`BatchProgressSteps`·Platform WIP) | `ROADMAP.md` v1.1·v1.2·`USER_STORIES.md` FE-13·`REQUIREMENTS.md` §1-5-2 |
| 3 | v1 **`merged`**·SEC-007 test 해소·Maven 213/213 | `ROADMAP.md` 핵심 진단·`QA_FEEDBACK.md` |
| 4 | **이관 규율 8항** — v2 선행 dirty-tree 금지 | `ROADMAP.md`·결정 53·`PLAN_NOTES.md` |
| 5 | **FE-13·BE-7** 신설 | `USER_STORIES.md` §16·§17 |

**핵심 판단**: ① **v1 merged 후 v2 선행 WIP** = B08 BLOCK(규율 8). ② **B07 #3 Platform·배치 UI** = BNK-6 HQ/플랫폼 패리티(FE-13). ③ **잔여 BLOCK = merge(B03) + dirty-tree commit(B02 #5·B07 #3·B08)**.

**coder 다음 액션**: ① B02 #5·B08 backend commit(or stash). ② B07 #3 frontend 26 files commit. ③ v1.1 J01 → B03 ready → merge.

**미해결 추적**: #27·#31·#32·#33·#35·**#36(운영 게이트 권고 강화)**.

---

## 2026-06-07 — planner(PLN): 자동 기획 동기화 23차 (TSR 32·33차 + B02 #5·B07 #3 recurrence + v1 merged + Recharts WIP + planner 22차 false `[x]` 철회)

`build --role planner` 자동 동기화. **핵심 입력**: TSR 32차(01:30 backend — develop HEAD `e8750d2` 불변, working tree DIRTY 1 untracked `PilotChecklistJwtE2eTest.java` 634 lines/22 @Test, **QA-B02 #5**, planner 22차 false `[x]`, backend test `@e8750d2` merge 완료)·33차(01:16 frontend — develop HEAD `3fdc266` 불변, working tree DIRTY 18 files Recharts WIP, WT 142/12·736 modules PASS, **QA-B07 #3**). v1 **`merged`**·B05 Fixed. 벤치마크 BNK-6 **신규 입력 없음**. **Open 0건** — Planned BLOCK **B03 + B02 #5 + B07 #3**.

| # | 반영 | 산출물 |
|---|------|--------|
| 1 | **B02 #5 Open→Planned** — `PilotChecklistJwtE2eTest` untracked, v1 §6·P1–P8 `[x]` **철회**, BE-6 #5 재발 | `ROADMAP.md` v1·`USER_STORIES.md` §13·§17·`QA_FEEDBACK.md` |
| 2 | **B07 #3 Open→Planned** — Recharts 18 files WIP, v1.1 QA-B04·B07 @HEAD `[x]` **철회**, FE-6 #3 재발 | `ROADMAP.md` v1.1·v1.2·`USER_STORIES.md` FE-12·US-M02 |
| 3 | v1 **`merged`**·B05 Fixed·backend test merge 완료 | `ROADMAP.md` v1·`QA_FEEDBACK.md` Fixed |
| 4 | **v1.2 Recharts 차트 레이어 P0** — BNK-6-4·US-M02·FE-12 | `ROADMAP.md` v1.2·`REQUIREMENTS.md` §1-5-2·§6-3 |
| 5 | **#36 에스컬레이션 강화** — 21차 「8커밋 무재발」 철회, planner 22차 false `[x]` | `PLAN_NOTES.md` 23차 sync |

**핵심 판단**: ① **테스트 PASS ≠ 이관 PASS** — WT 품질은 PASS이나 dirty-tree가 BLOCK. ② **planner 22차 오류** — `PilotChecklistJwtE2eTest` develop HEAD 미존재 상태 `[x]` 부여(규율 5). ③ **Recharts WIP** = v1.2 P0(BNK-6 대시보드 3블록·HQ 비교). ④ **잔여 BLOCK = B03(merge) + B02 #5 + B07 #3(commit)**.

**coder 다음 액션**: ① B02 #5·B07 #3 develop commit. ② v1.1 J01(#33·#35) → B03 ready → merge. ③ v1.2 Recharts·≥60% KPI는 v1.1 merged 후.

**미해결 추적**: #27·#31·#32·#33·#35·**#36(운영 게이트 권고 강화)**.

---

## 2026-06-07 — planner(PLN): 자동 기획 동기화 21차 (TSR 30·31차 + B02 #4 Fixed + COD 22 pilotPageFlows P1–P8 페이지 E2E + UXD 14 FeeRateHistoryPanel + 결정 52 흡수 8묶음)

`build --role planner` 자동 동기화. **핵심 입력**: TSR 30차(00:28 backend — develop HEAD `c3f3146`→**`e8750d2`**(+1커밋 COD 21차 `SevenRoleJwtLoginE2eTest.java` 384 lines 7역할 JWT live filter-chain E2E), working tree **CLEAN**, `@Test` 183→**199**(+16), Maven 79/79 PASS, **QA-B02 recurrence #4 Fixed**, v1 R-04 live JWT E2E **[x]**)·31차(00:43 frontend — develop HEAD `57ff3c0`→`a42d6fb`→**`3fdc266`**(+2커밋: UXD 14차 `FeeRateHistoryPanel`·`chartColors.js` 8 files; COD 22차 `pilotPageFlows.test.jsx` 433 lines P1–P8 페이지 RTL E2E), **14커밋 ahead**, working tree **CLEAN**, `npm test` **140/11 PASS**(+10/+1), build 113 modules, audit 0건). 벤치마크 BNK-6 **신규 입력 없음**. **Open 0건** — Planned BLOCK **4건**(B01·B03·B05·SEC-007 merge 게이트 단일) 불변.

| # | 반영 | 산출물 |
|---|------|--------|
| 1 | TSR 30차 **QA-B02 recurrence #4 Fixed** — COD 21차 `e8750d2` `SevenRoleJwtLoginE2eTest` develop commit, `@Test` 199, Maven 79/79 PASS, working tree CLEAN. v1 R-04 「7역할 라이브 JWT 로그인 E2E」**[x] 충족**. Planned BLOCK 5→4 | `ROADMAP.md` v1 QA-B02 `[x]`·핵심 진단 31차·`USER_STORIES.md` §17 BE-6 #4 Fixed |
| 2 | TSR 31차 **frontend R-05 P1–P8 페이지 단위 E2E PARTIAL 강화** — COD 22차 `3fdc266` `pilotPageFlows.test.jsx`(433 lines), `npm test` 130/10→**140/11 PASS**, build 113 modules, audit 0건 | `ROADMAP.md` v1.1 Must API E2E PARTIAL·`USER_STORIES.md` §13·**FE-11 신설** |
| 3 | TSR 31차 **UXD 14차 `a42d6fb` 흡수 (결정 52)** — `FeeRateHistoryPanel.jsx`·`FeeSchedulePage` 이력 모달·`chartColors.js`·`BATCH_STATUS` 8 files. **US-G00a PARTIAL**(이력 UI) | `USER_STORIES.md` US-G00a·`ROADMAP.md` v1.1 메모 |
| 4 | **결정 52 흡수 8묶음 갱신** — ①~⑦ 20차 7묶음 + ⑧ UXD 14차 + COD 22차 = 총 **14커밋 / ~98 files** v1.1 develop→test merge 동반 | `ROADMAP.md`·`PLAN_NOTES.md` |
| 5 | **#36 에스컬레이션 갱신** — BE-6 #4 Fixed(30차 commit). FE-6 **8커밋 무재발**. 운영 게이트 권고는 **예방적** 잔존 | `PLAN_NOTES.md` 21차 sync |
| 6 | 21차 동기화 기록 | `decisions.md` |

**핵심 판단**: ① **backend B02 #4 Fixed** — dirty-tree·B02 사유 **완전 소멸**. 잔여 v1 BLOCK = **merge 게이트(B01·SEC-007) + REQUIREMENTS §6 체크리스트 + P1–P8 라이ve E2E(post-merge)**. ② **frontend R-05 페이지 E2E PARTIAL 강화** — fetch-mock 라우팅(FE-9) + 7역할 매트릭스 위 **페이지 통합 회귀(FE-11)**. 라이ve backend·J01 API 잔여. ③ **UXD 14차 US-G00a 이력 UI** — 백엔드 live 이력 API는 merge 후. ④ **잔여 BLOCK = merge 게이트 4건 단일** — 기능(J01)·절차(merge ready·§6)만 잔여.

**coder 다음 액션**: ① v1 **REQUIREMENTS §6 coder 자체 점검** + P1–P8 라이ve E2E(post-merge) → `merge_status: ready` → B01·SEC-007. ② v1.1 J01(#33·#35 결정 후) → DBA V41 → COD → B03 ready → merge(흡수 8묶음·B05). ③ v1.2 ≥60% KPI는 v1.1 merged 후.

**미해결 추적**: #27·#31·#32·#33·#35·**#36(운영 게이트 권고 예방적 잔존)**.

---

## 2026-06-06 — planner(PLN): 자동 기획 동기화 20차 (TSR 28·29차 + B02 recurrence #4 Open→Planned + UXD 13차 Switch·셀프 체크인 토글 흡수 + COD 20차 7역할 JWT 로그인·라우트 가드 Vitest 단위 E2E 자동화 정식 충족 + US-UX-03 신설 + BE-6 패턴 #4 재발·종결 공언 철회)

`build --role planner` 자동 동기화. **핵심 입력**: TSR 28차(23:19 양 스트림 — backend develop HEAD `c3f3146` 불변·working tree DIRTY 1 untracked `src/test/java/com/ogada/backend/security/SevenRoleJwtLoginE2eTest.java` 384 lines 7역할 JWT 로그인 E2E 통합 테스트 WIP — Spring Security filter chain·JwtAuthFilter·UserDetailsService 통합 라이브 발급/검증, 이관 규율 6 위반 → QA-B02 recurrence #4 Open·BE-6 #4 재발; frontend UXD 13차 `07fd305` `feat(ux): 전사 설정 Switch 컴포넌트·셀프 체크인 토글` — `Switch.jsx`(WAI-ARIA `role=switch`·`aria-checked`·44px hit·`forced-colors`)·`SettingsPage.jsx` `allow_client_self_checkin` 토글·`Switch.test.jsx` 5건 회귀, 7 files +218/-7, working tree CLEAN, `npm test` 32/7→37/8·build 112 modules·audit 0건)·29차(23:31 frontend COD 20차 `57ff3c0` — `sevenRoleJwtLogin.test.jsx`(132)·`sevenRoleRouteGuard.test.jsx`(83)·`sevenRoleRouteMatrix.js`(75)·`roleHomePaths.test.jsx`(+26) 4 files +316: 7역할 JWT 로그인·라우트 가드 Vitest 단위 E2E 자동화, working tree CLEAN, `npm test` 37/8→**130/10 PASS**(+93 tests/+2 files)·build 112 modules·audit 0건, FE-7 회귀 없음). 벤치마크 BNK-6 **신규 입력 없음**.

| # | 반영 | 산출물 |
|---|------|--------|
| 1 | TSR 28차 **QA-B02 recurrence #4 Open → Planned** — backend develop HEAD `c3f3146` 불변·working tree DIRTY 1 untracked `SevenRoleJwtLoginE2eTest.java` 384 lines 7역할 JWT 로그인 E2E 통합 테스트 WIP·이관 규율 6 위반·BE-6 #4 재발(19차 5커밋 무재발 종결 공언 철회). HEAD Fixed 산출물(`PilotChecklistApiAccessTest`·`MustApi`·RBAC·`ProductionSecretValidator`·V39·V40) 규율 5 PASS 유지·`@Test` 183·Maven 79/79 PASS | `QA_FEEDBACK.md` Planned 신규 항목·Fixed B02 recurrence #4 note·`ROADMAP.md` v1 QA-B02 `[x]` 철회·BE-6 종결 공언 철회 |
| 2 | TSR 29차 **frontend R-04 7역할 JWT 로그인·라우트 가드 Vitest 단위 E2E 자동화 정식 충족** — COD 20차 `57ff3c0` `sevenRoleJwtLogin.test.jsx`(132 lines AuthProvider login + LoginPage submit 7역할 매트릭스 platform_admin→/platform·hq_admin→/dashboard/hq·branch_admin·social_worker·caregiver→/dashboard·guardian·client_user→/guardian·sysadmin→/settings)·`sevenRoleRouteGuard.test.jsx`(83 lines ProtectedRoute 7역할 허용·거부 매트릭스 E2E)·`sevenRoleRouteMatrix.js`(75 lines 라우트 접근 매트릭스 모듈)·`roleHomePaths.test.jsx`(+26) 4 files +316; `npm test` 37/8→**130/10 PASS**(+93/+2)·build 112 modules·audit 0건 — 라이브 backend 통합 E2E는 `SevenRoleJwtLoginE2eTest` commit + B01 merged 후 | `ROADMAP.md` v1.1 7역할 화면·메뉴 `[x]` 강화·v1 P1–P8 양 스트림 PARTIAL 강화·USER_STORIES §13 단위 자동화 진전 갱신·§16 FE-9 갱신 |
| 3 | TSR 28차 **UXD 13차 `07fd305` 흡수 (결정 52 적용)** — `Switch.jsx` WAI-ARIA·`SettingsPage.jsx` `allow_client_self_checkin` 토글·`Switch.test.jsx` 5건 (결정 16 안 3 `client_user` 조건부 활성화의 UI 정착, DESIGN_SYSTEM §1 컴포넌트·§9 접근성 확장) → v1.1 develop→test merge 동반 흡수 | `ROADMAP.md` v1.2 흡수 7묶음 갱신·`PLAN_NOTES.md` 20차 sync·USER_STORIES Epic UX **US-UX-03 신설**·§14 합계 45→46 |
| 4 | USER_STORIES **US-UX-03 신설** (전사 설정 Switch·셀프 체크인 토글, v1.1, 결정 16 안 3 UI 정착) — 인수 조건 5건 [x](Switch WAI-ARIA·44px hit·forced-colors·SettingsPage 토글·Switch.test 5건)·1건 [ ](라이브 backend 연동 — v1.1 merge 후); UXD 13차 `07fd305` 반영 | `USER_STORIES.md` §12a Epic UX |
| 5 | USER_STORIES **§16 FE-9 갱신**(7역할 라우트 매트릭스·홈 경로·로그인 단위 E2E 매트릭스 자동화 추가 — `sevenRoleJwtLogin.test.jsx`·`sevenRoleRouteGuard.test.jsx`·`sevenRoleRouteMatrix.js`)·**§16 FE-10 신설**(전사 Switch WAI-ARIA·forced-colors)·**§17 BE-6 recurrence #4 갱신**(5커밋 무재발 종결 공언 철회·운영 게이트 권고 재검토) | `USER_STORIES.md` |
| 6 | **#36 에스컬레이션 재오픈** — BE-6 #4 재발로 19차 「5커밋 무재발 완전 종결」 공언 철회. FE-6는 무재발 6커밋 유지(`a84473f`→`ed1bf22`→`404a30e`→`cc34f23`→`07fd305`→`57ff3c0`) — 양 스트림 비대칭. **운영 게이트(pre-commit hook 등) 권고 재검토 필요**: ① backend Maven CI에 「신규 `*Test.java` 파일 working tree 한정」 fail-fast 검증 추가, ② coder 워크플로우 가이드에 「테스트 작성 직후 `mvn -q test` PASS → 즉시 develop commit」 체크포인트 명시, ③ planner 자동 sync 시 「BE-6 패턴 #N 재발」 카운터 자동 갱신 | `PLAN_NOTES.md` 20차 sync·#36 갱신·`USER_STORIES.md` §17 BE-6·BE-6 패턴 종결 공언 철회 주석 |
| 7 | **결정 52 흡수 7묶음 갱신** — ① v1.2 P0 `a72e249`(42 files), ② US-D03 `3fc549a`(2), ③ UXD 10차 `5656e19`(7), ④ UXD 11차 `2d742b3`(7), ⑤ COD 17차 `a84473f`+`ed1bf22`(10), ⑥ UXD 12차 `404a30e`(3)+COD 18차 `c3f3146`(1)+COD 19차 `cc34f23`(3), ⑦ **UXD 13차 `07fd305`(7)+COD 20차 `57ff3c0`(4)** — 총 12커밋 / ~89 files 모두 v1.1 develop→test merge 시 동반 승격. v1.2 정식 완료 기준(2단 SideNav 모듈 가중 커버리지 ≥60%·E2E·등급이력 UI)은 v1.1 merged 후 v1.2 사이클 | `ROADMAP.md` 핵심 진단 29차·v1.2 흡수 메모·`PLAN_NOTES.md` 결정 52 흡수 7묶음 갱신 |
| 8 | 20차 동기화 기록 | `decisions.md` |

**핵심 판단**: ① **backend B02 recurrence #4 Open → Planned, BE-6 종결 공언 철회** — 19차에 「BE-6 5커밋 무재발 완전 종결」 공언했으나 20차 TSR 28차에서 신규 7역할 JWT 로그인 E2E 통합 테스트 `SevenRoleJwtLoginE2eTest.java`(384 lines, Spring Security filter chain·JwtAuthFilter·UserDetailsService) develop 미커밋으로 #4 재발. 19차 5커밋 무재발 → 20차 1커밋 dirty. coder가 `mvn -q test` PASS 후 develop commit 시 B02 #4 자동 Fixed + v1 R-04 라이브 7역할 JWT 로그인 E2E 완료 기준 동시 충족 → B01·SEC-007 동반 해소 경로 단축. ② **frontend R-04 7역할 JWT 로그인·라우트 가드 단위 E2E 자동화 정식 충족** — COD 20차 `57ff3c0` 4 files +316으로 AuthProvider login + LoginPage submit + ProtectedRoute 7역할 허용·거부 매트릭스 단위 검증 자동화, `npm test` 130/10 PASS. FE-6 무재발 6커밋 유지. ③ **UXD 13차 Switch·셀프 체크인 토글 흡수**(결정 52) — `Switch.jsx` WAI-ARIA·`SettingsPage` `allow_client_self_checkin` 토글·`Switch.test.jsx` 5건. 결정 16 안 3(`client_user` 조건부 활성화) UI 정착. **US-UX-03 신설**. ④ **결정 52 흡수 7묶음 갱신** — 총 12커밋/~89 files (v1.2 P0·US-D03·UXD 10/11/12/13차·COD 17/18/19/20차) 모두 v1.1 develop→test merge 시 동반 승격. ⑤ **잔여 BLOCK = merge 게이트(B01·B03·B05·SEC-007) + B02 #4(BE-6 commit)** — 잔여는 backend 1 commit(`SevenRoleJwtLoginE2eTest.java`)·기능(J01 backend API)·절차(merge ready). ⑥ #36 에스컬레이션 **재오픈** — BE-6 종결 공언 철회, 운영 게이트 권고 재검토 필요.

**coder 다음 액션**: ① **B02 recurrence #4 commit(BE-6 우선)** — `SevenRoleJwtLoginE2eTest.java` 384 lines `mvn -q test` PASS 확인 후 develop commit → B02 #4 자동 Fixed + v1 R-04 라이브 7역할 JWT 로그인 E2E 완료 기준 충족 → 잔여 v1 `[ ]`(P1–P8 라이브 E2E·SEC-007 test 승격) 진행 → `merge_status: ready` → B01·SEC-007 동반 해소. ② v1.1 J01 백엔드 API: PLN 명세(#33 채널·#35 만료 정책 결정 후) → DBA `guardian_invitations` V41 migration → COD 백엔드 구현 → COD 프론트 실 API 연동(스텁 제거) → B03 ready → merge(흡수 7묶음 자동 동반·결정 52, B05 동반 해소). ③ v1.2 본격 사이클(2단 SideNav 모듈 가중 커버리지 ≥60%·E2E·등급이력 UI)은 v1.1 merged 후.

**미해결 추적**: #27·#31·#32·#33(보호자 알림 채널 1종 — J01 백엔드 API 명세 선행)·#35(`guardian_invitations` 스키마·만료/재발송 정책)·**#36(BE-6 패턴 #4 재발·종결 공언 철회·운영 게이트 권고 재검토 — 20차 재오픈)**.

---

## 2026-06-06 — planner(PLN): 자동 기획 동기화 19차 (TSR 26·27차 + PilotChecklistApiAccessTest 29 @Test + pilotChecklist fetch-mock 자동화 + UXD 12차 LoginPage DS·Modal 접근성)

`build --role planner` 자동 동기화. **핵심 입력**: TSR 26차(22:20 양 스트림 — backend COD 18차 `c3f3146` `PilotChecklistApiAccessTest` 697 lines **29 @Test**(USER_STORIES §13 P1–P8 × 7역할 `@PreAuthorize` `@WebMvcTest` 자동화), develop CLEAN·`@Test` 154→**183**, Maven 79/79 PASS; frontend UXD 12차 `404a30e` `LoginPage.jsx`·`Modal.jsx`·`components.css` 3 files +183/-28 — DS Field/TextInput/Button·모노그램 카드·Modal 포커스 트랩·`forced-colors`·`prefers-contrast` WCAG 1.4.11, working tree CLEAN·`npm test` 13/5·build 111·audit 0건)·TSR 27차(22:40 frontend COD 19차 `cc34f23` `pilotChecklist.js/.test.js`·`GuardianInviteModal.test.jsx` 3 files +396 — P1–P8 services.js 매핑·Vitest fetch-mock JWT·HTTP·경로·GuardianInviteModal 회귀 4건, working tree CLEAN·`npm test` 13/5 → **32/7**(+19 tests/+2 files)·build 111·audit 0건). 벤치마크 BNK-6 **신규 입력 없음**.

| # | 반영 | 산출물 |
|---|------|--------|
| 1 | TSR 26차 **backend R-04 7역할 권한 분리 PARTIAL 진전** — COD 18차 `c3f3146` `PilotChecklistApiAccessTest` 697 lines 29 @Test 일괄 커밋, `@WebMvcTest` 65건(36 RBAC + 29 Pilot), working tree CLEAN, `@Test` 120→154→**183**(+29 vs 24차), Maven 79/79 PASS — 라이브 7역할 JWT E2E만 잔여 | `ROADMAP.md` v1 7역할 권한 분리 단위 PARTIAL 진전 주석·QA-B02 `c3f3146` 갱신·R-04 65건 |
| 2 | TSR 27차 **frontend v1.1 Must API JWT 라우팅 fetch-mock 자동화·J01/J02 회귀 자동화 진전** — COD 19차 `cc34f23` `src/api/pilotChecklist.js`(211, P1–P8 services.js 경로 + HTTP 메서드 + 페이로드 + 권한 매핑 계약 사전)·`pilotChecklist.test.js`(104, Vitest fetch-mock JWT·HTTP·경로 자동 검증 +15 tests)·`GuardianInviteModal.test.jsx`(81, invite/expire/resend/scope 4건 회귀) — `npm test` 32/7 PASS·build 111·audit 0건 | `ROADMAP.md` v1.1 P1–P8 프론트 재현 PARTIAL·보호자 초대 E2E PARTIAL·B04/B07 5커밋 무재발·USER_STORIES `§13` 단위 자동화 주석·FE-9 신설 |
| 3 | TSR 26차 **UXD 12차 `404a30e` 흡수 (결정 52 적용)** — `LoginPage.jsx`·`Modal.jsx`·`components.css` DS Field/TextInput/Button 적용·모노그램 카드·Modal 포커스 트랩·`forced-colors`·`prefers-contrast` WCAG 1.4.11 비텍스트 대비 충족·DESIGN_SYSTEM §9 접근성 진전 | `ROADMAP.md` v1.2 흡수 6묶음·`PLAN_NOTES.md` 19차 sync·USER_STORIES FE-7 26차 갱신 |
| 4 | USER_STORIES §13 파일럿 체크리스트 **단위 자동화 PARTIAL 진전 주석 추가** — backend `PilotChecklistApiAccessTest` 29 @Test + frontend `pilotChecklist.js/.test.js` fetch-mock 양 스트림 단위 보장; 라이브 E2E는 B01 merged 후 | `USER_STORIES.md` §13 |
| 5 | USER_STORIES **§16 FE-7 27차 + FE-9 신설** — pilotChecklist fetch-mock 자동화 정착(P1–P8 단위 회귀); §17 **BE-6 5커밋 무재발 갱신** — 22차→24차→26차 Fixed 후 5커밋 패턴 완전 종결 | `USER_STORIES.md` |
| 6 | **#36 양 스트림 BE-6·FE-6 패턴 완전 종결 확인** — backend 5커밋 무재발(4274459→aa71412→c3f3146)·frontend 4커밋 무재발(a84473f→ed1bf22→404a30e→cc34f23). 운영 게이트(pre-commit hook 등) 권고 공식 보류 확정 | `PLAN_NOTES.md` 19차 sync |
| 7 | **J01 백엔드 API 미구현 잔여 — 추가 질문 #33·#35 명세 결정 대기**: API_SPEC §4 `/guardians/invitations` POST·`/guardian/invitations/{token}/accept` POST·`GET /guardian/invitations` 명세 + DBA `guardian_invitations` 테이블 V41(필드·만료·재발송 정책) — 채널 1종(#33)·만료 정책(#35) 결정 후 작성 | `PLAN_NOTES.md` 19차 sync·USER_STORIES US-J01 잔여 명세 |
| 8 | 19차 동기화 기록 | `decisions.md` |

**핵심 판단**: ① **backend R-04 7역할 권한 분리 PARTIAL 진전** — `PilotChecklistApiAccessTest` 29 @Test로 P1–P8 × 7역할 `@PreAuthorize` 자동화 정식 충족, `@WebMvcTest` 65건(36 RBAC + 29 Pilot). 라이브 7역할 JWT 로그인 E2E만 v1 ready 잔여. ② **frontend v1.1 Must API JWT 라우팅 fetch-mock 자동화** — `pilotChecklist.js` 계약 사전이 services.js와 USER_STORIES §13을 연결, fetch-mock으로 JWT·HTTP·경로·페이로드 단위 자동화. 라이브 수동 시나리오는 backend v1 test merge 후. ③ **양 스트림 5/4커밋 무재발** — BE-6·FE-6 dirty-tree 패턴 완전 종결, 운영 게이트 권고 공식 보류. ④ **잔여 BLOCK = merge 게이트(B01·B03·B05·SEC-007) 단일** — dirty-tree·B02·B07·SEC-008 사유 모두 소멸. ⑤ **결정 52 흡수 6묶음** 유지: v1.2 P0·US-D03·UXD 10·11·12차·COD 17·18·19차 모두 v1.1 develop→test merge 동반. ⑥ **J01 백엔드 API 미구현 — 명세 작성은 #33·#35 결정 후 보류** (추측 명세 금지·rules.md §1).

**coder 다음 액션**: ① v1 7역할 **라이브 JWT 로그인 E2E**(Spring Security filter chain·실 토큰 발급/검증 통합 시나리오 1건씩) + SEC-007 develop→test merge 후 P0 패치 재검증 → `merge_status: ready` → B01·SEC-007 동반 해소. ② v1.1 J01 백엔드 API — PLN 명세(#33·#35 결정 후) → DBA `guardian_invitations` V41 → COD 백엔드 구현 → COD 프론트 실 API 연동 → B03 ready → merge(흡수 6묶음 자동 동반·결정 52, B05 동반 해소). ③ v1.2 본격 사이클(2단 SideNav 모듈 가중 커버리지 ≥60%·E2E·등급이력 UI)은 v1.1 merged 후.

**미해결 추적**: #27·#31·#32·#33(보호자 알림 채널 1종 — J01 백엔드 API 명세 선행)·#35(`guardian_invitations` 스키마·만료/재발송 정책)·#36(BE-6/FE-6 양 스트림 패턴 완전 종결 — 권고 공식 보류).

---

## 2026-06-06 — planner(PLN): 자동 기획 동기화 18차 (TSR 24·25차 + B07 recurrence #2 Fixed + SEC-008 동일 사이클 Fixed + R-02 Must API 라우팅 [x] 승격 + UXD 11차 dark mode)

`build --role planner` 자동 동기화. **핵심 입력**: TSR 24차(21:13 backend COD 16차 `aa71412` Must API 라우팅·RBAC·ProductionSecretValidator 테스트 +34 → `@Test` 154, R-02 Must API 라우팅 PARTIAL→[x] 승격, working tree CLEAN; frontend UXD 11차 `2d742b3` dark mode 7 files 정상 커밋·`overrides.esbuild ^0.25.0`; **신규 SEC-008** npm audit dev chain 5 vuln/1 critical Open)·25차(21:32 frontend COD 17차 `a84473f` US-M02 8 files 일괄 커밋 + `ed1bf22` vite 6.4.3·vitest 4.1.8 메이저 업그레이드 — B07 recurrence #2 Fixed·SEC-008 동일 사이클 Fixed·`npm audit` 0 vuln·`npm test` 13/5·build 111 modules PASS). 벤치마크 BNK-6 **신규 입력 없음**.

| # | 반영 | 산출물 |
|---|------|--------|
| 1 | TSR 25차 **QA-B07 recurrence #2 Planned→Fixed** — COD 17차 `a84473f feat(v1.2-p0): 대시보드 실데이터 위젯·Must 페이지 API 보강 (US-M02)`(8 files +636/-170) 일괄 커밋, working tree CLEAN, HEAD `npm test` 13/5·build 111 modules PASS, 이관 규율 5·6·7 PASS — TSR 25차 독립 검증 | `QA_FEEDBACK.md` Fixed 갱신·`ROADMAP.md` v1.1 B07 `[x]` 복원·QA→태스크 매핑 |
| 2 | TSR 24차 **SEC-20260606-008 신규 Open → 25차 Fixed 동일 사이클** — npm audit dev chain 5 vuln(esbuild GHSA-67mh-4wv8-2f99·vite path traversal·vitest UI GHSA-5xrq-8626, 1 critical) → COD 17차 `ed1bf22` vite `^6.4.3`·vitest `^4.1.8`·`overrides.esbuild ^0.25.0`로 `npm audit --audit-level=high` **0 vulnerabilities** | `QA_FEEDBACK.md` Fixed 신설·`ROADMAP.md` v1.1 SEC-008 완료 기준 신설·USER_STORIES §16 FE-8 신설 |
| 3 | TSR 24차 **R-02 Must API 라우팅 PARTIAL→[x] 승격** — COD 16차 `aa71412 test(v1): Must API 엔드포인트 라우팅 단위 테스트 보강` `MustApiEndpointRoutingTest` §1–§9 26+ @Test, `RoleBasedControllerAccessTest` 확장, `ProductionSecretValidatorTest` 추가, `@Test` 120→154, working tree CLEAN | `ROADMAP.md` v1 R-02 [x] 승격 |
| 4 | **UXD 11차 `2d742b3` 흡수** — dark mode 7 files (`useDarkMode.js` 훅·`Topbar` 토글·`AppShell` body class·DESIGN_SYSTEM `[data-theme="dark"]` 토큰) 정상 커밋, FE-7 충족 | `ROADMAP.md` v1.2 |
| 5 | **US-M02 Fixed 진전** — `dashboardWidgets.js` 위젯 집계 로직(오늘 출석/결석·미납·미매칭 NHIS) + `dashboardWidgets.test.js` 3 PASS, develop HEAD 일괄 커밋 — 인수 조건 첫 2항 [x] 부분 충족(StatCard 데모 제거·API 연동·위젯 3블록 진전) | `USER_STORIES.md` §12d Fixed 진전 메모 |
| 6 | USER_STORIES §17 **BE-6 4커밋 무재발 갱신** — #1·#2·#3 모두 해소 후 22차 Fixed → 24차 COD 16차 `aa71412`까지 4커밋 working tree CLEAN, **패턴 종결 신호**, 운영 게이트 권고 보류; §16 **FE-6 #2 Fixed 갱신**·**신설 FE-8**(dev audit 정책) | `USER_STORIES.md` |
| 7 | #36 에스컬레이션 갱신 — backend BE-6 패턴 종결(4커밋 무재발)·frontend FE-6 #2 Fixed → 양 스트림 dirty-tree 패턴 모두 종결 신호 | `PLAN_NOTES.md` 18차 sync 섹션 |
| 8 | 18차 동기화 기록 | `decisions.md` |

**핵심 판단**: ① **B07 recurrence #2 정식 Fixed** — COD 17차 `a84473f` US-M02 8 files 일괄 커밋·working tree CLEAN, HEAD build 111·`npm test` 13/5 PASS·이관 규율 5·6·7 PASS, FE-6 #2 정식 해소. ② **SEC-008 동일 사이클 처리** — 24차 신규 Open(npm audit 5 vuln/1 critical) → 25차 COD 17차 `ed1bf22`(vite 6·vitest 4 메이저 업그레이드 + esbuild override) → audit 0건. dev chain 전용으로 prod 번들 무관, 빠른 동일 사이클 해소. ③ **R-02 Must API 라우팅 [x] 승격** — COD 16차 `aa71412` `MustApiEndpointRoutingTest` §1–§9 26+ @Test로 v1 Must API 엔드포인트 매핑·인증 라우팅 정식 검증. ④ **양 스트림 dirty-tree 패턴 모두 종결** — backend BE-6 #3 Fixed 후 4커밋 무재발(94f0fb9→4274459→aa71412)·frontend FE-6 #2 Fixed → #36 운영 게이트(pre-commit hook 등) 권고 보류. ⑤ **잔여 Planned BLOCK = merge 게이트 단일**(B01·B03·B05·SEC-007) — 코드/테스트 사유 BLOCK 0건. ⑥ **결정 52 유지**: v1.2 P0(`a72e249`)·UXD 10차(`5656e19`)·UXD 11차(`2d742b3`)·US-M02(`a84473f`)·SEC-008(`ed1bf22`) 모두 v1.1 develop→test merge에 동반 흡수.

**coder 다음 액션**: ① v1 완료 기준(E2E·SEC-007 develop→test merge 후 P0 패치 재검증) → `merge_status: ready` → develop→test merge(B01·SEC-007 동반 해소). ② v1.1 E2E·J01(보호자 초대 백엔드 API — API_SPEC §5 PLN 명세 후 DBA `guardian_invitations` 테이블·COD 구현) → B03 ready → merge(v1.2 P0·UXD 10·11차·US-M02·SEC-008 자동 동반·결정 52, B05 동반 해소). v1.2 본격 사이클(2단 SideNav 모듈 가중 커버리지 ≥60%·E2E·등급이력 UI)은 v1.1 merged 후.

**미해결 추적**: #27·#31·#32·#33·#35·#36(BE-6/FE-6 양 스트림 패턴 종결 신호 — 운영 게이트 권고 보류).

---

## 2026-06-06 — planner(PLN): 자동 기획 동기화 17차 (TSR 22·23차 + B02 recurrence #3 Fixed + B07 recurrence #2 Planned + UXD 10차 + US-M02 WIP)

`build --role planner` 자동 동기화. **핵심 입력**: TSR 22차(20:11 backend B02 recurrence #3 Fixed via `4274459`, COD 15차 — TSR 독립 검증, `@Test` 120·Maven 79/79 PASS)·23차(20:17 frontend B07 recurrence #2 — `5656e19`(UXD 10차) 위 v1.2 P0 US-M02 대시보드 실데이터 위젯 8 files WIP 미커밋·WT build 112·`npm test` 13/5 PASS·HEAD Fixed 규율 5 PRESENT 유효). 벤치마크 BNK-6 **신규 입력 없음**.

| # | 반영 | 산출물 |
|---|------|--------|
| 1 | TSR 22차 **QA-B02 recurrence #3 Planned→Fixed** — COD 15차 `4274459` `NhisImportServiceTest`·`RoleBasedControllerAccessTest`·`BillingControllerRoutingTest` 3 files 일괄 커밋, working tree CLEAN, `@Test` 120·Maven 79/79 PASS, BE-6 #3 정식 해소 | `QA_FEEDBACK.md`·`ROADMAP.md` v1 QA-B02 `[x]` 복원 |
| 2 | TSR 23차 **QA-B07 recurrence #2 Open→Planned** — `5656e19`(UXD 10차) 위 v1.2 P0 US-M02 대시보드 위젯 실데이터 8 files WIP 미커밋(FE-6 위반·FE-7 충족·HEAD Fixed 규율 5 유효, WT build 112·`npm test` 13/5 PASS·신규 `dashboardWidgets.test.js` 3 PASS·회귀 없음) | `QA_FEEDBACK.md`·`ROADMAP.md` v1.1 B07 `[x]` 철회·recurrence #2 주석 |
| 3 | **UXD 10차 `5656e19` 흡수** — 이용자 본인 계정 발급 필드(`client_user`, 결정 16)·`CopayTypeSelect`(결정 27 4구분)·브랜드색 통일(DESIGN_SYSTEM §1) 정상 커밋. 결정 52에 따라 v1.1 merge 동반 | `ROADMAP.md` v1.2 |
| 4 | **US-M02 진전(대시보드 실데이터 위젯)** — `dashboardWidgets.js` 위젯 집계 로직(오늘 출석/결석·미납·미매칭 NHIS) WT 완성·`dashboardWidgets.test.js` 3 PASS, develop HEAD 미커밋(B07 recurrence #2 범위) | `USER_STORIES.md` §12d·`ROADMAP.md` v1.2 |
| 5 | USER_STORIES §17 **BE-6 recurrence #3 Fixed** 갱신, §16 **FE-6** 23차 recurrence #2 사례 추가 | `USER_STORIES.md` |
| 6 | #36 에스컬레이션 갱신 — backend BE-6 패턴 해소(3회→Fixed)·frontend FE-6 패턴 #2 신규(반복) | `PLAN_NOTES.md` |
| 7 | 17차 동기화 기록 | `decisions.md` |

**핵심 판단**: ① backend B02 **recurrence #3 정식 Fixed** — COD 15차 `4274459`로 20차 미커밋이던 NHIS·Billing 라우팅·RBAC 테스트 3 files 일괄 커밋. develop `@Test` 98→**120**, working tree CLEAN, Maven 79/79 PASS·package SUCCESS 재현. BE-6 #3 해소·이관 규율 6 충족, 잔여 backend BLOCK = **merge 게이트 단일**(B01·SEC-007). ② frontend B07 **recurrence #2** — `5656e19`(UXD 10차) 정상 커밋 후 그 위에 v1.2 P0 **US-M02 대시보드 위젯 실데이터** WIP 8 files 미커밋. WT 품질 게이트는 충족(FE-7) — 신규 `dashboardWidgets.test.js` 3 PASS·build 112 modules·`npm test` 13/5 PASS, **기능 결함 아닌 미커밋(프로세스) 위반**. v1.2 P0 흡수 범위(결정 52) 내 작업 → commit 후 v1.1 merge에 자동 동반. ③ **결정 52 유지**: v1.2 P0 + UXD 10차 + US-M02 위젯 모두 v1.1 develop→test merge에 동반 흡수, 별도 v1.2 merge 라운드 불추가. v1.2 정식 완료 기준(2단 SideNav 커버리지 ≥60%·E2E)은 v1.1 merged 후 v1.2 사이클에서.

**coder 다음 액션**: ① **B07 recurrence #2 commit/revert**(FE-6·FE-7, US-M02 대시보드 위젯 8 files — `npm test`·`npm run build` 이미 PASS) → frontend working tree clean. ② v1 완료 기준(E2E·Must API·SEC-007) → `merge_status: ready` → develop→test merge(B01·SEC-007 동반 해소). ③ v1.1 E2E·J01(보호자 초대 백엔드 API — API_SPEC §5 PLN 명세 후) → B03 ready → merge(v1.2 P0 `a72e249`·UXD 10차 `5656e19`·US-M02 위젯 자동 동반·결정 52, B05 동반 해소). v1.2 본격 사이클은 v1.1 merged 후.

**미해결 추적**: #27·#31·#32·#33·#35·#36(BE-6 패턴 #3 해소·FE-6 패턴 #2 신규 — frontend 반복 패턴, 운영 게이트 권고 유지).

---

## 2026-06-06 — planner(PLN): 자동 기획 동기화 16차 (TSR 20·21차 + B02 recurrence #3 + B07 Fixed + v1.2 P0 흡수 결정 52)

`build --role planner` 자동 동기화. **핵심 입력**: TSR 20차(19:12 backend B02 recurrence #3 — 신규 테스트 3 files 미커밋)·21차(19:22 frontend B07 recurrence Fixed — `a72e249` v1.2 P0 42 files + `3fc549a` US-D03 일괄 커밋, working tree CLEAN, HEAD build 110·`npm test` 10/4 PASS). 벤치마크 BNK-6 **신규 입력 없음**.

| # | 반영 | 산출물 |
|---|------|--------|
| 1 | TSR 20차 **QA-B02 recurrence #3** Open→Planned — `NhisImportServiceTest`·`RoleBasedControllerAccessTest`·`BillingControllerRoutingTest` 3 files 미커밋(BE-6 위반 3회째) | `QA_FEEDBACK.md`·`ROADMAP.md` v1 QA-B02 `[x]` 철회 |
| 2 | TSR 21차 **QA-B07 recurrence Fixed 확정** — `a72e249`(v1.2 P0 42 files +3863/-311) + `3fc549a`(US-D03) 일괄 커밋, working tree CLEAN, 규율 5·6·7 PASS, FE-7 정식 충족 | `QA_FEEDBACK.md`·`ROADMAP.md` v1.1 B07 Fixed 갱신 |
| 3 | **결정 52** — v1.2 P0 산출물은 **v1.1 develop→test merge에 동반 흡수**(별도 분리 안 함), v1.1 merge ready 게이트는 v1.1 완료 기준만, v1.2 정식 완료 기준은 v1.1 merged 후 사이클 | `PLAN_NOTES.md`·`ROADMAP.md` v1.2 status `planned→in_progress` |
| 4 | USER_STORIES §17 **BE-6** recurrence #3 갱신(NHIS·Billing 라우팅 테스트 추가), §16 **FE-7** 21차 정식 충족 주석 | `USER_STORIES.md` |
| 5 | #36 에스컬레이션 갱신 — backend B02 recurrence **3회 연속 반복** 패턴, frontend 해소·v1.2 흡수 | `PLAN_NOTES.md` |
| 6 | 16차 동기화 기록 | `decisions.md` |

**핵심 판단**: ① backend B02 **recurrence #3** — BE-6(완료 단위 커밋·`mvn -q test` PASS) 위반이 #1(15차)·#2 Fixed → **#3 재발**. 패턴 반복 → coder 워크플로우 운영 게이트 검토(#36). ② frontend B07 **정식 Fixed** — 19~20차 dirty 42 files → `a72e249` 일괄 커밋·working tree CLEAN·HEAD build 110·`npm test` 10/4 PASS, 이관 규율 5·6·7 PASS·FE-7 충족. ③ **결정 52**: v1.2 P0 산출물이 v1.1 라우팅·세션 인프라(`routeAccess.js`·`SessionTimeoutProvider`)와 결합 → 분리 비효율, v1.1 merge에 동반 흡수. v1.2 정식 완료 기준(2단 SideNav 커버리지 ≥60%·E2E)은 v1.1 merged 후 v1.2 사이클에서.

**coder 다음 액션**: ① **B02 recurrence #3 commit/revert**(BE-6, `mvn -q test` PASS 후) → backend working tree clean. ② v1 완료 기준(E2E·Must API·SEC-007) → `merge_status: ready` → develop→test merge(B01·SEC-007 동반 해소). ③ v1.1 E2E·J01 → B03 ready → merge(v1.2 P0 `a72e249` 자동 동반·결정 52, B05 동반 해소). v1.2 본격 사이클은 v1.1 merged 후.

**미해결 추적**: #27·#31·#32·#33·#35·#36(backend B02 recurrence #3 — 3회 반복).

---

## 2026-06-06 — planner(PLN): 자동 기획 동기화 15차 (TSR 17·18·19차 + B02 Fixed + B07 FE-7 회복)

`build --role planner` 자동 동기화. **핵심 입력**: TSR 17차(18:34 backend B02 Fixed)·18차(18:42 backend 불변)·19차(18:45 frontend B07 FE-7 회복). 벤치마크 BNK-6 **신규 입력 없음**.

| # | 반영 | 산출물 |
|---|------|--------|
| 1 | TSR 17차 **QA-B02 recurrence Fixed** — develop `b5d70a8` clean, GuardianAccess RBAC 3 tests TSR 검증 | `QA_FEEDBACK.md` Fixed·`ROADMAP.md` |
| 2 | backend 잔여 BLOCK = **merge 게이트 단일**(B01·SEC-007) — dirty-tree·B02 사유 소멸 | `ROADMAP.md`·`PLAN_NOTES.md` |
| 3 | TSR 19차 **B07 Planned 갱신** — 35 files, WT build/test PASS(FE-7), dirty-tree 지속 | `ROADMAP.md` v1.2·`USER_STORIES` FE-7 |
| 4 | USER_STORIES §17 **BE-6 Fixed** 확정 | `USER_STORIES.md` |
| 5 | #36 에스컬레이션 갱신 — backend 해소, frontend B07 잔존 | `PLAN_NOTES.md` |

**핵심 판단**: backend **CLEAN** — B02 recurrence 해소, merge 게이트만 BLOCK. frontend B07 — **35 files dirty-tree**, FE-7 **충족**(commit 준비). 잔여 Planned 5건(B01·B03·B05·SEC-007·B07).

**coder 다음 액션**: ① B07 commit/revert(FE-6·FE-7 충족), ② v1 E2E→ready→merge, ③ v1.1 E2E·J01.

**미해결 추적**: #27·#31·#32·#33·#35·#36(B07).

---

## 2026-06-06 — planner(PLN): 자동 기획 동기화 13차 (TSR 15·16차 + B02 recurrence + B07 WT 회귀)

`build --role planner` 자동 동기화. **핵심 입력**: TSR 15차(18:04 backend B02 recurrence)·16차(18:07 frontend B07 WT build/test FAIL). 벤치마크 BNK-6 **신규 입력 없음**.

| # | 반영 | 산출물 |
|---|------|--------|
| 1 | TSR 15차 **QA-B02 recurrence** Open→Planned — `RoleBasedControllerAccessTest` guardian RBAC +74 lines dirty | `QA_FEEDBACK.md`·`ROADMAP.md` |
| 2 | v1 완료 기준 QA-B02 `[x]` **철회** — HEAD @ `fac3d07` Fixed **유효**, recurrence 별도 | `ROADMAP.md` |
| 3 | **결정 51** — WIP 커밋 전 품질 게이트(FE-7 frontend build/test, BE-6 backend clean) | `PLAN_NOTES.md`·`USER_STORIES.md` |
| 4 | TSR 16차 **B07 Planned 강화** — 29 files·WT duplicate `ROUTE_ACCESS` build/test FAIL | `ROADMAP.md` v1.2·`USER_STORIES` FE-7 |
| 5 | USER_STORIES §17 **BE-6**(backend dirty-tree recurrence) | `USER_STORIES.md` |
| 6 | #36 에스컬레이션 갱신 — 양 스트림 dirty-tree 병행 | `PLAN_NOTES.md` |

**핵심 판단**: 12차 이후 **양 스트림 동시 dirty-tree recurrence** — backend RBAC WIP(B02)·frontend v1.2 WIP(B07, 품질 회귀). HEAD Fixed **양쪽 유효**(규율 5). merge 게이트(B01·B03·B05·SEC-007) + dirty-tree가 병행 BLOCK.

**coder 다음 액션**: ① B02 commit/revert(BE-6), ② B07 duplicate fix + FE-7 PASS → commit/revert, ③ v1 E2E→ready→merge, ④ v1.1 E2E·J01.

**미해결 추적**: #27·#31·#32·#33·#35·#36.

---

## 2026-06-07 — db_architect(DBA): V40 round 34 전수 재대조 (backend `fac3d07` guardian billing + NHIS guidance 반영)

backend `fac3d07`(guardian billing API·NHIS import guidance·7-role RBAC tests) 직후 DBA가 변경 도메인을 V1–V40 스키마와 1:1 재대조. **신규 누락 테이블/인덱스/제약 없음** — V41 미생성(rules.md §2/§8, round 33 패턴 유지).

| # | 점검 대상 | 결과 |
|---|----------|------|
| 1 | `GET /guardian/clients/{clientId}/billing` — `BillingService.listClientBillingHistoryForPortal` | ✅ V25 `idx_billing_claim_items_org_client_created`(직원 이용자 청구 탭과 **동일** 인덱스 재사용)·V25 `idx_guardian_clients_org_guardian_client`(보호자 연결 검증)·V33 partial(active 분기)·V8 `uq_billing_claims_org_id`(Tenant 앵커) 전부 커버 |
| 2 | `GET /billing/imports/nhis/guidance` — `BillingController.nhisImportGuidance` | ✅ 정적 응답(롱텀 2026 Chrome/Edge 안내) — **DB 미사용** |
| 3 | RBAC/단위 테스트(`RoleBasedControllerAccessTest`·`GuardianPortalServiceTest`·`AuthServiceTest`·`NhisImportGuidanceTest`) | ✅ 스키마 영향 없음 |
| 4 | 보호자 초대 테이블(`guardian_invitations`, US-J01·v1.1) | ⏸ **API_SPEC 계약 확정 보류** — 채널(이메일/SMS)·만료·1회용 정책 미정. PLAN_NOTES `### DB 설계 질문` #35에 가설 스키마 + 보류 사유 기록 |

| 산출물 | 갱신 |
|--------|------|
| `docs/technical/ERD.md` §8 | `GET /guardian/clients/{clientId}/billing`·`GET /billing/imports/nhis/guidance` 매핑 2행 추가, 메타 timestamp |
| `docs/ops/DATA_RETENTION_POLICY.md` §8 | 보호자 포털 청구 탭 인덱스 매핑(V25·V8 Tenant 앵커) 1행 추가, 메타 timestamp |
| `docs/planning/PLAN_NOTES.md` `### DB 설계 질문` | #34(round 34 전수 재대조 — 신규 누락 0건)·#35(`guardian_invitations` API 계약 보류) 신설, 메타 timestamp |
| `memory/decisions.md` | 본 항목 최상단 추가 |

**핵심 판단**: backend `fac3d07`의 신규 쿼리(`listClientBillingHistoryForPortal`·`getClientBillingHistory`)는 모두 **이용자 청구 탭과 동일 인덱스**를 재사용 — 보호자/`client_user` 분기는 `GuardianClientRepository.existsByOrganizationIdAndGuardianUserIdAndClientId`(V25) 또는 `clients.user_id` 1:1(V23)로 격리되어 cross-tenant 누수 없음. NHIS guidance는 정적 응답으로 DB 무관.

**coder 개선 후보(선택)**: `BillingClaimRepository.findByIdInAndOrganizationId(Set<UUID>, UUID)` 메서드 추가 시 `findAllById + filter`를 단일 쿼리로 단순화 가능 — V8 `uq_billing_claims_org_id` UK 활용. 성능 차이 미미하므로 **DB 변경 불필요**, repository 시그니처만 변경.

**US-J01 보호자 초대(v1.1) 설계 게이트**: PLN가 API_SPEC §5에 `POST /guardians/invitations` 계약(채널·만료·1회용·재발급)을 명세하면 DBA가 즉시 `guardian_invitations` 마이그레이션(V41 후보) 작성. 가설 스키마는 PLAN_NOTES #35에 박음.

**미해결 추적**: #27·#31·#32·#33(보호자 초대 채널 — US-J01과 동일 게이트)·#35(duration_band).

---

## 2026-06-06 — planner(PLN): 자동 기획 동기화 12차 (TSR 13·14차 + B07 recurrence)

`build --role planner` 자동 동기화. **핵심 입력**: TSR 13차(17:30 backend `fac3d07`)·14차(17:35 frontend B07 recurrence). 벤치마크 BNK-6 **신규 입력 없음**.

| # | 반영 | 산출물 |
|---|------|--------|
| 1 | TSR 14차 **QA-B07 recurrence** Open→Planned — v1.2 P0 19 files dirty-tree, HEAD @ `998ac87` Fixed **유효** | `QA_FEEDBACK.md`·`ROADMAP.md` |
| 2 | **결정 50** — v1.2 선행 dirty-tree 금지(이관 규율 7), USER_STORIES §16 **FE-6** | `PLAN_NOTES.md`·`USER_STORIES.md` |
| 3 | backend `fac3d07` 부분 진전 — `RoleBasedControllerAccessTest`·`NhisImportGuidance`·guardian billing | `ROADMAP.md` v1 완료 기준 PARTIAL 주석 |
| 4 | v1.2 WIP 관측(14차) — P0 다수 working tree, commit/revert 태스크 | `ROADMAP.md` v1.2 |
| 5 | #36 B07 recurrence 갱신 — merge 게이트 + dirty-tree 병행 | `PLAN_NOTES.md` |

**핵심 판단**: 11차 dirty-tree 해소 후 **v1.2 선행 착수**로 B07 **recurrence**. v1.1 merge 게이트(B03·B05) 우선 — v1.2 WIP는 commit or revert. backend RBAC/guidance는 v1 **기능 진전**이나 E2E·merge 잔여.

**coder 다음 액션**: ① B07 recurrence commit/revert → clean tree, ② v1 E2E→ready→merge(B01·SEC-007), ③ v1.1 E2E·J01→B03 ready.

**미해결 추적**: #27·#31·#32·#33·#35·#36.

---

## 2026-06-06 — planner(PLN): 자동 기획 동기화 11차 (TSR 11·12차 + BNK-6 v1.2 + SEC-007)

`build --role planner` 자동 동기화. **핵심 입력**: TSR 11차(16:40 backend)·12차(16:55 frontend), SEC 3차(SEC-007), BNK 6차 완료(`BENCHMARK_REPORT §9`·`COMPETITOR_MATRIX §8`).

| # | 반영 | 산출물 |
|---|------|--------|
| 1 | COD 11차 Fixed 확정 반영 — B06·B02·B07·B04·H04·M01·SEC-005, develop 양 스트림 clean | `QA_FEEDBACK.md` Fixed·`ROADMAP.md` QA 진단 |
| 2 | SEC-007(Open) → Planned — B01 merge 동반 해소 태스크 | `QA_FEEDBACK.md`·`ROADMAP.md` v1 SEC-007 완료 기준 |
| 3 | v1.2 BNK-6 범위 확정 — P0 5건·P1 3건·P2 2건, BNK-6 완료 `[x]` | `ROADMAP.md` v1.2 |
| 4 | §1-5-2 화면 밀도 KPI·G13/G14·§6-3 | `REQUIREMENTS.md` |
| 5 | Epic K·L·M·UX (8 스토리), §15 갭 Epic 명칭 정리 | `USER_STORIES.md` |
| 6 | **결정 49 확정** — 모듈 커버 ≥60% + 2단 SideNav = v1.2 완료 KPI | `PLAN_NOTES.md`·`ROADMAP.md` |
| 7 | #36 에스컬레이션 **부분 해소** — 커밋 완료, merge·E2E 잔여 | `PLAN_NOTES.md` #36 |

**핵심 판단**: 10차까지 dirty-tree·false Fixed가 유일 블로커였으나 **COD 11차로 해소**. 잔여 BLOCK = **merge 게이트(B01·B03·B05) + SEC-007(B01 동반) + v1/v1.1 E2E·J01 완료 기준 미충족**. BNK-6로 v1.2는 **기존 DB 활용 low-cost high-density** P0 5건으로 ≥60% KPI 달성 경로 확정.

**coder 다음 액션**: v1 완료 기준(E2E·P1–P8·SEC-007) → ready → merge → v1.1 E2E·J01 → B03 ready.

**미해결 추적**: #27·#31·#32·#33·#35.

---

## 2026-06-06 — planner(PLN): 자동 기획 동기화 10차 (상태 불변 재확인 + coder 미조치 에스컬레이션 강화)

`build --role planner` 자동 동기화. 9차(16:10) 이후 **신규 입력 0건** — QA_FEEDBACK·TEST_REPORT 최종 갱신은 TSR 9차(15:45) 그대로, 벤치마크(BNK 6차)는 여전히 **착수 대기**. submodule HEAD·working tree 직접 점검 결과 **9차와 완전 동일**:
- backend `7d9d2eb` dirty (10 mod + 2 untracked — `ClientService`·`CreateClientRequest`·`ClientResponse`·`ClientEntity`·`GuardianClientRepository`·`PrimaryGuardianLinkRequest`·`V39__client_guardian_link_status.sql` 등 client↔guardian 미커밋, B06 유지)
- frontend `f1c89d9` dirty (22 mod + 20 untracked — `src/api/`·`*.test.jsx`·신규 페이지·`AuthContext` 등, B07 유지)

신규 기획 변경·태스크·결정 **없음**. QA Open 0건 → Planned 이동 없음. 이번 동기화는 **현황 재확인·메타 갱신·에스컬레이션 강화**만 수행.

| # | 반영 | 산출물 |
|---|------|--------|
| 1 | `## QA 피드백 반영` 10차 노트(submodule HEAD 직접 점검 — 9차 대비 불변), 메타·변경 이력 timestamp | `docs/planning/ROADMAP.md` |
| 2 | `### [PLN] 자동 기획 동기화 — 10차` 섹션, **추가 질문 #36 에스컬레이션 강화**(미조치 지속 회차 누적·권고 명시), 메타 timestamp | `docs/planning/PLAN_NOTES.md` |
| 3 | 10차 동기화 기록 | `memory/decisions.md` 최상단 |

**핵심 판단(9차와 동일·강화)**: 잔여 BLOCK 9건은 **전부 이관 규율 미준수**(완료 단위 develop 커밋·`merge_status` 미승격)가 유일 블로커 — 기능 갭 아님. 산출물은 양 스트림 모두 develop **working tree에 사실상 완성**(backend Maven 79/79·frontend vitest 6 PASS)됐으나 develop HEAD 미커밋. 결정 41·44·45(이관 규율 1·5·6)로 이미 커버 — **신규 결정 불필요**. 5·6·7차 태스크화 → TSR 8·9차 → 10차까지 **coder 0건 조치 지속**, 정체가 길어짐 → #36 에스컬레이션 강화(planner/사용자 운영 게이트 결정 필요).

**미변경**: REQUIREMENTS·USER_STORIES·API_SPEC·FLOWCHART(7·8차까지 반영), DB 제약(V1–V39), 청구 2단계·QR B·platform_admin·MVP 제외. **미해결 추적**: #27·#31·#32·#33·#35·#36.

---

## 2026-06-06 — benchmark_researcher(BNK): 6차 화면·메뉴 전수 매핑 (BNK-6 — v1.2 화면 밀도 백로그)

사용자 피드백 「프론트 기능이 너무 적다」(결정 47) 대응. 케어포 `daycare/func.php`·주야간 매뉴얼 PDF(번호식 1~12 전수)·이지케어 기능/앱·엔젤 앱/system_feature 재조사 + **ogada `src/frontend` 실측**(App.jsx 24 route·SideNav.jsx). 산출물: `BENCHMARK_REPORT §9`(완료)·`COMPETITOR_MATRIX §8`(전수 매핑·KPI·역할별·UX·백로그) 신규 작성, 5차 본문 유지.

| # | 결정·권고 | 근거 | planner/coder 영향 |
|---|----------|------|-------------------|
| 1 | **모듈 커버리지 ~25–30% 확정** — 케어포 12모듈 중 완전 ✅ 2(수급자·기초설정)+청구7-1·NHIS / 부분 △ 5 / 갭 ❌ 5 | [func.php](https://www.carefor.co.kr/daycare/func.php)·매뉴얼 PDF 전수 vs App.jsx | 6차 가설(~25%) 확정. v1.2 목표 **≥60%**(결정 49) |
| 2 | **화면수 KPI** — ogada **24 route**(21 page, SideNav 1단 flat) vs 케어포 **80+**(2~3단)·이지케어 ~40·엔젤 ~40 | App.jsx·SideNav.jsx 실측 / 경쟁사 메뉴 | KPI 표 §8-2 |
| 3 | **화면 밀도 갭의 본질 = 「기존 데이터의 화면 부재」** — P0 5건은 신규 테이블 ≤1개 | guardian_clients·billing·clients·attendance 기존 자산 | **low-cost high-density** — v1.2 P0 |
| 4 | **v1.2 P0 5건** — ①보호자 관리 화면(1-3) ②본인부담 입금·미납(7-2/7-3 G13) ③등급변동 이력(1-9 G14) ④대시보드 위젯 실데이터 ⑤**2단 SideNav 그룹화** | 케어포 메뉴·대시보드 3블록 | ROADMAP v1.2 `planned`·USER_STORIES Epic K·L·M |
| 5 | **v1.2 P1 3건** — 급여제공 기록 세분화(식사·목욕·간호, 케어포 3-1 한장 기록지)·직원근태/교육(8장)·본인부담 간편계산기(7-10) | 케어포·엔젤 통합 기록지 | health_records 확장·근태 테이블 |
| 6 | **UX 패턴** — 케어포 대시보드 **3블록(오늘 일정·미처리·공지)** + 좌측 **번호식 2~3단 메뉴**; 엔젤 **직무별 자동 메뉴 + 한장 통합 기록지**; 이지케어 **달력형 일정** | [IT리드 가이드](https://itread.kr/blog/0464-shortcut-6/)·엔젤/이지케어 앱 | v1.2 SideNav 그룹·대시보드 위젯 설계(UXD) |
| 7 | **v2/Won't 유지** — CMS·간편결제(7-4/5)·재무회계(12)·평가 자동화·프로그램/이동서비스(2·5)는 밀도 목표 외 | 5차 G2·G4·G5 | MVP 제외 불변 |

**차별화 재확인(불변)**: ogada는 케어포에 **없는** QR B방식·다지점 HQ(`/dashboard/hq`)·플랫폼 개통(`/platform`)·7역할 RBAC **4축** 보유 — 화면 수 갭과 별개로 영업 우위 유지.  
**planner 후속**: ROADMAP v1.2 P0/P1 `status: planned`(완료 기준 화면 커버리지 ≥60%+2단 SideNav), USER_STORIES Epic K·L·M, REQUIREMENTS §3 Should(직원·프로그램·식사) v1.2 승격 후보, **결정 49 확정**.  
**미해결 추적**: #27(공단 엑셀 실컬럼)·#31(가격 tier)·#32(다지점 HQ 경쟁사 사례)·#33(보호자 채널)·#35(duration_band).

---

## 2026-06-06 — planner(PLN): 자동 기획 동기화 9차 (TSR 8·9차 재검증 반영 + coder 미조치 에스컬레이션)

`build --role planner` 자동 동기화. **핵심 입력은 TSR 8차(15:38)·9차(15:45) 재검증**(`QA_FEEDBACK.md`·`TEST_REPORT.md`) — 7차(15:15) 이후 추가된 재검증 2회 모두 **회귀·이관 상태 완전 불변, coder 미조치, 신규 Open 0건**. Planned 9건(B01·B03·B04·B05·B06·B07·H04·M01·SEC-005) 전부 잔존. 벤치마크(5차)는 신규 입력 없음 — **현황 정합·정확도 갱신·에스컬레이션 중심**(신규 기획·태스크·결정 없음).

| # | 반영 | 산출물 |
|---|------|--------|
| 1 | `## QA 피드백 반영` 9차 노트(TSR 8·9차 — B07 악화 22m+20u·신규 `AttendanceStatsPage`·`BranchesPage`, M01 develop working tree `vitest` 6 PASS 미커밋), 메타·변경 이력 | `docs/planning/ROADMAP.md` |
| 2 | v1.1 완료 기준 M01·B07 항목 9차 근거(로컬 완성·develop HEAD 미커밋) 주석 | `docs/planning/ROADMAP.md` |
| 3 | `### QA 피드백 반영 9차` 표·진단, 자동 동기화 9차 섹션, **추가 질문 #36(coder 장기 미조치 에스컬레이션)** | `docs/planning/PLAN_NOTES.md` |
| 4 | 9차 동기화 기록 | `memory/decisions.md` 최상단 |

**핵심 판단**: 잔여 BLOCK 9건은 **기능 미구현이 아니라 이관 규율 미준수**(완료 단위 develop 커밋·`merge_status` 미승격). backend Maven 79/79·frontend build·frontend 자동 테스트(vitest 6 PASS)가 모두 develop **working tree에 사실상 완성**돼 있으나 develop HEAD 미커밋(B06·B07). → 결정 41·44·45(이관 규율 1·5·6)로 이미 커버되어 **신규 결정 불필요**, develop 커밋 한 단계가 유일 블로커.

**에스컬레이션(#36)**: QA Planned 9건이 5·6·7차 태스크화 후 TSR 8·9차까지 **coder 0건 조치**. planner/사용자 확인 필요 — ① coder 루프가 `status: in_progress` 버전을 실제 커밋하는지(워크트리 권한·자동 커밋 단계), ② 완료 단위 자동 develop 커밋을 coder 실행 프로토콜에 강제할지(`.agents` 워크플로우). **실행/운영 게이트 결정 사항**(기획 변경 아님).

**미변경**: REQUIREMENTS·USER_STORIES·API_SPEC·FLOWCHART(7·8차까지 반영), DB 제약(V1–V39), 청구 2단계·QR B·platform_admin·MVP 제외. **미해결 추적**: #27·#31·#32·#33·#35·#36.

---

## 2026-06-06 — planner(PLN): 8차 사용자 피드백 (파비콘·기능 밀도·docs 재구성)

| # | 결정 | 산출물 |
|---|------|--------|
| 46 | v1.1 **파비콘 Must** (US-UX-01) — UXD §11 → COD `public/` | `product/DESIGN_SYSTEM.md`, `planning/ROADMAP.md` v1.1 |
| 47 | **BNK 6차** 경쟁사 화면·메뉴 전수 매핑 → **v1.2** P0~P2 백로그 | `planning/research/BENCHMARK_REPORT.md` §9, `planning/ROADMAP.md` v1.2 |
| 48 | `docs/` **역할별 하위 폴더** — 삭제 없이 `README.md` 인덱스 | `docs/README.md`, `AGENT_USAGE.md` §1 |
| 49 | *(BNK-6 완료 후)* SideNav 2단·화면 커버 KPI **≥60%** (v1.2 완료 기준 초안) | `COMPETITOR_MATRIX.md` §4 |

**에이전트 지시**: `PLAN_NOTES.md` `### [PLN] 에이전트 작업 지시` — BNK 즉시 `build --role benchmark_researcher`, UXD/COD 파비콘 병행.

---

## 2026-06-06 — planner(PLN): 자동 기획 동기화 7차 (dirty-tree 재오염 + frontend false Fixed 회귀 + createClient 계약 명세화)

`build --role planner` 자동 동기화. **핵심 입력은 TSR 재검증**(`QA_FEEDBACK.md`·`TEST_REPORT.md` 2026-06-06T14:45 backend·14:55 frontend):
develop fix 커밋 직후 **dirty-tree 재오염**(backend B06 — 신규 client↔guardian 미커밋, `createClient` `primaryGuardian` 필수 **API 계약 변경**)과 frontend `Fixed` 3건의 **false Fixed 회귀**(H04 실 API·M01 Vitest·SEC-005 localStorage가 develop HEAD 미반영) + frontend working tree 대량 오염(B07). 벤치마크(5차)는 신규 입력 없음 — QA 회귀 처리 중심.

| # | 반영 | 산출물 |
|---|------|--------|
| 1 | v1 완료 기준 QA-B02 `[x]` 철회(working tree 재오염), v1.1 H04·M01 `[x]` 철회·SEC-005 항목 신설 | `docs/planning/ROADMAP.md` |
| 2 | `## QA 피드백 반영` 7차 노트 + **이관 규율 6항(완료 단위 커밋·API 계약 변경 문서화 게이트)**, QA→태스크 매핑 B06·B07·SEC-005, 변경 이력 | `docs/planning/ROADMAP.md` |
| 3 | `POST /clients` **`primaryGuardian` 필수 계약 명세화**(누락 400·단일 트랜잭션·`guardian_link_status=LINKED` V39) | `docs/technical/API_SPEC.md` §4 |
| 4 | §16 프론트 구현 규약 **FE-5**(JWT 메모리 세션·localStorage 금지, SEC-005) | `docs/planning/USER_STORIES.md` |
| 5 | **결정 45**(dirty-tree·계약 문서화 게이트 + createClient 보호자 계약 확정), `### QA 피드백 반영 7차` 표, 자동 동기화 7차 섹션 | `docs/planning/PLAN_NOTES.md` |
| 6 | Open 5건(B06·B07·H04·M01·SEC-005) → **Planned 이동** | `docs/qa/QA_FEEDBACK.md` |

**결정 45 (이관 규율 6 + 보호자 계약 확정)**: ① 한 작업의 `Fixed`/`[x]` 직후라도 새 작업을 **working tree 미커밋으로 남기지 않는다**(완료 단위 develop 커밋 — B06·B07). ② **API 계약 변경**(필수 필드 추가 등, 예: `createClient` `primaryGuardian` 필수)은 **develop 커밋 전 API_SPEC·ROADMAP 반영** — 미반영 계약 변경은 이관 BLOCK. ③ B06 작업 범위는 **v1 US-D01(보호자 1명 이상 필수, 결정 19) 확정** — 신규 스토리 불필요, 누락된 API 계약만 명세화.

**coder 다음 액션 (7차)**: B06(client↔guardian develop 커밋 + API_SPEC §4 정합·working tree clean) → 잔여 backend(H02·H01·B02·B01) → **v1 merged** → (frontend) SEC-005(메모리 세션)·H04(실 API)·M01(Vitest) develop 커밋 → B07(working tree clean)·B03(v1.1 ready). 각 `Fixed` 전 `git show develop:<path>` 자기검증(결정 44) + 완료 단위 커밋·계약 문서 선반영(결정 45) 필수.

**미변경**: REQUIREMENTS·FLOWCHART(US-D01 이미 반영), DB 제약(V1–V39), 청구 2단계·QR B·platform_admin·MVP 제외. **미해결 추적**: #27·#31·#32·#33·#35.

---

## 2026-06-06 — benchmark_researcher: 5차 경쟁사 재검증 (2026 수가 전등급·가산·시장규모·케어포 메뉴 트리)

공식 사이트·롱텀 수가·케어포 `daycare/func.php`·NHIS 경영공시·엔젤 기능/가입 폼 재조사(조사일 **2026-06-06**).
산출물: `docs/planning/research/BENCHMARK_REPORT.md`(§2-1 시장규모·§3-1 메뉴 트리·§4-1 가산/월한도·§5-2 G11~G14),
`docs/planning/research/COMPETITOR_MATRIX.md` 5차 갱신.

| # | 결정·권고 | 근거 | planner/coder 영향 |
|---|----------|------|-------------------|
| 1 | **2026 주야간 수가 전등급×5밴드 전수 확정** — 1~5·인지지원 × 3~6h…13h+ (인지지원은 10h+부터 56,360 고정) | [롱텀 수가](https://www.longtermcare.or.kr/npbs/e/b/502/npeb502m01.web?menuId=npe0000002742), [강남구청](https://www.gangnam.go.kr/board/happyapgu_faq/613/view.do) | `hq_admin` 수가 입력 화면 시드값·테스트 픽스처 |
| 2 | **가산율(G11)** — 야간(18-22)20·심야(22-06)30·주말/공휴일30·유급휴일50%, **중복 불가** | 공단 가산 규정([엔젤시터](https://angelsitter.co.kr/contents.php?cname=benefit_4)) | `fee_schedules` 부가 축 — **v1.1~v2**, 파일럿 표준 주간운영은 가산 드묾 |
| 3 | **월15일↑ 추가산정(G12)** — 월한도 1~2등급10·3~5등급20·치매전담50% | 압구정/강남 안내 | 월한도 초과 계산 — **v2** |
| 4 | **케어포 주야간 메뉴 트리(func.php) 확인** — 본인부담 7장이 청구→입금→미납→**CMS**→**간편결제** 5단계 수납 lifecycle | [func.php](https://www.carefor.co.kr/daycare/func.php) | **G13** 본인부담 수납(입금·미납) v1.1; ogada MVP는 7-1(청구·명세)만 패리티 |
| 5 | **시장규모 TAM** — 주야간보호 **5,598개소**(2025 3Q, 14.7%), 전체 29,734 | [NHIS 경영공시](http://www.nhis.or.kr/announce/wbhaec11502m01.do) | ogada 직접 경쟁 모수 ≈5,600 (케어포 14k·이지케어 9,210은 방문 포함) — 영업·가격(#31) |
| 6 | **엔젤 = 정원(capacity) 기준 과금** + 보호자 **이메일** 법정서식(급여비용명세서·기록지 월1회) 발송 | [엔젤 가입 폼](https://www.lcms.or.kr/reg/viewRegStep.do), [system_feature](http://www.silverangel.kr/silverangel/angelsystem/system_feature.do) | 과금 축 3종(flat/이용자수/정원, G10); 보호자 채널 **이메일** 저비용 대안(#33) |
| 7 | **케어포 「다기관 통합」은 제3자 블로그 마케팅 수준** — 공식 func.php·매뉴얼에 HQ 통합 대시보드 화면 **여전히 미확인** | [narayoung 블로그](https://a.narayoung.com/entry/노인-장기요양-케어포-carefor) vs 공식 | ogada `/dashboard/hq` 차별 **유지**(#32) |
| 8 | **등급변동 이력(G14)** — 케어포 1-9·엔젤 등급조정내역 존재 | func.php·엔젤 system_feature | ogada `clients.ltc_grade` 단일값 → **이력화 검토**(Should) |

**미변경(4차와 동일)**: 청구 2단계, QR B, platform_admin, NHIS `처리상태` 파서(케어포 44438 **조치완료** 재확인),
MVP 제외(평가·회계·CMS), 수가 1밴드→v1.1 다밴드(결정 42).
**신규 추적**: G11(가산율)·G12(월한도 추가산정)·G13(수납 lifecycle)·G14(등급변동 이력) — planner 로드맵 분류 입력.

---

## 2026-06-06 — planner(PLN): 자동 기획 동기화 6차 (false Fixed 회귀 처리 + 이관 규율 검증 게이트)

`build --role planner` 자동 동기화. **핵심 입력은 TSR 재검증**(`docs/qa/QA_FEEDBACK.md` 2026-06-06T07:52):
5차에서 `Fixed`로 옮긴 **backend 산출물(QA-H01 `처리상태` 파서·SEC-001/002/004=H02)이 develop HEAD에
미반영**(test working tree·stash 한정)임이 확인되어 **Open 복귀**(false Fixed). 즉 결정 41(develop 커밋
우선)이 실제로 위반된 재발 사례. 벤치마크(BENCHMARK·COMPETITOR_MATRIX 4차)는 5차 이후 신규 입력 없음.

| # | 반영 | 산출물 |
|---|------|--------|
| 1 | v1 완료 기준 **QA-H01 `[x]` 철회**(develop HEAD 미반영) | `docs/planning/ROADMAP.md` |
| 2 | `## QA 피드백 반영` 6차 회귀 노트 + **이관 규율 5항(Fixed↔develop HEAD `git show` 검증 게이트)** 신설·변경 이력·메타 owner COD→PLN 복원 | `docs/planning/ROADMAP.md` |
| 3 | backend Open 4건(B01·B02·H01·H02) → **Planned 재이동**(planned 매핑) | `docs/qa/QA_FEEDBACK.md` |
| 4 | **결정 44**(Fixed↔develop 검증 게이트), `### QA 피드백 반영 6차` 표, 6차 동기화 섹션 | `docs/planning/PLAN_NOTES.md` |

**결정 44 (이관 규율 강화)**: coder는 `Fixed` 기록·완료 기준 `[x]` 전에 `git show develop:<path>`로 산출물이
develop HEAD에 존재함을 **자기검증**한다. 미커밋·stash·working tree 근거 `Fixed`/`[x]`는 무효 — 재검증 시
Open 복귀·체크박스 철회. frontend `Fixed`(QA-H03/H04/M01·SEC-003)는 develop HEAD 반영 확인 — **영향 없음**.

**coder 다음 액션**: H02(SEC develop 커밋) → H01(파서+테스트 develop 커밋) → B02(working tree clean) →
B01(v1 `[x]`·`ready`) → **v1 merged** → (frontend) B04·B03. 각 `Fixed` 전 `git show` 자기검증 필수.

**미변경**: USER_STORIES §16·US-G04·G9, REQUIREMENTS·API_SPEC·FLOWCHART(5차 이미 반영), 청구 2단계, QR B,
platform_admin, MVP 제외, DB 제약(V1–V37). **미해결 추적**: #27·#31·#32·#35.

---

## 2026-06-06 — planner(PLN): 자동 기획 동기화 5차 (QA Open 10건 태스크화 + 4차 벤치마크 G9)

`build --role planner` 자동 동기화. 이전 4차까지 QA Open **0건**이었으나, tester 첫 이관 검증으로
`docs/qa/TEST_REPORT.md` 작성 + `docs/qa/QA_FEEDBACK.md` Open **10건**(BLOCK 5·HIGH 4·MEDIUM 1) 발생.
**테스트 PASS(Maven 81/81·Vite build) ≠ 이관 PASS(BLOCK)** — develop 미커밋·merge_status 미승격·기능 갭.

| # | 반영 | 산출물 |
|---|------|--------|
| 1 | `## QA 피드백 반영` 신설 — QA→태스크 매핑·**이관 규율 4항**(develop 커밋 우선·Fixed↔develop 정합·ready 게이트·v1선행) | `docs/planning/ROADMAP.md` |
| 2 | v1 완료 기준 — QA-H01 `처리상태` 파서 **테스트**·QA-H02 SEC develop 커밋·QA-B01/B02 working tree clean | `docs/planning/ROADMAP.md` |
| 3 | v1.1 완료 기준 — QA-H03(ProtectedRoute)·H04(실 API 연동)·M01(Vitest)·B05 선행 게이트·B03/B04 | `docs/planning/ROADMAP.md` |
| 4 | US-G04 선행열 샘플 테스트, US-G00a G9 duration_band, **§16 프론트 구현 규약 FE-1~4** | `docs/planning/USER_STORIES.md` |
| 5 | 결정 41(이관 규율)·42(수가 1밴드→다밴드)·43(프론트 실 API), QA 반영 5차 표, 추가질문 #35 | `docs/planning/PLAN_NOTES.md` |
| 6 | Open 10건 → **Planned** 이동(각 항목 `planned` 매핑) | `docs/qa/QA_FEEDBACK.md` |

**4차 벤치마크(G9)**: 공단 2026 수가는 **등급×이용시간대** 2차원 — v1 파일럿 1밴드 고정, v1.1 `duration_band`
다밴드(결정 42, 추가질문 #35). G10 가격·G8 EZCARE는 기존 반영 유지.

**coder 다음 액션**: B02/H02(backend develop 커밋·SEC 정합) → H01(파서+테스트) → B01(v1 ready) →
**v1 merged** → B04/H03/H04/M01(frontend) → B03(v1.1 ready).

**미해결 추적**: #27(공단 엑셀 실컬럼·G7), #31(가격 tier), #32(다지점 HQ 사례), #35(duration_band 표준시간).
**미변경**: 청구 2단계, QR B, platform_admin, MVP 제외(평가·회계·CMS), DB 제약(V1–V36).

---

## 2026-06-06 — db_architect(DBA): V36 마이그레이션 (clients·billing 시간 정합 CHECK)

V1–V35 커버리지 재대조 (ERD §4·§7-31, API_SPEC §4/§7, DATA_RETENTION §4-1, PLAN_NOTES
#22/#27 V34 패턴 확장). Must 엔티티 시간 단조성을 DB에서 완성 — `created_at` ↔ `*_at`
역전 방어가 backup(V12)·NHIS(V20)·clients discharge(V34)에 그치지 않고 PII consent·
LTC 인정·청구 생성까지 확장. coder 흐름은 변경 없음(기존 데이터 항상 충족).

| # | 결정·산출물 | 근거 | coder·tester 영향 |
|---|------------|------|-------------------|
| 1 | `chk_clients_consent_after_created` — `consent_collected_at IS NULL OR consent_collected_at >= created_at` | REQUIREMENTS §3-2-1 2단계 동의·V3/V5 RRN consent CHECK | `ClientService.collectConsent`는 `OffsetDateTime.now()` 적재 → 항상 충족. PII 이관·raw SQL backfill 시 backdated 거부 |
| 2 | `chk_clients_ltc_cert_valid_from_after_birth` — `ltc_cert_valid_from IS NULL OR ltc_cert_valid_from >= birth_date` | REQUIREMENTS §3-2 LTC 인정서·V2 컬럼·V4 종료일 정합 | 등록 입력 typo(예: 출생 1945-03-02 / 인정 1945-03-01) 거부. `ltc_cert_valid_from` nullable 유지(2단계 등록) |
| 3 | `chk_billing_claims_generated_after_created` — `generated_at >= created_at` | API_SPEC §7-3 claim 재계산·V1 `generated_at` DEFAULT NOW() | `BillingService.generateClaim`은 `setGeneratedAt(now())` → 항상 충족. raw SQL 직접 UPDATE·이력 backdate 거부 (V8 status 단방향 트리거와 보완) |

**시간 정합 패턴 완성도**:

| 테이블 | 시간 정합 CHECK | 버전 |
|--------|----------------|------|
| `backup_runs` | `completed_at >= started_at` | V12 |
| `nhis_import_batches` | `imported_at >= created_at` | V20 |
| `refresh_tokens`·`password_reset_tokens`·`branch_qr_tokens` | `expires_at >= created_at` | V13 |
| `clients` | `discharged_at >= created_at` | V34 |
| `clients` | `consent_collected_at >= created_at`, `ltc_cert_valid_from >= birth_date` | **V36** |
| `billing_claims` | `generated_at >= created_at` | **V36** |
| `branch_qr_tokens` | `expires_at::date >= valid_date` | V14 |

**미변경**: actor 자동 적재(V32/V33/V35), Tenant FK 패턴(V5/V14/V21/V22), 청구 동결(V8/V11),
NHIS reconciliation(V19/V21), 이용자 retention(V32/V33/V34). Must 엔티티 핵심 제약은 V1–V35에서 완료.

---

## 2026-06-06 — benchmark_researcher: 4차 경쟁사 재검증 (이지케어 요금·2026 수가·G9)

공식 사이트·요금표·롱텀 수가·케어포 2026 매뉴얼 재조사(조사일 **2026-06-06**). 산출물:
`docs/planning/research/BENCHMARK_REPORT.md`, `docs/planning/research/COMPETITOR_MATRIX.md` 4차 갱신.

| # | 결정·권고 | 근거 | planner/coder 영향 |
|---|----------|------|-------------------|
| 1 | **`fee_schedules`에 duration_band(이용시간대) 축 검토** — 공단 2026 수가는 **등급×시간(3~6h…13h+)** 2차원 | [롱텀 2026 수가](https://www.longtermcare.or.kr/npbs/e/b/502/npeb502m01.web?menuId=npe0000002742), [케어포 2026 고시](https://www.carefor.co.kr/cs/view_pds.php?calmgno=46327) | G9 — MVP는 파일럿 **1밴드 고정** 가능, v1.1 다밴드; §3-9-1·ERD 보강 |
| 2 | **이지케어 공개 tier 요금** — 10,000 + (일정관리 N−10)×500 + VAT; 37명=25,850 | [ezCare_charge](https://ezcare.easyms.co.kr/new/ezCare_charge.html) | G10 — ogada 가격: 케어포 **flat 33k** vs 이지케어 **인원 비례** (PLAN_NOTES #31) |
| 3 | **롱텀 엑셀 다운로드** — Chrome/Edge 「안전하지 않은 콘텐츠」 허용 필수 | [케어포 FAQ cscmgno=1237](https://www.carefor.co.kr/cs/view_notice.php?cscmgno=1237) | USER_MANUAL·파일럿 NHIS import 온보딩 체크리스트 |
| 4 | **케어포 다지점** — getting_started에 **다기관 통합 매뉴얼 없음** 재확인; 1기관번호=1계정 유지 | [getting_started](https://www.carefor.co.kr/cs/getting_started.php) | ogada `/dashboard/hq` 차별 유지 — PLAN_NOTES #32 |
| 5 | **copay 15/9/6/0%** — 2026 공단·센터 안내와 ogada 4구분 **일치** 확인 | [강남구청 2026 안내](https://www.gangnam.go.kr/board/happyapgu_faq/613/view.do) | §3-9-2 유지; 케어포 3구분(7.5%)과의 UI 라벨 차이만 주의 |
| 6 | **이지케어 EZCARE 보호자** — **기관 초대 → 프로필 수락** 후 명세·청구 조회 | [Google Play](https://play.google.com/store/apps/details?hl=ko&id=com.easyms.ezcare) | v1.1 G8 — ogada `guardian` 초대 흐름 벤치마크 |

**미변경(3차와 동일)**: 청구 2단계, QR B, platform_admin, NHIS `처리상태` 파서, MVP 제외(평가·회계·CMS).

---

## 2026-06-06 — benchmark_researcher: 3차 경쟁사 재검증 (EZCARE·NHIS·롱텀2026)

공식 사이트·매뉴얼·앱스토어·공지 재조사(조사일 **2026-06-06**). 산출물:
`docs/planning/research/BENCHMARK_REPORT.md`, `docs/planning/research/COMPETITOR_MATRIX.md` 3차 갱신.

| # | 결정·권고 | 근거 | planner/coder 영향 |
|---|----------|------|-------------------|
| 1 | **NHIS 엑셀 파서** — 선행 `처리상태` 열 **스킵·정규화** 필수 | 케어포 [44438](https://www.carefor.co.kr/cs/view_notice.php?calmgno=44438), [visitcare.pdf §4-1](https://www.carefor.co.kr/pdf_manual/visitcare.pdf) | import 파서·reconciliation — G7 파일럿 샘플과 병행 검증 |
| 2 | **롱텀 2026.01.16 개편** — IE 불가, Chrome/Edge 필수 안내 | [longtermcare 개편 공지](https://longtermcare.or.kr/npbs/e/g/540/openCyberCstMain.web?menuId=npe0000002594) | USER_MANUAL·파일럿 온보딩: 엑셀 export 전 브라우저 체크 |
| 3 | **이지케어 EZCARE 앱** — 보호자 **초대·명세 조회** 지원 확인 | [App Store](https://apps.apple.com/kr/app/%EC%9D%B4%EC%A7%80%EC%BC%80%EC%96%B4-ezcare/id6740553966), 2026.03 주야간 확대 | G8 신규 — v1.1 보호자 포털은 **초대 흐름+명세 탭**이 최소 패리티 |
| 4 | **다지점 HQ** — 경쟁사는 **1기관번호=1계정** 모델(△), ogada Org-Branch **차별 유지** | 케어포 가입·기관기호 11자리; 공식 HQ 대시보드 **미확인** | `/dashboard/hq` Must — PLAN_NOTES #32 |
| 5 | **엔젤 CMS TCO** — 월 30,000원 + 건당 수수료 벤치마크 | [silverangel extraService](https://www.silverangel.kr/newSilverangel/service/extraService.do) | v2 CMS·가격 정책(PLAN_NOTES #31) 입력 |
| 6 | **이지케어 규모** — 9,210 재가기관(2026.06.06 실시간) | [ezcare.easyms.co.kr](https://ezcare.easyms.co.kr/) | 영업·경쟁 포지셔닝 참고 |

**미변경(2차와 동일)**: 청구 2단계, QR B, platform_admin, MVP 제외(평가·회계·CMS).

---

## 2026-06-06 — planner(PLN): 자동 기획 동기화 3차 (QA 0건·문서 식별자 PLA→PLN 정렬)

`build --role planner` 자동 동기화. 입력 문서 재확인 결과 **신규 기획 변경 없음** —
정합성 정렬과 기록만 수행.

| # | 점검·반영 | 산출물 |
|---|----------|--------|
| 1 | `QA_FEEDBACK.md` Open **0건**, `TEST_REPORT.md` 미작성 — Planned 이동 없음 | (변경 없음) |
| 2 | BENCHMARK·COMPETITOR_MATRIX 2차 조사(결정 29–35) **이미 반영** 확인 | (변경 없음) |
| 3 | planner 문서 식별자 정본 정렬: `agents.yaml` 기준 `PLA→PLN`, audience `coder,tester→COD,TSR,UXD,DBA,BNK,TWR` (BNK는 선행 마이그레이션 완료) | `ROADMAP.md`·`PLAN_NOTES.md`·`FLOWCHART.md`·`API_SPEC.md`·`REQUIREMENTS.md`·`USER_STORIES.md` 메타, PLAN_NOTES 섹션 `[PLA]→[PLN]` |
| 4 | 자동 동기화 3차 기록 | `PLAN_NOTES.md` `### [PLN] 자동 기획 동기화 — 3차`, `ROADMAP.md` 변경 이력 |

**트레이드오프**: 식별자 정렬은 본문 메타 주석만 변경(파일명·git 충돌 회피). REQUIREMENTS·
USER_STORIES는 기존에 메타 주석이 없어 신규 추가 — 향후 `doc:owner`/`audience` 자동 점검과 정합.
**미해결 추적**: 추가질문 #27(공단 엑셀 실컬럼·G7), #31(가격 tier), #32(다지점 HQ 사례) — 신규 입력 없어 변동 없음.

---

## 2026-06-06 — planner: 보호자 연결 필수 + 카카오톡 채널 알림 로드맵

| # | 결정 | 근거 | 영향 |
|---|------|------|------|
| 1 | **이용자 등록 시 보호자 1명 이상 필수** — `POST /clients` + `primaryGuardian` | US-D01·QR B·알림 수신 전제 | V39 `guardian_link_status`, `ClientService.create` |
| 2 | **v1.1** 보호자 알림 = 인앱·FCM·이메일(무료) 골격만 | 파일럿 비용·구현 속도 | Epic J01·J02 범위 유지 |
| 3 | **v2** 보호자 외부 알림 = **카카오톡 채널 알림톡** (+ SMS fallback) | 케어포·이지케어 패리티, 국내 도달률 | US-J03, `NotificationService` |

---

## 2026-06-06 — planner: 자동 기획 동기화 (벤치마크 2차 → ROADMAP·API·FLOWCHART)

`build --role planner` 자동 동기화. QA_FEEDBACK Open **0건**, TEST_REPORT 미작성.

| # | 반영 | 산출물 |
|---|------|--------|
| 1 | v1 ROADMAP에 P0–P3·NHIS reconciliation 완료 기준·파일럿 P8 추가 | `docs/planning/ROADMAP.md` |
| 2 | API_SPEC §7-4 NHIS reconciliation 5엔드포인트·`?status=` 필터 명세 | `docs/technical/API_SPEC.md` |
| 3 | FLOWCHART §7-1 reconciliation Mermaid 흐름 | `docs/planning/FLOWCHART.md` |
| 4 | PLAN_NOTES `[PLA]` QA·벤치마크 동기화 섹션, 결정 29–35, 추가질문 #30–32 | `docs/planning/PLAN_NOTES.md` |
| 5 | USER_STORIES 파일럿 P8(US-G06) | `docs/planning/USER_STORIES.md` |

**미변경(기존 반영 완료)**: REQUIREMENTS §1-5·§6-2, USER_STORIES US-G06, BENCHMARK/COMPETITOR_MATRIX.

---

## 2026-06-06 — benchmark_researcher: 2차 경쟁사 벤치마크 (케어포·이지케어·엔젤·롱텀)

공식 사이트·매뉴얼·FAQ·공지(조사일 **2026-06-06**) 재조사. 산출물:
`docs/planning/research/BENCHMARK_REPORT.md`, `docs/planning/research/COMPETITOR_MATRIX.md` 전면 갱신.

| # | 결정·권고 | 근거 | planner/coder 영향 |
|---|----------|------|-------------------|
| 1 | **청구 2단계(내부계산 + 롱텀 + 엑셀 import + 본인부담)** — ogada MVP 방향 **유지** | 케어포·이지케어 공통 패턴 ([케어포 교육](https://www.carefor.co.kr/cs/view_notice.php?calmgno=43619), [이지케어 fnc](https://ezcare.easyms.co.kr/new/ezCare_fnc.html)) | §3-9·NHIS import 우선 구현 |
| 2 | **QR B방식(보호자→지점 QR)** — **차별화 유지**, NFC/RFID MVP **불필요** | 케어포=NFC 직원앱, 이지케어=RFID(방문), 공개 자료에 보호자 QR **없음** | 파일럿 P1; 하드웨어 제외 |
| 3 | **`platform_admin` Tenant 개통** — 경쟁사 셀프/상담 가입과 **의도적 차별** 유지 | 케어포 셀프+1mo무료, 이지케어 상담, 엔젤 온라인 | §1-3 A방식 확정 재확인 |
| 4 | **다지점 HQ 대시보드** — MVP **Must** (경쟁사 공개 자료 동등 기능 **미확인**) | ogada 파일럿 2지점 | `/dashboard/hq` 파일럿 핵심 |
| 5 | **평가·재무회계·CMS·이동서비스** — MVP **제외** 유지 | 케어포/엔젤=평가·CMS, 이지케어=회계 | Should/Could 로만 로드맵 |
| 6 | **NHIS 엑셀 실컬럼** — 파일럿 센터 샘플 확보 **P0** (PLAN_NOTES #27) | 업계 import 공통이나 ogada 스키마 검증 필요 | import 파서·reconciliation UI |
| 7 | **보호자 포털** — MVP는 **QR+기록열람 골격**, 알림톡/CMS는 **v1.1** | 케어포 가족돌봄앱 성숙 | Should Epic 우선순위 |
| 8 | **가격 벤치마크** — 케어포 주야간 **월 33,000원(VAT포함)** 참고 ([cost.php](https://www.carefor.co.kr/price/cost.php)) | ogada 가격 미정 | 영업·플랫폼 정책 별도 |

**트레이드오프**: 경쟁사는 **기능 폭**(평가·회계·NFC)으로 lock-in; ogada는 **SaaS 다지점·QR·MVP 속도**로 파일럿→전국 판매.

---

## 2026-06-06 — db_architect: V19 마이그레이션 (공단 reconciliation 매칭·배치 무결성)

ERD·V1–V18·API_SPEC·USER_STORIES 재대조. 청구(billing) Must 엔티티 커버리지
점검 중 공단 import reconciliation 결과와 그 전제 데이터를 묶는 무결성 규칙이
없던 3개 공백을 `V19`로 마감. 동시에 ERD 문서 드리프트(V18 미기재,
`clients.discharged_at` 타입 표기 오류)를 정정.

| # | 결정 | 근거 |
|---|------|------|
| 1 | `nhis_import_rows`: `match_status`가 `MATCHED`/`DISCREPANCY`이면 `client_id` 필수 (`chk_nhis_import_rows_match_requires_client`) | 매칭 결과와 매칭 대상 이용자가 항상 함께 존재 — 이용자별 reconciliation 뷰 정합(API §7-3). `UNMATCHED`만 `client_id` NULL 허용 |
| 2 | `nhis_import_batches.row_count >= 0` | 파싱 행 수 음수 방어 |
| 3 | `nhis_import_batches`: `status = COMPLETED`이면 `imported_at` 필수 | `backup_runs` 완료 시각 패턴(V9/V12)과 정합 — 완료된 import는 완료 시각 보유 |

**트레이드오프**
- 세 제약 모두 유효 데이터에 대해 항상 참 → greenfield 기존 행 거부 없음. CHECK로
  표현 가능(교차 테이블 아님)하여 트리거 대신 ALTER ADD CONSTRAINT 사용.
- 배치 제약은 `COMPLETED`만 대상(`FAILED`/`PENDING`/`PROCESSING`은 `imported_at` NULL 허용).

**문서 정정**: ERD §4-3 `discharged_at` 타입 `date → timestamptz`(V2 실제와 일치),
§4-4 `branch_qr_tokens.token_value`(V18) 반영, §7 마이그레이션 표 V18·V19 추가.

**coder 영향**: 공단 엑셀 매칭 서비스는 행을 `MATCHED`/`DISCREPANCY`로 전이할 때
반드시 `client_id`를 함께 세팅해야 한다(부분 업데이트 금지). 배치 완료 처리 시
`status=COMPLETED`와 `imported_at`을 같은 트랜잭션에서 기록한다.

---

## 2026-06-05 — db_architect: V8 마이그레이션 (Tenant 무결성 + 청구 불변)

ERD·V1–V7·API_SPEC·USER_STORIES 대조 후, 문서엔 명시됐으나 DB로 강제되지
않던 4개 공백을 `V8`로 마감.

| # | 결정 | 근거 |
|---|------|------|
| 1 | `users.active_branch_id` 복합 FK `(organization_id, active_branch_id)` → `branches` | 활성 지점이 타 Tenant 지점일 수 없도록 차단 (V4/V5/V7 Tenant FK 패턴 일관화) |
| 2 | 청구 확정 후 **불변** 트리거 (`billing_claims`·`billing_claim_items`) + 단방향 상태 전이 | REQUIREMENTS §3-9-1 이력 보존, USER_STORIES US-G05 "확정 후 수정 제한", ERD §4-6 "확정 후 불변" |
| 3 | `nhis_import_rows`에 `organization_id` + 복합 FK(배치·이용자) | reconciliation 매칭이 타 Tenant 이용자로 새는 것 방지 (API §7-3) |
| 4 | `health_records (organization_id, record_type, recorded_at DESC)` 인덱스 | `GET /dashboard/hq/alerts` 전 지점 건강 이상 집계 (V7 attendance HQ 인덱스와 동형) |

**결정 배경 / 트레이드오프**
- 청구 불변은 CHECK로 표현 불가(이전 상태 비교 필요)하므로 BEFORE UPDATE/INSERT/DELETE
  **트리거**로 구현. `status` 전이와 `updated_at`은 허용, 금액·스코프만 잠금.
- `billing_claim_items` 동결 트리거는 부모 cascade 삭제 시 부모 행이 먼저 제거되어
  `SELECT status`가 NULL → 정상 cascade 허용(직접 조작만 차단).
- `nhis_import_rows.client_id`는 매칭 전 NULL이므로 복합 FK는 MATCH SIMPLE로 NULL 스킵.
- 기존 단순 FK는 유지(중복이나 무해), 복합 FK로 Tenant 스코프만 추가.

**coder 영향**: 청구 확정(`PATCH /billing/claims/{id}/status`)은 금액 재계산 없이
상태만 전이해야 함. 확정 후 라인/금액 수정 시도는 DB가 거부 → 애플리케이션은
DRAFT 단계에서만 generate/재계산 수행.
