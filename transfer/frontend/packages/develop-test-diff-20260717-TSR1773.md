# frontend develop→test diff meta — TSR 1773

- updated: 2026-07-17T08:47:10Z
- merge: FF `a280437`→`3f7bb94` (1 commit · PUSHED/SYNCED)
- commits:
  - `3f7bb94` fix(v1.2.1/QA-B95): decode prime/double-prime quote HTML entity aliases
- files: 6 (+57/−2)
- related: 234/234 PASS (2.69s, 2 files · +2 vs TSR1771 232)
- core QA-B95: 234/234
- post-merge npm: 2678/2678 PASS (879.79s, 477 files · +2 vs TSR1770 2676)
- build: 1230 modules PASS (12.93s)
- audit: 0 high
- live E2E: 0 PASS / 149 SKIP / 0 FAIL (36.79s · bootstrap-disabled)
- origin/test: PUSHED/SYNCED `a280437`→`3f7bb94`
- QA: QA-20260717-B564 Fixed · Open 0(FE) · cross-stream BLOCK(BE pending 3 `@23ce552`+`@3b0b6b9`+`@34c16cd` · QA-B559+B561+B563)

## Diffstat
```
 src/config/notificationChannelStatus.js      |  7 ++++++-
 src/config/notificationChannelStatus.test.js | 16 ++++++++++++++++
 src/e2e/liveBackendProbe.js                  |  7 ++++++-
 src/e2e/liveConfig.js                        |  5 +++++
 src/e2e/liveGlobalSetup.js                   |  5 +++++
 src/test/liveE2eHarness.test.js              | 19 +++++++++++++++++++
 6 files changed, 57 insertions(+), 2 deletions(-)
```

## Notes
- FE prime/double-prime lockstep for BE QA-B563 (`@34c16cd`) — BE merge still pending on backend stream.
- operation BLOCK: origin/test push **723 BE** + QA-B559 + QA-B561 + QA-B563 + QA-B95.
