<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-07-18T19:35:00Z -->
# develop→test diff — TSR1865 (frontend · 2026-07-18)

## 요약

| 항목 | 값 |
|---|---|
| merge 범위 | `9b0481d`→`3b903c8` (FF, 1 commit) |
| 커밋 | `3b903c8` fix(v1.2.1/transport): reject reversed service-fee date range before API round-trip (G16 id=2 form polish) |
| 변경 파일 수 | 4 |
| 삽입 / 삭제 | +104 / -5 |

## 변경 파일 목록

| 파일 | +lines | -lines | 설명 |
|---|---|---|---|
| `src/components/transport/TransportServiceFeePanel.jsx` | +22 | -2 | FE 사전 차단 — 역방향 기간 즉시 에러 표시, 서버 왕복 건너뜀 |
| `src/components/transport/TransportServiceFeePanel.test.jsx` | +46 | -1 | 역방향 기간 차단 통합 테스트 추가 |
| `src/config/transportServiceFee.js` | +26 | 0 | `isTransportServiceFeeDateRangeInOrder` 함수·상수 추가 |
| `src/config/transportServiceFee.test.js` | +15 | 0 | BE validateDateRange lockstep 단위 테스트 추가 |

## 커밋 상세

```
commit 3b903c8e8041e92af1109cda9ee55f9dfae2a2b6
Author: jwj3400 <rlwlsdnr@naver.com>
Date:   Sat Jul 18 18:23:27 2026 +0000

fix(v1.2.1/transport): reject reversed service-fee date range before API round-trip (G16 id=2 form polish)

TransportServiceFeePanel 조회/생성이 시작일>종료일 역방향 기간을 서버에
보낸 뒤에야 BE 400 을 표면화하던 문제를 사전 차단한다. FE 에서
isTransportServiceFeeDateRangeInOrder 로 검사해 BE
TransportServiceFeeService.validateDateRange 와 동일한 문구
("시작일은 종료일보다 이후일 수 없습니다.")를 즉시 노출하고 목록/생성 왕복을 건너뛴다.

Co-authored-by: Cursor <cursoragent@cursor.com>
```

## 검증 결과 (TSR1865)

- **full suite**: 2765/2765 PASS (488 files · 890.96s) · +2 vs TSR1863
- **build**: 1234 modules PASS (11.04s)
- **audit high**: 0 vulnerabilities
- **live E2E**: SKIP (QA-B95 carry: bootstrap disabled)
