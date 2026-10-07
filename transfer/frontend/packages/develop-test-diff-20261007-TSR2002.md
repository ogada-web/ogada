<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-10-07T17:21:00Z -->
# develop → test diff (TSR2002)

- measured: 2026-10-07T17:21:00Z
- test: `29c2304` (`src/frontend-test`, branch `test`, WT CLEAN)
- develop: `29c2304` (`src/frontend`, branch `develop`, WT CLEAN)
- `test...develop`: **0 / 0**
- merge: already on test (reflog `2026-10-07 17:02:57Z` FF `5cf667b`→`29c2304`; this cycle did not merge)
- regression: `npm test` **2865/2865 PASS** (493 files, 843.00s, exit 0). Locked wrapper runs vitest in `src/frontend`; SHA matches test.
- build: `npm run build` in `src/frontend-test` **PASS** (8.64s, 1236 modules)
- audit: full tree **4 high** (dev/transitive) · `npm audit --omit=dev --audit-level=high` **exit 0**

## Pending

없음. `29c2304` `fix(v1.2.1/SEC-D46): reject search-path and reserved attachment hosts (BE lockstep)` 가 develop와 test 양쪽에 있다.

```
 src/pages/HomeNewsletterLaunchPage.test.jsx | 132 +
 src/utils/homeNewsletter.js                 |  34 +
 src/utils/homeNewsletter.test.js            |  31 +
 3 files changed, 193 insertions(+), 4 deletions(-)
```

Tracker: `QA-20261007-B688` **Verified**. Dev-audit residual: `QA-20261007-B689` **Open (HIGH, non-BLOCK)**.

로컬 이관 **PASS**. 운영 승격 **BLOCK** (health DOWN · origin/test unpushed FE+1 BE+1 · QA-B116 · QA-B95).
