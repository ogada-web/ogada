<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-10T02:25:00+00:00 -->
# develop ↔ test diff 메타 (2026-06-10, 173차 — develop WT DIRTY 3 · test @598d108 불변)

> **173차 재검증 (02:25 UTC) — test `@598d108` CLEAN·origin/test 동기화·246/246 PASS·develop `06d68dd` HEAD **불변**·WT **DIRTY 3**(2M+1U: `CmsService.java`+12/-1·`CmsServiceTest.java`+19·`V62` untracked — G2 CMS billing claim snapshot WIP, **171차 CLEAN→재오염**)·HEAD **362/362 PASS**·WT **363/363 PASS**(+1 @Test)·34 ahead·origin/develop @ `06d68dd`·PASS(v1)·⚠ **Open 1 BLOCK(QA-20260610-B13)**·**v1.2.1 merge BLOCK**:
> develop HEAD **`06d68dd`** 불변(fee schedule forward-only guard @ 171차 HEAD). WT **DIRTY 3** — `CmsService.java`(+12/-1: G2 CMS billing claim duration_band snapshot logic)·`CmsServiceTest.java`(+19: +1 @Test)·`V62__billing_claim_item_duration_band_snapshot.sql`(untracked). **171차 CLEAN→재오염**.
> develop HEAD **362/362 PASS**(83 suites)·WT **363/363 PASS**(83 suites, +1 @Test). develop **34커밋 ahead** — v1.2.1 merge gate **BLOCK**(WT dirty·QA-20260610-B13). **COD 액션**: G2 CMS billing claim snapshot WIP 커밋 → WT clean → merge(34) UNBLOCK.

> **171차 재검증 (01:36 UTC) — test `@598d108` CLEAN·origin/test 동기화·246/246 PASS·develop `06d68dd`(+1 vs `425a05f`: `fix(billing): enforce forward-only fee schedule versions` — `BillingService`·`BillingServiceTest` +57, 361→362 +1 @Test) WT **CLEAN**·362/362 PASS·34 ahead·origin/develop @ `06d68dd`·PASS(v1)·Open 0(backend)·★ **v1.2.1 merge FULLY UNBLOCKED**:
> develop HEAD **`06d68dd`**(+1: fee schedule forward-only version guard — `BillingService`·`BillingServiceTest` +57 lines).
> develop `mvn test` **362/362 PASS**(83 suites). develop **34커밋 ahead** — v1.2.1 merge gate **FULLY UNBLOCKED**. fee schedule version monotonicity @ HEAD.

> **169차 재검증 (01:15 UTC) — test `@598d108` CLEAN·origin/test 동기화·246/246 PASS·develop `425a05f`(+1 vs `f23f15a`: `feat(v2/G9): add duration_band to fee schedules and client billing lookup`) WT **CLEAN**·361/361 PASS·33 ahead·origin/develop @ `425a05f`·PASS(v1)·Open 0(backend)·★ **v1.2.1 merge FULLY UNBLOCKED**:
> develop HEAD **`425a05f`**(+1: G9 duration_band — `DurationBand`·`V61__fee_schedules_duration_band.sql`·`FeeScheduleDurationBandTest`·`DurationBandTest`·`BillingService`·`ClientService`, 16 files +419/-15, 355→361 +6 @Test).
> develop `mvn test` **361/361 PASS**(83 suites). develop **33커밋 ahead** — v1.2.1 merge gate **FULLY UNBLOCKED**. G9 duration_band @ HEAD — FE 연동·ROADMAP G9 반영 P1 잔여(planner).

> **167차 재검증 (00:52 UTC) — test `@598d108` CLEAN·origin/test 동기화·246/246 PASS·develop `f23f15a`(+1 vs `6ed48ff`: `fix(v2/G2): harden SMTP email validation in SmtpEmailProvider`) WT **CLEAN**·355/355 PASS·32 ahead·origin/develop @ `f23f15a`·PASS(v1)·Open 0(backend)·★ **v1.2.1 merge FULLY UNBLOCKED**:
> develop HEAD **`f23f15a`**(+1: G2 SMTP email validation hardening — `SmtpEmailProvider`·`SmtpEmailProviderTest`, 353→355 +2 @Test). **QA-20260610-B12 Fixed** — 165차 DIRTY 2M WIP 커밋됨.
> develop `mvn test` **355/355 PASS**(81 suites). develop **32커밋 ahead** — v1.2.1 merge gate **FULLY UNBLOCKED**. G2 SMTP validation @ HEAD — 실 SMTP credentials·운영 발송 P1 잔여.

> **165차 재검증 (00:32 UTC) — test `@598d108` CLEAN·origin/test 동기화·246/246 PASS·develop `6ed48ff` HEAD **불변**·WT **DIRTY 2M**·HEAD **353/353 PASS**·WT **355/355 PASS**(+2)·31 ahead·origin/develop @ `6ed48ff`·PASS(v1)·Open 1 BLOCK·⚠ **v1.2.1 merge BLOCK**:
> develop HEAD **`6ed48ff`** 불변(163차 G2 SMTP + V60 CMS FK @ HEAD). WT **DIRTY 2M** — `SmtpEmailProvider.java`(+54/-2: `SIMPLE_EMAIL_PATTERN`·`requireConfiguredEmail`·invalid-email skip)·`SmtpEmailProviderTest.java`(+37: email validation hardening). **163차 CLEAN→재오염**. develop HEAD **353/353 PASS**(81 suites)·WT **355/355 PASS**(+2 @Test). develop **31커밋 ahead** — v1.2.1 merge gate **BLOCK**(QA-20260610-B12).

> **163차 재검증 (00:12 UTC) — test `@598d108` CLEAN·origin/test 동기화·246/246 PASS·develop `6ed48ff`(+1 vs 161차 `2c6e57e`) WT **CLEAN**·353/353 PASS·31 ahead·origin/develop @ `6ed48ff`·PASS(v1)·Open 0(backend)·★ **v1.2.1 merge FULLY UNBLOCKED**:
> develop HEAD **`6ed48ff`**(`feat(v2/G2): add SMTP email provider and CMS tenant FK backing` — `SmtpEmailProvider`·`NotificationConfig`/`NotificationProperties`·`application.yml`·`pom.xml`·`V60__cms_enrollment_tenant_fk_backing.sql`·`SmtpEmailProviderTest`, 7 files +361, 350→353 +3 @Test). **QA-20260610-B11 Fixed** — 161차 DIRTY 7 WIP 전부 커밋됨.
> develop `mvn test` **353/353 PASS**(81 suites). develop **31커밋 ahead** — v1.2.1 merge gate **FULLY UNBLOCKED**. G2 SMTP provider skeleton — 실 SMTP credentials·운영 발송 P1 잔여.

> **161차 재검증 (23:51 UTC) — test `@598d108` CLEAN·origin/test 동기화·246/246 PASS·develop `2c6e57e` HEAD **불변**·WT **DIRTY 7**(4M+3U: G2 SMTP·V60 CMS FK WIP, 159차 CLEAN→**재오염**)·develop HEAD **350/350 PASS**·WT **353/353 PASS**(+3)·30 ahead·origin/develop @ `2c6e57e`·PASS(v1)·Open 1 BLOCK·⚠ **v1.2.1 merge BLOCK**:
> test·origin/test `598d108` 동기화 유지. test `mvn test` **246/246 PASS**(64 suites)·Boot **3.3.1**·Flyway **V50**.
> develop HEAD **`2c6e57e`** 불변(FCMS CMS skeleton @ 159차). WT **DIRTY 7** — `SmtpEmailProvider`·`NotificationConfig`/`NotificationProperties`·`application.yml`·`pom.xml`·`V60__cms_enrollment_tenant_fk_backing.sql`·`SmtpEmailProviderTest` (**HEAD ABSENT**). develop HEAD **350/350 PASS**(80 suites)·WT **353/353 PASS**(81 suites, +3 @Test). develop **30커밋 ahead** — v1.2.1 merge gate **BLOCK**(QA-20260610-B11).

> **159차 재검증 (23:12 UTC) — test `@598d108` CLEAN·origin/test 동기화·246/246 PASS·develop `2c6e57e`(+1) WT CLEAN·350/350 PASS·30 ahead·origin/develop 동기화·PASS(v1)·Open 0(backend)·★ v1.2.1 merge FULLY UNBLOCKED**:
> develop HEAD **`2c6e57e`**(`feat(v2/G2): add Hyosung FCMS CMS enrollment and debit skeleton` — `CmsService`·`CmsController`·`V59__cms_fcms_enrollment.sql`·`CmsServiceTest`·`CmsCopayLifecycleE2eTest`, 22 files +1547/-1, 342→350 +8 @Test). develop `mvn test` **350/350 PASS**(80 suites). develop **30커밋 ahead** — v1.2.1 merge gate **FULLY UNBLOCKED**. G2 CMS **StubFcmsClient skeleton** — 실 FCMS 연동/배치 debit P1 잔여.
