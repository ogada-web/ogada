<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-07-13T22:19:55+00:00 -->
# frontend develop→test — TSR 1508차 (UXD-172)

- **when**: 2026-07-13T22:19:55+00:00
- **range**: `bd12f28`..`175c570` (**1** commit · FF)
- **commit**: `175c570 ux(a11y/US-Q01): fix invalid shuttle sheet table semantics (UXD-172)`
- **files**: `TransportShuttleSheetView.jsx` · `TransportShuttleScheduleView.jsx` (role=table→list/listitem · aria-label)
- **related**: shuttle unit **20/20 PASS**
- **post-merge**: `npm test` **2372/2372 PASS**(804.64s · 453 files)
- **build**: **1206 modules PASS**(8.85s) · audit **0 high**
- **live E2E**: **120 PASS / 29 SKIP / 0 FAIL**(40.82s · bootstrap-disabled)
- **origin/test**: PUSHED `bd12f28`→`175c570` · unpushed **0**
- **QA**: QA-B369 Fixed · residual Open **QA-B344**(BE pending **30**)
- **verdict**: FE transfer local+remote **PASS** · overall **BLOCK**(BE QA-B344)
