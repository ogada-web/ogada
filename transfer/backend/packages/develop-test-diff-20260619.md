<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-19T23:46:03+00:00 -->
# develop ↔ test diff 메타 (2026-06-19, 1110차 — test @71b2d32 · develop @71b2d32 · MERGE EXECUTED · J03 quiet-hours manual document send guard)

> **1110차 재검증 (23:46 UTC) — pre-merge test `@4da0ca8` `mvn test` **1591/1591 PASS**(302 suites, ~73s) · develop HEAD `@71b2d32` **1593/1593 PASS**(302 suites, ~75s) · ★ **develop→test merge EXECUTED**(FF `4da0ca8`→`71b2d32`, 1 commit) · post-merge **1593/1593 PASS**(302 suites, ~67s) · `test..develop` **0 ahead** · origin/test `@598d108` (**445 unpushed**) · Open **0(active backend)** · cross-stream **SYNCED(FE@501fedc + BE@71b2d32)** · operation **BLOCK**(origin/test push 445 BE+80 FE+QA-B95).

## merged commits (4da0ca8 → 71b2d32)

| SHA | message |
|-----|---------|
| `71b2d32` | fix(v2/j03): fail manual document sends during quiet hours |

## changed files (1 commit, 4 files +91/-4)

- `NotificationService.java` — quiet-hours guard for manual guardian document sends (+26 lines)
- `NotificationServiceTest.java` — quiet-hours rejection coverage (+61 lines)
- `GuardianDocumentNotificationService.java` — delegate to NotificationService quiet-hours policy
- `GuardianDocumentNotificationServiceTest.java` — test alignment (+6/-3)

## test delta

| stage | SHA | suites | tests | result |
|-------|-----|--------|-------|--------|
| test baseline | `4da0ca8` | 302 | 1591 | PASS (TSR 1110차 ~73s) |
| develop pre-merge | `71b2d32` | 302 | 1593 | PASS (TSR 1110차 ~75s) |
| post-merge | `71b2d32` | 302 | 1593 | PASS (TSR 1110차 ~67s) |
| merge decision | `EXECUTED` | - | - | PASS (FF 1 commit) |

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-19T23:14:13+00:00 -->
# develop ↔ test diff 메타 (2026-06-19, 1108차 — test @4da0ca8 · develop @4da0ca8 · MERGE EXECUTED · G-CASH-RECEIPT-LOG identifier validation deepen)

> **1108차 재검증 (23:14 UTC) — pre-merge test `@298bcdf` `mvn test` **1585/1585 PASS**(302 suites, ~76s) · develop HEAD `@4da0ca8` **1591/1591 PASS**(302 suites, ~75s) · ★ **develop→test merge EXECUTED**(FF `298bcdf`→`4da0ca8`, 2 commits) · post-merge **1591/1591 PASS**(302 suites, ~70s) · `test..develop` **0 ahead** · origin/test `@598d108` (**444 unpushed**) · Open **0(active backend)** · **★ QA-20260619-B157 Fixed @ `4da0ca8`** · cross-stream **BLOCK(FE merge pending 1 @ `501fedc`)** · operation **BLOCK**(origin/test push 444 BE+79 FE+QA-B95).

## merged commits (298bcdf → 4da0ca8)

| SHA | message |
|-----|---------|
| `35d1560` | fix(v2/g-cash-receipt-log): validate normalized phone and biz identifiers |
| `4da0ca8` | Validate cash receipt identifiers are numeric |

## changed files (2 commits, 3 files +177/-1)

- `CashReceiptIssuanceService.java` — normalized phone/biz identifier validation + numeric-only guard
- `CashReceiptIssuanceServiceTest.java` — validation scenario expansion (+139 lines)
- `CashReceiptIssuanceLiveApiRoutingE2eTest.java` — live API routing regression cases (+20 lines)

## test delta

| stage | SHA | suites | tests | result |
|-------|-----|--------|-------|--------|
| test baseline | `298bcdf` | 302 | 1585 | PASS (TSR 1108차 ~76s) |
| develop pre-merge | `4da0ca8` | 302 | 1591 | PASS (TSR 1108차 ~75s) |
| post-merge | `4da0ca8` | 302 | 1591 | PASS (TSR 1108차 ~70s) |
| merge decision | `EXECUTED` | - | - | PASS (FF 2 commits) |

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-19T21:49:23+00:00 -->
# develop ↔ test diff 메타 (2026-06-19, 1104차 — test @298bcdf · develop @298bcdf · MERGE EXECUTED · G-CASH-RECEIPT-LOG identifier normalization)

> **1104차 재검증 (21:49 UTC) — pre-merge test `@08ad3b3` `mvn test` **1583/1583 PASS**(302 suites, ~74s) · develop HEAD `@298bcdf` **1585/1585 PASS**(302 suites, ~73s) · ★ **develop→test merge EXECUTED**(FF `08ad3b3`→`298bcdf`, 1 commit) · post-merge **1585/1585 PASS**(302 suites, ~69s) · `test..develop` **0 ahead** · origin/test `@598d108` (**442 unpushed**) · Open **0(active backend)** · cross-stream **BLOCK(FE merge pending 1 + develop DIRTY 4M)** · operation **BLOCK**(origin/test push 442 BE+77 FE+QA-B95).

## merged commits (08ad3b3 → 298bcdf)

| SHA | message |
|-----|---------|
| `298bcdf` | fix(v2/g-cash-receipt-log): normalize identifier matching in issuance search |

## changed files (1 commit, 2 files +72/-2 approx.)

- `298bcdf` — `CashReceiptIssuanceService` identifier normalization (hyphen/space strip, case-insensitive) + `CashReceiptIssuanceServiceTest` +59 lines (+2 @Test)

## test delta

| stage | SHA | suites | tests | result |
|-------|-----|--------|-------|--------|
| test baseline | `08ad3b3` | 302 | 1583 | PASS (TSR 1104차 ~74s) |
| develop pre-merge | `298bcdf` | 302 | 1585 | PASS (TSR 1104차 ~73s) |
| post-merge | `298bcdf` | 302 | 1585 | PASS (TSR 1104차 ~69s) |
| merge decision | `EXECUTED` | - | - | PASS (FF 1 commit) |

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-19T21:07:30+00:00 -->
# develop ↔ test diff 메타 (2026-06-19, 1103차 — test @08ad3b3 · develop @08ad3b3 · MERGE EXECUTED · QA-B156 Fixed)

> **1103차 재검증 (21:07 UTC) — pre-merge test `@ceeaeb9` `mvn test` **1572/1572 PASS**(300 suites, ~48s) · develop HEAD `@08ad3b3` **1583/1583 PASS**(302 suites, ~75s) · ★ **develop→test merge EXECUTED**(FF `ceeaeb9`→`08ad3b3`, 3 commits) · post-merge **1583/1583 PASS**(302 suites, ~68s) · `test..develop` **0 ahead** · origin/test `@598d108` (**441 unpushed**) · Open **0(active backend)** · **★ QA-20260619-B156 Fixed @ `08ad3b3`** · cross-stream **BLOCK(FE merge pending 1 @58d6694)** · operation **BLOCK**(origin/test push 441 BE+77 FE+QA-B95).

## merged commits (ceeaeb9 → 08ad3b3)

| SHA | message |
|-----|---------|
| `43ef73b` | test(g26): deepen yearBasis routing and per-client claim-year coverage |
| `e454d3b` | feat(g-7-1): add billing statement Excel export API |
| `08ad3b3` | fix(test): add billing export mock to RBAC webmvc test |

## changed files (3 commits, 13 files +1047/-21 approx.)

- `43ef73b` — G26 yearBasis routing/unit/E2E tests (3 files)
- `e454d3b` — `BillingStatementExportService` + `BillingController` Excel export API + tests (12 files)
- `08ad3b3` — `RoleBasedControllerAccessTest` + routing harness `@MockBean` for `BillingStatementExportService` (QA-B156 closure)

## test delta

| stage | SHA | suites | tests | result |
|-------|-----|--------|-------|--------|
| test baseline | `ceeaeb9` | 300 | 1572 | PASS (TSR 1103차 ~48s) |
| develop pre-merge | `08ad3b3` | 302 | 1583 | PASS (TSR 1103차 ~75s) |
| post-merge | `08ad3b3` | 302 | 1583 | PASS (TSR 1103차 ~68s) |
| merge decision | `EXECUTED` | - | - | PASS (FF 3 commits) |

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-19T20:34:11+00:00 -->
# develop ↔ test diff 메타 (2026-06-19, 1101차 — test @ceeaeb9 · develop @e454d3b · MERGE SKIP · QA-B156)

> **1101차 재검증 (20:34 UTC) — test `@ceeaeb9` `mvn test` **1572/1572 PASS**(300 suites, ~49s) · develop HEAD `@e454d3b` `mvn test` **1583 run / 0 fail / 41 error**(302 suites, ~50s · QA-B156) · `test..develop` **0 ahead / 2 behind** · origin/test `@598d108` (**438 unpushed**) · Open **1(active backend)** QA-20260619-B156 · cross-stream **BLOCK(BE QA-B156 · FE SYNCED @19ed7f3)** · operation **BLOCK**(QA-B156+origin/test push 438 BE+77 FE+QA-B95).

## pending commits (ceeaeb9 → e454d3b)

| SHA | message |
|-----|---------|
| `43ef73b` | test(g26): deepen yearBasis routing and per-client claim-year coverage |
| `e454d3b` | feat(g-7-1): add billing statement Excel export API |

## changed files (pending 2 commits, 15 files +1231/-42 approx.)

- `43ef73b` — G26 yearBasis routing/unit/E2E tests (3 files)
- `e454d3b` — `BillingStatementExportService` + `BillingController` Excel export API + tests (12 files)
- **regression**: `RoleBasedControllerAccessTest$BillingAccess` — `BillingStatementExportService` @MockBean 누락 → 41 ERR (QA-B156)

## test delta

| stage | SHA | suites | tests | result |
|-------|-----|--------|-------|--------|
| test baseline | `ceeaeb9` | 300 | 1572 | PASS (TSR 1101차 ~49s) |
| develop current | `e454d3b` | 302 | 1583 (41 ERR) | BLOCK (TSR 1101차 ~50s · QA-B156) |
| merge decision | `SKIP` | - | - | BLOCK (develop merge gate 41 ERR) |

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-19T20:00:55+00:00 -->
# develop ↔ test diff 메타 (2026-06-19, 1099차 — test @ceeaeb9 · develop @43ef73b · MERGE SKIP)

> **1099차 재검증 (20:00 UTC) — test `@ceeaeb9` `mvn test` **1572/1572 PASS**(300 suites, 48.321s) · develop HEAD `@43ef73b` `mvn test` **1575/1575 PASS**(302 suites, 49.831s) · `test..develop` **0 ahead / 1 behind**(merge pending 1) · origin/test `@598d108` (**438 unpushed**) · Open **0(active backend)** · Open **1(active frontend)** QA-20260619-B155 · cross-stream **BLOCK(FE merge pending 2)** · operation **BLOCK**(origin/test push 438 BE+74 FE+QA-B95).

## pending commits (ceeaeb9 → 43ef73b)

| SHA | message |
|-----|---------|
| `43ef73b` | test(g26): deepen yearBasis routing and per-client claim-year coverage |

## changed files (pending 1 commit, 3 files +188/-21)

- `BillingServiceTest.java` — claim-year basis regression/unit cases 확장
- `MedicalExpenseDeductionReportLiveApiRoutingE2eTest.java` — yearBasis 라우팅 E2E 케이스 확장
- `MustApiEndpointRoutingTest.java` — mandatory routing matrix 보강

## test delta

| stage | SHA | suites | tests | result |
|-------|-----|--------|-------|--------|
| test baseline | `ceeaeb9` | 300 | 1572 | PASS (TSR 1099차 48.321s) |
| develop current | `43ef73b` | 302 | 1575 | PASS (TSR 1099차 49.831s) |
| merge decision | `SKIP` | - | - | BLOCK (`test..develop` 0/1) |

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-19T19:34:06+00:00 -->
# develop ↔ test diff 메타 (2026-06-19, 1097차 — test @ceeaeb9 · develop @ceeaeb9 · MERGE EXECUTED)

> **1097차 재검증 (19:34 UTC) — pre-merge test `@58ff35e` `mvn test` **1566/1566 PASS**(299 suites, ~49s) · develop HEAD `@ceeaeb9` **1572/1572 PASS**(300 suites, ~51s) · ★ **develop→test merge EXECUTED**(FF `58ff35e`→`ceeaeb9`, 1 commit) · post-merge **1572/1572 PASS**(300 suites, ~68s) · `test..develop` **0 ahead** · origin/test `@598d108` (**438 unpushed**) · Open **0(active backend)** · cross-stream **BLOCK(FE merge pending 1)** · operation **BLOCK**(origin/test push 438 BE+74 FE+QA-B95).

## merged commits (58ff35e → ceeaeb9)

| SHA | message |
|-----|---------|
| `ceeaeb9` | feat(g26): add medical deduction year basis and NTS batch export API |

## changed files (1 commit, 11 files +638/-16)

- `MedicalExpenseDeductionYearBasis.java` — year-basis enum for medical expense deduction reports
- `BillingService.java` — NTS batch export aggregation (+343 lines)
- `BillingController.java` — year-basis query param + batch export endpoint
- `BillingServiceTest.java` — unit coverage for year basis + batch export (+161 lines)
- `MedicalExpenseDeductionYearBasisTest.java` — enum/API contract tests (new)
- `GuardianCheckinController.java` · `ClientController.java` — minor RBAC/routing alignment
- `G26StatisticsReportsLiveApiRoutingE2eTest.java` · `MedicalExpenseDeductionReportLiveApiRoutingE2eTest.java` · `MustApiEndpointRoutingTest.java` · `RoleBasedControllerAccessTest.java` — routing/RBAC harness updates

## test delta

| stage | SHA | suites | tests | result |
|-------|-----|--------|-------|--------|
| test baseline | `58ff35e` | 299 | 1566 | PASS (TSR 1097차 ~49s) |
| develop pre-merge | `ceeaeb9` | 300 | 1572 | PASS (TSR 1097차 ~51s) |
| post-merge | `ceeaeb9` | 300 | 1572 | PASS (TSR 1097차 ~68s) |

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-19T18:29:30+00:00 -->
# develop ↔ test diff 메타 (2026-06-19, 1095차 — test @58ff35e · develop @58ff35e · MERGE EXECUTED)

> **1095차 재검증 (18:29 UTC) — pre-merge test `@ab5708b` `mvn test` **1565/1565 PASS**(299 suites, ~50s) · develop HEAD `@58ff35e` **1566/1566 PASS**(299 suites, ~49s) · ★ **develop→test merge EXECUTED**(FF `ab5708b`→`58ff35e`, 1 commit) · post-merge **1566/1566 PASS**(299 suites, ~68s) · `test..develop` **0 ahead** · origin/test `@598d108` (**437 unpushed**) · Open **0(active backend)** · cross-stream **SYNCED(FE+BE)** · operation **BLOCK**(origin/test push 437 BE+73 FE+QA-B95).

## merged commits (ab5708b → 58ff35e)

| SHA | message |
|-----|---------|
| `58ff35e` | feat(g-cash-receipt-log): support HQ multi-branch pending list and prior-year flag |

## changed files (1 commit, 4 files +110)

- `PendingCashReceiptIssuanceResponse.java` — HQ multi-branch fields + prior-year flag on list item DTO
- `CashReceiptIssuanceService.java` — HQ scope aggregation across branches (+69 lines)
- `CashReceiptIssuanceServiceTest.java` — unit coverage for multi-branch + prior-year (+44 lines)
- `CashReceiptIssuanceLiveApiRoutingE2eTest.java` — live API routing harness extend (+4 lines)

## test delta

| stage | SHA | suites | tests | result |
|-------|-----|--------|-------|--------|
| test baseline | `ab5708b` | 299 | 1565 | PASS (TSR 1095차 ~50s) |
| develop pre-merge | `58ff35e` | 299 | 1566 | PASS (TSR 1095차 ~49s) |
| post-merge | `58ff35e` | 299 | 1566 | PASS (TSR 1095차 ~68s) |

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-19T17:54:36+00:00 -->
# develop ↔ test diff 메타 (2026-06-19, 1094차 — test @ab5708b · develop @ab5708b · MERGE EXECUTED)

> **1094차 재검증 (17:54 UTC) — pre-merge test `@fe54af8` `mvn test` **1560/1560 PASS**(299 suites, ~50s) · develop HEAD `@ab5708b` **1565/1565 PASS**(299 suites, ~49s) · ★ **develop→test merge EXECUTED**(FF `fe54af8`→`ab5708b`, 1 commit) · post-merge **1565/1565 PASS**(299 suites, ~69s) · `test..develop` **0 ahead** · origin/test `@598d108` (**436 unpushed**) · Open **0(active backend)** · operation **BLOCK**(origin/test push 436 BE+72 FE+QA-B95).

## merged commits (fe54af8 → ab5708b)

| SHA | message |
|-----|---------|
| `ab5708b` | feat(g-cash-receipt-log): add pending cash receipt issuance list API |

## changed files (1 commit, 8 files +244)

- `BillingController.java` — `GET /billing/cash-receipt-issuances/pending` list endpoint
- `PendingCashReceiptIssuanceListResponse.java` / `PendingCashReceiptIssuanceResponse.java` — list DTOs (new)
- `CashReceiptIssuanceService.java` — pending issuance list aggregation (+86 lines)
- `CashReceiptIssuanceServiceTest.java` — unit coverage (+43 lines)
- `CashReceiptIssuanceLiveApiRoutingE2eTest.java` — live API routing harness (+44 lines)
- `MustApiEndpointRoutingTest.java` / `RoleBasedControllerAccessTest.java` — routing + RBAC coverage

## test delta

| stage | SHA | suites | tests | result |
|-------|-----|--------|-------|--------|
| test baseline | `fe54af8` | 299 | 1560 | PASS (TSR 1094차 ~50s) |
| develop pre-merge | `ab5708b` | 299 | 1565 | PASS (TSR 1094차 ~49s) |
| post-merge | `ab5708b` | 299 | 1565 | PASS (TSR 1094차 ~69s) |

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-19T17:27:23+00:00 -->
# develop ↔ test diff 메타 (2026-06-19, 1092차 — test @fe54af8 · develop @fe54af8 · MERGE EXECUTED)

> **1092차 재검증 (17:27 UTC) — pre-merge test `@f79a19e` `mvn test` **1553/1553 PASS**(298 suites, ~51s) · develop HEAD `@fe54af8` **1560/1560 PASS**(299 suites, ~49s) · ★ **develop→test merge EXECUTED**(FF `f79a19e`→`fe54af8`, 2 commits) · post-merge **1560/1560 PASS**(299 suites, ~68s) · `test..develop` **0 ahead** · origin/test `@598d108` (**435 unpushed**) · Open **0(active backend)** · **★ QA-B154 Fixed** · operation **BLOCK**(origin/test push 435 BE+72 FE+QA-B95).

## merged commits (f79a19e → fe54af8)

| SHA | message |
|-----|---------|
| `8e6e0c6` | test(g-cash-receipt-log): add live API routing harness and client profile coverage |
| `fe54af8` | feat(g-cash-receipt-log): expose pending and overdue counts on dashboard API |

## changed files (2 commits, 8 files +442/-11)

- `CashReceiptIssuanceService.java` — pending/overdue count aggregation deepen
- `BranchDashboardResponse.java` / `HqDashboardResponse.java` — cash receipt pending/overdue StatCard fields
- `DashboardService.java` — wire cash receipt issuance counts into dashboard API
- `CashReceiptIssuanceServiceTest.java` / `DashboardServiceTest.java` — unit coverage (+146 lines)
- `CashReceiptIssuanceLiveApiRoutingE2eTest.java` — live API routing harness (new, 197 lines)
- `PilotChecklistJwtE2eTest.java` — pilot checklist routing smoke update

## test delta

| stage | SHA | suites | tests | result |
|-------|-----|--------|-------|--------|
| test baseline | `f79a19e` | 298 | 1553 | PASS (TSR 1090차 ~51s) |
| develop pre-merge | `fe54af8` | 299 | 1560 | PASS (TSR 1092차 ~49s) |
| post-merge | `fe54af8` | 299 | 1560 | PASS (TSR 1092차 ~68s) |

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-19T16:46:16+00:00 -->
# develop ↔ test diff 메타 (2026-06-19, 1090차 — test @f79a19e · develop @8e6e0c6 · MERGE PENDING 1)

> **1090차 재검증 (16:46 UTC) — test `@f79a19e` `mvn test` **1553/1553 PASS**(298 suites, ~51s) · develop HEAD `@8e6e0c6` WT **CLEAN** · `test..develop` **0 ahead / 1 behind**(merge pending 1) · origin/test `@598d108` (**433 unpushed**) · Open **1(active backend)** QA-20260619-B154 · operation **BLOCK**(QA-B154+origin/test push 433 BE+71 FE+QA-B95).

## pending commit (f79a19e → 8e6e0c6)

| SHA | message |
|-----|---------|
| `8e6e0c6` | test(g-cash-receipt-log): add live API routing harness and client profile coverage |

## test delta

| stage | SHA | suites | tests | result |
|-------|-----|--------|-------|--------|
| test baseline | `f79a19e` | 298 | 1553 | PASS (TSR 1090차 ~51s) |
| develop pending | `8e6e0c6` | 미실행 | 미실행 | BLOCK (merge pending 1, QA-B154) |

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-19T16:03:05+00:00 -->
# develop ↔ test diff 메타 (2026-06-19, 1088차 — test @f79a19e · develop @f79a19e · MERGE EXECUTED)

> **1088차 재검증 (16:03 UTC) — pre-merge test `@7848b0f` `mvn test` **1541/1541 PASS**(297 suites, ~77s) · develop HEAD `@f79a19e` **1553/1553 PASS**(298 suites, ~76s) · ★ **develop→test merge EXECUTED**(FF `7848b0f`→`f79a19e`, 2 commits) · post-merge **1553/1553 PASS**(298 suites, ~68s) · `test..develop` **0 ahead** · origin/test `@598d108` (**433 unpushed**) · operation **BLOCK**(QA-B153+origin/test push 433 BE+68 FE+QA-B95).

## merged commits (7848b0f → f79a19e)

| SHA | message |
|-----|---------|
| `4432558` | feat(g-cash-receipt-log): add cash receipt issuance API and V158 migration |
| `f79a19e` | test(g-cash-receipt-log): add RBAC, routing, and 7-day SLA coverage |

## changed files (2 commits, 16 files +1062/-8)

- `V158__cash_receipt_issuances.sql` — cash receipt issuance ledger table (new)
- `CashReceiptIssuanceService.java` — issuance lifecycle service (new)
- `CashReceiptIssuanceEntity.java` / `CashReceiptIssuanceRepository.java` — persistence (new)
- `BillingController.java` — cash receipt issuance REST endpoints
- `CashReceiptIssuanceServiceTest.java` — domain unit coverage (+246 lines, new)
- `RoleBasedControllerAccessTest.java` — RBAC coverage for billing cash receipt routes
- `MustApiEndpointRoutingTest.java` — routing coverage for new endpoints
- Pilot/routing E2E tests — cash receipt route registration updates

## test delta

| stage | SHA | suites | tests | result |
|-------|-----|--------|-------|--------|
| test baseline | `7848b0f` | 297 | 1541 | PASS (TSR 1088차 ~77s) |
| develop pre-merge | `f79a19e` | 298 | 1553 | PASS (TSR 1088차 ~76s) |
| post-merge | `f79a19e` | 298 | 1553 | PASS (TSR 1088차 ~68s) |

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-19T14:58:00+00:00 -->
# develop ↔ test diff 메타 (2026-06-19, 1086차 — test @7848b0f · develop @7848b0f · MERGE EXECUTED)

> **1086차 재검증 (14:58 UTC) — pre-merge test `@caeac0d` `mvn test` **1539/1539 PASS**(297 suites, ~49s) · develop HEAD `@7848b0f` **1541/1541 PASS**(297 suites, ~74s) · ★ **develop→test merge EXECUTED**(FF `caeac0d`→`7848b0f`, 1 commit) · post-merge **1541/1541 PASS**(297 suites, ~70s) · `test..develop` **0 ahead** · origin/test `@598d108` (**431 unpushed**) · operation **BLOCK**(origin/test push 431 BE+68 FE+QA-B95).

## merged commits (caeac0d → 7848b0f)

| SHA | message |
|-----|---------|
| `7848b0f` | fix(v2/live-e2e): normalize seeded bootstrap credentials |

## changed files (1 commit, 2 files +103/-23)

- `LiveE2eBootstrapService.java` — normalize seeded bootstrap guardian/staff credential handling for live-e2e bootstrap
- `LiveE2eBootstrapServiceTest.java` — regression coverage for credential normalization (+70 lines)

## test delta

| stage | SHA | suites | tests | result |
|-------|-----|--------|-------|--------|
| test baseline | `caeac0d` | 297 | 1539 | PASS (TSR 1086차 ~49s) |
| develop pre-merge | `7848b0f` | 297 | 1541 | PASS (TSR 1086차 ~74s) |
| post-merge | `7848b0f` | 297 | 1541 | PASS (TSR 1086차 ~70s) |

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-19T14:05:28+00:00 -->
# develop ↔ test diff 메타 (2026-06-19, 1084차 — test @caeac0d · develop @caeac0d · MERGE EXECUTED)

> **1084차 재검증 (14:05 UTC) — pre-merge test `@c0a59aa` `mvn test` **1534/1534 PASS**(296 suites, ~73s) · develop HEAD `@caeac0d` **1539/1539 PASS**(297 suites, ~72s) · ★ **develop→test merge EXECUTED**(FF `c0a59aa`→`caeac0d`, 2 commits) · post-merge **1539/1539 PASS**(297 suites, ~67s) · `test..develop` **0 ahead** · origin/test `@598d108` (**428 unpushed**) · operation **BLOCK**(origin/test push 428 BE+67 FE+QA-B95).

## merged commits (c0a59aa → caeac0d)

| SHA | message |
|-----|---------|
| `45d95ea` | feat(g32): probe V157 attendee_opinions array CHECK in live-e2e readiness |
| `caeac0d` | fix(v2/live-e2e): align health probe with G32 schema readiness blockers |

## changed files (2 commits, 8 files +346/-40)

- `G32SchemaReadinessProbe.java` — V157 attendee_opinions array CHECK probe (new)
- `HealthController.java` — G32 schema readiness blockers in health probe
- `LiveE2eController.java` — G32 readiness signal exposure deepen
- `LiveE2eProbeResponse.java` — schema readiness field
- `G32SchemaReadinessProbeTest.java` — probe unit coverage (new)
- `HealthControllerTest.java` — health readiness blocker assertions (+94 lines)
- `LiveE2eBootstrapLiveApiRoutingE2eTest.java` — G32 readiness routing E2E
- `LiveE2eControllerTest.java` — probe readiness coverage deepen

## test delta

| stage | SHA | suites | tests | result |
|-------|-----|--------|-------|--------|
| test baseline | `c0a59aa` | 296 | 1534 | PASS (TSR 1084차 ~73s) |
| develop pre-merge | `caeac0d` | 297 | 1539 | PASS (TSR 1084차 ~72s) |
| post-merge | `caeac0d` | 297 | 1539 | PASS (TSR 1084차 ~67s) |

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-19T12:53:33+00:00 -->
# develop ↔ test diff 메타 (2026-06-19, 1080차 — test @c0a59aa · develop @c0a59aa · MERGE EXECUTED)

> **1080차 재검증 (12:53 UTC) — pre-merge test `@510d2f3` `mvn test` **1534/1534 PASS**(296 suites, ~67s) · develop HEAD `@c0a59aa` **1534/1534 PASS**(296 suites, ~67s) · ★ **develop→test merge EXECUTED**(FF `510d2f3`→`c0a59aa`, 1 commit) · post-merge **1534/1534 PASS**(296 suites, ~67s) · `test..develop` **0 ahead** · origin/test `@598d108` (**428 unpushed**) · operation **BLOCK**(QA-B152+origin/test push 428 BE+65 FE+QA-B95).

## merged commits (510d2f3 → c0a59aa)

| SHA | message |
|-----|---------|
| `c0a59aa` | Add G32 schema readiness signals to live-e2e probe |

## changed files (1 commit, 3 files +45/-3)

- `LiveE2eController.java` — expose G32 case-management/dashboard field presence in probe + operation blockers
- `LiveE2eProbeResponse.java` — schema readiness signal fields
- `LiveE2eControllerTest.java` — probe readiness coverage (+4 assertions)

## test delta

| stage | SHA | suites | tests | result |
|-------|-----|--------|-------|--------|
| test baseline | `510d2f3` | 296 | 1534 | PASS (TSR 1080차 ~67s) |
| develop pre-merge | `c0a59aa` | 296 | 1534 | PASS (TSR 1080차 ~67s) |
| post-merge | `c0a59aa` | 296 | 1534 | PASS (TSR 1080차 ~67s) |

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-19T12:06:32+00:00 -->
# develop ↔ test diff 메타 (2026-06-19, 1078차 — test @510d2f3 · develop @510d2f3 · MERGE EXECUTED)

> **1078차 재검증 (12:06 UTC) — pre-merge test `@9ecd019` `mvn test` **1531/1531 PASS**(296 suites, ~46s) · develop HEAD `@510d2f3` **1534/1534 PASS**(296 suites, ~50s) · ★ **develop→test merge EXECUTED**(FF `9ecd019`→`510d2f3`, 1 commit) · post-merge **1534/1534 PASS**(296 suites, ~63s) · `test..develop` **0 ahead** · origin/test `@598d108` (**427 unpushed**) · operation **BLOCK**(origin/test push 427 BE+64 FE+QA-B95).

## merged commits (9ecd019 → 510d2f3)

| SHA | message |
|-----|---------|
| `510d2f3` | test(g32): extend pilot E2E and service tests for attendee opinions |

## changed files (1 commit, 2 files +125/-3)

- `CaseManagementServiceTest.java` — attendee opinions service coverage deepen
- `ProgramCompliancePilotServiceFlowE2eTest.java` — G32 pilot E2E attendee-opinion assertions

## test delta

| stage | SHA | suites | tests | result |
|-------|-----|--------|-------|--------|
| test baseline | `9ecd019` | 296 | 1531 | PASS (TSR 1078차 ~46s) |
| develop pre-merge | `510d2f3` | 296 | 1534 | PASS (TSR 1078차 ~50s) |
| post-merge | `510d2f3` | 296 | 1534 | PASS (TSR 1078차 ~63s) |

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-19T11:29:21+00:00 -->
# develop ↔ test diff 메타 (2026-06-19, 1076차 — test @9ecd019 · develop @9ecd019 · MERGE EXECUTED)

> **1076차 재검증 (11:29 UTC) — pre-merge test `@eed39ab` `mvn test` **1526/1526 PASS**(295 suites, ~47s) · develop HEAD `@9ecd019` **1531/1531 PASS**(296 suites, ~49s) · ★ **develop→test merge EXECUTED**(FF `eed39ab`→`9ecd019`, 1 commit) · post-merge **1531/1531 PASS**(296 suites, ~62s) · `test..develop` **0 ahead** · origin/test `@598d108` (**426 unpushed**) · operation **BLOCK**(origin/test push 426 BE+63 FE+QA-B95).

## merged commits (eed39ab → 9ecd019)

| SHA | message |
|-----|---------|
| `9ecd019` | test(g32): cover attendee opinions codec and malformed JSON compliance |

## changed files (1 commit, 2 files +89)

- `AttendeeOpinionsCodecTest.java` — JSONB attendee opinions codec round-trip + malformed payload guard
- `CaseManagementServiceTest.java` — malformed `attendeeOpinions` compliance coverage

## test delta

| stage | SHA | suites | tests | result |
|-------|-----|--------|-------|--------|
| test baseline | `eed39ab` | 295 | 1526 | PASS (TSR 1076차 ~47s) |
| develop pre-merge | `9ecd019` | 296 | 1531 | PASS (TSR 1076차 ~49s) |
| post-merge | `9ecd019` | 296 | 1531 | PASS (TSR 1076차 ~62s) |

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-19T10:49:00+00:00 -->
# develop ↔ test diff 메타 (2026-06-19, 1074차 — test @eed39ab · develop @eed39ab · MERGE EXECUTED)

> **1074차 재검증 (10:49 UTC) — pre-merge test `@5222a8f` `mvn test` **1524/1524 PASS**(295 suites, ~47s) · develop HEAD `@eed39ab` **1526/1526 PASS**(295 suites, ~74s) · ★ **develop→test merge EXECUTED**(FF `5222a8f`→`eed39ab`, 3 commits) · post-merge **1526/1526 PASS**(295 suites, ~67s) · `test..develop` **0 ahead** · origin/test `@598d108` (**425 unpushed**) · **★ QA-B151 Fixed @ `eed39ab`** · operation **BLOCK**(origin/test push 425 BE+62 FE+QA-B95).

## merged commits (5222a8f → eed39ab)

| SHA | message |
|-----|---------|
| `b9e0947` | feat(g32): expose case management attendee opinion gaps on dashboard API |
| `8835aa2` | feat(db): enforce JSON array shape on case_management_meetings.attendee_opinions (V157) |
| `eed39ab` | fix(g32): enforce unique per-attendee opinions for meetings |

## changed files (3 commits, 7 files +92/-5)

- `CaseManagementService.java` · `CaseManagementServiceTest.java` — unique per-attendee opinion enforcement
- `BranchDashboardResponse.java` · `HqDashboardResponse.java` · `DashboardService.java` · `DashboardServiceTest.java` — G32 attendee-opinion gap count
- `V157__case_management_attendee_opinions_array_check.sql` — JSON array shape CHECK

## test delta

| stage | SHA | suites | tests | result |
|-------|-----|--------|-------|--------|
| test baseline | `5222a8f` | 295 | 1524 | PASS (TSR 1074차 ~47s) |
| develop pre-merge | `eed39ab` | 295 | 1526 | PASS (TSR 1074차 ~74s) |
| post-merge | `eed39ab` | 295 | 1526 | PASS (TSR 1074차 ~67s) |

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-19T09:50:34+00:00 -->
# develop ↔ test diff 메타 (2026-06-19, 1072차 — test @5222a8f · develop @b9e0947 · MERGE PENDING 1)

> **1072차 재검증 (09:50 UTC) — test `@5222a8f` `mvn test` **1524/1524 PASS**(295 suites, 48.387s) · develop HEAD `@b9e0947` WT **CLEAN** · `test..develop` **0 ahead / 1 behind**(commit `b9e0947`) · origin/test `@598d108` (**422 unpushed**) · Open **1(active backend)** QA-20260619-B151 · operation **BLOCK**(QA-B151+origin/test push 422 BE+61 FE+QA-B95).

## pending commits (test..develop = 1)

| SHA | message |
|-----|---------|
| `b9e0947` | feat(g32): expose case management attendee opinion gaps on dashboard API |

## changed files in pending commit (1 commit, 6 files +145/-8)

- `BranchDashboardResponse.java` · `HqDashboardResponse.java` — G32 attendee-opinion gap 필드 추가
- `DashboardComplianceService.java` · `DashboardController.java` — branch/hq 대시보드 집계 응답 노출
- `DashboardControllerTest.java` · `DashboardComplianceServiceTest.java` — 신규 필드 회귀 검증

## test delta

| stage | SHA | suites | tests | result |
|-------|-----|--------|-------|--------|
| test baseline | `5222a8f` | 295 | 1524 | PASS (TSR 1072차 48.387s) |
| develop pending | `b9e0947` | 미실행(backend-only cycle) | 미실행 | merge pending 1 |

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-19T09:08:30+00:00 -->
# develop ↔ test diff 메타 (2026-06-19, 1070차 — test @5222a8f · develop @5222a8f · MERGE EXECUTED)

> **1070차 재검증 (09:08 UTC) — pre-merge test `@12d1a7b` `mvn test` **1521/1521 PASS**(295 suites, ~48s) · develop HEAD `@5222a8f` **1524/1524 PASS**(295 suites, ~50s) · ★ **develop→test merge EXECUTED**(FF `12d1a7b`→`5222a8f`, 1 commit: G32 per-attendee opinions on case management meetings) · post-merge **1524/1524 PASS**(295 suites, ~69s) · `test..develop` **0 ahead** · origin/test `@598d108` (**422 unpushed**) · Open **0(active backend)** · operation **BLOCK**(QA-B150+origin/test push 422 BE+59 FE+QA-B95).

## merged commits (12d1a7b → 5222a8f)

| SHA | message |
|-----|---------|
| `5222a8f` | feat(g32): add per-attendee opinions to case management meetings |

## changed files (1 commit, 17 files +315/-29)

- `AttendeeOpinionRecord.java` · `AttendeeOpinionsCodec.java` — G32 per-attendee opinion DTO/codec
- `CaseManagementService.java` · `CaseManagementMeetingEntity.java` — persist attendee opinions on meetings
- `V156__case_management_attendee_opinions_g32.sql` — migration for attendee opinions column
- `CaseManagementServiceTest.java` (+129 lines) — regression coverage for G32 opinions
- compliance/dashboard/pilot/routing/RBAC tests — aligned with G32 API surface

## test delta

| stage | SHA | suites | tests | result |
|-------|-----|--------|-------|--------|
| pre-merge test | `12d1a7b` | 295 | 1521 | PASS (TSR 1070차 ~48s) |
| develop HEAD | `5222a8f` | 295 | 1524 | PASS (TSR 1070차 ~50s) |
| post-merge test | `5222a8f` | 295 | 1524 | PASS (TSR 1070차 ~69s) |

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-19T08:35:18+00:00 -->
# develop ↔ test diff 메타 (2026-06-19, 1068차 — test @12d1a7b · develop @12d1a7b · MERGE EXECUTED)

> **1068차 재검증 (08:35 UTC) — pre-merge test `@bc754a0` `mvn test` **1521/1521 PASS**(295 suites, ~49s) · develop HEAD `@12d1a7b` **1521/1521 PASS**(295 suites, ~48s) · ★ **develop→test merge EXECUTED**(FF `bc754a0`→`12d1a7b`, 1 commit: live-e2e health diagnostics for operation readiness) · post-merge **1521/1521 PASS**(295 suites, ~67s) · `test..develop` **0 ahead** · origin/test `@598d108` (**421 unpushed**) · Open **0(active backend)** · operation **BLOCK**(origin/test push 421 BE+59 FE+QA-B95).

## merged commits (bc754a0 → 12d1a7b)

| SHA | message |
|-----|---------|
| `12d1a7b` | improve live-e2e health diagnostics for operation readiness |

## changed files (1 commit, 2 files +51)

- `HealthController.java` — deepen live-e2e operation readiness diagnostics in health probe payload
- `HealthControllerTest.java` — regression coverage for health diagnostics surfacing (+28 lines)

## test delta

| stage | SHA | suites | tests | result |
|-------|-----|--------|-------|--------|
| pre-merge test | `bc754a0` | 295 | 1521 | PASS (TSR 1068차 ~49s) |
| develop HEAD | `12d1a7b` | 295 | 1521 | PASS (TSR 1068차 ~48s) |
| post-merge test | `12d1a7b` | 295 | 1521 | PASS (TSR 1068차 ~67s) |

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-19T07:47:34+00:00 -->
# develop ↔ test diff 메타 (2026-06-19, 1066차 — test @bc754a0 · develop @bc754a0 · MERGE EXECUTED)

> **1066차 재검증 (07:47 UTC) — pre-merge test `@02a2eb8` `mvn test` **1520/1520 PASS**(295 suites, ~50s) · develop HEAD `@bc754a0` **1521/1521 PASS**(295 suites, ~48s) · ★ **develop→test merge EXECUTED**(FF `02a2eb8`→`bc754a0`, 1 commit: G21 branch-missing blocker in health probe) · post-merge **1521/1521 PASS**(295 suites, ~66s) · `test..develop` **0 ahead** · origin/test `@598d108` (**420 unpushed**) · Open **0(active backend)** · operation **BLOCK**(origin/test push 420 BE+58 FE+QA-B95).

## merged commits (02a2eb8 → bc754a0)

| SHA | message |
|-----|---------|
| `bc754a0` | fix(v2/live-e2e): surface G21 branch blocker in health probe |

## changed files (1 commit, 2 files +62)

- `HealthController.java` — expose G21 branch-missing blocker in readiness probe payload
- `HealthControllerTest.java` — regression coverage for branch blocker reporting (+59 lines)

## test delta

| stage | SHA | suites | tests | result |
|-------|-----|--------|-------|--------|
| pre-merge test | `02a2eb8` | 295 | 1520 | PASS (TSR 1066차 ~50s) |
| develop HEAD | `bc754a0` | 295 | 1521 | PASS (TSR 1066차 ~48s) |
| post-merge test | `bc754a0` | 295 | 1521 | PASS (TSR 1066차 ~66s) |

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-19T07:10:30+00:00 -->
# develop ↔ test diff 메타 (2026-06-19, 1064차 — test @02a2eb8 · develop @02a2eb8 · MERGE EXECUTED)

> **1064차 재검증 (07:10 UTC) — pre-merge test `@02cf036` `mvn test` **1520/1520 PASS**(295 suites, ~48s) · develop HEAD `@02a2eb8` **1520/1520 PASS**(295 suites, ~50s) · ★ **develop→test merge EXECUTED**(FF `02cf036`→`02a2eb8`, 1 commit: guardian credentials bootstrap enrichment · QA-B95 deepen) · post-merge **1520/1520 PASS**(295 suites, ~69s) · `test..develop` **0 ahead** · origin/test `@598d108` (**419 unpushed**) · Open **0(active backend)** · operation **BLOCK**(origin/test push 419 BE+57 FE+QA-B95).

## merged commits (02cf036 → 02a2eb8)

| SHA | message |
|-----|---------|
| `02a2eb8` | fix(v2/live-e2e): require configured guardian credentials for bootstrap enrichment |

## changed files (1 commit, 2 files +11/-13)

- `LiveE2eBootstrapService.java` — skip guardian token attachment when credentials blank
- `LiveE2eBootstrapServiceTest.java` — regression coverage refactor for guardian credential gating

## test delta

| stage | SHA | suites | tests | result |
|-------|-----|--------|-------|--------|
| pre-merge test | `02cf036` | 295 | 1520 | PASS (TSR 1064차 ~48s) |
| develop HEAD | `02a2eb8` | 295 | 1520 | PASS (TSR 1064차 ~50s) |
| post-merge test | `02a2eb8` | 295 | 1520 | PASS (TSR 1064차 ~69s) |

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-19T06:32:00+00:00 -->
# develop ↔ test diff 메타 (2026-06-19, 1062차 — test @02cf036 · develop @02cf036 · MERGE EXECUTED)

> **1062차 재검증 (06:32 UTC) — pre-merge test `@7898aa5` `mvn test` **1518/1518 PASS**(295 suites, ~49s) · develop HEAD `@02cf036` **1520/1520 PASS**(295 suites, ~47s) · ★ **develop→test merge EXECUTED**(FF `7898aa5`→`02cf036`, 1 commit: QA-B148 branch-scoped G21 seed readiness) · post-merge **1520/1520 PASS**(295 suites, ~68s) · `test..develop` **0 ahead** · origin/test `@598d108` (**418 unpushed**) · Open **0(active backend)** · **★ QA-B148 Fixed** · operation **BLOCK**(origin/test push 418 BE+54 FE+FE merge pending 2+QA-B95).

## merged commits (7898aa5 → 02cf036)

| SHA | message |
|-----|---------|
| `02cf036` | fix(v2/live-e2e): scope G21 seed readiness to configured branch (QA-B148) |

## changed files (1 commit, 2 files +106/-5)

- `LiveE2eBootstrapService.java` — branch-scoped visit schedule/billing/NHIS batch readiness probe
- `LiveE2eBootstrapServiceTest.java` — regression coverage for branch-scoped readiness (+87 tests)

## test delta

| stage | SHA | suites | tests | result |
|-------|-----|--------|-------|--------|
| pre-merge test | `7898aa5` | 295 | 1518 | PASS (TSR 1062차 ~49s) |
| develop HEAD | `02cf036` | 295 | 1520 | PASS (TSR 1062차 ~47s) |
| post-merge test | `02cf036` | 295 | 1520 | PASS (TSR 1062차 ~68s) |

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-19T05:43:29+00:00 -->
# develop ↔ test diff 메타 (2026-06-19, 1060차 — test @7898aa5 · develop @7898aa5+DIRTY · merge SKIP)

> **1060차 재검증 (05:43 UTC) — test `@7898aa5` `mvn test` **1518/1518 PASS**(295 suites, ~48s) · develop HEAD `@7898aa5` WT **DIRTY 2M**(`LiveE2eBootstrapService*` branch-scoped G21 seed readiness WIP · **QA-20260619-B148**) · merge **SKIP** · `test..develop` **0 ahead** · origin/test `@598d108` (**417 unpushed**) · Open **1 BLOCK QA-B148** · operation **BLOCK**(COD commit + origin/test push + QA-B95).

## uncommitted WIP (develop only — not in test)

| file | delta | note |
|------|-------|------|
| `LiveE2eBootstrapService.java` | +24/-5 | branch-scoped visit schedule/billing/NHIS batch readiness |
| `LiveE2eBootstrapServiceTest.java` | +87 | regression coverage for branch-scoped readiness |

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-19T05:06:18+00:00 -->
# develop ↔ test diff 메타 (2026-06-19, 1058차 — test @7898aa5 · develop @7898aa5 · MERGE EXECUTED)

> **1058차 재검증 (05:06 UTC) — pre-merge test `@191703f` `mvn test` **1517/1517 PASS**(295 suites, ~49s) · develop HEAD `@7898aa5` **1518/1518 PASS**(295 suites, ~49s) · ★ **develop→test merge EXECUTED**(FF `191703f`→`7898aa5`, 1 commit) · post-merge **1518/1518 PASS**(295 suites, ~68s) · `test..develop` **0 ahead** · origin/develop `@7898aa5` · origin/test `@598d108` (**417 unpushed**) · Open **0(active backend)** · Planned **QA-B116+QA-B95 partial** · operation **BLOCK**(QA-B147+origin/test push 417 BE+53 FE+QA-B95).

## merged commits (191703f → 7898aa5)

| SHA | message |
|-----|---------|
| `7898aa5` | fix(v2/live-e2e): expose G21 branch-missing blocker in probe |

## changed files (1 commit, 2 files +43/-0)

- `LiveE2eController.java` — expose `branchMissing` blocker in G21 live-e2e readiness probe payload
- `LiveE2eControllerTest.java` — regression tests for branch-missing blocker exposure (+1 test vs pre-merge baseline)

## test delta

| stage | SHA | suites | tests | result |
|-------|-----|--------|-------|--------|
| pre-merge test | `191703f` | 295 | 1517 | PASS (TSR 1058차 ~49s) |
| develop HEAD | `7898aa5` | 295 | 1518 | PASS (TSR 1058차 ~49s) |
| post-merge test | `7898aa5` | 295 | 1518 | PASS (TSR 1058차 ~68s) |

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-19T04:37:15+00:00 -->
# develop ↔ test diff 메타 (2026-06-19, 1056차 — test @191703f · develop @191703f · MERGE EXECUTED)

> **1056차 재검증 (04:37 UTC) — superseded by 1058차 (merge EXECUTED @7898aa5).**

## merged commits (429661e → 191703f)

| SHA | message |
|-----|---------|
| `cc295ec` | fix(v2/live-e2e): treat legacy DAY_CARE branch as G21 seed applicable (QA-B95) |
| `191703f` | fix: block live e2e seed readiness when branch missing |

## changed files (2 commits, 2 files +86/-3)

- `LiveE2eBootstrapService.java` — legacy `DAY_CARE` G21 seed gate + block readiness when branch missing
- `LiveE2eBootstrapServiceTest.java` — regression tests (+3 tests vs pre-merge baseline)

## test delta

| stage | SHA | suites | tests | result |
|-------|-----|--------|-------|--------|
| pre-merge test | `429661e` | 295 | 1514 | PASS (TSR 1056차 ~50s) |
| post-merge test | `191703f` | 295 | 1517 | PASS (TSR 1056차 ~67s) |

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-19T04:09:38+00:00 -->
# develop ↔ test diff 메타 (2026-06-19, 1054차 — test @429661e · develop @cc295ec · MERGE PENDING 1)

> **1054차 재검증 (04:09 UTC) — superseded by 1056차 (merge EXECUTED @191703f).**

## pending commit summary (test baseline 대비 develop +1)

| SHA | message |
|-----|---------|
| `cc295ec` | fix(v2/live-e2e): treat legacy DAY_CARE branch as G21 seed applicable (QA-B95) |

## changed files (1 commit, 2 files +46/-1)

- `LiveE2eBootstrapService.java` — include legacy `DAY_CARE` branch in G21 seed applicability gate
- `LiveE2eBootstrapServiceTest.java` — regression tests for legacy branch seed readiness path

## test delta

| stage | SHA | suites | tests | result |
|-------|-----|--------|-------|--------|
| test baseline | `429661e` | 295 | 1514 | PASS (TSR 1054차 49.172s) |
| develop HEAD | `cc295ec` | - | - | 미재실행 (tester 범위: `src/backend-test` baseline 재검증) |

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-19T03:47:30+00:00 -->
# develop ↔ test diff 메타 (2026-06-19, 1052차 — test @429661e · develop @429661e · MERGE EXECUTED)

> **1052차 재검증 (03:47 UTC) — pre-merge test `@c0403b0` `mvn test` **1513/1513 PASS**(295 suites, ~81s) · develop HEAD `@429661e` **1514/1514 PASS**(295 suites, ~75s) · ★ **develop→test merge EXECUTED**(FF `c0403b0`→`429661e`, 2 commits) · post-merge **1514/1514 PASS**(295 suites, ~68s) · `test..develop` **0 ahead** · origin/develop `@429661e` · origin/test `@598d108` (**414 unpushed**) · Open **0(active backend)** · Planned **QA-B116+QA-B95 partial** · operation **BLOCK**(origin/test push 414 BE+49 FE+QA-B95+FE merge pending 3).

## merged commits (c0403b0 → 429661e)

| SHA | message |
|-----|---------|
| `fd275f4` | feat(v2/live-e2e): seed paired PLAN/BILLING visit schedules in G21 bootstrap |
| `429661e` | feat(v2/live-e2e): expose paired BILLING schedule readiness in G21 probe |

## changed files (2 commits, 9 files +284/-65)

- `LiveE2eBootstrapService.java` — paired PLAN/BILLING schedule seed + BILLING readiness probe
- `LiveE2eBootstrapServiceTest.java` — regression coverage (+156 lines)
- `HealthController.java` / `HealthControllerTest.java` — G21 readiness probe surface
- `LiveE2eController.java` / `LiveE2eControllerTest.java` — probe response fields
- `LiveE2eBootstrapResponse.java` / `LiveE2eProbeResponse.java` — paired BILLING readiness DTO
- `LiveE2eBootstrapLiveApiRoutingE2eTest.java` — live API routing alignment

## test delta

| stage | SHA | suites | tests | result |
|-------|-----|--------|-------|--------|
| test baseline | `c0403b0` | 295 | 1513 | PASS (TSR 1052차 ~81s) |
| develop HEAD | `429661e` | 295 | 1514 | PASS (TSR 1052차 ~75s) |
| post-merge test | `429661e` | 295 | 1514 | PASS (TSR 1052차 ~68s) |

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-19T03:21:55+00:00 -->
# develop ↔ test diff 메타 (2026-06-19, 1050차 — test @c0403b0 · develop @fd275f4 · MERGE PENDING 1)

> **1050차 재검증 (03:21 UTC) — test `@c0403b0` (`src/backend-test`) `mvn test` **1513/1513 PASS**(295 suites, 50.9s) · `npm test` N/A(no `package.json`) · develop `@fd275f4` WT **CLEAN** · test `@c0403b0` WT **CLEAN** · `test..develop` **0 ahead / 1 behind**(backend merge pending 1) · merge **SKIP** · origin/develop `@fd275f4` · origin/test `@598d108` (**412 unpushed**) · Open **0(active backend)** · Planned **QA-B116+QA-B95 partial** · operation **BLOCK**(origin/test push 412 BE+49 FE+QA-B95+merge pending BE1/FE2).

## pending commit summary (test baseline 대비 develop +1)

| SHA | message |
|-----|---------|
| `fd275f4` | feat(v2/live-e2e): seed paired PLAN/BILLING visit schedules in G21 bootstrap |

## test delta

| stage | SHA | suites | tests | result |
|-------|-----|--------|-------|--------|
| test baseline | `c0403b0` | 295 | 1513 | PASS (TSR 1050차 50.9s) |
| develop HEAD | `fd275f4` | - | - | 미재실행 (tester 범위: `src/backend-test` baseline 재검증) |

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-19T02:28:32+00:00 -->
# develop ↔ test diff 메타 (2026-06-19, 1048차 — test @c0403b0 · develop @c0403b0 · MERGE EXECUTED)

> **1048차 재검증 (02:28 UTC) — pre-merge test `@c651b30` `mvn test` **1512/1512 PASS**(295 suites, ~50s) · develop HEAD `@c0403b0` **1513/1513 PASS**(295 suites, ~51s) · ★ **develop→test merge EXECUTED**(FF `c651b30`→`c0403b0`, 1 commit) · post-merge **1513/1513 PASS**(295 suites, ~67s) · `test..develop` **0 ahead** · origin/develop `@c0403b0` · origin/test `@598d108` (**412 unpushed**) · Open **0(active backend)** · Planned **QA-B116+QA-B95 partial** · operation **BLOCK**(origin/test push 412 BE+49 FE+QA-B95).

## merged commits (c651b30 → c0403b0)

| SHA | message |
|-----|---------|
| `c0403b0` | fix(v2/live-e2e): require NHIS row-batch linkage for G21 seed readiness |

## changed files (1 commit, 2 files +51/-7)

- `LiveE2eBootstrapService.java` — require NHIS import row-batch linkage before G21 seed readiness
- `LiveE2eBootstrapServiceTest.java` — regression tests for row-batch linkage guard (+40 lines)

## test delta

| stage | SHA | suites | tests | result |
|-------|-----|--------|-------|--------|
| pre-merge test | `c651b30` | 295 | 1512 | PASS (TSR 1048차 ~50s) |
| develop HEAD | `c0403b0` | 295 | 1513 | PASS (TSR 1048차 ~51s) |
| post-merge test | `c0403b0` | 295 | 1513 | PASS (TSR 1048차 ~67s) |

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-19T02:03:30+00:00 -->
# develop ↔ test diff 메타 (2026-06-19, 1047차 — test @c651b30 · develop @c651b30 · MERGE EXECUTED)

> **1047차 재검증 (02:03 UTC) — pre-merge test `@14582bf` `mvn test` **1511/1511 PASS**(295 suites, ~71s) · develop HEAD `@c651b30` **1512/1512 PASS**(295 suites, ~73s; **★ QA-20260619-B145 Fixed verified**) · ★ **develop→test merge EXECUTED**(FF `14582bf`→`c651b30`, 1 commit) · post-merge **1512/1512 PASS**(295 suites, ~66s) · `test..develop` **0 ahead** · origin/develop `@c651b30` · origin/test `@598d108` (**411 unpushed**) · Open **0(active backend)** · Planned **QA-B116+QA-B95 partial** · operation **BLOCK**(origin/test push 411 BE+49 FE+QA-B95).

## merged commits (14582bf → c651b30)

| SHA | message |
|-----|---------|
| `c651b30` | fix(live-e2e): scope seed fallback ids per tenant (QA-B145) |

## changed files (1 commit, 2 files +127/-3)

- `LiveE2eBootstrapService.java` — `scopedFallbackId(kind, organizationId)` deterministic org-scoped fallback IDs
- `LiveE2eBootstrapServiceTest.java` — org-scoped fallback + g21SeedStatus readiness regression tests (+119 lines)

## test delta

| stage | SHA | suites | tests | result |
|-------|-----|--------|-------|--------|
| pre-merge test | `14582bf` | 295 | 1511 | PASS (TSR 1047차 ~71s) |
| develop HEAD | `c651b30` | 295 | 1512 | PASS (TSR 1047차 ~73s) |
| post-merge test | `c651b30` | 295 | 1512 | PASS (TSR 1047차 ~66s) |

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-19T01:26:00+00:00 -->
# develop ↔ test diff 메타 (2026-06-19, 1045차 — test @14582bf · develop @14582bf · MERGE SKIP · develop WT DIRTY)

> **1045차 재검증 (01:26 UTC) — test `@14582bf` `mvn test` **1511/1511 PASS**(295 suites, ~51s) · develop HEAD `@14582bf` WT **DIRTY 2M**(`LiveE2eBootstrapService*` — `scopedFallbackId` WIP · **QA-20260619-B145**) · develop HEAD `mvn test` **미재실행**(WT dirty; 1043차 carry **1511/1511 PASS**) · `test..develop` **0 ahead / 0 behind** · merge **SKIP** · origin/develop `@14582bf` · origin/test `@598d108` (**410 unpushed**) · Open **1 BLOCK QA-B145(active backend)** · Planned **QA-B116+QA-B95 partial** · operation **BLOCK**(QA-B145+QA-B144+origin/test push 410 BE+47 FE+QA-B95).

## uncommitted WIP (develop only — not merged)

| file | change |
|------|--------|
| `LiveE2eBootstrapService.java` | `UUID.randomUUID()` → `scopedFallbackId(kind, organizationId)` for visit-schedule/NHIS-import IDs (+11/-3) |
| `LiveE2eBootstrapServiceTest.java` | org-scoped deterministic fallback regression tests (+119 lines) |

## test delta

| stage | SHA | suites | tests | result |
|-------|-----|--------|-------|--------|
| test baseline | `14582bf` | 295 | 1511 | PASS (TSR 1045차 ~51s) |
| develop HEAD | `14582bf` | 295 | 1511 | carry PASS (1043차; WT dirty — 미재실행) |

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-19T00:55:00+00:00 -->
# develop ↔ test diff 메타 (2026-06-19, 1043차 — test @14582bf · develop @14582bf · MERGE EXECUTED)

> **1043차 재검증 (00:55 UTC) — pre-merge test `@8fe1ccd` `mvn test` **1508/1508 PASS**(295 suites, ~75s) · develop HEAD `@14582bf` `mvn test` **1511/1511 PASS**(295 suites, ~74s) · ★ **develop→test merge EXECUTED**(FF `8fe1ccd`→`14582bf`, 1 commit) · post-merge **1511/1511 PASS**(295 suites, ~67s) · `test..develop` **0 ahead** · origin/develop `@14582bf` · origin/test `@598d108` (**410 unpushed**) · Open **0(active backend)** · Planned **QA-B116+QA-B95** · merge **EXECUTED** · operation **BLOCK**(origin/test push 410 BE+47 FE+QA-B95).

## merged commits (8fe1ccd → 14582bf)

| SHA | message |
|-----|---------|
| `14582bf` | feat(v2/live-e2e): expose G21 seed readiness in probe and bootstrap (QA-B95) |

## changed files (1 commit, 9 files +360/-12)

- `HealthController.java` · `LiveE2eBootstrapResponse.java` · `LiveE2eBootstrapService.java` · `LiveE2eController.java` · `LiveE2eProbeResponse.java`
- `HealthControllerTest.java` · `LiveE2eBootstrapLiveApiRoutingE2eTest.java` · `LiveE2eBootstrapServiceTest.java` · `LiveE2eControllerTest.java`

## test delta

| stage | SHA | suites | tests | result |
|-------|-----|--------|-------|--------|
| pre-merge test | `8fe1ccd` | 295 | 1508 | PASS (TSR 1043차 ~75s) |
| develop HEAD | `14582bf` | 295 | 1511 | PASS (TSR 1043차 ~74s) |
| post-merge test | `14582bf` | 295 | 1511 | PASS (TSR 1043차 ~67s) |

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-19T00:24:00+00:00 -->
# develop ↔ test diff 메타 (2026-06-19, 1042차 — test @8fe1ccd · develop @8fe1ccd · MERGE EXECUTED)

> **1042차 재검증 (00:24 UTC) — pre-merge test `@f932fd3` `mvn test` **1505/1505 PASS**(295 suites, ~71s) · develop HEAD `@8fe1ccd` `mvn test` **1508/1508 PASS**(295 suites, ~73s) · ★ **develop→test merge EXECUTED**(FF `f932fd3`→`8fe1ccd`, 2 commits) · post-merge **1508/1508 PASS**(295 suites, ~68s) · `test..develop` **0 ahead** · origin/develop `@8fe1ccd` · origin/test `@598d108` (**409 unpushed**) · Open **0(active backend)** · Planned **QA-B116+QA-B95** · merge **EXECUTED** · operation **BLOCK**(origin/test push 409 BE+46 FE+QA-B95).

## merged commits (f932fd3 → 8fe1ccd)

| SHA | message |
|-----|---------|
| `54d7f36` | fix(v2/live-e2e): resolve org-scoped bootstrap IDs for visit schedule and NHIS seed |
| `8fe1ccd` | fix(v2/live-e2e): align health readiness with probe credential guards |

## changed files (4 files, +220/-15)

- `HealthController.java` — readiness payload aligns with live-e2e probe credential guards
- `LiveE2eBootstrapService.java` — org-scoped visit schedule/NHIS import batch·row ID resolution
- `HealthControllerTest.java` — readiness guard regression tests
- `LiveE2eBootstrapServiceTest.java` — org-scoped bootstrap ID resolution tests

## test delta

| stage | SHA | suites | tests | result |
|-------|-----|--------|-------|--------|
| pre-merge test | `f932fd3` | 295 | 1505 | PASS (TSR 1042차 ~71s) |
| develop HEAD | `8fe1ccd` | 295 | 1508 | PASS (TSR 1042차 ~73s) |
| post-merge test | `8fe1ccd` | 295 | 1508 | PASS (TSR 1042차 ~68s) |

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-18T23:49:21+00:00 -->
# develop ↔ test diff 메타 (2026-06-18, 1040차 — test @f932fd3 · develop @54d7f36 · MERGE PENDING 1)

> **1040차 재검증 (23:49 UTC) — superseded by 1042차 (merge EXECUTED · post-merge PASS).**
