# develop→test diff — TSR 1551 (2026-07-14)

- stream: frontend
- local merge state: **committed SYNCED** (`test @b7c9fa4` == `develop @b7c9fa4`, pending **0**) + **WT DIRTY 2M**
- merge action: **SKIP** (dirty-tree · pipeline §1-1 · no new SHA)
- dirty WIP: `HomeNewsletterLaunchPage.jsx` + `HomeNewsletterLaunchPage.test.jsx` (+25/-2 · `branchId` → dispatch-history API)
- test baseline (`src/frontend-test`): **CARRY 2450/2450 PASS** (TSR1548 · 833.96s, 465 files)
- build / live E2E: **SKIP** (merge 없음 · live carry **116/33/0**)
- origin/test: committed HEAD **PUSHED** `@b7c9fa4` (FE 0 unpushed) · WIP uncommitted
- QA: Open **1** (**QA-B396** BLOCK) · FE transfer **BLOCK**
- cross-stream: **BLOCK** (BE `@3ea0832` SYNCED · FE dirty)
- operation: **BLOCK** (QA-B116 origin/test **632 BE** + QA-B95 + QA-B396)

## COD commit required

```
src/pages/HomeNewsletterLaunchPage.jsx      # branchId → fetchHomeNewsletterDispatchHistoryApi
src/pages/HomeNewsletterLaunchPage.test.jsx # branch-scope assertion +1 it
```

## Notes

- Full npm suite not re-run (dirty develop · §1-1 coder 압박 우선 · CARRY TSR1548)
- After COD commit + WT CLEAN → TSR FF merge(if ahead) + post-merge npm + live E2E
