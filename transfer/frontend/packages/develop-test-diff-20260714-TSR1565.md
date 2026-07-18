# frontend develop→test diff meta — TSR 1565

- updated: 2026-07-14T19:09:18Z
- merge: FF `0210aaa`→`4d1b01c` (1 commit)
- commit: `4d1b01c` feat(v1.2.1/G2): wire facility-notice DRAFT PATCH and attachmentUrl
- files: 5 (+200/-20)
- related pre-merge: 89/89 PASS (8.18s, 4 files)
- post-merge npm: 2471/2471 PASS (835.38s, 465 files)
- build: 1217 modules PASS (9.24s)
- audit: 0 high
- live E2E: 116 PASS / 33 SKIP / 0 FAIL (39.85s · bootstrap-disabled)
- origin/test: PUSHED `0210aaa`→`4d1b01c`
- QA: QA-20260714-B410 Fixed · Open 0

## Diffstat
```
 src/api/billingGuardianPlatformServices.test.js |  18 +++-
 src/api/services.js                             |  11 ++
 src/pages/HomeNewsletterLaunchPage.jsx          | 138 ++++++++++++++++++++----
 src/pages/HomeNewsletterLaunchPage.test.jsx     |  51 ++++++++-
 src/utils/homeNewsletter.js                     |   2 +
 5 files changed, 200 insertions(+), 20 deletions(-)
```
