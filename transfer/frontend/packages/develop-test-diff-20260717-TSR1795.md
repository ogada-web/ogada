<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-07-17T17:05:19Z -->
# frontend develop→test diff meta — TSR 1795

- updated: 2026-07-17T17:05:19Z
- merge: FF `9e40c19`→`592a483` (1 commit · ALL SYNCED+PUSHED · pending **1→0**)
- commits:
  - `592a483` fix(v1.2.1/M12): lockstep SSO portal path allowlist with BE
- files: 2 (+126/−4)
- related: 26/26 PASS (accountingBpo+AccountingBpoPage · 5.13s · +3 vs TSR1794)
- post-merge npm: 2699/2699 PASS (883.33s, 480 files · +3 vs TSR1794)
- build: 1231 modules PASS (9.22s · Δ0 modules)
- audit: 0 high
- live E2E: 0 PASS / 149 SKIP / 0 FAIL (34.57s · bootstrap-disabled)
- origin/test: ALL SYNCED+PUSHED `@592a483`
- QA: QA-20260717-B583 Fixed · Open 0(FE) · cross-stream SYNCED(BE `@bfe6b3f` local · FE `@592a483`) · origin/test BE **734** unpushed

## Diffstat
```
 src/utils/accountingBpo.js      | 66 +++++++++++++++++++++++++++++++++++++++--
 src/utils/accountingBpo.test.js | 64 ++++++++++++++++++++++++++++++++++++++-
 2 files changed, 126 insertions(+), 4 deletions(-)
```

## Notes
- QA-B583: FE `isAllowlistedAccountingBpoSsoPortalUrl` HTTPS+sujifine host+`/carefor_login` path allowlist · reject non-443/query/fragment/userinfo · BE QA-B581 `@bfe6b3f` lockstep.
- Verification SHA identical on develop / test / origin/test / origin/develop · tests measured at `@592a483`.
- operation BLOCK: origin/test push **734 BE** + QA-B95.
