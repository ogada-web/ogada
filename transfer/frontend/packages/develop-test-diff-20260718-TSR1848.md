<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-07-18T12:40:00Z -->
# FE develop→test diff — TSR1848 (2026-07-18)

## 요약
- **merge**: develop→test **FF** `23b47ea`→`af1d4f6` (pending **1→0**)
- **commit**: `af1d4f6` `fix(v1.2.1/transport): focus departure-round field when dispatch save is blocked (id=2 form polish)`
- **성격**: 접근성(WCAG 2.4.3 Focus Order / 3.3.1 Error Identification) 개선 — 회차(`departureRound`) 검증 실패 시 키보드·스크린리더 포커스를 회차 입력 필드로 이동. 신규 엔드포인트·라우트·상태 로직 변경 없음(behavior additive: 포커스 이동만 추가).

## 변경 파일
```
 src/pages/TransportRunNewPage.jsx      | 7 ++++++-
 src/pages/TransportRunNewPage.test.jsx | 2 ++
 2 files changed, 8 insertions(+), 1 deletion(-)
```

- `TransportRunNewPage.jsx`: `useRef`로 `roundInputRef` 추가, 회차 input 에 `ref` 연결. `handleSaveDraft` 의 FE `parseDepartureRoundInput` 사전 검증 실패 분기 + BE `fieldErrors.departureRound` 응답 분기 양쪽에서 `roundInputRef.current?.focus()` 호출.
- `TransportRunNewPage.test.jsx`: 기존 회차 오류 회귀 테스트 2건에 `toHaveFocus()` 단언 추가(신규 테스트 케이스 아님 → 테스트 수 불변 2755).

## 검증 결과 (`src/frontend-test @af1d4f6`)
| 항목 | 결과 |
|------|------|
| full suite `npm test` | **2755/2755 PASS** (488 files · 892.80s · 0 FAIL) |
| `npm run build` | **1234 modules PASS** (9.27s) |
| `npm audit --audit-level=high` | **0 vulnerabilities** |
| live E2E (post-merge·결정 96) | **SKIP** — backend UP(`/api/v1/health`=200)이나 `liveE2eBootstrapEnabled=false` → seed/login 불가 = **QA-B95** |
| develop/test | **SYNCED `@af1d4f6`** · WT CLEAN · pending 0 |

## 잔여 리스크
- **QA-B116**: FE local `test` origin/test(`b23711f`) 대비 **+13**, BE local `test` origin/test(`598d108`) 대비 **+759** 미push → operation 승격 전 push 필요(tester/merge 스크립트 전담).
- **QA-B95**: live E2E bootstrap 비활성(`OGADA_LIVE_E2E_BOOTSTRAP_ENABLED` 미설정) → post-merge live E2E 미실행. ops 환경변수 선결 필요.
