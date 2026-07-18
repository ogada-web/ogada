<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-07-18T14:40:22Z -->
# develop-test diff (frontend) — TSR1854

- stream: `frontend`
- test branch: `test`
- merge: `d6f3889 -> 8766331` (fast-forward)
- scope: id=2 transport departure-round out-of-range reject

## Commit

- `8766331` `fix(v1.2.1/transport): reject out-of-range departure-round input (id=2 form polish)`

## Changed files

```text
src/config/transport.js
src/config/transport.test.js
```

## Diff stat

```text
src/config/transport.js      | 20 +++++++++++++++++++-
src/config/transport.test.js | 24 ++++++++++++++++++++++++
2 files changed, 43 insertions(+), 1 deletion(-)
```
