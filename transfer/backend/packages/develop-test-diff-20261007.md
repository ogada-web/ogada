<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-10-07T16:58:12Z -->
# develop → test diff (TSR2000)

- measured: 2026-10-07T16:58:12Z
- test: `1e8857b4` (`src/backend-test`, branch `test`)
- develop: `4aad7cc2` (`src/backend`, branch `develop`, WT CLEAN)
- `test...develop`: **0 / 1**
- merge: **SKIP**
- regression on test: `mvn -o -B test` **2476/2476 PASS** (01:44 min, 412 suites)

## Pending (not on test)

`4aad7cc2` fix(v3/SEC-D46): reject search-path and reserved attachment hosts

```
.../domain/FacilityNoticeSupport.java              | 33 +++++++++--
.../domain/FacilityNoticeServiceTest.java          | 53 +++++++++++++++++
.../domain/FacilityNoticeSupportTest.java          | 68 ++++++++++++++++++++++
3 files changed, 149 insertions(+), 5 deletions(-)
```

Tracker: `QA-20261007-B687` (BLOCK). COD Fixed: `QA-20261007-B686`.
