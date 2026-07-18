# frontend develop→test diff meta — TSR 1770

- updated: 2026-07-17T08:08:00Z
- merge: FF `56fa1c0`→`a280437` (1 commit · PUSHED/SYNCED)
- commits:
  - `a280437` fix(v1.2.1/QA-B95): decode guillemet quote HTML entity aliases
- files: 6 (+59/−4)
- related: 232/232 PASS (2.70s, 2 files · +2 vs TSR1768 230)
- core QA-B95: 232/232
- post-merge npm: 2676/2676 PASS (883.73s, 477 files · +2 vs TSR1768 2674)
- build: 1230 modules PASS (9.25s)
- audit: 0 high
- live E2E: 0 PASS / 149 SKIP / 0 FAIL (33.75s · bootstrap-disabled)
- origin/test: PUSHED/SYNCED `56fa1c0`→`a280437`
- QA: QA-20260717-B562 Fixed · Open 0(FE) · cross-stream BLOCK(BE pending 2 `@23ce552`+`@3b0b6b9` · QA-B559+B561)

## Diffstat
```
 src/config/notificationChannelStatus.js      |  7 ++++++-
 src/config/notificationChannelStatus.test.js | 16 ++++++++++++++++
 src/e2e/liveBackendProbe.js                  |  7 ++++++-
 src/e2e/liveConfig.js                        |  7 ++++++-
 src/e2e/liveGlobalSetup.js                   |  7 ++++++-
 src/test/liveE2eHarness.test.js              | 19 +++++++++++++++++++
 6 files changed, 59 insertions(+), 4 deletions(-)
```

## Notes
- FE guillemet lockstep for BE QA-B561 (`@3b0b6b9`) — BE merge still pending on backend stream.
- operation BLOCK: origin/test push **723 BE** + QA-B559 + QA-B561 + QA-B95.
