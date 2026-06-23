<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-06T23:19:00+00:00 -->
# develop ↔ test diff 메타 (2026-06-06, 23:19 28차 재검증)

> **28차 재검증 (23:19)**: develop HEAD **`c3f3146` 불변**(COD 18차). working tree **DIRTY** — 1 untracked `SevenRoleJwtLoginE2eTest.java`(384 lines, 7역할 JWT 로그인 E2E WIP). **B02 recurrence #4 Open**(이관 규율 6 위반). HEAD Fixed 규율 5 PASS(PRESENT 유효). `mvn -q test`(test) **79/79 PASS**(28차 실측). 판정 **BLOCK (B02 recurrence #4 + merge 게이트 B01·SEC-007)**.

> **26차 재검증 (22:20)**: COD 18차 `c3f3146` **파일럿 P1–P8·7역할 RBAC API 접근 검증** — TSR 독립 검증. develop HEAD `c3f3146`·working tree **CLEAN**, develop **7커밋** test 앞섬. test `@2799e29` stale. `mvn -q test`(test) **79/79 PASS**·package SUCCESS(76,466,058 B) 재현. develop HEAD `@Test` **183**(24차 154→+29, `PilotChecklistApiAccessTest` 29 @Test). ROADMAP v1 **R-04 @WebMvcTest 65건 진전**. 이관 판정 **BLOCK (merge 게이트 B01·SEC-007 단일)** — R-04 진전, dirty-tree·B02 사유 소멸.

> **24차 재검증 (21:13)**: COD 16차 `aa71412` **Must API 라우팅·RBAC 커버리지 확장** — develop HEAD `aa71412`·CLEAN, develop 6커밋 앞섬. Maven 79/79 PASS. @Test 154. R-02 [x] 승격. BLOCK (B01·SEC-007). (이력)

> **22차 재검증 (20:11)**: COD 15차 `4274459` B02 recurrence #3 Fixed. develop 5커밋 앞섬. Maven 79/79 PASS. @Test 120. BLOCK (B01·SEC-007). (이력)

## 커밋 수준

- `develop` HEAD: `c3f3146` — "test(v1): 파일럿 P1–P8·7역할 RBAC API 접근 검증 (COD 18차)"
- `test` HEAD: `2799e29` — "feat: Spring Boot 3.x 백엔드 초기 구현"
- `git rev-list --count test..develop` = **7**
- `git rev-list --count develop..test` = 0
- `git diff --stat 2799e29 c3f3146` = **42 files, +3211 / -62**

## `2799e29` → `c3f3146` (develop 신규 7커밋, test 미반영)

### 커밋 1 — `7d9d2eb` (SEC/NHIS/Flyway)

| 유형 | 파일 | 요약 | QA |
|------|------|------|-----|
| modified | `pom.xml` | Spring Boot 3.3.1 → 3.5.3 | SEC-004/H02 |
| modified | `billing/domain/NhisExcelParser.java` | `처리상태` 선행열 skip | H01 |
| added | `auth/domain/AuthRateLimitService.java` | rate limit | SEC-001 |
| added | `security/ProductionSecretValidator.java` | prod 시크릿 검증 | SEC-002/006 |
| added | `db/migration/V35`–`V38` | Flyway | — |

### 커밋 2 — `4d476c6` (primaryGuardian·V39·V40)

| 유형 | 파일 | 요약 | QA |
|------|------|------|-----|
| modified | `clients/api/CreateClientRequest.java` | `primaryGuardian` 필수 | B06/US-D01 |
| added | `clients/api/PrimaryGuardianLinkRequest.java` | 보호자 연결 | B06 |
| added | `db/migration/V39`·`V40` | guardian_link_status·branch UK | B06 |

### 커밋 3 — `fac3d07` (guardian billing·NHIS guidance·7-role RBAC)

| 유형 | 파일 | 요약 | ROADMAP |
|------|------|------|---------|
| modified | `billing/api/BillingController.java` | guardian billing API | R-02 PARTIAL |
| added | `billing/domain/NhisImportGuidance.java` | Chrome/Edge 필수 안내 | R-11 PARTIAL |
| added | `security/RoleBasedControllerAccessTest.java` | 7역할 RBAC (7 @Test) | R-04 PARTIAL |

### 커밋 4 — `b5d70a8` (B02 recurrence #1·#2 해소)

| 유형 | 파일 | 요약 | QA |
|------|------|------|-----|
| modified | `security/RoleBasedControllerAccessTest.java` | guardian/client_user RBAC 3 tests | B02 recurrence 해소 |

### 커밋 5 — `4274459` (B02 recurrence #3 Fixed)

| 유형 | 파일 | 요약 | QA |
|------|------|------|-----|
| modified | `billing/domain/NhisImportServiceTest.java` | NHIS import 지점 검증·수동 매칭 테스트 확장 | B02 recurrence #3 |
| modified | `security/RoleBasedControllerAccessTest.java` | billing/guardian RBAC 확장 (+22 @Test) | B02 recurrence #3 |
| added | `billing/api/BillingControllerRoutingTest.java` | Billing 컨트롤러 라우팅 3 @Test | B02 recurrence #3 |

### 커밋 6 — `aa71412` (COD 16차 — Must API 라우팅·RBAC 커버리지 확장)

| 유형 | 파일 | 요약 | ROADMAP |
|------|------|------|---------|
| added | `api/MustApiEndpointRoutingTest.java` | §1–§9 Must 라우팅 26+ @Test (+459 lines) | **R-02 [x] 승격** |
| modified | `security/RoleBasedControllerAccessTest.java` | 7역할 RBAC 커버리지 확장 (+148 lines, 36 @Test) | R-04 PARTIAL |
| (포함) | `security/ProductionSecretValidatorTest.java` | prod secret validator 테스트 (+59 lines) | SEC-002/006 검증 |

### 커밋 7 — `c3f3146` (COD 18차 — 파일럿 P1–P8·7역할 RBAC API 접근 검증)

| 유형 | 파일 | 요약 | ROADMAP |
|------|------|------|---------|
| added | `security/PilotChecklistApiAccessTest.java` | P1–P8·7역할 @WebMvcTest @PreAuthorize 29 @Test (+697 lines) | **R-04 진전** (65건 총계) |

> **26차 이관 규율 5 검증**: `git cat-file -e c3f3146:<path>` — `PilotChecklistApiAccessTest`·`MustApiEndpointRoutingTest`·`RoleBasedControllerAccessTest`·`ProductionSecretValidator`·`AuthRateLimitService`·`NhisExcelParser`·`PrimaryGuardianLinkRequest`·V39·V40 **전부 PRESENT(PASS)**. working tree **CLEAN**(0 dirty).

## 테스트 차이

| 컨텍스트 | 커밋 | 총 테스트 | 결과 |
|----------|------|-----------|------|
| test 브랜치 (src/backend-test) | `2799e29` | 79 (23 suites) | **PASS** (26차 22:20 실측) |
| develop HEAD (read-only) | `c3f3146` | **183** (@Test grep, 커밋됨 — +29 vs 24차) | merge 후 Maven ~183 예상 |
| develop working tree | CLEAN (0 dirty) | 183 | COD 18차 확정 |

## 빌드 산출물 (test 브랜치)

| 항목 | 값 |
|------|-----|
| JAR | `target/backend-0.0.1-SNAPSHOT.jar` |
| 크기 | 76,466,058 bytes |
| Spring Boot | 3.3.1 (test) / 3.5.3 (develop HEAD) |
| 실행 | 2026-06-06T22:20:00+00:00 |

## SEC-007 (test 브랜치 잔존 취약)

| 항목 | test `@2799e29` | develop `@c3f3146` |
|------|-----------------|-------------------|
| `ProductionSecretValidator` | **ABSENT** | PRESENT |
| `DB_PASSWORD:ogada` default | **PRESENT** | 제거(환경변수) |
| Spring Boot | 3.3.1 | 3.5.3 |
| Auth rate limit | **ABSENT** | PRESENT |

> B01 merge 시 SEC-007 동반 해소 예상.

## 이관 판정

**BLOCK** — B02 recurrence #4(Open: SevenRoleJwtLoginE2eTest.java 미커밋) + merge 게이트(B01·SEC-007). dirty-tree(B02 recurrence #4 재발 — 26·27차 CLEAN 이후).
- COD 16차 `aa71412`: Must API 라우팅·RBAC 확장·ProductionSecretValidatorTest (+34 @Test, 154 total)
- 잔여 완료 기준: 7역할 E2E·USER_STORIES P1–P8·REQUIREMENTS §6 체크리스트
