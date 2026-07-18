# frontend develop→test diff meta — TSR 1767

- updated: 2026-07-17T06:38:38Z
- merge: FF `694266e`→`56fa1c0` (1 commit · PUSHED/SYNCED)
- commits:
  - `56fa1c0` fix(v1.2.1/QA-B95): decode low-9/reversed-9 quote HTML entity aliases
- files: 6 (+66/−2)
- related: 230/230 PASS (2.63s, 2 files · +2 vs TSR1765 228)
- core QA-B95: 230/230
- post-merge npm: 2674/2674 PASS (877.81s, 477 files · +2 vs TSR1765 2672)
- build: 1230 modules PASS (13.05s)
- audit: 0 high
- live E2E: 0 PASS / 149 SKIP / 0 FAIL (36.41s · bootstrap-disabled)
- origin/test: PUSHED/SYNCED `694266e`→`56fa1c0`
- QA: QA-20260717-B560 Fixed · Open 0(FE) · cross-stream BLOCK(BE pending 1 `@23ce552` · QA-B559)

## Diffstat
```
 src/config/notificationChannelStatus.js      |  9 ++++++++-
 src/config/notificationChannelStatus.test.js | 17 +++++++++++++++++
 src/e2e/liveBackendProbe.js                  |  9 ++++++++-
 src/e2e/liveConfig.js                        |  7 +++++++
 src/e2e/liveGlobalSetup.js                   |  7 +++++++
 src/test/liveE2eHarness.test.js              | 19 +++++++++++++++++++
 6 files changed, 66 insertions(+), 2 deletions(-)
```
