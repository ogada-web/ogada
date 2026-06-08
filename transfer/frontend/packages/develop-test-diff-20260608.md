<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-08T05:00:00+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-08 86차 재검증)

> **86차 재검증 (05:00) — test `@c510f5c` 불변·143/46 PASS·125 modules·audit 0·develop `362dbf0`(+6 v1.3-A·v3 CLEAN)·164/54 PASS·139 modules·PASS(v1.2)·v1.3 pending·v3 develop-only**: 84차(test `c510f5c`·develop `7ef1083` +4) 대비 **test HEAD 불변** — v1.2 merged 유지. develop HEAD **`7ef1083`→`362dbf0`**(+2: `3e9a9ab` fix(a11y): v3 식사·프로그램 기록 폼 접근성 재점검 (US-N01·N02) · `362dbf0` test(v3): add meals/programs API E2E via pilotPageFlows (US-N01·N02)). 양 worktree **CLEAN**. **신규 Open 0건** — 판정 **PASS**(v1.2). v1.3 `in_progress`/`pending`(backend transport API test 미승격) · v3 **develop-only**(merge 게이트 미설정).

## 커밋 수준 (86차)

| 항목 | 84차 | 86차 |
|------|------|------|
| develop HEAD | `7ef1083` (+4) | **`362dbf0`** (+6) |
| test HEAD | `c510f5c` (v1.2 merged) | **`c510f5c`** (불변) |
| commits gap | develop 4 ahead | **develop 6 ahead** |
| develop WT | CLEAN | **CLEAN** |
| develop tests | 157/53 PASS | **164/54 PASS** |
| test tests | 143/46 PASS | **143/46 PASS** (불변) |

### develop 신규 커밋 (test `c510f5c` 이후, 86차 — 84차 대비 +2)

| SHA | Message |
|-----|---------|
| `3e9a9ab` | fix(a11y): v3 식사·프로그램 기록 폼 접근성 재점검 (US-N01·N02) |
| `362dbf0` | test(v3): add meals/programs API E2E via pilotPageFlows (US-N01·N02) |

> **`c510f5c..362dbf0` diff stat**: 33 files, +2602/-21 — v1.3-A Transport + a11y + v3 MealsPage·ProgramsPage·MealRecordForm·ProgramParticipationForm + US-G06 ReconciliationPage + **신규** v3 `MealRecordForm`·`ProgramParticipationForm`·`MealsPage`·`ProgramsPage` a11y 재점검(ARIA·레이블·키보드 내비게이션) + pilotPageFlows US-N01(식사 기록 API E2E)·US-N02(프로그램 참여 API E2E) + `services.js`(+v3 meals/programs endpoints).

## test 브랜치 (frontend-test @ `c510f5c`, 86차 TSR 독립 실측)

| 항목 | 결과 |
|------|------|
| working tree | **CLEAN** |
| build | **125 modules PASS** (vite 6.4.3, JS 320.10 kB gzip 91.25 kB, CSS 31.03 kB gzip 5.84 kB) |
| npm ci + npm test | **143/46 PASS** (vitest 4.1.8) |
| npm audit | **0 vulnerabilities** |
| 이관 규율 5 | ProtectedRoute·services.js·SideNav·pilotChecklist·AuthContext·ReconciliationPage **PRESENT** |
| SEC-005 | AuthContext localStorage/sessionStorage **0건** |

## develop HEAD (`362dbf0`, 86차 TSR 실측)

| 항목 | 결과 |
|------|------|
| working tree | **CLEAN** |
| npm test | **164/54 PASS** (+21/+8 vs test 143/46 — Transport·v3 Meals/Programs·v3 E2E US-N01·N02·UNMATCHED 회귀) |
| npm run build | **139 modules PASS** (vite 6.4.3, JS 347.60 kB gzip 97.57 kB, CSS 33.35 kB gzip 6.20 kB) |
| npm audit | **0 vulnerabilities** |
| v1.3-A 산출물 | TransportPage·RunNew·RunDetail·KakaoMap·Disclaimer·StopList·transport.js·transportUtils **HEAD PRESENT** |
| v3 산출물 | MealsPage·ProgramsPage·MealRecordForm·ProgramParticipationForm·meals.js·programs.js + a11y + pilotPageFlows US-N01·N02 **HEAD PRESENT** |
| 보안 | KAKAO 지도 키 `import.meta.env.VITE_KAKAO_MAP_JS_KEY`(하드코딩 0) · `MAX_TRANSPORT_STOPS=15` |

## 판정 (86차)

**PASS** (v1.2) — test `@c510f5c` v1.2 merged 검증 불변. develop +6 v1.3-A·v3 **CLEAN** (non-blocking).
**v1.3 이관 게이트 미충족(pending)** — v1.3-A frontend UI 셸은 backend v1.3-A transport API(develop `53a1ffe` PRESENT, **test 미승격**)·RBAC·US-T01~T03 라이브 E2E 동반 후 merge. **v3(식사·프로그램) develop-only** — ROADMAP 버전·merge 게이트 미설정(planner 정의 대기), 정상(결함 아님). 잔여 BLOCK: backend merge(18) + SEC-D14 + post-merge live E2E(결정 73).

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-08T03:55:00+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-08 84차 재검증)

> **84차 재검증 (03:55) — test `@c510f5c` 불변·143/46 PASS·125 modules·audit 0·develop `7ef1083`(+4 v1.3-A·v3 CLEAN)·157/53 PASS·139 modules·PASS(v1.2)·v1.3 pending·v3 develop-only**: 82차(test `c510f5c`·develop `e8d1854` +2) 대비 **test HEAD 불변** — v1.2 merged 유지. develop HEAD **`e8d1854`→`7ef1083`**(+2: `f0b174a` fix(a11y): v1.3 배차 UI 접근성 재점검 · `7ef1083` feat(v3): add meals and programs management UI shell §3-5·§3-6). 양 worktree **CLEAN**. **신규 Open 0건** — 판정 **PASS**(v1.2). v1.3 `in_progress`/`pending`(backend transport API test 미승격) · v3 **develop-only**(merge 게이트 미설정).

## 커밋 수준 (84차)

| 항목 | 82차 | 84차 |
|------|------|------|
| develop HEAD | `e8d1854` (+2) | **`7ef1083`** (+4) |
| test HEAD | `c510f5c` (v1.2 merged) | **`c510f5c`** (불변) |
| commits gap | develop 2 ahead | **develop 4 ahead** |
| develop WT | CLEAN | **CLEAN** |
| develop tests | 150/50 PASS | **157/53 PASS** |
| test tests | 143/46 PASS | **143/46 PASS** (불변) |

### develop 신규 커밋 (test `c510f5c` 이후, 84차)

| SHA | Message |
|-----|---------|
| `f01e3a8` | feat(uxd-43): US-G06 UNMATCHED 후보 이용자 검색 UI 보강 |
| `e8d1854` | feat(v1.3): add transport pickup dispatch UI shell (US-T01~T03) |
| `f0b174a` | fix(a11y): v1.3 배차 UI 접근성 재점검 (US-T01~T03) |
| `7ef1083` | feat(v3): add meals and programs management UI shell (§3-5·§3-6) |

> **`c510f5c..7ef1083` diff stat**: 31 files, +2540/-15 — v1.3-A Transport(`TransportPage`(+test)·`TransportRunNewPage`·`TransportRunDetailPage`·`transportUtils`(+test)·`KakaoTransportMap`·`TransportStopList`(+test)·`TransportDisclaimer`·`config/transport.js`) + a11y 재점검 + **v3 신규** `MealsPage`(+test)·`ProgramsPage`(+test)·`components/meals/MealRecordForm`(+test)·`components/programs/ProgramParticipationForm`·`config/meals.js`·`config/programs.js` + `App.jsx`·`navConfig`·`roleNav`·`sevenRoleRouteMatrix`·`services.js`(+75)·`components.css`(+150) + US-G06 `ReconciliationPage`(+test).

## test 브랜치 (frontend-test @ `c510f5c`, 84차 TSR 독립 실측)

| 항목 | 결과 |
|------|------|
| working tree | **CLEAN** |
| build | **125 modules PASS** (vite 6.4.3, JS 320.10 kB gzip 91.25 kB, CSS 31.03 kB gzip 5.84 kB) |
| npm ci + npm test | **143/46 PASS** (vitest 4.1.8) |
| npm audit | **0 vulnerabilities** |
| 이관 규율 5 | ProtectedRoute·services.js·SideNav·pilotChecklist·AuthContext·ReconciliationPage **PRESENT** |
| SEC-005 | AuthContext localStorage/sessionStorage **0건** |

## develop HEAD (`7ef1083`, 84차 TSR 실측)

| 항목 | 결과 |
|------|------|
| working tree | **CLEAN** |
| npm test | **157/53 PASS** (+14/+7 vs test 143/46 — Transport·v3 Meals/Programs·UNMATCHED 회귀) |
| npm run build | **139 modules PASS** (vite 6.4.3, JS 347.26 kB gzip 97.45 kB, CSS 33.35 kB gzip 6.20 kB) |
| npm audit | **0 vulnerabilities** |
| v1.3-A 산출물 | TransportPage·RunNew·RunDetail·KakaoMap·Disclaimer·StopList·transport.js·transportUtils **HEAD PRESENT** |
| v3 산출물 | MealsPage·ProgramsPage·MealRecordForm·ProgramParticipationForm·meals.js·programs.js **HEAD PRESENT** |
| 보안 | KAKAO 지도 키 `import.meta.env.VITE_KAKAO_MAP_JS_KEY`(하드코딩 0) · `MAX_TRANSPORT_STOPS=15` |

## 판정 (84차)

**PASS** (v1.2) — test `@c510f5c` v1.2 merged 검증 불변. develop +4 v1.3-A·v3 **CLEAN** (non-blocking).
**v1.3 이관 게이트 미충족(pending)** — v1.3-A frontend UI 셸은 backend v1.3-A transport API(develop `53a1ffe` PRESENT, **test 미승격**)·RBAC·US-T01~T03 라이브 E2E 동반 후 merge. **v3(식사·프로그램) develop-only** — ROADMAP 버전·merge 게이트 미설정(planner 정의 대기), 정상(결함 아님). 잔여 BLOCK: backend merge(17) + SEC-D14 + post-merge live E2E(결정 73).

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-08T02:37:00+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-08 82차 재검증)

> **82차 재검증 (02:37) — v1.2 develop→test merge 완료·test `@c510f5c`·143/46 PASS·125 modules·audit 0·develop `e8d1854`(+2 v1.3-A CLEAN)·2 ahead·develop 150/50 PASS·133 modules·PASS(v1.2)·v1.3 pending**: 81차(test `4f71543`·develop `c510f5c` +15) 대비 **v1.2 develop→test merge 실행** — test HEAD **`4f71543`→`c510f5c`**(v1.2 merged, ROADMAP 부합). develop HEAD **`c510f5c`→`e8d1854`**(+2: `f01e3a8` feat(uxd-43): US-G06 UNMATCHED 후보 이용자 검색 UI 보강 · `e8d1854` feat(v1.3): add transport pickup dispatch UI shell (US-T01~T03)). 양 worktree **CLEAN**. **신규 Open 0건** — 판정 **PASS**(v1.2). v1.3 `in_progress`/`merge_status: pending` — v1.3-A UI 셸 한정.

## 커밋 수준 (82차)

| 항목 | 81차 | 82차 |
|------|------|------|
| develop HEAD | `c510f5c` | **`e8d1854`** (+2) |
| test HEAD | `4f71543` (v1.1 merged) | **`c510f5c`** (v1.2 merged) |
| commits gap | develop 15 ahead | **develop 2 ahead** |
| develop WT | CLEAN | **CLEAN** |
| develop tests | 143/46 PASS | **150/50 PASS** |
| test tests | 58/18 PASS | **143/46 PASS** (v1.2 흡수) |

### v1.3-A develop 신규 커밋 (test `c510f5c` 이후, 82차)

| SHA | Message |
|-----|---------|
| `f01e3a8` | feat(uxd-43): US-G06 UNMATCHED 후보 이용자 검색 UI 보강 |
| `e8d1854` | feat(v1.3): add transport pickup dispatch UI shell (US-T01~T03) |

> **`c510f5c..e8d1854` diff stat**: 20 files, +1483/-11 — v1.3-A `TransportPage.jsx`(+test)·`TransportRunNewPage.jsx`·`TransportRunDetailPage.jsx`·`transportUtils.js`(+test)·`components/transport/KakaoTransportMap.jsx`·`TransportStopList.jsx`(+test)·`TransportDisclaimer.jsx`·`config/transport.js`·`layout/navConfig.js`·`auth/roleNav.js`·`App.jsx`·`api/services.js`(+41)·`auth/sevenRoleRouteMatrix.js`·`styles/components.css`(+150) + US-G06 `pages/ReconciliationPage.jsx`(+test) UNMATCHED 후보 검색.

## test 브랜치 (frontend-test @ `c510f5c`, 82차 TSR 독립 실측)

| 항목 | 결과 |
|------|------|
| working tree | **CLEAN** |
| build | **125 modules PASS** (vite 6.4.3, JS 320.10 kB gzip 91.25 kB, CSS 31.03 kB gzip 5.84 kB) |
| npm ci + npm test | **143/46 PASS** (vitest 4.1.8) |
| npm audit | **0 vulnerabilities** |
| 이관 규율 5 | ProtectedRoute·services.js·SideNav·pilotChecklist·liveConfig·AuthContext·ReconciliationPage **PRESENT** |
| SEC-005 | AuthContext localStorage/sessionStorage **0건** |

## develop HEAD (`e8d1854`, 82차 TSR 실측)

| 항목 | 결과 |
|------|------|
| working tree | **CLEAN** |
| npm test | **150/50 PASS** (+7/+4 vs test 143/46 — Transport·UNMATCHED 회귀) |
| npm run build | **133 modules PASS** (vite 6.4.3, JS 334.18 kB gzip 94.86 kB, CSS 33.35 kB) |
| npm audit | **0 vulnerabilities** |
| v1.3-A 산출물 | TransportPage·TransportRunNewPage·TransportRunDetailPage·KakaoTransportMap·TransportDisclaimer·transport.js·transportUtils **HEAD PRESENT** |
| 운영 고지 | BNK-7 §10-3(이동서비스비 청구·G15 미포함) + BNK-8(케어포 패리티·경로 최적화 v1.3-B) **PRESENT** |
| 보안 | KAKAO 지도 키 `import.meta.env.VITE_KAKAO_MAP_JS_KEY`(하드코딩 0·키 누락 graceful) · `MAX_TRANSPORT_STOPS=15` |

## 판정 (82차)

**PASS** (v1.2) — test `@c510f5c` v1.2 merged 검증 완료. develop v1.3-A **+2 CLEAN** (non-blocking).
**v1.3 이관 게이트 미충족(pending)** — v1.3-A develop는 frontend UI 셸 한정. 완료 기준 중 DBA `transport_runs`/`stops` 스키마·roster/runs CRUD·**confirm** API·RBAC(DRAFT=hq_admin/CONFIRMED=직원 read)·Geocoding **서버 프록시**·US-T01~T03 라이브 E2E **미완**(backend 의존). v1.3 merge는 backend v1.3-A API 동반 완료 후 — 현 단계 정상(결함 아님). 잔여 BLOCK: backend merge(16) + SEC-D14 + post-merge live E2E(결정 73).

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-08T01:35:00+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-08 81차 재검증)

> **81차 재검증 (01:35) — test `@4f71543` 불변·58/18 PASS·86 modules·audit 0·develop `c510f5c`(+2 v1.2 CLEAN)·15 ahead·develop 143/46 PASS·PASS**: 80차(develop `95b92b9` +13·PASS) 대비 develop HEAD **`c510f5c`**(+2: `fd4e8f3` feat(ux): US-G06 DISCREPANCY 청구 라인 비교 링크·접근성 재점검 · `c510f5c` test(v1.2): US-G06 DISCREPANCY compare pilotPageFlows E2E). test HEAD `4f71543` **불변** — 58/18 PASS·86 modules·audit 0 유지(독립 실측 CONFIRMED). develop WT **CLEAN** (0 dirty). develop `npm test` **143/46 PASS**·audit **0**. 이관 규율 5 PRESENT · SEC-005 0건. **신규 Open 0건** — 판정 **PASS**(v1.1). backend merge(15) 잔여.

## 커밋 수준 (81차)

| 항목 | 80차 | 81차 |
|------|------|------|
| develop HEAD | `95b92b9` | **`c510f5c`** (+2) |
| test HEAD | `4f71543` (v1.1 merged) | **`4f71543`** (불변) |
| commits gap | develop 13 ahead | **develop 15 ahead** |
| develop WT | CLEAN | **CLEAN** |
| develop tests | 137/45 PASS | **143/46 PASS** |

### v1.2 develop 신규 커밋 (80차 `95b92b9` 이후, 81차)

| SHA | Message |
|-----|---------|
| `fd4e8f3` | feat(ux): US-G06 DISCREPANCY 청구 라인 비교 링크·접근성 재점검 |
| `c510f5c` | test(v1.2): US-G06 DISCREPANCY compare pilotPageFlows E2E |

## test 브랜치 (frontend-test @ `4f71543`, 81차 TSR 독립 실측)

| 항목 | 결과 |
|------|------|
| working tree | **CLEAN** |
| build | **86 modules PASS** (vite 6.4.3, JS 210.46 kB gzip 66.20 kB, CSS 27.27 kB) |
| npm test | **58/18 PASS** (vitest 4.1.8) |
| npm audit | **0 vulnerabilities** |
| 이관 규율 5 | ProtectedRoute·services.js·SideNav·pilotChecklist·liveConfig·AuthContext **PRESENT** |
| SEC-005 | AuthContext localStorage/sessionStorage **0건** |

## develop HEAD (`c510f5c`, 81차 TSR 실측)

| 항목 | 결과 |
|------|------|
| working tree | **CLEAN** |
| npm test | **143/46 PASS** (+6/+1 vs 80차 137/45 — US-G06 DISCREPANCY 회귀) |
| npm audit | **0 vulnerabilities** |

## 판정 (81차)

**PASS** — v1.1 test `@4f71543` 검증 유지. develop v1.2 **+15 CLEAN** (non-blocking). post-merge **live E2E run** 권장(결정 73). backend merge(15) 잔여.

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-08T00:30:00+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-08T00:30 80차 재검증)

> **80차 재검증 (00:30) — test `@4f71543` 불변·58/18 PASS·86 modules·audit 0·develop `95b92b9`(+2 v1.2 CLEAN)·13 ahead·develop 137/45 PASS·124 modules·PASS**: 77차(develop `4957bd3` +11·PASS) 대비 develop HEAD **`95b92b9`**(+2: `3ec8206` feat(uxd-41): US-F03 낙상·사고·특이사항 이벤트 기록 UI 신설 · `95b92b9` fix(v1.2): US-F03 incident API 본문 detail 필드 정합). test HEAD `4f71543` **불변** — 58/18 PASS·86 modules·audit 0 유지(독립 재실측 CONFIRMED). develop WT **CLEAN** (0 dirty). develop `npm test` **137/45 PASS**·build **124 modules**·audit **0**. 이관 규율 5 PRESENT · SEC-005 0건. **신규 Open 0건** — 판정 **PASS**(v1.1). backend merge(14) 잔여.

## 커밋 수준 (80차)

| 항목 | 77차 | 80차 |
|------|------|------|
| develop HEAD | `4957bd3` | **`95b92b9`** (+2) |
| test HEAD | `4f71543` (v1.1 merged) | **`4f71543`** (불변) |
| commits gap | develop 11 ahead | **develop 13 ahead** |
| develop WT | CLEAN | **CLEAN** |
| develop tests | 130/44 PASS | **137/45 PASS** |
| develop modules | 123 modules | **124 modules** |

### v1.2 develop 신규 커밋 (77차 `4957bd3` 이후, 80차)

| SHA | Message |
|-----|---------|
| `3ec8206` | feat(uxd-41): US-F03 낙상·사고·특이사항 이벤트 기록 UI 신설 |
| `95b92b9` | fix(v1.2): US-F03 incident API 본문 detail 필드 정합 (Q154) |

## test 브랜치 (frontend-test @ `4f71543`, 80차 TSR 독립 실측)

| 항목 | 결과 |
|------|------|
| working tree | **CLEAN** |
| build | **86 modules PASS** (vite 6.4.3, JS 210.46 kB gzip 66.20 kB, CSS 27.27 kB) |
| npm test | **58/18 PASS** (vitest 4.1.8) |
| npm audit | **0 vulnerabilities** |
| 이관 규율 5 | ProtectedRoute·services.js·SideNav·pilotChecklist·liveConfig·AuthContext **PRESENT** |
| SEC-005 | AuthContext localStorage/sessionStorage **0건** |

## develop HEAD (`95b92b9`, 80차 TSR 실측)

| 항목 | 결과 |
|------|------|
| working tree | **CLEAN** |
| npm test | **137/45 PASS** (+7/+1 vs 77차 130/44 — US-F03 이벤트 기록 회귀) |
| npm run build | **124 modules PASS** (vite 6.4.3, JS 316.89 kB gzip 90.47 kB, CSS 30.85 kB) |
| npm audit | **0 vulnerabilities** |

## 판정 (80차)

**PASS** — v1.1 test `@4f71543` 검증 유지. develop v1.2 **+13 CLEAN** (non-blocking). post-merge **live E2E run** 권장(결정 73). backend merge(14) 잔여.

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-07T23:30:00+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-07T23:30 77차 재검증)

> **77차 재검증 (23:30) — test `@4f71543` 불변·58/18 PASS·86 modules·audit 0·develop `4957bd3`(+2 v1.2 CLEAN)·11 ahead·develop 130/44 PASS·123 modules·PASS**: 76차(develop `c5708c7` +9·PASS) 대비 develop HEAD **`4957bd3`**(+2: `9863312` feat(uxd-40): US-F01 활력징후 비정상 범위 입력 경고·정상 범위 단일 원천 · `4957bd3` fix(v1.2): FAQ Q154 건강·NHIS API 본문 정합). test HEAD `4f71543` **불변** — 58/18 PASS·86 modules·audit 0 유지(독립 재실측 CONFIRMED). develop WT **CLEAN** (0 dirty). develop `npm test` **130/44 PASS**·build **123 modules**·audit **0**. 이관 규율 5 PRESENT · SEC-005 0건. **신규 Open 0건** — 판정 **PASS**(v1.1). backend merge(13) 잔여.

## 커밋 수준 (77차)

| 항목 | 76차 | 77차 |
|------|------|------|
| develop HEAD | `c5708c7` | **`4957bd3`** (+2) |
| test HEAD | `4f71543` (v1.1 merged) | **`4f71543`** (불변) |
| commits gap | develop 9 ahead | **develop 11 ahead** |
| develop WT | CLEAN | **CLEAN** |
| develop tests | 115/40 PASS | **130/44 PASS** |
| develop modules | 120 modules | **123 modules** |

### v1.2 develop 신규 커밋 (76차 `c5708c7` 이후, 77차)

| SHA | Message |
|-----|---------|
| `9863312` | feat(uxd-40): US-F01 활력징후 비정상 범위 입력 경고·정상 범위 단일 원천 |
| `4957bd3` | fix(v1.2): FAQ Q154 건강·NHIS API 본문 정합 |

> **`c5708c7..4957bd3` diff stat**: 15 files, +572/-75 — 신규 `src/utils/vitalsRanges.js`(+test)·`src/utils/healthRecords.js`(+test) (활력징후 정상 범위 단일 원천·비정상 경고) + `VitalsRecordForm.jsx`·`HealthPage`/`HealthDetailPage` 등 연동.

## test 브랜치 (frontend-test @ `4f71543`, 77차 TSR 독립 실측)

| 항목 | 결과 |
|------|------|
| working tree | **CLEAN** |
| build | **86 modules PASS** (vite 6.4.3, JS 210.46 kB gzip 66.20 kB, CSS 27.27 kB) |
| npm test | **58/18 PASS** (vitest 4.1.8) |
| npm audit | **0 vulnerabilities** |
| 이관 규율 5 | ProtectedRoute·services.js·SideNav·pilotChecklist·liveConfig·AuthContext **PRESENT** |
| SEC-005 | AuthContext localStorage/sessionStorage **0건** |

## develop HEAD (`4957bd3`, 77차 TSR 실측)

| 항목 | 결과 |
|------|------|
| working tree | **CLEAN** |
| npm test | **130/44 PASS** (+15/+4 vs 76차 115/40 — vitalsRanges·healthRecords 회귀) |
| npm run build | **123 modules PASS** (vite 6.4.3, JS 313.51 kB gzip 89.67 kB, CSS 30.85 kB) |
| npm audit | **0 vulnerabilities** |

## 판정 (77차)

**PASS** — v1.1 test `@4f71543` 검증 유지. develop v1.2 **+11 CLEAN** (non-blocking). post-merge **live E2E run** 권장(결정 73). backend merge(13) 잔여.

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-07T22:27:00+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-07T22:27 76차 재검증)

> **76차 재검증 (22:27) — test `@4f71543` 불변·58/18 PASS·86 modules·audit 0·develop `c5708c7`(+1 v1.2 CLEAN)·9 ahead·develop 115/40 PASS·120 modules·PASS**: 75차(develop `a627c6d` +8·PASS) 대비 develop HEAD **`c5708c7`**(+1: `feat(uxd-39): Must 흐름 UI 보강 — guardian/checkin·건강·NHIS·접근성`). test HEAD `4f71543` **불변** — 58/18 PASS·86 modules·audit 0 유지(독립 재실측 CONFIRMED). develop WT **CLEAN** (0 dirty). develop `npm test` **115/40 PASS**·build **120 modules**·audit **0**. 이관 규율 5 PRESENT · SEC-005 0건. **신규 Open 0건** — 판정 **PASS**(v1.1). backend merge(12) 잔여.

## 커밋 수준 (76차)

| 항목 | 75차 | 76차 |
|------|------|------|
| develop HEAD | `a627c6d` | **`c5708c7`** (+1) |
| test HEAD | `4f71543` (v1.1 merged) | **`4f71543`** (불변) |
| commits gap | develop 8 ahead | **develop 9 ahead** |
| develop WT | CLEAN | **CLEAN** |
| develop tests | 110/36 PASS | **115/40 PASS** |
| develop modules | 117 modules | **120 modules** |

### v1.2 develop 신규 커밋 (75차 `a627c6d` 이후, 76차)

| SHA | Message |
|-----|---------|
| `c5708c7` | feat(uxd-39): Must 흐름 UI 보강 — guardian/checkin·건강·NHIS·접근성 |

> **`a627c6d..c5708c7` diff stat**: 17 files, +748/-91 — `MedicationRecordForm.jsx`(+test)·`VitalsRecordForm.jsx`·`NhisReconciliationTable.jsx`(+test)·`MedicationDuplicateAlert.jsx`(+test)·`HealthPage.jsx`·`HealthDetailPage.jsx`(+test)·`ReconciliationPage.jsx`·`GuardianPortalPage.jsx`·`navConfig.js`·`components.css`.

## test 브랜치 (frontend-test @ `4f71543`, 76차 TSR 독립 실측)

| 항목 | 결과 |
|------|------|
| working tree | **CLEAN** |
| build | **86 modules PASS** (vite 6.4.3, JS 210.46 kB gzip 66.20 kB, CSS 27.27 kB) |
| npm test | **58/18 PASS** (vitest 4.1.8) |
| npm audit | **0 vulnerabilities** |
| 이관 규율 5 | ProtectedRoute·services.js·SideNav·pilotChecklist·liveConfig·AuthContext **PRESENT** |
| SEC-005 | AuthContext localStorage/sessionStorage **0건** |

## 판정 (76차)

**PASS** — v1.1 test `@4f71543` 검증 유지. develop v1.2 **+9 CLEAN** (non-blocking). post-merge **live E2E run** 권장(결정 73). backend merge(12) 잔여.

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-07T21:24:00+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-07T21:24 75차 재검증)

> **75차 재검증 (21:24) — test `@4f71543` 불변·58/18 PASS·86 modules·audit 0·develop `a627c6d`(+2 v1.2 CLEAN)·8 ahead·develop 110/36 PASS·117 modules·PASS**: 73차(develop `9bdf59f` +6·PASS) 대비 develop HEAD **`a627c6d`**(+2: `6f3f746` 수기 출석 체크인/아웃·결석 흐름(US-E01·E02) · `a627c6d` US-E03 QR 저장·US-E05 출석 통계 API 통합). test HEAD `4f71543` **불변** — 58/18 PASS·86 modules·audit 0 유지(독립 재실측 CONFIRMED). develop WT **CLEAN** (0 dirty). develop `npm test` **110/36 PASS**·build **117 modules**·audit **0**. 이관 규율 5 PRESENT · SEC-005 0건. **신규 Open 0건** — 판정 **PASS**(v1.1). backend merge(11) 잔여.

## 커밋 수준 (75차)

| 항목 | 73차 | 75차 |
|------|------|------|
| develop HEAD | `9bdf59f` | **`a627c6d`** (+2) |
| test HEAD | `4f71543` (v1.1 merged) | **`4f71543`** (불변) |
| commits gap | develop 6 ahead | **develop 8 ahead** |
| develop WT | CLEAN | **CLEAN** |
| develop tests | (73차 미재실행) | **110/36 PASS** |
| develop modules | — | **117 modules** |

### v1.2 develop 신규 커밋 (73차 `9bdf59f` 이후, 75차)

| SHA | Message |
|-----|---------|
| `6f3f746` | feat(ux): 수기 출석 체크인/아웃·결석 흐름 보강 (US-E01·E02) |
| `a627c6d` | feat(v1.2): US-E03 QR 저장·US-E05 출석 통계 API 통합 |

> **`9bdf59f..a627c6d` diff stat**: 14 files, +767/-47 — `services.js`(+18)·`AttendanceAbsentModal.jsx`(+test)·`CheckoutModal.jsx`(+test)·`AttendancePage.jsx`(+243)(+test)·`AttendanceStatsPage.jsx`(+test)·`QrGeneratePage.jsx`(+test)·`utils/downloadDataUrl.js`(+test)·`components/ui/index.js`.

## test 브랜치 (frontend-test @ `4f71543`, 75차 TSR 독립 실측)

| 항목 | 결과 |
|------|------|
| working tree | **CLEAN** |
| build | **86 modules PASS** (vite 6.4.3, JS 210.46 kB gzip 66.20 kB, CSS 27.27 kB) |
| npm test | **58/18 PASS** (vitest 4.1.8) |
| npm audit | **0 vulnerabilities** |
| 이관 규율 5 | ProtectedRoute·services.js·SideNav·pilotChecklist·liveConfig·AuthContext **PRESENT** |
| SEC-005 | AuthContext localStorage/sessionStorage **0건** |

## 판정 (75차)

**PASS** — v1.1 test `@4f71543` 검증 유지. develop v1.2 **+8 CLEAN** (non-blocking). post-merge **live E2E run** 권장(결정 73). backend merge(11) 잔여.

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-07T20:21:00+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-07T20:21 73차 재검증)

> **73차 재검증 (20:21) — test `@4f71543` 불변·58/18 PASS·86 modules·audit 0·develop `9bdf59f`(+2 v1.2 CLEAN)·6 ahead·PASS**: 71차(develop `42f48e1` +4·PASS) 대비 develop HEAD **`9bdf59f`**(+2: `a68f150` GuardianCheckinPage DS FilterChips(US-E04) · `9bdf59f` P0 CRUD E2E·입금 모달·보호자 초대/수정 수정). test HEAD `4f71543` **불변** — 58/18 PASS 유지. develop WT **CLEAN** (0 dirty). 이관 규율 5 PRESENT · SEC-005 0건. **신규 Open 0건** — 판정 **PASS**(v1.1). backend merge(10) 잔여.

## 커밋 수준 (73차)

| 항목 | 71차 | 73차 |
|------|------|------|
| develop HEAD | `42f48e1` | **`9bdf59f`** (+2) |
| test HEAD | `4f71543` (v1.1 merged) | **`4f71543`** (불변) |
| commits gap | develop 4 ahead | **develop 6 ahead** |
| develop WT | CLEAN | **CLEAN** |

### v1.2 develop 신규 커밋 (71차 `42f48e1` 이후, 73차)

| SHA | Message |
|-----|---------|
| `a68f150` | fix(ux): GuardianCheckinPage 체크인 유형 DS FilterChips 전환 (US-E04) |
| `9bdf59f` | feat(v1.2): P0 CRUD E2E·입금 모달·보호자 초대/수정 수정 |

## test 브랜치 (frontend-test @ `4f71543`, 73차 TSR 독립 실측)

| 항목 | 결과 |
|------|------|
| working tree | **CLEAN** |
| build | **86 modules PASS** (vite 6.4.3, JS 210.46 kB gzip 66.20 kB, CSS 27.27 kB) |
| npm test | **58/18 PASS** (vitest 4.1.8) |
| npm audit | **0 vulnerabilities** |
| 이관 규율 5 | ProtectedRoute·services.js·SideNav·pilotChecklist·FE-22 **PRESENT** |
| SEC-005 | AuthContext localStorage/sessionStorage **0건** |

## 판정 (73차)

**PASS** — v1.1 test `@4f71543` 검증 유지. develop v1.2 **+6 CLEAN** (non-blocking). post-merge **live E2E run** 권장(결정 73). backend merge(10) 잔여.

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-07T19:20:00+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-07T19:20 71차 재검증)

> **71차 재검증 (19:20) — test `@4f71543` 불변·58/18 PASS·86 modules·audit 0·develop `42f48e1`(+4 v1.2)·89/28 PASS·114 modules·PASS**: 69차(develop `e0eaf32` +2·82/27·PASS) 대비 develop HEAD **`42f48e1`**(+2: `0d83a42` UXD 15 missing pages · `42f48e1` P0 page-flow tests·module coverage KPI). test HEAD `4f71543` **불변** — PASS 유지. develop WT **CLEAN**. develop 89/28 PASS·114 modules·audit 0. **신규 Open 0건** — 판정 **PASS**(v1.1).

## 커밋 수준 (71차)

| 항목 | 69차 | 71차 |
|------|------|------|
| develop HEAD | `e0eaf32` | **`42f48e1`** (+2) |
| test HEAD | `4f71543` (v1.1 merged) | **`4f71543`** (불변) |
| commits gap | develop 2 ahead | **develop 4 ahead** |
| develop tests | 82/27 PASS | **89/28 PASS** |
| develop modules | (not re-run 69차) | **114 modules** |

### v1.2 develop 선행 커밋 (test `4f71543` 이후, 71차 기준)

| SHA | Message |
|-----|---------|
| `64468a3` | feat(ux): v1.2 P0 UI components, SideNav menus, Must page DS integration (UXD 35) |
| `e0eaf32` | fix(v1.2): align guardians route RBAC and extend page-flow regression tests |
| `0d83a42` | feat(ux): implement 15 missing page screens (US-D01, E03-E05, F04, G01-G07, H01-H04, B01, A01) |
| `42f48e1` | fix(v1.2): P0 page-flow tests, module coverage KPI, title alignment |

## test 브랜치 (frontend-test @ `4f71543`, 71차 TSR 실측)

| 항목 | 결과 |
|------|------|
| working tree | **CLEAN** |
| build | **86 modules PASS** (vite 6.4.3, JS 210.46 kB gzip 66.20 kB, CSS 27.27 kB) |
| npm test | **58/18 PASS** (vitest 4.1.8) |
| npm audit | **0 vulnerabilities** |
| 이관 규율 5 | ProtectedRoute·services.js·SideNav·pilotChecklist·FE-22 **PRESENT** |
| SEC-005 | AuthContext localStorage/sessionStorage **0건** |

## develop HEAD (`42f48e1`, 71차 TSR 실측)

| 항목 | 결과 |
|------|------|
| working tree | **CLEAN** |
| npm test | **89/28 PASS** (+7/+1 vs 69차 82/27) |
| npm run build | **114 modules PASS** (vite 6.4.3, JS 295.02 kB gzip 84.80 kB, CSS 30.23 kB) |
| npm audit | **0 vulnerabilities** |
| 이관 규율 5 | ProtectedRoute·services.js·SideNav·pilotChecklist·liveConfig·AuthContext **PRESENT** |
| SEC-005 | AuthContext localStorage/sessionStorage **0건** |

## 판정 (71차)

**PASS** — v1.1 test `@4f71543` 검증 유지. develop v1.2 **+4 CLEAN** (non-blocking). post-merge **live E2E run** 권장(결정 73). backend merge(9) 잔여.

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-07T18:12:00+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-07T18:12 69차 재검증)

> **69차 재검증 (18:12) — v1.1 merge 완료·test `@4f71543`·58/18 PASS·86 modules·audit 0·develop +2(v1.2)·PASS**: 67차(develop 13 ahead·test `e5fd48d` stale·BLOCK) 대비 **develop→test merge 실행** — test HEAD **`4f71543`**. `src/frontend-test` `npm ci`+`npm test` **58/18 PASS**·build **86 modules**·audit **0**. develop HEAD **`e0eaf32`**(+2 v1.2: `64468a3` UXD 35 P0 UI · `e0eaf32` guardians RBAC) · WT **CLEAN** · develop `npm test` **82/27 PASS**. **ROADMAP v1.1 `merge_status: merged`**. **Open 0**. 판정 **PASS**(v1.1).

## 커밋 수준 (69차)

| 항목 | 67차 | 69차 |
|------|------|------|
| develop HEAD | `4f71543` | **`e0eaf32`** (+2 v1.2) |
| test HEAD | `e5fd48d` (stale) | **`4f71543`** (v1.1 merged) |
| commits gap | develop 13 ahead | **develop 2 ahead** (v1.2 only) |
| ROADMAP merge_status | ready | **merged** |

### v1.2 develop 선행 커밋 (test `4f71543` 이후)

| SHA | Message |
|-----|---------|
| `64468a3` | feat(ux): v1.2 P0 UI components, SideNav menus, Must page DS integration (UXD 35) |
| `e0eaf32` | fix(v1.2): align guardians route RBAC and extend page-flow regression tests |

## test 브랜치 (frontend-test @ `4f71543`, 69차 TSR 실측)

| 항목 | 결과 |
|------|------|
| working tree | **CLEAN** |
| build | **86 modules PASS** (vite 6.4.3, JS 210.46 kB gzip 66.20 kB, CSS 27.27 kB) |
| npm test | **58/18 PASS** (vitest 4.1.8) |
| npm audit | **0 vulnerabilities** |
| 이관 규율 5 | ProtectedRoute·services.js·SideNav·pilotChecklist·FE-22 **PRESENT** |
| SEC-005 | AuthContext localStorage/sessionStorage **0건** |

## develop HEAD (`e0eaf32`, read-only)

| 항목 | 결과 |
|------|------|
| working tree | **CLEAN** |
| npm test | **82/27 PASS** (+24/+9 vs test — v1.2 P0 UI·guardians RBAC 회귀) |

## 판정 (69차)

**PASS** — v1.1 test `@4f71543` 검증 완료. develop v1.2 **+2 CLEAN** (non-blocking). post-merge **live E2E run** 권장(결정 73). backend merge(8) 잔여.

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-07T17:31:00+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-07T17:31 67차 재검증, 이력)

> **67차 재검증 (17:31) — develop `d592a17`→`f64e1dd`→`4f71543`(+2커밋)·UXD SideNav·FE-22 live config preconditions·CLEAN·58/18 PASS·86 modules·develop 13 ahead·ROADMAP merge_status ready·BLOCK(B03/SEC-D14 merge 미실행)**: 65차(`d592a17`·46/13·11 ahead) 대비 develop HEAD **`4f71543`**. develop WT **CLEAN**. develop build **86 modules**·`npm test` **58/18 PASS**·audit **0**. test `@e5fd48d` build **36 PASS**·N/A·**2 moderate**. **Open 0**. 판정 **BLOCK**(merge 게이트 단일 — live E2E run 은 결정 73 post-merge).

## 커밋 수준 (67차)

| 항목 | 65차 | 67차 |
|------|------|------|
| develop HEAD | `d592a17` | **`4f71543`** |
| test HEAD | `e5fd48d` (stale) | **`e5fd48d`** (stale) |
| commits gap | develop 11 ahead | **develop 13 ahead** |
| ROADMAP merge_status | ready (48차) | **ready** (변경 없음) |

### develop 신규 커밋 (65차 `d592a17` 이후, 67차)

| SHA | Message |
|-----|---------|
| `f64e1dd` | feat(uxd-33): 2단 SideNav·기반 UI 컴포넌트·AppShell 접근성 보강 |
| `4f71543` | test(v1.1): enforce FE-22 live E2E config preconditions |

### UXD SideNav (`f64e1dd` — 20 files)

- `src/layout/SideNav.jsx`(+test)·`AppShell.jsx`·`navConfig.js` — 2단 SideNav·역할별 메뉴
- `src/components/ui/` — `BranchSwitcher`·`FilterChips`·`Pagination`·`SearchInput`·`StatCard`·`TabPanel`·`Table`·`Tabs`(+test) 등 기반 UI
- `npm test` **46/13 → 58/18 PASS**(+12/+5 — SideNav·Tabs·FilterChips·BranchSwitcher·LogoutButton 등)

### FE-22 preconditions (`4f71543` — 4 files +35/-11)

- `src/e2e/liveConfig.js` — `LIVE_E2E=1` 시 필수 env(auth/client/guardian) **fail-fast** 검증
- `pilotLiveApi`·`pilotLivePages`·`guardianLiveApi` — skip 대신 precondition assert 로 live run 우회 방지

## develop HEAD (67차 — CLEAN)

| 항목 | 결과 |
|------|------|
| working tree | **0 dirty** |
| build | **86 modules PASS** (vite 6.4.3, JS 210.46 kB gzip 66.20 kB, CSS 27.27 kB) |
| npm test | **58/18 PASS** (vitest 4.1.8, 65차 46/13 → +12/+5) |
| npm audit | **0 vulnerabilities** |
| 이관 규율 5 | Must API·guardian REST·J01/J02·FE-22 harness·SideNav·ProtectedRoute **PRESENT** |
| SEC-005 | AuthContext localStorage/sessionStorage **0건** |

## test 브랜치 (frontend-test, 67차 TSR 실측)

- `npm run build`: **SUCCESS** (36 modules, Vite 5.4.21, JS 165.43 kB)
- `npm test`: **N/A** (Missing script @ e5fd48d)
- `npm audit`: 0 high, **2 moderate**

## 판정 (67차)

**BLOCK** — **B03/SEC-D14 develop→test merge 미실행**(13 commits · ROADMAP `merge_status: ready`). develop 품질 **58/18 PASS**·CLEAN·audit **0** — **merge 후 test 재검증 전 PASS 불가**. Must·J01/J02 **live E2E run**은 결정 73 **post-merge 권장**(harness + precondition @ `4f71543` develop HEAD PRESENT).

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-07T16:50:00+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-07T16:50 65차 재검증, 이력)

> **65차 재검증 (16:50) — develop `bb0cec4`→`d592a17`(+3커밋)·guardian REST+J01/J02·tone Alert a11y·FE-22 live E2E harness·CLEAN·46/13 PASS·develop 11 ahead·BLOCK(B03/SEC-D14)**: 63차(`811aef3`/`bb0cec4`·37/9·8 ahead) 대비 develop HEAD **`d592a17`**. develop WT **CLEAN**. develop build **75 modules**·`npm test` **46/13 PASS**·audit **0**. test `@e5fd48d` build **36 PASS**·N/A·**2 moderate**. **Open 0**. 판정 **BLOCK**.

## 커밋 수준 (65차)

| 항목 | 63차 | 65차 |
|------|------|------|
| develop HEAD | `bb0cec4` | **`d592a17`** |
| test HEAD | `e5fd48d` (stale) | **`e5fd48d`** (stale) |
| commits gap | develop 8 ahead | **develop 11 ahead** |
| baseline ref | `c3b863e` + 2 | **`7170b2a` + 2** (workspace_baseline 갱신 예정) |

### develop 신규 커밋 (63차 `bb0cec4` 이후, 65차)

| SHA | Message |
|-----|---------|
| `7170b2a` | feat(v1.1): wire guardian portal to REST APIs and J01/J02 tests |
| `449cd4f` | fix(ux): tone-based Alert live region + PublicAuthLayout h1/skip-link (US-J01) |
| `d592a17` | feat(v1.1): FE-22 live E2E harness for Must P1–P8 and J01/J02 APIs |

### FE-22 live E2E harness (`d592a17` — 10 files +369/-4)

- `src/e2e/pilotLiveApi.e2e.test.js`(109) · `src/e2e/pilotLivePages.e2e.test.jsx`(84) · `src/e2e/guardianLiveApi.e2e.test.js`(45)
- `src/e2e/liveConfig.js`(37) · `src/e2e/liveSession.js`(67) · `src/e2e/liveAuthStub.js`(6)
- `vitest.live.config.js`(13) · `package.json`(`test:live-e2e` script) · `src/api/http.js` · `vite.config.js`(test `exclude: src/e2e/**`)
- **게이팅**: `LIVE_E2E=1` + 자격증명(`LIVE_E2E_ACCESS_TOKEN` 또는 `LIVE_E2E_EMAIL`/`PASSWORD`) + `VITE_API_BASE`(default `http://127.0.0.1:8080`). 기본 `npm test` 에서 제외 → 회귀 안정성 유지. 실제 live run 은 develop→test merge·backend v1 test 승격(SEC-D14) 후.

## develop HEAD (65차 — CLEAN)

| 항목 | 결과 |
|------|------|
| working tree | **0 dirty** |
| build | **75 modules PASS** (vite 6.4.3, JS 209.19 kB) |
| npm test | **46/13 PASS** (vitest 4.1.8, 63차 37/9 → +9/+4) |
| npm audit | **0 vulnerabilities** |
| 이관 규율 5 | guardian REST·J01/J02·Alert a11y·FE-22 e2e harness·ProtectedRoute **PRESENT** |
| SEC-005 | AuthContext localStorage/sessionStorage **0건** |

## test 브랜치 (frontend-test, 65차 TSR 실측)

- `npm run build`: **SUCCESS** (36 modules, Vite 5.4.21, JS 165.43 kB)
- `npm test`: **N/A** (Missing script @ e5fd48d)
- `npm audit`: 0 high, **2 moderate**

## 판정 (65차)

**BLOCK** — **B03/SEC-D14 merge 게이트** + Must·J01/J02 라이브 E2E **run** 미실행(harness 는 develop HEAD PRESENT, backend merge·LIVE_E2E 후 실행). develop 품질 **46/13 PASS**·CLEAN — **이관 PASS 아님**(merge·ROADMAP 게이트).

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-07T15:00:00+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-07T15:00 61차 재검증, 이력)

> **61차 재검증 (15:00) — baseline 43차 +2커밋·develop CLEAN·6/6 PASS·test stale·3 ahead·BLOCK(B03)**: 59차(`e5fd48d` skeleton·WT DIRTY) 대비 develop HEAD **`7c0ecdc`→`e043eac`**(+3 commits vs test). develop WT **CLEAN**. develop build **65 modules**·`npm test` **6/6 PASS**·audit **4 vuln**. test `@e5fd48d` build **36 PASS**·N/A·**2 moderate**. **Open 0**. 판정 **BLOCK**.

## 커밋 수준 (61차)

| 항목 | 59차 workspace | 61차 workspace |
|------|----------------|----------------|
| develop HEAD | `e5fd48d` (스켈레톤) | **`e043eac`** (MVP + tests) |
| test HEAD | `e5fd48d` | **`e5fd48d`** (stale) |
| commits gap | 0 | **develop 3 ahead** |
| baseline ref | TSR57 `d5654c0` 불일치 | **43차 `7c0ecdc` + 2** |

### develop commits ahead of test (61차)

| SHA | Message |
|-----|---------|
| `7c0ecdc` | feat(frontend): JWT 로그인·앱 셸·MVP 라우트 복구 |
| `1d9a701` | test(v1.1): add route guard and phone masking regression tests |
| `e043eac` | test(v1.1): restore vitest test runner dependencies |

## develop HEAD (61차 — CLEAN)

| 항목 | 결과 |
|------|------|
| working tree | **0 dirty** |
| build | **65 modules PASS** |
| npm test | **6/6 PASS** (ProtectedRoute 3 · MaskedPhone 3) |
| npm audit | **4 vuln** (3 moderate · 1 critical — SEC-008 잔여) |
| SEC-D12 | **PASS** — ProtectedRoute @ HEAD |

## test 브랜치 (frontend-test, 61차 TSR 실측)

- `npm ci` + `npm run build`: **SUCCESS** (36 modules, Vite 5.4.21, JS 165.43 kB)
- `npm test`: **N/A** (Missing script @ e5fd48d)
- `npm audit`: 0 high, **2 moderate**

## 판정 (61차)

**BLOCK** — **B03 merge 게이트** + v1.1 완료 기준(Must API·E2E·J01·SEC-008) 미충족. develop 품질 **6/6 PASS**·CLEAN — **이관 PASS 아님**(merge·ROADMAP 게이트).

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-08T02:05:00+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-08T02:05 59차 재검증, 이력)

> **59차 재검증 (02:05) — workspace baseline 단절·develop=test @e5fd48d·TSR57 재현 불가·SEC-D12·신규 QA-B11·BLOCK**: TSR57(10:11) 대비 workspace **전면 불일치** — develop HEAD **`d5654c0` → `e5fd48d`**, test **`e5fd48d` 동일**(18 behind → **0 ahead**). develop WT **DIRTY 11 entries**(partial auth WIP). HEAD `App.jsx` **무방비**(SEC-D12). test `npm run build` **36 modules PASS**·`npm test` **N/A**·audit **2 moderate**. **신규 Open QA-B11**. 판정 **BLOCK**.

## 커밋 수준 (59차)

| 항목 | TSR57 baseline | 59차 workspace |
|------|----------------|----------------|
| develop HEAD | `d5654c0` (18 ahead) | **`e5fd48d`** (스켈레톤) |
| test HEAD | `e5fd48d` (18 behind) | **`e5fd48d`** (동일) |
| commits gap | 18 | **0** |

## develop working tree (59차)

| 항목 | TSR57 | 59차 |
|------|-------|------|
| total dirty | 20 (B07 #6) | **11** |
| WT build | 758 modules | **N/A** (vitest·v1.1 deps 부재) |
| WT npm test | 209/210 FAIL (H05) | **N/A** |
| HEAD ProtectedRoute | PRESENT @ d5654c0 | **ABSENT** (WT only) |

**WT 범위**: 6 modified(`index.html`·`App.jsx`·`main.jsx`·`DashboardPage`·`LoginPage`·`styles.css`) + 5 untracked(`src/auth/`·`src/components/`·`ForbiddenPage.jsx`·`src/styles/`·`theme.js`).

## test 브랜치 (frontend-test, 59차 TSR 실측)

- `npm ci` + `npm run build`: **SUCCESS** (36 modules, Vite 5.4.21, JS 165.43 kB)
- `npm test`: **N/A** (Missing script @ e5fd48d)
- `npm audit`: 0 high, **2 moderate** (esbuild/vite dev chain)

## 판정 (59차)

**BLOCK** — **QA-B11**(baseline 단절) + **SEC-D12**(HEAD 무방비) + develop WT **DIRTY**(미커밋 auth WIP). TSR57 Planned(B03·B07 #6·H05) **workspace에서 재검증 불가**. 선행: submodule checkout `d5654c0` 또는 planner baseline 갱신.

---
