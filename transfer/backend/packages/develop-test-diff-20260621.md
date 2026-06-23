<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-22T00:10:54+00:00 -->
# develop ↔ test diff 메타 (2026-06-22, 1255차 — test @479995e · develop @479995e · merge EXECUTED)

> **1255차 재검증 (00:10 UTC) — pre-merge test `@abddbee` **1773/1773 PASS**(~80s, 333 suites) · develop `@479995e` pre-merge **1780/1780 PASS**(~80s, 334 suites) · ★ **merge EXECUTED**(FF `abddbee`→`479995e`, 1 commit) · post-merge **1780/1780 PASS**(~75s) · **★ QA-B231 Fixed @ `479995e`** · Open **0(active backend)** · cross-stream **SYNCED(FE@dfa981c + BE@479995e)** · operation **BLOCK**.

## test delta (1255차)

| stage | SHA | suites | tests | result |
|-------|-----|--------|-------|--------|
| test baseline | `abddbee` | 333 | 1773 | PASS (~80s) |
| develop pre-merge | `479995e` | 334 | 1780 | PASS (~80s) |
| post-merge test | `479995e` | 334 | 1780 | PASS (~75s) |
| branch divergence | `test..develop` | - | - | `0/0` SYNCED |
| merge decision | **EXECUTED** | - | - | FF 1 commit |

## merged commit (1255차)

| SHA | message |
|-----|---------|
| `479995e` | feat(v2/G-BILLING): persist billing report filters per month and branch |

## changed files (merged `479995e`)

| file | status |
|------|--------|
| `src/main/java/com/ogada/backend/billing/api/BillingController.java` | modified |
| `src/main/java/com/ogada/backend/billing/api/BillingReportFilterItemResponse.java` | added |
| `src/main/java/com/ogada/backend/billing/api/BillingReportFiltersResponse.java` | added |
| `src/main/java/com/ogada/backend/billing/api/SaveBillingReportFilterRequest.java` | added |
| `src/main/java/com/ogada/backend/billing/domain/BillingReportFilterService.java` | added |
| `src/main/java/com/ogada/backend/billing/persistence/BillingReportFilterEntity.java` | added |
| `src/main/java/com/ogada/backend/billing/persistence/BillingReportFilterRepository.java` | added |
| `src/main/resources/db/migration/V170__billing_report_filters.sql` | added |
| `src/test/java/com/ogada/backend/billing/domain/BillingReportFilterServiceTest.java` | added |
| `src/test/java/com/ogada/backend/routing/MustApiEndpointRoutingTest.java` | modified |
| `src/test/java/com/ogada/backend/security/RoleBasedControllerAccessTest.java` | modified |

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-21T22:58:00+00:00 -->
# develop ↔ test diff 메타 (2026-06-21, 1252차 — test @abddbee · develop @abddbee · merge EXECUTED)

> **1252차 재검증 (22:58 UTC) — pre-merge test `@a6eb8b7` **1770/1770 PASS**(~54s, 333 suites) · develop `@abddbee` pre-merge **1773/1773 PASS**(~56s, 333 suites) · ★ **merge EXECUTED**(FF `a6eb8b7`→`abddbee`, 1 commit) · post-merge **1773/1773 PASS**(~75s) · **★ QA-B229 Fixed @ `abddbee`** · Open **0(active backend)** · cross-stream **SYNCED(FE@5fd468b + BE@abddbee)** · operation **BLOCK**.

## test delta (1252차)

| stage | SHA | suites | tests | result |
|-------|-----|--------|-------|--------|
| test baseline | `a6eb8b7` | 333 | 1770 | PASS (~54s) |
| develop pre-merge | `abddbee` | 333 | 1773 | PASS (~56s) |
| post-merge test | `abddbee` | 333 | 1773 | PASS (~75s) |
| branch divergence | `test..develop` | - | - | `0/0` SYNCED |
| merge decision | **EXECUTED** | - | - | FF 1 commit |

## merged commit (1252차)

| SHA | message |
|-----|---------|
| `abddbee` | feat(v2/G-BILLING-DEPOSIT-ORDER-GUARD): apply prior deposit guard before CMS and easy-pay |

## changed files (merged `abddbee`)

| file | status |
|------|--------|
| `src/main/java/com/ogada/backend/billing/cms/domain/CmsService.java` | modified |
| `src/main/java/com/ogada/backend/billing/domain/BillingService.java` | modified |
| `src/main/java/com/ogada/backend/billing/easypay/domain/EasyPayService.java` | modified |
| `src/test/java/com/ogada/backend/billing/cms/domain/CmsServiceTest.java` | modified |
| `src/test/java/com/ogada/backend/billing/domain/BillingServiceTest.java` | modified |
| `src/test/java/com/ogada/backend/billing/easypay/domain/EasyPayServiceTest.java` | modified |

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-21T21:39:33+00:00 -->
# develop ↔ test diff 메타 (2026-06-21, 1249차 — test @10c0daf · develop @a6eb8b7 · merge SKIP)

> **1249차 재검증 (21:39 UTC) — test `@10c0daf` **1769/1769 PASS**(54.035s, 333 suites) · develop `@a6eb8b7` WT **CLEAN** · merge **SKIP**(`test..develop` **0/1** pending) · **QA-B228 Open(BLOCK)** · Open **1(active backend)** · cross-stream **BLOCK(BE pending 1 @a6eb8b7 · FE dirty/pending 8 @ebdf737)** · operation **BLOCK**.

## test delta (1249차)

| stage | SHA | suites | tests | result |
|-------|-----|--------|-------|--------|
| test baseline | `10c0daf` | 333 | 1769 | PASS (54.035s) |
| develop pre-merge | `a6eb8b7` | - | - | not executed (tester read-only, merge pending gate) |
| post-merge test | - | - | - | merge **SKIP** |
| branch divergence | `test..develop` | - | - | `0/1` pending |
| merge decision | **SKIP** | - | - | backend develop→test pending 1 (QA-B228) |

## pending commit (1249차)

| SHA | message |
|-----|---------|
| `a6eb8b7` | feat(v2/G-BILLING-DEPOSIT-ORDER-GUARD): enforce prior-month copay deposit order |

## changed files (pending `a6eb8b7`)

| file | status |
|------|--------|
| `src/main/java/com/ogada/backend/billing/domain/BankDepositImportService.java` | modified |
| `src/main/java/com/ogada/backend/billing/domain/BillingService.java` | modified |
| `src/test/java/com/ogada/backend/billing/domain/BankDepositCopayLifecycleE2eTest.java` | modified |
| `src/test/java/com/ogada/backend/billing/domain/BankDepositImportServiceTest.java` | modified |
| `src/test/java/com/ogada/backend/billing/domain/BillingServiceTest.java` | modified |
| `src/test/java/com/ogada/backend/billing/domain/CopayGuardianNotifyPaymentE2eTest.java` | modified |

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-21T20:45:00+00:00 -->
# develop ↔ test diff 메타 (2026-06-21, 1247차 — test @10c0daf · develop @10c0daf · merge EXECUTED)

> **1247차 재검증 (20:45 UTC) — pre-merge test `@560057f` **1767/1767 PASS**(~80s, 333 suites) · develop `@10c0daf` pre-merge **1769/1769 PASS**(~82s, 333 suites) WT **CLEAN** · ★ **merge EXECUTED**(FF `560057f`→`10c0daf`, 1 commit) · post-merge **1769/1769 PASS**(~70s) · **★ QA-B225 Fixed @ `10c0daf`** · Open **0(active backend)** · Open **1(active frontend)** QA-B226 · cross-stream **BLOCK(FE pending 8 · BE SYNCED@10c0daf)** · operation **BLOCK**.

## test delta (1247차)

| stage | SHA | suites | tests | result |
|-------|-----|--------|-------|--------|
| test baseline | `560057f` | 333 | 1767 | PASS (~80s) |
| develop pre-merge | `10c0daf` | 333 | 1769 | PASS (~82s) |
| post-merge test | `10c0daf` | 333 | 1769 | PASS (~70s) |
| branch divergence (pre) | `test..develop` | - | - | `0/1` pending |
| merge decision | **EXECUTED** | - | - | FF `560057f`→`10c0daf` (1 commit) |

## merged commits (1247차)

| SHA | message |
|-----|---------|
| `10c0daf` | test(v2/attendance): cover manual check-in method validation |

## merged file delta (1247차)

| file | delta | note |
|------|-------|------|
| `StaffWorkAttendanceServiceTest.java` | +69L | manualCheckIn mobile/kiosk method validation 2 @Test |

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-21T19:03:13+00:00 -->
# develop ↔ test diff 메타 (2026-06-21, 1245차 — test @560057f · develop @560057f · merge SKIP · develop DIRTY)

> **1245차 재검증 (19:03 UTC) — test `@560057f` **1767/1767 PASS**(54.428s, 333 suites) · develop `@560057f` WT **DIRTY 1M**(`StaffWorkAttendanceServiceTest.java` +69L) · develop pre-merge(WIP) **1769/1769 PASS**(53.757s) · merge **SKIP**(`test..develop` **0/0** · dirty) · **QA-B225 Open(BLOCK)** · Open **1(active backend)** · cross-stream **BLOCK(FE pending 6/hang · BE dirty)** · operation **BLOCK**.

## test delta (1245차)

| stage | SHA | suites | tests | result |
|-------|-----|--------|-------|--------|
| test baseline | `560057f` | 333 | 1767 | PASS (54.428s) |
| develop pre-merge (WIP) | `560057f` | 333 | 1769 | PASS (53.757s, +2 WIP @Test) |
| branch divergence | `test..develop` | - | - | `0/0` SYNCED |
| merge decision | **SKIP** | - | - | develop WT DIRTY 1M (QA-B225) |

## develop dirty-tree (1245차)

| file | delta | note |
|------|-------|------|
| `StaffWorkAttendanceServiceTest.java` | +69L | `manualCheckInShouldNormalizeCheckInMethod` · `manualCheckInShouldRejectUnsupportedMethod` WIP 미커밋 |

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-21T17:43:12+00:00 -->
# develop ↔ test diff 메타 (2026-06-21, 1242차 — test @560057f · develop @560057f · merge EXECUTED)

> **1242차 재검증 (17:43 UTC) — pre-merge test `@61e1970` **1755/1755 PASS**(55.517s, 328 suites) · develop `@560057f` pre-merge **1767/1767 PASS**(54.674s, 333 suites) · ★ **merge EXECUTED**(FF `61e1970`→`560057f`, 1 commit) · post-merge **1767/1767 PASS**(73.0s) · **★ QA-B224 Fixed @ `560057f`** · Open **0(active backend)** · cross-stream **BLOCK(FE B222 · BE SYNCED)** · operation **BLOCK**.

## test delta (1242차)

| stage | SHA | suites | tests | result |
|-------|-----|--------|-------|--------|
| test baseline | `61e1970` | 328 | 1755 | PASS (55.517s) |
| develop pre-merge | `560057f` | 333 | 1767 | PASS (54.674s) |
| post-merge test | `560057f` | 333 | 1767 | PASS (73.0s) |
| branch divergence (pre) | `test..develop` | - | - | `0/1` pending |
| merge decision | **EXECUTED** | - | - | FF `61e1970`→`560057f` (1 commit) |

## merged commits (1242차)

| SHA | message |
|-----|---------|
| `560057f` | `feat(v2/G-STAFF-WORK-ATTENDANCE): add staff daily check-in/out roster API` |

## changed files (1242차 merge — 15 files, +1141)

| area | note |
|------|------|
| `V169__staff_work_attendance_g_staff_work_attendance.sql` | staff_work_attendance table |
| `StaffWorkAttendanceController/Service` | daily check-in/out roster API |
| `StaffWorkAttendanceLiveApiRoutingE2eTest` | live API routing harness |
| `RoleBasedControllerAccessTest` | StaffWorkAttendanceAccess RBAC |
| `MustApiEndpointRoutingTest` | routing coverage +12 tests |

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-21T14:56:00+00:00 -->
# develop ↔ test diff 메타 (2026-06-21, 1237차 — test @61e1970 · develop @61e1970 · merge EXECUTED)

> **1237차 재검증 (14:56 UTC) — pre-merge test `@56cb5d9` **1743/1743 PASS**(~82s, 325 suites) · develop `@61e1970` pre-merge **1755/1755 PASS**(~81s, 328 suites) · ★ **merge EXECUTED**(FF `56cb5d9`→`61e1970`, 2 commits) · post-merge **1755/1755 PASS**(74.3s) · **★ QA-B223 Fixed @ `61e1970`** · Open **0(active backend)** · cross-stream **BLOCK(FE B222 · BE SYNCED)** · operation **BLOCK**.

## test delta (1237차)

| stage | SHA | suites | tests | result |
|-------|-----|--------|-------|--------|
| test baseline | `56cb5d9` | 325 | 1743 | PASS (~82s) |
| develop pre-merge | `61e1970` | 328 | 1755 | PASS (~81s) |
| post-merge test | `61e1970` | 328 | 1755 | PASS (74.3s) |
| branch divergence (pre) | `test..develop` | - | - | `0/2` pending |
| merge decision | **EXECUTED** | - | - | FF `56cb5d9`→`61e1970` (2 commits) |

## merged commits (1237차)

| SHA | message |
|-----|---------|
| `0c69060` | `feat(v2/attendance): extend daily list with branch roster clientName and status` |
| `61e1970` | `test(v2/attendance): add roster live API routing and RBAC coverage` |

## changed files (1237차 merge)

| file | note |
|------|------|
| `AttendanceItemResponse.java` | roster clientName/status fields |
| `AttendanceService.java` | daily list roster enrichment |
| `AttendanceStatusSupport.java` | **new** status normalization helper |
| `AttendanceControllerRoutingTest.java` | routing coverage +12 tests |
| `AttendanceServiceTest.java` | roster branch coverage |
| `AttendanceStatusSupportTest.java` | **new** unit tests |
| `AttendanceRosterLiveApiRoutingE2eTest.java` | **new** live API E2E harness |
| `RoleBasedControllerAccessTest.java` | RBAC coverage for attendance roster |

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-21T14:00:00+00:00 -->
# develop ↔ test diff 메타 (2026-06-21, 1233차 — test @56cb5d9 · develop @56cb5d9 · merge EXECUTED)

> **1233차 재검증 (14:00 UTC) — pre-merge test `@a45c040` **1741/1741 PASS**(~82s, 325 suites) · develop `@56cb5d9` pre-merge **1743/1743 PASS**(~81s, 325 suites) · ★ **merge EXECUTED**(FF `a45c040`→`56cb5d9`, 2 commits) · post-merge **1743/1743 PASS**(~74s) · **★ QA-B219 Fixed @ `56cb5d9`** · **★ QA-B220 Fixed @ `56cb5d9`** · Open **0(active backend)** · cross-stream **SYNCED(FE@a4ea2d5 + BE@56cb5d9)** · operation **BLOCK**.

## test delta (1233차)

| stage | SHA | suites | tests | result |
|-------|-----|--------|-------|--------|
| test baseline | `a45c040` | 325 | 1741 | PASS (~82s) |
| develop pre-merge | `56cb5d9` | 325 | 1743 | PASS (~81s) |
| post-merge test | `56cb5d9` | 325 | 1743 | PASS (~74s) |
| branch divergence (pre) | `test..develop` | - | - | `0/2` pending |
| merge decision | **EXECUTED** | - | - | FF `a45c040`→`56cb5d9` (2 commits) |

## merged commits (1233차)

| SHA | message |
|-----|---------|
| `018a781` | `fix(v2/live-e2e): prioritize hard operation blockers` |
| `56cb5d9` | `test(v2/live-e2e): align operation blocker expectations with error priority` |

## changed files (1233차 merge)

| file | note |
|------|------|
| `LiveE2eOperationReadinessSupport.java` | hard operation blocker suffix priority |
| `LiveE2eOperationReadinessSupportTest.java` | +22 lines regression coverage |
| `HealthControllerTest.java` | suffix expectation aligned (`staff-bootstrap-error`) |
| `LiveE2eControllerTest.java` | suffix expectation aligned |

## notable state (1233차)

| area | note |
|------|------|
| backend test suite | `src/backend-test` post-merge `mvn test` **1743/1743 PASS** (325 suites) |
| backend branch gate | develop/test **SYNCED @56cb5d9** · `test..develop` **0/0** |
| backend open | **0(active backend)** — QA-B219+B220 Fixed |
| cross-stream | FE develop/test **SYNCED @a4ea2d5** · BE develop/test **SYNCED @56cb5d9** |
| origin/test | STALE @598d108 — **498 unpushed BE** · **144 unpushed FE** |
| operation | **BLOCK** — origin/test push + QA-B95 partial(19 SKIP carry) |

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-21T13:00:00+00:00 -->
# develop ↔ test diff 메타 (2026-06-21, 1231차 — test @a45c040 · develop @018a781 · merge SKIP)

> **1231차 재검증 (13:00 UTC) — test `@a45c040` **1741/1741 PASS**(~78.5s, 325 suites) · develop `@018a781` pre-merge **1741/1743 FAIL**(~83.7s, 325 suites; 2 FAIL) · merge **SKIP**(`test..develop` **0/1** pending `018a781` + develop HEAD regression) · **QA-B219 Open** · **QA-B220 Open** · Open **2(active backend)** · cross-stream **BLOCK(FE B218 dirty · BE B219+B220)** · operation **BLOCK**.

## test delta (1231차)

| stage | SHA | suites | tests | result |
|-------|-----|--------|-------|--------|
| test baseline | `a45c040` | 325 | 1741 | PASS (~78.5s) |
| develop pre-merge | `018a781` | 325 | 1743 | **1741/1743 FAIL** (~83.7s; 2 FAIL) |
| post-merge test | — | — | — | merge **SKIP** |
| branch divergence (pre) | `test..develop` | - | - | `0/1` pending |
| merge decision | **SKIP** | - | - | develop HEAD regression blocks merge |

## pending commits (1231차)

| SHA | message | blocker |
|-----|---------|---------|
| `018a781` | `fix(v2/live-e2e): prioritize hard operation blockers` | QA-B219 (develop HEAD 2 FAIL) |

## notable state (1231차)

| area | note |
|------|------|
| backend test suite | `src/backend-test` baseline `mvn test` **1741/1741 PASS** (325 suites) |
| backend branch gate | develop **0/1 ahead** of test · develop pre-merge **2 FAIL** |
| backend open | **2(active backend)** — QA-B219(regression) + QA-B220(merge pending blocked) |
| cross-stream | FE develop WT **DIRTY 3M** (QA-B218 carry) · BE merge **SKIP** |
| origin/test | STALE @598d108 — **496 unpushed** BE · FE **143 unpushed** |
