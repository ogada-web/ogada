<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-07-14T23:30:00+00:00 -->
<!-- tester-sync: TSR 1576차 2026-07-14T23:30:00+00:00 (frontend) -->

# develop-test diff (TSR1576)

- stream: `frontend`
- test(worktree): `d4e1e68`
- develop: `5b3075f`
- pending commits: `1`
- range: `d4e1e68..5b3075f`

## Commit(s)

- `5b3075f` feat(v1.2.1/G2): sanitize facility-notice attachments and open clone for edit

## Changed files

```text
src/config/competitorModuleCoverage.js      |   3 +-
src/pages/HomeNewsletterLaunchPage.jsx      |  70 +++++++++++------
src/pages/HomeNewsletterLaunchPage.test.jsx | 113 +++++++++++++++++++++++++++-
src/utils/homeNewsletter.js                 |  32 ++++++--
src/utils/homeNewsletter.test.js            |  30 +++++++-
5 files changed, 216 insertions(+), 32 deletions(-)
```

## Verification snapshot

- `npm test` (locked): `2493/2493 PASS` in `832.61s` (lock script targets `src/frontend`)
- related regression: `40/40 PASS` (`HomeNewsletterLaunchPage.test.jsx`, `homeNewsletter.test.js`)
- `npm run build` (`src/frontend-test`): `1217 modules PASS` (`9.24s`)
- `npm audit --omit=dev --audit-level=high` (`src/frontend-test`): `0 high`
