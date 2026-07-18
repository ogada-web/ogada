<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-07-16T14:43:48Z -->
# develop→test diff package — frontend TSR1714

- **stream**: frontend
- **develop HEAD**: `29fc34f` (WT **CLEAN**)
- **test HEAD (local)**: `29fc34f` (WT **CLEAN** · FF merged)
- **origin/test**: `039cd88` (**push pending 1**)
- **merge**: **FF EXECUTED local** `039cd88`→`29fc34f` (pending **1→0** local · **origin push SKIP** read-only cycle)
- **diff range**: 1 commit
  1. `29fc34f` fix(v1.2.1/QA-B95): decode bidi embedding/isolate and NonBreakingSpace entities (+2 @Test)
- **related (develop pre-merge)**: **192/192 PASS** (2.51s, 2 · notificationChannelStatus + liveE2eHarness · +2 vs 190)
- **post-merge npm**: **2636/2636 PASS** (868.09s, 477 · +2 vs 2634 · `src/frontend-test`)
- **build**: **1230** modules (9.58s · frontend-test)
- **audit**: **0** high
- **live E2E**: **0 PASS / 149 SKIP / 0 FAIL** (33.59s · bootstrap-disabled)
- **Open**: **2** (QA-B512 BE pending 3 · QA-B519 FE origin/test push pending 1)
- **Planned**: QA-B116 (origin/test **697 BE**) + QA-B95
- **verdict**: **BLOCK**
- **cross-stream**: BLOCK (BE `@d911983` pending 3 vs `@fde0606` · FE local `@29fc34f` vs origin `@039cd88`)
- **operation**: **BLOCK** (697 BE + 1 FE unpushed)
- **backend@8080**: UP/200
