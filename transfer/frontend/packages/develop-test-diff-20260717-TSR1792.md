<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-07-17T15:32:20Z -->
# frontend develop→test diff meta — TSR 1792

- updated: 2026-07-17T15:32:20Z
- merge: FF `2e06d5a`→`8e74b07` (1 commit · ALL SYNCED+PUSHED · pending **1→0**)
- commits:
  - `8e74b07` fix(v1.2.1/v3): accept program photo content-type parameters
- files: 2 (+57/−2)
- related: 8/8 PASS (programsPhoto · content-type normalize · 5.93s)
- post-merge npm: 2695/2695 PASS (885.32s, 480 files · +1 vs TSR1788/1789)
- build: 1231 modules PASS (11.07s · Δ0 modules)
- audit: 0 high
- live E2E: 0 PASS / 149 SKIP / 0 FAIL (35.46s · bootstrap-disabled)
- origin/test: ALL SYNCED+PUSHED `@8e74b07`
- QA: QA-20260717-B579 Fixed · Open 0(FE) · cross-stream SYNCED(BE `@72a6534` · FE ALL SYNCED+PUSHED `@8e74b07`)

## Diffstat
```
 src/config/programs.js           | 31 +++++++++++++++++++++++++++++--
 src/config/programsPhoto.test.js | 28 ++++++++++++++++++++++++++++
 2 files changed, 57 insertions(+), 2 deletions(-)
```

## Notes
- v3: FE `normalizeProgramSchedulePhotoContentType` — accept `image/jpeg; charset=binary` (BE QA-B578 `@72a6534` lockstep).
- Verification SHA identical on develop / test / origin/test · tests measured at `@8e74b07`.
- cross-stream SYNCED · operation BLOCK: origin/test push **732 BE** + QA-B95.
