# develop→test diff · TSR1661 · merge SKIP (dirty-tree §1-1)

- range: SHA develop/test/origin/test **ALL SYNCED `@79763a3`** · pending commits **0**
- develop WT: **DIRTY 5M** (+26/−13)
  - `src/config/notificationChannelStatus.js` — decode pass 3→5 · triple-encoded `&AMP;AMP;#…` (BE `@33f388d`)
  - `src/config/notificationChannelStatus.test.js` — +1 `it` triple-encoded regression
  - `src/e2e/liveBackendProbe.js` · `liveConfig.js` · `liveGlobalSetup.js` — same pass/parity
- merge: **SKIP** (dirty-tree · coder commit first · QA-B479)
- related / post-merge / build / live: **SKIP** · npm **CARRY 2595/2595** (TSR1659)
- origin/test: unchanged `@79763a3` (FE 0 unpushed)
- Open: **1** (**QA-B479** FE DIRTY)
- cross-stream: BLOCK (FE dirty · BE `@33f388d` SYNCED)
- operation: BLOCK (origin/test **677 BE** + QA-B116 + QA-B95)
- coder action: commit the 5 dirty files on `src/frontend` develop → WT CLEAN → next TSR FF/revalidate
