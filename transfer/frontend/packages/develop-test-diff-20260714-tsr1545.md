# develop→test diff — TSR 1545 (2026-07-14)

- stream: frontend
- merge: **SKIP** (develop `@7c5767c` pending **1** + WT **DIRTY 6M+2U** HomeNewsletterLaunch WIP)
- commits (pending, not merged):
  - `7c5767c ux(a11y): announce new tab on M12 BPO external portal link (UXD-175)`
- uncommitted WIP (dirty-tree BLOCK):
  - `App.jsx`, `services.js`, `ClientsContextNav.jsx`, `competitorModuleCoverage.js`(+test), `navConfig.js`
  - `HomeNewsletterLaunchPage.jsx`, `utils/homeNewsletter.js` (untracked)
- pre-merge related (committed UXD-175): **6/6 PASS** (5.86s, `AccountingBpoPage.test.jsx`)
- post-merge: **SKIP** (merge none · CARRY TSR1543 **2438/2438** @ test `063c269`)
- build: **1215** modules PASS reconfirm (9.19s)
- audit: 0 high
- live E2E: **SKIP** (merge none · carry **116/33/0**)
- origin/test: FE **0 unpushed** @ `063c269` · develop **1** ahead of test (unmerged)
- QA: **QA-B393 Open**(BLOCK · dirty-tree) · cross-stream **BLOCK** (BE `@6ab4d67` · FE pending+dirty)
- operation: BLOCK (QA-B116 origin/test **630 BE** + QA-B95)

## Pending commits (`063c269..develop`)

```
7c5767c ux(a11y): announce new tab on M12 BPO external portal link (UXD-175)
```

## Dirty diffstat (uncommitted · `@7c5767c` working tree)

```
 src/App.jsx                                 | 10 ++++++++++
 src/api/services.js                         |  8 ++++++++
 src/components/ui/ClientsContextNav.jsx     |  4 ++++
 src/config/competitorModuleCoverage.js      |  4 ++--
 src/config/competitorModuleCoverage.test.js |  4 ++--
 src/layout/navConfig.js                     |  6 ++++++
?? src/pages/HomeNewsletterLaunchPage.jsx
?? src/utils/homeNewsletter.js
 6 files changed, 32 insertions(+), 4 deletions(-) · 2 untracked
```
