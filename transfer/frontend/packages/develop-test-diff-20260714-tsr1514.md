<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-07-14T00:12:24+00:00 -->
# frontend develop→test diff — TSR 1514차

- **when**: 2026-07-14T00:12:24+00:00
- **range**: `654b2c6`..`a6255a0` (**1** commit · **MERGED+PUSHED**)
- **develop head**: `a6255a0`
- **test head**: `a6255a0` (SYNCED)
- **summary**: QA-B372 G16 blank shuttle address PATCH `""` fallback FF merge 완료 · develop/test/origin/test ALL SYNCED

## Merged Commit

- `a6255a0 fix(v1.2.1/QA-B372): send blank shuttle addresses as empty string on PATCH`

## Diffstat

```text
 src/config/vehicles.js          | 10 ++++++----
 src/config/vehicles.test.js     |  7 ++++---
 src/pages/VehiclesPage.jsx      |  2 +-
 src/pages/VehiclesPage.test.jsx | 36 ++++++++++++++++++++++++++++++++++++
 4 files changed, 47 insertions(+), 8 deletions(-)
```

## Validation Snapshot

- related vitest: **9/9 PASS**
- `npm test` post-merge: **2377/2377 PASS** (808.65s, 454 files)
- `npm run build`: **1206 modules PASS** (8.88s)
- `npm audit --omit=dev --audit-level=high`: **0 vulnerabilities**
- `live E2E`: **120 PASS / 29 SKIP / 0 FAIL** (38.00s)
- `origin/test` push: **PASS** (`654b2c6`→`a6255a0`)
