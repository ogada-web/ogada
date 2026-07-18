<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-07-16T14:47:11Z -->
# develop→test diff package — frontend TSR1715

- **stream**: frontend
- **develop HEAD**: `29fc34f` (WT **CLEAN**)
- **test HEAD (local)**: `29fc34f` (WT **CLEAN**)
- **origin/test**: `29fc34f` (**PUSHED** `039cd88`→`29fc34f`)
- **merge**: **CARRY** TSR1714 FF local (pending **0**) · **origin/test PUSH EXECUTED** this cycle
- **diff range**: 1 commit (already merged TSR1714)
  1. `29fc34f` fix(v1.2.1/QA-B95): decode bidi embedding/isolate and NonBreakingSpace entities (+2 @Test)
- **related**: **CARRY 192/192 PASS** (TSR1714 · 2.51s · SHA unchanged)
- **post-merge npm**: **CARRY 2636/2636 PASS** (TSR1714 · 868.09s, 477 · SHA unchanged `@29fc34f`)
- **build**: **CARRY 1230** modules (TSR1714 · 9.58s)
- **audit**: **CARRY 0** high
- **live E2E**: **CARRY 0 PASS / 149 SKIP / 0 FAIL** (TSR1714 · bootstrap-disabled · merge 0 this cycle)
- **Open**: **1** (QA-B512 BE pending 3 · FE Open **0**)
- **Fixed this cycle**: QA-20260716-B519 (origin/test push `@29fc34f`)
- **Planned**: QA-B116 (origin/test **700 BE**) + QA-B95
- **verdict**: **PASS**(FE) · cross-stream **BLOCK**(BE)
- **cross-stream**: BLOCK (BE `@d911983` pending **3** vs test `@fde0606` · FE **ALL SYNCED `@29fc34f`**)
- **operation**: **BLOCK** (700 BE origin/test unpushed · FE synced)
- **backend@8080**: UP/200
