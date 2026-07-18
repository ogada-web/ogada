# develop→test diff · TSR1630 · SYNCED reconfirm (no merge)

- range: none (already SYNCED `@5843845` · develop=test=origin/test)
- merge: **SKIP**
- related reconfirm: **62/62 PASS** (5.80s · 2 files · VisitRfidDiffComparePanel + billingGuardianPlatformServices)
- npm: **CARRY 2564/2564 PASS** (TSR1629 · same SHA · 859.19s, 472)
- build: **1225** modules (9.31s reconfirm) · audit **0 high**
- live: **SKIP**(no merge · carry default **0/149/0** TSR1629)
- Open: **1**(QA-B461 BE · develop `@27de3a3` vs test `@7868384` pending 1)
- cross-stream: BLOCK (BE only · FE `@5843845` ALL SYNCED+PUSHED)
- operation: BLOCK (origin/test **666 BE** · QA-B116 + QA-B95)
- note: `scripts/npm-test-locked.sh` cds to `src/frontend` (develop WT); at SYNCED SHA this equals `src/frontend-test@5843845`
