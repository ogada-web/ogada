<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-07-17T12:32:57Z -->
# frontend develop→test diff meta — TSR 1782

- updated: 2026-07-17T12:32:57Z
- merge: FF `420286e`→`9a48e13` (1 commit · PUSHED/SYNCED · pending **1→0**)
- commits:
  - `9a48e13` fix(v1.2.1/QA-B95): filter null/blank effective operation blockers
- files: 3 (+118/−6)
- related: 182/182 PASS (liveE2eHarness.test.js · 1.60s · +2)
- post-merge npm: 2684/2684 PASS (872.38s, 477 files · +2 vs TSR1780)
- build: 1230 modules PASS (9.44s)
- audit: 0 high
- live E2E: 0 PASS / 149 SKIP / 0 FAIL (34.59s · bootstrap-disabled)
- origin/test: PUSHED/SYNCED `420286e`→`9a48e13`
- QA: QA-20260717-B571 Fixed · Open 0(FE) · cross-stream SYNCED(BE `@0dfc992` · FE ALL SYNCED+PUSHED `@9a48e13`)

## Diffstat
```
 src/e2e/liveBackendProbe.js     | 47 +++++++++++++++++++++++++++++++
 src/e2e/liveGlobalSetup.js      | 15 ++++++----
 src/test/liveE2eHarness.test.js | 62 ++++++++++++++++++++++++++++++++++++++++-
 3 files changed, 118 insertions(+), 6 deletions(-)
```

## Notes
- QA-B95: `resolveEffectiveOperationBlockers`/`resolveSuppressedBootstrapOperationBlockers` drop null/blank tokens (BE `@0dfc992` lockstep).
- liveGlobalSetup reuses shared helpers for computed effective/suppressed paths.
- cross-stream SYNCED locally · operation BLOCK: origin/test push **728 BE** + QA-B95.
