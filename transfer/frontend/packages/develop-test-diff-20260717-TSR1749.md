# frontend develop→test diff meta — TSR 1749

- updated: 2026-07-17T01:46:30Z
- merge: FF `d6be05c`→`9907725` (2 commits · already PUSHED before reval)
- commits:
  - `9907725` fix(v1.2.1/QA-B95): decode parenthesis wrapping HTML entities
  - `971c636` ux(a11y): promote 26 undefined ds-* classes to components.css (UXD-186)
- files: 7 (+283/-0)
- related: 217/217 PASS (2.61s, 2 files · +2 vs TSR1747)
- core QA-B95: 217/217
- post-merge npm: 2661/2661 PASS (877.56s, 477 files · +2 vs TSR1747 2659)
- build: 1230 modules PASS (9.61s)
- audit: 0 high
- live E2E: 0 PASS / 149 SKIP / 0 FAIL (34.66s · bootstrap-disabled)
- origin/test: PUSHED/SYNCED `d6be05c`→`9907725`
- QA: QA-20260717-B546 Fixed · Open 0(FE) · residual Open QA-B545(BE)

## Diffstat
```
 src/config/notificationChannelStatus.js      |   4 +
 src/config/notificationChannelStatus.test.js |  16 ++
 src/e2e/liveBackendProbe.js                  |   4 +
 src/e2e/liveConfig.js                        |   3 +
 src/e2e/liveGlobalSetup.js                   |   3 +
 src/styles/components.css                    | 236 +++++++++++++++++++++++++++
 src/test/liveE2eHarness.test.js              |  17 ++
 7 files changed, 283 insertions(+)
```
