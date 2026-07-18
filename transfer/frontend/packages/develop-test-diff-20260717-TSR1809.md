<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-07-17T22:21:45Z -->
# frontend develop→test diff meta — TSR 1809

- updated: 2026-07-17T22:21:45Z
- merge: FF+PUSH `cf28a2e`→`4691856` (2 commits · ALL SYNCED+PUSHED · pending **2→0**)
- commits:
  - `8b164c3` fix(v1.2.1/v3): verify grade-history and refresher magic bytes before upload (SEC-D25 · QA-B596)
  - `4691856` fix(v1.2.1/QA-B597): align refresher certificate page upload fixture with SEC-D25 magic
- files: 10 (+491/−71)
- related: 13/13 PASS (StaffRefresherTrainingPage+Panel+staffRefresherTrainingCertificates · 7.94s)
- post-merge npm: 2728/2728 PASS (890.03s, 486 files · +5 vs TSR1805 2723)
- build: 1233 modules PASS (11.19s · Δ0 modules)
- audit: 0 high
- live E2E: 0 PASS / 149 SKIP / 0 FAIL (33.86s · bootstrap-disabled)
- origin/test: ALL SYNCED+PUSHED `@4691856`
- QA: QA-20260717-B597 Fixed · Open 0(FE) · cross-stream SYNCED(BE `@be64fda` local · FE `@4691856`) · origin/test BE **742** unpushed

## Diffstat
```
 .../staff/StaffRefresherCertificatePanel.jsx       |   2 +-
 .../staff/StaffRefresherCertificatePanel.test.jsx  |  25 +++-
 src/components/ui/GradeHistoryAttachmentPanel.jsx  |   2 +-
 .../ui/GradeHistoryAttachmentPanel.test.jsx        |  28 +++--
 src/config/gradeHistoryAttachments.js              | 137 +++++++++++++++++---
 src/config/gradeHistoryAttachments.test.js         |  97 +++++++++++---
 src/config/staffRefresherTrainingCertificates.js   | 140 ++++++++++++++++++---
 .../staffRefresherTrainingCertificates.test.js     |  92 ++++++++++++++
 src/pages/StaffRefresherTrainingPage.jsx           |   2 +-
 src/pages/StaffRefresherTrainingPage.test.jsx      |  37 +++++-
 10 files changed, 491 insertions(+), 71 deletions(-)
```

## Notes
- QA-B596: FE SEC-D25 grade-history PDF/PNG + refresher-certificate PDF/PNG/JPEG FileReader 8-byte magic + Content-Type `;param` normalize (BE QA-B595 `@ed94521` lockstep).
- QA-B597: page upload test fixture `%PDF-1.4 mock` sync + MIME spoof reject lock (TSR1807 regression fix · product code unchanged).
- Verification SHA identical on develop / test / origin/test / origin/develop · tests measured at `@4691856`.
- operation BLOCK: origin/test push **742 BE** + QA-B95.
