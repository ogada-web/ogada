<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-07-17T13:24:14Z -->
# frontend develop→test diff meta — TSR 1784

- updated: 2026-07-17T13:24:14Z
- merge: FF `9a48e13`→`d3e282b` (1 commit · PUSHED/SYNCED · pending **1→0**)
- commits:
  - `d3e282b` fix(v1.2.1/QA-B95): accept semicolon-optional amp HTML entities
- files: 6 (+47/−5)
- related: 240/240 PASS (notificationChannelStatus + liveE2eHarness · 2.72s · +2)
- post-merge npm: 2686/2686 PASS (883.65s, 477 files · +2 vs TSR1782)
- build: 1230 modules PASS (9.39s)
- audit: 0 high
- live E2E: 0 PASS / 149 SKIP / 0 FAIL (34.37s · bootstrap-disabled)
- origin/test: PUSHED/SYNCED `9a48e13`→`d3e282b`
- QA: QA-20260717-B573 Fixed · Open 0(FE) · cross-stream SYNCED(BE `@7389ef0` · FE ALL SYNCED+PUSHED `@d3e282b`)

## Diffstat
```
 src/config/notificationChannelStatus.js      |  5 ++++-
 src/config/notificationChannelStatus.test.js | 13 +++++++++++++
 src/e2e/liveBackendProbe.js                  |  6 ++++--
 src/e2e/liveConfig.js                        |  4 +++-
 src/e2e/liveGlobalSetup.js                   |  4 +++-
 src/test/liveE2eHarness.test.js              | 20 ++++++++++++++++++++
 6 files changed, 47 insertions(+), 5 deletions(-)
```

## Notes
- QA-B95: FE `&amp` semicolon-optional decode before numeric refs (`bootstrap&amp#45disabled` → `bootstrap-disabled`) · BE LiveE2eOperationReadinessSupport lockstep.
- cross-stream SYNCED locally · operation BLOCK: origin/test push **729 BE** + QA-B95.
