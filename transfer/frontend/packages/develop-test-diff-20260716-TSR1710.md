<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-07-16T13:18:45Z -->
# develop→test diff package — frontend TSR1710

- **stream**: frontend
- **develop HEAD**: `a3703a5` (WT **CLEAN**)
- **test HEAD**: `5b69e7a` (WT **CLEAN**)
- **origin/test**: `5b69e7a` (**PUSHED/SYNCED**)
- **origin/develop**: `5b69e7a` (develop ahead **2** locally · not pushed)
- **merge**: **SKIP** (pending **2** · read-only directive · QA-B514 Open)
- **diff range**: `test..develop` (2 commits)
  - `d171df6` ux(a11y): wrap HomeNewsletterLaunchPage raw tables in `.ds-table-wrap` (UXD-183)
  - `a3703a5` fix(v1.2.1/QA-B95): decode ThickSpace and MathML invisible HTML entities
- **files changed**: 7 files, +98/−4
  - `src/e2e/liveConfig.js`, `src/e2e/liveGlobalSetup.js`, `src/test/liveE2eHarness.test.js` (QA-B95 decode)
  - `src/pages/HomeNewsletterLaunchPage.jsx` (UXD-183 table wrap)
  - `src/config/notificationChannelStatus.js`, `src/config/notificationChannelStatus.test.js`
- **related**: **188/188 PASS** (2.63s, 2 · +2 vs 186 · develop pre-merge)
- **npm regression**: **CARRY 2630/2630 PASS** (TSR1707 · test SHA `@5b69e7a` unchanged)
- **post-merge 예상**: ~**2632/2632** (+2 ThickSpace/MathML cases)
- **build**: **1230** modules (10.69s)
- **audit**: **0** high
- **live E2E**: **SKIP** (merge 없음 · CARRY **0/149/0** TSR1707 · bootstrap-disabled)
- **Open**: **2** (QA-B512 BE transfer · QA-B514 FE transfer)
- **Planned**: QA-B116 (origin/test **697 BE**) + QA-B95
- **verdict**: **BLOCK**
- **cross-stream**: **BLOCK** (BE pending 1 `@3937fa5` · FE pending 2 `@a3703a5`)
- **operation**: **BLOCK** (697 BE unpushed + FE/BE pending 미이관)
- **backend@8080**: UP/200
