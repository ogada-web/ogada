# frontend develop→test diff meta — TSR 1747

- updated: 2026-07-17T00:38:30Z
- merge: FF `6fceb8d`→`d6be05c` (1 commit)
- commit: `d6be05c` fix(v1.2.1/QA-B95): decode curly-brace wrapping HTML entities
- files: 6 (+55/-0)
- related: 215/215 PASS (2.65s, 2 files · +2 vs TSR1745)
- core QA-B95: 215/215
- post-merge npm: 2659/2659 PASS (877.25s, 477 files · +2 vs TSR1745 2657)
- build: 1230 modules PASS (9.89s)
- audit: 0 high
- live E2E: 0 PASS / 149 SKIP / 0 FAIL (37.80s · bootstrap-disabled)
- origin/test: PUSHED/SYNCED `6fceb8d`→`d6be05c`
- QA: QA-20260717-B544 Fixed · Open 0

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
