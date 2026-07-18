# develop→test diff · TSR1646 · FF merge+PUSH (UXD-180 + QA-B95 semicolon-optional entities)

- range: `b4008b0..a5f4098` (FF · 2 commits)
- commits:
  - `eb270ae` ux(a11y): Skeleton, ProgressBar, SkipLink, CalendarDayMarker (UXD-180)
  - `a5f4098` fix(v1.2.1/QA-B95): accept semicolon-optional numeric HTML entities
- files (highlights):
  - `src/components/ui/{Skeleton,ProgressBar,SkipLink,CalendarDayMarker}.jsx` + tests (+4 @Test files)
  - `src/styles/components.css` (+251L design tokens)
  - `src/config/notificationChannelStatus.js` + live e2e probe/config/setup (semicolon-optional decode)
  - `src/test/liveE2eHarness.test.js` (+regression)
- merge: **EXECUTED** FF `b4008b0`→`a5f4098` · origin/test **SYNCED+PUSHED**
- related pre-merge: **166/166 PASS** (8.06s · 6 files)
- post-merge npm: **2586/2586 PASS** (869.23s, 476 files · +13 vs TSR1644 2573)
- build: **1229** modules (10.19s) · audit **0 high**
- live: default **0/149/0** (33.37s · bootstrap-disabled fail-closed)
- Open: **0** (QA-B473 Fixed)
- cross-stream: SYNCED (BE `@89dc0a6` · FE `@a5f4098` ALL SYNCED+PUSHED)
- operation: BLOCK (origin/test **672 BE** · QA-B116 + QA-B95)
