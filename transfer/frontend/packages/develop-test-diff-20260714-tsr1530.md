# develop→test diff — TSR 1530 (2026-07-14)

- stream: frontend
- merge: FF `10bf059` → `aa86734` (pending 1→0)
- commit: `aa86734 feat(v1.2.1/M11): wire labor-cost-ratio compliance preview page`
- pre-merge related: 30/30 PASS (9.35s, 5 files)
- post-merge: 2410/2410 PASS (824.99s, 460 files)
- build: 1212 modules PASS (9.32s)
- audit: 0 high
- live E2E: 116 PASS / 33 SKIP / 0 FAIL (39.42s)
- origin/test: PUSHED (`10bf059`→`aa86734`)
- QA: QA-B381 Fixed · Open 0 · cross-stream SYNCED (BE `@bd06646` · FE `@aa86734`)
- operation: BLOCK (QA-B116 origin/test 623 BE + QA-B95)

## Commits

```
aa86734 feat(v1.2.1/M11): wire labor-cost-ratio compliance preview page
```

## Diffstat

```
 src/App.jsx                                       |  12 +
 src/api/services.js                               |  11 +
 src/api/staffPayrollServices.test.js              |  39 +++
 src/components/ui/StaffContextNav.jsx             |   1 +
 src/components/ui/StaffContextNav.test.jsx        |   4 +
 src/config/competitorModuleCoverage.js            |   4 +-
 src/config/competitorModuleCoverage.test.js       |   4 +-
 src/layout/navConfig.js                           |   6 +
 src/pages/StaffPayrollLaborCostRatioPage.jsx      | 286 ++++++++++++++++++++++
 src/pages/StaffPayrollLaborCostRatioPage.test.jsx | 174 +++++++++++++
 src/utils/staffPayrollLedger.js                   | 101 +++++++-
 src/utils/staffPayrollLedger.test.js              |  40 +++
 12 files changed, 677 insertions(+), 5 deletions(-)
```
