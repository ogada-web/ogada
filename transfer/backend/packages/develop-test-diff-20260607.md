<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-07T15:30:00+00:00 -->
# develop ↔ test diff 메타 (2026-06-07, 62차 재검증)

> **62차 재검증 (15:30 UTC) — develop HEAD `136239e` CLEAN·v2/J03 Solapi 추가·152/152·test 79/79·4커밋 ahead·merge 미실행·BLOCK(merge 게이트)**: develop HEAD **`136239e`**(+1커밋 vs 60차 `3f9264f` — `feat(v2/J03): Solapi alimtalk provider, guardian phone storage, billing notify`), working tree **CLEAN**. test `mvn test` **79/79 PASS**(23 suites, Boot 3.3.1). develop HEAD `mvn test` **152/152 PASS**(+5 vs 60차 147 — SolapiKakaoAlimtalkProviderTest 80 lines + NotificationServiceTest 244 lines + PhoneMaskingUtilTest 24 lines + NotificationPreferenceServiceTest 확장). develop **4커밋 ahead** (`f47ffa1`·`cf6116c`·`3f9264f`·`136239e`) — merge 미실행. **Open 0건**. 판정 **BLOCK**(merge 게이트).

> **60차 재검증 (14:55 UTC) — develop HEAD `3f9264f` CLEAN·BE-10 Fixed·147/147·test 79/79·3커밋 ahead·merge 미실행·BLOCK(merge 게이트)**: develop HEAD **`3f9264f`**(+2커밋 vs 58차 — `cf6116c` BE-10·`3f9264f` v2/J03), working tree **CLEAN**. **QA-B10 develop HEAD Fixed(TSR 독립 검증 PASS)**. develop `mvn test` **147/147 PASS**·test **79/79 PASS**(23 suites, Boot 3.3.1). develop **3커밋 ahead** — merge 미실행. **Open 0건**. 판정 **BLOCK**(merge 게이트).

> **56차 재검증 (10:01 UTC) — 54차 CLEAN→DIRTY 재오염(J01 WIP·27 files)·신규 BLOCK QA-B09**: develop HEAD **`428ba7d` 불변**, working tree **CLEAN→DIRTY** — **15M+12U=27 files**: `GuardianInvitationController`+DTO 4·`GuardianInvitationService`·`InvitationTokenService`·`InvitationExpiredException`·`GuardianInvitationEntity/Repository`·`V43`·`GuardianInvitationServiceTest` untracked; `ClientController/Response/Service`·`GlobalExceptionHandler`·`SecurityConfig`·test 10종 modified. `GuardianInvitationController`·`V43` HEAD ABSENT(이관 규율 6·8). test `mvn test` **213/213 PASS**(75 suites, 56차 실측). develop **3커밋 ahead** — merge 미실행. **신규 Open 1건(BLOCK — QA-B09)**. 판정 **BLOCK** — dirty-tree PASS 금지.

> **56차 재검증 (10:01 UTC) — 54차 CLEAN→DIRTY 재오염(J01 WIP·27 files)·신규 BLOCK QA-B09**: develop HEAD **`428ba7d` 불변**, working tree **CLEAN→DIRTY** — **15M+12U=27 files**: `GuardianInvitationController`+DTO 4·`GuardianInvitationService`·`InvitationTokenService`·`InvitationExpiredException`·`GuardianInvitationEntity/Repository`·`V43`·`GuardianInvitationServiceTest` untracked; `ClientController/Response/Service`·`GlobalExceptionHandler`·`SecurityConfig`·test 10종 modified. `GuardianInvitationController`·`V43` HEAD ABSENT(이관 규율 6·8). test `mvn test` **213/213 PASS**(75 suites, 56차 실측). develop **3커밋 ahead** — merge 미실행. **신규 Open 1건(BLOCK — QA-B09)**. 판정 **BLOCK** — dirty-tree PASS 금지.

> **54차 재검증 (18:23 KST) — COD 36 `428ba7d` B02 #6·B08 #2 Fixed·develop CLEAN·merge 3커밋 ahead**: develop HEAD `c3b8716`→**`428ba7d`**(+1커밋), working tree **DIRTY→CLEAN**. test `mvn test` **213/213 PASS**·develop HEAD **253/253 PASS**(92 suites)·JAR **82,868,029 B**. develop **3커밋 ahead** — merge 미실행. **신규 Open 0건** — dirty-tree **소멸**, Planned BLOCK **merge 단일**. 판정 **BLOCK**.

> **53차 재검증 (17:32 KST) — 51차 대비 HEAD·dirty-tree·merge 불변·WT +1 test·coder 미조치**: develop HEAD **`c3b8716` 불변**·working tree **DIRTY 불변**(2 untracked). test `mvn test` **213/213 PASS**·develop WT **253/253 PASS**(+1, domain test 4 @Test)·JAR **82,868,029 B**. develop **2커밋 ahead** — merge 미실행. **신규 Open 0건** — Planned BLOCK **merge + B02 #6 + B08 #2**. 판정 **BLOCK**.

> **51차 재검증 (16:58 KST) — 50차 대비 상태 완전 불변·coder 미조치·ROADMAP COD 35 false Fixed**: develop HEAD **`c3b8716` 불변**·working tree **DIRTY 불변**(2 untracked). test `mvn test` **213/213 PASS**·develop WT **252/252 PASS**·JAR **82,868,029 B**. develop **2커밋 ahead** — merge 미실행. **⚠ ROADMAP v1 QA-B02·v2 B08 `[x]`(COD 35) TSR FAIL**. **신규 Open 0건** — Planned BLOCK **merge + B02 #6 + B08 #2**. 판정 **BLOCK**.

> **50차 재검증 (16:15 KST) — 48차 CLEAN→DIRTY 재오염·HEAD Fixed 유지·Open 1 BLOCK**: 48차(`c3b8716` CLEAN) 대비 develop HEAD **불변**·working tree **CLEAN→DIRTY** — 2 untracked: `V42__guardian_notification_preferences_consent_temporal.sql`(54 lines, consent CHECK) + `NotificationPreferenceServiceTest.java`(128 lines, 3 @Test). `git cat-file -e HEAD:` B02 #5·B08 **PRESENT** · V42·domain test **ABSENT**. test `mvn test` **213/213 PASS**·develop WT **252/252 PASS**(+3)·JAR **82,868,029 B**. develop **2커밋 ahead of test** — merge 미실행. **신규 Open 1건(BLOCK)**. 판정 **BLOCK** — dirty-tree PASS 금지.

> **48차 재검증 (15:35 KST) — COD 32차 B02 #5·B08 정식 Fixed TSR 독립 검증 PASS·dirty-tree 소멸**: 46차(dirty-tree 3M+4U·COD false Fixed) 대비 **develop 전진·CLEAN 회복**. develop HEAD `e8750d2`→**`c3b8716`**(+2커밋). develop working tree **CLEAN**. develop committed `mvn test` **249/249 PASS**. test **213/213 PASS**. 판정 **BLOCK**(merge 게이트 단일).

> **46차 재검증 (14:30 KST)**: 44·45차 대비 **dirty-tree 확대·WT +6 tests·coder 미조치·신규 Open 0건**. develop·test HEAD **동일 `@e8750d2`**. test `mvn test` **213/213 PASS**(75 suites)·develop WT **249/249 PASS**(91 suites, +6 vs 44차)·JAR **82,868,029 B**. develop WT **DIRTY 확대** — 44차 1M+4U → **3M+4U**: ① `.gitignore` ② **modified** `MustApiEndpointRoutingTest`(+64, B08 notification routing) · `RoleBasedControllerAccessTest`(+93, B08 RBAC) ③ untracked B02 #5 + B08(7 java + V41 + **8 @Test**). **COD Fixed TSR 검증 FAIL** — HEAD ABSENT. HEAD `@Test` **199**·WT surefire **249**(+36). 판정 **BLOCK**.

> **44차 재검증 (04:59 KST)**: 42·43차 대비 **HEAD·dirty-tree 구조 불변·coder 미조치·신규 Open 0건**. develop·test HEAD **동일 `@e8750d2`**. test `mvn test` **213/213 PASS**(75 suites)·develop WT **243/243 PASS**(88 suites)·JAR **82,868,029 B**. develop WT **DIRTY** — ① **1M** `.gitignore`(+`data/backups/`) ② **4 untracked** B02 #5 + B08(notification **8 @Test**). **COD Fixed TSR 검증 FAIL** — HEAD ABSENT. HEAD `@Test` **199**·WT **229**(+30). 판정 **BLOCK**.

> **42차 재검증 (13:25 KST)**: 40·41차 대비 **HEAD·dirty-tree 구조 불변·coder 미조치·신규 Open 0건**. develop·test HEAD **동일 `@e8750d2`**. test `mvn test` **213/213 PASS**(75 suites)·develop WT **243/243 PASS**(88 suites, **+3 vs 40차**)·JAR **82,868,029 B**. develop WT **DIRTY** — ① **1M** `.gitignore`(+`data/backups/`) ② **4 untracked** B02 #5 + B08(notification **8 @Test**, 40차 5→42차 8). **COD Fixed TSR 검증 FAIL** — HEAD ABSENT. HEAD `@Test` **199**·WT **229**(+30). 판정 **BLOCK**.

> **40차 재검증 (12:45 KST)**: 38차 대비 **부분 변화·COD false Fixed 재확인·신규 Open 0건**. develop·test HEAD **동일 `@e8750d2`**. test `mvn test` **213/213 PASS**(75 suites)·develop WT **240/240 PASS**(+27)·JAR **82,868,029 B**. develop WT **DIRTY** — ① **1M** `.gitignore`(+`data/backups/`) ② **4 untracked** B02 #5 + B08. **COD Fixed TSR 검증 FAIL** — HEAD ABSENT. `data/backups/` untracked **소멸**. HEAD `@Test` **199**·WT **226**. 판정 **BLOCK**.

> **38차 재검증 (12:05 KST)**: 36·37차 대비 **상태 불변·coder 미조치·신규 Open 0건**. develop·test HEAD **동일 `@e8750d2`**. test `mvn test` **213/213 PASS**(75 suites, 0 fail)·JAR **82,868,029 B** 재현. develop WT **DIRTY** — B02 #5 `PilotChecklistJwtE2eTest`(634 lines/22 @Test) + B08 notification WIP(6 java + V41 + 5 @Test) + `data/backups/` manifest. HEAD `@Test` **199**·WT **226**(+27). 판정 **BLOCK**.

> **36차 재검증 (11:25 KST)**: 34·35차 대비 **상태 불변·coder 미조치·신규 Open 0건**. develop·test HEAD **동일 `@e8750d2`**. test `mvn test` **213/213 PASS**(75 suites, 0 fail)·JAR **82,868,029 B** 재현. develop WT **DIRTY** — B02 #5 `PilotChecklistJwtE2eTest`(22 @Test) + B08 notification WIP(5 @Test) + `data/backups/` manifest. HEAD `@Test` **199**·WT **226**(+27). 판정 **BLOCK**.

> **34차 재검증 (10:45 KST)**: develop·test HEAD **동일 `@e8750d2`** — v1 develop→test **merge 완료**(33차 stale `@2799e29` 해소). test `mvn test` **213/213 PASS**(75 suites, Spring Boot 3.5.3)·JAR 82,868,029 B. SEC-007 test: `ProductionSecretValidator` **PRESENT**. develop working tree **DIRTY 확대** — 4 untracked 그룹(**8 files**): ① `PilotChecklistJwtE2eTest.java`(634 lines, 22 @Test, B02 #5 Planned) ② **v2 notification_preferences WIP**(V41·domain·api·persistence·test 5 @Test — **B08 Planned**). develop HEAD `@Test` **199**·WT grep **225**(+26). 판정 **BLOCK**(dirty-tree).

## 커밋 수준 (56차)

- `develop` HEAD: `428ba7d` — **불변** (54차 대비)
- `test` HEAD: `e8750d2` — **불변**
- `git rev-list --count e8750d2..428ba7d` = **3** (develop ahead)
- develop working tree = **DIRTY 27 files** (54차 CLEAN → 56차 J01 WIP 재오염)
- test `mvn test` = **213/213 PASS** (75 suites, **56차 실측**)

### develop 미커밋 (56차 — QA-B09 BLOCK)

| 파일 | 상태 | HEAD |
|------|------|------|
| `GuardianInvitationController.java` + DTO 4종·Service 3종·Entity/Repository·V43·Test | untracked (12) | ABSENT |
| `ClientController/Response/Service`·`GlobalExceptionHandler`·`SecurityConfig`·test ×10 | modified (15) | PRESENT (이전 버전) |

## 커밋 수준 (54차, 이력)

- `develop` HEAD: `428ba7d` — **+1커밋** (53차 `c3b8716` 대비)
- `test` HEAD: `e8750d2` — **불변**
- `git rev-list --count e8750d2..428ba7d` = **3** (develop ahead)
- develop working tree = **CLEAN** (53차 DIRTY → COD 36차 해소)
- develop HEAD surefire = **253/253** (92 suites, 0 fail)

### develop 3커밋 ahead (test 미반영 — merge 게이트)

| 커밋 | QA | 요약 |
|------|-----|------|
| `428ba7d` | **B02 #6·B08 #2 Fixed** | V42 consent CHECK·temporal + `NotificationPreferenceServiceTest`(4 @Test) |
| `c3b8716` | **B02 #5 Fixed** | `PilotChecklistJwtE2eTest`(634 lines/22 @Test) v1 P1–P8 live Bearer JWT E2E |
| `feac558` | **B08 Fixed** | v2 guardian notification preferences API (9 java + V41 + routing/RBAC) |

## develop 미커밋 (54차)

> **CLEAN** — 미커밋 변경 **0건**. B02 #6·B08 #2 **Fixed @HEAD** (TSR 54차 독립 검증 PASS).

## 커밋 수준 (53차)

- `develop` HEAD: `c3b8716` — **불변** (51차 대비)
- `test` HEAD: `e8750d2` — **불변**
- `git rev-list --count e8750d2..c3b8716` = **2** (develop ahead)
- develop working tree = **DIRTY** (2 untracked — **불변**)
- develop WT surefire = **253/253** (+1 vs 51차 252 — `NotificationPreferenceServiceTest` 4 @Test)

## 커밋 수준 (51차, 이력)

- `develop` HEAD: `c3b8716` — **불변** (50차 대비)
- `test` HEAD: `e8750d2` — **불변**
- `git rev-list --count e8750d2..c3b8716` = **2** (develop ahead)
- develop working tree = **DIRTY** (2 untracked — **불변**)
- ROADMAP COD 35 Fixed 주장 = **false** (HEAD·WT 불변)

## 커밋 수준 (50차, 이력)

- `develop` HEAD: `c3b8716` — 불변 (48차 대비)
- `test` HEAD: `e8750d2` — 불변
- `git rev-list --count e8750d2..c3b8716` = **2** (develop ahead)
- develop working tree = **DIRTY** (2 untracked — 48차 CLEAN→재오염)

## develop 미커밋 (50차)

| 유형 | 경로 | 요약 | QA |
|------|------|------|-----|
| untracked | `db/migration/V42__guardian_notification_preferences_consent_temporal.sql` | kakao/sms consent CHECK·temporal monotonicity (54 lines) | **B08 #2 Planned** — HEAD ABSENT |
| untracked | `notification/domain/NotificationPreferenceServiceTest.java` | domain unit test (8050 B, **4 @Test**) | **B08 #2 Planned** — HEAD ABSENT |

> WT `mvn test` **253/253 PASS**(+4 vs HEAD committed 249). **Open 0건** — B02 #6·B08 #2 **Planned 유지**.

## develop 미커밋 (50차, 이력)

> **CLEAN** — 46차 dirty-tree(3M+4U)가 COD 32차 2커밋으로 전부 커밋. 미커밋 변경 **0건**. 이관 규율 5·6·8 PASS.

## 커밋 수준 (48차, 이력)

### develop 2커밋 ahead (test 미반영 — merge 게이트)

| 커밋 | QA | 요약 |
|------|-----|------|
| `c3b8716` | **B02 #5 Fixed** | `PilotChecklistJwtE2eTest`(634 lines/22 @Test) v1 P1–P8 live Bearer JWT E2E + `.gitignore` |
| `feac558` | **B08 Fixed** | v2 guardian notification preferences API (9 java + V41 + 2 controller test + routing/RBAC 확장) |

## develop 미커밋 (48차)

> **CLEAN** — 46차 dirty-tree(3M+4U)가 COD 32차 2커밋으로 전부 커밋. 미커밋 변경 **0건**. 이관 규율 5·6·8 PASS.

## develop 미커밋 (46차, 이력)

| 유형 | 경로 | 요약 | QA |
|------|------|------|-----|
| modified | `.gitignore` | +`data/backups/` (미커밋) | B02 부분 정리 WIP |
| modified | `api/MustApiEndpointRoutingTest.java` | **+64 lines** — notification preference routing @WebMvcTest | **B08 Planned** — scope 확대 |
| modified | `security/RoleBasedControllerAccessTest.java` | **+93 lines** — notification RBAC @WebMvcTest | **B08 Planned** — scope 확대 |
| untracked | `security/PilotChecklistJwtE2eTest.java` | P1–P8 live Bearer JWT E2E (634 lines, 22 @Test) | **B02 #5 Planned** — COD Fixed **FAIL** |
| untracked | `notification/` (7 java) | Guardian notification preferences API·service | **B08 Planned** — COD Fixed **FAIL** |
| untracked | `db/migration/V41__guardian_notification_preferences.sql` | v2 알림 수신 설정 테이블 | **B08 Planned** |
| untracked | `notification/*Test.java` | **8 @Test** (Guardian 5 + Staff 3) | **B08 Planned** |

> 44차 대비: untracked 4건 **불변** + **신규 modified 2건**(B08). WT surefire **249/249**(+6).

## develop 미커밋 (44차)

| 유형 | 경로 | 요약 | QA |
|------|------|------|-----|
| modified | `.gitignore` | +`data/backups/` (미커밋) | B02 부분 정리 WIP |
| untracked | `security/PilotChecklistJwtE2eTest.java` | P1–P8 live Bearer JWT E2E (634 lines, 22 @Test) | **B02 #5 Planned** — COD Fixed **FAIL** |
| untracked | `notification/` (7 java) | Guardian notification preferences API·service | **B08 Planned** — COD Fixed **FAIL** |
| untracked | `db/migration/V41__guardian_notification_preferences.sql` | v2 알림 수신 설정 테이블 | **B08 Planned** |
| untracked | `notification/*Test.java` | **8 @Test** (Guardian 5 + Staff 3) | **B08 Planned** |

> 42·43차 대비: HEAD·dirty-tree **구조 불변**. COD Fixed **TSR 44차 FAIL** 유지.

## develop 미커밋 (42차)

| 유형 | 경로 | 요약 | QA |
|------|------|------|-----|
| modified | `.gitignore` | +`data/backups/` (미커밋) | B02 부분 정리 WIP |
| untracked | `security/PilotChecklistJwtE2eTest.java` | P1–P8 live Bearer JWT E2E (634 lines, 22 @Test) | **B02 #5 Planned** — COD Fixed **FAIL** |
| untracked | `notification/` (7 java) | Guardian notification preferences API·service | **B08 Planned** — COD Fixed **FAIL** |
| untracked | `db/migration/V41__guardian_notification_preferences.sql` | v2 알림 수신 설정 테이블 | **B08 Planned** |
| untracked | `notification/*Test.java` | **8 @Test** (40차 5→42차 8) | **B08 Planned** |

> 40·41차 대비: HEAD·dirty-tree **구조 불변**. notification WIP @Test **5→8** (+3). COD Fixed **TSR 42차 FAIL** 유지.

## develop 미커밋 (40차, 이력)

| 유형 | 경로 | 요약 | QA |
|------|------|------|-----|
| modified | `.gitignore` | +`data/backups/` (미커밋) | B02 부분 정리 WIP |
| untracked | `security/PilotChecklistJwtE2eTest.java` | P1–P8 live Bearer JWT E2E (634 lines, 22 @Test) | **B02 #5 Planned** — COD Fixed **FAIL** |
| untracked | `notification/` (6 java) | Guardian notification preferences API·service | **B08 Planned** — COD Fixed **FAIL** |
| untracked | `db/migration/V41__guardian_notification_preferences.sql` | v2 알림 수신 설정 테이블 (23 lines) | **B08 Planned** |
| untracked | `notification/api/GuardianNotificationPreferenceControllerTest.java` | 5 @Test | **B08 Planned** |

> 38차 대비: `data/backups/` untracked **소멸** (`.gitignore` WIP). COD Fixed 주장 **TSR 40차 FAIL**.

> 33차 대비 **변화**: test merge 완료·Maven 79→**213** tests. develop dirty **1 file→8 files**(notification v2 WIP 추가).

## `2799e29` → `e8750d2` (8커밋 — **test에 merge 완료**)

| 커밋 | 요약 |
|------|------|
| `7d9d2eb` | NHIS 선행열·SEC·Flyway V35–V38·Boot 3.5.3 |
| `4d476c6` | primaryGuardian 필수·V39·V40 |
| `fac3d07` | guardian billing·NHIS guidance·7-role RBAC |
| `b5d70a8` | guardian/client_user RBAC WebMvcTest |
| `4274459` | NHIS·billing routing·RBAC 테스트 확장 |
| `aa71412` | Must API 라우팅·RBAC 커버리지 |
| `c3f3146` | PilotChecklistApiAccessTest P1–P8 |
| `e8750d2` | SevenRoleJwtLoginE2eTest live JWT E2E |

## Maven (test @e8750d2 — merge 후, 44차)

| 항목 | 결과 |
|------|------|
| `mvn test` (test) | **213/213 PASS** (75 suites, 0 fail) |
| `mvn test` (develop WT) | **243/243 PASS** (88 suites) |
| `mvn -q -DskipTests package` | SUCCESS — **82,868,029 B** |
| Spring Boot (test) | **3.5.3** |
| `@Test` (committed HEAD) | **199** |
| `@Test` (develop WT grep) | **229** (+30 untracked) |

## Maven (test @e8750d2 — merge 후, 42차)

| 항목 | 결과 |
|------|------|
| `mvn test` (test) | **213/213 PASS** (75 suites, 0 fail) |
| `mvn test` (develop WT) | **243/243 PASS** (88 suites; 40차 240→42차 **+3**) |
| `mvn -q -DskipTests package` | SUCCESS — **82,868,029 B** |
| Spring Boot (test) | **3.5.3** |
| `@Test` (committed HEAD) | **199** |
| `@Test` (develop WT grep) | **229** (+30 untracked) |

## Maven (test @e8750d2 — merge 후, 40차, 이력)

| 항목 | 결과 |
|------|------|
| `mvn test` (test) | **213/213 PASS** (75 suites, 0 fail) |
| `mvn test` (develop WT) | **240/240 PASS** (+27 untracked tests) |
| `mvn -q -DskipTests package` | SUCCESS — **82,868,029 B** |
| Spring Boot (test) | **3.5.3** |
| `@Test` (committed HEAD) | **199** |
| `@Test` (develop WT grep) | **226** (+27 untracked) |

## SEC-007 (test @e8750d2)

| 항목 | 32차 (test @2799e29) | 34차 (test @e8750d2) |
|------|----------------------|----------------------|
| `ProductionSecretValidator` | ABSENT | **PRESENT** |
| Spring Boot | 3.3.1 | **3.5.3** |
| Flyway latest | V34 | **V40** |

## 이관 판정 (48차)

**BLOCK** — **develop→test merge 게이트 단일**. B02 #5·B08 정식 Fixed(develop HEAD `c3b8716` PRESENT·working tree CLEAN·committed 249/249 PASS, 이관 규율 5·6·8 PASS)로 **dirty-tree·false Fixed 사유 소멸**. 잔여 = develop 2커밋 ahead(`feac558`·`c3b8716`)이 test 미반영 — develop→test merge 실행 후 PASS 가능. **backend 30+회 dirty-tree/false-Fixed 정체 종결**.
