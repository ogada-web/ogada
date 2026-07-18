# develop→test diff · TSR1658 · pending transfer (no merge)

- range: `a356083..79763a3` (pending 1 commit)
- commits:
  - `79763a3` feat(v1.2.1/J03): wire dedicated dispatch-reference-unit-rates catalog
- files (pending transfer):
  - `src/api/services.js`
  - `src/api/settingsServices.test.js`
  - `src/components/ui/NotificationChannelReadinessPanel.jsx`
  - `src/components/ui/NotificationChannelReadinessPanel.test.jsx`
  - `src/config/competitorModuleCoverage.js`
  - `src/config/notificationDispatchUnitRates.js`
- diffstat: `6 files changed, 100 insertions(+), 10 deletions(-)`
- merge: **SKIP** (source edit 금지 정책 준수 · pending 유지)
- baseline verification on test `@a356083`: `npm test` **2595/2595 PASS** (872.30s, 477 files)
- build/audit: `npm run build` **1230 modules PASS** (11.91s) · `npm audit --omit=dev` **0 vulnerabilities**
- live: **SKIP** (no merge · carry default **0/149/0** from TSR1655)
- Open: **2** (QA-B476 BE carry + QA-B478 FE new)
- cross-stream: BLOCK (BE pending 2 + FE pending 1)
- operation: BLOCK (origin/test **676 BE** + QA-B116 + QA-B95 + QA-B478)
