# develop→test diff — TSR 1523 (2026-07-14)

- stream: frontend
- merge: FF `e18ee5c` → `585155c` (pending 1→0)
- commit: `585155c feat(v1.2.1/M11): wire simple payment statement reports page`
- pre-merge related: 24/24 PASS (8.72s, 5 files)
- post-merge: 2396/2396 PASS (801.17s, 458 files)
- build: 1210 modules PASS (9.04s)
- audit: 0 high
- live E2E: 116 PASS / 33 SKIP / 0 FAIL (39.49s)
- origin/test: PUSHED (`e18ee5c`→`585155c`)
- QA: QA-B377 Fixed · residual Open QA-B376 (BE pending 1 @c455145)

## Commits

```
585155c feat(v1.2.1/M11): wire simple payment statement reports page
```

## Diffstat

```
 src/App.jsx                                 |  12 +
 src/api/services.js                         |  11 +
 src/api/staffPayrollServices.test.js        |  48 +++-
 src/components/ui/StaffContextNav.jsx       |   1 +
 src/components/ui/StaffContextNav.test.jsx  |   4 +
 src/config/competitorModuleCoverage.js      |   4 +-
 src/config/competitorModuleCoverage.test.js |   4 +-
 src/layout/navConfig.js                     |   6 +
 src/pages/StaffPayrollLedgerPage.jsx        |   6 +-
 src/pages/StaffPayrollReportsPage.jsx       | 411 ++++++++++++++++++++++++++++
 src/pages/StaffPayrollReportsPage.test.jsx  | 145 ++++++++++
 src/utils/staffPayrollLedger.js             |  63 ++++-
 src/utils/staffPayrollLedger.test.js        |  14 +-
 13 files changed, 717 insertions(+), 12 deletions(-)
```
