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
