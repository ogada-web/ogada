<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-07-15T17:00:02Z -->
# develop→test diff — frontend TSR1634

- **develop**: `e76e631` — fix(v1.2.1/QA-B95): decode HTML entity live readiness blockers
- **test (pre)**: `e837185`
- **pending**: 1 commit
- **range**: `e837185..e76e631`

## Commits
```
e76e631 fix(v1.2.1/QA-B95): decode HTML entity live readiness blockers
```

## Stat
```
 .../visits/VisitRfidDiffComparePanel.jsx           |  7 +-
 .../visits/VisitRfidDiffComparePanel.test.jsx      | 33 +++++++++
 src/config/notificationChannelStatus.js            | 66 +++++++++++++++++-
 src/config/notificationChannelStatus.test.js       | 10 +++
 src/e2e/liveBackendProbe.js                        | 80 ++++++++++++++++++++--
 src/e2e/liveConfig.js                              | 44 +++++++++++-
 src/e2e/liveGlobalSetup.js                         | 44 +++++++++++-
 src/test/liveE2eHarness.test.js                    | 25 +++++++
 8 files changed, 296 insertions(+), 13 deletions(-)
```

## Files
```
src/components/visits/VisitRfidDiffComparePanel.jsx
src/components/visits/VisitRfidDiffComparePanel.test.jsx
src/config/notificationChannelStatus.js
src/config/notificationChannelStatus.test.js
src/e2e/liveBackendProbe.js
src/e2e/liveConfig.js
src/e2e/liveGlobalSetup.js
src/test/liveE2eHarness.test.js
```
