# frontend develop→test diff meta — TSR 1563

- updated: 2026-07-14T18:27:41Z
- merge: FF `d613826`→`0210aaa` (1 commit)
- commit: `0210aaa` feat(v1.2.1/G2): persist compose preview as facility-notice DRAFT
- files: 6 (+116/-19)
- related pre-merge: 38/38 PASS (6.95s, 3 files)
- post-merge npm: 2471/2471 PASS (837.74s, 465 files)
- build: 1217 modules PASS (9.26s)
- audit: 0 high
- live E2E: 116 PASS / 33 SKIP / 0 FAIL (37.38s · bootstrap-disabled)
- origin/test: PUSHED `d613826`→`0210aaa`
- QA: QA-20260714-B408 Fixed · Open 0

## Diffstat
```
 src/config/competitorModuleCoverage.js      |  4 +--
 src/config/competitorModuleCoverage.test.js |  4 +--
 src/pages/HomeNewsletterLaunchPage.jsx      | 45 ++++++++++++++++++++++-------
 src/pages/HomeNewsletterLaunchPage.test.jsx |  9 ++++++
 src/utils/homeNewsletter.js                 | 44 ++++++++++++++++++++++++----
 src/utils/homeNewsletter.test.js            | 29 +++++++++++++++++++
 6 files changed, 116 insertions(+), 19 deletions(-)
```
