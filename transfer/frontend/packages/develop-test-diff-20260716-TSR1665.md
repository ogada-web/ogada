<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-07-16T01:03:00Z -->
# develop→test diff package — frontend TSR1665

- **stream**: frontend
- **range**: `79763a3..793a43c` (FF · pending **3→0**)
- **test HEAD (pre)**: `79763a3`
- **test HEAD (post)**: `793a43c`
- **develop HEAD**: `793a43c` (WT CLEAN)
- **origin/test (pre-push)**: `79763a3`

## Commits

1. `9181ca8` ux(a11y): fix FE-16 unit-rates CSS and forced-colors (UXD-181)
2. `a89a873` fix(v1.2.1/QA-B95): decode triple-encoded HTML entity blockers
3. `793a43c` feat(v1.2.1/G17): surface dual-numbering guardrail on indicator-27 UI

## Files (13 · +197/−16)

- `src/components/ui/BathingScheduleIndicator27Panel.jsx` (+test)
- `src/config/notificationChannelStatus.js` (+test)
- `src/e2e/liveBackendProbe.js` / `liveConfig.js` / `liveGlobalSetup.js`
- `src/pages/FunctionalRecoveryPage.jsx` (+test)
- `src/styles/components.css`
- `src/test/liveE2eHarness.test.js`
- `src/utils/functionalRecoveryCompliance.js` (+test)

## Verification (TSR1665)

| check | result |
|-------|--------|
| related vitest | **186/186 PASS** (13.57s, 5 files) |
| post-merge vitest | **2599/2599 PASS** (868.69s, 477 · +2 vs 2597) |
| `npm run build` | **1230** modules PASS (10.49s) |
| `npm audit --omit=dev` | **0** vulnerabilities |
| live E2E (default) | **0/149/0** (34.26s · bootstrap-disabled) |
| `origin/test` push | **PASS** `79763a3`→`793a43c` |
| develop/test/origin | **ALL SYNCED `@793a43c`** |

## Closure targets

- **QA-B481** Fixed (develop→test drift · includes G17 `@793a43c`)
- **QA-B479** Fixed carry (triple-encoded FE parity landed in merge)
- residual Open: **QA-B482** (BE dirty-tree) · Planned **QA-B116+QA-B95** · operation BLOCK (origin/test **678 BE**)
