<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-07-16T03:42:47Z -->
# develop→test diff package — frontend TSR 1675

- **verdict**: **BLOCK** (dirty-tree §1-1 — PASS 금지)
- **committed SHA**: develop = test = origin/test = `483dfe1` (SYNCED · pending **0**)
- **merge**: **SKIP** (no new commits; develop WT DIRTY)
- **npm**: CARRY **2603/2603** (TSR1673 · same SHA)
- **live E2E**: SKIP (no merge)
- **Open**: QA-20260716-B490 (FE) + QA-20260716-B489 (BE)

## Uncommitted develop WIP (QA-B490 — must commit)

```
 M src/utils/accountingBpo.js           (+22/-10 · SSO demote when blockers)
 M src/utils/accountingBpo.test.js      (+21 · demote + canLaunch regressions)
 M src/pages/AccountingBpoPage.test.jsx (+36 · hide SSO launch when blockers)
```

Stat: **3 files, +69/−10**. Intent: M12 accounting BPO — if `ssoReadinessBlockers` non-empty, force `ssoAvailability=PLANNED` and refuse SSO launch even when API reports AVAILABLE.

## COD next action

1. Commit the 3 dirty files on `src/frontend` `develop` (WT CLEAN).
2. TSR: FF merge → `test` + related (`accountingBpo*`) + full `npm test` + origin/test push.
3. Parallel: BE QA-B489 dirty 2M also needs commit (cross-stream BLOCK).
