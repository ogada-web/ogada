<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-07-16T15:54:28Z -->
# develop→test diff package — frontend TSR1719

- **stream**: frontend
- **develop HEAD**: `61f8f19` (WT **CLEAN**)
- **test HEAD (local)**: `61f8f19` (WT **CLEAN**)
- **origin/test**: `61f8f19` (**PUSHED** `975aecb`→`61f8f19`)
- **origin/develop**: `61f8f19`
- **merge**: **FF EXECUTED** `975aecb`→`61f8f19` (pending **1→0**) · **origin/test PUSH EXECUTED**
- **diff range**: 1 commit
  1. `61f8f19` fix(v1.2.1/QA-B95): decode ZeroWidthNonJoiner/Joiner HTML entities (+2 @Test · BE `@ba5b0cb` lockstep)
- **files**: 6 files (+44/−4) — `notificationChannelStatus.js` · `liveBackendProbe.js` · `liveConfig.js` · `liveGlobalSetup.js` + tests
- **related**: **195/195 PASS** (2.52s, 2 files · +2 vs 193)
- **post-merge npm**: **2639/2639 PASS** (869.08s, 477 · +2 vs 2637 · SHA `@61f8f19`)
- **build**: **1230** modules PASS (9.39s · frontend-test)
- **audit**: **0** high
- **live E2E**: **0 PASS / 149 SKIP / 0 FAIL** (33.61s · bootstrap-disabled · fail-closed)
- **Open**: **0**
- **Fixed this cycle**: QA-20260716-B522 (FF merge+PUSH `@61f8f19`)
- **Planned**: QA-B116 (origin/test **702 BE**) + QA-B95
- **verdict**: **PASS**(FE) · cross-stream **SYNCED**(BE `@ba5b0cb` · FE ALL SYNCED+PUSHED `@61f8f19`)
- **operation**: **BLOCK** (702 BE origin/test unpushed · FE ALL SYNCED)
- **backend@8080**: UP/200
