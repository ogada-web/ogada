# develop→test diff · TSR1644 · FF merge+PUSH (QA-B95 uppercase hex HTML entity decode)

- range: `fd6b996..b4008b0` (FF · 1 commit)
- commit: `b4008b0` fix(v1.2.1/QA-B95): decode uppercase hex HTML entities in readiness blockers
- files:
  - `src/config/notificationChannelStatus.js` (+uppercase hex `#X` numeric entity decode)
  - `src/config/notificationChannelStatus.test.js` (+regression)
  - `src/e2e/liveBackendProbe.js` / `liveConfig.js` / `liveGlobalSetup.js` (parity)
  - `src/test/liveE2eHarness.test.js` (+uppercase hex / double-encoded cases)
- merge: **EXECUTED** FF `fd6b996`→`b4008b0` + origin/test **PUSHED**
- related pre-merge: **153/153 PASS** (2.40s · 2 files · notificationChannelStatus + liveE2eHarness)
- post-merge npm: **2573/2573 PASS** (865.83s, 472 files · +2 vs TSR1642 2571)
- build: **1225** modules (9.43s) · audit **0 high** · reconfirm build 9.23s (TSR1644b)
- live: default **0/149/0** (33.27s · bootstrap-disabled fail-closed) · reconfirm 33.85s (TSR1644b)
- origin/test: **PUSHED** `fd6b996`→`b4008b0`
- Open: **0** (QA-B471 Fixed)
- cross-stream: SYNCED (BE `@cf700b9` · FE `@b4008b0` ALL SYNCED+PUSHED)
- operation: BLOCK (origin/test **671 BE** · QA-B116 + QA-B95)
