<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-07-18T06:05:00Z -->
# frontend develop→test 이관 패키지 — TSR1831 (2026-07-18)

## 요약
- **merge**: develop→test **FF** `2789553`→`51a3db4` (pending **4→0**) via `./scripts/git_merge_to_test.sh frontend TSR1831`
- **post-merge full suite** `npm test`: **2742/2743 PASS · 1 FAIL** (898.70s · 488 test files)
- **build** `npm run build`: **1234 modules PASS** (10.74s)
- **audit** `npm audit --audit-level=high`: **0 vulnerabilities**
- **verdict**: **BLOCK** — post-merge 회귀 1건 (**QA-20260718-B609**)

## 이관 커밋 (4)
| SHA | 종류 | 요약 |
|-----|------|------|
| `1f9d49c` | **제품**(fix) | bank deposit excel 업로드 전 매직바이트 검증(`validateBankDepositExcelImportFile`·xlsx-only OOXML) — SEC-D34 5번째 경로 |
| `6f8e349` | test | RFID compare 이중엑셀 pre-upload magic-byte spoof-reject 회귀 lock |
| `d0c8fd2` | **제품**(css) | UXD-192 리포트 페이지 인쇄 시 context navigation 숨김 |
| `51a3db4` | test | billing NHIS(청구내역상세) import MIME-spoof reject 회귀 lock |

## diffstat (`2789553..51a3db4`)
```
 src/components/ui/BankDepositImportPanel.jsx       | 13 ++++++-
 src/components/ui/BankDepositImportPanel.test.jsx  | 33 ++++++++++++++---
 src/components/visits/VisitRfidDiffComparePanel.test.jsx | 31 ++++++++++++++++
 src/config/excelImportFiles.js                     | 16 +++++++-
 src/config/excelImportFiles.test.js                | 27 ++++++++++++++
 src/pages/NHISImportPage.test.jsx                  | 34 +++++++++++++++++
 src/styles/components.css                          |  2 +-
 src/styles/printStylesheet.test.js                 | 43 ++++++++++++++++++++++
 8 files changed, 190 insertions(+), 9 deletions(-)
```

## 회귀 (QA-20260718-B609 · HIGH/BLOCK)
- **test**: `src/pages/pilotPageFlows.test.jsx > pilotPageFlows > v1.2.1 P1 flows > imports bank deposit excel from payment page (US-L01)`
- **위치**: `pilotPageFlows.test.jsx:4207` (`waitFor` timeout)
- **원인**: `1f9d49c` 가 제품 코드에 `validateBankDepositExcelImportFile`(xlsx-only OOXML 매직바이트) 를 preview API 호출 전에 추가. 통합 테스트 fixture(`pilotPageFlows.test.jsx:4198` `new File(["data"], "bank.xlsx", {...})`)는 비-OOXML(`PK\x03\x04` 시그니처 없음) → 신규 검증이 fail-closed 로 차단 → `POST /api/v1/billing/imports/bank-deposits/preview` **미호출**.
- **증상**: `AssertionError: expected "vi.fn()" to be called with .../bank-deposits/preview` (실제 호출: `/formats`·`/claims`·`/cms/enrollments`).
- **COD 조치**: `src/frontend@develop` 에서 US-L01 fixture 를 유효 OOXML payload 로 정정(`BankDepositImportPanel.test.jsx` 패턴 참조), 단건 + full-suite PASS 후 커밋 → TSR develop→test FF 재검증.
- **prevention**: pre-upload magic-byte 강화 시 panel 단건 test 뿐 아니라 pilot/통합 fixture 도 동기화. 회귀 lock 커밋은 push 전 full-suite `npm test` 1회 실행.

## 브랜치 상태
- FE develop `51a3db4` / test `51a3db4` (local SYNCED·WT CLEAN) · origin/test `b23711f` (local +5, 미푸시)
- BE develop/test `2c102e5` (SYNCED·Open 0) · origin/test `598d108` (751 pending push=QA-B116)

## 후속
- **선행**: QA-B609(COD FE fixture) → QA-B116(751 BE origin/test push) → QA-B95(operation 승격)
