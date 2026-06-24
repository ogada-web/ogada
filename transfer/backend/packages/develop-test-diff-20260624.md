<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-24T20:03:00+00:00 -->
# develop ↔ test diff 메타 (2026-06-24, 1376차 — test @2eaf17e · develop @2eaf17e SYNCED · merge SKIP)

> **1376차 재검증 (20:03 UTC) — SYNCED revalidation test `@2eaf17e` **1899/1899 PASS**(55.253s, 359 suites, BUILD SUCCESS) · develop `@2eaf17e` WT **CLEAN** · `test..develop` **0**(SYNCED) · merge **SKIP**(SYNCED) · Open **1 carry** QA-B298(MEDIUM · FE live E2E US-O05) · cross-stream **SYNCED(FE@64a7648 + BE@2eaf17e)** · backend@8080 **UP/200** · disk **40%** avail · operation **BLOCK**.**

## test delta (1376차)

| stage | SHA | suites | tests | result |
|-------|-----|--------|-------|--------|
| SYNCED revalidation test | `2eaf17e` | 359 | 1899 | PASS (55.253s) |
| develop WT | `2eaf17e` | — | — | **CLEAN** |
| merge decision | **SKIP** | — | — | 0/0 SYNCED |

## key risk (1376차)

| area | risk |
|------|------|
| origin/test push | 554 BE + 220 FE unpushed — QA-B116 선행 |
| operation | QA-B298 live E2E US-O05 1 FAIL (frontend) · QA-B95 partial |
| cross-stream | SYNCED — FE@64a7648 + BE@2eaf17e |

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-24T20:00:24+00:00 -->
# develop ↔ test diff 메타 (2026-06-24, 1375차 — test @2eaf17e · develop @2eaf17e SYNCED · merge EXECUTED)

> **1375차 재검증 (20:00 UTC) — baseline test `@670756a` **1895/1895 PASS**(60.3s, 358 suites) · develop `@2eaf17e` pre-merge **1899/1899 PASS**(60.5s, 359 suites, +4 tests) WT **CLEAN** · ★ **merge EXECUTED** FF `670756a`→`2eaf17e` (1 commit) · post-merge **1899/1899 PASS**(79.4s) · **★ QA-B299 Fixed** · cross-stream **SYNCED(FE@64a7648 + BE@2eaf17e)** · backend@8080 **UP/200** · operation **BLOCK**.**

## test delta (1375차)

| stage | SHA | suites | tests | result |
|-------|-----|--------|-------|--------|
| baseline test | `670756a` | 358 | 1895 | PASS (60.3s) |
| develop pre-merge | `2eaf17e` | 359 | 1899 | PASS (60.5s, +4 tests) |
| post-merge test | `2eaf17e` | 359 | 1899 | PASS (79.4s) |
| merge | EXECUTED | — | 1 commit | FF `670756a`→`2eaf17e` |

## merged commits (1375차)

| SHA | message |
|-----|---------|
| `2eaf17e` | feat(v2/G2b): add CMS payment method catalog API for silverangel parity |

## key risk (1375차)

| area | risk |
|------|------|
| origin/test push | 554 BE + 220 FE unpushed — QA-B116 선행 |
| operation | QA-B298 live E2E US-O05 1 FAIL (frontend) · QA-B95 partial |
| cross-stream | SYNCED — FE@64a7648 + BE@2eaf17e |

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-24T19:01:00+00:00 -->
# develop ↔ test diff 메타 (2026-06-24, 1373차 — test @670756a · develop @670756a SYNCED · merge EXECUTED)

> **1373차 재검증 (19:01 UTC) — pre-merge test `@88a58d9` **1893/1893 PASS**(85.2s, 358 suites) · develop `@670756a` pre-merge **1895/1895 PASS**(82.7s, 358 suites, +2 tests) WT **CLEAN** · ★ **merge EXECUTED** FF `88a58d9`→`670756a` (3 commits) · post-merge **1895/1895 PASS**(78.5s) · **★ QA-B295 Fixed** · cross-stream **SYNCED(FE@216ab7a + BE@670756a)** · backend@8080 **UP/200** · operation **BLOCK**.**

## test delta (1373차)

| stage | SHA | suites | tests | result |
|-------|-----|--------|-------|--------|
| pre-merge test | `88a58d9` | 358 | 1893 | PASS (85.2s) |
| develop pre-merge | `670756a` | 358 | 1895 | PASS (82.7s, +2 tests) |
| post-merge test | `670756a` | 358 | 1895 | PASS (78.5s) |
| merge | EXECUTED | — | 3 commits | FF `88a58d9`→`670756a` |

## merged commits (1373차)

| SHA | message |
|-----|---------|
| `2f83563` | feat(v2/G-SMS-TEMPLATE-CATALOG): expose ezcareMessageKind on staff dispatch responses |
| `a12873c` | test(v2/G-SMS-TEMPLATE-CATALOG): lock ezcareMessageKind on guardian dispatch routes |
| `670756a` | fix(v2/live-e2e): accept ogada bootstrap env toggle |

## key risk (1373차)

| area | risk |
|------|------|
| origin/test push | 553 BE + 219 FE unpushed — QA-B116 선행 |
| operation | live-e2e bootstrap-disabled carry — QA-B95 partial |

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-24T18:00:00+00:00 -->
# develop ↔ test diff 메타 (2026-06-24, 1371차 — test @88a58d9 · develop @a12873c pending 2 · merge SKIP)

> **1371차 재검증 (18:00 UTC) — roadmap-merged test `@88a58d9` **1893/1893 PASS**(83.0s, 358 suites) · develop `@a12873c` pre-merge **1894/1894 PASS**(84.0s, 358 suites, +1 test) WT **CLEAN** · merge **SKIP**(`test..develop` **0/2** pending `2f83563`+`a12873c`) · **QA-B295 Open update(BLOCK,pending 1→2)** · cross-stream **BLOCK(BE pending 2 @a12873c · FE pending 1 @c7d0982)** · backend@8080 **UP/200** · operation **BLOCK**.**

## test delta (1371차)

| stage | SHA | suites | tests | result |
|-------|-----|--------|-------|--------|
| roadmap-merged test | `88a58d9` | 358 | 1893 | PASS (83.0s) |
| develop pre-merge | `a12873c` | 358 | 1894 | PASS (84.0s, +1 test) |
| merge | SKIP | — | — | `test..develop` 0/2 pending |

## pending commits (1371차)

| SHA | message |
|-----|---------|
| `2f83563` | feat(v2/G-SMS-TEMPLATE-CATALOG): expose ezcareMessageKind on staff dispatch responses |
| `a12873c` | test(v2/G-SMS-TEMPLATE-CATALOG): lock ezcareMessageKind on guardian dispatch routes |

## key risk (1371차)

| area | risk |
|------|------|
| backend transfer gate | test/develop 테스트 모두 PASS이나 develop pending **2**로 test 브랜치 미이관 — 1370차 pending 1에서 확대 |
| cross-stream | FE develop `@c7d0982` pending 1 추가 — 양 스트림 merge gate 동시 BLOCK |

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-24T16:50:30+00:00 -->
# develop ↔ test diff 메타 (2026-06-24, 1370차 — test @88a58d9 · develop @2f83563 pending 1 · merge SKIP)

> **1370차 재검증 (16:50 UTC) — roadmap-merged test `@88a58d9` **1893/1893 PASS**(59.388s, 358 suites) · develop `@2f83563` pre-merge **1893/1893 PASS**(59.267s, 358 suites) WT **CLEAN** · merge **SKIP**(`test..develop` **0/1** pending `2f83563`) · pending commit `feat(v2/G-SMS-TEMPLATE-CATALOG): expose ezcareMessageKind on staff dispatch responses` · **QA-B295 Open(BLOCK)** · cross-stream **BLOCK(BE pending 1 @2f83563 · FE SYNCED@c06d581)** · backend@8080 **UP/200** · operation **BLOCK**.**

## test delta (1370차)

| stage | SHA | suites | tests | result |
|-------|-----|--------|-------|--------|
| roadmap-merged test | `88a58d9` | 358 | 1893 | PASS (59.388s) |
| develop pre-merge | `2f83563` | 358 | 1893 | PASS (59.267s) |
| merge | SKIP | — | — | `test..develop` 0/1 pending |

## pending commit (1370차)

| SHA | message |
|-----|---------|
| `2f83563` | feat(v2/G-SMS-TEMPLATE-CATALOG): expose ezcareMessageKind on staff dispatch responses |

## key risk (1370차)

| area | risk |
|------|------|
| backend transfer gate | test/develop 테스트는 모두 통과했지만 develop pending 1로 test 브랜치 미이관 상태 |

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-24T15:47:47+00:00 -->
# develop ↔ test diff 메타 (2026-06-24, 1368차 — test @88a58d9 · develop @88a58d9 SYNCED · merge EXECUTED)

> **1368차 재검증 (15:47 UTC) — pre-merge test `@ef8bb4e` **1893/1893 PASS**(~58s, 358 suites) · develop `@88a58d9` pre-merge **1893/1893 PASS**(~59s) WT **CLEAN** · ★ **merge EXECUTED** FF `ef8bb4e`→`88a58d9` (1 commit) · post-merge **1893/1893 PASS**(~72s) · **★ QA-B293 Fixed** · cross-stream **BLOCK(BE SYNCED@88a58d9 · FE pending 1 @4adeb1c)** · backend@8080 **UP/200** · operation **BLOCK**.**

## test delta (1368차)

| stage | SHA | suites | tests | result |
|-------|-----|--------|-------|--------|
| pre-merge test | `ef8bb4e` | 358 | 1893 | PASS (~58s) |
| develop pre-merge | `88a58d9` | 358 | 1893 | PASS (~59s) |
| merge | FF `ef8bb4e`→`88a58d9` | — | — | 1 commit |
| post-merge test | `88a58d9` | 358 | 1893 | PASS (~72s) |

## merged commit (1368차)

| SHA | message |
|-----|---------|
| `88a58d9` | test(v2/live-e2e): lock g21 seed detail in health fallback |

## key changes (1368차)

| area | change |
|------|--------|
| `HealthControllerTest` | G21 seed detail UUID assertion lock (+1 line) for live-e2e health fallback regression |

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-24T14:13:22+00:00 -->
# develop ↔ test diff 메타 (2026-06-24, 1366차 — test @ef8bb4e · develop @ef8bb4e SYNCED · merge EXECUTED)

> **1366차 재검증 (14:13 UTC) — pre-merge test `@1d5d441` **1891/1891 PASS**(~57s, 358 suites) · develop `@ef8bb4e` pre-merge **1893/1893 PASS**(~57s, 358 suites, +2 tests) WT **CLEAN** · ★ **merge EXECUTED** FF `1d5d441`→`ef8bb4e` (2 commits) · post-merge **1893/1893 PASS**(~81s) · **★ QA-B292 Fixed** · cross-stream **BLOCK(BE SYNCED@ef8bb4e · FE pending 3 @5a6d42c + QA-B290/B291)** · backend@8080 **UP/200** · operation **BLOCK**.**

## test delta (1366차)

| stage | SHA | suites | tests | result |
|-------|-----|--------|-------|--------|
| pre-merge test | `1d5d441` | 358 | 1891 | PASS (~57s) |
| develop pre-merge | `ef8bb4e` | 358 | 1893 | PASS (~57s, +2 tests) |
| merge | FF `1d5d441`→`ef8bb4e` | — | — | 2 commits |
| post-merge test | `ef8bb4e` | 358 | 1893 | PASS (~81s) |

## merged commits (1366차)

| SHA | message |
|-----|---------|
| `fed6f1f` | fix(v2/G-SMS-TEMPLATE-CATALOG): gate dispatchReady by channel credentials |
| `ef8bb4e` | feat(v2/G-SMS-TEMPLATE-CATALOG): expose ezcareMessageKind on dispatch responses |

## key changes (1366차)

| area | change |
|------|--------|
| `NotificationChannelReadinessService` | dispatchReady credential gate + ezcareMessageKind catalog deepen |
| `BillingClaimNotifyResponse` / `GuardianDocumentNotifyResponse` | ezcareMessageKind field on dispatch responses |
| `NotificationSmsTemplateCatalogServiceTest` | +43 lines catalog/dispatch coverage |
| `MustApiEndpointRoutingTest` / `RoleBasedControllerAccessTest` | routing/RBAC coverage update |

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-24T13:10:05+00:00 -->
# develop ↔ test diff 메타 (2026-06-24, 1364차 — test @1d5d441 · develop @fed6f1f pending 1 · merge SKIP)

> **1364차 재검증 (13:10 UTC) — roadmap-merged test `@1d5d441` **1891/1891 PASS**(59.43s, BUILD SUCCESS) · develop `@fed6f1f` WT **CLEAN** · merge **SKIP**(`test..develop` **0/1** pending `fed6f1f`) · **QA-B292 Open(BLOCK)** · cross-stream **BLOCK(BE pending 1 @fed6f1f · FE pending 2 @9c25d44 + QA-B290/B291)** · backend@8080 **UP/200** · operation **BLOCK**.**

## test delta (1364차)

| stage | SHA | tests | result |
|-------|-----|-------|--------|
| test regression | `1d5d441` | 1891 | PASS (59.43s) |
| develop pending | `fed6f1f` | 미검증 | pending 1 |
| merge | SKIP | — | `test..develop` 0/1 |

## pending commit (1364차)

| SHA | message |
|-----|---------|
| `fed6f1f` | fix(v2/G-SMS-TEMPLATE-CATALOG): gate dispatchReady by channel credentials |

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-24T12:38:25+00:00 -->
# develop ↔ test diff 메타 (2026-06-24, 1362차 — test @1d5d441 · develop @1d5d441 SYNCED · merge EXECUTED)

> **1362차 재검증 (12:38 UTC) — pre-merge test `@b9d0599` **1884/1884 PASS**(~86s, 357 suites) · develop `@1d5d441` pre-merge **1891/1891 PASS**(~86s, 358 suites, +7 tests) WT **CLEAN** · ★ **merge EXECUTED** FF `b9d0599`→`1d5d441` (1 commit) · post-merge **1891/1891 PASS**(~77s) · cross-stream **BLOCK(BE SYNCED@1d5d441 · FE pending 1 @c04968c + QA-B290/B291)** · backend@8080 **UP/200** · operation **BLOCK**.**

## test delta (1362차)

| stage | SHA | suites | tests | result |
|-------|-----|--------|-------|--------|
| pre-merge test | `b9d0599` | 357 | 1884 | PASS (~86s) |
| develop pre-merge | `1d5d441` | 358 | 1891 | PASS (~86s, +7 tests) |
| merge | FF `b9d0599`→`1d5d441` | — | — | 1 commit |
| post-merge test | `1d5d441` | 358 | 1891 | PASS (~77s) |

## merged commit (1362차)

| SHA | message | files |
|-----|---------|-------|
| `1d5d441` | feat(v2/G-SMS-TEMPLATE-CATALOG): wire staff access key SMS dispatch | 13 (+492/-7) |

## key changes (1362차)

| area | change |
|------|--------|
| `StaffAccessKeyNotificationService` | staff access key SMS dispatch wire (new service + 187-line test) |
| `StaffNotificationController` | `POST /api/v1/notifications/staff/access-key` dispatch endpoint |
| `NotificationService` / `AlimtalkFallbackText` | STAFF_ACCESS_KEY template catalog integration |
| `MustApiEndpointRoutingTest` | routing coverage +29 lines |

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-24T11:49:04+00:00 -->
# develop ↔ test diff 메타 (2026-06-24, 1359차 — test @b9d0599 · develop @b9d0599 SYNCED · merge EXECUTED)

> **1359차 재검증 (11:49 UTC) — pre-merge test `@8631d1e` **1879/1879 PASS**(~55s, 355 suites) · develop `@b9d0599` pre-merge **1884/1884 PASS**(~55s, 357 suites, +5 tests) WT **CLEAN** · ★ **merge EXECUTED** FF `8631d1e`→`b9d0599` (1 commit) · post-merge **1884/1884 PASS**(~76s) · cross-stream **SYNCED(FE@068049b + BE@b9d0599)** · backend@8080 **UP/200** · operation **BLOCK**.**

## test delta (1359차)

| stage | SHA | suites | tests | result |
|-------|-----|--------|-------|--------|
| pre-merge test | `8631d1e` | 355 | 1879 | PASS (~55s) |
| develop pre-merge | `b9d0599` | 357 | 1884 | PASS (~55s, +5 tests) |
| merge | FF `8631d1e`→`b9d0599` | — | — | 1 commit |
| post-merge test | `b9d0599` | 357 | 1884 | PASS (~76s) |

## merged commit (1359차)

| SHA | message | files |
|-----|---------|-------|
| `b9d0599` | feat(v2/G-SMS-TEMPLATE-CATALOG): wire staff monthly schedule alimtalk dispatch | 16 (+584/-18) |

## key changes (1359차)

| area | change |
|------|--------|
| `StaffMonthlyScheduleNotificationService` | staff monthly schedule alimtalk dispatch wire (new service + 205-line test) |
| `StaffNotificationController` | `POST /api/v1/notifications/staff/monthly-schedule` dispatch endpoint |
| `NotificationService` / `GuardianNotificationPayloadBuilder` | staff schedule notification channel integration |
| `VisitScheduleRepository` | monthly schedule query for staff dispatch |
| `MustApiEndpointRoutingTest` | routing coverage +37 lines |

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-24T10:31:22+00:00 -->
# develop ↔ test diff 메타 (2026-06-24, 1357차 — test @8631d1e · develop @8631d1e SYNCED · merge EXECUTED)

> **1357차 재검증 (10:31 UTC) — pre-merge test `@fb323ae` **1875/1875 PASS**(~56s, 354 suites) · develop `@8631d1e` pre-merge **1879/1879 PASS**(~55s, 355 suites, +4 tests) WT **CLEAN** · ★ **merge EXECUTED** FF `fb323ae`→`8631d1e` (1 commit) · post-merge **1879/1879 PASS**(~80s) · cross-stream **BLOCK(BE SYNCED@8631d1e · FE pending 2 @ef3948c + pre-merge FAIL QA-B289)** · backend@8080 **UP/200** · operation **BLOCK**.**

## test delta (1357차)

| stage | SHA | suites | tests | result |
|-------|-----|--------|-------|--------|
| pre-merge test | `fb323ae` | 354 | 1875 | PASS (~56s) |
| develop pre-merge | `8631d1e` | 355 | 1879 | PASS (~55s, +4 tests) |
| merge | FF `fb323ae`→`8631d1e` | — | — | 1 commit |
| post-merge test | `8631d1e` | 355 | 1879 | PASS (~80s) |

## merged commit (1357차)

| SHA | message | files |
|-----|---------|-------|
| `8631d1e` | feat(v2/G-SMS-TEMPLATE-CATALOG): wire client monthly schedule alimtalk dispatch | 17 (+403/-11) |

## key changes (1357차)

| area | change |
|------|--------|
| `VisitScheduleNotificationService` | client monthly schedule alimtalk dispatch wire (new service + test) |
| `NotificationEventType` / `AlimtalkTemplateVariables` | schedule notification template variables |
| `MustApiEndpointRoutingTest` | routing coverage +31 lines |
| `application.yml` | notification config flag +1 |

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-24T09:09:00+00:00 -->
# develop ↔ test diff 메타 (2026-06-24, 1355차 — test @fb323ae · develop @fb323ae SYNCED · merge EXECUTED)

> **1355차 재검증 (09:09 UTC) — pre-merge test `@b6c9b16` **1875/1875 PASS**(~56s, 354 suites) · develop `@fb323ae` pre-merge **1875/1875 PASS**(~57s) WT **CLEAN** · ★ **merge EXECUTED** FF `b6c9b16`→`fb323ae` (1 commit) · post-merge **1875/1875 PASS**(~77s) · **★ QA-B287 Fixed** · cross-stream **BLOCK(BE SYNCED@fb323ae · FE pending 1 @15f2195)** · backend@8080 **UP/200** · operation **BLOCK**.**

## test delta (1355차)

| stage | SHA | suites | tests | result |
|-------|-----|--------|-------|--------|
| pre-merge test | `b6c9b16` | 354 | 1875 | PASS (~56s) |
| develop pre-merge | `fb323ae` | 354 | 1875 | PASS (~57s) |
| merge | FF `b6c9b16`→`fb323ae` | — | — | 1 commit |
| post-merge test | `fb323ae` | 354 | 1875 | PASS (~77s) |

## merged commit (1355차)

| SHA | message | files |
|-----|---------|-------|
| `fb323ae` | feat(v2/G-SMS-TEMPLATE-CATALOG): expose dispatch-ready counts in catalog API | 6 (+25/-8) |

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-24T07:40:00+00:00 -->
# develop ↔ test diff 메타 (2026-06-24, 1353차 — test @b6c9b16 · develop @b6c9b16 SYNCED · develop WT DIRTY 5M)

> **1353차 재검증 (07:40 UTC) — ROADMAP merged SYNCED revalidation `@b6c9b16` **1875/1875 PASS**(~56s, 354 suites) · develop `@b6c9b16` WT **DIRTY 5M**(G-SMS-TEMPLATE-CATALOG catalog deepen WIP · +25/-8 lines) · develop dirty WIP **1875/1875 PASS**(~60s) · merge **SKIP**(`test..develop` **0/0** SYNCED+dirty) · **QA-B287 Open(BLOCK)** · cross-stream **BLOCK(BE dirty@b6c9b16 · FE SYNCED@d682562)** · backend@8080 **UP/200** · operation **BLOCK**.**

## dirty WIP delta (1353차 · uncommitted)

| path | change |
|------|--------|
| `notification/api/NotificationTemplateCatalogEntryResponse.java` | catalog entry 필드 deepen |
| `notification/api/NotificationTemplateCatalogResponse.java` | response 메타 추가 |
| `notification/domain/NotificationChannelReadinessService.java` | catalog readiness 연동 deepen |
| `notification/domain/NotificationSmsTemplateCatalogServiceTest.java` | catalog 테스트 보강 |
| `routing/MustApiEndpointRoutingTest.java` | must API 라우팅 검증 조정 |
| `security/RoleBasedControllerAccessTest.java` | RBAC 테스트 보강 |

## test delta (1353차)

| stage | SHA | suites | tests | result |
|-------|-----|--------|-------|--------|
| test regression | `b6c9b16` | 354 | 1875 | PASS (~56s) |
| develop dirty WIP | `b6c9b16` | 354 | 1875 | PASS (~60s) |
| merge | SKIP | — | — | 0/0 SYNCED+dirty |

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-24T06:38:00+00:00 -->
# develop ↔ test diff 메타 (2026-06-24, 1351차 — test @b6c9b16 · develop @b6c9b16 SYNCED · merge EXECUTED)

> **1351차 재검증 (06:38 UTC) — pre-merge test `@9aaefa0` **1872/1872 PASS**(~85s, 353 suites) · develop `@b6c9b16` pre-merge **1875/1875 PASS**(~83s, 354 suites, +3 tests) WT **CLEAN** · ★ **merge EXECUTED** FF `9aaefa0`→`b6c9b16` (1 commit) · post-merge **1875/1875 PASS**(~75s) · **★ QA-B286 Fixed** · cross-stream **BLOCK(BE SYNCED@b6c9b16 · FE pending 1 @596658a+pre-merge FAIL)** · backend@8080 **UP/200** · operation **BLOCK**.**

## test delta (1351차)

| stage | SHA | suites | tests | result |
|-------|-----|--------|-------|--------|
| pre-merge test | `9aaefa0` | 353 | 1872 | PASS (~85s) |
| develop pre-merge | `b6c9b16` | 354 | 1875 | PASS (~83s, +3 tests) |
| merge | FF `9aaefa0`→`b6c9b16` | — | — | 1 commit |
| post-merge test | `b6c9b16` | 354 | 1875 | PASS (~75s) |

## merged commit (1351차)

| SHA | message |
|-----|---------|
| `b6c9b16` | feat(v2/G-SMS-TEMPLATE-CATALOG): add ezCare message_kind Solapi template catalog API |

## changed files (1351차 · merged)

| path | change |
|------|--------|
| `src/main/java/com/ogada/backend/notification/api/NotificationChannelStatusController.java` | template catalog endpoint 추가 |
| `src/main/java/com/ogada/backend/notification/api/NotificationTemplateCatalogEntryResponse.java` | catalog entry DTO 신규 |
| `src/main/java/com/ogada/backend/notification/api/NotificationTemplateCatalogResponse.java` | catalog response DTO 신규 |
| `src/main/java/com/ogada/backend/notification/domain/NotificationChannelReadinessService.java` | catalog readiness 연동 |
| `src/main/java/com/ogada/backend/notification/domain/NotificationSmsTemplateCatalog.java` | ezCare message_kind catalog 도메인 신규 |
| `src/main/java/com/ogada/backend/notification/domain/NotificationTemplateCodes.java` | template code 상수 추가 |
| `src/test/java/com/ogada/backend/notification/domain/NotificationSmsTemplateCatalogServiceTest.java` | catalog 서비스 테스트 신규 |
| `src/test/java/com/ogada/backend/routing/MustApiEndpointRoutingTest.java` | must API 라우팅 검증 추가 |
| `src/test/java/com/ogada/backend/security/RoleBasedControllerAccessTest.java` | RBAC 접근 제어 테스트 추가 |

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-24T05:10:57+00:00 -->
# develop ↔ test diff 메타 (2026-06-24, 1349차 — test @9aaefa0 · develop @9aaefa0 SYNCED · merge EXECUTED)

> **1349차 재검증 (05:10 UTC) — pre-merge test `@d11263b` **1863/1863 PASS**(~58s, 349 suites) · develop `@9aaefa0` pre-merge **1872/1872 PASS**(~60s, 356 suites) WT **CLEAN** · ★ **merge EXECUTED** FF `d11263b`→`9aaefa0` (1 commit) · post-merge **1872/1872 PASS**(~75s) · **★ QA-B284 Fixed** · cross-stream **SYNCED(FE@a43bcb7 + BE@9aaefa0)** · backend@8080 **UP/200** · operation **BLOCK**.**

## test delta (1349차)

| stage | SHA | suites | tests | result |
|-------|-----|--------|-------|--------|
| pre-merge test | `d11263b` | 349 | 1863 | PASS (~58s) |
| develop pre-merge | `9aaefa0` | 356 | 1872 | PASS (~60s) |
| merge | FF `d11263b`→`9aaefa0` | — | — | 1 commit |
| post-merge test | `9aaefa0` | 356 | 1872 | PASS (~75s) |

## merged commit (1349차)

| SHA | message |
|-----|---------|
| `9aaefa0` | feat(v2/FAQ21823): add employment contract compliance API and dashboard counts |

## changed files (1349차 · merged)

| path | change |
|------|--------|
| `src/main/java/com/ogada/backend/dashboard/api/BranchDashboardResponse.java` | dashboard contract compliance count field 추가 |
| `src/main/java/com/ogada/backend/dashboard/domain/DashboardService.java` | dashboard compliance 집계 로직 추가 |
| `src/main/java/com/ogada/backend/staffemploymentcontract/api/StaffEmploymentContractComplianceController.java` | compliance API endpoint 신규 |
| `src/main/java/com/ogada/backend/staffemploymentcontract/api/StaffEmploymentContractComplianceResponse.java` | compliance DTO 신규 |
| `src/main/java/com/ogada/backend/staffemploymentcontract/api/StaffEmploymentContractRenewalAlertResponse.java` | renewal alert DTO 신규 |
| `src/main/java/com/ogada/backend/staffemploymentcontract/domain/StaffEmploymentContractCompliance.java` | compliance 도메인 모델 신규 |
| `src/main/java/com/ogada/backend/staffemploymentcontract/domain/StaffEmploymentContractComplianceService.java` | compliance 서비스 로직 신규 |
| `src/test/java/com/ogada/backend/dashboard/domain/DashboardServiceTest.java` | dashboard compliance 테스트 추가 |
| `src/test/java/com/ogada/backend/routing/MustApiEndpointRoutingTest.java` | must API 라우팅 검증 추가 |
| `src/test/java/com/ogada/backend/security/RoleBasedControllerAccessTest.java` | RBAC 접근 제어 테스트 추가 |
| `src/test/java/com/ogada/backend/staffemploymentcontract/domain/StaffEmploymentContractComplianceServiceTest.java` | service 테스트 신규 |
| `src/test/java/com/ogada/backend/staffemploymentcontract/domain/StaffEmploymentContractComplianceTest.java` | domain 테스트 신규 |

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-24T03:44:19+00:00 -->
# develop ↔ test diff 메타 (2026-06-24, 1347차 — test @d11263b · develop @d11263b SYNCED · merge EXECUTED)

> **1347차 재검증 (03:44 UTC) — pre-merge test `@0494334` **1863/1863 PASS**(~56s, 349 suites) · develop `@d11263b` pre-merge **1863/1863 PASS**(~58s) WT **CLEAN** · ★ **merge EXECUTED** FF `0494334`→`d11263b` (1 commit) · post-merge **1863/1863 PASS**(~75s) · **★ QA-B282 Fixed** · cross-stream **SYNCED(FE@cba9ff8 + BE@d11263b)** · backend@8080 **UP/200** · disk **36%** avail · operation **BLOCK**.**

## test delta (1347차)

| stage | SHA | suites | tests | result |
|-------|-----|--------|-------|--------|
| pre-merge test | `0494334` | 349 | 1863 | PASS (~56s) |
| develop pre-merge | `d11263b` | 349 | 1863 | PASS (~58s) |
| merge | FF `0494334`→`d11263b` | — | — | 1 commit |
| post-merge test | `d11263b` | 349 | 1863 | PASS (~75s) |

## merged commit (1347차)

| SHA | message |
|-----|---------|
| `d11263b` | feat(v2/live-e2e): add explicit operation reason in health and probe |

## changed files (1347차 · merged)

| path | change |
|------|--------|
| `src/main/java/com/ogada/backend/system/HealthController.java` | operation reason in health response |
| `src/main/java/com/ogada/backend/system/LiveE2eController.java` | operation reason in probe |
| `src/main/java/com/ogada/backend/system/LiveE2eProbeResponse.java` | reason field |
| `src/test/java/com/ogada/backend/system/HealthControllerTest.java` | +tests |
| `src/test/java/com/ogada/backend/system/LiveE2eControllerTest.java` | +tests |

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-24T02:39:11+00:00 -->
# develop ↔ test diff 메타 (2026-06-24, 1346차 — test @0494334 · develop @0494334 SYNCED · merge EXECUTED)

> **1346차 재검증 (02:39 UTC) — pre-merge test `@c8358e9` **1857/1857 PASS**(~57s, 349 suites) · develop `@0494334` pre-merge **1863/1863 PASS**(~57s, +6 tests) WT **CLEAN** · ★ **merge EXECUTED** FF `c8358e9`→`0494334` (1 commit) · post-merge **1863/1863 PASS**(~75s) · **★ QA-B281 Fixed** · cross-stream **BLOCK(BE SYNCED@0494334 · FE pending 2 @28033cf)** · backend@8080 **UP/200** · disk **36%** avail · operation **BLOCK**.**

## test delta (1346차)

| stage | SHA | suites | tests | result |
|-------|-----|--------|-------|--------|
| pre-merge test | `c8358e9` | 349 | 1857 | PASS (~57s) |
| develop pre-merge | `0494334` | 349 | 1863 | PASS (~57s, +6 tests) |
| merge | FF `c8358e9`→`0494334` | — | — | 1 commit |
| post-merge test | `0494334` | 349 | 1863 | PASS (~75s) |

## merged commit (1346차)

| SHA | message |
|-----|---------|
| `0494334` | fix(v2/live-e2e): distinguish bootstrap service-unavailable state |

## changed files (1346차 · merged)

| path | change |
|------|--------|
| `src/main/java/com/ogada/backend/system/HealthController.java` | bootstrap service-unavailable distinction |
| `src/main/java/com/ogada/backend/system/LiveE2eController.java` | bootstrap unavailable state handling |
| `src/main/java/com/ogada/backend/system/LiveE2eOperationReadinessSupport.java` | readiness support |
| `src/test/java/com/ogada/backend/system/HealthControllerTest.java` | +tests |
| `src/test/java/com/ogada/backend/system/LiveE2eControllerTest.java` | +tests |
| `src/test/java/com/ogada/backend/system/LiveE2eOperationReadinessSupportTest.java` | +tests |

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-24T01:44:46+00:00 -->
# develop ↔ test diff 메타 (2026-06-24, 1344차 — test @c8358e9 · develop @c8358e9 SYNCED · merge EXECUTED)

> **1344차 재검증 (01:44 UTC) — pre-merge test `@8b3fdcd` **1857/1857 PASS**(~56s, 349 suites) · develop `@c8358e9` pre-merge **1857/1857 PASS**(~58s) WT **CLEAN** · ★ **merge EXECUTED** FF `8b3fdcd`→`c8358e9` (1 commit) · post-merge **1857/1857 PASS**(~75s) · **★ QA-B279 Fixed** · cross-stream **BLOCK(BE SYNCED@c8358e9 · FE pending 1 @0869589)** · backend@8080 **UP/200** · disk **36%** avail · operation **BLOCK**.**

## test delta (1344차)

| stage | SHA | suites | tests | result |
|-------|-----|--------|-------|--------|
| pre-merge test | `8b3fdcd` | 349 | 1857 | PASS (~56s) |
| develop pre-merge | `c8358e9` | 349 | 1857 | PASS (~58s) |
| merge | FF `8b3fdcd`→`c8358e9` | — | — | 1 commit |
| post-merge test | `c8358e9` | 349 | 1857 | PASS (~75s) |

## merged commit (1344차)

| SHA | message |
|-----|---------|
| `c8358e9` | fix(v2/live-e2e): add explicit bootstrap enable hint in readiness responses |

## changed files (1344차 · merged)

| path | change |
|------|--------|
| `src/main/java/com/ogada/backend/system/HealthController.java` | readiness response bootstrap enable hint |
| `src/main/java/com/ogada/backend/system/LiveE2eController.java` | bootstrap enable hint |
| `src/main/java/com/ogada/backend/system/LiveE2eOperationReadinessSupport.java` | bootstrap enable hint |
| `src/main/java/com/ogada/backend/system/LiveE2eProbeResponse.java` | probe field |
| `src/test/java/com/ogada/backend/system/HealthControllerTest.java` | readiness hint tests |
| `src/test/java/com/ogada/backend/system/LiveE2eControllerTest.java` | controller hint tests |

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-24T00:09:00+00:00 -->
# develop ↔ test diff 메타 (2026-06-24, 1343차 — test @8b3fdcd · develop @8b3fdcd SYNCED · merge EXECUTED)

> **1343차 재검증 (00:09 UTC) — pre-merge test `@f600fd6` **1857/1857 PASS**(~56s, 349 suites) · develop `@8b3fdcd` pre-merge **1857/1857 PASS**(~57s) WT **CLEAN** · ★ **merge EXECUTED** FF `f600fd6`→`8b3fdcd` (1 commit) · post-merge **1857/1857 PASS**(~59s) · **★ QA-B277 Fixed** · cross-stream **SYNCED(FE@87da06d + BE@8b3fdcd)** · backend@8080 **UP/200** · disk **35%** avail · operation **BLOCK**.**

## test delta (1343차)

| stage | SHA | suites | tests | result |
|-------|-----|--------|-------|--------|
| pre-merge test | `f600fd6` | 349 | 1857 | PASS (~56s) |
| develop pre-merge | `8b3fdcd` | 349 | 1857 | PASS (~57s) |
| merge | FF `f600fd6`→`8b3fdcd` | — | — | 1 commit |
| post-merge test | `8b3fdcd` | 349 | 1857 | PASS (~59s) |

## merged commit (1343차)

| SHA | message |
|-----|---------|
| `8b3fdcd` | Fix QA-B277: keep live-e2e bootstrap opt-in |

## changed files (1343차 · merged)

| path | change |
|------|--------|
| `src/main/resources/application.yml` | `ogada.live-e2e.bootstrap-enabled` nested default committed (QA-B277 fix) |
