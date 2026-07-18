<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-07-18T20:40:00Z -->
# develop→test diff — TSR1869 (frontend · 2026-07-18)

## 요약

| 항목 | 값 |
|---|---|
| merge 범위 | `171075f`→`6c280d0` (FF, 1 commit) |
| 커밋 | `6c280d0` fix(v1.2.1/transport): clear stale fee records on rejected service-fee date range (G16 id=2 form polish) |
| 변경 파일 수 | 2 |
| 삽입 / 삭제 | +27 / -0 |

## 변경 파일 목록 (git diff --numstat 171075f..6c280d0)

| 파일 | +lines | -lines | 설명 |
|---|---|---|---|
| `src/components/transport/TransportServiceFeePanel.jsx` | +3 | 0 | 기간 사전 차단 분기에서 `setRecords([])` 추가 — 거부된 기간과 무관한 직전 유효 기간 청구 기록을 함께 비워 오류 배너와 어긋나는 stale 목록이 남지 않도록 함(정상 기간 load/generate 동작 불변) |
| `src/components/transport/TransportServiceFeePanel.test.jsx` | +24 | 0 | date-range 오류로 조회가 차단될 때 직전 기록이 사라지고 EmptyState("청구 기록 없음")로 전환되는지 검증하는 회귀 테스트 추가 |

## 커밋 상세

```
commit 6c280d08aa0732f51d3ae37aa6edc00bb649dbea
Author: jwj3400 <rlwlsdnr@naver.com>
Date:   Sat Jul 18 20:23:09 2026 +0000

fix(v1.2.1/transport): clear stale fee records on rejected service-fee date range (G16 id=2 form polish)

TransportServiceFeePanel.load cleared only success/skipped banners when
pre-blocking an empty/reversed query range but left the previous valid
range's records mounted, so a stale fee list lingered contradicting the
error banner. Clear records in the pre-block branch so the table falls
back to EmptyState (valid-range load/generate unchanged; extends the
9b0481d stale-banner-clear lineage).

Co-authored-by: Cursor <cursoragent@cursor.com>
```

## 검증 결과 (TSR1869)

- **full suite**: 2769/2769 PASS (488 files · 900.28s) · +1 vs TSR1867 2768 (신규 stale-records clear 회귀 테스트 +1) — src/frontend-test `@6c280d0`
- **build**: 1234 modules PASS (10.91s)
- **audit high**: 0 vulnerabilities
- **live E2E**: SKIP (QA-B95 carry: bootstrap disabled · backend `/health=200` UP 이나 `liveE2eBootstrapEnabled=false`)
- **FF-safe**: merge-base(`171075f`) == test HEAD → 순수 fast-forward, 충돌 없음
- **verdict**: PASS (FE local transfer) · develop/test SYNCED `@6c280d0` · Open(FE) 0
