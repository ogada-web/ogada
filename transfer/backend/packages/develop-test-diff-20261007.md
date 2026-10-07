<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-10-07T17:40:00Z -->
# develop → test diff (TSR2003)

- measured: 2026-10-07T17:40:00Z
- test: `4aad7cc2` (`src/backend-test`, branch `test`, WT CLEAN)
- develop: `d73aec11` (`src/backend`, branch `develop`, WT CLEAN)
- `test...develop`: **0 / 1**
- merge: SKIP (no backend version with `merge_status=ready`; tester did not merge)
- regression on test: `mvn -o -B test` **2479/2479 PASS** (01:24 min, 412 suites, 0F/0E/0S, BUILD SUCCESS, EXIT 0)
- develop targeted: `ProgramClientGroup*Test` **14/14 PASS** (18.1s). Full suite on develop was not run.

## Pending

`d73aec11` `feat(v3.1/US-P01): add program client group assignment API`

- 14 files, +949
- no new Flyway migration (V179 reuse, max on test V196)
- tracker: `QA-20261007-B690` **Open BLOCK**

로컬 이관 **BLOCK**. 운영 승격 **BLOCK** (QA-B690 · health DOWN · push 미수행 · origin/test unpushed BE+1 FE+1).
