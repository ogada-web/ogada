<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-17T22:19:30+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-17 967차)

> **967차 PASS(@test rerun) + merge FULLY UNBLOCKED(2 FE)** — test `@b93e098` 1st **1 FAIL/1653 PASS** (317.29s; `IntensiveExcretionObservationPage` flake) → rerun **1654/1654 PASS** (317.05s) · develop HEAD `@7aac550` **1654/1654 PASS** (321.26s) · build **1045 modules** (7.47s) · audit **0** · live E2E **122 PASS/19 SKIP** (29.40s) · develop `@7aac550` WT **CLEAN** · test `@b93e098` WT **CLEAN** · `test..develop` **2 ahead** · origin/test `@ab4de83` (**2 unpushed**) · **★ QA-B130 Fixed verified @ `7aac550`** · Open **0(active)** · Planned **QA-B116+QA-B95 partial** · operation **BLOCK**(origin/test push 2 FE+372 BE+QA-B95)

## 967차 (2026-06-17T22:19 UTC) — live-e2e bootstrap + BathingSchedule test stabilize · merge pending

| 항목 | 값 (967차) |
|------|-----|
| test HEAD | `b93e098` (local; origin/test `ab4de83`) |
| develop HEAD | `7aac550` |
| ahead (`test..develop`) | **2** (`b2c09e1` · `7aac550`) |
| unit test (@test 1st) | **1 FAIL/1653 PASS** (342 files, 317.29s; `IntensiveExcretionObservationPage` create flake) |
| unit test (@test rerun) | **1654/1654 PASS** (342 files, 317.05s) |
| unit test (@develop HEAD) | **1654/1654 PASS** (342 files, 321.26s) |
| build | 1045 modules SUCCESS (7.47s) |
| audit | 0 vulnerabilities |
| live E2E (@test workaround) | **122 PASS/19 SKIP** (49 files, 29.40s) |
| FE merge status | **FULLY UNBLOCKED** — 2 commits pending local merge |
| BE test/develop HEAD | `92be918` CLEAN |
| BE origin/test | `598d108` (372 unpushed) |
| routes / pages (@develop) | 106 route · 157 page files |
| operation | **BLOCK** (origin/test push + QA-B95) |

### Pending merge commits (2)

1. `b2c09e1` — `fix(live-e2e): refresh bootstrap credentials reliably for QA-B95`
2. `7aac550` — `stabilize bathing schedule create test` (QA-B130 closure)
