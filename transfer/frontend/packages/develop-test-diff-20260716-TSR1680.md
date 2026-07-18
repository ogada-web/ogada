<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-07-16T05:15:30Z -->
# develop→test diff package — frontend TSR1680

- **stream**: frontend
- **develop / test / origin/test**: `83e6296` (ALL SYNCED+PUSHED · WT CLEAN)
- **pending commits**: 0
- **range**: `b42174a..83e6296` (FF-merged TSR1679 · origin/test PUSH confirmed TSR1680)
- **commit**: `83e6296` — `fix(v1.2.1/QA-B95): decode soft-hyphen and whitespace HTML entities`
- **related smoke**: **166/166 PASS** (notificationChannelStatus + liveE2eHarness · 2.42~2.48s)
- **full npm**: **2609/2609 PASS** (872.44s, 477)
- **build**: **1230** modules PASS
- **audit**: 0 high
- **live E2E**: **0 PASS / 149 SKIP / 0 FAIL** (33.30s · bootstrap-disabled fail-closed)
- **Open**: 0 (QA-B492 Fixed)
- **cross-stream**: BLOCK — BE `c67c7ed` pending 1 vs test `4bf5684` · origin/test **684 BE**
- **verdict**: PASS (FE)

```
git -C src/frontend log --oneline test..develop
# (empty — synced)

git -C src/frontend show --stat 83e6296
# src/config/notificationChannelStatus.js(+test)
# src/e2e/liveBackendProbe.js · liveConfig.js · liveGlobalSetup.js
# src/test/liveE2eHarness.test.js
```
