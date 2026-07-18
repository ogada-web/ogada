# develop→test diff — TSR 1543 (2026-07-14)

- stream: frontend
- merge: FF `b12f259` → `063c269` (pending 1→0)
- commits (this merge):
  - `063c269 fix(v1.2.1/M12): align module coverage KPI and SSO blocker messaging`
- pre-merge related: 32/32 PASS (5.84s, 3 files)
- post-merge: 2438/2438 PASS (837.80s, 463 files · +2 vs 2436)
- build: 1215 modules PASS (10.48s)
- audit: 0 high
- live E2E: 116 PASS / 33 SKIP / 0 FAIL (38.17s · bootstrap-disabled)
- origin/test: PUSHED (`b12f259`→`063c269`)
- QA: QA-B391 Fixed · Open 0 · cross-stream SYNCED (BE `@093ac88` · FE `@063c269`)
- operation: BLOCK (QA-B116 origin/test 629 BE + QA-B95)

## Commits (`b12f259..063c269`)

```
063c269 fix(v1.2.1/M12): align module coverage KPI and SSO blocker messaging
```

## Diffstat

```
 src/config/competitorModuleCoverage.js      |  6 ++++--
 src/config/competitorModuleCoverage.test.js | 10 ++++++++--
 src/pages/AccountingBpoPage.test.jsx        |  9 +++++----
 src/utils/accountingBpo.js                  | 12 +++++++++---
 src/utils/accountingBpo.test.js             | 22 +++++++++++++++++-----
 5 files changed, 43 insertions(+), 16 deletions(-)
```
