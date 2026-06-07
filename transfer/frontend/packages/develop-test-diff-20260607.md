<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-07T15:40:00+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-07T15:40 63차 재검증)

> **63차 재검증 (15:40) — develop `e043eac`→`811aef3`(+2커밋)·Must API pages·pilotChecklist·7-role·pilotPageFlows·SEC-008 develop HEAD 반영·CLEAN·35/9 PASS·74 modules·audit 0·잔여 BLOCK = B03 merge 게이트 단일·Open 0**: 61차(`e043eac` CLEAN·6/6 PASS·audit 4 vuln) 대비 develop HEAD `e043eac`→`f506c90`→`c3b863e`→`b87a8f5`→**`811aef3`**(baseline `c3b863e` 대비 +2커밋: `b87a8f5` US-J01 초대 행 스크린리더 레이블·**`811aef3`** Must API pages·pilot checklist·7-role tests·SEC-008), working tree **CLEAN**(0 dirty). **이관 규율 5 — develop HEAD 반영 확정**: `git cat-file -e HEAD:` `src/api/services.js`·`src/api/pilotChecklist.js`(+test)·`src/pages/pilotPageFlows.test.jsx`·`src/auth/sevenRoleJwtLogin.test.jsx`·`src/auth/sevenRoleRouteGuard.test.jsx`·`src/auth/sevenRoleRouteMatrix.js`·`src/pages/{AttendancePage,BillingPage,ClientDetailPage,ClientListPage,HealthPage,NHISImportPage,ReconciliationPage}.jsx`·`src/auth/ProtectedRoute.jsx`·`src/test/setupTests.js` **전부 PRESENT**. SEC-005 AuthContext localStorage/sessionStorage **0건**. develop HEAD `npm run build`(vite 6.4.3) **74 modules SUCCESS**(JS 205.76 kB gzip 65.05 kB, CSS 24.45 kB)·`npm test`(vitest 4.1.8) **35 tests/9 files PASS**(61차 6/2 → +29/+7)·`npm audit` **0 vulnerabilities**(high·all — **SEC-008 develop HEAD 해소**, 61차 4 vuln→0). test `@e5fd48d`(src/frontend-test) build **36 modules PASS**·`npm test` **N/A**(Missing script)·**7 behind**·audit 0h/2mod. **신규 Open 0건** — v1.1 H04 Must API·M01 vitest 확장·R-04a 7-role·R-05 pilotPageFlows·SEC-008 **develop HEAD 반영**(라이브 E2E·J01 백엔드 API는 merge·backend 후). 판정 **BLOCK**(B03 merge 게이트 단일).

## 커밋 수준 (63차)

- `develop` HEAD: `811aef3` (`feat(v1.1): Must API pages, pilot checklist, 7-role tests, SEC-008`)
- `test` HEAD: `e5fd48d` — 스켈레톤 (merge 미실행, **7 behind**)
- **test 7 commits behind develop**: `7c0ecdc`·`1d9a701`·`e043eac`·`f506c90`·`c3b863e`·`b87a8f5`·`811aef3`

## develop working tree (63차 — Must API pages·SEC-008 develop HEAD 반영·CLEAN)

| 항목 | 61차 (`e043eac`) | 63차 (`811aef3`) |
|------|------------------|------------------|
| modified | **0** | **0** |
| untracked | **0** | **0** |
| total | **0 (CLEAN)** | **0 (CLEAN)** |
| HEAD build modules | 65 (vite 5.4.21) | **74 (vite 6.4.3)** |
| HEAD npm test | 6/2 (vitest 1.6.1) | **35/9 (vitest 4.1.8)** |
| npm audit | 4 vuln (1 critical) | **0 (SEC-008 해소)** |

**경위 (`811aef3`, 22 files +1968/-752)**: Must API pages(`AttendancePage`·`BillingPage`·`ClientDetailPage`·`ClientListPage`·`HealthPage`·`NHISImportPage`·`ReconciliationPage`·`DashboardPage` REST 연동)·`src/api/services.js`(+144)·`pilotChecklist.js`(+test, P1–P8 fetch-mock)·`pilotPageFlows.test.jsx`(페이지 단위 RTL E2E)·`sevenRoleJwtLogin.test.jsx`·`sevenRoleRouteGuard.test.jsx`·`sevenRoleRouteMatrix.js`(7역할 매트릭스)·`setupTests.js` + `package.json`/`package-lock.json` vite `^6.4.3`·vitest `^4.1.8`(SEC-008). 직전 `b87a8f5` US-J01 `GuardianInvitationList` 행 액션 스크린리더 레이블. → 61차 FAIL/ABSENT였던 **H04·M01·R-04a·R-05·SEC-008 develop HEAD 반영**. 라이브 E2E·J01 백엔드 초대 API는 develop→test merge·backend 후.

## test 브랜치 (frontend-test, 63차 TSR 확인)

- `npm run build`: SUCCESS (36 modules, Vite 5.4.21, JS 165.43 kB) — 스켈레톤 (불변)
- `npm test`: N/A (Missing script @ e5fd48d)
- `npm audit`: 0 high, 2 moderate (stale vite 5.4.21 — SEC-008 fix 미머지)

## 판정 (63차)

**BLOCK** — merge 게이트 **B03 단일**(v1.1 merge_status pending·develop→test **7 commits** 미머지·잔여 완료 기준 Must **라이브 E2E**·J01 백엔드 API). develop HEAD clean build/test/audit PASS(74·35/9·0) + Must API·pilot·7-role·SEC-008 **develop HEAD 반영** — `merge_status: ready` 게이트만 잔존.

> **추가 관측 (15:46, coder 동시 진행)**: 검증 직후 develop **`811aef3`→`bb0cec4`**(+1커밋 `fix(v1.1): restrict billing route access to admin roles` — billing 라우트 admin RBAC·`roleNav` `STAFF_NAV` 분리). working tree **CLEAN**·`npm test` **37/9 PASS**·build **74 modules**·audit **0**·develop **8 ahead** of test. 판정 **BLOCK** 불변(B03). coder 동시 진행 중.

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-07T10:11:00+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-07T10:11 57차 재검증, 이력)

> **57차 재검증 (10:11) — B07 #6 18→20 files·FE-7 회귀(209/210 FAIL)·HEAD Fixed 유지·BLOCK = B03+B07 #6·Open 1(HIGH)**: 56차(18 files·205/42 PASS) 대비 develop HEAD **`d5654c0` 불변**·working tree **DIRTY 확대** — **14M+6U=20 files**. 신규: `ClientPhotoField.test.jsx`·`GuardianListCard.test.jsx`·`ClientFormPage.jsx`. develop WT `npm run build` **758 modules PASS**·`npm test` **209/44 FAIL**(1 — `GuardianListCard.test.jsx` MaskedPhone)·`npm audit` **0건**. test `@e5fd48d` build 36·N/A·**18 behind**. **신규 Open 1건(HIGH)**: H05. 판정 **BLOCK**.

## 커밋 수준 (57차)

- `develop` HEAD: `d5654c0` (COD 35차, origin/develop ahead **18**)
- `test` HEAD: `e5fd48d` — 스켈레톤 (merge 미실행, **18 behind**)
- **test 18 commits behind develop**

## develop working tree (57차 — B07 #6 recurrence + FE-7 FAIL)

| 항목 | 55차 | 57차 |
|------|------|------|
| modified | **11** | **14** |
| untracked | **4** | **6** |
| total | **15 (DIRTY)** | **20 (DIRTY)** |
| WT build modules | 758 | **758** |
| WT npm test | 205/42 PASS | **209/210 FAIL** (H05) |
| npm audit | 0 | **0** |

**WIP 범위**: `DateInput`(+test)·`GuardianInvitationList`(+test)·`ClientPhotoField.test.jsx`·`GuardianListCard.test.jsx`·`ClientDetailPage`·`ClientFormPage`·`GuardianInviteModal`·`GuardianListCard`·`LoginHistoryPanel`·`AuditLogPanel`·`ClientPhotoField`·`PaymentRecordModal`(+test)·`services.js`·`GuardianInvitationAcceptPage`(+test)·`components.css`·`index.js`.

## test 브랜치 (frontend-test, 57차 TSR 확인)

- `npm run build`: SUCCESS (36 modules, Vite 5.4.21, JS 165.43 kB) — 스켈레톤 (불변)
- `npm test`: N/A (Missing script @ e5fd48d)
- `npm audit`: 0 high, 2 moderate (stale vite 5.4.21)

## 판정 (57차)

**BLOCK** — **B03 merge 게이트 + B07 #6 dirty-tree + H05 FE-7 test FAIL**. develop WT build PASS(758)이나 npm test 209/210 FAIL. 잔여: v1.1 live E2E·J01 백엔드 API·develop→test merge(18 commits).

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-07T09:29:08+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-07T09:29 55차 재검증, 이력)

> **55차 재검증 (09:29) — B07 recurrence #6(CLEAN→DIRTY 15 files)·HEAD Fixed 유지·WT 205/42 PASS·BLOCK = B03+B07 #6·Open 1**: 53차(`d5654c0` CLEAN·199/40·B03 단일) 대비 develop HEAD **`d5654c0` 불변**·working tree **CLEAN→DIRTY** — **11M+4U=15 files**. 신규 WIP: `DateInput.jsx`(+test)·`GuardianInvitationList.jsx`(+test — J01 목록 UI) + modified `ClientDetailPage`(+98)·`GuardianInviteModal`·`GuardianListCard`·`LoginHistoryPanel`·`AuditLogPanel`·`ClientPhotoField`·`services.js`·`GuardianInvitationAcceptPage`(+test)·`components.css`. develop WT `npm run build` **758 modules PASS**(+2 vs 756)·`npm test` **205/42 PASS**(+6/+2 vs 199/40)·`npm audit` **0건**. test `@e5fd48d` build 36·npm test N/A·**18 behind**. **신규 Open 1건(BLOCK)**: B07 #6. 판정 **BLOCK**.

## 커밋 수준 (55차)

- `develop` HEAD: `d5654c0` (COD 35차, origin/develop ahead **18**)
- `test` HEAD: `e5fd48d` — 스켈레톤 (merge 미실행, **18 behind**)
- **test 18 commits behind develop**

## develop working tree (55차 — B07 #6 recurrence)

| 항목 | 53차 | 55차 |
|------|------|------|
| modified | **0** | **11** |
| untracked | **0** | **4** |
| total | **0 (CLEAN)** | **15 (DIRTY)** |
| WT build modules | 756 (HEAD) | **758 (WT)** |
| WT npm test | 199/40 (HEAD) | **205/42 (WT)** |
| npm audit | 0 | **0** |

**WIP 범위**: `DateInput.jsx`(+test, DS 날짜 입력)·`GuardianInvitationList.jsx`(+test, J01 초대 목록 UI)·`ClientDetailPage`(+98, 보호자/초대 연동)·`GuardianInviteModal`·`GuardianListCard`·`LoginHistoryPanel`·`AuditLogPanel`·`ClientPhotoField`·`services.js`·`GuardianInvitationAcceptPage`(+test)·`components.css`(ds-date-input).

## test 브랜치 (frontend-test, 55차 TSR 확인)

- `npm run build`: SUCCESS (36 modules, Vite 5.4.21, JS 165.43 kB) — 스켈레톤 (불변)
- `npm test`: N/A (Missing script @ e5fd48d)
- `npm audit`: 0 high, 2 moderate (stale vite 5.4.21)

## 판정 (55차)

**BLOCK** — **B03 merge 게이트 + B07 #6 dirty-tree**. develop WT build/test/audit PASS(758·205/42·0)이나 15 files 미커밋. 잔여: v1.1 live E2E·J01 백엔드 API·develop→test merge(18 commits).

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-07T08:36:21+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-07T08:36 53차 재검증, 이력)

> **53차 재검증 (08:36) — COD 35차 `d5654c0` FE-17 J01 수락 UI·LogoutButton·레이아웃 회귀·B07 #5 Fixed·CLEAN·199/40·756 modules·B03 BLOCK 단일·Open 0**: 52차(`0b9b001` DIRTY 20 files·B07 #5 Open) 대비 develop HEAD **`0b9b001`→`d5654c0`**(+1커밋 COD 35차, 25 files +823/-57, **18 ahead**)·working tree **DIRTY→CLEAN**(0 files). **B07 #5 Fixed TSR 독립 검증 PASS** — HEAD `LogoutButton.jsx`·`GuardianInvitationAcceptPage.jsx`·`GuardianInvitationAcceptForm.jsx`·`PublicAuthLayout.jsx`·`BillingPage.layout.test.jsx`·`services.js`(acceptGuardianInvitationApi) **전부 PRESENT**. develop HEAD build **756 modules PASS**(+2 vs 52차 754)·`npm test` **199/40 PASS**(+5/+2 vs 194/38)·`npm audit` **0건**. test `@e5fd48d` build 36·npm test N/A·**18 behind**. **신규 Open 0건** — B07 #5 소멸. 판정 **BLOCK**(B03 단일).

## 커밋 수준 (53차)

- `develop` HEAD: `d5654c0` (COD 35차, origin/develop ahead **18**)
- `test` HEAD: `e5fd48d` — 스켈레톤 (merge 미실행, **18 behind**)
- **test 18 commits behind develop**

## develop working tree (53차 — B07 #5 Fixed·CLEAN)

| 항목 | 52차 | 53차 |
|------|------|------|
| modified | 15 | **0** |
| untracked | 5 | **0** |
| total | **20 (DIRTY)** | **0 (CLEAN)** |
| HEAD build modules | 754 (WT) | **756 (HEAD)** |
| HEAD npm test | 194/38 (WT) | **199/40 (HEAD)** |
| npm audit | 0 | **0** |

**경위**: 52차 DIRTY 20 files(B07 recurrence #5) → COD 35차 `d5654c0`(feat(v1.1): FE-17 J01 보호자 초대 수락 UI·LogoutButton·레이아웃 회귀, 25 files +823/-57) **일괄 커밋** → working tree **CLEAN**. **B07 #5 소멸**. TSR 53차 독립 검증: `git status --porcelain` 0줄·`git cat-file -e HEAD:` 전 산출물 PRESENT·SEC-005 0건.

## test 브랜치 (frontend-test, 53차 TSR 확인)

- `npm run build`: SUCCESS (36 modules, Vite 5.4.21, JS 165.43 kB) — 스켈레톤 (불변)
- `npm test`: N/A (Missing script @ e5fd48d)
- `npm audit`: 0 high, 2 moderate (stale vite 5.4.21)

## 판정 (53차)

**BLOCK** — **B03 merge 게이트 단일**. develop HEAD(clean) build/test/audit PASS(756·199/40·0). B07 #5 소멸. 잔여: v1.1 live E2E·J01 백엔드 API·develop→test merge(18 commits).

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-07T08:03:37+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-07T08:03 52차 재검증, 이력)

> **52차 재검증 (08:03) — B07 recurrence #5(CLEAN→DIRTY 20 files)·HEAD Fixed 유지·WT 194/38 PASS·BLOCK = B03+B07 #5·Open 1**: 50차(`0b9b001` CLEAN·187/35·B03 단일) 대비 develop HEAD **`0b9b001` 불변**·working tree **CLEAN→DIRTY** — **15M+5U=20 files**. 신규 WIP: `LogoutButton.jsx`(+test)·`BillingPage.layout.test.jsx`·`GuardianInvitationAcceptPage.jsx`(+test — J01). develop WT `npm run build` **754 modules PASS**(+2)·`npm test` **194/38 PASS**(+7/+3)·`npm audit` **0건**. test `@e5fd48d` build 36·npm test N/A·**17 behind**. **신규 Open 1건(BLOCK)**: B07 #5. 판정 **BLOCK**.

## 커밋 수준 (52차)

- `develop` HEAD: `0b9b001` (COD 34차, origin/develop ahead **17**)
- `test` HEAD: `e5fd48d` — 스켈레톤 (merge 미실행, **17 behind**)
- **test 17 commits behind develop**

## develop working tree (52차 — B07 recurrence #5)

| 항목 | 50차 | 52차 |
|------|------|------|
| modified | 0 | **15** |
| untracked | 0 | **5** |
| total | **0 (CLEAN)** | **20 (DIRTY)** |
| WT build modules | 752 | **754 (WT)** |
| WT npm test | 187/35 | **194/38 (WT)** |
| npm audit | 0 | **0** |

**경위**: 50차 COD 34차 `0b9b001` CLEAN 직후 coder WIP 미커밋 — `LogoutButton`·`GuardianInvitationAcceptPage`(J01)·레이아웃 회귀 테스트 + AuthContext·Recharts·청구 페이지 수정. WT 품질 PASS이나 이관 규율 6·7 위반.

## test 브랜치 (frontend-test, 52차 TSR 확인)

- `npm run build`: SUCCESS (36 modules, Vite 5.4.21, JS 165.43 kB) — 스켈레톤 (불변)
- `npm test`: N/A (Missing script @ e5fd48d)
- `npm audit`: 0 high, 2 moderate (stale vite 5.4.21)

## 판정 (52차)

**BLOCK** — **B03 merge 게이트 + B07 recurrence #5 dirty-tree**. develop WT build/test/audit PASS(754·194/38·0) — **커밋 없이 PASS 불가**.

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-07T07:17:37+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-07T07:17 50차 재검증, 이력)

> **50차 재검증 (07:17) — COD 34차 `0b9b001` ds-* 유틸리티 전환·AttendancePage 레이아웃 회귀 테스트·working tree CLEAN·잔여 BLOCK = B03 merge 게이트 단일·Open 0**: 49차(`c98f98d` CLEAN, 186/34, B03 단일) 대비 **frontend develop 전진** — develop HEAD `c98f98d`→**`0b9b001`**(+1커밋 COD 34차 `fix(v1.1): Must 페이지 UXD ds-* 유틸리티 전환·AttendancePage 레이아웃 회귀 테스트`, origin/develop 대비 **17 ahead**). develop working tree **CLEAN**(0 dirty). **이관 규율 5 PASS** — `git -C src/frontend status --porcelain` **0줄**, `git cat-file -e HEAD:` `ChartContainer`·`FeeScheduleTable`·`AuthContext`·`pilotChecklist`·`chartColors`·`vite.config.js`·`sevenRoleJwtLogin.test.jsx`·`sevenRoleRouteMatrix.js` **전부 PRESENT**. SEC-005 AuthContext localStorage/sessionStorage **0건**. **FE-15 코드 스플릿 Fixed 유지** — 3 청크(react-vendor 166.34·index 181.88·recharts 393.53 kB, 최대 393.53 kB < 500 kB). develop HEAD(clean) `npm run build` **752 modules PASS**(vite 6.4.3, CSS 52.95 kB)·`npm test` **187 tests/35 files PASS**(vitest 4.1.8, 49차 186/34 → +1/+1 `AttendancePage.layout.test.jsx`)·`npm audit` **0건**. test `@e5fd48d` build 36·npm test N/A·**17 behind**. **frontend Open 0건** — B07 #3·#4·FE-15 사유 **전부 소멸**, 잔여 BLOCK = **B03 merge 게이트 단일**. 판정 **BLOCK**(B03).

## 커밋 수준 (50차)

- `develop` HEAD: `0b9b001` (COD 34차 `fix(v1.1)`, origin/develop ahead **17**)
- `test` HEAD: `e5fd48d` — 스켈레톤 (merge 미실행, **17 behind**)
- **test 17 commits behind develop**

## develop working tree (50차 — B07 #3·#4 전부 소멸·FE-15 Fixed 유지)

| 항목 | 49차 | 50차 |
|------|------|------|
| modified | 0 | **0** |
| untracked | 0 | **0** |
| total | **0 (CLEAN)** | **0 (CLEAN)** |
| HEAD build modules | 752 | **752 (HEAD)** |
| HEAD JS 청크 | 3 청크 분리(최대 393.53 kB ✓) | **3 청크 분리**(최대 393.53 kB ✓ 유지) |
| HEAD CSS | 52.04 kB | **52.95 kB** (+0.91 kB ds-* 전환) |
| HEAD npm test | 186/34 | **187/35 (HEAD)** |
| npm audit | 0 | **0** |

**경위**: COD 34차 `0b9b001` — Must 페이지 9개 컴포넌트(`AttendanceAbsentModal`·`BatchProgressSteps`·`CheckoutModal`·`FeeRateHistoryPanel`·`HealthAbnormalBanner`·`MedicationDuplicateAlert`·`PasswordResetRequestModal`·`PlatformOrgDetailModal`·`SessionTimeoutModal`) 인라인 style→ds-* 유틸리티 클래스 전환 + `AttendancePage.layout.test.jsx` 레이아웃 회귀 자동화 추가. 테스트 수 186/34→187/35. working tree CLEAN 유지.

## test 브랜치 (frontend-test, 50차 TSR 확인)

- `npm run build`: SUCCESS (36 modules, Vite 5.4.21, JS 165.43 kB) — 스켈레톤 (불변)
- `npm test`: N/A (Missing script @ e5fd48d)
- `npm audit`: 0 high, 2 moderate (stale vite 5.4.21 — SEC-008 fix 미머지)

## 판정 (50차)

**BLOCK** — merge 게이트 **B03 단일**(v1.1 merge_status pending·develop→test 17 commits 미머지·잔여 완료 기준 Must live E2E·J01 백엔드 API). B07 #3·#4·FE-15 사유 **전부 소멸**. develop HEAD clean build/test/audit PASS(752·187/35·0) — `merge_status: ready` 게이트만 잔존.

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-07T15:45:00+09:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-07T15:45 49차 재검증, 이력)

> **49차 재검증 (15:45) — B07 #4 신호 해소(COD 33차 `c98f98d`)·FE-15 코드 스플릿 Fixed·working tree CLEAN·잔여 BLOCK = B03 merge 게이트 단일·Open 0**: 47차(`4be0938` CLEAN, 비차단 LOW JS 청크 744.95 kB) + TSR 48차 backend 교차 관측(frontend `4be0938` 재오염 5 files — B07 recurrence #4 신호) 대비 **frontend develop 전진** — develop HEAD `4be0938`→**`c98f98d`**(+1커밋 `fix(v1.1): UXD 인라인 style 제거·FE-15 코드 스플릿·레이아웃 회귀 테스트`, 7 files +145/-23, origin/develop 대비 **16 ahead**). develop working tree **CLEAN**(0 dirty — 48차 교차 관측 5 files re-dirty가 `c98f98d`로 **일괄 커밋**, B07 recurrence #4 신호 **소멸·미발생 확정**). **이관 규율 5 PASS** — `git -C src/frontend status --porcelain` **0줄**, `git cat-file -e HEAD:` `ChartContainer`·`FeeScheduleTable`·`AuthContext`·`pilotChecklist`·`chartColors`·`vite.config.js` **전부 PRESENT**. SEC-005 AuthContext localStorage/sessionStorage **0건**. **FE-15 코드 스플릿 정식 Fixed** — `vite.config.js` `build.rollupOptions.output.manualChunks` 추가 → 47차 단일 JS 청크 **744.95 kB** → **3 청크 분리**(`react-vendor` 166.34 kB·`index` 182.52 kB·`recharts` 393.53 kB, 최대 청크 **393.53 kB < 500 kB**, vite 경고 **해소**). develop HEAD(clean) `npm run build` **752 modules PASS**(vite 6.4.3, CSS 52.04 kB)·`npm test` **186 tests/34 files PASS**(vitest 4.1.8, 47차 185/33 → +1/+1 `ClientDetailPage.layout.test.jsx`)·`npm audit` **0건**. test `@e5fd48d` build 36·npm test N/A·**16 behind**. **frontend Open 0건** — B07 #4 신호·FE-15 LOW 사유 **소멸**, 잔여 BLOCK = **B03 merge 게이트 단일**. 판정 **BLOCK**(B03).

## 커밋 수준 (49차)

- `develop` HEAD: `c98f98d` (COD 33차 `fix(v1.1)`, origin/develop ahead **16**)
- `test` HEAD: `e5fd48d` — 스켈레톤 (merge 미실행, **16 behind**)
- **test 16 commits behind develop**

## develop working tree (49차 — B07 #4 신호 소멸·FE-15 Fixed)

| 항목 | 47차 | 49차 |
|------|------|------|
| modified | 0 | **0** |
| untracked | 0 | **0** |
| total | **0 (CLEAN)** | **0 (CLEAN)** |
| HEAD build modules | 752 | **752 (HEAD)** |
| HEAD JS 청크 | 단일 744.95 kB(>500kB ⚠) | **3 청크 분리**(최대 393.53 kB ✓) |
| HEAD npm test | 185/33 | **186/34 (HEAD)** |
| npm audit | 0 | **0** |

**경위**: TSR 48차 backend 라운드 교차 관측한 frontend `4be0938` 재오염 5 files(`ClientDetailPage`·`ClientFormPage`·`GuardiansPage`·`PlatformPage`·`components.css`)를 **COD 33차 `c98f98d`(7 files +145/-23)로 일괄 커밋** → working tree CLEAN. B07 recurrence #4는 **신호 단계에서 종결**(정식 Open 미등록). 동반: **FE-15 코드 스플릿**(`vite.config.js` manualChunks — react-vendor·recharts·index 분리)·UXD 인라인 style 제거·`ClientDetailPage.layout.test.jsx` 레이아웃 회귀 테스트.

## test 브랜치 (frontend-test, 49차 TSR 실측)

- `npm run build`: SUCCESS (36 modules, Vite 5.4.21, JS 165.43 kB) — 스켈레톤
- `npm test`: N/A (Missing script @ e5fd48d)
- `npm audit`: 0 high, 2 moderate (stale vite 5.4.21 — SEC-008 fix 미머지)

## 판정 (49차)

**BLOCK** — merge 게이트 **B03 단일**(v1.1 merge_status pending·develop→test 16 commits 미머지·잔여 완료 기준 Must live E2E·J01 백엔드 API). B07 recurrence #4 신호·FE-15 LOW 사유 **소멸**. develop HEAD clean build/test/audit PASS(752·186/34·0) + 청크 분리 — `merge_status: ready` 게이트만 잔존.

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-07T14:45:00+09:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-07T14:45 47차 재검증, 이력)

> **47차 재검증 (14:45) — B07 #3 Fixed TSR 독립 검증 PASS(COD 31차 `4be0938`)·잔여 BLOCK = B03 merge 게이트 단일**: 45차(`3fdc266` DIRTY 76 files) 대비 develop HEAD `3fdc266`→**`4be0938`**(+1커밋 COD 31차 `feat(v1.1/v1.2): Recharts·플랫폼·청구·건강·운영/보안 UI 일괄 커밋 (B07 #3)`, 82 files +4589/-545, origin/develop 대비 **15 ahead**). develop working tree **76 files → CLEAN**(0 dirty). **QA-B07 recurrence #3 정식 Fixed 확정** — `git status --porcelain` 0줄·`git cat-file -e HEAD:` Recharts(`ChartContainer`·`AttendanceRateChart`·`HealthTrendChart`)·FE-13(`FeeScheduleTable`·`CopayRateTable`·`NhisImportGuidePanel`·`BillingStatusConfirmModal`·`GuardianDailySummary`)·FE-14(`AuditLogPanel`·`BackupSettingsPanel`·`LoginHistoryPanel`·`PasswordChangeModal`)·`HealthAlertList`·`FeeRateHistoryPanel`·`chartColors.js`·`dashboardWidgets.js` **전부 PRESENT**(이관 규율 5 PASS). SEC-005 AuthContext localStorage/sessionStorage 0건. develop HEAD(clean) `npm run build` **752 modules PASS**(vite 6.4.3, JS 744.95 kB gzip 211.42 kB, CSS 51.49 kB)·`npm test` **185/33 PASS**(vitest 4.1.8)·`npm audit` **0건**. `recharts ^2.15.4` 커밋. test `@e5fd48d` build 36·npm test N/A·**15 behind**. **frontend Open 0건** — B07 #3 dirty 사유 소멸, 잔여 BLOCK = **B03 단일**. 비차단 LOW: JS 청크 744.95 kB(>500 kB).

## 커밋 수준

- `develop` HEAD: `4be0938` (COD 31차, origin/develop ahead **15**)
- `test` HEAD: `e5fd48d` — 스켈레톤 (merge 미실행)
- **test 15 commits behind develop**

## develop working tree (47차 — B07 #3 Fixed)

| 항목 | 45차 | 47차 |
|------|------|------|
| modified | 40 | **0** |
| untracked | 36 | **0** |
| total | **76 (DIRTY)** | **0 (CLEAN)** |
| HEAD build modules | — (WT 749) | **752 (HEAD)** |
| HEAD npm test | — (WT 181/30) | **185/33 (HEAD)** |
| npm audit | 0 | **0** |

**경위**: 45차 dirty 76 files(Recharts·청구·copay·수가표·보호자·건강·NHIS·운영/보안 설정 WIP)를 **COD 31차 `4be0938`(82 files +4589/-545)로 일괄 커밋** → working tree CLEAN. develop HEAD 직접 build/test/audit 실측(WT-only 아님). FE-12(Recharts 차트 레이어)·FE-13(청구·수가표·NHIS UI)·FE-14(운영·보안 설정 UI) develop HEAD 반영.

## test 브랜치 (frontend-test, 47차 TSR 실측)

- `npm run build`: SUCCESS (36 modules, Vite 5.4.21, JS 165.43 kB) — 스켈레톤
- `npm test`: N/A (Missing script @ e5fd48d)
- `npm audit`: 0 high, 2 moderate (stale vite 5.4.21 — SEC-008 fix 미머지)

## 판정

**BLOCK** — merge 게이트 **B03 단일**(v1.1 merge_status pending·develop→test 15 commits 미머지·잔여 완료 기준 Must live E2E·J01 백엔드 API). B07 #3 dirty-tree 사유 **소멸**(Fixed). develop HEAD clean build/test/audit PASS — `merge_status: ready` 게이트만 잔존.

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-07T14:02:36+09:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-07T14:02 45차 재검증, 이력)

> **45차 재검증 (14:02) — B07 #3 dirty-tree 확대(72→76 files)·WT 181/30 PASS·B03 BLOCK 유지**: develop HEAD `3fdc266` **불변**. working tree **40M+36U=76 files**(43차 38M+34U=72 → +4). 신규 WIP: **`FeeScheduleTable`(+test)** + 2 modified. WT `npm run build` **749 modules PASS**(+1)·`npm test` **181/30 PASS**(+2/+1)·`npm audit` **0건**. test `@e5fd48d` build 36·npm test N/A·14 behind. **frontend Open 0건** — Planned BLOCK **B03 + B07 #3**.

## 커밋 수준

- `develop` HEAD: `3fdc266` (불변, origin/develop ahead **14**)
- `test` HEAD: `e5fd48d` — 스켈레톤 (merge 미실행)
- **test 14 commits behind develop**

## develop working tree (45차 — B07 recurrence #3 확대)

| 항목 | 43차 | 45차 |
|------|------|------|
| modified | 38 | **40** |
| untracked | 34 | **36** |
| total | **72 (DIRTY)** | **76 (DIRTY)** |
| build modules | 748 (WT) | **749 (WT)** |
| npm test | 179/29 (WT) | **181/30 (WT)** |
| npm audit | 0 | **0** |

**WIP 범위 (45차 신규/확대)**: 43차 WIP + `FeeScheduleTable`(+test) + 2 modified(api/config).

## test 브랜치 (frontend-test, 45차 TSR 실측)

- `npm run build`: SUCCESS (36 modules, Vite 5.4.21, JS 165.43 kB)
- `npm test`: N/A (Missing script)
- `npm audit`: 0 high, 2 moderate (stale vite 5.4.21)

## 판정

**BLOCK** — B07 recurrence #3 (Planned, 76 files) + B03 merge 게이트. PASS 금지.

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-07T13:27:22+09:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-07T13:27 43차 재검증, 이력)

> **43차 재검증 (13:27) — B07 #3 dirty-tree 확대(61→72 files)·WT 179/29 PASS·B03 BLOCK 유지**: develop HEAD `3fdc266` **불변**. working tree **38M+34U=72 files**(41차 37M+24U=61 → +11). 신규 WIP: `BillingStatusConfirmModal`·`CopayRateTable`·`GuardianDailySummary`·`HealthAlertList`·`NhisImportGuidePanel`(+tests). WT `npm run build` **748 modules PASS**(+5)·`npm test` **179/29 PASS**(+10/+5)·`npm audit` **0건**. test `@e5fd48d` build 36·npm test N/A·14 behind. **frontend Open 0건** — Planned BLOCK **B03 + B07 #3**.

## 커밋 수준

- `develop` HEAD: `3fdc266` (불변, origin/develop ahead **14**)
- `test` HEAD: `e5fd48d` — 스켈레톤 (merge 미실행)
- **test 14 commits behind develop**

## develop working tree (43차 — B07 recurrence #3 확대)

| 항목 | 41차 | 43차 |
|------|------|------|
| modified | 37 | **38** |
| untracked | 24 | **34** |
| total | **61 (DIRTY)** | **72 (DIRTY)** |
| build modules | 743 (WT) | **748 (WT)** |
| npm test | 169/24 (WT) | **179/29 (WT)** |
| npm audit | 0 | **0** |

**WIP 범위 (43차 신규/확대)**: 41차 WIP + `BillingStatusConfirmModal`(+test) + `CopayRateTable`(+test) + `GuardianDailySummary`(+test) + `HealthAlertList`(+test) + `NhisImportGuidePanel`(+test) + 1 modified(api/config).

## test 브랜치 (frontend-test, 43차 TSR 실측)

- `npm run build`: SUCCESS (36 modules, Vite 5.4.21, JS 165.43 kB)
- `npm test`: N/A (Missing script)
- `npm audit`: 0 high, 2 moderate (stale vite 5.4.21)

## 판정

**BLOCK** — B07 recurrence #3 (Planned, 72 files) + B03 merge 게이트. PASS 금지.

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-07T12:52:35+09:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-07T12:52 41차 재검증)

> **41차 재검증 (12:52) — 39차 대비 상태 불변(±1 modified)·WT 169/24 PASS·B03 BLOCK 유지**: develop HEAD `3fdc266` **불변**. working tree **37M+24U=61 files**(39차 36M+24U=60 → +1 modified). WT `npm run build` **743 modules PASS**·`npm test` **169/24 PASS**·`npm audit` **0건**. test `@e5fd48d`(frontend-test) build 36·npm test N/A·14 behind. **frontend Open 0건** — Planned BLOCK **B03 + B07 #3**.

## 커밋 수준

- `develop` HEAD: `3fdc266` (불변, origin/develop ahead **14**)
- `test` HEAD: `e5fd48d` — 스켈레톤 (merge 미실행)
- **test 14 commits behind develop**

## develop working tree (41차 — B07 recurrence #3)

| 항목 | 39차 | 41차 |
|------|------|------|
| modified | 36 | **37** |
| untracked | 24 | **24** |
| total | **60 (DIRTY)** | **61 (DIRTY)** |
| build modules | 743 (WT) | **743 (WT)** |
| npm test | 169/24 (WT) | **169/24 (WT)** |
| npm audit | 0 | **0** |

**WIP 범위**: 39차와 동일 — Recharts 차트 5종·Platform·감사·백업·비밀번호·로그인이력·SettingsPage.test + 37 modified pages/api/config.

## test 브랜치 (frontend-test, 41차 TSR 실측)

- `npm run build`: SUCCESS (36 modules, Vite 5.4.21, JS 165.43 kB)
- `npm test`: N/A (Missing script)
- `npm audit`: 0 high, 2 moderate (stale vite 5.4.21)

## 판정

**BLOCK** — B07 recurrence #3 (Planned, 61 files) + B03 merge 게이트. PASS 금지.

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-07T12:09:00+09:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-07T12:09 39차 재검증, 이력)

> **39차 재검증 (12:09) — B07 #3 dirty-tree 확대(44→60 files)·WT 169/24 PASS·B03 BLOCK 유지**: develop HEAD `3fdc266` **불변**. working tree **확대** 37차 26M+18U=44 → **36M+24U=60 files**(`LoginHistoryPanel`·`PasswordChangeModal`·`PasswordResetRequestModal`·`PlatformOrgDetailModal`(+tests)·`SettingsPage.test.jsx` + Recharts·감사·백업 WIP). WT `npm run build` **743 modules PASS**·`npm test` **169/24 PASS**(+8/+4)·`npm audit` **0건**. test `@e5fd48d` stale(14 behind). **frontend Open 0건** — Planned BLOCK **B03 + B07 #3**.

## 커밋 수준

- `develop` HEAD: `3fdc266` (불변, origin/develop ahead **14**)
- `test` HEAD: `e5fd48d` — 스켈레톤 (merge 미실행)
- **test 14 commits behind develop**

## develop working tree (39차 — B07 recurrence #3 확대)

| 항목 | 37차 | 39차 |
|------|------|------|
| modified | 26 | **36** |
| untracked | 18 | **24** |
| total | **44 (DIRTY)** | **60 (DIRTY)** |
| build modules | 741 (WT) | **743 (WT)** |
| npm test | 161/20 (WT) | **169/24 (WT)** |
| npm audit | 0 | **0** |

**WIP 범위 (39차 신규/확대)**: 37차 WIP + `LoginHistoryPanel`(+test) + `PasswordChangeModal`(+test) + `PasswordResetRequestModal`(+test) + `PlatformOrgDetailModal`(+test) + `SettingsPage.test.jsx` + `HealthTrendChart.test.jsx` + 10 modified pages/api.

## test 브랜치 (frontend-test)

- `npm run build`: SUCCESS (36 modules, Vite 5.4.21, JS 165.43 kB)
- `npm test`: N/A (Missing script)
- `npm audit`: 0 high, 2 moderate (stale vite 5.4.21)

## 판정

**BLOCK** — B07 recurrence #3 (Planned, 60 files) + B03 merge 게이트. PASS 금지.

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-07T11:30:00+09:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-07T11:30 37차 재검증, 이력)

> **37차 재검증 (11:30) — B07 #3 dirty-tree 확대(26→44 files)·WT 161/20 PASS·B03 BLOCK 유지**: develop HEAD `3fdc266` **불변**. working tree **확대** 35차 26 → **26M+18U=44 files**(`AuditLogPanel`·`BackupSettingsPanel`·`PasswordChangeModal`·`FilterChips.test` + Recharts·Platform WIP). WT `npm run build` **741 modules PASS**·`npm test` **161/20 PASS**(+17/+7)·`npm audit` **0건**. test `@e5fd48d` stale(14 behind). **frontend Open 0건** — Planned BLOCK **B03 + B07 #3**.

## 커밋 수준

- `develop` HEAD: `3fdc266` (불변, origin/develop ahead **14**)
- `test` HEAD: `e5fd48d` — 스켈레톤 (merge 미실행)
- **test 14 commits behind develop**

## develop working tree (37차 — B07 recurrence #3 확대)

| 항목 | 35차 | 37차 |
|------|------|------|
| modified | 18 | **26** |
| untracked | 8 | **18** |
| total | **26 (DIRTY)** | **44 (DIRTY)** |
| build modules | 738 (WT) | **741 (WT)** |
| npm test | 144/13 (WT) | **161/20 (WT)** |
| npm audit | 0 | **0** |

**WIP 범위 (37차 신규/확대)**: Recharts 차트 5 files + `AuditLogPanel`(+test) + `BackupSettingsPanel`(+test) + `PasswordChangeModal`(+test) + `FilterChips.test` + `BatchProgressSteps`·`PlatformOrgDetailModal` + Platform·Settings·NHIS·Reconciliation·Forbidden 수정.

## test 브랜치 (frontend-test)

- `npm run build`: SUCCESS (36 modules, Vite 5.4.21, JS 165.43 kB)
- `npm test`: N/A (Missing script)
- `npm audit`: 0 high, 2 moderate (stale vite 5.4.21)

## 판정

**BLOCK** — B07 recurrence #3 (Planned, 44 files) + B03 merge 게이트. PASS 금지.

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-07T01:50:00+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-07T01:50 35차 재검증, 이력)

> **35차 재검증 (01:50) — B07 #3 dirty-tree 확대(18→26 files)·WT 144/13 PASS·B05 해소·BLOCK 유지**: develop HEAD `3fdc266` **불변**. working tree **확대** 33차 13M+5U=18 → **18M+8U=26 files**(`BatchProgressSteps`·`PlatformOrgDetailModal`·Platform/NHIS/Reconciliation/Forbidden WIP 추가). WT `npm run build` **738 modules PASS**·`npm test` **144/13 PASS**(+2/+1)·`npm audit` **0건**. test `@e5fd48d` stale(14 behind). ROADMAP v1 `merged` → B05 해소. **frontend Open 0건** — Planned BLOCK **B03 + B07 #3**.

## 커밋 수준

- `develop` HEAD: `3fdc266` (불변, origin/develop ahead **14**)
- `test` HEAD: `e5fd48d` — 스켈레톤 (merge 미실행)
- **test 14 commits behind develop**

## develop working tree (35차 — B07 recurrence #3 확대)

| 항목 | 33차 | 35차 |
|------|------|------|
| modified | 13 | **18** |
| untracked | 5 | **8** |
| total | **18 (DIRTY)** | **26 (DIRTY)** |
| build modules | 736 (WT) | **738 (WT)** |
| npm test | 142/12 (WT) | **144/13 (WT)** |
| npm audit | 0 | **0** |

**WIP 범위 (35차 신규/확대)**: Recharts 차트 5 files + `BatchProgressSteps`(+test) + `PlatformOrgDetailModal` + Platform·NHIS·Reconciliation·Forbidden·pilotPageFlows·chartColors·components.css 수정.

## test 브랜치 (frontend-test)

- `npm run build`: SUCCESS (36 modules, Vite 5.4.21, JS 165.43 kB)
- `npm test`: N/A (Missing script)
- `npm audit`: 0 high, 2 moderate (stale vite 5.4.21)

## 판정

**BLOCK** — B07 recurrence #3 (Planned, 26 files) + B03 merge 게이트. PASS 금지.
