<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-07-13T21:29:00+00:00 -->
# frontend develop→test merge — TSR 1505차

- **when**: 2026-07-13T21:29:00+00:00
- **range**: `afbbaa7`..`bd12f28` (**23** commits · FF merge EXECUTED)
- **result**: develop/test **SYNCED `@bd12f28`**
- **post-merge npm test**: **2372/2372 PASS** (802.04s, 453 files)
- **build**: 1206 modules PASS (8.76s)
- **audit**: 0 high
- **live E2E**: 120 PASS / 29 SKIP / 0 FAIL (37.88s · bootstrap-disabled)
- **QA**: QA-B352 **Fixed** · QA-B368 Fixed carry · residual Open QA-B344 (BE pending 29)
- **HEAD commits (top)**:
  - `bd12f28` fix(v1.2.1/QA-B368): block day-status excluded clients on manual draft runs
  - `d285899` fix(v1.2.1/QA-B366): surface all-excluded day-status suggest guidance
  - `e48db91` fix(v1.2.1/QA-B95): gate transport and safety live suites on schema blockers
  - `c012ed0` test(v1.2.1/QA-B361): stabilize month-boundary fixtures across five suites
  - `d873894` feat(v1.2.1/QA-B360): add transport shuttle sheet workflow and stabilize labels
  - … (+18 older US-Q01/G16/live-e2e commits)

- **verdict**: FE transfer local merge **PASS** · overall transfer **BLOCK**(BE QA-B344)
