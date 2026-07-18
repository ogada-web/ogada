# develop→test diff — TSR 1525 (2026-07-14)

- stream: frontend
- merge: FF `585155c` → `9ea151b` (pending 1→0)
- commit: `9ea151b feat(v1.2.1/M11): wire allowance/deduction master catalog basis page`
- pre-merge related: 25/25 PASS (8.26s, 5 files)
- post-merge: 2400/2400 PASS (830.73s, 459 files)
- build: 1211 modules PASS (8.76s)
- audit: 0 high
- live E2E: 116 PASS / 33 SKIP / 0 FAIL (40.90s)
- origin/test: PUSHED (`585155c`→`9ea151b`)
- QA: QA-B378 Fixed · residual Open QA-B376 (BE pending 2 @c455145+eca95e3)

## Commits

```
9ea151b feat(v1.2.1/M11): wire allowance/deduction master catalog basis page
```

## Diffstat

```
 src/App.jsx                                 |  12 ++
 src/api/services.js                         |   8 ++
 src/api/staffPayrollServices.test.js        |  32 +++++
 src/components/ui/StaffContextNav.jsx       |   1 +
 src/components/ui/StaffContextNav.test.jsx  |   4 +
 src/config/competitorModuleCoverage.js      |   4 +-
 src/config/competitorModuleCoverage.test.js |   4 +-
 src/layout/navConfig.js                     |   6 +
 src/pages/StaffPayrollBasisPage.jsx         | 207 ++++++++++++++++++++++++++++
 src/pages/StaffPayrollBasisPage.test.jsx    | 147 ++++++++++++++++++++
 src/utils/staffPayrollLedger.js             |  98 ++++++++++++-
 src/utils/staffPayrollLedger.test.js        |  57 ++++++--
 12 files changed, 559 insertions(+), 21 deletions(-)
```
