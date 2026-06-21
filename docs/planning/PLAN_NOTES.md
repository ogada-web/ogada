<!-- doc:owner=PLN doc:audience=COD,TSR,UXD,DBA,BNK,TWR updated=2026-06-21T23:54:00Z -->
<!-- tech_writer-sync: TWR 302차 2026-06-21T23:54:00Z — docs ops 주기 동기화 — **BE `a6eb8b7`/FE `5fd468b` 확정·V1–V169·109 route·87 page·모듈 KPI 78.62%·merge gate 657** · 301차 Q614(선행입금) Q612(직원출퇴근) 완반영 · PLAN_NOTES Must 갭 재정리 · **미해결 4건: 출석통계 FE wire(Q613)·QR이미지(Q590)·결석버튼 UX·청구필터저장 API** · **다음 우선순위**: ① 출석통계 contract 정합(coder) ② QR 이미지 생성(coder) ③ 결석 버튼 UX ④ 청구 월별 필터 저장 API(coder) -->
<!-- tech_writer-sync: TWR 301차 2026-06-21T23:15:00Z — docs ops 자동 갱신 완료 · Q612/Q614·G-BILLING-DEPOSIT-ORDER-GUARD·G-STAFF 출근방식 · CHANGELOG/FAQ/USER_MANUAL/ADMIN_GUIDE/DEPLOYMENT_GUIDE 메타·섹션 갱신 · baseline 확정 `BE a6eb8b7`/`FE 5fd468b` · 모듈 KPI 78.62% · merge gate 657 · next: 출석 통계 FE wire·QR 생성 이미지·직원 MOBILE/NFC·본인부담 비율 저장 API -->
<!-- tech_writer-sync: TWR 300차 2026-06-21T20:42:00Z — docs ops 자동 갱신 완료 · Q609/Q612/Q613 신규/정정 · CHANGELOG/FAQ/USER_MANUAL/ADMIN_GUIDE/DEPLOYMENT_GUIDE 메타·섹션 갱신 · baseline 확정 `BE 560057f`/`FE 53d65a0` · 모듈 KPI 78.45% · merge gate 651 · next: 출석 통계 FE wire·QR 생성 이미지·직원 MOBILE/NFC·본인부담 비율 저장 API -->
<!-- planner-sync: PLN 185차 2026-06-21T21:30 KST — BNK-477~480·TSR 1234~1241차 · ★ 모듈 78.45% KPI 정본 · ★ G-ATTENDANCE-ROSTER-STATUS ✅ superset · ★ NHIS #44 G16 parity 재입증 · QA-B222 Open→Planned · ★ QA-B223 Fixed @ `61e1970` · merge gate 647(FE147+BE500) · BE SYNCED/FE BLOCK(hang) · cross-stream BLOCK(FE) · QA Open 0(active) -->
<!-- planner-sync: PLN 184차 2026-06-21T20:30 KST — BNK-470~471·TSR 1223~1226차 · QA-B212/B213/B214 Open→Planned · ★ QA-B209~B214 Fixed carry · ★ G-STAFF-DOCUMENT-REPOSITORY P3 △→✅ FULL-STACK closure(P3 candidate 제거) · ★ G-BATHING ✅ full-stack carry(183차 partial 정정) · ★ 신규 G-MENU-PERMISSION-MATRIX P3「가정」 · 4축 가정 번복 0 · merge gate 634(FE141+BE493) · cross-stream SYNCED · QA Open 0(active) -->
<!-- planner-sync: PLN 183차 2026-06-21T12:00 KST — BNK-464~465·TSR 1214~1215차 · QA-B204 Open→Planned · ★ QA-B195~B205 Fixed carry · ★ G15-KAKAO-QUOTA-DASH △→✅ closure(P3 candidate 제거) · ★ G-BATHING BE API △→✅ partial(FE wire P2) · 4축 가정 번복 0 · merge gate 623(FE135+BE488) · cross-stream BLOCK(BE) · QA Open 0(active) -->
<!-- planner-sync: PLN 182차 2026-06-21T11:30 KST — BNK-456~458·TSR 1192~1203차 · QA-B195/B196/B192 Open→Planned · ★ QA-B193/B194 Fixed · ★ G-BILLING 3건 △→✅ full-stack closure(P3 candidate 제거) · ★ G32 FAQ21740 parity deepen · merge gate 612(FE128+BE484) · cross-stream BLOCK · QA Open 0(active) -->
<!-- planner-sync: PLN 181차 2026-06-21T08:30 KST — BNK-447~452·TSR 1184~1191차 · QA-B187/B188 Open→Planned · ★ QA-B186 Fixed @ `82a542c` · ★ G-STAFF-LEAVE-STATUS △→✅ full-stack closure(V166·`onLeaveCount`·휴직 Badge·P3 candidate 제거) · ★ 4축 교차검증 가정 번복 0 · ★ 신규 candidate G-COMM-CALLER-AUTH P3(silverangel 221562 발신번호 인증 마감 6/23) · merge gate 602(FE122+BE480) · FE/BE merge pending 2 · cross-stream BLOCK(FE+BE) · QA Open 0(active) -->
<!-- planner-sync: PLN 180차 2026-06-21T05:30 KST — BNK-445~446·TSR 1177~1179차 · QA-B182 Open→Planned · ★ QA-B181 Fixed @ `a18b30e` · ★ G-BANK-EXCEL-8 ✅ FE closure · ★ G-STAFF-NHIS ✅ full-stack · merge gate 590 · FE SYNCED/BE merge pending 1 · cross-stream BLOCK(BE) · QA Open 0(active) -->
<!-- planner-sync: PLN 179차 2026-06-20T23:00 KST — BNK-435~441·TSR 1165~1167차 · QA-B178 Open→Planned · ★ QA-B177 Fixed @ `a0f051d` · ★ G-BILLING-PRIOR-DEPOSIT-GUARD ✅ closure · ★ G-BANK-EXCEL-8/G-STAFF-NHIS-EXCEL-IMPORT △ BE partial · merge gate 581 · FE SYNCED/BE merge pending 1 · cross-stream BLOCK(BE) · QA Open 0(active) -->
<!-- planner-sync: PLN 178차 2026-06-20T21:00 KST — BNK-432~434·TSR 1154~1155차 · ★ G14 plan-form △→✅ closure(V164·`/care-plan-form`) · ★ G24 FAQ21800 8-item parity ✅ · ★ QA-B169/B170/B171/B172 Fixed · QA-B116 Planned(origin/test push 464 BE+105 FE) · QA-B95 Planned carry · ★ G-BILLING-PRIOR-DEPOSIT-GUARD P2 · ★ G-BANK-EXCEL-8 P3 candidate · merge gate 569 · FE/BE `@d723d5a`/`@80b9619` SYNCED WT CLEAN · cross-stream SYNCED · QA Open 0(active) -->
<!-- planner-sync: PLN 177차 2026-06-20T18:00 KST — BNK-424~429·TSR 1137~1143차 · QA-B169/B170 Open→Planned · ★ QA-B163 Fixed @ `94f2535` · ★ QA-B167 Fixed @ `ba74bb5` · ★ G15-KAKAO-INTEGRATION 6-layer 우위 · ★ G15-KAKAO-QUOTA-DASH P3 candidate · merge gate 555 · FE `@ba74bb5`/BE `@e2b764b` WT DIRTY 9M+4U · cross-stream BLOCK(FE+BE) · QA Open 0(active) -->
<!-- planner-sync: PLN 176차 2026-06-20T15:00 KST — BNK-419~423·TSR 1127~1131차 · QA-B163 Open→Planned · ★ QA-B159 Fixed @ `bfad37d` · ★ G-CASH-RECEIPT-LOG end-to-end 재입증 ✅ · ★ FAQ21823 partial+ · merge gate 543 · FE merge pending 2/BE SYNCED · cross-stream BLOCK(FE) · QA Open 0(active) -->
<!-- planner-sync: PLN 175차 2026-06-20T12:00 KST — BNK-417~418·TSR 1118~1119차 · QA-B159 Open→Planned · ★ FAQ21823 근로계약 갱신 summary+대시보드 widget @ `f31c346` · QA Open 0(active) · merge gate 533 · FE `@f31c346` SYNCED/BE merge pending 2 · live E2E 126 PASS/19 SKIP -->
<!-- planner-sync: PLN 174차 2026-06-20T07:00 KST — BNK-406~412·TSR 1100~1107차 · QA-B157 Open→Planned · QA Open 0(active) · ★ QA-B155/B156 Fixed · ★ G26 yearBasis+NTS CSV ✅ · ★ G-7-1 Excel ✅ · ★ G-CASH-RECEIPT-LOG 6-계층 deepen · ★ G-CASH-RECEIPT-TAX-DEDUCTION-EXPORT △→✅ · ★ 신규 candidate G-PROVIDER-CHANGE-COUNSEL P3 · merge gate 522 · FE `@99b795a` SYNCED/BE `@35d1560`(merge pending 1) WT CLEAN · live E2E 126 PASS/19 SKIP -->
<!-- planner-sync: PLN 173차 2026-06-20T04:00 KST — BNK-399~405·TSR 1086~1096차 · QA Open 0(active) · ★ QA-B153/B154 Fixed · ★★★ G-CASH-RECEIPT-LOG 4-계층 closure ✅ · ★ 172차 P2 gap → closure · ★ 신규 candidate G-CASH-RECEIPT-TAX-DEDUCTION-EXPORT P3 · merge gate 511 · FE `@8aebe55`/BE `@58ff35e` develop=test SYNCED WT CLEAN · live E2E 126 PASS/19 SKIP -->
<!-- planner-sync: PLN 172차 2026-06-19T23:30 KST — BNK-393~398·TSR 1074~1085차 · QA Open 0(active) · ★ QA-B150/B151/B152 Fixed · ★ 신규 갭 1 G-CASH-RECEIPT-LOG P2「확인」(BNK-398) · ★ 신규 candidate G-LTM-DIRECT-SYNC P3「가정·미확인」 · 케어포 3-1 segment nav ✅ · G32 4-계층 superset · merge gate 498 · FE `@9b80505`/BE `@caeac0d` develop=test SYNCED WT CLEAN · live E2E 124 PASS/19 SKIP -->
<!-- planner-sync: PLN 171차 2026-06-19T16:00 KST — BNK-386~392·TSR 1062~1073차 · QA-B151 Open→Planned · ★ G32 FAQ21797 6/6 full-stack closure · QA Open 0(active) · merge gate 485 · FE `@e55ae96`/BE `@b9e0947` WT CLEAN -->
<!-- planner-sync: PLN 170차 2026-06-19T15:00 KST — BNK-381~385·TSR 1050~1061차 · QA-B149(frontend)+QA-B148(backend) Open→Planned 태스크화(develop WT dirty-tree·`VisitBatchConfirmPanel` loading guard / `LiveE2eBootstrapService` branch-scoped G21 seed readiness WIP 미커밋·이관 규율 5·6·7·기능 갭 아님·QA-B142/B145/B147 lineage) · QA Open 0(active) · Planned 4건(QA-B148+B149+B116+B95) · QA-B116 Planned(origin/test push 417 BE+54 FE·post-merge 1756/1756+1518/1518 PASS) · QA-B95 Planned carry · ★ BNK-385 본인부담 7단 7/7 parity·func 107-leaf · ★ BNK-384 FAQ21817 상태변화 기록지 주1회 7일(이지케어 3-FAQ 트리니티)·G39 P3「가정」 · 백본 zero drift·신규 갭 0 · merge gate 471(FE54+BE417) · FE `@0002943`/BE `@7898aa5` develop WT DIRTY 2M(test CLEAN) · live E2E 123 PASS/19 SKIP -->
<!-- planner-sync: PLN 169차 2026-06-19T11:50 KST — BNK-376~380·TSR 1040~1049차 · ★ G21 seed readiness NHIS row-batch linkage ✅ @ `c0403b0` · ★ QA-B142~B145 Fixed · QA Open 0(active) · QA-B116 Planned(origin/test push 412 BE+49 FE) · QA-B95 Planned carry · merge gate 461 · FE `@0915f80`/BE `@c0403b0` SYNCED WT CLEAN · page 85 · live E2E 123 PASS/19 SKIP -->
<!-- planner-sync: PLN 168차 2026-06-18T23:45 KST — BNK-368~375·TSR 1028~1039차 · ★ G21 standalone NHIS comparison panel @ `797c529` · ★ G41 filter-year @ `28e5525` · ★ silverangel G15 실데이터 일지 full-stack 우위(BNK-375) · ★ QA-B141 Fixed(local)·QA-B142/B143 Planned · QA Open 0(active) · QA-B116 Planned(origin/test push 407 BE+44 FE·FE merge pending 1) · QA-B95 Planned carry · merge gate 451 · FE `@28e5525` DIRTY 2M/BE `@f932fd3` DIRTY 2M -->
<!-- planner-sync: PLN 167차 2026-06-18T22:30 KST — BNK-362~367·TSR 1016~1027차 · ★ G21 batch-confirm readiness full-stack closure(△→✅) · ★ G-SCHEDULE-FIX-LTM-COMPARE BE closure(P3→✅·`GET /visits/nhis-comparison`) · ★ G-7-1-PRINT-BUNDLE ✅+ · ★ G-CHANGE-REASON-AUDIT P3 candidate · QA Open 0(active) · QA-B116 Planned(origin/test push 38 FE+402 BE·BE merge pending 1) · QA-B95 Planned carry · merge gate 440 · FE `@f232285` SYNCED/BE `@8a8c5b3` WT CLEAN · 백본 zero drift·4축 번복 0·신규 갭 candidate 1 -->
<!-- planner-sync: PLN 166차 2026-06-18T21:00 KST — BNK-355~361·TSR 1004~1015차 · ★★★ G15 별지 제22호 일지④ input+print+export 3-축 full-stack closure → P2 Must ✅ CLOSED · ★ V155 transport waypoint non-empty CHECK · ★ G15 export direction @ `72124f7` · QA Open 0(active) · ★ QA-B137/B138 Fixed(B138 live-e2e guardian credential fallback @ `94c65e2`) · QA-B116 Planned(31 FE+396 BE·FE SYNCED·BE merge pending 1) · QA-B95 Planned carry · merge gate 428 · FE `@94c65e2` SYNCED/BE `@72124f7` WT CLEAN · 백본 zero drift·4축 번복 0·신규 갭 0 -->
<!-- planner-sync: PLN 165차 2026-06-18T18:00 KST — BNK-348~354·TSR 1000~1003차 · ★ G41 ✅+ deepen · ★ G21 RFID compare ✅ full-stack · G-SCHEDULE-FIX-LTM-COMPARE P3 · QA Open 0(active) · QA-B116 Planned(25 FE+390 BE·FE SYNCED·BE merge pending 1) · merge gate 415 · FE `@caa215f`/BE `@dac19d3` WT CLEAN -->
<!-- planner-sync: PLN 164차 2026-06-18T15:00 KST — BNK-342~347·TSR 980~991차 · ★ QA-B135 Fixed @ `d7f1a9a` · QA Open 0(active) · QA-B116 Planned(merge EXECUTED local·post-merge PASS·origin/test push 18 FE+384 BE) · QA-B95 Planned carry · ★ BNK-347 G15 partial+++·driver signature·일지④ 인쇄·별지 P2 Must · ★ BNK-346 G21 RFID 7-code P1 · merge gate 402·local SYNCED · FE `@1c8f236`/BE `@d7f1a9a` WT CLEAN -->
<!-- planner-sync: PLN 163차 2026-06-18T11:30 KST — BNK-335~341·TSR 970~979차 · ★ QA-B131/B132/B133 Fixed · QA Open 0(active) · QA-B116 Planned(merge EXECUTED local·origin/test push pending) · QA-B95 Planned carry · ★ BNK-341 carefor transport 10-leaf·4-축 우위 · ★ BNK-339 FAQ21799 신규직원 건강검진 △ @ `8e6310a` · merge gate 391·local SYNCED · FE `@38642e2`/BE `@40ef105` WT CLEAN -->
<!-- planner-sync: PLN 162차 2026-06-18T07:30 KST — BNK-333~334·TSR 955~969차 · ★ QA-B127/B128/B129/B130 Fixed · ★ QA-B131 Planned(live-e2e script path) · QA Open 0(active) · QA-B116 Planned(merge 3 FE+1 BE) · QA-B95 Planned carry · ★ BNK-334 silverangel 6종 zero drift·CMS parity · ★ BNK-333 carefor 7-x Route 1:1 · merge FULLY UNBLOCKED · FE `@7d2cb4a`/BE `@09df8c7` WT CLEAN -->
<!-- planner-sync: PLN 161차 2026-06-17T18:00 KST — BNK-321~323·TSR 952~954차 · ★ QA-B127 Planned(develop HEAD 56 FAIL) · ★ QA-B128 Planned(BE WT DIRTY 1M+2U) · QA Open 0(active) · QA-B116 Planned(merge 420) · QA-B95 Planned carry · ★ G-STAFF-WORKLOG·G-HOSPITAL-ESCORT P3 candidate · ★ G-CASH-RECEIPT deepen · merge 420 BLOCK · FE `@188ce71`/BE `@73cffc5` WT BLOCK -->
<!-- planner-sync: PLN 159차 2026-06-18T09:00 KST — BNK-307~310·TSR 929~931차 · ★ func 2-9 verification closure·audit trail FE wire full-stack·L02 nursing live E2E harness · QA-B121 Planned(live E2E·FE merge BLOCK) · QA-B116 Planned(merge 41) · QA-B95 Planned(partial RUN) · merge 398 BLOCK(FE only) · FE `b48252a`/BE `30243f7` WT CLEAN -->
<!-- tech_writer-sync: TWR 212차 2026-06-18T13:30 KST — docs ops audit-trail RBAC 보강 완료(USER_MANUAL·ADMIN_GUIDE·DEPLOYMENT_GUIDE·FAQ·CHANGELOG) · next P2(213~215차): Q417~Q420·CSV/PDF export·L03 nursing 5 leaf·NHIS #44·Kakao v2·guardian contact mask -->
<!-- planner-sync: PLN 158차 2026-06-18T06:00 KST — BNK-303~306·TSR 919차 · ★ func 2-7/2-8 full-stack·audit trail read API·NHIS #44 5-date·K008 FAQ21768 · QA Open 0 · QA-B116 Planned(merge 34) · QA-B95 Planned · merge 385 FULLY UNBLOCKED · FE `8b68fdb`/BE `6eb9cc0` WT CLEAN -->
<!-- planner-sync: PLN 157차 2026-06-18T03:00 KST — BNK-298~302·TSR 898~909 · ★ G15 일지④ PUT persistence+FE 편집 closure live(v1.3-C Must 후보) · ★ silverangel CMS 3-method mainService.do → G2b parity · ★ longterm KRDS DRIFT → V103 seed authoritative · QA-B120 Fixed @ `af4d7f8` · QA-B116 Planned(merge pending 28·post-merge 재검증) · QA-B95 Planned carry · 신규 갭 0·가정 번복 0 · merge 374 FULLY UNBLOCKED · FE `cb30f24`/BE `c13800c` WT CLEAN -->
<!-- planner-sync: PLN 160차 2026-06-18T12:00 KST — BNK-311~315·TSR 932~942차 · ★ QA-B121 Fixed @ `0695244` · ★ QA-B122 Fixed @ `f0e52b8` · QA Open 0(active) · QA-B116 Planned(merge pending 48) · QA-B95 Planned carry · ★ BNK-315 신규 갭 candidate G-CASH-RECEIPT P3「가정」(FAQ21700 현금영수증) · merge 410 FULLY UNBLOCKED · FE `0baabe9`/BE `f0e52b8` WT CLEAN -->
<!-- planner-sync: PLN 156차 2026-06-18T00:00 KST — BNK-292~297·TSR 887~897 · ★ QA-B115/B117/B118 Fixed · QA-B116 Planned(merge pending) · QA-B95 Planned carry · ★ BNK-297 이지링크(EzLink) PC 클라이언트 → web-first 차별화 가정 강화 · ★ G-COGNITIVE-WORKSHEET(=G29) P3 candidate FAQ21781 · merge 364 FULLY UNBLOCKED · FE `825c6b0`/BE `8a1f342` WT CLEAN -->
<!-- planner-sync: PLN 155차 2026-06-17T21:00 KST — BNK-286~291·TSR 875~886 · ★ QA-B115/B116/B117 Open→Planned 태스크화(3 BLOCK·dirty-tree+test regression·이관 규율 5·6·7·기능 갭 아님) · QA-B112/B114 Fixed · QA-B95 Planned carry · ★ BNK-286~291 transport cluster deepen(V143~V146·결정 96) · NHIS #44 이동서비스비 일지④ 의무→법정 일지 입력 폼 P2→v1.3-C Must 검토 · ezCare 계획/청구 2-track+RFID→split-view P1 · 신규 갭 0·가정 번복 0 · merge 351 BLOCK · FE `d3bef42`/BE `114411f` WT DIRTY -->
<!-- planner-sync: PLN 154차 2026-06-17T18:00 KST — 사용자 요청 plan 변경(배차 IA·명단 연락처·SideNav 비주얼·SEC-005 refresh sessionStorage) · 결정 96 -->
<!-- planner-sync: PLN 153차 2026-06-17T12:00 KST — BNK-280~285·TSR 863~874 · ★ BNK-285 케어포 3-product line·dual-source numbering closure · ★ QA-B113 Fixed @ `b000d92` · QA-B112/B114 Open→Planned · QA-B95 Planned · merge 341 BLOCK · FE `b000d92`/BE `7ac0a46` WT DIRTY -->
<!-- planner-sync: PLN 152차 2026-06-17T09:00 KST — BNK-275~279·TSR 850~862 · QA-B110 Fixed @ `e54a699` · FE develop→test 다중 merge live @ `7106106`(4 pending) · BNK-278 PDF p.92 7-8 통계 leaf 미확인 1→0(G26 통계 ✅ full 확정) · BNK-279 L02_M09/M10/M14 △ partial+ · BNK-277 G21 split-view FE closure·J03 quiet-hours guard · QA-B95 operation BLOCK 잔존(신규 증상 live-e2e bootstrap HTTP 500 + guardian credentials 미설정·COD Fixed는 tester 미검증) · QA Open 0(active) · 신규 evidence angelsitter #774·FAQ 21745/21765 K008(payroll out-of-scope) · merge 330(326 BE + 4 FE·FULLY UNBLOCKED) · FE `6b34d31`/BE `f6f1756` WT CLEAN -->
<!-- planner-sync: PLN 151차 2026-06-17T06:00 KST — BNK-269~274·TSR 838~849 · ★ G26 ③ 이동서비스비 월별 통계 ✅ full stack(3-function 완성) @ `3672bbe`/`09e4ec17` · FE develop→test MERGED+origin/test PUSH @ `68da0aa` · QA-B110 backend dirty-tree recurrence Open→Planned · QA-B95 Planned 유지 · QA Open 0(active) · 신규 갭 candidate G-STAFF-CHANGE-COUNSEL P3(「가정」 주야간 적용성 미확인) · merge 320(BE only·⚠ QA-B110 선행 BLOCK) · FE `68da0aa`/BE `c5f1325` WT DIRTY 2M -->
<!-- planner-sync: PLN 150차 2026-06-17T03:00 KST — BNK-262~268·TSR 826~837 · ★ G26 7-8 본인부담/의료비공제 통계 대시보드 ✅ full stack @ `d8f1fdf`/`3481eb8` · FE develop→test MERGED+origin/test PUSH @ `d8f1fdf` · QA-B106 Fixed @ TSR 827 · QA-B95 Planned 유지 · QA Open 0(active) · merge 315(BE only) · FE `d8f1fdf`/BE `3481eb8` -->
<!-- planner-sync: PLN 149차 2026-06-16T21:00 KST — BNK-256~261·TSR 813~825 · L02 rpt cluster end-to-end ✅(M04/M05/M06/M11/M12/M16/M17) · G21 청구반영 검은/빨간 배지 UI ✅ full @ `25ca88e` · FE develop→test local MERGED @ `25ca88e` · QA-B106 origin/test push 누락 Open→Planned · QA-B95 Planned 유지 · QA Open 0(active) · G-Payroll triple-source P3 · merge 309(BE) · FE `25ca88e`/BE `b38c6f7` -->
<!-- planner-sync: PLN 148차 2026-06-16T18:00 KST — BNK-252~255·TSR 801~812 · v1.3-A Kakao route preview ✅ · L02_M04/M05 rpt ✅ full · L02_M17 rpt △ BE · V141 · QA-B101~B104 Fixed · QA Open 0 · QA-B95 Planned · merge 312 · FE `388e1da`/BE `ae7e744` -->
<!-- planner-sync: PLN 147차 2026-06-16T12:00 KST — BNK-248~251·TSR 789~800 · L02_M13 ✅ full · L02_M15 ✅ FE · G30 phone panel ✅ full · FE merged @ `4299914` · L02 6/15(40%) · law.go.kr MOHW 2025-247 evidence · plan/claim P2 · QA Open 0 · QA-B95 Planned · merge 301 · FE `c5f82a6`/BE `c655743` -->
<!-- planner-sync: PLN 146차 2026-06-16T09:00 KST — BNK-244~247·TSR 777~788 · L02_M01/M03 ✅ full · G-7-1-4CHANNEL ✅ full stack · G30 FAQ21841 BE · L02 4/15 · SEC-D29/D30 신규 audit · QA Open 0 · QA-B98/B99 Fixed · QA-B95 Planned · merge 649 FULLY UNBLOCKED · FE `61141a6`/BE `de25b3e` -->
<!-- planner-sync: PLN 145차 2026-06-16T06:00 KST — BNK-240~243·TSR 765~776 · L02_M07 ✅ full · live-e2e harness deepen · 7-1 4채널 P2 · MOHW 2026-126 · longterm oscillating noise · QA-B99 Planned · QA-B95 Planned · merge 636 BLOCK(FE) · FE `6f53978` WT DIRTY 3M/BE `18ff83e` WT CLEAN -->
<!-- planner-sync: PLN 144차 2026-06-16T00:30 KST — BNK-236~239·TSR 753~764 · G30 evidence window ✅ deepen · G39 ✅ partial+ · L02_M02 ✅ FE wire · G-BODY-RESTRAINT(L02_M07) P2 · G-STAFF-LIFECYCLE P2 · G-REVENUE-EXPENSE P3 · func.php 107 leaf · QA Open 0 · QA-B95 Planned · merge 625 · FE `95e7e96`/BE `df14e15` -->
<!-- planner-sync: PLN 143차 2026-06-15T21:00 KST — BNK-232~235·TSR 741~752 · G24b list ✅ · G19 harness △ · G30/G39 P2 deepen △ · #44 lawImg DRIFT · G18-SHORT 연장 · QA-B95 Planned · merge 612 · FE `73094f9`/BE `73df04d` -->
<!-- planner-sync: PLN 142차 2026-06-15T18:00 KST — BNK-227~231·TSR 729~740 · G24b dashboard ✅ · G41 enum 23+ ✅ · QA-B95 Planned · live E2E env BLOCK · merge 602 · FE `3cbe582`/BE `1e21b20` -->
<!-- planner-sync: PLN 141차 2026-06-15T14:00 KST — BNK-224~226·TSR 717~728 · G-ONBOARD-SUPPORT ✅ full · G24b ✅ full · QA-B94 Fixed · merge 589 FULLY UNBLOCKED · FE `92b9eff`/BE `f4c8beb` -->
<!-- planner-sync: PLN 140차 2026-06-15T11:00 KST — BNK-219~223·TSR 705~716 · QA-B93 Fixed · G-ONBOARD-SUPPORT △ BE · merge 577 FULLY UNBLOCKED · FE `2ccc88e`/BE `735dd53` -->
<!-- planner-sync: PLN 139차 2026-06-15T08:00 KST — BNK-217~218·TSR 693~704 · L03 13/14 ✅ effective 100% · QA-B92 Fixed · QA-B93 Planned · merge 566 BLOCK(BE) · FE `89dc52d`/BE `6b0238a` -->
<!-- planner-sync: PLN 138차 2026-06-15T05:00 KST — BNK-213~216·TSR 681~692 · v1.3-B ✅ full · L03_M01/M06 △ BE · QA-B88/B89/B90 Fixed · merge 555 FULLY UNBLOCKED · FE `3845f0c`/BE `a4352a8` -->
<!-- planner-sync: PLN 137차 2026-06-15T02:00 KST — BNK-209~212·TSR 669~680 · L03_M11/M13/M14/M04 ✅ full · QA-B86/B87 Fixed · QA-B88/B89/B90 Planned · v1.3-B △ partial+ · merge 545 BLOCK · FE `97108f2`/BE `090b2d7` -->
<!-- planner-sync: PLN 136차 2026-06-14T23:00 KST — BNK-204~208·TSR 657~668 · G-NURSING-PRESSURE-ULCER ✅ full · L03_M11 ✅ full · L03_M14 BE ✅ partial+ · QA-B85 Fixed · QA-B86/B87 Planned · merge 534 BLOCK(BE) · FE `246df56`/BE `1a822d2` -->
<!-- planner-sync: PLN 135차 2026-06-14T20:00 KST — BNK-199~203·TSR 642~656 · G21 batch-confirm ✅ full · G17b ✅ full · QA-B83/B84 Fixed · 신규 갭 G-NURSING-PRESSURE-ULCER P1(v3.1 Must 6번째) · merge 521 UNBLOCKED · FE `ad319d7`/BE `3bd6a43` -->
<!-- planner-sync: PLN 134차 2026-06-14T17:00 KST — BNK-195~198·TSR 634~641 · G21 batch-confirm ✅ partial+ · US-UX-05 ✅ · QA-B81/B82 Fixed · merge 512 UNBLOCKED · FE `13e691e`/BE `c22a5dc` -->
<!-- planner-sync: PLN 133차 2026-06-14T15:00 KST — 배차 자동 최적화 변수·제약(다중 차량·담당 안정성·거리 공정성) · 사용자 요청 -->
<!-- planner-sync: PLN 132차 2026-06-14T14:00 KST — BNK-191~194·TSR 623~633 · 7-5 ✅ full · J03 quiet-hours ✅ partial+ · QA-B81/B82 Planned · merge 500 BLOCK(FE) · FE `111f056`/BE `a057739` -->
<!-- planner-sync: PLN 131차 2026-06-14T13:30 KST — US-UX-05 SideNav 5그룹 토글(운영·이동·출석·기록·청구) · 사용자 요청 -->
<!-- planner-sync: PLN 130차 2026-06-14T07:00 KST — BNK-188~190·TSR 612~622 · 7-5 ✅ partial+ · MOHW 2025-247 · LCMS 평가 SLA P3 · QA-B78/B79 Planned · merge 489 BLOCK · FE `bebd874`/BE `b893e97` -->
<!-- planner-sync: PLN 130차 2026-06-14T07:00 KST — BNK-188~190·TSR 612~622 · 7-5 ✅ partial+ · MOHW 2025-247 · LCMS 평가 SLA P3 · QA-B78/B79 Planned · merge 489 BLOCK · FE `bebd874`/BE `b893e97` -->
<!-- planner-sync: PLN 129차 2026-06-14T05:30 KST — BNK-185~187·TSR 600~611 · G41/G41b ✅ partial+ · G-STAFF-WELFARE P3 · G-ONBOARD-SUPPORT P2 · QA-B76/B77 Fixed · merge 479 FULLY UNBLOCKED · FE `e14ba10`/BE `32f87f1` -->
<!-- planner-sync: PLN 128차 2026-06-14T04:00 KST — BNK-180~184·TSR 587~599 · G30 ✅ full · G34-QUAL ✅ partial+ · G41 △ BE · QA-B74 Fixed · merge 468 FULLY UNBLOCKED · FE `5146895`/BE `6191b91` -->
<!-- planner-sync: PLN 127차 2026-06-14T02:30 KST — BNK-176~179·TSR 574~586 · 8-12 ✅ partial+ · J03 readiness ✅ partial+ · G34-QUAL P2 · QA-B74 Planned · merge 455 BLOCK(FE) · FE `443efca`/BE `229f84c` -->
<!-- planner-sync: PLN 126차 2026-06-14T01:00 KST — BNK-172~175·TSR 562~573 · #44 P0 ✅ · 8-12 deepen · G42 partial+ · QA-B72 Fixed · merge 443 FULLY UNBLOCKED · FE `a7a6004`/BE `39ee679` -->
<!-- planner-sync: PLN 125차 2026-06-13T23:30 KST — BNK-168~171·TSR 550~561 · G30 ✅ partial+ · 8-12 aggregated API ✅ partial+ · EZCare K008~K014 P3 · merge 430 FULLY UNBLOCKED · FE `07956f5`/BE `5692662` -->
<!-- planner-sync: PLN 124차 2026-06-13T21:00 KST — BNK-164~167·TSR 538~549 · G9-COG ✅ FE+BE · FAQ21824 checklist ✅ partial+ · G-7x-1 guard ✅ partial+ · G9-COPAY-NAMING ✅ · merge 418 FULLY UNBLOCKED · FE `e77b7e4`/BE `edd2771` -->
# 기획 메모 (planning/PLAN_NOTES.md)

> **작성**: planner 에이전트 (`PLN`) · tech_writer 에이전트 (`TWR`)  
> **최종 갱신**: 2026-06-21 (302차 TWR — **자동 기획 동기화** ·docs ops 주기 갱신·미해결 Must 4건 재정리·coder 다음 액션 명확화) | 185차 PLN — **자동 기획 동기화** BNK-477~480·TSR 1234~1241차·QA-B222 Planned·★ QA-B223 Fixed·★ 모듈 78.45% KPI·★ G-ATTENDANCE-ROSTER-STATUS ✅ superset·merge gate 647·cross-stream BLOCK(FE)·QA Open 0) | 301차 TWR — ops 자동 동기화 carry  

### [TWR] 302차 docs 자동 갱신 (2026-06-21, 23:54 UTC — **baseline 확정·미해결 Must 갭 4건 재정리**)

**상황**: 301차 완료 후 코드 merge 진행 중 — **출석 통계·QR 생성·결석 버튼·청구 필터 저장** 미구현 Must 기능 정리

**갱신 내용**:

| 문서 | 변경 사항 | 상태 |
|------|----------|------|
| **PLAN_NOTES** | **미해결 Must 기능 재정리** · **4건 상황 분류** · **다음 우선순위 명확화** · coder/planner 지시 갱신 | ✅ |
| **메타 헤더** | `updated=2026-06-21T23:54:00Z` · TWR 302차 기록 · baseline carry `BE a6eb8b7`/`FE 5fd468b` | ✅ |

**baseline 확정**: `BE a6eb8b7`·`FE 5fd468b`·V1–V169·**109 route**·**87 page**·**모듈 KPI 78.62%**·**merge gate 657**

**302차 분석 결과 — 미해결 Must 기능 4건 상황**:

| # | 기능 | 상태 | 문서 이슈 | 다음 액션 | 우선순위 |
|---|------|------|----------|----------|---------|
| 1 | **출석 통계 FE wire** (`/attendance/stats`) | API ✅(`GET /api/v1/attendance/stats/monthly`·BE `560057f`) · FE `5fd468b` **UI 부재·contract 갭** | **Q613 기록만** · `yearMonth`/`dailyRates`/`clientStats` 필드 정합 필요 · Swagger 우회 | **coder** — FE 화면 구현·API contract 정합 | **P2** |
| 2 | **QR 생성 이미지** (`/attendance/qr-scan`) | API ✅(`POST /api/v1/attendance/qr/generate`·payload base64) · FE **이미지 렌더·다운로드 미구현** | **Q590 payload ✅·이미지 갭** · 모바일 웹뷰 QR 인식 테스트 미확인 | **coder** — qrcode.js 라이브러리 · 이미지 생성·표시·다운로드 · 테스트 | **P3** |
| 3 | **결석 버튼 UX** (`/attendance` 화면) | API ✅(`POST /api/v1/attendance/absence`·clientId/date) · FE **버튼·모달 미구현** | **Q94 FAQ 기록만** · Swagger 우회 · API 계약 미확정 | **UXD** — 모달·버튼 명세 · **coder** — FE 구현 | **P2** |
| 4 | **청구 필터 저장 API** (월별·조회·인쇄·재발행) | API **`GET /billing/reports/filters?month=...` 미구현** · FE **`appliedFilters` echo** ✅(`a6eb8b7`/`5fd468b`) | **Q601 echo 완료·저장 API 미정·월별 조회 필터 저장 API 부재** | **coder** — 백엔드 `BillingReportFilterService`·`filtersForMonthAndBranch()` 구현 | **P2** |

**coder 다음 액션 (302차)**:
1. **출석 통계 FE wire** — `GET /api/v1/attendance/stats/monthly` 응답 필드·구조 확정 → FE `/attendance/stats` 화면 구현·테이블/차트 선택
2. **QR 이미지 생성** — `POST /api/v1/attendance/qr/generate` 응답 base64·PNG 렌더 → 다운로드·모바일 인식 테스트
3. **결석 버튼** — UXD 명세 후 `/attendance` 모달·버튼 추가
4. **청구 필터 저장** — BE `GET /billing/reports/filters?month=YYYY-MM` 엔드포인트 구현 → 월별·기간·수동 필터 저장

**다음 TWR 갱신 신호**: coder 1~4번 항목 **1건 이상 구현 완료** 시 Q631~Q634(신규) 기록·CHANGELOG 갱신·USER_MANUAL §1-5 갱신

---

### [PLN] QA 피드백 반영 (2026-06-21, 185차 — BNK-477~480 · TSR 1234~1241차 · QA-B222 Open→Planned · QA Open 0 · ★ QA-B223 Fixed @ `61e1970` · ★ 모듈 78.45% KPI · ★ G-ATTENDANCE-ROSTER-STATUS ✅ superset · QA-B116 Planned · QA-B95 Planned carry)

| 항목 | 내용 | 반영 문서 |
|------|------|-----------|
| **git baseline** | BE develop/test `@61e1970` · `test..develop` **0/0 SYNCED** · WT **CLEAN** · **1755/1755 PASS** · FE develop `@8383f8d` · test `@a4ea2d5` · `test..develop` **0/3** pending · WT **CLEAN** · test **1956/1956 PASS** · develop pre-merge **hang BLOCK** · merge gate **647**(FE147+BE500) · origin/test push **500 BE+147 FE** · live E2E **SKIP** · **107 route·87 page·V1–V168** · **BE Test 237** · **FE test 432** · **모듈 78.45%** | ROADMAP CURRENT BASELINE |
| **QA-B222 Planned** | FE develop pre-merge vitest hang 재발(`@8383f8d` serial pool fix **불충분**·~872 tests·EasyPayPanel 인근·exit 143) · merge pending 3 · TSR 1234~1241차 Open → PLN 185차 Planned | QA_FEEDBACK Open→Planned · ROADMAP P0 |
| **QA-B223 Fixed carry** | BE attendance roster live API routing/RBAC · merge EXECUTED @ `61e1970` · TSR 1237차 Fixed | QA_FEEDBACK Fixed carry |
| **BNK-477~480** | **★ 모듈 78.45% KPI 정본**(29 feature·△4 잔여·❌5 out-of-scope) · **★ G-ATTENDANCE-ROSTER-STATUS ✅ superset** @ `0c69060`/`@61e1970` · **★ module 8 0.75→0.8**(US-R03 mobile) · **★ NHIS #44 G16 parity 재입증** · **★ module 7 11/11 Route 1:1** · **백본 4종 276차 zero drift** · **4축 가정 번복 0** | ROADMAP·REQUIREMENTS·USER_STORIES |
| **잔여 P0/P3** | **COD QA-B222 vitest hang fix** → **tester FE merge(3)** → **origin/test push(500 BE+147 FE)** → **QA-B116 post-merge** → **QA-B95 operation 승격** · **P3 carry** G-STAFF-ANNUAL-SCHEDULE · G-STAFF-WORK-ATTENDANCE · G-STAFF-WORK-SCHEDULE-NHIS-EXCEL · G-MENU-PERMISSION-MATRIX · G-COMM-CALLER-AUTH(6/23) | ROADMAP v2·v3 |

**coder/ops 다음 액션 (185차)**: ① **COD QA-B222**(vitest hang root-cause·EasyPayPanel/serial pool·`VITEST_CONCURRENCY.md`) ② **tester FE merge(3)** @ `6bde24a`+`3bffb17`+`8383f8d` ③ **origin/test push**(500 BE+147 FE) ④ **QA-B116 post-merge** ⑤ **QA-B95** operation 승격.

> **184차→185차 delta**: merge gate 634→**647** · BE develop `@b583c11`→**`61e1970`**(1739→**1755/1755**·SYNCED) · FE develop `@fd15a2f`→**`8383f8d`**(test `@a4ea2d5`·**0/3 pending**·pre-merge hang) · **모듈 78.28%→78.45%** · **QA-B222 Open→Planned** · **★ QA-B223 Fixed** · **cross-stream SYNCED→BLOCK(FE hang)** · origin/test push **493+141→500+147** · FE test 431→**432** · route 108→**107**.

### [BNK] BNK-477~480 인사이트 (2026-06-21) — ★ 78.45% KPI · ★ 출석 roster superset · ★ NHIS #44 parity

| BNK | 인사이트 | planner 반영 |
|-----|----------|-------------|
| **BNK-480** | **모듈 78.45% KPI 정본** — 29 feature 22.75/29(✅20·△4·❌5 out-of-scope) · HEAD zero advance · merge gate **647** carry | REQUIREMENTS §1-5-2 · ROADMAP baseline |
| **BNK-479** | **NHIS #44 G16 parity 재입증** — `TransportServiceFeeService` 5-row ↔ 제34조 ①~⑤ | PLAN_NOTES #44 carry · REQUIREMENTS G16 |
| **BNK-478** | **module 7 11/11** demo `view.cost_*` ↔ `/billing/*` · **module 8 P3 deepen**(8-3 연간일정·8-4 직원 출퇴근 NFC/mobile) | ROADMAP v3 P3 · PLAN_NOTES `### 추가 질문` |
| **BNK-477** | **G-ATTENDANCE-ROSTER-STATUS ✅ superset** @ `0c69060`/`@61e1970` — `clientName`·`status`·`usesTransport` · 케어포 func 2-3 | USER_STORIES · REQUIREMENTS |
| **BNK-477~480** | **4축 가정 번복 0** · 백본 4종 276차 zero drift · silverangel weekly notice 0 · 신규 core 갭 0 | PLAN_NOTES carry |

### [TWR] 291차 docs 자동 갱신 (2026-06-21, 07:50 UTC — Q598–Q601 신규 · 현장 운영 부록)

**상황**: 최근 코드 구현(G-BATHING API, QR 생성 갭, 청구 필터)을 Must 기능으로 문서화·현장 운영 절차 보강

**갱신 내용**:

| 문서 | 변경 사항 | 상태 |
|------|----------|------|
| **FAQ.md** | **Q598** 목욕 일정 월별 복사(G-BATHING BE API) · **Q599** 출석 QR 생성(payload·이미지 갭) · **Q600** 공단 자동 제출(NTS P3) · **Q601** 청구 필터 `appliedFilters`(FE wire ✅) | ✅ |
| **USER_MANUAL.md** | **부록 A1–A5** 월말 청구·출석·건강·목욕·필터 현장 운영 가이드 추가 | ✅ |
| **CHANGELOG/ADMIN_GUIDE/DEPLOYMENT_GUIDE** | meta 헤더 갱신(`updated=2026-06-21T07:50:00Z`) | ✅ |

**baseline 확정**: `BE 0c9518a` · `FE 580a86b` · V1–V166 · **108 route · 87 page** · **merge gate 614** · **290차 반영 완료**

**291차 완료 항목**:
- ★ **Q598 목욕 일정 월별 복사** — `CopyBathingSchedulesFromPreviousMonthResponse` API · `POST /api/v1/care/bathing-schedules/copy-from-previous-month` · BNK-465
- ★ **Q599 출석 QR 생성 갭** — payload ✅ · 이미지 생성 P3 · 모바일 인식 P3 · Must 기능 but FE wire 미완료
- ★ **Q600 공단 NTS 자동 제출** — 현재 수동·v2+ roadmap · `G-CASH-RECEIPT-NTS-API` P3
- ★ **Q601 청구 필터 `appliedFilters`** — `BillingReportAppliedFilters` · 서버 우선·인쇄 헤더 포함 · BNK-457 ✅
- ★ **부록 A1–A5** — 월말·출석·건강·목욕·필터 현장 운영 체크리스트·API·프로세스

**다음 우선순위** (PLN 184차 carry):
1. **origin/test push**(493 BE+141 FE) → **QA-B116 post-merge 재확인**
2. **QA-B95 operation 승격**(126 PASS/19 SKIP carry)
3. **COD 출석 roster API 확장** (P2·현재 API-only)
4. **FE QR 이미지 생성** (P3·qrcode.js + navigator.mediaDevices)
5. **G-CASH-RECEIPT-NTS-API** (P3·국세청 연동)

---

### [PLN] QA 피드백 반영 (2026-06-21, 184차 — BNK-470~471 · TSR 1223~1226차 · QA-B212/B213/B214 Open→Planned · QA Open 0 · ★ QA-B209~B214 Fixed carry · ★ G-STAFF-DOCUMENT-REPOSITORY △→✅ FULL-STACK closure · ★ G-BATHING ✅ full-stack carry · QA-B116 Planned · QA-B95 Planned carry)

| 항목 | 내용 | 반영 문서 |
|------|------|-----------|
| **git baseline** | FE develop/test `@fd15a2f` · `test..develop` **0/0 SYNCED** · WT **CLEAN** · **1955/1955 PASS** · BE develop/test `@b583c11` · `test..develop` **0/0 SYNCED** · WT **CLEAN** · **1739/1739 PASS** · merge gate **634**(FE141+BE493) · origin/test push **493 BE+141 FE** · live E2E **126 PASS/19 SKIP** · **108 route·87 page·V1–V167** · **BE Test 236** · **FE test 431** | ROADMAP CURRENT BASELINE |
| **QA-B212 Planned** | FE develop→test merge pending 2 @ `fd15a2f`(21-slot panel + repository-progress API wire) · TSR 1226차 Fixed → PLN 184차 Planned | QA_FEEDBACK Open→Planned · ROADMAP merged |
| **QA-B213 Planned** | vitest locked-wrapper 5m+ hang · TSR 1226차 미재현 Fixed → PLN 184차 Planned(monitor carry) | QA_FEEDBACK Open→Planned |
| **QA-B214 Planned** | BE develop→test merge pending 1 @ `b583c11`(21-slot repository progress API) · TSR 1225차 Fixed → PLN 184차 Planned | QA_FEEDBACK Open→Planned · ROADMAP merged |
| **QA-B209~B211 Fixed carry** | G-BILLING overdue·US-R02 staff status print·pilotPageFlows merges @ `f6266ec`~`d2815d2` | QA_FEEDBACK Fixed carry |
| **BNK-470~471** | **★ G-STAFF-DOCUMENT-REPOSITORY P3 △→✅ FULL-STACK closure** @ `03d0d43`/`fd15a2f`/`b583c11` · **470차 P3 candidate 제거** · **★ G-BATHING ✅ full-stack carry** @ `9a957fb`/`a426663`(183차 BE partial 정정) · **★ 신규 G-MENU-PERMISSION-MATRIX P3「가정」**(FAQ21695) · **★ 4축 교차검증 가정 번복 0** · **백본 3종 268차 zero drift** | ROADMAP·REQUIREMENTS·USER_STORIES |
| **잔여 P0/P3** | **origin/test push(493 BE+141 FE)** → **QA-B116 post-merge** → **QA-B95 operation 승격** · **P3 carry** G-MENU-PERMISSION-MATRIX · G-STAFF-DOCUMENT mobile upload · G30 자가진단↔현장 점수 비교 · G-COMM-CALLER-AUTH(6/23) · G-ORAL-CARE-PERIOD-REPORT | ROADMAP v2·v3 |

**coder/ops 다음 액션 (184차)**: ① **origin/test push**(493 BE+141 FE) ② **QA-B116 post-merge 재확인** ③ **QA-B95** operation 승격.

> **183차→184차 delta**: merge gate 623→**634** · FE develop `@a8ccb04`→**`fd15a2f`**(1932→**1955/1955**·SYNCED) · BE develop `@49a1721`→**`b583c11`**(1706→**1739/1739**·SYNCED) · **QA-B212/B213/B214 Open→Planned(Fixed)** · **G-STAFF-DOCUMENT-REPOSITORY P3→✅ closure** · **G-BATHING P2 partial→✅ full-stack carry** · **신규 G-MENU-PERMISSION-MATRIX P3** · **cross-stream BLOCK(BE)→SYNCED** · origin/test push **488+135→493+141** · FE test 429→**431**.

### [BNK] BNK-470~471 인사이트 (2026-06-21) — ★ G-STAFF-DOCUMENT-REPOSITORY full-stack · ★ G-MENU-PERMISSION-MATRIX P3 · ★ 4축 번복 0

| BNK | 인사이트 | planner 반영 |
|-----|----------|-------------|
| **BNK-470** | **G-STAFF-DOCUMENT-REPOSITORY FE panel** @ `03d0d43` — `StaffDocumentRepositoryPanel` 21-slot·FAQ21825 lifecycle config | ROADMAP v1.2.1 · REQUIREMENTS G-STAFF-DOCUMENT-REPOSITORY · US-R03c |
| **BNK-471** | **G-STAFF-DOCUMENT-REPOSITORY full-stack closure** @ `fd15a2f`/`b583c11` — repository-progress API wire + BE RBAC · 케어포 p.96 20-doc superset · **470차 P3 candidate 제거** | ROADMAP·REQUIREMENTS·USER_STORIES ✅ |
| **BNK-471** | **신규 G-MENU-PERMISSION-MATRIX P3「가정」** — FAQ21695 계정×메뉴 fine-grained permission · ogada 7-role JWT only · v3 enterprise · MVP out-of-scope | ROADMAP v3 · REQUIREMENTS · PLAN_NOTES `### 추가 질문` |
| **BNK-471** | **G30 carry** — FAQ21692 자가진단↔현장 점수 비교 페이지 · MVP out-of-scope | PLAN_NOTES `### 추가 질문` |
| **BNK-471** | **ezCare home banner DRIFT** — 무료→추천 promo pivot · 마케팅 only · ogada impact 0 | carry only |
| **BNK-470~471** | **4축 가정 번복 0** · 백본 3종 268차 zero drift · 신규 core 갭 0 | PLAN_NOTES carry |

### [PLN] QA 피드백 반영 (2026-06-21, 183차 — BNK-464~465 · TSR 1214~1215차 · QA-B204 Open→Planned · QA Open 0 · ★ QA-B195~B205 Fixed carry · ★ G15-KAKAO-QUOTA-DASH △→✅ closure · ★ G-BATHING BE API △→✅ partial · QA-B116 Planned · QA-B95 Planned carry)

| 항목 | 내용 | 반영 문서 |
|------|------|-----------|
| **git baseline** | FE develop/test `@a8ccb04` · `test..develop` **0/0 SYNCED** · WT **CLEAN** · **1932/1932 PASS** · BE develop `@49a1721`/test `@0c9518a` · `test..develop` **0/1**(merge pending 1 · **QA-B204 Planned**) · WT **CLEAN** · **1706/1706 PASS** · merge gate **623**(FE135+BE488) · origin/test push **488 BE+135 FE** · live E2E **126 PASS/19 SKIP** · **108 route·87 page·V1–V166** · **BE Test 232** · **FE test 429** | ROADMAP CURRENT BASELINE |
| **QA-B204 Planned** | BE develop→test merge pending 1 @ `49a1721`(G-BATHING copy-from-previous-month API) · TSR 1214차 Open → PLN 183차 Planned · **이관 규율 6·7·기능 갭 아님** | QA_FEEDBACK Open→Planned · ROADMAP P0-1 |
| **QA-B195~B205 Fixed carry** | G-BILLING·live-e2e·G21 dashboard·G15 Kakao quota·DashboardPage test stabilize merges @ `cb3fe3d`~`a8ccb04` | QA_FEEDBACK Fixed carry |
| **BNK-464~465** | **★ G15-KAKAO-QUOTA-DASH △→✅ closure** @ `580a86b`(HQ dashboard widget·ogada exclusive vs 3사) · **P3 candidate 제거** · **★ G-BATHING copy-from-previous-month BE API △→✅ partial** @ `49a1721` · **FE wire P2 backlog** · **★ 4축 교차검증 가정 번복 0** · **★ longterm 502/503 session gate(on-disk carry)** · **백본 4종 263차 zero drift** | ROADMAP·REQUIREMENTS·USER_STORIES |
| **잔여 P0/P2/P3** | **tester BE merge(1) QA-B204** → **origin/test push(488 BE+135 FE)** → **QA-B116 post-merge** → **QA-B95 operation 승격** · **P2 carry** G-BATHING-SCHEDULE-PREV-MONTH-COPY FE wire · **P3 carry** G-COMM-CALLER-AUTH(6/23) · G-ORAL-CARE-PERIOD-REPORT · G-LTM-DIRECT-SYNC · G-PROVIDER-CHANGE-COUNSEL · G24 총평 전용 필드 | ROADMAP v2·v3 |

**coder/ops 다음 액션 (183차)**: ① **tester BE merge(1) QA-B204** @ `49a1721` ② **origin/test push**(488 BE+135 FE) ③ **QA-B116 post-merge 재확인** ④ **QA-B95** operation 승격 ⑤ **COD P2** G-BATHING FE wire(`BathingSchedulesPage` copy-from-previous-month).

> **182차→183차 delta**: merge gate 612→**623** · FE develop `@cb3fe3d`→**`a8ccb04`**(1916/1917→**1932/1932**·SYNCED) · BE develop `@7b99313`→**`49a1721`**(1689→**1706/1706**·merge pending 1) · BE test `@375fb9d`→**`0c9518a`** · **QA-B204 Open→Planned** · **QA-B195~B196/B192 resolved carry** · **G15-KAKAO-QUOTA-DASH P3→✅ closure** · **G-BATHING P3→P2 BE partial** · **신규 core 갭 0** · FE test 425→**429** · origin/test push **482+127→488+135** · cross-stream BLOCK(FE+BE)→**BLOCK(BE only)**.

### [BNK] BNK-464~465 인사이트 (2026-06-21) — ★ G15-KAKAO-QUOTA-DASH exclusive · ★ G-BATHING BE API · ★ 4축 번복 0

| BNK | 인사이트 | planner 반영 |
|-----|----------|-------------|
| **BNK-464** | **G15-KAKAO-QUOTA-DASH HQ 위젯 closure** @ `580a86b` — 4-tone 매트릭스·LOW threshold 500·role gate · **케어포·이지케어·엔젤 map API quota ❌ = ogada exclusive** | ROADMAP v1.3-A · REQUIREMENTS G15-KAKAO-QUOTA-DASH · US-M02-d ✅ |
| **BNK-465** | **G-BATHING copy-from-previous-month BE API** @ `49a1721` — 케어포 3-3 cross-walk · ezCare FAQ21191 방문목욕 out-of-scope · **FE wire ❌ → P2** | ROADMAP v3 · US-O01 · REQUIREMENTS G-BATHING row |
| **BNK-464~465** | **4축(G14·대시보드·v1.3-C·v2 CMS) 가정 번복 0** · longterm 502/503 live session gate · 백본 4종 zero drift | PLAN_NOTES carry |

### [TWR] 289차 docs 자동 동기화 (2026-06-21, 05:36 UTC — baseline 확정·288차 반영 완료)

**상황**: 최근 288차 코드 변경 반영을 위한 문서 일괄 동기화 필수

| 문서 | 변경 사항 | 상태 |
|------|----------|------|
| **CHANGELOG.md** | meta 헤더 갱신 (`updated=2026-06-21T05:36:00Z`) · 288차 내용 확정 | ✅ |
| **FAQ.md** | meta 헤더 갱신 · Q587/Q588 신규 추가 상태 확인 | ✅ |
| **USER_MANUAL.md** | meta 헤더 갱신 · 1-3/1-5 Must 기능 체크리스트 최신화 | ✅ |
| **ADMIN_GUIDE.md** | meta 헤더 갱신 · 1-3 구현 상태 반영 | ✅ |
| **DEPLOYMENT_GUIDE.md** | meta 헤더 갱신 · 1-3 아키텍처 최신화 | ✅ |
| **PLAN_NOTES.md** | tech_writer-sync 주석 추가 · 289차 기록 작성 | ✅ |

**baseline 확정**: `BE 7b99313` (1 commit since `14935a3`) · `FE e2f1246` (3 commits since `33e9e1a`) · V1–V166 · **108 route · 87 page** · **merge gate 614**

**288차 반영 완료 항목**:
- ★ **G-BILLING appliedFilters FE wire full-stack** (`c6a412f`/`e2f1246`) — BillingReportPage · billingReportFilters.js · appliedFilters summary · FAQ Q587 closure
- ★ **UXD-148 billing report filter a11y** (`e2f1246`) — aria-busy · aria-live · dateTime · FAQ Q588
- ★ **live E2E feature-scoped operation blockers** (`cb3fe3d`) — liveConfig normalization · suite contract filtering · FAQ Q580 deepen

**다음 우선순위** (PLN 182차 align):
1. **COD QA-B195 fix** — `liveE2eSuiteGuard.test.js` regex 추가
2. **tester FE merge (QA-B196)** + **BE merge (QA-B192)**
3. **origin/test push** (482 BE + 127 FE)
4. **QA-B116 post-merge** 재검증
5. **QA-B95** operation 승격
6. **지속 P3**: 출석 roster API 확장 · QR 생성 payload·이미지 · G-CASH-RECEIPT-NTS-API

---

### [PLN] QA 피드백 반영 (2026-06-21, 182차 — BNK-456~458 · TSR 1192~1203차 · QA-B195/B196/B192 Open→Planned · QA Open 0 · ★ QA-B193/B194 Fixed · ★ G-BILLING 3건 △→✅ full-stack closure · ★ G32 FAQ21740 parity deepen · QA-B116 Planned · QA-B95 Planned carry)

| 항목 | 내용 | 반영 문서 |
|------|------|-----------|
| **QA-B195 Planned** | FE develop HEAD 1 FAIL `liveE2eSuiteGuard.test.js` — `liveCashReceiptDescribe` regex 누락 @ `cb3fe3d` · TSR 1203차 Open → PLN 182차 Planned · **COD 선행 fix** | QA_FEEDBACK Open→Planned · ROADMAP P0-1 |
| **QA-B196 Planned** | FE develop→test merge pending 1 @ `cb3fe3d`(v2/live-e2e suite gates) · blocked by QA-B195 · TSR 1203차 Open → PLN 182차 Planned · **이관 규율 6·7·기능 갭 아님** | QA_FEEDBACK Open→Planned · ROADMAP P0-2 |
| **QA-B192 Planned** | BE develop→test merge pending 2 @ `14935a3`(appliedFilters echo)+`7b99313`(receipt-basis test) · TSR 1198~1202차 Open → PLN 182차 Planned · **이관 규율 6·7·기능 갭 아님** | QA_FEEDBACK Open→Planned · ROADMAP P0-3 |
| **QA-B193 Fixed** | BE develop dirty-tree `BillingServiceTest` WIP → commit @ `7b99313` · develop WT **CLEAN** | QA_FEEDBACK Fixed carry |
| **QA-B194 Fixed** | FE merge EXECUTED @ `c6a412f`(appliedFilters FE wire) · post-merge 1913/1913 PASS | QA_FEEDBACK Fixed carry |
| **BNK-456~458** | **★ G-BILLING deposit half-month + receipt dual-basis △→✅ full-stack** @ `e38ccfd`/`375fb9d`/`b96d038` · **★ appliedFilters FE wire △→✅** @ `c6a412f`/`14935a3` · **P3 candidate 3건 제거** · **★ G32 FAQ21740 반기별 1회 parity deepen** · **★ module 8 PDF p.98–105 cross-walk**(8-3/8-6/8-8 P3 carry) | ROADMAP·REQUIREMENTS·USER_STORIES |
| **잔여 P0/P3** | **COD QA-B195 fix** → **tester FE merge(1) QA-B196** → **tester BE merge(2) QA-B192** → **origin/test push(482 BE+127 FE)** → **QA-B116 post-merge** → **QA-B95 operation 승격** · **P3 carry** G-COMM-CALLER-AUTH(6/23 마감) · G-BATHING-SCHEDULE-PREV-MONTH-COPY · G-ORAL-CARE-PERIOD-REPORT · G15-KAKAO-QUOTA-DASH · G-LTM-DIRECT-SYNC · G-PROVIDER-CHANGE-COUNSEL · G24 총평 전용 필드 · module 8 PDF workflow | ROADMAP v2·v3 |

**coder/ops 다음 액션 (182차)**: ① **COD QA-B195 fix** — `liveE2eSuiteGuard.test.js` regex에 `liveCashReceiptDescribe` 추가 @ `cb3fe3d` ② **tester FE merge(1) QA-B196** ③ **tester BE merge(2) QA-B192** ④ **origin/test push**(482 BE+127 FE) ⑤ **QA-B116 post-merge 재확인** ⑥ **QA-B95** operation 승격.

> **181차→182차 delta**: merge gate 602→**612** · FE develop `@2581347`→**`cb3fe3d`**(1901→**1916/1917**·merge pending 1+regression) · FE test `@82a542c`→**`c6a412f`** · BE develop `@1d7cee2`→**`7b99313`**(1673→**1689/1689**·merge pending 2) · BE test `@2edbdc4`→**`375fb9d`** · **QA-B195/B196/B192 Open→Planned** · **QA-B193/B194 Fixed carry** · **G-BILLING 3건 P3 candidate→✅ full-stack closure(제거)** · **G32 FAQ21740 parity deepen** · **신규 core 갭 0** · BE Test 230→**232** · FE test 424→**425** · origin/test push **478+120→482+127**.

### [BNK] BNK-456~458 인사이트 (2026-06-21) — ★ G-BILLING 3건 full-stack closure · ★ G32 FAQ21740 parity deepen · ★ module 7 11/11 + module 8 PDF cross-walk

| BNK | 인사이트 | planner 반영 |
|-----|----------|-------------|
| **BNK-455~456** | **G-BILLING deposit half-month + receipt dual-basis ✅ full-stack** @ `e38ccfd`/`375fb9d`/`b96d038` · BE appliedFilters API echo @ `14935a3` | ROADMAP·REQUIREMENTS·USER_STORIES — **P3 `G-BILLING-DEPOSIT-HALFMONTH-REPORT`·`G-BILLING-RECEIPT-DUAL-BASIS` 제거** |
| **BNK-457** | **G-BILLING appliedFilters FE wire ✅ full-stack** @ `c6a412f`/`14935a3` · `billingReportFilters.js` server label 우선 · **P3 `G-BILLING-APPLIED-FILTERS-WIRE` 제거** · module 7 11-leaf Route 1:1 · module 8 PDF p.98–105 8-leaf cross-walk(8-3/8-6/8-8 P3 carry) | ROADMAP v1.2.1 · REQUIREMENTS §1-5 |
| **BNK-458** | **FAQ21740 사례관리회의록 반기별 1회 ↔ G32 ✅ parity deepen** · FAQ21730 2025 수가표 PNG out-of-scope · 가격·도입 256~258차 verbatim 불변 | ROADMAP·REQUIREMENTS G32 row · PLAN_NOTES |

### [PLN] QA 피드백 반영 (2026-06-21, 181차 — BNK-447~452 · TSR 1184~1191차 · QA-B187/B188 Open→Planned · QA Open 0 · ★ QA-B186 Fixed · ★ G-STAFF-LEAVE-STATUS △→✅ full-stack closure · ★ 4축 가정 번복 0 · ★ 신규 candidate G-COMM-CALLER-AUTH P3 · QA-B116 Planned · QA-B95 Planned carry)

| 항목 | 내용 | 반영 문서 |
|------|------|-----------|
| **git baseline** | FE develop `@2581347`/test `@82a542c` · `test..develop` **0/2**(merge pending 2 · **QA-B188 Planned**) · WT **CLEAN** · **1901/1901 PASS** · build **1079 modules** · BE develop `@1d7cee2`/test `@2edbdc4` · `test..develop` **0/2**(merge pending 2 · **QA-B187 Planned**) · WT **CLEAN** · **1673/1673 PASS** · merge gate **602**(FE122+BE480) · origin/test push **478 BE+120 FE** · live E2E **126 PASS/19 SKIP** · **108 route·87 page·V1–V166** · **BE Test 230** · **FE test 424** | ROADMAP CURRENT BASELINE |
| **QA-B188 Planned** | FE develop→test merge pending 2 @ `2581347`(G-STAFF-LEAVE-STATUS ON_LEAVE FE wire)+`e45df26`(live-e2e token probe) · TSR 1189~1191차 Open → PLN 181차 Planned · **이관 규율 6·7·기능 갭 아님** | QA_FEEDBACK Open→Planned · ROADMAP P0 |
| **QA-B187 Planned** | BE develop→test merge pending 2 @ `1d7cee2`(lifecycle summary API `onLeaveCount`)+`68d4457`(ON_LEAVE enum+V166) · TSR 1188~1190차 Open → PLN 181차 Planned · **이관 규율 6·7·기능 갭 아님** | QA_FEEDBACK Open→Planned · ROADMAP P0 |
| **QA-B186 Fixed** | FE merge EXECUTED @ `82a542c`(live-e2e placeholder auth token bootstrap probing) · TSR 1187차 | QA_FEEDBACK Fixed · ROADMAP v2 |
| **BNK-447~452** | **★ G-STAFF-LEAVE-STATUS △→✅ full-stack closure** @ `2581347`/`1d7cee2`(V166·`STAFF_LIFECYCLE_STATUS.ON_LEAVE`·`StaffLifecyclePanel` 휴직 Badge·`StaffLifecycleSummaryPanel`+`GET /api/v1/staff/lifecycle-summary` `onLeaveCount`·복직 regression — **P3 candidate 제거**) · **★ 4축 교차검증(G14·대시보드/G26·v1.3-C·v2 CMS) 가정 번복 0**(P0/P1 재정렬 없음) · **★ 신규 candidate G-COMM-CALLER-AUTH P3「가정」**(silverangel notice 221562 발신번호 본인인증 마감 6/23·MVP out-of-scope) · **★ G-BANK-EXCEL-8 BE row guard ✅+**(BNK-448) · **★ 백본 6종 zero drift 254차** · **★ longterm 502/503 5th cycle stable** · **신규 core 갭 0** | ROADMAP·REQUIREMENTS·USER_STORIES |
| **QA-B116 Planned** | origin/test push **478 BE+120 FE** · push 후 post-merge 재검증 | ROADMAP P0 |
| **QA-B95 Planned** | operation BLOCK · `./scripts/run-live-e2e.sh` full criteria 미충족 carry(19 SKIP) | ROADMAP P0 |
| **잔여 P0/P3** | **tester FE merge(2) QA-B188 + BE merge(2) QA-B187** → **origin/test push(478 BE+120 FE)** → **QA-B116 post-merge** → **QA-B95 operation 승격** · **P3 carry** G-COMM-CALLER-AUTH(신규·6/23 마감) · G-BILLING-DEPOSIT-HALFMONTH-REPORT · G-BILLING-RECEIPT-DUAL-BASIS · G-BATHING-SCHEDULE-PREV-MONTH-COPY · G-ORAL-CARE-PERIOD-REPORT · G15-KAKAO-QUOTA-DASH · G-LTM-DIRECT-SYNC · G-PROVIDER-CHANGE-COUNSEL · G24 총평 전용 필드 | ROADMAP v2·v3 |

**coder/ops 다음 액션 (181차)**: ① **tester FE merge(2) QA-B188** @ `2581347`+`e45df26` ② **tester BE merge(2) QA-B187** @ `1d7cee2`+`68d4457` ③ **origin/test push**(478 BE+120 FE) ④ **QA-B116 post-merge 재확인** ⑤ **QA-B95** operation 승격.

> **180차→181차 delta**: merge gate 590→**602** · FE develop `@a18b30e`(SYNCED)→**`2581347`**(1885→**1901/1901**·merge pending 2) · FE test `@a18b30e`→**`82a542c`** · BE develop `@7d29a38`→**`1d7cee2`**(1670→**1673/1673**·merge pending 2) · BE test `@e3b74a0`→**`2edbdc4`** · cross-stream BLOCK(BE)→**BLOCK(FE+BE)** · **QA-B187/B188 Open→Planned** · **QA-B186 Fixed** · **G-STAFF-LEAVE-STATUS P3 candidate→✅ full-stack closure(제거)** · **신규 candidate G-COMM-CALLER-AUTH P3** · **신규 core 갭 0** · live E2E 145 SKIP→**126 PASS/19 SKIP** · BE Test 228→**230** · FE test 422→**424** · V165→**V166**.

### [BNK] BNK-447~452 인사이트 (2026-06-21) — ★ G-STAFF-LEAVE-STATUS △→✅ full-stack · ★ 4축 가정 번복 0 · ★ 신규 candidate G-COMM-CALLER-AUTH P3 · ★ 백본 6종 zero drift

| BNK | 핵심 | 기획 반영 |
|-----|------|-----------|
| **BNK-452** | **★ G-STAFF-LEAVE-STATUS △→✅ full-stack closure**(V166·`ON_LEAVE` enum·`onLeaveCount` summary API·휴직 Badge·복직 regression) · **★ 4축 교차검증 가정 번복 0**(G14·대시보드/G26·v1.3-C·v2 CMS baseline 안정·P0/P1 재정렬 없음) · **★ 신규 evidence silverangel notice 221562**(미인증 발신번호 본인인증 마감 2026-06-23 17:00·삭제 18:00·`부가서비스>문자발신번호관리`) → **G-COMM-CALLER-AUTH P3「가정」** · ezCare 254차 cachebuster DRIFT·엑셀 포맷 변경 0 | ROADMAP v2·v3 · REQUIREMENTS §1-5 · US-R03b ✅ · PLAN_NOTES `### 추가 질문` |
| **BNK-448~451** | **★ G-BANK-EXCEL-8 BE row guard ✅+**(BNK-448 `@6ed7cd4` non-positive row guard) · **★ longterm 610 server-side session gate 「확인」**(BNK-448·MVP out-of-scope) · **★ longterm 502/503 oscillating `var s16` 3rd cycle close → 5th cycle stable**(BNK-448·452) · **★ silverangel 5월 공지 3종**(발신번호 본인인증·기관운영 cycle gate·건강관리기록부 daily·BNK-451) · **★ ON_LEAVE BE enum closure**(BNK-451 `@68d4457`) · 백본 6종 zero drift 251~254차 | ROADMAP v1.2.1 · REQUIREMENTS §1-5 · carry |

### [PLN] QA 피드백 반영 (2026-06-21, 180차 — BNK-445~446 · TSR 1177~1179차 · QA-B182 Open→Planned · QA Open 0 · ★ QA-B181 Fixed · ★ G-BANK-EXCEL-8 ✅ · ★ G-STAFF-NHIS ✅ full-stack · QA-B116 Planned · QA-B95 Planned carry)

| 항목 | 내용 | 반영 문서 |
|------|------|-----------|
| **git baseline** | FE develop/test `@a18b30e` · `test..develop` **0/0 SYNCED** · WT **CLEAN** · **1885/1885 PASS** · BE develop `@7d29a38`/test `@e3b74a0` · `test..develop` **0/1** · WT **CLEAN** · **1670/1670 PASS** · merge gate **590**(FE115+BE475) · origin/test push **475 BE+115 FE** · live E2E **145 SKIP/0 PASS** · **108 route·87 page·V1–V165** · **BE Test 228** · **FE test 422** | ROADMAP CURRENT BASELINE |
| **QA-B182 Planned** | BE develop→test merge pending 1 @ `7d29a38`(G-BANK-EXCEL-8 non-positive row selection guard) · TSR 1178~1179차 Open → PLN 180차 Planned · **이관 규율 6·7·기능 갭 아님** | QA_FEEDBACK Open→Planned · ROADMAP P0 |
| **QA-B181 Fixed** | FE merge EXECUTED @ `a18b30e`(G-BANK-EXCEL-8 `BankDepositImportPanel` FE wire) · TSR 1179차 | QA_FEEDBACK Fixed · ROADMAP v2 |
| **BNK-445~446** | **★ G-BANK-EXCEL-8 ✅ full-stack closure** @ `a18b30e`/`e3b74a0`+BE `@7d29a38`(pending merge) · **★ G-STAFF-NHIS-EXCEL-IMPORT ✅ full-stack** @ `4315ee2`/`2f6f3bc` · **★ 케어포 7-x 10/10 재입증** · **★ 신규 P3 G-BILLING-DEPOSIT-HALFMONTH-REPORT**(PDF p.91 반월 split) · **★ G-BILLING-RECEIPT-DUAL-BASIS P3 carry** · **★ ezCare FAQ21720 G-STAFF-LEAVE-STATUS P3「가정」**(휴직 LEAVE enum·신규 갭 1) · **★ FAQ21708 HR/payroll out-of-scope** 재확인 · **신규 갭 1** | ROADMAP·REQUIREMENTS·USER_STORIES |
| **QA-B116 Planned** | origin/test push **475 BE+115 FE** · push 후 post-merge 재검증 | ROADMAP P0 |
| **QA-B95 Planned** | operation BLOCK · live E2E staff-bootstrap-not-ready · `./scripts/run-live-e2e.sh` full criteria 미충족 carry | ROADMAP P0 |
| **잔여 P0/P3** | **tester BE merge(1) QA-B182** → **origin/test push(475 BE+115 FE)** → **QA-B116 post-merge** → **QA-B95 operation 승격** · **P3 carry** G-STAFF-LEAVE-STATUS · G-BILLING-DEPOSIT-HALFMONTH-REPORT · G-BILLING-RECEIPT-DUAL-BASIS · G15-KAKAO-QUOTA-DASH · G-BATHING-SCHEDULE-PREV-MONTH-COPY · G-ORAL-CARE-PERIOD-REPORT · G-LTM-DIRECT-SYNC · G-PROVIDER-CHANGE-COUNSEL · G24 총평 전용 필드 | ROADMAP v2·v3 |

**coder/ops 다음 액션 (180차)**: ① **tester BE merge(1) QA-B182** @ `7d29a38` ② **origin/test push**(475 BE+115 FE) ③ **QA-B116 post-merge 재확인** ④ **QA-B95** operation 승격.

> **179차→180차 delta**: merge gate 581→**590** · FE develop `@a0f051d`→**`a18b30e`**(1878→**1885/1885**·SYNCED) · BE develop `@6f7f145`→**`7d29a38`** · BE test `@07a85a3`→**`e3b74a0`** · **QA-B182 Open→Planned** · **QA-B181 Fixed** · **G-BANK-EXCEL-8 P2 FE wire→✅ full-stack closure** · **G-STAFF-NHIS-EXCEL-IMPORT △→✅ full-stack** · **신규 P3 +3**(G-STAFF-LEAVE-STATUS·G-BILLING-DEPOSIT-HALFMONTH-REPORT·G-BILLING-RECEIPT-DUAL-BASIS carry) · **신규 갭 0→1**(휴직 LEAVE enum) · live E2E 126/19→**145 SKIP/0 PASS** · BE Test 227→**228** · FE test 421→**422** · V164→**V165**.

### [BNK] BNK-445~446 인사이트 (2026-06-21) — ★ G-BANK ✅ full-stack · ★ G-STAFF-NHIS ✅ · ★ carefor 7-x · ★ ezCare FAQ21720 휴직 갭

| BNK | 핵심 | 기획 반영 |
|-----|------|-----------|
| **BNK-445** | **케어포 7-x 10/10 재입증** · **★ 신규 P3 G-BILLING-DEPOSIT-HALFMONTH-REPORT**(PDF p.91 1~15일/16~말일) · **G-BILLING-RECEIPT-DUAL-BASIS P3 carry** · func 228차 zero drift | ROADMAP v1.2.1 · REQUIREMENTS §1-5 |
| **BNK-446** | **★ G-BANK-EXCEL-8 ✅** @ `a18b30e`/`e3b74a0`+`7d29a38` · **★ FAQ21720 G-STAFF-LEAVE-STATUS P3「가정」** — ON_LEAVE enum 갭 · **FAQ21708 HR out-of-scope** · FAQ trinity 249차 zero drift | US-R03 · ROADMAP v2·v3 |

### [PLN] QA 피드백 반영 (2026-06-20, 179차 — BNK-435~441 · TSR 1165~1167차 · QA-B178 Open→Planned · QA Open 0 · ★ QA-B177 Fixed · ★ G-BILLING-PRIOR-DEPOSIT-GUARD ✅ · ★ G-BANK/G-STAFF-NHIS △ BE partial · QA-B116 Planned · QA-B95 Planned carry)

| 항목 | 내용 | 반영 문서 |
|------|------|-----------|
| **git baseline** | FE develop/test `@a0f051d` · `test..develop` **0/0 SYNCED** · WT **CLEAN** · **1878/1878 PASS** · BE develop `@6f7f145`/test `@07a85a3` · `test..develop` **0/1** · WT **CLEAN** · **1651/1651 PASS** · merge gate **581**(FE111+BE470) · origin/test push **469 BE+111 FE** · live E2E **126 PASS/19 SKIP** · **108 route·87 page·V1–V164** · **BE Test 227** · **FE test 421** | ROADMAP CURRENT BASELINE |
| **QA-B178 Planned** | BE develop→test merge pending 1 @ `6f7f145`(G-BANK-EXCEL-8 preview parser guard) · TSR 1166~1167차 Open → PLN 179차 Planned · **이관 규율 6·7·기능 갭 아님** | QA_FEEDBACK Open→Planned · ROADMAP P0 |
| **QA-B177 Fixed** | FE merge EXECUTED @ `a0f051d`(L02_M15 CareServiceSpecialNotesPage test stabilization + live-e2e skip diagnostics) · TSR 1167차 | QA_FEEDBACK Fixed · ROADMAP v1.2.1 |
| **BNK-435~441** | **★ G-BILLING-PRIOR-DEPOSIT-GUARD ✅ closure carry**(BNK-436 dashboard widget+API) · **★ G-BANK-EXCEL-8 △ BE partial** @ `07a85a3`/`6f7f145`(8-bank catalog+preview+import·FE wire ❌) · **★ G-STAFF-NHIS-EXCEL-IMPORT △ BE partial** @ `6f7f145`(NHIS caregiver excel preview+import·FE wire ❌) · **★ BNK-441 module3 PDF workflow** — func 107-leaf·demo nav 0·7-x 10/10·리포트 15.0% · **★ 신규 candidate G-BATHING-SCHEDULE-PREV-MONTH-COPY·G-ORAL-CARE-PERIOD-REPORT P3** · **신규 갭 0** | ROADMAP·REQUIREMENTS·USER_STORIES |
| **QA-B116 Planned** | origin/test push **469 BE+111 FE** · push 후 post-merge 재검증 | ROADMAP P0 |
| **QA-B95 Planned** | operation BLOCK · `./scripts/run-live-e2e.sh` full criteria 미충족 carry | ROADMAP P0 |
| **잔여 P0/P2/P3** | **tester BE merge(1) QA-B178** → **origin/test push(469 BE+111 FE)** → **QA-B116 post-merge** → **QA-B95 operation 승격** · **P2 carry** G-BANK-EXCEL-8 FE wire · G-STAFF-NHIS-EXCEL-IMPORT FE wire · G15-KAKAO-QUOTA-DASH · **P3 carry** G-BATHING-SCHEDULE-PREV-MONTH-COPY · G-ORAL-CARE-PERIOD-REPORT · G-LTM-DIRECT-SYNC · G-PROVIDER-CHANGE-COUNSEL · G24 총평 전용 필드 | ROADMAP v1.2.1·v2·v3 |

**coder/ops 다음 액션 (179차)**: ① **tester BE merge(1) QA-B178** @ `6f7f145` ② **origin/test push**(469 BE+111 FE) ③ **QA-B116 post-merge 재확인** ④ **QA-B95** operation 승격.

> **178차→179차 delta**: merge gate 569→**581** · FE develop `@d723d5a`→**`a0f051d`**(1878/1878·SYNCED) · BE develop `@80b9619` SYNCED→**`6f7f145` merge pending 1** · cross-stream SYNCED→**BLOCK(BE)** · **QA-B178 Open→Planned** · **QA-B177 Fixed** · **G-BILLING-PRIOR-DEPOSIT-GUARD P2→✅ closure** · **G-BANK-EXCEL-8 P3→△ BE partial(P2 FE wire)** · **신규 G-STAFF-NHIS-EXCEL-IMPORT △ BE** · **신규 candidate +2**(G-BATHING-SCHEDULE-PREV-MONTH-COPY·G-ORAL-CARE-PERIOD-REPORT) · live E2E 122/23→**126/19** · page 86→**87** · BE Test 224→**227** · FE test 419→**421**.

### [BNK] BNK-435~441 인사이트 (2026-06-20) — ★ G-BILLING-PRIOR-DEPOSIT-GUARD ✅ · ★ G-BANK/G-STAFF-NHIS △ BE partial · ★ module3 PDF workflow · ★ func 107-leaf 정본

| BNK | 핵심 | 기획 반영 |
|-----|------|-----------|
| **BNK-441** | func.php **107-leaf 정본**·demo 시설 셸 nav 0·PDF p.4+p.45 module3 workflow(3-1~3-6·구강 1/2/3개월) · 7-x **10/10** ↔ ogada 18 `/billing/*` · 리포트 밀도 **15.0%** | ROADMAP v1.2.1 · REQUIREMENTS §1-5 |
| **BNK-440** | **G-STAFF-NHIS-EXCEL-IMPORT △ BE** @ `6f7f145` · **G-BANK-EXCEL-8 △ BE** @ `07a85a3`/`6f7f145` · FE wire ❌ → **P2 carry** | US-R03 · US-L01 · ROADMAP v2 |
| **BNK-436~439** | **G-BILLING-PRIOR-DEPOSIT-GUARD ✅ full-stack** · silverangel notice 221547 · FAQ21812 관리자 라운딩 P3 carry | ROADMAP v1.2.1 · carry |
| **BNK-435** | LCMS evaluation.do 404 · silverangel 지표27 이중 정의 · **주야간 목욕 △ optional billing** | carry · 신규 갭 0 |

### [PLN] QA 피드백 반영 (2026-06-20, 178차 — BNK-432~434 · TSR 1154~1155차 · QA-B169~B172 Fixed · QA Open 0 · ★ G14 plan-form closure · ★ G24 FAQ21800 parity · QA-B116 Planned · QA-B95 Planned carry)

| 항목 | 내용 | 반영 문서 |
|------|------|-----------|
| **git baseline** | FE develop/test `@d723d5a` · `test..develop` **0/0 SYNCED** · WT **CLEAN** · **1866/1866 PASS** · BE develop/test `@80b9619` · `test..develop` **0/0 SYNCED** · WT **CLEAN** · **1640/1640 PASS** · merge gate **569**(FE105+BE464) · origin/test push **464 BE+105 FE** · live E2E **122 PASS/23 SKIP** · **108 route·86 page·V1–V164** · **BE Test 224** · **FE test 419** | ROADMAP CURRENT BASELINE |
| **QA-B171 Fixed** | BE merge EXECUTED @ `80b9619`(V164 G14 care plan API + V163 regions seed purge + live-e2e guardian fallback) · TSR 1154차 | QA_FEEDBACK Fixed · ROADMAP v1.2.1 |
| **QA-B172 Fixed** | FE merge EXECUTED @ `d723d5a`(G14 care plan UI + branch switcher/tokens) · TSR 1155차 | QA_FEEDBACK Fixed · ROADMAP v1.2.1 |
| **QA-B169/B170 Fixed carry** | QA-B169 @ `3023c9e`(Kakao quota tracker BE) · QA-B170 @ `c37228d`(KakaoTransportMap post-merge FAIL) · TSR 1144~1149차 | QA_FEEDBACK Fixed |
| **BNK-432~434** | **★ G14 plan-form △→✅ closure** — V164·`ClientCarePlanFormService`·10 NHIS fields·Route `/clients/:clientId/care-plan-form` @ `34eb47a`/`ce422e3`/`d723d5a` · FAQ21802 cross-walk ✅ · **★ G24 FAQ21800 8/8 parity ✅** + fiscal year compliance · 총평 전용 필드 △(`homeVisitNotes`) → **P3 carry** · **★ v2 infra** V161~V163 closure · **★ 신규 candidate G-BILLING-PRIOR-DEPOSIT-GUARD P2**(carefor p.85) · **★ G-BANK-EXCEL-8 P3**(PDF p.88) · **신규 갭 0** | ROADMAP·REQUIREMENTS·USER_STORIES |
| **QA-B116 Planned** | origin/test push **464 BE+105 FE** · push 후 post-merge 재검증 | ROADMAP P0 |
| **QA-B95 Planned** | operation BLOCK · `./scripts/run-live-e2e.sh` full criteria 미충족 carry | ROADMAP P0 |
| **잔여 P0/P2/P3** | **tester origin/test push(464 BE+105 FE)** → **QA-B116 post-merge** → **QA-B95 operation 승격** · **P2 carry** G-BILLING-PRIOR-DEPOSIT-GUARD · G15-KAKAO-QUOTA-DASH · **P3 carry** G-BANK-EXCEL-8 · G-LTM-DIRECT-SYNC · G-PROVIDER-CHANGE-COUNSEL · G24 총평 전용 필드 | ROADMAP v1.2.1·v2·v3 |

**coder/ops 다음 액션 (178차)**: ① **tester origin/test push**(464 BE+105 FE) ② **QA-B116 post-merge 재확인** ③ **QA-B95** operation 승격(live E2E env·full criteria).

> **177차→178차 delta**: merge gate 555→**569** · cross-stream BLOCK→**SYNCED** · **QA-B169/B170/B171/B172 Planned/Open→Fixed** · **G14 plan-form P2 △→✅ closure(V164)** · **G24 FAQ21800 parity ✅** · **신규 candidate +2**(G-BILLING-PRIOR-DEPOSIT-GUARD·G-BANK-EXCEL-8) · live E2E 126/19→**122/23** · route 107→**108** · V159→**V164**.

### [BNK] BNK-432~434 인사이트 (2026-06-20) — ★ G14 plan-form full-stack closure(V164·FAQ21802) · ★ G24 FAQ21800 8-item parity · ★ v2 V161~V163 infra closure · ★ carefor PDF p.86~88 billing/deposit evidence · 신규 candidate G-BILLING-PRIOR-DEPOSIT-GUARD·G-BANK-EXCEL-8

| BNK | 핵심 | 기획 반영 |
|-----|------|-----------|
| **BNK-433** | G14 **△→✅** — BE `ClientCarePlanFormService`·V164·10 NHIS fields @ `34eb47a`/`80b9619` · FE `ClientCarePlanFormPage`·Route `/clients/:clientId/care-plan-form` @ `ce422e3`/`d723d5a` · FAQ21802 cross-walk ✅ · **신규 갭 0** | ROADMAP v1.2.1 · US-T08b · REQUIREMENTS G14-NHIS-PLAN-FORM |
| **BNK-434** | G24/G24b **FAQ21800 8/8 parity ✅** · fiscal year compliance ✅ · 총평(종합소견) 전용 필드 △ via `homeVisitNotes` → **P3 carry** | US-T09 · REQUIREMENTS G24 |
| **BNK-432** | v2 infra — V161 HQ admin single·V162 user account requests·V163 Korean legal districts seed @ `80b9619` | ROADMAP v2 |

### [PLN] QA 피드백 반영 (2026-06-20, 177차 — BNK-424~429 · TSR 1137~1143차 · QA-B169/B170 Open→Planned · QA Open 0 · ★ G15-KAKAO-INTEGRATION 6-layer · ★ QA-B163/B167 Fixed · QA-B116 Planned · QA-B95 Planned carry)

| 항목 | 내용 | 반영 문서 |
|------|------|-----------|
| **git baseline** | FE develop `@ba74bb5`/test `@acc5933` · `test..develop` **0/1** · FE develop WT **CLEAN** · FE develop **1856/1856 PASS** · FE test post-merge **1847/1852 PASS**(5 FAIL) · BE develop `@e2b764b`/test `@48eea95` · `test..develop` **0/1** · BE develop WT **DIRTY 9M+4U** · BE test **1615/1615 PASS** · BE develop **1621/1621 PASS** · merge gate **555**(FE98+BE457) · origin/test push **456 BE+97 FE** · live E2E **126 PASS/19 SKIP**(carry) · **107 route·86 page·V1–V159** · **BE Test 221** · **FE test 416** | ROADMAP CURRENT BASELINE |
| **QA-B169 Planned** | BE develop WT **DIRTY 9M+4U** — Kakao API status/quota tracker WIP(`KakaoRestApiUsageTracker`·`TransportKakaoQuotaUsageResponse` 등) · merge pending **1** @ `e2b764b` · TSR 1139~1143차 Open → PLN 177차 Planned · **이관 규율 5·6·7·기능 갭 아님** | QA_FEEDBACK Open→Planned · ROADMAP P0 |
| **QA-B170 Planned** | FE test post-merge `@acc5933` **5 FAIL**(`KakaoTransportMap` import 4 + `CareNursingServiceReportPage` 1) · develop `@ba74bb5` **1856/1856 PASS**·fix committed · TSR 1141~1143차 Open → PLN 177차 Planned · **이관 규율 5·6·7·기능 갭 아님** | QA_FEEDBACK Open→Planned · ROADMAP P0 |
| **QA-B163/B167 Fixed** | QA-B163 Fixed @ `94f2535`(panel test) · QA-B167 Fixed @ `ba74bb5`(Kakao map WIP commit + `TransportKakaoApiStatusPanel`) · QA-B168 Fixed @ `acc5933`(`pilotPageFlows`) | QA_FEEDBACK Fixed |
| **BNK-424~429** | **★ G15-KAKAO-INTEGRATION 6-layer 우위**(케어포 postcode 1-layer only·BNK-429) · **★ TransportKakaoApiStatusPanel** FE @ `ba74bb5` · **★ Kakao quota tracker** BE WIP(4U untracked) · **★ 신규 candidate G15-KAKAO-QUOTA-DASH P3「가정」** · **★ FAQ21832 HR payroll out-of-scope** · func.php module 2 cross-walk ✅5·✅+3·△4·❌0 · **신규 갭 0** | ROADMAP·REQUIREMENTS·USER_STORIES |
| **QA-B116 Planned** | origin/test push **456 BE+97 FE** · push 후 post-merge 재검증 | ROADMAP P0 |
| **QA-B95 Planned** | operation BLOCK · `./scripts/run-live-e2e.sh` full criteria 미충족 carry | ROADMAP P0 |
| **잔여 P0/P2/P3** | **COD QA-B169 BE commit** → **COD QA-B170 verify** → **tester FE+BE merge(1 each)** → **origin/test push(456 BE+97 FE)** → **QA-B116 post-merge** → **QA-B95 operation 승격** · **P3 carry** G15-KAKAO-QUOTA-DASH · G-CASH-RECEIPT-NTS-API · G-PROVIDER-CHANGE-COUNSEL | ROADMAP v1.3-A·v2 |

**coder/ops 다음 액션 (177차)**: ① **COD QA-B169** — BE Kakao quota tracker WIP commit(9M+4U) → WT **CLEAN** ② **COD QA-B170** — develop `@ba74bb5` fix verified → tester FE merge(1) ③ **tester BE merge(1)** @ `e2b764b` ④ **origin/test push**(456 BE+97 FE) ⑤ **QA-B116 post-merge 재확인** ⑥ **QA-B95** operation 승격.

> **176차→177차 delta**: merge gate 543→**555** · FE develop `@16afd4c`→**`ba74bb5`**(WT CLEAN·1856/1856 PASS) · BE develop `@bfad37d` SYNCED→**`e2b764b` WT DIRTY 9M+4U** · QA-B163 Planned→**Fixed @ `94f2535`** · **QA-B169/B170 Open→Planned** · **G15-KAKAO-INTEGRATION 5-layer→6-layer deepen** · **신규 candidate G15-KAKAO-QUOTA-DASH P3** · cross-stream BLOCK(FE only)→**FE+BE**.

### [BNK] BNK-448 인사이트 (2026-06-20) — ★★★ longterm 610 carry-미확인(BNK-371~447 ~80 cycle) → 「확인」 server-side session gate · ★★ longterm 502/503 oscillating `var s16` 3rd cycle 반전 · ★ G-BANK-EXCEL-8 BE row guard deepen + UXD-146 a11y deepen(merge 594) · ★ 백본 6종 zero drift 251차 · ★ 2026 고시 2종 DRIFT verbatim 불변 · ★ 4축 교차검증 가정 번복 0

| BNK | 핵심 | planner 반영 |
|-----|------|-------------|
| **BNK-448** | **★★★ longterm 610 carry-미확인 → 「확인」 server-side session gate** — [longterm 610](https://www.longtermcare.or.kr/npbs/e/b/610/npeb610m01.web?menuId=npe0000003237) HTTP **200·422B·`d3c90b33`** literal `refreshedException` 본문(공단 anti-bot/session gate·ezCare `/new.ez` 70B stub과 동일 패턴)·on-disk md5 IDENTICAL·**미확인 -1**(서버가 literal 텍스트 반환·추측→확인 승격 NOT)·BNK-371~447 ~80 cycle carry resolved·MVP out-of-scope · **★★ longterm 502/503 oscillating `var s16` 3rd cycle 반전** — BNK-431 `b5aee8c1`(no s16) → BNK-447 `72148cfe`(+s16·+9B) → **BNK-448 `b5aee8c1`(no s16·-9B 반전)**·503은 `8ca7d1fa`↔`c94cc389` 동일 binary oscillation·verbatim 단기보호 74,060/통합재가/경감 50%×4·60%×3 IDENTICAL·`grep -c "var s16"` live=0 vs on-disk(BNK-447)=1·alt 스냅샷 영구 reference 일치 · **★ G-BANK-EXCEL-8 BE row guard deepen ✅+** (`@6ed7cd4` `validateSelectedRowNumbers` parsed `ParsedBankDepositRow::rowNumber` Set 비교·BusinessRuleException 「선택한 행 번호를 엑셀에서 찾을 수 없습니다」·"silently skipping all rows" 잠재 결함 차단·BNK-447 ✅ → ✅+) + **UXD-146 a11y deepen** (`@a7d9a2f` BankDeposit/StaffNhisCaregiver preview row 컨텍스트 라벨·time semantics·aria-live polite/assertive·공용 bank-deposit-formats CSS) · **★ FE QA-B95 auth blocker 회복 fix** (`@9105332` operation-readiness staff/guardian auth ready 시 blocker 회복 가능 분류·`liveE2eHarness.test.js` regression·145 SKIP false-skip 축소 기대) · **★ 백본 6종 zero drift 251차** (NHIS #44 `c886ff1f` 러-1~4·silverangel essential canonical `c79c1be3`·system_feature `c9507190`·feeService `eab352a8`·extraService `f9c5d877`·carefor func.php `6226e6eb` IDENTICAL) · **★ 2026 고시 2종 cachebuster/counter DRIFT verbatim 불변(덮어쓰기 2건)** law247 `ffbd9b31`→`8bb35403`(제2025-247호·시행 2026.1.1·일부개정)·mohw126 `572665d0`→`88b994b9`(제2026-126호·본인부담상한액×13·2026-06-15) · **★ 4축 교차검증 가정 번복 0** (G14 plan-form ✅·대시보드/G26 ✅·v1.3-C ✅+·v2 CMS ✅·G-BANK/G-STAFF ✅+ deepen·G-STAFF-LEAVE-STATUS·G-BILLING-DEPOSIT-HALFMONTH-REPORT P3「가정」 carry) · **가정 번복 0**·**신규 갭 0**·**candidate 변동 0**·**상태 변경 3**(FE +2·BE +1·merge 591→594)·**미확인 -1**(longterm 610 → 「확인」 server-gate) | ROADMAP carry(G-BANK ✅·G-STAFF ✅·deepen 메모만)·`workspace_baseline.yaml` FE `@9105332`/BE `@6ed7cd4`·merge 594·COMPETITOR_MATRIX @HEAD·미확인 carry list 갱신(longterm 610 resolved → 「확인」 server-gate·remaining: silverangel SaaS 공개 요금만 carry) |

**planner 다음 액션 (BNK-448)**: ① **tester merge 594**(FE117+BE477·양쪽 WT CLEAN·선행 commit 불필요·V1–V165 contiguous·BE Test 228·FE test 422·QA-B182 Planned → Fixed candidate) ② `workspace_baseline.yaml` 정정 완료(FE `@a18b30e`→`@9105332`·ahead 115→117·BE `@7d29a38`→`@6ed7cd4`·ahead 476→477·merge 591→594) ③ **미확인 carry list 갱신** — longterm 610 resolved as 「확인」 server-gate (BNK-371~447 ~80 cycle 만에 close)·remaining 미확인: silverangel SaaS 공개 요금만 carry ④ **G-BANK-EXCEL-8·G-STAFF-NHIS-EXCEL-IMPORT ✅+ deepen 메모** (closure 변경 없음·BE row guard + UXD-146 a11y deepen 메모만) ⑤ **QA-B95 operation 승격 진단 강화** — FE `@9105332` auth blocker recovery 로 145 SKIP 일부 PASS 전환 기대·BE bootstrap state 회복 필요 carry · ⑥ **P0/P1 재정렬 0** — tester BE merge 1·origin/test push 594·QA-B95 operation 승격 carry.

### [BNK] BNK-447 인사이트 (2026-06-20) — ★★★ G-BANK-EXCEL-8 FE wire △→✅ full-stack closure(merge 591) · ★★ silverangel essential canonical 경로 이전 확인(`/newSilverangel/daycare/`) · ★ 백본 4종 zero drift 250차 · ★ 2026 수가/규제 4종 DRIFT verbatim 불변

| BNK | 핵심 | planner 반영 |
|-----|------|-------------|
| **BNK-447** | **★★★ G-BANK-EXCEL-8 FE wire △→✅ FULL-STACK CLOSURE** — BNK-446 FE WT DIRTY 4M(`BankDepositImportPanel.jsx`+`services.js`+test×2)→`@a18b30e` `feat(v2/G-BANK-EXCEL-8): wire bank deposit preview and row selection on payment page` commit + BE `@7d29a38` `test(g-bank-excel-8): reject non-positive bank deposit row selection`(WT DIRTY 1M closure) ↔ 케어포 PDF p.88 8-bank 본인부담 입금 ↔ ogada `/billing/imports/bank-deposits` 미리보기+행선택 full-stack parity·신규 갭 0 · **★★ silverangel essential canonical 경로 이전 재실측** — `/silverangel/angelsystem/daycareEssentialWork.do`·`/silverangel/daycare/daycareEssentialWork.do` 모두 **HTTP 404·`3c93af54`** → 정본 [`/newSilverangel/daycare/daycareEssentialWork.do`](https://www.silverangel.kr/newSilverangel/daycare/daycareEssentialWork.do) HTTP **200·131,664B·`c79c1be3` zero drift**·이동서비스 평가지표(운전자·동승자·차량안전·차량운행표) verbatim 불변 ↔ ogada G15 별지 제22호 실데이터 운행일지 우위 · **★ 백본 4종 zero drift 250차**(NHIS #44 `c886ff1f` 러-1~4·system_feature `c9507190`·feeService `eab352a8`·extraService `f9c5d877`) · **★ 2026 수가/규제 4종 DRIFT verbatim 불변(덮어쓰기 4건)** longterm 502 `72148cfe`(+9B `var s16;`·단기보호 74,060·통합재가)·503 `c94cc389`(경감 50%×4/60%×3)·law247 `ffbd9b31`(제2025-247호·시행 2026.1.1)·mohw126 `572665d0`(제2026-126호·본인부담상한액·2026-06-15) · **가정 번복 0**·**신규 갭 0**·**candidate 변동 0**·**상태 변경 1**(G-BANK △→✅)·**미확인 0**(essential 경로 resolved) | ROADMAP **G-BANK-EXCEL-8 P2 ✅ closure**(candidate 제거) · `workspace_baseline.yaml` FE `@a18b30e`/BE `@7d29a38`·merge 591 · COMPETITOR_MATRIX @HEAD · silverangel essential 인용 경로 `/newSilverangel/daycare/` 정정 |

**planner 다음 액션 (BNK-447)**: ① **tester merge 591**(FE115+BE476·양쪽 WT CLEAN·선행 commit 불필요·V1–V165 contiguous) ② `workspace_baseline.yaml` 정정 완료(FE `@fffc2c1`→`@a18b30e`·dirty 4M→CLEAN·ahead 114→115·BE `@e3b74a0`→`@7d29a38`·dirty 1M→CLEAN·ahead 475→476·merge 589→591) ③ **ROADMAP `G-BANK-EXCEL-8` P2 ✅ closure 반영**(candidate 제거) ④ **silverangel essential 인용 경로 정정**(`/silverangel/angelsystem`·`/silverangel/daycare` 404 → 정본 `/newSilverangel/daycare/daycareEssentialWork.do`) ⑤ **silverangel SaaS 공개 요금표·longterm 610 게이트** 미확인 carry.

### [BNK] BNK-430~431 인사이트 (2026-06-20) — ★ silverangel.co.kr 엔젤쇼핑몰 vendor 부수 도메인 1차 확인 · ★ silverangel 2-track ↔ ogada `BranchServiceType` 5-type cross-coverage + `IntegratedHomeProviderDiscoveryPanel` 통합재가 단독 우위 · ★ NHIS #44 218차 1차 확인 closure · 백본 12종 verbatim 불변

| BNK | 핵심 | planner 반영 |
|-----|------|-------------|
| **BNK-431** | **★★★ 신규 evidence URL 1건(주력)** [silverangel.co.kr shop type=5](https://www.silverangel.co.kr/shop/listtype.php?type=5) HTTP **200·179,268B·`dda346ff`** = 「엔젤쇼핑몰 할인상품」 `<title>할인상품 | 엔젤쇼핑몰</title>`·`<strong>(주)엔젤시스템</strong>`·1.3k~34.1k 케어용품·010-8326-9469(SaaS 1600-6859 별도) = **silverangel 2-도메인 split vendor 모델 1차 확인**(BNK-371~430 230+ cycle 만에 최초 cross-link)·**SaaS 가입비 0건 미확인 carry** · **★★ silverangel `mainService.do` 2-track 정본**(입소+주야간 only·`/visit/*`·`/integrated/*`·`/recipient/*` 14종 URL probe 모두 404) ↔ **ogada `BranchServiceType` 5-type(DAY_NIGHT/SHORT_TERM/INTEGRATED_HOME/HOME_CARE/NURSING_FACILITY)** + `IntegratedHomeProviderDiscoveryPanel`(공단 longterm 검색 API·`searchAdminKindCd=07`·`ltcAdminKindChoiceYn8=Y`·**월10만원 가산 안내 verbatim**) = **통합재가 발견·연계 unique 우위** · **★ NHIS #44 러-1~4 218차 1차 확인 closure**(PLAN_NOTES #44 요청)·러-1 편도 1회당·1일 1회·러-2 왕복=편도×2·러-3 추가·러-4 일지·④ 별지 제22호 verbatim 불변 · **★ 백본 12종 verbatim 불변** silverangel 4종 + lcms zero drift + longterm 502/503 `+var s16;` 1-line(74,060·50%/60% 불변) + law247 cachebuster + mohw126 조회수 +6 counter only(본인부담상한액 불변) · **신규 갭 0** · **신규 candidate +2**(G-VENDOR-SHOP-INTEGRATION P3「가정」 + G-INTEGRATED-HOME-MONITORING-DEEPEN P3「가정」) | ROADMAP v1.3-C/v2(BranchServiceType 5-type 우위 메모) · REQUIREMENTS §1-5(통합재가 가산 cross-walk) · USER_STORIES(US-INTEGRATED-HOME deepen) · COMPETITOR_MATRIX @HEAD |
| **BNK-430** | **★★★ Channel.io bc7f4cd9 237차 DRIFT**(검은=반영/빨간=미반영 verbatim 불변) · **★★ G21 4축 lifecycle** schedule-rfid comp_01~09 + change-list 7-col excel + duplicate-schedule negative + bc7f4cd9 처리상태 → ogada COMP_01~09 ✅+·black/red UI P3 carry · **★ 가격·도입 9,347 verbatim·V160 platform_admin rename** | ROADMAP G21 carry · COMPETITOR_MATRIX 갱신 |
| **BE WT DIRTY 5M+11U** | `UserAccountRequest*` 6 API + 2 persistence + `V161__one_hq_admin_per_organization.sql` + `V162__user_account_requests.sql` = **HQ admin 단일 보장 + 사용자 계정 요청 워크플로 신규 layer WIP**·V160 platform_admin rename 후속 권한 layer 완성 = **SaaS 멀티테넌트 onboard 운영 일관성 확보** | coder 즉시 commit→push → V1–V162·merge 561 |
| **이전 BNK-424~429** | **★ G15-KAKAO-INTEGRATION 6-layer 우위**(케어포 postcode 1-layer only·BNK-429) · TransportKakaoApiStatusPanel FE @ `ba74bb5` · Kakao quota tracker BE → BNK-429 commit closure(+11 quota tracker layer) | carry · 신규 갭 0 |

**planner 다음 액션 (BNK-431)**: ① **tester merge 560**(FE101+BE459·BE WT DIRTY 5M+11U 선행 commit 권장·V1–V160 contiguous) ② `workspace_baseline.yaml` 정정(FE `@4d87e19`→`@380be3c`·dirty 10M→**1M**·ahead 99→**101**·BE `@3023c9e` carry·dirty CLEAN→**DIRTY 5M+11U** User account request layer WIP·V160→V160+untracked V161/V162·BE Test 221→**222**·merge 558→**560**) ③ **ROADMAP v1.3-C/v2** 갱신 — `BranchServiceType` 5-type cross-coverage + `IntegratedHomeProviderDiscoveryPanel` 통합재가 가산 발견·월10만원 안내 우위 메모 + G-VENDOR-SHOP-INTEGRATION/G-INTEGRATED-HOME-MONITORING-DEEPEN P3 candidates 추가 ④ **PLAN_NOTES #44 closure**(NHIS 러-1~4 218차 1차 확인·verbatim 불변) ⑤ **silverangel SaaS 공개 요금표·longterm 610 게이트** 미확인 carry.

### [BNK] BNK-424~429 인사이트 (2026-06-20) — ★ G15-KAKAO-INTEGRATION 6-layer 우위 · Kakao API status panel · quota tracker WIP · FAQ21832 out-of-scope

| BNK | 핵심 | planner 반영 |
|-----|------|-------------|
| **BNK-429** | **★★★ 케어포 postcode 1-layer only ↔ ogada 6-layer**(postcode + Maps + Geocoding + Directions + API status panel + quota tracker WIP) = **5-layer 우위 재확정** · func.php module 2 cross-walk ✅5·✅+3·△4·❌0 · **신규 candidate G15-KAKAO-QUOTA-DASH P3「가정」** | ROADMAP v1.3-A · REQUIREMENTS §1-5 · USER_STORIES US-T02 |
| **BNK-428** | FE `@acc5933` WT DIRTY 13M+2U → **`@ba74bb5` CLEAN commit closure** + `TransportKakaoApiStatusPanel` 신규 · BE `@48eea95` → **`@e2b764b` commit** + quota tracker 4U WIP | QA-B167 Fixed · QA-B169 Planned |
| **BNK-427~424** | 8축 가정 번복 0 · G-CASH-RECEIPT-LOG·G26·G32 carry 재입증 · 백본 244/217차 zero drift | carry · 신규 갭 0 |
| **BNK-428 FAQ21832** | HR payroll Top5 hub evidence → **module 11 payroll out-of-scope N/A** carry | carry · 신규 갭 아님 |

### [PLN] QA 피드백 반영 (2026-06-20, 176차 — BNK-419~423 · TSR 1127~1131차 · QA-B163 Open→Planned · QA Open 0 · ★ G-CASH-RECEIPT-LOG end-to-end · ★ FAQ21823 partial+ · QA-B116 Planned · QA-B95 Planned carry)

| 항목 | 내용 | 반영 문서 |
|------|------|-----------|
| **git baseline** | FE develop `@16afd4c`/test `@debe6dd` · BE develop/test `@bfad37d` · FE **merge pending 2** · BE **SYNCED** · WT **CLEAN** · merge gate **543**(FE90+BE453) · origin/test push **453 BE+90 FE** · FE test **1833/1833** · FE develop **1838/1840**(2 FAIL) · BE **1606/1606+1608/1608 PASS** · live E2E **126 PASS/19 SKIP**(carry) · **107 route·86 page·V1–V159** · **BE Test 218** · **FE test 414** | ROADMAP CURRENT BASELINE |
| **QA-B163 Planned** | FE develop HEAD `@16afd4c` **2 FAIL** `StaffEmploymentContractRenewalSummaryPanel.test.jsx` — lifecycle `?tab=lifecycle` href·MemoryRouter · TSR 1131차 Open → PLN 176차 Planned · **이관 규율 6·7·기능 갭 아님** | QA_FEEDBACK Open→Planned · ROADMAP P0 |
| **QA-B159 Fixed** | BE develop→test merge EXECUTED @ `bfad37d` · TSR 1130차 verified · post-merge **1608/1608 PASS** | QA_FEEDBACK Planned |
| **BNK-419~423** | **★★★ G-CASH-RECEIPT-LOG full-stack end-to-end 재입증 ✅**(BNK-423) · **★ FAQ21823 △ partial+**(BNK-422·5항 checklist+서식 modal `@1b6d2b1`·lifecycle tab `@033b319`·renewal record `@16afd4c`) · **★ Channel.io fd80da95** G-PROVIDER-CHANGE-COUNSEL P3 · **★ 케어포 module 10** P3 candidates G-CLIENT-PHOTO-ALBUM·G-NOTICE-BOARD·G-BULK-SMS(BNK-421) · **신규 갭 0** | ROADMAP·REQUIREMENTS·USER_STORIES |
| **QA-B116 Planned** | origin/test push **453 BE+90 FE** · post-merge **1606/1606+1833/1833 PASS** · push 후 재확인 | ROADMAP P0 |
| **QA-B95 Planned** | operation BLOCK · `./scripts/run-live-e2e.sh` full criteria 미충족 carry | ROADMAP P0 |
| **잔여 P0/P2/P3** | **COD QA-B163 test fix** → **tester FE merge(2)** → **origin/test push(453 BE+90 FE)** → **QA-B116 post-merge** → **QA-B95 operation 승격** · **P2 carry** FAQ21823 BE contract record · **P3 carry** G-CASH-RECEIPT-NTS-API · G-PROVIDER-CHANGE-COUNSEL · G-CLIENT-PHOTO-ALBUM | ROADMAP v1.2.1·v2·v3.1 |

**coder/ops 다음 액션 (176차)**: ① **COD QA-B163** — panel test lifecycle href·MemoryRouter fix → develop HEAD **0 FAIL** ② **tester FE merge(2)** @ `033b319`·`16afd4c` ③ **origin/test push**(453 BE+90 FE) ④ **QA-B116 post-merge 재확인** ⑤ **QA-B95** operation 승격.

> **175차→176차 delta**: merge gate 533→**543** · BE merge pending 2(QA-B159)→**SYNCED @ `bfad37d`** · FE merge pending 0→**2(QA-B163 Planned)** · **G-CASH-RECEIPT-LOG → end-to-end 재입증 ✅** · **FAQ21823 △ partial → △ partial+** · **신규 벤치마크 갭 0**.

### [BNK] BNK-419~423 인사이트 (2026-06-20) — ★ G-CASH-RECEIPT-LOG end-to-end · FAQ21823 partial+ · 케어포 module 10 P3

| BNK | 핵심 | planner 반영 |
|-----|------|-------------|
| **BNK-423** | G-CASH-RECEIPT-LOG **전 계층 git 실측 재입증 ✅** — V158/V159·API 4 endpoint·FE page/modal/alerts·테스트 6종 · 잔여 P3 = NTS API only | ROADMAP v3.1 · US-G26 · REQUIREMENTS §1-5 |
| **BNK-422** | FAQ21823 **5항 checklist+서식 modal closure** @ `1b6d2b1` · Channel.io fd80da95 = **G-PROVIDER-CHANGE-COUNSEL P3** · 01df98f5 G21 3-Track 1–2 ✅ | US-R03 · ROADMAP v1.2.1 |
| **BNK-421** | 케어포 module 10 9-leaf cross-walk · **P3 candidates** G-CLIENT-PHOTO-ALBUM·G-NOTICE-BOARD·G-BULK-SMS | REQUIREMENTS §1-5 P3 backlog |

### [PLN] QA 피드백 반영 (2026-06-20, 175차 — BNK-417~418 · TSR 1118~1119차 · QA-B159 Open→Planned · QA Open 0 · ★ FAQ21823 근로계약 갱신 · QA-B116 Planned · QA-B95 Planned carry)

| 항목 | 내용 | 반영 문서 |
|------|------|-----------|
| **git baseline** | FE `@f31c346`/BE develop `@beef81e` · test BE `@7e4c07e` · FE **SYNCED** · BE **merge pending 2** · WT **CLEAN** · merge gate **533**(FE85+BE448) · origin/test push **448 BE+85 FE** · FE **1828/1828** · BE test **1598/1598** · BE develop **1600/1600** · live E2E **126 PASS/19 SKIP** · **107 route·86 page·V1–V158** · **BE Test 217** · **FE test 413** | ROADMAP CURRENT BASELINE |
| **QA-B159 Planned** | BE develop→test merge pending 2 @ `7a9d7a5`(live-e2e seed readiness) + `beef81e`(default credentials bootstrap) · TSR 1118차 Open → PLN 175차 Planned · **이관 규율 6·7·기능 갭 아님** | QA_FEEDBACK Open→Planned · ROADMAP P0 |
| **QA-B158 Fixed** | DateInput month-only date-boundary test @ `0038846` · TSR 1113차 verified | QA_FEEDBACK 기록 |
| **BNK-417~418** | **★ 케어포 module 7 11/11 ✅ + superset 2**(G33 청구시작·G26 통계) · **★ module 11 HR payroll 6/6 out-of-scope** · **★ FAQ21823 `StaffEmploymentContractRenewalPanel` △ partial** @ `f62402f`/`f31c346`(근로계약 renewal·급여대장 0) · **★ ezCare 7e0734fa 시급→급여 4-Track = 재가 HR out-of-scope** · **★ bc7f4cd9 검은/빨간 G21 parity ✅ carry** · **신규 갭 0** · **백본 235~236차 zero drift** | ROADMAP·REQUIREMENTS·USER_STORIES |
| **QA-B116 Planned** | origin/test push **448 BE+85 FE** · post-merge **1598/1598+1828/1828 PASS** · push 후 재확인 | ROADMAP P0 |
| **QA-B95 Planned** | operation BLOCK · `./scripts/run-live-e2e.sh` full criteria 미충족 carry | ROADMAP P0 |
| **잔여 P0/P3** | **tester BE merge(2)** @ `7a9d7a5`·`beef81e` → **origin/test push(448 BE+85 FE)** → **QA-B116 post-merge** → **QA-B95 operation 승격** · **P3 carry** G-HOURLY-WAGE-SCHEDULE-REUPLOAD · G-CASH-RECEIPT-NTS-API · G-PROVIDER-CHANGE-COUNSEL · module 11 payroll | ROADMAP v1.2.1·v2·v3.1 |

**coder/ops 다음 액션 (175차)**: ① **tester BE merge(2)** @ `7a9d7a5`·`beef81e` → post-merge `mvn test` PASS ② **origin/test push**(448 BE+85 FE) ③ **QA-B116 post-merge 재확인** ④ **QA-B95** operation 승격.

> **174차→175차 delta**: merge gate 522→**533** · BE merge pending 1(QA-B157 Fixed)→**2(QA-B159 Planned)** · FE `@99b795a`→`@f31c346`(FAQ21823 dashboard widget +1) · **신규 벤치마크 갭 0** · **FAQ21823 US-R03 △ partial deepen**.

### [BNK] BNK-417~418 인사이트 (2026-06-20) — ★ 케어포 module 7/11 cross-walk · FAQ21823 · ezCare G21 parity

| BNK | 핵심 | planner 반영 |
|-----|------|-------------|
| **BNK-417** | 케어포 module 7 **11/11 ✅** + PDF p.90/p.92 superset(G33·G26) · module 11 **6/6 HR payroll out-of-scope** · FAQ21823 근로계약 renewal △ @ `f62402f`/`f31c346` · demo-work 이동서비스 nav 0 | ROADMAP v1.2.1 · US-R03 · REQUIREMENTS §1-5 |
| **BNK-418** | ezCare FAQ21829 Top5 hub + Channel.io **7e0734fa** 시급→급여 4-Track = **재가 HR out-of-scope** · **bc7f4cd9** 검은/빨간 = ogada G21 **✅+ carry** · 도입 9,347 oscillation carry | ROADMAP G21 메모 · REQUIREMENTS G21 · P3 G-HOURLY-WAGE-SCHEDULE-REUPLOAD「가정」 |

### [PLN] QA 피드백 반영 (2026-06-20, 174차 — BNK-406~412 · TSR 1100~1107차 · QA-B157 Open→Planned · QA Open 0 · ★ G26/G-7-1 closure · QA-B116 Planned · QA-B95 Planned carry)

| 항목 | 내용 | 반영 문서 |
|------|------|-----------|
| **git baseline** | FE `@99b795a`/BE develop `@35d1560` · test `@298bcdf` · FE **SYNCED** · BE **merge pending 1** · WT **CLEAN** · merge gate **522**(FE79+BE443) · origin/test push **442 BE+79 FE** · FE **1807/1807** · BE test **1585/1585** · BE develop **1589/1589** · live E2E **126 PASS/19 SKIP** · **107 route·86 page·V1–V158** · **BE Test 216** · **FE test 409** | ROADMAP CURRENT BASELINE |
| **QA-B157 Planned** | BE develop→test merge pending 1 @ `35d1560`(G-CASH-RECEIPT-LOG identifier validation·BNK-412) · TSR 1106차 Open → PLN 174차 Planned · **이관 규율 6·7·기능 갭 아님** | QA_FEEDBACK Open→Planned · ROADMAP P0 |
| **QA-B155/B156 Fixed** | FE merge EXECUTED @ `19ed7f3`(G26 yearBasis+NTS CSV·G-CASH-RECEIPT) · BE RBAC mock @ `08ad3b3`(G-7-1 Excel export) | QA_FEEDBACK 기록 |
| **BNK-406~412** | **★ G26 `@19ed7f3` yearBasis+NTS CSV ✅ full-stack**(BNK-408) · **★ G-7-1 Excel `@58d6694`/`@e454d3b` ✅**(BNK-409) · **★ G-CASH-RECEIPT-LOG 6-계층 deepen** — UXD-139 a11y(BNK-407) + pending error guard `@99b795a`(BNK-411) + identifier 검증 `@35d1560`(BNK-412) · **★ G-CASH-RECEIPT-TAX-DEDUCTION-EXPORT △→✅**(G26 closure) · **★ 신규 candidate G-PROVIDER-CHANGE-COUNSEL P3「가정」**(BNK-410 FAQ21795) · **★ 8축 교차검증 가정 번복 0** · **백본 227/229차 zero drift** | ROADMAP·REQUIREMENTS·USER_STORIES |
| **QA-B116 Planned** | origin/test push **442 BE+79 FE** · post-merge **1585/1585+1807/1807 PASS** · push 후 재확인 | ROADMAP P0 |
| **QA-B95 Planned** | operation BLOCK · `./scripts/run-live-e2e.sh` full criteria 미충족 carry | ROADMAP P0 |
| **잔여 P0/P3** | **tester BE merge(1)** @ `35d1560` → **origin/test push(442 BE+79 FE)** → **QA-B116 post-merge** → **QA-B95 operation 승격** · **P3 carry** G-CASH-RECEIPT-NTS-API · G-PROVIDER-CHANGE-COUNSEL · G-LTM-DIRECT-SYNC · G14 plan-form · module 1 상담일지 | ROADMAP v1.2.1·v3.1 |

**coder/ops 다음 액션 (174차)**: ① **tester BE merge(1)** @ `35d1560` → post-merge `mvn test` PASS ② **origin/test push**(442 BE+79 FE) ③ **QA-B116 post-merge 재확인** ④ **QA-B95** operation 승격.

> **173차→174차 delta**: G-CASH-RECEIPT-LOG 4-계층 → **6-계층**(⑤ pending load error guard @ `99b795a` ⑥ identifier 검증 @ `35d1560`). G-CASH-RECEIPT-TAX-DEDUCTION-EXPORT P3 candidate → **✅ 해소**(G26 NTS CSV @ `19ed7f3`). G-7-1 엑셀다운로드 P3 carry → **✅ closure**(BNK-409).

### [BNK] BNK-406~412 인사이트 (2026-06-20) — ★ G26/G-7-1 closure · G-CASH-RECEIPT-LOG 6-계층 · G-PROVIDER-CHANGE-COUNSEL P3

| BNK | 핵심 | planner 반영 |
|-----|------|-------------|
| **BNK-408** | G26 `@19ed7f3` segmented「수납년도/청구년도」+「국세청 CSV」export ↔ 케어포 manual 7-8 **✅ full-stack** | ROADMAP v1.2.1 G26 · US-L07 · REQUIREMENTS §1-5 |
| **BNK-409** | G-7-1 `@58d6694`/`@e454d3b` Excel export ↔ 케어포 PDF p.87 ② **✅ parity** | G-7-1-PRINT-BUNDLE ✅+ · REQUIREMENTS |
| **BNK-410** | FAQ21795 급여제공직원 변경 14일 상담 ↔ ogada 고충 상담 only **❌** · 재가 out-of-scope | **G-PROVIDER-CHANGE-COUNSEL P3「가정」** |
| **BNK-411~412** | `@99b795a` pending error guard + `@35d1560` identifier validation | G-CASH-RECEIPT-LOG 6-계층 · US-G26 |

### [TWR] 문서 작성 현황 (2026-06-21 282차 자율 실행)

> **최근 갱신 (282차)**: ops 문서 **updated=2026-06-21T21:00:00+09:00** 동기화 · **BE `6ed7cd4`/FE `9105332` · 180차 baseline · G-BANK invalid rowNumbers · live E2E auth recovery · UXD-146 · 출석 Must 갭 체크리스트**
>
> ✅ **ops 문서 282차 자율 동기화 완료**:
> - **CHANGELOG.md** — **282차 Unreleased** · **G-BANK invalid rowNumbers guard** · **live E2E auth blocker recovery** · **UXD-146 import a11y**
> - **USER_MANUAL.md** — **§1-3·§2-2·§4-4·§4-6·§4-7-0** baseline·출석 roster·QR Must 갭 현장 대응·은행 invalid rowNumbers·UXD-146
> - **ADMIN_GUIDE.md** — **§1-4·§10-4 US-L01** invalid rowNumbers·live E2E Q580·UXD-146
> - **FAQ.md** — **Q579–Q581 신규** · **Q576·Q578·Q94·Q109 갱신** · Must 보강 FAQ 유지
> - **DEPLOYMENT_GUIDE.md** — baseline **`6ed7cd4`/`9105332`** · §1-3·§3-7·§11-3 스모크
>
> **다음 문서화 우선순위 (283차+)**: **출석 roster API 확장**(coder 후속) · **QR 생성 payload·이미지 갭**(coder) · **G-CASH-RECEIPT-NTS-API** P3 · **L03_M15 말기 돌봄** · **7-5 live PG** · **G-STAFF-LEAVE-STATUS** P3 · **데이터 보관·파기 정책**

### [TWR] 문서 작성 현황 (2026-06-21 279차 자율 실행)

> **최근 갱신 (279차)**: ops 문서 **updated=2026-06-21T06:00:00+09:00** 동기화 · **BE `3bbfc00`/FE `a2f599c` · 179차 baseline · G-BANK-EXCEL-8 · G-STAFF-NHIS-EXCEL-IMPORT · V165 · US-H01 · docs 279차 완료**
>
> ✅ **ops 문서 279차 자율 동기화 완료**:
> - **CHANGELOG.md** — **279차 Unreleased** · **G-BANK-EXCEL-8** · **G-STAFF-NHIS-EXCEL-IMPORT** · **V165** · **US-H01** · **UXD-144/145**
> - **USER_MANUAL.md** — **§1-3·§1-5·§2-2·§4-6·§4-7-0·§5-2** NHIS caregiver bulk·은행 preview API·HQ dual dashboard
> - **ADMIN_GUIDE.md** — **§1-4·§3-2-1·§10-4 US-L01** formats+preview·staff NHIS import·V165
> - **FAQ.md** — **Q572–Q575** 신규 · Q227 bank deposit preview cross-ref
> - **DEPLOYMENT_GUIDE.md** — baseline **`3bbfc00`/`a2f599c`** · V165 · §1-4·§11-3 스모크
>
> **다음 문서화 우선순위 (280차+)**: **출석 roster·QR Must 갭** (Q94·Q109) · **G-BANK-EXCEL-8 FE preview wire** · **G-CASH-RECEIPT-NTS-API** P3 · **L03_M15 말기 돌봄** · **7-5 live PG** · **데이터 보관·파기 정책**

### [TWR] 문서 작성 현황 (2026-06-21 278차 자율 실행)

> **최근 갱신 (278차)**: ops 문서 **updated=2026-06-21T03:30:00+09:00** 동기화 · **BE `80b9619`/FE `d723d5a` · 178차 baseline 확정 · G14 NHIS 10-field care plan form ✅ · V162–V164 · dashboard claimGenerationGuard StatCard · docs 278차 완료**
>
> ✅ **ops 문서 278차 자율 동기화 완료**:
> - **workspace_baseline.yaml** — **178차 baseline** BE `80b9619`(464 commits)/FE `d723d5a`(105 commits)·V1–V164·108 route·86 page
> - **CHANGELOG.md** — **278차 Unreleased 블록** 완료 · **G14 care-plan-form ✅** · **V162–V164** · **dashboard claimGenerationGuard StatCard (Q571)**
> - **USER_MANUAL.md** — **§1-3·§1-5·§2-2·§4-2** baseline·G32 경로 정정·청구 생성 가드 StatCard·Must 빠른 점검
> - **ADMIN_GUIDE.md** — **§1-4·§1-4-a·§6-2-2a·§6-2-2b** G14·청구 생성 가드 운영 모니터링
> - **FAQ.md** — **Q567–Q571** Must 보강·G32 API 경로 정정·Q571 StatCard 안내
> - **DEPLOYMENT_GUIDE.md** — baseline **`80b9619`/`d723d5a`** · §1-4 Must API 스모크 목록
>
> **다음 문서화 우선순위 (279차+)**: **P3 출석 roster·QR Must 갭** (Q94·Q109 extended) · **G-CASH-RECEIPT-NTS-API** P3 · **L03_M15 말기 돌봄 호스피스** · **7-5 live PG실연동** · **데이터 보관·파기 정책** · **PII 보호·마스킹 조치**

### [TWR] 문서 작성 현황 (2026-06-21 275차 자율 실행)

> **최근 갱신 (275차)**: ops 문서 **updated=2026-06-21T02:15:00+09:00** 동기화 · **BE `3023c9e`/FE `380be3c`·BNK-424~429·G15-KAKAO-INTEGRATION·BranchServiceType 5-type·P3 candidates**
>
> ✅ **ops 문서 275차 자율 동기화 완료**:
> - **FAQ.md** — **§21 v1.3-A 배차·Kakao** (Q425~430) · **TransportKakaoApiStatusPanel·API 일일 사용량·통합재가·BranchServiceType·V160 role_code rename**
> - **FAQ.md** — **§22 v2 roadmap·P3 candidates** (Q431~433) · **현금영수증 자동 발급·출석 QR 정합·L03 간호급여**
> - **CHANGELOG.md** — **275차 Unreleased 블록** 갱신
> - **총 9개 신규 FAQ** (Q425~Q433·Q424 이전 434개 기존)
>
> **다음 문서화 우선순위 (276차+)**: **출석 roster·QR Must 갭** (Q94·Q109 extended) · **L03_M15 말기 돌봄** · **7-5 live PG** · **G-CASH-RECEIPT-NTS-API** · **데이터 보관·파기 정책**

### [TWR] 문서 작성 현황 (2026-06-21 274차 자율 실행)

> **최근 갱신 (274차)**: ops 문서 **updated=2026-06-21T01:30:00+09:00** 동기화 · **BE `3023c9e`/FE `380be3c` · V160 ogada_platform_admin · Kakao per-API quota · staff account request workflow · platform hq_admin issuance validation · UXD-143 a11y · 양쪽 WT CLEAN**
>
> ✅ **ops 문서 274차 자율 동기화 완료**:
> - **USER_MANUAL.md** — §1-3·§2-2·§4-7·§5-3·§5-8 **staff account request** · **Kakao per-API quota table**
> - **ADMIN_GUIDE.md** — §1-3·§3 **ogada_platform_admin** · **§3-2-1 platform account request approval** · **hq_admin issuance validation**
> - **DEPLOYMENT_GUIDE.md** — §1-3·§4-7 **V160** · **Kakao daily limit properties** · baseline **`3023c9e`/`380be3c`**
> - **FAQ.md** — **Q554 갱신** (per-API quota) · **Q555~Q556 신규** (account request · role rename)
> - **CHANGELOG.md** — 274차 Unreleased 블록
>
> **다음 문서화 우선순위 (275차+)**: **출석 roster·QR Must 갭** (Q94·Q109) · **G15-KAKAO-QUOTA-DASH P3** (콘솔 대비 대시보드) · L03 간호급여 잔여 leaf · 7-5 live PG · **G-CASH-RECEIPT-NTS-API**

### [TWR] 문서 작성 현황 (2026-06-21 267차 자율 실행)

> **최근 갱신 (267차)**: ops 문서 **updated=2026-06-21T00:00:00+09:00** 동기화 · **BE `beef81e`/FE `f31c346` · US-R03 FAQ21823 list+dashboard renewal widgets · live E2E allow-default-credentials · 양쪽 WT CLEAN**
>
> ✅ **ops 문서 267차 자율 동기화 완료**:
> - **USER_MANUAL.md** — §1-3·§2-2·§4-2·§5-3 **FAQ21823 목록·대시보드·상세 3계층**
> - **ADMIN_GUIDE.md** — §1-4·§6-2-6b **`StaffEmploymentContractRenewalSummaryPanel`·dashboard widget** · **`allow-default-credentials`**
> - **DEPLOYMENT_GUIDE.md** — §1-3·§3-7·§11-3 baseline **`beef81e`/`f31c346`** · live E2E credential flag checklist
> - **FAQ.md** — **Q540 갱신** (list+dashboard) · **Q542 신규** (allow-default-credentials) · **Q490 갱신**
> - **CHANGELOG.md** — 267차 Unreleased 블록
>
> **다음 문서화 우선순위 (268차+)**: P3 **G-CASH-RECEIPT-NTS-API** (홈택스 실연동) · **출석 roster·QR Must 갭** (Q94·Q109) · L03 간호급여 잔여 leaf · 7-5 live PG · G-PROVIDER-CHANGE-COUNSEL

### [TWR] 문서 작성 현황 (2026-06-20 265차 자율 실행)

> **최근 갱신 (265차)**: ops 문서 **updated=2026-06-20T22:30:00+09:00** 동기화 · **BE `7e4c07e`/FE `0038846` · J03 guardian document quiet-hours manual reject · G-CASH-RECEIPT-LOG FE identifier pre-submit validation · 양쪽 WT CLEAN**
>
> ✅ **ops 문서 265차 자율 동기화 완료**:
> - **USER_MANUAL.md** — §1-3·§2-2·§4-7-3·§5-10-1 **보호자 서류 quiet-hours 거부** · **Modal submit 전 identifier 검증**
> - **ADMIN_GUIDE.md** — §1-4·§10-4·§10-8 **`dispatchManualClientEvent`** · **`CashReceiptRegisterModal` FE validation**
> - **DEPLOYMENT_GUIDE.md** — §1-3·§3-7·§11-3 baseline **`7e4c07e`/`0038846`** · guardian document quiet-hours regression checklist
> - **FAQ.md** — **Q537 갱신** (FE pre-submit validation) · **Q539 신규** (J03 guardian document quiet-hours)
> - **CHANGELOG.md** — 265차 Unreleased 블록
>
> **다음 문서화 우선순위 (266차+)**: P3 **G-CASH-RECEIPT-NTS-API** (홈택스 실연동) · **출석 roster·QR Must 갭** (Q94·Q109) · L03 간호급여 잔여 leaf · 7-5 live PG · G-PROVIDER-CHANGE-COUNSEL

### [TWR] 문서 작성 현황 (2026-06-20 264차 자율 실행)

> **최근 갱신 (264차)**: ops 문서 **updated=2026-06-20T21:00:00+09:00** 동기화 · **BE `4da0ca8`/FE `501fedc` · G-CASH-RECEIPT-LOG numeric-only identifier · UXD-140 G26/G-7-1/pending a11y · 양쪽 WT CLEAN**
>
> ✅ **ops 문서 264차 자율 동기화 완료**:
> - **USER_MANUAL.md** — §1-3·§2-2·§4-6-0-1·§5-10-1·§5-10-2 **숫자만 식별자 검증** · **pending Alert `aria-describedby`** · **G26 forced-colors** · **PDF `aria-label`**
> - **ADMIN_GUIDE.md** — §1-4·§10-4 **`4da0ca8` numeric-only** · **UXD-140 a11y**
> - **DEPLOYMENT_GUIDE.md** — §1-3·§3-7 baseline **`4da0ca8`/`501fedc`** · merge gate ~524
> - **FAQ.md** — **Q537 갱신** (numeric-only) · **Q538 신규** (UXD-140 a11y)
> - **CHANGELOG.md** — 264차 Unreleased 블록
>
> **다음 문서화 우선순위 (265차+)**: P3 **G-CASH-RECEIPT-NTS-API** (홈택스 실연동) · L03 간호급여 잔여 leaf · 7-5 live PG · G-PROVIDER-CHANGE-COUNSEL

### [TWR] 문서 작성 현황 (2026-06-20 263차 자율 실행)

> **최근 갱신 (263차)**: ops 문서 **updated=2026-06-20T18:00:00+09:00** 동기화 · **BE `35d1560`/FE `99b795a` · G-CASH-RECEIPT-LOG identifier normalize+validation · pending load error guard · 양쪽 WT CLEAN**
>
> ✅ **ops 문서 263차 자율 동기화 완료**:
> - **USER_MANUAL.md** — §1-3·§2-2·§5-10-1 **휴대폰·사업자번호 digit 검색·검증** · **pending API 실패 Alert** · Modal **「· 작년분」** suffix
> - **ADMIN_GUIDE.md** — §1-4·§10-4 **CashReceiptIssuanceService normalize+validate** · **`CashReceiptIssuancePage` pendingError**
> - **DEPLOYMENT_GUIDE.md** — §1-3·§3-7 baseline **`35d1560`/`99b795a`** · merge gate ~521
> - **FAQ.md** — **Q537 신규** (identifier search·validation·pending error)
> - **CHANGELOG.md** — 263차 Unreleased 블록
>
> **다음 문서화 우선순위 (264차+)**: P3 **G-CASH-RECEIPT-TAX-DEDUCTION-EXPORT** (연간 batch Excel) · **G-CASH-RECEIPT-NTS-API** (홈택스 실연동) · L03 간호급여 잔여 leaf · 7-5 live PG

### [PLN] QA 피드백 반영 (2026-06-20, 173차 — BNK-399~405 · TSR 1086~1096차 · QA-B153/B154 Fixed · QA Open 0 · ★ G-CASH-RECEIPT-LOG 4-계층 closure ✅ · QA-B116 Planned · QA-B95 Planned carry)

| 항목 | 내용 | 반영 문서 |
|------|------|-----------|
| **git baseline** | FE `@8aebe55`/BE `@58ff35e` · develop=test **SYNCED** · WT **CLEAN** · merge gate **511**(FE74+BE437) · origin/test push **437 BE+74 FE** · FE **1793/1793** · BE **1566/1566** · live E2E **126 PASS/19 SKIP** · **107 route·86 page·V1–V158** | ROADMAP CURRENT BASELINE |
| **QA-B153 Fixed** | FE develop HEAD full-suite 2 FAIL(VisitsPage·pilotPageFlows UXD-138 a11y) → COD fix `@d80f9dc` · TSR 1089차 merge EXECUTED · post-merge **1788/1788 PASS** | QA_FEEDBACK Open(기록) |
| **QA-B154 Fixed** | BE develop→test merge 2 commits EXECUTED @ `fe54af8`(G-CASH-RECEIPT-LOG dashboard API) · post-merge **1560/1560 PASS** | QA_FEEDBACK Open(기록) |
| **BNK-399~405** | **★★★ G-CASH-RECEIPT-LOG 4-계층 closure ✅**(172차 P2 gap → closure·**신규 갭 0**) — ① `/billing/cash-receipts` + V158 @ `cfc4b04`/`f79a19e` ② 수납 prompt @ `a17f148` ③ 대시보드 due-gate @ `221458e`/`fe54af8` ④ HQ pending + prior-year @ `58ff35e` + FE advisory @ `8aebe55` · **★ 케어포 7-2-1/7-8 cross-walk** · **★ 신규 candidate G-CASH-RECEIPT-TAX-DEDUCTION-EXPORT P3** · **백본 223차 zero drift** | ROADMAP·REQUIREMENTS·USER_STORIES |
| **QA-B116 Planned** | origin/test push **437 BE+74 FE** · post-merge **1566/1566+1793/1793 PASS** · push 후 재확인 | ROADMAP P0 |
| **QA-B95 Planned** | operation BLOCK · `./scripts/run-live-e2e.sh` full criteria 미충족 carry | ROADMAP P0 |
| **잔여 P0/P3** | **tester origin/test push(437 BE+74 FE)** → **QA-B116 post-merge** → **QA-B95 operation 승격** · **P3 carry** G-CASH-RECEIPT-NTS-API · G-CASH-RECEIPT-TAX-DEDUCTION-EXPORT · G-LTM-DIRECT-SYNC · G-PERIODIC-OBLIGATION-CALENDAR · G14 plan-form · G-7-1 엑셀다운로드 | ROADMAP v1.2.1·v3.1 |

**coder/ops 다음 액션 (173차)**: ① **tester origin/test push**(437 BE+74 FE) ② **QA-B116 post-merge 재확인** ③ **QA-B95** operation 승격(`./scripts/run-live-e2e.sh` full criteria). G-CASH-RECEIPT-LOG P2 구현 사이클 **완료** — P3 carry만 잔존(NTS API·국세청 batch export).

> **172차 P2 gap closure 근거 (173차)**: BNK-398에서 확인된 G-CASH-RECEIPT-LOG 갭(이지케어 FAQ 21701 별도 발급목록 메뉴)은 BNK-399~405에서 **4-계층 full-stack closure**로 해소. `/billing/reports/receipts`(수납 ledger)와 분리된 per-payment NTS 발급 이력 워크플로가 `@8aebe55`/`@58ff35e` 기준 **운영 가능**. 실시간 NTS API 자동발급(`G-CASH-RECEIPT-NTS-API`)·국세청 batch 자동 export(`G-CASH-RECEIPT-TAX-DEDUCTION-EXPORT`)만 P3 carry.

### [BNK] BNK-399~405 인사이트 (2026-06-20) — ★ G-CASH-RECEIPT-LOG 4-계층 closure · 케어포 7-8 cross-walk · 백본 223차 zero drift

| BNK | 핵심 | planner 반영 |
|-----|------|-------------|
| **BNK-400~403** | V158 `cash_receipt_issuances` + `/billing/cash-receipts` + 수납 CASH prompt + `CashReceiptRegisterModal` — FAQ 21701/21716 parity | US-G26 인수 조건 ✅ · ROADMAP v3.1 closure |
| **BNK-404** | 대시보드 `cashReceiptPendingCount`/`cashReceiptOverdueCount` SLA 7일 — FAQ 21716 due-date 가시화 | ROADMAP 4-계층 ③ |
| **BNK-405** | HQ `listPendingIssuances(branchId=null)` + `priorYearIssuanceEligible` + FE advisory @ `8aebe55` — FAQ 21717 | ROADMAP 4-계층 ④ · **신규 candidate G-CASH-RECEIPT-TAX-DEDUCTION-EXPORT** |
| **BNK-405 cross-walk** | 케어포 7-2-1/7-8 연1회 batch Excel ↔ ogada per-payment advisory + 연간 batch **두 시점 superset** | REQUIREMENTS §1-5 |

> **상태**: 초안 (사용자 승인 전)

---

---


---



### [PLN] QA 피드백 반영 (2026-06-19, 172차 — BNK-393~398 · TSR 1074~1085차 · QA-B150/B151/B152 Fixed · QA Open 0 · ★ 신규 갭 1 G-CASH-RECEIPT-LOG P2「확인」 · QA-B116 Planned · QA-B95 Planned carry)

> **172차 자동 기획 동기화** — BNK-393~398·TSR 1074~1085차. **QA Open 0(active)** — 신규 Open 항목 없음(Open→Planned 이동 0건). **★ QA-B151 Fixed @ `eed39ab`**(backend develop→test merge 3 commits EXECUTED·post-merge 1526/1526 PASS·171차 Planned 해소) · **★ QA-B152 Fixed @ `09912ba`**(live-e2e stale-runtime G32 필드 누락 skip guard·1079차 2 FAIL → 1081차 0 FAIL) · **★ QA-B150 Fixed @ `b272a7b`**(FE G32 merge) · **QA-B116 Planned carry**(origin/test push **430 BE+68 FE**·post-merge **1539/1539+1784/1784 PASS**) · **QA-B95 Planned carry**(operation BLOCK·live E2E **124 PASS/19 SKIP**).

| 항목 | 172차 관측 | 조치 |
|------|-----------|------|
| **baseline** | FE develop/test **`9b80505`** WT **CLEAN** · **SYNCED** · BE develop/test **`caeac0d`** WT **CLEAN** · **SYNCED** · `test..develop` FE/BE **0 ahead** · origin/test FE **`ab4de83`**(68 unpushed) · BE **`598d108`**(430 unpushed) · FE test **1784/1784 PASS** · BE test **1539/1539 PASS** · live E2E **124 PASS/19 SKIP** · **106 route** · **85 page** · **V1–V157** · **BE Test 211** · **FE test 405** · **모dule 78.28%** | ROADMAP CURRENT BASELINE 172차 갱신 · `workspace_baseline.yaml` 정정 |
| **BNK-393~398** | **★★★ 신규 갭 1 G-CASH-RECEIPT-LOG P2「확인」**(BNK-398 FAQ 21701/21716/21717 — 이지케어 「2.10 현금영수증 발급목록」 수급자 모듈 별도 메뉴 + 「현금영수증 발급정보 관리」 ↔ ogada `/billing/reports/receipts` **수납 ledger only**·NTS 발급내역 별도 메뉴 ❌) · **★ G32 4-계층 superset**(BNK-394 FAQ 21736 회의록 작성예시 + V157 array CHECK probe @ `45d95ea`) · **★ 케어포 3-1 segment nav ✅ @ `1d5747d`** · **★ func.php module 4 간호급여 10-leaf ✅7·△3·신규 갭 0**(BNK-397) · **★ silverangel 평가지표 PDF 이동서비스 지표40/41 ↔ G15 우위·신규 갭 0**(BNK-395) · **백본 216차 zero drift** · **8축 번복 0** | ROADMAP v3.1 candidate 표·v1.2.1 G32·REQUIREMENTS §1-5·USER_STORIES |
| **QA** | **Open 0(active)** · **QA-B150/B151/B152 Fixed** · **QA-B116 Planned** · **QA-B95 Planned carry** · Open→Planned 이동 **0건** | QA_FEEDBACK Open 0 carry · ROADMAP 172차 P0 |
| **merge gate** | **498 vs origin/test**(68 FE+430 BE) · **FE/BE develop=test SYNCED** · **cross-stream SYNCED(FE+BE)** | ROADMAP merge_status ready · operation BLOCK(origin/test push+QA-B95) |
| **잔여 P0/P2/P3** | **tester origin/test push(430 BE+68 FE)** → **QA-B116 post-merge** → **QA-B95 operation 승격** · **P2「확인」신규** G-CASH-RECEIPT-LOG(별도 사이클 spec→DB `cash_receipt_issuances`→FE `/billing/cash-receipts`) · **P3 carry** G-LTM-DIRECT-SYNC·G-PERIODIC-OBLIGATION-CALENDAR·G-CHANGE-REASON-AUDIT·G-STAFF-WELFARE·G34-APPROVAL | ROADMAP v1.2.1·v2·v3.1 갱신 |

**coder/ops 다음 액션 (172차)**: ① **tester origin/test push**(430 BE+68 FE) ② **QA-B116 post-merge 재확인** ③ **QA-B95** operation 승격(`./scripts/run-live-e2e.sh` full criteria) ④ **(신규 사이클)** G-CASH-RECEIPT-LOG P2 — API_SPEC·ERD 명세 → `cash_receipt_issuances`(`client_id`·`payment_id`·`nts_receipt_no`·`identifier_type`(phone/biz)·`identifier_value`·`issued_at`·`amount`) 마이그레이션 → `/billing/cash-receipts`(목록 + 수급자별 발급정보 관리) FE.

> **신규 갭 처리 근거 (172차)**: BNK-398의 G-CASH-RECEIPT-LOG는 이지케어 직접 메뉴(FAQ 21701)와 법적 운영 원칙(FAQ 21716 납입 즉시 발급·FAQ 21717 연도 mismatch) **2-evidence**로 확인되어, 기존 P3「가정」 candidate(G-CASH-RECEIPT)을 **P2「확인」으로 승격**한다. ogada `/billing/reports/receipts`(수납대장·누가 얼마 납입)와 `MedicalExpenseDeductionPanel`(연말정산 의료비공제 NTS XLSX·연 1회 집계)은 **이미 존재**하나, **per-payment NTS 현금영수증 발급 이력**(발급번호·식별자·발급일별 trace)은 별개 워크플로로 **부재** = 실제 기능 갭. MVP 직후 별도 사이클로 spec→DB→FE 구현 권장(법정 의무·세무 감사 대응).

---

### [BNK] BNK-393~398 인사이트 (2026-06-19) — ★ 신규 갭 1 G-CASH-RECEIPT-LOG P2 · G32 4-계층 superset · 케어포 3-1 nav · 백본 216차 zero drift

| BNK | 핵심 인사이트 | ogada 반영 |
|-----|-------------|-----------|
| **BNK-398** | **★★★ FAQ 21701 「현금영수증 발급 내역」** — 이지케어 「2.수급자 > 2.10 현금영수증 발급목록」 + 「현금영수증 발급정보 관리」(목록+수급자별 NTS 상세) = 수급자 모듈 별도 메뉴 ↔ ogada `/billing/reports/receipts` 수납 ledger only·NTS 발급내역 ❌ · FAQ 21716/21717 발급 lifecycle 법적 제약 · BE V157 array CHECK readiness probe @ `45d95ea` · 케어포 3-1 segment nav @ `1d5747d` | **신규 갭 1 G-CASH-RECEIPT-LOG P2「확인」** ROADMAP v3.1 candidate 표 등록 · 케어포 3-1 nav ✅ closure 기록 |
| **BNK-394** | **★ FAQ 21736 사례관리회의록 작성예시(반기·정적 서식)** ↔ ogada G32 **4-계층 superset**(per-attendee opinions + 중복 차단 + 대시보드 due gate + V157 JSONB array CHECK) · V157 commit closure(`8835aa2`·V1–V157 contiguous) | ROADMAP v1.2.1 G32 superset 재입증 · 신규 갭 0 |
| **BNK-397** | **★ func.php module 4 간호급여 10-leaf 전수 cross-walk** ✅7·△3(물리치료 전용·시설 PT out-of-scope)·❌0 = `competitorModuleCoverage.js` `{id:'4',coverage:1}` cross-confirm · ogada 욕창 5-단계 lifecycle·배설/체중/구강 superset 우위 | 신규 갭 0 · COMPETITOR_MATRIX methodology carry |
| **BNK-396** | **★ longterm 502/503/610 게이트 reason 직접 확인**(세션 만료 `refreshedException` 422B + 파라미터 누락 `bKey` JS alert·미확인 4→3) · 8축 교차검증 가정 번복 0 | **신규 candidate G-LTM-DIRECT-SYNC P3「가정·미확인」**(공단 직접 연동 future-work·MVP out-of-scope) ROADMAP v3.1 candidate 등록 |
| **BNK-395** | **★ silverangel 공개 평가지표 PDF 이동서비스 지표40/41**(운전자 자격·차량안전수칙·차량운행표·정적 점검) ↔ ogada G15 별지 제22호 **실데이터 일지 full-stack 우위**(`pickupAddress`/`actualPickupTime`/`companionAccompanied`/`driverSignature`) | 신규 갭 0 · G15 우위 재입증 |
| **BNK-393** | func.php module 8 직원관리 15-leaf + 8-5 사례관리회의록 ↔ G32 superset · 백본 211차 zero drift | 신규 갭 0 · ROADMAP G32 carry |

---

### [PLN] QA 피드백 반영 (2026-06-19, 171차 — BNK-386~392 · TSR 1062~1073차 · QA-B151 Open→Planned · QA Open 0 · QA-B116 Planned · QA-B95 Planned carry)

> **171차 자동 기획 동기화** — BNK-386~392·TSR 1062~1073차. **QA Open 1건(active)** → **QA-B151(backend) Open→Planned 태스크화**(develop→test merge pending 1 @ `b9e0947`·G32 dashboard `caseManagementAttendeeOpinionGapCount` API·**이관 규율 6·7·기능 갭 아님**) · **★ QA-B150 Fixed @ `b272a7b`**(FE G32 per-attendee opinions merge) · **QA-B116 Planned carry**(origin/test push **422 BE+62 FE**·post-merge **1524/1524+1769/1769 PASS**) · **QA-B95 Planned carry**(operation BLOCK·live E2E **123 PASS/19 SKIP**).

| 항목 | 171차 관측 | 조치 |
|------|-----------|------|
| **baseline** | FE develop/test **`e55ae96`** WT **CLEAN** · **SYNCED** · BE develop **`b9e0947`** WT **CLEAN** / test **`5222a8f`** · `test..develop` BE **0 ahead / 1 behind** · origin/test FE **62** · BE **423 unpushed** · FE test **1769/1769 PASS** · BE test **1524/1524 PASS** · live E2E **123 PASS/19 SKIP** · **106 route** · **85 page** · **V1–V156** · **BE Test 209** · **FE test 403** · **모dule 78.28%** | ROADMAP CURRENT BASELINE 171차 갱신 |
| **BNK-386~392** | **★ G32 FAQ21797 6/6 full-stack closure** — per-attendee `attendeeOpinions[]` @ `b272a7b`/`5222a8f` + V156 `attendee_opinions JSONB` + dashboard due gate @ `e55ae96`/`b9e0947` · **★ V155→V156 migration 정정** · **★ BNK-391** silverangel 지표41/42/43 + NHIS #44 3축 · **★ evidence** silverangel download list·feeService·LCMS cms 404 · **백본 210차 zero drift** · **신규 갭 0** | ROADMAP v1.2.1 G32 · REQUIREMENTS §1-5 · USER_STORIES US-T07 |
| **QA** | **Open 0(active)** · **QA-B151 Planned** · **QA-B116 Planned** · **QA-B95 Planned carry** | QA_FEEDBACK Open→Planned · ROADMAP 171차 P0 |
| **merge gate** | **485 vs origin/test**(62 FE+423 BE) · **FE SYNCED** · **BE merge pending 1** · cross-stream **BLOCK(BE only)** | ROADMAP merge_status pending(BE merge) · operation BLOCK |
| **잔여 P0** | **tester BE merge(1)** @ `b9e0947` → **origin/test push(422 BE+62 FE)** → **QA-B116 post-merge** → **QA-B95 operation 승격** · **P3 carry** G39 7일 due-date·G-CHANGE-REASON-AUDIT·G-CASH-RECEIPT·longterm 610 미확인 | ROADMAP v1.2.1·v2 갱신 |

**coder/ops 다음 액션 (171차)**: ① **tester BE merge(1)** @ `b9e0947` → post-merge `mvn test` PASS ② **origin/test push**(422 BE+62 FE) ③ **QA-B116 post-merge 재확인** ④ **QA-B95** operation 승격(`./scripts/run-live-e2e.sh` full criteria).

---

### [BNK] BNK-386~392 인사이트 (2026-06-19) — ★ G32 FAQ21797 6/6 full-stack closure · dashboard attendee-opinion due gate · V156 정정

| BNK | 핵심 인사이트 | ogada 반영 |
|-----|-------------|-----------|
| **BNK-392** | **★ G32 attendee-opinion gap 대시보드 계층 확장** — BE `caseManagementAttendeeOpinionGapCount`(branch/HQ) @ `b9e0947` · FE `dashboardSummary.js` @ `e55ae96` = **회의 폼 + 대시보드 due gate 2-계층 superset** · **V155→V156 자체 정정** | ROADMAP G32 ✅+ · US-T07 · merge gate +1 |
| **BNK-391** | **★ G32 per-attendee opinions full-stack closure** — FAQ21797 「참가 직원별 의견 필수」5/5 @ `b272a7b`/`5222a8f` · 엔젤 지표43「분기·2인」 vs ogada「반기·3인+opinions」**superset** | REQUIREMENTS G32 · COMPETITOR_MATRIX |
| **BNK-390~391** | ezCare FAQ 21797 cross-walk · silverangel download list(공단 평가지표 PDF 3종) · feeService CMS 마케팅 · LCMS `/service/cms.do` 404 | P3 carry · 벤치마크 evidence |
| **BNK-386~389** | G21 live-e2e·G39 FAQ21817 carry · 백본 210차 zero drift · **4축 번복 0** · **신규 갭 0** | ROADMAP baseline carry |

---

### [PLN] QA 피드백 반영 (2026-06-19, 170차 — BNK-381~385 · TSR 1050~1061차 · QA-B148/B149 Open→Planned · QA Open 0 · QA-B116 Planned(origin/test push 417 BE+54 FE) · QA-B95 Planned carry)

> **170차 자동 기획 동기화** — BNK-381~385·TSR 1050~1061차. **QA Open 2건(active)** → **QA-B149(frontend)+QA-B148(backend) Open→Planned 태스크화**(develop WT dirty-tree·`VisitBatchConfirmPanel` loading guard / `LiveE2eBootstrapService` branch-scoped G21 seed readiness WIP 미커밋·**이관 규율 5·6·7 위반·기능 갭 아님**·QA-B142/B145/B147 lineage recurrence) · **QA-B116 Planned carry**(origin/test push **417 BE+54 FE**·post-merge **1756/1756+1518/1518 PASS**·local test 브랜치 CLEAN) · **QA-B95 Planned carry**(operation BLOCK·live E2E **123 PASS/19 SKIP**).

| 항목 | 170차 관측 | 조치 |
|------|-----------|------|
| **baseline** | FE develop **`0002943`** WT **DIRTY 2M** / test **`0002943`** WT **CLEAN** · `test..develop` **0 ahead** · BE develop **`7898aa5`** WT **DIRTY 2M** / test **`7898aa5`** WT **CLEAN** · `test..develop` **0 ahead** · origin/test FE `@ab4de83`(**54 unpushed**) · BE `@598d108`(**417 unpushed**) · FE test **1756/1756 PASS** · BE test **1518/1518 PASS** · live E2E **123 PASS/19 SKIP** · **106 route** · **85 page** · **V1–V155** · **BE Test 209** · **FE test 402** · **모dule 78.28%** | ROADMAP CURRENT BASELINE 170차 갱신 |
| **BNK-381~385** | **★ BNK-385** 본인부담금 **7단 업무흐름도**(①청구생성→②명세/발송→③입금→④미납→⑤청구시작→⑥리포트→⑦의료비공제·통계) **7/7 ✅ parity** + `claimGenerationBasis` parity·func **107-leaf**/demo 107 loadPage·109=107+2 해소 · **★ BNK-384** FAQ21817 **상태변화 기록지 주1회 7일**(이지케어 3-FAQ 트리니티 완성: 21816 주간+21817 상태변화+21818 RFID 월간)·ogada 7-필드 **✅ 7/7** · **★ BNK-382** 백본 3종 zero drift(NHIS #44 202차·func.php 200차·silverangel essential 202차) · **4축 번복 0** · **신규 갭 0** | ROADMAP v2 G21/G39 · REQUIREMENTS §1-5 · USER_STORIES US-V05 |
| **QA** | **Open 0(active)** · **QA-B148/B149 Open→Planned** · **QA-B116 Planned** · **QA-B95 Planned carry** | QA_FEEDBACK Open→Planned · ROADMAP 170차 P0 |
| **merge gate** | **471 vs origin/test**(54 FE+417 BE) · **develop WT DIRTY 2M 양쪽**(test 브랜치 CLEAN·`test..develop` 0 ahead) · **cross-stream BLOCK(FE+BE develop dirty)** | ROADMAP merge_status pending(develop dirty) · operation BLOCK |
| **잔여 P0/P2/P3** | **COD QA-B148/B149 commit→push develop** → **tester 재검증·merge** → **origin/test push(417 BE+54 FE)** → **QA-B116 post-merge** → **QA-B95 operation 승격** · **P2 carry** G21 FE `nhisComparisonSummary` StatCard wire · **P3 carry** G39 weekly-manual 7일 due-date 알림·RFID 특이사항→별지 동치 라벨링(BNK-384)·G-CHANGE-REASON-AUDIT·G-CASH-RECEIPT | ROADMAP v2 갱신 |

**coder/ops 다음 액션 (170차)**: ① **COD QA-B149**(`VisitBatchConfirmPanel.jsx`·`.test.jsx` loading guard) + **QA-B148**(`LiveE2eBootstrapService.java`·`.test.java` branch-scoped G21 seed readiness) **commit→push develop**(완료 단위 커밋·working tree clean) ② **tester 재검증·develop→test merge** ③ **origin/test push**(417 BE+54 FE) ④ **QA-B116 post-merge 재확인** ⑤ **QA-B95** operation 승격(`./scripts/run-live-e2e.sh` full criteria).

> **이관 규율 재고지(170차)**: QA-B142→B145→B147→B148→B149는 동일 **develop working tree dirty-tree 재오염** 패턴의 반복으로, **기능 갭이 아니라 이관 규율 5(Fixed↔develop HEAD 검증)·6(완료 단위 develop 커밋)·7(merge 선행 dirty-tree 금지) 미준수**가 유일 블로커다. baseline test 브랜치는 항상 CLEAN·PASS이므로 산출물 자체는 완성 상태 → COD가 완료 단위로 **commit→push** 만 수행하면 즉시 merge·push 가능. 신규 기획·태스크 없음(BNK-381~385 신규 갭 0).

---

### [BNK] BNK-381~385 인사이트 (2026-06-19) — ★ 본인부담 7단 7/7 parity · FAQ21817 3-FAQ 트리니티 · 백본 zero drift · 신규 갭 0

| BNK | 핵심 인사이트 | ogada 반영 |
|-----|-------------|-----------|
| **BNK-385** | 케어포 매뉴얼 PDF p.84 **본인부담금 7단 업무흐름도**(①청구생성→②명세/발송→③입금→④미납→⑤청구시작→⑥리포트→⑦의료비공제·통계) + 선행입금 가드 + 청구명세서생성기준(9-1=청구내역상세 vs 2-1 일정) ↔ ogada 7-x Route 11/11 + `claimGenerationBasis` 토글 = **7/7 ✅ parity** · func **107 unique leaf**·demo 107 loadPage·「109」=107 operable+2 deprecated 해소 | ROADMAP v2 billing ✅ 재입증 · 신규 갭 0 |
| **BNK-384** | 이지케어 **FAQ21817 상태변화 기록지(요양보호사) 주1회·7일 이내** 작성·RFID 특이사항란=별지 동치 인정 → **이지케어 3-FAQ 트리니티 완성**(21816 주간 4단 + 21817 상태변화 주1회 + 21818 RFID 월간 5단) ↔ ogada `CareServiceWeeklyRecordPage`+`CareServiceSpecialNotesPage` 7-필드 **✅ 7/7 parity** | G39 P3「가정」 — 7일 due-date 알림·RFID 특이사항→별지 동치 라벨링(`### 추가 질문` 신규) |
| **BNK-382~383** | silverangel `system_feature` 정본(`/silverangel/angelsystem/` vs `/newSilverangel/*` 404)·NHIS #44 203차 zero drift·2026 수가(502 74,060·503 50/60%) cross-walk | COMPETITOR_MATRIX methodology carry · G34-APPROVAL P3 carry |
| **BNK-381** | func.php 202차 zero drift·module 7 본인부담 7-x 11/11 Route parity 재입증·demo `view.cost_*` ↔ `/billing/*` cross-walk + 공단 import 범위 초과 우위 | ROADMAP v2 billing 우위 재확인 · 신규 갭 0 |

---

### [PLN] QA 피드백 반영 (2026-06-19, 169차 — BNK-376~380 · TSR 1040~1049차 · ★ QA-B142~B145 Fixed · QA Open 0 · QA-B116 Planned(origin/test push 412 BE+49 FE) · QA-B95 Planned carry)

> **169차 자동 기획 동기화** — BNK-376~380·TSR 1040~1049차. **QA Open 0(active)** · **★ QA-B142 Fixed @ `54d7f36`→`c0403b0`** · **★ QA-B143 Fixed @ `2095985`** · **★ QA-B144 Fixed @ `0915f80`** · **★ QA-B145 Fixed @ `c651b30`/`c0403b0`** · **QA-B116 Planned carry**(origin/test push **412 BE+49 FE**·post-merge **1753/1753+1513/1513 PASS**) · **QA-B95 Planned carry**(operation BLOCK·live E2E **123 PASS/19 SKIP**).

| 항목 | 169차 관측 | 조치 |
|------|-----------|------|
| **baseline** | FE develop/test **`0915f80`** WT **CLEAN** · SYNCED · BE develop/test **`c0403b0`** WT **CLEAN** · SYNCED · origin/test **412 BE+49 FE unpushed** · FE test **1753/1753 PASS** · BE test **1513/1513 PASS** · live E2E **123 PASS/19 SKIP** · **106 route** · **85 page** · **V1–V155** · **BE Test 209** · **FE test 402** · **모dule 78.28%** | ROADMAP CURRENT BASELINE 169차 갱신 |
| **BNK-376~380** | **★ BNK-380** G21 seed readiness **NHIS row-batch linkage ✅** @ `c0403b0` · **★ page 84→85**(73-cycle undercount correction) · **★ BNK-379** silverangel CMS **`/service/` canonical**(`/daycare/`→404) · **★ BNK-378** FAQ21818 RFID 5-step·ezCare schedule-p300·price 9,346 · **백본 3종 zero drift**(NHIS #44 202차·func.php 200차·silverangel essential 202차) · **4축 번복 0** · **신규 갭 0** | ROADMAP v2 G21 · REQUIREMENTS §1-5 · USER_STORIES US-V05 |
| **QA** | **Open 0(active)** · **QA-B142~B145 Fixed** · **QA-B116 Planned** · **QA-B95 Planned carry** | QA_FEEDBACK Planned 갱신 · ROADMAP 169차 P0 |
| **merge gate** | **461 vs origin/test**(49 FE+412 BE) · **local develop=test SYNCED** · **cross-stream SYNCED** | ROADMAP merge_status ready · operation BLOCK(origin/test push+QA-B95) |
| **잔여 P0/P2/P3** | **tester origin/test push(412 BE+49 FE)** → **QA-B116 post-merge** → **QA-B95 operation 승격** · **P2 carry** G21 FE `nhisComparisonSummary` StatCard wire · **P3 carry** G-CHANGE-REASON-AUDIT·G-CASH-RECEIPT·FAQ21818 RFID ledger(out-of-scope) | ROADMAP v1.2.1·v2 갱신 |

**coder/ops 다음 액션 (169차)**: ① **tester origin/test push**(412 BE+49 FE) ② **QA-B116 post-merge 재확인** ③ **QA-B95** operation 승격(`./scripts/run-live-e2e.sh` full criteria).

---

### [BNK] BNK-376~380 인사이트 (2026-06-19) — ★ G21 seed readiness closure · silverangel `/service/` URL · page 85 correction

| BNK | 핵심 인사이트 | ogada 반영 |
|-----|-------------|-----------|
| **BNK-380** | G21 seed readiness **NHIS row-batch linkage** BE closure @ `c0403b0` · page **84→85** = 73-cycle undercount correction(신규 기능 아님) · 백본 3종 zero drift(NHIS #44 202차·func.php 200차·silverangel essential 202차) | ROADMAP v2 G21 ✅ deepen · US-V05 seed readiness closure |
| **BNK-379** | silverangel CMS URLs `/daycare/`→**404** · canonical = **`/service/`** path | COMPETITOR_MATRIX methodology carry · 벤치마크 URL 정본 |
| **BNK-378** | FAQ21818 RFID **월 전송분 5-step workflow** · ezCare schedule-p300 · price oscillation **9,346** | P3 carry(out-of-scope)·RFID ledger reference only |
| **BNK-376~377** | G21 live-e2e harness·bootstrap readiness deepen carry | QA-B95 partial progress(123 PASS/19 SKIP) |

---

### [PLN] QA 피드백 반영 (2026-06-18, 168차 — BNK-368~375 · TSR 1028~1039차 · ★ QA-B141 Fixed(local) · QA-B142/B143 Open→Planned · QA Open 0 · QA-B116 Planned(FE merge pending 1·origin/test push 407 BE+44 FE) · QA-B95 Planned carry)

> **168차 자동 기획 동기화** — BNK-368~375·TSR 1028~1039차. **QA Open 2건(active)** → **QA-B142/B143 Planned 태스크화**(develop WT dirty-tree·이관 규율 6·7·기능 갭 아님) · **★ QA-20260618-B141 Fixed(local)** — unit regression 1743/1743 PASS·미커밋 WIP → **QA-B143** lineage · **QA-B116 Planned carry**(origin/test push **407 BE+44 FE**·FE merge pending **1**·post-merge **1739/1739+1505/1505 PASS**) · **QA-B95 Planned carry**(operation BLOCK·live E2E 122 PASS/19 SKIP).

| 항목 | 168차 관측 | 조치 |
|------|-----------|------|
| **baseline** | FE develop **`28e5525`** WT **DIRTY 2M** · test **`f26e075`** WT **CLEAN** · `test..develop` **0 ahead / 1 behind** · origin/test **44 unpushed** · BE develop/test **`f932fd3`** · BE test **1505/1505 PASS** · FE test **1739/1739 PASS**(@test) · develop HEAD **1743/1743 PASS**(WIP 포함) · live E2E **122 PASS/19 SKIP** · **106 route** · **84 page** · **V1–V155** · **BE Test 209** · **FE test 402** · **모dule 78.28%** | ROADMAP CURRENT BASELINE 168차 갱신 |
| **BNK-368~375** | **★ BNK-372** `VisitNhisComparisonPanel` standalone @ `797c529` · **★ BNK-374** FAQ21820 월금액 재산정 4단(재가 out-of-scope carry) · **★ BNK-375** silverangel essential 이동서비스 **정적 수칙 점검표** ↔ ogada G15 **실데이터 일지 full-stack 우위** · NHIS #44 **199차 zero drift** · **★ G41** filter-year validation @ `28e5525` · **4축 번복 0** · **신규 갭 0** | ROADMAP v2 G21 · REQUIREMENTS §1-5 G15/G21 · USER_STORIES US-V05/US-T05 |
| **QA** | **Open 0(active)** · **QA-B142/B143 Planned** · **QA-B141 Fixed(local)** · **QA-B116 Planned** · **QA-B95 Planned carry** | QA_FEEDBACK Open→Planned · ROADMAP 168차 P0 |
| **merge gate** | **451 vs origin/test**(44 FE+407 BE) · **FE merge pending 1** · **cross-stream BLOCK**(양쪽 WT DIRTY 2M) | ROADMAP v1.2.1 merge_status pending · operation BLOCK |
| **잔여 P0/P1/P2** | **COD QA-B142/B143 commit→push** → **tester FE merge(1)** → **origin/test push(407 BE+44 FE)** → **QA-B116 post-merge** → **QA-B95** · **P2 carry** G21 FE `nhisComparisonSummary` StatCard wire · **P3 carry** G-CHANGE-REASON-AUDIT·G-CASH-RECEIPT·RFID 270분 hint | ROADMAP v1.2.1·v2 갱신 |

**coder/ops 다음 액션 (168차)**: ① **COD QA-B142**(`LiveE2eBootstrapService*` org-scoped ID resolution) + **QA-B143**(`CareNursingServiceReportPage`·`CareServiceSpecialNotesPage` test stabilization) **commit→push** ② **tester FE merge(1)** ③ **origin/test push**(407 BE+44 FE) ④ **QA-B116 post-merge** ⑤ **QA-B95** operation 승격.

---

### [BNK] BNK-372~375 인사이트 (2026-06-18) — ★ G21 standalone NHIS panel · silverangel G15 우위 · live-e2e bootstrap deepen

| BNK | 핵심 관측 | 기획 반영 |
|-----|----------|----------|
| **BNK-372** | **★ G-SCHEDULE-FIX-LTM-COMPARE FE standalone closure** — `VisitNhisComparisonPanel` on visits page @ `797c529` + BE live-e2e NHIS import batch seed @ `b73e5f4` = ezCare `chk-ltm-fix` **능동 reconcile UX ✅+** | ROADMAP v2 G21 · REQUIREMENTS G-SCHEDULE-FIX-LTM-COMPARE · USER_STORIES US-V05 |
| **BNK-373~374** | 케어포 module 6 위생·안전 coverage 0 baseline cross-confirm · FAQ21820 **월금액 재산정**(공단 포털·재가 out-of-scope) · schedule-rfid 270분 엑셀 오류 formatter **P3 carry** | REQUIREMENTS P3 carry · PLAN_NOTES 추가 질문 |
| **BNK-375** | **★★ silverangel essential 이동서비스 평가지표 verbatim** — 정적 수칙 점검(운전자 자격·동승자·차량안전·차량운행표) ↔ ogada G15 **별지 제22호 input+print+export 3축 full-stack** = **운영 데이터 일지 우위** · NHIS #44 199차 zero drift · **신규 갭 0** | ROADMAP v1.3-C G15 carry ✅ · REQUIREMENTS §1-5 G15 · USER_STORIES US-T05 |

---

### [PLN] QA 피드백 반영 (2026-06-18, 167차 — BNK-362~367 · TSR 1016~1027차 · QA Open 0 · QA-B116 Planned(FE SYNCED·origin/test push 38 FE+402 BE·BE merge pending 1) · QA-B95 Planned carry)

> **167차 자동 기획 동기화** — BNK-362~367·TSR 1016~1027차. **QA Open 0건(active)** — 신규 Open→Planned 태스크화 **불요**(직전 사이클 QA-B137/B138 이미 Fixed·이번 TSR 1016~1027 사이클 신규 BLOCK 0). **QA-B116 Planned carry**(FE develop=test **SYNCED** @ `f232285`·post-merge **1723/1723+1498/1498 PASS**·origin/test push **38 FE+402 BE**·BE local merge pending **1**) · **QA-B95 Planned carry**(operation BLOCK·live E2E 122 PASS/19 SKIP).

| 항목 | 167차 관측 | 조치 |
|------|-----------|------|
| **baseline** | FE develop/test **`f232285`** SYNCED · **0 ahead** local · origin/test **38 unpushed** · WT **CLEAN** · BE develop **`8a8c5b3`** · test **`03a052a`** · `test..develop` **0 ahead / 1 behind**(merge pending 1) · origin/test **402 unpushed** · BE test **1498/1498 PASS** · FE test **1723/1723 PASS**(★ FE test files 402·+7 vs 166차 395) · live E2E **122 PASS/19 SKIP** · **106 route** · **84 page** · **V1–V155** · **BE Test 209** · **모dule 78.28%** | ROADMAP CURRENT BASELINE 167차 갱신 |
| **BNK-362~367** | **★ G21 batch-confirm readiness full-stack closure**(△→✅·BNK-365) — readiness PLAN/BILLING split + per-kind ready/block-unassigned @ `f26abb0`/`5f710e3` + FE wire @ `f9ed97d` · **★ G-SCHEDULE-FIX-LTM-COMPARE P3 candidate → BE closure(✅·BNK-366~367)** — `GET /visits/nhis-comparison` 4종 분류 @ `03a052a` + `nhisComparisonSummary` readiness embed @ `8a8c5b3`(FE summary wire △ P2) · **★ G-7-1-PRINT-BUNDLE ✅+**(BNK-363~364) — `BillingStatementPrintPanel` @ `50d330d` + 미납 영수증 제외 라벨 @ `f5639df`(엑셀다운로드 ❌ P3) · **★ 신규 candidate G-CHANGE-REASON-AUDIT P3「가정」**(`change-list` field-level diff·BNK-362) · **4축 번복 0** · **백본 zero drift** · **신규 갭 candidate 1·가정 번복 0** | ROADMAP v2 G21 완료 기준 · REQUIREMENTS §1-5 G21/G-SCHEDULE-FIX-LTM-COMPARE/G-7-1-PRINT-BUNDLE/G-CHANGE-REASON-AUDIT · USER_STORIES US-V05 |
| **QA** | **Open 0(active)** · **QA-B116 Planned** · **QA-B95 Planned carry** | QA_FEEDBACK Open/Planned note 167차 · ROADMAP 167차 P0 |
| **merge gate** | **FE SYNCED** · **BE 1 ahead** local · **440 vs origin/test**(38 FE+402 BE) · post-merge PASS | ROADMAP v1.2.1 merge_status ready · operation = BE merge + push |
| **잔여 P0/P1/P2** | **tester BE merge(1)** + **origin/test push(38 FE+402 BE)** → **QA-B116 post-merge** → **QA-B95**(`npm run test:live-e2e` PASS) · **P2 carry** G21 FE `nhisComparisonSummary` StatCard wire·G-7-1 엑셀다운로드 · **P3** G-CASH-RECEIPT·G-STAFF-WORKLOG·G-CHANGE-REASON-AUDIT·G-PERIODIC-OBLIGATION-CALENDAR carry | ROADMAP v1.2.1·v2 갱신 |

**coder/ops 다음 액션 (167차)**: ① **tester BE merge(1)** ② **origin/test push**(38 FE+402 BE) ③ **QA-B116 post-merge** 재확인 ④ **QA-B95** — `npm run test:live-e2e` 표준 명령 **PASS**·operation 승격 ⑤ **P2 carry** — G21 `VisitBatchConfirmPanel`에 `readiness.nhisComparisonSummary` matched/discrepancy/missing/extra StatCard wire(별도 `fetchVisitNhisComparisonApi` 호출 불필요 — BE `8a8c5b3` 설계 의도).

---

### [BNK] BNK-368~371 인사이트 (2026-06-18) — ★ G21 `nhisComparisonSummary` FE wire full-stack closure · NHIS #44 러-1~4 196차 zero drift · silverangel 4종 zero drift · lcms CJ프레시웨이 MOU 식단표

| BNK | 핵심 관측 | 기획 반영 |
|-----|----------|----------|
| **BNK-368** | **4축 교차검증 번복 0**(G14 △·대시보드/G26 ✅·v1.3-C ✅·v2 CMS ✅) · G21 RFID no-diff success alert @ `f232285`(「차이 없습니다」) = ezCare schedule-rfid UX ✅+ · 케어포 공지46626 엑셀 import 공식 대체 verbatim 불변 · NHIS #44 194차 zero drift | ROADMAP baseline · REQUIREMENTS G21 |
| **BNK-369** | **★ G21 `nhisComparisonSummary` FE wire full-stack closure(P2 #1 △→✅)** — `VisitBatchConfirmPanel` StatCard 4종(일치/불일치/NHIS누락/일정외NHIS) @ `68a4e35` + BE `4046046` readiness deepen ↔ ezCare `chk-ltm-fix` parity ✅+ · 케어포 PDF p.85 선행입금 가드 ↔ ogada `BillingPage`/`EasyPayPage` 능동 prior-month block UI 우위 | ROADMAP v2 G21 `[x]` · REQUIREMENTS G-SCHEDULE-FIX-LTM-COMPARE |
| **BNK-370** | **★★★ ezCare schedule-rfid `comp_01~09` 8-leaf 전수 ↔ ogada `config/visits.js` `COMP_01~09` cross-walk(comp_02 미사용까지 정합)** — ezCare terse 컬럼 라벨 대비 ogada 의미 명시 라벨 + tone(danger/warning/info/neutral) + 변형 정규화(`comp-4`→`COMP_04`) 우위 = G21 RFID full-stack parity ✅+ · 데모 8종 DRIFT cachebuster/session verbatim 불변 · 도입 9,345개·셋팅 33,000·37명 25,850 verbatim | REQUIREMENTS §1-5 G21 · USER_STORIES US-V05 |
| **BNK-371** | **★★★ NHIS #44 제34조 러-1~4 5-date 개정이력 196차 zero drift(①~⑤ verbatim)** — ④ 「이동서비스 일지 작성·보관」 법정 의무 ↔ ogada **별지 제22호 input+print+export 3축 full-stack closure**(케어포 func 2-x 정적·엔젤 정적 차량운행일지 대비 ④ 우위) · **★★ silverangel 4종 live zero drift**(essential/daycareProgramProvided/extraService/main_service)·이동서비스 이중 트랙 carry · **★ lcms 배너 회전 CJ프레시웨이 MOU 식단표 무상제공** = vendor 제휴 마케팅(SW 기능 아님·식단표 자동작성 MVP out-of-scope·신규 갭 아님) · **★ longterm 502/503·law247 DRIFT cosmetic**(74,060·50/60%·제2025-247호 verbatim·덮어쓰기 4건) · **상태 변경 1**(BNK-370 BE WT 1M→commit·merge 444→446) | ROADMAP v1.3-C G15 `[x]` · REQUIREMENTS §1-5 G15 · USER_STORIES US-T05 · COMPETITOR_MATRIX @HEAD |

**planner 다음 액션 (BNK-368~371)**: ① **tester merge 446**(FE41+BE405·양쪽 WT CLEAN) ② `workspace_baseline.yaml` 정정(FE `@ad18606`·ahead 41·BE `@39fa41a`·dirty true(1M)→**false**·ahead 405·FE test 400·merge 446) ③ **P3 carry** — G-SCHEDULE-FIX-LTM-COMPARE FE summary wire(BNK-369 closure)·G-CHANGE-REASON-AUDIT·G-CASH-RECEIPT·G-PERIODIC-OBLIGATION-CALENDAR ④ **식단표 자동작성·영양사 연계(lcms CJ MOU)는 P3 보류** — vendor 제휴·MVP out-of-scope·신규 갭 아님.

---

### [BNK] BNK-362~367 인사이트 (2026-06-18) — ★ G21 readiness full-stack closure · G-SCHEDULE-FIX-LTM-COMPARE BE ✅ · G-7-1-PRINT-BUNDLE ✅+ · G-CHANGE-REASON-AUDIT P3

| BNK | 핵심 관측 | 기획 반영 |
|-----|----------|----------|
| **BNK-362** | 이지케어 데모 PGID 3종 신규(방문현황 `schedule-p500`·납부내역 `pAmt-a200`·변경사유 `change-list`) — schedule-p500·pAmt-a200 = ogada `/visits`·`/billing/*` parity ✅ · **change-list `chg_before/chg_after/mName` field-level diff** ↔ ogada `AuditLogPanel` action-level only △ → **신규 candidate G-CHANGE-REASON-AUDIT P3「가정」**(MVP out-of-scope) · 도입 9,345 oscillation 폐기 carry | REQUIREMENTS G-CHANGE-REASON-AUDIT P3 · PLAN_NOTES 추가 질문 |
| **BNK-363** | 케어포 PDF p.87 ② 인쇄 산출물(주소라벨지·급여비용명세서·영수증·청구리스트·ALL) ↔ FE `BillingStatementPrintPanel` @ `50d330d` = **G-7-1-PRINT-BUNDLE △→✅+**(발송 패널과 인쇄 패널 분리) · BE `28860ae` G21 PLAN/BILLING split blocker counts deepen | REQUIREMENTS G-7-1-PRINT-BUNDLE · ROADMAP v1.2.1 |
| **BNK-364** | **4축 교차검증 번복 0**(G14 △·대시보드/G26 ✅·v1.3-C ✅·v2 CMS ✅) · G-7-1 미납 claim ALL 인쇄 시 영수증 제외 안내 라벨 @ `f5639df`(honest UX) · 백본 2종 live zero drift | ROADMAP baseline · REQUIREMENTS 백본·G-7-1-PRINT-BUNDLE |
| **BNK-365** | **★ G21 batch-confirm readiness full-stack closure(△→✅)** — `VisitConfirmReadinessResponse` PLAN/BILLING split + `readyPlan`/`readyBilling` per-kind + 미배정 draft 거부 @ `f26abb0`/`5f710e3` ↔ FE wire @ `f9ed97d` · 케어포 func.php module 2(이동서비스/일정) 9-leaf 정적 ↔ ogada 6단 게이트 우위 | ROADMAP v2 G21 · REQUIREMENTS G21 · USER_STORIES US-V05 |
| **BNK-366** | **★ G-SCHEDULE-FIX-LTM-COMPARE P3 candidate → BE in-progress** — ogada BE WT DIRTY `VisitNhisComparison*`(`GET /visits/nhis-comparison`) ↔ ezCare `schedule-fix` `chk-ltm-fix` 「공단 청구명세서와 비교」 1:1 · matched/discrepancy/missing/extra 4종 분류 + per-client `visitDayCount`↔`nhisServiceDays` + 동일 월 guard = 능동 reconcile 우위 | REQUIREMENTS G-SCHEDULE-FIX-LTM-COMPARE · USER_STORIES US-V05 |
| **BNK-367** | **★ G-SCHEDULE-FIX-LTM-COMPARE BE closure(✅ status change)** — `03a052a`(API) + `8a8c5b3`(`nhisComparisonSummary` readiness embed·별도 round-trip 제거) committed·WT CLEAN(잔여 FE summary wire △ P2) · FE G21 RFID diff code variant normalize @ `570912e` · NHIS #44 193차 zero drift | ROADMAP v2 G21 `[x]` · REQUIREMENTS G-SCHEDULE-FIX-LTM-COMPARE BE ✅ |

---

### [PLN] QA 피드백 반영 (2026-06-18, 166차 — BNK-355~361 · TSR 1004~1015차 · QA Open 0 · ★ QA-B137/B138 Fixed · QA-B116 Planned(FE SYNCED·origin/test push 31 FE+396 BE·BE merge pending 1) · QA-B95 Planned carry)

> **166차 자동 기획 동기화** — BNK-355~361·TSR 1004~1015차. **QA Open 0건(active)** — **★ QA-20260618-B137 Fixed @ `4a112fe`**(FE develop/test 불일치) · **★ QA-20260618-B138 Fixed @ `94c65e2`**(live-e2e guardian credential fallback — TSR 1013차 Open BLOCK 등장 → 1015차 Fixed verified·develop→test merge EXECUTED, **신규 Open→Planned 태스크화 불요**: tester 사이클 내 발견·해소) · **QA-B116 Planned carry**(FE develop=test **SYNCED** @ `94c65e2`·post-merge **1699/1699+1491/1491 PASS**·origin/test push **31 FE+396 BE**·BE local merge pending **1**) · **QA-B95 Planned carry**(operation BLOCK).

| 항목 | 166차 관측 | 조치 |
|------|-----------|------|
| **baseline** | FE **`94c65e2`** · test **`94c65e2`** · **0 ahead** local · origin/test **31 unpushed** · WT **CLEAN** · BE develop **`72124f7`** · test **`8cf09d8`** · **1 ahead** local · origin/test **396 unpushed** · BE test **1491/1491 PASS** · FE test **1699/1699 PASS** · live E2E **122 PASS/19 SKIP** · **106 route** · **84 page** · **V1–V155** · **BE Test 209** · **FE test 395** · **모dule 78.28%** | ROADMAP CURRENT BASELINE 166차 갱신 |
| **BNK-355~361** | **★★★ G15 별지 제22호(이동서비스 일지④) input+print+export 3-축 full-stack closure → P2 Must ✅ CLOSED** @ `a1d6e32`(print layout)/`7de5a6f`(input align)/`07be394`·`b1a16ff`·`e358f2d`·`72124f7`(input completion+export·direction) — 케어포 func 2-x·엔젤 정적 차량운행일지(단일 법정 일지④ 폼 부재) 대비 **우위 확정** · **★ V155 transport waypoint 주소 non-empty CHECK** @ `64c4c80`(V151+V154 패턴 흡수) · **★ PDF p.87 4채널 발송 ↔ G-7-1-4CHANNEL parity ✅ 재확인** · **★ 백본 4종 live zero drift**(NHIS #44 187차·func.php 186차·demo-work·silverangel essential) · **4축 번복 0** · **신규 갭 0·가정 번복 0** | ROADMAP v1.3-C 완료 기준 G15 `[x]` · REQUIREMENTS §1-5 G15 · USER_STORIES US-T05 |
| **QA** | **Open 0(active)** · **QA-B137/B138 Fixed** · **QA-B116 Planned** · **QA-B95 Planned carry** | QA_FEEDBACK Open/Planned note 166차 · ROADMAP 166차 P0 |
| **merge gate** | **FE SYNCED** · **BE 1 ahead** local · **428 vs origin/test**(31 FE+397 BE) · post-merge PASS | ROADMAP v1.2.1 merge_status ready · operation = BE merge + push |
| **잔여 P0/P1/P2** | **tester BE merge(1)** + **origin/test push(31 FE+396 BE)** → **QA-B116 post-merge** → **QA-B95**(`npm run test:live-e2e` PASS) · **P2 Must** 일지④ 인쇄·별지 제22호 전항목 **✅ CLOSED**(잔여 운영 UX polish only) · **P3** G-SCHEDULE-FIX-LTM-COMPARE·G-CASH-RECEIPT·G-STAFF-WORKLOG·G-PERIODIC-OBLIGATION-CALENDAR carry | ROADMAP v1.2.1·v1.3-C·v2 갱신 |

**coder/ops 다음 액션 (166차)**: ① **tester BE merge(1)** ② **origin/test push**(31 FE+396 BE) ③ **QA-B116 post-merge** 재확인 ④ **QA-B95** — `npm run test:live-e2e` 표준 명령 **PASS**·operation 승격 ⑤ **P2 Must 일지④ closure 후속** — 운영 UX polish(감사 trail UI·인쇄 미세조정) Should 수준 carry.

---

### [BNK] BNK-355~361 인사이트 (2026-06-18) — ★★★ G15 별지 제22호 input+print+export 3-축 closure · V155 waypoint CHECK · 백본 4종 zero drift

| BNK | 핵심 관측 | 기획 반영 |
|-----|----------|----------|
| **BNK-355** | **V155** `transport_run_stops` waypoint 주소 **non-empty defense-in-depth CHECK** @ `64c4c80`(V151 stop_kind 분기 + V154 driver signature pair-CHECK 패턴 흡수·additive·CLIENT/BRANCH 영향 0) | ROADMAP v1.3-C · DBA 마이그레이션 lineage |
| **BNK-356~357** | G15 별지 제22호 **print layout**(탑승 장소 컬럼·운전자 서명 인쇄 블록·A4 bordered) @ `a1d6e32` + **input↔print align** @ `7de5a6f` · PDF p.90 청구시작 번호충돌 재확인 | ROADMAP v1.3-C G15 closure |
| **BNK-358~359** | NHIS #44 제34조 러-1~4 **5-date 개정이력 zero drift**(고시 불변) · 엔젤 이동서비스 **이중 트랙**(급여제공+차량운행일지 정적) ↔ ogada **input+export full-stack closure**(기관 연락처·`pickupAddress` export) @ `e358f2d`/`b1a16ff` = **별지 제22호 input+print+export 3-축 closure** | ROADMAP v1.3-C G15 `[x]` · REQUIREMENTS G15 우위 |
| **BNK-360~361** | **4축 교차검증 번복 0**(G14 △·대시보드/G26 ✅·v1.3-C ✅·v2 CMS ✅) · **백본 4종 live zero drift** · **G15 export `direction`(승차/하차) BE deepen** @ `72124f7` · PDF p.87 4채널 발송 ↔ G-7-1-4CHANNEL parity ✅ 재확인 | ROADMAP baseline · REQUIREMENTS 백본 |

---

### [PLN] QA 피드백 반영 (2026-06-18, 165차 — BNK-348~354 · TSR 1000~1003차 · QA Open 0 · QA-B116 Planned(FE SYNCED·origin/test push 25 FE+390 BE·BE merge pending 1) · QA-B95 Planned carry)

> **165차 자동 기획 동기화** — BNK-348~354·TSR 1000~1003차. **QA Open 0건(active)** — **QA-B116 Planned carry**(FE develop=test **SYNCED** @ `caa215f`·post-merge **1690/1690+1485/1485 PASS**·origin/test push **25 FE+390 BE**·BE local merge pending **1**) · **QA-B95 Planned carry**(operation BLOCK).

| 항목 | 165차 관측 | 조치 |
|------|-----------|------|
| **baseline** | FE **`caa215f`** · test **`caa215f`** · **0 ahead** local · origin/test **25 unpushed** · WT **CLEAN** · BE develop **`dac19d3`** · test **`9e050b1`** · **1 ahead** local · origin/test **389 unpushed** · BE test **1485/1485 PASS** · FE test **1690/1690 PASS** · live E2E **122 PASS/19 SKIP** · **106 route** · **84 page** · **V1–V154** · **BE Test 209** · **FE test 395** | ROADMAP CURRENT BASELINE 165차 갱신 |
| **BNK-348~354** | **★ G41 ✅+ deepen** — 대시보드 위젯 @ `9e91e6a` + PDF 8-7 alerts + 8-7-1 export @ `caa215f` · **★ G21 RFID compare ✅ full-stack** @ `27c9de3`/`4a112fe`/`1ca6c19` · **★ G-SCHEDULE-FIX-LTM-COMPARE P3 candidate** · **★ G-CASH-RECEIPT deepen**(`receipt-list`) · **★ carefor module 8** 15-leaf cross-walk · **4축 번복 0** · **신규 갭 0** | REQUIREMENTS §1-5 · USER_STORIES US-S02/S04 · ROADMAP v1.2.1·v2 |
| **QA** | **Open 0(active)** · **QA-B116 Planned** · **QA-B95 Planned carry** | QA_FEEDBACK Planned note 165차 · ROADMAP 165차 P0 |
| **merge gate** | **FE SYNCED** · **BE 1 ahead** local · **415 vs origin/test**(25 FE+390 BE unpushed) | ROADMAP v1.2.1 merge_status ready · operation = BE merge + push |
| **잔여 P0/P1/P2** | **tester BE merge(1)** + **origin/test push(25 FE+390 BE)** → **QA-B116 post-merge** → **QA-B95**(`npm run test:live-e2e` PASS) · **P2 Must** 일지④ **인쇄·별지 제22호 전항목** · **P3** G-SCHEDULE-FIX-LTM-COMPARE·G-CASH-RECEIPT carry | ROADMAP v1.2.1·v1.3-C·v2 갱신 |

**coder/ops 다음 액션 (165차)**: ① **tester BE merge(1)** ② **origin/test push**(25 FE+390 BE) ③ **QA-B116 post-merge** 재확인 ④ **QA-B95** — `npm run test:live-e2e` 표준 명령 **PASS**·operation 승격 ⑤ **P2 Must** 일지④ **차량운행표 인쇄·별지 제22호 전항목**.

---

### [BNK] BNK-348~354 인사이트 (2026-06-18) — ★ G41 ✅+ deepen · G21 RFID ✅ full-stack · G-SCHEDULE-FIX-LTM-COMPARE P3

| BNK | 핵심 관측 | 기획 반영 |
|-----|----------|----------|
| **BNK-348~350** | NHIS #44·func.php·silverangel **zero drift carry** · 4축 교차검증 번복 0 | ROADMAP baseline · REQUIREMENTS 백본 |
| **BNK-351~352** | `schedule-rfid` **7-code diff compare** FE+BE+E2E closure @ `27c9de3`/`4a112fe`/`1ca6c19` → G21 **P1→✅** | REQUIREMENTS G21 · ROADMAP v2 · USER_STORIES G21 |
| **BNK-353** | G41 **대시보드 compliance 위젯** @ `9e91e6a` — FAQ21808 미이수 갭 카운트 | REQUIREMENTS G41 · USER_STORIES US-S04 · US-H01 |
| **BNK-354** | G41 **PDF 8-7 mandatory alerts + 8-7-1 report export** @ `caa215f` · **G-CASH-RECEIPT deepen**(`receipt-list`) · **G-SCHEDULE-FIX-LTM-COMPARE P3**(`schedule-fix` `chk-ltm-fix`) · carefor module 8 15-leaf(✅8·△2·❌5) | REQUIREMENTS · USER_STORIES · PLAN_NOTES 추가 질문 |

---

### [PLN] QA 피드백 반영 (2026-06-18, 164차 — BNK-342~347 · TSR 980~991차 · ★ QA-B135 Fixed · QA Open 0 · QA-B116 Planned(merge EXECUTED local·post-merge PASS) · QA-B95 Planned carry)

> **164차 자동 기획 동기화** — BNK-342~347·TSR 980~991차. **QA Open 0건(active)** — **★ QA-B135 Fixed @ `d7f1a9a`**(BE WT dirty 4M→CLEAN·merge EXECUTED) · **QA-B116 Planned carry**(local develop=test **SYNCED**·post-merge **1677/1677+1470/1470 PASS**·origin/test push **18 FE+384 BE**) · **QA-B95 Planned carry**(operation BLOCK).

| 항목 | 164차 관측 | 조치 |
|------|-----------|------|
| **baseline** | FE **`1c8f236`** · test **`1c8f236`** · **0 ahead** local · origin/test **18 unpushed** · WT **CLEAN** · BE **`d7f1a9a`** · test **`d7f1a9a`** · **0 ahead** local · origin/test **384 unpushed** · BE test **1470/1470 PASS** · FE test **1677/1677 PASS** · live E2E **122 PASS/19 SKIP** · **106 route** · **84 page** · **V1–V154** · **BE Test 207** · **FE test 393** · **모dule 78.28%** | ROADMAP CURRENT BASELINE 164차 갱신 |
| **BNK-342~347** | **★ BNK-347** NHIS #44 **175차 zero drift**·엔젤 지표41/42 ↔ G15 **partial+++**·**driver signature full-stack** @ `f51e365`/V154 · **★ BNK-346** `schedule-rfid` **7-code diff matrix** → G21 **P1** · **★ BNK-345** 7-x 본인부담 **11/11+G33 parity**·은행엑셀 8종 · **★ BNK-343~346** legal fields validation·compliance 가이드 @ `b4644e8`/`0df6902` · **4축 번복 0** · **신규 갭 0** | REQUIREMENTS §1-5 G15·G21 · USER_STORIES US-T05 · ROADMAP v1.3-C·v2 |
| **QA** | **Open 0(active)** · **QA-B135 Fixed** · **QA-B116 Planned** · **QA-B95 Planned carry** | QA_FEEDBACK Planned note 164차 · ROADMAP 164차 P0 |
| **merge gate** | **local develop=test SYNCED**(양쪽 WT CLEAN) · **402 vs origin/test**(18 FE+384 BE unpushed) · merge **EXECUTED local**·post-merge PASS | ROADMAP v1.2.1 merge_status ready · operation = push |
| **잔여 P0/P1/P2** | **tester origin/test push(18 FE+384 BE)** → **QA-B116 post-merge 재확인** → **QA-B95**(`npm run test:live-e2e` PASS) · **P2 Must** 일지④ **인쇄·별지 제22호 전항목** · **P1** G21 **RFID 7-code diff matrix** · **P2** 7-3 미납 문자·조정 UI · **P3** K008 payroll out-of-scope | ROADMAP v1.2.1·v1.3-C·v2 갱신 |

**coder/ops 다음 액션 (164차)**: ① **tester origin/test push**(18 FE+384 BE) ② **QA-B116 post-merge** 재확인 ③ **QA-B95** — `npm run test:live-e2e` 표준 명령 **PASS**·operation 승격 ④ **P2 Must** 일지④ **차량운행표 인쇄·별지 제22호 전항목** ⑤ **P1** G21 RFID 7-code diff matrix UI.

---

### [BNK] BNK-342~347 인사이트 (2026-06-18) — ★ G15 partial+++ deepen · G21 RFID 7-code P1 · NHIS #44 175차 zero drift

| BNK | 핵심 관측 | 기획 반영 |
|-----|----------|----------|
| **BNK-342~344** | NHIS #44 **러-1~4 carry**·175차 zero drift·4축 교차검증 번복 0 | ROADMAP baseline · REQUIREMENTS G15 |
| **BNK-345** | 7-x 본인부담 **11/11+G33 parity**·은행엑셀 8종·7-3 미납 문자·조정 UI **P2 carry** | REQUIREMENTS G2·G33 · ROADMAP v2 |
| **BNK-346** | 이지케어 `schedule-rfid` colModel **`comp_01`~`comp_09`** → **RFID 7-code diff matrix P1**(hardware RFID 별도) | REQUIREMENTS G21 · ROADMAP v2 · USER_STORIES US-V0x |
| **BNK-347** | 엔젤 지표41/42 ↔ `companionAccompanied`+pickup/dropoff validation·**driver signature full-stack** @ `f51e365`/V154 · 잔여 **인쇄·별지 제22호 전항목 P2 Must** | ROADMAP v1.3-C · US-T05 · REQUIREMENTS G15 |

---

### [PLN] QA 피드백 반영 (2026-06-18, 163차 — BNK-335~341 · TSR 970~979차 · ★ QA-B131/B132/B133 Fixed · QA Open 0 · QA-B116 Planned(merge EXECUTED local·origin/test push pending) · QA-B95 Planned carry)

> **163차 자동 기획 동기화** — BNK-335~341·TSR 970~979차. **QA Open 0건(active)** — **★ QA-B131 Fixed @ `8882d9f`** · **★ QA-B132 Fixed @ `101aaee`** · **★ QA-B133 Fixed @ `40d4284`** · **QA-B116 Planned carry**(local develop=test **SYNCED**·origin/test push **12 FE+379 BE**·post-merge 재검증) · **QA-B95 Planned carry**(operation BLOCK).

| 항목 | 163차 관측 | 조치 |
|------|-----------|------|
| **baseline** | FE **`38642e2`** · test **`38642e2`** · **0 ahead** local · origin/test **12 unpushed** · WT **CLEAN** · BE **`40ef105`** · test **`40ef105`** · **0 ahead** local · origin/test **379 unpushed** · BE test **1463/1463 PASS** · FE test **1670/1670 PASS** · live E2E **122 PASS/19 SKIP** · **106 route** · **84 page** · **V1–V153** · **모dule 78.28%** | ROADMAP CURRENT BASELINE 163차 갱신 |
| **BNK-335~341** | **★ BNK-341** carefor func **`2.이동서비스관리` 10-leaf** ↔ ogada transport 9 route cross-walk·**4-축 우위**(VRP·compliance·service-fees·Kakao)·백본 **170차 zero drift** · **★ BNK-339** FAQ21799 건강검진 parity ✅·**신규직원 1년 이내 서류 △ @ `8e6310a`** · **★ BNK-340** FAQ21710 payroll out-of-scope·K008 P3 · **4축 번복 0** · **신규 갭 0** | REQUIREMENTS §1-5 G15·G-Health · USER_STORIES US-R03·US-T05 · ROADMAP v1.3-C P2 Must |
| **QA** | **Open 0(active)** · **QA-B131/B132/B133 Fixed** · **QA-B116 Planned** · **QA-B95 Planned carry** | QA_FEEDBACK Planned note 163차 · ROADMAP 163차 P0 |
| **merge gate** | **local develop=test SYNCED**(양쪽 WT CLEAN) · **391 vs origin/test**(12 FE+379 BE unpushed) · merge **EXECUTED local** | ROADMAP v1.2.1 merge_status ready · operation = push |
| **잔여 P0/P1/P2** | **tester origin/test push(12 FE+379 BE)** → **QA-B116 post-merge** → **QA-B95**(`npm run test:live-e2e` PASS) · **P2 Must** 일지④ full 법정 입력 · **P2** 신규직원 건강검진 파일함·직원 파일함 스캔 · **P1** RFID·G21 split-view · **P3** G-BANK-TXN-LOOKUP·candidate carry | ROADMAP v1.2.1·v1.3-C·v2·v3.1 갱신 |

**coder/ops 다음 액션 (163차)**: ① **tester origin/test push**(12 FE+379 BE) ② **QA-B116 post-merge** 재검증 ③ **QA-B95** — `npm run test:live-e2e` 표준 명령 **PASS**·operation 승격 ④ **P2 Must** 이동서비스 일지④ full 법정 입력 서식.

---

### [BNK] BNK-335~341 인사이트 (2026-06-18) — ★ carefor transport 10-leaf cross-walk · FAQ21799 신규직원 건강검진 △ · 4축 번복 0

| BNK | 핵심 관측 | 기획 반영 |
|-----|----------|----------|
| **BNK-335~336** | tester BE 372-batch merge closure·V153 G26 deposit index·G30 evidence panel·4축 교차검증 번복 0 | ROADMAP baseline · merge gate 정리 |
| **BNK-337** | G-BANK-TXN-LOOKUP P3 candidate deepen(PGID `w4c-bank.statement`)·transport roster hub planned pickup | REQUIREMENTS P3 candidate · ROADMAP v2 |
| **BNK-338~339** | NHIS #44 **167~168차 zero drift**·FAQ21799 연간 건강검진·FAQ21806 입사 6단 parity·QA-B95 harness deepen | USER_STORIES US-R02/US-R03 · G-Health-8-10 |
| **BNK-340** | FAQ21710 신규개설기관 인건비 지출비율 = **payroll out-of-scope**·cluster 21708–21710 | K008 P3 carry · 신규 갭 아님 |
| **BNK-341** | carefor **`2.이동서비스관리` 10-leaf** ↔ ogada **9 route**·**4-축 우위** 재확인·일지④ full 입력 **P2 Must carry**·백본 170차 zero drift | ROADMAP v1.3-C · US-T05 · REQUIREMENTS G15 |

---

### [PLA] QA 피드백 반영 (2026-06-18, 162차 — BNK-333~334 · TSR 955~969차 · ★ QA-B127~B130 Fixed · ★ QA-B131 Planned · QA Open 0 · QA-B116 Planned(merge 3 FE+1 BE) · QA-B95 Planned carry)

> **162차 자동 기획 동기화** — BNK-333~334·TSR 955~969차. **QA Open 0건(active)** — **★ QA-B127 Fixed @ `ab4de83`** · **★ QA-B128 Fixed @ `2157df5`** · **★ QA-B129 Fixed @ `d68c4bf`** · **★ QA-B130 Fixed @ `7aac550`** · **QA-B131 Planned**(MEDIUM·`npm run test:live-e2e` script path) · **QA-B116 Planned carry**(merge pending **3 FE+1 BE** local·origin/test push **372 BE+2 FE**·post-merge 재검증) · **QA-B95 Planned carry**(operation BLOCK).

| 항목 | 162차 관측 | 조치 |
|------|-----------|------|
| **baseline** | FE **`7d2cb4a`** · test **`b93e098`** · **3 ahead** local · origin/test **2 unpushed** · WT **CLEAN** · BE **`09df8c7`** · test **`92be918`** · **1 ahead** local · origin/test **372 unpushed** · BE test **1457/1457 PASS** · FE test **1654/1654 PASS** @ test · develop HEAD **1654/1654 PASS** · live E2E workaround **122 PASS/19 SKIP** · `npm run test:live-e2e` **FAIL(127)**(QA-B131) · **106 route** · **84 page** · **V1–V152** · **모dule 78.28%** | ROADMAP CURRENT BASELINE 162차 갱신 |
| **BNK-333~334** | **★ BNK-333** func.php **107-leaf** 정본·demo 시설 셸 **이동서비스 0**·케어포 **7-x ↔ ogada Route 1:1 closed**·PDF p.90 청구시작 evidence · **★ BNK-334** silverangel 정본 **6종 URL zero drift**·CMS 3-method **ogada parity**(`/billing/cms`)·이동서비스 **통합 허브**(`/transport/compliance`) vs 엔젤 이중 트랙(정적 차량운행일지) **우위**·NHIS #44 **164차 zero drift**·longterm 4종 cosmetic DRIFT(verbatim 불변) · **가정 번복 1**(silverangel `/service/` 404 probe = URL 추측 오류) · **신규 갭 0** | REQUIREMENTS §1-5 · USER_STORIES · ROADMAP v1.3-C P2 carry |
| **QA** | **Open 0(active)** · **QA-B131 Planned** · **QA-B116 Planned** · **QA-B95 Planned carry** | QA_FEEDBACK Planned note 162차 · ROADMAP 162차 P0 |
| **merge gate** | **FULLY UNBLOCKED**(3 FE+1 BE local·양쪽 WT CLEAN·cross-stream UNBLOCKED) · merge **미실행** | ROADMAP v1.2.1 merge_status BE+FE ready |
| **잔여 P0/P1** | **COD QA-B131**(script path) → **tester merge(3 FE+1 BE)** → **origin/test push** → **QA-B116 post-merge** → **QA-B95**(`npm run test:live-e2e` 표준 명령 PASS) · **P2(최우선)** 일지④ full 법정 입력·desiredBoarding ETA FE wire · **P1** RFID·G21 split-view · **P3** G-STAFF-WORKLOG·G-HOSPITAL-ESCORT·G-CASH-RECEIPT(「 가정」) | ROADMAP v1.2.1·v1.3-C·v2·v3.1 갱신 |

**coder/ops 다음 액션 (162차)**: ① **COD QA-B131** — `src/frontend-test/package.json` `test:live-e2e` → repo root `scripts/npm-test-locked.sh` 경로 정정 ② **tester merge(3 FE+1 BE)** ③ **origin/test push**(372 BE+2 FE) ④ **QA-B116 post-merge** 재검증 ⑤ **QA-B95** — `npm run test:live-e2e` 표준 명령 **PASS** 확인.

---

### [BNK] BNK-333~334 인사이트 (2026-06-18) — ★ carefor 7-x Route 1:1 · silverangel 6종 zero drift · CMS parity · 이동서비스 통합 허브 우위

| BNK | 핵심 관측 | 기획 반영 |
|-----|----------|----------|
| **BNK-333** | func.php **107-leaf** 정본(109 폐기) · demo-work **이동서비스 키워드 0** · 케어포 **7-x ↔ ogada `/billing/*` Route 1:1 closed**(demo 7-10 간편계산기 gap은 ogada `/billing/calculator`로 커버) · PDF p.90 청구시작 금액설정 evidence | REQUIREMENTS G33 carry · ROADMAP baseline |
| **BNK-334** | silverangel 정본 **6종 URL 전수 zero drift**(`/daycare/daycareEssentialWork.do` `c79c1be3` 등) · 초기 `/service/essential.do` 404 = **URL 경로 추측 오류**(가정 자체 번복) · CMS 3-method **extraService.do** ↔ ogada `/billing/cms` **parity** · 이동서비스 **급여제공계획+기관운영 이중 트랙** vs ogada `/transport/compliance` **통합 허브 우위** · NHIS #44 **164차 zero drift** · **신규 갭 0** | REQUIREMENTS §1-5 G2b·G15 · ROADMAP P2 일지④ carry |

---

### [PLA] QA 피드백 반영 (2026-06-17, 161차 — BNK-321~323 · TSR 952~954차 · ★ QA-B127 Planned · ★ QA-B128 Planned · QA Open 0 · QA-B116 Planned(merge 420) · QA-B95 Planned carry · ★ G-STAFF-WORKLOG·G-HOSPITAL-ESCORT P3 candidate · ★ G-CASH-RECEIPT deepen)

> **161차 자동 기획 동기화** — BNK-321~323·TSR 952~954차. **QA Open 0건(active)** — **QA-B127 Planned**(develop HEAD `@188ce71` unit **56 FAIL/1578 PASS**·DateInput/picker partial fix·17 files) · **QA-B128 Planned**(backend develop WT **DIRTY 1M+2U**·V152+TransportSuggestService WIP) · **QA-B116 Planned carry**(merge pending **420**·post-merge 재검증) · **QA-B95 Planned carry**(operation BLOCK).

| 항목 | 161차 관측 | 조치 |
|------|-----------|------|
| **baseline** | FE **`188ce71`** · test **`bf73c4c`** · **53 ahead** · WT **CLEAN** · BE **`73cffc5`** · test **`704478f`** · **367 ahead** · WT **DIRTY 1M+2U** · BE test **1451/1451 PASS** · FE test **1627/1627 PASS** @ test · develop HEAD **56 FAIL/1578 PASS** · live E2E **122 PASS/19 SKIP** · **106 route** · **85 page** · **V1–V151** · **V152 WIP** · **모dule 78.28%** | ROADMAP CURRENT BASELINE 161차 갱신 |
| **BNK-321~323** | **★ BNK-323 G-STAFF-WORKLOG P3 candidate「 가정」**(FAQ21705 전 직종 출퇴근부/근무일지·ogada `LeadCaregiverWorkLogPage`만) · **★ BNK-322 G-HOSPITAL-ESCORT P3 candidate「 가정」**(angelsitter #781 병원동행 시범·주·야간보호형 참여 가능) · **★ BNK-323 G-CASH-RECEIPT deepen**(FAQ21702/21701 수납 연동·2.10 발급목록) · **★ BNK-321** DatePicker/TimeInput+desiredBoarding ETA WIP · NHIS #44 156차 zero drift · **P2 최우선** 일지④ full 입력+ETA wire+V152 commit · **신규 갭 candidate +2· 가정 번복 0** | REQUIREMENTS §1-5 · USER_STORIES · ROADMAP v3.1 P3 |
| **QA** | **Open 0(active)** · **QA-B127 Planned** · **QA-B128 Planned** · **QA-B116 Planned**(merge 420) · **QA-B95 Planned carry** | QA_FEEDBACK Planned note 161차 · ROADMAP 161차 P0 |
| **merge gate** | **merge 420 BLOCK**(53 FE + 367 BE·FE unit FAIL+BE dirty·cross-stream BLOCK) · merge **미실행** | ROADMAP v1.2.1 merge_status BE+FE pending |
| **잔여 P0/P1** | **COD QA-B127**(0 FAIL) → **QA-B128**(WT clean+V152 commit) → **tester merge(420)** → **QA-B116 post-merge** → **QA-B95 full live E2E PASS** · **P2(최우선)** 일지④ full 법정 입력·desiredBoarding ETA FE wire · **P3** G-STAFF-WORKLOG·G-HOSPITAL-ESCORT·G-CASH-RECEIPT(「 가정」) | ROADMAP v1.2.1·v1.3-C·v2·v3.1 갱신 |

**coder/ops 다음 액션 (161차)**: ① **COD QA-B127** — DateInput/picker 잔여 17 FAIL test files → develop HEAD `npm test` **0 FAIL** ② **COD QA-B128** — V152+TransportSuggestService WIP 커밋 → BE WT **CLEAN** ③ **tester merge(420)** ④ **QA-B116 post-merge** 재검증 ⑤ **QA-B95** `./scripts/run-live-e2e.sh` ⑥ **P2** 일지④ full 입력+ETA wire.

---

### [BNK] BNK-321~323 인사이트 (2026-06-17) — ★ G-STAFF-WORKLOG·G-HOSPITAL-ESCORT P3 candidate · G-CASH-RECEIPT deepen · DatePicker/ETA WIP

| BNK | 핵심 관측 | 기획 반영 |
|-----|----------|----------|
| **BNK-321** | DatePicker/TimeInput 도입·desiredBoarding ETA WIP · transport 경유지+ETA full-stack closure carry · **모dule 78.28%** confirm(92.07% 아님) | ROADMAP P2 carry · v2 transport |
| **BNK-322** | **★ G-HOSPITAL-ESCORT P3 candidate「 가정」** — angelsitter #781 장기요양 병원동행 시범·통합재 가기관(주·야간보호형 참여 가능)·2026-07-30 개시 · `MEDICAL_FACILITY` stop+동반 활동 로그 갭 | REQUIREMENTS · USER_STORIES · ROADMAP v3.1 |
| **BNK-323** | **★ G-STAFF-WORKLOG P3 candidate「 가정」** — FAQ21705 1.8 직원 출퇴근부/근무일지·달력·결재라인·빈서식 · **G-CASH-RECEIPT deepen** FAQ21702/21701 · NHIS #44 zero drift · merge **420 BLOCK** | REQUIREMENTS · USER_STORIES · PLAN_NOTES `### 추가 질문` |

---

### [PLA] QA 피드백 반영 (2026-06-18, 160차 — BNK-311~315 · TSR 932~942차 · ★ QA-B121 Fixed @ `0695244` · ★ QA-B122 Fixed @ `f0e52b8` · QA Open 0 · QA-B116 Planned(merge 48) · QA-B95 Planned carry · ★ 신규 갭 candidate G-CASH-RECEIPT P3「가정」)

> **160차 자동 기획 동기화** — BNK-311~315·TSR 932~942차. **QA Open 0건(active)** — **QA-B121 Fixed @ `0695244`**(develop HEAD live E2E **122/122 PASS**·fee-schedule seed + CSV Blob assert closure) · **QA-B122 Fixed @ `f0e52b8`**(backend develop WT clean 복구·`LiveE2eBootstrapService` recurrence closure) · **QA-B116 Planned carry**(develop `@0baabe9` WT CLEAN·**merge pending 48 commits**·unit **1509/1509 PASS**·post-merge `npm test`+live E2E 재검증) · **QA-B95 Planned carry**(live E2E SKIP→partial RUN·operation BLOCK).

| 항목 | 160차 관측 | 조치 |
|------|-----------|------|
| **baseline** | FE **`0baabe9`** · test/origin/test **`7106106`** · **48 ahead** · WT **CLEAN** · BE **`f0e52b8`** · test **`598d108`** · **362 ahead** · WT **CLEAN** · BE test **246/246 PASS** · FE test **1509/1509 PASS** @ test · develop `@0baabe9` live E2E **122/122 PASS** · live E2E @test **3 FAIL/109 PASS/25 SKIP**(구버전 harness·post-merge closure) · **106 route** · **84 page**(@ develop) · **V1–V149** | ROADMAP CURRENT BASELINE 160차 갱신 |
| **BNK-311~315** | **★ BNK-315 신규 갭 candidate G-CASH-RECEIPT P3「가정」**(FAQ21700 본인부담금 현금영수증 발급·취소·발행내역 전용 메뉴·수납 동시 발급·연락처 기반 발급번호 ↔ ogada billing 수납등록 ✅·`현금영수증`/`cashReceipt` **grep 0건 = ❌**·세무 연동 실재하나 MVP 범위 밖) · **★ BNK-314 4축 교차검증(G14·대시보드·v1.3-C·v2 CMS) 가정 번복 0**·`TransportPage.test.jsx` 회귀 해소 · **★ BNK-313/314 FAQ21792 2026 계약/근로계약서·FAQ21779 지정갱신제·BNK-312 silverangel privacyPolicy 효성CMS** = G2b/G14/G-APPRAISAL 근거 강화(신규 갭 아님) · **★ G14 NHIS plan generation(10필드) P2 carry** · **★ 백본 4종 zero drift**(NHIS #44·func.php 107 leaf·silverangel essential·ezCare fnc DRIFT cachebuster only)·이지케어 도입 9,342 oscillating noise 23회 폐기 · **가정 번복 0·신규 갭 candidate 1·상태 변경 1·미확인 1** | REQUIREMENTS §1-5 G-CASH-RECEIPT · USER_STORIES G-CASH-RECEIPT · ROADMAP v3.1 P3 · COMPETITOR_MATRIX @HEAD |
| **QA** | **Open 0(active)** · **QA-B121 Fixed @ `0695244`** · **QA-B122 Fixed @ `f0e52b8`** · **QA-B116 Planned**(merge pending 48) · **QA-B95 Planned carry** | QA_FEEDBACK Planned note 160차 · ROADMAP 160차 P0 |
| **merge gate** | BE+FE **FULLY UNBLOCKED** · ★ **cross-stream merge FULLY UNBLOCKED** · **merge pending 410**(362 BE + 48 FE·양쪽 WT CLEAN) · merge **미실행** | ROADMAP v1.2.1 merge_status BE+FE ready |
| **잔여 P0/P1** | **tester merge(410)** → **QA-B116 post-merge `npm test`+live E2E 재검증** → **QA-B95 full live E2E PASS**(`./scripts/run-live-e2e.sh`·operation 승격) · **P1** RFID 하드웨어·듀얼패널 split-view·G21 split-view · **P2(최우선)** 이동서비스 일지④ **full 법정 입력 서식**·G14 NHIS plan generation(10필드)·G15 일지④ **인쇄·보관 UX**·G34 전자결재 · **P3** **G-CASH-RECEIPT(신규 candidate)**·G-COGNITIVE-WORKSHEET(=G29)·K008 payroll·G-APPRAISAL | ROADMAP v1.2.1·v1.3-C·v2·v3.1 갱신 |

**coder/ops 다음 액션 (160차)**: ① **tester merge(410)**(양쪽 WT CLEAN·QA-B121/B122 closure·즉시 가능) ② **QA-B116 post-merge** — develop→test merge 후 `npm test -- --run` **PASS @ test HEAD** + live E2E 재검증 ③ **QA-B95** — `./scripts/run-live-e2e.sh` **full PASS**(operation 승격 선행) ④ **P2(최우선)** 이동서비스 일지④ full 법정 입력 서식(`TransportCompliancePage` guide level)·G14 NHIS plan generation ⑤ **P3 검토** G-CASH-RECEIPT 본인부담금 현금영수증(승격 아님·「가정」 backlog).

---

### [BNK] BNK-311~315 인사이트 (2026-06-18) — ★ G-CASH-RECEIPT P3 candidate · 4축 교차검증 가정 번복 0 · 백본 zero drift

| BNK | 핵심 관측 | 기획 반영 |
|-----|----------|----------|
| **BNK-311~312** | FAQ21790 stub·ezCare RFID/중복일정/듀얼모니터 운영 UX carry · silverangel privacyPolicy **효성CMS** 3-method(자동이체·카드·가상계좌·1600-6859) = G2b 근거 강화 · NHIS #44 단일 개정일(2025-07-01) 러-1~4 50%·④ 일지 의무 재확인 · 신규 갭 0 | carry · REQUIREMENTS G2b · ROADMAP baseline |
| **BNK-313** | **FAQ21792** 2026 근로계약서(시급제)·장기요양급여제공 계약서/변경/표준 양식 일괄출력 가이드 = 계약/서식 운영 근거(신규 갭 아님) · `TransportPage.test.jsx` 1 fail 관측(→314 해소) | carry · G14 |
| **BNK-314** | **4축 교차검증(G14·대시보드·v1.3-C·v2 CMS) 가정 번복 0** · `TransportPage.test.jsx` 회귀 해소(상태 변경 1)·`mvn test` 1447 PASS · **FAQ21779 지정갱신제** = G-APPRAISAL out-of-scope(신규 갭 아님) · **G14 NHIS plan generation(10필드 authoritative) P2** | ROADMAP P2 carry · REQUIREMENTS G14 |
| **BNK-315** | **★ 신규 갭 candidate G-CASH-RECEIPT P3「가정」**(FAQ21700 본인부담금 현금영수증·`cashReceipt` grep 0건·수납등록은 있으나 현금영수증 발급 연동 ❌·MVP 범위 밖) · 백본 zero drift·ezCare fnc DRIFT cachebuster only·도입 9,342 oscillating 폐기 · merge **410 FULLY UNBLOCKED** | REQUIREMENTS §1-5 G-CASH-RECEIPT · USER_STORIES G-CASH-RECEIPT · PLAN_NOTES `### 추가 질문` |

---

### [PLA] QA 피드백 반영 (2026-06-18, 159차 — BNK-307~310 · TSR 929~931차 · ★ func 2-9 verification closure · ★ audit trail FE wire full-stack · QA-B121 Planned · QA-B116 Planned(merge 41) · QA-B95 Planned carry)

> **159차 자동 기획 동기화** — BNK-307~310·TSR 929~931차. **QA Open 0건(active)** — **QA-B121 Planned**(live E2E 4 FAIL·FE merge BLOCK) · **QA-B116 Planned carry**(develop `@b48252a` WT CLEAN·**merge pending 41 commits**·unit **1509/1509 PASS**·post-merge 재검증) · **QA-B95 Planned carry**(SKIP→partial RUN·4 FAIL 잔여·operation BLOCK).

| 항목 | 159차 관측 | 조치 |
|------|-----------|------|
| **baseline** | FE **`b48252a`** · test **`7106106`** · origin/test **`7106106`** · **41 ahead** · WT **CLEAN** · BE **`30243f7`** · test **`598d108`** · **357 ahead** · WT **CLEAN** · BE test **246/246 PASS** · FE test **1509/1509 PASS** @ test · live E2E @test **4 FAIL/108 PASS/25 SKIP** · develop live E2E **1 FAIL/121 PASS** · **106 route** · **84 page**(@ develop) · **V1–V148** | ROADMAP CURRENT BASELINE 159차 갱신 |
| **BNK-307~310** | **★ func 2-9 verification closure** — `ClientOutingReportPage`+`clientOutingReportLiveApi.e2e.test.js` @ `3a0110f` = **P2 closed** · **★ G15 audit trail FE wire full-stack** @ `3cc5a08`(BE read @ `5994d15`) · **★ L02 nursing reports live E2E harness** @ BNK-309 · **★ BE actuator liveness/readiness** @ `30243f7` · **가정 번복 0·신규 갭 0** | REQUIREMENTS §1-5 G15 · USER_STORIES US-T05 · ROADMAP v1.3-C |
| **QA** | **Open 0(active)** · **QA-B121 Planned**(P5b·transport timeout·staff CSV Blob×2) · **QA-B116 Planned**(merge pending 41) · **QA-B95 Planned carry** | QA_FEEDBACK Planned note 159차 · ROADMAP 159차 P0 |
| **merge gate** | BE **FULLY UNBLOCKED** · FE **BLOCK**(QA-B121) · ⚠ **cross-stream BLOCK**(FE only) · **merge pending 398**(357 BE + 41 FE) · merge **미실행** | ROADMAP v1.2.1 merge_status BE ready·FE pending |
| **잔여 P0/P1** | **COD QA-B121 live E2E fix** → **tester merge(398)** → **QA-B116 post-merge `npm test` 재검증** → **QA-B95 full live E2E PASS** · **P1** RFID 하드웨어·듀얼패널 split-view·G21 split-view · **P2** 이동서비스 일지④ **full 입력 서식**·G15 일지④ **인쇄·보관 UX**·G34 전자결재 · **P3** G-VOLUNTEER-MGMT·K008 G-Payroll·G-COGNITIVE-WORKSHEET(=G29) | ROADMAP v1.2.1·v1.3-C·v2·v3.1 갱신 |

**coder/ops 다음 액션 (159차)**: ① **COD QA-B121 fix** — P5b fee-schedule live API·staff CSV Blob assert·transport page wait ② **tester merge(398)**(BE ready·FE fix 후) ③ **QA-B116 post-merge** — `npm test -- --run` **PASS @ test HEAD** ④ **QA-B95** — `./scripts/run-live-e2e.sh` **full PASS** ⑤ **P2** 이동서비스 일지④ full 입력 서식(`TransportCompliancePage` guide level).

---

### [PLA] QA 피드백 반영 (2026-06-18, 158차 — BNK-303~306 · TSR 919차 · ★ func 2-7/2-8 full-stack · ★ audit trail read API · QA Open 0 · QA-B116 Planned(merge 34) · QA-B95 Planned carry)

> **158차 자동 기획 동기화** — BNK-303~306·TSR 919차. **QA Open 0건(active)** — **QA-B116 Planned carry**(develop `@8b68fdb` WT CLEAN·**merge pending 34 commits**·post-merge 재검증) · **QA-B95 Planned carry**(live E2E SKIP·operation BLOCK).

| 항목 | 158차 관측 | 조치 |
|------|-----------|------|
| **baseline** | FE **`8b68fdb`** · test **`7106106`** · origin/test **`7106106`** · **34 ahead** · WT **CLEAN** · BE **`6eb9cc0`** · test **`598d108`** · **351 ahead** · WT **CLEAN** · BE test **246/246 PASS** · FE test **1509/1509 PASS** @ test · **106 route** · **84 page**(@ develop) · **V1–V148** | ROADMAP CURRENT BASELINE 158차 갱신 |
| **BNK-303~306** | **★ BNK-304~306 func 2-7/2-8** — BE monthly report read API(`5d27ad3`) → FE `TransportMonthlyReportsPage`(`6a18dfd`) = **full-stack closure** · **★ BNK-306 audit trail read API** @ `5994d15`(FE UI P2) · **★ NHIS #44** 제34조 개정 5-date 불변 · **★ BNK-305 FAQ21768** K008 대체휴무 불가 = payroll P3 carry · **가정 번복 0·신규 갭 0** | REQUIREMENTS §1-5 G15 · USER_STORIES US-T05 · API_SPEC §12 monthly reports·audit trail · ROADMAP v1.3-C |
| **QA** | **Open 0(active)** · **QA-B116 Planned**(merge pending 34) · **QA-B95 Planned carry** | QA_FEEDBACK Planned note 158차 · ROADMAP 158차 P0 |
| **merge gate** | FE+BE **FULLY UNBLOCKED** · **merge pending 385**(351 BE + 34 FE) · merge **미실행** | ROADMAP v1.2.1 merge_status ready |
| **잔여 P0/P1** | **tester merge(385)** → **QA-B116 post-merge `npm test` 재검증** → **QA-B95 bootstrap fix + guardian credentials → `run-live-e2e.sh`** · **P1** RFID 하드웨어·듀얼패널 split-view·G21 split-view · **P2** func **2-9 외출리포트 정합**·G15 일지④ **FE audit UI·인쇄·보관 UX**·G34 전자결재 · **P3** G-COGNITIVE-WORKSHEET(=G29)·K008 G-Payroll·G-GUARDIAN-MEETING | ROADMAP v1.2.1·v1.3-C·v2·v3.1 갱신 |

**coder/ops 다음 액션 (158차)**: ① **tester merge(385)**(양쪽 WT CLEAN·즉시 가능) ② **QA-B116 post-merge** — develop→test merge 후 `npm test -- --run` **PASS @ test HEAD** 확인 ③ **QA-B95** — live-e2e bootstrap fix + guardian credentials → **`./scripts/run-live-e2e.sh`** ④ **P2** func 2-9 `ClientOutingReportPage` cross-walk 점검 · G15 일지④ FE audit UI.

---

### [PLA] QA 피드백 반영 (2026-06-18, 157차 — BNK-298~302 · TSR 898~909 · ★ QA-B120 Fixed · QA-B116 Planned(merge pending 28) · QA-B95 Planned carry · ★ G15 일지④ PUT closure · ★ silverangel CMS 3-method · ★ longterm KRDS DRIFT)

> **157차 자동 기획 동기화** — BNK-298~302·TSR 898~909. **QA Open 0건(active)** — **QA-B120 Fixed @ `af4d7f8`**(live-e2e harness dirty-tree recurrence) · **QA-B116 Planned carry**(develop `@cb30f24` WT CLEAN·**merge pending 28 commits**·post-merge 재검증) · **QA-B95 Planned carry**(live E2E SKIP·backend@8080 UP/500·operation BLOCK).

| 항목 | 157차 관측 | 조치 |
|------|-----------|------|
| **baseline** | FE **`cb30f24`** · test **`7106106`** · origin/test **`7106106`** · **28 ahead** · WT **CLEAN** · BE **`c13800c`** · test **`598d108`** · **346 ahead** · WT **CLEAN** · BE test **246/246 PASS** · FE test **1509/1509 PASS** @ test · **105 route** · **83 page**(@ develop) · **V1–V147** | ROADMAP CURRENT BASELINE 157차 갱신 |
| **BNK-298~302** | **★ BNK-300~302 G15 일지④** — GET export → **PUT persistence+FE 편집 closure live** = **v1.3-C Must 종결 후보**(잔여: 인쇄·보관 UX·감사 trail) · **★ BNK-302 silverangel mainService.do CMS 3-method** ↔ **G2b parity** · **★ BNK-302 longterm KRDS DRIFT** → **V103 seed authoritative** · **★ BNK-301 FAQ21757** G30 방문상담 20min cross-confirm · **★ BNK-298 US-E04 QrCheckinTargetsPanel FE closure** · **가정 번복 0·신규 갭 0** | REQUIREMENTS §1-5 G15·G2b · USER_STORIES US-T05 · API_SPEC §12 service-log · ROADMAP v1.3-C |
| **QA** | **Open 0(active)** · **QA-B116 Planned**(merge pending 28) · **QA-B95 Planned carry** | QA_FEEDBACK Planned note 157차 · ROADMAP 157차 P0 |
| **merge gate** | FE+BE **FULLY UNBLOCKED** · **merge pending 374**(346 BE + 28 FE) · merge **미실행** | ROADMAP v1.2.1 merge_status ready |
| **잔여 P0/P1** | **tester merge(374)** → **QA-B116 post-merge `npm test` 재검증** → **QA-B95 bootstrap fix + guardian credentials → `run-live-e2e.sh`** · **P1** RFID 하드웨어·듀얼패널 split-view · **P2** G15 일지④ 인쇄·보관 UX·감사 trail · G34 전자결재 · **P3** G-COGNITIVE-WORKSHEET(=G29)·G-GUARDIAN-MEETING | ROADMAP v1.2.1·v1.3-C·v2·v3.1 갱신 |

**coder/ops 다음 액션 (157차)**: ① **tester merge(374)**(양쪽 WT CLEAN·즉시 가능) ② **QA-B116 post-merge** — develop→test merge 후 `npm test -- --run` **PASS @ test HEAD** 확인 ③ **QA-B95** — live-e2e bootstrap HTTP 500 fix + guardian credentials(`scripts/dev-live-e2e.env`) → **`./scripts/run-live-e2e.sh`** 재검증(operation 승격 선행) ④ **P1** RFID 하드웨어·듀얼패널 split-view ⑤ **P2** G15 일지④ 인쇄·보관 UX·감사 trail.

---

### [BNK] BNK-298~302 인사이트 (2026-06-18) — ★ G15 일지④ PUT closure · silverangel CMS 3-method · longterm KRDS DRIFT

| BNK | 핵심 관측 | 기획 반영 |
|-----|----------|----------|
| **BNK-298~299** | US-E04 QrCheckinTargetsPanel FE closure · NHIS #44 139차 zero drift carry · merge gate 366→372 | carry · ROADMAP baseline |
| **BNK-300** | **GET `/transport/runs/{runId}/service-log`** export end-to-end closure(별지 제22호) · 일지④ **P2→v1.3-C Must 승격 권고** | USER_STORIES US-T05 · API_SPEC §12 |
| **BNK-301** | FAQ21757 G30 방문상담 20min cross-confirm · ezCare oscillating noise carry · 신규 갭 0 | carry · G30 |
| **BNK-302** | **PUT persistence+FE 편집 closure live**(`aaaeb10`/`7a4b310`) · **silverangel mainService.do CMS 3-method carousel** ↔ G2b · **longterm 502/501/610/503 KRDS DRIFT** → V103 authoritative · **신규 갭 0·가정 번복 0** · merge **374 FULLY UNBLOCKED** | REQUIREMENTS G15·G2b · PLAN_NOTES `### 추가 질문` 일지④ 갱신 |

---

### [PLA] QA 피드백 반영 (2026-06-18, 156차 — BNK-292~297 · TSR 887~897 · ★ QA-B115/B117/B118 Fixed · QA-B116 Planned(merge pending) · QA-B95 Planned carry · ★ BNK-297 이지링크·G-COGNITIVE-WORKSHEET)

> **156차 자동 기획 동기화** — BNK-292~297·TSR 887~897. **QA Open 0건(active)** — **QA-B115 Fixed @ `45bd923`** · **QA-B117 Fixed @ `1d1a71f`** · **QA-B118 Fixed @ `cf6cd70`** · **QA-B116 Planned carry**(develop `1569/1569 PASS` @ `825c6b0`·**merge pending 22 commits**·post-merge 재검증) · **QA-B95 Planned carry**(live E2E SKIP·operation BLOCK).

| 항목 | 156차 관측 | 조치 |
|------|----------|------|
| **baseline** | FE **`825c6b0`** · test **`7106106`** · origin/test **`7106106`** · **22 ahead** · WT **CLEAN** · BE **`8a1f342`** · test **`598d108`** · **342 ahead** · WT **CLEAN** · BE test **246/246 PASS** · FE test **1509/1509 PASS** @ test · develop HEAD **1569/1569 PASS** · **105 route** · **83 page**(@ develop) · **V1–V147** | ROADMAP CURRENT BASELINE 156차 갱신 |
| **BNK-292~297** | **★ BNK-297 FAQ21764 이지링크(EzLink)** — 이지케어 NHIS = **설치형 PC 클라이언트**(구 smartaib4pc) → ogada **web-first + 공단 엑셀 import 차별화 가정 강화** · **★ FAQ21781 인지활동지 출력 시범** → **G-COGNITIVE-WORKSHEET(=G29) P3 candidate** · **★ 백본 zero drift carry**(NHIS #44 138차·func.php·silverangel·Channel.io) · **★ QA-B95 harness deepen** @ `6f2a4eb`/`8a1f342` · **가정 번복 0·신규 갭 candidate 1** | REQUIREMENTS §1-5 G7·G29 · ROADMAP v3.1 P3 · COMPETITOR_MATRIX @HEAD |
| **QA** | **Open 0(active)** · **QA-B116 Planned**(merge pending) · **QA-B95 Planned carry** | QA_FEEDBACK Planned note 156차 · ROADMAP 156차 P0 |
| **merge gate** | FE **ready**(22·WT CLEAN) · BE **ready**(342·WT CLEAN) · ★ **cross-stream merge FULLY UNBLOCKED** · **merge 364** · merge **미실행** | ROADMAP v1.2.1 merge_status 갱신 |
| **잔여 P0/P1** | **tester merge(364)** → **QA-B116 post-merge `npm test` 재검증** → **QA-B95 bootstrap fix + guardian credentials → `run-live-e2e.sh`** · **P1** RFID 하드웨어·듀얼패널 split-view · **P2→v1.3-C Must 검토** transport 법정 일지④ 입력 서식 · **P2** L02 care nav live E2E·G34 전자결재 · **P3** G-COGNITIVE-WORKSHEET(=G29)·G-GUARDIAN-MEETING·K008 G-Payroll | ROADMAP v1.2.1·v1.3-C·v2·v3.1 갱신 |

**coder/ops 다음 액션 (156차)**: ① **tester merge(364)**(양쪽 WT CLEAN·즉시 가능) ② **QA-B116 post-merge** — develop→test merge 후 `npm test -- --run` **PASS @ test HEAD** 확인 ③ **QA-B95** — live-e2e bootstrap HTTP 500 fix + guardian credentials(`scripts/dev-live-e2e.env`) → **`./scripts/run-live-e2e.sh`** 재검증(operation 승격 선행) ④ **P1** RFID 하드웨어·듀얼패널 split-view ⑤ **P2→v1.3-C Must 검토** transport 법정 이동서비스 일지④ 입력 서식.

---

### [BNK] BNK-292~297 인사이트 (2026-06-18) — ★ 이지링크(EzLink) PC 클라이언트 · G-COGNITIVE-WORKSHEET · merge FULLY UNBLOCKED

| BNK | 핵심 | 기획 반영 |
|-----|------|----------|
| **BNK-292~296** | QA-B95 harness deepen·백본 zero drift·transport/ezCare carry · merge gate 360→363 | carry · ROADMAP baseline |
| **BNK-297** | **★ FAQ21764 이지링크(EzLink)** — 공단자료 조회 = **Windows 설치 에이전트**·직원/수급자·방문일정 가져오기 → ogada **web-first + 엑셀 import = PC 에이전트 미의존 차별화 「가정」 강화** · **★ FAQ21781 인지활동지** — 이지케어도 「시범·하반기 확장」 → **G-COGNITIVE-WORKSHEET(=G29) P3 candidate** · ezCare 도입 9,334 oscillating noise 19회 연속 폐기 · merge **364 FULLY UNBLOCKED** | REQUIREMENTS G7·G29 · USER_STORIES G29 · PLAN_NOTES `### 추가 질문` |

---

### [PLA] QA 피드백 반영 (2026-06-17, 155차 — BNK-286~291 · TSR 875~886 · ★ QA-B115/B116/B117 Open→Planned 태스크화(3 BLOCK·dirty-tree+test regression·기능 갭 아님) · QA-B112/B114 Fixed · QA-B95 Planned carry · ★ transport cluster deepen(V143~V146·결정 96) · NHIS #44 이동서비스비 일지④ 의무 · ezCare 계획/청구 2-track+RFID)

> **155차 자동 기획 동기화** — BNK-286~291·TSR 875~886. **QA Open 3건(active BLOCK) → Planned 태스크화 후 Open 0(active)** — **QA-B115**(frontend develop WT DIRTY 20M+1U·transport dispatch cluster WIP)·**QA-B116**(test `@7106106` `MealAssistanceRecordPage` create 1 FAIL·develop fix 미커밋·RE-OPEN)·**QA-B117**(backend develop WT DIRTY 5M·transport+ClientService test WIP)는 **전부 dirty-tree·test regression = 이관 규율 5·6·7 위반(완료 단위 develop 커밋·`npm test`/`mvn test` before commit·Fixed↔HEAD 정합)·기능 갭 아님**(QA-B07/B110/B112/B114 lineage·프로세스 정체) · **QA-B112 Fixed @ `c1f1428`**(TSR 877차)·**QA-B114 Fixed @ `5ebaade`**(TSR 875차) closure 확인 · **QA-B95 Planned carry**(live-e2e bootstrap HTTP 500 + guardian credentials 미설정·operation 잔존).

| 항목 | 155차 관측 | 조치 |
|------|----------|------|
| **baseline** | FE **`d3bef42`** · test **`7106106`** · origin/test **`7106106`** · **15 ahead** · WT **DIRTY 20M+1U**(QA-B115·결정 96) · BE **`114411f`** · test **`598d108`** · **336 ahead** · WT **DIRTY 5M**(QA-B117) · BE test **246/246 PASS** · FE test **1 FAIL/1508 PASS** @ test(QA-B116) · **105 route** · **83 page**(@ develop) · **V1–V146** | ROADMAP CURRENT BASELINE 155차 갱신 |
| **BNK-286~291** | **★ transport cluster deepen 풀스택** — BE V143 `transport_run_stops.stop_kind`(CLIENT/BRANCH 지점 waypoints)·V144 `vehicles.default_driver_id`·V145 `default_driver_name`·V146 `desired_pickup/dropoff_time`+DROPOFF duplicate guard @ `f5b2b42`/`114411f` · FE map pins·`koreanGeocode.js`·driver labels·split-view route editor @ `84e75ec`/`d3bef42`(결정 96-154-1/2/3 closure) · **★ NHIS #44 이동서비스비 러-1~4 verbatim 1차 확인**(편도 50%·1일 1회·**④ 이동서비스 일지 작성·보관 의무**)↔엔젤 지표41/42↔ogada `TransportCompliancePage` = **3-source cross-walk**→**법정 일지④ 입력 서식 P2→v1.3-C Must 승격 검토** · **★ ezCare 계획/청구 2-track + RFID 정산**(Channel.io plan-billing-diff `341309a1`)↔G21 검은/빨간 배지 ✅→**RFID 하드웨어·듀얼패널 split-view P1** · **★ 신규 evidence** angelsitter #766(2026 Q1 Q&A·out-of-scope)·Channel.io plan-billing-diff · **정본 zero drift**(NHIS #44·func.php·silverangel essential·longterm 502 74,060)·ezCare 도입 9,334 oscillating noise 폐기 · **가정 번복 0·신규 갭 0** | REQUIREMENTS §1-5 transport compliance cross-walk · ROADMAP v1.3-C/v2 P1 · COMPETITOR_MATRIX ogada 열 @HEAD |
| **QA** | **Open 0건(active)** · **QA-B115/B116/B117 Planned(BLOCK)** · **QA-B112/B114 Fixed** · **QA-B95 Planned carry** | QA_FEEDBACK Open→Planned 이동 · ROADMAP 155차 P0 태스크화 |
| **merge gate** | FE **ready**(15·⚠ QA-B115/B116 WT clean+test PASS 선행) · BE **ready**(336·⚠ QA-B117 WT clean 선행) · ⚠ **cross-stream merge BLOCK**(FE+BE) · **merge 351** | ROADMAP v1.2.1 merge_status 갱신 |
| **잔여 P0/P1** | **COD ① FE transport WIP(QA-B115)+`MealAssistanceRecordPage.test.jsx` fix(QA-B116) 커밋→`npm test` 1509/1509 PASS @ HEAD→WT clean ② BE transport+ClientService test WIP(QA-B117) 커밋→`mvn test` 246/246 PASS→WT clean ③ tester merge(351) ④ QA-B95 bootstrap fix + guardian credentials → `run-live-e2e.sh`** · **P1** RFID 하드웨어·듀얼패널 split-view·G26 모니터링 근거 표시 일관성 · **P2→v1.3-C Must 검토** transport 법정 이동서비스 일지④ 입력 서식 · **P2** L02 care nav live E2E·G21 plan/claim 분리 UI·8-1 업무분장 블록 · **P3** G34 전자결재·G-GUARDIAN-MEETING(지표27)·시설 module 9 기초설정 cross-walk·K008 G-Payroll(out-of-scope) | ROADMAP v1.2.1·v1.3-C·v2·v3.1 갱신 |

**coder/ops 다음 액션 (155차)**: ① **COD `src/frontend` develop transport dispatch WIP(QA-B115) + `MealAssistanceRecordPage.test.jsx` fix(QA-B116) 완료 단위 커밋 → `npm test -- --run` **1509/1509 PASS** @ develop HEAD → WT CLEAN**(이관 규율 5·6) ② **COD `src/backend` develop transport+`ClientServiceTest.java` WIP(QA-B117) 커밋 → `mvn test` **246/246 PASS** → WT CLEAN** ③ **tester merge(351)**(양쪽 WT clean + test PASS 선행) ④ **QA-B95** — live-e2e bootstrap HTTP 500 fix + guardian credentials(`scripts/dev-live-e2e.env`) → **`./scripts/run-live-e2e.sh`** 재검증(operation 승격 선행) ⑤ **P1** RFID 하드웨어·듀얼패널(계획 vs RFID 태그) split-view ⑥ **P2→v1.3-C Must 검토** transport 법정 이동서비스 일지④ 입력 서식(NHIS #44·지표41).

---

### [BNK] BNK-286~291 인사이트 (2026-06-17) — ★ transport cluster deepen(V143~V146·결정 96) · NHIS #44 일지④ · ezCare 계획/청구 2-track·RFID

| BNK | 핵심 | 기획 반영 |
|-----|------|----------|
| **BNK-286~287** | 정본 zero drift(NHIS #44 러-1~4·func.php 107 leaf·silverangel essential)·BE roster guardian mapping·transport waypoints WIP carry | carry · transport cluster |
| **BNK-288** | FE WT 14M+3U closure live(`b002bb4` roster contact 컬럼+SEC-005 session refactor·`84e75ec` split-view route editor) = **결정 96-154-1/2/3 FE closure** | USER_STORIES US-T·SEC-005 예외 |
| **BNK-289** | 백본 정본 3종 live 재실측 zero drift·BE V143 `transport_run_stops.stop_kind`(지점 waypoints·결정 96-154-1 데이터모델 backstop) WIP | ROADMAP v2/transport |
| **BNK-290** | **★ ezCare 계획/청구 2-track + RFID 정산**(Channel.io plan-billing-diff `341309a1`·「계획=안내용·청구=정산용(RFID 전송·직접입력)」·확정 4단·진한 숫자=정상/적색=재업로드)↔G21 검은/빨간 배지 ✅ · 가격 33,000/25,850·도입 9,334 oscillating noise 폐기(out-of-scope) · BE V143+V144 commit live `f5b2b42` | **RFID 하드웨어·듀얼패널 split-view P1** · ROADMAP v1.3-B/v2 backlog |
| **BNK-291** | **★ NHIS #44 이동서비스비 러-1~4 verbatim 1차 확인**(제34조 5항·편도 50%·1일 1회·수급자 부담 없음·**④ 이동서비스 일지 작성·보관**)↔엔젤 지표41/42(운전자 자격·동승·차량운행표·시간 준수)↔ogada `TransportCompliancePage`·V103 seed·G26 ③ 통계 = **transport compliance 3-source cross-walk 확정** · BE V145+V146 commit live `114411f`(default driver name·desired pickup/dropoff time·DROPOFF guard) · 신규 evidence angelsitter #766(out-of-scope) | **transport 법정 일지④ 입력 서식 P2→v1.3-C Must 승격 검토** · REQUIREMENTS §1-5 |

---

### [USR] 사용자 요청 — 배차·SideNav·인증 plan 변경 기록 (2026-06-17, 154차)

> **배경**: 2026-06-17 세션에서 사용자가 연속 요청한 UX·배차·인증 변경 중, **기존 ROADMAP·USER_STORIES·SEC-005·API_SPEC(c7941e9)과 달라진 부분**을 기록한다. 구현은 `src/frontend`·`src/backend` develop WT 기준(커밋 전).

| # | 영역 | 기존 plan | 사용자 요청·확정 변경 | 구현·문서 반영 |
|---|------|-----------|------------------------|----------------|
| **1** | **배차 메뉴 IA** | `TransportContextNav` — 배차·차량·이동서비스비·외출 등 **이동 하위 분리** · v1.3-B 자동 배차는 별도 화면 후보 | **수동·자동 배차를 동일 `/transport` 페이지**에 통합 — 생성 방식만 다름 · **법정 준수(G15)** 는 `/transport/compliance` 분리 · `/transport/auto-dispatch` → `/transport` 리다이렉트 | `TransportPage.jsx` · `TransportCompliancePage.jsx` · `TransportContextNav.jsx` · `App.jsx` |
| **2** | **`/transport` 섹션 순서** | 초기 UI 셸 — 「운행 조건」카드(날짜·지점) + 명단 + 루트 | ① **운행 루트**(확정·임시 run 목록) **최상단** · 날짜·지점 안내는 루트 카드 내부 · ② **배차 신청 인원 명단** · ③ **자동 배차**(`hq_admin`) · ④ **수동 배차** 생성 버튼 · **「운행 조건」독립 카드 제거** | `TransportPage.jsx` |
| **3** | **명단 연락처 컬럼** | US-T01·`c7941e9` — roster·정차 **`pickupContact`**(픽업 연락처) 노출·마스킹 | 명단 테이블 — **「연락처」**(이용자 `phone`) · **「보호자 연락처」**(대표 보호자 `primaryGuardian` 전화) · **픽업 연락처 컬럼 미표시** · API `pickupContact` **호환 유지** · 정차(`TransportStopList`)는 **기존 `pickupContact` 유지** | BE `TransportRosterItemResponse.contact`·`guardianContact` · FE `TransportPage.jsx` |
| **4** | **`usesTransport` 노출** | DB·API(V47·`1ec538b`)에 **이미 존재** — plan은 ClientForm만 명시 | 이용자 **목록·상세**에 「배차 이용」컬럼·필터·요약 카드 노출(사용자 인지 갭) | `ClientListPage` · `ClientDetailPage` · `clientTransport.js` |
| **5** | **SideNav 비주얼** | US-UX-05 — 5그룹 토글·초기 접힘·`sessionStorage` persist @ `3845f0c` (**기능** 위주) | **그룹 헤더 확대·브랜드 블록·아이콘·좌측 액센트·Linear/Stripe 스타일** · **무한 스크롤 버그** 수정(`html/body/#root overflow:hidden`·`overscroll-behavior`) | `SideNav.jsx` · `sideNavIcons.jsx` · `components.css` · `tokens.css` |
| **6** | **로그인 세션 유지** | SEC-005·`session.js` — JWT **메모리 전용** · 새로고침 시 재로그인 **설계상 동작** · `LoginPage` 「메모리에만 보관」안내 | 새로고침·뒤로가기 후 **같은 탭 로그인 유지** — **refresh token만 `sessionStorage`**(탭 종료 시 삭제) · access token 메모리 · 앱 기동 시 `restoreSession()` | `session.js` · `AuthContext.jsx` · `ProtectedRoute.jsx` |

**결정 96 (154차)**

1. **배차 UX** — 운영 진입점은 **`/transport` 단일 허브**; 자동/수동은 **탭·섹션 분리가 아닌 동일 페이지 내 생성 경로 차이**로만 구분한다. 법정 준수·차량·이동서비스비 등 **컨텍스트 네비 항목은 유지**한다.
2. **명단 PII** — roster **`contact`·`guardianContact`** 는 **`pickupContact`와 동일 마스킹 규칙**(non-HQ `010-****-xxxx`) · `hq_admin`만 `tel:` 링크.
3. **SEC-005 예외** — **access token localStorage/sessionStorage 금지는 유지** · **refresh token `sessionStorage` 허용**(탭 스코프) · httpOnly cookie 전환은 **후속(SEC-D30 후보)**.

**후속 문서·QA**

- [ ] `API_SPEC` §12 roster 필드(`contact`·`guardianContact`) 명시 — **154차 반영**
- [ ] `SECURITY_CHECKLIST` A-3-4 · `FAQ` 로그인 세션 안내 갱신
- [ ] `DESIGN_SYSTEM` §8-2 SideNav 비주얼 deepen(154차 #5)
- [ ] `USER_MANUAL` §1-3 로그인·배차 명단 컬럼

---

---

---

---

---

### [PLA] QA 피드백 반영 (2026-06-17, 153차 — BNK-280~285 · TSR 863~874 · ★ BNK-285 케어포 3-product line·dual-source numbering closure · ★ QA-B113 Fixed @ `b000d92` · QA-B112/B114 Open→Planned · QA-B95 Planned · QA Open 0건(active))

> **153차 자동 기획 동기화** — BNK-280~285·TSR 863~874. **QA Open 2건(active BLOCK) → Planned 태스크화 후 Open 0(active)** · **QA-B113 Fixed @ `b000d92`**(Kakao map SDK preview·dirty-tree closure·직후 QA-B114 재오염) · **QA-B112/B114 Open→Planned**(양쪽 develop WT dirty·merge gate BLOCK) · **QA-B95 Planned carry**.

| 항목 | 153차 관측 | 조치 |
|------|----------|------|
| **baseline** | FE **`b000d92`** · test **`7106106`** · origin/test **`7106106`** · **10 ahead** · WT **DIRTY 5M+4U**(QA-B114) · BE **`7ac0a46`** · test **`598d108`** · **331 ahead** · WT **DIRTY 2M**(QA-B112) · BE test **246/246 PASS** · FE test **1508/1509 PASS**(flakes) | ROADMAP CURRENT BASELINE 153차 갱신 |
| **BNK-280~285** | **★ BNK-285 3-product line**(`intro_si` 11 module·`intro_visit` 8 module·주야간=시설+이동서비스 module 2)·**dual-source numbering closure**(시설 2-4=신체제재↔V131·주야간 2-4=차량관리·demo-work=intro_si 셸) · **★ BNK-283~284 QA-B95 harness deepen** · **★ BNK-280 RFID split-view·L02 care nav pilot E2E** @ `6b34d31` · **가정 번복 0·신규 갭 0** | REQUIREMENTS §1-5 dual-source cross-walk · ROADMAP v1.3-A/v3.1 |
| **QA** | **Open 0(active)** · **QA-B112/B114 Planned** · **QA-B113 Fixed** · **QA-B95 Planned carry** | QA_FEEDBACK Open→Planned 이동 |
| **merge gate** | FE **ready**(10·⚠ QA-B114 WT clean 선행 BLOCK) · BE **ready**(331·⚠ QA-B112 WT clean 선행 BLOCK) · ⚠ **cross-stream merge BLOCK** · **merge 341** | ROADMAP v1.2.1 merge_status 갱신 |
| **잔여 P0/P1** | **COD QA-B112/B114 develop 커밋→WT clean** → **tester merge(341)** → **QA-B95 bootstrap fix + guardian credentials + `run-live-e2e.sh`** · **P1** G26 모니터링 근거·RFID 하드웨어 split-view · **P2** L02 care nav live E2E·transport 법정 일지·G21 plan/claim UI · **P3** 시설 module 9 기초설정 cross-walk(US-O) | ROADMAP v1.2.1·v2·v3.1 갱신 |

**coder/ops 다음 액션 (153차)**: ① **COD `src/backend` `LiveE2eBootstrapService` credential guard WIP 커밋→WT CLEAN**(QA-B112) ② **COD `src/frontend` Kakao map instance refactor(`KakaoBareMap`·`kakaoMapInstance.js`·`useKakaoMap.js`) 커밋→WT CLEAN**(QA-B114) ③ **tester merge(341)**(양쪽 WT clean 선행) ④ **QA-B95** — bootstrap HTTP 500 fix + guardian credentials → **`./scripts/run-live-e2e.sh`** 재검증.

---

### [BNK] BNK-280~285 인사이트 (2026-06-17) — ★ 3-product line · dual-source numbering · QA-B95 harness

| BNK | 핵심 | 기획 반영 |
|-----|------|----------|
| **BNK-280** | RFID split-view pilot E2E·L02 care nav pilot E2E @ `6b34d31`·bootstrap throwable guard @ `f6f1756` | ROADMAP v2 G21 P1 · L02 care nav P2 |
| **BNK-281~282** | 정본 zero drift·ezCare FAQ 21762(크롬 다운로드) out-of-scope | carry |
| **BNK-283~284** | QA-B95 guardian bootstrap·routing E2E commit @ `ec142db`·credential guard WIP @ `7ac0a46` | QA-B112 Planned · QA-B95 carry |
| **BNK-285** | **★ 3-product line** — 주야간=시설+이동서비스 module 2·방문 8 module·inter-product 공유 module 9~11 · **★ dual-source numbering closure** — 시설 `intro_si` 2-4=신체제재(demo-work 정본)·주야간 `daycare` 2-4=차량관리 · ogada L02/L03 deepen = **시설급여 평가지표 코어 차용** | REQUIREMENTS §1-5 cross-walk · PLAN_NOTES `### 추가 질문` |

---

### [PLA] QA 피드백 반영 (2026-06-17, 152차 — BNK-275~279 · TSR 850~862 · ★ QA-B110 Fixed @ `e54a699` · FE develop→test 다중 merge live @ `7106106` · BNK-278 PDF p.92 7-8 통계 leaf 미확인 1→0 · BNK-279 L02_M09/M10/M14 △ partial+ · ★ QA-B95 operation BLOCK 잔존(신규 증상 live-e2e bootstrap HTTP 500·COD Fixed는 tester 미검증) · QA Open 0건(active))

> **152차 자동 기획 동기화** — BNK-275~279·TSR 850~862. **QA Open 0건(active)** · **QA-B110 Fixed @ `e54a699`**(151차 Planned 항목 closure·backend WT clean·`mvn test` 246/246 PASS·merge gate 가드 해소) · **★ QA-B95 operation BLOCK 잔존** — COD가 `liveGlobalSetup` bootstrap fallback을 적용하고 `## Fixed`에 기록했으나 **tester TSR 850~862 live E2E는 여전히 47 suites SKIP**(신규 증상 = `live-e2e bootstrap HTTP 500` + guardian credentials 미설정) → **false Fixed(이관 규율 5)·Planned carry** · **FE develop→test 다중 merge live**(849 `68da0aa` 이후·test 현재 `7106106`·develop `6b34d31` 4 pending).

| 항목 | 152차 관측 | 조치 |
|------|----------|------|
| **baseline** | FE **`6b34d31`** · test **`7106106`** · origin/test **`7106106`** · **4 ahead** · WT **CLEAN** · BE **`f6f1756`** · test **`598d108`** · **326 ahead** · WT **CLEAN** · BE test **246/246 PASS** · FE test **1509/1509 PASS** · FE develop HEAD **1526/1526 PASS** · **103 route**(+3) · **82 page**(+1) · **V1–V142** | ROADMAP CURRENT BASELINE 152차 갱신 |
| **BNK-275~279** | **★ BNK-278 미확인 1→0**(PDF p.92 7-8 통계 leaf·G26 dual-function 1:1 cross-confirm·**G26 통계 ✅ full 확정**·신규 갭 0) · **★ BNK-279 L02_M09/M10/M14 care-scoped nursing reports P2→△ partial+**(care nav E2E deepen 잔여·상태 변경 1) · **★ BNK-277 G21 청구반영 요약 split-view FE closure**(P1 진전)·J03 quiet-hours reject guard · **★ NHIS #44 러-1~4 122~125차 zero drift**(법정 일지 서식 P2 carry) · **★ silverangel system_feature 전자결재 정본 회복**(G34 전자결재 P2·G-GUARDIAN-MEETING 지표27 P3) · **★ 신규 evidence angelsitter #774**(2026 단기보호·가족휴가제 공모·G18-SHORT-PILOT/G-FAMILY-LEAVE P3 deepen) · **★ FAQ 21745/21765 K008 G-Payroll**(payroll out-of-scope·신규 갭 아님) · **가정 번복 0**·**신규 갭 0**·**상태 변경 1**·**미확인 1→0** | REQUIREMENTS §1-5 · ROADMAP v1.2.1/v2 · COMPETITOR_MATRIX ogada 열 @HEAD |
| **QA** | **Open 0건(active)** · **QA-B110 Fixed @ `e54a699`** · **QA-B95 operation BLOCK carry**(tester 미검증 Fixed·신규 증상 bootstrap 500) | QA_FEEDBACK Planned note 152차 · COD Fixed entry에 false-Fixed 경고 추가 |
| **merge gate** | FE **merged** @ `7106106`(+4 ready) · BE **ready**(326·WT CLEAN) · ★ **cross-stream merge FULLY UNBLOCKED** · **merge 330**(326 BE + 4 FE) | ROADMAP v1.2.1 FE `merged` · BE `ready` |
| **잔여 P0/P1** | **BE+FE tester merge(330)**(양쪽 WT CLEAN·즉시 가능) · **★ COD QA-B95 live-e2e bootstrap HTTP 500 fix + guardian credentials 주입 → live E2E 재검증**(operation 승격 선행) · **G26 모니터링 근거 표시 일관성 P1**·**RFID split-view P1** · **L02_M09/M10/M14 care nav E2E P2**·**transport 법정 일지 P2**·**G21 plan/claim 분리 UI P2**·**8-1 업무분장 P2** · **P3** G34 전자결재·G-GUARDIAN-MEETING·G18-SHORT-PILOT/G-FAMILY-LEAVE(#774)·G-STAFF-CHANGE-COUNSEL·K008 G-Payroll·module 8 잔여 | ROADMAP v1.2.1·v2·v3.1 갱신 |

**coder/ops 다음 액션 (152차)**: ① **BE+FE tester merge(330)**(양쪽 WT CLEAN·즉시 가능) ② **★ COD QA-B95 — `live-e2e bootstrap HTTP 500` 원인 수정**(staff token 자동발급 정상화) + **guardian credentials 주입**(`scripts/dev-live-e2e.env` GUARDIAN_* 또는 guardian bootstrap) → **`./scripts/run-live-e2e.sh` 실제 RUN 확인 → tester 재검증**(operation 승격 선행) ③ **P1** G26 모니터링 근거 표시 일관성(G30/G24b/G21 통일)·RFID split-view ④ **P2** L02_M09/M10/M14 care nav E2E·transport 법정 일지 서식·G21 plan/claim 분리 UI·8-1 업무분장 블록.

---

### [PLA] QA 피드백 반영 (2026-06-17, 151차 — BNK-269~274 · TSR 838~849 · ★ G26 ③ 이동서비스비 월별 통계 ✅ full stack(3-function 완성) · FE develop→test MERGED+origin/test PUSH @ `68da0aa` · QA-B110 backend dirty-tree recurrence Open→Planned · QA-B95 Planned · QA Open 0건(active) · 신규 갭 candidate G-STAFF-CHANGE-COUNSEL P3)

> **151차 자동 기획 동기화** — BNK-269~274(G26 ③ 이동서비스비 월별 통계 풀스택 closure·G26 3-function 완성·PDF p.93/p.94 module 8 cross-walk·평가지표 번호 벤더별 상이 확정·정본 4종 zero-drift·ezCare oscillating noise 13회 연속 폐기·vitest full suite 2F flaky)·TSR 838~849. **QA Open 0건(active)** · **QA-B110 Open→Planned**(backend develop `@c5f1325` WT **DIRTY 2M** `VisitService.java`·`VisitServiceTest.java` 재오염·QA-B07 lineage·이관 규율 5·7 위반·test `@598d108` **246/246 PASS** 불변·**기능 갭 아님**) · **QA-B108/B109 Fixed** @ `43d308a`/`14d210c` · **QA-B95 Planned 유지** · **FE develop→test MERGED+origin/test PUSH @ `68da0aa`**(849차·post-merge **1509/1509 PASS**).

| 항목 | 151차 관측 | 조치 |
|------|----------|------|
| **baseline** | FE **`68da0aa`** · test **`68da0aa`** · origin/test **`68da0aa`** · WT **CLEAN** · BE **`c5f1325`** · test **`598d108`** · **320 ahead** · WT **DIRTY 2M**(QA-B110) · BE test **246/246 PASS** · FE test **1509/1509 PASS** · **100 route** · **81 page** · **V1–V142** | ROADMAP CURRENT BASELINE 151차 갱신 |
| **BNK-269~274** | **★ G26 ③ 이동서비스비 월별 통계 ✅ full stack** @ `3672bbe`/`09e4ec17`(G26 **3-function 완성**·결정 95 50회째) · **★ 신규 갭 candidate G-STAFF-CHANGE-COUNSEL P3**(FAQ21795·평가지표19·14일 SLA·「가정」 주야간 적용성 미확인) · **★ module 8 cross-walk**(8-3/8-6/8-8 P3·8-1 업무분장 P2) · **★ G26 모니터링 근거 표시 일관성 P1**(BNK-273) · **★ transport 법정 일지 서식 P2 carry** · **가정 번복 1**(demo L02 rpt 7→6 carry)·**신규 갭 candidate 1**·**미확인 0** | REQUIREMENTS §1-5 · ROADMAP v1.2.1/v2/v3.1 · COMPETITOR_MATRIX ogada 열 @HEAD |
| **QA** | **Open 0건(active)** · **QA-B110 Open→Planned** · **QA-B108/B109 Fixed** · **QA-B95 Planned 유지** | QA_FEEDBACK Open→Planned 이동 · ROADMAP 151차 P0 태스크화 |
| **merge gate** | FE **merged** @ `68da0aa` · BE **ready**(320·⚠ **QA-B110 WT clean 선행 BLOCK**) · ⚠ **cross-stream merge BLOCK**(BE dirty-tree) | ROADMAP v1.2.1 FE `merged` · BE `ready` |
| **잔여 P0/P1** | **COD QA-B110 develop 커밋/정리(WT clean)** → **BE tester merge(320)** · **live E2E env**→**QA-B95 해소** · **G26 모니터링 근거 표시 일관성 P1** · **RFID split-view P1** · **transport 법정 일지 P2** · **G21 plan/claim 분리 UI P2** · **8-1 직원신규등록 업무분장 P2** · **G-STAFF-CHANGE-COUNSEL P3**(적용성 확정 후) · **G-GUARDIAN-MEETING P3** · **module 8 잔여 P3** | ROADMAP v1.2.1·v2·v3.1 갱신 |

**coder/ops 다음 액션 (151차)**: ① **COD `src/backend` develop `VisitService.java`·`VisitServiceTest.java` WIP 완료 단위 커밋/정리 → WT CLEAN**(QA-B110·이관 규율 5·7·기능 갭 아님·`mvn test` 1회 후 커밋) ② **BE tester merge(320)**(WT clean 선행) ③ **`cp scripts/dev-live-e2e.env.example scripts/dev-live-e2e.env`** + credentials + backend `localhost:8080` 기동 → **`./scripts/run-live-e2e.sh`**(QA-B95 해소) ④ **P1** G26 모니터링 근거 표시 일관성(G30/G24b/G21 표기 통일)·RFID split-view ⑤ **P2** transport 법정 일지 서식·G21 plan/claim 분리 UI·8-1 업무분장 블록.

---

### [BNK] BNK-269~274 인사이트 (2026-06-17) — ★ G26 ③ 이동서비스비 통계 full stack · 상담일지 cluster candidate · module 8 cross-walk

| BNK | 핵심 | 기획 반영 |
|-----|------|----------|
| **BNK-269** | **신규 갭 candidate G-STAFF-CHANGE-COUNSEL P3**(FAQ21795 직원변경 상담일지·평가지표19·14일 SLA·A→B(14일 미만)→A 재교체 예외) + 정기 요보사 상담(FAQ21804) = **상담일지 cluster** · 모바일 통합앱(FAQ21760 out-of-scope) · ezCare oscillating noise 13회 연속 폐기 | PLAN_NOTES `### 추가 질문` (「가정」 주야간 적용성 미확인) |
| **BNK-270** | **★ G26 ③ 이동서비스비 월별 통계 ✅ full stack** @ `3672bbe`/`09e4ec17`(결정 95) · **PDF p.93 module 8 cross-walk**(8-3 연간일정·8-6 회의록·8-8 자원봉사 **P3** gaps) | ROADMAP v1.2.1 G26 3-function 완성 · v3 module 8 P3 |
| **BNK-271** | **평가지표 번호 벤더별 상이 확정**(케어포 `td.num`=가중치 역순 ≠ 엔젤 공단 지표번호) · G-GUARDIAN-MEETING 매핑 시 **엔젤 essential 지표27 정본 우선** · transport **법정 일지 서식 P2 carry**(NHIS #44 ④·silverangel 지표41) · 정본 4종 zero-drift | ROADMAP v3.1 G-GUARDIAN-MEETING P3 · transport 일지 P2 |
| **BNK-272** | ogada git 실측 baseline `@43d308a`/`@30f03e8`(이후 FE merge `68da0aa`·BE `c5f1325`) · **vitest full suite 2F flaky**(MealPreferenceSurvey/NursingServiceRecord isolated 7/7 PASS) · G26 ③ pilot E2E deepen | QA_FEEDBACK flake 기록 · ROADMAP baseline |
| **BNK-273** | **G26 대시보드 모니터링 근거 표시 일관성 P1**(G30/G24b/G21 표기 체계 통일) · FAQ 21700대 backlog 추가 축소 P2 | ROADMAP v1.2.1/v2 P1 |
| **BNK-274** | **케어포 PDF p.94 8-1 직원신규등록 필드 블록**(업무분장+대체자·4대보험/자격증·직종별 조직도) → staff 운영 UX 후보 **P2 carry** · func.php 107 leaf 122차 zero-drift | ROADMAP v3 module 8 P2 · 가정 번복 0 |

---

### [PLA] QA 피드백 반영 (2026-06-17, 150차 — BNK-262~268 · TSR 826~837 · ★ G26 7-8 본인부담/의료비공제 통계 대시보드 ✅ full stack · FE develop→test MERGED+origin/test PUSH @ `d8f1fdf` · QA-B106 Fixed · QA-B95 Planned · QA Open 0건(active))

> **150차 자동 기획 동기화** — BNK-262~268(G26 dual-function BE `@903f462`+`@6d10e0d` → FE wire `@d8f1fdf` 풀스택 closure·NHIS #44 118차 zero drift·silverangel 지표27 보호자회의 P3·func.php 117차 zero drift·RFID split-view P1 carry)·TSR 826~837. **QA Open 0건(active)** · **QA-B106 Fixed @ TSR 827** · **신규 Open→Planned 이동 0건** · **QA-B95 Planned 유지**.

| 항목 | 150차 관측 | 조치 |
|------|----------|------|
| **baseline** | FE **`d8f1fdf`** · test **`d8f1fdf`** · origin/test **`d8f1fdf`** · WT **CLEAN** · BE **`3481eb8`** · test **`598d108`** · **315 ahead** · WT **CLEAN** · BE test **246/246 PASS** · FE test **1504/1504 PASS** · **100 route** · **81 page** · **V1–V142** | ROADMAP CURRENT BASELINE 150차 갱신 |
| **BNK-262~268** | **★ G26 7-8 통계 대시보드 ✅ full stack** @ `d8f1fdf`/`3481eb8` · **★ NHIS #44 118차 zero drift** · **★ silverangel 지표27 보호자회의 P3** · **★ QA-B106 Fixed** · **가정 번복 0·신규 갭 0·미확인 0** | REQUIREMENTS §1-5 · ROADMAP v1.2.1 · USER_STORIES US-L07 |
| **QA** | **Open 0건(active)** · **QA-B106 Fixed @ TSR 827** · **QA-B95 Planned 유지** | QA_FEEDBACK status 동기화 |
| **merge gate** | FE **merged** @ `d8f1fdf` · BE **ready**(315) · ★ **cross-stream FULLY UNBLOCKED** | ROADMAP v1.2.1 FE `merged` · BE `ready` |
| **잔여 P0/P1** | **tester merge BE(315)** · **live E2E env**→**QA-B95 해소** · **RFID split-view P1** · **G26 이동서비스비 통계 leaf P1** · **G21 plan/claim 분리 UI P2** · **L02_M09/M10/M14 P2** · **transport 법정 일지 P2** · **G-GUARDIAN-MEETING P3** | ROADMAP v2·v3.1 갱신 |

**coder/ops 다음 액션 (150차)**: ① **tester merge BE(315)** ② **`cp scripts/dev-live-e2e.env.example scripts/dev-live-e2e.env`** + credentials → **`./scripts/run-live-e2e.sh`**(QA-B95) ③ **P1** RFID split-view·G26 이동서비스비 통계 ④ **P2** G21 plan/claim 분리 UI·L02_M09/M10/M14.

---

### [BNK] BNK-262~268 인사이트 (2026-06-17) — ★ G26 7-8 통계 대시보드 full stack · NHIS #44 · 지표27

| BNK | 핵심 | 기획 반영 |
|-----|------|----------|
| **BNK-262~264** | **G26 BE dual-function** `@903f462`(①)+`@6d10e0d`(②) · **G21 nav cross-link** `@55fdbd0` | ROADMAP v2 G21 partial+ |
| **BNK-265~266** | **func.php 107 leaf·demo-work 시설 셸 이동서비스 0** · **L07 7-x 10/11 ✅** | REQUIREMENTS §1-5 carry |
| **BNK-267** | **NHIS #44 117~118차 zero drift** · **silverangel 지표27=보호자회의 P3** | ROADMAP v3.1 G-GUARDIAN-MEETING P3 |
| **BNK-268** | **★ G26 통계 FE wire ✅ full stack** @ `d8f1fdf` — `/billing/reports/statistics`·결정 95 3-cycle closure | ROADMAP v1.2.1 · USER_STORIES US-L07 |

---

### [PLA] QA 피드백 반영 (2026-06-16, 149차 — BNK-256~261 · TSR 813~825 · L02 rpt cluster end-to-end ✅ · G21 청구반영 검은/빨간 배지 UI ✅ full · FE develop→test local MERGED · QA-B106 origin/test push 누락 Open→Planned · QA-B95 Planned · QA Open 0건(active))

> **149차 자동 기획 동기화** — BNK-256~261(G-Payroll triple-source 확정 P3·L02 rpt cluster M06/M11/M12/M16/M17 풀스택 closure·G21 청구반영 검은/빨간 배지 UI full·7-2-1 의료비공제 통계 leaf 미확인 P2·정본 4종 zero-drift·ezCare oscillating noise 폐기·FAQ 상한 ~21842)·TSR 813~825. **QA Open 0건(active)** · **QA-B106 Open→Planned**(frontend local `test`@`25ca88e` merge 완료 그러나 `origin/test`@`4299914` 16 commits 미푸시·merge pipeline push 단계 BLOCK) · **QA-B105 Fixed @ `49eb944`** · **QA-B95 Planned 유지**.

| 항목 | 149차 관측 | 조치 |
|------|----------|------|
| **baseline** | FE **`25ca88e`** · local test **`25ca88e`**(824차 merge) · origin/test **`4299914`**(**16 unpushed**) · WT **CLEAN** · BE **`b38c6f7`** · test **`598d108`** · **309 ahead** · WT **CLEAN** · BE test **246/246 PASS** · FE test **1490/1490 PASS** · **99 route** · **147 page** · **V1–V142** | ROADMAP CURRENT BASELINE 149차 갱신 |
| **BNK-256~261** | **★ L02 rpt cluster end-to-end ✅**(M04/M05/M06/M11/M12/M16/M17 풀스택) · **★ G21 청구반영 검은/빨간 배지 UI ✅ full** @ `6da49aa`/`25ca88e`(Channel.io bc7f4cd9 1:1) · **★ V142** · **★ G-Payroll triple-source 확정 P3** · **★ 7-2-1 의료비공제 통계 leaf 미확인 P2** · **가정 번복 0·신규 갭 0·미확인 1**(7-8 통계) | REQUIREMENTS §1-5 carry · ROADMAP v2/v3.1 status · COMPETITOR_MATRIX ogada 열 @HEAD |
| **QA** | **Open 0건(active)** · **QA-B106 Open→Planned** · **QA-B105 Fixed** · **QA-B95 Planned 유지** | QA_FEEDBACK Open→Planned 이동 · ROADMAP 149차 P0 push 태스크화 |
| **merge gate** | BE **ready**(309·WT CLEAN) · FE local **merged**(⚠ origin/test push 잔여 QA-B106) · ★ **cross-stream FULLY UNBLOCKED** · **309 commits**(BE only) | ROADMAP v1.2.1 BE `merge_status: ready` · FE test merged(local) |
| **잔여 P0/P1** | **`git -C src/frontend-test push origin test`**(QA-B106) · **BE tester merge(309)** · **live E2E env**→**QA-B95 해소** · **Kakao route preview live API E2E run** · **G30 live API E2E run** · **P2** L02_M09/M10/M14·7-2-1 통계 대시보드·G2b CMS 2/3·RFID split-view · **P3** G-Payroll·G-REVENUE-EXPENSE·G-HOMEPAGE | ROADMAP v2·v3·v3.1 갱신 |

**coder/ops 다음 액션 (149차)**: ① **`git -C src/frontend-test push origin test`** → `origin/test` = `25ca88e` 확인(QA-B106 해소·operation 승격 선행) ② **BE tester merge(309)**(WT CLEAN·V1–V142) ③ **`cp scripts/dev-live-e2e.env.example scripts/dev-live-e2e.env`** + credentials + backend `localhost:8080` 기동 → **`./scripts/run-live-e2e.sh`**(QA-B95 해소) ④ **Kakao route preview·G30 live API E2E run** ⑤ **P2** L02_M09/M10/M14 leaf·7-2-1 의료비공제 통계 대시보드(func/demo leaf 미확인 — 7-8 evidence 재추적).

---

### [BNK] BNK-256~261 인사이트 (2026-06-16) — ★ L02 rpt cluster end-to-end · G21 청구반영 색상 UI · G-Payroll triple-source · 7-8 통계 미확인

| BNK | 핵심 | 기획 반영 |
|-----|------|----------|
| **BNK-256** | **G-Payroll triple-source 확정**(func.php fnc dt#7 + carefor module 11 6-leaf + FAQ21819) · func.php module 10 부가서비스 8-leaf | REQUIREMENTS §1-5 G-Payroll **P3** carry |
| **BNK-257** | **L02_M06/M17 rpt 풀스택 closure** @ `fa20943`/`9cc0c1d` · demo L02 rpt cluster 실측 **6**(BNK-253 7 가정 번복) | ROADMAP v3.1 L02 rpt 4/6→full · 가정 번복 1 |
| **BNK-258** | test/harness consolidation only(구현 closure 아님) · **FAQ substantive 상한 ~21842** · Channel.io 검은/빨간 verbatim | QA_FEEDBACK status · FAQ census 상한 |
| **BNK-259** | **BE +2 = L02 cluster 3 leaf**(M11/M12 rpt + M16 식사선호도)·**V142** | ROADMAP v3.1 L02 backlog |
| **BNK-260** | **L02_M11/M12/M16 FE wire 풀스택 closure** @ `ff9c8c5`/`8b804fc` · G21 청구반영 BE side @ `6da49aa` | ROADMAP v3.1 L02 end-to-end · v2 G21 |
| **BNK-261** | **★ G21 청구반영 검은/빨간 배지 UI 풀스택 closure** @ `25ca88e`(`VisitsPage` billingClaimReflectionStatus·검은=REFLECTED·빨간=NOT_REFLECTED) · **7-2-1 의료비공제 통계 대시보드 leaf 미확인 P2**(PDF p.92 7-8 vs func 7-2-1) | ROADMAP v2 G21 plan/claim P2 부분 closure · 미확인 1 |

---

### [PLA] QA 피드백 반영 (2026-06-16, 148차 — BNK-252~255 · TSR 801~812 · v1.3-A Kakao route preview ✅ · L02_M04/M05 rpt ✅ full · L02_M17 rpt △ BE · V141 · QA-B101~B104 Fixed · QA Open 0건 · QA-B95 Planned)

> **148차 자동 기획 동기화** — BNK-252~255(carefor 2-x 이동서비스 10-leaf census·Kakao Directions route preview map·geocode refactor·L02_M04/M05 rpt print·L02_M17 rpt BE·V141 integrity·#44 러-1~4 108차 zero drift·ezCare oscillating noise 폐기·G-Payroll P3 carry)·TSR 801~812. **QA Open 0건** · **신규 Open→Planned 이동 0건** · **QA-B101/B102/B103/B104 Fixed** · **QA-B95 Planned 유지**.

| 항목 | 148차 관측 | 조치 |
|------|----------|------|
| **baseline** | FE **`388e1da`** · test **`4299914`** · **9 ahead** · WT **CLEAN** · BE **`ae7e744`** · test **`598d108`** · **303 ahead** · WT **CLEAN** · BE test **246/246 PASS** · FE test **1444/1444 PASS** · **94 route** · **75 page** · **V1–V141** | ROADMAP CURRENT BASELINE 148차 갱신 |
| **BNK-252~255** | **★ v1.3-A Kakao route preview ✅ deepen** @ `0c523cd`/`d46688d`/`3eeac92`(carefor 2-2 대비 **지도 경로 미리보기 우위**·geocode-status save blocking 제거) · **★ L02_M04/M05 rpt ✅ full+print** @ `c655743`/`c5f82a6`/`d2145b0` · **★ L02_M17 rpt △ BE** @ `ae7e744` · **★ V141 committed** @ `e8b8398` · **★ L02 leaf 8/15(53%)** · **가정 번복 0·신규 갭 0** | REQUIREMENTS §1-5 · USER_STORIES US-T02·US-O06 · ROADMAP v1.3·v3.1 |
| **QA** | **Open 0건** · **QA-B101~B104 Fixed** · **QA-B95 Planned 유지** · 신규 Open→Planned 0건 | QA_FEEDBACK status 동기화 · ROADMAP live E2E verification BLOCK |
| **merge gate** | BE+FE **ready** · WT **CLEAN** · ★ **cross-stream FULLY UNBLOCKED** · **312 commits**(9 FE+303 BE) pending · merge **미실행** | ROADMAP v1.2.1 BE `merge_status: ready` · FE test merged |
| **잔여 P0/P1** | **tester merge(312)** · **live E2E env**→**QA-B95 해소** · **Kakao route preview live API E2E run** · **L02_M06/M17 rpt FE wire** · **G30 live API E2E run** · **P2** G21 plan/claim 분리 UI·L02_M11/M12 rpt·G2b CMS 2/3 · **P3** G-MEAL-PREFERENCE·G-Payroll·G18-SHORT-PILOT | ROADMAP v3·v3.1·v2 갱신 |

**coder/ops 다음 액션 (148차)**: ① **tester merge(312)**(양 스트림 WT CLEAN·V1–V141) ② **`cp scripts/dev-live-e2e.env.example scripts/dev-live-e2e.env`** 후 credentials 설정 + backend `localhost:8080` 기동 ③ **`./scripts/run-live-e2e.sh`** → QA-B95 해소 ④ **Kakao route preview live API E2E run** ⑤ **L02_M17 rpt FE wire** + **L02_M06 체위변경 rpt aggregate** ⑥ **P2** G21 plan/claim 분리 UI 착수(Channel.io evidence).

---

### [BNK] BNK-252~255 인사이트 (2026-06-16) — ★ v1.3-A route preview · L02 rpt deepen · carefor 2-x 매핑

| BNK | 핵심 | 기획 반영 |
|-----|------|----------|
| **BNK-252** | **L02_M04/M05 print UX** @ `d2145b0` · demo L02 rpt cluster 4건 잔여(M06/M11/M12/M17) 식별 | ROADMAP v3.1 L02 backlog |
| **BNK-253** | **Kakao route preview API wire** @ `0c523cd`/`e8b8398` · **V141 committed** · PDF p.85 선행입금 가드 cross-confirm · L02_M06/M17 rpt **P1** | ROADMAP v1.3-A deepen · USER_STORIES US-T02 |
| **BNK-254** | **ezCare 7-dt verbatim** · **G-Payroll P3 carry**(dt#7) · Channel.io plan/claim 이중일정 evidence | REQUIREMENTS §1-5 carry |
| **BNK-255** | **carefor func.php 2-x 이동서비스 10-leaf ↔ ogada transport 1:1** · **ogada Kakao route preview = 경쟁사 대비 차별화**(carefor/demo-work 지도 부재) · **#44 러-1~4 verbatim carry** · **L02_M17 BE** @ `ae7e744` | ROADMAP v1.3-A · COMPETITOR_MATRIX ogada 열 @HEAD |

---

### [PLA] QA 피드백 반영 (2026-06-16, 147차 — BNK-248~251 · TSR 789~800 · L02_M13 ✅ full · L02_M15 ✅ FE · G30 phone panel ✅ full · FE merged · QA Open 0건 · QA-B95 Planned)

> **147차 자동 기획 동기화** — BNK-248~251(L02_M13 풀스택 closure·G30 phone panel FE closure·L02_M15 특이사항 FE wire·L02_M04/M05 rpt BE·live-e2e harness consolidation·law.go.kr MOHW 2025-247 본문 evidence·plan/claim 이중일정 Channel.io 3-source·lcms oscillating noise)·TSR 789~800. **QA Open 0건** · **신규 Open→Planned 이동 0건** · **QA-B95 Planned 유지**(live E2E env+credentials+backend DOWN BLOCK).

| 항목 | 147차 관측 | 조치 |
|------|----------|------|
| **baseline** | FE **`c5f82a6`** · test **`4299914`** · **2 ahead** · WT **CLEAN** · BE **`c655743`** · test **`598d108`** · **299 ahead** · WT **CLEAN** · BE test **246/246 PASS** · FE test **1444/1444 PASS** · **94 route** · **137 page** · **V1–V140** | ROADMAP CURRENT BASELINE 147차 갱신 |
| **BNK-248~251** | **★ L02_M13 ✅ full stack** @ `81a2223`/`9ad8346`(V140·결정 95 31~32회째) · **★ G30 FAQ21841 ✅ full stack** @ `344a28b`/`9ad8346`(phone `satisfiedCount` StatCard) · **★ L02_M15 ✅ FE wire** @ `3549896` · **★ L02_M04/M05 rpt BE △** @ `c655743` · **★ FE develop→test MERGED** @ `4299914`(TSR 796) · **★ law.go.kr admRulInfoP MOHW 2025-247** (#44 dual-source) · **★ plan/claim P2** · **★ L02 leaf 6/15(40%)** · **가정 번복 0·신규 갭 0** | REQUIREMENTS §1-5 · USER_STORIES US-O06·US-T15 · ROADMAP v3.1·v2 G21 |
| **QA** | **Open 0건** · **QA-B95 Planned 유지** · 신규 Open→Planned 0건 | QA_FEEDBACK status 동기화 · ROADMAP live E2E verification BLOCK |
| **merge gate** | FE test **merged** · BE **ready** · WT **CLEAN** · ★ **cross-stream FULLY UNBLOCKED** · **301 commits**(2 FE+299 BE) pending · FE merge **완료** · BE merge **미실행** | ROADMAP v1.2.1 FE `merge_status: merged` · BE `ready` |
| **잔여 P0/P1** | **tester merge BE(299)** · **live E2E env**→**QA-B95 해소** · **G30 live API E2E run** · **L02_M04/M05 rpt FE wire** · **P2** G21 plan/claim 분리 UI·검은/빨간 청구반영·RFID split-view·G2b CMS 2/3 · **P3** G-MEAL-PREFERENCE·G18-SHORT-PILOT·G-FAMILY-LEAVE | ROADMAP v3·v3.1·v2 갱신 |

**coder/ops 다음 액션 (147차)**: ① **tester merge BE(299)**(WT CLEAN·V1–V140) ② **`cp scripts/dev-live-e2e.env.example scripts/dev-live-e2e.env`** 후 credentials 설정 + backend `localhost:8080` 기동 ③ **`./scripts/run-live-e2e.sh`** → QA-B95 해소 ④ **G30 live API E2E run**(phone panel FE 추가됨) ⑤ **L02_M04/M05 rpt FE wire** ⑥ **P2** G21 plan/claim 분리 UI 착수(Channel.io evidence).

---

### [BNK] BNK-248~251 인사이트 (2026-06-16) — ★ L02_M13/M15 · G30 full · FE merged · law.go.kr evidence · plan/claim P2

| BNK | 핵심 | 기획 반영 |
|-----|------|----------|
| **BNK-248** | **a11y/health hardening** — L02_M01/M03/G-7-1 a11y pass·V139 integrity · **상태 변경 0** | PLAN_NOTES carry |
| **BNK-249** | **L02 care 2-1-x census** — demo 15 leaf 전수·M13/M15/M16 식별 · func.php dual-source numbering | REQUIREMENTS L02 backlog |
| **BNK-250** | **★ L02_M13 ✅ full stack** @ `81a2223`/`9ad8346` · **★ G30 phone panel ✅ FE** · **★ Channel.io plan/claim 3-source** — 계획일정 vs 청구일정 분리·검은/빨간 처리상태·RFID split-view P2 · FAQ rowid ~21842 상한 | ROADMAP v2 G21 P2 · USER_STORIES US-O06 |
| **BNK-251** | **harness consolidation only** — live-e2e probe·env auto-load · **★ law.go.kr admRulInfoP MOHW 2025-247 본문** (#44 dual-source) · **★ FE merged @ `4299914`** · BE 299 pending · L02_M15 @ `3549896` · L02_M04/M05 BE @ `c655743` · **L02 6/15** | ROADMAP 147차 baseline · REQUIREMENTS #44 |

---

### [PLA] QA 피드백 반영 (2026-06-16, 146차 — BNK-244~247 · TSR 777~788 · L02_M01/M03 ✅ full · G-7-1-4CHANNEL ✅ full stack · G30 FAQ21841 BE · SEC-D29/D30 신규 audit · QA Open 0건 · QA-B98/B99 Fixed · QA-B95 Planned)

> **146차 자동 기획 동기화** — BNK-244~247(L02_M01 요양급여 제공기록 풀스택 closure·L02_M03 목욕 풀스택 closure·G-7-1-4CHANNEL 급여명세서 4채널 일괄발송 풀스택·G30 FAQ21841 유선상담 5명·60% 만족 BE·L02 leaf 4/15·Channel.io 일정확정 lock·RFID split-view·longterm/ezCare oscillating noise 폐기 확정)·TSR 777~788·SEC 15차. **QA Open 0건** · **QA-B98 Fixed @ `1f77324`** · **QA-B99 Fixed @ `e6944f1`** · **QA-B95 Planned 유지**(live E2E env+credentials+backend DOWN BLOCK) · **신규 Open→Planned 이동 0건**. **신규 audit SEC-D29(Medium)·SEC-D30(Low)** — QA Open [SEC] 0·BLOCK 없음(operation 승격 전 검토 권고).

| 항목 | 146차 관측 | 조치 |
|------|----------|------|
| **baseline** | FE **`61141a6`** · BE **`de25b3e`** · **356+293 ahead** · WT **CLEAN**(양 스트림) · BE test **246/246 PASS** · FE test **217/217 PASS** · **90 route** · **71 page** · **V1–V138** | ROADMAP CURRENT BASELINE 146차 갱신 |
| **BNK-244~247** | **★ L02_M01 ✅ full stack** @ `13b8a37`/`41b2123`(V134·결정 95 27회째) · **★ L02_M03 목욕 ✅ full stack** @ `e703252`/`950415d`(V137·SKIPPED 사유 필수 가드 `@47a4e25`·결정 95 28회째) · **★ G-7-1-4CHANNEL 4채널 일괄발송 ✅ full stack** @ `3a2e82e`/`1fd1434`(V133·우편/문자/이메일/직접수령·PDF p.87 1:1) · **★ G30 FAQ21841 유선상담 5명·60% ✅ BE** @ `344a28b`(V138·`"유선상담 5명·60% 만족"` verbatim·FE panel `satisfiedCount` 잔여 P1) · **★ L02 leaf 4/15(27%)** · **★ Channel.io 일정확정 lock**(급여명세+원천세 P2)·**RFID split-view P2** · **★ longterm/ezCare oscillating noise 폐기 확정** · **가정 번복 0·신규 갭 0·미확인 0** | REQUIREMENTS §1-5 · USER_STORIES US-O06·US-O07 · ROADMAP v3.1 |
| **QA** | **Open 0건** · **QA-B98 Fixed @ `1f77324`** · **QA-B99 Fixed @ `e6944f1`** · **QA-B95 Planned 유지** · 신규 Open→Planned 0건 | QA_FEEDBACK status 동기화 · ROADMAP live E2E verification BLOCK |
| **SEC** | **신규 audit SEC-D29**(live-e2e bootstrap·**Medium**)·**SEC-D30**(health endpoint·**Low**) · **QA Open [SEC] 0건·BLOCK 없음** · SEC-D14 P0 origin/test 잔여 carry | ROADMAP P2 SEC-D29/D30 검토(비차단·operation 전) |
| **merge gate** | BE+FE **ready** · WT **CLEAN** · ★ **cross-stream FULLY UNBLOCKED** · **649 commits**(FE356+BE293) pending · merge **미실행** | ROADMAP v1.2.1 `merge_status: ready` 유지 |
| **잔여 P0/P1** | **tester merge(649)** · **live E2E env**(`scripts/dev-live-e2e.env` credentials+backend `:8080`)→**QA-B95 해소** · **live E2E run** · **★ G30 phone consultation FE panel `satisfiedCount` 표시**(FAQ21841·결정 95 30회째 후보) · **L02_M04 식사·M05 투약 leaf**(L02 5/15 next) · **G-7-1-4CHANNEL post-merge live 검증** · **P2** G21 확정 lock·RFID split-view·SEC-D29/D30 검토 · **P3** K008 Top5(FAQ21832 G-Payroll)·G-REVENUE-EXPENSE·G-FAMILY-LEAVE·G18-SHORT-PILOT | ROADMAP v3·v3.1 갱신 |

**coder/ops 다음 액션 (146차)**: ① **tester merge(649)**(양 스트림 WT CLEAN·V1–V138 contiguous) ② **`cp scripts/dev-live-e2e.env.example scripts/dev-live-e2e.env`** 후 credentials 설정 + backend `localhost:8080` 기동 ③ **`./scripts/run-live-e2e.sh`** → QA-B95 해소 ④ **G30 phone consultation FE panel** `satisfiedCount`/`satisfactionMet` 표시(FAQ21841 5명·60%·BE 응답 필드 호환) ⑤ **L02_M04 식사·M05 투약** P1 leaf BE→FE ⑥ **SEC-D29/D30** operation 승격 전 검토(비차단).

---

### [BNK] BNK-244~247 인사이트 (2026-06-16) — ★ L02_M01/M03 full · G-7-1-4CHANNEL full stack · G30 FAQ21841 · oscillating noise 폐기

| BNK | 핵심 | 기획 반영 |
|-----|------|----------|
| **BNK-244** | **교차검증·갭 우선순위 8h+** — longterm 4종 ±9B·ezCare 도입 9,331 **non-monotonic oscillating live counter noise 폐기 확정**(추세지표 폐기 권고) · 정본 4종(NHIS #44·func.php·silverangel·longterm) zero-drift · **가정 번복 0·신규 갭 0** | PLAN_NOTES 정본 추세지표 noise 폐기 |
| **BNK-245** | **G-7-1-4CHANNEL ✅ BE closure** @ `3a2e82e`(`BillingStatementDispatchChannel` enum 우편/문자/이메일/직접수령·`BillingStatementDispatchService` 318줄·V133·PDF p.87 1:1·우편 발송일 수정 가능/문자·이메일 자동기록 수정 불가) · **L02_M01 ✅ BE closure** @ `13b8a37`(V134 7 note·`/api/v1/care/weekly-service-records`) · func.php 107 leaf carry | ROADMAP v3 7-1 4채널 · USER_STORIES US-O07 |
| **BNK-246** | **L02_M01 ✅ full stack**(FE wire @ `41b2123`·결정 95 27회째·L02 3/15) · **L02_M03 목욕 △ BE shipped** @ `e703252`(V137) · **★ 신규 evidence FAQ21832 K002 Top5**(장기근속·명절수당·연말정산·G-Payroll P3)·**FAQ21839 방문상담 20분+ 전전월**(G30 cross-confirm)·**FAQ21841 유선상담 5명·60% Y** · Channel.io 일정확정 lock(급여명세+원천세)·검은/빨간 처리상태·RFID split-view P2 | REQUIREMENTS §1-5 · ROADMAP v3.1 G30·G21 |
| **BNK-247** | **L02_M03 목욕 ✅ full stack**(FE wire @ `950415d`·결정 95 28회째) · **G30 FAQ21841 유선상담 5명·60% 만족 ✅ BE** @ `344a28b`(V138 `satisfied BOOLEAN`·`isPhoneConsultationSatisfactionMet` 임계값·`"유선상담 5명·60% 만족"` verbatim·MonitoringService.java L236·FE panel `satisfiedCount` 잔여 P1) · **L02 leaf 4/15(27%)** L02_M01·M02·M03·M07 · **결정 95 누적 29회·30분 1-cycle benchmark→coder closure가 dominant delivery pattern 확정** · 가정 번복 0·신규 갭 0 | ROADMAP v3.1 G30 ✅ deepen·L02 backlog · USER_STORIES US-O06 |

---

### [PLA] QA 피드백 반영 (2026-06-16, 145차 — BNK-240~243 · TSR 765~776 · L02_M07 ✅ full · live-e2e harness deepen · QA-B99 Open→Planned · merge BLOCK)

> **145차 자동 기획 동기화** — BNK-240~243(L02_M07 full stack closure·live-e2e harness BE bootstrap+FE probe guard·7-1 4채널 PDF p.87·MOHW 2026-126·longterm oscillating noise·ezCare FAQ21831)·TSR 765~776. **QA Open 1 BLOCK** → **Planned**: **QA-B99** · **QA-B98 Fixed @ `1f77324`** · **QA-B95 Planned 유지**.

| 항목 | 145차 관측 | 조치 |
|------|----------|------|
| **baseline** | FE **`6f53978`** · BE **`18ff83e`** · **349+287 ahead** · FE WT **DIRTY 3M** · BE WT **CLEAN** · BE test **246/246 PASS** · FE test **217/217 PASS** · **87 route** · **69 page** · **V1–V132** | ROADMAP CURRENT BASELINE 145차 갱신 |
| **BNK-240~243** | **★ L02_M07 ✅ full stack** @ `ea6092a`/`14a2bb9`/`d862a82`(결정 95 26회째·L02 2/15) · **★ live-e2e harness deepen** @ `1f77324`/`18ff83e`/`10f32c4`/`07dd49b` · **★ 7-1 4채널 P2 deepen**(PDF p.87) · **★ MOHW 2026-126 P3** · **★ longterm oscillating ±9B** · **★ ezCare FAQ21831·도입 9,324** | REQUIREMENTS §1-5 · USER_STORIES US-O06 · ROADMAP v3.1 |
| **QA** | **QA-B99 Open→Planned** — FE WT **DIRTY 3M** live E2E harness WIP · **QA-B98 Fixed @ `1f77324`** · **QA-B95 Planned 유지** | QA_FEEDBACK Planned · ROADMAP merge **636 BLOCK** |
| **merge gate** | BE **ready** · FE **BLOCK** · ⚠ **cross-stream BLOCK** · **636 commits** pending · merge **실행 금지** | ROADMAP v1.2.1 FE `merge_status: pending` |
| **잔여 P0/P1** | **COD QA-B99 fix→WT clean→tester merge(636)** · **live E2E env** · **live E2E run** · **7-1 4채널·7-2 은행엑셀** · **P2** L02_M01/M03·rpt cluster·G-STAFF-LIFECYCLE · **P3** G-REVENUE-EXPENSE·G-FAMILY-LEAVE·G18-SHORT-PILOT | ROADMAP v3·v3.1 갱신 |

**coder/ops 다음 액션 (145차)**: ① **QA-B99 fix** — `liveConfig.js`·`liveDescribe.js`·`liveGlobalSetup.js` 커밋 또는 revert → WT clean ② **`cp scripts/dev-live-e2e.env.example scripts/dev-live-e2e.env`** 후 credentials 설정 + backend `localhost:8080` 기동 ③ **`./scripts/run-live-e2e.sh`** → QA-B95 해소 ④ **tester merge(636)** ⑤ **7-1 4채널 일괄발송** 채널 enum 설계 착수 ⑥ **L02_M01/M03** P1 leaf 우선.

---

### [BNK] BNK-240~243 인사이트 (2026-06-16) — ★ L02_M07 full · live-e2e harness · 7-1 4채널 · MOHW 2026-126 · longterm noise

| BNK | 핵심 | 기획 반영 |
|-----|------|----------|
| **BNK-240** | **L02_M07 BE closure** @ `ea6092a`·**MOHW 2026-126** 본인부담상한 고시 · **#44 98차 zero drift** · G14·대시보드·v1.3-C·v2 CMS **가정 번복 0** | REQUIREMENTS G-BODY-RESTRAINT △→✅ BE partial+ |
| **BNK-241** | **L02_M07 FE closure** @ `14a2bb9`/`d862a82`·`/care/body-restraint`·V132 integrity · **PDF p.87 7-1 4채널** evidence(`0988a8fe`) · L02 **2/15 full** | USER_STORIES US-O06 ✅ · ROADMAP P2 7-1 deepen |
| **BNK-242** | **live-e2e env prefer-local** @ `10f32c4`/`8b7e476` · **FAQ21831** 콜백 지연·K008 Top5 · **ezCare 도입 9,324(−7)** · fnc 7-dt 매핑 | PLAN_NOTES live E2E scope |
| **BNK-243** | **live-e2e probe guard** @ `07dd49b` · **BE bootstrap** @ `1f77324`·**status fallback** @ `18ff83e` · **longterm 4종 oscillating ±9B** 확정(verbatim 불변) · **lawImg 200·0B empty** | ROADMAP merge gate · QA-B98 Fixed carry |

---

### [PLA] QA 피드백 반영 (2026-06-16, 144차 — BNK-236~239 · TSR 753~764 · G30 evidence window ✅ deepen · G39 ✅ partial+ · L02_M02 ✅ FE wire · 신규 갭 3건 · func.php 107 leaf · QA Open 0건 · QA-B95 Planned)

> **144차 자동 기획 동기화** — BNK-236~239(G30 monitoring evidence window 풀스택 deepen·G39 dispatch pilot+live harness·L02_M02 집중배설관찰 FE wire·신규 갭 G-BODY-RESTRAINT(L02_M07 신체제재)·G-STAFF-LIFECYCLE(FAQ21825 입사~퇴사 4단)·G-REVENUE-EXPENSE(module 12)·func.php 107 leaf 정본·주야간 PDF 132p snapshot·#44 러-1~4 97차 zero drift)·TSR 753~764. **QA Open 0건** · **QA-B96/B97 Fixed** · **QA-B95 Planned 유지**(live E2E env BLOCK).

| 항목 | 144차 관측 | 조치 |
|------|----------|------|
| **baseline** | FE **`95e7e96`** · BE **`df14e15`** · **343+282 ahead** · WT **CLEAN** · BE test **246/246 PASS** · FE test **217/217 PASS** · **86 route** · **68 page** · **V1–V131**(V131 WIP) | ROADMAP CURRENT BASELINE 144차 갱신 |
| **BNK-236~239** | **★ G30 evidence window ✅ deepen** @ `73df04d`(FAQ21838 전전월±2개월 1:1) · **★ G39 ✅ partial+**(pilot+live harness) · **★ L02_M02 ✅ FE wire** @ `1264c16` · **★ G-BODY-RESTRAINT(L02_M07) P2 △ BE WIP**(V131·demo `view.care_sanction`) · **★ G-STAFF-LIFECYCLE P2**(FAQ21825 4단·퇴사·희망이음 RFID) · **★ G-REVENUE-EXPENSE P3**(module 12 PDF-only) · **★ func.php 107 leaf 정본** · **★ #44 러-1~4 97차 zero drift** · **★ longterm 4종 verbatim 불변** | REQUIREMENTS §1-5 · USER_STORIES · ROADMAP v3/v3.1 backlog |
| **QA** | **Open 0건** · **QA-B96 Fixed @ `eb16734`** · **QA-B97 Fixed @ `0122bfe`** · **QA-B95 Planned 유지** | QA_FEEDBACK status 동기화 · ROADMAP live E2E verification BLOCK |
| **merge gate** | BE+FE **ready** · WT **CLEAN** · **625 commits** pending · ⚠ **live E2E verification BLOCK**(credentials 미설정·backend@8080 DOWN) | ROADMAP v1.2.1 `merge_status: ready` 유지 |
| **잔여 P0/P1** | **live E2E env 구성** · **tester merge(625)** · **live E2E run**(mvn/npm 1회) · **L02_M07 신체제재 coder commit+FE wire(V131)** · **7-1 명세 4채널 일괄발송** · **7-2 은행엑셀 일괄입금** · **RFID split-view** · **P2** G-STAFF-LIFECYCLE 퇴사 4단·G-BODY-RESTRAINT 인권 기록 요건·L02 잔여 leaf · **P3** G-REVENUE-EXPENSE·G-FAMILY-LEAVE·G18-SHORT-PILOT·G-LIVECHAT·G-CIST·G-STAFF-MEETING | ROADMAP v3·v3.1 갱신 |

**coder/ops 다음 액션 (144차)**: ① **`cp scripts/dev-live-e2e.env.example scripts/dev-live-e2e.env`** 후 guardian/live creds 설정 + backend `localhost:8080` 기동 ② **`./scripts/run-live-e2e.sh`** 재검증 → QA-B95 해소 ③ **tester merge(625)** ④ **L02_M07 신체제재 V131 commit + `/care/body-restraint` FE wire**(demo `view.care_sanction` 앵커·결정 95 closure 후보) ⑤ **7-1 명세 4채널 일괄발송·7-2 은행엑셀 일괄입금**(PDF p.87~88) ⑥ **RFID split-view UI**(ezCare change_work·Channel.io bc7f4cd9).

---

### [BNK] BNK-236~239 인사이트 (2026-06-16) — ★ G30 evidence window · G39 dispatch · L02_M02 closure · 신규 갭 3건 · func.php 107 leaf

| BNK | 핵심 | 기획 반영 |
|-----|------|----------|
| **BNK-236** | **G30 monitoring evidence window ✅ deepen** — `MonitoringEvidenceWindow`(전전월 `BASE_OFFSET_MONTHS=2`·`RADIUS_MONTHS=2`·최소 연속 3개월) FAQ21838 「전전월 ±2개월」 1:1·**결정 95 24회째** · **G39 △→✅ partial+**(pilot E2E 91줄+live harness 88줄) · 96차 cross-validation **가정 번복 0**·**미확인 0** · ezCare 도입 9,330(+1) | ROADMAP v3.1 G30 ✅·v2 G21 G39 closure |
| **BNK-237** | **func.php 107 leaf 정본**(agents.yaml「109」**가정 번복**·module 2 이동서비스 10 leaf 주야간 전용) · **주야간 사용매뉴얼 PDF 132p+TOC snapshot**(module 1~12·7-x PDF↔func 번호 불일치·p.85 선행입금 가드 1:1 carry) · **신규 갭 G-REVENUE-EXPENSE P3**(module 12 수입지출관리 PDF-only) · **P1** 7-1 명세 4채널 일괄발송·7-2 은행엑셀 일괄입금 | REQUIREMENTS §1-5 func.php 107 · ROADMAP v3 backlog |
| **BNK-238** | **신규 갭 G-STAFF-LIFECYCLE P2**(FAQ21825 종사자 입사~퇴사 4단 lifecycle·**퇴사 4단**·희망이음 RFID 핸드폰 등록·US-R03 부분 커버) · **L02_M02 집중배설관찰 ❌→△ BE**(V130·결정 95 25회째) · FAQ21828 운영규정 교육(평가지표 5·면담 확인) · **RFID split-view P1**(change_work·Channel.io 3-source) · FAQ rowid 카탈로그 상한 ~21845 재확인 | USER_STORIES US-R03 확장 · ROADMAP v3 backlog |
| **BNK-239** | **신규 갭 G-BODY-RESTRAINT(L02_M07 신체제재) P2 △ BE WIP**(V131 `body_restraint_records`·`restraint_method` 6 enum·`reason` NOT NULL·`alternative_attempted`·`guardian_notified`·`release_reason`·demo `view.care_sanction` 앵커·**func.php 2-4=차량관리 무관 주의**·결정 95 in-flight) · **L02_M02 △→✅ FE wire** @ `1264c16` · **#44 러-1~4 97차 zero drift**(joHistory `c886ff1f`·50% 산정·1일1회·편도·lawImg 404 dead·V103 seed carry) · **longterm 502/610/503/501 verbatim 불변**(74,060·110%·50/60%·12일/24회·일률 +9B 템플릿 drift) | ROADMAP v3.1 L02_M07 backlog · REQUIREMENTS G-BODY-RESTRAINT |

---

### [PLA] QA 피드백 반영 (2026-06-15, 143차 — BNK-232~235 · TSR 741~752 · G24b list ✅ · G19 harness △ · G30/G39 P2 deepen △ · QA Open 0건 · QA-B95 Planned)

> **143차 자동 기획 동기화** — BNK-232~235(G24b list page closure·G19 provider discovery harness·live E2E harness defaults·#44 lawImg DRIFT·silverangel URL catalog 축소·G18-SHORT-PILOT 무기한 연장·G30/G39 P2 pilot E2E)·TSR 741~752. **QA Open 0건** · **QA-B95 Planned 유지**(live E2E env BLOCK).

| 항목 | 143차 관측 | 조치 |
|------|----------|------|
| **baseline** | FE **`73094f9`** · BE **`73df04d`** · **336+276 ahead** · WT **CLEAN** · BE test **246/246 PASS** · FE test **217/217 PASS** · **85 route** · **67 page** · **V1–V129** | ROADMAP CURRENT BASELINE 143차 갱신 |
| **BNK-232~235** | **★ G24b compliance list page ✅** @ `eb16734` · **★ G19 provider discovery harness △** @ `41d8de5`/`8cb8789` · **★ live E2E harness defaults ✅** @ `0122bfe` · **★ G30/G39 P2 deepen △** @ `73df04d`/`73094f9` · **★ #44 joHistory 95차 zero drift** · **★ lawImg 95차 DRIFT 404** · **★ silverangel extra/fee 404** · **★ G18-SHORT-PILOT 2026.1~무기한** · **★ G-STAFF-MEETING P3 candidate** | REQUIREMENTS §1-5 · USER_STORIES US-T08/US-T09/US-T15 |
| **QA** | **Open 0건** · **QA-B95 Planned 유지** | QA_FEEDBACK status 불변 · ROADMAP live E2E verification BLOCK |
| **merge gate** | BE+FE **ready** · WT **CLEAN** · **612 commits** pending · ⚠ **live E2E verification BLOCK** | ROADMAP v1.2.1 `merge_status: ready` 유지 |
| **잔여 P0/P1** | **live E2E env 구성**(`scripts/dev-live-e2e.env`) · **tester merge(612)** · **live E2E run**(mvn/npm 1회) · **G19 provider discovery FE wire** · 7-5 live PG · 8-12 print · J03 Solapi · v1.3 live E2E · **P2 L02 v3.1 Must 5건** · G30 ±2개월·monitoring 12지표 · G39 guardian dispatch · **P3 G-FAMILY-LEAVE·G18-SHORT-PILOT·G-LIVECHAT·G-CIST·G-STAFF-MEETING** | ROADMAP v1.2.1·v3.1 갱신 |

**coder/ops 다음 액션 (143차)**: ① **`cp scripts/dev-live-e2e.env.example scripts/dev-live-e2e.env`** 후 guardian/live creds 설정 ② **`./scripts/run-live-e2e.sh`** 재검증 → QA-B95 해소 ③ **tester merge(612)** ④ **G19 provider discovery FE wire**(longterm `selectLtcoSrch` filter) ⑤ **G30/G39 P2 live E2E run** @ `73df04d`/`73094f9` ⑥ **L02 v3.1 Must 5건** 우선.

---

### [BNK] BNK-232~235 인사이트 (2026-06-15) — ★ G24b list closure · G19 harness · #44 lawImg DRIFT · G18-SHORT 연장 · G30/G39 P2 deepen

| BNK | 핵심 | 기획 반영 |
|-----|------|----------|
| **BNK-232** | **G24b compliance list WIP→closure** — `NeedsAssessmentStatusPage` @ `eb16734` · **G-STAFF-MEETING P3 candidate**(FAQ21822 직원회의·2026 평가 삭제·운영 모듈 잔존) | USER_STORIES US-T09 · REQUIREMENTS G24 |
| **BNK-233** | **func.php 107 leaf 정본**(agents.yaml「109」정정) · G24b status page full stack @ `eb16734` | REQUIREMENTS §1-5 · PLAN_NOTES func.php 카운트 |
| **BNK-234** | **G39 guardian dispatch UI ✅** @ `4d1a4f2` · **G19 provider discovery live API harness ✅** @ `41d8de5` · ezCare FAQ21819 K008 급여명세서 deepen | USER_STORIES US-T08 · G19 P1 |
| **BNK-235** | **#44 lawImg 95차 DRIFT 404** — joHistory `c886ff1f`+V103 seed evidence 유지 · **silverangel extra/fee 404**(유효 URL 4건) · **2026 단기보호 시범 2026.1~무기한 연장** · **ShortTermCareContract** 단일 모델 권고(G18+G-FAMILY-LEAVE) · **G30/G39 P2 pilot E2E** @ `73df04d`/`73094f9` | ROADMAP P2/P3 · REQUIREMENTS G16·G18·G2b |

---

### [PLA] QA 피드백 반영 (2026-06-15, 142차 — BNK-227~231 · TSR 729~740 · G24b dashboard ✅ · G41 enum 23+ ✅ · QA-B95 Planned · live E2E env BLOCK)

> **142차 자동 기획 동기화** — BNK-227~231(G24b compliance API+dashboard widget closure·G41 V129 enum 23+ closure·#44 91차 재확정·longterm provider search·visit/easy-pay harness deepen·ezCare FAQ21838/21816~21818·carefor monitoring 12지표)·TSR 729~740. **QA Open 1 BLOCK** → **Planned**: **QA-B95**(frontend live E2E env 누락·4 suite FAIL).

| 항목 | 142차 관측 | 조치 |
|------|----------|------|
| **baseline** | FE **`3cbe582`** · BE **`1e21b20`** · **330+272 ahead** · WT **CLEAN** · BE test **246/246 PASS** · FE test **217/217 PASS** · **85 route** · **66 page** · **V1–V129** | ROADMAP CURRENT BASELINE 142차 갱신 |
| **BNK-227~231** | **★ G24b compliance API+dashboard widget ✅** @ `98002d4`/`f4c8beb`/`ca0b627`/`baa6d6d` · **★ G41 enum 23+ ✅** V129 @ `b1c92e1` · **★ #44 P0 ✅ 91차** · **★ longterm provider search** → G19 P1 · **★ harness deepen** @ `3cbe582`/`1e21b20` · **★ P2 carry** G39 dispatch·G30 ±2개월·monitoring 12지표 | REQUIREMENTS §1-5 · USER_STORIES US-T09/US-H01/US-S04 |
| **QA** | **QA-B95 Open→Planned** — `npm run test:live-e2e` 4 suite FAIL · `LIVE_E2E_*` env 누락 | QA_FEEDBACK Planned · ROADMAP live E2E verification BLOCK |
| **merge gate** | BE+FE **ready** · WT **CLEAN** · **602 commits** pending · ⚠ live E2E verification BLOCK | ROADMAP v1.2.1 `merge_status: ready` 유지 |
| **잔여 P0/P1** | **live E2E env 구성**(`scripts/dev-live-e2e.env`) · **tester merge(602)** · **live E2E run**(mvn/npm 1회) · **G19 provider discovery P1** · 7-5 live PG · 8-12 print · J03 Solapi · v1.3 live E2E · **P2 L02 v3.1 Must 5건** · G39 dispatch · G30 window · **P3 G-FAMILY-LEAVE·G-LIVECHAT·G-CIST·K008~K014** | ROADMAP v1.2.1·v3.1 갱신 |

**coder/ops 다음 액션 (142차)**: ① **`cp scripts/dev-live-e2e.env.example scripts/dev-live-e2e.env`** 후 `LIVE_E2E_EMAIL`/`PASSWORD`(또는 `LIVE_E2E_ACCESS_TOKEN`)·`LIVE_E2E_CLIENT_ID`·guardian creds 설정 ② **`./scripts/run-live-e2e.sh`** 또는 `cd src/frontend-test && npm run test:live-e2e` 재검증 → QA-B95 해소 ③ **tester merge(602)** ④ **live E2E run** full harness ⑤ **G19 provider discovery** 기획 착수(longterm `selectLtcoSrch.web` filter) ⑥ **L02 v3.1 Must 5건** 우선.

---

### [BNK] BNK-227~231 인사이트 (2026-06-15) — ★ G24b dashboard closure · G41 enum closure · G19 discovery · live E2E env

| BNK | 핵심 | 기획 반영 |
|-----|------|----------|
| **BNK-227** | **G24b compliance API deepen** — `GET /clients/needs-assessments/compliance`·FAQ21810 정기+등급변경 재사정 · 결정 95 20회째 | API_SPEC §9-2-1 · ROADMAP P1 carry → **dashboard widget P1 닫힘**(BNK-229) |
| **BNK-228~229** | **G24b dashboard widget ✅** @ `ca0b627`/`baa6d6d` · **G41 V129 enum 23+ ✅** @ `b1c92e1` · carefor monitoring.php 12지표 evidence | USER_STORIES US-H01/US-T09/US-S04 · REQUIREMENTS G24b/G41 |
| **BNK-230** | **ezCare FAQ21838** 모니터링 ±2개월·RFID audit · **FAQ21816/21817/21818** 급여기록 이중 주기 | ROADMAP P2 G39 dispatch·G30 window |
| **BNK-231** | **#44 91차 zero drift** · **longterm provider search** `ltcAdminKindChoiceYn7/8` · silverangel transport negative scan · harness @ `3cbe582`/`1e21b20` | G19 P1 provider discovery · PLAN_NOTES #44 carry |

---

### [PLA] QA 피드백 반영 (2026-06-15, 141차 — BNK-224~226 · TSR 717~728 · G-ONBOARD-SUPPORT ✅ full · G24b ✅ full · QA-B94 Fixed · merge FULLY UNBLOCKED)

> **141차 자동 기획 동기화** — BNK-224~226(G-ONBOARD 1-cycle full stack·G24b V128 8항목 full·P1 harness deepen·FAQ21810/21814/21815 evidence)·TSR 717~728. **QA Open 0건** · **QA-B94 Fixed @ `43c4b08`**(Open 섹션 Fixed 기록·Planned 이동 없음).

| 항목 | 141차 관측 | 조치 |
|------|----------|------|
| **baseline** | FE **`92b9eff`** · BE **`f4c8beb`** · **323+266 ahead** · WT **CLEAN** · BE test **246/246 PASS** · FE test **217/217 PASS** · develop HEAD **1323/1323 PASS** · **84 route** · **67 page** · **V1–V128** | ROADMAP CURRENT BASELINE 141차 갱신 |
| **BNK-224~226** | **★ G-ONBOARD-SUPPORT ✅ full stack** @ `36264b5`/`4c1fd43`/`735dd53` · **★ G24b ✅ full stack** V128 @ `45fb6d9`/`49fbf67` · **★ P1 harness deepen** G14/G19/G30/L03 @ `fcabed0`/`8eed216` · **★ FAQ 21810/21814/21815** evidence · **★ appraisal.php 2026** 1~20 지표(BNK-225) | REQUIREMENTS §1-5 · USER_STORIES US-O05/US-T09 |
| **QA** | Open **0건** · **QA-B94 Fixed @ `43c4b08`** | QA_FEEDBACK status 갱신 · ROADMAP merge **589 FULLY UNBLOCKED** |
| **merge gate** | BE+FE **ready** · ★ **FULLY UNBLOCKED** · **589 commits** pending | ROADMAP v1.2.1 `merge_status: ready` |
| **잔여 P0/P1** | **tester merge(589)** · **live E2E run**(G-NURSING·G14·G19·G30·mvn/npm 1회) · 7-5 live PG · 8-12 print · J03 Solapi · v1.3 live E2E · **P2 L02 v3.1 Must 5건** · G41 enum 23+ · 21815 변경사유 필드 · **P3 G-FAMILY-LEAVE·G-LIVECHAT·G-CIST·K008~K014** | ROADMAP v1.2.1·v3.1 갱신 |

**coder 다음 액션 (141차)**: ① **tester merge(589)** ② **live E2E run**(G-NURSING·G14·G19·G30 harness `fcabed0`/`8eed216`·mvn/npm 1회) ③ G41b `LIVE_E2E` manual verify ④ 7-5 live PG ⑤ 8-12 print ⑥ J03 Solapi ⑦ v1.3 live E2E ⑧ **L02 v3.1 Must 5건** 착수 시 우선.

---

### [BNK] BNK-224~226 인사이트 (2026-06-15) — ★ G-ONBOARD full · G24b full · P1 harness deepen · FAQ evidence

| BNK | 핵심 | 기획 반영 |
|-----|------|----------|
| **BNK-224** | **G-ONBOARD-SUPPORT 1-cycle full stack** — BE V126/V127 @ `4c1fd43`/`735dd53` + FE panel+live E2E @ `36264b5` · silverangel 36-item·4-session SLA 1:1 · **결정 95 18회째** | USER_STORIES US-O05 ✅ · ROADMAP v1.2.1 |
| **BNK-225** | **P1 harness deepen** — G14/G19/G30/L03 consolidated live E2E @ `fcabed0`/`8eed216` · **appraisal.php 2026** 지표 1~20 evidence · G37 attachment @ `a565a50` | ROADMAP P1 carry · REQUIREMENTS G30/G14 |
| **BNK-226** | **G24b ✅ full stack** — V128 5컬럼+FE @ `45fb6d9`/`49fbf67` · FAQ21810 8 세부항목 1:1 · FAQ21814 G42·FAQ21815 G14/G17b cross-confirm · **결정 95 19회째** | USER_STORIES US-T09 · REQUIREMENTS G24 |

---

### [PLA] QA 피드백 반영 (2026-06-15, 140차 — BNK-219~223 · TSR 705~716 · QA-B93 Fixed · G-ONBOARD-SUPPORT △ BE · merge FULLY UNBLOCKED)

> **140차 자동 기획 동기화** — BNK-219~223(L03 live E2E harness deepen·QA-B93 Fixed·G14/G-ONBOARD harness·G-FAMILY-LEAVE evidence ✅·G-LIVECHAT/G-CIST P3 candidate)·TSR 705~716. **QA Open 0건** · **139차 Planned QA-B93 → Fixed @ `b45830d`**.

| 항목 | 140차 관측 | 조치 |
|------|----------|------|
| **baseline** | FE **`2ccc88e`** · BE **`735dd53`** · **316+261 ahead** · WT **CLEAN** · BE test **246/246 PASS** · FE test **217/217 PASS** · **84 route** · **67 page** · **V1–V125** | ROADMAP CURRENT BASELINE 140차 갱신 |
| **BNK-219~223** | **★ L03 live E2E harness 5종+deepen** @ `75c6c76`/`b698871`/`548f670`/`2ccc88e` · **★ QA-B93 Fixed @ `b45830d`** · **★ G-ONBOARD-SUPPORT △ BE** @ `735dd53` · **★ G-FAMILY-LEAVE evidence ✅** 3-source · **★ P3 candidate** G-LIVECHAT·G-CIST | REQUIREMENTS §1-5 · USER_STORIES US-O05 |
| **QA** | Open **0건** · **QA-B93 Fixed @ `b45830d`** | QA_FEEDBACK status 갱신 · ROADMAP merge **577 FULLY UNBLOCKED** |
| **merge gate** | BE+FE **ready** · ★ **FULLY UNBLOCKED** · **577 commits** pending | ROADMAP v1.2.1 `merge_status: ready` |
| **잔여 P0/P1** | **tester merge(577)** · **G-NURSING live E2E run**(L03 13/14 leaf·mvn/npm 1회) · G14 live upload E2E · G19·G30 · **P2 G-ONBOARD-SUPPORT 1~4회차 SLA·G24b** · 7-5 live PG · 8-12 print · J03 Solapi · v1.3 live E2E · **P3 G-FAMILY-LEAVE·G-LIVECHAT·G-CIST·K008~K014** | ROADMAP v1.2.1·v3.1 갱신 |

**coder 다음 액션 (140차)**: ① **tester merge(577)** ② **G-NURSING live E2E run**(mvn/npm 1회·L03 13/14 leaf) ③ G14 live upload E2E ④ G30·G19 live API E2E ⑤ **G-ONBOARD-SUPPORT FE wire**(1~4회차 SLA checklist UI) ⑥ G24b·7-5 live PG ⑦ v1.3 live E2E.

---

### [BNK] BNK-219~223 인사이트 (2026-06-15) — ★ L03 harness deepen · QA-B93 closure · G-FAMILY-LEAVE evidence · P3 candidates

| BNK | 핵심 | 기획 반영 |
|-----|------|----------|
| **BNK-219** | **L03_M15 FE wire ✅** @ `efa4472` · L03 14/14 effective 100% carry | USER_STORIES US-O04 M15 ✅ · ROADMAP v3.1 |
| **BNK-220~221** | **L03 a11y+reports E2E split** @ `671a704`/`b698871` · **QA-B93 Fixed** @ `b45830d` · G21 batch confirm pilot @ `5edc45c` | ROADMAP v1.2.1 · QA_FEEDBACK Fixed |
| **BNK-222** | **G14 첨부 live E2E harness** @ `548f670` · **L03 reports pilot flow** @ `a728f1b` | USER_STORIES G14 · US-O04 live E2E |
| **BNK-223** | **silverangel 4 URL 신규 evidence** · **G-FAMILY-LEAVE △→✅** 3-source · **G-LIVECHAT·G-CIST P3 candidate** · **G-ONBOARD BE △** @ `735dd53` | REQUIREMENTS §1-5 · USER_STORIES US-O05 |

---

### [PLA] QA 피드백 반영 (2026-06-15, 139차 — BNK-217~218 · TSR 693~704 · L03 13/14 ✅ effective 100% · QA-B92 Fixed · QA-B93 Planned · merge BLOCK)

> **139차 자동 기획 동기화** — BNK-217~218(L03_M01/M06 FE wire·L03_M07/M09/M10/M15 rpt full stack·func.php 4-x Route closure·L03_M08 N/A)·TSR 693~704. **QA Open 1 BLOCK** → **Planned**: **QA-B93** · **QA-B92 Fixed @ `2966447`**.

| 항목 | 139차 관측 | 조치 |
|------|----------|------|
| **baseline** | FE **`89dc52d`** · BE **`6b0238a`** · **311+255 ahead** · FE WT **CLEAN** · BE WT **DIRTY 2M** · FE HEAD **1313/1313 PASS** · BE test **246/246 PASS** · FE test **217/217 PASS** · **84 route** · **67 page** · **V1–V125** | ROADMAP CURRENT BASELINE 139차 갱신 |
| **BNK-217~218** | **★ L03_M01/M06 ✅ full** @ `12591d4`/`2966447` · **★ L03_M07/M09/M10 ✅ full** @ `2a05271`/`c23b1a3` · **★ L03_M15 ✅ full** @ `75bddee` · **★ L03 13/14 93%·effective 100%**(M08 N/A) · **★ func.php 4-x↔Route 5/5 closure** | ROADMAP v3.1·USER_STORIES US-O04 갱신 |
| **QA** | Open **1 BLOCK** → **Planned** · **QA-B92 Fixed @ `2966447`** | QA_FEEDBACK Open→Planned · ROADMAP merge **566 BLOCK** |
| **merge gate** | BE **BLOCK**(WT dirty) · FE **ready** · ⚠ **cross-stream BLOCK** · **566 commits** pending | ROADMAP v1.2.1 `merge_status: pending`(BE) |
| **잔여 P0/P1** | **COD QA-B93 fix→WT clean→tester merge(566)** · **G-NURSING live E2E**(L03 13/14 leaf) · 요양 기록 reinforce P1 · G30·G14/G34/G34b/G42/G19 live E2E · 7-5 live PG · 8-12 print live E2E · J03 Solapi · RFID split-view · **P2 G-ONBOARD-SUPPORT·G24b** · v1.3 live E2E · **P3 G-STAFF-COUNSEL·G18-SHORT-PILOT·G41-COG-REFRESHER·K008~K014** | ROADMAP v1.2.1·v3.1 갱신 |

**coder 다음 액션 (139차)**: ① **QA-B93 fix** — `EasyPayService`·`EasyPayServiceTest` 커밋 또는 revert → WT clean ② **tester merge(566)** ③ **G-NURSING live E2E harness run**(L03 13/14 leaf·mvn/npm 1회) ④ G30·G14/G34/G34b/G42/G19 live API E2E ⑤ 8-12 print live E2E ⑥ G41b `LIVE_E2E=1` ⑦ 7-5 live PG ⑧ J03 Solapi ⑨ v1.3 live E2E.

---

### [BNK] BNK-217~218 인사이트 (2026-06-15) — ★ L03 full stack closure · func.php 4-x · L03_M08 N/A

| BNK | 핵심 | 기획 반영 |
|-----|------|----------|
| **BNK-217** | **L03_M01+M06 FE wire ✅ full** — `12591d4`(+2,100줄·20파일) + live E2E @ `2966447` · V125 integrity @ `ee8b2a4` | USER_STORIES US-O04 M01/M06 ✅ · ROADMAP v3.1 |
| **BNK-218** | **L03_M07/M09/M10 rpt FE+BE ✅ full** @ `2a05271`/`c23b1a3` · **M15 pressure ulcer rpt ✅ full** @ `75bddee` · func.php 4-1~4-5 ↔ ogada Route **5/5 closure** | USER_STORIES US-O04 M07/M09/M10/M15 ✅ · REQUIREMENTS §1-5 |
| **BNK-218** | **L03_M08 noready2 carefor 자체 disabled → N/A 폐기 확정** · L03 effective **100%** | PLAN_NOTES 추가 질문 · ROADMAP v3.1 완료 기준 |

---

### [PLA] QA 피드백 반영 (2026-06-15, 138차 — BNK-213~216 · TSR 681~692 · v1.3-B ✅ full · QA-B88/B89/B90 Fixed · merge FULLY UNBLOCKED)

> **138차 자동 기획 동기화** — BNK-213~216(v1.3-B full stack·L03_M01 V123·L03_M06 V124·US-UX-05 deepen·US-R02 print·G-STAFF-COUNSEL P3)·TSR 681~692. **QA Open 0건** · **137차 Planned QA-B88/B89/B90 → Fixed** · **QA-B91 Fixed @ `c865d2b`**.

| 항목 | 138차 관측 | 조치 |
|------|----------|------|
| **baseline** | FE **`3845f0c`** · BE **`a4352a8`** · **305+250 ahead** · WT **CLEAN** · FE HEAD **1275/1275 PASS** · BE test **246/246 PASS** · FE test **217/217 PASS** · **77 route** · **64 page** · **V1–V124** | ROADMAP CURRENT BASELINE 138차 갱신 |
| **BNK-213~216** | **★ v1.3-B ✅ full** — BE @ `db94a65` + FE @ `2ffe59f` (BNK-214~216) · **★ L03_M01 △ BE** V123 @ `9bd1660` · **★ L03_M06 △ BE** V124 @ `a4352a8` · **★ L03 BE 10/14 71%·FE 8/14 57%** · **★ US-UX-05 deepen** @ `edfba7f`/`3845f0c` · **★ US-R02 8-12 print** @ `e3e6964` · **★ 신규 P3 G-STAFF-COUNSEL**(FAQ21804) | ROADMAP v1.3-B·v3.1·USER_STORIES US-O04/US-T02-B 갱신 |
| **QA** | Open **0건** · **QA-B88/B89/B90 Fixed** · **QA-B91 Fixed @ `c865d2b`** | QA_FEEDBACK status 갱신 · ROADMAP merge **555 FULLY UNBLOCKED** |
| **merge gate** | BE+FE **ready** · ★ **FULLY UNBLOCKED** · **555 commits** pending | ROADMAP v1.2.1 `merge_status: ready` |
| **잔여 P0/P1** | **tester merge(555)** · **L03_M01/M06 FE wire P1** · G-NURSING live E2E run · 요양 기록 reinforce P1 · G30·G14/G34/G34b/G42/G19 live E2E · 7-5 live PG · 8-12 print live E2E · J03 Solapi · RFID split-view · **P2 L03 4 leaf** · **P2 G24b·G41-COG-REFRESHER·G-ONBOARD-SUPPORT** · v1.3 live E2E · **P3 G-STAFF-COUNSEL·G18-SHORT-PILOT·K008~K014** | ROADMAP v1.2.1·v3.1 갱신 |

**coder 다음 액션 (138차)**: ① **tester merge(555)** ② **L03_M01 FE wire** `/nursing/service` + **L03_M06 FE wire** ③ G-NURSING live E2E harness run ④ G30·G14/G34/G34b/G42/G19 live API E2E ⑤ 8-12 print live E2E ⑥ G41b `LIVE_E2E=1` ⑦ 7-5 live PG ⑧ J03 Solapi ⑨ v1.3 live E2E ⑩ **L03 4 leaf 잔여(M07·M09·M10·M15)**.

---

### [BNK] BNK-213~216 인사이트 (2026-06-15) — ★ v1.3-B full · L03_M01/M06 BE · G-STAFF-COUNSEL

| BNK | 핵심 | 기획 반영 |
|-----|------|----------|
| **BNK-214** | **v1.3-B TSP suggest API ✅ BE** — `TransportSuggestService`·`TransportRunOptimizer`·V120–V122 @ `db94a65` · 결정 75 PoC closure | ROADMAP v1.3-B △→✅ BE |
| **BNK-215** | **v1.3-B FE wire ✅ full** — `TransportSuggestPanel`·`BranchTransportSettingsPanel` @ `2ffe59f` · **L03_M01 BE ✅** V123 @ `9bd1660` | ROADMAP v1.3-B ✅ full · USER_STORIES US-T02-B · US-O04 M01 △ |
| **BNK-216** | **L03_M06 배설/비위관/도뇨관 BE ✅** V124 @ `a4352a8` · **US-UX-05 deepen** @ `edfba7f`/`3845f0c` | USER_STORIES US-O04 M06 △ · US-UX-05 |
| **BNK-213** | **G-STAFF-COUNSEL P3** — FAQ21804 요양보호사 정기 상담(평가지표 2·5필드·30일 조치) · **v1.3-B WIP→commit** 경로 확정 | REQUIREMENTS §1-5 · ROADMAP P3 |

---

### [PLA] QA 피드백 반영 (2026-06-15, 137차 — BNK-209~212 · TSR 669~680 · L03 ✅ 4 leaf · QA-B86/B87 Fixed · QA-B88/B89/B90 Planned · merge BLOCK)

> **137차 자동 기획 동기화** — BNK-209~212(L03_M14 FE full·L03_M13 oral care·L03_M04 emergency·v1.3-B transport suggest WIP)·TSR 669~680. **QA Open 3 BLOCK** → **Planned**: **QA-B88** · **QA-B89** · **QA-B90** · **QA-B86/B87 Fixed** @ `63cb193`.

| 항목 | 137차 관측 | 조치 |
|------|----------|------|
| **baseline** | FE **`97108f2`** · BE **`090b2d7`** · **299+246 ahead** · FE WT **1U** · BE WT **DIRTY 18** · FE HEAD **1263/1266 FAIL** · BE test **246/246 PASS** · FE test **217/217 PASS** · **78 route** · **63 page** · **V1–V119** | ROADMAP CURRENT BASELINE 137차 갱신 |
| **BNK-209~212** | **★ L03_M14 ✅ full** @ `962858b`/`63cb193` (BNK-210) · **★ L03_M13 ✅ full** @ `bb3dee8`/`faf55f0` V118 (BNK-211) · **★ L03_M04 ✅ full** @ `97108f2`/`81bca68` V119 (BNK-212) · **★ L03 14 leaf 57% 커버**(8/14 ✅) · **★ v1.3-B △ partial+** suggest API WIP @ `090b2d7` · **★ 신규 P2** G24b·G41-COG-REFRESHER·G-ONBOARD-SUPPORT | ROADMAP v3.1·v1.3-B·USER_STORIES US-O04 갱신 |
| **QA** | Open **3 BLOCK** → **Planned** · **QA-B86/B87 Fixed** @ `63cb193` | QA_FEEDBACK Open→Planned · ROADMAP merge **545 BLOCK** |
| **merge gate** | BE+FE **pending** · ⚠ **cross-stream BLOCK** · **545 commits** pending | ROADMAP v1.2.1 `merge_status: pending` |
| **잔여 P0/P1** | **COD QA-B88/B89/B90 fix→WT clean→HEAD test PASS→tester merge(545)** · **v1.3-B suggest API completion** · G-NURSING live E2E run · 요양 기록 reinforce P1 · G30·G14/G34/G34b/G42/G19 live E2E · 7-5 live PG · 8-12 print · J03 Solapi · RFID split-view · **P2 L03 6 leaf** · **P2 G24b·G41-COG-REFRESHER·G-ONBOARD-SUPPORT** · v1.3 live E2E · **P3** G18-SHORT-PILOT·G2 import UX·K008~K014 | ROADMAP v1.2.1·v3.1 갱신 |

**coder 다음 액션 (137차)**: ① **QA-B89 fix** — `PressureUlcerPage.test.jsx` client select mock → HEAD **1266/1266 PASS** ② **QA-B88 fix** — injectable `Clock` WIP 커밋(4M) → WT clean ③ **QA-B90 fix** — transport v1.3-B WIP 커밋/revert(15 files) → WT clean ④ **tester merge(545)** ⑤ **v1.3-B suggest API** completion ⑥ G-NURSING live E2E harness run ⑦ **L03 6 leaf 잔여** ⑧ G30·G14/G34/G34b/G42/G19 live API E2E.

---

### [BNK] BNK-209~212 인사이트 (2026-06-15) — ★ L03_M14/M13/M04 full · v1.3-B WIP · 신규 P2 갭

| BNK | 핵심 | 기획 반영 |
|-----|------|----------|
| **BNK-210** | **L03_M14 체중 1-cycle full** — FE @ `962858b` + BE @ `63cb193` V116~V117 · QA-B86/B87 Fixed | USER_STORIES US-O04 M14 ✅ · ROADMAP v3.1 |
| **BNK-211** | **L03_M13 구강 ✅ full** @ `bb3dee8`/`faf55f0` V118 · **신규 P2** G24b(욕구사정 8항목·FAQ21800)·G41-COG-REFRESHER(반기 교육·FAQ21803) | USER_STORIES US-O04 M13 ✅ · REQUIREMENTS §1-5 |
| **BNK-212** | **L03_M04 응급 ✅ full** @ `97108f2`/`81bca68` V119 · **G-ONBOARD-SUPPORT P2**(silverangel 4회차 SLA) · QA-B89 collateral | USER_STORIES US-O04 M04 ✅ · PLAN_NOTES 추가 질문 |
| **BNK-209** | **v1.3-B transport suggest WIP** — `TransportRunOptimizer`·V120 @ `090b2d7` · 결정 75 PoC | ROADMAP v1.3-B △ partial+ · QA-B90 Planned |

---

### [PLA] QA 피드백 반영 (2026-06-14, 136차 — BNK-204~208 · TSR 657~668 · G-NURSING ✅ full · L03_M11 ✅ full · L03_M14 BE △ · QA-B85 Fixed · QA-B86/B87 Planned · merge BLOCK(BE))

> **136차 자동 기획 동기화** — BNK-204~208(G-NURSING-PRESSURE-ULCER 1-cycle full·L03_M11 vital check full·L03_M14 weight BE V116·FAQ21783 NHIS resilience)·TSR 657~668. **QA Open 2 BLOCK** → **Planned**: **QA-B86** · **QA-B87** · **QA-B85 Fixed** @ `5780c65`.

| 항목 | 136차 관측 | 조치 |
|------|----------|------|
| **baseline** | FE **`246df56`** · BE **`1a822d2`** · **293+241 ahead** · WT **CLEAN** · FE HEAD **1210/1210 PASS** · BE HEAD **1085/1095 FAIL**(10 Errors) · BE test **246/246 PASS** · FE test **217/217 PASS** · **75 route** · **61 page** · **V1–V116** | ROADMAP CURRENT BASELINE 136차 갱신 |
| **BNK-204~208** | **★ G-NURSING-PRESSURE-ULCER P1→✅ full** — BE V114 @ `edda491` + FE @ `e214da1` + pilot/live E2E @ `024e720`/`24a1c5c` (BNK-204~206) · **★ L03_M11 ✅ full** @ `8570fa2`/`80c0bd5` (BNK-207) · **★ L03_M14 BE ✅ partial+** @ `1a822d2` V116 · FE wire ❌ · **★ L03 77%→62% 미커버** · **★ FAQ21783 G2 import resilience P2** | ROADMAP v3.1·USER_STORIES US-O03/O04 갱신 |
| **QA** | Open **2 BLOCK** → **Planned** · **QA-B85 Fixed** @ `5780c65` · **QA-B86/B87 Planned** | QA_FEEDBACK Open→Planned · ROADMAP merge **534 BLOCK** |
| **merge gate** | BE **pending**(HEAD test FAIL) · FE **ready** · ⚠ **cross-stream BLOCK** · **534 commits** pending | ROADMAP v1.2.1 `merge_status: pending` |
| **잔여 P0/P1** | **COD QA-B86/B87 fix→merge(534)** · **L03_M14 FE wire P1** · G-NURSING live E2E run · 요양 기록 reinforce P1 · G30·G14/G34/G34b/G42/G19 live E2E · 7-5 live PG · 8-12 print · J03 Solapi · RFID split-view · **P2 L03 6 leaf** · v1.3 live E2E · **P3** G18-SHORT-PILOT·G2 import UX·K008~K014 | ROADMAP v1.2.1·v3.1 갱신 |

**coder 다음 액션 (136차)**: ① **QA-B86 fix** — `NursingWeightRecordPilotServiceFlowE2eTest` fixture `2098`→과거/당일 또는 `Clock` 주입 → HEAD **1095/1095 PASS** ② **QA-B87 fix** — service-flow E2E에 `@FixedClock`/`NotificationQuietHoursPolicy` stub (KST 22:00~08:00 wall-clock 독립) ③ **tester merge(534)** ④ **L03_M14 FE `NursingWeightRecordPage` wire** ⑤ G-NURSING live E2E harness run ⑥ G30·G14/G34/G34b/G42/G19 live API E2E ⑦ G41b `LIVE_E2E=1` ⑧ 7-5 live PG ⑨ 8-12 print ⑩ J03 Solapi ⑪ G7 실파일 ⑫ US-L01 live ⑬ US-R03 P2 ⑭ v1.3 live E2E.

---

### [BNK] BNK-204~208 인사이트 (2026-06-14) — ★ G-NURSING full · L03_M11 · L03_M14 · FAQ21783

| BNK | 핵심 | 기획 반영 |
|-----|------|----------|
| **BNK-204** | **G-NURSING-PRESSURE-ULCER 1-cycle 풀스택 폐루프** — BE V114 9 endpoints @ `edda491` + FE wire @ `e214da1` (4,243줄/30파일) | ROADMAP v3.1 Must 6번째 ✅ full · USER_STORIES US-O03 |
| **BNK-206** | **검증층 deepen** — pilot 4-step E2E @ `24a1c5c` · API contract+live harness @ `024e720` · input guards @ `d638493` | ROADMAP v3.1 완료 기준 `[x]` |
| **BNK-207** | **L03_M11 통합 바이탈 1-cycle full** — BE V115 @ `80c0bd5` + FE @ `8570fa2` (2,399줄/27파일) | USER_STORIES US-O04 M11 ✅ · L03 9→6 leaf reduction |
| **BNK-208** | **L03_M14 체중 BE closure** — V116 @ `e95df4c`/`1a822d2` · future measure-date guard → **QA-B86** pilot fixture drift | USER_STORIES US-O04 M14 BE △ · QA-B86 Planned |
| **BNK-208** | **FAQ21783 공단서버불안정** — NHIS import 로딩 지연·복구 안내 → **G2 import resilience P2** | REQUIREMENTS §1-5 · PLAN_NOTES 추가 질문 |

---

### [PLA] QA 피드백 반영 (2026-06-14, 135차 — BNK-199~203 · TSR 642~656 · G21 batch-confirm ✅ full · G17b ✅ full · QA-B83/B84 Fixed · merge FULLY UNBLOCKED)

> **135차 자동 기획 동기화** — BNK-199~203(G21 batch-confirm 5-cycle·G17b 인지활동형 미제공 사유 4-cycle V112/V113·demo L03 간호급여 13 leaf·demo L02 요양기록 15 leaf·G18-SHORT-PILOT·MOHW 247 HWPX 제32조)·TSR 642~656. **QA Open 0건** · **QA-B83 Fixed** @ `4ba7ea6`(US-UX-05 SideNav WT dirty closure) · **QA-B84 Fixed** @ `3bd6a43`(G17b ProgramService WT dirty closure) · **Open→Planned 이동 없음**(WT dirty BLOCK은 모두 coder 커밋으로 자체 해소).

| 항목 | 135차 관측 | 조치 |
|------|----------|------|
| **baseline** | FE **`ad319d7`** · BE **`3bd6a43`** · **286+235 ahead** · WT **CLEAN** · HEAD **1164/1164 PASS** · BE test **246/246 PASS** · FE test **217/217 PASS** · **69 route** · **59 page** · **V1–V113** | ROADMAP CURRENT BASELINE 135차 갱신 |
| **BNK-199~203** | **★ G21 batch-confirm partial+→✅ full**(FE+BE+E2E 5-cycle @ `13e691e`/`c22a5dc`) · **★ G17b 인지활동형 미제공 사유 ✅ full**(BE V112 `6b7e6cb`→V113 `ba7d84f`→ABSENT 가드 `3bd6a43` + FE `c26cfa7`/`487416d`·MOHW 제32조) · **★★ 신규 갭 G-NURSING-PRESSURE-ULCER**(dual-source·v3.1 Must 6번째·P1) · **★ demo L03 간호급여 13 leaf 77% 미커버**(P2) · **★ demo L02 요양기록 15 leaf 33% gap reinforce**(P1) · **★ G18-SHORT-PILOT P3** | ROADMAP v3.1 범위·완료 기준·USER_STORIES Epic O 갱신 |
| **QA** | Open **0건** · **QA-B83/B84 Fixed** · SEC-D22 **Planned** | QA_FEEDBACK 갱신 · 이동 없음 |
| **merge gate** | BE+FE **ready** · ★ **FULLY UNBLOCKED** · **521 commits** pending | ROADMAP v1.2.1 `merge_status: ready` |
| **잔여 P0/P1** | **tester merge(521)** · **★ G-NURSING-PRESSURE-ULCER 4단(P1)** · **요양 기록 reinforce(P1)** · G21 batch-confirm live E2E · G30·G14/G34/G34b/G42/G19 live API E2E · 7-5 live PG·8-12 print·J03 Solapi·RFID split-view·G41b `LIVE_E2E`(P2) · **L03 간호급여 9 leaf(P2)** · v1.3 live E2E · **P3** G18-SHORT-PILOT·G-FAMILY-LEAVE·G-RURAL-SUBSIDY·G-PROG-MGR-BONUS·LCMS·K008~K014 | ROADMAP v1.2.1·v3.1 갱신 |

**coder 다음 액션 (135차)**: ① **tester merge(521)** ② G21 batch-confirm·G30·G14/G34/G34b/G42/G19 **live API E2E run** ③ G41b `LIVE_E2E=1` manual verify ④ 7-5 live PG·8-12 print·J03 Solapi·RFID split-view P2 ⑤ G7 실파일 ⑥ G2 SMTP+FCMS ⑦ US-L01 live ⑧ US-R03 P2 ⑨ v1.3 live E2E ⑩ **v3.1 착수 시 G-NURSING-PRESSURE-ULCER·요양 기록 reinforce 우선화**.

---

### [BNK] BNK-199~203 인사이트 (2026-06-14) — ★ G21 5-cycle · G17b 4-cycle · G-NURSING-PRESSURE-ULCER

| BNK | 핵심 | 기획 반영 |
|-----|------|----------|
| **BNK-199** | **G21 batch-confirm 5-cycle 폐루프 완전 닫힘** — `VisitBatchConfirmPanel` 242줄+pilot E2E + BE unassigned/paired-diverged ID lists · FAQ rowid 상한 ~21845 | ROADMAP v2 G21 ✅ full · USER_STORIES US-V05 |
| **BNK-200** | **demo L02 요양기록 15 leaf 전수·33% gap** — 주간 한장기록지·집중배설관찰·식사 sub 4종·신체제재·체위변경 리포트 ❌ | **결정 94 v3.1 Must reinforce** · ROADMAP v3.1 범위·완료 기준 |
| **BNK-201** | **G17b BE 폐루프 V112** · **angelsitter 단기보호 시범사업** 2026.7.1~·야간운영비 64,000원·가족휴가제 연12일 | ROADMAP v3.1 **G18-SHORT-PILOT P3** |
| **BNK-202** | **G17b 인지활동형 미제공 사유 FE+BE 3-cycle 폐루프** — V113·`ProgramService.resolveSkipReason`·MOHW 제32조 1:1 | REQUIREMENTS G17b · ROADMAP v2 G17b ✅ full |
| **BNK-203** | **★★ 신규 갭 G-NURSING-PRESSURE-ULCER**(욕창 케어 lifecycle·dual-source silverangel 평가지표+케어포 demo L03 4 leaf) → **v3.1 Must 6번째·결정 94** · **demo L03 간호급여 13 leaf 77% 미커버 P2** · G17b 4-cycle deepen(BE WT dirty closure) | ROADMAP v3.1 **G-NURSING-PRESSURE-ULCER P1**·**L03 9 leaf P2** · USER_STORIES Epic O |

---

### [PLA] QA 피드백 반영 (2026-06-14, 134차 — BNK-195~198 · TSR 634~641 · G21 batch-confirm ✅ partial+ · US-UX-05 ✅ · QA-B81/B82 Fixed · merge FULLY UNBLOCKED)

> **134차 자동 기획 동기화** — BNK-195~198(J03 4-cycle·V111 guardian link·FAQ21782 일정확정·G21 batch-confirm BE+FE·US-UX-05·G42 anonymous box·MOHW 247 HWPX)·TSR 634~641. **QA Open 0건** · **QA-B81 Fixed** @ `56f0204` · **QA-B82 Fixed** @ `360b4d7` · **Open→Planned 이동 없음**(132차 Planned에서 coder Fixed 처리).

| 항목 | 134차 관측 | 조치 |
|------|----------|------|
| **baseline** | FE **`13e691e`** · BE **`c22a5dc`** · **280+232 ahead** · WT **CLEAN** · HEAD **1149/1149 PASS** · BE test **246/246 PASS** · FE test **217/217 PASS** · **69 route** · **59 page** · **V1–V111** | ROADMAP CURRENT BASELINE 갱신 |
| **BNK-195~198** | **★ J03 quiet-hours partial+→✅ full** — 4-cycle @ `56f0204`/`e5b4b88`→`360b4d7`/`dbecd72`→`a057739` · **★ G21 batch-confirm ✅ partial+** — BE @ `0b807d8`/`c22a5dc` + FE @ `13e691e` · **★ US-UX-05 ✅** @ `1e111be`/`8a8b930` · **★ MOHW 2025-247 HWPX 정본** · **★ 신규 갭 4건** G17b·G-FAMILY-LEAVE·G-RURAL-SUBSIDY·G-PROG-MGR-BONUS | REQUIREMENTS·USER_STORIES US-V05·ROADMAP merge **512 UNBLOCKED** |
| **QA** | Open **0건** · **QA-B81 Fixed** @ `56f0204` · **QA-B82 Fixed** @ `360b4d7` · SEC-D22 **Planned** | QA_FEEDBACK 갱신 · 이동 없음 |
| **merge gate** | BE+FE **ready** · ★ **FULLY UNBLOCKED** · **512 commits** pending | ROADMAP v1.2.1 `merge_status: ready` |
| **잔여 P0/P1** | **tester merge(512)** · **G21 batch-confirm live E2E P1** · G30·G14/G34/G34b/G42/G19 **live API E2E** · G41b `LIVE_E2E` P2 · 7-5 live PG P2 · 8-12 print P2 · J03 Solapi live P2 · US-L01 live · US-R03 P2 · v1.3 live E2E · **P2** G17b·RFID split-view · **P3** LCMS·G9-COPAY-503·K008~K014·신규 4갭 | ROADMAP v1.2.1·v2 갱신 |

**coder 다음 액션 (134차)**: ① **tester merge(512)** ② **G21 batch-confirm `pilotPageFlows` E2E** ③ G30·G14/G34/G34b/G42/G19 **live API E2E run** ④ G41b `LIVE_E2E=1` manual verify ⑤ G21·RFID·확정 lock P2 ⑥ 8-12 print P2 ⑦ J03 Solapi live P2 ⑧ G7 실파일 ⑨ G2 SMTP+FCMS ⑩ US-L01 live ⑪ US-R03 P2 ⑫ v1.3 live E2E ⑬ **DESIGN_SYSTEM §8-2** SideNav 문서 동기화.

---

### [BNK] BNK-195~198 인사이트 (2026-06-14) — ★ G21 batch-confirm · US-UX-05 · MOHW 247 HWPX

| BNK | 핵심 | 기획 반영 |
|-----|------|----------|
| **BNK-195** | **J03 shared quiet-hours policy** @ `a057739` — `NotificationQuietHoursPolicy` 단일 정책 · dispatch↔readiness drift 차단 | USER_STORIES US-J03 · J03-readiness ✅ full |
| **BNK-196** | **V111 guardian link guard** @ `dbecd72` · **J03 UXD-101 a11y** @ `360b4d7` | REQUIREMENTS 7-5 · US-L06 |
| **BNK-197** | **FAQ21782 일정확정 5단** — 공단 비교·변경이력 ack · **G21 batch-confirm BE** @ `0b807d8` | USER_STORIES **US-V05** · API_SPEC §14 |
| **BNK-198** | **★ G21 4-cycle 폐루프** — BE batch-confirm @ `0b807d8`/`c22a5dc` + FE @ `13e691e` · **US-UX-05 ✅** · **MOHW 247 HWPX** · **신규 갭 4건** | ROADMAP v2 · REQUIREMENTS §1-5 |

---

### [USR] 사용자 요청 — 배차 자동 최적화 변수·제약 (2026-06-14, 133차)

> **요청 원문 (변수 조건)**: 센터 운행 차량 대수 · 어르신 총 인원 · 어르신 개별 특이사항(예: 아침 9시 반드시 픽업)  
> **요청 원문 (목표)**: 운전자별 모시는·내리는 어르신 **변동 최소** · 운전자별 **등하원 운행 거리 공정성**  
> **기획 반영**: REQUIREMENTS **§3-13-9** · USER_STORIES **US-T02-B** · ROADMAP v1.3-B 완료 기준 · PLAN_NOTES **결정 74**

| 항목 | 133차 판단 | 조치 |
|------|-----------|------|
| **범위** | v1.3-A(단일 run·수동)와 **분리** — **v1.3-B 다중 차량 자동 배차 제안** | §3-13-9 신설 |
| **변수 V1~V3** | `vehicles` 정원·roster 총 인원·`default_pickup_time`+`transport_notes` | DBA `clients.transport_notes` · API `POST …/runs/suggest` |
| **목표 O1~O2** | TSP 단순 최단거리(PLAN_NOTES #41 ④) **확장** — **담당 안정성·거리 공정성** soft 우선 | `w1,w2 > w3` 가중치 |
| **확정 흐름** | 자동 **제안** → `hq_admin` **수동 조정** → US-T02 확정 (기존 게이트 유지) | 변경 없음 |
| **우선순위** | **v1.3-B Should** — v1.3-A·C 완료 후 착수 | ROADMAP v1.3-B 갱신 |

**결정 74 (133차)**: v1.3-B 자동 배차는 ① **차량 대수·총 인원·개별 특이사항**을 Hard/Soft 입력으로 받고, ② **운전자별 담당 안정성(O1)·등하원 거리 공정성(O2)**을 **단순 최단거리(O3)보다 우선**하는 soft 목표로 최적화한다. `hq_admin` 수동 오버라이드·확정 게이트는 v1.3-A와 동일.

---

### [PLA] QA 피드백 반영 (2026-06-14, 132차 — BNK-191~194 · TSR 623~633 · 7-5 ✅ full · J03 quiet-hours ✅ partial+ · QA-B81/B82 Planned · merge BLOCK(FE))

> **132차 자동 기획 동기화** — BNK-191~194(7-5 V110 integrity·provider normalize·route alias·J03 quiet-hours FE+BE 3-cycle·longterm 503 감경·LCMS 3단 온보딩·#44 67차)·TSR 623~633. **QA Open 2 BLOCK** → **Planned**: **QA-B81**(FE test FAIL) · **QA-B82**(FE WT dirty) · **cross-stream merge BLOCK**.

| 항목 | 132차 관측 | 조치 |
|------|----------|------|
| **baseline** | FE **`111f056`** · BE **`a057739`** · **274+226 ahead** · BE WT **CLEAN** · FE WT **DIRTY 2M** · HEAD **1141/1143 FAIL** · BE test **246/246 PASS** · **69 route** · **59 page** · **V1–V110** | ROADMAP CURRENT BASELINE 갱신 |
| **BNK-191~194** | **★ 7-5 partial+→✅ full** — prior-month guard commit @ `bebd874`/`b893e97` → V110 @ `16a0734`/`51f2505` → hardening @ `745a2f6`/`328874d` → route alias @ `8f9ad0c`/`7ec7cd4` · **★ J03 ✅ partial+** — quiet-hours FE billing-notify block @ `111f056` · BE dispatch+boundary @ `328874d`/`a057739` · **★ longterm 503 감경 P3** · **★ #44 67차 carry** | REQUIREMENTS·USER_STORIES US-L06/US-J03 · ROADMAP merge **500 BLOCK** |
| **QA-B81/B82** | FE `@111f056` HEAD **1141/1143 FAIL** + WT **DIRTY 2M** · BE `@a057739` WT **CLEAN** | Open→Planned · COD test fix+route alias commit → WT clean → tester merge(500) |
| **merge gate** | BE **ready** · FE **BLOCK** · ⚠ **cross-stream BLOCK** · **500 commits** pending | ROADMAP v1.2.1 `merge_status: pending` |
| **잔여 P0/P1** | **COD QA-B81/B82 fix→merge(500)** · **7-5 route alias commit** · **7-5 live PG P2** · G30·G14/G34/G34b/G42/G19 **live E2E** · G41b LIVE_E2E P2 · G21·RFID P2 · 8-12 print P2 · J03 Solapi live P2 · US-L01 live · US-R03 P2 · v1.3 live E2E · **US-UX-05 P1** · **P3** LCMS 평가 role·G9-COPAY-503·K008~K014 | ROADMAP v1.2.1·v2 갱신 |

**coder 다음 액션 (132차)**: ① **QA-B81 fix** — `pilotPageFlows.test.jsx` quiet-hours KST mock 또는 차단 메시지 assertion → HEAD **1143/1143 PASS** ② **QA-B82 fix** — `services.js`+`billingGuardianPlatformServices.test.js` 커밋 또는 revert → WT clean ③ **tester merge(274+226=500)** ④ **7-5 live PG P2** ⑤ G30·G14/G34/G34b/G42/G19 **live API E2E run** ⑥ G41b `LIVE_E2E=1` manual verify ⑦ G21·RFID·확정 lock P2 ⑧ 8-12 print P2 ⑨ J03 Solapi live P2 ⑩ G7 실파일 ⑪ G2 SMTP+FCMS ⑫ US-L01 live ⑬ US-R03 P2 ⑭ v1.3 live E2E ⑮ **US-UX-05 SideNav 토글**.

---

### [BNK] BNK-191~194 인사이트 (2026-06-14) — ★ 7-5 full · J03 quiet-hours 3-cycle · longterm 503 감경

| BNK | 핵심 | 기획 반영 |
|-----|------|----------|
| **BNK-191** | **7-5 전월 가드 WT dirty 7파일 커밋** @ `bebd874`/`b893e97` · PDF p.87·func.php 64차 zero drift | ROADMAP 7-5 carry |
| **BNK-192** | **★★★ 7-5 4-cycle hardening 완료** — V110 integrity CHECK 10종 @ `16a0734` · EasyPayPanel a11y @ `51f2505` · func.php 65차 zero drift | USER_STORIES **US-L06** ✅ full |
| **BNK-193** | **7-5 provider normalization deepen** @ `745a2f6`/`328874d` · **J03 quiet-hours BE dispatch tests** · 이지케어 이중일정 4단 evidence | USER_STORIES US-J03 · G21 P1 |
| **BNK-194** | **★ J03 quiet-hours FE+BE 3-cycle ✅ partial+** @ `111f056`/`a057739` · **longterm 503 감경** 50%/60%·14일 SLA · **#44 67차** | REQUIREMENTS G9-COPAY-503 P3 · PLAN_NOTES |

---

### [USR] 사용자 요청 — SideNav 5그룹 접힘/펼침 토글 (2026-06-14, 131차)

> **요청 원문**: 「사이드바의 **운영, 이동, 출석, 기록, 청구**를 **토글**로 해서 **클릭 시 하위메뉴**가 나오게」  
> **기획 반영**: **US-UX-05** (v1.2.1 P1) · REQUIREMENTS §3-0 · ROADMAP v1.2.1 P1 · DESIGN_SYSTEM §8-2 갱신 예정

| 항목 | 131차 판단 | 조치 |
|------|-----------|------|
| **현재 구현** | `SideNav.jsx` + `navConfig.js` — 5그룹·`button` 토글·`aria-expanded` **스켈레톤 ✅** | US-UX-02 lineage |
| **갭** | 초기값 **전 그룹 펼침** · DESIGN_SYSTEM 「데스크톱 항상 펼침」 — 사용자 기대(**클릭 시 하위 노출·기본 접힘**)와 **미정합** | **US-UX-05 Planned** |
| **범위** | 운영(`operations`)·이동(`transport`)·출석(`attendance`)·기록(`records`)·청구(`billing`) — 역할별 `navGroupsForRole` 필터 **유지** | USER_STORIES US-UX-05 |
| **우선순위** | **v1.2.1 P1 Should** — merge-blocking 아님 · UX 완성 | ROADMAP v1.2.1 잔여 P1 |
| **선행** | US-UX-02 2단 그룹 구조 ✅ · ContextNav(출석·기록·청구·이동) **병행 유지** | 변경 없음 |

**동작 확정안 (131차)**

1. 그룹 헤더 클릭 → 하위 `NavLink` 목록 접힘/펼침.
2. **초기: 전 그룹 접힘** + **현재 route 부모 그룹만 auto-expand**.
3. **다중 그룹 동시 펼침 허용** (accordion 아님).
4. **모바일·데스크톱 동일** — 「769px+ 항상 펼침」 규칙 **폐기**.
5. `sessionStorage` 상태 유지 — **P2 후속**.

**coder 다음 액션 (131차)**: ① **`SideNav.jsx`** — 초기 `expanded`를 route 기반 auto-expand로 변경 · 전 그룹 default collapsed ② **`SideNav.test.jsx`** — 활성 그룹 auto-expand·토글 회귀 ③ **`DESIGN_SYSTEM §8-2`**·**`USER_MANUAL §3-1`** 동기화 ④ (선택 P2) sessionStorage persist.

---

### [PLA] QA 피드백 반영 (2026-06-14, 130차 — BNK-188~190 · TSR 612~622 · 7-5 ✅ partial+ · QA-B78/B79 Planned · merge BLOCK)

> **130차 자동 기획 동기화** — BNK-188~190(G41b V107·7-5 skeleton+pilot E2E+prior-month guard·MOHW 2025-247·silverangel 지표41/42·LCMS 평가 SLA)·TSR 612~622. **QA Open 2 BLOCK** → **Planned**: **QA-B78**(BE)·**QA-B79**(FE) · **cross-stream merge BLOCK**.

| 항목 | 130차 관측 | 조치 |
|------|----------|------|
| **baseline** | FE **`bebd874`** · BE **`b893e97`** · **269+220 ahead** · WT **DIRTY**(BE 2M·FE 3M+1U) · HEAD **1126/1126 PASS** · WT **1128/1128 PASS** · **69 route** · **59 page** · **V1–V109** | ROADMAP CURRENT BASELINE 갱신 |
| **BNK-188~190** | **★ G41b V107 ✅** @ `ee42e5d` · **★ 7-5 ✅ partial+** — skeleton @ `c9baca2`/`438f5c7` · pilot E2E @ `3848af6`/`1231389` · prior-month guard @ `bebd874`/`b893e97` · **★ MOHW 2025-247** · **★ LCMS 평가 read-only role P3** · **★ silverangel 지표41/42 carry** | REQUIREMENTS·USER_STORIES US-L06 · API_SPEC §9-15 · ROADMAP merge **489 BLOCK** |
| **QA-B78/B79** | BE `@b893e97` WT **DIRTY 2M**(provider normalization) · FE `@bebd874` WT **DIRTY 3M+1U** · TSR 620차 CLEAN→재오염 | Open→Planned · COD 커밋/revert → WT clean → tester merge(489) |
| **merge gate** | BE+FE **BLOCK** · ⚠ **cross-stream BLOCK** · **489 commits** pending | ROADMAP v1.2.1 `merge_status: pending` |
| **잔여 P0/P1** | **COD QA-B78/B79 fix→merge(489)** · **7-5 provider normalization commit** · **7-5 live PG P2** · G30·G14/G34/G34b/G42/G19 **live E2E** · G41b LIVE_E2E P2 · G21·RFID P2 · 8-12 print P2 · J03 Solapi P2 · US-L01 live · US-R03 P2 · v1.3 live E2E · **P3** LCMS 평가 role·G-STAFF-WELFARE·K008~K014 | ROADMAP v1.2.1·v2 갱신 |

**coder 다음 액션 (130차)**: ① **QA-B78/B79 fix** — BE `CreateEasyPayPaymentRequest`+RBAC test · FE `EasyPayPanel`+`easyPay.js`+tests 커밋 또는 revert → WT clean ② **tester merge(269+220=489)** ③ **7-5 live PG P2** ④ G30·G14/G34/G34b/G42/G19 **live API E2E run** ⑤ G41b `LIVE_E2E=1` manual verify ⑥ G21·RFID·확정 lock P2 ⑦ 8-12 print P2 ⑧ J03 Solapi·quiet-hours P2 ⑨ G7 실파일 ⑩ G2 SMTP+FCMS ⑪ US-L01 live ⑫ US-R03 P2 ⑬ v1.3 live E2E.

---

### [BNK] BNK-188~190 인사이트 (2026-06-14) — ★ 7-5 partial+ · MOHW 2025-247 · LCMS 평가 SLA

| BNK | 핵심 | 기획 반영 |
|-----|------|----------|
| **BNK-188** | **G41 hardcoded 7일 제거** @ `e14ba10` · **G41b V107 ✅** @ `ee42e5d` · **PDF p.85–92 7-x workflow** · demo-work 52차 DRIFT | ROADMAP v1.2.1 · REQUIREMENTS 7-x |
| **BNK-189** | **★★★ 7-5 `npay_manage` 폐루프 착수** — `/billing/easy-pay`·Stub PG @ `c9baca2`/`438f5c7` · **69 route** · FAQ21835 stub 번복 | USER_STORIES **US-L06** · API_SPEC §9-15 |
| **BNK-190** | **7-5 pilot E2E deepen** @ `3848af6`/`1231389` · **MOHW 2025-247** HTML · **silverangel 지표41/42** · **LCMS 평가 read-only role P3** · longterm610·lawImg DRIFT carry | REQUIREMENTS G-LCMS-EVAL · PLAN_NOTES |

---

### [PLA] QA 피드백 반영 (2026-06-14, 129차 — BNK-185~187 · TSR 600~611 · G41/G41b ✅ partial+ · QA-B76/B77 Fixed · merge FULLY UNBLOCKED)

> **129차 자동 기획 동기화** — BNK-185~187(G41b 4분류·compliance API+FE·live E2E harness·orientation min-date·FAQ21807 반기 nuance·G-STAFF-WELFARE·G-ONBOARD-SUPPORT)·TSR 600~611. **QA Open 0건(active)** · **QA-B76/B77 Fixed** · **Open→Planned 이동 없음**(tester가 Open→Fixed 직접 처리 · Planned §에 기록 유지).

| 항목 | 129차 관측 | 조치 |
|------|----------|------|
| **baseline** | FE **`e14ba10`** · BE **`32f87f1`** · **264+215 ahead** · WT **CLEAN** · HEAD **1110/1110 PASS** · **66 route** · **57 page** · **V1–V106** | ROADMAP CURRENT BASELINE 갱신 |
| **BNK-185~187** | **★ G41/G41b ✅ partial+** — 184→187 **4-cycle** @ `613b6af`/`e69bf00`→`0f11158`/`38d24b6`→`299d21f`/`a4ab0c2`/`76fe2fb`→`32f87f1`/`e14ba10` · **★ G-STAFF-WELFARE P3** — FAQ21796 · **★ G-ONBOARD-SUPPORT P2** — silverangel 14필드 · **★ FAQ21807** 연1회→**반기1회+** · **★ QA-B76 Fixed** @ `299d21f` · **★ QA-B77 Fixed** @ `76fe2fb` | REQUIREMENTS·USER_STORIES·API_SPEC §9-14 · ROADMAP merge **479 UNBLOCKED** |
| **QA** | Open **0건** · **QA-B76 Fixed** @ `299d21f` · **QA-B77 Fixed** @ `76fe2fb` · SEC-D22 **Planned** | QA_FEEDBACK 갱신 · 이동 없음 |
| **merge gate** | BE+FE **ready** · ★ **FULLY UNBLOCKED** · **479 commits** pending | ROADMAP v1.2.1 `merge_status: ready` |
| **잔여 P0/P1** | **tester merge(479)** · **G41b `LIVE_E2E` manual verify P2** · G30·G14/G34/G34b/G42/G19 **live E2E** · G21·RFID·확정 lock P2 · 8-12 print P2 · J03 Solapi·quiet-hours P2 · US-L01 live · US-R03 P2 · v1.3 live E2E · **P3** G-STAFF-WELFARE·K008~K014·G-HOMEPAGE | ROADMAP v1.2.1·v2 갱신 |

**coder 다음 액션 (129차)**: ① **tester merge(479)** ② **G41b `LIVE_E2E=1` manual verify** ③ G30·G14/G34/G34b/G42/G19 **live API E2E run** ④ G21·RFID·확정 lock P2 ⑤ 8-12 print P2 ⑥ J03 Solapi·quiet-hours P2 ⑦ G7 실파일 ⑧ G2 SMTP+FCMS ⑨ US-L01 live ⑩ US-R03 P2 ⑪ v1.3 live E2E.

---

### [BNK] BNK-185~187 인사이트 (2026-06-14) — ★ G41/G41b 4-cycle · G-STAFF-WELFARE · G-ONBOARD-SUPPORT

| BNK | 핵심 | 기획 반영 |
|-----|------|----------|
| **BNK-185** | **G41b 4분류 FE+BE** @ `613b6af`/`e69bf00` · **FAQ21796 직원복지(포상) P3** | REQUIREMENTS G-STAFF-WELFARE · USER_STORIES US-S03 |
| **BNK-186** | **compliance API+FE** @ `0f11158`/`38d24b6` · **G-ONBOARD-SUPPORT 14필드 P2** | API_SPEC §9-14 · PLAN_NOTES G-ONBOARD |
| **BNK-187** | **live E2E harness** @ `a4ab0c2` · **orientation min-date** @ `299d21f` · **QA-B76/B77 Fixed** · **66 route** 정정 | USER_STORIES US-S04 · ROADMAP merge **479** |

---

### [PLA] QA 피드백 반영 (2026-06-14, 128차 — BNK-180~184 · TSR 587~599 · G30 ✅ full · G34-QUAL ✅ partial+ · G41 △ BE · QA-B74 Fixed · merge FULLY UNBLOCKED)

> **128차 자동 기획 동기화** — BNK-180~184(G34-QUAL 4-cycle·G30 checklist 3-cycle·G41 training log BE·G41b 갭·G21 확정 lock)·TSR 587~599. **QA Open 0건(active)** · **Open→Planned 이동 없음** · **QA-B74 Fixed @ `cfd87c5`**.

| 항목 | 128차 관측 | 조치 |
|------|----------|------|
| **baseline** | FE **`5146895`** · BE **`6191b91`** · **257+211 ahead** · WT **CLEAN** · HEAD **1094/1094 PASS** · **67 route** · **V1–V104** | ROADMAP CURRENT BASELINE 갱신 |
| **BNK-180~184** | **★ G34-QUAL ✅ partial+** — 177→183 4-cycle @ `574bd08`/`997831c` · **★ G30 ✅ full** — checklist @ `b1dfd34`/`400c835`/`5146895` · **★ G41 △ BE** — V104 @ `6191b91` · **★ G41b P2** · **★ QA-B74 Fixed** | REQUIREMENTS·USER_STORIES·API_SPEC §9-12~14 · ROADMAP merge **468 UNBLOCKED** |
| **QA** | Open **0건** · **QA-B74 Fixed** @ `cfd87c5` · SEC-D22 **Planned** | QA_FEEDBACK 갱신 · 이동 없음 |
| **merge gate** | BE+FE **ready** · ★ **FULLY UNBLOCKED** · **468 commits** pending | ROADMAP v1.2.1 `merge_status: ready` |
| **잔여 P0/P1** | **tester merge(468)** · **G41 FE wire P2** · **G30 live API E2E** · G14·G34/G34b/G42 live E2E · **8-12 print P2** · **J03 Solapi·quiet-hours P2** · **G21 확정 lock P2** · G19 P1 · US-L01 live · US-R03 P2 · v1.3 live E2E · **P3** K008~K014·G-HOMEPAGE·G41b | ROADMAP v1.2.1·v2 갱신 |

**coder 다음 액션 (128차)**: ① **tester merge(468)** ② **G41 FE wire** ③ **G30 live API E2E** ④ G14·G34/G34b/G42 live E2E ⑤ **8-12 print P2** ⑥ **J03 Solapi·quiet-hours P2** ⑦ **G21 확정 lock P2** ⑧ G7 실파일 ⑨ G2 SMTP+FCMS ⑩ **G41b 3분류 P2** ⑪ US-L01 live ⑫ US-R03 P2 ⑬ v1.3 live E2E.

---

### [BNK] BNK-180~184 인사이트 (2026-06-14) — ★ G30 full · G34-QUAL partial+ · G41 BE

| BNK | 핵심 | 기획 반영 |
|-----|------|----------|
| **BNK-180** | **G34-QUAL FE+BE** @ `726b3de` · FAQ21837 5년 gate | REQUIREMENTS G34-QUAL |
| **BNK-181** | **pilot E2E GREEN** · **이지케어 일정확정 lock·RFID** | ROADMAP G21 P2 |
| **BNK-182** | **compliance API** @ `9a8bd2a` | API_SPEC §9-13 |
| **BNK-183** | **G34-QUAL FE panel** @ `574bd08` · **G30 checklist BE** @ `b1dfd34` | USER_STORIES US-T15 |
| **BNK-184** | **G30 checklist FE+E2E** @ `5146895` · **G41 BE** @ `6191b91` · **G41b 갭** | USER_STORIES **US-S04** |

---

### [PLA] QA 피드백 반영 (2026-06-14, 127차 — BNK-176~179 · TSR 574~586 · 8-12 ✅ partial+ · J03 readiness ✅ partial+ · QA-B74 Planned · merge BLOCK(FE))

> **127차 자동 기획 동기화** — BNK-176~179(8-12 BE CSV FE wire·pagination·G42 modal a11y·J03 channel readiness API+FE panel·email/quiet-hours deepen·G21 closure·G34-QUAL team lead gate·refresher API refactor)·TSR 574~586. **QA Open 0건(active)** · **QA-B74 Open→Planned** · merge **455 BLOCK(FE)**.

| 항목 | 127차 관측 | 조치 |
|------|----------|------|
| **baseline** | FE **`443efca`** · BE **`229f84c`** · **250+205 ahead** · WT **CLEAN** · HEAD **1081/1082 FAIL** · **66 route** · **V1–V103** | ROADMAP CURRENT BASELINE 갱신 |
| **BNK-176~179** | **★ #44 P0 ✅ carry** · **★ 8-12 ✅ partial+** — BE CSV FE wire @ `488f547` · pagination @ `ff173af` · G42 modal @ `6012044` · **★ J03 ✅ partial+** — channel-status API @ `d4acab7` · FE panel @ `6b1258c`/`d695923` · email/quiet-hours @ `fffd355` · **★ G21 closure** @ `c16f4fe` · **★ G34-QUAL P2** · **★ QA-B74 Planned** | REQUIREMENTS·USER_STORIES·API_SPEC §9-11·§11-10 · ROADMAP merge **455 BLOCK** |
| **QA-B74** | `@443efca` refresher compliance API refactor → `pilotPageFlows` stale `/api/v1/users` mock · **1081/1082 FAIL** | Planned → COD fix mock → **1082/1082 PASS** → tester merge(455) |
| **merge gate** | BE **ready** · FE **BLOCK** · ⚠ **cross-stream BLOCK** · **455 commits** pending | ROADMAP v1.2.1 `merge_status: pending` |
| **잔여 P0/P1** | **COD QA-B74 fix→merge(455)** · **G30 live E2E verify** · G14·G34/G34b/G42 **live API E2E run** · **8-12 print layout P2** · **J03 live Solapi E2E·quiet-hours BE enforce P2** · **G34-QUAL P2** · G19 통합재가 P1 · US-L01 live · US-R03 P2 · v1.3 live E2E · **P3** K008~K014·G-HOMEPAGE·G9-SHORT/G9-DEMENTIA/G9-DR | ROADMAP v1.2.1·v2 우선순위 갱신 |

**coder 다음 액션 (127차)**: ① **QA-B74 fix** — `pilotPageFlows.test.jsx` mock/assertion → `/api/v1/staff/refresher-training/compliance` · develop HEAD **1082/1082 PASS** ② **tester merge(250+205=455)** ③ **G30 live E2E verify** ④ G14·G34/G34b/G42 **live API E2E run** ⑤ **8-12 print layout P2** ⑥ **J03 live Solapi E2E·quiet-hours dispatch BE enforce P2** ⑦ **G34-QUAL team lead 5yr gate P2** ⑧ G7 **실파일**(#27) ⑨ G2 **SMTP+FCMS 실연동** ⑩ US-L01 **은행 8종 E2E live** ⑪ **US-R03 P2** ⑫ v1.3 live E2E.

---

### [BNK] BNK-176~179 인사이트 (2026-06-14) — ★ 8-12 partial+ · J03 readiness · G34-QUAL · QA-B74

| BNK | 핵심 | 기획 반영 |
|-----|------|----------|
| **BNK-176** | **8-12 BE CSV FE wire ✅** @ `488f547` · **G42 modal a11y ✅** @ `6012044` · **#44 P0 ✅ carry** @ `39ee679` | USER_STORIES US-R02 · API_SPEC §9-11 |
| **BNK-177** | **J03 channel readiness BE API ✅** @ `d4acab7` · **FAQ21837 G34-QUAL P2 신규** | API_SPEC §11-10 · REQUIREMENTS G34-QUAL |
| **BNK-178** | **8-12 pagination ✅** @ `ff173af` · **G21 WT dirty closure** @ `c16f4fe` | USER_STORIES US-R02 · ROADMAP |
| **BNK-179** | **J03 FE panel ✅ partial+** @ `6b1258c`/`d695923` · **email/quiet-hours deepen** @ `fffd355` · **refresher API refactor** @ `443efca` → **QA-B74** | USER_STORIES US-J03 · US-S02 · QA-B74 Planned |

---

### [PLA] QA 피드백 반영 (2026-06-14, 126차 — BNK-172~175 · TSR 562~573 · #44 P0 ✅ · 8-12 deepen · G42 partial+ · QA-B72 Fixed · merge FULLY UNBLOCKED)

> **126차 자동 기획 동기화** — BNK-172~175(8-12 PDF 7종 FE·live E2E harness·BE CSV export·#44 NHIS lawImg 정본·V103 seed 보정·G42 follow-up UI+API·duplicate approval UX·silverangel websiteProvided·FAQ21833 K012)·TSR 562~573. **QA Open 0건** · **QA-B72 Fixed @ `a7a6004`** · **Open→Planned 이동 없음**.

| 항목 | 126차 관측 | 조치 |
|------|----------|------|
| **baseline** | FE **`a7a6004`** · WT **CLEAN** · HEAD **1067/1067 PASS** · BE **`39ee679`** · WT **CLEAN** · **243+200 ahead** · **67 route** · **V1–V103** | ROADMAP CURRENT BASELINE **126차** 갱신 |
| **BNK-172~175** | **★ #44 P0 ✅** @ `39ee679`(5230/8630) · **★ 8-12 deepen** — PDF 7종 FE·live E2E·BE CSV @ `07956f5`/`ccc4d75`/`bc927f7` · **★ G42 ✅ partial+** @ `14124d6`/`bcb1d9f`/`892450a`/`a7a6004` · **★ G30 V101** @ `f4c8558` · **★ G-HOMEPAGE P3** · **★ FAQ21833 K012 P3** | REQUIREMENTS·USER_STORIES·API_SPEC §9-11 · ROADMAP merge **443** UNBLOCKED |
| **QA** | Open **0건** · **QA-B72 Fixed** @ `a7a6004` · SEC-D22 **Planned** | QA_FEEDBACK 갱신 · 이동 없음 |
| **merge gate** | P0 `[x]` · BE+FE **ready** · ★ **FULLY UNBLOCKED** · 합계 **443 commits** | tester merge **443** 즉시 가능 |
| **잔여 P0/P1** | merge(443) · **G30 live E2E verify** · G14·G34/G34b/G42 **live API E2E run** · **8-12 BE CSV FE wire·print layout P2** · G19 통합재가 P1 · US-L01 live · US-R03 P2 · v1.3 live E2E · **P3** K008~K014·G-HOMEPAGE·G9-SHORT/G9-DEMENTIA/G9-DR | ROADMAP v1.2.1·v2 우선순위 갱신 |

**coder 다음 액션 (126차)**: ① **tester merge(243+200=443)** ② **G30 live E2E verify** ③ G14·G34/G34b/G42 **live API E2E run** ④ **8-12 BE CSV FE wire·print layout P2** ⑤ **G42 익명함·전자결재 P2** ⑥ G24-plan-change(21815) P2 ⑦ G7 **실파일**(#27) ⑧ G2 **SMTP+FCMS 실연동** ⑨ **7-5 npay P2** ⑩ **21823 P2** ⑪ **G2b P2** ⑫ US-L01 **은행 8종 E2E live** ⑬ **US-R03 P2** ⑭ v1.3 live E2E.

---

### [BNK] BNK-172~175 인사이트 (2026-06-14) — ★ #44 P0 · 8-12 deepen · G42 follow-up · G-HOMEPAGE

> `BENCHMARK_REPORT.md` §172~175 · `COMPETITOR_MATRIX.md` §172~175 · ogada `@a7a6004`/`@39ee679` 실측.

| # | 항목 | 권장 조치 (planner 반영) |
|---|------|------------------------|
| **BNK-172** | **8-12 PDF 7종 FE 폐루프 ✅** @ `07956f5` — `STAFF_STATUS_REPORT_OUTPUTS`·referenceDate·print/CSV client-side · getting_started 직원앱 3분기 evidence | USER_STORIES US-R02 · ROADMAP v1.2.1 |
| **BNK-173** | **8-12 live E2E harness ✅** @ `ccc4d75` · **G30 V101 integrity** @ `f4c8558` · **G42 follow-up API** @ `2ebca70` · **FAQ21833 K012 재무회계 P3** · change_work 404→200 복구 | USER_STORIES US-R02/US-T14 · PLAN_NOTES K012 |
| **BNK-174** | **★★★ #44 56차 정본=NHIS 제34조 lawImg** — 830/2,630/**5,230**/**8,630** · ogada V68 drift P0 · **G42 follow-up UI 폐루프** @ `14124d6`/`bcb1d9f` | REQUIREMENTS G16/#44 · USER_STORIES US-T14 |
| **BNK-175** | **#44 P0 ✅** @ `39ee679` · **8-12 BE CSV export** @ `bc927f7` · **G42 duplicate approval UX** @ `892450a`/`a7a6004` · **QA-B72 Fixed** · **G-HOMEPAGE P3** — silverangel websiteProvided.do | REQUIREMENTS G-HOMEPAGE · API_SPEC §9-11 |

---

### [PLA] QA 피드백 반영 (2026-06-13, 125차 — BNK-168~171 · TSR 550~561 · G30 ✅ partial+ · 8-12 aggregated API ✅ partial+ · merge FULLY UNBLOCKED)

> **125차 자동 기획 동기화** — BNK-168~171(G9-COPAY-NAMING FE 폐루프·G9-COG NHIS import gate·G30 monitoring UI+API·8-12 aggregated API·referenceDate·exports·EZCare FAQ 14종 K008~K014·silverangel URL migration·#44 53차)·TSR 550~561. **QA Open 0건** · **Open→Planned 이동 없음**.

| 항목 | 125차 관측 | 조치 |
|------|----------|------|
| **baseline** | FE **`07956f5`** · WT **CLEAN** · HEAD **1048/1048 PASS** · BE **`5692662`** · WT **CLEAN** · **931/931 PASS**(TSR 558) · **236+194 ahead** · **67 route** · **V1–V100** | ROADMAP CURRENT BASELINE **125차** 갱신 |
| **BNK-168~171** | **★ G9-COPAY-NAMING ✅** @ `e77b7e4`/`a5c2736` · **★ G9-COG NHIS import gate ✅** @ `8bb6583` · **★ G30 ✅ partial+** @ `6f6915f`/`6a72b70`/`0da41c6`/`b8e92bf` · **★ 8-12 ✅ partial+** @ `bf6dd25`/`aaa16f8`/`07956f5` · **★ EZCare FAQ 14종·K008~K014 P3 cluster** · **★ silverangel URL migration DRIFT** · **★ #44 53차**(정본=longterm 502) | REQUIREMENTS §1-5·USER_STORIES US-R02/US-T15 · ROADMAP merge **430** UNBLOCKED |
| **QA** | Open **0건** · **QA-B71 Fixed** @ `b47e85c` · SEC-D22 **Planned** | QA_FEEDBACK 갱신 · 이동 없음 |
| **merge gate** | P0 `[x]` · BE+FE **ready** · ★ **FULLY UNBLOCKED** · 합계 **430 commits** | tester merge **430** 즉시 가능 |
| **잔여 P0/P1** | merge(430) · **G30 live E2E verify** · G14·G34/G34b/G42 **live API E2E run** · **8-12 PDF 7종 P2** · G19 통합재가 P1 · US-L01 live · US-R03 P2 · v1.3 live E2E · **P3** K008~K014·G9-SHORT/G9-DEMENTIA/G9-DR | ROADMAP v1.2.1·v2 우선순위 갱신 |

**coder 다음 액션 (125차)**: ① **tester merge(236+194=430)** ② **G30 live E2E verify** ③ G14·G34/G34b/G42 **live API E2E run** ④ **8-12 PDF 7종·엑셀 P2** ⑤ **G42 전자결재·익명함 P2** ⑥ G24-plan-change(21815) P2 ⑦ G7 **실파일**(#27) ⑧ G2 **SMTP+FCMS 실연동** ⑨ **7-5 npay P2** ⑩ **21823 P2** ⑪ **G2b P2** ⑫ US-L01 **은행 8종 E2E live** ⑬ **US-R03 P2** ⑭ v1.3 live E2E.

---

### [BNK] BNK-168~171 인사이트 (2026-06-13) — ★ G30 partial+ · 8-12 aggregated API · EZCare FAQ cluster · silverangel URL migration

> `BENCHMARK_REPORT.md` §168~171 · `COMPETITOR_MATRIX.md` §168~171 · ogada `@07956f5`/`@5692662` 실측.

| # | 항목 | 권장 조치 (planner 반영) |
|---|------|------------------------|
| **BNK-168** | **G9-COPAY-NAMING ✅ FE 폐루프** @ `e77b7e4`/`a5c2736` — longterm 503 4-tier 감경·func.php 7-x **9/10 Route** | REQUIREMENTS G9-COPAY-NAMING carry · ROADMAP v1.2.1 |
| **BNK-169** | **G9-COG NHIS import gate ✅** @ `8bb6583` · **EZCare FAQ 14 categories** — ogada **5/14 부재**(K008~K014) → **P3 cluster** · **G30 P1 monitoring UI** 착수 | REQUIREMENTS K008~K014 P3 · USER_STORIES US-T15 |
| **BNK-170** | **G30 FE+BE loop ✅ partial+** — FAQ21836/21841 5필드+유선상담 5명·V100 @ `6f6915f`/`6a72b70` · **silverangel `/system_feature/` 404→`/newSilverangel/` DRIFT** | USER_STORIES US-T15 · PLAN_NOTES silverangel URL |
| **BNK-171** | **8-12 aggregated API ✅ partial+** — `GET /api/v1/staff/reports/status`·`fetchStaffStatusReportApi`·referenceDate·exports @ `bf6dd25`/`07956f5` · **67 route** · **V1–V100** · **#44 53차** | USER_STORIES US-R02 · ROADMAP merge **430** |

---

### [PLA] QA 피드백 반영 (2026-06-13, 124차 — BNK-164~167 · TSR 538~549 · G9-COG ✅ · FAQ21824 checklist ✅ partial+ · merge FULLY UNBLOCKED)

> **124차 자동 기획 동기화** — BNK-164~167(7-1 guard UX·longterm 502/503 verbatim·G9-COG 폐루프·FAQ21824 checklist·FAQ21829·G9-COPAY-NAMING)·TSR 538~549. **QA Open 0건** · **Open→Planned 이동 없음**.

| 항목 | 124차 관측 | 조치 |
|------|----------|------|
| **baseline** | FE **`e77b7e4`** · WT **CLEAN** · HEAD **1020/1020 PASS** · BE **`edd2771`** · WT **CLEAN** · **897/897 PASS** · **230+188 ahead** · **66 route** · **V1–V99** | ROADMAP CURRENT BASELINE **124차** 갱신 |
| **BNK-164~167** | **★ G-7x-1 guard ✅ partial+** @ `338c014`/`21eb0af` · **★ G9-COG ✅ FE+BE** @ `6ef671b`/`edd2771`(30/30 cells·V99) · **★ FAQ21824 checklist ✅ partial+** @ `58256c6` · **★ G9-COPAY-NAMING ✅** @ `e77b7e4` · **★ longterm 502/503 verbatim** · **★ #44 49차**(정본=longterm 502) · **★ FAQ21829** · **★ P3 신규** G9-SHORT/G9-DEMENTIA/G9-DR | REQUIREMENTS §1-5·USER_STORIES US-G00a/US-D03 · ROADMAP merge **418** UNBLOCKED |
| **QA** | Open **0건** · SEC-D22 **Planned** | QA_FEEDBACK 갱신 · 이동 없음 |
| **merge gate** | P0 `[x]` · BE+FE **ready** · ★ **FULLY UNBLOCKED** · 합계 **418 commits** | tester merge **418** 즉시 가능 |
| **잔여 P0/P1** | merge(418) · G30/G14/G34/G34b/G42 **live E2E** · **FAQ21824 live E2E** · **G-7x-1 guard live E2E** · 8-12 PDF 7종 P2 · G42·21823·7-5·G2b P2 · G19 통합재가 P1 · US-L01 live · US-R03 P2 · v1.3 live E2E · **P3** G9-SHORT/G9-DEMENTIA/G9-DR | ROADMAP v1.2.1·v2 우선순위 갱신 |

**coder 다음 액션 (124차)**: ① **tester merge(230+188=418)** ② G30/G14/G34/G34b/G42 **live API E2E run** ③ **FAQ21824·G-7x-1 guard live E2E** ④ **G9-COG NHIS import live E2E** ⑤ **8-12 PDF 7종·엑셀 P2** ⑥ **G42 전자결재·익명함 P2** ⑦ G24-plan-change(21815) P2 ⑧ G7 **실파일**(#27) ⑨ G2 **SMTP+FCMS 실연동** ⑩ **7-5 npay P2** ⑪ **21823 P2** ⑫ **G2b P2** ⑬ US-L01 **은행 8종 E2E live** ⑭ **US-R03 P2** ⑮ v1.3 live E2E.

---

### [BNK] BNK-164~167 인사이트 (2026-06-13) — ★ G9-COG 폐루프 · longterm 502/503 · FAQ21824 checklist · FAQ21829

> `BENCHMARK_REPORT.md` §164~167 · `COMPETITOR_MATRIX.md` §164~167 · ogada `@e77b7e4`/`@edd2771` 실측.

| # | 항목 | 권장 조치 (planner 반영) |
|---|------|------------------------|
| **BNK-164** | **7-1 선행입금 UX ✅ partial+** @ `338c014` — `ClaimGenerationGuardBanner` 7-2→7-1 workflow · demo `search_menu.js`·L07 pamcode 10/11 | USER_STORIES US-M03-b ✅ partial+ · ROADMAP v1.2.1 |
| **BNK-165** | **FAQ21824 필드→Route 4단 매핑**·**21298 이중일정 zero drift**·**change_work 404**·FAQ21827 | PLAN_NOTES FAQ21824 carry · G21 live E2E P1 |
| **BNK-166** | **★ longterm 502/503 verbatim 전수** — 월한도 6/6·주야간 25/30→**30/30** · **503 4-tier 감경** · **#44 정본=longterm 502** 재확정 | REQUIREMENTS §1-5 124차 · **P3** G9-SHORT/G9-DEMENTIA/G9-DR/G9-COPAY-NAMING |
| **BNK-167** | **★ G9-COG P2→✅ FE+BE** @ `6ef671b`/`edd2771` · **★ FAQ21824 checklist ✅ partial+** @ `58256c6` · **★ FAQ21829** 연초 CS·Top5 | USER_STORIES US-G00a·US-D03 · ROADMAP merge **418** |

---

### [PLA] QA 피드백 반영 (2026-06-13, 123차 — BNK-160~163 · TSR 526~537 · G42 ✅ partial · G34b ✅ partial+ · merge FULLY UNBLOCKED)

> **123차 자동 기획 동기화** — BNK-160~163(PDF 7-x·G34b clone·G42 폐루프·FAQ21824·#44 47차·8-12 status report·G34b import-draft)·TSR 526~537. **QA Open 0건** · **Open→Planned 이동 없음** · **QA-B68 Fixed**.

| 항목 | 123차 관측 | 조치 |
|------|----------|------|
| **baseline** | FE **`02cbd05`** · WT **CLEAN** · HEAD **1001/1001 PASS** · BE **`8487667`** · WT **CLEAN** · **882/882 PASS** · **224+184 ahead** · **65 route** | ROADMAP CURRENT BASELINE **123차** 갱신 |
| **BNK-160~163** | **★ G42 ✅ partial** @ `b0a9e06`/`bcdc411`/`0460e9b` · **★ G34b ✅ partial+** @ `1b5fabe`/`994f5ea`/`8487667` · **★ 8-12 △ partial** @ `02cbd05` · **★ FAQ21824 zero drift** · **★ #44 47차**(byl18≠러-1~4) · **★ 7-1 선행입금 P1** · **★ QA-B68 Fixed** | REQUIREMENTS G42/G34b/8-12/FAQ21824 · USER_STORIES US-T13/T14/US-R02 · ROADMAP merge **408** UNBLOCKED |
| **QA** | Open **0건** · **QA-B68 Fixed** @ `db21e85` · **SEC-D22 Planned** | QA_FEEDBACK 갱신 · 이동 없음 |
| **merge gate** | P0 `[x]` · BE+FE **ready** · ★ **FULLY UNBLOCKED** · 합계 **408 commits** | tester merge **408** 즉시 가능 |
| **잔여 P0/P1** | merge(408) · G30/G14/G34/G34b/G42 **live E2E** · **8-12 PDF 7종 P2** · **G42 전자결재·익명함 P2** · **7-1 선행입금 UX P1** · G24-plan-change P2 · G7 실파일 · G2 SMTP+FCMS · 7-5·21823·G2b P2 · US-L01 live · US-R03 P2 · v1.3 live E2E | ROADMAP v1.2.1·v2 우선순위 갱신 |

**coder 다음 액션 (123차)**: ① **tester merge(224+184=408)** ② G30/G14/G34/G34b/G42 **live API E2E run** ③ **8-12 PDF 7종·엑셀 P2** ④ **G42 전자결재·익명함 P2** ⑤ **7-1 선행입금 가드 UX P1** ⑥ G24-plan-change(21815) P2 ⑦ G7 **실파일**(#27) ⑧ G2 **SMTP+FCMS 실연동** ⑨ **7-5 npay P2** ⑩ **21823 P2** ⑪ **G2b P2** ⑫ US-L01 **은행 8종 E2E live** ⑬ **US-R03 P2** ⑭ v1.3 live E2E.

---

### [BNK] BNK-160~163 인사이트 (2026-06-13) — ★ G42 partial · G34b deepen · 8-12 · FAQ21824

> `BENCHMARK_REPORT.md` §160~163 · `COMPETITOR_MATRIX.md` §160~163 · ogada `@02cbd05`/`@8487667` 실측.

| # | 항목 | 권장 조치 (planner 반영) |
|---|------|------------------------|
| **BNK-160** | **G34b 전월 clone** @ `1b5fabe` · **G21 assigned caregiver guard** @ `b459f4c` · **PDF p.87–92 7-x**·**7-1 선행입금 P1** | USER_STORIES US-T13 ✅ partial+ · REQUIREMENTS G-7x-1-guard |
| **BNK-161** | **G42 benchmark→coder 폐루프 ✅ partial** @ `b0a9e06`/`0460e9b` · **FAQ21824 lifecycle** md5 `03038ccb` zero drift | USER_STORIES **US-T14** ✅ partial · REQUIREMENTS FAQ21824 v2 Epic |
| **BNK-162** | **#44 47차 방법론** — byl18=방문요양 원거리교통비 별표뿐·러-1~4 **수가표 별표 직접 출처 필요** · G34b role guard | PLAN_NOTES #44 carry · 하드코딩 금지 재확정 |
| **BNK-163** | **8-12 ❌→△ partial** @ `02cbd05` · **G34b import-draft API** @ `8487667` · FAQ21824 재실측 | USER_STORIES **US-R02** 8-12 partial · ROADMAP v1.2.1 |

---

### [PLA] QA 피드백 반영 (2026-06-13, 122차 — BNK-155~159 · TSR 514~525 · G40b ✅ full · G34b ✅ partial · merge FULLY UNBLOCKED)

> **122차 자동 기획 동기화** — BNK-155~159(G40b 폐루프·G34b import·FAQ21812~16·21823·G42·longterm live·LCMS 404 cluster·G21 guard test)·TSR 514~525. **QA Open 0건** · **Open→Planned 이동 없음** · **QA-B65/B66/B67 Fixed**.

| 항목 | 122차 관측 | 조치 |
|------|----------|------|
| **baseline** | FE **`3c7d2c7`** · WT **CLEAN** · HEAD **965/965 PASS** · BE **`2925ff7`** · WT **CLEAN** · **852/852 PASS** · **217+178 ahead** · **64 route** | ROADMAP CURRENT BASELINE **122차** 갱신 |
| **BNK-155~159** | **★ G40b ✅ full** @ `7b68f54`/`6657d90`/`a7b4a39` · **★ G34b ✅ partial** @ `0ce04ad`/`d41546f` · **★ US-R02 HR link** @ `d41546f` · **★ G21 assigned-user+day-care test** @ `dc48933`/`2925ff7` · **★ FAQ21812~14·21816·21823** · **★ G42 P2** · **★ longterm live·#44 46차** · **★ QA-B65/B66/B67 Fixed** | REQUIREMENTS G40b/G34b/G42 · USER_STORIES US-T12/T13/T14 · ROADMAP merge **395** UNBLOCKED |
| **QA** | Open **0건** · **QA-B65/B66/B67 Fixed** @ `dc48933`/`2925ff7`/`3c7d2c7` · **SEC-D22 Planned** | QA_FEEDBACK 갱신 · 이동 없음 |
| **merge gate** | P0 `[x]` · BE+FE **ready** · ★ **FULLY UNBLOCKED** · 합계 **395 commits** | tester merge **395** 즉시 가능 |
| **잔여 P0/P1** | merge(395) · G30/G14/G34 **live E2E** · G40/G40b **live E2E** · G17/G32/G33/G37/G38/G39 live E2E · G7 실파일 · G2 SMTP+FCMS · **G42·21823·7-5·G2b P2** · US-L01 live · US-R03 P2 · 8-7/8-12 P2 · v1.3 live E2E | ROADMAP v1.2.1·v2 우선순위 갱신 |

**coder 다음 액션 (122차)**: ① **tester merge(217+178=395)** ② G30/G14/G34 **live API E2E run** ③ G40/G40b **live API E2E run** ④ G17/G32/G33/G37/G38/G39 **live E2E run** ⑤ G7 **실파일**(#27) ⑥ G2 **SMTP+FCMS 실연동** ⑦ **G42 P2**(FAQ21814) ⑧ **21823 P2**(근로재계약) ⑨ **G34b P2**(월별 clone) ⑩ **7-5 npay P2** ⑪ **G2b P2** ⑫ US-L01 **은행 8종 E2E live** ⑬ **US-R03 P2** ⑭ **8-7/8-12 P2** ⑮ v1.3 live E2E.

---

### [BNK] BNK-155~159 인사이트 (2026-06-13) — ★ G40b full · G34b · G42 · FAQ21816

> `BENCHMARK_REPORT.md` §155~159 · `COMPETITOR_MATRIX.md` §155~159 · ogada `@3c7d2c7`/`@2925ff7` 실측.

| # | 항목 | 권장 조치 (planner 반영) |
|---|------|------------------------|
| **BNK-155~156** | **G40b 3-cycle 폐루프 완전 닫힘** — Panel→Status Route→V96 integrity @ `7b68f54`/`6657d90`/`a7b4a39` | USER_STORIES US-T12 ✅ full · ROADMAP v1.2.1 |
| **BNK-157~158** | **G34b needs-assessment import ✅ partial** @ `0ce04ad` · **FAQ21812~14·21823 정본** | USER_STORIES **US-T13** · **US-T14** · REQUIREMENTS G34b/G42 |
| **BNK-158** | **US-R02 health checkup→HR hub link** @ `d41546f` · **longterm.or.kr live 복구** · **#44 46차** | REQUIREMENTS G-Health-8-10 partial+ · PLAN_NOTES #44 carry |
| **BNK-159** | **QA-B67 API error normalize** @ `3c7d2c7` · **G21 day-care guard test** @ `2925ff7` · **FAQ21816 급여제공기록지** | ROADMAP G21 scope 분리 유지 · G39 dispatch FE P2 |

---

### [PLA] QA 피드백 반영 (2026-06-13, 121차 — BNK-152~154 · TSR 502~513 · G40 ✅ partial+ · G40b △ partial · merge FULLY UNBLOCKED)

> **121차 자동 기획 동기화** — BNK-152~154(demo-work pamcode·FAQ21811 G40b·G40 폐루프·효성CMS 3-method·LCMS regStep 404·#44 43차)·TSR 502~513. **QA Open 0건** · **Open→Planned 이동 없음** · **QA-B62/B63/B64 Fixed**.

| 항목 | 121차 관측 | 조치 |
|------|----------|------|
| **baseline** | FE **`22325f4`** · WT **CLEAN** · HEAD **946/946 PASS** · BE **`bdfc140`** · WT **CLEAN** · **844/844 PASS** · **211+175 ahead** · **63 route** | ROADMAP CURRENT BASELINE **121차** 갱신 |
| **BNK-152~154** | **★ G40 FE+BE+V93/V94 폐루프 닫힘** @ `72676a5`/`686d686`/`e89175e` · **★ G40b 반기 기초평가 △ partial** @ `84e59d2`/`22325f4`/`bdfc140` · **★ FAQ21811 지표16** · **★ G2b P2**(가상계좌·카드·다계좌) · **★ LCMS regStep.do 404** · **★ #44 43차 0건** | REQUIREMENTS G40/G40b/G2b · USER_STORIES US-T11/US-T12 · API_SPEC §9-8/§9-9 · ROADMAP merge **386** UNBLOCKED |
| **QA** | Open **0건** · **QA-B62/B63/B64 Fixed** @ `e89175e`/`f0752b6`/`2589b94` · **SEC-D22 Planned** | QA_FEEDBACK 갱신 · 이동 없음 |
| **merge gate** | P0 `[x]` · BE+FE **ready** · ★ **FULLY UNBLOCKED** · 합계 **386 commits** | tester merge **386** 즉시 가능 |
| **잔여 P0/P1** | merge(386) · G40/G40b live E2E · G34/G24/G14/G30 live E2E · G17/G32/G33/G37/G38/G39 live E2E · G7 실파일 · G2 SMTP+FCMS · **G2b P2** · US-L01 live · US-R03 P2 · 8-7/8-12 P2 · 7-5 npay P2 · G30 Epic · v1.3 live E2E | ROADMAP v1.2.1·v2 우선순위 갱신 |

**coder 다음 액션 (121차)**: ① **tester merge(211+175=386)** ② G40/G40b **live API E2E run** ③ G34/G24/G14/G30 **live E2E run** ④ G17/G32/G33/G37/G38/G39 **live E2E run** ⑤ G7 **실파일**(#27) ⑥ G2 **SMTP+FCMS 실연동** ⑦ **G2b P2**(가상계좌·카드·다계좌) ⑧ US-L01 **은행 8종 E2E live** ⑨ **US-R03 P2** ⑩ **8-7/8-12 P2** ⑪ **7-5 npay P2** ⑫ **G30 Epic** ⑬ v1.3 live E2E.

---

### [BNK] BNK-152~154 인사이트 (2026-06-13) — ★ G40 폐루프 · G40b · G2b · LCMS 404

> `BENCHMARK_REPORT.md` §152~154 · `COMPETITOR_MATRIX.md` §152~154 · ogada `@22325f4`/`@bdfc140` 실측.

| # | 항목 | 권장 조치 (planner 반영) |
|---|------|------------------------|
| **BNK-152~153** | **G40 benchmark→coder 3중 폐루프 닫힘** — FE WIP→V94→dashboard widget @ `2f5af63`/`f0752b6`/`72676a5` | USER_STORIES US-T11 ✅ partial+ · ROADMAP v1.2.1 |
| **BNK-153** | **FAQ21811 지표16 반기 기초평가** — G40(급여개시 전 1회) vs G40b(반기 1회) **주기 분리** | USER_STORIES **US-T12** · REQUIREMENTS G40b · API_SPEC §9-9 |
| **BNK-154** | **효성CMS 3-method** — 가상계좌·카드·다계좌 정산 · ogada G2=CMS 자동이체만 | REQUIREMENTS **G2b P2** · ROADMAP v2 |
| **BNK-154** | **LCMS regStep.do live 404** — 정원 과금 온보딩 UI 역공학 불가 · snapshot carry | PLAN_NOTES 추가 질문 · #44 43차 placeholder 유지 |

---

### [PLA] QA 피드백 반영 (2026-06-13, 120차 — BNK-145~151 · TSR 497~501 · G40 BE partial · FAQ21806 V92 · merge BLOCK)

> **120차 자동 기획 동기화** — BNK-145~151(FAQ21838 모니터링·FAQ21806 V92 onboarding·G40 V93 BE·silverangel 9-step·EZCare 일정확정·demo-work npay·8-12 P2)·TSR 497~501. **QA Open 0건** · **QA-B62 Open→Planned** · **SEC-D22 Planned** 유지.

| 항목 | 120차 관측 | 조치 |
|------|----------|------|
| **baseline** | FE **`4efa168`** · WT **DIRTY 2M** · HEAD **917/917 PASS** · WT **921/921 PASS** · BE **`686d686`** · WT **CLEAN** · **205+171 ahead** · **63 route** | ROADMAP CURRENT BASELINE **120차** 갱신 |
| **BNK-145~151** | **★ FAQ21806 V92 onboarding FE+BE deepen** @ `e76ca06`/`d4ee057`/`9ebb87f`/`4efa168` · **★ G40 BE ✅ partial** @ `22d736b`/`686d686` · **★ silverangel 9-step admission** · **★ EZCare 일정확정 4단** · **★ demo-work 7-5 npay·8-12 P2** · **★ #44 40차 0건** · **★ QA-B62 Planned** | REQUIREMENTS G40 · USER_STORIES US-T11 · API_SPEC §9-8 · ROADMAP v1.2.1 merge BLOCK |
| **QA** | Open **0건** · **QA-B62 Planned**(FE WT dirty) · **SEC-D22 Planned** | QA_FEEDBACK Open→Planned · ROADMAP QA-B62 완료 기준 |
| **merge gate** | P0 `[x]` · BE **ready** · FE **pending** · ⚠ **BLOCK** · 합계 **376 commits** | COD FE 2M clean→tester merge **376** |
| **잔여 P0/P1** | FE WT clean(2M) · merge(376) · **G40 FE Panel** · G34/G24/G14/G30 live E2E · G17/G32/G33/G37/G38/G39 live E2E · G7 실파일 · G2 SMTP+FCMS · US-L01 live · US-R03 P2 · 8-7/8-12 P2 · 7-5 npay P2 · G30 Epic · v1.3 live E2E | ROADMAP v1.2.1·v2 우선순위 갱신 |

**coder 다음 액션 (120차)**: ① **FE `http.js`·`http.test.js` 커밋/revert→WT clean**(QA-B62) ② **tester merge(205+171=376)** ③ **G40 FE Panel**(ClientDetail 위험도평가 3종) ④ G34/G24/G14/G30 **live API E2E run** ⑤ G17/G32/G33/G37/G38/G39 **live E2E run** ⑥ G7 **실파일**(#27) ⑦ G2 **SMTP+FCMS 실연동** ⑧ US-L01 **은행 8종 E2E live** ⑨ **US-R03 P2** ⑩ **8-7/8-12 P2** ⑪ **7-5 npay P2** ⑫ **G30 Epic** ⑬ v1.3 live E2E.

---

### [BNK] BNK-145~151 인사이트 (2026-06-13) — ★ G40 BE · FAQ21806 V92 · 8-12 P2 · merge 376 BLOCK

> `BENCHMARK_REPORT.md` §145~151 · `COMPETITOR_MATRIX.md` §145~151 · ogada `@4efa168`/`@686d686` 실측.

| # | 항목 | 권장 조치 (planner 반영) |
|---|------|------------------------|
| **BNK-145~146** | **FAQ21806 onboarding V92 폐루프** — StaffPage summary+BE compliance API @ `e76ca06`/`d4ee057` · **demo-work 7-5 npay** · **PDF 8-10≠func 8-10** → **8-12 Epic** | USER_STORIES US-R03 · REQUIREMENTS G-Staff-LC · ROADMAP 8-12 P2 |
| **BNK-149** | **EZCare 일정확정 4단** — 계획→청구→RFID→확정·확정 전 본인부담 대조 | REQUIREMENTS G21/G2 · USER_STORIES US-V04 · live E2E P1 |
| **BNK-150~151** | **G40 신규입소 위험도평가** — silverangel 지표21 3종 · BE V93 ✅ partial · **FE 0건 P2** | USER_STORIES **US-T11** · API_SPEC §9-8 · ROADMAP G40 FE |
| **BNK-146** | **8-12 직원현황 리포트** — PDF 7종 출력 ≠ func 8-10 건강검진 | USER_STORIES US-R02 · Route `/staff/reports/status` P2 |

---

### [PLA] QA 피드백 반영 (2026-06-13, 119차 — BNK-141~144 · TSR 476~488 · US-R03 HR hub · G2 CMS cancel · merge FULLY UNBLOCKED)

> **119차 자동 기획 동기화** — BNK-141~144(V90 integrity·US-R03 HR file hub V91·FAQ21828 운영규정 교육·G2 CMS 해지 API+UI·law.go.kr #44 38차·LCMS 해지 workflow)·TSR 476~488. **QA Open 0건** · **QA-B60 Fixed** · **Open→Planned 이동 없음**(이미 0 Open).

| 항목 | 119차 관측 | 조치 |
|------|----------|------|
| **baseline** | FE **`9a6fdb6`** · WT **CLEAN** · HEAD **900/900 PASS** · BE **`4a622ab`** · WT **CLEAN** · **805/805 PASS**(TSR 485 기준) · **201+166 ahead** · **63 route** | ROADMAP CURRENT BASELINE **119차** 갱신 |
| **BNK-141~144** | **★ V90 integrity** @ `a206508` · **★ US-R03 HR file hub ✅ partial** @ `bbb8e35`/`bc3c967`/`57ed2db` · **★ G2 CMS 등록+해지 ✅ partial** @ `72aff00`/`a34d0eb`/`4a622ab`/`9a6fdb6` · **★ FAQ21828 운영규정 교육 P2** · **★ FAQ21807 이중 정본** · **★ #44 38차 0건** · **★ QA-B60 Fixed** | REQUIREMENTS G-Staff-LC·G2 · USER_STORIES US-R03·US-L03 · API_SPEC §9-7 |
| **QA** | Open **0건** · **QA-B60 Fixed** @ `57ed2db` · **SEC-D22 Planned** | QA_FEEDBACK 갱신 · 이동 없음 |
| **merge gate** | P0 `[x]` · BE+FE **ready** · ★ **FULLY UNBLOCKED** · 합계 **367 commits** | tester merge **367** 즉시 가능 |
| **잔여 P0/P1** | merge(367) · G2 CMS/US-R03/8-7-1/US-R02/G34 **live E2E run** · G17/G32/G33/G37/G38/G39 live E2E · G7 실파일 · G2 **SMTP+FCMS 실연동** · US-L01 live · **US-R03 P2**(FAQ21806 6단계 workflow) · **8-7 P2**(FAQ21807+21828 교육일지) · **8-10 P2**(건강검진 파일함 deepen) · **7-5/다중결제 P2** · **G30 Epic** · v1.3 live E2E | ROADMAP v1.2.1·v2 우선순위 갱신 |

**coder 다음 액션 (119차)**: ① **tester merge(201+166=367)** ② G2 CMS/US-R03/8-7-1/US-R02/G34 **live API E2E run** ③ G17/G32/G33/G37/G38/G39 **live E2E run** ④ G7 **실파일**(#27) ⑤ G2 **SMTP+FCMS 실연동** ⑥ US-L01 **은행 8종 E2E live** ⑦ **US-R03 P2**(FAQ21806 입사 6단계 workflow) ⑧ **8-7 P2**(FAQ21807+21828 교육일지) ⑨ **8-10 P2**(건강검진 파일함 deepen) ⑩ **7-5/다중결제 P2** ⑪ **G30 Epic** ⑫ v1.3 live E2E.

---

### [BNK] BNK-141~144 인사이트 (2026-06-13) — ★ HR file hub · G2 CMS cancel · FAQ21828 · merge 367 FULLY UNBLOCKED

> `BENCHMARK_REPORT.md` §141~144 · `COMPETITOR_MATRIX.md` §141~144 · ogada `@9a6fdb6`/`@4a622ab` 실측.

| # | 항목 | 권장 조치 (planner 반영) |
|---|------|------------------------|
| **BNK-141** | **V90 integrity** — US-S02/US-R02 HR constraints @ `a206508` · attachment UX @ `b599d8f` | API_SPEC §9-5/§9-6 · ROADMAP v1.2.1 |
| **BNK-142** | **US-R03 HR file hub ✅ partial** — `StaffHrFileController`+V91+`StaffHrFilePanel` @ `bbb8e35`/`bc3c967` · getting_started.php Wayback **302→200 복구** | USER_STORIES US-R03 · API_SPEC §9-7 |
| **BNK-143** | **FAQ21828 운영규정 교육** — 지표5·연1+신규7일·필수4필드 ↔ FAQ21807(지표14·반기) **이중 정본** | USER_STORIES US-S02·US-R02 P2 · PLAN_NOTES 추가 질문 |
| **BNK-144** | **G2 CMS 해지 ✅ partial** — duplicate guard·cancellation API·cancelled history·FE modal @ `72aff00`/`a34d0eb`/`4a622ab`/`9a6fdb6` · **LCMS 해지 workflow** · **#44 38차 0건** | USER_STORIES US-L03 · REQUIREMENTS G2 |

---

### [PLA] QA 피드백 반영 (2026-06-13, 118차 — BNK-137~140 · TSR 464~475 · 8-7-1 ✅ · 8-10 partial · merge FULLY UNBLOCKED)

> **118차 자동 기획 동기화** — BNK-137~140(8-7-1 cert API+UI·8-10 health checkup V89·FAQ21806 onboarding·FAQ21822 P3·PDF 8-10 충돌·G21 xls deepen)·TSR 464~475. **QA Open 0건** · **QA-B57/B58/B59 Fixed** · **Open→Planned 이동 없음**(이미 0 Open).

| 항목 | 118차 관측 | 조치 |
|------|----------|------|
| **baseline** | FE **`50bdb6e`** · WT **CLEAN** · HEAD **883/883 PASS** · BE **`1817c36`** · WT **CLEAN** · **786/786 PASS** · **196+160 ahead** · **63 route** | ROADMAP CURRENT BASELINE **118차** 갱신 |
| **BNK-137~140** | **★ 8-7-1 partial+→✅** @ `51477bd`/`0a7fe16`/`46f1ac0`/`50bdb6e` · **★ 8-10 ❌ P2→✅ partial** @ `f1268c6`/`604787f`/`bad88f5` · **★ FAQ21806 US-R03 onboarding P2** · **★ FAQ21822 직원회의 P3** · **★ PDF↔func.php 8-10 충돌** · **★ G21 legacy/uppercase xls** @ `3f444a1`/`1817c36` · **★ QA-B57/B58/B59 Fixed** | REQUIREMENTS G34·G-Health-8-10 · USER_STORIES US-S02·US-R02 · ROADMAP v1.2.1 |
| **QA** | Open **0건** · **QA-B57/B58/B59 Fixed** · **SEC-D22 Planned** | QA_FEEDBACK 갱신 · 이동 없음 |
| **merge gate** | P0 `[x]` · BE+FE **ready** · ★ **FULLY UNBLOCKED** · 합계 **356 commits** | tester merge **356** 즉시 가능 |
| **잔여 P0/P1** | merge(356) · G34/US-R02/US-R03/G24/G14 **live E2E run** · G17/G32/G33/G37/G38/G39 live E2E · G7 실파일 · G2 SMTP · US-L01 live · **US-R03 P2**(FAQ21806) · **8-10 P2**(파일함) · **8-7 P2**(교육일지) · **7-5/다중결제 P2** · **G30 Epic** · v1.3 live E2E | ROADMAP v1.2.1·v2 우선순위 갱신 |

**coder 다음 액션 (118차)**: ① **tester merge(196+160=356)** ② G34/US-R02/US-R03/G24/G14 **live API E2E run** ③ G17/G32/G33/G37/G38/G39 **live E2E run** ④ G7 **실파일**(#27) ⑤ G2 **SMTP** ⑥ US-L01 **은행 8종 E2E live** ⑦ **US-R03 P2**(FAQ21806 입사서류) ⑧ **8-10 P2**(직원 파일함) ⑨ **8-7 P2**(교육일지·리포트) ⑩ **7-5/다중결제 P2** ⑪ **G30 Epic** ⑫ v1.3 live E2E.

---

### [BNK] BNK-137~140 인사이트 (2026-06-13) — ★ 8-7-1 ✅ · 8-10 partial · FAQ21806 · merge 356 FULLY UNBLOCKED

> `BENCHMARK_REPORT.md` §137~142 · `COMPETITOR_MATRIX.md` §137~142 · `memory/decisions.md` BNK-137~140 참조. ogada `@50bdb6e`/`@1817c36` 실측.

| # | 항목 | 권장 조치 (planner 반영) |
|---|------|------------------------|
| **BNK-137** | **8-7-1 BE cert API V88** @ `51477bd` · FE upload UI **P2→✅** @ `0a7fe16` | USER_STORIES US-S02 · API_SPEC §9-5 |
| **BNK-138** | **8-10 ✅ partial** — V89+`StaffHealthCheckupsPage` · **PDF↔func.php 8-10 충돌** | REQUIREMENTS G-Health-8-10 · USER_STORIES US-R02 · API_SPEC §9-6 |
| **BNK-139** | **FAQ21806 입사 6단계** — onboarding + V89 건강검진 **이중 1:1** | USER_STORIES US-R03 P2 |
| **BNK-140** | **G21 uppercase `.XLS`** · **func.php 36차 zero drift** · **QA-B57/B58/B59 Fixed** | ROADMAP merge **356 FULLY UNBLOCKED** |

---

### [PLA] QA 피드백 반영 (2026-06-13, 117차 — BNK-132~136 · TSR 453~463 · 8-7-1 partial · merge FULLY UNBLOCKED)

> **117차 자동 기획 동기화** — BNK-132~136(US-R03 V87+badge·8-7-1 △→✅ partial·G34 e-sign·FAQ21799·FAQ21801·longterm live 복구·MOHW247 #44 32차)·TSR 453~463. **QA Open 0건** · **QA-B56 Fixed** · **Open→Planned 이동 없음**(이미 0 Open).

| 항목 | 117차 관측 | 조치 |
|------|----------|------|
| **baseline** | FE **`a11bbeb`** · WT **CLEAN** · HEAD **866/866 PASS** · BE **`9c9fd5b`** · WT **CLEAN** · **755/755 PASS** · **191+155 ahead** · **62 route** | ROADMAP CURRENT BASELINE **117차** 갱신 |
| **BNK-132~136** | **★ US-R03 V87+badge+validation+date normalize** @ `61336df`/`b3e59e2`/`37dc785`/`bb4c1af` · **★ 8-7-1 ✅ partial** @ `314b380`/`9c9fd5b`/`a11bbeb` · **★ G34 e-sign ✅** · **★ longterm.or.kr live 복구** · **★ FAQ21799 건강검진 P2** · **★ FAQ21801 G39 반기 nuance** · **★ MOHW247 #44 32차** · **★ QA-B56 Fixed** @ `18e2b4c` | REQUIREMENTS G34·G-Staff-LC·G-Health-8-10 · USER_STORIES US-R03·US-S02 · ROADMAP v1.2.1 |
| **QA** | Open **0건** · **QA-B56 Fixed** · **SEC-D22 Planned** | QA_FEEDBACK 갱신 · 이동 없음 |
| **merge gate** | P0 `[x]` · BE+FE **ready** · ★ **FULLY UNBLOCKED** · 합계 **346 commits** | tester merge **346** 즉시 가능 |
| **잔여 P0/P1** | merge(346) · G34/US-R03/G24/G14 **live E2E run** · G17/G32/G33/G37/G38/G39 live E2E · G7 실파일 · G2 SMTP · US-L01 live · **US-R03 P2** · **8-7-1 P2**(이수증) · **건강검진 8-10 P2** · **7-5/다중결제 P2** · **G30 Epic** · v1.3 live E2E | ROADMAP v1.2.1·v2 우선순위 갱신 |

**coder 다음 액션 (117차)**: ① **tester merge(191+155=346)** ② G34/US-R03/G24/G14 **live API E2E run** ③ G17/G32/G33/G37/G38/G39 **live E2E run** ④ G7 **실파일**(#27) ⑤ G2 **SMTP** ⑥ US-L01 **은행 8종 E2E live** ⑦ **US-R03 P2**(직원 파일함·근로계약서·4대보험) ⑧ **8-7-1 P2**(이수증 첨부) ⑨ **건강검진 8-10 P2** ⑩ **7-5/다중결제 P2** ⑪ **G30 Epic** ⑫ v1.3 live E2E.

---

### [BNK] BNK-132~136 인사이트 (2026-06-13) — ★ US-R03 deepen · 8-7-1 partial · longterm 복구 · MOHW247

> `BENCHMARK_REPORT.md` §134~138 · `COMPETITOR_MATRIX.md` §134~138 · `memory/decisions.md` BNK-132~136 참조. ogada `@a11bbeb`/`@9c9fd5b` 실측.

| # | 항목 | 권장 조치 (planner 반영) |
|---|------|------------------------|
| **BNK-132~133** | **US-R03 운영 하드닝 deepen** — 5xx guard·G21 paired link·V87·StatusBadge·longterm live 복구 | USER_STORIES US-R03 `[x]` deepen · ROADMAP v1.2.1 |
| **BNK-134** | **FAQ21801 G39 반기1회 nuance** — silverangel 지표44(연1) vs 이지케어 지표24(반기) | REQUIREMENTS G39 · PLAN_NOTES 추가 질문 |
| **BNK-135** | **FAQ21799 건강검진 8-10 P2 Epic** · **8-7-1 ❌→△ UI** · **G34 sign modal** · **QA-B56** BE WT dirty | REQUIREMENTS G-Health-8-10 · USER_STORIES US-S02 · ROADMAP QA-B56 |
| **BNK-136** | **8-7-1 △→✅ partial** — BE compliance API+live harness · **MOHW247 #44 32차** · **regStep.do 404 DRIFT** | API_SPEC §9-5 · USER_STORIES US-S02 partial `[x]` |

---

### [PLA] QA 피드백 반영 (2026-06-13, 116차 — BNK-128~131 · TSR 452 · US-R03 core · merge FULLY UNBLOCKED)

> **116차 자동 기획 동기화** — BNK-128~131(US-R03 BE+FE+V86 wired·Staff lifecycle pilot E2E deepen·longterm.or.kr live drift·LCMS 평가 SLA·CMS 3-method)·TSR 452. **QA Open 0건** · **QA-B54/B55 Fixed** · **Open→Planned 이동 없음**(이미 0 Open).

| 항목 | 116차 관측 | 조치 |
|------|----------|------|
| **baseline** | FE **`a018e71`** · WT **CLEAN** · HEAD **844/844 PASS** · BE **`82bdbcd`** · WT **CLEAN** · **741/741 PASS** · **185+150 ahead** · **61 route** | ROADMAP CURRENT BASELINE **116차** 갱신 |
| **BNK-128~131** | **★ US-R03 core wired** @ `75440bc`/`7243d21`/`9441a3c`/`a018e71` · **★ QA-B54/B55 Fixed** · **★ G34 signature audit ✅** @ `8ccd287` · **★ G21 paired link draft sync ✅** @ `82bdbcd` · **★ longterm.or.kr live 수가 셸 드리프트** · **★ #44 29차 0건(로컬)** · **★ LCMS 평가 SLA P3** · **★ CMS 3-method P2** | REQUIREMENTS G-Staff-LC · USER_STORIES US-R03 partial · ROADMAP v1.2.1 |
| **QA** | Open **0건** · **QA-B54/B55 Fixed** · **SEC-D22 Planned** | QA_FEEDBACK 갱신 · 이동 없음 |
| **merge gate** | P0 `[x]` · BE+FE **ready** · ★ **FULLY UNBLOCKED** · 합계 **335 commits** | tester merge **335** 즉시 가능 |
| **잔여 P0/P1** | merge(335) · G24/G14/G34/US-R03 **live E2E run** · G34 **e-sign·보수교육** · G17/G32/G33/G37/G38/G39 live E2E · G7 실파일 · G2 SMTP · US-L01 live · **US-R03 P2**(문서·서식·4대보험) · **7-5/다중결제 P2** · **8-7-1 보수교육 P2** · G30 Epic · v1.3 live E2E | ROADMAP v1.2.1·v2 우선순위 갱신 |

**coder 다음 액션 (116차)**: ① **tester merge(185+150=335)** ② G24/G14/G34/US-R03 **live API E2E run** ③ G34 **전자서명·8-7-1 보수교육 workflow** ④ G17/G32/G33/G37/G38/G39 **live API E2E run** ⑤ G7 **실파일**(#27) ⑥ G2 **SMTP** ⑦ US-L01 **은행 8종 E2E live** ⑧ **US-R03 P2**(직원 파일함·근로계약서·4대보험) ⑨ **7-5/다중결제 P2** ⑩ **8-7-1 보수교육 P2** ⑪ **G30 Epic** ⑫ v1.3 live E2E.

---

### [BNK] BNK-128~131 인사이트 (2026-06-13) — ★ US-R03 core wired · longterm live drift · merge 335 FULLY UNBLOCKED

> `BENCHMARK_REPORT.md` §130~133 · `COMPETITOR_MATRIX.md` §130~133 · `memory/decisions.md` BNK-128~131 참조. ogada `@a018e71`/`@82bdbcd` 실측.

| # | 항목 | 권장 조치 (planner 반영) |
|---|------|------------------------|
| **BNK-128~129** | **Staff lifecycle Epic WIP→committed** — UI scaffolding @ `e7c289e` → BE API+V86 @ `75440bc` | USER_STORIES US-R03 partial `[x]` · ROADMAP v1.2.1 완료 기준 |
| **BNK-130** | **benchmark→coder 5-cycle 폐루프** — FAQ21825 4상태 ↔ V86 CHECK 1:1 · offboarding 가드 verbatim | REQUIREMENTS G-Staff-LC △ partial |
| **BNK-131** | **Staff lifecycle pilot E2E deepen** @ `9441a3c` · **longterm.or.kr live 수가 셸 드리프트** · **#44 29차** | PLAN_NOTES 추가 질문 · 로컬 snapshot carry |
| **BNK-127 carry** | **LCMS CMS 3-method**·**autosave P3**·**7-5/다중결제 P2** | REQUIREMENTS G2·G-UX-Autosave 유지 |

---

### [PLA] QA 피드백 반영 (2026-06-12, 115차 — BNK-125~127 · TSR 440 · G24/G14 develop · merge BLOCK)

> **115차 자동 기획 동기화** — BNK-125~127(G24/G14 develop 닫힘·LCMS=엔젤·CMS 3-method·FAQ21825 직원 lifecycle·autosave P3)·TSR 440. **QA Open 0건** · **QA-B54 Open→Planned** · **SEC-D22 Planned 유지**.

| 항목 | 115차 관측 | 조치 |
|------|----------|------|
| **baseline** | FE **`479e064`** · WT **CLEAN** · HEAD **827/827 PASS** · BE **`728339e`** · WT **DIRTY 2M** · **724/724 PASS** · **178+145 ahead** · **59 route** | ROADMAP CURRENT BASELINE **115차** 갱신 |
| **BNK-125~127** | **★ G24/G14 develop 닫힘** @ `2642838`/`6f3315a`/`b238779`/`5be9070`/`479e064` · **★ LCMS=엔젤 동일 vendor**·CMS **3-method P2** · **★ FAQ21825 직원 lifecycle Epic P2** · **★ autosave P3** · **#44 27차 0건** | REQUIREMENTS G2·G24·G14·G-Staff-LC · USER_STORIES US-T09/T10·US-R03 · ROADMAP v1.2.1 |
| **QA** | Open **0건** · **QA-B54 Planned**(BE WT dirty) · **SEC-D22 Planned** | QA_FEEDBACK Open→Planned · ROADMAP QA-B54 완료 기준 |
| **merge gate** | P0 `[x]` · FE **ready** · BE **ready**(WT clean 선행) · ⚠ **BLOCK** · 합계 **323 commits** | tester merge **323** — **COD BE WT clean 선행** |
| **잔여 P0/P1** | COD BE WT clean · merge(323) · G24/G14/G34 **live E2E run** · G34 e-sign·보수교육 · G17/G32/G33/G37/G38/G39 live E2E · **직원 lifecycle Epic** · G7 실파일 · G2 SMTP · US-L01 live · **7-5/다중결제 P2** · G30 Epic · v1.3 live E2E | ROADMAP v1.2.1·v2 우선순위 갱신 |

**coder 다음 액션 (115차)**: ① **BE `VisitService.java`·`VisitServiceTest.java` 커밋/revert→WT clean**(QA-B54) ② **tester merge(178+145=323)** ③ G24/G14/G34 **live API E2E run** ④ G34 **e-sign·8-7-1 보수교육** ⑤ G17/G32/G33/G37/G38/G39 **live E2E run** ⑥ G7 **실파일** ⑦ G2 **SMTP** ⑧ US-L01 **live** ⑨ **직원 lifecycle Epic P2** 착수 검토 ⑩ **7-5/다중결제 P2** ⑪ G30 Epic ⑫ v1.3 live E2E.

---

### [BNK] BNK-125~127 인사이트 (2026-06-12) — ★ G24/G14 develop 닫힘 · LCMS=엔젤 · 직원 lifecycle Epic · merge BLOCK

> `BENCHMARK_REPORT.md` §127~129 · `COMPETITOR_MATRIX.md` §127~129 · `memory/decisions.md` BNK-125~127 참조. ogada `@479e064`/`@728339e` 실측.

| # | 항목 | 권장 조치 (planner 반영) |
|---|------|------------------------|
| **BNK-125** | **G24/G14 2중 cite-back 폐루프** — 욕구사정 Form+API·계약서 파일함 Route+첨부 API @ `2642838`/`6f3315a` · V83 G34 integrity @ `ec4cdf6` | USER_STORIES US-T09/T10 partial `[x]` · ROADMAP v1.2.1 완료 기준 `[x]` |
| **BNK-126** | **G24 가정방문 일자 BE 가드** @ `b238779` · **V85 integrity** · **FAQ21825 직원 lifecycle Epic** 신규 | REQUIREMENTS G-Staff-LC · USER_STORIES **US-R03** 신설 |
| **BNK-127** | **LCMS=엔젤 동일 vendor**·CMS **3-method** → **7-5 P2** · **autosave UX P3** · BE WT dirty recurrence(QA-B54) | REQUIREMENTS G2·G-UX-Autosave · 차별화: 특허 marketing 회피·멀티테넌트 SaaS 강조 |

---

### [PLA] QA 피드백 반영 (2026-06-12, 112차 — BNK-119~122 · TSR 428 · G34 partial · merge FULLY UNBLOCKED)

> **112차 자동 기획 동기화** — BNK-119~122(G34 partial·LifecycleWorkflowPanel·G-Payroll P3·cost_master_statistic·module 9-4/9-5/10-3/10-8)·TSR 428. **QA Open 0건(backend/frontend)** · **QA-B50/B51/B52 Fixed** · **SEC-D22 Planned 유지** · **Open→Planned 이동 없음**(이미 0 Open).

| 항목 | 112차 관측 | 조치 |
|------|----------|------|
| **baseline** | FE **`6d6b426`** · WT **CLEAN** · HEAD **800/800 PASS** · BE **`559648f`** · WT **CLEAN** · **689/689 PASS** · **171+140 ahead** · **57 route·81 page** | ROADMAP CURRENT BASELINE **112차** 갱신 |
| **BNK-119~122** | **★ G34 US-S01 FE+BE partial ✅** @ `6d6b426`/`559648f` · **★ LifecycleWorkflowPanel G17/G32 ✅** @ `22bd6b7`/`50e5fac` · **★ QA-B50/B51/B52 Fixed** · **★ G21 paired visit hardening ✅** · **★ G-Payroll Epic P3**(module 11 6 leaf) · **★ cost_master_statistic P3** · **★ FAQ21805·FAQ21820 P2** · **★ func.php 29차 zero drift** · **★ #44 22차 0건** | REQUIREMENTS G34·G40·G-Payroll · USER_STORIES US-S01 partial · ROADMAP v1.2.1 |
| **QA** | Open **0건**(BE/FE) · **QA-B50/B51/B52 Fixed** · **SEC-D22 Planned** | QA_FEEDBACK 갱신 · 이동 없음 |
| **merge gate** | P0 `[x]` · BE+FE **ready** · ★ **FULLY UNBLOCKED** · 합계 **311 commits** | tester merge **311** 즉시 가능 |
| **잔여 P1** | merge(311) · G34 **e-sign·보수교육** · G17/G32/G33/G37/G38/G39 **live API E2E run** · G7 실파일(#27) · G2 SMTP · US-L01 live · G24/G30 Epic · v1.3 live E2E · FAQ21800·FAQ21805·FAQ21820 P2 · 본인부담 6단 게이트 P2 · 7-5·8-7-1 P2 · SEC-D22 `.gitignore` | ROADMAP v1.2.1·v2·v3 우선순위 갱신 |

**coder 다음 액션 (112차)**: ① **tester merge(171+140=311)** ② G34 **전자서명·8-7-1 보수교육 workflow** ③ G17/G32/G33/G37/G38/G39 **live API E2E run** ④ G7 **실파일**(#27) ⑤ G2 **SMTP** ⑥ US-L01 **은행 8종 E2E live** ⑦ **G24/G30 Epic** ⑧ v1.3 live E2E ⑨ **FAQ21800·FAQ21805·FAQ21820 P2** ⑩ **본인부담 6단 게이트 P2** ⑪ **7-5 간편결제 P2** ⑫ **8-7-1 보수교육 P2**.

---

### [BNK] BNK-119~122 인사이트 (2026-06-12) — ★ G34 partial · LifecycleWorkflowPanel · G-Payroll P3 · merge 311 FULLY UNBLOCKED

> `BENCHMARK_REPORT.md` §121~124 · `COMPETITOR_MATRIX.md` §121~124 · `memory/decisions.md` BNK-119~122 참조. ogada `@6d6b426`/`@559648f` 실측.

| # | 항목 | 권장 조치 (planner 반영) |
|---|------|------------------------|
| **BNK-119** | G17/G32 edit-flow pilot E2E deepen · 보수교육 triple-source · #44 21차 | ROADMAP v1.2.1 baseline carry · G34 P2 유지 |
| **BNK-120** | **LifecycleWorkflowPanel** G17 5단계·G32 4단계 — compliance UX 차별 | ROADMAP 완료 기준 `[x]` · QA-B50 선행 |
| **BNK-121** | **G14↔G38 dual-source** — FAQ21805(계약) vs FAQ21820(급여계약통보) 별개 Epic | USER_STORIES US-T10·G38 lifecycle P2 · PLAN_NOTES 추가 질문 |
| **BNK-122** | **G34 partial** @ `6d6b426`/`559648f` · **G-Payroll module 11** 6 leaf P3 · **cost_master_statistic** P3 · route **57** 정정 | REQUIREMENTS G34·G40·G-Payroll · USER_STORIES US-S01 partial · ROADMAP 112차 |

---

### [PLA] QA 피드백 반영 (2026-06-12, 111차 — BNK-115~118 · TSR 415~416 · QA-B49 Fixed · merge FULLY UNBLOCKED)

> **111차 자동 기획 동기화** — BNK-115~118(QA-B49 폐루프·G34 업무수행일지 갭·FAQ21805 계약 lifecycle·getting_started 302)·TSR 415~416. **QA Open 0건(backend/frontend)** · **QA-B49 Fixed** @ `f72da41`/`8fa9f3d` · **SEC-D22 Planned 유지** · **Open→Planned 이동 없음**(이미 Planned/Fixed).

| 항목 | 111차 관측 | 조치 |
|------|----------|------|
| **baseline** | FE **`2cd2cd8`** · WT **CLEAN** · HEAD **775/775 PASS** · BE **`3ad2a90`** · WT **CLEAN** · **672/672 PASS** · **165+135 ahead** · **58 route·81 page** | ROADMAP CURRENT BASELINE **111차** 갱신 |
| **BNK-115~118** | **QA-B49 Fixed ✅** @ `f72da41`/`8fa9f3d` · **G17/G32 edit-flow pilot E2E ✅** @ `2cd2cd8`/`3ad2a90` · **G34 선임 업무수행일지 P2 갭**(케어포 8-1-1/8-1-2 · ogada 0건) · **FAQ21805 수급자 계약 lifecycle P2** · **getting_started.php HTTP 302** · **func.php 26차 zero drift** · **#44 20차 0건** | REQUIREMENTS G34·G14 · USER_STORIES US-S01·US-T10 · ROADMAP v1.2.1 |
| **QA** | Open **0건**(BE/FE) · **QA-B49 Fixed** · **SEC-D22 Planned** | QA_FEEDBACK 갱신 · 이동 없음 |
| **merge gate** | P0 `[x]` · BE+FE **ready** · ★ **FULLY UNBLOCKED** · 합계 **300 commits** | tester merge **300** 즉시 가능 |
| **잔여 P1** | merge(300) · G17/G32/G33/G37/G38/G39 **live API E2E run** · G7 실파일(#27) · G2 SMTP · US-L01 live · G24/G30 Epic · v1.3 live E2E · FAQ21800·FAQ21805 P2 · G34 업무수행일지 P2 · 본인부담 6단 게이트 P2 · 7-5·8-7-1 P2 · SEC-D22 `.gitignore` | ROADMAP v1.2.1·v2·v3 우선순위 갱신 |

**coder 다음 액션 (111차)**: ① **tester merge(165+135=300)** ② G17/G32/G33/G37/G38/G39 **live API E2E run** ③ G7 **실파일**(#27) ④ G2 **SMTP** ⑤ US-L01 **은행 8종 E2E live** ⑥ **G24/G30 Epic** ⑦ v1.3 live E2E ⑧ **FAQ21800·FAQ21805 P2** ⑨ **G34 업무수행일지 P2** ⑩ **본인부담 6단 게이트 P2** ⑪ **7-5 간편결제 P2** ⑫ **8-7-1 보수교육 P2**.

---

### [BNK] BNK-115~118 인사이트 (2026-06-12) — ★ QA-B49 폐루프 · G34 업무수행일지 갭 · merge 300 FULLY UNBLOCKED

> `BENCHMARK_REPORT.md` §117~120 · `COMPETITOR_MATRIX.md` §117~118 · `memory/decisions.md` BNK-115~118 참조. ogada `@2cd2cd8`/`@3ad2a90` 실측.

| # | 항목 | 권장 조치 (planner 반영) |
|---|------|------------------------|
| 1 | **★ QA-B49 Fixed ✅** | FE `@f72da41` snapshot-first + parallel fallbacks · BE `@15b3c7e` lineage · TSR 414~416 recurrence closed |
| 2 | **★ G17/G32 edit-flow pilot E2E ✅** | FE `@2cd2cd8` `pilotPageFlows` · BE `@3ad2a90` visit edit-cancel·case-management pilot |
| 3 | **★ G34 선임 요양보호사 업무수행일지 P2 갭** | 케어포 func.php **8-1-1/8-1-2** depth-3 dual-leaf · ogada `workLog|업무수행일지` **0건** → **US-S01** v3 P2 |
| 4 | **★ FAQ21805 수급자 계약 lifecycle P2** | 이지케어 [비정기] 계약 갱신·해지·서명 → **US-T10** · G14 확장 |
| 5 | **getting_started.php HTTP 302** | BNK-114 HTTP 200 → **302** 접근 변동 · Wayback 스냅샷 신뢰도 재확인 |
| 6 | **func.php 26차 zero drift** | md5 `6226e6eb` · 108 leaf · 7-x 11 leaf |
| 7 | **#44 20차 0건** | law byl18·longterm2026·통합재가·MOHW247 — 수동 보류 유지 |
| 8 | **merge gate 300** | FE **165** ahead · WT **CLEAN** · BE **135** ahead · WT **CLEAN** → ★ **FULLY UNBLOCKED** |
| 9 | **SEC-D22 Planned** | `scripts/dev-backend.env` `.gitignore` 미매칭 — **infra/OPS** · MEDIUM · merge BLOCK 아님 |

---

### [PLA] QA 피드백 반영 (2026-06-12, 110차 — BNK-110~114 · TSR 400~404 · QA-B49 Planned)

> **110차 자동 기획 동기화** — BNK-110~114(G38/G39 dashboard deepen·BE pilot E2E·widget counts API·G17/G32 edit)·TSR 400~404. **QA Open 0건(backend/frontend)** · **QA-B49 Open→Planned**(FE WT DIRTY 2M · dashboard snapshot aggregation WIP) · **SEC-D22 Planned 유지**.

| 항목 | 110차 관측 | 조치 |
|------|----------|------|
| **baseline** | FE **`26499b3`** · WT **DIRTY 2M** · HEAD **769/769**·WT **770/770 PASS** · BE **`a0a7f9c`** · WT **CLEAN** · **666/666 PASS** · **161+130 ahead** · **58 route·80 page** | ROADMAP CURRENT BASELINE **110차** 갱신 |
| **BNK-110~114** | **G39 dashboard widget ✅** @ `a16e1fe`/`8e66ae8` · **G38 FE+live E2E ✅** @ `28c22b0`/`87e6fae`/`4b2b082` · **G38/G39 BE pilot E2E ✅** @ `a9f8bda` · **BE dashboard widget counts ✅** @ `a0a7f9c` · **G17/G32 edit ✅** @ `26499b3` · **FAQ21800 욕구사정 P2** · **module8 8-8~8-12 P2** · **#44 18차 0건** | REQUIREMENTS G38/G39/G24 · USER_STORIES US-T08 · ROADMAP v1.2.1 |
| **QA** | Open **0건**(BE/FE) · **QA-B49 Planned**(BLOCK·FE WT) · **SEC-D22 Planned** | QA_FEEDBACK Open→Planned 이동 |
| **merge gate** | P0 `[x]` · BE **ready** · FE **BLOCK** · 합계 **291 commits BLOCK** | COD QA-B49→WT clean→tester merge |
| **잔여 P1** | **QA-B49 커밋/revert** · merge(291) · G17/G32/G33/G37/G38/G39 **live API E2E run** · G7 실파일(#27) · G2 SMTP · US-L01 live · G24/G30 Epic · v1.3 live E2E · FAQ21800 P2 · 본인부담 6단 게이트 P2 · 7-5·8-7-1 P2 · SEC-D22 `.gitignore` | ROADMAP v1.2.1·v2 우선순위 갱신 |

**coder 다음 액션 (110차)**: ① **QA-B49** — `DashboardPage.jsx`·`DashboardPage.test.jsx` **단일 커밋 또는 revert** → WT **CLEAN** ② **tester merge(161+130=291)** ③ G17/G32/G33/G37/G38/G39 **live API E2E run** ④ G7 **실파일**(#27) ⑤ G2 **SMTP** ⑥ US-L01 **은행 8종 E2E live** ⑦ **G24/G30 Epic** ⑧ v1.3 live E2E ⑨ **FAQ21800 욕구사정 P2** ⑩ **본인부담 6단 게이트 P2** ⑪ **7-5 간편결제 P2** ⑫ **8-7-1 보수교육 P2**.

---

### [BNK] BNK-110~114 인사이트 (2026-06-12) — ★ G38/G39 폐루프 deepen · BE widget counts · QA-B49 merge BLOCK

> `BENCHMARK_REPORT.md` §112~116 · `COMPETITOR_MATRIX.md` §112~116 · `memory/decisions.md` BNK-110~114 참조. ogada `@26499b3`/`@a0a7f9c` 실측.

| # | 항목 | 권장 조치 (planner 반영) |
|---|------|------------------------|
| 1 | **★ G39 FE dashboard widget ✅** | BNK-110 `@a16e1fe` → BNK-113 `@8e66ae8` weekly/monthly deepen — indicator-44 4-pillar |
| 2 | **★ G38 FE+live E2E harness ✅** | BNK-111 `@28c22b0`/`87e6fae` · partial-load warning `@4b2b082` (BNK-112) |
| 3 | **★ G38/G39 BE pilot service-flow E2E ✅** | BNK-112 `@a9f8bda` — `ProvisionCompliancePilotServiceFlowE2eTest` |
| 4 | **★ BE dashboard widget counts API ✅** | BNK-114 `@a0a7f9c` — `BranchDashboardResponse` snapshot fields |
| 5 | **★ G17/G32 edit flow ✅** | BNK-113 `@26499b3` — case management·functional recovery edit |
| 6 | **★ FAQ21800 [연간] 정기 욕구사정 P2** | BNK-113 — 지표15·`2.수급자관리>기초평가>욕구사정` → **G24/G14 Epic** |
| 7 | **★ 케어포 module8 8-8~8-12 P2** | BNK-112 — 자원봉사·고충·건강검진·직원현황 리포트 |
| 8 | **#44 18차 0건** | law byl18·longterm2026·통합재가·MOHW247 — BNK-25 placeholder 유지 |
| 9 | **merge gate 291 BLOCK** | FE **161** ahead · WT **DIRTY 2M**(QA-B49) · BE **130** ahead · WT **CLEAN** |
| 10 | **SEC-D22 Planned** | `scripts/dev-backend.env` `.gitignore` 미매칭 — **infra/OPS** · MEDIUM · merge BLOCK 아님 |

---

### [PLA] QA 피드백 반영 (2026-06-12, 109차 — BNK-106~109 · TSR 389~392 · SEC-D22 Planned)

> **109차 자동 기획 동기화** — BNK-106~109(G37 FE+live E2E+MIME fallback·G38 care-plan notification compliance BE·G39 provision result evaluation FE+BE)·TSR 389~392. **QA Open 0건(backend/frontend)** · **SEC-D22 Planned 유지** — infra `.gitignore` · MEDIUM · BLOCK 아님 · **Open→Planned 이동 없음**.

| 항목 | 109차 관측 | 조치 |
|------|----------|------|
| **baseline** | FE **`1c99bcd`** · BE **`f082933`** · **155+125 ahead** · **양쪽 WT CLEAN** · **56 route·80 page** · **749/749·657/657 PASS** | ROADMAP CURRENT BASELINE **109차** 갱신 |
| **BNK-106~109** | **G37 FE+live E2E+MIME fallback ✅** @ `e026ae9`/`6875af5`/`e9d1178`(QA-B46 Fixed) · **G38 care-plan notification compliance BE ✅** @ `5fd35a6`(FAQ 21802 · **FE P2**) · **G39 provision result evaluation FE+BE ✅** @ `1c99bcd`/`f082933`(V80 · **StatCard P2**) · **silverangel 지표44 20차 zero drift** · **#44 16차 0건** · **ezCare 9,323** | REQUIREMENTS G37·G38·G39 · USER_STORIES US-M01-g·US-T08 · API_SPEC G38/G39 갱신 |
| **QA** | Open **0건**(BE/FE) · QA-B45/B46 **Fixed** · **SEC-D22 Planned** | QA_FEEDBACK 갱신 · 이동 없음 |
| **merge gate** | P0 `[x]` · BE+FE **ready** · ★ **FULLY UNBLOCKED** · **280 commits** | tester merge **280** 즉시 가능 |
| **잔여 P1** | merge(280) · G17/G32/G33/G37/G39 **live API E2E run** · G7 실파일(#27) · G2 SMTP · US-L01 live · G24/G30 Epic · v1.3 live E2E · **G38 FE·G39 StatCard P2** · 본인부담 6단 게이트 P2 · 7-5·8-7-1 P2 · SEC-D22 `.gitignore` | ROADMAP v1.2.1·v2 우선순위 갱신 |

**coder 다음 액션 (109차)**: ① **tester merge(155+125=280)** ② G17/G32/G33/G37/G39 **live API E2E run** ③ G7 **실파일**(#27) ④ G2 **SMTP** ⑤ US-L01 **은행 8종 E2E live** ⑥ **G24/G30 Epic** ⑦ v1.3 live E2E ⑧ **G38 FE 모니터링 UI P2** ⑨ **G39 dashboard StatCard P2** ⑩ **본인부담 6단 게이트 P2** ⑪ **7-5 간편결제 P2** ⑫ **8-7-1 보수교육 P2**.

---

### [BNK] BNK-106~109 인사이트 (2026-06-12) — ★ G37 폐루프 완전 닫힘 · G38 BE · G39 FE+BE · merge gate 280 FULLY UNBLOCKED

> `BENCHMARK_REPORT.md` §108~111 · `COMPETITOR_MATRIX.md` §108~111 · `memory/decisions.md` BNK-106~109 참조. ogada `@1c99bcd`/`@f082933` 실측.

| # | 항목 | 권장 조치 (planner 반영) |
|---|------|------------------------|
| 1 | **★ G37 FE+live E2E+MIME fallback ✅** | BNK-105→106→108→109 `@e026ae9`/`6875af5`/`e9d1178` — `GradeHistoryAttachmentPanel`·live harness·QA-B46 spoofing 차단 |
| 2 | **★ G38 care-plan notification compliance BE ✅** | BNK-106 `@5fd35a6` — `CarePlanNotificationComplianceService`·5/11-month milestone·FAQ 21802 · **FE StatCard P2** |
| 3 | **★ G39 provision result evaluation FE+BE ✅** | BNK-107 `@f082933`/`1c99bcd` — V80·`ProvisionResultEvaluationPage`·indicator-44 4-pillar · **dashboard StatCard P2** |
| 4 | **★ silverangel 지표44 20차 zero drift** | md5 `c79c1be3` · V80 schema 1:1 패리티 교차검증 |
| 5 | **#44 16차 0건** | law byl18·longterm2026·통합재가·MOHW247 — BNK-25 placeholder 유지 |
| 6 | **ezCare 9,323** | +3 micro-drift · 번복 아님 |
| 7 | **merge gate 280** | FE **155** ahead · WT **CLEAN** · BE **125** ahead · WT **CLEAN** → ★ **FULLY UNBLOCKED** |
| 8 | **SEC-D22 Planned** | `scripts/dev-backend.env` `.gitignore` 미매칭 — **infra/OPS** · MEDIUM · merge BLOCK 아님 |

---

### [PLA] QA 피드백 반영 (2026-06-12, 108차 — BNK-103~105 · TSR 375~380 · SEC-D22 Planned)

> **108차 자동 기획 동기화** — BNK-103~105(G17/G32 compliance contracts·G33 pilot E2E·J03 primary guardian dispatch·G37 BE)·TSR 375~380. **QA Open 0건(backend/frontend)** · **SEC-D22 Planned 유지** — infra `.gitignore` · MEDIUM · BLOCK 아님 · **Open→Planned 이동 없음**.

| 항목 | 108차 관측 | 조치 |
|------|----------|------|
| **baseline** | FE **`8b0c6c7`** · BE **`0325d95`** · **149+120 ahead** · **양쪽 WT CLEAN** · **56 route·78 page** · **717/717·637/637 PASS** | ROADMAP CURRENT BASELINE **108차** 갱신 |
| **BNK-103~105** | **G17/G32 API contracts+422 guard ✅** · **G33 settlement pilot E2E+reload fallback ✅** · **G26 ClientDetail NTS xlsx E2E ✅** · **J03 primary guardian dispatch ✅** · **G37 care-plan attachment BE ✅**(FE UI P1) · **Channel.io → G35 CIST(P3)·G34 문자 인증(P2)** · **#44 15차 0건** | REQUIREMENTS G17·G26·G32·G33·G37 · USER_STORIES US-J03·US-T06·US-T07·US-L04·US-M01-g 갱신 |
| **QA** | Open **0건**(BE/FE) · **SEC-D22 Planned** · SEC-D23 **Fixed** @ `c89a82b` | QA_FEEDBACK 갱신 · 이동 없음 |
| **merge gate** | P0 `[x]` · BE+FE **ready** · ★ **FULLY UNBLOCKED** · **269 commits** | tester merge **269** 즉시 가능 |
| **잔여 P1** | merge(269) · G17/G32/G33 **live API E2E run** · **G37 FE care-plan attachment UI** · G7 실파일(#27) · G2 SMTP · US-L01 live · G24/G30 Epic · v1.3 live E2E · 본인부담 6단 게이트 P2 · 7-5·8-7-1 P2 · SEC-D22 `.gitignore` | ROADMAP v1.2.1·v2 우선순위 갱신 |

**coder 다음 액션 (108차)**: ① **tester merge(149+120=269)** ② G17/G32/G33 **live API E2E run**(`programComplianceLiveApi.e2e.test.js`) ③ **G37 FE care-plan attachment UI** ④ G7 **실파일**(#27) ⑤ G2 **SMTP** ⑥ US-L01 **은행 8종 E2E live** ⑦ **G24/G30 Epic** ⑧ v1.3 live E2E ⑨ **본인부담 6단 게이트 P2** ⑩ **7-5 간편결제 P2** ⑪ **8-7-1 보수교육 P2**.

---

### [BNK] BNK-103~105 인사이트 (2026-06-12) — ★ benchmark→coder 3중 cite-back · G37 BE · J03 dispatch · merge gate 269 FULLY UNBLOCKED

> `BENCHMARK_REPORT.md` §105~107 · `COMPETITOR_MATRIX.md` §105~107 · `memory/decisions.md` BNK-103~105 참조. ogada `@8b0c6c7`/`@0325d95` 실측.

| # | 항목 | 권장 조치 (planner 반영) |
|---|------|------------------------|
| 1 | **★ G17/G32 program compliance contracts+422 guard ✅** | BNK-105 `@8b0c6c7` — `programComplianceServices.test.js`·`CaseManagementPage`·`FunctionalRecoveryPage` |
| 2 | **★ G33 settlement pilot E2E+reload fallback ✅** | BNK-105 `@730792b`/`eb488799` — `pilotPageFlows` G33·`BillingSettingsPanel` default settings reload |
| 3 | **★ G26 ClientDetail NTS xlsx E2E ✅** | BNK-75 cite-back `@48827b6` — billing tab xlsx export (실파일 제출 P2 잔여) |
| 4 | **★ J03 primary guardian dispatch ✅** | BNK-105 `@555a19f`/`d86405c` — `NotificationService` primary 우선·E2E |
| 5 | **★ G37 등급 인정기간 PDF 첨부 BE ✅** | BNK-105 `@0325d95` — V78·attachment CRUD API · **FE UI P1** |
| 6 | **★ Channel.io 3 evidence** | G35 **CIST(P3)** · G34 **전자서명 문자 인증(P2)** · G37 **이용계획서 PDF(P2→BE 닫힘)** |
| 7 | **#44 15차 0건** | law byl18·longterm2026·통합재가·MOHW247 — BNK-25 placeholder 유지 |
| 8 | **merge gate 269** | FE **149** ahead · WT **CLEAN** · BE **120** ahead · WT **CLEAN** → ★ **FULLY UNBLOCKED** |
| 9 | **SEC-D22 Planned** | `scripts/dev-backend.env` `.gitignore` 미매칭 — **infra/OPS** · MEDIUM · merge BLOCK 아님 |

---

### [PLA] QA 피드백 반영 (2026-06-12, 107차 — BNK-99~102 · TSR 363~368 · SEC-D22 Planned)

> **107차 자동 기획 동기화** — BNK-99~102(G17 지표27 3행·G33 settlement+V77·G2 CMS debit·live E2E harness)·TSR 363~368. **QA Open 0건(backend/frontend)** · **SEC-D22 Planned 유지** — infra `.gitignore` · MEDIUM · BLOCK 아님 · **Open→Planned 이동 없음**.

| 항목 | 107차 관측 | 조치 |
|------|----------|------|
| **baseline** | FE **`c413615`** · BE **`838a7f6`** · **142+114 ahead** · **양쪽 WT CLEAN** · **56 route·78 page** · **693/693·609/609 PASS** | ROADMAP CURRENT BASELINE **107차** 갱신 |
| **BNK-99~102** | **G17 지표27 3행 BE→FE ✅** · **G33 settlement UI+V77 integrity ✅** · **G2 CMS debit 이력+FAILED 응답 ✅** · **programCompliance live E2E harness ✅** · **이지케어 FAQ21815·6단 본인부담 P2** · **#44 13차 0건** · **lcms 상품설명서·단기보호 74,060 P2** | REQUIREMENTS G17·G2·G33 · USER_STORIES US-T06·US-L05 갱신 |
| **QA** | Open **0건**(BE/FE) · **SEC-D22 Planned** · SEC-D23 **Fixed** @ `c89a82b` | QA_FEEDBACK 갱신 · 이동 없음 |
| **merge gate** | P0 `[x]` · BE+FE **ready** · ★ **FULLY UNBLOCKED** · **256 commits** | tester merge **256** 즉시 가능 |
| **잔여 P1** | merge(256) · G17/G32/G33 **live E2E run** · G7 실파일(#27) · G2 SMTP · US-L01 live · G24/G30 Epic · v1.3 live E2E · 본인부담 6단 게이트 P2 · 7-5·8-7-1 P2 · SEC-D22 `.gitignore` | ROADMAP v1.2.1·v2 우선순위 갱신 |

**coder 다음 액션 (107차)**: ① **tester merge(142+114=256)** ② G17/G32/G33 **live E2E run**(`programComplianceLiveApi.e2e.test.js`) ③ G7 **실파일**(#27) ④ G2 **SMTP** ⑤ US-L01 **은행 8종 E2E live** ⑥ **G24/G30 Epic** ⑦ v1.3 live E2E ⑧ **본인부담 6단 게이트 P2** ⑨ **7-5 간편결제 P2** ⑩ **8-7-1 보수교육 P2**.

---

### [BNK] BNK-99~102 인사이트 (2026-06-12) — ★ G17 지표27 3행 폐루프 · G33 settlement+V77 · G2 CMS debit · live E2E harness · merge gate 256 FULLY UNBLOCKED

> `BENCHMARK_REPORT.md` §101~104 · `COMPETITOR_MATRIX.md` §101~104 · `memory/decisions.md` BNK-99~102 참조. ogada `@c413615`/`@838a7f6` 실측.

| # | 항목 | 권장 조치 (planner 반영) |
|---|------|------------------------|
| 1 | **★ G17 지표27 3행 BE→FE ✅** | BNK-100 BE @ `0048105`/`e820b28` → BNK-101 FE StatCard @ `21b1855` → BNK-102 dashboard widgets @ `f1c60fe` — row3 verbatim 「급여제공 시작일까지 기능회복훈련 계획 수립」 |
| 2 | **★ G33 settlement UI+V77 integrity ✅** | BNK-100 `@359cf0c` settlement modal · `@42bc06e` V77 integrity (QA-B44 Fixed) |
| 3 | **★ G2 CMS debit 이력+FAILED 응답 ✅** | BNK-102 `@c5a6cec` failed debit history preserve · `@838a7f6` operator retry FAILED response |
| 4 | **★ programCompliance live E2E harness ✅** | `@c413615` `programComplianceLiveApi.e2e.test.js` — **run 잔여**(post-merge) |
| 5 | **★ 이지케어 FAQ21815·6단 본인부담 게이트** | BNK-99 `ezCare_change_work`·Channel.io 2d53ea63 — **본인부담 6단 게이트 P2** |
| 6 | **★ lcms 상품설명서·단기보호 74,060** | BNK-100 MOHW↔롱텀 교차 · **G18 단기보호 시드 P2** |
| 7 | **#44 13차 0건** | law byl18·longterm2026·통합재가·MOHW247 — BNK-25 placeholder 유지 |
| 8 | **merge gate 256** | FE **142** ahead · WT **CLEAN** · BE **114** ahead · WT **CLEAN** → ★ **FULLY UNBLOCKED** |
| 9 | **SEC-D22 Planned** | `scripts/dev-backend.env` `.gitignore` 미매칭 — **infra/OPS** · MEDIUM · merge BLOCK 아님 |

---

### [PLA] QA 피드백 반영 (2026-06-12, 106차 — BNK-95~98 · TSR 346~356 · SEC-D22 Planned)

> **106차 자동 기획 동기화** — BNK-95~98(G33 폐루프·G32 FE 5기둥·PDF 7-x·getting_started)·TSR 346~356. **QA Open 0건(backend/frontend)** · **SEC-D22 Open→Planned** — infra `.gitignore` · MEDIUM · BLOCK 아님.

| 항목 | 106차 관측 | 조치 |
|------|----------|------|
| **baseline** | FE **`7564c2a`** · BE **`70e6191`** · **135+109 ahead** · **양쪽 WT CLEAN** · **55 route·46 page** · **679/679·603/603 PASS** | ROADMAP CURRENT BASELINE **106차** 갱신 |
| **BNK-95~98** | **G33 FE+BE+overdue+settlement ✅** · **G32 evaluationConductedMet FE+BE ✅** · **US-D01 primary guardian ✅** · **PDF 7-x 삼원 불일치 정책** · **getting_started 이동서비스 분리** · **#44 11차 0건** | REQUIREMENTS G33·G32 · USER_STORIES US-L05·US-T07 갱신 |
| **QA** | Open **0건**(BE/FE) · **SEC-D22 Planned** · SEC-D23 **Fixed** @ `c89a82b` | QA_FEEDBACK Open→Planned 이동 |
| **merge gate** | P0 `[x]` · BE+FE **ready** · ★ **FULLY UNBLOCKED** · **244 commits** | tester merge **244** 즉시 가능 |
| **잔여 P1** | merge(244) · G17/G32/G33 **live E2E** · G7 실파일(#27) · G2 SMTP · US-L01 live · G24/G30 Epic · v1.3 live E2E · 본인부담 공단비교 P2 · 7-5·8-7-1 P2 · SEC-D22 `.gitignore` | ROADMAP v1.2.1·v2 우선순위 갱신 |

**coder 다음 액션 (106차)**: ① **tester merge(135+109=244)** ② G17/G32/G33 **live E2E** ③ G7 **실파일**(#27) ④ G2 **SMTP** ⑤ US-L01 **은행 8종 E2E live** ⑥ **G24/G30 Epic** ⑦ v1.3 live E2E ⑧ **본인부담 공단비교 UX P2** ⑨ **7-5 간편결제 P2** ⑩ **8-7-1 보수교육 P2**.

---

### [BNK] BNK-95~98 인사이트 (2026-06-12) — ★ G33 BNK-94→98 폐루프 · G32 FE 5기둥 · PDF 7-x 삼원 불일치 · getting_started · merge gate 244 FULLY UNBLOCKED

> `BENCHMARK_REPORT.md` §97~100 · `COMPETITOR_MATRIX.md` §97~100 · `memory/decisions.md` BNK-95~98 참조. ogada `@7564c2a`/`@70e6191` 실측.

| # | 항목 | 권장 조치 (planner 반영) |
|---|------|------------------------|
| 1 | **★ G33 청구시작 폐루프 ✅** | BNK-94 PDF p.90 → BNK-97 V76+settings @ `3d5eb3e`/`9e1a2ed` → BNK-98 ledger+overdue @ `deaae7a`/`7564c2a`+settlement @ `70e6191` — **7-x 10/11 + G33 별도 ✅** |
| 2 | **★ G32 evaluationConductedMet FE ✅** | BNK-95 WIP → BNK-96 `@7f2289b` StatCard+widget — **5기둥 FE+BE 완전 닫힘** |
| 3 | **★ US-D01 primary guardian BE ✅** | `@0441a07` `CreateClientRequest` primary guardian 필수 — BNK-96 |
| 4 | **★ PDF↔func.php 7-x 삼원 불일치** | func `7-3`=미납 vs PDF `7-3`=청구시작 · func `7-5`=간편결제 vs PDF `7-5`=연간대장 · **Route ID 정본=func.php** · **rename 금지** |
| 5 | **★ getting_started 이동서비스 분리** | 주야간/시설 매뉴얼 이원화 + YouTube 「이동서비스 관리」— demo-work=시설 셸(119 view·송영 0) |
| 6 | **★ 이지케어 FAQ21474·본인부담 비교** | 일정확정 4단 메뉴 · Channel.io 8d304da8 6건 차이 — **본인부담 공단비교 P2** 잔여 |
| 7 | **#44 11차 0건** | law byl18·longterm2026·통합재가·MOHW247 — BNK-25 placeholder 유지 |
| 8 | **merge gate 244** | FE **135** ahead · WT **CLEAN** · BE **109** ahead · WT **CLEAN** → ★ **FULLY UNBLOCKED** |
| 9 | **SEC-D22 Planned** | `scripts/dev-backend.env` `.gitignore` 미매칭 — **infra/OPS** · MEDIUM · merge BLOCK 아님 |

---

### [PLA] QA 피드백 반영 (2026-06-11, 105차 — BNK-91~94 · TSR 338~344 · QA Open 0건)

> **105차 자동 기획 동기화** — BNK-91~94(G32 triple-source·compliance 4기둥·7-3 갭·PilotFixture)·TSR 338~344. **QA Open 0건** · **Open→Planned 이동 없음** — QA-B42/B43 **Fixed** @ `40c303d`/`37e6b00`.

| 항목 | 105차 관측 | 조치 |
|------|----------|------|
| **baseline** | FE **`37e6b00`** · BE **`208b37e`** · **129+103 ahead** · **양쪽 WT CLEAN** · **55 route·78 page** · **656/656·581/581 PASS** | ROADMAP CURRENT BASELINE **105차** 갱신 |
| **BNK-91~94** | **G32 triple-source ✅** · **compliance 4기둥 BE ✅** · **V75 plan FE+BE ✅** · **PDF 7-3 P2 갭** · **PilotFixture ✅** · **#44 10차 0건** | REQUIREMENTS G32·G33·G34 · USER_STORIES US-T07 갱신 |
| **QA** | Open **0건** · B42/B43 **Fixed** · Planned **0건** | QA_FEEDBACK 갱신 · 이동 없음 |
| **merge gate** | P0 `[x]` · BE+FE **ready** · ★ **FULLY UNBLOCKED** · **232 commits** | tester merge **232** 즉시 가능 |
| **잔여 P1** | merge(232) · G32 **`evaluationConductedMet` FE StatCard** · G17/G32 **live E2E** · G7 실파일(#27) · G2 SMTP · US-L01 live · G24/G30 Epic · v1.3 live E2E · 7-3 청구시작 P2 · 본인부담 공단비교 P2 | ROADMAP v1.2.1·v2 우선순위 갱신 |

**coder 다음 액션 (105차)**: ① **tester merge(129+103=232)** ② G32 **`evaluationConductedMet` FE StatCard** ③ G17/G32 **live E2E** ④ G7 **실파일**(#27) ⑤ G2 **SMTP** ⑥ US-L01 **은행 8종 E2E live** ⑦ **G24/G30 Epic** ⑧ v1.3 live E2E ⑨ **7-3 청구시작 P2** ⑩ **본인부담 공단비교 UX P2**.

---

### [BNK] BNK-91~94 인사이트 (2026-06-11) — ★ G32 triple-source·compliance 4기둥 BE·V75 plan FE+BE·PDF 7-3 갭·PilotFixture·merge gate 232 FULLY UNBLOCKED

> `BENCHMARK_REPORT.md` §93~96 · `COMPETITOR_MATRIX.md` §93~96 · `memory/decisions.md` BNK-91~94 참조. ogada `@37e6b00`/`@208b37e` 실측.

| # | 항목 | 권장 조치 (planner 반영) |
|---|------|------------------------|
| 1 | **★ G32 triple-source 확정** | BNK-91 이지케어 FAQ21797 「반기·3인·7필드+서명·평가지표23」→ silverangel 지표43+케어포8-5와 **삼원 정본** · ogada **정본=지표43**(분기·≥2인) · P2: 직종별·서명 확장 |
| 2 | **★ G32 compliance 4기둥 BE ✅** | BNK-92~93 `evaluationConductedMet` @ `11277b9` — 회의·≥2인·30일반영·**지표29 평가실시** · **잔여 P1**: FE StatCard/widget 미소비 |
| 3 | **★ V75 `case_management_plan` FE+BE ✅** | BNK-91~92 BE @ `0a270a2` · FE Field @ `443f379`/`40c303d` · QA-B42 **Fixed** |
| 4 | **★ PDF 7-3 청구시작 P2 신규 갭** | BNK-94 케어포 매뉴얼 p.90 「도입 전 미납/선납·1회 생성 후 변경 불가」— func.php `7-3`=미납관리와 **번호 충돌** → G33 온보딩 초기 잔액 UX |
| 5 | **★ func.php 108항목·리포트 38.3%** | BNK-94 — ogada ~5 report routes vs 케어포 36 리포트 leaf → **v3.1 P3** ERP 리포트 밀도 |
| 6 | **★ FAQ 45982·`8-7-1` 보수교육** | K-MMSE·문자 별도 과금(P3 안내) · 요양보호사 보수교육 depth-3 leaf(P2) → G34 |
| 7 | **★ PilotFixturePanel ✅** | `@37e6b00` NHIS·visit fixture·pilot API setup — QA-B43 Fixed · 파일럿 G7 실파일(#27) 선행 조건 완화 |
| 8 | **#44 10차 0건** | law byl18·longterm2026·통합재가 3원천 — BNK-25 placeholder 유지·하드코딩 금지 |
| 9 | **merge gate 232** | FE **129** ahead · WT **CLEAN** · BE **103** ahead · WT **CLEAN** → ★ **FULLY UNBLOCKED** · **656/656·581/581 PASS** |
| 10 | **잔여 P1** | merge(232) · G32 FE StatCard · G17/G32 live E2E · US-L01 live · G24/G30 Epic · 7-3 청구시작 P2 |

---

### [PLA] QA 피드백 반영 (2026-06-11, 104차 — BNK-87~90 · TSR 331~332 · QA Open 0건)

> **104차 자동 기획 동기화** — BNK-87~90(G17/G32 FE+BE·V74·케어포 8-5·NHIS 비교)·TSR 331~332. **QA Open 0건** · **Open→Planned 이동 없음** — QA-B41 **Fixed** @ `5e1828c`.

| 항목 | 104차 관측 | 조치 |
|------|----------|------|
| **baseline** | FE **`0adf8c6`** · BE **`5e1828c`** · **122+98 ahead** · **양쪽 WT CLEAN** · **54 route·45 page** · **646/646·576/576 PASS** | ROADMAP CURRENT BASELINE **104차** 갱신 |
| **BNK-87~90** | **G17/G32 FE+BE ✅** · **V74 integrity ✅** · **G32 dual-source**(지표43+케어포 8-5) · **NHIS 비교 partial** · **#44 7차 0건** | REQUIREMENTS·USER_STORIES US-T06·US-T07·G32 행 갱신 |
| **QA** | Open **0건** · B41 **Fixed** · Planned **0건** | QA_FEEDBACK 갱신 · 이동 없음 |
| **merge gate** | P0 `[x]` · BE+FE **ready** · ★ **FULLY UNBLOCKED** · **220 commits** | tester merge **220** 즉시 가능 |
| **잔여 P1** | merge(220) · G17/G32 **live E2E** · G7 실파일(#27) · G2 SMTP · US-L01 live · G24/G30 Epic · v1.3 live E2E · 본인부담 공단비교 P2 | ROADMAP v1.2.1·v2 우선순위 갱신 |

**coder 다음 액션 (104차)**: ① **tester merge(122+98=220)** ② G17/G32 **live E2E** ③ G7 **실파일**(#27) ④ G2 **SMTP** ⑤ US-L01 **은행 8종 E2E live** ⑥ **G24/G30 Epic** ⑦ v1.3 live E2E ⑧ **본인부담 공단비교 UX P2**(이지케어 2d53ea63) ⑨ **G26 xlsx E2E P2**.

---

### [BNK] BNK-87~90 인사이트 (2026-06-11) — ★ G17/G32 FE+BE 폐루프 마감 · 케어포 8-5 dual-source · 이지케어 본인부담 비교 · merge gate 220 FULLY UNBLOCKED

> `BENCHMARK_REPORT.md` §89~92 · `COMPETITOR_MATRIX.md` §89~92 · `memory/decisions.md` BNK-87~90 참조. ogada `@0adf8c6`/`@5e1828c` 실측.

| # | 항목 | 권장 조치 (planner 반영) |
|---|------|------------------------|
| 1 | **★ G17/G32 FE+BE 폐루프 마감** | BNK-87 `c288fdd` FE 착수 → BNK-88 `7eebd8c` attendee 정규화+V74 `622b5e5` → BNK-89 compliance NaN-safe·분기 bounds → BNK-90 G17 서버 오류 매핑 `b58429d` — **잔여: live E2E** |
| 2 | **★ G32 dual-source 패리티** | 케어포 func.php **`8-5.사례관리 회의록`** verbatim(BNK-90) + silverangel 지표43 — ogada G32 = **평가+ERP 메뉴 동등** 영업 근거 · **P2**: 케어포 `8-6 회의록(운영위/보호자)` 유형 분기 |
| 3 | **★ 이지케어 본인부담 비교 partial** | Channel.io 2d53ea63 「일정확정 전 공단 청구명세서 비교」→ `BillingDetailPage` panel @ `0adf8c6`·BE API @ `2225a7a` — **P2 잔여**: 일괄체크·확정 후 잠금 UX |
| 4 | **★ lcms 셀프 가입 3-step** | viewRegStep `9283f031` — 정원 4분류·KMC 본인인증 = ogada **A방식(platform_admin)** 대비 온보딩 차별화 근거 |
| 5 | **#44 7차 0건** | law byl18·longterm 2026·통합재가 3원천 — BNK-25 placeholder 유지·하드코딩 금지 |
| 6 | **merge gate 220** | FE **122** ahead · WT **CLEAN** · BE **98** ahead · WT **CLEAN** → ★ **FULLY UNBLOCKED** · **646/646·576/576 PASS** |
| 7 | **잔여 P1** | tester merge(220) · G17/G32 live E2E · US-L01 live · G24/G30 Epic · v1.3 live E2E · 본인부담 공단비교 P2 |

---

### [PLA] QA 피드백 반영 (2026-06-11, 103차 — BNK-84~86 · TSR 319~320 · QA Open 0건)

> **103차 자동 기획 동기화** — BNK-84~86(7-9·G17·G32 BE)·TSR 319~320. **QA Open 0건** · **Open→Planned 이동 없음** — QA-B37/B38 **Fixed** @ `53e4016`/`b92a1d4`/`55fae99`.

| 항목 | 103차 관측 | 조치 |
|------|----------|------|
| **baseline** | FE **`53e4016`** · BE **`55fae99`** · **116+94 ahead** · **양쪽 WT CLEAN** · **54 route·74 page** · **616/616·569/569 PASS** | ROADMAP CURRENT BASELINE **103차** 갱신 |
| **BNK-84~86** | **7-9 FE+BE ✅** · **G17 BE ✅** · **G32 BE ✅** · **통합재가 월 10만원** · **silverangel 6차 zero drift** · **#44 6차 0건** | REQUIREMENTS·USER_STORIES US-M03-c·US-T06·US-T07 갱신 |
| **QA** | Open **0건** · B37/B38 **Fixed** · Planned **0건** | QA_FEEDBACK 갱신 · 이동 없음 |
| **merge gate** | P0 `[x]` · BE+FE **ready** · ★ **FULLY UNBLOCKED** · **210 commits** | tester merge **210** 즉시 가능 |
| **잔여 P1** | merge(210) · **G32 FE** · **G17 FE** · G7 실파일(#27) · G2 SMTP · US-L01 live · G24/G30 Epic · v1.3 live E2E · G26 xlsx E2E P2 | ROADMAP v1.2.1·v2 우선순위 갱신 |

**coder 다음 액션 (103차)**: ① **tester merge(116+94=210)** ② **G32 FE**(`/case-management/meetings`·6필드·2인 이상·30일 widget) ③ **G17 FE**(`/programs/functional-recovery/*`) ④ G7 **실파일**(#27) ⑤ G2 **SMTP** ⑥ US-L01 **은행 8종 E2E live** ⑦ **G24/G30 Epic** ⑧ v1.3 live E2E ⑨ **G26 xlsx E2E P2**.

---

### [BNK] BNK-84~86 인사이트 (2026-06-11) — ★ 7-9·G17·G32 BE 3폐루프 닫힘 · silverangel 6차 zero drift · 통합재가 월 10만원 · merge gate 210 FULLY UNBLOCKED

> `BENCHMARK_REPORT.md` §87~88 · `COMPETITOR_MATRIX.md` §87~88 · `memory/decisions.md` BNK-84~86 참조. ogada `@53e4016`/`@55fae99` 실측.

| # | 항목 | 권장 조치 (planner 반영) |
|---|------|------------------------|
| 1 | **★ 7-9 환불 lifecycle FE+BE ✅** | BNK-84 BE `de49b21` V71 → BNK-85 FE `212e010`/`b92a1d4` `RefundRecordModal`+refunds Route — **7-x 10/11**(7-5 ❌ 별개) · benchmark→coder **3단계 폐루프** |
| 2 | **★ G17 BE ✅ · FE 잔여 P1** | `73e169a` V72·`FUNCTIONAL_RECOVERY` program_type — silverangel 지표27 verbatim · FE `/programs/functional-recovery/*` 미구현 |
| 3 | **★ G32 BE ✅ · FE 잔여 P1** | `55fae99` V73·`CaseManagementController` — 지표43 6필드·분기 UNIQUE·30일 윈도우 · FE Route·폼·dashboard widget 미구현 |
| 4 | **★ US-G04 upload guard ✅** | `53e4016` year coverage normalize — QA-B37 lineage 완료 · 이지케어 사후 안내 ↔ ogada **import 전 차단** |
| 5 | **★ 통합재가 「주야간 월 10만원」** | longterm npeb610 md5 `0ea575be` verbatim ↔ MOHW 247 `100,000` — v2+ Epic V mutually exclusive 가드 |
| 6 | **#44 6차 0건** | MOHW 247·law byl18·longterm 2026 3원천 — BNK-25 placeholder 유지·하드코딩 금지 |
| 7 | **merge gate 210** | FE **116** ahead · WT **CLEAN** · BE **94** ahead · WT **CLEAN** → ★ **FULLY UNBLOCKED** · **616/616·569/569 PASS** |
| 8 | **잔여 P1** | tester merge(210) · G32 FE · G17 FE · US-L01 live · G24/G30 Epic · v1.3 live E2E |

---

### [BNK] BNK-84 인사이트 (2026-06-11) — ★ BE 7-9 환불 lifecycle BE 닫힘(BNK-82 P2 마감·benchmark→coder 폐루프) · silverangel 4지표 verbatim 4차 · 통합재가 「주야간 월 10만원」 verbatim 신규 추출 · #44 6차 0건 · merge gate 204 FE WT

> `BENCHMARK_REPORT.md` §87 · `COMPETITOR_MATRIX.md` §87 · `memory/decisions.md` BNK-84 참조. ogada `@c30aaac`/`@de49b21` 실측.

| # | 항목 | 권장 조치 (planner 반영) |
|---|------|------------------------|
| 1 | **★ BE 7-9 환불 lifecycle BE ✅** | `de49b21` `feat(v2/US-M03): add copay refund API and refunds ledger report (7-9)` — 커밋 메시지·V71 SQL 헤더 모두 「**(BNK-82)**」 명시·`POST /billing/claims/{id}/refunds`·`GET /billing/reports/refunds`(4번째 variant)·V71 REFUNDED+무결성 5층(`chk_billing_claims_refunded_requires_metadata`·전진 전용 트리거·partial 인덱스·멀티테넌트 FK)·`BillingServiceTest`+150·routing/RBAC+86 ↔ 케어포 「**7-9.본인부담금 수납,환불내역**」 BE 1:1 패리티 → **BNK-82 §85-2 P2 7-x 마감(benchmark→coder 폐루프 BNK-79→81→82→84 4사이클 연속)** |
| 2 | **★ FE Route `/billing/reports/refunds` 잔여 (P2)** | `rg refund\|환불 src/frontend/src` = 0건 → coder P2: `BillingRefundReportPage` + `RefundRecordModal` + `recordCopayRefundApi`. `competitorModuleCoverage.js` id `7-9` 등록 검토(BE만→0.5·FE 완성 후 1.0). 7-x 패리티: BE 11/11(7-5 ❌ 별개)·FE 10/11 (refunds Route 잔여) |
| 3 | **★ silverangel 4지표 verbatim 4차 재확인 (md5 `c79c1be3` 완전 불변)** | [daycareEssentialWork](https://www.silverangel.kr/newSilverangel/daycare/daycareEssentialWork.do) HTTP **200·131,664B** — ① 지표27 「**개인별 기능회복훈련 계획 — 주야간보호 27 기능회복훈련**」 (G17 P1 Epic) ② 지표41 「**계약서에 이동서비스수칙 포함**」+「**일지-수칙 예시**」 (G15 v1.3-C P2) ③ 지표42 「**1. 운전자 외 동승 2. 시간을 준수**」 (G15 ✅·`eef07e5` 닫힘) ④ 지표43 6필수 필드·**2인 이상**·**30일 가드** (G32 P2 신규) |
| 4 | **★ G32 P2 사례관리 회의록 권장 스펙 (지표43 verbatim 강화)** | ① 6필수 필드 폼: 일자·수급자명·선정사유·회의내용·회의결과·참석자명 ② 분기별 unique partial index (`organization_id, branch_id, year, quarter`) ③ **참석자 ≥2명 가드**(직종 무관) ④ **30일 이내 급여반영 가드**(회의일+30d 안 `/programs`/`/billing` 변경 1건 이상·dashboard widget) — G24/G30과 묶음 Epic |
| 5 | **★ 통합재가 「주야간보호형 월 10만원」 공단 verbatim 신규 추출** | [npeb610](https://www.longtermcare.or.kr/npbs/e/b/610/npeb610m01.web?menuId=npe0000002731) md5 `0ea575be`(BNK-69 동일·BNK-80 `8d53dcc1` 역드리프트) — 「**주·야간보호형: 수급자 1인당 월 10만원 지급**」+「**가정방문형: 월 한도액의 110%·방문간호 월2회·방문요양 월4회·80% 충족 필수**」 ↔ MOHW 247 PDF 「**제55조의2 100,000원**」(grep 100,000=3·제55조의2=10) **양립 1:1** → v2+ Epic V (단일 기관기호 통합재가)·G19 라벨에 「월 10만원」 표기·`billing_addons` mutually exclusive 가드(`INTEGRATED_HOME_10PCT` vs `DAYCARE_INTEGRATED_100K`) |
| 6 | **#44 이동서비스비 러-1~4 6차 교차 0건** | MOHW 247 PDF `cbc172d8`(833,389B·55p·29,717 chars) + law byl18 `b72abb43`(불변) + longterm 2026 `b5aee8c1`(BNK-78 동일·BNK-80 `72148cfe` 역드리프트) **3원천 「러-1~4/이동서비스/원거리/830/2,630/4,430/6,230 전부 0건」** → BNK-25 placeholder 6차 0건 재확정·하드코딩 절대 금지 |
| 7 | **★ 효성CMS 「월 30,000원·1600-6859·자동이체 250원·가상계좌 300원」 verbatim 불변** | [silverangel extraService](https://www.silverangel.kr/newSilverangel/service/extraService.do) md5 `f9c5d877`(BNK-54·76 완전 동일) — ogada v2 FCMS 라벨 패리티 체크리스트 6차 유지 |
| 8 | **merge gate 204** | FE **113** ahead · WT **dirty 1M** (`MonthlyBenefitCapBanner.test.jsx`·BNK-81 §84-3 1F 플레이키 안정화 WIP·`findByText("월한도 90% 이상 사용")` + `queryByText("월한도 확인 중") not present`) · BE **91** ahead · WT **CLEAN** → **즉시(coder)**: FE 1M 커밋·push → **즉시(tester)**: merge **204** |
| 9 | **잔여 P1** | merge(204) · **FE refunds Route** (coder P2) · US-L01 live · G17 Epic(지표25~27) · G24/G30 Epic · **G32 P2 사례관리** · v1.3 live E2E · G26 xlsx E2E |

---

### [BNK] BNK-78~81 인사이트 (2026-06-11) — ★ 모듈 76.67% · US-G04 연도 수가 가드 · G26 NTS xlsx · G21 dup slot · merge gate 198 FE BLOCK

> `BENCHMARK_REPORT.md` §81~84 · `COMPETITOR_MATRIX.md` §81~84 · `memory/decisions.md` BNK-78~81 참조. ogada `@5c0d83d`/`@970c7af` 실측.

| # | 항목 | 권장 조치 (planner 반영) |
|---|------|------------------------|
| 1 | **★ 모듈 76.67%** | id `7-2-1` 등록 @ `c1d9788` lineage · sum 20.70 · ≥60% PASS (BNK-78) |
| 2 | **★ US-G04 연도 수가 가드 UX partial ✅** | `FeeScheduleYearGuardBanner` @ `5c0d83d` — 이지케어 사후 안내 ↔ ogada **import 전 사전 차단** 차별 (BNK-79 P2) |
| 3 | **★ BE fee schedule year guard ✅** | `FeeScheduleYearCoverage`·`NhisImportService` @ `970c7af` — NHIS import 연도 등급×시간대 그리드 불완전 시 거부 (BNK-81) |
| 4 | **★ FE upload guard WIP** | `NHISImportPage` `feeScheduleYearCoverage()` — **QA-B37 Planned** · FE-BE 패리티 미커밋 = merge BLOCK |
| 5 | **★ G26 NTS xlsx partial ✅** | `medicalExpenseDeduction.js` NTS 레이아웃 @ `fd569d7` — 국세청 제출 E2E **P2 잔여** (BNK-79) |
| 6 | **★ G21 dup paired slot ✅** | `VisitService` create/update/import 중복 거부 @ `0ae5f8d`/`ff12473` (BNK-79·80) |
| 7 | **★ US-L01 8은행 포맷 ✅** | `bankDepositFormats`·케어포 8은행 엑셀 가이드+E2E @ `758e590` (BNK-80) |
| 8 | **★ 통합재가 2종 조합** | 롱텀 「① 방문간호+방문요양 ② 주·야간+방문요양」verbatim → **v2+ Epic V** (BNK-80) |
| 9 | **#44·지표41** | 5차 6원천 0건·**수동 보류** · 하드코딩 금지 — BNK-80 **번복 0건** |
| 10 | **merge gate 198** | FE **110** ahead · WT **DIRTY 2M** · BE **88** ahead · WT **CLEAN** → **FE BLOCK** · **601/601·532/532 PASS** @ HEAD |

---

### [PLA] QA 피드백 반영 (2026-06-11, 102차 — BNK-78~81 · TSR 307~308 · QA-B37 Planned)

> **102차 자동 기획 동기화** — BNK-78~81(US-G04·G26 xlsx·G21·US-L01)·TSR 307~308. **QA Open 0건** · **QA-B37 Open→Planned** — FE `NHISImportPage*` upload guard WIP.

| 항목 | 102차 관측 | 조치 |
|------|----------|------|
| **baseline** | FE **`5c0d83d`** · BE **`970c7af`** · **110+88 ahead** · **FE WT DIRTY 2M** · **52 route·74 page** · **601/601·532/532 PASS** | ROADMAP CURRENT BASELINE **102차** 갱신 |
| **BNK-78~81** | **모듈 76.67%** · **US-G04 partial** · **G26 xlsx partial** · **G21 dup slot ✅** · **US-L01 8-bank ✅** · **#44 수동 보류** | REQUIREMENTS·USER_STORIES US-G04·G26·G21 갱신 |
| **QA** | Open **0건** · **QA-B37 Planned** @ PLN 102차 | QA_FEEDBACK Open→Planned 이동 |
| **merge gate** | P0 `[x]` · BE **ready** · FE **BLOCK**(WT clean 선행) · **198 commits** | COD FE WT clean → tester merge **198** |
| **잔여 P1** | merge(198) · QA-B37 upload guard · G7 실파일 · G2 SMTP · US-L01 live · G17/G24/G30/G32 Epic · v1.3 live E2E · G26 xlsx E2E | ROADMAP v1.2.1·v2 우선순위 갱신 |

**coder 다음 액션 (102차)**: ① **QA-B37 `NHISImportPage*` 2M 커밋→push** ② **tester merge(110+88=198)** ③ G7 **실파일**(#27) ④ G2 **SMTP** ⑤ US-L01 **은행 8종 E2E live** ⑥ **G17 Epic** ⑦ **G24/G30/G32 Epic** ⑧ v1.3 live E2E ⑨ **G26 xlsx E2E P2**.

---

### [BNK] BNK-74~77 인사이트 (2026-06-11) — ★ G26 7-2-1 FE+BE E2E 닫힘 · CMS/easy-pay 제외 패리티 · G17·G32 Epic 후보 · merge gate 187

> `BENCHMARK_REPORT.md` §77~80 · `COMPETITOR_MATRIX.md` §77~80 · `memory/decisions.md` BNK-74~77 참조. ogada `@c1d9788`/`@1af5b1f` 실측.

| # | 항목 | 권장 조치 (planner 반영) |
|---|------|------------------------|
| 1 | **★ G26 7-2-1 FE+BE E2E ✅** | `MedicalExpenseDeductionPanel`(staff+guardian)·API·CSV export @ `7e5c806`/`7f10449` · **7-x 10/11** (BNK-75) |
| 2 | **★ CMS·간편결제 제외 = func.php leaf 분리** | BE `970f547`/`1af5b1f` · FE exclusion UI @ `c1d9788` — 7-2-1↔7-4/7-5 별개 leaf 정합 (BNK-77) |
| 3 | **★ US-L04 taxYear UX ✅** | submit-on-blur·stale-response guard @ `be1bdd0`/`13272bc` — QA-B34 Fixed |
| 4 | **★ copayAmount null 가드 ✅** | BE `1af5b1f` — QA-B35 Fixed · BNK-73 `paidAt` 계열 확장 |
| 5 | **★ G17 지표27 P1 Epic** | 「개인별 기능회복훈련 계획」— `/programs` CRUD만 → 지표25~27 묶음 (BNK-72/76 이월) |
| 6 | **★ G32 사례관리 회의록 P2** | 엔젤 지표43 verbatim — 6필드·분기 1회·30일 반영 가드 → G24/G30 묶음 Epic (BNK-76) |
| 7 | **law.go.kr 별표1** | 「방문요양·방문간호 원거리교통비」— 주야간 #44 별개·v2+ 별도 fee schedule (BNK-76) |
| 8 | **#44·지표41** | 4차 6원천 0건·**수동 보류** · 41 P2(계약서 수칙 PDF) — BNK-74 **번복 0건** |
| 9 | **merge gate 187** | FE **104** ahead · WT **CLEAN** · BE **83** ahead · WT **CLEAN** → ★ **FULLY UNBLOCKED** · **574/574·520/520 PASS** |
| 10 | **잔여 P1** | tester merge(187) · G7 실파일(#27) · G2 SMTP · US-L01 live · G17/G24/G30/G32 Epic · v1.3 live E2E · **G26 xlsx P3** |

---

### [PLA] QA 피드백 반영 (2026-06-11, 101차 — BNK-74~77 · TSR 295~296 · QA Open 0건)

> **101차 자동 기획 동기화** — BNK-74~77(G26·G17·G32)·TSR 295~296. **QA Open 0건** · **Open→Planned 이동 없음** — QA-B34/B35 **Fixed** @ `13272bc`/`be1bdd0`/`1af5b1f`.

| 항목 | 101차 관측 | 조치 |
|------|----------|------|
| **baseline** | FE **`c1d9788`** · BE **`1af5b1f`** · **104+83 ahead** · **양쪽 WT CLEAN** · **52 route·74 page** · **574/574·520/520 PASS** | ROADMAP CURRENT BASELINE **101차** 갱신 |
| **BNK-74~77** | **G26 7-2-1 ✅** · **CMS/easy-pay 제외 ✅** · **G17 P1 Epic** · **G32 P2 신규** · **#44 수동 보류** | REQUIREMENTS G26·G32·G17 · USER_STORIES US-L04 |
| **QA** | Open **0건** · B34/B35 **Fixed** · Planned **0건** | QA_FEEDBACK 갱신 · 이동 없음 |
| **merge gate** | P0 `[x]` · BE+FE **ready** · ★ **FULLY UNBLOCKED** · **187 commits** | tester merge **187** 즉시 가능 |
| **잔여 P1** | merge(187) · G7 실파일 · G2 SMTP · US-L01 live · G17/G24/G30/G32 Epic · v1.3 live E2E · G26 xlsx P3 | ROADMAP v1.2.1·v2 우선순위 갱신 |

**coder 다음 액션 (101차)**: ① **tester merge(104+83=187)** ② G7 **실파일**(#27) ③ G2 **SMTP** ④ US-L01 **은행 8종 E2E live** ⑤ **G17 Epic** ⑥ **G24/G30/G32 Epic** ⑦ v1.3 live E2E ⑧ G15 **P2** ⑨ **G26 xlsx P3**.

---

### [BNK] BNK-73 인사이트 (2026-06-11) — ★ G2/v2 `paidAt` 필수 = 케어포 7-2 패리티 · US-J02 GuardianPortal 닫힘 · G26 7-2-1 P2 · merge gate 176

> `BENCHMARK_REPORT.md` §76 · `COMPETITOR_MATRIX.md` §76 · `memory/decisions.md` BNK-73 참조. ogada `@0024c88`/`@ed730a2` 실측.

| # | 항목 | 권장 조치 (planner 반영) |
|---|------|------------------------|
| 1 | **★ G2/v2 `paidAt` 입금일 필수 ✅** | BE `BillingService` — null→「입금일을 입력해주세요」·미래일 차단 @ `ed730a2` · FE `PaymentRecordModal`/`BillingDetailPage` @ `0024c88` · `J03AlimtalkServiceFlowE2eTest` fixture @ `ed730a2` — **케어포 7-2 PDF 패리티** (QA-B31/B33 Fixed). |
| 2 | **★ US-J02 GuardianPortal 닫힘 ✅** | out-of-order `loadTargets` guard @ `62058d3` · stale billing error clear @ `189a00d` · **WT CLEAN** (QA-B32 Fixed). |
| 3 | **★ G26 7-2-1 연말정산 P2** | 케어포 func.php 7-2-1 의료비공제 — ogada `의료비공제`/`연말정산` **0건** → 보호자 포털 **납입증명 자동 산출** P2 (`납부확인서` 기반 확장). **G26 레지스트리**: BNK-44 「치매전담실」 할당 **P3 보류로 이관**(ID 충돌 해소). |
| 4 | **★ G17 지표27 P1 Epic 후보** | 엔젤 「**개인별 기능회복훈련 계획**」verbatim — ogada `/programs` 일정·참여 CRUD만 → **지표25~27 묶음 Epic** (BNK-72 이월·강화). |
| 5 | **#44·지표41·42** | 3차 6원천 0건·**수동 보류** · 42✅ · 41 P2(계약서 수칙 PDF) — BNK-72 **번복 0건**. |
| 6 | **merge gate 176** | FE **98** ahead · WT **CLEAN** · BE **78** ahead · WT **CLEAN** → ★ **FULLY UNBLOCKED** · **558/558·510/510 PASS**. |
| 7 | **잔여 P1** | tester merge(176) · G7 실파일(#27) · G2 SMTP · US-L01 live · G30 Epic · v1.3 live E2E · **G17 Epic**. |

---

### [BNK] BNK-72 인사이트 (2026-06-11) — ★ 엔젤 지표41/42/27 전수 · #44 3차 6원천 0건 · law.go.kr 재실측 성공 · merge gate 171

> `BENCHMARK_REPORT.md` §75 · `COMPETITOR_MATRIX.md` §75 · `memory/decisions.md` BNK-72 참조. ogada `@bed612c`/`@894e246` 실측.

| # | 항목 | 권장 조치 (planner 반영) |
|---|------|------------------------|
| 1 | **★ 엔젤 지표41 P2** | [daycareEssentialWork](https://www.silverangel.kr/newSilverangel/daycare/daycareEssentialWork.do) md5 `c79c1be` — 「**계약서에 이동서비스수칙 포함**」·「**일지—수칙 예시**」 → ogada **42✅** · **41 P2**: 계약서 수칙 PDF 첨부·평가 제출용 예시 파일 → ROADMAP v1.3-C 잔여. |
| 2 | **★ G17 지표27 갭** | 「**개인별 기능회복훈련 계획**」verbatim — ogada `/programs` CRUD만 → **G17 Epic P1 후보**(지표25~27 묶음·이지케어 인지활동북 별축). |
| 3 | **#44 3차 0건** | MOHW247·angelsitter PDF·longterm·**★ MOHW 시행규칙 HWP**·law.go.kr **러-1~4 단가 0건** → **BNK-25 유지·하드코딩 금지** · 수동 보류. |
| 4 | **★ law.go.kr SSL 해소** | byl18 UA fetch HTTP **200** `b72abb43` — 「별표 1·2·별지 1」만·별표18 미존재 재확인. |
| 5 | **merge gate 171** | FE **95** ahead · WT **dirty 2** · BE **76** ahead · WT **dirty 2** → tester merge **커밋 후**(npm 554·mvn 509 GREEN). |
| 6 | **잔여 P1** | US-L01 live · **G24 Epic** · G7 실파일(#27) · G2 SMTP · v1.3 live E2E. |

---

### [BNK] BNK-69 인사이트 (2026-06-11) — ★ G19 롱텀 통합재가 정본 · 엔젤 지표41/42 · #44 2차 거리 단가 수동 보류 · merge gate 168

> `BENCHMARK_REPORT.md` §72 · `COMPETITOR_MATRIX.md` §72 · `memory/decisions.md` BNK-69 참조. ogada `@fcf713a`/`@64ebf6e` 실측.

| # | 항목 | 권장 조치 (planner 반영) |
|---|------|------------------------|
| 1 | **★ G19 롱텀 통합재가 정본** | [통합재가서비스 안내](https://www.longtermcare.or.kr/npbs/e/b/610/npeb610m01.web?menuId=npe0000002731) md5 `0ea575be` — 「하나의 기관기호·2종+ 급여·가정방문형 월한도 110%」 → REQUIREMENTS G19·BranchesPage surcharge notice 정합 재확인. |
| 2 | **★ 엔젤 지표41/42** | 지표41 5수칙(계약서 수칙 첨부) · 지표42 동승·시간준수 — ogada **42✅** @ `eef07e5` · **41 P2**(계약서 첨부·평가 자료) → ROADMAP v1.3-C 잔여. |
| 3 | **#44 2차 교차 거리 단가 0건** | MOHW·공단 매뉴얼·longterm 2026 **러-1~4 단가 미추출** → **BNK-25 830/2,630/4,430/6,230 유지·하드코딩 금지** · 수동 보류 유지. |
| 4 | **★ G15 공단 3분리 UI ✅** | `TransportForm18GuidePanel` form 18/19/20 three-way @ `fcf713a` — BNK-65 P2 **닫힘**. **잔여 P2**: 변경 7일 가드 BE validation. |
| 5 | **잔여 P1** | tester merge(**168**) · G7 **실파일**(#27) · G2 **SMTP** · US-L01 **은행 8종 live** · **G30 Epic**(주기별 업무·모니터링) · v1.3 live E2E. |
| 6 | **merge gate 168** | FE **93** ahead · WT **CLEAN** · BE **75** ahead · WT **CLEAN** → ★ **FULLY UNBLOCKED** · **모듈 75.77%**. |

---

### [BNK] BNK-68 인사이트 (2026-06-10) — ★ G31 공단 인증서 자동 연동(Won't v1) · 이지케어 Channel.io · 운영 3단계 · RFID 30분

> `BENCHMARK_REPORT.md` §71 · `COMPETITOR_MATRIX.md` §71 · `memory/decisions.md` BNK-68 참조. 벤치마크 초안 **G25** = 공단 인증서 연동 → 기획 레지스트리 **G31** 확정(**G25** = 본인부담률 엑셀 BNK-35와 충돌 방지).

| # | 항목 | 권장 조치 (planner 반영) |
|---|------|------------------------|
| 1 | **★ G31 공단 인증서 자동 일정 연동** | 이지케어 Channel.io **범용 기관 인증서·계획/청구 2트랙·확정 제외 전체 초기화** — ogada **Won't v1**(엑셀 import=업계 표준 BNK-20) · **P2**: 온보딩 「공단 포털→엑셀→ogada」3단 가이드. |
| 2 | **이지케어 운영 3단계** | STEP01 일정확정→02 본인부담→03 급여명세서 — ogada v1 **STEP01~02만** · STEP03 payroll **Won't v1**. |
| 3 | **RFID 30분 검출** | 태그↔계획 30분↑·급여제공자 불일치 3종 — RFID live **2016.03.28 종료** 불변 → ogada QR v1 유지. |
| 4 | **P0/P1 재정렬** | **즉시**: tester merge **168** · **P1**: US-L01 live · **G30 Epic** · **P2**: G31 온보딩 · 3-1-1~3-1-4 leaf. |

---

### [PLA] QA 피드백 반영 (2026-06-11, 100차 — BNK-72~73 · TSR 283~284 · QA Open 0건)

> **100차 자동 기획 동기화** — BNK-72~73(`paidAt`·US-J02·G17·G26)·TSR 283~284. **QA Open 0건** · **Open→Planned 이동 없음** — QA-B31/B32/B33 **Fixed** @ `4001510`/`62058d3`/`ed730a2`/`0024c88`.

| 항목 | 100차 관측 | 조치 |
|------|----------|------|
| **baseline** | FE **`0024c88`** · BE **`ed730a2`** · **98+78 ahead** · **양쪽 WT CLEAN** · **52 route·74 page** · **558/558·510/510 PASS** | ROADMAP CURRENT BASELINE **100차** 갱신 |
| **BNK-72~73** | **`paidAt` 필수 ✅** · **US-J02 race·stale error ✅** · **G17 P1 Epic** · **G26 7-2-1 P2** · **#44 수동 보류** | REQUIREMENTS G13·G17·G26 · USER_STORIES US-J02·US-L01·US-T06 |
| **QA** | Open **0건** · B31/B32/B33 **Fixed** · Planned **0건** | QA_FEEDBACK 갱신 · 이동 없음 |
| **merge gate** | P0 `[x]` · BE+FE **ready** · ★ **FULLY UNBLOCKED** · **176 commits** | tester merge **176** 즉시 가능 |
| **잔여 P1** | merge(176) · G7 실파일 · G2 SMTP · US-L01 live · G30 Epic · v1.3 live E2E · G17 Epic | ROADMAP v1.2.1·v2 우선순위 갱신 |

**coder 다음 액션 (100차)**: ① **tester merge(98+78=176)** ② G7 **실파일**(#27) ③ G2 **SMTP** ④ US-L01 **은행 8종 E2E live** ⑤ **G30 Epic** ⑥ v1.3 live E2E ⑦ **G17 Epic**(지표25~27) ⑧ G15 **P2** ⑨ **G26 P2**(7-2-1).

---

### [PLA] QA 피드백 반영 (2026-06-11, 99차 — BNK-68~69 · TSR 271~272 · QA Open 0건)

> **99차 자동 기획 동기화** — BNK-68~69(G15 v1.3-C 대부분·G7 guidance·G19·G31)·TSR 271~272. **QA Open 0건** · **Open→Planned 이동 없음** — QA-B24/B26/B27/B28 **Fixed** @ `1220bfb`/`2b6024a`/`b5218a9`/`0abf164`.

| 항목 | 99차 관측 | 조치 |
|------|----------|------|
| **baseline** | FE **`fcf713a`** · BE **`64ebf6e`** · **93+75 ahead** · **양쪽 WT CLEAN** · **52 route·74 page** · **547/547·505 PASS** | ROADMAP CURRENT BASELINE **99차** 갱신 |
| **BNK-68~69** | **G15 2-1-1/2-9 ✅** · **TSF E2E ✅** · **공단 3분리 UI ✅** · **G7 live guidance ✅** · **G19 롱텀 정본** · **G31 신규** | REQUIREMENTS G7·G15·G16·G19·G31 · USER_STORIES US-T05 |
| **QA** | Open **0건** · B24/B26/B27/B28 **Fixed** · Planned **0건** | QA_FEEDBACK Planned 섹션 갱신 · 이동 없음 |
| **merge gate** | P0 `[x]` · BE+FE **ready** · ★ **FULLY UNBLOCKED** · **168 commits** | tester merge **168** 즉시 가능 |
| **잔여 P1** | merge(168) · G7 실파일 · G2 SMTP · US-L01 live · G30 Epic · v1.3 live E2E | ROADMAP v1.3-C·v1.2.1 우선순위 갱신 |

**coder 다음 액션 (99차)**: ① **tester merge(93+75=168)** ② G7 **실파일**(#27) ③ G2 **SMTP** ④ US-L01 **은행 8종 E2E live** ⑤ **G30 Epic** ⑥ v1.3 live E2E ⑦ G15 **P2**(계약서 수칙 첨부·3-1-1~4 leaf).

---

### [BNK] BNK-66 인사이트 (2026-06-11) — ★★ G16 FE 닫힘 · ★ G15 3-1 급여제공↔이동서비스 연계 · TSF npm 534/534 GREEN · merge gate 158 · FE WT BLOCK

> `BENCHMARK_REPORT.md` §69 · `COMPETITOR_MATRIX.md` §69 · `memory/decisions.md` BNK-66 참조. ogada `@08dbcf0`/`@dd7a580` 실측.

| # | 항목 | 권장 조치 (planner 반영) |
|---|------|------------------------|
| 1 | **★★ G16 FE 닫힘** | `VehiclesPage` `/transport/vehicles`·`TransportVehicleSelect` @ `107bfb3`/`08dbcf0` — 케어포 2-4 차량 마스터 패리티. **잔여**: 이동서비스비 청구·`transport_service_fee` 테이블. |
| 2 | **★ G15 3-1 연계 ✅** | `CareProvisionRecordPanel`+BE `CareProvisionRecordService` @ `8bdead6`/`08dbcf0` — 케어포 3-1 부분 패리티(확정 배차·출석 3원 대조). **잔여**: 3-1-1~3-1-4 하위 leaf P2. |
| 3 | **★ TSF npm 534/534 GREEN** | BNK-64/65 TransportServiceFee FE 2F **해소**. WT **535/535 PASS**(+1 test, QA-B24 WIP). |
| 4 | **#44 1차 정본 번복 0건** | BNK-65 angelsitter PDF md5 `3f92619c` 재확인. **거리 단가(러-1~4) 수동 보류** 유지. |
| 5 | **신규 P2 — 공단 3분리 워크플로 UI** | 적용/변경/중단 신청 + 등록상태 4단 + 변경 7일 가드 — BNK-65 권고 이월. |
| 6 | **잔여 P1** | **COD FE WT clean**(QA-B24) → tester merge(**158**) · G15 **2-1-1/2-9** · **이동서비스비 청구** · G7 **실파일**(#27) · US-L01 **은행 8종 live** · **G24** Epic. |
| 7 | **merge gate 158** | FE **88** ahead · WT **DIRTY 4M** → **BLOCK** · BE **70** ahead · WT **CLEAN** → **ready** · **모듈 75.77%**. |

---

### [PLA] QA 피드백 반영 (2026-06-11, 98차 — BNK-65~66 · TSR 260~261 · QA Open→Planned 1건)

> **98차 자동 기획 동기화** — BNK-65~66(G16 FE·G15 3-1·#44 1차 정본)·TSR 260~261. **QA-20260610-B24 Open→Planned**.

| 항목 | 98차 관측 | 조치 |
|------|----------|------|
| **baseline** | FE **`08dbcf0`** · BE **`dd7a580`** · **88+70 ahead** · **FE WT DIRTY 4M** · **BE WT CLEAN** · **53 route·74 page** · **534/535·497 PASS** | ROADMAP CURRENT BASELINE **98차** 갱신 |
| **BNK-65~66** | **G16 FE ✅** · **G15 3-1 ✅** · **#44 1차 정본 ✅** · **모듈 75.77%** · **TSF GREEN** | REQUIREMENTS G15·G16·G7 · USER_STORIES US-T05·US-G06 |
| **QA-B24** | G7 NHIS import live guidance WIP 4M · B07 #13 recurrence | **Open→Planned** · ROADMAP FE merge BLOCK · coder **커밋 or revert** |
| **merge gate** | P0 `[x]` · BE **ready** · FE **BLOCK** · **158 commits** | tester merge **BE 선행 가능·FE WT clean 후** |
| **잔여 P1** | FE WT clean · G15 2-1-1/2-9 · 이동서비스비 · G7 실파일 · US-L01 live E2E · G24 | ROADMAP v1.3-C·v1.2.1 우선순위 갱신 |

**coder 다음 액션 (98차)**: ① **FE WT clean**(QA-B24: `feat(G7): NHIS import live guidance API wiring` or revert) ② **tester merge(88+70=158)** ③ G15 **2-1-1/2-9·이동서비스비** ④ G7 **실파일**(#27) ⑤ G2 **SMTP** ⑥ US-L01 **은행 8종 E2E live** ⑦ **G24** Epic ⑧ v1.3 live E2E.

---

### [BNK] BNK-65 인사이트 (2026-06-10) — ★★★ #44 「공단 공식 사용자 매뉴얼」 1차 정본 PDF 추출 성공 — 5년 추적 종료(거리 단가 제외) · ★ TSF FE 커밋 닫힘 · merge gate 153

> `BENCHMARK_REPORT.md` §68 · `COMPETITOR_MATRIX.md` §68 · `memory/decisions.md` BNK-65 참조. 로테이션: 엔젤·롱텀·규제 4–6h. ogada `@2b45709`/`@bd375e6` 실측.

| # | 항목 | 권장 조치 (planner 반영) |
|---|------|------------------------|
| 1 | **★★★ #44 「공단 공식 사용자 매뉴얼」 1차 정본 PDF 확보** | [angelsitter no=235→PDF 직접 다운로드](https://angelsitter.co.kr/uploads/files/%EC%A3%BC%EC%95%BC%EA%B0%84%EB%B3%B4%ED%98%B8_%EC%9D%B4%EB%8F%99%EC%84%9C%EB%B9%84%EC%8A%A4%EB%B9%84%EC%9A%A9_%EC%82%AC%EC%9A%A9%EC%9E%90_%EB%A7%A4%EB%89%B4%EC%96%BC.pdf) HTTP **200·1,369,661B**·md5 **`3f92619c`**·PDF v1.4·**10p**·pypdf **3,505 chars** 전수 추출 · 「2021. 2.」발행·「**출처: 노인장기요양보험**」 verbatim → 공단 공식 1차 정본 확정. **4중 verbatim**: ①시행규칙 제32조·고시 제34조·세부사항 제8조 ②실거주지↔기관 양방향 ③**최단거리(도로거리·편도)·수급자별 1일 1회·일지 작성/보관** ④적용/변경/중단·**변경 7일 신고**·등록상태 4단(작성중→진행중→적용/적용불가). **거리별 단가(러-1~4)는 본 PDF 미수록**(절차 매뉴얼 한정) → 공단 수가표 별도 추적·**BNK-25 단가 유지·하드코딩 금지**. BNK-9~62 추적 사이클 종료(거리 단가 제외). |
| 2 | **★ ogada G15 v1.3-C 3중 정확 패리티 확정** | (1) 공단 매뉴얼 「**'존재하지 않는 주소입니다' 알림**」(p.5) ↔ ogada FE `318411d` `countGeocodeFailures`/Alert/disabled (BNK-59 QA-B19) — **1:1 + α 접근성** · (2) 공단 「**수급자별 1일 1회 산정**」(p.3) ↔ BE `88d4c59` `TransportServiceFeeService.ONE_PER_DAY_NOTE` (BNK-64) — **1:1** · (3) 공단 「이동서비스 일지 작성 보관」 ↔ FE `7389884` `TransportServiceLogPanel`/서식22 export (BNK-61) — **1:1 + 동작 산출물 차별**. |
| 3 | **★ TSF FE 커밋 닫힘 (BNK-64 P1)** | FE `9dfef92` `Wire transport service fee page into routing and formatting` — `/transport/service-fees`·`TransportServiceFeePanel`(+356줄)·`services.js`·`transportServiceFee.js`·테스트 3종 +665줄 · **잔여**: npm 2F(러-1 라벨·홍길동 렌더)·FE E2E. |
| 4 | **신규 P2 — 공단 매뉴얼 3분리 워크플로 UI 라벨 매핑** | TransportServiceFee 라이프사이클 정밀화: 「적용신청 / 변경신청 / 중단신청」 메뉴 + 등록상태 4단(`작성중→진행중→적용/적용불가`) 라벨 + **변경 7일 가드**(사유 발생 후 7일 초과 시 소급 적용 불가 → UI 경고·BE validation). coder 비블로커. |
| 5 | **공단 vs 협회 용어 분리** | 공단 매뉴얼: 「적용신청서/변경신청서/중단신청서」(서식 번호 미사용) · 협회 PDF(BNK-62): 「별지 제18호/19호/20호/22호」 — 같은 워크플로 두 표기. ogada `TransportForm18GuidePanel`(BNK-61 `eecf0be`)는 **「적용신청(별지 제18호서식)」 병기 권장** — BNK-62 권고 유지. |
| 6 | **엔젤·롱텀·규제 정적 재실측 — md5 전부 불변** | silverangel `c950719`·daycareEssentialWork `c79c1be`·extraService `f9c5d877`·lcms `57ec33be`/`9283f031`·longtermcare 2026 `b5aee8c1` · law.go.kr admRulBylInfoR bylNo=18 정적 HTML 「별표 1·별표 2·별지 1」만 — 별지 18~22는 JS 렌더(BNK-44/47 패턴 일관). 본 사이클 가정 번복 0건. |
| 7 | **잔여 P1** | TransportServiceFee FE **E2E**(npm 2F 해소) · US-L01 은행 8종 live · **G24** 모니터링 15문항 Epic · BE BillingService WIP 커밋. |
| 8 | **수동 보류** | #44 **거리별 실액(러-1~4·830·2,630·4,430·6,230)** = **공단 「2026 장기요양 급여비용 산정방법 안내」 PDF** 또는 longtermcare 부속 자료 별도 추적 — 차기 「엔젤·롱텀·규제」 사이클(BNK-66 대상). |
| 9 | **merge gate 153** | tester develop→test **FE86+BE67=153** · FE WT CLEAN · BE WT dirty 2(BillingService WIP) — BE 커밋 후 mvn GREEN 재검증 권장. **모듈 75.77%**(id `2` 0.75 → 0.9 권고 coder 이월). |

---

### [BNK] BNK-62 인사이트 (2026-06-10) — ★★ #44 「이동서비스비용 = 별지 제18호서식」 1차 확인 · ★ 엔젤 지표42(동승·시간준수) 정확 패리티 · 모듈 75.38%

> `BENCHMARK_REPORT.md` §65 · `COMPETITOR_MATRIX.md` §65 · `memory/decisions.md` BNK-62 참조. 로테이션: 엔젤·롱텀·규제 4–6h. ogada `@eef07e5`/`@9d7c17f` 실측.

| # | 항목 | 권장 조치 (planner 반영) |
|---|------|------------------------|
| 1 | **★★ #44 「별지 제18호서식」 1차 확인** | [협회 세부운영규정 제8조](https://carefor.co.kr/ct_att/contents_article/0/202507/45798/D3OeRGtj1h.pdf) verbatim — 이동서비스비용 **적용신청=별지 제18호**·**변경/중단=제19호**·**공단통보=제20호**·**운행일지=제22호**·**수급자별 1일 1회 산정** · BNK-44 「(고시) **별표** 18 미존재」와 **양립**(별표≠별지) → #44 **「수동 보류」→「1차 확인」 격상**. 거리별 실액(러-1~4) 본문 미추출 → **BNK-25 단가 유지·하드코딩 금지**. |
| 2 | **★ 시간준수·동승 기록 ✅(지표42 정확 패리티)** | FE `transportTimeCompliance.js` @ `eef07e5`(15분 tolerance·준수/지연/미기록·동승/미동승) ↔ 엔젤 daycareEssentialWork **지표42**(md5 `c79c1be`) 「1.운전자 외 직원 동승 2.시간을 준수」 1:1 — BNK-54~60 P1 **닫힘**. |
| 3 | **★ 별지18 안내 + 모듈 0.6→0.75** | FE `transportForm18.js`·`TransportForm18GuidePanel` @ `eecf0be` · `competitorModuleCoverage.js` id `2` 이동서비스 0.6→0.75 → **모듈 75.38%**(BNK-60 P2 닫힘). **정밀화(비블로커)**: step1 「적용·변경·중단 제18호」→ 적용=제18호/변경·중단=제19호/통보=제20호 분리. |
| 4 | **★ G21 visits paired sync ✅** | BE `9d7c17f` — BNK-61 visits WIP 커밋 확정(양쪽 WT CLEAN). |
| 5 | **2026 수가표 5×6 재확인** | longtermcare md5 `b5aee8c1` verbatim — 76,820(10~13h 1등급)·인지 cap 56,360 → `feeSchedules.js` 일치 불변. silverangel/lcms md5 전부 불변. |
| 6 | **잔여 P1** | G15 2-1-1/2-9 외출 lifecycle · **이동서비스비 청구(별지18 신청 후·1일1회 가드)** · US-L01 은행 8종 live · #44 거리 실액 수동. |
| 7 | **merge 144** | tester develop→test **81+63=144** · 양쪽 WT CLEAN · 모듈 **75.38%**. |

---

### [BNK] BNK-59~61 인사이트 (2026-06-11) — ★ G15 v1.3-C 진전 · G29·G30 신규 갭 · demo-work 송영 0건

> `BENCHMARK_REPORT.md` §62~64 · `COMPETITOR_MATRIX.md` §59~61 · `memory/decisions.md` BNK-59~61 참조.

| # | 항목 | 권장 조치 (planner 반영) |
|---|------|------------------------|
| 1 | **★ QA-B19 geocode UX ✅** | FE `countGeocodeFailures`·Alert·저장/확정 차단 @ `318411d`/`695c0f7` — TSR 234 Fixed. |
| 2 | **★ V65 계약 무결성 ✅** | BE `transport_service_contracts_integrity.sql`·`TransportContractService` @ `24733c7` (BNK-59). |
| 3 | **★ 서식22 운행일지 export ✅** | `TransportServiceLogPanel`·`transportServiceLog.js` @ `7389884` — confirmed run stop → 인쇄/다운로드 (BNK-61). |
| 4 | **★ 제18호 가이드 ✅** | `TransportForm18GuidePanel`·`transportForm18.js` @ `eecf0be` (BNK-61). |
| 5 | **★ 시간 준수 기록 ✅** | `transportTimeCompliance.js` @ `eef07e5` — 엔젤 「시간을 준수함」 패리티 방향 (BNK-61). |
| 6 | **★ G21 paired schedule sync ✅** | BE `VisitService.syncPairedScheduleProgress()` @ `9d7c17f` — QA-B22 Fixed (TSR 245). |
| 7 | **신규 G29**(인지활동북) | 이지케어 FAQ 21781 시범 — `/programs` 자료 배포 없음 → **v3.1 P3** (BNK-59 · 벤치마크 초안 G23 라벨과 **ID 충돌** → 기획 레지스트리 **G29** 확정). |
| 8 | **신규 G30**(주기별 업무·모니터링) | 이지케어 FAQ 21782~21842 39+건 — 평가/모니터링 동반 도구 → **v3.1 P3** (BNK-61 · 벤치마크 초안 G24 라벨과 **ID 충돌** → **G30** 확정). |
| 9 | **demo-work 송영 0건** | 케어포 119 view-id 전수 — 차량/송영 view 0건 → ogada G15 폐루프 **영업 차별화 근거** (BNK-60). |
| 10 | **잔여 P1** | 2-1-1/2-9 외출 lifecycle · 이동서비스비 청구 · US-L01 은행 8종 live · #44 수동 보류. |
| 11 | **merge 144 · npm 508 · mvn 459** | tester develop→test **81+63=144** · 양쪽 WT CLEAN · 모듈 **74.81%**. |

---

### [PLA] QA 피드백 반영 (2026-06-11, 97차 — BNK-59~61 · TSR 245~246 · QA Open 0건)

> **97차 자동 기획 동기화** — BNK-59~61(G15 v1.3-C 진전·G29·G30)·TSR 245~246. **QA Open 0건** · **이동 없음** — QA-B19 **Fixed** @ `695c0f7` · QA-B22 **Fixed** @ `9d7c17f`.

| 항목 | 97차 관측 | 조치 |
|------|----------|------|
| **baseline** | FE **`eef07e5`** · BE **`9d7c17f`** · **81+63 ahead** · **양 스트림 WT CLEAN** · **49 route·67 page** · **508/133·459 PASS** | ROADMAP CURRENT BASELINE **97차** 갱신 |
| **BNK-59~61** | **G15 서식22·제18호·시간준수·무결성·geocode ✅** · **G29·G30 신규** · **demo-work 송영 0건** | REQUIREMENTS G15·G29·G30 · ROADMAP v1.3-C · USER_STORIES US-T05 |
| **QA** | **Open 0건** · Planned **0건** (B19 Fixed) | Planned 이동 **없음** |
| **merge gate** | P0 `[x]` · **`merge_status: ready`** · **144 commits** | ★ **FULLY UNBLOCKED** — tester develop→test merge 즉시 가능 |
| **잔여 P1** | G15 **2-1-1/2-9·이동서비스비** · G7 실파일 · G2 SMTP · live E2E 백로그 | ROADMAP v1.3-C·v1.2.1 우선순위 갱신 |

**coder 다음 액션 (97차)**: ① **tester merge(81+63=144)** ② G15 **2-1-1/2-9·이동서비스비** ③ G7 **실파일**(#27) ④ G2 **SMTP** ⑤ G13·US-J02 **live run** ⑥ G21 **live E2E** ⑦ US-L01 **은행 8종 E2E live** ⑧ v1.3 live E2E.

---

### [BNK] BNK-58 인사이트 (2026-06-10) — ★ G15 2-2/2-3 · 계약 서명 · G11 v2 · lcms selectProductGuide

> `BENCHMARK_REPORT.md` §61 · `COMPETITOR_MATRIX.md` §58 · `memory/decisions.md` BNK-58 참조.

| # | 항목 | 권장 조치 (planner 반영) |
|---|------|------------------------|
| 1 | **★ G15 2-2/2-3 출석 이원화 ✅** | FE `/attendance/boarding`·`/on-site`·`attendanceTransportMode.js` @ `6c4c151` · BE `GET /attendance?transportMode=boarding\|on_site` @ `d6d7e7f` — 케어포 2-2/2-3 패리티. |
| 2 | **★ G15 계약 서명 API+UI ✅** | BE `TransportContractService`·V64 @ `3c8f9fe` · FE `TransportCompliancePanel` wiring @ `9e3cab5`. |
| 3 | **★ G11 v2 청구 자동 가산 ✅** | BE `feat(v2/G11): apply fee surcharge automatically in claim generation` @ `d7475fd` — 이지케어 fnc 패리티. |
| 4 | **QA-B19 geocode failure UI WIP** | WT 4M — `countGeocodeFailures`·Alert·저장 차단 · **Planned** · FE merge BLOCK. |
| 5 | **잔여 P1** | 2-1-1/2-9 외출 lifecycle · 운행일지 DB · 이동서비스 **시간 준수** 기록(엔젤 평가) · US-L01 은행 live · #44 수동. |
| 6 | **lcms selectProductGuide 신규** | [selectProductGuide.do](https://www.lcms.or.kr/reg/selectProductGuide.do) — G10 **정원 tier 과금** 벤치 보강. |
| 7 | **merge 133 · npm 482 · mvn 453** | tester develop→test **74+59=133** · BE WT CLEAN · **FE WT DIRTY 4M** · 모듈 **74.81%**. |

---

### [PLA] QA 피드백 반영 (2026-06-10, 96차 — BNK-58 · TSR 231~232 · QA Open→Planned 1건)

> **96차 자동 기획 동기화** — BNK-58(G15 2-2/2-3·계약 서명·G11 v2)·TSR 231~232. **QA-20260610-B19 Open→Planned**.

| 항목 | 96차 관측 | 조치 |
|------|----------|------|
| **baseline** | FE **`6c4c151`** · BE **`d6d7e7f`** · **74+59 ahead** · **BE WT CLEAN · FE WT DIRTY 4M** · **48 path·40 page** · **482/127·453 PASS** | ROADMAP CURRENT BASELINE **96차** 갱신 |
| **BNK-58** | **G15 2-2/2-3 ✅** · **계약 서명 ✅** · **G11 v2 ✅** · **#44 4차 0건** · **lcms selectProductGuide** | REQUIREMENTS G15·G11 · ROADMAP v1.3-C · USER_STORIES US-T05·US-E06 |
| **QA-B19** | FE WT **4M** geocode failure UI WIP · B07 #12 | Open→**Planned** · ROADMAP v1.3-C·v1.2.1 FE merge gate |
| **merge gate** | P0 `[x]` · BE **ready** · FE **BLOCK** · **133 commits** | BE merge 즉시 가능 · FE **WT clean 선행** |
| **잔여 P1** | **B19 커밋/revert** · G15 **2-1-1/2-9·운행일지** · G7 실파일 · G2 SMTP · live E2E 백로그 | ROADMAP v1.3-C·v1.2.1 우선순위 갱신 |

**coder 다음 액션 (96차)**: ① **B19 geocode UI 커밋 or revert → FE WT clean** ② **tester merge(74+59=133)** ③ G15 **2-1-1/2-9·운행일지** ④ G7 **실파일**(#27) ⑤ G2 **SMTP** ⑥ G13·US-J02 **live run** ⑦ G21 **live E2E** ⑧ US-L01 **은행 8종 E2E live**.

---

### [BNK] BNK-53 인사이트 (2026-06-10) — ★ G11 catalog+가이드 E2E · G15 v1.3-C 부분 · 케어포 108 leaf 불변

> `BENCHMARK_REPORT.md` §56 · `COMPETITOR_MATRIX.md` §53 · `memory/decisions.md` BNK-53 참조.

| # | 항목 | 권장 조치 (planner 반영) |
|---|------|------------------------|
| 1 | **★ G11 가산율 catalog+가이드 E2E ✅** | `FeeSurchargeRateCatalog` 야20·심야30·휴일30·유급휴일50%·`NO_STACKING_NOTE`·`V1_NOTICE` @ `904072b` · `GET/POST /billing/fee-surcharge-*` · FE `FeeSurchargeGuidePanel` `/billing/fee-schedules` @ `3db8db3`. **잔여 v2 P1**: 청구 자동 가산(이지케어 fnc 패리티). |
| 2 | **★ G15 v1.3-C 부분 ✅** | `TransportCompliancePanel` 5수칙+계약서·일지 Modal @ `3db8db3` — 평가 자료 제출 기준 충족(텍스트 정본). **잔여 P1**: ① 계약서 서명 저장 API ② 탑승(2-2)/출석(2-3) 이원화 ③ 외출 리포트(2-9). |
| 3 | **케어포 func.php 108 leaf·11 모듈 verbatim 불변** | Wayback md5 `5005fef7…` · 8-11 「삭제예정」·7-10 「간편계산기」 불변 · live carefor **timeout 30s** 지속. |
| 4 | **G27·US-L01 bank FE ✅ 재확인** | BNK-50~52·94차 lineage — `MonthlyBenefitCapGuardPanel`·`BankDepositImportPanel` @ `9ffff0c`/`fba5ea8`. |
| 5 | **#44 수동 보류** | BNK-47 확정 **번복 없음** · 830/2,630/4,430/6,230 유지. |
| 6 | **merge 122 · npm 467 · mvn 434** | tester develop→test **68+54=122** · 양쪽 WT CLEAN · 모듈 **74.81%** 불변. |

---

### [PLA] QA 피드백 반영 (2026-06-10, 95차 — BNK-53 · TSR 219~220 · QA Open 0건)

> **95차 자동 기획 동기화** — BNK-53(G11 catalog+가이드·G15 v1.3-C 부분)·TSR 219~220. **QA Open 0건** · **이동 없음**.

| 항목 | 95차 관측 | 조치 |
|------|----------|------|
| **baseline** | FE **`62f022df`** · BE **`d5e0e01`** · **68+54 ahead** · **양 스트림 WT CLEAN** · **46 path·40 page** · **467/126·434 PASS** | ROADMAP CURRENT BASELINE **95차** 갱신 |
| **BNK-53** | **G11 catalog+가이드 E2E ✅** · **G15 v1.3-C 부분 ✅** · **G27·US-L01 bank FE ✅** · **케어포 108 leaf 불변** · **#44 수동 보류** | REQUIREMENTS G11·G15·G27·G13 · ROADMAP v1.2.1·v1.3-C · USER_STORIES US-M05·US-T05·US-M04·US-L01 · API_SPEC §7-1-b |
| **merge gate** | P0 `[x]` · **`merge_status: ready`** · **122 commits** | ★ **FULLY UNBLOCKED** — tester develop→test merge 즉시 가능 |
| **QA Open** | **0건** (frontend·backend) | Planned 이동 **없음** |
| **잔여 P1** | **G11 v2 자동 가산** · **G15 v1.3-C 잔여 3건** · G7 실파일 · G2 SMTP · G13·US-J02 live · G21 live E2E · US-L01 은행 8종 E2E live | ROADMAP v1.2.1·v1.3-C·v2 우선순위 갱신 |

**coder 다음 액션 (95차)**: ① **tester merge(68+54=122)** ② G11 **v2 청구 자동 가산** ③ G15 **서명 API·탑승/출석·2-9** ④ G7 **실파일**(#27) ⑤ G2 **SMTP 실연동** ⑥ G13·US-J02 **live run** ⑦ G21 **live E2E** ⑧ US-L01 **은행 8종 E2E live**.

---

### [BNK] BNK-49 인사이트 (2026-06-10) — ★ G27 BE · US-L01 bank BE · US-M03-b 닫힘 · 케어포 2-x 11 leaf

> `BENCHMARK_REPORT.md` §52 · `COMPETITOR_MATRIX.md` §49 · `memory/decisions.md` BNK-49 참조.

| # | 항목 | 권장 조치 (planner 반영) |
|---|------|------------------------|
| 1 | **★ G27 재가급여 월한도액 2026 BE catalog+guard ✅** | `MonthlyBenefitCapCatalog` MOHW 247 verbatim @ `a92e625` — 1등급 **2,512,900**~5등급 **1,208,900** · `GET /monthly-benefit-caps`·`/monthly-benefit-cap-guard`. **잔여 P1**: **인지지원 676,320** 시드 · **FE `/billing`·`/dashboard` 월한도 표기·초과 경고**(US-M04 · 케어포 10-2-1). |
| 2 | **★ US-L01 은행엑셀 일괄입금 BE-only ✅** | `POST /billing/imports/bank-deposits` · flexible header parser @ `e50533f`/`95bb34d`. **잔여 P1**: **FE upload UI on `/billing/payments`**. |
| 3 | **★ US-M03-b 청구생성기준+전월가드 ✅** | BE `@b953662`/`857bd32` · FE `@5bdb476`/`911e732`/`25f3225` — BNK-47 §49-7 **1사이클 닫힘**. **잔여**: NHIS import live + 운영 가이드. |
| 4 | **케어포 func.php 2-x 11 leaf verbatim** | 탑승/출석 **이원화** · **2-7~2-9** 리포트 · 외출 lifecycle — ogada `/transport`는 **pickup-only** → **G15 v1.3-C** 세부 갭(수칙·계약 Route). |
| 5 | **#44 수동 보류** | BNK-47 MOHW 247 PDF 0건 확정 **번복 없음** · 830/2,630/4,430/6,230 **유지**. |
| 6 | **가정 번복 0건** | US-M03·G14·대시보드·#44 BNK-47 가정 **유지**. |
| 7 | **merge 110 · npm 434 · mvn 412** | tester develop→test **61+49=110** · 양쪽 WT CLEAN · 모듈 **74.81%** 불변. |

---

### [PLA] QA 피드백 반영 (2026-06-10, 94차 — BNK-49 · TSR 207~208 · QA Open 0건)

> **94차 자동 기획 동기화** — BNK-49(G27 BE·US-L01 bank BE·US-M03-b·케어포 2-x)·TSR 207~208. **QA Open 0건** · **이동 없음** — QA-20260610-B07 #11 **Fixed** @ `c9451a0`.

| 항목 | 94차 관측 | 조치 |
|------|----------|------|
| **baseline** | FE **`c9451a0`** · BE **`467cd70`** · **61+49 ahead** · **양 스트림 WT CLEAN** · **46 path·40 page** · **434/434·412 PASS** | ROADMAP CURRENT BASELINE **94차** 갱신 |
| **BNK-49** | **G27 BE ✅** · **US-L01 bank BE ✅** · **US-M03-b ✅** · **케어포 2-x 11 leaf** · **#44 수동 보류** | REQUIREMENTS G27·G28·G15 · ROADMAP v1.2.1·v1.3-C · USER_STORIES US-M03-b·US-M04·US-L01·US-T05 |
| **merge gate** | P0 `[x]` · **`merge_status: ready`** · **110 commits** | ★ **FULLY UNBLOCKED** — tester develop→test merge 즉시 가능 |
| **QA Open** | **0건** (frontend·backend) | Planned 이동 **없음** |
| **잔여 P1** | **G27 FE** · **US-L01 bank FE** · G7 실파일(#27) · G2 SMTP · G13·US-J02 live run · G21 live E2E · **G15 v1.3-C** | ROADMAP v1.2.1·v1.3-C 우선순위 갱신 |

---

### [BNK] BNK-47 인사이트 (2026-06-10) — ★ #44 「247 PDF 0건 확정」 · 제13조⑩ 통합재가 +10% · 재가급여 월한도액 2026 인상 · 제74조 치매전담 시설 정정

> `BENCHMARK_REPORT.md` §50 · `COMPETITOR_MATRIX.md` §47 · `memory/decisions.md` BNK-47 9행 참조.

| # | 항목 | 권장 조치 (planner 반영) |
|---|------|------------------------|
| 1 | **★ #44 「MOHW 247 PDF 「이동서비스비」 0건 확정 — 추적 종료」** | [PDF 재추출](https://www.mohw.go.kr/boardDownload.es?bid=0026&list_no=1488433&seq=2) 30,423 chars — 「이동서비스/이동서비스비/제34조/러-/830/2,630/4,430/6,230」 **모두 0건 verbatim**. 247 PDF §2-가 개정대상조항 목록에 **제34조 미포함**. [law.go.kr admRulInfoP](https://www.law.go.kr/LSW/admRulInfoP.do?admRulSeq=2100000271110&chrClsCd=010201) **JS 렌더 → curl 본문 0건**. → **#44 「P0 BLOCK」 → 「수동·공단 매뉴얼 발견 시 재개」**로 격하. **BNK-25 2차 교차 단가 830/2,630/4,430/6,230 유지·하드코딩 금지**. |
| 2 | **★ 신규 1차 정본 — 제13조 ⑩ 통합재가 월한도액 +10% 추가산정** | [PDF p.10~11 verbatim](https://www.mohw.go.kr/boardDownload.es?bid=0026&list_no=1488433&seq=2) 「가정방문형 통합재가 80%이상 → 등급별 월한도액 10% 추가산정」 + 「**제13조⑩4호 ↔ 제55조의2 mutually exclusive**」. ogada v1 Won't 유지 + v2+ `billing_addons.addon_code` CHECK 제약(INTEGRATED_HOME_10PCT vs DAYCARE_INTEGRATED_100K) **P2 신규 룰**. |
| 3 | **★ 신규 1차 정본 — 재가급여 월한도액 2026 인상값** | [PDF p.10 verbatim](https://www.mohw.go.kr/boardDownload.es?bid=0026&list_no=1488433&seq=2) — 1등급 **2,512,900(+9.0%)**·2등급 2,331,200·3등급 1,528,200·4등급 1,409,700·5등급 1,208,900·인지지원 676,320. **P1 신규**: `feeSchedules.js`에 `monthlyBenefitCaps2026` 시드 + **「월한도 초과 경고」 UX**(케어포 10-2-1 패턴 패리티). |
| 4 | **★ BNK-44 가정 부분 정정 — 제74조 치매전담형 시설 (1등급 없음·시설 Won't v1)** | [PDF p.52~53 verbatim](https://www.mohw.go.kr/boardDownload.es?bid=0026&list_no=1488433&seq=2) 「제74조(치매전담형장기요양기관급여비용)」 = **시설급여 사-1~4·2등급부터**. BNK-44 「`programType=DEMENTIA_DAY` 확장 P2」 가정은 「**시설 사-X = ogada 시설 Won't v1 → 적용 X**」로 정정 · 주야간 치매전담실 별도 표는 247 PDF 미게재 → **P3 보류**. |
| 5 | **★ US-M03 청구 생성기준 설정 + 전월 미입금 가드 1사이클 내 닫힘** | BE `@857bd32`(prior month copay block)·`@b953662`(settings + NHIS path) · FE `@911e732`(prior-month guard UI)·`@25f3225`(settings UI) — BNK-46 §49-7 P1 신규 갭(케어포 PDF p.85·9-1) **1사이클 진전**. **잔여**: NHIS import live + 운영 가이드(케어포 7-1↔7-2 「전월 입금 필수」 패리티 검증). |
| 6 | **silverangel·extraService·daycareEssentialWork md5 동일** | system_feature md5 **`c950719`**·extraService md5 **`f9c5d8`**·daycareEssentialWork md5 **`c79c1be`** — **BNK-44/37 정독 무드리프트**. 정량 카운트(전자결재 2·전자서명 12·노인학대 5·납부확인서 2·월마감 1·관리자가 확인 1) — G2/UXD 갭 유효. |
| 7 | **이지케어 미실측 (다음 사이클)** | BNK-47은 엔젤·롱텀·규제 로테이션. 이지케어 charge·도입수는 BNK-42(9,308)·BNK-45(9,309) 기준 → BNK-48에서 재측정. |
| 8 | **merge 103 · npm 428 · mvn 390** | tester develop→test **58+45=103** · 양쪽 WT CLEAN · 모듈 **74.81%** 불변. |

---

### [BNK] BNK-45 인사이트 (2026-06-10) — ★ #44 서비스 구분 · 케어포 46105 · G2 +2 · US-L01 guard

> `BENCHMARK_REPORT.md` §48 · `COMPETITOR_MATRIX.md` §45 · `memory/decisions.md` BNK-45 8행 참조.

| # | 항목 | 권장 조치 (planner 반영) |
|---|------|------------------------|
| 1 | **★ #44 「이동지원서비스 시범사업」≠「이동서비스비(러-1~4)」** | 방문요양 **동행·편도 3,000원** 시범사업과 주야간 **픽업/드롭 러-1~4**는 **별개 서비스** — ogada는 후자만 해당(v1.3-C). 문서 표기 **「#44 별표18 수동 추출」→「#44 제34조·공단 매뉴얼 1차 출처 재추적」** 로 갱신. **830/2,630/4,430/6,230 불변**. |
| 2 | **케어포 공지 46105 — 2026 평가 반영** | [공지 46105](https://www.carefor.co.kr/cs/view_notice.php?calmgno=46105) — 2025-12-23 주야간 평가지표 업데이트 · 지표25(기능회복훈련 계획)·26(실행) — **G17 ogada 갭 유지** · v3.1 `programType=FUNCTIONAL_RECOVERY` 후보. |
| 3 | **G2 +2 templates partial 닫힘** | BE `@0854fbd`·FE `@eedcc80` — **납부확인서·노인학대예방교육** 이메일/notify (엔젤 extraService·system_feature). **SMTP live·스케줄 잔여**. |
| 4 | **US-L01 overpayment guard** | FE `@dd72ff8`·BE `@4109680` — 초과입금·non-positive amount 차단 (QA-20260610-B15 Fixed). |
| 5 | **G19 통합재가 라벨 (Won't v1 유지)** | FE `@4c7c994` — 지점 폼 **「통합재가 가산 월 100,000원/인」** 안내 라벨만. 전체 G19 기능은 Won't v1. |
| 6 | **이지케어 9,309**(+1) · merge **98** | tester develop→test merge **55+43** · npm **413** · mvn **383** · 모듈 **74.81%** 불변. |

---

### [PLA] QA 피드백 반영 (2026-06-10, 93차 — BNK-45 · TSR 192~196 · QA Open 0건)

> **93차 자동 기획 동기화** — BNK-45(#44 재정의·46105·G2 +2·US-L01)·TSR 192~196. **QA Open 0건** · **이동 없음** — QA-20260610-B15 **Fixed** @ `4109680`.

| 항목 | 93차 관측 | 조치 |
|------|----------|------|
| **baseline** | FE **`eedcc80`** · BE **`0854fbd`** · **55+43 ahead** · **양 스트림 WT CLEAN** · **46 path·40 page** · **413/413·383 PASS** | ROADMAP CURRENT BASELINE **93차** 갱신 |
| **BNK-45** | **#44 서비스 구분** · **이지케어 9,309** · **46105** · **US-L01 guard** · **G2 5종 partial** · **G19 라벨** | REQUIREMENTS G16·G2-n·G19 · ROADMAP v1.2.1 · USER_STORIES US-L01 |
| **merge gate** | P0 `[x]` · **`merge_status: ready`** · **98 commits** | ★ **FULLY UNBLOCKED** — tester develop→test merge 즉시 가능 |

**coder 다음 액션 (93차)**: ① **tester merge(55+43=98)** ② G7 **실파일**(#27) ③ G2 **SMTP 실연동** ④ G13·US-J02 **live run**(결정 73) ⑤ G21 **live E2E** ⑥ G15 수칙·계약 Route ⑦ G11 가산수가 ⑧ **#44 제34조 1차 출처** ⑨ v1.3 live E2E.

---

### [BNK] BNK-44 인사이트 (2026-06-10) — ★ #44 가정 수정 · MOHW 247 PDF 정본 · 치매전담실 5밴드 · G2 +2 템플릿

> 다음 PLN 자동동기화 사이클에서 반영 요청. `BENCHMARK_REPORT.md` §47 · `memory/decisions.md` 최상단 BNK-44 8행 참조.

| # | 항목 | 권장 조치 (planner 검토) |
|---|------|------------------------|
| 1 | **★ #44 「별표18」 가정 자체 수정** | [law.go.kr admRulBylInfoR](https://www.law.go.kr/LSW/admRulBylInfoR.do?admRulSeq=2100000271110&bylClsCd=110201&bylNo=18) 본 고시는 「**별표 1·2뿐 — 별표 18 미존재**」. **93차 BNK-45 추가**: 「이동지원서비스 시범사업」(동행·3,000원)은 ogada **비해당**. 주야간 이동서비스비는 **고시 제34조·공단 매뉴얼** 재추적. **단가(BNK-25 2차) 불변**. |
| 2 | **★ MOHW 제2025-247 PDF 1차 정본 확보** | [PDF](https://www.mohw.go.kr/boardDownload.es?bid=0026&list_no=1488433&seq=2) pypdf 30,479 chars — 라/마/바 5밴드·제55조의2 통합재가 가산 100,000원/인·제36조의2 가족인 요양보호사 12일·별표2 취약지 52개·가족요양비 240,450원 verbatim. `feeSchedules.js` 라-4 76,820 PDF 일치 재확인. |
| 3 | **★ 치매전담실 5밴드 신규 갭** | [공단 2026 수가](https://www.longtermcare.or.kr/npbs/e/b/502/npeb502m01.web?menuId=npe0000002742)에 「치매전담실」 별도 5밴드 존재 — 현 `feeSchedules.js`는 일반형만 시드. **P2 신규**: `programType` enum 확장(`DEMENTIA_DAY`) + 별도 매트릭스 시드(G9 v1.2). |
| 4 | **G2 +2 템플릿** | silverangel `system_feature`/`extraService` — ① **납부확인서 이메일** ② **노인학대예방교육 자동 이메일+기록**. **93차 partial 닫힘** @ `0854fbd`/`eedcc80` — **SMTP live·스케줄 잔여**. |
| 5 | **G19 통합재가 라벨 표기** | Won't v1 유지하되, 명세서에 「**통합재가 가산** 월 100,000원/인」 라벨 옵션 표기(MOHW 제55조의2 정본). P3. |
| 6 | **G15 41~42 / G11 가산율 / G21 live E2E** | 92차 다음 액션 ⑥~⑦ 그대로 유지. BNK-44는 본 영역 신규 인사이트 없음. |

---

### [PLA] QA 피드백 반영 (2026-06-10, 92차 — BNK-42 · TSR 183·184 · QA Open 0건)

> **92차 자동 기획 동기화** — BNK-42(G9 닫힘·G2 templates·US-J02·모듈 74.81%)·TSR 183(FE)·184(BE). **QA Open 0건** · **이동 없음** — QA-B07 #10 **Fixed** @ `5348d9c`.

| 항목 | 92차 관측 | 조치 |
|------|----------|------|
| **baseline** | FE **`eb3f0fd`** · BE **`f77a268`** · **48+38 ahead** · **양 스트림 WT CLEAN** · **46 path·40 page** · **390/390·371 PASS** | ROADMAP CURRENT BASELINE **92차** 갱신 |
| **BNK-42** | **G9 duration_band ✅** — 25셀·스냅샷·폴백(`6fe853b`/`5348d9c`/`eb3f0fd`) · **G2 templates 3종** @ `f77a268`+원화 `872e040` · **이지케어 9,308/9,231** · **모듈 74.81%** · **가정 번복 0건** | REQUIREMENTS G9·G2 · ROADMAP v1.2.1 · USER_STORIES US-G00a·US-J02·G2-n |
| **US-J02** | billing filter/dedupe/retry @ `0dc4c4a`/`5348d9c` — QA-B07 #10 **Fixed** | USER_STORIES US-J02 인수 조건 `[x]` |
| **merge gate** | P0 `[x]` · **`merge_status: ready`** · **86 commits** | ★ **FULLY UNBLOCKED** — tester develop→test merge 즉시 가능 |

**coder 다음 액션 (92차)**: ① **tester merge(48+38=86)** ② G7 **실파일**(#27) ③ G2 **SMTP 실연동** ④ G13·US-J02 **live run**(결정 73) ⑤ G21 **live E2E** ⑥ G15 수칙·계약 Route ⑦ G11 가산수가 ⑧ #44 별표18 수동 추출.

### [PLA] QA 피드백 반영 (2026-06-10, 91차 — BNK-38 · TSR 172 · QA-B07 #10 Planned)

> **91차 자동 기획 동기화** — BNK-38(G9·G21 billing lock·G2 SMTP·CMS FE)·TSR 172(FE). **QA Open 1건→Planned** — **QA-20260610-B07 #10**.

| 항목 | 91차 관측 | 조치 |
|------|----------|------|
| **baseline** | FE **`527ba2d`** · BE **`06d68dd`** · **41+34 ahead** · **FE WT DIRTY 2M** · **BE WT CLEAN** · **46 path·40 page** · **370/370·359 PASS** | ROADMAP CURRENT BASELINE **91차** 갱신 |
| **BNK-38** | **G9 duration_band partial** @ `425a05f`/`06d68dd` · **G21 billing confirm-lock partial** @ `c4fb7ff`/`02cd2b2` · **G2 SMTP committed** @ `6ed48ff`/`f23f15a` · **CMS FE Route ✅** @ `6c6dc7a`/`c0a01b4` | REQUIREMENTS G2·G9·G21 · ROADMAP v1.2.1·v2 · USER_STORIES US-L03·US-J02 |
| **QA-B07 #10** | FE WT **DIRTY 2M** — `GuardianPortalPage`(+test) US-J02 WIP: billing filter/dedupe/retry | Open→**Planned** · ROADMAP v1.2.1 FE WT clean 선행 · USER_STORIES US-J02 인수 조건 추가 |
| **merge gate** | P0 `[x]` · **`merge_status: ready`** · **75 commits** | **BE FULLY UNBLOCKED** · **FE WT clean 선행** |

**coder 다음 액션 (91차)**: ① **US-J02 WIP 커밋+push** 또는 revert → FE WT CLEAN ② **tester merge(41+34)** ③ G7 **실파일**(#27) ④ G2 **SMTP templates·실발송** ⑤ G9 **duration_band 완료** ⑥ G13·US-J02 **live run** ⑦ G21 **live E2E** ⑧ Hyosung FCMS **실연동** ⑨ G11 가산수가.

### [PLA] QA 피드백 반영 (2026-06-10, 90차 — BNK-35 · TSR 159·160 · merge FULLY UNBLOCKED)

> **90차 자동 기획 동기화** — BNK-35(7-x·CMS stub·G25·111 leaf)·TSR 159(BE)·160(FE). **QA Open 0건** · **Planned 0건** · **이동 없음**.

| 항목 | 90차 관측 | 조치 |
|------|----------|------|
| **baseline** | FE **`e6df92c`** · BE **`2c6e57e`** · **34+30 ahead** · **양 스트림 WT CLEAN** · **45 path·39 page** · **351/100·350/350 PASS** | ROADMAP CURRENT BASELINE **90차** 갱신 |
| **BNK-35** | func.php **111 leaf·32 리포트(28.8%)** · **7-x 8/11** · **CMS BE stub** @ `2c6e57e` · **G2 email skeleton** @ `fbedcc3`/`6eba2ef` · **공지920 본인부담률 엑셀 P2(G25)** | REQUIREMENTS G2·G25 · ROADMAP v2 CMS · USER_STORIES US-M02-c |
| **US-M02-c** | **7위젯**(`overdueCount`+`pendingReviewCount`) @ `f755428`/`20bfac1` | ROADMAP v1.2.1 · USER_STORIES US-M02 |
| **G13 hardening** | cross-page live billing E2E @ `c72e9df`/`e6df92c` | ROADMAP v1.2.1 US-L02 · **live run 잔여**(결정 73) |
| **merge gate** | P0+G7 UX+US-M02-b+US-M02-c+US-J03-h `[x]` · **`merge_status: ready`** · **64 commits** | ★ **FULLY UNBLOCKED** — tester merge 즉시 가능 |
| **QA** | Open **0** · Planned **0** | 신규 태스크 **없음** |

**coder 다음 액션 (90차)**: ① **tester merge(34+30)** ② G7 **실파일**(#27) ③ G2 **SMTP/메일벤더** 실연동 ④ v2 **CMS FE Route**(`/billing/cms`) ⑤ G13·US-J02 **live run** ⑥ G21 **통합 E2E** ⑦ G9 **duration_band** ⑧ G11 가산수가.

### [PLA] QA 피드백 반영 (2026-06-10, 89차 — BNK-31 · TSR 147·148 · merge FULLY UNBLOCKED)

> **89차 자동 기획 동기화** — BNK-31(G13 E2E·G21 visit 파서·v3 meals/programs FE 닫힘·G2 이메일 P1)·TSR 147(BE)·148(FE). **QA Open 0건** · **Planned 0건** · **이동 없음**.

| 항목 | 89차 관측 | 조치 |
|------|----------|------|
| **baseline** | FE **`14e9066`** · BE **`0ebe945`** · **28+24 ahead** · **양 스트림 WT CLEAN** · **45 path·39 page** · **340/97·334/334 PASS** | ROADMAP CURRENT BASELINE **89차** 갱신 |
| **BNK-31** | **G13 US-L02 pagination·reminder E2E** @ `fed457f`/`14e9066` · **G21 visit 파서** @ `7fbd219` · **v3 meals/programs FE POST** @ `6a59b74` · G14·대시보드·#44·v2 CMS **번복 없음** | REQUIREMENTS G5·G13·G21 · USER_STORIES US-L02·Epic N · ROADMAP v1.2.1 US-L02 partial |
| **merge gate** | P0+G7 UX+US-M02-b+US-J03-h `[x]` · **`merge_status: ready`** · **52 commits** | ★ **FULLY UNBLOCKED** — tester merge 즉시 가능 |
| **QA** | Open **0** · Planned **0** | 신규 태스크 **없음** |

**coder 다음 액션 (89차)**: ① **tester merge(28+24)** ② G7 **실파일**(#27) ③ G2 **이메일 실발송 채널**(엔젤 법정서식 3종) ④ G13 **cross-page 상태전이** live E2E ⑤ G21 **통합 E2E** ⑥ v1.3 live E2E ⑦ 이지케어 **2026.7.1** FAQ 스캔.

### [PLA] QA 피드백 반영 (2026-06-10, 88차 — BNK-28 · TSR 135·136 · merge FULLY UNBLOCKED)

> **88차 자동 기획 동기화** — BNK-28(G21 확정↔import·G2 notify·대기수급자 P2)·TSR 135(BE)·136(FE). **QA Open 0건** · **Planned 0건** · **이동 없음**.

| 항목 | 88차 관측 | 조치 |
|------|----------|------|
| **baseline** | FE **`311c7c0`** · BE **`3e4d3e6`** · **21+19 ahead** · **양 스트림 WT CLEAN** · **45 path·39 page** · **326/93·329/329 PASS** | ROADMAP CURRENT BASELINE **88차** 갱신 |
| **BNK-28** | 케어포 func.php **97 leaf·리포트 44%** · **G21 확정↔import P1 닫힘** @ `bf3d40d`/`84f3441` · **G2 notify** @ `c48fb67`/`84f3441` · **US-V04 import FE partial** @ `60cea98`/`311c7c0` | REQUIREMENTS G2-n·G21·G23·G24 · USER_STORIES Epic V·US-G02·US-V02·US-V04 · API_SPEC §7·§14 |
| **merge gate** | P0+G7 UX+US-M02-b+US-J03-h `[x]` · **`merge_status: ready`** · **40 commits** | ★ **FULLY UNBLOCKED** — tester merge 즉시 가능 |
| **QA** | Open **0** · Planned **0** | 신규 태스크 **없음** |

**coder 다음 액션 (88차)**: ① **tester merge(21+19)** ② G7 **실파일**(#27) ③ G2-n **실발송 채널** ④ US-J02·G13 **live** E2E ⑤ v1.3 live E2E ⑥ Epic V **US-V04 live E2E** ⑦ v3 meals/programs **FE 연결**.

### [COD] 설정 API 정합·SEC-D17 apiFetch (2026-06-09, 88차 갱신)

| 항목 | 상태 | 비고 |
|------|------|------|
| **로그인 이력** | ✅ FE `@develop` | `GET /auth/login-history` + apiFetch · 필드 `roleCode`·`ipAddress`·`createdAt` |
| **감사 로그** | ✅ FE | `GET /settings/audit-logs?page&size` · `action`·`createdAt` 매핑 |
| **백업** | ✅ FE | `GET /settings/backups` + `PATCH /settings/system { backupEnabled }` |
| **비밀번호 재설정** | ✅ FE | `POST /auth/password/reset-request` (기존 `/password-reset/request` 오류 수정) |
| **비밀번호 변경** | ☐ **BLOCK(BE)** | `POST /auth/change-password` **백엔드 미구현** — FE `changePasswordApi`·`PasswordChangeModal` fieldErrors 준비됨 · backend stream 착수 필요 |
| **billing/guardian/platform/settings apiFetch** | ✅ FE @ `e1320f4` | SEC-D17 — raw fetch 제거 · `services.js` 통일 (BNK-25) |

### [PLA] QA 피드백 반영 (2026-06-10, 87차 — BNK-25 · TSR 123·124 · merge FULLY UNBLOCKED)

> **87차 자동 기획 동기화** — BNK-25(#44 충돌 해소·G17·G21)·TSR 123(BE)·124(FE). **QA Open 0건** · **Planned 0건** · **이동 없음**.

| 항목 | 87차 관측 | 조치 |
|------|----------|------|
| **baseline** | FE **`e1320f4`** · BE **`ee3fa3a`** · **15+12 ahead** · **양 스트림 WT CLEAN** · **45 path·39 page** · **311/91·306/306 PASS** | ROADMAP CURRENT BASELINE **87차** 갱신 |
| **BNK-25** | **#44 2차 교차 확정** 830/2,630/4,430/6,230 · **G17** 지표25+26 · **G21** NHIS import @ `ee3fa3a` · **SEC-D17** @ `e1320f4` | REQUIREMENTS G16·G17·G21 · USER_STORIES US-T05·T06·**US-V04** |
| **merge gate** | P0+G7 UX+US-M02-b+US-J03-h `[x]` · **`merge_status: ready`** · **27 commits** | ★ **FULLY UNBLOCKED** — tester merge 즉시 가능 |
| **QA** | Open **0** · Planned **0** | 신규 태스크 **없음** |

**coder 다음 액션 (87차)**: ① **tester merge(15+12)** ② G7 **실파일**(#27) ③ US-J02·G13 **live** E2E ④ v1.3 live E2E ⑤ Epic V **US-V04** NHIS import FE ⑥ G11·알림톡 실발송(v1.1).

### [PLA] QA 피드백 반영 (2026-06-10, 86차 — TSR 116 · BNK-22 재확인 · baseline 불변)

> **86차 자동 기획 동기화** — TSR 116(FE/BE)·BNK-22(US-J03-h 닫힘). **QA Open 0건** · **Planned 0건** · **이동 없음** · baseline **85차와 동일**.

| 항목 | 86차 관측 | 조치 |
|------|----------|------|
| **baseline** | FE **`e39164d`** · BE **`dd49204`** · **11+6 ahead** · FE **WT DIRTY 9** · BE **WT DIRTY 26** · **45 path·39 page** | ROADMAP CURRENT BASELINE **86차** 유지 |
| **TSR 116** | FE **287/89 PASS**(WT dirty) · BE **288/288 PASS** @ HEAD · **신규 Open 0건** | merge gate **WT clean 선행** 재확인 |
| **BNK-22** | **US-J03-h 닫힘** @ `e39164d` · 케어포 **10-7** 패리티 · **실발송(10-1) v1.1/v2** | REQUIREMENTS G8-h · USER_STORIES US-J03-h **유지** |
| **merge gate** | P0+G7 UX+US-M02-b+US-J03-h `[x]` · **`merge_status: ready`** · **17 commits** | **BE+FE WT clean** 후 tester merge |
| **QA** | Open **0** · Planned **0** | 신규 태스크 **없음** |

**coder 다음 액션 (86차)**: ① **backend WT clean**(26) ② **frontend WT clean**(9) ③ **tester merge(11+6)** ④ G7 **실파일**(#27) ⑤ US-J02·G13 **live** E2E ⑥ v1.3 live E2E ⑦ G11·알림톡 실발송(v1.1).

### [PLA] QA 피드백 반영 (2026-06-10, 85차 — BNK-22 · US-J03-h/G8 알림 이력 · FE WT DIRTY)

> **85차 자동 기획 동기화** — BNK-22(US-J03 알림 이력 폐루프·케어포 10-7·FE `@e39164d`·BE `@dd49204`). **QA Open 0건** · **Planned 0건** · **이동 없음**.

| 항목 | 85차 관측 | 조치 |
|------|----------|------|
| **baseline** | FE **`e39164d`** · BE **`dd49204`** · **11+6 ahead** · FE **WT DIRTY 9** · BE **WT DIRTY 26** · **45 path·39 page** · 테스트 **WT dirty 미재실행** | ROADMAP CURRENT BASELINE 갱신 |
| **BNK-22** | **G8 알림 발송 이력 UI 닫힘** — `NotificationHistoryPanel` @ `e39164d` · 케어포 **10-7 안내발송내역** 패리티 · PIPA 연락처 비표시 | ROADMAP v1.2.1 · USER_STORIES **US-J03-h** · REQUIREMENTS G8-h |
| **알림톡/SMS 실발송** | 케어포 **10-1 문자메시지 발송** 미연동 — `empty="알림톡 연동 미완"` | **v1.1/v2 잔여** · US-J03(알림톡) 범위 유지 |
| **모듈 커버** | **72.5%** 불변 — 발송 채널 연동 시 **~74.4%** 예상 | REQUIREMENTS §1-5-2 유지 |
| **merge gate** | P0+G7 UX+US-M02-b+US-J03-h `[x]` · **`merge_status: ready`** · **11+6 commits** | merge **선행 = BE WT clean + FE WT clean** |
| **QA** | Open **0** · Planned **0** | 신규 태스크 **없음** |

**coder 다음 액션 (85차)**: ① **backend WT clean**(26) ② **frontend WT clean**(9) ③ **tester merge(11+6)** ④ G7 **실파일**(#27) ⑤ US-J02·G13 **live** E2E ⑥ v1.3 live E2E ⑦ G11·알림톡 실발송(v1.1).

### [PLA] QA 피드백 반영 (2026-06-10, 84차 — BNK-20 · US-M02-b 닫힘 · FE WT CLEAN)

> **84차 자동 기획 동기화** — BNK-20(이지케어 역공학·RFID 2016 종료·G11·가격 9,306)·planner git 실측(FE `1794e1c`·BE `dd49204`). **QA Open 0건** · **Planned 0건** · **이동 없음**.

| 항목 | 84차 관측 | 조치 |
|------|----------|------|
| **baseline** | FE **`1794e1c`** · BE **`dd49204`** · **10+6 ahead** · FE **WT CLEAN** · BE **WT DIRTY 17** · **45 path·39 page** · **275/85·288/288 PASS** | ROADMAP CURRENT BASELINE 갱신 |
| **BNK-20** | 이지케어 **RFID 실시간 2016 종료→엑셀** · **G11 가산수가** 표준 기대치 · **9,306**·셋팅 **55k** · G21 이중일정 · 급여·회계 lock-in | REQUIREMENTS G7·G11·G21 · ROADMAP v2 |
| **US-M02-b** | `DashboardPage` **「NHIS 대기(보류)」** @ `1794e1c` — BNK-20 §23-1 갭 **해소** | ROADMAP v1.2.1 · USER_STORIES US-M02 |
| **G7 NHIS** | fixture tests @ `dd49204` **부분 ✅** · **실파일 BLOCK** (#27) | PLAN_NOTES #27 유지 |
| **merge gate** | P0+G7 UX+US-M02-b `[x]` · **`merge_status: ready`** · **10+6 commits** | merge **선행 = backend WT clean** |
| **QA** | Open **0** · Planned **0** | 신규 태스크 **없음** |

**coder 다음 액션 (84차)**: ① **backend WT clean**(v3 meals/programs·V55 WIP) ② **tester merge(10+6)** ③ G7 **실파일** 샘플(#27) ④ US-J02·G13 **live** E2E ⑤ v1.3 live E2E run ⑥ G11 가산수가(v1.1).

### [PLA] QA 피드백 반영 (2026-06-10, 83차 — BNK-19 · TSR 114 · `pendingReviewCount` P1)

> **83차 자동 기획 동기화** — BNK-19(교차검증·대시보드 갭·케어포 2장)·TSR 114(frontend `6db762a` UXD-59·WT DIRTY 3U·backend WT DIRTY 15). **QA Open 0건** · **Planned 0건** · **이동 없음**.

| 항목 | 83차 관측 | 조치 |
|------|----------|------|
| **baseline** | FE **`6db762a`** · BE **`dd49204`** · **9+6 ahead** · FE **WT DIRTY 3U** · BE **WT DIRTY 15** · **45 path·39 page** · **271/83·288/288 PASS** | ROADMAP CURRENT BASELINE 갱신 |
| **BNK-19** | G7 reconciliation **닫힘** 재확인 · **대시보드 `pendingReviewCount`** Could→**P1** · 케어포 **2장**·공지 **46626** | ROADMAP v1.2.1 · US-M02-b · REQUIREMENTS §1-5 |
| **G7 NHIS** | fixture tests @ `dd49204` **부분 ✅** · **실파일 BLOCK** (#27) | US-G06 · PLAN_NOTES #27 유지 |
| **UXD-59** | Epic K·L·J02 @ `6db762a` — `GuardianClientLinks`·`OverdueSummaryBar` | v1.2.1 P1 진전 · develop-only |
| **v3 bleed** | meals/programs forms WIP(FE 3U) · meals/programs API·V55 WIP(BE 15) | merge gate **WT clean 선행** |
| **merge gate** | P0+G7 UX `[x]` · **`merge_status: ready`** · **9+6 commits** | merge **선행 = WT clean** (TSR 114) |
| **QA** | Open **0** · Planned **0** | 신규 태스크 **없음** |

**coder 다음 액션 (83차)**: ① **develop WT clean**(v3 WIP 커밋/revert) ② **tester merge(9+6)** ③ G7 **실파일** 샘플(#27) ④ **대시보드 `pendingReviewCount`**(US-M02-b) ⑤ US-J02·G13 **live** E2E ⑥ v1.3 live E2E run.

### [PLA] QA 피드백 반영 (2026-06-09, 82차 — BNK-18 · TSR 112·113 · G7 FE 닫힘)

> **82차 자동 기획 동기화** — BNK-18(G7 3상태 폐루프·케어포 `처리상태`열 역전)·TSR 112(backend `dd49204` Region·NHIS fixture tests)·113(frontend `16402b2` G7·G13·Epic V E2E). **QA Open 0건** · **Planned 0건** · **이동 없음**.

| 항목 | 82차 관측 | 조치 |
|------|----------|------|
| **baseline** | FE **`16402b2`** · BE **`dd49204`** · **8+6 ahead** · WT **CLEAN** · **45 path·39 page** · **267/81·288/288 PASS** | ROADMAP CURRENT BASELINE 갱신 |
| **G7 NHIS** | BE **`PENDING_REVIEW`** @ `4cc328d`/`dd49204` · FE **`Badge`·`NhisReconciliationTable`·`NhisPendingReviewGuide`** @ `fbb0b7a`/`16402b2` | US-G06 **3상태 UX `[x]`** · G7 **실파일 샘플 BLOCK** |
| **G13** | `pilotPageFlows` US-L01·L02 @ `16402b2` | fetch-mock E2E **진전** · live E2E 잔여 |
| **Epic V G21** | `/visits` FE @ `371794f` · E2E partial @ `16402b2` | US-V01~V03 partial · v2 `in_progress` |
| **BNK-18** | 케어포 `처리상태`열 **삭제 우회→ogada 파싱** · `pendingReviewCount` ReconciliationPage ✅ | REQUIREMENTS G7 · ROADMAP v1.2.1 |
| **모듈 커버** | **72.5%** (불변) | REQUIREMENTS §1-5-2 유지 |
| **merge gate** | P0+US-M03+G7 UX 완료 · **TSR 113 FULLY UNBLOCKED** | tester merge **8+6** |
| **QA** | Open **0** · Planned **0** | 신규 태스크 **없음** |

**coder 다음 액션 (82차)**: ① **tester merge(8+6)** ② G7 **파일럿 실파일** 샘플(#27) ③ US-J02·G13 **live** E2E ④ v1.3 live E2E run ⑤ Epic V 공단 import ⑥ (Could) 대시보드 `pendingReviewCount` 위젯.

### [PLA] QA 피드백 반영 (2026-06-09, 81차 — BNK-17 · TSR 110·111 · G7 BE · Epic V FE)

> **81차 자동 기획 동기화** — BNK-17(G21 `/visits` FE·G7 `PENDING_REVIEW` BE·#44 충돌·FCMS)·TSR 110(backend `4cc328d`)·111(frontend `371794f` WT DIRTY 4). **QA Open 0건** · **Planned 0건** · **이동 없음**.

| 항목 | 81차 관측 | 조치 |
|------|----------|------|
| **baseline** | FE **`371794f`** · BE **`4cc328d`** · **6+5 ahead** · FE **WT DIRTY 4** · **45 path·39 page** | ROADMAP CURRENT BASELINE 갱신 |
| **G7 NHIS** | BE **`PENDING_REVIEW`** V54+서비스 @ `4cc328d` **커밋** · FE `NhisReconciliationTable` WIP | US-G06 partial · API_SPEC §7-4 갱신 |
| **Epic V G21** | `/visits` FE @ `371794f` — PLAN/BILLING Tabs·모바일 체크인 | US-V01~V03 partial · v2 `in_progress` |
| **BNK-17** | #44 law.go.kr **2차 출처 충돌** · CMS=**효성CMS(FCMS)** | v1.3-C BLOCK · G2 v2 FCMS API |
| **모듈 커버** | **72.5%** (불변, BNK-17 재실측) | REQUIREMENTS §1-5-2 유지 |
| **merge gate** | P0+US-M03 완료 · **`merge_status: ready`** | tester merge **6+5** · FE WT clean 권고 |
| **QA** | Open **0** · Planned **0** | 신규 태스크 **없음** |

**coder 다음 액션 (81차)**: ① **G7 FE 커밋**(WT clean) ② **tester merge(6+5)** ③ G7 파일럿 샘플 ④ G13·US-J02 live E2E ⑤ v1.3 live E2E ⑥ Epic V E2E.

### [PLA] QA 피드백 반영 (2026-06-09, 80차 — BNK-16 · TSR 109 · US-M03 닫힘)

> **80차 자동 기획 동기화** — BNK-16(이지케어 FAQ 233건·US-M03 닫힘)·TSR 109(frontend `0a07799`). **QA Open 0건** · **Planned 0건** · **이동 없음**.

| 항목 | 80차 관측 | 조치 |
|------|----------|------|
| **baseline** | FE **`0a07799`** · BE **`1812165`** · **5+4 ahead** · WT **CLEAN** · **44 path·38 page** | ROADMAP CURRENT BASELINE 갱신 |
| **US-M03/G22** | `/billing/reports/*`·`/billing/calculator` @ `dbf485e` · E2E @ `0a07799` | US-M03 **P1 `[x]`** · G22 **닫힘** |
| **모듈 커버** | **72.5%** (68.7%→+3.8pp, BNK-16 코드 실측) | REQUIREMENTS §1-5-2 KPI 갱신 |
| **BNK-16** | 이지케어 **9,306** · FAQ payroll+직원 **37%** lock-in · 7-2-1·7-9 **Could** | REQUIREMENTS·ROADMAP W1~2 갱신 |
| **G7 NHIS** | 케어포 **성공/오류/대기 3상태** vs ogada 2상태 | US-G06·G7 **P0** — `### 추가 질문` 기록 |
| **US-J02** | `pilotPageFlows` E2E @ `0a07799` | fetch-mock E2E **진전** · live E2E 잔여 |
| **v2 G21** | branch guard @ `1812165` | backend bleed 지속 · `/visits` UI **merge 후** |
| **QA** | Open **0** · Planned **0** | 신규 태스크 **없음** |

**coder 다음 액션 (80차)**: ① **tester develop→test merge(5+4)** — v1.2.1 `merge_status: ready` ② **G7 NHIS** 샘플 + 대기상태 UX ③ **G13** 입금→미납 E2E ④ US-J02 live E2E ⑤ v1.3 live E2E run.

### [PLA] QA 피드백 반영 (2026-06-09, 79차 — TSR 106·107 · G14 GET API 닫힘)

> **79차 자동 기획 동기화** — TSR 106(backend G14)·107(frontend US-J02 필드 정합). **QA Open 0건** · **Planned 0건** · **이동 없음**.

| 항목 | 79차 관측 | 조치 |
|------|----------|------|
| **baseline** | FE **`465bdae`** · BE **`15e41e3`** · **3+3 ahead** · WT **CLEAN** | ROADMAP CURRENT BASELINE 갱신 |
| **G14 GET API** | `LtcGradeHistoryService`·`ClientController` @ `15e41e3` · **262/262 PASS** | US-M01 **P0 `[x]`** · ROADMAP **`merge_status: ready`** |
| **US-J02** | `465bdae` guardian billing live API 필드 정합 | P1 잔여 — live E2E·명세 탭 통합 |
| **v2 G21 bleed** | `@d768820` lineage (V53·`/visits`) develop-only | v1.2.1 merge **후** `/visits` UI 착수 |
| **BNK-13·14** | 7-6~7-10 리포트 · ~68.7% · 1-3=기초평가 | **US-M03 P1** 유지 |
| **QA** | Open **0** · Planned **0** | 신규 태스크 **없음** |

**coder 다음 액션 (79차)**: ① **tester develop→test merge(3+3)** — v1.2.1 `merge_status: ready` ② v1.3 live E2E run ③ G7 NHIS ④ US-M03 P1 ⑤ US-J02·G13 E2E.

### [PLA] QA 피드백 반영 (2026-06-09, 78차 — BNK-13·14 재확인 · baseline 불변)

> **78차 자동 기획 동기화** — BNK-13(func.php 106 leaf·7-x 1:1)·BNK-14 git 실측 재확인. **QA Open 0건** · **Planned 0건** · **이동 없음**.

| 항목 | 78차 관측 | 조치 |
|------|----------|------|
| **baseline** | FE **`6d0a03a`** · BE **`d768820`** · **2+2 ahead** · WT **CLEAN** | **77차와 동일** — ROADMAP CURRENT BASELINE 유지 |
| **BNK-14** | US-M02 ✅ · G14 GET API **미구현** · **~68.7%** | v1.2.1 P0 **유일 잔여** — 결정 92 |
| **BNK-13** | func.php **106 leaf** · 7-1~7-3 ogada Route **✅** · **7-6~7-10 ❌** | **US-M03**(G22) v1.2.1 **P1** — ROADMAP·USER_STORIES 유지 |
| **케어포 1-3 정정** | **1-3=기초평가** · 보호자=1-1 내장 탭 | ogada `/guardians` **분리 Route 차별** — 통합 UX는 후속 |
| **G21 RFID** | 이지케어 FAQ 21647 | v2 Epic V — backend **`d768820`** 선행 완료 · UI 잔여 |
| **QA** | Open **0** · Planned **0** | 신규 태스크 **없음** |

**coder 다음 액션 (78차, superseded by 79차)**: ① **G14 GET API** ② P0 `[x]` → merge(4) ③ v1.3 live E2E ④ G7 NHIS ⑤ US-M03 P1.

### [PLN] 사용자 운영 확정 (2026-06-09, 결정 94)

| # | 항목 | 결정 |
|---|------|------|
| 1 | 요양·목욕 리포트 (3-3~3-7) | **v3.1 Must** — §3-5-a |
| 2 | 프로그램 그룹·리포트 (5-3~5-10) | **v3.1 Must** — §3-6-a |
| 3 | 위생·점검·시설운영일지 (6-2~6-4) | **v3.1 Must** — §3-14 (Won't 철회) |
| 4 | 직원 HR (8-2~8-13) | **v3 Must** — §3-8-a |
| 5 | 11장 직원 급여대장 | v3 G4 회계 모듈 (결정 94 범위 외) |

**coder 다음 티켓 (결정 94 후속)**: v3 merge-blocking 잔여 → **v3.1 DBA**(`bathing_*`·`program_groups`·`safety_checks`) → API_SPEC → FE route.

### [PLN] 사용자 운영 확정 (2026-06-09, 결정 92)

| # | 항목 | 결정 |
|---|------|------|
| 1 | 파이프라인 주기 | ~~10초~~ → **15분** (`AGENT_INTERVAL_SECONDS=900`, 결정 93) |
| 2 | v1.2.1 P0 구현 순서 | **① US-M02 ✅** @ `6d0a03a` → **② US-M01 GET API** (G14) |
| 3 | develop→test merge | **P0(US-M01 GET API) 완료 후** — US-M01 완료 기준 `[x]` 충족 시에만 `merge_status: ready` · **지금 merge/push 금지** |

**coder 다음 티켓 (결정 92 + 81차)**:
1. **G7 FE 커밋** — `NhisReconciliationTable`·`Badge` WT 4 files → clean
2. **tester merge** — develop→test **6+5 commits** (FE `371794f`·BE `4cc328d`) · v1.2.1 **`merge_status: ready`**
3. **G7 NHIS** — 파일럿 샘플 + **3상태 UX** 완료 (BE `PENDING_REVIEW` ✅)
4. **(P1) US-J02·G13** — 보호자 명세 live E2E · 입금→미납 상태전이
5. v1.3 live E2E run(결정 73)
6. Epic V E2E·공단 import — `/visits` @ `371794f` partial

---

### [PLN] 사용자 기획 확정 — **2개월 완성 스프린트** (2026-06-09, 결정 91)

> **완성 목표: 2026-08-09 (8주)** · 방문요양→**v2** · 회계·시설→**v3** (결정 90 4주→8주 연장)

| 주차 | 기간 | 버전 | 핵심 deliverable |
|------|------|------|-----------------|
| **W1~2** | 6/9~6/22 | v1.2.1 | G14 · G22 · **US-M02-b ✅** · **US-J03-h ✅** · merge(11+6)·BE+FE WT clean · G7 샘플 · G13 E2E · v1.3 live E2E |
| **W3~4** | 6/23~7/6 | **v2** | **방문요양** `/visits` · plan/billing · 보호자·CMS·방문체크인 |
| **W5~6** | 7/7~7/20 | **v3** | staff/meals · **`/finance/ledger`** · **`/finance/payroll`** · 자동분개 |
| **W7~8** | 7/21~8/9 | **v3** | **시설급여** `/facility/*` · 욕창·배설 · 통합 E2E · merge ready |

| 모듈 | 버전 | 결정 |
|------|------|------|
| 방문요양 (G21) | **v2** | 결정 90 (v4-A 철회) |
| 재무회계 (G4) | **v3** | 결정 90 (v4-C 철회) |
| 시설급여 (G20) | **v3** | W4 (1개월 완성 포함) |
| v4 | **폐기** | v2·v3 흡수 |

**MVP 제외 (v3.1)**: 평가 서식 80종 · 통장 OpenAPI · RFID

---

### [PLN] 사용자 기획 확정 — **전체 ERP 범위** (2026-06-09, 결정 89)

> **결정 76·81 철회**: 주야간만 → **시설급여·방문요양·재무회계 포함** 통합 ERP.  
> **→ 결정 90으로 일정 압축**: v4 폐기 · 4주 완성.

---

### [PLN] 사용자 기획 확정 — 파일럿 2주차 전체 포함 (2026-06-09, 결정 76~81)

> **5번 수정**: 파일럿 2주차 — QR만 → **6항목 전부** (결정 80).

| 주차 | 시나리오 | 담당 | 선행 |
|------|----------|------|------|
| **1주차** | P1 이용자+보호자 · P2 수기출석 · P3 건강기록 | 센터장·요보사 | — |
| **2주차 D1~2** | P5 대시보드 실데이터·HQ 비교 | 센터장 | 1주차 출석·건강 데이터 |
| **2주차 D2~3** | P4 QR 출석 (B방식) | 요보사·보호자 | 지점 QR 생성 |
| **2주차 D3~4** | P9 이동서비스 배차·지도 (v1.3-A) | 센터장(hq) | 이용자 픽업 프로필 |
| **2주차 D4~5** | P10 보호자 초대·명세/기록 열람 (J01/J02) | 센터장 | 보호자 연결·이메일 채널(결정 59) |
| **2주차 D5~6** | P6–P8 월말 청구·NHIS import | 센터장 | 출석·등급·수가표 |
| **2주차 D6~7** | P11 본인부담 입금·미납 (부분입금) | 센터장 | 청구서 CONFIRMED |

**구현 깊이**: **8주 완성 (결정 91)** — v2 방문요양 · v3 회계·시설 · ~85% 패리티.

| 정책 | 결정 (82~85) |
|------|----------------|
| G7 NHIS 샘플 | 공개 실파일 **없음** → 합성 fixture 개발 · 파일럿 실파일 최종 검증 |
| 과납 | **불허** |
| J01 채널 | **이메일** (SMS **v3**) |
| 초대 만료 | **7일** |
| CMS (v2) | **센터 자체 효성CMS + ogada 연동** — ogada 요금 0원 |
| TSP (v1.3-B) | **다중 차량 VRP** — **담당 안정성(O1)·거리 공정성(O2)** soft 우선 · 총 거리(O3) 다음 (결정 74 · §3-13-9) |

---

### [PLA] QA 피드백 반영 (2026-06-09, 77차 — BNK-14 재확인 + backend v2/G21 bleed)

> **77차 자동 기획 동기화** — BNK-14 재확인·backend `d768820` v2/G21 선행 커밋 관측. **QA Open 0건** · **Planned 0건**.

| 항목 | 77차 관측 | 조치 |
|------|----------|------|
| **backend bleed** | develop **`d768820`**(+1 vs `2012945`: v2/G21 visit schedules) · **`257/257 PASS`** · **2 ahead of test** | ROADMAP v2 G21 backend **`[x]`** @ `d768820` · **결정 92** merge gate **v1.2.1 P0 선행** 명시 |
| **BNK-14 불변** | US-M02 **닫힘** · G14 GET API **미구현** · **~68.7%** | v1.2.1 **in_progress** 유지 |
| **G21 이중 일정** | V53 `schedule_kind`·`paired_schedule_id`·`createPairedBillingSchedule` | backend ✅ · `/visits` UI·import **잔여** |
| **frontend** | **`6d0a03a`** · **2 ahead** · **225/72 PASS** | G14 GET API **P0 유일 잔여** |

**coder 다음 액션 (77차)**: ① **G14 GET API**(US-M01) — **결정 92 최우선** ② P0 `[x]` → merge(4 commits) ③ v1.3 live E2E ④ G7 NHIS ⑤ US-M03 P1 · v2 `/visits` UI는 **v1.2.1 P0 후**.

### [PLA] QA 피드백 반영 (2026-06-09, 76차 — BNK-14 + TSR 105 + v1.2.1 진전)

> **76차 자동 기획 동기화** — BNK-14 git 실측·TSR 105. **QA Open 0건** · **Planned 0건**.

| 항목 | 76차 관측 | 조치 |
|------|----------|------|
| **BNK-14 baseline** | frontend **`6d0a03a`** · backend **`2012945`** · **39 Route·36 page** · **~68.7%** | ROADMAP·REQUIREMENTS §1-5-2 갱신 |
| **US-M02** | `dashboardSummary.js`·5위젯·`BranchCompareChart` @ `6d0a03a` | ROADMAP v1.2.1 **P0-1 `[x]`** |
| **US-M01/G14** | UI+DB(V48) ✅ · **`GET /ltc-grade-history` ABSENT** | ROADMAP·API_SPEC **P0 유일 잔여** |
| **G22 7-6~10** | 케어포 7장 리포트 5건 갭 | **US-M03** v1.2.1 P1 신설 |
| **G21 RFID** | 이지케어 FAQ 21647 | v2 방문요양 Must — REQUIREMENTS G21 유지 |
| **TSR 105** | test `c7c8f07` 217/70 · develop `6d0a03a` 225/72 · **2 ahead** | merge gate **P0 후** |

**coder 다음 액션 (76차)**: ① **G14 GET API** (US-M01) ② P0 `[x]` → tester merge(3 commits) ③ v1.3 live E2E ④ G7 NHIS ⑤ US-M03 P1.

---

### [PLN] QA 피드백 반영 (2026-06-09, 75차 — QA-B12·SEC-D14 Fixed + v1.2.1 in_progress + API_SPEC G14)

> **75차 자동 기획 동기화** — planner git 실측으로 merge gate 해소 확인. **QA Open 0건** · **Planned 0건**.

| 항목 | 75차 관측 | 조치 |
|------|----------|------|
| **QA-B12 push gap** | backend develop/test/origin **`598d108`** · frontend develop/test/origin **`c7c8f07`** · **0 ahead** | Planned→**Fixed** · SEC-D14 동반 Fixed |
| **frontend merge(22)** | test `c510f5c`→**`c7c8f07`**(v1.3-A·UXD-55 포함) | merge gate **해소** |
| **v1.2.1 활성화** | merge gate 완료 | ROADMAP **`status: in_progress`** · frontend 단일 활성 |
| **API_SPEC G14** | `ltc_grade_history` 명세 부재 | **§4-2** 신설 — US-M01 coder 계약 |
| **backend WT 13** | regions·V51/V52 WIP | commit/revert 게이트 **잔여** |
| **BNK-10~12** | 74차 불변 | G14·US-M02·G7 NHIS 샘플만 coder 착수 |

**coder 다음 액션 (75차, 우선순위)**: ① **v1.2.1** US-M01 G14(`ltc_grade_history`·API_SPEC §4-2) ② US-M02 대시보드/HQ BranchCompare ③ backend WT 13 정리 ④ v1.3 live E2E run(결정 73) ⑤ G7 NHIS 샘플(파일럿).

---

### [COD] 코더 질문 — frontend 활성 버전/HEAD 실측 (2026-06-09, 76차)

- **실측(76차)**: backend develop **`2012945`** · frontend develop **`6d0a03a`** · WT **CLEAN** · test 대비 **1+2 ahead**.
- **활성 frontend 버전**: **v1.2.1 `in_progress`** — **G14 GET API** 1건 잔여 (US-M02 ✅).
- **coder 다음 티켓**: ① **US-M01 GET API** ② P0 완료 후 tester merge.

### [COD] 코더 질문 — frontend 활성 버전/HEAD 실측 (2026-06-09, 75차 갱신 → **결정 92**)

### [COD] 코더 질문 — frontend 활성 버전/HEAD 실측 (2026-06-09, 74차 — **75차 갱신**)

- **실측(74차 planner git)**: `src/frontend` develop **`c7c8f07`** · test **`c510f5c`** · WT **CLEAN** · **22 ahead**.
- **73차 drift 해소**: ROADMAP·PLAN_NOTES·QA baseline **`c7c8f07`** 기준 재동기화(BNK-12).
- **활성 frontend 버전**: **없음** — v1.2.1 **planned**(merge gate 후) · v3 frontend **보류**.
- **coder 다음 티켓**: ① tester **origin/test push(QA-B12)** ② frontend merge(22) ③ **v1.2.1** US-M01 G14·US-M02 실데이터 — merge gate 후.

### [PLN] QA 피드백 반영 (2026-06-09, 74차 — BNK-10·11·12 + TSR 102·103 + v1.2.1 + SEC-D14 Planned + Open 0건)

> **74차 자동 기획 동기화** — BNK-10(이지케어 ERP)·BNK-11(케어포 demo-work)·BNK-12(baseline·가격) + TSR 102·103. **QA Open 0건** — SEC-D14·QA-B12 **Planned**.

| 항목 | 74차 관측 | 조치 |
|------|----------|------|
| **BNK-10 이지케어** | 9,298개소 · **계획/청구 이중 일정** · 급여·4대보험 lock-in | G4 Won't v1 유지 · G8 EZCARE 초대 패턴 · **#45** 이중 일정 UX 검토(방문 확장 시) |
| **BNK-11 demo-work** | 시설급여 120메뉴 · **이동서비스 없음** · 주야간=func.php 109항목 | 벤치마크 **정본=func.php** · **G20** 시설특화 Won't v1 |
| **BNK-12 baseline** | frontend **`c7c8f07`** 40 Route·35 page · **~74–78% KPI PASS** | REQUIREMENTS §1-5-2·ROADMAP baseline 갱신 |
| **BNK-12 v1.2 잔여** | G14 등급이력 · US-M02 대시보드 실데이터 | **v1.2.1** ROADMAP 신설 · US-M01·M02 태스크 |
| **TSR 102 backend** | test `@598d108` 246/246 · WT **DIRTY 13** | regions/V51/V52 WIP — commit/revert 게이트 |
| **TSR 103 frontend** | **`c7c8f07`** UXD-55 US-J02 · **217/70 PASS** · **22 ahead** | v1.2.1 US-J02 partial · merge(22) BLOCK |
| **SEC-D14** | origin/test STALE · QA-B12 동반 | Open→Planned · push 후 Fixed |
| **G7 NHIS** | 파일럿 샘플 미확보 | v1.2.1 **즉시** · #27 유지 |

**coder 다음 액션 (74차, 우선순위)**: ① **tester: origin/test push(QA-B12)** ② backend WT 13 files 정리 ③ **frontend merge(22)** ④ **v1.2.1** G14·US-M02 (merge gate 후) ⑤ v1.3 live E2E run ⑥ G7 NHIS 샘플(파일럿).

---

### [COD] 현재 baseline (89차 git 실측 — 단일 진실 원천)

| stream | develop HEAD | test HEAD | WT | ahead of test | 비고 |
|--------|--------------|-----------|-----|---------------|------|
| backend | **`0ebe945`** | **`598d108`** | **CLEAN** | **24** | visit pilot E2E·overdue notify lifecycle tests · **`334/334 PASS`** |
| frontend | **`14e9066`** | **`c7c8f07`** | **CLEAN** | **28** | US-L02 pagination·reminder E2E·timestamp sync · **`340/97 PASS`** · **45 path·39 page** |

> **폐기 SHA**: `d5654c0`·`e5fd48d`·`428ba7d`·`4be0938` — checkout 재현 **금지**.  
> **활성 버전**: **v1.2.1 `in_progress`** · **v2 `in_progress`** · **`merge_status: ready`** — P0+G22+G7 UX+US-M02-b+US-J03-h `[x]` (결정 92 · ★ **FULLY UNBLOCKED**).  
> **89차 COD 조치**: tester merge(**28+24=52**) → P1(G7 실파일·G2 이메일 실발송·G13 cross-page·G21 통합 E2E·live E2E).

### [COD] 현재 baseline (88차 git 실측 — **superseded by 89차**)

| stream | develop HEAD | test HEAD | WT | ahead of test | 비고 |
|--------|--------------|-----------|-----|---------------|------|
| backend | **`3e4d3e6`** | **`598d108`** | **CLEAN** | **19** | G21 확정차단·notify API·paired cancel/sync · **`329/329 PASS`** |
| frontend | **`311c7c0`** | **`c7c8f07`** | **CLEAN** | **21** | G2 notify UI·G21 import·paired cancel UX·QR branch-scoped · **`326/93 PASS`** · **45 path·39 page** |

### [COD] 현재 baseline (87차 git 실측 — **superseded by 88차**)

| stream | develop HEAD | test HEAD | WT | ahead of test | 비고 |
|--------|--------------|-----------|-----|---------------|------|
| backend | **`ee3fa3a`** | **`598d108`** | **CLEAN** | **12** | G21 NHIS visit import·HOME_VISIT guard · **`306/306 PASS`** |
| frontend | **`e1320f4`** | **`c7c8f07`** | **CLEAN** | **15** | SEC-D17 apiFetch·formErrors/http·UXD-62 · **`311/91 PASS`** · **45 path·39 page** |

### [COD] 현재 baseline (85차 git 실측 — **superseded by 88차**)

| stream | develop HEAD | test HEAD | WT | ahead of test | 비고 |
|--------|--------------|-----------|-----|---------------|------|
| backend | **`dd49204`** | **`598d108`** | **DIRTY 26** | **6** | G7 fixture @ `dd49204` + v3 meals/programs·V55·Client/Visit WIP |
| frontend | **`e39164d`** | **`c7c8f07`** | **DIRTY 9** | **11** | US-J03-h @ `e39164d` + v3 meals/programs WIP · **45 path·39 page** |

> **폐기 SHA**: `d5654c0`·`e5fd48d`·`428ba7d`·`4be0938` — checkout 재현 **금지**.  
> **활성 버전**: **v1.2.1 `in_progress`** · **v2 `in_progress`** · **`merge_status: ready`** — P0+G22+G7 UX+US-M02-b+US-J03-h `[x]` (결정 92 · **BE+FE WT clean 선행**).  
> **85차 COD 조치**: BE+FE WT clean → tester merge(**11+6**) → P1(G7 실파일·live E2E·G11·알림톡 실발송 v1.1).

### [COD] 현재 baseline (84차 git 실측 — **superseded by 85차**)

| stream | develop HEAD | test HEAD | WT | ahead of test | 비고 |
|--------|--------------|-----------|-----|---------------|------|
| backend | **`dd49204`** | **`598d108`** | **CLEAN** | **6** | G7 V54+fixture tests @ `dd49204` + v2/G21 lineage |
| frontend | **`16402b2`** | **`c7c8f07`** | **CLEAN** | **8** | G7 UX @ `fbb0b7a`/`16402b2` · Epic V `/visits` · **`267/81 PASS`** · **45 path·39 page** |

> **폐기 SHA**: `d5654c0`·`e5fd48d`·`428ba7d`·`4be0938` — checkout 재현 **금지**.  
> **활성 버전**: **v1.2.1 `in_progress`** · **v2 `in_progress`**(Epic V partial) · **`merge_status: ready`** — P0+G22+G7 UX `[x]` (결정 92 · TSR 113 FULLY UNBLOCKED).  
> **82차 COD 조치**: tester merge(**8+6**) → P1(G7 실파일·G13·live E2E).

### [COD] 현재 baseline (81차 git 실측 — **superseded by 82차**)

| stream | develop HEAD | test HEAD | WT | ahead of test | 비고 |
|--------|--------------|-----------|-----|---------------|------|
| backend | **`4cc328d`** | **`598d108`** | **CLEAN** | **5** | G7 `PENDING_REVIEW` V54 @ `4cc328d` + v2/G21 lineage |
| frontend | **`371794f`** | **`c7c8f07`** | **DIRTY 4** | **6** | Epic V `/visits` @ `371794f` + G7 NHIS UI WIP · **`259/80 PASS`** · **45 path·39 page** |

> **폐기 SHA**: `d5654c0`·`e5fd48d`·`428ba7d`·`4be0938` — checkout 재현 **금지**.  
> **활성 버전**: **v1.2.1 `in_progress`** · **v2 `in_progress`**(Epic V partial) · **`merge_status: ready`** — P0 `[x]` + US-M03 `[x]` (결정 92).  
> **81차 COD 조치**: G7 FE 커밋(WT clean) → tester merge(**6+5**) → P1(G7 샘플·G13·live E2E).

### [COD] 현재 baseline (80차 git 실측 — **superseded by 81차**)

| stream | develop HEAD | test HEAD | WT | ahead of test | 비고 |
|--------|--------------|-----------|-----|---------------|------|
| backend | **`1812165`** | **`598d108`** | **CLEAN** | **4** | v2/G21 lineage + G14 @ `15e41e3` + branch guard @ `1812165` |
| frontend | **`0a07799`** | **`c7c8f07`** | **CLEAN** | **5** | US-M03 @ `dbf485e` + US-J02·US-M03 E2E @ `0a07799` · **`240/76 PASS`** · **44 path·38 page** |

> **폐기 SHA**: `d5654c0`·`e5fd48d`·`428ba7d`·`4be0938` — checkout 재현 **금지**.  
> **활성 버전**: **v1.2.1 `in_progress`** · **`merge_status: ready`** — P0 `[x]` + US-M03 `[x]` (결정 92).  
> **80차 COD 조치**: tester develop→test merge(**5+4**) → P1(G7·G13·live E2E).

### [COD] 현재 baseline (79차 git 실측 — **superseded by 81차**)

| stream | develop HEAD | test HEAD | WT | ahead of test | 비고 |
|--------|--------------|-----------|-----|---------------|------|
| backend | **`15e41e3`** | **`598d108`** | **CLEAN** | **3** | `d768820` v2/G21 + **`15e41e3` G14 GET API** · **`262/262 PASS`** |
| frontend | **`465bdae`** | **`c7c8f07`** | **CLEAN** | **3** | US-M02·US-M01 @ `6d0a03a` + US-J02 필드 정합 @ `465bdae` · **`225/72 PASS`** |

> **폐기 SHA**: `d5654c0`·`e5fd48d`·`428ba7d`·`4be0938` — checkout 재현 **금지**.  
> **활성 버전**: **v1.2.1 `in_progress`** · **`merge_status: ready`** — P0 `[x]` (결정 92).  
> **79차 COD 조치**: tester develop→test merge(**3+3**) → P1(US-M03·G7·live E2E).

### [COD] 현재 baseline (77차 git 실측 — **superseded by 79차**)

| stream | develop HEAD | test HEAD | WT | ahead of test | 비고 |
|--------|--------------|-----------|-----|---------------|------|
| backend | **`d768820`** | **`598d108`** | **CLEAN** | **2** | `2012945` regions + **`d768820` v2/G21 visits** · **`257/257 PASS`** |
| frontend | **`6d0a03a`** | **`c7c8f07`** | **CLEAN** | **2** | US-M02·US-M01 UI @ `6d0a03a` · **`225/72 PASS`** · **~68.7%** |

> **폐기 SHA**: `d5654c0`·`e5fd48d`·`428ba7d`·`4be0938` — checkout 재현 **금지**.  
> **활성 버전**: **v1.2.1 `in_progress`** — **G14 GET API** 1건 잔여(결정 92). v2 G21 backend **선행 포함** — frontend `/visits`는 **P0 후**.  
> **77차 COD 조치**: US-M01 GET API → P0 `[x]` → merge(**4 commits**).

### [COD] 현재 baseline (76차 git 실측 — **superseded by 77차**)

| stream | develop HEAD | test HEAD | WT | ahead of test | 비고 |
|--------|--------------|-----------|-----|---------------|------|
| backend | **`2012945`** | **`598d108`** | **CLEAN** | **1** | regions V51·branch V52 · V50 copay |
| frontend | **`6d0a03a`** | **`c7c8f07`** | **CLEAN** | **2** | US-M02·US-M01 UI @ `6d0a03a` · **`225/72 PASS`** · **~68.7%** |

### [COD] 현재 baseline (75차 git 실측 — **superseded by 77차**)

| stream | develop HEAD | test HEAD | origin/test | WT | ahead of test | 비고 |
|--------|--------------|-----------|-------------|-----|---------------|------|
| backend | **`598d108`** | **`598d108`**(local) | **`2799e29`** STALE | **DIRTY 13** | **26** vs origin | v2 copay V50 · **QA-B12** |
| frontend | **`c7c8f07`** | `c510f5c` | (submodule) | **CLEAN** | **22** | UXD-55 @ `c7c8f07` |

### [COD] 코더 질문 — frontend 활성 버전/HEAD 실측 (2026-06-09, 73차 — **74차 갱신**)

- **실측(73차 planner git)**: `src/frontend` develop **`7cd9293`** · test **`c510f5c`** · WT **CLEAN** · **49 ahead**.
- **72차 문서 drift 해소**: ROADMAP·PLAN_NOTES·QA baseline을 **`7cd9293`** 기준으로 재동기화.
- **활성 frontend 버전**: **없음** — v1.3 `status: done`/`merge_status: merged`(local) · v3 frontend **보류**(merge-blocking 잔여).
- **coder 다음 티켓**: merge gate 해소 전 **신규 frontend 구현 착수 금지** — tester **origin/test push(QA-B12)** + frontend merge(49) 선행.

### [COD] 코더 질문 — frontend 착수 가능 시점 확인 (2026-06-09, 73차 기준)

- **관측**: ROADMAP·QA_FEEDBACK 기준 frontend 활성 `in_progress` 버전 부재, develop **`7cd9293`** CLEAN·test 대비 **49 ahead**. QA-B12(origin/test push)·SEC-D14·frontend merge(49) 해소 전 신규 작업 금지 지침 유지.
- **제약**: merge/push는 tester/operation 전담, coder는 `src/frontend` develop에서만 작업 가능(rules §8/§10-1).
- **요청**: planner가 다음 frontend `in_progress` 버전/티켓을 지정하거나 v3(Staff API·프로그램 사진 등) 재개 시점을 명시해 달라. 지정 전까지 coder는 frontend 변경을 보류한다.

---

### [PLN] QA 피드백 반영 (2026-06-09, 73차 — TSR 100·101 + QA-B12 push gap + UXD-54 + BNK-9 재확인 + Open 0건)

> **73차 자동 기획 동기화** — TSR 100차(backend)·101차(frontend) + BNK-9 재확인. **QA Open 0건** — QA-20260608-B12 **Planned**.

| 항목 | 73차 관측 | 조치 |
|------|----------|------|
| **QA-B12 push gap** | 로컬 test **`598d108`**(=develop) · **origin/test STALE `2799e29`** — **26 ahead·미푸시** | ROADMAP 이관 규율 **11항** · **`git_merge_to_test.sh` push**(tester 전담) → Fixed |
| **backend local merge** | TSR 100: `32575aa` lineage **243/243 PASS** — v1 + v1.3-A + v3 test 반영 | v1.3 **`merge_status: merged`(local)** · operation은 origin push 후 |
| **backend develop +1** | **`598d108`** — v2 copay payment·V50·`BillingServiceTest`+198 | Epic L backend API **부분 진전** · 차기 merge 사이클 |
| **frontend HEAD** | **`7cd9293`**(+1 vs `e641f62`: UXD-54) · **`npm test` 214/69** · **49 ahead** | US-UX-04 UXD-54 반영 · frontend merge(49) BLOCK |
| **UXD-54** | `BranchScopeNotice` → QrGeneratePage·TransportPage·TransportRunNew/Detail | USER_STORIES US-UX-04 갱신 |
| **BNK-9** | Directions·러-1~4·G17~G19 — **47~72차 반영 불변** | 변경 없음 · #44 law.go.kr 잔여 |
| **활성 버전** | frontend 단일 `in_progress` **없음** | 65~72차 결정 **유지** |

**coder 다음 액션 (73차, 우선순위)**: ① **tester: origin/test push(QA-B12)** — coder push 금지 ② **SEC-D14(origin) 재검증** ③ **frontend merge(49)** ④ **v1.3 live E2E run**(post-merge·`LIVE_E2E=1`) ⑤ v3 StaffPage API·프로그램 사진(게이트 후) ⑥ v2 Epic L frontend UI·live Solapi.

---

### [COD] 현재 baseline (73차 git 실측 — 단일 진실 원천)

| stream | develop HEAD | test HEAD | origin/test | WT | ahead of origin/test | 비고 |
|--------|--------------|-----------|-------------|-----|----------------------|------|
| backend | **`598d108`** | **`598d108`**(local) | **`2799e29`** STALE | **CLEAN** | **26** (미푸시) | v2 copay payment @ `598d108` · local merge PASS · **QA-B12** |
| frontend | **`7cd9293`** | `c510f5c` | (submodule) | **CLEAN** | **49** vs test | UXD-54 @ `7cd9293` · **`npm test` 214/69** |

> **폐기 SHA**: `d5654c0`·`e5fd48d`·`428ba7d`·`4be0938` — checkout 재현 **금지**.  
> **활성 frontend 버전 없음**: v1.3 local merged · v2 backend-only bleed · v3 frontend **보류**.  
> **73차 COD 조치**: merge gate 해소 전 frontend 신규 착수 **보류**.

---

### [COD] 코더 질문 — frontend 활성 버전/HEAD 실측 불일치 (2026-06-08, 72차 — **73차 해소**)

- **실측(현재 워크스페이스 주입값)**: `src/frontend` develop **`7cd9293`** · test **`c510f5c`** · WT **CLEAN**.
- **문서 불일치**: `ROADMAP`/`QA_FEEDBACK`/`PLAN_NOTES` 최신 기록은 frontend develop **`e641f62`** 기준으로 `merge_status: ready`를 유지 중.
- **판단**: frontend 단일 `in_progress` 버전이 없어 신규 구현 범위를 확정할 수 없으므로, v1.3 merge 실행 주체(테스터)와 v3 frontend 재개 시점을 planner가 먼저 확정해야 함.
- **요청**: planner가 ① frontend 실측 HEAD 기준 재동기화(`7cd9293` vs `e641f62`) ② frontend 활성 버전(없음 유지 vs v3 승격) ③ coder 다음 구현 티켓(US/버전)을 `ROADMAP`에 단일값으로 확정해 달라.

---

### [PLN] QA 피드백 반영 (2026-06-08, 72차 — TSR 98·99차 + masking 단위테스트 + UXD-53 + BNK-9 재확인 + Open 0건)

> **72차 자동 기획 동기화** — TSR 98차(backend)·99차(frontend) 기준 planner git 실측 + BNK-9 재확인. **QA Open 0건** — 70차 Planned BLOCK 갱신.

| 항목 | 72차 관측 | 조치 |
|------|----------|------|
| **backend HEAD** | **`32575aa`**(+1 vs `c7941e9`) · WT **CLEAN** · **`mvn test` 243/243**(+2) · **25 ahead** | `TransportServiceTest` pickup contact masking 단위 테스트 — SEC-D9 회귀 안전망 · ROADMAP v1.3 완료 기준 **`[x]`** |
| **frontend HEAD** | **`e641f62`**(+2 vs `1d910c2`) · test **`c510f5c`** · WT **CLEAN** · **`npm test` 212/69 PASS**(+4/+1) · **780 modules 3청크**(max **367 kB**) · **40 Route·51 page** | UXD-53 `BranchScopeNotice` @ `0d36e30` · `pilotPageFlows` US-E01/E05 E2E @ `e641f62` |
| **UXD-53 지점 스코프** | `BranchScopeNotice`(`role="status"`) — AttendancePage·AttendanceStatsPage·QrGeneratePage·Transport 연동 | USER_STORIES **US-UX-04** 신설 · US-E01/E02/E05 인수 조건 보강 |
| **BNK-9** | Directions·러-1~4·G17~G19 — **47~71차 반영 불변** | 변경 없음 · #44 law.go.kr 잔여 |
| **활성 버전** | v1.3 `status: done`/`merge_status: ready` · frontend 단일 `in_progress` **없음** · v3 frontend **보류** | 65~71차 결정 **유지** |
| **merge gap** | backend **25 ahead** · frontend develop **20 ahead** | SEC-D14·B03 **backend merge 잔여** + v1.3 live E2E run |

**coder 다음 액션 (72차, 우선순위)**: ① **backend merge(25)** ② **B03/SEC-D14(backend)** test 재검증 ③ **frontend merge(20)** ④ **v1.3 live E2E run**(post-merge·`LIVE_E2E=1`, 결정 73) ⑤ v3 StaffPage API·프로그램 사진(merge gate 후) ⑥ v2 알림 프론트 UI·live Solapi.

---

### [COD] 현재 baseline (72차 git 실측 — 단일 진실 원천)

| stream | develop HEAD | test HEAD | WT | ahead of test | 비고 |
|--------|--------------|-----------|-----|---------------|------|
| backend | **`32575aa`** | `2799e29` | **CLEAN** | **25** | masking 단위테스트 @ `32575aa` · pickup masking API @ `c7941e9`+ · **`mvn test` 243/243** |
| frontend | **`e641f62`** | `c510f5c` | **CLEAN** | **20** | UXD-53 `BranchScopeNotice` @ `0d36e30`+ · pilotPageFlows E01/E05 E2E @ `e641f62` · **`npm test` 212/69** · **40 Route·51 page** |

> **폐기 SHA**: `d5654c0`·`e5fd48d`·`428ba7d`·`4be0938` — checkout 재현 **금지**.  
> **활성 frontend 버전 없음**: v1.3-A `merge_status: ready`(ROADMAP) · v2 backend-only `in_progress` · v3 frontend **보류**(merge-blocking: 프로그램 사진·Staff API).  
> **72차 COD 조치**: `TransportServiceTest` masking +2 @Test · UXD-53 `pilotPageFlows` US-E01/E05 E2E @ `e641f62`.

**coder 다음 액션 (72차)**: ① **backend merge(25)** ② **frontend merge(20)** — tester 스크립트 ③ **v1.3 live E2E run**(post-merge·`LIVE_E2E=1`) ④ planner: v3 frontend 재개 시점 확정 ⑤ v3 StaffPage API·프로그램 사진(게이트 후).

### [COD] 코더 질문 — frontend 활성 버전 없음 (2026-06-08, 71차)

- **실측**: `src/frontend` develop **`0d36e30`** · WT **CLEAN** · test 대비 **19 ahead**.
- **관측**: ROADMAP v1.3 `status: done`/`merge_status: merged` · v2 `stream: backend` only · v3 frontend merge-blocking 3건 미완 — **단일 `in_progress` frontend 버전 부재**.
- **71차 조치**: UXD-53(US-E01/E05/E03/T03 a11y) @ `0d36e30` **유지** · `pilotPageFlows` BranchScopeNotice E2E **추가**.
- **planner 협의 요청**: v3 frontend(프로그램 사진·Staff API) 재개를 v1.3 develop→test merge **후**로 유지할지, 또는 v3를 frontend 단일 활성으로 승격할지 **확정 필요**.

---

### [COD] 현재 baseline (70차 git 실측 — 단일 진실 원천)

| stream | develop HEAD | test HEAD | WT | ahead of test | 비고 |
|--------|--------------|-----------|-----|---------------|------|
| backend | **`c7941e9`** | `2799e29` | **CLEAN** | **24** | pickup contact masking @ `c7941e9` · address masking @ `e7d4cf6`+ · transport E2E @ `f8d1b02`+ · **`mvn test` 241/241** |
| frontend | **`1d910c2`** | `c510f5c` | **CLEAN** | **18** | contact masking UI @ `37be0a3`+ · T03 E2E @ `1d910c2` · ClientForm 픽업 @ `3c55339` · live harness @ `d484206`+ · **`npm test` 208/68** · **40 Route·51 page** |

> **폐기 SHA**: `d5654c0`(TSR57)·`e5fd48d`(스켈레톤)·`428ba7d`(TSR56)·**`4be0938`**(24 route — git object 없음) — checkout 재현 **금지**.  
> **확정 파일**: `.agents/workspace_baseline.yaml` · `run_agent.py` build 시 **실측 git HEAD 자동 주입** — **70차 git 실측이 stale baseline보다 우선**.  
> **Fixed @ 70차**: transport contact masking API @ `c7941e9` **PRESENT** · UI @ `1d910c2` **PRESENT** · v1.3-A merge-blocking **충족** → ROADMAP `merge_status: ready` · live E2E **run 잔여**(결정 73 post-merge).

**coder 다음 액션 (70차)**: ① **backend merge(24)** ② **frontend merge(18)** — v1.3 `merge_status: ready` ③ **v1.3 live E2E run**(post-merge·`LIVE_E2E=1`) ④ v3 StaffPage API·프로그램 사진(v1.3 merged 후).

---

### [PLN] QA 피드백 반영 (2026-06-08, 70차 — TSR 96·97차 + transport pickup contact masking UI + BNK-9 재확인 + Open 0건)

> **70차 자동 기획 동기화** — TSR 96차(backend)·97차(frontend) 기준 planner git 실측 + BNK-9 재확인. **QA Open 0건** — 69차 Planned BLOCK 갱신.

| 항목 | 70차 관측 | 조치 |
|------|----------|------|
| **backend HEAD** | **`c7941e9`**(+1 vs `e7d4cf6`) · WT **CLEAN** · **`mvn test` 241/241** · **24 ahead** | `TransportService.maskPhone` non-HQ pickup contact masking — ROADMAP v1.3·API_SPEC §12·USER_STORIES US-T01/US-T03 **`[x]`** |
| **frontend HEAD** | **`1d910c2`**(+2 vs `3c55339`) · test **`c510f5c`** · WT **CLEAN** · **`npm test` 208/68 PASS** · **779 modules 3청크**(max **367 kB**) · **40 Route·51 page** | `TransportPickupContact`·T03 contact masking E2E @ `1d910c2` |
| **transport privacy 완성** | API 주소(`e7d4cf6`) + 연락처(`c7941e9`) · UI `TransportPickupContact`·`pilotPageFlows` T03 @ `1d910c2` | SEC-D9·PII(개인정보보호법) — DATA_RETENTION_POLICY 반영 권고 |
| **BNK-9** | Directions·러-1~4·G17~G19 — **47~69차 반영 불변** | 변경 없음 · #44 law.go.kr 잔여 |
| **merge gap** | backend **24 ahead** · frontend develop **18 ahead** | SEC-D14·B03 **backend merge 잔여** + v1.3 live E2E run |

**coder 다음 액션 (70차, 우선순위)**: ① **backend merge(24)** ② **B03/SEC-D14(backend)** test 재검증 ③ **frontend merge(18)** ④ **v1.3 live E2E run**(post-merge·`LIVE_E2E=1`, 결정 73) ⑤ v3 StaffPage API·프로그램 사진(v1.3 gate 후) ⑥ v2 알림 프론트 UI·live Solapi.

---

### [COD] 현재 baseline (69차 git 실측 — 단일 진실 원천)

| stream | develop HEAD | test HEAD | WT | ahead of test | 비고 |
|--------|--------------|-----------|-----|---------------|------|
| backend | **`c7941e9`** | `2799e29` | **CLEAN** | **24** | pickup contact masking @ `c7941e9` · address masking @ `e7d4cf6`+ · transport E2E @ `f8d1b02`+ |
| frontend | **`37be0a3`** | `c510f5c` | **CLEAN** | **17** | contact masking UI @ `37be0a3` · ClientForm 픽업 @ `3c55339` · live harness @ `d484206`+ · **`npm test` 208/68** |

> **폐기 SHA**: `d5654c0`(TSR57)·`e5fd48d`(스켈레톤)·`428ba7d`(TSR56)·**`4be0938`**(24 route — git object 없음) — checkout 재현 **금지**.  
> **확정 파일**: `.agents/workspace_baseline.yaml` · `run_agent.py` build 시 **실측 git HEAD 자동 주입** — **69차 git 실측이 stale baseline보다 우선**.  
> **Fixed @ 69차**: transport contact masking UI @ `37be0a3` **PRESENT** · address masking API @ `e7d4cf6`+ **PRESENT** · v1.3-A merge-blocking **충족** → ROADMAP `merge_status: ready` · live E2E **run 잔여**(결정 73 post-merge).

**coder 다음 액션 (69차)**: ① **backend merge(24)** ② **frontend merge(17)** — v1.3 `merge_status: ready` ③ **v1.3 live E2E run**(post-merge·`LIVE_E2E=1`) ④ v3 StaffPage API·프로그램 사진(v1.3 merged 후).

---

### [COD] 현재 baseline (planner 68차 git 실측 — 단일 진실 원천)

| stream | develop HEAD | test HEAD | WT | ahead of test | 비고 |
|--------|--------------|-----------|-----|---------------|------|
| backend | **`e7d4cf6`** | `2799e29` | **CLEAN** | **23** | transport pickup masking non-HQ @ `e7d4cf6` · `TransportPilotServiceFlowE2eTest` @ `f8d1b02`+ · transport profile @ `1ec538b`+ · v3 meals/programs @ `dfd9be2`+ · **`mvn test` 241/241** |
| frontend | **`3c55339`** | `c510f5c` | **CLEAN** | **16** | UXD-51 FE-13/FE-14 복원 @ `2a0ef3d` · ClientForm 픽업 프로필 @ `3c55339` · FE-15 `manualChunks` @ `d484206`+ · transport live harness @ `d484206`+ · **`npm test` 203/67** · **778 modules 3청크**(max 367 kB) · **40 Route·51 page** |

> **폐기 SHA**: `d5654c0`(TSR57)·`e5fd48d`(스켈레톤)·`428ba7d`(TSR56)·**`4be0938`**(24 route — git object 없음) — checkout 재현 **금지**.  
> **확정 파일**: `.agents/workspace_baseline.yaml` · `run_agent.py` build 시 **실측 git HEAD 자동 주입** — **68차 git 실측이 stale baseline보다 우선**.  
> **Fixed @ 68차**: transport pickup masking @ `e7d4cf6` **PRESENT** · ClientForm 픽업 프로필 @ `3c55339` **PRESENT** · UXD-51 FE-13/FE-14 @ `2a0ef3d` **PRESENT** · live E2E **run 잔여**(결정 73).

---

### [PLN] QA 피드백 반영 (2026-06-08, 68차 — TSR 94·95차 + transport pickup masking + UXD-51 + ClientForm 픽업 프로필 + BNK-9 재확인 + Open 0건)

> **68차 자동 기획 동기화** — TSR 94차(backend)·95차(frontend) 기준 planner git 실측 + BNK-9 재확인. **QA Open 0건** — 67차 Planned BLOCK 갱신.

| 항목 | 68차 관측 | 조치 |
|------|----------|------|
| **backend HEAD** | **`e7d4cf6`**(+1 vs `f8d1b02`) · WT **CLEAN** · **`mvn test` 241/241**(+1) · **23 ahead** | `TransportService.maskAddress` non-HQ pickup masking — ROADMAP v1.3·API_SPEC §12·USER_STORIES US-T01/US-T03 **`[x]`** |
| **frontend HEAD** | **`3c55339`**(+2 vs `d484206`) · test **`c510f5c`** · WT **CLEAN** · **`npm test` 203/67 PASS**(+14/+7) · **778 modules 3청크**(max **367 kB**) · **40 Route·51 page** | UXD-51 FE-13/FE-14 복원 · ClientFormPage 픽업 프로필 UI |
| **transport privacy @ `e7d4cf6`** | `TransportService`(+47/-10 maskAddress)·`TransportServiceTest`(+38)·`TransportPilotServiceFlowE2eTest`(+1) | SEC-D9·PII — non-HQ 역할 pickup 주소 마스킹 API_SPEC §12 반영 |
| **ClientForm 픽업 프로필 @ `3c55339`** | `ClientFormPage` usesTransport·pickupAddress·pickupContact·defaultPickupTime UI | USER_STORIES US-T01 frontend 폼 연동 **`[x]`** · FAQ Q166 |
| **UXD-51 @ `2a0ef3d`** | FE-13/FE-14 누락 UI 컴포넌트 복원·a11y 재점검 | FE-13·FE-14 lineage **유지**(COD 31차 `4be0938` 이후 회귀 복원) |
| **BNK-9** | Directions·러-1~4·G17~G19 — **47~67차 반영 불변** | 변경 없음 · #44 law.go.kr 잔여 |
| **활성 버전** | v1.3 frontend 단일 · backend merge(23) 최우선 | 67차 결정 **유지** |
| **merge gap** | backend **23 ahead** · frontend develop **16 ahead** | SEC-D14·B03 **backend merge 잔여** + v1.3 live E2E run |

**coder 다음 액션 (68차, 우선순위)**: ① **backend merge(23)** ② **B03/SEC-D14(backend)** test 재검증 ③ **frontend merge(16)** ④ **v1.3 live E2E run**(post-merge·`LIVE_E2E=1`, 결정 73) ⑤ v1.3 `merge_status: ready` 판단 ⑥ v3 StaffPage API·프로그램 사진(v1.3 gate 후) ⑦ v2 알림 프론트 UI·live Solapi.

---

### [PLN] QA 피드백 반영 (2026-06-08, 67차 — TSR 93차 + TransportPilot E2E + transport live harness + FE-15 복원 + BNK-9 재확인 + Open 0건)

> **67차 자동 기획 동기화** — TSR 93차(backend·frontend) 기준 planner git 실측 + BNK-9 재확인. **QA Open 0건** — 66차 Planned BLOCK 갱신.

| 항목 | 67차 관측 | 조치 |
|------|----------|------|
| **backend HEAD** | **`f8d1b02`**(+1 vs `1ec538b`) · WT **CLEAN** · **`mvn test` 240/240**(+9) · **22 ahead** | `TransportPilotServiceFlowE2eTest`·transport RBAC — ROADMAP v1.3 **`[x]`** |
| **frontend HEAD** | **`d484206`**(+2 vs `637b9b3`) · test **`c510f5c`** · WT **CLEAN** · **`npm test` 189/60 PASS** · **766 modules 3청크**(max **367 kB**) · **40 Route·50 page** | FE-15 복원 · transport live harness · transport a11y forced-colors |
| **TransportPilot E2E @ `f8d1b02`** | `TransportPilotServiceFlowE2eTest`(+183)·`PilotChecklistJwtE2eTest`(+32)·`RoleBasedControllerAccessTest`(+125 transport RBAC) | USER_STORIES US-T01~T03 backend service-flow **`[x]`** |
| **transport live harness @ `d484206`** | `src/e2e/transportLiveApi.e2e.test.js` develop HEAD PRESENT · 기본 `npm test` 제외(FE-22 패턴) | ROADMAP v1.3 harness **`[x]`** · live **run** post-merge 권장(결정 73) |
| **FE-15 @ `d484206`** | `manualChunks` 복원 — 91/92차 단일 JS 756 kB 회귀 **해소** · max **367 kB <500 kB** | USER_STORIES FE-15 **Fixed** · v1.2.1 후속 항목 **소멸** |
| **BNK-9** | Directions·러-1~4·G17~G19 — **47~66차 반영 불변** | 변경 없음 · #44 law.go.kr 잔여 |
| **활성 버전** | v1.3 frontend 단일 · backend merge(22) 최우선 | 66차 결정 **유지** |
| **merge gap** | backend **22 ahead** · frontend develop **14 ahead** | SEC-D14·B03 **backend merge 잔여** + v1.3 live E2E run |

**coder 다음 액션 (67차, 우선순위)**: ① **backend merge(22)** ② **B03/SEC-D14(backend)** test 재검증 ③ **frontend merge(14)** ④ **v1.3 live E2E run**(post-merge·`LIVE_E2E=1`, 결정 73) ⑤ v1.3 `merge_status: ready` 판단 ⑥ v3 StaffPage API·프로그램 사진(v1.3 gate 후) ⑦ v2 알림 프론트 UI·live Solapi.

---

### [PLN] QA 피드백 반영 (2026-06-08, 66차 — TSR 92차 + US-T01 profile + pilotPageFlows transport + BNK-9 재확인 + Open 0건)

> **66차 자동 기획 동기화** — TSR 92차(backend·frontend) 기준 planner git 실측 + BNK-9 재확인. **QA Open 0건** — 65차 Planned BLOCK 갱신.

| 항목 | 66차 관측 | 조치 |
|------|----------|------|
| **backend HEAD** | **`1ec538b`**(+1 vs `767d977`) · WT **CLEAN** · **`mvn test` 231/231** · **21 ahead** | US-T01 Clients API transport profile — ROADMAP v1.3·USER_STORIES US-T01 `[x]` |
| **frontend HEAD** | **`637b9b3`**(+2 vs `8a764df`) · test **`c510f5c`** · WT **CLEAN** · **`npm test` 189/60 PASS** · **766 modules** · **40 Route·50 page** | `pilotPageFlows` transport US-T01~T03 E2E · UXD-49 HQ 건강 이상 지점명 |
| **US-T01 @ `1ec538b`** | `ClientResponse` usesTransport·pickupAddress·pickupContact·defaultPickupTime · `ClientServiceTest` +2 · `PilotChecklistJwtE2eTest` transport routing +3 | USER_STORIES US-T01 client profile **`[x]`** · roster 구성 backend 선행 **완료** |
| **pilotPageFlows @ `637b9b3`** | transport US-T01~T03 fetch-mock E2E + `pilotChecklist` T01~T03 **HEAD PRESENT** | ROADMAP v1.3 **`pilotPageFlows` `[x]`** · live backend E2E **잔여** |
| **UXD-49 @ `00375f6`** | HQ 대시보드 건강 이상 목록 **지점명** 표시 (US-H02 PARTIAL) | USER_STORIES US-H02 진전 기록 |
| **BNK-9** | Directions·러-1~4·G17~G19 — **47~65차 반영 불변** | 변경 없음 · #44 law.go.kr 잔여 |
| **활성 버전** | v1.3 frontend 단일 · backend merge(21) 최우선 | 65차 결정 **유지** |
| **merge gap** | backend **21 ahead** · frontend develop **12 ahead** | SEC-D14·B03 **backend merge 잔여** + v1.3 live E2E |

**coder 다음 액션 (66차, 우선순위)**: ① **backend merge(21)** ② **B03/SEC-D14(backend)** test 재검증 ③ **v1.3 live backend E2E**(post-merge 권장) ④ **frontend merge(12)** ⑤ FE-15 bundle code-split(v1.2.1) ⑥ v3 StaffPage API·프로그램 사진(v1.3 gate 후) ⑦ v2 알림 프론트 UI·live Solapi.

---

### [COD] 코더 질문 — frontend 활성 버전 단일화 (2026-06-08) — **65차 해소 · 67차 유지**

- **실측 상태**: `src/frontend` develop **`d484206`** · working tree **CLEAN**.
- **충돌 관측**: ROADMAP v1.3·v2·v3 동시 `in_progress` — 「단일 in_progress」규칙과 표면 충돌.
- **67차 planner 결정**:
  - **frontend coder 단일 활성 = v1.3-A** — merge-blocking: service-flow E2E **`[x]` @ `f8d1b02`** · live harness **`[x]` @ `d484206`** · live **run 잔여**(결정 73).
  - **v2·v3 frontend 신규 착수 보류** — develop 선행 적재만 유지. v2 backend follow-up·v3 Staff API는 **backend merge(22) 후** 또는 v1.3 `merge_status: ready` 이후 재개.
  - **backend coder 최우선 = develop→test merge(22) + SEC-D14** — v1.3 transport API test 미승격 해소.
- **코더 조치**: v1.3 live E2E run·backend merge 게이트 외 **신규 frontend 기능 코딩 보류**.

---

### [PLN] QA 피드백 반영 (2026-06-08, 65차 — TSR 91차 + UXD-48 Recharts + BNK-9 재확인 + Open 0건)

> **65차 자동 기획 동기화** — TSR 91차(backend·frontend) 기준 planner git 실측 + BNK-9 재확인. **QA Open 0건** — 64차 Planned BLOCK 갱신.

| 항목 | 65차 관측 | 조치 |
|------|----------|------|
| **backend HEAD** | **`767d977`** · WT **CLEAN** · **`mvn test` 226/226** · **20 ahead** | 변경 없음 — merge 게이트 **최우선** |
| **frontend HEAD** | **`8a764df`**(+1 vs `73f7d39`) · test **`c510f5c`** · WT **CLEAN** · **`npm test` 183/60 PASS** · **766 modules** · **40 Route·50 page** | UXD-48 Recharts — US-M02·US-H01/E05/F04/H02 develop 연동 |
| **UXD-48 Recharts @ `8a764df`** | `ChartContainer`·`AttendanceRateChart`·`HealthTrendChart`·Dashboard/AttendanceStats/HealthDetail **HEAD PRESENT** | USER_STORIES US-M02 Recharts 3항 **[x] 부분** · HQ `BranchCompareChart` **잔여** |
| **FE-15 bundle 회귀 (TSR 91 LOW)** | 단일 JS **756 kB** (>500 kB vite 경고) — `manualChunks` 분리 **미적용 회귀** | **v1.2.1 후속**(non-blocking) · merge BLOCK 아님 |
| **BNK-9** | Directions·러-1~4·G17~G19 — **47~64차 반영 불변** | 변경 없음 · #44 law.go.kr 잔여 |
| **활성 버전** | v1.3·v2·v3 동시 in_progress | **frontend 단일 = v1.3-A** · v2/v3 frontend **보류** (COD 질문 해소) |
| **merge gap** | backend **20 ahead** · frontend develop **10 ahead** | SEC-D14·B03 **backend merge 잔여** + v1.3 transport E2E |

**coder 다음 액션 (65차, 우선순위)**: ① **backend merge(20)** ② **B03/SEC-D14(backend)** test 재검증 ③ **v1.3 `pilotPageFlows` transport E2E**(단일 frontend 활성) ④ **frontend merge(10)** ⑤ FE-15 bundle code-split(v1.2.1) ⑥ v3 StaffPage API·프로그램 사진(v1.3 gate 후) ⑦ v2 알림 프론트 UI·live Solapi ⑧ (post-merge) FE-22 live run.

---

### [PLN] QA 피드백 반영 (2026-06-08, 64차 — TSR 89·90차 + v1.3-A unconfirm UI 완료 + BNK-9 재확인 + Open 0건)

> **64차 자동 기획 동기화** — TSR 89차(backend)·90차(frontend) 기준 planner git 실측. **QA Open 0건** — 63차 Planned BLOCK 갱신.

| 항목 | 64차 관측 | 조치 |
|------|----------|------|
| **backend HEAD** | **`767d977`**(+1 vs `0d8968d`) · WT **CLEAN** · **`mvn test` 226/226** · **20 ahead** | v1.3-A transport unconfirm PATCH contract + POST legacy alias — ROADMAP v1.3 완료 기준 갱신 |
| **frontend HEAD** | **`73f7d39`**(+1 vs `fe33e7c`) · test **`c510f5c`** · WT **CLEAN** · **`npm test` 179/58 PASS** · **143 modules** · **40 Route·50 page** | UXD-47 `TransportUnconfirmModal`·`StaffRoleSelect`·StaffPage a11y·`TransportRunDetailPage` unconfirm |
| **v1.3-A unconfirm @ `767d977`/`73f7d39`** | backend PATCH+POST · frontend modal·detail page·Vitest 3건 HEAD PRESENT | ROADMAP v1.3 — **unconfirm UI `[x]`** · **`pilotPageFlows` transport·live E2E 잔여** |
| **BNK-9** | Directions·러-1~4·G17~G19 — **47~63차 반영 불변** | 변경 없음 · #44 law.go.kr 잔여 |
| **merge gap** | backend **20 ahead** · frontend develop **9 ahead** | SEC-D14·B03 **backend merge 잔여** + v1.3·v3 frontend merge |

**coder 다음 액션 (64차, 우선순위)**: ① **backend merge(20)** ② **B03/SEC-D14(backend)** test 재검증 ③ **v1.3 `pilotPageFlows` transport E2E** ④ **frontend merge(9)** ⑤ **v3 StaffPage API·프로그램 사진 업로드** ⑥ v2 알림 프론트 UI·live Solapi ⑦ (post-merge) FE-22 live run.

---

### [PLN] QA 피드백 반영 (2026-06-08, 63차 — TSR 87·88차 + v1.3-A unconfirm + v3 StaffPage + Open 0건)

> **63차 자동 기획 동기화** — TSR 87차(backend)·88차(frontend) 기준 planner git 실측. **QA Open 0건** — 62차 Planned BLOCK 갱신.

| 항목 | 63차 관측 | 조치 |
|------|----------|------|
| **backend HEAD** | **`0d8968d`**(+1 vs `dfd9be2`) · WT **CLEAN** · **`mvn test` 226/226** · **19 ahead** | v1.3-A transport run unconfirm hq_admin(6 files +102) — ROADMAP v1.3 완료 기준 갱신 |
| **frontend HEAD** | **`fe33e7c`**(+8 vs `c510f5c`) · test **`c510f5c`** · WT **CLEAN** · **`npm test` 170/55 PASS** · **140 modules** | v3 StaffPage UI + UXD-46 CSS·체크인 a11y · `362dbf0` v3 E2E lineage 포함 |
| **v1.3-A unconfirm @ `0d8968d`** | transport run unconfirm hq_admin API HEAD PRESENT | ROADMAP v1.3 — **frontend unconfirm UI·US-T01~T03 live E2E 잔여** |
| **v3 StaffPage @ `fe33e7c`** | StaffPage v3 UI develop HEAD PRESENT | ROADMAP v3 **직원 모듈 UI develop 진입** — §3-8 부분 · **merge 게이트 63차 신설** |
| **v3 merge 게이트 미정의 (TSR 87·88차 지적)** | TSR 87·88: "ROADMAP v3 merge 게이트 미정의 — planner 정의 대기" | ROADMAP v3 **merge 게이트·완료 기준 이번 63차 정의 완료** |
| **BNK-9** | Directions·러-1~4·G17~G19 — **47~62차 반영 불변** | 변경 없음 · #44 law.go.kr 잔여 |
| **merge gap** | backend **19 ahead** · frontend develop **8 ahead** | SEC-D14·B03 **backend merge 잔여** + v1.3·v3·UXD frontend merge |

**coder 다음 액션 (63차, 우선순위)**: ① **backend merge(19)** ② **B03/SEC-D14(backend)** test 재검증 ③ **v1.3 transport unconfirm 프론트 UI**·`pilotPageFlows` transport ④ **frontend merge(8)** ⑤ **v3 프로그램 사진 업로드·StaffPage 완전 기능** ⑥ v2 알림 프론트 UI·live Solapi ⑦ (post-merge) FE-22 live run.

---

### [PLN] QA 피드백 반영 (2026-06-08, 62차 — BNK-9 + v3 full stack + Open 0건)

> **62차 자동 기획 동기화** — BNK-9 재확인 + planner git 실측. **QA Open 0건** — 61차 Planned BLOCK 갱신.

| 항목 | 62차 관측 | 조치 |
|------|----------|------|
| **backend HEAD** | **`dfd9be2`**(+1 vs `53a1ffe`) · WT **CLEAN** · **`mvn test` 224/224** · **18 ahead** | v3 meals/programs REST·V49 — ROADMAP v3 완료 기준 §3-5·§3-6 `[x]` |
| **frontend HEAD** | **`362dbf0`**(+2 vs `7ef1083`) · test **`c510f5c`** · WT **CLEAN** · **`npm test` 164/54 PASS** · **39 route·47 page** | v3 `pilotPageFlows` US-N01·N02 E2E · a11y @ `3e9a9ab` |
| **v3 @ `dfd9be2`/`362dbf0`** | V49·`/api/v1/meals/*`·`/api/v1/programs/*`·`pilotPageFlows`·`pilotChecklist` N01/N02 | ROADMAP v3 **§3-5·§3-6 develop 완료** — 프로그램 사진·직원·평가 **후속** |
| **v1.3-A** | transport API @ `53a1ffe`+ · UI @ `e8d1854`+ lineage | ROADMAP v1.3 **US-T01~T03 live E2E·`pilotPageFlows` transport 잔여** |
| **BNK-9** | Directions·러-1~4·G17~G19 — **47~61차 반영 불변** | 변경 없음 · #44 law.go.kr 잔여 · v1.3-B 다중경유 Directions PoC 후순위 |
| **모듈 커버** | meals/programs backend+frontend 연동 완료 | **~65–68% 추정**(v1.2 ≥60% KPI 유지, 프로그램 사진·직원·평가 △) |
| **merge gap** | backend **18 ahead** · frontend develop **6 ahead** | SEC-D14·B03 **backend merge 잔여** + v1.3·v3 frontend merge |

**coder 다음 액션 (62차, 우선순위)**: ① **backend merge(18)** ② **B03/SEC-D14(backend)** test 재검증 ③ **v1.3 transport live E2E**·`pilotPageFlows` ④ **frontend merge(6)** ⑤ v2 알림 프론트 UI·live Solapi ⑥ (post-merge) FE-22 live run.

---

### [PLN] QA 피드백 반영 (2026-06-08, 61차 — BNK-9 + v1.3-A backend + v3 shell + Open 0건)

> **61차 자동 기획 동기화** — BNK-9 재확인 + planner git 실측. **QA Open 0건** — 60차 Planned BLOCK 갱신.

| 항목 | 61차 관측 | 조치 |
|------|----------|------|
| **backend HEAD** | **`53a1ffe`**(+1 vs `52e0621`) · WT **CLEAN** · **`mvn test` 212/212** · **17 ahead** | v1.3-A transport API·V47·geocode proxy — ROADMAP v1.3 완료 기준 6/7 `[x]` |
| **frontend HEAD** | **`7ef1083`**(+2 vs `c510f5c`) · test **`c510f5c`** · WT **CLEAN** · **`npm test` 157/53 PASS** · **39 route·34 page** | v3 `/meals`·`/programs` UI shell(§3-5·§3-6) · v1.3 a11y @ `f0b174a` |
| **v1.3-A @ `53a1ffe`** | `TransportController`·V47·`TransportServiceTest`·`TransportControllerRoutingTest` | ROADMAP v1.3 **backend PRESENT** — **US-T01~T03 live E2E·frontend merge 잔여** |
| **v3 @ `7ef1083`** | `MealsPage`·`ProgramsPage`·`MealRecordForm`·meals/programs API 클라이언트·Vitest | ROADMAP v3 **frontend PARTIAL** — **backend meals/programs API 선행** |
| **BNK-9** | Directions·러-1~4·G17~G19 — **47~60차 반영 불변** | 변경 없음 · #44 law.go.kr 잔여 · v1.3-B 다중경유 Directions PoC 후순위 |
| **모듈 커버** | transport(케어포 2장)·meals/programs(3·5장) UI 추가 | **~62–65% 추정**(v1.2 ≥60% KPI 유지, backend 미연동 △) |
| **merge gap** | backend **17 ahead** · frontend develop **4 ahead** | SEC-D14·B03 **backend merge 잔여** + v1.3·v3·UXD-43 frontend merge |

**coder 다음 액션 (61차, 우선순위)**: ① **backend merge(17)** ② **B03/SEC-D14(backend)** test 재검증 ③ **v1.3 transport live E2E**·`pilotPageFlows` ④ **v3 DBA+BE** meals/programs API ⑤ **frontend merge(4)** ⑥ v2 알림 프론트 UI·live Solapi ⑦ (post-merge) FE-22 live run.

---

### [PLN] QA 피드백 반영 (2026-06-08, 60차 — TSR 82 + v1.3 transport shell + BNK-9 불변 + Open 0건)

> **60차 자동 기획 동기화** — TSR 82(backend) + BNK-9 재확인 + planner git 실측. **QA Open 0건** — 59차 Planned BLOCK 갱신.

| 항목 | 60차 관측 | 조치 |
|------|----------|------|
| **backend HEAD** | **`52e0621`**(+1 vs `ac17ad8`) · WT **CLEAN** · **`mvn test` 202/202** · **16 ahead** | v2/J03 copay PAID→`BILLING_PAYMENT_RECEIVED` alimtalk — ROADMAP v2·USER_STORIES US-J03 follow-up |
| **frontend HEAD** | **`e8d1854`**(+2 vs `c510f5c`) · test **`c510f5c`** · WT **CLEAN** · **`npm test` 150/50 PASS** · **37 route·41 page** | v1.3 transport UI shell(US-T01~T03) · UXD-43 UNMATCHED 후보 검색 |
| **v1.3 @ `e8d1854`** | `TransportPage`·`TransportRunNewPage`·`TransportRunDetailPage`·`TransportDisclaimer`·`KakaoTransportMap` | ROADMAP v1.3 **frontend PARTIAL** — **backend transport API·Flyway 선행** |
| **UXD-43 @ `f01e3a8`** | `ReconciliationPage` UNMATCHED 후보 이용자 검색 UI | USER_STORIES US-G06 인수 조건 **PARTIAL** — 단일 트랜잭션 매칭 API 잔여 |
| **BNK-9** | Directions·러-1~4·G17~G19 — **47~59차 반영 불변** | 변경 없음 · #44 law.go.kr 잔여 |
| **merge gap** | backend **16 ahead** · frontend develop **2 ahead** | SEC-D14·B03 **backend merge 잔여** + v1.3·UXD-43 frontend merge |

**coder 다음 액션 (60차, 우선순위)**: ① **backend merge(16)** ② **B03/SEC-D14(backend)** test 재검증 ③ **v1.3 DBA+BE** transport API·Flyway(frontend shell 연동) ④ **frontend merge(2)** ⑤ v2 알림 **프론트 UI**·live Solapi ⑥ (post-merge) FE-22 live run.

---

### [PLN] QA 피드백 반영 (2026-06-08, 59차 — TSR 80·81 + US-G06 DISCREPANCY + BNK-9 불변 + Open 0건)

> **59차 자동 기획 동기화** — TSR 80(backend)·81(frontend) + BNK-9 재확인 + planner git 실측. **QA Open 0건** — 58차 Planned BLOCK 갱신.

| 항목 | 59차 관측 | 조치 |
|------|----------|------|
| **backend HEAD** | **`ac17ad8`**(+1 vs `4c74f84`) · WT **1U**(`data/`) · **`mvn test` 198/198** · **15 ahead** | v2/J03 `AlimtalkFallbackText` SMS fallback — ROADMAP v2·USER_STORIES US-J03 follow-up |
| **frontend HEAD** | **`c510f5c`**(+2 vs `95b92b9`) · test **`c510f5c`** · WT **CLEAN** · **`npm test` 143/46 PASS** · **34 route·38 page** | US-G06 DISCREPANCY compare Modal·E2E |
| **US-G06 @ `fd4e8f3`** | `DiscrepancyComparePanel`·`NhisReconciliationTable` compare 액션·접근성 | USER_STORIES US-G06 인수 조건 `[x]` 갱신 |
| **`c510f5c` E2E** | `pilotPageFlows` US-G06 DISCREPANCY 회귀 | ROADMAP v1.2 완료 기준·P8 체크리스트 |
| **v1.2 frontend merge** | develop=test **`c510f5c`** — TSR 81 | ROADMAP v1.2 `merge_status: merged` · B03 frontend portion **소멸** |
| **BNK-9** | Directions·러-1~4·G17~G19 — **47~58차 반영 불변** | 변경 없음 · #44 law.go.kr 잔여 |
| **merge gap** | backend **15 ahead** · frontend **0** | SEC-D14·B03 **backend merge 단일** |

**coder 다음 액션 (59차, 우선순위)**: ① **backend merge(15)** ② **B03/SEC-D14(backend)** test 재검증 ③ v2 알림 **프론트 UI**·live Solapi·템플릿 심사 ④ (post-merge) FE-22 live run.

---

### [PLN] QA 피드백 반영 (2026-06-08, 58차 — TSR 79·80 + UXD-41 US-F03 + BNK-9 불변 + Open 0건)

> **58차 자동 기획 동기화** — TSR 79(backend)·80(frontend) + BNK-9 재확인 + planner git 실측. **QA Open 0건** — 57차 Planned BLOCK 갱신.

| 항목 | 58차 관측 | 조치 |
|------|----------|------|
| **backend HEAD** | **`4c74f84`**(+1 vs `32a1f8f`) · WT **CLEAN** · **`mvn test` 191/191** · **14 ahead** | v2/J03 Solapi 템플릿 변수 매핑 — ROADMAP v2·USER_STORIES US-J03 follow-up |
| **frontend HEAD** | **`95b92b9`**(+2 vs `4957bd3`) · test **`4f71543`** · WT **CLEAN** · **`npm test` 137/45 PASS** · **34 route·38 page** | UXD-41 US-F03·Q154 incident API 정합 |
| **UXD-41 @ `3ec8206`** | `IncidentRecordForm`·`HealthPage` incident 탭·`pilotPageFlows` US-F03 E2E | USER_STORIES US-F03·REQUIREMENTS §3-4 갱신 |
| **`95b92b9` Q154** | `healthApiPayload.js` incident `description`→`detail` 필드 정합 | FAQ Q154 incident 항목 **Fixed** |
| **BNK-9** | Directions·러-1~4·G17~G19 — **47~57차 반영 불변** | 변경 없음 · #44 law.go.kr 잔여 |
| **merge gap** | backend **14** · frontend develop **13 ahead** of test | SEC-D14·B03 **backend merge 잔여** + v1.2 frontend merge |

**coder 다음 액션 (58차, 우선순위)**: ① **backend merge(14)** ② **B03/SEC-D14(backend)** test 재검증 ③ **frontend v1.2 merge(13)** ④ v2 알림 **프론트 UI**·템플릿 심사 ⑤ (post-merge) FE-22 live run.

---

### [PLN] QA 피드백 반영 (2026-06-08, 57차 — TSR 77·78 + UXD-40·Q154 + BNK-9 불변 + Open 0건)

> **57차 자동 기획 동기화** — TSR 77(frontend)·78(backend) + BNK-9 재확인 + planner git 실측. **QA Open 0건** — 56차 Planned BLOCK 갱신.

| 항목 | 57차 관측 | 조치 |
|------|----------|------|
| **backend HEAD** | **`32a1f8f`**(+1 vs `0832fbf`) · WT **CLEAN** · **13 ahead** · `mvn test` **185/185** | ROADMAP·REQUIREMENTS §1-3-1 갱신 |
| **service-layer E2E** | `J03AlimtalkServiceFlowE2eTest` 5건 · `AttendanceServiceTest` check-out dispatch | ROADMAP v2·USER_STORIES US-J03 follow-up |
| **frontend HEAD** | **`4957bd3`**(+2 vs `c5708c7`) · test **`4f71543`** · WT **CLEAN** · **`npm test` 130/44 PASS** · build **123 modules** | UXD-40·Q154 진전 |
| **UXD-40 @ `9863312`** | `vitalsRanges.js`·`VitalsRecordForm` 비정상 범위 인라인 경고(US-F01) | USER_STORIES US-F01·DESIGN_SYSTEM |
| **Q154 @ `4957bd3`** | `healthApiPayload.js`·`healthRecords.js`·`NhisReconciliationTable` — 건강·NHIS API 본문 정합 **Fixed** | USER_STORIES US-F01·F02·G06 · FAQ Q154 |
| **BNK-9** | Directions·러-1~4·G17~G19 — **47~56차 반영 불변** | 변경 없음 · #44 law.go.kr 잔여 |
| **merge gap** | backend **13** · frontend develop **11 ahead** of test | SEC-D14·B03 **backend merge 잔여** + v1.2 frontend merge |

**coder 다음 액션 (57차, 우선순위)**: ① **backend merge(13)** ② **B03/SEC-D14(backend)** test 재검증 ③ **frontend v1.2 merge(11)** ④ v2 알림 **프론트 UI**·템플릿 심사 ⑤ (post-merge) FE-22 live run.

---

### [PLN] QA 피드백 반영 (2026-06-08, 56차 — TSR 76 + UXD-39 + vitals dispatch + BNK-9 불변 + Open 0건)

> **56차 자동 기획 동기화** — TSR 76(backend·frontend) + BNK-9 재확인 + planner git 실측. **QA Open 0건** — 55차 Planned BLOCK 갱신.

| 항목 | 56차 관측 | 조치 |
|------|----------|------|
| **backend HEAD** | **`0832fbf`**(+1 vs `8ce1151`) · WT **CLEAN** · **12 ahead** · `mvn test` **179/179** | ROADMAP·REQUIREMENTS §1-3-1 갱신 |
| **vitals dispatch** | `HealthRecordService` — 활력징후→DAILY_CARE alimtalk · `HealthRecordServiceTest` +53 lines | ROADMAP v2·USER_STORIES US-J03 follow-up |
| **frontend HEAD** | **`c5708c7`**(+1 vs `a627c6d`) · test **`4f71543`** · WT **CLEAN** · **`npm test` 115/40 PASS** · build **120 modules** | UXD-39 Must UI 진전 |
| **UXD-39** | `VitalsRecordForm`·`MedicationRecordForm`·`NhisReconciliationTable`·`MedicationDuplicateAlert`·`HealthDetailPage` 표+FilterChips | USER_STORIES US-F01·F02·F04·G06 |
| **BNK-9** | Directions·러-1~4·G17~G19 — **47~55차 반영 불변** | 변경 없음 · #44 law.go.kr 잔여 |
| **API 갭** | 건강 DTO(`recordedAt`·`bloodGlucose`)·NHIS reconciliation 필드명 불일치 | FAQ Q154 · coder 후속(非 BLOCK) |
| **merge gap** | backend **12** · frontend develop **9 ahead** of test | SEC-D14·B03 **backend merge 잔여** + v1.2 frontend merge |

**coder 다음 액션 (56차, 우선순위)**: ① **backend merge(12)** ② **B03/SEC-D14(backend)** test 재검증 ③ **frontend v1.2 merge(9)** ④ 건강·NHIS API 본문 정합 ⑤ (post-merge) FE-22 live run · v2 알림 **프론트 UI** 잔여.

---

### [PLN] QA 피드백 반영 (2026-06-08, 55차 — TSR 74·75 재확인 + Epic E 진전 + BNK-9 불변 + Open 0건)

> **55차 자동 기획 동기화** — TSR 74(backend)·75(frontend) + BNK-9 재확인 + planner git 실측. **QA Open 0건** — 54차 Planned BLOCK 갱신.

| 항목 | 55차 관측 | 조치 |
|------|----------|------|
| **backend HEAD** | **`8ce1151`**(+1 vs `c53dd3b`) · WT **CLEAN** · **11 ahead** · `mvn test` **178/178** | ROADMAP·REQUIREMENTS §1-3-1 갱신 |
| **backend V46** | `V46__notification_history_query_index.sql` — 알림 이력 조회 인덱스 | ROADMAP v2·API_SPEC §11-5 follow-up |
| **frontend HEAD** | **`a627c6d`**(+2 vs `9bdf59f`) · test **`4f71543`** · WT **CLEAN** · **`npm test` 110/36 PASS** · build **117 modules** | Epic E 출석·QR·통계 진전 |
| **`6f3f746`** | 수기 출석 UI — **US-E01·E02** | USER_STORIES US-E01·E02 주석 |
| **`a627c6d`** | QR 생성·출석 통계 API — **US-E03·E05** | USER_STORIES US-E03·E05 주석 |
| **BNK-9** | Directions·러-1~4·G17~G19 — **47~54차 반영 불변** | 변경 없음 · #44 law.go.kr 잔여 |
| **v1.2 P0 게이트** | ≥60% KPI·P0 E2E **충족** · P1 3건 **v1.2.1 후순위** | ROADMAP v1.2 `merge_status: ready` coder 판단 대기 |
| **merge gap** | backend **11** · frontend develop **8 ahead** of test | SEC-D14·B03 **backend merge 잔여** + v1.2 frontend merge |

**coder 다음 액션 (55차, 우선순위)**: ① **backend merge(11)** ② **B03/SEC-D14(backend)** test 재검증 ③ **frontend v1.2 merge(8)** ④ (post-merge) FE-22 live run · v2 알림 이력 **프론트 UI** 잔여.

---

### [PLN] 결정 73 — live E2E merge 게이트 제외 (2026-06-07, 사용자)

> **48차 planner 반영** — Must P1–P8·J01/J02 live E2E run은 **`merge_status: ready` 선행 조건에서 제외**. merge 후 post-merge·권장 검증.

| 항목 | 조치 |
|------|------|
| **ROADMAP v1.1** | merge-blocking 완료 기준 `[x]` 유지 · live E2E → `### post-merge 검증` 이동 · **`merge_status: ready`** |
| **이관 규율 10항** | live E2E run ≠ merge BLOCK |
| **FE-22** | harness @ `d592a17` Fixed · **live run** = merge **후** 권장 |

**coder 다음 액션 (48차, 우선순위)**: ① **frontend merge(11)** — v1.1 `ready` ② **backend merge(6)** ③ **B03** test 재검증 ④ (post-merge) FE-22 live run.

---

### [PLN] QA 피드백 반영 (2026-06-08, 53차 — TSR 72·73 + v2 알림 이력 API + v1.2 P0 E2E·US-E04·Open 0건)

> **53차 자동 기획 동기화** — TSR 72(backend)·73(frontend) + BNK-9 재확인 + planner git 실측. **QA Open 0건** — 52차 Planned BLOCK 갱신.

| 항목 | 53차 관측 | 조치 |
|------|----------|------|
| **backend HEAD** | **`c53dd3b`**(+1 vs `78e8928`) · WT **CLEAN** · **10 ahead** · `mvn test` **178/178** | ROADMAP·REQUIREMENTS §1-3-1·API_SPEC §11-5 갱신 |
| **backend v2/J03** | `GuardianNotificationHistoryController`·`StaffClientNotificationHistoryController`·`NotificationHistoryService`(+test) | ROADMAP v2 완료 기준·USER_STORIES US-J03 follow-up |
| **frontend HEAD** | **`9bdf59f`**(+2 vs `42f48e1`) · test **`4f71543`** · WT **CLEAN** · **`npm test` 97/30 PASS** · build **114 modules** | v1.2 P0 CRUD E2E·입금 모달·보호자 초대/수정 |
| **`a68f150`** | `GuardianCheckinPage` DS FilterChips — **US-E04** | USER_STORIES US-E04 주석 |
| **`9bdf59f`** | P0 CRUD E2E·`PaymentRecordModal`·보호자 초대/수정 — Epic K·L | ROADMAP v1.2·USER_STORIES US-K01·L01 진전 |
| **BNK-9** | Directions·러-1~4·G17~G19 — **47~52차 반영 불변** | 변경 없음 · #44 law.go.kr 잔여 |
| **merge gap** | backend **10** · frontend develop **6 ahead** of test | SEC-D14·B03 **backend merge 잔여** + v1.2 frontend merge |

**coder 다음 액션 (53차, 우선순위)**: ① **backend merge(10)** ② **B03/SEC-D14(backend)** test 재검증 ③ **frontend v1.2 merge(6)** ④ (post-merge) FE-22 live run · v2 알림 이력 **프론트 UI** 잔여.

---

### [PLN] QA 피드백 반영 (2026-06-08, 52차 — TSR 70·71 + v1.2 UXD 15 pages·P0 KPI·Open 0건)

> **52차 자동 기획 동기화** — TSR 70(backend)·71(frontend) + BNK-9 재확인 + planner git 실측. **QA Open 0건** — 51차 Planned BLOCK 갱신.

| 항목 | 52차 관측 | 조치 |
|------|----------|------|
| **backend HEAD** | **`78e8928`**(+1 vs `44e0f02`) · WT **CLEAN** · **9 ahead** · `mvn test` **171/171** | ROADMAP·REQUIREMENTS §1-3-1 갱신 |
| **backend v2/J03** | `HealthRecordService` 투약기록 생성 시 **DAILY_CARE alimtalk** dispatch · `HealthRecordServiceTest` | ROADMAP v2·USER_STORIES US-J03 follow-up 주석 |
| **frontend HEAD** | **`42f48e1`**(+2 vs `e0eaf32`) · test **`4f71543`** · WT **CLEAN** · **`npm test` 89/28 PASS** · build **114 modules** | v1.2 **33 route·33 page** · module coverage KPI |
| **UXD @ `0d83a42`** | **15 missing pages** — US-D01·E03-E05·F04·G01-G07·H01-H04·B01·A01 | ROADMAP v1.2·USER_STORIES Epic D·E·F·G·H 진전 |
| **`42f48e1`** | P0 page-flow tests·module coverage KPI·title 정렬 | 결정 49 ≥60% **측정 진행**(~45–50% 추정) |
| **BNK-9** | Directions·러-1~4·G17~G19 — **47~51차 반영 불변** | 변경 없음 · #44 law.go.kr 잔여 |
| **merge gap** | backend **9** · frontend develop **4 ahead** of test | SEC-D14·B03 **backend merge 잔여** + v1.2 frontend merge |

**coder 다음 액션 (52차, 우선순위)**: ① **backend merge(9)** ② **B03/SEC-D14(backend)** test 재검증 ③ **frontend v1.2 merge(4)** ④ (post-merge) FE-22 live run · ≥60% KPI 잔여(P0 E2E·SideNav 2단 depth).

---

### [PLN] QA 피드백 반영 (2026-06-08, 51차 — TSR 68·69 + v1.1 merged + UXD 35 v1.2 커밋·Open 0건)

> **51차 자동 기획 동기화** — TSR 68(backend)·69(frontend) + BNK-9 재확인 + planner git 실측. **QA Open 0건** — 50차 Planned BLOCK 갱신.

| 항목 | 51차 관측 | 조치 |
|------|----------|------|
| **backend HEAD** | **`44e0f02`**(+1 vs `c221531`) · WT **CLEAN** · **8 ahead** · `mvn test` **170/170** | ROADMAP·REQUIREMENTS §1-3-1 갱신 |
| **frontend HEAD** | **`e0eaf32`**(+2) · test **`4f71543`** · WT **CLEAN** · **`npm test` 82/27 PASS** | v1.1 **`merge_status: merged`** · SEC-D14 frontend portion **해소** |
| **UXD 35 @ `64468a3`** | P0 UI·SideNav·Must page DS integration **develop 커밋** | US-UX-02·FE-12/13 lineage **진전** · 50차 24 files WIP **소멸** |
| **`e0eaf32`** | `/guardians` RBAC·page-flow 회귀 확장 | USER_STORIES FE-12/13·guardians route 주석 |
| **BNK-9** | Directions·러-1~4·G17~G19 — **47·49·50차 반영 불변** | 변경 없음 · #44 law.go.kr 잔여 |
| **merge gap** | backend **8** · frontend develop **2 ahead** of test | SEC-D14·B03 **backend merge 잔여** + v1.2 frontend merge |

**coder 다음 액션 (51차, 우선순위)**: ① **backend merge(8)** ② **B03/SEC-D14(backend)** test 재검증 ③ **frontend v1.2 merge(2)** ④ (post-merge) FE-22 live run · ≥60% KPI 측정.

---

### [PLN] QA 피드백 반영 (2026-06-08, 50차 — BNK-9 재확인 + frontend dirty-tree 재확대·Open 0건)

> **50차 자동 기획 동기화** — BNK-9 벤치마크 재확인 + planner git 실측. **QA Open 0건** — 49차 Planned BLOCK 갱신.

| 항목 | 50차 관측 | 조치 |
|------|----------|------|
| **backend HEAD** | **`c221531`** 불변 · WT **3M** · **7 ahead** | baseline·ROADMAP 유지 |
| **frontend HEAD** | **`4f71543`** 불변 · WT **1M→24 files 재확대** | v1.2 Must UI WIP cluster 관측 · FE-6 recurrence **미커밋 단일** |
| **WT WIP cluster** | `DashboardWidgetGrid`·`FileUpload`·`GuardianInviteModal`·`HealthAbnormalBanner`·`NhisImportGuidePanel`·`MaskedRevealField` + Must pages 6종 modified | ROADMAP v1.2·FE-12/13 lineage 주석 |
| **BNK-9** | Directions·러-1~4·G17~G19 — **47·49차 반영 불변** | 변경 없음 · #44 law.go.kr 잔여 |
| **merge gap** | backend **7** · frontend **0** | SEC-D14·B03 **backend merge 잔여** |
| **WT dirty** | backend 3M · frontend **24 files** = **27 total** | commit/revert 후 merge |

**coder 다음 액션 (50차, 우선순위)**: ① **WT dirty-tree 정리**(27 files — Must UI 일괄 commit 또는 revert) ② **backend merge(7)** ③ **B03/SEC-D14** test 재검증 ④ (post-merge) FE-22 live run.

---

### [PLN] QA 피드백 반영 (2026-06-08, 49차 — TSR 66·67 + BNK-9 재확인 + baseline HEAD 갱신·Open 0건)

> **49차 자동 기획 동기화** — TSR 66(backend)·67(frontend) + BNK-9 벤치마크 재확인 + planner git 실측. **QA Open 0건** — 47·48차 Planned BLOCK 갱신.

| 항목 | 49차 관측 | 조치 |
|------|----------|------|
| **backend HEAD** | `80bdb1e`→**`c221531`**(+1 v2/J03) · `mvn test` **169/169** · **7 ahead** · WT **3M** | baseline·ROADMAP·REQUIREMENTS 갱신 |
| **frontend HEAD** | `d592a17`→**`4f71543`**(+2: UXD SideNav·FE-22 liveConfig) · `npm test` **58/18** · build **86 modules** · develop=test | v1.2 US-UX-02 SideNav **진전** |
| **TSR 66 @ `c221531`** | v2/J03 NotificationAlimtalkDispatchE2eTest 7건 · v1 artifacts **PRESENT** | v2 in_progress 유지 · backend merge(7) |
| **TSR 67 @ `4f71543`** | UXD `f64e1dd` SideNav·AppShell · FE-22 `liveConfig` fail-fast | ROADMAP v1.2·USER_STORIES US-UX-02 주석 |
| **BNK-9** | Directions·러-1~4·G17~G19 — **47차 반영 불변** | 변경 없음 · #43 해소 · #44 law.go.kr 잔여 |
| **merge gap** | backend **7** · frontend **0**(test 승격) | SEC-D14·B03 **backend merge 잔여** |
| **WT dirty** | backend 3M · frontend 1M | commit/revert 후 merge |

**coder 다음 액션 (49차, 우선순위)**: ① **WT dirty-tree 정리**(4 files) ② **backend merge(7)** ③ **B03/SEC-D14** test 재검증 ④ (post-merge) FE-22 live run.

---

### [PLN] QA 피드백 반영 (2026-06-08, 47차 — TSR 64·65 + BNK-9 + baseline HEAD 갱신·Open 0건)

> **47차 자동 기획 동기화** — TSR 64(backend)·65(frontend) + BNK-9 벤치마크 + planner git 실측. **QA Open 0건** — 46차 Planned BLOCK 갱신.

| 항목 | 47차 관측 | 조치 |
|------|----------|------|
| **backend HEAD** | `136239e`→**`80bdb1e`**(+2: BE-11·V45 lineage) · `mvn test` **158/158** · **6 ahead** | baseline·ROADMAP·REQUIREMENTS 갱신 |
| **frontend HEAD** | `7170b2a`→**`d592a17`**(+3: guardian REST·Alert a11y·**FE-22 harness**) · `npm test` **46/13** · **18 route** · **11 ahead** | v1.1 FE-22 **PARTIAL** · KPI drift 정정 |
| **TSR 64 @ `80bdb1e`** | **BE-11 Fixed @ `8d42bdd`** · SEC-20260608-014 **Planned→Fixed** | ROADMAP·USER_STORIES BE-11 `[x]` |
| **TSR 65 @ `d592a17`** | FE-22 harness HEAD PRESENT · **live run** merge·`LIVE_E2E` 후 | ROADMAP v1.1 live E2E **run** 잔여 |
| **BNK-9** | Directions 10k/8원·다중경유 5k/16원 · 러-1~4 실액 · G17~G19 | REQUIREMENTS §1-5-3·ROADMAP v1.3·#43 해소·#44 갱신 |
| **문서 drift** | `4be0938`/24 route **미존재** · `@7170b2a` 15 route · `@d592a17` 18 route | v1.2 KPI·완료 `[x]` lineage 주석 |
| **merge gap** | backend **6** · frontend **11** | SEC-D14·B03 BLOCK **유지** |

**coder 다음 액션 (47차, 우선순위)**: ~~① FE-22 live E2E run(merge·backend·`LIVE_E2E` 후)~~ **→ 48차 결정 73: merge 후 post-merge** ② **backend merge(6)** ③ **frontend merge(11)** ④ **B03** ready.

---

### [PLN] QA 피드백 반영 (2026-06-08, 45차 — TSR 62·63 + COD Must API·J01 REST + baseline HEAD 갱신·Open 0건)

> **45차 자동 기획 동기화** — TSR 62(backend)·63(frontend) + planner 실측 @ `7170b2a`. QA Open **0건**.

| 항목 | 45차 관측 | 조치 |
|------|----------|------|
| **backend HEAD** | `3f9264f`→**`136239e`**(+1 Solapi) · `mvn test` **152/152** · **4 ahead** | baseline·ROADMAP 갱신 |
| **frontend HEAD** | `c3b863e`→**`7170b2a`**(+4: Must API·pilot·7-role·SEC-008·guardian REST) · `npm test` **40/11** · audit **0** · **9 ahead** | v1.1 완료 기준 `[x]` 승격 |
| **TSR 63 @ `811aef3`** | H04·M01·R-04a·R-05·SEC-008 Fixed · 이관 규율 5 PASS | ROADMAP v1.1 완료 기준 갱신 |
| **COD `7170b2a`** | J01 `ClientDetailPage`·J02 `GuardianPortalPage` REST fetch-mock 회귀 | US-J01/J02 **PARTIAL** — live E2E 잔여 |
| **v1.1 잔여** | Must **라이브 E2E** · J01 **live API E2E** | ROADMAP `[ ]` 유지 |
| **merge gap** | backend **4** · frontend **9** | 잔여 BLOCK **양 스트림 merge + B03** |
| **BNK-8** | v1.3-A 패리티·v1.3-B 차별화 | 42차 반영 **변경 없음** |

**coder 다음 액션 (45차, 우선순위)**: ① **Must 라이브 E2E** — P1–P8 수동 시나리오(live backend) ② **J01 live API E2E** — guardian 초대·명세 live 연동 ③ **backend merge(4)** ④ **frontend merge(9)** ⑤ **B03** ready.

---

### [PLN] QA 피드백 반영 (2026-06-08, 44차 — TSR 61 + COD FE-18/FE-19 Fixed + baseline HEAD 갱신·Open 0건)

> **44차 자동 기획 동기화** — TSR 61(frontend) + planner 실측. QA Open **0건** · COD `f506c90`·`c3b863e` 반영.

| 항목 | 44차 관측 | 조치 |
|------|----------|------|
| **frontend HEAD** | `e043eac`→**`c3b863e`**(+2: `f506c90` FE-18/19 · `c3b863e` favicon) | baseline·ROADMAP·USER_STORIES 갱신 |
| **FE-18·FE-19** | `GuardianInvitationList`·`PaymentRecordModal`·`GuardianPortalPage`·`services.js` HEAD PRESENT · `npm test` **9/9 PASS** | **Fixed @ `f506c90`** · B07 #6·H05·SEC-D9 소멸 |
| **TSR 61** | `e043eac` CLEAN · 6/6 PASS · SEC-D12 유효 · H04 FAIL · M01 PARTIAL | v1.1 완료 기준 정합 갱신 |
| **v1.1 잔여** | `pilotPageFlows`·Must API·ReconciliationPage·7역할 tests **ABSENT** | ROADMAP v1.1 `[ ]` 재정렬 · d5654c0 lineage 재구현 태스크 |
| **merge gap** | backend **3** · frontend **5** | 잔여 BLOCK **양 스트림 merge + B03** |
| **BNK-8** | v1.3-A 패리티·v1.3-B 차별화 | 42차 반영 **변경 없음** |

**coder 다음 액션 (44차, 우선순위)**: ① **Must API·P1–P8** — `pilotChecklist`·Must 페이지 API 연동 재구현 ② **J01 live E2E** — FE-18 UI + backend J01 API 연동 ③ **SEC-008** — vite/vitest upgrade(선택·non-blocking) ④ **backend merge(3)** ⑤ **frontend merge(5)** ⑥ **B03** ready.

---

## 사용자 입력 요약

주간보호센터 운영 관리 **앱/웹**을 구현한다.

| 항목 | 사용자 명시 |
|------|------------|
| 백엔드 | **Java** |
| 프론트엔드 | **React** |
| 추가 요청 | 타 주간보호센터 관리 웹 **벤치마킹 전담 에이전트** 추가 |
| 1주차 목표 | **관리자 대시보드 출력**까지 완료 |
| MVP v1 범위 | Must 전체: 인증, 이용자, 출석, 건강기록, 대시보드 |
| **2026-06-06 추가** | ① 프론트 **파비콘** 적용 기획, ② 경쟁사 대비 **기능·화면 밀도** 부족 → BNK **6차 심화 조사** 후 v1.2 백로그, ③ `docs/` **폴더 분류** 정리 |
| 레거시 코드 | `src/backend`(Python/FastAPI) **전부 폐기**, Java 신규 시작 |
| 기술 세부 | Spring Boot 3.x, Vite+React, PostgreSQL, JWT+RBAC |
| 출석 방식 | **수기 + QR 모두** 지원 |
| 운영 모델 | **다지점** — 지점별 관리 + 통합 관리 구분 |
| MVP 역할 | **6개 역할 전부** 별도 UI·권한으로 구현 |
| hq_admin 쓰기 | `active_branch_id` 선택 시 해당 지점만 CRUD (B방식) |
| QR 스캔 | **B방식** — 보호자/이용자가 지점 QR 스캔 (A방식은 MVP 제외) |
| 사업 모델 | **전국 판매 B2B SaaS** (개인용 아님) |
| 1주차 범위 | 6역할 로그인·화면·권한 **전부** 포함 (골격만 X) |
| QR 계정 정책 | **안 3** — guardian + client_user(센터별 on/off) |
| 배포 클라우드 | **벤더 무관** |
| 목표 일정 | **일정 무관** (런칭 시점 제약 없음) |
| 파일럿 센터 | **있음** — 실제 운영 센터에서 테스트 |
| 신규 고객 등록 | **확정: A** — ogada 직원 (`platform_admin`, `/platform`) |
| 청구·정산 | **MVP v1 포함** (케어포 벤치마킹 기반 2단계 모델) |
| 벤치마킹 참고 | **케어포** (carefor.co.kr) |
| 파일럿 인원 | 센터장 1 + 요양보호사 5, **지점 2곳** |
| 수가표 관리 | **B방식** — `hq_admin`이 화면에서 등급별·연도별 수가 입력·관리 (코드 고정 X) |
| 본인부담률 | **이용자별 구분 관리** — 일반15%/감경9%/감경6%/기초수급0%, 테이블화 |
| **2026-06-07 대화** | ① 보호자 초대 채널 개념 질문 ② **급한 목표 = develop→test merge 검증** ③ 파일럿 1주차 업무 3가지 → **planner 확정**(결정 57) |
| **2026-06-07 대화(2)** | ① 보호자 초대 채널 **이메일 단일 확정**(결정 59) ② 파일럿 1주차 P1–P3 **유지** ③ **배차·이동경로** 기능 추가(결정 60) |
| **2026-06-07 대화(3)** | 배차 **1차 = 수동 명단 + 수동 순서 + 지도**(v1.3-A). TSP·도로 길찾기는 v1.3-B (결정 61) |
| **2026-06-07 대화(4)** | ① 정차 **최대 15명** ② `hq_admin` **배차 확정** → 직원 명단·지도 **조회만** ③ **픽업만** (드롭 후속) (결정 62) |

---

## 확인된 결정 사항

1. **기술 스택 변경**: `.agents/agents.yaml` 초기 설정(Python/FastAPI + Vanilla JS) 대신 **Java 백엔드 + React 프론트엔드**로 진행한다.
2. **도메인**: 주간보호센터 운영 관리 (이용자·출석·건강·청구 등).
3. **플랫폼**: 웹 기반, 모바일·PC 반응형 (기존 요구사항 유지).
4. **벤치마킹 에이전트**: 경쟁·유사 서비스 분석을 기획 단계에 포함한다. (`benchmark_researcher` — agents.yaml·run_agent.py 반영 완료, 3시간 loop)
5. **1주차 완료 목표** (2026-06-05 확정): 로그인 → 이용자·출석·건강 데이터 입력 → **관리자 대시보드(`/dashboard`) 실데이터 출력**까지.
6. **MVP v1 기능 범위** (2026-06-05 확정): Must 5개 모듈 전부 포함 — 인증, 이용자 관리, 출석 관리, 건강 기록, 관리자 대시보드. Should/Could는 v1 이후.
7. **레거시 코드 처리** (2026-06-05 확정): 기존 `src/backend`(Python/FastAPI) **전부 폐기**. Java 백엔드로 신규 구현. 마이그레이션·병행 없음.
8. **기술 스택 세부** (2026-06-05 확정): Spring Boot 3.x, Vite+React(SPA), PostgreSQL, JWT+RBAC.
9. **출석 방식** (2026-06-05 확정): 수기 체크인/아웃 **와** QR 코드 체크인/아웃 **모두** MVP에 포함. `check_in_method`로 구분.
10. **다지점 운영** (2026-06-05 확정): 여러 지점 운영 전제. **지점별 관리**(Branch Scope)와 **통합 관리**(HQ Scope) 체계 분리. MVP에 Organization-Branch 계층·이중 대시보드 포함.
11. **MVP 역할 범위** (2026-06-05 확정): `hq_admin`, `branch_admin`, `social_worker`, `caregiver`, `guardian`, `sysadmin` **6개 역할 모두** 별도 화면·메뉴·권한으로 구현.
12. **hq_admin 쓰기 권한** (2026-06-05 확정): 전 지점 조회·집계 기본, **수정·등록은 `active_branch_id` 선택 시 해당 지점만** (B방식).
13. **QR 출석 방식** (2026-06-05 확정): **B방식** — 보호자/이용자가 **지점 입구 QR**을 스캔. 수기(직원)와 병행. A방식(직원이 이용자 QR 스캔)은 MVP 제외.
14. **사업 모델** (2026-06-05 확정): **전국 판매용 B2B SaaS**. 고객 1법인 = Organization(Tenant). 테넌트 간 데이터 완전 격리.
15. **1주차 완료 범위** (2026-06-05 확정): 6역할 로그인·메뉴·권한·홈 화면 **전부** 1주차 완료 기준에 포함.
16. **QR 스캔 계정 정책** (2026-06-05 확정): **안 3** — `guardian` 항상 + `client_user`(이용자 본인) 조건부, Organization `allow_client_self_checkin` 설정.
17. **배포 클라우드** (2026-06-05 확정): AWS/GCP/NCP 등 **벤더 무관**, 구현 단계에서 선택.
18. **목표 런칭 일정** (2026-06-05 확정): **일정 무관** — 특정 출시 데드라인 없음.
19. **이용자–보호자 연결** (2026-06-06 확정): 주간보호센터 **이용자마다 보호자 1명 이상** `guardian_clients` 연결 필수. 등록 API `primaryGuardian` 동시 제출, `clients.guardian_link_status` (V39).
20. **보호자 알림 채널** (2026-06-06 확정): **v1.1** = 인앱·FCM·이메일(무료) 골격 / **v2** = **카카오톡 채널 알림톡** + SMS fallback (US-J03).
19. **파일럿 운영 센터** (2026-06-05 확정): **있음** — 실제 운영 센터에서 테스트·피드백 수집 예정.
20. **신규 고객 등록** (2026-06-05 확정): **A — ogada 직원** (`platform_admin`). `/platform` 화면 MVP 포함.
21. **청구·정산** (2026-06-05 확정): MVP v1 **포함** (급여 계산, 월별 청구서).
22. **파일럿 현장 사용** (2026-06-05 확정): 지점 **2곳**, 센터장 **1명**, 요양보호사 **5명**.
23. **벤치마킹 참고 서비스** (2026-06-05): **케어포** (사용자 지정). 이지케어·엔젤시스템·롱텀 비교 조사 (REQUIREMENTS §1-5).
24. **청구 MVP 방식** (2026-06-05 확정): 케어포식 2단계 (내부계산+엑셀import).
25. **파일럿 참여 역할** (2026-06-05 확정): 센터장 + 요양보호사만.
26. **수가표 관리 방식** (2026-06-05 확정): **B방식** — `hq_admin`이 화면에서 등급별·연도별 수가를 입력·수정. 코드 고정 금지, 버전 이력 보존. (`fee_schedules` 엔티티)
27. **본인부담률 관리** (2026-06-05 확정): **이용자별 구분 저장** — 일반 15% / 감경 9% / 감경 6% / 기초수급 0%. 비율은 테이블화(`copay_rates`)하고 이용자는 구분 코드(`clients.copay_type`) 보유. 청구 계산 시 이용자별 비율 적용.
28. **주민등록번호 처리** (2026-06-05 확정): **수집함**. 근거 = 공단 청구명세서 법정 필수 항목(노인장기요양보험법 시행규칙). 정책 = ① 암호화 저장(PIPA §24-2) ② 화면·목록·로그 마스킹 ③ 별도 수집·이용 동의 ④ 청구·법정 목적 외 사용 금지·접근 audit_log. (REQUIREMENTS §3-2-1)
29. **청구 2단계 모델 유지** (2026-06-06, benchmark_researcher): 내부계산 + 롱텀(기관) + 엑셀 import + 본인부담 — 케어포·이지케어 업계 표준과 동일. 공단 직접 API·CMS·보호자 발송은 후속.
30. **QR B방식 차별화 유지** (2026-06-06): 보호자/이용자→지점 QR. NFC/RFID(케어포·이지케어) MVP 불필요 — 하드웨어 없이 파일럿 검증.
31. **`platform_admin` Tenant 개통 유지** (2026-06-06): 경쟁사 셀프/상담 가입과 의도적 차별 — 전국 B2B SaaS 온보딩.
32. **다지점 HQ 대시보드 Must** (2026-06-06): 경쟁사 공개 자료 동등 기능 미확인 — 파일럿 2지점 핵심 차별화.
33. **NHIS reconciliation UI Must** (2026-06-06): `MATCHED`/`DISCREPANCY`/`UNMATCHED` 행 매칭·수동 보정 — US-G06, API_SPEC §7-4, V19+ DB 제약.
34. **평가·재무회계·CMS·이동서비스 MVP 제외 유지** (2026-06-06): v2(CMS)·v3(프로그램·평가)·Won't(회계).
35. **가격 벤치마크 참고** (2026-06-06): 케어포 주야간 월 33,000원(VAT 포함) — ogada tier 정책은 영업 별도(추가질문 #31).
36. **NHIS 엑셀 `처리상태` 선행열 스킵** (2026-06-06, 3차 benchmark): import 파서 Must — 케어포 [44438](https://www.carefor.co.kr/cs/view_notice.php?calmgno=44438). 파일럿 샘플과 병행 검증(G7).
37. **롱텀 2026.01.16 개편** (2026-06-06, 3차): IE 불가, Chrome/Edge 필수 — import UI·온보딩 가이드에 반영.
38. **G8 보호자 초대·명세 v1.1** (2026-06-06, 3차): 이지케어 EZCARE 앱 패턴 — US-J01·J02, ROADMAP v1.1 Must.
39. **다지점 HQ 차별 재확인** (2026-06-06, 3차): 경쟁사 1기관번호=1계정(△), ogada Org-Branch `/dashboard/hq` 유지.
40. **엔젤 CMS TCO** (2026-06-06, 3차): 월 30,000원+건당 수수료 — v2 CMS·가격 정책 입력(#31).
41. **이관 규율 — develop 커밋 우선** (2026-06-06, QA 반영): coder는 완료 즉시 **develop에 커밋**하고, QA_FEEDBACK `Fixed`는 **develop HEAD에 산출물이 존재할 때만** 기록한다. test working tree 로컬 변경만으로 Fixed·ready 금지 (QA-B01·B02·B04·H02·H03 재발 방지, ROADMAP `## QA 피드백 반영`).
42. **수가 시간대 1밴드 → 다밴드** (2026-06-06, 4차 벤치마크 G9): 2026 공단 수가는 **등급×이용시간대** 2차원. v1은 파일럿 센터 **표준 이용시간 1밴드 고정**, **v1.1에서 `duration_band` 다밴드** 도입 — §3-9-1·ERD 보강(추가질문 #35).
43. **프론트 v1.1 실 API 연동 규약** (2026-06-06, QA-H04·M01): v1.1 Must 화면은 **JWT로 `/api/v1/*` 호출**(localStorage 데모 제거) + **Vitest 회귀**가 충족돼야 스토리 인수 완료 — USER_STORIES §16.
44. **이관 규율 강화 — Fixed↔develop HEAD 검증 게이트** (2026-06-06, 6차, QA-H01·H02 false Fixed 회귀): 결정 41(develop 커밋 우선)에도 불구하고 backend `Fixed`(QA-H01·SEC-001/002/004)가 **test working tree에만 존재**하고 develop HEAD에 미반영된 채 기록되어 TSR 재검증(07:52)에서 Open 복귀했다. → **`Fixed` 기록·완료 기준 `[x]`는 `git show develop:<path>`로 산출물이 develop HEAD에 존재함을 검증한 뒤에만 유효**하다(ROADMAP 이관 규율 5항). 미커밋·stash·working tree 근거 `Fixed`/`[x]`는 무효이며 재검증 시 Open 복귀·체크박스 철회. coder는 `Fixed` 기록 전 `git -C src/backend show develop:<경로>`(또는 frontend)로 자기검증한다.
45. **dirty-tree 재오염·API 계약 변경 문서화 게이트 + createClient 보호자 계약 확정** (2026-06-06, 7차, QA-B06·B07·H04·M01·SEC-005): … v1.1 완료 기준 H04·M01 `[x]` 철회.
46. **프론트 파비콘 v1.1 Must** (2026-06-06, 사용자): UXD §9 → COD `public/`·`index.html` (US-UX-01).
47. **BNK 6차 → v1.2 기능 밀도** (2026-06-06, 사용자): 경쟁사 메뉴·화면 전수 매핑 후 P0~P2 백로그 (ROADMAP v1.2).
48. **docs 역할별 하위 폴더** (2026-06-06, 사용자): `docs/README.md` + planning/product/technical/qa/security/ops — 삭제 없이 분류만.
49. **v1.2 화면 커버 KPI ≥60%** (2026-06-06, BNK-6 확정): SideNav 2단 + P0 5건(보호자·입금·미납·등급이력·실데이터 대시보드) — 모듈 가중 커버리지 25~30%→≥60%. `ROADMAP v1.2` 완료 기준.
50. **v1.2 선행 dirty-tree 금지** (2026-06-06, 12차, QA-B07 recurrence): v1.1 `merge_status: merged` 전 v1.2 P0 착수 시에도 **완료 단위 develop 커밋** 또는 **stash/revert**로 working tree clean 유지(이관 규율 7). HEAD @ `998ac87` v1.1 Fixed(B07·B04) **유효** — recurrence는 v1.2 미커밋 작업.
51. **WIP 커밋 전 품질 게이트** (2026-06-06, 13차, TSR 16차·FE-7): frontend v1.2 WIP develop 커밋 전 **`npm test`·`npm run build` PASS** 필수 — duplicate symbol 등으로 build/test FAIL 상태 커밋 금지. backend RBAC WIP도 **`mvn -q test` PASS** 후 커밋(BE-6, B02 recurrence).
52. **v1.2 P0 산출물 v1.1 merge 동반 흡수** (2026-06-06, 16차, TSR 21차 후속): v1.1 `merge_status: merged` 전 develop에 선행 커밋된 v1.2 P0 산출물(`a72e249` — `GuardiansPage`·`GuardianDetailPage`·`PaymentPage`·`OverduePage`·`BillingDetailPage`·`SideNav` 2단·`routeAccess.js`·`SessionTimeoutProvider`·`MaskedPhone`·`QrScanPanel` 등 42 files)은 **v1.1 develop→test merge에 동반 흡수**한다. 별도 v1.2 merge 라운드 추가하지 않고, v1.1 merge ready 게이트는 **v1.1 완료 기준만으로 평가**(7역할 E2E·Must API E2E·J01). v1.2 P0의 정식 완료 기준(2단 SideNav 모듈 가중 커버리지 ≥60%·실데이터 위젯 E2E·등급이력 UI·보호자 CRUD·입금·미납 E2E)은 **v1.1 merged 이후 v1.2 사이클**에서 평가한다. 근거: ① develop 커밋 `a72e249`는 working tree clean·HEAD `npm test` 10/4·build 110 modules PASS로 회귀 위험 낮음(이관 규율 5·6·7 PASS), ② v1.2 P0 산출물이 v1.1 라우팅·세션 인프라(`routeAccess.js`·`SessionTimeoutProvider`)와 결합되어 분리 매우 비효율, ③ 결정 18 「기능 폭보다 출시 속도」 우선. v1.2 status는 `planned→in_progress`로 갱신(P0 develop 선행 커밋 반영).
53. **v2 선행 dirty-tree 금지** (2026-06-07, 24차, QA-B08): v1 `merge_status: merged` **후** v2(`status: in_progress`) 착수 시에도 **완료 단위 develop 커밋** 또는 **stash/revert**로 working tree clean 유지(이관 규율 8). v2 산출물(`notification_preferences`·V41 등)을 working tree에만 두면 **B08 recurrence BLOCK**. v1 완료 기준 `[x]`는 develop HEAD 산출물 존재 시에만 유효(규율 5).
54. **backend develop→test merge 분리 정책** (2026-06-07, 32차, TSR 48차; **36차 갱신**): develop HEAD `428ba7d`(COD 36 V42 + `NotificationPreferenceServiceTest` 4 @Test 포함, `c3b8716`+2커밋 `feac558`·`c3b8716` + COD 36 +1)가 test `@e8750d2` 대비 **3 ahead**. → ① **v1 보완 merge 즉시 권고** — `428ba7d` HEAD를 develop→test merge(**3커밋 일괄**). ② **v2 `notification_preferences`·V42 test 검증은 v2 사이클 별도 평가** — 결정 52 패턴과 동일, ROADMAP v2 `merge_status: pending` 유지·v2 완료 기준(BE-7 `[x]`·알림톡 E2E 등) 충족 후 v2 ready.
55. **파일럿 1주차 우선 업무 3가지** (2026-06-07, 사용자 위임·planner 확정): ① **P1 이용자 등록+대표 보호자 연결**(센터장) ② **P2 수기 출석 체크인/아웃 10명**(요양보호사) ③ **P3 일일 건강·투약 기록**(요양보호사). 2주차+: P4 지점 B·P5 대시보드·P6–P8 월말 청구·NHIS. 근거: 일일 운영 루프·파일럿 역할·데이터 선행 관계(REQUIREMENTS §1-3-1·USER_STORIES §13).
56. **사용자 우선순위 = develop→test merge 검증** (2026-06-07): backend `428ba7d` HEAD Fixed·**WT DIRTY 27 files(B09)**·3 ahead → **B09(BE-8) 선행 후 merge**. frontend B07 #6(FE-18·FE-19) dirty-tree + **FE-7 FAIL(H05)** 해소 후 v1.1 ready → merge. coder→tester 순서 명시(REQUIREMENTS §1-3-1 merge 표).

---

### [PLN] QA 피드백 반영 (2026-06-08, 42차 — TSR 58·59 + BNK-8 + baseline 회귀·Open 4→Planned)

> **42차 자동 기획 동기화** — TSR 58(backend)·59(frontend) + BNK-8. QA Open **4건→Planned** · B09·SEC-D8 **Fixed @ `f47ffa1`**.

| 항목 | 42차 관측 | 조치 |
|------|----------|------|
| **QA-B10** | test `@2799e29`(79/79) vs merged `e8750d2` · develop `@f47ffa1` v1 E2E **ABSENT** | **BE-10** · ROADMAP v1 test merge 주석 · `#42` 결정 대기 |
| **SEC-D11** | backend develop `f47ffa1`·test `2799e29` · frontend `e5fd48d`(develop=test) vs TSR baselines | **INFRA-B12** |
| **SEC-D12** | HEAD `@e5fd48d` route 무방비 · `ProtectedRoute` ABSENT | **INFRA-B12** checkout `d5654c0` 또는 **FE-20** |
| **QA-B11** | frontend develop·test 동일 `@e5fd48d` · TSR57 `d5654c0` 18 behind | **INFRA-B12** |
| **BNK-8** | 케어포 지도보기 확인 → v1.3-A=패리티 · v1.3-B=차별화 | REQUIREMENTS §1-5-3 · ROADMAP v1.3 · Epic T |
| **B09 Fixed** | J01 API @ `f47ffa1` HEAD PRESENT · merge **1 commit** | BE-8 Fixed · backend merge gap 3→1 |

**coder 다음 액션 (42차)**: ⓪ **INFRA-B12**(submodule checkout) → ① **BE-10**/#42 baseline 결정 → ② **FE-19** → ③ **FE-18** → ④ backend merge(1 @ `f47ffa1`) → ⑤ **B03**.

### [PLN] QA 피드백 반영 (2026-06-08, 41차 — BNK-7 G15/G16 v1.3 명시 + submodule·QA 재확인·Open 0건)

> **41차 자동 기획 동기화** — QA Open **0건**·TEST_REPORT 최종 **TSR 57**(frontend)·**TSR 56**(backend)·SEC 4차 **Planned**. **BNK-7 planner 권고(§10-3·§10-5) 문서화** — v1.3-A 「운영 시각화 한정」·v1.3-C G15/G16 완료 기준·US-T05 신설.

| 항목 | 41차 관측 | 조치 |
|------|-----------|------|
| QA Open | **0건** | Planned BLOCK 5건 유지(B03·merge·B09·B07 #6·H05) |
| BNK-7 v1.3 | G15(법정 서식)·G16(차량·이동서비스비) | **ROADMAP v1.3-A/C 완료 기준·REQUIREMENTS §1-5-1·§3-13·USER_STORIES US-T05** 갱신 |
| ogada workspace | 40차와 **동일** — backend stale·WT 9U(V35~V43 only) · frontend stale·WT CLEAN | checkout **`428ba7d`/`d5654c0`** 선행 불변 |
| TSR baseline | develop backend **`428ba7d`** · frontend **`d5654c0`** | 56·57차 기준 **유지** |

**coder 다음 액션 (41차, 우선순위 — 40차 동일)**: ⓪ submodule checkout → ① **FE-19** → ② **FE-18** → ③ **BE-8** → ④ backend merge → ⑤ **B03**.

---

### [PLN] QA 피드백 반영 (2026-06-08, 40차 — 벤치마크·QA 재확인 + submodule 드리프트 부분 개선·TSR 57 baseline 유지·Open 0건)

> **40차 자동 기획 동기화** — QA Open **0건**(38~39차 Planned 유지)·TEST_REPORT 최종 **TSR 57**(frontend)·**TSR 56**(backend)·SEC 4차 **Planned**. BNK-7(§10)·COMPETITOR_MATRIX §9·결정 60~62·G15/G16→v1.3-C — **38차 반영 완료·신규 기획 변경 없음**.

| 항목 | 40차 관측 | 조치 |
|------|-----------|------|
| QA Open | **0건** | Planned BLOCK 5건 유지(B03·merge·B09·B07 #6·H05) |
| BNK-7 v1.3 | G15(법정 서식)·G16(차량·이동서비스비) → **v1.3-C** | ROADMAP v1.3·REQUIREMENTS §3-13 반영 확인 — 변경 없음 |
| ogada workspace | `src/backend` @ **`2799e29`**(stale) · WT **9U**(V35~V43) · `src/frontend` **init** @ **`e5fd48d`**(stale) · WT **CLEAN** | **부분 개선**(39차 frontend 부재→복구) — checkout 후 coder/tester 재개 |
| TSR baseline | develop backend **`428ba7d`** · frontend **`d5654c0`** | 38차·56·57차 기준 **유지** |

**coder 다음 액션 (40차, 우선순위 — 38~39차 동일, 선행: submodule checkout)**: ⓪ **`git submodule update --init --recursive`** 후 **backend `git checkout 428ba7d`**·**frontend `git checkout d5654c0`**. ① **FE-19(H05+SEC-D9)** — MaskedPhone 테스트 정합 → WT `npm test` PASS. ② **B07 #6(FE-18)** — 20 files WIP develop 커밋. ③ **B09(BE-8+SEC-D8)** — J01 API + SecurityConfig 검증 → develop 커밋. ④ **backend merge** — B09 해소 후 3커밋 merge. ⑤ **B03** — v1.1 Must 라이ve E2E → frontend merge.

---

### [PLN] QA 피드백 반영 (2026-06-07, 39차 — 벤치마크·QA 재확인 + ogada workspace submodule 드리프트·TSR 57 baseline 유지·Open 0건)

> **39차 자동 기획 동기화** — QA Open **0건**(38차 Planned 유지)·TEST_REPORT 최종 **TSR 57**(frontend)·**TSR 56**(backend)·SEC 4차 **Planned**. BNK-7(§10)·COMPETITOR_MATRIX §9·결정 60~62·G15/G16→v1.3-C — **38차 반영 완료·신규 기획 변경 없음**.

| 항목 | 39차 관측 | 조치 |
|------|-----------|------|
| QA Open | **0건** | Planned BLOCK 5건 유지(B03·merge·B09·B07 #6·H05) |
| BNK-7 v1.3 | G15(법정 서식)·G16(차량·이동서비스비) → **v1.3-C** | ROADMAP v1.3·REQUIREMENTS §3-13 반영 확인 — 변경 없음 |
| ogada workspace | `src/backend` @ **`2799e29`**(stale) · WT 8U(V35~V42) · `src/frontend` **부재** | **블로커** — submodule init/checkout 후 coder/tester 재개 |
| TSR baseline | develop backend **`428ba7d`** · frontend **`d5654c0`** | 38차·56·57차 기준 **유지** |

**coder 다음 액션 (39차, 우선순위 — 38차 동일, 선행: submodule 동기화)**: ⓪ **`git submodule update --init --recursive`** — backend develop `428ba7d`·frontend develop `d5654c0` checkout. ① **FE-19(H05+SEC-D9)** — MaskedPhone 테스트 정합 → WT `npm test` PASS. ② **B07 #6(FE-18)** — 20 files WIP develop 커밋. ③ **B09(BE-8+SEC-D8)** — J01 API + SecurityConfig 검증 → develop 커밋. ④ **backend merge** — B09 해소 후 3커밋 merge. ⑤ **B03** — v1.1 Must 라이ve E2E → frontend merge.

---

### [PLN] QA 피드백 반영 (2026-06-07, 38차 — SEC 4차 SEC-D8·SEC-D9 Open→Planned·BE-8·FE-19 보안 게이트·Open 0건)

> **SEC 4차 재점검(12:49 UTC)** — 37차 TSR 56·57차 반영 후 security_auditor가 등록한 **Open 2건**을 planner가 태스크화. ① **SEC-20260607-009**(SEC-D8) J01 `SecurityConfig` 공개 endpoint 허용 범위·`InvitationTokenService` 단일사용·만료·rate limit — **BE-8 commit/merge 금지** 게이트·API_SPEC §4-1·SECURITY_CHECKLIST H-6. ② **SEC-20260607-010**(SEC-D9) `GuardianListCard` MaskedPhone PII `010-****-5678` 유지·테스트 정합 — **FE-19**·QA-H05 동반·마스킹 제거 시 BLOCK 격상.

| QA/SEC id | sev | ver | 38차 관측 | 상태 |
|-----------|-----|-----|-----------|------|
| SEC-20260607-009 | BLOCK | v1.1 J01 | SEC-D8 — `SecurityConfig` modified(HEAD ABSENT)·accept endpoint 공개 허용 범위 미검증 | **Planned → BE-8 보안 게이트** |
| SEC-20260607-010 | MEDIUM | v1.1 FE-7 | SEC-D9 — MaskedPhone 마스킹 vs 테스트 평문 불일치·PII 노출 방지 | **Planned → FE-19 보안 게이트** |
| QA-20260607-B09 | BLOCK | v1.1 J01 | TSR 56 — 27 files J01 API WIP·**SEC-D8 동반** | **Planned → BE-8** |
| QA-20260607-H05 | HIGH | v1.1 FE-7 | TSR 57 — MaskedPhone vs 테스트·**SEC-D9 동반** | **Planned → FE-19** |

**BE-8 보안 게이트 체크리스트(SEC-D8)**: ① `SecurityConfig` 허용 경로 = `/guardian/invitations/{token}/accept` **단일** ② `InvitationTokenService` 토큰 단일사용(used_at/상태)·만료(exp)·128-bit 엔트로피 ③ `GlobalExceptionHandler` 토큰 값·내부 상세 미노출 ④ 초대 endpoint rate limit(IP/email).

**FE-19 보안 게이트 체크리스트(SEC-D9)**: ① `GuardianListCard.jsx` `MaskedPhone` 렌더링 `010-****-5678` 유지 ② 테스트 assertion·`aria-label` 마스킹 값 정합 ③ FE-7 PASS 후 develop 커밋 — **마스킹 제거 방향 변경 금지**.

**coder 다음 액션 (38차, 우선순위)**: ① **FE-19(H05+SEC-D9)** — MaskedPhone 테스트 정합 → WT `npm test` PASS. ② **B07 #6(FE-18)** — 20 files WIP develop 커밋. ③ **B09(BE-8+SEC-D8)** — J01 API + SecurityConfig 검증 → develop 커밋. ④ **backend merge** — B09 해소 후 3커밋 merge. ⑤ **B03** — v1.1 Must 라이ve E2E → frontend merge.

---

### [PLN] QA 피드백 반영 (2026-06-07, 37차 — TSR 56·57차 + backend B09 Planned·BE-8 J01 API WIP + frontend H05 Planned·FE-19·B07 #6 20 files·#36 양 스트림 재오픈·Open 0건)

> **TSR 56차(10:01, backend)** 54차 `428ba7d` **CLEAN→DIRTY** — **15M+12U=27 files** J01 `guardian_invitations` WIP(`GuardianInvitationController`·DTO 4종·`GuardianInvitationService`·`InvitationTokenService`·`V43__guardian_invitations.sql`·`GuardianInvitationServiceTest` untracked + Client/Security/테스트 15종 modified). **HEAD `428ba7d` Fixed(B02 #6·B08 #2) 규율 5 유효**. WT `mvn test` **253/253 PASS**·develop **3 ahead of test**. → **QA-B09 Open→Planned**·**BE-8**·**API_SPEC §4-1**·#36 **backend BE-6 #7 재오픈**. **TSR 57차(10:11, frontend)** 55차 15→56차 18→**57차 20 files**(+`PaymentRecordModal`+test·`ClientPhotoField.test`·`GuardianListCard.test`·`ClientFormPage`). WT build **758 modules PASS**·WT `npm test` **209/210 FAIL** — `GuardianListCard.test.jsx` MaskedPhone 불일치(**FE-7**). → **QA-H05 Open→Planned**·**FE-19**·B07 #6 commit 게이트에 FE-7 선행.

| QA id | sev | ver | 37차 관측 | 상태 |
|-------|-----|-----|-----------|------|
| QA-20260607-B09 | BLOCK | v1.1 J01 | TSR 56 — 27 files J01 API WIP·WT `mvn test` 253/253·HEAD `428ba7d` Fixed 규율 5 유효 | **Planned → BE-8** |
| QA-20260607-H05 | HIGH | v1.1 FE-7 | TSR 57 — GuardianListCard MaskedPhone vs 테스트·209/210 FAIL·B07 #6 범위 | **Planned → FE-19** |
| QA-20260606-B07 | BLOCK | v1.1 | TSR 57 — **20 files** WIP·WT build PASS·**npm test FAIL**·HEAD `d5654c0` Fixed | **recurrence #6 Planned (FE-18+FE-19)** |
| BE-8 | — | v1.1 J01 | J01 `guardian_invitations` API(V43·Controller·Service·token) **완료 단위 develop 커밋** | Planned |
| FE-19 | — | v1.1 FE-7 | `GuardianListCard.test.jsx` **MaskedPhone** 마스킹·`aria-label` 검증 정합 → `npm test` PASS | Planned |
| QA-20260606-B03 | BLOCK | v1.1 | frontend merge 18 ahead + backend merge 3 ahead @ `428ba7d` + **B09·B07 #6·H05** 선행 | Planned(잔존) |

**#36 에스컬레이션 — 양 스트림 재오픈(37차)**: 36차 backend BE-6/BE-7 해소 직후 **B09 recurrence(BE-6 #7)** + frontend **FE-6 #5 지속**(B07 #6 + FE-7 H05). 결정 63 운영 게이트(build 대기) 유지.

**coder 다음 액션 (37차, 우선순위)**: ① **FE-19(H05)** — `GuardianListCard.test.jsx` MaskedPhone 정합 → WT `npm test` PASS(FE-7). ② **B07 #6(FE-18)** — 20 files WIP **완료 단위 develop 커밋** → tree clean. ③ **B09(BE-8)** — J01 API WIP + API_SPEC §4-1 정합 → develop 커밋 → tree clean. ④ **backend merge** — B09 해소 후 develop→test **`428ba7d` 3커밋** merge(결정 54). ⑤ **B03** — v1.1 Must 라이ve E2E·J01 E2E → `merge_status: ready` → frontend merge(18 ahead).

---

### [PLN] QA 피드백 반영 (2026-06-07, 36차 — TSR 54·55차 + backend B02 #6·B08 #2 Fixed `428ba7d`·#36 BE-6/BE-7 해소 + frontend B07 recurrence #6 Open→Planned·FE-18·Open 0건)

> **TSR 54차(09:23, backend)** 53차 `c3b8716` DIRTY → develop HEAD **`428ba7d`**(+1 COD 36차 V42 consent CHECK·temporal + `NotificationPreferenceServiceTest` 4 @Test), working tree **DIRTY→CLEAN**. **QA-B02 recurrence #6·QA-B08 recurrence #2 정식 Fixed — TSR 독립 검증 PASS**: `git cat-file -e HEAD:` V42·domain test **PRESENT**(이관 규율 5·6·8 PASS). develop HEAD `mvn test` **253/253 PASS**·test **213/213 PASS**. develop **3커밋 ahead of test** — merge 미실행(결정 54 갱신). **#36 backend BE-6 #6·BE-7 #2 해소**. **TSR 55차(09:29, frontend)** 53차 `d5654c0` **CLEAN→DIRTY** — **11M+4U=15 files**(`DateInput`+test·`GuardianInvitationList`+test J01 목록·`ClientDetailPage` 보호자/초대·`GuardianInviteModal`·`GuardianListCard`·`LoginHistoryPanel`·`AuditLogPanel`·`ClientPhotoField`·`services.js`·`GuardianInvitationAcceptPage`+test·`components.css`). **HEAD `d5654c0` Fixed(FE-17·B07 #5) 규율 5 유효**. WT `npm test` **205/42 PASS**(+6/+2)·build **758 modules**·audit **0**. → **QA-B07 recurrence #6 Open→Planned**·**FE-18** 매핑·#36 **frontend FE-6 #5 재오픈**.

| QA id | sev | ver | 36차 관측 | 상태 |
|-------|-----|-----|-----------|------|
| QA-20260606-B02 | BLOCK | v1 | TSR 54 COD 36 `428ba7d` — V42 + `NotificationPreferenceServiceTest` 4 @Test develop 커밋·WT **CLEAN**·253/253·이관 규율 5·6·8 PASS | **recurrence #6 Fixed** |
| QA-20260607-B08 | BLOCK | v2 | TSR 54 COD 36 `428ba7d` — V42 follow-up develop HEAD PRESENT·WT **CLEAN** | **recurrence #2 Fixed** |
| QA-20260606-B07 | BLOCK | v1.1 | TSR 55 — 15 files WIP(DateInput·GuardianInvitationList J01·ClientDetail 보호자/초대)·WT 205/42·758 modules·HEAD `d5654c0` Fixed 규율 5 유효 | **recurrence #6 Planned** |
| FE-18 | — | v1.1 J01 | `DateInput`(DS)·`GuardianInvitationList`(J01 초대 목록)·`ClientDetailPage` 보호자/초대 UI·관련 패널 연동 WIP **완료 단위 develop 커밋** | Planned |
| QA-20260606-B03 | BLOCK | v1.1 | frontend merge 18 ahead + backend merge 3 ahead @ `428ba7d` + J01 백엔드 API·라이ve E2E | Planned(잔존) |

**#36 에스컬레이션 — backend 해소·frontend FE-6 #5 재오픈(36차)**: backend COD 36 `428ba7d`로 **B02 #6·B08 #2 종결**(working tree CLEAN). frontend는 53차 `d5654c0` CLEAN 직후 **B07 #6 recurrence** → **FE-6 #5**. 결정 56 운영 게이트(pre-commit hook·CI fail-fast) 권고는 **frontend 한정** 유지(결정 53·56 — backend 패턴 해소 후 frontend 재발).

**coder 다음 액션 (36차, 우선순위)**: ① **B07 #6(FE-18)** — DateInput·GuardianInvitationList·ClientDetail J01 WIP **완료 단위 develop 커밋**(FE-6·규율 7) → working tree clean. ② **backend merge** — develop→test **`428ba7d` 3커밋** 일괄 merge(결정 54 갱신). ③ **J01** — API_SPEC §4·DBA `guardian_invitations`(#33·#35 결정 후) → 백엔드 초대/수락/목록 API → FE-17·FE-18 실 API 연동. ④ **B03** — v1.1 Must 라이ve E2E 완료 → `merge_status: ready` → frontend develop→test merge(18 ahead). ⑤ **결정 56** — frontend pre-commit/CI fail-fast 구현(별도 build 사이클).

---

### [PLN] QA 피드백 반영 (2026-06-07, 35차 — TSR 53차 + frontend B07 recurrence #5 정식 Fixed `d5654c0`·FE-17 J01 수락 UI 충족·frontend 잔여 BLOCK B03 단일 + backend 51차 대비 불변·B02 #6/B08 #2 Planned·domain test 3→4 @Test·#36 backend 단독 재축소·Open 0건)

> **TSR 53차(08:36, frontend)** 52차 `0b9b001` **DIRTY 20 files(B07 #5 Open)** → develop HEAD `0b9b001`→**`d5654c0`**(+1커밋 COD 35차 `feat(v1.1): FE-17 J01 보호자 초대 수락 UI·LogoutButton·레이아웃 회귀 (B07 #5)`, 25 files +823/-57, **18 ahead**), working tree **DIRTY→CLEAN**. **QA-B07 recurrence #5 정식 Fixed — TSR 독립 검증 PASS**: `git -C src/frontend status --porcelain` **0줄**, `git cat-file -e HEAD:` `LogoutButton.jsx`(+test)·`GuardianInvitationAcceptPage.jsx`(+test)·`GuardianInvitationAcceptForm.jsx`·`PublicAuthLayout.jsx`·`BillingPage.layout.test.jsx`·`services.js`(`acceptGuardianInvitationApi`) **전부 PRESENT**(이관 규율 5·6·7 PASS). SEC-005 AuthContext localStorage/sessionStorage **0건**. HEAD `npm test` **199/40 PASS**·build **756 modules**(3청크 최대 393.53 kB)·audit **0**. → **FE-17 develop HEAD 반영 확정**(결정 52 흡수 ⑪묶음)·**잔여 frontend BLOCK = B03 merge 게이트 단일**(develop→test **18커밋** 미머지·완료 기준 Must 라이ve E2E·J01 백엔드 API). **TSR 53차(17:32, backend)** 51차 대비 **HEAD·dirty-tree·merge 완전 불변** — develop HEAD `c3b8716`·WT **DIRTY** 2 untracked(V42 consent CHECK·temporal + `NotificationPreferenceServiceTest` **3→4 @Test**) **HEAD ABSENT**(규율 5·6·8 — v2 follow-up 미커밋). **HEAD `c3b8716` Fixed(B02 #5·B08) 규율 5 유효**. test `mvn test` **213/213**·WT **253/253 PASS**(+1)·develop **2 ahead of test**(merge 미실행, 결정 54). **B02 #6·B08 #2 Planned 유지**.

| QA id | sev | ver | 35차 관측 | 상태 |
|-------|-----|-----|-----------|------|
| QA-20260606-B07 | BLOCK | v1.1 | TSR 53 COD 35차 `d5654c0` 25 files 일괄 커밋·WT **CLEAN**·`git cat-file -e HEAD:` 산출물 PRESENT·199/40·756 modules·이관 규율 5·6·7 PASS | **recurrence #5 Fixed** |
| FE-17 | — | v1.1 J01 | `GuardianInvitationAcceptPage`(+test)·`LogoutButton`(+test)·`BillingPage.layout.test`·`acceptGuardianInvitationApi`·AuthContext logout develop HEAD `d5654c0` 반영 | **Fixed @HEAD**(API 연동은 백엔드 J01 후) |
| QA-20260606-B02 | BLOCK | v1 | TSR 53 불변 — V42 + `NotificationPreferenceServiceTest`(4 @Test) WT untracked·HEAD ABSENT. **HEAD `c3b8716` Fixed(B02 #5) 규율 5 유효** | **recurrence #6 Planned** |
| QA-20260607-B08 | BLOCK | v2 | TSR 53 불변 — V42 follow-up WT untracked·HEAD ABSENT. **V41+8@Test HEAD PRESENT 유효** | **recurrence #2 Planned** |
| QA-20260606-B03 | BLOCK | v1.1 | J01 백엔드 API·라이ve E2E·merge 게이트 잔존(18 ahead) | Planned(잔존) |

**#36 에스컬레이션 — backend 단독 재축소(35차)**: 34차 양 스트림 재오픈에서 frontend는 COD 35차 `d5654c0` commit으로 **B07 #5(FE-6 #4) 종결**(working tree CLEAN·FE-17 충족) → 에스컬레이션이 **backend 단독(BE-6 #6·BE-7 recurrence #2)**으로 재축소(33차 비대칭 회귀). backend는 TSR 50·51·53차 3회 연속 V42 + `NotificationPreferenceServiceTest` 미커밋 잔존. → 결정 53 운영 게이트(pre-commit hook `git diff --quiet -- src/test` + V*.sql·CI fail-fast) 권고를 **backend 스트림 한정**으로 유지.

**coder 다음 액션 (35차, 우선순위)**: ① **B02 #6·B08 #2** — `V42__guardian_notification_preferences_consent_temporal.sql` + `NotificationPreferenceServiceTest`(4 @Test) **완료 단위 develop 커밋**(BE-6·BE-7·규율 8) 또는 stash/revert → working tree clean → 자동 Fixed. ② **backend merge** — develop→test `c3b8716` 2커밋 일괄 merge(결정 54). ③ **J01** — API_SPEC §4·DBA `guardian_invitations`(#33·#35 결정 후) → 백엔드 초대/수락 API → FE-17 `GuardianInvitationAcceptPage`·`acceptGuardianInvitationApi` 실 API 연동(현재 fetch-mock/스텁). ④ **B03** — v1.1 Must 라이ve E2E 완료 → `merge_status: ready` → frontend develop→test merge(18 ahead·FE-15·FE-16·FE-17 흡수). ⑤ **v1.2 KPI** — SideNav ≥60%·P0 E2E는 v1.1 merged 후.

---

### [PLN] QA 피드백 반영 (2026-06-07, 34차 — TSR 51·52차 + backend COD 35 false Fixed 철회·B02 #6/B08 #2 Planned 유지 + frontend B07 recurrence #5 Open→Planned·J01 수락 UI WIP·FE-17·#36 양 스트림 재오픈·Open 0건)

> **TSR 51차(07:58, backend)** 50차 대비 **상태 완전 불변·coder 미조치** — develop HEAD `c3b8716`·WT **DIRTY** 2 untracked(V42 + `NotificationPreferenceServiceTest` 3 @Test) **HEAD ABSENT**. **COD 35 Fixed 주장 TSR FAIL** → ROADMAP v1 QA-B02 `[x]`·v2 B08 recurrence #2 `[x]` **철회**. B02 #6·B08 #2 **Planned 유지**. test `mvn test` **213/213**·WT **252/252 PASS**·develop **2 ahead of test**. **TSR 52차(08:03, frontend)** 50차 `0b9b001` **CLEAN→DIRTY 재오염** — 15M+5U=**20 files**(`LogoutButton`·`BillingPage.layout.test`·`GuardianInvitationAcceptPage`+test J01·AuthContext·Recharts·청구/보호자 페이지). **HEAD `0b9b001` Fixed(FE-15·FE-16) 규율 5 유효**. WT `npm test` **194/38 PASS**·build **754 modules**·audit **0**. → **QA-B07 recurrence #5 Open→Planned**·**FE-17(J01 수락 UI·LogoutButton·레이아웃 회귀)** 매핑.

| QA id | sev | ver | 34차 관측 | 상태 |
|-------|-----|-----|-----------|------|
| QA-20260606-B02 | BLOCK | v1 | TSR 51 COD 35 false Fixed 철회 — V42 + `NotificationPreferenceServiceTest` WT untracked·HEAD ABSENT. **HEAD `c3b8716` Fixed(B02 #5) 규율 5 유효** | **recurrence #6 Planned** |
| QA-20260607-B08 | BLOCK | v2 | TSR 51 COD 35 false Fixed 철회 — V42 follow-up WT untracked·HEAD ABSENT. **V41+8@Test HEAD PRESENT 유효** | **recurrence #2 Planned** |
| QA-20260606-B07 | BLOCK | v1.1 | TSR 52 CLEAN→DIRTY 20 files(LogoutButton·GuardianInvitationAcceptPage J01·BillingPage.layout.test). **HEAD `0b9b001` Fixed 규율 5 유효** | **recurrence #5 Planned** |
| QA-20260606-B03 | BLOCK | v1.1 | J01 백엔드 API·라이ve E2E·merge 게이트 잔존(17 ahead) | Planned(잔존) |
| FE-17 | — | v1.1 J01 | J01 수락 UI WIP(`GuardianInvitationAcceptPage`+test)·`LogoutButton`+test·`BillingPage.layout.test`·AuthContext logout·WT 194/38·754 modules | **Planned(B07 #5)** |

**#36 에스컬레이션 — 양 스트림 재오픈(34차)**: 33차 backend 단독 재오픈 직후 frontend도 COD 33·34차 연속 CLEAN 후 **B07 #5 recurrence**(FE-6 #4). backend는 COD 35 false Fixed로 B02 #6·B08 #2 **지속**. → 결정 53 운영 게이트(pre-commit hook·CI fail-fast) 권고를 **양 스트림**으로 복원.

**coder 다음 액션 (34차, 우선순위)**: ① **B02 #6·B08 #2** — V42 + `NotificationPreferenceServiceTest` 완료 단위 develop 커밋(BE-6·BE-7·규율 8) 또는 stash/revert → working tree clean. ② **B07 #5** — LogoutButton·GuardianInvitationAcceptPage(J01)·BillingPage.layout.test·AuthContext 등 **완료 단위 develop 커밋**(FE-6·FE-17) 또는 stash/revert. ③ **backend merge** — develop→test `c3b8716` 2커밋(결정 54). ④ **J01** — API_SPEC §4·DBA `guardian_invitations`(#33·#35) → 백엔드 API → FE-17 실 API 연동. ⑤ **B03** — v1.1 Must 라이ve E2E → `merge_status: ready` → frontend merge(17 ahead·FE-16·FE-17 흡수).

---

### [PLN] QA 피드백 반영 (2026-06-07, 33차 — TSR 50차 + backend B02 recurrence #6 + B08 recurrence #2 Open→Planned·V42 consent CHECK·temporal v2 follow-up 미커밋·HEAD Fixed 규율 5 유효·frontend COD 34차 ds-* 유틸리티 전환 FE-16·#36 backend 단독 재오픈·Open 0건)

> **TSR 50차(16:15, backend)** 48차 `c3b8716` **CLEAN→DIRTY 재오염** — 2 untracked: ① `V42__guardian_notification_preferences_consent_temporal.sql`(54 lines — kakao/sms 유료 채널 consent CHECK + `consent_at`/`updated_at` temporal monotonicity, API_SPEC §11-3·ERD §4-7-1 정합) ② `NotificationPreferenceServiceTest.java`(128 lines/**3 @Test** — paid channel consent stamp·upsert). develop HEAD `c3b8716` **불변**·**B02 #5·B08(`feac558`) HEAD PRESENT 유지**(이관 규율 5 — 48차 Fixed **유효**); `git cat-file -e HEAD:V42`·`NotificationPreferenceServiceTest` → **ABSENT**(규율 6·8 위반). → **QA-B02 recurrence #6 + QA-B08 recurrence #2 Open→Planned**, ROADMAP v1 QA-B02 working tree clean `[x]` 철회·v2 BE-7 **V42 consent CHECK·temporal** follow-up 완료 기준 태스크화. test `mvn test` **213/213 PASS**·develop WT **252/252 PASS**(+3)·develop **2 ahead of test**(merge 미실행). **TSR 50차(07:17, frontend)** develop HEAD `c98f98d`→**`0b9b001`**(+1커밋 COD 34차 `fix(v1.1): Must 페이지 UXD ds-* 유틸리티 전환·AttendancePage 레이아웃 회귀 테스트`, **17 ahead**), working tree **CLEAN**. 9 컴포넌트(`AttendanceAbsentModal`·`BatchProgressSteps`·`CheckoutModal`·`FeeRateHistoryPanel`·`HealthAbnormalBanner`·`MedicationDuplicateAlert`·`PasswordResetRequestModal`·`PlatformOrgDetailModal`·`SessionTimeoutModal`) 인라인 style→**ds-* 유틸리티 전환** + `AttendancePage.layout.test.jsx`. HEAD `npm test` **187/35**·752 modules·audit **0**·**신규 Open 0** → **FE-16(DESIGN_SYSTEM ds-* 마이그레이션) 매핑**.

| QA id | sev | ver | 33차 관측 | 상태 |
|-------|-----|-----|-----------|------|
| QA-20260606-B02 | BLOCK | v1 | TSR 50차 CLEAN→DIRTY 재오염(V42 + `NotificationPreferenceServiceTest` v2 follow-up 미커밋). **HEAD `c3b8716` Fixed(B02 #5) 규율 5 유효** | **recurrence #6 Planned** |
| QA-20260607-B08 | BLOCK | v2 | V41+8@Test HEAD PRESENT 유효; **V42 consent CHECK·temporal + `NotificationPreferenceServiceTest` 3 @Test 미커밋** | **recurrence #2 Planned** |
| QA-20260606-B03 | BLOCK | v1.1 | J01·라이ve E2E·v1.1 완료 기준 `[ ]` — frontend merge 게이트 잔존(17 ahead) | Planned(잔존) |
| FE-16 | — | v1.1/v1.2 | COD 34차 `0b9b001` ds-* 유틸리티 전환 9 컴포넌트·`AttendancePage.layout.test.jsx`·187/35·WT CLEAN | 진전(신규 Open 0) |

**#36 에스컬레이션 — backend 단독 재오픈(33차)**: 32차 대칭 종결(BE-6 #5·BE-7 해소) 직후 backend가 v2 follow-up(V42 + `NotificationPreferenceServiceTest`)을 **미커밋 재오염**(BE-6 #6·BE-7 recurrence #2). frontend는 COD 33·34차 연속 working tree CLEAN(FE-6 패턴 자율 정착 유지). → 결정 53대로 운영 게이트(pre-commit hook `git diff --quiet -- src/test` + V*.sql·CI fail-fast) 권고를 **backend 스트림 한정**으로 유지.

**coder 다음 액션 (33차, 우선순위)**: ① **B02 #6·B08 #2** — `V42__guardian_notification_preferences_consent_temporal.sql` + `NotificationPreferenceServiceTest`(3 @Test) **완료 단위 develop 커밋**(BE-6·BE-7·규율 8) 또는 stash/revert → working tree clean → 자동 Fixed. ② **backend merge** — develop→test `c3b8716` 2커밋 일괄 merge(결정 54). ③ **J01** — API_SPEC §4·DBA `guardian_invitations`(#33·#35 결정 후) → 백엔드 API → 프론트 실 API 연동. ④ **B03** — v1.1 Must 라이ve E2E 완료 → `merge_status: ready` → frontend develop→test merge(17 ahead 동반·FE-16 흡수). ⑤ **v1.2 KPI** — SideNav ≥60%·P0 E2E는 v1.1 merged 후.

---

### [PLN] QA 피드백 반영 (2026-06-07, 32차 — TSR 48·49차 + backend B02 #5·B08 정식 Fixed `c3b8716`·30+회 백엔드 정체 종결·frontend FE-15 Fixed·B07 #4 신호 소멸·#36 대칭 종결·Open 0건)

> **TSR 48차(15:35, backend)** develop HEAD `e8750d2`→**`c3b8716`**(+2커밋 COD 32차 `feac558` B08·`c3b8716` B02 #5), working tree **3M+4U→CLEAN**. **QA-B02 #5·QA-B08 정식 Fixed** — TSR 독립 검증 + planner 직접 재검증(`git cat-file -e HEAD:` `PilotChecklistJwtE2eTest`·V41·`notification/` 9 java PRESENT, 이관 규율 5·6·8 PASS). develop committed `mvn test` **249/249 PASS**. develop **2 ahead of test** — **결정 54** v1 보완 merge 즉시 권고. **TSR 49차(15:45, frontend)** develop HEAD `4be0938`→**`c98f98d`**(+1커밋 COD 33차 FE-15·UXD 인라인 style, **16 ahead**), working tree **CLEAN**. **FE-15 정식 Fixed** — `manualChunks`로 단일 JS 744.95 kB → 최대 **393.53 kB**. **B07 #4 신호 소멸**(48차 교차 5 files → `c98f98d` 일괄 커밋). HEAD `npm test` **186/34**·752 modules·audit **0**. **신규 Open 0**·**#36 대칭 종결(양 스트림 dirty-tree·false Fixed 소멸)**.

| QA id | sev | ver | 32차 관측 | 상태 |
|-------|-----|-----|-----------|------|
| QA-20260606-B07 | BLOCK | v1.1/v1.2 | COD 31차 `4be0938` Fixed 유지·COD 33차 `c98f98d` B07 #4 신호 소멸 | **Fixed** |
| QA-20260606-B02 | BLOCK | v1 | COD 32차 `c3b8716` `PilotChecklistJwtE2eTest` 22 @Test + `.gitignore` HEAD PRESENT·WT CLEAN | **Fixed** |
| QA-20260607-B08 | BLOCK | v2 | COD 32차 `feac558` V41 + 7 java + 8 @Test HEAD PRESENT·WT CLEAN | **Fixed** |
| QA-20260606-B03 | BLOCK | v1.1 | J01·라이ve E2E·v1.1 완료 기준 `[ ]` — **frontend merge 게이트 + backend merge(2커밋) 잔존** | Planned(잔존) |
| FE-15 | LOW | v1.2 | COD 33차 `c98f98d` `manualChunks`·최대 393.53 kB·186/34 | **Fixed** |

**#36 에스컬레이션 — 대칭 종결(32차)**: frontend COD 31차·33차 commit으로 FE-6 #3·FE-15 해소. backend COD 32차 commit으로 BE-6 #5·BE-7 해소. **30+회 양 스트림 정체 종결** — 운영 게이트(pre-commit hook·CI fail-fast) 권고 **예방적 보류**.

**coder 다음 액션 (32차, 우선순위)**: ① **backend merge** — develop→test `c3b8716` 즉시 merge(결정 54, 2커밋 일괄). ② **J01** — API_SPEC §4·DBA `guardian_invitations`(#33·#35 결정 후) → 백엔드 API 구현 → 프론트 실 API 연동. ③ **B03** — v1.1 Must 라이ve E2E 완료 → `merge_status: ready` → frontend develop→test merge(16 ahead 동반). ④ **v1.2 KPI** — SideNav ≥60%·P0 E2E는 v1.1 merged 후.

---

### [PLN] QA 피드백 반영 (2026-06-07, 31차 — TSR 46·47차 + frontend B07 #3 정식 Fixed `4be0938`·30+회 정체 종결·backend B02 #5·B08 dirty-tree 확대·false Fixed 재확인·Open 0건)

> **TSR 47차(14:45, frontend)** develop HEAD `3fdc266`→**`4be0938`**(COD 31차 82 files +4589/-545, **15 ahead**), working tree **76→0 CLEAN**. **QA-B07 recurrence #3 정식 Fixed** — TSR 독립 검증 + planner 직접 재검증(`git -C src/frontend status --porcelain` 0줄·`git cat-file -e HEAD:` FE-12/13/14 전 산출물 PRESENT·SEC-005 localStorage 0건, 이관 규율 5 PASS). HEAD `npm test` **185/33**·build **752 modules**·audit **0**. **비차단 LOW 신규**: 단일 JS 청크 **744.95 kB**(>500 kB vite 경고) → `manualChunks` 코드 스플릿 권고(#38·FE-15·v1.2 후속, merge BLOCK 아님). **TSR 46차(14:30, backend)** develop·test `@e8750d2` 동일, dirty-tree **1M+4U→3M+4U 확대** — B08 WIP가 `MustApiEndpointRoutingTest`(+64)·`RoleBasedControllerAccessTest`(+93) **modified**까지 확장. **COD Fixed(B02 #5·B08) TSR + planner 직접 검증 FAIL**(`PilotChecklistJwtE2eTest`·`V41`·`notification/` HEAD ABSENT, 이관 규율 5). test 213/213·develop WT **249/249 PASS**. **신규 Open 0**·**#36 비대칭 종결(frontend 해소·backend 단독 잔존)**.

| QA id | sev | ver | 31차 관측 | 상태 |
|-------|-----|-----|-----------|------|
| QA-20260606-B07 | BLOCK | v1.1/v1.2 | COD 31차 `4be0938` 82 files 일괄 커밋·WT **76→0 CLEAN**·HEAD 전 산출물 PRESENT(이관 규율 5 PASS)·185/33·752 modules·audit 0 | **Fixed** |
| QA-20260606-B02 | BLOCK | v1 | COD false Fixed 재확인 — `PilotChecklistJwtE2eTest` **HEAD ABSENT·WT untracked only** | Planned(#5, 잔존) |
| QA-20260607-B08 | BLOCK | v2 | COD false Fixed 재확인 — V41 + 7 java + 8 @Test **HEAD ABSENT** + `MustApiEndpointRoutingTest`(+64)·`RoleBasedControllerAccessTest`(+93) **modified 확대** | Planned(잔존) |
| QA-20260606-B03 | BLOCK | v1.1 | J01·라이ve E2E·v1.1 완료 기준 `[ ]` — **frontend merge 게이트 단일** | Planned(잔존) |

**frontend TSR 47차 — B07 #3 정식 Fixed**: COD 31차 `4be0938`가 FE-12(Recharts 차트)·FE-13(플랫폼·배치·청구·copay·NHIS·보호자·`FeeScheduleTable`)·FE-14(운영/보안/계정) WIP **76 files를 develop HEAD에 일괄 반영**. 30+회(11~46차) 누적된 frontend dirty-tree·미커밋 정체가 **종결**됨 — FE-6 #3 해소·FE-7 충족. 잔여 frontend BLOCK은 **B03 merge 게이트 단일**(v1.1 완료 기준 J01 백엔드 API·라이ve E2E·`merge_status: ready`).

**#36 에스컬레이션 — 비대칭 종결(31차)**: frontend는 COD 31차 commit으로 종결 공언 가능(FE-6 #3 해소·dirty-tree 0). backend는 B02 #5·B08 **false Fixed 지속**(TSR 46차 HEAD ABSENT) → 운영 게이트(pre-commit hook·CI fail-fast) 권고는 **backend 스트림 한정**으로 유지(상세 #36).

**coder 다음 액션 (31차, 우선순위)**: ① **B02 #5** — `PilotChecklistJwtE2eTest.java` develop commit(v1 §6·P1–P8 live JWT E2E 완료 신호 동반). ② **B08** — v2 `notification_preferences`(7 java/8 @Test + V41 + modified 2 test) develop commit 또는 stash/revert(BE-7). ③ **`.gitignore`** — `data/backups/` 정합(#37). ④ **B03** — v1.1 J01(#33·#35) 완료 → `merge_status: ready` → develop→test merge(B07 #3 커밋 15 ahead 동반). ⑤ **FE-15(비차단)** — `manualChunks` 코드 스플릿(#38, v1.2 후속).

---

### [PLN] QA 피드백 반영 (2026-06-07, 30차 — TSR 45차 + frontend B07 #3 72→76 files·`FeeScheduleTable`(+test)·WT 181/30·749 modules·backend 44차 baseline 불변·Open 0건)

> TSR 45차(14:02, frontend) develop HEAD **`3fdc266` 불변**(43차 대비), dirty-tree **72→76 files**(40M+36U) — 신규 **`FeeScheduleTable`(+test)** + 기존 FE-12·FE-13·FE-14 WIP. WT **181/30·749 modules·audit 0** TSR 독립 재현(+2/+1 tests vs 43차). backend(44차 baseline) develop·test `@e8750d2`·B02 #5·B08 dirty-tree·COD Fixed FAIL — **변화 없음**. **신규 Open 0**·**30차 연속 coder 미조치**.

| QA id | sev | ver | 30차 관측 | 상태 |
|-------|-----|-----|-----------|------|
| QA-20260606-B02 | BLOCK | v1 | COD false Fixed 철회 유지 — `PilotChecklistJwtE2eTest` **WT untracked only**·`.gitignore` +`data/backups/` 1M 미커밋 | Planned(#5, 잔존) |
| QA-20260607-B08 | BLOCK | v2 | COD false Fixed 철회 유지 — V41 + 7 java + **8 @Test** **WT untracked only** | Planned(잔존) |
| QA-20260606-B07 | BLOCK | v1.1/v1.2 | develop `3fdc266` HEAD Fixed PRESENT; WT **76 files**(43차 72→45차 **+4**, 신규 **`FeeScheduleTable`(+test)**) — FE-13 수가표 테이블 UI(US-G00a·케어포 9-x) | Planned(#3, 범위 확대) |
| QA-20260606-B03 | BLOCK | v1.1 | J01·라이ve E2E·v1.1 완료 기준 `[ ]` — **merge 게이트 단일** | Planned(잔존) |

**frontend TSR 45차 — B07 #3 범위 확대(72→76 files)**: **`FeeScheduleTable`(+test)** — 수가표 목록·등급×연도 테이블 UI(US-G00a·케어포 9-x 수가설정·HEAD `FeeRateHistoryPanel` 이력 모달 연계). BNK-6 §9 기초설정·운영 — 케어포 수가설정 화면 패리티. WT 품질 **PASS**(181/30·749 modules·audit 0) — FE-7 충족·FE-6 #3 재발(미커밋)만 해당.

**#36 에스컬레이션 — 인프라 강제 단계 진입**: **30차 연속 coder 미조치** + frontend dirty-tree **범위 누적 확대**(26→44→60→61→72→**76**) + COD false Fixed 재발(TSR 40·42차) → pre-commit hook·CI fail-fast **인프라 강제 단계 진입** 유지(PLAN_NOTES `### 추가 질문` #36).

**coder 다음 액션 (30차, 우선순위)**: ① **B02 #5** — `PilotChecklistJwtE2eTest.java` develop commit. ② **B08** — v2 `notification_preferences`(7 java/**8 @Test**) develop commit 또는 stash/revert(BE-7). ③ **`.gitignore`** — `data/backups/` 커밋(#37). ④ **B07 #3** — **76 files** develop commit(FE-12·FE-13·FE-14 cluster 분리 권장: (a) Recharts+`HealthAlertList` FE-12, (b) Platform·배치·청구·copay·NHIS·보호자·**`FeeScheduleTable`** FE-13, (c) 운영/보안·계정 FE-14). ⑤ v1.1 J01(#33·#35) → B03 ready → merge.

### [PLN] QA 피드백 반영 (2026-06-07, 29차 — TSR 42·43차 + backend 상태 불변·B08 @Test 5→8·frontend B07 #3 61→72 files·청구·건강·NHIS·보호자 UI WIP·Open 0건)

> TSR 42차(13:25, backend) develop·test HEAD **`@e8750d2` 동일**(40·41차 대비 **상태 불변**), develop WT **DIRTY 불변** — B02 #5·B08·`.gitignore` +`data/backups/` 1M. **COD Fixed(B02 #5·B08) TSR 독립 검증 FAIL** 재확인. WT `mvn test` **243/243 PASS**(+3)·B08 @Test **5→8**·HEAD `@Test` 199·WT **229**. TSR 43차(13:27, frontend) develop HEAD **`3fdc266` 불변**, dirty-tree **61→72 files**(38M+34U) — 신규 **`BillingStatusConfirmModal`(+test)·`CopayRateTable`(+test)·`GuardianDailySummary`(+test)·`HealthAlertList`(+test)·`NhisImportGuidePanel`(+test)** + 기존 FE-12·FE-13·FE-14 WIP. WT **179/29·748 modules·audit 0** TSR 독립 재현. **신규 Open 0**·**29차 연속 coder 미조치**.

| QA id | sev | ver | 29차 관측 | 상태 |
|-------|-----|-----|-----------|------|
| QA-20260606-B02 | BLOCK | v1 | COD false Fixed 철회 유지 — `PilotChecklistJwtE2eTest` **WT untracked only**·`.gitignore` +`data/backups/` 1M 미커밋 | Planned(#5, 잔존) |
| QA-20260607-B08 | BLOCK | v2 | COD false Fixed 철회 유지 — V41 + 7 java + **8 @Test** **WT untracked only**(42차 5→8) | Planned(잔존) |
| QA-20260606-B07 | BLOCK | v1.1/v1.2 | develop `3fdc266` HEAD Fixed PRESENT; WT **72 files**(41차 61→43차 **+11**, 신규 5종+tests) — FE-12 `HealthAlertList`·FE-13 청구·copay·NHIS·보호자 UI | Planned(#3, 범위 확대) |
| QA-20260606-B03 | BLOCK | v1.1 | J01·라이ve E2E·v1.1 완료 기준 `[ ]` — **merge 게이트 단일** | Planned(잔존) |

**backend TSR 42차 — 상태 불변·B08 WIP 소폭 확대**: 40·41차 대비 develop HEAD·dirty-tree **구조 불변**. notification @Test **5→8**·WT `mvn test` **240→243 PASS**. COD Fixed FAIL 재확인 — commit 없음.

**frontend TSR 43차 — B07 #3 범위 확대(61→72 files)**: 신규 WIP 5종은 BNK-6·REQUIREMENTS §3-9·§3-11·US-M02·Epic L·J 매핑 — ① **`BillingStatusConfirmModal`** — 청구 상태 확인(US-G06 reconciliation 연계), ② **`CopayRateTable`** — 본인부담률 테이블(결정 27·Epic G), ③ **`HealthAlertList`** — 건강 알림 위젯(US-M02 3블록), ④ **`NhisImportGuidePanel`** — NHIS import 가이드(결정 37·롱텀2026 Chrome/Edge), ⑤ **`GuardianDailySummary`** — 보호자 일일 요약(Epic J/K). WT 품질 **PASS**(179/29·748 modules·audit 0) — FE-7 충족·FE-6 #3 재발(미커밋)만 해당.

**#36 에스컬레이션 — 인프라 강제 단계 진입 검토**: **29차 연속 coder 미조치** + frontend dirty-tree **범위 누적 확대**(26→44→60→61→72) + COD false Fixed 재발(TSR 40·42차) → pre-commit hook·CI fail-fast **인프라 강제 단계 진입** 검토(PLAN_NOTES `### 추가 질문` #36).

**coder 다음 액션 (29차, 우선순위)**: ① **B02 #5** — `PilotChecklistJwtE2eTest.java` develop commit. ② **B08** — v2 `notification_preferences`(7 java/**8 @Test**) develop commit 또는 stash/revert(BE-7). ③ **`.gitignore`** — `data/backups/` 커밋(#37). ④ **B07 #3** — **72 files** develop commit(FE-12·FE-13·FE-14 cluster 분리 권장: (a) Recharts+`HealthAlertList` FE-12, (b) Platform·배치·청구·copay·NHIS·보호자 FE-13, (c) 운영/보안·계정 FE-14). ⑤ v1.1 J01(#33·#35) → B03 ready → merge.

### [PLN] QA 피드백 반영 (2026-06-07, 27차 — TSR 40·41차 + backend COD false Fixed 철회·`.gitignore` 부분 진전·frontend 41차 상태 불변·Open 0건)

> TSR 40차(12:45, backend) develop·test HEAD **`@e8750d2` 동일**(38차 대비), develop WT **부분 변화** — `.gitignore` **+`data/backups/`** 1M 미커밋·`data/backups/` untracked **소멸**(#37 부분 진전). **COD Fixed 주장(B02 #5·B08) TSR 독립 검증 FAIL** — `PilotChecklistJwtE2eTest`·`notification/`·V41 **HEAD ABSENT**·WT untracked 유지(이관 규율 5). WT `mvn test` **240/240 PASS**(+27). TSR 41차(12:52, frontend) develop HEAD **`3fdc266` 불변**, dirty-tree **60→61 files**(39차 대비 ±1 modified)·WT **169/24·743 modules·audit 0** TSR 독립 재현. **신규 Open 0**·**27차 연속 coder 미조치**.

| QA id | sev | ver | 27차 관측 | 상태 |
|-------|-----|-----|-----------|------|
| QA-20260606-B02 | BLOCK | v1 | COD false Fixed 철회 — `PilotChecklistJwtE2eTest` **WT untracked only**·`.gitignore` +`data/backups/` 1M 미커밋 | Planned(#5, 잔존) |
| QA-20260607-B08 | BLOCK | v2 | COD false Fixed 철회 — V41 + 6 java + 5 @Test **WT untracked only**·HEAD ABSENT | Planned(잔존) |
| QA-20260606-B07 | BLOCK | v1.1/v1.2 | develop `3fdc266` HEAD Fixed PRESENT; WT **61 files**(39차 60→41차 ±1 modified) — FE-12·FE-13·FE-14 WIP 동일 범위 | Planned(#3, 잔존) |
| QA-20260606-B03 | BLOCK | v1.1 | J01·라이ve E2E·v1.1 완료 기준 `[ ]` — **merge 게이트 단일** | Planned(잔존) |

**backend TSR 40차 COD false Fixed 철회**: COD가 B02 #5(`PilotChecklistJwtE2eTest`)·B08(`notification_preferences`) develop 반영을 주장했으나 TSR 40차 `git cat-file -e HEAD:` **ABSENT** — ROADMAP v1 **QA-B02 `[x]`·v2 BE-7 `[x]` 철회**·QA→태스크 매핑 Planned 복원. **부분 진전**: `.gitignore`에 `data/backups/` 추가(1M 미커밋)로 untracked manifest **소멸** — #37(data/backups 추적 정책) 결정 전 `.gitignore` 커밋 필요.

**frontend 41차 상태 불변**: 39차 60 files → **61 files**(±1 modified). WT 품질 **PASS**(169/24·743 modules·audit 0) — FE-7 충족·FE-6 #3 재발(미커밋)만 해당.

**#36 에스컬레이션 — 인프라 강제 단계 진입 검토**: 27차 연속 coder 미조치 + COD false Fixed 재발(TSR 40차) → pre-commit hook·CI fail-fast **인프라 강제 단계 진입** 검토(PLAN_NOTES `### 추가 질문` #36).

**coder 다음 액션 (27차, 우선순위)**: ① **B02 #5** — `PilotChecklistJwtE2eTest.java` develop commit. ② **B08** — v2 `notification_preferences`(6 java/5 @Test) develop commit 또는 stash/revert(BE-7). ③ **`.gitignore`** — `data/backups/` 커밋(#37). ④ **B07 #3** — 61 files develop commit(FE-12·FE-13·FE-14 cluster 분리 권장). ⑤ v1.1 J01(#33·#35) → B03 ready → merge.

### [PLN] QA 피드백 반영 (2026-06-07, 26차 — TSR 38·39차 + 상태 불변 + B07 #3 44→60 files·계정 보안·로그인 이력 UI WIP·FE-14 §3-1 매핑 확장 + B08 dirty-tree 잔존 + COD 03:08 부분 진전·develop 미커밋 + Open 0건)

> TSR 38차(12:05, backend) develop·test HEAD **`@e8750d2` 동일**(0 commits diff)·`mvn test` **213/213 PASS**(75 suites, Spring Boot 3.5.3)·`package` SUCCESS(82,868,029 B)·SEC-007 test **PRESENT**. develop working tree **DIRTY 불변** — ① B02 #5 `PilotChecklistJwtE2eTest`(634 lines/22 @Test, Planned) ② **B08 v2 `notification_preferences` WIP**(V41 + 7 java + 5 @Test, Planned) ③ `data/backups/` manifest. HEAD `@Test` **199**·WT **226**. TSR 39차(12:09, frontend) develop HEAD **`3fdc266` 불변**, working tree **44→60 files**(36M+24U) — 신규 **`LoginHistoryPanel`(+test, §3-1 로그인 이력)·`PasswordChangeModal`(+test, §3-1 비밀번호 재설정·COD 03:08 `SettingsPage` 보안 탭 연결)·`PasswordResetRequestModal`(+test, §3-1)·`PlatformOrgDetailModal`(+test, US-A01 Tenant 상세)·`SettingsPage.test.jsx`·`HealthTrendChart.test.jsx`** + 기존 Recharts·`BatchProgressSteps`·`AuditLogPanel`·`BackupSettingsPanel`·`FilterChips`. WT build **743 modules PASS**(+2)·`npm test` **169/24 PASS**(+8/+4)·audit **0건**(FE-7). → **B07 #3 Planned 범위 확대**(신규 Open 0). **양 스트림 HEAD·dirty-tree 사유 불변 — COD 03:08 부분 진전이나 develop 미커밋 지속**.

| QA id | sev | ver | 26차 관측 | 상태 |
|-------|-----|-----|-----------|------|
| QA-20260606-B07 | BLOCK | v1.1/v1.2 | develop `3fdc266` HEAD Fixed PRESENT; WT **60 files**(35차 26→37차 44→39차 60) — Recharts·Platform·배치·운영/보안 설정 + **계정 보안·로그인 이력**(`LoginHistoryPanel`·`PasswordChangeModal`·`PasswordResetRequestModal`·`PlatformOrgDetailModal`·`SettingsPage.test`·`HealthTrendChart.test`) WIP, FE-6 #3 재발 | Planned(#3, 범위 확대) |
| QA-20260607-B08 | BLOCK | v2 | develop `e8750d2` WT — `notification_preferences` 7 java/5 @Test + `data/backups/` manifest untracked 불변, B02 #5 동반 | Planned(잔존) |
| QA-20260606-B02 | BLOCK | v1 | B02 #5 `PilotChecklistJwtE2eTest` untracked 유지 — HEAD `@Test` 199·WT 226 | Planned(#5, 잔존) |
| QA-20260606-B03 | BLOCK | v1.1 | J01·라이ve E2E·v1.1 완료 기준 `[ ]` — **merge 게이트 단일** | Planned(잔존) |

**frontend 39차 B07 #3 범위 확대 → FE-14 §3-1 매핑 확장**: 37차 44 files → **60 files**(+16). 신규 WIP는 ① **계정 보안 UI**(`PasswordChangeModal`(+test)·`PasswordResetRequestModal`(+test)) — REQUIREMENTS §3-1 「비밀번호 재설정 (이메일 발송)」 매핑, ② **로그인 이력 UI**(`LoginHistoryPanel`(+test)) — §3-1 「로그인 이력 조회」 매핑, ③ **Tenant 상세 UI**(`PlatformOrgDetailModal`(+test)) — US-A01 Tenant 관리·**FE-13 범위 확장**, ④ 테스트 회귀 강화(`SettingsPage.test`·`HealthTrendChart.test`·FE-12 회귀). FE-14는 운영/보안 설정 + **계정 보안·로그인 이력** §3-1 인증 모듈 매핑까지 확장. WT 품질 PASS(169/24·743 modules·audit 0) — FE-7 충족·프로세스 위반(미커밋)만 해당.

**COD 03:08 frontend 부분 진전 — develop 미커밋**: `SettingsPage` 보안 탭에 `PasswordChangeModal`·`PasswordResetRequestModal` 연결 + `SettingsPage.test.jsx` 추가. 로컬 검증 169/24·743 modules PASS — **develop working tree 미커밋**(이관 규율 5·6 위반 지속·B07 #3 Planned 유지). 「테스트 PASS ≠ 이관 PASS」 — coder가 「작업 단위 commit」 패턴에 정착 실패. backend 26차도 동일(B02 #5·B08 미커밋 불변).

**backend 38차 B08·`data/backups/` 관측 불변**: TSR 36차 대비 변화 없음 — `notification_preferences` 7 java/5 @Test·`data/backups/` manifest 모두 working tree에 유지. JAR size 82,868,029 B로 SEC-007 test PRESENT 재확인. coder commit·stash·revert·`.gitignore` 정합 중 어느 것도 미실행. #37(data/backups 추적 정책)·BE-7(v2 dirty-tree) 결정 대기.

**coder 다음 액션 (26차, 우선순위, 25차 대비 불변)**: ① **B02 #5** — `PilotChecklistJwtE2eTest.java` develop commit. ② **B08** — v2 `notification_preferences`(7 java/5 @Test) develop commit 또는 stash/revert(BE-7), `data/backups/` 정리(#37). ③ **B07 #3** — 60 files develop commit(FE-6·FE-7·FE-12·FE-13·**FE-14**). 단위 분리 권장: (a) Recharts FE-12 cluster, (b) Platform·배치 FE-13 cluster, (c) 운영/보안·계정 보안·로그인 이력 FE-14 cluster. ④ v1.1 J01(#33·#35) → B03 ready → merge. **26차 연속 미조치 — #36 운영 게이트(pre-commit hook·CI fail-fast) 권고 강화 유지·인프라 강제 단계 진입 검토**.

### [PLN] QA 피드백 반영 (2026-06-07, 25차 — TSR 36·37차 + 상태 불변 + B07 #3 26→44 files·FE-14 신설 + B08 dirty-tree 잔존 + Open 0건)

> TSR 36차(11:25, backend) develop·test HEAD **`@e8750d2` 동일**(0 commits diff)·`mvn test` **213/213 PASS**(75 suites)·SEC-007 test **PRESENT**. develop working tree **DIRTY 불변** — ① B02 #5 `PilotChecklistJwtE2eTest`(22 @Test, Planned) ② **B08 v2 `notification_preferences` WIP 소폭 확대**(V41 + **7 java + 5 @Test**, Planned) ③ `data/backups/` manifest(로컬 산출물, 신규 untracked 관측). HEAD `@Test` **199**·WT **226**. TSR 37차(11:30, frontend) develop HEAD **`3fdc266` 불변**, working tree **26→44 files**(26M+18U) — 신규 운영/보안 설정 UI `AuditLogPanel`(+test)·`BackupSettingsPanel`(+test)·`PasswordChangeModal`(+test)·`FilterChips.test` + 기존 Recharts·`BatchProgressSteps`·`PlatformOrgDetailModal`·Platform/NHIS/Reconciliation/Forbidden. WT build **741 modules PASS**·`npm test` **161/20 PASS**(+17/+7)·audit **0건**(FE-7). → **B07 #3 Planned 범위 확대**(신규 Open 0). **양 스트림 HEAD·dirty-tree 사유 불변 — coder 미조치 지속**.

| QA id | sev | ver | 25차 관측 | 상태 |
|-------|-----|-----|-----------|------|
| QA-20260606-B07 | BLOCK | v1.1/v1.2 | develop `3fdc266` HEAD Fixed PRESENT; WT **44 files**(35차 26→37차 44) — Recharts·Platform·배치 + 운영/보안 설정 UI WIP, FE-6 #3 재발 | Planned(#3, 범위 확대) |
| QA-20260607-B08 | BLOCK | v2 | develop `e8750d2` WT — `notification_preferences` 6→**7 java**·4→**5 @Test** + `data/backups/` manifest untracked, B02 #5 동반 | Planned(잔존, 소폭 확대) |
| QA-20260606-B02 | BLOCK | v1 | B02 #5 `PilotChecklistJwtE2eTest` untracked 유지 — HEAD `@Test` 199·WT 226 | Planned(#5, 잔존) |
| QA-20260606-B03 | BLOCK | v1.1 | J01·라이ve E2E·v1.1 완료 기준 `[ ]` — **merge 게이트 단일** | Planned(잔존) |

**frontend 37차 B07 #3 범위 확대 → FE-14 신설**: 35차 26 files → **44 files**. 신규 컴포넌트가 차트·플랫폼(FE-12·FE-13) 범위를 벗어난 **운영·보안 설정 UI**(감사 로그·백업 정책·비밀번호 변경·필터 칩)이므로 **FE-14**로 분리 태스크화(USER_STORIES §16). BNK-6 케어포 대비 운영/보안 모듈 커버리지 확대 기여. WT 품질 PASS(161/20·741 modules) — FE-7 충족·프로세스 위반(미커밋)만 해당.

**backend 36차 B08·`data/backups/` 관측**: `notification_preferences` WIP가 6→7 java·4→5 @Test로 소폭 확대(이관 규율 8 미해소). 신규로 `data/backups/` manifest가 untracked로 관측 — 로컬 산출물/백업 디렉터리 추정, `.gitignore` 정합 또는 commit 분리 필요(아래 추가 질문 #37).

**coder 다음 액션 (25차, 우선순위, 24차 대비 불변)**: ① **B02 #5** — `PilotChecklistJwtE2eTest.java` develop commit. ② **B08** — v2 `notification_preferences`(7 java+5 @Test) develop commit 또는 stash/revert(BE-7), `data/backups/` 정리. ③ **B07 #3** — 44 files develop commit(FE-6·FE-7·FE-12·FE-13·**FE-14**). ④ v1.1 J01(#33·#35) → B03 ready → merge. **25차 연속 미조치 — #36 운영 게이트(pre-commit hook) 권고 강화**.

### [PLN] QA 피드백 반영 (2026-06-07, 24차 — TSR 34·35차 + B08 Open→Planned + B07 #3 26 files + v1 merged·SEC-007 test 해소)

> TSR 34차(01:45, backend) develop·test HEAD **`@e8750d2` merged**·Maven **213/213 PASS**·SEC-007 test `ProductionSecretValidator` **PRESENT**. develop working tree **DIRTY 8 files** — ① B02 #5 `PilotChecklistJwtE2eTest`(Planned) ② **v2 `notification_preferences` WIP**(V41 + 6 java + 4 @Test) → **QA-B08 Open→Planned**. TSR 35차(01:50, frontend) develop HEAD **`3fdc266` 불변**, working tree **18→26 files** — `BatchProgressSteps`(+test)·`PlatformOrgDetailModal`·Platform/NHIS/Reconciliation/Forbidden WIP. WT build **738 modules PASS**·`npm test` **144/13 PASS**·audit **0건**(FE-7). → **B07 #3 Planned 범위 확대**(신규 Open 0).

| QA id | sev | ver | 24차 관측 | 상태 |
|-------|-----|-----|-----------|------|
| QA-20260607-B08 | BLOCK | v2 | develop `e8750d2` v1 merged 이후 WT 8 files — `NotificationPreferenceService`·`GuardianNotificationPreferenceController`·V41 + 4 @Test, B02 #5 동반 | Open→**Planned** |
| QA-20260606-B02 | BLOCK | v1 | B02 #5 `PilotChecklistJwtE2eTest` untracked 유지 — HEAD `@Test` 199·WT 225 | Planned(#5, 잔존) |
| QA-20260606-B07 | BLOCK | v1.1/v1.2 | develop `3fdc266` HEAD Fixed PRESENT; WT **26 files** Recharts·Platform·배치 WIP — FE-6 #3 재발 | Planned(#3, 범위 확대) |
| QA-20260606-B03 | BLOCK | v1.1 | J01·라이ve E2E·v1.1 완료 기준 `[ ]` — **merge 게이트 단일** | Planned(잔존) |

**backend 34차 B08 v2 선행 WIP**: v1 merged 직후 `guardian_notification_preferences`(V41)·`NotificationPreferenceService`·`GuardianNotificationPreferenceController`·`GuardianNotificationPreferenceControllerTest`(4 @Test) 미커밋. v2 알림 채널 선행 골격 — API_SPEC §11·BE-7. B02 #5와 동반 dirty-tree(합계 8 files) → commit 시 B08·B02 #5 분리 또는 일괄 commit 후 clean.

**frontend 35차 B07 #3 범위 확대**: 33차 Recharts 18 files → **26 files** — `BatchProgressSteps`·`PlatformOrgDetailModal`·Platform/NHIS/Reconciliation/Forbidden. BNK-6 HQ/플랫폼·NHIS 배치 UX(FE-13). WT 품질 PASS(144/13·738 modules) — FE-7 충족·프로세스 위반만 해당.

**coder 다음 액션 (24차, 우선순위)**: ① **B02 #5** — `PilotChecklistJwtE2eTest.java` develop commit. ② **B08** — v2 `notification_preferences` develop commit 또는 stash/revert(BE-7). ③ **B07 #3** — 26 files develop commit(FE-6·FE-7·FE-12·FE-13). ④ v1.1 J01(#33·#35) → B03 ready → merge.

### [PLN] QA 피드백 반영 (2026-06-07, 23차 — TSR 32·33차 + B02 #5·B07 #3 recurrence + v1 merged + Recharts WIP + planner 22차 false `[x]` 철회)

> TSR 32차(01:30, backend) develop HEAD **`e8750d2` 불변**, working tree **DIRTY** — 1 untracked `PilotChecklistJwtE2eTest.java`(634 lines, **22 @Test**, P1–P8 live Bearer JWT filter-chain E2E WIP). planner 22차·COD가 ROADMAP v1 §6·P1–P8 `[x]`·`merge_status: ready`에 본 파일을 인용했으나 **develop HEAD ABSENT**(이관 규율 5·6 위반) → **QA-B02 recurrence #5 Open→Planned**. backend test `@e8750d2` merge **완료**(33차 교차). TSR 33차(01:16, frontend) develop HEAD **`3fdc266` 불변**, working tree **DIRTY** — 13M+5U=**18 files** Recharts 차트 WIP(`recharts ^2.15.4`·`ChartContainer`·`AttendanceRateChart`·`BranchCompareChart`·`HealthTrendChart`·`ChartContainer.test.jsx` + Dashboard·HealthDetail·AttendanceStats). WT build **736 modules PASS**·`npm test` **142/12 PASS**·audit **0건**(FE-7). → **QA-B07 recurrence #3 Open→Planned**. v1 **`merged`**·B05 Fixed.

| QA id | sev | ver | 23차 관측 | 상태 |
|-------|-----|-----|-----------|------|
| QA-20260606-B02 | BLOCK | v1 | develop `e8750d2` HEAD Fixed PRESENT·`SevenRoleJwtLoginE2eTest` PRESENT; WT 1 untracked `PilotChecklistJwtE2eTest` 634 lines/22 @Test — planner 22차 false `[x]` | Open→**Planned**(#5) |
| QA-20260606-B07 | BLOCK | v1.1/v1.2 | develop `3fdc266` HEAD Fixed PRESENT; WT 18 files Recharts WIP — FE-6 #3 재발·21차 「8커밋 무재발」 **철회** | Open→**Planned**(#3) |
| QA-20260606-B03 | BLOCK | v1.1 | J01 백엔드 API·라이ve E2E·v1.1 완료 기준 `[ ]` 잔여 — **merge 게이트 단일** | Planned(잔존) |
| QA-20260606-B05 | BLOCK | v1.1 | v1 **`merged`** — **Fixed** | Fixed |
| QA-20260606-B01 | BLOCK | v1 | v1 **`merged`** — B01·SEC-007 **Fixed**(22차 COD ready, 33차 test merge 완료) | Fixed |

**backend 32차 BE-6 #5 재발**: 30차 #4 Fixed(`e8750d2` CLEAN) 직후 `PilotChecklistJwtE2eTest.java`(634 lines, 22 @Test) 미커밋. v1 REQUIREMENTS §6·P1–P8 live JWT E2E를 충족할 자산이나 develop HEAD 미반영. planner 22차 false `[x]` 확인 — **ROADMAP `[x]`는 develop HEAD 산출물 존재 시에만 유효**(규율 5). coder: `mvn -q test` PASS(WT `@Test` 221) 후 develop commit → B02 #5 Fixed + v1 §6·P1–P8 `[x]` 복원 가능.

**frontend 33차 FE-6 #3 재발**: 31차 CLEAN(`3fdc266`) 직후 Recharts 차트 레이어 18 files WIP. BNK-6 대시보드 3블록·HQ 지점 비교(BNK-6-4) + UXD 14차 `chartColors.js` 토큰 연계 → **v1.2 P0 Recharts**(US-M02·**FE-12**). WT 품질 PASS(142/12·736 modules) — FE-7 충족·프로세스 위반만 해당.

**#36 에스컬레이션 강화**: 21차 「BE-6·FE-6 8커밋 무재발 종결」 **철회** — 32·33차 양 스트림 동시 recurrence. planner 22차 `PilotChecklistJwtE2eTest` false `[x]` 추가 확인. **운영 게이트(pre-commit hook·`git diff --quiet` CI check) 권고 재강화**.

**coder 다음 액션 (23차, 우선순위)**: ① **B02 #5** — `PilotChecklistJwtE2eTest.java` develop commit(BE-6, Maven PASS) → v1 §6·P1–P8 `[x]` 복원. ② **B07 #3** — Recharts 18 files develop commit(FE-6·FE-7) → v1.1 QA-B04·B07 `[x]` 복원. ③ v1.1 J01(#33·#35) → B03 ready → merge(흡수 8묶음). ④ v1.2 Recharts·≥60% KPI는 v1.1 merged 후 정식 평가.

### [PLN] QA 피드백 반영 (2026-06-07, 21차 — TSR 30·31차 + B02 #4 Fixed + COD 22차 P1–P8 페이지 E2E + UXD 14차 FeeRateHistoryPanel + Open 0건 유지)

> TSR 30차(00:28, backend) develop HEAD `c3f3146`→**`e8750d2`**(+1커밋 COD 21차 — `SevenRoleJwtLoginE2eTest.java` 384 lines 7역할 JWT live filter-chain E2E), working tree **CLEAN**, `@Test` 183→**199**(+16), Maven 79/79 PASS. **QA-B02 recurrence #4 정식 Fixed** — v1 R-04 「7역할 라이브 JWT 로그인 E2E」**[x] 충족**. Planned BLOCK **5건→4건**. TSR 31차(00:43, frontend) develop HEAD `57ff3c0`→`a42d6fb`→**`3fdc266`**(+2커밋 — UXD 14차 `a42d6fb`: `FeeRateHistoryPanel`·`chartColors.js`·`BATCH_STATUS` 8 files; COD 22차 `3fdc266`: `pilotPageFlows.test.jsx` 433 lines P1–P8 페이지 RTL E2E), **14커밋 ahead**, working tree **CLEAN**. HEAD `npm run build` **113 modules PASS**·`npm test` **130/10→140/11 PASS**(+10/+1)·`npm audit` **0건**. **Open 0건** — Planned BLOCK **4건**(B01·B03·B05·SEC-007 merge 게이트 단일) 불변.

| QA id | sev | ver | 21차 관측 | 상태 |
|-------|-----|-----|-----------|------|
| QA-20260606-B02 | BLOCK | v1 | develop `e8750d2` CLEAN·`SevenRoleJwtLoginE2eTest` PRESENT·`@Test` 199·Maven 79/79 PASS — recurrence #4 **Fixed**(30차 TSR 독립 검증) | Fixed(유지·강화) |
| QA-20260606-B01 | BLOCK | v1 | `merge_status: pending` — v1 잔여 REQUIREMENTS §6 체크리스트·P1–P8 라이ve E2E(post-merge) + ready 미설정 | Planned(잔존) |
| QA-20260606-B03 | BLOCK | v1.1 | **흡수 8묶음**(결정 52, 14커밋/~98 files); R-05 P1–P8 페이지 E2E PARTIAL 강화(`3fdc266` 140/11 PASS); J01 백엔드 API·라이ve E2E 잔여 | Planned(잔존) |
| QA-20260606-B05 | BLOCK | v1.1 | 선행 v1 `merge_status: merged` 미충족 | Planned(잔존) |
| SEC-007 | BLOCK | v1 | test(`2799e29`) P0 미패치 — B01 merge 동반 해소 | Planned(잔존) |

**backend 30차 B02 #4 Fixed**: COD 21차 `e8750d2` `test(v1): 7역할 JWT 로그인·RBAC live filter-chain E2E (SevenRoleJwtLoginE2eTest)` — 384 lines develop HEAD 커밋. `@Test` 183→**199**(+16). working tree CLEAN. v1 완료 기준 「7역할 라이브 JWT 로그인 E2E」**[x] 충족**. BE-6 #4 Fixed 후 **8커밋 무재발**(`4274459`→`aa71412`→`c3f3146`→`e8750d2`).

**frontend 31차 R-05 P1–P8 페이지 단위 E2E PARTIAL 강화**: COD 22차 `3fdc266` `pilotPageFlows.test.jsx`(433 lines — AttendancePage·DashboardPage·HealthPage·BillingPage·NHISImportPage·ReconciliationPage·ClientDetailPage·GuardianPage RTL fetch-mock JWT API 호출·페이지 렌더 통합 검증). `npm test` 130/10→**140/11 PASS**(+10/+1), build 113 modules PASS, audit 0건. FE-6 **8커밋 무재발**(`a84473f`→`3fdc266`).

**UXD 14차 `a42d6fb` — US-G00a PARTIAL**: `FeeRateHistoryPanel.jsx`·`FeeSchedulePage` 이력 모달·`chartColors.js` Recharts 토큰·`BATCH_STATUS` 공유 상수 8 files. 수가 변경 **이력 조회 UI** 진전(백엔드 이력 API live 연동은 merge 후). v1.1 merge 동반 흡수(결정 52).

**결정 52 흡수 8묶음(21차 갱신)**: ①~⑦ 20차 7묶음 + ⑧ **UXD 14차 `a42d6fb`(8 files) + COD 22차 `3fdc266`(pilotPageFlows 1 file +433)** — 총 **14커밋 / ~98 files** v1.1 develop→test merge 동반.

**#36 에스컬레이션 — BE-6 #4 Fixed·운영 게이트 권고 잔존**: 20차 #4 재발 후 30차 commit으로 Fixed. FE-6 8커밋 무재발 유지. 운영 게이트(pre-commit hook 등) 권고는 **예방적**으로 잔존.

**J01 백엔드 API 미구현 — PLN 명세 결정 대기 유지**: API_SPEC §4 + DBA `guardian_invitations` — **#33 채널 1종·#35 만료/재발송 정책 결정 후 작성** — 보류 유지.

**coder 다음 액션 (21차, 우선순위)**: ① v1 **REQUIREMENTS §6 coder 자체 점검** + P1–P8 **라이ve E2E**(develop→test merge 후) → `merge_status: ready` → B01·SEC-007 동반 해소. ② v1.1 J01 백엔드 API: PLN 명세(#33·#35 결정 후) → DBA V41 → COD 백엔드 → COD 프론트 실 API → B03 ready → merge(흡수 8묶음·결정 52, B05 동반 해소). ③ v1.2 본격 사이클(2단 SideNav ≥60%·E2E)은 v1.1 merged 후.

### [PLN] QA 피드백 반영 (2026-06-06, 20차 — TSR 28·29차 + B02 recurrence #4 Open→Planned + UXD 13차 Switch·셀프 체크인 토글 흡수 + COD 20차 7역할 JWT 로그인·라우트 가드 Vitest 단위 E2E 자동화 정식 충족 + US-UX-03 신설 + BE-6 패턴 #4 재발·종결 공언 철회)

> TSR 28차(23:19 양 스트림 — backend develop HEAD `c3f3146` 불변·working tree **DIRTY** 1 untracked `src/test/java/com/ogada/backend/security/SevenRoleJwtLoginE2eTest.java` 384 lines 7역할 JWT 로그인 E2E 통합 테스트 WIP, 이관 규율 6 위반 → QA-B02 recurrence #4 Open·BE-6 #4 재발; frontend UXD 13차 `07fd305` 전사 설정 Switch·셀프 체크인 토글 7 files +218/-7, working tree CLEAN, `npm test` 32/7→37/8·build 112 modules·audit 0건)·29차(23:31 frontend COD 20차 `57ff3c0` — `sevenRoleJwtLogin.test.jsx`(132)·`sevenRoleRouteGuard.test.jsx`(83)·`sevenRoleRouteMatrix.js`(75)·`roleHomePaths.test.jsx`(+26) 4 files +316: 7역할 JWT 로그인·라우트 가드 Vitest 단위 E2E 자동화, working tree CLEAN, `npm test` 37/8→**130/10 PASS**(+93 tests/+2 files)·build 112 modules·audit 0건, FE-7 회귀 없음). **B02 recurrence #4 Open→Planned**·19차 BE-6 5커밋 무재발 종결 공언 **철회**·UXD 13차+COD 20차 흡수 → 결정 52 흡수 7묶음 갱신.

| QA id | sev | ver | 20차 관측 | 상태 |
|-------|-----|-----|----------|------|
| QA-20260606-B02 | BLOCK | v1 | HEAD @ `c3f3146` Fixed 산출물 규율 5 PRESENT 유효; 28차 working tree **1 untracked** `SevenRoleJwtLoginE2eTest.java` 384 lines 미커밋(7역할 JWT 로그인 E2E 통합 — Spring Security filter chain·JwtAuthFilter·UserDetailsService 라이브 발급/검증) — 이관 규율 6 위반·BE-6 #4 재발 | Fixed→**Planned**(recurrence #4) |
| QA-20260606-B01 | BLOCK | v1 | `merge_status: pending` — 라이브 7역할 JWT 로그인 E2E·SEC-007 잔여 (`SevenRoleJwtLoginE2eTest` commit 후 충족) | Planned(잔존) |
| QA-20260606-B03 | BLOCK | v1.1 | 라이브 backend 통합 E2E·J01 백엔드 API 잔여; **흡수 7묶음**(+UXD 13차 + COD 20차 = 12커밋/~89 files, 결정 52); 7역할 JWT 로그인·라우트 가드 단위 E2E 자동화 **PARTIAL 충족**(57ff3c0 매트릭스 130/10 PASS) | Planned(잔존) |
| QA-20260606-B05 | BLOCK | v1.1 | 선행 v1 merged 미충족 | Planned(잔존) |
| SEC-20260606-007 | BLOCK | v1 | test P0 미패치 — B01 동반 | Planned(잔존) |

**backend 28차 BE-6 패턴 #4 재발**: COD 18차 `c3f3146` 후 develop HEAD 불변(20차 PLN 관측 시점), working tree에 `src/test/java/com/ogada/backend/security/SevenRoleJwtLoginE2eTest.java`(384 lines) 미커밋. 신규 테스트는 **Spring Security filter chain·JwtAuthFilter·UserDetailsService를 통합한 라이브 7역할 JWT 로그인 E2E 시나리오** — v1 완료 기준 「7역할 라이브 JWT 로그인 E2E」를 직접 충족할 수 있는 자산이지만 develop HEAD 미반영. 19차 「BE-6 5커밋 무재발 종결 공언」(BE-6 #3 Fixed 후 22차→24차→26차 5커밋 무재발)을 20차에 **철회** — backend는 「테스트 추가 → 즉시 develop 커밋」 패턴 정착에 실패함. coder가 `mvn -q test` PASS(현재 develop HEAD 기준 Maven 79/79 PASS 재현) 후 develop commit 시 B02 #4 자동 Fixed + v1 R-04 라이브 7역할 JWT 로그인 E2E 완료 기준 동시 충족 → B01 ready 후보.

**frontend 29차 R-04 7역할 JWT 로그인·라우트 가드 단위 E2E 자동화 정식 충족**: COD 20차 `57ff3c0` `test(v1.1): 7역할 JWT 로그인·라우트 가드 E2E 자동화` — 4 files +316.
- `src/auth/sevenRoleJwtLogin.test.jsx`(132 lines) — AuthProvider login() 7역할 JWT 메모리 세션·홈 경로 매트릭스 자동 검증: `platform_admin→/platform`·`hq_admin→/dashboard/hq`·`branch_admin·social_worker·caregiver→/dashboard`·`guardian·client_user→/guardian`·`sysadmin→/settings` + LoginPage 폼 submit 7역할 자동화.
- `src/auth/sevenRoleRouteGuard.test.jsx`(83 lines) — ProtectedRoute 7역할 허용·거부 매트릭스 단위 E2E.
- `src/auth/sevenRoleRouteMatrix.js`(75 lines) — 7역할 라우트 접근 매트릭스 모듈(테스트·런타임 공유).
- `roleHomePaths.test.jsx`(+26 lines) — 홈 경로 회귀.
HEAD `npm test` 37/8→**130/10 PASS**(+93 tests/+2 files, vitest 4.1.8), build 112 modules PASS, audit 0건. **v1.1 R-04 frontend 7역할 화면·메뉴·권한 분리 단위 E2E 자동화 정식 충족** — 라이브 backend 통합 E2E는 `SevenRoleJwtLoginE2eTest.java` commit + B01 merged 후. FE-6 패턴 무재발 6커밋(`a84473f`→`ed1bf22`→`404a30e`→`cc34f23`→`07fd305`→`57ff3c0`).

**frontend 28차 UXD 13차 `07fd305` 흡수 (결정 52)**: `feat(ux): 전사 설정 Switch 컴포넌트·셀프 체크인 토글` — 7 files +218/-7. `Switch.jsx` WAI-ARIA `role=switch`·`aria-checked`·44px hit target·`forced-colors` 미디어 쿼리 적용·`SettingsPage.jsx` `allow_client_self_checkin` 토글 컨트롤(결정 16 안 3 `client_user` 조건부 활성화의 UI 정착)·`Switch.test.jsx` 5건 회귀. DESIGN_SYSTEM §1 컴포넌트·§9 접근성 확장. **US-UX-03 신설**(전사 설정 Switch·셀프 체크인 토글 컨트롤). 결정 52에 따라 v1.1 develop→test merge 동반 흡수.

**결정 52 흡수 7묶음(20차 갱신)**: ① v1.2 P0 `a72e249`(42 files), ② v1.1 US-D03 `3fc549a`(2 files), ③ UXD 10차 `5656e19`(7 files), ④ UXD 11차 `2d742b3`(7 files), ⑤ COD 17차 `a84473f`(8 files) + `ed1bf22`(2 files), ⑥ UXD 12차 `404a30e`(3 files) + COD 18차 `c3f3146`(1 file) + COD 19차 `cc34f23`(3 files), ⑦ **UXD 13차 `07fd305`(7 files, 전사 설정 Switch·셀프 체크인 토글) + COD 20차 `57ff3c0`(4 files, 7역할 JWT 로그인·라우트 가드 Vitest 단위 E2E +316)**. 총 **12커밋 / ~89 files** 모두 v1.1 develop→test merge 시 동반 승격.

**J01 백엔드 API 미구현 — PLN 명세 결정 대기 유지**: TSR 27차 `GuardianInviteModal.test.jsx` 회귀 4건은 프론트 스텁. 19차에 식별된 API_SPEC §4 추가 명세(`POST /clients/{clientId}/guardians/invitations`·`POST /guardian/invitations/{token}/accept`·`GET /guardian/invitations`) + DBA `guardian_invitations` 테이블은 **#33 채널 1종·#35 만료/재발송 정책 결정 후 작성** — 보류 유지(rules.md §1 자율 실행, 추측 명세 금지). 20차 신규 결정 없음.

**#36 에스컬레이션 — BE-6 패턴 #4 재발·종결 공언 철회**: 19차에 「BE-6 5커밋 무재발 완전 종결」(BE-6 #3 Fixed 후 22차→24차→26차 5커밋 working tree CLEAN 유지) 공언했으나 **20차 TSR 28차에서 BE-6 #4 재발**(신규 7역할 JWT E2E 384 lines 미커밋). 19차 5커밋 무재발 → 20차 1커밋 dirty(c3f3146 working tree). FE-6는 무재발 6커밋 유지(`a84473f`→`ed1bf22`→`404a30e`→`cc34f23`→`07fd305`→`57ff3c0`). → backend는 「테스트 작성 → 즉시 commit」 정착에 실패함. **운영 게이트(pre-commit hook 등) 권고 재검토 필요** — backend Maven CI에 `git diff --quiet -- src/test` 등 pre-push check 또는 coder 워크플로우의 "테스트 생성 시 자동 commit" 안내.

**coder 다음 액션 (20차, 우선순위)**: ① **B02 recurrence #4 commit (BE-6)** — `SevenRoleJwtLoginE2eTest.java` `mvn -q test` PASS 확인 후 develop commit → B02 #4 자동 Fixed + v1 R-04 「7역할 라이브 JWT 로그인 E2E」 완료 기준 동시 충족 → v1 잔여 `[ ]`(P1–P8 라이브 E2E·SEC-007 test 승격) 진행 → `merge_status: ready` → B01·SEC-007 동반 해소. ② v1.1 J01 백엔드 API: PLN 명세(#33·#35 결정 후) → DBA `guardian_invitations` V41 → COD 백엔드 구현 → COD 프론트 실 API 연동 → B03 ready → merge(흡수 7묶음 자동 동반·결정 52, B05 동반 해소). ③ v1.2 본격 사이클(2단 SideNav 모듈 가중 커버리지 ≥60%·E2E·등급이력 UI)은 v1.1 merged 후.

### [PLN] QA 피드백 반영 (2026-06-06, 19차 — TSR 26·27차 + PilotChecklistApiAccessTest 29 @Test + pilotChecklist fetch-mock 자동화 + UXD 12차 LoginPage DS·Modal 접근성 흡수 + Open 0건 유지)

> TSR 26차(22:20 양 스트림 — backend COD 18차 `c3f3146` `PilotChecklistApiAccessTest.java` 697 lines **29 @Test**(P1–P8 × 7역할 `@PreAuthorize` `@WebMvcTest`), develop CLEAN·`@Test` 154→**183**, Maven 79/79 PASS; frontend UXD 12차 `404a30e` LoginPage DS·Modal 포커스 트랩·`forced-colors`·`prefers-contrast` WCAG 1.4.11 — 3 files +183/-28, working tree CLEAN·`npm test` 13/5·build 111·audit 0건)·27차(22:40 frontend COD 19차 `cc34f23` `pilotChecklist.js/.test.js`·`GuardianInviteModal.test.jsx` 3 files +396 — P1–P8 services.js 매핑·Vitest fetch-mock JWT·HTTP·경로 자동화·GuardianInviteModal 4건 회귀, working tree CLEAN·`npm test` 13/5→**32/7**(+19 tests/+2 files)·build 111·audit 0건). **양 스트림 working tree CLEAN 유지·신규 Open 0건** — 잔여 BLOCK = merge 게이트(B01·B03·B05·SEC-007) 단일 불변.

| QA id | sev | ver | 19차 관측 | 상태 |
|-------|-----|-----|----------|------|
| QA-20260606-B02 | BLOCK | v1 | develop `c3f3146` CLEAN·`@Test` 183·Maven 79/79 PASS·BE-6 #3 Fixed 후 **5커밋 무재발** | Fixed(유지·강화) |
| QA-20260606-B07 | BLOCK | v1.1/v1.2 | develop `cc34f23` CLEAN·`npm test` 32/7·build 111·audit 0건·FE-6 #2 Fixed 후 **4커밋 무재발** | Fixed(유지·강화) |
| QA-20260606-B01 | BLOCK | v1 | `merge_status: pending` — v1 완료 기준 7역할 라이브 JWT E2E·SEC-007 잔여 (R-04 `@WebMvcTest` 65건 PARTIAL 진전·P1–P8 단위 PARTIAL) | Planned(잔존) |
| QA-20260606-B03 | BLOCK | v1.1 | 라이브 7역할 JWT E2E·J01 백엔드 API·Must 라이브 E2E 잔여(단위 fetch-mock P1–P8·J01/J02 회귀 PARTIAL); **흡수 6묶음**(결정 52) | Planned(잔존) |
| QA-20260606-B05 | BLOCK | v1.1 | 선행 v1 merged 미충족 | Planned(잔존) |
| SEC-20260606-007 | BLOCK | v1 | test P0 미패치 — B01 동반 | Planned(잔존) |

**backend 26차 R-04 7역할 권한 분리 PARTIAL 진전**: COD 18차 `c3f3146` `test(v1): pilot checklist P1–P8 × 7역할 @PreAuthorize @WebMvcTest` — `PilotChecklistApiAccessTest.java` 697 lines 신규(29 @Test). USER_STORIES §13 P1(이용자 등록)·P2(수기 체크인)·P3(건강·투약)·P4(지점 전환)·P5(대시보드)·P6(월말 청구)·P7(엑셀 import)·P8(reconciliation 매칭) 8개 시나리오 × 7역할(`platform_admin`·`hq_admin`·`branch_admin`·`social_worker`·`caregiver`·`guardian`·`client_user`) 조합 중 핵심 29건을 `@WebMvcTest` + `@WithMockUser`로 `@PreAuthorize` 라우팅·인가 자동 검증. develop `@Test` 120→154→**183**(+29). Maven 79/79 PASS·package SUCCESS 재현. **`@WebMvcTest` 65건**(36 RBAC + 29 Pilot) — R-04 단위 자동화 정식 충족, **라이브 7역할 JWT 로그인 E2E**만 잔여. BE-6 #3 Fixed 후 **5커밋 무재발**(94f0fb9→4274459→aa71412→c3f3146) — 패턴 완전 종결.

**frontend 27차 v1.1 Must API JWT 라우팅 fetch-mock 자동화**: COD 19차 `cc34f23` `test(v1.1): pilot P1–P8 fetch-mock·GuardianInviteModal 회귀` — 3 files +396. ① `src/api/pilotChecklist.js`(211 lines) — USER_STORIES §13 P1–P8 시나리오를 `services.js` 경로 + HTTP 메서드 + 필수 페이로드 + 권한(JWT 역할)로 매핑한 **계약 사전(contract dictionary)**. ② `pilotChecklist.test.js`(104 lines) — Vitest fetch-mock으로 각 P 시나리오에 대해 `Authorization: Bearer <JWT>` 헤더·메서드·경로·페이로드 자동 검증(+15 tests). ③ `GuardianInviteModal.test.jsx`(81 lines) — invite/expire/resend/scope 4건 회귀(+4 tests). HEAD `npm test` 13/5→**32/7 PASS**(+19 tests/+2 files, FE-7 회귀 없음)·build 111 modules PASS(JS 313.68 kB gzip 91.78)·`npm audit --audit-level=high` 0건. **R-05 Must API JWT 라우팅·R-07 J01/J02 라우팅 fetch-mock 자동화 진전** — 라이브 7역할 JWT E2E·J01 백엔드 초대 API 잔여. FE-6 #2 Fixed 후 **4커밋 무재발**(a84473f→ed1bf22→404a30e→cc34f23).

**frontend 26차 UXD 12차 LoginPage DS·Modal 접근성 흡수 (결정 52)**: `404a30e feat(ux): LoginPage DS·Modal 포커스 트랩·forced-colors·prefers-contrast` — `LoginPage.jsx`·`Modal.jsx`·`components.css` 3 files +183/-28. DS Field/TextInput/Button 컴포넌트 적용으로 v1.1 인증 화면 시각 시스템 정착·모노그램 카드 일관성·Modal 포커스 트랩으로 키보드 사용성·`forced-colors`·`prefers-contrast` 미디어 쿼리로 **WCAG 1.4.11 비텍스트 대비 충족**(시스템 고대비·강제 색 모드 준수). DESIGN_SYSTEM §9 접근성 진전. 결정 52에 따라 v1.1 develop→test merge 동반 흡수.

**결정 52 흡수 6묶음(19차 갱신)**: ① v1.2 P0 `a72e249`(42 files), ② v1.1 US-D03 `3fc549a`(2 files), ③ UXD 10차 `5656e19`(7 files), ④ UXD 11차 `2d742b3`(7 files), ⑤ COD 17차 `a84473f`(8 files) + `ed1bf22`(2 files), ⑥ **UXD 12차 `404a30e`(3 files, LoginPage DS·Modal 접근성)** + **COD 18차 `c3f3146`(1 file, PilotChecklistApiAccessTest 29 @Test)** + **COD 19차 `cc34f23`(3 files, pilotChecklist fetch-mock·GuardianInviteModal 회귀)**. 총 **9커밋 / ~78 files** 모두 v1.1 develop→test merge 시 동반 승격. v1.2 정식 완료 기준(2단 SideNav 모듈 가중 커버리지 ≥60%·실데이터 위젯 E2E·등급이력 UI·보호자 CRUD·입금·미납 E2E)은 v1.1 merged 후 v1.2 사이클.

**J01 백엔드 API 미구현 — 신규 PLN 명세 필요**: TSR 27차 검증 `GuardianInviteModal.test.jsx` 회귀 4건은 **프론트 스텁 동작**(invite/expire/resend/scope UI 상태 전이만 검증). 실제 J01 E2E 달성을 위해서는 다음이 필요:
- **API_SPEC §4 신규 엔드포인트 명세** (이번 라운드 작성 보류 — 채널·만료 정책 결정 필요):
  - `POST /clients/{clientId}/guardians/invitations` — 초대 발송(이메일/SMS — 채널은 추가 질문 #33 v1.1 = 인앱·FCM·이메일 골격 → 1종 확정 필요)
  - `POST /guardian/invitations/{token}/accept` — 보호자가 초대 수락 시 `guardian` 계정 생성·`guardian_clients` 연결
  - `GET /guardian/invitations` — 만료/재발송 목록
  - `POST /guardian/invitations/{id}/resend` · `DELETE /guardian/invitations/{id}` — 만료·재발송 UI
- **DBA `guardian_invitations` 테이블** 신규(추가 질문 #35 가설 스키마): `id`·`tenant_id`·`branch_id`·`client_id`·`channel`·`token_hash`·`status`(PENDING/SENT/ACCEPTED/EXPIRED/REVOKED)·`expires_at`·`accepted_at`·`accepted_by_user_id`·`created_at`·`audit` — 만료 정책(예: 7일)·재발송 횟수 한도 합의 필요.
- **PLN 의사결정 대기**: 채널 1종 확정(추가 질문 #33), 만료/재발송 정책(추가 질문 #35) — 두 결정 모두 v1.1 merge ready 전 필수.

**#36 에스컬레이션 완전 종결 확인**: backend BE-6 패턴 #1·#2·#3 모두 해소 후 **5커밋 무재발**(22차 4274459 → 24차 aa71412 → 26차 c3f3146). frontend FE-6 패턴 #1·#2 모두 해소 후 **4커밋 무재발**(25차 a84473f → 25차 ed1bf22 → 26차 404a30e → 27차 cc34f23). **양 스트림 dirty-tree·미커밋 패턴 완전 종결** — 운영 게이트(pre-commit hook 등) 권고 **공식 보류 확정**.

**coder 다음 액션 (19차, 우선순위)**: ① **v1 완료 기준 잔여 `[ ]`**: 7역할 **라이브 JWT 로그인 E2E**(`PilotChecklistApiAccessTest` 단위 충족 → live Spring Security filter chain·JWT 발급/검증 E2E 시나리오 1건씩), SEC-007 develop→test merge 후 P0 패치 재검증 → `merge_status: ready` → **B01·SEC-007 동반 해소**. ② **v1.1 J01 백엔드 API 명세 확정 대기 후 구현**: ❶ PLN — API_SPEC §4 `/guardians/invitations` 명세(채널 #33·만료 #35 결정 필요), ❷ DBA — `guardian_invitations` 테이블 V41 migration, ❸ COD — `GuardianInvitationController`·`GuardianInvitationService`·토큰 검증·이메일/SMS 발송 통합, ❹ Frontend — `GuardianInviteModal` 스텁 제거·실 API 연동 → B03 ready → merge(흡수 6묶음 자동 동반·결정 52, B05 동반 해소). ③ v1.2 본격 사이클(2단 SideNav 모듈 가중 커버리지 ≥60%·E2E·등급이력 UI)은 v1.1 merged 후.

### [PLN] QA 피드백 반영 (2026-06-06, 18차 — TSR 24·25차 + B07 recurrence #2 Fixed + SEC-008 Fixed + R-02 Must API 라우팅 [x] 승격 + UXD 11차 dark mode 흡수)

> TSR 24차(21:13 backend COD 16차 `aa71412` — Must API 라우팅·RBAC·ProductionSecretValidator 단위 테스트 3 files 일괄 커밋, `@Test` 154; frontend UXD 11차 `2d742b3` dark mode 7 files; npm audit 5 vuln/1 critical SEC-008 신규 Open)·25차(21:32 frontend COD 17차 `a84473f`(US-M02 대시보드 실데이터 8 files) + `ed1bf22`(SEC-008 vite 6·vitest 4·esbuild override) — working tree CLEAN, HEAD build 111·`npm test` 13/5·`npm audit` 0건). **양 스트림 dirty-tree·B02·B07·SEC-008 사유 모두 소멸** — 잔여 BLOCK = merge 게이트(B01·B03·B05·SEC-007) 단일.

| QA id | sev | ver | 18차 관측 | 상태 |
|-------|-----|-----|----------|------|
| QA-20260606-B07 | BLOCK | v1.1/v1.2 | COD 17차 `a84473f` US-M02 8 files 일괄 커밋·working tree CLEAN·HEAD build 111·`npm test` 13/5 PASS·이관 규율 5·6·7 PASS — TSR 25차 독립 검증 | Planned→**Fixed**(recurrence #2 정식 Fixed) |
| SEC-20260606-008 | MEDIUM | v1.1 | COD 17차 `ed1bf22` vite `^6.4.3`·vitest `^4.1.8`·`overrides.esbuild ^0.25.0` → develop `npm audit --audit-level=high` 0건·all 0 vulnerabilities — TSR 25차 독립 검증 | Open→**Fixed**(동일 사이클 24차→25차) |
| (R-02) Must API 라우팅 | — | v1 | TSR 24차 `MustApiEndpointRoutingTest` §1–§9 26+ @Test 커버 — develop `aa71412` `@Test` 154 | PARTIAL→**[x] 승격** |
| QA-20260606-B02 | BLOCK | v1 | develop `aa71412` CLEAN·`@Test` 154·Maven 79/79 PASS — recurrence #3 해소 후 4커밋 무재발 | Fixed(유지·강화) |
| QA-20260606-B01 | BLOCK | v1 | `merge_status: pending` — v1 완료 기준 미충족(7역할 E2E·P1–P8 E2E)+SEC-007 잔여 | Planned(잔존) |
| QA-20260606-B03 | BLOCK | v1.1 | 7역할 E2E·J01·Must API E2E 잔여; **v1.2 P0 + UXD 10·11차 + US-M02 + SEC-008 흡수 5건**(결정 52) | Planned(잔존) |
| QA-20260606-B05 | BLOCK | v1.1 | 선행 v1 merged 미충족 | Planned(잔존) |
| SEC-20260606-007 | BLOCK | v1 | test P0 미패치 — B01 동반 | Planned(잔존) |

**backend 24차 R-02 [x] 승격**: COD 16차 `aa71412` `feat(test)` — 22차 `4274459` `@Test` 120 → 24차 `aa71412` `@Test` **154**(+34, MustApiEndpointRoutingTest 26+ tests +459줄·RoleBasedControllerAccessTest 확장 +148줄·ProductionSecretValidatorTest +59줄). Maven 79/79 PASS(test)·package SUCCESS(76,466,058 B) 재현. **R-02 Must API 엔드포인트** 17차까지 PARTIAL → 24차 [x] 승격(인증·이용자·출석·건강·청구·NHIS reconciliation·대시보드 라우팅 단위 테스트 26+ 커버). working tree CLEAN — BE-6 #3 해소 후 **4커밋 무재발**, 패턴 종결 신호.

**frontend 25차 B07 recurrence #2 Fixed + SEC-008 Fixed (동일 COD 17차 사이클)**: ① `a84473f feat(v1.2-p0): 대시보드 실데이터 위젯·Must 페이지 API 보강 (US-M02)` — 23차 미커밋이던 8 files(`dashboardWidgets.js`·`.test.js` 3 tests·`DashboardPage`·`AttendancePage`·`ClientFormPage`·`GuardiansPage`·`GuardianListCard`·`services.js`) +636/-170 일괄 커밋. ② `ed1bf22 fix(security): vite 6·vitest 4·esbuild override` — `package.json` overrides.esbuild `^0.25.0` + vite `^6.4.3` + vitest `^4.1.8` 메이저 업그레이드(`package-lock.json` +390/-303). develop HEAD `npm run build` **111 modules PASS**(vite 6.4.3, JS 313.14 kB gzip 91.58)·`npm test` **13 tests/5 files PASS**(vitest 4.1.8, FE-7 회귀 없음)·`npm audit --audit-level=high` **0건**(all 0 vulnerabilities; 24차 5/1 critical → 25차 0). 이관 규율 5·6·7 모두 충족.

**SEC-008 동일 사이클 처리(24차→25차)**: TSR 24차에서 SEC-008 신규 Open으로 등록(`docs/qa/QA_FEEDBACK.md` Open 섹션) → 같은 라운드 안에 COD 17차가 `ed1bf22`로 vite/vitest/esbuild 메이저 업그레이드 → TSR 25차에서 audit 0건 검증. dev 환경 전용 취약점(prod 번들 무관)이라 v1.1 merge 게이트 BLOCK이 아닌 MEDIUM Open이었으나, 빠른 업그레이드로 **동일 사이클 Open→Fixed**.

**UXD 11차 `2d742b3` 흡수(결정 52 적용)**: `feat(ux): dark mode toggle·tokens.css·AppShell·theme.js`(7 files +280/-1) — `ThemeToggle.jsx`·`tokens.css` CSS 변수·`AppShell` dark/light 전환·`theme.js` 컨텍스트. DESIGN_SYSTEM §1·§9 시각 시스템 확장. 결정 52에 따라 v1.1 develop→test merge에 **동반 흡수**(별도 v1.2 merge 라운드 불추가).

**잔여 흡수 묶음(결정 52)**: ① v1.2 P0 `a72e249`(42 files), ② v1.1 US-D03 `3fc549a`(2 files), ③ UXD 10차 `5656e19`(7 files), ④ UXD 11차 `2d742b3`(7 files), ⑤ COD 17차 `a84473f`(8 files) + `ed1bf22`(2 files). **5묶음·~68 files** 모두 v1.1 develop→test merge 시 동반 승격. v1.2 정식 완료 기준(2단 SideNav 모듈 가중 커버리지 ≥60%·실데이터 위젯 E2E·등급이력 UI·보호자 CRUD·입금·미납 E2E)은 v1.1 merged 후 v1.2 사이클에서 평가.

**coder 다음 액션 (18차, 우선순위)**: ① **v1 완료 기준 잔여 `[ ]`**: 7역할 JWT 로그인·메뉴·권한 분리(`RoleBasedControllerAccessTest` 36 tests PARTIAL → E2E 보강), §6 Must·§6-2 P0–P1 체크리스트, USER_STORIES P1–P8 E2E(수기 출석·월말 청구·reconciliation), SEC-007 develop→test merge 후 P0 패치 재검증 → `merge_status: ready` → **B01·SEC-007 동반 해소**. ② v1.1 잔여 `[ ]`: Must 화면 API 연동 E2E P1–P8(백엔드 v1 test 승격 후 라이브), 보호자 초대·명세 E2E US-J01(백엔드 API 미구현 — API_SPEC §5 PLN 명세 후 DBA `guardian_invitations` 테이블·COD 구현) → `merge_status: ready` → **B03 해소**(v1.2 P0·UXD 10·11차·US-M02·SEC-008 자동 동반·결정 52). v1.1 merged 시 **B05 동반 해소**. v1.2 본격 사이클(2단 SideNav 모듈 가중 커버리지 ≥60%·E2E·등급이력 UI)은 v1.1 merged 후.

### [PLN] QA 피드백 반영 (2026-06-06, 17차 — TSR 22·23차 + B02 recurrence #3 Fixed + B07 recurrence #2 Planned + UXD 10차 + US-M02 WIP)

> TSR 22차(20:11 backend B02 recurrence #3 Fixed via `4274459`, COD 15차 — TSR 독립 검증)·23차(20:17 frontend B07 recurrence #2 — `5656e19`(UXD 10차) 위 대시보드 실데이터 WIP 8 files 미커밋). backend develop `4274459` HEAD CLEAN·`@Test` 120·Maven 79/79 PASS — B02 recurrence #3 정식 Fixed. frontend HEAD `5656e19` Fixed·working tree DIRTY 8 files(FE-6 위반·FE-7 충족) — recurrence #2.

| QA id | sev | ver | 17차 관측 | 상태 |
|-------|-----|-----|----------|------|
| QA-20260606-B02 | BLOCK | v1 | develop `4274459` clean·`@Test` 120·Maven 79/79 PASS·NHIS·Billing routing·RBAC 테스트 3 files 커밋 | Planned→**Fixed**(recurrence #3 정식 Fixed) |
| QA-20260606-B07 | BLOCK | v1.1/v1.2 | HEAD @ `5656e19`(UXD 10차) Fixed **유효**(규율 5 PRESENT); 23차 working tree **8 files** US-M02 대시보드 실데이터 WIP 미커밋(`dashboardWidgets.js/.test.js`·`DashboardPage`·`AttendancePage`·`ClientFormPage`·`GuardiansPage`·`GuardianListCard`·`services.js`); WT build 112·`npm test` 13/5 PASS(FE-7 충족·신규 위젯 테스트 3건·회귀 없음) | Open→**Planned**(recurrence #2) |
| QA-20260606-B01 | BLOCK | v1 | `merge_status: pending` — v1 완료 기준 미충족(E2E·Must API)+SEC-007 잔여 (B02 recurrence #3 해소) | Planned(잔존) |
| QA-20260606-B03 | BLOCK | v1.1 | 7역할 E2E·J01·Must API E2E 잔여; **v1.2 P0 + UXD 10차 산출물 동반 흡수**(결정 52) | Planned(잔존) |
| QA-20260606-B05 | BLOCK | v1.1 | 선행 v1 merged 미충족 | Planned(잔존) |
| SEC-20260606-007 | BLOCK | v1 | test P0 미패치 — B01 동반 | Planned(잔존) |

**backend 22차 B02 recurrence #3 Fixed**: COD 15차 `4274459` `feat(test)` — 20차 미커밋이던 `NhisImportServiceTest`(+56, 지점 검증·수동 매칭)·`RoleBasedControllerAccessTest`(+239/-4, billing/guardian RBAC 확장)·`BillingControllerRoutingTest`(신규, 3 `@Test`) 일괄 커밋. develop `@Test` 98→**120**, Maven 79/79 PASS·package SUCCESS 재현. **BE-6 #3 정식 해소**(이관 규율 6 충족) — 3회 반복 패턴은 #36에서 추적 유지.

**frontend 23차 B07 recurrence #2**: 21차 `a72e249`+`3fc549a` clean → 22~23차 사이 **UXD 10차 `5656e19`** 정상 커밋(이용자 본인 계정 발급·`CopayTypeSelect`·브랜드색 — DESIGN_SYSTEM·결정 27/16, 5 ahead of origin) → 그 위에 v1.2 P0 **US-M02 대시보드 실데이터 위젯 작업** 8 files WIP 미커밋(이관 규율 6·7 위반). WT 품질 게이트는 충족(build 112·`npm test` 13/5 PASS·신규 `dashboardWidgets.test.js` 3건 PASS) — **기능 결함 아닌 미커밋 프로세스 위반**. v1.2 P0 흡수 범위(결정 52) 내 작업이므로 commit 후 v1.1 merge에 자동 동반 흡수.

**v1.2 P0 진전(US-M02)**: `dashboardWidgets.js` 위젯 집계 로직(오늘 출석/결석·미납·미매칭 NHIS 등)이 WT에 완성·develop HEAD 미커밋. 결정 49 KPI ≥60% 모듈 가중 커버리지 달성에 기여 — coder commit 후 v1.2 P0 완료 기준 「실데이터 위젯」 항목 추가 진전.

**coder 다음 액션 (17차, 우선순위)**: ① **B07 recurrence #2** — US-M02 대시보드 실데이터 위젯 8 files **develop 커밋 또는 stash/revert**(FE-6·FE-7, 이관 규율 7) → frontend working tree clean. ② v1 완료 기준(E2E·P1–P8·Must API·SEC-007) → `merge_status: ready` → develop→test merge(B01·SEC-007 동반 해소). ③ v1.1 E2E·J01(보호자 초대 백엔드 API — API_SPEC §5 PLN 명세 후) → B03 ready → merge(v1.2 P0 `a72e249`·UXD 10차 `5656e19`·US-M02 대시보드 위젯 자동 동반·결정 52, B05 동반 해소). v1.2 본격 사이클(2단 SideNav 커버리지 ≥60%·E2E·등급이력 UI)은 **v1.1 merged 후**.

### [PLN] QA 피드백 반영 (2026-06-06, 16차 — TSR 20·21차 + B02 recurrence #3 + B07 Fixed + v1.2 P0 흡수)

> TSR 20차(19:12 backend B02 recurrence #3, 신규 테스트 3 files 미커밋)·21차(19:22 frontend B07 recurrence Fixed, `a72e249` v1.2 P0 + `3fc549a` US-D03 일괄 커밋, working tree CLEAN). backend develop `b5d70a8` HEAD Fixed **유지**·working tree **DIRTY**(BE-6 #3 위반). frontend HEAD `3fc549a` Fixed·working tree **CLEAN**(FE-6·FE-7 충족, B07 정식 Fixed).

| QA id | sev | ver | 16차 관측 | 상태 |
|-------|-----|-----|----------|------|
| QA-20260606-B02 | BLOCK | v1 | HEAD @ `b5d70a8` Fixed **유효**(규율 5 PRESENT); 20차 working tree **3 files** 신규 테스트 미커밋(`NhisImportServiceTest` +56·`RoleBasedControllerAccessTest` +239/-4·`BillingControllerRoutingTest` 3 `@Test`) | Open→**Planned**(recurrence #3) |
| QA-20260606-B07 | BLOCK | v1.1/v1.2 | HEAD @ `3fc549a` Fixed·working tree CLEAN; HEAD `npm test` 10/4·build 110 modules PASS — 21차 TSR 독립 검증 | Planned→**Fixed** |
| QA-20260606-B01 | BLOCK | v1 | `merge_status: pending` — v1 완료 기준 미충족(E2E·Must API)+SEC-007+**B02 recurrence #3** 잔여 | Planned(잔존) |
| QA-20260606-B03 | BLOCK | v1.1 | 7역할 E2E·J01·Must API E2E 잔여; **v1.2 P0 산출물 동반 흡수**(결정 52) | Planned(잔존) |
| QA-20260606-B05 | BLOCK | v1.1 | 선행 v1 merged 미충족 | Planned(잔존) |
| SEC-20260606-007 | BLOCK | v1 | test P0 미패치 — B01 동반 | Planned(잔존) |

**backend 20차 B02 recurrence #3**: 17·18차 CLEAN(`b5d70a8`) 해소 직후 신규 테스트 작성 → develop 미커밋 패턴 **반복(#3)**. 신규 테스트는 유효한 RBAC·NHIS import·Billing 라우팅 확장(coverage 강화)이나 dirty-tree로 merge 게이트 검증 tree 오염. **BE-6 재발 — 이관 규율 6 반복 위반**.

**frontend 21차 B07 recurrence Fixed**: 19~20차 dirty 35~42 files → `a72e249 feat(v1.2-p0)`(+3863/-311) 42 files 일괄 커밋으로 working tree clean. HEAD build 110 modules·`npm test` 10/4 PASS — 이관 규율 5·6·7 PASS, FE-7 정식 충족. v1.2 P0 산출물은 **결정 52**에 따라 v1.1 develop→test merge에 동반 흡수.

**coder 다음 액션 (16차, 우선순위)**: ① **B02 recurrence #3** — 신규 테스트 3 files **develop 커밋 또는 revert**(BE-6, `mvn -q test` PASS 후) → backend working tree clean. ② v1 완료 기준(E2E·P1–P8·Must API·SEC-007) → `merge_status: ready` → develop→test merge(B01·SEC-007 동반 해소). ③ v1.1 E2E·J01(보호자 초대 API) → B03 ready → merge(B05 동반 해소). v1.2 P0 산출물(`a72e249`)은 ③의 v1.1 merge에 자동 동반.

### [PLN] QA 피드백 반영 (2026-06-06, 15차 — TSR 17·18·19차 + B02 Fixed + B07 FE-7 회복)

> TSR 17차(18:34 backend B02 Fixed)·18차(18:42 backend 불변)·19차(18:45 frontend). backend develop `b5d70a8` **CLEAN** — B02 recurrence **Fixed 확정**. frontend HEAD `998ac87` Fixed **유지**, working tree **B07 recurrence**(35 files, WT build/test **PASS**).

| QA id | sev | ver | 15차 관측 | 상태 |
|-------|-----|-----|----------|------|
| QA-20260606-B02 | BLOCK | v1 | develop `b5d70a8` clean·GuardianAccess RBAC 3 tests **Fixed**(17차 TSR 검증) | **Fixed** |
| QA-20260606-B07 | BLOCK | v1.1/v1.2 | HEAD @ `998ac87` Fixed **유효**; 19차 **35 files**·WT build/test **PASS**(FE-7 회복) | Planned(**dirty-tree 지속**) |
| QA-20260606-B01 | BLOCK | v1 | `merge_status: pending` — E2E·API·SEC-007 잔여 | Planned(잔존) |
| QA-20260606-B03 | BLOCK | v1.1 | 7역할 E2E·J01·Must API E2E + **B07 recurrence** 선행 | Planned(잔존) |
| QA-20260606-B05 | BLOCK | v1.1 | 선행 v1 merged 미충족 | Planned(잔존) |
| SEC-20260606-007 | BLOCK | v1 | test P0 미패치 — B01 동반 | Planned(잔존) |

**backend 17·18차**: develop `b5d70a8` working tree **CLEAN**, `@Test` 98, Maven 79/79(test) 재현. 잔여 BLOCK = **merge 게이트 단일**(B01·SEC-007) — dirty-tree·B02 사유 **소멸**.

**frontend 19차 B07**: 16차 29→**35 files**(v1.2 P0 WIP 확대). WT `npm test` 10/4·build 107 modules **PASS** — FE-7 **충족**, dirty-tree·규율 6·7 **지속**.

**coder 다음 액션 (15차, 우선순위)**: ① **B07 recurrence** — v1.2 WIP **develop 커밋 또는 revert** → working tree clean (FE-6·FE-7 충족). ② v1 완료 기준(E2E·P1–P8·SEC-007) → `merge_status: ready` → merge(B01·SEC-007). ③ v1.1 E2E·J01 → B03 ready.

### [PLN] QA 피드백 반영 (2026-06-06, 13차 — TSR 15·16차 + B02 recurrence + B07 WT 회귀)

> TSR 15차(18:04 backend)·16차(18:07 frontend). backend `fac3d07` HEAD Fixed **유지**, working tree **B02 recurrence**(`RoleBasedControllerAccessTest` +74 lines). frontend HEAD `998ac87` Fixed **유지**, working tree **B07 recurrence 악화**(29 files, WT build/test FAIL).

| QA id | sev | ver | 13차 관측 | 상태 |
|-------|-----|-----|----------|------|
| QA-20260606-B02 | BLOCK | v1 | HEAD @ `fac3d07` clean **유효**; 15차 working tree **1 modified** RBAC 테스트 확장 미커밋 | Open→**Planned**(recurrence) |
| QA-20260606-B07 | BLOCK | v1.1/v1.2 | HEAD @ `998ac87` Fixed **유효**; 16차 **29 files**·WT `routeAccess.js` duplicate → build/test **FAIL** | Planned(**강화**) |
| QA-20260606-B01 | BLOCK | v1 | `merge_status: pending` — E2E·API·SEC-007·**B02 recurrence** 잔여 | Planned(잔존) |
| QA-20260606-B03 | BLOCK | v1.1 | 7역할 E2E·J01·Must API E2E + **B07 recurrence** 선행 | Planned(잔존) |
| QA-20260606-B05 | BLOCK | v1.1 | 선행 v1 merged 미충족 | Planned(잔존) |
| SEC-20260606-007 | BLOCK | v1 | test P0 미패치 — B01 동반 | Planned(잔존) |

**backend 15차 B02 recurrence**: `RoleBasedControllerAccessTest` `GuardianAccess` nested class — `guardianCanListCheckinTargets`·`clientUserCanViewDailyRecords`·`caregiverCannotAccessGuardianCheckinTargets`. v1 7역할 RBAC **부분 진전 유지**(fac3d07 HEAD), WIP는 develop 커밋 또는 revert(BE-6).

**frontend 16차 B07 강화**: 14차 19 files→**29 files**. WT `npm test` 6 passed/3 files FAIL(`routeAccess.test.jsx` duplicate)·`npm run build` FAIL(`routeAccess.js:29` duplicate `ROUTE_ACCESS`). → **FE-7** 신설: 커밋 전 build/test PASS.

**coder 다음 액션 (13차, 우선순위)**: ① **B02 recurrence** — RBAC 테스트 확장 **develop 커밋 또는 revert** → backend clean (BE-6). ② **B07 recurrence** — `routeAccess.js` duplicate 수정 → `npm test`·`npm run build` PASS → commit or revert (FE-6·FE-7). ③ v1 완료 기준(E2E·P1–P8·SEC-007·QA-B02) → `merge_status: ready` → merge(B01·SEC-007). ④ v1.1 E2E·J01 → B03 ready.

### [PLN] QA 피드백 반영 (2026-06-06, 12차 — TSR 13·14차 + B07 recurrence)

> TSR 13차(17:30 backend)·14차(17:35 frontend). backend `fac3d07` clean·RBAC/guidance **부분 진전**. frontend HEAD `998ac87` Fixed **유지**, working tree **v1.2 P0 dirty**(B07 recurrence).

| QA id | sev | ver | 12차 관측 | 상태 |
|-------|-----|-----|----------|------|
| QA-20260606-B07 | BLOCK | v1.1/v1.2 | HEAD @ `998ac87` clean **유효**; 14차 working tree **19 files** v1.2 P0 미커밋 | Open→**Planned**(recurrence) |
| QA-20260606-B01 | BLOCK | v1 | `merge_status: pending` — E2E·API·SEC-007 잔여 | Planned(잔존) |
| QA-20260606-B03 | BLOCK | v1.1 | 7역할 E2E·J01·Must API E2E + **B07 recurrence** 선행 | Planned(잔존) |
| QA-20260606-B05 | BLOCK | v1.1 | 선행 v1 merged 미충족 | Planned(잔존) |
| SEC-20260606-007 | BLOCK | v1 | test P0 미패치 — B01 동반 | Planned(잔존) |

**backend 13차 부분 진전**: develop `fac3d07` — guardian billing API·`NhisImportGuidance`·`RoleBasedControllerAccessTest`(7-role RBAC). v1 완료 기준 7역할·롱텀2026 안내 **PARTIAL**(단위 테스트/API, E2E·import UI 잔여).

**frontend 14차 B07 recurrence**: v1.2 P0 WIP — `GuardiansPage`·`PaymentPage`·`OverduePage`·`GradeHistoryTimeline`·`DashboardWidgetGrid`·SideNav 2단·`routeAccess.js`·`ClientDetailPage` 초대 UI. working tree `npm test` 10/4·build 96 modules.

**coder 다음 액션 (12차, 우선순위)**: ① **B07 recurrence** — v1.2 WIP **develop 커밋 또는 revert** → working tree clean (FE-6). ② v1 완료 기준(E2E·P1–P8·SEC-007) → `merge_status: ready` → merge(B01·SEC-007). ③ v1.1 Must API E2E·7역할·J01 → B03 ready. v1.2 본격 착수는 **v1.1 merged 후**.

### [PLN] QA 피드백 반영 (2026-06-06, 11차 — TSR 11·12차 + SEC-007)

> TSR 11차(16:40 backend)·12차(16:55 frontend) — **COD 11차 조치 반영**. develop working tree **양 스트림 clean**, false Fixed **0건**.

| QA id | sev | ver | 11차 관측 | 상태 |
|-------|-----|-----|----------|------|
| QA-20260606-B06 | BLOCK | v1 | develop `4d476c6` clean·`primaryGuardian` PRESENT | **Fixed** |
| QA-20260606-B02 | BLOCK | v1 | develop `4d476c6` clean | **Fixed** |
| QA-20260606-B07 | BLOCK | v1.1 | develop `998ac87` clean·49 files | **Fixed** |
| QA-20260606-B04 | BLOCK | v1.1 | B07 동반 해소 | **Fixed** |
| QA-20260606-H04 | HIGH | v1.1 | `src/api/*`·15+ 페이지 develop HEAD | **Fixed** |
| QA-20260606-M01 | MEDIUM | v1.1 | `npm test` 6/6 develop HEAD | **Fixed** |
| SEC-20260606-005 | HIGH | v1.1 | AuthContext 메모리 세션 | **Fixed** |
| SEC-20260606-007 | BLOCK | v1 | test `2799e29` P0 미패치 — B01 동반 | Open→**Planned** |
| QA-20260606-B01 | BLOCK | v1 | `merge_status: pending` — E2E·API 잔여 | Planned(잔존) |
| QA-20260606-B03 | BLOCK | v1.1 | 7역할 E2E·J01·Must API E2E 미충족 | Planned(잔존) |
| QA-20260606-B05 | BLOCK | v1.1 | 선행 v1 merged 미충족 | Planned(잔존) |

**진단**: dirty-tree·false Fixed 블로커 **해소**(COD 11차). 잔여 BLOCK = **merge 게이트 3건 + SEC-007(B01 동반)** — 기능 산출물은 develop HEAD에 존재, **v1/v1.1 완료 기준 미충족 항목(E2E·J01) + merge 미실행**이 유일 원인.

**coder 다음 액션 (11차)**: ① v1 완료 기준 잔여 `[ ]`(API Must E2E·7역할·P1–P8·SEC-007) 충족 → `merge_status: ready` → **develop→test merge(B01·SEC-007 해소)** → ② v1.1 Must API E2E·7역할·J01(백엔드 초대 API) → B03 ready → B05 해소.

### [PLN] QA 피드백 반영 (2026-06-06, 9차 — TSR 8·9차 재검증·coder 미조치 확인)

> TSR 8차(2026-06-06T15:38)·9차(15:45) 재검증에서 **회귀·이관 상태 완전 불변, coder 미조치, 신규 Open 0건** 확인. 7차에 Planned로 옮긴 9건이 그대로 잔존 — 신규 태스크화 불필요. 벤치마크(`BENCHMARK_REPORT`·`COMPETITOR_MATRIX` 5차)는 신규 입력 없음(이미 반영).

| QA id | sev | ver | 9차 관측 | 상태 |
|-------|-----|-----|----------|------|
| QA-20260606-B01 | BLOCK | v1 | `merge_status: pending` 유지 — 완료 기준 미충족 | Planned(잔존) |
| QA-20260606-B06 | BLOCK | v1 | develop `7d9d2eb` dirty(6 mod + 2 untracked, V39 미커밋) 동일 | Planned(잔존) |
| QA-20260606-B03 | BLOCK | v1.1 | `merge_status: pending` 유지 | Planned(잔존) |
| QA-20260606-B04·B07 | BLOCK | v1.1 | develop dirty **악화** 22 mod + 20 untracked(신규 `AttendanceStatsPage`·`BranchesPage`) | Planned(잔존·악화) |
| QA-20260606-B05 | BLOCK | v1.1 | 선행 v1 `pending` 유지 | Planned(잔존) |
| QA-20260606-H04 | HIGH | v1.1 | `src/api/*` untracked·페이지 TODO 주석 — develop HEAD 미반영 | Planned(잔존) |
| QA-20260606-M01 | MEDIUM | v1.1 | **신규 관측**: develop working tree `vitest run` **6 tests/3 files PASS** — 로컬 완성·develop HEAD 미커밋 | Planned(잔존) |
| SEC-20260606-005 | HIGH | v1.1 | `AuthContext.jsx` localStorage 잔존 | Planned(잔존) |

**진단**: 잔여 9건은 **기능 갭이 아니라 이관 규율 미준수**가 본질이다. backend Maven 79/79 PASS·frontend build PASS·frontend 자동 테스트(vitest 6 PASS)가 모두 **로컬에는 완성**돼 있으나 develop HEAD 미커밋(B06·B07)·`merge_status: pending`(B01·B03)으로 이관 BLOCK. → 신규 스토리·완료 기준 추가 없이 **이관 규율 1·5·6(완료 단위 develop 커밋·Fixed↔HEAD 정합)** 준수만으로 해소 가능.

**coder 다음 액션 (변동 없음, 7차와 동일)**: ① B06(client↔guardian + V39 develop 커밋 + API_SPEC §4 정합·working tree clean) → 잔여 backend(H02·H01·B02·B01) → **v1 `merge_status: ready`→merged** → ② (frontend) SEC-005·H04·M01·신규 페이지 **완료 단위 develop 커밋**(이미 로컬 완성분 우선) → B07(working tree clean) → B03(v1.1 ready). 각 커밋 전 `git show develop:<path>` 자기검증(결정 44) 필수.

### [PLN] QA 피드백 반영 (2026-06-06, 7차 — dirty-tree 재오염 + frontend false Fixed 회귀)

> TSR 재검증(backend 2026-06-06T14:45·frontend 14:55)에서 신규 Open 5건 발생. backend는 v1 fix 커밋(`7d9d2eb`) 직후 **working tree 재오염**(client↔guardian 미커밋·`createClient` 계약 변경, B06), frontend는 5차 `Fixed` 3건이 develop HEAD(`f1c89d9`) 미반영으로 **Open 복귀**(H04·M01·SEC-005) + working tree 대량 오염(B07). H03·SEC-003은 develop HEAD 가드 커밋 확인 — Fixed 유지.

| QA id | sev | ver | 7차 조치 | 상태 |
|-------|-----|-----|----------|------|
| QA-20260606-B06 | BLOCK | v1 | client↔guardian develop 커밋·working tree clean + `createClient` `primaryGuardian` **계약 명세**(API_SPEC §4); v1 완료 기준 QA-B02 `[x]` 철회 | Open→Planned |
| QA-20260606-B07 | BLOCK | v1.1 | v1.1 산출물(api·테스트·신규 페이지·UI) develop 커밋·working tree clean | Open→Planned |
| QA-20260606-H04 | HIGH | v1.1 | Must 화면 실 API(JWT) 연동 develop 커밋; v1.1 완료 기준 `[x]` **철회**(false Fixed) | Open→Planned |
| QA-20260606-M01 | MEDIUM | v1.1 | Vitest `test` 스크립트 develop 커밋; v1.1 완료 기준 `[x]` **철회**(false Fixed) | Open→Planned |
| SEC-20260606-005 | HIGH | v1.1 | JWT localStorage 제거 → 메모리 세션 develop 커밋; v1.1 완료 기준·US §16 FE-5 신설 | Open→Planned |

**조치 요약**: ① ROADMAP v1 완료 기준 QA-B02 `[x]` 철회(working tree 재오염), v1.1 완료 기준 H04·M01 `[x]` 철회·SEC-005 항목 신설, ② **이관 규율 6항(완료 단위 커밋·API 계약 변경 문서화 게이트)** 신설(결정 45), ③ B06 범위 v1 US-D01 확정 → **API_SPEC §4 `primaryGuardian` 계약 명세화**, ④ USER_STORIES §16 **FE-5**(메모리 세션), ⑤ QA_FEEDBACK Open 5건 → Planned 이동.

**coder 다음 액션 (우선순위 — 7차)**: B06(client↔guardian develop 커밋 + API_SPEC 정합·working tree clean) → H02/H01/B02/B01 잔여 backend → **v1 merged** → (frontend) SEC-005(메모리 세션)·H04(실 API)·M01(Vitest) develop 커밋 → B07(working tree clean)·H03 유지 → B03(v1.1 ready). **각 `Fixed` 전 `git show develop:<path>` 자기검증(결정 44) + 완료 단위 커밋·계약 변경 문서 선반영(결정 45) 필수**.

### [PLN] QA 피드백 반영 (2026-06-06, 6차 — false Fixed 회귀)

> TSR 재검증(2026-06-06T07:52)에서 5차 때 `Fixed`로 기록한 **backend 산출물(QA-H01 파서·SEC-001/002/004=H02)이 develop HEAD 미반영**(test working tree 한정)으로 확인 → **Open 복귀**. backend BLOCK 2(B01·B02)도 재확인. frontend H03·H04·M01은 develop 반영 확인 — `Fixed` 유지.

| QA id | sev | ver | 6차 조치 | 상태 |
|-------|-----|-----|----------|------|
| QA-20260606-B01 | BLOCK | v1 | v1 완료 기준 전 `[x]`(QA-H01 포함) 후 `merge_status: ready` | Planned(재반영) |
| QA-20260606-B02 | BLOCK | v1 | develop working tree clean + 이관 규율 1·5 | Planned(재반영) |
| QA-20260606-H01 | HIGH | v1 | ROADMAP v1 `[x]` **철회** → 파서·테스트 develop 커밋 후 재검증 | Open→Planned |
| QA-20260606-H02 | HIGH | v1 | SEC-001/002/004 develop 커밋 + 이관 규율 1·2·5 | Open→Planned |

**조치 요약**: ① ROADMAP v1 완료 기준 QA-H01 `[x]` 철회(develop 미반영), ② QA_FEEDBACK backend 4건 Open→Planned 재이동, ③ **이관 규율 5항(결정 44 — `git show develop:<path>` 검증 게이트)** 신설, ④ frontend Fixed(H03/H04/M01)는 영향 없음.

**coder 다음 액션 (우선순위 — 6차)**: H02(SEC develop 커밋·정합) → H01(`처리상태` 파서+테스트 develop 커밋) → B02(working tree clean) → B01(v1 완료 기준 전 `[x]`·`ready`) → **v1 merged** → (frontend) B04·B03. **각 `Fixed` 기록 전 `git show develop:<path>` 자기검증 필수**(결정 44).

### [PLN] QA 피드백 반영 (2026-06-06, 5차)

> `docs/qa/QA_FEEDBACK.md` Open **10건**(BLOCK 5·HIGH 4·MEDIUM 1) + `docs/qa/TEST_REPORT.md` 최초 검증을 태스크화 → QA_FEEDBACK **Planned** 이동. coder 수정·develop 커밋 후 **Fixed**.

| QA id | sev | ver | ROADMAP·문서 태스크 | 상태 |
|-------|-----|-----|--------------------|------|
| QA-20260606-B01 | BLOCK | v1 | 완료 기준 전 `[x]` 후 `merge_status: ready` (ROADMAP v1 test merge) | Planned |
| QA-20260606-B02 | BLOCK | v1 | develop working tree clean·Flyway V35/V36 반영 (v1 완료 기준) | Planned |
| QA-20260606-H01 | HIGH | v1 | `처리상태` 파서 **+ 선행열 샘플 테스트** (ROADMAP v1·US-G04) | Planned |
| QA-20260606-H02 | HIGH | v1 | SEC-001/002/004 develop 커밋 (ROADMAP v1·결정 41) | Planned |
| QA-20260606-B03 | BLOCK | v1.1 | 완료 기준 충족 후 `merge_status: ready` (ROADMAP v1.1) | Planned |
| QA-20260606-B04 | BLOCK | v1.1 | develop working tree clean (ROADMAP v1.1) | Planned |
| QA-20260606-B05 | BLOCK | v1.1 | 선행 게이트 — v1 `merged` 후 착수 (ROADMAP v1.1·US §16 FE-4) | Planned |
| QA-20260606-H03 | HIGH | v1.1 | ProtectedRoute(SEC-003) develop 커밋 (ROADMAP v1.1·US §16 FE-2) | Planned |
| QA-20260606-H04 | HIGH | v1.1 | Must 화면 실 API(JWT) 연동 (ROADMAP v1.1·US §16 FE-1·결정 43) | Planned |
| QA-20260606-M01 | MEDIUM | v1.1 | Vitest + RTL `test` 스크립트 (ROADMAP v1.1·US §16 FE-3) | Planned |

**진단**: Maven 81/81·Vite build PASS이나 **이관 BLOCK** — ① SEC fix가 test working tree에만 있고 develop 미커밋(Fixed↔develop 불일치), ② merge_status 미승격, ③ NHIS `처리상태` 파서·프론트 실 API·Vitest 기능 갭. → 이관 규율(결정 41)·완료 기준 보강으로 태스크화.

**coder 다음 액션 (우선순위)**: B02/H02(backend develop 커밋·SEC 정합) → H01(처리상태 파서+테스트) → B01(v1 ready) → **v1 merged** → B04/H03/H04/M01(frontend) → B03(v1.1 ready).

### [PLN] 자동 기획 동기화 — 11차 (2026-06-06)

사용자 대화 없이 `build --role planner` 실행. **핵심 입력**: TSR 11·12차(16:40·16:55), SEC 3차(SEC-007), **BNK 6차 완료**(§9·§8).

| 갱신 | 산출물 |
|------|--------|
| SEC-007 Open→Planned, 11차 QA 노트·진단 갱신, v1 SEC-007 완료 기준, v1.2 BNK-6 범위 확정, QA→태스크 SEC-007 | `ROADMAP.md` |
| §1-5-2 화면 밀도·G13/G14·§6-3 v1.2 P0 | `REQUIREMENTS.md` |
| Epic K·L·M·UX (US-K01~M02·UX-02), §15 갭表 정리 | `USER_STORIES.md` |
| 11차 QA 표·#36 부분 해소·결정 49·BNK 완료 표시 | `PLAN_NOTES.md` |
| 11차 동기화 기록 | `decisions.md` |

**미변경**: API_SPEC·FLOWCHART(계약 변경 없음). **미해결 추적**: #27·#31·#32·#33·#35.

### [PLN] 자동 기획 동기화 — 12차 (2026-06-06)

사용자 대화 없이 `build --role planner` 실행. **핵심 입력**: TSR 13차(17:30 backend)·14차(17:35 frontend). 벤치마크 BNK-6 **이미 반영**(신규 입력 없음).

| 갱신 | 산출물 |
|------|--------|
| 12차 QA 노트·진단·이관 규율 7항, v1 `fac3d07` PARTIAL, v1.1/v1.2 B07 recurrence, v1.2 WIP·완료 기준 | `ROADMAP.md` |
| 12차 QA 표·결정 50·#36 B07 recurrence·backend 13차 부분 진전 | `PLAN_NOTES.md` |
| §16 **FE-6**(v1.2 선행 dirty-tree 금지) | `USER_STORIES.md` |
| B07 recurrence Open→Planned | `QA_FEEDBACK.md` |
| 12차 동기화 기록 | `decisions.md` |

**핵심 판단**: HEAD @ `998ac87` v1.1 Fixed **유효**. B07 recurrence = v1.2 P0 미커밋(19 files). backend `fac3d07` RBAC·NHIS guidance **부분 진전** — v1 E2E 잔여.

**미변경**: REQUIREMENTS(벤치마크 신규 없음)·API_SPEC·FLOWCHART. **미해결 추적**: #27·#31·#32·#33·#35·#36(B07 recurrence).

### [PLN] 자동 기획 동기화 — 20차 (2026-06-06)

사용자 대화 없이 `build --role planner` 실행. **핵심 입력**: TSR 28차(23:19 양 스트림 — backend develop HEAD `c3f3146` 불변·working tree DIRTY 1 untracked `SevenRoleJwtLoginE2eTest.java` 384 lines 7역할 JWT 로그인 E2E 통합 테스트 WIP → QA-B02 recurrence #4 Open·BE-6 #4 재발; frontend UXD 13차 `07fd305` 전사 설정 Switch·셀프 체크인 토글 7 files +218/-7, working tree CLEAN, `npm test` 37/8·build 112·audit 0건)·29차(23:31 frontend COD 20차 `57ff3c0` — `sevenRoleJwtLogin.test.jsx`(132)·`sevenRoleRouteGuard.test.jsx`(83)·`sevenRoleRouteMatrix.js`(75)·`roleHomePaths.test.jsx`(+26) 4 files +316: 7역할 JWT 로그인·라우트 가드 Vitest 단위 E2E 자동화, working tree CLEAN, `npm test` 37/8→**130/10 PASS**(+93/+2)·build 112 modules·audit 0건). 벤치마크 BNK-6 **신규 입력 없음**(이미 반영, 결정 49).

| 갱신 | 산출물 |
|------|--------|
| 20차 동기화 노트·QA→태스크 매핑 B02 recurrence #4 Planned·핵심 진단 29차 갱신, v1 QA-B02 `[x]` 철회·7역할 권한 분리 잔여(라이브 backend E2E) 갱신, v1.1 7역할 화면·메뉴 단위 E2E 자동화 `[x]` 강화·Must API E2E 매트릭스 자동화·B04/B07 6커밋 무재발·SEC-008 26·27·29차 audit 0건 유지·R-04 단위 E2E 정식 충족 주석 추가 | `ROADMAP.md` |
| 20차 QA 표·20차 sync 섹션·결정 52 흡수 7묶음 갱신·#36 에스컬레이션 재오픈(BE-6 #4 재발·종결 공언 철회·운영 게이트 권고 재검토)·UXD 13차 Switch·셀프 체크인 토글 흡수 메모·COD 20차 7역할 JWT 로그인·라우트 가드 단위 E2E 흡수 메모·BE-6 패턴 재오픈 | `PLAN_NOTES.md` |
| §13 파일럿 체크리스트 단위 자동화 진전(frontend 7역할 라우트 매트릭스 단위 E2E 추가)·§16 FE-9 갱신(7역할 JWT 로그인·라우트 가드 단위 E2E 매트릭스 자동화 추가)·§17 BE-6 recurrence #4 갱신(5커밋 무재발 종결 공언 철회)·신규 US-UX-03 또는 §16 추가(전사 설정 Switch·셀프 체크인 토글) | `USER_STORIES.md` |
| **B02 recurrence #4 Open→Planned**(planner 20차 sync 노트, Fixed B02 verified_at 28차 recurrence #4·planner Planned 이동 안내 갱신, 신규 Planned 섹션 항목 [TSR] v1 backend B02 recurrence #4 — coder commit 시 v1 R-04 라이브 E2E 충족 안내) | `QA_FEEDBACK.md` |
| 20차 동기화 기록 | `decisions.md` 최상단 |

**핵심 판단**: ① **backend B02 recurrence #4 Open → Planned** — 19차 「BE-6 5커밋 무재발 완전 종결」 공언을 20차 #4 재발로 **철회**. `SevenRoleJwtLoginE2eTest.java`(384 lines)는 v1 R-04 라이브 7역할 JWT 로그인 E2E 완료 기준을 충족할 직접 자산임에도 develop HEAD 미반영. coder가 `mvn -q test` PASS 후 develop commit 시 B02 #4 자동 Fixed + v1 R-04 라이브 E2E 동시 충족 → B01·SEC-007 동반 해소 경로 단축. ② **frontend R-04 7역할 JWT 로그인·라우트 가드 단위 E2E 자동화 정식 충족** — COD 20차 `57ff3c0` 4 files +316으로 AuthProvider login + LoginPage submit + ProtectedRoute 7역할 매트릭스 단위 검증 자동화. `npm test` 130/10 PASS(+93 tests vs 27차). FE-6 무재발 6커밋. ③ **UXD 13차 Switch·셀프 체크인 토글 흡수(결정 52)** — `Switch.jsx` WAI-ARIA·`SettingsPage` `allow_client_self_checkin` 토글·`Switch.test.jsx` 5건. 결정 16 안 3 UI 정착. US-UX-03 신설(전사 설정 Switch). v1.1 merge 동반. ④ **결정 52 흡수 7묶음 갱신** — 총 12커밋/~89 files(v1.2 P0·US-D03·UXD 10/11/12/13차·COD 17/18/19/20차) 모두 v1.1 develop→test merge 시 동반 승격. ⑤ **잔여 BLOCK = merge 게이트(B01·B03·B05·SEC-007) + B02 #4(BE-6 commit)** — 잔여는 backend 1 commit(`SevenRoleJwtLoginE2eTest.java`)·기능(J01 backend API)·절차(merge ready). ⑥ #36 에스컬레이션 **재오픈** — BE-6 종결 공언 철회, 운영 게이트(pre-commit hook 등) 권고 재검토 필요.

**미변경**: REQUIREMENTS·API_SPEC(J01 초대 계약 미명시 — #33·#35 결정 대기)·FLOWCHART·BENCHMARK(BNK-6 완료). DB(V1–V40)·청구 2단계·QR B·platform_admin·MVP 제외 정책 유지. ERD `guardian_invitations` 가설 스키마(round 35) 보류 유지.  
**미해결 추적**: #27·#31·#32·#33·#35·**#36(BE-6 패턴 #4 재발·종결 공언 철회·운영 게이트 권고 재검토)**.

### [PLN] 자동 기획 동기화 — 19차 (2026-06-06)

사용자 대화 없이 `build --role planner` 실행. **핵심 입력**: TSR 26차(22:20 양 스트림 — backend COD 18차 `c3f3146` `PilotChecklistApiAccessTest` 697 lines 29 @Test 일괄 커밋·USER_STORIES §13 P1–P8 × 7역할 `@PreAuthorize` `@WebMvcTest` 자동화 `@WebMvcTest` 65건; frontend UXD 12차 `404a30e` LoginPage DS·Modal 포커스 트랩·forced-colors·prefers-contrast WCAG 1.4.11)·27차(22:40 frontend COD 19차 `cc34f23` `pilotChecklist.js`(211)·`pilotChecklist.test.js`(104) P1–P8 services.js 매핑·fetch-mock·`GuardianInviteModal.test.jsx`(81) 회귀 4건). 벤치마크 BNK-6 **신규 입력 없음**.

19차 결정 사항(20차에서 일부 갱신·일부 유지): backend R-04 `@WebMvcTest` 65건 PARTIAL 진전, frontend P1–P8 fetch-mock 자동화, UXD 12차 흡수, #36 양 스트림 BE-6/FE-6 패턴 완전 종결 공언 → **20차에 BE-6 #4 재발로 종결 공언 철회**(FE-6는 무재발 유지).

**미변경**(19차 시점): REQUIREMENTS·API_SPEC·FLOWCHART·BENCHMARK. **미해결 추적**: #27·#31·#32·#33·#35·#36(20차에서 BE-6 패턴 재오픈).

### [PLN] 자동 기획 동기화 — 18차 (2026-06-06)

사용자 대화 없이 `build --role planner` 실행. **핵심 입력**: TSR 24차(21:13 backend COD 16차 `aa71412` Must API 라우팅·RBAC·ProductionSecretValidator 테스트 +34 @Test → 154, R-02 PARTIAL→[x]; frontend UXD 11차 `2d742b3` dark mode 7 files; npm audit 5 vuln/1 critical SEC-008 신규 Open)·25차(21:32 frontend COD 17차 `a84473f`(US-M02 8 files 일괄 커밋, B07 recurrence #2 Fixed) + `ed1bf22`(vite 6·vitest 4·esbuild override, SEC-008 Fixed) — develop CLEAN, audit 0건). 벤치마크 BNK-6 **신규 입력 없음**(이미 반영, 결정 49).

| 갱신 | 산출물 |
|------|--------|
| 18차 동기화 노트·QA→태스크 매핑 B07 recurrence #2 Fixed·SEC-008 Fixed·R-02 [x] 승격, 핵심 진단 25차 갱신, v1 QA-B02 `aa71412` 갱신, v1.1 SEC-008 완료 기준 신설·B07 recurrence #2 Fixed 주석, v1.2 US-M02 develop 커밋 [x] | `ROADMAP.md` |
| 18차 QA 표·18차 sync 섹션·#36 양 스트림 패턴 종결 신호(BE-6 4커밋 무재발·FE-6 #2 Fixed)·UXD 11차 흡수 메모 | `PLAN_NOTES.md` |
| §16 **FE-6** recurrence #2 Fixed 갱신, §17 **BE-6** Fixed 강화(4커밋 무재발), §12d **US-M02 Fixed** 진전 메모 갱신 | `USER_STORIES.md` |
| Open 0건 유지(B07 #2·SEC-008 모두 Fixed 이동), planner 18차 sync 노트, B07 Fixed note 갱신(recurrence #2 정식 Fixed), SEC-008 Fixed note 신설 | `QA_FEEDBACK.md` |
| 18차 동기화 기록 | `decisions.md` 최상단 |

**핵심 판단**: ① backend **R-02 Must API 라우팅 [x] 승격** — TSR 24차 COD 16차 `aa71412` `MustApiEndpointRoutingTest` §1–§9 26+ @Test 커버(인증·이용자·출석·건강·청구·NHIS reconciliation·대시보드 전 Must 라우팅), `RoleBasedControllerAccessTest` 확장(36 tests PARTIAL — E2E 잔여), `ProductionSecretValidatorTest` 단위 테스트. develop `@Test` 120→154(+34), Maven 79/79 PASS·package SUCCESS 재현. BE-6 #3 Fixed 후 **4커밋 무재발** — 패턴 종결 신호. ② frontend **B07 recurrence #2 + SEC-008 동일 사이클 Fixed** — COD 17차가 `a84473f`(US-M02 8 files 일괄 커밋, 이관 규율 5·6·7 PASS) + `ed1bf22`(vite 6·vitest 4·esbuild override, audit 5 vuln/1 critical → 0)를 같은 라운드에 처리. develop HEAD CLEAN·build 111 modules·`npm test` 13/5·audit 0건 — FE-6 #2 Fixed, FE-7 회귀 없음. ③ **결정 52 흡수 5묶음**: v1.2 P0 `a72e249` + US-D03 `3fc549a` + UXD 10차 `5656e19` + UXD 11차 `2d742b3` + COD 17차 `a84473f`+`ed1bf22` — v1.1 develop→test merge 동반. ④ **잔여 BLOCK = merge 게이트 단일**(B01·B03·B05·SEC-007) — dirty-tree·B02·B07·SEC-008 사유 전부 소멸, 잔여는 기능(7역할 E2E·P1–P8 E2E·J01) + 절차(merge ready)만.

**미변경**: REQUIREMENTS·API_SPEC(J01 초대 계약 미명시는 PLAN_NOTES `### DB 설계 질문` #35 가설 + 추가질문 #33 채널 결정 대기 — 변경 없음)·FLOWCHART·BENCHMARK(BNK-6 완료). DB(V1–V40)·청구 2단계·QR B·platform_admin·MVP 제외 정책 유지.  
**미해결 추적**: #27·#31·#32·#33·#35·#36(BE-6 패턴 종결·FE-6 패턴 종결 — 양 스트림 dirty-tree 패턴 모두 해소).

### [PLN] 자동 기획 동기화 — 17차 (2026-06-06)

사용자 대화 없이 `build --role planner` 실행. **핵심 입력**: TSR 22차(20:11 backend B02 recurrence #3 Fixed via `4274459`)·23차(20:17 frontend B07 recurrence #2 — `5656e19`(UXD 10차) 위 대시보드 실데이터 WIP 8 files 미커밋·WT build/test PASS·HEAD Fixed 규율 5 PRESENT 유효). 벤치마크 BNK-6 **신규 입력 없음**(이미 반영, 결정 49).

| 갱신 | 산출물 |
|------|--------|
| 17차 동기화 노트·QA→태스크 매핑 B02 recurrence #3 Fixed·B07 recurrence #2 Planned·UXD 10차 흡수·US-M02 진전, 핵심 진단 23차 갱신, v1 QA-B02 `[x]` 복원, v1.1 B07 `[x]` 철회·recurrence #2 주석, v1.2 UXD 10차+US-M02 WIP 메모·완료 기준 갱신 | `ROADMAP.md` |
| 17차 QA 표·17차 sync 섹션·#36 갱신(BE-6 #3 해소·FE-6 #2 신규·반복 패턴) | `PLAN_NOTES.md` |
| §16 **FE-6**(23차 recurrence #2 사례 추가)·§17 **BE-6 recurrence #3 Fixed** 주석 갱신·§12d US-M02 진전(대시보드 위젯 WT 완성) 메모 | `USER_STORIES.md` |
| Open B07 recurrence #2 → Planned 이동, planner 17차 sync 노트, B02 Fixed note 갱신, B07 Fixed note 갱신(recurrence #2 Planned 이동 안내) | `QA_FEEDBACK.md` |
| 17차 동기화 기록 | `decisions.md` 최상단 |

**핵심 판단**: ① backend B02 **recurrence #3 정식 Fixed**(COD 15차 `4274459` — TSR 22차 독립 검증, BE-6 #3 해소). 단 동일 패턴 3회 반복(15·20·해소) → coder 워크플로우 운영 게이트(#36) 권고 유지. ② frontend B07 **recurrence #2** — `5656e19`(UXD 10차) 정상 커밋 후, 그 위에 v1.2 P0 **US-M02 대시보드 위젯 실데이터** WIP 8 files 미커밋. HEAD Fixed 산출물(규율 5) 유효하나 working tree dirty(규율 6·7)로 v1.1 merge 게이트 BLOCK. WT 품질 게이트는 충족(FE-7) — 신규 `dashboardWidgets.test.js` 3 PASS·build 112 modules·`npm test` 13/5 PASS, 회귀 없음 → **기능 결함 아닌 미커밋(프로세스) 위반**. ③ **결정 52 적용**: UXD 10차(`5656e19`) + US-M02 대시보드 위젯(commit 후) 모두 v1.1 develop→test merge에 동반 흡수, 별도 v1.2 merge 라운드 불추가.

**미변경**: REQUIREMENTS·API_SPEC·FLOWCHART(계약 변경 없음)·BENCHMARK(6차 완료). DB(V1–V40)·청구 2단계·QR B·platform_admin·MVP 제외 정책 유지.  
**미해결 추적**: #27·#31·#32·#33·#35·#36(B02 recurrence #3 해소·B07 recurrence #2 신규 — frontend 반복 패턴 #2).

### [PLN] 자동 기획 동기화 — 16차 (2026-06-06)

사용자 대화 없이 `build --role planner` 실행. **핵심 입력**: TSR 20차(19:12 backend B02 recurrence #3)·21차(19:22 frontend B07 recurrence Fixed + v1.2 P0 `a72e249` 일괄 커밋). 벤치마크 BNK-6 **신규 입력 없음**(이미 반영, 결정 49).

| 갱신 | 산출물 |
|------|--------|
| 16차 동기화 노트·QA→태스크 매핑 B02 recurrence #3·v1.2 P0 흡수 결정 52, v1 QA-B02 `[x]` 철회, v1.1 B07 Fixed 갱신, v1.2 status `planned→in_progress`·P0 커밋 완료 기준 `[x]` 승격 | `ROADMAP.md` |
| 16차 QA 표·**결정 52**(v1.2 P0 v1.1 merge 흡수)·#36 갱신(backend B02 recurrence #3 잔존·frontend B07 해소)·16차 sync 섹션 | `PLAN_NOTES.md` |
| §17 **BE-6 recurrence #3** 갱신(NHIS·Billing 라우팅 테스트 추가), §16 **FE-7 21차 정식 충족** 주석 | `USER_STORIES.md` |
| B02 recurrence #3 Open→**Planned** 이동, planner 16차 sync 노트, Fixed B02 note 갱신(현재 Open → 16차 Planned) | `QA_FEEDBACK.md` |
| 16차 동기화 기록 | `decisions.md` 최상단 |

**핵심 판단**: ① backend B02 **recurrence #3** — 17·18차 clean 직후 신규 테스트 미커밋 패턴 **3회째 반복**(BE-6 위반). HEAD Fixed 산출물(규율 5) 유효하나 working tree dirty(규율 6)로 merge 게이트 BLOCK. ② frontend B07 **정식 Fixed** — 19~20차 v1.2 P0 dirty 42 files → `a72e249` 일괄 커밋으로 working tree clean·HEAD build 110·`npm test` 10/4 PASS. ③ **결정 52**: v1.2 P0 산출물(42 files)이 v1.1 라우팅·세션 인프라와 결합되어 분리 비효율 → v1.1 develop→test merge에 동반 흡수. v1.2 정식 완료 기준(2단 SideNav 커버리지 ≥60%·E2E)은 v1.1 merged 후 v1.2 사이클에서.

**미변경**: REQUIREMENTS·API_SPEC·FLOWCHART(계약 변경 없음)·BENCHMARK(6차 완료). DB(V1–V40)·청구 2단계·QR B·platform_admin·MVP 제외 정책 유지.  
**미해결 추적**: #27·#31·#32·#33·#35·#36(B02 recurrence #3 잔존, frontend 해소).

### [PLN] 자동 기획 동기화 — 15차 (2026-06-06)

사용자 대화 없이 `build --role planner` 실행. **핵심 입력**: TSR 17차(18:34 backend B02 Fixed)·18차(18:42 backend 불변)·19차(18:45 frontend B07 FE-7 회복). 벤치마크 BNK-6 **신규 입력 없음**.

| 갱신 | 산출물 |
|------|--------|
| 15차 QA 노트·진단, backend merge 게이트 단일, v1.2 WIP 35 files·WT PASS | `ROADMAP.md` |
| 15차 QA 표·#36 backend 해소·frontend B07 갱신 | `PLAN_NOTES.md` |
| BE-6 Fixed·FE-7 19차 회복 주석 | `USER_STORIES.md` |
| B07 Planned 19차 갱신, planner 15차 sync 노트 | `QA_FEEDBACK.md` |
| 15차 동기화 기록 | `decisions.md` |

**핵심 판단**: backend dirty-tree·B02 recurrence **소멸** — 잔여 = merge 게이트(B01·SEC-007). frontend B07 — **35 files dirty-tree 지속**, FE-7 **충족**(commit 준비 완료).

**미변경**: REQUIREMENTS·API_SPEC·FLOWCHART·BENCHMARK(6차 완료). **미해결 추적**: #27·#31·#32·#33·#35·#36(B07 recurrence).

### [PLN] 자동 기획 동기화 — 13차 (2026-06-06)

사용자 대화 없이 `build --role planner` 실행. **핵심 입력**: TSR 15차(18:04 backend B02 recurrence)·16차(18:07 frontend B07 WT FAIL). 벤치마크 BNK-6 **신규 입력 없음**.

| 갱신 | 산출물 |
|------|--------|
| 13차 QA 노트·진단, v1 QA-B02 `[x]` 철회, v1.2 WIP 29 files·WT build/test FAIL | `ROADMAP.md` |
| 13차 QA 표·결정 51·#36 양 스트림 dirty-tree | `PLAN_NOTES.md` |
| §16 **FE-7**(커밋 전 build/test PASS), §17 **BE-6**(backend dirty-tree) | `USER_STORIES.md` |
| B02 recurrence Open→Planned, B07 Planned 강화 | `QA_FEEDBACK.md` |
| 13차 동기화 기록 | `decisions.md` |

**핵심 판단**: 양 스트림 **동시 dirty-tree recurrence** — backend RBAC WIP(B02)·frontend v1.2 WIP(B07, duplicate `ROUTE_ACCESS`). HEAD Fixed **양쪽 유효**.

**미변경**: REQUIREMENTS·API_SPEC·FLOWCHART·BENCHMARK(6차 완료). **미해결 추적**: #27·#31·#32·#33·#35·#36.

### [PLN] 자동 기획 동기화 — 10차 (2026-06-06)

사용자 대화 없이 `build --role planner` 실행. **9차(16:10) 이후 신규 입력 0건** — `QA_FEEDBACK.md`·`TEST_REPORT.md` 최종 갱신은 TSR 9차(15:45) 그대로(Open 0건), 벤치마크(BNK 6차)는 여전히 **착수 대기**. 이번에는 submodule HEAD·working tree를 **직접 점검**해 9차 관측과 대조 — **완전 동일**(backend `7d9d2eb` 10 mod + 2 untracked, frontend `f1c89d9` 22 mod + 20 untracked). 신규 기획 변경·태스크·결정 **없음** — **현황 재확인·메타 갱신·에스컬레이션 강화**만 수행.

| 갱신 | 산출물 |
|------|--------|
| `## QA 피드백 반영` 10차 노트(submodule HEAD 직접 점검 — 9차 대비 불변), 변경 이력·메타 timestamp | `ROADMAP.md` |
| `### [PLN] 자동 기획 동기화 — 10차` 섹션, **추가 질문 #36 에스컬레이션 강화**(6회 연속 정체·루프 미실행 가능성·권고), 메타 timestamp | `PLAN_NOTES.md` |
| 10차 동기화 기록 | `decisions.md` 최상단 |
| Open 0건 — QA_FEEDBACK Planned 이동 없음(이미 9건 Planned) | (변경 없음) |

**핵심 판단(9차 강화)**: 잔여 BLOCK 9건은 전부 **이관 규율 미준수**가 유일 블로커 — 기능 갭 아님. develop working tree에 산출물이 **사실상 완성**(Maven 79/79·vitest 6 PASS)됐으나 미커밋. 결정 41·44·45로 이미 커버되어 **신규 결정 불필요**. 5·6·7·8·9·10차까지 coder 0건 조치 → #36 에스컬레이션 강화(루프 실제 실행 여부 진단 추가).  
**미변경**: REQUIREMENTS·USER_STORIES·API_SPEC·FLOWCHART(7·8차까지 반영), DB 제약(V1–V39), 청구 2단계·QR B·platform_admin·MVP 제외.  
**미해결 추적**: #27(공단 엑셀 실컬럼·G7), #31(가격 tier), #32(다지점 HQ 사례), #33(보호자 초대 채널), #35(duration_band 표준시간), **#36(coder 미조치 — 강화)**.

### [PLN] 자동 기획 동기화 — 9차 (2026-06-06)

사용자 대화 없이 `build --role planner` 실행. **핵심 입력은 TSR 8차(15:38)·9차(15:45) 재검증**(`QA_FEEDBACK.md`·`TEST_REPORT.md`) — 7차(15:15) 이후 추가된 재검증 2회 모두 **상태 불변, coder 미조치, 신규 Open 0건**. 벤치마크(5차)는 신규 입력 **없음**. 신규 기획 변경·태스크화 불필요 — **현황 정합·정확도 갱신·에스컬레이션** 중심.

| 갱신 | 산출물 |
|------|--------|
| `## QA 피드백 반영` 9차 노트(TSR 8·9차 — B07 악화 22m+20u·신규 페이지, M01 develop working tree `vitest` 6 PASS 미커밋), 메타 timestamp | `ROADMAP.md` |
| v1.1 완료 기준 M01·B07 항목에 9차 근거(로컬 완성·develop HEAD 미커밋) 주석 추가 | `ROADMAP.md` |
| 변경 이력 9차 항목 | `ROADMAP.md` |
| `### QA 피드백 반영 9차` 표·진단, 9차 동기화 섹션, **추가 질문 #36(coder 장기 미조치 에스컬레이션)**, 메타 갱신 | `PLAN_NOTES.md` |
| 9차 동기화 기록 | `decisions.md` 최상단 |
| Open 0건 — QA_FEEDBACK Planned 이동 없음(이미 9건 Planned) | (변경 없음) |

**핵심 판단**: 잔여 BLOCK 9건은 **기능 미구현이 아니라 이관 규율 미준수**(완료 단위 develop 커밋·`merge_status` 미승격). frontend 자동 테스트가 develop working tree에서 통과(vitest 6 PASS)하나 미커밋 — 즉 산출물은 사실상 완성, **develop 커밋 한 단계가 유일 블로커**. 신규 결정·스토리 없음 — 결정 41·44·45(이관 규율 1·5·6)로 이미 커버.  
**미변경**: REQUIREMENTS·USER_STORIES·API_SPEC·FLOWCHART(7차까지 반영 완료), DB 제약(V1–V39), 청구 2단계·QR B·platform_admin·MVP 제외.  
**미해결 추적**: #27(공단 엑셀 실컬럼·G7), #31(가격 tier), #32(다지점 HQ 사례), #33(보호자 초대 채널), #35(duration_band 표준시간), **#36(coder 미조치 에스컬레이션 — 신규)**.

### [PLN] 자동 기획 동기화 — 7차 (2026-06-06)

사용자 대화 없이 `build --role planner` 실행. **핵심 입력은 TSR 재검증 결과**(`QA_FEEDBACK.md`·`TEST_REPORT.md` 2026-06-06T14:45 backend·14:55 frontend) — develop fix 커밋 직후 **dirty-tree 재오염**(backend B06)과 frontend `Fixed` 3건의 **false Fixed 회귀**(H04·M01·SEC-005) + working tree 대량 오염(B07). 벤치마크(`BENCHMARK_REPORT`·`COMPETITOR_MATRIX` 5차)는 신규 기획 입력 **없음**(이미 반영) — QA 회귀 처리 중심.

| 갱신 | 산출물 |
|------|--------|
| v1 완료 기준 QA-B02 `[x]` 철회(working tree 재오염), v1.1 H04·M01 `[x]` 철회·SEC-005 항목 신설 | `ROADMAP.md` |
| `## QA 피드백 반영` 7차 회귀 노트 + **이관 규율 6항(완료 단위 커밋·API 계약 변경 문서화 게이트)** 신설, QA→태스크 매핑 B06·B07·SEC-005, 변경 이력 | `ROADMAP.md` |
| `POST /clients` **`primaryGuardian` 필수 계약 명세화**(누락 시 400·단일 트랜잭션·`guardian_link_status=LINKED`) | `API_SPEC.md` §4 |
| §16 프론트엔드 구현 규약 **FE-5**(JWT 메모리 세션·localStorage 금지, SEC-005) | `USER_STORIES.md` |
| 결정 45(dirty-tree·계약 문서화 게이트 + createClient 보호자 계약 확정), `### QA 피드백 반영 7차` 표 | `PLAN_NOTES.md` |
| 7차 동기화 기록 | `decisions.md` 최상단 |
| Open 5건(B06·B07·H04·M01·SEC-005) → **Planned 이동** | `QA_FEEDBACK.md` |

**B06 범위 판정**: TSR가 「본 작업이 v1 P1(보호자 연결) 범위인지 확정·계약 변경 명세화 요청」 → **확정**. 이용자–보호자 연결 필수는 **결정 19·US-D01(v1 Must, 범위 #3)**로 이미 기획됨 — 신규 스토리 불필요, 누락된 **API 계약(`primaryGuardian`)만 API_SPEC §4에 명세화**. ERD `guardian_link_status`(V39)·V39 트리거는 기존 반영.  
**미변경**: REQUIREMENTS·FLOWCHART(US-D01·보호자 연결 이미 반영), DB 제약(V1–V39), 청구 2단계·QR B·platform_admin·MVP 제외.  
**미해결 추적**: #27(공단 엑셀 실컬럼·G7), #31(가격 tier), #32(다지점 HQ 사례), #33(보호자 초대 채널), #35(duration_band 표준시간) — 파일럿 입력 대기.

### [PLN] 자동 기획 동기화 — 6차 (2026-06-06)

사용자 대화 없이 `build --role planner` 실행. **핵심 입력은 TSR 재검증 결과**(`QA_FEEDBACK.md` 2026-06-06T07:52) — 5차에서 `Fixed`로 옮긴 backend 산출물이 develop HEAD에 미반영(test working tree·stash 한정)임이 확인되어 **Open 복귀**(false Fixed). 벤치마크(`BENCHMARK_REPORT`·`COMPETITOR_MATRIX` 4차)는 5차 이후 **신규 입력 없음** — 기획 변경 없음.

| 갱신 | 산출물 |
|------|--------|
| v1 완료 기준 QA-H01 `[x]` **철회**(develop 미반영 false Fixed) | `ROADMAP.md` |
| `## QA 피드백 반영`에 6차 회귀 처리 노트 + **이관 규율 5항(검증 게이트)** 신설 | `ROADMAP.md` |
| 변경 이력 6차 항목, 메타 owner COD→PLN 복원 | `ROADMAP.md` |
| backend Open 4건(B01·B02·H01·H02) → **Planned 재이동**(planned 매핑·정정) | `QA_FEEDBACK.md` |
| 결정 44(Fixed↔develop HEAD `git show` 검증 게이트), `### QA 피드백 반영 6차` 표 | `PLAN_NOTES.md` |
| 6차 동기화 기록 | `decisions.md` 최상단 |

**미변경**: USER_STORIES §16(FE-1~4)·US-G04(QA-H01)·G9 duration_band는 5차에 이미 반영 — backend Open 항목은 기존 태스크로 커버되어 신규 스토리 불필요. REQUIREMENTS·API_SPEC·FLOWCHART 변경 없음.  
**미해결 추적**: #27(공단 엑셀 실컬럼·G7), #31(가격 tier), #32(다지점 HQ 사례), #35(duration_band 표준시간) — 파일럿 입력 대기.

### [PLN] 자동 기획 동기화 — 5차 (2026-06-06)

사용자 대화 없이 `build --role planner` 실행. **이번 동기화의 핵심 입력은 신규 작성된 `TEST_REPORT.md`·QA_FEEDBACK Open 10건** — 이전 4차까지 QA Open 0건이었으나 tester 첫 이관 검증에서 BLOCK 5·HIGH 4·MEDIUM 1 발생.

| 갱신 | 산출물 |
|------|--------|
| `## QA 피드백 반영` 신설 — QA→태스크 매핑·이관 규율 4항 | `ROADMAP.md` |
| v1 완료 기준 — QA-H01 파서 테스트·QA-H02 SEC develop 커밋·QA-B01/B02 + G9 1밴드 노트 | `ROADMAP.md` |
| v1.1 완료 기준 — QA-H03/H04/M01·선행 게이트(B05)·ready 규율(B03/B04) | `ROADMAP.md` |
| US-G04 `처리상태` 선행열 샘플 테스트, US-G00a G9 duration_band, §16 프론트 구현 규약(FE-1~4) | `USER_STORIES.md` |
| 결정 41(이관 규율)·42(수가 1밴드→다밴드)·43(프론트 실 API), QA 피드백 반영 5차 표, 추가질문 #35 | `PLAN_NOTES.md` |
| Open 10건 → **Planned** 이동 + planner 매핑 주석 | `QA_FEEDBACK.md` |
| ROADMAP/USER_STORIES/PLAN_NOTES 메타 owner=PLN 정렬 | (메타) |

**4차 벤치마크 반영**: G9(수가 등급×시간대 2차원) — v1 1밴드·v1.1 다밴드(결정 42, #35); G10(가격 tier)·EZCARE G8은 기존 반영 유지(#31, 결정 38).  
**차별화 유지**: platform_admin, HQ, QR B, MVP 집중.  
**미해결 추적**: #27(공단 엑셀 실컬럼·G7), #31(가격 tier), #32(다지점 HQ 사례), #35(duration_band 표준시간) — 파일럿 입력 대기.

### [PLN] 벤치마크 3차 동기화 (2026-06-06)

`benchmark_researcher` 3차 재검증(`BENCHMARK_REPORT.md`·`COMPETITOR_MATRIX.md` 3차, `memory/decisions.md` 2026-06-06 최상단)을 기획 문서에 반영.

| 문서 | 갱신 내용 |
|------|----------|
| `ROADMAP.md` | v1 P0 `처리상태` 파서·롱텀2026 Chrome/Edge 완료 기준; v1.1 G8(초대·명세); v2 엔젤 CMS TCO |
| `REQUIREMENTS.md` | §1-5 3차 조사·EZCARE·9,210·롱텀2026; §1-5-1 G8; §3-7·§3-9 파서·브라우저 안내 |
| `USER_STORIES.md` | US-G04 `처리상태`·롱텀 안내; Epic J US-J01·J02 (v1.1 G8); §15 갭 G8 |
| `API_SPEC.md` | §7-4 엑셀 파서 정규화·롱텀2026 UI 안내 |
| `FLOWCHART.md` | §7-1 `처리상태` 분기; §9-1 보호자 초대·명세 (v1.1) |

**차별화 유지**: platform_admin, HQ, QR B, MVP 집중.  
**즉시 검증(G7)**: 파일럿 센터 NHIS 엑셀 샘플 + `처리상태` 포함 여부 (#27).

### [PLN] 자동 기획 동기화 — 4차 (2026-06-06)

사용자 대화 없이 `build --role planner` 실행. QA Open **0건**, TEST_REPORT 미작성 — Planned 이동 없음. 벤치마크 **3차** 신규 입력(G8·처리상태·롱텀2026·CMS TCO) 반영 완료.

### [PLN] 벤치마크 2차 동기화 (2026-06-06)

`benchmark_researcher` 산출물(`BENCHMARK_REPORT.md`, `COMPETITOR_MATRIX.md`) 및 `memory/decisions.md` 2026-06-06 결정을 기획 문서에 반영.

| 문서 | 갱신 내용 |
|------|----------|
| `ROADMAP.md` | v1 P0–P3·NHIS reconciliation 완료 기준, v1.1 보호자·v2 CMS·v3 갭 매핑 |
| `REQUIREMENTS.md` | §1-5-1 갭·차별화, §6-2 P0–P3 (기반 반영 완료) |
| `USER_STORIES.md` | US-G06 reconciliation, §14 갭 로드맵 (기반 반영 완료) |
| `API_SPEC.md` | §7-3 status 필터, §7-4 NHIS reconciliation 엔드포인트 |
| `FLOWCHART.md` | §7-1 NHIS reconciliation 흐름도 |

**차별화 유지**: `platform_admin` 개통, 다지점 HQ, QR B, MVP 집중.  
**즉시 검증 필요(G7)**: 공단 엑셀 실컬럼 — 파일럿 센터 샘플 확보(추가질문 #27).

### [PLN] 자동 기획 동기화 — 3차 (2026-06-06)

사용자 대화 없이 `build --role planner`로 실행. 입력 문서(QA_FEEDBACK·TEST_REPORT·BENCHMARK·COMPETITOR_MATRIX·decisions) 재확인 결과 **신규 기획 변경 사항 없음** — 기록·정합성 정렬만 수행.

| 점검 | 결과 | 조치 |
|------|------|------|
| `QA_FEEDBACK.md` Open | **0건** | ROADMAP/USER_STORIES/PLAN_NOTES 신규 Planned 없음 |
| `TEST_REPORT.md` | **미작성** (test 브랜치 검증 전) | 작성 시 다음 동기화에서 반영 |
| BENCHMARK·COMPETITOR_MATRIX | 2026-06-06 2차 조사 **이미 반영** (결정 29–35) | 변경 없음 |
| 문서 식별자 | planner 문서가 구 `PLA`/`coder,tester` 메타 사용 — `agents.yaml` 정본은 `PLN`/role-code (BNK는 이미 마이그레이션) | **ROADMAP·PLAN_NOTES·FLOWCHART·API_SPEC·REQUIREMENTS·USER_STORIES 메타를 `doc:owner=PLN doc:audience=COD,TSR,UXD,DBA,BNK,TWR`로 정렬**, PLAN_NOTES 섹션 `[PLA]→[PLN]` |

**미해결(추적 유지)**: 추가질문 #27(공단 엑셀 실컬럼·G7), #31(가격 tier), #32(다지점 HQ 경쟁사 사례). 신규 입력 없어 변동 없음.

---

## 제안: 벤치마킹 에이전트 (`benchmark_researcher`)

| 항목 | 내용 |
|------|------|
| 역할 | Competitive Research / Benchmark Analyst |
| 목적 | 국내외 주간보호·요양기관 관리 웹/앱의 기능·UX·가격·차별점을 조사해 기획·설계에 반영 |
| 주요 산출물 | `docs/planning/research/BENCHMARK_REPORT.md`, `docs/planning/research/COMPETITOR_MATRIX.md`, `memory/decisions.md` (벤치마킹 기반 결정) |
| 협업 시점 | Phase 1(기획) 선행 또는 병행 — REQUIREMENTS·USER_STORIES·DESIGN_SYSTEM 작성 전 |
| 조사 관점 | 핵심 기능 커버리지, 보호자 포털 UX, 출석·건강 기록 흐름, 알림 연동, 청구/급여 모듈, 접근성·모바일 UX |

> **참고**: `benchmark_researcher` 에이전트가 `docs/planning/research/BENCHMARK_REPORT.md`, `docs/planning/research/COMPETITOR_MATRIX.md` 를 유지하고, planner(build --role planner)가 이를 읽어 기획을 갱신한다. 3시간 loop: `./scripts/agent_planning_start.sh`

---

### DB 설계 질문 (db_architect, 2026-06-05)

V1–V17 커버리지 점검 중 식별한, **DB로 강제하지 않고 애플리케이션/테스트에 위임**하기로 결정한 항목. 정책 확정 시 제약 추가 검토.

1. **`users.active_branch_id` ∈ `user_branches`** — 현재 V8은 활성 지점이 동일 Tenant인지만 FK로 보장한다. "사용자가 실제 배정받은 지점만 활성화" 규칙은 DB로 강제하지 않았다. 사유: `hq_admin`이 `user_branches` 행 없이 전 지점 활성화하는 운영 모델(전 지점 묵시적 접근)인지, 명시적 배정 모델인지 미확정. **coder는 `POST /auth/active-branch`에서 토큰 `branch_ids` 내 값만 허용**하도록 검증. 명시적 배정 모델로 확정되면 `(user_id, active_branch_id) → user_branches` 복합 FK 추가.
2. **`billing_claim_items` 라인 산술 ↔ 스냅샷 비율** — V6은 행 단위 `total = nhis + copay`만 보장한다. `copay_amount = round(total_amount × copay_rate_snapshot)`, `total_amount = daily_rate_snapshot × attendance_days`의 정확한 반올림은 CHECK로 강제하지 않았다(반올림 규칙 충돌 위험). **coder는 청구 계산 서비스에서 단일 반올림 규칙(예: `RoundingMode.HALF_UP`, 원 단위)을 적용하고 tester가 회귀 테스트로 검증**. 확정 반올림 규칙은 §3-9-2 보강 시 문서화.
3. **`nhis_import_rows` 매칭 이용자의 지점 일치** (2026-06-06, V21 마감) — V21 `trg_nhis_rows_client_branch`로 `client_id` 설정 시 `clients.branch_id = nhis_import_batches.branch_id`를 DB에서 강제한다. V21 `trg_nhis_batches_claim_branch`로 배치↔청구 연결 시 지점도 일치. **가정**: ogada는 지점 단위 import·reconciliation(파일럿 2지점). 공단 엑셀이 **법인(Tenant) 단위 일괄**로 확정되면 V21 #4 트리거 완화 또는 `branch_id` 비정규화 검토(추가질문 27).
4. **`nhis_import_rows.organization_id` 자동 복사** (2026-06-06, V22) — V22 `trg_nhis_import_rows_set_org`가 부모 배치에서 Tenant를 자동 설정(V21 청구 라인 패턴). 앱은 여전히 명시 설정 권장.
5. **`guardian_clients.organization_id` 자동 복사** (2026-06-06, V23) — V23 `trg_guardian_clients_set_org`가 연결 `clients`에서 Tenant 자동 설정. 보호자 연결 INSERT 시 앱이 `organization_id`를 생략해도 FK·QR 스캔 Tenant 검증과 정합.
6. **청구 라인 출석일·금액 쌍 CHECK** (2026-06-06, V24) — V23 `chk_billing_claim_items_positive_days`(`total > 0 → days ≥ 1`)와 V24 `chk_billing_claim_items_days_implies_amount`(`days ≥ 1 → total > 0`)로 DB 레벨 쌍방 방어. 반올림·산술 정확성은 여전히 앱·테ster 책임(항목 2).
7. **NHIS import `ltc_cert_no` 공백 CHECK** (2026-06-06, V25) — V25 `chk_nhis_import_rows_ltc_cert_nonempty`가 NULL·공백 문자열 행을 DB에서 거부. 엑셀 파서는 앱에서 빈 행 skip 권장.
8. **`billing_claim_items` 청구서당 1라인 UK** (2026-06-06, V26) — V26 `uq_billing_claim_items_claim_client`가 `(claim_id, client_id)` 중복을 DB에서 거부. `BillingService.generateClaim`은 이용자당 1행만 생성하며, NHIS reconciliation의 `findByClaimIdAndClientId` 전제와 일치. 수동 SQL·버그로 인한 중복 라인 방어.
9. **V2 중복 UK 정리** (2026-06-06, V27) — V2 `uq_claim_item_client`와 V26 `uq_billing_claim_items_claim_client`가 동일 컬럼 UK. V27에서 V2 이름 제거, V26 이름만 유지.
10. **cross-tenant 이메일 로그인 인덱스** (2026-06-06, V28) — `idx_users_email_lower`가 `findAllByEmailIgnoreCase`를 지원. 동일 이메일 다중 Tenant 계정은 **앱에서 거부**(`AuthService` BusinessRuleException) — DB UK는 `(organization_id, email)` Tenant 스코프만. 전역 이메일 UK는 SaaS 다 Tenant 동일 이메일 정책 미확정으로 DB 강제하지 않음.
11. **NHIS 배치 행 정렬 인덱스** (2026-06-06, V28) — `idx_nhis_import_rows_batch_created`가 import 응답 행 순서를 지원. `(batch_id, ltc_cert_no)` UK는 엑셀 중복 행 허용을 위해 추가하지 않음 — reconciliation UI는 앱에서 중복 표시.
12. **user_branches user_id 역조회** (2026-06-06, V29) — `idx_user_branches_user_id`가 `findByUserId`/`findByUserIdIn`을 지원. V25 `(branch_id, user_id)`는 `GET /users?branchId=` 지점 필터 전용.
13. **플랫폼 사업자번호 검색** (2026-06-06, V29) — `idx_organizations_business_no_trgm`이 `businessNoContainingIgnoreCase`를 지원. exact match는 `organizations.business_no` UK(V1).
14. **청구 라인 claim_id 정렬** (2026-06-06, V29) — `idx_billing_claim_items_claim_created`가 `findByClaimIdOrderByCreatedAtAsc`를 지원. V2 `idx_billing_claim_items_claim` 대체; Tenant 스코프 조회는 V27 `(organization_id, claim_id, created_at)` 병행.
15. **Tenant 이메일 case-insensitive UK** (2026-06-06, V30) — V30 `uq_users_org_email_lower`가 `(organization_id, lower(email))` UK로 V1 case-sensitive `uq_user_email_per_org`를 대체. **coder는 `users.email` 저장 시 trim+소문자 정규화 권장** — DB UK와 앱 `existsByOrganizationIdAndEmailIgnoreCase` 정합. cross-tenant 로그인은 V28 `idx_users_email_lower` + 앱 단일 active 계정 검증 유지.
16. **비밀번호 변경 refresh 폐기** (2026-06-06, V30) — V30 `idx_refresh_tokens_user_active`가 `(user_id) WHERE revoked_at IS NULL` partial 인덱스. **`AuthService.resetPassword`가 `RefreshTokenRepository.revokeAllActiveForUser` 호출** — V30 인덱스 활용(2026-06-07 round 42 재확인). password_reset_tokens는 V28 `idx_password_reset_tokens_user_active` 기존 패턴.
17. **청구 목록 status 필터 인덱스** (2026-06-06, V31) — V31 `idx_billing_claims_org_branch_status_generated`가 `(organization_id, branch_id, status, generated_at DESC)` 지원. API_SPEC §7-3 상태 필터는 **coder가 `BillingClaimRepository`·`BillingService.listClaims`에 status 쿼리 파라미터 추가** 시 활용.
18. **청구 상태 이력 no-op CHECK** (2026-06-06, V31) — V31 `chk_claim_status_history_distinct_transition`이 `from_status = to_status` 이력 INSERT를 DB에서 거부. `trg_billing_claims_status_history`(V10/V21)는 실제 전이만 적재하므로 기존 데이터 무영향.
19. **대표 보호자 partial 인덱스** (2026-06-06, V31) — V31 `idx_guardian_clients_org_client_primary`가 `clearPrimaryForClient` UPDATE 스캔 지원. UK `uq_guardian_clients_primary`(V7)와 병행.
20. **`attendance.created_by` 미설정** (2026-06-06, V31 점검 → **V32 마감**) — V32 `trg_attendance_set_created_by`가 `ogada.actor_user_id` 세션 변수로 INSERT 시 `created_by` 자동 적재. **coder는** `AttendanceService` check-in/absence/QR 트랜잭션에서 `DbSessionContext.setActorUserId` 호출(청구 status PATCH와 동일). DB NOT NULL CHECK는 세션 미설정 legacy 행 허용을 위해 보류.
21. **`billing_claims.generated_by` 미설정** (2026-06-06, V32) — V32 `trg_billing_claims_set_generated_by`가 session actor로 INSERT 시 자동 적재. **coder는** `BillingService.generateClaim`에서 `dbSessionContext.setActorUserId` 호출 권장.
22. **NHIS COMPLETED `imported_at` backstop** (2026-06-06, V32) — V32 `trg_nhis_batches_set_imported_at`가 COMPLETED + NULL `imported_at` 시 `created_at`/NOW() 설정. JPA `@PrePersist`와 병행; raw SQL 방어.
23. **퇴소 purge 인덱스** (2026-06-06, V32) — `idx_clients_org_discharged_at` partial 인덱스. retention 배치 구현 시 Tenant 스코프 cutoff 쿼리 활용.
24. **건강·NHIS actor backstop** (2026-06-06, V33) — V33 `trg_health_records_set_recorded_by`·`trg_nhis_batches_set_imported_by`가 session `ogada.actor_user_id`로 NULL actor 컬럼 자동 적재. `HealthRecordService`·`NhisImportService`는 앱에서 JWT subject 설정하나 V32 출석 패턴과 동일하게 DB 방어. **coder는** `DbSessionContext.setActorUserId`를 출석·청구·건강·NHIS 쓰기 트랜잭션 공통 호출 권장.
25. **퇴소 child purge 인덱스** (2026-06-06, V33) — V33 `idx_attendance_client_purge`·`idx_health_records_client_purge`·`idx_billing_claim_items_client_purge`가 `client_id IN (discharged cohort)` bulk DELETE/익명화 스캔 지원 (DATA_RETENTION §4-1).
26. **활성 이용자 목록 pagination** (2026-06-06, V33) — V33 `idx_clients_org_branch_active_created` partial 인덱스. `ClientRepository.searchByScope` query=null 시 branch+active 필터 + created_at 정렬.
27. **이용자 생애주기 정합 + 지점 단위 retention purge** (2026-06-06, V34) — V5 `chk_clients_discharge_active`(`discharged_at IS NULL OR is_active = FALSE`)와 V34 `chk_clients_discharged_after_created`(`discharged_at >= created_at`)가 쌍을 이뤄 `clients.is_active` ↔ `discharged_at` 양방향 무결성을 완성한다. `ClientService.discharge()`는 두 컬럼을 동시 적재(`setActive(false) + setDischargedAt(NOW())`)하므로 항상 통과. **coder가 추후** 일괄 reactivation·backfill 스크립트를 추가하면 CHECK가 1차 방어. 또한 V34 `idx_clients_org_branch_discharged_at` partial 인덱스가 지점 단위 retention purge(지점 폐쇄·부분 Tenant rollback) 시 cohort 선정 비용을 낮춤 — Tenant 스코프(V32 `idx_clients_org_discharged_at`)와 병행.
28. **이용자·청구 시간 정합 완성** (2026-06-06, V36) — V36이 Must 엔티티 시간 단조성 패턴을 완성한다.
    - `chk_clients_consent_after_created`(`consent_collected_at >= created_at`) — 2단계 동의 수집(생성 시 NULL → `collectConsent`에서 NOW())이므로 항상 충족. PII 이관·raw SQL backfill 시 backdated consent를 DB가 거부.
    - `chk_clients_ltc_cert_valid_from_after_birth`(`ltc_cert_valid_from >= birth_date`) — 장기요양 인정서는 출생 이후 발급. 입력 typo(예: 1945-03-02 출생 / 1945-03-01 인정)·잘못된 import 데이터 차단. `ltc_cert_valid_from` nullable 유지(2단계 등록).
    - `chk_billing_claims_generated_after_created`(`generated_at >= created_at`) — `BillingService.generateClaim`은 `setGeneratedAt(now())` 적재로 항상 충족. raw SQL 직접 UPDATE·이력 backdate 거부. V8 status 단방향 트리거(DRAFT→CONFIRMED→PAID)와 결합해 청구 audit timeline 단조성 보장.
    - **시간 정합 패턴 완성도**: V12 backup_runs / V13 토큰 expires / V20 NHIS imported / V34 clients discharged / **V36 clients consent·ltc·billing generated** — Must 엔티티 핵심 `*_at` 컬럼은 모두 `created_at`/`birth_date` 대비 단조성을 DB에서 강제.
    - **coder 영향 없음** — 기존 서비스 흐름(2단계 등록, NHIS import, billing 생성)은 모두 V36 CHECK를 항상 충족하며, 마이그레이션은 backfill 없이 적용된다.
29. **Must 엔티티 row lifecycle·NHIS reconciliation** (2026-06-06, V37) — V36 `*_at >= created_at` INSERT/생성 시각 정합에 이어 UPDATE 경로를 DB에서 보완.
    - `chk_attendance_updated_after_created`·`chk_attendance_checkin_after_created` — 체크아웃 UPDATE·체크인 INSERT는 `AttendanceService`가 `now()` 적재로 항상 충족.
    - `chk_clients_updated_after_created` — PATCH/discharge/consent UPDATE.
    - `chk_billing_claims_updated_after_created` — V36 `generated_at` CHECK와 쌍; status PATCH UPDATE.
    - `uq_nhis_import_rows_org_id` — `findByIdAndOrganizationId` Tenant 앵커 (`PATCH .../rows/{rowId}/match`).
    - `idx_nhis_import_batches_org_branch_claim_created` — `findScopedBatches` claimId+branch 필터.
    - **coder 영향 없음** — 기존 JPA 흐름은 V37 CHECK를 항상 충족.
30. **NHIS 배치 지점 목록 인덱스** (2026-06-06, V38) — V38 `idx_nhis_import_batches_org_branch_created`가 `GET /billing/imports/nhis?branchId=`(yearMonth·claimId 없음) 지점 전체 import 이력 최신순을 지원. V27 `(org, branch, year_month, created_at)`·V37 partial `(org, branch, claim_id, created_at)` 보완. **coder 영향 없음** — `NhisImportBatchRepository.findScopedBatches` 기존 쿼리가 인덱스 활용.
31. **ERD↔마이그레이션↔API_SPEC↔repository 전수 대조 (2026-06-06, V39 기준)** — DBA가 21개 `*Repository`의 모든 쿼리 메서드·API_SPEC §1–§9 엔드포인트·Must 엔티티(billing·attendance·clients·health·guardians·audit)를 V1–V39 스키마와 대조. **신규 누락 테이블/인덱스/제약 없음**으로 확인 — 신규 마이그레이션 미생성(불필요한 V40 회피, rules.md §2/§8).
    - **청구 단일성**: `billing_claims (organization_id, branch_id, year_month)` **UK** `uq_claim_branch_month`(V1) — `BillingClaimRepository.findByOrganizationIdAndBranchIdAndYearMonth`의 `Optional` 단일 반환 보장(중복 청구 차단).
    - **as-of 수가/본인부담**: `findEffectiveForGrade`/`findEffectiveByType` → V23 `(org, ltc_grade, effective_from DESC)`·`(org, copay_type, effective_from DESC)`; 현행 단일은 V7 partial UK + EXCLUDE 비중첩.
    - **NHIS 후보 검색**: `searchMatchCandidates` → `ClientRepository.searchByScope`(V33 partial + V12/V26 trigram). 행 매칭 `findByIdAndOrganizationId` → V37 `uq_nhis_import_rows_org_id`.
    - **출석 집계/프로필 탭**: `AttendanceRepository` 6개 count/list 메서드 모두 V22/V24/V25/V26 partial·복합 인덱스로 커버.
    - **ERD 문서 동기화만 보완**: V39 `idx_clients_guardian_link_pending`·`guardian_link_status`/`trg_guardian_clients_refresh_link_status`가 §6 인덱스표·§7 상세 서브섹션에 누락 → §6 행 추가·**§7-34 신설**(다른 버전과 형식 정합). 스키마 변경 없음.
32. **지점명 case-insensitive UK 누락 (2026-06-06, V40)** — V39 전수 대조(#31) 이후 `BranchRepository`·`BranchService` 재점검에서 **앱 의도 ↔ DB 보장 불일치** 1건 식별. `BranchService.create`는 `existsByOrganizationIdAndNameIgnoreCase`, `update`는 `existsByOrganizationIdAndNameIgnoreCaseAndIdNot`로 지점명 중복을 **대소문자 무시**로 거부하나, V1 `uq_branch_name_per_org UNIQUE (organization_id, name)`는 **case-sensitive**다. → 동시 요청으로 「Happy」·「happy」가 둘 다 앱 검증을 통과해 양쪽 INSERT될 수 있는 race window 존재(case-sensitive UK가 구별).
    - **V40 조치**: `uq_branch_name_per_org` DROP 후 functional UK `uq_branches_org_name_lower (organization_id, lower(name))` 생성 — **V30 `uq_users_org_email_lower`(이메일) 패턴의 지점명 대칭**. `branches.organization_id` NOT NULL이라 partial 술어 불필요(V30은 `platform_admin` 위해 partial).
    - **기존 데이터 무영향**: 앱이 항상 대소문자 무시 중복을 거부해왔으므로 거부될 case-variant 지점명 없음. `BranchService`가 `name.trim()` 적용(이미)이라 공백·대소문자 정규화가 앱·DB 정합.
    - **coder 영향 없음** — 기존 `BranchService` 흐름은 V40 UK를 항상 충족. ERD §6 인덱스표·§7-35 신설·§7 마이그레이션표(V40 행) 동기화.
33. **V40 기준 전수 재대조 — 신규 누락 0건 (2026-06-06, round 33)** — V40 적용 후 DBA가 21개 `*Repository`의 전 쿼리 메서드·API_SPEC §1–§9 엔드포인트·Must 엔티티(billing·attendance·clients·health·guardians·audit)를 V1–V40 스키마(인덱스·제약·트리거)와 다시 1:1 대조. **신규 누락 테이블/인덱스/제약 없음** — 불필요한 V41 미생성(rules.md §2/§8).
    - **billing 커버리지**: `BillingClaimRepository`(`findByOrganizationIdAndBranchIdAndYearMonth`→UK `uq_claim_branch_month` V1; `…AndStatusOrderByGeneratedAtDesc`→`idx_billing_claims_org_branch_status_generated` V31; `…OrderByGeneratedAtDesc`→V22)·`BillingClaimItemRepository`(`findByClaimIdOrderByCreatedAtAsc`→V29; `findByClaimIdAndClientId`→UK V26; `findByOrganizationIdAndClientIdOrderByCreatedAtDesc`→V25)·`FeeScheduleRepository`/`CopayRateRepository` as-of(`findEffective*`→V23 `(org, grade/type, effective_from DESC)` + V7 EXCLUDE)·`NhisImport*`(`findScopedBatches`→V27/V37/V38; `findByIdAndOrganizationId`→UK `uq_nhis_import_rows_org_id` V37) **전부 인덱스 매핑**.
    - **attendance 커버리지**: 출석 집계 6개(`countBy…CheckInAtIsNotNull` 일/월별·`…CheckOutAtIsNotNull`·`…AbsenceReasonIsNotNull`)→V22 partial; 당일 목록(`…AttendanceDateOrderByCreatedAtDesc`)→V23; 프로필·체크인 단건(`findTopBy…`)→V24; 이용자 출석 탭(`…ClientIdOrderByAttendanceDateDesc…`·`…AttendanceDateBetween…`)→V24 `(org, client, attendance_date DESC)`. XOR·달력일·시간 정합 CHECK(V4/V11/V14/V15/V37) 유지.
    - **나머지 도메인**: `HealthRecordRepository`(프로필 V24·지점/HQ alerts V23 branchId IN)·`GuardianClientRepository`(연결·대표 V23/V24/V31)·`UserRepository`/`UserBranchRepository`(이메일 UK V30·`idx_users_email_lower` V28·user_branches V29/V25)·`BranchRepository`(case-insensitive UK V40)·`OrganizationRepository`(name/business_no trigram V27/V29·backup partial V28)·토큰·로그인·백업(V2/V6/V9/V13/V14/V15/V16/V28/V30) 모두 커버.
    - **결론**: ERD §6/§7·DATA_RETENTION §8 구현 메모와 repository 쿼리가 V40 시점 정합. 추가 마이그레이션·문서 변경 불필요(본 검증 기록만 추가).
34. **V40 기준 전수 재대조 — 신규 누락 0건 (2026-06-06, round 34, backend `fac3d07` 반영)** — backend `fac3d07`(guardian billing API·NHIS import guidance·7-role RBAC tests) 커밋 직후 DBA가 변경된 도메인(guardian portal billing·NHIS guidance)을 V1–V40 스키마와 1:1 재대조. **신규 누락 테이블/인덱스/제약 없음** — V41 미생성(rules.md §2/§8, round 33 패턴).
    - **`GET /guardian/clients/{clientId}/billing`** (`BillingService.listClientBillingHistoryForPortal` + `GuardianPortalService.getClientBillingHistory`): ① `ClientRepository.findByIdAndOrganizationIdAndActiveTrue` → V33 `idx_clients_org_branch_active_created` partial(active 분기) + Tenant PK. ② `GuardianClientRepository.existsByOrganizationIdAndGuardianUserIdAndClientId` → V25 `idx_guardian_clients_org_guardian_client`. `client_user` 분기는 `clients.user_id` 1:1 매칭(V23 `idx_clients_org_user`). ③ `BillingClaimItemRepository.findByOrganizationIdAndClientIdOrderByCreatedAtDesc` → V25 `idx_billing_claim_items_org_client_created`(직원 이용자 청구 탭과 **동일** 인덱스 재사용). ④ `BillingClaimRepository.findAllById(claimIds)` + post-filter `organizationId.equals(...)` → PK + V8 `uq_billing_claims_org_id` Tenant 앵커. post-filter는 데이터 정합 방어(V21 `trg_billing_claim_items_set_org`·V16 Tenant FK가 이미 정합 보장하나, raw SQL backfill 등 비정상 경로 대비). **coder 개선 후보(선택)**: `BillingClaimRepository.findByIdInAndOrganizationId(Set<UUID>, UUID)`로 단일 쿼리화 시 V8 UK 활용 가능 — 성능 차이 미미하므로 DB 변경 불필요, repository 시그니처만 추가하면 됨.
    - **`GET /billing/imports/nhis/guidance`** (`BillingController.nhisImportGuidance`·`NhisImportGuidance.toResponse`): 정적 응답(롱텀 2026 Chrome/Edge 안내·온보딩 텍스트) — **DB 미사용, 스키마 영향 없음**.
    - **7-role RBAC tests** (`RoleBasedControllerAccessTest`·`GuardianPortalServiceTest`·`AuthServiceTest`·`NhisImportGuidanceTest`): 컨트롤러 접근 제어·서비스 단위 테스트 — DB 스키마 영향 없음.
    - **ERD §8 API↔테이블 매핑 보강**: `GET /guardian/clients/{clientId}/billing`(V25 인덱스 재사용 주석)·`GET /billing/imports/nhis/guidance`(정적 응답) 2행 추가. **DATA_RETENTION §8** 구현 메모에 보호자 포털 청구 탭 인덱스 매핑 1행 추가. 신규 마이그레이션·CHECK·트리거 없음.
35. **보호자 초대 테이블(`guardian_invitations`) 설계 — API_SPEC 계약 확정까지 보류** (2026-06-06, round 34, COD-Q J01) — `### [COD] 보호자 초대 API 계약 확인`에서 frontend(`ClientDetailPage`)가 `POST /api/v1/guardians/invitations`를 호출하나, **API_SPEC에 엔드포인트·요청 스키마·이메일/SMS 채널·만료 정책 미명시**(US-J01, v1.1, 추가질문 #33). DBA는 채널·만료 정책 확정 전 테이블을 설계하지 않는다(rules.md §1 자율 실행 — 불확실 항목은 보류).
    - **확정 대기 항목**: ① 초대 채널(이메일 링크 vs SMS 코드 vs 둘 다), ② 토큰 만료(7일 권장), ③ 1회용 vs 재발급, ④ 초대 발신자(`branch_admin`/`social_worker`) actor 기록, ⑤ 거절·만료 상태 추적.
    - **설계 가설(API_SPEC 확정 시)**: `guardian_invitations`(`id`·`organization_id` FK·`client_id` FK·`invited_by` FK→`users`·`channel` ENUM(`email`|`sms`)·`recipient_contact_encrypted`·`token_hash` UK·`expires_at`·`accepted_at` nullable·`accepted_user_id` FK→`users` nullable·`revoked_at` nullable·`created_at`). 인덱스: `(organization_id, client_id, created_at DESC)` + partial `(token_hash) WHERE accepted_at IS NULL AND revoked_at IS NULL AND expires_at > NOW()`. retention: 만료/사용 후 30일 purge(기존 토큰 패턴 V14/V15 재사용).
    - **현재 frontend graceful fallback**: 404/501 시 「백엔드 미구현」 안내 — DB 미생성 상태에서 충돌 없음. PLN가 API_SPEC §5 추가 시 DBA가 즉시 마이그레이션 작성.
36. **V40 기준 전수 재대조 — 신규 누락 0건 (2026-06-06, round 36, backend `fac3d07` HEAD 불변)** — 신규 DBA 호출. backend HEAD는 여전히 `fac3d07`(round 34 대조 시점과 동일)이고 working tree 변경은 `RoleBasedControllerAccessTest.java`(B02 recurrence, **테스트 전용 — DB 영향 없음**)뿐이다. 21개 `*Repository` 전 쿼리 메서드를 V1–V40 스키마(인덱스·제약·트리거)와 다시 1:1 대조 — **신규 누락 테이블/인덱스/제약 없음**. 불필요한 V41 미생성(rules.md §2/§8, round 33/34 패턴 유지).
    - **마이그레이션 연속성**: `V1`–`V40` 40개 파일 contiguous(버전 갭·중복 0). `V2__attendance_add_attendance_date.sql` 충돌본은 삭제됨(ERD §7 주의 참고).
    - **billing**: `BillingClaimRepository`(`findByIdAndOrganizationId`→V10 `uq_billing_claims_org_id`; `findByOrganizationIdAndBranchIdAndYearMonth`→V1 UK `uq_claim_branch_month`; `…OrderByGeneratedAtDesc`→V22; `…AndStatusOrderByGeneratedAtDesc`→V31)·`BillingClaimItemRepository`(`findByClaimIdOrderByCreatedAtAsc`→V29; `findByClaimIdAndClientId`→V26 UK; `findByOrganizationIdAndClientIdOrderByCreatedAtDesc`→V25)·`FeeScheduleRepository`/`CopayRateRepository`(`findEffective*`·`findTop…EffectiveToIsNull`→V23 `(org, grade/type, effective_from DESC)` + V7 EXCLUDE + partial 현행 UK; 목록은 V27)·`NhisImport{Batch,Row}Repository`(`findScopedBatches`→V27/V37/V38; `findByIdAndOrganizationId`→V37/V8 UK; `findByBatchIdOrderByCreatedAtAsc`→V28) **전부 인덱스 매핑**.
    - **attendance**: 당일 목록·집계 6개·프로필/체크인 단건·이용자 출석 탭(`…ClientIdOrderByAttendanceDateDesc…`·`…AttendanceDateBetween…`)→V22 partial·V23·V24·V25/V26 — 누락 없음.
    - **나머지 도메인**: `ClientRepository`(`searchByScope`→V33 partial + V12/V26 trigram; `findByOrganizationIdAndBranchIdAndLtcCertNo`→V27; UK V4)·`GuardianClientRepository`(연결·대표·QR 대상→V23/V24/V25/V31)·`HealthRecordRepository`(프로필 V24·지점/HQ alerts V8/V23 `branchIdIn`)·`User`/`UserBranch`/`Branch`/`Organization`Repository(이메일 UK V30·`idx_users_email_lower` V28·user_branches V25/V29·지점명 UK V40·org trigram V27/V29)·토큰·로그인·백업·audit(JdbcClient, `idx_audit_logs_org_created`)·`OrganizationSettingsRepository`(`allow_client_self_checkin` 단건 조회) 모두 커버.
    - **`guardian_invitations` 여전히 보류**: API_SPEC 전수 grep(`invitation|invite|초대`) **0건** — round 35 가설 테이블은 PLN의 API_SPEC §5 초대 계약(채널·만료) 확정 전까지 미생성 유지. frontend graceful fallback 충돌 없음.
    - **Must 엔티티 커버리지**: agents.yaml `core_entities` 전부 충족 — `medications`는 `health_records.record_type='medication'`(ERD §4-5), `meal_records`·`activity_programs`는 v1 이후 Should 예약(ERD §5). 청구·출석 Must 핵심 제약·인덱스 완비.
    - **결론**: ERD(§6/§7·§8)·DATA_RETENTION(§8)·repository 쿼리가 V40·`fac3d07` 시점 정합. 추가 마이그레이션·문서 변경 불필요(본 검증 기록만 추가).
37. **V40 기준 전수 재대조 — 신규 누락 0건 (2026-06-06, round 37, backend `b5d70a8` HEAD)** — 신규 DBA 호출. backend HEAD가 round 34/36 대조 시점 `fac3d07` → **`b5d70a8`**로 1커밋 전진했으나, 변경분은 `RoleBasedControllerAccessTest` guardian/client_user RBAC WebMvcTest 확장(**QA-B02 recurrence Fixed, 테스트 전용 — DB 영향 없음**)뿐이다. 21개 `*Repository`(billing 6·attendance 1·clients/guardian 2·health 1·auth 3·users 2·org 2·settings 2·기타)의 전 쿼리 메서드를 V1–V40 스키마(인덱스·제약·트리거)와 다시 1:1 대조 — **신규 누락 테이블/인덱스/제약 없음**. 불필요한 V41 미생성(rules.md §2/§8, round 33/34/36 패턴 유지).
    - **마이그레이션 연속성**: `V1`–`V40` 40개 파일 contiguous(버전 갭·중복 0). `V2__attendance_add_attendance_date.sql` 충돌본 삭제 상태 유지(ERD §7 주의).
    - **billing Must 커버리지**: `BillingClaimRepository`(`findByIdAndOrganizationId`→V10 UK `uq_billing_claims_org_id`; `findByOrganizationIdAndBranchIdAndYearMonth`→V1 UK `uq_claim_branch_month` 단일 청구 보장; `…OrderByGeneratedAtDesc`→V22; `…AndStatusOrderByGeneratedAtDesc`→V31)·`BillingClaimItemRepository`(`findByClaimIdOrderByCreatedAtAsc`→V29; `findByClaimIdAndClientId`→V26 UK `(claim_id, client_id)`; `findByOrganizationIdAndClientIdOrderByCreatedAtDesc`→V25)·`FeeSchedule`/`CopayRate`(`findEffective*`→V23 `(org, grade/type, effective_from DESC)` + V7 EXCLUDE 비중첩)·`NhisImport{Batch,Row}`(`findScopedBatches`→V27/V37/V38; `findByIdAndOrganizationId`→V37 UK `uq_nhis_import_rows_org_id`) **전부 인덱스 매핑**.
    - **attendance Must 커버리지**: 당일 목록(`…AttendanceDateOrderByCreatedAtDesc`)→V23; 프로필/체크인 단건(`findTopBy…ClientIdAndAttendanceDate…`)→V24; 집계 — client-월 present(`countBy…ClientIdAndAttendanceDateBetweenAndCheckInAtIsNotNull`)→V26 partial, branch-일 present/checkout/absence→V22 partial 3종, branch-월 present(`countBy…AttendanceDateBetweenAndCheckInAtIsNotNull`)→V25 partial; 이용자 출석 탭(`…ClientIdOrderByAttendanceDateDescCreatedAtDesc`·`…AttendanceDateBetween…`)→V24 `(org, client, attendance_date DESC)`. XOR·달력일·시간 정합 CHECK(V4/V11/V14/V15/V37) 유지.
    - **guardian**: `findByOrganizationIdAndClientIdOrderByPrimaryGuardianDescCreatedAtAsc`→V24·`…GuardianUserIdOrderBy…`→V23·`exists/find…GuardianUserIdAndClientId`→V25·`countByOrganizationIdAndClientId`→V24 prefix·`clearPrimaryForClient`(UPDATE WHERE org+client+is_primary)→V31 partial `(org, client_id) WHERE is_primary`. 대표 보호자 1명 UK(V7)·link_status 트리거(V39) 유지.
    - **나머지 도메인**: `ClientRepository`(`searchByScope`→V33 partial + V12/V26 trigram; cert exact→V27; UK V4)·`HealthRecordRepository`(프로필 V24·지점/HQ alerts V8/V23)·`User`/`UserBranch`/`Branch`/`Organization`(이메일 UK V30·`idx_users_email_lower` V28·user_branches V25/V29·지점명 case-insensitive UK V40·org trigram V27/V29)·토큰·로그인·백업·audit·`OrganizationSettingsRepository` 모두 커버.
    - **`guardian_invitations` 여전히 보류**: API_SPEC 전수 grep(`invitation|invite|초대`) **0건**(재확인) — round 35 가설 테이블은 PLN의 API_SPEC §5 초대 계약(채널·만료) 확정 전까지 미생성. frontend graceful fallback 충돌 없음.
    - **Must 엔티티 커버리지**: agents.yaml `core_entities` 전부 충족 — `medications`는 `health_records.record_type='medication'`(ERD §4-5), `meal_records`·`activity_programs`는 v1 이후 Should 예약(ERD §5). 청구·출석 Must 핵심 제약·인덱스 완비.
    - **결론**: ERD(§6/§7·§8)·DATA_RETENTION(§8)·repository 쿼리가 V40·`b5d70a8` 시점 정합. 추가 마이그레이션·CHECK·트리거·문서 변경 불필요(본 검증 기록 + ERD 메타 timestamp 갱신만).
38. **V40 기준 전수 재대조 — 신규 누락 0건 (2026-06-06, round 38, backend `b5d70a8` HEAD 불변)** — 신규 DBA 호출. backend HEAD는 round 37과 동일 **`b5d70a8`**(guardian/client_user RBAC WebMvcTest, DB 영향 없음). working tree 변경은 테스트 파일뿐. 21개 `*Repository` 전 쿼리 메서드·API_SPEC §1–§9·agents.yaml `core_entities`(users·clients·guardians·attendance·health_records·medications→`health_records.record_type`·meal_records/activity_programs→v1 Should 예약·billing·audit_logs·notifications)를 V1–V40 스키마와 1:1 재대조 — **신규 누락 테이블/인덱스/제약 없음**. V41 미생성(rules.md §2/§8).
    - **마이그레이션 연속성**: V1–V40 40개 contiguous(갭·중복 0).
    - **Must billing**: `BillingClaimRepository`/`BillingClaimItemRepository`/`FeeScheduleRepository`/`CopayRateRepository`/`NhisImport{Batch,Row}Repository` — UK `uq_claim_branch_month`(V1)·`uq_billing_claim_items_claim_client`(V26)·`uq_billing_claims_org_id`(V10)·`uq_nhis_import_rows_org_id`(V37)·status+generated_at(V31)·NHIS batch 목록(V27/V37/V38) 전부 매핑.
    - **Must attendance**: 당일 목록(V23)·체크인 단건 `findTopBy…`(V24)·집계 6종(V22/V25/V26 partial)·프로필 탭(V24)·XOR·달력일·시간 정합(V4/V11/V14/V15/V37) 유지.
    - **Must guardians/clients**: `guardian_link_status`+트리거(V39)·대표 보호자 UK(V7)·partial(V31)·연결 검증(V25)·case-insensitive 지점명 UK(V40)·Tenant 이메일 UK(V30).
    - **`guardian_invitations` 보류 유지**: API_SPEC 초대 계약 0건 — round 35 가설 테이블은 PLN 확정 전 미생성.
    - **v1.2 P0(등급 이력·입금 미납)**: MVP Must 범위 외 — REQUIREMENTS §6-3·ROADMAP v1.2. `billing_claims.status` DRAFT/CONFIRMED/PAID는 MVP 충족; v1.2 Epic L/M는 API_SPEC·PLN 확정 후 별도 마이그레이션.
    - **결론**: ERD·DATA_RETENTION·repository가 V40·`b5d70a8` 시점 정합. 추가 마이그레이션·스키마 변경 불필요(본 검증 기록 + ERD 메타 timestamp 갱신만).
39. **V40 기준 전수 재대조 — 신규 누락 0건 (2026-06-06, round 39, backend `4274459` HEAD)** — 신규 DBA 호출. backend HEAD가 round 38(`b5d70a8`) → **`4274459`**로 1커밋 전진. 변경분은 `BillingControllerRoutingTest`·`NhisImportServiceTest`(지점 불일치 매칭 거부)·`RoleBasedControllerAccessTest`(guardian/client_user RBAC·billing routing) **테스트 전용** — repository·서비스 시그니처·스키마 영향 없음. 21개 `*Repository` 전 쿼리 메서드·API_SPEC §1–§9·agents.yaml `core_entities`를 V1–V40 스키마(인덱스·제약·트리거)와 1:1 재대조 — **신규 누락 테이블/인덱스/제약 없음**. V41 미생성(rules.md §2/§8).
    - **마이그레이션 연속성**: V1–V40 40개 contiguous(갭·중복 0).
    - **Must billing**: `BillingClaimRepository`/`BillingClaimItemRepository`/`FeeScheduleRepository`/`CopayRateRepository`/`NhisImport{Batch,Row}Repository` — UK `uq_claim_branch_month`(V1)·`uq_billing_claim_items_claim_client`(V26)·`uq_billing_claims_org_id`(V10)·`uq_nhis_import_rows_org_id`(V37)·status+generated_at(V31)·NHIS batch 목록(V27/V37/V38) 전부 매핑. `NhisImportService.matchRow` 지점 검증은 V21 `trg_nhis_rows_client_branch` DB 방어 + 앱 이중 검증(신규 테스트).
    - **Must attendance**: 당일 목록(V23)·체크인 단건 `findTopBy…`(V24)·집계 6종(V22/V25/V26 partial)·프로필 탭(V24)·대시보드(`DashboardService`→동일 repository 메서드)·XOR·달력일·시간 정합(V4/V11/V14/V15/V37) 유지.
    - **Must guardians/clients/health/audit**: `guardian_link_status`+트리거(V39)·대표 보호자 UK(V7)·연결 검증(V25)·case-insensitive 지점명 UK(V40)·Tenant 이메일 UK(V30)·건강 alerts(V23 branch·V8 org type)·audit_logs `idx_audit_logs_org_created`(V2/V6).
    - **`guardian_invitations` 보류 유지**: API_SPEC 초대 계약 0건 — round 35 가설 테이블은 PLN 확정 전 미생성.
    - **v1.2 P0(등급 이력·입금 미납)**: MVP Must 범위 외 — REQUIREMENTS §6-3·ROADMAP v1.2.
    - **결론**: ERD·DATA_RETENTION·repository가 V40·`4274459` 시점 정합. 추가 마이그레이션·스키마 변경 불필요(본 검증 기록 + ERD 메타 timestamp 갱신만).
40. **V40 기준 전수 재대조 — 신규 누락 0건 (2026-06-06, round 40, backend `aa71412` HEAD)** — 신규 DBA 호출. backend HEAD가 round 39(`4274459`) → **`aa71412`**로 1커밋 전진. 변경분은 `MustApiEndpointRoutingTest`(API_SPEC Must 엔드포인트 라우팅)·`RoleBasedControllerAccessTest`(7역할 RBAC 확장) **테스트 전용** — repository·서비스 시그니처·스키마 영향 없음. 21개 `*Repository` 전 쿼리 메서드·API_SPEC §1–§9·agents.yaml `core_entities`를 V1–V40 스키마(인덱스·제약·트리거)와 1:1 재대조 — **신규 누락 테이블/인덱스/제약 없음**. V41 미생성(rules.md §2/§8).
    - **마이그레이션 연속성**: V1–V40 40개 contiguous(갭·중복 0).
    - **Must billing**: `BillingClaimRepository`/`BillingClaimItemRepository`/`FeeScheduleRepository`/`CopayRateRepository`/`NhisImport{Batch,Row}Repository` — UK `uq_claim_branch_month`(V1)·`uq_billing_claim_items_claim_client`(V26)·`uq_billing_claims_org_id`(V10)·`uq_nhis_import_rows_org_id`(V37)·status+generated_at(V31)·NHIS batch 목록(V27/V37/V38) 전부 매핑.
    - **Must attendance**: 당일 목록(V23)·체크인 단건 `findTopBy…`(V24)·집계 6종(V22/V25/V26 partial)·프로필 탭(V24)·대시보드(`DashboardService`→동일 repository 메서드)·XOR·달력일·시간 정합(V4/V11/V14/V15/V37) 유지.
    - **Must guardians/clients/health/audit**: `guardian_link_status`+트리거(V39)·대표 보호자 UK(V7)·연결 검증(V25)·case-insensitive 지점명 UK(V40)·Tenant 이메일 UK(V30)·건강 alerts(V23 branch·V8 org type)·audit_logs `idx_audit_logs_org_created`(V2/V6).
    - **`guardian_invitations` 보류 유지**: API_SPEC 초대 계약 0건 — round 35 가설 테이블은 PLN 확정 전 미생성.
    - **v1.2 P0(등급 이력·입금 미납)**: MVP Must 범위 외 — REQUIREMENTS §6-3·ROADMAP v1.2.
    - **결론**: ERD·DATA_RETENTION·repository가 V40·`aa71412` 시점 정합. 추가 마이그레이션·스키마 변경 불필요(본 검증 기록 + ERD 메타 timestamp 갱신만).
41. **V40 기준 전수 재대조 — 신규 누락 0건 (2026-06-06, round 41, backend `c3f3146` HEAD)** — 신규 DBA 호출. backend HEAD가 round 40(`aa71412`) → **`c3f3146`**로 1커밋 전진. 변경분은 `PilotChecklistApiAccessTest`(파일럿 P1–P8·7역할 RBAC API 접근 검증, 697행) **테스트 전용** — repository·서비스 시그니처·스키마 영향 없음. 21개 `*Repository` 전 쿼리 메서드·API_SPEC §1–§9·agents.yaml `core_entities`를 V1–V40 스키마(인덱스·제약·트리거)와 1:1 재대조 — **신규 누락 테이블/인덱스/제약 없음**. V41 미생성(rules.md §2/§8, round 33–40 패턴 유지).
    - **마이그레이션 연속성**: V1–V40 40개 contiguous(갭·중복 0).
    - **Must billing**: `BillingClaimRepository`(`findByIdAndOrganizationId`→V10 UK; `findByOrganizationIdAndBranchIdAndYearMonth`→V1 UK `uq_claim_branch_month`; `…OrderByGeneratedAtDesc`→V22; `…AndStatusOrderByGeneratedAtDesc`→V31)·`BillingClaimItemRepository`(`findByClaimIdOrderByCreatedAtAsc`→V29; `findByClaimIdAndClientId`→V26 UK; `findByOrganizationIdAndClientIdOrderByCreatedAtDesc`→V25)·`FeeSchedule`/`CopayRate`(`findEffective*`→V23 + V7 EXCLUDE)·`NhisImport{Batch,Row}`(`findScopedBatches`→V27/V37/V38; `findByIdAndOrganizationId`→V37 UK) **전부 인덱스 매핑**. 파일럿 P6·P7 테스트가 exercise하는 `/billing/claims/generate`·`/billing/imports/nhis`·`PATCH …/rows/{rowId}/match`는 기존 제약·인덱스로 커버.
    - **Must attendance**: 당일 목록(V23)·체크인 단건 `findTopBy…`(V24)·집계 6종(V22/V25/V26 partial)·프로필 탭(V24)·파일럿 P3 `POST /attendance/check-in`·대시보드(`DashboardService`)·XOR·달력일·시간 정합(V4/V11/V14/V15/V37) 유지.
    - **Must guardians/clients/health/audit**: 파일럿 P1 `POST /clients`(primaryGuardian)·P4 건강 vitals/medications·P5 대시보드·P8 RBAC — `guardian_link_status`+트리거(V39)·대표 보호자 UK(V7)·연결 검증(V25)·case-insensitive 지점명 UK(V40)·Tenant 이메일 UK(V30)·건강 alerts(V23/V8)·audit_logs `idx_audit_logs_org_created`(V2/V6) 유지.
    - **`guardian_invitations` 보류 유지**: API_SPEC 전수 grep(`invitation|invite|초대`) **0건** — round 35 가설 테이블은 PLN 확정 전 미생성.
    - **v1.2 P0(등급 이력·입금 미납)**: MVP Must 범위 외 — REQUIREMENTS §6-3·ROADMAP v1.2.
    - **결론**: ERD·DATA_RETENTION·repository가 V40·`c3f3146` 시점 정합. 추가 마이그레이션·스키마 변경 불필요(본 검증 기록 + ERD/DATA_RETENTION 메타 timestamp 갱신만).
42. **V40 기준 전수 재대조 — 신규 누락 0건 (2026-06-07, round 42, backend `c3f3146` HEAD 불변)** — 신규 DBA 호출. backend HEAD는 round 41과 동일 **`c3f3146`**. working tree 변경은 untracked `SevenRoleJwtLoginE2eTest.java`(E2E 테스트, DB 영향 없음)뿐. 21개 `*Repository` 전 쿼리 메서드·API_SPEC §1–§9·agents.yaml `core_entities`를 V1–V40 스키마(인덱스·제약·트리거)와 1:1 재대조 — **신규 누락 테이블/인덱스/제약 없음**. V41 미생성(rules.md §2/§8).
    - **마이그레이션 연속성**: V1–V40 40개 contiguous(갭·중복 0).
    - **Must billing**: `BillingClaimRepository`/`BillingClaimItemRepository`/`FeeScheduleRepository`/`CopayRateRepository`/`NhisImport{Batch,Row}Repository` — UK `uq_claim_branch_month`(V1)·`uq_billing_claim_items_claim_client`(V26)·`uq_billing_claims_org_id`(V10)·`uq_nhis_import_rows_org_id`(V37)·status+generated_at(V31)·NHIS batch 목록(V27/V37/V38) 전부 매핑.
    - **Must attendance**: 당일 목록(V23)·체크인 단건 `findTopBy…`(V24)·집계 6종(V22/V25/V26 partial)·프로필 탭(V24)·대시보드·XOR·달력일·시간 정합(V4/V11/V14/V15/V37) 유지.
    - **Must guardians/clients/health/audit**: `guardian_link_status`+트리거(V39)·대표 보호자 UK(V7)·연결 검증(V25)·case-insensitive 지점명 UK(V40)·Tenant 이메일 UK(V30)·건강 alerts(V23/V8)·audit_logs `idx_audit_logs_org_created`(V2/V6).
    - **인증 보완 확인**: `AuthService.resetPassword` → `revokeAllActiveForUser`(V30 `idx_refresh_tokens_user_active`) — PLAN_NOTES #16 갱신.
    - **`guardian_invitations` 보류 유지**: API_SPEC 초대 계약 0건 — round 35 가설 테이블은 PLN 확정 전 미생성.
    - **v1.2 P0(등급 이력·입금 미납)**: MVP Must 범위 외 — REQUIREMENTS §6-3·ROADMAP v1.2.
    - **결론**: ERD·DATA_RETENTION·repository가 V40·`c3f3146` 시점 정합. 추가 마이그레이션·스키마 변경 불필요(본 검증 기록 + ERD/DATA_RETENTION 메타 timestamp 갱신만).
43. **V40 기준 전수 재대조 — 신규 누락 0건 (2026-06-07, round 43, backend `e8750d2` HEAD)** — 신규 DBA 호출. backend HEAD가 round 42(`c3f3146`) → **`e8750d2`**로 1커밋 전진. `git diff c3f3146 e8750d2` = `src/test/java/com/ogada/backend/security/SevenRoleJwtLoginE2eTest.java`(384행) **1건뿐, `src/main/` 변경 0건** — round 42에서 untracked였던 7역할 JWT 로그인 라이브 filter-chain E2E 테스트가 develop에 커밋된 것(BE-6 #4 해소). working tree CLEAN. repository·서비스 시그니처·스키마 영향 없음. 21개 `*Repository` 전 쿼리 메서드·API_SPEC §1–§9·agents.yaml `core_entities`를 V1–V40 스키마(인덱스·제약·트리거)와 1:1 재대조 — **신규 누락 테이블/인덱스/제약 없음**. V41 미생성(rules.md §2/§8, round 33–42 패턴 유지).
    - **마이그레이션 연속성**: `V1`–`V40` 40개 파일 contiguous(버전 갭·중복 0, `ls db/migration | wc -l` = 40). `V2__attendance_add_attendance_date.sql` 충돌본 삭제 상태 유지(ERD §7 주의).
    - **Must billing**: `BillingClaimRepository`(`findByIdAndOrganizationId`→V10 UK `uq_billing_claims_org_id`; `findByOrganizationIdAndBranchIdAndYearMonth`→V1 UK `uq_claim_branch_month` 단일 청구; `…OrderByGeneratedAtDesc`→V22; `…AndStatusOrderByGeneratedAtDesc`→V31)·`BillingClaimItemRepository`(`findByClaimIdOrderByCreatedAtAsc`→V29; `findByClaimIdAndClientId`→V26 UK `(claim_id, client_id)`; `findByOrganizationIdAndClientIdOrderByCreatedAtDesc`→V25)·`FeeSchedule`/`CopayRate`(`findEffective*`→V23 `(org, grade/type, effective_from DESC)` + V7 EXCLUDE 비중첩)·`NhisImport{Batch,Row}Repository`(`findScopedBatches`→V27/V37/V38; `findByIdAndOrganizationId`→V37 UK `uq_nhis_import_rows_org_id`; `findByBatchIdOrderByCreatedAtAsc`→V28) **전부 인덱스 매핑**.
    - **Must attendance**: 당일 목록(V23)·체크인 단건 `findTopBy…`(V24)·집계 6종(client-월 present V26·branch-일 present/checkout/absence V22·branch-월 present V25 partial)·프로필 탭(V24)·대시보드(`DashboardService` 동일 메서드)·XOR·달력일·시간 정합 CHECK(V4/V11/V14/V15/V37) 유지.
    - **Must guardians/clients/health/audit**: `guardian_link_status`+`trg_guardian_clients_refresh_link_status`(V39)·대표 보호자 1명 UK(V7)·연결 검증(V25)·case-insensitive 지점명 UK(V40)·Tenant 이메일 UK(V30)·`idx_users_email_lower`(V28)·건강 alerts(지점 V23·org type V8)·audit_logs `idx_audit_logs_org_created`(V2/V6)·`searchByScope`(V33 partial + V12/V26 trigram).
    - **`guardian_invitations` 보류 유지**: API_SPEC 전수 grep(`invitation|invite|초대`) **0건** 재확인 — round 35 가설 테이블은 PLN의 API_SPEC §5 초대 계약(채널·만료) 확정 전까지 미생성. frontend graceful fallback 충돌 없음.
    - **v1.2 P0(등급 이력·입금 미납)**: MVP Must 범위 외 — REQUIREMENTS §6-3·ROADMAP v1.2.
    - **결론**: ERD·DATA_RETENTION·repository가 V40·`e8750d2` 시점 정합. 추가 마이그레이션·CHECK·트리거·문서 변경 불필요(본 검증 기록 + ERD/DATA_RETENTION 메타 timestamp 갱신만).
44. **V40 기준 전수 재대조 — 신규 누락 0건 (2026-06-07, round 44, backend `e8750d2` HEAD 불변)** — 신규 DBA 호출. backend HEAD는 round 43과 동일 **`e8750d2`**(7역할 JWT 로그인 E2E 커밋). working tree 변경은 untracked `src/test/java/com/ogada/backend/security/PilotChecklistJwtE2eTest.java`(파일럿 체크리스트 JWT E2E 테스트) **1건뿐 — 테스트 전용, `src/main/`·repository·entity·스키마 영향 0건**. 이번 라운드는 prior 라운드 결론을 신뢰하지 않고 **21개 `*Repository` 인터페이스 파일을 직접 정독**하여 전 쿼리 메서드를 V1–V40 인덱스·제약·트리거와 1:1 독립 재대조 — **신규 누락 테이블/인덱스/제약 없음**. V41 미생성(rules.md §2/§8, round 33–43 패턴 유지).

45. **V40 기준 전수 재대조 — Must 누락 0건 + B08 v2 WIP 관측 (2026-06-07, round 45, backend `e8750d2` HEAD 불변)** — 신규 DBA 호출. backend HEAD는 round 43·44와 동일 **`e8750d2`**. develop commit Δ = 0. **working tree에 신규 v2 B08 WIP 출현**: ① `src/main/resources/db/migration/V41__guardian_notification_preferences.sql`(`notification_preferences` 테이블 + UK `(organization_id, guardian_user_id)` + 인덱스 1개 + `quiet_hours` 쌍 CHECK), ② `src/main/java/com/ogada/backend/notification/` 6 java(`NotificationPreferenceEntity`·`Repository`·`Service`·API DTO 등), ③ `src/test/java/com/ogada/backend/notification/` 4 @Test, ④ round 44에서 관측된 `PilotChecklistJwtE2eTest.java` 잔존. 모두 **untracked — develop HEAD 미커밋, MVP Must 범위 외 (REQUIREMENTS §6 v2 알림 채널 — `notify_attendance` 등은 v2 카카오·SMS 발송과 결합).** **22개 `*Repository`**(`NotificationPreferenceRepository` 추가) 인터페이스·서비스를 V1–V40 스키마와 1:1 재대조 — **Must 엔티티(billing·attendance·clients·health·guardians·audit) 신규 누락 0건**. V41 자체는 coder의 B08 v2 WIP 산물이므로 DBA는 commit 전 reshape하지 않음(rules.md §8 — 기존 파일 스타일·구조 존중).
    - **마이그레이션 연속성**: 커밋된 V1–V40 = 40개 contiguous(갭·중복 0). WT V41은 develop merge 후 V41로 정상 진입 가능.
    - **Must billing/attendance/clients/health/guardians/audit 커버리지**: round 44 직접 정독 매핑(`BillingClaimRepository` 4·`BillingClaimItemRepository` 3·`AttendanceRepository` 8·`ClientRepository`·`GuardianClientRepository`·`HealthRecordRepository`·`User`/`UserBranch`/`Branch`/`Organization`·토큰·로그인·백업·audit) **변동 없음** — backend `src/main/` 변경 0건.
    - **신규 추가된 `NotificationPreferenceRepository`**: 단일 메서드 `findByOrganizationIdAndGuardianUserId(UUID, UUID)` — V41 UK `uq_notification_preferences_org_guardian` + 인덱스 `idx_notification_preferences_org_guardian`로 커버. 추가 인덱스 불필요(V41 자체 정합). 단 V41은 **API_SPEC §11과 schema gap**(아래 V42 follow-up 참고).
    - **API_SPEC §11 vs V41 schema gap (DBA 관측, B08 commit 후 reconcile 필요)**:
      | 항목 | API_SPEC §11-1 명세 | V41 실제 컬럼 | 조치 |
      |------|-------------------|---------------|------|
      | 채널 토글 5종 | `channel_in_app`·`channel_push`·`channel_email`·`channel_kakao`·`channel_sms` | `allow_in_app`·`allow_web_push`·`allow_email`·`allow_kakao_alimtalk`·`allow_sms_fallback` | **컬럼명 차이** — `NotificationPreferenceEntity`가 `allow_*` ↔ JSON `channelInApp` 매핑(`@Column(name=…)`). 외부 계약 OK, 내부 명칭만 상이. PLN·COD가 ERD/API_SPEC §11-1 텍스트 정렬 권장(어느 쪽이 정본인지 결정). |
      | 이벤트 토글 4종 | `notify_attendance`·`notify_daily_care`·`notify_billing`·`notify_emergency` | **컬럼 없음** | **DBA V42 후보** — V41 commit 후 `BOOLEAN NOT NULL DEFAULT TRUE` 4컬럼 추가, 발송 매트릭스의 행(이벤트)×열(채널) 둘 다 보존. |
      | 카카오·SMS 수신 동의 | `consent_at` 기록 (§11-3, PIPA marketing-adjacent) | **컬럼 없음** | **DBA V42 후보** — `kakao_consent_at TIMESTAMPTZ`·`sms_consent_at TIMESTAMPTZ` NULL 허용, CHECK `allow_kakao_alimtalk = FALSE OR kakao_consent_at IS NOT NULL`(SMS도 대칭). PIPA §22 적법 동의 보관 필수. |
      | row lifecycle 시간 정합 | (암묵) | `updated_at >= created_at` CHECK 없음 | **DBA V42 후보** — V37 패턴 확장(`chk_notification_preferences_updated_after_created`). JPA `@PrePersist`/`@PreUpdate`는 항상 충족하지만 raw SQL backdate 1차 방어. |
      | quiet hours 정합 | 미명시 | `chk_notification_preferences_quiet_hours_pair`(둘 다 NULL 또는 둘 다 NOT NULL) 존재; **순서 CHECK 없음** | V41 그대로 두기 — 24시간 wrap-around(예: `22:00–07:00`)가 자연스러우므로 `end > start` CHECK는 부정확. UI에서 안내. |
    - **V42 follow-up (보류 — B08 commit + PLN API_SPEC §11 텍스트 확정 후 작성)**:
      ```sql
      -- V42__notification_preferences_event_toggles_and_consent.sql (DBA 후보)
      ALTER TABLE notification_preferences
          ADD COLUMN notify_attendance BOOLEAN NOT NULL DEFAULT TRUE,
          ADD COLUMN notify_daily_care BOOLEAN NOT NULL DEFAULT TRUE,
          ADD COLUMN notify_billing    BOOLEAN NOT NULL DEFAULT TRUE,
          ADD COLUMN notify_emergency  BOOLEAN NOT NULL DEFAULT TRUE,
          ADD COLUMN kakao_consent_at  TIMESTAMPTZ,
          ADD COLUMN sms_consent_at    TIMESTAMPTZ,
          ADD CONSTRAINT chk_np_kakao_consent_required
              CHECK (allow_kakao_alimtalk = FALSE OR kakao_consent_at IS NOT NULL),
          ADD CONSTRAINT chk_np_sms_consent_required
              CHECK (allow_sms_fallback = FALSE OR sms_consent_at IS NOT NULL),
          ADD CONSTRAINT chk_np_updated_after_created
              CHECK (updated_at >= created_at),
          ADD CONSTRAINT chk_np_kakao_consent_after_created
              CHECK (kakao_consent_at IS NULL OR kakao_consent_at >= created_at),
          ADD CONSTRAINT chk_np_sms_consent_after_created
              CHECK (sms_consent_at IS NULL OR sms_consent_at >= created_at);
      ```
      ※ V42 작성 트리거: ① B08 develop commit, ② PLN가 API_SPEC §11-1 표를 정본화(컬럼명 정렬), ③ 카카오 알림톡 발신 사업자 등록 결정(채널 ID·템플릿). 셋 다 만족하면 DBA가 V42 마이그레이션 + ERD §4-7·§6·§7 보강 + DATA_RETENTION §3 알림 동의 보존 추가.
    - **`guardian_invitations` 보류 유지 (#35)**: API_SPEC 초대 계약 전수 grep(`invitation|invite|초대`) **0건** 재확인 — PLN의 API_SPEC §5 초대 계약(채널·만료) 확정 전까지 미생성.
    - **v1.2 P0(등급 이력·입금 미납)**: MVP Must 범위 외 — REQUIREMENTS §6-3·ROADMAP v1.2.
    - **결론**: ERD·DATA_RETENTION·repository가 V40·`e8750d2` 시점 정합. **Must 스코프 추가 마이그레이션·스키마 변경 불필요**. v2 V41 reshape는 coder commit + PLN 텍스트 정렬 후 DBA가 별도 라운드에서 V42로 처리(이번 라운드는 메타 timestamp 갱신 + #45 기록만).
    - **마이그레이션 연속성**: `V1`–`V40` 40개 파일 contiguous(버전 갭·중복 0). `V2__attendance_add_attendance_date.sql` 충돌본 삭제 상태 유지(ERD §7 주의).
    - **Must billing (직접 정독 매핑)**: `BillingClaimRepository` 4메서드(`findByIdAndOrganizationId`→V10 UK `uq_billing_claims_org_id`; `findByOrganizationIdAndBranchIdAndYearMonth`→V1 UK `uq_claim_branch_month` 단일 청구; `…OrderByGeneratedAtDesc`→V22; `…AndStatusOrderByGeneratedAtDesc`→V31)·`BillingClaimItemRepository` 3메서드(`findByClaimIdOrderByCreatedAtAsc`→V29; `findByClaimIdAndClientId`→V26 UK `(claim_id, client_id)`; `findByOrganizationIdAndClientIdOrderByCreatedAtDesc`→V25)·`FeeScheduleRepository`(`findByOrganizationIdOrderByYearDesc…`→V27 `(org, year DESC, grade ASC, effective_from DESC)`; `findTop…YearAndLtcGradeAndEffectiveToIsNull`→V7 partial 현행 UK; `findEffectiveForGrade`→V23 `(org, grade, effective_from DESC)` + V7 EXCLUDE)·`CopayRateRepository`(`findTop…CopayTypeAndEffectiveToIsNull`→V7 partial UK; `findEffectiveByType`→V23)·`NhisImport{Batch,Row}Repository`(`findScopedBatches` 4-파라미터 nullable yearMonth/claimId→V27/V37 partial/V38; `findByIdAndOrganizationId`→V37 UK `uq_nhis_import_rows_org_id`; `findByBatchIdOrderByCreatedAtAsc`→V28) **전부 인덱스 매핑**.
    - **Must attendance (직접 정독 매핑)**: `AttendanceRepository` 8메서드 — 당일 목록(`…AttendanceDateOrderByCreatedAtDesc`)→V23; 체크인 단건(`findTopBy…ClientIdAndAttendanceDate…`)→V24; 집계 4종(client-월 present `countBy…ClientIdAndAttendanceDateBetweenAndCheckInAtIsNotNull`→V26 partial, branch-일 present/checkout/absence→V22 partial 3종, branch-월 present→V25 partial); 이용자 출석 탭(`…ClientIdOrderByAttendanceDateDescCreatedAtDesc`·`…AttendanceDateBetween…`)→V24 `(org, client, attendance_date DESC)`. XOR·달력일·시간 정합 CHECK(V4/V11/V14/V15/V37) 유지.
    - **Must clients/guardians/health (직접 정독 매핑)**: `ClientRepository`(`findByIdAndOrganizationIdAndActiveTrue`→V33 partial+PK; `findByOrganizationIdAndUserIdAndActiveTrue`→V23 `idx_clients_org_user`; `searchByScope`(branchIds IN + nullable branchId/query)→V33 partial + V12/V26 trigram; counts→V23 `(org, branch, is_active)`; `findByOrganizationIdAndLtcCertNo`→V4 UK; `…BranchIdAndLtcCertNo`→V27)·`GuardianClientRepository`(연결·대표 정렬 `…OrderByPrimaryGuardianDescCreatedAtAsc`→V24/V23; `exists/find…GuardianUserIdAndClientId`→V25; `countBy…ClientId`→V24 prefix; `clearPrimaryForClient` UPDATE→V31 partial `(org, client) WHERE is_primary`; 대표 1명 UK V7·link_status 트리거 V39)·`HealthRecordRepository`(프로필 `…ClientIdOrderByRecordedAtDesc…`→V24; 지점 alerts `…BranchIdAndRecordedAtGreaterThanEqual…`→V23; HQ alerts `…BranchIdIn…`→V8 org-type).
    - **인증·조직·기타 (직접 정독 매핑)**: `UserRepository`(`existsByOrganizationIdAndEmailIgnoreCase`→V30 UK `uq_users_org_email_lower`; `findAllByEmailIgnoreCase`(cross-tenant lower)→V28 `idx_users_email_lower`; `findByOrganizationId`(nullable active)→V30 `(org, is_active)`)·`UserBranchRepository`(`findByUserId`/`findByUserIdIn`→V29 `(user_id)`; `deleteByUserId`→동일)·`RefreshTokenRepository`(`findActiveByTokenHash`/`revokeByTokenHash`→V6 UK `token_hash`; `revokeAllActiveForUser`→V30 partial `(user_id) WHERE revoked_at IS NULL`)·`BranchRepository`(`existsByOrganizationIdAndNameIgnoreCase(AndIdNot)`→V40 functional UK `(org, lower(name))`)·`OrganizationRepository`(`findByActiveTrueAndBackupEnabledTrue`→V28 partial; `findByName…OrBusinessNo…ContainingIgnoreCase`→V27/V29 trigram). audit_logs(JdbcClient)→V2/V6 `idx_audit_logs_org_created`.
    - **`guardian_invitations` 보류 유지**: API_SPEC 전수 grep(`invitation|invite|초대`) **0건** 재확인 — round 35 가설 테이블은 PLN의 API_SPEC §5 초대 계약(채널·만료) 확정 전까지 미생성. frontend graceful fallback 충돌 없음.
    - **v1.2 P0(등급 이력·입금 미납)**: MVP Must 범위 외 — REQUIREMENTS §6-3·ROADMAP v1.2. `billing_claims.status` DRAFT/CONFIRMED/PAID는 MVP 충족.
    - **결론**: ERD·DATA_RETENTION·repository가 V40·`e8750d2` 시점 정합. 추가 마이그레이션·CHECK·트리거·문서 변경 불필요(본 검증 기록 + ERD/DATA_RETENTION 메타 timestamp 갱신만).

46. **billing·attendance Must 직접 재대조 — 신규 누락 0건 (2026-06-07, round 46, backend `e8750d2` HEAD 불변)** — 신규 DBA 호출. backend HEAD는 round 43~45와 동일 **`e8750d2`**, develop commit Δ=0. working tree도 round 45와 동일(untracked `PilotChecklistJwtE2eTest.java` + v2 B08 WIP V41/`notification` java·test + `data/`). 이번 라운드는 prior 결론을 신뢰하지 않고 **billing·attendance repository 인터페이스 7개 파일을 직접 정독**(task 지정 Must 초점)하여 전 쿼리 메서드를 V1–V40 인덱스·제약과 1:1 독립 매핑 — **Must 신규 누락 0건**.
    - **billing 매핑(직접 정독)**: `BillingClaimRepository`(`findByIdAndOrganizationId`→V10 UK `uq_billing_claims_org_id`; `findByOrganizationIdAndBranchIdAndYearMonth`→V1 UK `uq_claim_branch_month` 단일 청구; `…OrderByGeneratedAtDesc`→V22; `…AndStatusOrderByGeneratedAtDesc`→V31)·`BillingClaimItemRepository`(`findByClaimIdOrderByCreatedAtAsc`→V29; `findByClaimIdAndClientId`→V26 UK `(claim_id, client_id)`; `findByOrganizationIdAndClientIdOrderByCreatedAtDesc`→V25)·`FeeScheduleRepository`(`…OrderByYearDescLtcGradeAscEffectiveFromDesc`→V27; `…AndYearOrderBy…`→V27 prefix; `findTop…YearAndLtcGradeAndEffectiveToIsNull`→V7 partial 현행 UK; `findEffectiveForGrade`→V23 + V7 EXCLUDE; `findByIdAndOrganizationId`→PK + org 필터)·`CopayRateRepository`(`…OrderByCopayTypeAscEffectiveFromDesc`→V23; `findTop…CopayTypeAndEffectiveToIsNull`→V7 partial UK; `findEffectiveByType`→V23)·`NhisImportBatchRepository`(`findByIdAndOrganizationId`→V8 UK; `findScopedBatches` nullable yearMonth/claimId→V27/V37 partial/V38)·`NhisImportRowRepository`(`findByBatchIdOrderByCreatedAtAsc`→V28; `findByIdAndOrganizationId`→V37 UK `uq_nhis_import_rows_org_id`). **전부 인덱스/제약 매핑**.
    - **attendance 매핑(직접 정독)**: `AttendanceRepository` 8메서드 — 당일 목록(`…AttendanceDateOrderByCreatedAtDesc`)→V23; 체크인 단건(`findTopBy…ClientIdAndAttendanceDate…`)→V24; 집계 4종(client-월 present→V26 partial, branch-일 present/checkout/absence→V22 partial 3종, branch-월 present→V25 partial); 이용자 출석 탭(`…ClientIdOrderByAttendanceDateDescCreatedAtDesc`·`…AttendanceDateBetween…`)→V24 `(org, client, attendance_date DESC)`. XOR·달력일·시간 정합 CHECK(V4/V11/V14/V15/V37) 유지.
    - **V41/V42 보류 재확인**: V41 `guardian_notification_preferences`는 여전히 **untracked**(B08 develop commit 미발생 = #45 V42 트리거 ① 미충족). uncommitted V41 위에 V42 `ALTER`를 작성하면 마이그레이션 비정합(존재하지 않는 테이블 ALTER)이므로 **DBA는 V42 미작성** — rules.md §8(coder WIP reshape 금지). #45 V42 후보 SQL(event-toggle·consent·시간 정합 CHECK)은 ① B08 commit ② API_SPEC §11-1 정본화 ③ 카카오 발신 사업자 결정 셋 충족 시 즉시 작성.
    - **`guardian_invitations` 보류 유지(#35)**: API_SPEC 초대 계약 0건 — PLN §5 계약 확정 전 미생성.
    - **결론**: ERD(§6/§7·§8)·repository가 V40·`e8750d2` 시점 정합. Must 스코프 추가 마이그레이션·스키마·문서 변경 불필요(본 검증 기록 + ERD 메타 timestamp 갱신만).

47. **billing·attendance Must — repository ↔ 마이그레이션 SQL 물리 대조 0건 (2026-06-07, round 47, backend `e8750d2` HEAD 불변)** — 신규 DBA 호출. 이번 라운드는 prior 결론(round 33–46)·ERD 산문을 신뢰하지 않고, billing 6 + attendance 1 = **7개 repository 인터페이스를 직접 정독**한 뒤 각 쿼리 메서드의 backing 인덱스/제약이 **실제 마이그레이션 SQL 파일에 물리적으로 존재**하는지 `rg`로 1:1 확인(ERD 문서 매핑이 아닌 DDL 원문 grep). **Must 신규 누락 0건.**
    - **billing 물리 확인**: `uq_billing_claims_org_id`(V10:15)·`uq_claim_branch_month`(V1:129)·`idx_billing_claims_org_branch_generated`(V22:61)·`idx_billing_claims_org_branch_status_generated`(V31:14)·`uq_billing_claim_items_claim_client`(V26:18)·`idx_billing_claim_items_claim_created`(V29:33)·`idx_billing_claim_items_org_client_created`(V25:17)·`idx_fee_schedules_org_list`(V27:32)·`idx_fee_schedules_org_grade_effective`/`idx_copay_rates_org_type_effective`(V23:88/91, + V7 EXCLUDE·현행 partial UK)·`uq_nhis_import_rows_org_id`(V37:57)·`idx_nhis_import_batches_org_branch_created`(V38:13)·`idx_nhis_import_batches_org_branch_claim_created`(V37:64)·`idx_nhis_import_rows_batch_created`(V28:31) — 모두 DDL 원문 존재.
    - **attendance 물리 확인**: `findBy…AttendanceDateOrderByCreatedAtDesc`→`idx_attendance_daily_list`(V23:76); `findTopBy…ClientIdAndAttendanceDate…`→`idx_attendance_org_branch_client_date`(V24:27); 집계 4종→`idx_attendance_branch_present`/`_checkout`/`_absence`(V22:73/77/81)·`idx_attendance_billing_client_present`(V26:26)·`idx_attendance_monthly_present`(V25:24); 이용자 출석 탭(2메서드)→`idx_attendance_org_client_date`(V24:21). XOR·달력일·시간 정합 CHECK(V4/V11/V14/V15/V37) 유지.
    - **V41/V42·`guardian_invitations` 보류 재확인**: V41 `guardian_notification_preferences`는 여전히 untracked(B08 develop commit 미발생 = #45 V42 트리거 ① 미충족). uncommitted V41 위 V42 `ALTER` 작성은 비정합 → 미작성(rules.md §8). `guardian_invitations`는 PLN API_SPEC §5 계약 확정 전 미생성.
    - **결론**: V1–V40 contiguous, billing·attendance Must repository ↔ DDL 물리 정합. 추가 마이그레이션·스키마·문서 변경 불필요(본 검증 기록 + ERD 메타 timestamp 갱신만).

48. **billing·attendance Must DDL 물리 재대조 0건 + V41 reshape 관측 (2026-06-07, round 48, backend `e8750d2` HEAD 불변)** — 신규 DBA 호출. backend develop HEAD는 round 43~47과 동일 **`e8750d2`**(commit Δ=0). prior 결론을 신뢰하지 않고 billing 4·attendance 1·NHIS batch 1 repository 인터페이스를 직접 정독한 뒤 backing 인덱스/제약을 마이그레이션 SQL에서 `rg`로 물리 확인 — **Must 신규 누락 0건**.
    - **billing 물리 확인**: `findByIdAndOrganizationId`→`uq_billing_claims_org_id`(V10:15)·`findByOrganizationIdAndBranchIdAndYearMonth`→`uq_claim_branch_month`(V1:129)·`…OrderByGeneratedAtDesc`→`idx_billing_claims_org_branch_generated`(V22:61)·`…AndStatusOrderByGeneratedAtDesc`→`idx_billing_claims_org_branch_status_generated`(V31:14)·`findByClaimIdAndClientId`→`uq_billing_claim_items_claim_client`(V26:18)·`findByClaimIdOrderByCreatedAtAsc`→`idx_billing_claim_items_claim_created`(V29:33)·`findByOrganizationIdAndClientIdOrderByCreatedAtDesc`→`idx_billing_claim_items_org_client_created`(V25:17)·NHIS row `findByIdAndOrganizationId`→`uq_nhis_import_rows_org_id`(V37:57)·`findScopedBatches`→`idx_nhis_import_batches_org_branch_claim_created`(V37:64) partial + `idx_nhis_import_batches_org_branch_created`(V38:13) — 전부 DDL 원문 존재.
    - **attendance 물리 확인**: 당일 목록→`idx_attendance_daily_list`(V23:76); 체크인 단건 `findTopBy…`→`idx_attendance_org_branch_client_date`(V24:27); 집계 4종→`idx_attendance_branch_present`/`_checkout`/`_absence`(V22:73/77/81)·`idx_attendance_billing_client_present`(V26:26)·`idx_attendance_monthly_present`(V25:24); 이용자 출석 탭 2메서드→`idx_attendance_org_client_date`(V24:21). XOR·달력일·시간 정합 CHECK(V4/V11/V14/V15/V37) 유지.
    - **V41 reshape 관측 (신규 — #45 V42 follow-up 대부분 obsolete)**: untracked WIP `V41__guardian_notification_preferences.sql`이 round 45 관측본(`allow_in_app`·`allow_web_push`… + `quiet_hours` 쌍 CHECK, event-toggle·consent 없음)에서 **coder가 재작성**됨. 현재 V41 컬럼: `channel_in_app`·`channel_push`·`channel_email`·`channel_kakao`·`channel_sms` + `notify_attendance`·`notify_daily_care`·`notify_billing`·`notify_emergency` + `consent_at`(테이블 `guardian_notification_preferences`, FK `guardian_user_id`→`users`, UK `(organization_id, guardian_user_id)` + 동명 인덱스). `NotificationPreferenceEntity`(`@Column(name="channel_in_app")` 등)·`NotificationPreferenceService`·`…Repository.findByOrganizationIdAndGuardianUserId`와 자체 정합. **→ #45 V42 후보 중 event-toggle 4컬럼·`consent_at`은 V41에 이미 포함 = 불필요.** 잔여 V42 후보는 ① consent-required CHECK(`channel_kakao=FALSE OR consent_at IS NOT NULL`, SMS 대칭) ② `chk_…_updated_after_created`(V37 패턴) 2건뿐이며 **B08 develop commit 후** 작성(uncommitted V41 위 V42 ALTER는 비정합, rules.md §8). API_SPEC §11-1은 FK를 `guardians.guardian_id`로 기재하나 실제는 `users.guardian_user_id` — PLN(문서 소유자)/COD 텍스트 정렬 권장(DBA 비소유 문서, 미편집).
    - **`guardian_invitations` 보류 유지(#35)**: PLN API_SPEC §5 초대 계약(채널·만료) 확정 전 미생성. v1.2 P0(등급 이력·입금 미납)는 MVP Must 범위 외(REQUIREMENTS §6-3·ROADMAP v1.2).
    - **결론**: V1–V40 contiguous, billing·attendance Must repository ↔ DDL 물리 정합. Must 스코프 추가 마이그레이션·스키마 변경 불필요. ERD §7 검증 노트 V41 reshape 반영·메타 timestamp 갱신만 수행.

49. **billing·attendance Must DDL 재확인 0건 (2026-06-07, round 49, backend `e8750d2` HEAD 불변)** — 신규 DBA 호출. backend develop HEAD는 round 43–48과 동일 **`e8750d2`** (commit Δ=0). working tree도 round 48과 동일 (`.gitignore` M·`notification/` java·V41·`PilotChecklistJwtE2eTest.java` untracked). prior 결론을 신뢰하지 않고 billing(`BillingClaimRepository` 4·`BillingClaimItemRepository` 3·`NhisImportBatchRepository` 2·`NhisImportRowRepository` 2)·attendance(`AttendanceRepository` 8) 5개 인터페이스를 **직접 정독**한 뒤 backing 인덱스/제약 16건을 `rg`로 마이그레이션 SQL 원문에서 1:1 물리 확인 — **Must 신규 누락 0건**.
    - **billing 물리 재확인**: `findByIdAndOrganizationId`→`uq_billing_claims_org_id`(V10:15)·`findByOrganizationIdAndBranchIdAndYearMonth`→`uq_claim_branch_month`(V1:129)·`…OrderByGeneratedAtDesc`→`idx_billing_claims_org_branch_generated`(V22:61)·`…AndStatusOrderByGeneratedAtDesc`→`idx_billing_claims_org_branch_status_generated`(V31:14)·`findByClaimIdAndClientId`→`uq_billing_claim_items_claim_client`(V26:18)·`findByClaimIdOrderByCreatedAtAsc`→`idx_billing_claim_items_claim_created`(V29:33)·`findByOrganizationIdAndClientIdOrderByCreatedAtDesc`→`idx_billing_claim_items_org_client_created`(V25:17)·NHIS row `findByIdAndOrganizationId`→`uq_nhis_import_rows_org_id`(V37:57)·`findByBatchIdOrderByCreatedAtAsc`→`idx_nhis_import_rows_batch_created`(V28:31)·NHIS batch `findByIdAndOrganizationId`→`uq_nhis_import_batches_org_id`(V8)·`findScopedBatches`(nullable yearMonth/claimId)→`idx_nhis_import_batches_org_branch_claim_created`(V37:64) partial + `idx_nhis_import_batches_org_branch_created`(V38:13).
    - **attendance 물리 재확인**: 당일 목록(`…AttendanceDateOrderByCreatedAtDesc`)→`idx_attendance_daily_list`(V23:76); 체크인 단건(`findTopBy…ClientIdAndAttendanceDate…`)→`idx_attendance_org_branch_client_date`(V24:27); 집계 4종(client-월 present→`idx_attendance_billing_client_present` V26:26 partial; branch-일 present/checkout/absence→`idx_attendance_branch_present`/`_checkout`/`_absence` V22:73/77/81 partial; branch-월 present→`idx_attendance_monthly_present` V25:24 partial); 이용자 출석 탭 2메서드(`…ClientIdOrderByAttendanceDateDescCreatedAtDesc`·`…ClientIdAndAttendanceDateBetween…`)→`idx_attendance_org_client_date`(V24:21). XOR·달력일·시간 정합 CHECK(V4/V11/V14/V15/V37)·`(client_id, attendance_date)` UK(V2) 유지.
    - **V41 보류 재확인**: `git status` 결과 V41 여전히 **untracked** (B08 develop commit 미발생) — #45/#48 V42 후보(consent-required CHECK 2건 + `chk_…_updated_after_created`) 작성 트리거 미충족. uncommitted V41 위 V42 `ALTER`는 비정합이므로 미작성(rules.md §8). API_SPEC §11-1 FK 표기 불일치(`guardians.guardian_id` vs `users.guardian_user_id`)는 PLN/COD 영역.
    - **`guardian_invitations` 보류 유지(#35)**: API_SPEC 초대 계약 grep `invitation|invite|초대` **0건** — PLN §5 계약 확정 전 미생성. v1.2 P0(등급 이력·입금 미납)는 MVP Must 범위 외.
    - **결론**: V1–V40 contiguous(40개), billing·attendance Must repository ↔ DDL 물리 정합. Must 스코프 추가 마이그레이션·CHECK·트리거·스키마 변경 불필요. 본 라운드 작업은 ERD §7·DATA_RETENTION 메타 timestamp 갱신 + ERD §7 round 48 → round 49 라벨 갱신뿐.

50. **billing·attendance Must DDL 물리 재확인 0건 + REQUIREMENTS/API_SPEC 재대조 (2026-06-07, round 50, backend `e8750d2` HEAD 불변)** — 신규 DBA 호출. backend develop HEAD는 round 43–49와 동일 **`e8750d2`**(commit Δ=0). `git status`로 V41 여전히 **untracked** 확인(`ls db/migration` = 41개 중 V41만 미추적, V1–V40 contiguous). prior 결론(round 33–49)·ERD 산문을 신뢰하지 않고 billing 4 repository(`BillingClaimRepository` 4메서드·`BillingClaimItemRepository` 3·`NhisImportBatchRepository` 2·`NhisImportRowRepository` 2) + `AttendanceRepository` 8메서드 인터페이스를 **직접 정독**, backing 인덱스/제약을 마이그레이션 SQL 원문에서 `rg`로 줄번호까지 1:1 물리 확인 — **Must 신규 누락 0건**.
    - **billing 물리 재확인**: `findByIdAndOrganizationId`→`uq_billing_claims_org_id`(V10:15)·`findByOrganizationIdAndBranchIdAndYearMonth`→`uq_claim_branch_month`(V1:129)·`…OrderByGeneratedAtDesc`→`idx_billing_claims_org_branch_generated`(V22:61)·`…AndStatusOrderByGeneratedAtDesc`→`idx_billing_claims_org_branch_status_generated`(V31:14)·`findByClaimIdAndClientId`→`uq_billing_claim_items_claim_client`(V26:18)·`findByClaimIdOrderByCreatedAtAsc`→`idx_billing_claim_items_claim_created`(V29:33)·`findByOrganizationIdAndClientIdOrderByCreatedAtDesc`→`idx_billing_claim_items_org_client_created`(V25:17)·NHIS batch `findByIdAndOrganizationId`→`uq_nhis_batches_org_id`(V8:117)·`findScopedBatches`(nullable yearMonth/claimId)→`idx_nhis_import_batches_org_branch_claim_created`(V37:64) partial + `idx_nhis_import_batches_org_branch_created`(V38:13)·NHIS row `findByIdAndOrganizationId`→`uq_nhis_import_rows_org_id`(V37:57)·`findByBatchIdOrderByCreatedAtAsc`→`idx_nhis_import_rows_batch_created`(V28:31).
    - **attendance 물리 재확인**: 당일 목록(`…AttendanceDateOrderByCreatedAtDesc`)→`idx_attendance_daily_list`(V23:76); 체크인 단건(`findTopBy…ClientIdAndAttendanceDate…`)→`idx_attendance_org_branch_client_date`(V24:27); 집계 4종(client-월 present→`idx_attendance_billing_client_present` V26:26 partial; branch-일 present/checkout/absence→`idx_attendance_branch_present`/`_checkout`/`_absence` V22:73/77/81 partial; branch-월 present→`idx_attendance_monthly_present` V25:24 partial); 이용자 출석 탭 2메서드→`idx_attendance_org_client_date`(V24:21). XOR·달력일·시간 정합 CHECK(V4/V11/V14/V15/V37)·`(client_id, attendance_date)` UK(V2) 유지.
    - **REQUIREMENTS·API_SPEC 재대조**: REQUIREMENTS §3-9(청구 2단계·수가표 B·copay 4구분·NHIS reconciliation)·§3-3(출석 manual/qr_self)·§3-2-1(RRN 암호화·마스킹·동의)·API_SPEC §4–§9 엔드포인트 모두 V1–V40 스키마로 커버. agents.yaml `core_entities` 11종 충족(`medications`→`health_records.record_type='medication'`, `meal_records`·`activity_programs`→v1 이후 Should 예약 ERD §5, `notifications`→V1/V10).
    - **V41/V42 보류 재확인**: V41 `guardian_notification_preferences`는 `git status`상 여전히 untracked(B08 develop commit 미발생 = #45 V42 트리거 ① 미충족). uncommitted V41 위 V42 `ALTER`는 비정합이므로 미작성(rules.md §8·§11 범위 제어). #45/#48 V42 후보(consent-required CHECK 2건 + `chk_…_updated_after_created`)는 ① B08 commit ② API_SPEC §11-1 정본화(현재 FK를 `guardians.guardian_id`로 표기하나 실제 `users.guardian_user_id` — PLN/COD 정렬 영역) ③ 카카오 발신 사업자 결정 셋 충족 시 즉시 작성.
    - **`guardian_invitations` 보류 유지(#35)**: API_SPEC 초대 계약 grep `invitation|invite|초대` **0건** — PLN §5 계약 확정 전 미생성. v1.2 P0(등급 이력·입금 미납)는 MVP Must 범위 외(REQUIREMENTS §6-3·ROADMAP v1.2).
    - **결론**: V1–V40 contiguous, billing·attendance Must repository ↔ DDL 물리 정합. Must 스코프 추가 마이그레이션·CHECK·트리거·스키마 변경 불필요. 본 라운드 작업은 ERD §7 round 49 → round 50 라벨·DATA_RETENTION 메타 timestamp 갱신뿐.

51. **billing·attendance Must DDL 물리 재확인 0건 + core_entities 전수 대조 (2026-06-07, round 51, backend `e8750d2` HEAD 불변)** — 신규 DBA 호출. backend develop HEAD는 round 43–50과 동일 **`e8750d2`**(commit Δ=0). `git status`: V41 `guardian_notification_preferences` + `notification/` java·test 여전히 **untracked**. prior 결론(round 33–50)을 신뢰하지 않고 billing 4 repository + `AttendanceRepository` 8메서드를 **직접 정독**, backing 인덱스/제약 16건을 마이그레이션 SQL 원문 `rg`로 물리 확인 — **Must 신규 누락 0건**.
    - **billing 물리 재확인**: round 50과 동일 16건 — `uq_billing_claims_org_id`(V10:15)·`uq_claim_branch_month`(V1:129)·`idx_billing_claims_org_branch_generated`(V22:61)·`idx_billing_claims_org_branch_status_generated`(V31:14)·`uq_billing_claim_items_claim_client`(V26:18)·`idx_billing_claim_items_claim_created`(V29:33)·`idx_billing_claim_items_org_client_created`(V25:17)·`uq_nhis_batches_org_id`(V8:117)·`idx_nhis_import_batches_org_branch_claim_created`(V37:64) partial + `idx_nhis_import_batches_org_branch_created`(V38:13)·`uq_nhis_import_rows_org_id`(V37:57)·`idx_nhis_import_rows_batch_created`(V28:31).
    - **attendance 물리 재확인**: `idx_attendance_daily_list`(V23:76)·`idx_attendance_org_branch_client_date`(V24:27)·집계 partial 4종(V22:73/77/81·V25:24·V26:26)·`idx_attendance_org_client_date`(V24:21). XOR·달력일·시간 정합 CHECK(V4/V11/V14/V15/V37)·`(client_id, attendance_date)` UK(V2) 유지.
    - **agents.yaml `core_entities` 11종**: `users`·`clients`·`guardians`(→`guardian_clients`+`users.role_code=guardian`)·`attendance`·`health_records`·`medications`(→`health_records.record_type='medication'`)·`meal_records`·`activity_programs`(→v1 Should 예약 ERD §5)·`billing`(→`billing_claims`/`fee_schedules`/`copay_rates`/`nhis_import_*`)·`audit_logs`·`notifications`(→V1/V10) — **Must MVP 전부 V1–V40 커버**.
    - **V41/V42·v1.2 P0 보류 재확인**: V41 untracked(B08 commit 미발생) → V42 미작성(rules.md §8). v1.2 Epic L(입금·미납)·Epic M(등급 이력)는 MVP Must 범위 외 — `billing_claims.status` DRAFT/CONFIRMED/PAID로 MVP 충족; `ltc_grade_history`·부분입금은 PLN API_SPEC 확정 후 별도 마이그레이션.
    - **문서 보완**: ERD §4-7-1 `guardian_notification_preferences`(v2 WIP) 신설·§7 V41 행 추가·DATA_RETENTION §3 수신 설정 보존 1행 추가. **Must 스코프 신규 마이그레이션 없음**.

52. **B08 commit 확인 → 보류했던 V42 (보호자 알림 설정 consent·시간 정합) 추가 (2026-06-07, round 52, backend HEAD `e8750d2` → `c3b8716`)** — 신규 DBA 호출. round 48~51에서 「B08 develop commit 후 작성」으로 **보류**해 온 V42 후보가 이번 round 해제됨.
    - **상태 변화 확인**: backend develop HEAD가 round 51 관측 `e8750d2`에서 **`c3b8716`로 전진**. `git log`에 `feac558 feat(v2): guardian notification preferences API (QA-B08)` 커밋 존재, `git status` **작업트리 clean** → V41 `guardian_notification_preferences.sql` + `NotificationPreferenceService`/`…Entity`/`…Repository`/Controller·테스트(`feac558`, 12파일)가 **모두 커밋 완료**(round 51까지의 untracked 상태 종료). 보류 전제(uncommitted V41 위 ALTER 비정합)가 해소됨.
    - **앱 로직 정독 후 CHECK 안전성 검증**: `NotificationPreferenceService.applyUpdate`는 요청이 `channelKakao`·`channelSms`를 활성화할 때(`isConsentChannelEnabled`) 항상 `consent_at = OffsetDateTime.now()`를 적재하고, `consent_at`을 NULL로 되돌리는 경로가 없음 → `(channel_kakao OR channel_sms) ⇒ consent_at IS NOT NULL` 앱 작성 행에 always-true. `NotificationPreferenceEntity.@PrePersist`(`created_at=updated_at=NOW()`)·`@PreUpdate`(`updated_at=NOW()`) → `updated_at >= created_at`·`consent_at >= created_at` always-true. **네 CHECK 모두 backfill 불필요**.
    - **V42 작성**: `V42__guardian_notification_preferences_consent_temporal.sql` — ①`chk_…_kakao_consent` ②`chk_…_sms_consent`(API_SPEC §11-3 동의 기록 규칙 DB backstop) ③`chk_…_updated_after_created`(V37 패턴) ④`chk_…_consent_after_created`(V36 패턴). ERD §4-7-1·§7-36·§7 round note·migration 버전표(V41 커밋·V42 신규) 갱신.
    - **Must 재대조**: billing(4 repository)·attendance(`AttendanceRepository` 8메서드) backing 인덱스/제약 round 51 동일 — **Must 신규 누락 0건** 유지. V42는 **v2 알림(Must 범위 외) 무결성 보완**.
    - **잔여**: `guardian_invitations`(US-J01 v1.1)·v1.2 P0(`ltc_grade_history`·부분입금/미납)는 PLN API_SPEC 계약 확정 후 별도 마이그레이션. API_SPEC §11-1 FK 표기(`guardians.guardian_id`)와 실제 스키마(`users.guardian_user_id`) 텍스트 불일치 → PLN/COD 정렬 권장(DBA 비소유 문서).

53. **V42 정합 재검증 + billing·attendance·NHIS repository ↔ V41 컬럼 독립 재대조 0건 (2026-06-07, round 53, backend HEAD `c3b8716` 불변)** — 신규 DBA 호출. round 52에서 추가한 V42가 디스크에 존재(submodule untracked)하고 ERD §4-7-1·§7-36·§7 버전표·DATA_RETENTION §3(line 51)에 반영됨을 확인. prior 결론을 신뢰하지 않고 repository 인터페이스·V41/V42 DDL 원문을 **직접 정독**해 재대조 — **Must 신규 누락 0건, V42 컬럼 정합 OK**.
    - **V42 ↔ V41 컬럼 정합**: V42의 4개 CHECK가 참조하는 `channel_kakao`·`channel_sms`·`consent_at`·`created_at`·`updated_at`이 모두 V41 `guardian_notification_preferences` 정의(라인 8·9·14·15·16)에 존재 → `ALTER TABLE ... ADD CONSTRAINT` 비정합 없음. V41 커밋(`feac558`) 위 V42 ALTER 전제 충족.
    - **마이그레이션 연속성**: `ls db/migration` = **42개**(V1–V42 contiguous), 버전 갭·중복 0. V42만 submodule untracked(round 52 산출), V1–V41 커밋 완료. `V2__attendance_add_attendance_date.sql` 충돌본 삭제 상태 유지(ERD §7 주의).
    - **billing/attendance/NHIS 직접 정독**: `BillingClaimRepository`(4)·`BillingClaimItemRepository`(3)·`NhisImportBatchRepository`(2: `findByIdAndOrganizationId`→V8 UK·`findScopedBatches` nullable yearMonth/claimId→V37 partial+V38)·`NhisImportRowRepository`(2: `findByBatchIdOrderByCreatedAtAsc`→V28·`findByIdAndOrganizationId`→V37 UK)·`AttendanceRepository`(8: 당일목록 V23·체크인 단건 V24·집계 4종 V22/V25/V26 partial·이용자 출석 탭 2메서드 V24) 전 메서드 backing 인덱스/제약 물리 존재.
    - **Must 커버리지**: REQUIREMENTS §3-9(청구 2단계·수가표 B·copay 4구분·NHIS reconciliation)·§3-3(manual/qr_self)·§3-2-1(RRN 암호화·마스킹·동의)·API_SPEC §4–§9·agents.yaml `core_entities` 11종 모두 V1–V42 커버. 추가 테이블/인덱스/제약 불필요.
    - **잔여 유지**: `guardian_invitations`(v1.1)·`ltc_grade_history`·부분입금/미납(v1.2 P0)는 MVP Must 범위 외, PLN API_SPEC 계약 확정 후 별도 마이그레이션. 본 라운드는 검증 기록 + ERD 메타 timestamp·§7 라운드 라벨 갱신만 수행(신규 스키마 0).

54. **billing·attendance·NHIS repository ↔ DDL 물리 재확인 0건 + V41/V42 컬럼 정합 (2026-06-07, round 54, backend HEAD `c3b8716` 불변)** — 신규 DBA 호출. backend develop HEAD는 round 52·53과 동일 **`c3b8716`**(`feac558` B08 커밋 포함). prior 라운드(33–53) 산문·ERD 매핑을 신뢰하지 않고 repository 인터페이스 9개를 **직접 정독**한 뒤 backing 인덱스/제약을 마이그레이션 SQL 원문 `rg`로 줄번호까지 1:1 물리 확인 — **Must 신규 누락 0건**.
    - **billing/NHIS 물리 확인(12건)**: `findByIdAndOrganizationId`→`uq_billing_claims_org_id`(V10:15)·`findByOrganizationIdAndBranchIdAndYearMonth`→`uq_claim_branch_month`(V1:129)·`…OrderByGeneratedAtDesc`→`idx_billing_claims_org_branch_generated`(V22:61)·`…AndStatusOrderByGeneratedAtDesc`→`idx_billing_claims_org_branch_status_generated`(V31:14)·`findByClaimIdOrderByCreatedAtAsc`→`idx_billing_claim_items_claim_created`(V29:33)·`findByClaimIdAndClientId`→`uq_billing_claim_items_claim_client`(V26:18)·`findByOrganizationIdAndClientIdOrderByCreatedAtDesc`→`idx_billing_claim_items_org_client_created`(V25:17)·NHIS batch `findByIdAndOrganizationId`→`uq_nhis_batches_org_id`(V8:117)·`findScopedBatches`(nullable yearMonth/claimId)→`idx_nhis_import_batches_org_branch_claim_created`(V37:64) partial + `idx_nhis_import_batches_org_branch_created`(V38:13)·NHIS row `findByIdAndOrganizationId`→`uq_nhis_import_rows_org_id`(V37:57)·`findByBatchIdOrderByCreatedAtAsc`→`idx_nhis_import_rows_batch_created`(V28:31).
    - **attendance 물리 확인(8메서드)**: 당일 목록(`…AttendanceDateOrderByCreatedAtDesc`)→`idx_attendance_daily_list`(V23:76); 체크인 단건(`findTopBy…ClientIdAndAttendanceDate…`)→`idx_attendance_org_branch_client_date`(V24:27); 집계 4종(client-월 present→`idx_attendance_billing_client_present` V26:26; branch-일 present/checkout/absence→`idx_attendance_branch_present`/`_checkout`/`_absence` V22:73/77/81; branch-월 present→`idx_attendance_monthly_present` V25:24); 이용자 출석 탭 2메서드(`…ClientIdOrderByAttendanceDateDescCreatedAtDesc`·`…ClientIdAndAttendanceDateBetween…`)→`idx_attendance_org_client_date`(V24:21). XOR·달력일·시간 정합 CHECK(V4/V11/V14/V15/V37)·`(client_id, attendance_date)` UK(V2) 유지.
    - **V42 ↔ V41 컬럼 정합 재확인**: V42 4개 CHECK(`chk_…_kakao_consent`·`…_sms_consent`·`…_updated_after_created`·`…_consent_after_created`)가 참조하는 `channel_kakao`(V41:8)·`channel_sms`(V41:9)·`consent_at`(V41:14)·`created_at`(V41:15)·`updated_at`(V41:16)이 모두 커밋된 V41 테이블 정의에 존재 → `ALTER TABLE ... ADD CONSTRAINT` 비정합 0. `ls db/migration` = **42개**(V1–V42 contiguous, 갭·중복 0), V42만 submodule untracked.
    - **Must 커버리지**: REQUIREMENTS §3-9(청구 2단계·수가표 B·copay 4구분·NHIS reconciliation)·§3-3(manual/qr_self)·§3-2-1(RRN 암호화·마스킹·동의)·API_SPEC §4–§9·agents.yaml `core_entities` 11종 모두 V1–V42 커버. 추가 테이블/인덱스/제약 불필요.
    - **잔여 유지**: `guardian_invitations`(v1.1, #35)·`ltc_grade_history`·부분입금/미납(v1.2 P0)는 MVP Must 범위 외 — PLN API_SPEC 계약 확정 후 별도 마이그레이션. API_SPEC §11-1 FK 표기(`guardians.guardian_id`)와 실제 스키마(`users.guardian_user_id`) 불일치는 PLN/COD 정렬 권장(DBA 비소유 문서). 본 라운드는 검증 기록 + ERD/DATA_RETENTION 메타 timestamp·ERD §7 라운드 라벨 갱신만 수행(신규 스키마 0).

55. **billing·attendance·NHIS Must DDL 물리 재확인 0건 + V42 untracked 상태 확인 (2026-06-07, round 55, backend HEAD `c3b8716` 불변)** — 신규 DBA 호출. backend develop HEAD는 round 52–54와 동일 **`c3b8716`**. `git status`: V42 `guardian_notification_preferences_consent_temporal.sql` + `notification/domain/` 테스트 1건 **untracked**(round 52 산출, V41 `feac558` 커밋 위 ALTER — 비정합 0). prior 라운드 산문을 신뢰하지 않고 billing 4·attendance 1·NHIS batch/row 2·`FeeScheduleRepository`/`CopayRateRepository` as-of 2 = **9 repository 인터페이스 직접 정독** + backing 인덱스/제약 22건을 마이그레이션 SQL `rg`로 줄번호 1:1 물리 확인 — **Must 신규 누락 0건**.
    - **billing/NHIS 물리 확인(14건)**: `uq_billing_claims_org_id`(V10:15)·`uq_claim_branch_month`(V1:129)·`idx_billing_claims_org_branch_generated`(V22:61)·`idx_billing_claims_org_branch_status_generated`(V31:14)·`uq_billing_claim_items_claim_client`(V26:18)·`idx_billing_claim_items_claim_created`(V29:33)·`idx_billing_claim_items_org_client_created`(V25:17)·`idx_fee_schedules_org_list`(V27:32)·`idx_fee_schedules_org_grade_effective`(V23:88, + V7 EXCLUDE·현행 partial UK)·`idx_copay_rates_org_type_effective`(V23:91, + V7 EXCLUDE)·`uq_nhis_batches_org_id`(V8:117)·`idx_nhis_import_batches_org_branch_claim_created`(V37:64) partial + `idx_nhis_import_batches_org_branch_created`(V38:13)·`uq_nhis_import_rows_org_id`(V37:57)·`idx_nhis_import_rows_batch_created`(V28:31).
    - **attendance 물리 확인(8메서드)**: `idx_attendance_daily_list`(V23:76)·`idx_attendance_org_branch_client_date`(V24:27)·집계 partial 4종(V22:73/77/81·V25:24·V26:26)·`idx_attendance_org_client_date`(V24:21). XOR·달력일·시간 정합 CHECK(V4/V11/V14/V15/V37)·`(client_id, attendance_date)` UK(V2) 유지.
    - **v2 `NotificationPreferenceRepository`**: `findByOrganizationIdAndGuardianUserId` → V41 UK `uq_guardian_notification_preferences_org_guardian` + 동명 인덱스. V42 4 CHECK(kakao/sms consent·updated/consent temporal) 컬럼 정합 OK — **Must 범위 외**, develop commit 대기(untracked).
    - **v2 잔여 후보(V43, Must 아님)**: `guardian_notification_preferences`에 `notifications`(V10)와 동일한 복합 FK `(organization_id, guardian_user_id) → users(organization_id, id)`·`role_code='guardian'` 트리거(V13 `guardian_clients` 패턴) 미적용 — 앱(`NotificationPreferenceService.validateStaffAccess`)이 Tenant·연결 검증하므로 Must 블로커 아님. B08+V42 develop commit 후 필요 시 V43 작성.
    - **Must 커버리지**: REQUIREMENTS §3-9·§3-3·§3-2-1·API_SPEC §4–§9·agents.yaml `core_entities` 11종 — V1–V42 커버. `meal_records`·`activity_programs`는 v1 Should 예약(ERD §5).
    - **잔여 유지**: `guardian_invitations`(v1.1, #35)·v1.2 P0(등급 이력·입금 미납) — PLN API_SPEC 확정 후 별도 마이그레이션.
    - **결론**: Must 스코프 추가 마이그레이션·CHECK·트리거·스키마 변경 불필요. V42는 coder develop commit 대기. 본 라운드는 검증 기록 + ERD/DATA_RETENTION 메타 timestamp 갱신만.

56. **V42 develop commit 확인 + billing·attendance·NHIS Must DDL 물리 재확인 0건 (2026-06-07, round 56, backend HEAD `428ba7d`)** — 신규 DBA 호출. round 55에서 V42 untracked였던 상태가 **`428ba7d` develop commit으로 해소**(`git status` clean, `ls db/migration` = 42개 contiguous). prior 라운드 산문을 신뢰하지 않고 billing 4·attendance 1·NHIS 2·`FeeSchedule`/`CopayRate` as-of 2·`NotificationPreferenceRepository` 1 = **10 repository 인터페이스 직접 정독** + backing 인덱스/제약 22건(Must) + V42 4 CHECK를 마이그레이션 SQL `rg`로 줄번호 1:1 물리 확인 — **Must 신규 누락 0건**.
    - **상태 변화**: backend HEAD `c3b8716` → **`428ba7d`**(`feat(v2): V42 consent CHECK·temporal + NotificationPreferenceServiceTest`). V41(`feac558`) + V42 모두 develop HEAD 반영, working tree **clean**.
    - **billing/NHIS 물리 확인(14건)**: `uq_billing_claims_org_id`(V10:15)·`uq_claim_branch_month`(V1:129)·`idx_billing_claims_org_branch_generated`(V22:61)·`idx_billing_claims_org_branch_status_generated`(V31:14)·`uq_billing_claim_items_claim_client`(V26:18)·`idx_billing_claim_items_claim_created`(V29:33)·`idx_billing_claim_items_org_client_created`(V25:17)·`idx_fee_schedules_org_list`(V27:32)·`idx_fee_schedules_org_grade_effective`(V23:88, + V7 EXCLUDE·현행 partial UK)·`idx_copay_rates_org_type_effective`(V23:91, + V7 EXCLUDE)·`uq_nhis_batches_org_id`(V8:117)·`idx_nhis_import_batches_org_branch_claim_created`(V37:64) partial + `idx_nhis_import_batches_org_branch_created`(V38:13)·`uq_nhis_import_rows_org_id`(V37:57)·`idx_nhis_import_rows_batch_created`(V28:31).
    - **attendance 물리 확인(8메서드)**: `idx_attendance_daily_list`(V23:76)·`idx_attendance_org_branch_client_date`(V24:27)·집계 partial 4종(V22:73/77/81·V25:24·V26:26)·`idx_attendance_org_client_date`(V24:21). XOR·달력일·시간 정합 CHECK(V4/V11/V14/V15/V37)·`(client_id, attendance_date)` UK(V2) 유지.
    - **v2 `NotificationPreferenceRepository`**: `findByOrganizationIdAndGuardianUserId` → V41 UK `uq_guardian_notification_preferences_org_guardian`. V42 4 CHECK(kakao/sms consent·updated/consent temporal) 컬럼 정합 OK — **Must 범위 외**, develop `428ba7d` 커밋 완료.
    - **v2 잔여 후보(V43, Must 아님)**: `guardian_notification_preferences`에 `notifications`(V10)와 동일한 복합 FK `(organization_id, guardian_user_id) → users(organization_id, id)`·`role_code='guardian'` 트리거(V13 `guardian_clients` 패턴) 미적용 — `NotificationPreferenceService`가 Tenant·연결 검증하므로 Must 블로커 아님. 필요 시 V43 작성.
    - **Must 커버리지**: REQUIREMENTS §3-9(청구 2단계·수가표 B·copay 4구분·NHIS reconciliation)·§3-3(manual/qr_self)·§3-2-1(RRN 암호화·마스킹·동의)·API_SPEC §4–§9·agents.yaml `core_entities` 11종 — V1–V42 커버. `meal_records`·`activity_programs`는 v1 Should 예약(ERD §5).

57. **워크스페이스 마이그레이션 복구 + V35–V42 물리 작성 (2026-06-07, round 57, backend submodule `2799e29`)** — 신규 DBA 호출. ogada 루트에서 `src/backend` submodule이 삭제(`D src/backend`)되어 Flyway SQL **0건** 상태였음. `git submodule update --init src/backend`로 복구 → develop `2799e29`에 **V1–V34** 존재 확인. ERD §7·§7-30~§7-36에만 기재되어 있던 **V35–V42 8건을 물리 작성**하여 `ls db/migration` = **42개 contiguous**(갭·중복 0).
    - **V35**: `trg_fee_schedules_set_created_by`·`trg_branch_qr_tokens_set_created_by`(V32 actor 패턴).
    - **V36**: `chk_clients_consent_after_created`·`chk_clients_ltc_cert_valid_from_after_birth`·`chk_billing_claims_generated_after_created`.
    - **V37**: `chk_*_updated_after_created`(attendance/clients/billing_claims)·`chk_attendance_checkin_after_created`·`uq_nhis_import_rows_org_id`·`idx_nhis_import_batches_org_branch_claim_created`.
    - **V38**: `idx_nhis_import_batches_org_branch_created`.
    - **V39**: `clients.guardian_link_status` + `trg_guardian_clients_refresh_link_status` + `idx_clients_guardian_link_pending`.
    - **V40**: `uq_branches_org_name_lower`(V30 이메일 UK 패턴).
    - **V41–V42**: `guardian_notification_preferences` + consent/temporal CHECK 4건(v2 B08, MVP Must 범위 외).
    - **coder 전달**: submodule develop에 **커밋·push 필요**(현재 로컬 untracked 8파일). `DbSessionContext.setActorUserId`는 V35 actor 트리거와 연동. V39 `guardian_link_status`는 `ClientRepository`/등록 API에서 `LINKED` 전제 검증 권장.
    - **보류 유지**: `guardian_invitations`(v1.1 US-J01) — API_SPEC §4 초대 엔드포인트 명세 후 **V43** 별도 작성. v1.2 P0(등급 이력·입금 미납) 동일.

58. **V43 guardian_invitations + Must billing·attendance·NHIS 재대조 0건 (2026-06-07, round 58, backend submodule `2799e29`)** — 신규 DBA 호출. round 57 untracked V35–V42 유지 + **API_SPEC §4-1·REQUIREMENTS §8-1(결정 59 EMAIL·7일 만료) 확정**으로 **#35 보류 해제** → **`V43__guardian_invitations.sql` 작성**. `ls db/migration` = **43개** contiguous.
    - **V43 스키마**: `guardian_invitations` — EMAIL only CHECK·`token_hash` UK·`(organization_id, id)` Tenant UK·status lifecycle CHECK(`PENDING`/`ACCEPTED`/`CANCELLED`/`REVOKED`)·PII `recipient_email_encrypted`+`recipient_email_masked`·복합 FK(clients/branches/users V5/V14)·`trg_set_org_branch`(V23)·`trg_set_invited_by`(V32)·목록/pending/expires/revoked/accepted purge 인덱스.
    - **Must billing·attendance·NHIS 재확인**: `BillingClaimRepository`(4)·`BillingClaimItemRepository`(3)·`AttendanceRepository`(8)·`NhisImportBatchRepository`(1)·`NhisImportRowRepository`(2) 쿼리 메서드 backing 인덱스/제약 22건 — V1–V42 SQL `rg` 물리 존재 **0건 누락**.
    - **Must core_entities**: agents.yaml 11종 — `medications`→`health_records`, `meal_records`/`activity_programs`→v1 Should(ERD §5), `notifications`→V2, **`guardian_invitations`→V43(v1.1)**. MVP Must(§6-1) 청구·출석·이용자·건강·감사 **V1–V42 완비**.
    - **coder 전달**: BE-8(J01) — V35–V43 **develop 커밋** 후 `GuardianInvitationService`/`InvitationTokenService`/`GuardianInvitationRepository` 구현. accept TX: invitation `ACCEPTED` + `users`(guardian) + `guardian_clients` + `guardian_link_status` 트리거(V39). SEC-D8: accept만 `permitAll`. Flyway migrate 검증 필수.
    - **잔여**: v1.2 P0(`ltc_grade_history`·부분입금/미납) — PLN API_SPEC 확정 후 V44+. v2 `guardian_notification_preferences` 복합 FK `(org, guardian_user_id)→users`·role 트리거 — Must 아님, B08+V42 후 선택 V44.

59. **V43 보완 + Must billing·attendance·guardian 재대조 0건 (2026-06-08, round 59, backend submodule `2799e29`)** — round 58 V43 유지·독립 재검증. **V43 delta**: ①`client_id REFERENCES clients(id) ON DELETE CASCADE` — V2 `guardian_clients`·이용자 purge(DATA_RETENTION §4-1) 정합 ②partial `idx_guardian_invitations_pending_expires` — 만료 PENDING purge 배치 스캔. **Must 재확인**: `BillingClaimRepository`(4)·`BillingClaimItemRepository`(3)·`FeeScheduleRepository`(4)·`CopayRateRepository`(3)·`AttendanceRepository`(8)·`NhisImportBatchRepository`(1 scoped)·`NhisImportRowRepository`(2)·`GuardianClientRepository`(6) — backing 인덱스/제약 SQL `rg` **0건 누락**. **agents.yaml core_entities 11종**: MVP Must(billing·attendance·clients·health·guardians·audit) V1–V42 완비; `guardian_invitations` V43(v1.1); `meal_records`/`activity_programs`→Should(ERD §5); `notifications`→v2. **보류**: v1.3-A `transport_runs`/`transport_run_stops`(REQUIREMENTS §3-13·결정 62) — **API_SPEC §transport 미작성** → V44+ 대기. v1.2 P0(등급 이력·부분입금) 동일. **coder**: V35–V43 develop 커밋 → `mvn flyway:migrate` 검증 → BE-8 J01 구현.

60. **V1–V43 develop 커밋 확인 + Must·J01 repository ↔ DDL 물리 재대조 0건 (2026-06-08, round 60, backend `f47ffa1`)** — 신규 DBA 호출. backend develop HEAD가 round 59 관측 `2799e29`(V35–V43 untracked) → **`f47ffa1`로 전진**(`feat(v1.1/v2): J01 guardian invitations API + notification preferences`). `git status` **clean**, `ls db/migration` = **43개** contiguous(V1–V43 갭·중복 0). prior 라운드 산문을 신뢰하지 않고 billing 4·attendance 1·NHIS 2·`FeeSchedule`/`CopayRate` as-of 2·`GuardianClientRepository` 6·**`GuardianInvitationRepository` 5** = **11 repository 인터페이스 직접 정독** + backing 인덱스/제약 28건(Must 22 + V43 J01 6)을 마이그레이션 SQL `rg`로 줄번호 1:1 물리 확인 — **Must 신규 누락 0건**.
    - **billing/NHIS 물리 확인(14건)**: round 56·59와 동일 — `uq_billing_claims_org_id`(V10:15)·`uq_claim_branch_month`(V1:129)·`idx_billing_claims_org_branch_generated`(V22:61)·`idx_billing_claims_org_branch_status_generated`(V31:14)·`uq_billing_claim_items_claim_client`(V26:18)·`idx_billing_claim_items_claim_created`(V29:33)·`idx_billing_claim_items_org_client_created`(V25:17)·`idx_fee_schedules_org_list`(V27:32)·`idx_fee_schedules_org_grade_effective`(V23:88, + V7 EXCLUDE)·`idx_copay_rates_org_type_effective`(V23:91, + V7 EXCLUDE)·`uq_nhis_batches_org_id`(V8:117)·`idx_nhis_import_batches_org_branch_claim_created`(V37:64) partial + `idx_nhis_import_batches_org_branch_created`(V38:13)·`uq_nhis_import_rows_org_id`(V37:57)·`idx_nhis_import_rows_batch_created`(V28:31).
    - **attendance 물리 확인(8메서드)**: `idx_attendance_daily_list`(V23:76)·`idx_attendance_org_branch_client_date`(V24:27)·집계 partial 4종(V22:73/77/81·V25:24·V26:26)·`idx_attendance_org_client_date`(V24:21). XOR·달력일·시간 정합 CHECK(V4/V11/V14/V15/V37)·`(client_id, attendance_date)` UK(V2) 유지.
    - **J01 `GuardianInvitationRepository` 물리 확인(5메서드)**: `findByTokenHash`→`uq_guardian_invitations_token_hash`(V43:27)·`findByOrganizationIdAndClientIdOrderByCreatedAtDesc`→`idx_guardian_invitations_org_client_created`(V43:69)·`findByIdAndOrganizationIdAndClientId`→`uq_guardian_invitations_org_id`(V43:28) + `client_id` 필터·`existsByOrganizationIdAndClientIdAndRecipientEmailMaskedAndStatus`/`revokePendingByClientAndMaskedEmail`→`idx_guardian_invitations_org_client_pending`(V43:72) partial `WHERE status='PENDING'`(이용자당 PENDING 행 ≤소수 → masked email 필터는 seq scan 허용). purge 인덱스 4종(V43:76/79/83/87) DATA_RETENTION §3 정합.
    - **`GuardianInvitationService` 구현 확인**: `f47ffa1`에 create/list/resend/cancel/accept 구현·`InvitationTokenService` SHA-256·7일 `expires_at`·재발송 PENDING→`REVOKED`·accept TX(`users`+`guardian_clients`+`ACCEPTED`) — V43 CHECK·트리거·FK와 정합.
    - **agents.yaml `core_entities` 11종**: MVP Must(billing·attendance·clients·health·guardians·audit) V1–V42 완비; `guardian_invitations` V43(v1.1, BE-8 커밋 완료); `medications`→`health_records.record_type`; `meal_records`/`activity_programs`→Should(ERD §5); `notifications`→v2(V41/V42).
    - **v2 잔여 후보(V44+, Must 아님)**: ①`guardian_notification_preferences` 복합 FK `(organization_id, guardian_user_id)→users`·`role_code='guardian'` 트리거(V13 패턴) ②J01 `exists`/`revoke` 최적화용 partial `(org, client_id, recipient_email_masked) WHERE status='PENDING'` — 이용자당 PENDING ≤소수라 Must 블로커 아님.
    - **보류 유지**: v1.3-A `transport_runs`/`transport_run_stops`(REQUIREMENTS §3-13) — API_SPEC §transport 미작성 → V44+ 대기. v1.2 P0(`ltc_grade_history`·부분입금/미납) 동일.
    - **결론**: Must 스코프 추가 마이그레이션·CHECK·트리거·스키마 변경 불필요. ERD/DATA_RETENTION 메타 timestamp·§7 round 60 검증 노트 갱신만.

61. **J03 NotificationService 연동 + Must·J01 repository ↔ DDL 물리 재대조 0건 (2026-06-08, round 61, backend `3f9264f`)** — 신규 DBA 호출. backend develop HEAD가 round 60 `f47ffa1` → **`3f9264f`** 1커밋 전진(`feat(v2/J03): NotificationService dispatch skeleton with stub providers`). `git diff f47ffa1..3f9264f` = `NotificationService`·`NotificationEntity`/`Repository`(save-only)·stub Kakao/SMS providers·`AttendanceService` check-in/out `dispatchClientEvent` hook·단위/E2E 테스트 — **`db/migration/` 변경 0건**. prior 라운드 산문을 신뢰하지 않고 billing 4·attendance 1·NHIS 2·`FeeSchedule`/`CopayRate` as-of 2·`GuardianClientRepository` 6·`GuardianInvitationRepository` 5·`GuardianNotificationPreferenceRepository` 1 = **12 repository** 직접 정독 + backing 인덱스/제약 29건 SQL `rg` 물리 확인 — **Must 신규 누락 0건**.
    - **J03 DB 영향**: `NotificationRepository` extends `JpaRepository` only — 커스텀 `@Query`/`findBy*` 없음. `notifications` INSERT는 V2 테이블·V3 `chk_notifications_channel`(`kakao`/`sms`)·`chk_notifications_status`(`PENDING`/`SENT`/`FAILED`)·V10 `fk_notifications_recipient_org`·V7 `fk_notifications_branch_org`·V15 purge `idx_notifications_created`로 충분. quiet hours·event-type 필터는 앱(`NotificationService`/`GuardianPreferenceSnapshot`) — DB 변경 불필요.
    - **Must billing/attendance/NHIS/J01**: round 60 물리 확인(14+8+6건) **변동 없음** — `AttendanceService` hook은 기존 출석 INSERT/UPDATE 후 `NotificationService` 호출만 추가, repository 시그니처·스키마 무관.
    - **agents.yaml `core_entities` 11종**: MVP Must(billing·attendance·clients·health·guardians·audit) V1–V42 완비; `guardian_invitations` V43(v1.1); `notifications` V2+V3 schema + J03 앱 INSERT(v2); `medications`→`health_records.record_type`; `meal_records`/`activity_programs`→Should(ERD §5).
    - **v2 잔여 후보(V44+, Must 아님)**: ①`guardian_notification_preferences` 복합 FK `(organization_id, guardian_user_id)→users`·`role_code='guardian'` 트리거(V13 패턴) ②`notifications` `status='SENT' ⇒ sent_at IS NOT NULL` CHECK(V20 backup·V19 NHIS 패턴) ③J01 `exists`/`revoke` 최적화 partial `(org, client_id, recipient_email_masked) WHERE status='PENDING'`.
    - **보류 유지**: v1.3-A `transport_runs`/`transport_run_stops`(REQUIREMENTS §3-13) — API_SPEC §transport 미작성 → V44+ 대기. v1.2 P0(`ltc_grade_history`·부분입금/미납) 동일.
    - **결론**: Must 스코프 추가 마이그레이션·CHECK·트리거·스키마 변경 불필요. ERD §4-7 notifications J03 메모·DATA_RETENTION §8 dispatch 메모·본 #61 기록 + ERD/DATA_RETENTION 메타 timestamp 갱신만.

62. **V44 Solapi·V45 v2 무결성 + Must repository ↔ DDL 물리 재대조 0건 (2026-06-08, round 62, backend `136239e`)** — 신규 DBA 호출. backend develop HEAD가 round 61 `3f9264f` → **`136239e`** 1커밋 전진(`feat(v2/J03): Solapi alimtalk provider, guardian phone storage, billing notify`). **`V44__users_guardian_phone.sql`** coder 커밋 포함(`UserEntity.phone_*`·`GuardianPhoneResolver`·`applyGuardianPhone`). **V45** round 62 신규: ①`chk_users_phone_pair` ②`chk_notifications_sent_requires_at`·`sent_after_created` ③`fk_guardian_notification_preferences_user_org`+role 트리거 ④`idx_guardian_invitations_org_client_email_pending`. billing 4·attendance 1·NHIS 2·as-of 2·`GuardianClientRepository` 6·`GuardianInvitationRepository` 5·`GuardianNotificationPreferenceRepository` 1 = **12 repository** + Must backing 22건 SQL `rg` — **Must 신규 누락 0건**. `ls db/migration` = **45개** contiguous(V45 untracked — coder 커밋 필요). v1.3-A `transport_runs`·v1.2 P0 — API_SPEC 미확정 → **V46+ 보류**. Flyway migrate 미실행(로컬 PG 인증).

63. **V45 develop 커밋 확인 + BE-11 rate-limit DB 영향 0 + Must DDL 물리 재대조 0건 (2026-06-07, round 63, backend `80bdb1e`)** — 신규 DBA 호출. backend develop HEAD가 round 62 관측 `136239e` → **`80bdb1e`로 2커밋 전진**. `git log`: ① `8d42bdd feat(v1/BE-11): add AuthRateLimitService for login·refresh·password reset` ② `80bdb1e feat(v2): V45 users phone pair·notification prefs FK·sent_at CHECK`. round 62에서 untracked였던 **V45가 `80bdb1e`로 커밋 완료**, `git status` **working tree clean**, `ls V*.sql` = **45개 contiguous**(V1–V45, 버전 갭·중복 0, `sed` 버전번호 1..45 검증).
    - **BE-11 `AuthRateLimitService` DB 영향 = 0**: 파일 직접 정독 — `ConcurrentHashMap<String, Deque<Instant>>` **인메모리 슬라이딩 윈도우**(60초)만 사용, JPA/Repository/엔티티·`db/migration` 변경 없음. 한도값은 `@Value` 설정 주입(`ogada.security.auth-*-rate-limit-per-minute`). 로그인·refresh·비밀번호 재설정 throttling은 **스키마 영향 없음** — 영속 rate-limit 테이블 불필요(분산 환경 요구 시 Redis 등 외부 스토어가 적합, DB 테이블 비권장).
    - **V45 ↔ ERD 정합 재확인**: `chk_users_phone_pair`(V45:10)·`chk_notifications_sent_requires_at`(V45:21)·`chk_notifications_sent_after_created`(V45:25)·`fk_guardian_notification_preferences_user_org`(V45:32)·`trg_guardian_notification_preferences_role_guard`(V45:57)·`idx_guardian_invitations_org_client_email_pending`(V45:66) — DDL 원문 6건 모두 존재, ERD §7-38·§4-2·§4-7·§4-7-1 기재와 일치.
    - **Must billing·attendance·NHIS 물리 재확인**: prior 산문을 신뢰하지 않고 핵심 제약을 `rg` 직접 재확인 — `uq_claim_branch_month`(V1:129)·`uq_billing_claim_items_claim_client`(V26:18)·`chk_billing_claims_amount_sum`(V6:22)·`trg_billing_claims_total_reconciliation`(V11)·`chk_attendance_presence_xor_absence`(V11:22)·`uq_nhis_import_rows_org_id`(V37:37) 모두 DDL 원문 존재. round 60~62 매핑(billing 14·attendance 8·NHIS·as-of·guardian) 변동 없음(`db/migration` 신규 0).
    - **agents.yaml `core_entities` 11종**: MVP Must(billing·attendance·clients·health·guardians·audit) V1–V42 완비; `guardian_invitations` V43(v1.1); `notifications` V2/V3 + V45 SENT CHECK; `medications`→`health_records.record_type='medication'`; `meal_records`/`activity_programs`→Should(ERD §5).
    - **baseline 드리프트(PLN 영역, DBA 미편집)**: `.agents/workspace_baseline.yaml` `backend.develop`이 `136239e`로 기재 — 실측 HEAD `80bdb1e`(2커밋 ahead)와 불일치. `run_agent.py build`가 실측 HEAD로 자동 갱신하거나 PLN이 동기화 권장(rules.md baseline §; DBA 비소유 파일).
    - **보류 유지**: v1.3-A `transport_runs`/`transport_run_stops`(REQUIREMENTS §3-13, 결정 62) — API_SPEC §transport 미작성 → V46+ 대기. v1.2 P0(`ltc_grade_history`·부분입금/미납) 동일 — MVP Must 범위 외.
    - **결론**: V1–V45 contiguous·tree clean, Must repository ↔ DDL 물리 정합, BE-11 rate-limit DB 영향 0. **Must 스코프 추가 마이그레이션·CHECK·트리거·스키마 변경 불필요**(불필요한 V46 회피, rules.md §2/§8/§11). 본 라운드는 검증 기록 + ERD §7 round 63 노트·메타 timestamp 갱신만.

64. **J03 HealthRecordService 알림 연동 + Must repository ↔ DDL 물리 재대조 0건 (2026-06-07, round 65, backend `c221531`)** — 신규 DBA 호출. backend develop HEAD는 round 64와 동일 **`c221531`**(`feat(v2/J03): wire daily care·emergency health notifications and alimtalk E2E tests`). `git diff 80bdb1e..c221531` = `HealthRecordService`·`AttendanceServiceTest`·`HealthRecordServiceTest`·`NotificationAlimtalkDispatchE2eTest` 4건 — **`db/migration/` 변경 0건**. prior 라운드 산문을 신뢰하지 않고 billing 4·attendance 1·NHIS 2·as-of 2·`GuardianClientRepository` 6·`GuardianInvitationRepository` 5·`GuardianNotificationPreferenceRepository` 1·`NotificationRepository`(PK-only) = **13 repository** 직접 정독 + Must 핵심 제약 7건(`uq_claim_branch_month` V1:129·`uq_billing_claim_items_claim_client` V26:18·`chk_billing_claims_amount_sum` V6:22·`trg_billing_claims_total_reconciliation` V11:81·`chk_attendance_presence_xor_absence` V11:22·`uq_nhis_import_rows_org_id` V37:37·`chk_nhis_import_rows_match_requires_client` V19:26) SQL `rg` 물리 확인 — **Must 신규 누락 0건**. `ls V*.sql` = **45개** contiguous(1..45).
    - **J03 디스패치 경로**: `NotificationService.dispatchClientEvent` → `GuardianClientRepository.findByOrganizationIdAndClientIdOrderByPrimaryGuardianDescCreatedAtAsc`(V24 `idx_guardian_clients_org_client`) → `GuardianNotificationPreferenceRepository.findByOrganizationIdAndGuardianUserId`(V41 UK) → `NotificationRepository.save`(PK). `HealthRecordService` medications→`DAILY_CARE`·incident(fall)→`EMERGENCY` — 기존 `health_records` INSERT + V33 actor backstop만, 신규 테이블·인덱스 불필요.
    - **agents.yaml `core_entities` 11종**: MVP Must(billing·attendance·clients·health·guardians·audit) V1–V45 완비; `medications`→`health_records.record_type='medication'`; `meal_records`/`activity_programs`→Should(ERD §5). `notifications` V2 + V45 SENT CHECK.
    - **보류 유지**: v1.3-A `transport_runs`·v1.2 P0(등급 이력·부분입금) — API_SPEC 미확정 → V46+.
    - **결론**: Must 스코프 추가 마이그레이션·CHECK·트리거·스키마 변경 불필요. ERD §8 API §11·J03 디스패치 매핑 3행 보강 + round 65 검증 노트만.

66. **J03 quiet-hours Clock bean + Must repository ↔ DDL 물리 재대조 0건 (2026-06-07, round 66, backend `44e0f02`)** — 신규 DBA 호출. backend develop HEAD가 round 65 `c221531` → **`44e0f02`** 1커밋 전진(`Ensure quiet hours clock is provided and add coverage`). `git diff c221531..44e0f02` = `NotificationConfig`(Asia/Seoul `Clock` bean)·`NotificationConfigTest`·`GlobalExceptionHandler`·`SecurityConfig` 4건 — **`db/migration/` 변경 0건**. quiet hours는 `NotificationService` 앱 로직 + `@Value` 설정(`ogada.notification.quiet-hours-*`) — DB 테이블·컬럼·인덱스 불필요(DATA_RETENTION §8·ERD §4-7과 정합). prior 라운드 산문을 신뢰하지 않고 billing 4·attendance 8·NHIS 2·as-of 2·`GuardianClientRepository` 6·`GuardianInvitationRepository` 5·`GuardianNotificationPreferenceRepository` 1·`NotificationRepository`(PK-only) = **13 repository** 직접 정독 + Must 핵심 제약 7건(`uq_claim_branch_month` V1:129·`uq_billing_claim_items_claim_client` V26:18·`chk_billing_claims_amount_sum` V6:22·`trg_billing_claims_total_reconciliation` V11:81·`chk_attendance_presence_xor_absence` V11:22·`uq_nhis_import_rows_org_id` V37:37·`chk_nhis_import_rows_match_requires_client` V19:26) SQL `rg` 물리 확인 — **Must 신규 누락 0건**. `ls V*.sql` = **45개** contiguous(1..45).
    - **agents.yaml `core_entities` 11종**: MVP Must(billing·attendance·clients·health·guardians·audit·notifications) V1–V45 완비; `medications`→`health_records.record_type='medication'`; `meal_records`/`activity_programs`→Should(ERD §5).
    - **보류 유지**: v1.3-A `transport_runs`/`transport_run_stops`(REQUIREMENTS §3-13) — API_SPEC §transport 미작성 → V46+ 대기. v1.2 P0(등급 이력·부분입금/미납) 동일.
    - **결론**: Must 스코프 추가 마이그레이션·CHECK·트리거·스키마 변경 불필요(불필요한 V46 회피, rules.md §2/§8/§11). ERD §7 round 66 검증 노트 + 본 항목만.

67. **J03 투약 DAILY_CARE 알림 연동 + Must repository ↔ DDL 물리 재대조 0건 (2026-06-08, round 67, backend `78e8928`)** — 신규 DBA 호출. backend develop HEAD가 round 66 `44e0f02` → **`78e8928`** 1커밋 전진(`feat(v2/J03): dispatch DAILY_CARE alimtalk on medication records`). `git diff 44e0f02..78e8928` = `HealthRecordService`·`HealthRecordServiceTest` 2건 — **`db/migration/` 변경 0건**. `createMedication`이 `dispatchHealthNotification(DAILY_CARE)` 호출 — 기존 `health_records` INSERT + V33 `trg_health_records_set_recorded_by`·V41 UK·V45 prefs FK/role·`notifications` INSERT(V45 SENT CHECK) 경로만 사용, 신규 테이블·인덱스 불필요. prior 라운드 산문을 신뢰하지 않고 billing 4·attendance 8·NHIS 2·as-of 2·`GuardianClientRepository` 6·`GuardianInvitationRepository` 5·`GuardianNotificationPreferenceRepository` 1·`NotificationRepository`(PK-only) = **13 repository** 직접 정독 + Must 핵심 제약 7건(`uq_claim_branch_month` V1:129·`uq_billing_claim_items_claim_client` V26:18·`chk_billing_claims_amount_sum` V6:22·`trg_billing_claims_total_reconciliation` V11:81·`chk_attendance_presence_xor_absence` V11:22·`uq_nhis_import_rows_org_id` V37:37·`chk_nhis_import_rows_match_requires_client` V19:26) SQL `rg` 물리 확인 — **Must 신규 누락 0건**. `ls V*.sql` = **45개** contiguous(1..45), working tree clean.
    - **agents.yaml `core_entities` 11종**: MVP Must(billing·attendance·clients·health·guardians·audit·notifications) V1–V45 완비; `medications`→`health_records.record_type='medication'`; `meal_records`/`activity_programs`→Should(ERD §5).
    - **보류 유지**: v1.3-A `transport_runs`/`transport_run_stops`(REQUIREMENTS §3-13) — API_SPEC §transport 미작성 → V46+ 대기. v1.2 P0(등급 이력·부분입금/미납) 동일.
    - **결론**: Must 스코프 추가 마이그레이션·CHECK·트리거·스키마 변경 불필요. ERD §7 round 67 검증 노트 + 본 #67 기록만.

68. **V46 develop 커밋 확인 + Must repository ↔ DDL 물리 재대조 0건 (2026-06-07, round 69, backend `8ce1151`)** — 신규 DBA 호출. backend develop HEAD가 round 68 관측 `c53dd3b`(V46 untracked) → **`8ce1151`로 1커밋 전진** (`feat(v2/J03): add notification history query index (V46)`). round 68 untracked 산물이 develop HEAD에 정상 커밋 — `git status` clean, `ls db/migration | wc -l` = **46개 contiguous**(버전번호 1..46 `sed` 검증, 갭·중복 0). `git diff c53dd3b..8ce1151` = `V46__notification_history_query_index.sql` **1파일 신규**(9줄: 헤더 주석 + `CREATE INDEX idx_notifications_org_recipient_created ON notifications (organization_id, recipient_user_id, created_at DESC)`) — 신규 테이블·컬럼·CHECK·트리거 0건, ALTER 0건.
    - **prior 결론 신뢰 안 함**: 16 repository 인터페이스 직접 정독(`BillingClaim` 4·`BillingClaimItem` 3·`FeeSchedule` 4·`CopayRate` 3·`NhisImportBatch` 2·`NhisImportRow` 2·`Attendance` 8·`BranchQrToken` 1·`Client` 8·`GuardianClient` 5·`HealthRecord` 4·`GuardianInvitation` 5·`GuardianNotificationPreference` 1·`Notification` 2·`User`/`UserBranch`/`Branch`/`Organization`·토큰·로그인·백업·audit) + Must 핵심 제약 7건(`uq_claim_branch_month` V1:129·`uq_billing_claim_items_claim_client` V26:18·`chk_billing_claims_amount_sum` V6:22·`trg_billing_claims_total_reconciliation` V11:81·`chk_attendance_presence_xor_absence` V11:22·`uq_nhis_import_rows_org_id` V37:37·`chk_nhis_import_rows_match_requires_client` V19:26) + V46 인덱스 SQL `rg` 줄번호 1:1 물리 확인 — **Must billing·attendance·clients·health·guardians·audit·notifications 신규 누락 0건**.
    - **`NotificationRepository` 매핑**: `findByOrganizationIdAndRecipientUserIdOrderByCreatedAtDesc(org, recipient, Pageable)` + `…RecipientUserIdInOrderByCreatedAtDesc(org, recipientIds, Pageable)` → V46 `idx_notifications_org_recipient_created (organization_id, recipient_user_id, created_at DESC)` Tenant 스코프 페이지네이션. V2 `idx_notifications_recipient`(recipient만)·`idx_notifications_org_created`(recipient 없음)는 보조 인덱스로 유지 — `IN`-list 매칭 시 PG planner가 V46 prefix `(org, recipient)` exact-match를 우선 사용.
    - **agents.yaml `core_entities` 11종 재대조**: `users` V1+V44+V45·`clients` V1+·`guardians`(=`guardian_clients` V2+`guardian_invitations` V43+`guardian_notification_preferences` V41+V42+V45)·`attendance` V1+·`health_records` V1+(`medications` polymorphic via `record_type='medication'`)·`billing`(=`billing_claims`+`billing_claim_items`+`fee_schedules`+`copay_rates`+`nhis_import_batches`+`nhis_import_rows`+`billing_claim_status_history`) V1+·`audit_logs` V1+·`notifications` V2+V45+V46 — **MVP Must 전부 충족**. `meal_records`·`activity_programs`는 ERD §5 v1 후속(REQUIREMENTS §3-5/§3-6 미Must, ROADMAP v1 명시 제외 유지).
    - **보류 유지**: v1.3-A `transport_runs`/`transport_run_stops`(REQUIREMENTS §3-13) — API_SPEC §transport 미작성 → V47+ 대기. v1.2 P0(등급 이력·부분입금/미납) 동일.
    - **결론**: V46 develop HEAD 정상 커밋, Must 스코프 추가 마이그레이션·CHECK·트리거·스키마 변경 불필요. ERD §7-39(V46) round 69 commit 확인 노트 + ERD §7 검증 상태 round 69 entry + ERD/DATA_RETENTION 메타 timestamp 갱신만(2026-06-07T22:15+09:00).

70. **J03 vitals DAILY_CARE 알림 연동 + Must repository ↔ DDL 물리 재대조 0건 (2026-06-08, round 70, backend `0832fbf`)** — 신규 DBA 호출. backend develop HEAD가 round 69 `8ce1151` → **`0832fbf`** 1커밋 전진(`feat(v2/J03): dispatch DAILY_CARE notifications for vitals`). `git diff 8ce1151..0832fbf` = `HealthRecordService`·`HealthRecordServiceTest` 2건 — **`db/migration/` 변경 0건**. `createVitals`가 `dispatchHealthNotification(DAILY_CARE)` 호출 — 기존 `health_records` INSERT + V33 actor backstop + V41/V45 prefs + `notifications` INSERT(V45 SENT CHECK) 경로만 사용, 신규 테이블·인덱스 불필요. prior 라운드 산문을 신뢰하지 않고 24 repository 인터페이스 직접 정독 + Must 핵심 제약 7건 SQL `rg` 물리 확인 — **Must billing·attendance·clients·health·guardians·audit·notifications 신규 누락 0건**.
    - **마이그레이션 연속성**: V1–V46 46개 contiguous(갭·중복 0). `git status` backend submodule **CLEAN**.
    - **Must billing/attendance**: round 69 물리 확인(14+8+6건) **변동 없음** — `uq_claim_branch_month`·`uq_billing_claim_items_claim_client`·XOR·NHIS UK·status reconciliation 트리거 유지.
    - **J03 health dispatch 완성도**: vitals(`0832fbf`)·medications(`78e8928`)·notes/incidents(`c221531`) — 모두 `health_records` polymorphic + `notifications` 이력(V46 인덱스). ERD §8 J03 매핑 vitals/notes 행 분리 보강.
    - **agents.yaml `core_entities`**: 11종 전부 충족. `meal_records`·`activity_programs`는 ERD §5 v1 후속(REQUIREMENTS §3-5/§3-6 미Must).
    - **보류 유지**: v1.3-A `transport_runs`/`transport_run_stops`(REQUIREMENTS §3-13) — API_SPEC §transport 미작성 → V47+ 대기. v1.2 P0(등급 이력·부분입금/미납) 동일.
    - **결론**: Must 스코프 추가 마이그레이션·CHECK·트리거·스키마 변경 불필요(불필요한 V47 회피, rules.md §2/§8/§11). ERD §7-40 round 70 검증 노트 + ERD/DATA_RETENTION 메타 timestamp 갱신만.

71. **J03 alimtalk E2E 테스트 + Must billing·attendance 재대조 0건 (2026-06-08, round 71, backend `32a1f8f`)** — 신규 DBA 호출. backend develop HEAD가 round 70 `0832fbf` → **`32a1f8f`** 1커밋 전진(`feat(v2/J03): add service-layer alimtalk flow E2E tests`). `git diff 0832fbf..32a1f8f` = Java E2E 테스트만 — **`db/migration/` 변경 0건**. J03 알림 디스patch 경로는 기존 `health_records`·`attendance`·`guardian_notification_preferences`(V41+V45)·`notifications`(V45 SENT CHECK + V46 history index)만 사용 — 신규 테이블·인덱스 불필요.
    - **Must billing·attendance**: ERD·API_SPEC §5·§7 대조 — `attendance`(UK·XOR·temporal·billing partial)·`billing_claims`(status DRAFT/CONFIRMED/PAID·확정 불변)·`billing_claim_items`(스냅샷·UK)·`fee_schedules`/`copay_rates`(as-of)·NHIS reconciliation(V19–V22·V37–V38) **전부 V1–V46에 존재**. Must 핵심 제약 7건 + V46 `idx_notifications_org_recipient_created` SQL `rg` 물리 재확인 — **신규 누락 0건**.
    - **agents.yaml `core_entities`**: 11종 MVP Must 충족. `meal_records`·`activity_programs`는 Should(v1 후속).
    - **보류 유지**: v1.3-A `transport_runs`/`transport_run_stops`(REQUIREMENTS §3-13) — API_SPEC §transport 미작성 → V47+ 대기. v1.2 P0(`ltc_grade_history`·부분입금/미납, Epic L/M) — PLN API_SPEC 계약 확정 후.
    - **결론**: Must 스코프 추가 마이그레이션 불필요. ERD §7-41 round 71 검증 노트 + ERD/DATA_RETENTION 메타 timestamp 갱신만.

72. **J03 Solapi template 변수 매핑 + Must billing·attendance 재대조 0건 (2026-06-08, round 72, backend `4c74f84`)** — 신규 DBA 호출. backend develop HEAD가 round 71 `32a1f8f` → **`4c74f84`** 1커밋 전진(`feat(v2/J03): map alimtalk payload to Solapi template variables`). `git diff 32a1f8f..4c74f84` = `AlimtalkTemplateVariables`·`SolapiKakaoAlimtalkProvider`·테스트 6파일 — **`db/migration/` 변경 0건**. Solapi 발송 시 `notifications.payload` JSON→템플릿 변수 변환은 앱 레이어 전용 — 기존 `notifications`(V2+V45 SENT CHECK+V46 history index) 스키마로 충분.
    - **Must billing·attendance**: ERD·API_SPEC §5·§7 대조 — round 71과 동일, Must 핵심 제약 7건 + V46 `idx_notifications_org_recipient_created` SQL `rg` 물리 재확인 — **신규 누락 0건**.
    - **agents.yaml `core_entities`**: 11종 MVP Must 충족. `meal_records`·`activity_programs`는 Should(v1 후속).
    - **보류 유지**: v1.3-A `transport_runs`/`transport_run_stops`(REQUIREMENTS §3-13) — API_SPEC §transport 미작성 → V47+ 대기. v1.2 P0(`ltc_grade_history`·부분입금/미납, Epic L/M) — PLN API_SPEC 계약 확정 후.
    - **결론**: Must 스코프 추가 마이그레이션 불필요. ERD §7-42 round 72 검증 노트 + ERD/DATA_RETENTION 메타 timestamp 갱신만.

73. **J03 alimtalk SMS fallback relay + Must billing·attendance 재대조 0건 (2026-06-08, round 73, backend `ac17ad8`)** — 신규 DBA 호출. backend develop HEAD가 round 72 `4c74f84` → **`ac17ad8`** 1커밋 전진(`feat(v2/J03): add Korean SMS fallback text for alimtalk relay`). `git diff 4c74f84..ac17ad8` = `AlimtalkFallbackText`·`SolapiKakaoAlimtalkProvider`·`SolapiSmsProvider`·테스트 7파일 — **`db/migration/` 변경 0건**. 카카오 발송 실패 시 SMS 대체 문구·Solapi SMS API 호출은 앱 레이어 전용 — 기존 `notifications`(V2+V45 SENT CHECK+V46 history index)·V44 `users.phone_*`·V41/V45 prefs 스키마로 충분.
    - **Must billing·attendance**: ERD·API_SPEC §5·§7 대조 — round 72와 동일, Must 핵심 제약 7건 + V46 `idx_notifications_org_recipient_created` SQL `rg` 물리 재확인 — **신규 누락 0건**.
    - **agents.yaml `core_entities`**: 11종 MVP Must 충족. `medications`=`health_records.record_type='medication'`·`meal_records`·`activity_programs`는 Should(v1 후속).
    - **보류 유지**: v1.3-A `transport_runs`/`transport_run_stops`(REQUIREMENTS §3-13) — API_SPEC §transport 미작성 → V47+ 대기. v1.2 P0(`ltc_grade_history`·부분입금/미납, Epic L/M) — PLN API_SPEC 계약 확정 후.
    - **결론**: Must 스코프 추가 마이그레이션 불필요. ERD §7-43 round 73 검증 노트 + ERD/DATA_RETENTION 메타 timestamp 갱신만.

74. **v1.3-A transport(V47) + v1.2 등급 이력(V48) + Must billing·attendance 재대조 (2026-06-08, round 74, backend `52e0621`)** — DBA 호출. API_SPEC §12 transport 계약 확정(60차)·frontend `e8d1854` UI shell 선행 → **V47** 작성.
    - **V47**: `clients` 배차 컬럼(`uses_transport`·주소/픽업/좌표/검증 메타)·`transport_runs`(DRAFT|CONFIRMED·UK branch×date×PICKUP)·`transport_run_stops`(≤15·geocode_status)·트리거(명단 자격·Tenant/branch 복사·actor backstop).
    - **V48**: `client_ltc_grade_history` + `trg_clients_ltc_grade_history` — US-M01. API_SPEC 엔드포인트 미작성이나 USER_STORIES 인수 조건 명확.
    - **Must billing·attendance**: V1–V46 대조 — 핵심 제약 7건 유지, **신규 누락 0건**.
    - **보류**: v1.2 Epic L 부분입금(`billing_payments`) — API_SPEC·US-L01 미확정 → **V50+ 보류**(아래 #74-1).

75. **V49 v3 meals/programs + Must billing·attendance 재대조 0건 (2026-06-08, round 75, backend `53a1ffe`)** — Must billing·attendance·NHIS 핵심 제약 7건 SQL `rg` 물리 재확인 — **Must 신규 누락 0건**. **V49** `meal_menus`·`meal_records`·`activity_programs`·`program_participations` 4테이블 신규(API §13·frontend `7ef1083`·`config/meals.js`/`programs.js` enum 정합). agents.yaml `core_entities` `meal_records`·`activity_programs` **V49 충족**. ERD §4-11·§8·DATA_RETENTION §3 갱신. **coder**: `MealService`/`ProgramService`·JPA·`MustApiEndpointRoutingTest` §13·`mvn flyway:migrate` 검증.

### [DBA] DB 설계 질문

#### #172. V167 G-BILLING-OVERDUE-ADJUSTMENT 신규 + V168 defense-in-depth integrity (2026-06-21, round 184, backend `b583c11`)
- **배경**: round 183(#171 — G-BATHING 전월 일정 복사·G21 dashboard gap count·신규 V167 불요, backend `49a1721`) → backend HEAD **`b583c11`** 7 commit 전진 — `4d92844` **V167** `billing_overdue_management_records`·`billing_overdue_adjustments` 신규(케어포 PDF p.89 7-3 미납관리 ②③④⑤ parity)·`c17097d` live API routing/RBAC 테스트·`f6266ec` overdue SMS 자동 등록 scope 가드(앱)·`a426663` G-BATHING copy 라우팅 테스트·`b583c11` G-STAFF-DOCUMENT-REPOSITORY 21-slot progress API(앱).
- **`git diff --name-only 49a1721..b583c11 -- src/main/resources/db/migration/`** = **`V167__billing_overdue_management_and_adjustments.sql` 1파일**. `… -- '**/*Entity.java' '**/*Repository.java'` = **`OverdueManagementRecordEntity.java`·`OverdueAdjustmentEntity.java`·`OverdueManagementRecordRepository.java`·`OverdueAdjustmentRepository.java` 4파일** (V167 짝). G-STAFF-DOCUMENT-REPOSITORY는 `StaffDocumentRepositoryCompliance` 도메인 객체·`StaffHrFileService` 인메모리 progress 집계 — V91 `staff_hr_files` 위 read-only, 신규 DDL 0건.
- **V167 검토 (coder 소유 — DBA confirmation)**:
  - `billing_overdue_management_records` (회수 CRM 대장 — 케어포 p.89 ②③⑤): contact_method enum CHECK(PHONE|SMS|OTHER)·`(org, claim, client, recorded_at DESC)` 인덱스 1개. 비공백 CHECK·Tenant FK·temporal CHECK 0건.
  - `billing_overdue_adjustments` (금액 조정 audit — 케어포 p.89 ④): adjustment_type enum CHECK(PARTIAL|FULL_WRITE_OFF)·`previous/adjusted_amount >= 0 AND adjusted ≤ previous` CHECK·`(org, claim, client, recorded_at DESC)` 인덱스 1개. 비공백 CHECK·Tenant FK·temporal CHECK 0건.
  - V158 cash-receipt(`length(trim()) > 0` × 3·Tenant FK × 3) / V164 client_care_plan_forms(`length(trim()) > 0` × 9·Tenant FK × 4) / V165 user_account_requests(`length(trim()) > 0` × 3·Tenant FK × 3) 패턴 대비 **defense-in-depth 비대칭**.
  - 트리거: `OverdueManagementService.{createManagementRecord,createAdjustment,recordAutomaticSmsRemindersForClaim}` 가 비공백·길이·`requireActorUserId`·`claim.getBranchId()` 동기화를 앱에서 강제하나, raw SQL·향후 batch import(NHIS 배치 미납 회수 자동화·G-7-1 명세 dispatch 후 자동 등록 확장)로 우회 적재 시 ① 빈 note/reason ② 미래 `recorded_at` ③ cross-tenant 사용자/지점/이용자/청구 참조 가능.
- **DBA 신규 V168** — V167 비대칭 일괄 해소 (V94/V117/V164/V165 패턴):
  - `chk_billing_overdue_mgmt_note_nonempty` / `chk_billing_overdue_adj_reason_nonempty` (length(trim()) > 0)
  - `chk_billing_overdue_mgmt_recorded_at_after_created` / `chk_billing_overdue_adj_recorded_at_after_created` (recorded_at >= created_at — V94/V96/V117 패턴)
  - **8 Tenant FK pairs** (각 테이블 4쌍): `(org, branch_id) → branches`·`(org, claim_id) → billing_claims`·`(org, client_id) → clients`·`(org, recorded_by) → users` (anchor: `uq_branches_org_id` V4·`uq_billing_claims_org_id` V10·`uq_clients_org_id` V5/V8·`uq_users_org_id` V5)
  - **4 backing index**: `idx_*_client_purge` on `(client_id)` (V117 보존 패턴 — `clients` 퇴소 후 보존기간 만료 일괄 삭제 backing) + `idx_*_org_recorded_by` on `(organization_id, recorded_by)` (V117 audit 패턴 — `users` 퇴직 시 본 사용자 작성 회수 기록 조회 backing). V167의 NOT NULL 컬럼이라 partial 인덱스 WHERE 절 불요.
  - single-additive `ALTER TABLE`·`CREATE INDEX` only — 신규 컬럼·트리거 0건.
- **의도적 제외 (P3 carry — 다음 라운드 재평가)**:
  - **활성 이용자 INSERT guard** (V164 `trg_*_guard_active_client` 패턴) — 미납 회수·금액 조정은 이용자 퇴소(`is_active=false` / `discharged_at`) 이후에도 수행되어야 하는 회계 lifecycle 의 일부. guard 추가 시 정당한 회수·조정 흐름을 차단.
  - **recorded_by 자동 채움 트리거** (V32 `ogada_read_actor_user_id` 패턴) — V167 에서 `recorded_by NOT NULL` + 서비스가 항상 `requireActorUserId()` 로 채움. Tenant FK pair 가 cross-tenant 사용자 차단.
  - **`(org, claim_id, client_id) → billing_claim_items` 복합 FK** — `OverdueManagementService.requireClaimItem` 가 `findByClaimIdAndClientId` 조회로 강제. plain CHECK 로 subquery 표현 불가.
  - **`previous_amount`/`adjusted_amount` ↔ `billing_claim_items.copay_amount` cross-table 일치** — `recalculateClaimCopayAmount` 시점에 `billing_claims.copay_amount` 가 합계와 일치해야 하나, 시점 의존·subquery 필요 → immutable CHECK 표현 불가. 앱 책임 (#161 reciprocal pair CHECK·#164 cash-receipt amount==copay P2 보류와 동일 정책).
- **안전성**: V167 round 184 최초 도입 — 운영 적재 0건 시점에 즉시 V168 closure. 모든 CHECK immutable·NULL 분기 명시·기존 NOT NULL 컬럼 위 Tenant FK 쌍이라 backfill 불요.
- **검증 결과**:
  - `mvn flyway:migrate` (로컬 PG14, dev DB) → V165→V166→V167→V168 순서 적용 PASS, `flyway_schema_history.success=t`.
  - `mvn flyway:validate` → **Successfully validated 168 migrations** (V1–V168 contiguous, 갭·중복 0).
  - **로컬 PG14 SAVEPOINT 검증 5 negative + 2 positive PASS**:
    - 정상 INSERT (mgmt + adj) — `INSERT 0 1` × 2.
    - 빈 `note` (공백 trim) → `chk_billing_overdue_mgmt_note_nonempty` REJECT.
    - `recorded_at = now() - interval '1 hour'` → `chk_billing_overdue_mgmt_recorded_at_after_created` REJECT.
    - cross-tenant `branch_id` (다른 org 의 branch) → `fk_billing_overdue_mgmt_branch_org` REJECT.
    - cross-tenant `recorded_by` (다른 org 의 user) → `fk_billing_overdue_mgmt_recorded_by_org` REJECT.
    - 빈 `reason` → `chk_billing_overdue_adj_reason_nonempty` REJECT.
  - `mvn test -Dtest='OverdueManagementServiceTest,OverdueManagementLiveApiRoutingE2eTest'` → **12/12 PASS**.
  - `mvn test -Dtest='*Billing*Test,*Overdue*Test'` → **131/131 PASS**.
- **Must billing·attendance·NHIS 핵심 제약 7건** SQL 물리 재확인 → **전부 불변** (`uq_claim_branch_month` V1·`uq_billing_claim_items_claim_client` V26·`chk_billing_claims_amount_sum` V6·`trg_billing_claims_total_reconciliation` V11·`chk_attendance_presence_xor_absence` V11/V14·`uq_nhis_import_rows_org_id` V37·`chk_nhis_import_rows_match_requires_client` V19→V54). agents.yaml `core_entities` 11종 전수 충족(`billing` V167+V168 추가).
- **`ls db/migration | wc -l` = 168** contiguous(V1–V168, 갭·중복 0).
- **결론**: V168 신규 1건. ERD §1 round 184 행·메타 timestamp 갱신·`billing` core_entity 비고에 V167+V168 추가. **보류 carry**(전 라운드 동일 + 본 라운드 신규): V167 활성 이용자 guard(P3 — 회계 lifecycle)·V167 cross-table copay 일치(P2 — 앱 책임)·V166 `is_active` pairing(P3)·V162 `branch_ids` 요소 UUID(P3)·현금영수증 cross-table/time(P2)·PLAN↔BILLING reciprocal(P2)·이동서비스일지④ 시간 tolerance(P2)·`staff_attendance`/`staff_schedules`(Should)·`billing_payments`(Epic L). **coder 전달**: V168 commit 후 `git push origin develop` (run_agent.py build 자동 push)·`OverdueManagementSchemaReadinessProbe`(round 180 V165 / round 173 V157 / round 176 V159 / round 178 V164 패턴) 후속 추가 권장 — `pg_constraint` 에서 `chk_billing_overdue_mgmt_note_nonempty`·`fk_billing_overdue_adj_branch_org` 존재 boolean 노출, `HealthController.isOperationReady`/`/live-e2e/probe` gate 와이어. `mvn test`·`mvn flyway:migrate` 결과는 본 라운드 검증 PASS — coder 추가 검증 불요.

#### #171. G-BATHING 전월 일정 복사 · G21 대시보드 NHIS gap count 검토 · 신규 V167 불요 (2026-06-21, round 183, backend `49a1721`)
- **배경**: round 182(#170 — G-BILLING 리포트 필터·신규 V167 불요, backend `7b99313`) → backend HEAD **`49a1721`** 4 commit 전진 — `49a1721` **G-BATHING `POST /api/v1/care/bathing-schedules/copy-from-previous-month`**(케어포 module3 3-3 전월 일정 불러 일괄생성)·`0796821` **G21 대시보드 `nhisComparisonGapCount` 노출**·`ad11fda` notification quiet-hours 테스트 deepen·`0c9518a` live-e2e bootstrap blocker 우선순위. **전부 앱 only**(`care/bathschedule`·`dashboard`·`system` 패키지 + 테스트).
- **`git diff --name-only 7b99313..49a1721 -- src/main/resources/db/migration/`** = **0파일**. **`… -- '**/*Entity.java' '**/*Repository.java'`** = **0파일**. **`git diff 7b99313..49a1721 | grep -iE 'CREATE TABLE|ALTER TABLE|@Entity|@Column|@Table'`** = **0건**. `ls db/migration | wc -l` = **166** contiguous(V1–V166, 갭·중복 0).
- **G-BATHING copy DB backing 대조** (신규 인덱스 0건):
  - ① **전월 소스 적재** — `BathingScheduleRepository.findByOrganizationIdAndBranchIdAndScheduledDateBetweenOrderByScheduledDateDescScheduledTimeDescCreatedAtDescClientIdAsc` → V136 `idx_bathing_schedules_org_branch_scheduled_date`.
  - ② **대상월 occupied keys** — 동일 메서드로 대상월 범위 적재 후 `clientId|scheduledDate` 키셋 **인메모리** 구성.
  - ③ **신규 행 INSERT** — `save` → V136 UK `(organization_id, client_id, scheduled_date)` + domain CHECK. copy는 `SCHEDULED`만 생성·소스 `CANCELLED`/`SKIPPED` skip·UK 충돌 skip·`mapToTargetMonthDate` 말일 clamp는 앱 도메인.
- **G21 dashboard `nhisComparisonGapCount` DB backing** (신규 인덱스 0건): `DashboardService`→`VisitService.getNhisComparison`(V53/V38/V28/V5 기존 인덱스) 결과를 `countNhisComparisonGapLines`로 **인메모리** 집계 — 신규 `@Query`·DDL 0건.
- **Must billing·attendance·NHIS 핵심 제약 7건** SQL 물리 재확인 — **전부 불변**. agents.yaml `core_entities` 11종 전수 충족.
- **결론**: **신규 V167 불요** — G-BATHING copy·G21 dashboard gap는 기존 `bathing_schedules`(V136)·visit/NHIS import 인덱스 위 읽기/INSERT 전용. ERD §1 round 183·§8 copy-from-previous-month·§7 검증 헤더 + 메타 timestamp + 본 #171. **보류 carry**(전 라운드 동일): V166 `is_active` pairing(P3)·V162 `branch_ids` 요소 UUID(P3)·현금영수증 cross-table/time(P2)·PLAN↔BILLING reciprocal(P2)·이동서비스일지④ 시간 tolerance(P2)·`staff_attendance`/`staff_schedules`(Should)·`billing_payments`(Epic L). **coder**: 추가 DDL 0건 — G-BATHING FE wire P2는 스키마 영향 없음.

#### #170. G-BILLING 대장 리포트 반월·기준 필터 검토 · 신규 V167 불요 (2026-06-21, round 182, backend `7b99313`)
- **배경**: round 181(#169 — V166 `ON_LEAVE` lifecycle 검토·신규 V167 불요, backend `1d7cee2`) → backend HEAD **`7b99313`** 4 commit 전진 — `b96d038` **입금대장 반월(`FULL`/`FIRST_HALF`/`SECOND_HALF`)·수납대장 기준(`PAYMENT`/`CLAIM`) 필터**(`GET /billing/reports/{variant}`, 케어포 PDF p.91 parity)·`375fb9d` 리포트 필터 달력월 검증(앱)·`14935a3` 적용 필터 echo(앱)·`7b99313` 필터 단언 테스트(테스트 only). **전부 앱 only**(`billing` 패키지 + 테스트).
- **`git diff --name-only 1d7cee2..7b99313 -- src/main/resources/db/migration/`** = **0파일**. **`… -- '**/*Entity.java' '**/*Repository.java'`** = **0파일**. **`git diff 1d7cee2..7b99313 | grep -iE 'CREATE TABLE|ALTER TABLE|@Entity|@Column|@Table'`** = **0건**(신규 테이블·컬럼·엔티티·레포지토리 0건). `ls db/migration | wc -l` = **166** contiguous(V1–V166, 갭·중복 0).
- **신규 필터 DB backing 대조** (신규 인덱스 0건):
  - ① **입금대장 반월 필터** (`period`) — `BillingService.buildPaymentReportItems`가 `billingClaimRepository.findByOrganizationIdAndBranchIdAndStatusOrderByPaidAtDesc(org, branch, PAID)`로 적재 후 `matchesDepositPeriod(claim.getPaidAt(), targetMonth, period)`로 **인메모리** 분기(`FIRST_HALF`=일자 1–15·`SECOND_HALF`=16–말). 적재 쿼리는 V153 `idx_billing_claims_org_branch_status_paid_at`(partial PAID·`paid_at DESC`)로 backing — `period`는 DB 술어가 아닌 인메모리 필터라 전용 인덱스 불요.
  - ② **수납대장 기준 필터** (`basis`) — 동일 PAID 적재 행을 `matchesReceiptLedgerMonth(claim, targetMonth, basis)`로 **인메모리** 분기(`PAYMENT`=수납월·`CLAIM`=청구년월). `basis=CLAIM` 시 영수증번호(`formatReceiptNo`) 미노출 — claim 컬럼 기반, `cash_receipt_issuances` 조인 없음. V153 backing 그대로.
  - ③ **청구대장**(`charges`)은 본 라운드 변경 없음 — `findByOrganizationIdAndBranchIdAndYearMonthOrderByGeneratedAtDesc`(V149 `(org, branch, year_month DESC, status, generated_at DESC)` + V1 `idx_billing_claims_org_branch_month`) 불변.
- **Must billing·attendance·NHIS 핵심 제약 7건** SQL 물리 재확인 — **전부 불변**(`uq_claim_branch_month` V1·`uq_billing_claim_items_claim_client` V26·`chk_billing_claims_amount_sum` V6·`trg_billing_claims_total_reconciliation` V11·`chk_attendance_presence_xor_absence` V11/V14·`uq_nhis_import_rows_org_id` V37·`chk_nhis_import_rows_match_requires_client` V19→V54). agents.yaml `core_entities` 11종 전수 충족.
- **결론**: **신규 V167 불요** — 반월·기준 필터는 전부 인메모리 분기이고, 기존 적재 쿼리(V153/V149/V1)가 정렬·범위를 모두 backing. ERD §1 round 182 행·§7-81 검증 헤더·§8 deposits/receipts 매핑 + 메타 timestamp + 본 #170. **보류 carry**(전 라운드 동일): V166 `is_active` pairing(P3)·V162 `branch_ids` 요소 UUID(P3)·현금영수증 cross-table(`amount==copay`)/time(`issued_at`)(P2 — 앱 책임)·PLAN↔BILLING reciprocal pair CHECK(P2)·이동서비스일지④ 시간 tolerance(P2)·`staff_attendance`/`staff_schedules`(Should)·`billing_payments`(Epic L). **coder**: 추가 DDL 0건 — 스키마 영향 없음.

#### #169. V166 `ON_LEAVE` lifecycle 검토 · lifecycle summary API · 신규 V167 불요 (2026-06-21, round 181, backend `1d7cee2`)
- **배경**: round 180(#168 — V165 후속 live-e2e probe·신규 DDL 0건, backend `7d29a38`) → backend HEAD **`1d7cee2`** 6 commit 전진 — `68d4457` **V166 `staff_leave_status_on_leave.sql`**(coder·G-STAFF-LEAVE-STATUS FAQ 21720)·`2edbdc4` NHIS processing-status header parsing(앱 only)·`6ed7cd4` G-BANK-EXCEL-8 row guard(앱 only)·`1d7cee2` **lifecycle summary API**(`StaffLifecycleSummaryController`·`GET /api/v1/staff/lifecycle-summary` `onLeaveCount`).
- **`git diff --name-only 7d29a38..1d7cee2 -- src/main/resources/db/migration/`** = **V166 1파일**. **`… -- '**/*Entity.java' '**/*Repository.java'`** = **0파일**. **`CREATE TABLE|ALTER TABLE` grep(V166 제외)** = **0건**. `ls db/migration | wc -l` = **166** contiguous(V1–V166, 갭·중복 0).
- **V166 검토 (coder 소유, DBA confirmation)**:
  - `chk_users_lifecycle_status` enum 5값(`ON_LEAVE` 추가) — V86 4값 CHECK 교체.
  - `chk_users_on_leave_requires_hired_at` — `ON_LEAVE` → `hired_at` NOT NULL.
  - `chk_users_on_leave_no_termination_date` — `ON_LEAVE` → `terminated_at` NULL.
  - V87 temporal/state pair-CHECK 패턴으로 `UserService.validateLifecycleState()` ON_LEAVE 가드 DB 미러 — well-formed.
  - **의도적 제외**: `is_active=false` pairing — 앱(`UserService` ON_LEAVE 전이·`StaffTrainingLogService` ON_LEAVE 제외) 책임. TERMINATED도 DB 미강제 → V167 추가 불요(P3 carry).
- **lifecycle summary API DB backing** (신규 인덱스 0건): `userRepository.findByOrganizationId` + `user_branches` 지점 필터 + 인메모리 `StaffLifecycleSummary.summarize` — V86 `idx_users_org_lifecycle_status` 재사용.
- **Must billing·attendance·NHIS 핵심 제약 7건** SQL 물리 재확인 — **전부 불변**.
- **agents.yaml `core_entities` 11종** 전수 충족(`users` V166 ON_LEAVE carry).
- **결론**: **신규 V167 불요** — V166 well-formed, summary API 앱 only. ERD §1 round 181·§4-2 V166·§7 V166·§8 lifecycle-summary + DATA_RETENTION ON_LEAVE 보존 + 본 #169. **보류 carry**: V166 `is_active` pairing(P3)·V162 `branch_ids` 요소 UUID(P3)·현금영수증 cross-table/time(P2)·PLAN↔BILLING reciprocal(P2)·`staff_attendance`/`staff_schedules`(Should)·`billing_payments`(Epic L). **coder**: 추가 DDL 0건.

#### #168. V165 후속 — live-e2e V165 readiness probe · 신규 DDL 0건 (2026-06-21, round 180, backend `7d29a38`)
- **배경**: round 179(#167 — DBA V165 `user_account_requests` defense-in-depth integrity 신규, backend `6f7f145`) → backend HEAD **`7d29a38`** 6 commit 전진 — `05ca0a8` **V165 commit**(라운드 179 DBA 산출의 committed 형태·`feat(db): harden user_account_requests with defense-in-depth integrity (V165)`)·`3bbfc00` **live-e2e probe gate on V165**(`UserAccountRequestSchemaReadinessProbe` + `HealthController`/`LiveE2eController`/`LiveE2eOperationReadinessSupport` 와이어)·`b11e29a` G21 seed branch service_type 정규화(앱 only)·`2f6f3bc` G-STAFF-NHIS-EXCEL-IMPORT 선택 검증(앱 only)·`e3b74a0` G-BANK-EXCEL-8 행 선택 검증(앱 only)·`7d29a38` G-BANK-EXCEL-8 non-positive 거부 테스트(테스트 only).
- **`git diff --name-only 6f7f145..7d29a38 -- src/main/resources/db/migration/`** = **`V165__user_account_requests_integrity.sql` 1파일**(라운드 179 documented, `05ca0a8` commit 형태). **`… -- '**/*Entity.java' '**/*Repository.java'`** = **0파일**. **`git diff 6f7f145..7d29a38 -- ':(exclude)src/main/resources/db/migration/' | grep -iE 'CREATE TABLE|ALTER TABLE|@Entity|@Column|@Query'`** = **0건**(V165 commit 자체 제외 — 신규 테이블·컬럼·엔티티·레포지토리·쿼리 0건). `ls db/migration | wc -l` = **165** contiguous(V1–V165, 갭·중복 0).
- **`UserAccountRequestSchemaReadinessProbe` 영향 분석 (신규 DDL 0건·읽기 전용)**:
  - 신규 컴포넌트 `com.ogada.backend.system.UserAccountRequestSchemaReadinessProbe`(44 lines·`@Component` Spring bean). 메서드 `integrityCheckReady()` 가 단 한 개의 SELECT 실행 — `SELECT COUNT(*) FROM pg_constraint c JOIN pg_class t ON c.conrelid=t.oid JOIN pg_namespace n ON t.relnamespace=n.oid WHERE t.relname='user_account_requests' AND n.nspname='public' AND c.conname='chk_user_account_requests_review_state_pair'`. V165 의 review-state pair CHECK 존재만 boolean 으로 노출.
  - `HealthController.isOperationReady`·`LiveE2eOperationReadinessSupport.requireOperationReady` 에 와이어 — probe 실패 시 `/health 503` + `operationReady=false` 응답. **NHIS caregiver bulk import (`G-STAFF-NHIS-EXCEL-IMPORT @6f7f145`)가 defense-in-depth 결손 스키마에서 실행되지 않도록 차단**.
  - 동일 패턴 carry: round 173 V157 `CaseManagementSchemaReadinessProbe`·round 176 V159 `CashReceiptSchemaReadinessProbe`·round 178 V164 `ClientCarePlanFormSchemaReadinessProbe` — DBA 신규 CHECK 와 짝으로 coder 가 readiness gate 추가하는 정착된 운영 패턴.
- **`b11e29a`·`2f6f3bc`·`e3b74a0`·`7d29a38` 영향 분석 (신규 DDL 0건)**:
  - **`b11e29a`** `LiveE2eBootstrapService.normalizeBranchServiceType` — `service_type` 문자열 normalization(`DAY_CARE` ↔ `HOME_VISIT` 등 enum value) 후 G21 seed applicable 분기. 스키마 미접근.
  - **`2f6f3bc`** `StaffNhisCaregiverImportService.normalizeSelectedRowNumbers` — 선택 행 번호 비-null·>0·distinct·비-empty 거부(앱 검증). 라운드 178 V165 약속(`branch_ids` JSONB array nonempty + Tenant FK)과 결합되어 cross-tenant·malformed 적재 1차 방어 deepen.
  - **`e3b74a0`·`7d29a38`** `BankDepositImportService` 동일 패턴(`normalizeSelectedRowNumbers`)·non-positive row number 거부 테스트. `billing` 도메인 — `user_account_requests` 영향 0(별 entity).
- **78/78 JPA `@Entity` ↔ Flyway `CREATE TABLE` 1:1 대조 carry** — 누락 0건(`audit_logs`·`billing_claim_status_history`는 raw SQL 전용, 설계 의도).
- **Must billing·attendance·NHIS 핵심 제약 7건** SQL 물리 재확인 — **전부 불변**(`uq_claim_branch_month` V1·`uq_billing_claim_items_claim_client` V26·`chk_billing_claims_amount_sum` V6·`trg_billing_claims_total_reconciliation` V11·`chk_attendance_presence_xor_absence` V11/V14·`uq_nhis_import_rows_org_id` V37·`chk_nhis_import_rows_match_requires_client` V19→V54). agents.yaml `core_entities` 11종 전수 충족(`users` 행 V165 적용 carry).
- **결론**: **신규 V166 불필요** — V165 후속 라운드는 commit + live-e2e readiness probe 와이어(읽기 전용)·앱 단 선택 검증으로, 기존 V165 CHECK + Tenant FK 위 defense-in-depth 가 의도대로 활성됨을 confirmation. ERD §1 round 180 행·§7 검증 헤더(round 180 @ `7d29a38`)·메타 timestamp + DATA_RETENTION 메타 timestamp + 본 #168. **보류 carry**: V162 `branch_ids` 요소별 UUID CHECK(P3 — 앱 책임)·V162 이메일 lower-case CHECK(P3 — partial UK)·V164 `notified_at` 시간 정합(P3)·이동서비스일지④ 시간 tolerance(P2)·현금영수증 `amount==copay`·`issued_at` 시간성(P2 — 앱 책임)·PLAN↔BILLING reciprocal pair CHECK(P2)·`waypoint_label` 길이/공백(P3)·L02 M05 투약·`staff_attendance`/`staff_schedules`(Should)·`billing_payments`(Epic L). **coder**: 추가 DDL 0건 — 스키마 영향 없음. `mvn flyway:migrate`(V165 적재 0건 가정)·`mvn test` 재검증은 라운드 179 PASS 결과 carry — 본 라운드 추가 변경분은 probe·앱 검증만 (`UserAccountRequestSchemaReadinessProbeTest` 42 lines·`HealthControllerTest` +97 lines·`LiveE2eControllerTest` +63 lines·`LiveE2eOperationReadinessSupportTest` +67 lines·`LiveE2eBootstrapLiveApiRoutingE2eTest` +37 lines = +306 lines test coverage).

#### #167. V165 `user_account_requests` defense-in-depth integrity (V162 비대칭 closure) (2026-06-20, round 179, backend `6f7f145`)
- **배경**: round 178(#계산 — ERD `@80b9619` 검증, V161~V164 신규 4건 일괄·V162 후속 V165 잠재 P2/P3 보류) → backend HEAD **`6f7f145`** 6커밋 전진 — `07a03c0` 대시보드 prior-deposit guard·`1134b2d` G21 FK-safe paired seed·`8b3f66d` G21 NHIS seed readiness tighten·`1283153` bootstrap error blocker priority·`07a85a3` **G-BANK-EXCEL-8 8-bank 카탈로그 + preview API**·`6f7f145` **★ G-STAFF-NHIS-EXCEL-IMPORT NHIS 요양보호사 Excel preview/import API**(carefor PDF p.95 워크플로). **전부 앱 only**(`billing`·`users` 패키지 + 테스트).
- **`git diff --name-only 80b9619..6f7f145 -- src/main/resources/db/migration/`** = **0파일**, **`… -- '**/*Entity.java' '**/*Repository.java'`** = **0파일**(coder 신규 테이블·컬럼·엔티티·레포지토리·마이그레이션 0건). `UserAccountRequestRepository` 미변경 — `6f7f145` `StaffNhisCaregiverImportService`는 기존 `UserAccountRequestService.submit` 위 wrapper(Excel 행→`SubmitUserAccountRequestPayload` 변환).
- **트리거**: `6f7f145` G-STAFF-NHIS-EXCEL-IMPORT가 NHIS 요양보호사 Excel 한 건당 다수 `user_account_requests` 적재 — 라운드 178 DBA 검증 헤더가 명시한 「**대량 신청 적재 전 P2 잠재 정정 판단 보류**」 시점이 정확히 도래. 적재 0건(`SELECT count(*) FROM user_account_requests` = **0**) 시점에 즉시 V165 closure.
- **DBA 신규 V165** — V162가 `chk_*_status` enum CHECK + 3 인덱스만 두고 출시되었던 비대칭(V164 client_care_plan_forms 11-CHECK well-formed 패턴과 격차) 일괄 해소. **8 CHECK + 3 Tenant FK**, single-additive `ALTER TABLE`만, 신규 컬럼·트리거·인덱스 0건:
  - ① **`chk_*_email_nonempty`/`chk_*_display_name_nonempty`** (`length(trim()) > 0`) — V164 9 nonempty CHECK·V157/V155 패턴.
  - ② **`chk_*_role_code_tenant_assignable`** (`role_code IN ('branch_admin','social_worker','caregiver','guardian','client_user')`) — `UserService.enforceRolePolicy`의 TENANT_API_BLOCKED_ROLES(`hq_admin` — V161 partial UK로 `ogada_platform_admin`만 발급) + OGADA_ONLY_ROLES(`ogada_*`·`sysadmin`) 검증의 DB 방어선. V160 `chk_users_role_code` 와 부분 정합(상위 집합).
  - ③ **`chk_*_branch_ids_array`** (`jsonb_typeof = 'array' AND jsonb_array_length > 0`) — V157 attendee_opinions array CHECK 패턴. raw SQL 객체/스칼라 적재 차단.
  - ④ **`chk_*_updated_after_created`/`chk_*_reviewed_after_created`** (V37 temporal·V36 sanity 패턴).
  - ⑤ **`chk_*_review_state_pair`** — status 3-상태 ↔ reviewer/created_user pair(`PENDING`= 셋 NULL·`REJECTED`= reviewer 쌍·`APPROVED`= reviewer 쌍 + `created_user_id`). V102 follow_up·V154 driver signature pair-CHECK 패턴. `UserAccountRequestService.{approve,reject}` 와 1:1 정합.
  - ⑥ **`chk_*_review_note_nonempty`** (nullable, 값이 있다면 비공백) — app trim 후 빈 문자열 잔존 차단.
  - ⑦ **Tenant FK 3쌍** `(organization_id, requested_by_user_id)`·`(organization_id, created_user_id)`·`(organization_id, active_branch_id)` → users/branches Tenant UK(V5/V4 anchor). V14 actor·V164 client_care_plan_forms·V77 billing_start_balance 패턴. MATCH SIMPLE(nullable NULL skip).
- **의도적 제외 (V165 ◯ → 영구 보류)**:
  - **`reviewed_by_user_id` Tenant FK 쌍** — 검토자(`ogada_platform_admin`·V160)는 `users.organization_id IS NULL`이지만 본 행 `organization_id`는 Tenant라 쌍이 영구 위반 → V162 평면 FK `REFERENCES users(id)`가 단독 referential integrity 보장.
  - **이메일 lower-case CHECK** — V162 `uq_*_pending_email` partial UK가 이미 `lower(email)` 차단·앱 항상 lower-case 저장. 향후 mixed-case 표시 허용 가능성 P3 보류.
  - **`branch_ids` 요소별 UUID 형태 CHECK** — plain PostgreSQL CHECK 표현 불가(요소 집계·정규식 매칭 subquery 필요). 앱 `UserService.validateTenantAccountRequestBranches` 책임 P3 유지.
- **데이터 안전**: V162 round 178에서 막 도입된 신규 테이블, 본 라운드 시점 `SELECT count(*) FROM user_account_requests` = **0** → backfill 불요·즉시 검증 PASS. 모든 CHECK는 immutable·NULL 분기 명시. 복합 Tenant FK 3건 모두 V5/V4 anchor 위에서 동작.
- **로컬 PG14 검증 PASS** (`psql --single-transaction` SAVEPOINT 격리):
  - **Negative (7)**: T1 빈 email → `chk_*_email_nonempty` ✅·T2 `hq_admin` role → `chk_*_role_code_tenant_assignable` ✅·T3 `{"x":1}` JSONB → `chk_*_branch_ids_array` ✅·T4 `[]` → `chk_*_branch_ids_array` ✅·T5 PENDING + reviewed_at → `chk_*_review_state_pair` ✅·T6 APPROVED 무 created_user → `chk_*_review_state_pair` ✅·T7 cross-tenant requester(org_dddd + user_aaaa) → `fk_*_requester_org` ✅.
  - **Positive (3)**: T8 valid PENDING 적재 ✅·T9 PENDING→APPROVED transition(reviewer + created_user) ✅·T10 PENDING→REJECTED transition(reviewer + note) ✅.
- **앱 정합**: `UserAccountRequestService.submit`은 `email.trim().toLowerCase()`·`displayName.trim()`·`roleCode.trim().toLowerCase()`·`validateAssignableRoleForTenantRequest`·`validateTenantAccountRequestBranches` + non-empty active_branch 강제. `approve`는 reviewer + created_user 쌍 적재. `reject`는 reviewer + `review_note.trim()` 적재. **본 V165 약속과 1:1 정합** → 정상 경로 영향 0, raw SQL/대량 import 우회만 차단(defense-in-depth).
- **Must billing·attendance·NHIS 핵심 제약 7건** SQL 물리 재확인 — **전부 불변**. agents.yaml `core_entities` 11종 전수 충족(`users` 행 V165 추가). `ls db/migration | wc -l` = **165** contiguous(V1–V165, 갭·중복 0).
- **결론**: **V165 신규** ✅ — 라운드 178 DBA 보류 항목(P2 복합 Tenant FK + P2 pair CHECK + P3 JSONB array CHECK) 일괄 closure. ERD §1 round 179 행·Must coverage `users` 행 갱신·§4-2 V162 ✅ closure + V165 신규 절·§7 마이그레이션 V165 행·§7 검증 헤더(round 179)·DATA_RETENTION §2/§4-1 갱신·메타 timestamp + 본 #167. **보류**: V162 `branch_ids` 요소별 UUID CHECK(P3 — 앱 책임)·V162 이메일 lower-case CHECK(P3 — partial UK)·V164 `notified_at` 시간 정합(P3)·이동서비스일지④ 시간 tolerance(P2)·현금영수증 `amount==copay`·`issued_at` 시간성(P2 — 앱 책임)·PLAN↔BILLING reciprocal pair CHECK(P2)·`waypoint_label` 길이/공백(P3)·L02 M05 투약·`staff_attendance`/`staff_schedules`(Should)·`billing_payments`(Epic L). **coder**: `mvn flyway:migrate`(적재 0건 가정)·`mvn test` 재검증 권장 — V165는 additive CHECK + Tenant FK이므로 mock 단위 테스트 무영향, Testcontainers `UserAccountRequestService.{submit,approve,reject}` 정상 경로 100% 충족 예상. raw SQL seed 가 있다면 본 약속 위반 시 마이그레이션 직후 INSERT 실패할 수 있음(검토 후 수정).

#### #166. V159 live-e2e readiness probe · Must billing·attendance 재대조 · 신규 V160 불요 (2026-06-20, round 176, backend `bfad37d`)
- **배경**: round 176+(`beef81e`/V159 gap 식별·#165 「V159 불요」는 앱-only export 라운드 판단) → **`15061a9`** **V159 `chk_cash_receipt_issuances_identifier_value_format`** 커밋(DBA) → backend HEAD **`bfad37d`** 5커밋 전진 — `1139e79` **live-e2e probe에 V159 schema readiness 노출**·`4d4457f` **probe readiness를 cash-receipt schema gate에 연동**·`091c372` unsupported branch G21 seed not-applicable·`bfad37d` operation readiness centralization(전부 **앱 only**, `system/` 패키지 + 테스트).
- **`git diff --name-only 15061a9..bfad37d -- src/main/resources/db/migration/`** = **0파일**, **`… -- '**/*Entity.java' '**/*Repository.java'`** = **0파일**, **`CREATE TABLE|ALTER TABLE` grep** = **0건**. `CashReceiptSchemaReadinessProbe`는 `pg_constraint`/`pg_class`에서 V159 CHECK 존재만 **읽기** — 신규 테이블·컬럼·인덱스·`@Query` 0건.
- **78/78 JPA `@Entity` ↔ Flyway `CREATE TABLE` 1:1 대조** — entity→migration 누락 0건. `audit_logs`·`billing_claim_status_history`는 raw SQL 전용(설계 의도).
- **Must billing·attendance·NHIS 핵심 제약 7건** SQL 물리 재확인 — **전부 불변**(`uq_claim_branch_month` V1·`uq_billing_claim_items_claim_client` V26·`chk_billing_claims_amount_sum` V6·`trg_billing_claims_total_reconciliation` V11·`chk_attendance_presence_xor_absence` V11/V14·`uq_nhis_import_rows_org_id` V37·`chk_nhis_import_rows_match_requires_client` V19→V54). agents.yaml `core_entities` 11종 전수 충족. `ls db/migration | wc -l` = **159** contiguous(V1–V159, 갭·중복 0).
- **결론**: **신규 V160 불필요** — V159 probe·live-e2e readiness는 기존 CHECK 읽기 전용. ERD §1 round 176 `@bfad37d` 행·§7 검증 헤더(round 176 `@bfad37d`)·메타 timestamp + 본 #166. **보류**: 현금영수증 `amount==copay`·`issued_at` 시간성 DB enforce(P2 — 앱 책임)·PLAN↔BILLING reciprocal pair CHECK(P2)·이동서비스일지④ 시간 tolerance(P2)·`waypoint_label` 길이/공백(P3)·L02 M05 투약·`staff_attendance`/`staff_schedules`(Should)·`billing_payments`(Epic L). **coder**: 추가 DDL 0건 — 스키마 영향 없음.

#### #165. G26 의료비공제 연도기준·NTS/Excel export·현금영수증 식별자 정규화 검토 → 신규 V159 불요 (2026-06-19, round 175, backend `35d1560`)
- **배경**: round 174(#164 「V158 현금영수증 발급 대장 검토·V159 불요」, backend `58ff35e`) → backend HEAD **`35d1560`** 6커밋 전진 — `ceeaeb9` **G26 의료비공제 연도기준 + NTS 배치 export API**(`MedicalExpenseDeductionYearBasis` PAID_YEAR|CLAIM_YEAR·국세청 CSV)·`43ef73b` yearBasis 라우팅·per-client 청구년 커버리지 테스트·`e454d3b` **G-7-1 청구서 Excel export API**(`BillingStatementExportService`·`BillingStatementExportKind`)·`08ad3b3` RBAC webmvc 테스트 billing export mock·`298bcdf` 현금영수증 식별자 매칭 정규화·`35d1560` 현금영수증 휴대폰/사업자 식별자 검증. **전부 앱 only**(`billing`·`clients`·`attendance` 패키지 + 테스트).
- **`git diff --name-only 58ff35e..35d1560 -- src/main/resources/db/migration/`** = **0파일**, **`… -- '**/*Entity.java' '**/*Repository.java'`** = **0파일**, **`git diff 58ff35e..35d1560 | grep -iE 'CREATE TABLE|ALTER TABLE|@Entity|@Column|@Query'`** = **0건**. 변경 20파일(서비스 7·테스트 13) — coder 신규 테이블·컬럼·엔티티·레포지토리·마이그레이션 0건. `ls db/migration | wc -l` = **158** contiguous(V1–V158, 갭·중복 0).
- **신규 노출 쿼리 DB backing 대조** (신규 조회 인덱스 0건):
  - ① **G26 의료비공제 연도기준** — `BillingService`가 PAID 청구를 `billingClaimRepository`로 적재 후 `matchesMedicalExpenseTaxYear(claim, taxYear, yearBasis)`로 **인메모리** 분기. PAID_YEAR=`paid_at` 연도·CLAIM_YEAR=`claim_year_month` 기준. 적재 쿼리는 V153 `idx_billing_claims_org_branch_status_paid_at`(partial PAID·`paid_at DESC`)로 이미 backing — yearBasis 는 DB 술어가 아닌 인메모리 필터이므로 전용 인덱스 불요. NTS CSV(`formatMedicalExpenseDeductionNtsCsv`)는 동일 결과 직렬화.
  - ② **G-7-1 청구서 Excel export** — `BillingStatementExportService`가 `billingClaimRepository.findByIdAndOrganizationId`(V1 Tenant UK)·`billingClaimItemRepository.findByClaimIdOrderByCreatedAtAsc`(V26 청구항목)·`clientRepository.findByOrganizationIdAndIdIn`(V5 `uq_clients_org_id`)·`guardianClientRepository.findByOrganizationIdAndClientIdInAndPrimaryGuardianTrue`(기존 인덱스)·`userRepository.findByOrganizationIdAndIdIn`만 호출 — 전부 PK/Tenant-UK/기존 인덱스. 신규 레포지토리 메서드·`@Query` 0건.
  - ③ **현금영수증 식별자 정규화** — `normalizeIdentifierSearchValue`(`replaceAll("\\D","")`)·`contains(queryDigits)`는 V158 `idx_cash_receipt_issuances_org_branch_issued_at`로 적재된 발급 행을 **인메모리** 필터. PHONE/BIZ 길이 검증(`validateIdentifierValue`)도 앱 검증 — 신규 DB 술어·인덱스 0건(V158 `identifier_type` enum CHECK·nonempty CHECK 위 추가 앱 가드).
- **Must billing·attendance·NHIS 핵심 제약 7건** SQL 물리 재확인 — **전부 불변**(`uq_claim_branch_month` V1·`uq_billing_claim_items_claim_client` V26·`chk_billing_claims_amount_sum` V6·`trg_billing_claims_total_reconciliation` V11·`chk_attendance_presence_xor_absence` V11/V14·`uq_nhis_import_rows_org_id` V37·`chk_nhis_import_rows_match_requires_client` V19→V54). agents.yaml `core_entities` 11종 전수 충족.
- **결론**: **신규 V159 불필요** — G26 연도기준·NTS/Excel export·식별자 정규화는 기존 인덱스(V153/V1/V26/V5/V158) 위 읽기 전용 export·인메모리 분기·필터, 신규 DB 술어 0건. ERD §1 round 175 행·§7 검증 헤더(round 175)·메타 timestamp + 본 #165. **보류**: 현금영수증 `amount==copay`·`issued_at` 시간성 DB enforce(P2 — 앱 책임)·PLAN↔BILLING reciprocal pair CHECK(P2)·이동서비스일지④ 시간 tolerance(P2)·`waypoint_label` 길이/공백(P3)·L02 M05 투약·`staff_attendance`/`staff_schedules`(Should)·`billing_payments`(Epic L). **coder**: 추가 DDL 0건 — 스키마 영향 없음.

#### #164. V158 현금영수증 발급 대장(`cash_receipt_issuances`) 검토 → DBA 후속 V159 불요 (2026-06-19, round 174, backend `58ff35e`)
- **배경**: round 173(#163 「G32 참석자별 의견 앱 무결성 deepen·신규 DDL 0건」, backend `caeac0d`) → backend HEAD **`58ff35e`** 6커밋 전진 — `7848b0f`(seed 자격증명 정규화·앱 only)·`4432558` **V158 `cash_receipt_issuances` 신규 + 현금영수증 발급 API**(coder, G-CASH-RECEIPT-LOG BNK-398·이지케어 FAQ 21701/21716/21717)·`f79a19e`/`8e6e0c6`(RBAC·라우팅·7일 SLA·라이브 API 하니스 테스트)·`fe54af8`/`ab5708b`/`58ff35e`(대시보드 pending/overdue 카운트·발급대기 목록 API·HQ 다지점·전년도 발급 flag — 전부 앱 only).
- **`git diff --name-only caeac0d..58ff35e -- src/main/resources/db/migration/`** = **V158 1파일**(coder), **`… -- '**/*Entity.java'`** = `CashReceiptIssuanceEntity`(신규), **`… -- '**/*Repository.java'`** = `CashReceiptIssuanceRepository`(신규). `ls db/migration | wc -l` = **158** contiguous(V1–V158, 갭·중복 0).
- **V158 검토 (coder 소유)**: `cash_receipt_issuances` = PAID + CASH 본인부담 청구당 1건 국세청(NTS) 현금영수증 발급 기록. coder 가 전사 defense-in-depth 규약(V60 CMS Tenant FK·V155 WAYPOINT nonempty·V52 결제 actor)을 **이미 완비** —
  - ① **복합 Tenant FK 3건** `(org,branch_id)→branches`·`(org,client_id)→clients`·`(org,billing_claim_id)→billing_claims` (cross-tenant 연결 차단).
  - ② **Tenant UK 3종** `uq_*_org_id`(`(org,id)` 앵커)·`uq_*_org_claim`(`(org,billing_claim_id)` = **청구당 1건**, 앱 `existsByOrganizationIdAndBillingClaimId` 이중 방어)·`uq_*_org_nts_no`(발급번호 Tenant 중복 불가).
  - ③ **도메인 CHECK 4종** `identifier_type IN ('PHONE','BIZ')`·`nts_receipt_no`/`identifier_value` `length(trim())>0`·`amount>0`.
  - ④ **조회 인덱스 2종** `idx_*_org_branch_issued_at`·`idx_*_org_client_issued_at` `(…, issued_at DESC)`.
- **레포지토리 4메서드 인덱스 backing 대조** (신규 인덱스 0건): `findBy…BranchIdOrderByIssuedAtDesc`→`idx_*_org_branch_issued_at`·`findBy…ClientIdOrderByIssuedAtDesc`→`idx_*_org_client_issued_at`·`existsBy…BillingClaimId`/`findBy…BillingClaimId`→`uq_*_org_claim` 좌선두 — 전부 충족.
- **DBA 후속 V159 불요 결정**: 잔여 불변식은 PostgreSQL CHECK 로 표현 불가하거나 중복 위험 → **앱(`CashReceiptIssuanceService`) 책임 유지** —
  - `amount == billing_claims.copay_amount`(교차테이블 동등)·`issued_at`이 수납일(`paid_at`) 이전 금지 = subquery 필요 → plain CHECK 불가, trigger 화 시 `createIssuance` 로직 중복·괴리 위험.
  - `issued_at` 미래 금지 = `CURRENT_DATE`(non-immutable) → CHECK 불가.
  - `createIssuance`가 이미 셋 모두 강제(BusinessRuleException) — #161 PLAN↔BILLING reciprocal pair CHECK·#162 요소 비공백 P2/P3 보류와 동일 정책.
- **Must billing·attendance·NHIS 핵심 제약 7건** SQL 물리 재확인 — **전부 불변**(`uq_claim_branch_month` V1·`uq_billing_claim_items_claim_client` V26·`chk_billing_claims_amount_sum` V6·`trg_billing_claims_total_reconciliation` V11·`chk_attendance_presence_xor_absence` V11/V14·`uq_nhis_import_rows_org_id` V37·`chk_nhis_import_rows_match_requires_client` V19→V54). agents.yaml `core_entities` 11종 전수 충족(`cash_receipt_issuances`는 `billing` core_entity 발급 대장 확장).
- **결론**: **신규 V159 불필요** — V158 은 defense-in-depth 완비된 well-formed 테이블, 잔여 불변식은 앱 책임. ERD §1 V158/round 174 행·§4-6 `cash_receipt_issuances` diagram·규칙 bullet·§7 마이그레이션 V158 행·§7 검증 헤더(round 174)·§8 API 매핑·헤더 DDL 범위 `…V158`·메타 timestamp + 본 #164. **보류**: 현금영수증 `amount==copay`·`issued_at` 시간성 DB enforce(P2 — 앱 책임)·PLAN↔BILLING reciprocal pair CHECK(P2)·이동서비스일지④ 시간 tolerance(P2)·`waypoint_label` 길이/공백(P3)·L02 M05 투약·`staff_attendance`/`staff_schedules`(Should)·`billing_payments`(Epic L). **coder**: 추가 DDL 0건 — 스키마 영향 없음.

#### #163. G32 참석자별 의견 앱 무결성 deepen · live-e2e V157 readiness probe · 신규 DDL 0건 (2026-06-19, round 173, backend `caeac0d`)
- **배경**: round 172(#162 「V156 G32 참석자별 의견 검토 → V157 JSONB array CHECK 신규」, backend `b9e0947`) → backend HEAD **`caeac0d`** 6커밋 전진 — `8835aa2` **V157 commit**(round 172 DBA 산출 `chk_case_management_meetings_attendee_opinions_array`의 committed 형태)·`eed39ab` **참석자별 의견 작성자 유일성·참석자명단 1:1 대응·참석자명 중복 거부**(`CaseManagementService`)·`9ecd019` codec/malformed-JSON 테스트·`510d2f3` pilot E2E·서비스 테스트·`c0a59aa` **live-e2e probe에 G32 schema readiness 신호 추가**·`45d95ea` **probe V157 array CHECK readiness**·`caeac0d` health probe ↔ G32 readiness 정렬. `8835aa2`(V157) 외 전부 **앱 only**(`casemanagement`·`system` 패키지 + 테스트).
- **`git diff --name-only b9e0947..caeac0d -- src/main/resources/db/migration/`** = **V157 1파일**(round 172 #162에서 이미 검토·문서화), **`… -- '**/*Entity.java' '**/*Repository.java'`** = **0파일**, **`git diff b9e0947..caeac0d | grep -iE 'CREATE TABLE|ALTER TABLE|@Entity|@Column|@Query'`** = `ALTER TABLE`(V157만). `ls db/migration | wc -l` = **157** contiguous(V1–V157, 갭·중복 0).
- **G32 앱 무결성 deepen 대조 (`eed39ab` — 신규 DDL 0건)**: ① 작성자 유일성(`opinionNames.size == opinions.size`) ② 의견 ↔ 참석자명단 1:1 대응(`opinions.size == distinct attendeeNames size`) ③ 참석자명 중복 거부(`distinctCount == attendees.size`). 셋 모두 **JSONB 배열 요소 간 cardinality·uniqueness + TEXT `attendee_names` 교차 검증**이다. plain PostgreSQL CHECK 는 subquery·배열 요소 집계를 표현할 수 없고, trigger 로 강제하면 `AttendeeOpinionsCodec` 디코딩·정규화 로직을 DB 에 중복 구현하게 되어 괴리·유지보수 위험 → **앱·codec 책임 유지**(#162 「요소별 name/opinion 비공백·jobRole enum P3 보류」와 동일 정책). V157 array-shape CHECK 가 이미 DB 1차 방어를 제공하므로 비대칭 갭 없음.
- **live-e2e V157 readiness probe 대조 (`c0a59aa`/`45d95ea`/`caeac0d` — 신규 DDL 0건)**: `HealthController`·`LiveE2e*` 가 V157 `chk_*_attendee_opinions_array` 의 존재·작동을 operation readiness 신호로 **읽기만** 한다(`information_schema`/probe 쿼리·신규 테이블·컬럼·인덱스·`@Query` 0건).
- **Must billing·attendance·NHIS 핵심 제약 7건** SQL 물리 재확인 — **전부 불변**(`uq_claim_branch_month` V1·`uq_billing_claim_items_claim_client` V26·`chk_billing_claims_amount_sum` V6·`trg_billing_claims_total_reconciliation` V11·`chk_attendance_presence_xor_absence` V11/V14·`uq_nhis_import_rows_org_id` V37·`chk_nhis_import_rows_match_requires_client` V19→V54). agents.yaml `core_entities` 11종 전수 충족.
- **결론**: **신규 V158 불필요** — G32 참석자별 의견 cross-element 무결성은 DB 로 표현 불가하거나 중복 위험이라 앱·codec 책임(V157 array-shape 1차 방어 유지), live-e2e probe 는 V157 읽기 전용. ERD §1 round 173 행·§7 검증 헤더(round 173)·메타 timestamp + 본 #163. **보류**: 참석자별 의견 요소(name/opinion 비공백·jobRole enum) DB CHECK(P3 — 앱 codec 책임)·PLAN↔BILLING reciprocal pair CHECK(P2)·이동서비스일지④ 시간 tolerance(P2)·`waypoint_label` 길이/공백(P3)·L02 M05 투약·`staff_attendance`/`staff_schedules`(Should)·`billing_payments`(Epic L). **coder**: 추가 DDL 0건 — 스키마 영향 없음.

#### #162. V156 G32 참석자별 의견 검토 → V157 JSONB array CHECK 신규 (2026-06-19, round 172, backend `b9e0947`)
- **배경**: round 169(#161 「G21 paired PLAN/BILLING seed·readiness·V156 불필요」, backend `7898aa5`) → backend HEAD **`b9e0947`** 6커밋 전진 — `02cf036`·`02a2eb8`·`bc754a0`·`12d1a7b`(전부 **앱 only** live-e2e/health probe, `system/` 패키지)·`5222a8f` **V156 `attendee_opinions` JSONB 추가**(coder, G32 FAQ21797 참석자별 의견)·`b9e0947` 대시보드 attendee-opinion gap 노출(앱 only).
- **`git diff --name-only 7898aa5..b9e0947 -- src/main/resources/db/migration/`** = **V156 1파일**(coder), **`… -- '**/*Entity.java'`** = `CaseManagementMeetingEntity`(컬럼 매핑 `attendee_opinions` 1건), **`… -- '**/*Repository.java'`** = **0파일**. `ls db/migration | wc -l` = **157**(V157 신규 후) contiguous(V1–V157, 갭·중복 0).
- **V156 검토 (coder 소유)**: `case_management_meetings.attendee_opinions JSONB`(nullable, `[{name, jobRole?, opinion}]`). 회의내용=참가 직원별 의견 필수 parity(BNK-390 carry gap). `AttendeeOpinionsCodec.{encode,decode}`가 직렬화/디코딩(빈 목록=NULL, 디코딩 실패=빈 목록 graceful). 대시보드 gap 노출(`DashboardService`·`CaseManagementService`)은 동일 행 인메모리 집계 — **신규 조회 인덱스 불요**(필터 술어 아님).
- **DBA 신규 V157** — V156이 **제약 없이** JSONB 컬럼을 추가한 비대칭 갭 해소(round 164 V155 WAYPOINT 비공백·V154 운전자 서명 pair-CHECK와 동일 defense-in-depth):
  - ① **근거** — codec 계약은 JSON **배열**을 전제하나 V156은 형태 보장이 없어 raw SQL 로 객체/스칼라(`{"x":1}`·`"foo"`·`42`)가 적재되면 codec 이 예외를 삼키고 **조용히 빈 목록 디코딩**(데이터 품질 손상·gap 통계 왜곡). 동일 테이블의 TEXT 컬럼(`selection_reason`·`meeting_content`·`meeting_result`·`attendee_names`·`case_management_plan`)은 모두 nonempty CHECK 로 방어하는데 JSONB만 무방비(비대칭).
  - ② **DDL** — 추가 제약 1건만(`chk_case_management_meetings_attendee_opinions_array`: `attendee_opinions IS NULL OR jsonb_typeof(attendee_opinions) = 'array'`). 기존 V73(6필수 CHECK·`uq_*_client_quarter`·`uq_*_org_id`)·V74(date↔quarter CHECK·active guard·actor·org-branch sync 트리거)·V75(`case_management_plan` nonempty) **전부 불변** → 후속 integrity 마이그레이션 불요·테이블 재작성 0.
  - ③ **데이터 안전** — V156 직후라 기존 행은 **NULL 또는 앱(`AttendeeOpinionsCodec.encode`) 작성 유효 배열뿐** → backfill 불요·Flyway clean DB migrate 즉시 검증 PASS. NULL 은 `IS NULL` 분기로 CHECK 통과(`jsonb_typeof(NULL)`=NULL 대비 명시 가드).
  - ④ **앱 정합** — `CaseManagementService`는 항상 `encode`(배열 직렬화)로 적재 → 항상 충족. V157은 raw SQL·우회 경로 1차 방어(defense-in-depth, mock 단위 테스트 무영향).
- **Must billing·attendance·NHIS 핵심 제약 7건** SQL 물리 재확인 — **전부 불변**(`uq_claim_branch_month` V1·`uq_billing_claim_items_claim_client` V26·`chk_billing_claims_amount_sum` V6·`trg_billing_claims_total_reconciliation` V11·`chk_attendance_presence_xor_absence` V11/V14·`uq_nhis_import_rows_org_id` V37·`chk_nhis_import_rows_match_requires_client` V19→V54). agents.yaml `core_entities` 11종 전수 충족(`case_management_meetings`는 G32 지표43 도메인 — core_entities 외 회의록 확장).
- **결론**: **V157 신규**. ERD §1 V156/V157 행·§4-13 참석자별 의견 규칙·diagram 컬럼·§7 마이그레이션 V156/V157 행·§7 구현 메모 V156/V157 행·§8 API 매핑·헤더 DDL 범위 `…V157`·§7 검증 헤더(round 172)·메타 timestamp + 본 #162. **보류**: 참석자별 의견 **요소별 name/opinion 비공백·jobRole enum** DB CHECK(P3 — 앱 codec 책임)·PLAN↔BILLING reciprocal pair CHECK(P2)·이동서비스일지④ 시간 tolerance(P2)·`waypoint_label` 길이/공백(P3)·L02 M05 투약·`staff_attendance`/`staff_schedules`(Should)·`billing_payments`(Epic L). **coder**: V157 `mvn flyway:migrate`·`mvn test` 재검증(추가 CHECK 는 mock 단위 테스트 무영향 — BE Test PASS 유지 예상).

#### #161. G21 paired PLAN/BILLING seed·readiness deepen · 신규 DDL 0건 (2026-06-19, round 169, backend `7898aa5`)
- **배경**: round 168(#160 「G21 seed readiness probe·NHIS row↔batch linkage·V156 불필요」, backend `c0403b0`) → backend HEAD **`7898aa5`** 5커밋 전진 — `fd275f4` **live-e2e bootstrap paired PLAN/BILLING visit schedule seed**(`ensurePairedVisitSchedules` — `visit_schedules` PLAN·BILLING 2행 upsert·`paired_schedule_id` 상호 연결)·`429661e` **probe/bootstrap에 `billingVisitScheduleReady` 노출**·`cc295ec` **legacy `DAY_CARE` 지점도 G21 seed applicable**(QA-B95)·`191703f` **branch missing 시 seed readiness 차단**·`7898aa5` **probe에 branch-missing blocker 노출**. **전부 앱 only**(QA-B95 live-e2e operation probe 안정화 — `system/` 패키지 9파일).
- **`git diff --name-only c0403b0..7898aa5 -- src/main/resources/db/migration/`** = **0파일**, **`… -- '**/*Entity.java' '**/*Repository.java'`** = **0파일**, **`git diff c0403b0..7898aa5 | grep -iE 'CREATE TABLE|ALTER TABLE|@Entity|@Column|@Query'`** = **0건**. 변경 파일 9개 전부 `com.ogada.backend.system` — coder 신규 테이블·컬럼·엔티티·레포지토리·마이그레이션 0건.
- **G21 paired BILLING readiness DB backing 대조** (신규 조회 인덱스 0건):
  - ① **PLAN 일정 readiness** — `visitScheduleRepository.findByIdAndOrganizationId(resolvedVisitScheduleId, org)` → **V53** `uq_visit_schedules_org_id`(+ **V53** `idx_visit_schedules_org_branch_kind_date` 보완). 지점 스코프는 조회 후 `branchId` 인메모리 필터.
  - ② **BILLING 일정 readiness + 페어 검증** — `findByIdAndOrganizationId(resolvedBillingVisitScheduleId, org)` 동일 PK 조회 + `isPairedPlanBillingSchedules`(PLAN/BILLING `schedule_kind`·`paired_schedule_id` 상호 일치) — **인메모리** 검증. DB는 **V53** `fk_visit_schedules_paired_org`·**V56** `idx_visit_schedules_org_paired`로 페어 FK·역조회 이미 backing. reciprocal pair CHECK(양방향 kind·id 일치)는 **앱·E2E seed 책임** — DB 강제 보류(P2, #160 보류 목록과 동일 패턴).
  - ③ **NHIS readiness** — round 168(#160)과 동일: batch `findByIdAndOrganizationId` → **V8** `uq_nhis_batches_org_id`, row → **V37** `uq_nhis_import_rows_org_id`, linkage `row.batchId == batch.id` 인메모리.
  - ④ **branch missing** — `branchRepository.findById(branchId)` PK 단건 → null/inactive 시 `LiveE2eG21SeedStatus.missingBranchOrInactive()`(신규 DDL 0건).
  - ⑤ **legacy DAY_CARE applicable** — `isG21SeedApplicableBranch`가 `HOME_VISIT`/`INTEGRATED_HOME` 외 `DAY_CARE`도 true — bootstrap이 지점 `service_type`을 HOME_VISIT로 승격·paired seed 수행(스키마 변경 없음).
- **Must billing·attendance·NHIS 핵심 제약 7건** SQL 물리 재확인 — **전부 불변**(`uq_claim_branch_month` V1·`uq_billing_claim_items_claim_client` V26·`chk_billing_claims_amount_sum` V6·`trg_billing_claims_total_reconciliation` V11·`chk_attendance_presence_xor_absence` V11/V14·`uq_nhis_import_rows_org_id` V37·`chk_nhis_import_rows_match_requires_client` V19→V54). agents.yaml `core_entities` 11종 전수 충족. `ls db/migration | wc -l` = **155** contiguous(V1–V155, 갭·중복 0).
- **결론**: **신규 V156 불필요** — G21 paired BILLING seed·readiness는 기존 visit_schedules(V53/V56)·NHIS import(V8/V37) 위 읽기/시드 전용. ERD §1 round 169 행·§7 검증 헤더(round 169)·메타 timestamp + 본 #161. **보류**: PLAN↔BILLING reciprocal pair CHECK(P2)·이동서비스일지④ 시간 tolerance DB enforce(P2)·`waypoint_label` 길이/공백 정책(P3)·L02 M05 투약·`staff_attendance`/`staff_schedules`(Should)·`billing_payments`(Epic L). **coder**: 추가 DDL 0건 — 스키마 영향 없음.

#### #160. G21 seed readiness probe · NHIS row↔batch linkage · 신규 DDL 0건 (2026-06-19, round 168, backend `c0403b0`)
- **배경**: round 167(#159 「G21 NHIS comparison deepen·live-e2e NHIS seed·V156 불필요」, backend `f932fd3`) → backend HEAD **`c0403b0`** 3커밋 전진 — `c651b30` **per-tenant seed fallback id 스코프**(`LiveE2eBootstrapService.scopedFallbackId` — DEFAULT 고정 UUID 미존재 시 org 스코프 deterministic id 폴백)·`14582bf` **probe/bootstrap에 G21 seed readiness 노출**(`LiveE2eProbeResponse`·`LiveE2eBootstrapResponse`에 visit-schedule·NHIS batch/row readiness 플래그)·`c0403b0` **G21 seed readiness가 NHIS row↔batch linkage 요구**(seed 완료 판정에 `nhisImportRow.batchId == nhisImportBatch.id` 추가). **전부 앱 only**(QA-B95 live-e2e operation probe 안정화 — `system/` 패키지).
- **`git diff --name-only f932fd3..c0403b0 -- src/main/resources/db/migration/`** = **0파일**, **`… -- '**/*Entity.java' '**/*Repository.java'`** = **0파일**, **`git diff f932fd3..c0403b0 | grep -iE 'CREATE TABLE|ALTER TABLE|@Entity|@Column|@Query'`** = **0건**. 변경 파일 9개 전부 `com.ogada.backend.system`(`HealthController`·`LiveE2eController`·`LiveE2eBootstrapService`·`LiveE2eBootstrapResponse`·`LiveE2eProbeResponse` + 테스트 4) — coder 신규 테이블·컬럼·엔티티·레포지토리·마이그레이션 0건.
- **G21 seed readiness probe DB backing 대조** (신규 조회 인덱스 0건 — 전부 PK/Tenant-UK 단건 조회):
  - ① **방문 일정 readiness** — `visitScheduleRepository.findByIdAndOrganizationId(resolvedVisitScheduleId, org)` → visit_schedules Tenant UK(+ **V53** `idx_visit_schedules_org_branch_kind_date` 보완). `findById(DEFAULT_VISIT_SCHEDULE_ID)` fallback은 PK.
  - ② **NHIS 배치 readiness** — `nhisImportBatchRepository.findByIdAndOrganizationId(resolvedBatchId, org)` → **V8** `uq_nhis_batches_org_id (organization_id, id)`. `findById(DEFAULT_NHIS_IMPORT_BATCH_ID)` fallback은 PK.
  - ③ **NHIS 행 readiness + batch linkage** — `nhisImportRowRepository.findByIdAndOrganizationId(resolvedRowId, org)` → **V37** `uq_nhis_import_rows_org_id`. `nhisImportReady = batchReady && rowReady && (row.batchId == batch.id)` — linkage 비교는 조회한 두 엔티티의 **인메모리** 동등성(신규 count `@Query`·DDL 0건).
  - ④ **fallback id·지점** — `branchRepository.findById(branchId)`·`scopedFallbackId(prefix, org)`(`UUID.nameUUIDFromBytes("kind:org")` name-based deterministic, DB 미접근) — PK 단건 또는 순수 계산.
- **Must billing·attendance·NHIS 핵심 제약 7건** SQL 물리 재확인 — **전부 불변**(`uq_claim_branch_month` V1·`uq_billing_claim_items_claim_client` V26·`chk_billing_claims_amount_sum` V6·`trg_billing_claims_total_reconciliation` V11·`chk_attendance_presence_xor_absence` V11/V14·`uq_nhis_import_rows_org_id` V37·`chk_nhis_import_rows_match_requires_client` V19→V54). agents.yaml `core_entities` 11종 전수 충족. `ls db/migration | wc -l` = **155** contiguous(V1–V155, 갭·중복 0).
- **결론**: **신규 V156 불필요** — G21 seed readiness probe·NHIS row↔batch linkage는 기존 PK/Tenant-UK(V8/V37/V53) 위 읽기 전용 검증. ERD §7 검증 헤더(round 168)·메타 timestamp + 본 #160. **보류**: 이동서비스일지④ 시간 tolerance DB enforce(P2)·`waypoint_label` 길이/공백 정책(P3)·L02 M05 투약·`staff_attendance`/`staff_schedules`(Should)·`billing_payments`(Epic L). **coder**: 추가 DDL 0건 — 스키마 영향 없음.

#### #159. G21 NHIS comparison deepen · live-e2e NHIS seed · 신규 DDL 0건 (2026-06-18, round 167, backend `f932fd3`)
- **배경**: round 166(#158 「G21 confirm-readiness·NHIS 비교 API·V156 불필요」, backend `8a8c5b3`) → backend HEAD **`f932fd3`** 4커밋 전진 — `4046046` **NHIS comparison summary deepen**(matched/unmatched/discrepancy/unpaired 분류·blocker 메시지·`VisitNhisComparisonSummary` DTO 확장)·`39fa41a` batch-confirm pilot E2E NHIS readiness blocker 정렬·`b73e5f4` **live-e2e bootstrap NHIS import batch seed**(`LiveE2eBootstrapService.ensureSampleNhisImportBatch` — 방문요양 지점만 고정 UUID batch+row 1건 MATCHED upsert)·`f932fd3` live-e2e default-credentials operation probe 차단. **전부 앱 only**(G21 batch-confirm·NHIS 비교 E2E 안정화).
- **`git diff --name-only 8a8c5b3..f932fd3 -- src/main/resources/db/migration/`** = **0파일**, **`… -- '**/*Entity.java' '**/*Repository.java'`** = **0파일**(coder 신규 테이블·컬럼·엔티티·레포지토리·마이그레이션 0건). `VisitScheduleRepository`·`NhisImportBatchRepository`·`NhisImportRowRepository` **미변경** — `4046046`/`b73e5f4`가 호출하는 기존 메서드만 사용.
- **G21 NHIS comparison deepen DB backing 대조** (round 166 #158과 동일 — 신규 조회 인덱스 0건):
  - ① **PLAN 일정 범위** — `findBy…ScheduleKindAndVisitDateBetween…` → **V53** `idx_visit_schedules_org_branch_kind_date`.
  - ② **최신 NHIS 배치** — `NhisImportBatchRepository.findScopedBatches` → **V38** `idx_nhis_import_batches_org_branch_created`(+ **V27** month variant).
  - ③ **배치 행** — `NhisImportRowRepository.findByBatchIdOrderByCreatedAtAsc` → **V28** `idx_nhis_import_rows_batch_created`.
  - ④ **이용자 batch 조회** — `clientRepository.findByOrganizationIdAndIdIn` → **V5** `uq_clients_org_id`.
  - summary deepen(4종 분류·blocker 메시지·per-client diff)은 동일 list 쿼리 결과를 **인메모리 집계** — 신규 count `@Query`·DDL 0건.
- **live-e2e NHIS seed 대조** (`LiveE2eBootstrapService.ensureSampleNhisImportBatch` — 신규 DDL 0건):
  - HOME_VISIT/INTEGRATED_HOME 지점(`BranchServiceType.isHomeVisitLike`)에서만 실행 — 주간보호(DAY_CARE) 파일럿 Tenant는 skip(의도 정합).
  - `nhis_import_batches` upsert(COMPLETED·`row_count=1`) + `nhis_import_rows` upsert(MATCHED·`client_id`·`ltc_cert_no`) — **V21** 지점 일치·**V22** org 복사·**V25** cert 공백 CHECK·**V54** match_status CHECK·**V37** Tenant UK 위에서만 동작.
- **Must billing·attendance·NHIS 핵심 제약 7건** SQL 물리 재확인 — **전부 불변**(`uq_claim_branch_month` V1·`uq_billing_claim_items_claim_client` V26·`chk_billing_claims_amount_sum` V6·`trg_billing_claims_total_reconciliation` V11·`chk_attendance_presence_xor_absence` V11/V14·`uq_nhis_import_rows_org_id` V37·`chk_nhis_import_rows_match_requires_client` V19→V54). agents.yaml `core_entities` 11종 전수 충족. `ls db/migration | wc -l` = **155** contiguous(V1–V155, 갭·중복 0).
- **결론**: **신규 V156 불필요** — G21 NHIS comparison deepen·live-e2e seed는 기존 인덱스·NHIS import 제약 위 읽기/시드 전용. ERD §7 검증 헤더(round 167)·메타 timestamp + 본 #159. **보류**: 이동서비스일지④ 시간 tolerance DB enforce(P2)·`waypoint_label` 길이/공백 정책(P3)·L02 M05 투약·`staff_attendance`/`staff_schedules`(Should)·`billing_payments`(Epic L). **coder**: 추가 DDL 0건 — 스키마 영향 없음.

#### #158. G21 confirm-readiness 분리 카운트 · 방문 NHIS 비교 API · 신규 DDL 0건 (2026-06-18, round 166, backend `8a8c5b3`)
- **배경**: round 165(#157 「G15 export 심화·V156 불필요」, backend `72124f7`) → backend HEAD **`8a8c5b3`** 6커밋 전진 — `6aeafe7` **plan-billing readiness split counts** 노출·`28860ae` readiness split blocker counts 심화·`f26abb0` per-kind ready flags·blocker messages on confirm-readiness·`5f710e3` 미배정 DRAFT batch confirm 차단·`03a052a` **`GET /visits/nhis-comparison`**(batch-confirm 사전 client별 방문일수 vs 최신 NHIS 배치 비교)·`8a8c5b3` confirm-readiness에 NHIS 비교 summary 임베드. **전부 앱 only**(G21 방문요양 batch-confirm 사전 점검 UX 심화).
- **`git diff --name-only 72124f7..8a8c5b3 -- src/main/resources/db/migration/`** = **0파일**, **`… -- '**/*Entity.java' '**/*Repository.java'`** = **0파일**(coder 신규 테이블·컬럼·엔티티·레포지토리·마이그레이션 0건). `VisitScheduleRepository` 미변경 — `03a052a`가 호출한 `findByOrganizationIdAndBranchIdAndScheduleKindAndVisitDateBetweenOrderByVisitDateAscPlannedStartTimeAsc`는 기존 보유 메서드(`GET /visits?kind=`과 공유).
- **G21 NHIS 비교 API DB backing 대조** (`VisitService` NHIS comparison — 신규 조회 인덱스 0건):
  - ① **PLAN 일정 범위** — `findBy…ScheduleKindAndVisitDateBetween…` → **V53** `idx_visit_schedules_org_branch_kind_date` `(org, branch, schedule_kind, visit_date DESC)` 3-equality + visit_date range prefix-exact. `planned_start_time` 동일자 tiebreak는 지점×기간 bounded 결과 in-memory sort(`GET /visits?kind=` 동일 backing) → 전용 인덱스 불요.
  - ② **최신 NHIS 배치** — `NhisImportBatchRepository.findScopedBatches`(org+branch, `createdAt DESC`) → **V38** `idx_nhis_import_batches_org_branch_created`(+ **V27** `…_org_branch_month_created` month variant).
  - ③ **배치 행** — `NhisImportRowRepository.findByBatchIdOrderByCreatedAtAsc` → **V28** `idx_nhis_import_rows_batch_created` `(batch_id, created_at ASC)`.
  - ④ **이용자 batch 조회** — `clientRepository.findByOrganizationIdAndIdIn(org, ids)` → **V5** `uq_clients_org_id` `(organization_id, id)`.
  - confirm-readiness split counts·per-kind ready flags·blocker 메시지·미배정 DRAFT 차단은 동일 list 쿼리 결과를 **인메모리 집계** — 신규 count `@Query`·DDL 0건.
- **Must billing·attendance·NHIS 핵심 제약 7건** SQL 물리 재확인 — **전부 불변**(`uq_claim_branch_month` V1·`uq_billing_claim_items_claim_client` V26·`chk_billing_claims_amount_sum` V6·`trg_billing_claims_total_reconciliation` V11·`chk_attendance_presence_xor_absence` V11/V14·`uq_nhis_import_rows_org_id` V37·`chk_nhis_import_rows_match_requires_client` V19→V54). agents.yaml `core_entities` 11종 전수 충족. `ls db/migration | wc -l` = **155** contiguous(V1–V155, 갭·중복 0).
- **결론**: **신규 V156 불필요** — G21 confirm-readiness·NHIS 비교 사전 점검은 기존 V53/V27/V38/V28/V5 인덱스 위 읽기 전용. ERD §7 검증 헤더(round 166)·메타 timestamp + 본 #158. **보류**: 이동서비스일지④ 시간 tolerance DB enforce(P2)·`waypoint_label` 길이/공백 정책(P3)·L02 M05 투약·`staff_attendance`/`staff_schedules`(Should)·`billing_payments`(Epic L). **coder**: 추가 DDL 0건 — 스키마 영향 없음.

#### #157. G15 이동서비스일지 export 심화 · 신규 DDL 0건 (2026-06-18, round 165, backend `72124f7`)
- **배경**: round 164(#156 「V155 WAYPOINT 주소 비공백 제약」, V155 commit = `64c4c80`) → backend HEAD **`72124f7`** 6커밋 전진 — `2d98040` live-e2e bootstrap transport roster seed·`a179256` **V155 WAYPOINT 주소 검증 테스트 보강**(앱 단위 테스트만)·`a8e2bb2` 서비스일지 export 지점 연락처(주소·지역경로·전화)·`e358f2d` export row `pickupAddress` 노출·`8cf09d8` live-e2e probe blocker 의미 정정·`72124f7` 서비스일지 export `direction` 노출. **전부 앱 only**(별지 제22호 이동서비스일지 인쇄·공단 청구 reconcile 콘텐츠 보강).
- **`git diff --name-only 64c4c80..72124f7 -- src/main/resources/db/migration/`** = **0파일**, **`… -- '**/*Entity.java' '**/*Repository.java'`** = **0파일**(coder 신규 테이블·컬럼·엔티티·레포지토리·마이그레이션 0건). `git diff 64c4c80..72124f7`에서 `CREATE TABLE`/`ALTER TABLE`/`@Entity`/`@Column`/`@Query` 매치 **0건**.
- **G15 export 신규 노출 필드 DB backing 대조** (`TransportService.getServiceLog` — 신규 조회 인덱스 0건):
  - ① **`direction`** → `transport_runs.direction`(V47 `VARCHAR(20) NOT NULL DEFAULT 'PICKUP'` + V146 `chk_transport_runs_direction IN ('PICKUP','DROPOFF')`). 앱 `resolveRunDirection`의 공백 fallback(`hasText` 미충족 → PICKUP)은 DB NOT NULL+CHECK가 이미 빈/잘못된 값을 차단하므로 dead-defensive(무해·갭 아님). export note prefix `픽업:`/`하차:` 분기는 이 컬럼만 사용.
  - ② **`branchAddress`/`branchPhone`/`branchRegionPath`** → `branches.address_line1`·`phone_encrypted`·`region_dong_code`(V51). `requireBranch(org, branchId)`는 PK 조회. `BranchLocationResolver.resolveRegionPath` → `RegionLookupService.resolvePath`는 `region_dongs.code`(PK·V51)→`region_sigungus`/`region_sidos` `findById`(PK) 3 PK 조회뿐 — **export당 1회**(지점 단위, row 단위 아님). 신규 인덱스 불요.
  - ③ **row `pickupAddress`** → `clientRepository.findAllById(clientIds)`(PK batch) + `transportAddressService.resolvePickupAddressPlain(client)`. 기존 stop 조회(`idx_transport_run_stops_run_order`) 재사용.
- **Must billing·attendance·NHIS 핵심 제약 7건** SQL 물리 재확인 — **전부 불변**(`uq_claim_branch_month` V1·`uq_billing_claim_items_claim_client` V26·`chk_billing_claims_amount_sum` V6·`trg_billing_claims_total_reconciliation` V11·`chk_attendance_presence_xor_absence` V11/V14·`uq_nhis_import_rows_org_id` V37·`chk_nhis_import_rows_match_requires_client` V19→V54). agents.yaml `core_entities` 11종 전수 충족(`transport_runs`는 transport 도메인 — core_entities 외 G15 법정 일지). `ls db/migration | wc -l` = **155** contiguous(V1–V155, 갭·중복 0).
- **결론**: **신규 V156 불필요** — G15 export 심화는 기존 PK/인덱스 위 읽기 전용 노출(direction은 기존 NOT NULL+CHECK로 이미 보호). ERD §7 검증 헤더(round 165)·메타 timestamp + 본 #157. **보류**: 이동서비스일지④ 시간 tolerance DB enforce(P2)·`waypoint_label` 길이/공백 정책(P3)·L02 M05 투약·`staff_attendance`/`staff_schedules`(Should)·`billing_payments`(Epic L 부분입금). **coder**: 추가 DDL 0건 — 스키마 영향 없음. BE WT 변경 시 `mvn test` 재검증.

#### #156. V155 WAYPOINT 주소 비공백 제약 · Must 재대조 0건 (2026-06-18, round 164, backend `dac19d3`)
- **배경**: round 163(#155 「V154 운전자 서명·신규 V155 불필요」·`waypoint_address` TRIM nonempty CHECK를 P2 보류) → backend HEAD `bc3a35c` → **`dac19d3`**(21파일 전진 — G21 RFID transmission diff compare·live-e2e bootstrap·VisitService check-in assigned-user guard·테스트, **앱 only**).
- **`git diff --name-only bc3a35c..dac19d3 -- src/main/resources/db/migration/`** = **0파일**, **`… -- '**/*Entity.java' '**/*Repository.java'`** = **0파일**(coder 신규 엔티티·레포지토리·마이그레이션 0건). 신규 VisitService 쿼리(`userRepository.findByIdAndOrganizationId` PK·`userBranchRepository.existsByOrganizationIdAndUserIdAndBranchId`)는 V90 `uq_user_branches_org_user_branch`로 **이미 backing** — 신규 인덱스 불요.
- **DBA 신규 V155 `transport_run_stops_waypoint_address_nonempty`** — round 153~155에서 P2로 반복 보류하던 「WAYPOINT 주소 공백 거부는 앱 책임」 갭을 DB 레벨로 해소:
  - ① **근거** — V151 `chk_transport_run_stops_client_kind`가 WAYPOINT에 `waypoint_address IS NOT NULL`만 강제 → `''`/whitespace 적재 가능. 공백 주소는 배달 불가 정차·지오코딩 실패·별지 제22호 이동서비스일지 빈 칸을 유발. V154 운전자 서명 `btrim(name)<>''`·V65 transport contract pair-CHECK와 동일한 방어 패턴 부재(비대칭).
  - ② **DDL** — 추가 제약 1건만(`chk_transport_run_stops_waypoint_address_nonempty`: `stop_kind<>'WAYPOINT' OR (waypoint_address IS NOT NULL AND btrim(waypoint_address)<>'')`). 기존 `chk_*_stop_kind`(V151)·`chk_*_client_kind`(V151)·`trg_*_guard_client`(V152)·`trg_*_enforce_max`(V143) **전부 불변** → 후속 integrity 마이그레이션 불요·테이블 재작성 0.
  - ③ **데이터 안전** — `rg waypoint_address|WAYPOINT` migration·`scripts/` 전수 = WAYPOINT 적재 seed **0건** → backfill 불요·Flyway clean DB migrate 안전. CLIENT/BRANCH 정차는 `stop_kind<>'WAYPOINT'` short-circuit으로 무영향.
  - ④ **앱 정합** — `TransportService`는 이미 `"  "` 공백 주소를 service-layer에서 거부(`createRunShouldRejectWaypointWithoutAddress` 단위 테스트 — mock 기반이므로 DB 제약 무영향). V155는 raw SQL·우회 경로 1차 방어(defense-in-depth).
- **Must billing·attendance·NHIS 핵심 제약 7건** SQL 물리 재확인 — **전부 불변**(`uq_claim_branch_month` V1·`uq_billing_claim_items_claim_client` V26·`chk_billing_claims_amount_sum` V6·`trg_billing_claims_total_reconciliation` V11·`chk_attendance_presence_xor_absence` V11/V14·`uq_nhis_import_rows_org_id` V37·`chk_nhis_import_rows_match_requires_client` V19→V54). agents.yaml `core_entities` 11종 전수 충족(`transport_run_stops`는 transport 도메인 — core_entities 외, US-T02 cluster). `ls db/migration | wc -l` = **155** contiguous(V1–V155, 갭·중복 0).
- **결론**: **V155 신규**. ERD §1 V155 행·§4-9 정차 종류 규칙·§7 마이그레이션 V155 행·헤더 DDL 범위 `…V155`·§7 검증 헤더(round 164) + 본 #156. **보류**: 이동서비스일지④ 시간 tolerance DB enforce(P2)·`waypoint_label` 길이/공백 정책(P3)·L02 M05 투약·`staff_attendance`/`staff_schedules`(Should)·`billing_payments`(Epic L). **coder**: V155 `mvn flyway:migrate`·`mvn test` 재검증(추가 제약은 mock 단위 테스트 무영향 — BE Test PASS 유지 예상).

#### #155. V154 G15 운전자 서명 영속화 · Must 재대조 0건 (2026-06-18, round 163, backend `bc3a35c`)
- **배경**: round 162(#154 「V153 PAID 청구 paid_at partial 인덱스」) → backend HEAD `09df8c7` → **`bc3a35c`**(workspace_baseline 2026-06-18T05:25Z). coder가 **V154 `transport_service_log_driver_signature`**(BNK-346 P2 Must deepen)를 추가 — V148 일지④(동승자·실제 탑승·동승·하차)에 이어 별지 제22호 운전자 서명자명(VARCHAR(120))·서명일(DATE)을 영속화. FE `f51e365`에 driver wire 동반(workspace_baseline 注).
- **`git diff --name-only 09df8c7..bc3a35c -- src/main/resources/db/migration/`** = **V154 1파일**(coder). `ls db/migration | wc -l` = **154** contiguous(V1–V154, 갭·중복 0).
- **V154 integrity 대조** (V148 nullable VARCHAR/TIME 추가·V65 transport contract pair CHECK 패턴):
  - ① **DDL은 ALTER ADD COLUMN 2건 + ADD CONSTRAINT 1건만** — 신규 UK·FK·트리거·인덱스 0건. `transport_runs`는 V47 org/branch sync·복합 Tenant FK·`trg_transport_runs_set_actors` actor backstop을 **이미 보유** → 동일 행 upsert에 후속 integrity 마이그레이션 **불필요**(§7-74 V148 동일 패턴, §7-72 V146 nullable TIME 패턴).
  - ② **pair CHECK 정합** — `chk_transport_runs_service_log_driver_signature_pair`가 `(name IS NULL AND signed_on IS NULL) OR (name IS NOT NULL AND btrim(name)<>'' AND signed_on IS NOT NULL)` 강제. `TransportServiceLogService.upsert`(앱)는 항상 둘 다 채우거나 둘 다 NULL을 보냄 → 항상 충족. raw SQL `UPDATE transport_runs SET service_log_driver_signatory_name='...'` 한쪽 적재·공백 이름 1차 방어(V65 transport contract `signed_on`/`signatory_name` pair CHECK 패턴).
  - ③ **purge·감사 정합** — 운행일(`run_date`) 2년 cohort(DATA_RETENTION §3) — stop·companion·서명 컬럼이 stop/run 행과 함께 purge(`idx_transport_runs_org_branch_date`). upsert 감사는 V148 동일 `audit_logs` `TRANSPORT_SERVICE_LOG_UPSERT`(§7-75) 재사용 — 별도 action·테이블 미신설(`AuditLogWriter.record` 호출 시 서명 변경도 details JSON 포함 가능).
- **Repository 영향**: `TransportRunRepository`·`TransportRunStopRepository` 신규 쿼리 0건. CONFIRMED run 단건 조회(`findById…`)·service-log audit trail 조회(V6 `idx_audit_logs_target`) 모두 기존 인덱스 재사용 — **신규 조회 인덱스 0건**.
- **Must billing·attendance·NHIS 핵심 제약 7건** SQL 물리 재확인 — **전부 불변**(`uq_claim_branch_month` V1·`uq_billing_claim_items_claim_client` V26·`chk_billing_claims_amount_sum` V6·`trg_billing_claims_total_reconciliation` V11·`chk_attendance_presence_xor_absence` V11/V14·`uq_nhis_import_rows_org_id` V37·`chk_nhis_import_rows_match_requires_client` V19→V54). agents.yaml `core_entities` 11종 전수 충족 — `transport_runs`는 transport 도메인(V148 영속화 cluster), `core_entities` 외 G15 법정 일지 확장.
- **결론**: **신규 V155 integrity 마이그레이션 불필요**. ERD §4-9 transport_runs 컬럼·서비스일지④ 규칙·§7-78 신설·§7 마이그레이션 V154 행·§7 검증 헤더(round 163)·§8 `/transport/runs/{runId}/service-log` 매핑·헤더 DDL 범위 갱신 + DATA_RETENTION §2 운전자 서명 분류·§3 transport cohort 행·§6 audit 필수 기록·§8 coder 메모 + 본 #155. **보류**: 이동서비스일지④ 시간 tolerance DB enforce(P2)·`waypoint_address` TRIM nonempty CHECK(P2)·L02 M05 투약·`staff_attendance`/`staff_schedules`(Should)·`billing_payments`(Epic L). **coder**: BE WT 4M 미커밋 변경 commit·push 후 `mvn flyway:migrate`·`mvn test` 재검증(BE Test 207 PASS 유지 예상).

#### #154. V153 billing paid_at report index · live-e2e bootstrap · Must 재대조 0건 (2026-06-17, round 162, backend `09df8c7`)
- **배경**: round 161(#153 「V153 불필요」·`paid_at` partial 인덱스 P2 보류) → **`09df8c7`** 5커밋 전진(live-e2e bootstrap·actuator alias·guardian credential hardening, 앱 only). DBA가 V71 `refunded_at` partial과 비대칭인 PAID `paid_at DESC` 조회 backing을 **V153**으로 해소.
- **`git diff --name-only dd2fa2c..09df8c7 -- src/main/resources/db/migration/`** = **0파일**(coder). DBA **V153 1파일** 신규. `ls db/migration | wc -l` = **153** contiguous.
- **V153 integrity 대조**:
  - ① `idx_billing_claims_org_branch_status_paid_at` — partial `(org, branch, status, paid_at DESC) WHERE status='PAID'`, V71 `idx_billing_claims_org_branch_status_refunded_at` 대칭.
  - ② `BillingClaimRepository.findByOrganizationIdAndBranchIdAndStatusOrderByPaidAtDesc` → G26 ① `buildMedicalExpenseDeductionReportItems`·7-7/7-8 `buildPaymentReportItems`(deposits/receipts).
  - ③ V50 `chk_billing_claims_paid_requires_metadata`가 PAID 행 `paid_at` NOT NULL — partial predicate에 `paid_at IS NOT NULL` 중복 불필요.
- **Must billing·attendance·NHIS 핵심 제약 7건** SQL 물리 재확인 — **전부 불변**. agents.yaml `core_entities` 11종 전수 충족.
- **결론**: **V153 신규**. ERD §4-6·§6·§7-48·§8·round 162 검증 헤더 + DATA_RETENTION §4 + 본 #154. **보류**: `waypoint_address` TRIM nonempty CHECK(P2)·L02 M05 투약·`staff_attendance`/`staff_schedules`(Should)·`billing_payments`(Epic L).

#### #153. V150–V152 transport waypoint cluster · V152 is_active guard fix · Must 재대조 0건 (2026-06-17, round 161, backend `dd2fa2c`)
- **배경**: round 160(`f0e52b8`/PLAN_NOTES #152 「V150 불필요」) → coder **`0e46b37`** **V150 `planned_departure_time`**·**`de3474d`** **V151 arbitrary address WAYPOINT**·**`dd2fa2c`** **V152 `is_active` guard fix** + settings validation(앱 only).
- **`git diff --name-only f0e52b8..HEAD -- src/main/resources/db/migration/`** = **V150–V152 3파일**. `ls db/migration | wc -l` = **152** contiguous.
- **V150–V152 integrity 대조** (DBA 신규 DDL 0건 — coder 작성분 검증·문서화):
  - ① **V150** — `transport_runs.planned_departure_time` nullable TIME. V47 org/branch sync·actor backstop 보유 → 후속 integrity 불필요.
  - ② **V151** — `stop_kind` `WAYPOINT`·`waypoint_address`(NOT NULL when WAYPOINT)·`waypoint_label`(nullable)·CHECK·`trg_*_guard_client` REPLACE. `trg_transport_run_stops_enforce_max`(V143)는 CLIENT 15·TOTAL 17만 검사 → WAYPOINT는 TOTAL에만 포함(정합). 공백 주소 거부는 앱 책임.
  - ③ **V152** — V143이 `clients.active`(미존재 컬럼) 참조 → CLIENT 정차 guard 항상 실패. `is_active`로 REPLACE만 수행.
- **Must billing·attendance·NHIS 핵심 제약 7건** SQL 물리 재확인 — **전부 불변**. agents.yaml `core_entities` 11종 전수 충족.
- **결론**: **신규 V153 불필요**. ERD §4-9·§7-77·§8·round 161 검증 헤더 + DATA_RETENTION §2/§3 waypoint + 본 #153. **보류**: `waypoint_address` TRIM nonempty CHECK(P2)·L02 M05 투약·`staff_attendance`/`staff_schedules`(Should)·`billing_payments`(Epic L)·`paid_at` partial 인덱스(P2).

#### #152. V149 Must billing·attendance query indexes · live-e2e bootstrap · Must 재대조 0건 (2026-06-17, round 160, backend `f0e52b8`)
- **배경**: round 158(`6eb9cc0`/PLAN_NOTES #151 「V149 불필요」) → coder **`4f974fd`** **V149 `attendance_billing_must_query_indexes`** 추가 → **`f0e52b8`** 4커밋 전진(live-e2e bootstrap·actuator alias·seed conflict 복구, 앱 only).
- **`git diff --name-only 6eb9cc0..HEAD -- src/main/resources/db/migration/`** = **V149 1파일**. `ls db/migration | wc -l` = **149** contiguous.
- **V149 integrity 대조** (DBA 신규 DDL 0건 — coder 작성분 검증·문서화):
  - ① `idx_attendance_org_branch_date_client_checkout` — partial `(org, branch, attendance_date, client_id) WHERE check_out_at IS NOT NULL`. V25 check_in partial·V22 일 단위 checkout과 상호 보완. `GET /attendance/stats/monthly` 1차 backing은 V25(`countBy…CheckInAtIsNotNull`) 유지.
  - ② `idx_billing_claims_org_branch_month_status_generated` — `(org, branch, year_month DESC, status, generated_at DESC)`. V31·V1·V22 단일축 보완. G26 ② `findBy…YearMonthOrderByGeneratedAtDesc` 12회/요청.
- **Must billing·attendance·NHIS 핵심 제약 7건** SQL 물리 재확인 — **전부 불변**. agents.yaml `core_entities` 11종 전수 충족.
- **결론**: **신규 V150 불필요**. ERD §4-4·§4-6·§6·§7-76·§7 마이그레이션 V149 행·round 160 검증 헤더 + 본 #152. **보류**: L02 잔여 leaf(M05 투약)·`staff_attendance`/`staff_schedules`(Should)·`billing_payments`(Epic L)·`paid_at` partial 인덱스(P2).

#### #151. G15 service-log audit trail · transport monthly reports · Must 재대조 0건 (2026-06-17, round 158, backend `6eb9cc0`)
- **배경**: round 157(`c13800c`/V148 carry) → **`6eb9cc0`** 5커밋 전진 — `aa42b9c` **G15 service-log upsert audit**(`audit_logs` `TRANSPORT_SERVICE_LOG_UPSERT`)·`5994d15` **`GET /transport/runs/{runId}/service-log/audit-trail`**·`5d27ad3` **transport monthly reports 2-7/2-8**·`6eb9cc0` live-e2e bootstrap(앱 only).
- **`git diff --name-only c13800c..HEAD -- src/main/resources/db/migration/`** = **0파일**. `ls db/migration | wc -l` = **148** contiguous.
- **G15 audit trail 대조** (신규 DDL 0건):
  - ① **저장소** — 별도 `transport_service_log_audit` 테이블 없음. `PUT …/service-log` 성공 시 `AuditLogWriter.record` → `audit_logs` append(`action=TRANSPORT_SERVICE_LOG_UPSERT`, `target_type=transport_run`, `details`: runDate·stopUpdateCount·recorded/onTime/total).
  - ② **읽기** — `AuditLogRepository.findByOrganizationIdAndTarget` 신규 메서드 → V6 `idx_audit_logs_target` prefix + `action` post-filter, limit 50. run 단위 상한이므로 **신규 인덱스 불요**.
  - ③ **보존** — `audit_logs` Tenant `audit_retention_days` 정책(§3). V148 일지④ 본문 컬럼은 `transport_runs`/`transport_run_stops` 2년 cohort와 동반 purge.
- **Transport monthly reports 대조** — `TransportMonthlyReportService`가 `clients`·`transport_runs`·`transport_run_stops`·`transport_service_contracts` 읽기 전용 집계(func 2-7/2-8). V47/V64/V32 기존 인덱스 재사용, 신규 `@Query`·DDL 0건.
- **Must billing·attendance·NHIS 핵심 제약 7건** SQL 물리 재확인 — **전부 불변**. agents.yaml `core_entities` 11종 전수 충족.
- **결론**: **신규 V149 불필요**. ERD §4-7·§4-9·§7-75·§8 audit-trail·monthly-reports + DATA_RETENTION §3 transport V148 + 본 #151. **보류**: L02 잔여 leaf(M05 투약)·`staff_attendance`/`staff_schedules`(Should)·`billing_payments`(Epic L)·`paid_at` partial 인덱스(P2)·`idx_audit_logs_org_action_target` partial(P2).

#### #150. V147 guardian 링크 트리거 `updated_at` 정정 검증 · Must 재대조 0건 (2026-06-17, round 156, backend `8a1f342`)
- **배경**: round 155(`114411f`/§7-72에서 「V147 integrity 후속 불필요」 결론) 이후 coder가 **V147**(`22396e0` `fix(v2/live-e2e): align client consent timestamps for guardian bootstrap (QA-B95)` 번들)을 추가 — **transport 무관**, V39 guardian 링크 트리거의 `updated_at` 산식 정정. `git diff --name-only 114411f..HEAD -- src/main/resources/db/migration/` = **V147 1파일**. `ls db/migration | wc -l` = **147** contiguous(V1–V147, 갭·중복 0).
- **V147 정합성 검증 (DBA 신규 DDL 0건 — coder 작성분 확인)**:
  - ① **버그 근원**: V39 `trg_guardian_clients_refresh_link_status`(AFTER INSERT/DELETE on `guardian_clients`)가 부모 `clients.updated_at = NOW()`로 갱신. PostgreSQL `NOW()`는 **트랜잭션 시작 시각 고정**인데 Hibernate가 동일 트랜잭션에서 `clients.created_at`을 더 늦게(문장 수준) 적재 → 이용자+보호자 **단일 트랜잭션 생성** 시 `updated_at < created_at`으로 V37 `chk_clients_updated_after_created` 위반 가능(QA-B95 guardian bootstrap live-e2e에서 노출).
  - ② **정정**: V147이 함수 본문만 `CREATE OR REPLACE` → `updated_at = GREATEST(created_at, NOW())`. 트리거 바인딩·컬럼·CHECK·인덱스 불변 → 테이블 재작성·테스트 영향 0건.
  - ③ **잔여 위험 스캔**: `updated_at = NOW()`(또는 `CURRENT_TIMESTAMP`/`clock_timestamp`) 트리거 패턴을 V1–V147 전수 `rg` 물리 확인 — **V39 단 1건뿐**. 그 외 `chk_*_updated_after_created` 38개 테이블의 `updated_at`은 전부 Hibernate(애플리케이션) 관리 → 동일 잠재 버그 **잔여 0건**.
- **#146 정정 보완**: round 152 #146에서 「V39 트리거는 `NOW()`로 CHECK를 항상 충족」으로 본 ERD §7-34 가설이 **폐기** — `GREATEST` 정정 반영. ERD §7-34 노트에 ⚠ 폐기 가설 명시.
- **Must billing·attendance·NHIS 핵심 제약 7건** SQL 물리 재확인 — **전부 불변**(`uq_claim_branch_month` V1·`uq_billing_claim_items_claim_client` V26·`chk_billing_claims_amount_sum` V6·`trg_billing_claims_total_reconciliation` V11·`chk_attendance_presence_xor_absence` V11/V14·`uq_nhis_import_rows_org_id` V37·`chk_nhis_import_rows_match_requires_client` V19→V54). agents.yaml `core_entities` 11종 전수 충족(`medications`→`health_records.record_type='medication'`).
- **결론**: **신규 V148 불필요**. ERD §7-73 V147 행·§7 마이그레이션 목록 V147 행·§7-34 ⚠ 폐기 가설·헤더 DDL 범위 `…V147` + DATA_RETENTION 메타 timestamp(트리거 정정은 보존·purge 무영향) + 본 #150. **보류**: L02 잔여 leaf(M05 투약)·`staff_attendance`/`staff_schedules`(Should)·`billing_payments`(Epic L)·`paid_at` partial 인덱스(P2).

#### #149. V143–V146 transport cluster deepen · Must billing·attendance 재대조 0건 (2026-06-17, round 155, backend `114411f`)
- **배경**: round 154(`7ac0a46`/V142 carry) → **`114411f`** 2커밋 전진 — `f5b2b42` **V143 `transport_run_stops` BRANCH waypoint**·**V144 `vehicles.default_driver_id`**·`114411f` **V145 `default_driver_name`**·**V146 `clients.desired_boarding/dropoff_time`+`DROPOFF` direction**(BNK-286~291·결정 96·US-T02).
- **`git diff --name-only 7ac0a46..HEAD -- src/main/resources/db/migration/`** = **V143–V146 4파일**. coder develop 커밋 완료 — DBA 신규 DDL 추가 **0건**.
- **V143–V146 integrity 대조**:
  - ① **V143 self-contained** — `stop_kind` CHECK·partial UK·`client_id` nullable·트리거 3건 REPLACE를 단일 마이그레이션에 포함 → 별도 V147 불필요.
  - ② **V144** Tenant FK `(org, default_driver_id)→users` + partial index — `user_branches` 배정 FK·TERMINATED 가드는 앱 책임(name 우선 정책).
  - ③ **V145** backfill UPDATE only.
  - ④ **V146** nullable TIME 2건 + direction CHECK — V120/V122 partial UK가 `direction` 포함(PICKUP/DROPOFF 각 1건 허용).
- **Must billing·attendance·NHIS 핵심 제약 7건** SQL 물리 재확인 — **전부 불변**. agents.yaml `core_entities` 11종 전수 충족(`medications`→`health_records.record_type='medication'`). `ls db/migration | wc -l` = **146** contiguous.
- **결론**: **신규 V147 불필요**. ERD §4-3/§4-9/§7-72/§8·DATA_RETENTION §2/§3 + 본 #149. **보류**: L02 잔여 leaf(M05 투약)·`staff_attendance`/`staff_schedules`(Should)·`billing_payments`(Epic L)·`paid_at` partial 인덱스(P2).

#### #148. live-e2e bootstrap deepen · L02 nursing report pilot E2E · Must 재대조 0건 (2026-06-16, round 154, backend `7ac0a46`)
- **배경**: round 153(`f6f1756`/V142 carry) → **`7ac0a46`** 5커밋 전진 — `304bb2a`/`f5205e3`/`ec142db` live-e2e bootstrap·guardian bootstrap·onboarding support seed(QA-B95)·`2ba2761` L02 care-scoped nursing report pilot E2E(BNK-280)·`7ac0a46` role-mismatched seed guard.
- **`git diff --name-only f6f1756..HEAD -- src/main/resources/db/migration/`** = **0파일**. `git diff f6f1756..HEAD -- '**/*Repository.java' '**/*Entity.java'`** = **0파일**.
- **live-e2e bootstrap DB backing 대조** (신규 테이블·컬럼·Repository 0건):
  - Tenant/지점/직원 — `LiveE2eBootstrapService.bootstrap()`이 `organizations`·`branches`·`users`·`user_branches` 고정 UUID upsert(V1/V4/V29).
  - 보호자 bootstrap — `POST /api/v1/live-e2e/bootstrap-guardian`이 `users`·`guardian_clients` 연결 upsert(V2/V5).
  - onboarding support — `ensureBranchOnboardingSupport` → `branch_onboarding_support`(V126/V127) `findByOrganizationIdAndBranchId` 1쿼리.
- **L02 nursing report pilot E2E** — `CareNursingReportsPilotServiceFlowE2eTest`가 `GET /care/reports/nursing-service` 검증; backing은 V123 `idx_nursing_service_records_org_branch_service_date`(round 153 #147과 동일).
- **Must billing·attendance·NHIS 핵심 제약 7건** SQL 물리 재확인 — **전부 불변**. agents.yaml `core_entities` 11종 전수 충족. `ls db/migration | wc -l` = **142** contiguous.
- **결론**: **신규 V143 불필요**. ERD §7 round 154 검증 헤더 + 본 #148. **보류**: L02 잔여 leaf(M05 투약)·`staff_attendance`/`staff_schedules`(Should)·`billing_payments`(Epic L)·`paid_at` partial 인덱스(P2).

#### #147. G26 ③ transport fee statistics · L02 care report proxies · Must 재대조 0건 (2026-06-17, round 153, backend `f6f1756`)
- **배경**: round 150(`3481eb8`/V142 carry) → **`f6f1756`** 11커밋 전진 — `3672bbe` **G26 ③ `GET /billing/reports/transport-service-fee-statistics`**·`98ef09b` **L02_M16 `GET /care/reports/meal-preference`**·`002e3eb` **L02_M14 `GET /care/reports/nursing-service`**(care-scoped nursing proxy)·`e54a699` G21 UNPAIRED fix·`39f5f4e` J03 quiet-hours dispatch reject·`30f03e8`/`f6f1756` G26 pilot E2E·live-e2e bootstrap hardening.
- **`git diff --name-only 3481eb8..HEAD -- src/main/resources/db/migration/`** = **0파일**. G26 ③·L02 리포트 3커밋 구간 신규 DDL **0건**.
- **G26 ③ DB backing 대조** (신규 테이블·컬럼·Repository 0건):
  - `TransportServiceFeeRecordRepository.findByOrganizationIdAndBranchIdAndServiceDateBetweenOrderByServiceDateDescClientIdAsc` → V68 `idx_transport_service_fee_records_org_branch_date` prefix-exact; 12개월 `YearMonth` 버킷·CONFIRMED/DRAFT 금액 분리는 인메모리.
- **L02 care report proxy 대조** (신규 조회 인덱스 0건):
  - meal-preference — `MealPreferenceSurveyService.list` → V142 `idx_meal_preference_surveys_org_branch_date`.
  - nursing-service — `NursingServiceRecordService.getTotalReport` → V123 `idx_nursing_service_records_org_branch_service_date`(L03 `/nursing/service-records/reports/total`과 동일 backing).
- **Must billing·attendance·NHIS 핵심 제약 7건** SQL 물리 재확인 — **전부 불변**. agents.yaml `core_entities` 11종 전수 충족. `ls db/migration | wc -l` = **142** contiguous.
- **결론**: **신규 V143 불필요**. ERD §7-48 G26 ③·§8 3행·round 153 검증 헤더 + 본 #147. **G26 3-function(①②③) DB backing 완성**. **보류**: L02 잔여 leaf(M05 투약)·`staff_attendance`/`staff_schedules`(Should)·`billing_payments`(Epic L)·`paid_at` partial 인덱스(P2).

#### #146. core_entities 재대조 — `medications` 물리 매핑 명시 필요 (2026-06-16, round 152, workspace HEAD)
- **배경**: 사용자 지시(ERD·migration·API_SPEC 재대조, billing·attendance Must 커버리지 점검)에 따라 `agents.yaml` `db_architect.core_entities` 11종과 `V1..V142`/`API_SPEC`를 교차 검증.
- **검증 결과**:
  - `attendance`·`billing` 계열은 테이블·제약·인덱스가 이미 충분히 존재(핵심 가드: 출석 XOR/temporal·청구 상태 전이/합계 정합·NHIS 매칭 제약·tenant FK).
  - 누락 테이블/인덱스/제약 신규 추가 대상은 확인되지 않음(**신규 migration 불필요**).
  - 단, `core_entities.medications`는 별도 물리 테이블이 아니라 `health_records.record_type='medication'` 도메인 모델로 구현되어 있어 문서만 보면 오해 가능.
- **조치**: `docs/technical/ERD.md` §8 API_SPEC 매핑 표에 `POST /clients/{clientId}/health/medications` → `health_records(record_type='medication')` 행을 추가해 **core_entities↔물리 스키마 매핑을 명시**.
- **결론**: 이번 라운드는 문서 정합화로 종료. 신규 DDL은 보류가 아니라 **불필요(0건)**.

#### #145. G26 7-8 dual-function statistics · Must billing·attendance 재대조 0건 (2026-06-17, round 150, backend `3481eb8`)
- **배경**: round 149(`b38c6f7`/V142 carry) → **`3481eb8`** 6커밋 전진 — `903f462` **G26 ① `GET /billing/reports/medical-expense-deduction-statistics`**(지점·귀속연도별 이용자 의료비공제 집계·페이지네이션)·`6d10e0d` **G26 ② `GET /billing/reports/copay-monthly-statistics`**(연 12개월 본인부담 6필드·PDF p.92 verbatim)·`472cb1d` live-e2e bootstrap tenant-scope fix·`1840640`/`92ae60b`/`3481eb8` pilot E2E·live API routing harness. FE `/billing/reports/statistics` @ `d8f1fdf`(planner 150차).
- **`git diff --name-only b38c6f7..HEAD -- src/main/resources/db/migration/`** = **0파일**. `472cb1d`·G26 4커밋 구간 신규 DDL **0건**.
- **G26 DB backing 대조** (신규 테이블·컬럼·Repository 0건):
  - ① **의료비공제 통계** — `BillingService.listMedicalExpenseDeductionReport` → `billingClaimRepository.findByOrganizationIdAndBranchIdAndStatusOrderByPaidAtDesc` → V5 `idx_billing_claims_org_branch_status` prefix + 인메모리 `isPaidInTaxYear`·`isEligibleMedicalExpensePayment`(CMS/EASY_PAY 제외); 이용자별 `billingClaimItemRepository.findByClaimIdOrderByCreatedAtAsc` → V29 `idx_billing_claim_items_claim_created`.
  - ② **본인부담 월별 통계** — `BillingService.listCopayMonthlyStatistics` → 12× `findByOrganizationIdAndBranchIdAndYearMonthOrderByGeneratedAtDesc` → V1 `idx_billing_claims_org_branch_month` + V22 `idx_billing_claims_org_branch_generated` prefix; 청구별 `sumClaimCopayAmount` → 동일 claim_items 인덱스. CONFIRMED=미수·PAID=입금·REFUNDED=청구건수 포함은 앱 상태 필터.
- **Repository ↔ 인덱스 backing 1:1 검증** (신규 조회 인덱스 0건): G26 2 API 모두 기존 `BillingClaimRepository`·`BillingClaimItemRepository` 메서드 재사용 — round 107 G26 이용자 단건(`findByOrganizationIdAndClientIdOrderByCreatedAtDesc` → V25)과 짝. `paid_at DESC` 전용 partial(`idx_billing_claims_org_branch_status_paid_at`)은 대형 Tenant 성능 관측 전 **P2 보류**.
- **Must billing·attendance·NHIS 핵심 제약 7건** SQL 물리 재확인 — **전부 불변**. agents.yaml `core_entities` 11종 전수 충족. `ls db/migration | wc -l` = **142** contiguous.
- **결론**: **신규 V143 불필요**. ERD §7-48·§8 G26 2행·round 150 검증 헤더 + 본 #145. **보류**: L02 잔여 leaf(M05 투약)·`staff_attendance`/`staff_schedules`(Should)·`billing_payments`(Epic L)·`paid_at` partial 인덱스(P2).

#### #144. V142 L02_M16 meal_preference_surveys · G21 billingClaimReflectionStatus · Must 재대조 0건 (2026-06-16, round 149, backend `b38c6f7`)
- **배경**: round 148(`ae7e744`/V141 carry) → **`b38c6f7`** 4커밋 전진 — `f33252a` **V142 `meal_preference_surveys`**(L02_M16·G-MEAL-PREFERENCE·케어포 view.meal_satisfaction)·`2cf0908` L02_M11/M12 care report BE·`6da49aa` **G21 `billingClaimReflectionStatus`** on visit list/detail·`b38c6f7` G21 pilot E2E.
- **`git diff --name-only ae7e744..HEAD -- src/main/resources/db/migration/`** = **V142 1파일**. `6da49aa`·`b38c6f7`·`2cf0908` 구간 신규 DDL **0건**.
- **V142 integrity 대조** (V141 교훈 — V140 actor partial 누락 재발 방지):
  - ① **self-contained DDL** — org/branch sync·퇴소 guard·actor backstop·client purge·list 인덱스·**actor partial `idx_meal_preference_surveys_org_recorded_by`** 모두 V142 단일 마이그레이션에 포함(coder `f33252a`가 V141 교훈 반영).
  - ② **V143 integrity 후속 불필요** — V140→V141 분리 패턴과 달리 actor partial 선행 포함.
- **Repository ↔ 인덱스 backing 1:1 검증** (신규 조회 인덱스 0건):
  - `findByOrganizationIdAndBranchIdAndSurveyDateBetweenOrderBySurveyDateDescMealTypeAscCreatedAtDescClientIdAsc` → V142 `idx_meal_preference_surveys_org_branch_date` prefix-exact·정렬 1:1.
  - `findByOrganizationIdAndBranchIdAndClientIdAndSurveyDateBetweenOrderBy…` → 동일 인덱스 + UK `(client, survey_date, meal_type)` cohort.
  - `findByIdAndOrganizationId` → PK + V142 UK `(org, id)`.
- **G21 billingClaimReflectionStatus DB 영향**: `VisitService.resolveBillingClaimReflectionStatus` — PLAN/BILLING 페어(`paired_schedule_id`·V56 `idx_visit_schedules_org_paired`)의 `visit_date`·`planned_start_time`·`planned_end_time` 슬롯 정합을 **인메모리 비교**해 `REFLECTED`/`NOT_REFLECTED`/`UNPAIRED` 반환. **신규 테이블·컬럼·인덱스·`@Query` 0건** — FE 검은/빨간 배지는 응답 필드만 사용(@ `25ca88e`).
- **Must billing·attendance·NHIS 핵심 제약 7건** SQL 물리 재확인 — **전부 불변**. agents.yaml `core_entities` 11종 전수 충족 — `meal_preference_surveys`는 `meal_records`(V49) L02 선호도 보완·별도 테이블. `ls db/migration | wc -l` = **142** contiguous.
- **결론**: **신규 V143 불필요**. ERD §4-11c·§4-12 G21·§6·§7 V142·§8 L02_M16/G21 + DATA_RETENTION §2/§3/§4-1 + 본 #144. **보류**: L02 잔여 leaf(M05 투약)·`staff_attendance`/`staff_schedules`(Should)·`billing_payments`(Epic L)·API_SPEC L02 § `/care/meal-preference-surveys` 행(coder/tech_writer).

#### #143. L02_M17 intensive-excretion report · V141 develop 커밋 · Must 재대조 0건 (2026-06-15, round 148, backend `ae7e744`)
- **배경**: round 147(`c655743`/V140·V141 DBA carry) → **`ae7e744`** 4커밋 전진 — `27b40cd` care report default date window·`e8b8398` **V141 develop 커밋**·`3eeac92` transport QA-B103(카카오 지도 API, DB 미신규)·`ae7e744` **L02_M17 `GET /care/reports/intensive-excretion`**.
- **`git diff --name-only c655743..HEAD -- src/main/resources/db/migration/`** = **V141 1파일**(`e8b8398`). `ae7e744`·`3eeac92`·`27b40cd` 구간 신규 DDL **0건**.
- **L02_M17 DB 영향**: `CareReportService.getIntensiveExcretionReport` → `IntensiveExcretionObservationService.list` → V130 `intensive_excretion_observation_records` + V132 purge/actor partial. 배뇨·배변·양쪽·중재 건수는 **인메모리 집계** — 신규 테이블·컬럼·인덱스·`@Query` 0건. L02_M04(meal-excretion)·L02_M05(bath-help)와 동일 read-only 리포트 패턴.
- **Must billing·attendance·NHIS 핵심 제약 7건** SQL 물리 재확인 — **전부 불변**. agents.yaml `core_entities` 11종 전수 충족. `ls db/migration | wc -l` = **141** contiguous.
- **결론**: **신규 V142 불필요**. ERD §4-11a·§8 L02_M17/M05 리포트 매핑·round 148 검증 헤더 + 본 #143. **보류**: L02 M05 투약 leaf·`staff_attendance`/`staff_schedules`(Should)·`billing_payments`(Epic L).

#### #142. V140 L02_M13 meal_assistance_records → V141 integrity 후속 (2026-06-16, round 147, backend `c655743`)
- **배경**: round 146(`de25b3e`/V139 carry) → **`c655743`** 전진 — `81a2223` **V140 `meal_assistance_records`**(L02_M13 통합식사도움·케어포 demo `view.total_meal`·`meal_type`/`intake_level`/`diet_restriction` enum CHECK·UK `(client, record_date, meal_type)`·복합 Tenant FK 4건·list/purge 인덱스·org/branch sync·퇴소 INSERT guard·`recorded_by` actor backstop 트리거, BNK-248~250, coder)·`9ad8346` FE `/care/meal-assistance-records`·`c655743` L02_M04/M05 report BE carry.
- **`git diff --name-only de25b3e..HEAD -- src/main/resources/db/migration/`** = **V140 1파일**. `… -- '**/*Repository.java'` = `MealAssistanceRecordRepository` 신규 + `CareReportService`가 `MealAssistanceRecordService` 주입.
- **V140 integrity 대조** (V135/V137 패턴):
  - ① **org/branch sync·퇴소 guard·actor backstop·client purge·list 인덱스 선행 포함** — coder가 V140 단일 마이그레이션에 V135 스타일 self-contained DDL 작성(별도 V141 전제 트리거 3건·purge 인덱스 1건 포함). integrity 후속 범위 축소.
  - ② **actor 감사 partial 부재** — `idx_*_org_recorded_by` 미보유 → **V141** `idx_meal_assistance_records_org_recorded_by (organization_id, recorded_by) WHERE recorded_by IS NOT NULL`(V125/V135 패턴). `MealAssistanceRecordService.create`가 `jwtScopeResolver.requireActorUserId()`로 명시 적재 + V140 `trg_*_set_recorded_by` backstop과 짝.
- **Repository ↔ 인덱스 backing 1:1 검증** (신규 조회 인덱스 0건):
  - `findByOrganizationIdAndBranchIdAndRecordDateBetweenOrderByRecordDateDescMealTypeAscCreatedAtDescClientIdAsc` → V140 `idx_*_org_branch_date` prefix-exact·정렬 1:1.
  - `findByOrganizationIdAndBranchIdAndClientIdAndRecordDateBetweenOrderBy…` → 동일 인덱스 + UK `(client, record_date, meal_type)` cohort.
  - `findByIdAndOrganizationId` → PK + V140 UK `(org, id)`.
  - `CareReportService.getMealExcretionReport` — `MealAssistanceRecordService.list` 인메모리 집계, 신규 DDL 0건.
- **Must billing·attendance·NHIS 핵심 제약 7건** SQL 물리 재확인 — **전부 불변**. agents.yaml `core_entities` 11종 전수 충족 — `meal_assistance_records`는 `meal_records`(V49) L02 상세 보완·별도 테이블. `ls db/migration | wc -l` = **141** contiguous(V1–V141, 갭·중복 0).
- **결론**: **V141 신규** + ERD §4-11b·§6·§7 V140–V141·§8 L02_M13/L02_M04 + DATA_RETENTION §2/§3/§4-1 + PLAN_NOTES #142. **보류**: L02 잔여 leaf(M05 투약)·`staff_attendance`/`staff_schedules`(Should)·`billing_payments`(Epic L). coder: V141 develop 커밋·push 후 `mvn flyway:migrate`·`mvn test` 재검증(BE 246/246 PASS 유지 예상).

#### #141. V133 G-7-1-4CHANNEL · V134 L02_M01 · V136 L02_M03 · V138 G30 satisfied → V139 integrity 후속 (2026-06-16, round 146, backend `de25b3e`)
- **배경**: round 145(`18ff83e`/신규 DDL 0건) → **`de25b3e`** 6+커밋 전진 — `3a2e82e` **V133 `billing_statement_dispatches_g7_1_4channel`**(G-7-1-4CHANNEL 본인부담금 명세 4채널 일괄발송·POSTAL/SMS/EMAIL/IN_PERSON·케어포 PDF p.87, BNK-241/245, coder)·`13b8a37` **V134 `care_service_weekly_records`**(L02_M01 주간 요양급여 제공기록 7-note + `chk_*_week_start_monday` + 최소 1종 본문 CHECK + UK `(org, client, week_start_date)`, BNK-244, coder)·`e703252` **V136 `bathing_schedules`**(L02_M03 목욕일정·`bath_type` 4종·`status` 4종 + `chk_*_completed_requires_notes` + `chk_*_completed_requires_completed_at` + UK `(org, client, scheduled_date)`, BNK-245, coder)·`47a4e25` **fix(v2/L02_M03) require reasons for skipped bathing schedules**(앱 가드 `BathingScheduleService.validateStatusPayload` CANCELLED/SKIPPED → `notes` 비공백 필수, coder)·`344a28b` **V138 `monitoring_phone_consultation_satisfaction_g30`**(FAQ21841 "유선상담 5명·60% 만족" `satisfied BOOLEAN NOT NULL DEFAULT FALSE`, coder)·`de25b3e` notification readiness payload(앱 응답만). V135(`l02_care_v134_integrity`)·V137(`l02_care_v136_integrity`)는 coder가 V125 nursing 패턴으로 자체 작성한 후속 integrity 커밋.
- **`git diff --name-only 18ff83e..HEAD -- src/main/resources/db/migration/`** = **V133·V134·V135·V136·V137·V138 6파일**. `… -- '**/*Repository.java'` = `BillingStatementDispatchRepository`·`CareServiceWeeklyRecordRepository`·`BathingScheduleRepository` 신규 + `MonitoringPhoneConsultationRepository` `satisfied` 응답 노출.
- **V133 누락 식별 3건 → V139 해소** (V52 `billing_claims.payment_recorded_by` actor backstop / V125 nursing client purge / V32 actor partial 패턴):
  - ① **`dispatched_by` actor backstop 부재** — `BillingStatementDispatchService.batchDispatch`가 `entity.setDispatchedBy(actorUserId)`로 명시 적재하나 V52/V32 `ogada_read_actor_user_id()` 세션 backstop 미적용 → raw SQL INSERT 미커버 → **V139** `trg_billing_statement_dispatches_set_dispatched_by`(BEFORE INSERT only — UPDATE는 V133 PATCH 시 actor 보존).
  - ② **org/branch sync 트리거·활성 client 가드 의도적 보류** — org/branch는 부모 `billing_claims`에서 복사하므로 client 기반 sync 부적합. 확정 청구의 본인부담금 명세는 **퇴소 후에도 발송 의무**(미납 회수)가 있어 `trg_*_guard_active_client` 미적용(rules.md §11 변경 범위 제어). V133 Tenant 복합 FK 5건이 cross-tenant drift 1차 방어.
  - ③ **client purge index 부재** — 기존 `idx_billing_statement_dispatches_claim_client (org, claim_id, client_id, dispatched_at DESC)`는 `client_id`가 비-선두라 DATA_RETENTION §3 cohort purge(`WHERE client_id IN (…)`) 미지원 → **V139** `idx_billing_statement_dispatches_client_purge (client_id)`.
  - ④ **actor 감사 partial 부재** — 발송자별 감사 조회용 부분 인덱스 미보유 → **V139** `idx_billing_statement_dispatches_org_dispatched_by (organization_id, dispatched_by) WHERE dispatched_by IS NOT NULL`(V32 패턴).
- **V136 누락 식별 1건 → V139 해소** (V112 functional_recovery / V113 program_participations / V130 본문 비공백 패턴):
  - ⑤ **CANCELLED/SKIPPED `notes` 미강제** — `47a4e25` 앱 가드(`validateStatusPayload`: CANCELLED·SKIPPED → `notes` 비공백)가 DB CHECK 미반영. raw SQL UPDATE에서 사유 누락 가능 → **V139** `chk_bathing_schedules_cancelled_skipped_requires_notes` CHECK. `notes` 컬럼 자체는 NULLable 유지, SCHEDULED·COMPLETED 상태는 기존 행위 그대로(`chk_bathing_schedules_completed_requires_notes` V136 불변).
- **V134/V135 · V136/V137 integrity 정합 확인**: V135 `trg_care_service_weekly_records_set_org_branch`·`trg_*_guard_active_client`(INSERT only)·`trg_*_set_recorded_by` 3 트리거 + `idx_*_client_purge`·partial `idx_*_org_recorded_by`(V125 패턴 1:1). V137 동일 패턴 `bathing_schedules` 3 트리거 + 2 인덱스. **V138** `satisfied BOOLEAN NOT NULL DEFAULT FALSE` 단일 컬럼 추가 — V100 UK `(org, branch, year, month, client)`·V101 actor backstop·client purge / org_created_by partial 인덱스가 컬럼 단위로 그대로 적용, integrity 후속 불요.
- **Repository ↔ 인덱스 backing 1:1 검증** (신규 조회 인덱스 0건):
  - `BillingStatementDispatchRepository.findByOrganizationIdAndClaimIdOrderByDispatchedAtDescCreatedAtDesc` → V133 `idx_*_claim_client (org, claim_id, client_id, dispatched_at DESC)` prefix-exact·정렬 1:1.
  - `BillingStatementDispatchRepository.findByIdAndOrganizationIdAndClaimId` → PK + V133 UK `(org, id)` + FK backing.
  - `CareServiceWeeklyRecordRepository.findByOrganizationIdAndBranchIdAndWeekStartDateBetween…`·`findByOrganizationIdAndClientIdAndWeekStartDate`·`findByIdAndOrganizationId` → V134 `idx_*_org_branch_week_start` + UK `(org, client, week_start)` + PK 1:1.
  - `BathingScheduleRepository.findByOrganizationIdAndBranchIdAndScheduledDateBetween…`·`findByOrganizationIdAndClientIdAndScheduledDate`·`findByIdAndOrganizationId` → V136 `idx_*_org_branch_scheduled_date` + UK `(org, client, scheduled_date)` + PK 1:1.
  - `MonitoringPhoneConsultationRepository` 기존 쿼리 3건 → V100 UK·list 인덱스 1:1(satisfied 컬럼은 read-only 응답에 포함, 인덱스 영향 없음).
- **Must billing·attendance·NHIS 핵심 제약 7건** SQL 물리 재확인 — **전부 불변**(`uq_claim_branch_month` V1·`uq_billing_claim_items_claim_client` V26·`chk_billing_claims_amount_sum` V6·`trg_billing_claims_total_reconciliation` V11·`chk_attendance_presence_xor_absence` V11/V14·`uq_nhis_import_rows_org_id` V37·`chk_nhis_import_rows_match_requires_client` V19→V54). agents.yaml `core_entities` 11종 전수 충족 — `billing_statement_dispatches`는 `billing` 확장 (청구 발송 채널 이력 별도 테이블·G-7-1-4CHANNEL 4채널 발송 audit). `ls db/migration | wc -l` = **139** contiguous(V1–V139, 갭·중복 0).
- **테스트 호환성**: V139 = `CREATE FUNCTION` + `CREATE TRIGGER` + 2 `CREATE INDEX` + 1 `ALTER TABLE … ADD CONSTRAINT`. 기존 V133/V136 컬럼·UK·PK 불변 → `BillingStatementDispatchServiceTest`·`BathingScheduleServiceTest`·repository pilot 테스트 변경 0건. Flyway migrate 시 V139 ADD CONSTRAINT는 기존 행(round 145~146 신규 도입 — V136 행 0~소량)에 평가되므로 안전; 기존 CANCELLED/SKIPPED 행이 빈 `notes`로 존재할 가능성 있으면 coder가 데이터 backfill 후 migrate(권장).
- **결론**: **V139 신규** + ERD §7 V133–V139 6행·§7 검증 헤더(round 146)·§4-1 DDL 포인터 V139·§6 인덱스(billing_statement_dispatches·care_service_weekly_records·bathing_schedules)·§8 매핑(G-7-1-4CHANNEL/L02_M01/L02_M03) + DATA_RETENTION §2/§3/§4-1/§8 행 + PLAN_NOTES #141. **보류**: L02 잔여 leaf(M04 식사·M05 투약 — BNK-247 P1)·`staff_attendance`/`staff_schedules`(Should)·`billing_payments`(Epic L 부분입금)·G30 FE Panel `satisfiedCount` 표시(coder P1). coder: V139 develop 커밋·push 후 `mvn flyway:migrate`·`mvn test` 재검증(BE 246/246 PASS 유지 예상).

#### #140. live-e2e harness deepen · V132 carry — 신규 DDL 0건 (2026-06-15, round 145, backend `18ff83e`)
- **배경**: round 144(`df14e15`/V130–V131·V132 DBA 산출) → **`18ff83e`** 5커밋 전진 — `d862a82` V132 integrity(coder develop 커밋)·`ec5f11c`/`8b7e476` live-e2e DB probe sanitized detail·`1f77324` live-e2e bootstrap seeding(`LiveE2eBootstrapService`·`LiveE2eController`)·`18ff83e` status fallback for seeded user lookup. `git diff --name-only df14e15..18ff83e -- src/main/resources/db/migration/` = **V132 1파일 carry**(`d862a82`)·`18ff83e` 단독 신규 migration **0건**. `… -- '**/*Repository.java'` = **0파일**·`'**/*.java'`에서 `@Entity`/`CREATE TABLE`/`ALTER TABLE` 매치 **0건**.
- **대조 결과** (신규 테이블·컬럼·조회 쿼리 0건):
  - ① **live-e2e bootstrap** — `ogada.live-e2e.bootstrap-enabled=true` 시 고정 UUID로 `organizations`·`branches`·`users`·`user_branches` upsert + `AuthService.login` 토큰 반환. prod 기본 off(`@ConditionalOnProperty`). 기존 V1/V4/V29 인덱스 backing, 신규 DDL 불요.
  - ② **live-e2e readiness** — `LiveReadinessProbe`·`HealthController` DB 연결 검사만. 스키마 무관.
  - ③ **V132 carry** — round 144 DBA 산출(`trg_*_set_org_branch`·`trg_*_guard_active_client`·`trg_*_set_recorded_by`·purge partial 4건)이 `d862a82`에서 develop 커밋 완료. 본 라운드 추가 integrity 후속 **0건**.
- **Must billing·attendance·NHIS 핵심 제약 7건** SQL 물리 재확인 — **전부 불변**. agents.yaml `core_entities` 11종 전수 충족. `ls db/migration | wc -l` = **132** contiguous(V1–V132).
- **결론**: **신규 V133 불필요** — live-e2e는 기존 Tenant 스키마 위 시드·헬스 검사. 본 라운드 산출은 ERD §7 검증 헤더(round 145) + PLAN_NOTES #140. **보류**: L02 잔여 leaf·`staff_attendance`/`staff_schedules`(Should)·`billing_payments`(Epic L). coder: `mvn flyway:migrate`·`mvn test` 재검증.

#### #139. V130 L02_M02 · V131 L02_M07 → V132 integrity 후속 (2026-06-15, round 144, backend `df14e15`)
- **배경**: round 143(`73df04d`/신규 DDL 0건) → **`df14e15`** 전진 — coder **V130** `intensive_excretion_observation_records`(L02_M02 집중배설관찰·BNK-238)·**V131** `body_restraint_records`(L02_M07 신체제재·BNK-239)·FE `/care/intensive-excretion`·`/care/body-restraint`. V132는 DBA 이번 라운드 산출.
- **V130–V131 integrity 대조** (V125 nursing 패턴):
  - ① **org/branch sync 트리거 부재** — `IntensiveExcretionObservationService`/`BodyRestraintRecordService`가 JWT scope·client에서 org/branch 적재하나 raw SQL branch drift 가능 → **V132** `trg_*_set_org_branch` 2건
  - ② **퇴소 INSERT 가드 부재** — 앱 `findByIdAndOrganizationIdAndActiveTrue`로 활성 강제하나 DB 방어 부재 → **V132** `trg_*_guard_active_client` 2건(INSERT only — UPDATE는 기존 행 수정 허용)
  - ③ **`recorded_by` actor backstop 부재** — `DbSessionContext.setActorUserId` + 앱 명시 적재 있으나 V32 패턴 미적용 → **V132** `trg_*_set_recorded_by` 2건
  - ④ **purge/FK backing 부재** — list index는 있으나 `client_id IN (…)` cohort purge·`recorded_by` audit 조회 미지원 → **V132** `idx_*_client_purge`·partial `idx_*_org_recorded_by` 2쌍
- **선행 보유 확인** — V130·V131 모두 복합 Tenant FK 4건·UK `(org, id)` 앵커·도메인 CHECK·list 인덱스 **선행 보유** → integrity 후속만 필요.
- **Repository 쿼리** — 각 3메서드(list branch·list branch+client·findByIdAndOrganizationId) — V130/V131 list/UK 인덱스 1:1 backing, **신규 조회 인덱스 0건**.
- **Must billing·attendance·NHIS 핵심 제약 7건** SQL 물리 재확인 — **전부 불변**. agents.yaml `core_entities` 11종 전수 충족(L02는 `health_records` 보완). `ls db/migration | wc -l` = **132** contiguous(V1–V132).
- **결론**: **V132 신규** + ERD §4-11a·§6·§7·§8·DATA_RETENTION·PLAN_NOTES #139. **보류**: L02 잔여 leaf FE wire·`staff_attendance`/`staff_schedules`(Should). coder: V132 develop 커밋·push 후 `mvn flyway:migrate`·`mvn test` 재검증.

#### #138. G19 통합재가 제공기관 탐색 · G30/G39 모니터링 evidence window — 신규 DDL 0건 (2026-06-15, round 143, backend `73df04d`)
- **배경**: round 142(`1e21b20`/V129 carry) → **`73df04d`** 4커밋 전진 — `f44ee73` **G19 integrated-home provider discovery endpoint**(`GET /branches/integrated-home/provider-discovery`·`IntegratedHomeProviderDiscoveryResponse`·`BranchService`, API_SPEC §3-1)·`41d8de5` G19 live API 라우팅 하네스·`8cb8789` **G19 provider discovery filter value 중앙화**(BNK-235)·`73df04d` **G30/G39 monitoring evidence window + care-provision dispatch pilot E2E**(`MonitoringEvidenceWindow`·`MonitoringIntegratedChecklist`·`MonitoringService` 도메인 값객체). `git diff --name-only 1e21b20..HEAD -- src/main/resources/db/migration/` = **0파일**·`… -- '**/*Repository.java'` = **0파일**·`'**/*.java'`에서 `@Entity`/`@Table`/`@Column`/`CREATE/ALTER TABLE` 매치 **0건**.
- **대조 결과** (신규 테이블·컬럼·조회 쿼리 0건):
  - ① **G19 provider discovery** — `BranchController`·`BranchService.getIntegratedHomeProviderDiscovery`·`IntegratedHomeProviderDiscoveryResponse`는 롱텀케어 포털 검색 URL·필터 파라미터(`ltcAdminKindChoiceYn8=Y`·`searchAdminKindCd=06|07`·월10만원 가산 안내)를 반환하는 **정적 설정 DTO**. JWT 스코프 검증 외 DB 미사용 — branch 읽기만(기존 V4 `branches` 인덱스 backing). `8cb8789`는 filter value 상수 중앙화(BNK-235)로 응답 콘텐츠 불변.
  - ② **G30/G39 monitoring evidence window** — `MonitoringEvidenceWindow`·`MonitoringIntegratedChecklist`·`MonitoringService`·`MonitoringIntegratedChecklistResponse`가 자가진단·유선상담·급여제공결과평가 evidence 윈도우(rolling 기간·dispatch 정합)를 기존 `monitoring_self_diagnoses`/`monitoring_phone_consultations`(V100/V101)·`provision_result_evaluations`(V80/V81)·`program_participations` 조회 결과 위에서 **인메모리 계산**. 신규 `@Query`·집계 SQL·Repository 0건 → 기존 list 인덱스 그대로 backing.
  - ③ **pilot E2E**(`CareProvisionRecordDispatchPilotServiceFlowE2eTest`·`IntegratedHomeProviderDiscoveryLiveApiRoutingE2eTest`·`PilotChecklistJwtE2eTest`) — 검증층, DB 미신규.
- **Must billing·attendance·NHIS 핵심 제약 7건** SQL 물리 재확인 — **전부 불변**(`uq_claim_branch_month` V1·`uq_billing_claim_items_claim_client` V26·`chk_billing_claims_amount_sum` V6·`trg_billing_claims_total_reconciliation` V11·`chk_attendance_presence_xor_absence` V11/V14·`uq_nhis_import_rows_org_id` V37·`chk_nhis_import_rows_match_requires_client` V19→V54). agents.yaml `core_entities` 11종 전수 충족. `ls db/migration | wc -l` = **129** contiguous(V1–V129).
- **결론**: **신규 V130 불필요** — G19는 정적 설정 응답·G30/G39는 기존 인덱스 위 읽기 전용 인메모리 집계. 본 라운드 산출은 ERD §7 검증 헤더(round 143) + PLAN_NOTES #138. **보류**: `staff_attendance`/`staff_schedules`(Should)·G41 FAQ21808 FE Panel 28종 enum dropdown(BNK-221 P2). coder: `mvn flyway:migrate`·`mvn test` 재검증 권장.

#### #137. V129 G41 FAQ21808 23종 staff_training_logs enum 확장 — integrity 후속 0건 (2026-06-15, round 142, backend `1e21b20`)
- **배경**: round 141(`f4c8beb`/V128 G24b carry) → **`1e21b20`** 6커밋 전진 — coder **V129** `staff_training_logs_g41_faq21808_guidelines`(FAQ21808 운영규정 11항목 + 급여제공지침 12종 합계 23종 enum 확장, BNK-221 P2·decisions BNK-228, `b1c92e1`)·`345c0cb` Locale.ROOT 정규화·`3dd94e6`/`0cd8ea8` G2 EASY_PAY/KakaoPay alias 정규화·`4fe655b`/`1e21b20` visit/easy-pay live API routing E2E 테스트.
- **V129 integrity 대조** (V99 G9-COG `chk_clients_ltc_grade` 0–5 확장 / V75 `case_management_plan` nonempty / V103 transport seed 보정 — CHECK·seed 자체완결 패턴):
  - ① **DDL은 ALTER CHECK 2건만** — `chk_staff_training_logs_type` DROP/ADD(5→28 enum: ELDERLY_HUMAN_RIGHTS·OPERATING_REGULATION·DISASTER_RESPONSE·FIRE_SAFETY_EQUIPMENT·STAFF_RIGHTS + OP_REG_* 11 + GUIDELINE_* 12) + `chk_staff_training_logs_g41b_annual_no_half` DROP/ADD 의미 확장(`ELDERLY_HUMAN_RIGHTS OR reference_half IS NULL` — V107 4종 → V129 27종으로 확장, **이름은 보존**). 신규 컬럼·FK·트리거·인덱스 0건.
  - ② **선행 보유 정합** — V104 UK `(org, id)` Tenant 앵커·V104 복합 FK 4건(branch/new_hire_user/created_by/`(org,new_hire_user,branch)→user_branches`)·V105 `trg_*_set_org`/`trg_*_set_created_by`/`chk_*_trained_at_year`·V104 `chk_*_updated_after_created`/V37 temporal 패턴 모두 행 단위 신규 enum에도 그대로 적용.
  - ③ **Java 도메인 ↔ DB CHECK 정합** — `StaffTrainingLogType.ALL_ALLOWED`(28종) ↔ V129 enum 1:1, `SIMPLE_ANNUAL_TRAINING_TYPES`(26종) ↔ 앱 `resolveReferenceHalf` NULL 강제. DB는 V104 `chk_*_operating_no_half` + V129 `chk_*_g41b_annual_no_half`로 `OPERATING_REGULATION`·`ELDERLY_HUMAN_RIGHTS` 외 모든 26종 NULL 강제(`OPERATING_REGULATION`만 V104, ELDERLY_HUMAN_RIGHTS 제외 27종은 V129 — 두 CHECK가 함께 동작해 모두 NULL).
  - ④ **Repository 7쿼리 ↔ V104 `idx_staff_training_logs_org_branch_year_type` 1:1 backing** — 모두 `(organization_id, branch_id, training_type, reference_year)` prefix 등치 사용. 28 distinct enum 값 → selectivity 약 5.6배 향상. **신규 인덱스 0건**.
  - ⑤ **G41 compliance 앱 변경**(`StaffTrainingLogService.getCompliance` BNK-221) — `FAQ21808_TOPICS_REQUIRED`(=`FAQ21808_TOPICS.size()` = 23) 연 1회 + 기존 ELDERLY_HUMAN_RIGHTS 반기 1회·OPERATING_REGULATION 연 1회·G41b 3종 연 1회 + 신규직원 7일 오리엔테이션 합계 compliance — 전부 V104 인덱스 위 인메모리 집계, DB 변경 불요.
  - ⑥ **테스트 호환성** — V129 ALTER만(V104 컬럼/PK 불변) → 기존 `StaffTrainingLogServiceTest`/`ControllerTest`/`Catalog` 변경 0건.
- **Must billing·attendance·NHIS 핵심 제약 7건** SQL 물리 재확인 — **전부 불변**. agents.yaml `core_entities` 11종 전수 충족. `ls db/migration | wc -l` = **129** contiguous(V1–V129).
- **결론**: **V129 자체 완결 — 신규 V130 integrity 후속 불필요**. 본 라운드 산출은 ERD §4-18-1 28종 enum 갱신·§7-71 V129 행·§7 검증 헤더(round 142)·DATA_RETENTION §2/§3/§8 staff_training_logs 행 + PLAN_NOTES #137. **보류**: G41 FAQ21808 FE Panel 28종 enum dropdown(BNK-221 P2)·`staff_attendance`/`staff_schedules`(Should). coder: `mvn flyway:migrate`·`mvn test` 재검증 권장.

#### #136. V128 G24b 욕구사정 8영역 확장 — integrity 후속 0건 (2026-06-15, round 141, backend `f4c8beb`)
- **배경**: round 141(`735dd53`/V126·V127 carry) → **`f4c8beb`** 전진 — coder **V128** `client_needs_assessments` 5 TEXT 컬럼(`disease`·`communication`·`nutrition`·`living_environment`·`resource_utilization`, G24b BNK-226·`45fb6d9`)·FE 8영역 폼 @ `49fbf67`. V127 DBA integrity는 `4c1fd43`에서 선행 커밋.
- **V128 integrity 대조** (V99 CHECK 확장 패턴):
  - ① **nullable TEXT 5건** — V84 `physical`/`cognitive`/`family`/`economic`/`social`/`service_needs`와 동일(자유텍스트·NULL 허용·인덱스 불요)
  - ② **FK·UK·트리거·purge 인덱스 변경 없음** — V85 `trg_*_set_org_branch`·`trg_*_guard_active_client`·`trg_*_set_recorded_by`·`idx_*_client_purge`·`idx_*_org_recorded_by`가 행 단위로 신규 컬럼 포함 UPDATE에도 적용
  - ③ **8영역 completeness CHECK 보류** — 앱 `ClientNeedsAssessmentService`·FE validation(V84 6영역과 동일 정책)
- **Repository 쿼리** — `ClientNeedsAssessmentRepository` 4메서드 전부 V84 UK·`idx_client_needs_assessments_org_client_year` backed, **신규 조회 인덱스 0건**.
- **Must billing·attendance·NHIS 핵심 제약 7건** SQL 물리 재확인 — **전부 불변**. agents.yaml `core_entities` 11종 전수 충족. `ls db/migration | wc -l` = **128** contiguous(V1–V128).
- **결론**: **신규 V129 불필요** — ERD §7-54·§7-70·§8·DATA_RETENTION §2 G24b 확인 + PLAN_NOTES #136. **보류**: `staff_attendance`/`staff_schedules`(Should). coder: `mvn flyway:migrate`·`mvn test` 재검증 권장.

#### #135. V126 G-ONBOARD-SUPPORT · V127 integrity 후속 (2026-06-15, round 141, backend `735dd53`)
- **배경**: round 140(`6b0238a`) → **`735dd53`** — coder **V126** `branch_onboarding_support`(지점 1행 UK·`opened_on`·`session_state` JSONB 1~4회차, BNK-186/212). DBA **V127** integrity(`4c1fd43`): UK `(org, id)` Tenant 앵커·복합 FK `(org, branch_id)→branches`·`(org, updated_by)→users`·`opened_on` 도메인 CHECK·`updated_by` actor backstop·`(org, updated_by)` partial 인덱스.
- **Repository** — `BranchOnboardingSupportRepository.findByOrganizationIdAndBranchId` — V126 UK `branch_id` 1:1 backing, 신규 조회 인덱스 0건.
- **Must billing·attendance·NHIS** — 불변. `ls db/migration | wc -l` = **127** at V127 commit.
- **결론**: V127 DBA 산출 완료 — ERD §7-69·§8 onboarding-support 3행·DATA_RETENTION §2·§3.

#### #134. L03_M07/M09/M10/M15 읽기 전용 리포트 — 신규 DDL 0건 (2026-06-15, round 140, backend `6b0238a`)
- **배경**: round 139(`9bd1660`/V125 DBA 산출) → **`6b0238a`** 4커밋 전진 — `c23b1a3` **L03_M07/M09/M10 nursing service report API**(통합 간호제공·병의원 진료내역·투약제공 리포트, BNK-218)·`75bddee` **L03_M15 pressure ulcer provision report API**(욕창 케어 제공 리포트, BNK-218)·`4ab06cd` report live API routing 하네스 + provisions alias·`6b0238a` nursing date window 보정(historical query). `git diff --name-only ee8b2a4..HEAD -- src/main/resources/db/migration/` = **0파일**. `… -- '**/*Repository.java'` = **0파일**.
- **대조 결과** (신규 테이블·컬럼·조회 쿼리 0건):
  - ① **L03_M07/M09/M10** — `NursingServiceRecordService.getTotalReport`(전체·간호/투약/진료 count)·`getHospitalVisitReport`(`medicalVisit` 필터)·`getMedicationDeliveryReport`(`medicationProvided` 필터) 모두 기존 `list(fromDate, toDate, clientId).items()`를 **인메모리** 집계·필터. 새 `@Query`·집계 SQL 0건 → V123 `idx_nursing_service_records_org_branch_service_date` + UK list 인덱스 그대로 backing.
  - ② **L03_M15** — `PressureUlcerService.getProvisionReport`가 기존 `listCareRecords(...)` 결과 인메모리 래핑 → V114 `idx_pressure_ulcer_care_records_*` list 인덱스 재사용.
  - ③ **date-window 보정(`6b0238a`)** — `NursingServiceRecordService`/`NursingWeightRecordService.resolveDateWindow`가 `to` 먼저 해석 후 `from = to.minusDays(90)`로 default 순서만 변경(historical `toDate` 기준 90일 창 정렬). 범위 술어 `service_date/measure_date BETWEEN from AND to`는 동일 → 인덱스 영향 0건.
- **Must billing·attendance·NHIS 핵심 제약 7건** SQL 물리 재확인 — **전부 불변**(`uq_claim_branch_month` V1·`uq_billing_claim_items_claim_client` V26·`chk_billing_claims_amount_sum` V6·`trg_billing_claims_total_reconciliation` V11·`chk_attendance_presence_xor_absence` V11/V14·`uq_nhis_import_rows_org_id` V37·`chk_nhis_import_rows_match_requires_client` V19→V54). agents.yaml `core_entities` 11종 전수 충족(nursing은 `health_records` 보완). `ls db/migration | wc -l` = **125** contiguous(V1–V125, 갭·중복 0).
- **API 경로 실측** — `NursingServiceRecordController` base `/api/v1/nursing/service-records` + `/reports/total`·`/reports/hospital-visits`·`/reports/medication-delivery`; `PressureUlcerController` base `/api/v1/nursing/pressure-ulcer` + `/reports/provision`(alias `/reports/provisions`, `4ab06cd`). FE route(`/nursing/service/reports…`)와 BE API 경로는 별개 — ERD는 BE 실경로 기준.
- **결론**: **신규 V126 불필요** — 리포트 4종은 기존 인덱스 위 읽기 전용 인메모리 집계. ERD §4-24-2(리포트 엔드포인트 행)·§8(API 매핑 2행)·§7 검증 헤더(round 140) + PLAN_NOTES #134 갱신. **보류**: L03 잔여 leaf FE wire·`staff_attendance`/`staff_schedules`(Should). **참고**: backend WT에 `EasyPayService.java`/`EasyPayServiceTest.java` 미커밋 변경 존재 — coder 영역(DBA 비간섭). coder: `mvn flyway:migrate`·`mvn test` 재검증 권장.

#### #133. V123 G-NURSING 제공기록 · V124 배설/경관 → V125 integrity 후속 (2026-06-15, round 139, backend `9bd1660`)
- **배경**: round 138(`090b2d7`/V121·V122) → **`9bd1660`** 전진 — coder **V123** `nursing_service_records`(L03_M01 간호급여 제공기록·3-flag `nursing_provided`/`medication_provided`/`medical_visit`·BNK-214/215, baseline `9bd1660`)·**V124** `nursing_excretion_tube_records`(L03_M06 배설/경관영양(NG)/유치도뇨·BNK-216). V123은 committed baseline, V124는 직전 추가. V125는 DBA 이번 라운드 산출.
- **V123–V124 integrity 대조** (V117/V121 nursing 패턴):
  - ① **org/branch sync 트리거 부재** — `NursingServiceRecordService`/`NursingExcretionTubeRecordService`가 JWT scope·client에서 org/branch 적재하나 raw SQL branch drift 가능 → **V125** `trg_*_set_org_branch` 2건
  - ② **퇴소 INSERT 가드 부재** — 앱이 활성 강제하나 DB 방어 부재 → **V125** `trg_*_guard_active_client` 2건(INSERT only — UPDATE는 기존 행 수정 허용)
  - ③ **`recorded_by` actor backstop 부재** — `DbSessionContext.setActorUserId` + 앱 명시 적재 있으나 V32 `ogada_read_actor_user_id()` 패턴 미적용 → **V125** `trg_*_set_recorded_by` 2건
  - ④ **purge/FK backing 부재** — list index는 있으나 `client_id IN (…)` cohort purge·`recorded_by` audit 조회 미지원 → **V125** `idx_*_client_purge`·partial `idx_*_org_recorded_by` 2쌍
- **선행 보유 확인** — V123·V124 모두 복합 Tenant FK 4건(`branch_org`·`client_org`·`client_branch_org`·`recorded_by_org`)·UK `(org, id)` 앵커·도메인 CHECK(V123 최소 1종 선택·V124 tube_type 3종·교체일 정합)·list 인덱스 **선행 보유** → integrity 후속만 필요.
- **Repository 쿼리** — V123/V124 list/UK 인덱스 1:1 backing, **신규 조회 인덱스 0건**.
- **Must billing·attendance·NHIS 핵심 제약 7건** SQL 물리 재확인 — **전부 불변**. agents.yaml `core_entities` 11종 전수 충족(nursing은 `health_records` 보완). `ls db/migration | wc -l` = **125** contiguous(V1–V125).
- **결론**: **V125 신규** + ERD §4-24-2·§6·§7-68·§8·DATA_RETENTION §2·§3·PLAN_NOTES #133. **보류**: L03_M01 FE wire·`staff_attendance`/`staff_schedules`(Should). coder: V125 develop 커밋·push 후 `mvn flyway:migrate`·`mvn test` 재검증.

#### #132. V118–V119 G-NURSING oral/emergency · V120 v1.3-B → V121/V122 integrity 후속 (2026-06-15, round 138, backend `090b2d7`)
- **배경**: round 137(`1a822d2`/V117) → **`090b2d7`** 전진 — coder **V118** `nursing_oral_care_checks`(L03_M13, BNK-211, `3540b4f`)·**V119** `nursing_emergency_records`(L03_M04, BNK-212, `81bca68`)·**V120** `transport_v1_3_b`(결정 75, WIP untracked @ WT `090b2d7`). `git diff --name-only 1a822d2..HEAD -- src/main/resources/db/migration/` = **V118·V119 2파일**(committed). V120·V121·V122는 DBA 이번 라운드 산출.
- **V118–V119 integrity 대조** (V117 nursing 패턴):
  - ① **org/branch sync 트리거 부재** — `NursingOralCareCheckService`/`NursingEmergencyRecordService`가 JWT scope·client에서 org/branch 적재하나 raw SQL branch drift 가능 → **V121** `trg_*_set_org_branch` 2건
  - ② **퇴소 INSERT 가드 부재** — `requireClientInScope(..., write=true)`가 활성 강제하나 DB 방어 부재 → **V121** `trg_*_guard_active_client` 2건
  - ③ **`recorded_by` actor backstop 부재** — `DbSessionContext.setActorUserId` + 앱 명시 적재 있으나 V32 패턴 미적용 → **V121** `trg_*_set_recorded_by` 2건
  - ④ **purge/FK backing 부재** — list index는 있으나 `client_id IN (…)` cohort purge 미지원 → **V121** `idx_*_client_purge`·partial `idx_*_org_recorded_by` 2쌍
- **V120 integrity 대조** (V47/V70 transport 패턴):
  - ① **legacy UK 부재** — V120이 `uq_transport_runs_org_branch_date_direction` 해제 후 차량별 partial UK만 추가 → `vehicle_id IS NULL` v1.3-A 단일 운행 중복 가능 → **V122** partial UK
  - ② **suggest events Tenant 앵커·actor 부재** — `TransportSuggestService`가 `created_by` 명시 적재하나 Tenant 앵커·backstop 없음 → **V122** `uq_transport_suggest_events_org_id`·`trg_*_set_created_by`
  - ③ **settings updated_by backstop 부재** — `BranchTransportSettingsService`가 명시 적재하나 V52 패턴 미적용 → **V122** `trg_branch_transport_settings_set_updated_by`
- **Repository 7쿼리** — oral 4·emergency 3·suggest count 1 — V118–V120 list/UK/count 인덱스 1:1 backing, **신규 조회 인덱스 0건**.
- **Must billing·attendance·NHIS 핵심 제약 7건** SQL 물리 재확인 — **전부 불변**. agents.yaml `core_entities` 11종 전수 충족. `ls db/migration | wc -l` = **122** contiguous(V1–V122).
- **결론**: **V121·V122 신규** + ERD §4-24-1·§4-25·§6·§7·§8·DATA_RETENTION·PLAN_NOTES #132. **보류**: V120 coder 커밋·v1.3-B FE wire·`staff_attendance`/`staff_schedules`(Should). coder: V120+V121+V122 develop 커밋·push 후 `mvn flyway:migrate`·`mvn test` 재검증.

#### #131. V114–V116 G-NURSING nursing tables → V117 integrity 후속 (2026-06-14, round 137, backend `1a822d2`)
- **배경**: round 136(`3bd6a43`/V112·V113) → **`1a822d2`** 전진 — coder **V114** `pressure_ulcer_assessments`/`pressure_ulcer_care_records`(G-NURSING-PRESSURE-ULCER, BNK-203~206)·**V115** `nursing_vital_checks`(L03_M11, BNK-207)·**V116** `nursing_weight_records`(L03_M14, BNK-208). `git diff --name-only 3bd6a43..HEAD -- src/main/resources/db/migration/` = **V114·V115·V116 3파일**(coder).
- **V114–V116 integrity 대조** (V93 client_risk_assessments / V70 client_outings 신규 테이블 패턴):
  - ① **org/branch sync 트리거 부재** — `PressureUlcerService`/`NursingVitalCheckService`/`NursingWeightRecordService`가 JWT scope·client에서 org/branch 적재하나 raw SQL branch drift 가능 → **V117** `trg_*_set_org_branch` 4건
  - ② **퇴소 INSERT 가드 부재** — `requireClientInScope(..., write=true)`가 `findByIdAndOrganizationIdAndActiveTrue`로 활성 강제하나 DB 방어 부재 → **V117** `trg_*_guard_active_client` 4건(INSERT only — UPDATE는 기존 행 수정 허용)
  - ③ **`recorded_by` actor backstop 부재** — `DbSessionContext.setActorUserId` + 앱 명시 적재 있으나 V32 패턴 미적용 → **V117** `trg_*_set_recorded_by` 4건
  - ④ **purge/FK backing 부재** — list index `(org, branch, date DESC, client_id)`는 `client_id IN (…)` cohort purge 미지원 → **V117** `idx_*_client_purge`·partial `idx_*_org_recorded_by` 4쌍
  - ⑤ **`recorded_at` temporal CHECK 부재** — `pressure_ulcer_assessments`만 `recorded_at` 보유 → **V117** `chk_pressure_ulcer_assessments_recorded_at_after_created`
- **Repository 12쿼리** — assessment 5·care 4·vital 3·weight 5 — V114–V116 list/UK 인덱스 1:1 backing, **신규 조회 인덱스 0건**.
- **Must billing·attendance·NHIS 핵심 제약 7건** SQL 물리 재확인 — **전부 불변**. agents.yaml `core_entities` 11종 전수 충족(nursing는 `health_records` 보완 — v3.1 Must). `ls db/migration | wc -l` = **117** contiguous(V1–V117).
- **결론**: **V117 신규** + ERD §4-24·§6·§7·§8·DATA_RETENTION·PLAN_NOTES #131. **보류**: L03_M14 FE wire·COGNITIVE ABSENT skip_reason DB trigger(P2, PLAN_NOTES #130)·`staff_attendance`/`staff_schedules`(Should). coder: V117 develop 커밋·push 후 `mvn flyway:migrate`·`mvn test` 재검증.

#### #130. V112/V113 G17b cognitive activity · ABSENT satisfaction 앱 가드 — 신규 DDL 0건 (2026-06-14, round 136, backend `3bd6a43`)
- **배경**: round 135(`c22a5dc`/V111) → **`3bd6a43`** 전진 — `6b7e6cb` **V112 `functional_recovery_cognitive_activity_reason_g17b`**·`ba7d84f` **V113 `program_participation_skip_reason_g17b`**·`3bd6a43` ABSENT satisfaction 앱 가드(Java only). `git diff --name-only c22a5dc..HEAD -- src/main/resources/db/migration/` = **V112·V113 2파일**(coder). `git diff --name-only c22a5dc..HEAD -- '**/*Repository.java'` = **0파일**.
- **대조 결과**:
  - ① **V112** — `functional_recovery_plans`에 MOHW 2025-247 제32조 미제공 사유 CHECK **DB 완결**(`chk_functional_recovery_plans_cognitive_activity_reason`). `FunctionalRecoveryService.normalizeNotProvidedReason` 앱 이중 방어.
  - ② **V113** — `activity_programs.program_type`에 `COGNITIVE`·`program_participations.skip_reason` enum CHECK·ATTENDED/skip_reason 상호배타. **`COGNITIVE`+`ABSENT` ⇒ skip_reason 필수**는 DB 미강제 — `ProgramService.resolveSkipReason`·`CognitiveActivitySkipReason.normalize` 앱 전담(V113 `chk_program_participations_attended_skip_reason`은 ATTENDED만 제한). raw SQL 방어선 필요 시 V114 trigger(`activity_programs` JOIN) 검토 보류(P2).
  - ③ **3bd6a43** — ABSENT+만족도 입력 거부는 V49 `chk_program_participations_satisfaction_pair` + 앱 `resolveSatisfaction`, DDL 0건.
- **Must billing·attendance·NHIS 핵심 제약 7건** SQL 물리 재확인 — **전부 불변**. agents.yaml `core_entities` 11종 전수 충족. `ls db/migration | wc -l` = **113** contiguous(V1–V113).
- **결론**: **신규 V114 불필요(당 라운드)** — ERD §4-11·§7 V112/V113·§7-64·§8·DATA_RETENTION·PLAN_NOTES #130 갱신. **보류**: COGNITIVE ABSENT skip_reason DB trigger(P2)·`staff_attendance`/`staff_schedules`(Should). coder: `mvn flyway:migrate`·`mvn test` 재검증 권장.

#### #129. V111 guardian-link guard 커밋 확인 · J03 quiet-hours · G21 batch-confirm — 신규 DDL 0건 (2026-06-14, round 135, backend `c22a5dc`)
- **배경**: round 134(`b893e97`/V110) → **`c22a5dc`** 전진 — `dbecd72` **V111 easy-pay guardian link DB guard**(round 134 DBA follow-up 산출, coder develop 커밋 확인)·`16a0734`/`82054f1` easy-pay provider 정규화 강화·`8f9ad0c` easy-pay claim route alias·`328874d`/`9652bf0`/`e5b4b88`/`a057739`/`9a4ab8e` **J03 알림 quiet-hours**(수동 발송 차단·정책 공유)·`0b807d8`/`a121ae4`/`c22a5dc` **G21 방문일정 batch confirm**(NHIS 게이트·readiness draft IDs). `git diff --name-only b893e97..HEAD -- src/main/resources/db/migration/` = **V110·V111 2파일**(둘 다 DBA 산출 — V110 round 134·V111 follow-up, 이번 라운드 커밋 확인). `git diff --name-only b893e97..HEAD -- '**/*Repository.java'` = **0파일**.
- **대조 결과** (신규 테이블·컬럼·조회 쿼리 0건):
  - ① **J03 quiet-hours**(`NotificationQuietHoursPolicy`·`NotificationService`·`BillingService.rejectManualNotifyDuringQuietHours`) — `NotificationProperties` env/config read-only·KST clock, **DB 미사용**.
  - ② **easy-pay provider 정규화**(`CreateEasyPayPaymentRequest` regex `(?i)\s*(CARD|KAKAO_PAY)\s*`·`EasyPayService.normalizeProvider` `strip()`+`Locale.ROOT`) — 정규화 결과는 여전히 `CARD`/`KAKAO_PAY` → **V108 `chk_easy_pay_requests_provider`(CARD/KAKAO_PAY) 충족**, 신규 제약 불요.
  - ③ **easy-pay route alias**(`EasyPayController` `/claims/{id}` 추가) — 라우팅 호환만, DB 미사용.
  - ④ **G21 batch confirm**(`VisitService` batch confirm·`BatchConfirmVisitSchedules*`·`VisitConfirmReadinessResponse`) — 재사용 쿼리 `findByIdAndOrganizationId`·`findByOrganizationIdAndBranchIdAndVisitDateBetween…`·`…ScheduleKindAndVisitDateBetween…`·paired schedule 조회 모두 기존 V53 self-FK·V56 `idx_visit_schedules_org_*_date` backing → **신규 인덱스 0건**.
- **V111 대조** (V13 guardian_clients role guard·V45 guardian_notification_preferences 패턴): `easy_pay_requests.guardian_user_id`가 NULL 아닐 때 기존 데이터 사전 검증(DO 블록) + `trg_easy_pay_requests_validate_guardian_link`(BEFORE INSERT/UPDATE)가 동일 Tenant `users.role_code='guardian'` 및 `guardian_clients` `(organization_id, guardian_user_id, client_id)` 연결을 강제. 앱 `EasyPayService` `existsByOrganizationIdAndGuardianUserIdAndClientId` 검증의 **DB 방어선** — 직원/관리자 대납(`guardian_user_id` NULL)은 비간섭, 보호자 셀프 결제 확장 시 본인 연결 청구만 허용.
- **Must billing·attendance·NHIS 핵심 제약 7건** SQL 물리 재확인 — **전부 불변**(`uq_claim_branch_month` V1·`uq_billing_claim_items_claim_client` V26·`chk_billing_claims_amount_sum` V6·`trg_billing_claims_total_reconciliation` V11·`chk_attendance_presence_xor_absence` V11/V14·`uq_nhis_import_rows_org_id` V37·`chk_nhis_import_rows_match_requires_client` V19→V54). agents.yaml `core_entities` 11종 전수 충족(EASY_PAY는 billing 결제 수단 확장). `ls db/migration | wc -l` = **111** contiguous(V1–V111, 갭·중복 0).
- **결론**: **신규 V112 불필요** — V111행(ERD §7)·§4-23·§6·§8은 round 134에서 이미 반영, 이번 라운드는 **ERD 검증 헤더 + PLAN_NOTES #129** 갱신. **보류**: G2 7-5 KakaoPay/Card 실 PG 연동(stub `StubEasyPayProvider`)·`EASY_PAY` CMS-style 환불 정합(P2)·`staff_attendance`/`staff_schedules`(Should). coder: `mvn flyway:migrate`·`mvn test` 재검증 권장.

#### #128. V108/V109 easy_pay_requests · V110 integrity 후속 (2026-06-14, round 134, backend `b893e97`)
- **배경**: round 133(`32f87f1`/V106·V107 DBA) → **`b893e97`** 4커밋 전진 — `438f5c7` **V108 `easy_pay_requests`**(v2 G2 7-5 본인부담금 간편결제 PG skeleton·`billing_claims.payment_method`에 `EASY_PAY` 추가·케어포 view.npay_manage parity, BNK-189, coder)·`70b3fb8` **V109 `pg_order_id` nullable**(order-init 실패 시 PG order id 미발급 행 보존, coder)·`1231389` G2/7-5 pilot service-flow E2E·`b893e97` G2/7-5 전월 미납 가드(`getClaimGenerationGuard` 재사용). `git diff --name-only 32f87f1..HEAD -- src/main/resources/db/migration/` = **V108·V109 2파일**(coder).
- **V108/V109 integrity 대조** (V59 CMS / V88-V89 staff HR / V93 risk-assessment → V60/V90/V93 후속 패턴):
  - ① **단일컬럼 FK만 선언** — `organization_id`·`branch_id`·`claim_id`·`client_id`·`guardian_user_id` 5건 모두 single-column REFERENCES → 다른 Tenant의 branch/claim/client/guardian 연결 가능(cross-tenant 위험, V8/V60 규약 위반) → **V110** Tenant 앵커 `uq_easy_pay_requests_org_id` + 복합 Tenant FK 5건(`(org, branch_id)→branches`·`(org, claim_id)→billing_claims`·`(org, client_id)→clients`·`(org, branch_id, client_id)→clients`·`(org, guardian_user_id)→users`)
  - ② **org sync 트리거 부재** — `EasyPayService`가 JWT scope에서 `organizationId` 적재·claim에서 `branchId` 복사하나 raw SQL INSERT 미커버 → **V110** `trg_easy_pay_requests_set_org`(branch→org, V60 CMS·V74 case_management 패턴)
  - ③ **활성 이용자 가드 부재** — 간편결제는 **실시간 결제**(stub provider→PG redirect→confirm). 퇴소·비활성 이용자가 결제 행을 생성하면 안 됨. 앱 가드는 청구 활성 검증만이고 client lifecycle 미체크 → **V110** `trg_easy_pay_requests_guard_active_client`(V10/V93 패턴, INSERT 시만; UPDATE는 FAILED 재시도 위해 허용)
  - ④ **lifecycle CHECK 부재** — `REQUESTED`(transient·persist 없음)→`PENDING`(createOrder 성공)→`SUCCEEDED`(confirm 성공·`completed_at`·`pg_transaction_id`)/`FAILED`(`completed_at`·`failure_reason`)/`CANCELLED`(P2). V108은 `chk_easy_pay_requests_status` enum CHECK만 보유 → **V110** 5건 CHECK: lifecycle pair(REQUESTED/PENDING ↔ `completed_at IS NULL` · SUCCEEDED/FAILED/CANCELLED ↔ `completed_at IS NOT NULL`, V20 backup_runs 패턴)·FAILED→`failure_reason` 비공백·SUCCEEDED→`pg_transaction_id` 비공백·PENDING→`pg_order_id` 비공백(V109 FAILED는 NULL 허용)·`amount > 0`
  - ⑤ **temporal CHECK 부재** — V36/V37 시간 정합 패턴이 신규 테이블에 미적용 → **V110** 3건(`updated_at`/`requested_at >= created_at`·`completed_at >= requested_at`)
  - ⑥ **FK backing 부재** — V108 `uq_easy_pay_requests_org_claim`이 `(org, claim_id)`만 backing, `branch_id`/`client_id`/`guardian_user_id`는 seq scan·cohort purge 불가 → **V110** 3건 partial(`(org, branch_id)`·`(client_id)` purge·`(org, guardian_user_id)` partial)
- **`EasyPayRequestRepository`** 단일 쿼리(`findByOrganizationIdAndClaimId`) — V108 UK 1:1 backing, 신규 조회 인덱스 0건.
- **앱 lifecycle ↔ V110 CHECK 정합 확인** (`EasyPayService.requestClaimPayment`): persist 흐름은 PENDING(`completed_at=null`+`pg_order_id` set after createOrder)→SUCCEEDED(`completed_at=now`+`pg_transaction_id`+`completed_at`) 또는 FAILED(`completed_at=now`+`failure_reason`); `persistFailedPaymentRequest`가 FAILED의 `failure_reason`·`completed_at` 모두 설정 — **V110 CHECK 5건 전부 충족**, app-side regression risk 0.
- **`billing_claims.payment_method` EASY_PAY**(V108) — V50 PAID 메타·V52 actor backstop 패턴 재사용. `recordCopayPayment(claimId, EASY_PAY)` 호출이 V50 `chk_billing_claims_paid_requires_metadata`(`paid_at IS NOT NULL AND payment_method IS NOT NULL`) 충족 + V52 `trg_billing_claims_set_payment_recorded_by` backstop.
- **테스트 호환성** — `EasyPayServiceTest`·`EasyPayPilotServiceFlowE2eTest` 모두 `Mockito.mock(EasyPayRequestRepository.class)` 사용(JPA persistence layer 미실행), V110 DDL은 실제 PostgreSQL Flyway migrate에서만 평가 → **테스트 호환성 영향 0**.
- **Must billing·attendance·NHIS 핵심 제약 7건** SQL 물리 재확인 — **전부 불변**(`uq_claim_branch_month` V1·`uq_billing_claim_items_claim_client` V26·`chk_billing_claims_amount_sum` V6·`trg_billing_claims_total_reconciliation` V11·`chk_attendance_presence_xor_absence` V11/V14·`uq_nhis_import_rows_org_id` V37·`chk_nhis_import_rows_match_requires_client` V19→V54). agents.yaml `core_entities` 11종 전수 충족(EASY_PAY는 billing 결제 수단 확장). `ls db/migration | wc -l` = **110** contiguous(V1–V110).
- **결론**: **V110 신규** + ERD §4-23·§6 easy_pay 인덱스 14행·§7 V108/V109/V110 3행·§8 EASY_PAY API 4행·DATA_RETENTION §3 easy_pay_requests 행·§8 coder 메모·PLAN_NOTES #128. **보류**: G2 7-5 KakaoPay/Card 실 PG 연동(stub `StubEasyPayProvider`만)·`EASY_PAY` CMS-style 환불 정합(P2 — `easy_pay_requests` cancel/refund webhook)·`staff_attendance`/`staff_schedules`(Should). coder: V110 develop 커밋·push 후 `mvn flyway:migrate`·`mvn test` 재검증.

#### #127. V106 G41b categories · V107 annual no-half 후속 (2026-06-14, round 133, backend `32f87f1`)
- **배경**: round 132(`6191b91`/V104·DBA V105 산출) → **`32f87f1`** 5커밋 — `613b6af` **V105 integrity + V106 categories**(G41b 3종 CHECK 확장, BNK-184)·`0f11158` compliance API·`299d21f` earliest orientation·`32f87f1` branch scope guard(BNK-187). `git diff --name-only 6191b91..HEAD -- src/main/resources/db/migration/` = **V105·V106 2파일**(coder).
- **V106 integrity 대조** (V99 CHECK 확장 패턴):
  - ① actor/org/purge/FK **해당 없음** — 컬럼·FK 0건, V105 선행 완료
  - ② **연간 3종 `reference_half` CHECK 부재** — V104 `chk_staff_training_logs_operating_no_half`는 `OPERATING_REGULATION`만. G41b `DISASTER_RESPONSE`·`FIRE_SAFETY_EQUIPMENT`·`STAFF_RIGHTS`는 앱 `SIMPLE_ANNUAL_TRAINING_TYPES`/`resolveReferenceHalf`만 → **V107** `chk_staff_training_logs_g41b_annual_no_half`
- **G41b 앱 변경**(BNK-187) — `validateCreateFields` branch scope·earliest orientation date: **V105** `(org,new_hire_user_id,branch_id)→user_branches` FK + 앱 이중 방어, 신규 DDL 0건
- **Repository 8쿼리** — V104 인덱스 1:1 backing, 신규 조회 인덱스 0건
- **Must billing·attendance·NHIS 핵심 제약 7건** SQL 물리 재확인 — **전부 불변**. agents.yaml `core_entities` 11종 전수 충족. `ls db/migration | wc -l` = **107** contiguous(V1–V107).
- **결론**: **V107 신규** + ERD §4-18-1·§7·§8·DATA_RETENTION·PLAN_NOTES #127. **보류**: `staff_attendance`/`staff_schedules`(Should). coder: V107 develop 커밋·push 후 `mvn flyway:migrate`·`mvn test` 재검증.

#### #126. V104 staff training logs · V105 integrity 후속 (2026-06-14, round 132, backend `6191b91`)
- **배경**: round 131(`229f84c`/V103) → **`6191b91`** 전진 — `6191b91` **V104 `staff_training_logs`**(US-S02 FAQ21807/21828·BNK-184)·`StaffTrainingLogService`·compliance/list/create/update API·pilot/RBAC/routing tests. `git diff --name-only 229f84c..HEAD -- src/main/resources/db/migration/` = **V104 1파일**(coder).
- **V104 integrity 대조** (V88/V91 신규 staff 테이블 → V90/V92 후속 패턴):
  - ① **org sync 부재** — `organization_id` 앱 입력 의존 → **V105** `trg_staff_training_logs_set_org`(branch→org, V74 패턴)
  - ② **신규직원 배정 FK 부재** — `(org,new_hire_user_id)→users`만, `user_branches` 미연결 → **V105** `(org,new_hire_user_id,branch_id)→user_branches`
  - ③ **`created_by` actor backstop 부재** — 앱 명시 적재·`DbSessionContext.setActorUserId` 있으나 V32 패턴 미적용 → **V105**
  - ④ **`trained_at` 연도 CHECK 부재** — 앱 `validateTrainedAtYear`만 → **V105** `chk_staff_training_logs_trained_at_year`
  - ⑤ **purge/audit partial 부재** — `new_hire_user_id` cohort·`created_by` audit → **V105** 2건
- **Repository 8쿼리** — V104 `idx_staff_training_logs_org_branch_year_type`·`idx_staff_training_logs_org_branch_new_hire_user` 1:1 backing, 신규 조회 인덱스 0건.
- **Must billing·attendance·NHIS 핵심 제약 7건** SQL 물리 재확인 — **전부 불변**. agents.yaml `core_entities` 11종 전수 충족. `ls db/migration | wc -l` = **105** contiguous(V1–V105).
- **결론**: **V105 신규** + ERD §4-18-1·§7·§8·DATA_RETENTION §2/§3/§8·PLAN_NOTES #126. **보류**: `staff_attendance`/`staff_schedules`(Should). coder: V105 develop 커밋·push 후 `mvn flyway:migrate`·`mvn test` 재검증.

#### #125. J03 channel-readiness · G21 assigned-user guard · US-R02 CSV — 신규 DDL 0건 (2026-06-14, round 131, backend `229f84c`)
- **배경**: round 130(`39ee679`/V103) → **`229f84c`** 5커밋 전진 — `d4acab7` **J03 notification channel readiness status API**·`fffd355` email/quiet-hours gates·`229f84c` KST clock zone lock·`c16f4fe` **G21 assigned-user check-in guard**(QA-B73)·`c4dbe43` US-R02 staff status CSV export. `git diff --name-only 39ee679..HEAD -- src/main/resources/db/migration/` = **0파일**.
- **대조 결과**: `NotificationChannelReadinessService`·`NotificationChannelStatusController` — `NotificationProperties` env/config read-only, **DB 미사용**. `VisitService.validateAssignedUser`(G21 guard 강화) — V5 `uq_users_org_id`·V90 `uq_user_branches_org_user_branch` 기존 UK backed(PLAN_NOTES #120과 동일). US-R02 CSV — `UserRepository` 기존 V86 lifecycle 인덱스 재사용, 신규 `@Query` 0건. `git diff --name-only 39ee679..HEAD -- '**/*Repository.java'` = **0파일**.
- **Must billing·attendance·NHIS 핵심 제약 7건** SQL 물리 재확인 — **전부 불변**(`uq_claim_branch_month` V1·`uq_billing_claim_items_claim_client` V26·`chk_billing_claims_amount_sum` V6·`trg_billing_claims_total_reconciliation` V11·`chk_attendance_presence_xor_absence` V11/V14·`uq_nhis_import_rows_org_id` V37·`chk_nhis_import_rows_match_requires_client` V19→V54). agents.yaml `core_entities` 11종 전수 충족. `ls db/migration | wc -l` = **103** contiguous(V1–V103).
- **결론**: **신규 V104 불필요** + ERD §7-63·§8·DATA_RETENTION 메타·PLAN_NOTES #125 갱신. **보류**: `staff_attendance`/`staff_schedules`(Should). coder: `mvn flyway:migrate`·`mvn test` 재검증 권장.

#### #124. V102 G42 사후관리 follow-up · V103 RU-3/RU-4 seed 보정 — V104 불필요 (2026-06-13, round 130, backend `39ee679`)
- **배경**: round 129(`5692662`/V100) → **`39ee679`** 전진 — `f4c8558` **V101 integrity 커밋**(round 129 DBA 산출)·`2ebca70` **V102 `grievance_counseling_follow_up_g42`**(G42 FAQ21814 사후관리·재발 확인 API+DDL, BNK-161 P2)·`39ee679` **V103 `transport_service_fee_seed_correction_bnk_174`**(BNK-174 NHIS lawImg RU_3/RU_4 정본). `git diff --name-only 5692662..HEAD -- src/main/resources/db/migration/` = **V101·V102·V103 3파일**.
- **V102 integrity 대조** (V97→V98 신규 테이블 패턴과 구분 — **기존 테이블 컬럼 추가**):
  - ① **CHECK·partial index 선행 포함** — `chk_grievance_counseling_records_follow_up_fields`(pair NULL 일관성·notes 비공백·`approved_at` 필수·`follow_up_recorded_at>=approved_at`) + `idx_grievance_counseling_records_pending_follow_up`(APPROVED·미기록 큐) → raw SQL pair 불일치 1차 방어.
  - ② **actor backstop·FK·org sync·purge 인덱스 해당 없음** — 신규 FK/actor 컬럼 0건, 기존 APPROVED 행 UPDATE 경로.
  - ③ **재기록 immutability** — 앱 `recordFollowUp`이 `followUpRecordedAt != null` 거부. DB UPDATE 잠금 트리거(V83 signed-lock 패턴)는 **의도적 보류** — 사후관리 notes 정정 운영 요구 미확정(rules.md §11).
  - ④ **Repository 3쿼리 1:1 backing** — `countBy…FollowUpRecordedAtIsNull/IsNotNull`·`findBy…OrderByApprovedAtAsc` → V102 partial index.
- **V103**: `transport_service_fee_rates` UPDATE only — V68 drift(4430/6230) → NHIS 2026 정본(5230/8630). 스키마·인덱스·제약 0건.
- **Must billing·attendance·NHIS 핵심 제약 7건** SQL 물리 재확인 — **전부 불변**(`uq_claim_branch_month` V1·`uq_billing_claim_items_claim_client` V26·`chk_billing_claims_amount_sum` V6·`trg_billing_claims_total_reconciliation` V11·`chk_attendance_presence_xor_absence` V11/V14·`uq_nhis_import_rows_org_id` V37·`chk_nhis_import_rows_match_requires_client` V19→V54). agents.yaml `core_entities` 11종 전수 충족. `ls db/migration | wc -l` = **103** contiguous(V1–V103).
- **결론**: **신규 V104 불필요** + ERD §4-21·§4-9·§6·§7-61·§7-62·§8·DATA_RETENTION §2/§3/§8·PLAN_NOTES #124 갱신. **보류**: `staff_attendance`/`staff_schedules`(Should). coder: `mvn flyway:migrate`·`mvn test` 재검증 권장.

#### #123. V100 G30 모니터링 자체점검·전화상담 → V101 integrity 후속 (2026-06-13, round 129, backend `5692662`)
- **배경**: round 128(`edd2771`/V99) → **`5692662`** 전진 — `8bb6583` G9-COG NHIS import 게이팅·`aaa16f8` 8-12 직원현황 집계 API(US-R02)·`6a72b70` **V100 `monitoring_self_diagnoses`·`monitoring_phone_consultations`**(G30 FAQ21836·21841·BNK-169)·`5501745` route·`b8e92bf`/`5692662` 파일럿 E2E·RBAC. `git diff --name-only edd2771..HEAD -- src/main/resources/db/migration/` = **V100 1파일**(coder).
- **V100 누락 식별 → V101 해소** (V93 client_risk_assessments / V98 grievance 신규 테이블 패턴):
  - ① **`created_by` actor backstop 부재** — V100 두 테이블 모두 `created_by` nullable FK이나 `MonitoringService`가 명시 적재만 하고 V93/V98 `trg_*_set_created_by`(`ogada_read_actor_user_id`, V32) 미적용 → raw SQL INSERT 미커버 → **V101** 트리거 2건.
  - ② **전화상담 활성 이용자 가드 부재** — `MonitoringService.recordPhoneConsultation`은 `findByIdAndOrganizationIdAndActiveTrue`로 활성 이용자만 허용(안부전화 = 현재 이용자 대상)하나 DB 방어 부재 → **V101** `trg_monitoring_phone_consultations_guard_active_client`(V93 패턴, `is_active≠true OR discharged_at IS NOT NULL` 거부). 자체점검표(`monitoring_self_diagnoses`)는 이용자 비참조(지점 단위) → 가드 미해당.
  - ③ **FK backing 부재** — V100 복합 Tenant FK(`client_id`/`created_by`)에 PostgreSQL 자동 인덱스 없음·이용자 cohort purge 미지원(V100 `idx_*_org_branch_year_month`·UK 모두 `client_id`/`created_by` 선두 아님) → **V101** partial 3건(`idx_monitoring_phone_consultations_client_purge`·`idx_monitoring_phone_consultations_org_created_by`·`idx_monitoring_self_diagnoses_org_created_by`).
- **신규 조회 인덱스 0건**: `MonitoringSelfDiagnosisRepository`(2쿼리)·`MonitoringPhoneConsultationRepository`(3쿼리) 전부 V100 `idx_*_org_branch_year_month` + UK 1:1 backing. `ClientRepository.existsBy…ActiveTrueAndLtcGrade`(G9-COG 게이팅 `8bb6583`)는 기존 `(org, branch)` client 인덱스 prefix backing — 신규 인덱스 불요.
- **V100 자체 완결분**: 도메인 CHECK(year 2000~2100·month 1~12·item_code 1~15)·본문 NOT-EMPTY·`updated_at>=created_at`·복합 Tenant FK 5건·월 단위 UK — V101은 신규 컬럼·도메인 CHECK 추가 없음(actor/guard/index만).
- Must billing·attendance·NHIS 핵심 제약 7건 불변. agents.yaml `core_entities` 11종 전수 충족(monitoring은 G30 확장 — core_entities 외). `ls db/migration | wc -l` = **101** contiguous(V1–V101).
- **결론**: **V101 신규** + ERD §4-22·§6·§7·§8·DATA_RETENTION §3/§8·PLAN_NOTES #123 갱신. **보류**: G30 모니터링 FE Panel·8-12 PDF 7종(P2)·`staff_attendance`/`staff_schedules`(Should). coder: V101 develop 커밋·push 후 `mvn flyway:migrate`·`mvn test` 재검증 권장.

#### #122. V99 G9-COG 인지지원등급 `ltc_grade` 0 — 신규 DDL 0건·V100 불필요 (2026-06-13, round 128, backend `edd2771`)
- **배경**: round 127(`8487667`/V97) → **`edd2771`** 전진 — `b0a9e06`/`bcdc411` G42·`8487667` G34b·`6ef671b` **V99 `cognitive_support_ltc_grade_g9`**(G9-COG FE+BE·BNK-166)·`edd2771` bulk NHIS seed apply. `git diff --name-only 8487667..HEAD -- src/main/resources/db/migration/` = **V98·V99 2파일**(V98 round 127 DBA 산출·V99 coder).
- **V99 자체 완결**: 4테이블 CHECK 확장만 — `clients`·`fee_schedules`·`billing_claim_items`·`client_ltc_grade_history`의 `ltc_grade`/`previous_grade`/`new_grade`를 `BETWEEN 0 AND 5`로 통일. 신규 컬럼·FK·트리거·인덱스 0건 → **V100 integrity 후속 불필요**(V97→V98 패턴 미해당).
- **대조 결과**: Must billing·attendance·NHIS 핵심 제약 7건 불변. agents.yaml `core_entities` 11종 전수 충족. `ls db/migration | wc -l` = **99** contiguous(V1–V99).
- **DB 경계 명문화**: grade 0 월 급여한도(`MonthlyBenefitCapCatalog`)·등급 0 `fee_schedules` Tenant 시드는 **앱/NHIS bulk apply** 책임 — DB는 도메인 허용만(V99). `fee_schedules` EXCLUDE·`uq_fee_schedule_current`(V61)는 grade 0을 별도 키로 취급해 1–5와 비중첩 공존.
- **결론**: **신규 V100 불필요** + ERD §4-3·§4-6·§4-10·§6·§7-60·§8·DATA_RETENTION §2 갱신. **보류**: grade 0 수가 시드 운영 가이드·`staff_attendance`/`staff_schedules`(Should). coder: `mvn flyway:migrate`·`mvn test` 재검증 권장.

#### #121. V97 G42 고충상담 기록 integrity 후속 → V98 신규 (2026-06-13, round 127, backend `8487667`)
- **배경**: round 126(`2925ff7`/V96) → **`8487667`** 전진 — `b0a9e06` **V97 `grievance_counseling_records`**(G42 이지케어 FAQ21814·케어포 func.php 8-8 지표7) + `bcdc411`/`0460e9b`/`994f5ea`/`1b5fabe`/`8487667`. `git diff --name-only 2925ff7..HEAD -- src/main/resources/db/migration/` = **V97 1파일**(coder).
- **V97 자체 완결**: 5채널 receipt(`WRITTEN`/`PHONE`/`SMS`/`IN_PERSON`/`ANONYMOUS_BOX`) · 3종 target polymorphism(`CLIENT`/`CAREGIVER`/`OTHER` + `chk_*_target_links` 상호배타) · DRAFT/SUBMITTED/APPROVED 전자결재(`chk_*_submitted_fields` NULL 일관성) · Tenant 복합 FK 6건(branch·client·client_branch·staff_user·approved_by·created_by) · `idx_*_org_branch_counseled_at` 목록 인덱스.
- **V97 누락 식별 → V98 해소**: ① **결재 시각 정합 부재** — `chk_*_submitted_fields`가 NULL 일관성만 강제, `submitted_at>=created_at`·`approved_at>=submitted_at` 부재(raw SQL 백데이트 전이 가능) → **V98** 2건 CHECK(V36/V94 temporal 패턴). ② **`created_by` actor backstop 부재** — `GrievanceCounselingService`는 `entity.setCreatedBy(actorId)`로 명시 적재하나 V83/V81 패턴 미적용(raw SQL INSERT 미커버) → **V98** `trg_*_set_created_by`. ③ **FK backing 부재** — V97의 6건 복합 Tenant FK(`client_id`/`staff_user_id`/`approved_by`/`created_by`)에 PostgreSQL 자동 인덱스 없음 → **V98** partial 인덱스 4건(NULL-heavy target polymorphism용). ④ **결재 큐 핫패스 부재** — `approval_status='SUBMITTED'` 결재함 widget(123차 P2 잔여)을 위한 부분 인덱스 → **V98** `idx_*_org_branch_pending_approval`.
- **활성 client/staff 가드 의도적 보류**: V81/V83/V93/V95는 퇴소·비활성 이용자 INSERT를 DB에서 차단하나, G42는 **퇴소·퇴사 후 사후관리·과거 사건 백데이트 등록 허용**이 필요(`counseled_at` 백데이트·익명함 사후 처리 — BNK-161 P2 사후관리 스코프). 앱은 신규 등록 시 `findByIdAndOrganizationIdAndActiveTrue`·`isActive && terminatedAt IS NULL`로 활성 강제. DB 가드는 추가하지 않음(rules.md §11 변경 범위 제어).
- `GrievanceCounselingRepository` 3쿼리 — V97 PK + `idx_*_org_branch_counseled_at` 1:1 backing, 신규 조회 인덱스 0건. Must billing·attendance·NHIS 핵심 제약 7건 불변. agents.yaml `core_entities` 11종 전수 충족(`grievance_counseling_records`는 `audit_logs` 대체 아님 — 별도 결재 워크플로 테이블). `ls db/migration | wc -l` = **98** contiguous(V1–V98).
- **결론**: **V98 신규** + ERD §4-21·§6·§7·§8·DATA_RETENTION §2/§3/§4-1/§8 갱신. **보류**: G42 P2(전자결재 UI·익명함·사후관리 BNK-161)·8-12 PDF 7종 P2·G34b live E2E run·`staff_attendance`/`staff_schedules`(Should). coder: V98 develop 커밋·push 후 `mvn flyway:migrate`·`mvn test` 재검증 권장.

#### #120. V96 커밋 확인 · G21 방문일정 배정 직원 검증 backing 재대조 — 신규 DDL 0건 (2026-06-13, round 126, backend `2925ff7`)
- **배경**: round 125(`bdfc140`/V95) → **`2925ff7`** 3커밋 전진 — `a7b4a39` **V96 integrity 커밋**(round 119 DBA 산출, G40b `recorded_at>=created_at` CHECK)·`dc48933` **G21 방문일정 생성/수정 시 배정 직원 검증**·`2925ff7` G21 day-care guard 체크인/아웃 테스트.
- **대조 결과**: `git diff --name-only bdfc140..HEAD -- src/main/resources/db/migration/` = **V96 1파일**(coder 커밋, round 119 산출) → round 125 이후 **신규 스키마 변경 0건**. `src/main/` 변경 = `VisitService.java`(G21 `validateAssignedUser`) + `UserBranchRepository.java`(신규 메서드 1개).
- **G21 신규 repository 쿼리 ↔ 기존 제약 backing (DB 이중 방어, 신규 DDL 불요)**: `VisitService.validateAssignedUser`(`POST /visits`·`PATCH /visits/{id}` 배정 직원 검증)가 호출하는 2쿼리 모두 기존 제약 1:1 backed.
  - `userRepository.findByIdAndOrganizationId(assignedUserId, organizationId)` → **V5 `uq_users_org_id`** `(organization_id, id)` UNIQUE 앵커 + PK. 퇴사·비활성(`is_active=false`/`terminated_at IS NOT NULL`) 거부는 앱 레이어(`users.terminated_at` = V86 staff lifecycle read-only).
  - `userBranchRepository.existsByOrganizationIdAndUserIdAndBranchId(organizationId, assignedUserId, branchId)` → **V90 `uq_user_branches_org_user_branch`** `(organization_id, user_id, branch_id)` UNIQUE 인덱스에 prefix-exact 매핑 — 별도 인덱스 불요. (배정 직원이 해당 지점에 배속된 직원인지 검증; `visit_schedules.assigned_user_id` self-FK는 V53 `fk_visit_schedules_assigned_user_org` + V56 `idx_visit_schedules_org_assigned_date`로 별도 backed.)
- Must billing·attendance·NHIS 핵심 제약 7건 불변(`uq_claim_branch_month` V1·`uq_billing_claims_org_id` V10·`uq_billing_claim_items_claim_client` V26·`uq_nhis_import_rows_org_id` V37·출석 집계 V22/V25/V26 partial·시간 정합 V4/V11/V14/V15/V37). agents.yaml `core_entities` 11종 전수 충족. `ls db/migration | wc -l` = **96** contiguous(V1–V96).
- **결론**: **신규 V97 마이그레이션·테이블·인덱스·제약 불필요**(rules.md §1·§17) — G21 배정 직원 검증은 V5/V90 UK 위의 앱 레이어 강화. 본 라운드: ERD §4-12 배정 직원 검증 backing 행 추가 + ERD/DATA_RETENTION 메타 timestamp 갱신. **보류**: G40b/G40 live E2E run·`staff_attendance`/`staff_schedules`(Should). coder: `mvn flyway:migrate`·`mvn test` 재검증 권장.

#### #119. V95 G40b periodic risk assessment · V96 integrity 후속 (2026-06-13, round 125, backend `bdfc140`)
- **배경**: round 124(`686d686`/V94) → **`bdfc140`** — coder **V95** `client_periodic_risk_assessments`(G40b 이지케어 지표16·FAQ21811 반기 3종)·`ClientRiskAssessmentService` periodic API·compliance.
- **대조 결과**: `git diff --name-only 686d686..HEAD -- src/main/resources/db/migration/` = **V95 1파일**. V95가 V93→V94 패턴과 달리 org sync·퇴소 guard·actor backstop·purge partial·compliance `idx_*_org_branch_period`을 **선행 포함**(coder `84e59d2`).
- **V95 누락 1건 → V96 해소**: `recorded_at>=created_at` temporal CHECK(V94 패턴). compliance branch sweep은 `idx_client_periodic_risk_assessments_org_branch_period`로 이미 1:1 backing — 별도 `org_branch` 인덱스 불요(fiscal_year/half 열 포함).
- Must billing·attendance·NHIS 핵심 제약 7건 불변. agents.yaml `core_entities` 11종 전수 충족. `ls db/migration | wc -l` = **96** contiguous(V1–V96).
- **결론**: **V96 신규** + ERD §4-20·§6·§7·§8·DATA_RETENTION. **보류**: G40b live E2E run·`staff_attendance`·`staff_schedules`(Should). coder: V96 push 후 `mvn flyway:migrate`·`mvn test`.

#### #118. V93 G40 admission risk assessment · V94 integrity 후속 (2026-06-13, round 124, backend `686d686`)
- **배경**: round 123(`4a622ab`/V92) → **`686d686`** — coder **V93** `client_risk_assessments`(G40 silverangel 지표21 3종)·`ClientRiskAssessmentService`·compliance API.
- **대조 결과**: `git diff --name-only 4a622ab..HEAD -- src/main/resources/db/migration/` = **V93 1파일**. V93가 V91→V92 패턴과 달리 org sync·퇴소 guard·actor backstop·purge partial을 **선행 포함**(coder `22d736b`).
- **V93 누락 2건 → V94 해소**: ① compliance branch sweep `(organization_id, branch_id)` 인덱스(`findByOrganizationIdAndBranchId`) ② `recorded_at>=created_at` temporal CHECK(V90 패턴).
- Must billing·attendance·NHIS 핵심 제약 7건 불변. agents.yaml `core_entities` 11종 전수 충족(`health_records` medication polymorphic·`meal_records`/`activity_programs` V49). `ls db/migration | wc -l` = **94** contiguous(V1–V94).
- **결론**: **V94 신규** + ERD §4-19·§6·§7-59·§8·DATA_RETENTION. **보류**: G40 FE Panel(P2)·`staff_attendance`·`staff_schedules`(Should). coder: V94 push 후 `mvn flyway:migrate`·`mvn test`.

#### #117. V91 staff HR file hub · V92 integrity 후속 (2026-06-13, round 123, backend `4a622ab`)
- **배경**: round 122(`1817c36`/V90) → **`4a622ab`** — coder **V91** `staff_hr_files`(US-R03 HR file hub·FAQ21806 8종)·G2 CMS cancellation API(기존 `CANCELLED` status 재사용).
- **대조 결과**: `git diff --name-only 1817c36..HEAD -- src/main/resources/db/migration/` = **V91 1파일**. `StaffHrFileRepository` 3쿼리 — V91 `idx_staff_hr_files_org_user_uploaded`·UK `(org,user,document_type)` 1:1 backing → **신규 조회 인덱스 0건**.
- **V91 누락 4건 → V92 해소**: ① org-sync 트리거 ② `uploaded_by` actor backstop ③ `uploaded_at>=created_at` CHECK ④ `user_id` purge·`org_uploaded_by` partial 인덱스. (배정 FK·Tenant FK는 V91 선행 완료)
- **G2 CMS cancellation**: `CmsService.cancelEnrollment` — `status='CANCELLED'` V59 CHECK 재사용, 신규 컬럼·인덱스 불요.
- Must billing·attendance·NHIS 핵심 제약 7건 불변. agents.yaml `core_entities` 11종 전수 충족. `ls db/migration | wc -l` = **92** contiguous(V1–V92).
- **결론**: **V92 신규** + ERD §4-18·§6·§7·§8·DATA_RETENTION. **보류**: FAQ21806 6단계 workflow CRUD(P2)·`staff_attendance`·`staff_schedules`(Should). coder: V92 push 후 `mvn flyway:migrate`·`mvn test`.

#### #116. V88–V90 staff HR 첨부·건강검진 integrity 후속 (2026-06-13, round 122, backend `1817c36`)
- **배경**: round 121(`9c9fd5b`) → **`1817c36`** — coder **V88** `staff_refresher_training_certificates`(US-S02 8-7-1 이수증)·**V89** `staff_health_checkups`(US-R02 8-10 건강검진). round 121은 compliance bool만·P2 첨부 보류로 **V88 불필요** 결론이었으나 coder가 V88/V89 선행 착수.
- **대조 결과**: `git diff --name-only 9c9fd5b..HEAD -- src/main/resources/db/migration/` = **V88+V89 2파일**. Repository 쿼리(`StaffRefresherTrainingCertificateRepository`·`StaffHealthCheckupRepository`) — V88/V89 인덱스 1:1 backing → **신규 조회 인덱스 0건**.
- **V88/V89 누락 5건 → V90 해소**: ① `uq_user_branches_org_user_branch` on `user_branches`(V79 패턴) ② `(org,user_id,branch_id)→user_branches` composite FK 2테이블 ③ org-sync 트리거 2건 ④ `uploaded_by`/`recorded_by` actor backstop ⑤ `uploaded_at>=created_at`·`checkup_date` not-in-future CHECK + purge/actor partial 인덱스.
- Must billing·attendance·NHIS 핵심 제약 7건 불변. agents.yaml `core_entities` 11종 전수 충족. `ls db/migration | wc -l` = **90** contiguous(V1–V90).
- **결론**: **V90 신규** + ERD §4-16·§4-17·§7-57·DATA_RETENTION 보수교육·건강검진 행. **보류**: US-R02 P2 건강검진 파일함 첨부·`staff_attendance`·`staff_schedules`(Should). coder: V90 push 후 `mvn flyway:migrate`·`mvn test`.

#### #115. US-S02 8-7-1 보수교육 compliance · V84–V87 마이그레이션 표 정합 — 신규 DDL 0건 (2026-06-13, round 121, backend `9c9fd5b`)
- **배경**: round 120(`82bdbcd`/V86·V87) → **`9c9fd5b`** 8커밋 — US-R03 lifecycle API+V86·**V87 integrity**(`cc7da1a`)·**US-S02 보수교육 compliance API**(`9c9fd5b`, BNK-136).
- **대조 결과**: `git diff --name-only cc7da1a..HEAD -- src/main/resources/db/migration/` = **0파일**. V87 이후 신규 스키마 0건. `StaffRefresherTrainingService` 쿼리 3종(`findByOrganizationId`·`findByUserIdIn`·`findByOrganizationId`) — V1/V29/V86 기존 인덱스 1:1 backing.
- **US-S02 DB 경계**: compliance는 `users.hired_at` + `lifecycle_checklist` JSONB 키 `refresher-training`(bool)만 사용 — 격년 due·4상태는 앱 도메인(`StaffRefresherTrainingCompliance`). **별도 테이블·CHECK·인덱스 불요**. P2 이수증 첨부·직원 파일함 확정 시 `staff_training_records`(또는 `users` 첨부 FK) DDL 검토 — 현재 보류.
- **ERD drift 해소**: §7 마이그레이션 표 V84–V87 행 누락 보완·§4-2 US-S02·§7-56·§8 매핑·헤더 DDL 범위 V87 갱신.
- Must billing·attendance·NHIS 핵심 제약 7건 불변. agents.yaml `core_entities` 11종 전수 충족. `ls db/migration | wc -l` = **87** contiguous(V1–V87).
- **결론**: Must 스코프 **신규 V88 불필요** — 문서 갱신만. **보류**: `staff_attendance`·`staff_schedules`(Should)·US-S02 P2 이수증. coder: `mvn flyway:migrate`·`mvn test`.

#### #114. V82 G34 lead caregiver work log · V83 integrity 후속 (2026-06-12, round 118, backend `559648f`)
- **배경**: round 117(`3ad2a90`) → **`559648f`** 전진 — coder `feat(v2/G34): add lead caregiver work log API (US-S01)` + **V82** `lead_caregiver_work_logs`.
- **대조 결과**: `git diff --name-only 3ad2a90..HEAD -- src/main/resources/db/migration/` = **V82 1파일**. `LeadCaregiverWorkLogRepository` 쿼리 4건 — V82 `idx_lead_caregiver_work_logs_org_branch_date`·UK `(org, client_id, log_date)` 1:1 backing → **신규 조회 인덱스 0건**.
- **V82 누락 5건 → V83 해소**: ① org/branch sync 트리거 ② 퇴소 INSERT 가드 ③ `created_by` actor backstop ④ 서명 후 UPDATE 잠금(`signature_status='SIGNED'`) ⑤ `idx_*_client_purge`·`idx_*_org_created_by` partial.
- **보류**: `SMS_VERIFIED` 보호자 링크 서명 토큰 테이블 — v2 P2(앱 workflow only, BNK-105 triple-source). `staff_attendance`·`staff_schedules`(REQUIREMENTS §3-8) — agents.yaml Should, DDL 미착수.
- Must billing·attendance·NHIS 핵심 제약 7건 불변. agents.yaml `core_entities` 11종 전수 충족. `ls db/migration | wc -l` = **83** contiguous(V1–V83).
- **결론**: **V83 신규** + ERD §4-15·§7-53·DATA_RETENTION G34 행. **API_SPEC drift**: `/staff/lead-caregiver-logs` — PLN/TWR 정렬 권장. coder: V83 push 후 `mvn flyway:migrate`·`mvn test`.

#### #113. G38/G39 대시보드 집계 · 파일럿 E2E 재대조 — 신규 DDL 0건 (2026-06-12, round 117, backend `3ad2a90`)
- **배경**: round 116(`a0a7f9c`/V81) → **`3ad2a90`** 5커밋 — `7ba18c1`/`70d76a4`/`15b3c7e` **G38-G39 HQ/branch 대시보드 compliance 스냅샷 집계**(FE용)·`0ed781f` G17-G32 program compliance 편집흐름 파일럿 E2E·`3ad2a90` G21-G32 방문 편집-취소·사례관리 파일럿 E2E.
- **대조 결과**: `git diff --name-only a0a7f9c..HEAD -- src/main/resources/db/migration/` = **0파일**. 변경 9파일 = `dashboard/`(DashboardService·HqDashboardResponse·BranchDashboardResponse)·`casemanagement`/`programs` 서비스 + 테스트 4파일 — **Repository.java 변경 0파일** → 신규 쿼리·`@Query` 0건.
- **집계 호출 repository 메서드 전부 `a0a7f9c` 선재**(`git grep -l` 확인): 출석 `countBy…AttendanceDateAndCheckInAt/CheckOutAt/AbsenceReasonIsNotNull`(V22 `idx_attendance_branch_present`/`_checkout`/`_absence` partial + V2 `idx_attendance_branch_date`)·`nhisImportRowRepository.countBy…MatchStatus`(V22 `(org, match_status)`)·`billingClaimItemRepository.countOverdueItemsByBranch`·`clientRepository.countBy…ActiveTrue/False`(#108–112 backed 메서드 재호출) — in-memory 집계 재사용 → **신규 인덱스 0건**.
- Must billing·attendance·NHIS 핵심 제약 7건 불변. agents.yaml `core_entities` 11종 전수 충족. `ls db/migration | wc -l` = **81** contiguous(V1–V81).
- **결론**: Must 스코프 **신규 V82 불필요** — 기존 repository 집계 재사용 + 파일럿 E2E. ERD round 117 검증 기록·메타 timestamp 갱신. **API_SPEC drift**: G38-G39 HQ/branch 대시보드 compliance 스냅샷 필드 미반영(실측 DTO PRESENT) — PLN/TWR 정렬 권장(DBA 비소유). coder: `mvn flyway:migrate`·`mvn test` 재검증.

#### #112. V81 커밋 확인 · G38/G39 compliance 재대조 — 신규 DDL 0건 (2026-06-12, round 116, backend `a0a7f9c`)
- **배경**: round 115(`f082933`/V80) → **`a0a7f9c`** 5커밋 — `5fd35a6` **G38 care-plan notification compliance**(BNK-106)·`f082933` V80 G39·`3ca37ff` **V81 integrity 커밋**(round 115 DBA 산출)·`03211e6`/`a9f8bda`/`a0a7f9c` G38-G39 dashboard widget counts.
- **대조 결과**: `git diff --name-only f082933..HEAD -- src/main/resources/db/migration/` = **V80+V81 2파일**(coder). `git diff --name-only 3ca37ff..HEAD -- src/main/resources/db/migration/` = **0파일** → V81 이후 **신규 스키마 변경 0건**. 신규 repository 쿼리: G38 3건·G39 compliance 4건 — 전부 기존 인덱스 1:1 backing(ERD §4-10 G38·§4-14 compliance bullet).
- **V81 자체 완결**: org/branch sync·퇴소 INSERT 가드·`created_by` actor backstop·purge/actor partial 인덱스 — V74 functional_recovery/case_management 패턴 정렬. **DBA 후속 V82 불필요**.
- Must billing·attendance·NHIS 핵심 제약 7건 불변. agents.yaml `core_entities` 11종 전수 충족. `ls db/migration | wc -l` = **81** contiguous(V1–V81).
- **결론**: Must 스코프 **신규 V82 불필요**. ERD round 116 검증 기록·§4-10 G38·§4-14 compliance·§8 매핑·메타 timestamp 갱신. **API_SPEC drift**: G38 compliance·G39 dashboard widget — PLN/TWR 정렬 권장. coder: `mvn flyway:migrate`·`mvn test` 재검증.

#### #111. V78 G37 인정기간 계획서 첨부 integrity 후속 → V79 신규 (2026-06-12, round 114, backend `0325d95`)
- **배경**: round 113(`838a7f6`) → **`0325d95`** 5커밋 — 파일럿 E2E 3건(G17-G32·G33·G2-G21)·J03 주 보호자 우선 배차(`555a19f`+E2E)·**`0325d95` V78 G37 인정기간 계획서 첨부**(BNK-105, 이지케어 FAQ `49a778e8`).
- **대조 결과**: `git diff --name-only 838a7f6..HEAD -- src/main/resources/db/migration/` = **V78 1파일**(coder). 신규 repository 2건(`ClientLtcGradeHistoryAttachmentRepository`·`ClientLtcGradeHistoryRepository`) — 쿼리 5건 전부 기존 인덱스 1:1 backing(`org_history`·`org_client`·V48 `org_client_changed`·PK) → **신규 조회 인덱스 0건**.
- **V78 누락 4건 → V79 해소**: ① **cross-client 링크 갭** — 첨부 `history_id`가 `(org, history_id)` FK로만 묶여 동일 Tenant 내 **다른 이용자** 등급이력 연결 가능(앱은 read만 가드). 부모 `client_ltc_grade_history`에 `uq_(org, client_id, id)` 추가 후 첨부 FK를 `(org, client_id, history_id)`로 교체(`ON DELETE CASCADE` 유지) → DB에서 동일 이용자 강제. ② `uploaded_by` 세션 actor backstop(V70 패턴). ③ `uploaded_at >= created_at` CHECK(V48 패턴). ④ clients CASCADE/퇴소 purge 인덱스 `idx_..._client_purge`(`client_id` 선두) + `idx_..._org_uploaded_by` partial.
- **J03/G17/G2**: 배차 우선·급여개시 compliance·CMS debit FAILED 이력은 Java/E2E 레이어 — 비첨부 repository 변경 0건, DB 불요.
- Must billing·attendance·NHIS 핵심 제약 7건 불변. agents.yaml `core_entities` 11종 전수 충족. `ls db/migration | wc -l` = **79** contiguous(V1–V79).
- **결론**: **V79 신규** + ERD §4-10·인덱스·마이그레이션 목록·DATA_RETENTION 갱신. **API_SPEC drift**: G37 첨부 엔드포인트 미반영(실측 컨트롤러 PRESENT) — PLN/TWR 정렬 권장(DBA 비소유). coder: V79 push 후 `mvn flyway:migrate`·`mvn test` 재검증.

#### #110. V76 G33 billing start balance · V77 integrity 후속 (2026-06-12, round 112, backend `70e6191`)
- **배경**: round 111(`208b37e`) → **`70e6191`** 6커밋 — `3d5eb3e` **V76 G33**·ledger/overdue/settlement Java(`e7df238`/`deaae7a`/`70e6191`).
- **대조 결과**: `git diff --name-only 208b37e..HEAD -- src/main/resources/db/migration/` = **V76 1파일**. 신규 repository 쿼리 0건.
- **V76 누락 3건 → V77 해소**: ① `billing_start_balance_set_by` Tenant FK ② initial lock actor backstop ③ post-lock immutability + positive amount monotonic decrease (settlement).
- **인덱스**: G33 조회는 `organizations` PK — **신규 0건**. Must billing·attendance·core_entities 11종 충족. `ls db/migration | wc -l` = **77**.
- **결론**: **V77 신규**. API_SPEC G33 엔드포인트 미반영 — PLN 정렬 권장. coder: V77 push 후 `mvn flyway:migrate`·`mvn test`.

#### #109. V75 case_management_plan 커밋 확인 · G32 지표29 compliance 쿼리 backing 재대조 — 신규 DDL 0건 (2026-06-12, round 111, backend `208b37e`)
- **배경**: round 110(`5e1828c`) → **`208b37e`** 5커밋 전진 — `0a270a2` **V75 `case_management_plan`**(BNK-91 P2)·`8431b5c` US-L03 취소 CMS 재등록 재사용·`11277b9` **G32 지표29 평가실시 compliance**(BNK-92 P1)·`98e40a3` Solapi 승인 템플릿 매핑·`208b37e` hq_admin client 생성 허용.
- **대조 결과**: `git diff --name-only 5e1828c..HEAD -- src/main/resources/db/migration/` = **V75 1파일**(coder `0a270a2`). `git diff --name-only 5e1828c..HEAD -- '**/*Repository.java'` = **2파일**(`ProgramParticipationRepository`·`FunctionalRecoveryPlanRepository` — 지표29 신규 `@Query` 2건).
- **V75 자체 완결**(coder 소유): `case_management_meetings.case_management_plan TEXT NOT NULL` + `chk_case_management_meetings_plan_nonempty`(trim>0), 기존 행 `meeting_result` backfill 후 NOT NULL 승격. TEXT 본문 → FK·인덱스 불요; V73/V74 org-branch sync·active guard·actor backstop 트리거는 INSERT 페이로드 확장에 always-true 비간섭 → **DBA 후속 integrity 마이그레이션 불필요**.
- **지표29 compliance 쿼리 2건 ↔ 기존 인덱스 1:1 backing**: (a) `existsAttendedFunctionalRecoveryForClientInDateWindow`(org+client+`status='ATTENDED'`+record_date 윈도우·activity_programs PK 조인 program_type) → V49 **`idx_program_participations_client_date`** + 조인측 V49 `idx_activity_programs_org_branch_type_date`; (b) `existsUpdatedPlanForClientInWindow`(org+client+updated_at 윈도우) → V72 **`uq_functional_recovery_plans_client_year`**(org+client 접두어, 이용자당 연도 UK로 행 극소) — **신규 인덱스 0건**.
- Must billing·attendance·NHIS 핵심 제약 7건 불변. agents.yaml `core_entities` 11종 전수 충족. `ls db/migration | wc -l` = **75** contiguous(V1–V75, 갭·중복 0).
- **결론**: Must·G32 스코프 **신규 V76 불필요**. **API_SPEC drift**: `case_management_plan` 필드·지표29 compliance 응답 미반영(실측 컨트롤러 PRESENT) — PLN/TWR 정렬 권장(DBA 비소유). coder: develop push 후 `mvn flyway:migrate`·`mvn test` 재검증.

#### #108. V74 커밋 확인 · NHIS 청구 대조 API·G32 앱 가드 재대조 — 신규 DDL 0건 (2026-06-11, round 110, backend `5e1828c`)
- **배경**: round 109(`55fae99`) → **`5e1828c`** 4커밋 전진 — `622b5e5` **V74 integrity guards 커밋**(round 109 DBA 산출)·`2225a7a` NHIS claim comparison API + G32 attendee_names 정규화·`fea28b8` G32 분기 쿼리 bounds·`5e1828c` 테스트.
- **대조 결과**: `git diff --name-only 55fae99..HEAD -- src/main/resources/db/migration/` = **V74 1파일**(`622b5e5`). `git diff --name-only 622b5e5..HEAD -- src/main/resources/db/migration/` = **0파일** → V74 이후 **신규 스키마 변경 0건**. `git diff 622b5e5..HEAD -- '**/Repository.java'` = 빈 목록.
- **NHIS comparison**(`getClaimNhisComparison`): `uq_billing_claims_org_id`(V10)·`idx_billing_claim_items_claim_created`(V29)·`idx_nhis_import_batches_org_branch_claim_created`(V37)·`idx_nhis_import_rows_batch_created`(V28) — read-only, 신규 인덱스 0건.
- **G32**: attendee_names 정규화·분기 bounds — 앱 레이어; DB V73/V74 불변(#107 참석자 ≥2명 CHECK 보류 유지).
- Must billing·attendance·core_entities 11종 전수 충족. `ls db/migration | wc -l` = **74** contiguous(V1–V74).
- **결론**: Must 스코프 **신규 V75 불필요**. API_SPEC `nhis-comparison` 미반영 — PLN 정렬 권장. coder: `mvn flyway:migrate`·`mvn test` 재검증.

#### #106. V71–V73 coder DDL · V74 integrity 후속 (2026-06-11, round 109, backend `55fae99`)
- **배경**: develop HEAD **`55fae99`** — V71(`de49b21` 환불)·V72(`73e169a` G17)·V73(`55fae99` G32) coder 커밋 완료. `ls db/migration` = **74개** contiguous(V1–V74).
- **V71 대조**: `billing_claims.status` REFUNDED·`refunded_*` 4컬럼·PAID→REFUNDED guard·Tenant FK `refund_recorded_by`·partial `idx_billing_claims_org_branch_status_refunded_at` — API `POST /billing/claims/{id}/refunds`·`GET /billing/reports/refunds` 1:1. **V74** `refund_amount > 0`·`refunded_at >= paid_at` CHECK + `trg_billing_claims_set_refund_recorded_by`(V52 대칭).
- **V72 대조**: `activity_programs.program_type`·`functional_recovery_plans` UK `(org, client, plan_year)` — `FunctionalRecoveryController` backing. **V74** 퇴소 guard·org sync·actor·purge.
- **V73 대조**: `case_management_meetings` 6필수 필드·분기 UK — `CaseManagementController` backing. **V74** date/year/quarter CHECK·V70 패턴 guard/actor/purge.
- **보류 (#107)**: ① 참석자 ≥2명 — `attendee_names` TEXT 쉼표/줄바꿈 구분은 **앱**(`validateAttendeeCount`) 전담, DB CHECK 미도입(구분자 규칙 미확정). ② 30일 급여반영 — cross-table(`program_participations`/`billing_claims`) CHECK 보류, compliance JPQL 앱 전담. ③ `billing_addons` mutually exclusive(BNK-47) — v2+ Epic V, PLN 확정 전.
- **결론**: Must billing·attendance·core_entities 11종 전수 충족. coder: V74 커밋 후 `mvn flyway:migrate`·`mvn test` 재검증.

#### #105. 방문일정 수기 중복 슬롯 가드 — V66 재사용·partial UNIQUE 보류 (2026-06-11, round 108, backend `970c7af`)
- **배경**: round 107(`1af5b1f`) → **`970c7af`** 6커밋 전진 — `VisitService.ensureNoDuplicateVisitSlot` + `VisitScheduleRepository.existsBy…PlannedStartTime…PlannedEndTime…IdNotAndStatusIn` 추가로 round #100에서 **보류했던 수기 create/update 중복 슬롯 가드**를 구현(`POST /visits` create·paired BILLING·`PATCH /visits/{id}` update·paired). 그 외 `BillingService`/`NhisImportService`/`FeeScheduleYearCoverage`(US-G04 귀속연도 25칸 수가 커버리지 — 인메모리 집계, DB 미사용).
- **대조 결과**: `git diff --name-only 1af5b1f..HEAD -- src/main/resources/db/migration/` = **0파일**. 변경 repository 1건(`VisitScheduleRepository`) — 신규 쿼리 1건뿐. 워크스페이스 submodule 실측 — HEAD `970c7af`·branch develop·working tree clean.
- **신규 쿼리 ↔ V66 backing(정확 일치)**: `existsBy…AndIdNotAndStatusIn`의 등치 7열(org·branch·client·visit_date·schedule_kind·planned_start_time·planned_end_time) + `StatusIn` 집합 `IMPORT_DUPLICATE_BLOCKING_STATUSES`={DRAFT,CONFIRMED,IN_PROGRESS,COMPLETED}은 **V66 `idx_visit_schedules_org_branch_client_slot_duplicate` partial 술어와 정확히 일치** → 완전 backing. `id <> ?`는 비인덱스 trivial 필터(자기 제외, 결과 1행 필터). **신규 인덱스 0건**.
- **partial UNIQUE 보류(재검토 결과)**: round #100이 "수기 가드 확정 후 검토"로 미뤘던 partial UNIQUE를 재평가 — **이번 라운드도 보류**. ① NULL-distinct: `planned_start_time`/`planned_end_time` NULL 허용(V53 `chk_visit_schedules_time_order`) → PG 기본 NULL-distinct로 UNIQUE가 NULL-time 중복을 강제 못함(앱 derived 쿼리는 null→`IS NULL` 등치로 차단 — DB가 앱보다 느슨, 정합성 역전 없음). ② 배포 안전성: 가드 신설(`970c7af`) 이전 생성된 활성 중복 행 존재 시 `CREATE UNIQUE INDEX`(Flyway 트랜잭션 내, non-CONCURRENTLY) 실패 → 전체 마이그레이션·배포 차단(rules.md §16 Reliability > Convenience, §6 롤백 고려). ③ v2/G21 안정화 단계(rules.md §17). → 동시 INSERT race·raw SQL 우회 방어는 v2 데이터 정착 후 `CONCURRENTLY`+사전 dedup 확정 시 재검토. PLAN↔BILLING 페어는 `schedule_kind`가 인덱스 열이라 충돌 없음.
- Must billing·attendance·NHIS 핵심 제약 7건 불변. agents.yaml `core_entities` 11종 전수 충족. `ls db/migration | wc -l` = **70개** contiguous(V1–V70).
- **결론**: Must 스코프 **신규 V71 마이그레이션·테이블·인덱스·제약 불필요**. 본 라운드: ERD §6 V66 행에 수기 가드 backing 명시 + §7-49 신설 + ERD/DATA_RETENTION 메타 timestamp 갱신 — 스키마 변경 0건. **coder 메모**: 수기 중복 가드는 앱+V66 인덱스로 end-to-end 동작 — 추가 DDL 불요. develop push 후 `mvn flyway:migrate`·`mvn test` 재검증 권장.

#### #104. G26 의료비공제 · G2 CMS debit integrity 재대조 — 신규 DDL 0건 (2026-06-11, round 107, backend `1af5b1f`)
- **배경**: round 106(`ed730a2`) → **`1af5b1f`** 5커밋 전진 — `7f10449` G26 연말정산 의료비공제 API(staff+guardian)·`27f20de`/`6bf51c8` CMS debit amount·SUCCEEDED integrity guard·`970f547` CMS/EASY_PAY 제외 필터·`1af5b1f` copayAmount null 수납 거부.
- **대조 결과**: `git diff --name-only ed730a2..HEAD -- src/main/resources/db/migration/` = **빈 목록(0파일)** → round 106 이후 **신규 스키마 변경 0건**. `git diff ed730a2..HEAD -- '**/Repository.java'` = 빈 목록 → **신규 repository 쿼리·`@Query` 0건**. 워크스페이스 submodule 실측 — HEAD `1af5b1f`·branch develop·working tree clean.
- **신규 5 Java 커밋 ↔ 기존 스키마 backing(앱 레이어, DB 이중 방어)**: ① **G26 의료비공제** — `findByOrganizationIdAndClientIdOrderByCreatedAtDesc` → V25 `idx_billing_claim_items_org_client_created` + claim PK lookup; PAID/paidAt/귀속연도/CMS·EASY_PAY 제외는 인메모리 필터 — 신규 인덱스 0건. ② **CMS debit guards** — amount>0·FCMS 금액 일치·SUCCEEDED↔PAID/CMS 정합은 `CmsService` 앱 검증; V59/V50/V60 기존 제약 backing. ③ **copayAmount null** — 앱 가드, DB V4 `>= 0`만(#99 패턴).
- **문서 drift**: G26 엔드포인트·`EASY_PAY` payment_method — API_SPEC 미반영, V50 CHECK에 EASY_PAY 미포함 — PLN/TWR 정렬 권장(DBA 비소유).
- Must billing·attendance·NHIS 핵심 제약 7건 불변. agents.yaml `core_entities` 11종 전수 충족. `ls db/migration | wc -l` = **70개** contiguous(V1–V70).
- **결론**: Must 스코프 **신규 V71 마이그레이션·테이블·인덱스·제약 불필요**. 본 라운드: ERD §7-48·§8 G26 2행 + ERD/DATA_RETENTION 메타 timestamp 갱신 — 스키마 변경 0건. **coder 메모**: develop push 후 `mvn flyway:migrate`·`mvn test` 재검증 권장.

#### #103. paidAt PAID 가드 · 방문 지점 HOME_CARE alias 재대조 — 신규 DDL 0건 (2026-06-11, round 106, backend `ed730a2`)
- **배경**: round 105(`64ebf6e`) → **`ed730a2`** 3커밋 전진 — `894e246` 방문일정 지점 가드 **HOME_CARE alias 수용**·`4001510` 수납 기록 시 **paidAt 필수**·`ed730a2` PAID 전이 전 **paidAt 필수**.
- **대조 결과**: `git diff --name-only 64ebf6e..HEAD -- src/main/resources/db/migration/` = **빈 목록(0파일)** → round 105 이후 **신규 스키마 변경 0건**. `git diff --name-only 64ebf6e..HEAD -- '**/*Repository.java'` = 빈 목록 → **신규 repository 쿼리·`@Query` 0건**. 워크스페이스 submodule 실측 — HEAD `ed730a2`·branch develop·working tree clean.
- **신규 3 Java 커밋 ↔ 기존 스키마 backing(앱 레이어, DB 이중 방어)**: ① **paidAt PAID 가드**(`ed730a2`)·**수납 기록 paidAt 필수**(`4001510`) — `BillingService`가 `CONFIRMED→PAID`·수납 영수증 시 `paid_at` 적재 강제(round 105 payment_method 강제와 짝); DB는 **V50 `chk_billing_claims_paid_requires_metadata`**(PAID → `paid_at`·`payment_method` NOT NULL) + V52 actor backstop과 이중 방어 — 신규 컬럼·제약 불요. ② **방문 지점 HOME_CARE alias**(`894e246`) — `BranchServiceType.BY_CODE`가 입력 alias `HOME_CARE`→`HOME_VISIT` 매핑, `normalizeCode`가 정본 `name()`=`'HOME_VISIT'`로 영속화 → **V51 `chk_branches_service_type`** 불변(alias 입력 전용·DB 미저장). `VisitService` 가드(`isHomeVisitLike`)는 `branches.service_type` 정본 read — 신규 DDL 0건.
- **문서 drift**: REQUIREMENTS §1-2 급여종(`HOME_CARE`/`FACILITY_CARE`) ↔ DB 정본(`HOME_VISIT`/`INTEGRATED_HOME`) 불일치를 `894e246` alias가 입력단 흡수 — PLN/TWR 용어 정렬 권장(DBA 비소유, `FACILITY_CARE`=시설급여 v3 G20 미도입).
- Must billing·attendance·NHIS 핵심 제약 7건 불변. agents.yaml `core_entities` 11종 전수 충족. `ls db/migration | wc -l` = **70개** contiguous(V1–V70, `uniq -d` 빈 출력).
- **결론**: Must 스코프 **신규 V71 마이그레이션·테이블·인덱스·제약 불필요**(rules.md §1·§17) — 3건 모두 기존 V50/V51 제약 위의 앱 레이어 강화. 본 라운드: ERD round 106 검증 기록 + ERD/DATA_RETENTION 메타 timestamp 갱신 — 스키마 변경 0건. **coder 메모**: develop push 후 `mvn flyway:migrate`·`mvn test` 재검증 권장.

#### #102. V70 커밋 확인 · 청구/이동서비스 앱 가드 재대조 — 신규 DDL 0건 (2026-06-10, round 105, backend `64ebf6e`)
- **배경**: round 104(`dd7a580`) → **`64ebf6e`** 5커밋 전진 — `3def542` 보호자 billing DRAFT 숨김·`ba4c9d9` **V70 integrity guards 커밋**(round 104 DBA 산출)·`b5218a9` 이동서비스비 cross-branch UPDATE 거부·`9a97a1c` G7 NHIS import guidance API 복원·`64ebf6e` PAID 알림 전 payment method 강제.
- **대조 결과**: `git diff --name-only dd7a580..HEAD -- src/main/resources/db/migration/` = **V70 1파일**(round 104 산출, coder 커밋) → round 104 이후 **신규 스키마 변경 0건**. `git diff --name-only dd7a580..HEAD -- '*/Repository.java'` = 빈 목록 → **신규 repository 쿼리·`@Query` 0건**.
- **신규 4 Java 커밋 ↔ 기존 스키마 backing(앱 레이어, DB 이중 방어)**: ① 보호자 billing DRAFT 숨김 — `claim.getStatus()` ∈ `{CONFIRMED, PAID}` 인메모리 필터(V31 status 인덱스 재사용). ② 이동서비스비 cross-branch UPDATE 거부 — V70 `trg_transport_service_fee_records_guard_client`(BEFORE UPDATE OF branch_id 지점 일치)와 이중 방어. ③ G7 import guidance — 인메모리 `NhisImportGuidance`, DB 미사용. ④ PAID 전 payment method 강제 — **V50 `chk_billing_claims_paid_requires_metadata`**(PAID → payment_method/paid_at NOT NULL) + `chk_billing_claims_payment_method`(CASH/BANK_TRANSFER) DB 제약과 이중 방어, 신규 컬럼 불요.
- **API_SPEC drift**: G15 outings·G16 fees/vehicles·G7 guidance 엔드포인트 일부 API_SPEC 미반영(실측 컨트롤러 PRESENT) — PLN/TWR 정렬 권장(DBA 비소유).
- Must billing·attendance·NHIS 핵심 제약 7건 불변. agents.yaml `core_entities` 11종 전수 충족. `ls db/migration` = **70개** contiguous.
- **결론**: Must 스코프 **신규 V71 마이그레이션·테이블·인덱스·제약 불필요**(rules.md §1·§17). 본 라운드: ERD round 105 검증 기록 + ERD/DATA_RETENTION 메타 timestamp 갱신 — 스키마 변경 0건. **coder 메모**: develop push 후 `mvn flyway:migrate`·`mvn test` 재검증 권장.

#### #101. V67–V69 G15/G16 coder DDL · V70 integrity 후속 (2026-06-10, round 104, backend `dd7a580`)
- **배경**: round 103(`9d7c17f`) → **`dd7a580`** 4커밋 전진 — coder `7dfcc9e` **V67** `client_outings`(G15 2-1-1/2-9)·`88d4c59` **V68** `transport_service_fee_*`(G16 1일1회)·`bd375e6` **V69** `vehicles`+`transport_runs.vehicle_id`.
- **V67–V69 분석**: Tenant FK·조회 인덱스·fee 1일1회 UK·V68 actor backstop(fee records)은 coder DDL에 포함. V49 meal_records·V65 transport contracts 대비 **8건 누락** 식별.
- **해소 — V70**: ① `client_outings` — `uq_client_outings_org_id`·`(org,branch,client)` FK·`trg_client_outings_set_org_branch`·`guard_active_client`·`set_recorded_by`·purge·`updated_at` CHECK ② `transport_service_fee_records` — org-branch sync·transport client guard·purge·recorded_by backing ③ `vehicles` — actor backstop·recorded_by backing ④ `transport_runs` — `trg_transport_runs_guard_vehicle_branch`.
- **API_SPEC drift**: G15 outings·G16 fees/vehicles 엔드포인트는 **API_SPEC 미반영**(실측 `ClientOutingController`·`TransportController` fee paths·`VehicleController` @ `dd7a580`) — PLN/TWR 정렬 권장(DBA 비소유).
- Must billing·attendance·NHIS 핵심 제약 7건 불변. agents.yaml `core_entities` 11종 전수 충족. `ls db/migration` = **70개** contiguous.
- **coder 메모**: V70 push 후 `mvn flyway:migrate`·`mvn test` 검증. 앱은 이미 actor·scope 검증 — V70은 raw SQL·우회 INSERT 방어.

#### #100. V66 visit_schedules import duplicate slot EXISTS — G21 NHIS re-import guard (2026-06-11, round 103, backend `9d7c17f`)
- **배경**: round 102(`d6d7e7f`) → **`9d7c17f`** 4커밋 전진 — `9aafa3e` **NHIS visit import duplicate skip**(`hasExistingVisitSchedule`·`VisitScheduleRepository.existsBy…PlannedStartTimeAndPlannedEndTimeAndStatusIn`)·`b0a88ac` billing no-op status 앱 거부·`9d7c17f` paired PLAN/BILLING check-in/out sync·`24733c7` transport contract Java guard(V65 DDL은 round 102 산출).
- **신규 누락 1건 식별·V66 해소**: `9aafa3e` EXISTS 쿼리는 org+branch+client+visit_date+schedule_kind+**planned_start_time+planned_end_time**+status IN (DRAFT/CONFIRMED/IN_PROGRESS/COMPLETED) — V57 PLAN blocking(시간 미포함)·V53 목록 인덱스로는 backing 불충분. → **V66** `idx_visit_schedules_org_branch_client_slot_duplicate` partial.
- **DB partial UNIQUE 보류**: 동일 슬롯 중복은 앱에서 skip(IMPORT_SKIPPED)하나, `planned_start_time`/`planned_end_time` NULL 허용(V53 CHECK) + 수기 `POST /visits` 중복 검사 미구현 → race·NULL edge에서 partial UK가 오탐/미탐 가능. **V66은 EXISTS backing만**(V57 패턴). partial UK는 수기 create에도 duplicate guard 추가 확정 후 검토.
- **paired sync·billing no-op**: `9d7c17f` paired UPDATE는 V56/V53 기존 인덱스만 사용 — DDL 0건. `b0a88ac` no-op 거부는 V31 `chk_claim_status_history_distinct_transition`(이력 INSERT)과 앱 레이어 이중 방어.
- Must billing·attendance·NHIS 핵심 제약 7건 불변. agents.yaml `core_entities` 11종 전수 충족. `ls db/migration` = **66개** contiguous.
- **coder 메모**: V66 push 후 `mvn flyway:migrate`·`mvn test` 검증. NHIS import duplicate skip은 앱+인덱스; concurrent INSERT race는 v2에서 partial UK 검토.

#### #99. V64 transport_service_contracts·V65 integrity — G15 계약서 영속화 후속 (2026-06-10, round 102, backend `d6d7e7f`)
- **배경**: round 101(`d5e0e01`) → **`d6d7e7f`** 5커밋 전진 — coder `3c8f9fe`가 **V64** `transport_service_contracts`(US-T05 G15 이동서비스 이용 계약서) + `GET/PUT /transport/contracts/{clientId}` API 추가. `d7475fd` G11 auto surcharge in `generateClaim`·`d6d7e7f` attendance `transportMode` filter는 Java-only.
- **V64 분석**: Tenant 복합 FK 4건·UK `(org, client_id)`·`idx_transport_service_contracts_org_branch` — 전사 V4/V5 규약 충족. 그러나 V47 transport·V33 actor/purge 패턴 대비 **3건 누락** 식별.
- **해소 — V65**: ① `trg_transport_service_contracts_set_recorded_by`(actor backstop) ② `trg_transport_service_contracts_guard_client`(`uses_transport`·활성·지점 일치) ③ 서명 pair CHECK 2건 ④ `idx_transport_service_contracts_client_purge` ⑤ `idx_transport_service_contracts_org_recorded_by` partial.
- **API 경로 drift**: API_SPEC §7 `POST /transport/contracts/{clientId}/signature` → 실측 `GET/PUT /transport/contracts/{clientId}` (`TransportController` @ `3c8f9fe`) — PLN/TWR API_SPEC 정렬 권장(DBA 비소유).
- **G11 auto surcharge**(`d7475fd`): `FeeSurchargeRateCatalog`가 청구 생성 시 일별 금액에 bake-in — `billing_claim_items.total_amount`에 반영, **가산율 스냅샷 컬럼 불요**(§7-45 v2 확정 시 `surcharge_*_snapshot` 검토).
- Must billing·attendance·NHIS 핵심 제약 7건 불변. agents.yaml `core_entities` 11종 전수 충족. `ls db/migration` = **65개** contiguous.
- **coder 메모**: V65 push 후 `mvn flyway:migrate`·`mvn test` 검증. `TransportContractService`는 이미 `setActorUserId`·활성 이용자 검증 — V65는 raw SQL·우회 경로 방어.

#### #98. v2/G11 가산율 catalog·G27 급여한도 seed 재대조 — 신규 DDL 0건, §7-1-b catalog DB 경계 명문화 (2026-06-10, round 101, backend `d5e0e01`)
- **배경**: round 100(`467cd70`) → **`d5e0e01`** 5커밋 전진 — `5fc44ec` G2 SMTP provider 시작 guard·`20bc1be` G27 인지지원등급 월 급여한도 catalog seed·`18ee9b6` 알림 solapi provider enforce·`904072b` **G11 MOHW 가산율 catalog + preview API**·`d5e0e01` G11 preview 테스트 강화. 워크스페이스 submodule 실측 — `git rev-parse --short HEAD` = **`d5e0e01`**·branch **develop**·working tree **clean**.
- **대조 결과**: `git diff --name-only 467cd70..HEAD -- src/main/resources/db/migration/` = **0파일**. `src/main/` 변경 12파일 전부 Java billing/notification 레이어(`FeeSurchargeRateCatalog`·`FeeSurchargeRateCode`·`MonthlyBenefitCapCatalog`·DTO·`BillingController`·`BillingService`·`NotificationConfig`). **신규 repository 쿼리 0건**(`git diff …src/main | rg "Repository\.|@Query|find[A-Z]|count[A-Z]|exists[A-Z]"` = none).
- **§7-1-b `fee_surcharge_rates` 누락 아님 (설계 명문화)**: API_SPEC §7-1-b가 `fee_surcharge_rates`를 테이블명처럼 표기하나, `BillingService.listFeeSurchargeRates`/`previewFeeSurcharge`는 `jwtScopeResolver.requireOrganizationId()` + **인메모리 `FeeSurchargeRateCatalog`**(MOHW 2026 야간20·심야30·휴일30·유급휴일50% 고정값)만 사용 — **물리 테이블 없음**. API_SPEC v1Notice("v1 catalog·가이드만, 청구 자동 가산은 v2")와 정합. `git grep fee_surcharge_rates` = **0건**(코드·마이그레이션). → ERD **§7-45 신설**로 catalog ↔ DB 경계 명문화(향후 v2 청구 자동 가산 확정 시 `fee_surcharge_rates` Tenant catalog + `billing_claim_items.surcharge_*_snapshot` 작성 — V62 `duration_band_snapshot` 패턴).
- **G27 월 급여한도**(`MonthlyBenefitCapCatalog`)·**알림 provider guard**(`NotificationConfig`) — 각각 인메모리 catalog·config 레이어, DB 미사용(round 100 §7-44 재확인).
- **Must 커버리지**: billing·attendance·NHIS 핵심 제약 7건(`uq_claim_branch_month` V1·`uq_billing_claims_org_id` V10·`uq_billing_claim_items_claim_client` V26·`uq_nhis_import_rows_org_id` V37·`chk_billing_claims_amounts_nonneg` V4 외) 물리 재확인 — **전부 불변**. agents.yaml `core_entities` 11종 전수 충족. `ls db/migration` = **63개** contiguous(V1–V63).
- **결론**: Must 스코프 **신규 V64 마이그레이션·테이블·인덱스·제약 불필요**. **본 라운드**: ERD §7-45 신규·§8 가산율 endpoint 2행·round 101 검증 기록 + ERD/DATA_RETENTION 메타 timestamp 갱신 — 스키마 변경 0건. coder는 develop push 후 `mvn flyway:migrate`·`mvn test` 검증 권장.
- 미작성 엔티티(`fee_surcharge_rates` v2 자동 가산·`vehicles`/`transport_service_fee` v1.3-C·`staff_schedules`/`staff_attendance` §3-8) — API_SPEC 계약·v2 단계 확정 전 → **V64+ 보류**(rules.md §1·§17).

#### #97. V63 청구 생성 기준 문서 동기화·US-M03/US-L01 후속 재대조 — 신규 DBA DDL 0건 (2026-06-10, round 100, backend `467cd70`)
- **배경**: round 99(`0854fbd`) 이후 coder가 US-M03·US-L01 후속 4커밋 전진 — `b953662` **`V63__organization_claim_generation_basis.sql`**(`organizations.claim_generation_basis` CHECK)·청구 NHIS import 경로·`e50533f` 은행 입금 엑셀 bulk import·`a92e625` 월별 급여한도 catalog/guard API·`467cd70` guard RBAC/E2E hardening.
- **대조 결과**: `git diff --name-only 0854fbd..467cd70 -- src/main/resources/db/migration/` = **V63 1파일**(coder 소유, DBA 신규 작성 0건). ERD가 V62·`ls 62개`에서 멈춰 있던 **문서 drift**를 본 라운드에서 해소(§4-1·§4-3·§4-6 mermaid·§7 V63 행·§7-44·§8).
- **Must billing·attendance backing 재확인**: ① `claim_generation_basis` — org PK 조회, 인덱스 불필요. ② 전월 가드 — `idx_billing_claims_org_branch_status_year_month`(V50). ③ 출석 기반 생성 — `idx_attendance_billing_days`(V4)·`idx_attendance_billing_client_present`(V26). ④ NHIS import 기반 생성 — `nhis_import_batches`/`nhis_import_rows` V37/V22/V28. ⑤ bank deposit import — `billing_claims` PAID(V50/V52)+`audit_logs` only. ⑥ monthly benefit cap — 인메모리 catalog, DB 0건.
- **앱 전용( DB 미강제)**: `NHIS_IMPORT` 모드에서 import 선행·`MATCHED`/`DISCREPANCY` 행만 집계 — `BillingService.resolveNhisServiceDaysByClient` 책임(PLAN_NOTES #2 반올림 패턴과 동일).
- Must 핵심 제약 7건 불변. agents.yaml `core_entities` 11종 전수 충족. `ls db/migration` = **63개** contiguous.
- **coder 메모**: V63은 이미 `b953662`에 커밋됨 — `OrganizationEntity.claimGenerationBasis`·`BillingSettingsService`와 정합. `mvn flyway:migrate`·`mvn test` 재검증 권장.

#### #96. G2 수납 영수증·노인학대예방 지침 이메일 재대조 — 신규 DDL 0건 (2026-06-10, round 99, backend `0854fbd`)
- **배경**: round 98(`f77a268`) 이후 coder가 G2 알림·수납 후속 5커밋 전진 — `40567a2` 청구 보호자 알림 client 중복 제거·`4109680` copay 입금액 양수 검증·`399bc22` CMS billing RBAC 테스트·`588b8e6` 수납 영수증 payload·`0854fbd` 수납 영수증 notify+`elder-abuse-prevention-guideline` 엔드포인트.
- **대조 결과**: `git diff --name-only f77a268..0854fbd -- src/main/resources/db/migration/` = **0파일**. 신규 기능은 전부 기존 `notifications`·`billing_claims`(V50/V52)·`cms_enrollments`(V59/V60) 경로 재사용.
- **앱 전용 검증( DB 미강제)**: ① copay `request.amount() > 0` — V4 `chk_billing_claims_amounts_nonneg`는 `>= 0`만 보장, PAID 시 양수 입금은 앱·테ster 책임(PLAN_NOTES #2 반올림 패턴과 동일). ② 청구 라인 client 중복 알림 — V26 `(claim_id, client_id)` UK가 데이터 전제, 앱 dedup은 방어적.
- **consent 매핑**: `ELDER_ABUSE_PREVENTION_GUIDELINE` → `notify_daily_care`(`NotificationEventType` @ `0854fbd`) — 별도 DB 컬럼 불요.
- Must billing·attendance·NHIS 핵심 제약 7건 불변. agents.yaml `core_entities` 11종 전수 충족. `ls db/migration` = **62개** contiguous.
- **본 라운드 산출**: ERD §7 round 99 검증 기록·§8 elder-abuse/수납 영수증 매핑·DATA_RETENTION §8 2행 — **V63+ 보류**(미작성 `vehicles`/`staff_schedules` 등).

#### #95. G9 duration_band 청구 라인 스냅샷·유효수가 인덱스 — V62 신규 (2026-06-10, round 97, backend develop)
- **배경**: BNK-39(`425a05f`/`06d68dd`) coder가 **V61** `fee_schedules_duration_band`로 등급 × 이용시간(`duration_band` 5밴드 H3_6~H13_PLUS)을 `fee_schedules`·`clients`에 도입. 본 라운드는 V61 도입 이후 **청구(Must) 후속 누락**을 API_SPEC §7·REQUIREMENTS §3-9-1·`FeeScheduleRepository`·`BillingService.generateClaim`·`BillingClaimItemEntity` 대조로 식별.
- **누락 ① 밴드 스냅샷 부재**: `generateClaim`은 `client.getDurationBand()`로 수가를 해석(`requireEffectiveFeeSchedule`→`findEffectiveForGradeAndBand`)하나, `billing_claim_items`는 `daily_rate_snapshot`/`ltc_grade`/`copay_type`/`copay_rate_snapshot`만 스냅샷하고 **밴드는 저장하지 않음** → V61 다밴드 청구 라인을 원본 `fee_schedules` 행으로 재대조 불가(§3-9-1 "과거 청구는 당시 수가 유지" 위반).
- **누락 ② 유효수가 인덱스 밴드 미정렬**: `findEffectiveForGradeAndBand`(generateClaim 핫패스)는 `(org, ltc_grade, duration_band)` 등치 + `effective_from` 범위·DESC 정렬이나, `idx_fee_schedules_org_grade_effective`(V23)는 `duration_band` 이전 인덱스.
- **해소 — V62**:
  - ① `billing_claim_items.duration_band_snapshot VARCHAR(20)` + `chk_billing_claim_items_duration_band`(V61과 동일 5종) + `trg_billing_claim_items_set_duration_band`(BEFORE INSERT, 밴드 NULL이면 `clients.duration_band`에서 해석 — V32 actor/V48 grade backstop 패턴, `clients.id` PK 조회로 V21 org backstop 순서 무관). **backfill 주의**: V8 `trg_billing_claim_items_lock`이 CONFIRMED/PAID 청구의 라인 UPDATE를 거부하므로 명시 `UPDATE … backfill`은 확정/수납 청구에서 실패 → **`NOT NULL DEFAULT 'H10_13'`(PG11+ 메타데이터 전용 ADD COLUMN, 트리거 미발생) 후 `DROP DEFAULT`**로 우회(DROP 후 생략 INSERT는 NULL→트리거가 정확 밴드 적재). DRAFT 잠금(V8)·org backstop(V21)과 공존.
  - ② `idx_fee_schedules_org_grade_band_effective`(`(org, ltc_grade, duration_band, effective_from DESC)`) 신규 + V23 `idx_fee_schedules_org_grade_effective` DROP(신규가 `(org, ltc_grade)` 접두어로 기존 경로 커버). 목록 인덱스 `idx_fee_schedules_org_list`(V27)는 ORDER BY에 밴드가 없어 **변경 안 함**.
- **coder 구현 메모**: V62 트리거가 밴드를 자동 보존하므로 **앱 변경 없이도 정확**. 다만 명시성·테스트 가독성을 위해 `BillingClaimItemEntity`에 `durationBandSnapshot` 필드(+ `generateClaim`에서 `item.setDurationBandSnapshot(client.getDurationBand())`) 추가를 권장 — 트리거는 `IF NULL`이라 명시 적재와 비간섭. `FeeScheduleResponse`/청구 상세 DTO에 밴드 노출은 PLN/UXD 후속.
- Must billing·attendance·NHIS 핵심 제약 7건 불변. agents.yaml `core_entities` 11종 전수 충족. `ls db/migration` = **62개**(V1–V62 contiguous). ERD §7 마이그레이션 목록표가 V60에서 멈춰 있어 **V61·V62 행 보강**(문서 drift 해소).
- **검증**: 로컬 `ogada` DB는 flyway_history 스키마 drift(개발 환경 이슈)로 전체 `mvn flyway:migrate` 불가 — V62 DDL 자체는 non-destructive(ADD COLUMN nullable→backfill→NOT NULL, CREATE/DROP INDEX). coder는 develop push 후 `mvn flyway:migrate`·`mvn test` 검증 권장.

#### #94. CMS(효성 FCMS) 스켈레톤 Tenant 무결성·FK backing — V60 신규 (2026-06-10, round 96, backend `2c6e57e`)
- 워크스페이스 submodule 실측: `git rev-parse --short HEAD` = **`2c6e57e`** · branch **develop** · working tree **clean**. round 95(`0ebe945`) → **`2c6e57e`** 전진 — billing notify(`84f3441`)·overdue reminder partial index 정합(`c67ff1e`)·overdue 퇴소 이름 유지(`a401537`)·email 채널·**V59 CMS FCMS 스켈레톤**(`2c6e57e`). `db/migration/` 신규는 V59뿐.
- **V59 분석**: `billing_claims.payment_method` CHECK에 `CMS` 추가 + `cms_enrollments`(보호자 자동출금 동의 — `payer_name`·`bank_code`·`account_last4`·`fcms_member_id`·`status`)·`cms_debit_requests`(청구별 출금 요청, `(org, claim_id)` UK). 그러나 **모든 관계 컬럼을 단일컬럼 FK**(`branches(id)`·`clients(id)`·`users(id)`·`billing_claims(id)`·`cms_enrollments(id)`)로만 선언 — 전사 Tenant 무결성 규약(V4 `uq_branches_org_id`·V5 `uq_users_org_id`/`uq_clients_org_id`·V8 `fk_nhis_rows_*_org`·V10 `uq_billing_claims_org_id`·V16 billing_claim_items 복합 FK·V52 payment actor 복합 FK)과 불일치.
- **신규 누락 1건 식별·해소**: 다른 Tenant의 지점/이용자/보호자/청구를 한 Tenant의 CMS 출금(payer_name·bank_code·account_last4 = 금융 준식별 정보)에 연결할 수 있는 cross-tenant 위험. → **V60** ① `uq_cms_enrollments_org_id` 앵커 + ② `cms_enrollments` 복합 Tenant FK 3건(`(org, branch_id)→branches`·`(org, client_id)→clients`·`(org, guardian_user_id)→users`) + ③ `cms_debit_requests` 복합 Tenant FK 2건(`(org, claim_id)→billing_claims`·`(org, enrollment_id)→cms_enrollments`) + ④ FK backing 인덱스 3건(`idx_cms_enrollments_org_branch`·`_org_guardian`·`idx_cms_debit_requests_org_enrollment`, V56 컨벤션 — 좌선두 backed `(org, client_id)`·`(org, claim_id)`는 재인덱스 안 함). V59 단일 FK는 V8 패턴대로 유지, 모든 스코프 컬럼 NOT NULL → MATCH SIMPLE = 완전 매치·backfill 불필요.
- **보존 정책**: DATA_RETENTION §3에 CMS 동의(동의 해지·퇴소 후 5년, `account_last4`만 최소 수집)·출금 요청(청구 연도 5년, `failure_reason`은 사용자 안내 사유만) 2행 추가 + §8 구현 메모 1행.
- Must billing·attendance·NHIS 핵심 제약 7건 불변. agents.yaml `core_entities` 11종 전수 충족. `ls db/migration` = **60개**(V1–V60 contiguous).
- **coder 영향 없음**: 앱은 항상 동일 org로 INSERT → 신규 FK 항상 충족, repository 시그니처·DTO 변경 0건 — V60은 raw SQL·버그 경로의 cross-tenant 적재 방어 + FK validation/조회 성능. Flyway migrate 미실행(로컬 PG drift) — coder는 V60 push 후 `mvn flyway:migrate` 검증 권장.
- 미작성 엔티티(`vehicles`/`transport_service_fee` v1.3-C·`staff_schedules`/`staff_attendance` §3-8) — API_SPEC 계약 미작성 → **V61+ 보류**(rules.md §1·§17).

#### #93. notifications billing reminder claim lookup — V58 신규 (2026-06-10, round 95, backend `0ebe945`)
- 워크스페이스 submodule 실측: `git rev-parse --short HEAD` = **`0ebe945`** · branch **develop** · working tree **clean**. round 94(`3e4d3e6`) → **`0ebe945`** 5커밋 전진 — V57 coder 커밋(`469d08c`)·overdue pagination+guardian context(`4ee652d`)·NHIS parser(`7fbd219`)·overdue/visit 테스트(`09932ef`/`0ebe945`).
- **신규 repository 쿼리 1건**: `NotificationRepository.findLatestBillingReminderAtByClaimIds`(native — `organization_id`+`template_code='BILLING_STATEMENT'`+`payload->>'claimId' IN`+DISTINCT ON claimId+`COALESCE(sent_at, created_at) DESC`) — `BillingService.loadLastBillingReminderAt`이 `GET /billing/overdue` 페이지마다 호출(`4ee652d`). V46 `idx_notifications_org_recipient_created`는 recipient-history 전용 — claimId equality·reminder 시각 정렬 backing 없음.
- **신규 누락 1건 해소**: **V58** — `idx_notifications_org_template_claim_reminder` partial (`(org, template_code, payload->>'claimId', COALESCE(sent_at, created_at) DESC) WHERE payload ? 'claimId'`).
- Must billing·attendance·NHIS 핵심 제약 7건 불변. `ls db/migration` = **58개** contiguous. agents.yaml `core_entities` 11종 전수 충족.
- **coder 영향 없음**: `NotificationRepository`·`BillingService` 시그니처 변경 없음 — V58은 overdue 목록 reminder 집계 성능 방어. `mvn flyway:migrate` 검증 권장.

#### #92. visit_schedules NHIS import 확정 PLAN EXISTS 인덱스 — V57 신규 (2026-06-10, round 94, backend `3e4d3e6`)
- 워크스페이스 submodule 실측: `git rev-parse --short HEAD` = **`3e4d3e6`** · branch **develop** · working tree **clean**. round 93(`ee3fa3a`) → **`3e4d3e6`** 7커밋 전진 — V56 coder 커밋(`adec560`)·paired cancel/sync(`b63bb1f`/`3e4d3e6`)·NHIS import 확정 PLAN 차단+`notify`(`84f3441`)·auth change-password(`fe5b38b`).
- **신규 repository 쿼리 1건**: `VisitScheduleRepository.existsByOrganizationIdAndBranchIdAndClientIdAndVisitDateAndScheduleKindAndStatusIn` — `VisitService.hasBlockingConfirmedPlan`이 NHIS import(`POST /visits/imports/nhis`) 행마다 호출(`84f3441`). V53 인덱스는 목록/기간 조회용 — 5열 equality EXISTS에 전용 backing 없음.
- **신규 누락 1건 해소**: **V57** — `idx_visit_schedules_org_branch_client_plan_blocking` partial (`(org, branch, client_id, visit_date) WHERE schedule_kind='PLAN' AND status IN (CONFIRMED, IN_PROGRESS, COMPLETED)`).
- paired sync/cancel·`findByIdAndOrganizationId(pairedScheduleId)` — V56 `idx_visit_schedules_org_paired`·`uq_visit_schedules_org_id` backed. `POST /billing/claims/{id}/notify` — `notifications`+V46/V45 기존 경로. Must billing·attendance·NHIS 핵심 제약 7건 불변. `ls db/migration` = **57개** contiguous.
- **coder 영향 없음**: `VisitService`·repository 시그니처 변경 없음 — V57은 EXISTS 성능·import 대량 행 스캔 방어. `mvn flyway:migrate` 검증 권장.

#### #91. visit_schedules FK backing 인덱스 — V56 신규 (2026-06-09, round 93, backend `ee3fa3a`)
- 워크스페이스 submodule 실측: `git rev-parse --short HEAD` = **`ee3fa3a`** · branch **develop**. round 92(`dd49204`) → **`ee3fa3a`** 5커밋 전진 — V55(`83fe308`)·meals/programs POST·clients enrich·visits HOME_VISIT 제한·NHIS 방문일정 import(`ee3fa3a`).
- **V53/V55 대조**: V55(`83fe308` 커밋 완료)가 퇴소 가드·actor backstop을 보완했으나, V53 `visit_schedules`의 관계 컬럼 **`paired_schedule_id`(self-FK)·`assigned_user_id`(users FK)** 에 backing 인덱스가 없음 — V47 transport_run_stops·V29 billing_claim_items 컨벤션과 불일치.
- **신규 누락 1건 해소**: **V56** — `idx_visit_schedules_org_paired`(partial, PLAN↔BILLING 페어·self-FK 검증) + `idx_visit_schedules_org_assigned_date`(partial, 배정 요양보호사 일정).
- **coder 영향 없음**: `VisitScheduleRepository` 기존 3쿼리는 V53 인덱스 backed. V56은 FK validation·향후 페어/배정 조회 최적화. `POST /visits`·`POST /visits/imports/nhis`의 `createPairedBillingSchedule` 흐름과 정합.
- `ls db/migration` = **56개**(V1–V56 contiguous). Must billing·attendance·NHIS 핵심 제약 7건 불변. agents.yaml `core_entities` 11종 전수 충족.
- **V56은 develop untracked** — coder는 V56 커밋·push 후 `mvn flyway:migrate` 검증. 로컬 `ogada` DB flyway_history V46·스키마 drift로 전체 migrate 불가(개발 환경 이슈, V56 DDL 자체는 non-destructive).
- 미작성 엔티티(`billing_payments` #74-1·`vehicles`/`transport_service_fee` v1.3-C·`staff_schedules`/`staff_attendance` §3-8) — API_SPEC 계약 미작성 → **V57+ 보류**.

#### #90. 진행 중 coder meals/guardian 쿼리 대조 — 신규 누락 0건 (2026-06-09, round 90, backend `dd49204`)
- 워크스페이스 submodule 실측: `git rev-parse --short HEAD` = **`dd49204`** · branch **develop** — round 89과 **커밋 HEAD 동일**. round 89 산출 **V55가 여전히 untracked**(develop 미커밋, coder push 대기). 작업트리에 coder 진행 중(미커밋) meals·programs·visits 변경 + untracked `CreateMealMenuRequest`·`CreateProgramScheduleRequest` — DBA 비소유(Java 레이어).
- **신규 repository 쿼리 2건 backing 대조**:
  - `GuardianClientRepository.findByOrganizationIdAndClientIdInAndPrimaryGuardianTrue(org, clientIds)` → **`idx_guardian_clients_org_client_primary`**(V31, partial `(organization_id, client_id) WHERE is_primary = TRUE`) — org + `client_id IN` + `is_primary=true` 정확 backing. 신규 인덱스 불필요.
  - `MealMenuRepository.findByOrganizationIdAndBranchIdAndMenuDateAndMealType(org, branch, date, type)` → **`uq_meal_menus_org_branch_date_type`**(V49 UNIQUE) — 단건 exact-match backing. 신규 인덱스 불필요.
- Must billing·attendance·NHIS 핵심 제약 7건 `rg -l` 물리 재확인 — **전부 불변, Must 신규 누락 0건**. `ls db/migration` = **55개** contiguous(1..55 갭·중복 0). agents.yaml `core_entities` 11종 전수 충족.
- 미작성 엔티티(`billing_payments` #74-1·`vehicles`/`transport_service_fee` v1.3-C·`staff_schedules`/`staff_attendance` §3-8) — API_SPEC 계약 미작성 → **V56+ 보류**(rules.md §1·§17).
- **coder 영향 없음**: 진행 중 쿼리 2건 모두 기존 인덱스 backed. **본 라운드**: ERD §7 검증 기록 + ERD·DATA_RETENTION 메타 timestamp 갱신만 — 스키마·신규 마이그레이션 없음. coder는 V55 커밋·push 후 `mvn flyway:migrate` 검증.

#### #89. visit_schedules 퇴소 가드·actor backstop — V55 신규 (2026-06-09, round 89, backend `dd49204`)
- 워크스페이스 submodule 실측: `git rev-parse --short HEAD` = **`dd49204`** · branch **develop** · working tree **clean**. round 88(`4cc328d`) → **`dd49204`** 1커밋 전진 — Region API·NHIS fixture **테스트만**, `db/migration/` 변경 0건.
- **V53 대조**: coder `d768820`이 `visit_schedules` 테이블·복합 Tenant FK·상태 CHECK·4 인덱스를 완결했으나, 동일 프로젝트의 V10(출석)·V49(식사)·V47(배차 actor) 패턴 대비 **① `trg_*_guard_active_client` INSERT 가드·② session-actor backstop** 누락. `VisitService.requireClientInScope(write=true)`는 지점 스코프만 검증하고 `clients.is_active`/`discharged_at`은 검사하지 않음.
- **신규 누락 1건 해소**: **V55** — `trg_visit_schedules_guard_active_client`(INSERT only, V10 대칭) + `trg_visit_schedules_set_actors`(`created_by`/`confirmed_by`/`cancelled_by`, V47 `trg_transport_runs_set_actors` 대칭).
- **coder 영향 없음**: `VisitService`가 이미 actor를 entity에 설정·`DbSessionContext.setActorUserId` 호출 — V55는 raw SQL·미래 앱 경로 방어. 퇴소 후 신규 일정만 INSERT 거부(기존 행 체크인/아웃 UPDATE 허용).
- **문서 보강**: ERD §4-1 V51 `region_*`·`branches.service_type`/`branch_code` mermaid(문서만, DDL은 V51 기존).
- `ls db/migration` = **55개**(V1–V54 + DBA V55). Must billing·attendance·NHIS 핵심 제약 7건 불변. Flyway migrate 미실행 — coder는 V55 push 후 `mvn flyway:migrate` 검증.

#### #85. V50 수납 메타 actor 무결성 보강 — V52 신규 (2026-06-09, round 85, backend `598d108`)
- 워크스페이스 submodule 실측: `git rev-parse HEAD` = **`598d1086`** · branch **develop**. round 84(`32575aa`) → **`598d108`** 1커밋 전진(`feat(v2): add copay payment recording, overdue list, and guardian billing API`). working tree에 coder 미커밋 작업(`ClientRepository`·`ActivityProgramRepository` 쿼리 리팩터·`regions/` 패키지·branch_profile DTO + untracked **`V51__admin_regions_and_branch_profile.sql`**) 존재 — billing DDL과 무관, DBA 비소유·미접촉.
- **V50 분석**(`598d108` 커밋): `billing_claims`에 `paid_at`·`payment_method`(`CASH|BANK_TRANSFER` CHECK)·`payment_recorded_by` 추가 + `chk_billing_claims_paid_requires_metadata`(PAID → paid_at·payment_method 필수) + 미납 목록 인덱스 `idx_billing_claims_org_branch_status_year_month`. 신규 쿼리 `findBy…StatusAndYearMonthLessThanOrderByYearMonthAsc`(US-L02 overdue) ↔ V50 인덱스 정확 매핑. **V50 자체는 정합**.
- **신규 누락 1건 식별·해소**: V50의 `payment_recorded_by UUID`가 스키마의 다른 모든 actor 컬럼(`created_by`/`recorded_by`/`generated_by`/`imported_by`)과 달리 **① 복합 Tenant FK(V14 패턴)·② session-actor backstop(V32/V33/V35/V47 패턴) 모두 부재** → cross-tenant actor 적재 가능 race·raw SQL 경로 무방비. → **V52** 작성:
  - `fk_billing_claims_payment_recorded_by_org` `(organization_id, payment_recorded_by) → users(organization_id, id)` (MATCH SIMPLE → DRAFT/CONFIRMED NULL 행 skip, V50 신규 NULL 컬럼 backfill 불필요; users(org, id) UK = `uq_users_org_id` V5).
  - `trg_billing_claims_set_payment_recorded_by` — `status='PAID'` 전이 시 `ogada.actor_user_id` backstop(V47 transport `confirmed_by` UPDATE-path 패턴). V8 immutability 트리거는 amounts/scope만 잠그므로 `payment_recorded_by` 적재와 무충돌.
- **버전 충돌 처리**: coder가 동시 작업 중인 untracked **V51(admin_regions/branch_profile)**이 V51을 선점 → 본 billing 후속을 **V52**로 배정(rules.md §11 타 작업 미간섭). 충돌 회피 외 admin_regions 마이그레이션은 미접촉.
- **coder 영향 없음**: `BillingService.recordCopayPayment`이 이미 `jwtScopeResolver.requireActorUserId()`(동일 Tenant)를 `setPaymentRecordedBy`로 적재 — V52 FK·트리거를 기존 흐름이 항상 충족. coder 리팩터(client 검색 trigram·activity_programs `(org, branch, schedule_date)` V49)는 동일 컬럼 재사용 → 신규 인덱스 불필요.
- `ls db/migration` = **52개**(V1–V50 + coder V51 + DBA V52), 버전번호 1..52 갭·중복 0. Must billing·attendance·NHIS 핵심 제약 7건 불변. agents.yaml `core_entities` 11종 전수 충족. Flyway migrate 미실행(로컬 PG 인증) — coder는 V50·V51·V52 push 후 `mvn flyway:migrate` 검증 권장.
- 미작성 엔티티(`billing_payments` 복수 부분입금 #74-1 — V50은 단일 컬럼 접근으로 MVP·v2 충족·`vehicles`/`transport_service_fee` v1.3-C·`staff_schedules`/`staff_attendance` §3-8) — API_SPEC 계약 미작성 → **V53+ 보류**(rules.md §1·§17).
- **본 라운드**: **V52 신규 마이그레이션** + ERD §4-6(mermaid·V50/V52 bullet)·§7(마이그레이션표 V50/V51/V52·검증 기록)·§8(수납·미납 API 2행)·DATA_RETENTION §8(actor·수납 메모) + 메타 timestamp 갱신.

#### #74-1 갱신 (2026-06-09, round 85): 본인부담 수납 — **V50/V52로 해소**
- round 74-1에서 「설계 가설 ① `billing_payments` 자식 테이블 또는 ② `billing_claims` 단일 컬럼」으로 보류했던 항목이 **②안(`billing_claims.paid_at`·`payment_method`·`payment_recorded_by`)으로 coder 구현·V50 마이그레이션**되며 확정. 복수 부분입금은 v2 범위에서 단일 수납으로 단순화 — 부분입금·복수 입금 요건이 추후 확정되면 `billing_payments` 자식 테이블로 확장(V50 컬럼은 마지막 수납 요약으로 유지 가능). actor 무결성은 V52에서 보강.

#### #84. Transport 마스킹 단위테스트 커밋 — 스키마 변경 없음 (2026-06-09, round 84, backend `32575aa`)
- 워크스페이스 submodule 실측: `git rev-parse --short HEAD` = **`32575aa`** · branch **develop** · working tree **clean**(`git status --porcelain` 빈 출력). round 83(`c7941e9`) 이후 1커밋 전진.
- `git diff --name-only c7941e9..32575aa` = **`TransportServiceTest.java` 단일 파일**(transport pickup 마스킹 단위테스트, SEC-D9/TSR 98·99차). `-- src/main/resources/db/migration/` 필터 시 **0파일** → **두 커밋 간 스키마 동일**. 컨트롤러·서비스·DTO·DDL 변경 0건 — 마스킹 로직은 round 82/83에서 이미 추가된 V47 기존 컬럼(`clients.pickup_address_encrypted`·`pickup_contact_encrypted` BYTEA) read-side 처리.
- `ls db/migration` = **49개** contiguous(1..49 갭·중복 0). Must billing·attendance·NHIS 핵심 제약 7건 SQL 줄번호 물리 재확인 — **Must 신규 누락 0건**. agents.yaml `core_entities` 11종 전부 충족(`medications`=`health_records.record_type` polymorphic·`guardians`=`guardian_clients`+`guardian_invitations` V43·`meal_records`/`activity_programs` V49).
- 30개 `*Repository` ↔ V1–V49 인덱스·UK 대조 불변 — 본 커밋은 신규 쿼리·repository 미추가(테스트 전용).
- 미작성 엔티티(`billing_payments` #74-1·`vehicles`/`transport_service_fee` v1.3-C·`staff_schedules`/`staff_attendance` §3-8) — API_SPEC 계약 미작성 → **V50+ 보류**(rules.md §1·§17).
- **본 라운드**: ERD §7 round 84 검증 기록 + ERD·DATA_RETENTION 메타 timestamp 갱신만 — 스키마·신규 마이그레이션 없음. **coder 영향 없음**.

#### #83. Transport pickup 연락처/주소 마스킹 (SEC-D9) — 스키마 변경 없음 (2026-06-09, round 83, backend `c7941e9`)
- 워크스페이스 submodule 실측: `git rev-parse --short HEAD` = **`c7941e9`**(`feat(transport): mask pickup contact for non-hq views`) · branch **develop** · working tree **clean**. round 80 산문(`1ec538b`) 이후 3커밋 전진(`f8d1b02` E2E/RBAC → `e7d4cf6` 주소 마스킹 → `c7941e9` 연락처 마스킹) — 셋 다 **`db/migration/` 변경 0건**.
- round 81·82·83 모두 transport **read-side 마스킹/E2E**: roster·run·stop 응답에서 `pickup_address`·`pickup_contact`를 `hq_admin`/`platform_admin`/`sysadmin`만 전체 노출, 그 외 역할 마스킹(REQUIREMENTS §3-13-7). 마스킹 원천은 **V47 기존 컬럼** `clients.pickup_address_encrypted`·`pickup_contact_encrypted`(BYTEA) — 신규 테이블·컬럼·인덱스·제약·트리거 불필요.
- `ls db/migration` = **49개** contiguous(1..49 갭·중복 0). Must billing·attendance·NHIS 핵심 제약 7건 SQL 물리 재확인 — **Must 신규 누락 0건**. agents.yaml `core_entities` 11종 전부 충족(`medications`=`health_records.record_type` polymorphic·`guardians`=`guardian_clients`+`guardian_invitations` V43·`meal_records`/`activity_programs` V49).
- 28개 `*Repository` ↔ V1–V49 인덱스·UK 대조 불변 — transport 마스킹은 신규 쿼리 미추가(기존 V47 `findByTransportRunIdOrderByStopOrderAsc`→`idx_transport_run_stops_run_order` 등 재사용).
- 미작성 엔티티(`billing_payments` #74-1·`vehicles`/`transport_service_fee` v1.3-C·`staff_schedules`/`staff_attendance` §3-8) — API_SPEC 계약 미작성 → **V50+ 보류**(rules.md §1·§17).
- **본 라운드**: ERD §7 round 83 검증 기록 + ERD·DATA_RETENTION 메타 timestamp 갱신만 — 스키마·신규 마이그레이션 없음. **coder 영향 없음**.

#### #80. US-T01 Clients transport profile API — 스키마 변경 없음 (2026-06-08, round 80, backend `1ec538b`)
- round 79(`767d977`) → **`1ec538b`** 1커밋 전진 — `ClientResponse`·`CreateClientRequest`·`UpdateClientRequest`·`ClientService`에 V47 transport 컬럼 DTO 노출(US-T01). **`db/migration/` 0건**, working tree clean.
- ERD §4–§8·API_SPEC §5(출석)·§7(청구)·§13(식사/프로그램)·Clients transport profile·DATA_RETENTION §3–§4·Flyway V1–V49 **전수 재대조**.
- Must 핵심 제약 7건 SQL `rg` 물리 재확인 — **Must 신규 누락 0건**. `ls db/migration` = **49개** contiguous.
- agents.yaml `core_entities` 11종 전부 충족 — transport profile은 `clients` 테이블(V47) 기존 컬럼 매핑.
- 30 repository ↔ V47/V49 인덱스·UK 1:1 대조 — **신규 누락 인덱스/제약 0건**.
- 미작성 엔티티(`billing_payments` #74-1·`vehicles`/`transport_service_fee`·`staff_schedules`/`staff_attendance`) — API_SPEC 미작성 → **V50+ 보류**.
- **본 라운드**: ERD §7 round 80·§8 Clients 매핑 + ERD·DATA_RETENTION 메타 timestamp 갱신만 — 스키마·신규 마이그레이션 없음.

#### #79. Must billing·attendance·core_entities 재대조 — 신규 누락 0건 (2026-06-08, round 79, backend `767d977`)
- round 78(`767d977`) 이후 **backend HEAD·`db/migration/` 변화 없음** — working tree clean.
- ERD §4–§8·API_SPEC §5(출석)·§7(청구)·§13(식사/프로그램)·DATA_RETENTION §3–§4·Flyway V1–V49 **전수 재대조**.
- Must 핵심 제약 7건 SQL `rg` 물리 재확인 — **Must 신규 누락 0건**. `ls db/migration` = **49개** contiguous.
- agents.yaml `core_entities` 11종 전부 충족 — `medications`는 `health_records.record_type='medication'` polymorphic; `meal_records`·`activity_programs`는 V49.
- 30 repository ↔ V47/V49 인덱스·UK 1:1 대조 — round 78 결과 재현, **신규 누락 인덱스/제약 0건**.
- 미작성 엔티티(`billing_payments` #74-1·`vehicles`/`transport_service_fee`·`staff_schedules`/`staff_attendance`) — API_SPEC 미작성 → **V50+ 보류**.
- **본 라운드**: ERD §7 round 79 검증 기록 + ERD·DATA_RETENTION 메타 timestamp 갱신만 — 스키마·신규 마이그레이션 없음.

#### #78. V49 기준 전수 재대조 — 신규 누락 0건 (2026-06-08, round 78, backend `767d977`)
- backend HEAD가 round 77(`0d8968d`) → **`767d977`**로 1커밋 전진(`fix(v1.3-A): align transport unconfirm route with PATCH contract`). `git diff --name-only` = `TransportController.java` + 라우팅 테스트 2건 — **`db/migration/` 0건**, working tree clean.
- 신규 도메인 repository(transport·meals·programs 6개) 쿼리 메서드를 **직접 정독**하고 V47/V49 인덱스·UK와 1:1 물리 대조 — **신규 누락 인덱스/제약 0건**.
  - `TransportRunRepository`(3)→`uq_transport_runs_org_id`·`uq_transport_runs_org_branch_date_direction`(V47); `TransportRunStopRepository`(3)→`idx_transport_run_stops_run_order`(V47).
  - `MealMenuRepository`(1)·`MealRecordRepository`(2)→`idx_meal_menus_org_branch_date`·`uq_meal_records_client_date_type`(V49).
  - `ActivityProgramRepository`(2)·`ProgramParticipationRepository`(2)→`idx_activity_programs_org_branch_date`·`uq_activity_programs_org_id`·`uq_program_participations_client_program_date`(V49).
- Must billing·attendance·NHIS 핵심 제약 7건 SQL `rg` 줄번호 물리 재확인 — **Must 신규 누락 0건**. `ls db/migration` = **49개** contiguous(1..49 갭·중복 0). agents.yaml `core_entities` 11종 전부 충족.
- 미작성 엔티티(`billing_payments` Epic L #74-1·`vehicles`/`transport_service_fee` v1.3-C·`staff_schedules`/`staff_attendance` §3-8)는 API_SPEC 미작성 → **V50+ 보류**(rules.md §1).
- **본 라운드**: ERD §7 round 78 검증 기록 + ERD·DATA_RETENTION 메타 timestamp 갱신만 — 스키마·신규 마이그레이션 없음.

#### #74-1. 본인부담 부분입금 스키마 (Epic L, US-L01/L02)

| 항목 | 현황 | 결정 대기 |
|------|------|-----------|
| MVP | `billing_claims.status` DRAFT→CONFIRMED→PAID + `billing_claim_status_history` | TSR 82 PAID 알림 연동 완료 |
| v1.2 P0 | 입금일·금액·수단(현금/계좌)·부분입금 | API_SPEC 엔드포인트 **미작성** |
| 설계 가설 | ① `billing_payments` 자식 테이블(복수 입금) 또는 ② `billing_claims`에 `paid_at`/`payment_method` 단일 컬럼 | 부분입금 허용 여부·미납 집계 규칙 확정 후 **V50** |

### 추가 질문

다음 항목이 확정되기 전까지 상세 스펙·일정·구현 범위는 가정으로만 기재한다.

#### [PLN] G-STAFF-ANNUAL-SCHEDULE — 직원 연간일정계획 (2026-06-21, 185차 — BNK-478 · **신규 candidate · 「가정」 P3**)

- **근거**: 케어포 PDF p.99 **8-3 연간일정계획** — 기념일·월별 업무일지·개인/요양원 일정 카테고리·달력 출력 · **프로그램권한「요양원 일정 관리」** 필요.
- **현황**: ogada `/staff` cluster ✅ · **연간일정 전용 Route ❌** · demo `view.schedule_manage` L08_M12 미대응.
- **검토 질문**: MVP 범위 포함 여부 — **planner 권고(추측·미확인)**: **P3 backlog·v3 Must 후보·MVP out-of-scope**.

#### [PLN] G-STAFF-WORK-ATTENDANCE — 직원 출퇴근·근무일지 (2026-06-21, 185차 — BNK-478 · **신규 candidate · 「가정」 P3 deepen**)

- **근거**: 케어포 PDF p.100 **8-4 출퇴근 및 근무일지** — 전체 직원 일자별 일괄입력·근무일지·**PC/NFC/모바일** 구분표시 · **프로그램권한「근태 관리[근무일지]」**.
- **현황**: ogada 수급자 `/attendance` ✅ superset · **직원 출퇴근 Route ❌** · US-R01 v3 Must 잔여.
- **검토 질문**: NFC/mobile 채널 MVP 포함 여부 — **planner 권고(추측·미확인)**: **P3 deepen·US-R01 v3 Must 연계·MVP out-of-scope**.

#### [PLN] G-STAFF-WORK-SCHEDULE-NHIS-EXCEL — 직원 근무일정 NHIS 엑셀 (2026-06-21, 185차 — BNK-478 · **P3 carry**)

- **근거**: 케어포 PDF p.101 **8-5 근무일정** — 공단 연동 엑셀 import workflow (BNK-323 G-STAFF-WORKLOG cluster carry).
- **현황**: ogada `G-STAFF-NHIS-EXCEL-IMPORT` 요보사 등록 ✅ · **근무일정 NHIS 엑셀 ❌**.
- **검토 질문**: US-R01·G-STAFF-WORKLOG P3 cluster와 통합 여부 — **planner 권고(추측·미확인)**: **P3 backlog·MVP out-of-scope**.

#### [PLN] G-BATHING-SCHEDULE-PREV-MONTH-COPY — 목욕일정 전월 일괄생성 (2026-06-21, 184차 — BNK-466 · **✅ full-stack closure @ `9a957fb`/`a426663`**)

- **근거**: 케어포 PDF p.45 module3 **3-3 목욕일정** — 「**전월 일정 불러 일괄생성**」.
- **현황**: **✅ closure** — BE API @ `49a1721`/`a426663` · FE `BathingSchedulesPage` wire @ `9a957fb`.
- **검토 질문**: 추가 Must 승격 불요 — **planner 권고**: **✅ closure·183차 P2 candidate 제거**.

#### [PLN] G-STAFF-DOCUMENT-REPOSITORY — 직원 인사서류 21-slot repository (2026-06-21, 184차 — BNK-470~471 · **✅ full-stack closure @ `03d0d43`/`fd15a2f`/`b583c11`**)

- **근거**: 케어포 PDF p.96 zone③ 20-doc + ezCare FAQ21825 lifecycle — ogada **21-slot superset**.
- **현황**: **✅ closure** — FE panel + API wire + BE repository-progress API + RBAC tests.
- **검토 질문**: **mobile upload P3 carry** — 현장 촬영·모바일 첨부 workflow · MVP out-of-scope.

#### [PLN] G-MENU-PERMISSION-MATRIX — 계정×메뉴 fine-grained 권한 (2026-06-21, 184차 — BNK-471 · **신규 candidate · 「가정」 P3**)

- **근거**: ezCare [**FAQ21695**](https://ezcare.easyms.co.kr/help/faq.ez?rowid=21695&type=web) — 계정별 financial 메뉴 partial deny toggle.
- **현황**: ogada 7-role JWT RBAC only · **per-account×per-menu matrix ❌**.
- **검토 질문**: MVP 범위 포함 여부 — **planner 권고(추측·미확인)**: **P3 backlog·v3 enterprise·MVP out-of-scope**.

#### [PLN] G30 — 자가진단↔현장 점수 비교 페이지 (2026-06-21, 184차 — BNK-471 · FAQ21692 · **P3 carry**)

- **근거**: ezCare FAQ21692 — 2024 모니터링 9번 「직전 6개월 매월 자가진단」 vs 현장 점수 **비교 페이지**.
- **현황**: ogada G30 self-diagnosis+integrated checklist ✅ · **dedicated score comparison page ❌**.
- **검토 질문**: MVP 범위 포함 여부 — **planner 권고(추측·미확인)**: **P3 backlog·MVP out-of-scope**.

#### [PLN] G-BATHING-SCHEDULE-PREV-MONTH-COPY — 목욕일정 전월 일괄생성 (2026-06-20, 179차 — BNK-441 · **신규 candidate · 「가정」 P3**)

- **근거**: 케어포 PDF p.45 module3 **3-3 목욕일정** — 「**전월 일정 불러 일괄생성**」 vs ogada `/care/bathing-schedules` CRUD only.
- **현황**: ogada bathing schedule CRUD ✅ · **전월 bulk copy ❌**.
- **검토 질문**: MVP 범위 포함 여부 — **planner 권고(추측·미확인)**: **P3 backlog·MVP out-of-scope·평가 backfill 후속**.

#### [PLN] G-ORAL-CARE-PERIOD-REPORT — 구강관리 1/2/3개월 리포트 (2026-06-20, 179차 — BNK-441 · **신규 candidate · 「가정」 P3**)

- **근거**: 케어포 PDF p.45 module3 **3-4 구강관리일지** — **1/2/3개월** period report template vs ogada `/nursing/oral-care-checks` CRUD only.
- **현황**: ogada oral care checks CRUD ✅ · **multi-period report template ❌**.
- **검토 질문**: dedicated period report vs existing `/care/reports/*` cluster reuse — **planner 권고(추측·미확인)**: **P3 backlog·Must 승격 보류**.

#### [PLN] G-STAFF-NHIS-EXCEL-IMPORT — 요양보호사 NHIS 엑셀 일괄등록 (2026-06-21, 180차 — BNK-444 · **✅ full-stack closure @ `4315ee2`/`2f6f3bc`**)

- **근거**: 케어포 PDF p.95 **8-1-2 공단연동** — FE `StaffNhisCaregiverImportPanel` + BE preview/import API full-stack @ `4315ee2`/`2f6f3bc`.
- **현황**: **✅ closure** — `/staff` 패널 + 6-status Badge + row selection normalize.
- **검토 질문**: 추가 Must 승격 불요 — **planner 권고**: **✅ closure·P3 carry only**(NHIS import UX polish).

#### [PLN] G-BANK-EXCEL-8 — 은행 8종 일괄입금 엑셀 (2026-06-21, 180차 — BNK-445~446 · **✅ full-stack closure @ `a18b30e`/`e3b74a0`+`7d29a38` pending**)

- **근거**: 케어포 PDF p.88 — BE 8-bank catalog+preview+import @ `e3b74a0` · FE `BankDepositImportPanel` @ `a18b30e` · BE hardening `@7d29a38`(merge pending QA-B182).
- **검토 질문**: MVP 범위 포함 여부 — **planner 권고(추측·미확인)**: **✅ closure·BE merge(1) QA-B182 선행**.

#### [PLN] G-STAFF-LEAVE-STATUS — 직원 휴직(ON_LEAVE) lifecycle 상태 (2026-06-21, 182차 — BNK-452 · **✅ full-stack closure @ `2581347`/`1d7cee2`/`5f1815f`** · QA-B187/B188 Fixed)

- **근거**: ezCare [FAQ 21720](https://ezcare.easyms.co.kr/help/faq.ez?rowid=21720&type=web) 「입사·퇴사·**휴직** 등 상태변경」 — BNK-452 **FE+summary API wire로 ✅ closure** · TSR 1192~1193차 merge EXECUTED.
- **현황**: **✅ closure** — `STAFF_LIFECYCLE_STATUS.ON_LEAVE` + CHECK `V166` · `StaffLifecyclePanel` 휴직 Badge · `onLeaveCount` summary API · ON_LEAVE→ACTIVE 복직 regression.
- **검토 질문**: 추가 Must 승격 불요 — **planner 권고**: **✅ closure·P3 candidate 제거·merge 게이트 only 잔여 없음(QA-B187/B188 Fixed)**.

#### [PLN] G-STAFF-LEAVE-STATUS — 직원 휴직(ON_LEAVE) lifecycle 상태 (2026-06-21, 181차 — BNK-452 · **✅ full-stack closure @ `2581347`/`1d7cee2`** · 180차 P3 candidate 제거)

- **근거**: ezCare [FAQ 21720](https://ezcare.easyms.co.kr/help/faq.ez?rowid=21720&type=web) 「입사·퇴사·**휴직** 등 상태변경」 — BNK-446 ON_LEAVE enum 갭 → BNK-452 **FE+summary API wire로 ✅ closure**.
- **현황**: **✅ closure** — `STAFF_LIFECYCLE_STATUS.ON_LEAVE` + CHECK `V166` · `StaffLifecyclePanel` 「휴직」 combobox+warning Badge · `StaffLifecycleSummaryPanel`+`GET /api/v1/staff/lifecycle-summary` `onLeaveCount` · ON_LEAVE `active=false`·hiredAt 필수 · ON_LEAVE→ACTIVE 복직 regression.
- **검토 질문**: 추가 Must 승격 불요 — **planner 권고**: **✅ closure·P3 candidate 제거**(BE/FE merge pending 2 = QA-B187/B188 transfer 게이트만 잔여).

#### [PLN] G-COMM-CALLER-AUTH — 문자 발신번호 본인인증 관리 (2026-06-21, 181차 — BNK-452 · **신규 candidate · 「가정」 P3**)

- **근거**: silverangel [notice 221562](https://www.silverangel.kr/silverangel/support/notice/view.do?pageNo=1&Tmp_idx=221562) 「미인증 휴대전화 발신번호 삭제 예정안내」 — `부가서비스 > 문자발신번호관리` 메뉴에서 **본인인증 마감 2026-06-23 17:00**·미인증 번호 **18:00 일괄 삭제**(선행 공지 221551 시리즈 2차).
- **현황**: ogada SMS는 9-event 알림 발송만 ✅ · **발신번호 self-verification/관리 workflow ❌**.
- **검토 질문**: 발신번호 본인인증·관리 화면 MVP 범위 포함 여부 — **planner 권고(추측·미확인)**: **P3 backlog·MVP out-of-scope**. 경쟁사 마감(6/23)은 compliance 인텔로만 기록하고 **urgency↑이나 자체 SMS 발송 벤더 정책 확정 전까지 P3 유지**.

#### [PLN] G-BILLING-DEPOSIT-HALFMONTH-REPORT — 입금대장 반월 split (2026-06-21, 182차 — BNK-455~457 · **✅ full-stack closure @ `e38ccfd`/`375fb9d`/`b96d038`** · 180차 P3 candidate 제거)

- **근거**: 케어포 PDF p.91 ② — `BillingReportPage` `period=FULL|FIRST_HALF|SECOND_HALF` + BE filter @ `b96d038`/`375fb9d`.
- **현황**: **✅ closure** — `/billing/reports/deposits` 반월 variant + `appliedFilters.depositPeriodLabel` server echo.
- **검토 질문**: 추가 Must 승격 불요 — **planner 권고**: **✅ closure·P3 candidate 제거**.

#### [PLN] G-BILLING-RECEIPT-DUAL-BASIS — 수납대장 청구/수납 2-track (2026-06-21, 182차 — BNK-455~457 · **✅ full-stack closure @ `e38ccfd`/`375fb9d`/`b96d038`** · 180차 P3 carry 제거)

- **근거**: 케어포 PDF p.91 ③ — `basis=PAYMENT|CLAIM` + `appliedFilters.receiptBasisLabel` @ `c6a412f`/`14935a3`.
- **현황**: **✅ closure** — `/billing/reports/receipts` 청구/수납 2-track full-stack.
- **검토 질문**: MVP 범위 포함 여부 — **planner 권고**: **✅ closure·P3 candidate 제거**.

#### [PLN] G-BILLING-APPLIED-FILTERS-WIRE — billing report appliedFilters FE wire (2026-06-21, 182차 — BNK-456~457 · **✅ full-stack closure @ `c6a412f`/`14935a3`** · BNK-456 P3「가정」 제거)

- **근거**: 케어포 PDF p.91 인쇄 헤더 server-side metadata — BE echo @ `14935a3` → FE wire @ `c6a412f` `billingReportFilters.js` server label 우선.
- **현황**: **✅ closure** — print scope label server `appliedFilters.*Label` 우선.
- **검토 질문**: optional FE wire → **planner 권고**: **✅ closure·P3 candidate 제거**.

#### [PLN] G-BILLING-DEPOSIT-HALFMONTH-REPORT — 입금대장 반월 split (2026-06-21, 180차 — BNK-445 · **superseded by 182차 ✅ closure**)

- **근거**: 케어포 PDF p.91 ② — 월간 + **1~15일** + **16~말일** 입금대장 vs ogada `/billing/reports/deposits` 월 1종 only.
- **검토 질문**: dedicated report variant vs existing deposits report filter — **planner 권고(추측·미확인)**: **P3 backlog·Must 승격 보류**.

#### [PLN] G-BILLING-RECEIPT-DUAL-BASIS — 수납대장 청구/수납 2-track (2026-06-21, 180차 — BNK-445 · **P3 carry · 「가정」**)

- **근거**: 케어포 PDF p.91 ③ — 청구기준·수납기준 구분 vs ogada `receipts` 단일 variant.
- **검토 질문**: MVP 범위 포함 여부 — **planner 권고(추측·미확인)**: **P3 carry·Must 승격 보류**.

#### [PLN] G-STAFF-NHIS-EXCEL-IMPORT — 요양보호사 NHIS 엑셀 일괄등록 (2026-06-20, 179차 — BNK-440 · **superseded by 180차 ✅ full-stack closure**)

- **근거**: 케어포 PDF p.95 **8-1-2 공단연동** — 공단 엑셀 다운로드 → 일괄등록 vs ogada BE `@6f7f145` preview+import API ✅ · FE `/staff` import panel ❌.
- **현황**: BE `StaffNhisCaregiverImportController` ✅ · FE manual CRUD only.
- **검토 질문**: FE import panel wire를 v1.2.1 Must로 승격할지 — **planner 권고(추측·미확인)**: **P2 backlog·FE wire 후 closure 검토**.

#### [PLN] G-BILLING-PRIOR-DEPOSIT-GUARD — 청구 전 선행 입금 가드 (2026-06-20, 178차 — BNK-433/436 · **✅ closure @ BNK-436**)

- **근거**: 케어포 PDF p.85 「**7-1 청구 전 7-2 선행 입금**」 — BNK-436 dashboard widget+API full-stack closure @ `0d233b9`/`07a03c0`.
- **현황**: ogada G28 prior-deposit guard·G33 settlement API ✅ · **dashboard due-gate widget ✅ closure**.
- **검토 질문**: billing confirm 전 deposit completeness gate 추가 범위 — **planner 권고(추측·미확인)**: **✅ closure·추가 Must 승격 불요**.

#### [PLN] G-BANK-EXCEL-8 — 은행 8종 일괄입금 엑셀 (2026-06-20, 179차 — BNK-440 · **superseded by 180차 ✅ closure**)

- **근거**: 케어포 PDF p.88 — **은행 8종 일괄입금 엑셀** · BE `@6f7f145`/`07a85a3` 8-bank catalog+preview+import API ✅ · FE bank deposit import modal ❌.
- **검토 질문**: MVP 범위에 bank-specific bulk import FE wire 포함 여부 — **planner 권고(추측·미확인)**: **P2 backlog·FE wire 후 closure 검토**(178차 P3에서 승격).

#### [PLN] G24 총평(종합소견) 전용 필드 — FAQ21800 parity 잔여 (2026-06-20, 178차 — BNK-434 · **P3 carry · △ partial**)

- **근거**: BNK-434 — FAQ21800 8/8 item parity ✅ · **총평 전용 필드**는 ogada `homeVisitNotes`로 △ 커버.
- **검토 질문**: dedicated `overallOpinion` 필드 분리 vs notes reuse — **planner 권고(추측·미확인)**: **P3 carry·Must 승격 보류**.

#### [PLN] G15-KAKAO-QUOTA-DASH — Kakao REST API quota/usage 대시보드 위젯 (2026-06-20, 177차 — BNK-429 · **신규 candidate · 「가정」 P3 · BE ✅ @ `80b9619` · FE widget ❌**)

- **근거**: BNK-429 — ogada BE `@80b9619` `KakaoRestApiUsageTracker`·`TransportKakaoQuotaUsageResponse` ✅(QA-B169 Fixed) · 케어포 postcode 1-layer only(quota/status **부재**).
- **현황**: BE tracker ✅ · FE `TransportKakaoApiStatusPanel` @ `ba74bb5` = API status/route preview 가시화 ✅ · **quota dashboard widget ❌**.
- **검토 질문**: ① FE quota widget wire를 v1.3-A Must로 승격할지 ② HQ admin 대시보드 vs transport settings 전용 패널 중 IA — **planner 권고(추측·미확인)**: **P3 backlog·FE widget wire 후 P2 승격 검토**.

#### [PLN] G-PROVIDER-CHANGE-COUNSEL — 급여제공직원 변경 상담일지 (2026-06-20, 174차 — BNK-410 · **신규 candidate · 「가정」 P3 · 재가 out-of-scope**)

- **근거**: 이지케어 [FAQ 21795](https://ezcare.easyms.co.kr/help/faq.ez?rowid=21795&type=web) — 「**급여제공직원 변경 14일 이내 상담 + 상담일지**」·「**오전/오후 2명 요양보호사 이중 일정**(동일 수급자·시간대 분리)」.
- **현황**: ogada `/staff/grievance-counselings` = 직원 **고충** 상담 only → 급여제공직원 변경 상담일지 **❌** · 이중 일정은 `/visits` 다중 방문 **△ parity**.
- **검토 질문**: 재가 방문요양 평가지표 성격 — 주야간보호 MVP **out-of-scope** 여부 — **planner 권고(추측·미확정)**: **P3 backlog·Must 승격 보류**.

#### [PLN] silverangel feeService 공개 요금표 — 로그인 선행 여부 (2026-06-19, 171차 — BNK-391 · **미확인 carry**)

- **근거**: [silverangel feeService.do](https://www.silverangel.kr/newSilverangel/service/feeService.do) — CMS·본인부담금 자동출금 마케팅 verbatim·**공개 요금표 숫자 0**(시설코드 로그인 선행·가격 역추출 **미확인**).
- **검토 질문**: ogada B2B SaaS 요금 정책 벤치마크에 silverangel 공개 페이지를 포함할지 — **planner 권고(추측·미확인)**: **P3 reference only**.

#### [PLN] longterm 610 `refreshedException` — 수가 페이지 재실측 (2026-06-19, 171차 — BNK-391 · **미확인 carry**)

- **근거**: [longterm 610](https://www.longtermcare.or.kr/npbs/e/b/610/npeb610m01.web?menuId=npe0000002751) **422B `refreshedException`**(209~210차 carry).
- **검토 질문**: BNK rotation 시 610 재실측 주기 — **planner 권고**: V103 seed authoritative·610은 **반기 1회 수동 cross-walk**.

#### [PLN] G39 상태변화 기록지 — 주1회 7일 due-date 알림 · RFID 특이사항→별지 동치 라벨링 (2026-06-19, 170차 — BNK-384 · **신규 candidate · 「가정」 P3 · 입력 폼 ✅·알림/라벨링 △**)

- **근거**: 이지케어 [FAQ 21817](https://ezcare.easyms.co.kr/help/faq.ez?rowid=21817&type=web) — 상태변화 기록지(요양보호사) **주1회 이상·7일 이내** 작성(시행규칙 별지 서식)·**RFID 특이사항란 = 별지 동치 인정**·모바일 작성·서명·평가지표 = 이지케어 3-FAQ 트리니티(21816 주간 4단 + 21817 상태변화 주1회 + 21818 RFID 월간 5단).
- **현황**: ogada `CareServiceWeeklyRecordPage`(`/care/weekly-service-records`)+`CareServiceSpecialNotesPage`(`/care/service-special-notes`) 7-필드(`stateChangeNotes`·`specialNotes`·`physicalCareNotes`·`cognitiveActivityNotes`·`mealAssistanceNotes`·`nursingNotes`·`programParticipationNotes`) **입력 ✅ 7/7 parity** · **7일 due-date 자동 알림 △**(미작성 경과 알림 ❌) · **RFID 특이사항란 → 공단 전송 별지 동치 라벨링 △**.
- **검토 질문**: ① v2/v3 기록 cluster에 **상태변화 기록 7일 미작성 due-date 알림**(주1회 SLA 경고)을 포함할지 ② RFID 특이사항 데이터를 **별지 서식 동치로 라벨링/전송**할지 — **planner 권고(추측·미확정)**: **P3 backlog 등재·Must 승격 보류**(입력 full-stack 우위 이미 확보·알림/라벨링은 운영 편의·MVP 범위 밖).

#### [PLN] G15 이동서비스 수칙 보호자 제공(②) — silverangel 평가지표 vs ogada 계약 흐름 (2026-06-18, 168차 — BNK-375 · **△ partial · P2 Should carry**)

- **근거**: silverangel essential [daycareEssentialWork.do](https://www.silverangel.kr/newSilverangel/daycare/daycareEssentialWork.do) 평가지표 ② 「이동서비스 수칙을 수급자(보호자)에게 제공함」— 계약서 첨부·이동서비스수칙 포함 점검.
- **현황**: ogada G15 **별지 제22호 실데이터 일지 input+print+export 3축 full-stack ✅**(BNK-355~361·375) · 계약/동의 흐름 carry · **수칙 PDF/첨부 제공 이력 UI △**.
- **검토 질문**: ① v1.3-C transport compliance에 **수칙 제공 확인(②) 체크리스트**를 추가할지 ② 계약서 첨부만으로 충분한지 — **planner 권고(추측·미확정)**: **P2 Should carry**(평가 정적 점검 parity·Must 승격 보류·실데이터 일지 우위는 이미 확보).

#### [PLN] 신규직원 건강검진 1년 이내 서류 자동검증 (2026-06-18, 163차 — BNK-339 · **△ partial @ `8e6310a`**)

- **근거**: 이지케어 [FAQ 21799](https://ezcare.easyms.co.kr/help/faq.ez?rowid=21799&type=web) — 신규직원은 급여개시일까지 **결핵 포함 1년 이내** 건강검진 결과통보서 필요.
- **현황**: FE `@8e6310a` `feat(v1.2.1/staff): add new-hire health checkup document window validation` = **StaffLifecyclePanel ⑥ 연동·1년 window 자동 판정 △ partial** · `/staff/health-checkups` 연간 관리 ✅ · **전용 파일함 스캔 보관 UI △**.
- **검토 질문**: ① 입사 전 서류 **스캔→직원 파일함** 워크플로를 v2 US-R03에 포함할지 — **planner 권고(추측·미확정)**: **P2 deepen**(자동검증 partial closure 후 파일함 UX).

#### [PLN] silverangel 정본 URL 경로 — `/service/` vs `/daycare/daycareEssentialWork.do` (2026-06-19, 169차 — BNK-379 · **방법론 갱신 · 기능 갭 아님**)

- **관측**: BNK-379 — silverangel CMS URLs **`/daycare/`→404** · canonical = **`/service/`** path(예: `/service/mainService.do`). BNK-334(162차)에서 `/daycare/daycareEssentialWork.do`가 정본이었으나, 169차 BNK-379에서 CMS 경로 재확인.
- **planner 권고(추측·미확정)**: 벤치마크 rotation 시 **BNK-380 snapshots + `/service/` prefix 우선** · `/daycare/*` 경로 추측 금지 · on-disk md5 zero drift(202차)가 최종 정본.

#### [PLN] silverangel 정본 URL 경로 — `/service/essential.do` vs `/daycare/daycareEssentialWork.do` (2026-06-18, 162차 — BNK-334 · **방법론 자체 번복 · 기능 갭 아님** · **169차 BNK-379로 supersede**)

- **관측**: BNK-334 초기 `/service/essential.do` probe가 404를 반환했으나, 정본은 `/daycare/daycareEssentialWork.do`(`c79c1be3` **200 zero drift**)임을 재확인.
- **planner 권고(추측·미확정)**: 벤치마크 rotation 시 **README·snapshots 인용 URL 우선**·`/service/*` 경로 추측 금지.

#### [PLN] G-STAFF-WORKLOG — 전 직종 출퇴근부/근무일지 (2026-06-17, 161차 — BNK-323 · **신규 갭 candidate · 「 가정」 P3 · MVP out-of-scope 추정**)

- **근거**: 이지케어 [FAQ 21705](https://ezcare.easyms.co.kr/help/faq.ez?rowid=21705&type=web) — 메뉴 **1.직원 > 1.8 직원 출퇴근부/근무일지**·달력 일자별 작성·결재라인·빈서식 출력·현지조사 evidence.
- **현황**: ogada **`LeadCaregiverWorkLogPage`**(선임 요보사 한정)만 · 전 직종 출퇴근부+근무일지 캘린더 **`/staff/work-logs` Route 0건**.
- **검토 질문**: ① v2 직원관리 cluster에 **전 직종 근무일지**를 포함할지 ② 선임 요보사 일지만 유지할지 — **planner 권고(추측·미확정)**: **P3 backlog·Must 승격 보류**(운영 편의·현지조사 evidence이나 MVP 범위 밖).

#### [PLN] G-HOSPITAL-ESCORT — 장기요양 병원동행 시범 (2026-06-17, 161차 — BNK-322 · **신규 갭 candidate · 「 가정」 P3 · MVP out-of-scope 추정**)

- **근거**: [angelsitter #781](https://angelsitter.co.kr/board.view.php?board=bbs3&no=781) — 통합재 가기관(주·야간보호형 참여 가능)·이동 보조·병원 내 수속·진료 동행·약 수령·2026-07-30 개시.
- **현황**: ogada transport **`MEDICAL_FACILITY` stop_kind** partial · **동반 활동 로그(수속/대기/진료/약수령) 및 별도 수 가 3축 ❌**.
- **검토 질문**: ① v2 통합재 가 연계 시 **병원동행 시범** Epic을 transport 확장으로 포함할지 ② MVP transport만 유지할지 — **planner 권고(추측·미확정)**: **P3 backlog·2026-07-30 시범 개시 후 재검토**.

#### [PLN] G-CHANGE-REASON-AUDIT — 범용 필드 변경이력 조회 그리드 (2026-06-18, 167차 — BNK-362 · **신규 갭 candidate · 「가정」 P3 · MVP out-of-scope 추정**)

- **근거**: 이지케어 데모 `change-list` PGID(2.수급자 ▶ 변경사유 조회)·`grid_change_reason` colModel(`chg_what`·`chg_before`·`chg_after`·`mName`·`memo`·`sDate`) = 임의 변경항목의 **변경전/변경후/작성자**를 단일 그리드로 field-level diff 조회.
- **현황**: ogada `AuditLogPanel`은 **action·actor만 표시**하고 before/after 값 미노출 · `ltcGradeChangeReason` 등 **특정 필드만** 사유 기록 → 범용 field-level diff 그리드 **❌**.
- **검토 질문**: ① v2/v3 감사 cluster에 **범용 필드 변경이력 그리드**(엔티티·필드·변경전/후·작성자·시각)를 포함할지 ② action-level audit + 개별 reason 필드만 유지할지 — **planner 권고(추측·미확정)**: **P3 backlog 등재·Must 승격 보류**(현지조사 evidence 가치 있으나 범용 diff 인프라 비용·MVP 범위 밖).

#### [PLN] G-SCHEDULE-FIX-LTM-COMPARE — 청구 확정 전 공단 명세서 사전 비교 (2026-06-18, 165차 — BNK-354 · **167차 status change: P3 candidate → BE closure ✅** @ `03a052a`/`8a8c5b3`)

- **근거**: 이지케어 `schedule-fix` PGID — 일정 확정 전 **「공단 청구명세서와 비교하기」** 체크박스(`chk-ltm-fix`)·방문요양 청구 reconcile workflow.
- **167차 status change(BNK-366~367)**: ogada BE에서 **`GET /visits/nhis-comparison`으로 closure** — matched/discrepancy/missing/extra 4종 라인 분류 + per-client `visitDayCount`↔`nhisServiceDays` + 동일 월 guard + `VisitConfirmReadinessResponse.nhisComparisonSummary` readiness embed(별도 round-trip 제거) + `nhisComparisonAcknowledged` batch ack guard. ezCare 단순 checkbox 대비 **능동 reconcile 우위 설계**. **P3 candidate → BE ✅ status change**.
- **잔여 검토 질문**: ① FE `VisitBatchConfirmPanel`에 `nhisComparisonSummary` matched/discrepancy/missing/extra StatCard wire를 **P2**로 진행할지(BE `8a8c5b3` 설계 의도 = 별도 `fetchVisitNhisComparisonApi` 호출 불필요) — **planner 권고(추측·미확정)**: **P2 carry**(BE closure 후속 FE polish).

#### [PLN] G-CASH-RECEIPT — 본인부담금 현금영수증 발급 (2026-06-18, 160차 — BNK-315 · **신규 갭 candidate · 「가정」 P3 · MVP out-of-scope 추정** · **165차 deepen: `receipt-list` PGID**)

- **근거**: 이지케어 [FAQ 21700](https://ezcare.easyms.co.kr/help/faq.ez?rowid=21700&type=web) — 「본인부담금 수납등록과 **동시에 현금영수증 발급**」·전용 `[본인부담금 현금영수증]` 메뉴·**연락처 기반 발급번호**·발급 취소=수납 내역 삭제·발행내역 조회.
- **현황**: ogada billing 클러스터 = 청구·수납등록(현금/카드/CMS·G2b easy-pay) ✅ · **현금영수증(국세청) 발급·취소·발행내역 연동 ❌**(`현금영수증`/`cashReceipt`/`cash_receipt` grep **0건**).
- **검토 질문**: ① 주야간 본인부담 현금/카드 수납의 **세무 현금영수증 발급**을 v2/v3 범위에 포함할지(국세청 현금영수증 API·홈택스 연동 필요), ② 수납등록만 유지하고 현금영수증은 외부 POS/세무로 위임할지 — **planner 권고(추측·미확정)**: **P3 backlog 등재·Must 승격 보류**(주야간 본인부담 세무 연동은 실재 수요이나 MVP 범위 밖·국세청 연동 비용 검토 필요).
- **미확인**: 실제 발급 화면 세부 필드(로그인 필요)는 BNK-315 기준 **미확인**. **BNK-323 deepen**: FAQ21702/21701 — 수납 연동·2.10 발급목록·취소=수납삭제 cross-confirm(여전히 grep 0건).

#### [PLN] 이동서비스 일지④ full 입력 서식 — Must vs P2 범위 (2026-06-18, 164차 — BNK-347 · **부분 확정**)

- **근거**: NHIS #44 ④ 일지 작성·보관 의무 · BNK-343~347 **partial+++ closure** — legal fields client+server validation @ `b4644e8`/`ac1d43f` · compliance 법정 가이드 @ `0df6902` · **driver signature full-stack** @ `f51e365`/V154 · audit trail full-stack @ `3cc5a08`.
- **164차 확정(기획)**: core 입력·저장·검증·서명·audit = **Must 충족** · 잔여 **P2 Must** = **차량운행표 인쇄 레이아웃 + 별지 제22호 전 항목**(BNK-347).
- **미확정**: 인쇄 시 **공단 제출용 PDF vs 브라우저 인쇄** 포맷 우선순위 — planner 권고(추측·미확정): 별지 제22호 **필드 전수 매핑 우선**·PDF 템플릿은 2차.

#### [PLN] G21 RFID — schedule-rfid 7-code diff matrix vs 하드웨어 RFID (2026-06-18, 164차 — BNK-346 · **미확정**)

- **근거**: 이지케어 `schedule-rfid` colModel **`comp_01`~`comp_09`** 7-code diff matrix · Channel.io plan-billing-diff.
- **현황**: ogada G21 plan/claim UI·청구반영 배지 ✅ · **RFID reconciliation UI ❌** · 하드웨어 RFID(NFC/리더) 연동 **v3.1 Won't carry**.
- **검토 질문**: ① v2 P1은 **소프트웨어 diff matrix UI만**(스케줄 대조·수동 보정)인지 ② 하드웨어 RFID 실연동을 포함할지 — **planner 권고(추측·미확정)**: **7-code diff matrix = P1 소프트웨어 only** · hardware RFID = **v3.1+ Won't**.

#### [PLN] live E2E operation 승격 게이트 정책 (2026-06-18, 159차 — QA-B121+QA-B95 · **미확정**)

- **근거**: TSR 931차 — live E2E SKIP→partial RUN 진전(4 FAIL/108 PASS) · QA-B121 FE merge BLOCK · 결정 73은 merge 선행 조건에서 live E2E 제외.
- **검토 질문**: operation 승격을 **full live E2E PASS hard gate**로 유지할지, 또는 unit+merge 게이트만으로 승격하고 live E2E는 **post-merge smoke(비차단)** 로 강등할지 — planner/운영 결정 대기(추측을 확정으로 승격하지 않음).

#### [PLN] G-COGNITIVE-WORKSHEET(=G29) — 인지활동지 출력 콘텐츠 (2026-06-18, 156차 — BNK-297 · **신규 갭 candidate · 「가정」 P3 · MVP out-of-scope**)

- **근거**: 이지케어 [FAQ 21781](https://ezcare.easyms.co.kr/help/faq.ez?rowid=21781&type=web) — 「인지맞춤형 학습지·낱장 출력·**시범 서비스**·하반기 확장 예정」.
- **현황**: ogada **G17b** = skipReason·참여 기록만 · **학습지/워크시트 콘텐츠 제공 ❌** · 기존 **G29** v3.1 P3 backlog와 동일 Epic(N)·US-T06 연계.
- **검토 질문**: ① 콘텐츠 **제작·배포·PDF 출력**을 v3.1 범위에 포함할지, ② ogada는 **참여 기록만 유지**하고 콘텐츠는 외부(인쇄업체·교재)로 위임할지 — 이지케어도 미성숙(시범)이므로 **planner 권고(추측·미확정)**: v3.1 **P3 candidate 유지·Must 승격 보류**.

#### [PLN] 이지링크(EzLink) 대비 web-first 공단 import 차별화 (2026-06-18, 156차 — BNK-297 · **확정 가정 강화 · 마케팅/온보딩 문서 후보**)

- **근거**: FAQ21764 — 이지케어 「공단자료 조회 프로그램」→ **이지링크** PC 클라이언트(구 smartaib4pc) 설치 필수.
- **ogada 포지션(가정)**: **별도 PC 에이전트 없이** web SaaS + **공단 엑셀 import** 워크플로 = 차별화 keystone · 공단 import **견고성**이 product quality 핵심.
- **미확정**: 마케팅 카피·USER_MANUAL·FAQ에 「이지링크 불필요」를 **명시 노출**할지 — 사용자/운영 결정 대기(추측을 확정으로 승격하지 않음).

#### [PLN] develop working tree 재오염 동시 3건(QA-B115/B116/B117) — 구조적 프로세스 정체 에스컬레이션 (2026-06-17, 155차 — **★ 156차 부분 해소 · 인프라 게이트 결정 대기**)

- **156차 갱신**: TSR 887~897 — **QA-B115/B117/B118 Fixed** · develop **양쪽 WT CLEAN** · merge gate **FULLY UNBLOCKED(364)** · 잔여 = **QA-B116 merge pending** + **QA-B95 operation**.
- **155차 관측**: TSR 886차 기준 **FE develop WT DIRTY 20M+1U(QA-B115)·test 1 FAIL(QA-B116)·BE develop WT DIRTY 5M(QA-B117)** 동시 발생 — 단일 사이클 dirty-tree BLOCK이 **3건 동시**로 확대. 전부 **기능 갭 아님**(QA-B07/B110/B112/B114 lineage·이관 규율 5·6·7 미준수).
- **신규 위험**: QA-B116은 COD가 develop WT에서 `MealAssistanceRecordPage.test.jsx`를 수정했으나 **미커밋·`npm test` 미실행 상태로 Fixed 주장**(false Fixed·이관 규율 5·6) → test 브랜치 regression 지속. 커밋 전 `npm test` 게이트 누락이 반복.
- **영향**: cross-stream merge **BLOCK**(351 pending·336 BE + 15 FE) · operation 승격 잔여 = QA-B115/B116/B117 + QA-B95.
- **미확정(인프라·#36 계열)**: 동일 dirty-tree·false-Fixed 패턴이 다수 사이클 반복(B101/B103/B110/B112/B114/B115/B117) — **`run_agent.py build` 종료 시 ① WT clean 게이트 ② 커밋 전 `npm test`/`mvn test` 통과 게이트 강제** 도입 여부 결정 권고(인프라 영역·coder/ops·planner/사용자 결정 대기·추측을 확정으로 승격하지 않음).

#### [PLN] transport 법정 이동서비스 일지④ 입력 서식 — v1.3-C Must closure 후보 (2026-06-18, 157차 — BNK-300~302 · **158차 BNK-306로 audit trail 부분 해소 · 잔여 미확정**)

- **근거**: NHIS #44 고시 제34조 5항 verbatim — 이동서비스비 산정 조건에 「**④ 이동서비스 일지를 작성하여 보관**」 의무 명시(joHistory `c886ff1f`). 엔젤 essential 지표41(차량운행표)·지표42(시간 준수)와 **3-source cross-walk** 성립.
- **157차 상태 변경**: BNK-300 GET export → **BNK-302 PUT persistence+FE 편집 폼 closure live**(`aaaeb10` BE `PUT /transport/runs/{runId}/service-log` + FE `TransportServiceLogPanel` @ `7a4b310`). **v1.3-C Must 승격 종결 후보** — 155차 「export-only vs 입력 폼」 질문은 **입력·저장+export 경로로 부분 해소**.
- **158차 갱신**: BNK-306 **audit trail read API** @ `5994d15` = 감사 trail **BE closure live** · **159차 갱신**: BNK-307 **audit trail FE wire** @ `3cc5a08` = **full-stack closure live** · 잔여 = **인쇄·보관 UX**.
- **잔여 P2(미확정)**: ① **인쇄·보관 UX**(별지 서식 PDF/인쇄 레이아웃·보관 기간 안내) ② **이동서비스 일지④ full 입력 서식** — `TransportCompliancePage` guide level vs 별지 전용 폼 범위.
- **planner 권고(추측·미확정)**: core 입력·저장·export·BE audit read는 closure 후보이므로 **v1.3-C Must로 승격**, FE audit UI·인쇄·보관은 **P2 잔여**가 최소 범위로 적합할 것으로 보이나 사용자 확정 전 가정으로만 기재.

#### [PLN] 케어포 func 2-9 외출리포트 ↔ ogada `ClientOutingReportPage` 정합 (2026-06-18, 159차 — BNK-307~310 · **✅ verification closure**)

- **근거**: 케어포 func.php 「**2-9.수급자 외출 리포트**」 leaf — ogada `ClientOutingReportPage`·`ClientOutingsPage`·V67 @ `a0dcfc0`/`7dfcc9e` + **live E2E harness** `clientOutingReportLiveApi.e2e.test.js` @ `3a0110f`(BNK-307~310).
- **159차 상태 변경**: 158차 P2 미확정 → **verification closure live** — 필드 매핑·route IA·live API harness 입증. **신규 갭 0**.
- **잔여**: 없음(func 2-9 cluster). 상위 P2 = **이동서비스 일지④ full 입력 서식**.

#### [PLN] transport 법정 이동서비스 일지④ 입력 서식 — P2→v1.3-C Must 승격 검토 (2026-06-17, 155차 — BNK-291 · **157차 BNK-302로 부분 해소**)

- **근거**: NHIS #44 고시 제34조 5항 verbatim — 이동서비스비 산정 조건에 「**④ 이동서비스 일지를 작성하여 보관**」 의무 명시(joHistory `c886ff1f`). 엔젤 essential 지표41(차량운행표)·지표42(시간 준수)와 **3-source cross-walk** 성립.
- **현황**: ogada `TransportCompliancePage`(G15 수칙 가이드)·`/transport/runs/*`(운행기록)·V103 seed·G26 ③ 이동서비스비 통계는 ✅이나, **법정 일지 전용 입력·출력(서식) 폼은 P2 backlog**.
- **검토 질문**: ① 「④ 일지 작성·보관」을 2026 평가 hard 요건으로 보고 **v1.3-C Must로 승격**할지, ② 기존 운행기록(run/stop) 데이터로 **일지 export만 추가**(별지 서식 PDF)하면 충분한지 — 산출물 범위(입력 폼 신규 vs export-only) 결정 필요.
- **planner 권고(추측·미확정)**: run/stop 데이터가 이미 존재하므로 **export-only(별지 서식)부터 v1.3-C Must, 전용 입력 폼은 P2 유지**가 최소 범위로 적합할 것으로 보이나, 사용자 확정 전 가정으로만 기재.

#### [PLN] 케어포 3-product line·dual-source numbering (2026-06-17, 153차 — BNK-285 · **확정 가정**)

- **3-product line**: 케어포는 단일 product가 아니라 **주야간(`daycare/func.php`)·시설급여(`intro_si/func.php`)·방문급여(`intro_visit/func.php`)** 3 product line SaaS. 주야간 = 시설 module 구조 + **module 2「이동서비스관리」삽입**.
- **dual-source numbering**: 동일 module 번호라도 product line마다 leaf 의미가 다름 — **시설 2-4 = 신체제재 기록**(demo-work `view.care_sanction` 정본)·**주야간 2-4 = 차량관리**. demo-work 시설 셸은 `intro_si` 콘텐츠 표시.
- **ogada 매핑 정책**: L02/L03 deepen(V131 body_restraint·V134 care_service_weekly·V123 nursing 등)은 **시설급여(`intro_si`) 평가지표 코어 차용** — 주야간 `daycare/func.php`만으로 cross-walk 시 numbering 충돌 위험.
- **planner 조치**: REQUIREMENTS §1-5 cross-walk 표에 「공식 정본 = `intro_si/func.php`(시설)·주야간 정본 = `daycare/func.php`·dual-source 주의」 명시.
- **다음 BNK rotation 권고**: 시설 module 9「기초설정」leaf ↔ ogada US-O 운영설정 cluster 매핑 deepen.

#### [PLN] v2/live-e2e 통합검증 — bootstrap HTTP 500 + guardian credentials 미설정 (2026-06-17, 152차 — QA-B95 · **Planned · operation 승격 단일 블로커**)

- **152차 신규 관측**: COD가 `liveGlobalSetup` bootstrap fallback(`/api/v1/system/live-e2e/bootstrap` staff token 자동발급)을 적용하고 QA_FEEDBACK `## Fixed`에 기록(단위 테스트 24/24 PASS)했으나, **tester TSR 850~862 `npm run test:live-e2e`는 여전히 47 suites SKIP/137 skipped** — **false Fixed(이관 규율 5)**.
- **신규 증상 2종**: ① **`live-e2e bootstrap HTTP 500`** — staff credential 부재 시 fallback token 자동발급 엔드포인트가 500 반환(부트스트랩 자체 실패) ② **guardian credentials 미설정** — `scripts/dev-live-e2e.env` PRESENT·backend@8080 UP/200이지만 GUARDIAN_* 자격 부재로 guardian live suite skip.
- **영향**: 기능/merge 게이트와 **독립**(merge 330 FULLY UNBLOCKED) · **operation 승격 단일 블로커**(QA-B95 only) · 코드/운영 영역(coder+ops).
- **152차 planner 가정·수동 해소**: ① COD가 live-e2e bootstrap 컨트롤러 500 원인 수정(staff 자동 부트스트랩 token 발급 정상화) ② guardian credentials 주입(env GUARDIAN_* 또는 guardian bootstrap) ③ `./scripts/run-live-e2e.sh` 실행 → suites 실제 RUN(SKIP→PASS) 확인 → tester 재검증.
- **미확정(planner 결정 대기)**: live E2E를 **operation 승격 hard gate로 유지**할지, 또는 환경/부트스트랩 friction이 다수 사이클(QA-B95~B100 계열) 반복되는 점을 감안해 **post-merge non-blocking smoke로 강등**하고 operation 승격은 unit/merge 게이트로 한정할지 — 운영 게이트 정책 결정 필요(추측을 확정으로 승격하지 않음).

#### [PLN] backend develop working tree 재오염 — LiveE2eBootstrapService credential guard WIP (2026-06-17, 153차 — QA-B112 · **Planned**)

- TSR 872차: `src/backend` develop HEAD `@7ac0a46` **불변**·WT **DIRTY 2M** — `LiveE2eBootstrapService.java`·`LiveE2eBootstrapServiceTest.java` 미커밋(QA-B95 `hasConfiguredCredentials()`·`hasConfiguredGuardianCredentials()` 가드 WIP).
- **계보**: QA-B07 dirty-tree lineage · QA-B95 harness deepen(BNK-283~284) 연계 · **기능 갭 아님** — develop 커밋 누락(이관 규율 5·7).
- **영향**: backend merge gate **BLOCK** · cross-stream merge **BLOCK** · BE merge(331) 실행 금지.
- **153차 planner 가정**: COD가 WIP 완료 단위 커밋 → WT CLEAN → tester merge(341) 선행.

#### [PLN] frontend develop working tree 재오염 — Kakao map instance refactor WIP (2026-06-17, 153차 — QA-B114 · **Planned**)

- TSR 874차: `src/frontend` develop HEAD `@b000d92`(QA-B113 Fixed 직후) **불변**·WT **DIRTY 5M+4U** — `KakaoTransportMap*`·`navConfig.js`·`components.css` + `KakaoBareMap.jsx`·`kakaoMapInstance.js`·`kakaoMapInstance.test.js`·`useKakaoMap.js` 미커밋.
- **계보**: QA-B111/B113 transport map view split lineage · v1.3-A Kakao map SDK preview deepen(BNK-285) · **기능 갭 아님**.
- **영향**: frontend merge gate **BLOCK** · cross-stream merge **BLOCK** · FE merge(10) 실행 금지.
- **153차 planner 가정**: COD가 map instance refactor 커밋 → WT CLEAN → tester merge(341) 선행.

#### [PLN] backend develop working tree 재오염 recurrence — VisitService WIP (2026-06-17, 151차 — QA-B110 · **✅ Fixed @ `e54a699` (TSR 850 검증)**)

- **152차 planner 갱신**: QA-B110 **Fixed @ `e54a699`**(`fix(v2/visits): return unpaired status for missing paired schedule`·`VisitService`/`VisitServiceTest` 2 files +12/-1)·backend WT **CLEAN** 복귀·test `@598d108` `mvn test` **246/246 PASS**·**backend merge gate 가드 해소**(TSR 850 검증). 구조적 dirty-tree 재발 방지 권고(아래)는 carry.
- TSR 849차: `src/backend` develop HEAD `@c5f1325`(커밋 증분 0) 위 working tree **DIRTY 2M** — `VisitService.java`·`VisitServiceTest.java` 미커밋 재오염 · test worktree `src/backend-test` `mvn test` **246/246 PASS**(기능 정상)
- **계보**: QA-B07(2026-06-06) dirty-tree 패턴 lineage · QA-B101/B103(VisitService/transport refactor 계열)과 동일 재발 · **기능 갭 아님 — 완료 단위 develop 커밋 누락(이관 규율 5·7)이 유일 블로커**
- **영향**: backend merge gate **BLOCK** · cross-stream merge **BLOCK** · BE merge(320) 실행 금지 · operation 승격 잔여 = QA-B110 + QA-B95
- **151차 planner 가정**: 코드 결함 아님 · **수동 해소**: COD가 `VisitService`/`VisitServiceTest` WIP를 완료 단위로 정리·`mvn test` 1회 후 **develop 커밋** → WT CLEAN → BE tester merge(320)
- **미확정(구조적)**: VisitService 계열 dirty-tree가 반복 재발(B101/B103/B110) — pre-commit hook·`run_agent.py build` 종료 시 WT clean 게이트 강제 여부 검토 권고(인프라 영역·coder/ops·#36 에스컬레이션 계열)

#### [PLN] 직원변경/정기 요보사 상담일지 cluster (2026-06-17, 151차 — BNK-269 · **신규 갭 candidate · 「가정」 주야간 적용성 미확인 P3**)

- ezCare FAQ21795 「[주간] 상담일지 작성(직원변경 시)」: 급여제공 직원 변경 시 변경 직원 급여개시일로부터 **토·공휴일 포함 14일 이내** 수급자(보호자) 상담·상담일지 작성 (평가지표**19**·업무인계 필드: 건강상태·생활환경·특이사항·관리자 동행 소개) · 예외: A(기존)→B(14일 미만)→A 재교체 시 상담 미실시 인정
- cross-confirm: FAQ21804 「[연간] 요양보호사 정기 상담」(평가지표2·BNK-213) 도 ogada 미구현 → **상담일지 cluster**(정기 상담 + 직원변경 상담)로 묶어 검토 권고
- ogada 실측: staff 도메인 = `staffhr`/`staffreport`/`staffrefresher`/`stafftraininglog`/`staffhealth`/`leadcaregiver` · 상담 = `grievance`(G42)·`monitoring`(G30)·`onboardingsupport` — **직원변경/정기 요보사 상담일지 전용 기능 부재**
- **「가정」(미확인)**: ezCare 평가지표 19 numbering 은 시설/방문/주야간이 상이(silverangel 시설 지표19=노인인권) — **주야간보호 평가 체계에서의 적용성·의무 여부 미확인** · 추측을 확인으로 승격하지 않음 → **planner 결정 대기**(주야간 의무 확인 시 G-STAFF-CHANGE-COUNSEL Epic P3 승격·USER_STORIES 후보)

#### [PLN] frontend origin/test push 누락 after develop→test local merge (2026-06-16, 149차 — QA-B106 · **✅ Fixed @ TSR 827**)

- **150차 planner 갱신**: QA-B106 **Fixed @ TSR 827** — `origin/test` push 완료 @ `55fdbd0`→`d8f1fdf` lineage · FE develop=test=origin/test **`d8f1fdf`** · operation 잔여 BLOCK = **QA-B95 only**
- TSR 825차: frontend local `test` `@25ca88e`(=develop, 820차 14 commits + 824차 merge 완료·**1490/1490 PASS**) 그러나 `origin/test` `@4299914` 로 **16 commits 미푸시**(`git log --oneline origin/test..test` → 16)
- `origin/develop` `@25ca88e` 동기화됨 — develop는 push 정상, **test 브랜치 push 단계만 누락**
- **149차 planner 가정**: 코드 결함 아님 · merge pipeline(`scripts/git_merge_to_test.sh`) 의 `git push origin test` 단계 점검 필요 · **수동 해소**: `git -C src/frontend-test push origin test` → `origin/test` = `25ca88e` 확인 · submodule 재 clone 시 test 산출물 **유실 위험**(이관 규율 push 누락) → operation 승격 **선행 필수** · BE merge(309)와 **병행 가능**(독립 push)
- **미확정**: merge pipeline push 단계가 매 사이클 반복 누락되는지(구조적) vs 1회성 — 재발 시 pipeline push 검증 step 추가 권고(코드 영역 — coder/ops)

#### [PLN] v1.3-B transport suggest WIP dirty-tree (2026-06-15, 137차 — QA-B90 · **✅ Fixed @ `db94a65`**)

- **138차 planner 갱신**: QA-B90 **Fixed** @ `db94a65` — v1.3-B suggest API committed · FE wire @ `2ffe59f` · **v1.3-B ✅ full stack**

#### [PLN] PressureUlcerPage client select mock regression (2026-06-15, 137차 — QA-B89 · **✅ Fixed @ `8d00f5d`**)

- **138차 planner 갱신**: QA-B89 **Fixed** @ `8d00f5d` — HEAD **1275/1275 PASS** @ TSR 692

#### [PLN] G-NURSING injectable Clock WIP dirty-tree (2026-06-15, 137차 — QA-B88 · **✅ Fixed @ `090b2d7`**)

- **138차 planner 갱신**: QA-B88 **Fixed** @ `090b2d7` — nursing date guard committed · WT **CLEAN**

#### [PLN] L03_M01/M06 FE wire scope (2026-06-15, 138차 — BNK-215~216 · **✅ Fixed @ BNK-217 `12591d4`/`2966447`**)

- **139차 planner 갱신**: M01 `/nursing/service` + M06 `/nursing/excretion-tubes` **✅ full stack** @ BNK-217 · L03 **13/14 effective 100%**

#### [PLN] L03_M08 scope (2026-06-15, 139차 — BNK-218 · **N/A 폐기 확정**)

- carefor demo `L03_M08` noready2 자체 disabled — ogada 구현 **불필요** · L03 커버리지 **effective 100%**(13/13 구현 대상 leaf)

#### [PLN] EasyPay provider normalization dirty-tree (2026-06-15, 139차 — QA-B93 · **✅ Fixed @ `b45830d`**)

- **140차 planner 갱신**: QA-B93 **Fixed** @ `b45830d` — `EasyPayService.normalizePersistedProvider` committed · BE+FE WT **CLEAN** · merge **577 FULLY UNBLOCKED**

#### [PLN] G-ONBOARD-SUPPORT FE wire scope (2026-06-15, 140차 — BNK-223 · **✅ Fixed @ BNK-224 `36264b5`/`4c1fd43`**)

- **141차 planner 갱신**: G-ONBOARD-SUPPORT **✅ full stack** — BE V126/V127 + FE `BranchOnboardingSupportPanel` + live E2E harness @ `36264b5` · QA-B94 openedOn guard @ `43c4b08`

#### [PLN] G26 7-8 통계 대시보드 leaf (2026-06-16, 149차 — BNK-261 · **✅ full stack 3-function @ BNK-270 `09e4ec17`**)

- **150차 planner 갱신**: PDF p.92 7-8 dual-function(① 의료비공제·② 본인부담 월별 6필드) **✅ full stack closure** @ `d8f1fdf`/`3481eb8` — `/billing/reports/statistics`·`BillingStatisticsReportPage`·`g26StatisticsReports.js` (결정 95 48~49회째)
- **151차 planner 갱신**: **③ 이동서비스비 월별 통계 ✅ full stack closure** @ `3672bbe`(BE `GET /billing/reports/transport-service-fee-statistics`·`TransportServiceFeeService` aggregate)/`09e4ec17`(FE `fetchTransportServiceFeeStatisticsApi`·`BillingStatisticsReportPage` ③ 섹션) · pilot E2E deepen @ `30f03e8`(BNK-272) — **G26 3-function 완성**(①의료비공제+②본인부담+③이동서비스비·결정 95 50회째·NHIS #44 러-1~4 연계)
- **잔여 P1**: G26 **모니터링 근거 표시 일관성**(BNK-273·G30/G24b/G21 표기 체계 통일) — 통계 대시보드와 모니터링 근거 cross-link UX 검토

#### [PLN] silverangel 지표27 보호자회의 (2026-06-17, 150차 — BNK-267 · **P3 신규 Epic 후보**)

- silverangel essential 지표27 「가족과의 소통」— **보호자 회의 반기별 1회+**(일시·장소·방법·내용·결과·참석자) · ogada △ 부분(알림·G14·meal menu) · **보호자회의 전용 Epic 없음** → **G-GUARDIAN-MEETING P3** (ROADMAP v3.1 · USER_STORIES 후보)

#### [PLN] G21 plan/claim 이중일정 UI 분리 (2026-06-16, 147차 — BNK-250 · **색상 처리상태 ✅ BNK-261 · 일정 분리 UI 미확정**)

- Channel.io 증거: 「계획일정 가져오기」vs「청구일정 가져오기」분리·청구반영 검은/빨간 숫자 (b2863b61+bc7f4cd9)
- **147차 planner 조치**: ROADMAP v2 **P2** 태스크화 · BE `schedule_kind` PLAN/BILLING **이미 존재** — **FE 분리 UI·색상 처리상태** 설계 착수 대기
- **149차 planner 갱신**: **청구반영 검은/빨간 배지 UI ✅ full** @ `6da49aa`(BE `billingClaimReflectionStatus` flag)/`25ca88e`(FE `VisitsPage` 배지·검은=REFLECTED·빨간=NOT_REFLECTED·UNPAIRED·Channel.io bc7f4cd9 1:1) — **색상 처리상태 부분 closure**
- **미확정 잔여**: 「계획일정 가져오기」/「청구일정 가져오기」 **import 분리 UI**(b2863b61) — v2 G21 범위 내 단일 화면 탭 vs 별도 Route · coder UXD 협의 후 API_SPEC 보강 · **P2 carry**

#### [PLN] frontend live E2E harness dirty-tree (2026-06-15, 145차 — QA-B99 · **✅ Fixed @ `e6944f1`/`9ad8346`**)

- **147차 planner 갱신**: QA-B99 **Fixed** @ `e6944f1`/`9ad8346` — live E2E harness committed · WT **CLEAN** · FE develop→test **merged** @ `4299914` (TSR 796)

#### [PLN] live E2E 환경변수 구성 scope (2026-06-15, 142차 — QA-B95 · **Planned**)

- TSR 740차: `npm run test:live-e2e` 4 suite FAIL — `LIVE_E2E configuration is incomplete`
- **필수 env**: `LIVE_E2E=1` · `LIVE_E2E_EMAIL`/`LIVE_E2E_PASSWORD` 또는 `LIVE_E2E_ACCESS_TOKEN` · `LIVE_E2E_CLIENT_ID` · `LIVE_E2E_GUARDIAN_EMAIL`/`PASSWORD`(guardian suite용)
- **정본**: `scripts/dev-live-e2e.env.example` → `scripts/dev-live-e2e.env` · 실행: `./scripts/run-live-e2e.sh`
- **142차 planner 가정**: 코드 결함 아님 · **스테이징/로컬 env 구성 후 재검증** → QA-B95 해소 · merge(612)와 **병행 가능**(결정 73: live E2E run은 develop→test merge 선행 조건 아님) · **operation 승격 전 필수**

#### [PLN] G19 통합재가 provider discovery scope (2026-06-15, 143차 — BNK-231~235 · **△ BE harness ✅ · FE wire ❌ P1**)

- longterm [selectLtcoSrch.web](https://www.longtermcare.or.kr/npbs/r/a/201/selectLtcoSrch.web) — `ltcAdminKindChoiceYn8`(통합재가)·`Yn7`(가족휴가)·`searchAdminKindCd` 06/07 filter
- **143차 planner 갱신**: BE live API harness @ `41d8de5` · provider filter centralize @ `8cb8789` · ogada **FE discovery UI 미구현** · v2+ Epic V — **외부 링크 deep-link vs 내장 provider search API** 방식 미결

#### [PLN] #44 이동서비스비 lawImg 접근 DRIFT (2026-06-15, 143차 — BNK-235 · **P0 seed 유지 · evidence joHistory+V103**)

- [NHIS #44 joHistory](https://www.nhis.or.kr/lm/lmxsrv/law/joHistoryContent.do?DATE_END=20231229&DATE_START=20250701&SEQ=1637&SEQ_CONTENTS=3281769) **95차 zero drift** `c886ff1f` — 러-1~4 법문 verbatim·1일1회·편도50%·일지 의무
- [NHIS lawImg](https://www.nhis.or.kr/lm/lmxsrv/law/lawImageView.do?SEQ=1637&SEQ_CONTENTS=3281769&LAWGROUP=2) **95차 DRIFT 404** `fd7a675e` — 로그인/인증 필요 추정
- **143차 planner 가정**: ogada V103 seed **830/2,630/5,230/8,630** 유지 · 향후 `law.go.kr admRulBylInfoR.do` 대체 접근 시도 권고(BNK-236) · **P0 닫힘 상태 유지**

#### [PLN] G18-SHORT-PILOT·G-FAMILY-LEAVE 통합 모델 (2026-06-15, 143차 — BNK-235 · **P3 deepen**)

- [silvercare.org 공지](http://www.silvercare.org/info/notice_view.asp?b_idx=16929) — **2026.1~별도 통보 시까지**(무기한 연장) · 단기보호 월 **9일** · 가족휴가제 연 **12일** · 전산 4챕터(이용자·종사자·청구·청구관리)
- **143차 planner 가정**: G18-SHORT-PILOT + G-FAMILY-LEAVE = 단일 **`ShortTermCareContract`** 모델 통합 권고 · MVP 범위 밖 · v3.x+ 검토

#### [PLN] G-STAFF-MEETING scope (2026-06-15, 143차 — BNK-232 · FAQ21822 · **P3 candidate**)

- 이지케어 FAQ21822 — 「**2026년 평가지표에서 [직원회의] 삭제**」·운영 편의로 월간 회의록 잔존 · 메뉴 `10.기관평가▶10.1서류함▶직원회의록`
- **143차 planner 가정**: **법정 필수 아님** · G42 고충처리·G41 직원교육과 별 Epic · **P3 candidate** · MVP 범위 밖

#### [PLN] G2b silverangel extraService evidence DRIFT (2026-06-15, 143차 — BNK-235 · **LCMS product 정본 carry**)

- silverangel `daycareExtraService.do`·`daycareFeeService.do` **404 URL 폐기** — G2b 3-method evidence는 [LCMS product](https://www.lcms.or.kr/reg/selectProductGuide.do) `57ec33be` zero drift로 carry
- **143차 planner 가정**: G2b **P2 scope 불변** · silverangel 공개 URL 카탈로그 **4건**(essential·summary·businessSupport·daycareProgram)

#### [PLN] G24b 8항목 scope (2026-06-15, 141차 — BNK-226 · **✅ full stack · live E2E run P1**)

- ezCare FAQ21810 8 세부항목 ↔ V128 5신규컬럼 + V84 기존 6필드 = **1:1 parity** @ `45fb6d9`/`49fbf67`
- **143차 planner 갱신**: compliance API @ `98002d4`/`f4c8beb` · **dashboard widget ✅** @ `ca0b627`/`baa6d6d` (BNK-229) · **compliance list page ✅** @ `eb16734` (BNK-232~233) · **live E2E run** post-merge 권장(결정 96) · 21815 「변경사유」 필드 = **P2**

#### [PLN] G-FAMILY-LEAVE evidence scope (2026-06-15, 140차 — BNK-223 · **evidence ✅ · 구현 ❌ P3**)

- MOHW 2025-247 HWPX + angelsitter #774 + **longterm menuId=2854 정본** = 3-source 완전 정합
- **140차 planner 가정**: 연 12일 단기보호 OR 24회 종일 방문요양 한도 트래킹 = **P3** · G18-SHORT-PILOT·US-R03(8-13) 연계 · **v3.x candidate**

#### [PLN] G-LIVECHAT·G-CIST scope (2026-06-15, 140차 — BNK-223 · **P3 candidate 미확정**)

- silverangel daycareProgramProvided.do — **굽은나무 라이브톡**(vendor live chat) · **CIST/K-MMSE~2/GDS** 3종 인지선별검사
- **140차 planner 가정**: NHIS authoritative scope **외** · ogada G9-COG(BNK-167)은 NHIS 등급 import만 · **P3·v3.x+ 검토** · MVP 범위 밖

#### [PLN] G-STAFF-COUNSEL scope (2026-06-15, 138차 — BNK-213 · FAQ21804 · **P3 미확정**)

- 이지케어 FAQ21804 — 요양보호사 정기 상담(평가지표 2·5필드·30일 조치·메뉴 `1.직원▶1.3▶요양보호사 상담일지`)
- **138차 planner 가정**: v3.1+ **P3** — MVP 범위 밖 · US-R03 HR lifecycle과 연계 검토

#### [PLN] J03 service-flow E2E quiet-hours wall-clock (2026-06-14, 136차 — QA-B87 · **✅ Fixed @ `63cb193`**)

- **137차 planner 갱신**: QA-B87 **Fixed** @ `63cb193` — BE HEAD **1095/1095 PASS** (TSR 669차)

#### [PLN] L03_M14 pilot E2E future measure-date fixture (2026-06-14, 136차 — QA-B86 · **✅ Fixed @ `63cb193`**)

- **137차 planner 갱신**: QA-B86 **Fixed** @ `63cb193` — pilot fixture/Clock injection 정합 완료

#### [PLN] v1.3-B 자동 배차(다중 차량) 인터뷰 — **✅ 사용자 확정 (2026-06-14, 138차 · 결정 75)**

> v1.3-A 백엔드 완료 · v1.3-C(vehicles·이동서비스비·G15) 구현 · v1.3-B 코드 0%. **데모 후 재피드백** 전제로 PoC 범위 확정. 상세 REQUIREMENTS §3-13-9-5.

| # | 확정 |
|---|------|
| **Q1** | **(c)** 픽업(PICKUP) 자동배차 먼저 · 드롭(DROPOFF) = **v1.3-B.1** · **픽업 PoC = 이번 주 목표** |
| **Q2** | **(a) 차량당 1 run** — unique를 `지점×일×방향×vehicle_id`로 변경(DBA 마이그레이션) |
| **Q3** | 기본 **w1=0.5 / w2=0.3 / w3=0.2** · **지점(branch) 설정에서 변경 가능** + UI에 각 항목 설명(안정성·공정성·최단거리) |
| **Q4** | 픽업 시간창 **±15분** 기본 · 지점 설정으로 변경 가능 · **`clients.transport_notes`** 신규 추가 |
| **Q5** | **PoC: `POST /runs/suggest` ≤ 10회/지점/일** (hard cap, 429+UI 안내). Directions는 suggest 내부 호출만·데모 후 상한 재조정 |
| **Q6** | 자동 제안 → 수동 조정(DRAFT) → 확정 **OK** · 오버라이드 사유 코드 = **v1.3-B.1** |

**알고리즘(기획·구현 방향)**: OR-Tools VRP/TSP + Kakao Directions 거리 행렬 · 목표함수 `w1×담당변경 + w2×거리편차 + w3×총km` (Hard: 정원·시간창·스코프).

#### [PLN] MOHW 2025-247 HWPX 개정 항목 scope (2026-06-14, 134차 — BNK-198 · **P2/P3 미확정**)

- [MOHW 2025-247 HWPX 첨부](https://www.mohw.go.kr/boardDownload.es?bid=0026&list_no=1488433&seq=1) — application/hwp+zip 정본 **139,330B** · 17개 개정 항목(가~하) verbatim
- ogada **즉시 반영 P2**: **G17b**(제32조 인지활동형 미제공 사유)
- ogada **v2+/P3 후보**: **G-FAMILY-LEAVE**(제36조의2)·**G-RURAL-SUBSIDY**(제11조의8 별표2)·**G-PROG-MGR-BONUS**(제17조)
- **134차 planner 가정**: MVP 범위 밖 — 사용자 ROI 확인 전 Route 착수 금지 · G17b만 v2 P2 우선 검토

#### [PLN] G21 batch-confirm live E2E scope (2026-06-14, 134차 — BNK-197~198 · **✅ partial+ @ `13e691e`/`c22a5dc`**)

- 이지케어 [**FAQ 21782**](https://ezcare.easyms.co.kr/help/faq.ez?rowid=21782&type=web) — 「일정확정 전, 공단 청구명세서와 비교하기」5단·변경이력 일괄체크
- ogada **US-V05 ✅ partial+** — BE readiness/batch-confirm @ `0b807d8`/`c22a5dc` · FE `VisitBatchConfirmPanel` @ `13e691e`
- **134차 planner 갱신**: develop 닫힘 ✅ partial+ · **잔여 P1** = `pilotPageFlows` US-V05 E2E · G7 실파일 NHIS 비교 live 연동

#### [PLN] J03 quiet-hours dispatch enforce scope (2026-06-14, 134차 — BNK-195~198 · **✅ full @ `a057739`**) — **supersedes 132차 partial+**

- ogada J03 **quiet-hours 4-cycle ✅ full** — shared policy @ `a057739` · QA-B81/B82 Fixed
- **134차 planner 갱신**: dispatch 차단 **BE+FE+policy 단일화 완료** · **잔여 P2** = Solapi **live** 발송 E2E only

#### [PLA] #44 이동서비스비 러-1~4 출처 (2026-06-14, 126차 — BNK-174~175 · **56차·정본=NHIS 제34조 lawImg · P0 ✅ @ `39ee679`**)

- [NHIS 세부규칙 제34조](https://www.nhis.or.kr/lm/lmxsrv/law/joHistoryContent.do?DATE_END=20231229&DATE_START=20250701&SEQ=1637&SEQ_CONTENTS=3281769) embedded lawImg — **830/2,630/5,230/8,630** verbatim
- ogada V68 RU_3/RU_4 **4430/6230 → 5230/8630 보정 ✅** @ `39ee679` (V103)
- **126차 planner 갱신**: 125차 「정본=longterm 502·수동 보류」→ **56차 NHIS lawImg 정본 확정** · **P0 seed drift 해소**

#### [PLA] 8-12 HR report pack completion (2026-06-14, 127차 — BNK-176~179 · **✅ partial+**)

- PDF 7종 FE ✅ @ `07956f5` · live E2E harness ✅ @ `ccc4d75` · BE CSV export ✅ @ `bc927f7` · **BE CSV FE wire ✅** @ `488f547` · pagination ✅ @ `ff173af`
- **127차 planner 갱신**: 126차 △ deepen → **127차 ✅ partial+** · **잔여 P2** = print layout·사진 실데이터·live run

#### [PLN] J03 quiet-hours dispatch enforce scope (2026-06-14, 132차 — BNK-193~194 · **✅ partial+ @ `111f056`/`a057739`**)

- ogada J03 **quiet-hours FE+BE 3-cycle ✅ partial+** — BE dispatch skip/allow tests @ `328874d` · FE billing-notify block @ `111f056` · G32 boundary @ `a057739`
- 엔젤 sms_service.do·이지케어 K010 FAQ에 **조용한 시간대 공개 정책 0건** — ogada **자체 차별화** 가정 유지
- **132차 planner 갱신**: dispatch 차단 **BE+FE 구현 확인** · **잔여 P2** = Solapi **live** 발송 E2E · **QA-B81** `pilotPageFlows` test 정합화

#### [PLN] G9-COPAY-503 감경 lifecycle scope (2026-06-14, 132차 — BNK-194 · **P3 미확정**)

- [longterm 503 본인부담금 감경](https://www.longtermcare.or.kr/npbs/e/b/503/npeb503m01.web?menuId=npe0000002743) — 50%/60% 2트랙·직권/신청 **14일 SLA** verbatim evidence
- ogada G9-COPAY-NAMING 4-tier ✅ · **503 신청/해지 lifecycle UI ❌**
- **132차 planner 갱신**: v2+ **P3** — 감경 신청·해지·SLA 안내 UX · G9-SHORT/G9-DEMENTIA cluster와 분리 검토

#### [PLN] 7-5 live PG provider·G2b scope (2026-06-14, 132차 — BNK-191~194 · **✅ full @ `16a0734`/`51f2505`→`745a2f6`**)

- 케어포 func `7-5`·demo-work `npay_manage`·엔젤 **3-method** — ogada **Stub PG+V110 integrity ✅** @ `16a0734`/`51f2505` · provider hardening @ `745a2f6`/`328874d`
- **route alias WIP** — `services.js` `/payment` fallback (QA-B82)
- **live PG 벤더** — Hyosung FCMS vs 별도 PG vs 카카오페이 직연동 **미확정**
- **132차 planner 갱신**: 7-5 = **✅ full** (4-cycle hardening) · **잔여 P2** = live PG·G2b · route alias commit(QA-B82)

#### [PLN] J03 quiet-hours dispatch enforce scope (2026-06-14, 127차 — BNK-179 · **P2 미확정**) — **superseded by 132차**

#### [PLN] G41/G41b 교육일지 4분류 scope (2026-06-14, 129차 — BNK-184~187 · **✅ partial+ @ `e14ba10`/`32f87f1`**)

- 케어포 func `8-7.교육일지(노인인권, 재난, 소화, 직원권익)` 4분류 ↔ ogada V105~V106 **5종 CHECK** + compliance aggregate @ `0f11158`/`38d24b6`
- FAQ21807 **연1회→반기1회+** nuance — ogada `referenceHalf` CHECK **1:1**
- **129차 planner 갱신**: G41/G41b = **✅ partial+** (184→187 4-cycle) · **잔여 P2** = `LIVE_E2E=1` manual verify

#### [PLN] G-STAFF-WELFARE 포상급 지급 scope (2026-06-14, 129차 — BNK-185 · **P3 미확정**)

- 이지케어 [**FAQ21796**](https://ezcare.easyms.co.kr/help/faq.ez?rowid=21796&type=web) — 분기 1회+·`10.1서류함>포상급 지급내역서`·인건비 **외** 수당만·회식/상장 단독 불인정
- ogada `payroll`/`staff_welfare` Route·API **0건** — K008 cluster와 묶음 검토
- **129차 planner 갱신**: v2+ **P3 Epic** · US-S03(8-1-1 복지대장)과 분리 유지

#### [PLN] G-ONBOARD-SUPPORT 기관 도입 체크list scope (2026-06-14, 129차 — BNK-186 · **P2 미확정**)

- silverangel [**businessSupportService.do**](https://www.silverangel.kr/newSilverangel/service/businessSupportService.do) — 1회차 8필드·2회차(+10일) 6필드 verbatim
- FAQ21806(직원 onboarding)과 **기관 도입** 축 분리 — platform_admin/SaaS onboarding 후보
- **129차 planner 갱신**: v1.2.1 범위 **외** · **P2 carry** · 구현 전 사용자 ROI 확인

#### [PLN] 7-5 live PG provider·G2b scope (2026-06-14, 130차 — BNK-189~190 · **△ partial+ @ `bebd874`/`b893e97`**) — **superseded by 132차**

- 케어포 func `7-5`·demo-work `npay_manage`·엔젤 **3-method**(자동이체·가상계좌·카드) — ogada **Stub PG ✅** @ `438f5c7`/`c9baca2` · pilot E2E @ `3848af6`/`1231389`
- **live PG 벤더** — Hyosung FCMS(기존 G2 CMS) vs 별도 PG vs 카카오페이 직연동 **미확정**
- **130차 planner 갱신**: 7-5 = **✅ partial+** (skeleton+pilot E2E+prior-month guard) · **잔여 P2** = live PG·G2b 가상계좌/카드 · provider normalization WIP(QA-B78/B79) · **→ superseded by 132차**

#### [PLN] LCMS 평가 read-only role scope (2026-06-14, 130차 — BNK-190 · **P3 미확정**)

- LCMS [selectProductGuide.do](https://www.lcms.or.kr/reg/selectProductGuide.do) — 「기관 평가 시 엔젤시스템 접속」·「데이터 외부 유출 금지」 verbatim
- ogada audit log·RBAC ✅ · **평가 전용 read-only role**·계약 SLA UI **0건**
- **130차 planner 갱신**: v2+ **P3** — `evaluator_readonly` 역할·평가기간 임시 권한 vs hq_admin 위임 **사용자 확정 전 Won't v1.2.1**

#### [PLN] G30 integrated checklist scope (2026-06-14, 128차 — BNK-181~184 · **✅ full @ `5146895`**)

- BNK-181→183 BE→184 FE **3-cycle 폐루프 완전 닫힘** — FAQ21838/21839/21841/21842 aggregate
- **128차 planner 갱신**: G30 = **✅ full** · **잔여 P1** = live API E2E verify

#### [PLN] G34-QUAL team lead eligibility gate (2026-06-14, 128차 — BNK-177~183 · **✅ partial+ @ `574bd08`/`997831c`**)

- [FAQ 21837](https://ezcare.easyms.co.kr/help/faq.ez?rowid=21837&type=web) — 177→183 **4-cycle 폐루프** 완료
- **128차 planner 갱신**: G34-QUAL = **✅ partial+** · StaffPage admin summary = **P3 carry**

#### [PLN] G34-QUAL team lead eligibility gate (2026-06-14, 127차 — BNK-177 · **P2 신규**) — **superseded by 128차**

- [FAQ 21837](https://ezcare.easyms.co.kr/help/faq.ez?rowid=21837&type=web) — 팀장급 요양보호사 **실무경력 5년**(월 60시간×60개월)·고시 48~58조
- ogada G34 선임 업무수행일지 ✅ · **FE gate partial** @ `443efca` · **BE eligibility 검증 ❌**
- **127차 planner 갱신**: G34-QUAL = **P2** · v2 모니터링 checklist 연계 검토

#### [PLA] G-HOMEPAGE scope (2026-06-14, 126차 — BNK-175 · **P3/v2+ Epic**)

- silverangel [websiteProvided.do](https://www.silverangel.kr/newSilverangel/webSite/websiteProvided.do) — 기관 홈페이지 제작·계절 디자인·수급자 연동·CJ MOU 식단표
- **126차 planner 가정**: ogada MVP 범위 밖 · **P3/v2+ Epic** · 사용자 확정 전 Route 착수 금지

#### [PLA] FAQ21833 K012 재무회계 scope (2026-06-14, 126차 — BNK-173 · **P3 신규**)

- 이지케어 [**FAQ 21833**](https://ezcare.easyms.co.kr/help/faq.ez?rowid=21833&type=web) — 종신보험료·운영자금·재무회계 기준 확인
- **126차 planner 가정**: **P3 cluster**(K008~K014) · MVP 범위 밖

#### [PLA] EZCare FAQ 14종 K008~K014 cluster (2026-06-13, 125차 — BNK-169 · **P3 신규**)

- 이지케어 FAQ **14 categories** 벤치마크 — ogada **5/14 미구현**(K008~K014: 인력배치·시설·급여제공·모니터링·CS 등)
- **125차 planner 가정**: **P3/v2+ cluster** — G30 monitoring ✅ partial+ 이후 패리티 검토 · MVP 범위 밖 · 사용자 확정 전 일괄 Route 착수 금지

#### [PLA] silverangel URL migration DRIFT (2026-06-13, 125차 — BNK-170 · **정보성**)

- silverangel `/system_feature/` live **404** → 정본 **`/newSilverangel/`** 경로로 migration
- **125차 planner 가정**: 벤치마크 snapshot carry · ogada 구현 영향 없음 · 재벤치마크 시 URL 정본 갱신

#### [PLA] G30 monitoring live E2E scope (2026-06-13, 125차 — BNK-169~171 · **✅ partial+ @ `b8e92bf`**)

- FAQ21836/21841 5필드 자가진단·유선상담 5명·V100·basis fallback·pilot E2E @ `6f6915f`/`6a72b70`/`0da41c6`/`b8e92bf`
- **125차 planner 가정**: develop 닫힘 ✅ partial+ · **잔여 P1** = tester live E2E verify · FAQ21812 관리자 라운딩·FAQ21813 업무수행일지와 **통합 checklist**는 v2 Epic

#### [PLA] 8-12 HR report pack completion (2026-06-13, 125차 — BNK-171 · **✅ partial+ @ `07956f5`**)

- 케어포 func `8-12`·PDF p.106 — ogada aggregated API·referenceDate·exports ✅ @ `bf6dd25`/`07956f5`
- **125차 planner 갱신**: 123차 △ partial → **125차 ✅ partial+** · **잔여 P2** = PDF 7종·엑셀·live E2E

#### [PLA] #44 이동서비스비 러-1~4 출처 (2026-06-13, 125차 — BNK-171 · **53차·정본=longterm 502**)

- [law byl18](https://www.law.go.kr/LSW/admRulBylInfoR.do?admRulSeq=2100000271110&bylClsCd=110201&bylNo=18) — 주야간 러-1~4 **부재** carry
- **125차 planner 가정**: #44 **정본=longterm 502**(MOHW 제2025-247호·2026.01.05 수정) 재확정 · byl18=방문요양 원거리교통비 별표뿐 · **수동 보류** 유지

#### [PLA] FAQ21824 lifecycle wizard scope (2026-06-13, 124차 — BNK-165~167 · **checklist ✅ partial+**)

- 이지케어 [**FAQ 21824**](https://ezcare.easyms.co.kr/help/faq.ez?rowid=21824&type=web) 4단(계약→공단등록→서비스→월말청구) — ogada **checklist ✅ partial+** @ `58256c6` (`ClientFaq21824LifecyclePanel`)
- **124차 planner 갱신**: BNK-165 P1 「checklist UX」→ **✅ partial+ 닫힘** · **단일 wizard ❌ 유지**(모듈별 deep-link) · **잔여 P1** = live E2E · FAQ21829 Top5(청구일정·일정확정) 교차

#### [PLA] #44 이동서비스비 러-1~4 출처 (2026-06-13, 124차 — BNK-166~167 · **49차·정본=longterm 502**)

- [law byl18](https://www.law.go.kr/LSW/admRulBylInfoR.do?admRulSeq=2100000271110&bylClsCd=110201&bylNo=18) — 주야간 러-1~4 **부재** carry
- **124차 planner 가정**: #44 **정본=longterm 502**(MOHW 제2025-247호·2026.01.05 수정) 재확정 · byl18=방문요양 원거리교통비 별표뿐 · **수동 보류** 유지

#### [PLA] G9-SHORT/G9-DEMENTIA/G9-DR scope (2026-06-13, 124차 — BNK-166 · **P3 신규**)

- longterm 502 표③ 단기보호 5 fees · 표④ 치매전담실 5×5=25 fees · 503 의사소견서 본인 10% — ogada catalog **미반영**
- **124차 planner 가정**: **P3/v2+** — 주야간 MVP 완료 후 scope · 하드코딩 금지 · 정본=longterm 502 verbatim

#### [PLA] 7-1 선행입금 가드 UX (2026-06-13, 124차 — BNK-164 · **✅ partial+ @ `338c014`**)

- 케어포 PDF p.86–87 「**이전달 입금처리 필수**」 — ogada **`ClaimGenerationGuardBanner` ✅ partial+**
- **124차 planner 갱신**: BNK-160 P1 → **124차 ✅ partial+** · **잔여 P1** = live API E2E · warn vs hard block 정책은 운영 파일럿 후 확정

#### [PLA] FAQ21824 lifecycle wizard scope (2026-06-13, 123차 — BNK-161~163 · **superseded by 124차**)

- 이지케어 [**FAQ 21824**](https://ezcare.easyms.co.kr/help/faq.ez?rowid=21824&type=web) 4단(계약→공단등록→서비스→월말청구) — ogada는 G14·G24·G34·G38·7-x **모듈별 ✅ partial**이나 **단일 wizard ❌**
- **123차 planner 가정**: v2 Epic — 파일럿 현장용 **온보딩 checklist UI**로 분할 · RFID점검·공단계획 비교는 G21 v2 · 사용자 확정 전 일괄 wizard Route 착수 금지

#### [PLA] #44 이동서비스비 러-1~4 출처 (2026-06-13, 123차 — BNK-162 · **47차 방법론 정밀화**)

- [law byl18](https://www.law.go.kr/LSW/admRulBylInfoR.do?admRulSeq=2100000271110&bylClsCd=110201&bylNo=18) md5 `b72abb43` — select 옵션 **3건뿐**(방문요양·방문간호 원거리교통비·취약지역·변경신청서) → **주야간 이동서비스비 러-1~4 부재**
- **123차 planner 가정**: 러-1~4 정본 = **「장기요양급여비용 등에 관한 고시」 수가표 별표 직접 fetch** · 하드코딩 금지 · #44 수동 보류 유지

#### [PLA] G42 grievance P2 deepen scope (2026-06-13, 123차 — BNK-161 · **partial ✅**)

- FAQ21814 고충상담 — ogada **G42 ✅ partial** @ `b0a9e06`/`0460e9b` (CRUD+approval)
- **123차 planner 가정**: 잔여 P2 = **익명함·전자결재 UI·사후관리** — G34 sign modal 재사용 검토 · 사용자 확정 전 별도 결재 워크플로우 착수 금지

#### [PLA] 8-12 HR report pack completion (2026-06-13, 123차 — BNK-163 · **△ partial**)

- 케어포 func `8-12`·PDF p.106 — ogada `/staff/reports/status` Route ✅ @ `02cbd05`
- **123차 planner 가정**: 완성 기준 = **PDF 7종 출력·엑셀·기준일 필터·live E2E** — G41(8-7 교육일지)과 동일 HR report pack으로 묶음

#### [PLA] 7-1 선행입금 가드 UX (2026-06-13, 123차 — BNK-160 · **P1 deepen**)

- 케어포 PDF p.86–87 「**이전달 입금처리 필수**」 — ogada US-M03-b 전월 미입금 가드 ✅ · **청구 생성 UX deepen ❌**
- **123차 planner 가정**: `/billing` 청구 생성 전 **paidAt completeness** 안내·차단 UX = P1 · 사용자 확정 전 자동 차단 정책(하드 block vs warn) 미확정

#### [PLA] G40b fiscal-half compliance dashboard (2026-06-13, 121차 — BNK-153 · **122차 ✅ full @ `7b68f54`**)

- 이지케어 FAQ21811 **반기 1회** · Channel.io `2.2 정기욕구평가현황`·관리일 체크
- **122차 planner 확정**: `PeriodicRiskAssessmentStatusPage` Route **`/clients/periodic-risk-assessments`** ✅ @ `7b68f54` — 121차 가정 **해소**

#### [PLA] LCMS product/selectProductGuide 404 cluster (2026-06-13, 122차 — BNK-158 · **정보성**)

- [LCMS product/selectProductGuide.do](https://www.lcms.or.kr/product/selectProductGuide.do) live **404** · md5 `abe57876`(= regStep.do **동일 404 셸**)
- **122차 planner 가정**: 정본은 [reg/selectProductGuide.do](https://www.lcms.or.kr/reg/selectProductGuide.do) `57ec33be` **43차 zero drift** · product URL **폐기** carry

#### [PLA] G42 grievance + FAQ21823 wage contract scope (2026-06-13, 122차 — BNK-157 · **123차 ✅ partial @ `b0a9e06`**)

- FAQ21814 고충상담·FAQ21823 임금협의·근로(재)계약 — ogada **G42 ✅ partial** · 21823 **0건**
- **123차 planner 갱신**: G42=**US-T14 ✅ partial** · 잔여 P2=익명함·전자결재·사후관리 · 21823=**US-R03 P2** workflow 하위(서식·3년 보관)

#### [PLA] silverangel 9-step admission scope (2026-06-13, 121차 — BNK-150~154 · **P2 Epic**)

- silverangel essential 「신규입소시」 9-step — 지표19(수급자교육)·20(욕구사정)·**21(위험도 3종=G40 ✅ partial+)**·22(급여계획)·27(기능회복)·33(기피식)·35(연명의료)
- **121차 planner 가정**: G40 ✅ partial+ 완료 → 나머지 5종은 G24/G17/G38 lifecycle **Epic T**로 분할 — 사용자 확정 전 일괄 Route 착수 금지

#### [PLA] G40b fiscal-half compliance dashboard (2026-06-13, 121차 — BNK-153 · **P2**)

- 이지케어 FAQ21811 **반기 1회** · Channel.io `2.2 정기욕구평가현황`·관리일 체크
- **121차 planner 가정**: G40b Panel ✅ partial → **반기 compliance list 대시보드** 별 Route — 사용자 확정 전 `/clients` 전역 대시보드 착수 금지

#### [PLA] G2b Hyosung CMS multi-payment scope (2026-06-13, 121차 — BNK-154 · **P2**)

- silverangel extraService **자동이체·가상계좌·카드** 3-method · ogada G2=FCMS 자동이체만
- **121차 planner 가정**: v2 Epic L — **가상계좌·카드**는 G2 CMS 등록/해지 ✅ partial 후속 · 사용자 확정 전 PG 벤더 선정 금지

#### [PLA] LCMS regStep.do 404 onboarding evidence (2026-06-13, 121차 — BNK-154 · **정보성**)

- [lcms regStep.do](https://www.lcms.or.kr/reg/regStep.do) live **404** · 로컬 snapshot `docs/planning/research/snapshots/lcms_regstep.html` carry
- **121차 planner 가정**: 정원 구간별 요금 역공학 **미확인** — LCMS=엔젤 vendor 확정 carry · 온보딩 UI 벤치마크는 `selectProductGuide.do` 정본 유지

#### [PLA] FAQ21828 vs FAQ21807 교육일지 이중 정본 (2026-06-13, 119차 — BNK-143 · **P2**)

- 이지케어 [**FAQ 21828**](https://ezcare.easyms.co.kr/help/faq.ez?rowid=21828&type=web)(지표5·연1+신규7일·필수4필드) vs [**FAQ 21807**](https://ezcare.easyms.co.kr/help/faq.ez?rowid=21807&type=web)(지표14·반기 노인인권) vs 케어포 func **`8-7.교육일지`**
- **119차 planner 가정**: US-S02 `/staff/training` 하위 **교육일지 탭** + documentType(`operational-regulation`·`elder-rights`) 분리 — 사용자 확정 전 구현 착수 금지

#### [PLA] PDF↔func.php 8-10 번호 충돌 (2026-06-13, 118차 — BNK-138 · **P2 정책**)

- 케어포 [PDF 132p](https://web.archive.org/web/20260528120000/https://www.carefor.co.kr/ct_att/contents_article/0/202206/12/Dov8rzFqBv.pdf) **`8-10.현황 리포트`** ≠ func.php **`8-10.건강검진관리`**
- BNK-98 **7-x 삼원 불일치 정책**을 **8-x에 확장** — Route 정본=func.php · PDF=온보딩 보조 · rename 금지

#### [PLA] FAQ21806 US-R03 onboarding scope (2026-06-13, 119차 — BNK-139~142 · **P2 workflow**)

- 이지케어 [**FAQ 21806**](https://ezcare.easyms.co.kr/help/faq.ez?rowid=21806&type=web) 입사 6단계·서류 **8종**·건강검진 **5영역**
- ogada US-R02 partial ✅ · US-R03 lifecycle core ✅ · **HR file hub ✅ partial** @ `bbb8e35`/`bc3c967` — **6단계 workflow CRUD·근로계약 서식·4대보험** v2 P2 잔여

#### [PLA] FAQ21822 직원회의 (2026-06-13, 118차 — BNK-139 · **P3 정보성**)

- **2026 평가지표 [직원회의] 삭제** — 메뉴 `10.기관평가>10.1서류함>직원회의록`
- G32 사례관리 회의록과 **별개** · 서식은 G34/G32 재사용 · **v3.1 Could**

#### [PLA] FAQ21799 건강검진 Epic scope (2026-06-13, 117차 — BNK-135 · **117차→118차 partial ✅**)

- ~~ogada lifecycle `health-checkup` checklist UI만 — **건강검진 BE·파일함 ❌**~~ → **118차 partial ✅** @ `f1268c6`/`604787f`
- **잔여 P2**: 직원 파일함 PDF/jpg 첨부 · 케어포 **8-12 직원현황 리포트**

#### [PLA] US-S02 FAQ21798 홀/짝 nuance (2026-06-13, 118차 — BNK-137 · **P3**)

- 이지케어 FAQ21798 — **홀/짝 출생연도** 이수 주기 vs ogada `REFRESHER_TRAINING_INTERVAL_YEARS=2`(입사일 기준)
- **P3** — 파일럿 센터 규모·직원 연령대 확인 후 정렬 여부 결정

#### [PLA] G39 반기 vs 연1 평가 주기 (2026-06-13, 117차 — BNK-134 · FAQ21801)

- 이지케어 **FAQ21801** = **반기별 1회 이상** (지표24) vs silverangel **지표44** = **연1회** 표기
- ogada BE V80 `UNIQUE(org,client,year)` = **연1회 가드**(보수적·합법) — **반기 다회 허용** 여부 파일럿 확인 필요

#### [PLA] US-S02 scope 분리 (2026-06-13, 117차 — BNK-135~136)

- coder 커밋 `G34-US-S02` = **8-7-1 보수교육** — 기획 US-S02(8-1-1 복지대장)와 **ID 충돌**
- planner **117차**: US-S02=보수교육(8-7-1) · **US-S03**=복지(포상) 제공대장(8-1-1) v3 Could로 **분리**

#### [PLA] longterm.or.kr live 수가 (2026-06-13, 117차 — BNK-133 · **#44 32차 복구**)
- **MOHW247 bid=247** 5차 출처 추가 — 러-1~4 **0건** · BNK-25 placeholder **32차 재확정**
- ~~로컬 snapshot carry만~~ → **live 복구 확인** · 이동서비스/거리단가 **수동 보류** 유지

#### [PLA] silverangel regStep.do HTTP 404 (2026-06-13, 117차 — BNK-136 · **DRIFT**)

- [regStep.do](https://www.silverangel.kr/newSilverangel/reg/regStep.do) · [product/selectProductGuide.do](https://www.lcms.or.kr/product/selectProductGuide.do) **404**
- 정본 [reg/selectProductGuide.do](https://www.lcms.or.kr/reg/selectProductGuide.do) md5 `57ec33be` — 온보딩 벤치마크 URL 갱신 필요

#### [PLA] longterm.or.kr live 수가 셸 드리프트 (2026-06-13, 116차 — BNK-131 · **superseded by 117차 — live 복구**)

- [longterm 2026 수가](https://www.longtermcare.or.kr/npbs/e/b/502/npeb502m01.web?menuId=npe0000002742) HTTP 200·md5 `19296bef` — title「전산 작업 안내」·live 수가표 **교체**
- ogada는 `docs/planning/research/snapshots/longterm_2026fees.html`·`docs/planning/research/snapshots/longterm_integrated.html` **로컬 snapshot carry** — live 복구 후 재실측 필요
- **BNK-25 거리단가 placeholder·하드코딩 금지** 29차 재확정

#### [PLA] 직원 lifecycle Epic scope (2026-06-12, 115차 — BNK-126~131 · FAQ21825 · **P1 core ✅ / P2 문서·서식**)

- 이지케어 FAQ21825 4단계 — **core wired** @ `75440bc`/`7243d21`/`9441a3c`/`a018e71` (상태머신·체크리스트·offboarding 가드)
- **P2 잔여**: 직원 파일함·근로계약서 서식·4대보험 신고·문서저장 자동화
- **G-Payroll module 11**(P3)과 **묶음 vs 분리** — v2 착수 시 ROI·파일럿 규모 확인 필요
- 4대보험·퇴직정산은 **v3 재무회계(G4)**와 경계 — MVP는 **체크리스트+파일함**만 vs 풀 HR

#### [PLA] LCMS CMS 3-method vs ogada 7-5 우선순위 (2026-06-12, 115차 — BNK-127 · **P2**)

- 엔젤/LCMS **계좌+카드+가상계좌** vs ogada CMS **자동이체 단일** — v2 FCMS 실연동과 **동시 vs 순차** 착수 여부
- Hyosung FCMS 커넥터(결정 87)와 **다중결제 채널** 범위 정렬

#### [PLA] autosave UX v1.3 후보 (2026-06-12, 115차 — BNK-127 · **P3**)

- LCMS 「큰화면·자동저장」 — ogada DESIGN_SYSTEM(큰폰트·터치)과 철학 일치 · **debounced autosave** 패턴 v1.3+ 적용 화면 범위 미정

#### [PLA] G37 FE care-plan attachment UI scope (2026-06-12, 108차 — BNK-105 · **superseded by 109차**)

- ~~BE V78·CRUD API @ `0325d95` **확인** — FE UI **미구현**~~ → **109차 닫힘** @ `e026ae9`/`6875af5`/`e9d1178`
- 인정기간별 **1건 우선 vs N건 허용** — 벤치마크 §107-2 「여러 건도 허용」·현재 구현 **N건 허용** · 파일럿 UX 확인 **잔여**

#### [PLA] G34 선임 요양보호사 업무수행일지 scope (2026-06-12, 112차 — BNK-118~122 · **superseded by 117차**)

- **117차 진전**: `/staff/lead-caregiver-log` Route·CRUD·**e-sign ✅** @ `314b380` · **8-7-1 △→✅ partial** @ `9c9fd5b`/`a11bbeb` (US-S02)
- **잔여**: func.php 8-1-2 depth-3 verbatim 필드 · **live E2E run** · **8-7-1 이수증 P2**
- 케어포 **8-1-1 복지(포상) 제공대장** — ogada **0건** · **US-S03** v3 Could (US-S02=8-7-1로 분리)
- 엔젤 **11종 서명** · 이지케어 **2974fadd** triple-source — e-sign scope 사용자 확인 **잔여**

#### [PLA] G-Payroll Epic scope (2026-06-12, 112차 — BNK-122 · **P3 Epic**)

- 케어포 module 11 **6 leaf**(11-1~11-6) — ogada payroll/salary **0건** · `/finance/payroll` placeholder와 **범위 정렬** 필요
- G34(8 module 직원 HR)와 **별개 도메인** — mid-large 센터 ROI 검토 후 v3+ vs v3.1 결정 필요

#### [PLA] FAQ21820 급여계약통보 lifecycle (2026-06-12, 112차 — BNK-121 · **P2 Epic**)

- FAQ21805(계약 체결·G14)와 **별개** — FAQ21820=[월간] 급여계약통보·전월말 공단 포털
- G38 care-plan notification compliance와 **LifecycleWorkflowPanel** 연계 검토 · US-T08/T10 교차

#### [PLA] G34 선임 요양보호사 업무수행일지 scope (2026-06-12, 111차 — BNK-118 · **superseded by 112차**)

- ~~ogada **0건**~~ → **112차 partial ✅** @ `6d6b426`/`559648f`
- ~~REQUIREMENTS §3-8-a `/staff/lead-caregiver-log` **v3** 예약~~ → **P2 △ partial** — e-sign workflow 잔여

#### [PLA] FAQ21805 수급자 계약 lifecycle scope (2026-06-12, 111차 — BNK-117~118 · **P2 Epic**)

- 이지케어 **FAQ21805** [비정기] 수급자 계약 — 갱신·해지·서명·비정기 주기
- G14 등급이력 **별도** — 계약 lifecycle은 **US-T10** · Epic T/G14 확장
- v1.2.1 범위 **외** · merge(300) 후 P2 착수 검토

#### [PLA] getting_started.php HTTP 302 (2026-06-12, 111차 — BNK-118 · **미확인**)

- BNK-114 **HTTP 200** → BNK-118 **HTTP 302** 접근 변동 — Wayback·live fetch 재확인 필요
- 이동서비스 분리 정책(#76) **번복 아님** — 스냅샷 신뢰도만 재검증

#### [PLA] G38/G39 dashboard snapshot aggregation (2026-06-12, 110차 — BNK-114 · **superseded by 111차 — QA-B49 Fixed**)

- ~~BE `@a0a7f9c` dashboard widget counts API ✅~~ → **111차 닫힘** @ `8fa9f3d`/`f72da41` — snapshot-first + parallel fallbacks
- ~~FE WT WIP 2M~~ → **WT CLEAN** @ `2cd2cd8` · **775/775 PASS**

#### [PLA] FAQ21800 정기 욕구사정 scope (2026-06-12, 110차 — BNK-113 · **P2 Epic**)

- 이지케어 [**FAQ 21800**](https://ezcare.easyms.co.kr/help/faq.ez?rowid=21800&type=web) — [연간] 정기 욕구사정·**평가지표15**·`2.수급자관리>기초평가>욕구사정`·연1회·이전기록 비교
- ogada **기초평가 탭 갭** — G14 등급이력·G24/G30 주기별 업무 Epic과 **묶음 검토** · v1.2.1 범위 **외** · **P2 후보**

#### [PLA] G38 FE care-plan notification monitoring UI scope (2026-06-12, 109차 — BNK-106 · **superseded by 110차**)

- ~~BE `GET /clients/care-plan-notifications/compliance` @ `5fd35a6` **확인** — per-client 5/11-month milestone·재발급 미반영 counts~~
- ~~FAQ 21802 **황갈=5·11개월·빨강=재발급 미반영** 색상 규칙을 dashboard StatCard/알림으로 surface할지 **P2 확정**~~ → **110차 닫힘** @ `28c22b0`/`4b2b082`/`87e6fae` · snapshot aggregation **QA-B49 잔여**

#### [PLA] G39 FE dashboard StatCard vs full page (2026-06-12, 109차 — BNK-107 · **superseded by 110차**)

- ~~`ProvisionResultEvaluationPage` @ `1c99bcd` **전용 페이지 ✅**~~ → **110차 닫힘** @ `8e66ae8`/`a16e1fe`/`28c22b0` · dashboard widget+weekly/monthly deepen ✅

#### [PLA] v1.2.1 merge gate 300 commits (2026-06-12, 111차 — TSR 415~416 · ★ **FULLY UNBLOCKED**)

- FE **`2cd2cd8`** 165 ahead · WT **CLEAN** → merge **ready**
- BE **`3ad2a90`** 135 ahead · WT **CLEAN** → merge **ready**
- **58 route·81 page** · **775/775·672/672 PASS** · **모듈 78.28%**
- **tester merge(300)** 즉시 가능 — QA Open 0건(BE/FE) · QA-B49 **Fixed** · SEC-D22 **Planned**(infra)
- **잔여 P1**: G17/G32/G33/G37/G38/G39 **live API E2E run** · G7 실파일 · US-L01 live · G24/G30 Epic · FAQ21800·FAQ21805 P2 · G34 업무수행일지 P2 · 본인부담 6단 게이트 P2 · 7-5·8-7-1 P2 · SEC-D22 `.gitignore`

#### [PLA] v1.2.1 merge gate 291 commits (2026-06-12, 110차 — TSR 400~404 · ★ **FE BLOCK** · **superseded by 111차**)

- FE **`26499b3`** 161 ahead · WT **DIRTY 2M** → merge **BLOCK**(QA-B49)
- BE **`a0a7f9c`** 130 ahead · WT **CLEAN** → merge **ready**
- **COD QA-B49→WT clean** 선행 필요 — **111차 닫힘**

#### [PLA] v1.2.1 merge gate 280 commits (2026-06-12, 109차 — TSR 389~392 · ★ **FULLY UNBLOCKED** · **superseded by 110차**)

- FE **`1c99bcd`** 155 ahead · WT **CLEAN** → merge **ready**
- BE **`f082933`** 125 ahead · WT **CLEAN** → merge **ready**
- **56 route·80 page** · **749/749·657/657 PASS** · **모듈 76.67%**
- **tester merge(280)** 즉시 가능 — QA Open 0건(BE/FE) · SEC-D22 **Planned**(infra)
- **잔여 P1**: G17/G32/G33/G37/G39 **live API E2E run** · G7 실파일 · US-L01 live · G24/G30 Epic · **G38 FE·G39 StatCard P2** · 본인부담 6단 게이트 P2 · 7-5·8-7-1 P2 · SEC-D22 `.gitignore`

#### [PLA] v1.2.1 merge gate 269 commits (2026-06-12, 108차 — TSR 375~380 · ★ **FULLY UNBLOCKED** · **superseded by 109차**)

- FE **`8b0c6c7`** 149 ahead · WT **CLEAN** → merge **ready**
- BE **`0325d95`** 120 ahead · WT **CLEAN** → merge **ready**
- **56 route·78 page** · **717/717·637/637 PASS** · **모듈 76.67%**
- **tester merge(269)** 즉시 가능 — QA Open 0건(BE/FE) · SEC-D22 **Planned**(infra)
- **잔여 P1**: G17/G32/G33 **live API E2E run** · **G37 FE UI** · G7 실파일 · US-L01 live · G24/G30 Epic · 본인부담 6단 게이트 P2 · 7-5·8-7-1 P2 · SEC-D22 `.gitignore`

#### [PLA] G33 settlement FE·1회 변경 불가 UX (2026-06-12, 107차 — BNK-100 · **부분 닫힘** · **superseded by 108차 pilot E2E**)

- BE settlement API+claim guard @ `70e6191` · FE settlement UI @ `359cf0c` **`BillingStartBalanceSettlementModal`** — **기본 폐루프 ✅**
- PDF p.90 「변경 불가」copy·수정 버튼 **비활성+툴팁** 문구가 파일럿 기대와 일치하는지 **사용자/파일럿 확인 전**(US-L05 live E2E 시 검증)

#### [PLA] v1.2.1 merge gate 256 commits (2026-06-12, 107차 — TSR 363~368 · ★ **FULLY UNBLOCKED**)

- FE **`c413615`** 142 ahead · WT **CLEAN** → merge **ready**
- BE **`838a7f6`** 114 ahead · WT **CLEAN** → merge **ready**
- **56 route·78 page** · **693/693·609/609 PASS** · **모듈 76.67%**
- **tester merge(256)** 즉시 가능 — QA Open 0건(BE/FE) · SEC-D22 **Planned**(infra)
- **잔여 P1**: G17/G32/G33 **live E2E run** · G7 실파일 · US-L01 live · G24/G30 Epic · 본인부담 6단 게이트 P2 · 7-5·8-7-1 P2 · SEC-D22 `.gitignore`

#### [PLA] G33 settlement FE·1회 변경 불가 UX (2026-06-12, 106차 — BNK-98 · **superseded by 107차**)

- BE settlement API+claim guard @ `70e6191` **확인** — FE 전용 settlement UI·「1회 생성 후 변경 불가」안내 copy **미확정** (US-L05 잔여)
- PDF p.90 「변경 불가」= API idempotent guard만으로 충분한지, FE 수정 버튼 **비활성+툴팁**까지 v1.2.1 필수인지 **사용자/파일럿 확인 전**

#### [PLA] PDF↔func.php 7-x 번호 정책 (2026-06-12, 106차 — BNK-98 확정·문서화)

- **확정**: ogada Route·COMPETITOR_MATRIX **메뉴 ID = func.php** · PDF = 온보딩·워크플로 보조 · **Route rename 금지**
- **잔여 P2**: func `7-5` 간편결제 vs PDF `7-5` 연간청구대장 — ogada **7-5 미구현** 우선순위 v2 vs v3.1

#### [PLA] v1.2.1 merge gate 244 commits (2026-06-12, 106차 — TSR 346~356 · ★ **FULLY UNBLOCKED** · **superseded by 107차**)

- FE **`7564c2a`** 135 ahead · WT **CLEAN** → merge **ready**
- BE **`70e6191`** 109 ahead · WT **CLEAN** → merge **ready**
- **55 route·46 page** · **679/679·603/603 PASS** · **모듈 76.67%**
- **tester merge(244)** 즉시 가능 — QA Open 0건(BE/FE) · SEC-D22 **Planned**(infra)
- **잔여 P1**: G17/G32/G33 **live E2E** · G7 실파일 · US-L01 live · G24/G30 Epic · 본인부담 공단비교 P2 · 7-5·8-7-1 P2 · SEC-D22 `.gitignore`

#### [PLA] v1.2.1 merge gate 232 commits (2026-06-11, 105차 — TSR 338~344 · ★ **FULLY UNBLOCKED** · **superseded by 106차**)

- FE **`37e6b00`** 129 ahead · WT **CLEAN** → merge **ready**
- BE **`208b37e`** 103 ahead · WT **CLEAN** → merge **ready**
- **55 route·78 page** · **656/656·581/581 PASS** · **모듈 76.67%**
- **tester merge(232)** 즉시 가능 — QA Open 0건 · QA-B42/B43 Fixed
- **잔여 P1**: G32 **`evaluationConductedMet` FE StatCard** · G17/G32 **live E2E** · G7 실파일 · US-L01 live · G24/G30 Epic · **7-3 청구시작 P2** · 본인부담 공단비교 P2

#### [PLA] v1.2.1 merge gate 220 commits (2026-06-11, 104차 — TSR 331~332 · ★ **FULLY UNBLOCKED** · **superseded by 105차**)

- FE **`0adf8c6`** 122 ahead · WT **CLEAN** → merge **ready**
- BE **`5e1828c`** 98 ahead · WT **CLEAN** → merge **ready**
- **54 route·45 page** · **646/646·576/576 PASS** · **모듈 76.67%**
- **tester merge(220)** 즉시 가능 — QA Open 0건 · QA-B41 Fixed
- **잔여 P1**: G17/G32 **live E2E** · G7 실파일 · US-L01 live · G24/G30 Epic · 본인부담 공단비교 P2

#### [PLA] v1.2.1 merge gate 210 commits (2026-06-11, 103차 — TSR 319~320 · ★ **FULLY UNBLOCKED** · **superseded by 104차**)

- FE **`53e4016`** 116 ahead · WT **CLEAN** → merge **ready**
- BE **`55fae99`** 94 ahead · WT **CLEAN** → merge **ready**
- **54 route·74 page** · **616/616·569/569 PASS** · **모듈 76.67%**
- **tester merge(210)** 즉시 가능 — QA Open 0건 · QA-B37/B38 Fixed
- **잔여 P1**: **G32 FE** · **G17 FE** · G7 실파일 · US-L01 live · G24/G30 Epic

#### [PLA] v1.2.1 merge gate 198 commits (2026-06-11, 102차 — TSR 307~308 · **FE BLOCK** · **superseded by 103차**)

- FE **`5c0d83d`** 110 ahead · WT **DIRTY 2M** → merge **BLOCK** (QA-B37 upload guard WIP)
- BE **`970c7af`** 88 ahead · WT **CLEAN** → merge **ready**
- **52 route·74 page** · **601/601·532/532 PASS** · **모듈 76.67%**
- **COD 선행**: QA-B37 2M 커밋 → FE WT clean → tester merge **198**

#### [PLA] v1.2.1 merge gate 187 commits (2026-06-11, 101차 — TSR 295~296 · ★ **FULLY UNBLOCKED** · **superseded by 102차**)

- FE **`c1d9788`** 104 ahead · WT **CLEAN** → merge **ready**
- BE **`1af5b1f`** 83 ahead · WT **CLEAN** → merge **ready**
- **52 route·74 page** · **574/574·520/520 PASS** · **모듈 75.77%**
- **tester merge(187)** 즉시 가능 — QA Open 0건 · QA-B34/B35 Fixed

#### [PLA] v1.2.1 merge gate 176 commits (2026-06-11, 100차 — TSR 283~284 · ★ **FULLY UNBLOCKED** · **superseded by 101차**)

- FE **`0024c88`** 98 ahead · WT **CLEAN** → merge **ready**
- BE **`ed730a2`** 78 ahead · WT **CLEAN** → merge **ready**
- **52 route·74 page** · **558/558·510/510 PASS** · **모듈 75.77%**
- **tester merge(176)** 즉시 가능 — QA Open 0건 · QA-B31/B32/B33 Fixed

#### [PLA] G26 레지스트리 ID 충돌 해소 (2026-06-11, 100차 · BNK-71~73)

- **G26** = **7-2-1 의료비공제(연말정산)** P2 (BNK-71·73 확정)
- BNK-44 「치매전담실 5밴드」는 **P3 보류** — BNK-47 정정(시설 사-X = Won't v1) 유지 · 별도 G 코드 **미할당**

#### [PLA] v1.2.1 merge gate 168 commits (2026-06-11, 99차 — TSR 271~272 · ★ **FULLY UNBLOCKED** · **superseded by 100차**)

- FE **`fcf713a`** 93 ahead · WT **CLEAN** → merge **ready**
- BE **`64ebf6e`** 75 ahead · WT **CLEAN** → merge **ready**
- **52 route·74 page** · **547/547·505 PASS** · **모듈 75.77%**
- **tester merge(168)** 즉시 가능 — QA Open 0건 · QA-B24/B26/B27/B28 Fixed

#### [PLA] BNK-68~69 G31·G19·G15 v1.3-C (2026-06-11, 99차 · **신규**)

- **G15 2-1-1/2-9 ✅** @ `a0dcfc0`/`7dfcc9e` · **TSF E2E ✅** @ `88d4c59`/`9dfef92` · **공단 3분리 UI ✅** @ `fcf713a`
- **G7 live guidance ✅** @ `1220bfb`/`0abf164` · **G19 롱텀 통합재가 정본** (BNK-69)
- **신규 G31**(공단 인증서 자동 일정 연동) — Won't v1 · P2 온보딩 가이드 (벤치마크 G25 라벨 → **G31** 확정, G25=본인부담률 엑셀 유지)
- **잔여 P1**: tester merge(168) · G7 실파일(#27) · US-L01 live · G30 Epic · v1.3 live E2E
- **#44**: 거리 단가 **수동 보류** 유지 (BNK-69 2차 교차 0건)

#### [PLA] v1.2.1 merge gate 158 commits (2026-06-11, 98차 — TSR 260~261 · **FE BLOCK** · **superseded by 99차**)

- FE **`08dbcf0`** 88 ahead · WT **DIRTY 4M** → merge **BLOCK** (QA-B24 G7 live guidance WIP)
- BE **`dd7a580`** 70 ahead · WT **CLEAN** → merge **ready**
- **53 route·74 page** · **534/535·497 PASS** · **모듈 75.77%**
- **COD 선행**: QA-B24 4 files **커밋 or revert** → FE WT clean → tester merge **158**

#### [PLA] v1.2.1 merge gate 144 commits (2026-06-11, 97차 — TSR 245~246 · ★ **FULLY UNBLOCKED** · **superseded by 98차**)

- FE **`eef07e5`** 81 ahead · WT **CLEAN** → merge **ready**
- BE **`9d7c17f`** 63 ahead · WT **CLEAN** → merge **ready**
- **49 route·67 page** · **508/508·459 PASS** · **모듈 74.81%**
- **tester merge(144)** 즉시 가능 — QA Open 0건 · QA-B19 Fixed @ `695c0f7`

#### [PLA] BNK-59~61 G15·G29·G30 (2026-06-11, 97차 · **신규** · BNK-58 잔여 일부 해소)

- **G15 서식22 export ✅** @ `7389884` · **제18호 가이드 ✅** @ `eecf0be` · **시간 준수 ✅** @ `eef07e5`
- **V65 계약 무결성 ✅** @ `24733c7` · **QA-B19 geocode UX ✅** @ `695c0f7`
- **신규 G29**(인지활동북)·**G30**(주기별 업무·모니터링) — v3.1 P3 (벤치마크 초안 G23/G24 라벨과 기획 레지스트리 충돌 → G29/G30 확정)
- **잔여 P1**: 2-1-1/2-9 외출 lifecycle · 이동서비스비 청구 · US-L01 은행 8종 live E2E
- **#44**: BNK-47 **수동 보류** 유지

#### [PLA] v1.2.1 merge gate 133 commits (2026-06-10, 96차 — TSR 231~232 · **FE BLOCK** · **superseded by 97차**)

- FE **`6c4c151`** 74 ahead · WT **DIRTY 4M** → merge **BLOCK** (QA-B19 geocode UI WIP)
- BE **`d6d7e7f`** 59 ahead · WT **CLEAN** → merge **ready**
- **48 path·40 page** · **482/482·453 PASS** · **모듈 74.81%**
- **COD 선행**: B19 geocode UI **커밋 or revert** → FE WT clean → tester merge **133**

#### [PLA] BNK-58 G15·G11 v2·QA-B19 (2026-06-10, 96차 · **superseded by BNK-59~61**)

- **G15 2-2/2-3 출석 이원화 ✅** @ `6c4c151`/`d6d7e7f` — US-E06 신규
- **G15 계약 서명 ✅** @ `3c8f9fe`/`9e3cab5`
- **G11 v2 청구 자동 가산 ✅** @ `d7475fd` — US-M05 완료
- **잔여 P1**: geocode failure UX(B19 Planned) · 2-1-1/2-9 외출 lifecycle · 운행일지 DB · US-L01 은행 8종 live E2E
- **#44**: BNK-47 **수동 보류** 유지

#### [PLA] v1.2.1 merge gate 122 commits (2026-06-10, 95차 — TSR 219~220 · ★ **FULLY UNBLOCKED** · **superseded by 96차**)

- FE **`62f022df`** 68 ahead · WT **CLEAN** → merge **unblocked**
- BE **`d5e0e01`** 54 ahead · WT **CLEAN** → merge **unblocked**
- **46 path·40 page** · **467/126·434 PASS** · **모듈 74.81%**

#### [PLA] BNK-53 G11·G15 부분 (2026-06-10, 95차 · **superseded by BNK-58**)

- **G11 catalog+가이드 ✅** @ `904072b`/`3db8db3` — **v2 P1**: 청구 자동 가산 적용 (US-M05)
- **G15 v1.3-C 부분 ✅** @ `3db8db3` — **잔여 P1**: 계약서 서명 저장 API · 탑승(2-2)/출석(2-3) 이원화 · 외출 리포트(2-9)
- **G27·US-L01 bank FE ✅** — BNK-50~52 lineage 재확인 (94차 문서 drift 정정)
- **#44**: BNK-47 **수동 보류** 유지

#### [PLA] v1.2.1 merge gate 110 commits (2026-06-10, 94차 — TSR 207~208 · ★ **FULLY UNBLOCKED** · **superseded by 95차**)

- FE **`c9451a0`** 61 ahead · WT **CLEAN** → merge **unblocked**
- BE **`467cd70`** 49 ahead · WT **CLEAN** → merge **unblocked**
- **46 path·40 page** · **434/434·412 PASS** · **모듈 74.81%**

#### [PLA] BNK-49 G27·US-L01 bank·2-x (2026-06-10, 94차 · **superseded by BNK-53**)

- **G27 BE ✅** @ `a92e625` — **FE·인지지원 676,320 ✅** @ `20bc1be`/`fba5ea8` (BNK-52)
- **US-L01 bank BE+FE ✅** @ `e50533f`/`9ffff0c` (BNK-49·50)
- **US-M03-b ✅** — NHIS import live + 운영 가이드 검증 잔여
- **케어포 2-x**: 탑승/출석 이원화·2-7~2-9 리포트 — **v1.3-C 범위·우선순위** 사용자 확인 필요 (G15)
- **#44**: BNK-47 **수동 보류** 유지 — 공단 매뉴얼 발견 시 재개

#### [PLA] v1.2.1 merge gate 98 commits (2026-06-10, 93차 — TSR 192~196 · ★ **FULLY UNBLOCKED** · **superseded by 94차**)

- FE **`eedcc80`** 55 ahead · WT **CLEAN** → merge **unblocked**
- BE **`0854fbd`** 43 ahead · WT **CLEAN** → merge **unblocked**
- **46 path·40 page** · **413/413·383 PASS** · **모듈 74.81%**

#### [PLA] BNK-45 #44·G2·US-L01 (2026-06-10, 93차 · **신규**)

- **#44**: 「이동지원서비스 시범사업」(동행·3,000원) ≠ 주야간 「이동서비스비」(러-1~4) — **재추적=고시 제34조** · 금액 **830/2,630/4,430/6,230 불변**
- **G2**: templates **5종 partial** @ `0854fbd`/`eedcc80` — **SMTP live 잔여**
- **US-L01**: overpayment guard @ `dd72ff8`/`4109680` — **닫힘**
- **46105**: 케어포 2026 평가 반영 — **G17 v3.1 후보** · ogada **Won't v1** 유지
- **치매전담실 5밴드**: `programType=DEMENTIA_DAY` — **P2** (BNK-44 잔여)

#### [PLA] v1.2.1 merge gate 86 commits (2026-06-10, 92차 — TSR 183·184 · ★ **FULLY UNBLOCKED** · **superseded by 93차**)

- FE **`eb3f0fd`** 48 ahead · WT **CLEAN** → merge **unblocked**
- BE **`f77a268`** 38 ahead · WT **CLEAN** → merge **unblocked**
- **46 path·40 page** · **390/390·371 PASS** · **모듈 74.81%**

#### [PLA] BNK-42 G9·G2 templates·US-J02 (2026-06-10, 92차 · **신규**)

- **G9** `duration_band` **✅** — 25셀·`durationBandSnapshot`·폴백 @ `0c34f85`/`0719648`/`6fe853b`/`5348d9c`/`eb3f0fd` (BNK-41·42)
- **G2** SMTP **templates 3종** @ `f77a268`+원화 `872e040` — **SMTP/메일벤더 실연동 잔여**
- **US-J02** billing filter/dedupe/retry @ `0dc4c4a`/`5348d9c` — QA-B07 #10 **Fixed**
- **#44** **제34조 1차 출처 재추적 P0 BLOCK** — 「별표18」 표기 폐기 · 하드코딩 금지

#### [PLA] v1.2.1 merge gate 75 commits (2026-06-10, 91차 — TSR 172 · **superseded by 92차**)

- FE **`527ba2d`** 41 ahead · WT **DIRTY 2M** (QA-B07 #10) → merge **BLOCK**
- BE **`06d68dd`** 34 ahead · WT **CLEAN** → merge **unblocked**
- **46 path·40 page** · **370/370·359 PASS**

#### [PLA] BNK-38 G9·G21·G2·CMS (2026-06-10, 91차 · **superseded by 92차**)

- **G9** `duration_band` V61 @ `425a05f` — partial committed · fee schedule forward-only @ `06d68dd`
- **G21** billing confirm-lock guide @ `c4fb7ff` + cross-page E2E @ `02cd2b2` — **live run 잔여**
- **G2** `SmtpEmailProvider` committed @ `6ed48ff`/`f23f15a` — **템플릿·실발송 잔여**
- **CMS FE** `/billing/cms` @ `6c6dc7a`/`c0a01b4` — BNK-35 「FE 미구현」 **번복**

#### [PLA] v1.2.1 merge gate 64 commits (2026-06-10, 90차 — TSR 159·160 · ★ **FULLY UNBLOCKED**)
- **관측**: develop FE **34 ahead** · BE **30 ahead** — **양 스트림 WT CLEAN** · TSR 159·160 **신규 Open 0건** · **351/100·350/350 PASS**.
- **판단**: `merge_status: ready` · ★ **FULLY UNBLOCKED** — tester develop→test merge **64 commits** 즉시 가능.
- **잔여**: merge(64) → G7 실파일(#27)·G2 **SMTP/메일벤더**·v2 **CMS FE Route**·G13·US-J02 **live run**·G21 통합 E2E·G9·G11.

#### [PLA] BNK-35 케어포 7-x·CMS·G25 (2026-06-10, 90차 · **신규**)
- **관측**: func.php **111 leaf·32 리포트(28.8%)** · ogada **7-x 8/11** Must~v1.1 · **CMS 7-4 BE stub** @ `2c6e57e` · FE Route ❌ · [공지920](https://web.archive.org/web/20260608120000/https://carefor.co.kr/cs/view_notice.php?cscmgno=920) 본인부담률 엑셀→7-1 재계산.
- **판단**: **G25 본인부담률 엑셀 업로드 P2** · **v2 CMS FE Route P1** — BE skeleton 활용.
- **미확정**: FCMS 실연동 벤더·약정(#33 연계) · 공지920 엑셀 컬럼 스펙(파일럿 샘플).

#### [PLA] G2 email skeleton 닫힘 (2026-06-10, 90차 — BNK-34·35 · **partial**)
- **관측**: BE `StubEmailProvider`·`NotificationService` email-first @ `fbedcc3`/`6eba2ef` — 엔젤 법정서식 3종(기록지·명세·가정통신문) 패리티 방향.
- **판단**: **G2-n 이메일 채널 skeleton `[x]`** — **SMTP/메일벤더·템플릿·실패처리 잔여**(P1).
- **미확정**: 이메일 vs 알림톡 우선(#33) · 운영 발송 벤더(SendGrid/SES/국내).

#### [PLA] US-M02-c 7위젯 닫힘 (2026-06-10, 90차 — BNK-33·35 · **닫힘**)
- **관측**: BE `overdueCount` @ `f755428` · FE `mapBranchDashboardSummary` @ `20bfac1`/`1c20d17` — 케어포 대시보드 미납 위젯 패리티.
- **판단**: **US-M02-c v1.2.1 Must `[x]`** — 대시보드 **7 StatCard** 실데이터 완성.

#### [PLA] G13 cross-page E2E hardening (2026-06-10, 90차 — BNK-35 · **partial**)
- **관측**: `pilotLiveApi.e2e.test.js`·`c72e9df` cross-page live billing hardening · `e6df92c` paid-state normalize.
- **판단**: fetch-mock·harness **진전 `[x]`** — **live run post-merge 권장**(결정 73).

#### [PLA] v1.2.1 merge gate 52 commits (2026-06-10, 89차 — TSR 147·148 · ★ **FULLY UNBLOCKED**)
- **관측**: develop FE **28 ahead** · BE **24 ahead** — **양 스트림 WT CLEAN** · TSR 147·148 **신규 Open 0건**.
- **판단**: `merge_status: ready` · ★ **FULLY UNBLOCKED** — tester develop→test merge **52 commits** 즉시 가능.
- **잔여**: merge(52) → G7 실파일(#27)·G2 **이메일** 실발송·G13 cross-page·G21 통합 E2E·live E2E.

#### [PLA] G13 US-L02 pagination E2E 부분 닫힘 (2026-06-10, 89차 — BNK-31 · **partial**)
- **관측**: `OverduePage` pagination·reminder E2E @ `fed457f` · reminder timestamp sync @ `14e9066` · BE overdue pagination+guardian @ `4ee652d`.
- **판단**: **US-L02 fetch-mock E2E `[x]`** — **cross-page 상태전이 live E2E**만 잔여(P1).
- **경쟁사**: 케어포 7-3 미납 관리·독려 — 패리티 진전.

#### [PLA] G21 visit import 파서 (2026-06-10, 89차 — BNK-31 · **partial**)
- **관측**: `NhisVisitScheduleExcelParser` 한국어 날짜/시간 변형 @ `7fbd219` — 공단 엑셀 포맷 편차 대응.
- **판단**: G21 **파서 `[x]`** — **통합 E2E·실파일 검증** 잔여(P1).
- **잔여**: US-V04 live E2E · G7 실파일(#27) 연계.

#### [PLA] v3 meals/programs FE POST 닫힘 (2026-06-10, 89차 — BNK-30·31 · **닫힘**)
- **관측**: `/meals`·`/programs` POST menus·records·schedule·participations FE @ `6a59b74` — 케어포 6-1·5-2 기본 CRUD 패리티.
- **판단**: G5 **v3 FE 연결 `[x]`** — 5-3~5-10·리포트·집계는 **v3.1**(결정 94).

#### [PLA] G2 이메일 채널 P1 (2026-06-10, 89차 — BNK-29·31)
- **관측**: 엔젤 **월1회 기록지·명세·가정통신문 이메일** 자동발송 — ogada G2-n notify API+UI는 **실채널 없음**.
- **판단**: v1.1/v2 **이메일 채널 P1** — 알림톡/SMS와 병행 검토(PLAN_NOTES #33 연계).
- **미확정**: 이메일 vs 알림톡 우선 채널(#33).

#### [PLA] v1.2.1 merge gate 40 commits (2026-06-10, 88차 — TSR 135·136 · **superseded by 89차**)
- **관측**: develop FE **21 ahead** · BE **19 ahead** — **양 스트림 WT CLEAN** · TSR 135·136 **신규 Open 0건**.
- **판단**: `merge_status: ready` · ★ **FULLY UNBLOCKED** — tester develop→test merge **40 commits** 즉시 가능.
- **잔여**: merge(40) → G7 실파일(#27)·G2-n 실발송·US-V04 live E2E·live E2E.

#### [PLA] G21 확정↔import P1 닫힘 (2026-06-10, 88차 — BNK-28 · **닫힘**)
- **관측**: BE `hasBlockingConfirmedPlan` @ `84f3441` · FE 확정↔import 가이드 @ `bf3d40d` · `VisitNhisImportPanel` @ `60cea98`/`311c7c0`.
- **판단**: US-V02 확정↔import **P1 `[x]`** — **US-V04 live E2E**·청구일정 import 확장(#45) 잔여.

#### [PLA] G2 보호자 명세 notify (2026-06-10, 88차 — BNK-28 · **partial**)
- **관측**: `POST /billing/claims/{id}/notify` @ `84f3441` · billing notify UI @ `c48fb67`.
- **판단**: **G2-n API+UI 골격 `[x]`** — **실채널(알림톡/SMS) v1.1/v2(US-J03)** 잔여.

#### [PLA] v1.2.1 merge gate 27 commits (2026-06-10, 87차 — TSR 123·124 · **superseded by 88차**)
- **관측**: develop FE **15 ahead** · BE **12 ahead** — **양 스트림 WT CLEAN** · TSR 123·124 **신규 Open 0건**.
- **판단**: `merge_status: ready` · ★ **FULLY UNBLOCKED** — tester develop→test merge **27 commits** 즉시 가능.
- **잔여**: merge(27) → G7 실파일(#27)·US-V04 import FE·live E2E.

#### [PLA] v1.2.1 merge gate 17 commits (2026-06-10, 86차 — TSR 116 · **superseded by 87차**)
- **관측**: develop FE **11 ahead** · BE **6 ahead** — FE **WT DIRTY 9** · BE **WT DIRTY 26** · TSR 116 **신규 Open 0건**.
- **판단**: `merge_status: ready` 유지 · **merge 실행 전 양 스트림 WT clean** 필수(이관 규율 1·5).
- **잔여**: WT clean → merge **17** → G7 실파일(#27)·live E2E.

#### [PLA] US-J03-h 알림 발송 이력 닫힘 (2026-06-10, 86차 — BNK-22 · **닫힘**)
- **관측**: `NotificationHistoryPanel` @ `e39164d` — 케어포 **10-7 안내발송내역(문자, 이메일)** 패리티 · PIPA 연락처 비표시.
- **판단**: **US-J03-h v1.2.1 Must `[x]`** — **실발송 채널(케어포 10-1)** 은 **v1.1/v2(US-J03)** 잔여.
- **모듈 커버**: 72.5% 불변 — 발송 연동 완료 시 **~74.4%** 예상(BNK-22 §25-4).

#### [PLA] G7 엑셀 import = 업계 표준 (2026-06-10, 84차 — BNK-20 · **전략 확정**)
- **관측**: 이지케어 [ezCare_fnc.html](https://ezcare.easyms.co.kr/new/ezCare_fnc.html) — **RFID 실시간 공단연동 2016.03.28 종료→엑셀파일 연동** (BNK-20 §23-5).
- **판단**: ogada G7 **엑셀 중심 NHIS import**는 레거시가 아닌 **업계 현행 표준** — `처리상태`열 파싱·`PENDING_REVIEW` 자동분류는 **차별 포인트** 유지.
- **영업 메시지**: 「공단 실시간 연동 없음」은 **약점 아님** — 케어포·이지케어 동일 패러다임.

#### [PLA] G11 가산수가 자동계산 (2026-06-10, 84차 — BNK-20 · **P1 v1.1**)
- **관측**: 이지케어 일정·본인부담 양면 「**(가산)수가 자동계산**」 마케팅 명시(BNK-20 §23-3).
- **판단**: 파일럿 1밴드·가산없음은 정당화되나 **영업 시 경쟁사 표준 기대치** — ROADMAP **v1.1~v2 G11**.
- **미확정**: 파일럿 센터 야간·휴일 가산 발생 빈도(#35 연계).

#### [PLA] 대시보드 `pendingReviewCount` 위젯 (2026-06-10, 83차 — BNK-19 · **84차 닫힘**)
- **관측**: `ReconciliationPage` **`StatCard label="대기(보류)"`** + `batch.pendingReviewCount` **✅** · `DashboardPage`·`dashboardSummary.js` **`nhisPendingReviewCount`** @ `1794e1c` **✅**.
- **판단**: **US-M02-b 닫힘** — BNK-20 §23-1 「2사이클 미착수」 갭 **해소**(coder `1794e1c`).
- **구현**: NHIS import 배치 API `pendingReviewCount` 합산 — `sumPendingReviewNhisFromBatches` (클라이언트 집계).

#### [PLA] G7 NHIS `PENDING_REVIEW` enum (2026-06-09, 82차 — BNK-18 · **UX 닫힘**)
- **관측**: BE+FE **3상태 UX 닫힘** @ `4cc328d`/`dd49204`/`fbb0b7a`/`16402b2` — `Badge`·`NhisReconciliationTable`·`NhisPendingReviewGuide`·`ReconciliationPage.pendingReviewCount`·`pilotPageFlows` G7 E2E.
- **판단**: 케어포 **성공/오류/대기 3상태** + 박스 4색 **패리티 달성** — BNK-18 §21-2 · BNK-19 **재확인**.
- **잔여**: ① 파일럿 센터 **실파일** NHIS 엑셀 (#27) ② **대시보드 `pendingReviewCount`** — **P1** (83차 상향).

#### [PLA] v1.2.1 merge gate 16 commits (2026-06-10, 84차 — **BE WT clean 선행**)
- **관측**: develop FE **10 ahead** · BE **6 ahead** — FE **WT CLEAN** @ `1794e1c` · BE **WT DIRTY 17**(meals/programs·V55·Client/Visit).
- **판단**: `merge_status: ready` 유지 · **merge 실행 전 backend WT clean** 필수(이관 규율 1·5).
- **잔여**: BE WT clean → merge **10+6** → G7 실파일·live E2E.

#### [PLA] v1.2.1 merge gate 15 commits (2026-06-10, 83차 — TSR 114 · **superseded by 84차**)
- **관측**: develop FE **9 ahead** · BE **6 ahead** — FE **WT DIRTY 3U**(v3 forms) · BE **WT DIRTY 15**(meals/programs·V55).
- **판단**: `merge_status: ready` 유지 · **merge 실행 전 develop WT clean** 필수(이관 규율 1·5).
- **잔여**: WT clean → merge **9+6** → G7 실파일·`pendingReviewCount`·live E2E.

#### [PLA] v1.2.1 merge gate 14 commits (2026-06-09, 82차 — TSR 113 · **superseded by 83차**)
- **관측**: develop FE **8 ahead** · BE **6 ahead** of test — **양 스트림 WT CLEAN** · TSR 113 **merge gate FULLY UNBLOCKED**.
- **판단**: tester develop→test merge **8+6** ff 가능 — v2 `/visits`·G7 PENDING_REVIEW **develop-only bleed** 동반 promote(결정 92).
- **잔여**: merge 후 G7 실파일·live E2E(결정 73).

#### [PLA] G7 NHIS `PENDING_REVIEW` enum (2026-06-09, 81차 — BNK-17 · **superseded by 82차**)
- **관측**: BE **`PENDING_REVIEW`** + `match_status_reason` @ `4cc328d` V54 **커밋** · FE `NhisReconciliationTable`·`Badge` **WT 4 files WIP**.
- **판단**: DB enum **확정** — UI·파일럿 샘플·배치 집계 3상태 UX **잔여**.
- **미확정**: 파일럿 센터 NHIS 엑셀 실파일 확보 시점 (#27).

#### [PLA] #44 이동서비스비 러-1~4 2차 교차 확정 (2026-06-09, 87차 — BNK-25 · **81차 충돌 해소**)
- **관측**: angelsitter 공단 매뉴얼 #235 + 블로그 교차 — **830/2,630/4,430/6,230원**(5/10/20km·1일1회) · BNK-9 정합 · **BNK-17(2,630/2,630/5,230/7,850) 폐기**.
- **판단**: `transport_service_fee` 시드 **구조 설계 가능** — **상수 하드코딩 금지** 유지 · **별표18 HWP 1차 추출만 잔여**.
- **미확정**: MOHW 제2025-247호 별표18 HWP/PDF 1차 금액 추출(law.go.kr `flSeq=26492443`은 급여제공기록지 서식만 노출).

#### [PLA] #44 law.go.kr 이동서비스비 2차 출처 충돌 (2026-06-09, 81차 — BNK-17 · **superseded by 87차**)
- **관측**: BNK-9 2차 **830/2,630/4,440/6,240원** vs BNK-17 2차(angelsitter) **2,630/2,630/5,230/7,850원** — 구간·금액 **모두 불일치** · law.go.kr 1차 **여전히 미확인**.
- **판단**: `transport_service_fee` 시드·v1.3-C **BLOCK** — **상수 하드코딩 금지** 재확인.
- **미확정**: 1차 출처(law.go.kr TLS·고시 admRulSeq) 확정 전 구현 착수 **금지**.

#### [PLA] G2 CMS 효성CMS(FCMS) (2026-06-09, 81차 — BNK-17)
- **관측**: 엔젤·케어포 CMS 백엔드 = **효성CMS(FCMS)** 계열 — ogada G2 v2는 자체 구축 대신 **FCMS API 커넥터** 검토.
- **미확정**: FCMS 계약·API 키·수수료 구조 — 영업/운영 입력 대기.

#### [PLA] Epic V FE develop bleed (2026-06-09, 81차 — BNK-17)
- **관측**: `/visits` FE @ `371794f` — v1.2.1 merge **전** v2 Epic V 착수(결정 92 대비 bleed).
- **판단**: develop-only 허용 · merge gate **6+5** 일괄 · E2E·import는 **post-merge** 우선.
- **미확정**: v1.2.1 P1(G7) 완료 전 Epic V 추가 착수 범위 — coder 우선순위 G7 FE > merge.

#### [PLA] G7 NHIS 대기(보류) 3상태 UX (2026-06-09, 80차 — BNK-15·16 · **superseded by 81차**)
- **관측**: 케어포 NHIS import = **성공/오류/대기 3상태** + 박스 4색 상태코딩(BNK-15 §18-4) · ogada US-G06 = MATCHED/DISCREPANCY/UNMATCHED(행 단위) — 배치 **집계 2상태**.
- **판단**: G7 **P0** — 파일럿 샘플 확보 시 **「대기(보류)」** 상태·오류 원인 가이드(해당월·미등록 수급자) 추가 검토.
- **미확정**: ~~`PENDING`/`ON_HOLD` DB enum~~ → **`PENDING_REVIEW` V54 확정** @ `4cc328d`.

#### [PLA] v1.2.1 merge gate 11 commits (2026-06-09, 81차 — BNK-17·TSR 110·111)
- **관측**: develop FE **6 ahead** · BE **5 ahead** of test — P0+US-M03 완료 · FE **WT DIRTY 4**(G7 WIP).
- **판단**: tester develop→test merge **6+5** — G7 FE 커밋 후 WT clean **권고**.
- **잔여**: merge 후 G7 샘플·G13·live E2E.

#### [PLA] 7-2-1 연말정산·7-9 환불대장 (2026-06-09, 80차 — BNK-16)
- **관측**: US-M03 닫힘 후 본인부담 7-x 잔여 = **7-2-1**(연말정산·의료비공제)·**7-9**(환불대장)만.
- **판단**: v1.2.1 **범위 외** · **Could** — 파일럿 센터가 월말 필수로 쓰는지 사용자/센터장 입력 대기.
- **가정**: v2 또는 v1.2.1 post-merge 후순위.

#### [PLA] v1.2.1 merge gate 9 commits (2026-06-09, 80차 — BNK-16·TSR 109)
- **관측**: develop FE **5 ahead** · BE **4 ahead** of test — P0+US-M03 완료 · **`merge_status: ready`** 유지(결정 92).
- **판단**: tester develop→test merge **5+4** 일괄 — v2 G21 bleed(`d768820`·`1812165`) 포함.
- **잔여**: merge 후 G7·G13·live E2E.

#### [PLN] v1.3-A live backend E2E (2026-06-09, 75차 갱신)
- **관측**: develop/test/origin **`598d108`**/`c7c8f07` 동기화(75차) · harness @ `d484206`+ **PRESENT**.
- **잔여**: live Bearer JWT backend 연동 E2E **run** — **`LIVE_E2E=1`** · **결정 73 post-merge 권장**(merge-blocking **아님**).
- **v1.3 `merge_status: merged`**: test **`c7c8f07`**(origin 동기화) — operation 승격 **가능**(backend WT 13·v1.2.1 잔여 병행).

#### [PLA] v2 G21 backend bleed vs 결정 92 (2026-06-09, 78차 재확인)
- **관측**: backend develop **`d768820`** — v2/G21 visits **선행 커밋** · v1.2.1 P0(G14 GET API) **미완** — **77차 대비 불변**.
- **판단**: merge gate **v1.2.1 P0 후**(결정 92) — bleed는 **develop-only** 허용 · tester merge 시 **4 commits** 일괄.
- **미확정**: coder가 v2 backend를 v1.2.1 P0 **전** 추가하는 워크플로 **허용 여부** — 현재 관측 1회(78차 재확인).

#### [PLA] G14 GET API vs 케어포 1-9 전수 리포트 (2026-06-09, 76차 — BNK-14)
- **관측**: 케어포 1-9 = **전 수급자 등급변동 현황 리포트** · ogada = **개별 이용자 등급 탭**만 @ `6d0a03a`.
- **판단**: v1.2.1 P0 = **`GET /ltc-grade-history`** · 전수 리포트 Route = **US-M01-b v2 검토**.
- **미확정**: 파일럿 센터가 전수 리포트를 월말 필수로 쓰는지 — 사용자/센터장 입력 대기.

#### [PLA] v1.2.1 develop-only 패리티 (2026-06-09, 76차 — BNK-14)
- **관측**: develop **`6d0a03a`**/**`2012945`** · 모듈 **~68.7% PASS** · US-M02 **닫힘** · G14 **GET API 잔여**.
- **판단**: P0 = **G14 GET API 1건** · P1 = **G22 7-6~10**(US-M03) · 케어포 1-9 전수 리포트 = **v2 검토**.
- **범위**: ROADMAP v1.2.1 · **G20 Won't v1**.

#### [PLN] v1.2.1 develop-only 패리티 (2026-06-09, 75차 — BNK-12)
- **관측**: develop/test/origin **`c7c8f07`** 동기화(75차) · 모듈 **~74–78% PASS** · 잔여 P0 **G14(US-M01)·US-M02 실데이터**.
- **판단**: merge gate **해소** — ROADMAP v1.2.1 **`in_progress`** · API_SPEC §4-2 `ltc_grade_history` 명세 확정.
- **범위**: ROADMAP v1.2.1 표 참조 · **G20 Won't v1**(BNK-11 demo-work 시설 메뉴).

#### [PLN] origin/test push gap (2026-06-09, 75차 — **해소**)
- **관측**: backend·frontend develop/test/origin **동기화** @ `598d108`/`c7c8f07` — **0 ahead**.
- **판단**: QA-B12·SEC-D14 **Fixed** — operation 승격·원격 CI 차단 **소멸**.
- **잔여**: backend WT 13 files · v1.2.1 구현 · v1.3 live E2E run.

#### [PLN] 이지케어 계획/청구 이중 일정 (2026-06-09, 74차 — BNK-10 #45)
- **관측**: 이지케어 **계획일정**(안내) vs **청구일정**(정산) **2회 import** — ogada는 NHIS import **1회**.
- **판단**: ogada **주간 출석 중심** — 방문요양 확장 전 **Won't**. 파일럿은 단일 import 유지.
- **미확정**: 다지점 법인이 방문+주야간 혼합 운영 시 이중 UX 필요 여부 — 사용자 입력 대기.

#### [PLN] origin/test push gap (2026-06-09, 73차 — **75차 Fixed**)
- **관측(73차)**: 로컬 test = develop @ **`598d108`** · origin/test @ **`2799e29`** — **26커밋 STALE**.
- **75차 해소**: origin/test push·frontend merge 완료 — QA-B12·SEC-D14 Fixed.

#### [PLN] v1.3-A live backend E2E (2026-06-08, 72차 갱신 — superseded by 73차)
- **관측**: `pilotPageFlows` transport US-T01~T03 fetch-mock E2E @ `637b9b3`+ · T03 contact masking E2E @ `1d910c2`+ · masking 단위테스트 @ `32575aa` **HEAD PRESENT**. Clients transport profile @ `1ec538b`+ · pickup address/contact masking API @ `e7d4cf6`/`c7941e9` · UI @ `37be0a3`+/`1d910c2`+ · `ClientFormPage` 픽업 프로필 @ `3c55339` **HEAD PRESENT**(TSR 96~99차).
- **잔여**: live Bearer JWT backend 연동 E2E **run** — harness @ `d484206`+ **PRESENT** · **결정 73 post-merge 권장**(merge-blocking **아님**).
- **v1.3 `merge_status: ready`**: merge-blocking **충족** — develop→test merge(25+20) + live E2E run은 post-merge 권장.

#### [PLN] 다중 in_progress 버전 우선순위 (2026-06-08, 65차 — COD 충돌 해소 · 68차 baseline 갱신)
- **관측**: ROADMAP에 v1.3·v2·v3가 동시 `in_progress` — 「단일 in_progress」규칙과 표면 충돌.
- **65차 planner 결정**: **frontend coder 단일 활성 = v1.3-A**(`pilotPageFlows` transport merge-blocking). v2·v3 frontend **신규 착수 보류**. backend **merge(23) 최우선**.
- **baseline**: backend **`c7941e9`** · frontend **`1d910c2`** — ROADMAP·PLAN_NOTES **70차 동기화**.

#### [PLN] FE-15 bundle code-split 회귀 (2026-06-08, 65차 — TSR 91 LOW → **67차 해소**)
- **관측**: `8a764df` UXD-48 Recharts 통합 후 build 단일 JS **756 kB** — v1.2 FE-15 `manualChunks`(<500 kB) **회귀**.
- **67차 해소**: `d484206` — `manualChunks` 복원 · 3청크(max **367 kB <500 kB**) · TSR 93차 독립 검증 PASS.
- **판단**: **non-blocking LOW** — merge 게이트·v1.3 transport E2E **차단 아님**.
- **후속**: v1.2.1 — `vite.config.js` `manualChunks` recharts·vendor 재분리.

#### [PLN] v3 StaffPage 완전 기능 범위 미확정 (2026-06-08, 65차 갱신)
- **관측**: `73f7d39`+ StaffPage v3 UI·`8a764df` Recharts develop 진입. **65차: v3 frontend 신규 착수 보류** — v1.3 merge gate 선행.
- **미확정 항목**:
  - 직원 정보 CRUD API 엔드포인트 스펙 (`/api/v1/staff/*` 또는 기존 `users` 재활용 여부)
  - 근태(출퇴근) 기록 — 별도 테이블 vs `attendance_records` 유사 패턴
  - 직원 앱/모바일 뷰 필요 여부 (케어포 §8-4 방식)
- **가정**: API_SPEC v3 직원 섹션 확정 전까지 frontend UI shell 유지, backend API는 v3 merge-blocking 완료 기준 충족 시 함께 merge.

#### [PLN] v1.3-A unconfirm 프론트 UI — **해소 @ `73f7d39`** (2026-06-08, 64차 · 66차 E2E 갱신)
- **관측**: backend `767d977`+ PATCH+POST · frontend `TransportUnconfirmModal`·`TransportRunDetailPage` unconfirm·Vitest 3건 **HEAD PRESENT**. **`pilotPageFlows` transport @ `637b9b3` HEAD PRESENT**(TSR 92차).
- **잔여**: live backend 연동 E2E(결정 73 post-merge 권장).
- **v1.3 merge_status: ready** 판단: live E2E 계획 확정 또는 post-merge 합의 후 coder 설정.

#### [PLN] ogada workspace submodule 드리프트 (2026-06-08, 44차)
- **관측**: `src/backend` develop **`3f9264f`** · test **`2799e29`** · WT **CLEAN** · **3 ahead**. `src/frontend` develop **`c3b863e`** · test **`e5fd48d`** · WT **CLEAN** · **5 ahead** (`7c0ecdc`·`1d9a701`·`e043eac`·`f506c90`·`c3b863e`).
- **43차 대비**: frontend `e043eac`→`c3b863e`(+2 COD 커밋) · FE-18/FE-19 Fixed · merge gap 3→**5**.
- **권고**: d5654c0 checkout **금지** · `c3b863e` lineage 위 v1.1 Must API·P1–P8 재구현 후 merge.

#### [PLN] ogada workspace submodule 드리프트 (2026-06-08, 42차)
- **관측**: `src/backend` develop **`f47ffa1`**(+1 vs test) · test **`2799e29`(stale)** · WT **CLEAN** · develop **89/89**·test **79/79**. `src/frontend` develop·test **동일 `@e5fd48d`(스켈레톤)** · TSR57 **`d5654c0` 18 behind** · WT **DIRTY**(auth WIP, TSR59).
- **58·59차 대비 41차 변화**: backend stale `2799e29`→develop **`f47ffa1` CLEAN**(B09 Fixed) · frontend 여전히 **`e5fd48d`** · **신규 QA-B10·SEC-D12·QA-B11**.
- **권고**: **INFRA-B12** — frontend **`git checkout d5654c0`** + backend **BE-10**/#42 baseline 결정 후 FE-19→FE-18→merge.

#### [PLN] ogada workspace submodule 드리프트 (2026-06-08, 41차)
- **관측**: 40차와 **완전 동일** — `src/backend` @ **`2799e29`** · WT **9U**(V35~V43 migrations only, TSR 56 J01 **27 files 미반영**) · `src/frontend` @ **`e5fd48d`** · WT **CLEAN**.
- **41차 추가**: BNK-7 G15/G16 문서화 완료 — **submodule·BLOCK·coder 우선순위 변경 없음**.
- **권고**: `git submodule update --init --recursive` → backend **`428ba7d`** · frontend **`d5654c0`**. FE-19→FE-18→BE-8.

#### [PLN] ogada workspace submodule 드리프트 (2026-06-08, 40차)
- **관측**: ogada 루트 `git submodule status` — `src/backend` HEAD **`2799e29`**(stale, TSR 56 **`428ba7d`** 불일치) · WT **9 untracked migrations**(V35~V43, DBA round 57~58·TSR 56 J01 27 files와 **다름**) · `src/frontend` **init 완료** @ **`e5fd48d`**(stale, TSR 57 **`d5654c0`** 불일치) · WT **CLEAN**(FE-18·FE-19 WIP **미반영**).
- **39차 대비**: frontend 디렉터리 부재 → **init 복구**. backend WT 8U→9U(V43 추가). BLOCK·우선순위 **불변**.
- **영향**: TSR 56·57·SEC 4차 재검증·coder FE-19/BE-8 작업 **여전히 불가** — develop HEAD checkout 전까지 기획 baseline만 유효.
- **권고**: coder/운영 — `git submodule update --init --recursive` 후 **backend `git checkout 428ba7d`**·**frontend `git checkout d5654c0`**. FE-19→FE-18→BE-8 순서 유지(38차).

#### [PLN] ogada workspace submodule 드리프트 (2026-06-07, 39차)
- **관측**: ogada 루트 `git submodule status` — `src/backend` HEAD **`2799e29`**(초기 구현, TSR 56 **`428ba7d`** 불일치) · WT **8 untracked migrations**(V35~V42, TSR 56 J01 27 files와 **다름**) · `src/frontend` **디렉터리 없음**(submodule index `-e5fd48d`, TSR 57 **`d5654c0`** 불일치).
- **영향**: TSR 56·57·SEC 4차 재검증·coder FE-19/BE-8 작업 **불가** — submodule checkout 전까지 기획 baseline만 유효.
- **권고**: coder/운영 — `git submodule update --init --recursive` 후 backend·frontend 각 develop 최신 checkout. frontend 복구 후 FE-19→FE-18→BE-8 순서 유지(38차).

#### [PLN] 사용자 결단 — build 실행·L1 매턴·dirty-tree 정리 (2026-06-07)
- 사용자 지시: "실행하고 매턴 켜 정리도 선행작업으로 진행하고"
- 조치 요청 (planner → coder):
  1. 즉시 build 실행(사용자 승인에 따름) — coder는 `INFRA-1~3` 착수 지시를 받음.
  2. L1 게이트를 coder의 매 턴마다 항상 활성화하도록 적용(턴 종료 후 working tree 검사).
  3. frontend dirty-tree 정리(우선: B07 #6, B09 관련 커밋)를 build/merge 전 선행 작업으로 수행.
- 추적: 해당 지시는 `docs/planning/REQUIREMENTS.md` §8-2에 기록됨(플래너 문서화). 사용자 승인 마커는 플래너가 추가하지 않음.

#### [PLN] 빌드 실패 처리 규칙 (2026-06-07)
- 사용자 지시 반영: 빌드 실패 시 coder는 실패 로그와 원인 요약을 남기고, 수정 브랜치 또는 이슈를 생성하여 수정 후 재시도를 수행해야 한다.
- 보고 항목: 실패 로그(마스킹된 경우 표기), 원인 요약, 임시 조치, 수정 브랜치/PR 링크, 재시도 결과, 미해결 시 에스컬레이션 시점.
- 기록 위치: `PLAN_NOTES.md` 회고 섹션 및 `INFRA-1-start` TODO 업데이트.

#### [PLN] 자동 에스컬레이션 및 실패로그 관리 (2026-06-07)
- 자동 에스컬레이션 주기: 12시간(사용자 확정). 실패가 지속될 경우 12시간 간격으로 planner 및 운영 담당자에게 에스컬레이션.
- 실패 로그 관리: GitHub 우선 사용 권장
  1. CI(예: GitHub Actions) 빌드에서 실패 로그를 빌드 아티팩트로 저장.
  2. `INFRA-1-start` TODO 또는 전용 GitHub 이슈에 아티팩트 링크와 마스킹된 요약을 첨부.
  3. 수정 브랜치/PR 생성 시 해당 이슈에 연결하고 PR 코멘트에 빌드 재시도 결과를 추가.
- 보안: 로그 제출 전 시크릿·토큰 마스킹 필수.

#### [PLN] dirty-tree 정리 정책 (2026-06-07)
- 정리 주기: 24시간(사용자 지시). coder는 24시간 내에 develop의 dirty 상태를 해소할 것.
- 권장 절차:
  - 필요한 변경은 의미 있는 작은 커밋으로 정리.
  - 임시 변경은 `git stash` 또는 별도 `wip/<short-desc>` 브랜치로 이동.
  - 불필요 변경은 `git restore --staged` / `git checkout -- <file>`로 되돌리기.
  - 정리 완료 후 `FE-dirty-tree-clean` TODO에 조치 내역(커밋/스태시/브랜치 링크) 보고.

#### [PLN] GitHub 이슈 기반 CI 실패 티켓 자동화 (2026-06-07)
- 추가된 파일:
  - `.github/ISSUE_TEMPLATE/ci-failure.md` — CI 실패 이슈 템플릿
  - `.github/workflows/ci-failure-issue.yml` — 워크플로 실패 시 자동 이슈 생성
  - `.github/workflows/ci-escalation.yml` — 12시간 주기 자동 에스컬레이션(스케줄)
- 동작 요약:
  - CI 워크플로가 완료되고 상태가 `success`가 아니면 자동으로 `ci-failure` 라벨 이슈를 생성합니다.
  - 생성된 이슈는 CI 실패 메타(워크플로 이름, 브랜치, 커밋, Run URL, Logs URL)를 포함합니다.
  - 스케줄 워크플로는 12시간마다 열린 `ci-failure` 이슈를 검사하고, 마지막 업데이트가 12시간 이상이면 코멘트로 에스컬레이션 문구를 남기고 `escalated` 라벨을 추가합니다.
- 주의:
  - 빌드 로그는 CI에서 artifact로 업로드 후 이슈에 링크하여 관리하세요(로그 마스킹 필수).
  - 필요 시 워크플로/이슈 템플릿을 운영팀 요구에 맞춰 확장합니다.

#### [PLN] 2026-06-07 검토 기록 — 작업 시작 요청 (플래너 조치)
- 검토 시각: 2026-06-07T03:44Z (UTC)
- 작업 내용:
  1. 로컬 리포지토리 상태 점검: `git status --porcelain` 결과 다수의 수정(M)·삭제(D) 항목 및 untracked 파일 존재(특히 `.git.accidental-*`, `.git.disabled-*` 항목 다수).
  2. 현재 CI/빌드 실행 프로세스는 발견되지 않음(진행 중 빌드 없음).
  3. 이상 소견:
     - `.git.accidental-*` / `.git.disabled-*` 관련 항목이 다수 삭제(D)로 표시됨 — Git 메타데이터 관련 불명확 상태로, 실수로 생성된 임시/백업 git 폴더가 커밋/제거 이력에 남아 있음. coder는 이 상태가 의도된 것인지 확인 후 불필요 파일 정리 필요.
     - `src/frontend` 관련 변경(원래 보고된 dirty-tree) 여전히 존재함(편집된 docs·frontend WIP 파일 다수).
  4. 플래너 조치: coder에게 즉시 작업 시작 요청(이미 TODO로 등록됨). 우선순위:
     - (A) `.git.accidental-*` / `.git.disabled-*` 항목 원인 확인 및 안전한 정리(삭제 또는 .gitignore·복구).
     - (B) frontend dirty-tree 정리(B07 #6, B09 우선) — 24시간 내 정리.
     - (C) 빌드 실행 및 결과 보고(성공/실패 로그 + 실패 시 이슈 생성).
  5. 기록 위치: 이 항목은 `FE-dirty-tree-clean` 및 `INFRA-1-start` TODO 업데이트와 함께 회고에 누적됩니다.

#### 배차(지도) 정책: 확정 (2026-06-15)

- **서버 Geocoding REST 프록시는 사용하지 않음** — 주소→좌표는 **카카오맵 JS SDK `Geocoder`** 가 브라우저에서 수행.
- **경로 폴리라인**: 카카오 Mobility Directions API (`/api/v1/transport/route-preview`) — 좌표는 FE Geocoder 결과를 전달.
- **자동 배차 제안(v1.3-B)**: 서버 최적화 입력으로 `clients.pickup_lat`/`pickup_lng` 가 저장된 이용자만 포함(없으면 수동 배차 안내).
- **임시 저장/확정**: geocode 실패로 저장 차단하지 않음 — 주소는 필수, 지도는 클라이언트 Geocoder에 의존.
- **API 키**: `VITE_KAKAO_MAP_JS_KEY`(지도·Geocoder), `KAKAO_REST_KEY`(Directions only).

#### 타겟·운영 범위

1. ~~**대상 센터 규모**~~ → **확정**: **다지점** 운영, 지점별·통합 관리 구분
2. ~~**MVP 사용자**~~ → **확정**: 6개 역할 **전부** 별도 UI·권한 구현
3. ~~**파일럿 운영 센터**~~ → **확정**: **있음**
3-1. ~~파일럿 인원·지점~~ → **확정**: 지점 2, 센터장 1, 요양보호사 5
3-2. ~~파일럿 참여 역할~~ → **확정**: **센터장(`branch_admin`) + 요양보호사(`caregiver`)만**
4. ~~**규모 가정**~~ → **가정 확정**: 전국 SaaS 기준 1년차 ~50법인/~150지점, 3년차 ~500법인/~2,000지점 (REQUIREMENTS §1-2)
5. ~~**hq_admin 쓰기 권한**~~ → **확정**: `active_branch_id` 선택 시 해당 지점 CRUD (B방식)
6. ~~**신규 고객 등록**~~ → **확정**: **A — ogada 직원** (`platform_admin`)

#### 기술 스택 세부

7. ~~**Java 프레임워크**~~ → **확정**: Spring Boot 3.x
8. ~~**React 구성**~~ → **확정**: Vite + React (SPA)
9. ~~**데이터베이스**~~ → **확정**: PostgreSQL
10. ~~**인증 방식**~~ → **확정**: JWT + RBAC (지점 스코프)
11. ~~**기존 `src/backend` 처리**~~ → **확정**: 전부 폐기, Java 신규 시작

#### 기능·우선순위

12. ~~**MVP 기능 범위**~~ → **확정**: Must 전체 + 다지점·조직 관리
13. ~~**청구·정산 v1**~~ → **확정**: MVP v1 **포함**
13-1. ~~청구 MVP~~ → **확정**: 케어포 동일 (**내부계산+명세서+공단엑셀import**)
14. **보호자 알림** 채널 우선순위는? (카카오 알림톡 / SMS / 앱 푸시) — MVP v1 제외
15. ~~**QR 출석**~~ → **확정**: 수기 + QR **모두** MVP 포함
16. ~~**QR 스캔 주체**~~ → **확정**: **B방식** (보호자/이용자 → 지점 QR). A방식 MVP 제외
17. ~~**QR 스캔 계정 정책**~~ → **확정**: **안 3** (`guardian` + `client_user`, `allow_client_self_checkin` on/off)

#### 벤치마킹

18. ~~**벤치마킹 참고**~~ → **확정**: **케어포** (carefor.co.kr). §1-5 1차 조사 반영
19. 벤치마킹 시 **가장 중시하는 비교 축**은? (기능 완성도 / UX / 가격 / 규정 준수 / 모바일 UX)
20. **국내 장기요양 포털·공단 시스템**과의 연동·호환 요구가 있나?

#### 비기능·제약

21. ~~**배포 클라우드**~~ → **확정**: 벤더 **무관** (구현 단계 선택)
22. ~~**동시 접속 규모**~~ → **가정 확정**: 1년차 ~500 / 3년차 ~5,000 (REQUIREMENTS §1-2)
23. **개인정보·의료 데이터** 보관 기간·암호화 정책에 센터 내부 규정이 있나?
24. ~~**예산·일정**~~ → **확정**: 목표 런칭 **일정 무관**
25. **접근성·다국어** 요구는 한국어 단일 + WCAG 2.1 AA로 충분한가?

#### 빌드 전 잔여 공백 (2026-06-05 신규 식별)

26. ~~**청구·정산 계산 규칙 구체화**~~ → **확정** (2026-06-05):
    - 수가 = **관리자 입력 테이블(B방식)**, `hq_admin` 관리, 연도별 버전 (§3-9-1)
    - 본인부담률 = **이용자별 구분**(일반15%/감경9%·6%/기초수급0%) (§3-9-2)
    - 가산·식대·비급여: 수가표 부가 항목으로 **선택 입력** 가능하게 구조화 (세부 항목은 구현 시 확정)
27. **공단 청구내역상세 엑셀 포맷**: import할 엑셀의 실제 컬럼 스펙(샘플 파일) 확보 필요. **3차 벤치마크**: 선행 **`처리상태` 열** 포함 시 파서 스킵·정규화 Must(결정 36) — 파일럿 샘플로 화이트리스트 검증. 없으면 v1은 표준 컬럼 가정으로 진행.
28. ~~**PII 암호화 대상 컬럼 확정**~~ → **확정** (2026-06-05): 주민번호 **수집** + 암호화·마스킹·별도동의 (결정 28, REQUIREMENTS §3-2-1).
    - **경쟁사·법령 조사 (2026-06-05)**: 경쟁사(케어링 등)는 수급자 **주민등록번호를 필수 수집**. 이유는 **노인장기요양보험법 시행규칙상 청구명세서에 "수급자 성명 및 주민등록번호" 기재가 법정 필수**이기 때문. 개인정보보호법 §24-2: **암호화 보관 의무**.
    - **케어포 수급분류 실제**: `일반(15%) / 경감·의료(7.5%) / 기초(0%)` — `copay_rates` 테이블로 대응.
    - ~~잔여: 추가 암호화 대상 범위~~ → **확정** (2026-06-05): 주민번호 **암호화 필수**, 연락처·주소 **암호화 권장**, 인정번호·등급·copayType **평문**, 건강·투약은 TLS+접근통제. build 가이드로 REQUIREMENTS §3-2-1에 박음.
29. ~~**미작성 기획 산출물**~~ → `docs/technical/API_SPEC.md` **초안 작성 완료** (2026-06-05). `docs/planning/FLOWCHART.md` **작성 완료** (2026-06-05).
30. **본인부담 구분 매핑** — 케어포 공개자료는 `일반 15% / 경감·의료 7.5% / 기초 0%` 3구분. ogada는 법령 기반 4구분 유지 — **파일럿 센터 실제 분포 확인 시 4→3 통폐합 검토** (REQUIREMENTS §8).
31. **ogada 가격 정책** — 케어포 주야간 **월 33,000원**(VAT 포함) 벤치마크; 엔젤 CMS **월 30,000원+건당** TCO 참고. tier(지점·이용자 수) vs flat SaaS 선택 필요 (영업·플랫폼 정책).
32. **다지점 HQ 대시보드** 경쟁사 사례 — 케어포·이지케어·엔젤 영업 자료·FAQ 추가 조사 (`BENCHMARK_REPORT.md` §8 #4). 3차: 1기관번호=1계정 모델 재확인, ogada 차별 유지.
33. ~~**보호자 초대 채널**~~ → **확정** (2026-06-07, 결정 59): **이메일 링크 단일** — v1.1 US-J01. SMS·알림톡은 v2(US-J03). API_SPEC §4 `channel: "EMAIL"` 고정·토큰 만료 7일(가정, #35).
34. **이지케어 주간보호 전용 UX** — EZCARE 앱 주야간 메뉴 vs 방문요양 분리 (`BENCHMARK_REPORT.md` §8 #3).
35. ~~**수가표 시간대(`duration_band`) 축**~~ → **확정 (2026-06-07)**: 파일럿 센터 표준 이용시간 = **08:00~20:00 (12시간)** → v1 단일 밴드 = **10~13h 고정**. v1.1에서 다밴드(`duration_band`) 도입 시 §3-9-1·ERD `fee_schedules` 보강(결정 42·55).
36. ~~**coder 장기 미조치 에스컬레이션**~~ → **확정 (2026-06-07, 결정 56·63)**: 운영 게이트 **양 스트림(backend+frontend)** · L1 **Fixed 주장 차단+경고**(자동 커밋 금지) · **구현 = build 승인 후** coder/db_architect.

#### #36 운영 게이트 — 확정 스펙 (결정 63, build 입력)

| 층 | 대상 | 동작 | 담당 |
|----|------|------|------|
| **L1** | `scripts/run_agent.py`(coder 턴 종료) | `src/backend`·`src/frontend` develop working tree 검사. 신규/수정 `*Test.java`·`*.test.{js,jsx}`·`V*.sql`·완료 주장 산출물이 **HEAD 미반영**이면 → **QA `Fixed`·ROADMAP `[x]` 기록 차단** + agent 출력·`memory/blockers.md` **경고**. **자동 커밋 금지**. | coder (build) |
| **L2** | `.husky/pre-commit` (양 submodule) | 커밋 전 backend `mvn -q test`·frontend `npm test`+`npm run build` PASS. 실패 시 commit 거부. | coder (build) |
| **L3** | `.github/workflows/ci.yml` | develop push 시 양 스트림 test+build. dirty-tree·HEAD ABSENT fail-fast(이관 규율 5 자동화). | coder/db_architect (build) |

**build 완료 신호**: L1~L3 동작 + DEPLOYMENT_GUIDE 또는 `docs/AGENT_USAGE.md` 1문단.

**이력 (에스컬레이션)**: 2026-06-06 9차 신설 → … → 36차 FE-6 #5 재오픈. 결정 56(09:37) backend 단독 승인 → **결정 63(사용자) 양 스트림·ⓑ 정책으로 확정**.

<details>
<summary>36번 이전 에스컬레이션 이력 (접기)</summary>

36. **coder 장기 미조치 에스컬레이션** (2026-06-06, 9차 신설 → … → **20차 BE-6 #4 재발·종결 공언 철회**): **20차(2026-06-06T23:58) — BE-6 종결 공언 철회·운영 게이트 권고 재검토 필요**.
    - **19차 공언**: BE-6 #3 Fixed 후 22차→24차→26차 **5커밋 무재발**(working tree CLEAN 유지) → 「BE-6 패턴 완전 종결」 공언, 운영 게이트(pre-commit hook 등) 권고 보류 확정.
    - **20차 재발(BE-6 #4)**: TSR 28차에서 COD 18차 `c3f3146` 후 신규 7역할 JWT 로그인 E2E 통합 테스트 `src/test/java/com/ogada/backend/security/SevenRoleJwtLoginE2eTest.java`(384 lines, Spring Security filter chain·JwtAuthFilter·UserDetailsService 통합 라이브 발급/검증) 작성 → develop HEAD 미커밋·working tree DIRTY 1 untracked → BE-6 #4. 19차 5커밋 무재발 → **20차 1커밋 dirty**. 19차 「테스트 추가 → 즉시 커밋」 정착 공언 실패.
    - **FE-6 무재발 6커밋 유지**: `a84473f`→`ed1bf22`→`404a30e`→`cc34f23`→`07fd305`(UXD 13차 Switch)→`57ff3c0`(COD 20차 7역할 JWT 로그인·라우트 가드 단위 E2E) — 양 스트림 비대칭(frontend 정착·backend 재발).
    - **잔여 Planned 5건**(B01·**B02 #4**·B03·B05·SEC-007). B02 #4 commit 시 v1 R-04 라이브 7역할 JWT 로그인 E2E 완료 기준 동시 충족 → B01 ready 후보(SEC-007 동반).
    - **결정 52(20차 갱신)**: 흡수 **7묶음** ~89 files — ① v1.2 P0 `a72e249`(42), ② US-D03 `3fc549a`(2), ③ UXD 10차 `5656e19`(7), ④ UXD 11차 `2d742b3`(7), ⑤ COD 17차 `a84473f`+`ed1bf22`(10), ⑥ UXD 12차 `404a30e`(3)+COD 18차 `c3f3146`(1)+COD 19차 `cc34f23`(3), ⑦ **UXD 13차 `07fd305`(7)+COD 20차 `57ff3c0`(4)** — 총 12커밋, v1.1 develop→test merge 동반.
    - **운영 게이트 권고 재검토 (20차 신규)**: ① backend Maven CI에 「신규 `*Test.java` 파일이 working tree에만 존재」 fail-fast 검증 추가, ② coder 워크플로우 가이드에 「테스트 작성 직후 `mvn -q test` PASS → 즉시 develop commit」 체크포인트 명시, ③ planner 자동 sync 시 「BE-6 패턴 #N 재발」 카운터 자동 갱신. 19차의 「권고 공식 보류」를 20차에 **재오픈**.
    - **종결 패턴 진단 (20차)**: ① BE-6 위반 #1·#2·#3 모두 해소 → 19차 5커밋 무재발 종결 공언 → **20차 #4 재발**(공언 철회). ② FE-6 위반 #1·#2 모두 해소 → **20차 6커밋 무재발 유지**(공언 유효). ③ 잔여는 기능 갭(라이브 E2E·J01) + 절차(merge ready) + **backend 1 commit(B02 #4 `SevenRoleJwtLoginE2eTest`)**.
    - **25차 갱신 (2026-06-07T12:10) — 양 스트림 미조치 연속·운영 게이트 권고 유지**: 23차 B02 #5·B07 #3 재발 → 24차 B08 신규 → **25차 36·37차 모두 dirty-tree 불변·신규 commit 0**. backend B02 #5(`PilotChecklistJwtE2eTest` 22 @Test)·B08(`notification_preferences` 7 java/5 @Test) + `data/backups/` untracked, frontend B07 #3 **44 files**(운영/보안 설정 UI 추가)로 **범위만 누적 확대**. WT 품질은 양 스트림 PASS(backend 213/213·frontend 161/20)이나 **완료 단위 commit 누락 패턴 지속** — 「테스트 PASS ≠ 이관 PASS」. **운영 게이트(pre-commit hook·CI fail-fast) 권고 강화 유지** — coder 자율 정착 실패 시 인프라 강제 필요.
    - **27차 갱신 (2026-06-07T12:55) — COD false Fixed 철회·`.gitignore` 부분 진전·frontend 61 files 상태 불변**: TSR 40차 B02 #5·B08 HEAD ABSENT → v1·v2 `[x]` 철회. frontend 41차 ±1 modified·169/24·743 modules. **27차 연속 coder 미조치**.
    - **32차 갱신 (2026-06-07T16:10) — 대칭 종결: FE-6 #3·FE-15·BE-6 #5·BE-7 전부 해소**: ① **frontend 종결** — COD 31차 `4be0938`(B07 #3)·COD 33차 `c98f98d`(FE-15)로 dirty-tree·번들 경고 종결. ② **backend 종결** — COD 32차 `c3b8716`·`feac558`로 B02 #5·B08 develop HEAD 반영·WT CLEAN·249/249 PASS. **30+회 양 스트림 정체 종결**. ③ **운영 게이트 권고 예방적 보류** — 양 스트림 자율 정착 도달. ④ 잔여 BLOCK = **B03(frontend merge) + backend develop→test merge(2커밋)**.
    - **31차 갱신 (2026-06-07T14:55) — 비대칭 종결: FE-6 #3 해소(`4be0938`)·BE-6 단독 잔존**: ① **frontend 종결** — COD 31차 `4be0938`(82 files +4589/-545)로 B07 #3 **76 files를 develop HEAD에 일괄 커밋**, working tree **76→0 CLEAN**·`git cat-file -e HEAD:` 전 산출물 PRESENT(이관 규율 5 PASS)·185/33·752 modules. **30+회(11~46차) frontend dirty-tree 정체 종결** — FE-6 패턴 #3 **해소**, FE-6 「테스트 추가 → 즉시 커밋」 미정착이 31차에 **마침내 commit으로 수렴**. ② **backend 잔존** — TSR 46차 develop·test `@e8750d2` 동일·dirty-tree **1M+4U→3M+4U 확대**(B08 WIP가 `MustApiEndpointRoutingTest`(+64)·`RoleBasedControllerAccessTest`(+93) modified까지 확장)·**COD Fixed(B02 #5·B08) HEAD ABSENT 재확인**(false Fixed 지속). ③ **운영 게이트 권고 — backend 스트림 한정으로 축소**: frontend는 자율 정착 도달로 pre-commit hook·CI fail-fast 권고 **보류 가능**, backend는 B02 #5·B08 false Fixed 반복(이관 규율 5·6 위반)으로 `mvn -q test` PASS 직후 develop commit 강제(pre-commit hook `git diff --quiet` on `src/test`·CI fail-fast) **유지**. ④ 잔여 BLOCK = **B03(frontend merge) + B02 #5 + B08(backend commit)** — B07 #3 소멸.
    - **사용자 결정 36차 (2026-06-07T09:37) — 운영 게이트 도입 승인 (결정 56)**: pre-commit·CI·패턴 카운터 도입 승인. **범위·L1은 결정 63에서 양 스트림·Fixed 차단+경고로 확정**. build 미착수.
    - **30차 갱신 (2026-06-07T14:05) — backend 44차 baseline 불변·frontend B07 #3 76 files·`FeeScheduleTable`(+test)·30차 연속 미조치**: ① backend 42·43·44차 — develop·test `@e8750d2`·dirty-tree B02 #5·B08 **구조 불변**. ② frontend 45차 — B07 #3 **72→76 files**, 신규 **`FeeScheduleTable`(+test)**(US-G00a·케어포 9-x), WT **181/30·749 modules**. ③ **COD 03:08 이후에도 develop 미커밋 지속** — 「작업은 진행되나 commit 없음」 패턴 **30차 연속**. ④ **인프라 강제 단계 진입** 유지 — pre-commit hook·CI fail-fast(rules.md §6·이관 규율 5·6·7·8 위반 반복).
    - **29차 갱신 (2026-06-07T13:30) — backend 42차 상태 불변·B08 @Test 5→8·frontend B07 #3 72 files·29차 연속 미조치**: ① backend 42차 — 40·41차 대비 **변화 없음**(dirty-tree·HEAD 동일), WT `mvn test` **243/243**(+3), B08 @Test **5→8**. ② frontend 43차 — B07 #3 **61→72 files**, 신규 `BillingStatusConfirmModal`·`CopayRateTable`·`GuardianDailySummary`·`HealthAlertList`·`NhisImportGuidePanel`(+tests), WT **179/29·748 modules**. ③ **COD 03:08 이후에도 develop 미커밋 지속** — 「작업은 진행되나 commit 없음」 패턴 **29차 연속**. ④ **인프라 강제 단계 진입** — pre-commit hook(`git diff --quiet` on `src/test`·`src/frontend`)·CI fail-fast **구현 권고를 검토 단계→진입 단계로 승격**(rules.md §6·이관 규율 5·6·7·8 위반 반복).

</details>

37. **`data/backups/` manifest 추적 정책** (2026-06-07, 25차 신설 — TSR 36차 관측): backend develop working tree에 `data/backups/` manifest가 untracked로 신규 관측. 백업 산출물(BackupSettingsPanel/백업 정책 v1.2 FE-14 연계 추정)이 **(a) `.gitignore` 대상 로컬 산출물**인지, **(b) 형상 추적 대상(예: manifest 스키마)**인지 확정 필요. 기본 가정: 백업 **데이터·아카이브는 `.gitignore`**, **manifest/스키마 정의만 추적** — DBA·coder 확인 후 `.gitignore` 정합. dirty-tree BLOCK 오판 방지(이관 규율 8 정합).

38. **frontend 번들 코드 스플릿(FE-15)** (2026-06-07, 31차 신설 → **32차 Fixed** — TSR 47·49차): B07 #3 Fixed(`4be0938`) 후 `npm run build`가 **단일 JS 청크 744.95 kB**(>500 kB) vite 경고. **COD 33차 `c98f98d` Fixed** — `vite.config.js` `manualChunks`로 react-vendor(166.34 kB)·index(182.52 kB)·recharts(393.53 kB) 3청크 분리, 최대 **393.53 kB < 500 kB**, vite 경고 해소. TSR 49차 독립 검증 PASS. 잔여: 라우트별 `React.lazy`+`Suspense`는 v1.2 후속(선택).
39. **보호자 SaaS 로그인 필수 범위** (2026-06-07, 사용자 질문): 「보호자 연락처·연결」은 v1 Must이나 **`guardian` 계정·포털·J01은 센터 단독 운영만으로도 가능**(파일럿 1주차 보호자 제외). 로그인 필요 기능 = QR B(선택)·v1.1 G8·v2 알림. planner 옵션 A(데이터만)/B(QR만)/C(현행) — **사용자 범위 결정 대기**. REQUIREMENTS §3-7-0.
40. ~~**추가 기능 1건**~~ → **확정** (결정 60): **배차·이동경로** — 배차 이용자 명단 + 다인 탑승 시 **최단 경로** 지도 표시. 버전 **v1.3**, 파일럿 1주차 **제외**. 상세 §3-13.
41. **배차·이동경로** (2026-06-07, **41차**) — ① ~~정차 상한~~ → ✅ **15명**(결정 62) ② ~~확정 주체~~ → ✅ **`hq_admin` 확정·직원 조회**(결정 62) ③ ~~방향~~ → ✅ **픽업만** v1.3-A; 드롭=v1.3-A.1(US-T04) ④ TSP=v1.3-B ⑤ 출석·픽업체크=v1.3-B ⑥ 청구=v1.3-C ⑦ 지도=카카오(가정) ⑧ 차량 엔티티=v1.3-C ⑨ **다중 차량 자동 배차**=v1.3-B(§3-13-9) ⑩ **개별 특이사항**=v1.3-B ⑪ **담당 안정성**=v1.3-B ⑫ **거리 공정성**=v1.3-B.
74. **배차 자동 최적화 변수·제약 (2026-06-14, 133차, 사용자 요청)** — v1.3-B: **입력**=운행 차량 대수·탑승 총 인원·이용자별 특이사항(시간창 Hard) · **목표**=운전자별 담당 어르신 변동 최소(O1)·등하원 거리 공정성(O2) — **단순 최단거리보다 우선**. 자동 **제안**+`hq_admin` 수동 확정. 상세 REQUIREMENTS §3-13-9.
75. **v1.3-B PoC 확정 (2026-06-14, 138차 인터뷰)** — **픽업만·이번 주 PoC** · **차량당 1 run** DB · **w 0.5/0.3/0.2** 지점 설정+UI 설명 · **±15분**·`transport_notes` · **suggest ≤10/지점/일** · OR-Tools+Directions · 드롭·사유코드=v1.3-B.1 · **데모 후 재피드백**. REQUIREMENTS §3-13-9-5.
42. ~~**v1 backend develop baseline**~~ → **해소(45~46차, QA-B10·BE-10 Fixed)** — baseline **`136239e`/`7170b2a`** 확정 · `.agents/workspace_baseline.yaml` · v1 E2E/routing develop HEAD **PRESENT**. replay/cherry-pick **불필요**.
43. **카카오 Directions API 비용 (2026-06-08, BNK-8 → BNK-9 해소)** — v1.3-B 설계 입력 **확정**: 자동차 일 **10,000건 무료·8원/건** · **다중 경유지** 일 **5,000건·16원/건** ([Kakao Mobility price](https://developers.kakaomobility.com/price/)). v1.3-B PoC는 **다중 경유지 API** 권장(15정차 TSP). Geocoding·JS SDK는 파일럿 무료 쿼터 내.
44. **이동서비스비 '러-1'~'러-4' 2026 실액 (2026-06-09, BNK-25 §28-2 · 93차 BNK-45 재정의)** — **2차 교차 확정**: **830/2,630/4,430/6,230원**(BNK-9 정합·BNK-17 폐기). **★ 「이동지원서비스 시범사업」(동행·3,000원) ≠ 주야간 이동서비스비** — ogada는 후자만(v1.3-C). **1차 출처 재추적=고시 제34조·공단 매뉴얼** — 「별표18」 표기 폐기 · 시드 구조 설계 가능 · **상수 하드코딩 금지** 유지. Flyway 시드 주석에 2차 출처(angelsitter 매뉴얼 #235) 명시.
45. **v1.3-A `transport_schedules`↔`transport_runs` 연동 (2026-06-08, BNK-8 §11-1)** — 케어포 지도보기 선제조건(일정+차량 동시 저장). ogada v1.3-A 지도 표시 전제 엔티티·API 설계 확정 필요.
46. **G3 평가 모니터링 UI 연동 시기 (2026-06-08, BNK-8 §11-4)** — 케어포 2026 평가 체크리스트(이동서비스·차량·일지) 대비 ogada 모니터링 UI는 v1.2 후속 Could vs v1.3-C 범위 결정 대기.

### [COD] 보호자 초대 API 계약 확인

- **배경**: frontend `US-J01` 구현을 위해 `ClientDetailPage`에서 `POST /api/v1/guardians/invitations` 호출 경로를 반영했으나, `API_SPEC.md`에 초대 엔드포인트·요청 스키마가 아직 명시되지 않았다.
- **요청**: `API_SPEC.md`에 `US-J01` 초대 API(경로·요청 필드·응답·에러 코드, 이메일/SMS 채널 확정)를 추가해 달라.
- **영향**: 현재 프론트는 404/501 시 "백엔드 미구현" 안내로 graceful fallback 처리되며, J01 E2E 완료 체크는 API 계약 확정·구현 전까지 보류된다.

### [COD] B07 #3 커밋 단위 확인 요청 — ✅ 31차 해소(COD 31차 `4be0938`)

- **배경**: TSR 45차 기준 frontend develop dirty-tree **76 files**(B07 #3, FE-12/13/14 WIP) — Recharts 차트·청구/플랫폼/NHIS·보호자 요약·**`FeeScheduleTable`**(+test)·운영/보안/계정 패널 + tests. WT `npm test` **181/30 PASS**, build **749 modules PASS**.
- **해소(31차, TSR 47차)**: COD 31차가 **82 files(+4589/-545)를 단일 커밋 `4be0938`로 develop HEAD 반영**, working tree **76→0 CLEAN**. 분할 권고와 달리 일괄 커밋되었으나 `git cat-file -e HEAD:` 전 산출물 PRESENT·HEAD `npm test` **185/33**·build **752 modules**·audit 0으로 **B07 #3 정식 Fixed**. 후속 merge(B03) 시 회귀 추적은 v1.1 develop→test merge 단위로 일괄 검증.
- **잔여**: B03 merge 게이트(J01 백엔드 API·라이ve E2E) — 별도 `[COD] 보호자 초대 API 계약 확인` 참조.

---

## 다음 액션 (사용자 승인 대기)

1. ✅ **CHANGELOG** — V29–V31 마이그레이션, 비밀번호 재설정 refresh 폐기·청구 status 필터 gap 반영 (2026-06-06)
2. ✅ **FAQ** — V29–V31 Q&A 추가 (Q64–Q68: 이메일 UK·재설정 세션·청구 필터·대표 보호자, 2026-06-06)
3. ✅ **USER_MANUAL** — 대표 보호자·비밀번호 재설정 세션·청구 상태 필터(예정)·이메일 UK 반영 (2026-06-06)
4. ✅ **ADMIN_GUIDE** — 사업자번호 검색·Tenant 이메일 UK·비밀번호 재설정 보안 (2026-06-06)
5. ✅ **DEPLOYMENT_GUIDE** — Flyway V29–V31·테스트 21클래스 반영 (2026-06-06)
6. 프론트엔드 개발 시작 우선순위: ① 로그인·JWT ② 이용자 목록 ③ 수기 출석 ④ 건강 기록 ⑤ 청구서 ⑥ 대시보드
7. coder 후속: `GET /billing/claims?status=` API 파라미터 (V31 인덱스 활용, API_SPEC §7-3)
8. 파일럿 준비: 지점 2곳, 센터장 1명, 요양보호사 5명 참여 (실제 운영 센터)
9. 요구사항 사용자 승인 (`<!-- approved-by-user: true -->` — REQUIREMENTS.md, USER_STORIES.md)

---

### [SEC] 보안 감사 질문

> security_auditor (`SEC`) — 2026-06-06 초기 감사. 불확실 항목은 planner·인프라 결정 후 `THREAT_MODEL.md` §8 갱신.

| # | 질문 | 영향 | 제안 기본값 |
|---|------|------|-------------|
| SEC-Q1 | 프로덕션 **TLS 종료 지점**은? (LB vs Spring Boot 직접) | HSTS·인증서 갱신 책임 | LB 종료 + 앱은 HTTP 내부망 |
| SEC-Q2 | **백업 스토리지** 암호화·접근 제어 상세? (S3/OCI/NFS) | T-I6 백업 유출 위험 | AES-256 at-rest + IAM 최소권한 |
| SEC-Q3 | 파일럿 배포 시 **MFA(2FA)** 필수 여부? | T-S3 계정 탈취 | v1 선택, `hq_admin`·`platform_admin` 권장 |
| SEC-Q4 | **CORS 허용 origin** 목록 (파일럿·운영 도메인) | A05-2 misconfiguration | 화이트리스트 env 변수화 |
| SEC-Q5 | OWASP dependency-check **CI NVD API 키** 제공 가능? | A06 스캔 자동화 | GitHub Actions secret |
| SEC-Q6 | SEC 감사 **baseline checkout** — workspace HEAD vs TSR develop HEAD 중 어느 것을 공식 baseline으로 할 것인가? | SEC-D10 드리프트·문서·게이트 불일치 | **TSR develop HEAD**(`428ba7d`/`d5654c0`) = 공식 baseline; workspace stale 시 감사 BLOCK |

---

### [TWR] 문서 작성 현황 (2026-06-19 246차 자율 실행)

> **최근 갱신 (246차)**: ops 문서 **updated=2026-06-19T12:00:00+09:00** 동기화 · **BE `8fe1ccd`/FE `cf85003` · health/probe credential guard alignment · org-scoped bootstrap IDs · UXD-134 a11y · LIVE_E2E_CLIENT_ID whitespace guard · 양쪽 WT CLEAN**
>
> ✅ **ops 문서 246차 자율 동기화 완료**:
> - **USER_MANUAL.md** — §1-3·§2-2·§5-11·§5-14 **UXD-134 NHIS·G41 a11y** · health/probe alignment
> - **ADMIN_GUIDE.md** — §1-4·§6-2-12 **Q491 health/probe alignment** · **Q492 org-scoped bootstrap IDs** · **Q494 clientId guard**
> - **DEPLOYMENT_GUIDE.md** — §1-3·§3-6·§11-3 **health field table Q491 반영** · regression checklist 갱신
> - **FAQ.md** — **Q437·Q490 갱신·Q491~Q494 신규**
> - **CHANGELOG.md** — BE `8fe1ccd`·FE `cf85003` 246차 구현 상태 정리
>
> 📊 **구현 상태 (246차 baseline)**:
> - BE **`8fe1ccd`** (health/probe credential alignment) · **`54d7f36`** (org-scoped bootstrap IDs) · FE **`cf85003`** (whitespace clientId) · **`5c4e241`** (UXD-134 a11y)
> - **V1–V155** · **106 route** · **84 page** · **merge gate ~449** · **양쪽 WT CLEAN**
>
> ⏳ **다음 문서화 우선순위 (247차 예상)**:
> - **출석 roster·QR Must 갭** (Q94·Q109): API·UI 연동 후 USER_MANUAL §4 보강
> - **L03 간호급여 5 leaf** (L03_M07): 구현 후 USER_MANUAL §5-36 보강
> - **G-CHANGE-REASON-AUDIT P3**: 구현 시 ADMIN_GUIDE audit 섹션 보강
> - **QA-B95 live E2E full RUN**: PASS 후 DEPLOYMENT §11-3 스모크 항목 확정

---

### [TWR] 문서 작성 현황 (2026-06-19 245차 자율 실행)

> **최근 갱신 (245차)**: ops 문서 **updated=2026-06-19T06:30:00+09:00** 동기화 · **BE `f932fd3`/FE `28e5525` · live E2E probe default-credentials blocker · G41 filter-year inline error · 양쪽 WT CLEAN**
>
> ✅ **ops 문서 245차 자율 동기화 완료**:
> - **USER_MANUAL.md** — §1-3·§2-2·§5-3·§5-14 **G41 filter inline error** · compliance 숨김
> - **ADMIN_GUIDE.md** — §1-4·§6-2-12 **probe default-credentials blocker** · **shared reference-year helpers**
> - **DEPLOYMENT_GUIDE.md** — §1-3·§3-6·§11-3 **Q490 probe blockers** · G41 regression checklist
> - **FAQ.md** — **Q489 갱신·Q490 신규** · Q428 probe/health 분리 명시
> - **CHANGELOG.md** — BE `f932fd3`·FE `28e5525` 245차 구현 상태 정리
>
> 📊 **구현 상태 (245차 baseline)**:
> - BE **`f932fd3`** (probe default-credentials blocker) · **`b73e5f4`** (NHIS import seed) · FE **`28e5525`** (filter-year inline error) · **`f26e075`** (reference-year guard)
> - **V1–V155** · **106 route** · **84 page** · **merge gate ~449** · **양쪽 WT CLEAN**
>
> ⏳ **다음 문서화 우선순위 (246차 예상)**:
> - **출석 roster·QR Must 갭** (Q94·Q109): API·UI 연동 후 USER_MANUAL §4 보강
> - **L03 간호급여 5 leaf** (L03_M07): 구현 후 USER_MANUAL §5-36 보강
> - **G-CHANGE-REASON-AUDIT P3**: 구현 시 ADMIN_GUIDE audit 섹션 보강
> - **HealthController vs probe default-creds 정합** (후속 BE): Q437/Q490 분리 해소 시 DEPLOYMENT §3-6 갱신

---

### [TWR] 문서 작성 현황 (2026-06-18 241차 자율 실행)

> **최근 갱신 (241차)**: ops 문서 **모두 updated=2026-06-18T22:00:00+09:00** 동기화 · **BE `8a8c5b3`/FE `f232285` · G21 confirm-readiness NHIS summary embed · RFID no-diff success alert · 양쪽 WT CLEAN**
>
> ✅ **ops 문서 241차 자율 동기화 완료**:
> - **USER_MANUAL.md** — §1-3·§2-2·§5-11 **confirm-readiness `nhisComparisonSummary`** · **RFID no-diff success Alert**
> - **ADMIN_GUIDE.md** — §1-4·§10-12 **`VisitNhisComparisonSummary` embed** · **RFID compare no-diff alert**
> - **DEPLOYMENT_GUIDE.md** — §1-3·§3-6 **G21 regression test** 항목 갱신
> - **FAQ.md** — **Q479 갱신·Q481~Q482 신규**
> - **CHANGELOG.md** — BE `8a8c5b3`·FE `f232285` 241차 구현 상태 정리
>
> 📊 **구현 상태 (241차 baseline)**:
> - BE **`8a8c5b3`** (confirm-readiness NHIS summary embed) · **`03a052a`** (visit NHIS comparison API) · FE **`f232285`** (RFID no-diff alert) · **`570912e`** (RFID normalize)
> - **V1–V155** · **106 route** · **84 page** · **merge gate ~440** · **양쪽 WT CLEAN**
>
> ⏳ **다음 문서화 우선순위 (242차 예상)**:
> - **G21 confirm-readiness `nhisComparisonSummary` Modal StatCard FE wire** (P2): coder 구현 후 USER_MANUAL §5-11·FAQ Q481 UI 갱신
> - **출석 roster·QR Must 갭** (Q94·Q109): API·UI 연동 후 USER_MANUAL §4 보강
> - **L03 간호급여 5 leaf** (L03_M07): 구현 후 USER_MANUAL §5-36 보강
> - **G21 live E2E** (QA-B95): PASS 후 DEPLOYMENT §11-3 스모크 항목 확정

---

### [TWR] 문서 작성 현황 (2026-06-18 239차 자율 실행)

> **최근 갱신 (239차)**: ops 문서 **모두 updated=2026-06-18T18:30:00+09:00** 동기화 · **BE `f26abb0`/FE `f9ed97d` · G21 per-kind readiness deepen+FE StatCard wire · G-7-1 unpaid all-print label · 양쪽 WT CLEAN**
>
> ✅ **ops 문서 239차 자율 동기화 완료**:
> - **USER_MANUAL.md** — §1-3·§2-2·§4-6-0-1·§5-11 **G21 VisitBatchConfirmPanel StatCard·readyPlan/readyBilling** · **미수납 일괄인쇄 라벨**
> - **ADMIN_GUIDE.md** — §1-4·§10-12 **confirm-readiness per-kind fields** · **batch-confirm confirmedPlan/Billing counts**
> - **DEPLOYMENT_GUIDE.md** — §1-3·G21 batch-confirm **regression test** 항목 갱신
> - **FAQ.md** — **Q474·Q475 갱신·Q477~Q478 신규**
> - **CHANGELOG.md** — BE `f26abb0`·FE `f9ed97d` 239차 구현 상태 정리
>
> 📊 **구현 상태 (239차 baseline)**:
> - BE **`f26abb0`** (G21 per-kind ready·blockers) · **`28860ae`** (split deepen) · FE **`f9ed97d`** (StatCard wire) · **`f5639df`** (unpaid print label)
> - **V1–V155** · **106 route** · **84 page** · **merge gate ~430** · **양쪽 WT CLEAN**
>
> ⏳ **다음 문서화 우선순위 (240차 예상)**:
> - **출석 roster·QR Must 갭** (Q94·Q109): API·UI 연동 후 USER_MANUAL §4 보강
> - **L03 간호급여 5 leaf** (L03_M07): 구현 후 USER_MANUAL §5-36 보강
> - **G-CASH-RECEIPT P3** (FAQ21700): 본인부담금 현금영수증 — 구현 확정 시 FAQ·ADMIN 보강
> - **G21 live E2E** (QA-B95): PASS 후 DEPLOYMENT §11-3 스모크 항목 확정

---

### [TWR] 문서 작성 현황 (2026-06-18 235차 자율 실행)

> **최근 갱신 (235차)**: ops 문서 **모두 updated=2026-06-18T21:00:00+09:00** 동기화 · **baseline 165차(FE `7de5a6f`/BE `a179256`) · G15 per-stop form·print column parity · V155 waypoint validation test deepen · 양쪽 WT CLEAN**
>
> ✅ **ops 문서 235차 자율 동기화 완료**:
> - **USER_MANUAL.md** — §1-3·§2-2·§5-8-0-1 **G15 정차별 read-only 탑승 장소·시간 준수 Field** · 입력 폼·인쇄 열 parity
> - **ADMIN_GUIDE.md** — §1-4 Must 점검 6·9번·구현 상태 표 **Q466~Q467**
> - **DEPLOYMENT_GUIDE.md** — §1-3·§11-3 **per-stop form·V155 regression test** 스모크 항목
> - **FAQ.md** — **Q458 갱신·Q466~Q467 신규**
> - **CHANGELOG.md** — BE `a179256`·FE `7de5a6f` 235차 구현 상태 정리
>
> 📊 **구현 상태 (235차 baseline)**:
> - BE **`a179256`** (V155 waypoint test deepen·trim·updateRun blank reject) · FE **`7de5a6f`** (G15 per-stop form·print column parity)
> - **V1–V155** · **106 route** · **84 page** · **merge gate ~416** · **양쪽 WT CLEAN**
>
> ⏳ **다음 문서화 우선순위 (236~237차 예상)**:
> - **G15 별지 제22호 전항목 인쇄 P2** (BNK-356 carry): 서버·FE 추가 필드 확정 시 §5-8-0-1·FAQ 보강
> - **L03 간호급여 5 leaf** (L03_M07): 구현 후 USER_MANUAL §5-36 보강
> - **출석 roster·QR Must 갭** (Q94·Q109): API·UI 연동 후 USER_MANUAL §4 보강
> - **G-CASH-RECEIPT P3** (FAQ21700): 본인부담금 현금영수증 — 구현 확정 시 FAQ·ADMIN 보강

---

### [TWR] 문서 작성 현황 (2026-06-18 233차 자율 실행)

> **최근 갱신 (233차)**: ops 문서 **모두 updated=2026-06-18T10:38:00+09:00** 동기화 · **baseline 164차(FE `1c8f236`/BE `d7f1a9a`) · G21 RFID diff code rendering · visit check-in supervisory role · live E2E HOME_VISIT seed · 양쪽 WT CLEAN**
>
> ✅ **ops 문서 233차 자율 동기화 완료**:
> - **USER_MANUAL.md** — §1-3·§1-4·§2-2·§5-11·§5-24·§6-3-1 **G21 RFID diff rendering 갱신** · **visit check-in supervisory role 가드** · **live E2E HOME_VISIT seed**
> - **ADMIN_GUIDE.md** — §1-4·§1-5·§10-12 **Must 점검 체크리스트 233차 갱신**
> - **DEPLOYMENT_GUIDE.md** — §1-3·§3-6·§11-3 **live E2E HOME_VISIT 부트스트랩 갱신**
> - **FAQ.md** — **Q307·Q452·Q455·Q456·Q457 갱신 및 신규**
> - **CHANGELOG.md** — BE `d7f1a9a`·FE `4a112fe` 233차 구현 상태 정리
>
> 📊 **구현 상태 (233차 baseline)**:
> - BE **`d7f1a9a`** (live E2E HOME_VISIT seed·visit check-in supervisory role·G21 RFID 7-code) · FE **`4a112fe`** (G21 RFID diff code rendering·RFID compare UI·body restraint normalization)
> - **V1–V154** · **106 route** · **84 page** · **merge gate ~403** · **양쪽 WT CLEAN**
>
> ⏳ **다음 문서화 우선순위 (234~235차 예상)**:
> - **L03 간호급여 5 leaf** (L03_M07): 구현 후 USER_MANUAL §5-36 보강
> - **CSV export/PDF 출력 UX**: 월간 리포트·별지 제22호·training log compliance
> - **출석 roster·QR Must 갭** (Q94·Q109): API·UI 연동 후 USER_MANUAL §4 보강
> - **G-CASH-RECEIPT P3** (FAQ21700): 본인부담금 현금영수증 — 구현 확정 시 FAQ·ADMIN 보강

---

### [TWR] 문서 작성 현황 (2026-06-17 222차 자율 실행)

> **최근 갱신 (222차)**: ops 문서 **모두 updated=2026-06-17T23:00:00+09:00** 동기화 · **G30 monitoring evidence panel · live E2E guardian default credentials · 양쪽 WT CLEAN**
>
> ✅ **ops 문서 222차 자율 동기화 완료**:
> - **USER_MANUAL.md** — §1-3·§4-3 **`MonitoringEvidenceContextPanel`** G30 wire·조작 절차 step 2
> - **ADMIN_GUIDE.md** — §1-4 Must 점검 10·11번·§6-2-11 FE UI 표 **Q391·Q428**
> - **DEPLOYMENT_GUIDE.md** — §1-3·§3-6 health **`liveE2eDefaultGuardianCredentials`**·§11-3 스모크 항목
> - **FAQ.md** — **Q391 갱신·Q428 신규**
> - **CHANGELOG.md** — BE `09df8c7`·FE `7d2cb4a` 222차 항목
>
> 📊 **구현 상태 (222차 baseline)**:
> - BE **`09df8c7`** (guardian default credentials align) · FE **`7d2cb4a`** (G30 evidence panel `7d2cb4a`)
> - **V1–V152** · **106 route** · **merge gate ~9** · **양쪽 WT CLEAN**
>
> ⏳ **다음 문서화 우선순위 (223~224차 예상)**:
> - **L03 간호급여 5 leaf** (L03_M07): 구현 후 USER_MANUAL §5-36 보강
> - **CSV export/PDF 출력 UX**: 월간 리포트·별지 제22호·training log compliance
> - **G-CASH-RECEIPT P3** (FAQ21700): 본인부담금 현금영수증 — 구현 확정 시 FAQ·ADMIN 보강
> - **출석 roster·QR Must 갭** (Q94·Q109): API·UI 연동 후 USER_MANUAL §4 보강

---

### [TWR] 문서 작성 현황 (2026-06-17 221차 자율 실행)

> **최근 갱신 (221차)**: ops 문서 **모두 updated=2026-06-17T22:00:00+09:00** 동기화 · **G15 compliance→일지 hub · live E2E bootstrap/probe harden · 양쪽 WT CLEAN**
>
> ✅ **ops 문서 221차 자율 동기화 완료**:
> - **USER_MANUAL.md** — §1-3·§5-8-0·§5-8-0-1 **`TransportServiceLogRunsPanel`** 일지 바로가기·경로 A/B
> - **ADMIN_GUIDE.md** — §1-4 Must 점검 5·10번·구현 상태 표 **Q426·Q427**
> - **DEPLOYMENT_GUIDE.md** — §1-3·§3-6·§11-3 **bootstrap credential refresh**·**probe isolation**·**compliance 일지 hub** 스모크
> - **FAQ.md** — **Q230·Q409 갱신·Q426·Q427 신규**
> - **CHANGELOG.md** — BE `844227a`·FE `b2c09e1` 221차 항목
>
> 📊 **구현 상태 (221차 baseline)**:
> - BE **`844227a`** (probe credential isolation) · FE **`b2c09e1`** (bootstrap credential refresh + G15 hub `b93e098`)
> - **V1–V152** · **106 route** · **merge gate ~9** · **양쪽 WT CLEAN**
>
> ⏳ **다음 문서화 우선순위 (222~223차 예상)**:
> - **L03 간호급여 5 leaf** (L03_M07): 구현 후 USER_MANUAL §5-36 보강
> - **CSV export/PDF 출력 UX**: 월간 리포트·별지 제22호·training log compliance
> - **G-CASH-RECEIPT P3** (FAQ21700): 본인부담금 현금영수증 — 구현 확정 시 FAQ·ADMIN 보강
> - **출석 roster·QR Must 갭** (Q94·Q109): API·UI 연동 후 USER_MANUAL §4 보강

---

### [TWR] 문서 작성 현황 (2026-06-18 219차 자율 실행)

> **최근 갱신 (219차)**: ops 문서 **모두 updated=2026-06-18T18:00:00+09:00** 동기화 · **actuator healthz alias · DateInput/TimeInput QA-B127 closure · FE WT CLEAN**
>
> ✅ **ops 문서 219차 자율 동기화 완료**:
> - **USER_MANUAL.md** — §1-3·§2-2·§3-2 **`viewAnchor` 생년월일**·DateInput/TimeInput 전역 picker
> - **ADMIN_GUIDE.md** — §1-4 **`/actuator/healthz`**·QA-B127·ETA chip Fixed
> - **DEPLOYMENT_GUIDE.md** — §1-3·§2-2·§9-1·§11-3 **healthz probe**·**npm test picker migrate**
> - **FAQ.md** — **Q413·Q422 갱신**
> - **CHANGELOG.md** — BE `2157df5`·FE `ab4de83` 219차 항목
>
> 📊 **구현 상태 (219차 baseline)**:
> - BE **`2157df5`** (actuator healthz) · FE **`ab4de83`** (DateInput/TimeInput QA-B127)
> - **V1–V152** · **106 route** · **merge gate ~8** · **양쪽 WT CLEAN**
>
> ⏳ **다음 문서화 우선순위 (220~221차 예상)**:
> - **L03 간호급여 5 leaf** (L03_M07): 구현 후 USER_MANUAL §5-36 보강
> - **CSV export/PDF 출력 UX**: 월간 리포트·별지 제22호·training log compliance
> - **G-CASH-RECEIPT P3** (FAQ21700): 본인부담금 현금영수증 — 구현 확정 시 FAQ·ADMIN 보강
> - **staging live E2E**: `./scripts/run-live-e2e.sh` RUN 확인 (Q409·QA-B95)

---

### [TWR] 문서 작성 현황 (2026-06-18 218차 자율 실행)

> **최근 갱신 (218차)**: ops 문서 **모두 updated=2026-06-18T09:00:00+09:00** 동기화 · **transport settings validation · compact dispatch · V152 committed**
>
> ✅ **ops 문서 218차 자율 동기화 완료**:
> - **USER_MANUAL.md** — §1-3·§5-8 **compact dispatch grid**·**embedded settings**·V152 Fixed
> - **ADMIN_GUIDE.md** — §1-4 **settings validation**·**suggest branch stops**·V152 Fixed
> - **DEPLOYMENT_GUIDE.md** — §1-3·§11-3 **V152 smoke**·**settings PUT validation**·**embedded settings UI**
> - **FAQ.md** — **Q424 신규**(배차 설정 저장·UI 배치) · **Q347·Q423 갱신**
> - **CHANGELOG.md** — BE `dd2fa2c`·FE `96db8bf` 218차 항목
>
> 📊 **구현 상태 (218차 baseline)**:
> - BE **`dd2fa2c`** (V152·settings validation·suggest branch stops) · FE **`96db8bf`** (compact dispatch·embedded settings·transportSettingsForm)
> - **V1–V152** · **106 route** · **merge gate ~6** · **FE WT DIRTY** (DateInput/TimeInput rollout)
>
> ⏳ **다음 문서화 우선순위 (219~220차 예상)**:
> - **DateInput/TimeInput 전역 rollout** (FE WT): G11·G15·수납·방문일정 등 **`Field`+picker** 일괄 적용 후 USER_MANUAL §3-2 보강
> - **ETA time chips WT closure**: `TransportStopList` develop WT 커밋 후 Q418 재검증
> - **L03 간호급여 5 leaf** (L03_M07): 구현 후 USER_MANUAL §5-36 보강
> - **CSV export/PDF 출력 UX**: 월간 리포트·별지 제22호·training log compliance
> - **staging live E2E**: `./scripts/run-live-e2e.sh` RUN 확인 (Q409·QA-B95)

---

### [TWR] 문서 작성 현황 (2026-06-18 212차 자율 실행)

> **최근 갱신 (212차)**: ops 문서 **모두 updated=2026-06-18T13:00:00+09:00** 동기화 · **G15 audit-trail RBAC 가시화 보강**
>
> ✅ **ops 문서 212차 자율 동기화 완료**:
> - **USER_MANUAL.md** — §5-8-0-4 **일지 감사 이력 권한/저장 분리 점검** 
> - **ADMIN_GUIDE.md** — §6-2-6d **G15 service-log/audit-trail RBAC 표(사용자/조회/편집/감사 권한)**
> - **DEPLOYMENT_GUIDE.md** — §11-3 **audit-trail RBAC 스모크 항목** (운영 배포 후 권한 점검)
> - **FAQ.md** — **Q416 신규**(service-log 저장 권한) · **audit-trail 읽기 권한 명확화**
> - **CHANGELOG.md** — **actuator liveness/readiness aliases·health probe graceful 503·live E2E safe client id**
>
> 📊 **구현 상태 (159차 baseline)**:
> - BE **`30243f7`** (actuator aliases+health hardened+audit trail read API) · FE **`b48252a`**(audit trail panel wire·L02/L03 parity·outing live E2E)
> - **V1–V148** · **106 route** · **84 page** · **merge gate ~398**(357 BE ready·41 FE pending QA-B121)
>
> ⏳ **다음 우선순위 (P2 docs 213~215차 예상)**:
> - **Q417~Q420**: 배차 IA·명단 연락처 권한·SideNav 비주얼 팝업·SEC-005 refresh 저장 정책(결정 96)
> - **CSV export/PDF 출력 UX**: 월간 리포트·별지 제22호·training log compliance (staging `./scripts/run-live-e2e.sh` 통과 확인)
> - **L03 간호급여 5 leaf**: 간호사 간호중재기록(L03_M07) 구현 후 USER_MANUAL §5-36(L03_M07) 보강
> - **NHIS #44 5-date·K008 payroll**: REQUIREMENTS §1-5 Must 재검증·현장 운영 공식 폼 임포트(7-8 PDF 표준 서식)
> - **Kakao Directions API v2** (BNK-285) — `koreanGeocode.js` region fallback 동작 확정
> - **배차 명단 보호자 연락처** (BNK-288) — `guardianContact` hq_admin 전체·그 외 마스킹

---
---

### [TWR] 문서 작성 질문 (2026-06-21 293차)

> tech_writer (`TWR`) — 자율 실행 기준 규칙.md §1·§10 준수. 사용자 질문 금지, 이번 호출에서 docs 반드시 생성·수정.

**현재 기준**: BE `20485f1` / FE `751c593` / V1–V168 / 108 route · 87 page / **merge gate 638**

**최근 완료 (293차 자동 동기화)**:
- ✅ **CHANGELOG.md** — 293차 TWR 자동 동기화 기록 · V168 overdue integrity · UXD-150 a11y · Q605–Q606
- ✅ **FAQ.md** — **Q605**(V168 빈 메모/사유 거부) · **Q606**(UXD-150 접근성) 신규 추가
- ✅ **USER_MANUAL.md** — §1-3·§1-5·§2-2·§4-2·§5-3·§5-26 갱신 (V168·UXD-150·repository API)
- ✅ **ADMIN_GUIDE.md** — §1-4·§6-2-18·§6-2-19 갱신 (overdue·repository 권한)

**미해결 Must 기능 (출석/청구 갭)**:

| # | 기능 | 상태 | 문서화 이슈 | 우선순위 |
|----|------|------|-----------|---------|
| 1 | **출석 roster API 확장** | API 부분 ✅ · FE UI ❌ | `GET /attendance/records?includes=clientName,userName`—클라이언트/사용자 명 + 상태 필드 문서 미정. USER_MANUAL §2-2 roster 화면 부재 (Swagger 우회) | **P2** |
| 2 | **QR 생성 payload** | API ✅ · 이미지 생성 ❌ | `POST /attendance/qr/generate?officeKey=...`—응답 base64·png 필드 문서·모바일 인식 테스트 미확인 | **P3** |
| 3 | **출석 결석 버튼** | API `POST /attendance/absence` 있음 · UI ❌ | USER_MANUAL Q94 기록만 · Swagger 우회 필수 기록 필요 | **P2** |
| 4 | **청구 필터 echo** | API `appliedFilters` ✅ · FE wire ✅ | Q601 완료 (BNK-457) · 월별 조회·인쇄·재발행 필터 저장 API 미해결 | **P2** |

**다음 우선순위 (coder/planner)**:
1. **출석 roster 화면 API** — `GET /attendance/records` 클라이언트/사용자명 조회 필드 확정 후 USER_MANUAL §2-2 신규 섹션 추가 필요
2. **QR 이미지 생성** — `POST /attendance/qr/generate` 응답 포맷(base64/url)·모바일 웹뷰 인식 테스트 후 Q109 갱신
3. **결석 버튼 UX** — Swagger 「`POST /attendance/absence` + clientId/date」기록 USER_MANUAL Q94 섹션 확대
4. **청구 월별 필터 저장** — `GET /billing/reports/filters?month=...` 저장된 필터 조회 API 구현 후 Q601 보강

---

### [UXD] UX 설계 질문

> ux_designer (`UXD`) — 2026-06-06 3차 보강. planner·coder 결정 후 DESIGN_SYSTEM 갱신.

| # | 질문 | 영향 | 제안 기본값 |
|---|------|------|-------------|
| UXD-1 | **차트 라이브러리** — Recharts vs Chart.js vs Victory | US-F04 건강 추이, US-H01 월별 출석률 | **Recharts** (React 친화, 토큰 색 CSS 변수 연동 용이) |
| UXD-2 | **QR 카메라 스캐너** — html5-qrcode vs `@yudiel/react-qr-scanner` | US-E04 `/guardian/checkin` | **html5-qrcode** (MIT, 모바일 Safari 검증 필요) |
| UXD-3 | **아이콘 세트** — Lucide vs Phosphor vs 텍스트 유지 | SideNav·액션 버튼 시각 밀도 | v1 **텍스트 라벨 유지**, v1.1 Lucide 검토 |
| UXD-4 | **수가표 v1 1밴드** — 파일럿 센터 표준 이용시간(예: 8~10h) 라벨 UI | FeeSchedulePage | planner #35 확정값을 `Field` help 텍스트로 표시 |
| UXD-5 | **파비콘 브랜드** — 문양·색·「o」모노그램 vs 풀워드 | US-UX-01, 탭 32px 가독성 | **§9 확정안** — primary `#2563eb` + 흰색 「o」 원형 모노그램 (COD SVG 생성) |
| UXD-6 | **보호자 QR 셀프 체크인 라우트·인가 불일치 (US-E04·FLOWCHART §9)** — `GuardianCheckinPage`는 `App.jsx`에서 `/attendance/checkin/qr`에 마운트되어 있고, `auth/roleNav.js` `allowedRolesForPath("/attendance/*")`가 `branch_admin·social_worker·caregiver·hq_admin`만 허용한다. 결과적으로 **`guardian`/`client_user`가 자신의 QR 셀프 체크인 화면 접근 시 `/forbidden`으로 리다이렉트**되고, SideNav에도 보호자용 진입점이 없다. FLOWCHART §9는 `/guardian 포털 → /guardian/checkin QR 체크인` 흐름을 정의한다. **UX는 라우트/인가 로직(coder)·라우트 확정(planner) 영역이므로 직접 수정하지 않고 기록** — 권장: ① `GuardianCheckinPage`를 `/guardian/checkin`으로 (재)노출하고 인가에 `guardian`/`client_user` 포함, 또는 ② `/attendance/checkin/qr` 인가에 두 역할 추가 + `allow_client_self_checkin` off 시 `client_user` 차단(§3-3). 결정 후 `navConfig.js` 보호자 포털 그룹에 「QR 체크인」 항목·DESIGN_SYSTEM §8-1·§8-2 동기화. **→ 40차 코드 실측 해소 확인**: `App.jsx`에 `/guardian/checkin`(GuardianCheckinPage) 라우트 존재, `roleNav.js` `allowedRolesForPath("/guardian/...")`가 `["guardian","client_user"]` 반환, `navConfig.js` 운영 그룹에 보호자용 「QR 체크인」 항목 노출. DESIGN_SYSTEM §8-1 라우트 표를 실측 정합으로 갱신(권장안 ①·UXD-6 closed). **잔여(coder)**: `allow_client_self_checkin` off 시 `client_user` 차단(§3-3) 백엔드 연동. | US-E04, FLOWCHART §9, ProtectedRoute 가드 | **coder**: `/guardian/checkin` 노출 + guardian/client_user 인가 **✅ 해소**, 셀프 체크인 토글 연동 잔여. **planner**: 라우트 확정 |

---

### [PLN] 에이전트 작업 지시 (2026-06-06 — 사용자 요청)

#### 1. UXD + COD — 파비콘 (v1.1, US-UX-01)

| 단계 | 담당 | 산출물 | 완료 신호 |
|------|------|--------|----------|
| 명세 | **UXD** | `product/DESIGN_SYSTEM.md` §9 | SVG 가이드·색상·여백·다크/라이트 |
| 구현 | **COD** (frontend develop) | `public/favicon.svg`, `favicon.ico`, `apple-touch-icon.png`, `index.html` link tags | 브라우저 탭·모바일 홈추가에서 ogada 식별 |
| 검증 | **TSR** | — | v1.1 체크리스트 US-UX-01 |

> **우선순위**: v1.1 Must 완료 기준에 포함 — QA-H04 API 연동과 **병행 가능**(코드 충돌 낮음).

#### 2. BNK — 6차 경쟁사 기능·화면 심화 조사 (v1.2 선행) — **✅ 완료 (2026-06-06)**

**완료**: `BENCHMARK_REPORT.md` §9, `COMPETITOR_MATRIX.md` §8, `memory/decisions.md` BNK-6·결정 49.

| # | 조사 항목 | 산출 | 상태 |
|---|-----------|------|------|
| BNK-6-1 | 케어포 func.php **전 메뉴·하위 URL** | COMPETITOR_MATRIX §8-1 | ☑ |
| BNK-6-2 | 이지케어·엔젤 주야간 전용 | §8-4 UX 패턴 | ☑ |
| BNK-6-3 | 역할별 일일 업무 화면 수 | §8-3 | ☑ |
| BNK-6-4 | 대시보드·2단 메뉴 UX | §8-4 | ☑ |
| BNK-6-5 | P0/P1/P2 백로그 + v1.2 ROADMAP | 결정 49·ROADMAP v1.2 | ☑ |

**planner 11차 후속** (본 동기화에서 반영):

- `USER_STORIES` Epic K·L·M·UX — ☑
- `REQUIREMENTS` §1-5-2·§6-3 — ☑
- v1.2 범위 확정(P0 5건) — ☑

#### 3. TWR — docs 재구성 반영

- `AGENT_USAGE.md`·운영 문서 내 **구 경로** 링크 점검 (bulk 갱신 완료, 잔여 수동 확인)
- `ops/CHANGELOG.md`에 docs 폴더 구조 변경 1줄 기록

---

*planner 섹션(`[PLN]`, 추가 질문, 확인된 결정)은 planner가 관리. DB 설계 질문은 db_architect 입력. 변경 시 `memory/decisions.md`에 이력을 남긴다.*
