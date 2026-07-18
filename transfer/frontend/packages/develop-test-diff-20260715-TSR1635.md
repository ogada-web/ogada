# develop → test diff package — TSR 1635 (frontend)

- **when**: 2026-07-15T17:04:09Z
- **stream**: frontend
- **develop**: `e76e631` CLEAN
- **test (local)**: `e76e631` CLEAN
- **origin/test**: `e837185`
- **pending (develop..test local)**: 0
- **pending (origin/test..test)**: 1
- **range**: `origin/test..test`
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
`&#45;`, `&#x2d;`, `&lt;`, `&gt;` HTML entity blocker decoding parity was added across live readiness + notification channel status + liveE2e harness, with related regression tests included. Local `test` is synced, but remote `origin/test` is one commit behind and still needs push before operation promotion.
