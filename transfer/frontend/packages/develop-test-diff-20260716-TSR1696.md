<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-07-16T10:12:00Z -->
# develop→test diff package — frontend TSR1696

- **stream**: frontend
- **develop HEAD**: `e45dacb` (WT **CLEAN**)
- **test / origin/test**: `e45dacb` (ALL SYNCED+PUSHED · WT CLEAN)
- **pending commits**: 0 (was **1** before merge)
- **merge**: **FF EXECUTED** `f5dded2`→`e45dacb` (QA-B95 zero-width + tab/newline named HTML entities · FE↔BE lockstep `@7102f82`)
- **changed files** (6):
  - `src/config/notificationChannelStatus.js`
  - `src/config/notificationChannelStatus.test.js`
  - `src/e2e/liveBackendProbe.js`
  - `src/e2e/liveConfig.js`
  - `src/e2e/liveGlobalSetup.js`
  - `src/test/liveE2eHarness.test.js`
- **related smoke (develop)**: **178/178 PASS** (notificationChannelStatus + liveE2eHarness · 2.49s, 2 · +4 vs 1694)
- **full npm**: **2622/2622 PASS** (+4 vs 2618 · 869.37s, 477)
- **build / audit / live E2E**: build **1230** (9.35s) · audit **0** · live **0/149/0** (36.08s)
- **Open**: 0
- **cross-stream**: **local SYNCED** — BE develop/test **SYNCED `@7102f82`** · FE **ALL SYNCED+PUSHED `@e45dacb`** · origin/test **693 BE** unpushed
- **verdict**: **PASS**(FE) · operation **BLOCK**(693 BE)

```
git -C src/frontend log --oneline test..develop
# (empty — ALL SYNCED)

git -C src/frontend rev-parse develop test origin/test
# e45dacb e45dacb e45dacb

git -C src/frontend log --oneline f5dded2..e45dacb
# e45dacb fix(v1.2.1/QA-B95): decode zero-width and tab/newline named HTML entities
```
