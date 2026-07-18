<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-07-16T02:45:22Z -->
# develop→test diff package — frontend TSR1671 (FF merge+PUSH)

- **stream**: frontend
- **range**: `07198a2..2cefb1d` (pending **1→0**)
- **test HEAD**: `2cefb1d`
- **develop HEAD**: `2cefb1d` (WT CLEAN)
- **origin/test**: `2cefb1d` (★ PUSHED)

## Commits

1. `2cefb1d` fix(v1.2.1/QA-B95): decode named-num HTML blocker entities

## Files (6)

- `src/config/notificationChannelStatus.js`
- `src/config/notificationChannelStatus.test.js`
- `src/e2e/liveBackendProbe.js`
- `src/e2e/liveConfig.js`
- `src/e2e/liveGlobalSetup.js`
- `src/test/liveE2eHarness.test.js`

## Verification (TSR1671)

| check | result |
|-------|--------|
| related vitest | **162/162 PASS** (2.44s, 2 · notificationChannelStatus + liveE2eHarness) |
| full vitest | **2602/2602 PASS** (871.44s, 477 · +2 vs 2600) |
| `npm run build` | **1230** modules PASS (10.75s) |
| `npm audit --omit=dev` | **0** vulnerabilities |
| live E2E | default **0 PASS/149 SKIP/0 FAIL** (34.42s · bootstrap-disabled fail-closed) |
| `origin/test` push | **PASS** `07198a2`→`2cefb1d` |
| develop/test/origin | **ALL SYNCED `@2cefb1d`** |
| cross-stream | **local SYNCED**(BE `@777b5a7` · FE `@2cefb1d`) |
| Open | **0** (QA-B486 Fixed) |
| verdict | **PASS**(FE) · operation **BLOCK**(681 BE · QA-B116+QA-B95) |
