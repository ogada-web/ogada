<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-07-15T10:55:25Z -->
# develop→test diff · TSR1615 · UXD-179 / QA-B451

- range: `353eb7f..a2db731` (FF · 2 commits · local `src/frontend-test` only)
- commits:
  - `8b8095a` — `ux(a11y): add G-LINKAGE org-wide report route and draft labels (UXD-179)`
  - `a2db731` — `fix(v1.2.1/UXD-179): apply linkage report filters only on submit`
- files (14): `App.jsx` · `services.js` · `ClientLinkageRecordsPanel*` · `ClientLinkageRecordForm.jsx`(+`maxLength`) · `ClientLinkageRecordsReportPanel*` · `ClientsContextNav*` · `navConfig.js` · `ClientLinkageRecordsReportPage*` · `clientLinkageRecordsServices.test.js` · `components.css`
- related: **24/24 PASS** (13.43s · 6 files)
- npm: **2549/2550 FAIL** (857.89s · 472 files) — **QA-B451**
- fail: `ClientLinkageRecordForm.test.jsx` › `blocks institution names over BE max length`
  - cause: `maxLength={200}` caps input → JS length-error message never renders
- build: **1223** modules (10.69s) · audit **0 high**
- live: **SKIP** (unit FAIL)
- Open: **1 BLOCK (QA-B451)**
- origin/test: **NOT PUSHED** (remains `@353eb7f`)
- cross-stream: BLOCK (BE `@9dff00f` · FE unit fail)
- operation: BLOCK (origin/test **660 BE** · QA-B116 + QA-B95)
- **PASS 금지** until QA-B451 Fixed + full suite green + origin/test push
