# frontend develop→test diff meta — TSR 1775

- updated: 2026-07-17T10:09:31Z
- merge: FF `3f7bb94`→`93f77e1` (1 commit · PUSHED/SYNCED)
- commits:
  - `93f77e1` fix(v1.2.1/QA-B95): decode long prime HTML entity aliases
- files: 6 (+55/−8)
- related: 234/234 PASS (3.32s, 2 · Δ0 vs TSR1774)
- core QA-B95: 234/234
- post-merge npm: 2678/2678 PASS (880.02s, 477 files · Δ0)
- build: 1230 modules PASS (9.44s)
- audit: 0 high
- live E2E: 0 PASS / 149 SKIP / 0 FAIL (34.28s · bootstrap-disabled)
- origin/test: PUSHED/SYNCED `3f7bb94`→`93f77e1`
- QA: QA-20260717-B565 Fixed · Open 0(FE) · cross-stream BLOCK(BE pending 4 · QA-B559+B561+B563 · `@31b10d5` extended-prime WIP)

## Diffstat
```
 src/config/notificationChannelStatus.js      |  8 ++++++--
 src/config/notificationChannelStatus.test.js | 14 +++++++++++++-
 src/e2e/liveBackendProbe.js                  |  8 ++++++--
 src/e2e/liveConfig.js                        |  6 +++++-
 src/e2e/liveGlobalSetup.js                   |  6 +++++-
 src/test/liveE2eHarness.test.js              | 21 ++++++++++++++++++++-
 6 files changed, 55 insertions(+), 8 deletions(-)
```

## Notes
- FE long-prime (`&bprime;`/`&tprime;`/`&qprime;`/`&backprime;`) lockstep for BE QA-B563 (`@34c16cd`) — BE merge still pending on backend stream.
- operation BLOCK: origin/test push **725 BE** + QA-B559 + QA-B561 + QA-B563 + QA-B95.
