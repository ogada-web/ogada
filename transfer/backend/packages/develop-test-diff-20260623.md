<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-23T17:59:15+00:00 -->
# develop ↔ test diff 메타 (2026-06-23, 1330차 — test @62fce23 · develop @c4e6bcb pending 2 + DIRTY 4M · merge SKIP)

> **1330차 재검증 (17:59 UTC) — test `@62fce23` **1843/1843 PASS**(~80s, 347 suites) · develop `@c4e6bcb` WT **DIRTY 4M**(`ClientService*`·`CreateClientRequest`·`UpdateClientRequest`·`ClientServiceTest`) · merge **SKIP**(`test..develop` **0/2** pending `5fd12dd`+`c4e6bcb` · develop dirty) · **QA-20260623-B272 Planned(update,BLOCK)** · cross-stream **BLOCK(BE dirty pending 2 · FE dirty@426d63a pending 3)** · backend@8080 **UP/200** · disk **34%** avail · operation **BLOCK**.**

## test delta (1330차)

| stage | SHA | suites | tests | result |
|-------|-----|--------|-------|--------|
| test regression | `62fce23` | 347 | 1843 | PASS (~80s) |
| develop HEAD (dirty) | `c4e6bcb` + 4M | — | — | merge SKIP (dirty+pending 2) |
| merge decision | **SKIP** | — | — | `test..develop` 0/2 pending + develop dirty |

## develop dirty files (1330차 — uncommitted WIP)

| path | note |
|------|------|
| `ClientService.java` | client domain address/PII masking WIP |
| `ClientServiceTest.java` | client unit tests |
| `CreateClientRequest.java` | API request DTO |
| `UpdateClientRequest.java` | API request DTO |

## pending commits (1330차)

| SHA | message |
|-----|---------|
| `5fd12dd` | test(v3/US-R01-c): add leave ledger live API routing harness |
| `c4e6bcb` | feat(v3/US-R01-c): add V175 leave ledger integrity and harden dev isolation |

> **1324차 재검증 (16:25 UTC) — test `@62fce23` **1843/1843 PASS**(~68s, 347 suites) · develop dirty WIP `@5fd12dd`+9M+1U **1846/1846 PASS**(~76s, +3 tests) · merge **SKIP**(`test..develop` **0/1** pending + dirty) · **QA-20260623-B272 Planned(carry,BLOCK)** · cross-stream **BLOCK(BE dirty@5fd12dd · FE dirty@8057c1e)** · backend@8080 **UP/200** · disk **36%** avail · operation **BLOCK**.**

## test delta (1324차)

| stage | SHA | suites | tests | result |
|-------|-----|--------|-------|--------|
| test regression | `62fce23` | 347 | 1843 | PASS (~68s) |
| develop dirty WIP | `5fd12dd` + 9M+1U | 347 | 1846 | PASS (~76s, +3 vs test) |
| merge decision | **SKIP** | — | — | `test..develop` 0/1 pending + develop dirty |

## develop dirty files (1324차 — uncommitted WIP)

| path | note |
|------|------|
| `ClientService.java` | client domain WIP |
| `ClientServiceTest.java` | client unit tests |
| `LiveE2eBootstrapService.java` | live-e2e bootstrap WIP |
| `application.yml` | config delta |
| `HealthControllerTest.java` | live-e2e test harness |
| `LiveE2eBootstrapLiveApiRoutingE2eTest.java` | leave-ledger routing |
| `LiveE2eBootstrapServiceTest.java` | bootstrap unit tests |
| `LiveE2eControllerTest.java` | controller tests |
| `LiveE2eOperationReadinessSupportTest.java` | readiness support |
| `V175__staff_leave_ledger_entries_integrity_us_r01c.sql` | untracked migration |

> **1323차 재검증 (15:41 UTC) — test `@62fce23` **1843/1843 PASS**(~72s, 347 suites) · develop `@5fd12dd` WT **DIRTY 6M+1U** · dirty WIP `mvn test` **SKIP**(disk **100%**) · merge **SKIP**(`test..develop` **0/1** pending + dirty) · **QA-20260623-B272 Planned(update,BLOCK)** · cross-stream **BLOCK(BE dirty@5fd12dd · FE dirty@8057c1e)** · backend@8080 **UP/200** · operation **BLOCK**.**

> **1321차 재검증 (14:37 UTC) — test `@62fce23` **1843/1843 PASS**(59.608s, 347 suites) · develop pre-merge `@5fd12dd` **1845/1845 PASS**(56.226s, +2 tests) · merge **SKIP**(`test..develop` **0/1** pending `5fd12dd`) · **QA-20260623-B272 Open(BLOCK)** · cross-stream **BLOCK(BE pending 1 @5fd12dd · FE SYNCED@b7101d5)** · backend@8080 **UP/200** · operation **BLOCK**.**

## test delta (1321차)

| stage | SHA | suites | tests | result |
|-------|-----|--------|-------|--------|
| test regression | `62fce23` | 347 | 1843 | PASS (59.608s) |
| develop pre-merge | `5fd12dd` | 347 | 1845 | PASS (56.226s, +2 tests) |
| merge decision | **SKIP** | — | — | `test..develop` 0/1 pending |

## pending commits (1321차)

| SHA | message |
|-----|---------|
| `5fd12dd` | test(v3/US-R01-c): add leave ledger live API routing harness |

## changed files (pending delta — highlights)

- `LiveE2eBootstrapLiveApiRoutingE2eTest.java` — leave-ledger live API routing harness coverage
- `RoleBasedControllerAccessTest.java` — RBAC routing assertions 강화(+2 tests)

> **1319차 재검증 (14:16 UTC) — pre-merge test `@bb9df48` **1837/1837 PASS**(~91s, 345 suites) · develop pre-merge `@62fce23` **1843/1843 PASS**(~91s, 347 suites, +6 tests) · ★ merge **EXECUTED**(FF `bb9df48`→`62fce23`, 1 commit) · post-merge **1843/1843 PASS**(~74s) · **★ QA-20260623-B271 Fixed @ `62fce23`** · cross-stream **BLOCK(BE SYNCED@62fce23 · FE pre-merge FAIL@b7101d5 QA-B270)** · backend@8080 **UP/200** · operation **BLOCK**.**

## test delta (1319차)

| stage | SHA | suites | tests | result |
|-------|-----|--------|-------|--------|
| pre-merge test | `bb9df48` | 345 | 1837 | PASS (~91s) |
| develop pre-merge | `62fce23` | 347 | 1843 | PASS (~91s, +6 tests) |
| merge decision | **EXECUTED** | — | — | FF `bb9df48`→`62fce23` (1 commit) |
| post-merge test | `62fce23` | 347 | 1843 | PASS (~74s) |

## merged commits (1319차)

| SHA | message |
|-----|---------|
| `62fce23` | test(v3/US-R01-c): add leave ledger pilot flow and RBAC coverage |

## changed files (merge delta — highlights)

- `StaffLeaveLedgerPilotServiceFlowE2eTest.java` — leave ledger pilot E2E flow (+210L)
- `RoleBasedControllerAccessTest.java` — leave-ledger RBAC coverage (+97L)

> **1317차 재검증 (13:01 UTC) — pre-merge test `@f1225b0` **1830/1830 PASS**(~58s, 342 suites) · develop pre-merge `@bb9df48` **1837/1837 PASS**(~60s, 345 suites, +7 tests) · ★ merge **EXECUTED**(FF `f1225b0`→`bb9df48`, 1 commit) · post-merge **1837/1837 PASS**(~76s) · **★ QA-20260623-B269 Fixed @ `bb9df48`** · cross-stream **BLOCK(BE SYNCED@bb9df48 · FE dirty@949e9bf QA-B268)** · backend@8080 **UP/200** · operation **BLOCK**.**

## test delta (1317차)

| stage | SHA | suites | tests | result |
|-------|-----|--------|-------|--------|
| pre-merge test | `f1225b0` | 342 | 1830 | PASS (~58s) |
| develop pre-merge | `bb9df48` | 345 | 1837 | PASS (~60s, +7 tests) |
| merge decision | **EXECUTED** | — | — | FF `f1225b0`→`bb9df48` (1 commit) |
| post-merge test | `bb9df48` | 345 | 1837 | PASS (~76s) |

## merged commits

| SHA | message |
|-----|---------|
| `bb9df48` | feat(v3/US-R01-c): add canonical staff leave ledger API |

## changed files (merge delta — highlights)

- `StaffLeaveLedgerController.java` — canonical leave ledger REST API (list/create/update)
- `StaffLeaveLedgerService.java` — leave ledger domain service (+380L)
- `V174__staff_leave_ledger_us_r01c.sql` — staff leave ledger schema migration
- `StaffLeaveLedgerServiceTest.java` — service unit tests (+182L)
- `MustApiEndpointRoutingTest.java` — routing coverage (+52L)
- `StaffAnnualLeaveSupport.java` / `StaffWorkAttendanceSupport.java` — relatedSurfaces cross-link metadata

> **1315차 재검증 (11:49 UTC) — pre-merge test `@40ab9e7` **1829/1829 PASS**(~83s, 342 suites) · develop pre-merge `@f1225b0` **1830/1830 PASS**(~80s, 342 suites, +1 test) · ★ merge **EXECUTED**(FF `40ab9e7`→`f1225b0`, 1 commit) · post-merge **1830/1830 PASS**(~71s) · **★ QA-20260623-B267 Fixed @ `f1225b0`** · cross-stream **SYNCED(FE@949e9bf + BE@f1225b0)** · backend@8080 **UP/200** · operation **BLOCK**.**

## test delta (1315차)

| stage | SHA | suites | tests | result |
|-------|-----|--------|-------|--------|
| pre-merge test | `40ab9e7` | 342 | 1829 | PASS (~83s) |
| develop pre-merge | `f1225b0` | 342 | 1830 | PASS (~80s, +1 test) |
| merge decision | **EXECUTED** | — | — | FF `40ab9e7`→`f1225b0` (1 commit) |
| post-merge test | `f1225b0` | 342 | 1830 | PASS (~71s) |

## merged commits (1315차)

| SHA | message |
|-----|---------|
| `f1225b0` | test(v2/G2): verify CMS branch roster status filter normalization |
