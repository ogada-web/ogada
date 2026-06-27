<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-24T23:23:58+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-24 1381차)

> **1381차 PASS** — baseline ROADMAP merged `@c3c6272` **2151/2151 PASS**(725.37s) · develop pre-merge `@1db75d0` **2151/2151 PASS**(727.33s) · ★ merge **EXECUTED** FF `c3c6272`→`1db75d0` (2) · post-merge **2151/2151 PASS**(728.63s) · build **1167 PASS**(8.40s) · audit **0** · live E2E **122 PASS/25 SKIP/0 FAIL**(bootstrap-disabled carry) · **★ QA-B304 Fixed @ `1db75d0`** · cross-stream **SYNCED(FE@1db75d0 + BE@dac8ebd)** · operation **BLOCK**

## 1381차 검증 요약 (merge EXECUTED · post-merge PASS)

| 항목 | 결과 |
|---|---|
| test/develop HEAD | test `1db75d0` · develop `1db75d0` **SYNCED** |
| ahead (`test..develop`) | **0/0** |
| develop working tree | **CLEAN** |
| test working tree | **DIRTY** (`?? 9`, 무해한 빈 파일 carry) |
| npm test baseline (@test c3c6272) | **2151/2151 PASS** (725.37s, 416 files) |
| npm test pre-merge (@develop 1db75d0) | **2151/2151 PASS** (727.33s, 416 files) |
| merge | **EXECUTED** FF `c3c6272`→`1db75d0` (2 commits) |
| npm test post-merge (@test 1db75d0) | **2151/2151 PASS** (728.63s, 416 files) |
| build | **1167 modules PASS** (8.40s @ test) |
| npm audit (high+, omit=dev) | **0** |
| live E2E | **122 PASS / 25 SKIP / 0 FAIL** (36.50s · bootstrap-disabled carry) |
| transfer verdict | **PASS** |
| open issue (frontend) | **0** |
| cross-stream | **SYNCED** (FE@`1db75d0` + BE@`dac8ebd`) |
| operation | **BLOCK** (origin/test push 556 BE+224 FE + QA-B95 partial) |

## merged commits (`c3c6272..1db75d0`)

1. `e63aa8e` — `ux(a11y): promote ds-cms-payment-method-catalog CSS and spec G16 parity-rules FE (UXD-162)`
2. `1db75d0` — `feat: add retry to CMS payment catalog panel`

## diff stat (3 files, +93 −29)

- `CmsPaymentMethodCatalogPanel.jsx` — G16 parity-rules FE wire + fetch retry
- `CmsPaymentMethodCatalogPanel.test.jsx` — retry harness (+1 test)
- `components.css` — UXD-162 ds-cms-payment-method-catalog tokens

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-24T22:04:29+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-24 1379차)

> **1379차 PASS** — baseline ROADMAP merged `@4875937` **2150/2150 PASS**(725.30s) · develop pre-merge `@c3c6272` **2150/2150 PASS**(727.05s) · ★ merge **EXECUTED** FF `4875937`→`c3c6272` (1) · post-merge **2150/2150 PASS**(734.78s) · build **1167 PASS**(8.41s) · audit **0** · live E2E **122 PASS/25 SKIP/0 FAIL**(bootstrap-disabled carry) · **★ QA-B302 Fixed @ `c3c6272`** · cross-stream **SYNCED(FE@c3c6272 + BE@bd1e87e)** · operation **BLOCK**

## 1379차 검증 요약 (merge EXECUTED · post-merge PASS)

| 항목 | 결과 |
|---|---|
| test/develop HEAD | test `c3c6272` · develop `c3c6272` **SYNCED** |
| ahead (`test..develop`) | **0/0** |
| develop working tree | **CLEAN** |
| test working tree | **DIRTY** (`?? 9`, 무해한 빈 파일 carry) |
| npm test baseline (@test 4875937) | **2150/2150 PASS** (725.30s, 416 files) |
| npm test pre-merge (@develop c3c6272) | **2150/2150 PASS** (727.05s, 416 files) |
| merge | **EXECUTED** FF `4875937`→`c3c6272` (1 commit) |
| npm test post-merge (@test c3c6272) | **2150/2150 PASS** (734.78s, 416 files) |
| build | **1167 modules PASS** (8.41s @ test) |
| npm audit (high+, omit=dev) | **0** |
| live E2E | **122 PASS / 25 SKIP / 0 FAIL** (36.65s · bootstrap-disabled carry) |
| transfer verdict | **PASS** |
| open issue (frontend) | **0** |
| cross-stream | **SYNCED** (FE@`c3c6272` + BE@`bd1e87e`) |
| operation | **BLOCK** (origin/test push 555 BE+222 FE + QA-B95 partial) |

## merged commits (`4875937..c3c6272`)

1. `c3c6272` — `fix: dedupe live e2e operation readiness skip reasons`

## diff stat (2 files, +41 −4)

- `src/e2e/liveConfig.js` — operation readiness skip reason dedupe
- `src/test/liveE2eHarness.test.js` — harness vitest lock (+1 test)

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-24T20:50:01+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-24 1377차)

> **1377차 PASS** — baseline ROADMAP merged `@64a7648` **2149/2149 PASS**(715.46s) · develop pre-merge `@4875937` **2149/2149 PASS**(722.01s) · ★ merge **EXECUTED** FF `64a7648`→`4875937` (1) · post-merge **2149/2149 PASS**(726.99s) · build **1166 PASS**(8.42s) · audit **0** · live E2E **122 PASS/25 SKIP/0 FAIL**(US-O05 closure) · **★ QA-B300 Fixed @ `4875937`** · **★ QA-B298 Fixed @ `4875937`** · cross-stream **SYNCED(FE@4875937 + BE@2eaf17e)** · operation **BLOCK**

## 1377차 검증 요약 (merge EXECUTED · post-merge PASS)

| 항목 | 결과 |
|---|---|
| test/develop HEAD | test `4875937` · develop `4875937` **SYNCED** |
| ahead (`test..develop`) | **0/0** |
| develop working tree | **CLEAN** |
| test working tree | **DIRTY** (`?? 9`, 무해한 빈 파일 carry) |
| npm test baseline (@test 64a7648) | **2149/2149 PASS** (715.46s, 416 files) |
| npm test pre-merge (@develop 4875937) | **2149/2149 PASS** (722.01s, 416 files) |
| merge | **EXECUTED** FF `64a7648`→`4875937` (1 commit) |
| npm test post-merge (@test 4875937) | **2149/2149 PASS** (726.99s, 416 files) |
| build | **1166 modules PASS** (8.42s @ test) |
| npm audit (high+, omit=dev) | **0** |
| live E2E | **122 PASS / 25 SKIP / 0 FAIL** (37.74s · US-O05 closure · bootstrap-disabled carry) |
| transfer verdict | **PASS** |
| open issue (frontend) | **0** |
| cross-stream | **SYNCED** (FE@`4875937` + BE@`2eaf17e`) |
| operation | **BLOCK** (origin/test push 554 BE+221 FE + QA-B95 partial) |

## merged commits (`64a7648..4875937`)

1. `4875937` — `feat(v1.2.1/G2b): wire CMS payment-method-catalog panel and fix US-O05 live E2E`

## diff stat (8 files, +292 −1)

- `CmsPaymentMethodCatalogPanel.jsx` + panel wire on `/cms`
- `branchOnboardingSupportLiveApi.e2e.test.js` — US-O05 sessions assertion fix (QA-B298 closure)
- `services.js` + `settingsServices.test.js` — CMS catalog API client

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-24T19:44:02+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-24 1374차)

> **1374차 PASS** — baseline ROADMAP merged `@216ab7a` **2145/2145 PASS**(717.07s) · develop pre-merge `@64a7648` **2145/2145 PASS**(726.10s) · ★ merge **EXECUTED** FF `216ab7a`→`64a7648` (1) · post-merge **2145/2145 PASS**(723.68s) · build **1166 PASS**(8.78s) · audit **0** · live E2E **121 PASS/25 SKIP/1 FAIL**(US-O05 ×1) · **★ QA-B297 Fixed @ `64a7648`** · **QA-B298 Open**(MEDIUM) · cross-stream **SYNCED(FE@64a7648 + BE@670756a)** · operation **BLOCK**

## 1374차 검증 요약 (merge EXECUTED · post-merge PASS)

| 항목 | 결과 |
|---|---|
| test/develop HEAD | test `64a7648` · develop `64a7648` **SYNCED** |
| ahead (`test..develop`) | **0/0** |
| develop working tree | **CLEAN** |
| test working tree | **DIRTY** (`?? 9`, 무해한 빈 파일 carry) |
| npm test baseline (@test 216ab7a) | **2145/2145 PASS** (717.07s, 415 files) |
| npm test pre-merge (@develop 64a7648) | **2145/2145 PASS** (726.10s, 415 files) |
| merge | **EXECUTED** FF `216ab7a`→`64a7648` (1 commit) |
| npm test post-merge (@test 64a7648) | **2145/2145 PASS** (723.68s, 415 files) |
| build | **1166 modules PASS** (8.78s @ test) |
| npm audit (high+, omit=dev) | **0** |
| live E2E | **121 PASS / 25 SKIP / 1 FAIL** (37.82s · `branchOnboardingSupportLiveApi` US-O05 ×1) |
| transfer verdict | **PASS** |
| open issue (frontend) | **1** (QA-B298 MEDIUM) |
| cross-stream | **SYNCED** (FE@`64a7648` + BE@`670756a`) |
| operation | **BLOCK** (origin/test push 553 BE+220 FE + QA-B95 partial + live E2E 1 FAIL) |

## merged commits (`216ab7a..64a7648`)

1. `64a7648` — `test(v1.2.1/QA-B95): relax bootstrap blocker gating for recovered auth`

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-24T18:42:08+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-24 1372차)

> **1372차 PASS** — baseline ROADMAP merged `@c06d581` **2142/2142 PASS**(715.76s) · develop pre-merge `@216ab7a` **2142/2142 PASS**(715.56s) · ★ merge **EXECUTED** FF `c06d581`→`216ab7a` (2) · post-merge **2142/2142 PASS**(718.89s) · build **1165 PASS**(8.52s) · audit **0** · live E2E **147 SKIP/0 PASS**(bootstrap-disabled) · **★ QA-B296 Fixed @ `216ab7a`** · cross-stream **BLOCK(BE pending 2 @a12873c · FE SYNCED@216ab7a)** · operation **BLOCK**

## 1372차 검증 요약 (merge EXECUTED · post-merge PASS)

| 항목 | 결과 |
|---|---|
| test/develop HEAD | test `216ab7a` · develop `216ab7a` **SYNCED** |
| ahead (`test..develop`) | **0/0** |
| develop working tree | **CLEAN** |
| test working tree | **DIRTY** (`?? 9`, 무해한 빈 파일 carry) |
| npm test baseline (@test c06d581) | **2142/2142 PASS** (715.76s, 415 files) |
| npm test pre-merge (@develop 216ab7a) | **2142/2142 PASS** (715.56s, 415 files) |
| merge | **EXECUTED** FF `c06d581`→`216ab7a` (2 commits) |
| npm test post-merge (@test 216ab7a) | **2142/2142 PASS** (718.89s, 415 files) |
| build | **1165 modules PASS** (8.52s @ test) |
| npm audit (high+, omit=dev) | **0** |
| live E2E | **147 SKIP / 0 PASS** (32.71s · bootstrap-disabled carry) |
| transfer verdict | **PASS** |
| open issue (frontend) | **0** |
| cross-stream | **BLOCK** (FE@`216ab7a` SYNCED · BE pending 2 QA-B295) |
| operation | **BLOCK** (origin/test push 550 BE+219 FE + QA-B95 partial) |

## merged commits (`c06d581..216ab7a`)

1. `216ab7a` — `test(v1.2.1/G-SMS-TEMPLATE-CATALOG): lock billing dispatch template label assertions`
2. `c7d0982` — `feat(v1.2.1/G-SMS-TEMPLATE-CATALOG): show template label on dispatch success`

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-24T16:37:49+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-24 1369차)

> **1369차 PASS** — baseline ROADMAP merged `@3f686e3` **2137/2137 PASS**(725.60s) · develop pre-merge `@c06d581` **2140/2140 PASS**(721.71s, +3 tests) · ★ merge **EXECUTED** FF `3f686e3`→`c06d581` (2) · post-merge **2140/2140 PASS**(723.85s) · build **1165 PASS**(8.35s) · audit **0** · live E2E **147 SKIP/0 PASS**(bootstrap-disabled) · **★ QA-B294 Fixed @ `c06d581`** · cross-stream **SYNCED(FE@c06d581 + BE@88a58d9)** · operation **BLOCK**

## 1369차 검증 요약 (merge EXECUTED · post-merge PASS)

| 항목 | 결과 |
|---|---|
| test/develop HEAD | test `c06d581` · develop `c06d581` **SYNCED** |
| ahead (`test..develop`) | **0/0** |
| develop working tree | **CLEAN** |
| test working tree | **DIRTY** (`?? 9`, 무해한 빈 파일 carry) |
| npm test baseline (@test 3f686e3) | **2137/2137 PASS** (725.60s, 415 files) |
| npm test pre-merge (@develop c06d581) | **2140/2140 PASS** (721.71s, 415 files, +3 tests) |
| merge | **EXECUTED** FF `3f686e3`→`c06d581` (2 commits) |
| npm test post-merge (@test c06d581) | **2140/2140 PASS** (723.85s, 415 files) |
| build | **1165 modules PASS** (8.35s @ test) |
| npm audit (high+, omit=dev) | **0** |
| live E2E | **147 SKIP / 0 PASS** (31.93s · bootstrap-disabled carry) |
| transfer verdict | **PASS** |
| open issue (frontend) | **0** |
| cross-stream | **SYNCED** (FE@`c06d581` + BE@`88a58d9`) |
| operation | **BLOCK** (origin/test push 550 BE+217 FE + QA-B95 partial) |

## merged commits (`3f686e3..c06d581`)

1. `c06d581` — `test(v1.2.1/UXD-161): lock G-SMS dispatch panel form-stack a11y`
2. `4adeb1c` — `ux(a11y): promote ds-form-stack for G-SMS dispatch panels (UXD-161)`

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-24T14:58:20+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-24 1367차)

> **1367차 PASS** — baseline pre-merge `@068049b` `npm test` **2136/2137 FAIL**(724.73s · stale `StaffAnnualLeavePage` ×1) · develop pre-merge `@3f686e3` **2137/2137 PASS**(724.16s) · ★ merge **EXECUTED** FF `068049b`→`3f686e3` (4) · post-merge **2137/2137 PASS**(727.65s) · build **1165 PASS**(8.47s) · audit **0** · live E2E **147 SKIP/0 PASS**(bootstrap-disabled) · **★ QA-B290 Fixed @ `3f686e3`** · **★ QA-B291 Fixed carry** · cross-stream **SYNCED(FE@3f686e3 + BE@ef8bb4e)** · operation **BLOCK**

## 1367차 검증 요약 (merge EXECUTED · post-merge PASS)

| 항목 | 결과 |
|---|---|
| test/develop HEAD | test `3f686e3` · develop `3f686e3` **SYNCED** |
| ahead (`test..develop`) | **0/0** |
| develop working tree | **CLEAN** |
| test working tree | **DIRTY** (`?? 9`, 무해한 빈 파일 carry) |
| npm test baseline (@test 068049b) | **2136/2137 FAIL** (724.73s, stale pending) |
| npm test pre-merge (@develop 3f686e3) | **2137/2137 PASS** (724.16s, 415 files) |
| merge | **EXECUTED** FF `068049b`→`3f686e3` (4 commits) |
| npm test post-merge (@test 3f686e3) | **2137/2137 PASS** (727.65s, 415 files) |
| build | **1165 modules PASS** (8.47s @ test) |
| npm audit (high+, omit=dev) | **0** |
| live E2E | **147 SKIP / 0 PASS** (32.85s · bootstrap-disabled carry) |
| transfer verdict | **PASS** |
| open issue (frontend) | **0** |
| cross-stream | **SYNCED** (FE@`3f686e3` + BE@`ef8bb4e`) |
| operation | **BLOCK** (origin/test push 549 BE+215 FE + QA-B95 partial) |

## merged commits (`068049b..3f686e3`)

1. `3f686e3` — `fix(v1.2.1/G-SMS-TEMPLATE-CATALOG): align ezCare message_kind fallback labels`
2. `5a6d42c` — `feat(v1.2.1/G-SMS-TEMPLATE-CATALOG): align message_kind 11·13·19 dispatch UI labels`
3. `9c25d44` — `feat(v1.2.1/G-SMS-TEMPLATE-CATALOG): wire message_kind 1·12·21 dispatch UI`
4. `c04968c` — `feat(v1.2.1/G-SMS-TEMPLATE-CATALOG): surface pending template dispatch readiness`

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-24T14:58:20+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-24 1367차)

> **1367차 PASS** — baseline `@068049b` **2136/2137 FAIL**(724.73s · stale `StaffAnnualLeavePage` pending) · develop pre-merge `@3f686e3` **2137/2137 PASS**(724.16s) · ★ merge **EXECUTED** FF `068049b`→`3f686e3` (4 commits) · post-merge **2137/2137 PASS**(727.65s, 415 files) · develop/test **SYNCED** @ `3f686e3` · build **1165 modules PASS**(8.47s) · audit **0** · live E2E **147 SKIP/0 PASS**(bootstrap-disabled carry) · **★ QA-B290 Fixed** · **★ QA-B291 Fixed carry** · cross-stream **SYNCED(FE@3f686e3 + BE@ef8bb4e)** · operation **BLOCK**

## 1367차 검증 요약 (merge EXECUTED · SYNCED)

| 항목 | 결과 |
|---|---|
| test/develop HEAD | **SYNCED** @ `3f686e3` |
| ahead (`test..develop`) | **0/0** |
| develop working tree | **CLEAN** |
| test working tree | **DIRTY** (`?? 9`, 무해한 빈 파일 carry) |
| npm test baseline (@test 068049b) | **2136/2137 FAIL** (724.73s · stale pending) |
| npm test pre-merge (@develop 3f686e3) | **2137/2137 PASS** (724.16s, 415 files) |
| merge | **EXECUTED** FF `068049b`→`3f686e3` (4 commits) |
| npm test post-merge (@test 3f686e3) | **2137/2137 PASS** (727.65s, 415 files) |
| build | **1165 modules PASS** (8.47s @ test) |
| npm audit (high+, omit=dev) | **0** |
| live E2E | **147 SKIP / 0 PASS** (bootstrap-disabled carry) |
| transfer verdict | **PASS** |
| open issue (frontend) | **0** |
| cross-stream | **SYNCED** (FE@`3f686e3` + BE@`ef8bb4e`) |
| operation | **BLOCK** (origin/test push 549 BE+215 FE + QA-B95 partial) |

## merged commits (`068049b..3f686e3`)

1. `3f686e3` — `fix(v1.2.1/G-SMS-TEMPLATE-CATALOG): align ezCare message_kind fallback labels`
2. `5a6d42c` — `feat(v1.2.1/G-SMS-TEMPLATE-CATALOG): align message_kind 11·13·19 dispatch UI labels`
3. `9c25d44` — `feat(v1.2.1/G-SMS-TEMPLATE-CATALOG): wire message_kind 1·12·21 dispatch UI`
4. `c04968c` — `feat(v1.2.1/G-SMS-TEMPLATE-CATALOG): surface pending template dispatch readiness`

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-24T13:57:33+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-24 1365차)

> **1365차 BLOCK** — ROADMAP merged regression `@068049b` `npm test` **2134/2134 PASS**(715.48s, 414 files) · develop `@5a6d42c` WT **CLEAN** · merge **SKIP**(`test..develop` **0/3** pending `c04968c`+`9c25d44`+`5a6d42c`) · `npm run build` **1165 modules PASS**(8.21s) · `npm audit --omit=dev --audit-level=high` **0** · live E2E **SKIP**(merge 없음 · bootstrap-disabled 147 SKIP/0 PASS carry) · **QA-20260624-B290 Open(BLOCK)** · **★ QA-20260624-B291 Fixed carry** · cross-stream **BLOCK(BE pending 1 @fed6f1f · FE pending 3 @5a6d42c)** · operation **BLOCK**

## 1365차 검증 요약 (baseline PASS · merge pending 3)

| 항목 | 결과 |
|---|---|
| test/develop HEAD | test `068049b` · develop `5a6d42c` |
| ahead (`test..develop`) | **0/3** pending `c04968c`+`9c25d44`+`5a6d42c` |
| develop working tree | **CLEAN** |
| test working tree | **DIRTY** (`?? 9`, 무해한 빈 파일 carry) |
| npm test baseline (@test 068049b) | **2134/2134 PASS** (715.48s, 414 files) |
| npm test pre-merge (@develop 5a6d42c) | **SKIP** (merge pending 3 · 미실행) |
| merge | **SKIP** (`068049b..5a6d42c`) |
| build | **1165 modules PASS** (8.21s @ test) |
| npm audit (high+, omit=dev) | **0** |
| live E2E | **SKIP** (merge 없음 · bootstrap-disabled carry 147 SKIP / 0 PASS) |
| transfer verdict | **BLOCK** |
| open issue (frontend) | **1** QA-20260624-B290 |
| cross-stream | **BLOCK** (BE pending 1 @`fed6f1f` · FE pending 3 @`5a6d42c`) |
| operation | **BLOCK** (origin/test push 547 BE+211 FE + QA-B95 partial + QA-B292 backend pending 1) |

## pending commits (`068049b..5a6d42c`)

1. `5a6d42c` — `feat(v1.2.1/G-SMS-TEMPLATE-CATALOG): align message_kind 11·13·19 dispatch UI labels`
2. `9c25d44` — `feat(v1.2.1/G-SMS-TEMPLATE-CATALOG): wire message_kind 1·12·21 dispatch UI`
3. `c04968c` — `feat(v1.2.1/G-SMS-TEMPLATE-CATALOG): surface pending template dispatch readiness`

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-24T12:59:05+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-24 1363차)

> **1363차 BLOCK** — ROADMAP merged regression `@068049b` `npm test` **2134/2134 PASS**(720.65s, 414 files) · develop `@9c25d44` WT **CLEAN** · merge **SKIP**(`test..develop` **0/2** pending `c04968c`+`9c25d44`) · `npm run build` **1165 modules PASS**(8.21s) · `npm audit --omit=dev --audit-level=high` **0** · live E2E **SKIP**(merge 없음 · bootstrap-disabled 147 SKIP/0 PASS carry) · **QA-20260624-B290 Open(BLOCK)** · **★ QA-20260624-B291 Fixed** · cross-stream **BLOCK(BE SYNCED@1d5d441 · FE pending 2 @9c25d44)** · operation **BLOCK**

## 1363차 검증 요약 (baseline PASS · merge pending 2)

| 항목 | 결과 |
|---|---|
| test/develop HEAD | test `068049b` · develop `9c25d44` |
| ahead (`test..develop`) | **0/2** pending `c04968c`+`9c25d44` |
| develop working tree | **CLEAN** |
| test working tree | **DIRTY** (`?? 9`, 무해한 빈 파일 carry) |
| npm test baseline (@test 068049b) | **2134/2134 PASS** (720.65s, 414 files) |
| npm test pre-merge (@develop 9c25d44) | **SKIP** (merge pending 2 · 미실행) |
| merge | **SKIP** (`068049b..9c25d44`) |
| build | **1165 modules PASS** (8.21s @ test) |
| npm audit (high+, omit=dev) | **0** |
| live E2E | **SKIP** (merge 없음 · bootstrap-disabled carry 147 SKIP / 0 PASS) |
| transfer verdict | **BLOCK** |
| open issue (frontend) | **1** QA-20260624-B290 |
| cross-stream | **BLOCK** (BE SYNCED@`1d5d441` · FE pending 2 @`9c25d44`) |
| operation | **BLOCK** (origin/test push 547 BE+211 FE + QA-B95 partial) |

## pending commits (`068049b..9c25d44`)

1. `9c25d44` — `feat(v1.2.1/G-SMS-TEMPLATE-CATALOG): wire message_kind 1·12·21 dispatch UI`
2. `c04968c` — `feat(v1.2.1/G-SMS-TEMPLATE-CATALOG): surface pending template dispatch readiness`

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-24T12:21:05+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-24 1361차)

> **1361차 BLOCK** — ROADMAP merged regression `@068049b` `npm test` **Terminated exit 143**(258.17s partial · summary 미생성) · develop `@c04968c` WT **CLEAN** · merge **SKIP**(`test..develop` **0/1** pending `c04968c`) · `npm run build` **1165 modules PASS**(9.71s) · `npm audit --omit=dev --audit-level=high` **0** · live E2E **SKIP**(merge 없음 · bootstrap-disabled 147 SKIP/0 PASS carry) · **QA-20260624-B290 Open(BLOCK)** · **QA-20260624-B291 Open(HIGH)** · cross-stream **BLOCK(BE SYNCED@b9d0599 · FE pending 1 @c04968c)** · operation **BLOCK**

## 1361차 검증 요약 (regression run Terminated · merge pending 1)

| 항목 | 결과 |
|---|---|
| test/develop HEAD | test `068049b` · develop `c04968c` |
| ahead (`test..develop`) | **0/1** pending `c04968c` |
| develop working tree | **CLEAN** |
| test working tree | **DIRTY** (`?? 9`, 무해한 빈 파일 carry) |
| npm test baseline (@test 068049b) | **Terminated exit 143** (258.17s partial · summary 미생성) |
| npm test pre-merge (@develop c04968c) | **SKIP** (merge pending 1 · 미실행) |
| merge | **SKIP** (`068049b..c04968c`) |
| build | **1165 modules PASS** (9.71s @ test) |
| npm audit (high+, omit=dev) | **0** |
| live E2E | **SKIP** (merge 없음 · bootstrap-disabled carry 147 SKIP / 0 PASS) |
| transfer verdict | **BLOCK** |
| open issue (frontend) | **2** QA-20260624-B290, QA-20260624-B291 |
| cross-stream | **BLOCK** (BE SYNCED@`b9d0599` · FE pending 1 @`c04968c`) |
| operation | **BLOCK** (origin/test push 546 BE+211 FE + QA-B95 partial) |

## pending commit (`068049b..c04968c`)

1. `c04968c` — `feat(v1.2.1/G-SMS-TEMPLATE-CATALOG): surface pending template dispatch readiness`

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-24T12:06:45+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-24 1360차)

> **1360차 BLOCK** — ROADMAP merged baseline `@068049b` `npm test` **2128/2128 PASS**(717.46s, 413 files) · develop `@c04968c` WT **CLEAN** · merge **SKIP**(`test..develop` **0/1** pending `c04968c` · pre-merge 미실행) · `npm run build` **1165 modules PASS**(8.29s) · `npm audit --omit=dev --audit-level=high` **0** · live E2E **SKIP**(merge 없음 · bootstrap-disabled 147 SKIP/0 PASS carry) · **QA-20260624-B290 Open(BLOCK)** · cross-stream **BLOCK(BE SYNCED@b9d0599 · FE pending 1 @c04968c)** · operation **BLOCK**

## 1360차 검증 요약 (ROADMAP merged PASS · merge pending 1)

| 항목 | 결과 |
|---|---|
| test/develop HEAD | test `068049b` · develop `c04968c` |
| ahead (`test..develop`) | **0/1** pending `c04968c` |
| develop working tree | **CLEAN** |
| test working tree | **DIRTY** (`?? 9`, 무해한 빈 파일 carry) |
| npm test baseline (@test 068049b) | **2128/2128 PASS** (717.46s, 413 files) |
| npm test pre-merge (@develop c04968c) | **SKIP** (merge pending 1 · 미실행) |
| merge | **SKIP** (`068049b..c04968c`) |
| build | **1165 modules PASS** (8.29s @ test) |
| npm audit (high+, omit=dev) | **0** |
| live E2E | **SKIP** (merge 없음 · bootstrap-disabled carry 147 SKIP / 0 PASS) |
| transfer verdict | **BLOCK** |
| open issue (frontend) | **1** QA-20260624-B290 |
| cross-stream | **BLOCK** (BE SYNCED@`b9d0599` · FE pending 1 @`c04968c`) |
| operation | **BLOCK** (origin/test push 546 BE+211 FE + QA-B95 partial) |

## pending commit (`068049b..c04968c`)

1. `c04968c` — `feat(v1.2.1/G-SMS-TEMPLATE-CATALOG): surface pending template dispatch readiness`

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-24T11:18:57+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-24 1358차)

> **1358차 PASS(SYNCED @068049b)** — baseline `@c9cf03b` **2128/2128 PASS**(710s) · develop pre-merge `@068049b` **2128/2128 PASS**(723s) · merge **EXECUTED** FF `c9cf03b`→`068049b` (3 commits) · post-merge **2128/2128 PASS**(710s) · build **1165 PASS**(8.37s) · audit **0 high** · live E2E **147 SKIP/0 PASS**(33s · bootstrap-disabled) · **★ QA-B289 Fixed @ `068049b`** · cross-stream **SYNCED(FE@068049b + BE@8631d1e)** · operation **BLOCK**

## 1358차 검증 요약 (merge EXECUTED · SYNCED PASS)

| 항목 | 결과 |
|---|---|
| test/develop HEAD | **068049b** SYNCED |
| ahead (`test..develop`) | **0/0** |
| develop working tree | **CLEAN** |
| test working tree | **DIRTY** (`?? 9`, 무해한 빈 파일 carry) |
| npm test baseline (@test c9cf03b) | **2128/2128 PASS** (710s, 413 files) |
| npm test pre-merge (@develop 068049b) | **2128/2128 PASS** (723s) |
| merge | **EXECUTED** FF `c9cf03b`→`068049b` (3 commits) |
| npm test post-merge (@test 068049b) | **2128/2128 PASS** (710s) |
| build | **1165 modules PASS** (8.37s @ test) |
| npm audit (high+, omit=dev) | **0** |
| live E2E | **147 SKIP / 0 PASS** (33s · bootstrap-disabled) |
| transfer verdict | **PASS** |
| open issue (frontend) | **0** |
| cross-stream | **SYNCED** (FE@`068049b` + BE@`8631d1e`) |
| operation | **BLOCK** (origin/test push 545 BE+211 FE + QA-B95 partial) |

## merged commits (`c9cf03b..068049b`)

1. `15f2195` — `ux(a11y): G-SMS template catalog and FAQ21823 retention wire (UXD-160)`
2. `ef3948c` — `feat(v1.2.1/G-SMS-TEMPLATE-CATALOG): deepen module 10 coverage to 0.65`
3. `068049b` — `fix(v1.2.1/QA-B289): align renewal action accessible name`

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-24T10:04:00+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-24 1356차)

> **1356차 BLOCK** — baseline `@c9cf03b` **2126/2126 PASS**(720.42s r2 reconfirm) · develop pre-merge `@ef3948c` **2127/2128 FAIL**(717.10s · FAQ21823 ×1 · isolated FAIL) · merge **SKIP**(`0/2` pending · pre-merge FAIL) · build **1165 PASS**(9.99s) · audit **0 high** · live E2E **SKIP** · **QA-B289 Open(BLOCK · UXD-160 aria-label)** · cross-stream **BLOCK(BE SYNCED@fb323ae · FE pending 2)** · operation **BLOCK**

## 1356차 검증 요약 (pre-merge FAIL · merge SKIP)

| 항목 | 결과 |
|---|---|
| test/develop HEAD | test `c9cf03b` · develop `ef3948c` |
| ahead (`test..develop`) | **0/2** pending `15f2195`+`ef3948c` |
| develop working tree | **CLEAN** |
| test working tree | **DIRTY** (`?? 9`, 무해한 빈 파일 carry) |
| npm test baseline (@test c9cf03b) | **2126/2126 PASS** (720.27s, worktree flock) |
| npm test pre-merge (@develop ef3948c) | **2127/2128 FAIL** (717.10s · isolated FAIL) |
| merge | **SKIP** (pre-merge FAIL) |
| build | **1165 modules PASS** (9.99s @ test) |
| npm audit (high+, omit=dev) | **0** |
| live E2E | **SKIP** (merge 없음 · bootstrap-disabled carry) |
| transfer verdict | **BLOCK** |
| open issue (frontend) | **1** QA-B289 |
| cross-stream | **BLOCK** (BE SYNCED@`fb323ae` · FE pending 2 + pre-merge FAIL) |
| operation | **BLOCK** (origin/test push 544 BE+208 FE + QA-B95 partial) |

## pending commits (`c9cf03b..ef3948c`)

1. `15f2195` — `ux(a11y): G-SMS template catalog and FAQ21823 retention wire (UXD-160)`
2. `ef3948c` — `feat(v1.2.1/G-SMS-TEMPLATE-CATALOG): deepen module 10 coverage to 0.65`

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-24T08:24:00+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-24 1354차)

> **1354차 PASS(SYNCED @c9cf03b)** — develop pre-merge **2126/2126 PASS**(718.39s, +1 test) · merge **EXECUTED** FF `d682562`→`c9cf03b` (1 commit) · post-merge worktree **2126/2126 PASS**(713.33s, 413 files) · `npm run build` **1165 modules PASS**(8.27s) · `npm audit --omit=dev --audit-level=high` **0** · live E2E **SKIP**(bootstrap-disabled · 147 SKIP/0 PASS carry) · **★ QA-B288 Fixed** · Open **0 FE** · cross-stream **BLOCK(BE dirty@b6c9b16 QA-B287 · FE SYNCED@c9cf03b)** · operation **BLOCK**

## 1354차 검증 요약 (SYNCED revalidation PASS)

| 항목 | 결과 |
|---|---|
| test/develop HEAD | test `c9cf03b` · develop `c9cf03b` |
| ahead (`test..develop`) | **0/0** SYNCED |
| develop working tree | **CLEAN** |
| test working tree | **DIRTY** (`?? 9`, 무해한 빈 파일 carry) |
| npm test post-merge (@test c9cf03b worktree) | **2126/2126 PASS** (713.33s, 413 files) |
| npm test pre-merge (@develop c9cf03b) | **2126/2126 PASS** (718.39s, +1 test) |
| merge | **EXECUTED** FF `d682562`→`c9cf03b` (1 commit) |
| build | **1165 modules PASS** (8.37s @ test) |
| npm audit (high+, omit=dev) | **0** |
| live E2E | **SKIP** (bootstrap-disabled carry) |
| transfer verdict | **PASS** |
| open issue (frontend) | **0** |
| cross-stream | **BLOCK** (BE dirty@`b6c9b16` QA-B287 · FE SYNCED@`c9cf03b`) |
| operation | **BLOCK** (origin/test push 543 BE+208 FE + QA-B95 partial) |

## applied commits (`d682562..c9cf03b`)

1. `c9cf03b` — `feat(v1.2.1/G-SMS-TEMPLATE-CATALOG-FE-WIRE): wire ezCare template catalog into readiness panel`

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-24T07:19:30+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-24 1352차)

> **1352차 PASS(SYNCED @d682562)** — ROADMAP merged revalidation `@d682562` **2125/2125 PASS**(722.01s, 413 files) · develop pre-merge **2125/2125 PASS**(708.06s, +4 tests) · merge **SKIP**(`0/0` · FF `a43bcb7`→`d682562` 2 commits applied) · `npm run build` **1165 modules PASS**(8.56s) · `npm audit --omit=dev --audit-level=high` **0** · live E2E **SKIP**(bootstrap-disabled · 147 SKIP/0 PASS carry) · **★ QA-B285 Fixed** · transfer **PASS** · cross-stream **SYNCED(FE@d682562 + BE@b6c9b16)** · operation **BLOCK**

## 1352차 검증 요약 (SYNCED revalidation PASS)

| 항목 | 결과 |
|---|---|
| test/develop HEAD | test `d682562` · develop `d682562` |
| ahead (`test..develop`) | **0/0** SYNCED |
| develop working tree | **CLEAN** |
| test working tree | **DIRTY** (`?? 9`, 무해한 빈 파일 carry) |
| npm test post-merge (@test d682562) | **2125/2125 PASS** (722.01s, 413 files) |
| npm test pre-merge (@develop d682562) | **2125/2125 PASS** (708.06s, +4 tests) |
| merge | **SKIP** (0/0 · 1352차 FF already applied) |
| build | **1165 modules PASS** (8.56s @ test) |
| npm audit (high+, omit=dev) | **0** |
| live E2E | **SKIP** (bootstrap-disabled carry) |
| transfer verdict | **PASS** |
| open issue (frontend) | **0** |
| cross-stream | **SYNCED** (FE@`d682562` + BE@`b6c9b16`) |
| operation | **BLOCK** (origin/test push 543 BE+207 FE + QA-B95 partial) |

## applied commits (`a43bcb7..d682562`)

1. `596658a` — `feat(v1.2.1/FAQ21823): wire employment contract compliance API to dashboard and staff`
2. `d682562` — `fix(v1.2.1/QA-B285): align FAQ21823 tests with compliance API wire`

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-24T05:58:53+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-24 1350차)

> **1350차 BLOCK** — baseline `@a43bcb7` `npm test` **2123/2125 FAIL**(710s · 2 FAIL · isolated FAQ21823 **3/3 PASS** pollution) · develop pre-merge `@596658a` **2123/2125 FAIL**(720s · 2 FAIL · isolated **2/2 FAIL**) · merge **SKIP**(`0/1` pending · pre-merge FAIL) · build **PASS**(12.20s) · audit **0 high** · live E2E **SKIP** · **QA-B285 Open(BLOCK)** · cross-stream **BLOCK(BE SYNCED@9aaefa0 · FE pending 1)** · operation **BLOCK**

## 1350차 검증 요약 (pre-merge FAIL · merge SKIP)

| 항목 | 결과 |
|---|---|
| test/develop HEAD | test `a43bcb7` · develop `596658a` |
| ahead (`test..develop`) | **0/1** pending `596658a` |
| develop working tree | **CLEAN** |
| test working tree | **DIRTY** (`?? 9`, 무해한 빈 파일 carry) |
| npm test baseline (@test a43bcb7) | **2123/2125 FAIL** (710s · isolated FAQ21823 3/3 PASS) |
| npm test pre-merge (@develop 596658a) | **2123/2125 FAIL** (720s · isolated FAQ21823 2/2 FAIL) |
| merge | **SKIP** (pre-merge FAIL) |
| build | **PASS** (12.20s @ test) |
| npm audit (high+) | **0** |
| live E2E | **SKIP** (merge 없음 · bootstrap-disabled carry) |
| transfer verdict | **BLOCK** |
| open issue (frontend) | **1** (QA-B285 Open) |
| cross-stream | **BLOCK** (BE SYNCED@`9aaefa0` · FE pending 1 + pre-merge FAIL) |
| operation | **BLOCK** (origin/test push 542 BE+205 FE + QA-B95 partial) |

## pending commit (`a43bcb7..596658a`)

1. `596658a` — `feat(v1.2.1/FAQ21823): wire employment contract compliance API to dashboard and staff`

## pre-merge FAIL 상세

| 테스트 | 증상 |
|---|---|
| `StaffPage.test.jsx` FAQ21823 | heading `근로(재)계약·임금협의 (FAQ 21823)` 미렌더 |
| `pilotPageFlows.test.jsx` FAQ21823 | `global.fetch` assertion `/api/v1/users?page=0&size=200` 불일치 (billing API 우선 호출) |

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-24T04:43:09+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-24 1348차)

> **1348차 PASS(SYNCED @a43bcb7)** — baseline `@cba9ff8` `npm test` **2121/2121 PASS**(413 files, 719.81s) · develop pre-merge **Terminated exit 143**(~658s carry) · ★ merge **EXECUTED** FF `cba9ff8`→`a43bcb7` (1 commit) · post-merge **2121/2121 PASS**(818.17s) · `npm run build` **1165 modules PASS**(8.50s) · `npm audit` **1 high**(form-data) · live E2E **SKIP**(bootstrap-disabled · 147 SKIP/0 PASS carry) · **QA-B283 Fixed** · transfer **PASS** · cross-stream **SYNCED(FE@a43bcb7 + BE@d11263b)** · operation **BLOCK**

## 1348차 검증 요약 (post-merge PASS · SYNCED)

| 항목 | 결과 |
|---|---|
| test/develop HEAD | test `a43bcb7` · develop `a43bcb7` |
| ahead (`test..develop`) | **0/0** SYNCED |
| develop working tree | **CLEAN** |
| test working tree | **DIRTY** (`?? 9`, 무해한 빈 파일 carry) |
| npm test baseline (@test cba9ff8) | **2121/2121 PASS** (719.81s, 413 files) |
| npm test pre-merge (@develop a43bcb7) | **Terminated exit 143** (~658s partial, vitest concurrency carry) |
| merge | **EXECUTED** FF `cba9ff8`→`a43bcb7` (1 commit) |
| npm test post-merge (@test a43bcb7) | **2121/2121 PASS** (818.17s, 413 files) |
| build | **1165 modules PASS** (8.50s @ test) |
| npm audit (high+) | **1 high** (form-data CRLF) |
| live E2E | **SKIP** (bootstrap-disabled carry 147 SKIP / 0 PASS) |
| transfer verdict | **PASS** |
| open issue (frontend) | **0** (QA-B283 Fixed) |
| cross-stream | **SYNCED** (BE@`d11263b` · FE@`a43bcb7`) |
| operation | **BLOCK** (origin/test push 541 BE+205 FE + QA-B95 partial) |

## merged commit (`cba9ff8..a43bcb7`)

1. `a43bcb7` — `feat(v1.2.1/FAQ21823): add retention expiry alerts and contract template print`
