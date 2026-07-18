# frontend develop→test diff — TSR 1517

- date: 2026-07-14T01:27:13Z
- develop/test/origin/test: `95192f5`
- merge: FF `0c6950a`→`95192f5`
- commit: `fix: align indicator 27 copy with functional recovery`
- files: 6 (+17/-15)
- related: bathing **8/8 PASS**
- post-merge: **2379/2379 PASS** (804.84s, 454 files)
- build: **1206 PASS** (8.92s)
- audit: **0**
- live E2E: **116 PASS / 33 SKIP / 0 FAIL** (37.84s · bootstrap-disabled)

## stat
95192f5 fix: align indicator 27 copy with functional recovery
 src/api/services.js                                    |  2 +-
 src/components/ui/BathingScheduleIndicator27Panel.jsx  | 18 ++++++++++--------
 .../ui/BathingScheduleIndicator27Panel.test.jsx        |  6 +++---
 src/pages/BathingSchedulePage.jsx                      |  2 +-
 src/pages/BathingSchedulePage.test.jsx                 |  2 +-
 src/styles/components.css                              |  2 +-
 6 files changed, 17 insertions(+), 15 deletions(-)
