# develop→test diff meta — TSR1602 frontend (FF merge+PUSH)
generated: 2026-07-15T07:30:59Z
range: d6f7069..c59da8f (2 commits)
merge: FF EXECUTED (QA-B441 G-LINKAGE-RECORD draft rehydrate + BE max-length validation)
commits:
  - c59da8f fix(v1.2.1/G-LINKAGE-RECORD): map server validation and enforce BE max lengths
  - fae1f34 fix(v1.2.1/G-LINKAGE-RECORD): rehydrate folded summary on draft edit
files: 6 changed, 292 insertions(+), 10 deletions(-)
---
related pre-merge: 36/36 PASS (10.96s, 6 files · G-LINKAGE-RECORD)
npm post-merge: 2539/2539 PASS (859.60s, 471 files · +6 @Test vs 2533)
build: 1222 modules PASS (10.73s @ src/frontend-test)
audit: 0 high
live E2E: default 0 PASS / 149 SKIP / 0 FAIL (33.41s fail-closed · bootstrap-disabled)
  opt-in: SKIP (carry TSR1597 116/33/0 · pipeline speed)
Open: 0
verdict: PASS (FE ALL SYNCED+PUSHED @c59da8f)
cross-stream: SYNCED (BE @a72866f · FE @c59da8f)
operation: BLOCK (origin/test 655 BE · QA-B116+QA-B95)
patch: transfer/frontend/packages/develop-test-diff-20260715-TSR1602.patch
