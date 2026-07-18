<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-07-17T13:58:37Z -->
# frontend develop→test diff meta — TSR 1786

- updated: 2026-07-17T13:58:37Z
- merge: FF `d3e282b`→`ce2325c` (1 commit · ALL SYNCED+PUSHED · pending **1→0**)
- commits:
  - `ce2325c` fix(v1.2.1/QA-B95): accept semicolon-optional named-num entities
- files: 4 (+14/−11)
- related: 240/240 PASS (notificationChannelStatus + liveE2eHarness · 2.67s · Δ0 · in-place expand)
- post-merge npm: 2686/2686 PASS (878.83s, 477 files · Δ0 vs TSR1784)
- build: 1230 modules PASS (9.76s · frontend-test reconfirm)
- audit: 0 high
- live E2E: 0 PASS / 149 SKIP / 0 FAIL (39.14s · bootstrap-disabled · TSR reconfirm; prior 35.94s)
- origin/test: ALL SYNCED+PUSHED `@ce2325c`
- QA: QA-20260717-B575 Fixed · Open 0(FE) · cross-stream SYNCED(BE `@b7f4337` local · FE ALL SYNCED+PUSHED `@ce2325c`)

## Diffstat
```
 src/config/notificationChannelStatus.js      | 4 ++--
 src/config/notificationChannelStatus.test.js | 8 +++++---
 src/e2e/liveBackendProbe.js                  | 4 ++--
 src/test/liveE2eHarness.test.js              | 9 +++++----
 4 files changed, 14 insertions(+), 11 deletions(-)
```

## Notes
- QA-B95: FE semicolon-optional `&num` named-num decode (`guardian&num45not-ready` → `guardian-not-ready`) · channel-status + live probe lockstep.
- cross-stream SYNCED locally · operation BLOCK: origin/test push **730 BE** + QA-B95.
- Independent reconfirm: related 240/240 · npm 2686/2686 · build 1230 · audit 0 · live 0/149/0 — matches TSR1786 gate.
