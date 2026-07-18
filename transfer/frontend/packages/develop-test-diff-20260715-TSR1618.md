# develop→test diff · TSR1618 · QA-B451 + UXD-179

- range: `353eb7f..68cd253` (FF · 3 commits · origin/test push)
- commits:
  - `8b8095a` — `ux(a11y): add G-LINKAGE org-wide report route and draft labels (UXD-179)`
  - `a2db731` — `fix(v1.2.1/UXD-179): apply linkage report filters only on submit`
  - `68cd253` — `fix(v1.2.1/QA-B451): restore soft max-length validation path` (ClientLinkageRecordForm `-maxLength`)
- files: 14 (+504/−48 across range) · QA-B451 delta = `ClientLinkageRecordForm.jsx` 1 deletion
- related: **13/13 PASS** (10.45s · Form+ReportPage+ReportPanel)
- npm: **2550/2550 PASS** (869.20s · 472 files · +1 vs 2549 FAIL @a2db731)
- build: **1223** modules (10.84s) · audit **0 high**
- live: default **0 PASS/149 SKIP/0 FAIL** (33.94s · bootstrap-disabled fail-closed) · opt-in **SKIP**(carry TSR1597 **116/33/0**)
- Open: **0** · Fixed **QA-B451**
- cross-stream: SYNCED (BE `@34d4968` · FE `@68cd253` ALL SYNCED+PUSHED)
- operation: BLOCK (origin/test **661 BE** · QA-B116 + QA-B95)
