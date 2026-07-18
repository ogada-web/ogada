<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-07-17T20:27:30Z -->
# frontend develop→test diff meta — TSR 1803

- updated: 2026-07-17T20:27:30Z
- merge: FF `dc81f6e`→`e16f432` (2 commits · ALL SYNCED+PUSHED · pending **2→0**)
- commits:
  - `b2eb059` ux(a11y): hide staff status filters on print and wire photo error ARIA (UXD-190)
  - `e16f432` fix(v1.2.1/v3): verify client photo magic bytes before upload (SEC-D25 · QA-B592)
- files: 11 (+510/−3)
- related: 25/25 PASS (clientPhotos+ClientPhotoUpload+ProgramSchedulePhotoUpload+StaffStatusReport · 13.37s · +16 vs TSR1801)
- post-merge npm: 2715/2715 PASS (886.31s, 483 files · +9 vs TSR1801 2706)
- build: 1233 modules PASS (9.23s · +2 modules)
- audit: 0 high
- live E2E: 0 PASS / 149 SKIP / 0 FAIL (34.38s · bootstrap-disabled)
- origin/test: ALL SYNCED+PUSHED `@e16f432`
- QA: QA-20260717-B592 Fixed · UXD-190 absorbed · Open 0(FE) · cross-stream SYNCED(BE `@cdba083` local · FE `@e16f432`) · origin/test BE **739** unpushed

## Diffstat
```
 src/api/clientPhotoServices.test.js                |  30 +++++
 src/api/services.js                                |  15 +++
 src/components/clients/ClientPhotoUpload.jsx       |  96 +++++++++++++
 src/components/clients/ClientPhotoUpload.test.jsx  |  84 ++++++++++++
 .../programs/ProgramSchedulePhotoUpload.jsx        |   5 +-
 .../programs/ProgramSchedulePhotoUpload.test.jsx   |  11 +-
 src/config/clientPhotos.js                         | 149 +++++++++++++++++++++
 src/config/clientPhotos.test.js                    |  92 +++++++++++++
 src/pages/ClientDetailPage.jsx                     |  25 ++++
 src/pages/StaffStatusReportPage.jsx                |   2 +-
 src/pages/StaffStatusReportPage.test.jsx           |   4 +
 11 files changed, 510 insertions(+), 3 deletions(-)
```

## Notes
- QA-B592: FE SEC-D25 client profile photo FileReader 12-byte magic + Content-Type `;param` normalize + `ClientDetailPage` wire (BE QA-B591 `@cdba083` lockstep).
- UXD-190: print CSS hide staff status filters · program photo upload error `role="alert"` ARIA.
- Verification SHA identical on develop / test / origin/test / origin/develop · tests measured at `@e16f432`.
- operation BLOCK: origin/test push **739 BE** + QA-B95.
