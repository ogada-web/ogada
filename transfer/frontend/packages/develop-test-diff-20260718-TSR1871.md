<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-07-18T22:18:00Z -->

# frontend develop→test FF merge diff — TSR1871 (`6c280d0`→`ab9ef17`)

- **stream**: frontend
- **merge**: FF `6c280d0` → `ab9ef17` (2 commits · pending 2→0)
- **merge-base**: `6c280d0` (== 이전 test HEAD) → FF-safe, 충돌 없음
- **post-merge**: develop = test = `ab9ef17` · WT CLEAN · pending 0

## Commits (2)

| sha | subject |
|-----|---------|
| `32b7ae3` | fix(a11y/transport): route service-fee date-range error to date fields (UXD-195) |
| `ab9ef17` | fix(a11y/transport): focus first invalid service-fee date field on blocked 조회/생성 (UXD-195 follow-up) |

## Diffstat (`6c280d0..ab9ef17`)

```
 .../transport/TransportServiceFeePanel.jsx         | 146 +++++++++++++--------
 .../transport/TransportServiceFeePanel.test.jsx    |  96 ++++++++++++++
 src/config/transportServiceFee.js                  |  25 ++++
 src/config/transportServiceFee.test.js             |  14 ++
 4 files changed, 229 insertions(+), 52 deletions(-)
```

## 성격 (UXD-195 a11y · id=2 form polish)

- `32b7ae3`: 이동서비스비 조회 기간(빈/역방향) 검증 오류를 상단 페이지 Alert 대신 **종료일 필드의 `role="alert"`(`#service-fee-to-error`)** 로 귀속. 두 날짜 필드에 `aria-invalid` + 시작일 `aria-describedby` 연결 추가, API 오류만 상단 Alert 유지 (WCAG 3.3.1·4.1.2 · §117·§118 필드 오류 라우팅 패턴).
- `ab9ef17`: 명시적 조회/생성이 기간 검증으로 차단될 때 **첫 위반 날짜 필드로 키보드 포커스 이동**. `resolveTransportServiceFeeDateRangeErrorField(from,to)` 헬퍼(필수→순서: 시작일 빈값→from, 종료일 빈값→to, 역방향→from) 추가 (WCAG 3.3.1).
- 정상 기간 조회/생성 동작 불변 · product code + 회귀 테스트만 변경 · behavior-neutral for valid ranges.

## 검증 (post-merge · `ab9ef17` · `src/frontend-test`)

- full suite `npm test`: **2773/2773 PASS** (488 files · 893.04s · +4 vs TSR1869 2769 · locked flock · EXIT 0)
- `npm run build`: **1234 modules PASS** (11.09s)
- `npm audit --audit-level=high`: **0 vulnerabilities** (high 0)
- live E2E (결정 96): **SKIP** (QA-B95 carry · backend `/health` UP 이나 `liveE2eBootstrapEnabled=false` · guardian bootstrap HTTP 500)
- Open(FE): **0** · transfer verdict **PASS** (FE local)
