<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-07T00:43:00+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-07T00:43 31차 재검증)

> **31차 재검증 (00:43) — COD `3fdc266` P1–P8 페이지 단위 E2E·UXD 14차 `a42d6fb`·140/11 PASS·merge 게이트 단일**: develop HEAD `57ff3c0`→`a42d6fb`→**`3fdc266`**(+2커밋, **14 ahead**, working tree **CLEAN**). ① UXD 14차: `FeeRateHistoryPanel`·`chartColors.js`·`BATCH_STATUS`. ② COD: `pilotPageFlows.test.jsx`(433 lines — 8 Must 페이지 RTL E2E). HEAD build **113 modules PASS**·`npm test` **140/11 PASS**(+10/+1)·`npm audit` **0건**. test `@e5fd48d` 불변(stale, 14 behind). 이관 규율 5 PASS. 잔여 BLOCK = **merge 게이트(B03·B05) 단일**.

> **28차 재검증 (23:19) — UXD 13차 `07fd305`·working tree CLEAN·37/8 PASS·merge 게이트 단일**: develop HEAD `cc34f23`→**`07fd305`**(+1커밋 UXD 13차 `feat(ux): 전사 설정 Switch 컴포넌트·셀프 체크인 토글`, **11커밋 ahead**, working tree **CLEAN**). Switch.jsx·Switch.test.jsx(5건)·SettingsPage.jsx. HEAD build **112 modules PASS**(vite 6.4.3, JS 314.56 kB gzip 92.06)·`npm test` **37/8 PASS**(+5/+1 vs 27차 32/7, FE-7 회귀 없음)·`npm audit` **0건**. test `@e5fd48d` 불변(stale, 11 behind). 이관 규율 5 — HEAD `07fd305` Fixed 산출물 PRESENT 유효. 잔여 BLOCK = **merge 게이트(B03·B05) 단일**.

> **27차 재검증 (22:40) — COD 19차 `cc34f23` 파일럿 P1–P8·J01/J02 Must API 라우팅 자동화·working tree CLEAN 유지·merge 게이트 단일(B03·B05) 잔존**: develop HEAD **전진** `404a30e`→**`cc34f23`**(+1커밋 COD 19차, origin/develop 대비 **10 ahead**), test HEAD **불변**(`e5fd48d`). `test(v1.1): 파일럿 P1–P8·J01/J02 Must API JWT 라우팅 자동화`(3 files +396) — `src/api/pilotChecklist.js`(211: USER_STORIES §13 P1–P8 시나리오를 `services.js` 경로 매핑)·`pilotChecklist.test.js`(104: Vitest fetch mock JWT·메서드·경로 검증)·`GuardianInviteModal.test.jsx`(81: 보호자 초대 UI 회귀 4건). 이관 규율 5 — `git cat-file -e HEAD:` `pilotChecklist.js/.test.js`·`GuardianInviteModal.test.jsx` + 기존 Fixed 산출물 **PRESENT**. develop HEAD(clean) `npm run build` **111 modules PASS**(vite 6.4.3, JS 313.68 kB gzip 91.78)·`npm test`(vitest 4.1.8) **13/5 → 32/7 PASS**(+19 tests/+2 files)·`npm audit` **0 vulnerabilities**. test `@e5fd48d` build 36 PASS·npm test N/A·audit 0 high·2 moderate(stale). **잔여 BLOCK = merge 게이트 단일(B03·B05)** — 불변. **R-05 Must API·R-07 J01/J02 라우팅 fetch-mock 자동화 진전**(라이브 E2E·J01 백엔드 API 잔여). 판정 **BLOCK**.

> **26차 재검증 (22:20)**: develop HEAD `ed1bf22`→`404a30e`(UXD 12차 LoginPage DS·Modal 포커스 트랩·고대비), working tree CLEAN. HEAD build 111·npm test 13/5 PASS·audit 0. 판정 BLOCK(B03·B05). (이력)

> **25차 재검증 (21:32) — COD 17차 B07 recurrence #2·SEC-008 Fixed·working tree CLEAN 회복·merge 게이트 단일(B03·B05) 잔존**: develop HEAD **전진** `2d742b3`→`a84473f`→**`ed1bf22`**(+2커밋 COD 17차, origin/develop 대비 **8 ahead**), test HEAD **불변**(`e5fd48d`). ① `a84473f feat(v1.2-p0): 대시보드 실데이터 위젯·Must 페이지 API 보강 (US-M02)`(8 files +636/-170) — 23·24차 미커밋이던 대시보드 실데이터 WIP 8 files **일괄 커밋** → develop working tree **DIRTY 8 files → CLEAN**, **QA-B07 recurrence #2 정식 Fixed**. ② `ed1bf22 fix(security): vite 6·vitest 4·esbuild override`(`package.json`+`package-lock.json` +390/-303) — vite `^6.4.3`·vitest `^4.1.8`·`overrides.esbuild ^0.25.0` → develop **`npm audit` 0 vulnerabilities**(24차 5 vuln/1 critical → 0), **SEC-008 정식 Fixed**. 이관 규율 5 — HEAD `ed1bf22` Fixed 산출물(api·routeAccess·AuthContext localStorage 0건·favicon·ThemeToggle·tokens.css·**dashboardWidgets.js/.test.js 신규 커밋**) **PRESENT**. develop HEAD `npm run build` **111 modules PASS**(vite 6.4.3, JS 313.14 kB gzip 91.58)·`npm test`(vitest 4.1.8) **13/5 PASS**. test `@e5fd48d` build 36 PASS·npm test N/A·audit 0 high·2 moderate(stale). **잔여 BLOCK = merge 게이트 단일(B03·B05)** — dirty-tree·SEC-008 사유 **소멸**. 판정 **BLOCK**.

> **24차 재검증 (21:13)**: develop HEAD `5656e19`→`2d742b3`(UXD 11차 dark mode), working tree DIRTY 8 files(B07 recurrence #2). npm audit 5 vuln(1 critical) → SEC-008 Open. WT build 114·npm test 13/5 PASS. 판정 BLOCK. (이력)
> **23차 재검증 (20:17)**: develop HEAD `5656e19`(UXD 10차), DIRTY 8 files, B07 recurrence #2 Open. WT build 112·npm test 13/5 PASS. 판정 BLOCK. (이력)
> **21차 재검증 (19:22) — B07 recurrence Fixed·working tree CLEAN**: develop `998ac87`→`a72e249`→`3fc549a`(4 ahead), working tree CLEAN. HEAD build 110·npm test 10/4 PASS. 판정 BLOCK(B03·B05). (이력)

## 커밋 수준

- `develop` HEAD: `3fdc266` — test(v1.1): P1–P8·J01/J02 Must 화면 페이지 단위 E2E 자동화 (1 file +433) (origin/develop 대비 ahead **14**)
  - 직전 `a42d6fb` — feat(ux/14차): BATCH_STATUS·FeeRateHistoryPanel·Recharts 차트 토큰 (8 files +335/-8)
  - 직전 `57ff3c0` — test(v1.1): 7역할 JWT 로그인·라우트 가드 E2E 자동화 (COD 20차)
  - 직전 `cc34f23` — test(v1.1): 파일럿 P1–P8·J01/J02 Must API JWT 라우팅 자동화 (COD 19차, 3 files +396) (origin/develop 대비 ahead **10**)
  - 직전 `404a30e` — feat(ux): 로그인 화면 스타일·Modal 포커스 트랩·고대비 모드 (UXD 12차, 3 files +183/-28)
  - 직전 `ed1bf22` — fix(security): vite 6·vitest 4·esbuild override (SEC-008, COD 17차)
  - 직전 `a84473f` — feat(v1.2-p0): 대시보드 실데이터 위젯·Must 페이지 API 보강 (US-M02, 8 files +636/-170)
  - 직전 `2d742b3` — feat(ux): 다크 모드 토큰·ThemeToggle 추가 (UXD 11차)
  - 직전 `5656e19` — feat(ux): 이용자 본인 계정 발급 필드·CopayTypeSelect·브랜드색 (UXD 10차)
  - 직전 `3fc549a` — feat(v1.1): ClientDetailPage 건강·출석 탭 API 연동 (US-D03)
  - 직전 `a72e249` — feat(v1.2-p0): 보호자·입금·미납·2단 SideNav·routeAccess 중앙화 (42 files +3863/-311)
  - 직전 `998ac87` — feat(v1.1): API client layer, memory JWT session, Vitest, favicon
- `test` HEAD: `e5fd48d` — feat: React Vite SPA 초기 스켈레톤
- **test 브랜치는 develop보다 stale** — develop이 test 대비 **14 commits ahead** (v1.1 + v1.2 P0 + UXD 10~14차 + US-M02 + SEC-008 + P1–P8 라우팅·페이지 E2E + 7역할 JWT E2E 미머지)

## develop working tree (QA-B07 — 25차 recurrence #2 Fixed, 26·27차 CLEAN 유지)

| 항목 | 21차 | 23차 | 24차 | 25차 | 26차 | 27차 |
|------|------|------|------|------|------|------|
| modified | **0** | 6 | 6 | **0** | **0** | **0** |
| untracked | **0** | 2 | 2 | **0** | **0** | **0** |
| total | **0 (CLEAN)** | 8 (DIRTY) | 8 (DIRTY) | **0 (CLEAN)** | **0 (CLEAN)** | **0 (CLEAN)** |
| build | PASS(110) | PASS(112) | PASS(114) | PASS(111) | PASS(111) | **PASS(111)** |
| npm test | PASS(10/4) | PASS(13/5) | PASS(13/5) | PASS(13/5) | PASS(13/5) | **PASS(32/7)** |
| npm audit | — | 0h·2mod | 5 vuln(1 crit) | **0 vuln** | **0 vuln** | **0 vuln** |

**27차**: COD 19차 `cc34f23`(pilotChecklist.js/.test.js·GuardianInviteModal.test.jsx, +396) 커밋 — working tree CLEAN 유지, `npm test` 13/5 → **32/7 PASS**(+19 tests/+2 files). P1–P8·J01/J02 Must API JWT 라우팅 fetch-mock 자동화. build·audit 회귀 없음. 이관 규율 5·6·7 PASS.

> **⚠ 범위 관측**: v1.2 P0(`a72e249`·`a84473f`) + UXD 10·11·12차(`5656e19`·`2d742b3`·`404a30e`) + COD 19차(`cc34f23`)가 v1.1 merge 전 develop 선행 커밋(10 ahead). 전부 develop 커밋 완료 — v1.1 develop→test merge 시 동반 흡수(결정 52). 미커밋 WIP 없음.

## develop HEAD(커밋) Fixed 정합 — 이관 규율 5·6

`git cat-file -e HEAD:<path>` @ `cc34f23`:

| 산출물 | develop HEAD `cc34f23` | 판정 |
|--------|------------------------|------|
| `src/api/pilotChecklist.js`·`pilotChecklist.test.js`·`GuardianInviteModal.test.jsx` (`cc34f23`) | PRESENT | COD 19차 P1–P8 라우팅 자동화 **PASS** |
| `src/pages/LoginPage.jsx`·`src/components/ui/Modal.jsx`·`components.css` (`404a30e`) | PRESENT | UXD 12차 DS·포커스 트랩·고대비 **PASS** |
| `src/components/ProtectedRoute.jsx` + `src/App.jsx` 7역할 가드 | PRESENT | H03·SEC-003 **PASS** |
| `src/api/http.js` · `src/api/services.js` | PRESENT | H04 **PASS** |
| `src/auth/AuthContext.jsx` 메모리 세션 (localStorage/sessionStorage 0건) | PRESENT | SEC-005 **PASS** |
| `package.json` `"test":"vitest run"` (vitest 4.1.8) · `*.test.jsx`×4 | PRESENT | M01 **PASS** |
| `public/favicon.*` + `index.html` | PRESENT | US-UX-01 **PASS** |
| `src/auth/routeAccess.js` 중앙 가드 (`a72e249`) | PRESENT | v1.2 P0 **PASS** |
| `src/components/ui/ThemeToggle.jsx`·`src/styles/tokens.css` (`2d742b3`) | PRESENT | UXD 11차 **PASS** |
| `src/pages/dashboardWidgets.js`·`dashboardWidgets.test.js` (`a84473f`) | PRESENT | US-M02·B07 #2 **PASS** |
| `package.json` vite 6·vitest 4·esbuild override (`ed1bf22`) | PRESENT | SEC-008 **PASS** |
| develop working tree clean | **CLEAN** | B07 **PASS** (recurrence #2 Fixed) |

## 빌드·테스트

### test 브랜치 `e5fd48d` (in `src/frontend-test`)

- `npm run build`: SUCCESS (Vite 5.4.21, **36 modules**, JS 165.43 kB)
- `npm test`: `Missing script: "test"` — N/A
- `npm audit`: 0 high, 2 moderate (vite 5.4.21 stale — SEC-008 fix 미머지)

### develop `cc34f23` HEAD (in `src/frontend`, working tree CLEAN — 27차)

- `npm run build`: **PASS** — 111 modules (vite 6.4.3), JS 313.68 kB (gzip 91.78 kB), CSS 40.90 kB
- `npm test`: **PASS** — **32 passed/7 files** (`pilotChecklist`·`GuardianInviteModal`·`dashboardWidgets` 3·`routeAccess` 4·`ProtectedRoute` 3·`AuthContext` 2·`roleHomePaths` 1)
- `npm audit`: **0 vulnerabilities** (high·all 모두 — SEC-008 Fixed 유지)

## v1.1 잔여 갭 (merge 게이트 단일)

- 선행 v1 backend `merge_status: pending` (B05) — backend B01·SEC-007
- v1.1 완료 기준 **라이브 E2E**(7역할 JWT 로그인·Must API P1–P8)·보호자 초대 J01 백엔드 API 미구현 (B03) — 라우팅 fetch-mock 자동화는 `cc34f23` 완료
- develop→test merge 미실행 — test stale `e5fd48d` (10 commits behind)
- **dirty-tree(B07 recurrence #2)·SEC-008는 COD 17차로 Fixed — 소멸**

## 이관 판정

**BLOCK** — B03·B05 merge 게이트(develop→test merge 미실행)가 **단일** 잔여 사유. HEAD @ `cc34f23` Fixed 산출물 규율 5 **유효**(false Fixed 0건), working tree CLEAN, build 111·test **32/7**·audit 0건 PASS. COD 19차로 P1–P8·J01/J02 라우팅 자동화 커버리지 확대(R-05·R-07 진전). 잔여 BLOCK은 backend v1 승격 + v1.1 **라이브 E2E**·J01 백엔드 API 충족에 의존하는 **프로세스·기능 게이트**(프론트 자동 테스트·품질 갭 아님).
