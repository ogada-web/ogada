<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-07-16T17:09:14Z -->
# develop→test diff package — frontend TSR1724

- **stream**: frontend
- **develop HEAD**: `ed48077` (WT **DIRTY 6M** — QA-B95 figure/punctuation/ideographic space WIP uncommitted)
- **test HEAD (local)**: `8a05640` (WT **CLEAN**)
- **origin/test**: `8a05640` (**PUSHED** carry TSR1721)
- **origin/develop**: `ed48077` (UXD-184 a11y commit pushed · QA-B95 WIP **not committed**)
- **merge**: **SKIP** (read-only directive · pending **1** committed + **6 uncommitted**)
- **diff range**: `8a05640..ed48077` (1 commit) + working tree 6M WIP
- **related (baseline `@8a05640`)**: **195/195 PASS** (2.51s, 2 files · Δ0 · frontend-test)
- **related (develop pre-merge)**: **197/197 PASS** (3.25s, 2 files · +2 vs 195 · includes DIRTY 6M WIP)
- **post-merge npm**: **CARRY 2639/2639 PASS** (TSR1721 · SHA `@8a05640` unchanged)
- **build**: **1230** modules PASS (9.29s · frontend-test)
- **audit**: **0** high
- **live E2E**: **CARRY 0 PASS / 149 SKIP / 0 FAIL** (TSR1721 · merge 0 · bootstrap-disabled)
- **Open**: **2** (QA-B525 backend · QA-B526 frontend)
- **Planned**: QA-B116 (origin/test **703 BE**) + QA-B95
- **verdict**: **BLOCK** · cross-stream **BLOCK**(BE pending 1 `@08cdb87` · FE DIRTY 6M + pending 1 `@ed48077`)
- **operation**: **BLOCK** (703 BE origin/test unpushed · FE merge gate blocked by DIRTY 6M)
- **backend@8080**: UP/200
- **post-merge expected**: ~**2641/2641** npm after COD commit 6M + FF merge
