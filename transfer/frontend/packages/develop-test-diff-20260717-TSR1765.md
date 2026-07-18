# frontend develop→test diff meta — TSR 1765

- updated: 2026-07-17T06:02:07Z
- merge: FF `ac3af73`→`694266e` (2 commits · PUSHED/SYNCED)
- commits:
  - `694266e` fix(v1.2.1/QA-B95): decode Left/Right Quote HTML entity aliases
  - `0438a17` ux(a11y): promote 9 undefined ds-* text/spacing/group classes (UXD-187)
- files: 7 (+130/−6)
- related: 228/228 PASS (2.68s, 2 files · +2 vs TSR1763 226)
- core QA-B95: 228/228
- post-merge npm: 2672/2672 PASS (882.90s, 477 files · +2 vs TSR1763 2670)
- build: 1230 modules PASS (11.13s)
- audit: 0 high
- live E2E: 0 PASS / 149 SKIP / 0 FAIL (34.33s · bootstrap-disabled)
- origin/test: PUSHED/SYNCED `ac3af73`→`694266e`
- QA: QA-20260717-B557 Fixed · Open 0 · cross-stream SYNCED(BE `@a9bd7c0`)

## Diffstat
```
 src/config/notificationChannelStatus.js      |  8 +++-
 src/config/notificationChannelStatus.test.js | 17 +++++++
 src/e2e/liveBackendProbe.js                  |  8 +++-
 src/e2e/liveConfig.js                        |  6 ++-
 src/e2e/liveGlobalSetup.js                   |  6 ++-
 src/styles/components.css                    | 72 ++++++++++++++++++++++++++++
 src/test/liveE2eHarness.test.js              | 19 ++++++++
 7 files changed, 130 insertions(+), 6 deletions(-)
```
