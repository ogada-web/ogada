<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-07-18T11:15:00Z -->
# frontend develop→test 이관 패키지 — TSR1844 (2026-07-18)

## 요약
- **merge**: develop→test **FF** `0d37788`→`93f4932` (pending **1→0**)
- **post-merge full suite** `npm test`: **2751/2751 PASS** (894.42s · 488 test files · 0 FAIL)
- **targeted** `TransportRunNewPage.test.jsx`: full suite에 포함·PASS (peer `vitest run` PID1203049 lock 로 별도 재실행 생략 — 경쟁 실행 금지)
- **build** `npm run build`: **1234 modules PASS** (10.79s)
- **audit** `npm audit --audit-level=high`: **0 vulnerabilities**
- **verdict**: **PASS** — Open(FE) **0**

## 이번 FF 이관 커밋 (1)
| SHA | 종류 | 요약 |
|-----|------|------|
| `93f4932` | **제품**(fix) | id=2 transport — 이전 운행 불러오기 시 남아있던 회차(round) 검증 오류를 초기화하여 로드된 데이터와 회차 필드 a11y 상태·표시 오류를 정합화 + 회귀 test |

## 이번 커밋 diffstat (`0d37788..93f4932`)
```
 src/pages/TransportRunNewPage.jsx      | 31 +++++++++-------
 src/pages/TransportRunNewPage.test.jsx | 66 ++++++++++++++++++++++++++++++++++
 2 files changed, 84 insertions(+), 13 deletions(-)
```

## 누적 diffstat (`b23711f..93f4932` · origin/test 대비 +11)
```
 src/components/ui/BankDepositImportPanel.jsx             |  13 +-
 src/components/ui/BankDepositImportPanel.test.jsx        |  33 ++++-
 src/components/visits/VisitRfidDiffComparePanel.test.jsx |  31 +++++
 src/config/excelImportFiles.js                          |  36 +++++-
 src/config/excelImportFiles.test.js                     |  75 +++++++++++
 src/config/transport.js                                 |  13 ++
 src/config/transport.test.js                            |  19 +++
 src/pages/NHISImportPage.test.jsx                       |  34 +++++
 src/pages/TransportRunDetailPage.jsx                    |  15 ++-
 src/pages/TransportRunNewPage.jsx                       |  60 +++++++--
 src/pages/TransportRunNewPage.test.jsx                  | 142 +++++++++++++++++++++
 src/pages/pilotPageFlows.test.jsx                       |  10 +-
 src/styles/components.css                               |   2 +-
 src/styles/printStylesheet.test.js                      |  43 +++++++
 14 files changed, 494 insertions(+), 32 deletions(-)
```

## 검증 (TSR1844 post-merge)
- **product code**: `TransportRunNewPage` — 이전 운행 불러오기(load prior run)가 현재 회차 상태를 end-to-end 로 교체하도록 수정. 이전 검증 오류(`departureRound` error·aria-invalid/role=alert)가 로드 후에도 남던 문제 해소. 서버 계약(`departureRound @Min(1)`) 정합 불변.
- **회귀 없음**: 전체 스위트 2751/2751 PASS (직전 TSR1840 `@f72af3f` 2747 → +4 test 순증: `0d37788` route-stop limit + `93f4932` stale round error clear).
- **Open(FE)**: 0

## 브랜치 상태
- FE develop/test **SYNCED `@93f4932`** · WT CLEAN · origin/test `b23711f` (local **+11** · 미푸시)
- BE develop/test **SYNCED `@b8facfc`** · Open(BE) **0** · origin/test `598d108` (**757** pending push = QA-B116)

## 후속
- **Planned**: QA-B116(757 BE + 11 FE origin/test push) → QA-B95(operation 승격·live E2E bootstrap)
- **operation BLOCK**: QA-B116(push) + QA-B95(live bootstrap)
