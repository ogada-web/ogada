# develop→test diff — TSR 1527 (2026-07-14)

- stream: frontend
- merge: FF `9ea151b` → `10bf059` (pending 1→0)
- commit: `10bf059 fix(v1.2.1/G17): normalize bathing indicator ownership metadata`
- pre-merge related: 24/24 PASS (11.20s, 5 files)
- post-merge: 2402/2402 PASS (811.46s, 459 files)
- build: 1211 modules PASS (9.06s)
- audit: 0 high
- live E2E: 116 PASS / 33 SKIP / 0 FAIL (37.57s)
- origin/test: PUSHED (`9ea151b`→`10bf059`)
- QA: QA-B379 Fixed · Open 0 · cross-stream SYNCED (BE `@907007e` · FE `@10bf059`)
- operation: BLOCK (QA-B116 origin/test 622 BE + QA-B95)

## Commits

```
10bf059 fix(v1.2.1/G17): normalize bathing indicator ownership metadata
```

## Diffstat

```
 .../ui/BathingScheduleIndicator27Panel.jsx         | 37 ++++++++++++++++++++--
 .../ui/BathingScheduleIndicator27Panel.test.jsx    | 37 ++++++++++++++++++++++
 2 files changed, 71 insertions(+), 3 deletions(-)
```
