<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-07T17:22:00+00:00 -->
# develop ↔ test diff 메타 (2026-06-08, 66차 재검증)

> **66차 재검증 (17:22 UTC) — develop `c221531` CLEAN·v2/J03 daily care·emergency health alimtalk E2E·merge 7커밋·develop 169/169·test 79/79·Open 0·BLOCK(merge 게이트 단일)**:
> develop HEAD **`c221531`**(+1커밋 vs 64차 `80bdb1e` — `feat(v2/J03): wire daily care·emergency health notifications and alimtalk E2E tests`), working tree **CLEAN**.
> test HEAD **`2799e29`**(v1 초기 구현 baseline) — ROADMAP v1 merged 기대 **`e8750d2`** 와 **불일치**.
> test `mvn test` **79/79 PASS**(23 suites, Boot 3.3.1). develop HEAD `mvn test` **169/169 PASS**(64차 158 → +11).
> develop **7커밋 ahead** — merge 미실행. **모든 v1 baseline artifacts PRESENT @ c221531(TSR 66차 독립 검증 PASS)**.

> **64차 재검증 (16:30 UTC) — develop `80bdb1e` CLEAN·BE-11 AuthRateLimitService Fixed·V45 Fixed·merge 6커밋·develop 158/158·test 79/79·Open 0·BLOCK(merge 게이트 단일)**:
> develop HEAD **`80bdb1e`**(+2커밋 vs 62차 `136239e` — `8d42bdd` BE-11 AuthRateLimitService · `80bdb1e` V45), working tree **CLEAN**.
> test HEAD **`2799e29`**(v1 초기 구현 baseline) — ROADMAP v1 merged 기대 **`e8750d2`** 와 **불일치**.
> test `mvn test` **79/79 PASS**(23 suites, Boot 3.3.1). develop HEAD `mvn test` **158/158 PASS**.
> develop **6커밋 ahead** — merge 미실행. **BE-11 Fixed @ `8d42bdd`** · **V45 Fixed @ `80bdb1e`** · **SEC-20260608-014 Planned→Fixed**.

## 커밋 수준 (66차)

| 항목 | 값 |
|------|-----|
| `develop` HEAD | `c221531` — `feat(v2/J03): wire daily care·emergency health notifications and alimtalk E2E tests` |
| `test` HEAD | `2799e29` — `feat: Spring Boot 3.x 백엔드 초기 구현` |
| ROADMAP v1 merged 기대 test | `e8750d2` — **미달** (213 tests·Boot 3.5.3·SEC-007) |
| `git rev-list --count test..develop` | **7** |
| develop working tree | **CLEAN** (0 dirty) |
| test working tree | **CLEAN** |

### develop 7커밋 ahead (test 미반영 — merge 게이트)

| 커밋 | QA | 요약 |
|------|-----|------|
| `f47ffa1` | **B09·B08·BE-8 Fixed** | J01 `guardianinvitations/*` + V43 + notification V41–V42 + V35–V40 + SecurityConfig |
| `cf6116c` | **BE-10 Fixed** | v1 baseline 복원 — `PilotChecklistJwtE2eTest`·`MustApiEndpointRoutingTest`·`ProductionSecretValidatorTest`·`SevenRoleJwtLoginE2eTest`·`RoleBasedControllerAccessTest` |
| `3f9264f` | v2/J03 | NotificationService dispatch skeleton + stub providers |
| `136239e` | v2/J03 Solapi | SolapiKakaoAlimtalkProvider·GuardianPhoneStorage·BillingNotifyService·PhoneMaskingUtil |
| `8d42bdd` | **BE-11 Fixed (SEC-D13)** | `AuthRateLimitService` IP+email 슬라이딩 윈도우 60s, login·refresh·reset rate limit, 429 RATE_LIMITED |
| `80bdb1e` | v2 V45 | `V45__v2_notification_prefs_integrity_and_users_phone_pair.sql` — users phone pair·notifications FK·guardian_invitations index |
| `c221531` | v2/J03 | `NotificationAlimtalkDispatchE2eTest`(7 @Test) — daily care·emergency health notifications alimtalk dispatch E2E |

### develop HEAD 산출물 검증 (규율 5, 66차)

| path | HEAD |
|------|------|
| `guardianinvitations/api/GuardianInvitationController.java` | **PRESENT** (f47ffa1) |
| `db/migration/V43__guardian_invitations.sql` | **PRESENT** (f47ffa1) |
| `notification/domain/NotificationPreferenceService.java` | **PRESENT** (f47ffa1) |
| `db/migration/V42__*.sql` | **PRESENT** (f47ffa1) |
| `pilot/PilotChecklistJwtE2eTest.java` | **PRESENT** (cf6116c) |
| `security/SevenRoleJwtLoginE2eTest.java` | **PRESENT** (cf6116c) |
| `security/ProductionSecretValidatorTest.java` | **PRESENT** (cf6116c) |
| `routing/MustApiEndpointRoutingTest.java` | **PRESENT** (cf6116c) |
| `security/RoleBasedControllerAccessTest.java` | **PRESENT** (cf6116c) |
| `auth/domain/AuthRateLimitService.java` | **PRESENT** (8d42bdd) ← **BE-11 Fixed** |
| `auth/domain/AuthRateLimitServiceTest.java` | **PRESENT** (8d42bdd) |
| `db/migration/V45__*.sql` | **PRESENT** (80bdb1e) ← **V45** |

## Maven (64차 실측)

| context | command | result |
|---------|---------|--------|
| test `@2799e29` | `mvn test` | **79/79 PASS** (23 suites) |
| develop `@80bdb1e` | `mvn test` | **158/158 PASS** |
| test package | `mvn -q -DskipTests package` | SUCCESS — JAR **76,466,058 B** |

## 판정

**BLOCK** — merge 게이트(6커밋). BE-11·V45 dirty-tree **소멸**(Fixed @ `8d42bdd`/`80bdb1e`). SEC-20260608-014 **Fixed**.

---

## 이력 — 58차 재검증 (2026-06-07T14:00 UTC)

> develop HEAD **`f47ffa1`**, working tree CLEAN. test **`2799e29`** 79/79. develop **1커밋 ahead**. **QA-B09 Fixed** · **SEC-D8 Fixed** · **신규 Open QA-B10**(v1 merged baseline regression). 판정 **BLOCK**(merge+history).
