> 빌드 실패 처리 규칙 (추가: 2026-06-07, 사용자 지시)
- 원칙: 빌드 실패 시 즉시 빌드를 중단하고 실패 원인과 복구 계획을 문서화한다.
- coder 책임:
  1. 실패 로그(빌드 stdout/stderr, 테스트 실패 요약)를 확보하여 `INFRA-1-start` TODO에 첨부 및 보고한다.
  2. 원인 요약(예: 컴파일 에러/테스트 실패/의존성 불일치/환경 변수 누락 등)과 임시 대응(스태시·리버트·빠른 패치)을 기록한다.
  3. 수정 브랜치 또는 버그 이슈를 생성하고(`branch: fix/<short-desc>`), 관련 커밋과 PR 링크를 보고한다.
  4. 민감정보(시크릿·토큰)는 로그에 노출하지 않고, 필요한 경우 마스킹 후 보고한다.
  5. 수정 완료 후 재시도(build/rerun tests) 결과를 보고하고, 실패 반복 시 planner에게 즉시 에스컬레이션한다.
- 추적: 위 항목은 `PLAN_NOTES.md`에 회고 및 원인 분석으로 누적 기록한다.

> 자동 에스컬레이션 (추가: 2026-06-07, 사용자 확정)
- 주기: 실패 발생 후 12시간마다 자동 에스컬레이션(지속 실패 시 12시간 간격으로 planner 및 지정된 운영 담당자에게 알림).
- 에스컬레이션 내용: 최신 실패로그 링크, 원인 요약, 현재 수정 브랜치/PR 링크, 다음 예상 조치.
- 에스컬레이션 채널: GitHub 이슈(권장) + 지정된 알림 채널(예: Slack) — 채널 미지정 시 GitHub 이슈를 기본 사용.

> 실패 로그 관리(추가: 2026-06-07)
- 권장 방식(간단):
  1. CI(예: GitHub Actions)에서 빌드 아티팩트로 실패 로그 업로드.
  2. 관련 GitHub 이슈를 생성하고(또는 기존 이슈에 코멘트), 아티팩트 링크 및 마스킹된 로그 요약을 첨부.
  3. PR을 통해 수정 시 PR 코멘트에 이슈 링크와 빌드 재시도 결과를 남김.
- 보안: 로그 제출 전 시크릿·토큰 마스킹 필수.

> dirty-tree 정리 정책 (추가: 2026-06-07, 사용자 지시)
- 정의: dirty tree = develop 브랜치의 작업 디렉토리에 커밋되지 않은 변경(수정·스테이지되지않은 파일·추적 안된 파일) 존재 상태.
- 주기: 정리 주기 24시간(매 24시간마다 L1 검사와 병행하여 정리 권고).  
- 조치: coder는 24시간 내에 dirty 상태를 해소(적절한 커밋 / 스태시 후 별도 브랜치로 이동 / 불필요 변경 리셋)하고 결과를 `FE-dirty-tree-clean` TODO에 보고.
<!-- doc:owner=PLN doc:audience=COD,TSR,UXD,DBA,BNK,TWR updated=2026-06-18T09:00:00+09:00 -->
<!-- planner-sync: PLN 159차 2026-06-18T09:00 KST — BNK-307~310·func 2-9 verification closure·audit trail FE wire full-stack·QA-B121 Planned · merge 398 BLOCK(FE only) · FE `b48252a`/BE `30243f7` WT CLEAN -->
<!-- planner-sync: PLN 158차 2026-06-18T06:00 KST — BNK-303~306·func 2-7/2-8 full-stack·audit trail read API·NHIS #44 5-date·K008 FAQ21768 · merge 385 FULLY UNBLOCKED · FE `8b68fdb`/BE `6eb9cc0` WT CLEAN -->
<!-- planner-sync: PLN 157차 2026-06-18T03:00 KST — BNK-298~302·TSR 898~909 · ★ G15 일지④ PUT persistence+FE 편집 closure live(v1.3-C Must 후보) · ★ silverangel CMS 3-method mainService.do → G2b parity · ★ longterm KRDS DRIFT → V103 seed authoritative · QA-B120 Fixed @ `af4d7f8` · QA-B116 Planned(merge pending 28·post-merge 재검증) · QA-B95 Planned carry · 신규 갭 0·가정 번복 0 · merge 374 FULLY UNBLOCKED · FE `cb30f24`/BE `c13800c` WT CLEAN -->
<!-- doc:owner=PLN doc:audience=COD,TSR,UXD,DBA,BNK,TWR updated=2026-06-23T17:30:00+09:00 -->
<!-- planner-sync: PLN 191차 2026-06-23T17:30 KST — BNK-551~552·TSR 1321~1322차 · ★ US-R01-c leave-ledger BE ✅ FE wire △ · ★ v1.3-C M2 차별화 · ★ QA-B272/B273 Planned · merge gate 718 · cross-stream BLOCK · QA Open 0(active) -->
<!-- planner-sync: PLN 188차 2026-06-22T18:00 KST — BNK-515~519·TSR 1282~1285차 · ★ G2-CMS-ENROLLMENT-ROSTER ✅ full-stack closure · ★ G34-WORKFLOW-CATALOG ✅ full-stack closure · ★ G-STAFF-ANNUAL-LEAVE P3 candidate · ★ QA-B248 Planned(BE merge pending 2) · merge gate 685 · cross-stream BLOCK(BE) · QA Open 0(active) -->
<!-- planner-sync: PLN 187차 2026-06-22T09:30 KST — BNK-505~507·TSR 1269~1271차 · ★ M7 10/10+superset ✅ · ★ G34-WORKFLOW-CATALOG·G30-LEGEND P3 candidate · ★ QA-B239 Fixed @ `9db0bbb` · ★ QA-B240 Planned(FE merge pending 1) · merge gate 674(FE162+BE512) · cross-stream BLOCK(FE) · QA Open 0(active) -->
<!-- planner-sync: PLN 186차 2026-06-22T09:00 KST — BNK-491~493·TSR 1248~1255차 · ★ 모듈 78.79% KPI(+0.34pp·CMS 0.65) · ★ G-BILLING-DEPOSIT-ORDER-GUARD ✅ 3-channel · ★ G-BILLING-REPORT-FILTER-PERSISTENCE △ BE(V170) · ★ QA-B222 Fixed @ `5fd468b` · ★ QA-B229~B231 Fixed carry · merge gate 661(FE156+BE505) · BE SYNCED/FE merge pending 1 · cross-stream SYNCED(BE) · QA Open 0(active) -->
<!-- planner-sync: PLN 185차 2026-06-21T21:30 KST — BNK-477~480·TSR 1234~1241차 · ★ 모듈 78.45% KPI 정본 · ★ G-ATTENDANCE-ROSTER-STATUS ✅ superset · ★ NHIS #44 G16 parity 재입증 · QA-B222 Open→Planned · ★ QA-B223 Fixed @ `61e1970` · merge gate 647 · cross-stream BLOCK(FE) · QA Open 0(active) -->
<!-- planner-sync: PLN 184차 2026-06-21T20:30 KST — BNK-470~471·TSR 1223~1226차 · ★ G-STAFF-DOCUMENT-REPOSITORY P3 △→✅ FULL-STACK closure · ★ G-BATHING ✅ full-stack carry(183차 partial 정정) · ★ 신규 G-MENU-PERMISSION-MATRIX P3「가정」 · QA-B212/B213/B214 Open→Planned · merge gate 634 · cross-stream SYNCED · QA Open 0(active) -->
<!-- planner-sync: PLN 183차 2026-06-21T12:00 KST — BNK-464~465·TSR 1214~1215차 · ★ G15-KAKAO-QUOTA-DASH △→✅ closure · ★ G-BATHING BE API △→✅ partial(FE wire P2) · QA-B204 Planned · merge gate 623 · cross-stream BLOCK(BE) · QA Open 0(active) -->
<!-- planner-sync: PLN 182차 2026-06-21T11:30 KST — BNK-456~458·TSR 1192~1203차 · ★ G-BILLING 3건 △→✅ full-stack closure · ★ G32 FAQ21740 parity deepen · QA-B195/B196/B192 Planned · QA-B193/B194 Fixed · merge gate 612 · cross-stream BLOCK · QA Open 0(active) -->
<!-- planner-sync: PLN 181차 2026-06-21T08:30 KST — BNK-447~452·TSR 1184~1191차 · ★ QA-B186 Fixed @ `82a542c` · ★ G-STAFF-LEAVE-STATUS △→✅ full-stack closure(V166·`onLeaveCount`·휴직 Badge·P3 candidate 제거) · ★ 4축 교차검증 가정 번복 0 · ★ 신규 candidate G-COMM-CALLER-AUTH P3(silverangel 221562 발신번호 인증 마감 6/23) · QA-B187/B188 Open→Planned · merge gate 602 · FE/BE merge pending 2 · cross-stream BLOCK(FE+BE) · QA Open 0(active) -->
<!-- planner-sync: PLN 180차 2026-06-21T05:30 KST — BNK-445~446·TSR 1177~1179차 · ★ QA-B181 Fixed @ `a18b30e` · ★ G-BANK-EXCEL-8 ✅ full-stack · ★ G-STAFF-NHIS-EXCEL-IMPORT ✅ full-stack · ★ 신규 P3 G-STAFF-LEAVE-STATUS·G-BILLING-DEPOSIT-HALFMONTH-REPORT · QA-B182 Open→Planned · merge gate 590 · FE SYNCED/BE merge pending 1 · cross-stream BLOCK(BE) · QA Open 0(active) -->
<!-- planner-sync: PLN 179차 2026-06-20T23:00 KST — BNK-435~441·TSR 1165~1167차 · ★ G-BILLING-PRIOR-DEPOSIT-GUARD ✅ closure · ★ G-BANK-EXCEL-8/G-STAFF-NHIS-EXCEL-IMPORT △ BE partial · QA-B178 Open→Planned · QA-B177 Fixed · merge gate 581 · FE SYNCED/BE merge pending 1 · cross-stream BLOCK(BE) · QA Open 0(active) -->
<!-- planner-sync: PLN 178차 2026-06-20T21:00 KST — BNK-432~434·TSR 1154~1155차 · ★ G14 plan-form △→✅ closure(V164) · ★ G24 FAQ21800 8-item parity ✅ · ★ QA-B169~B172 Fixed · ★ G-BILLING-PRIOR-DEPOSIT-GUARD P2 · ★ G-BANK-EXCEL-8 P3 candidate · merge gate 569 · FE/BE `@d723d5a`/`@80b9619` SYNCED WT CLEAN · cross-stream SYNCED · QA Open 0(active) -->
<!-- planner-sync: PLN 177차 2026-06-20T18:00 KST — BNK-424~429·TSR 1137~1143차 · QA-B169/B170 Open→Planned · ★ G15-KAKAO-INTEGRATION 6-layer 우위 · ★ G15-KAKAO-QUOTA-DASH P3 candidate · ★ QA-B163/B167 Fixed · merge gate 555 · FE `@ba74bb5`/BE `@e2b764b` WT DIRTY 9M+4U · cross-stream BLOCK(FE+BE) · QA Open 0(active) -->
<!-- planner-sync: PLN 176차 2026-06-20T15:00 KST — BNK-419~423·TSR 1127~1131차 · QA-B163 Open→Planned · ★ QA-B159 Fixed @ `bfad37d` · ★ G-CASH-RECEIPT-LOG end-to-end 재입증 ✅ · ★ FAQ21823 partial+ · merge gate 543 · FE merge pending 2/BE SYNCED · cross-stream BLOCK(FE) · QA Open 0(active) -->
<!-- planner-sync: PLN 175차 2026-06-20T12:00 KST — BNK-417~418·TSR 1118~1119차 · QA-B159 Open→Planned · ★ FAQ21823 G-Staff-LC △ partial · ★ 케어포 module 7 11/11 ✅ · ★ ezCare bc7f4cd9 G21 parity · QA Open 0(active) · merge gate 533 · FE `@f31c346` SYNCED/BE merge pending 2 · live E2E 126 PASS/19 SKIP -->
<!-- planner-sync: PLN 174차 2026-06-20T07:00 KST — BNK-406~412·TSR 1100~1107차 · QA-B157 Open→Planned · ★ G26 yearBasis+NTS CSV ✅ · ★ G-7-1 Excel ✅ · ★ G-CASH-RECEIPT-LOG 6-계층 deepen · ★ G-CASH-RECEIPT-TAX-DEDUCTION-EXPORT △→✅ · ★ G-PROVIDER-CHANGE-COUNSEL P3 candidate · merge gate 522 · FE `@99b795a` SYNCED/BE merge pending 1 -->
<!-- planner-sync: PLN 173차 2026-06-20T04:00 KST — BNK-399~405·TSR 1086~1096차 · ★★★ G-CASH-RECEIPT-LOG 4-계층 closure ✅(172차 P2 gap → closure·신규 갭 0) · ★ 신규 candidate G-CASH-RECEIPT-TAX-DEDUCTION-EXPORT P3 · QA-B153/B154 Fixed · QA Open 0 · merge gate 511 · FE `@8aebe55`/BE `@58ff35e` develop=test SYNCED WT CLEAN -->
<!-- planner-sync: PLN 172차 2026-06-19T23:30 KST — BNK-393~398·TSR 1074~1085차 · ★ 신규 갭 1 G-CASH-RECEIPT-LOG P2「확인」(BNK-398 FAQ 21701/21716/21717·G-CASH-RECEIPT P3 승격·US-G26) · ★ 신규 candidate G-LTM-DIRECT-SYNC P3「가정·미확인」 · QA-B150/B151/B152 Fixed · QA Open 0 · merge gate 498 · FE `@9b80505`/BE `@caeac0d` develop=test SYNCED WT CLEAN -->
<!-- planner-sync: PLN 171차 2026-06-19T16:00 KST — BNK-386~392·TSR 1062~1073차 · ★ G32 FAQ21797 6/6 full-stack closure(per-attendee opinions + dashboard due gate @ `e55ae96`/`b9e0947`) · ★ V156 migration 정정 · QA-B151 Planned · merge gate 485 · FE `@e55ae96`/BE `@b9e0947` WT CLEAN -->
<!-- planner-sync: PLN 169차 2026-06-19T11:50 KST — BNK-376~380·TSR 1040~1049차·★ G21 seed readiness NHIS row-batch linkage ✅ @ `c0403b0` · ★ page 85 · ★ QA-B142~B145 Fixed · merge gate 461 · FE `@0915f80`/BE `@c0403b0` SYNCED WT CLEAN · live E2E 123 PASS/19 SKIP -->
<!-- planner-sync: PLN 168차 2026-06-18T23:45 KST — BNK-368~375·TSR 1028~1039차·★ G21 standalone NHIS comparison panel @ `797c529` · ★ G41 filter-year @ `28e5525` · ★ silverangel G15 실데이터 일지 full-stack 우위(BNK-375) · QA-B142/B143 Planned · merge gate 451 · FE `@28e5525` DIRTY 2M/BE `@f932fd3` DIRTY 2M -->
<!-- planner-sync: PLN 167차 2026-06-18T22:30 KST — BNK-362~367·TSR 1016~1027차·★ G21 batch-confirm readiness full-stack closure(△→✅)·★ G-SCHEDULE-FIX-LTM-COMPARE BE closure(P3→✅)·★ G-7-1-PRINT-BUNDLE ✅+·★ G-CHANGE-REASON-AUDIT P3 candidate · QA Open 0 · merge gate 440 · FE `@f232285` SYNCED/BE `@8a8c5b3`(merge pending 1) WT CLEAN -->
<!-- planner-sync: PLN 165차 2026-06-18T18:00 KST — BNK-348~354·TSR 1000~1003차·G41 ✅+ deepen·G21 RFID ✅ full-stack·G-SCHEDULE-FIX-LTM-COMPARE P3 · FE `@caa215f`/BE `@dac19d3` WT CLEAN -->
<!-- planner-sync: PLN 164차 2026-06-18T15:00 KST — BNK-342~347·TSR 980~991차·QA-B135 Fixed·G15 partial+++·G21 RFID 7-code P1 · FE `@1c8f236`/BE `@d7f1a9a` WT CLEAN -->
<!-- planner-sync: PLN 163차 2026-06-18T11:30 KST — BNK-335~341·TSR 970~979차·QA-B131/B132/B133 Fixed·carefor transport 10-leaf·FAQ21799 신규직원 건강검진 △·merge local SYNCED · FE `@38642e2`/BE `@40ef105` WT CLEAN -->
<!-- planner-sync: PLN 162차 2026-06-18T07:30 KST — BNK-333~334·TSR 955~969차·QA-B127~B130 Fixed·QA-B131 Planned·silverangel 6종 zero drift·carefor 7-x Route 1:1·merge FULLY UNBLOCKED · FE `@7d2cb4a`/BE `@09df8c7` WT CLEAN -->
<!-- planner-sync: PLN 161차 2026-06-17T18:00 KST — BNK-321~323·TSR 952~954차·QA-B127/QA-B128 Planned·G-STAFF-WORKLOG·G-HOSPITAL-ESCORT P3 candidate·G-CASH-RECEIPT deepen·merge 420 BLOCK · FE `@188ce71`/BE `@73cffc5` WT BLOCK -->
<!-- planner-sync: PLN 160차 2026-06-18T12:00 KST — BNK-311~315·TSR 932~942차·QA-B121/B122 Fixed·신규 갭 candidate G-CASH-RECEIPT P3「가정」(FAQ21700 현금영수증) · merge 410 FULLY UNBLOCKED · FE `0baabe9`/BE `f0e52b8` WT CLEAN -->
<!-- planner-sync: PLN 156차 2026-06-18T00:00 KST — BNK-292~297·이지링크(EzLink) 차별화·G-COGNITIVE-WORKSHEET(=G29) · merge 364 FULLY UNBLOCKED · FE `825c6b0`/BE `8a1f342` WT CLEAN -->
<!-- planner-sync: PLN 153차 2026-06-17T12:00 KST — BNK-280~285·3-product line·dual-source numbering · QA-B112/B114 Planned · merge 341 BLOCK · FE `b000d92`/BE `7ac0a46` -->
<!-- planner-sync: PLN 150차 2026-06-17T03:00 KST — BNK-262~268·TSR 826~837 · G26 7-8 통계 대시보드 ✅ full stack · FE `d8f1fdf`/BE `3481eb8` · QA-B95 Planned · merge 315(BE) -->
<!-- planner-sync: PLN 148차 2026-06-16T18:00 KST — BNK-252~255·TSR 801~812 · v1.3-A Kakao route preview ✅ · L02_M04/M05 rpt ✅ full · L02_M17 rpt △ BE · QA-B95 Planned · merge 312 · FE `388e1da`/BE `ae7e744` -->
<!-- planner-sync: PLN 147차 2026-06-16T12:00 KST — BNK-248~251·TSR 789~800 · L02_M13/M15 ✅ · G30 phone panel ✅ full · FE merged · L02 6/15(40%) · plan/claim P2 · QA-B95 Planned · merge 301 · FE `c5f82a6`/BE `c655743` -->
<!-- planner-sync: PLN 145차 2026-06-16T06:00 KST — BNK-240~243·TSR 765~776 · L02_M07 ✅ full · 7-1 4채널 P2 · MOHW 2026-126 · QA-B99 Planned · merge 636 BLOCK(FE) · FE `6f53978`/BE `18ff83e` -->
<!-- planner-sync: PLN 144차 2026-06-16T00:30 KST — BNK-236~239·TSR 753~764 · G30 evidence window ✅ deepen · G39 ✅ partial+ · L02_M02 ✅ FE wire · G-BODY-RESTRAINT(L02_M07) P2 · G-STAFF-LIFECYCLE P2 · G-REVENUE-EXPENSE P3 · func.php 107 leaf · QA Open 0 · QA-B95 Planned · merge 625 · FE `95e7e96`/BE `df14e15` -->
<!-- planner-sync: PLN 143차 2026-06-15T21:00 KST — BNK-232~235·TSR 741~752 · G24b list ✅ · G19 harness △ · G30/G39 P2 deepen △ · #44 lawImg DRIFT · G18-SHORT 연장 · QA-B95 Planned · merge 612 · FE `73094f9`/BE `73df04d` -->
<!-- planner-sync: PLN 142차 2026-06-15T18:00 KST — BNK-227~231·TSR 729~740 · G24b dashboard ✅ · G41 enum 23+ ✅ · G19 provider discovery P1 · QA-B95 Planned · merge 602 · FE `3cbe582`/BE `1e21b20` -->
<!-- planner-sync: PLN 141차 2026-06-15T14:00 KST — BNK-224~226·TSR 717~728 · G-ONBOARD-SUPPORT ✅ full · G24b ✅ full · QA-B94 Fixed · merge 589 FULLY UNBLOCKED · FE `92b9eff`/BE `f4c8beb` -->
<!-- planner-sync: PLN 140차 2026-06-15T11:00 KST — BNK-219~223·TSR 705~716 · QA-B93 Fixed · G-ONBOARD-SUPPORT △ BE · merge 577 FULLY UNBLOCKED · FE `2ccc88e`/BE `735dd53` -->
<!-- planner-sync: PLN 139차 2026-06-15T08:00 KST — BNK-217~218·TSR 693~704 · L03 13/14 ✅ effective 100% · QA-B93 Planned · merge 566 BLOCK(BE) · FE `89dc52d`/BE `6b0238a` -->
<!-- planner-sync: PLN 138차 2026-06-15T05:00 KST — BNK-213~216·TSR 681~692 · v1.3-B ✅ full · L03_M01/M06 △ BE · QA-B88/B89/B90 Fixed · merge 555 FULLY UNBLOCKED · FE `3845f0c`/BE `a4352a8` -->
<!-- planner-sync: PLN 137차 2026-06-15T02:00 KST — BNK-209~212·TSR 669~680 · L03_M11/M13/M14/M04 ✅ full · QA-B86/B87 Fixed · QA-B88/B89/B90 Planned · v1.3-B △ partial+ · merge 545 BLOCK · FE `97108f2`/BE `090b2d7` -->
<!-- planner-sync: PLN 136차 2026-06-14T23:00 KST — BNK-204~208·TSR 657~668 · G-NURSING ✅ full · L03_M11 ✅ full · L03_M14 BE △ · QA-B86/B87 Planned · merge 534 BLOCK(BE) · FE `246df56`/BE `1a822d2` -->
<!-- planner-sync: PLN 134차 2026-06-14T17:00 KST — BNK-195~198·TSR 634~641 · G21 batch-confirm ✅ partial+ · US-UX-05 ✅ · QA-B81/B82 Fixed · merge 512 UNBLOCKED · FE `13e691e`/BE `c22a5dc` -->
<!-- planner-sync: PLN 132차 2026-06-14T14:00 KST — BNK-191~194·TSR 623~633 · 7-5 ✅ full · J03 quiet-hours ✅ partial+ · QA-B81/B82 Planned · merge 500 BLOCK(FE) · FE `111f056`/BE `a057739` -->
<!-- planner-sync: PLN 131차 2026-06-14T13:30 KST — US-UX-05 SideNav 5그룹 토글 · 사용자 요청 -->
<!-- planner-sync: PLN 129차 2026-06-14T05:30 KST — BNK-185~187·TSR 600~611 · G41/G41b ✅ partial+ · G-STAFF-WELFARE P3 · G-ONBOARD-SUPPORT P2 · QA-B76/B77 Fixed · merge 479 FULLY UNBLOCKED · FE `e14ba10`/BE `32f87f1` -->
<!-- planner-sync: PLN 128차 2026-06-14T04:00 KST — BNK-180~184·TSR 587~599 · G30 ✅ full · G34-QUAL ✅ partial+ · G41 △ BE · QA-B74 Fixed · merge 468 FULLY UNBLOCKED · FE `5146895`/BE `6191b91` -->
<!-- planner-sync: PLN 127차 2026-06-14T02:30 KST — BNK-176~179·TSR 574~586 · 8-12 ✅ partial+ · J03 readiness ✅ partial+ · G34-QUAL P2 · QA-B74 Planned · merge 455 BLOCK(FE) · FE `443efca`/BE `229f84c` -->
<!-- planner-sync: PLN 126차 2026-06-14T01:00 KST — BNK-172~175·TSR 562~573 · #44 P0 ✅ · 8-12 deepen · G42 partial+ · merge 443 FULLY UNBLOCKED · FE `a7a6004`/BE `39ee679` -->
<!-- planner-sync: PLN 125차 2026-06-13T23:30 KST — BNK-168~171·TSR 550~561 · G30 ✅ partial+ · 8-12 aggregated API ✅ partial+ · EZCare K008~K014 P3 · merge 430 FULLY UNBLOCKED · FE `07956f5`/BE `5692662` -->
<!-- planner-sync: PLN 124차 2026-06-13T21:00 KST — BNK-164~167·TSR 538~549 · G9-COG ✅ FE+BE · FAQ21824 checklist ✅ partial+ · G-7x-1 guard ✅ partial+ · G9-COPAY-NAMING ✅ · merge 418 FULLY UNBLOCKED · FE `e77b7e4`/BE `edd2771` -->
# 주간보호센터 웹 시스템 — 요구사항 명세 (planning/REQUIREMENTS.md)

> **작성**: planner 에이전트  
> **최초 작성일**: 2026-06-03  
> **최종 갱신**: 2026-06-23 (191차 — BNK-551~552 · TSR 1321~1322차 · **★ US-R01-c leave-ledger BE ✅ FE wire △ · ★ v1.3-C M2 차별화 · ★ QA-B272/B273 Planned · merge gate 718 · cross-stream BLOCK · disk ENOSPC**)  
> **상태**: 초안 (Draft) — 사용자 승인 전  
> **1주차 목표**: 관리자 대시보드 출력까지 (Must 기능 전체 포함)

---

## 1. 프로젝트 개요

| 항목 | 내용 |
|------|------|
| 프로젝트명 | ogada — **장기요양 통합 ERP** (주야간·방문요양·시설급여·재무회계) |
| 목적 | 장기요양기관의 이용자·일정·출석·건강·청구·수납·급여·회계 등 **운영·정산 전 과정** 디지털화 |
| **사업 모델** | **전국 판매용 B2B SaaS** (개인·단일 센터 전용 아님) |
| 주요 사용자 | 센터장, 사회복지사, 요양보호사, 보호자 |
| 플랫폼 | 웹 앱 (PC + 모바일 반응형) |
| 언어 | 한국어 |

### 1-1. 기술 스택 (사용자 확정: 2026-06-05)

| 계층 | 기술 | 비고 |
|------|------|------|
| 백엔드 | **Java — Spring Boot 3.x** | REST API, JWT 인증 |
| 프론트엔드 | **React — Vite SPA** | React Router, API 클라이언트 분리 |
| 데이터베이스 | **PostgreSQL** | dev/prod 동일 엔진 |
| 인증 | **JWT + RBAC** | 역할·지점 스코프 기반 접근 제어 |
| 아키텍처 | **SaaS 멀티테넌트** | Tenant(Organization) → Branch 계층, 테넌트 간 데이터 완전 격리 |
| 레거시 코드 | **폐기** | 기존 `src/backend`(Python/FastAPI) 전부 폐기, Java로 신규 시작 |

> **변경 이력**
> - 초기 에이전트 설정(Python/FastAPI + Vanilla JS) → **Java + React**로 변경
> - 기존 Python/FastAPI 코드 **전부 폐기**, Java 백엔드 신규 구현
> - 기술 세부(Spring Boot 3.x, Vite+React, PostgreSQL, JWT) **2026-06-05 확정**
> - 사업 모델 **전국 판매 B2B SaaS** 확정 (2026-06-05)

### 1-2. 사업·서비스 모델 (사용자 확정: 2026-06-05)

| 항목 | 정의 |
|------|------|
| 제품 성격 | 전국 **장기요양기관**(주야간·방문요양·시설급여·복합) 운영법인에 **판매·구독**하는 통합 ERP |
| 고객(Tenant) | 요양기관 운영 주체 1법인 = `Organization` 1개 |
| **급여종(서비스 유형)** | 지점(`Branch`)별 **1개 이상** — `DAY_CARE`(주야간) · `HOME_CARE`(방문요양) · `FACILITY_CARE`(시설급여) · 복합 지점 허용 (결정 89, 이지케어 가입 유형 대응) |
| 다지점 | 1고객이 여러 `Branch` 운영 (지점별 + 통합 관리) |
| 데이터 격리 | **테넌트(Organization) 간 데이터 접근 불가** — API·DB 모두 `organization_id` 강제 |
| 확장 목표 | 초기 소수 파일럿 → 전국 다수 법인·다지점 동시 운영 |
| 온보딩 | 신규 고객 Organization 생성 → 지점·계정·초기 설정 (플랫폼 관리 기능 필요, §1-3) |

**규모 가정 (전국 SaaS, 설계 기준 — 수치는 추후 조정)**

| 지표 | 1년차 목표 | 3년차 목표 |
|------|-----------|-----------|
| 가입 운영법인(Organization) | ~50 | ~500 |
| 전체 지점(Branch) | ~150 | ~2,000 |
| 동시 접속 | ~500 | ~5,000 |
| 지점당 이용자 | ~20–50 | 동일 |
| 지점당 직원 계정 | ~5–15 | 동일 |

### 1-3. 「새 고객 센터 계정은 누가 만들어 주나?」(= 반복 질문 1번의 본질)

> **용어 없이**: 전국에 센터에 ogada를 **팔 때**, 새 센터가 처음 쓸 **전용 공간 + 센터장 로그인**을 **누가 만들어 주느냐**는 질문이다.

**「행복주간보호센터」가 ogada 구매 → 월요일부터 사용. 그 전에:**

| 순서 | 해야 할 일 | 예시 |
|------|-----------|------|
| ① | 센터 **전용 데이터 공간** 만들기 | 행복주간보호만의 DB (다른 센터와 섞이면 안 됨) |
| ② | 센터장 **첫 로그인 계정** 만들기 | `kim@happy-care.com` 발급 |
| ③ | 센터장이 직원·이용자 등록 | 김센터장이 직접 (이미 확정) |

**1번 질문 = ①②를 누가 하느냐**

| 선택 | 누가 ①② 담당 | 쉬운 말 |
|------|------------|--------|
| **A** | **ogada를 파는 쪽 직원** | 통신사 매장이 **새 회선 개통**해 주는 것 |
| **B** | **각 센터 IT 담당** | 센터가 **스스로** 공간·계정 생성 |
| **C** | **센터가 웹에서 셀프 가입** | 쿠팡 **판매자 회원가입**처럼 스스로 신청 |

**역할 이름 (참고만)**: A → `platform_admin` 화면 `/platform` | B → `sysadmin`에 등록 기능 | C → `/signup`

#### 비유 한 줄

| 서비스 | 판매사 직원 (개통) | 고객사 IT (내부 관리) |
|--------|-------------------|---------------------|
| 휴대폰 | SKT 매장 직원이 **새 회선 개통** | 회사 IT가 **직원 폰 설정·백업** |
| **ogada** | **`platform_admin`** 이 **새 센터 법인 등록** | **`sysadmin`** 이 **자기 센터 백업·설정** |

#### 실제 흐름 예시 — 「행복주간보호센터」가 ogada 가입

| 순서 | 누가 | 화면에서 하는 일 | 결과 |
|------|------|----------------|------|
| 1 | **ogada 영업/운영 직원** (`platform_admin`) | `/platform` → 「고객 등록」→ 법인명·요금제 입력 | Tenant `행복주간보호` 생성 |
| 2 | `platform_admin` | 첫 관리자 계정 발급 (`kim@happy-care.com`, 역할 `hq_admin`) | 고객에게 로그인 정보 전달 |
| 3 | **행복주간보호 김센터장** (`hq_admin`) | 로그인 → 지점 등록·직원 계정 생성 | 센터 실제 운영 시작 |
| 4 | **행복주간보호 IT담당** (`sysadmin`) | `/settings` → 백업 설정·감사 로그 확인 | **행복주간보호 내부만** 관리 |

> 1~2번은 **ogada 직원**만. 3~4번은 **고객 센터 사람**만.

#### 역할별 「할 수 있는 일 / 없는 일」

| 행동 | `platform_admin` | `sysadmin` | `hq_admin` |
|------|-----------------|-----------|-----------|
| 새 센터 법인(Tenant) **등록** | ✅ | ❌ | ❌ |
| **전국** 가입 고객사 **목록** 보기 | ✅ | ❌ | ❌ |
| **자기 회사** 백업·기술 설정 | ❌ | ✅ | ❌ |
| **자기 회사** 이용자·출석 관리 | ❌ | ❌ | ✅ |
| **다른 센터** 이용자 데이터 보기 | ❌ | ❌ | ❌ |

#### 구현 선택 (A/B/C와 연결)

| 선택 | MVP에 넣을 화면 | 비고 |
|------|----------------|------|
| **A — ogada 직원이 등록** | `/platform` (고객 센터 등록 + 센터장 계정 발급) | planner **권장**, 전국 SaaS 표준 |
| **B — 센터 IT가 등록** | `sysadmin`에 등록 기능 추가 | 비권장 (보안·혼동) |
| **C — 센터 셀프 가입** | `/signup` 공개 가입 | 계약 전 무료 가입 위험, 후속 검토 |

> **확정 (2026-06-05)**: **A — ogada 직원**이 신규 고객 센터 등록 + 센터장 첫 계정 발급.  
> MVP에 `platform_admin` 역할 및 `/platform` 화면 포함.

### 1-3-1. 파일럿 운영 (사용자 확정: 2026-06-05)

| 항목 | 내용 |
|------|------|
| 파일럿 센터 | **있음** — 실제 운영 센터 |
| 지점 수 | **2곳** |
| 현장 사용 인원 | **센터장 1명** + **요양보호사 5명** |
| **표준 이용시간** | **08:00 ~ 20:00 (12시간)** — 사용자 확정 2026-06-07 |
| 활용 | 출석(수기·QR)·건강기록·청구·2지점 전환 UX 검증 |
| 파일럿 참여 역할 | **`branch_admin`(센터장) + `caregiver`(요양보호사)만** (2026-06-05 확정) |
| 파일럿 제외 | `hq_admin`·보호자·사회복지사 — MVP 구현은 하되 파일럿 현장 미참여 |

> **수가 1밴드 가정 (v1)**: 표준 이용시간 12시간 → NHIS 2026 수가 밴드 **10~13h** 적용 (§3-9-1). 부분 이용자(예: 6~8h만 이용)는 v1.1 다밴드(`duration_band`) 도입 시 분리.

#### 「테스트」가 무슨 뜻인가 (planner 정의)

여기서 **테스트**는 개발자의 자동화 테스트(pytest 등)가 **아니다**.

| 구분 | 뜻 | 예시 |
|------|-----|------|
| **개발 테스트** | 개발자·QA가 코드 검증 | API 호출 성공, 버튼 클릭 동작 |
| **파일럿 테스트** ← 여기서 말한 것 | **실제 센터 직원·보호자**가 만든 프로그램을 **진짜 업무처럼** 써 보고 피드백 | 요양보호사가 출석 입력, 보호자가 QR 스캔, 센터장이 청구서 확인 |

**왜 물었나** — 파일럿에서 **누가·무엇을** 써 볼지 알면, 화면·버튼·순서를 그 사람 기준으로 설계할 수 있다.

#### 파일럿 1주차 우선 업무 3가지 (planner 확정: 2026-06-07, 결정 57)

> 파일럿 참여 역할(`branch_admin`+`caregiver`)·일일 운영 루프·데이터 선행 관계 기준. **2주차 이후**: P4(지점 B 전환)·P5(대시보드)·P6–P8(월말 청구·NHIS).

| 순서 | 업무 | 담당 | 체크리스트 | 근거 |
|------|------|------|-----------|------|
| **1** | **이용자 등록 + 대표 보호자 1명 이상 연결** | 센터장 | P1 (US-D01) | 출석·건강·청구의 전제 데이터 |
| **2** | **수기 출석 체크인/아웃** (아침 10명 규모) | 요양보호사 | P2 (US-E01) | 파일럿 핵심 일일 업무·센터장·요양보호사 역할 분리 검증 |
| **3** | **일일 건강·투약 기록** | 요양보호사 | P3 (US-F01, F02) | 출석 직후 케어 기록 루프 — 청구·대시보드 입력 데이터 축적 |

> **제외(1주차)**: QR 출석(B방식)·보호자 초대(J01)·월말 청구(P6–P8) — merge·라이ve E2E 안정 후 2주차 이후.

#### develop→test merge 검증 우선 (사용자 확정: 2026-06-07, 결정 58)

| 스트림 | develop 상태 (64차 planner git 실측) | merge 전 선행 |
|--------|---------------------------|--------------|
| **backend** | HEAD **`767d977`** · tree **CLEAN** · `mvn test` **226/226 PASS** · test 대비 **20커밋 ahead** | ① develop→test merge(결정 54) ② **B03/SEC-D14** test 재검증 |
| **frontend** | HEAD **`73f7d39`** · tree **CLEAN** · `npm test` **179/58 PASS** · audit **0** · **40 Route·50 page** · test **`c510f5c`** · develop **9 ahead** | ① v1.3·v3 merge ② post-merge live E2E 권장(결정 73) |

> **ogada workspace submodule (73차)**: `src/backend` develop/local test @ **`598d108`** · **origin/test STALE `2799e29`**(QA-B12 push) · `src/frontend` @ **`7cd9293`** CLEAN — v1.2 merged @ test `c510f5c` · v1.3-A **local test merged** · v2 copay payment API @ `598d108`(develop-only) · UXD-54 QR·Transport `BranchScopeNotice` @ `7cd9293` · frontend **49 ahead** · SEC-D14 **origin push 후 재검증** · **`4be0938`/24 route 인용 폐기**(BNK-9).

> **원칙**: 테스트 PASS ≠ 이관 PASS — working tree clean + develop HEAD에 산출물 존재(이관 규율 5) 후 merge.

### 1-4. 배포 환경 (사용자 확정: 2026-06-05)

| 항목 | 결정 |
|------|------|
| 클라우드 벤더 | **무관** (AWS / GCP / NCP 등 구현 단계에서 선택) |
| 형태 | SaaS 멀티테넌트, 단일 클라우드 리전 운영 가정 |
| 원칙 | 클라우드 종속 최소화 — Docker + PostgreSQL 기준 이식 가능 구조 |

### 1-5. 벤치마킹·경쟁 분석

| 항목 | 내용 |
|------|------|
| 사용자 지정 참고 | **[케어포](https://www.carefor.co.kr/)** (carefor.co.kr) |
| 1차 조사 | 2026-06-05 (planner) |
| **2차 상세 조사** | **2026-06-06** (`benchmark_researcher` — 공식 사이트·매뉴얼·FAQ·공지 기반) |
| **3차 재검증** | **2026-06-06** — EZCARE 앱·NHIS `처리상태`열·롱텀 2026 개편·엔젤 CMS TCO |
| **6차 화면·메뉴 전수** | **2026-06-06** (BNK-6) — 케어포 12모듈→ogada route, **모듈 커버리지 ~25–30%**, v1.2 P0~P2 백로그 |
| **10차 이지케어 ERP** | **2026-06-09** (BNK-10) — `/new.ez` 로그인 게이트 · Channel.io·FAQ 역공학 · **계획/청구 이중 일정** · 급여·4대보험 lock-in |
| **11차 케어포 demo-work** | **2026-06-09** (BNK-11) — 시설급여 120메뉴 · **이동서비스 없음** · 주야간 **정본=func.php** · **G20** 시설특화 |
| **12차 baseline·가격** | **2026-06-09** (BNK-12) — ogada **`c7c8f07` 40 Route·35 page · ~74–78%** · 이지케어 **9,298** · v1.2.1 G14·대시보드 잔여 |
| **13차 func.php·7-x 1:1** | **2026-06-08** (BNK-13) — func.php **106 leaf** · 본인부담 **7-1~7-3 ogada Route ✅** · **7-6~7-10 리포트 5건 갭** → **US-M03 P1**(G22) · 1-3=기초평가(보호자=1-1 탭) |
| **14차 git 실측·US-M02/M01** | **2026-06-09** (BNK-14 + planner 78차) — ogada **`6d0a03a`/`d768820` 39 Route·36 page · ~68.7%** · US-M02 **닫힘** · G14 **GET API 잔여** · v2/G21 backend visits @ `d768820` |
| **16차 US-M03·FAQ 전수** | **2026-06-09** (BNK-16 + planner 80차) — ogada **`0a07799`/`1812165` 44 path·38 page · **72.5%** · US-M03(G22) **닫힘** · G7 NHIS **3상태 UX** P0 · 이지케어 **9,306**·FAQ payroll lock-in **37%** |
| **17차 방문요양·NHIS 3상태** | **2026-06-09** (BNK-17 + planner 81차) — ogada **`371794f`/`4cc328d` 45 path·39 page · **72.5%** · Epic V `/visits` FE 착수 · G7 **`PENDING_REVIEW`** BE 커밋 · #44 law.go.kr **2차 출처 충돌** · CMS=**효성CMS(FCMS)** |
| **18차 G7 폐루프 확정** | **2026-06-09** (BNK-18 + planner 82차) — ogada **`16402b2`/`dd49204` 45 path·39 page · **72.5%** · G7 **3상태 UX BE+FE 닫힘** · 케어포 `처리상태`열 **파싱 역전** · merge gate **8+6 FULLY UNBLOCKED** |
| **19차 대시보드 갭·케어포 2장** | **2026-06-10** (BNK-19 + planner 83차) — ogada **`6db762a`/`dd49204` · **72.5%** · G7 reconciliation **재확인** · **대시보드 `pendingReviewCount` P1** · merge **9+6 · WT clean 선행** |
| **20차 이지케어 역공학·RFID 폐기** | **2026-06-10** (BNK-20 + planner 84차) — G7 **엑셀=업계 표준** · **US-M02-b 닫힘** · G11 가산수가 P1 |
| **22차 알림 발송 이력 폐루프** | **2026-06-09** (BNK-22 + planner 86차) — **`NotificationHistoryPanel`** @ `e39164d` · 케어포 **10-7** 패리티 · **US-J03-h 닫힘** · **실발송(10-1) v1.1/v2** · merge **17 commits · BE+FE WT clean 선행** |
| **25차 엔젤·롱텀·규제** | **2026-06-09** (BNK-25 + planner 87차) — ogada **`e1320f4`/`ee3fa3a` 45 path·39 page · **72.5%** · **#44 이동서비스비 2차 교차 확정**(830/2,630/4,430/6,230) · **G17** 지표25+26 · **G21** NHIS visit import BE · **SEC-D17** apiFetch · merge **27 commits · FULLY UNBLOCKED** |
| **28차 func.php·G21/G2** | **2026-06-10** (BNK-28 + planner 88차) — ogada **`311c7c0`/`3e4d3e6` 45 path·39 page · **72.5%** · 케어포 func.php **97 leaf·리포트 44%** · **G21 확정↔import P1 닫힘** · **G2 notify API+UI** · **대기수급자 P2** · merge **40 commits · FULLY UNBLOCKED** |
| **31차 교차검증·G13 E2E** | **2026-06-10** (BNK-31 + planner 89차) — ogada **`14e9066`/`0ebe945` 45 path·39 page · **72.5%** · **G13 US-L02 pagination E2E 부분 닫힘** · **G21 visit 파서** @ `7fbd219` · **v3 meals/programs FE POST** @ `6a59b74` · G14·대시보드·#44·v2 CMS **번복 없음** · **G2 이메일 P1** · merge **52 commits · FULLY UNBLOCKED** |
| **35차 케어포 7-x·CMS** | **2026-06-10** (BNK-35 + planner 90차) — ogada **`e6df92c`/`2c6e57e` 45 path·39 page · **72.5%** · func.php **111 leaf·32 리포트(28.8%)** · **7-x 8/11** · **CMS BE stub** @ `2c6e57e` · **G2 email skeleton** @ `fbedcc3` · **US-M02-c 7위젯** · **G25 본인부담률 엑셀 P2** · merge **64 commits · FULLY UNBLOCKED** |
| **42차 G9·G2·US-J02** | **2026-06-10** (BNK-42 + planner 92차) — ogada **`eb3f0fd`/`f77a268` 46 path·40 page · **74.81%** · **G9 duration_band ✅** · **G2 templates 3종** @ `f77a268`+원화 `872e040` · **US-J02 filter/dedupe/retry ✅** · 이지케어 **9,308/9,231** · **가정 번복 0건** · merge **86 commits · FULLY UNBLOCKED** |
| **45차 #44 재정의·G2 +2** | **2026-06-10** (BNK-45 + planner 93차) — ogada **`eedcc80`/`0854fbd` 46 path·40 page · **74.81%** · **★ #44 이동지원≠이동서비스비** · **G2 templates 5종 partial** · **US-L01 overpayment guard ✅** · **G19 라벨 partial** @ `4c7c994` · 케어포 **46105** · 이지케어 **9,309** · merge **98 commits · FULLY UNBLOCKED** |
| **49차 G27·US-L01 bank·2-x** | **2026-06-10** (BNK-49 + planner 94차) — ogada **`c9451a0`/`467cd70` 46 path·40 page · **74.81%** · **★ G27 월한도액 BE catalog+guard ✅** @ `a92e625` · **US-L01 은행엑셀 BE ✅** @ `e50533f`/`95bb34d` · **US-M03-b 청구설정 ✅** · **케어포 2-x 11 leaf verbatim** → G15 v1.3-C 세부 갭 · **#44 수동 보류** · merge **110 commits · FULLY UNBLOCKED** |
| **53차 G11·G15 부분** | **2026-06-10** (BNK-53 + planner 95차) — ogada **`62f022df`/`d5e0e01` 46 path·40 page · **74.81%** · **★ G11 catalog+가이드 E2E ✅** · **★ G15 v1.3-C 부분 ✅** · merge **122 commits · FULLY UNBLOCKED** |
| **58차 G15·G11 v2·QA-B19** | **2026-06-10** (BNK-58 + planner 96차) — ogada **`6c4c151`/`d6d7e7f` 48 path·40 page · **74.81%** · **★ G15 2-2/2-3 ✅** · **★ 계약 서명 ✅** · **★ G11 v2 ✅** · **QA-B19 geocode UI WIP** · merge **133 · BE UNBLOCKED · FE BLOCK** |
| **66차 G16·G15 3-1·#44** | **2026-06-11** (BNK-65~66 + planner 98차) — ogada **`08dbcf0`/`dd7a580` 53 route·74 page · **75.77%** · **★ #44 공단 매뉴얼 1차 정본 ✅** md5 `3f92619c` · **★ G16 FE 닫힘** `VehiclesPage` @ `107bfb3` · **★ G15 3-1 연계 ✅** `CareProvisionRecordPanel`+BE @ `8bdead6` · **TSF npm 534/534 GREEN** · merge **158 · BE ready · FE BLOCK**(WT 4M) |
| **86차 US-R03 core·longterm drift·merge FULLY UNBLOCKED** | **2026-06-13** (BNK-128~131 + planner 116차) — ogada **`a018e71`/`82bdbcd` 61 route · **78.28%** · **★ US-R03 BE+FE+V86 wired** @ `75440bc`/`7243d21`/`9441a3c`/`a018e71` · **★ QA-B54/B55 Fixed** · **★ longterm.or.kr live 수가 셸 드리프트**(#44 29차·로컬 snapshot carry) · **★ LCMS 평가 SLA·CMS 3-method P2** · **★ 직원 lifecycle 문서/서식/4대보험 P2 잔여** · merge **335 · FULLY UNBLOCKED** |
| **130차 7-5 partial+·MOHW 2025-247·merge BLOCK** | **2026-06-14** (BNK-188~190 + planner 130차) — ogada **`bebd874`/`b893e97` 69 route · **78.28% carry** · **★ G41b V107 ✅** @ `ee42e5d` · **★ 7-5 간편결제 ✅ partial+** — skeleton+pilot E2E+prior-month guard @ `c9baca2`/`438f5c7`→`3848af6`/`1231389`→`bebd874`/`b893e97` · **★ MOHW 고시 2025-247 HTML** · **★ LCMS 평가 read-only role P3** · **★ silverangel 지표41/42 carry** · **QA-B78/B79 Planned** · merge **489 · BLOCK**(WT dirty) |
| **132차 7-5 full·J03 quiet-hours·merge BLOCK(FE)** | **2026-06-14** (BNK-191~194 + planner 132차) — ogada **`111f056`/`a057739` 69 route · **78.28% carry** · **★ 7-5 간편결제 ✅ full** — V110 integrity @ `16a0734`/`51f2505` → provider hardening @ `745a2f6`/`328874d` → route alias @ `8f9ad0c`/`7ec7cd4` · **★ J03 quiet-hours ✅ partial+** — FE billing-notify block @ `111f056` · BE dispatch+boundary @ `328874d`/`a057739` · **★ longterm 503 감경 evidence P3** · **★ #44 67차 carry** · **QA-B81/B82 Planned** · merge **500 · BLOCK(FE)** |
| **139차 L03 13/14 ✅ effective 100%·QA-B93 Planned·merge BLOCK** | **2026-06-15** (BNK-217~218 + planner 139차) — ogada **`89dc52d`/`6b0238a` 84 route·67 page · **78.28% carry** · V1–V125 · **★ L03 13/14 ✅ effective 100%** — M01/M06 FE @ `12591d4`/`2966447` · M07/M09/M10 rpt @ `2a05271`/`c23b1a3` · M15 rpt @ `75bddee` · M08 **N/A** · **★ func.php 4-x↔Route 5/5 closure** · **★ v1.3-B ✅ full carry** · **★ QA-B92 Fixed @ `2966447`** · **★ QA-B93 Planned**(EasyPay dirty-tree) · merge **566 · BLOCK(BE)** |
| **138차 v1.3-B ✅ full·L03_M01/M06 △ BE·merge UNBLOCKED** | **2026-06-15** (BNK-213~216 + planner 138차) — ogada **`3845f0c`/`a4352a8` 77 route·64 page · **78.28% carry** · V1–V124 · **★ v1.3-B ✅ full** — BE suggest @ `db94a65` + FE wire @ `2ffe59f` (BNK-214~216 · 결정 95) · **★ L03_M01/M06 △ BE shipped** — V123 @ `9bd1660` · V124 @ `a4352a8` · FE wire ❌ · **★ L03 BE 10/14 71%·FE 8/14 57%** · **★ US-UX-05 deepen** @ `edfba7f`/`3845f0c` · **★ US-R02 8-12 print** @ `e3e6964` · **★ 신규 P3 G-STAFF-COUNSEL**(FAQ21804) · **★ QA-B88/B89/B90 Fixed** · **QA Open 0건** · merge **555 · FULLY UNBLOCKED** |
| **141차 G-ONBOARD ✅·G24b ✅·merge UNBLOCKED** | **2026-06-15** (BNK-224~226 + planner 141차) — ogada **`92b9eff`/`f4c8beb` 84 route·67 page · **78.28% carry** · V1–V128 · **★ G-ONBOARD-SUPPORT ✅ full stack** @ `36264b5`/`4c1fd43`/`735dd53` · **★ G24b ✅ full stack** V128 @ `45fb6d9`/`49fbf67` · **★ P1 harness deepen** @ `fcabed0`/`8eed216` · **★ FAQ 21810/21814/21815** evidence · **★ QA-B94 Fixed @ `43c4b08`** · **QA Open 0건** · merge **589 · FULLY UNBLOCKED** |
| **148차 v1.3-A route preview·L02 rpt deepen** | **2026-06-16** (BNK-252~255 + planner 148차) — ogada **`388e1da`/`ae7e744` 94 route·75 page · V1–V141** · **★ v1.3-A Kakao Directions route preview map ✅ deepen** @ `0c523cd`/`d46688d`/`3eeac92`(carefor 2-2 대비 **지도 경로 미리보기·OR-Tools VRP 우위**·BNK-255) · **★ L02_M04/M05 rpt ✅ full+print** @ `c655743`/`c5f82a6`/`d2145b0` · **★ L02_M17 집중배설 rpt △ BE** @ `ae7e744` · **★ L02 leaf 8/15(53%)** · **★ #44 러-1~4 108차 zero drift** · **★ G-Payroll P3 carry**(ezCare dt#7) · **QA Open 0** · **QA-B95 Planned** · merge **312**(9 FE+303 BE) · ⚠ **live E2E verification BLOCK** |
| **150차 G26 7-8 통계 대시보드·FE merged+push·NHIS #44** | **2026-06-17** (BNK-262~268 + planner 150차) — ogada **`d8f1fdf`/`3481eb8` 100 route·81 page · V1–V142** · **★ G26 7-8 본인부담/의료비공제 통계 대시보드 ✅ full stack** @ `903f462`/`6d10e0d`(BE)·`d8f1fdf`(FE `/billing/reports/statistics`·PDF p.92 7-8 verbatim 1:1·결정 95 48~49회째) · **★ FE develop→test MERGED+origin/test PUSH** @ `d8f1fdf`(1504/1504 PASS) · **★ QA-B106 Fixed @ TSR 827** · **★ NHIS #44 118차 zero drift** · **★ silverangel 지표27 보호자회의 P3** · **★ func.php 117차 zero drift** · **QA Open 0(active)** · **QA-B95 Planned** · merge **315**(BE only) · ⚠ **live E2E verification BLOCK** |
| **156차 BNK-297 이지링크·G-COGNITIVE-WORKSHEET·merge FULLY UNBLOCKED** | **2026-06-18** (BNK-292~297 + planner 156차) — ogada **`825c6b0`/`8a1f342` 105 route·83 page · V1–V147** · **★ BNK-297 FAQ21764 이지링크(EzLink)** — 이지케어 NHIS 연동 = **설치형 PC 클라이언트**(구 smartaib4pc)·직원/수급자 등록·방문일정 가져오기 → ogada **web-first SaaS + 공단 엑셀 import = PC 에이전트 미의존 차별화 가정 강화**(신규 갭 아님) · **★ FAQ21781 인지활동지 출력 시범** → **G-COGNITIVE-WORKSHEET(=G29) P3 candidate** deepen(이지케어도 하반기 확장·MVP out-of-scope) · **★ QA-B115/B117/B118 Fixed** · **QA-B116 Planned**(merge pending 22·post-merge 재검증) · **QA-B95 Planned** · **★ 백본 zero drift carry**(NHIS #44 138차·func.php·silverangel·Channel.io plan-billing-diff) · **신규 갭 candidate 1·가정 번복 0** · merge **364 FULLY UNBLOCKED**(342 BE + 22 FE·양쪽 WT CLEAN) · ⚠ **live E2E verification BLOCK**(QA-B95 only) |
| **161차 BNK-323 G-STAFF-WORKLOG·BNK-322 G-HOSPITAL-ESCORT P3 candidate·G-CASH-RECEIPT deepen·QA-B127/QA-B128 Planned·merge BLOCK(420)** | **2026-06-17** (BNK-321~323 + planner 161차) — ogada **`188ce71`/`73cffc5` 106 route·85 page · V1–V151·V152 WIP** · **★ QA-B127 Planned**(develop HEAD **56 FAIL/1578 PASS**·DateInput/picker) · **★ QA-B128 Planned**(BE WT **DIRTY 1M+2U**·V152 WIP) · **★ BNK-323 G-STAFF-WORKLOG P3 candidate「 가정」**(FAQ21705 전 직종 출퇴근부/근무일지·ogada 선임 요보사 한정) · **★ BNK-322 G-HOSPITAL-ESCORT P3 candidate「 가정」**(angelsitter #781 병원동행 시범·주·야간보호형 참여 가능) · **★ BNK-323 G-CASH-RECEIPT deepen**(FAQ21702/21701) · **★ BNK-321** DatePicker/TimeInput+desiredBoarding ETA WIP · NHIS #44 zero drift · **QA Open 0(active)** · **QA-B116 Planned**(merge 420) · **QA-B95 Planned** · **신규 갭 candidate +2· 가정 번복 0** · merge **420 BLOCK**(53 FE + 367 BE) · ⚠ **live E2E verification BLOCK**(QA-B127+QA-B128+QA-B116+QA-B95) |
| **162차 BNK-334 silverangel 6종 zero drift·CMS parity·QA-B131 Planned·merge FULLY UNBLOCKED(3 FE+1 BE)** | **2026-06-18** (BNK-333~334 + planner 162차) — ogada **`7d2cb4a`/`09df8c7` 106 route·84 page · V1–V152** · **★ QA-B127/B128/B129/B130 Fixed** · **★ QA-B131 Planned**(MEDIUM·`npm run test:live-e2e` script path·workaround **122 PASS/19 SKIP**) · **★ BNK-334** silverangel 정본 **6종 URL zero drift**·CMS 3-method **ogada `/billing/cms` parity**·이동서비스 **통합 허브**(`/transport/compliance`) vs 엔젤 이중 트랙 **우위** · **★ BNK-333** carefor func **107-leaf**·**7-x Route 1:1 closed**·demo 이동서비스 **0** · NHIS #44 **164차 zero drift** · **가정 번복 1**(silverangel URL probe 오류) · **신규 갭 0** · **QA Open 0(active)** · **QA-B116 Planned**(3 FE+1 BE local) · **QA-B95 Planned** · merge **FULLY UNBLOCKED**(3 FE+1 BE local·양쪽 WT CLEAN) · ⚠ **operation BLOCK**(QA-B131+origin/test push+QA-B95) |
| **164차 BNK-347 G15 partial+++·G21 RFID 7-code·QA-B135 Fixed·merge local SYNCED** | **2026-06-18** (BNK-342~347 + planner 164차) — ogada **`1c8f236`/`d7f1a9a` 106 route·84 page · V1–V154** · **★ QA-B135 Fixed @ `d7f1a9a`** · **★ BNK-347** NHIS #44 **175차 zero drift**·엔젤 지표41/42 ↔ G15 **partial+++**·**driver signature full-stack** @ `f51e365`/V154 · **★ BNK-346** `schedule-rfid` **7-code diff matrix** → G21 **P1** · **4축 번복 0** · **신규 갭 0** · **QA Open 0(active)** · **QA-B116 Planned**(merge EXECUTED local·post-merge PASS) · **QA-B95 Planned** · merge **local SYNCED**·**402 vs origin/test**(18 FE+384 BE) · ⚠ **operation BLOCK**(origin/test push+QA-B95) · **P2 Must**: 일지④ **인쇄·별지 제22호 전항목** · **P1**: G21 RFID 7-code matrix |
| **191차 BNK-551~552 US-R01-c leave-ledger BE ✅ FE wire △·v1.3-C M2 차별화·QA-B272/B273 Planned·merge gate 718 BLOCK** | **2026-06-23** (BNK-551~552 + planner 191차) — ogada **`8057c1e`/`5fd12dd` 111 route·89 page · V1–V174 · BE Test 251 · FE test 450 · 모듈 **78.79%** · merge gate **718** · **★ US-R01-c leave-ledger BE ✅ FE wire △** @ `bb9df48`/`5fd12dd`/`8057c1e` · **relatedSurfaces BE AVAILABLE ↔ FE PLANNED 동기화 P1**(BNK-551) · **★ v1.3-C M2 10-leaf 8✅·2△·+3 superset·demo transport nav 0** = **P2 마케팅 차별화** · **★ P3 deepen**: G-TRANSPORT-TIME-SYNC·G-VISIT-RESERVATION·G-NFC-NIGHT-PATROL·G-REPORT-DENSITY · **★ QA-B272/B273 Planned** · **4축 가정 번복 0** · **신규 core 갭 0** · **QA Open 0(active)** · merge **718** · cross-stream **BLOCK** · live E2E **127 PASS/19 SKIP** · ⚠ **disk 100% ENOSPC** · ⚠ **operation BLOCK** |
| **190차 BNK-540~541 M6 v3.1 P1 재확인·US-R01 relatedSurfaces 차별화·leave-ledger P1 candidate·QA-B255/B263/B264 Fixed·merge gate 710 SYNCED** | **2026-06-23** (BNK-540~541 + planner 190차) — ogada **`95f55aa`/`83a26e7` 111 route·89 page · V1–V173 · BE Test 247 · FE test 449 · 모듈 **78.79%** · merge gate **710** · **★ M6 위생·시설관리 5-leaf v3.1 P1 재확인**(6-1 `/meals` LIVE·6-2~6-4 `/safety/*` PLANNED·**신규 core 갭 0**) · **★ US-R01 relatedSurfaces 양방향 closure 재입증**(정보 모델 투명성 **차별화 우위**) · **★ v3 `/staff/leave-ledger` P1 candidate「가정」**(US-R01-c·BNK-532) · **★ QA-B255/B263/B264 Fixed** · **★ FE test KPI 449 정본** · **4축 가정 번복 0** · **QA Open 0(active)** · merge **710** · cross-stream **SYNCED** · live E2E **127 PASS/19 SKIP** · ⚠ **operation BLOCK** |
| **188차 BNK-515~519 G2-CMS-ENROLLMENT-ROSTER ✅·G34-WORKFLOW-CATALOG ✅·G-STAFF-ANNUAL-LEAVE P3·QA-B248 Planned·merge gate 685 BLOCK(BE)** | **2026-06-22** (BNK-515~519 + planner 188차) — ogada **`3ece965`/`d3d4d2d` 110 route·89 page · V1–V171 · BE Test 243 · FE test 443 · 모듈 **78.79%** · merge gate **685** · **★ G2-CMS-ENROLLMENT-ROSTER ✅ full-stack closure** @ `df9ec6c`→`3ece965`(FE branch roster·FilterChips·payment links) + BE `@d0c0d12`/`@d3d4d2d` · **★ G34-WORKFLOW-CATALOG ✅ full-stack closure** @ `77cfc38`(`/compliance/workflow-catalog`) · **★ G-STAFF-ANNUAL-LEAVE P3 candidate**(BNK-516·ezCare worker-b100 tab01) · **★ FE test KPI 443 정본**(BNK-519) · **★ QA-B247~B250 Fixed(FE)** · **★ QA-B248 Planned**(BE merge pending 2) · **4축 가정 번복 0** · **백본 311~312차 zero drift** · **신규 core 갭 0** · **QA Open 0(active)** · merge **685** · cross-stream **BLOCK(BE)/FE SYNCED** · live E2E **126 PASS/19 SKIP** · ⚠ **operation BLOCK** |
| **187차 BNK-505~507 M7 10/10+superset ✅·G34-WORKFLOW-CATALOG·G30-LEGEND P3·QA-B239 Fixed·QA-B240 Planned·merge gate 674 BLOCK(FE)** | **2026-06-22** (BNK-505~507 + planner 187차) — ogada **`d058e43`/`9db0bbb` 109 route·87 page · V1–V171 · BE Test 242 · FE test 438 · 모듈 **78.79%** · merge gate **674** · **★ M7 demo L07 `cost_*` 10/10 ↔ `/billing/*` + 7 superset ✅** @ `d058e43`/`9db0bbb`(BNK-506) · **M4 물리 out-of-scope** · **★ G34-WORKFLOW-CATALOG P3 candidate**(ezCare FAQ 21795–21828 15/28 verbatim·13건 미인용) · **★ G30-LEGEND P3 candidate**(`MonitoringItemCatalog` ↔ 공단 평가지표 1-15 cross-walk MAP) · **guide-E200 SaaS+컨설팅 v2/v3 monetization out-of-scope** · **★ US-D03 attendance tab API wire** @ `d058e43` · **★ QA-B239 Fixed @ `9db0bbb`** · **★ QA-B240 Planned**(FE merge pending 1) · **4축 가정 번복 0** · **백본 299~301차 zero drift** · **신규 core 갭 0** · **QA Open 0(active)** · merge **674** · cross-stream **BLOCK(FE)/BE SYNCED** · live E2E **126 PASS/19 SKIP** · ⚠ **operation BLOCK** |
| **186차 BNK-491~493 모듈 78.79% KPI·G-BILLING 3-channel guard·report filter persist BE·QA-B222 Fixed·merge gate 661 SYNCED(BE)** | **2026-06-22** (BNK-491~493 + planner 186차) — ogada **`dffd726`/`479995e` 109 route·87 page · V1–V170 · BE Test 241 · FE test 436 · 모듈 **78.79%** · merge gate **661** · **★ G-BILLING-DEPOSIT-ORDER-GUARD ✅ 3-channel uniform** @ `abddbee`/`dfa981c`(manual+CMS+EasyPay·케어포 PDF p.85) · **★ G-BILLING-REPORT-FILTER-PERSISTENCE △ BE partial** @ `479995e`(V170·GET/PUT filters·FE wire ❌ P2) · **★ US-E05 API contract △ partial** @ `dffd726` · **★ QA-B222 Fixed @ `5fd468b`** · **★ QA-B229~B231 Fixed carry** · **4축 가정 번복 0** · **백본 4-URL 289차 zero drift** · **신규 core 갭 0** · **QA Open 0(active)** · merge **661** · cross-stream **SYNCED(BE)/FE merge pending 1** · live E2E **126 PASS/19 SKIP** · ⚠ **operation BLOCK** |
| **185차 BNK-477~480 모듈 78.45% KPI·출석 roster superset·NHIS #44 parity·QA-B222 Planned·merge gate 647 BLOCK(FE)** | **2026-06-21** (BNK-477~480 + planner 185차) — ogada **`8383f8d`/`61e1970` 107 route·87 page · V1–V168 · BE Test 237 · FE test 432 · 모듈 **78.45%** · merge gate **647** · **★ 모듈 78.45% KPI 정본**(29 feature·✅20·△4·❌5 out-of-scope) · **★ G-ATTENDANCE-ROSTER-STATUS ✅ superset** @ `0c69060`/`@61e1970` · **★ module 8 0.75→0.8**(US-R03 mobile) · **★ NHIS #44 G16 parity 재입증** · **★ module 7 11/11 Route 1:1** · **★ QA-B223 Fixed @ `61e1970`** · **QA-B222 Planned**(vitest hang·FE merge pending 3) · **4축 가정 번복 0** · **백본 4종 276차 zero drift** · **신규 core 갭 0** · **QA Open 0(active)** · merge **647** · cross-stream **BLOCK(FE hang)** · ⚠ **operation BLOCK** |
| **184차 BNK-470~471 G-STAFF-DOCUMENT-REPOSITORY △→✅ full-stack·G-BATHING ✅ full-stack carry·G-MENU-PERMISSION-MATRIX P3 신규·4축 번복 0·merge gate 634 SYNCED** | **2026-06-21** (BNK-470~471 + planner 184차) — ogada **`fd15a2f`/`b583c11` 108 route·87 page · V1–V167 · BE Test 236 · FE test 431** · **★ G-STAFF-DOCUMENT-REPOSITORY P3 △→✅ FULL-STACK closure ✅** @ `03d0d43`/`fd15a2f`/`b583c11` — 21-slot `StaffDocumentRepositoryPanel`+`GET /staff/hr-files/users/{userId}/repository-progress`·케어포 PDF p.96 zone③ 20-doc + FAQ21825 lifecycle **21-slot superset** · **470차 P3 candidate 제거** · **★ G-BATHING copy-from-previous-month ✅ full-stack carry ✅** @ `9a957fb`/`a426663`(BNK-466 closure·183차 BE partial 정정) · **★ 신규 G-MENU-PERMISSION-MATRIX P3「가정」**(FAQ21695 계정×메뉴 fine-grained·v3 enterprise·MVP out-of-scope) · **★ 4축 가정 번복 0** · **백본 3종 268차 zero drift** · **신규 core 갭 0** · **QA Open 0(active)** · **★ QA-B209~B214 Fixed carry** · merge **634**(FE141+BE493) · live E2E **126 PASS/19 SKIP** · ⚠ **operation BLOCK**(origin/test push 493 BE+141 FE+QA-B95) · **P3 carry**: G-MENU-PERMISSION-MATRIX · G-STAFF-DOCUMENT mobile upload · G30 자가진단↔현장 점수 비교 · G-COMM-CALLER-AUTH(6/23) · G-ORAL-CARE-PERIOD-REPORT · module 8 PDF workflow |
| **183차 BNK-464~465 G15-KAKAO-QUOTA-DASH △→✅·G-BATHING BE API △→✅ partial·4축 번복 0·QA-B204 Planned·merge gate 623 BLOCK(BE)** | **2026-06-21** (BNK-464~465 + planner 183차) — ogada **`a8ccb04`/`49a1721` 108 route·87 page · V1–V166 · BE Test 232 · FE test 429** · **★ G15-KAKAO-QUOTA-DASH △→✅ closure ✅** @ `580a86b`/`a8ccb04` — HQ dashboard 4-tone widget·**ogada exclusive**(BNK-464) · **177차 P3 candidate 제거** · **★ G-BATHING copy-from-previous-month BE API △→✅ partial ✅** @ `49a1721` · **FE wire ❌ → P2 backlog** · **★ 4축 가정 번복 0** · **백본 4종 263차 zero drift** · **신규 core 갭 0** · **QA Open 0(active)** · **QA-B204 Planned**(BE merge pending 1) · **★ QA-B195~B205 Fixed carry** · merge **623**(FE135+BE488) · live E2E **126 PASS/19 SKIP** · ⚠ **operation BLOCK**(QA-B204+origin/test push 488 BE+135 FE+QA-B95) · **P2 carry**: G-BATHING-SCHEDULE-PREV-MONTH-COPY FE wire · **P3 carry**: G-COMM-CALLER-AUTH(6/23) · G-ORAL-CARE-PERIOD-REPORT · module 8 PDF workflow |
| **182차 BNK-456~458 G-BILLING 3건 △→✅ full-stack·G32 FAQ21740 parity deepen·QA-B195/B196/B192 Planned·QA-B193/B194 Fixed·merge gate 612 BLOCK** | **2026-06-21** (BNK-456~458 + planner 182차) — ogada **`cb3fe3d`/`7b99313` 108 route·87 page · V1–V166 · BE Test 232 · FE test 425** · **★ G-BILLING deposit half-month + receipt dual-basis △→✅ full-stack closure ✅** @ `e38ccfd`/`375fb9d`/`b96d038` · **★ G-BILLING appliedFilters FE wire △→✅ full-stack closure ✅** @ `c6a412f`/`14935a3`/`7b99313` · **180차 P3 candidate 3건 제거** · **★ G32 FAQ21740 반기별 1회 parity deepen ✅**(BNK-458) · **★ module 8 PDF p.98–105 cross-walk**(8-3/8-6/8-8 P3 carry) · **★ func.php 258차 zero drift** · **신규 core 갭 0** · **QA Open 0(active)** · **QA-B195/B196/B192 Planned** · **★ QA-B193 Fixed @ `7b99313`** · **★ QA-B194 Fixed @ `c6a412f`** · merge **612**(FE128+BE484) · develop HEAD **1916/1917 FAIL(1)** · live E2E **126 PASS/19 SKIP** · ⚠ **operation BLOCK**(QA-B195+QA-B196+QA-B192+origin/test push 482 BE+127 FE+QA-B95) · **P3 carry**: G-COMM-CALLER-AUTH(6/23) · G-BATHING-SCHEDULE-PREV-MONTH-COPY · G-ORAL-CARE-PERIOD-REPORT · G15-KAKAO-QUOTA-DASH · module 8 PDF workflow |
| **181차 BNK-447~452 G-STAFF-LEAVE-STATUS △→✅ full-stack·4축 가정 번복 0·신규 candidate G-COMM-CALLER-AUTH P3·QA-B187/B188 Planned·QA-B186 Fixed·merge gate 602 BLOCK(FE+BE)** | **2026-06-21** (BNK-447~452 + planner 181차) — ogada **`2581347`/`1d7cee2` 108 route·87 page · V1–V166 · BE Test 230 · FE test 424** · **★ G-STAFF-LEAVE-STATUS △→✅ full-stack closure ✅**(`STAFF_LIFECYCLE_STATUS.ON_LEAVE`+CHECK `V166` @ `1d7cee2` · `StaffLifecyclePanel` 휴직 Badge @ `2581347` · `StaffLifecycleSummaryPanel`+`GET /api/v1/staff/lifecycle-summary` `onLeaveCount` · 복직 regression · **180차 P3 candidate 제거**) · **★ 4축 교차검증(G14·대시보드/G26·v1.3-C·v2 CMS) 가정 번복 0**(P0/P1 재정렬 없음·baseline 안정) · **★ 신규 candidate G-COMM-CALLER-AUTH P3「가정」**(silverangel notice 221562 발신번호 본인인증 마감 2026-06-23·MVP out-of-scope·SMS 9-event만 ✅) · **★ G-BANK-EXCEL-8 BE row guard ✅+**(BNK-448) · **★ 백본 6종 zero drift 254차** · **★ longterm 502/503 5th cycle stable** · **신규 core 갭 0** · **QA Open 0(active)** · **★ QA-B186 Fixed @ `82a542c`** · **QA-B187 Planned**(BE merge pending 2 @ `1d7cee2`+`68d4457`)·**QA-B188 Planned**(FE merge pending 2 @ `2581347`+`e45df26`) · **QA-B116 Planned**(origin/test push **478 BE+120 FE**) · **QA-B95 Planned** · merge **602**(FE122+BE480·FE+BE merge pending 2) · live E2E **126 PASS/19 SKIP** · ⚠ **operation BLOCK**(QA-B187+QA-B188+origin/test push+QA-B95) · **P3 carry**: G-COMM-CALLER-AUTH(신규·6/23 마감) · G-BILLING-DEPOSIT-HALFMONTH-REPORT · G-BILLING-RECEIPT-DUAL-BASIS · G-BATHING-SCHEDULE-PREV-MONTH-COPY · G-ORAL-CARE-PERIOD-REPORT · G15-KAKAO-QUOTA-DASH |
| **180차 BNK-445~446 G-BANK/G-STAFF-NHIS ✅ full-stack·신규 P3 +3·QA-B182 Planned·QA-B181 Fixed·merge gate 590 BLOCK(BE)** | **2026-06-21** (BNK-445~446 + planner 180차) — ogada **`a18b30e`/`7d29a38` 108 route·87 page · V1–V165 · BE Test 228 · FE test 422** · **★ G-BANK-EXCEL-8 ✅ full-stack closure ✅**(BE 8-bank catalog+preview+import @ `e3b74a0`/`2f6f3bc` · FE `BankDepositImportPanel` @ `a18b30e` · BE hardening non-positive row guard @ `7d29a38` merge pending QA-B182) · **★ G-STAFF-NHIS-EXCEL-IMPORT ✅ full-stack closure ✅** @ `4315ee2`/`2f6f3bc`(FE `StaffNhisCaregiverImportPanel`+BE preview/import) · **★ BNK-445~446 billing PDF p.91** — 입금대장 반월 split·수납대장 2-track → **신규 P3 G-BILLING-DEPOSIT-HALFMONTH-REPORT·G-BILLING-RECEIPT-DUAL-BASIS** · **★ BNK-446 FAQ21720** — ON_LEAVE enum gap → **신규 P3 G-STAFF-LEAVE-STATUS** · **백본 zero drift** · **QA Open 0(active)** · **★ QA-B181 Fixed @ `a18b30e`** · **QA-B182 Planned**(BE merge pending 1 @ `7d29a38`) · **QA-B116 Planned**(origin/test push **475 BE+115 FE**) · **QA-B95 Planned** · merge **590**(FE SYNCED·BE merge pending 1) · live E2E **145 SKIP/0 PASS** · ⚠ **operation BLOCK**(QA-B182+origin/test push+QA-B95) · **P3 carry**: G-STAFF-LEAVE-STATUS · G-BILLING-DEPOSIT-HALFMONTH-REPORT · G-BILLING-RECEIPT-DUAL-BASIS · G-BATHING-SCHEDULE-PREV-MONTH-COPY · G-ORAL-CARE-PERIOD-REPORT · G15-KAKAO-QUOTA-DASH |
| **179차 BNK-435~441 G-BILLING-PRIOR-DEPOSIT-GUARD ✅ closure·G-BANK/G-STAFF-NHIS △ BE partial·QA-B178 Planned·QA-B177 Fixed·merge gate 581 BLOCK(BE)** | **2026-06-20** (BNK-435~441 + planner 179차) — ogada **`a0f051d`/`6f7f145` 108 route·87 page · V1–V164 · BE Test 227 · FE test 421** · **★ G-BILLING-PRIOR-DEPOSIT-GUARD ✅ closure ✅**(BNK-436 dashboard widget+API @ `0d233b9`/`07a03c0`/`07a03c0`) · **★ G-BANK-EXCEL-8 △ BE partial** @ `07a85a3`/`6f7f145`(8-bank catalog+preview+import API·FE wire ❌) · **★ G-STAFF-NHIS-EXCEL-IMPORT △ BE partial** @ `6f7f145`(NHIS caregiver excel preview+import·FE wire ❌) · **★ BNK-441 module3 PDF workflow** — func 107-leaf·demo nav 0·7-x 10/10·리포트 15.0% · **★ 신규 candidate G-BATHING-SCHEDULE-PREV-MONTH-COPY·G-ORAL-CARE-PERIOD-REPORT P3** · **백본 zero drift** · **QA Open 0(active)** · **★ QA-B177 Fixed @ `a0f051d`** · **QA-B178 Planned**(BE merge pending 1) · **QA-B116 Planned**(origin/test push **469 BE+111 FE**) · **QA-B95 Planned** · merge **581**(FE SYNCED·BE merge pending 1) · live E2E **126 PASS/19 SKIP** · ⚠ **operation BLOCK**(QA-B178+origin/test push+QA-B95) · **P2 carry**: G-BANK-EXCEL-8 FE wire · G-STAFF-NHIS-EXCEL-IMPORT FE wire · G15-KAKAO-QUOTA-DASH · **P3 carry**: G-BATHING-SCHEDULE-PREV-MONTH-COPY · G-ORAL-CARE-PERIOD-REPORT · G-LTM-DIRECT-SYNC · G-PROVIDER-CHANGE-COUNSEL · G24 총평 전용 필드 |
| **178차 BNK-432~434 G14 plan-form △→✅ closure·G24 FAQ21800 parity·QA-B169~B172 Fixed·merge gate 569 SYNCED** | **2026-06-20** (BNK-432~434 + planner 178차) — ogada **`d723d5a`/`80b9619` 108 route·86 page · V1–V164 · BE Test 224 · FE test 419** · **★ BNK-433 G14 plan-form △→✅ closure ✅**(V164·`ClientCarePlanFormService`·10 NHIS fields BE @ `34eb47a`/`80b9619` · FE `ClientCarePlanFormPage`·Route `/clients/:clientId/care-plan-form` @ `ce422e3`/`d723d5a` · FAQ21802 cross-walk ✅ · **신규 갭 0**) · **★ BNK-434 G24 FAQ21800 8/8 parity ✅** + fiscal year compliance · 총평 전용 필드 △(`homeVisitNotes`) → **P3 carry** · **★ BNK-432 v2 infra** V161 HQ admin single·V162 user account requests·V163 Korean legal districts seed @ `80b9619` · **★ 신규 candidate G-BILLING-PRIOR-DEPOSIT-GUARD P2「가정」**(carefor PDF p.85 「7-1 청구 전 7-2 선행 입금」) · **★ G-BANK-EXCEL-8 P3「가정」**(PDF p.88 은행 8종 일괄입금 엑셀) · **★ G15-KAKAO-QUOTA-DASH P3 carry**(BE tracker ✅ @ `80b9619`·FE widget ❌) · **백본 zero drift** · **QA Open 0(active)** · **★ QA-B169/B170/B171/B172 Fixed** @ `3023c9e`/`c37228d`/`80b9619`/`d723d5a` · **QA-B116 Planned**(origin/test push **464 BE+105 FE**) · **QA-B95 Planned** · merge **569 SYNCED(local)** · live E2E **122 PASS/23 SKIP** · ⚠ **operation BLOCK**(origin/test push+QA-B95) · **P2 carry**: G-BILLING-PRIOR-DEPOSIT-GUARD · G15-KAKAO-QUOTA-DASH · **P3 carry**: G-BANK-EXCEL-8 · G-LTM-DIRECT-SYNC · G-PROVIDER-CHANGE-COUNSEL · G24 총평 전용 필드 |
| **177차 BNK-424~429 G15-KAKAO-INTEGRATION 6-layer 우위·Kakao API status panel·quota tracker WIP·QA-B169/B170 Planned·merge gate 555 BLOCK(FE+BE)** | **2026-06-20** (BNK-424~429 + planner 177차) — ogada **`ba74bb5`/BE `@e2b764b` 107 route·86 page · V1–V159 · BE Test 221 · FE test 416** · **★ BNK-429 G15-KAKAO-INTEGRATION 6-layer 우위 ✅ 재확정**(케어포 postcode 1-layer only vs ogada postcode+Maps+Geocoding+Directions+API status panel+quota tracker WIP) · **★ TransportKakaoApiStatusPanel** FE @ `ba74bb5` · **★ KakaoRestApiUsageTracker** BE WIP(4U untracked @ `e2b764b`) · **★ 신규 candidate G15-KAKAO-QUOTA-DASH P3「가정」**(quota tracker UI 대시보드 위젯화·BE commit 후 P2 승격 검토) · **★ FAQ21832 HR payroll out-of-scope N/A** · func.php module 2 cross-walk ✅5·✅+3·△4·❌0 · **신규 갭 0** · **QA Open 0(active)** · **QA-B169 Planned**(BE WT DIRTY 9M+4U·merge pending 1) · **QA-B170 Planned**(FE test post-merge 5 FAIL·develop 1856/1856 PASS) · **★ QA-B163 Fixed @ `94f2535`** · **★ QA-B167 Fixed @ `ba74bb5`** · **QA-B116 Planned**(origin/test push **456 BE+97 FE**) · **QA-B95 Planned** · merge **555**(FE98+BE457) · live E2E **126 PASS/19 SKIP** · ⚠ **operation BLOCK**(QA-B169+QA-B170+push+QA-B95) · **P3 carry**: G15-KAKAO-QUOTA-DASH · G-CASH-RECEIPT-NTS-API · G-PROVIDER-CHANGE-COUNSEL |
| **176차 BNK-419~423 G-CASH-RECEIPT-LOG end-to-end 재입증 ✅·FAQ21823 partial+·QA-B163 Planned·merge gate 543 BLOCK(FE)** | **2026-06-20** (BNK-419~423 + planner 176차) — ogada **`16afd4c`/BE `@bfad37d` 107 route·86 page · V1–V159 · BE Test 218 · FE test 414** · **★ BNK-423 G-CASH-RECEIPT-LOG full-stack end-to-end 재입증 ✅**(V158/V159·API 4·FE 3컴포넌트·테스트 6) · **★ FAQ21823 △ partial+** @ `1b6d2b1`/`033b319`/`16afd4c`(5항 checklist·서식 modal·lifecycle tab·renewal record) · **★ BNK-422** Channel.io fd80da95 G-PROVIDER-CHANGE-COUNSEL P3 · **★ BNK-421** 케어포 module 10 P3 candidates G-CLIENT-PHOTO-ALBUM·G-NOTICE-BOARD·G-BULK-SMS · **신규 갭 0** · **QA Open 0(active)** · **QA-B163 Planned**(FE 2 FAIL panel test) · **★ QA-B159 Fixed @ `bfad37d`** · **QA-B116 Planned**(origin/test push **453 BE+90 FE**) · **QA-B95 Planned** · merge **543**(BE SYNCED·FE merge pending 2) · live E2E **126 PASS/19 SKIP** · ⚠ **operation BLOCK**(QA-B163+push+QA-B95) · **P3 carry**: G-CASH-RECEIPT-NTS-API · G-PROVIDER-CHANGE-COUNSEL · G-CLIENT-PHOTO-ALBUM |
| **175차 BNK-417~418 케어포 module 7 11/11 ✅·FAQ21823 근로계약 갱신 △·QA-B159 Planned·merge gate 533 BLOCK(BE)** | **2026-06-20** (BNK-417~418 + planner 175차) — ogada **`f31c346`/BE develop `beef81e` 107 route·86 page · V1–V158 · BE Test 217 · FE test 413** · **★ BNK-417** 케어포 module 7 **11/11 ✅ + superset 2**(G33 청구시작·G26 통계) · module 11 **6/6 HR payroll out-of-scope** · **★ FAQ21823 `StaffEmploymentContractRenewalPanel` △ partial** @ `f62402f`/`f31c346`(근로계약 renewal summary+대시보드 widget·급여대장 0) · **★ BNK-418** ezCare **7e0734fa** 시급→급여 4-Track = **재가 HR out-of-scope** · **bc7f4cd9** 검은/빨간 = ogada G21 **✅+ carry** · **백본 235~236차 zero drift** · **신규 갭 0** · **QA Open 0(active)** · **QA-B159 Planned**(BE merge pending 2 @ `7a9d7a5`·`beef81e`) · **QA-B116 Planned**(origin/test push **448 BE+85 FE**) · **QA-B95 Planned** · merge **533**(FE SYNCED·BE merge pending 2) · live E2E **126 PASS/19 SKIP** · ⚠ **operation BLOCK**(QA-B159+push+QA-B95) · **P3 carry**: G-HOURLY-WAGE-SCHEDULE-REUPLOAD · G-CASH-RECEIPT-NTS-API · G-PROVIDER-CHANGE-COUNSEL · module 11 payroll |
| **174차 BNK-408~412 G26/G-7-1 closure·G-CASH-RECEIPT-LOG 6-계층 deepen·QA-B157 Planned·merge gate 522 BLOCK(BE)** | **2026-06-20** (BNK-406~412 + planner 174차) — ogada **`99b795a`/BE develop `35d1560` 107 route·86 page · V1–V158 · BE Test 216 · FE test 409** · **★ G26 `@19ed7f3` yearBasis(PAID_YEAR/CLAIM_YEAR)+NTS CSV export ✅ full-stack**(BNK-408·G-CASH-RECEIPT-TAX-DEDUCTION-EXPORT **△→✅ 해소**) · **★ G-7-1 Excel `@58d6694`/`@e454d3b` ✅**(BNK-409·PDF p.87 ② parity) · **★ G-CASH-RECEIPT-LOG 6-계층 deepen** — UXD-139 a11y(BNK-407) + pending error guard `@99b795a`(BNK-411) + identifier 검증 `@35d1560`(BNK-412) · **★ 신규 candidate G-PROVIDER-CHANGE-COUNSEL P3「가정」**(BNK-410 FAQ21795·재가 out-of-scope) · **★ 8축 교차검증 가정 번복 0** · **백본 227/229차 zero drift** · **QA Open 0(active)** · **QA-B157 Planned**(BE merge pending 1) · **QA-B116 Planned**(origin/test push **442 BE+79 FE**) · **QA-B95 Planned** · merge **522**(FE SYNCED·BE merge pending 1) · live E2E **126 PASS/19 SKIP** · ⚠ **operation BLOCK**(QA-B157+push+QA-B95) · **P3 carry**: G-CASH-RECEIPT-NTS-API · G-PROVIDER-CHANGE-COUNSEL · G-LTM-DIRECT-SYNC |
| **173차 BNK-405 G-CASH-RECEIPT-LOG 4-계층 closure·QA-B153/B154 Fixed·merge gate 511 SYNCED** | **2026-06-20** (BNK-399~405 + planner 173차) — ogada **`8aebe55`/`58ff35e` 107 route·86 page · V1–V158** · **★★★ G-CASH-RECEIPT-LOG 4-계층 full-stack closure ✅**(172차 P2 gap → closure·**신규 갭 0**) — ① `/billing/cash-receipts` + V158 @ `cfc4b04`/`f79a19e` ② 수납 prompt @ `a17f148` ③ 대시보드 due-gate @ `221458e`/`fe54af8` ④ HQ pending + prior-year @ `58ff35e`/`8aebe55` · **QA Open 0(active)** · **★ QA-B153/B154 Fixed** · **QA-B116 Planned**(origin/test push **437 BE+74 FE**) · **QA-B95 Planned** · merge **511 SYNCED** · ⚠ **operation BLOCK** |
| **172차 BNK-398 신규 갭 G-CASH-RECEIPT-LOG P2·QA-B150/B151/B152 Fixed·merge gate 498 SYNCED** | **2026-06-19** (BNK-393~398 + planner 172차) — ogada **`9b80505`/`caeac0d` 106 route·85 page · V1–V157** · **★★★ 신규 갭 1 G-CASH-RECEIPT-LOG P2「확인」** — 이지케어 FAQ 21701 「2.수급자 > 2.10 현금영수증 발급목록」+「현금영수증 발급정보 관리」(목록+수급자별 NTS 상세) = 수급자 모듈 **별도 메뉴** ↔ ogada `/billing/reports/receipts`(BillingReportPage variant=`receipts`·**수납 ledger only**)·`MedicalExpenseDeductionPanel`(연말정산 NTS XLSX·연 1회) → **per-payment NTS 발급 이력 ❌** · FAQ 21716(납입 즉시·몰아서 ❌)·FAQ 21717(작년분 발급 가능·올해 연말정산 ❌·종합소득세 별도) = NTS lifecycle 법적 제약 → **G-CASH-RECEIPT P3 승격**(`cash_receipt_issuances`·US-G26 신규) · **★ BNK-394 FAQ 21736 사례관리회의록 작성예시 ↔ G32 4-계층 superset** · **★ BNK-398 BE V157 array CHECK probe @ `45d95ea`·케어포 3-1 segment nav @ `1d5747d`** · **★ BNK-397 func.php module 4 간호급여 10-leaf ✅7·△3·신규 갭 0**(욕창/배설/체중/구강 superset) · **★ BNK-396 longterm 게이트 2-모드 확인 → G-LTM-DIRECT-SYNC P3「가정·미확인」** · **★ BNK-395 silverangel 평가지표 PDF 이동서비스 지표40/41 ↔ G15 우위·신규 갭 0** · **백본 216차 zero drift** · **8축 번복 0** · **QA Open 0(active)** · **★ QA-B150/B151/B152 Fixed**(전부 merge EXECUTED·post-merge PASS) · **QA-B116 Planned**(origin/test push **430 BE+68 FE**·post-merge **1539/1539+1784/1784 PASS**) · **QA-B95 Planned** · merge **498 SYNCED**(FE/BE develop=test) · live E2E **124 PASS/19 SKIP** · ⚠ **operation BLOCK**(origin/test push+QA-B95) · **P2「확인」 신규**: G-CASH-RECEIPT-LOG |
| **171차 BNK-392 G32 6/6 closure·V156·QA-B151 Planned·merge gate 485** | **2026-06-19** (BNK-386~392 + planner 171차) — ogada **`e55ae96`/`b9e0947` 106 route·85 page · V1–V156** · **★ G32 FAQ21797 6/6 full-stack closure** — per-attendee `attendeeOpinions[]` @ `b272a7b`/`5222a8f` + V156 `attendee_opinions JSONB` + dashboard `caseManagementAttendeeOpinionGapCount` @ `e55ae96`/`b9e0947` = **회의 폼 + 대시보드 due gate 2-계층 superset**(ezCare/엔젤/케어포 정적 서류함 대비 우위) · **★ V155→V156 migration 정정** · **★ BNK-391** silverangel 지표41/42/43 + NHIS #44 3축 · **★ evidence** silverangel download list·feeService·LCMS cms 404 · **백본 210차 zero drift** · **4축 번복 0** · **신규 갭 0** · **QA Open 0(active)** · **QA-B151 Planned**(BE merge pending 1) · **QA-B116 Planned**(origin/test push **422 BE+62 FE**) · **QA-B95 Planned** · merge **485**(FE SYNCED·BE merge pending 1) · live E2E **123 PASS/19 SKIP** · ⚠ **operation BLOCK**(QA-B151+push+QA-B95) |
| **169차 BNK-380 G21 seed readiness·page 85·QA-B142~B145 Fixed·merge gate 461 SYNCED** | **2026-06-19** (BNK-376~380 + planner 169차) — ogada **`0915f80`/`c0403b0` 106 route·85 page · V1–V155** · **★ BNK-380** G21 seed readiness **NHIS row-batch linkage ✅ full-stack** @ `c0403b0` · **★ page 84→85**(73-cycle undercount correction·신규 기능 아님) · **★ BNK-379** silverangel CMS **`/service/` canonical**(`/daycare/`→404) · **★ BNK-378** FAQ21818 RFID 5-step·ezCare schedule-p300·price 9,346 carry · **백본 3종 zero drift**(NHIS #44 202차·func.php 200차·silverangel essential 202차) · **4축 번복 0** · **신규 갭 0** · **QA Open 0(active)** · **★ QA-B142~B145 Fixed** · **QA-B116 Planned**(origin/test push **412 BE+49 FE**·post-merge PASS) · **QA-B95 Planned** · merge **461 SYNCED(local)** · live E2E **123 PASS/19 SKIP** · ⚠ **operation BLOCK**(origin/test push+QA-B95) · **P3 carry**: G-CHANGE-REASON-AUDIT·G-CASH-RECEIPT·FAQ21818 RFID ledger(out-of-scope) |
| **168차 BNK-375 silverangel G15 실데이터 일지 우위·G21 standalone NHIS panel·merge gate 451 BLOCK** | **2026-06-18** (BNK-368~375 + planner 168차) — ogada **`28e5525`/`f932fd3` 106 route·84 page · V1–V155** · **★ BNK-372** `VisitNhisComparisonPanel` standalone @ `797c529` · **★ BNK-375** silverangel essential 이동서비스 **정적 수칙 점검표** ↔ ogada G15 **별지 제22호 input+print+export 3축 full-stack 우위** · NHIS #44 **199차 zero drift** · **★ G41** filter-year validation @ `28e5525` · **4축 번복 0** · **신규 갭 0** · **QA Open 0(active)** · **QA-B142/B143 Planned**(develop WT DIRTY 2M) · **QA-B116 Planned**(origin/test push **407 BE+44 FE**·FE merge pending **1**) · **QA-B95 Planned** · merge **451 BLOCK**(양쪽 WT DIRTY 2M) · ⚠ **operation BLOCK**(QA-B142+QA-B143+push+QA-B95) · **P3 carry**: G-CHANGE-REASON-AUDIT·월금액 재산정(재가)·RFID 270분 hint |
| **167차 BNK-367 G21 readiness full-stack closure·G-SCHEDULE-FIX-LTM-COMPARE BE ✅·G-7-1-PRINT-BUNDLE ✅+·merge gate 440** | **2026-06-18** (BNK-362~367 + planner 167차) — ogada **`f232285`/`8a8c5b3` 106 route·84 page · V1–V155** · **★ G21 batch-confirm readiness full-stack closure**(△→✅) — FE `VisitBatchConfirmPanel` PLAN/BILLING split wire @ `f9ed97d` + BE per-kind ready/block-unassigned @ `f26abb0`/`5f710e3`(BNK-365) · **★ G-SCHEDULE-FIX-LTM-COMPARE P3→BE ✅ closure** — `GET /visits/nhis-comparison` 4종 분류 @ `03a052a` + readiness embed @ `8a8c5b3`(BNK-366~367·**FE summary wire △ P2**) · **★ G-7-1-PRINT-BUNDLE ✅+** — `BillingStatementPrintPanel` 4종 인쇄 @ `50d330d` + 미납 영수증 제외 라벨 @ `f5639df`(BNK-363~364·**엑셀다운로드 ❌ P3**) · **★ 신규 candidate G-CHANGE-REASON-AUDIT P3「가정」**(`change-list` field-level diff·BNK-362) · **4축 교차검증 번복 0** · **백본 zero drift** · **QA Open 0(active)** · **QA-B116 Planned**(FE SYNCED·origin/test push **38 FE+402 BE**·BE merge pending **1**) · **QA-B95 Planned**(live E2E 122 PASS/19 SKIP) · merge gate **440** · ⚠ **operation BLOCK**(BE merge+origin/test push+QA-B95) · **P2 Must**: 일지④ 인쇄·별지 제22호 **✅ CLOSED**(166차) |
| **165차 BNK-354 G41 ✅+ deepen·G21 RFID ✅ full-stack·G-SCHEDULE-FIX-LTM-COMPARE P3·merge gate 415** | **2026-06-18** (BNK-348~354 + planner 165차) — ogada **`caa215f`/`dac19d3` 106 route·84 page · V1–V154** · **★ G41 ✅+ deepen** — 대시보드 위젯 @ `9e91e6a` + PDF 8-7 mandatory alerts + 8-7-1 report export @ `caa215f` · **★ G21 RFID compare ✅ full-stack** @ `27c9de3`/`4a112fe`/`1ca6c19` · **★ G-SCHEDULE-FIX-LTM-COMPARE P3 candidate**(`schedule-fix` `chk-ltm-fix`) · **★ G-CASH-RECEIPT deepen**(`receipt-list` colModel) · **★ carefor module 8** 15-leaf cross-walk(✅8·△2·❌5) · **4축 번복 0** · **신규 갭 0** · **QA Open 0(active)** · **QA-B116 Planned**(FE SYNCED·origin/test push **25 FE+390 BE**·BE merge pending **1**) · **QA-B95 Planned** · merge gate **415** · ⚠ **operation BLOCK**(BE merge+origin/test push+QA-B95) · **P2 Must**: 일지④ **인쇄·별지 제22호 전항목** |
| **163차 BNK-341 carefor transport 10-leaf·4-축 우위·FAQ21799 신규직원 건강검진 △·merge local SYNCED** | **2026-06-18** (BNK-335~341 + planner 163차) — ogada **`38642e2`/`40ef105` 106 route·84 page · V1–V153** · **★ QA-B131/B132/B133 Fixed** · **★ BNK-341** carefor func **`2.이동서비스관리` 10-leaf** ↔ transport 9 route·**4-축 우위**(VRP·compliance·service-fees·Kakao)·백본 **170차 zero drift** · **★ BNK-339** FAQ21799 건강검진 parity ✅·**신규직원 1년 이내 서류 △ @ `8e6310a`** · **★ BNK-340** FAQ21710 payroll out-of-scope·K008 P3 · **4축 번복 0** · **신규 갭 0** · **QA Open 0(active)** · **QA-B116 Planned**(merge EXECUTED local) · **QA-B95 Planned** · merge **local SYNCED**·**391 vs origin/test**(12 FE+379 BE) · ⚠ **operation BLOCK**(origin/test push+QA-B95) · **P2 Must**: 일지④ full 법정 입력 서식 |
| **160차 BNK-315 G-CASH-RECEIPT P3 candidate·QA-B121/B122 Fixed·merge FULLY UNBLOCKED(410)** | **2026-06-18** (BNK-311~315 + planner 160차) — ogada **`0baabe9`/`f0e52b8` 106 route·84 page · V1–V149** · **★ QA-B121 Fixed @ `0695244`**(develop HEAD live E2E **122/122 PASS**·fee-schedule seed + CSV Blob assert) · **★ QA-B122 Fixed @ `f0e52b8`**(backend develop WT clean 복구) · **★ BNK-315 신규 갭 candidate G-CASH-RECEIPT P3「가정」**(FAQ21700 본인부담금 현금영수증 발급·취소·발행내역·수납 동시 발급·연락처 기반 발급번호 ↔ ogada billing 수납등록 ✅·`현금영수증`/`cashReceipt` grep **0건 = ❌**·MVP 범위 밖·승격 아님) · **★ BNK-314 4축 교차검증(G14·대시보드·v1.3-C·v2 CMS) 가정 번복 0**·`TransportPage.test.jsx` 회귀 해소 · **★ BNK-313 FAQ21792 2026 계약/근로계약서·BNK-314 FAQ21779 지정갱신제·BNK-312 silverangel privacyPolicy 효성CMS** = G2b/G14/G-APPRAISAL 근거 강화(신규 갭 아님) · **★ G14 NHIS plan generation(10필드) P2 carry** · **★ 백본 4종 zero drift**(NHIS #44·func.php 107 leaf·silverangel essential·ezCare fnc DRIFT cachebuster only)·이지케어 도입 9,342 oscillating noise 23회 폐기 · **QA Open 0(active)** · **QA-B116 Planned**(merge pending 48·post-merge 재검증) · **QA-B95 Planned** · **신규 갭 candidate 1·가정 번복 0·상태 변경 1·미확인 1** · merge **410 FULLY UNBLOCKED**(362 BE + 48 FE·양쪽 WT CLEAN) · ⚠ **live E2E verification BLOCK**(QA-B116+QA-B95) |
| **159차 BNK-310 func 2-9 verification closure·audit trail FE wire·merge BLOCK(FE)** | **2026-06-18** (BNK-307~310 + planner 159차) — ogada **`b48252a`/`30243f7` 106 route·84 page · V1–V148** · **★ func 2-9 verification closure** — `ClientOutingReportPage`+live E2E harness @ `3a0110f` · **★ G15 audit trail FE wire full-stack** @ `3cc5a08`(BE read @ `5994d15`) · **★ L02 nursing reports live E2E harness** @ BNK-309 · **★ BE actuator liveness/readiness** @ `30243f7` · **QA Open 0(active)** · **QA-B121 Planned**(live E2E 4 FAIL·FE merge BLOCK) · **QA-B116 Planned**(merge pending 41·post-merge 재검증) · **QA-B95 Planned**(partial RUN) · **신규 갭 0·가정 번복 0** · merge **398 BLOCK(FE only)**(357 BE + 41 FE·BE WT CLEAN) · ⚠ **live E2E verification BLOCK**(QA-B121+QA-B95) |
| **158차 BNK-306 func 2-7/2-8 full-stack·audit trail read·NHIS #44 5-date·merge FULLY UNBLOCKED** | **2026-06-18** (BNK-303~306 + planner 158차) — ogada **`8b68fdb`/`6eb9cc0` 106 route·84 page · V1–V148** · **★ BNK-304~306 케어포 func 2-7/2-8** — BE `GET /transport/reports/monthly-service-variation`·`/monthly-resident-status` @ `5d27ad3`(migration 0) → FE `TransportMonthlyReportsPage` `/reports/transport-monthly` @ `6a18dfd` = **full-stack closure live** · **★ BNK-306 G15 일지④ audit trail read API** @ `5994d15`(잔여: FE audit UI·인쇄·보관 UX P2) · **★ BNK-306 NHIS #44** 제34조 개정 이력 **5-date 전부 「변경 사항 없음」**(러-1~4 정본 2025-07-01 불변 deepen) · **★ BNK-305 FAQ21768** K008 근로자의 날 대체휴무 불가 = **payroll out-of-scope·P3 carry**(신규 갭 아님) · **★ BNK-305 이지케어 도입 9,337 oscillating** 추세지표 폐기 carry · **QA Open 0(active)** · **QA-B116 Planned**(merge pending 34·post-merge 재검증) · **QA-B95 Planned** · **신규 갭 0·가정 번복 0** · merge **385 FULLY UNBLOCKED**(351 BE + 34 FE·양쪽 WT CLEAN) · ⚠ **live E2E verification BLOCK**(QA-B95 only) |
| **157차 BNK-302 G15 일지④ PUT closure·silverangel CMS·longterm DRIFT·merge FULLY UNBLOCKED** | **2026-06-18** (BNK-298~302 + planner 157차) — ogada **`cb30f24`/`c13800c` 105 route·83 page · V1–V147** · **★ BNK-300~302 G15 일지④ 상태 변경** — GET export(`0cfa970`/`b69c8ae`) → **PUT persistence+FE 편집 폼 closure live**(`aaaeb10` BE `PUT /transport/runs/{runId}/service-log` + FE `TransportServiceLogPanel` @ `7a4b310`) = **v1.3-C Must 승격 종결 후보**(잔여: 인쇄·보관 UX·감사 trail) · **★ BNK-302 silverangel [mainService.do](https://www.silverangel.kr/newSilverangel/service/mainService.do) CMS 3-method carousel**(자동이체·카드·가상계좌·1600-6859) ↔ ogada **G2b 정본 1:1** · **★ BNK-302 longterm 502/501/610/503 KRDS 구조 DRIFT** — 정적 수가 literal 소실 → **V103 seed + BNK-235~279 carry authoritative** · static scrape **반기 1회 수동 cross-walk** 권고 · **★ BNK-301 FAQ21757** G30 방문상담 20분 cross-confirm(신규 갭 0) · **★ BNK-298 US-E04 QrCheckinTargetsPanel FE closure** · **★ QA-B120 Fixed @ `af4d7f8`** · **QA-B116 Planned**(merge pending 28·post-merge 재검증) · **QA-B95 Planned** · **신규 갭 0·가정 번복 0** · merge **374 FULLY UNBLOCKED**(346 BE + 28 FE·양쪽 WT CLEAN) · ⚠ **live E2E verification BLOCK**(QA-B95 only) |
| **155차 transport cluster deepen·NHIS #44 일지④·ezCare 계획/청구 2-track·merge BLOCK** | **2026-06-17** (BNK-286~291 + planner 155차) — ogada **`d3bef42`/`114411f` 105 route·83 page · V1–V146** · **★ transport cluster deepen 풀스택** — BE V143 `transport_run_stops.stop_kind`(지점 waypoints)·V144 `default_driver_id`·V145 `default_driver_name`·V146 `desired_pickup/dropoff_time`+DROPOFF guard @ `f5b2b42`/`114411f` · FE map pins·Korean geocode·split-view route editor @ `84e75ec`/`d3bef42`(결정 96-154-1/2/3 closure) · **★ NHIS #44 이동서비스비 러-1~4 verbatim 1차 확인**(편도 50%·1일 1회·**④ 이동서비스 일지 작성·보관 의무**)↔엔젤 지표41/42↔ogada `TransportCompliancePage` = **3-source cross-walk**→**법정 일지④ 입력 서식 P2→v1.3-C Must 승격 검토** · **★ ezCare 계획/청구 2-track + RFID 정산**(Channel.io plan-billing-diff `341309a1`)→**RFID 하드웨어·듀얼패널 split-view P1** · **★ QA-B115/B116/B117 Open→Planned**(3 BLOCK·dirty-tree+test regression·기능 갭 아님) · **QA-B112/B114 Fixed** · **QA-B95 Planned** · **신규 갭 0·가정 번복 0** · merge **351**(336 BE + 15 FE·⚠ BLOCK) · ⚠ **live E2E verification BLOCK** |
| **153차 3-product line·dual-source numbering·merge BLOCK** | **2026-06-17** (BNK-280~285 + planner 153차) — ogada **`b000d92`/`7ac0a46` 103 route·82 page · V1–V142** · **★ BNK-285 케어포 3-product line** — `intro_si`(시설 11 module)·`intro_visit`(방문 8 module)·주야간=`daycare`(시설+이동서비스 module 2 삽입) · **★ dual-source numbering closure** — 시설 `intro_si` 2-4=신체제재(demo-work 정본)·주야간 `daycare` 2-4=차량관리·ogada L02/L03 deepen=**시설급여 평가지표 코어 차용** · **★ QA-B113 Fixed @ `b000d92`** · **QA-B112/B114 Planned**(WT dirty·merge BLOCK) · **QA-B95 Planned** · merge **341**(331 BE + 10 FE·⚠ BLOCK) · ⚠ **live E2E verification BLOCK** |
| **147차 L02_M13/M15·G30 full·FE merged·plan/claim P2** | **2026-06-16** (BNK-248~251 + planner 147차) — ogada **`c5f82a6`/`c655743` 94 route·137 page · **78.28% carry** · V1–V140 · **★ L02_M13 통합식사도움 ✅ full stack** @ `81a2223`/`9ad8346`(V140·결정 95 31~32회째) · **★ G30 FAQ21841 ✅ full stack** @ `344a28b`/`9ad8346`(phone panel) · **★ L02_M15 특이사항 ✅ FE** @ `3549896` · **★ L02_M04/M05 rpt BE △** @ `c655743` · **★ FE develop→test MERGED** @ `4299914` · **★ law.go.kr MOHW 2025-247 본문** (#44 dual-source) · **★ plan/claim 이중일정 P2** (Channel.io BNK-250) · **★ L02 leaf 6/15(40%)** · **QA Open 0건** · **QA-B95 Planned** · merge **301**(FE merged·BE 299 pending) · ⚠ **live E2E verification BLOCK** |
| **145차 L02_M07 full·7-1 4채널·live-e2e harness·MOHW 2026-126** | **2026-06-16** (BNK-240~243 + planner 145차) — ogada **`6f53978`/`18ff83e` 87 route·69 page · **78.28% carry** · V1–V132 · **★ L02_M07 G-BODY-RESTRAINT ✅ full stack** @ `ea6092a`/`14a2bb9`/`d862a82`(V131+V132·`/care/body-restraint`·결정 95 26회째·L02 2/15) · **★ live-e2e harness deepen** @ `1f77324`/`18ff83e`/`10f32c4`/`07dd49b` · **★ 7-1 4채널 일괄발송 P2 deepen**(PDF p.87 우편·문자·이메일·직접수령·발송일 수정 규칙) · **★ MOHW 고시 제2026-126호 P3**(본인부담상한·G9 cross-ref) · **★ longterm 4종 oscillating ±9B noise 확정** · **★ #44 joHistory 99차 zero drift** · **★ ezCare FAQ21831·도입 9,324** · **QA-B99 Planned** · **QA-B95 Planned** · **QA-B98 Fixed** · merge **636 BLOCK**(FE WT dirty) · ⚠ **cross-stream merge BLOCK** |
| **144차 G30 evidence window·G39 partial+·L02_M02 FE wire·신규 갭 3건·func.php 107 leaf** | **2026-06-16** (BNK-236~239 + planner 144차) — ogada **`95e7e96`/`df14e15` 86 route·68 page · **78.28% carry** · V1–V131(V131 WIP) · **★ G30 monitoring evidence window ✅ deepen**(`MonitoringEvidenceWindow` 전전월±2개월·FAQ21838 1:1·결정 95 24회째) @ `73df04d` · **★ G39 ✅ partial+**(pilot+live harness) · **★ L02_M02 집중배설관찰 ✅ FE wire** @ `1264c16`(V130) · **★ 신규 갭 G-BODY-RESTRAINT(L02_M07 신체제재) P2 △ BE WIP**(V131·demo `view.care_sanction`) · **★ 신규 갭 G-STAFF-LIFECYCLE P2**(FAQ21825 4단·퇴사·희망이음 RFID) · **★ 신규 갭 G-REVENUE-EXPENSE P3**(module 12 PDF-only) · **★ func.php 107 leaf 정본**(agents.yaml「109」번복) · **★ 주야간 PDF 132p snapshot** · **★ #44 러-1~4 97차 zero drift** · **★ longterm 4종 verbatim 불변** · **QA Open 0건** · **QA-B96/B97 Fixed** · **QA-B95 Planned** · merge **625 · WT CLEAN** · ⚠ **live E2E verification BLOCK** |
| **143차 G24b list·G19 harness·G30/G39 P2·lawImg DRIFT·G18-SHORT 연장** | **2026-06-15** (BNK-232~235 + planner 143차) — ogada **`73094f9`/`73df04d` 85 route·67 page · **78.28% carry** · V1–V129 · **★ G24b compliance list page ✅** @ `eb16734` · **★ G19 provider discovery harness △** @ `41d8de5`/`8cb8789` · **★ G30/G39 P2 deepen △** monitoring evidence window+care-provision dispatch pilot E2E @ `73df04d`/`73094f9` · **★ #44 joHistory 95차 zero drift** · **★ lawImg 95차 DRIFT 404** · **★ silverangel extra/fee 404** · **★ G18-SHORT-PILOT 2026.1~무기한** · **★ G-STAFF-MEETING P3 candidate** · **QA Open 0건** · **QA-B95 Planned** · merge **612 · WT CLEAN** · ⚠ **live E2E verification BLOCK** |
| **142차 G24b dashboard·G41 enum·live E2E env BLOCK** | **2026-06-15** (BNK-227~231 + planner 142차) — ogada **`3cbe582`/`1e21b20` 85 route·66 page · **78.28% carry** · V1–V129 · **★ G24b compliance API+dashboard widget ✅** @ `98002d4`/`f4c8beb`/`ca0b627`/`baa6d6d` · **★ G41 enum 23+ ✅** V129 @ `b1c92e1` · **★ #44 P0 ✅ 91차** · **★ longterm provider search** → G19 P1 · **★ harness deepen** @ `3cbe582`/`1e21b20` · **★ QA-B95 Planned**(live E2E env) · merge **602 · WT CLEAN** · ⚠ **live E2E verification BLOCK** |
| **140차 QA-B93 Fixed·G-ONBOARD △·merge UNBLOCKED** | **2026-06-15** (BNK-219~223 + planner 140차) — ogada **`2ccc88e`/`735dd53` 84 route·67 page · **78.28% carry** · V1–V125 · **★ QA-B93 Fixed @ `b45830d`** · **★ L03 live E2E harness deepen** @ `75c6c76`/`b698871`/`2ccc88e` · **★ G-ONBOARD-SUPPORT △ BE** @ `735dd53` · **★ G-FAMILY-LEAVE evidence ✅** 3-source · **★ P3 candidate** G-LIVECHAT·G-CIST · **QA Open 0건** · merge **577 · FULLY UNBLOCKED** |
| **137차 L03 4 leaf full·v1.3-B △·merge BLOCK** | **2026-06-15** (BNK-209~212 + planner 137차) — ogada **`97108f2`/`090b2d7` 78 route·63 page · **78.28% carry** · V1–V119 · **★ L03_M11/M13/M14/M04 ✅ full** — M14 @ `962858b`/`63cb193` · M13 @ `bb3dee8`/`faf55f0` V118 · M04 @ `97108f2`/`81bca68` V119 · **★ L03 14 leaf 57% 커버**(8/14 ✅) · **★ v1.3-B △ partial+** suggest API WIP @ `090b2d7` · **★ 신규 P2** G24b·G41-COG-REFRESHER·G-ONBOARD-SUPPORT · **QA-B86/B87 Fixed @ `63cb193`** · **QA-B88/B89/B90 Planned** · merge **545 · BLOCK**(FE HEAD FAIL + BE WT dirty) |
| **136차 G-NURSING full·L03_M11 full·L03_M14 BE △·merge BLOCK(BE)** | **2026-06-14** (BNK-204~208 + planner 136차) — ogada **`246df56`/`1a822d2` 75 route·61 page · **78.28% carry** · V1–V116 · **★ G-NURSING-PRESSURE-ULCER ✅ full** — BE V114 @ `edda491`+FE @ `e214da1`+pilot/live E2E @ `024e720`/`24a1c5c` (BNK-204~206) · **★ L03_M11 통합 바이탈 ✅ full** @ `8570fa2`/`80c0bd5` (BNK-207) · **★ L03_M14 체중 BE ✅ partial+** @ `1a822d2` V116 · FE wire ❌ · **★ L03 77%→62% 미커버** · **★ FAQ21783 G2 import resilience P2** · **QA-B85 Fixed** · **QA-B86/B87 Planned** · merge **534 · BLOCK(BE HEAD test FAIL)** |
| **135차 G21 full·G17b full·G-NURSING-PRESSURE-ULCER P1·merge UNBLOCKED** | **2026-06-14** (BNK-199~203 + planner 135차) — ogada **`ad319d7`/`3bd6a43` 69 route·59 page · **78.28% carry** · V1–V113 · **★ G21 batch-confirm ✅ full** — FE+BE+E2E 5-cycle @ `13e691e`/`c22a5dc` · **★ G17b 인지활동형 미제공 사유 ✅ full** — V112/V113+ABSENT 가드 4-cycle @ `6b7e6cb`/`ba7d84f`/`3bd6a43`+`c26cfa7`/`487416d` (MOHW 제32조) · **★★ 신규 갭 G-NURSING-PRESSURE-ULCER**(욕창 케어 lifecycle·dual-source·v3.1 Must 6번째·결정 94·P1) · **★ demo L03 간호급여 13 leaf 77% 미커버 P2** · **★ demo L02 요양기록 15 leaf 33% gap reinforce P1** · **★ G18-SHORT-PILOT P3** · **QA-B83/B84 Fixed** · **QA Open 0건** · merge **521 · FULLY UNBLOCKED** |
| **134차 G21 batch-confirm·US-UX-05·merge UNBLOCKED** | **2026-06-14** (BNK-195~198 + planner 134차) — ogada **`13e691e`/`c22a5dc` 69 route · **78.28% carry** · **★ J03 quiet-hours ✅ full** — 4-cycle @ `56f0204`→`a057739` · **★ G21 batch-confirm ✅ partial+** — BE @ `0b807d8`/`c22a5dc` + FE @ `13e691e` (FAQ21782 5단) · **★ US-UX-05 ✅** @ `1e111be`/`8a8b930` · **★ MOHW 2025-247 HWPX 정본** · **★ 신규 갭**: G17b(P2)·G-FAMILY-LEAVE(P3)·G-RURAL-SUBSIDY(P3)·G-PROG-MGR-BONUS(P3) · **QA Open 0건** · merge **512 · UNBLOCKED** |
| **129차 G41/G41b partial+·G-STAFF-WELFARE P3·merge FULLY UNBLOCKED** | **2026-06-14** (BNK-185~187 + planner 129차) — ogada **`e14ba10`/`32f87f1` 66 route · **78.28% carry** · **★ G41/G41b ✅ partial+** — 184→187 4-cycle · compliance+live E2E harness @ `0f11158`/`38d24b6`/`a4ab0c2` · **★ G-STAFF-WELFARE P3** — FAQ21796 · **★ G-ONBOARD-SUPPORT P2** — silverangel 14필드 · **★ QA-B76/B77 Fixed** · merge **479 · FULLY UNBLOCKED** |
| **128차 G30 full·G34-QUAL partial+·G41 BE·merge FULLY UNBLOCKED** | **2026-06-14** (BNK-180~184 + planner 128차) — ogada **`5146895`/`6191b91` 67 route · **78.28% carry** · **★ G30 ✅ full** — integrated checklist FE+BE+E2E @ `b1dfd34`/`400c835`/`5146895` · **★ G34-QUAL ✅ partial+** — 177→183 4-cycle @ `574bd08`/`997831c` · **★ G41 △ BE partial** — training log API+V104 @ `6191b91` · **★ QA-B74 Fixed** @ `cfd87c5` · merge **468 · FULLY UNBLOCKED** |
| **127차 8-12 partial+·J03 readiness·G34-QUAL·merge BLOCK(FE)** | **2026-06-14** (BNK-176~179 + planner 127차) — ogada **`443efca`/`229f84c` 66 route · **78.28% carry** · **★ #44 P0 ✅ carry** · **★ 8-12 ✅ partial+** — BE CSV FE wire @ `488f547` · pagination @ `ff173af` · G42 modal @ `6012044` · **★ J03 ✅ partial+** — channel-status API+FE panel+email/quiet-hours @ `d4acab7`/`6b1258c`/`d695923`/`fffd355` · **★ G21 closure** @ `c16f4fe` · **★ G34-QUAL P2**(FAQ21837) · **QA-B74 Planned** · merge **455 · BLOCK(FE)** |
| **126차 #44 P0 ✅·8-12 deepen·G42 partial+·merge FULLY UNBLOCKED** | **2026-06-14** (BNK-172~175 + planner 126차) — ogada **`a7a6004`/`39ee679` 67 route · **78.28% carry** · **★ #44 P0 ✅** — NHIS 제34조 lawImg 830/2,630/**5,230**/**8,630** · V68 RU_3/RU_4 seed @ `39ee679` · **★ 8-12 △ deepen** — PDF 7종 FE·live E2E·BE CSV export @ `07956f5`/`ccc4d75`/`bc927f7` · **★ G42 ✅ partial+** — follow-up+approval queue @ `14124d6`/`bcb1d9f` · **QA-B72 Fixed** @ `a7a6004` · **★ G-HOMEPAGE P3** · merge **443 · FULLY UNBLOCKED** |
| **125차 G30 partial+·8-12 aggregated API·EZCare FAQ cluster·merge FULLY UNBLOCKED** | **2026-06-13** (BNK-168~171 + planner 125차) — ogada **`07956f5`/`5692662` 67 route · **78.28% carry** · **★ G30 ✅ partial+** — `MonitoringSelfDiagnosisPage`+V100·FAQ21836 basis fallback·pilot E2E @ `6f6915f`/`b8e92bf` · **★ 8-12 ✅ partial+** — aggregated API·referenceDate·exports @ `bf6dd25`/`07956f5` · **★ G9-COPAY-NAMING ✅** @ `e77b7e4` · **★ G9-COG NHIS import gate ✅** @ `8bb6583` · **★ EZCare K008~K014 P3 cluster** · **★ #44 53차** · merge **430 · FULLY UNBLOCKED** |
| **124차 G9-COG·FAQ21824 checklist·longterm 502/503·merge FULLY UNBLOCKED** | **2026-06-13** (BNK-164~167 + planner 124차) — ogada **`e77b7e4`/`edd2771` 66 route · **78.28% carry** · **★ G9-COG ✅ FE+BE** — 30/30 cells·V99 @ `6ef671b`/`edd2771` · **★ FAQ21824 checklist ✅ partial+** @ `58256c6` · **★ G-7x-1 guard ✅ partial+** @ `338c014`/`21eb0af` · **★ G9-COPAY-NAMING ✅** @ `e77b7e4` · **★ longterm 502/503 verbatim** · **★ #44 49차**(정본=longterm 502) · **★ P3** G9-SHORT/G9-DEMENTIA/G9-DR · merge **418 · FULLY UNBLOCKED** |
| **123차 G42 partial·G34b deepen·8-12 partial·merge FULLY UNBLOCKED** | **2026-06-13** (BNK-160~163 + planner 123차) — ogada **`02cbd05`/`8487667` 65 route · **78.28% carry** · **★ G42 ✅ partial** — V97+approval @ `b0a9e06`/`bcdc411` · **★ G34b ✅ partial+** — clone·role guard·import-draft @ `1b5fabe`/`8487667` · **★ 8-12 △ partial** @ `02cbd05` · **★ FAQ21824 zero drift** · **★ #44 47차**(byl18≠러-1~4) · merge **408 · FULLY UNBLOCKED** |
| **122차 G40b full·G34b·G42·merge FULLY UNBLOCKED** | **2026-06-13** (BNK-155~159 + planner 122차) — ogada **`3c7d2c7`/`2925ff7` 64 route · **78.28%** · **★ G40b ✅ full** — V95/V96+Status Route @ `7b68f54`/`a7b4a39` · **★ G34b ✅ partial** — needs-assessment import @ `0ce04ad` · **★ G42 고충상담 P2** · **★ FAQ21816 급여제공기록지** · merge **395 · FULLY UNBLOCKED** |
| **121차 G40 partial+·G40b·G2b·merge FULLY UNBLOCKED** | **2026-06-13** (BNK-152~154 + planner 121차) — ogada **`22325f4`/`bdfc140` 63 route · **78.28%** · **★ G40 FE+BE+V93/V94 ✅ partial+** · **★ G40b 반기 기초평가(지표16·FAQ21811) △ partial** · **★ 효성CMS 3-method → G2b P2** · **★ LCMS regStep.do 404 DRIFT** · merge **386 · FULLY UNBLOCKED** |
| **120차 G40 BE·FAQ21806 V92·8-12 P2·merge BLOCK** | **2026-06-13** (BNK-145~151 + planner 120차) — ogada **`4efa168`/`686d686` 63 route · **78.28%** · **★ FAQ21806 onboarding V92 FE+BE deepen** · **★ G40 신규입소 위험도평가 BE ✅ partial** · **★ silverangel 9-step·EZCare 일정확정·demo-work npay** · merge **376 · BLOCK**(FE WT dirty · QA-B62) |
| **119차 US-R03 HR hub·G2 CMS cancel·merge FULLY UNBLOCKED** | **2026-06-13** (BNK-141~144 + planner 119차) — ogada **`9a6fdb6`/`4a622ab` 63 route · **78.28%** · **★ US-R03 HR file hub ✅ partial** · **★ G2 CMS 등록+해지 ✅ partial** · merge **367 · FULLY UNBLOCKED** |
| **85차 G24/G14 develop·직원 lifecycle·merge BLOCK** | **2026-06-12** (BNK-125~127 + planner 115차) — ogada **`479e064`/`728339e` 59 route · **78.28%** · **★ G24/G14 develop 닫힘** · merge **323 · BLOCK**(BE WT dirty · QA-B54) |
| **82차 G34 partial·G-Payroll P3·merge FULLY UNBLOCKED** | **2026-06-12** (BNK-119~122 + planner 112차) — ogada **`6d6b426`/`559648f` 57 route·81 page · **78.28%** · **★ G34 US-S01 FE+BE partial ✅** @ `6d6b426`/`559648f` · **★ LifecycleWorkflowPanel G17/G32 ✅** · **★ QA-B50/B51/B52 Fixed** · **★ G-Payroll Epic P3**(module 11 6 leaf · ogada 0건) · **★ cost_master_statistic P3** · **★ FAQ21805·FAQ21820 P2** · merge **311 · FULLY UNBLOCKED** |
| **81차 QA-B49 Fixed·G34 업무수행일지·merge FULLY UNBLOCKED** | **2026-06-12** (BNK-115~118 + planner 111차) — ogada **`2cd2cd8`/`3ad2a90` 58 route·81 page · **78.28%** · **★ QA-B49 Fixed** @ `f72da41`/`8fa9f3d` · **★ G38/G39 dashboard snapshot aggregation ✅** · **★ G17/G32 edit-flow pilot E2E ✅** @ `2cd2cd8`/`3ad2a90` · **★ G34 선임 요양보호사 업무수행일지 P2 갭**(케어포 8-1-1/8-1-2 · ogada 0건) · **★ FAQ21805 수급자 계약 lifecycle P2** · **★ getting_started.php HTTP 302** · merge **300 · FULLY UNBLOCKED** |
| **80차 G38/G39 폐루프·FAQ21800·merge FE BLOCK** | **2026-06-12** (BNK-110~114 + planner 110차) — ogada **`26499b3`/`a0a7f9c` 58 route·80 page · **78.28%** · **★ G38 FE+BE+pilot E2E ✅** @ `28c22b0`/`a9f8bda`/`4b2b082` · **★ G39 dashboard widget+weekly/monthly ✅** @ `8e66ae8`/`a16e1fe` · **★ BE dashboard widget counts ✅** @ `a0a7f9c` · **★ G17/G32 edit ✅** @ `26499b3` · **★ FAQ21800 [연간] 욕구사정 P2** · **★ QA-B49 Planned**(FE WT BLOCK) · merge **291 · FE BLOCK** |
| **79차 G37 FE·G38 BE·G39 FE+BE·MIME guard** | **2026-06-12** (BNK-106~109 + planner 109차) — ogada **`1c99bcd`/`f082933` 56 route·80 page · **76.67%** · **★ G37 FE+live E2E+MIME fallback ✅** @ `e026ae9`/`6875af5`/`e9d1178`(QA-B46 Fixed) · **★ G38 care-plan notification compliance BE ✅** @ `5fd35a6`(BNK-106 · FAQ 21802 · **FE P2**) · **★ G39 provision result evaluation FE+BE ✅** @ `1c99bcd`/`f082933`(BNK-107 · V80 · **StatCard P2**) · **★ silverangel 지표44 20차 zero drift** · **#44 16차 0건** · merge **280 · FULLY UNBLOCKED** |
| **78차 G17/G32 contracts·G33 pilot E2E·J03 dispatch·G37 BE** | **2026-06-12** (BNK-103~105 + planner 108차) — ogada **`8b0c6c7`/`0325d95` 56 route·78 page · **76.67%** · **★ G17/G32 program compliance API contracts+422 guard ✅** · **★ G33 settlement pilot E2E+reload fallback ✅** · **★ G26 ClientDetail NTS xlsx E2E ✅** · **★ J03 primary guardian dispatch BE+E2E ✅** · **★ G37 care-plan attachment BE ✅**(FE UI P1) · **★ Channel.io → G35 CIST(P3)·G34 문자 인증(P2)** · **#44 15차 0건** · merge **269 · FULLY UNBLOCKED** |
| **77차 G17 지표27 3행·G2 CMS debit·live E2E harness** | **2026-06-12** (BNK-99~102 + planner 107차) — ogada **`c413615`/`838a7f6` 56 route·78 page · **76.67%** · **★ G17 지표27 3행 BE→FE ✅**(BNK-100→101→102) · **★ G33 settlement UI+V77 integrity ✅** · **★ G2 CMS debit 이력+FAILED 응답 ✅** · **★ programCompliance live E2E harness ✅** · **★ 이지케어 FAQ21815·6단 본인부담 P2** · **★ lcms 상품설명서·단기보호 74,060 P2** · **#44 13차 0건** · merge **256 · FULLY UNBLOCKED** |
| **76차 G33 폐루프·PDF 7-x 정책·G32 FE 5기둥** | **2026-06-12** (BNK-95~98 + planner 106차) — ogada **`7564c2a`/`70e6191` 55 route·46 page · **76.67%** · **★ G33 청구시작 FE+BE+overdue+settlement ✅**(BNK-94→97→98) · **★ G32 evaluationConductedMet FE+BE 5기둥 ✅** · **★ US-D01 primary guardian BE ✅** · **★ PDF↔func.php 7-x 삼원 불일치**(Route=func.php·rename 금지) · **★ getting_started 이동서비스 분리** · **#44 11차 0건** · merge **244 · FULLY UNBLOCKED** |
| **75차 G32 triple-source·compliance 4기둥·7-3 갭** | **2026-06-11** (BNK-91~94 + planner 105차) — ogada **`37e6b00`/`208b37e` 55 route·78 page · **76.67%** · **★ G32 triple-source**(지표43+케어포8-5+이지케어21797) · **★ G32 compliance 4기둥 BE**(`evaluationConductedMet`) · **★ V75 `case_management_plan` FE+BE ✅** · **★ PilotFixturePanel ✅** · **★ PDF 7-3 청구시작 P2 신규 갭** · **★ FAQ 45982 K-MMSE P3** · **#44 10차 0건·수동 보류** · merge **232 · FULLY UNBLOCKED** |
| **74차 G17/G32 FE+BE·케어포 8-5** | **2026-06-11** (BNK-87~90 + planner 104차) — ogada **`0adf8c6`/`5e1828c` 54 route·45 page · **76.67%** · **★ G17/G32 FE+BE 폐루프 ✅** · **★ V74 integrity ✅** · **★ G32 dual-source**(지표43+케어포 8-5) · **★ NHIS 본인부담 비교 partial** · **#44 7차 0건·수동 보류** · merge **220 · FULLY UNBLOCKED** |
| **73차 7-9·G17·G32 BE** | **2026-06-11** (BNK-84~86 + planner 103차) — ogada **`53e4016`/`55fae99` 54 route·74 page · **76.67%** · **★ 7-9 환불 FE+BE ✅** (7-x 10/11) · **★ G17 BE ✅** @ `73e169a` · **★ G32 BE ✅** @ `55fae99` · **★ US-G04 upload guard ✅** · **★ 통합재가 「주야간 월 10만원」** verbatim · **#44 6차 0건·수동 보류** · merge **210 · FULLY UNBLOCKED** |
| **72차 US-G04·G26 xlsx·G21** | **2026-06-11** (BNK-78~81 + planner 102차) — ogada **`5c0d83d`/`970c7af` 52 route·74 page · **76.67%** · **★ US-G04 연도 수가 가드 UX partial ✅** · **★ BE fee schedule year guard ✅** · **★ G26 NTS xlsx partial ✅** · **★ G21 dup paired slot ✅** · **★ US-L01 8은행 포맷 ✅** · **#44 5차 0건·수동 보류** · merge **198 · BE ready · FE BLOCK**(QA-B37) |
| **71차 G26·G32·G17** | **2026-06-11** (BNK-74~77 + planner 101차) — ogada **`c1d9788`/`1af5b1f` 52 route·74 page · **75.77%** · **★ G26 7-2-1 FE+BE E2E ✅** (7-x 10/11) · **★ CMS/easy-pay 제외** · **★ G17 지표27 P1 Epic** · **★ G32 사례관리 회의록 P2** · **#44 4차 0건·수동 보류** · merge **187 · FULLY UNBLOCKED** |
| **70차 paidAt·US-J02·G17·G26** | **2026-06-11** (BNK-72~73 + planner 100차) — ogada **`0024c88`/`ed730a2` 52 route·74 page · **75.77%** · **★ G2/v2 `paidAt` 필수 ✅** = 케어포 7-2 패리티 · **★ US-J02 race·stale error ✅** @ `62058d3`/`189a00d` · **★ G17 지표27 P1 Epic** · **★ G26 7-2-1 연말정산 P2** · **#44 3차 0건·수동 보류** · merge **176 · FULLY UNBLOCKED** |
| **69차 G15 v1.3-C·G7·G31** | **2026-06-11** (BNK-68~69 + planner 99차) — ogada **`fcf713a`/`64ebf6e` 52 route·74 page · **75.77%** · **★ G15 2-1-1/2-9·TSF·공단 3분리 UI ✅** @ `a0dcfc0`/`88d4c59`/`fcf713a` · **★ G7 live guidance ✅** @ `1220bfb`/`0abf164` · **★ G19 롱텀 통합재가 정본 ✅** BNK-69 · **★ G31**(공단 인증서 자동 연동 Won't v1) BNK-68 · merge **168 · FULLY UNBLOCKED** |
| **61차 G15·G29·G30** | **2026-06-11** (BNK-59~61 + planner 97차) — ogada **`eef07e5`/`9d7c17f` 49 route·67 page · **74.81%** · **★ G15 서식22 export ✅** @ `7389884` · **★ 제18호 가이드 ✅** @ `eecf0be` · **★ 시간 준수 ✅** @ `eef07e5` · **★ V65 계약 무결성 ✅** @ `24733c7` · **★ QA-B19 Fixed ✅** @ `695c0f7` · **신규 G29**(인지활동북)·**G30**(주기별 업무·모니터링) · merge **144 · FULLY UNBLOCKED** |
| 상세 문서 | `docs/planning/research/BENCHMARK_REPORT.md`, `docs/planning/research/COMPETITOR_MATRIX.md` |
| 활용 | 청구·정산 설계, MVP 차별화, 우선순위(§6) — `USER_STORIES`·`API_SPEC` 갱신 근거 |

#### 국내 주요 경쟁·유사 서비스 (2026-06-09 갱신 — BNK-10·12)

| 서비스 | 유형 | 주야간보호 | 핵심 특징 | 공개 규모·가격 |
|--------|------|-----------|----------|---------------|
| **케어포** | 민간 ERP (웹 + 직원 앱 + **가족돌봄앱**) | ✅ 전용 모듈 | **2단계 청구** + 본인부담 + **NFC 직원 출석** + 평가·CMS·간편결제 · **3-product line**(`daycare` 주야간·`intro_si` 시설·`intro_visit` 방문)·**demo-work=시설 셸**(`intro_si` 콘텐츠·이동서비스 없음) | **14,000+** 기관 / 월 **33,000원** flat (주야간, VAT 포함) |
| **이지케어** | 민간 ERP (웹 SaaS + **EZCARE 모바일 앱**) | ✅ 지원·확대 | **계획/청구 이중 일정** + **엑셀 공단 연동**(RFID 실시간 **2016 종료**, BNK-20) + **급여·4대보험·재무회계** lock-in; EZCARE **초대·명세**; **FAQ21825 직원 입사~퇴사 lifecycle**; 로그인 **`oCode`+ID+PW** | **9,330** 재가기관(2026.06.12, BNK-126) / 셋팅 **정가 55k→33k(40%)** · 월 10k+(N−10)×500+VAT |
| **엔젤시스템(LCMS)** | 민간 ERP (웹 + 직원 앱) — [lcms.or.kr](https://www.lcms.or.kr/) = **엔젤 동일 vendor**(BNK-127) | ✅ 지원 | **CMS 3-method**(계좌+카드+가상계좌·효성FCMS) + **사례관리 특허(제10-1120519호)** marketing + 평가·필수교육·큰화면·자동저장 UX | 상담 |
| **롱텀(공단)** | 공단 공식 | ✅ 급여청구 | **무료**. 공단 급여청구·심사·입퇴소 신고. **2026-01-16 개편** — IE 불가, Chrome/Edge 필수 | 무료 |

> **출처**: [케어포 cost.php](https://www.carefor.co.kr/price/cost.php), [이지케어 규모](https://www.easyms.co.kr/new/ezCare.html), [엔젤 LCMS](https://www.lcms.or.kr/), [공단 longtermcare](https://www.longtermcare.or.kr/) — 전체 URL·매뉴얼은 `BENCHMARK_REPORT.md` §7.

#### 케어포 — 청구·정산 실제 흐름 (벤치마킹 핵심)

> 출처: [케어포 교육 공지](https://www.carefor.co.kr/cs/view_notice.php?calmgno=43619), 매뉴얼 요약

**「공단 급여 청구」와 「본인부담금 청구」가 분리**되어 있다.

```
[일상 운영 — 케어포]
  출석·급여제공기록·일정 입력
           ↓
[① 공단 급여 청구 — 장기요양정보시스템(롱텀)]
  입퇴소신고 확인 → 청구서 조회·전송 → 공단 심사·지급
           ↓
  공단에서 「청구내역상세」엑셀 다운로드
           ↓
[② 케어포 연동]
  청구내역상세 엑셀 업로드 → 수급자별 공단 청구 건수 반영
           ↓
[③ 본인부담금 — 케어포]
  본인부담금 청구서 생성(개별/일괄) → 보호자 발송·수납 관리
```

| 단계 | 어디서 | 무엇을 |
|------|--------|--------|
| 급여비용 청구(공단→지급) | **공단 포털** | 장기요양급여비용 청구·전송 |
| 데이터 연동 | **엑셀 파일** | 공단 청구상세 ↓ 업로드 → 민간 ERP |
| 본인부담금(보호자→센터) | **케어포** | 명세서·청구서·수납·CMS/간편결제 |

※ 케어포도 공단과 **실시간 API 직접 연동**이라기보다 **엑셀 기반 연동** + 공단 포털 병행이 일반적.

#### ogada 청구·정산 설계 제안 (벤치마킹 기반)

| 단계 | MVP v1 목표 | 케어포 대비 |
|------|------------|------------|
| 1 | 출석·이용자·등급 → **급여 항목·본인부담금 자동 계산** | 동일 방향 |
| 2 | **월별 청구서·명세서** 생성·출력 (`/billing`) | 동일 |
| 3 | 공단 **청구내역 엑셀 import** (연동 기초) | 케어포 4단계 유사 |
| 4 | 공단 포털 **직접 전송** | MVP **제외** (공단 UI에서 수행) |
| 5 | 본인부담금 **보호자 발송·수납** | v1 이후 (알림톡·CMS) |

> **확정 (2026-06-05)**: 케어포와 동일 — **내부 계산 + 청구서·명세서 + 공단 엑셀 import**. 공단 직접 전송·CMS·보호자 발송은 후속.

#### 1-5-1. 경쟁사 대비 갭·차별화 요약 (2026-06-06 — `BENCHMARK_REPORT.md` §5, 3차 재검증)

**ogada 차별화 (유지)**

| # | 항목 | 경쟁사 동등 기능 |
|---|------|-----------------|
| 1 | **전국 B2B SaaS** — `platform_admin` Tenant 개통 (`/platform`) | 경쟁사는 셀프 가입(케어포) / 상담(이지케어) / 온라인 가입(엔젤) — **`platform_admin` 화면 자체가 차별** |
| 2 | **다지점 HQ 대시보드** + Branch Switcher | 경쟁사는 **1기관번호=1계정** 모델(△) — 공식 HQ 대시보드 **미확인**. ogada Org-Branch **명시적 차별** |
| 3 | **QR B방식** (보호자/이용자 → 지점 입구 QR) | 케어포=NFC(직원), 이지케어=RFID(방문), 엔젤·롱텀=없음 — **하드웨어 없이 스마트폰만** |
| 4 | **7역할 명시적 RBAC** (`platform_admin` 분리) | 경쟁사는 직종별 메뉴는 있으나 **SaaS 운영 역할(`platform_admin`/`sysadmin`) 분리 명시 없음** |
| 5 | **MVP 집중** — 출석·건강·청구·대시보드 | 경쟁사 평가·회계·직원급여 전범위 → ogada는 **구현 속도·파일럿 검증** 우선 |

**갭 (의도적 후속 / 검증 필요)**

| # | 갭 | 경쟁사 | ogada | 로드맵 |
|---|-----|--------|-------|--------|
| G1 | 보호자 **풀 포털/앱** (사진·푸시·명세 조회) | 케어포 가족돌봄앱 ✅ | △ MVP: QR + 기록열람 골격, 알림 없음 | **v1.1** (파일럿 후) |
| G8 | 보호자 **명세서 모바일**(초대·조회) | 케어포·**이지케어 EZCARE** ✅ | △ MVP: QR+열람 골격 | **v1.1** — 초대 흐름·명세 탭 (US-J01·J02) |
| **G8-h** | **알림 발송 이력**(케어포 10-7 안내발송내역) | 케어포 **10-7** ✅ | ✅ **`NotificationHistoryPanel`** @ `e39164d` · BE API @ `c53dd3b` lineage | **v1.2.1 ✅** (US-J03-h) · **실발송(10-1) v1.1/v2** |
| G2 | **CMS·간편결제** (본인부담 자동이체) | 케어포·엔젤(LCMS) ✅ — **엔젤 CMS 3-method**(계좌+카드+가상계좌·BNK-127) · **LCMS 해지 workflow**(BNK-144) vs ogada **CMS 자동이체 단일** | △ **등록+해지 ✅ partial** — duplicate guard+cancellation API+cancelled history+FE cancel modal @ `72aff00`/`4a622ab`/`9a6fdb6` · **★ 7-5 간편결제 ✅ partial+** — `/billing/easy-pay`·Stub PG+pilot E2E+prior-month guard @ `c9baca2`/`438f5c7`→`bebd874`/`b893e97` (BNK-189~190) | **v2 P1** — Hyosung FCMS **실연동** · **7-5 live PG·G2b P2**(BNK-190) |
| **G2-n** | **보호자 명세·법정서식 발송**(케어포 7-1·엔젤 이메일) | 케어포 **7-1** ✅ · 엔젤 **이메일** 법정서식 | △ **`POST /billing/claims/{id}/notify`** + UI @ `c48fb67`/`84f3441` · **templates 5종 partial** @ `0854fbd`/`eedcc80`(명세·기록지·가정통신문·**납부확인서·학대예방교육**) · **SMTP 실연동 잔여** | **v2 P1** `in_progress` (BNK-45) |
| G3 | **공단 평가 2026 지표** 자동화·서식 | 케어포·엔젤·이지케어 ✅ | ❌ | **Could** (영업 차별 아님) |
| G4 | **재무회계·세무·4대보험** | 이지케어 ✅ | ❌ | **v3 Must** (결정 90 — W3) |
| G5 | 이동서비스·프로그램·식단·**요양리포트·위생·직원HR** | 케어포(주야간 전 모듈) ✅ | △ v3 **FE POST 닫힘** @ `6a59b74` + **v3.1 Must(결정 94)** | **배차 = v1.3** · **식단·프로그램 기본 CRUD = v3 ✅** · **3-3~3-7·5-3~5-10·6-2~6-4·8-2~8-13 = v3.1 Must** |
| **G15** | **이동서비스 법정 서식**(별지 제22호 일지·제18/19/20 신청·제공기록지 차량번호) — 2026 평가 점검 | 케어포·엔젤·이지케어 ✅ | △ **FE+BE 대부분 ✅** — func 2-7/2-8·2-9·audit trail·PUT persistence·**legal fields validation**·**compliance 가이드**·**driver signature** ✅ @ `b4644e8`/`0df6902`/`f51e365` · **★ BNK-347** 엔젤 지표41/42 **partial+++**·NHIS #44 **175차 zero drift** · **★ BNK-375** silverangel 정적 점검표 대비 **실데이터 일지 full-stack 우위 ✅** · **잔여 P2 Should**: 계약서 수칙 제공(②) UX polish | **v1.3-C** — A단계는 「운영 편의용」 명시 (BNK-7 §10-3) |
| **G16** | **차량 마스터·정원·이동서비스비 청구** | 케어포 2-4·2-5 ✅ | ✅ **FE+BE ✅** — `VehiclesPage` `/transport/vehicles`·`TransportVehicleSelect` @ `107bfb3`/`08dbcf0` · **이동서비스비 청구·`transport_service_fee` API+FE E2E ✅** @ `88d4c59`/`9dfef92` · **#44 P0 seed ✅** — RU_3/RU_4 **5230/8630** @ `39ee679` · **joHistory 95차 zero drift** `c886ff1f` · **lawImg 95차 DRIFT 404**(BNK-235 · V103 evidence 유지) | **v1.3-C** — 러-1~4 **830/2,630/5,230/8,630원**(BNK-174 정본·joHistory verbatim) |
| **G17** | **2026 평가 기능회복훈련** — **지표25(계획 2점)+지표26(실행 3점)+지표27(개인별 계획 3행)** | 케어포·이지케어 ✅ · 엔젤 **지표27 verbatim** · **공지46105** | ✅ **FE+BE 3행** — `FunctionalRecoveryPage` @ `c288fdd`/`b58429d` · BE V72 @ `73e169a` · **지표27 row2/row3 compliance** @ `e820b28`/`21b1855`/`f1c60fe` · **live E2E harness** @ `c413615` · **★ API contracts+422 guard ✅** @ `8b0c6c7` | **v1.2.1 ✅** · **live E2E run P1** (BNK-87~102 · v3.1 `FUNCTIONAL_RECOVERY` 병행) |
| **G18** | **주야간 내 단기보호 시범**(2026.1~무기한·월9일·전산 4챕터) | 케어포 ✅ · [silvercare 공지](http://www.silvercare.org/info/notice_view.asp?b_idx=16929) ✅ (BNK-235) | ❌ — **G18-SHORT-PILOT P3** · G-FAMILY-LEAVE와 **`ShortTermCareContract` 통합** 권고 | **Won't v1** · **P3/v3.x+** (BNK-9·235) |
| **G19** | **통합재가서비스** | 케어포 ✅ · [롱텀 통합재가 안내](https://www.longtermcare.or.kr/npbs/e/b/610/npeb610m01.web?menuId=npe0000002731) ✅ · [provider search](https://www.longtermcare.or.kr/npbs/r/a/201/selectLtcoSrch.web?menuId=npe0000002783) ✅ (BNK-231) | △ **지점 폼 라벨 partial** @ `4c7c994` · **정본 md5 `0ea575be`** — 「**주·야간보호형: 수급자 1인당 월 10만원 지급**」+ 가정방문형 110% · **provider discovery harness △** @ `41d8de5`/`8cb8789` · **FE discovery UI ❌** | **Won't v1** · **v2+ Epic V P1** — addon 상호배타 가드 + 기관 discovery FE wire (BNK-231~235) |
| G6 | NFC/RFID 출석 (직원·태그) | 케어포·이지케어 | ❌ (QR B로 대체) | **의도적 — B방식 유지** |
| G7 | 공단 엑셀 **컬럼 스펙** 실측·**`처리상태` 선행열**·**대기(보류) 3상태 UX**·**import live guidance**·**US-G04 연도 수가 가드**·**본인부담 공단 비교 partial**·**★ web-first import(이지링크 PC 에이전트 미의존 차별화 「가정」)** | 케어포 3상태(성공/오류/대기) · 이지케어 **엑셀 표준**·**★ FAQ21764 이지링크(EzLink) PC 클라이언트**(직원/수급자·방문일정 가져오기·BNK-297) · [연도 수가 미적용](https://docs.channel.io/ezcare/ko/articles/%EA%B3%B5%EB%8B%A8%EC%9D%BC%EC%A0%95-%EA%B0%80%EC%A0%B8%EC%98%A4%EA%B8%B0-%EC%8B%9C-%ED%95%B4%EB%8B%B9-%EC%97%B0%EB%8F%84-%EC%88%98%EA%B0%80-%EB%AF%B8%EC%A0%81%EC%9A%A9-0ccb9026) 사후 안내 (BNK-79) · [본인부담금 비교기능](https://docs.channel.io/ezcare/ko/articles/%EB%B3%B8%EC%9D%B8%EB%B6%80%EB%8B%B4%EA%B8%88-%EB%B9%84%EA%B5%90%EA%B8%B0%EB%8A%A5-%ED%99%9C%EC%9A%A9%ED%95%98%EA%B8%B0-%EB%B6%88%EC%9D%BC%EC%B9%98-%ED%99%95%EC%9D%B8%EB%B0%A9%EB%B2%95-2d53ea63) 「일정확정 전 공단 대조」(BNK-87) | ✅ BE **`PENDING_REVIEW`** @ `4cc328d`/`dd49204` · FE **`Badge`·`NhisReconciliationTable`·`NhisPendingReviewGuide`** @ `fbb0b7a`/`16402b2` · **대시보드 `nhisPendingReviewCount`** @ `1794e1c` · **live guidance ✅** @ `1220bfb`/`0abf164` · **★ US-G04 FE+BE upload guard ✅** @ `53e4016`/`970c7af` · **★ NHIS comparison panel partial ✅** @ `0adf8c6`/`2225a7a` | **UX 닫힘** · **파일럿 실파일 BLOCK** (#27) · **본인부담 공단비교 P2 잔여** |
| **G9** | **수가표 시간대** (`duration_band`) — 등급×이용시간 2차원 | 케어포·이지케어 ✅ | ✅ **FE+BE E2E** — 25셀·`durationBandSnapshot`·폴백 @ `0c34f85`/`0719648`/`6fe853b`/`5348d9c`/`eb3f0fd` (BNK-41·42) | **v1.2.1 ✅** |
| **G11** | **수가 가산율** — 야간20·심야30·휴일30·유급휴일50% (중복불가) | 이지케어 **(가산)수가 자동계산** 명시(BNK-20) | ✅ **catalog+가이드+자동 가산 E2E** @ `904072b`/`3db8db3`/`d7475fd` — `FeeSurchargeRateCatalog`·`GET/POST fee-surcharge-*`·`FeeSurchargeGuidePanel`·청구 자동 적용 | **v1.2.1 ✅** (US-M05 · BNK-53·56·58) |
| **G12** | **월15일↑ 추가산정** | 케어포·공단 ✅ | ❌ | **v1.1~v2** — 파일럿 표준운영 드묾 |
| G13 | **본인부담 수납 lifecycle** — 입금·미납 (7-2·7-3) | 케어포 func 7장 ✅ | △ UI+**pagination·reminder·cross-page hardening** @ `c72e9df`/`e6df92c` · **US-L01 overpayment guard ✅** @ `dd72ff8`/`4109680` · **★ `paidAt` 필수 가드 ✅** @ `ed730a2`/`0024c88` (BNK-73 · 케어포 7-2 패리티) · **은행엑셀 BE+FE ✅** @ `e50533f`/`9ffff0c` · **은행 8종 E2E live 잔여** · **live run 잔여**(결정 73) | **v1.2 P0** (US-L01·L02) |
| G14 | **등급 변동 이력** (1-9) · **수급자 급여계약 lifecycle** (FAQ21805) · **★ NHIS 10-field 급여계획서 작성**(FAQ21802) | 케어포·엔젤 ✅ · 이지케어 FAQ **21805** [비정기] 계약 ✅ · FAQ **21802** 급여계획서 ✅ | ✅ 등급이력 UI+DB(V48)+GET API @ `15e41e3` · ✅ **계약서 파일함 Route+첨부 API** @ `2642838`/`6f3315a`/`5be9070` · ✅ **NHIS 10-field plan-form ✅** V164·`ClientCarePlanFormService`·`/clients/:clientId/care-plan-form` @ `34eb47a`/`ce422e3`/`d723d5a`(BNK-433) · ❌ **계약 lifecycle**(비정기 갱신·해지·서명) | **v1.2.1 P0 ✅** (US-M01·US-T08b) · **plan-form ✅** · **계약 lifecycle P2** (US-T10 · BNK-117~126) |
| **G37** | **등급 인정기간별 첨부 PDF**(이지케어 Channel.io 49a778e8·「돋보기 미리보기」) | 이지케어 ✅ | ✅ **FE+BE ✅** — V78+V79·`GradeHistoryAttachmentPanel`·live E2E harness·MIME fallback guard @ `e026ae9`/`6875af5`/`e9d1178` | **v1.2.1 ✅** (BNK-105~109 · US-M01-g) |
| **G38** | **급여제공계획서 통보 모니터링**(이지케어 FAQ 21802·황갈=5·11개월·빨강=재발급 미반영) · **plan-form 작성은 G14-NHIS 분리** | 이지케어 ✅ | ✅ **monitor FE+BE ✅** — BE `@5fd35a6`/`a9f8bda`/`a0a7f9c` · FE dashboard widget+live E2E+partial-load warning @ `28c22b0`/`4b2b082`/`87e6fae` · **snapshot aggregation ✅** @ `8fa9f3d`/`f72da41`(QA-B49 Fixed) · **★ plan-form 작성 → G14 ✅** @ `d723d5a`(BNK-433) | **v1.2.1 ✅** (BNK-106~118 · US-T08 monitor · **US-T08b plan-form**) |
| **G14-NHIS-PLAN-FORM** | **NHIS 10-field 급여계획서 작성·연도별 persist**(FAQ21802·5/11개월·재작성) | 이지케어 FAQ **21802** ✅ | ✅ **FE+BE ✅ full-stack** — V164·`ClientCarePlanFormService`·`GET/PUT /api/v1/clients/{id}/care-plan-forms/{year}` @ `34eb47a`/`80b9619` · FE `ClientCarePlanFormPage`·Route `/clients/:clientId/care-plan-form` @ `ce422e3`/`d723d5a` · FAQ21802 cross-walk ✅ | **v1.2.1 ✅** (BNK-433 · US-T08b) |
| **G-BILLING-PRIOR-DEPOSIT-GUARD** | **청구 전 선행 입금 가드**(케어포 PDF p.85 「7-1 청구 전 7-2 선행 입금」) | 케어포 PDF p.85 ✅ | ✅ **dashboard due-gate widget+API ✅ full-stack** @ `0d233b9`/`07a03c0`/`07a03c0`(BNK-436) | **v1.2.1 ✅** (BNK-436 · US-M02-c widget) |
| **G-BANK-EXCEL-8** | **은행 8종 일괄입금 엑셀**(케어포 PDF p.88) | 케어포 PDF p.88 ✅ | ✅ **full-stack closure ✅** — BE 8-bank catalog+preview+import @ `e3b74a0`/`2f6f3bc` · FE `BankDepositImportPanel` @ `a18b30e` · BE non-positive row guard @ `7d29a38`(merge pending QA-B182) · legacy US-L01 generic import ✅ @ `e50533f`/`9ffff0c` | **v1.2.1 ✅** — BNK-445~446 · US-L01 · **은행 8종 E2E live 잔여** |
| **G-STAFF-NHIS-EXCEL-IMPORT** | **요양보호사 NHIS 엑셀 일괄등록**(케어포 PDF p.95 8-1-2 공단연동) | 케어포 PDF p.95 ✅ | ✅ **full-stack closure ✅** — BE `StaffNhisCaregiverImportController` preview+import @ `2f6f3bc` · FE `StaffNhisCaregiverImportPanel` @ `4315ee2` · 6-status Badge+row selection normalize | **v1.2.1 ✅** — BNK-444 · US-R03 |
| **G-BATHING-SCHEDULE-PREV-MONTH-COPY** | **목욕일정 전월 일괄생성**(케어포 func.php 3-3·PDF p.45 module3) | 케어포 func 3-3 △ · ezCare FAQ21191 방문목욕(out-of-scope) | ✅ **full-stack closure ✅** — BE `POST /api/v1/care/bathing-schedules/copy-from-previous-month` @ `49a1721`/`a426663` · FE `BathingSchedulesPage` 전월복사 wire @ `9a957fb` · `createdCount`/`skippedCount` toast | **v3.1 ✅** — BNK-466 closure · **183차 P2 candidate 제거** |
| **G-STAFF-DOCUMENT-REPOSITORY** | **직원 인사서류 21-slot repository·진행률**(케어포 PDF p.96 zone③ 20-doc + FAQ21825 lifecycle) | 케어포 PDF p.96 zone③ 20-doc △ · ezCare FAQ21825 lifecycle ✅ | ✅ **full-stack closure ✅** — FE `StaffDocumentRepositoryPanel` 21-slot @ `03d0d43` · FE repository-progress API wire @ `fd15a2f` · BE `StaffDocumentRepositoryCompliance`+`GET /staff/hr-files/users/{userId}/repository-progress` @ `b583c11` · **21-slot superset** | **v1.2.1 ✅** — BNK-470~471 · US-R03c · **470차 P3 candidate 제거** · **mobile upload P3 carry** |
| **G-MENU-PERMISSION-MATRIX** | **계정×메뉴 fine-grained 권한 매트릭스**(ezCare FAQ21695) | ezCare [**FAQ21695**](https://ezcare.easyms.co.kr/help/faq.ez?rowid=21695&type=web) ✅ | ❌ — ogada 7-role JWT RBAC only · **per-account×per-menu partial deny 없음** | **P3「가정」** — BNK-471 · v3 enterprise · MVP out-of-scope |
| **G15-KAKAO-QUOTA-DASH** | **HQ 대시보드 Kakao API quota 위젯**(외부 map API 잔여 가시화) | 케어포·이지케어·엔젤 **❌** | ✅ **HQ dashboard widget ✅ closure** — `buildTransportKakaoQuotaDashboardWidget` 4-tone·role `hq_admin/sysadmin`·`GET /api/v1/transport/kakao-api-status` @ `580a86b`/`a8ccb04` · **ogada exclusive**(BNK-464) | **v1.3-A ✅** — BNK-464 · US-M02-d · **177차 P3 candidate 제거** |
| **G-ORAL-CARE-PERIOD-REPORT** | **구강관리 1/2/3개월 리포트**(케어포 PDF p.45 module3 3-4) | 케어포 PDF p.45 ✅ | △ `/nursing/oral-care-checks` CRUD ✅ · **multi-period report template ❌** | **P3「가정」** — BNK-441 candidate · MVP out-of-scope |
| **G-STAFF-LEAVE-STATUS** | **직원 휴직(ON_LEAVE) lifecycle 상태**(ezCare FAQ21720) | ezCare [**FAQ21720**](https://ezcare.easyms.co.kr/help/faq.ez?rowid=21720&type=web) ✅ | ✅ **full-stack closure ✅** — `STAFF_LIFECYCLE_STATUS.ON_LEAVE`+CHECK `V166` @ `1d7cee2` · `StaffLifecyclePanel` 「휴직」 combobox+warning Badge @ `2581347`/`5f1815f` · `StaffLifecycleSummaryPanel`+`GET /api/v1/staff/lifecycle-summary` `onLeaveCount` · ON_LEAVE→ACTIVE 복직 regression(QA-B187/B188 Fixed) | **v2 ✅** — BNK-452 · US-R03b · **180차 P3 candidate 제거** |
| **G-COMM-CALLER-AUTH** | **문자 발신번호 본인인증·관리**(silverangel `부가서비스>문자발신번호관리`) | silverangel [**notice 221562**](https://www.silverangel.kr/silverangel/support/notice/view.do?pageNo=1&Tmp_idx=221562) ✅(인증 마감 2026-06-23) | ❌ — SMS 9-event 발송만 ✅ · **발신번호 self-verification/관리 화면 없음** | **P3「가정」** — BNK-452 · MVP out-of-scope · 경쟁사 6/23 마감 compliance 인텔 |
| **G-BILLING-DEPOSIT-HALFMONTH-REPORT** | **입금대장 반월 split**(케어포 PDF p.91 ②) — 1~15일·16~말일 | 케어포 PDF p.91 ✅ | ✅ **full-stack closure ✅** — `/billing/reports/deposits` `period=FULL|FIRST_HALF|SECOND_HALF` + `appliedFilters.depositPeriodLabel` @ `e38ccfd`/`375fb9d`/`b96d038`/`c6a412f` | **v1.2.1 ✅** — BNK-455~457 · US-L08 · **180차 P3 candidate 제거** |
| **G-BILLING-RECEIPT-DUAL-BASIS** | **수납대장 청구/수납 2-track**(케어포 PDF p.91 ③) | 케어포 PDF p.91 ✅ | ✅ **full-stack closure ✅** — `/billing/reports/receipts` `basis=PAYMENT|CLAIM` + `appliedFilters.receiptBasisLabel` @ `e38ccfd`/`375fb9d`/`b96d038`/`c6a412f` | **v1.2.1 ✅** — BNK-455~457 · US-L09 · **180차 P3 candidate 제거** |
| **G-BILLING-APPLIED-FILTERS-WIRE** | **billing report appliedFilters FE wire**(케어포 PDF p.91 인쇄 헤더 server metadata) | 케어포 PDF p.91 ✅ | ✅ **full-stack closure ✅** — BE echo @ `14935a3` · FE `billingReportFilters.js` server `appliedFilters.*Label` 우선 @ `c6a412f` | **v1.2.1 ✅** — BNK-456~457 · **P3 candidate 제거** |
| **G-BILLING-DEPOSIT-ORDER-GUARD** | **입금·청구 순서 가드 3-channel uniform**(manual+CMS+EasyPay·케어포 PDF p.85) | 케어포 PDF p.85 ✅ | ✅ **3-channel uniform closure ✅** — manual guard @ `abddbee` · CMS guard @ `dfa981c` · EasyPay guard @ `dfa981c` · KPI CMS 0.6→0.65 | **v1.2.1 ✅** — BNK-491~492 · US-L01 |
| **G-BILLING-REPORT-FILTER-PERSISTENCE** | **청구 리포트 월별 필터 저장·복원**(GET/PUT persist·인쇄·재발행) | 케어포 PDF p.91 △ | △ **BE partial ✅** — V170 `billing_report_filters` · `GET/PUT /billing/reports/filters` @ `479995e` · **FE persist wire ❌** | **P2** — BNK-493 · US-L08 · TWR 302 gap #4 partial |
| **G39** | **급여제공결과평가**(silverangel **지표44**·주1 상태변화·월1 기록지·**연1** 평가·30일 재작성) · **이지케어 FAQ21801 지표24 반기1회 nuance** | 엔젤 **지표44** ✅ · silverangel verbatim · 이지케어 **FAQ21801 반기1회** ✅ (BNK-134) | ✅ **FE+BE ✅** — V80·`ProvisionResultEvaluationPage`·dashboard weekly/monthly widget @ `8e66ae8`/`a16e1fe`/`a0a7f9c` · **snapshot aggregation ✅** @ `8fa9f3d`/`f72da41`(QA-B49 Fixed) · **★ guardian dispatch UI ✅** @ `4d1a4f2` · **★ care-provision dispatch pilot E2E △** @ `73094f9`/`73df04d` (BNK-234~235) | **v1.2.1 ✅** · **live E2E run P1** · 반기 vs 연1 주기 nuance 교차검증 (BNK-134 · US-T08) |
| **G22** | **본인부담 대장 리포트** (7-6~7-10) | 케어포 7장 ✅ | ✅ @ `dbf485e` · **7-9 환불 ✅** @ `212e010`/`de49b21` (7-2-1 → **G26**) | **v1.2.1 P1 ✅** (BNK-16·BNK-84~85) |
| **G20** | **시설급여 특화**(생활실·욕창·집중배설 — demo-work) | 케어포 demo-work ✅ | ❌ | **v3 Must** (결정 90) |
| **G21** | **방문요양·계획/청구 이중 일정·NHIS import·billing confirm-lock·batch-confirm readiness·RFID compare** | 이지케어 3-1·FAQ21782 ✅ · **Channel.io plan/claim 3-source** ✅ (BNK-250) · **schedule-rfid `comp_01`~`comp_09`** ✅ (BNK-346~352) · **`schedule-fix` 6단 확정 게이트** ✅ (BNK-365) | ✅ **batch-confirm readiness full-stack closure**(△→✅) — BE `VisitConfirmReadinessResponse` draft/paired-diverged/unassigned/confirmed × **PLAN/BILLING split** + `readyPlan`/`readyBilling` per-kind 플래그 + blocker 라인 + **미배정 draft 거부** @ `f26abb0`/`5f710e3` · FE `VisitBatchConfirmPanel` PLAN/BILLING split 카운트 wire @ `f9ed97d` · **RFID 7-code diff compare ✅ full-stack** @ `27c9de3`/`4a112fe`/`1ca6c19`(BNK-351~352) · **standalone NHIS comparison panel ✅** @ `797c529`(BNK-372) · diff code variant normalize @ `570912e`(BNK-367) · **청구반영 검은/빨간 배지 ✅ full** @ `25ca88e`(BNK-261) · **plan/claim 분리 UI·RFID split-view P2** · **live E2E 잔여** | **v2 Must** `in_progress` (결정 90 · BNK-42·197~198·250·261·346~352·362~367) |
| **G23** | **대기 수급자**(케어포 1-1-1) | 케어포 **1-1-1** ✅ | ❌ (`status=WAITLIST` 가정) | **P2** — v2 후속 검토 (BNK-28) |
| **G24** | **정기 욕구사정(지표15)·리포트 전수** · **FAQ21800 8-item parity** | 이지케어 FAQ **21800** ✅(BNK-434 8/8 parity) · **FAQ21810** 8 세부항목 ✅ (BNK-226) · 케어포 **1-2/1-3 기초평가** ✅ (BNK-125 triple-source) | ✅ **욕구사정 Form+Compare+Panel+API+가정방문 일자** @ `2642838`/`6f3315a`/`b238779`/`5be9070`/`479e064` · **★ G24b 8항목 ✅ full** V128 @ `45fb6d9`/`49fbf67` · **★ compliance API+dashboard widget ✅** @ `98002d4`/`f4c8beb`/`ca0b627`/`baa6d6d` · **★ compliance list page ✅** @ `eb16734` (BNK-232~233) · **★ FAQ21800 fiscal year compliance ✅** · **총평 전용 필드 △**(`homeVisitNotes`) → **P3 carry** | **P2 ✅ full stack** (BNK-226~234 · US-T09 · **live E2E run P1** · QA-B95 env 선행) |
| **G25** | **본인부담률 엑셀 업로드·7-1 재계산**(케어포 1-1-2·공지920) | 케어포 **공지920** ✅ | ❌ | **P2** — v2 후속 (BNK-35) |
| **G31** | **공단 인증서 자동 일정 연동**(이지케어 Channel.io live pull) | 이지케어 **범용 기관 인증서·계획/청구 2트랙** ✅ | ❌ (엑셀 import=업계 표준) | **Won't v1** · **P2** 온보딩 「공단 포털→엑셀→ogada」3단 가이드 (BNK-68 · 벤치마크 G25 라벨 → **G31** 확정) |
| **G26** | **7-2-1 의료비공제(연말정산)** — 보호자 납입증명 자동 산출 | 케어포 **7-2-1** ✅ | ✅ **FE+BE E2E** — `MedicalExpenseDeductionPanel`·CSV export·**CMS/easy-pay 제외** @ `7e5c806`/`c1d9788`/`1af5b1f` · **★ NTS xlsx 레이아웃 partial ✅** @ `fd569d7` · **★ ClientDetail billing tab xlsx E2E ✅** @ `48827b6` · **★ 7-8 통계 대시보드 ✅ full stack** @ `903f462`/`6d10e0d`(BE)·`d8f1fdf`(FE `/billing/reports/statistics`) (BNK-263~268) | **v1.2.1 ✅** · **국세청 실파일 제출 검증 P2** · **이동서비스비 통계 leaf P1** · ※ BNK-44 「치매전담실」은 **P3 보류** |
| **G32** | **사례관리 회의록**(엔젤 지표43·케어포 **8-5**·이지케어 **FAQ21797·FAQ21740**) — 반기·3인(직종별)·**참가 직원별 의견 필수**·6필드+**사례관리 계획**·30일 반영·**지표29 평가실시**·**대시보드 due gate** | 엔젤 **지표43+지표29** ✅ · 케어포 **8-5** ✅ · 이지케어 **21797** 반기·3인·서명·per-speaker opinions ✅ · **FAQ21740** 반기별 1회 cadence ✅ (BNK-91~392·458) | ✅ **FE+BE 6/6 full-stack** — `CaseManagementPage`·V75 `case_management_plan` @ `443f379`/`40c303d` · **BE+FE `evaluationConductedMet`** @ `11277b9`/`7f2289b` · **★ `attendeeOpinions[]` + V156 `attendee_opinions JSONB`** @ `5222a8f`/`b272a7b` · **★ dashboard `caseManagementAttendeeOpinionGapCount`** @ `b9e0947`/`e55ae96` · 30일 widget @ `0821ce8` · **★ API contracts+422 guard ✅** @ `8b0c6c7` · **★ FAQ21740 반기별 1회 parity deepen ✅**(BNK-458) | **v1.2.1 ✅+** · **live E2E P1** · G24/G30 묶음 (BNK-91~392·458) |
| **G27** | **재가급여 월한도액 2026** — 등급별 cap·초과 경고 | 케어포 **10-2-1** ✅ | ✅ **BE catalog+guard** @ `a92e625`/`20bc1be`(1등급 2,512,900~5등급 1,208,900·**인지지원 676,320**) · **FE 표기·초과 경고 E2E** @ `5e64125`/`fba5ea8` | **v1.2.1 ✅** (US-M04 · BNK-47·49·52) |
| **G28** | **청구 생성기준·전월 입금 가드** | 케어포 9-1·7-1↔7-2 | ✅ BE @ `b953662`/`857bd32` · FE @ `5bdb476`/`911e732`/`25f3225` | **v1.2.1 ✅** (US-M03-b · BNK-49) |
| **G29** | **인지활동북 자료실**(인지훈련 학습지 PDF·낱장 출력) — **G-COGNITIVE-WORKSHEET** | 이지케어 **시범** [FAQ 21781](https://ezcare.easyms.co.kr/help/faq.ez?rowid=21781&type=web) ✅ — 「인지맞춤형 학습지·낱장 출력·하반기 확장」(BNK-297) | ❌ (`/programs` CRUD·G17b skipReason/참여기록만) | **v3.1 P3** (BNK-59·297 · G17 연계 · MVP out-of-scope) |
| **G30** | **주기별 업무 가이드·2026 모니터링 문항 대응** — FAQ21842 「직전 6개월 매월 자가진단」·**FAQ21841 유선상담 5명·60% Y**·**FAQ21812 관리자 라운딩**·**FAQ21813 업무수행일지**·**통합 checklist aggregate** | 이지케어 FAQ **21782~21842** 64건 ✅ · **FAQ21841** 5명·60% verbatim ✅ (BNK-250) · 엔젤 **지표29** 평가실시 ✅ | ✅ **full** — self-diagnosis+phone consultation @ `6f6915f`/`b8e92bf` · **integrated checklist** @ `b1dfd34`/`400c835`/`5146895` · **monitoring evidence window ✅ deepen** @ `73df04d` · **★ phone satisfaction panel ✅ full** @ `344a28b`/`9ad8346`(`satisfiedCount` StatCard) | **P1 ✅ full** · **live API E2E verify P1** |
| **G33** | **청구시작 기준금액**(PDF p.90 `7-3.청구시작 금액설정`) — 도입 전 미납/선납·1회 생성 후 변경 불가 | 케어포 **매뉴얼 PDF** ✅ (func.php `7-3`=미납관리와 **번호 충돌** · BNK-98 삼원 불일치 정책) | ✅ **FE+BE E2E** — settings @ `3d5eb3e`/`9e1a2ed` · ledger @ `e7df238` · overdue @ `deaae7a`/`7564c2a` · settlement API @ `70e6191` · **settlement UI** @ `359cf0c` · **V77 integrity** @ `42bc06e` · **★ pilot E2E+reload fallback ✅** @ `730792b`/`eb488799` (BNK-94→100) | **v1.2.1 ✅** · **live E2E run P1** |
| **G34** | **선임 요양보호사 업무수행일지**(`8-1-2`)·**보수교육**(`8-7-1`)·K-MMSE·**전자서명 문자 인증**·문자 부가과금 안내 | 케어포 **func.php `8-1-1`/`8-1-2`/`8-7-1`** ✅ · 엔젤 **11종 서명** · FAQ **45982** K-MMSE·문자 별도 과금 ✅ · Channel.io **2974fadd** 전자서명 문자 인증 ✅ (BNK-105·118~144) | △ **업무수행일지+전자서명+8-7-1 ✅** — Route·CRUD·`SignLeadCaregiverWorkLogModal`·`/staff/training`·BE compliance+cert API·FE cert UI @ `314b380`/`51477bd`/`0a7fe16`/`50bdb6e` · **잔여 P2**: 케어포 8-7-1 리포트·FAQ21807+**21828** 교육일지 | **P2 △ partial→✅(8-7-1 core)** — func.php depth-3 verbatim·8-7 리포트·교육일지 잔여 · **P3** FAQ21798 홀/짝 nuance (BNK-137~144 · US-S01·US-S02) |
| **G-Health-8-10** | **직원 건강검진**(케어포 8-10·이지케어 **FAQ21799** 지표9) — 실시일·파일함·5영역·사무직 2년/일반 1년 | 케어포 **8-10 건강검진관리** ✅ · 이지케어 **FAQ21799** ✅ · **PDF 8-10.현황 리포트 ≠ func 8-10.건강검진** (BNK-138) | △ **✅ partial+** — `/staff/health-checkups`·5영역·`StaffStatusReportPage` 집계 ✅ · **★ BNK-339** FAQ21799 parity ✅ · **★ 신규직원 1년 이내 서류 자동검증 △ @ `8e6310a`**(`StaffLifecyclePanel` ⑥ 연동) · **잔여 P2**: 직원 파일함 스캔 보관 deepen | **P2 △ partial+** — US-R02·US-R03·FAQ21806 연계 |
| **G-Staff-LC** | **직원 입사~퇴사 lifecycle** (이지케어 FAQ **21825**·**21806**·**21823**) — 파일함·근로계약서·4대보험·퇴사 체크리스트·**근로계약 갱신** | 이지케어 FAQ **21825**·**21806**·**21823** ✅ · 케어포 8장 일부 | △ **core wired+V91 HR hub+FAQ21806 V92 ✅ partial+FAQ21823 △ partial+** — BE API+V86+V87+V91+V92+FE lifecycle·`StaffHrFilePanel`+onboarding summary @ `75440bc`/`e76ca06`/`d4ee057`/`4efa168` · **FAQ21823 △ partial+** @ `1b6d2b1`/`033b319`/`16afd4c`(5항 checklist·서식 modal·lifecycle tab·renewal record·급여대장 0) · **FAQ21806 6단계 workflow CRUD ❌ P2** | **P1 core ✅ / P2 FAQ21806 workflow / P2 FAQ21823 deepen** — US-R03 (BNK-129~151·417~422) |
| **G40** | **신규입소 위험도평가**(silverangel 지표21·급여개시 전) — 낙상·욕창·인지기능 3종 스크리닝 | silverangel **essential L1767–1776** ✅ · 케어포 1-2/1-3 기초평가 일부 | ✅ **partial+** — V93/V94+FE Panel+compliance widget @ `72676a5`/`686d686`/`e89175e` · **live E2E run 잔여** | **P2 ✅ partial+** — US-T11 · G24 욕구사정 ✅와 대칭 lifecycle (BNK-150~154) |
| **G34b** | **업무수행일지 불러오기**(이지케어 FAQ21813·지표11·모니터링 7) — 욕구사정·급여계획 템플릿 재사용·전월 clone·인지활동 role | 이지케어 [**FAQ21813**](https://ezcare.easyms.co.kr/help/faq.ez?rowid=21813&type=web) ✅ · G34 lead work log ✅ | ✅ **partial+** — import @ `0ce04ad` · clone @ `1b5fabe` · role guard @ `994f5ea`/`b6ecc35` · import-draft API @ `8487667` · **live E2E run 잔여** | **P2 ✅ partial+** — US-T13 · G34/G30 연계 (BNK-160~163) |
| **G42** | **고충상담 기록·전자결재**(이지케어 FAQ21814·지표7) — 접수·익명함·사후관리 | 이지케어 [**FAQ21814**](https://ezcare.easyms.co.kr/help/faq.ez?rowid=21814&type=web) ✅ · 케어포 func **8-8** ✅ | ✅ **partial+** — `/staff/grievance-counselings`·V97·follow-up checklist+approval queue @ `14124d6`/`bcb1d9f`/`892450a`/`a7a6004` · **잔여 P2**: 익명함·전자결재 UI deepen | **P2 ✅ partial+** — US-T14 · G30 모니터링 checklist 연계 (BNK-161~175) |
| **G-Health-8-12** | **직원 현황 리포트**(케어포 **8-12**·PDF p.106 7종) — 명부·사진게시·연락처·월간명부·입퇴사·엑셀 | 케어포 **8-12.현황 리포트** ✅ · demo `L08_M09` `view.staff_report` ✅ | ✅ **partial+** — aggregated API·referenceDate·exports @ `bf6dd25`/`07956f5` · **PDF 7종 FE ✅** @ `07956f5` · **live E2E harness ✅** @ `ccc4d75` · **BE CSV export ✅** @ `bc927f7` · **BE CSV FE wire ✅** @ `488f547` · **pagination ✅** @ `ff173af` (BNK-172~179) | **P2 ✅ partial+** — US-R02 · **잔여 P2**: print layout·live run |
| **G34-QUAL** | **팀장급 요양보호사 자격기준**(이지케어 **FAQ21837**·고시 48~58조) — 실무경력 **5년**(월 60h×60개월) | 이지케어 [**FAQ21837**](https://ezcare.easyms.co.kr/help/faq.ez?rowid=21837&type=web) ✅ | ✅ **partial+** — FE gate @ `443efca`·BE enforce @ `726b3de`·compliance API @ `9a8bd2a`·FE panel @ `574bd08`·pilot E2E @ `997831c` (BNK-177~183) | **P2 ✅ partial+** — G34·US-S01 연계 |
| **G41** | **기관 교육일지 8-7**(케어포 func·FAQ21807/21808/21828) — 노인인권·운영규정 4필드·신규직원 7일·**반기1회+ nuance**·PDF 8-7 alerts·8-7-1 export | 케어포 **8-7.교육일지(노인인권, 재난, 소화, 직원권익)** ✅ · FAQ21807 **반기1회+** ✅ · FAQ21808 **23 topics** ✅ | ✅ **✅+ deepen** — FE+BE+compliance+live E2E harness @ `e14ba10`/`32f87f1` · **★ enum 23+ ✅** V129 @ `b1c92e1` · **★ 대시보드 위젯 ✅** @ `9e91e6a` · **★ PDF 8-7 mandatory alerts + 8-7-1 report export ✅** @ `caa215f` (BNK-353~354) · **잔여 P2**: `LIVE_E2E` manual verify | **P2 ✅+ deepen** — US-S04 (BNK-184~187·229·353~354) |
| **G41b** | **교육일지 4분류**(재난·소화·직원권익 포함) — 케어포 func 8-7 verbatim | 케어포 func **4분류** ✅ | ✅ **✅+ deepen** — V105/V106 5종 CHECK·compliance aggregate·FE StatCard @ `613b6af`/`38d24b6` · PDF 8-7 alerts @ `caa215f` · **잔여 P2**: live E2E manual verify | **P2 ✅+ deepen** — US-S04 (BNK-185~187·354) |
| **J03-readiness** | **알림 채널 발송 준비 상태**(케어포 10-7·이지케어 K010) — Solapi·SMTP·템플릿·조용한 시간대 | 케어포 **10-7 안내발송내역** ✅ · 이지케어 K010 문자발송 ✅ | ✅ **full** — channel-status @ `d4acab7` · quiet-hours 4-cycle @ `56f0204`→`a057739` · **잔여 P2**: live Solapi E2E | **P2 ✅ full** — US-J03 (BNK-177~198) |
| **G-STAFF-WELFARE** | **직원복지(포상) 집행**(이지케어 FAQ21796·지표7) — 분기 1회+·포상급 지급내역서·인건비 외 수당 | 이지케어 [**FAQ21796**](https://ezcare.easyms.co.kr/help/faq.ez?rowid=21796&type=web) ✅ · func `8-6` 회의록(복지및포상) ✅ | ❌ — `payroll`/`staff_welfare` Route·API **0건** | **P3** — US-S03 · K008 cluster (BNK-185) |
| **G-STAFF-MEETING** | **직원회의록**(이지케어 FAQ21822) — 2026 평가지표 삭제·운영 편의 월간 회의 | 이지케어 [**FAQ21822**](https://ezcare.easyms.co.kr/help/faq.ez?rowid=21822&type=web) ✅ (BNK-232) | ❌ — `staff.*meeting` Route **0건** | **P3 candidate** — 법정 필수 아님 · G42·G41과 별 Epic (BNK-232) |
| **G-ONBOARD-SUPPORT** | **기관 도입 온보딩 체크list**(silverangel businessSupport 1~4회차 36-item) | silverangel [**businessSupportService.do**](https://www.silverangel.kr/newSilverangel/service/businessSupportService.do) ✅ | ✅ **full stack** — BE V126/V127 @ `735dd53`/`4c1fd43` + FE panel+live E2E @ `36264b5` | **P2 ✅ full** — platform_admin/SaaS onboarding · US-O05 (BNK-224) |
| **G-HOMEPAGE** | **기관 홈페이지 제작**(silverangel websiteProvided) — Type A/B/C·계절 디자인·자동 결제 | silverangel [**websiteProvided.do**](https://www.silverangel.kr/newSilverangel/webSite/websiteProvided.do) ✅ 정본 (BNK-223) | ❌ **부재** — ogada MVP 범위 밖 | **P3/v2+** — BNK-175·223 · 사용자 확정 전 착수 금지 |
| **K008~K014** | **EZCare FAQ 14종 갭 cluster** — 인력배치·시설·급여제공·모니터링·CS 등 5/14 미구현 | 이지케어 FAQ **14 categories** ✅ (BNK-169) | ❌ — ogada **5/14 부재** | **P3 cluster** — G30 partial+ 이후 v2+ 패리티 검토 (BNK-169) |
| **G-7x-1-guard** | **7-1 선행입금 가드**(케어포 PDF p.86–87) — 월별 청구 전 이전달 입금 완료 UX | 케어포 PDF p.87 **「이전달 입금처리 필수」** verbatim ✅ | △ US-M03-b 전월 미입금 가드 ✅ · **청구 생성 UX deepen ❌** | **P1 deepen** — 7-x workflow (BNK-160) |
| **FAQ21824** | **재가 수급자 계약→청구 4단 lifecycle** — 계약·공단등록·서비스·월말청구 | 이지케어 [**FAQ21824**](https://ezcare.easyms.co.kr/help/faq.ez?rowid=21824&type=web) ✅ md5 `03038ccb` zero drift | △ 모듈별 partial(G14·G24·G34·G38·7-x) · **단일 wizard ❌** | **v2 Epic** — 온보딩 checklist (BNK-161~163) |
| **G40b** | **반기 기초평가 위험도**(이지케어 지표16·FAQ21811) — 낙상·욕창·인지 **반기 1회** | 이지케어 [**FAQ21811**](https://ezcare.easyms.co.kr/help/faq.ez?rowid=21811&type=web) ✅ · Channel.io 관리일·FRIA | ✅ **full** — V95/V96+BE API @ `84e59d2`/`bdfc140`/`a7b4a39` · FE Panel+Status Route @ `7b68f54`/`6657d90`/`22325f4` · **live E2E run 잔여** | **P2 ✅ full** — US-T12 · G40(지표21)과 **주기 nuance** 분리 (BNK-155~156) |
| **G2b** | **효성CMS 다중 결제수단**(가상계좌·카드·다계좌 정산) | [LCMS product](https://www.lcms.or.kr/reg/selectProductGuide.do) **3-method** ✅ · silverangel [**extraService.do**](https://www.silverangel.kr/newSilverangel/service/extraService.do) **250원/건·300원/건·효성CMS** ✅ zero drift (BNK-334) · ogada `/billing/cms` **parity** | ✅ **`/billing/cms` `CmsPage.jsx`** 3-method parity (BNK-334 cross-confirm) | **closed** — G2 CMS ✅ · LCMS product `57ec33be` 정본 carry |
| **G-Stat-CMS** | **본인부담 청구 통계**(`cost_master_statistic`) | 케어포 demo-work **`view.cost_master_statistic`** ✅ (BNK-122 · cost_* 9 paths) | ✅ **`/billing/reports/statistics`** @ `d8f1fdf` — ① 의료비공제·② 본인부담 월별 6필드 (PDF p.92 7-8 · BNK-268) | **v1.2.1 ✅** · **이동서비스비 통계 leaf P1** |
| **G-Payroll** | **직원 급여관리**(케어포 module 11) — 11-1~11-6 leaf | 케어포 **11-1 월별 급여대장**·**11-2 퇴직적립금**·**11-3 급여계약**·**11-4 급여기초**·**11-5 인건비 지출비율**·**11-6 간이지급명세서** ✅ (BNK-122) | ❌ — ogada payroll/salary 키워드 **0건** · `/finance/payroll` placeholder만 | **P3 Epic** — v3+ ROI 검토 · **직원 lifecycle Epic**(FAQ21825)과 **묶음 검토** (BNK-122~126) |
| **G-LCMS-EVAL** | **LCMS 평가 접속·데이터 SLA** (selectProductGuide) | LCMS 「기관 평가 시 엔젤시스템 접속」·「데이터 외부 유출 금지」 verbatim (BNK-190) | △ audit log·RBAC ✅ · **평가 read-only role ❌** · **계약 SLA UI ❌** | **P3** — LCMS selectProductGuide SLA (BNK-190) |
| **G17b** | **인지활동형 미제공 사유 강제**(장기요양법 **제32조**) — 미제공 시 사유·근거 기록 | MOHW 2025-247 HWPX **제32조** verbatim (BNK-198) | ❌ — 인지활동형 프로그램 미제공 사유 필드·게이트 **0건** | **P2** — G17/G29 연계 (BNK-198) |
| **G-FAMILY-LEAVE** | **가족휴가제**(장기요양법 **제36조의2**) — 연 12일/24회 한도 | MOHW 2025-247 HWPX + angelsitter #774 + **longterm menuId=2854 정본** ✅ 3-source (BNK-223) | ❌ — 직원 휴가·가족돌봄 Route **0건** | **P3** — US-R03·8-13·G18-SHORT-PILOT 연계 (BNK-198·223) |
| **G-RURAL-SUBSIDY** | **농어촌 지원금**(장기요양법 **제11조의8 별표2**) | MOHW 2025-247 HWPX verbatim (BNK-198) | ❌ — 지역별 보조금 catalog **0건** | **P3** — v2+ (BNK-198) |
| **G-PROG-MGR-BONUS** | **프로그램 관리자 수당**(장기요양법 **제17조**) | MOHW 2025-247 HWPX verbatim (BNK-198) | ❌ — 프로그램 담당자 수당 정산 **0건** | **P3** — v3+ (BNK-198) |
| **G-UX-Autosave** | **큰화면·자동저장 UX** (LCMS 엔젤) | LCMS **「스마트&터치·기록지 큰화면·자동저장」** (BNK-127) | △ DESIGN_SYSTEM 큰폰트·터치 44px·다크모드 ✅ · **autosave 패턴 ❌** | **P3** — v1.3+ UX 후보 (BNK-127) |
| **G35** | **CIST 인지기능검사** (Channel.io evidence) | 이지케어 ✅ | ❌ | **P3** (BNK-105 · G17/G29 연계 검토) |
| **G-LIVECHAT** | **실시간 라이브 채팅**(silverangel **굽은나무 라이브톡** vendor brand) | silverangel [**daycareProgramProvided.do**](https://www.silverangel.kr/newSilverangel/daycare/daycareProgramProvided.do) ✅ (BNK-223) | ❌ — G42(민원·고충)은 비동기 문서 기반 | **P3 candidate** — v3.x+ (BNK-223) |
| **G-CIST** | **인지선별검사 3종**(CIST·K-MMSE~2·GDS) — NHIS scope 외 | silverangel daycareProgramProvided.do ✅ (BNK-223) | ❌ — G9-COG는 NHIS 등급 import만 | **P3 candidate** — NHIS authoritative scope 외 (BNK-223) |
| **G-BODY-RESTRAINT** | **신체제재 기록**(L02_M07·노인복지·장기요양 인권) — 제재수단·부위·사유·대체수단·보호자통지·해제 | 케어포 demo-work **`view.care_sanction`**(「2-4.신체제재 기록」 verbatim) ✅ (BNK-239~241) | ✅ **full stack** — V131 `body_restraint_records`·V132 integrity @ `ea6092a`/`d862a82` · FE `/care/body-restraint`·`BodyRestraintRecordForm` @ `14a2bb9` · pilot/live E2E carry | **P2 ✅ full** — 결정 95 26회째 closure · L02 **6/15** · **func.php 2-4=차량관리 무관**(demo numbering 한정) |
| **G-7-1-4CHANNEL** | **본인부담금 명세 4채널 일괄발송**(케어포 PDF p.87) — 우편·문자·이메일·직접수령·발송일 수정 규칙 | 케어포 PDF p.87 「**우편·문자·이메일·직접수령**」일괄발송 verbatim ✅ (BNK-241 `0988a8fe`) | ✅ **full stack** — BE `BillingStatementDispatchChannel` enum·V133 @ `3a2e82e` · FE dispatch UI @ `1fd1434` · PDF p.87 1:1 | **P2 ✅ full** — BNK-246~247 · US-G02 · US-O07 |
| **G-7-1-PRINT-BUNDLE** | **급여명세 인쇄 산출물 4종 일괄 출력 + Excel export**(케어포 PDF p.87 ②) — 주소라벨지·급여비용명세서·영수증·청구리스트·전체 일괄·**엑셀다운로드** | 케어포 PDF p.87 ② verbatim ✅ (BNK-363·409) | ✅+ **full stack** — FE `BillingStatementPrintPanel` 4종 print @ `50d330d` + **Excel export** `@58d6694`/`@e454d3b`(BNK-409) · 미납 claim ALL 인쇄 시 영수증 제외 라벨 @ `f5639df` | **P2 ✅+** — BNK-363~364·409 closure |
| **G-CHANGE-REASON-AUDIT** | **범용 필드 변경이력 조회 그리드**(이지케어 `change-list`) — 변경전/변경후/작성자·변경일·항목·메모 단일 그리드 field-level diff | 이지케어 **`change-list` PGID**·`grid_change_reason`(`chg_what`·`chg_before`·`chg_after`·`mName`) ✅ (BNK-362) | △ — `AuditLogPanel`(action·actor only·before/after 값 ❌)·`ltcGradeChangeReason`(특정 필드만 사유) | **P3 candidate「 가정」** — v2/v3+ · 범용 field-level diff 그리드 · MVP **out-of-scope** (BNK-362) |
| **L02_M13** | **통합식사도움기록**(케어포 2-1-1·demo `view.total_meal`) — 식사유형·섭취량·식이제한·도움내용 | 케어포 func **1-1**·demo `L02_M13` ✅ (BNK-249~250) | ✅ **full stack** — V140 `meal_assistance_records` @ `81a2223` · FE `/care/meal-assistance-records`·`MealAssistanceRecordForm` @ `9ad8346` | **v3.1 ✅** — L02 6/15 (40%) · 결정 95 31~32회째 (BNK-250) |
| **L02_M15** | **요양급여 특이사항**(케어포 2-1-3·demo `view.care_service_bigo_all`) | 케어포 demo `L02_M15` ✅ (BNK-249) | ✅ **FE wire** — V134 weekly API special note @ `3549896` · BE weekly record carry | **v3.1 ✅** — L02 6/15 (40%) (BNK-251) |
| **L02_M04/M05** | **요양/식사/화장실·목욕도움 리포트**(케어포 2-5·2-6 rpt) | 케어포 demo `view.care_meal_excretion`·`view.bath_help` ✅ (BNK-249) | △ **BE partial** — `CareReportController`·`CareReportService` @ `c655743` · **FE rpt wire 잔여 P1** | **v3.1 P1** — L02 rpt cluster (BNK-251) |
| **G-MEAL-PREFERENCE** | **식사(간식) 선호도 조사 및 반영**(케어포 2-1-4·demo `view.meal_satisfaction`) | 케어포 func **1-4**·demo `L02_M16` ✅ (BNK-249) | ❌ — 선호도/만족도 survey Route **0건** | **P3** — L02_M16 · 법정 필수 아님 (BNK-250~251) |
| **L02_M02** | **집중배설관찰**(케어포 2-2·demo `view.care_excretion`) — 배뇨/배변·변 형상·관찰·중재 | 케어포 func **2-2**·demo `L02_M02` ✅ (BNK-200·238·239) | ✅ — BE `POST/GET /api/v1/care/intensive-excretion-observations`(V130·`excretionType`·`stoolConsistency` 5종) @ `fd42b7e` + FE `/care/intensive-excretion` @ `1264c16` | **v3.1 ✅** — L02 6/15 (40%) · 결정 94 Must #2 (BNK-238~239) |
| **G-STAFF-LIFECYCLE** | **종사자 입사~퇴사 4단 lifecycle**(이지케어 FAQ21825) — 1.계약·2.신고·3.근로활동·4.퇴사 | 이지케어 [**FAQ21825**](https://ezcare.easyms.co.kr/help/faq.ez?rowid=21825&type=web) ✅ md5 `a5f73548` (BNK-238) | △ partial — US-R03 onboarding·G41·V89 부분 커버 · **퇴사 4단**(사직서·인력변경·보험해지·퇴직정산·인수인계·공단 일정 삭제) ❌ · **희망이음 RFID 핸드폰 등록** ❌ | **P2** — US-R03 offboarding 확장 · G-Payroll/K008과 묶음 검토 · G-ONBOARD-SUPPORT와 별도 (BNK-238) |
| **G-GUARDIAN-MEETING** | **보호자 회의 반기 1회+**(silverangel 지표27) — 일시·장소·방법·내용·결과·참석자 | silverangel essential **지표27** ✅ (BNK-267) | ❌ — 알림·G14·meal menu △ 부분 · **보호자회의 전용 Epic 없음** | **P3** — v3.1 Must 후보 (BNK-267) |
| **G-CASH-RECEIPT-LOG** | **현금영수증 발급내역 로그**(per-payment NTS 이력) — 발급목록·수납 prompt·대시보드 due-gate·HQ pending·prior-year advisory·identifier 검증·pending error guard | 이지케어 FAQ21701/21716/21717 · BNK-398~423 | **✅ full stack end-to-end 재입증** — BNK-423 git 실측(V158/V159·API 4 endpoint·FE page/modal/alerts·테스트 6종) · 6-계층 @ `99b795a`/`35d1560` | **v3.1 ✅** — US-G26 · P3: G-CASH-RECEIPT-NTS-API |
| **G-CASH-RECEIPT-TAX-DEDUCTION-EXPORT** | **국세청 의료비공제 batch export**(연말정산·수납년도/청구년도·NTS CSV) | 케어포 7-8 「엑셀로 업로드」·BNK-408 | ✅ **`BillingStatisticsReportPage`** yearBasis toggle + NTS CSV export @ `19ed7f3`/`ceeaeb9` · **173차 P3 candidate → ✅ closure** | **v1.2.1 ✅** — US-L07 · G26 |
| **G-PROVIDER-CHANGE-COUNSEL** | **급여제공직원 변경 상담일지**(재가 평가지표·14일 SLA) | 이지케어 [**FAQ21795**](https://ezcare.easyms.co.kr/help/faq.ez?rowid=21795&type=web) · BNK-410 | ❌ — `/staff/grievance-counselings`(고충 only) · **재가 out-of-scope** | **P3 candidate「 가정」** — MVP 후속 (BNK-410) |
| **G-CASH-RECEIPT** | **본인부담금 현금영수증 발급**(국세청) — 수납 동시 발급·취소(수납 삭제)·연락처 기반 발급번호·발행내역·**2.10 발급목록**(`receipt-list`) | 이지케어 [**FAQ21700**](https://ezcare.easyms.co.kr/help/faq.ez?rowid=21700&type=web) ✅ · [**FAQ21702**](https://ezcare.easyms.co.kr/help/faq.ez?rowid=21702&type=web)/[**FAQ21701**](https://ezcare.easyms.co.kr/help/faq.ez?rowid=21701&type=web) deepen · **`receipt-list` PGID colModel** (BNK-354) | **✅+** — G-CASH-RECEIPT-LOG 6-계층 @ BNK-399~412 · **실시간 NTS API 자동발급 ❌**(`ntsReceiptNo` 수동 등록) | **v3.1 ✅+** — G-CASH-RECEIPT-LOG 흡수 · P3: G-CASH-RECEIPT-NTS-API |
| **G-SCHEDULE-FIX-LTM-COMPARE** | **청구 일정 확정 전 공단 명세서 사전 비교**(이지케어 `schedule-fix` `chk-ltm-fix`) — 「공단 청구명세서와 비교하기」체크박스 | 이지케어 **`schedule-fix` PGID**·`chk-ltm-fix` ✅ (BNK-354·366) | ✅ **BE closure** — `GET /visits/nhis-comparison`(matched/discrepancy/missing/extra 4종 분류 + per-client `visitDayCount`↔`nhisServiceDays` + 동일 월 guard) @ `03a052a` · `VisitConfirmReadinessResponse.nhisComparisonSummary` readiness embed(별도 round-trip 제거) @ `8a8c5b3` · `BatchConfirmVisitSchedulesRequest.nhisComparisonAcknowledged` ack guard ✅ · **FE `VisitBatchConfirmPanel` summary StatCard wire 잔여 △ P2** | **P3 candidate → BE ✅ closure** — ezCare 단순 checkbox 대비 능동 reconcile 우위 · **FE summary wire P2 carry** (BNK-366~367) |
| **G-STAFF-WORKLOG** | **전 직종 출퇴근부/근무일지**(이지케어 FAQ21705·1.8) — 달력·결재라인·빈서식·현지조사 evidence | 이지케어 [**FAQ21705**](https://ezcare.easyms.co.kr/help/faq.ez?rowid=21705&type=web) ✅ md5 `95f051c2` (BNK-323) | △ **`LeadCaregiverWorkLogPage`**(선임 요보사 한정) ✅ · **전 직종 캘린더/출퇴근부 ❌**(`staff_work_logs` Route **0건**) | **P3 candidate「 가정」** — v2 직원관리 cluster · MVP **out-of-scope** (BNK-323) |
| **G-HOSPITAL-ESCORT** | **장기요양 병원동행 시범**(angelsitter #781) — 통합재 가기관·주·야간보호형 참여·수속/진료/약수령 동행 | [angelsitter **#781**](https://angelsitter.co.kr/board.view.php?board=bbs3&no=781) ✅ md5 `55c85726` (BNK-322) | △ transport **`MEDICAL_FACILITY` stop** partial · **동반 활동 로그·별도 수 가 ❌** | **P3 candidate「 가정」** — v2 transport 확장 · 2026-07-30 시범 개시 후 재검토 · MVP **out-of-scope** (BNK-322) |
| **G-REVENUE-EXPENSE** | **수입지출관리**(케어포 매뉴얼 PDF module 12) — 수입·지출·결의 | 케어포 **주야간 사용매뉴얼 PDF 목차 p.3 「12.수입지출관리」** ✅ (func.php `c1`·demo pamcode **0건**·PDF-only · BNK-237) | ❌ — `revenue|expense|수입지출` Route **0건** | **P3** — `/finance/revenue-expense` · 재무회계 G4와 범위 정렬 · 주야간 MVP **Won't v1** (BNK-237) |

> **트레이드오프 갱신 (결정 91)**: **2026-08-09 8주 완성**. 방문요양→**v2**, 회계·시설급여→**v3**. 차별화 **SaaS HQ + QR B + TSP** 유지.

### 1-6. 전체 ERP 로드맵 — **2개월 스프린트** (결정 91, 2026-06-09)

> **완성 목표**: **2026-08-09 (8주)** · 벤치마크: 이지케어 9축 · 케어포 11모듈 · **MVP ~85% 패리티**

| 주차 | 버전 | 급여종·모듈 | deliverable |
|------|------|------------|-------------|
| **W1~2** (6/9~6/22) | v1.2.1 | 주야간 잔여 + 파일럿 | **G14 ✅** · **G22 ✅** · **7-9 환불 ✅** · **G7 UX+guidance+upload guard ✅** · **US-M02-b/c ✅** · **US-J03-h ✅** · **G9 ✅** · **US-J02 ✅** · **US-L01 guard ✅** · **`paidAt` ✅** · **G2 templates 5종 partial ✅** · **US-M03-b ✅** · **G27 ✅** · **US-L01 bank ✅** · **G11 ✅** · **G15 v1.3-C 대부분 ✅** · **G16 TSF ✅** · **G26 7-2-1 ✅** · **G26 xlsx partial+E2E ✅** · **G21 dup slot ✅** · **US-L01 8-bank format ✅** · **G17/G32 FE+BE ✅** · **G17 지표27 3행 ✅** · **G32 compliance 5기둥+contracts ✅** · **V75 plan FE+BE ✅** · **G33 청구시작+settlement+pilot E2E ✅** · **G2 CMS debit lineage ✅** · **J03 primary guardian dispatch ✅** · **G37 FE+BE ✅** · **G38 FE+BE+pilot E2E ✅** · **G39 FE+BE+dashboard widget ✅** · **G17/G32 edit ✅** · **LifecycleWorkflowPanel ✅** · **G34 partial ✅** · **PilotFixture ✅** · **NHIS 본인부담 비교 partial ✅** · **programCompliance live E2E harness ✅** · **QA-B49 snapshot aggregation ✅** · **G17/G32 edit-flow pilot E2E ✅** · merge(**178+145=323**·**BLOCK** BE WT clean 선행) · G7 **실파일** · G2 **SMTP** · US-L01 **은행 8종 E2E live** · G17/G32/G33/G37/G38/G39 **live E2E run** · **G34 e-sign·보수교육** · **FAQ21800·FAQ21805·FAQ21820 P2** · **G24/G30 Epic** · v1.3 live E2E · G15 **P2** · **본인부담 6단 게이트 P2** · **7-5·8-7-1 P2** |
| **W3~4** (6/23~7/6) | **v2** | **방문요양** + 보호자·CMS | `/visits` · plan/billing 이중일정 · FCMS · J01/J02 · 방문체크인 |
| **W5~6** (7/7~7/20) | **v3** | 직원·식사 + **재무회계** | staff API · `/finance/ledger` · `/finance/payroll` · 자동분개 |
| **W7~8** (7/21~8/9) | **v3** | **시설급여** + 통합 | `/facility/*` · 욕창·배설 · 통합 E2E · `merge_status: ready` |

| 버전 | 포함 모듈 | 케어포/이지케어 |
|------|----------|----------------|
| v1~v1.3 | 주야간 코어 | 모듈 1·4·7·9·10·배차 |
| **v2** | 보호자·알림·CMS · **방문요양(G21)** | 7-4·7-5·10-6 · 이지케어 3장 |
| **v3** | 식사·프로그램·**직원 HR(8-2~8-13)** · **회계(G4)** · **시설(G20)** | 3·5·8·5·7·12장 · demo-work |
| **v3.1** | **요양 리포트·목욕(3-3~3-7)** · **프로그램 확장(5-3~5-10)** · **위생안전(6-2~6-4)** | 결정 94 |

**공통 엔티티 (W2~W4 병행 설계)**:
- `branches.service_types[]` — `DAY_CARE` · `HOME_CARE` · `FACILITY_CARE`
- 방문(v2): `visit_schedules` · `plan_schedules` / `billing_schedules`
- 회계(v3): `chart_of_accounts` · `journal_entries` · `payroll_runs`
- 시설(v3): `facility_rooms` · `bed_assignments` · `pressure_ulcer_records`

**2개월 MVP 제외 (v3.1+)**: 평가 서식 80종 전수 · 통장 OpenAPI 실연동 · RFID 하드웨어 · G18/G19

#### 1-5-3. v1.3 배차·지도 포지셔닝 (BNK-8·**BNK-9**, 2026-06-08)

| 단계 | 차별화 수준 | 내용 | 영업 메시지 |
|------|-----------|------|------------|
| **v1.3-A** | **케어포 패리티** | 탑승자 위치 카카오맵·수동 순서·15명·픽업 | 「케어포 이동서비스 지도보기와 동등」 — **「최초 지도」 금지** |
| **v1.3-B** | **요양 ERP 내 유일(목표)** | **다중 차량** 자동 배차·TSP + 카카오 **Directions 다중 경유지 API** · **담당 안정성·거리 공정성**(§3-13-9) | 「요양 전용 경로 최적화」 — **영업 차별 핵심** · **✅ full @ `2ffe59f`/`db94a65`** (BNK-214~216) |
| **v1.3-C** | **법정·청구 패리티** | G15·G16 **`transport_service_fee`**·이동서비스비·공단 3분리 UI | 공단 평가·청구 필수 — **대부분 ✅** · P2: 계약서 수칙·3-1 leaf |

> **근거**: `BENCHMARK_REPORT.md` §11(BNK-8)·**§12(BNK-9)·§20(BNK-17)·§28(BNK-25)·§48(BNK-45)** — 케어포 매뉴얼 「⑤이동서비스 지도보기」공식 확인. v1.3-A Geocoding·JS SDK 파일럿 비용 = 카카오 무료 쿼터 내. v1.3-B Directions API — **10k/8원·다중경유 5k/16원 확정**(PLAN_NOTES #43 **해소**). v1.3-C 이동서비스비 — **#44 2차 교차 확정**(830/2,630/4,430/6,230·BNK-9·BNK-17 폐기) · **★ BNK-45: 「이동지원 시범사업」≠ 주야간 이동서비스비** · **제34조·공단 매뉴얼 1차 출처 재추적** → 시드 **구조 설계 가능** · **상수 하드코딩 금지** 유지.

#### 1-5-4. 케어포 평가지표 cross-walk — dual-source numbering (BNK-285, 2026-06-17)

> **정본 출처**: `BENCHMARK_REPORT.md` §285 · `memory/decisions.md` BNK-285 · 스냅샷 `carefor_intro_si_func.html`·`carefor_func.php`

| 정본 | URL/스냅샷 | ogada 용도 |
|------|------------|-----------|
| **시설급여** | `intro_si/func.php` (11 module) | **L02/L03 요양·간호 deepen 정본** — demo-work 시설 셸 = 이 콘텐츠 |
| **주야간보호** | `daycare/func.php` (11 module) | **이동서비스(module 2)·본인부담 7-x** — 주야간 = 시설 + module 2「이동서비스관리」삽입 |
| **방문급여** | `intro_visit/func.php` (8 module) | **out-of-scope** (ogada MVP 주야간보호) |

**dual-source numbering (module 번호 충돌 주의)**

| module·leaf | 시설 (`intro_si`) | 주야간 (`daycare`) | ogada 매핑 |
|-------------|-------------------|-------------------|-----------|
| 2-4 | **신체제재 기록** | **차량관리** | V131 `body_restraint_records` ↔ **시설 2-4** (demo-work `view.care_sanction` 정본) |
| 2-1~2-3 | 요양급여·집중배설·목욕 | 일정·탑승·출석 | L02 cluster (V134·V140·V142 등) ↔ **시설 2-x** |
| 2 (module) | 요양 급여제공 | **이동서비스관리** | transport `/transport/*` ↔ **주야간 module 2** |

**기획 규칙**: 평가지표·리포트 leaf cross-walk 시 **주야간 `daycare/func.php`만 보면 numbering 오류** — 요양·간호 코어는 **`intro_si/func.php` 우선**. 다음 BNK rotation: 시설 module 9「기초설정」↔ US-O 운영설정 cluster.

#### 1-5-2. 화면·메뉴 밀도 (BNK-6·**BNK-12·14·16·25**, 2026-06-10 — v1.2·v1.2.1·v1.3·v3 입력)

| KPI | ogada develop (93차 git 실측 `@eedcc80`/`@0854fbd`) | 케어포 (추정) | 목표 (결정 49·BNK-6·12·16·17·18·25·31·35·41·42·45) |
|-----|------------------------------------------------------|---------------|---------------------------|
| route 수 | **46 path·40 page** (`@eedcc80`, BNK-45) | **111 leaf** func.php (BNK-35 Wayback) | v1.2 **≥60% PASS** |
| SideNav depth | **2단** (US-UX-02) | **2~3단** 번호식 | **2단 그룹화** ✅ |
| SideNav 토글 | **✅ full** (US-UX-05) — 5그룹 접힘/펼침 | 2~3단 접힘 | **P1 Should** @ `1e111be`/`8a8b930` |
| 대시보드 | **7 StatCard** 실데이터 @ `20bfac1`/`f755428` | 3블록(일정·미처리·공지) | **US-M02+US-M02-b+US-M02-c ✅** (BNK-33·35) |
| 등급이력 | UI+DB(V48)+**GET API** @ `15e41e3` | 1-9 전수 리포트 | **v1.2.1 P0 ✅** |
| NHIS reconciliation | **DISCREPANCY compare** + BE+FE **`PENDING_REVIEW` 3상태** @ `16402b2`/`dd49204` | **3상태**(성공/오류/대기) | **G7 실파일 샘플 BLOCK** |
| TAM (주야간보호) | — | **5,598개소**(2025 3Q) | ogada 1차 TAM |
| Vitest (93차 `@eedcc80`) | develop **`413/413 PASS`** · WT **CLEAN** | — | post-merge live E2E 권장(결정 73) |
| backend tests (93차 `@0854fbd`) | develop **`383 PASS`** · WT **CLEAN** | — | merge(43) 대기 |
| frontend merge | develop **`eedcc80`** · test **`c7c8f07`** · **55 ahead** | — | v1.2.1 **`merge_status: ready`** · ★ **FULLY UNBLOCKED** |
| backend merge | develop **`0854fbd`** · test **`598d108`** · **43 ahead** | — | v1.2.1 **`merge_status: ready`** · ★ **FULLY UNBLOCKED** |
| 모듈 커버 (BNK-493) | **78.79%** @ `dffd726`/`479995e` (`competitorModuleCoverage.js` 29-feature 실측 · ✅20·△4·❌5 out-of-scope · CMS 0.65) | 11모듈 주야간 | **≥60% PASS** · △4 잔여 상승 여지 |
| FE-15 bundle | **Fixed @ `d484206`+** — max **367 kB <500 kB** | — | ✅ |
| 본인부담 7-x | **11/11 Route** (7-1~7-3·수가·copay·리포트 4·계산기·**`paidAt`**·**7-2-1 G26**·**7-9 환불**·**7-5 간편결제**) | **11 leaf** + **PDF 7-3 청구시작(G33)** | **7-2-1→G26 ✅** · **7-9 ✅** (BNK-84~85) · **G33 청구시작 ✅** (BNK-94→98) · **7-5 간편결제 ✅ partial+** @ `c9baca2`/`bebd874` (BNK-189~190) · **live PG P2** · **PDF↔func.php 7-x 번호 충돌 — Route rename 금지**(BNK-98) |
| ERP 리포트 밀도 | **~5 report routes** + 대시보드 | **94 leaf·36 리포트(38.3%)** (BNK-94) | **v3.1 P3** 백로그 |

> **문서 drift (BNK-9·12·14·16·17·18·19·20·22·25·28·31·35·38·41·42·45·49·53·58·59~61·65~114~122)**: 과거 KPI **24 route·`4be0938`·~74–78% 문서 추정** — git 실측 **`6d6b426`/`559648f` 57 route·81 page·78.28%** 우선. v1.2 test merged `[x]` · **v1.2.1 merge-blocking P0 `[x]`** · **G34 partial `[x]`** · **LifecycleWorkflowPanel `[x]`** · **G17/G32 compliance contracts `[x]`** · **G33 pilot E2E `[x]`** · **G37 FE+BE `[x]`** · **G38/G39 FE+BE+snapshot `[x]`** · **G17/G32 edit-flow pilot E2E `[x]`** · **BE+FE WT CLEAN** — ★ **merge FULLY UNBLOCKED**(112차 · merge **311 commits** · QA Open 0건).

**v1.2.1 develop-only (82차 — P0+G22+G7 UX 닫힘 · P1 잔여)**:

1. ~~**G14 GET API**~~ — ✅ @ `15e41e3` (US-M01)
2. ~~**G22 본인부담 리포트**~~ — ✅ @ `dbf485e` (US-M03)
3. ~~**G7 3상태 UX**~~ — ✅ BE @ `4cc328d`/`dd49204` · FE @ `fbb0b7a`/`16402b2` (BNK-18)
4. **(P1) G7 실파일 샘플** — PLAN_NOTES #27 · fixture tests @ `dd49204` ✅
5. **(P1) G13·US-J02 live run** — cross-page hardening @ `c72e9df` ✅ · **live run post-merge**(결정 73)
6. ~~**G9 duration_band**~~ — ✅ @ `0c34f85`/`0719648`+폴백 `6fe853b`/`5348d9c`/`eb3f0fd` (BNK-41·42)
7. **(P1) G2 SMTP 실연동** — templates **5종 partial** @ `0854fbd`/`eedcc80` ✅ · **SMTP/메일벤더 실연동** 잔여
8. **(P1) v2 CMS Hyosung** — `/billing/cms` @ `6c6dc7a` ✅ · **FCMS 실연동** 잔여
9. **(P1) US-J02 billing filter/dedupe/retry** — WIP @ WT dirty (B07 #10) · 커밋 선행
8. ~~**G11 catalog+가이드**~~ — ✅ @ `904072b`/`3db8db3` (BNK-53 · US-M05) · **v2 P1 잔여**: 청구 자동 가산

**v1.2 P0 (test merged @ `c510f5c`)** — low-cost high-density:

1. 보호자 관리 전용 (`guardian_clients` — Epic K)
2. 본인부담 입금·미납 (`billing_claims` + 상태 컬럼 — Epic L)
3. 등급변동 이력 (이력 테이블 — Epic M)
4. 대시보드 실데이터 위젯 (attendance·billing API — Epic M)
5. 2단 SideNav (Epic UX)
6. **Recharts 차트 레이어** — `ChartContainer`·출석률·지점비교·건강추이 + **`HealthAlertList`** + `chartColors.js` (BNK-6-4, US-M02·FE-12)
7. **Platform·NHIS 배치·청구·수가표 UI** — `BatchProgressSteps`·`PlatformOrgDetailModal`(+test)·**`BillingStatusConfirmModal`·`CopayRateTable`·`FeeScheduleTable`(+test, US-G00a·케어포 9-x 수가설정·HEAD `FeeRateHistoryPanel` 연계)·`NhisImportGuidePanel`·`GuardianDailySummary`**(+tests)·Platform/NHIS/Reconciliation/Forbidden (BNK-6 HQ/플랫폼·청구·copay·수가표 패리티, FE-13)
8. **운영·보안·계정 보안·로그인 이력 UI** — `AuditLogPanel`·`BackupSettingsPanel`·`FilterChips` + §3-1 매핑 **`PasswordChangeModal`·`PasswordResetRequestModal`·`LoginHistoryPanel`·`SettingsPage.test`** (BNK-6 운영/보안·계정 보안 모듈 패리티, FE-14)

> 상세 매핑표: `COMPETITOR_MATRIX.md` §8-1~8-5, `ROADMAP.md` v1.2.

---

## 2. 이해관계자 및 역할

### 2-1. 운영 모델 (사용자 확정: 2026-06-05)

**다지점 운영**을 전제로 하며, **지점별 관리**와 **통합 관리**를 구분한다.

| 관리 체계 | 대상 | 목적 |
|----------|------|------|
| **지점별 관리** (Branch Scope) | 개별 주간보호센터 1곳 | 해당 지점의 일상 운영·기록·현황 |
| **통합 관리** (HQ Scope) | 본사·다지점 운영 주체 | 전 지점 현황 비교·집계·정책·계정 관리 |

> 모든 운영 데이터(이용자·출석·건강기록 등)는 `branch_id`로 소속 지점이 식별된다.  
> `hq_admin`은 전 지점 **조회·집계**가 기본이며, **상세 기록 수정**은 `active_branch_id`를 선택한 경우에만 해당 지점 범위에서 가능.

### 2-2. 역할 정의

| 역할 | 코드 | 관리 체계 | 데이터 범위 | 주요 업무 |
|------|------|----------|------------|----------|
| 플랫폼 관리자 | `platform_admin` | ogada 내부 | 전 Tenant 목록·신규 등록 | **신규 고객 센터 등록**, 첫 `hq_admin` 발급 (`/platform`) |
| 통합 관리자 | `hq_admin` | 통합 | 전 지점 조회·집계, 지점·계정 관리 | 다지점 대시보드, 지점 등록, 정책 설정 |
| 지점장 | `branch_admin` | 지점별 | 소속 지점 1곳 | 지점 운영 총괄, 직원·이용자 관리, 지점 리포트 |
| 사회복지사 | `social_worker` | 지점별 | 소속 지점 | 이용자 관리, 케어 플랜, 프로그램 |
| 요양보호사 | `caregiver` | 지점별 | 소속 지점 | 출석·건강·식사 기록 입력 |
| 보호자 | `guardian` | 지점별 | 연결된 이용자 | 일일 기록 열람, 알림 수신 |
| 시스템 관리자 | `sysadmin` | 통합 | 시스템 전체 | 인프라, 백업, 기술 설정 |

### 2-3. RBAC 스코프 규칙 (MVP)

| 규칙 | 내용 |
|------|------|
| JWT 클레임 | `role`, `organization_id`, `branch_ids[]`, `active_branch_id` 포함 |
| 지점 스코프 | `branch_admin` 이하 역할은 **자신의 `branch_ids` 내 데이터만** CRUD |
| 통합 스코프 | `hq_admin`은 전 지점 **조회·집계** 기본, **쓰기(CRUD)** 는 `active_branch_id` 선택 시 해당 지점만 |
| 지점 전환 | `hq_admin` 및 다지점 권한 보유자는 UI **지점 선택기(Branch Switcher)** 로 `active_branch_id` 변경 |
| 지점 스코프 UI | 출석·QR·배차(목록·신규·상세) 화면에 **`BranchScopeNotice`**(`role="status"`)로 활성 지점 조회 범위 노출 — US-B02·US-UX-04 *(UXD-53 @ `0d36e30`+ · UXD-54 @ `7cd9293`+)*
| API 강제 | 모든 목록·집계 API에 `branch_id` 필터 또는 스코프 검증 필수 |
| 역할 분리 | MVP에서 **7개 역할**(고객 6 + ogada `platform_admin`) 각각 별도 화면·메뉴·권한 |

### 2-4. 역할별 MVP 화면·권한 (사용자 확정: 2026-06-05)

> MVP v1은 **전 역할**을 구분해 구현한다. `platform_admin`(ogada 직원) 포함.

| 역할 | 로그인 후 홈 | 주요 메뉴 (MVP) | 쓰기 권한 |
|------|------------|----------------|----------|
| `platform_admin` | `/platform` | 고객(Tenant) 등록·목록, 첫 `hq_admin` 계정 발급 | Tenant 생성·초기 계정만 (운영 데이터 CRUD 없음) |
| `hq_admin` | `/dashboard/hq` | 통합 대시보드, 지점 관리, 청구·정산, 전 지점 조회 | `active_branch_id` 지점만 CRUD |
| `branch_admin` | `/dashboard` | 지점 대시보드, 이용자, 출석(수기), 건강, 청구 조회 | 소속 지점 전체 CRUD |
| `social_worker` | `/dashboard` | 이용자 관리, 건강 기록, 출석 현황 조회 | 소속 지점 CRUD (직원관리 제외) |
| `caregiver` | `/dashboard` | 출석(수기), 건강 기록 입력, 이용자 목록(읽기) | 출석·건강 기록 쓰기 |
| `guardian` | `/guardian` | 연결 이용자 일일 기록 열람, **QR 체크인/아웃** | 연결 이용자 출석(QR), 복수 시 대상 선택 |
| `client_user` | `/guardian` | 이용자 **본인** 로그인 — 기록 열람·QR 체크인 (제한) | 본인 1명 출석(QR)만, Organization 설정 on 시 |
| `sysadmin` | `/settings` | **자기 Tenant** 기술 설정, 백업, 감사 로그 | 시스템 설정만 (타 Tenant·운영 CRUD 없음) |

> `client_user`는 6역할 외 **보조 계정 유형** — 이용자 본인 전용 제한 로그인. QR 안 3에 따름.

---

## 3. 기능 요구사항

### 3-0. 네비게이션·레이아웃 (US-UX, 우선순위: 🟡 Should → **v1.2.1 P1**)

> **US-UX-02** 2단 SideNav 그룹(운영·이동·출석·기록·청구)은 구현 완료. **US-UX-05**(사용자 요청 2026-06-14)는 **그룹 헤더 토글 UX**를 완성한다.

| ID | 요구 | 상세 | 상태 |
|----|------|------|------|
| **UX-02** | 2단 SideNav 5그룹 | `navConfig.js` `NAV_GROUPS` · 역할별 `navGroupsForRole` | ✅ |
| **UX-05** | **그룹 접힘/펼침 토글** | 운영·이동·출석·기록·청구 헤더 클릭 → 하위 메뉴 표시/숨김 | Planned |
| **UX-05a** | 초기 접힘 + 활성 그룹 auto-expand | deep link·새로고침 시 현재 route 부모 그룹만 펼침 | Planned |
| **UX-05b** | a11y | `aria-expanded`·`aria-controls`·`aria-hidden`·키보드 토글 · DESIGN_SYSTEM §8-2 | Planned |
| **UX-05c** | 뷰포트 통일 | 모바일·데스크톱 **동일 토글 규칙** (데스크톱 항상 펼침 **폐기**) | Planned |

- [x] 2단 SideNav — 운영·이동·출석·기록·청구 (`SideNav.jsx`·`navConfig.js`)
- [x] **5그룹 토글** — 클릭 시 하위 메뉴 접힘/펼침 (US-UX-05) @ `1e111be`/`8a8b930`
- [ ] **활성 route 그룹 자동 펼침** — 나머지 그룹 기본 접힘
- [ ] in-page ContextNav(출석·기록·청구·이동)와 **병행** — SideNav 토글과 충돌 없음

> 상세 인수 조건: `USER_STORIES.md` **US-UX-05** · `PLAN_NOTES.md` 131차.

### 3-1. 인증 및 계정 관리 (우선순위: 🔴 Must)

- [ ] 이메일/비밀번호 로그인
- [ ] 역할 기반 접근 제어 (RBAC) — 역할 + 지점 스코프
- [ ] JWT 발급·갱신 (`role`, `organization_id`, `branch_ids`, `active_branch_id`)
- [ ] 지점 선택기(Branch Switcher) — 다지점 권한 사용자
- [ ] 비밀번호 재설정 (이메일 발송)
- [ ] 세션 자동 만료 (30분 비활성 시)
- [ ] 로그인 이력 조회 (지점·역할 포함)

### 3-2. 이용자(어르신) 관리 (우선순위: 🔴 Must)

- [ ] 이용자 등록·수정·퇴소 처리 (**소속 지점 `branch_id` 필수**)
- [ ] 이용자 기본 정보: 이름, 생년월일, 성별, 주소, 연락처
- [ ] 장기요양등급, 인정번호 관리
- [ ] **주민등록번호 수집** (공단 청구 법정 필수) — 저장 시 암호화, 화면·목록·로그 마스킹, 별도 수집·이용 동의 (§3-2-1)
- [ ] **본인부담 구분** 관리 (일반 15% / 감경 9% / 감경 6% / 기초수급 0%) — 청구 계산에 사용 (§3-9-2)
- [ ] 보호자 정보 연결 (**1명 이상 필수** — 등록 API `primaryGuardian` 동시 연결, `guardian_link_status=LINKED`)

#### 3-2-1. 주민등록번호 처리 정책 (사용자 확정: 2026-06-05)

> 경쟁사·법령 조사 결과: **노인장기요양보험법 시행규칙**상 공단 청구명세서에 "수급자 성명 및 **주민등록번호**" 기재가 **법정 필수** → 청구 위해 수집 불가피. 개인정보보호법 §24-2상 **암호화 보관 의무**.

| 항목 | 정책 |
|------|------|
| 수집 | **수집함** (공단 급여비용 청구 목적, 법령 근거) |
| 저장 | **암호화 저장** (고유식별정보, PIPA §24-2) |
| 표시 | 화면·목록·로그·에러 메시지 **마스킹**(`******-*******`), 청구 등 법정 목적에서만 복호화 |
| 동의 | 수집·이용 **별도 동의** 흐름 (민감·고유식별정보 별도 동의) |
| 사용 제한 | 청구·법정 목적 **외 사용 금지**, 접근 시 audit_log 기록 |

**암호화 대상 컬럼 (사용자 확정: 2026-06-05 — build 가이드)**

> db_architect는 별도 대화 채널이 없으므로, 스키마 설계 가이드를 여기에 확정한다. build(coder) 단계는 이 표를 기준으로 컬럼 암호화를 적용한다.

| 데이터 | 분류 | 처리 |
|--------|------|------|
| 주민등록번호 | 고유식별정보 | **암호화 필수** + 마스킹 + 별도 동의 + 복호화 audit_log |
| 연락처(전화) | 준식별정보 | **암호화 권장** (저장 암호화, 화면 부분 마스킹) |
| 주소 | 준식별정보 | **암호화 권장** (저장 암호화) |
| 장기요양인정번호 | 식별번호(공단) | 평문 (검색·청구 키, 미암호화) |
| 장기요양등급·`copayType` | 운영 분류 | 평문 |
| 건강·투약 기록 | 민감정보 | 전송 TLS, 접근통제·audit_log (컬럼 암호화는 db_architect 판단) |

> 암호화 방식(컬럼 단위 vs 애플리케이션 레벨)·키 관리는 build 단계에서 시크릿 매니저/환경변수 기반으로 결정 (rules.md §3).
- [ ] 이용자 사진 업로드
- [ ] 이용자 목록 검색·필터·페이지네이션 (**지점별 / 통합 조회 구분**)
- [ ] 이용자 상세 프로필 페이지 (탭 구조: 기본정보 / 건강 / 출석 / 청구)

### 3-3. 출석 관리 (우선순위: 🔴 Must)

> **출석 방식 (2026-06-05 확정)**
> - **수기**: 직원이 웹에서 이용자 목록 체크인/아웃 (`check_in_method`: `manual`)
> - **QR (B방식)**: **보호자/이용자**가 스마트폰으로 **지점 입구 QR** 스캔 (`check_in_method`: `qr_self`)
>
> ※ QR A방식(직원이 이용자 명창 QR 스캔)은 MVP **미포함**. 필요 시 후속 추가.

#### QR A vs B 차이 (참고)

| 구분 | A방식 (직원 → 이용자 QR) | B방식 (보호자/이용자 → 지점 QR) ← **MVP** |
|------|------------------------|------------------------------------------|
| QR 부착 대상 | 이용자 명찰·카드·앱 | 지점 입구 게시 QR (고정) |
| 스캔 기기 | 직원 태블릿/폰 | 보호자·이용자 스마트폰 |
| 이용자 식별 | QR에 `client_id` 포함 | 로그인 계정 + 연결 이용자 선택 |
| 직원 개입 | 필요 (대면 확인) | 최소 (셀프 체크인) |
| 적합 상황 | 직원이 입구에서 관리 | 보호자 동반 도착·귀가 시 자가 처리 |

#### B방식 — 「누가 스캔하나」질문의 배경 (§3-3 부속)

B방식은 지점 QR만으로는 **어느 이용자가 출석했는지** 알 수 없다. 스캔 전에 **로그인한 계정**으로 이용자를 특정해야 한다.

**현장 시나리오**

| 상황 | 일반적 행위 | 시스템 설계 포인트 |
|------|------------|-------------------|
| 보호자가 어르신 동반 도착 | 보호자 폰으로 입구 QR 스캔 | `guardian` 계정 로그인 → 연결 이용자 자동/선택 → 체크인 |
| 보호자가 부모님 2명 이상 담당 | 스캔 전 「누구」 선택 | 복수 `guardian_client` 링크 시 **대상 선택 UI** |
| 어르신 혼자 도착 (보호자 없음) | 직원 수기 처리 또는 본인 폰 | 수기(`manual`)로 대체, 또는 이용자 본인 계정 |
| 어르신 스마트폰 사용 가능 | 본인이 QR 스캔 | 이용자 **본인 계정** 필요 여부 결정 |
| 전국 SaaS — 센터마다 운영 상이 | 센터 정책 다름 | 보호자 전용 vs 보호자+이용자 계정 **옵션** 권장 |

**스캔 계정 정책 (사용자 확정: 2026-06-05 — 안 3 채택)**

| 항목 | 내용 |
|------|------|
| QR 스캔 가능 계정 | `guardian` **항상** + `client_user`(이용자 본인) **조건부** |
| 센터별 설정 | Organization `allow_client_self_checkin` (boolean, 기본 off) |
| `client_user` | 이용자 1명 ↔ 계정 1개 연결, `/guardian` 동일 UI·최소 권한 |
| 보호자 복수 연결 | 스캔 전 **체크인 대상 선택** UI |

#### 기능 목록

- [ ] 일일 출석 현황 대시보드 (지점별 / 통합)
- [ ] **수기 체크인/아웃** — `caregiver` 이상 직원, 이용자 목록에서 처리
- [ ] **지점 QR 생성·출력** — 입소용/귀가용 QR, 지점·날짜·유효시간 포함
- [ ] **QR 셀프 체크인/아웃** — `guardian` 또는 `client_user`가 지점 QR 스캔
- [ ] Organization 설정 **`allow_client_self_checkin`** on/off (`hq_admin` 관리)
- [ ] `client_user` 계정 발급·연결 (이용자 등록 시 선택)
- [ ] 복수 이용자 연결 시 **체크인 대상 선택** UI (`guardian` 전용)
- [ ] 출석 시각 자동 기록 (`check_in_method`: `manual` | `qr_self`)
- [ ] 귀가 교통편 기록 (자가용, 차량 서비스 등)
- [ ] 월별 출석 통계 리포트 (지점별 / 통합 비교)
- [ ] 결석 사유 기록 및 알림

### 3-4. 건강 기록 (우선순위: 🔴 Must)

- [x] 일일 건강 체크 (혈압, 체온, 혈당, 산소포화도) — **`VitalsRecordForm` @ UXD-39/40**
- [x] 투약 기록 (약품명, 용량, 시간, 투약자) — **`MedicationRecordForm` @ UXD-39**
- [x] 낙상·사고 이벤트 기록 — **`IncidentRecordForm` @ UXD-41 (`3ec8206`)** · API `detail` 필드 @ `95b92b9`(Q154)
- [x] 특이사항 메모 — US-F03 `SYMPTOM`/`OTHER` 유형으로 통합
- [ ] 건강 기록 이력 조회 및 그래프 — US-F04 Recharts/표 형식 **부분 충족**

### 3-5. 식사 관리 (우선순위: 🟡 Should)

- [ ] 식단 등록 및 관리
- [ ] 이용자별 식이 제한 사항 (저염식, 당뇨식 등)
- [ ] 식사량 기록 (잘 먹음/보통/적게)
- [ ] 영양사 소견 기록

#### 3-5-a. 요양 급여 리포트·목욕 (케어포 3-3~3-7, **사용자 확정: 2026-06-09, 결정 94**)

> **v3.1 Must** — `/health` 통합 기록을 **케어포 3장 리포트 단위**로 분리·집계. 식사(§3-5)와 연계.

| 케어포 | 기능 | ogada | 버전 |
|--------|------|-------|------|
| 3-3 | 목욕일정 및 제공현황 | `/care/bathing` 일정·제공 | v3.1 |
| 3-4 | 요양/식사(조치)/화장실 리포트 | `/reports/care-daily` | v3.1 |
| 3-5 | 목욕도움 리포트 | `/reports/bathing` | v3.1 |
| 3-6 | 급여제공 리포트 | `/reports/care-provision` | v3.1 |
| 3-7 | 급여제공 서비스 집계 | `/reports/care-summary` | v3.1 |

- [ ] 이용자별·지점별 **목욕 일정** 등록·제공 완료 처리
- [ ] 요양·식사 조치·화장실 **일일 리포트** (기록→출력)
- [ ] 목욕도움·급여제공 **기간 리포트**·서비스 **집계** (월·주)

### 3-6. 프로그램 관리 (우선순위: 🟡 Should → **v3 기본**)

- [ ] 주간/월간 프로그램 일정 등록
- [ ] 이용자별 프로그램 참여 기록
- [ ] 프로그램 사진 업로드
- [ ] 프로그램 만족도 기록

#### 3-6-a. 프로그램 확장 — 그룹·의견·리포트 (케어포 5-3~5-10, **사용자 확정: 2026-06-09, 결정 94**)

> **v3.1 Must** — 케어포 5장 leaf 전수. v3 기본(§3-6) 일정·참여 위에 **운영·평가·리포트** 레이어.

| 케어포 | 기능 | ogada | 버전 |
|--------|------|-------|------|
| 5-3·5-3-1 | 프로그램 수급자 그룹·그룹 관리 | `/programs/groups` | v3.1 |
| 5-4 | 프로그램 정보관리(마스터) | `/programs/catalog` | v3.1 |
| 5-5·5-5-1 | 프로그램 의견수렴·관리자 업무수행일지 | `/programs/feedback` | v3.1 |
| 5-6 | 프로그램 계획(월·분기) | `/programs/plans` | v3.1 |
| 5-7~5-10 | 참여·제공·그룹이력·일정 **리포트** | `/programs/reports/*` | v3.1 |
| 5-1-1 | 외부강사·자원봉사자 | `/programs/instructors` | v3.1 |

- [ ] 프로그램 그룹 CRUD·이용자 배정·이력
- [ ] 프로그램 마스터(명칭·유형·목표) 관리
- [ ] 의견수렴·반영·관리자 일지
- [ ] 월·분기 프로그램 계획
- [ ] 참여·제공·그룹·일정 **리포트** (인쇄·엑셀)

### 3-7. 보호자 서비스 (우선순위: 🟡 Should)

#### 3-7-0. 보호자 「정보」 vs 「SaaS 로그인」 (2026-06-07 사용자 질문)

| 구분 | 필수? | 설명 |
|------|-------|------|
| **보호자 연락처·`guardian_clients` 연결** | **v1 Must** | 이용자 등록 시 **대표 보호자 1명 이상** 연락처·관계 저장(US-D01). 청구·법정 기록·감사 추적용 **데이터** — 로그인 계정 없이도 가능 |
| **보호자 `guardian` SaaS 로그인** | **Must 아님** (기능별 선택) | 센터장·요양보호사만으로 **수기 출석·건강·청구·대시보드** 운영 가능. 파일럿 1주차도 보호자 **미참여** 확정 |

**로그인이 필요한 경우(현재 로드맵)**

| 기능 | 버전 | 로그인 없이 대체 가능? |
|------|------|------------------------|
| **QR B방식 셀프 출석** | v1 Must | △ — 보호자/이용자 폰 스캔 시 **`guardian`/`client_user` 계정 필요**. 대체 = **직원 수기 출석만** |
| **일일 기록 열람** | v1 P2 | ◎ — 센터가 전화·종이·이메일 PDF로 전달 가능 |
| **초대·명세 모바일 조회** | v1.1 G8 | ◎ — 센터가 명세 **이메일/인쇄** 발송(엔젤 패턴). 포털은 **편의·경쟁사 패리티** |
| **알림톡·푸시** | v2 G1 | △ — 수신 주체 식별 필요(계정 또는 동의된 연락처) |

**왜 넣었나 (기획 근거, 벤치마크)**

1. **경쟁사 표준** — 케어포 가족돌봄앱·이지케어 EZCARE: 보호자 **앱/웹으로 명세·기록 조회** (G8)
2. **ogada 차별화 QR B** — 입·퇴소 시 보호자가 입구 QR 스캔 → **직원 부담 감소** (NFC/RFID 없이 스마트폰만)
3. **투명성·신뢰** — 가족이 출석·케어·본인부담금을 **스스로 확인** (민원·전화 문의 감소 기대)
4. **B2B SaaS 판매 포인트** — 「보호자 앱까지 포함」 vs 공단 롱텀(보호자 UX 약함)

**범위 축소 옵션 (미확정 — PLAN_NOTES #39)**

- **A. 데이터만** — `primaryGuardian` 연락처 저장, **계정·포털·J01 제외**, QR B 제외(수기 출석만)
- **B. QR만** — 최소 `guardian` 계정 + QR 체크인, 명세·초대 UI는 v2 이후
- **C. 현행 유지** — v1 QR + v1.1 G8(초대·명세) + v2 알림 (벤치마크 패리티)

- [ ] 보호자 전용 포털 (모바일 최적화)
- [ ] **보호자 초대 온보딩** — 기관이 보호자 계정 초대·연결 (v1.1, G8 — 이지케어 EZCARE·케어포 패턴)
- [ ] **본인부담금 명세·청구서 모바일 열람** (v1.1, G8 — 알림·CMS 없이 조회만)
- [ ] **v1.1** 인앱 알림·FCM Web Push·이메일(선택) — 무료 채널 골격
- [ ] **v2** 일일 케어 리포트·출석(도착/귀가)·긴급 알림 — **카카오톡 채널 알림톡** (+ SMS fallback)
- [ ] 공지사항 열람

### 3-8. 직원 관리 (우선순위: 🟡 Should → **v3 Must**)

- [ ] 직원 등록·수정·퇴직 처리
- [ ] 근무 일정 (교대 근무 스케줄)
- [ ] 근태 기록 (출퇴근 시각)
- [ ] 자격증 정보 관리 (요양보호사 자격증 번호 등)

#### 3-8-a. 직원 HR 확장 (케어포 8-2~8-13, **사용자 확정: 2026-06-09, 결정 94**)

> **v3 Must** (8-1 기본 + 아래 전부). **11장 직원 급여대장**은 재무(G4)와 분리 — §3-8 범위, 급여 **산출**은 v3 `/finance/payroll`.

| 케어포 | 기능 | ogada | 버전 |
|--------|------|-------|------|
| 8-1-1 | 복지(포상) 제공대장 | `/staff/welfare-ledger` | v3 |
| 8-1-2 | 선임 요양보호사 업무수행일지 | `/staff/lead-caregiver-log` | v3 |
| 8-2 | 근무일정표 | `/staff/schedules` | v3 |
| 8-3 | 연간 일정계획 | `/staff/annual-plan` | v3 Could |
| 8-4 | 출퇴근·근무관리 | `/staff/attendance` | v3 |
| 8-5 | 사례관리 회의록 | `/case-management/meetings` | **v1.2.1 ✅** (G32 · BNK-90 dual-source) |
| 8-6 | 운영위원회 회의록 | `/staff/committee-meetings` | v3 |
| 8-7·8-7-1 | 교육일지·요양보호사 보수교육 | `/staff/training` | v3 |
| 8-8 | 자원봉사자 활동일지 | `/staff/volunteers` | v3 Could |
| 8-9 | 고충처리 관리 | `/staff/grievances` | v3 |
| 8-10 | 건강검진관리 | `/staff/health-checkups` | v3 |
| 8-12 | 직원 현황 리포트 | `/staff/reports/status` | v1.2.1 ✅ partial+ @ `488f547`/`ff173af` |
| 8-13 | 연차·유급휴일 대장 | `/staff/leave-ledger` | v3 **P1 in_progress**(US-R01-c·BNK-551~552·BE API ✅ @ `5fd12dd` · FE wire △ @ `8057c1e` · monthly snapshot과 정보 모델 분리) |

- [ ] 근무일정·출퇴근·연차 대장
- [ ] 교육·회의록(사례·운영위)·업무수행일지
- [ ] 건강검진·고충처리·복지(포상) 대장
- [ ] 직원 현황 **리포트**

### 3-9. 청구·정산 (우선순위: 🔴 Must — 사용자 확정: 2026-06-05)

> MVP v1 **포함**. 벤치마킹(케어포) 기준 **2단계 모델**: ①공단 급여청구(공단 포털) ②본인부담금·내부청구서(ogada).

#### 3-9-1. 수가표 관리 (사용자 확정: 2026-06-05 — B방식, 2026-06-07 1밴드 확정)

- 수가(공단이 정한 1일당 급여 단가)는 **코드 고정이 아닌 관리자 입력 테이블**로 관리한다.
- `hq_admin`이 화면에서 **등급별·적용연도별 수가**를 등록·수정한다 (수가 개정 시 코드 변경 불필요).
- 청구 계산은 항상 **해당 시점에 유효한 수가 버전**을 참조한다 (이력 보존).

| 항목 | 내용 |
|------|------|
| 관리 주체 | `hq_admin` (전사 공통 수가표) |
| 키 | 적용연도(또는 시행일) × 장기요양등급 |
| 값 | 1일당 수가, (선택) 가산·식대 등 부가 항목 |
| 버전 | 연도/개정별로 이력 보존, 과거 청구는 당시 수가 유지 |
| **이용시간 밴드 (v1)** | **단일 밴드 — 10~13h 고정** (파일럿 센터 표준 이용시간 08-20=12h, 사용자 확정 2026-06-07) |
| **이용시간 밴드 (v1.1+)** | 다밴드(`duration_band`) — 3~6h / 6~8h / 8~10h / 10~13h / 13h+ (PLAN_NOTES #35) |

#### 3-9-2. 본인부담률 — 이용자별 관리 (사용자 확정: 2026-06-05)

- 본인부담률은 **이용자마다 다르므로 이용자별로 부담 구분을 저장**한다.
- 구분: **일반 15% / 감경 9% / 감경 6% / 기초수급(의료급여) 0%** (구분 코드로 관리, 비율은 테이블화하여 개정 대응).
- 이용자 등록·수정 시 본인부담 구분을 선택하며, 청구 계산은 해당 이용자의 구분 비율을 적용한다.

> **계산 흐름**: `등급별 수가(3-9-1) × 출석일수 = 총 급여비용` →
> `공단부담 = 총액 × (1 − 이용자 본인부담률)`, `본인부담금 = 총액 × 이용자 본인부담률(3-9-2)`.

#### 3-9-3. 기능 목록

- [ ] **수가표 관리 화면** (`hq_admin`, 등급별·연도별 입력·수정, 버전 이력)
- [ ] **이용자별 본인부담 구분** 등록·수정 (이용자 프로필, §3-2 연계)
- [ ] 장기요양 급여 항목 자동 계산 (등급 수가 × 출석일수 × 이용자 부담률)
- [ ] 월별 청구서·급여비용 명세서 생성·출력 (지점별 / 통합)
- [ ] 본인부담금 계산·청구서 생성 (개별 / 일괄)
- [ ] 청구 내역 이력·상태 (작성중 / 확정 / 수납완료) — 목록 **상태 필터** 제공 (V31 인덱스)
- [ ] 이용자 상세 **청구 탭** (§3-2)
- [ ] 공단 **청구내역상세 엑셀 import** (케어포식 연동, MVP)
- [ ] NHIS import **엑셀 파서 정규화** — 선행 **`처리상태` 열 자동 스킵·헤더 정규화** (케어포 공지 44438, 3차 벤치마크)
- [ ] import UI·온보딩: **롱텀 2026** — IE 접속 불가, **Chrome/Edge 필수** 안내 (엑셀 export 전제)
- [ ] **NHIS import reconciliation UI** — 배치별 행 매칭 상태 표시 (`MATCHED` / `DISCREPANCY` / `UNMATCHED`), 수동 매칭 보정 (`UNMATCHED → MATCHED`), 금액·일수 차이 강조 (DB: V19 / V21–V27 제약 — `memory/decisions.md` 2026-06-06)
- [ ] 공단 포털 **직접 전송·API** — MVP **제외** (후속, Could)
- [ ] 본인부담금 보호자 **발송·CMS 결제** — MVP **제외** (후속, v2)

#### 3-9-4. NHIS Import Reconciliation 모델 (사용자 확정 결과·DB 반영)

| 매칭 상태 | 의미 | UI 동작 |
|----------|------|---------|
| `MATCHED` | 공단 엑셀 행 ↔ ogada 이용자(`client_id`) **일치 + 금액·일수 일치** | 정상 표기, 청구서와 대조 완료 |
| `DISCREPANCY` | 이용자 매칭은 됐으나 **금액·일수 차이 존재** | 강조 표시, 차이 컬럼·재계산 트리거 |
| `UNMATCHED` | 인정번호·이름·생년월일로 자동 매칭 **실패** | 후보 이용자 검색·수동 연결 UI (`client_id` 설정 → `MATCHED`/`DISCREPANCY` 전이) |

> DB 제약: `MATCHED`/`DISCREPANCY`는 `client_id` 필수, `UNMATCHED`만 NULL 허용 (`chk_nhis_import_rows_match_requires_client` — V19).
> 매칭 이용자 지점 = 배치 지점 (V21 트리거). 부분 업데이트 금지 — 매칭 전이는 `client_id`와 함께 단일 트랜잭션 (decisions 2026-06-06).

### 3-14. 위생·안전·시설운영 (케어포 6-2~6-4, **사용자 확정: 2026-06-09, 결정 94**)

> **v3.1 Must** — 기존 §6 Won't(위생안전) **철회**. 6-1 주간식단표는 §3-5 `/meals`와 통합.

| 케어포 | 기능 | ogada | 버전 |
|--------|------|-------|------|
| 6-2 | 일일점검 | `/safety/daily-checks` | v3.1 |
| 6-3 | 정기점검 | `/safety/periodic-checks` | v3.1 |
| 6-3-1 | 감염병 관리 | `/safety/infection-control` | v3.1 |
| 6-4 | 시설운영일지 | `/safety/operation-log` | v3.1 |

- [ ] 일일·정기 점검 체크리스트·결함·조치 기록
- [ ] 감염병 발생·예방·소독 기록
- [ ] 시설운영일지(일별) 작성·인쇄

### 3-10. 서류 자동 생성 (우선순위: 🟠 Could)

- [ ] 이용자 개인별 케어 플랜 PDF 출력
- [ ] 급여 제공 기록지 자동 생성
- [ ] 각종 동의서 양식 출력

### 3-11. 관리자 대시보드 (우선순위: 🔴 Must)

#### 지점별 대시보드 (`branch_admin` 이하, `active_branch_id` 기준)

- [ ] 오늘의 출석 현황 요약 (해당 지점)
- [ ] 이용자 수 통계 (입소/퇴소/이용)
- [ ] 건강 이상 이용자 알림 목록
- [ ] 주요 지표 차트 (월별 출석률)

#### 통합 대시보드 (`hq_admin`)

- [ ] 전 지점 출석 현황 **한눈에 보기** (지점별 카드/표)
- [ ] 지점별 이용자 수·출석률 **비교**
- [ ] 전 지점 건강 이상 알림 **통합 목록** (지점명 표시)
- [ ] 지점 필터·기간 필터

### 3-12. 다지점·조직 관리 (우선순위: 🔴 Must)

| 구분 | 항목 | 지점별 관리 | 통합 관리 |
|------|------|------------|----------|
| 조직 | Organization(운영 주체) **신규 등록** | — | ✅ `platform_admin` (ogada 직원) |
| 조직 | Organization 내부 설정 | — | ✅ `hq_admin` |
| 지점 | Branch 등록·수정·비활성 | 조회만 | ✅ CRUD |
| 계정 | 직원 계정·역할·소속 지점 배정 | 지점 내 계정 조회 | ✅ 전 지점 |
| 이용자 | 이용자 CRUD | ✅ 소속 지점만 | 조회·집계만 |
| 출석 | 체크인/아웃·QR | ✅ 소속 지점만 | 조회·집계만 |
| 건강 | 건강·투약 기록 | ✅ 소속 지점만 | 조회·집계만 |
| 대시보드 | 현황·통계 | ✅ 지점 대시보드 | ✅ 통합 대시보드 |
| QR | QR 생성·스캔 | ✅ 지점 단위 | — |
| 설정 | 지점 운영 설정 | ✅ 지점 범위 | ✅ 전사 정책 |
| 청구 | 급여 청구·정산 | ✅ 소속 지점 | 조회·집계·확정 |
| 감사 | audit_log | 지점 이벤트 기록 | 전 지점 로그 조회 |

**핵심 엔티티**: `organizations` → `branches` → (`users`, `clients`, `attendance`, `health_records`, `billing`)
**청구 관련 엔티티**: `fee_schedules`(등급별·연도별 수가표, 전사 공통), `copay_rates`(본인부담 구분별 비율표), `clients.copay_type`(이용자별 본인부담 구분)

### 3-13. 배차·이동경로 (우선순위: 🟡 Should → **v1.3 Must**)

> **사용자 요청 (2026-06-07, 결정 60)**: 배차 이용 이용자 명단 + 탑승 경로 **지도 표시**.  
> **사용자 요청 (2026-06-14, 결정 74)**: **다중 차량** 자동 배차 — **차량 대수·총 인원·개별 특이사항** 입력, **운전자별 담당 안정성·등하원 거리 공정성** 목표 (§3-13-9).  
> **1차 구현 (결정 61·62)**: **수동 명단 + 수동 순서 + 지도**. `hq_admin`이 루트 **확정** 후 직원은 **명단·지도 조회만**. **픽업(PICKUP)만**, 정차 **최대 15명**. TSP·드롭·도로 길찾기는 후속.  
> **벤치마크 (BNK-7·BNK-8)**: 케어포 모듈 2「이동서비스」(일정·차량·이동서비스비·**지도보기**) — ogada **v1.3-A**는 **명단·지도 시각화(케어포 패리티, BNK-8)** — **이동서비스일지·청구(G15·G16)는 v1.3-C**. v1.3-B에서 **경로 최적화**로 차별화.  
> **파일럿 1주차(P1–P3) 제외** — v1.1 merge 안정 후 착수.  
> **67차 진전 (v1.3-A stack @ `f8d1b02`/`d484206` lineage)**: backend V47·`/api/v1/transport/*`·geocode proxy·unconfirm + **Clients transport profile** + **`TransportPilotServiceFlowE2eTest`** **PRESENT** · frontend transport UI·`TransportDisclaimer`·`TransportUnconfirmModal`(BNK-7·BNK-8) + **`pilotPageFlows` transport E2E** + **`transportLiveApi.e2e.test.js` harness** **PRESENT** — **live E2E run 잔여**(결정 73 post-merge).

#### 3-13-1. 일일 업무 흐름 (v1.3-A)

| 단계 | 역할 | 동작 | 화면 |
|------|------|------|------|
| ① 사전 등록 | `branch_admin`, `hq_admin` | 이용자 **「배차 이용」** on + **픽업 주소** | 이용자 등록/수정 |
| ② 명단·루트 편집 | `hq_admin` | 오늘·지점·**픽업** 명단 → 다중 선택 → **수동 순서** → 지도 미리보기 → **임시 저장(DRAFT)** | `/transport/runs/new` |
| ③ 루트 확정 | `hq_admin` | 순서·지도 최종 확인 후 **「배차 확정」** → `CONFIRMED` (이후 수정 불가) | `/transport/runs/:id` |
| ④ 운행 조회 | `caregiver`, `social_worker`, `branch_admin` | **확정된 루트만** 정차 명단·순번·지도 **읽기 전용** 조회 | `/transport/runs/:id` |
| ⑤ 후속 | — | 드롭(DROPOFF)·픽업 체크·출석 연동·TSP | v1.3-A.1 / v1.3-B |

**운행 단위 (v1.3-A)**: 지점 1곳 × 날짜 1일 × **방향 PICKUP 고정**. 드롭은 **v1.3-A.1 이후**.

**확정 게이트**: `caregiver` 등 직원은 `status = CONFIRMED` 인 루트만 API·UI에서 조회 가능. `DRAFT`는 `hq_admin`만 접근.

#### 3-13-2. 기능 범위 (3단계)

| 단계 | 범위 | Must? | 비고 |
|------|------|-------|------|
| **v1.3-A** *(사용자 확정)* | 배차 이용자 필터·당일 명단·**수동 정차 순서**·지도 **번호 마커**·**Kakao Directions 도로 경로 미리보기**·루트 저장/조회 | **◎ 1차 Must** | **★ 148차 deepen** @ `0c523cd`/`d46688d` — carefor 2-2 대비 **지도 경로 미리보기 우위**(BNK-255) · TSP·**G15 일지·G16 청구 제외** — UI에 「운영 편의용」 고지 |
| **v1.3-B** | **다중 차량** 자동 배차 제안·TSP·Directions **도로 경로**·구간 거리/시간·**운전자별 거리 공정성·담당 안정성** (§3-13-9) | Should | 결정 60 「최단 경로」 본체 · **영업 차별 핵심**(BNK-8) |
| **v1.3-C** | `vehicles` 차량 마스터·정원·**이동서비스비 청구**(케어포 2-5)·**G15 법정 서식** | Could | — |

#### 3-13-3. v1.3-A 상세 (수동 명단 + 지도)

**명단 (US-T01)**

- `clients.uses_transport = true` 인 이용자만 표시
- 당일 **퇴소·비활성** 제외, **지점 스코프**(`branch_id`) 강제
- 필터: `run_date`, `branch_id` — v1.3-A에서 `direction`은 **PICKUP 고정**(UI에 드롭 필터 없음)
 - 목록 컬럼: 이름·등급·픽업 주소·연락처·픽업 시간(`pickup_time`)·비고

**루트 생성 (US-T02 — v1.3-A 범위)**

1. 명단에서 이용자 **체크박스 다중 선택** — **최대 15명**/운행 (서버·UI 양쪽 검증, 결정 62)
2. 선택 목록에서 **드래그 앤 드롭**으로 방문 순서 지정 (`hq_admin` only, `DRAFT` 상태)
3. **출발/도착 = 센터(지점) 주소** — 경로: `센터 → 1번 → 2번 → … → 센터`
  - 정차의 `pickup_address`가 NULL인 경우 시스템은 자동으로 `clients.address`(이용자 기본 주소)를 사용합니다. `pickup_address`가 명시된 경우에는 해당 값을 우선 사용합니다.
4. 카카오맵 JS SDK + **서버 `TransportRoutePreviewService`(Kakao Directions API)** 로 주소→좌표·**도로 경로 미리보기** → 지도 **순번 마커** + **도로 폴리라인** @ `0c523cd`/`d46688d` (BNK-253~255) — live E2E run 잔여
5. 「임시 저장」→ `transport_runs`(`DRAFT`) + `transport_run_stops`
6. 「**배차 확정**」→ `CONFIRMED` — 직원 조회 가능, `hq_admin` 편집 **잠금**

**지도 UX (모바일 우선)**

- 지도 영역 + 정차 목록 **2패널**(PC: 좌우, 모바일: 탭 전환)
- 마커 클릭 시 해당 이용자 카드 하이라이트
- 주소 표시는 정차 목록에서 확인, 좌표 변환은 **카카오맵 JS SDK**가 담당

#### 3-13-4. 구현 방식

| 계층 | v1.3-A | v1.3-B/C (현행) |
|------|--------|-----------------|
| **지도 UI** | **카카오맵 JS SDK** | 동일 |
| **주소→좌표** | **카카오맵 JS SDK `Geocoder`** (클라이언트) | 동일 — **서버 Geocoding REST 프록시 없음** |
| **경로 표시** | 마커 간 **직선 polyline** | 카카오 Directions → **도로 폴리라인** |
| **순서** | **수동만** | TSP 휴리스틱 + 수동 오버라이드 |
| **API 키** | `VITE_KAKAO_MAP_JS_KEY`(지도·Geocoder), `KAKAO_REST_KEY`(Directions) | 동일 |

> **신규 의존성**: 카카오맵 JS SDK + Mobility Directions API (rules.md §12). **서버 Geocoding API는 사용하지 않음**.

#### 3-13-5. 데이터 모델 (v1.3-A 최소)

| 엔티티/컬럼 | 용도 | v1.3-A |
|-------------|------|--------|
| `clients.uses_transport` | 배차 이용 여부 | ✅ |
| `clients.address_search` | 이용자 기본 검색용 주소(필수, 정규화된 검색 단위: 시/도·시군구·도로명·우편번호 등) | ✅ |
| `clients.address_detail` | 상세주소(호수·층·참고사항 등, 자유문자) | ✅ |
| `clients.pickup_address` | 픽업 주소(개별 오버라이드, NULL이면 `clients.address_search` + `clients.address_detail` 사용) | ✅ |
| `clients.pickup_lat`, `pickup_lng`, `geocoded_at` | (선택) 저장 좌표 — 자동 배차 제안 등 서버 최적화 입력용 | △ |
| `clients.pickup_contact` | 픽업 연락처(저장: 암호화 권고; API: **`hq_admin`만 전체**, non-HQ는 **`010-****-5678` 마스킹** @ `c7941e9`) | ✅ |
| `clients.address_verified` | 주소 검증 여부 (boolean) — 기본 `false`, `hq_admin` 강제 저장 시 `false` 유지 | ✅ |
| `clients.address_verified_by` | 주소를 검증/강제저장한 사용자 id (nullable) | ✅ |
| `clients.address_verified_at` | 주소 검증/강제저장 시각 (timestamp, nullable) | ✅ |
| `clients.address_verification_deadline` | 강제 저장 후 검증 완료 기한(timestamp, nullable) — 권고: 24시간 | ✅ |
| `transport_runs` | 운행(날짜·`direction=PICKUP`·지점·상태·`confirmed_at`·`confirmed_by`) | ✅ |
| `transport_run_stops` | 정차(이용자·`stop_order`·`pickup_time`) — v1.3-A에 완료 체크 **없음** | ✅ |
| `transport_run_stops.geocode_status` | (레거시) 정차별 좌표 저장 상태 (`OK`/`PENDING`) — 지도 표시와 무관 | ✅ |
| `vehicles` | 차량 마스터 | ❌ v1.3-C |

주소 필드·검증 정책 (사용자 요구 반영)
- `clients.address_search`는 **필수**로 강제합니다. 이용자 생성/수정 시 서버는 입력된 주소에 대해 형식 검증(비어 있지 않음·최소 길이)을 수행합니다.
- `clients.address_detail`는 상세(호수·층·참고사항 등)로 자유 입력 허용.
- **지도 좌표 변환은 카카오맵 JS SDK `Geocoder`가 브라우저에서 수행** — 서버 Geocoding API 프록시 없음.
- 저장된 주소는 PII로 취급하여 DB 암호화(권고) 및 접근 제어 로그를 적용하도록 권고합니다.
**`transport_runs` 상태**: `DRAFT`(hq_admin 편집) → `CONFIRMED`(직원 조회 개방, **수정 불가**). `direction` 기본값 `PICKUP`.

#### 3-13-6. 화면·API (예비)

```
/transport                    — 오늘 명단·진행/완료 루트 목록
/transport/runs/new           — 명단 선택·수동 순서·지도 미리보기·저장
/transport/runs/:id           — 루트 상세·지도 (hq_admin: 확정 전 편집 / 직원: 확정 후 읽기 전용)
/transport/vehicles           — v1.3-C
```

| API (초안) | 메서드 | v1.3-A |
|------------|--------|--------|
| `/api/v1/transport/roster` | GET | 당일 배차 명단 |
| `/api/v1/transport/runs` | POST, GET | 루트 생성(DRAFT)·목록 |
| `/api/v1/transport/runs/{id}` | GET, PATCH | 상세·순서 수정 (`DRAFT`·hq_admin only) |
| `/api/v1/transport/runs/{id}/confirm` | POST | 배차 확정 → `CONFIRMED` (hq_admin only) |
| `/api/v1/transport/route-preview` | POST | 카카오 Directions 도로 경로 폴리라인 (좌표는 FE Geocoder 결과) |

> v1.3-A에 정차 완료 PATCH·드롭 run API **없음**.

#### 3-13-7. 권한·보안

| 역할 | v1.3-A |
|------|--------|
| `hq_admin` | 명단·루트 **생성·편집·확정** (`active_branch_id` 지점, B방식) |
| `branch_admin` | 이용자 `uses_transport` 설정; **확정 루트 조회** |
| `caregiver` | **`CONFIRMED` 루트만** 명단·지도 **읽기 전용** |
| `social_worker` | **`CONFIRMED` 루트만** 읽기 전용 |

 - `DRAFT` 루트: `hq_admin`만 GET/PATCH. 직원 API 403.
 - `CONFIRMED` 루트: 직원 GET 허용, PATCH/confirm 403.
 - 주소·좌표: 지점 스코프·RBAC 적용. **70차 @ `e7d4cf6`/`c7941e9`**: transport roster/runs API의 **pickup 주소·연락처는 `hq_admin`·`platform_admin`·`sysadmin`만 전체 노출** — `branch_admin`·`social_worker`·`caregiver`는 **마스킹**(SEC-D9·`010-****-5678` 패턴). frontend **`TransportPickupContact`** @ `1d910c2` — non-HQ tel 링크 없음. 저장 시 개인정보보호법·프로젝트 규정에 따라 암호화·접근통제 적용 권고(§3-2-1).
 - 지도 Geocoder: **브라우저(카카오맵 JS SDK)** 에서만 주소→좌표 변환; `confirmed_at`·`confirmed_by` 감사 로그

추가 권한 규칙(사용자 확정)
- `CONFIRMED` 상태의 루트는 **편집(순서 변경·주소·시간 수정 포함)을 `hq_admin`만 수행**할 수 있다.
- `hq_admin`은 필요 시 `CONFIRMED`를 `DRAFT`로 되돌려 수정 후 다시 `CONFIRMED` 가능(되돌림·확정 관련 이벤트는 `unconfirmed_by`·`unconfirmed_at`으로 감사 기록).
- 직원(`caregiver`/`social_worker` 등)은 `CONFIRMED` 루트에 대해 조회만 가능하며, PATCH/확정·해제 권한 없음.

#### 3-13-8. 확정·후속 (PLAN_NOTES #41)

| # | 항목 | 상태 |
|---|------|------|
| ① | 정차 상한 | ✅ **15명/운행** (결정 62) |
| ② | 확정 주체 | ✅ **`hq_admin` 확정 → 직원 조회** (결정 62) |
| ③ | 방향 | ✅ **픽업만** v1.3-A; 드롭 = v1.3-A.1 |
| ④ | TSP | v1.3-B |
| ⑤ | 출석·픽업 체크 | v1.3-B 이후 |
| ⑥ | 청구 | v1.3-C |
| ⑦ | 지도 | 카카오맵 (가정) |
| ⑧ | 차량 엔티티 | v1.3-C (15명 = 정원 상한으로 대체) |
| ⑨ | **다중 차량 자동 배차** | v1.3-B (§3-13-9) |
| ⑩ | **어르신 개별 특이사항(시간창 등)** | v1.3-B 입력 · v1.3-A는 `defaultPickupTime`·비고 수동 참고 |
| ⑪ | **운전자별 담당 안정성** | v1.3-B soft 목표 |
| ⑫ | **운전자별 등하원 거리 공정성** | v1.3-B soft 목표 |

#### 3-13-9. 자동 배차 최적화 조건 (v1.3-B, 사용자 요청 2026-06-14)

> **배경**: v1.3-A는 **단일 루트·수동** 배치. 본 절은 **센터 다중 차량·다중 운전자** 환경에서 `hq_admin`에게 **자동 배차 제안**을 생성할 때의 **입력 변수**와 **목표 제약**을 정의한다.  
> **범위**: v1.3-B — TSP·Directions와 **동시 설계**. v1.3-A는 본 절 **미적용**(수동 편집만).

##### 3-13-9-1. 입력 변수 (변수 조건)

| # | 변수 | 정의 | 데이터 소스 | 제약 |
|---|------|------|-------------|------|
| V1 | **센터 운행 차량 대수** | 당일·지점에서 **실제 운행**하는 차량 수 | `vehicles`(활성·지점 스코프) · `transport_runs.vehicle_id` | 차량 **정원**(`capacity`) ≤ 15명/운행(결정 62). 운행 차량 수 ≥ 1 |
| V2 | **어르신 총 인원** | 당일 배차 대상 **탑승 인원** | `GET /transport/roster` — `uses_transport=true`·활성·지점 스코프·퇴소 제외 | Σ(차량별 탑승) = 총 인원. 차량 정원 초과 **불가** |
| V3 | **어르신 개별 특이사항** | 이용자별 **픽업 시간·메모·제약** | `clients.default_pickup_time` · **`clients.transport_notes`**(신규, nullable) · (후속) 시간창 `pickup_earliest`/`pickup_latest` | **Hard**: 지정 시간창 위반 시 해당 정차 **배차 후보에서 제외** 또는 **경고+수동 확정 필수**. 예: 「아침 9시에 반드시 모시러 가야 함」→ `default_pickup_time=09:00` ± 허용 오차(기본 ±15분, 센터 설정) |

**특이사항 예시 (V3)**

| 유형 | 예시 | 처리 |
|------|------|------|
| 고정 픽업 시각 | 「매일 9시 정각 픽업」 | `default_pickup_time` + 시간창 Hard |
| 순서 제약 | 「A 어르신 탑승 후 B 어르신」 | v1.3-B.1 후속 — 동승·가족 그룹 ID |
| 일회성 메모 | 「오늘만 10시 이후」 | 당일 run 메모 또는 `transport_run_stops.pickup_time` 오버라이드 |
| 접근 제약 | 「휠체어·2층 계단 불가」 | `transport_notes` — UI 경고, 자동 배차 **soft 페널티** |

##### 3-13-9-2. 목표 제약 (최적화 목표)

| # | 목표 | 정의 | 측정 | 우선순위 |
|---|------|------|------|----------|
| O1 | **운전자별 담당 안정성** | **운전자(차량)별** 모시는·내리는 어르신 **구성 변동 최소화** | 전일(또는 직전 확정 run) 대비 **담당 이용자 변경 건수** · Jaccard 유사도 | **Soft — 가중치 높음** |
| O2 | **등하원 거리 공정성** | 각 운전자의 **등원+하원** 총 운행 거리가 **비슷**해야 함 (운전자 간 **공정성**) | Directions API 기준 **총 도로 거리(km)** · 표준편차·max-min 편차 | **Soft — 가중치 높음** |
| O3 | **경로 효율** | 센터 출발·복귀 포함 **총 거리·시간 최소** | TSP + 다중 경유 Directions | Soft — O1·O2 다음 |
| O4 | **시간창 준수** | V3 Hard 제약 **100%** | 정차별 ETA vs `pickup_time` | **Hard** |

**목표 함수 (개념)**

```
minimize  w1 × (담당 변경 건수)
        + w2 × (운전자 간 거리 편차)
        + w3 × (총 운행 거리)
subject to  차량 정원 · 시간창(V3) · 지점 스코프
```

- `w1`, `w2` > `w3` — **안정성·공정성**을 **단순 최단거리**보다 우선 (사용자 요청 2026-06-14).
- `hq_admin`은 제안안 **수동 오버라이드** 가능 — 오버라이드 사유 기록 권장(Mobiligent 「배차 이유 코드」 참고, BENCHMARK §10-4).

##### 3-13-9-3. 운행·UI 흐름 (v1.3-B)

| 단계 | 동작 |
|------|------|
| ① | `hq_admin`이 당일·지점·방향(PICKUP) 선택 |
| ② | 시스템이 **V1~V3** 로드 → **차량별 이용자·순서·예상 거리** 제안 생성 |
| ③ | UI: 차량(운전자) 탭별 명단·지도·**총 거리·담당 변경 건수·시간창 위반** 요약 |
| ④ | `hq_admin` **수동 조정** → 임시 저장(DRAFT) → **배차 확정**(기존 US-T02) |

##### 3-13-9-4. 데이터·API (v1.3-B 추가)

| 항목 | 용도 |
|------|------|
| `clients.transport_notes` | 배차 특이사항(자유 텍스트, PII 주의) |
| `transport_runs.driver_id` 또는 `vehicles.default_driver_id` | 운전자(직원) ↔ 차량 연계 |
| `transport_assignment_history` (후속) | 일별 차량↔이용자 매핑 — O1 안정성 산출 |
| `POST /api/v1/transport/runs/suggest` | V1~V3 입력 → 다중 run 제안(DRAFT 일괄 생성) |
| `branch_transport_settings` (또는 `branches` 확장) | 지점별 `pickup_tolerance_minutes`(기본 15), `w1`/`w2`/`w3`(기본 0.5/0.3/0.2) |
| DB unique 변경 | `uq_transport_runs_org_branch_date_direction` 폐기 → **`(organization_id, branch_id, run_date, direction, vehicle_id)`** unique (결정 75, 차량당 1 run) |

> **v1.3-A와의 관계**: v1.3-A는 **단일 run·수동**만. §3-13-9 API·다중 run 제안은 **v1.3-B부터** 제공.

##### 3-13-9-5. 사용자 확정 (2026-06-14, 결정 75 · 데모 후 재피드백)

| 항목 | 확정 |
|------|------|
| **범위** | **픽업 자동배차** (PICKUP) · 드롭 = v1.3-B.1 · **이번 주 PoC 목표** |
| **스키마** | **차량당 1 `transport_run`** (Q2-a) |
| **알고리즘** | **OR-Tools** VRP(차량 할당) + TSP(정차 순서) · **Kakao Directions** 도로 거리/시간 행렬 |
| **가중치** | 기본 **0.5 / 0.3 / 0.2** — `minimize w1×(담당 변경) + w2×(운전자 간 거리 편차) + w3×(총 km)` · **지점 설정 + UI 설명** |
| **시간창** | **±15분** 기본 · 지점 설정 변경 가능 · `clients.transport_notes` 추가 |
| **suggest 상한** | **`POST …/runs/suggest` ≤ 10회/지점/일** (PoC hard cap). 초과 시 429 + 「오늘 자동 제안 횟수 초과」 — **확정 run 개수 제한 아님** (차량 3대 = CONFIRMED run 3건 가능) |
| **Directions 비용** | suggest 10회/일이면 API 사용량은 무료 쿼터(5k/일) 대비 **충분히 여유** · 데모 확인 후 상한·fallback 재조정 |
| **UX** | §3-13-9-3 흐름 · 오버라이드 사유 코드 = v1.3-B.1 |

---

## 4. 비기능 요구사항

| 항목 | 요건 |
|------|------|
| 성능 | 페이지 로딩 3초 이내 (LTE 환경 기준) |
| 확장성 | 전국 SaaS — 테넌트·지점 수 증가에 따른 수평 확장 가능 구조 |
| 가용성 | 서비스 시간 중 99.5% 이상 (SaaS SLA 목표) |
| 보안 | HTTPS 필수, OWASP Top 10 대응 — **인증 API rate limiting**(SEC-D13·BE-11) v1.1 착수 · develop→test merge(SEC-D14) 전 test 배포 금지 |
| 개인정보 | 개인정보보호법, 장기요양보험법 준수 |
| 접근성 | WCAG 2.1 AA |
| 반응형 | 모바일(360px), 태블릿(768px), PC(1200px) 지원 |
| 브라우저 | Chrome, Safari, Edge 최신 2버전 이상 지원 |
| 백업 | 일 1회 자동 백업, 30일 보관 |
| API | REST (Java 백엔드), React SPA에서 소비 |
| 아키텍처 | React SPA ↔ Spring Boot REST API 분리, Organization-Branch 멀티테넌트 |
| 데이터 격리 | `organization_id` + `branch_id` 이중 격리, API 레벨 스코프 검증 |
| 테넌트 격리 | Organization 간 데이터·인증·설정 완전 분리 (SaaS 필수) |
| 배포 | 클라우드 벤더 **무관**, Docker 기반 이식 가능 구조 |

---

## 5. 화면 목록 (예비)

```
/ (로그인)
/platform (ogada 직원 — 신규 고객 센터 등록 — platform_admin)
/dashboard (지점 대시보드 — branch scope)
/dashboard/hq (통합 대시보드 — hq scope)
/branches (지점 목록·관리 — hq_admin)
/branches/:id (지점 상세)
/clients (이용자 목록 — 지점 필터)
/clients/new (이용자 등록)
/clients/:id (이용자 상세)
/attendance (출석 관리)
/attendance/checkin (수기 체크인/아웃)
/attendance/qr/generate (지점 QR 생성·출력 — 직원용)
/guardian/checkin (보호자 QR 스캔 체크인/아웃 — B방식)
/health (건강 기록)
/health/:client_id (이용자별 건강 기록)
/meals (식사 관리 — v1 이후)
/programs (프로그램 관리 — v1 이후)
/staff (직원 관리)
/billing (청구·정산 — MVP)
/billing/:id (청구서 상세)
/reports (통계 리포트 — 지점별/통합)
/settings (시스템·지점 설정)
/guardian (보호자 포털 — v1 이후)
/transport (배차·이동경로 — v1.3)
/transport/runs/:id (당일 루트·지도)
```

---

## 6. 우선순위 요약 (MoSCoW)

| 구분 | 기능 |
|------|------|
| 🔴 Must (MVP v1 전체 포함) | 인증, 플랫폼관리, 다지점·조직, 이용자, 출석(수기+QR), 건강, **청구·정산(reconciliation 포함)**, 대시보드 |
| 🟡 Should (v1 이후) | 식사 관리, 프로그램 관리, **배차·이동경로(§3-13, v1.3)**, 보호자 알림(SMS/알림톡), 보호자 풀 포털 |
| 🔴 **v3 / v3.1 Must** (결정 94) | **직원 HR 전체(§3-8-a)** · **요양·목욕 리포트(§3-5-a)** · **프로그램 그룹·리포트(§3-6-a)** · **위생·안전·시설운영일지(§3-14)** |
| 🟡 **v1.2 화면 밀도 P0** (BNK-6) | 보호자 관리 화면, 본인부담 입금·미납, 등급변동 이력, 대시보드 실데이터, 2단 SideNav — §1-5-2 |
| 🟠 Could (v1 이후) | 서류 자동 생성, 공단 포털 직접 연동, **공단 평가 2026 지표 자동화** |
| ⚪ Won't (v1) | 외부 EMR 연동, 생체인식 로그인, **재무회계·세무·4대보험**, **CMS·간편결제** (v2), NFC/RFID 출석(의도적 미채택) |

### 6-1. MVP v1 범위 (사용자 확정: 2026-06-05)

| # | 기능 모듈 | 포함 여부 | 비고 |
|---|----------|----------|------|
| 0 | 플랫폼·고객 등록 (§1-3, `platform_admin`) | ✅ 포함 | ogada 직원이 Tenant·첫 `hq_admin` 생성 |
| 1 | 다지점·조직 관리 (§3-12) | ✅ 포함 | Organization-Branch, RBAC 스코프 |
| 2 | 인증 및 계정 관리 (§3-1) | ✅ 포함 | JWT + RBAC + **7역할 UI** + 지점 선택기 |
| 3 | 이용자 관리 (§3-2) | ✅ 포함 | `branch_id` 소속, 지점/통합 조회 |
| 4 | 출석 관리 (§3-3) | ✅ 포함 | 수기(직원) + QR 셀프(B방식) |
| 5 | 건강 기록 (§3-4) | ✅ 포함 | 지점 스코프 |
| 6 | **청구·정산 (§3-9)** | ✅ 포함 | 급여 항목 계산, 월별 청구서, **NHIS reconciliation UI** (2026-06-05 확정 + 2026-06-06 reconciliation 추가) |
| 7 | 관리자 대시보드 (§3-11) | ✅ 포함 | 지점별 + 통합 |

> Should/Could(식사·프로그램·보호자 알림·직원·서류·공단연동·평가·재무회계)는 MVP v1 **외**.

### 6-2. 구현 우선순위 P0–P3 (2026-06-06 벤치마크 기반 — `BENCHMARK_REPORT.md` §5-3)

> MVP v1 내부 **구현 순서**. coder/db_architect 스프린트 입력. MoSCoW(§6) ⊆ P0–P2.

| 순위 | 기능 묶음 | 산출물 | 검증 |
|------|----------|--------|------|
| **P0** | Tenant·Branch·7역할 RBAC + 출석(수기) + 건강 + **청구(수가표 B·copay·월별 명세) + NHIS 엑셀 import(처리상태 정규화)** + 지점/통합 대시보드 | `/dashboard`, `/dashboard/hq`, `/clients`, `/attendance/checkin`, `/health`, `/billing`, `/billing/imports/nhis` | 파일럿(2지점, `branch_admin`+`caregiver`) 1주차 완료 기준 |
| **P1** | QR B 출석 + `guardian` / `client_user` + **NHIS reconciliation UI** (`MATCHED`/`DISCREPANCY`/`UNMATCHED` 행 매칭 상태) | `/attendance/qr/generate`, `/guardian/checkin`, reconciliation 행 보정 화면 | 케어포 4단계 UX 동등 |
| **P2** | 보호자 **기록 열람**(알림 없음) + 청구 상태 필터(`?status=`) + 청구 상태 이력 | `/guardian` 열람, `/billing?status=DRAFT/CONFIRMED/PAID` | v1 백엔드 — **G8 초대·명세**는 v1.1 |
| **P3** | 프로그램·식사·이동서비스·직원·평가 자동화 | v1.1+ — Should/Could | 경쟁사 패리티(케어포 주야간 전 모듈) |

> 일정 무관(결정 18) — 우선순위는 **품질·차별화 우선**, P0가 닫혀야 P1 시작.

### 6-3. v1.2 화면 밀도 P0 (BNK-6, 2026-06-06 — ROADMAP v1.2)

| P0 | REQUIREMENTS | USER_STORIES | 신규 DB |
|----|--------------|--------------|---------|
| 보호자 관리 | §3-7 확장 | Epic K | 불필요 |
| 입금·미납 | §3-9-3 후속 | Epic L (G13) | `billing_claims` 상태 |
| 등급변동 이력 | §3-2 확장 | Epic M (G14) | 이력 테이블 |
| 실데이터 대시보드 | §3-11 | Epic M | 불필요 |
| Recharts 차트·건강 알림 | §3-11 | Epic M (FE-12) | `recharts` 의존성 |
| 2단 SideNav | — | Epic UX | 불필요 |
| Platform·NHIS 배치·reconciliation·청구·copay·수가표 UI | §1-3·§3-9 | Epic G·M (FE-13, US-G00a) | 불필요(API 활용) |
| 운영·보안·계정 보안·로그인 이력 UI | §3-1·§9 | Epic M (FE-14) | 불필요(감사 로그·세션 API 활용) |

> KPI: 케어포 12모듈 대비 **모듈 가중 커버리지 ≥60%** (결정 49).

---

## 7. 1주차 스프린트 계획 (초안)

**완료 기준 (사용자 확정: 2026-06-05 — 7역할 전부 포함)**

| # | 검증 항목 | 통과 조건 |
|---|----------|----------|
| 1 | SaaS 테넌트 격리 | 서로 다른 Organization 데이터 교차 접근 불가 |
| 1b | `platform_admin` | `/platform`에서 신규 Tenant + 첫 `hq_admin` 생성 E2E |
| 2 | `hq_admin` | `/dashboard/hq` 통합 집계 + 지점 전환 후 해당 지점 CRUD + 청구 |
| 3 | `branch_admin` | `/dashboard` 지점 대시보드 + 이용자·출석·건강 CRUD |
| 4 | `social_worker` | 이용자·건강 기록 CRUD, 출석 조회 |
| 5 | `caregiver` | 수기 출석·건강 기록 입력 |
| 6 | `guardian` | `/guardian` 기록 열람 + `/guardian/checkin` QR 체크인 |
| 7 | `sysadmin` | `/settings` 시스템 설정 화면 접근 (운영 데이터 CRUD 없음) |
| 8 | 출석 2경로 | 수기 + QR(B) 모두 E2E 동작 |
| 9 | 대시보드 | 지점·통합 대시보드 실데이터 출력 |
| 10 | 청구·정산 | 출석·등급 기반 월별 청구서 생성·출력 |

| 순서 | 작업 | 산출물 |
|------|------|--------|
| 1 | 프로젝트 초기화 | Spring Boot + React + PostgreSQL, SaaS 멀티테넌트 스키마 |
| 2 | 플랫폼·조직·7역할 RBAC | `/platform`, Org/Branch, 7역할 JWT·라우팅, Branch Switcher |
| 3 | 이용자 CRUD | `organization_id` + `branch_id` 기반 API·화면 |
| 4 | 출석 (수기+QR B) | 수기 + 지점 QR + 보호자 스캔 |
| 5 | 건강 기록 | 지점 스코프 건강·투약 |
| 6 | 청구·정산 | 급여 계산, 월별 청구서 API·`/billing` 화면 |
| 7 | 대시보드 + 역할별 홈 | 지점/통합 대시보드, **7역할 E2E** |

**의존 관계**: 2번 선행 → 3~5번 → 6번(출석·이용자 데이터 필요) → 7번.  
> **범위 증가**: 청구·정산·`platform_admin` 추가로 1주차 목표 대비 작업량 증가 — 일정 무관 확정에 따라 스프린트 분할 검토.

---

## 8. 미확정·추가 확인 필요 사항

상세 질문 목록은 `docs/planning/PLAN_NOTES.md`의 **「추가 질문」** 섹션을 참고한다.

- 보호자 **알림** 채널 (v1 이후)
- ~~`API_SPEC.md` 초안 작성~~ → **완료** (2026-06-05, `docs/technical/API_SPEC.md`)
- ~~`FLOWCHART.md` 화면 흐름도 작성~~ → **완료** (2026-06-05, `docs/planning/FLOWCHART.md`)
- ~~주민등록번호 수집·암호화 정책 확정~~ → **확정: 수집 + 암호화·마스킹·별도동의** (§3-2-1)
- ~~**수가 이용시간 밴드** — 파일럿 표준 이용시간~~ → **확정** (2026-06-07): 08-20 = 12h → **v1 단일 밴드 10~13h 고정** (§3-9-1, PLAN_NOTES #35)
- **공단 청구내역상세 엑셀 실컬럼** 샘플 — 파일럿 센터 1곳 확보 필요 (PLAN_NOTES #27, 벤치마크 G7)
- **본인부담 구분 매핑** — 케어포 공개자료는 `일반 15% / 경감·의료 7.5% / 기초 0%` 3구분으로 단순화. ogada는 법령 기반 4구분(`GENERAL` 15% / `REDUCED_40` 9% / `REDUCED_60` 6% / `MEDICAID` 0%) 유지 — **파일럿 센터 실제 분포 확인 시 4→3 통폐합 검토** (PLAN_NOTES #30)
- **ogada 가격 정책** — 케어포 주야간 **월 33,000원**(VAT 포함) 벤치마크 기준 tier·flat 선택 필요 (영업·플랫폼 정책, PLAN_NOTES #31)
- **다지점 HQ 대시보드** 경쟁사 사례 — 영업 자료·FAQ 추가 조사 (BENCHMARK §8 #4, PLAN_NOTES #32)
- ~~**보호자 초대 채널** (v1.1 US-J01)~~ → **확정** (2026-06-07, 결정 59): **이메일 링크 단일** — §8-1
- ~~**#36 운영 게이트 (dirty-tree 재오염 방지)**~~ → **확정** (2026-06-07, 결정 56·63): **양 스트림** · L1 **Fixed 차단+경고**(자동 커밋 금지) · L2/L3 build 구현 대기 — §8-2

### 8-1. 보호자 초대 채널 (US-J01) — **확정: 이메일 링크 단일** (2026-06-07, 결정 59)

> 이용자 등록 시 **대표 보호자 연락처**는 이미 필수(US-D01). **초대 채널**은 그 보호자에게 **「ogada 보호자 포털 계정을 만들어 쓰세요」**라는 안내를 **어떤 경로로 보낼지**를 뜻한다.

| 단계 | 누가 | 무엇 |
|------|------|------|
| ① | 센터장 | 이용자 프로필에서 **보호자 이메일** 입력 → **「초대 보내기」** |
| ② | 시스템 | **이메일**로 초대 링크(URL + 토큰) 발송 |
| ③ | 보호자 | 링크 클릭 → 비밀번호 설정 → `guardian` 계정 생성·이용자와 연결 |
| ④ | 보호자 | `/guardian`에서 기록·명세 열람 (v1.1 J02) |

**v1.1 확정 정책**

| 항목 | 값 |
|------|-----|
| 채널 | **`EMAIL` 단일** (SMS·알림톡 **v1.1 제외**) |
| 발송 대상 | 보호자 **이메일 주소** (`guardian_clients` 연동) |
| 초대 링크 | `https://{tenant}/guardian/invitations/{token}/accept` |
| 토큰 만료 | **7일** (가정 — 재발송 UI로 갱신, PLAN_NOTES #35) |
| 재발송 | 센터장이 동일 이메일로 재발송 가능 (이전 토큰 무효화) |
| v2 추가 | SMS fallback·카카오 알림톡 (US-J03, 유료 채널) |

| 채널 | v1.1 | 비고 |
|------|------|------|
| **이메일 링크** | **◎ 확정** | 무료·구현 단순·v1.1 무료채널 원칙 정합 |
| SMS 코드/링크 | ❌ 제외 | v2 fallback |
| 둘 다 선택 | ❌ 제외 | 운영·구현 복잡도 회피 |

### 8-2. #36 운영 게이트 — **확정** (2026-06-07, 결정 56·63)

> **목적**: BE-6/FE-6 「테스트·산출물 작성 후 develop 미커밋 → false Fixed」 재발 차단. **구현은 build 승인 후** — planner는 스펙만 확정.

| 항목 | 정책 |
|------|------|
| 적용 범위 | **backend + frontend** (`src/backend`·`src/frontend` develop 브랜치) |
| L1 (에이전트) | coder 턴 종료 시 working tree 검사 → 미커밋 완료 산출물 있으면 **Fixed/`[x]` 차단 + 경고** — **자동 커밋 금지** |
| L2 (pre-commit) | commit 전 test/build PASS (build 구현) |
| L3 (CI) | develop push 시 양 스트림 CI (build 구현) |
| 상세 | `PLAN_NOTES.md` #36 · `ROADMAP.md` 이관 규율 9항 · `INFRA-1~3` |

- 요구사항 사용자 승인 (`<!-- approved-by-user: true -->` — 사용자 직접)

> 사용자 지시 (2026-06-07): build 즉시 실행 승인.
> 실행 지침:
- coder에게 `INFRA-1~3` 착수 지시 및 build 실행을 요청한다.
- L1 게이트는 coder의 각 턴마다 항상 활성화한다(매 턴 검사).
- frontend dirty-tree 정리(특히 B07 #6, B09 관련 커밋)를 build/merge 전 선행 작업으로 지정한다.

위 조치는 사용자 요청에 따른 운영·릴리스 절차 변경이며, planner는 스펙·작업 지시를 문서화함. 사용자 승인 마커는 planner가 추가하지 않음.

> 빌드 실패 처리 규칙 (추가: 2026-06-07, 사용자 지시)
- 원칙: 빌드 실패 시 즉시 빌드를 중단하고 실패 원인과 복구 계획을 문서화한다.
- coder 책임:
  1. 실패 로그(빌드 stdout/stderr, 테스트 실패 요약)를 확보하여 `INFRA-1-start` TODO에 첨부 및 보고한다.
  2. 원인 요약(예: 컴파일 에러/테스트 실패/의존성 불일치/환경 변수 누락 등)과 임시 대응(스태시·리버트·빠른 패치)을 기록한다.
  3. 수정 브랜치 또는 버그 이슈를 생성하고(`branch: fix/<short-desc>`), 관련 커밋과 PR 링크를 보고한다.
  4. 민감정보(시크릿·토큰)는 로그에 노출하지 않고, 필요한 경우 마스킹 후 보고한다.
  5. 수정 완료 후 재시도(build/rerun tests) 결과를 보고하고, 실패 반복 시 planner에게 즉시 에스컬레이션한다.
- 추적: 위 항목은 `PLAN_NOTES.md`에 회고 및 원인 분석으로 누적 기록한다.

---

*이 문서는 planner 에이전트가 관리합니다. 변경 시 `memory/decisions.md`에 이력을 남겨주세요.*
<!-- approved-by-user: true -->
