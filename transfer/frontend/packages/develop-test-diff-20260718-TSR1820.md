<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-07-18T02:10:00Z -->
# frontend develop→test diff — TSR1820 (QA-B606 Fixed & Verified·merge+PUSH)

- stream: **frontend**
- merge: FF `1cdfd5c` → `637bad8` (pending 1→0)
- develop / test / origin: **ALL SYNCED+PUSHED `@637bad8`**
- qa: **QA-20260718-B606 Fixed & Verified** (form-data 4.0.5→4.0.6·npm audit high 1→0) · Open(FE) **0**
- verified_at: 2026-07-18T02:10:00Z

## merge range (`1cdfd5c..637bad8`)

```
637bad8 fix(v1.2.1/QA-B606): bump form-data to 4.0.6 to clear npm audit high
```

## diff stat

```
 package-lock.json | 10 +++++-----
 1 file changed, 5 insertions(+), 5 deletions(-)
```

## verification (src/frontend-test @637bad8)

| item | result |
|------|--------|
| pre-merge `npm audit` high | 1 (form-data 4.0.5 CRLF·GHSA-hmw2-7cc7-3qxx) |
| post-merge `npm audit` high | **0** (0 vulnerabilities) — QA-B606 해소 확정 |
| `npm ls form-data` (after install) | **4.0.6** (jsdom@22.1.0 → form-data 4.0.6) |
| `npm run build` | **1234 modules PASS** (10.67s) |
| full suite `npm test` | **carry 2735/2735 PASS @1cdfd5c** (TSR1817·883.72s,487) — 제품/테스트 코드 byte-identical(merge=package-lock only) |
| origin/test push | PASS `1cdfd5c..637bad8` |
| live E2E | **SKIP** — 아래 note 참조 |

## notes
- QA-B606 fix(`637bad8`): `npm audit fix` 로 `form-data 4.0.5 → 4.0.6`(GHSA-hmw2-7cc7-3qxx CRLF injection) 상향. 변경은 `package-lock.json` 1건(+5/-5)뿐 · jsdom major 불변 · 제품/테스트 코드 무변경.
- 의존 경로 `ogada-frontend → jsdom@22.1.0 → form-data` = **devDependency 전용**(vitest jsdom 테스트 환경) · 프로덕션 Vite 번들 미포함 → 런타임 노출 0. 원래 severity LOW(non-BLOCK) 였으나 이번 사이클로 완전 해소.
- **full suite carry 근거**: 이번 merge diff 는 `package-lock.json` 1건뿐(product/test 소스 0 변경) → TSR1817 `@1cdfd5c` full suite 2735/2735 PASS 가 그대로 유효. 재실행 대신 carry.
- **live E2E SKIP 근거**: (1) `scripts/run-live-e2e.sh` 는 `cd src/frontend`(coder develop worktree) 에서 vitest 실행 — 실행 시점 해당 디렉토리에 **coder vitest run 진행 중**(01:53~) → `docs/qa/VITEST_CONCURRENCY.md` 위반 회피. (2) 본 merge 는 devDependency(form-data) bump 로 route/API/component **런타임 영향 0** → live E2E 재검증 무의미.
- cross-stream: FE ALL SYNCED+PUSHED `@637bad8`(Open 0) · BE develop/test local SYNCED `@efbdbec`(Open 0) 이나 `origin/test`=`598d108`(**746 pending push · QA-B116**) → operation BLOCK 잔존.
