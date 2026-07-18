<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-07-18T04:26:34Z -->
# frontend develop→test diff — TSR1827 (pending 1 · transfer BLOCK)

- stream: **frontend**
- merge: **SKIP** (`test..develop = 1`, read-only policy)
- develop / test: `@1f9d49c` / `@2789553` (**NOT SYNCED**)
- origin/develop / origin/test: `@1f9d49c` / `@b23711f` (local `test` +1, develop ahead +1)
- qa: **QA-20260718-B608 Open(MEDIUM/BLOCK)** — develop 미이관 pending 1
- verified_at: 2026-07-18T04:26:34Z

## pending range (`2789553..1f9d49c`)

```
1f9d49c fix(v1.2.1/v3/SEC-D34): validate bank deposit excel magic bytes before upload
```

## diff stat (`test..develop`)

```
 src/components/ui/BankDepositImportPanel.jsx      | 13 ++++++++-
 src/components/ui/BankDepositImportPanel.test.jsx | 33 +++++++++++++++++++----
 src/config/excelImportFiles.js                    | 10 +++++++
 src/config/excelImportFiles.test.js               | 27 +++++++++++++++++++
 4 files changed, 77 insertions(+), 6 deletions(-)
```

## verification (`src/frontend-test` @`2789553`)

| item | result |
|------|--------|
| full suite `npm test` | **SKIP(carry)** — peer `vitest run` 동시 실행 중(정책상 신규 실행 금지) · 기준선 **2737/2737 PASS**(TSR1824, 동일 test SHA `2789553`) |
| `npm run build` | **1234 modules PASS** (11.10s) |
| `npm audit --audit-level=high` | **0 vulnerabilities** |
| origin/test push | **미실행** (tester/merge 스크립트·run_agent.py 전담) |
| transfer verdict | **BLOCK** (pending 1 해소 전 PASS 금지) |

## notes
- `1f9d49c`는 bank deposit import 경로에 FE pre-upload magic-byte 검증을 추가한 변경으로, 현재 `test`에 미이관 상태다.
- 이번 사이클은 소스 merge 없이 baseline(`2789553`)만 재검증했다. build/audit는 green이지만 merge gate(`test..develop`)가 열려 있어 transfer는 BLOCK으로 유지한다.
- planner/coder 선행 액션: `src/frontend-test@test`에 `develop` 이관 후 full suite `npm test` 재실행, 결과를 TEST_REPORT/QA_FEEDBACK에 반영.
