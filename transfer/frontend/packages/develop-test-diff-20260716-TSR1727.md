<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-07-16T17:48:10Z -->
# develop→test diff package — frontend TSR1727

- **stream**: frontend
- **develop HEAD**: `73aa6dd` (WT **CLEAN**)
- **test HEAD (local)**: `8a05640` (WT **CLEAN**)
- **origin/test**: `8a05640` (**PUSHED** carry TSR1721)
- **origin/develop**: `73aa6dd`
- **merge**: **SKIP** (read-only directive · pending **3** committed · FF-ready)
- **diff range**: `8a05640..73aa6dd` (3 commits · 8 files changed, +131/-3)
- **pending commits**: `ed48077` (UXD-184 a11y), `031abef` (QA-B95 figure/punctuation/ideographic), `73aa6dd` (QA-B95 fractional em)
- **npm test (baseline @test `8a05640`)**: **CARRY 2643/2643 PASS** (TSR1726 · 869.55s, 477 · SHA unchanged)
- **develop pre-merge related**: **199/199 PASS** (2.90s · notificationChannelStatus + liveE2eHarness · +4 vs baseline related 195 · +2 vs TSR1724 197)
- **build**: **CARRY 1230** (TSR1726 · 9.17s · frontend-test)
- **audit**: **CARRY 0** high (TSR1726)
- **live E2E**: **SKIP** (merge 0 · CARRY 0 PASS / 149 SKIP / 0 FAIL from TSR1721)
- **Open**: **2** (QA-B525 backend · QA-B526 frontend)
- **Planned**: QA-B116 (origin/test **703 BE**) + QA-B95
- **verdict**: **BLOCK** · cross-stream **BLOCK**(BE pending 2 `@08cdb87`+`@e4123c3` · FE pending 3 `@ed48077`+`@031abef`+`@73aa6dd`)
- **operation**: **BLOCK** (703 BE origin/test unpushed + FE/BE merge pending)
- **backend@8080**: UP/200
- **next tester action**: FF merge `8a05640`→`73aa6dd` + post-merge npm ~2643/2643 + `git push origin test`
