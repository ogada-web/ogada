<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-07-16T11:47:00Z -->
# develop→test diff package — frontend TSR1704

- **stream**: frontend
- **develop HEAD**: `f73413d` (WT **CLEAN**)
- **test HEAD**: `f73413d` (WT **CLEAN**)
- **origin/test**: `f73413d` (**PUSHED/SYNCED**)
- **merge**: **FF EXECUTED** `cf8a248`→`f73413d` (pending **1→0** · **QA-B508 Fixed** QA-B95 NoBreak+Wj+named-space HTML entities · FE↔BE lockstep `@7883a90`)
- **diff range**: 1 commit — `f73413d` fix(v1.2.1/QA-B95): decode NoBreak, word-joiner and named space HTML entities (+4 @Test · 6 files)
- **related**: **184/184 PASS** (2.47s, 2 · notificationChannelStatus + liveE2eHarness · +4 vs 180)
- **post-merge npm**: **2628/2628 PASS** (869.69s, 477 · +4 vs 2624)
- **build**: **1230** modules (9.39s)
- **audit**: **0** high
- **live E2E**: **0 PASS / 149 SKIP / 0 FAIL** (34.30s · bootstrap-disabled)
- **Open**: **1** (QA-B509 BE pending `@7883a90`)
- **Planned**: QA-B116 (origin/test **696 BE**) + QA-B95
- **verdict**: **PASS**(FE)
- **cross-stream**: BLOCK (BE `@7883a90` pending 1 · FE `@f73413d` ALL PUSHED)
- **operation**: **BLOCK** (696 BE unpushed + QA-B509)
- **backend@8080**: UP/200
