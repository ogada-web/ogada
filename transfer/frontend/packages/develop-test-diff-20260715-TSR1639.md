# develop → test diff package — TSR 1639 (frontend)

- **when**: 2026-07-15T18:10:48Z
- **stream**: frontend
- **develop**: `c779ca1` CLEAN
- **test (local)**: `c779ca1` CLEAN
- **origin/test**: `c779ca1` (**★ PUSHED** from `e76e631`)
- **pending (develop..test local)**: 0 (was 1)
- **pending (origin/test..test)**: 0
- **range**: `e76e631..c779ca1` (FF merge + origin/test push)
- **subject**: fix(v1.2.1/QA-B95): multi-pass decode double-encoded HTML entities

## Commits
c779ca1 fix(v1.2.1/QA-B95): multi-pass decode double-encoded HTML entities

## Files
src/config/notificationChannelStatus.js
src/config/notificationChannelStatus.test.js
src/e2e/liveBackendProbe.js
src/e2e/liveConfig.js
src/e2e/liveGlobalSetup.js
src/test/liveE2eHarness.test.js

## Summary
FF merge develop→test `@c779ca1` (QA-B95 multi-pass / double-encoded HTML entity decode · FE parity deepen vs BE `@2768252`). related **151/151** · post-merge **2570/2570**(+2 vs 2568) · build **1225** · audit **0** · live default **0/149/0** · origin/test PUSHED. FE ALL SYNCED+PUSHED. residual operation BLOCK = origin/test **669 BE** (QA-B116).
