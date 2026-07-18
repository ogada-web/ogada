<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-07-16T15:21:25Z -->
# develop→test diff package — frontend TSR1717

- **stream**: frontend
- **develop HEAD**: `975aecb` (WT **CLEAN**)
- **test HEAD (local)**: `975aecb` (WT **CLEAN**)
- **origin/test**: `975aecb` (**PUSHED** `29fc34f`→`975aecb`)
- **origin/develop**: `975aecb`
- **merge**: **FF EXECUTED** `29fc34f`→`975aecb` (pending **1→0**) · **origin/test PUSH EXECUTED**
- **diff range**: 1 commit
  1. `975aecb` fix(v1.2.1/QA-B95): decode bidi long-alias HTML entities (+1 @Test · BE `@53efa0b` lockstep)
- **files**: `notificationChannelStatus.js` + `notificationChannelStatus.test.js` (+42/−1)
- **related**: **193/193 PASS** (2.52s, 2 files · +1 vs 192)
- **post-merge npm**: **2637/2637 PASS** (868.94s, 477 · +1 vs 2636 · SHA `@975aecb`)
- **build**: **1230** modules PASS (9.64s · frontend-test)
- **audit**: **0** high
- **live E2E**: **0 PASS / 149 SKIP / 0 FAIL** (34.81s · bootstrap-disabled · fail-closed)
- **Open**: **0**
- **Fixed this cycle**: QA-20260716-B520 (FF merge+PUSH `@975aecb`)
- **Planned**: QA-B116 (origin/test **701 BE**) + QA-B95
- **verdict**: **PASS**(FE) · cross-stream **SYNCED**(BE `@53efa0b` · FE `@975aecb`)
- **operation**: **BLOCK** (701 BE origin/test unpushed · FE ALL SYNCED)
- **backend@8080**: UP/200
