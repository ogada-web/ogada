<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-08T00:30:00+00:00 -->
# Frontend develop → test 이관 체크리스트

> **스트림**: frontend  
> **develop 브랜치**: `develop` (`src/frontend`)  
> **test 브랜치**: `test` (`src/frontend-test` worktree)  
> **검증 기준**: `docs/planning/ROADMAP.md` v1.1 완료 기준 (선행: v1 `merge_status: merged`) · **CURRENT BASELINE**: frontend test `4f71543` · develop `95b92b9` (+13 v1.2)  
> **작성**: tester (`TSR`)  
> **최종 갱신**: 2026-06-08T00:30:00+00:00

> **80차 재검증 (2026-06-08T00:30) — test `@4f71543` 불변·58/18 PASS·86 modules·audit 0·develop `95b92b9`(+2 v1.2 CLEAN)·13 ahead·develop 137/45 PASS·124 modules·PASS**: 77차(`4f71543`·58/18·86 modules·PASS) 대비 **test HEAD 불변** — `src/frontend-test` `npm test` **58/18 PASS**·`npm run build` **86 modules**(vite 6.4.3, JS 210.46 kB gzip 66.20 kB, CSS 27.27 kB)·`npm audit` **0** **그대로 PASS**(80차 독립 재실측 CONFIRMED). develop HEAD **`95b92b9`**(+2 vs 77차 `4957bd3`: `3ec8206` feat(uxd-41) US-F03 낙상·사고·특이사항 이벤트 기록 UI 신설 · `95b92b9` fix(v1.2) US-F03 incident API 본문 detail 필드 정합, 15 files approx.) · WT **CLEAN** · develop **13커밋 ahead**(77차 11→+2) · develop `npm test` **137/45 PASS**(77차 130/44 → +7/+1: US-F03 회귀)·`npm run build` **124 modules PASS**(vite 6.4.3, JS 316.89 kB gzip 90.47 kB, CSS 30.85 kB)·`npm audit` **0**. 이관 규율 5 — ProtectedRoute·services.js·SideNav·pilotChecklist·liveConfig·AuthContext **PRESENT** @ test·develop HEAD. SEC-005 localStorage/sessionStorage **0건**. **신규 Open 0건** — **판정 PASS**(v1.1 test `4f71543` 유효). 잔여: backend merge(14) + v1.2 develop 13 ahead + post-merge live E2E(결정 73 권장).

> **77차 재검증 (2026-06-07T23:30) — test `@4f71543` 불변·58/18 PASS·86 modules·audit 0·develop `4957bd3`(+2 v1.2 CLEAN)·11 ahead·develop 130/44 PASS·123 modules·PASS**: 76차(`4f71543`·58/18·86 modules·PASS) 대비 **test HEAD 불변** — `src/frontend-test` `npm test` **58/18 PASS**·`npm run build` **86 modules**(vite 6.4.3, JS 210.46 kB gzip 66.20 kB, CSS 27.27 kB)·`npm audit` **0** **그대로 PASS**(76차 독립 재실측 CONFIRMED). develop HEAD **`4957bd3`**(+2 vs 76차 `c5708c7`: `9863312` feat(uxd-40) US-F01 활력징후 비정상 범위 입력 경고·정상 범위 단일 원천(`src/utils/vitalsRanges.js`·`healthRecords.js` +test) · `4957bd3` fix(v1.2) FAQ Q154 건강·NHIS API 본문 정합, 15 files +572/-75) · WT **CLEAN** · develop **11커밋 ahead**(76차 9→+2) · develop `npm test` **130/44 PASS**(76차 115/40 → +15/+4: vitalsRanges·healthRecords 회귀)·`npm run build` **123 modules PASS**(vite 6.4.3, JS 313.51 kB gzip 89.67 kB, CSS 30.85 kB)·`npm audit` **0**. 이관 규율 5 — ProtectedRoute·services.js·SideNav·pilotChecklist·liveConfig·AuthContext **PRESENT** @ test·develop HEAD. SEC-005 localStorage/sessionStorage **0건**. **신규 Open 0건** — **판정 PASS**(v1.1 test `4f71543` 유효). 잔여: backend merge(13) + v1.2 develop 11 ahead + post-merge live E2E(결정 73 권장).

> **76차 재검증 (2026-06-07T22:27) — test `@4f71543` 불변·58/18 PASS·86 modules·audit 0·develop `c5708c7`(+1 v1.2 CLEAN)·9 ahead·develop 115/40 PASS·120 modules·PASS**: 75차(`4f71543`·58/18·86 modules·PASS) 대비 **test HEAD 불변** — `src/frontend-test` `npm test` **58/18 PASS**·`npm run build` **86 modules**(vite 6.4.3, JS 210.46 kB gzip 66.20 kB, CSS 27.27 kB)·`npm audit` **0** **그대로 PASS**(75차 독립 재실측 CONFIRMED). develop HEAD **`c5708c7`**(+1 vs 75차 `a627c6d`: `feat(uxd-39): Must 흐름 UI 보강 — guardian/checkin·건강·NHIS·접근성` — `MedicationRecordForm`·`VitalsRecordForm`·`NhisReconciliationTable`·`MedicationDuplicateAlert`·`HealthPage`/`HealthDetailPage`/`ReconciliationPage`/`GuardianPortalPage` DS 통합, 17 files +748/-91) · WT **CLEAN** · develop **9커밋 ahead**(75차 8→+1) · develop `npm test` **115/40 PASS**(75차 110/36 → +5/+4: `MedicationRecordForm`·`NhisReconciliationTable`·`HealthDetailPage`·`MedicationDuplicateAlert` 회귀)·`npm run build` **120 modules PASS**(vite 6.4.3, JS 310.33 kB gzip 88.52 kB, CSS 30.77 kB)·`npm audit` **0**. 이관 규율 5 — ProtectedRoute·services.js·SideNav·pilotChecklist·liveConfig·AuthContext **PRESENT** @ test·develop HEAD. SEC-005 localStorage/sessionStorage **0건**. **신규 Open 0건** — **판정 PASS**(v1.1 test `4f71543` 유효). 잔여: backend merge(12) + v1.2 develop 9 ahead + post-merge live E2E(결정 73 권장).

> **75차 재검증 (2026-06-07T21:24) — test `@4f71543` 불변·58/18 PASS·86 modules·audit 0·develop `a627c6d`(+2 v1.2 CLEAN)·8 ahead·develop 110/36 PASS·117 modules·PASS**: 73차(`4f71543`·58/18·86 modules·PASS) 대비 **test HEAD 불변** — `src/frontend-test` `npm test` **58/18 PASS**·`npm run build` **86 modules**(vite 6.4.3, JS 210.46 kB gzip 66.20 kB, CSS 27.27 kB)·`npm audit` **0** **그대로 PASS**(73차 독립 재실측 CONFIRMED). develop HEAD **`a627c6d`**(+2 vs 73차 `9bdf59f`: `6f3f746` 수기 출석 체크인/아웃·결석 흐름(US-E01·E02) · `a627c6d` US-E03 QR 저장·US-E05 출석 통계 API 통합) · WT **CLEAN** · develop **8커밋 ahead**(73차 6→+2) · develop `npm test` **110/36 PASS**(71차 89/28 → +21/+8: AttendancePage·AttendanceStatsPage·QrGeneratePage·AttendanceAbsentModal·CheckoutModal·downloadDataUrl 회귀)·`npm run build` **117 modules PASS**(vite 6.4.3, JS 303.24 kB gzip 86.86 kB, CSS 30.33 kB)·`npm audit` **0**. 이관 규율 5 — ProtectedRoute·services.js·SideNav·pilotChecklist·liveConfig·AuthContext **PRESENT** @ test·develop HEAD. SEC-005 localStorage/sessionStorage **0건**. **신규 Open 0건** — **판정 PASS**(v1.1 test `4f71543` 유효). 잔여: backend merge(11) + v1.2 develop 8 ahead + post-merge live E2E(결정 73 권장).

> **73차 재검증 (2026-06-07T20:21) — test `@4f71543` 불변·58/18 PASS·86 modules·audit 0·develop `9bdf59f`(+2 v1.2 CLEAN)·6 ahead·PASS**: 71차(`4f71543`·58/18·86 modules·PASS) 대비 **test HEAD 불변** — 58/18 PASS·86 modules·audit 0 **그대로 PASS**. develop HEAD **`9bdf59f`**(+2 vs 71차 `42f48e1`: `a68f150` GuardianCheckinPage DS FilterChips(US-E04) · `9bdf59f` P0 CRUD E2E·입금 모달·보호자 초대/수정 수정) · WT **CLEAN** · develop **6커밋 ahead** (71차 4→+2). 이관 규율 5 — ProtectedRoute·services.js·SideNav·pilotChecklist·liveConfig·AuthContext **PRESENT** @ develop HEAD. SEC-005 **0건**. **신규 Open 0건** — **판정 PASS**(v1.1 test `4f71543` 유효). 잔여: backend merge(10) + v1.2 develop 6 ahead + post-merge live E2E(결정 73 권장).

> **71차 재검증 (2026-06-07T19:20) — test `@4f71543` 불변·58/18 PASS·86 modules·audit 0·develop `42f48e1`(+4 v1.2 CLEAN)·89/28 PASS·114 modules·PASS**: 69차(`4f71543`·58/18·86 modules·PASS) 대비 **test HEAD 불변** — 58/18 PASS·86 modules·audit 0 **그대로 PASS**. develop HEAD **`42f48e1`**(+2 vs 69차 `e0eaf32`: `0d83a42` UXD 15 missing pages(US-D01·E03-E05·F04·G01-G07·H01-H04·B01·A01) · `42f48e1` P0 page-flow tests·module coverage KPI·title 정렬) · WT **CLEAN** · develop `npm test` **89/28 PASS**(69차 82/27 → +7/+1: `competitorModuleCoverage.test.js` 3건·pilotPageFlows 강화) · develop `npm run build` **114 modules PASS**(vite 6.4.3, JS 295.02 kB gzip 84.80 kB, CSS 30.23 kB) · develop `npm audit` **0**. 이관 규율 5 — ProtectedRoute·services.js·SideNav·pilotChecklist·liveConfig·AuthContext **PRESENT** @ develop HEAD. SEC-005 **0건**. **신규 Open 0건** — **판정 PASS**(v1.1 test `4f71543` 유효). 잔여: backend merge(9) + v1.2 develop 4 ahead + post-merge live E2E(결정 73 권장).

> **69차 재검증 (2026-06-07T18:12) — v1.1 merge 완료·test `@4f71543`·58/18 PASS·86 modules·audit 0·develop +2(v1.2 CLEAN)·PASS**: 67차(`4f71543`·13 ahead·BLOCK) 대비 **develop→test merge 실행** — test HEAD **`e5fd48d`→`4f71543`**(v1.1 merged). `src/frontend-test` `npm ci`+`npm test` **58/18 PASS**·`npm run build` **86 modules**(vite 6.4.3)·`npm audit` **0**. 이관 규율 5 — `ProtectedRoute`·`services.js`·`SideNav`·`pilotChecklist`·`pilotPageFlows`·`FE-22 liveConfig`·`vitest.live.config.js` **전부 PRESENT** @ test HEAD. SEC-005 localStorage/sessionStorage **0건**. develop HEAD **`e0eaf32`**(+2 v1.2: `64468a3` UXD 35 P0 UI · `e0eaf32` guardians RBAC) · WT **CLEAN** · develop `npm test` **82/27 PASS**. **ROADMAP v1.1 `merge_status: merged`**. **신규 Open 0건** — **판정 PASS**(v1.1). 잔여: backend merge(8) + v1.2 develop 2 ahead + post-merge live E2E(결정 73 권장).

> **67차 재검증 (2026-06-07T17:31) — develop `d592a17`→`f64e1dd`→`4f71543`(+2커밋)·UXD SideNav·FE-22 liveConfig preconditions·CLEAN·58/18 PASS·86 modules·audit 0·develop 13 ahead·ROADMAP merge_status ready·Open 0**: 65차(`d592a17`·46/13·11 ahead) 대비 develop HEAD **`4f71543`**(+2: `f64e1dd` UXD 2단 SideNav·AppShell·기반 UI · `4f71543` FE-22 liveConfig fail-fast) · working tree **CLEAN**. develop build **86 modules**·`npm test` **58/18 PASS**·audit **0**. test `@e5fd48d` **36/N/A**·**13 ahead** · **BLOCK = merge 미실행**(B03/SEC-D14). *(69차 merge 완료·PASS)*

> **65차 재검증 (2026-06-07T16:50) — develop `bb0cec4`→`7170b2a`→`449cd4f`→`d592a17`(+3커밋)·guardian REST+J01/J02·tone Alert a11y·FE-22 live E2E harness develop HEAD 반영·CLEAN·46/13 PASS·75 modules·audit 0·develop 11 ahead·잔여 BLOCK = B03/SEC-D14 merge 게이트 단일·Open 0**: 63차(`811aef3`/`bb0cec4` CLEAN·37/9·8 ahead) 대비 develop HEAD **`d592a17`**(+3커밋: `7170b2a` guardian portal REST 연동·J01/J02 tests·`449cd4f` tone 기반 Alert live region·`PublicAuthLayout` h1/skip-link(US-J01)·`d592a17` **FE-22** Must P1–P8·J01/J02 **live E2E harness**) · working tree **CLEAN**(0 dirty). **이관 규율 5** — `git cat-file -e HEAD:` `services.js`·`pilotChecklist.js`·`GuardianPortalPage.jsx`(+test)·`ClientDetailPage.jsx`·`GuardianInvitationAcceptPage.test.jsx`·`GuardianInvitationList.test.jsx`·`Alert.jsx`·`PublicAuthLayout.jsx`·`sevenRoleRouteMatrix.js`·`ProtectedRoute.jsx`·`src/e2e/pilotLiveApi.e2e.test.js`·`pilotLivePages.e2e.test.jsx`·`guardianLiveApi.e2e.test.js`·`liveConfig.js`·`vitest.live.config.js` **전부 PRESENT**. SEC-005 AuthContext localStorage/sessionStorage **0건**. **FE-22 live harness 게이팅**: `src/e2e/**` 는 `vite.config.js` test `exclude` → 기본 `npm test` 에서 제외, 별도 `npm run test:live-e2e`(`LIVE_E2E=1` + `vitest.live.config.js`)로만 실행(자격증명·실 백엔드 부재 시 skip). develop HEAD `npm run build` **75 modules PASS**(vite 6.4.3, JS 209.19 kB gzip 65.68 kB, CSS 24.45 kB)·`npm test` **46/13 PASS**(vitest 4.1.8, 63차 37/9 → +9/+4 — GuardianPortalPage·GuardianInvitationAcceptPage·GuardianInvitationList·guardian REST 회귀)·`npm audit` **0 vulnerabilities**. test `@e5fd48d` build **36 PASS**·`npm test` **N/A**(Missing script)·audit **2 moderate**(stale) · develop **11 ahead** · **신규 Open 0건**. **R-05 Must P1–P8·R-07 J01/J02 live E2E harness develop HEAD 반영**(실 LIVE_E2E run 은 develop→test merge·backend v1 test 승격 후). 판정 **BLOCK**(B03/SEC-D14 merge 게이트 단일).

> **63차 재검증 (2026-06-07T15:40) — develop `e043eac`→`811aef3`(+2커밋)·Must API pages·pilotChecklist·7-role·pilotPageFlows·SEC-008 develop HEAD 반영·CLEAN·35/9 PASS·74 modules·audit 0·잔여 BLOCK = B03 merge 게이트 단일·Open 0**: 61차(`e043eac` CLEAN·6/6·audit 4 vuln) 대비 develop HEAD **`811aef3`**(baseline `c3b863e` +2커밋: `b87a8f5` US-J01 a11y·`811aef3` Must API·pilot·7-role·SEC-008) · working tree **CLEAN**(0 dirty). **이관 규율 5** — `git cat-file -e HEAD:` `services.js`·`pilotChecklist.js`(+test)·`pilotPageFlows.test.jsx`·`sevenRoleJwtLogin/RouteGuard`·`sevenRoleRouteMatrix.js`·Must pages(`AttendancePage`·`BillingPage`·`ClientDetailPage`·`HealthPage`·`NHISImportPage`·`ReconciliationPage`)·`ProtectedRoute.jsx`(src/auth) **전부 PRESENT**. SEC-005 localStorage/sessionStorage **0건**. develop HEAD `npm run build` **74 modules PASS**(vite 6.4.3, JS 205.76 kB)·`npm test` **35/9 PASS**(vitest 4.1.8, 61차 6/2 → +29/+7)·`npm audit` **0 vulnerabilities**(**SEC-008 develop HEAD 해소**, 61차 4→0). test `@e5fd48d` build **36 PASS**·N/A · develop **7 ahead** · **신규 Open 0건** — v1.1 H04·M01·R-04a·R-05·SEC-008 **develop HEAD 반영**(라이브 E2E·J01 백엔드 API는 merge·backend 후). 판정 **BLOCK**(B03 merge 게이트 단일).
> **63차 추가 관측 (15:46, coder 동시 진행)**: 검증 직후 coder가 **`811aef3`→`bb0cec4`**(+1커밋 `fix(v1.1): restrict billing route access to admin roles` — billing 라우트 admin RBAC·`roleNav` `STAFF_NAV` 분리) 커밋. develop HEAD `bb0cec4` working tree **CLEAN**·`npm test` **37/9 PASS**(+2)·build **74 modules**·audit **0**·develop **8 ahead**. HEAD Fixed(811aef3 산출물) 규율 5 유효·판정 **BLOCK** 불변. **coder 동시 진행 중 — HEAD 추가 진전 가능**.

> **61차 재검증 (2026-06-07T15:00) — baseline 43차 +2커밋·develop CLEAN·6/6 PASS·test stale·merge 3커밋·BLOCK(B03)**: develop HEAD **`e043eac`**(+2 vs `7c0ecdc`) · working tree **CLEAN** · develop build **65 modules PASS** · develop `npm test` **6/6 PASS** · test `@e5fd48d` build **36 PASS**·N/A · develop **3 ahead** · SEC-D12 HEAD **PRESENT** · v1.1 Must API/E2E **미충족** · 판정 **BLOCK**. *(63차에서 `811aef3`로 진전 — H04·M01·SEC-008 develop HEAD 반영)*

> **59차 재검증 (2026-06-08T02:05) — workspace baseline 단절·develop=test @e5fd48d·TSR57 재현 불가·SEC-D12·QA-B11·BLOCK**: *(59차 — **61차에서 baseline 43차·develop `e043eac`로 대체**, SEC-D12 Fixed @ HEAD 재확인)*

> **57차 재검증 (2026-06-07T10:11) — B07 #6 18→20 files·FE-7 회귀(209/210 FAIL)·HEAD Fixed 유지·BLOCK = B03+B07 #6·Open 1(HIGH)**: *(TSR57 baseline — workspace @e5fd48d에서 **재현 불가**, planner baseline 유지)*

> **55차 재검증 (2026-06-07T09:29) — B07 recurrence #6(CLEAN→DIRTY 15 files)·HEAD Fixed 유지·WT 205/42 PASS·BLOCK = B03+B07 #6·Open 1**: 53차(`d5654c0` CLEAN·199/40·B03 단일) 대비 develop HEAD **`d5654c0` 불변**·working tree **CLEAN→DIRTY** — **11M+4U=15 files**. 신규 WIP: **`DateInput.jsx`(+test)**·**`GuardianInvitationList.jsx`(+test — J01 초대 목록 UI)** + modified `ClientDetailPage`(+98)·`GuardianInviteModal`·`GuardianListCard`·`LoginHistoryPanel`·`AuditLogPanel`·`ClientPhotoField`·`services.js`·`GuardianInvitationAcceptPage`(+test)·`components.css`. **이관 규율 5 — HEAD Fixed 유지**: `git cat-file -e HEAD:` `LogoutButton`·`GuardianInvitationAcceptPage`·`GuardianInvitationAcceptForm`·`PublicAuthLayout`·`BillingPage.layout.test` **PRESENT** · WT-only `DateInput`·`GuardianInvitationList` **HEAD ABSENT**. develop WT `npm run build` **758 modules PASS**(+2 vs 756)·`npm test` **205/42 PASS**(+6/+2 vs 199/40)·`npm audit` **0건**. test `@e5fd48d` build 36·npm test N/A·**18 behind**. **신규 Open 1건(BLOCK)**: **QA-B07 recurrence #6**. 판정 **BLOCK**(B03+B07 #6).

> **53차 재검증 (2026-06-07T08:36) — COD 35차 `d5654c0` FE-17 J01 수락 UI·LogoutButton·레이아웃 회귀·B07 #5 Fixed·CLEAN·199/40·756 modules·B03 BLOCK 단일·Open 0**: 52차(`0b9b001` DIRTY 20 files·B07 #5 Open) 대비 develop HEAD **`0b9b001`→`d5654c0`**(+1커밋 COD 35차 `feat(v1.1): FE-17 J01 보호자 초대 수락 UI·LogoutButton·레이아웃 회귀 (B07 #5)`, 25 files +823/-57, **18 ahead**)·working tree **DIRTY→CLEAN**(0 files — 20 files 일괄 커밋). **QA-B07 recurrence #5 Fixed TSR 53차 독립 검증 PASS**: `git status --porcelain` 0줄·`git cat-file -e HEAD:` `LogoutButton.jsx`·`GuardianInvitationAcceptPage.jsx`·`GuardianInvitationAcceptForm.jsx`·`PublicAuthLayout.jsx`·`BillingPage.layout.test.jsx`·`LogoutButton.test.jsx`·`services.js`(acceptGuardianInvitationApi) **전부 PRESENT**(이관 규율 5). SEC-005 AuthContext localStorage/sessionStorage **0건**. develop HEAD(clean) `npm run build` **756 modules PASS**(vite 6.4.3, 3 청크: react-vendor 166.34·index 186.68·recharts 393.53 kB)·`npm test` **199/40 PASS**(vitest 4.1.8, +5/+2 vs 52차 194/38)·`npm audit` **0건**. test `@e5fd48d` build 36·npm test N/A·**18 behind**. **신규 Open 0건** — B07 #5 소멸. 판정 **BLOCK**(B03 단일).

> **52차 재검증 (2026-06-07T08:03) — B07 recurrence #5(CLEAN→DIRTY 20 files)·HEAD Fixed 유지·WT 194/38 PASS·BLOCK = B03+B07 #5·Open 1**: 50차(`0b9b001` CLEAN·187/35·B03 단일) 대비 develop HEAD **`0b9b001` 불변**·working tree **CLEAN→DIRTY** — **15M+5U=20 files**. 신규 WIP: **`LogoutButton.jsx`(+test)**·**`BillingPage.layout.test.jsx`**·**`GuardianInvitationAcceptPage.jsx`(+test — J01 수락 UI)** + modified `AuthContext`·`AppShell`·Recharts·청구/보호자 페이지·`services.js`·스타일. **이관 규율 5 — HEAD Fixed 유지**: `git cat-file -e HEAD:` 기존 Fixed **PRESENT** · WT-only **HEAD ABSENT**. develop WT `npm run build` **754 modules PASS**(+2)·`npm test` **194/38 PASS**(+7/+3)·`npm audit` **0건**. test `@e5fd48d` build 36·npm test N/A·**17 behind**. **신규 Open 1건(BLOCK)**: **QA-B07 recurrence #5**. 판정 **BLOCK**(B03+B07 #5).

> **50차 재검증 (2026-06-07T07:17) — B07 #3·#4 소멸·FE-15 Fixed 유지·working tree CLEAN·잔여 BLOCK = B03 merge 게이트 단일·Open 0**: 49차(`c98f98d` CLEAN·186/34·B03 단일) 대비 develop HEAD `c98f98d`→**`0b9b001`**(+1커밋 COD 34차 `fix(v1.1): Must 페이지 UXD ds-* 유틸리티 전환·AttendancePage 레이아웃 회귀 테스트`, **17 ahead**), working tree **CLEAN**(0 dirty). **이관 규율 5 PASS** — `git status --porcelain` 0줄·`git cat-file -e HEAD:` `ChartContainer`·`FeeScheduleTable`·`AuthContext`·`pilotChecklist`·`chartColors`·`vite.config.js`·`sevenRoleJwtLogin.test.jsx`·`sevenRoleRouteMatrix.js` **전부 PRESENT**. SEC-005 AuthContext localStorage/sessionStorage **0건**. **FE-15 코드 스플릿 Fixed 유지** — 3 청크 유지(react-vendor 166.34·index 181.88·recharts 393.53 kB). develop HEAD(clean) `npm run build` **752 modules PASS**(vite 6.4.3, CSS 52.95 kB)·`npm test` **187/35 PASS**(vitest 4.1.8, 49차 186/34 → +1/+1 `AttendancePage.layout.test.jsx`)·`npm audit` **0건**. test `@e5fd48d` build 36·npm test N/A·**17 behind**. **frontend Open 0건** — B07 #3·#4·FE-15 사유 전부 소멸, Planned BLOCK = **B03 단일**. 판정 **BLOCK**(B03).

> **49차 재검증 (2026-06-07T15:45) — B07 #4 신호 해소(COD 33차 `c98f98d`)·FE-15 코드 스플릿 Fixed·working tree CLEAN·잔여 BLOCK = B03 merge 게이트 단일·Open 0**: 47차(`4be0938` CLEAN·비차단 LOW JS 744.95 kB) + TSR 48차 backend 라운드 교차 관측(frontend `4be0938` 재오염 5 files — B07 recurrence #4 신호) 대비 develop HEAD `4be0938`→**`c98f98d`**(+1커밋 `fix(v1.1): UXD 인라인 style 제거·FE-15 코드 스플릿·레이아웃 회귀 테스트`, 7 files +145/-23, **16 ahead**), working tree **CLEAN**(0 dirty — 재오염 5 files `c98f98d` 일괄 커밋, **B07 #4 신호 소멸·정식 Open 미등록**). **이관 규율 5 PASS** — `git status --porcelain` 0줄·`git cat-file -e HEAD:` `ChartContainer`·`FeeScheduleTable`·`AuthContext`·`pilotChecklist`·`chartColors`·`vite.config.js` **전부 PRESENT**. SEC-005 AuthContext localStorage/sessionStorage **0건**. **FE-15 코드 스플릿 정식 Fixed** — `vite.config.js` `manualChunks` → 47차 단일 JS 청크 **744.95 kB** → **3 청크 분리**(`react-vendor` 166.34·`index` 182.52·`recharts` 393.53 kB, 최대 **393.53 kB < 500 kB**, vite 경고 해소). develop HEAD(clean) `npm run build` **752 modules PASS**(vite 6.4.3, CSS 52.04 kB)·`npm test` **186/34 PASS**(vitest 4.1.8, 47차 185/33 → +1/+1 `ClientDetailPage.layout.test.jsx`)·`npm audit` **0건**. test `@e5fd48d` build 36·npm test N/A·**16 behind**. **frontend Open 0건** — B07 #4 신호·FE-15 LOW 사유 소멸, Planned BLOCK = **B03 단일**. 판정 **BLOCK**(B03).

> **47차 재검증 (2026-06-07T14:45) — B07 #3 Fixed TSR 독립 검증 PASS(COD 31차 `4be0938`·82 files 일괄 커밋·working tree CLEAN)·잔여 BLOCK = B03 merge 게이트 단일**: 45차(`3fdc266` DIRTY 76 files) 대비 develop HEAD `3fdc266`→**`4be0938`**(+1커밋, **15 ahead**), working tree **76 files → CLEAN**(0 dirty). **QA-B07 recurrence #3 정식 Fixed 확정 — TSR 독립 검증 PASS**: `git status --porcelain` 0줄·`git cat-file -e HEAD:` Recharts(`ChartContainer`·`AttendanceRateChart`·`HealthTrendChart`)·FE-13(`FeeScheduleTable`·`CopayRateTable`·`NhisImportGuidePanel`·`BillingStatusConfirmModal`)·FE-14(`AuditLogPanel`·`BackupSettingsPanel`·`LoginHistoryPanel`·`PasswordChangeModal`)·`HealthAlertList`·`GuardianDailySummary`·`FeeRateHistoryPanel`·`chartColors.js`·`dashboardWidgets.js` **전부 PRESENT**(이관 규율 5 PASS). SEC-005 AuthContext localStorage/sessionStorage **0건**. develop HEAD(clean) `npm run build` **752 modules PASS**(vite 6.4.3)·`npm test` **185/33 PASS**(vitest 4.1.8)·`npm audit` **0건**. `recharts ^2.15.4` 커밋 반영. test `@e5fd48d` build 36·npm test N/A·**15 behind**. **frontend Open 0건** — B07 #3 dirty 사유 **소멸**, Planned BLOCK = **B03 단일**(merge 게이트). 비차단 LOW: JS 청크 744.95 kB(>500 kB). 판정 **BLOCK**(B03).

> **45차 재검증 (2026-06-07T14:02) — B07 #3 dirty-tree 확대(72→76 files)·WT 181/30 PASS·B03 BLOCK 유지**: develop HEAD **불변**(`3fdc266`)·working tree **40M+36U=76 files**(43차 38M+34U=72 → +4). 신규 WIP: **`FeeScheduleTable`(+test)** + 기존 Recharts·청구·copay·설정 WIP. WT `npm run build` **749 modules PASS**(+1)·`npm test` **181/30 PASS**(+2/+1)·`npm audit` **0건**(FE-7). test `@e5fd48d` build 36·npm test N/A·14 behind. **frontend Open 0건** — Planned BLOCK **B03 + B07 #3**. 판정 **BLOCK**.

> **43차 재검증 (2026-06-07T13:27) — B07 #3 dirty-tree 확대(61→72 files)·WT 179/29 PASS·B03 BLOCK 유지**: develop HEAD **불변**(`3fdc266`)·working tree **38M+34U=72 files**(41차 37M+24U=61 → +11). 신규 WIP: `BillingStatusConfirmModal`·`CopayRateTable`·`GuardianDailySummary`·`HealthAlertList`·`NhisImportGuidePanel`(+tests). WT `npm run build` **748 modules PASS**(+5)·`npm test` **179/29 PASS**(+10/+5)·`npm audit` **0건**(FE-7). test `@e5fd48d` build 36·npm test N/A·14 behind. **frontend Open 0건** — Planned BLOCK **B03 + B07 #3**. 판정 **BLOCK**.

> **41차 재검증 (2026-06-07T12:52) — 39차 대비 상태 불변(±1 modified)·WT 169/24 PASS·B03 BLOCK 유지**: develop HEAD **불변**(`3fdc266`)·working tree **37M+24U=61 files**(39차 60→41차 +1 modified). WT `npm run build` **743 modules PASS**·`npm test` **169/24 PASS**·`npm audit` **0건**(FE-7). test `@e5fd48d`(frontend-test) build 36·npm test N/A·14 behind. **frontend Open 0건** — Planned BLOCK **B03 + B07 #3**. 판정 **BLOCK**.

> **39차 재검증 (2026-06-07T12:09) — B07 #3 dirty-tree 확대(44→60 files)·WT 169/24 PASS·B03 BLOCK 유지**: 37차 대비 develop HEAD **불변**(`3fdc266`)·working tree **확대** 44→**60 files**(36M+24U: `LoginHistoryPanel`·`PasswordChangeModal`·`PasswordResetRequestModal`·`PlatformOrgDetailModal`(+tests)·`SettingsPage.test.jsx` + Recharts·감사·백업 WIP). WT `npm run build` **743 modules PASS**·`npm test` **169/24 PASS**(+8/+4)·`npm audit` **0건**(FE-7). test `@e5fd48d` build 36·npm test N/A·14 behind. **frontend Open 0건** — Planned BLOCK **B03 + B07 #3**. 판정 **BLOCK**.

> **37차 재검증 (2026-06-07T11:30) — B07 #3 dirty-tree 확대(26→44 files)·WT 161/20 PASS·B03 BLOCK 유지**: 35차 대비 develop HEAD **불변**(`3fdc266`)·working tree **확대** 26→**44 files**(26M+18U: `AuditLogPanel`·`BackupSettingsPanel`·`PasswordChangeModal`·`FilterChips.test` + Recharts·Platform WIP). WT `npm run build` **741 modules PASS**·`npm test` **161/20 PASS**(+17/+7)·`npm audit` **0건**(FE-7). test `@e5fd48d` build 36·npm test N/A·14 behind. **frontend Open 0건** — Planned BLOCK **B03 + B07 #3**. 판정 **BLOCK**.

> **35차 재검증 (2026-06-07T01:50) — B07 #3 dirty-tree 확대(18→26 files)·WT 144/13 PASS·B03 BLOCK 유지**: 33차 대비 develop HEAD **불변**(`3fdc266`)·working tree **확대** 18→**26 files**(18M+8U: `BatchProgressSteps`·`PlatformOrgDetailModal`·Platform/NHIS/Reconciliation/Forbidden WIP 추가). WT `npm run build` **738 modules PASS**·`npm test` **144/13 PASS**(+2/+1)·`npm audit` **0건**(FE-7). 이관 규율 5 — HEAD Fixed **PRESENT**. test `@e5fd48d` build 36·npm test N/A·14 behind. **frontend Open 0건** — Planned BLOCK **B03 + B07 #3**. 판정 **BLOCK**.

> **33차 재검증 (2026-06-07T01:16) — B07 recurrence #3(Recharts 차트 WIP 18 files)·WT build/test PASS·B05 해소·B03 BLOCK 유지**: 31차(`3fdc266` CLEAN) 대비 develop HEAD **불변**·working tree **DIRTY 18 files**(13M+5U: `recharts ^2.15.4`·`ChartContainer`·`AttendanceRateChart`·`BranchCompareChart`·`HealthTrendChart`·`ChartContainer.test.jsx` + Dashboard·Health·AttendanceStats·FeeSchedule·ClientDetail·chartColors·pilotPageFlows 등). WT `npm run build` **736 modules PASS**·`npm test` **142/12 PASS**(+2/+1)·`npm audit` **0건**(FE-7 충족). 이관 규율 5 — HEAD `3fdc266` Fixed **PRESENT 유효**. test `@e5fd48d` build 36·npm test N/A·14 behind. ROADMAP v1 `merged` → **B05 선행 해소**. **QA-B07 recurrence #3 Planned**. 잔여 BLOCK = **B03 + B07 #3**. 판정 **BLOCK**.

> **31차 재검증 (2026-06-07T00:43) — COD `3fdc266` P1–P8 페이지 단위 E2E·UXD 14차 `a42d6fb`·140/11 PASS·merge 게이트 단일(B03·B05) 잔존**: 29차(`57ff3c0` CLEAN) 대비 **frontend develop 전진** — develop HEAD `57ff3c0`→`a42d6fb`→**`3fdc266`**(+2커밋, origin/develop 대비 **14 ahead**). ① **`a42d6fb feat(ux/14차)`**: `BATCH_STATUS`·`FeeRateHistoryPanel`(US-G00a)·`chartColors.js`·Recharts 토큰. ② **`3fdc266 test(v1.1): P1–P8·J01/J02 Must 화면 페이지 단위 E2E`**: `pilotPageFlows.test.jsx`(433 lines — 8 Must 페이지 RTL fetch-mock JWT 검증). develop working tree **CLEAN**. 이관 규율 5 — HEAD `3fdc266` 기존 Fixed + 신규 산출물 **PRESENT**. HEAD `npm run build` **113 modules PASS**·`npm test` **140/11 PASS**(+10/+1)·`npm audit` **0건**. test `@e5fd48d` build 36·npm test N/A·audit 0h·2mod(stale). **R-05 P1–P8 페이지 단위 E2E PARTIAL 강화**. 잔여 BLOCK = **merge 게이트 단일(B03·B05)**. 판정 **BLOCK**.

> **29차 재검증 (2026-06-06T23:31) — COD 20차 `57ff3c0` 7역할 JWT 로그인·라우트 가드 E2E 자동화·130/10 PASS·merge 게이트 단일(B03·B05) 잔존**: 28차(`07fd305` CLEAN) 대비 **frontend develop 전진** — develop HEAD `07fd305`→**`57ff3c0`**(+1커밋 COD 20차 `test(v1.1): 7역할 JWT 로그인·라우트 가드 E2E 자동화`, origin/develop 대비 **12 ahead**). 4 files +315/-1: `src/auth/sevenRoleJwtLogin.test.jsx`(132 lines — AuthProvider login() 7역할 JWT 세션·홈 경로 + LoginPage 폼 submit 7역할 Vitest 자동화)·`src/auth/sevenRoleRouteGuard.test.jsx`(83 lines — ProtectedRoute 7역할 접근·거부 매트릭스 E2E)·`src/auth/sevenRoleRouteMatrix.js`(75 lines — 7역할 라우트 접근 매트릭스 모듈)·`src/auth/roleHomePaths.test.jsx`(+26 lines). develop working tree **CLEAN**(0 dirty). 이관 규율 5 — HEAD `57ff3c0` 기존 Fixed 산출물 + 신규 `sevenRoleJwtLogin.test.jsx`·`sevenRoleRouteGuard.test.jsx`·`sevenRoleRouteMatrix.js` **PRESENT 유효**. develop HEAD(clean) `npm run build` **112 modules PASS**(vite 6.4.3, JS 314.56 kB gzip 92.06 kB, CSS 42.67 kB)·`npm test`(vitest 4.1.8) **130 tests/10 files PASS**(28차 37/8 → **+93 tests/+2 files**: sevenRoleJwtLogin·sevenRoleRouteGuard, FE-7 회귀 없음)·`npm audit` **0건**. test `@e5fd48d` build 36·npm test N/A·audit 0h·2mod(stale). **R-04 7역할 로그인·라우트 가드 Vitest 자동화 진전** — AuthProvider login() 7역할 JWT 메모리 세션·홈 경로 검증 + ProtectedRoute 7역할 허용·거부 매트릭스 자동화(라이브 백엔드 E2E는 backend v1 test 승격 후). **잔여 BLOCK = merge 게이트 단일(B03·B05)** — 불변. 판정 **BLOCK**.

> **28차 재검증 (2026-06-06T23:19) — UXD 13차 `07fd305` CLEAN·37/8 PASS·merge 게이트 단일(B03·B05) 잔존**: 27차(`cc34f23` CLEAN) 대비 **frontend develop 전진** — develop HEAD `cc34f23`→**`07fd305`**(+1커밋 UXD 13차 `feat(ux): 전사 설정 Switch 컴포넌트·셀프 체크인 토글`, origin/develop 대비 **11 ahead**). `Switch.jsx`(WAI-ARIA switch 패턴·role=switch·aria-checked·44px·forced-colors)·`Switch.test.jsx`(5건)·`SettingsPage.jsx`(REQUIREMENTS §3-3·FLOWCHART §2 allow_client_self_checkin 조작 컨트롤). develop working tree **CLEAN**(0 dirty). 이관 규율 5 — HEAD `07fd305` 기존 Fixed 산출물 **PRESENT 유효**. develop HEAD(clean) `npm run build` **112 modules PASS**(vite 6.4.3, JS 314.56 kB gzip 92.06 kB, CSS 42.67 kB)·`npm test`(vitest 4.1.8) **37 tests/8 files PASS**(27차 32/7 → +5/+1: Switch.test.jsx 5건, FE-7 회귀 없음)·`npm audit` **0건**. test `@e5fd48d` build 36·npm test N/A·audit 0h·2mod(stale). **잔여 BLOCK = merge 게이트 단일(B03·B05)** — 불변. 판정 **BLOCK**.

> **27차 재검증 (2026-06-06T22:40) — COD 19차 `cc34f23` 파일럿 P1–P8·J01/J02 Must API 라우팅 자동화·working tree CLEAN 유지·merge 게이트 단일(B03·B05) 잔존**: 26차(`404a30e` CLEAN) 대비 **frontend develop 전진** — develop HEAD `404a30e`→**`cc34f23`**(+1커밋 COD 19차; origin/develop 대비 **10 ahead**). `test(v1.1): 파일럿 P1–P8·J01/J02 Must API JWT 라우팅 자동화` — ① `src/api/pilotChecklist.js`(211 lines): USER_STORIES §13 P1–P8 시나리오를 `services.js` 경로에 매핑 ② `src/api/pilotChecklist.test.js`(104 lines): Vitest fetch mock으로 JWT 헤더·HTTP 메서드·경로 검증 ③ `src/components/ui/GuardianInviteModal.test.jsx`(81 lines): 보호자 초대 UI 회귀 4건. develop working tree **CLEAN**(0 dirty). 이관 규율 5 — `git cat-file -e HEAD:` `pilotChecklist.js`·`pilotChecklist.test.js`·`GuardianInviteModal.test.jsx`·api·routeAccess·AuthContext(localStorage 0건)·favicon·dashboardWidgets·`LoginPage.jsx`·`Modal.jsx`·`package.json` test **PRESENT** (PASS). develop HEAD(clean) `npm run build` **111 modules PASS**(vite 6.4.3, JS 313.68 kB gzip 91.78)·`npm test`(vitest 4.1.8) **32 tests/7 files PASS**(26차 13/5 → +19 tests/+2 files, FE-7 회귀 없음)·`npm audit --audit-level=high` **0건**. test `@e5fd48d` `npm run build` **36 modules PASS**·`npm test` **N/A**(merge 미실행)·`npm audit` 0 high·2 moderate(stale). **잔여 BLOCK = merge 게이트 단일(B03·B05)** — 불변. **R-05 Must API P1–P8·R-07 J01/J02 라우팅 fetch-mock 자동화 진전**(라이브 7역할 JWT E2E·J01 백엔드 초대 API 잔여). 판정 **BLOCK**.

> **26차 재검증 (2026-06-06T22:20) — UXD 12차 `404a30e` LoginPage DS·Modal 포커스 트랩·고대비 모드·working tree CLEAN 유지·merge 게이트 단일(B03·B05) 잔존**: 25차(`ed1bf22` CLEAN) 대비 **frontend develop 전진** — develop HEAD `ed1bf22`→**`404a30e`**(+1커밋 UXD 12차; origin/develop 대비 **9 ahead**). `feat(ux): 로그인 화면 스타일·Modal 포커스 트랩·고대비 모드` — ① `LoginPage.jsx`: `.ds-label`→`Field`/`TextInput`/`Button(block·lg)`/`Alert`·`.ds-login` 카드·브랜드 모노그램 ② `Modal.jsx`: Tab/Shift+Tab 포커스 트랩(WAI-ARIA dialog) ③ `components.css`: `forced-colors`·`prefers-contrast` WCAG 1.4.11·`.ds-label`·`.ds-login` 클래스. develop working tree **CLEAN**(0 dirty). 이관 규율 5 — `git cat-file -e HEAD:` `LoginPage.jsx`·`Modal.jsx`·`src/styles/components.css`·api·routeAccess·AuthContext(localStorage 0건)·favicon·dashboardWidgets·`package.json` test·`*.test.jsx`×5 **PRESENT** (PASS). develop HEAD(clean) `npm run build` **111 modules PASS**(vite 6.4.3, JS 313.68 kB gzip 91.78)·`npm test`(vitest 4.1.8) **13 tests/5 files PASS**(FE-7 회귀 없음)·`npm audit --audit-level=high` **0건**. test `@e5fd48d` `npm run build` **36 modules PASS**·`npm test` **N/A**(merge 미실행)·`npm audit` 0 high·2 moderate(stale). **잔여 BLOCK = merge 게이트 단일(B03·B05)** — 불변. 판정 **BLOCK**.

> **25차 재검증 (2026-06-06T21:32) — COD 17차 B07 recurrence #2·SEC-008 Fixed 독립 검증·working tree CLEAN 회복·merge 게이트 단일(B03·B05) 잔존**: 24차(`2d742b3` DIRTY 8 files·npm audit 5 vuln) 대비 **frontend develop 전진** — develop HEAD `2d742b3`→`a84473f`→**`ed1bf22`**(+2커밋 COD 17차; origin/develop 대비 **8 ahead**). ① **`a84473f feat(v1.2-p0): 대시보드 실데이터 위젯·Must 페이지 API 보강 (US-M02)`**(8 files +636/-170) — 23·24차 미커밋이던 대시보드 실데이터 WIP 8 files(`dashboardWidgets.js`·`dashboardWidgets.test.js`·`DashboardPage.jsx`·`AttendancePage.jsx`·`ClientFormPage.jsx`·`GuardiansPage.jsx`·`GuardianListCard.jsx`·`services.js`) **일괄 커밋** → **QA-B07 recurrence #2 정식 Fixed 확정**(working tree CLEAN). ② **`ed1bf22 fix(security): vite 6·vitest 4·esbuild override`**(`package.json`+`package-lock.json`, +390/-303) — vite `^6.4.3`·vitest `^4.1.8`·`overrides.esbuild ^0.25.0` → **`npm audit` 0 vulnerabilities(high·all 모두)** → **SEC-008 정식 Fixed 확정**. develop working tree **CLEAN**(0 dirty — 24차 8 files → 0). 이관 규율 5 — `git cat-file -e HEAD:` api·routeAccess·AuthContext(localStorage/sessionStorage 0건)·favicon·ThemeToggle·tokens.css·**`dashboardWidgets.js`·`dashboardWidgets.test.js`(신규 커밋)** **전부 PRESENT**(HEAD `ed1bf22` Fixed 유효). develop HEAD(clean) `npm run build` **111 modules PASS**(vite 6.4.3, JS 313.14 kB gzip 91.58, CSS 39.23 kB)·`npm test`(vitest 4.1.8) **13 tests/5 files PASS**(FE-7 회귀 없음). test `@e5fd48d` `npm run build` **36 modules PASS**·`npm test` **N/A**(merge 미실행)·`npm audit` 0 high·2 moderate(stale, vite 5.4.21). **잔여 BLOCK = merge 게이트 단일(B03·B05)** — dirty-tree(B07)·SEC-008 사유 **소멸**. 판정 **BLOCK**.

> **24차 재검증 (2026-06-06T21:13) — B07 recurrence #2(dirty-tree 지속)·UXD 11차·npm audit 에스컬레이션·merge 게이트 BLOCK 유지**: 23차(`5656e19` DIRTY 8 files) 대비 develop HEAD `5656e19`→`2d742b3`(UXD 11차 dark mode), working tree **DIRTY 8 files 지속**(B07 recurrence #2). WT build 114·npm test 13/5 PASS. npm audit 에스컬레이션 5 vuln(1 critical, dev chain) → SEC-008. 판정 BLOCK. (이력)

> **23차 재검증 (2026-06-06T20:17)**: develop HEAD `5656e19`(UXD 10차) DIRTY 8 files. WT build 112 modules·npm test 13/5 PASS. B07 recurrence #2 Open→17차 planner Planned. merge 게이트 B03·B05 유지. (이력)

> **21차 재검증 (2026-06-06T19:22)**: B07 recurrence Fixed·working tree CLEAN·merge 게이트 단일(B03·B05). (이력)

---

## 1. 이관 판정 요약

| 항목 | 값 |
|------|-----|
| **대상 버전** | v1.1 (프론트엔드 MVP — frontend stream) |
| **ROADMAP `merge_status`** | **`merged`** (test `@4f71543` 승격 완료) |
| **선행 v1 `merge_status`** | `merged` (backend develop `4c74f84` · test stale `2799e29` · 14 ahead) |
| **develop HEAD** | `95b92b9` — US-F03 incident API detail 필드 정합 (+ `3ec8206` UXD-41 낙상·사고 UI · `4957bd3` FAQ Q154 정합) |
| **develop working tree** | **CLEAN** (0 dirty) |
| **test HEAD** | `4f71543` — v1.1 merged (FE-22 liveConfig + UXD SideNav·Must API·guardian REST) |
| **test working tree** | **CLEAN** |
| **develop ahead of test** | **13 commits** (v1.2 `64468a3`·`e0eaf32`·`0d83a42`·`42f48e1`·`a68f150`·`9bdf59f`·`6f3f746`·`a627c6d`·`c5708c7`·`9863312`·`4957bd3`·`3ec8206`·`95b92b9`) |
| **이관 판정** | **PASS** — v1.1 test 브랜치 검증 완료 (80차 재확인) |

> **PASS 근거 (69차)**: ① **v1.1 develop→test merge 완료** — test `@4f71543` = ROADMAP merged HEAD. ② test `npm test` **58/18 PASS** · build **86 modules** · audit **0**. ③ 이관 규율 5 — Must API·SideNav·FE-22 harness·ProtectedRoute **PRESENT** @ test HEAD. ④ develop v1.2 **+2 commits CLEAN** — B07 recurrence 없음. ⑤ Must·J01/J02 **live E2E run** 미실행 — **결정 73 post-merge 권장**(merge-blocking 아님).

> **PASS 금지 사유 (65차, 이력)**: ① ROADMAP v1.1 merge pending(구 65차 기록) → **48차 ready로 갱신** ② develop→test merge 미실행 ③ test npm test N/A ④ live E2E run post-merge.

> **PASS 금지 사유 (61차, 이력)**: ① ROADMAP v1.1 `merge_status: pending`(B03) ② develop→test merge 미실행(3 ahead) ③ test npm test N/A ④ H04·M01·R-05/R-07 미충족 ⑤ develop audit 4 vuln(SEC-008) ⑥ FE-18·FE-19 Planned — **63차에서 H04·M01·SEC-008 develop HEAD 반영으로 해소**.

> **PASS 금지 사유 (59차, 이력)**: baseline 단절·SEC-D12·QA-B11 — **61차에서 43차 baseline + develop `e043eac`로 해소·SEC-D12 HEAD PRESENT 재확인**.

> **PASS 금지 사유 (57차)**: ① ROADMAP v1.1 `merge_status: pending`(B03), ② develop→test merge 미실행(test stale `e5fd48d`, **18 commits behind**), ③ **develop working tree DIRTY 20 files**(B07 recurrence #6), ④ **develop WT `npm test` 209/210 FAIL**(`GuardianListCard.test.jsx` MaskedPhone 마스킹·FE-7), ⑤ v1.1 잔여 완료 기준 `[ ]` — Must **라이브 E2E**·J01 백엔드 API. develop WT build **PASS**(758 modules)·audit **0건** — **test FAIL·커밋 없이 PASS 불가**.
> **PASS 금지 사유 (55차)**: ① ROADMAP v1.1 `merge_status: pending`(B03), ② develop→test merge 미실행(test stale `e5fd48d`, **18 commits behind**), ③ **develop working tree DIRTY 15 files**(B07 recurrence #6 — `DateInput`·`GuardianInvitationList`·`ClientDetailPage` J01 WIP 미커밋), ④ v1.1 잔여 완료 기준 `[ ]` — Must **라이브 E2E**·J01 백엔드 API. develop WT build/test/audit **PASS**(758 modules·205/42·0건) — **커밋 없이 PASS 불가**.
> **PASS 금지 사유 (53차)**: ① ROADMAP v1.1 `merge_status: pending`(B03), ② develop→test merge 미실행(test stale `e5fd48d`, **18 commits behind**), ③ v1.1 잔여 완료 기준 `[ ]` — Must **라이브 E2E**·J01 백엔드 API. develop HEAD(clean) build/test/audit **PASS**(756 modules·199/40·0건) — **merge 게이트(B03) 단일 BLOCK**.
> **PASS 금지 사유 (52차)**: ① ROADMAP v1.1 `merge_status: pending`(B03), ② develop→test merge 미실행(test stale `e5fd48d`, **17 commits behind**), ③ **develop working tree DIRTY 20 files**(B07 recurrence #5 — `LogoutButton`·`GuardianInvitationAcceptPage`·`BillingPage.layout.test` + AuthContext·Recharts·청구 페이지 WIP 미커밋), ④ v1.1 잔여 완료 기준 `[ ]` — Must **라이ve E2E**·J01 백엔드 API. develop WT build/test/audit **PASS**(754 modules·194/38·0건) — **커밋 없이 PASS 불가**.
> **PASS 금지 사유 (50차, 이력)**: ① ROADMAP v1.1 `merge_status: pending`(B03), ② develop→test merge 미실행(test stale `e5fd48d`, **17 commits behind**), ③ v1.1 잔여 완료 기준 Must **라이ve E2E**·J01. B07 #3·#4·FE-15 소멸. develop HEAD(clean) build/test/audit PASS.
> **PASS 금지 사유 (49차, 이력)**: ① ROADMAP v1.1 `merge_status: pending`(B03), ② develop→test merge 미실행(test stale `e5fd48d`, **16 commits behind**), ③ v1.1 잔여 완료 기준 live E2E·J01. B07 #4 신호(48차 교차 5 files) → COD 33차 `c98f98d` 커밋 CLEAN(신호 소멸·정식 Open 미등록). **FE-15 코드 스플릿 Fixed**(manualChunks — 단일 744.95 kB → 3 청크 최대 393.53 kB, vite 경고 해소).
> **PASS 금지 사유 (47차, 이력)**: ① ROADMAP v1.1 `merge_status: pending`(B03), ② develop→test merge 미실행(15 behind), ③ v1.1 잔여 완료 기준 live E2E·J01. B07 #3(45차 76 files) → `4be0938` 일괄 커밋 CLEAN(Fixed). 비차단 LOW: JS 청크 744.95 kB.
> **PASS 금지 사유 (45차, 이력)**: ① develop working tree **DIRTY 76 files**(B07 #3 — 43차 72→45차 +4: +2 untracked `FeeScheduleTable`(+test) + 2 modified·Recharts·설정 WIP 미커밋), ② ROADMAP v1.1 `merge_status: pending`(B03), ③ develop→test merge 미실행(test stale `e5fd48d`, 14 commits behind). **B05 선행 v1 merged 해소**. WT build/test **PASS**(749 modules·181/30) — **커밋 없이 PASS 불가**.
> **PASS 금지 사유 (43차)**: ① develop working tree **DIRTY 72 files**(B07 #3 — 41차 61→43차 +11: +10 untracked `BillingStatusConfirmModal`·`CopayRateTable`·`GuardianDailySummary`·`HealthAlertList`·`NhisImportGuidePanel` + Recharts·설정·감사 WIP 미커밋), ② ROADMAP v1.1 `merge_status: pending`(B03), ③ develop→test merge 미실행(test stale `e5fd48d`, 14 commits behind). **B05 선행 v1 merged 해소**. WT build/test **PASS**(748 modules·179/29) — **커밋 없이 PASS 불가**.
> **PASS 금지 사유 (41차)**: ① develop working tree **DIRTY 61 files**
> **PASS 금지 사유 (39차)**: ① develop working tree **DIRTY 60 files**
> **B07 recurrence #2 Fixed (25차 — `a84473f`)**: 23·24차 DIRTY 8 files(대시보드 실데이터 US-M02 WIP)가 `a84473f`(8 files +636/-170)로 **일괄 커밋** → working tree CLEAN, HEAD build 111·npm test 13/5 PASS(이관 규율 6·7 PASS, FE-7 충족). `dashboardWidgets.js`·`dashboardWidgets.test.js`가 develop HEAD에 PRESENT.
> **SEC-008 Fixed (25차 — `ed1bf22`)**: 24차 `npm audit 5 vuln(1 critical)`(esbuild/vite/vitest dev chain) → vite `^6.4.3`·vitest `^4.1.8`·`overrides.esbuild ^0.25.0` 업그레이드로 **develop `npm audit` 0 vulnerabilities**(high·all). prod 번들·테스트 회귀 없음(build 111·test 13/5 PASS).
> **HEAD Fixed 유지 (25차)**: `ed1bf22` HEAD 산출물(H04·M01·SEC-005·H03·US-UX-01·routeAccess·ThemeToggle·tokens.css·US-M02 대시보드 위젯) — 이관 규율 5 **PRESENT**(false Fixed 0건).
> **⚠ 범위 관측**: v1.2 P0(`a72e249`·`a84473f`) + UXD 10·11차(`5656e19`·`2d742b3`)가 v1.1 merge 전 develop 선행 커밋(8 ahead). v1.1 develop→test merge 시 **동반 흡수**(결정 52).

---

## 2. 브랜치·커밋 정합

| # | 항목 | 기대 | 실제 | 결과 |
|---|------|------|------|------|
| F-01 | develop → test 커밋 동기화 (v1.1) | v1.1 merged 후 test = merged HEAD | test **`4f71543`** (= v1.1 merged) · develop **`e0eaf32`** (**2 v1.2 ahead**) | **PASS** (v1.1) |
| F-02 | develop working tree clean | 커밋만으로 검증 가능 | **CLEAN** (0 dirty) | **PASS** |
| F-03 | test working tree clean | clean | clean | PASS |
| F-04 | ROADMAP v1.1 `merge_status` | `merged` | **`merged`** @ test `4f71543` | **PASS** |
| F-05 | ROADMAP v1 선행 merge | `merged` | `merged` (ROADMAP) — backend test stale | **PARTIAL** |
| F-06 | Baseline HEAD @ workspace | develop `7170b2a`+ | develop **`4f71543`** (+4 commits) | **PASS** |
| F-07 | SEC-D12 ProtectedRoute @ HEAD | HEAD PRESENT | **`ProtectedRoute.jsx`(src/auth)·App.jsx 래핑 PRESENT** @ `4f71543` | **PASS** |
| F-08 | H04 Must API + J02 GuardianPortal REST @ HEAD (이관 규율 5) | HEAD PRESENT | **`services.js`·Must pages·`GuardianPortalPage`·`pilotChecklist`·`pilotPageFlows`·7-role tests PRESENT** @ `4f71543` | **PASS** |
| F-09 | FE-22 live E2E harness + preconditions @ HEAD (이관 규율 5) | HEAD PRESENT | **`src/e2e/*`·`liveConfig.js`(fail-fast)·`vitest.live.config.js` PRESENT** @ `4f71543` | **PASS** (run post-merge) |
| F-10 | UXD SideNav 2-tier @ HEAD | HEAD PRESENT | **`src/layout/SideNav.jsx`(+test)·`AppShell.jsx`·`navConfig.js` PRESENT** @ `f64e1dd` | **PASS** |

---

## 3. 빌드·테스트

### 3-1. test 브랜치 `4f71543` (in `src/frontend-test` — 69차 TSR 실측)

| # | 항목 | 명령 | 결과 | 비고 |
|---|------|------|------|------|
| T-01 | Production build | `npm run build` | **PASS** | Vite 6.4.3, **86 modules**, JS 210.46 kB gzip 66.20 kB, CSS 27.27 kB |
| T-02 | Unit/component test | `npm test` (`vitest run`) | **PASS** | vitest 4.1.8, **58 tests/18 files** |
| T-03 | npm audit | `npm audit` | **PASS** | **0 vulnerabilities** |
| T-04 | dist 산출물 | `dist/` | JS 210.46 kB + CSS 27.27 kB | v1.1 MVP merged |
| T-05 | SEC-005 메모리 세션 | `git show HEAD:src/auth/AuthContext.jsx` | **PASS** | localStorage/sessionStorage **0건** |
| T-06 | HEAD artifacts (이관 규율 5) | `git cat-file -e HEAD:<path>` | **PASS** | ProtectedRoute·services.js·SideNav·pilotChecklist·FE-22 **PRESENT** |

### 3-2-67. develop `4f71543` HEAD (in `src/frontend` — read-only 검증, 67차, **CLEAN**)

| # | 항목 | 명령 | 결과 | 비고 |
|---|------|------|------|------|
| D-01 | Production build (HEAD) | `npm run build` | **PASS** | **86 modules**, vite 6.4.3, JS 210.46 kB gzip 66.20 kB, CSS 27.27 kB |
| D-02 | Unit/component test (HEAD) | `npm test` (`vitest run`) | **PASS** | vitest 4.1.8, **58 tests/18 files** (65차 46/13 → +12/+5 — SideNav·Tabs·FilterChips·BranchSwitcher·LogoutButton 등) |
| D-03 | develop HEAD artifacts | `git cat-file -e HEAD:<path>` | **PASS** | Must API·guardian REST/J01/J02·SideNav·AppShell·FE-22 e2e+liveConfig·ProtectedRoute **PRESENT** |
| D-04 | develop working tree clean | `git status --porcelain` | **PASS** | **0 dirty** |
| D-05 | HEAD route protection (SEC-D12) | `git show HEAD:src/App.jsx` | **PASS** | 라우트 **ProtectedRoute** 래핑 |
| D-06 | npm audit (develop HEAD) | `npm audit` | **PASS** | **0 vulnerabilities** |
| D-07 | SEC-005 메모리 세션 | `git show HEAD:src/auth/AuthContext.jsx` | **PASS** | localStorage/sessionStorage **0건** |
| D-08 | FE-22 live harness + preconditions | `liveConfig.js` + vite exclude | **PASS** | `LIVE_E2E=1` 시 env fail-fast · 실 run post-merge(결정 73) |

> **67차**: develop HEAD `4f71543` **CLEAN** · 58/18 PASS · audit **0** · UXD SideNav·FE-22 preconditions develop HEAD 반영. **PASS 금지** = B03/SEC-D14 merge 미실행(ROADMAP ready).

### 3-2-65. develop `d592a17` HEAD (in `src/frontend` — read-only 검증, 65차, **CLEAN**, 이력)

| # | 항목 | 명령 | 결과 | 비고 |
|---|------|------|------|------|
| D-01 | Production build (HEAD) | `npm run build` | **PASS** | **75 modules**, vite 6.4.3, JS 209.19 kB gzip 65.68 kB, CSS 24.45 kB |
| D-02 | Unit/component test (HEAD) | `npm test` (`vitest run`) | **PASS** | vitest 4.1.8, **46 tests/13 files** (63차 37/9 → +9/+4 — GuardianPortalPage·GuardianInvitationAcceptPage·GuardianInvitationList·guardian REST) |
| D-03 | develop HEAD artifacts | `git cat-file -e HEAD:<path>` | **PASS** | `services.js`·`GuardianPortalPage`(+test)·`ClientDetailPage`·`Alert.jsx`·`PublicAuthLayout.jsx`·`pilotChecklist`·`pilotPageFlows`·7-role·`ProtectedRoute` + `src/e2e/*`·`vitest.live.config.js` **PRESENT** |
| D-04 | develop working tree clean | `git status --porcelain` | **PASS** | **0 dirty** |
| D-05 | HEAD route protection (SEC-D12) | `git show HEAD:src/App.jsx` | **PASS** | 라우트 **ProtectedRoute** 래핑 |
| D-06 | npm audit (develop HEAD) | `npm audit` | **PASS** | **0 vulnerabilities** (vite 6.4.3·vitest 4.1.8) |
| D-07 | SEC-005 메모리 세션 | `git show HEAD:src/auth/AuthContext.jsx` | **PASS** | localStorage/sessionStorage **0건** |
| D-08 | FE-22 live harness 게이팅 | `vite.config.js` test.exclude | **PASS** | `src/e2e/**` 기본 `npm test` 제외 · 별도 `test:live-e2e`(LIVE_E2E) — 실 run 은 backend merge 후 |

> **65차**: develop HEAD `d592a17` **CLEAN** · 46/13 PASS · audit **0** · guardian REST/J01/J02·tone Alert a11y·**FE-22 live E2E harness** develop HEAD 반영. **PASS 금지** = B03/SEC-D14 merge 게이트(라이브 E2E run 은 develop→test merge·backend v1 test 승격·LIVE_E2E 환경 후).

### 3-2-63. develop `811aef3` HEAD (in `src/frontend` — read-only 검증, 63차, **CLEAN**)

| # | 항목 | 명령 | 결과 | 비고 |
|---|------|------|------|------|
| D-01 | Production build (HEAD) | `npm run build` | **PASS** | **74 modules**, vite 6.4.3, JS 205.76 kB gzip 65.05 kB, CSS 24.45 kB |
| D-02 | Unit/component test (HEAD) | `npm test` (`vitest run`) | **PASS** | vitest 4.1.8, **35 tests/9 files** (61차 6/2 → +29/+7 — pilotChecklist·pilotPageFlows·sevenRoleJwtLogin·sevenRoleRouteGuard·roleHomePaths 등) |
| D-03 | develop HEAD artifacts | `git cat-file -e HEAD:<path>` | **PASS** | `services.js`·`pilotChecklist.js`(+test)·`pilotPageFlows.test.jsx`·`sevenRoleJwtLogin/RouteGuard.test.jsx`·`sevenRoleRouteMatrix.js`·Must pages·`ProtectedRoute.jsx`(src/auth)·`AuthContext.jsx` **PRESENT** |
| D-04 | develop working tree clean | `git status --porcelain` | **PASS** | **0 dirty** |
| D-05 | HEAD route protection (SEC-D12) | `git show HEAD:src/App.jsx` | **PASS** | 5+ 라우트 **ProtectedRoute** 래핑 |
| D-06 | npm audit (develop HEAD) | `npm audit` | **PASS** | **0 vulnerabilities** — SEC-008 develop HEAD 해소 (vite 6.4.3·vitest 4.1.8, 61차 4 vuln→0) |
| D-07 | SEC-005 메모리 세션 | `git show HEAD:src/auth/AuthContext.jsx` | **PASS** | localStorage/sessionStorage **0건** |

> **63차**: develop HEAD `811aef3` **CLEAN** · 35/9 PASS · audit **0**(SEC-008 해소) · H04 Must API·R-04a 7-role·R-05 pilotPageFlows develop HEAD 반영. **PASS 금지** = B03 merge 게이트(라이브 E2E·J01 백엔드 API).

### 3-2. develop `e043eac` HEAD (in `src/frontend` — read-only 검증, 61차, **CLEAN**, 이력)

| # | 항목 | 명령 | 결과 | 비고 |
|---|------|------|------|------|
| D-01 | Production build (HEAD) | `npm run build` | **PASS** | **65 modules**, vite 5.4.21, JS 177.97 kB gzip 58.35 kB, CSS 24.46 kB |
| D-02 | Unit/component test (HEAD) | `npm test` (`vitest run`) | **PASS** | vitest 1.6.1, **6 tests/2 files** — ProtectedRoute 3 · MaskedPhone 3 |
| D-03 | develop HEAD artifacts | `git cat-file -e HEAD:<path>` | **PASS** | ProtectedRoute·AuthContext·App.jsx·http.js·authApi.js **PRESENT** · services.js·pilotPageFlows **ABSENT** |
| D-04 | develop working tree clean | `git status --porcelain` | **PASS** | **0 dirty** |
| D-05 | HEAD route protection (SEC-D12) | `git show HEAD:src/App.jsx` | **PASS** | `/dashboard`·`/platform`·`/clients` 등 **ProtectedRoute** 래핑 |
| D-06 | npm audit (develop HEAD) | `npm audit` | **FAIL** (non-blocking) | **4 vuln**(3 moderate·1 critical) — vitest 1.6.1 dev chain · SEC-008 upgrade 잔여 |

> **61차**: develop HEAD **CLEAN** · test stale. develop 6/6 PASS · MaskedPhone 마스킹 정합. **PASS 금지** = B03 + v1.1 완료 기준.

### 3-2-57. develop `d5654c0` working tree (in `src/frontend` — read-only 검증, 57차, **DIRTY 20 files**, TSR57 baseline — workspace 미반영)

| # | 항목 | 명령 | 결과 | 비고 |
|---|------|------|------|------|
| D-01 | Production build (WT) | `npm run build` | **PASS** | **758 modules**, vite 6.4.3, 3 청크: react-vendor 166.34·index 190.72·recharts 393.53 kB, CSS 52.85 kB |
| D-02 | Unit/component test (WT) | `npm test` (`vitest run`) | **FAIL** | vitest 4.1.8, **209 tests/44 files — 1 FAIL** (`GuardianListCard.test.jsx` MaskedPhone 마스킹, **FE-7 위반**) |
| D-03 | develop HEAD @ `d5654c0` | `git cat-file -e HEAD:<path>` | **PASS** | HEAD Fixed 산출물 PRESENT (규율 5) · WT-only `DateInput`·`GuardianInvitationList`·`GuardianListCard.test` **HEAD ABSENT** |
| D-04 | develop working tree clean | `git status --porcelain` | **FAIL** | **20 dirty** (14M+6U — B07 recurrence #6) |
| D-05 | **npm audit (develop WT)** | `npm audit` / `--audit-level=high` | **PASS** | **0 vulnerabilities** (high·all) |

> **57차**: develop working tree **DIRTY**이므로 D-01/D-02/D-05는 develop WT 직접 실측. WIP 범위: `DateInput.jsx`(+test)·`GuardianInvitationList.jsx`(+test)·`ClientPhotoField.test.jsx`·`GuardianListCard.test.jsx`·`ClientDetailPage`·`ClientFormPage`·`GuardianInviteModal`·`GuardianListCard`·`LoginHistoryPanel`·`AuditLogPanel`·`ClientPhotoField`·`PaymentRecordModal`(+test)·`services.js`·`GuardianInvitationAcceptPage`(+test)·`components.css`·`index.js`. **테스트 FAIL·dirty-tree — PASS 금지**.

### 3-2-53. develop `d5654c0` HEAD (in `src/frontend` — read-only 검증, 53차, **CLEAN**, 이력)

| # | 항목 | 명령 | 결과 | 비고 |
|---|------|------|------|------|
| D-01 | Production build (HEAD) | `npm run build` | **PASS** | **756 modules**, vite 6.4.3, 3 청크: react-vendor 166.34·index 186.68·recharts 393.53 kB, CSS 52.52 kB |
| D-02 | Unit/component test (HEAD) | `npm test` (`vitest run`) | **PASS** | vitest 4.1.8, **199 tests/40 files** (52차 WT 194/38 → +5/+2, FE-7 회귀 없음) |
| D-03 | develop HEAD @ `d5654c0` | `git cat-file -e HEAD:<path>` | **PASS** | `LogoutButton.jsx`·`GuardianInvitationAcceptPage.jsx`·`GuardianInvitationAcceptForm.jsx`·`PublicAuthLayout.jsx`·`BillingPage.layout.test.jsx`·`LogoutButton.test.jsx`·`services.js`(acceptGuardianInvitationApi) + 기존 Fixed **전부 PRESENT** (이관 규율 5) |
| D-04 | develop working tree clean | `git status --porcelain` | **PASS** | **0 dirty** (COD 35차 `d5654c0` 25 files 일괄 커밋, **B07 #5 Fixed**) |
| D-05 | **npm audit (develop HEAD)** | `npm audit` / `--audit-level=high` | **PASS** | **0 vulnerabilities** (high·all) |

> **53차**: develop working tree **CLEAN**이므로 D-01/D-02/D-05는 develop HEAD `d5654c0` 직접 실측. COD 35차 변경: `LogoutButton.jsx`(+test 67줄)·`GuardianInvitationAcceptPage.jsx`(167줄 J01 수락 UI)·`GuardianInvitationAcceptForm.jsx`·`PublicAuthLayout.jsx`·`BillingPage.layout.test.jsx`·`AuthContext`(logout) + `services.js`(acceptGuardianInvitationApi +19줄)·Recharts·ds-* 정리 25 files +823/-57. 테스트 수 199/40(52차 WT 194/38 대비 +5/+2). **B07 recurrence #5 Fixed·Open 0건**. **이관 규율 5·6·7·8 PASS**.

### 3-2-52. develop `0b9b001` working tree (in `src/frontend` — read-only 검증, 52차, **DIRTY 20 files**, 이력)

| # | 항목 | 명령 | 결과 | 비고 |
|---|------|------|------|------|
| D-01 | Production build (WT) | `npm run build` | **PASS** | **754 modules**, vite 6.4.3, 3 청크: react-vendor 166.34·index 185.35·recharts 393.53 kB, CSS 52.24 kB |
| D-02 | Unit/component test (WT) | `npm test` (`vitest run`) | **PASS** | vitest 4.1.8, **194 tests/38 files** (50차 187/35 → +7/+3) |
| D-03 | develop HEAD @ `0b9b001` | `git cat-file -e HEAD:<path>` | **PASS** | HEAD Fixed 산출물 PRESENT (규율 5) · WT-only `LogoutButton`·`GuardianInvitationAcceptPage`·`BillingPage.layout.test` **ABSENT** |
| D-04 | develop working tree clean | `git status --porcelain` | **FAIL** | **20 dirty** (15M+5U — B07 recurrence #5) |
| D-05 | **npm audit (develop WT)** | `npm audit` / `--audit-level=high` | **PASS** | **0 vulnerabilities** (high·all) |

> **52차**: develop working tree **DIRTY**이므로 D-01/D-02/D-05는 develop WT 직접 실측. WIP 범위: `LogoutButton`(+test)·`BillingPage.layout.test.jsx`·`GuardianInvitationAcceptPage`(+test — J01)·`AuthContext`·Recharts·청구/보호자 페이지. **테스트 PASS ≠ 이관 PASS**.

### 3-2-50. develop `0b9b001` HEAD (in `src/frontend` — read-only 검증, 50차, **CLEAN**, 이력)

| # | 항목 | 명령 | 결과 | 비고 |
|---|------|------|------|------|
| D-01 | Production build (HEAD) | `npm run build` | **PASS** | **752 modules**, vite 6.4.3, **3 청크 분리**: react-vendor 166.34·index 181.88·recharts 393.53 kB, CSS 52.95 kB (FE-15 코드 스플릿) |
| D-02 | Unit/component test (HEAD) | `npm test` (`vitest run`) | **PASS** | vitest 4.1.8, **187 tests/35 files** (49차 186/34 → +1/+1 `AttendancePage.layout.test.jsx`) |
| D-03 | develop HEAD @ `0b9b001` | `git cat-file -e HEAD:<path>` | **PASS** | Recharts·FE-12/13/14·`vite.config.js`(FE-15)·ds-* 전환·`AttendancePage.layout.test.jsx` + 기존 Fixed **전부 PRESENT** (규율 5) |
| D-04 | develop working tree clean | `git status --porcelain` | **PASS** | **0 dirty** (COD 34차 `0b9b001` 커밋 반영, B07 #3·#4 신호 전부 소멸) |
| D-05 | **npm audit (develop HEAD)** | `npm audit` / `--audit-level=high` | **PASS** | **0 vulnerabilities** (high·all) |

> **50차**: develop working tree **CLEAN**이므로 D-01/D-02/D-05는 develop HEAD `0b9b001` 직접 실측. COD 34차 변경: `AttendanceAbsentModal`·`BatchProgressSteps`·`CheckoutModal`·`FeeRateHistoryPanel`·`HealthAbnormalBanner`·`MedicationDuplicateAlert`·`PasswordResetRequestModal`·`PlatformOrgDetailModal`·`SessionTimeoutModal` — 인라인 style→ds-* 유틸리티 전환 + `AttendancePage.layout.test.jsx` 레이아웃 회귀 자동화 추가. **FE-15 코드 스플릿 Fixed 유지**: react-vendor 166.34·index 181.88·recharts 393.53 kB (최대 <500 kB). 테스트 수 187/35(49차 186/34 대비 +1/+1).

---

## 4. develop HEAD Fixed 정합 (이관 규율 5 — @ `d5654c0`, 53차)

| 산출물 | develop HEAD `d5654c0` | Fixed id | 판정 |
|--------|------------------------|----------|------|
| `ProtectedRoute.jsx` + `App.jsx` 7역할 가드 | PRESENT | H03·SEC-003 | **PASS** |
| `src/api/http.js`·`services.js` (+ acceptGuardianInvitationApi +19줄) | PRESENT | H04·FE-17(J01) | **PASS** |
| `package.json` test·Vitest 4.1.8·`*.test.jsx`×40 | PRESENT | M01 | **PASS** (HEAD 199/40 PASS) |
| `AuthContext.jsx` 메모리 세션 (localStorage/sessionStorage 0건) | PRESENT | SEC-005 | **PASS** |
| `public/favicon.*`·`index.html` | PRESENT | US-UX-01 | **PASS** |
| `src/auth/routeAccess.js` 중앙 가드 | PRESENT | v1.2 P0 | **PASS** |
| `src/components/ui/ThemeToggle.jsx`·`src/styles/tokens.css` | PRESENT | UXD 11차 다크모드 | **PASS** |
| `src/pages/dashboardWidgets.js`·`dashboardWidgets.test.js` | PRESENT | US-M02·B07 #2 | **PASS** |
| `package.json` vite 6·vitest 4·esbuild override | PRESENT | SEC-008 | **PASS** (npm audit 0건) |
| `src/components/ui/LogoutButton.jsx`·`LogoutButton.test.jsx` | PRESENT (`d5654c0`) | FE-17·B07 #5 | **PASS** (53차 신규 커밋) |
| `src/pages/GuardianInvitationAcceptPage.jsx`·`GuardianInvitationAcceptForm.jsx` | PRESENT (`d5654c0`) | FE-17·J01 수락 UI | **PASS** (53차 신규 커밋) |
| `src/components/ui/PublicAuthLayout.jsx` | PRESENT (`d5654c0`) | FE-17 | **PASS** (53차 신규 커밋) |
| `src/pages/BillingPage.layout.test.jsx` | PRESENT (`d5654c0`) | FE-17 레이아웃 회귀 | **PASS** (53차 신규 커밋) |
| develop working tree clean | **CLEAN** (0 dirty) | B07 | **PASS** (53차 — COD 35차 d5654c0, B07 #5 Fixed) |

---

## 5. ROADMAP v1.1 완료 기준 대조 (HEAD = `811aef3`, clean, 63차)

| # | ROADMAP 완료 기준 | 검증 방법 | 결과 | 비고 |
|---|-------------------|-----------|------|------|
| R-01 | `npm run build` 성공 | T-01/D-01 | **PARTIAL** | test 36 PASS / HEAD **74 PASS**(vite 6.4.3) — merge 후 동등 예상 |
| R-02 | 7역할 화면·메뉴·권한 분리 | App.jsx·ProtectedRoute·`sevenRoleRouteMatrix.js` | **PASS** | HEAD 가드·7역할 매트릭스 PRESENT |
| R-03 | ProtectedRoute·역할 가드 (H03) | HEAD `src/auth/ProtectedRoute.jsx` | **PASS** | |
| R-04 | Must 화면 REST API (H04) | HEAD `services.js`·Must pages | **PASS** | `services.js`(+144)·AttendancePage·BillingPage·ClientDetailPage·HealthPage·NHISImportPage·ReconciliationPage REST 연동 PRESENT |
| R-05 | Must 화면 API E2E P1–P8 | `pilotChecklist.test.js` + `pilotPageFlows.test.jsx` | **PARTIAL** | fetch-mock + 페이지 단위 RTL E2E **develop HEAD 반영**; 라이브 E2E는 merge·backend v1 test 승격 후 |
| R-04a | 7역할 JWT 로그인·라우트 가드 E2E | `sevenRoleJwtLogin.test.jsx`·`sevenRoleRouteGuard.test.jsx` | **PARTIAL** | Vitest 자동화 PRESENT; 라이브 백엔드 E2E는 merge·backend 후 |
| R-06 | NHIS reconciliation UI | HEAD `ReconciliationPage.jsx` | **PASS** | |
| R-07 | 보호자 초대·수락 UI (J01·J02) | HEAD·`GuardianInvitationList.jsx`(a11y)·`GuardianInvitationAcceptPage` | **PARTIAL** | J01 UI HEAD PRESENT; **J01 백엔드 초대 API 스텁** 유지 (B03 BLOCK) |
| R-08 | Vitest `npm test` (M01) | D-02 | **PARTIAL** | HEAD **35/9 PASS**(pilotChecklist·pilotPageFlows·7-role 포함); P1–P8 라이브·전체 회귀 잔여 |
| R-09 | JWT 메모리 세션 (SEC-005) | HEAD `AuthContext.jsx` | **PASS** | localStorage/sessionStorage 0건 |
| R-10 | 파비콘 (US-UX-01) | HEAD | **PASS** | `c3b863e` favicon restore |
| R-11 | develop working tree clean (B07) | `git status` | **PASS** | **CLEAN** (0 dirty) |
| R-12 | merge_status ready (B03) | ROADMAP | **FAIL** | `pending` (잔여 단일 BLOCK) |
| R-13 | 선행 v1 merged (B05) | backend v1 | **PASS** | `merged` |
| R-14 | (SEC-008) npm audit 0 vuln | D-06 | **PASS** | develop HEAD **0 vulnerabilities** (vite 6.4.3·vitest 4.1.8) |

> **63차**: 61차 FAIL/ABSENT였던 **R-04(H04)·R-05·R-04a·R-08(M01)·R-14(SEC-008)** 이 `811aef3`에서 **develop HEAD 반영**(PASS 또는 PARTIAL). 잔여 FAIL = **R-12(B03 merge_status)** 단일 — Must 라이브 E2E·J01 백엔드 API는 merge·backend v1.1 J01 API 후.

---

## 5-53. ROADMAP v1.1 완료 기준 대조 (HEAD = `d5654c0`, clean, 53차, 이력)

| # | ROADMAP 완료 기준 | 검증 방법 | 결과 | 비고 |
|---|-------------------|-----------|------|------|
| R-01 | `npm run build` 성공 | T-01/D-01 | **PARTIAL** | test 36 PASS / HEAD **756 PASS** (merge 후 동등 예상) |
| R-02 | 7역할 화면·메뉴·권한 분리 | App.jsx·가드·SideNav·routeAccess | **PASS** | HEAD 2단 SideNav·routeAccess 커밋 |
| R-03 | ProtectedRoute·역할 가드 (H03) | HEAD | PASS | |
| R-04 | Must 화면 REST API (H04) | HEAD api/ | **PASS** | |
| R-05 | Must 화면 API E2E P1–P8 | `pilotChecklist.test.js` + `pilotPageFlows.test.jsx` | **PARTIAL** | **라우팅 fetch-mock + 페이지 단위 RTL E2E 진전**; 라이브 E2E는 backend v1 test 미승격 |
| R-04a | **7역할 JWT 로그인·라우트 가드 E2E** | `sevenRoleJwtLogin.test.jsx`·`sevenRoleRouteGuard.test.jsx` | **PARTIAL** | Vitest 자동화 +93 tests(AuthProvider login 7역할·ProtectedRoute 매트릭스); 라이브 백엔드 E2E는 backend v1 test 승격 후 |
| R-06 | NHIS reconciliation UI | HEAD | **PASS** | |
| R-07 | 보호자 초대·수락 UI (J01·J02) | HEAD·`GuardianInvitationAcceptPage.jsx`·`GuardianInviteModal.test.jsx` | **PARTIAL** | **COD 35차 `d5654c0` — J01 수락 UI(`GuardianInvitationAcceptPage.jsx`·`GuardianInvitationAcceptForm.jsx`·`PublicAuthLayout.jsx`) + `acceptGuardianInvitationApi`(`services.js`) HEAD PRESENT**; **J01 백엔드 초대 API 스텁** 유지 (B03 BLOCK) |
| R-08 | Vitest `npm test` (M01) | D-02 | **FAIL** | WT **209/44 — 1 FAIL** (57차, `GuardianListCard.test.jsx` FE-7) |
| R-09 | JWT 메모리 세션 (SEC-005) | HEAD | **PASS** | AuthContext localStorage/sessionStorage 0건 |
| R-10 | 파비콘 (US-UX-01) | HEAD | **PASS** | |
| R-11 | develop working tree clean (B07) | `git status` | **FAIL** | 57차 **DIRTY** (20 files — B07 recurrence #6 Planned) |
| R-12 | merge_status ready (B03) | ROADMAP | **FAIL** | `pending` (잔여 단일 BLOCK) |
| R-13 | 선행 v1 merged (B05) | backend v1 | **PASS** | `merged` (test `@e8750d2`) |
| R-14 | (LOW) 번들 코드 스플릿 (FE-15) | D-01 | **PASS** | `manualChunks` 3 청크 분리 (최대 393.53 kB, vite 경고 해소) |

---

## 6. develop working tree (QA-B07 — 25차 recurrence #2 Fixed)

| 항목 | 21차(19:22) | 23차(20:17) | 24차(21:13) | 25차(21:32) |
|------|-------------|-------------|-------------|-------------|
| modified | **0** | 6 | 6 | **0** |
| untracked | **0** | 2 | 2 | **0** |
| total | **0 (CLEAN)** | **8 (DIRTY)** | **8 (DIRTY)** | **0 (CLEAN)** |
| HEAD build modules | 110 | 112(WT) | 114(WT) | **111** |
| HEAD npm test | 10/4 PASS | 13/5 PASS(WT) | 13/5 PASS(WT) | **13/5 PASS** |
| npm audit | — | 0h·2mod | **5 vuln(1 critical)** | **0 vulnerabilities** |
| 상태 | CLEAN (B07 해소) | DIRTY (recurrence #2 Open→Planned) | DIRTY (recurrence #2 Planned) | **CLEAN (recurrence #2 Fixed)** |

**25차 clean 회복 경위**: 23·24차 DIRTY 8 files(대시보드 실데이터 US-M02 WIP)를 COD 17차 `a84473f`(8 files +636/-170)로 **일괄 커밋** → working tree CLEAN. develop HEAD 그대로 `npm run build` 111 modules·`npm test` 13/5 PASS(FE-7 충족·회귀 없음). 추가로 `ed1bf22`로 SEC-008 dev 의존성 업그레이드.

> **SEC-008 해소 (25차 — `ed1bf22`)**: 24차 `5 vulnerabilities(4 moderate·1 critical)`(esbuild/vite/vitest dev chain) → vite `^6.4.3`·vitest `^4.1.8`·`overrides.esbuild ^0.25.0` 업그레이드로 **develop `npm audit` 0 vulnerabilities**(high·all). prod 번들·테스트 회귀 없음. test 브랜치는 stale(vite 5.4.21·2 moderate) — merge 시 동반 해소.

---

## 7. QA_FEEDBACK 연계 (frontend)

| id | severity | 상태 | 요약 |
|----|----------|------|------|
| QA-20260606-B03 | BLOCK | **Planned** | v1.1 merge_status pending · develop **7 ahead** · Must 라이브 E2E·J01 백엔드 API 잔여 |
| QA-20260606-H04 | HIGH | **develop HEAD 반영 (`811aef3`)** | `services.js`·Must pages·pilotChecklist·pilotPageFlows develop HEAD PRESENT — 라이브 E2E는 merge 후 |
| QA-20260606-M01 | MEDIUM | **PARTIAL (`811aef3`)** | vitest 35/9 PASS(61차 6 → +29) — P1–P8 라이브·전체 회귀 잔여 |
| SEC-20260606-008 | MEDIUM | **develop HEAD 해소 (`811aef3`)** | npm audit **0 vulnerabilities**(vite 6.4.3·vitest 4.1.8, 61차 4→0) |
| QA-20260607-H05 | HIGH | **Planned (partial)** | MaskedPhone 마스킹 정합 @ HEAD · GuardianListCard/J01 UI(FE-18) live 잔여 |

> **frontend Open 0건** — SEC-D12·QA-B11·SEC-D11 **Fixed @ 43차 baseline**. **H04·M01·SEC-008 develop HEAD 반영(`811aef3`)** — **Planned BLOCK = B03 merge 게이트 단일**(Must 라이브 E2E·J01 백엔드 API · backend merge 4커밋 동반).

---

## 8. operation 승격 전 필수 조치 (planner → coder)

> **63차 — H04·M01·R-04a·R-05·SEC-008 develop HEAD 반영(`811aef3`)으로 1·2·4항 해소. 잔여 = merge 게이트(B03) + J01 백엔드 API + 라이브 E2E.**

1. ~~**v1.1 Must API·Must pages**~~ **Fixed @ `811aef3`** — `services.js`·Must 화면 REST 연동 develop HEAD 반영 (H04).
2. ~~**Vitest 회귀 확대**~~ **PARTIAL @ `811aef3`** — pilotPageFlows·pilotChecklist·sevenRoleJwt/Guard develop HEAD 반영(35/9); P1–P8 라이브·전체 회귀는 merge·backend 후 (M01·R-05).
3. ~~**SEC-008**~~ **Fixed @ `811aef3`** — vite 6.4.3·vitest 4.1.8 upgrade, develop audit **0 vuln**.
4. **J01 보호자 초대 백엔드 API 연동** — 현재 `services.js` 헬퍼·스텁 → backend v1.1 J01 API(`guardian_invitations`) 후 라이브 연결 (R-07).
5. **Must API 라이브 E2E** — backend v1 test 승격 + merge 후 실 백엔드 대상 P1–P8 (R-05).
6. v1.1 완료 기준 잔여 `[x]` → `merge_status: ready` → develop→test merge (**7 commits**).
7. merge 후 test clean tree build·`npm test`·audit 재검증 → TSR PASS.

---

## 9. 서명

| 역할 | id | 판정 | 일시 |
|------|-----|------|------|
| QA·이관 | TSR | **PASS** (77차 — test **`4f71543`** 불변·**58/18 PASS**·**86 modules**·audit **0**·develop **`4957bd3` +11 v1.2 CLEAN**·**130/44 PASS**·**123 modules**·audit 0·이관 규율 5 PRESENT·SEC-005 0건·Open **0**) | 2026-06-07T23:30:00+00:00 |
| QA·이관 | TSR | **PASS** (76차 — test **`4f71543`** 불변·**58/18 PASS**·**86 modules**·audit **0**·develop **`c5708c7` +9 v1.2 CLEAN**·**115/40 PASS**·**120 modules**·audit 0·이관 규율 5 PRESENT·SEC-005 0건·Open **0**) | 2026-06-07T22:27:00+00:00 |
| QA·이관 | TSR | **PASS** (75차 — test **`4f71543`** 불변·**58/18 PASS**·**86 modules**·audit **0**·develop **`a627c6d` +8 v1.2 CLEAN**·**110/36 PASS**·**117 modules**·audit 0·이관 규율 5 PRESENT·SEC-005 0건·Open **0**) | 2026-06-07T21:24:00+00:00 |
| QA·이관 | TSR | **PASS** (73차 — test **`4f71543`** 불변·**58/18 PASS**·**86 modules**·audit **0**·develop **`9bdf59f` +6 v1.2 CLEAN**·이관 규율 5 PRESENT·SEC-005 0건·Open **0**) | 2026-06-07T20:21:00+00:00 |
| QA·이관 | TSR | **PASS** (71차 — test **`4f71543`** 불변·**58/18 PASS**·**86 modules**·audit **0**·develop **`42f48e1` +4 v1.2 CLEAN**·**89/28 PASS**·**114 modules**·이관 규율 5 PRESENT·SEC-005 0건·Open **0**) | 2026-06-07T19:20:00+00:00 |
| QA·이관 | TSR | **PASS** (69차 — v1.1 test **`4f71543` merged**·**58/18 PASS**·build **86 modules**·audit **0**·이관 규율 5 PRESENT·develop **`e0eaf32` +2 v1.2 CLEAN**·82/27 PASS·post-merge live E2E 권장·Open **0**) | 2026-06-07T18:12:00+00:00 |
| QA·이관 | TSR | **BLOCK** (67차 — develop **`4f71543` CLEAN**·**58/18 PASS**·build **86 modules**·audit **0**·UXD SideNav·FE-22 preconditions develop HEAD 반영·test **36 PASS/N/A**·develop **13 ahead**·ROADMAP **ready**·잔여 **B03/SEC-D14 merge 미실행**·Open **0**) | 2026-06-07T17:31:00+00:00 |
| QA·이관 | TSR | **BLOCK** (65차 — develop **`d592a17` CLEAN**·**46/13 PASS**·build **75 modules**·audit **0**·guardian REST+J01/J02·tone Alert a11y·**FE-22 live E2E harness** develop HEAD 반영·test **36 PASS/N/A**·develop **11 ahead**·잔여 **B03/SEC-D14 merge 게이트 단일**(live run gated)·Open **0**) | 2026-06-07T16:50:00+00:00 |
| QA·이관 | TSR | **BLOCK** (63차 — develop **`811aef3` CLEAN**·**35/9 PASS**·build **74 modules**·audit **0(SEC-008 해소)**·H04·M01·R-04a·R-05 **develop HEAD 반영**·test **36 PASS/N/A**·develop **7 ahead**·잔여 **B03 merge 게이트 단일**·Open **0**) | 2026-06-07T15:40:00+00:00 |
| QA·이관 | TSR | **BLOCK** (61차 — develop **`e043eac` CLEAN**·**6/6 PASS**·SEC-D12 HEAD **PASS**·test **36 PASS/N/A**·develop **3 ahead**·v1.1 완료 기준 **미충족**·Open **0**) | 2026-06-07T15:00:00+00:00 |
| QA·이관 | TSR | **BLOCK** (59차 — QA-B11·SEC-D12·develop WT DIRTY — **61차에서 baseline 해소**) | 2026-06-08T02:05:00+00:00 |
| QA·이관 | TSR | **BLOCK** (57차 — **B07 #6**(20 files DIRTY)·**H05 FE-7 FAIL**(209/210); WT build **758**·audit 0; 잔여 **B03 + B07 #6**; frontend **Open 1 HIGH**) | 2026-06-07T10:11:00+00:00 |
| QA·이관 | TSR | **BLOCK** (55차 — **B07 recurrence #6**(15 files DIRTY, WT build **758**·npm test **205/42**·audit 0, HEAD Fixed 규율 5 유효); 잔여 **B03 + B07 #6**; frontend **Open 1**) | 2026-06-07T09:29:08+00:00 |
| QA·이관 | TSR | **BLOCK** (53차 — **B07 #5 Fixed**(COD 35차 `d5654c0` CLEAN, HEAD build **756**·npm test **199/40**·audit 0, 규율 5 독립 검증 PASS); 잔여 **B03 단일**; frontend **Open 0**) | 2026-06-07T08:36:21+00:00 |
| QA·이관 | TSR | **BLOCK** (52차 — **B07 recurrence #5**(20 files DIRTY, WT build 754·npm test **194/38**·audit 0, HEAD Fixed 규율 5 유효); 잔여 **B03 + B07 #5**; frontend **Open 1**) | 2026-06-07T08:03:37+00:00 |
| QA·이관 | TSR | **BLOCK** (50차 — B07 #3·#4 소멸·FE-15 Fixed·CLEAN·187/35; B03 단일; Open 0) | 2026-06-07T07:17:37+00:00 |
| QA·이관 | TSR | **BLOCK** (47차 — **B07 #3 Fixed**(COD 31차 `4be0938`, working tree CLEAN, HEAD build 752·npm test 185/33·audit 0, 규율 5 독립 검증 PASS); 잔여 merge 게이트 **B03 단일**; B05 PASS; frontend Open 0) | 2026-06-07T14:45:00+09:00 |
| QA·이관 | TSR | **BLOCK** (45차 — B07 #3 dirty **76 files**·WT build 749·npm test 181/30·audit 0; B05 PASS; frontend Open 0) | 2026-06-07T14:02:36+09:00 |
| QA·이관 | TSR | **BLOCK** (43차 — B07 #3 dirty **72 files**·WT build 748·npm test 179/29·audit 0; B05 PASS; frontend Open 0) | 2026-06-07T13:27:22+09:00 |
| QA·이관 | TSR | **BLOCK** (41차 — B07 #3 dirty **61 files**·WT build 743·npm test 169/24·audit 0; B05 PASS; frontend Open 0) | 2026-06-07T12:52:35+09:00 |
| QA·이관 | TSR | **BLOCK** (39차 — B07 #3 dirty **60 files**·WT build 743·npm test 169/24·audit 0; B05 PASS; frontend Open 0) | 2026-06-07T12:09:00+09:00 |
| QA·이관 | TSR | **BLOCK** (37차 — B07 #3 dirty **44 files**·WT build 741·npm test 161/20·audit 0; B05 PASS; frontend Open 0) | 2026-06-07T11:30:00+09:00 |
| QA·이관 | TSR | **BLOCK** (35차 — B07 #3 dirty **26 files**·WT build 738·npm test 144/13·audit 0; B05 PASS; frontend Open 0) | 2026-06-07T01:50:00+00:00 |
| QA·이관 | TSR | **BLOCK** (33차 — B07 #3 dirty 18 files·WT build 736·npm test 142/12·audit 0; B05 PASS; Open 1) | 2026-06-07T01:16:00+00:00 |
| QA·이관 | TSR | **BLOCK** (31차 — B03·B05; COD `3fdc266`·UXD 14차, CLEAN, build 113·npm test 140/11; Open 0) | 2026-06-07T00:43:00+00:00 |
| QA·이관 | TSR | **BLOCK** (29차 — merge 게이트 단일 B03·B05; COD 20차 `57ff3c0` 7역할 JWT 로그인·라우트 가드 E2E 자동화 독립 검증, working tree CLEAN, HEAD build 112·**npm test 130/10 PASS**·audit 0건, 규율 5 PASS; R-04 Vitest 자동화 +93/+2 진전; frontend Open 0건) | 2026-06-06T23:31:00+00:00 |
| QA·이관 | TSR | **BLOCK** (27차 — merge 게이트 단일 B03·B05; COD 19차 `cc34f23` 파일럿 P1–P8·J01/J02 라우팅 자동화 독립 검증, working tree CLEAN, HEAD build 111·**npm test 32/7 PASS**·audit 0건, 규율 5 PASS; R-05·R-07 라우팅 자동화 진전; frontend Open 0건) | 2026-06-06T22:40:00+00:00 |
| QA·이관 | TSR | **BLOCK** (26차 — merge 게이트 단일 B03·B05; UXD 12차 `404a30e` LoginPage DS·Modal 포커스 트랩·고대비, working tree CLEAN, HEAD build 111·npm test 13/5 PASS·audit 0건) | 2026-06-06T22:20:00+00:00 |
| QA·이관 | TSR | **BLOCK** (25차 — merge 게이트 단일 B03·B05; **B07 recurrence #2 Fixed**(`a84473f` working tree CLEAN)·**SEC-008 Fixed**(`ed1bf22` npm audit 0건) 독립 검증; HEAD `ed1bf22` build 111·npm test 13/5 PASS; frontend Open 0건) | 2026-06-06T21:32:00+00:00 |
| QA·이관 | TSR | **BLOCK** (24차 — B07 recurrence #2 dirty 8 files(Planned) + merge 게이트 B03·B05; HEAD `2d742b3` Fixed 유효; **npm audit 에스컬레이션 SEC-008 신규 Open**) | 2026-06-06T21:13:00+00:00 |
| QA·이관 | TSR | **BLOCK** (23차 — B07 recurrence #2 dirty 8 files + merge 게이트 B03·B05; HEAD `5656e19` Fixed 유효) | 2026-06-06T20:17:00+00:00 |
| QA·이관 | TSR | **BLOCK** (21차 — merge 게이트 B03·B05 단일; B07 dirty-tree 해소) | 2026-06-06T19:22:00+00:00 |
| QA·이관 | TSR | **BLOCK** (19차 — B07 dirty 35 files + merge 게이트 B03·B05) | 2026-06-06T18:45:00+00:00 |
| QA·이관 | TSR | **BLOCK** (16차 — B07 악화 + merge 게이트 B03·B05) | 2026-06-06T18:07:00+00:00 |
