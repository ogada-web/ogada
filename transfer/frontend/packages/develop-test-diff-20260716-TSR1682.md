<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-07-16T05:52:33Z -->
# develop→test diff package — frontend TSR1682

- **stream**: frontend
- **develop / test / origin/test**: `1bc6eab` (ALL SYNCED+PUSHED · WT CLEAN)
- **pending commits**: 0
- **range**: `83e6296..1bc6eab` (local FF already present · origin/test PUSH confirmed)
- **commit**: `1bc6eab` — `fix(v1.2.1/QA-B95): strip invisible Unicode format chars in blockers`
- **related smoke**: **168/168 PASS** (notificationChannelStatus + liveE2eHarness · 2.45s)
- **full npm**: **2611/2611 PASS** (870.66s, 477 · +2 vs TSR1680 2609)
- **build**: **1230** modules PASS (9.14s)
- **audit**: 0 high
- **live E2E**: **0 PASS / 149 SKIP / 0 FAIL** (33.34s · bootstrap-disabled fail-closed)
- **Open**: 0 (QA-B494 Fixed)
- **cross-stream**: local SYNCED — BE `@20ac77f` · FE `@1bc6eab` ALL PUSHED · origin/test **685 BE** unpushed
- **verdict**: PASS (FE)

```
git -C src/frontend log --oneline test..develop
# (empty — synced)

git -C src/frontend show --stat 1bc6eab
# src/config/notificationChannelStatus.js(+test)
# src/e2e/liveBackendProbe.js · liveConfig.js · liveGlobalSetup.js
# src/test/liveE2eHarness.test.js
```
