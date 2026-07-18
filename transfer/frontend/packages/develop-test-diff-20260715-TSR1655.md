# develop→test diff · TSR1655 · FF merge+PUSH (J03 BE unit rates + QA-B95 end-terminated)

- range: `56797a8..a356083` (FF · 2 commits)
- commits:
  - `a356083` feat(v1.2.1/J03): prefer BE dispatchReferenceUnitRates in channel readiness
  - `b0b9ace` fix(v1.2.1/QA-B95): decode end-terminated numeric HTML entities
- files (highlights):
  - `src/config/notificationDispatchUnitRates.js` (+72L prefer BE `dispatchReferenceUnitRates` + static fallback)
  - `src/components/ui/NotificationChannelReadinessPanel.jsx` (+ BE rate wire)
  - `src/config/notificationChannelStatus.js` (+ end-terminated numeric entity decode)
  - `src/test/liveE2eHarness.test.js` (+ QA-B95 end-terminated regress)
- merge: **EXECUTED** FF `56797a8`→`a356083` · origin/test **SYNCED+PUSHED** (`b0b9ace` local-only → included)
- related pre-merge: **26/26 PASS** (3.75s · 3 files · notificationDispatchUnitRates + NotificationChannelReadinessPanel + notificationChannelStatus)
- post-merge npm: **2593/2593 PASS** (871.14s, 477 files · +5 vs TSR1649 2588)
- build: **1230** modules (10.68s) · audit **0 high**
- live: default **0/149/0** (33.31s · bootstrap-disabled fail-closed)
- Open: **1** (QA-B476 BE carry · FE Open 0 · QA-B477 Fixed)
- cross-stream: BLOCK (BE develop `@2f578fb` pending 1 vs test `@74e90c1` · FE `@a356083` ALL SYNCED+PUSHED)
- operation: BLOCK (origin/test **674 BE** · QA-B116 + QA-B95)
