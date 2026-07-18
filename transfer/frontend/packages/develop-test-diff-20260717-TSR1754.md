# frontend develop→test diff meta — TSR 1754

- updated: 2026-07-17T03:08:30Z
- merge: FF `1c84f0f`→`5ce4726` (1 commit · PUSHED/SYNCED)
- commits:
  - `5ce4726` fix(v1.2.1/QA-B95): decode bidi long-alias entities on live-e2e paths
- files: 4 (+79/-5)
- related: 220/220 PASS (2.80s, 2 files · +1 vs TSR1752)
- core QA-B95: 220/220
- post-merge npm: 2664/2664 PASS (882.91s, 477 files · +1 vs TSR1752 2663)
- build: 1230 modules PASS (10.82s)
- audit: 0 high
- live E2E: 0 PASS / 149 SKIP / 0 FAIL (35.17s · bootstrap-disabled)
- origin/test: PUSHED/SYNCED `1c84f0f`→`5ce4726`
- QA: QA-20260717-B549 Fixed · Open 0(FE) · Open 0 residual

## Diffstat
```
 src/e2e/liveBackendProbe.js     | 17 +++++++++++++++--
 src/e2e/liveConfig.js           | 15 +++++++++++++--
 src/e2e/liveGlobalSetup.js      | 15 +++++++++++++--
 src/test/liveE2eHarness.test.js | 37 +++++++++++++++++++++++++++++++++++++
 4 files changed, 79 insertions(+), 5 deletions(-)
```
