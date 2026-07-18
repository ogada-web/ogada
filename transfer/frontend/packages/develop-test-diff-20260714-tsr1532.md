# develop→test diff — TSR 1532 (2026-07-14)

- stream: frontend
- merge: FF `aa86734` → `02d185a` (pending 2→0)
- commits:
  - `d176581 ux(a11y/FE-16): harden US-PAYROLL-M11 payroll preview surfaces (UXD-174)`
  - `02d185a feat(v1.2.1/M11): wire retirement accrual preview page`
- pre-merge related: 43/43 PASS (18.54s, 8 files)
- post-merge: 2417/2417 PASS (827.07s, 461 files)
- build: 1213 modules PASS (9.01s)
- audit: 0 high
- live E2E: 116 PASS / 33 SKIP / 0 FAIL (37.52s)
- origin/test: PUSHED (`aa86734`→`02d185a`)
- QA: QA-B383 Fixed · Open 0 · cross-stream SYNCED (BE `@ff90532` · FE `@02d185a`)
- operation: BLOCK (QA-B116 origin/test 624 BE + QA-B95)

## Commits

```
02d185a feat(v1.2.1/M11): wire retirement accrual preview page
d176581 ux(a11y/FE-16): harden US-PAYROLL-M11 payroll preview surfaces (UXD-174)
```

## Diffstat

```
 src/App.jsx                                        |  12 +
 src/api/services.js                                |  11 +
 src/api/staffPayrollServices.test.js               |  45 +++
 src/components/ui/StaffContextNav.jsx              |   1 +
 src/components/ui/StaffContextNav.test.jsx         |   4 +
 src/config/competitorModuleCoverage.js             |   4 +-
 src/config/competitorModuleCoverage.test.js        |   4 +-
 src/layout/navConfig.js                            |   6 +
 src/pages/StaffPayrollBasisPage.jsx                |   8 +-
 src/pages/StaffPayrollLaborCostRatioPage.jsx       | 118 ++++----
 src/pages/StaffPayrollLaborCostRatioPage.test.jsx  |  22 +-
 src/pages/StaffPayrollLedgerPage.jsx               |  14 +-
 src/pages/StaffPayrollLedgerPage.test.jsx          |  14 +-
 src/pages/StaffPayrollReportsPage.jsx              |  14 +-
 src/pages/StaffPayrollReportsPage.test.jsx         |  14 +-
 src/pages/StaffPayrollRetirementAccrualPage.jsx    | 328 +++++++++++++++++++++
 .../StaffPayrollRetirementAccrualPage.test.jsx     | 199 +++++++++++++
 src/styles/components.css                          |  38 +++
 src/utils/staffPayrollLedger.js                    | 131 +++++++-
 src/utils/staffPayrollLedger.test.js               |  40 ++-
 20 files changed, 941 insertions(+), 86 deletions(-)
```
