# 과거 문서와 조사 출처

현재 정책은 루트 README의 현재 문서와 실제 코드가 기준입니다. 정리 전 루트 커밋은 `e66e75f`입니다. 필요한 과거 원문은 Git에서 파일별로 읽고 전체 워크스페이스를 과거 상태로 되돌리지 않습니다.

```bash
git show e66e75f:docs/planning/research/BENCHMARK_REPORT.md > /tmp/ogada-old-benchmark.md
git show e66e75f:docs/ops/DATA_RETENTION_POLICY.md > /tmp/ogada-old-retention.md
```

| 코드의 과거 근거 | BENCHMARK_REPORT.md 원문 위치 |
|---|---|
| `feeSchedules.js` | §4-1 |
| `transportForm18.js` | §10-3·§12 |
| `bankDepositFormats.js` | §49 |
| `transportCompliance.js` | §4255–4265 |
| `feeSurchargeRates.js` | §354–364·§6142–6151 |

이는 조사 이력을 찾는 안내이며 상수를 최신 법령·요율로 검증했다는 의미가 아닙니다. 업무 규칙 변경 시 실제 적용 근거를 확인합니다.

미커밋 조사 자료와 로컬 루프 로그는 정리 전에 `.venv/cleanup-backup/20261010T181108Z`에 비공개 패치·파일로 보존했습니다. 비공개 설정·미리보기 DB·백업과 앱 기능은 문서 정리 대상이 아닙니다.
