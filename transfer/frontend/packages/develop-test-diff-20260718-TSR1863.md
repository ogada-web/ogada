<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-07-18T17:53:00Z -->

# FE develop→test diff — TSR1863 (2026-07-18)

## 요약
- **merge**: FF `9f12482`→`9b0481d` (pending **1→0** · FF-safe: merge-base==test HEAD `9f12482`)
- **commit**: `9b0481d` fix(v1.2.1/transport): clear stale generate banners on service-fee reload (id=2 form polish)
- **stream**: frontend · **verdict**: PASS (FE local)

## 커밋 요지 (`9b0481d`)
G16 `TransportServiceFeePanel.load()` 가 기존에는 `error` 만 비우고 생성 성공 배너(`success`)와 건너뜀 목록(`skipped`)은 그대로 남겨, 청구 기록 생성 후 기간 변경/`조회` 시 직전 결과 배너가 stale 하게 남는 문제를 수정. `load()` 가 `success`/`skipped` 도 함께 비우고, `handleGenerate`/`handleConfirm` 은 `load()` 이후 성공 배너를 재설정해 **최신 결과만 노출**되도록 정리.

## 변경 파일
```
 src/components/transport/TransportServiceFeePanel.jsx      | 10 ++++++--
 src/components/transport/TransportServiceFeePanel.test.jsx | 30 ++++++++++++++++++++++
 2 files changed, 38 insertions(+), 2 deletions(-)
```
- product code: `TransportServiceFeePanel.jsx` +10/-2 (load stale-banner clear + 핸들러 배너 재설정 순서 조정 · 기존 유효 동작 불변)
- test: `TransportServiceFeePanel.test.jsx` +30 (신규 `@Test` 1건 — `조회` 시 stale generate success/skipped 배너 제거 회귀)

## 검증
| gate | result |
|------|--------|
| full suite `npm test` | **2763/2763 PASS** (488 files · 893.80s · +1 vs TSR1860 2762) |
| targeted `TransportServiceFeePanel.test.jsx` | **PASS** (full suite 내 488 files 전수 green 포함) |
| `npm run build` | **PASS** (1234 modules · 10.63s) |
| `npm audit --audit-level=high` | **PASS** (0 vulnerabilities) |
| live E2E (결정 96) | **SKIP** (QA-B95 carry: backend UP `/api/v1/health`=200 이나 `liveE2eBootstrapEnabled=false`) |
| develop / test | **SYNCED `@9b0481d`** WT CLEAN |
| Open(FE) | **0** |

## cross-stream
- BE develop/test **SYNCED `@6329323`** · Open(BE) 0
- FE develop/test **SYNCED `@9b0481d`** · Open(FE) 0
- operation **BLOCK**: origin/test push 미실행 (764 BE + 20 FE = QA-B116) + live bootstrap disabled (QA-B95)
