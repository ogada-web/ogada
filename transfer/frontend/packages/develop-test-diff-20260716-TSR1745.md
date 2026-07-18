<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-07-16T23:54:00Z -->
# develop→test diff package — frontend TSR1745

- **stream**: frontend
- **develop HEAD**: `6fceb8d` (WT **CLEAN**)
- **test HEAD (local)**: `6fceb8d` (WT **CLEAN**)
- **origin/test**: `6fceb8d` (**PUSHED**)
- **origin/develop**: `6fceb8d`
- **merge**: FF `7ee1cf1`→`6fceb8d` + **PUSH** · pending **1→0**
- **diff range absorbed**: `7ee1cf1..6fceb8d` (1 commit)
- **pending commits (absorbed)**:
  - `6fceb8d` — fix(v1.2.1/QA-B95): decode square-bracket wrapping HTML entities (COD B542 · QA-20260716-B542)
- **files**: 6 files (+55/−0) — `notificationChannelStatus.js/test.js` · `liveBackendProbe.js` · `liveConfig.js` · `liveGlobalSetup.js` · `liveE2eHarness.test.js`
- **related (post-merge @test)**: **213/213 PASS** (2.72s · 6-file · bracket-wrap +2) · core QA-B95 **213/213**
- **develop pre-merge related**: **213/213 PASS** (notificationChannelStatus + liveE2eHarness)
- **npm test (post-merge)**: **2657/2657 PASS** (877.13s, 477 files · +2 vs TSR1743 2655)
- **build**: **1230** (9.29s · elapsed 10.13s)
- **audit**: **0** high
- **live E2E**: **0 PASS / 149 SKIP / 0 FAIL** (34.81s · bootstrap-disabled · fail-closed · LIVE_EXIT=0)
- **Open**: **0**
- **Planned**: QA-B116 (origin/test **713 BE**) + QA-B95
- **verdict**: **PASS**(FE) · cross-stream **SYNCED(BE `@b348258` · FE `@6fceb8d`)**
- **operation**: **BLOCK** (713 BE origin/test unpushed)
- **backend@8080**: UP/200
- **next**: QA-B116 BE origin/test push · QA-B95 operation gate · PLN baseline FE `@6fceb8d`
