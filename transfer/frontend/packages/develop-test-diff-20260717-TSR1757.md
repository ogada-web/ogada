# frontend develop→test diff meta — TSR 1757

- updated: 2026-07-17T03:45:30Z
- merge: FF `5ce4726`→`40c85df` (1 commit · PUSHED/SYNCED)
- commits:
  - `40c85df` fix(v1.2.1/QA-B95): decode MathML long angle-bracket HTML entities
- files: 6 (+55/-6)
- related: 222/222 PASS (2.62s, 2 files · +2 vs TSR1755)
- core QA-B95: 222/222
- post-merge npm: 2666/2666 PASS (882.54s, 477 files · +2 vs TSR1754 2664)
- build: 1230 modules PASS (9.41s)
- audit: 0 high
- live E2E: 0 PASS / 149 SKIP / 0 FAIL (34.78s · bootstrap-disabled)
- origin/test: PUSHED/SYNCED `5ce4726`→`40c85df`
- QA: QA-20260717-B552 Fixed · Open 0(FE) · residual QA-B551(BE)

## Diffstat
```
 src/config/notificationChannelStatus.js      |  7 +++++--
 src/config/notificationChannelStatus.test.js | 18 ++++++++++++++++++
 src/e2e/liveBackendProbe.js                  |  7 +++++--
 src/e2e/liveConfig.js                        |  5 ++++-
 src/e2e/liveGlobalSetup.js                   |  5 ++++-
 src/test/liveE2eHarness.test.js              | 19 +++++++++++++++++++
 6 files changed, 55 insertions(+), 6 deletions(-)
```
