<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-07-17T19:36:13Z -->
# frontend develop→test diff meta — TSR 1801

- updated: 2026-07-17T19:36:13Z
- merge: FF `8e28fe0`→`dc81f6e` (2 commits · ALL SYNCED+PUSHED · pending **2→0**)
- commits:
  - `090ac10` test(v1.2.1/QA-B95): lock mid-token NoBreakSpace marker decode
  - `dc81f6e` test(v1.2.1/QA-B95): lock semicolon-optional NoBreakSpace marker decode
- files: 6 (+70/−2)
- related: 246/246 PASS (notificationChannelStatus+liveE2eHarness · 3.11s · +4 vs TSR1798)
- post-merge npm: 2706/2706 PASS (884.25s, 480 files · +4 vs TSR1798 2702)
- build: 1231 modules PASS (10.33s · Δ0 modules)
- audit: 0 high
- live E2E: 0 PASS / 149 SKIP / 0 FAIL (35.77s · bootstrap-disabled)
- origin/test: ALL SYNCED+PUSHED `@dc81f6e`
- QA: QA-20260717-B588 + QA-20260717-B590 Fixed · Open 0(FE) · cross-stream SYNCED(BE `@c19bfa6` local · FE `@dc81f6e`) · origin/test BE **738** unpushed

## Diffstat
```
 src/config/notificationChannelStatus.js      |  4 +++-
 src/config/notificationChannelStatus.test.js | 30 ++++++++++++++++++++++++++++
 src/e2e/liveBackendProbe.js                  |  4 +++-
 src/e2e/liveConfig.js                        |  2 ++
 src/e2e/liveGlobalSetup.js                   |  2 ++
 src/test/liveE2eHarness.test.js              | 30 ++++++++++++++++++++++++++++
 6 files changed, 70 insertions(+), 2 deletions(-)
```

## Notes
- QA-B588: mid-token `&NoBreakSpace;` strip-empty so bootstrap markers rejoin (BE QA-B587 lockstep).
- QA-B590: semicolon-optional `&NoBreakSpace-` / `&NOBREAKSPACE-` mid-token decode (BE QA-B589 `@c19bfa6` lockstep).
- Verification SHA identical on develop / test / origin/test / origin/develop · tests measured at `@dc81f6e`.
- operation BLOCK: origin/test push **738 BE** + QA-B95.
