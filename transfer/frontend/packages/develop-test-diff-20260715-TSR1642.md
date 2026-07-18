# develop→test diff · TSR1642 · FF merge+PUSH (G-LINKAGE report pagination)

- range: `c779ca1..fd6b996` (FF · 1 commit)
- commit: `fd6b996` feat(v1.2.1/G-LINKAGE): add report pagination controls
- files:
  - `src/pages/ClientLinkageRecordsReportPage.jsx` (+pagination / page-reset on filter)
  - `src/pages/ClientLinkageRecordsReportPage.test.jsx` (+1 pagination regression)
- merge: **EXECUTED** FF `c779ca1`→`fd6b996`
- related pre-merge: **4/4 PASS** (4.88s · 1 file · ClientLinkageRecordsReportPage)
- post-merge npm: **2571/2571 PASS** (862.00s, 472 files · +1 vs TSR1639 2570)
- build: **1225** modules (9.22s) · audit **0 high**
- live: default **0/149/0** (33.20s · bootstrap-disabled fail-closed)
- origin/test: **PUSHED** `c779ca1`→`fd6b996`
- Open: **0** (QA-B469 Fixed)
- cross-stream: SYNCED (BE `@baa1792` · FE `@fd6b996` ALL SYNCED+PUSHED)
- operation: BLOCK (origin/test **670 BE** · QA-B116 + QA-B95)
