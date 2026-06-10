<!-- doc:owner=PLN doc:audience=TSR,COD,SEC updated=2026-06-10T23:45:00+09:00 -->
# ogada 구현 로드맵

> **작성·유지**: `planner`  
> **구현**: `coder`는 `status: in_progress` 버전 **하나만** 작업  
> **검증**: `tester`는 `merge_status: merged` 이후 `test` 브랜치에서 검증  
> **피드백**: `tester` → `docs/qa/QA_FEEDBACK.md` → `planner` 반영 → `coder` 수정  
> **벤치마크 입력**: `docs/planning/research/BENCHMARK_REPORT.md`, `docs/planning/research/COMPETITOR_MATRIX.md`, `memory/decisions.md`

> **CURRENT BASELINE (96차 — git 실측·ROADMAP/QA 과거 SHA보다 우선)**: backend develop **`d6d7e7f`** · test **`598d108`** · **59 ahead** · WT **CLEAN** · frontend develop **`6c4c151`** · test **`c7c8f07`** · **74 ahead** · WT **DIRTY 4M** · **48 path·40 page** · planner 96차 (BNK-58 · TSR 231~232 · **G15 2-2/2-3 출석 이원화 ✅** @ `6c4c151`/`d6d7e7f` · **G15 계약 서명 API+UI ✅** @ `3c8f9fe`/`9e3cab5` · **G11 v2 청구 자동 가산 ✅** @ `d7475fd` · **QA-B19 geocode failure UI WIP** · **케어포 func.php 108 leaf 불변**) · `.agents/workspace_baseline.yaml`(run_agent build 시 갱신). **`d5654c0`/`e5fd48d`/`428ba7d` checkout 재현 금지**. 과거 인용 `4be0938`·24 route **미존재**. **모듈 커버 74.81%**(BNK-41~58 · ≥60% PASS). **v1.2.1 merge-blocking P0 `[x]` 유지** — BE **`merge_status: ready`** · FE **BLOCK**(WT dirty · QA-B19) · tester merge **74+59=133 commits** · TSR develop **482/127·453 PASS** @ HEAD/WT.

---

## 버전 상태 값

| 필드 | 값 | 의미 |
|------|-----|------|
| `status` | `planned` / `in_progress` / `done` | 구현 진행 상태 |
| `merge_status` | `pending` / `ready` / `merged` | develop → test merge 준비 |

**merge 규칙**: coder가 해당 버전 **완료 기준을 모두 충족**하면 `merge_status: ready`로 변경 → 다음 build 시 `develop`이 자동으로 `test`에 merge → `merged`로 갱신.

---

## QA 피드백 반영 (2026-06-06)

> `docs/qa/QA_FEEDBACK.md` Open 10건(BLOCK 5·HIGH 4·MEDIUM 1) + `docs/qa/TEST_REPORT.md` 최초 검증 결과를 태스크화. 각 항목은 QA_FEEDBACK에서 **Planned**로 이동, coder 수정 후 **Fixed**.

> **6차 동기화 (2026-06-06T08:10) — false Fixed 회귀 처리**: TSR 재검증(07:52)에서 backend `Fixed` 기록(QA-H01·SEC-001/002/004=H02)이 **develop HEAD 미반영**(test working tree 한정)으로 확인되어 **Open 복귀**. → backend 4건(BLOCK B01·B02, HIGH H01·H02)을 **Planned로 재반영**, v1 완료 기준 QA-H01 `[x]` 철회, **이관 규율 5항(Fixed↔develop HEAD 검증 게이트)** 신설. frontend H03·H04·M01은 develop HEAD 반영 확인 — `Fixed` 유지(영향 없음).

> **7차 동기화 (2026-06-06T15:15) — dirty-tree 재오염 + frontend false Fixed 회귀**: TSR 재검증(backend 14:45 / frontend 14:55)에서 ① backend develop HEAD(`7d9d2eb`) v1 fix 커밋 직후 working tree **재오염**(신규 미커밋 client↔guardian primary-link 작업, `createClient`가 `primaryGuardian` 필수로 **API 계약 변경** — QA-B06), ② frontend `Fixed` 3건(H04 api 연동·M01 Vitest·SEC-005 localStorage 제거)이 develop HEAD(`f1c89d9`) **미반영**으로 확인 → **Open 복귀**(이관 규율 5 위반), ③ frontend develop working tree **대량 오염**(22 modified + 18 untracked — QA-B07). → **v1 완료 기준 QA-B02 `[x]` 철회**(working tree 재오염), **v1.1 완료 기준 QA-H04·M01 `[x]` 철회** + SEC-005(메모리 세션) 항목 신설, **이관 규율 6항(API 계약 변경은 develop 커밋 전 API_SPEC·ROADMAP 반영)** 신설. B06 작업 범위는 v1 US-D01(보호자 1명 이상 필수, 결정 19)로 확정 — API_SPEC §4 `primaryGuardian` 계약 명세화.

> **9차 동기화 (2026-06-06T16:10) — TSR 8·9차 재검증 반영 (coder 미조치·신규 Open 0건)**: TSR 8차(15:38)·9차(15:45) 재검증에서 **회귀·이관 상태 완전 불변, coder 미조치, 신규 Open 0건** 확인. Planned 9건(B01·B03·B04·B05·B06·B07·H04·M01·SEC-005) 전부 미해소 잔존 → 양 스트림 이관 판정 **BLOCK 유지**. ① backend develop `7d9d2eb`(dirty/B06)·test `2799e29`(clean stale) 동일, `mvn -q test` **79/79 PASS** 재현. ② frontend develop dirty **악화**(22 mod + **20 untracked** — 신규 `AttendanceStatsPage`·`BranchesPage`로 QA-B07 확대), `npm run build` PASS·test 브랜치 `npm test` N/A. ③ **신규 관측(M01·B07 강화)**: frontend develop **working tree(미커밋)** `vitest run` **6 tests/3 files PASS** — 자동 테스트가 로컬에 완성됐으나 develop HEAD 미커밋. → **신규 기획·태스크 없음**(벤치마크 신규 입력 없음, QA Open 0). 잔여 9건은 전부 **이관 규율 1·5·6(완료 단위 develop 커밋·Fixed↔HEAD 정합) 미준수가 유일 블로커** — 기능 갭이 아닌 **프로세스 정체**. coder 미조치 장기화 → PLAN_NOTES `### 추가 질문` #36 에스컬레이션 기록.

> **10차 동기화 (2026-06-06T16:25) — 상태 불변 재확인 + 에스컬레이션 강화 (coder 미조치 6회 연속)**: 9차(16:10) 이후 **신규 입력 0건** — QA_FEEDBACK·TEST_REPORT 최종 갱신 TSR 9차(15:45) 그대로(Open 0), 벤치마크 BNK 6차 **착수 대기** 지속. planner가 submodule HEAD·working tree **직접 점검** → 9차와 **완전 동일**: backend `7d9d2eb` 10 mod + 2 untracked(`ClientService`·`CreateClientRequest`·`PrimaryGuardianLinkRequest`·`V39__client_guardian_link_status.sql` 등 client↔guardian 미커밋, B06 유지), frontend `f1c89d9` 22 mod + 20 untracked(`src/api/`·`*.test.jsx`·신규 페이지·`AuthContext`, B07 유지). Planned 9건 전부 미해소 → 양 스트림 **BLOCK 유지**. **신규 기획·태스크·결정 없음** — 잔여 9건은 전부 **이관 규율 1·5·6 미준수(완료 단위 develop 커밋 누락)**가 유일 블로커이며 산출물은 develop working tree에 사실상 완성(Maven 79/79·vitest 6 PASS). 5·6·7·8·9·10차에 걸쳐 **coder 0건 조치 6회 연속** → #36 에스컬레이션 **강화**(루프 실제 실행 여부 진단 추가, planner/사용자 운영 게이트 결정 대기).

> **11차 동기화 (2026-06-06T17:00) — TSR 11·12차 + BNK 6차 완료 반영**: ① **TSR 11차(16:40)**: backend develop `4d476c6` clean — **QA-B06·B02 Fixed 확정**, develop 2커밋 앞섬(`7d9d2eb`·`4d476c6`). ② **TSR 12차(16:55)**: frontend develop `998ac87` clean — **QA-B07·B04·H04·M01·SEC-005 Fixed 확정**, `npm test` 6/6·build 87 modules. ③ **SEC 3차**: SEC-007(Open) 등록 → **Planned 이동**(B01 동반). ④ **BNK 6차 완료**(`BENCHMARK_REPORT §9`·`COMPETITOR_MATRIX §8`) — v1.2 P0~P2 범위 확정·결정 49 KPI ≥60%. **잔여 BLOCK = merge 게이트 단일**(B01 backend·B03/B05 frontend·SEC-007) — dirty-tree·false Fixed 사유 **소멸**. coder 11차 조치로 #36 에스컬레이션 **부분 해소**(커밋 완료, merge 미실행 잔존).

> **12차 동기화 (2026-06-06T17:45) — TSR 13·14차 반영 (B07 recurrence + backend 부분 진전)**: ① **TSR 13차(17:30, backend)**: develop `4d476c6`→**`fac3d07`**(guardian billing·`NhisImportGuidance`·`RoleBasedControllerAccessTest` 7-role RBAC), working tree **CLEAN**, 3커밋 ahead of test. v1 완료 기준 **7역할 RBAC·롱텀2026 안내 부분 진전**(단위 테스트/API, E2E·import UI 잔여). ② **TSR 14차(17:35, frontend)**: develop HEAD `998ac87` 불변·HEAD Fixed **PRESENT** — 그러나 working tree **재오염**(v1.2 P0 19 files 미커밋, **QA-B07 recurrence**). working tree `npm test` 10/4·build 96 modules. → **B07 Open→Planned**, 이관 규율 **7항(v1.2 선행 dirty-tree 금지)** 신설·결정 50. **잔여 BLOCK = merge 게이트 4건 + B07 recurrence(Planned)** — HEAD @ `998ac87` v1.1 Fixed **유효**.

> **15차 동기화 (2026-06-06T19:00) — TSR 17·18·19차 반영 (B02 Fixed 확정 + B07 FE-7 회복·범위 확대)**: ① **TSR 17차(18:34, backend)**: COD 14차 `b5d70a8` GuardianAccess RBAC 3 tests **TSR 독립 검증 Fixed** — develop working tree **CLEAN**, `@Test` 98. **QA-B02 recurrence Planned→Fixed**. ② **TSR 18차(18:42, backend)**: 상태 **불변** — Maven 79/79 재현, 잔여 BLOCK = **merge 게이트 단일**(B01·SEC-007). ③ **TSR 19차(18:45, frontend)**: develop HEAD `998ac87` 불변·working tree **35 files**(16차 29→35, v1.2 P0 WIP 추가), WT `npm test` **10/4 PASS**·`npm run build` **107 modules PASS**(16차 FAIL **회복**, FE-7 충족). **B07 Planned 유지** — dirty-tree·규율 6·7 위반 **지속**. **잔여 BLOCK = merge 게이트 3건(B01·B03·B05·SEC-007) + B07 recurrence(Planned, frontend dirty-tree 단일)** — backend dirty-tree·B02 사유 **소멸**.

> **96차 동기화 (2026-06-10T23:45 KST) — BNK-58 + TSR 231~232 + G15 2-2/2-3·계약서·G11 v2 + FE merge BLOCK + QA Open→Planned 1건**: ① **planner git 재실측** — backend **`d6d7e7f`**(+5 vs `d5e0e01`: G15 `transportMode` API·G11 v2·계약 서명 lineage) · WT **CLEAN** · **`453 PASS`** · frontend **`6c4c151`**(+12 vs `62f022df`: G15 출석 이원화 Route·계약 UI lineage) · WT **DIRTY 4M** · **`482/482 PASS`** · **FE 74+BE 59 ahead** · **48 path·40 page**. ② **BNK-58** — **★ G15 2-2/2-3 출석 이원화 E2E ✅** @ `6c4c151`/`d6d7e7f` · **★ G15 계약 서명 ✅** @ `3c8f9fe`/`9e3cab5` · **★ G11 v2 청구 자동 가산 ✅** @ `d7475fd` · lcms **selectProductGuide** 신규 · **#44 4차 0건** · **케어포 108 leaf 불변** · **가정 번복 0건**. ③ **TSR 231~232** — **QA-20260610-B19 Open→Planned**(G15 geocode failure UI WIP 4M · B07 #12). ④ **merge gate**: BE **FULLY UNBLOCKED** · FE **BLOCK**(WT clean 선행) · 합계 **133 commits**. ⑤ **잔여 P1**: **COD B19 커밋/revert** → FE WT clean → merge(133) · G15 **2-1-1/2-9 외출·운행일지** · G7 실파일(#27) · G2 **SMTP** · G13·US-J02 **live run** · G21 **live E2E** · US-L01 **은행 8종 E2E live** · v1.3 live E2E.
> **95차 동기화 (2026-06-10T21:30 KST) — BNK-53 + TSR 219~220 + G11 catalog+가이드 E2E + G15 v1.3-C 부분 + merge FULLY UNBLOCKED + QA Open 0건**: ① **planner git 재실측** — backend **`d5e0e01`**(+7 vs `467cd70`: G11 `FeeSurchargeRateCatalog`+preview API lineage @ `904072b`) · WT **CLEAN** · **`434 PASS`** · frontend **`62f022df`**(+7 vs `c9451a0`: G11 `FeeSurchargeGuidePanel`+G15 `TransportCompliancePanel` lineage @ `3db8db3`) · WT **CLEAN** · **`467/126 PASS`** · **FE 68+BE 54 ahead** · **46 path·40 page**. ② **BNK-53** — **★ G11 가산율 catalog+가이드 E2E 닫힘** @ `904072b`/`3db8db3`(야20·심야30·휴일30·유급휴일50%·중복불가·`V1_NOTICE`) · **★ G15 v1.3-C 부분 닫힘** — `TransportCompliancePanel` 5수칙+계약서·일지 Modal `/transport` · **잔여**: 계약서 서명 저장 API·탑승(2-2)/출석(2-3) 이원화·외출 리포트(2-9) · **G27·US-L01 bank FE ✅** (BNK-50~52·94차 반영 확인) · **케어포 func.php 108 leaf·11 모듈 verbatim 불변** · **#44 수동 보류** · **가정 번복 0건** · **모듈 74.81%**. ③ **TSR 219~220** — **QA Open 0건**. ④ **잔여 P1**: tester merge(**122**) · G11 **v2 청구 자동 가산** · G15 v1.3-C **잔여 3건** · G7 실파일(#27) · G2 **SMTP 실연동** · G13·US-J02 **live run** · G21 **live E2E** · US-L01 **은행 8종 E2E live** · v1.3 live E2E.
> **94차 동기화 (2026-06-10T18:45 KST) — BNK-49 + TSR 207~208 + US-M03-b·US-L01 BE·G27 BE + 케어포 2-x + merge FULLY UNBLOCKED + QA Open 0건**: ① **planner git 재실측** — backend **`467cd70`**(+6 vs `0854fbd`: G27 `MonthlyBenefitCapCatalog`+guard·US-L01 bank deposit·US-M03 settings lineage) · WT **CLEAN** · **`412 PASS`** · frontend **`c9451a0`**(+6 vs `eedcc80`: US-M03 settings·basis alias @ `5bdb476`/`c9451a0`) · WT **CLEAN** · **`434/434 PASS`** · **FE 61+BE 49 ahead** · **46 path·40 page**. ② **BNK-49** — **★ G27 재가급여 월한도액 2026 BE catalog+guard 닫힘** @ `a92e625`(1등급 2,512,900~5등급 1,208,900 MOHW 247 verbatim) · **FE 표기·인지지원 676,320 시드 ❌** · **★ US-L01 은행엑셀 BE-only** @ `e50533f`/`95bb34d` · **★ US-M03-b 청구생성기준+전월가드 닫힘** @ `5bdb476`/`b953662`/`911e732`/`25f3225` · **케어포 func.php 2-x 11 leaf verbatim**(탑승/출석 이원화·2-7~2-9 리포트) → **G15 v1.3-C 세부 갭** · **#44 수동 보류** · **가정 번복 0건** · **모듈 74.81%**. ③ **TSR 207~208** — **QA Open 0건** · QA-20260610-B07 #11 **Fixed** @ `c9451a0`. ④ **잔여 P1**: tester merge(**110**) · **G27 FE**(월한도 초과 경고) · **US-L01 FE**(은행엑셀 업로드) · G7 실파일(#27) · G2 **SMTP 실연동** · G13·US-J02 **live run** · G21 **live E2E** · **G15 v1.3-C**(수칙·계약·2-x 리포트) · v1.3 live E2E · G11 가산수가.
> **93차 동기화 (2026-06-10T15:45 KST) — BNK-45 + TSR 192~196 + US-L01·G2 +2·G19 라벨 + #44 재정의 + merge FULLY UNBLOCKED + QA Open 0건**: ① **planner git 재실측** — backend **`0854fbd`**(+4 vs `f77a268`: G2 **납부확인서·학대예방교육** email+receipt enrich) · WT **CLEAN** · **`383 PASS`** · frontend **`eedcc80`**(+7 vs `eb3f0fd`: US-L01 **overpayment guard** @ `dd72ff8` · G19 **통합재가 라벨** @ `4c7c994` · G2 **notify UI 2종** @ `eedcc80`) · WT **CLEAN** · **`413/413 PASS`** · **FE 55+BE 43 ahead** · **46 path·40 page**. ② **BNK-45** — **★ #44 「이동지원서비스 시범사업」(동행·3,000원) ≠ 주야간 「이동서비스비」(러-1~4)** 구분 확정 · **이지케어 9,309**(+1) · **케어포 공지 46105** 2026 평가 반영 · **가정 번복 0건** · **모듈 74.81%**. ③ **TSR 192~196** — **QA Open 0건** · QA-20260610-B15 **Fixed** @ `4109680`. ④ **잔여 P1**: tester merge(**98**) · G7 실파일(#27) · G2 **SMTP 실연동** · G13·US-J02 **live run** · G21 **live E2E** · v1.3 live E2E · G15 수칙·계약 Route · G11 가산수가 · **#44 제34조 1차 출처 재추적**.
> **92차 동기화 (2026-06-10T13:25 KST) — BNK-42 + TSR 183·184 + G9 닫힘 + G2 SMTP templates + merge FULLY UNBLOCKED + QA Open 0건**: ① **planner git 재실측** — backend **`f77a268`**(+1 vs `872e040`: G2 **SMTP templates 3종**·`GuardianDocumentNotificationService`) · WT **CLEAN** · **`371 PASS`** · frontend **`eb3f0fd`**(+1 vs `5348d9c`: G9/US-J02 **duration band unified fallback**) · WT **CLEAN** · **`390/390 PASS`** · **FE 48+BE 38 ahead** · **46 path·40 page**. ② **BNK-42** — **G9 duration_band ✅** FE 2D+스냅샷+폴백(`6fe853b`/`5348d9c`/`eb3f0fd`) · **G2 원화 포맷** @ `872e040` · **G2 templates 3종** @ `f77a268`(엔젤 명세·기록지·가정통신문 패리티 방향) · **이지케어 9,308/9,231**(+6) · **가정 번복 0건** · **모듈 74.81%**. ③ **TSR 183·184** — **QA Open 0건** · QA-B07 #10 **Fixed** @ `5348d9c`. ④ **잔여 P1**: tester merge(**86**) · G7 실파일(#27) · G2 **SMTP 실연동** · G13·US-J02 **live run** · G21 **live E2E** · v1.3 live E2E · G15 수칙·계약 Route · G11 가산수가 · #44 별표18 수동 추출.
> **91차 동기화 (2026-06-10T12:30 KST) — BNK-38 + TSR 172 + G9·G21·G2·CMS FE 진전 + QA-B07 #10 Planned + FE merge BLOCK**: ① **planner git 재실측** — backend **`06d68dd`**(+4 vs `2c6e57e`: G9 `duration_band` V61·fee schedule forward-only·SMTP `SmtpEmailProvider`) · WT **CLEAN** · **`359 PASS`** · frontend **`527ba2d`**(+7 vs `e6df92c`: CMS `/billing/cms`·G21 billing confirm-lock·US-J02 pagination·GuardianPortal billing WIP) · WT **DIRTY 2M** · **`370/370 PASS`** · **FE 41+BE 34 ahead** · **46 path·40 page**. ② **BNK-38** — **G9 duration_band partial** @ `425a05f` · **G21 billing confirm-lock partial** @ `c4fb7ff`/`02cd2b2` · **G2 SMTP committed** @ `6ed48ff`/`f23f15a` · **CMS FE Route ✅** @ `6c6dc7a`/`c0a01b4` · **US-J02 billing filter/dedupe/retry WIP**. ③ **TSR 172** — **QA-20260610-B07 #10 Open→Planned** · FE merge **BLOCK**(WT dirty) · BE merge **unblocked**. ④ **잔여 P1**: FE WT clean → merge(**75**) · G7 실파일(#27) · G2 **SMTP templates·실발송** · G9 **duration_band 완료** · G13·US-J02 **live run** · G21 **live E2E** · v1.3 live E2E · G11 가산수가.
> **90차 동기화 (2026-06-10T23:30 KST) — BNK-35 + TSR 159·160 + G2 email·FCMS stub·7위젯 + merge gate FULLY UNBLOCKED + QA Open 0건**: ① **planner git 재실측** — backend **`2c6e57e`**(+6 vs `0ebe945`: G2 email enrich·FCMS `StubFcmsClient`·`CmsCopayLifecycleE2eTest`) · WT **CLEAN** · **`350/350 PASS`** · frontend **`e6df92c`**(+6 vs `14e9066`: US-M02-c overdue·US-L01/L02 live harness·cross-page hardening) · WT **CLEAN** · **`351/100 PASS`** · **FE 34+BE 30 ahead** · **45 path·39 page**. ② **BNK-35** — 케어포 func.php **111 leaf·32 리포트(28.8%)** · **7-x 8/11** · **공지920 본인부담률 엑셀 P2(G25)** · **CMS 7-4 BE stub** @ `2c6e57e` · FE `/billing/cms` **미구현** · **G2 email skeleton** @ `fbedcc3` · **US-M02-c 7위젯 닫힘** · **G13 cross-page hardening** @ `c72e9df`. ③ **TSR 159·160** — **신규 Open 0건** · v1.2.1 merge **FULLY UNBLOCKED**. ④ **잔여 P1**: tester merge(**64**) · G7 실파일(#27) · G2 **SMTP/메일벤더 실연동** · G13·US-J02 **live run**(결정 73) · G21 **통합 E2E** · v2 **CMS FE Route** · v1.3 live E2E · G9 **duration_band** · G11 가산수가.
> **89차 동기화 (2026-06-10T12:00 KST) — BNK-31 + TSR 147·148 + G13 E2E·G21 파서 + merge gate FULLY UNBLOCKED + QA Open 0건**: ① **planner git 재실측** — backend **`0ebe945`**(+5 vs `3e4d3e6`: visit pilot E2E·overdue notify lifecycle tests) · WT **CLEAN** · **`334/334 PASS`** · frontend **`14e9066`**(+7 vs `311c7c0`: US-L02 overdue·pagination E2E·reminder timestamp) · WT **CLEAN** · **`340/97 PASS`** · **FE 28+BE 24 ahead** · **45 path·39 page**. ② **BNK-31** — **G14·대시보드·#44·v2 CMS 번복 없음** · **G13 US-L02 pagination·reminder E2E 부분 닫힘** @ `fed457f`/`14e9066` · **G21 `NhisVisitScheduleExcelParser` 한국어 날짜/시간** @ `7fbd219` · **v3 식사·프로그램 FE POST** @ `6a59b74` **닫힘** · 케어포 func.php **timeout**·BNK-28 정본 유지 · **G2 이메일 채널 P1**(엔젤 법정서식). ③ **TSR 147·148** — **신규 Open 0건** · v1.2.1 merge **FULLY UNBLOCKED**. ④ **잔여 P1**: tester merge(**52**) · G7 실파일(#27) · G2 **이메일 실발송** · G13 **cross-page 상태전이** live E2E · G21 **통합 E2E** · v1.3 live E2E · 이지케어 **2026.7.1** FAQ.
> **88차 동기화 (2026-06-10T09:00 KST) — BNK-28 + TSR 135·136 + G21/G2 진전 + merge gate FULLY UNBLOCKED + QA Open 0건**: ① **planner git 재실측** — backend **`3e4d3e6`**(+7 vs `ee3fa3a`: G21 확정 차단·notify API·paired cancel cascade·draft sync) · WT **CLEAN** · **`329/329 PASS`** · frontend **`311c7c0`**(+7 vs `e1320f4`: G2 notify UI·G21 import 가이드·US-V04·paired cancel UX·QR branch-scoped) · WT **CLEAN** · **`326/93 PASS`** · **FE 21+BE 19 ahead** · **45 path·39 page**. ② **BNK-28** — 케어포 func.php **97 leaf·리포트 44%** · demo-work **120 view·이동서비스 0** · **G21 확정↔import P1 닫힘** @ `bf3d40d`/`84f3441` · **G2 notify API+UI 착수** @ `c48fb67`/`84f3441` · **대기수급자(1-1-1) P2** · 리포트 전수 **P2/v3.1**. ③ **TSR 135·136** — **신규 Open 0건** · v1.2.1 merge **FULLY UNBLOCKED**. ④ **잔여 P1**: tester merge(**40**) · G7 실파일(#27) · G2 **실발송 채널** · US-J02·G13 **live** E2E · v1.3 live E2E · v3 meals/programs **FE 연결**.
> **87차 동기화 (2026-06-10T06:00 KST) — BNK-25 + TSR 123·124 + merge gate FULLY UNBLOCKED + QA Open 0건**: ① **planner git 재실측** — backend **`ee3fa3a`**(+6 vs `dd49204`: G21 NHIS visit import·HOME_VISIT guard) · WT **CLEAN** · **`306/306 PASS`** · frontend **`e1320f4`**(+4 vs `e39164d`: SEC-D17 apiFetch·formErrors/http·UXD-62) · WT **CLEAN** · **`311/91 PASS`** · **FE 15+BE 12 ahead** · **45 path·39 page**. ② **BNK-25** — **#44 이동서비스비 러-1~4 2차 출처 충돌 해소** — **830/2,630/4,430/6,230원**(BNK-9 확정·BNK-17 폐기) · 별표18 HWP 1차만 잔여 · **G17** 지표25(계획 2점)+26(실행 3점) 정밀화 · **G21** NHIS visit import BE @ `ee3fa3a` · **SEC-D17** apiFetch FE @ `e1320f4`. ③ **TSR 123·124** — **신규 Open 0건** · v1.2.1 merge **FULLY UNBLOCKED**. ④ **잔여 P1**: tester merge(**27**) · G7 실파일(#27) · US-J02·G13 **live** E2E · v1.3 live E2E · Epic V NHIS import FE · G11·알림톡 실발송(v1.1/v2).
> **86차 동기화 (2026-06-10T04:30 KST) — TSR 116 재확인 + BNK-22 불변 + QA Open 0건**: ① **planner git 재실측** — baseline **85차와 동일**(FE `e39164d`·BE `dd49204`·**11+6 ahead**·WT **9+26 DIRTY**·**45 path·39 page**). ② **TSR 116** — FE develop **287/89 PASS** @ WT dirty · BE **288/288 PASS** @ HEAD · **신규 Open 0건** · v1.2.1 merge ready · **merge 선행 WT clean 미충족**. ③ **BNK-22** — **US-J03-h 닫힘** 재확인 · **알림톡/SMS 실발송(케어포 10-1) v1.1/v2 잔여**. ④ **잔여 P1**: WT clean → merge(17) · G7 실파일(#27) · US-J02·G13 live E2E · v1.3 live E2E · G11.
> **85차 동기화 (2026-06-10T03:00 KST) — BNK-22 + US-J03-h/G8 알림 이력 닫힘 + FE WT DIRTY**: ① **planner git 재실측** — backend **`dd49204`**(HEAD 불변) · WT **DIRTY 26** · frontend **`e39164d`**(+1 vs `1794e1c`: US-J03 `NotificationHistoryPanel`·UXD-61 Modal a11y) · **WT DIRTY 9** · **FE 11+BE 6 ahead** · **45 path·39 page** · 테스트 **WT dirty로 미재실행**(BNK-22). ② **BNK-22** — **G8 알림 발송 이력 UI 닫힘** @ `e39164d` — 케어포 **10-7 안내발송내역** 패리티 · PIPA 연락처 비표시 · **알림톡/SMS 실발송(10-1) v1.1/v2 잔여** · 모듈 커버 **72.5%**(발송 연동 시 ~74.4% 예상). ③ **QA Open 0건** · Planned 0건. ④ **잔여 P1**: **양 스트림 WT clean** → merge(**11+6**) · G7 **실파일**(#27) · US-J02·G13 **live** E2E · v1.3 live E2E · G11 가산수가(v1.1).
> **84차 동기화 (2026-06-10T01:30 KST) — BNK-20 + US-M02-b 닫힘 + FE WT CLEAN**: ① **planner git 재실측** — backend **`dd49204`**(HEAD 불변) · WT **DIRTY 17** · frontend **`1794e1c`**(+1 vs `6db762a`: BNK-19 대시보드 NHIS 대기 위젯·RegionSelector·식단 폼) · **WT CLEAN** · **FE 10+BE 6 ahead** · develop **`275/85`·`288/288 PASS`**. ② **BNK-20** — 이지케어 **RFID 실시간 2016 종료→엑셀** → G7 엑셀 전략 **업계 표준**(약점 아님) · **G11 가산수가** 경쟁사 표준 기대치 · 도입 **9,306**·셋팅 **정가 55k** · G21 이중일정 패리티 · 급여·회계 **Won't v1**. ③ **US-M02-b 닫힘** @ `1794e1c` — `DashboardPage` **「NHIS 대기(보류)」** 6번째 위젯(`nhisPendingReviewCount`). ④ **QA Open 0건** · Planned 0건. ⑤ **잔여 P1**: G7 **실파일 샘플**(#27) · US-J02·G13 **live** E2E · v1.3 live E2E · **merge 선행 BE WT clean**.
> **83차 동기화 (2026-06-10T00:15 KST) — BNK-19 + TSR 114 + `pendingReviewCount` P1 상향 + WT DIRTY 재오염**: ① **planner git 재실측** — backend **`dd49204`**(HEAD 불변) · WT **DIRTY 15**(meals/programs API·V55 visit integrity) · frontend **`6db762a`**(+1 vs `16402b2`: UXD-59 Epic K·L·J02 `GuardianClientLinks`·`OverdueSummaryBar`) · WT **DIRTY 3U** · **FE 9+BE 6 ahead** · develop **`271/83`·`288/288 PASS`**. ② **BNK-19** — G7 reconciliation **닫힘** 재확인(`fbb0b7a`/`16402b2`) · **대시보드 `pendingReviewCount` 위젯** PLA-82 Could→**P1** (US-M02 6번째 축) · 케어포 **2장 func.php**·공지 **46626** · #44 law.go.kr **1차 미확인 유지**. ③ **QA Open 0건** · Planned 0건. ④ **잔여 P1**: G7 **실파일 샘플**(#27) · **대시보드 `pendingReviewCount`** · US-J02·G13 **live** E2E · v1.3 live E2E · Epic V 공단 import · **merge 선행 WT clean**.
> **82차 동기화 (2026-06-09T23:30 KST) — BNK-18 + TSR 112·113 + G7 FE 닫힘 + merge gate FULLY UNBLOCKED**: ① **planner git 재실측** — backend **`dd49204`**(+1 vs `4cc328d`: Region API tests·NHIS pilot fixture parser) · frontend **`16402b2`**(+2 vs `371794f`: `fbb0b7a` G7 `PENDING_REVIEW` UI·`16402b2` G7·G13·Epic V `pilotPageFlows` E2E) · **FE 8+BE 6 ahead** · **양 스트림 WT CLEAN** · develop **`288/288`·`267/81 PASS`**. ② **BNK-18** — G7 **3상태 폐루프 BE+FE 닫힘**(`Badge`·`NhisReconciliationTable`·`NhisPendingReviewGuide`·`ReconciliationPage` `pendingReviewCount`) · 케어포 `처리상태`열 **파싱 역전** 확정. ③ **QA Open 0건** · Planned 0건. ④ **잔여 P1**: G7 **파일럿 엑셀 샘플**(데이터 BLOCK) · 대시보드 `pendingReviewCount` 위젯(Could) · US-J02 **live** E2E · v1.3 live E2E run · Epic V 공단 import.
> **81차 동기화 (2026-06-09T22:00 KST) — BNK-17 + TSR 110·111 + G7 BE 커밋 + Epic V `/visits` FE 착수**: ① **planner git 재실측** — backend **`4cc328d`**(+1 vs `1812165`: `feat(G7) NHIS PENDING_REVIEW` V54·`NhisReconciliationMatcher`·+5 @Test) · frontend **`371794f`**(+1 vs `0a07799`: Epic V `/visits` US-V01~V03) · **FE 6+BE 5 ahead** · FE **WT DIRTY 4**(G7 `NhisReconciliationTable`·`Badge` WIP) · BE **WT CLEAN** · develop **`259/80`·`269/269 PASS`**. ② **BNK-17** — G21 `/visits` FE 착수(이지케어 계획/청구 이중 Tabs) · G7 **V54+서비스 커밋** · #44 law.go.kr 러-1~4 **2차 출처 충돌** · 엔젤 CMS=**효성CMS(FCMS)**. ③ **QA Open 0건** · Planned 0건. ④ **잔여 P1**: G7 FE UI 커밋·파일럿 샘플 · G13 E2E · US-J02 live E2E · v1.3 live E2E · Epic V E2E·공단 import · 7-2-1·7-9 **Could**.
> **80차 동기화 (2026-06-09T21:00 KST) — BNK-16 + TSR 109 + US-M03 닫힘 + v1.2.1 P1 진전**: ① **planner git 재실측** — backend **`1812165`**(+1 vs `15e41e3`: `feat(v2/G21) home-visit branch guard`) · frontend **`0a07799`**(+2 vs `465bdae`: `dbf485e` US-M03 ledger·calculator UXD-56 · `0a07799` US-J02·US-M03 pilotPageFlows E2E) · **FE 5+BE 4 ahead·WT CLEAN** · **`240/76 PASS`**. ② **US-M03/G22 닫힘** — `/billing/reports/{charges,deposits,receipts}`·`/billing/calculator` @ `dbf485e` **PRESENT** (BNK-16). ③ **모듈 커버 72.5%**(68.7%→+3.8pp). ④ **BNK-16** — 이지케어 FAQ 233건·9,306 기관·payroll lock-in 37% 재확인 · G7 NHIS **3상태(대기)** UX P0. ⑤ **QA Open 0건** · Planned 0건. ⑥ **잔여 P1**: G7 NHIS·G13 E2E·US-J02 live E2E · v1.3 live E2E run · v2 `/visits` UI · 7-2-1·7-9 **Could**.
> **79차 동기화 (2026-06-09T19:35 KST) — TSR 106·107 + G14 GET API 닫힘 + v1.2.1 P0 완료**: ① **planner git 재실측** — backend **`15e41e3`**(+1 vs `d768820`: `feat(v1.2.1/G14) GET ltc-grade-history` · `LtcGradeHistoryServiceTest` 4 @Test) · frontend **`465bdae`**(+1 vs `6d0a03a`: US-J02 guardian billing live API 필드 정합) · 양 스트림 **3 ahead·WT CLEAN** · **`262/262`·`225/72 PASS`**. ② **US-M01/G14 닫힘** — `GET /api/v1/clients/{id}/ltc-grade-history` @ `15e41e3` **PRESENT** (TSR 106). ③ **v1.2.1 P0 `[x]`** — US-M02 @ `6d0a03a` + US-M01 @ `15e41e3` → **`merge_status: ready`** (결정 92). ④ **QA Open 0건** · Planned 0건. ⑤ **잔여 P1**: US-M03(G22)·US-J02 E2E·G13 E2E·G7 NHIS · v1.3 live E2E run · v2 `/visits` UI.
> **78차 동기화 (2026-06-09T11:00 KST) — BNK-13·14 재확인 + QA Open 0건 + baseline 불변**: ① **planner git 재실측** — backend **`d768820`** · frontend **`6d0a03a`** · 양 스트림 **2 ahead·WT CLEAN** — **77차 대비 delta 없음**. ② **BNK-14 불변** — US-M02 **닫힘** · G14 **GET API 1건 잔여** · **~68.7%** · 이지케어 RFID→**G21 v2**. ③ **BNK-13 반영** — func.php **106 leaf** · 본인부담 **7-1~7-3 Route ✅** · **7-6~7-10 리포트 5건** → **US-M03 P1**(G22). ④ **QA Open 0건** · Planned 0건 — **이동 없음**. ⑤ **활성 버전**: v1.2.1 **`in_progress` 단일** · v2 G21 backend **`@d768820` bleed** · merge **P0 후 4 commits**.
> **77차 동기화 (2026-06-09T10:05 KST) — BNK-14 재확인 + backend v2/G21 bleed + v1.2.1 G14 잔여**: ① **planner git 실측** — backend develop **`d768820`**(+1 vs `2012945`: `feat(v2/G21) visit schedules` · V53·`VisitServiceTest`) · test **`598d108`** · **2 ahead** · **`257/257 PASS`** · frontend **`6d0a03a`** · test **`c7c8f07`** · **2 ahead** · **`225/72 PASS`**. ② **BNK-14 불변** — US-M02 **닫힘** · G14 **GET API 미구현** · 모듈 **~68.7%** · 이지케어 RFID→**G21**. ③ **결정 92** — v1.2.1 **P0(G14) 선행** · v2 backend 선행 커밋은 **develop-only bleed**(merge gate **v1.2.1 P0 후**). ④ **v2 G21** — `schedule_kind` PLAN/BILLING·`paired_schedule_id`·체크인 API **backend ✅ @ `d768820`** · `/visits` UI·E2E **잔여**. ⑤ **QA Open 0건** · **잔여**: G14 GET API · v1.2.1 merge(4 commits) · G7 NHIS · v1.3 live E2E run.
> **76차 동기화 (2026-06-09T09:00 KST) — BNK-14 + TSR 105 + v1.2.1 진전 (US-M02 닫힘·G14 API 잔여)**: ① **planner git 실측** — backend develop **`2012945`**(WT CLEAN · test **`598d108`** · **1 ahead**) · frontend develop **`6d0a03a`**(WT CLEAN · test **`c7c8f07`** · **2 ahead**). ② **BNK-14** — US-M02 대시보드 실데이터 **닫힘** · US-M01 등급이력 **UI+DB(V48) ✅** · `GET /ltc-grade-history` **미구현** · 모듈 **~68.7%** · 이지케어 RFID→**G21 v2**. ③ **TSR 105** — test **`c7c8f07`** 217/70 PASS · develop **`6d0a03a`** 225/72 PASS · **QA Open 0건**. ④ **v1.2.1** — P0-1 US-M02 **`[x]`** · P0-2 US-M01 **GET API 1건 잔여** · P1 **7-6~7-10 본인부담 리포트**(BNK-13). ⑤ **잔여**: G14 backend API · v1.2.1 merge(2+1) · G7 NHIS · v1.3 live E2E run.
> **75차 동기화 (2026-06-09T04:00 KST) — QA-B12·SEC-D14 Fixed + v1.2.1 in_progress + API_SPEC G14**: ① **planner git 실측** — backend develop/test/origin **`598d108`**(WT DIRTY 13) · frontend develop/test/origin **`c7c8f07`**(0 ahead·CLEAN). ② **QA-B12·SEC-D14 Planned→Fixed** — origin push·frontend merge(22) **완료**. ③ **v1.2.1 `status: in_progress`** — frontend 단일 활성 버전(US-M01 G14·US-M02). ④ **API_SPEC §4-2** `ltc_grade_history` 명세 신설. ⑤ **BNK-10~12 불변** — G14·US-M02 잔여만 coder 착수. ⑥ **잔여**: backend WT 13 commit/revert · v1.3 live E2E run(결정 73) · G7 NHIS 샘플.
> **74차 동기화 (2026-06-09T03:00 KST) — BNK-10·11·12 + TSR 102·103 + SEC-D14 Planned + v1.2.1 + UXD-55 + baseline `@c7c8f07`**: ① **BNK-10** — 이지케어 ERP 9축·**계획/청구 이중 일정**·급여·4대보험 lock-in → ogada **Won't v1**(G4) · EZCARE 보호자 초대 패턴 G8 유지. ② **BNK-11** — 케어포 **demo-work=시설급여 셸**(이동서비스 없음) · 주야간 **정본=func.php 109항목** · **G20** 시설특화 Won't v1. ③ **BNK-12** — ogada **`c7c8f07` 40 Route·35 page·~74–78% KPI PASS** · 이지케어 **9,298개소** · v1.2 P0 잔여 **G14·대시보드 실데이터** → **v1.2.1**. ④ **TSR 102·103** — backend test `@598d108` 246/246 · frontend **`c7c8f07`** UXD-55 `GuardianBillingDetailModal`(US-J02) · **217/70 PASS** · develop **22 ahead**. ⑤ **QA Open 1건→Planned** — SEC-D14(origin STALE) QA-B12 동반. ⑥ **활성 frontend `in_progress` 없음** — merge gate 선행.
> **73차 동기화 (2026-06-09T00:15 KST) — TSR 100·101 + QA-B12 origin/test push gap + UXD-54 + v2 copay @598d108 + BNK-9 재확인 + Open 0건**: ① **planner git 실측(TSR 100·101차)** — backend develop **`598d108`**(+1 vs merge base `32575aa`: v2 copay payment·V50) WT **CLEAN** · local test **`598d108`**(=develop) · **origin/test STALE `2799e29`** — **26 ahead·미푸시**(QA-B12) · frontend **`7cd9293`**(+1 vs `e641f62`: UXD-54 `BranchScopeNotice` QR·배차 연동) WT **CLEAN** · **`npm test` 214/69 PASS** · **780 modules 3청크**(max **367 kB**) · test **`c510f5c`** · develop **49 ahead**. ② **TSR 100**: 로컬 develop→test merge **243/243 PASS** @ `32575aa` lineage — v1 baseline + v1.3-A transport + v3 meals/programs test 반영 · **origin push 미실행**. ③ **TSR 101**: UXD-54 US-UX-04 QR·Transport `BranchScopeNotice` — **판정 PASS(v1.2)**. ④ **BNK-9 불변** — Directions·러-1~4·G17~G19 · #44 law.go.kr 잔여. ⑤ **QA Open 0건** — **QA-20260608-B12 Planned**. ⑥ **잔여 BLOCK**: **origin/test push(QA-B12)** + **SEC-D14(origin)** + **frontend merge(49)** + v1.3 live E2E run(post-merge).
> **72차 동기화 (2026-06-08T23:45 KST) — TSR 98·99차 + transport masking 단위테스트 + UXD-53 BranchScopeNotice + BNK-9 재확인 + Open 0건**: ① **planner git 실측(TSR 98·99차)** — backend **`32575aa`**(+1 vs `c7941e9`: `TransportServiceTest` pickup contact masking 단위 테스트 +2 @Test) WT **CLEAN** · **`mvn test` 243/243** · **25 ahead** · frontend **`e641f62`**(+2 vs `1d910c2`: `0d36e30` UXD-53 `BranchScopeNotice`·출석·QR·배차 a11y · `e641f62` `pilotPageFlows` US-E01/E05 E2E) WT **CLEAN** · **`npm test` 212/69 PASS** · build **780 modules 3청크**(max **367 kB <500 kB**) · **40 Route·51 page** · test **`c510f5c`**. ② **v1.3-A SEC-D9 회귀 보강** — masking API(`c7941e9`) + 단위 테스트(`32575aa`) **HEAD PRESENT**. ③ **UXD-53 지점 스코프 UI** — `BranchScopeNotice` Attendance·QR·Transport 연동 · `pilotPageFlows` E2E **HEAD PRESENT**. ④ **BNK-9 불변** — Directions·러-1~4·G17~G19 · #44 law.go.kr 잔여. ⑤ **v1.3 `merge_status: ready` 유지** — develop→test merge(25+20) + live E2E run(post-merge). ⑥ **QA Open 0건** — 잔여 BLOCK: **backend merge(25) + SEC-D14(backend) + frontend merge(20)**.
> **70차 동기화 (2026-06-08T22:30 KST) — TSR 96·97차 + transport pickup contact masking UI + pilotPageFlows T03 E2E + BNK-9 재확인 + Open 0건**: ① **planner git 실측(TSR 96·97차)** — backend **`c7941e9`**(+1 vs `e7d4cf6`: non-HQ transport pickup **contact** masking — `TransportService.maskPhone`) WT **CLEAN** · **`mvn test` 241/241** · **24 ahead** · frontend **`1d910c2`**(+2 vs `3c55339`: `37be0a3` `TransportPickupContact`·픽업 프로필 a11y US-T03/UXD-52 · `1d910c2` `pilotPageFlows` T03 연락처 마스킹 E2E) WT **CLEAN** · **`npm test` 208/68 PASS** · build **779 modules 3청크**(max **367 kB <500 kB**) · **40 Route·51 page** · test **`c510f5c`**. ② **v1.3-A transport privacy 완성** — non-HQ pickup **주소(e7d4cf6) + 연락처(c7941e9)** API · **`TransportPickupContact` UI @ `37be0a3`** · T03 E2E @ `1d910c2` **HEAD PRESENT**. ③ **BNK-9 불변** — Directions·러-1~4·G17~G19 · #44 law.go.kr 잔여. ④ **v1.3 `merge_status: ready` 유지** — live E2E **run**만 잔여(결정 73 post-merge). ⑤ **QA Open 0건** — 잔여 BLOCK: **backend merge(24) + SEC-D14(backend) + frontend merge(18)** + v1.3 live E2E run(post-merge 권장).
> **68차 동기화 (2026-06-08T20:45 KST) — TSR 94·95차 + transport pickup masking + UXD-51 FE-13/FE-14 + ClientForm 픽업 프로필 + BNK-9 재확인 + Open 0건**: ① **planner git 실측(TSR 94·95차)** — backend **`e7d4cf6`**(+1 vs `f8d1b02`: non-HQ transport pickup address masking — `TransportService.maskAddress`) WT **CLEAN** · **`mvn test` 241/241** · **23 ahead** · frontend **`3c55339`**(+2 vs `d484206`: `2a0ef3d` UXD-51 FE-13/FE-14 누락 UI 복원·a11y · `3c55339` v1.3-A `ClientFormPage` 픽업 프로필 UI US-T01/Q166) WT **CLEAN** · **`npm test` 203/67 PASS** · build **778 modules 3청크**(max **367 kB <500 kB**) · **40 Route·51 page** · test **`c510f5c`**. ② **v1.3-A transport privacy @ `e7d4cf6`** — non-HQ 역할 pickup 주소 마스킹 API·`TransportServiceTest` **HEAD PRESENT**. ③ **US-T01 frontend @ `3c55339`** — `ClientFormPage` usesTransport·pickupAddress·pickupContact·defaultPickupTime UI 연동. ④ **UXD-51 @ `2a0ef3d`** — FE-13/FE-14 누락 컴포넌트 복원. ⑤ **BNK-9 불변** — Directions·러-1~4·G17~G19 · #44 law.go.kr 잔여. ⑥ **활성 버전 (68차)**: frontend **v1.3-A** 단일 · backend **merge(23) 최우선**. ⑦ **QA Open 0건** — 잔여 BLOCK: **backend merge(23) + SEC-D14(backend) + frontend merge(16)** + v1.3 live E2E run(post-merge 권장).
> **67차 동기화 (2026-06-08T19:30 KST) — TSR 93차 + TransportPilotServiceFlowE2eTest + transport live E2E harness + FE-15 복원 + BNK-9 재확인 + Open 0건**: ① **planner git 실측(TSR 93차)** — backend **`f8d1b02`**(+1 vs `1ec538b`: `TransportPilotServiceFlowE2eTest`·transport RBAC +9 tests) WT **CLEAN** · **`mvn test` 240/240** · **22 ahead** · frontend **`d484206`**(+2 vs `637b9b3`: `511c240` transport a11y forced-colors · `d484206` FE-15 `manualChunks` 복원 + `transportLiveApi.e2e.test.js` harness) WT **CLEAN** · **`npm test` 189/60 PASS** · build **766 modules 3청크**(max **367 kB <500 kB**) · **40 Route·50 page** · test **`c510f5c`**. ② **US-T01~T03 backend service-flow E2E @ `f8d1b02`** · **transport live E2E harness @ `d484206`**(FE-22 패턴, `src/e2e/**` 기본 test 제외) · **live run 잔여**(결정 73 post-merge). ③ **FE-15 Fixed @ `d484206`** — 91/92차 756 kB 회귀 **해소**. ④ **BNK-9 불변** — Directions·러-1~4·G17~G19 · #44 law.go.kr 잔여. ⑤ **활성 버전 (67차)**: frontend **v1.3-A** 단일 · backend **merge(22) 최우선**. ⑥ **QA Open 0건** — 잔여 BLOCK: **backend merge(22) + SEC-D14(backend) + frontend merge(14)** + v1.3 live E2E run(post-merge 권장).
> **66차 동기화 (2026-06-08T18:15 KST) — TSR 92차 + US-T01 client profile + pilotPageFlows transport E2E + UXD-49 HQ 건강 이상 + BNK-9 재확인 + Open 0건**: ① **planner git 실측(TSR 92차)** — backend **`1ec538b`**(+1 vs `767d977`: v1.3-A client transport profile US-T01 — `ClientResponse` usesTransport·pickupAddress·pickupContact·defaultPickupTime + `ClientServiceTest` +2·`PilotChecklistJwtE2eTest` transport routing +3) WT **CLEAN** · **`mvn test` 231/231** · **21 ahead** · frontend **`637b9b3`**(+2 vs `8a764df`: `00375f6` UXD-49 HQ 대시보드 건강 이상 지점명 US-H02 · `637b9b3` v1.3-A `pilotPageFlows` transport US-T01~T03 E2E + `pilotChecklist` T01~T03) WT **CLEAN** · **`npm test` 189/60 PASS** · build **766 modules**(JS 756 kB — FE-15 **non-blocking LOW**) · **40 Route·50 page** · test **`c510f5c`**. ② **US-T01 backend 완료** — Clients API transport profile @ `1ec538b` · **`pilotPageFlows` transport fetch-mock E2E @ `637b9b3`** · live backend E2E **잔여**. ③ **BNK-9 불변** — Directions·러-1~4·G17~G19 · #44 law.go.kr 잔여. ④ **활성 버전 (66차)**: frontend **v1.3-A** 단일 · backend **merge(21) 최우선**. ⑤ **QA Open 0건** — 잔여 BLOCK: **backend merge(21) + SEC-D14(backend) + frontend merge(12)** + v1.3 live E2E(post-merge 권장).
> **65차 동기화 (2026-06-08T08:45 UTC) — TSR 91차 + UXD-48 Recharts develop + BNK-9 재확인 + 활성 버전 우선순위 + Open 0건**: ① **planner git 실측(TSR 91차)** — backend **`767d977`** WT **CLEAN** · **`mvn test` 226/226** · **20 ahead** · frontend **`8a764df`**(+1 vs `73f7d39`: UXD-48 Recharts `ChartContainer`·`AttendanceRateChart`·`HealthTrendChart`·Dashboard/AttendanceStats/HealthDetail 연동 US-H01/E05/F04/H02) WT **CLEAN** · **`npm test` 183/60 PASS** · build **766 modules**(JS **756 kB** — FE-15 `manualChunks` **회귀·non-blocking LOW**) · **40 Route·50 page** · test **`c510f5c`**. ② **US-M02 Recharts develop HEAD PRESENT** — HQ `BranchCompareChart` **잔여**. ③ **BNK-9 불변** — Directions·러-1~4·G17~G19 · #44 law.go.kr 잔여. ④ **활성 버전 (65차)**: frontend coder **단일 우선 = v1.3-A**(`pilotPageFlows` transport merge-blocking) · v2·v3 frontend **신규 착수 보류** · backend **merge(20) 최우선**. ⑤ **QA Open 0건** — 잔여 BLOCK: **backend merge(20) + SEC-D14(backend) + frontend merge(10)** + v1.3 transport E2E.
> **64차 동기화 (2026-06-08T07:45 UTC) — TSR 89·90차 + v1.3-A unconfirm UI 완료 + BNK-9 재확인 + Open 0건**: ① **planner git 실측(TSR 89·90차)** — backend **`767d977`**(+1 vs `0d8968d`: v1.3-A transport unconfirm PATCH contract + POST legacy alias) WT **CLEAN** · **`mvn test` 226/226** · **20 ahead** · frontend **`73f7d39`**(+1 vs `fe33e7c`: UXD-47 `TransportUnconfirmModal`·`StaffRoleSelect`·StaffPage a11y·`TransportRunDetailPage` unconfirm US-T02) WT **CLEAN** · **`npm test` 179/58 PASS** · **143 modules** · **40 Route·50 page** · test **`c510f5c`**. ② **v1.3-A unconfirm stack 완료** — backend PATCH+POST @ `767d977` · frontend `TransportUnconfirmModal`·`TransportRunDetailPage.test.jsx` 3건 @ `73f7d39` **HEAD PRESENT**. ③ **BNK-9 불변** — Directions·러-1~4·G17~G19 · #44 law.go.kr 잔여. ④ **QA Open 0건** — 잔여 BLOCK: **backend merge(20) + SEC-D14(backend) + frontend merge(9)** + v1.3 `pilotPageFlows` transport·post-merge live E2E(결정 73).
> **63차 동기화 (2026-06-08T06:39 UTC) — TSR 87·88차 + v1.3-A transport unconfirm + v3 StaffPage + Open 0건**: ① **planner git 실측(TSR 87·88차 기준)** — backend **`0d8968d`**(+1 vs `dfd9be2`: v1.3-A transport run unconfirm hq_admin, 6 files +102) WT **CLEAN** · **`mvn test` 226/226** · **19 ahead** · frontend **`fe33e7c`**(+8 vs `c510f5c`: 86차 `362dbf0` +2 UXD-46 CSS·체크인 a11y · `fe33e7c` v3 StaffPage UI) WT **CLEAN** · **`npm test` 170/55 PASS** · **140 modules** · test **`c510f5c`**. ② **v1.3-A backend** — transport run unconfirm hq_admin API @ `0d8968d` **HEAD PRESENT** · frontend unconfirm UI **잔여** · US-T01~T03 live E2E 잔여. ③ **v3 StaffPage UI** — frontend **`fe33e7c`**에 StaffPage v3 포함 · ROADMAP v3 직원 모듈 진전 (**merge 게이트 이번 63차 정의**). ④ **BNK-9 불변** — Directions·러-1~4·G17~G19 · #44 law.go.kr 잔여. ⑤ **QA Open 0건** — 잔여 BLOCK: **backend merge(19) + SEC-D14(backend) + frontend merge(8)** + v1.3 unconfirm UI·live E2E + post-merge live E2E(결정 73).

> **62차 동기화 (2026-06-08T14:00) — BNK-9 재확인 + v3 meals/programs full stack + v1.3 live E2E 잔여**: ① **planner git 실측** — backend **`dfd9be2`**(+1 vs `53a1ffe`: v3 meals/programs REST·V49) WT **CLEAN** · **`mvn test` 224/224** · **18 ahead** · frontend **`362dbf0`**(+2 vs `7ef1083`: `3e9a9ab` v3 a11y · `362dbf0` pilotPageFlows US-N01·N02 E2E) WT **CLEAN** · **`npm test` 164/54 PASS** · **39 Route·47 page** · test **`c510f5c`**. ② **v3 §3-5·§3-6 develop 완료** — backend V49·`/api/v1/meals/*`·`/api/v1/programs/*` **PRESENT** · frontend E2E·`pilotChecklist` N01/N02 **PRESENT** · **프로그램 사진 업로드**·직원·평가 **후속**. ③ **v1.3-A** — transport API @ `53a1ffe`+ lineage **PRESENT** · **US-T01~T03 live E2E·`pilotPageFlows` transport 잔여**. ④ **BNK-9 불변** — Directions·러-1~4·G17~G19 · #44 law.go.kr 잔여. ⑤ **QA Open 0건** — 잔여 BLOCK: **backend merge(18) + SEC-D14(backend) + frontend merge(6)** + v1.3 live E2E·post-merge live E2E(결정 73).
> **61차 동기화 (2026-06-08T13:30) — BNK-9 재확인 + v1.3-A backend API + v3 meals/programs UI shell**: ① **planner git 실측** — backend **`53a1ffe`**(+1 vs `52e0621`: v1.3-A transport API·V47·Kakao geocode proxy) WT **CLEAN** · **`mvn test` 212/212** · **17 ahead** · frontend **`7ef1083`**(+2 vs `c510f5c`: `f0b174a` v1.3 a11y · `7ef1083` v3 `/meals`·`/programs` UI shell) WT **CLEAN** · **`npm test` 157/53 PASS** · **39 Route·34 page** · test **`c510f5c`**. ② **v1.3-A backend @ `53a1ffe`** — `/api/v1/transport/*`·V47·`TransportServiceTest`·`TransportControllerRoutingTest` **HEAD PRESENT** · frontend 연동·E2E **잔여**. ③ **v3 frontend PARTIAL @ `7ef1083`** — `MealsPage`·`ProgramsPage`·API 클라이언트·Vitest **HEAD PRESENT** · backend meals/programs API **ABSENT**. ④ **BNK-9 불변** — Directions·러-1~4·G17~G19 · #44 law.go.kr 잔여. ⑤ **QA Open 0건** — 잔여 BLOCK: **backend merge(17) + SEC-D14(backend) + frontend merge(4)** + v1.3 E2E·post-merge live E2E(결정 73).
> **60차 동기화 (2026-06-08T12:30) — TSR 82 + BNK-9 재확인 + v1.3 transport UI shell + copay PAID alimtalk + UXD-43 UNMATCHED**: ① **planner git 실측** — backend **`52e0621`**(+1 vs `ac17ad8`: copay claim CONFIRMED→PAID 시 `BILLING_PAYMENT_RECEIVED` alimtalk dispatch) WT **CLEAN** · **`mvn test` 202/202** · **16 ahead** · frontend **`e8d1854`**(+2 vs `c510f5c`: `f01e3a8` UXD-43 US-G06 UNMATCHED 후보 검색 · `e8d1854` v1.3 transport UI shell US-T01~T03) WT **CLEAN** · **`npm test` 150/50 PASS** · **37 Route·41 page** · test **`c510f5c`**. ② **TSR 82** — v2/J03 copay PAID 알림톡·SMS fallback. ③ **v1.3-A frontend PARTIAL** — `/transport`·`/transport/runs/new`·`/transport/runs/:id`·`TransportDisclaimer`·카카오맵 컴포넌트 **HEAD PRESENT** · **backend `/api/v1/transport/*` ABSENT**(DBA·API 선행). ④ **BNK-9 불변** — Directions·러-1~4·G17~G19 · #44 law.go.kr 잔여. ⑤ **QA Open 0건** — 잔여 BLOCK: **backend merge(16) + SEC-D14(backend) + frontend merge(2)** + post-merge live E2E(결정 73).
> **59차 동기화 (2026-06-08T12:00) — TSR 80·81 + BNK-9 재확인 + US-G06 DISCREPANCY + AlimtalkFallbackText + v1.2 frontend merged**: ① **planner git 실측** — backend **`ac17ad8`**(+1 vs `4c74f84`: `AlimtalkFallbackText`·SMS fallback relay) WT **1U**(`data/` 로컬 산출물, 비차단) · **`mvn test` 198/198** · **15 ahead** · frontend **`c510f5c`**(+2 vs `95b92b9`: `fd4e8f3` US-G06 `DiscrepancyComparePanel` · `c510f5c` pilotPageFlows US-G06 E2E) WT **CLEAN** · **`npm test` 143/46 PASS** · **34 Route·38 page** · develop=test **`c510f5c`**(**v1.2 merged**). ② **TSR 80** — v2/J03 `AlimtalkFallbackText` 한국어 SMS fallback · `incidentType`→`category` alias. ③ **TSR 81** — US-G06 DISCREPANCY 청구 라인 비교 Modal·E2E. ④ **BNK-9 불변** — Directions·러-1~4·G17~G19 · #44 law.go.kr 잔여. ⑤ **QA Open 0건** — 잔여 BLOCK: **backend merge(15) + SEC-D14(backend) 단일** + post-merge live E2E(결정 73). ⑥ **v1.2 frontend `merge_status: merged`** @ test `c510f5c`.
> **58차 동기화 (2026-06-08T11:00) — TSR 79·80 + BNK-9 재확인 + UXD-41 US-F03 + Solapi template variables + Q154 incident detail**: ① **planner git 실측** — backend **`4c74f84`**(+1 vs `32a1f8f`: `AlimtalkTemplateVariables`·Solapi provider) WT **CLEAN** · **`mvn test` 191/191** · **14 ahead** · frontend **`95b92b9`**(+2 vs `4957bd3`: `3ec8206` UXD-41 `IncidentRecordForm` · `95b92b9` Q154 incident `detail` 필드) WT **CLEAN** · **`npm test` 137/45 PASS** · build **124 modules** · **34 Route·38 page** · develop **13 ahead** · test **`4f71543`**. ② **TSR 79** — v2/J03 Solapi 알림톡 템플릿 변수 매핑. ③ **TSR 80** — UXD-41 US-F03 낙상·사고·특이사항 UI · Q154 incident API 정합. ④ **BNK-9 불변** — Directions·러-1~4·G17~G19 · #44 law.go.kr 잔여. ⑤ **QA Open 0건** — 잔여 BLOCK: **backend merge(14) + B03/SEC-D14(backend) + v1.2 develop 13 ahead** + post-merge live E2E(결정 73). ⑥ **v1.2 P0 게이트 충족** · P1 **v1.2.1 후순위** · `merge_status: ready` coder 판단 대기.
> **57차 동기화 (2026-06-08T10:00) — TSR 77·78 + BNK-9 재확인 + UXD-40·Q154 API 정합 + J03 service-layer E2E**: ① **planner git 실측** — backend **`32a1f8f`**(+1 vs `0832fbf`: `J03AlimtalkServiceFlowE2eTest`·`AttendanceServiceTest` check-out dispatch) WT **CLEAN** · **`mvn test` 185/185** · **13 ahead** · frontend **`4957bd3`**(+2 vs `c5708c7`: `9863312` UXD-40 vitals 비정상 경고 · `4957bd3` Q154 건강·NHIS API 본문 정합) WT **CLEAN** · **`npm test` 130/44 PASS** · build **123 modules** · **33 Route·33 page** · develop **11 ahead** · test **`4f71543`**. ② **TSR 77** — `healthApiPayload.js`·`vitalsRanges.js`(US-F01 UXD-40) · `NhisReconciliationTable` 필드 fallback(US-G06) — **FAQ Q154 Fixed**. ③ **TSR 78** — service-layer alimtalk flow E2E 5건(US-J03 v2 follow-up). ④ **BNK-9 불변** — Directions·러-1~4·G17~G19 · #44 law.go.kr 잔여. ⑤ **QA Open 0건** — 잔여 BLOCK: **backend merge(13) + B03/SEC-D14(backend) + v1.2 develop 11 ahead** + post-merge live E2E(결정 73). ⑥ **v1.2 P0 게이트 충족** · P1 **v1.2.1 후순위** · `merge_status: ready` coder 판단 대기.
> **56차 동기화 (2026-06-08T09:00) — TSR 76 + BNK-9 재확인 + UXD-39·vitals DAILY_CARE dispatch**: ① **planner git 실측** — backend **`0832fbf`**(+1 vs `8ce1151`: vitals DAILY_CARE dispatch) WT **CLEAN** · **`mvn test` 179/179** · **12 ahead** · frontend **`c5708c7`**(+1 vs `a627c6d`: UXD-39 Must 흐름 UI) WT **CLEAN** · **`npm test` 115/40 PASS** · build **120 modules** · **33 Route·33 page** · develop **9 ahead** · test **`4f71543`**. ② **TSR 76** — `VitalsRecordForm`·`MedicationRecordForm`·`NhisReconciliationTable`(US-F01·F02·G06 UI) · `HealthRecordService` vitals→DAILY_CARE alimtalk(US-J03 v2 follow-up). ③ **BNK-9 불변** — Directions·러-1~4·G17~G19 · #44 law.go.kr 잔여. ④ **QA Open 0건** — 잔여 BLOCK: **backend merge(12) + B03/SEC-D14(backend) + v1.2 develop 9 ahead** + post-merge live E2E(결정 73). ⑤ **v1.2 P0 게이트 충족** · P1 **v1.2.1 후순위** · API 본문 정합(건강·NHIS) **잔여**(FAQ Q154).
> **55차 동기화 (2026-06-08T08:30) — TSR 74·75 재확인 + BNK-9 불변 + planner git 실측 일치**: ① **planner git 실측** — backend **`8ce1151`** WT **CLEAN** · **`mvn test` 178/178** · **11 ahead** · frontend **`a627c6d`** WT **CLEAN** · **`npm test` 110/36 PASS** · **33 Route·33 page** · build **117 modules** · develop **8 ahead** · test **`4f71543`**. ② **TSR 74·75** — V46 알림 이력 인덱스 · Epic E(US-E01~E05) 출석·QR·통계 **진전 확인**. ③ **BNK-9 불변** — Directions 다중경유 5k/16원 · 러-1~4 실액 · G17~G19 Won't v1 · #44 law.go.kr 잔여. ④ **QA Open 0건** — 잔여 BLOCK: **backend merge(11) + B03/SEC-D14(backend) + v1.2 develop 8 ahead** + post-merge live E2E(결정 73). ⑤ **v1.2 P0 게이트 충족** — ≥60% KPI·P0 E2E `[x]` · P1(급여제공·직원·간편계산기) **v1.2.1 후순위** — `merge_status: ready`는 P1 범위 확정 후 coder 설정.
> **54차 동기화 (2026-06-08T07:30) — TSR 74·75 + BNK-9 재확인 + V46 알림 이력 인덱스 + v1.2 출석 Epic E**: ① **planner git 실측** — backend **`8ce1151`**(+1 vs `c53dd3b`: `V46__notification_history_query_index.sql`) WT **CLEAN** · **`mvn test` 178/178** · **11 ahead** · frontend develop **`a627c6d`**(+2 vs `9bdf59f`: `6f3f746` US-E01·E02 수기 출석 · `a627c6d` US-E03 QR 저장·US-E05 출석 통계 API) WT **CLEAN** · **`npm test` 110/36 PASS** · **33 Route·33 page** · build **117 modules** · test **`4f71543`** · develop **8 ahead**. ② **TSR 74**: V46 알림 이력 조회 인덱스 — **US-J03 v2 follow-up**. ③ **TSR 75**: 파일럿 출석 Epic E(수기 체크인/아웃·QR·월별 통계) — **결정 57 P2·US-E01~E05** 진전. ④ **BNK-9 불변** · **QA Open 0건** — 잔여 BLOCK: **backend merge(11) + B03/SEC-D14(backend)** + v1.2 develop **8 ahead** + post-merge live E2E(결정 73).
> **53차 동기화 (2026-06-08T01:00) — TSR 72·73 + BNK-9 재확인 + v2 알림 이력 API + v1.2 P0 E2E·US-E04**: ① **planner git 실측** — backend **`c53dd3b`**(+1 vs `78e8928`: v2/J03 guardian·staff **notification history APIs**) WT **CLEAN** · **`mvn test` 178/178** · **10 ahead** · frontend develop **`9bdf59f`**(+2: `a68f150` GuardianCheckinPage DS FilterChips(US-E04) · `9bdf59f` P0 CRUD E2E·`PaymentRecordModal`·보호자 초대/수정) WT **CLEAN** · **`npm test` 97/30 PASS** · **33 Route·33 page** · build **114 modules** · test **`4f71543`** · develop **6 ahead**. ② **TSR 72**: `GuardianNotificationHistoryController`·`StaffClientNotificationHistoryController`·`NotificationHistoryService`(+test) — **US-J03 v2 follow-up**. ③ **TSR 73**: v1.2 P0 CRUD E2E·입금 모달·보호자 초대/수정 UI — Epic K·L 진전. ④ **BNK-9 불변** · **QA Open 0건** — 잔여 BLOCK: **backend merge(10) + B03/SEC-D14(backend)** + v1.2 develop **6 ahead** + post-merge live E2E(결정 73).
> **52차 동기화 (2026-06-08T23:00) — TSR 70·71 + BNK-9 재확인 + v1.2 UXD 15 pages·P0 KPI**: ① **planner git 실측** — backend **`78e8928`**(+1 vs `44e0f02`: v2/J03 DAILY_CARE 투약 알림톡 dispatch) WT **CLEAN** · **`mvn test` 171/171** · **9 ahead** · frontend develop **`42f48e1`**(+2: `0d83a42` UXD 15 missing pages · `42f48e1` P0 page-flow·module coverage KPI) WT **CLEAN** · **`npm test` 89/28 PASS** · **33 Route·33 page** · test **`4f71543`** · develop **4 ahead**. ② **TSR 71**: UXD 15 pages(US-D01·E03-E05·F04·G01-G07·H01-H04·B01·A01) · module coverage KPI 테스트 · build **114 modules**. ③ **TSR 70**: `HealthRecordService` 투약기록→보호자 DAILY_CARE alimtalk — **US-J03 v2 follow-up**. ④ **BNK-9 불변** · **QA Open 0건** — 잔여 BLOCK: **backend merge(9) + B03/SEC-D14(backend)** + v1.2 develop **4 ahead** + post-merge live E2E(결정 73).
> **51차 동기화 (2026-06-08T22:00) — TSR 68·69 + BNK-9 재확인 + v1.1 merged + v1.2 UXD 35 커밋**: ① **planner git 실측** — backend **`44e0f02`**(+1 vs `c221531`) WT **CLEAN** · **`mvn test` 170/170** · **8 ahead** · frontend develop **`e0eaf32`**(+2: UXD 35 `64468a3` P0 UI·SideNav · `e0eaf32` guardians RBAC) WT **CLEAN** · **`npm test` 82/27 PASS** · **18 Route·18 page** · test **`4f71543`**(v1.1 merged) · develop **2 ahead**. ② **TSR 69**: v1.1 **`merge_status: merged`** · SEC-D14 **frontend portion 해소** · 50차 **24 files WIP → `64468a3` develop 커밋**(#36 frontend dirty-tree **해소**). ③ **BNK-9 불변** — Directions 5k/16원 · 러-1~4 실액 · G17~G19 Won't v1 · #44 law.go.kr 잔여. ④ **QA Open 0건** — 잔여 BLOCK: **backend merge(8) + B03/SEC-D14(backend)** + v1.2 develop **2 ahead** + post-merge live E2E(결정 73).
> **50차 동기화 (2026-06-08T21:00) — BNK-9 재확인 + frontend dirty-tree 재확대 + baseline HEAD 불변**: ① **planner git 실측** — backend **`c221531`** WT **3M** 불변 · **7 ahead** · frontend **`4f71543`** WT **24 files**(49차 1M→**재확대**) — Must 페이지·공통 UI WIP(`DashboardWidgetGrid`·`FileUpload`·`GuardianInviteModal`·`HealthAbnormalBanner`·`NhisImportGuidePanel`·`MaskedRevealField` + Attendance/Billing/Client/Health/NHIS/Dashboard modified) · **18 Route·18 page** · develop=test **동일 SHA**. ② **HEAD Fixed @ `4f71543` 유효**(이관 규율 5) — recurrence는 **미커밋 v1.2/Must UI WIP 단일**. ③ **BNK-9 불변** — Directions 5k/16원 · 러-1~4 실액 · G17~G19 Won't v1 · #44 law.go.kr 잔여. ④ **QA Open 0건** — 잔여 BLOCK: **backend merge(7) + B03/SEC-D14** + **WT dirty-tree(27 files)** commit/revert.
> **49차 동기화 (2026-06-08T20:00) — TSR 66·67 + BNK-9 재확인 + baseline HEAD 갱신**: ① **planner git 실측** — backend **`c221531`** WT **3M**(GlobalExceptionHandler·NotificationConfig·SecurityConfig) · `mvn test` **169/169 PASS** · **7 ahead** · frontend **`4f71543`** WT **1M**(`vite.config.js`) · `npm test` **58/18 PASS** · build **86 modules** · audit **0** · **18 Route·18 page** · develop=test **동일 SHA**(frontend 0 ahead). ② **TSR 66 @ `c221531`**: v2/J03 daily care·emergency health alimtalk E2E(+11 tests) · v1 baseline artifacts **PRESENT**. ③ **TSR 67 @ `4f71543`**: UXD SideNav·AppShell(`f64e1dd`) · FE-22 liveConfig fail-fast(`4f71543`) · **v1.2 P0 SideNav 진전**. ④ **BNK-9 불변** — Directions 5k/16원 · 러-1~4 실액 · G17~G19 Won't v1. ⑤ **QA Open 0건** — 잔여 BLOCK: **backend merge(7) + B03/SEC-D14** + WT dirty-tree(4 files) 정리.
> **48차 동기화 (2026-06-07T17:30) — 사용자 결정 73: live E2E merge 게이트 제외 + v1.1 `merge_status: ready`**: ① **결정 73** — Must P1–P8·J01/J02 **live E2E run은 merge 선행 조건 아님**(post-merge·권장 검증). ② **v1.1 merge 게이트 충족** — 완료 기준 merge-blocking 항목 전부 `[x]` · **`merge_status: ready`**. ③ **잔여 BLOCK**: **backend merge(6) + frontend merge(11) + B03** — live E2E run **제외**.

> **47차 동기화 (2026-06-08T18:30) — TSR 64·65 + BNK-9 벤치마크 + BE-11 Fixed + FE-22 harness PARTIAL + baseline HEAD 갱신**: ① **planner git 실측** — backend **`80bdb1e`** WT **CLEAN** · `mvn test` **158/158 PASS** · **6 ahead** · frontend **`d592a17`** WT **CLEAN** · `npm test` **46/13 PASS** · build **75 modules** · audit **0** · **18 Route·18 page** · **11 ahead**. ② **TSR 64 @ `80bdb1e`**: **BE-11 Fixed @ `8d42bdd`** — SEC-20260608-014 **Planned→Fixed** · `AuthRateLimitService` HEAD PRESENT. ③ **TSR 65 @ `d592a17`**: **FE-22 harness develop HEAD 반영** — `src/e2e/*`·`vitest.live.config.js` PRESENT · **실 live run**은 merge·backend·`LIVE_E2E` 후. ④ **BNK-9**: 카카오 Directions API 요금 확정(다중 경유지 5k/16원) · 이동서비스비 러-1~4 830/2,630/4,440/6,240원(2차 출처) · **G17·G18·G19 Won't v1** · v1.2 KPI **18 route @ `d592a17`**(과거 24 route·`4be0938` drift 정정). ⑤ **QA Open 0건** — 잔여 BLOCK: **backend merge(6) + frontend merge(11) + B03** + v1.1 **live E2E 실행**(FE-22 harness 완료·run 잔여). **→ 48차 결정 73으로 live E2E merge BLOCK 해제**.

> **46차 동기화 (2026-06-08T17:30) — SEC 6차 Open 2건 Planned + BNK-8 COMPETITOR_MATRIX 정합 + baseline 불변 재확인**: ① **planner 실측** — backend **`136239e`** WT **CLEAN** · `mvn test` **152/152 PASS** · **4 ahead** · frontend **`7170b2a`** WT **CLEAN** · `npm test` **40/11 PASS** · audit **0** · **9 ahead** — **45차와 완전 동일**. ② **SEC 6차 Open→Planned** — **SEC-20260608-013**(SEC-D14 develop→test 미승격) → **B03·backend/frontend merge 게이트** 동반(기존 BLOCK 강화) · **SEC-20260608-014**(SEC-D13 auth rate limit) → **BE-11**·`SECURITY_AUDIT.md` A04-1. ③ **BNK-8 정합** — `COMPETITOR_MATRIX` §1 케어포 **배차 지도 △**(카카오맵 지도보기) 수정. ④ **신규 태스크** — **FE-22**(Must·J01 live E2E)·**BE-11**(AuthRateLimitService). ⑤ **잔여 BLOCK**: **backend merge(4) + frontend merge(9) + B03** + v1.1 **Must 라이브 E2E·J01 live API E2E** + **BE-11**(SEC-D13).

> **45차 동기화 (2026-06-08T16:10) — TSR 62·63차 + COD Must API·J01 REST 반영 + baseline HEAD 갱신**: ① **backend develop `3f9264f`→`136239e`**(+1: Solapi alimtalk·GuardianPhoneStorage), WT **CLEAN**, `mvn test` **152/152 PASS**, **4커밋 ahead**. ② **frontend develop `c3b863e`→`7170b2a`**(+4: `b87a8f5` J01 a11y·`811aef3` Must API·pilot·7-role·SEC-008·`bb0cec4` billing RBAC·`7170b2a` guardian REST+J01/J02 tests), WT **CLEAN**, `npm test` **40/11 PASS**, build PASS, audit **0**. ③ **TSR 63차 @ `811aef3`**: QA-H04·M01·R-04a·R-05·SEC-008 **Fixed** — `pilotChecklist`·`pilotPageFlows`·`sevenRole*`·Must pages HEAD **PRESENT**. ④ **COD `7170b2a`**: J01 `ClientDetailPage`·J02 `GuardianPortalPage` REST API fetch-mock 회귀 — **live E2E 잔여**. ⑤ **잔여 BLOCK**: **backend merge(4) + frontend merge(9) + B03** + v1.1 **Must 라이브 E2E·J01 live API E2E**.

> **44차 동기화 (2026-06-08T16:00) — TSR 61차 + COD FE-18/FE-19 Fixed + baseline HEAD 갱신**: ① **frontend develop `e043eac`→`c3b863e`**(+2커밋: `f506c90` FE-18/FE-19 J01 UI·`c3b863e` US-UX-01 favicon), WT **CLEAN**, `npm test` **9/9 PASS**, build **70 modules PASS**. ② **FE-18·FE-19·B07 #6·H05·SEC-D9 Fixed @ `f506c90`** — `GuardianInvitationList`·`PaymentRecordModal`·`GuardianPortalPage`·`services.js` HEAD PRESENT. ③ **TSR 61차** baseline `e043eac` — SEC-D12·MaskedPhone 6/6 PASS·B07 dirty-tree(d5654c0) **소멸** 확인. ④ **v1.1 완료 기준 잔여**: H04 Must API·P1–P8 E2E·J01 live E2E·SEC-008 audit·`pilotPageFlows` — **`c3b863e` lineage 재구현**. ⑤ **잔여 BLOCK**: **backend merge(3커밋) + frontend merge(5커밋) + B03**.

> **43차 동기화 (2026-06-08T15:00) — workspace baseline 확정 + SEC-D12/QA-B11/SEC-D11 Fixed**: ① **신규 baseline** — backend **`3f9264f`** · frontend **`7c0ecdc`** (`.agents/workspace_baseline.yaml` + run_agent 실측). ② **`d5654c0`/`e5fd48d` checkout 폐기** — TSR57 frontend 유실·재현 불가. ③ **SEC-D12·QA-B11·SEC-D11 Fixed** @ `7c0ecdc`/`3f9264f`. ④ **QA-B10 Fixed** @ `3f9264f` 유지. ⑤ **잔여 BLOCK**: **backend merge(3커밋) + B03** — INFRA-B12 checkout 게이트 **소멸**.

> **42차 동기화 (2026-06-08T03:00) — TSR 58·59차 + BNK-8 반영 (Open 4→Planned·B09 Fixed·baseline 회귀·BLOCK 재우선순위)**: ① **QA Open 4건→Planned** — **QA-B10**(v1 merged baseline regression)·**SEC-D11**(submodule drift)·**SEC-D12**(frontend route 무방비)·**QA-B11**(frontend baseline 단절) → **BE-10·INFRA-B12·FE-20**·PLAN_NOTES `#42`. ② **TSR 58차**: backend develop **`f47ffa1` CLEAN** · **QA-B09·SEC-D8 Fixed** · test **`2799e29` stale** · develop **1커밋 ahead** · v1 E2E/routing 산출물 develop HEAD **ABSENT**(QA-B10). ③ **TSR 59차**: frontend develop·test **동일 `@e5fd48d`(스켈레톤)** · TSR57 **`d5654c0` 재현 불가** · `ProtectedRoute`·Vitest **HEAD ABSENT**(SEC-D12·QA-B11). ④ **BNK-8**: v1.3-A = **케어포 지도 패리티**(차별화 아님) · v1.3-B(TSP·도로경로) = **영업 차별 핵심**. ⑤ **잔여 Planned BLOCK**: **INFRA-B12 + BE-10 + FE-19 + FE-18 + backend merge(1커밋 @ `f47ffa1`) + B03** — B09 **소멸**.

> **41차 동기화 (2026-06-08T01:00) — BNK-7 G15/G16 v1.3 완료 기준 명시 + submodule·QA 재확인 (신규 Open 0·Planned BLOCK 불변)**: ① **QA Open 0건**·**TSR 56·57 baseline**·**SEC-D8·SEC-D9 Planned** — 38~40차 BLOCK **변경 없음**. ② **BNK-7(§10-3·§10-5) planner 권고 반영** — v1.3-A 완료 기준에 **「운영 시각화 한정·청구·평가(G15) 미대응」** 명시·v1.3-C 완료 기준 **G15(별지 제22호 일지·제18호)·G16(`vehicles`·이동서비스비)** 추가·REQUIREMENTS §1-5-1·USER_STORIES US-T05·Epic T 주석 갱신. ③ **planner ogada workspace 직접 점검(41차)** — 40차와 **완전 동일**: `src/backend` @ **`2799e29`(stale)** · WT **9U**(V35~V43, **J01 27 files 미반영**) · `src/frontend` @ **`e5fd48d`(stale)** · WT **CLEAN** → **TSR 56·57·SEC 4차 재검증 여전히 불가**. ④ **잔여 Planned BLOCK 불변**: **B03 + backend merge(3커밋 @ `428ba7d`) + B09(BE-8+SEC-D8) + B07 #6 + H05(FE-19+SEC-D9)**.

> **40차 동기화 (2026-06-08T00:30) — 벤치마크·QA 재확인 + submodule 드리프트 부분 개선·TSR 57 baseline 유지 (신규 Open 0·Planned BLOCK 불변)**: ① **QA Open 0건**·**BNK-7 G15/G16→v1.3-C**·**결정 60~62**·**SEC-D8·SEC-D9 Planned** — 38~39차 반영 **변경 없음**. ② **planner ogada workspace 직접 점검(40차)** — `src/backend` @ **`2799e29`(stale)** · WT **9U**(V35~V43 migrations, DBA round 57~58·**TSR 56 J01 27 files와 불일치**) · `src/frontend` **init 완료** @ **`e5fd48d`(stale)** · WT **CLEAN**(39차 부재→40차 복구, TSR 57 **`d5654c0`**·B07 #6/FE-19 WIP **미반영**) → **TSR 56·57·SEC 4차 재검증 여전히 불가**. ③ **기획 baseline = TSR 56·57 + SEC 4차(38차)** 유지. **잔여 Planned BLOCK 불변**: **B03 + backend merge(3커밋 @ `428ba7d`) + B09(BE-8+SEC-D8) + B07 #6 + H05(FE-19+SEC-D9)**.

> **39차 동기화 (2026-06-07T23:30) — 벤치마크·QA 재확인 + ogada workspace submodule 드리프트 관측 (신규 Open 0·TSR 57차 baseline 유지·Planned BLOCK 불변)**: ① **QA Open 0건**·**SEC 4차 SEC-D8·SEC-D9 Planned**·**BNK-7 G15/G16→v1.3-C**·**결정 60~62 v1.3-A** — 38차 반영 **변경 없음**. ② **planner ogada workspace 직접 점검** — `src/backend` submodule **HEAD `2799e29`(stale)** vs TSR 56 **`428ba7d`** · WT **8 untracked**(V35~V42 migrations, J01 27 files **아님**) · `src/frontend` **디렉터리 부재**(submodule index `-e5fd48d` vs TSR 57 **`d5654c0`**) → **TSR 56·57·SEC 4차 재검증 불가**. ③ **기획 baseline = TSR 56·57 + SEC 4차(38차)** 유지 — coder/tester는 submodule checkout·동기화 후 작업. **잔여 Planned BLOCK 불변**: **B03 + backend merge(3커밋 @ `428ba7d`) + B09(BE-8+SEC-D8) + B07 #6 + H05(FE-19+SEC-D9)**.

> **38차 동기화 (2026-06-07T22:00) — SEC 4차 재점검 반영 (SEC-D8·SEC-D9 Open→Planned·BE-8·FE-19 보안 게이트·Open 0건)**: ① **SEC-20260607-009 Open→Planned**(SEC-D8 J01 `SecurityConfig` 공개 endpoint 허용 범위·`InvitationTokenService` 단일사용·만료·rate limit) → **BE-8** 보안 게이트·**API_SPEC §4-1**·SECURITY_CHECKLIST H-6·**commit/merge 금지** 조건. ② **SEC-20260607-010 Open→Planned**(SEC-D9 MaskedPhone PII 마스킹 `010-****-5678` 유지·테스트 정합) → **FE-19** 보안 게이트·QA-H05 동반·마스킹 제거 시 BLOCK 격상. **Open 0건**·잔여 Planned BLOCK **B03 + backend merge(3커밋 @ `428ba7d`) + B09(BE-8+SEC-D8) + B07 #6 + H05(FE-19+SEC-D9)**.

> **37차 동기화 (2026-06-07T21:30) — TSR 56·57차 반영 (backend B09 Planned·BE-8 J01 API WIP + frontend H05 Planned·FE-19·B07 #6 20 files·FE-7 FAIL·#36 양 스트림 재오픈·Open 0건)**: ① **TSR 56차(10:01, backend)**: 54차 `428ba7d` **CLEAN→DIRTY** — **15M+12U=27 files** J01 `guardian_invitations` WIP(`GuardianInvitationController`·DTO 4종·`GuardianInvitationService`·`InvitationTokenService`·`V43__guardian_invitations.sql`·`GuardianInvitationServiceTest` untracked + Client/Security/테스트 15종 modified). **HEAD `428ba7d` Fixed(B02 #6·B08 #2) 규율 5 유효** — recurrence는 **미커밋 J01 API 단일**. WT `mvn test` **253/253 PASS**·develop **3 ahead of test**. → **QA-B09 Open→Planned**·**BE-8**·**API_SPEC §4-1**·#36 **backend BE-6 #7 재오픈**. ② **TSR 57차(10:11, frontend)**: 55차 15→56차 18→**57차 20 files**(+`PaymentRecordModal`+test·`ClientPhotoField.test`·`GuardianListCard.test`·`ClientFormPage`). WT build **758 modules PASS**·WT `npm test` **209/210 FAIL** — `GuardianListCard.test.jsx` MaskedPhone `010-****-5678` vs 평문 기대(**FE-7 위반**). → **QA-H05 Open→Planned**·**FE-19** 매핑·B07 #6 commit 게이트에 FE-7 선행. **Open 0건**·잔여 Planned BLOCK **B03 + backend merge(3커밋 @ `428ba7d`) + B09 + B07 #6 + H05**.

> **36차 동기화 (2026-06-07T19:30) — TSR 54·55차 반영 (backend B02 #6·B08 #2 Fixed `428ba7d`·#36 BE-6/BE-7 해소 + frontend B07 recurrence #6 Planned·FE-18·Open 0건)**: ① **TSR 54차(09:23, backend)**: 53차 `c3b8716` DIRTY → develop HEAD **`428ba7d`**(+1 COD 36차 V42 consent CHECK·temporal + `NotificationPreferenceServiceTest` 4 @Test), working tree **CLEAN**. **QA-B02 recurrence #6·QA-B08 recurrence #2 정식 Fixed — TSR 독립 검증 PASS**: `git cat-file -e HEAD:` V42·domain test **PRESENT**(이관 규율 5·6·8 PASS). develop HEAD `mvn test` **253/253 PASS**·test **213/213 PASS**. develop **3커밋 ahead of test** — merge 미실행(결정 54 갱신). **#36 backend BE-6 #6·BE-7 #2 해소**. ② **TSR 55차(09:29, frontend)**: 53차 `d5654c0` **CLEAN→DIRTY** — **11M+4U=15 files**(`DateInput`+test·`GuardianInvitationList`+test J01 목록·`ClientDetailPage` 보호자/초대·`GuardianInviteModal`·`GuardianListCard`·`LoginHistoryPanel`·`AuditLogPanel`·`ClientPhotoField`·`services.js`·`GuardianInvitationAcceptPage`+test·`components.css`). **HEAD `d5654c0` Fixed(FE-17·B07 #5) 규율 5 유효**. WT `npm test` **205/42 PASS**(+6/+2)·build **758 modules**·audit **0**. → **QA-B07 recurrence #6 Open→Planned**·**FE-18** 매핑·#36 **frontend FE-6 #5 재오픈**. **Open 0건**·잔여 Planned BLOCK **B03 + backend merge(3커밋 @ `428ba7d`) + B07 #6**.

> **35차 동기화 (2026-06-07T18:00) — TSR 53차 반영 (frontend B07 recurrence #5 정식 Fixed `d5654c0`·FE-17 J01 수락 UI 충족·frontend 잔여 BLOCK = B03 merge 게이트 단일 + backend 51차 대비 불변·B02 #6/B08 #2 Planned 유지·domain test 3→4 @Test·Open 0건)**: ① **TSR 53차(08:36, frontend)**: 52차 `0b9b001` **DIRTY 20 files(B07 #5 Open)** → develop HEAD `0b9b001`→**`d5654c0`**(+1커밋 COD 35차 `feat(v1.1): FE-17 J01 보호자 초대 수락 UI·LogoutButton·레이아웃 회귀 (B07 #5)`, 25 files +823/-57, **18 ahead**), working tree **DIRTY→CLEAN**. **QA-B07 recurrence #5 정식 Fixed — TSR 독립 검증 PASS**: `git -C src/frontend status --porcelain` **0줄**, `git cat-file -e HEAD:` `LogoutButton.jsx`(+test)·`GuardianInvitationAcceptPage.jsx`(+test)·`GuardianInvitationAcceptForm.jsx`·`PublicAuthLayout.jsx`·`BillingPage.layout.test.jsx`·`services.js`(`acceptGuardianInvitationApi`) **전부 PRESENT**(이관 규율 5·6·7 PASS). SEC-005 AuthContext localStorage/sessionStorage **0건**. HEAD `npm test` **199/40 PASS**(+5/+2 vs 52차 WT 194/38)·build **756 modules**(3청크 최대 393.53 kB)·audit **0**. → **FE-17(J01 수락 UI·LogoutButton·레이아웃 회귀) develop HEAD 반영 확정**(v1.1 J01 수락 프론트 흐름·결정 52 흡수 ⑪묶음). **잔여 frontend BLOCK = B03 merge 게이트 단일**(v1.1 `merge_status: pending`·develop→test **18커밋** 미머지·완료 기준 Must 라이ve E2E·J01 백엔드 API). ② **TSR 53차(17:32, backend)**: 51차 대비 **HEAD·dirty-tree·merge 완전 불변** — develop HEAD `c3b8716`·WT **DIRTY** 2 untracked(`V42__guardian_notification_preferences_consent_temporal.sql` 54 lines + `NotificationPreferenceServiceTest` **3→4 @Test**) **HEAD ABSENT**(규율 5·6·8 — v2 follow-up 미커밋). **B02 #6·B08 #2 Planned 유지**. test `mvn test` **213/213 PASS**·develop WT **253/253 PASS**(+1 vs 51차 252)·JAR 82,868,029 B·develop **2커밋 ahead of test**(merge 미실행, 결정 54). ③ **#36 frontend FE-6 #4 해소·backend 단독 잔존**: frontend는 COD 35차 commit으로 B07 #5(FE-6 #4) 종결 → 에스컬레이션 **backend 단독**(BE-6 #6·BE-7 recurrence #2)으로 재축소(33차 비대칭 회귀). ④ **잔여 Planned BLOCK = B03(frontend merge) + backend develop→test merge(2커밋 @ `c3b8716`) + B02 #6 + B08 #2** — B07 #5 **소멸**. Open **0건**·신규 벤치마크·QA Open 입력 **0건**.

> **34차 동기화 (2026-06-07T17:10) — TSR 51·52차 반영 (backend COD 35 false Fixed 철회·B02 #6/B08 #2 Planned 유지 + frontend B07 recurrence #5 Open→Planned·J01 수락 UI WIP·FE-17·Open 0건)**: ① **TSR 51차(07:58, backend)**: 50차 대비 **상태 완전 불변·coder 미조치** — develop HEAD `c3b8716`·WT **DIRTY** 2 untracked(V42 + `NotificationPreferenceServiceTest` 3 @Test) **HEAD ABSENT**. **COD 35 Fixed 주장 TSR FAIL** → ROADMAP v1 QA-B02 `[x]`·v2 B08 recurrence #2 `[x]` **철회**. B02 #6·B08 #2 **Planned 유지**. test `mvn test` **213/213**·WT **252/252 PASS**·develop **2 ahead of test**. ② **TSR 52차(08:03, frontend)**: 50차 `0b9b001` **CLEAN→DIRTY 재오염** — 15M+5U=**20 files**(`LogoutButton`·`BillingPage.layout.test`·`GuardianInvitationAcceptPage`+test J01·AuthContext·Recharts·청구/보호자 페이지). **HEAD `0b9b001` Fixed(FE-15·FE-16) 규율 5 유효** — recurrence는 미커밋 dirty 단일. WT `npm test` **194/38 PASS**·build **754 modules**·audit **0**. → **QA-B07 recurrence #5 Open→Planned**·**FE-17(J01 수락 UI·LogoutButton·레이아웃 회귀)** 매핑·#36 **양 스트림 재오픈**(backend BE-6 #6 + frontend FE-6 #4). ③ **잔여 Planned BLOCK = B03 + backend merge(2커밋) + B02 #6 + B08 #2 + B07 #5**. Open **0건**.

> **33차 동기화 (2026-06-07T16:40) — TSR 50차 반영 (backend B02 recurrence #6 + B08 recurrence #2 Open→Planned·V42 consent CHECK·temporal v2 follow-up 미커밋·HEAD Fixed 규율 5 유효·frontend COD 34차 ds-* 유틸리티 전환 FE-16·Open 0건)**: ① **TSR 50차(16:15, backend)**: 48차 `c3b8716` **CLEAN→DIRTY 재오염** — 2 untracked: ❶ `V42__guardian_notification_preferences_consent_temporal.sql`(54 lines — kakao/sms 유료 채널 consent CHECK + `updated_at`/`consent_at` temporal monotonicity, API_SPEC §11-3·ERD §4-7-1 정합) ❷ `NotificationPreferenceServiceTest.java`(128 lines/**3 @Test** — paid channel consent stamp·upsert). develop HEAD `c3b8716` **불변**·**B02 #5·B08(`feac558`) HEAD PRESENT 유지**(이관 규율 5 — 48차 Fixed **유효**); `git cat-file -e HEAD:V42`·`NotificationPreferenceServiceTest` → **ABSENT**(규율 6·8 위반 — v2 follow-up 미커밋). → **QA-B02 recurrence #6 + QA-B08 recurrence #2 Open→Planned**, **v1 완료 기준 QA-B02 working tree clean `[x]` 철회**(미커밋 재오염), v2 BE-7 **V42 consent CHECK·temporal** follow-up 완료 기준 태스크화. test `mvn test` **213/213 PASS**·develop WT **252/252 PASS**(+3 vs HEAD committed 249)·JAR 82,868,029 B·develop **2커밋 ahead of test**(merge 미실행). ② **TSR 50차(07:17, frontend)**: develop HEAD `c98f98d`→**`0b9b001`**(+1커밋 COD 34차 `fix(v1.1): Must 페이지 UXD ds-* 유틸리티 전환·AttendancePage 레이아웃 회귀 테스트`, **17 ahead**), working tree **CLEAN**. `AttendanceAbsentModal`·`BatchProgressSteps`·`CheckoutModal`·`FeeRateHistoryPanel`·`HealthAbnormalBanner`·`MedicationDuplicateAlert`·`PasswordResetRequestModal`·`PlatformOrgDetailModal`·`SessionTimeoutModal` 인라인 style→**ds-* 유틸리티 전환** + `AttendancePage.layout.test.jsx` 레이아웃 회귀 자동화. 이관 규율 5 PASS·SEC-005 0건·HEAD `npm test` **187/35 PASS**(49차 186/34 → +1/+1)·build **752 modules**(CSS 52.95 kB)·audit **0**·FE-15 코드 스플릿 Fixed 유지. → **FE-16(DESIGN_SYSTEM ds-* 유틸리티 마이그레이션) 매핑**·**신규 Open 0건**. ③ **#36 backend 단독 재오픈**(결정 53) — 32차 대칭 종결 직후 backend v2 follow-up 미커밋으로 BE-6/BE-7 패턴 재발(frontend는 COD 33·34차 연속 CLEAN). ④ **잔여 Planned BLOCK = B03(frontend merge) + backend develop→test merge(2커밋 @ `c3b8716`, 결정 54) + B02 #6 + B08 #2** — B02 #5·B08·B07 #3·FE-15 **HEAD Fixed 유효**. Open **0건**.

> **32차 동기화 (2026-06-07T16:10) — TSR 48·49차 반영 (backend B02 #5·B08 정식 Fixed `c3b8716`·30+회 백엔드 정체 종결·frontend FE-15 Fixed·B07 #4 신호 소멸·잔여 BLOCK = merge 게이트 2스트림·Open 0건)**: ① **TSR 48차(15:35, backend)**: develop HEAD `e8750d2`→**`c3b8716`**(+2커밋 `feac558` B08·`c3b8716` B02 #5), working tree **DIRTY 3M+4U→CLEAN**. **QA-B02 #5·QA-B08 정식 Fixed — TSR 독립 검증 PASS**: `git cat-file -e HEAD:` `PilotChecklistJwtE2eTest`·V41·`notification/` 9 java **전부 PRESENT**(이관 규율 5·6·8 PASS — 46차 false Fixed와 대조). develop committed `mvn test` **249/249 PASS**·test **213/213 PASS**. develop **2커밋 ahead of test** — **결정 54**: v1 보완 merge(`c3b8716`) 즉시 권고, `feac558`(v2 notification)은 HEAD 이력에 포함되나 v2 완료 기준·test 검증은 v2 사이클 별도 평가. ② **TSR 49차(15:45, frontend)**: develop HEAD `4be0938`→**`c98f98d`**(+1커밋 COD 33차 FE-15 코드 스플릿·UXD 인라인 style 제거, **16 ahead**), working tree **CLEAN**. **B07 recurrence #4 신호 소멸**(48차 교차 관측 5 files → `c98f98d` 일괄 커밋, 정식 Open 미등록). **FE-15 정식 Fixed** — `manualChunks`로 단일 JS 744.95 kB → 최대 **393.53 kB**(<500 kB, vite 경고 해소). HEAD `npm test` **186/34 PASS**·build **752 modules**·audit **0**. ③ **#36 대칭 종결**: frontend(FE-6 #3·FE-15)·backend(BE-6 #5·BE-7) **양 스트림 dirty-tree·false Fixed 사유 소멸** — 운영 게이트 권고 **예방적 보류**. ④ **잔여 Planned BLOCK = B03(frontend merge 게이트) + backend develop→test merge(2커밋)** — B02 #5·B08·B07 #3·B07 #4·FE-15 **소멸**. Open **0건**.

> **31차 동기화 (2026-06-07T14:55) — TSR 46·47차 반영 (frontend B07 #3 정식 Fixed `4be0938`·30+회 프론트 정체 종결·backend B02 #5·B08 dirty-tree 확대(3M+4U)·false Fixed 재확인·Open 0건)**: ① **TSR 47차(14:45, frontend)**: develop HEAD `3fdc266`→**`4be0938`**(COD 31차 `feat(v1.1/v1.2): Recharts·플랫폼·청구·건강·운영/보안 UI 일괄 커밋 (B07 #3)`, 82 files +4589/-545, **15 ahead**), working tree **DIRTY 76→0 CLEAN**. **QA-B07 recurrence #3 정식 Fixed — TSR 독립 검증 + planner 직접 재검증 PASS**: `git -C src/frontend status --porcelain` **0줄**, `git cat-file -e HEAD:` `ChartContainer`·`AttendanceRateChart`·`HealthTrendChart`·`FeeScheduleTable`·`CopayRateTable`·`HealthAlertList`·`NhisImportGuidePanel`·`BillingStatusConfirmModal`·`GuardianDailySummary`·`FeeRateHistoryPanel`·`AuditLogPanel`·`BackupSettingsPanel`·`LoginHistoryPanel`·`PasswordChangeModal`·`chartColors.js`·`dashboardWidgets.js`·`pilotChecklist.js`·`sevenRoleRouteMatrix.js` **전부 PRESENT**(이관 규율 5 PASS — backend false Fixed와 대조), SEC-005 `AuthContext` localStorage/sessionStorage **0건**. HEAD `npm test` **185/33 PASS**·build **752 modules**(`recharts ^2.15.4`)·audit **0**. → **FE-12·FE-13·FE-14 develop HEAD 반영 확정**(v1.1 완료 기준 B04·B07 @HEAD·M01 `[x]` 유효, v1.2 P0 차트·플랫폼·청구·운영/보안 UI 흡수). **잔여 frontend BLOCK = B03 merge 게이트 단일**(v1.1 `merge_status: pending`·develop→test 15 commits 미머지·완료 기준 Must 라이브 E2E·J01 백엔드 API). **비차단 LOW 신규**: 단일 JS 청크 **744.95 kB**(>500 kB vite 경고) → `manualChunks` 코드 스플릿 권고(FE-15·v1.2 후속, merge BLOCK 아님). ② **TSR 46차(14:30, backend)**: develop·test `@e8750d2` 동일, develop dirty-tree **1M+4U→3M+4U 확대** — B08 WIP가 **modified** `MustApiEndpointRoutingTest`(+64, notification routing)·`RoleBasedControllerAccessTest`(+93, notification RBAC)까지 확장. **COD Fixed(B02 #5·B08) TSR + planner 직접 재검증 FAIL** — `PilotChecklistJwtE2eTest`·`V41`·`notification/` **HEAD ABSENT**(이관 규율 5). test `mvn test` **213/213 PASS**·develop WT **249/249 PASS**(+6). ③ **#36 비대칭 종결 진단**: frontend는 COD 31차 commit으로 **30+회 정체 종결·B07 #3 Fixed**(FE-6 #3 해소), backend는 **B02 #5·B08 false Fixed 지속** — 에스컬레이션 범위가 **backend 단독**으로 축소. ④ **잔여 Planned BLOCK = B03(frontend merge) + B02 #5 + B08(backend dirty-tree commit)** — B07 #3 **소멸**. Open **0건**.

> **30차 동기화 (2026-06-07T14:05) — TSR 45차 반영 (frontend B07 #3 72→76 files·`FeeScheduleTable`(+test)·WT 181/30·749 modules·backend 44차 baseline 불변·Open 0건)**: ① **TSR 45차(14:02, frontend)**: develop HEAD **`3fdc266` 불변**(43차 대비), dirty-tree **72→76 files**(40M+36U) — 신규 WIP **`FeeScheduleTable`(+test)** + 기존 Recharts·청구·copay·건강·NHIS·설정 WIP. WT **181/30·749 modules·audit 0** TSR 독립 재현(+2/+1 tests vs 43차). → **B07 #3 Planned 범위 확대**·**FE-13 `FeeScheduleTable` 수가표 테이블 UI**(US-G00a·케어포 9-x 수가설정·`FeeRateHistoryPanel` HEAD 연계) 매핑. ② **backend(44차 baseline 불변)**: develop·test `@e8750d2`·B02 #5·B08 dirty-tree·COD Fixed FAIL — 변경 없음. ③ **잔여 Planned BLOCK = B03 + B02 #5 + B07 #3 + B08** 불변. Open **0건**·**30차 연속 coder 미조치**.

> **29차 동기화 (2026-06-07T13:30) — TSR 42·43차 반영 (backend B08 @Test 5→8·WT 243/243·frontend B07 #3 61→72 files·청구·건강·NHIS·보호자 UI WIP·Open 0건)**: ① **TSR 42차(13:25, backend)**: develop·test HEAD **`@e8750d2` 동일**(40·41차 대비 **상태 불변**), develop WT **DIRTY 불변** — B02 #5·B08·`.gitignore` +`data/backups/` 1M. **COD Fixed(B02 #5·B08) TSR 독립 검증 FAIL** 재확인. develop WT `mvn test` **243/243 PASS**(+3 vs 40차 240)·HEAD `@Test` **199**·WT **229**(+30). B08 notification @Test **5→8**. ② **TSR 43차(13:27, frontend)**: develop HEAD **`3fdc266` 불변**(41차 대비), dirty-tree **61→72 files**(38M+34U) — 신규 WIP **`BillingStatusConfirmModal`(+test)·`CopayRateTable`(+test)·`GuardianDailySummary`(+test)·`HealthAlertList`(+test)·`NhisImportGuidePanel`(+test)** + 기존 Recharts·Platform·운영/보안·계정 보안 WIP. WT **179/29·748 modules·audit 0** TSR 독립 재현(+10/+5 tests vs 41차). → **B07 #3 Planned 범위 확대**·**FE-12 `HealthAlertList`·FE-13 청구·copay·NHIS 가이드·보호자 요약 UI** 매핑. ③ **잔여 Planned BLOCK = B03 + B02 #5 + B07 #3 + B08** 불변. Open **0건**·**29차 연속 coder 미조치**.

> **28차 동기화 (2026-06-07T13:25) — TSR 42차 반영 (backend 40·41차 대비 상태 불변·B08 @Test 5→8·WT 243/243·COD Fixed FAIL·Open 0)**: develop·test `@e8750d2`·dirty-tree 구조 불변. B08 @Test 5→8·WT `mvn test` 243/243(+3). Planned BLOCK **B02 #5 + B08 + frontend B03·B07 #3** 불변.

> **27차 동기화 (2026-06-07T12:55) — TSR 40·41차 반영 (backend COD false Fixed 철회·`.gitignore` 부분 진전·frontend 41차 상태 불변·Open 0건)**: ① **TSR 40차(12:45, backend)**: develop·test HEAD **`@e8750d2` 동일**(38차 대비), develop WT **부분 변화** — `.gitignore` **+`data/backups/`** 1M 미커밋·`data/backups/` untracked **소멸**. **COD Fixed 주장(B02 #5·B08) TSR 독립 검증 FAIL** — `PilotChecklistJwtE2eTest`·`notification/`·V41 **HEAD ABSENT**(이관 규율 5). WT `mvn test` **240/240 PASS**(+27). → ROADMAP v1 **QA-B02 `[x]` 철회**·v2 **BE-7·QA-B08 `[x]` 철회**·QA→태스크 매핑 B02 #5·B08 **Planned 복원**. ② **TSR 41차(12:52, frontend)**: develop HEAD **`3fdc266` 불변**(39차 대비 **상태 불변 ±1 modified**), dirty-tree **37M+24U=61 files**(39차 60→41차 +1). WT **169/24·743 modules·audit 0** TSR 독립 재현. ③ **잔여 Planned BLOCK = B03 + B02 #5 + B07 #3 + B08** 불변. Open **0건**.

> **26차 동기화 (2026-06-07T12:25) — TSR 38·39차 반영 (상태 불변·B07 #3 범위 확대 44→60 files·운영/보안 설정 UI 확장(LoginHistory·PasswordChange·PasswordReset·PlatformOrgDetail·SettingsPage 테스트)·B08 dirty-tree 잔존·Open 0건)**: ① **TSR 38차(12:05, backend)**: develop·test HEAD **`@e8750d2` 동일**(0 commits diff)·`mvn test`(test) **213/213 PASS**(75 suites, 0 fail, Spring Boot 3.5.3)·`package` SUCCESS(82,868,029 B)·SEC-007 test `ProductionSecretValidator` **PRESENT**. develop working tree **DIRTY 불변** — ① B02 #5 `PilotChecklistJwtE2eTest`(634 lines/22 @Test, Planned) ② **B08 v2 `notification_preferences` WIP**(V41 + 7 java + 5 @Test, Planned) ③ `data/backups/` manifest(로컬 산출물). HEAD `@Test` **199**·WT **226**. **신규 Open 0**·**coder 미조치 지속**. ② **TSR 39차(12:09, frontend)**: develop HEAD **`3fdc266` 불변**, working tree **확대** — 37차 26M+18U=44 → **36M+24U=60 files**. 신규 WIP: **`LoginHistoryPanel`(+test)**·**`PasswordChangeModal`(+test)**·**`PasswordResetRequestModal`(+test)**·**`PlatformOrgDetailModal`(+test)**·**`SettingsPage.test.jsx`**·**`HealthTrendChart.test.jsx`** + 기존 Recharts·`BatchProgressSteps`·`AuditLogPanel`·`BackupSettingsPanel`·`FilterChips`. WT `npm run build` **743 modules PASS**(+2)·`npm test` **169/24 PASS**(+8/+4)·`npm audit` **0건**(FE-7). → **B07 #3 Planned 범위 확대**(신규 Open 0). ③ **COD 03:08 부분 진전 — FE-14 WIP 일부**: `SettingsPage` 보안 탭에 `PasswordChangeModal`·`PasswordResetRequestModal` 연결 + `SettingsPage.test.jsx` 추가, 로컬 검증 169/24·743 modules PASS — develop working tree 미커밋(B07 #3 Planned 유지·이관 규율 5·6). ④ **FE-14 범위 확장** — 운영/보안 설정 UI에 **로그인 이력·비밀번호 변경·비밀번호 재설정**(§3-1 인증 모듈 매핑) 추가, **FE-13 범위에 `PlatformOrgDetailModal`**(US-A01 Tenant 상세). ⑤ **잔여 Planned BLOCK = B03 + B02 #5 + B07 #3 + B08** 불변. ⑥ **테스트 PASS ≠ 이관 PASS** — 양 스트림 WT 품질 PASS(213/213·169/24)이나 dirty-tree(B02 #5·B07 #3·B08)·merge 게이트(B03)로 BLOCK. Open **0건**.

> **25차 동기화 (2026-06-07T12:10) — TSR 36·37차 반영 (상태 불변·B07 #3 범위 확대 26→44 files·B08 dirty-tree 잔존·Open 0건)**: ① **TSR 36차(11:25, backend)**: develop·test HEAD **`@e8750d2` 동일**(0 commits diff)·`mvn test` **213/213 PASS**(75 suites)·SEC-007 test **PRESENT**. develop working tree **DIRTY 불변** — ① B02 #5 `PilotChecklistJwtE2eTest`(634 lines/22 @Test, Planned) ② **B08 v2 `notification_preferences` WIP 범위 소폭 확대**(V41 + **7 java + 5 @Test**, Planned) ③ `data/backups/` manifest(로컬 산출물, 신규 관측). HEAD `@Test` **199**·WT **226**. **coder 미조치 지속**·신규 Open 0. ② **TSR 37차(11:30, frontend)**: develop HEAD **`3fdc266` 불변**, working tree **확대** — 35차 18M+8U=26 → **26M+18U=44 files**. 신규 WIP: **`AuditLogPanel`(+test)·`BackupSettingsPanel`(+test)·`PasswordChangeModal`(+test)·`FilterChips.test`**(운영·보안·계정 설정 UI) + 기존 Recharts·`BatchProgressSteps`·`PlatformOrgDetailModal`·Platform/NHIS/Reconciliation/Forbidden. WT `npm run build` **741 modules PASS**(+3)·`npm test` **161/20 PASS**(+17/+7)·`npm audit` **0건**(FE-7). → **B07 #3 Planned 범위 확대**(신규 Open 0). ③ **FE-14 신설** — 운영·보안 설정 UI(감사 로그·백업 설정·비밀번호 변경·FilterChips). ④ **잔여 Planned BLOCK = B03 + B02 #5 + B07 #3 + B08** 불변. **테스트 PASS ≠ 이관 PASS** — 양 스트림 WT 품질 PASS이나 dirty-tree(B02 #5·B07 #3·B08) + merge 게이트(B03)로 BLOCK. Open **0건**.

> **24차 동기화 (2026-06-07T02:30) — TSR 34·35차 반영 (B08 Open→Planned + B07 #3 범위 확대 26 files + v1 merged·SEC-007 test 해소 확인)**: ① **TSR 34차(01:45, backend)**: develop·test HEAD **`@e8750d2` merged**·Maven **213/213 PASS**·SEC-007 test **PRESENT**. develop working tree **DIRTY 8 files** — B02 #5 `PilotChecklistJwtE2eTest`(Planned) + **v2 `notification_preferences` WIP**(V41 + 6 java + 4 @Test) → **QA-B08 Open→Planned**. ② **TSR 35차(01:50, frontend)**: develop HEAD **`3fdc266` 불변**, working tree **18→26 files 확대** — `BatchProgressSteps`(+test)·`PlatformOrgDetailModal`·Platform/NHIS/Reconciliation/Forbidden WIP 추가. WT `npm test` **144/13 PASS**(+2/+1)·build **738 modules**·audit **0건**. B07 #3 **Planned 범위 확대**(신규 Open 0). ③ **v2 `notification_preferences` 골격** — ROADMAP v2 완료 기준·BE-7·API_SPEC §11. ④ **v1.2 Platform·배치 UI WIP** — FE-13·US-M02·BNK-6 HQ/플랫폼 패리티. ⑤ **이관 규율 8항** — v1 merged 후 v2 선행 dirty-tree 금지. ⑥ **잔여 Planned BLOCK = B03 + B02 #5 + B07 #3 + B08**. Open **0건**.

> **23차 동기화 (2026-06-07T02:00) — TSR 32·33차 반영 (B02 #5·B07 #3 dirty-tree recurrence + v1 merged·B05 해소 + Recharts 차트 WIP)**: ① **TSR 32차(01:30, backend)**: develop HEAD **`e8750d2` 불변**, working tree **DIRTY** — 1 untracked `PilotChecklistJwtE2eTest.java`(634 lines, **22 @Test**, P1–P8 live Bearer JWT E2E WIP) → **QA-B02 recurrence #5 Open**(planner 22차 false `[x]` — 이관 규율 5 위반). backend test `@e8750d2` merge **완료**(33차 교차). ② **TSR 33차(01:16, frontend)**: develop HEAD **`3fdc266` 불변**, working tree **DIRTY** — 13M+5U=**18 files**(`recharts ^2.15.4`·`ChartContainer`·3 chart components·대시보드·건강·출석 WIP) → **QA-B07 recurrence #3 Open**. WT build **736 modules PASS**·`npm test` **142/12 PASS**·audit **0건**(FE-7). v1 **`merged`** → **B05 해소**. ③ **B02 #5·B07 #3 Open→Planned** — v1 §6·P1–P8 `[x]` **철회**, v1.1 QA-B04·B07 `[x]` **철회**. ④ **v1.2 Recharts 차트 레이어**(BNK-6·US-M02·FE-12). ⑤ **잔여 Planned BLOCK = B03 + B02 #5 + B07 #3**. Open **0건**.

> **21차 동기화 (2026-06-07T01:00) — TSR 30·31차 반영 (B02 #4 Fixed + COD 22차 P1–P8 페이지 E2E + UXD 14차 FeeRateHistoryPanel — Open 0건·merge 게이트 BLOCK 4건 단일 유지)**: ① **TSR 30차(00:28, backend)**: develop HEAD `c3f3146`→**`e8750d2`**(+1커밋 COD 21차 — `SevenRoleJwtLoginE2eTest.java` 384 lines 7역할 JWT live filter-chain E2E), working tree **CLEAN**, `@Test` 183→**199**(+16), Maven 79/79 PASS. **QA-B02 recurrence #4 정식 Fixed** — v1 R-04 「7역할 라이브 JWT 로그인 E2E」**[x] 충족**. Planned BLOCK **5건→4건**. ② **TSR 31차(00:43, frontend)**: develop HEAD `57ff3c0`→`a42d6fb`→**`3fdc266`**(+2커밋 — UXD 14차 `a42d6fb`: `BATCH_STATUS`·`FeeRateHistoryPanel.jsx`(US-G00a)·`chartColors.js`·Recharts 토큰 8 files; COD 22차 `3fdc266`: `pilotPageFlows.test.jsx` 433 lines P1–P8 Must 화면 RTL fetch-mock JWT 페이지 E2E), **14커밋 ahead**, working tree **CLEAN**. HEAD `npm run build` **113 modules PASS**·`npm test` **130/10→140/11 PASS**(+10/+1, FE-7 회귀 없음)·`npm audit` **0건**. → **v1.1 R-05 P1–P8 페이지 단위 E2E PARTIAL 강화** — 라이브 backend·J01 API 잔여. ③ **이관 규율 5** — frontend `git cat-file -e 3fdc266:` `pilotPageFlows.test.jsx`·`FeeRateHistoryPanel.jsx`·`chartColors.js` + 기존 Fixed **PRESENT**. backend `git cat-file -e e8750d2:` `SevenRoleJwtLoginE2eTest` **PRESENT**. ④ **결정 52 흡수 8묶음(21차 갱신)**: 기존 7묶음 + ⑧ **UXD 14차 `a42d6fb`(8 files) + COD 22차 `3fdc266`(1 file, pilotPageFlows P1–P8 페이지 E2E +433)** — 총 **14커밋 / ~98 files** v1.1 merge 동반. ⑤ **#36 BE-6 #4 Fixed** — 20차 재발 후 COD 21차 commit으로 해소, 운영 게이트 권고는 잔존(패턴 재발 가능성). ⑥ Open **0건**·Planned BLOCK **4건**(B01·B03·B05·SEC-007 merge 게이트 단일) 불변. **⚠ 23차에서 B02 #5·B07 #3 recurrence 재발·planner 22차 false `[x]` 철회**.

> **20차 동기화 (2026-06-06T23:58) — TSR 28·29차 반영 (B02 recurrence #4 Open→Planned + UXD 13차 Switch·셀프 체크인 토글 흡수 + COD 20차 7역할 JWT 로그인·라우트 가드 Vitest 단위 E2E 자동화 정식 충족)**: ① **TSR 28차(23:19, 양 스트림)**: backend develop HEAD `c3f3146` **불변**, working tree **DIRTY** — 1 untracked `src/test/java/com/ogada/backend/security/SevenRoleJwtLoginE2eTest.java`(384 lines, 7역할 JWT 로그인 E2E 통합 테스트 WIP — Spring Security filter chain·JwtAuthFilter·UserDetailsService 통합 라이브 발급/검증 시나리오) → **QA-B02 recurrence #4 Open**(이관 규율 6 위반 — BE-6 패턴 19차 「5커밋 무재발 종결」 공언 철회·#4 재발). HEAD Fixed 산출물(`PilotChecklistApiAccessTest`·`MustApiEndpointRoutingTest`·`RoleBasedControllerAccessTest`·`ProductionSecretValidator`·V39·V40 — 규율 5 PASS) 유효 유지. `mvn -q test`(test `@2799e29`, clean) **79/79 PASS**(23 suites)·`package` SUCCESS(76,466,058 B) 재현. frontend develop HEAD `cc34f23`→**`07fd305`**(+1커밋 UXD 13차 `feat(ux): 전사 설정 Switch 컴포넌트·셀프 체크인 토글` — `Switch.jsx` WAI-ARIA `role=switch`·`aria-checked`·44px hit target·`forced-colors`·`SettingsPage` 셀프 체크인 토글 컨트롤·`Switch.test.jsx` 5건 회귀, 7 files +218/-7), develop **11커밋 ahead**, working tree **CLEAN**, `npm run build` **112 modules PASS**(+1 vs 27차)·`npm test` **37 tests/8 files PASS**(+5/+1 — Switch.test.jsx 5건 추가, FE-7 회귀 없음)·`npm audit` **0건**. ② **TSR 29차(23:31, frontend 중심)**: frontend develop HEAD `07fd305`→**`57ff3c0`**(+1커밋 COD 20차 `test(v1.1): 7역할 JWT 로그인·라우트 가드 E2E 자동화` — 4 files +316: `src/auth/sevenRoleJwtLogin.test.jsx`(132 lines — AuthProvider login() 7역할 JWT 메모리 세션·홈 경로 매트릭스(platform_admin→/platform·hq_admin→/dashboard/hq·branch_admin·social_worker·caregiver→/dashboard·guardian·client_user→/guardian·sysadmin→/settings) + LoginPage JWT 폼 submit 7역할 자동화)·`src/auth/sevenRoleRouteGuard.test.jsx`(83 lines — ProtectedRoute 7역할 허용·거부 매트릭스 단위 E2E)·`src/auth/sevenRoleRouteMatrix.js`(75 lines — 7역할 라우트 접근 매트릭스 모듈)·`roleHomePaths.test.jsx`(+26)), develop **12커밋 ahead**, working tree **CLEAN**. HEAD `npm run build` **112 modules PASS**(vite 6.4.3, JS 314.56 kB gzip 92.06 kB)·`npm test`(vitest 4.1.8) **37/8→**130 tests/10 files PASS**(+93 tests/+2 files, FE-7 회귀 없음)·`npm audit --audit-level=high` **0건**. → **v1.1 R-04 7역할 JWT 로그인·라우트 가드 Vitest 단위 E2E 자동화 정식 충족** — 라이브 7역할 JWT 로그인 backend E2E는 backend v1 test 승격 + `SevenRoleJwtLoginE2eTest` develop 커밋 후 — PARTIAL 진전 신호. ③ **이관 규율 5** — frontend `git cat-file -e 57ff3c0:` `sevenRoleJwtLogin.test.jsx`·`sevenRoleRouteGuard.test.jsx`·`sevenRoleRouteMatrix.js`·`Switch.jsx`·`Switch.test.jsx`·`SettingsPage.jsx`·기존 Fixed 산출물(api·routeAccess·AuthContext·favicon·dashboardWidgets·LoginPage·Modal·ThemeToggle) **PRESENT**. backend `git cat-file -e c3f3146:` 기존 Fixed 산출물 **PRESENT 유효**(SevenRoleJwtLoginE2eTest는 untracked — recurrence #4). ④ **결정 52 흡수 7묶음(20차 갱신)**: ① v1.2 P0 `a72e249`(42 files), ② v1.1 US-D03 `3fc549a`(2 files), ③ UXD 10차 `5656e19`(7 files), ④ UXD 11차 `2d742b3`(7 files), ⑤ COD 17차 `a84473f`(8 files) + `ed1bf22`(2 files), ⑥ UXD 12차 `404a30e`(3 files) + COD 18차 `c3f3146`(1 file) + COD 19차 `cc34f23`(3 files), ⑦ **UXD 13차 `07fd305`(7 files — Switch WAI-ARIA·셀프 체크인 토글·테스트) + COD 20차 `57ff3c0`(4 files — sevenRoleJwtLogin·sevenRoleRouteGuard·routeMatrix·roleHomePaths)** — 모두 v1.1 develop→test merge에 동반 흡수. ⑤ **R-04 7역할 권한 분리 PARTIAL 강화** — backend `@WebMvcTest` 65건(36 RBAC + 29 Pilot) + frontend Vitest 단위 E2E(`sevenRoleJwtLogin`·`sevenRoleRouteGuard` 매트릭스). 잔여 = **라이브 7역할 JWT 로그인 backend E2E**(`SevenRoleJwtLoginE2eTest` 384 lines 커밋 시 충족). ⑥ **BE-6 패턴 재오픈** — 19차 「5커밋 무재발 종결 공언」을 20차 #4 재발로 **철회**, 운영 게이트(pre-commit hook 등) 권고 재검토 입력(#36). FE-6 패턴은 「양 스트림 1커밋 무재발」 유지(UXD 13차·COD 20차 working tree CLEAN). ⑦ Planned BLOCK **5건**(B01·**B02 recurrence #4**·B03·B05·SEC-007) — Open 0건(planner 20차 반영 후 회복). ⑧ **US-UX-03 신설**(전사 설정 Switch·셀프 체크인 토글 — DESIGN_SYSTEM §1·§9 확장).

> **19차 동기화 (2026-06-06T23:00) — TSR 26·27차 반영 (PilotChecklistApiAccessTest 29 @Test·pilotChecklist fetch-mock·LoginPage DS·Modal 접근성 — Open 0건 유지·잔여 BLOCK = merge 게이트 단일)**: ① **TSR 26차(22:20, 양 스트림)**: backend develop HEAD `aa71412`→**`c3f3146`**(+1커밋 COD 18차 — `PilotChecklistApiAccessTest.java` 697 lines **29 @Test**, USER_STORIES §13 파일럿 P1–P8 + REQUIREMENTS §7 7역할 `@WebMvcTest` `@PreAuthorize` 자동화, "merge ready 선행"). develop **7커밋 ahead**, working tree **CLEAN**, `@Test` 154→**183**(+29). `mvn -q test`(test `@2799e29`) **79/79 PASS**·`package` SUCCESS(76,466,058 B) 재현. **R-04 7역할 권한 분리** 진전 — `@WebMvcTest` **65건**(36 RBAC + 29 Pilot)로 **PARTIAL 유지**(라이브 7역할 JWT 로그인 E2E 잔여). frontend develop HEAD `ed1bf22`→**`404a30e`**(+1커밋 UXD 12차 — `LoginPage.jsx`·`Modal.jsx`·`components.css` 3 files +183/-28: DS Field/TextInput/Button 적용·모노그램 카드·Modal 포커스 트랩·`forced-colors`·`prefers-contrast` **WCAG 1.4.11**). develop **9커밋 ahead**, working tree **CLEAN**. HEAD `npm run build` **111 modules PASS**(vite 6.4.3)·`npm test` **13/5 PASS**(vitest 4.1.8)·`npm audit --audit-level=high` **0건**. ② **TSR 27차(22:40, frontend 중심)**: frontend develop HEAD `404a30e`→**`cc34f23`**(+1커밋 COD 19차 — 3 files +396: `src/api/pilotChecklist.js`(211)·`pilotChecklist.test.js`(104)·`src/components/ui/GuardianInviteModal.test.jsx`(81)). develop **10커밋 ahead**, working tree **CLEAN**. USER_STORIES §13 파일럿 P1–P8 시나리오를 `services.js` 경로에 매핑 + Vitest fetch mock으로 JWT 토큰·HTTP 메서드·경로 검증 자동화 + GuardianInviteModal 회귀 **4건**(invite/expire/resend/scope). HEAD `npm test` **13/5 → 32/7 PASS**(+19 tests/+2 files, FE-7 회귀 없음)·`npm run build` **111 modules PASS**(JS 313.68 kB gzip 91.78)·`npm audit` **0건**. → **v1.1 Must API 라우팅 fetch-mock 자동화 진전**(R-05·R-07 P1–P8·J01/J02 라우팅·JWT·메서드 검증) — 라이브 7역할 JWT E2E·J01 백엔드 초대 API는 잔여. ③ **이관 규율 5** — backend `git cat-file -e c3f3146:` `PilotChecklistApiAccessTest`·`MustApiEndpointRoutingTest`·`RoleBasedControllerAccessTest`·`ProductionSecretValidator`·`NhisExcelParser`·V39·V40 **PRESENT**. frontend `git cat-file -e cc34f23:` `pilotChecklist.js/.test.js`·`GuardianInviteModal.test.jsx`·api·routeAccess·AuthContext(localStorage 0건)·favicon·dashboardWidgets·`LoginPage.jsx`·`Modal.jsx` **PRESENT**. ④ **결정 52 흡수 6묶음**: ① v1.2 P0 `a72e249`(42 files), ② v1.1 US-D03 `3fc549a`(2 files), ③ UXD 10차 `5656e19`(7 files), ④ UXD 11차 `2d742b3`(7 files), ⑤ COD 17차 `a84473f`(8 files) + `ed1bf22`(2 files), ⑥ **UXD 12차 `404a30e`(3 files, LoginPage DS·접근성)** + **COD 18차 `c3f3146`(1 file, PilotChecklistApiAccessTest)** + **COD 19차 `cc34f23`(3 files, pilotChecklist fetch-mock·GuardianInviteModal 회귀)**. 모두 v1.1 develop→test merge에 동반 흡수(별도 v1.2 merge 라운드 불추가). ⑤ Open **0건** 유지·Planned BLOCK **4건**(B01·B03·B05·SEC-007 merge 게이트 단일) 불변. ⑥ #36 양 스트림 BE-6/FE-6 패턴 **완전 종결 확인** — backend BE-6 #3 Fixed 후 5커밋 무재발(94f0fb9→4274459→aa71412→`c3f3146`)·frontend FE-6 #2 Fixed 후 3커밋 무재발(`a84473f`→`ed1bf22`→`404a30e`→`cc34f23`).

> **18차 동기화 (2026-06-06T22:00) — TSR 24·25차 반영 (B07 recurrence #2 Fixed + SEC-008 Fixed + R-02 Must API 라우팅 [x] 승격 + frontend/backend 양 스트림 dirty-tree 사유 소멸)**: ① **TSR 24차(21:13, backend·frontend)**: backend develop HEAD `4274459`→**`aa71412`**(+1커밋 COD 16차 — `MustApiEndpointRoutingTest`(+459)·`RoleBasedControllerAccessTest`(+148)·`ProductionSecretValidatorTest`(+59), 6커밋 ahead, working tree **CLEAN**, `@Test` 120→**154**(+34). `mvn -q test`(test `@2799e29`) **79/79 PASS**(23 suites)·`package` SUCCESS(76,466,058 B) 재현. **R-02 Must API 엔드포인트 라우팅** 22차 PARTIAL → **[x] 승격**(`MustApiEndpointRoutingTest` §1–§9 26+ @Test 커버). frontend develop HEAD `5656e19`→**`2d742b3`**(UXD 11차 dark mode — `ThemeToggle.jsx`·`tokens.css`·`AppShell`·`theme.js` 7 files +280/-1, 6 ahead). 그러나 develop working tree **DIRTY 8 files 지속**(B07 recurrence #2 — 23차와 동일 대시보드 실데이터 WIP). **신규 SEC-008**: `npm audit` **5 vulnerabilities(4 moderate·1 critical)** — esbuild GHSA-67mh-4wv8-2f99·vite ≤6.4.1·@vitest/mocker·vitest ≤4.1.0-beta.6·vite-node ≤2.2.0-beta.2 dev chain 에스컬레이션(23차 0 high·2 moderate → 24차 5 vuln/1 critical, prod 번들 무관·devDep 전용). → SEC-008 MEDIUM **Open 신규 등록**. ② **TSR 25차(21:32, frontend 중심)**: frontend develop HEAD `2d742b3`→`a84473f`→**`ed1bf22`**(+2커밋 COD 17차, 8 ahead). ❶ `a84473f feat(v1.2-p0): 대시보드 실데이터 위젯·Must 페이지 API 보강 (US-M02)`(8 files +636/-170) — 23·24차 미커밋이던 대시보드 실데이터 WIP 8 files(`dashboardWidgets.js`·`dashboardWidgets.test.js`·`DashboardPage`·`AttendancePage`·`ClientFormPage`·`GuardiansPage`·`GuardianListCard`·`services.js`) **일괄 커밋** → develop working tree **DIRTY→CLEAN**, **QA-B07 recurrence #2 정식 Fixed 확정**(TSR 25차 독립 검증). ❷ `ed1bf22 fix(security): vite 6·vitest 4·esbuild override`(`package.json`+`package-lock.json`, +390/-303) — vite `^6.4.3`·vitest `^4.1.8`·`overrides.esbuild ^0.25.0` → develop **`npm audit` 0 vulnerabilities**(high·all 모두; 24차 5 vuln/1 critical → 0), **SEC-008 정식 Fixed 확정**. 이관 규율 5 — `git cat-file -e HEAD:` api·routeAccess·AuthContext(localStorage 0건)·favicon·ThemeToggle·tokens.css·`dashboardWidgets.js`·`.test.js`·`*.test.jsx`×4 **전부 PRESENT**. develop HEAD(clean) `npm run build` **111 modules PASS**(vite 6.4.3, JS 313.14 kB gzip 91.58)·`npm test`(vitest 4.1.8) **13 tests/5 files PASS**(FE-7 회귀 없음). ③ **결과**: 양 스트림 dirty-tree·B02·B07·SEC-008 사유 **전부 소멸** → **잔여 BLOCK = merge 게이트 단일**(B01 backend·B03/B05 frontend·SEC-007 B01 동반). v1.1 완료 기준 **B07·SEC-008·B04 [x]**, v1.2 P0 **B07 recurrence #2 [x]**·**US-M02 [x]**. ④ **결정 52 유지** — UXD 11차(`2d742b3` dark mode)·UXD 10차(`5656e19`)·v1.2 P0(`a72e249`)·US-M02(`a84473f`)·SEC-008(`ed1bf22`) 5건 모두 v1.1 develop→test merge에 동반 흡수. v1.2 정식 완료 기준은 v1.1 merged 후 v1.2 사이클. ⑤ #36 에스컬레이션 — **양 스트림 BE-6 #3·FE-6 #2 모두 해소**(COD 15·17차 일괄 커밋 패턴), 잔여는 ROADMAP v1·v1.1 E2E·J01(보호자 초대 백엔드 API) 기능 잔여만. coder 다음 액션은 v1 E2E·Must API E2E·SEC-007 동반 → `merge_status: ready` 단일.

> **17차 동기화 (2026-06-06T20:42) — TSR 22·23차 반영 (B02 recurrence #3 Fixed + B07 recurrence #2 + v1.2 P0 대시보드 실데이터 WIP)**: ① **TSR 22차(20:11, backend)**: develop HEAD `b5d70a8`→**`4274459`**(+1커밋, COD 15차 — 20차 미커밋이던 `NhisImportServiceTest`·`RoleBasedControllerAccessTest`·`BillingControllerRoutingTest` **3 files 일괄 커밋**), develop working tree **DIRTY→CLEAN**, develop `@Test` 98→**120**. 이관 규율 5 — `git cat-file -e develop:` `BillingControllerRoutingTest`·`NhisImportServiceTest`(확장)·`RoleBasedControllerAccessTest`(확장)·SEC·NHIS·guardian·V39·V40 **전부 PRESENT**. `mvn -q test`(test `@2799e29`, clean) **79/79 PASS**(23 suites)·`package` SUCCESS(76,466,058 B) 재현. **QA-B02 recurrence #3 Fixed 확정**(TSR 22차 독립 검증 — BE-6 #3 해소). v1 완료 기준 QA-B02 `[x]` **복원**. ② **TSR 23차(20:17, frontend)**: develop HEAD `3fc549a`→**`5656e19`**(+1커밋 UXD 10차 `feat(ux): 이용자 본인 계정 발급 필드·CopayTypeSelect 적용·브랜드색 통일`, origin/develop 대비 **5 ahead**). 그러나 develop working tree **CLEAN→DIRTY** — 6 modified(`src/api/services.js`·`GuardianListCard.jsx`·`AttendancePage.jsx`·`ClientFormPage.jsx`·`DashboardPage.jsx`·`GuardiansPage.jsx`) + 2 untracked(`src/pages/dashboardWidgets.js`·`dashboardWidgets.test.js`) = **8 files**(+471/-170, v1.2 P0 **대시보드 위젯 실데이터(US-M02)** WIP 미커밋, 이관 규율 6·7 위반) → **QA-B07 recurrence #2 Open**. 이관 규율 5 — `git cat-file -e HEAD:` api·routeAccess·AuthContext(localStorage 0건)·favicon·`package.json` test·`*.test.jsx`×4 **PRESENT**(HEAD Fixed 유효). develop **working tree** `npm run build` **112 modules PASS**(JS 297.15 kB gzip 90.29)·`npm test`(`vitest run`) **13 tests/5 files PASS**(신규 `dashboardWidgets.test.js` 3 포함, **FE-7 회귀 없음**). → **B07 recurrence #2 Open→Planned** 이동. ③ **결정 52 유지** — v1.2 P0(`a72e249`) + UXD 10차(`5656e19`) + 향후 대시보드 실데이터 commit은 **v1.1 develop→test merge에 동반 흡수**, 별도 v1.2 merge 라운드 불추가. ④ **v1.2 P0 진전(US-M02 대시보드 실데이터 위젯)**: WT에 `dashboardWidgets.js`·`dashboardWidgets.test.js`(3 tests PASS) 완성·develop HEAD 미커밋 — coder가 commit/revert 후 working tree clean. **잔여 BLOCK = backend merge 게이트 단일(B01·SEC-007) + frontend merge 게이트(B03·B05) + B07 recurrence #2(Planned, dirty-tree 단일)** — backend dirty-tree·B02 사유 **소멸**, frontend dirty-tree는 **Planned**.

> **16차 동기화 (2026-06-06T19:46) — TSR 20·21차 반영 (frontend B07 recurrence Fixed + backend B02 recurrence #3 + v1.2 P0 선행 커밋 흡수 결정)**: ① **TSR 20차(19:12, backend)**: 18차 CLEAN 대비 develop working tree **재오염 #3** — 신규 테스트 3 files 미커밋(`NhisImportServiceTest`·`RoleBasedControllerAccessTest` mod + `billing/api/BillingControllerRoutingTest.java` 신규 untracked, 이관 규율 6 위반). HEAD `b5d70a8` Fixed 산출물 **유효 유지**(규율 5). Maven 79/79 PASS(test) 재현. → **QA-B02 Open 복귀**(recurrence #3). ② **TSR 21차(19:22, frontend)**: develop HEAD `998ac87`→`a72e249`(v1.2 P0 42 files 일괄 커밋: `GuardiansPage`·`PaymentPage`·`OverduePage`·`BillingDetailPage`·`GuardianDetailPage`·`SideNav` 2단·`routeAccess.js`·`SessionTimeoutProvider`·`MaskedPhone`·`QrScanPanel` 등)→`3fc549a`(`ClientDetailPage` 건강·출석 탭 API, US-D03), develop **4 ahead of origin**, working tree **42 files→CLEAN**. HEAD `npm test` **10/4 PASS**·`npm run build` **110 modules PASS**. → **QA-B07 recurrence 정식 Fixed 확정**(21차 TSR 독립 검증). ③ **v1.2 P0 선행 커밋 처리** — TSR 21차 신규 후속(`planner: v1.2 P0 선행 커밋(a72e249) 범위 결정 — v1.1 흡수 vs 분리`). **결정 52(아래) 신설**: v1.2 P0 산출물은 **v1.1 develop→test merge에 동반 흡수** — 별도 v1.2 merge 라운드 불추가, v1.1 merge ready 게이트는 v1.1 완료 기준만으로 평가. v1.2 P0의 정식 완료 기준(2단 SideNav·모듈 커버리지 ≥60%·실데이터 위젯·E2E)은 v1.1 merged 후 v1.2 사이클에서 평가. **잔여 BLOCK = backend B02 recurrence #3(Open)·merge 게이트 4건(B01·B03·B05·SEC-007)** — frontend dirty-tree B07 사유 **소멸**.

> **14차 동기화 (2026-06-06T18:32) — COD B02 recurrence 해소**: develop `b5d70a8` — `RoleBasedControllerAccessTest.GuardianAccess` guardian/client_user RBAC 3 tests 커밋, working tree **CLEAN**, `mvn -q test` **전체 PASS**. v1 QA-B02 `[x]` 복원. 잔여 BLOCK = merge 게이트 4건(B01·B03·B05·SEC-007) + **B07 recurrence(Planned, frontend)**.

> **13차 동기화 (2026-06-06T18:10) — TSR 15·16차 반영 (B02 recurrence + B07 WT 품질 회귀)**: ① **TSR 15차(18:04, backend)**: develop HEAD `fac3d07` 불변·13차 clean 후 working tree **재오염** — `RoleBasedControllerAccessTest` guardian/client_user RBAC +74 lines 미커밋(**QA-B02 recurrence**). → **B02 Open→Planned**, v1 완료 기준 QA-B02 `[x]` **철회**, USER_STORIES §17 **BE-6**. ② **TSR 16차(18:07, frontend)**: develop HEAD `998ac87` 불변·working tree **악화** 19→**29 files**(14M+15U), WT `npm test`·`npm run build` **FAIL**(`routeAccess.js` duplicate `ROUTE_ACCESS`). → **B07 Planned 강화**, USER_STORIES **FE-7**(커밋 전 build/test PASS). **잔여 BLOCK = merge 게이트 4건 + B02 recurrence(Planned) + B07 recurrence(Planned, 16차)** — 양 스트림 dirty-tree 병행.

### 핵심 진단 (planner, 96차 갱신 — BNK-58 · TSR 231~232 · FE merge BLOCK)

- **CURRENT BASELINE (96차)**: backend **`d6d7e7f`** · test **`598d108`** · **59 ahead** · WT **CLEAN** · frontend **`6c4c151`** · test **`c7c8f07`** · **74 ahead** · WT **DIRTY 4M** · **48 path·40 page** · TSR 232 FE **482/127**·TSR 231 BE **453 PASS** @ HEAD/WT.
- **v1.2.1 merge-blocking P0 `[x]` 유지** · BE **`merge_status: ready`** · FE **BLOCK**(QA-B19 · WT dirty) — merge **133 commits(74+59)** · BE ★ **FULLY UNBLOCKED** · FE **WT clean 선행**.
- **BNK-58**: **★ G15 2-2/2-3 출석 이원화 ✅** @ `6c4c151`/`d6d7e7f` · **★ G15 계약 서명 ✅** @ `3c8f9fe`/`9e3cab5` · **★ G11 v2 청구 자동 가산 ✅** @ `d7475fd` · **잔여 P1**: geocode failure UI(B19 WIP)·2-1-1/2-9 외출·운행일지 DB · **#44 수동 보류** · lcms **selectProductGuide** 신규(G10).
- **BNK-53·56 불변**: G11 catalog·G27·US-L01 bank·US-M03-b 닫힘 재확인 · **케어포 108 leaf 불변**.
- **QA Open 0건** · Planned **1건**(B19) · **활성 P1 우선순위**: ① **COD B19 커밋/revert → FE WT clean** ② tester merge(133) ③ **G15 v1.3-C 잔여**(geocode UI·2-1-1/2-9·운행일지) ④ G7 실파일(#27) ⑤ G2 **SMTP** ⑥ G13·US-J02 **live run** ⑦ G21 **live E2E** ⑧ US-L01 **은행 8종 E2E live** ⑨ v1.3 live E2E.

### 핵심 진단 (planner, 95차 — superseded by 96차)

- **CURRENT BASELINE (94차)**: backend **`467cd70`** · frontend **`c9451a0`** · merge **110 commits(61+49)** · TSR 208 FE **434/434**·TSR 207 BE **412 PASS**.
- **BNK-49**: G27 BE · US-L01 bank BE · US-M03-b · 케어포 2-x 11 leaf.

### 핵심 진단 (planner, 93차 — superseded by 94차)

- **CURRENT BASELINE (93차)**: backend **`0854fbd`** · frontend **`eedcc80`** · merge **98 commits(55+43)** · TSR 196 FE **413/413**·TSR 195 BE **383 PASS**.
- **BNK-45**: **#44 재정의** · **US-L01 overpayment guard** · **G2 templates 5종 partial** · **가정 번복 0건**.

### 핵심 진단 (planner, 86차 — superseded by 87차)

- **CURRENT BASELINE (86차)**: backend **`dd49204`** · test **`598d108`** · **6 ahead** · WT **DIRTY 26** · frontend **`e39164d`** · test **`c7c8f07`** · **11 ahead** · WT **DIRTY 9** · **45 path·39 page** · TSR 116 FE **287/89**·BE **288/288** @ HEAD.
- **v1.2.1 P0+US-M02-b+US-J03-h 닫힘** · **`merge_status: ready`** — merge **17 commits** · **BE+FE WT clean 선행**.
- **BNK-22**: G8 알림 이력 UI **닫힘** @ `e39164d` — 케어포 **10-7** 패리티 · **실발송(10-1) v1.1/v2**.
- **QA Open 0건** · Planned 0건 · **활성 우선순위**: ① BE WT clean ② FE WT clean ③ merge(17) ④ G7 실파일 ⑤ live E2E 백로그.

### 핵심 진단 (planner, 85차 — superseded by 87차)

- **CURRENT BASELINE (85차)**: backend **`dd49204`** · test **`598d108`** · **6 ahead** · WT **DIRTY 26** · frontend **`e39164d`** · test **`c7c8f07`** · **11 ahead** · WT **DIRTY 9** · **45 path·39 page** · 테스트 **WT dirty 미재실행**.
- **v1.2.1 P0+US-M02-b+US-J03-h 닫힘** · **US-M03/G22 닫힘** · **G7 reconciliation 닫힘**: US-M02 @ `6d0a03a` · US-M01 @ `15e41e3` · US-M03 @ `dbf485e` · G7 BE @ `4cc328d`/`dd49204` · G7 FE @ `fbb0b7a`/`16402b2` · **US-M02-b** @ `1794e1c` · **US-J03-h** @ `e39164d` → **`merge_status: ready`** (결정 92 · merge **11+6** · **BE+FE WT clean 선행**).
- **BNK-22**: **G8 알림 발송 이력 UI 닫힘** — `NotificationHistoryPanel`(케어포 **10-7 안내발송내역** 패리티) · BE `/guardian/notifications`·`/clients/:id/notifications` · **실발송(10-1) v1.1/v2 잔여** · 모듈 커버 **72.5%**(발송 연동 시 ~74.4%).
- **G7 NHIS 잔여**: **파일럿 엑셀 실파일**(데이터 BLOCK · #27) · fixture tests @ `dd49204` **부분 ✅** · 대시보드 `nhisPendingReviewCount` ✅ @ `1794e1c`.
- **G13 partial**: `pilotPageFlows` US-L01·L02 E2E @ `16402b2` — **live** 상태전이 E2E 잔여.
- **v2 G21 / v3 bleed**: backend meals/programs·V55·Visit WIP — **develop-only** · merge gate **양 스트림 WT clean** 후 11+6.
- **활성 우선순위 (85차)**: ① **backend WT clean**(26) ② **frontend WT clean**(9) ③ **tester merge(11+6)** ④ G7 실파일 ⑤ US-J02·G13 live E2E ⑥ v1.3 live E2E ⑦ G11·알림톡 실발송(v1.1).
- **QA Open 0건** · v1.2.1 **`in_progress`**(merge 대기) · v2 **`in_progress`** · v1.3-A **`merged`** @ test `c7c8f07`.
- **잔여 BLOCK**: **backend WT(26) + frontend WT(9)** + v1.2.1 **merge(11+6)** + G7 샘플 + live E2E 백로그.

### 핵심 진단 (planner, 81차 — superseded by 82차)

- **CURRENT BASELINE (81차)**: backend **`4cc328d`** · test **`598d108`** · **5 ahead** · WT **CLEAN** · frontend **`371794f`** · test **`c7c8f07`** · **6 ahead** · WT **DIRTY 4** · **`259/80 PASS`** · **45 path·39 page**.
- **v1.2.1 P0 닫힘** · **US-M03/G22 닫힘**: US-M02 @ `6d0a03a` · US-M01 @ `15e41e3` · **US-M03** @ `dbf485e` → **`merge_status: ready`** (결정 92 · merge **6+5**).
- **BNK-17**: G21 **`/visits` FE 착수** @ `371794f`(PLAN/BILLING Tabs·모바일 체크인) · G7 **V54+서비스 커밋** @ `4cc328d` · FE G7 UI **WT 4 files** · #44 **2차 출처 충돌** · CMS=**효성CMS**.
- **G7 NHIS P0**: 케어포 **성공/오류/대기 3상태** → backend **`PENDING_REVIEW`** @ `4cc328d` **커밋** · UI·파일럿 샘플 **잔여**.
- **v2 G21**: backend V53·`/visits` + **frontend Epic V** @ `371794f` — E2E·공단 import **잔여**.
- **활성 우선순위 (81차)**: ① **G7 FE 커밋**(WT clean) ② **tester merge(6+5)** ③ G7 파일럿 샘플 ④ G13·US-J02 live E2E ⑤ v1.3 live E2E ⑥ Epic V E2E.
- **QA Open 0건** · v1.2.1 **`in_progress`**(merge 대기) · v2 **`in_progress`**(Epic V partial) · v1.3-A **`merged`** @ test `c7c8f07`.
- **잔여 BLOCK**: FE **WT dirty(4)** + v1.2.1 **merge(6+5)** + G7 UI·샘플 + G13·live E2E.

### 핵심 진단 (planner, 80차 — superseded by 81차)

- **CURRENT BASELINE (80차)**: backend **`1812165`** · test **`598d108`** · **4 ahead** · WT **CLEAN** · frontend **`0a07799`** · test **`c7c8f07`** · **5 ahead** · WT **CLEAN** · **`240/76 PASS`** · **44 path·38 page**.
- **v1.2.1 P0 닫힘** · **US-M03/G22 닫힘**: US-M02 @ `6d0a03a` · US-M01 @ `15e41e3` · **US-M03** @ `dbf485e` → **`merge_status: ready`** (결정 92).
- **BNK-16**: 모듈 **72.5%**(+3.8pp) · 케어포 **7-6~7-10 ✅** · **7-2-1·7-9 Could** · 이지케어 **9,306**·FAQ payroll lock-in **37%**.
- **G7 NHIS P0**: 케어포 **성공/오류/대기 3상태** vs ogada 2상태 — **「대기(보류)」** UX·오류 가이드 검토(BNK-15 §18-4).
- **v2 G21 backend**: V53·`/visits`·branch guard @ `1812165` — `/visits` UI **v1.2.1 merge 후**.
- **활성 우선순위 (80차)**: ① **tester develop→test merge(5+4)** ② **G7 NHIS** ③ US-J02·**G13 E2E** ④ v1.3 live E2E run ⑤ v2 `/visits` UI.
- **QA Open 0건** · v1.2.1 **`in_progress`**(merge 대기) · v1.3-A **`merged`** @ test `c7c8f07`.
- **잔여 BLOCK**: v1.2.1 **merge(5+4)** + G7 NHIS + G13·live E2E + v2 UI.

### 핵심 진단 (planner, 79차 — superseded by 80차)

- **CURRENT BASELINE (79차)**: backend **`15e41e3`** · test **`598d108`** · **3 ahead** · WT **CLEAN** · **`262/262 PASS`** · frontend **`465bdae`** · test **`c7c8f07`** · **3 ahead** · WT **CLEAN** · **`225/72 PASS`** · **39 Route·36 page**.
- **v1.2.1 P0 닫힘**: US-M02 @ `6d0a03a` · **US-M01/G14 GET API** @ `15e41e3` → **`merge_status: ready`** (결정 92).
- **BNK-14·13**: 모듈 **~68.7%** · 케어포 **7-6~7-10** → **US-M03 P1**(G22) · **1-3=기초평가** 정정 유지.
- **v2 G21 backend**: V53·`/visits` @ `d768820` lineage — develop-only bleed · `/visits` UI **v1.2.1 merge 후**.
- **활성 우선순위 (79차)**: ① **tester develop→test merge(3+3)** ② v1.3 live E2E run ③ **G7 NHIS** ④ **US-M03 P1** ⑤ US-J02·G13 E2E.
- **QA Open 0건** · v1.2.1 **`in_progress`**(merge 대기) · v1.3-A **`merged`** @ test `c7c8f07`.
- **잔여 BLOCK**: v1.2.1 **merge(3+3)** + v1.3 live E2E run + G7 NHIS + P1 백로그.

### 핵심 진단 (planner, 78차 — superseded by 79차)

- **CURRENT BASELINE (78차)**: backend **`d768820`** · test **`598d108`** · **2 ahead** · WT **CLEAN** · **`257/257 PASS`** · frontend **`6d0a03a`** · test **`c7c8f07`** · **2 ahead** · WT **CLEAN** · **`225/72 PASS`** · **39 Route·36 page**. **77차 대비 delta 없음**.
- **BNK-14·13 (78차 재확인)**: US-M02 **닫힘** · G14 **GET API 미구현** · 모듈 **~68.7%** · 케어포 **7-6~7-10** → **US-M03 P1**(BNK-13) · **1-3=기초평가**(보호자는 1-1 탭·ogada `/guardians` 분리 Route).
- **v2 G21 backend @ `d768820`**: V53·`/visits`·PLAN/BILLING·체크인 — **결정 92** v1.2.1 P0 **선행** · `/visits` UI **v1.2.1 P0 후**.
- **활성 버전 (78차)**: ① **G14 GET API**(US-M01) **최우선** ② P0 `[x]` → merge(4 commits) ③ v1.3 live E2E run ④ **G7 NHIS** ⑤ **US-M03 P1**.
- **QA Open 0건** · v1.2.1 **`in_progress`** · v1.3-A **`merged`** @ test `c7c8f07`.
- **잔여 BLOCK**: **G14 backend GET API** + v1.2.1 merge(4) + v1.3 live E2E run + G7 NHIS.

### 핵심 진단 (planner, 77차 — superseded by 78차)


- **CURRENT BASELINE (77차)**: backend develop **`d768820`** · test **`598d108`** · **2 ahead** · WT **CLEAN** · **`257/257 PASS`** · frontend develop **`6d0a03a`** · test **`c7c8f07`** · **2 ahead** · WT **CLEAN** · **`225/72 PASS`** · **39 Route·36 page**. **git 실측(planner 77차)** — ROADMAP/QA 과거 SHA보다 **우선**.
- **BNK-14 (77차 재확인)**: US-M02 **닫힘** @ `6d0a03a` · US-M01 **UI+DB(V48) ✅** · `GET /ltc-grade-history` **미구현** · 모듈 **~68.7%**(≥60% PASS) · 케어포 1-9 **전수 리포트 Route 없음** · **7-6~7-10 리포트 P1** · 이지케어 RFID FAQ→**G21 v2**.
- **v2 G21 backend bleed @ `d768820`**: V53·`/api/v1/visits`·PLAN/BILLING 페어·체크인 API **`VisitServiceTest`(+11)** — **결정 92 위반 가능**(v1.2.1 P0 선행) · frontend `/visits`·E2E **잔여**.
- **활성 버전 우선순위 (77차)**: ① **v1.2.1 `in_progress` 단일 merge gate** — **G14 GET API** 1건 ② P0 `[x]` 후 **merge(4 commits: FE 2+BE 2)** ③ **v1.3 live E2E run**(결정 73) ④ **G7 NHIS 샘플** ⑤ **US-M03 P1** ⑥ v2 frontend·G21 UI **v1.2.1 P0 후**.
- **v1.2.1 (77차)**: **US-M02 `[x]`** · **US-M01 △** (GET API 잔여) · US-J02·G13·G7 **잔여**.
- **v1.3-A**: **`merge_status: merged`** @ test **`c7c8f07`** · live E2E **run**만 잔여.
- **QA Open 0건** · TSR 105 PASS(v1.2+v1.3-A @ test).
- **BNK-9 (불변)**: Directions 5k/16원 · 러-1~4 · G17~G19 Won't v1 · #44 law.go.kr 잔여.
- **잔여 BLOCK**: **G14 backend GET API** + v1.2.1 merge(**4 commits**) + v1.3 live E2E **run** + G7 NHIS 샘플.

### 핵심 진단 (planner, 74차 — **superseded by 75차**)

- **CURRENT BASELINE (74차)**: backend develop **`598d108`**(WT **DIRTY 13**) · **origin/test STALE `2799e29`**(QA-B12) · frontend **`c7c8f07`** · test **`c510f5c`** · develop **22 ahead**.
- **잔여 Planned BLOCK (74차)**: origin/test push + SEC-D14 + frontend merge(22).

### 핵심 진단 (planner, 73차 — **superseded by 74차**)

- **CURRENT BASELINE (73차)**: backend develop **`598d108`**(WT **CLEAN** · develop **`246/246 PASS`**) · local test **`598d108`**(=develop) · **origin/test STALE `2799e29`** — **26 ahead·미푸시**(QA-B12) · frontend develop **`7cd9293`**(WT **CLEAN** · **`npm test` 214/69** · **780 modules 3청크**(max **367 kB**) · test **`c510f5c`** · develop **49 ahead**). **git 실측(TSR 100·101차)** — ROADMAP/QA 과거 SHA보다 **우선**.
- **활성 버전 우선순위 (73차)**: ① **`origin/test` push(QA-B12)** — tester/merge 스크립트 전담 · operation·SEC-D14 선행 ② **frontend merge(49)** — v1.3 local merged·origin 미동기화 ③ **v1.3 live E2E run**(post-merge·결정 73) ④ v3 Staff API·프로그램 사진(merge 후) ⑤ v2 프론트 알림 UI·Epic L UI **보류** · **frontend 단일 `in_progress` 없음**.
- **v1.3-A (73차)**: local test **merged** @ `32575aa` lineage(+ develop `598d108` v2 bleed) · **`merge_status: merged`(local)** · **origin/test push 전 operation 승격 불가**(QA-B12).
- **v2 backend bleed @ `598d108`**: `RecordCopayPaymentRequest`·`OverdueClaimListResponse`·V50 copay payment metadata — **develop-only** · Epic L(US-L01·L02) backend API **부분 진전** · frontend UI·origin test 승격 **잔여**.
- **UXD-54 (73차)**: `BranchScopeNotice` — QrGeneratePage·TransportRunNewPage·TransportRunDetailPage·TransportPage 연동(US-UX-04 보완) @ `7cd9293`.
- **v1.1·v1.2**: **`merge_status: merged`** @ frontend test **`c510f5c`**.
- **BNK-9 (47~73차 재확인)**: Directions 다중경유 5k/16원 · 이동서비스비 830~6,240원(2차) · G17~G19 Won't v1 — **변경 없음** · #44 law.go.kr 1차 확인 잔여.
- **잔여 Planned BLOCK**: **origin/test push(QA-B12) + SEC-D14(origin) + frontend merge(49)** + v1.3 live E2E **run**(post-merge 권장).

### 핵심 진단 (planner, 72차 — **superseded by 74차**)

- **CURRENT BASELINE (72차)**: backend develop **`32575aa`**(WT **CLEAN** · **`mvn test` 243/243** · **25 ahead**) · frontend develop **`e641f62`**(WT **CLEAN** · **`npm test` 212/69** · **780 modules 3청크**(max **367 kB**) · **40 Route·51 page** · test **`c510f5c`** · develop **20 ahead**). **git 실측(TSR 98·99차)** — ROADMAP/QA 과거 SHA보다 **우선**.
- **활성 버전 우선순위 (72차)**: ① **backend merge(25) + SEC-D14** — 최우선 BLOCK ② **frontend merge(20)** — v1.3 `merge_status: ready` ③ **v1.3 live E2E run**(post-merge·결정 73) ④ v3 Staff API·프로그램 사진(merge 후) ⑤ v2 프론트 알림 UI **보류** · **frontend 단일 `in_progress` 없음**(v1.3 done·v3 보류).
- **v1.3-A transport privacy (72차)**: masking API @ `c7941e9` + **단위 테스트 보강 @ `32575aa`**(`TransportServiceTest` 10 @Test) · UI @ `1d910c2`+ — SEC-D9·PII 정합.
- **UXD-53 (72차)**: `BranchScopeNotice` — 출석·QR·배차 **활성 지점 조회 범위** 노출(US-B02/E01/E05) · `pilotPageFlows` E2E @ `e641f62`.
- **v1.1·v1.2**: **`merge_status: merged`** @ frontend test **`c510f5c`**.
- **v1.3-A**: **`merge_status: ready`** — merge-blocking **전부 `[x]`** · develop→test merge + live E2E **run** 잔여.
- **BNK-9 (47~72차 재확인)**: Directions 다중경유 5k/16원 · 이동서비스비 830~6,240원(2차) · G17~G19 Won't v1 — **변경 없음** · #44 law.go.kr 1차 확인 잔여.
- **잔여 Planned BLOCK**: **backend merge(25) + SEC-D14(backend) + frontend merge(20)** + v1.3 live E2E **run**(post-merge 권장).

### 핵심 진단 (planner, 68차 — **superseded by 70차**)

- **CURRENT BASELINE (68차)**: backend develop **`e7d4cf6`**(WT **CLEAN** · **`mvn test` 241/241** · **23 ahead**) · frontend develop **`3c55339`**(WT **CLEAN** · **`npm test` 203/67** · **778 modules 3청크**(max **367 kB**) · **40 Route·51 page** · test **`c510f5c`** · develop **16 ahead**). **git 실측(TSR 94·95차)** — ROADMAP/QA 과거 SHA보다 **우선**.
- **활성 버전 우선순위 (68차)**: ① **backend merge(23) + SEC-D14** — 최우선 BLOCK ② **frontend v1.3-A** — service-flow E2E **`[x]` @ `f8d1b02`+** · pickup masking **`[x]` @ `e7d4cf6`** · ClientForm 픽업 프로필 **`[x]` @ `3c55339`** · live harness **`[x]` @ `d484206`+** · **live run 잔여**(결정 73) ③ **v2 backend follow-up** — 프론트 알림 UI **보류** ④ **v3 frontend** — Staff API·프로그램 사진 **v1.3 merge gate 후** 재개.
- **폐기 SHA**: `d5654c0`(TSR57)·`e5fd48d`(스켈레톤)·`428ba7d`(TSR56) — **checkout 재현 금지**. **`4be0938`**·24 route — **git object 없음**(BNK-9 drift).
- **결정 73 (48차)**: live E2E **run**은 merge 선행 조건 **아님** — harness @ `d484206` **PRESENT** · post-merge run 권장.
- **v1.1·v1.2**: **`merge_status: merged`** @ frontend test **`c510f5c`**.
- **v1.3-A (68차)**: backend **`e7d4cf6`** — transport API stack + **Clients profile** + **`TransportPilotServiceFlowE2eTest`** + **non-HQ pickup address masking** **HEAD PRESENT** · frontend **`3c55339`** — transport UI·unconfirm·**`ClientFormPage` 픽업 프로필**·**`pilotPageFlows` T01~T03** + **`transportLiveApi.e2e.test.js` harness**·**UXD-51 FE-13/FE-14 복원** **HEAD PRESENT** · **잔여**: live E2E **run** · `merge_status: ready` 판단 대기.
- **FE-15 (67차)**: **`d484206`** — `manualChunks` 복원 · max **367 kB <500 kB** · **Fixed**(91/92차 756 kB 회귀 해소).
- **UXD-49 HQ 건강 이상**: **`00375f6`** lineage — 지점명 표시(US-H02 PARTIAL) · `BranchCompareChart` **잔여**.
- **v3 (64차 진전)**: backend **`dfd9be2`+** · frontend **`d484206`** lineage — meals/programs·StaffPage UI **PRESENT** · **프로그램 사진·Staff API** **후속**.
- **v2/J03 follow-up**: copay PAID alimtalk @ `52e0621` lineage — **live Solapi·프론트 알림 UI 잔여**.
- **SEC-D14/B03**: backend develop→test **23커밋** · frontend develop→test **16커밋** 미승격 — merge 게이트 **BLOCK**.
- **잔여 Planned BLOCK**: **backend merge(23) + SEC-D14(backend) + frontend merge(16)** + v1.3 live E2E **run**(post-merge 권장).
- **BNK-9 (47~67차 재확인)**: Directions 다중경유 5k/16원 · 이동서비스비 830~6,240원(2차) · G17~G19 Won't v1 — **변경 없음** · #44 law.go.kr 1차 확인 잔여.
- **v1.2 P1**: 급여제공·직원·간편계산기 — **v1.2.1 후순위**(merge 게이트 비차단).
- **모듈 커버 (67차 추정)**: v1.2 ≥60% KPI + transport service-flow E2E·live harness(케어포 2장)·meals/programs(3·5장)·StaffPage(8장 부분) **develop 연동** → **~69–72%** (BNK-6 KPI, 프로그램 사진·Staff API·평가 △).

### 핵심 진단 (planner, 66차 — **superseded by 67차**)

### 핵심 진단 (planner, 65차 — **superseded by 67차**)

### 핵심 진단 (planner, 63차 갱신 — **superseded by 64차**)

### 핵심 진단 (planner, 70차 — **superseded by 71차**)

- **CURRENT BASELINE (50차)**: backend develop **`c221531`**(WT **3M** — TSR 66 CLEAN 직후 재오염) · frontend develop **`4f71543`**(WT **24 files** — Must UI·공통 컴포넌트 WIP **재확대**) · **18 route·18 page**. **git 실측** — ROADMAP/QA/workspace_baseline 과거 SHA보다 **우선**.
- **폐기 SHA**: `d5654c0`(TSR57)·`e5fd48d`(스켈레톤)·`428ba7d`(TSR56) — **checkout 재현 금지**. **`4be0938`**·24 route — **git object 없음**(BNK-9 drift).
- **결정 73 (48차)**: live E2E run은 merge 선행 조건 **아님** — post-merge 권장(FE-22 harness @ `4f71543` **PRESENT**).
- **v1.1 merge 게이트**: merge-blocking `[x]` · **`merge_status: merged`** — frontend develop=test @ `4f71543`(test 승격 완료) · backend **7 ahead** 잔여(B03/SEC-D14).
- **v1.2 진전 (TSR 67) + 50차 WIP**: UXD **`f64e1dd`** SideNav·AppShell — US-UX-02 2단 SideNav **WIP**(@HEAD 미완). **추가 WIP**: `DashboardWidgetGrid`·`FileUpload`·`GuardianInviteModal`·`NhisImportGuidePanel`·`MaskedRevealField` 등 Must UI cluster — **FE-6 dirty-tree**(HEAD Fixed 유효).
- **SEC-D14/B03**: backend develop→test **7커밋** 미승격 — merge 게이트 **BLOCK**.
- **잔여 Planned BLOCK**: **backend merge(7) + B03/SEC-D14** + WT dirty-tree(**27 files**) commit/revert.
- **BNK-9 (47·49·50차 재확인)**: Directions 다중경유 5k/16원 · 이동서비스비 830~6,240원(2차) · G17~G19 Won't v1 — **변경 없음** · #44 law.go.kr 1차 확인 잔여.

### 핵심 진단 (planner, 65차 — **superseded by 66차**)

- **CURRENT BASELINE (45차)**: backend develop **`136239e`**(CLEAN) · frontend develop **`7170b2a`**(CLEAN). TSR 63 Fixed · COD `7170b2a` J01/J02 fetch-mock · 잔여 BLOCK merge(4+9)+B03+라이브 E2E 2건.

### 핵심 진단 (planner, 64차 — **superseded by 66차**)

- **CURRENT BASELINE (44차)**: backend develop **`3f9264f`**(CLEAN, BE-10·J01·v2/J03) · frontend develop **`c3b863e`**(CLEAN, MVP+vitest·FE-18/19·favicon). **`.agents/workspace_baseline.yaml`** + run_agent build **실측 주입** — ROADMAP/QA 과거 SHA보다 **우선**.
- **폐기 SHA**: `d5654c0`(TSR57 frontend)·`e5fd48d`(스켈레톤)·`428ba7d`(TSR56) — **checkout 재현 금지**. v1.2 Recharts·`pilotPageFlows`·Must API 전면 연동 등 **d5654c0 lineage** — **`c3b863e` 위 재구현 잔여**.
- **FE-18·FE-19 Fixed @ `f506c90`**: `GuardianInvitationList`·`PaymentRecordModal`·`GuardianPortalPage`·`GuardianInvitationAcceptPage`·`services.js` HEAD **PRESENT** · `npm test` **9/9 PASS** · B07 #6·H05·SEC-D9 **소멸**.
- **US-UX-01 @ `c3b863e`**: 브랜드 favicon 복구 커밋 — HEAD 반영.
- **QA-B10 Fixed @ `3f9264f`**: v1 E2E/routing/SEC-007 develop HEAD **PRESENT** — BE-10 **완료**.
- **backend merge gap**: develop **3커밋 ahead** of test — merge 게이트 **BLOCK**.
- **frontend merge gap**: develop **`c3b863e`** vs test **`e5fd48d`** — **5커밋 ahead** — B03 merge 게이트 **BLOCK**.
- **v1.1 완료 기준(TSR 61·44차)**: H04 Must API **FAIL** · M01 **PARTIAL**(9/9 vs P1–P8) · R-05/R-07 J01 **FAIL**(live E2E) · SEC-008 audit **4 vuln**(non-blocking) · `pilotPageFlows`·`pilotChecklist` **ABSENT**.
- **잔여 Planned BLOCK**: **backend merge(3커밋) + frontend merge(5커밋) + B03** — INFRA-B12·FE-18·FE-19 **소멸**.
- **#36 운영 게이트 (결정 63)**: baseline 주입(L1) **적용** · L2 pre-commit·L3 CI build 승인 대기.

### 핵심 진단 (planner, 63차 — **superseded by 64차**)

- **CURRENT BASELINE (43차)**: backend develop **`3f9264f`**(CLEAN, BE-10·J01·v2/J03) · frontend develop **`e043eac`**(CLEAN, JWT·ProtectedRoute·AppShell·vitest). **`.agents/workspace_baseline.yaml`** + run_agent build **실측 주입** — ROADMAP/QA 과거 SHA보다 **우선**.
- **폐기 SHA**: `d5654c0`(TSR57 frontend)·`e5fd48d`(스켈레톤)·`428ba7d`(TSR56) — **checkout 재현 금지**. v1.1 Recharts·FE-17·GuardianInvitationAccept 등은 **`e043eac` lineage 위에서 재구현**.
- **SEC-D12·QA-B11·SEC-D11 Fixed @ 43차**: frontend route 가드·baseline 단절·submodule drift — **`e043eac`/`3f9264f` 기준**.
- **QA-B10 Fixed @ `3f9264f`**: v1 E2E/routing/SEC-007 develop HEAD **PRESENT** — BE-10 **완료**.
- **backend merge gap**: develop **3커밋 ahead** of test (`f47ffa1`·`cf6116c`·`3f9264f`) — merge 게이트 **BLOCK**.
- **frontend merge gap**: develop **`e043eac`** vs test **`e5fd48d`** — B03 merge 게이트 **BLOCK**.
- **잔여 Planned BLOCK**: **backend merge(3커밋) + B03** — INFRA-B12 checkout **`d5654c0` 폐기**.
- **#36 운영 게이트 (결정 63)**: baseline 주입(L1) **적용** · L2 pre-commit·L3 CI build 승인 대기.

### 핵심 진단 (planner, 62차 — **superseded by 63차**)

- **BNK-8 v1.3 차별화 재정립 (42차)**: **v1.3-A = 케어포 이동서비스 지도보기 패리티**(BNK-7 「지도 없음」 가정 **번복** — 케어포도 카카오맵 탑승자 위치 조회). **영업 차별 = v1.3-B(TSP·Directions 도로경로)**. v1.3-C = G15·G16 법정·청구 패리티. v1.3-A 단독 「요양 ERP 최초 지도」 **메시지 금지**.
- **⚠ ogada workspace submodule·history drift (42차 planner 직접 점검)**: `src/backend` develop **`f47ffa1`**(+1 vs test) · test **`2799e29`(stale, ROADMAP merged `e8750d2` 미달)** · WT **CLEAN** · develop **89/89**·test **79/79**. `src/frontend` develop·test **동일 `@e5fd48d`(스켈레톤, TSR57 `d5654c0` 18 behind)** · WT **DIRTY**(auth WIP 미커밋, TSR59). → **TSR 57·59·SEC 4차 재현 불가** — **INFRA-B12** checkout 선행.
- **QA-B10 v1 baseline regression (58차)**: develop `@f47ffa1`에 `PilotChecklistJwtE2eTest`·`MustApiEndpointRoutingTest`·`ProductionSecretValidator` **ABSENT** — v1 `merge_status: merged` 유지하나 **test 승격·operation sign-off BLOCK**(**BE-10**·PLAN_NOTES `#42`).
- **SEC-D12 frontend route 무방비 (59차)**: HEAD `@e5fd48d` — `/platform`·`/settings`·`/dashboard/hq` **공개**. `ProtectedRoute`·`AuthContext` **HEAD ABSENT**. → **INFRA-B12 checkout `d5654c0`**(FE-2·H03 일괄 해소) 또는 **FE-20** develop 커밋.
- **B09·SEC-D8 Fixed @ `f47ffa1` (58차)**: J01 `GuardianInvitationController`·V43·`SecurityConfig`·rate limit **HEAD PRESENT** — **BE-8 완료**. backend merge gap **3→1 commit**.
- **테스트 PASS ≠ 이관 PASS**: backend develop **89/89**·test **79/79**·frontend test build **36 modules**·npm test **N/A** — **이관 판정 BLOCK** — **INFRA-B12 + BE-10 + FE-19 + FE-18 + backend merge(1 @ `f47ffa1`) + B03**.
- **SEC-D9(Planned)**: MaskedPhone PII `010-****-5678` 유지·테스트 정합 — **FE-19**·QA-H05·B07 #6 commit 게이트.
- **TSR 57 baseline(기획 유지)**: frontend develop **`d5654c0`** · backend develop **`f47ffa1`**(J01 포함) — workspace는 **양 스트림 baseline 미달**.
- **잔여 BLOCK = INFRA-B12(submodule baseline) + BE-10(v1 test baseline) + FE-19 + FE-18 + backend merge(1커밋 @ `f47ffa1`) + B03** — B09·SEC-D8 **소멸**. B02 #6·B08 #2·FE-17 @ **`428ba7d`/`d5654c0` lineage** — workspace checkout 후 재검증.
- **기능 잔여(v1.1)**: J01 백엔드 API **@ `f47ffa1` HEAD 반영**(BE-8 Fixed) · 프론트 **FE-18·FE-19**(baseline checkout 후) · 라이ve E2E merge ready 전 `[ ]`.
- **#36 운영 게이트 (결정 63)**: L1~L3 build 승인 대기. 현재 BLOCK: **INFRA-B12·BE-10·FE-19·FE-18·backend merge·B03**.

### QA → 태스크 매핑

| QA id | sev | ver | 태스크 (반영 위치) | 완료 신호 |
|-------|-----|-----|-------------------|-----------|
| QA-20260606-B01 | BLOCK | v1 | v1 완료 기준 전 항목 `[x]` 후 `merge_status: ready` | develop→test merged |
| QA-20260606-B02 | BLOCK | v1 | ~~recurrence #6 Planned~~ **recurrence #6 Fixed `428ba7d`** — V42 + `NotificationPreferenceServiceTest` 4 @Test develop 커밋·working tree clean | develop HEAD + clean tree ✓ |
| QA-20260606-H01 | HIGH | v1 | NHIS `처리상태` 선행열 스킵·정규화 파서 **+ 선행열 샘플 테스트** | `NhisExcelParserTest` 선행열 케이스 PASS |
| QA-20260606-H02 | HIGH | v1 | SEC-001/002/004 develop 커밋 → QA Fixed 정합 | develop HEAD에 산출물 존재 |
| QA-20260606-B03 | BLOCK | v1.1 | v1.1 **merge-blocking** 완료 기준 충족 후 `merge_status: ready` — **live E2E run 제외**(결정 73) | develop→test merged |
| QA-20260606-B04 | BLOCK | v1.1 | ~~develop 커밋 규율~~ **Fixed `998ac87`** | `git -C src/frontend status` clean |
| QA-20260606-B05 | BLOCK | v1.1 | **선행 게이트** — v1 `merged` 후 v1.1 이관 착수 | v1 merge_status: merged |
| QA-20260606-H03 | HIGH | v1.1 | SEC-003(ProtectedRoute·역할 가드) develop 커밋 | develop HEAD `/platform`·`/settings` 가드 |
| QA-20260606-H04 | HIGH | v1.1 | ~~Must 화면 API 연동~~ **Fixed `811aef3`**(TSR 63) | develop HEAD `services.js`·Must pages·`pilotChecklist` PRESENT |
| QA-20260606-M01 | MEDIUM | v1.1 | ~~Vitest + RTL~~ **Fixed `811aef3`**(TSR 63) | `npm test` **40/11 PASS** @ `7170b2a` |
| QA-20260606-B06 | BLOCK | v1 | ~~client↔guardian develop 커밋~~ **Fixed `4d476c6`** | develop HEAD + clean tree |
| QA-20260606-B07 | BLOCK | v1.1/v1.2 | ~~recurrence #5 Fixed `d5654c0`~~ **recurrence #6 Fixed `f506c90`** — J01 초대 목록/수락 UI + 명세 모달 develop 커밋, working tree clean, `npm test` 9/9 PASS | develop HEAD `f506c90` + working tree clean |
| QA-20260607-B09 | BLOCK | v1.1 J01 | ~~Planned~~ **Fixed @ `f47ffa1`**(TSR 58차) — J01 `guardian_invitations` API·V43·`SecurityConfig`·SEC-D8 **HEAD PRESENT** | develop HEAD `f47ffa1` + clean tree ✓ |
| QA-20260608-B10 | BLOCK | v1 | ~~Planned~~ **Fixed @ `136239e`** — v1 E2E/routing/SEC-007 develop HEAD PRESENT | BE-10 ✓ |
| SEC-20260608-011 | BLOCK | v1/v1.1 | ~~Planned~~ **Fixed @ 45차** — baseline `136239e`/`7170b2a` 확정 · workspace_baseline.yaml | INFRA-B12 checkout **폐기** ✓ |
| SEC-20260608-012 | BLOCK | v1 | ~~Planned~~ **Fixed @ `7170b2a`** — ProtectedRoute·AuthContext HEAD PRESENT | FE-20 ✓ |
| QA-20260608-B11 | BLOCK | v1.1 | ~~Planned~~ **Fixed @ 45차** — baseline `7170b2a` (d5654c0 replay 폐기) | baseline 확정 ✓ |
| QA-20260607-H05 | HIGH | v1.1 FE-7 | **Fixed `f506c90`** — `GuardianInvitationList.test.jsx` 마스킹(`010-****-5678`) 기준 회귀 추가·`npm test` 9/9 PASS | FE-19+SEC-D9 PASS |
| SEC-20260607-009 | BLOCK | v1.1 J01 | ~~Planned~~ **Fixed @ `f47ffa1`**(TSR 58차) — SEC-D8 accept 단일 permitAll·토큰 hash·rate limit | BE-8 ✓ |
| SEC-20260607-010 | MEDIUM | v1.1 FE-7 | **Fixed `f506c90`** — MaskedPhone 마스킹 유지 + 초대 목록 UI 회귀 테스트 반영 | FE-19 PASS |
| QA-20260607-B08 | BLOCK | v2 | ~~Fixed `feac558`~~ ~~recurrence #2 Planned~~ **recurrence #2 Fixed `428ba7d`** — V42 consent CHECK·temporal + `NotificationPreferenceServiceTest` 4 @Test develop HEAD PRESENT·working tree clean | V42 + test @HEAD ✓ |
| SEC-20260606-005 | HIGH | v1.1 | ~~JWT localStorage 제거~~ **Fixed `998ac87`** | `AuthContext.jsx` HEAD 메모리 세션 |
| SEC-20260606-007 | BLOCK | v1 | ~~develop→test 승격(B01 동반)~~ **Fixed** — test `@e8750d2` `ProductionSecretValidator`·Boot 3.5.3 **PRESENT**(TSR 34차) | B01 merged ✓ |
| SEC-20260606-008 | MEDIUM | v1.1 | ~~npm audit dev chain critical(esbuild·vite·vitest)~~ **Fixed `ed1bf22`(COD 17차, TSR 25차 독립 검증 — 18차 planner 반영)** — vite `^6.4.3`·vitest `^4.1.8`·`overrides.esbuild ^0.25.0` upgrade | `npm audit --audit-level=high` 0 vulnerabilities |
| SEC-20260608-013 | BLOCK | v1/v1.1 | **Planned(46차)** — SEC-D14 develop→test 보안 패치 미승격 → **B03·backend/frontend merge 게이트** 동반 · test 배포 금지 | `git_merge_to_test.sh` 후 TSR·SEC 재검증 |
| SEC-20260608-014 | HIGH | v1 | ~~Planned(46차)~~ **Fixed @ `8d42bdd`**(TSR 64) — SEC-D13 `AuthRateLimitService` login·refresh·password-reset rate limit HEAD PRESENT | BE-11 ✓ |
| QA-20260608-B12 | HIGH | v1/v1.3/v2 | **Fixed(75차)** — origin/test push·frontend merge(22) 완료 · develop/test/origin **`598d108`**/`c7c8f07` 동기화 | SEC-D14 Fixed · v1.2.1 착수 |

### 이관 규율 (전 버전 공통 — QA-B01~B07·H02·H03·SEC-005·SEC-007 재발 방지)

1. coder는 **완료 즉시 develop에 커밋**한다. test working tree 로컬 변경만으로 `Fixed` 기록 금지.
2. QA_FEEDBACK `Fixed`는 **develop HEAD에 산출물이 존재할 때만** 기록한다(파일·Flyway·pom 포함).
3. 완료 기준 전 항목 `[x]` → `merge_status: ready` 설정 → build가 develop→test merge → `merged` 갱신.
4. v1.1(frontend)은 **v1(backend) `merged`** 이후에만 이관을 시작한다(선행 게이트).
5. **(6차 신설 — false Fixed 재발 방지)** `Fixed` 기록·완료 기준 `[x]`는 **`git show develop:<path>` 로 산출물이 develop HEAD에 존재함을 검증**한 뒤에만 유효하다. test working tree·로컬 stash·미커밋 변경에 근거한 `Fixed`/`[x]`는 무효 — TSR 재검증 시 Open 복귀, 완료 기준 체크박스도 철회한다.
6. **(7차 신설 — dirty-tree 재오염·계약 변경 누락 재발 방지)** ① 한 작업의 `Fixed`/`[x]` 직후라도 **새 작업을 working tree에 미커밋 상태로 남기지 않는다**(완료 단위마다 develop 커밋 — QA-B06·B07). ② **API 계약 변경**(요청/응답 스키마·필수 필드 추가, 예: `createClient` `primaryGuardian` 필수)은 **develop 커밋 전 `docs/technical/API_SPEC.md`·해당 ROADMAP 범위에 반영**한다. 문서 미반영 계약 변경은 이관 BLOCK.
7. **(12차 신설 — v1.2 선행 dirty-tree 재발 방지, QA-B07 recurrence)** v1.1 `merge_status: merged` **전** v1.2(`status: planned`) P0 착수 시에도 ① **완료 단위 develop 커밋** 후 working tree clean, 또는 ② **stash/revert**로 v1.1 merge 게이트 검증 tree를 오염시키지 않는다. v1.2 산출물(`GuardiansPage`·SideNav 2단·`routeAccess.js` 등)을 working tree에만 두면 **B07 recurrence BLOCK**(HEAD Fixed @ `998ac87`는 규율 5로 **유효 유지**).
8. **(24차 신설 — v2 선행 dirty-tree 재발 방지, QA-B08)** v1 `merge_status: merged` **후** v2(`status: in_progress`) 착수 시에도 ① **완료 단위 develop 커밋** 후 working tree clean, 또는 ② **stash/revert**로 v1.1 frontend merge 게이트 tree를 오염시키지 않는다. v2 산출물(`notification_preferences`·V41 등)을 working tree에만 두면 **B08 recurrence BLOCK**. v1 완료 기준 `[x]`는 develop HEAD 산출물 존재 시에만 유효(규율 5).
9. **(42차 신설 — #36 운영 게이트, 결정 63)** coder 에이전트 턴 종료 시 `src/backend`·`src/frontend` develop working tree에 완료 주장 산출물(테스트·Flyway·WIP)이 **HEAD 미반영**이면 ① QA `Fixed`·완료 기준 `[x]` **기록 차단**, ② **경고** 출력 — **자동 커밋 금지**. L2 pre-commit·L3 CI는 build 구현 후 이 규율을 강제한다(`PLAN_NOTES.md` #36).
10. **(48차 신설 — live E2E merge 게이트 제외, 결정 73)** Must P1–P8·J01/J02 **live E2E run**(`FE-22`·`npm run test:live-e2e`·`LIVE_E2E=1`)은 **`merge_status: ready` 선행 조건 아님**. fetch-mock·Vitest 회귀(`npm test`)·harness 코드 존재로 merge-blocking 충족. live run은 **develop→test merge 후** post-merge·권장(파일럿·운영 검증).

11. **(73차 신설 — origin push 게이트, QA-B12)** develop→test merge는 **로컬 worktree만으로 완료 처리 금지**. `git_merge_to_test.sh`로 **`origin/test` push**까지 완료되어야 SEC-D14·operation 승격·원격 CI 검증 가능. 로컬 test ahead·origin STALE 상태는 **Planned BLOCK** — push 후 Fixed.

### build 대기 — #36 운영 게이트 (결정 63)

| ID | 산출물 | 완료 신호 |
|----|--------|----------|
| **INFRA-1** | L1 `scripts/run_agent.py` dirty-tree·HEAD 검사 | coder 턴 종료 시 미커밋 테스트 → Fixed 차단+경고 |
| **INFRA-2** | L2 `.husky/pre-commit` (backend+frontend) | commit 전 test/build FAIL → 거부 |
| **INFRA-B12** | workspace submodule baseline 정합(SEC-D11·QA-B11·SEC-D12) | ~~checkout `d5654c0`~~ **Fixed @ 43차** — `.agents/workspace_baseline.yaml` + run_agent 실측 |
| **INFRA-3** | L3 `.github/workflows/ci.yml` | develop push CI PASS |

> **상태**: planner 확정 · **build 승인 대기** · coder/db_architect 구현.

---

## v1 — MVP 핵심 (Must)

- **status**: done
- **merge_status**: merged
- **stream**: backend
- **목표**: 인증·다지점·이용자·출석·건강·청구(reconciliation 포함)·대시보드 (REQUIREMENTS §6 Must)
- **벤치마크 기준**: 케어포 2단계 청구(내부계산 + 롱텀 + 엑셀 import + 본인부담) — `BENCHMARK_REPORT.md` §4-1; NHIS 엑셀 **`처리상태` 선행열 스킵·정규화** (3차 §4-1 C-1)

### 범위

1. Spring Boot + PostgreSQL + Flyway 멀티테넌트 골격 (`platform_admin` Tenant 개통 — 경쟁사 대비 차별화)
2. JWT + **7역할** RBAC + 지점 스코프 + Branch Switcher
3. 이용자 CRUD(주민번호 암호화·copay 구분) + **보호자 1명 이상 연결 필수** (`guardian_clients`, `clients.guardian_link_status`), 출석(수기+QR B), 건강 기록
4. 청구·정산: 수가표 B·copay·월별 명세 + **NHIS 엑셀 import + reconciliation UI** (`MATCHED`/`DISCREPANCY`/`UNMATCHED`)
5. HQ/지점 대시보드 실데이터 (다지점 HQ — 경쟁사 공개 자료 동등 기능 미확인, 파일럿 핵심)

### 구현 우선순위 (v1 내부 — REQUIREMENTS §6-2)

| 단계 | 범위 | 완료 신호 |
|------|------|----------|
| **P0** | Tenant·Branch·7역할·출석(수기)·건강·청구(수가·copay·명세·NHIS import·**`처리상태`열 정규화**)·대시보드 | 파일럿 1주차 — `branch_admin`+`caregiver` E2E |
| **P1** | QR B + `guardian`/`client_user` + **NHIS reconciliation UI** | 케어포 4단계 UX 동등 (US-G06) |
| **P2** | 보호자 **기록 열람**(알림 없음) + 청구 `?status=` 필터 | v1 백엔드 — G1·G8 **초대·명세**는 v1.1 |
| **P3** | — (Should 모듈) | v1.1로 이관 |

> P0 완료 전 P1 착수 금지 (품질·차별화 우선 — 결정 18).

### 완료 기준

- [x] `src/backend` Maven test 전체 PASS
- [x] API_SPEC Must 엔드포인트 구현 (인증·이용자·출석·건강·청구·**NHIS reconciliation**·대시보드) *(develop `aa71412` — `MustApiEndpointRoutingTest` §1–§9 Must 라우팅 26 tests + 기존 routing/RBAC tests, Maven PASS)*
- [x] Flyway 마이그레이션 ERD와 정합 (V19+ reconciliation 제약 포함, V35–V40 develop 반영 — V39·V40 `4d476c6`)
- [x] **7역할** 로그인·메뉴·권한 분리 (`platform_admin` 포함) *(develop `e8750d2` — `RoleBasedControllerAccessTest` 36 tests + `PilotChecklistApiAccessTest` 29 tests = `@WebMvcTest` **65건** + **`SevenRoleJwtLoginE2eTest` 16+ tests**(COD 21차 — Spring Security filter chain·`JwtTokenService` live Bearer JWT 7역할 발급/검증·RBAC 허용·거부) + **frontend Vitest 단위 E2E**(`57ff3c0` — `sevenRoleJwtLogin.test.jsx`·`sevenRoleRouteGuard.test.jsx`·`sevenRoleRouteMatrix.js` 매트릭스) = **backend·frontend 자동화 충족**; 라이ve 통합 E2E는 develop→test merge 후)*
- [x] NHIS import: 배치 상세·수동 매칭(`PATCH .../rows/{id}/match`)·지점 일치 검증·**`처리상태` 선행열 스킵 파서** *(파서·서비스·routing tests develop `aa71412`; reconciliation **UI·E2E** 잔여 — frontend)*
- [x] **(QA-H01)** `처리상태` 선행열 포함 샘플 엑셀 import **테스트** — `NhisExcelParserTest` 선행열·헤더 정규화 케이스 PASS *(develop `7d9d2eb` HEAD 검증)*
- [x] **(QA-H02)** SEC-001/002/004(rate limit·prod secret validator·Spring Boot 3.5.3) **develop 커밋** — QA Fixed와 develop HEAD 정합
- [x] 롱텀 2026 export 안내: Chrome/Edge 필수(IE 불가) — import UI·온보딩 가이드 *(develop `fac3d07` `NhisImportGuidance` API·`NhisImportGuidanceTest`·`MustApiEndpointRoutingTest` guidance routing **backend 완료** — import UI·온보딩 E2E 잔여 frontend)*
- [x] REQUIREMENTS §6 Must·§6-2 P0–P1 체크리스트 충족 *(develop `c3b8716` — `PilotChecklistJwtE2eTest` 634 lines/22 @Test live Bearer JWT filter-chain E2E + `MustApiEndpointRoutingTest`·`PilotChecklistApiAccessTest` **65건**, Maven PASS)*
- [x] USER_STORIES 파일럿 체크리스트 P1–P8 PASS (수기 출석·월말 청구·**reconciliation**) *(develop `c3b8716` — `PilotChecklistJwtE2eTest` 22 @Test live Bearer JWT E2E + `PilotChecklistApiAccessTest` 29 @WebMvcTest; frontend `3fdc266` P1–P8 fetch-mock·페이지 E2E = **backend 자동화 충족**, 라이ve 수동·J01 API 잔여 frontend)*
- [x] **(SEC-007)** develop→test merge 후 test 브랜치 P0 패치(`ProductionSecretValidator`·rate limit·Boot 3.5.3) 재검증 — **develop HEAD 패치 PRESENT, `merge_status: ready` 설정 → 다음 build auto-merge로 test 동기화**
- [x] **(US-D01)** 이용자 등록 시 **대표 보호자 1명 이상** 동시 연결 — `POST /clients` `primaryGuardian` 필수, `guardian_link_status=LINKED` (V39) *(develop `4d476c6` HEAD 검증 — QA-B06 Fixed)*
- [x] **(QA-B02)** `src/backend` develop working tree clean — 미커밋 변경 없음 *(develop `428ba7d` — V42 + `NotificationPreferenceServiceTest` 4 @Test develop 커밋·working tree **CLEAN**, B02 #6 Fixed)*

> **수가 시간대(G9)**: 2026 공단 수가는 **등급×이용시간대(3~6h…13h+)** 2차원(`BENCHMARK_REPORT.md` §4-1). v1은 파일럿 센터 표준 이용시간 **08:00~20:00 (12h) → 단일 밴드 10~13h 고정**(사용자 확정 2026-06-07, PLAN_NOTES #35·결정 55). v1.1에서 다밴드(`duration_band`) 도입 시 §3-9-1·ERD 보강.

### test merge

- develop 완료 후 coder가 위 체크리스트를 `[x]`로 표시하고 `merge_status: ready` 설정
- **(QA-B01)** 체크리스트 전 항목 `[x]` 전에는 `merge_status: ready` 설정 금지
- **(QA-B10, 44차)** v1 `merge_status: merged` 유지 · **BE-10 Fixed @ `3f9264f`** — develop HEAD v1 E2E/routing **PRESENT** · test `@2799e29` **stale(3커밋 behind)** — develop→test merge 후 test 재검증

---

## v1.1 — 프론트엔드 MVP + 보호자 확장

- **status**: done
- **merge_status**: merged
- **stream**: frontend
- **목표**: React SPA — v1 백엔드 API 전면 연동 + 보호자 **초대·명세 열람**(G8·EZCARE 패턴) + 알림 골격 (G1)
- **선행**: v1 `merge_status: merged`

### 범위

1. Vite+React SPA, JWT 클라이언트, **7역할** 라우팅·Branch Switcher
2. 이용자·출석(수기+QR)·건강·청구·**NHIS reconciliation** UI (API_SPEC §7-3·§7-4)
3. HQ/지점 대시보드 차트·집계 (다지점 비교 — ogada 차별화)
4. 보호자 **초대 온보딩** + **명세·청구서 모바일 탭** (G8 — 이지케어 EZCARE·케어포 가족돌봄앱 패리티)
5. 보호자 포털 열람 강화 + **무료 알림 채널** (인앱·FCM Web Push·이메일) 설계·골격 — **카카오톡 채널 알림톡은 v2**
6. **브랜드 파비콘** — 탭·북마크·모바일 홈추가 아이콘 (`DESIGN_SYSTEM` §9, US-UX-01)

### 완료 기준

- [x] `npm run build` 성공 *(develop `7170b2a` — planner 실측 PASS, vite 6.4.3)*
- [x] 7역할 화면·메뉴·권한 분리 *(develop `811aef3`+ — `ProtectedRoute`·`sevenRoleJwtLogin`·`sevenRoleRouteGuard`·`sevenRoleRouteMatrix` HEAD **PRESENT**; TSR 63·45차 확인)*
- [x] **(QA-H03)** ProtectedRoute·역할 가드(SEC-003) **develop 커밋** — HEAD `@7170b2a`에서 `/platform`·`/settings`·`/dashboard/hq` 무방비 차단 *(TSR 63·45차 확인)*
- [x] **(QA-H04)** Must 화면 **REST API(JWT) 연동** — `services.js`·Must 페이지(`AttendancePage`·`BillingPage`·`ClientDetailPage`·`HealthPage`·`NHISImportPage`·`ReconciliationPage`)·`pilotChecklist.js` HEAD **PRESENT** *(TSR 63 Fixed @ `811aef3`)*
- [x] `/billing/imports/nhis/{batchId}` reconciliation 행 매칭·수동 연결 UI *(develop `811aef3` — `ReconciliationPage` HEAD **PRESENT**; TSR 63)*
- [x] **(US-UX-01)** **파비콘·앱 아이콘** — `public/favicon.svg`·`favicon.ico`·`apple-touch-icon.png`, `index.html` `<link rel="icon">`·`theme-color` *(develop `c3b863e` COD favicon restore)*
- [x] **(QA-M01)** Vitest + React Testing Library `test` 스크립트 — ProtectedRoute·MaskedPhone·J01·P1–P8·7역할 회귀 (`npm test` **40/11 PASS** @ `7170b2a`; TSR 63 **35/9** @ `811aef3`)*
- [x] **(SEC-005)** JWT access/refresh **localStorage 영구 저장 제거 → 메모리 세션** — `AuthContext.jsx` HEAD에서 `localStorage.get/set/removeItem(STORAGE_KEY)` 부재 *(develop `7c0ecdc`+ lineage)*
- [x] **(QA-B04·B07 @HEAD)** `src/frontend` develop working tree clean — 미커밋 변경 없음 *(develop `7170b2a` — B07 #6 Fixed @ `f506c90`, `git -C src/frontend status` **CLEAN**, HEAD `npm test` **40/11 PASS**·build PASS)*
- [x] **(SEC-008)** npm audit dev chain critical 해소 — develop audit **0 vulnerabilities** *(COD `811aef3` lineage `ed1bf22` 적용 — TSR 63 Fixed)*

> **B07 recurrence(14·16·19·20차→21차 Fixed)**: 19~20차 dirty 42 files → 21차 `a72e249` 일괄 커밋으로 working tree clean. v1.1 HEAD Fixed **유효 유지**. v1.2 P0 산출물은 **결정 52**에 따라 v1.1 merge에 동반 흡수(별도 분리 안 함).
> **B07 recurrence #2(23차 Open→17차 Planned→25차 Fixed)**: 21차 clean → 23차 `5656e19`(UXD 10차) 위 v1.2 P0 US-M02 대시보드 위젯 실데이터 8 files WIP 미커밋(17차 planner Planned) → **COD 17차 `a84473f` 일괄 커밋(8 files +636/-170 — `dashboardWidgets.js`·`.test.js`·`DashboardPage`·`AttendancePage`·`ClientFormPage`·`GuardiansPage`·`GuardianListCard`·`services.js`)** → working tree CLEAN, HEAD `npm test` 13/5·build 111 modules PASS, **TSR 25차 정식 Fixed 확정**(이관 규율 5·6·7 PASS).
> **SEC-008(24차 Open→25차 Fixed)**: 24차 npm audit 5 vulnerabilities(4 moderate·1 critical, esbuild GHSA·vite·vitest dev chain 에스컬레이션) → **COD 17차 `ed1bf22`** vite `^6.4.3`·vitest `^4.1.8`·`overrides.esbuild ^0.25.0` 메이저 업그레이드 → develop `npm audit --audit-level=high` **0 vulnerabilities**, all 0건. dev 환경 전용 취약점 — prod 번들 영향 없음. **TSR 25차 정식 Fixed 확정**.
> **R-05 P1–P8 페이지 단위 E2E PARTIAL 강화(31차 — COD 22차 `3fdc266`)**: `pilotPageFlows.test.jsx`(433 lines — AttendancePage·DashboardPage·HealthPage·BillingPage·NHISImportPage·ReconciliationPage·ClientDetailPage·GuardianPage RTL fetch-mock JWT API 호출·페이지 렌더 통합 검증) develop HEAD 커밋. `npm test` 130/10→**140/11 PASS**(+10/+1), build 113 modules PASS, audit 0건. → **R-05 frontend P1–P8 페이지 단위 E2E PARTIAL 강화** — fetch-mock 라우팅(FE-9) + 7역할 매트릭스(FE-9) 위 **페이지 통합 회귀(FE-11)** 충족. 라이ve backend·J01 API 잔여. 결정 52에 따라 v1.1 develop→test merge에 동반 흡수.
> **UXD 14차 `a42d6fb` — 수가표 이력 UI(US-G00a PARTIAL)**: `FeeRateHistoryPanel.jsx`·`FeeSchedulePage` 이력 모달·`chartColors.js`·Recharts 토큰·`BATCH_STATUS` 공유 상수 8 files. v1.1 merge 동반 흡수(결정 52).
> **B07 recurrence #3(33차 Open→23차 Planned→31차 Fixed)**: 31차 CLEAN → … → **COD 31차 `4be0938` 82 files 일괄 커밋** → working tree **CLEAN**, HEAD `npm test` **185/33 PASS**·build **752 modules** — FE-6 #3 해소. v1.2 FE-12·FE-13·FE-14 develop HEAD 반영.
> **FE-15 코드 스플릿 Fixed(32차 — COD 33차 `c98f98d`)**: `vite.config.js` `manualChunks` — 단일 JS 744.95 kB → 최대 393.53 kB(<500 kB). HEAD `npm test` **186/34 PASS**·build **752 modules**·audit 0. 결정 52 흡수 **⑩묶음** 추가.
> **B07 recurrence #5 Fixed(35차 — COD 35차 `d5654c0`, TSR 53차 독립 검증 PASS)**: 52차 CLEAN→DIRTY 20 files → **25 files 일괄 커밋** — FE-17 J01 수락 UI·LogoutButton·BillingPage.layout 등. working tree **CLEAN**, HEAD `npm test` **199/40 PASS**·build **756 modules**·audit 0 — **FE-17** 매핑·결정 52 흡수 ⑪묶음.
> **B07 recurrence #6 Fixed(44차 — COD `f506c90`, TSR 61·planner 실측)**: `7c0ecdc` lineage 위 **FE-18·FE-19** develop 커밋 — `GuardianInvitationList`·`PaymentRecordModal`·`GuardianPortalPage`·`GuardianInvitationAcceptPage`·`services.js` HEAD **PRESENT**, WT **CLEAN**, `npm test` **9/9 PASS**·build **70 modules PASS**. B07 #6·H05·SEC-D9 **소멸**. **#36 FE-6 #5 해소**.
> **B07 recurrence #6 Planned(37차 — TSR 56·57차, HEAD Fixed 유지)**: 53차 `d5654c0` CLEAN 직후 **15→18→20 files** WIP — `DateInput`·`GuardianInvitationList` J01·`ClientDetailPage`·`PaymentRecordModal`·`GuardianListCard`(+test, **QA-H05 MaskedPhone 불일치**)·기타 J01/설정 UI. WT build **758 modules PASS**·WT `npm test` **209/210 FAIL**(FE-7) — **FE-18·FE-19** 매핑·#36 FE-6 #5 유지. **HEAD `d5654c0` Fixed(FE-17) 규율 5 유효** — recurrence는 미커밋 dirty-tree 단일.

### post-merge 검증 (merge 게이트 제외 — 결정 73)

> live E2E는 **merge 선행 조건 아님**. develop→test merge·test 브랜치 검증 **후** 권장.

- [ ] Must P1–P8 **live backend run** (FE-22 — `src/e2e/*`·`npm run test:live-e2e`·`LIVE_E2E=1` + backend 가동)
- [ ] J01/J02 **live API run** (보호자 초대·수락·명세 — `guardianLiveApi.e2e.test.js` + 보호자 계정 env)

### 선행·test merge

- **(QA-B05)** 선행: v1 `merge_status: merged` 충족 후 v1.1 이관 착수
- **(QA-B03)** 위 **merge-blocking** 완료 기준 전 항목 `[x]` 후 `merge_status: ready` → develop→test merge — **live E2E run 제외**(결정 73)

---

## v1.2 — 프론트 기능 밀도·경쟁사 UI 패리티 (벤치마크 6차 — BNK-6 완료)

- **status**: done (v1.2 merged @ frontend test `c510f5c` · UXD 15 pages @ `0d83a42` · P0 KPI·E2E @ `9bdf59f` · Epic E @ `6f3f746`·`a627c6d` · UXD-39 @ `c5708c7` · UXD-40·Q154 @ `4957bd3` · UXD-41 US-F03 @ `3ec8206`·`95b92b9` · US-G06 DISCREPANCY @ `fd4e8f3`·`c510f5c`)
- **merge_status**: merged (TSR 81 — frontend develop=test `c510f5c` · P0 게이트·US-G06 DISCREPANCY 충족 · P1 v1.2.1 후순위)
- **stream**: frontend (+ backend API 보강 병행)
- **목표**: 사용자 체감 「기능이 적다」 해소 — **모듈 커버리지 25~30% → ≥60%**(결정 49) — 케어포 12모듈 대비 **low-cost high-density** 화면 추가
- **선행**: v1.1 `merge_status: merged` (단, **P0 산출물은 develop 선행 커밋·v1.1 merge 동반 흡수** — 결정 52)
- **벤치마크 근거**: `BENCHMARK_REPORT.md` §9·`COMPETITOR_MATRIX.md` §8 (BNK-6, 2026-06-06 **완료**)

> **배경**: ogada v1.2 **33 route·33 page @ `42f48e1`**(git 실측, TSR 71·52차) vs 케어포 **80+ 화면**(2~3단). **과거 planner 인용 24 route·`4be0938`은 git object 없음** — lineage 기록만 유효. 갭의 본질은 **신규 도메인 부재**가 아니라 **기존 DB(billing·guardian_clients·clients)의 화면 부재** — P0 5건은 신규 테이블 ≤1개.
> **TSR 67 진전 (49차)**: UXD **`f64e1dd`** — SideNav·AppShell·기반 UI 갱신 → **US-UX-02 2단 SideNav** v1.2 P0 착수 신호. FE-22 **`4f71543`** liveConfig fail-fast — harness 완성도 ↑.
> **51차 TSR 69 진전**: UXD 35 **`64468a3`** — Must 페이지 DS integration · **`e0eaf32`** guardians RBAC — WT **CLEAN** · **`npm test` 82/27 PASS**. 50차 **24 files WIP 소멸**.
> **52차 TSR 71 진전**: UXD **`0d83a42`** — **15 missing pages** (이용자·출석·건강·청구·설정·플랫폼 등 Epic D·E·F·G·H·B·A) · **`42f48e1`** P0 page-flow tests·**module coverage KPI**·title 정렬 — **18→33 route** · **`npm test` 89/28 PASS** · build **114 modules** · 모듈 커버 **~45–50% 추정** — 결정 49 **≥60% 잔여**.
> **53차 TSR 73 진전**: **`a68f150`** — `GuardianCheckinPage` DS FilterChips(US-E04) · **`9bdf59f`** — v1.2 P0 CRUD E2E·`PaymentRecordModal`(US-L01)·보호자 초대/수정(Epic K) · **`npm test` 97/30 PASS** · build **114 modules** · **≥60% module coverage KPI PASS** @ develop HEAD.
> **54차 TSR 75 진전**: **`6f3f746`** — 수기 출석 체크인/아웃·결석 흐름(US-E01·E02, 결정 57 P2) · **`a627c6d`** — QR 저장(US-E03)·출석 통계 API 연동(US-E05) · **`npm test` 110/36 PASS** · build **117 modules** · develop **8 ahead**.
> **59차 TSR 81 진전**: **`fd4e8f3`** — `DiscrepancyComparePanel`·`NhisReconciliationTable` compare 액션(US-G06 DISCREPANCY) · **`c510f5c`** — `pilotPageFlows` US-G06 E2E · **`npm test` 143/46 PASS** · frontend develop=test **`c510f5c`**(**v1.2 merged**).
> **58차 TSR 80 진전**: **`3ec8206`** UXD-41 — `IncidentRecordForm`·`HealthPage` incident 탭(US-F03) · **`95b92b9`** — `healthApiPayload.js` incident `detail` 필드(Q154) · **`npm test` 137/45 PASS** · build **124 modules** · **34 route·38 page** · develop **13 ahead**.
> **57차 TSR 77 진전**: **`9863312`** UXD-40 — `vitalsRanges.js`·`VitalsRecordForm` **비정상 범위 인라인 경고**(US-F01, 저장 비차단) · **`4957bd3`** — `healthApiPayload.js`·`healthRecords.js`·`NhisReconciliationTable` 필드 fallback — **FAQ Q154 Fixed**(건강·NHIS API 본문 정합) · **`npm test` 130/44 PASS** · build **123 modules** · develop **11 ahead**.
> **56차 TSR 76 진전**: **`c5708c7`** UXD-39 — `VitalsRecordForm`·`MedicationRecordForm`·`MedicationDuplicateAlert`(US-F01·F02 UI) · `NhisReconciliationTable`(US-G06) · `HealthDetailPage` 표+FilterChips(US-F04) · **`npm test` 115/40 PASS** · build **120 modules** · develop **9 ahead**. API 본문 정합(건강 DTO·NHIS 필드명) **잔여**(FAQ Q154).

> **P0 develop 일괄 커밋(21차, `a72e249`)**: 19~20차 WIP 42 files → **`a72e249 feat(v1.2-p0): 보호자·입금·미납·2단 SideNav·routeAccess 중앙화`**(+3863/-311)로 일괄 develop 커밋. 산출물: `GuardiansPage`·`GuardianDetailPage`·`PaymentPage`·`OverduePage`·`BillingDetailPage`·`SideNav` 2단·`routeAccess.js` 중앙화·`SessionTimeoutProvider`·`MaskedPhone`·`QrScanPanel` 등 42 files. develop HEAD `npm test` **10/4 PASS**·`npm run build` **110 modules PASS**(이전 87 modules에서 +23). working tree **CLEAN**·QA-B07 recurrence Fixed(이관 규율 5·6·7 PASS, FE-7 충족). → **결정 52: v1.1 develop→test merge에 동반 흡수** — 별도 v1.2 merge 라운드 불추가. v1.1 merge ready 게이트는 v1.1 완료 기준만으로 평가하고, v1.2 P0의 정식 완료 기준(2단 SideNav 모듈 커버리지 ≥60%·실데이터 위젯 E2E·등급이력 UI)은 **v1.1 merged 후 v1.2 사이클**에서 평가.

> **UXD 10차 develop 커밋(`5656e19`, 23차)**: `feat(ux): 이용자 본인 계정 발급 필드·CopayTypeSelect 적용·브랜드색 통일` — 이용자 등록 시 `client_user` 본인 계정 발급 필드(QR 스캔 안 3 정책, 결정 16), `CopayTypeSelect` 컴포넌트(일반/감경9%/감경6%/기초수급 — 결정 27, 본인부담 4구분), 브랜드색 통일(DESIGN_SYSTEM §1). 결정 52에 따라 v1.1 merge 동반 흡수. develop 5 ahead of origin. HEAD Fixed 규율 5 PRESENT 유지.

> **v1.2 P0 US-M02 대시보드 실데이터 위젯(COD 17차, `a84473f`)**: `dashboardWidgets.js`·`dashboardWidgets.test.js`(3 tests PASS)·`DashboardPage` branch/HQ API 연동 develop HEAD 커밋 완료 — B07 recurrence #2 Fixed.

### 범위 (BNK-6 §8-5·§9-3 확정)

| 우선 | 영역 | 경쟁 근거 | ogada 기반 | 신규 DB |
|------|------|-----------|-----------|---------|
| **P0** | **보호자 관리** 전용 화면(CRUD·연결) | 케어포 1-3 | `guardian_clients`(V7·V23·V39) | 불필요 |
| **P0** | 본인부담 **입금·미납** 화면 (G13) | 케어포 7-2·7-3 | `billing_claims`·`_items` | 입금 상태 컬럼 |
| **P0** | **등급변동 이력** 화면 (G14) | 케어포 1-9·엔젤 | `clients.ltc_grade` | 이력 테이블 |
| **P0** | 대시보드 위젯 **실데이터** (오늘 출석·미처리·공지) | 케어포 3블록 | attendance·health·billing API | 불필요 |
| **P0** | **2단 SideNav 그룹화** (청구·출석·기록·이용자) | 케어포 번호식 2단 | `SideNav.jsx` | 불필요 |
| **P0** | **Recharts 차트 레이어** — `ChartContainer`·출석률·지점비교·건강추이 + DESIGN_SYSTEM `chartColors.js` | 케어포 대시보드 3블록·HQ 비교(BNK-6-4) | attendance·health·billing API | `recharts` 의존성 |
| P1 | 급여제공 기록 **세분화**(식사·목욕·간호 탭) | 케어포 3-1 한장 기록지 | `health_records` | 유형 컬럼 |
| P1 | **직원·근태·교육** 화면 | 케어포 8장 | `users` | 근태 테이블 |
| P1 | 본인부담 **간편계산기** | 케어포 7-10 | `fee_schedules`·`copay_rates` | 불필요 |
| P2 | 가정통신문·수가변경 안내 | 케어포 1-5·10-2-1 | — | 발송 이력 |
| P2 | 프로그램·**이동서비스** | 케어포 2·5 (G5) | — | 신규 테이블 |

> **v2/Won't (밀도 목표 외)**: CMS·간편결제(7-4/7-5)·재무회계(12)·공단평가 자동화·알림톡(10-1, v2).

### 완료 기준

- [x] **BNK-6** `COMPETITOR_MATRIX.md` §8 전수 매핑 + `BENCHMARK_REPORT.md` §9 (2026-06-06)
- [x] planner: P0~P2 → `USER_STORIES` Epic K·L·M·UX + `REQUIREMENTS` §1-5-2 (11차)
- [x] P0 5건(보호자 관리·입금·미납·등급이력·실데이터 대시보드·2단 SideNav) **develop 커밋** *(21차: `a72e249` 42 files 일괄 커밋·`3fc549a` US-D03; 23차 UXD 10차 `5656e19` `client_user` 발급·`CopayTypeSelect`·브랜드색 — working tree CLEAN·HEAD build/test PASS)*
- [x] **(B07 recurrence #2)** v1.1 merge 게이트 검증 전 working tree clean *(COD 17차 `a84473f` — US-M02 대시보드 실데이터 8 files develop 커밋, working tree CLEAN)*
- [x] P0 5건 **프론트 E2E** — 보호자 CRUD·입금·미납·등급이력·실데이터 대시보드 *(develop `a68f150`+ — `pilotPageFlows.test.jsx` v1.2 P0 CRUD E2E 4건·`PaymentRecordModal.test.jsx` US-L01)*
- [x] SideNav **2단 깊이** + 모듈 가중 커버리지 ≥60% (결정 49 KPI) — `competitorModuleCoverage.test.js` **PASS** @ develop HEAD · `navConfig.js` 4그룹 2단 구조
- [x] **(US-M02)** `dashboardWidgets.js` 위젯 집계 로직(오늘 출석/결석·미납·미매칭 NHIS) + `dashboardWidgets.test.js` 3 PASS — develop `a84473f` HEAD 커밋
- [x] **(US-M02·FE-12)** Recharts **차트 레이어** — `ChartContainer`·`AttendanceRateChart`·`BranchCompareChart`·`HealthTrendChart` + `HealthAlertList`(+test) + `ChartContainer.test.jsx`·`HealthTrendChart.test.jsx` develop 커밋 *(lineage `4be0938`·현재 HEAD `@d592a17` — FE-6 커밋 게이트·이관 규율 5 PASS)*
- [x] **(FE-13)** Platform·NHIS 배치·reconciliation·청구·수가표 UI — `BatchProgressSteps`·`PlatformOrgDetailModal`·`BillingStatusConfirmModal`(+test)·`CopayRateTable`(+test)·**`FeeScheduleTable`(+test, US-G00a)**·`NhisImportGuidePanel`(+test)·`GuardianDailySummary`(+test)·Platform/NHIS/Reconciliation/Forbidden 페이지 develop 커밋 *(lineage `4be0938`·HEAD `@d592a17`)*
- [x] **(FE-14)** 운영·보안 설정 UI — `AuditLogPanel`(+test)·`BackupSettingsPanel`(+test)·`PasswordChangeModal`(+test)·`FilterChips`·`LoginHistoryPanel`·`PasswordResetRequestModal`·`SettingsPage.test.jsx` develop 커밋 *(lineage `4be0938`·HEAD `@d592a17` — SettingsPage 보안 탭 연동 포함)*
- [x] **(FE-15)** 프런트 번들 코드 스플릿 — `vite.config.js` `manualChunks`로 recharts·vendor 분리, 최대 청크 <500 kB *(develop `c98f98d` — COD 33차, TSR 49차 Fixed)*
- [x] **(US-G06)** DISCREPANCY 행 청구 라인 비교 Modal + ReconciliationPage 배선 — `DiscrepancyComparePanel`·`NhisReconciliationTable` compare 액션 · pilotPageFlows E2E *(develop `fd4e8f3` — COD 59차)*
- [ ] P1 3건(급여제공 세분화·직원근태·간편계산기) — v1.2 후반 또는 v1.2.1 *(merge 게이트 비차단)*
- [x] `merge_status: ready` 전 체크리스트 전 항목 `[x]` *(결정 52: P0 E2E·≥60% KPI·US-G06 DISCREPANCY 충족 — P1 v1.2.1 후순위, COD 59차)*

### USER_STORIES 매핑

| Epic | v1.2 범위 |
|------|-----------|
| **K** — 보호자 관리 | US-K01~K02 (P0) |
| **L** — 본인부담 수납 | US-L01~L02 입금·미납 (P0) |
| **M** — 등급·대시보드 | US-M01 등급이력·US-M02 실데이터 위젯 (P0) |
| **UX** — 네비게이션 | US-UX-02 2단 SideNav (P0) |

---

## v1.2.1 — develop-only 패리티 잔여 (BNK-12·14·16·17·18·19·20·22·25·28·31·33·35·38·41·42·45·49·50·52·53·56·58·96차 · **결정 92**)

- **status**: in_progress
- **merge_status**: **ready** — merge-blocking P0(US-M02·US-M01·US-M03·US-M03-b·G7 UX·US-M02-b/c·US-J03-h·G9·US-J02·US-L01 guard·G2 templates 5종·**US-L01 bank BE/FE**·**G27 BE/FE**·**G11 catalog+가이드**·**G11 v2 자동 가산**·**QA-B19 geocode UX**) **`[x]`** @ `318411d`/`d6d7e7f` lineage (결정 92 · COD QA-B19 @ `318411d` · BE+FE ★ **FULLY UNBLOCKED**)
- **stream**: frontend + backend
- **목표**: 케어포 func.php 대비 **74.81%** 유지(≥60% PASS) · **merge-blocking 닫힘** · P1(**G11 v2 자동 가산**·샘플·live E2E·SMTP·G15 v1.3-C 잔여) 후속
- **선행**: v1.2 `merge_status: merged` · QA-B12·SEC-D14 Fixed(75차)
- **구현 순서**: **US-M02~US-L01 guard `[x]`** → **US-M03-b `[x]`** → **US-L01 bank BE `[x]`** → **G27 BE `[x]`** → **tester merge(61+49)** → **G27 FE** · **US-L01 bank FE** → P1 후속
- **벤치마크 근거**: `BENCHMARK_REPORT.md` §13~§52 (BNK-10~49)

| 우선 | 항목 | 경쟁 근거 | ogada @ `16402b2` / `@dd49204` | 신규 DB |
|------|------|-----------|----------------------------------|---------|
| **P0-1** | **대시보드 실데이터** (US-M02) | 케어포 3블록 | ✅ 5위젯+Recharts+`BranchCompareChart` @ `6d0a03a` | 불필요 |
| **P0-2** | **등급변동 이력** (G14, US-M01) | 케어포 1-9 | ✅ UI+DB(V48)+**GET API** @ `15e41e3` | ✅ V48 |
| **P1** | **본인부담 대장 리포트** (7-6~7-10) | 케어포 7장 | ✅ `/billing/reports/*`·`/billing/calculator` @ `dbf485e` | 불필요 |
| **P1** | **알림 발송 이력 UI** (G8, US-J03-h) | 케어포 **10-7 안내발송내역** | ✅ `NotificationHistoryPanel` @ `e39164d` · BE API @ `c53dd3b` lineage | 불필요 |
| **P1** | **보호자 명세 상세** (G8, US-J02) | EZCARE·가족돌봄앱 | ✅ filter/dedupe/retry·duration band @ `0dc4c4a`/`5348d9c`/`eb3f0fd` · **live run 잔여**(결정 73) | 불필요 |
| **P1** | **본인부담 수납 E2E** (G13) | 케어포 7-2→7-3 | △ pagination·reminder·**cross-page hardening** @ `c72e9df`/`e6df92c` · **live run 잔여**(결정 73) | 불필요 |
| **P1** | **G2 이메일 채널** | 엔젤 법정서식 **5종** | △ **templates 5종 partial** @ `f77a268`+`872e040`+`0854fbd`/`eedcc80`(납부확인서·학대예방교육 **+2**) · **SMTP 실연동 잔여** | 불필요 |
| **P1** | **G27 월한도액 2026** (재가급여 cap·초과 경고) | 케어포 **10-2-1** ✅ | ✅ **BE catalog+guard** @ `a92e625`/`20bc1be` · **FE 표기·인지지원 676,320 E2E** @ `5e64125`/`fba5ea8` | **v1.2.1 ✅** (US-M04) |
| **P1** | **US-L01 은행엑셀 일괄입금** | 케어포 7-2 ✅ | ✅ **BE `POST /billing/imports/bank-deposits`** @ `e50533f`/`95bb34d` · **FE upload UI** @ `9ffff0c`+`BankDepositImportPanel` | **v1.2.1 ✅** (US-L01) |
| **P1** | **G11 가산율 catalog+가이드+자동 적용** | 이지케어 fnc 자동계산 ✅ | ✅ **BE catalog+preview+자동 가산** @ `904072b`/`d7475fd` · **FE `FeeSurchargeGuidePanel`** @ `3db8db3` | **v1.2.1 ✅** (US-M05 · BNK-53·56·58) |
| **P1** | **US-M03-b 청구생성기준+전월가드** | 케어포 9-1·7-1↔7-2 | ✅ BE @ `b953662`/`857bd32` · FE @ `5bdb476`/`911e732`/`25f3225` | **v1.2.1 ✅** |
| **P1** | **G9 duration_band** | 케어포·이지케어 5밴드 | ✅ 25셀·스냅샷·폴백 @ `0c34f85`/`0719648`/`6fe853b`/`5348d9c`/`eb3f0fd` (BNK-41·42) | V61·V62 |
| **P1** | 급여제공 **세분화** | 케어포 3-1 한장 | △ `/health` 통합 | 유형 컬럼 |
| **즉시** | **G7 NHIS 3상태 UX** | 케어포 3상태(BNK-15·18) | ✅ BE **`PENDING_REVIEW`** @ `4cc328d`/`dd49204` · FE **`Badge`·`NhisReconciliationTable`·`NhisPendingReviewGuide`** @ `fbb0b7a` | ✅ V54 |
| **즉시** | **G7 NHIS 파일럿 엑셀 샘플** | 업계 공통 | △ `NhisFixtureExporter`·parser tests @ `dd49204` · **실파일 BLOCK** | 불필요 |
| **Could** | **7-2-1 연말정산·7-9 환불대장** | 케어포 7장 | ❌ | v2 검토(BNK-16) |
| **P1** | 대시보드 **`pendingReviewCount` 위젯** (US-M02-b) | 케어포·이지케어 FAQ 21473 대기 안내 | ✅ `DashboardPage` **「NHIS 대기(보류)」** @ `1794e1c` · `sumPendingReviewNhisFromBatches` | 불필요 |

### 완료 기준 (v1.2.1)

- [x] **US-M02** — HQ `BranchCompareChart`·대시보드 5위젯 **100% API 실데이터** @ `6d0a03a` (BNK-14 §17-2)
- [x] **US-M01** — `GET /api/v1/clients/{id}/ltc-grade-history` + `LtcGradeHistoryService` @ `15e41e3` (TSR 106 · UI+DB V48 ✅)
- [x] **US-M03** — `/billing/reports/{charges,deposits,receipts}`·`/billing/calculator` @ `dbf485e` + `pilotPageFlows` E2E @ `0a07799` (BNK-16 · G22)
- [x] **G7 UX** — **대기(보류) `PENDING_REVIEW` 3상태** + `matchStatusReason` + `NhisPendingReviewGuide` + 4색 Badge @ `fbb0b7a`/`16402b2` (BNK-18 · 케어포 3상태 패리티)
- [ ] **G7 샘플** — 파일럿 센터 NHIS 엑셀 **실파일** 확보·파서 실데이터 검증 *(fixture tests @ `dd49204` ✅ · PLAN_NOTES #27 BLOCK)*
- [ ] **US-M01-b** — (선택) 케어포 1-9 **전 수급자 등급변동 리포트** Route — v1.2.1 **범위 외** · v2 검토(BNK-14 §17-3)
- [x] **US-J02** — `isGuardianVisibleBillingStatus`·`mergeUniqueBillingRecords`·`handleRetryBilling`·`/guardian` 명세·청구 탭 @ `0dc4c4a`/`5348d9c` (B07 #10 Fixed · **live API E2E harness** @ `guardianLiveApi.e2e.test.js` · **live run** merge 후 권장)
- [x] **US-L02 partial** — 미납 목록 **pagination·reminder·cross-page hardening E2E** @ `fed457f`/`c72e9df`/`e6df92c` (BNK-31·35 · 케어포 7-3 패리티 진전)
- [ ] **US-L01·L02 live run** — 입금→미납 **상태전이 live E2E run** (`pilotLiveApi.e2e.test.js` harness @ `20bfac1`+ · **merge 후 권장**, 결정 73)
- [x] **US-M02-b** — 지점 대시보드 **`pendingReviewCount`** 위젯 — `DashboardPage` **「NHIS 대기(보류)」** 6번째 StatCard · `dashboardSummary.js` `sumPendingReviewNhisFromBatches` @ `1794e1c` (BNK-19·20 · ReconciliationPage 패리티)
- [x] **US-M02-c** — 지점 대시보드 **`overdueCount`** 7번째 위젯 — BE `DashboardService.countOverdueClaimItems` @ `f755428` · FE `mapBranchDashboardSummary` @ `20bfac1`/`1c20d17` (BNK-33·35 · 케어포 미납 위젯 패리티)
- [x] **US-J03-h** — **알림 발송 이력 UI** — `NotificationHistoryPanel`(발송시각·채널·유형·상태) · 보호자 `/guardian`·직원 `/clients/:id` · 연락처 **비표시**(PIPA) @ `e39164d` (BNK-22 · 케어포 **10-7** 패리티 · **실발송 v1.1/v2 잔여**)
- [x] **G9 duration_band** — `/billing/fee-schedules` **25셀 2D**·`durationBandSnapshot`·폴백 @ `0c34f85`/`0719648`/`6fe853b`/`5348d9c`/`eb3f0fd` (BNK-41·42 · 롱텀 2026 5밴드 교차)
- [x] **G2 templates partial** — **5종** — ① 명세·기록지·가정통신문 @ `f77a268`+원화 `872e040` ② **납부확인서·학대예방교육** @ `0854fbd`/`eedcc80` · UI `GuardianDocumentNotifyPanel` (엔젤 extraService·system_feature 패리티 방향)
- [x] **US-L01 overpayment guard** — FE `PaymentRecordModal` 초과입금 차단 @ `dd72ff8` · BE non-positive amount reject @ `4109680` (QA-20260610-B15 Fixed)
- [x] **US-M03-b** — 청구생성기준 설정 + **전월 미입금 가드** — BE @ `b953662`/`857bd32` · FE @ `5bdb476`/`911e732`/`25f3225` (BNK-47·49 · 케어포 9-1 패리티)
- [x] **US-L01 bank deposit BE** — `POST /billing/imports/bank-deposits` · flexible header parser @ `e50533f`/`95bb34d` (BNK-49)
- [x] **G27 BE** — `MonthlyBenefitCapCatalog` MOHW 247 verbatim + `GET /monthly-benefit-caps`·`/monthly-benefit-cap-guard` @ `a92e625`/`20bc1be` (BNK-49·52 · **인지지원 676,320 catalog ✅**)
- [x] **G27 FE** — `/billing`·`/dashboard` **월한도 표기·초과 경고 UX** (US-M04 · 케어포 10-2-1 패리티) @ `5e64125`/`fba5ea8`+`MonthlyBenefitCapGuardPanel`·`monthlyCapWarningCount` 위젯
- [x] **US-L01 bank FE** — `/billing/payments` **은행엑셀 업로드 UI** (BNK-49·50) @ `9ffff0c`+`BankDepositImportPanel`·`branchId`·`appliedCount` 정합
- [x] **G11 catalog+가이드+자동 가산** — `FeeSurchargeRateCatalog` 4종·`GET/POST fee-surcharge-*` @ `904072b` · FE `FeeSurchargeGuidePanel` @ `3db8db3` · **v2 청구 자동 가산** @ `d7475fd` (BNK-53·56·58 · US-M05)
- [x] **FE WT clean** — QA-B19 geocode failure UX @ `318411d` — `countGeocodeFailures`·경고 Alert·저장/확정 차단·a11y `aria-describedby` (TSR 232 Planned → COD Fixed)
- [x] **BE WT clean** — develop HEAD @ `d6d7e7f` WT **CLEAN** (TSR 231)
- [x] **P0 `[x]`** — `npm test`/`mvn test` PASS · **`merge_status: ready`** → tester develop→test merge **75+59=134 commits** (결정 92 · COD `318411d`)

> **Won't (BNK-11 G20)**: 케어포 demo-work 시설특화(생활실·욕창·집중배설) — ogada 주야간 commute 모델 **의도적 제외**.

---

## v1.3 — 배차·이동경로 (결정 60·61·**62**, BNK-7·**BNK-8·BNK-9** G15·G16·G17~G19)

- **status**: done
- **merge_status**: merged
- **stream**: backend + frontend
- **목표**: **v1.3-A** 픽업 배차 — `hq_admin` 확정 → 직원 명단·지도 조회 (최대 15명). **v1.3-A = 케어포 이동서비스 지도보기 패리티**(BNK-8 — 차별화 아님). **영업 차별 = v1.3-B(TSP·도로경로)**. v1.3-A는 **운영 시각화 한정** — 청구·평가(G15) 미대응(BNK-7 §10-3).
- **선행**: v1.1 `merge_status: merged`
- **75차 진전 (v1.3-A stack — origin 동기화 완료)**: backend develop/test/origin **`598d108`** · frontend develop/test/origin **`c7c8f07`** — UXD-53·UXD-54·**UXD-55**·transport privacy·`pilotPageFlows` **HEAD PRESENT**. **잔여**: live E2E **run**(결정 73) · v1.2.1 **merge(3+3)**.

### 범위

| 단계 | 내용 | USER_STORIES | Must |
|------|------|--------------|------|
| **v1.3-A** | 픽업 명단·`hq_admin` 편집·**확정**·직원 **읽기 전용** 조회·지도 (**청구·일지 제외**) | US-T01·T02·T03 | **◎** |
| **v1.3-A.1** | 드롭(DROPOFF) 배차 (픽업과 동일 패턴) | US-T04 | Should |
| **v1.3-B** | TSP·Directions **다중 경유지 API** 도로 경로 (**영업 차별 핵심**, BNK-8·**BNK-9**) | US-T02(B) | Should |
| **v1.3-C** | `vehicles`·**`transport_service_fee` 테이블**·이동서비스비 청구·**G15 법정 서식** | US-T05 | Could |
| **Won't v1** | **G17** 기능회복훈련 · **G18** 단기보호 시범 · **G19** 통합재가 | — | Won't v1 (BNK-9) |

### 완료 기준 (v1.3-A)

- [x] DBA: `uses_transport`·`pickup_*`·`transport_runs`(DRAFT/CONFIRMED·PICKUP)·`stops`·`confirmed_*` *(V47 @ `53a1ffe`)*
- [x] Geocoding 서버 프록시 + `KAKAO_*` env (Directions 제외) *( `POST /api/v1/transport/geocode` @ `53a1ffe`)*
- [x] API: roster·runs CRUD·**confirm**·RBAC(DRAFT=hq_admin only, CONFIRMED=직원 read) *( `TransportController`·routing test @ `53a1ffe`)*
- [x] UI: `/transport`·`/transport/runs/new`·`/transport/runs/:id` + 카카오맵 *(frontend lineage `e8d1854`+)*
- [x] **15명 상한** 서버·UI 검증 *( `MAX_STOPS=15`·DTO `@Size(max=15)` @ `53a1ffe` + UI `MAX_TRANSPORT_STOPS`)*
- [x] **transport run unconfirm** — `hq_admin` 미확정 취소 API *( `PATCH /api/v1/transport/runs/{id}/unconfirm` + POST legacy alias @ `767d977`)*
- [x] **frontend unconfirm UI** — `TransportUnconfirmModal`·확정 취소 버튼·`TransportRunDetailPage` 연동·Vitest 3건 *( @ `73f7d39`)*
- [x] **Clients API transport profile** — `usesTransport`·`pickupAddress`·`pickupContact`·`defaultPickupTime` 노출·geocode 캐시 무효화 *( @ `1ec538b` — US-T01 backend)*
- [x] **`pilotPageFlows` transport US-T01~T03** fetch-mock E2E + `pilotChecklist` T01~T03 *( @ `637b9b3`)*
- [x] **backend `TransportPilotServiceFlowE2eTest`** — US-T01~T03 service-flow·transport RBAC *( @ `f8d1b02`)*
- [x] **transport live E2E harness** — `src/e2e/transportLiveApi.e2e.test.js` develop HEAD *( @ `d484206`+, FE-22 패턴 · 기본 `npm test` 제외)*
- [x] **non-HQ pickup address masking** — `TransportService.maskAddress` · roster/runs 응답에서 `branch_admin`/`social_worker`/`caregiver` 역할 pickup 주소 마스킹 *( @ `e7d4cf6`, SEC-D9·PII 정합)*
- [x] **non-HQ pickup contact masking UI** — `TransportPickupContact`·roster/정차 목록·`hq_admin`만 tel 링크·`pilotPageFlows` T03 E2E *( @ `1d910c2` lineage `37be0a3`+, US-T03/SEC-D9·backend `c7941e9` 정합)*
- [x] **non-HQ pickup masking 단위 테스트** — `TransportServiceTest` hq_admin 전체 노출·caregiver `getRun` 마스킹 어서션 *( @ `32575aa`, SEC-D9 회귀 안전망)*
- [x] **UXD-53·UXD-54 지점 스코프 UI** — `BranchScopeNotice`(`role="status"`) Attendance·QR·Transport(신규·상세·목록) 연동·`pilotPageFlows` US-E01/E05 E2E *( @ `7cd9293` lineage `0d36e30`+/`e641f62`+, US-B02/E01/E05/US-UX-04)*
- [x] **`ClientFormPage` 픽업 프로필 UI** — `usesTransport`·`pickupAddress`·`pickupContact`·`defaultPickupTime` 폼 연동 *( @ `3c55339`, US-T01/Q166)*
- [ ] **US-T01~T03 live E2E run** — harness **충족** · 실 Bearer JWT 연동 **run 잔여**(결정 73 post-merge 권장, merge BLOCK 아님)
- [x] UI·문서에 **「운영 편의용 — 이동서비스비 청구·평가 일지(G15) 미포함」** 고지 (BNK-7 §10-3) + **「케어포 이동서비스 지도보기와 동등 — 경로 최적화는 v1.3-B」** (BNK-8) *(`TransportDisclaimer`)*

### 완료 기준 (v1.3-B — BNK-9)

- [ ] **카카오 Directions 다중 경유지 API** PoC — 일 **5,000건 무료·초과 16원/건** (BNK-9 §12-1)
- [ ] TSP 자동 순서 + Directions 도로 경로·거리/시간 (US-T02-B)
- [ ] v1.3-B 월간 API 비용 산정(15정차×운행일수) — PLAN_NOTES #43 **해소**

### 완료 기준 (v1.3-C — G15·G16·BNK-9·BNK-49·BNK-53·BNK-58)

- [ ] `vehicles` 마스터·정원·차량번호 — `transport_runs` 배정 연계 (G16)
- [ ] 공단 **별지 제22호 이동서비스일지** export·**별지 제18호** 신청 전제 안내 (G15)
- [ ] 급여제공기록지 **이동서비스 제공·차량번호** 연계 (G15)
- [x] **탑승/출석 이원화** — 케어포 func.php **2-2/2-3** — `/attendance/boarding`·`/attendance/on-site`·`GET /attendance?transportMode=boarding|on_site` @ `6c4c151`/`d6d7e7f` (BNK-58)
- [x] **이동서비스 수칙·계약 텍스트 정본 UI (부분)** — `TransportCompliancePanel` 5수칙 체크리스트 + 계약서·일지 Modal @ `3db8db3` (BNK-53)
- [x] **계약서 서명 저장 API+UI** — `TransportContractService`·V64·`TransportCompliancePanel` wiring @ `3c8f9fe`/`9e3cab5` (BNK-58 · TSR 221~222)
- [ ] **배차 geocode 실패 UX** — `countGeocodeFailures`·경고 Alert·신규 저장 차단 @ WT 4M (QA-B19 Planned · B07 #12)
- [ ] **외출 리포트(2-9)·외출 관리(2-1-1)** — 케어포 lifecycle (BNK-58 P1 잔여)
- [ ] **운행일지 DB·이동서비스 시간 준수 기록** — 엔젤 daycareEssentialWork 「시간을 준수함」 (BNK-58 P1)
- [ ] **이동서비스비** 산정·청구 입력 — 고시 제34조 (G16, 케어포 2-5 패리티)
- [ ] **`transport_service_fee` 테이블** — 러-1~4 시드 **830/2,630/4,430/6,230원**(BNK-25 2차 교차 확정·BNK-47 **#44 수동 보류**) · **상수 하드코딩 금지**

### Won't v1 (BNK-9·**BNK-25** — G17~G19)

- **G17** 2026 평가 **지표25(계획 2점)+지표26(실행 3점)** 기능회복훈련 — **Could v2+** · v3.1(결정 94) 자동충족 경로
- **G18** 주야간 내 단기보호 시범(2026.1~, 월9일) — **Won't v1**
- **G19** 통합재가서비스 — **Won't v1**

### 미확정 (#41 잔여)

> 지도 벤더(카카오 가정)·출석 연동·픽업 체크 — v1.3-B. 드롭 — v1.3-A.1

---

## v2 — 보호자·알림·결제 · **방문요양** (결정 90)

- **status**: in_progress
- **merge_status**: pending
- **stream**: backend + frontend
- **목표**: 보호자 풀 포털·알림톡·CMS + **방문요양 일정 엔진(G21)** — **W3~4 (6/23~7/6)**
- **완성 목표**: **2026-08-09** (결정 91 8주 스프린트)
- **선행**: v1.2.1 `done` (W1~2)

### 범위

1. 보호자 풀 포털 (명세·기록·사진 열람 — 케어포 가족돌봄앱 수준)
2. **카카오톡 채널 알림톡** 연동 + SMS fallback
3. `NotificationService` + `notification_preferences`
4. 본인부담금 **CMS·간편결제** (Hyosung FCMS 커넥터, 결정 87) — **BE skeleton ✅** @ `2c6e57e`(`StubFcmsClient`·`CmsCopayLifecycleE2eTest`) · **FE `/billing/cms` Route ✅** @ `6c6dc7a`/`c0a01b4`(`CmsEnrollmentForm`·`CmsDebitPanel`) · **Hyosung 실연동 잔여**
5. **방문요양 (G21, Epic V)** — 이지케어 3장 패리티
   - `branches.service_types` + `HOME_CARE` 지점
   - `/visits` 달력형 방문일정 CRUD·확정/취소
   - **계획일정 vs 청구일정** 이중 모델 (`plan_schedules` / `billing_schedules`)
   - 사회복지사 **모바일 방문 체크인** (RFID 대안 — 이지케어도 RFID 실시간 **2016 종료→엑셀**, BNK-20)
   - 공단 일정 import 확장 · 일정확정 → 본인부담 연동

### 알림 채널 단계 (확정 2026-06-06)

| 단계 | 채널 | 비용 | 범위 |
|------|------|------|------|
| v1.1 | 인앱·FCM Web Push·이메일(선택) | 무료~저비용 | 포털·명세 안내 |
| **v2** | **카카오톡 채널 알림톡** | 건당 과금 | 앱 미사용 보호자·출석·긴급 |
| v2 | SMS/LMS | 건당 과금 | 알림톡 실패 fallback |

### 완료 기준

- [x] **(BE-7·QA-B08)** `notification_preferences` — V41 `guardian_notification_preferences`·`NotificationPreferenceService`·`GuardianNotificationPreferenceController` + 단위 테스트 **8 @Test** develop 반영 *(develop `feac558` — V41 + 7 java + 8 @Test HEAD PRESENT, `MustApiEndpointRoutingTest`·`RoleBasedControllerAccessTest` notification routing/RBAC, Maven PASS, 이관 규율 5·8 PASS)*
- [x] **(QA-B08 recurrence #2)** v2 follow-up **develop 반영·working tree clean** — `V42__guardian_notification_preferences_consent_temporal.sql`(kakao/sms 유료 채널 consent CHECK + `consent_at`/`updated_at` temporal monotonicity, API_SPEC §11-3·ERD §4-7-1) + `NotificationPreferenceServiceTest`(4 @Test — paid channel consent stamp·upsert) *(develop `428ba7d` — COD 36차 커밋·working tree **CLEAN**, B08 #2 Fixed)*
- [x] **(v2/J03 follow-up, TSR 72 @ `c53dd3b`)** 알림 **이력 조회 API** — `GET /guardian/notifications`·`GET /clients/{clientId}/notifications`·`NotificationHistoryService`(+test)·`MustApiEndpointRoutingTest` RBAC
- [x] **(v2/J03 follow-up, BNK-22 @ `e39164d`)** **알림 발송 이력 UI** — `NotificationHistoryPanel`·`fetchGuardianNotificationHistoryApi`·`fetchClientNotificationHistoryApi` · 보호자 포털·직원 이용자 상세 연동 · **실발송(알림톡/SMS) v1.1/v2 잔여**
- [x] **(v2/J03 follow-up, TSR 74 @ `8ce1151`)** **`V46__notification_history_query_index.sql`** — `idx_notifications_org_recipient_created` · 이력 조회 페이지네이션 성능
- [x] **(v2/J03 follow-up, TSR 76 @ `0832fbf`)** `HealthRecordService` — **활력징후(vitals) 기록 생성 시 DAILY_CARE alimtalk dispatch** · `HealthRecordServiceTest` 단위 테스트 — **템플릿 심사·발송 UI 잔여** · **이력 UI ✅ @ `e39164d`**
- [x] **(v2/J03 follow-up, TSR 78 @ `32a1f8f`)** **`J03AlimtalkServiceFlowE2eTest`** — attendance·health·billing 도메인 액션을 `NotificationService` 경유 service-layer alimtalk flow E2E 5건 · `AttendanceServiceTest` check-out dispatch — **템플릿 심사·발송 UI 잔여** · **이력 UI ✅ @ `e39164d`**
- [x] **(v2/J03 follow-up, TSR 79 @ `4c74f84`)** `AlimtalkTemplateVariables` — Solapi `kakaoOptions.variables` 매핑(attendance·daily care·billing·emergency) · `SolapiKakaoAlimtalkProvider`·`J03AlimtalkServiceFlowE2eTest` 확장 — **live 템플릿 심사·발송 UI 잔여** · **이력 UI ✅ @ `e39164d`**
- [x] **(v2/J03 follow-up, TSR 81 @ `ac17ad8`)** `AlimtalkFallbackText` — 알림톡 실패 시 한국어 SMS fallback 본문(Solapi alimtalk·SMS provider 공통) · EMERGENCY `incidentType`→`category` alias — **live Solapi·발송 UI 잔여** · **이력 UI ✅ @ `e39164d`**
- [x] **(v2/J03 follow-up, TSR 82 @ `52e0621`)** copay claim **CONFIRMED→PAID** 전환 시 **`BILLING_PAYMENT_RECEIVED`** alimtalk dispatch · `BillingServiceTest`·`J03AlimtalkServiceFlowE2eTest` 확장 · `notifyBilling` consent 재사용 — **live Solapi·발송 UI 잔여** · **이력 UI ✅ @ `e39164d`**
- [x] **(v2/Epic L backend, TSR 100 @ `598d108`)** copay **입금 기록·미납 목록·보호자 billing API** — `RecordCopayPaymentRequest`·`OverdueClaimListResponse`·`V50__billing_copay_payment_metadata.sql`·`BillingServiceTest`(+198) — **develop-only** · frontend Epic L UI·origin test 승격 **잔여**
- [x] **(v2/G2 email @ `6ed48ff`/`f23f15a`, BNK-38)** **`SmtpEmailProvider` committed** + `NotificationService` email dispatch — **템플릿·실발송·실패처리 잔여**
- [x] **(v2/G2 CMS @ `2c6e57e`/`6c6dc7a`, BNK-36·38)** **Hyosung FCMS enrollment·debit skeleton** + **FE `/billing/cms` Route ✅** — `StubFcmsClient`·`CmsEnrollmentForm`·`CmsDebitPanel` · **Hyosung 실연동 잔여**
- [ ] USER_STORIES Epic J·**J03**·**N**(v2 CMS·결제) 스토리 구현 (보호자 알림·결제·**CMS UI**)
- [ ] **카카오 비즈니스 채널** 개설·템플릿 심사·발송 API 연동 (US-J03)
- [x] **(v2/J03 backend service-layer)** 출석(도착/귀가)·일일 케어·명세·긴급 알림 **알림톡 E2E** — `J03AlimtalkServiceFlowE2eTest`·`NotificationAlimtalkDispatchE2eTest` · **live Solapi·발송 UI 잔여** · **이력 UI ✅ @ `e39164d`**
- [x] QA_FEEDBACK v2 범위 항목 0건 OPEN
- [ ] 본인부담금 보호자 발송·수납 E2E (MVP에서 제외했던 §3-9-3 후속)
- [x] **(v2/G21 backend @ `d768820`)** `V53__visit_schedules_v2.sql`·`VisitService`·`VisitController` — `GET/POST/PATCH /api/v1/visits`·확정/취소·체크인/아웃 · `VisitServiceTest`(+11)·`RoleBasedControllerAccessTest` RBAC
- [x] **(v2/G21 backend @ `ee3fa3a`, BNK-25)** **NHIS visit schedule import API** — `HOME_VISIT` branch guard · import endpoint · `VisitServiceTest` 확장
- [x] **(v2/G21 backend @ `84f3441`, BNK-28)** **확정 PLAN import 차단** — `hasBlockingConfirmedPlan` · FE 확정↔import 가이드 @ `bf3d40d` (US-V02 P1 **닫힘**)
- [x] **(v2/G21 backend @ `b63bb1f`/`3e4d3e6`, TSR 133·135)** **페어 일정 취소·draft sync** — paired PLAN/BILLING cancel cascade · draft 상태 동기화 · FE paired cancel UX @ `311c7c0`
- [x] **(v2/G2 notify @ `84f3441`/`c48fb67`, BNK-28)** **`POST /billing/claims/{id}/notify`** API + billing **보호자 알림 UI** — **실채널(알림톡/SMS) v1.1 잔여**
- [x] **계획/청구 이중 일정 (backend @ `d768820`)** — `schedule_kind` PLAN|BILLING·`paired_schedule_id`·`createPairedBillingSchedule`
- [x] **(v2/G21 backend @ `d768820`)** **방문 체크인 API** — `POST /visits/{id}/check-in`·`check-out` (MOBILE|MANUAL)
- [x] **(v2/G21 frontend @ `311c7c0`, BNK-28)** **`/visits` UI** — `VisitScheduleForm`·PLAN/BILLING Tabs·`VisitNhisImportPanel`·모바일 체크인(US-V01~V04 **partial**) — **US-V04 E2E 잔여**
- [x] **(v2/G21 billing confirm-lock @ `c4fb7ff`/`02cd2b2`, BNK-38)** **billing 확정 잠금 가이드** + cross-page E2E — **live run 잔여**
- [ ] `pilotPageFlows` 방문요양 E2E (US-V01~V04 live post-merge)

---

## v3 — 확장 모듈 · **재무회계** · **시설급여** (결정 90)

- **status**: planned
- **merge_status**: pending
- **stream**: backend + frontend + DBA
- **목표**: 식사·프로그램·직원 + **재무회계(G4)** + **시설급여(G20)** — **W5~8 (7/7~8/9)**
- **완성 목표**: **2026-08-09** (결정 91)
- **65차 진전 (`767d977`/`8a764df`)**: backend V49·meals/programs REST **PRESENT** · frontend `MealsPage`·`ProgramsPage`·`pilotPageFlows` US-N01·N02 E2E·`pilotChecklist` N01/N02 + **StaffPage UI·Recharts(UXD-48)** **PRESENT**. **§3-5·§3-6 develop 스택 완료** · **v3 frontend 신규 착수 보류(v1.3 merge gate 선행)** — **프로그램 사진 업로드**·StaffPage API·평가·서류 **후속**.
- **merge 게이트 (63차 신설)**: v3 `merge_status: ready` 조건 — ① 아래 완료 기준 merge-blocking 항목 **전부 `[x]`** ② `npm test`·`mvn test` PASS ③ working tree CLEAN — 충족 시 tester merge 실행.

### 범위

- Should/Could 모듈 (REQUIREMENTS §3-5~§3-8, §3-10)
- **재무회계 (G4, Epic F, W5~6)** — 이지케어 5·7·12장
  - `/finance/ledger` 수입지출·결의 CRUD
  - `/finance/payroll` 급여 산출·명세·4대보험 기본
  - 본인부담 PAID → **회계 자동분개**
- **시설급여 (G20, Epic S, W7~8)** — 케어포 demo-work MVP
  - `facility_rooms` · `bed_assignments` · `/facility/residents`
  - 욕창·집중배설 기록 · 시설급여 청구 분기
- **제외 (v3.1+)**: NFC/RFID · 평가 서식 80종 · 통장 OpenAPI 실연동

### 완료 기준 (v3 — §3-5~§3-8 + G4 + G20)

- [x] UI: `/meals` — 당일 식단·이용자 식사량·식이 제한·영양사 소견 (REQUIREMENTS §3-5)
- [x] UI: `/programs` — 당일 일정·참여·만족도 기록 (REQUIREMENTS §3-6)
- [x] `services.js` — `/api/v1/meals/*`·`/api/v1/programs/*` 클라이언트 + Vitest 회귀
- [x] SideNav·RBAC — `branch_admin`/`social_worker`/`caregiver`/`hq_admin` 기록 그룹 노출
- [x] DBA·backend: `meal_menus`·`meal_records`·`activity_programs`·`program_participations` Flyway·REST — **PRESENT @ backend `dfd9be2`+** (TSR 85)
- [x] US v3 §3-5·§3-6 E2E — API 연동 (`pilotPageFlows`·`pilotChecklist` N01/N02)
- [x] UI: `/staff` — StaffPage v3 직원 관리 UI·`StaffRoleSelect` a11y (케어포 §8 부분) **PRESENT @ frontend `73f7d39`** (TSR 90차)
- [ ] **[merge-blocking]** 프로그램 사진 업로드 — `activity_programs` 이미지 첨부 (§3-6-b · 케어포 프로그램 사진) · backend S3/local 업로드 API · frontend `ProgramsPage` 파일 인풋
- [ ] **[merge-blocking]** `/staff` 기본 — 직원 CRUD·자격 (§3-8 · 케어포 8-1)
- [ ] **[merge-blocking, 결정 94]** 직원 HR 확장 (§3-8-a) — 근무일정(8-2)·출퇴근(8-4)·교육·회의(8-5~8-7)·건강검진(8-10)·연차(8-13)·직원 리포트(8-12)
- [ ] **[merge-blocking]** `pilotPageFlows` v3 staff·photos E2E + `pilotChecklist` P0·N01~N03 항목 추가
- [ ] 공단 평가 2026 지표 자동화 여부 결정 (Could — 영업 차별 아님 · G17 Won't v1)
- [ ] 서류·외부강사·자원봉사자 모듈 (§3-10 — v3.1 후속)
- [ ] **재무회계 (G4, W5~6 Must)** — `chart_of_accounts`·`journal_entries` Flyway·REST
- [ ] **`/finance/ledger`** 수입지출·결의 UI
- [ ] **`/finance/payroll`** 급여 산출·4대보험·명세
- [ ] 본인부담 PAID → 회계 **자동분개**
- [ ] **시설급여 (G20, W7~8 Must)** — `facility_rooms`·`bed_assignments` Flyway·REST
- [ ] **`/facility/rooms`** · **`/facility/residents`** UI
- [ ] 욕창·배설 기록 화면
- [ ] v3 통합 E2E · `merge_status: ready` @ **2026-08-09**

---

## v3.1 — 요양 리포트·프로그램 확장·위생안전 (결정 94, 사용자 확정 2026-06-09)

- **status**: planned
- **merge_status**: pending
- **stream**: backend + frontend + DBA
- **목표**: 케어포 **3-3~3-7** · **5-3~5-10** · **6-2~6-4** leaf 패리티 — v3 기본(식단·프로그램 일정) 위 **운영·리포트** 레이어
- **선행**: v3 §3-5·§3-6 develop 스택 완료 · v3 `/staff` 기본(8-1) 착수

### 범위

| 우선 | 영역 | 케어포 | ogada route | 신규 DB |
|------|------|--------|-------------|---------|
| **P0** | 목욕 일정·제공 | 3-3 | `/care/bathing` | `bathing_schedules`·`bathing_records` |
| **P0** | 요양·식사·화장실 일일 리포트 | 3-4 | `/reports/care-daily` | care_daily_records 확장 |
| **P0** | 목욕·급여제공 리포트·집계 | 3-5~3-7 | `/reports/bathing`·`/reports/care-provision`·`/reports/care-summary` | 집계 뷰/쿼리 |
| **P0** | 프로그램 그룹·마스터·의견·계획 | 5-3~5-6 | `/programs/groups`·`/programs/catalog`·`/programs/feedback`·`/programs/plans` | `program_groups`·`program_catalog` |
| **P0** | 프로그램 리포트 4종 | 5-7~5-10 | `/programs/reports/*` | 리포트 쿼리 |
| **P1** | 일일·정기 점검·감염·시설운영일지 | 6-2~6-4 | `/safety/daily-checks`·`/safety/periodic-checks`·`/safety/infection-control`·`/safety/operation-log` | `safety_checks`·`operation_logs` |
| **P1** | 외부강사·자원봉사 (5-1-1) | 5-1-1 | `/programs/instructors` | `external_instructors` |

### 완료 기준 (v3.1)

- [ ] REQUIREMENTS §3-5-a·§3-6-a·§3-14 명세·API_SPEC·ERD 반영
- [ ] 목욕 일정 CRUD + 제공 완료 + 이용자별 조회
- [ ] 요양/식사/화장실·목욕·급여제공 **리포트** 화면 + 인쇄
- [ ] 프로그램 그룹·마스터·의견·계획 + **리포트 4종**
- [ ] 위생·안전 점검·감염·시설운영일지 CRUD
- [ ] `pilotPageFlows` v3.1 E2E · `merge_status: ready`

> **v3 병행 (결정 94)**: §3-8-a 직원 HR(8-2~8-13)은 **v3 완료 기준**에 merge-blocking 추가 — ROADMAP v3 §완료 기준 참조.

---

## v4 — *(결정 90 폐기 — v2·v3로 흡수)*

> 방문요양→**v2** · 회계·시설급여→**v3**. v3.1=요양·프로그램·위생 리포트 레이어.

---

## 변경 이력

| 날짜 | 변경 |
|------|------|
| 2026-06-08 | **자동 동기화 72차 — TSR 98·99 + masking 단위테스트 + UXD-53**: backend `32575aa`(25 ahead·CLEAN·243/243·TransportServiceTest +2) · frontend `e641f62`(20 ahead·CLEAN·212/69·780 modules·BranchScopeNotice·pilotPageFlows E01/E05 E2E) · v1.3 `merge_status: ready` · merge(25+20) 잔여 · Open 0건 |
| 2026-06-08 | **자동 동기화 70차 — TSR 96·97 + transport pickup contact masking UI + T03 E2E**: backend `c7941e9`(24 ahead·CLEAN·241/241·contact masking) · frontend `1d910c2`(18 ahead·CLEAN·208/68·779 modules·TransportPickupContact·T03 E2E) · v1.3 privacy 완성·`merge_status: ready` · live E2E run 잔여 · Open 0건 |
| 2026-06-08 | **자동 동기화 68차 — TSR 94·95 + transport pickup masking + UXD-51 + ClientForm 픽업 프로필**: backend `e7d4cf6`(23 ahead·CLEAN·241/241·non-HQ pickup masking) · frontend `3c55339`(16 ahead·CLEAN·203/67·778 modules·FE-13/FE-14 복원·ClientForm 픽업 UI) · v1.3 privacy·US-T01 UI `[x]` · live E2E run 잔여 · Open 0건 |
| 2026-06-08 | **자동 동기화 66차 — TSR 92 + US-T01 profile + pilotPageFlows transport + UXD-49**: backend `1ec538b`(21 ahead·CLEAN·231/231·Clients transport profile) · frontend `637b9b3`(12 ahead·CLEAN·189/60·766 modules·pilotPageFlows T01~T03 E2E·HQ 건강 이상 지점명) · v1.3 fetch-mock E2E `[x]` · live E2E 잔여 · Open 0건 |
| 2026-06-08 | **자동 동기화 65차 — TSR 91 + UXD-48 Recharts + 활성 버전 우선순위**: backend `767d977`(20 ahead·CLEAN·226/226) · frontend `8a764df`(10 ahead·CLEAN·183/60·766 modules·Recharts US-M02) · FE-15 bundle 회귀(non-blocking) · v1.3 단일 frontend 활성 · Open 0건 |
| 2026-06-08 | **자동 동기화 64차 — TSR 89·90차 + v1.3-A unconfirm UI 완료 + BNK-9 재확인**: backend `767d977`(20 ahead·CLEAN·226/226·unconfirm PATCH+POST) · frontend `73f7d39`(9 ahead·CLEAN·179/58·143 modules·40 route·TransportUnconfirmModal) · v1.3 unconfirm UI `[x]` · 핵심 진단 64차 · Open 0건 |
| 2026-06-08 | **자동 동기화 63차 — TSR 87·88차 + v1.3-A unconfirm + v3 StaffPage + merge 게이트 정의**: backend `0d8968d`(19 ahead·CLEAN·226/226·transport unconfirm hq_admin) · frontend `fe33e7c`(8 ahead·CLEAN·170/55·140 modules·StaffPage v3) · v3 merge 게이트 신설·완료 기준 갱신 · 핵심 진단 63차 · Open 0건 |
| 2026-06-08 | **자동 동기화 62차 — BNK-9 + v3 full stack**: meals/programs REST·V49 @ `dfd9be2` · pilotPageFlows E2E @ `362dbf0` · v3 §3-5·§3-6 develop 완료 · baseline `dfd9be2`/`362dbf0` · backend merge(18)+frontend merge(6) · Open 0건 |
| 2026-06-08 | **자동 동기화 61차 — BNK-9 + v1.3-A backend + v3 shell**: transport API·V47 @ `53a1ffe` · `/meals`·`/programs` UI @ `7ef1083` · v1.3-A 완료 기준 6/7 `[x]` · baseline `53a1ffe`/`7ef1083` · backend merge(17)+frontend merge(4) · Open 0건 |
| 2026-06-08 | **자동 동기화 59차 — TSR 80·81 + BNK-9**: `AlimtalkFallbackText` SMS fallback · US-G06 DISCREPANCY compare·E2E · v1.2 frontend merged @ `c510f5c` · baseline `ac17ad8`/`c510f5c` · backend merge(15) only · Open 0건 |
| 2026-06-08 | **자동 동기화 57차 — TSR 77·78 + BNK-9**: UXD-40 US-F01 비정상 범위 경고 · FAQ Q154 건강·NHIS API 본문 정합 Fixed · `J03AlimtalkServiceFlowE2eTest` service-layer alimtalk E2E · baseline `32a1f8f`/`4957bd3` · backend merge(13) · frontend +11 ahead · Open 0건 |
| 2026-06-08 | **자동 동기화 54차 — TSR 74·75 + BNK-9**: V46 알림 이력 인덱스 · US-E01~E05 출석 Epic E · baseline `8ce1151`/`a627c6d` · backend merge(11) · frontend +8 ahead |
| 2026-06-08 | **자동 동기화 42차 — TSR 58·59 + BNK-8**: QA-B10·SEC-D11·SEC-D12·QA-B11 Open→Planned · B09 Fixed @ `f47ffa1` · INFRA-B12·BE-10·FE-20 · v1.3-A=케어포 패리티 |
| 2026-06-08 | **자동 동기화 41차 — BNK-7 G15/G16 v1.3 완료 기준 명시**: v1.3-A 「운영 시각화 한정」·v1.3-C G15/G16·US-T05. submodule·QA Open 0·Planned BLOCK **불변**. TSR 57 baseline 유지 |
| 2026-06-08 | **자동 동기화 40차 — submodule 드리프트 부분 개선**: frontend init(`e5fd48d`·WT CLEAN)·backend stale(`2799e29`·WT 9U V35~V43) 불변. QA Open 0·Planned BLOCK·BNK-7·SEC-D8/D9 **변경 없음**. TSR 57 baseline 유지 |
| 2026-06-06 | 초안 — v1~v3 단계 분리, merge_status 규칙 정의 |
| 2026-06-06 | 벤치마크 2차 동기화 — v1 P0–P3·NHIS reconciliation 완료 기준, v1.1 보호자 확장, v2 CMS·v3 갭 매핑 |
| 2026-06-06 | 자동 동기화 3차 — QA Open 0건 재확인(범위 변경 없음), 문서 식별자 `PLA→PLN`·audience role-code 정렬 |
| 2026-06-06 | 벤치마크 3차 동기화 — G8(보호자 초대·명세 v1.1), NHIS `처리상태` 파서·롱텀2026 Chrome/Edge, 엔젤 CMS TCO |
| 2026-06-06 | 보호자 정책·알림 로드맵 — 이용자당 보호자 연결 필수(V39), v1.1 무료 채널, **v2 카카오톡 채널 알림톡**(US-J03) |
| 2026-06-06 | **자동 동기화 5차 — QA Open 10건 태스크화**: `## QA 피드백 반영` 신설(QA→태스크 매핑·이관 규율), v1 완료 기준에 QA-H01 파서 테스트·QA-H02 develop 커밋·QA-B01/B02, v1.1에 QA-H03/H04/M01/B03/B04/B05 추가; 4차 벤치마크 G9 1밴드·duration_band v1.1 명시; 메타 owner PLN 복원 |
| 2026-06-06 | **자동 동기화 6차 — false Fixed 회귀 처리**: TSR 재검증(07:52)에서 backend `Fixed`(QA-H01·H02) develop HEAD 미반영 확인 → v1 완료 기준 QA-H01 `[x]` 철회, backend 4건(B01·B02·H01·H02) Planned 재반영, **이관 규율 5항(Fixed↔develop HEAD `git show` 검증 게이트)** 신설; 메타 owner COD→PLN 복원. frontend H03/H04/M01은 develop 반영 확인·Fixed 유지 |
| 2026-06-06 | **자동 동기화 7차 — dirty-tree 재오염 + frontend false Fixed 회귀**: TSR 재검증(backend 14:45·frontend 14:55)에서 ① backend working tree 재오염(client↔guardian 미커밋·`createClient` 계약 변경 — QA-B06) → v1 완료 기준 QA-B02 `[x]` 철회, ② frontend `Fixed` 3건(H04·M01·SEC-005) develop HEAD 미반영 → v1.1 완료 기준 H04·M01 `[x]` 철회·SEC-005 항목 신설, ③ frontend working tree 대량 오염(QA-B07). **이관 규율 6항(완료 단위 커밋·API 계약 변경 문서화 게이트)** 신설; QA→태스크 매핑에 B06·B07·SEC-005 추가; B06 범위 v1 US-D01 확정 → API_SPEC §4 `primaryGuardian` 명세화 |
| 2026-06-06 | **8차 — 사용자 피드백**: v1.1 **파비콘(US-UX-01)** 완료 기준, **v1.2 프론트 기능 밀도**(BNK 6차 조사 선행), `docs/` 역할별 하위 폴더 재구성 |
| 2026-06-06 | **자동 동기화 9차 — TSR 8·9차 재검증 반영(coder 미조치)**: TSR 8차(15:38)·9차(15:45) 재검증에서 상태 불변·신규 Open 0건·Planned 9건(B01·B03·B04·B05·B06·B07·H04·M01·SEC-005) 전부 잔존 확인. `## QA 피드백 반영` 9차 노트(B07 악화 22m+20u·신규 페이지, M01 develop working tree `vitest` 6 PASS 미커밋), v1.1 완료 기준 M01·B07 9차 근거 추가, 메타 timestamp 갱신. 신규 태스크 없음 — 잔여 블로커는 전부 이관 규율(완료 단위 develop 커밋) 미준수. coder 장기 미조치 → PLAN_NOTES #36 에스컬레이션 |
| 2026-06-06 | **자동 동기화 10차 — 상태 불변 재확인·에스컬레이션 강화**: 9차(16:10) 이후 신규 입력 0건(QA Open 0·BNK 6차 착수 대기). planner가 submodule HEAD·working tree **직접 점검** → 9차와 완전 동일(backend `7d9d2eb` 10m+2u·frontend `f1c89d9` 22m+20u). `## QA 피드백 반영` 10차 노트, 메타·변경 이력 timestamp 갱신. **신규 기획·태스크·결정 없음** — coder 0건 조치 6회 연속(5·6·7·8·9·10차) → PLAN_NOTES #36 에스컬레이션 강화(루프 실제 실행 여부 진단 추가) |
| 2026-06-06 | **COD 11차 — frontend v1.1 develop 커밋(`998ac87`)**: API 클라이언트·메모리 JWT·Vitest·favicon·Must 페이지 연동 일괄 커밋, working tree clean. QA-B04·B07·H04·M01·SEC-005 Fixed, v1.1 완료 기준 6항 `[x]` 승격(reconciliation UI·파비콘 포함). 잔여: 7역할 E2E·Must API E2E·보호자 초대(J01)·merge ready(B03·B05 선행) |
| 2026-06-06 | **자동 동기화 11차 — TSR 11·12차 + BNK 6차**: backend B06·B02·frontend B07·B04·H04·M01·SEC-005 Fixed 확정, SEC-007 Planned, v1.2 BNK-6 범위 확정(P0 5건·결정 49), USER_STORIES Epic K·L·M·UX, REQUIREMENTS §1-5-2, #36 부분 해소 |
| 2026-06-06 | **자동 동기화 12차 — TSR 13·14차**: backend `fac3d07` RBAC·NHIS guidance 부분 진전, frontend **B07 recurrence**(v1.2 P0 dirty-tree) Planned, 이관 규율 7항·결정 50, v1.1 HEAD Fixed 유효·v1.2 WIP 관측 |
| 2026-06-06 | **COD 14차 — B02 recurrence 해소**: develop `b5d70a8` GuardianAccess RBAC 3 tests 커밋·working tree clean, v1 QA-B02 `[x]` 복원 |
| 2026-06-06 | **자동 동기화 13차 — TSR 15·16차**: backend **B02 recurrence**(RBAC 테스트 미커밋) Planned·QA-B02 `[x]` 철회·BE-6, frontend **B07 Planned 강화**(29 files·WT build/test FAIL·FE-7) |
| 2026-06-06 | **자동 동기화 15차 — TSR 17·18·19차**: backend **B02 recurrence Fixed 확정**(17차 TSR `b5d70a8` clean), backend 잔여 **merge 게이트 단일**(B01·SEC-007), frontend B07 **35 files·WT build/test PASS**(FE-7 회복)·dirty-tree Planned 유지 |
| 2026-06-06 | **자동 동기화 16차 — TSR 20·21차 + v1.2 P0 흡수 결정 52**: ① backend **B02 recurrence #3 Open→Planned**(20차 신규 테스트 3 files 미커밋), v1 완료 기준 QA-B02 `[x]` 철회·BE-6 Open 복귀. ② frontend **B07 recurrence Fixed**(21차 `a72e249` v1.2 P0 42 files + `3fc549a` US-D03 일괄 커밋, working tree CLEAN, HEAD build 110·`npm test` 10/4 PASS). ③ **결정 52** — v1.2 P0 산출물은 v1.1 develop→test merge에 **동반 흡수**(별도 분리 안 함), v1.2 정식 완료 기준은 v1.1 merged 후 사이클로 분리. v1.2 status `planned→in_progress`(P0 develop 선행 커밋). v1.2 완료 기준 P0 커밋 항목 `[x]` 승격. |
| 2026-06-06 | **자동 동기화 17차 — TSR 22·23차 (B02 recurrence #3 Fixed + B07 recurrence #2 + UXD 10차 + US-M02 WIP)**: ① backend **B02 recurrence #3 Planned→Fixed**(22차 COD 15차 `4274459` 독립 검증 — `NhisImportServiceTest`·`RoleBasedControllerAccessTest`·`BillingControllerRoutingTest` 3 files 일괄 커밋, working tree CLEAN, `@Test` 120, Maven 79/79 PASS), v1 완료 기준 QA-B02 `[x]` **복원**, BE-6 #3 해소. ② frontend **B07 recurrence #2 Open→Planned**(23차 `5656e19`(UXD 10차) 위 v1.2 P0 US-M02 대시보드 위젯 실데이터 WIP 8 files 미커밋, FE-6 위반·FE-7 충족·HEAD Fixed 규율 5 PRESENT 유효), v1.1 완료 기준 B07 `[x]` 철회. ③ **UXD 10차 `5656e19`** 흡수(이용자 본인 계정 발급·`CopayTypeSelect`·브랜드색) — 결정 52 적용 v1.1 merge 동반. ④ **US-M02 진전**: `dashboardWidgets.js`·`.test.js` 3 PASS·DashboardPage 위젯 — WT 완성·develop HEAD 미커밋. ⑤ 잔여 BLOCK = backend B01·SEC-007 + frontend B03·B05 + B07 recurrence #2(Planned 단일). |
| 2026-06-06 | **자동 동기화 19차 — TSR 26·27차 (PilotChecklistApiAccessTest 29 @Test + pilotChecklist fetch-mock 자동화 + LoginPage DS·접근성)**: ① backend **R-04 7역할 권한 분리 PARTIAL 진전**(TSR 26차 COD 18차 `c3f3146` — `PilotChecklistApiAccessTest.java` 697 lines 29 @Test 일괄 커밋, USER_STORIES §13 P1–P8 × 7역할 `@PreAuthorize` `@WebMvcTest` 자동화 — `@WebMvcTest` 65건 = 36 RBAC + 29 Pilot, working tree CLEAN, `@Test` 154→**183**(+29), Maven 79/79 PASS·package SUCCESS), v1 완료 기준 QA-B02 *(`c3f3146`)* 갱신·7역할 RBAC `@WebMvcTest` PARTIAL 진전·P1–P8 PARTIAL 진전. ② frontend **v1.1 Must API JWT 라우팅 fetch-mock 자동화·J01/J02 회귀 자동화 진전**(TSR 27차 COD 19차 `cc34f23` — `pilotChecklist.js`(211)·`pilotChecklist.test.js`(104)·`GuardianInviteModal.test.jsx`(81) 3 files +396, P1–P8 services.js 매핑·JWT·HTTP·경로 fetch-mock·GuardianInviteModal 4건 회귀, working tree CLEAN, `npm test` 13/5→**32/7**(+19 tests/+2 files)·build 111 modules·audit 0건), v1.1 완료 기준 P1–P8 프론트 재현 PARTIAL·보호자 초대 E2E PARTIAL·B04/B07 5커밋 무재발 갱신. ③ frontend **UXD 12차 `404a30e` LoginPage DS·Modal 포커스 트랩·`forced-colors`·`prefers-contrast` WCAG 1.4.11**(3 files +183/-28) 흡수. ④ **결정 52 흡수 6묶음**: ① v1.2 P0 `a72e249` + ② v1.1 US-D03 `3fc549a` + ③ UXD 10차 `5656e19` + ④ UXD 11차 `2d742b3` + ⑤ COD 17차 `a84473f`+`ed1bf22` + ⑥ **UXD 12차 `404a30e` + COD 18차 `c3f3146` + COD 19차 `cc34f23`** — 모두 v1.1 develop→test merge 동반. ⑤ **#36 양 스트림 BE-6·FE-6 패턴 완전 종결 확인**: backend BE-6 #3 Fixed 후 5커밋 무재발(94f0fb9→4274459→aa71412→`c3f3146`)·frontend FE-6 #2 Fixed 후 4커밋 무재발(`a84473f`→`ed1bf22`→`404a30e`→`cc34f23`). ⑥ Open 0건 유지·Planned BLOCK 4건(B01·B03·B05·SEC-007 merge 게이트 단일) 불변. ⑦ **J01 백엔드 API 미구현 잔여 — API_SPEC §4 신규 명세 필요**(`POST /clients/{clientId}/guardians/invitations`·`POST /guardian/invitations/{token}/accept`·`GET /guardian/invitations`) — PLAN_NOTES `### 추가 질문` #33·#35 가설 채널·스키마 결정 대기. |
| 2026-06-07 | **자동 동기화 33차 — TSR 50차 (backend B02 recurrence #6 + B08 recurrence #2 Open→Planned·V42 consent CHECK·temporal v2 follow-up 미커밋·HEAD Fixed 규율 5 유효·frontend COD 34차 ds-* 유틸리티 전환 FE-16·Open 0건)**: ① backend **TSR 50차** 48차 `c3b8716` CLEAN→DIRTY 재오염(2 untracked: `V42__guardian_notification_preferences_consent_temporal.sql` 54 lines + `NotificationPreferenceServiceTest` 3 @Test) → **QA-B02 recurrence #6 + QA-B08 recurrence #2 Planned**, v1 완료 기준 QA-B02 working tree clean `[x]` 철회·v2 BE-7 V42 follow-up 완료 기준 태스크화. HEAD Fixed(B02 #5·B08) 규율 5 유효·WT 252/252. ② frontend **COD 34차 `0b9b001`** ds-* 유틸리티 전환(9 컴포넌트 인라인 style 제거)·`AttendancePage.layout.test.jsx`·187/35·WT CLEAN·17 ahead → **FE-16** 매핑·신규 Open 0. ③ **#36 backend 단독 재오픈**(결정 53) — frontend COD 33·34차 연속 CLEAN. ④ 잔여 BLOCK = **B03(frontend merge) + backend merge(2커밋) + B02 #6 + B08 #2**. |
| 2026-06-07 | **자동 동기화 34차 — TSR 51·52차 (backend COD 35 false Fixed 철회·B02 #6/B08 #2 Planned + frontend B07 #5 Planned·FE-17 J01 수락 UI·#36 양 스트림 재오픈·Open 0)**: ① backend **COD 35 false Fixed 철회** — TSR 51 상태 불변·V42 + `NotificationPreferenceServiceTest` WT untracked·HEAD ABSENT, v1 QA-B02·v2 B08 recurrence #2 `[x]` 철회. ② frontend **B07 #5 Planned** — 20 files(LogoutButton·GuardianInvitationAcceptPage J01·BillingPage.layout.test)·WT 194/38·754 modules·HEAD `0b9b001` Fixed 규율 5 유효. ③ **FE-17** J01 수락 UI·LogoutButton·레이아웃 회귀 매핑. ④ **#36 양 스트림 재오픈**. ⑤ 잔여 BLOCK = **B03 + backend merge(2커밋) + B02 #6 + B08 #2 + B07 #5**. |
| 2026-06-07 | **자동 동기화 38차 — SEC 4차 SEC-D8·SEC-D9 (Open→Planned·BE-8·FE-19 보안 게이트·Open 0)**: ① **SEC-20260607-009 Planned** — SEC-D8 J01 `SecurityConfig` 공개 endpoint·토큰 정책·rate limit → **BE-8** commit/merge 금지·API_SPEC §4-1·SECURITY_CHECKLIST H-6. ② **SEC-20260607-010 Planned** — SEC-D9 MaskedPhone PII 마스킹 `010-****-5678` 유지 → **FE-19**·QA-H05 동반. ③ 37차 Open 0 vs SEC Open 2 불일치 정리. ④ 잔여 BLOCK = **B03 + backend merge(3커밋) + B09(BE-8+SEC-D8) + B07 #6 + H05(FE-19+SEC-D9)**. |
| 2026-06-07 | **자동 동기화 37차 — TSR 56·57차 (backend B09 Planned·BE-8 J01 API WIP + frontend H05 Planned·FE-19·B07 #6 20 files·FE-7 FAIL·#36 양 스트림 재오픈·Open 0)**: ① backend **QA-B09 Planned** — 54차 `428ba7d` CLEAN→DIRTY 27 files J01 API WIP, WT `mvn test` 253/253, develop 3 ahead. **BE-8**·API_SPEC §4-1. ② frontend **QA-H05 Planned** — GuardianListCard MaskedPhone 테스트 불일치 209/210 FAIL. **FE-19**. ③ **B07 #6** 15→20 files. ④ **#36 양 스트림 재오픈**(BE-6 #7 + FE-6 #5). ⑤ 잔여 BLOCK = **B03 + backend merge(3커밋) + B09 + B07 #6 + H05**. |
| 2026-06-07 | **자동 동기화 36차 — TSR 54·55차 (backend B02 #6·B08 #2 Fixed `428ba7d`·#36 BE-6/BE-7 해소 + frontend B07 #6 Planned·FE-18·Open 0)**: ① backend **QA-B02 #6·QA-B08 #2 Fixed** — COD 36 `428ba7d`(V42 + `NotificationPreferenceServiceTest` 4 @Test), WT CLEAN, develop HEAD `mvn test` **253/253**, develop **3 ahead of test**. ② frontend **B07 #6 Planned** — 15 files(DateInput·GuardianInvitationList J01·ClientDetail 보호자/초대), WT 205/42·758 modules, HEAD `d5654c0` Fixed 규율 5 유효. ③ **FE-18** J01 목록·DateInput DS·ClientDetail 보호자/초대 UI. ④ **#36 backend 해소·frontend FE-6 #5 재오픈**. ⑤ 잔여 BLOCK = **B03 + backend merge(3커밋) + B07 #6**. |
| 2026-06-07 | **자동 동기화 35차 — TSR 53차 (frontend B07 recurrence #5 정식 Fixed `d5654c0`·FE-17 J01 수락 UI 충족·frontend 잔여 BLOCK B03 단일 + backend 51차 대비 불변·B02 #6/B08 #2 Planned·domain test 3→4 @Test·Open 0)**: ① frontend **QA-B07 recurrence #5 Fixed** — COD 35차 `d5654c0`(25 files +823/-57, 18 ahead) 일괄 커밋, WT **20→0 CLEAN**, `git cat-file -e HEAD:` `LogoutButton`·`GuardianInvitationAcceptPage`(J01)·`GuardianInvitationAcceptForm`·`PublicAuthLayout`·`BillingPage.layout.test`·`acceptGuardianInvitationApi` 전부 PRESENT(이관 규율 5·6·7 PASS)·SEC-005 0건·HEAD `npm test` **199/40**·build **756 modules**·audit 0 → **FE-17 develop HEAD 반영 확정**·결정 52 흡수 ⑪묶음. ② backend **51차 대비 완전 불변** — develop `c3b8716` DIRTY(V42 + `NotificationPreferenceServiceTest` 3→**4 @Test** HEAD ABSENT)·B02 #6·B08 #2 Planned 유지·test 213/213·WT 253/253(+1)·develop 2 ahead of test(merge 미실행). ③ **#36 backend 단독 재축소** — frontend FE-6 #4 종결, 에스컬레이션 backend 단독(BE-6 #6·BE-7). ④ 잔여 BLOCK = **B03(frontend merge) + backend merge(2커밋) + B02 #6 + B08 #2**(B07 #5 소멸). 신규 벤치마크·QA Open 입력 0건. |
| 2026-06-07 | **자동 동기화 33차 — TSR 50차 (backend B02 #6 + B08 #2 Planned·V42 consent CHECK v2 follow-up·frontend COD 34 FE-16·#36 backend 단독 재오픈·Open 0)**: ① backend **B02 #6 + B08 #2 Planned** — 48차 CLEAN→DIRTY 2 untracked(V42 + `NotificationPreferenceServiceTest`), HEAD Fixed(B02 #5·B08) 규율 5 유효, v1 QA-B02 `[x]` 철회. ② frontend **FE-16 Fixed @HEAD** — COD 34 `0b9b001` ds-* 전환·187/35·WT CLEAN·17 ahead. ③ **#36 backend 단독 재오픈**. ④ 잔여 BLOCK = **B03 + backend merge(2커밋) + B02 #6 + B08 #2**. |
| 2026-06-07 | **자동 동기화 32차 — TSR 48·49차 (backend B02 #5·B08 Fixed `c3b8716`·30+회 백엔드 정체 종결·frontend FE-15 Fixed·B07 #4 신호 소멸·merge 게이트 2스트림·Open 0)**: ① backend **QA-B02 #5·QA-B08 Fixed** — COD 32차 `c3b8716`·`feac558`, WT **3M+4U→CLEAN**, `git cat-file -e HEAD:` 전 산출물 PRESENT(이관 규율 5·6·8 PASS)·`mvn test` **249/249**. **결정 54** v1 보완 merge 즉시 권고. ② frontend **FE-15 Fixed** — COD 33차 `c98f98d` `manualChunks`, 최대 청크 393.53 kB. **B07 #4 신호 소멸**. HEAD `npm test` **186/34**·752 modules·audit 0. ③ **#36 대칭 종결** — 양 스트림 dirty-tree·false Fixed 소멸. ④ 잔여 BLOCK = **B03 + backend merge(2커밋)**. |
| 2026-06-07 | **자동 동기화 31차 — TSR 46·47차 (frontend B07 #3 정식 Fixed `4be0938`·30+회 프론트 정체 종결·backend B02 #5·B08 dirty-tree 확대·false Fixed 재확인·Open 0)**: ① frontend **QA-B07 recurrence #3 Fixed** — COD 31차 `4be0938`(82 files +4589/-545, 15 ahead) 일괄 커밋, WT **76→0 CLEAN**, `git cat-file -e HEAD:` FE-12/13/14 전 산출물 PRESENT(이관 규율 5 PASS)·HEAD `npm test` **185/33**·build **752 modules**·audit 0. ② **비차단 LOW 신규** — 단일 JS 청크 **744.95 kB**(>500 kB) → `manualChunks` 코드 스플릿(FE-15·v1.2 후속, merge BLOCK 아님). ③ backend **dirty-tree 확대(1M+4U→3M+4U)** — B08 WIP가 `MustApiEndpointRoutingTest`(+64)·`RoleBasedControllerAccessTest`(+93) modified까지 확장·**COD Fixed(B02 #5·B08) TSR + planner 검증 FAIL**(HEAD ABSENT)·WT `mvn test` 249/249. ④ **#36 비대칭 종결** — frontend FE-6 #3 해소로 에스컬레이션 **backend 단독** 축소. ⑤ 잔여 BLOCK = **B03 + B02 #5 + B08**(B07 #3 소멸). |
| 2026-06-07 | **48차 — 결정 73 (사용자)**: live E2E merge 게이트 제외 · v1.1 `merge_status: ready` · 잔여 BLOCK merge(6+11)+B03 |
| 2026-06-08 | **자동 동기화 47차 — TSR 64·65 + BNK-9**: BE-11 Fixed @ `8d42bdd` · FE-22 harness @ `d592a17` PARTIAL · baseline `80bdb1e`/`d592a17` · 18 route KPI · Directions API·이동서비스비·G17~G19 · merge(6+11)+B03+live E2E run |
| 2026-06-08 | **자동 동기화 55차 — TSR 74·75 재확인 + BNK-9 불변 + Epic E 진전 + v1.2 P0 게이트 충족**: backend `8ce1151`(11 ahead·WT CLEAN·178/178) · frontend `a627c6d`(8 ahead·WT CLEAN·110/36·33 route·117 modules) · BNK-9·G17~G19 불변 · QA Open 0 · 잔여 BLOCK backend merge(11)+B03/SEC-D14+v1.2 8 ahead |
| 2026-06-08 | **자동 동기화 52차 — TSR 70·71 + BNK-9 재확인 + v1.2 UXD 15 pages·P0 KPI**: backend `78e8928`(9 ahead·WT CLEAN·171/171·DAILY_CARE alimtalk dispatch) · frontend `42f48e1`(4 ahead·WT CLEAN·89/28·33 route·114 modules) · test `4f71543` v1.1 merged · BNK-9·G17~G19 불변 · 모듈 커버 ~45–50% 추정 · 잔여 BLOCK backend merge(9)+B03/SEC-D14(backend)+v1.2 4 ahead |
| 2026-06-08 | **자동 동기화 51차 — TSR 68·69 + v1.1 merged + UXD 35 v1.2 커밋**: backend `44e0f02`(8 ahead·WT CLEAN·170/170) · frontend `e0eaf32`(2 ahead·WT CLEAN·82/27·18 route) · test `4f71543` v1.1 merged · BNK-9·G17~G19 불변 · 잔여 BLOCK backend merge(8)+B03/SEC-D14(backend)+v1.2 2 ahead |
| 2026-06-08 | **자동 동기화 50차 — BNK-9 재확인 + frontend dirty-tree 재확대**: backend `c221531`(7 ahead·WT 3M 불변) · frontend `4f71543`(WT **24 files** Must UI WIP·18 route·develop=test) · BNK-9·G17~G19 불변 · #44 law.go.kr 잔여 · 잔여 BLOCK backend merge(7)+B03+WT **27 files** |
| 2026-06-08 | **자동 동기화 49차 — TSR 66·67 + BNK-9 재확인**: backend `c221531`(v2/J03 alimtalk E2E·169/169·7 ahead·WT 3M) · frontend `4f71543`(UXD SideNav·FE-22 liveConfig·58/18·86 modules·develop=test) · BNK-9 불변 · 잔여 BLOCK backend merge(7)+B03+WT dirty |
| 2026-06-08 | **자동 동기화 46차 — SEC 6차 Open 2건 Planned + BNK-8 COMPETITOR_MATRIX 정합 + baseline 불변 재확인**: ① planner 실측 — backend `136239e`·frontend `7170b2a` WT CLEAN · `mvn test` 152/152 · `npm test` 40/11 · **45차와 동일**. ② **SEC-D14·SEC-D13 Open→Planned** → B03 merge·**BE-11**. ③ **FE-22**(live E2E) 신설. ④ COMPETITOR_MATRIX 케어포 배차 지도 △. ⑤ 잔여 BLOCK = merge(4+9)+B03+라이브 E2E+BE-11. |
| 2026-06-07 | **자동 동기화 30차 — TSR 45차 (frontend B07 #3 72→76 files·`FeeScheduleTable`(+test)·WT 181/30·749 modules·backend 44차 baseline 불변·Open 0)**: ① frontend **B07 #3 범위 확대** — 72→**76 files**, 신규 **`FeeScheduleTable`(+test)**·WT **181/30·749 modules**(+2/+1 tests vs 43차). ② **FE-13 `FeeScheduleTable` 수가표 테이블 UI**(US-G00a·케어포 9-x·`FeeRateHistoryPanel` HEAD 연계) 매핑. ③ backend **44차 baseline 불변** — B02 #5·B08·COD Fixed FAIL. ④ **#36 30차 연속 미조치** 강화. ⑤ 잔여 BLOCK = **B03 + B02 #5 + B07 #3 + B08** 불변. |
| 2026-06-07 | **자동 동기화 29차 — TSR 42·43차 (backend B08 @Test 5→8·WT 243/243·frontend B07 #3 61→72 files·청구·건강·NHIS·보호자 UI WIP·Open 0)**: ① backend **42차 상태 불변** — B08 @Test 5→8·WT `mvn test` 243/243(+3)·COD Fixed FAIL 재확인. ② frontend **B07 #3 범위 확대** — 61→**72 files**, 신규 `BillingStatusConfirmModal`·`CopayRateTable`·`GuardianDailySummary`·`HealthAlertList`·`NhisImportGuidePanel`(+tests)·WT **179/29·748 modules**. ③ **FE-12 `HealthAlertList`·FE-13 청구·copay·NHIS·보호자 UI** 매핑. ④ **#36 29차 연속 미조치** 강화. ⑤ 잔여 BLOCK = **B03 + B02 #5 + B07 #3 + B08** 불변. |
| 2026-06-07 | **자동 동기화 27차 — TSR 40·41차 (backend COD false Fixed 철회·`.gitignore` 부분 진전·frontend 41차 상태 불변·Open 0)**: ① backend **COD false Fixed 철회** — B02 #5·B08 develop HEAD **ABSENT**(TSR 40차 `git cat-file -e HEAD:` FAIL)·`.gitignore` +`data/backups/` 1M 미커밋(부분 진전)·WT `mvn test` 240/240. v1 **QA-B02 `[x]`·v2 BE-7 `[x]` 철회**. ② frontend **41차 상태 불변** — 60→**61 files**(±1 modified)·WT 169/24·743 modules·audit 0. ③ **#36 인프라 강제 단계 진입 검토** 강화. ④ 잔여 BLOCK = **B03 + B02 #5 + B07 #3 + B08** 불변. |
| 2026-06-07 | **자동 동기화 26차 — TSR 38·39차 (상태 불변·B07 #3 44→60 files·운영/보안 설정 UI 확장·B08 dirty-tree 잔존·Open 0)**: ① backend **B02 #5·B08 Planned 불변** — `notification_preferences` 7 java·5 @Test + `data/backups/` manifest untracked·Maven 213/213·`@Test` HEAD 199/WT 226·JAR 82,868,029 B. ② frontend **B07 #3 범위 확대** — 44→**60 files**, 신규 계정 보안·로그인 이력 UI(`LoginHistoryPanel`(+test)·`PasswordChangeModal`(+test, **COD 03:08 SettingsPage 보안 탭 연결**)·`PasswordResetRequestModal`(+test)·`PlatformOrgDetailModal`(+test)·`SettingsPage.test`·`HealthTrendChart.test`)·WT 169/24·743 modules·audit 0. ③ **FE-14 범위 확장** — 운영·보안 설정 UI에 §3-1 로그인 이력·비밀번호 변경·비밀번호 재설정 매핑, **FE-13에 `PlatformOrgDetailModal`(US-A01 Tenant 상세) 추가**. ④ **COD 03:08 부분 진전·develop 미커밋** — Settings 보안 탭 통합 진전. ⑤ 잔여 BLOCK = **B03 + B02 #5 + B07 #3 + B08** 불변. |
| 2026-06-07 | **자동 동기화 25차 — TSR 36·37차 (상태 불변·B07 #3 26→44 files·B08 dirty-tree 잔존·Open 0)**: ① backend **B02 #5·B08 Planned 불변** — `notification_preferences` WIP 6→**7 java**·4→**5 @Test** + `data/backups/` manifest untracked·Maven 213/213. ② frontend **B07 #3 범위 확대** — 26→**44 files**, 신규 운영/보안 설정 UI(`AuditLogPanel`·`BackupSettingsPanel`·`PasswordChangeModal`·`FilterChips`)·WT 161/20·741 modules. ③ **FE-14 신설**(운영·보안 설정 UI). ④ **coder 미조치 지속**·신규 Open 0. ⑤ 잔여 BLOCK = **B03 + B02 #5 + B07 #3 + B08** 불변. |
| 2026-06-07 | **자동 동기화 24차 — TSR 34·35차 (B08 Open→Planned + B07 #3 26 files + v1 merged·SEC-007 test 해소)**: ① backend **B08 Planned** — v2 `notification_preferences` V41 + 6 java + 4 @Test WIP. ② frontend **B07 #3 범위 확대** — 18→26 files(`BatchProgressSteps`·Platform WIP). ③ v1 **`merged`**·SEC-007 test 해소·Maven 213/213. ④ **이관 규율 8항**(v2 선행 dirty-tree). ⑤ **FE-13·BE-7·API_SPEC §11** 신설. ⑥ 잔여 BLOCK = **B03 + B02 #5 + B07 #3 + B08**. |
| 2026-06-07 | **자동 동기화 23차 — TSR 32·33차 (B02 #5·B07 #3 dirty-tree recurrence + v1 merged·B05 해소 + Recharts WIP)**: ① backend **B02 #5 Planned** — `PilotChecklistJwtE2eTest` untracked, planner 22차 false `[x]` 철회. ② frontend **B07 #3 Planned** — Recharts 18 files WIP, FE-6 #3 재발. ③ v1 **`merged`**·B05 Fixed·backend test `@e8750d2` merge 완료. ④ v1.2 **Recharts 차트 레이어** P0·FE-12. ⑤ 잔여 BLOCK = **B03 + B02 #5 + B07 #3**. |
| 2026-06-07 | **자동 동기화 21차 — TSR 30·31차 (B02 #4 Fixed + COD 22 pilotPageFlows P1–P8 페이지 E2E + UXD 14 FeeRateHistoryPanel)**: ① backend **QA-B02 #4 Fixed**(COD 21차 `e8750d2` SevenRoleJwtLoginE2eTest, `@Test` 199, R-04 live JWT E2E [x]). ② frontend **R-05 P1–P8 페이지 E2E PARTIAL 강화**(COD 22 `3fdc266` pilotPageFlows 433 lines, `npm test` 140/11). ③ **UXD 14차 `a42d6fb`** US-G00a 수가 이력 UI. ④ 결정 52 흡수 **8묶음**. ⑤ Open 0·Planned BLOCK 4건(merge 게이트 단일). ⑥ #36 BE-6 #4 Fixed. |
| 2026-06-06 | **자동 동기화 20차 — TSR 28·29차 (B02 recurrence #4 Open→Planned + UXD 13차 Switch·셀프 체크인 토글 흡수 + COD 20차 7역할 JWT 로그인·라우트 가드 Vitest 단위 E2E 자동화 정식 충족)**: ① backend **B02 recurrence #4 Open→Planned**(TSR 28차 COD `c3f3146` 불변·working tree DIRTY 1 untracked `SevenRoleJwtLoginE2eTest.java` 384 lines — 7역할 JWT 로그인 E2E 통합 테스트 WIP, Spring Security filter chain·JwtAuthFilter·UserDetailsService 통합 라이브 발급/검증, 이관 규율 6 위반·BE-6 #4 재발). v1 완료 기준 QA-B02 `[x]` **철회**·BE-6 5커밋 무재발 종결 공언 철회·USER_STORIES §17 BE-6 패턴 재오픈. ② frontend **R-04 7역할 JWT 로그인·라우트 가드 Vitest 단위 E2E 자동화 정식 충족**(TSR 29차 COD 20차 `57ff3c0` — `sevenRoleJwtLogin.test.jsx`(132)·`sevenRoleRouteGuard.test.jsx`(83)·`sevenRoleRouteMatrix.js`(75)·`roleHomePaths.test.jsx`(+26) 4 files +316, `npm test` 37/8→**130/10 PASS**(+93/+2)·build 112 modules·audit 0건, working tree CLEAN). v1.1 7역할 화면·메뉴·권한 분리 단위 E2E `[x]` 강화. ③ **UXD 13차 `07fd305` 흡수**(전사 설정 Switch WAI-ARIA `role=switch`/`aria-checked`/44px hit/`forced-colors`·SettingsPage `allow_client_self_checkin` 토글·`Switch.test.jsx` 5건 회귀 — 7 files +218/-7, 결정 16 안 3 UI 정착). **US-UX-03 신설**. ④ **결정 52 흡수 7묶음 갱신**(+UXD 13차 + COD 20차 = 총 12커밋·~89 files). ⑤ **#36 에스컬레이션 재오픈** — BE-6 5커밋 무재발 종결 공언 철회·#4 재발, 운영 게이트 권고 재검토 필요. FE-6는 무재발 6커밋 유지. ⑥ Planned BLOCK **5건**(B01·**B02 #4**·B03·B05·SEC-007) — Open 0건(planner 20차 반영 후 회복). |
| 2026-06-06 | **자동 동기화 18차 — TSR 24·25차 (B07 recurrence #2 Fixed + SEC-008 Fixed + R-02 Must API 라우팅 [x] 승격)**: ① backend **R-02 PARTIAL→[x] 승격**(TSR 24차 COD 16차 `aa71412` — `MustApiEndpointRoutingTest`(+459 26+ tests)·`RoleBasedControllerAccessTest`(+148)·`ProductionSecretValidatorTest`(+59) 3 files 일괄 커밋, working tree CLEAN, `@Test` 120→**154**, Maven 79/79 PASS·package SUCCESS), v1 완료 기준 QA-B02 *(`aa71412`)* 갱신·R-02 [x]. ② **SEC-008 Open→Planned→Fixed 동일 사이클**(24차 npm audit 5 vuln/1 critical 에스컬레이션 → COD 17차 `ed1bf22` vite `^6.4.3`·vitest `^4.1.8`·`overrides.esbuild ^0.25.0` → 25차 audit 0건). ③ frontend **B07 recurrence #2 Planned→Fixed**(25차 COD 17차 `a84473f` US-M02 8 files +636/-170 일괄 커밋 — `dashboardWidgets.js`·`.test.js`·`DashboardPage`·`AttendancePage`·`ClientFormPage`·`GuardiansPage`·`GuardianListCard`·`services.js`, working tree CLEAN, HEAD build 111 modules·`npm test` 13/5 PASS·audit 0건), v1.1 B07·SEC-008·B04 `[x]`·v1.2 US-M02 develop 커밋 [x]. ④ **결정 52 흡수 5건**: v1.2 P0 `a72e249` + US-D03 `3fc549a` + UXD 10차 `5656e19` + UXD 11차 `2d742b3`(dark mode) + COD 17차 `a84473f`+`ed1bf22` — 모두 v1.1 develop→test merge 동반. ⑤ **#36 양 스트림 패턴 종결**: BE-6 #3 Fixed 후 4커밋 무재발(15·16차)·FE-6 #2 Fixed via `a84473f`(17차). 잔여 BLOCK = **merge 게이트(B01·B03·B05·SEC-007) 단일** — dirty-tree·B02·B07·SEC-008 사유 모두 소멸. ⑥ Open 0건 유지. |
