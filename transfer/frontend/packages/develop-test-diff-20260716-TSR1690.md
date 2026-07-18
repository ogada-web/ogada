<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-07-16T08:22:42Z -->
# develop→test diff package — frontend TSR1690

- **stream**: frontend
- **develop HEAD**: `f9e1e91` (WT **CLEAN**)
- **test / origin/test**: `f9e1e91` (ALL SYNCED+PUSHED · WT CLEAN)
- **pending commits**: 0 (FF merge `91aee07`→`f9e1e91` · pending **1→0**)
- **merge**: **EXECUTED** (TSR1690 · QA-B498 Fixed)
- **changed files** (+155/−8): `notificationChannelStatus.js/test` · `liveBackendProbe.js` · `liveConfig.js` · `liveGlobalSetup.js` · `liveE2eHarness.test.js`
- **related smoke (develop)**: **174/174 PASS** (notificationChannelStatus + liveE2eHarness · 2.47s, 2 · +2 vs TSR1688 172)
- **full npm**: **2617/2617 PASS** (872.26s, 477 · +4 vs 2613)
- **build / audit / live E2E**: build **1230** (9.25s) · audit **0** · live **0/149/0** (33.17s)
- **Open**: 0
- **cross-stream**: **local SYNCED** — BE develop/test **SYNCED `@aa551fb`** · FE **ALL SYNCED+PUSHED `@f9e1e91`** · origin/test **691 BE** unpushed
- **verdict**: **PASS**(FE) · operation **BLOCK**(691 BE)

```
git -C src/frontend log --oneline test..develop
# (empty — ALL SYNCED)

git -C src/frontend show --stat f9e1e91
# fix(v1.2.1/QA-B95): decode unicode-escaped and bare decimal HTML entities in blockers
#  6 files changed, 155 insertions(+), 8 deletions(-)
```
