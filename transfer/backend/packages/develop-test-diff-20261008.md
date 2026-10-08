<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-10-08T01:54:06Z -->
# develop → test diff (TSR2004)

- measured: 2026-10-08T01:54:06Z
- test: `4aad7cc2` (`src/backend-test`, branch `test`, WT CLEAN)
- develop: `92466cfb` (`src/backend`, branch `develop`, WT CLEAN)
- `test...develop`: **0 / 2**
- merge: SKIP (no backend version with `merge_status=ready`; v3 token `merged`, v3.1 `pending`; tester did not merge)
- regression on test: `mvn -o -B test` **2479/2479 PASS** (01:19 min, 412 suites, 0F/0E/0S, BUILD SUCCESS, EXIT 0)
- develop targeted: catalog + client-group tests **26/26 PASS** (11.7s). Full suite on develop was not run.

## Pending

`92466cfb` `feat(v3.1/US-P01): add program catalog master API`

`d73aec11` `feat(v3.1/US-P01): add program client group assignment API`

- 26 files, +1831
- new migration on develop only: `V197__program_catalog_us_p01.sql` (test max V196)
- tracker: `QA-20261007-B690` **Open BLOCK** (pending 1→2)

로컬 이관 **BLOCK**. 운영 승격 **BLOCK** (QA-B690 · health DOWN · push 미수행 · origin/test unpushed BE+1 FE+1 · disk 95%).
