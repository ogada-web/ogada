<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-07-18T08:37:00Z -->

# develop → test diff — TSR1837 (frontend · 2026-07-18)

| field | value |
|-------|-------|
| stream | frontend |
| tsr | 1837 |
| base (prev test HEAD) | `495040f` |
| head (new test HEAD) | `5e816e6` |
| merge type | FF (1 commit) |
| files changed | 2 (+34 / -1) |
| product code changed | YES (refactor: extract constant, behavior unchanged) |
| test code changed | YES (+1 regression test) |
| post-merge npm test | **2745/2745 PASS** (891.13s · 488 files) |
| npm run build | **1234 PASS** (9.87s) |
| npm audit high | **0** |

## Commit absorbed

### `5e816e6` — refactor(v1.2.1/v3/SEC-D34): extract unreadable-excel copy to EXCEL_IMPORT_UNREADABLE_MESSAGE constant

**Author**: jwj3400 · **Date**: 2026-07-18T07:54:08Z

FE pre-upload header-read failure returned hardcoded `"엑셀 파일을 읽을 수 없습니다."` while every
other SEC-D34 message is an exported constant. Extract to `EXCEL_IMPORT_UNREADABLE_MESSAGE` and lock
verbatim against BE house-style message (getBytes IOException + 5 `*ExcelParser` corrupt-body guard,
BNK-856 `0a97b22`) so FE↔BE UX copy stays in lockstep (rules §2 magic-string constant; SEC-D34 axis m).

**Files changed** (`2 files, +34/-1`):
- `src/config/excelImportFiles.js` — export new `EXCEL_IMPORT_UNREADABLE_MESSAGE` constant; replace inline string literal with constant reference (`+11/-1`)
- `src/config/excelImportFiles.test.js` — add regression: header-read error returns `EXCEL_IMPORT_UNREADABLE_MESSAGE` (BE corrupt-body lockstep) (`+24/0`)

**Risk**: Low — pure refactor (no logic change; constant value identical to prior string literal). Test suite locked.

## Diff stat

```
 src/config/excelImportFiles.js      | 11 ++++++++++-
 src/config/excelImportFiles.test.js | 24 ++++++++++++++++++++++++
 2 files changed, 34 insertions(+), 1 deletion(-)
```

## Post-merge verification

| gate | result | detail |
|------|--------|--------|
| FF merge | PASS | `495040f..5e816e6` |
| npm test | **2745/2745 PASS** | 891.13s · 488 files (+1 test vs TSR1835 2744) |
| npm run build | **1234 PASS** | 9.87s |
| npm audit high | **0** | fresh |
| develop WT clean | PASS | WT CLEAN |
| pending (test..develop) | **0** | SYNCED `@5e816e6` |
