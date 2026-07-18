<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-07-18T13:24:00Z -->
# FE develop→test diff — TSR1852 (2026-07-18) · id=2 transport departure-round exponent/hex reject MERGED

## 요약
- **성격**: develop→test FF merge — TSR1850(no-op) 이후 `develop` 신규 커밋 **1**.
- **merge**: FF `af1d4f6`→`d6f3889` (pending **1→0**, FF-safe: merge-base==test HEAD).
- **develop / test / origin-develop**: **SYNCED `@d6f3889`** · WT CLEAN.
- **develop→test pending**: **0** (`git rev-list --left-right develop...test` = `0  0`).

## 이관 커밋
- `d6f3889` `fix(v1.2.1/transport): reject exponent/hex departure-round input (id=2 form polish)`
  - `parseDepartureRoundInput()` 이 `Number()` 관용 변환으로 `"1e2"→100`, `"0x1f"→31` 처럼 지수/16진 표기를 조용히 큰 회차로 왕복 → `type=number` 필드가 지수 표기를 허용하므로 오타(`1e2`)가 인라인 검증을 우회하고 100 회차를 배차. 순수 10진 정수(`/^\d+$/`)만 허용해 FE 의도와 BE `@Min(1) Integer` 계약을 일치.
  - 변경 파일: `src/config/transport.js` (+9/-1), `src/config/transport.test.js` (+11) — 지수/16진/부호 표기 신규 거부 회귀 테스트.
  - 제품 로직 변경(검증 강화) + 회귀 테스트 동반.

## 검증 (src/frontend-test @ test `d6f3889`)
| 항목 | 결과 |
|------|------|
| develop→test FF merge | **PASS** — `af1d4f6`→`d6f3889` (pending 1→0) |
| targeted `src/config/transport.test.js` | **PASS 10/10** (1.01s) |
| full suite `npm test` | **PASS 2756/2756** (905.24s · 488 files · +1 vs TSR1848 2755 = 신규 회귀 테스트) |
| `npm run build` | **1234 modules PASS** (10.71s) |
| `npm audit --audit-level=high` | **0 vulnerabilities** |
| live E2E (결정 96) | **SKIP** — backend UP(`/api/v1/health`=200) but `liveE2eBootstrapEnabled=false`=QA-B95 |

## 상태
- Open(FE): **0** (신규 Open 없음).
- transfer: **PASS** (FE local SYNCED · pending 0 · full suite green).
- cross-stream: **SYNCED local** (FE `@d6f3889` + BE `@5df9999` develop/test SYNCED · both Open 0).
- operation: **BLOCK** — origin/test push 759 BE + 14 FE(QA-B116) · live-e2e bootstrap disabled(QA-B95).
