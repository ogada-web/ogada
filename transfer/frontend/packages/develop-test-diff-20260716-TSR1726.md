<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-07-16T17:48:07Z -->
# develop→test diff package — frontend TSR1726

- **stream**: frontend
- **develop HEAD**: `73aa6dd` (WT **CLEAN**)
- **test / origin/test HEAD**: `8a05640` (WT **CLEAN**)
- **pending**: **3** (`test..develop`)
  1. `ed48077` — `ux(a11y): fix ds-muted and add ds-checkbox-group FE-16 (UXD-184)`
  2. `031abef` — `fix(v1.2.1/QA-B95): decode figure/punctuation/ideographic space entity aliases`
  3. `73aa6dd` — `fix(v1.2.1/QA-B95): decode fractional em space entity aliases`
- **diffstat** (`8a05640..73aa6dd`): 8 files, +131/−3
  - `notificationChannelStatus.js` + `.test.js`
  - `liveBackendProbe.js` · `liveConfig.js` · `liveGlobalSetup.js`
  - `liveE2eHarness.test.js`
  - `components.css` · `ClientLinkageRecordsPanel.jsx` (UXD-184)
- **related**: baseline **195/195** · develop pre-merge **199/199** (+4)
- **post-merge expected**: ~**2643/2643** (+4 vs TSR1721 2639)
- **merge**: **SKIP** (본 사이클 `src/frontend`·`src/frontend-test` 소스 수정 금지)
- **Open**: QA-20260716-B526 (FE pending 3) · QA-20260716-B525 (BE pending 2)
- **BE lockstep**: `@08cdb87` + `@e4123c3` vs test `@ff80f0b`
- **verdict**: **BLOCK** — next TSR cycle FF merge `@73aa6dd` + origin/test push
