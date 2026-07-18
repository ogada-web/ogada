<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-07-18T23:55:00Z -->
# develop→test diff · TSR1873 · 2026-07-18T23:55:00Z

## merge summary
- FF merge `ab9ef17`→`cf360d7` (pending **1→0**)
- 1 commit absorbed: `cf360d7`

## commit
- `cf360d7` fix(v1.2.1/care-reports): pre-block reversed date range before service-summary round-trip (L02_M12 form polish)

## diff stat (ab9ef17..cf360d7)
```
 src/config/careReports.js                   | 40 +++++++++++++++++++++++++++
 src/config/careReports.test.js              | 34 +++++++++++++++++++++++
 src/pages/ServiceSummaryReportPage.jsx      | 24 ++++++++++++++---
 src/pages/ServiceSummaryReportPage.test.jsx | 42 +++++++++++++++++++++++++++++
 4 files changed, 137 insertions(+), 3 deletions(-)
```

## test results
- full suite: **2778/2778 PASS** (892.51s · 489 files · +5 vs TSR1871 2773)
- build: **1234 modules** (9.31s/9.44s)
- audit high: **0**
- live E2E: **SKIP** (QA-B95 carry: `liveE2eBootstrapEnabled=false`)

## context
`ServiceSummaryReportPage` (L02_M12 급여제공 서비스 집계 리포트) 가 역방향 조회 기간(시작일 > 종료일)을 BE `CareReportService.resolveDateWindow` 에 보낸 뒤 400(`"종료일은 시작일 이후여야 합니다."`) 을 사후 표면화하던 문제를 FE 에서 사전 차단. 공용 헬퍼 `resolveCareReportDateRangeError` + `CARE_REPORT_DATE_RANGE_INVALID_MESSAGE`(BE 문구 verbatim lockstep)를 `src/config/careReports.js` 에 추가하고 load 가드에 연결 — 역방향이면 왕복 없이 종료일 필드에 오류 노출(`role="alert"` + `aria-invalid`) · stale 집계 제거. 결측값은 BE 기본 기간 대체이므로 사전 차단 대상 아님. id=2 form polish 계보(TransportServiceFeePanel 동일 패턴).

신규 테스트: `src/config/careReports.test.js` +34(4케이스 config 단위) + `src/pages/ServiceSummaryReportPage.test.jsx` +42(1케이스 역방향 차단 회귀).
