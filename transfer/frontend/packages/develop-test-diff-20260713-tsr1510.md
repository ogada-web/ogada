<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-07-13T22:53:19+00:00 -->
# frontend develop→test diff — TSR 1510차

- **when**: 2026-07-13T22:53:19+00:00
- **range**: `175c570`..`654b2c6` (**1** commit · pending)
- **develop head**: `654b2c6`
- **test head**: `175c570`
- **summary**: frontend `develop`가 `test`보다 1커밋 앞서 있어 transfer verdict는 BLOCK

## Pending Commit

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

- `npm test`: **2376/2376 PASS** (805.93s, 454 files)
- `npm run build`: **1206 modules PASS** (8.84s)
- `npm audit --omit=dev --audit-level=high`: **0 vulnerabilities**
- `live E2E`: SKIP (merge 없음, carry 120 PASS / 29 SKIP / 0 FAIL)

