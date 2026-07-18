<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-07-17T18:22:35Z -->
# frontend develop→test diff meta — TSR 1798

- updated: 2026-07-17T18:22:35Z
- merge: FF `bc1d343`→`8e28fe0` (1 commit · ALL SYNCED+PUSHED · pending **1→0**)
- commits:
  - `8e28fe0` fix(v1.2.1/v3): verify program photo magic bytes before upload (SEC-D25)
- files: 5 (+189/−21)
- related: 15/15 PASS (programsPhoto+ProgramSchedulePhotoUpload+ProgramsPage+programSchedulePhotoServices · 9.27s · +2 vs COD claim baseline carry)
- post-merge npm: 2702/2702 PASS (885.10s, 480 files · +3 vs TSR1795 2699)
- build: 1231 modules PASS (11.08s · Δ0 modules)
- audit: 0 high
- live E2E: 0 PASS / 149 SKIP / 0 FAIL (34.29s · bootstrap-disabled)
- origin/test: ALL SYNCED+PUSHED `@8e28fe0`
- QA: QA-20260717-B586 Fixed · Open 0(FE) · cross-stream SYNCED(BE `@d1ff63a` local · FE `@8e28fe0`) · origin/test BE **736** unpushed

## Diffstat
```
 .../programs/ProgramSchedulePhotoUpload.jsx        |   2 +-
 .../programs/ProgramSchedulePhotoUpload.test.jsx   |  26 ++++-
 src/config/programs.js                             | 105 ++++++++++++++++++++-
 src/config/programsPhoto.test.js                   |  74 ++++++++++++---
 src/pages/ProgramsPage.test.jsx                    |   3 +-
 5 files changed, 189 insertions(+), 21 deletions(-)
```

## Notes
- QA-B586: FE `validateProgramSchedulePhotoFile` JPEG/PNG/WEBP magic-byte fail-closed before upload · MIME spoof/truncated reject · BE QA-B585 `@d1ff63a` lockstep (SEC-D25).
- Verification SHA identical on develop / test / origin/test / origin/develop · tests measured at `@8e28fe0`.
- operation BLOCK: origin/test push **736 BE** + QA-B95.
