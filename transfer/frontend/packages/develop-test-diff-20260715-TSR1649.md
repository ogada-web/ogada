# develop→test diff · TSR1649 · FF merge+PUSH (J03 SMS dispatch reference unit rates)

- range: `a5f4098..56797a8` (FF · 1 commit)
- commits:
  - `56797a8` feat(v1.2.1/J03): surface SMS dispatch reference unit rates
- files (highlights):
  - `src/config/notificationDispatchUnitRates.js` + test (+52L config · ezCare app10/sms20/mms50 parity)
  - `src/components/ui/NotificationChannelReadinessPanel.jsx` (+42L operator guidance panel)
  - `src/components/ui/NotificationChannelReadinessPanel.test.jsx` (+8L regression)
  - `src/config/competitorModuleCoverage.js` (+1L id=10 carry 0.85)
- merge: **EXECUTED** FF `a5f4098`→`56797a8` · origin/test **SYNCED+PUSHED**
- related pre-merge: **162/162 PASS** (4.98s · 4 files · notificationDispatchUnitRates + NotificationChannelReadinessPanel + notificationChannelStatus + liveE2eHarness)
- post-merge npm: **2588/2588 PASS** (876.69s, 477 files · +2 vs TSR1646 2586)
- build: **1230** modules (11.30s) · audit **0 high**
- live: default **0/149/0** (33.40s · bootstrap-disabled fail-closed)
- Open: **0** (QA-B474 Fixed)
- cross-stream: BLOCK (BE develop `@e9f24f7` pending 1 vs test `@89dc0a6` · FE `@56797a8` ALL SYNCED+PUSHED)
- operation: BLOCK (origin/test **672 BE** · QA-B116 + QA-B95)
