<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-07-18T20:05:00Z -->
# develop→test diff — TSR1867 (frontend · 2026-07-18)

## 요약

| 항목 | 값 |
|---|---|
| merge 범위 | `3b903c8`→`171075f` (FF, 1 commit) |
| 커밋 | `171075f` fix(v1.2.1/transport): reject missing service-fee date range before API round-trip (G16 id=2 form polish) |
| 변경 파일 수 | 4 |
| 삽입 / 삭제 | +112 / -10 |

## 변경 파일 목록 (git diff --numstat 3b903c8..171075f)

| 파일 | +lines | -lines | 설명 |
|---|---|---|---|
| `src/components/transport/TransportServiceFeePanel.jsx` | +9 | -8 | FE 사전 차단 — `resolveTransportServiceFeeDateRangeError` 단일 진입점으로 `load`/`handleGenerate` 가드 통일(빈/역방향 기간 즉시 에러·서버 왕복 skip) |
| `src/components/transport/TransportServiceFeePanel.test.jsx` | +32 | -1 | 빈 기간(시작일/종료일 누락) 차단 통합 테스트 추가 |
| `src/config/transportServiceFee.js` | +40 | -1 | `isTransportServiceFeeDateRangePresent` 헬퍼·`TRANSPORT_SERVICE_FEE_DATE_RANGE_REQUIRED_MESSAGE` 상수·`resolveTransportServiceFeeDateRangeError`(필수→순서 단일 진입점) 추가 |
| `src/config/transportServiceFee.test.js` | +31 | 0 | 필수 검사·단일 진입점 BE validateDateRange lockstep 단위 테스트 추가 |

## 커밋 상세

```
commit 171075f21a043ed1693a233f833d075e0382d650
Author: jwj3400 <rlwlsdnr@naver.com>
Date:   Sat Jul 18 19:29:20 2026 +0000

fix(v1.2.1/transport): reject missing service-fee date range before API round-trip (G16 id=2 form polish)

TransportServiceFeePanel 조회/생성이 시작일 또는 종료일이 비어 있으면 서버에 보낸 뒤에야
BE 400 을 표면화하던 문제를 FE 에서 사전 차단한다. BE TransportServiceFeeService.validateDateRange
의 필수 검사 문구("조회 기간의 시작일과 종료일이 필요합니다.") verbatim lockstep +
isTransportServiceFeeDateRangePresent 헬퍼 및 resolveTransportServiceFeeDateRangeError(필수 → 순서)
단일 진입점을 추가하고 load/handleGenerate 가드를 이 진입점으로 통일했다. 정상 기간 동작은 불변.

Co-authored-by: Cursor <cursoragent@cursor.com>
```

## 검증 결과 (TSR1867)

- **full suite**: 2768/2768 PASS (488 files · 896.27s) · +3 vs TSR1865 2765
- **build**: 1234 modules PASS (9.41s)
- **audit high**: 0 vulnerabilities
- **live E2E**: SKIP (QA-B95 carry: bootstrap disabled · backend `/health=200` UP)
- **FF-safe**: merge-base(`3b903c8`) == test HEAD → 순수 fast-forward, 충돌 없음
- **verdict**: PASS (FE local transfer) · develop/test SYNCED `@171075f` · Open(FE) 0
