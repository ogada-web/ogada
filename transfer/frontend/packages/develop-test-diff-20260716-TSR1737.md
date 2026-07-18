<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-07-16T21:34:46Z -->
# develop→test diff package — frontend TSR1737

- **stream**: frontend
- **develop HEAD**: `b28eb45` (WT **CLEAN**)
- **test HEAD (local)**: `b28eb45` (WT **CLEAN**)
- **origin/test**: `b28eb45` (**PUSHED**)
- **origin/develop**: `b28eb45`
- **merge**: FF `ab9e853`→`b28eb45` + **PUSH** · pending **2→0**
- **diff range absorbed**: `ab9e853..b28eb45` (2 commits)
- **pending commits (absorbed)**:
  - `d3b0f1c` — ux(a11y): promote template-catalog message column to row header (UXD-185)
  - `b28eb45` — fix(v1.2.1/QA-B95): decode VeryThickSpace HTML entity alias (COD B535 · BE `@043f002` lockstep)
- **files**: 8 files (+42/−15) — `NotificationChannelReadinessPanel.jsx/.test.jsx` · `notificationChannelStatus.js/.test.js` · `liveBackendProbe.js` · `liveConfig.js` · `liveGlobalSetup.js` · `liveE2eHarness.test.js`
- **related (post-merge @test)**: **226/226 PASS** (5.43s · 4-file gate) · core QA-B95 **205/205** (2.65s)
- **develop pre-merge related**: **205/205 PASS** (COD · same SHA)
- **npm test (post-merge)**: **2649/2649 PASS** (873.45s, 477 files · Δ0 vs TSR1735 2649)
- **build**: **1230** (10.60s · frontend-test)
- **audit**: **0** high
- **live E2E**: **0 PASS / 149 SKIP / 0 FAIL** (34.57s · bootstrap-disabled · fail-closed · LIVE_EXIT=0)
- **Open**: **0** (**QA-B535 Fixed**)
- **Planned**: QA-B116 (origin/test **710 BE**) + QA-B95
- **verdict**: **PASS**(FE) · cross-stream **LOCAL SYNCED**(BE `@043f002` · FE `@b28eb45`)
- **operation**: **BLOCK** (710 BE origin/test unpushed)
- **backend@8080**: UP/200
- **next**: QA-B116 origin/test BE push · QA-B95 operation gate · PLN baseline FE `@b28eb45` / BE `@043f002`
