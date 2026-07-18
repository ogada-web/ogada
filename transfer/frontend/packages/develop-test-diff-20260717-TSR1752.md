# frontend develop→test diff meta — TSR 1752

- updated: 2026-07-17T02:18:34Z
- merge: FF `9907725`→`1c84f0f` (1 commit · PUSHED)
- commits:
  - `1c84f0f` fix(v1.2.1/QA-B95): decode angle wrapping HTML entities
- files: 6 (+55/-0)
- related: 219/219 PASS (2.60s, 2 files · +2 vs TSR1750)
- core QA-B95: 219/219
- post-merge npm: 2663/2663 PASS (877.36s, 477 files · +2 vs TSR1750 2661)
- build: 1230 modules PASS (11.00s)
- audit: 0 high
- live E2E: 0 PASS / 149 SKIP / 0 FAIL (34.56s · bootstrap-disabled)
- origin/test: PUSHED/SYNCED `9907725`→`1c84f0f`
- QA: QA-20260717-B547 Fixed · Open 0(FE) · Open 0 residual (B545 Fixed TSR1751)

## Diffstat
```
 src/config/notificationChannelStatus.js      |  6 ++++++
 src/config/notificationChannelStatus.test.js | 16 ++++++++++++++++
 src/e2e/liveBackendProbe.js                  |  6 ++++++
 src/e2e/liveConfig.js                        |  5 +++++
 src/e2e/liveGlobalSetup.js                   |  5 +++++
 src/test/liveE2eHarness.test.js              | 17 +++++++++++++++++
 6 files changed, 55 insertions(+)
```
