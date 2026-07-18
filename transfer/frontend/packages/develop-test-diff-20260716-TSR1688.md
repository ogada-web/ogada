<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-07-16T07:42:00Z -->
# develop→test diff package — frontend TSR1688

- **stream**: frontend
- **develop HEAD**: `91aee07` (**WT DIRTY 6M** — QA-B498 WIP uncommitted)
- **test / origin/test**: `91aee07` (SYNCED+PUSHED · WT CLEAN)
- **pending commits**: 0 (HEAD aligned; dirty working tree blocks merge)
- **merge**: **SKIP** (§1-1 dirty-tree · 이관 규율 1·5·7)
- **dirty files** (+118/−8): `notificationChannelStatus.js/test` · `liveBackendProbe.js` · `liveConfig.js` · `liveGlobalSetup.js` · `liveE2eHarness.test.js`
- **related smoke (develop dirty)**: **172/172 PASS** (notificationChannelStatus + liveE2eHarness · 2.52s, 2 · +2 vs TSR1684 170)
- **full npm**: **CARRY 2613/2613 PASS** (TSR1684 · same committed SHA)
- **build / audit / live E2E**: **SKIP** (no merge · carry TSR1684: build 1230 · audit 0 · live 0/149/0)
- **Open**: 1 — **QA-B498 BLOCK** (FE develop dirty · BE `@8c6cd6a` lockstep gap)
- **cross-stream**: **BLOCK** — BE develop/test **SYNCED `@8c6cd6a`** · FE develop **DIRTY 6M** · origin/test **690 BE** unpushed
- **verdict**: **BLOCK**(FE dirty-tree)

```
git -C src/frontend status -sb
# ## develop...origin/develop
#  M src/config/notificationChannelStatus.js
#  M src/config/notificationChannelStatus.test.js
#  M src/e2e/liveBackendProbe.js
#  M src/e2e/liveConfig.js
#  M src/e2e/liveGlobalSetup.js
#  M src/test/liveE2eHarness.test.js

git -C src/frontend log --oneline test..develop
# (empty — HEAD synced; WT dirty)
```
