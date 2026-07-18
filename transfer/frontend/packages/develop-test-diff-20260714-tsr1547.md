# develop→test diff — TSR 1547 (2026-07-14)

- stream: frontend
- merge: **SKIP** (test `@063c269` → develop `@b7c9fa4`, pending **2** commits; src/frontend-test read-only 정책)
- commits (pending, not merged):
  - `7c5767c ux(a11y): announce new tab on M12 BPO external portal link (UXD-175)`
  - `b7c9fa4 feat(v1.2.1/G2): wire home newsletter launch page and dispatch history`
- test baseline (`src/frontend-test`): **2450/2450 PASS** (836.92s, 465 files)
- develop related: **25/25 PASS** (carry from COD verification)
- build: **1215** modules PASS (9.47s)
- audit: 0 high (carry)
- live E2E: **SKIP** (merge 없음 · carry **116/33/0**)
- origin/test: FE **0 unpushed** @ `063c269`
- QA: Open **0** · transfer **BLOCK** (FE pending 2 + BE origin/test push 631)
- operation: BLOCK (QA-B116 + QA-B95)

## Pending commits (`063c269..b7c9fa4`)

```
b7c9fa4 feat(v1.2.1/G2): wire home newsletter launch page and dispatch history
7c5767c ux(a11y): announce new tab on M12 BPO external portal link (UXD-175)
```

## Diffstat (`063c269..b7c9fa4`)

```
 src/App.jsx                                 |  10 +
 src/api/services.js                         |  35 ++++
 src/components/ui/ClientsContextNav.jsx     |   4 +
 src/config/competitorModuleCoverage.js      |   4 +-
 src/config/competitorModuleCoverage.test.js |   4 +-
 src/layout/navConfig.js                     |   6 +
 src/pages/AccountingBpoPage.jsx             |   1 +
 src/pages/AccountingBpoPage.test.jsx        |   3 +
 src/pages/HomeNewsletterLaunchPage.jsx      | 300 ++++++++++++++++++++++++++++
 src/pages/HomeNewsletterLaunchPage.test.jsx | 209 +++++++++++++++++++
 src/utils/homeNewsletter.js                 | 296 +++++++++++++++++++++++++++
 src/utils/homeNewsletter.test.js            | 133 ++++++++++++
 12 files changed, 1001 insertions(+), 4 deletions(-)
```
