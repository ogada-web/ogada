# develop → test diff package — TSR 1636 (frontend)

- **when**: 2026-07-15T17:19:23Z
- **stream**: frontend
- **develop**: `e76e631` CLEAN
- **test (local)**: `e76e631` CLEAN
- **origin/test**: `e76e631` (**★ PUSHED** from `e837185`)
- **pending (develop..test local)**: 0
- **pending (origin/test..test)**: 0
- **range**: `e837185..e76e631` (origin/test push only · no new local merge)
- **subject**: fix(v1.2.1/QA-B95): decode HTML entity live readiness blockers

## Commits
e76e631 fix(v1.2.1/QA-B95): decode HTML entity live readiness blockers

## Files
src/components/visits/VisitRfidDiffComparePanel.jsx
src/components/visits/VisitRfidDiffComparePanel.test.jsx
src/config/notificationChannelStatus.js
src/config/notificationChannelStatus.test.js
src/e2e/liveBackendProbe.js
src/e2e/liveConfig.js
src/e2e/liveGlobalSetup.js
src/test/liveE2eHarness.test.js

## Summary
TSR1635 already validated local develop/test @`e76e631` (npm 2568/2568 · build 1225). TSR1636 closed **QA-B465** by pushing `origin/test` `e837185`→`e76e631`, reconfirmed related **159/159**, build **1225**, audit **0**. FE ALL SYNCED+PUSHED. Live E2E SKIP (no merge). residual operation BLOCK = origin/test **668 BE** (QA-B116).
