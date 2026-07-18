<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-07-16T09:27:31Z -->
# develop→test diff package — frontend TSR1693

- **stream**: frontend
- **develop HEAD**: `f5dded2` (WT **CLEAN**)
- **test / origin/test**: `f5dded2` (ALL SYNCED+PUSHED · WT CLEAN)
- **pending commits**: 0 (was **2** before merge)
- **merge**: **FF EXECUTED** `f9e1e91`→`f5dded2` (UXD-182 a11y + G2 branch-scope fallback)
- **changed files** (7):
  - `src/components/ui/BathingScheduleIndicator27Panel.jsx`
  - `src/components/ui/Pagination.jsx`
  - `src/pages/AccountingBpoPage.jsx`
  - `src/pages/FunctionalRecoveryPage.jsx`
  - `src/pages/HomeNewsletterLaunchPage.jsx`
  - `src/pages/HomeNewsletterLaunchPage.test.jsx`
  - `src/styles/components.css`
- **related smoke (develop)**: **71/71 PASS** (HomeNewsletterLaunchPage + AccountingBpoPage + accountingBpo + FunctionalRecoveryPage + BathingScheduleIndicator27Panel · 17.56s, 5)
- **full npm**: **2618/2618 PASS** (+1 vs 2617 · 869.99s, 477)
- **build / audit / live E2E**: build **1230** (9.11s) · audit **0** · live **0/149/0** (33.40s)
- **Open**: 0
- **cross-stream**: **local SYNCED** — BE develop/test **SYNCED `@431859c`** · FE **ALL SYNCED+PUSHED `@f5dded2`** · origin/test **692 BE** unpushed
- **verdict**: **PASS**(FE) · operation **BLOCK**(692 BE)

```
git -C src/frontend log --oneline test..develop
# (empty — ALL SYNCED)

git -C src/frontend rev-parse develop test origin/test
# f5dded2 f5dded2 f5dded2

git -C src/frontend log --oneline f9e1e91..f5dded2
# f5dded2 fix(v1.2.1/G2): use first valid branch scope fallback
# 0a5ec86 ux(a11y): M12 SSO blockers, G17 dual-numbering, G2 pagination (UXD-182)
```
