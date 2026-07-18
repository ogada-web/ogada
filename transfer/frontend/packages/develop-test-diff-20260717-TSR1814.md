<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-07-17T23:52:00Z -->
# frontend develop→test diff — TSR1814 (QA-B602 Fixed·merge+PUSH)

- stream: **frontend**
- merge: FF `3042a53` → `7ac3c84` (pending 1→0)
- develop / test / origin: **ALL SYNCED+PUSHED `@7ac3c84`**
- qa: **QA-20260717-B602 Fixed** (page/pilot NHIS excel fixture OOXML magic sync) · **QA-20260717-B605 Open(LOW)** flaky
- verified_at: 2026-07-17T23:52:00Z

## merge range (`3042a53..7ac3c84`)

```
7ac3c84 test(v1.2.1/v3/QA-B602): sync page/pilot NHIS excel fixtures to OOXML magic bytes
```

## diff stat

```
 src/pages/StaffPage.test.jsx      | 2 +-
 src/pages/pilotPageFlows.test.jsx | 5 +++--
 2 files changed, 4 insertions(+), 3 deletions(-)
```

## verification (src/frontend-test @7ac3c84)

| item | result |
|------|--------|
| targeted StaffPage+pilot | **164/164 PASS** (61.38s, 2 files) |
| full suite `npm test` | **2734/2735 (1 FAIL)** (892.24s, 487 files) |
| full-suite FAIL | `VisitRfidDiffComparePanel.test.jsx:256` — flaky (isolated **10/10 PASS** 5.05s) → QA-B605 LOW |
| origin/test push | PASS `3042a53..7ac3c84` |
| live E2E | SKIP (concurrent vitest lock — another agent full suite @23:50) |
| backend@8080 | UP/200 |

## notes
- 제품 코드 무변경 — 테스트 fixture만 OOXML magic bytes(`[0x50,0x4b,0x03,0x04,…]`)로 동기화.
- QA-B602 이전 2 FAIL(StaffPage caregiver import·pilot US-V04) → 모두 PASS.
- 남은 1 FAIL 은 full-suite 병렬 부하 하 flaky (isolated PASS) — 병합 회귀 아님.
