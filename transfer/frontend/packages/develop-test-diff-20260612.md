<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-13T00:09:15+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-12 492차)

> test `@c7c8f07` 불변 · develop `@e76ca06` HEAD **불변** (490차 대비) · WT **CLEAN** · **Open 0(frontend)** · merge pending **370** (203 FE + 167 BE) · **양 스트림 merge BLOCK**(BE WT dirty·QA-B61)

| 항목 | 값 |
|------|-----|
| test HEAD | `c7c8f07` |
| develop HEAD | `e76ca06` |
| ahead | 203 |
| diff stat | 358 files, +45933 / -1262 (HEAD 기준) |
| test npm test | 217/217 PASS (120.35s) |
| develop HEAD npm test | **908/908 PASS** (205 files, 269.35s, +8 @Test vs 488차 900) |
| test build | 781 modules (max 367.09 kB, 14.25s) |
| develop HEAD build | **908 modules** (index 519.05 kB >500 kB vite warn, 6.06s) |
| audit | 0 (prod omit=dev) |
| routes | 63 route |
| origin/develop | @ `e76ca06` (동기화) |
| merge gate (frontend) | **FULLY UNBLOCKED** (WT CLEAN · Open 0) |
| cross-stream merge | **BLOCK** (BE @ `d4ee057` WT **DIRTY 2M** · Open 1 BLOCK QA-B61) |

### TSR 492차 vs 490차

| 항목 | 490차 | 492차 |
|------|-------|-------|
| develop HEAD | `e76ca06` | `e76ca06` (불변) |
| develop HEAD npm test | 미재실행 | **908/908 PASS** |
| develop HEAD build | 미재실행 | **908 modules** |
| cross-stream merge | FULLY UNBLOCKED (오판) | **BLOCK** (491차 BE QA-B61 반영) |

### TSR 492차 판정

- **PASS(v1.2+v1.3-A @ test)** — test 브랜치 회귀 217/217 GREEN.
- **★ v1.2.1 merge FULLY UNBLOCKED**(frontend) — develop WT CLEAN · Open 0.
- **cross-stream merge BLOCK** — backend WT dirty · QA-20260612-B61 Open.
- **operation 승격 BLOCK** — develop→test merge 미실행(370 commits) · cross-stream BLOCK · post-merge live E2E 미실행.
