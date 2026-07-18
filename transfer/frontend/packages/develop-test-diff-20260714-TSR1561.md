<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-07-14T17:49:20+00:00 -->
# frontend develop→test diff — TSR 1561차

- **range**: `bb48b6c`→`d613826` (FF · 1 commit) + origin push `3bd50ac`→`d613826` (4 commits)
- **HEAD**: develop/test/origin/test **ALL SYNCED `@d613826`**
- **subject**: `feat(v1.2.1/G2): wire facility notices board CRUD in launch page`
- **files** (1 commit):
  - `src/api/services.js` (+55 facility-notices API)
  - `src/api/billingGuardianPlatformServices.test.js` (+45)
  - `src/pages/HomeNewsletterLaunchPage.jsx` (+476 board CRUD wire)
  - `src/pages/HomeNewsletterLaunchPage.test.jsx` (+134)
  - `src/utils/homeNewsletter.js` (+38)
- **related pre-merge**: **75/75 PASS** (7.07s, 3 files)
- **post-merge vitest**: **2470/2470 PASS** (832.04s, 465 files)
- **build**: **1217** modules · 8.97s
- **audit**: 0 high
- **live E2E**: **116 PASS / 33 SKIP / 0 FAIL** (37.91s · bootstrap-disabled)
- **QA**: **QA-B403/B404/B406 Fixed** (pairs BE QA-B405 `@55b8f84`) · Open **0**
- **live reconfirm**: **116/33/0** (38.54s · TSR1561 follow-up)
- **operation**: BLOCK (origin/test **638 BE** · QA-B116 + QA-B95)
