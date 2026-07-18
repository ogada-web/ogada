<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-07-18T05:02:00Z -->
# frontend develop→test diff — TSR1829 (pending 2 · transfer BLOCK)

- stream: **frontend**
- merge: **SKIP** (`test..develop = 2`, read-only policy)
- develop / test: `@6f8e349` / `@2789553` (**NOT SYNCED**)
- origin/develop / origin/test: `@6f8e349` / `@b23711f` (local `test` +1, develop SYNCED)
- qa: **QA-20260718-B608 Open(MEDIUM/BLOCK)** — develop 미이관 pending **2**
- verified_at: 2026-07-18T05:02:00Z

## pending range (`2789553..6f8e349`)

```
6f8e349 test(v1.2.1/v3/SEC-D34): lock RFID compare dual-excel pre-upload magic-byte
1f9d49c fix(v1.2.1/v3/SEC-D34): validate bank deposit excel magic bytes before upload
```

## diff stat (`test..develop`)

```
 src/components/ui/BankDepositImportPanel.jsx       | 13 ++++++++-
 src/components/ui/BankDepositImportPanel.test.jsx  | 33 ++++++++++++++++++----
 src/components/visits/VisitRfidDiffComparePanel.test.jsx | 31 ++++++++++++++++++++
 src/config/excelImportFiles.js                     | 16 +++++++++--
 src/config/excelImportFiles.test.js                | 27 ++++++++++++++++++
 5 files changed, 112 insertions(+), 8 deletions(-)
```

## verification (`src/frontend-test` @`2789553`)

| item | result |
|------|--------|
| full suite `npm test` | **SKIP(carry)** — peer `vitest run`(src/frontend) 동시 실행 중 · 기준선 **2737/2737 PASS**(TSR1824, 동일 test SHA `2789553`) |
| `npm run build` | **1234 modules PASS** (11.29s) |
| `npm audit --audit-level=high` | **0 vulnerabilities** |
| origin/test push | **미실행** (tester/merge 스크립트·run_agent.py 전담) |
| transfer verdict | **BLOCK** (pending 2 해소 전 PASS 금지) |

## notes
- TSR1827(pending 1=`1f9d49c`) 이후 coder가 `6f8e349`(RFID compare spoof-reject regression lock·test-only) 추가 → pending **1→2**.
- `1f9d49c`: bank deposit import FE pre-upload magic-byte 검증(BankDepositImportPanel + excelImportFiles validator).
- `6f8e349`: VisitRfidDiffComparePanel planFile MIME-spoof reject 회귀 test + excelImportFiles JSDoc 4-validator 정합(제품 코드 무변경).
- baseline(`2789553`) build/audit green이나 merge gate 미충족 → transfer BLOCK.
- planner/coder 선행: `src/frontend-test@test` FF 이관(`6f8e349`) + post-merge full suite `npm test` 재실행.
