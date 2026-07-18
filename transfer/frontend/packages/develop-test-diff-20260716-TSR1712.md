<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-07-16T13:52:52Z -->
# develop→test diff package — frontend TSR1712

- **stream**: frontend
- **develop HEAD**: `039cd88` (WT **CLEAN**)
- **test HEAD**: `039cd88` (WT **CLEAN**)
- **origin/test**: `039cd88` (**PUSHED/SYNCED**)
- **merge**: **FF EXECUTED** `5b69e7a`→`039cd88` (pending **3→0** · **QA-B514 Fixed**)
- **diff range**: 3 commits
  1. `d171df6` ux(a11y): wrap HomeNewsletterLaunchPage raw tables in `.ds-table-wrap` (UXD-183)
  2. `a3703a5` fix(v1.2.1/QA-B95): decode ThickSpace and MathML invisible HTML entities (+2 @Test)
  3. `039cd88` fix(v1.2.1/QA-B95): decode bidi marks and MathML Positive*Space entities (+2 @Test)
- **related**: **190/190 PASS** (2.50s, 2 · `src/frontend-test` · notificationChannelStatus + liveE2eHarness)
- **post-merge npm**: **2634/2634 PASS** (868.11s, 477 · +4 vs 2630 · same SHA)
- **build**: **1230** modules (10.74s · frontend-test)
- **audit**: **0** high
- **live E2E**: **0 PASS / 149 SKIP / 0 FAIL** (34.53s · bootstrap-disabled)
- **Open**: **1** (QA-B512 BE pending 2)
- **Planned**: QA-B116 (origin/test **699 BE**) + QA-B95
- **verdict**: **PASS**(FE)
- **cross-stream**: BLOCK (BE `@0a8a635` pending 2 vs `@fde0606` · FE `@039cd88` ALL PUSHED)
- **operation**: **BLOCK** (699 BE unpushed · Planned QA-B116)
- **backend@8080**: UP/200
