<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-07-18T11:56:00Z -->
# frontend develop→test 이관 패키지 — TSR1846 (2026-07-18)

## 요약
- **merge**: develop→test **FF** `93f4932`→`23b47ea` (pending **1→0**)
- **post-merge full suite** `npm test`: **2755/2755 PASS** (893.05s · 488 test files · 0 FAIL · 직전 TSR1844 2751 → +4)
- **build** `npm run build`: **1234 modules PASS** (9.28s)
- **audit** `npm audit --audit-level=high`: **0 vulnerabilities**
- **live E2E**: **SKIP** — backend `localhost:8080` **UP**(`/api/v1/health`=200)이나 `probe.bootstrapEnabled=false`(`detail=bootstrap=disabled`) → seed/login 불가 = **QA-B95** carry
- **verdict**: **PASS** — Open(FE) **0**

## 이번 FF 이관 커밋 (1)
| SHA | 종류 | 요약 |
|-----|------|------|
| `23b47ea` | **refactor**(제품·동작 불변) | id=2 transport — 인라인 회차(departureRound) 검증 로직을 `TransportRunNewPage`에서 `config/transport.js`의 `parseDepartureRoundInput` + `DEPARTURE_ROUND_INVALID_MESSAGE`로 추출. 중복 `Number()` 변환·페이지 로컬 메시지 상수 제거, BE `@Min(1) Integer departureRound` 제약과 verbatim 정합 유지. 동작 중립 + config 단위 테스트 추가 |

## 이번 커밋 diffstat (`93f4932..23b47ea`)
```
 src/config/transport.js           | 28 ++++++++++++++++++++++++++++
 src/config/transport.test.js      | 34 +++++++++++++++++++++++++++++++++-
 src/pages/TransportRunNewPage.jsx | 16 ++++++----------
 3 files changed, 67 insertions(+), 11 deletions(-)
```

## 누적 diffstat (`b23711f..23b47ea` · origin/test 대비 +12 commit)
```
 src/components/ui/BankDepositImportPanel.jsx       |  13 +-
 src/components/ui/BankDepositImportPanel.test.jsx  |  33 ++++-
 .../visits/VisitRfidDiffComparePanel.test.jsx      |  31 +++++
 src/config/excelImportFiles.js                     |  36 +++++-
 src/config/excelImportFiles.test.js                |  75 +++++++++++
 src/config/transport.js                            |  41 ++++++
 src/config/transport.test.js                       |  53 +++++++-
 src/pages/NHISImportPage.test.jsx                  |  34 +++++
 src/pages/TransportRunDetailPage.jsx               |  15 ++-
 src/pages/TransportRunNewPage.jsx                  |  56 ++++++--
 src/pages/TransportRunNewPage.test.jsx             | 142 +++++++++++++++++++++
 src/pages/pilotPageFlows.test.jsx                  |  10 +-
 src/styles/components.css                          |   2 +-
 src/styles/printStylesheet.test.js                 |  43 +++++++
 14 files changed, 551 insertions(+), 33 deletions(-)
```

## 검증 (TSR1846 post-merge)
- **product code**: `TransportRunNewPage.jsx` — 회차 검증 인라인 로직을 `parseDepartureRoundInput(rawValue)` 헬퍼로 위임(빈 값→`{ok:true,value:null}`, 1 이상 정수→`{ok:true,value}`, 그 외→`{ok:false,error:DEPARTURE_ROUND_INVALID_MESSAGE}`). 메시지·검증 규칙·서버 계약(`@Min(1)`) 불변 → **동작 중립 refactor**.
- **회귀 없음**: 전체 스위트 **2755/2755 PASS**(직전 TSR1844 `@93f4932` 2751 → +4: `config/transport.test.js` `parseDepartureRoundInput` 단위 테스트 순증).
- **Open(FE)**: 0

## 브랜치 상태
- FE develop/test **SYNCED `@23b47ea`** · WT CLEAN · origin/test `b23711f` (local **+12** · 미푸시)
- BE develop/test **SYNCED `@b8facfc`** · Open(BE) **1**(QA-B613 MEDIUM·미커밋 test) · origin/test `598d108` (**757** pending push = QA-B116)

## 후속
- **Planned**: QA-B116(757 BE + 12 FE origin/test push) → QA-B95(operation 승격·live E2E bootstrap: `OGADA_LIVE_E2E_BOOTSTRAP_ENABLED=true`)
- **operation BLOCK**: QA-B116(push) + QA-B95(live bootstrap disabled)
