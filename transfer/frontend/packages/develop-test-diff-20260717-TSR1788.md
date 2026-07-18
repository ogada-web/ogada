<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-07-17T14:35:48Z -->
# frontend develop→test diff meta — TSR 1788

- updated: 2026-07-17T14:35:48Z
- merge: FF `ce2325c`→`2e06d5a` (1 commit · ALL SYNCED+PUSHED · pending **1→0**)
- commits:
  - `2e06d5a` feat(v1.2.1/v3): wire program schedule photo upload
- files: 8 (+337/−0)
- related: 12/12 PASS (programSchedulePhotoServices + ProgramSchedulePhotoUpload + programsPhoto + ProgramsPage · 9.25s · +12)
- post-merge npm: 2694/2694 PASS (883.58s, 480 files · +8 vs TSR1786)
- build: 1231 modules PASS (9.24s · +1 vs TSR1786)
- audit: 0 high
- live E2E: 0 PASS / 149 SKIP / 0 FAIL (34.46s · bootstrap-disabled)
- origin/test: ALL SYNCED+PUSHED `@2e06d5a`
- QA: QA-20260717-B577 Fixed · Open 0(FE) · cross-stream SYNCED(BE `@1b8c764` · FE ALL SYNCED+PUSHED `@2e06d5a`)

## Diffstat
```
 src/api/programSchedulePhotoServices.test.js       | 30 +++++++
 src/api/services.js                                | 15 ++++
 .../programs/ProgramSchedulePhotoUpload.jsx        | 93 ++++++++++++++++++++++
 .../programs/ProgramSchedulePhotoUpload.test.jsx   | 75 +++++++++++++++++
 src/config/programs.js                             | 29 +++++++
 src/config/programsPhoto.test.js                   | 36 +++++++++
 src/pages/ProgramsPage.jsx                         | 22 +++++
 src/pages/ProgramsPage.test.jsx                    | 37 +++++++++
 8 files changed, 337 insertions(+)
```

## Notes
- v3: FE wire for `POST /programs/schedule/{id}/photo` — RBAC + JPEG/PNG/WEBP validation · lockstep with BE QA-B576 `@1b8c764`.
- cross-stream SYNCED · operation BLOCK: origin/test push **731 BE** + QA-B95.
