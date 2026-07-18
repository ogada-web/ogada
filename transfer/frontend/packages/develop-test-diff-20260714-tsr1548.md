# develop→test diff — TSR 1548 (2026-07-14)

- stream: frontend
- local merge state: **SYNCED** (`test @b7c9fa4` == `develop @b7c9fa4`, pending **0**)
- merge action: **SKIP** (already synced; `src/frontend-test` read-only policy)
- test baseline (`src/frontend-test`): **2450/2450 PASS** (833.96s, 465 files)
- build: **1217** modules PASS (8.96s)
- live E2E: **SKIP** (merge 없음 · carry **116/33/0**)
- origin/test: **BE 631 + FE 2 unpushed** (`origin/test @063c269` vs local `test @b7c9fa4`)
- QA: Open **0** · transfer **BLOCK** (origin/test push pending)
- operation: **BLOCK** (QA-B116 + QA-B95 + origin/test push backlog)

## Unpushed commits (`origin/test..test`)

```
b7c9fa4 feat(v1.2.1/G2): wire home newsletter launch page and dispatch history
7c5767c ux(a11y): announce new tab on M12 BPO external portal link (UXD-175)
```

## Diffstat (`origin/test..test`)

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
