<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-07-13T23:27:10+00:00 -->
# frontend develop→test diff — TSR 1512차

- **when**: 2026-07-13T23:27:10+00:00
- **range**: `175c570`..`654b2c6` (**1** commit · **MERGED+PUSHED**)
- **develop head**: `654b2c6`
- **test head**: `654b2c6` (SYNCED)
- **summary**: G16 vehicle shuttle address normalize FF merge 완료 · develop/test/origin/test ALL SYNCED

## Merged Commit

- `654b2c6 fix(v1.2.1/G16): normalize vehicle shuttle addresses to match BE`

## Diffstat

```text
src/config/vehicles.js          | 26 ++++++++++++++++++++++++
src/config/vehicles.test.js     | 27 +++++++++++++++++++++++++
src/pages/VehiclesPage.jsx      | 11 +++++++----
src/pages/VehiclesPage.test.jsx | 44 +++++++++++++++++++++++++++++++++++++++++
4 files changed, 104 insertions(+), 4 deletions(-)
```

## Validation Snapshot

- related vitest: **8/8 PASS**
- `npm test` post-merge: **2376/2376 PASS** (808.96s, 454 files)
- `npm run build`: **1206 modules PASS** (9.94s)
- `npm audit --omit=dev --audit-level=high`: **0 vulnerabilities**
- `live E2E`: **120 PASS / 29 SKIP / 0 FAIL** (40.53s)
- `origin/test` push: **PASS** (`175c570`→`654b2c6`)
