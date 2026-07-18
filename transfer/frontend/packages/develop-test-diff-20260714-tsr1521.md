# frontend develop→test diff — TSR 1521

- date: 2026-07-14T03:21:00Z
- develop/test/origin/test: `e18ee5c`
- merge: FF `bc9389d`→`e18ee5c` (pending **1→0**)
- commits:
  - `e18ee5c` feat(v1.2.1/M11): wire staff payroll ledger preview
- files: 13 (+839/-1)
- related: payroll **22/22 PASS** (5 files · 8.81s)
- post-merge: **2391/2391 PASS** (799.99s, 457 files)
- build: **1209 PASS** (10.52s)
- audit: **0**
- live E2E: **116 PASS / 33 SKIP / 0 FAIL** (42.51s · bootstrap-disabled)
- origin/test: **PUSHED** (`bc9389d`→`e18ee5c`)

## stat
e18ee5c feat(v1.2.1/M11): wire staff payroll ledger preview
 src/App.jsx                                        |  12 +
 src/api/services.js                                |  11 +
 src/api/staffPayrollServices.test.js               |  54 ++++
 .../staff/StaffPayrollRelatedSurfacesPanel.jsx     |  32 ++
 src/components/ui/StaffContextNav.jsx              |   1 +
 src/components/ui/StaffContextNav.test.jsx         |   4 +
 src/config/competitorModuleCoverage.js             |   3 +-
 src/config/competitorModuleCoverage.test.js        |   6 +
 src/layout/navConfig.js                            |   6 +
 src/pages/StaffPayrollLedgerPage.jsx               | 343 +++++++++++++++++++++
 src/pages/StaffPayrollLedgerPage.test.jsx          | 134 ++++++++
 src/utils/staffPayrollLedger.js                    | 164 ++++++++++
 src/utils/staffPayrollLedger.test.js               |  70 +++++
 13 files changed, 839 insertions(+), 1 deletion(-)
