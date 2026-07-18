<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-07-18T09:19:23Z -->
# frontend develop→test 이관 패키지 — TSR1840 (2026-07-18)

## 요약
- **merge**: develop→test **FF** `5e816e6`→`f72af3f` (pending **1→0**)
- **post-merge full suite** `npm test`: **2747/2747 PASS** (893.26s · 488 test files · 0 FAIL)
- **targeted** `npm test -- src/pages/TransportRunNewPage.test.jsx`: **6/6 PASS** (6.47s)
- **build** `npm run build`: **1234 modules PASS** (9.27s)
- **audit** `npm audit --audit-level=high`: **0 vulnerabilities**
- **verdict**: **PASS** — Open(FE) **0**

## 이번 FF 이관 커밋 (1)
| SHA | 종류 | 요약 |
|-----|------|------|
| `f72af3f` | **제품**(fix) | id=2 transport form polish — `TransportRunNewPage` 회차(departureRound) 클라이언트 검증(1 이상 정수) + 서버 `fieldErrors.departureRound` 필드 단위 오류 표시 + 회귀 test 2건 |

## 이번 커밋 diffstat (`5e816e6..f72af3f`)
```
 src/pages/TransportRunNewPage.jsx      | 26 +++++++++++-
 src/pages/TransportRunNewPage.test.jsx | 76 ++++++++++++++++++++++++++++++++++
 2 files changed, 100 insertions(+), 2 deletions(-)
```

## 누적 diffstat (`b23711f..f72af3f` · origin/test 대비 +9)
```
 src/components/ui/BankDepositImportPanel.jsx       | 13 +++-
 src/components/ui/BankDepositImportPanel.test.jsx  | 33 ++++++++--
 src/components/visits/VisitRfidDiffComparePanel.test.jsx | 31 +++++++++
 src/config/excelImportFiles.js                     | 36 ++++++++--
 src/config/excelImportFiles.test.js                | 75 +++++++++++++++++++++
 src/pages/NHISImportPage.test.jsx                  | 34 ++++++++++
 src/pages/TransportRunNewPage.jsx                  | 26 +++++++-
 src/pages/TransportRunNewPage.test.jsx             | 76 ++++++++++++++++++++++
 src/pages/pilotPageFlows.test.jsx                  | 10 ++-
 src/styles/components.css                          |  2 +-
 src/styles/printStylesheet.test.js                 | 43 ++++++++++++
 11 files changed, 362 insertions(+), 17 deletions(-)
```

## 검증 (TSR1840 post-merge)
- **product code**: `TransportRunNewPage` — BE `CreateTransportRunRequest.departureRound @Min(1)` 계약과 정합. 0·음수·소수는 `createTransportRunApi` 호출 전 사전 차단, 서버 반환 `fieldErrors.departureRound` 는 회차 `Field` error + aria-invalid/role=alert 매핑. 빈 값(자동 배정) 동작 불변.
- **회귀 없음**: 전체 스위트 2747/2747 PASS (직전 TSR1838 `@5e816e6` 2745 → +2 test 순증)
- **Open(FE)**: 0

## 브랜치 상태
- FE develop/test/origin-develop **SYNCED `@f72af3f`** · WT CLEAN · origin/test `b23711f` (local **+9** · 미푸시)
- BE develop/test **SYNCED `@913b9d2`** · Open(BE) **0** · origin/test `598d108` (**755** pending push = QA-B116)

## 후속
- **Planned**: QA-B116(755 BE + 9 FE origin/test push) → QA-B95(operation 승격·live E2E bootstrap)
- **operation BLOCK**: QA-B116(push) + QA-B95(live bootstrap)
