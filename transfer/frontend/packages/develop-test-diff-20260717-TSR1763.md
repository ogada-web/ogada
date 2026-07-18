# frontend develop→test diff meta — TSR 1763

- updated: 2026-07-17T05:11:58Z
- merge: FF `a364f97`→`ac3af73` (1 commit · PUSHED/SYNCED)
- commits:
  - `ac3af73` fix(v1.2.1/QA-B95): decode OpenCurly* quote HTML entity aliases
- files: 6 (+58/-2)
- related: 226/226 PASS (2.72s, 2 files · +2 vs TSR1761 224)
- core QA-B95: 226/226
- post-merge npm: 2670/2670 PASS (878.01s, 477 files · +2 vs TSR1760 2668)
- build: 1230 modules PASS (9.15s)
- audit: 0 high
- live E2E: 0 PASS / 149 SKIP / 0 FAIL (34.50s · bootstrap-disabled)
- origin/test: PUSHED/SYNCED `a364f97`→`ac3af73`
- QA: QA-20260717-B555 Fixed · Open 0 · cross-stream SYNCED(BE `@df2c1a0`)

## Diffstat
```
 src/config/notificationChannelStatus.js      |  7 ++++++-
 src/config/notificationChannelStatus.test.js | 17 +++++++++++++++++
 src/e2e/liveBackendProbe.js                  |  7 ++++++-
 src/e2e/liveConfig.js                        |  5 +++++
 src/e2e/liveGlobalSetup.js                   |  5 +++++
 src/test/liveE2eHarness.test.js              | 19 +++++++++++++++++++
 6 files changed, 58 insertions(+), 2 deletions(-)
```
