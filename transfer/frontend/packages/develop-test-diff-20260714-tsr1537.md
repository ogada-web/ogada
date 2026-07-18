# develop→test diff — TSR 1537 (2026-07-14)

- stream: frontend
- merge: FF `891231d` → `84b336b` (pending 1→0)
- commits:
  - `84b336b feat(v1.2.1/M12): wire accounting BPO launch catalog from API`
- pre-merge related: 20/20 PASS (5.59s, 3 files)
- post-merge: 2426/2426 PASS (826.61s, 463 files)
- build: 1215 modules PASS (9.76s)
- audit: 0 high
- live E2E: 116 PASS / 33 SKIP / 0 FAIL (41.57s)
- origin/test: PUSHED (`891231d`→`84b336b`)
- QA: QA-B387 Fixed · Open 0 · cross-stream SYNCED (BE `@54a3e56` · FE `@84b336b`)
- operation: BLOCK (QA-B116 origin/test 627 BE + QA-B95)

## Commits

```
84b336b feat(v1.2.1/M12): wire accounting BPO launch catalog from API
```

## Diffstat

```
 src/api/services.js                         |   8 ++
 src/config/competitorModuleCoverage.js      |   2 +-
 src/config/competitorModuleCoverage.test.js |   4 +-
 src/pages/AccountingBpoPage.jsx             | 143 ++++++++++++++++++++++++----
 src/pages/AccountingBpoPage.test.jsx        |  77 ++++++++++++++-
 src/utils/accountingBpo.js                  | 111 ++++++++++++++++++++-
 src/utils/accountingBpo.test.js             |  51 ++++++++++
 7 files changed, 368 insertions(+), 28 deletions(-)
```
