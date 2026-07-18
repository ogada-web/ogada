# frontend develop→test diff — TSR 1519

- date: 2026-07-14T02:30:09Z
- develop/test/origin/test: `bc9389d`
- merge: FF `95192f5`→`bc9389d` (pending **2→0**)
- commits:
  - `9578aa3` ux(a11y/FE-16): style day-status excluded roster items (UXD-173)
  - `bc9389d` fix(v1.2.1/G17): wire bathing claim vs indicator27 ownership
- files: 10 (+178/-32)
- related: bathing+transport **35/35 PASS** (7 files)
- post-merge: **2380/2380 PASS** (805.08s, 454 files)
- build: **1206 PASS** (8.86s)
- audit: **0**
- live E2E: **116 PASS / 33 SKIP / 0 FAIL** (37.27s · bootstrap-disabled)
- origin/test: **PUSHED** (`95192f5`→`bc9389d`)

## stat
bc9389d fix(v1.2.1/G17): wire bathing claim vs indicator27 ownership
 src/api/services.js                                |  9 +++-
 .../ui/BathingScheduleIndicator27Panel.jsx         | 52 +++++++++++++++++-----
 .../ui/BathingScheduleIndicator27Panel.test.jsx    | 41 ++++++++++++-----
 src/pages/BathingSchedulePage.jsx                  |  2 +-
 src/pages/BathingSchedulePage.test.jsx             | 17 +++++--
 src/pages/FunctionalRecoveryPage.jsx               |  9 ++++
 src/pages/FunctionalRecoveryPage.test.jsx          | 11 +++++
 src/styles/components.css                          | 10 ++++-
 src/utils/functionalRecoveryCompliance.js          | 31 ++++++++++++-
 src/utils/functionalRecoveryCompliance.test.js     | 28 ++++++++++++
 10 files changed, 178 insertions(+), 32 deletions(-)
