<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-07-16T16:33:40Z -->
# develop→test diff package — frontend TSR1721

- **stream**: frontend
- **develop HEAD**: `8a05640` (WT **CLEAN**)
- **test HEAD (local)**: `8a05640` (WT **CLEAN**)
- **origin/test**: `8a05640` (**PUSHED** `61f8f19`→`8a05640`)
- **origin/develop**: `8a05640`
- **merge**: **FF EXECUTED** `61f8f19`→`8a05640` (pending **1→0**) · **origin/test PUSH EXECUTED**
- **diff range**: 1 commit
  1. `8a05640` fix(v1.2.1/QA-B95): decode NoBreakSpace HTML entity in FE readiness paths (in-place test expand · BE `@ff80f0b` lockstep)
- **files**: 6 files (+11/−6) — `notificationChannelStatus.js` · `liveBackendProbe.js` · `liveConfig.js` · `liveGlobalSetup.js` + tests
- **related**: **195/195 PASS** (2.45s, 2 files · Δ0 vs 195 · in-place expand)
- **post-merge npm**: **2639/2639 PASS** (866.73s, 477 · Δ0 vs 2639 · SHA `@8a05640`)
- **build**: **1230** modules PASS (10.99s · frontend-test)
- **audit**: **0** high
- **live E2E**: **0 PASS / 149 SKIP / 0 FAIL** (33.48s · bootstrap-disabled · fail-closed)
- **Open**: **0**
- **Fixed this cycle**: QA-20260716-B524 (FF merge+PUSH `@8a05640`)
- **Planned**: QA-B116 (origin/test **703 BE**) + QA-B95
- **verdict**: **PASS**(FE) · cross-stream **SYNCED**(BE `@ff80f0b` · FE ALL SYNCED+PUSHED `@8a05640`)
- **operation**: **BLOCK** (703 BE origin/test unpushed · FE ALL SYNCED)
- **backend@8080**: UP/200
