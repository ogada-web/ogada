# develop-test-diff-20260718-TSR1860 (frontend)

**TSR**: TSR1860 | **stream**: frontend | **date**: 2026-07-18 | **merge**: FF `5aaee88`→`9f12482` (pending **1→0**)

## Merged commits (develop → test)

| sha | subject |
|-----|---------|
| `9f12482` | fix(v1.2.1/transport): normalize client list payload for service-fee panel |

## Changed files (aggregate)

| file | +/- |
|------|-----|
| `src/components/transport/TransportServiceFeePanel.jsx` | +10 / -2 |
| `src/components/transport/TransportServiceFeePanel.test.jsx` | +18 / -3 |

## Commit summaries

### `9f12482` — fix(v1.2.1/transport): normalize client list payload for service-fee panel

- `TransportServiceFeePanel.jsx` +10/-2: `fetchClientsApi` 응답이 배열 또는 `{ items: [...] }` paginated shape 모두에서 client 목록을 정규화해 G16 이동서비스비 기록의 client name 매핑이 깨지지 않도록 수정
- `TransportServiceFeePanel.test.jsx` +18/-3: paginated payload 회귀 테스트 추가 (7 tests)

## QA results

| check | result |
|-------|--------|
| develop→test pending (after merge) | **0** (0/0) |
| FF-safe | ✅ merge-base == test HEAD (`5aaee88`) |
| targeted `TransportServiceFeePanel.test.jsx` | **7/7 PASS** |
| full suite `npm test` | **2762/2762 PASS** (897.38s · 488 files · +1 vs TSR1858) |
| `npm run build` | **1234 modules PASS** (9.66s) |
| `npm audit --audit-level=high` | **0 vulnerabilities** |
| live E2E (결정 96) | **SKIP** — QA-B95 carry(bootstrap-disabled) |
| Open(FE) | **0** |
| transfer verdict | **PASS** (FE local) |
| cross-stream | **SYNCED local** (BE `@13eb863` + FE `@9f12482` develop/test SYNCED · both Open 0) |
| operation | **BLOCK** (763 BE + 19 FE origin/test push=QA-B116 + QA-B95) |
