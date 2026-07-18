# frontend develop→test diff meta — TSR 1760

- updated: 2026-07-17T04:25:10Z
- merge: FF `40c85df`→`a364f97` (1 commit · PUSHED/SYNCED)
- commits:
  - `a364f97` fix(v1.2.1/QA-B95): decode typographic quote entities in live blockers
- files: 6 (+69/-6)
- related: 224/224 PASS (2.59s, 2 files · +2 vs TSR1758 222)
- core QA-B95: 224/224
- post-merge npm: 2668/2668 PASS (879.51s, 477 files · +2 vs TSR1757 2666)
- build: 1230 modules PASS (10.89s)
- audit: 0 high
- live E2E: 0 PASS / 149 SKIP / 0 FAIL (34.47s · bootstrap-disabled)
- origin/test: PUSHED/SYNCED `40c85df`→`a364f97`
- QA: QA-20260717-B553 Fixed · Open 0 · cross-stream SYNCED(BE `@a0c1fe6`)

## Diffstat
```
 src/config/notificationChannelStatus.js      | 11 ++++++++++-
 src/config/notificationChannelStatus.test.js | 11 +++++++++++
 src/e2e/liveBackendProbe.js                  | 11 ++++++++++-
 src/e2e/liveConfig.js                        | 12 ++++++++++--
 src/e2e/liveGlobalSetup.js                   | 12 ++++++++++--
 src/test/liveE2eHarness.test.js              | 18 ++++++++++++++++++
 6 files changed, 69 insertions(+), 6 deletions(-)
```
