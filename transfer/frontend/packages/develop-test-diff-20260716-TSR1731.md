<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-07-16T19:07:52Z -->
# develop→test diff package — frontend TSR1731

- **stream**: frontend
- **develop HEAD**: `73169a1` (WT **CLEAN**)
- **test HEAD (local)**: `73169a1` (WT **CLEAN**)
- **origin/test**: `73169a1` (**PUSHED**)
- **origin/develop**: `73169a1`
- **merge**: **EXECUTED** FF `8a05640`→`c260baa`(18:17)→`73169a1`(18:50) + **PUSH** · pending **5→0**
- **diff range absorbed**: `8a05640..73169a1` (5 commits)
- **pending commits (absorbed)**: `ed48077` (UXD-184 a11y) · `031abef` (figure/punctuation/ideographic) · `73aa6dd` (fractional em) · `c260baa` (SixPerEm+long space · COD B528) · `73169a1` (MathSpace+WordJoiner · COD B530)
- **related (post-merge @test)**: **203/203 PASS** (2.54s · notificationChannelStatus + liveE2eHarness · +8 vs baseline 195 @`8a05640`)
- **npm test (post-merge)**: **2647/2647 PASS** (867.58s, 477 files · +8 vs TSR1721 2639 · +2 vs develop pre-merge 2645 @`c260baa`)
- **build**: **1230** (10.94s · frontend-test)
- **audit**: **0** high
- **live E2E**: **0 PASS / 149 SKIP / 0 FAIL** (32.92s · bootstrap-disabled · fail-closed · LIVE_EXIT=0)
- **Open**: **1** (QA-B525 backend only · **QA-B526 Fixed**)
- **Planned**: QA-B116 (origin/test **707 BE**) + QA-B95
- **verdict**: **PASS**(FE) · cross-stream **BLOCK**(BE pending 4 `@6014cca` vs `@ff80f0b`)
- **operation**: **BLOCK** (707 BE origin/test unpushed + BE merge gate B525)
- **backend@8080**: UP/200
- **next**: backend stream FF merge `@6014cca` (QA-B525) · PLN baseline FE `@73169a1`
