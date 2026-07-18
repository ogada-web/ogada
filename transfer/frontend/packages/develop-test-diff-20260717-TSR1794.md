<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-07-17T16:31:51Z -->
# frontend develop→test diff meta — TSR 1794

- updated: 2026-07-17T16:31:51Z
- merge: FF `8e74b07`→`9e40c19` (2 commits · ALL SYNCED+PUSHED · pending **2→0**)
- commits:
  - `bfd171d` ux(a11y): promote ds-stack--tight micro vertical stack (UXD-189)
  - `9e40c19` fix(v1.2.1/QA-B95): sync liveConfig named-num entity decode
- files: 4 (+46/−4)
- related: 241/241 PASS (liveE2eHarness+notificationChannelStatus · 2.71s · +1 vs TSR1792)
- post-merge npm: 2696/2696 PASS (880.62s, 480 files · +1 vs TSR1792)
- build: 1231 modules PASS (9.57s · Δ0 modules)
- audit: 0 high
- live E2E: 0 PASS / 149 SKIP / 0 FAIL (42.14s · bootstrap-disabled)
- origin/test: ALL SYNCED+PUSHED `@9e40c19`
- QA: QA-20260717-B582 Fixed · Open 0(FE) · cross-stream BLOCK(BE pending 1 `@759b15e` · FE ALL SYNCED `@9e40c19`)

## Diffstat
```
 src/e2e/liveConfig.js           |  4 ++--
 src/e2e/liveGlobalSetup.js      |  4 ++--
 src/styles/components.css       | 13 +++++++++++++
 src/test/liveE2eHarness.test.js | 29 +++++++++++++++++++++++++++++
 4 files changed, 46 insertions(+), 4 deletions(-)
```

## Notes
- QA-B582: FE `liveConfig.js`+`liveGlobalSetup.js` semicolon-optional named-num (`&num45`/`&NUM45`) lockstep with BE QA-B580 `@759b15e`.
- UXD-189: `ds-stack--tight` micro vertical stack token (a11y spacing).
- Verification SHA identical on develop / test / origin/test · tests measured at `@9e40c19`.
- cross-stream BLOCK: BE develop `@759b15e` pending 1 (QA-B581) · operation BLOCK: origin/test push **733 BE** + QA-B95.
