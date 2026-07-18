<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-07-17T21:36:57Z -->
# frontend develop→test diff meta — TSR 1807

- updated: 2026-07-17T21:36:57Z
- merge: SKIP (pending `cf28a2e`→`8b164c3`, 1 commit not absorbed)
- commits:
  - `8b164c3` fix(v1.2.1/v3): verify grade-history and refresher magic bytes before upload (SEC-D25 · QA-B596)
- files: 9 (+455/−70)
- related: `StaffRefresherTrainingPage.test.jsx` **3/4 PASS (1 FAIL)** (6.37s)
- full suite: **2726/2727 PASS (1 FAIL)** (886.07s, 486 files)
- failing assertion: `uploadStaffRefresherTrainingCertificateApi` expected call with `("staff-1", File)` but call count **0**
- build: 1233 modules PASS (9.68s)
- audit: 0 high
- live E2E: SKIP (merge 0; carry `0/149/0`, TSR1805)
- origin/test: unchanged `@cf28a2e`
- QA: **QA-20260717-B597 Open(BLOCK/HIGH)** · transfer BLOCK(FE)

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
 9 files changed, 455 insertions(+), 70 deletions(-)
```

## Notes
- `npm test` is locked by `scripts/npm-test-locked.sh`, but it executes against `src/frontend` (develop), so pending commit validation surfaced pre-merge regression before test-branch absorption.
- Planner/Coder action needed: fix `StaffRefresherTrainingPage` upload flow/test mismatch, then re-run locked suite and perform develop→test FF merge.
