<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-07-18T01:22:40Z -->
# frontend develop→test diff — TSR1817 (QA-B605 Fixed·merge+PUSH)

- stream: **frontend**
- merge: FF `7ac3c84` → `1cdfd5c` (pending 2→0)
- develop / test / origin: **ALL SYNCED+PUSHED `@1cdfd5c`**
- qa: **QA-20260717-B605 Fixed** (VisitRfidDiffComparePanel full-suite flaky 안정화) · Open(FE) **0**
- verified_at: 2026-07-18T01:22:40Z

## merge range (`7ac3c84..1cdfd5c`)

```
1cdfd5c test(v1.2.1/QA-B605): await async compare before dispatch button click
194823b ux(a11y): announce photo upload success to screen readers (UXD-191)
```

## diff stat

```
 src/components/clients/ClientPhotoUpload.jsx                | 6 ++++++
 src/components/clients/ClientPhotoUpload.test.jsx           | 3 +++
 src/components/programs/ProgramSchedulePhotoUpload.jsx      | 6 ++++++
 src/components/programs/ProgramSchedulePhotoUpload.test.jsx | 3 +++
 src/components/visits/VisitRfidDiffComparePanel.test.jsx    | 2 +-
 5 files changed, 19 insertions(+), 1 deletion(-)
```

## verification (src/frontend-test @1cdfd5c)

| item | result |
|------|--------|
| targeted (visit/client/program photo) | **17/17 PASS** (3 files, 8.82s) |
| full suite `npm test` | **2735/2735 PASS** (883.72s, 487 files) |
| QA-B605 flaky repro | **미재현** — `VisitRfidDiffComparePanel` full-suite 부하 하 통과 |
| origin/test push | PASS `7ac3c84..1cdfd5c` |
| live E2E | SKIP (merge post-merge full suite 내 liveBackendProbe fixture 경유·별도 실행 안 함) |

## notes
- QA-B605 fix(`1cdfd5c`): `VisitRfidDiffComparePanel.test.jsx` `reads snake_case dispatched_count` 케이스가 `uploadAndCompare()` 직후 async compare 완료 전 동기 `getByRole` 클릭 → 병렬 부하 시 버튼 미렌더 타임아웃 · `await screen.findByRole(...)` 로 전환. 제품 코드 무변경.
- UXD-191(`194823b`): `ClientPhotoUpload`/`ProgramSchedulePhotoUpload` 사진 업로드 성공을 스크린 리더에 announce (a11y) — 제품 코드 +6/+6, 테스트 +3/+3.
- 직전 TSR1814/1815 잔여 flaky(QA-B605 LOW)가 이번 full suite 2735/2735 PASS 로 해소 — 회귀 아님.
- cross-stream: BE `@f28e3d9` local test 병합 완료(Open 0) 이나 `origin/test`=`598d108` (**745 pending push · QA-B116**) → operation BLOCK 잔존.
