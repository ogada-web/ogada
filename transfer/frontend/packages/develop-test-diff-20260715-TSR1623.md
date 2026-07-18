# develop→test diff · TSR1623 · QA-B95 object-form live operation blockers

- range: `5b9656c..2c5bb2a` (FF · 1 commit · origin/test push)
- commits:
  - `2c5bb2a` — `fix(v1.2.1/QA-B95): accept object-form live operation blockers`
- files: 3 (+65/−8) — `liveBackendProbe.js` · `liveConfig.js` · `liveE2eHarness.test.js`
- related: **134/134 PASS** (1.45s · 1 file · liveE2eHarness)
- npm: **2556/2556 PASS** (859.79s · 472 files · +2 @Test vs 2554)
- build: **1223** modules (9.16s) · audit **0 high**
- live: default **0 PASS/149 SKIP/0 FAIL** (33.43s · bootstrap-disabled fail-closed) · opt-in **SKIP**(carry TSR1597 **116/33/0**)
- Open: **0** · Fixed **QA-B456**
- cross-stream: SYNCED (BE `@c080529` · FE `@2c5bb2a` ALL SYNCED+PUSHED)
- operation: BLOCK (origin/test **663 BE** · QA-B116 + QA-B95)
