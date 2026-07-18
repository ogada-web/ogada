<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-07-16T18:21:30Z -->
# develop→test diff package — frontend TSR1729

- **stream**: frontend
- **develop HEAD**: `c260baa` (WT **CLEAN**)
- **test HEAD (local)**: `8a05640` (WT **CLEAN**)
- **origin/test**: `8a05640` (**PUSHED** carry TSR1721)
- **origin/develop**: `c260baa`
- **merge**: **SKIP** (read-only directive · pending **4** committed · FF-ready)
- **diff range**: `8a05640..c260baa` (4 commits · 8 files changed, +212/-3)
- **pending commits**: `ed48077` (UXD-184 a11y), `031abef` (QA-B95 figure/punctuation/ideographic), `73aa6dd` (QA-B95 fractional em), `c260baa` (QA-B95 SixPerEm+long space · COD B528)
- **npm test (baseline @test `8a05640`)**: related **195/195 PASS** (2.50s · frontend-test) · full **CARRY 2639/2639** (TSR1721 · SHA unchanged)
- **develop pre-merge related**: **201/201 PASS** (3.43s · notificationChannelStatus + liveE2eHarness · +6 vs baseline related 195)
- **develop full suite (pre-merge)**: **2645/2645 PASS** (862.20s, 477 files · `npm-test-locked`→`src/frontend` · +2 vs TSR1726 2643)
- **build**: **1230** (9.99s · frontend-test)
- **audit**: **0** high (frontend-test)
- **live E2E**: **SKIP** (merge 0 · CARRY 0 PASS / 149 SKIP / 0 FAIL from TSR1721)
- **Open**: **2** (QA-B525 backend · QA-B526 frontend)
- **Planned**: QA-B116 (origin/test **703 BE**) + QA-B95
- **verdict**: **BLOCK** · cross-stream **BLOCK**(BE pending 3 `@08cdb87`+`@e4123c3`+`@4622896` · FE pending 4 `@ed48077`+`@031abef`+`@73aa6dd`+`@c260baa`)
- **operation**: **BLOCK** (703 BE origin/test unpushed + FE/BE merge pending)
- **backend@8080**: UP/200
- **next tester action**: FF merge `8a05640`→`c260baa` + post-merge npm ~2645/2645 + `git push origin test`
