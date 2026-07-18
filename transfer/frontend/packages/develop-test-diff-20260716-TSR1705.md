<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-07-16T11:48:00Z -->
# develop→test diff package — frontend TSR1705

- **stream**: frontend
- **develop HEAD**: `f73413d` (WT **CLEAN**)
- **test HEAD**: `f73413d` (WT **CLEAN**)
- **origin/test**: `f73413d` (**PUSHED/SYNCED**)
- **merge**: **FF EXECUTED**(TSR1704) `cf8a248`→`f73413d` (pending **1→0** · **QA-B508 Fixed**)
- **diff range**: 1 commit — `f73413d` fix(v1.2.1/QA-B95): decode NoBreak, word-joiner and named space HTML entities (6 files · +101/−1)
- **related**: **184/184 PASS** (3.39s, 2 · notificationChannelStatus + liveE2eHarness · TSR1705 reconfirm)
- **post-merge npm**: **2628/2628 PASS** (869.69s, 477 · +4 vs TSR1699 2624)
- **build**: **1230** modules (10.69s · TSR1705)
- **audit**: **0** high
- **live E2E**: **0 PASS / 149 SKIP / 0 FAIL** (TSR1704 34.30s · bootstrap-disabled)
- **Open**: **1** (QA-B509 BE pending `@7883a90`)
- **Planned**: QA-B116 (origin/test **696 BE**) + QA-B95
- **verdict**: **PASS**(FE)
- **cross-stream**: FE SYNCED · BE pending **1** (`7883a90` vs `5b59e83`)
- **operation**: **BLOCK** (696 BE unpushed + QA-B509)
- **backend@8080**: UP/200
