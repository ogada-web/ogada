# develop-test-diff-20260718-TSR1858 (frontend)

**TSR**: TSR1858 | **stream**: frontend | **date**: 2026-07-18 | **merge**: FF `b115ae0`→`5aaee88` (pending **2→0**)

## Merged commits (develop → test)

| sha | subject |
|-----|---------|
| `eca424f` | fix(a11y/transport): route server departureRound field error to field only (UXD-194) |
| `5aaee88` | fix(v1.2.1/transport): blur departure-round input on wheel to prevent silent value change (id=2 form polish) |

## Changed files (aggregate)

| file | +/- |
|------|-----|
| `src/pages/TransportRunNewPage.jsx` | +12 / -2 |
| `src/pages/TransportRunNewPage.test.jsx` | +34 / -2 |

## Commit summaries

### `eca424f` — fix(a11y/transport): route server departureRound field error to field only (UXD-194)

- `TransportRunNewPage.jsx` +6/-1: 서버 `departureRound` 필드 오류를 필드 단위로 라우팅 (UXD-194 a11y)
- `TransportRunNewPage.test.jsx` +2: 필드 오류 라우팅 회귀 테스트 추가

### `5aaee88` — fix(v1.2.1/transport): blur departure-round input on wheel to prevent silent value change (id=2 form polish)

- `TransportRunNewPage.jsx` +6: `<input type="number">` 에 `onWheel` 핸들러 추가 → 포커스 상태 마우스 휠이 회차 값을 조용히 바꾸는 데이터 무결성 문제를 `event.currentTarget.blur()`로 차단(스크롤 페이지로 넘김)
- `TransportRunNewPage.test.jsx` +32/-1: wheel blur 회귀 테스트 추가 (8→9 tests)

## QA results

| check | result |
|-------|--------|
| develop→test pending (after merge) | **0** (0/0) |
| FF-safe | ✅ merge-base == test HEAD (`b115ae0`) |
| targeted `TransportRunNewPage.test.jsx` | **9/9 PASS** (COD 1회 + TSR full suite) |
| full suite `npm test` | **2761/2761 PASS** (898.94s · 488 files · +1 vs TSR1856) |
| `npm run build` | **1234 modules PASS** (10.79s) |
| `npm audit --audit-level=high` | **0 vulnerabilities** |
| live E2E (결정 96) | **SKIP** (QA-B95 bootstrap-disabled carry) |
| develop/test HEAD | **SYNCED `@5aaee88`** · WT CLEAN |
| Open(FE) | **0** |
| origin/test push | SKIP — +18 local pending (Planned QA-B116) |

## Transfer verdict

**PASS (FE local)** — develop/test SYNCED `@5aaee88` · pending 0 · full suite 2761/2761 green · build 1234 · audit high 0

## Cross-stream / Operation

- BE develop `@417e2ff` / test `@4dcf60d` pending 1 → **QA-20260718-B614 Open(HIGH/BLOCK)** (COD develop→test FF 대기)
- operation: **BLOCK** (761 BE + 18 FE origin/test push=QA-B116 + QA-B95 live bootstrap)
