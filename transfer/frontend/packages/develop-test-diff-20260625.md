<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-25T22:51:53+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-25 1418차)

> **1418차 PASS** — baseline carry `@7e7c296` **2214/2214 PASS**(755.08s, 427 files · TSR 1416 post-merge) · develop pre-merge `@4bbd54a` **2217/2217 PASS**(754.56s, +3 tests) · ★ merge **EXECUTED** FF `7e7c296`→`4bbd54a` (1 commit) · post-merge **2217/2217 PASS**(748.16s) · build **1180 PASS**(11.36s) · audit **0** · live E2E **122/25/0**(37.08s · bootstrap-disabled) · **★ QA-B333 Fixed @ `7e7c296`**(carry) · **★ QA-B335 Fixed @ `4bbd54a`** · cross-stream **SYNCED(FE@4bbd54a + BE@d06e3f1)** · operation **BLOCK**

## 1418차 검증 요약 (merge EXECUTED · PASS)

| 항목 | 결과 |
|---|---|
| test/develop HEAD | test `4bbd54a` · develop `4bbd54a` **SYNCED** |
| ahead (`test..develop`) | **0** |
| develop working tree | **CLEAN** |
| test working tree | **DIRTY** (`?? 9`, 빈 파일 artifact · LOW carry) |
| npm test baseline (@test 7e7c296 carry) | **2214/2214 PASS** (755.08s, 427 files) |
| develop pre-merge (@4bbd54a) | **2217/2217 PASS** (754.56s, 427 files, +3 tests) |
| merge | **EXECUTED** FF `7e7c296`→`4bbd54a` (1 commit) |
| npm test post-merge (@test 4bbd54a) | **2217/2217 PASS** (748.16s, 427 files) |
| build | **1180 modules PASS** (11.36s @ test) |
| npm audit (high+, omit=dev) | **0** |
| live E2E | **122 PASS / 25 SKIP / 0 FAIL** (37.08s · bootstrap-disabled) |
| transfer verdict | **PASS** |
| open issue (frontend) | **0** |
| cross-stream | **SYNCED** (FE@4bbd54a + BE@d06e3f1) |
| operation | **BLOCK** (origin/test push 575 BE+247 FE + QA-B95 + QA-B116) |

## merged commit (`7e7c296..4bbd54a`)

1. `4bbd54a` — `fix(v1.2.1/QA-B95): wire recovered-auth readiness hints from health probe` (+3 vitest · BE `d06e3f1` alignment)

## diff stat (주요 영향)

- `src/e2e/liveBackendProbe.js` — `/health` recovered-auth·bootstrap hint 파싱
- `src/e2e/liveConfig.js` — `liveE2eAllowRecoveredAuth`·`liveE2eBootstrapEnableHint` 노출
- `src/e2e/liveGlobalSetup.js` — recovered-auth neutral operation reason
- `src/test/liveE2eHarness.test.js` — +3 regression tests

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-25T21:52:44+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-25 1416차)

> **1416차 BLOCK** — baseline `@b7004ca` **2214/2214 PASS**(753.55s, 427 files) · develop `@7e7c296` WT **CLEAN** · merge **SKIP**(`0/1` pending) · build **1180 PASS**(8.68s) · audit **0** · live E2E **SKIP**(merge 없음 · carry 122/25/0) · **QA-B333 Open(BLOCK)** · cross-stream **BLOCK(BE SYNCED@42a369e · FE pending 1 @7e7c296)** · operation **BLOCK**

## 1416차 검증 요약 (merge pending · BLOCK)

| 항목 | 결과 |
|---|---|
| test/develop HEAD | test `b7004ca` · develop `7e7c296` |
| ahead (`test..develop`) | **1** (pending `7e7c296`) |
| develop working tree | **CLEAN** |
| test working tree | **DIRTY** (`?? 9`, 빈 파일 artifact) |
| npm test baseline (@test b7004ca) | **2214/2214 PASS** (753.55s, 427 files) |
| develop pre-merge | **SKIP** (`src/frontend` read-only 정책) |
| merge | **SKIP** (pending 1 미이관) |
| npm test post-merge | **SKIP** (merge 미실행) |
| build | **1180 modules PASS** (8.68s @ test) |
| npm audit (high+, omit=dev) | **0** |
| live E2E | **SKIP** (merge 없음 · carry 122 PASS / 25 SKIP / 0 FAIL) |
| transfer verdict | **BLOCK** |
| open issue (frontend) | **1** (`QA-20260625-B333`) |
| cross-stream | **BLOCK** (BE SYNCED@42a369e · FE pending 1) |
| operation | **BLOCK** (origin/test push + QA-B95 + QA-B116 + QA-B333) |

## pending commit (`b7004ca..7e7c296`)

1. `7e7c296` — `fix(v1.2.1/QA-B95): ignore neutral operation blocker markers`

## diff stat (주요 예상 영향)

- `src/e2e/liveGlobalSetup.js` — operation blocker marker 무시 로직 보정(merge 전)

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-25T21:15:49+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-25 1414차)

> **1414차 PASS** — baseline `@33944e4` **2212/2212 PASS**(747.41s, 427 files) · develop pre-merge `@b7004ca` **2212/2212 PASS**(748.65s) · ★ merge **EXECUTED** FF `33944e4`→`b7004ca` (2 commits) · post-merge **2212/2212 PASS**(749.11s) · build **1180 PASS**(9.26s) · audit **0** · live E2E **122/25/0**(37.92s · bootstrap-disabled) · **★ QA-B331 Fixed @ `b7004ca`** · cross-stream **BLOCK(BE develop DIRTY@3342938 · FE SYNCED@b7004ca)** · operation **BLOCK**

## 1414차 검증 요약 (merge EXECUTED · PASS)

| 항목 | 결과 |
|---|---|
| test/develop HEAD | test `b7004ca` · develop `b7004ca` |
| ahead (`test..develop`) | **0** (SYNCED) |
| develop working tree | **CLEAN** |
| test working tree | **DIRTY** (`?? 9`, 무해한 빈 파일 carry) |
| npm test baseline (@test 33944e4) | **2212/2212 PASS** (747.41s, 427 files) |
| develop pre-merge | **2212/2212 PASS** (748.65s, 427 files) |
| merge | **EXECUTED** FF `33944e4`→`b7004ca` (2 commits) |
| npm test post-merge | **2212/2212 PASS** (749.11s, 427 files) |
| build | **1180 modules PASS** (9.26s @ test) |
| npm audit (high+, omit=dev) | **0** |
| live E2E | **122 PASS / 25 SKIP / 0 FAIL** (37.92s · bootstrap-disabled) |
| transfer verdict | **PASS** |
| open issue (frontend) | **0** |
| cross-stream | **BLOCK** (FE@b7004ca SYNCED · BE develop DIRTY@3342938 QA-B330) |
| operation | **BLOCK** (origin/test push 573 BE+245 FE + QA-B95 + QA-B116 + QA-B330) |

## merged commits (`33944e4..b7004ca`)

1. `bee97b9` — `ux(a11y/FE-16): promote refund-fee-preview CSS + fix schedule page a11y (UXD-165)`
2. `b7004ca` — `fix(v1.2.1/QA-B95): support legacy singular operation blocker keys`

## diff stat (5 files, +92 −4)

- `src/styles/components.css` — refund-fee-preview CSS (UXD-165)
- `src/pages/StaffMonthlySchedulePage.jsx` — a11y label/id 연결
- `src/e2e/liveConfig.js` · `src/e2e/liveBackendProbe.js` — legacy singular operation blocker key 지원
- `src/test/liveE2eHarness.test.js` — regression lock (+25 lines)

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-25T18:46:12+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-25 1410차)

> **1410차 PASS** — baseline `@2c9abd6` **2203/2203 PASS**(745.66s, 425 files) · develop pre-merge `@bd3253a` **2203/2203 PASS**(743.56s) · ★ merge **EXECUTED** FF `2c9abd6`→`bd3253a` (1 commit) · post-merge **2203/2203 PASS**(745.19s) · build **1178 PASS**(8.53s) · audit **0** · live E2E **122/25/0**(36.82s · bootstrap-disabled) · **★ QA-B327 Fixed @ `bd3253a`** · cross-stream **BLOCK(BE develop DIRTY@49fe2e7 · FE SYNCED@bd3253a)** · operation **BLOCK**

## 1410차 검증 요약 (merge EXECUTED · PASS)

| 항목 | 결과 |
|---|---|
| test/develop HEAD | test `bd3253a` · develop `bd3253a` |
| ahead (`test..develop`) | **0** (SYNCED) |
| develop working tree | **CLEAN** |
| test working tree | **DIRTY** (`?? 9`, 무해한 빈 파일 carry) |
| npm test baseline (@test 2c9abd6) | **2203/2203 PASS** (745.66s, 425 files) |
| develop pre-merge | **2203/2203 PASS** (743.56s, 425 files) |
| merge | **EXECUTED** FF `2c9abd6`→`bd3253a` (1 commit) |
| npm test post-merge | **2203/2203 PASS** (745.19s, 425 files) |
| build | **1178 modules PASS** (8.53s @ test) |
| npm audit (high+, omit=dev) | **0** |
| live E2E | **122 PASS / 25 SKIP / 0 FAIL** (36.82s · bootstrap-disabled) |
| transfer verdict | **PASS** |
| open issue (frontend) | **0** |
| cross-stream | **BLOCK** (FE@bd3253a SYNCED · BE develop DIRTY@49fe2e7 QA-B326) |
| operation | **BLOCK** (origin/test push 572 BE+242 FE + QA-B95 + QA-B116 + QA-B326) |

## merged commits (`2c9abd6..bd3253a`)

1. `bd3253a` — `fix: normalize live operation blockers from probe state`

## diff stat (3 files, +53 −10)

- `src/e2e/liveConfig.js` — probe state blocker label 정규화
- `src/e2e/liveGlobalSetup.js` — string-form blocker recoverable 처리
- `src/test/liveE2eHarness.test.js` — regression lock (+21 lines)

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-25T15:34:11+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-25 1406차)

> **1406차 PASS** — baseline `@15a3b7f` **2200/2200 PASS**(744.12s, 425 files) · develop pre-merge `@75c0f51` **2200/2200 PASS**(743.09s) · ★ merge **EXECUTED** FF `15a3b7f`→`75c0f51` (1 commit) · post-merge **2200/2200 PASS**(carry) · build **1178 PASS**(10.32s) · audit **0** · live E2E **122/25/0**(44.87s · bootstrap-disabled) · **★ QA-B323 Fixed @ `75c0f51`** · cross-stream **SYNCED(FE@75c0f51 + BE@0e55f3b)** · operation **BLOCK**

## 1406차 검증 요약 (merge EXECUTED · PASS)

| 항목 | 결과 |
|---|---|
| test/develop HEAD | test `75c0f51` · develop `75c0f51` |
| ahead (`test..develop`) | **0** (SYNCED) |
| develop working tree | **CLEAN** |
| test working tree | **DIRTY** (`?? 9`, 무해한 빈 파일 carry) |
| npm test baseline (@test 15a3b7f) | **2200/2200 PASS** (744.12s, 425 files) |
| develop pre-merge | **2200/2200 PASS** (743.09s, 425 files) |
| merge | **EXECUTED** FF `15a3b7f`→`75c0f51` (1 commit) |
| npm test post-merge | **2200/2200 PASS** (carry @`75c0f51`) |
| build | **1178 modules PASS** (10.32s @ test) |
| npm audit (high+, omit=dev) | **0** |
| live E2E | **122 PASS / 25 SKIP / 0 FAIL** (44.87s · bootstrap-disabled) |
| transfer verdict | **PASS** |
| open issue (frontend) | **0** |
| cross-stream | **SYNCED** (FE@75c0f51 + BE@0e55f3b) |
| operation | **BLOCK** (origin/test push 570 BE+239 FE + QA-B95 + QA-B116) |

## merged commits (`15a3b7f..75c0f51`)

1. `75c0f51` — `fix(v1.2.1/QA-B95): treat bootstrap-unavailable blockers as recoverable`

## diff stat (3 files, +98 −2)

- `src/e2e/liveConfig.js` — bootstrap-unavailable blocker label 정규화
- `src/e2e/liveGlobalSetup.js` — recovered auth 세션에서 bootstrap-unavailable 무시
- `src/test/liveE2eHarness.test.js` — regression lock (+88 lines)

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-25T14:30:00+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-25 1404차)

> **1404차 PASS** — baseline `@5914b2f` **2198/2198 PASS**(743.99s, 425 files) · develop pre-merge `@15a3b7f` **2198/2198 PASS**(745.36s, +12 tests) · ★ merge **EXECUTED** FF `5914b2f`→`15a3b7f` (2 commits) · post-merge **2198/2198 PASS**(carry) · build **1178 PASS**(13s) · audit **0** · live E2E **122/25/0**(37.15s · bootstrap-disabled) · **★ QA-B321 Fixed @ `15a3b7f`** · cross-stream **SYNCED(FE@15a3b7f + BE@650801b)** · operation **BLOCK**

## 1404차 검증 요약 (merge EXECUTED · PASS)

| 항목 | 결과 |
|---|---|
| test/develop HEAD | test `15a3b7f` · develop `15a3b7f` |
| ahead (`test..develop`) | **0** (SYNCED) |
| develop working tree | **CLEAN** |
| test working tree | **DIRTY** (`?? 9`, 무해한 빈 파일 carry) |
| npm test baseline (@test 5914b2f) | **2198/2198 PASS** (743.99s, 425 files) |
| develop pre-merge | **2198/2198 PASS** (745.36s, 425 files, +12 tests) |
| merge | **EXECUTED** FF `5914b2f`→`15a3b7f` (2 commits) |
| npm test post-merge | **2198/2198 PASS** (carry @`15a3b7f`) |
| build | **1178 modules PASS** (13s @ test) |
| npm audit (high+, omit=dev) | **0** |
| live E2E | **122 PASS / 25 SKIP / 0 FAIL** (37.15s · bootstrap-disabled) |
| transfer verdict | **PASS** |
| open issue (frontend) | **0** |
| cross-stream | **SYNCED** (FE@15a3b7f + BE@650801b) |
| operation | **BLOCK** (origin/test push 569 BE+238 FE + QA-B95 + QA-B116) |

## merged commits (`5914b2f..15a3b7f`)

1. `d64f81b` — `ux(a11y/FE-16): promote undefined shared util classes to single source (UXD-164)`
2. `15a3b7f` — `feat(v1.2.1/G-REPORT-DENSITY): wire M5 program report pages for US-P02`

## diff stat (14 files, +1107)

- `ProgramReportsPage.jsx` + `.test.jsx` — M5 4-leaf program report hub (신규)
- `ProgramReportPanel.jsx` + `.test.jsx` — shared report panel + API wire
- `ProgramReportNav.jsx` — context nav
- `programReports.js` — report catalog config
- `services.js` + `programReportServices.test.js` — program report API client
- `App.jsx` · `navConfig.js` · `RecordsContextNav.jsx` — route/nav wire
- `components.css` — UXD-164 util class promotion

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-25T12:56:17+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-25 1402차)

> **1402차 PASS** — baseline `@5914b2f` **2186/2186 PASS**(739.00s, 422 files, +5 tests) · develop/test **SYNCED** @ `5914b2f` · merge **SKIP**(`test..develop` **0**) · post-merge **2186/2186 PASS**(carry) · build **1174 PASS**(11.66s) · audit **0** · live E2E **122/25/0**(45.13s · bootstrap-disabled carry) · cross-stream **SYNCED(FE@5914b2f + BE@9f67954)** · operation **BLOCK**

## 1402차 검증 요약 (SYNCED revalidation · PASS)

| 항목 | 결과 |
|---|---|
| test/develop HEAD | test `5914b2f` · develop `5914b2f` |
| ahead (`test..develop`) | **0** (SYNCED) |
| develop working tree | **CLEAN** |
| test working tree | **DIRTY** (`?? 9`, 무해한 빈 파일 carry) |
| npm test baseline (@test 5914b2f) | **2186/2186 PASS** (739.00s, 422 files) |
| develop pre-merge | **2186/2186 PASS** (739.00s, 422 files, +5 tests) |
| merge | **SKIP** (SYNCED · commit already on test) |
| npm test post-merge | **2186/2186 PASS** (739.00s, 422 files · carry) |
| build | **1174 modules PASS** (11.66s @ test) |
| npm audit (high+, omit=dev) | **0** |
| live E2E | **122 PASS / 25 SKIP / 0 FAIL** (45.13s · bootstrap-disabled carry) |
| transfer verdict | **PASS** |
| open issue (frontend) | **0** |
| cross-stream | **SYNCED** (FE@5914b2f + BE@9f67954) |
| operation | **BLOCK** (origin/test push 568 BE+236 FE + QA-B95 + QA-B116) |

## carry commit (`e070c45..5914b2f`)

1. `5914b2f` — `feat(v2/G2/7-5): wire easy-pay provider catalog and mount transport parity panel`

## diff stat (주요)

- `src/components/ui/EasyPayProviderCatalogPanel.jsx` — G2/7-5 easy-pay provider catalog panel (+182 lines)
- `src/components/transport/TransportParityRulesPanel.test.jsx` — G16 parity-rules panel tests (+49 lines)
- `src/pages/EasyPayPage.jsx` · `TransportServiceFeePage.jsx` — panel mount wire
- `src/api/services.js` — easy-pay catalog API wire

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-25T11:29:13+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-25 1400차)

> **1400차 PASS** — baseline carry `@cadd74a` **2180/2180 PASS**(TSR 1398차) · develop pre-merge `@e070c45` **2181/2181 PASS**(736.76s) · merge **EXECUTED** FF `cadd74a`→`e070c45` (1 commit) · post-merge **2181/2181 PASS**(738.43s) · build **1172 PASS**(10.29s) · audit **0** · live E2E **122/25/0**(37.39s · bootstrap-disabled carry) · cross-stream **SYNCED(FE@e070c45 + BE@79725eb)** · operation **BLOCK**

## 1400차 검증 요약 (merge EXECUTED · PASS)

| 항목 | 결과 |
|---|---|
| test/develop HEAD | test `e070c45` · develop `e070c45` |
| ahead (`test..develop`) | **0** (SYNCED) |
| develop working tree | **CLEAN** |
| test working tree | **DIRTY** (`?? 9`, 무해한 빈 파일 carry) |
| npm test baseline (@test cadd74a carry) | **2180/2180 PASS** (TSR 1398차) |
| develop pre-merge | **2181/2181 PASS** (736.76s, 420 files, +1 test) |
| merge | **EXECUTED** FF `cadd74a`→`e070c45` (1 commit) |
| npm test post-merge | **2181/2181 PASS** (738.43s, 420 files) |
| build | **1172 modules PASS** (10.29s @ test) |
| npm audit (high+, omit=dev) | **0** |
| live E2E | **122 PASS / 25 SKIP / 0 FAIL** (37.39s · bootstrap-disabled carry) |
| transfer verdict | **PASS** |
| open issue (frontend) | **0** |
| cross-stream | **SYNCED** (FE@e070c45 + BE@79725eb) |
| operation | **BLOCK** (origin/test push 567 BE+235 FE + QA-B95 + QA-B116) |

## merge commit (`cadd74a..e070c45`)

1. `e070c45` — `fix(v1.2.1/QA-B95): honor recovered auth for live operation readiness`

## diff stat (주요)

- `src/e2e/liveConfig.js` — recovered-auth config probe
- `src/e2e/liveGlobalSetup.js` — auth recovery + bootstrap readiness deepen
- `src/test/liveE2eHarness.test.js` — +64 lines harness unit lock

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-25T11:30:00+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-25 1400차)

> **1400차 PASS** — baseline carry `@cadd74a` **2180/2180 PASS**(TSR 1398차) · develop pre-merge `@e070c45` **2181/2181 PASS**(736.76s) · ★ merge **EXECUTED** FF `cadd74a`→`e070c45` (1 commit) · post-merge **2181/2181 PASS**(738.43s) · build **1172 PASS**(10.21s) · audit **0** · live E2E **122 PASS/25 SKIP/0 FAIL**(37.39s carry) · **★ QA-B318 Fixed @ `e070c45`** · cross-stream **SYNCED(FE@e070c45 + BE@79725eb)** · operation **BLOCK**

## 1400차 검증 요약 (merge EXECUTED · PASS)

| 항목 | 결과 |
|---|---|
| test/develop HEAD | test `e070c45` · develop `e070c45` **SYNCED** |
| ahead (`test..develop`) | **0** |
| develop working tree | **CLEAN** |
| test working tree | **DIRTY** (`?? 9`, 무해한 빈 파일 carry) |
| npm test baseline (@test cadd74a carry) | **2180/2180 PASS** (TSR 1398차) |
| npm test pre-merge (@develop e070c45) | **2181/2181 PASS** (736.76s, 420 files, +1 test) |
| merge | **EXECUTED** FF `cadd74a`→`e070c45` (1 commit) |
| npm test post-merge | **2181/2181 PASS** (738.43s, 420 files) |
| build | **1172 modules PASS** (10.21s @ test) |
| npm audit (high+, omit=dev) | **0** |
| live E2E | **122 PASS / 25 SKIP / 0 FAIL** (37.39s · bootstrap-disabled carry) |
| transfer verdict | **PASS** |
| open issue (frontend) | **0** |
| cross-stream | **SYNCED** (FE@`e070c45` + BE@`79725eb`) |
| operation | **BLOCK** (origin/test push 567 BE+235 FE + QA-B95 partial + QA-B116) |

## merged commit (`cadd74a..e070c45`)

1. `e070c45` — `fix(v1.2.1/QA-B95): honor recovered auth for live operation readiness`

## diff stat (3 files, +158 −11)

- `liveGlobalSetup.js` — sessionStorage 복구 auth를 live operation readiness probe에 반영
- `liveConfig.js` — recovered-auth gate config
- `liveE2eHarness.test.js` — recovered-auth harness (+1 test)

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-25T10:20:34+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-25 1398차)

> **1398차 PASS** — baseline carry `@3d7f13b` **2171/2171 PASS**(TSR 1396차) · develop/test **SYNCED** @ `cadd74a` · merge **carry SYNCED**(`3d7f13b`→`cadd74a` 1 commit) · post-merge **2180/2180 PASS**(737.93s) · build **1172 PASS**(10.28s) · audit **0** · live E2E **SKIP**(122/25/0 carry) · cross-stream **BLOCK(BE pending 1 @aeecc1b · FE SYNCED@cadd74a)** · operation **BLOCK**

## 1398차 검증 요약 (carry SYNCED · PASS)

| 항목 | 결과 |
|---|---|
| test/develop HEAD | test `cadd74a` · develop `cadd74a` |
| ahead (`test..develop`) | **0** (SYNCED) |
| develop working tree | **CLEAN** |
| test working tree | **DIRTY** (`?? 9`, 무해한 빈 파일 carry) |
| npm test baseline (@test 3d7f13b carry) | **2171/2171 PASS** (TSR 1396차) |
| merge | **carry SYNCED** `3d7f13b`→`cadd74a` (1 commit) |
| npm test post-merge | **2180/2180 PASS** (737.93s, 420 files, +9 tests) |
| build | **1172 modules PASS** (10.28s @ test) |
| npm audit (high+, omit=dev) | **0** |
| live E2E | **SKIP** (merge 미실행 · bootstrap-disabled 122/25/0 carry) |
| transfer verdict | **PASS** |
| open issue (frontend) | **0** |
| cross-stream | **BLOCK** (BE pending 1@aeecc1b · FE SYNCED@cadd74a) |
| operation | **BLOCK** (origin/test push 566 BE+234 FE + QA-B317 + QA-B95 + QA-B116) |

## carry SYNCED commit (`3d7f13b..cadd74a`)

1. `cadd74a` — `feat(v1.2.1/G-REFUND-FEE-FE-WIRE): wire copay refund fee catalog into RefundRecordModal`

## diff stat (주요)

- `RefundRecordModal.jsx` + `.test.jsx` — 7-9 환불수수료 정책 catalog wire + net amount preview (G-REFUND-FEE-FE-WIRE)
- `BillingDetailPage.jsx` — `feePolicyCode` 전달
- `services.js` + tests — copay refund fee catalog API client

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-25T09:22:26+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-25 1396차)

> **1396차 PASS** — baseline carry `@58f3858` **2166/2166 PASS**(TSR 1394차) · develop pre-merge `@3d7f13b` **2171/2171 PASS**(740.00s) · merge **EXECUTED** FF `58f3858`→`3d7f13b` (1 commit) · post-merge **2171/2171 PASS** · build **1171 PASS**(11.80s) · audit **0** · live E2E **122 PASS/25 SKIP/0 FAIL**(39.38s carry) · **★ QA-B316 Fixed** · cross-stream **SYNCED(FE@3d7f13b + BE@2adae59)** · operation **BLOCK**

## 1396차 검증 요약 (merge EXECUTED · PASS)

| 항목 | 결과 |
|---|---|
| test/develop HEAD | test `3d7f13b` · develop `3d7f13b` |
| ahead (`test..develop`) | **0** (SYNCED) |
| develop working tree | **CLEAN** |
| test working tree | **DIRTY** (`?? 9`, 무해한 빈 파일 carry) |
| npm test baseline (@test 58f3858 carry) | **2166/2166 PASS** (TSR 1394차) |
| npm test pre-merge (@develop 3d7f13b) | **2171/2171 PASS** (740.00s, 419 files, +5 tests) |
| merge | **EXECUTED** FF `58f3858`→`3d7f13b` (1 commit) |
| npm test post-merge | **2171/2171 PASS** (737.00s, 419 files) |
| build | **1171 modules PASS** (11.80s @ test) |
| npm audit (high+, omit=dev) | **0** |
| live E2E | **122 PASS / 25 SKIP / 0 FAIL** (39.38s · bootstrap-disabled carry) |
| transfer verdict | **PASS** |
| open issue (frontend) | **0** |
| cross-stream | **SYNCED** (FE@3d7f13b + BE@2adae59) |
| operation | **BLOCK** (origin/test push 565 BE+233 FE + QA-B95 partial + QA-B116) |

## merged commit (`58f3858..3d7f13b`)

1. `3d7f13b` — `feat(v1.2.1/US-O01): wire bathing indicator-27 compliance panel and pre/post observation fields`

## diff stat (10 files, +457 −20)

- `BathingScheduleIndicator27Panel.jsx` + `.test.jsx` — 2026 평가지표 #27 목욕 전후관찰 compliance panel (신규)
- `BathingScheduleForm.jsx` + `.test.jsx` — pre/post observation 필드 wire
- `BathingSchedulePage.jsx` + `.test.jsx` — indicator-27 panel mount
- `services.js` + `bathingScheduleServices.test.js` — indicator-27 catalog API client
- `components.css` — panel 스타일

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-25T08:09:39+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-25 1394차)

> **1394차 PASS** — baseline ROADMAP merged `@892122d` `npm test` **2166/2166 PASS**(738.36s) · develop pre-merge `@58f3858` **2166/2166 PASS**(733.91s) · merge **EXECUTED** FF `892122d`→`58f3858` (1 commit) · post-merge **2166/2166 PASS** · build **1168 PASS**(8.49s) · audit **0** · live E2E **122 PASS/25 SKIP/0 FAIL**(37.51s carry) · **★ QA-B314 Fixed** · cross-stream **SYNCED(FE@58f3858 + BE@5a5174a)** · operation **BLOCK**

## 1394차 검증 요약 (merge EXECUTED · PASS)

| 항목 | 결과 |
|---|---|
| test/develop HEAD | test `58f3858` · develop `58f3858` |
| ahead (`test..develop`) | **0** (SYNCED) |
| develop working tree | **CLEAN** |
| test working tree | **DIRTY** (`?? 9`, 무해한 빈 파일 carry) |
| npm test baseline (@test 892122d) | **2166/2166 PASS** (738.36s, 418 files) |
| npm test pre-merge (@develop 58f3858) | **2166/2166 PASS** (733.91s, 418 files, +6 tests) |
| merge | **EXECUTED** FF `892122d`→`58f3858` (1 commit) |
| npm test post-merge | **2166/2166 PASS** (733.52s, 418 files) |
| build | **1168 modules PASS** (8.49s @ test) |
| npm audit (high+, omit=dev) | **0** |
| live E2E | **122 PASS / 25 SKIP / 0 FAIL** (37.51s · bootstrap-disabled carry) |
| transfer verdict | **PASS** |
| open issue (frontend) | **0** |
| cross-stream | **SYNCED** (FE@58f3858 + BE@5a5174a) |
| operation | **BLOCK** (origin/test push 564 BE+232 FE + QA-B95 partial + QA-B116) |

## merged commit (`892122d..58f3858`)

1. `58f3858` — `fix(v1.2.1/QA-B312): normalize annual leave branch scope fallback`

## diff stat (2 files, +40 −4)

- `StaffAnnualLeavePage.jsx` — API branch scope trim before `BranchScopeNotice` render
- `StaffAnnualLeavePage.test.jsx` — whitespace `branchName` fallback regression (+6 tests carry)

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-25T07:01:38+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-25 1392차)

> **1392차 PASS** — baseline ROADMAP merged `@892122d` `npm test` **2160/2160 PASS**(854.52s) · develop/test **SYNCED** @ `892122d` · merge **carry SYNCED**(`9a583ec`→`892122d` 4 commits) · post-merge **2160/2160 PASS** · build **1168 PASS**(8.51s) · audit **0** · live E2E **122 PASS/25 SKIP/0 FAIL**(37.83s carry) · **★ QA-B311 Fixed** · **★ QA-B312 Fixed** · cross-stream **BLOCK(BE pending 3 @56831fc · FE SYNCED@892122d)** · operation **BLOCK**

## 1392차 검증 요약 (carry SYNCED · PASS)

| 항목 | 결과 |
|---|---|
| test/develop HEAD | test `892122d` · develop `892122d` |
| ahead (`test..develop`) | **0** (SYNCED) |
| develop working tree | **CLEAN** |
| test working tree | **DIRTY** (`?? 9`, 무해한 빈 파일 carry) |
| npm test baseline (@test 892122d) | **2160/2160 PASS** (854.52s, 417 files) |
| merge | **carry SYNCED** (`9a583ec`→`892122d` 4 commits) |
| npm test post-merge | **2160/2160 PASS** (854.52s · baseline=post-merge) |
| build | **1168 modules PASS** (8.51s @ test) |
| npm audit (high+, omit=dev) | **0** |
| live E2E | **122 PASS / 25 SKIP / 0 FAIL** (37.83s · bootstrap-disabled carry) |
| transfer verdict | **PASS** |
| open issue (frontend) | **0** |
| cross-stream | **BLOCK** (FE SYNCED · BE pending 3) |
| operation | **BLOCK** (origin/test push 563 BE+231 FE + QA-B95 partial + QA-B313) |

## merged commits (`9a583ec..892122d`)

1. `e985522` — `test(v2/G2b+G16): lock 5/5 CMS catalog parity and parity-rules fallback`
2. `5bb84a6` — `feat(v2/G-NHIS-ALT-KEY-AUDIT-BADGE): surface alt-key matched rows in NHIS UI`
3. `7b4c6f9` — `feat(uxd/163): add TransportParityRulesPanel + audit badge CSS (G16·US-G06)`
4. `892122d` — `fix(v1.2.1/QA-B312): harden StaffAnnualLeavePage branch scope vitest isolation`

## diff stat (14 files, +416 −43)

- `TransportParityRulesPanel.jsx` / `.test.jsx` — G16 parity-rules panel 신규
- `NhisAltKeyMatchedBadge.jsx` / `.test.jsx` — alt-key matched 배지
- `NhisReconciliationTable.jsx` / `.test.jsx` — NHIS 비교표 alt-key 표시
- `VisitNhisComparisonDetail.jsx` / `.test.jsx` + `nhisAltKeyMatch.js` — 상세 패널 확장
- `StaffAnnualLeavePage.test.jsx` — vitest isolation harden (QA-B312)
- `styles/components.css` — audit badge CSS

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-25T04:44:19+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-25 1390차)

> **1390차 BLOCK** — baseline ROADMAP merged `@9a583ec` `npm test` **2164/2165 PASS**(1 fail, 749.37s) · failing `StaffAnnualLeavePage.test.jsx` branch label assertion(`조회 지점`) · isolated `StaffAnnualLeavePage` **8/8 PASS**(6.72s · pollution lineage) · develop pre-merge `@5bb84a6` **SKIP**(pending 2) · merge **SKIP**(`9a583ec..5bb84a6`) · build **1168 PASS**(8.63s) · audit **0** · live E2E **SKIP**(merge 없음 · 122 PASS/25 SKIP/0 FAIL carry) · **QA-B311 Open update(BLOCK)** · **QA-B312 Open update(HIGH)** · cross-stream **BLOCK(BE pending 1 @4963535 · FE pending 2 @5bb84a6)** · operation **BLOCK**

## 1390차 검증 요약 (merge SKIP · BLOCK)

| 항목 | 결과 |
|---|---|
| test/develop HEAD | test `9a583ec` · develop `5bb84a6` |
| ahead (`test..develop`) | **0/2** |
| develop working tree | **CLEAN** |
| test working tree | **DIRTY** (`?? 9`, 무해한 빈 파일 carry) |
| npm test baseline (@test 9a583ec) | **2164/2165 with 1 fail** (749.37s, 418 files) |
| failing test | `src/pages/StaffAnnualLeavePage.test.jsx` (`조회 지점` 텍스트 assertion fail · line 132) |
| npm test isolated (`StaffAnnualLeavePage`) | **8/8 PASS** (6.72s · B266/B270 pollution lineage) |
| npm test pre-merge (@develop 5bb84a6) | **SKIP** (merge pending 2 · pre-merge 미실행) |
| merge | **SKIP** (`9a583ec..5bb84a6`) |
| npm test post-merge | **SKIP** (merge 미실행) |
| build | **1168 modules PASS** (8.49s @ test) |
| npm audit (high+, omit=dev) | **0** |
| live E2E | **SKIP** (merge 없음 · bootstrap-disabled 122 PASS / 25 SKIP / 0 FAIL carry) |
| transfer verdict | **BLOCK** |
| open issue (frontend) | **2** (`QA-B311`, `QA-B312`) |
| cross-stream | **BLOCK** (FE pending 2 + BE pending 1) |
| operation | **BLOCK** (origin/test push 560 BE+227 FE + QA-B95 partial + QA-B311/B312/B313) |

## pending commits (`9a583ec..5bb84a6`)

1. `5bb84a6` — `feat(v2/G-NHIS-ALT-KEY-AUDIT-BADGE): surface alt-key matched rows in NHIS UI`
2. `e985522` — `test(v2/G2b+G16): lock 5/5 CMS catalog parity and parity-rules fallback`

## diff stat (10 files, +180 −19)

- `TransportServiceFeePanel.jsx` / `.test.jsx` — parity-rules fallback 강화 + 회귀 케이스 추가
- `CmsPaymentMethodCatalogPanel.test.jsx` — G2b catalog parity 5/5 lock 테스트
- `NhisAltKeyMatchedBadge.jsx` / `.test.jsx` — alt-key matched 배지 신규
- `NhisReconciliationTable.jsx` / `.test.jsx` — NHIS 비교표 alt-key 표시 반영
- `VisitNhisComparisonDetail.jsx` / `.test.jsx` + `nhisAltKeyMatch.js` — 상세 패널/설정 확장

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-25T03:34:06+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-25 1388차)

> **1388차 BLOCK** — baseline ROADMAP merged `@9a583ec` `npm test` **Terminated exit 143**(632.08s partial) · develop pre-merge `@e985522` **SKIP**(pending 1) · merge **SKIP**(`9a583ec..e985522`) · build **1168 PASS**(10.28s) · audit **0** · live E2E **SKIP**(merge 없음 · 122 PASS/25 SKIP/0 FAIL carry) · **QA-B311 Open(BLOCK)** · **QA-B312 Open(HIGH)** · cross-stream **BLOCK(BE@37416ac SYNCED · FE pending 1 @e985522)** · operation **BLOCK**

## 1388차 검증 요약 (merge SKIP · BLOCK)

| 항목 | 결과 |
|---|---|
| test/develop HEAD | test `9a583ec` · develop `e985522` |
| ahead (`test..develop`) | **0/1** |
| develop working tree | **CLEAN** |
| test working tree | **DIRTY** (`?? 9`, 무해한 빈 파일 carry) |
| npm test baseline (@test 9a583ec) | **Terminated exit 143** (632.08s, summary missing) |
| npm test pre-merge (@develop e985522) | **SKIP** (merge pending 1 · pre-merge 미실행) |
| merge | **SKIP** (`9a583ec..e985522`) |
| npm test post-merge | **SKIP** (merge 미실행) |
| build | **1168 modules PASS** (10.28s @ test) |
| npm audit (high+, omit=dev) | **0** |
| live E2E | **SKIP** (merge 없음 · bootstrap-disabled 122 PASS / 25 SKIP / 0 FAIL carry) |
| transfer verdict | **BLOCK** |
| open issue (frontend) | **2** (`QA-B311`, `QA-B312`) |
| cross-stream | **BLOCK** (FE pending 1 + BE@`37416ac` SYNCED) |
| operation | **BLOCK** (origin/test push 560 BE+227 FE + QA-B95 partial + QA-B311/B312) |

## pending commits (`9a583ec..e985522`)

1. `e985522` — `test(v2/G2b+G16): lock 5/5 CMS catalog parity and parity-rules fallback`

## diff stat (3 files, +64 −17)

- `TransportServiceFeePanel.jsx` — parity-rules fallback test contract 보강
- `TransportServiceFeePanel.test.jsx` — G16 회귀 커버리지 확대
- `CmsPaymentMethodCatalogPanel.test.jsx` — G2b catalog parity 5/5 lock

---

<!-- doc:owner=TSR doc:audience=PLN,COD updated=2026-06-25T00:57:00+00:00 -->
# develop ↔ test diff 메타 — frontend (2026-06-25 1383차)

> **1383차 PASS** — baseline ROADMAP merged `@1db75d0` **2157/2157 PASS**(726.63s) · develop pre-merge `@9aeedfe` **2157/2157 PASS**(722.77s) · ★ merge **EXECUTED** FF `1db75d0`→`9aeedfe` (1) · post-merge **2157/2157 PASS**(724.22s) · build **1167 PASS**(12.25s) · audit **0** · live E2E **122 PASS/25 SKIP/0 FAIL**(bootstrap-disabled carry) · **★ QA-B306 Fixed @ `9aeedfe`** · cross-stream **SYNCED(FE@9aeedfe + BE@e12b084)** · operation **BLOCK**

## 1383차 검증 요약 (merge EXECUTED · post-merge PASS)

| 항목 | 결과 |
|---|---|
| test/develop HEAD | test `9aeedfe` · develop `9aeedfe` **SYNCED** |
| ahead (`test..develop`) | **0/0** |
| develop working tree | **CLEAN** |
| test working tree | **DIRTY** (`?? 9`, 무해한 빈 파일 carry) |
| npm test baseline (@test 1db75d0) | **2157/2157 PASS** (726.63s, 417 files) |
| npm test pre-merge (@develop 9aeedfe) | **2157/2157 PASS** (722.77s, 417 files) |
| merge | **EXECUTED** FF `1db75d0`→`9aeedfe` (1 commit) |
| npm test post-merge (@test 9aeedfe) | **2157/2157 PASS** (724.22s, 417 files) |
| build | **1167 modules PASS** (12.25s @ test) |
| npm audit (high+, omit=dev) | **0** |
| live E2E | **122 PASS / 25 SKIP / 0 FAIL** (39.73s · bootstrap-disabled carry) |
| transfer verdict | **PASS** |
| open issue (frontend) | **0** |
| cross-stream | **SYNCED** (FE@`9aeedfe` + BE@`e12b084`) |
| operation | **BLOCK** (origin/test push 557 BE+225 FE + QA-B95 partial) |

## merged commits (`1db75d0..9aeedfe`)

1. `9aeedfe` — `feat(v2/G2b+G16): wire CMS collection methods and transport parity-rules API`

## diff stat (13 files, +740 −20)

- `CmsCollectionPanel.jsx` / `.test.jsx` — G2b virtual-account + multi-account collection UI (new)
- `TransportServiceFeePanel.jsx` / `.test.jsx` — G16 parity-rules catalog wire
- `CmsPage.jsx` / `.test.jsx` — CMS page integration
- `services.js` / `settingsServices.test.js` — API bindings
- `cms.js` — config constants
- `competitorModuleCoverage.js` — module KPI sync
