<!-- doc:owner=TWR doc:audience=human updated=2026-06-26T23:00:00+09:00 -->
# ogada 변경 기록

> **누가 쓰나**: TWR(문서 에이전트)  
> **누가 읽나**: 운영·기획 담당자(당신) — 개발 세부사항은 각 카드 맨 아래 「자세히」만 보면 됩니다.  
> **이 문서는 develop HEAD `d06e3f1` / frontend `4bbd54a`(377차 baseline, 2026-06-26) 기준입니다.**

## 읽는 법

1. **최근 7일 요약**만 봐도 됩니다.
2. 카드의 **내 화면/업무에 영향**이 「없음」이면 앱 체감 변화 없음(문서·테스트·내부 작업).
3. **3개월 지난 날짜**는 이 파일에서 삭제합니다. 오래된 내용은 남기지 않습니다.

## 최근 7일 요약

- **2026-06-26** — **TWR 377차 ops 문서 보강** — **Q722 recovered-auth readiness hints · Q713 deepen** · baseline **`d06e3f1`/`4bbd54a`**
- **2026-06-26** — **QA-B95 recovered-auth readiness hints FE wire** — **`liveE2eAllowRecoveredAuth`·`liveE2eBootstrapEnableHint` parse** · neutral hint filter · **FE `4bbd54a`**
- **2026-06-26** — **QA-B95 recovered-auth readiness hints BE expose** — **`BOOTSTRAP_RECOVERED_AUTH_HINT`** health/probe · **BE `d06e3f1`**
- **2026-06-26** — **TWR 376차 ops 문서 보강** — **Q719 G21 seed service-unavailable · Q720 neutral blocker · Q721 V180 · UXD-165** · baseline **`42a369e`/`7e7c296`**
- **2026-06-26** — **QA-B95 G21 seed detail + V180 integrity** — **`g21-seed=service-unavailable`** · **program_client_groups defense-in-depth** · **BE `42a369e`**
- **2026-06-26** — **QA-B95 neutral operation blocker markers** — **`none`/`ok` filter** · **FE `7e7c296`**
- **2026-06-26** — **UXD-165 a11y polish** — **`StaffMonthlySchedulePage` aria-busy/group** · **`.ds-refund-fee-preview` CSS** · **FE `bee97b9`**
- **2026-06-26** — **TWR 375차 ops 문서 보강** — **Q717 G-STAFF-MONTHLY-SCHEDULE-FE-WIRE · Q718 singular operation blocker · Q713 BE recovered auth** · baseline **`3342938`/`b7004ca`**
- **2026-06-26** — **G-STAFF-MONTHLY-SCHEDULE-FE-WIRE** — **`StaffMonthlySchedulePage`** · **`/staff/schedules`** · **FE `33944e4`**
- **2026-06-26** — **QA-B95 legacy singular operation blocker keys** — **`liveE2eOperationBlocker`** singular merge · **FE `b7004ca`**
- **2026-06-26** — **QA-B95 BE honor recovered auth in health/probe** — **`ogada.live-e2e.allow-recovered-auth`** · **BE `3342938`**
- **2026-06-26** — **TWR 374차 ops 문서 보강** — **Q716 string-form operation blocker normalize · Q713 deepen probe-state persistence** · baseline **`49fe2e7`/`bd3253a`**
- **2026-06-26** — **QA-B95 string-form operation blocker normalize** — **`liveBackendProbe`·`liveConfig`·`liveGlobalSetup`** · **FE `bd3253a`/`2c9abd6`**
- **2026-06-25** — **TWR 373차 ops 문서 보강** — **Q714 deepen 5-9 group-history fill · Q715 branchId filter · Q713 health reason surfacing** · baseline **`49fe2e7`/`f74a6e7`**
- **2026-06-25** — **G-REPORT-DENSITY program report branch filter** — **optional `branchId` query** · **BE `49fe2e7`**
- **2026-06-25** — **G-REPORT-DENSITY 5-9 group-history fill** — **V179 `program_client_groups`** · **membership aggregate** · **BE `337453d`**
- **2026-06-25** — **QA-B95 live E2E health reason surfacing** — **`liveBackendProbe` backend `reason`** · **FE `f74a6e7`**
- **2026-06-25** — **TWR 372차 ops 문서 보강** — **Q713 deepen bootstrapServiceAvailable probe · bootstrap-unavailable blocker recovery** · baseline **`0e55f3b`/`75c0f51`**
- **2026-06-25** — **QA-B95 bootstrap-unavailable blocker recovery** — **`liveConfig.js`/`liveGlobalSetup.js`** · **`bootstrap-unavailable` label filter** · **FE `75c0f51`**
- **2026-06-25** — **QA-B95 bootstrap service availability probe** — **`LiveE2eProbeResponse.bootstrapServiceAvailable`** · disabled vs bean-missing 분리 · **BE `0e55f3b`**
- **2026-06-25** — **TWR 371차 ops 문서 보강** — **Q714 G-REPORT-DENSITY M5 program reports** · **5-7~5-10 full-stack** · baseline **`650801b`/`15a3b7f`**
- **2026-06-25** — **G-REPORT-DENSITY M5 program report FE wire** — **`ProgramReportsPage`** · **4 GET `/programs/reports/*`** · **FE `15a3b7f`**
- **2026-06-25** — **G-REPORT-DENSITY M5 program report API** — **`ProgramReportController`** · **5-7~5-10** · **BE `650801b`**
- **2026-06-25** — **TWR 370차 ops 문서 보강** — **Q705 bathing FE closure 정합** · **Q712 M7 7-9 lifecycle deepen** · baseline **`9f67954`/`5914b2f`**
- **2026-06-25** — **TWR 369차 ops 문서 보강** — **Q709 7-5 provider-catalog FE wire** · **Q710 TransportParityRulesPanel page mount** · **Q713 deepen bootstrap readiness enforcement** · baseline **`9f67954`/`5914b2f`**
- **2026-06-25** — **G2/7-5 easy-pay provider catalog FE wire** — **`EasyPayProviderCatalogPanel`** · **`TransportParityRulesPanel` mount** · **FE `5914b2f`**
- **2026-06-25** — **QA-B95 bootstrap readiness enforcement** — **`ogada.live-e2e.enforce-bootstrap-readiness`** · health **`liveE2eBootstrapReadinessEnforced`** · **BE `9f67954`**
- **2026-06-25** — **TWR 368차 ops 문서 보강** — **Q712 `feePolicyCode` Bean Validation** · **Q713 live E2E effective operation readiness** · baseline **`79725eb`/`e070c45`**
- **2026-06-25** — **QA-B95 recovered auth operation readiness** — **`liveE2eEffectiveOperationReady`** · bootstrap-disabled false-block fix · **FE `e070c45`**
- **2026-06-25** — **7-9 refund fee policy input validation** — **`RecordCopayRefundRequest` `@Pattern`** · invalid code **`400`** · **BE `79725eb`**
- **2026-06-25** — **TWR 367차 ops 문서 보강** — **Q712 deepen 7-9 refund fee full-stack** · **`RefundRecordModal` catalog wire** · baseline **`aeecc1b`/`cadd74a`**
- **2026-06-25** — **G-REFUND-FEE-FE-WIRE** — **`RefundRecordModal`** policy·preview·net amount · **FE `cadd74a`** · FAQ **Q712 deepen**
- **2026-06-25** — **7-9 refund fee net validation** — **`POST …/refunds` `feePolicyCode`** · payment-channel match · **BE `aeecc1b`**
- **2026-06-25** — **TWR 366차 ops 문서 보강** — **Q712 7-9 copay refund fee policy catalog** · **Q705 목욕 FE full-stack closure** · baseline **`2adae59`/`3d7f13b`**
- **2026-06-25** — **US-O01 bathing FE wire** — **`BathingScheduleIndicator27Panel`** · **`preObservationNotes`/`postObservationNotes` form** · **FE `3d7f13b`**
- **2026-06-25** — **G-REFUND-FEE-DEDUCTION catalog API** — **`GET/POST /billing/copay/refund-fee-policy-catalog`** · **KCP 3.3%/500원 preview** · **BE `2adae59`** · FAQ **Q712**
- **2026-06-25** — **TWR 365차 ops 문서 보강** — **Q711 연차 branchName 공백 fallback** · **Q709 routing test lock** · **QA-B312 deepen** · baseline **`5a5174a`/`58f3858`**
- **2026-06-25** — **QA-B312 branch scope fallback** — **`normalizeBranchScope`** whitespace trim · **`BranchScopeNotice` 지점 ID fallback** · **FE `58f3858`**
- **2026-06-25** — **easy-pay provider-catalog routing test** — **`EasyPayControllerRoutingTest`** pgMode·RBAC lock · **BE `5a5174a`**
- **2026-06-25** — **TWR 364차 ops 문서 보강** — **Q709 7-5 easy-pay provider-catalog API** · **Q710 TransportParityRulesPanel scaffold** · **V178 DB integrity** · **QA-B312 vitest isolation** · baseline **`56831fc`/`892122d`**
- **2026-06-25** — **G-EASYPAY-PROVIDER-CATALOG** — **`GET /billing/easy-pay/provider-catalog`** CARD·KAKAO_PAY · **`pgMode` stub/live** · **BE `56831fc`** · FAQ **Q709**
- **2026-06-25** — **V178 CMS·목욕 defense-in-depth** — **`cms_collection_requests` lifecycle CHECK** · **bathing pre/post nonempty** · **BE `3c1fdce`**
- **2026-06-25** — **UXD-163 TransportParityRulesPanel + audit badge CSS** — **`TransportParityRulesPanel.jsx`** · **`ds-nhis-alt-key-badge`** · **FE `7b4c6f9`** · **page mount P2** (Q710)
- **2026-06-25** — **QA-B312 StaffAnnualLeavePage vitest isolation** — **full-suite pollution fix** · **FE `892122d`**
- **2026-06-25** — **TWR 363차 ops 문서 보강** — **Q708 CMS catalog EmptyState** · **NHIS 매칭 의사결정표** (Q706·Q707) · **목욕 Swagger 워크플로** (Q705) · **G16 parity-rules fallback 안내** (Q703) · **README 362차 동기화**
- **2026-06-25** — **G-NHIS-ALT-KEY-AUDIT-BADGE** — NHIS import **`altKeyMatched`** API·UI **「대체 매칭됨 — 검증 필요」** Badge · **BE `4963535` · FE `5bb84a6`** · FAQ **Q707** · USER_MANUAL §4-6-1
- **2026-06-25** — **G-NHIS-MASKED-NAME-FALLBACK** — 공단 **마스킹 수급자명** alt-key 자동 매칭 · **청구·방문 NHIS import** · **BE `37416ac`** · FAQ **Q706** · USER_MANUAL §4-6-1
- **2026-06-25** — **CMS catalog empty state** — **`CmsPaymentMethodCatalogPanel`** 빈 catalog **`EmptyState`** · **FE `9a583ec`**
- **2026-06-25** — **G16 parity-rules API spec + RBAC** — 응답 **`code`·`label`·`description`** · **`social_worker` 403** · **BE `e4f83af`** · FAQ **Q703·Q578** · **live E2E placeholder casing 정규화** · **FE `5afef2d`**
- **2026-06-25** — **G2b CMS collection + G16 parity-rules FE wire** — **`CmsCollectionPanel`** 가상계좌·다계좌 탭 · **`TransportServiceFeePanel`** parity-rules API · **M7 7-4 coverage 1.0** · **FE `9aeedfe`** · FAQ **Q701·Q703·Q704** 정정 · USER_MANUAL §4-6-3·§4-6-4
- **2026-06-25** — **US-O01 목욕 전·후 관찰 + 평가지표 27 compliance API** — **`preObservationNotes`·`postObservationNotes`** · **`GET /care/bathing-schedules/indicator-27-compliance`** · **BE V177 ✅** · **FAQ Q705** · USER_MANUAL §5-26 보강
- **2026-06-24** — **G2b CMS collection methods closure** — **`POST/GET /billing/cms/claims/{id}/virtual-account`** · **`POST/GET /billing/cms/claims/{id}/multi-account-settlement`** · **BE V176 ✅** · **FAQ Q704** · USER_MANUAL §4-6-3·4-6-4 신규
- **2026-06-24** — **G16 NHIS #44 parity rules API** — **`GET /transport/service-fee-parity-rules`** · **`TransportServiceFeeParityCatalog`** · FAQ **Q703**
- **2026-06-24** — **live E2E operation readiness dedupe** — **`liveConfig.js`** skip reason 중복 제거 · harness test lock (`c3c6272`)
- **2026-06-24** — **G2b CMS payment-method-catalog FE wire** — **엔젤 5-method 카탈로그 표 `/billing/cms`** · **수납 구현 5/5 완성** · **FAQ Q701 수정** · USER_MANUAL §4-6 정정
- **2026-06-24** — **G2b CMS payment-method-catalog API** — **`GET /billing/cms/payment-method-catalog`** silverangel parity · **5/5 기능 완성**
- **2026-06-24** — **M7 7-x lifecycle crosswalk** — **케어포 본인부담 10-leaf ↔ ogada `/billing/*` 1:1 재입증** · **FAQ Q700 · USER_MANUAL §5-10-0**
- **2026-06-24** — **G-SMS test lock** — **guardian dispatch `ezcareMessageKind` 회귀 테스트** · **청구·미납 발송 Alert 라벨 assertion**
- **2026-06-24** — **G-SMS dispatch success label** — **발송 성공 Alert에 ezCare 템플릿 한글명** · **직원 발송 API `ezcareMessageKind` 6/6 parity**
- **2026-06-24** — **G-SMS UXD-161·label sync** — **발송 패널 form-stack 간격** · **readiness fallback 라벨 ezCare parity** · health **`liveE2eG21SeedStatusDetail`** 테스트 lock
- **2026-06-24** — **G-SMS-TEMPLATE-CATALOG deepen** — **message_kind 11·13·19 UI 라벨** · **`dispatchReady` 채널 자격 검증** · 발송 API **`ezcareMessageKind` 응답** · **message_kind 1·12·21 발송 UI** · readiness **「발송 대기」**
- **2026-06-24** — **G-SMS-TEMPLATE-CATALOG full closure** — **직원 접속키 SMS API**(6/6 dispatch) · **`dispatchReadyCount`** · **UXD-160 a11y** · FAQ21823 compliance
- **2026-06-23** — 상세주소만 수정해도 저장, 이동서비스비 NHIS #44 안내 고정, 요양보호사 이용자 수정·주소 검색·목록 필터

---

## 2026-06-26

### 📄 TWR 377차 — ops 운영 문서 보강 (doc-only)
- **에이전트**: TWR
- **한 일**: **Q722 신규** — recovered-auth **`liveE2eBootstrapEnableHint`** BE expose (`d06e3f1`) · FE health parse·neutral filter (`4bbd54a`) · **Q713·Q720 deepen** · baseline **`d06e3f1`/`4bbd54a`**
- **내 화면/업무에 영향**: 없음 — 문서만 갱신
- **상태**: FAQ **Q722·Q713 deepen** · ADMIN_GUIDE **§1-4** · DEPLOYMENT **§1-4·§11-3** · README **§6**

<details>
<summary>자세히</summary>

- 대상: **IT live E2E triage** — QA-B95 cluster layer 9 (recovered-auth hint surfacing + FE neutral filter)
- P2 carry: **program reports FE `branchId`** · **7-5 live PG** · **J03 Solapi live dispatch** · **M6 6-2~6-4 `/safety/*`**

</details>

### ✅ QA-B95 recovered-auth readiness hints FE wire (`4bbd54a`)
- **에이전트**: COD
- **한 일**: **`liveBackendProbe.js`·`liveConfig.js`·`liveGlobalSetup.js`** — health **`liveE2eAllowRecoveredAuth`·`liveE2eBootstrapEnableHint`** parse · **`isLiveRecoveredAuthAllowed()`** · recovered-auth hint **neutral reason/blocker** · **`liveE2eHarness.test`** regression lock (BE `d06e3f1` align)
- **내 화면/업무에 영향**: 없음 — **live E2E harness** triage only
- **상태**: FE 완료 · FAQ **Q722** · DEPLOYMENT **§11-3** · ADMIN_GUIDE **§1-4**

<details>
<summary>자세히</summary>

- FE: `4bbd54a` (on `7e7c296` neutral blocker)
- hint match: **`recovered-auth` + `readiness mode`** (case-insensitive)
- before: hint surfaced but could count as actionable blocker/skip reason
- after: **`liveE2eEffectiveOperationReady=true`** when auth recovered + hint-only

</details>

### ✅ QA-B95 recovered-auth readiness hints BE expose (`d06e3f1`)
- **에이전트**: COD
- **한 일**: **`HealthController`·`LiveE2eController`** — bootstrap disabled + **`allow-recovered-auth`** + bean wired → **`liveE2eBootstrapEnableHint=Bootstrap is disabled; recovered-auth readiness mode is active.`** · **`LiveE2eOperationReadinessSupport.BOOTSTRAP_RECOVERED_AUTH_HINT`** · **`HealthControllerTest`·`LiveE2eControllerTest`** lock
- **내 화면/업무에 영향**: 없음 — health/probe 진단 precision
- **상태**: BE 완료 · FAQ **Q722·Q713 deepen** · DEPLOYMENT **§11-3**

<details>
<summary>자세히</summary>

- BE: `d06e3f1` (on `42a369e` V180 + G21 detail)
- before: **`liveE2eBootstrapEnableHint=null`** on recovered-auth path
- after: explicit hint — pairs **`liveE2eAllowRecoveredAuth=true`**

</details>

### 📄 TWR 376차 — ops 운영 문서 보강 (doc-only)
- **에이전트**: TWR
- **한 일**: **Q719 신규** — G21 seed **`service-unavailable` vs `disabled` 분리 (`42a369e`) · **Q720 신규** — neutral blocker **`none`/`ok` filter** (`7e7c296`) · **Q721 신규** — **V180** program group integrity · **Q698·Q717·Q712 deepen** — UXD-165 a11y·refund fee preview CSS (`bee97b9`) · baseline **`42a369e`/`7e7c296`**
- **내 화면/업무에 영향**: 없음 — 문서만 갱신
- **상태**: FAQ **Q719·Q720·Q721·Q698 deepen** · USER_MANUAL **§1-3·§4-7 근무일정표 a11y** · ADMIN_GUIDE **§1-4·§6-2-21** · DEPLOYMENT **§1-4·§2-2 V180·§11-3** · README **§6**

<details>
<summary>자세히</summary>

- 대상: **IT live E2E triage** — G21 seed detail precision · neutral placeholder blockers · **DBA V180** 5-9 group membership integrity
- P2 carry: **program reports FE `branchId`** · **7-5 live PG** · **J03 Solapi live dispatch** · **M6 6-2~6-4 `/safety/*`**

</details>

### ✅ QA-B95 G21 seed detail + V180 program group integrity (`42a369e`)
- **에이전트**: COD
- **한 일**: **`HealthController`** — bootstrap service-unavailable 시 **`liveE2eG21SeedStatusDetail=g21-seed=service-unavailable`** (기존 `disabled` 오표시 정정) · **Flyway V180** — `program_client_groups`/`program_client_group_members` 3-way FK·active-client guard·org/branch sync · **`HealthControllerTest`** regression lock
- **내 화면/업무에 영향**: 없음 — health 진단·DB defense-in-depth · **5-9 group-history read path** 데이터 정합 (Q714)
- **상태**: BE 완료 · FAQ **Q719·Q721·Q698 deepen** · DEPLOYMENT **§2-2 V180** · DATA_RETENTION §4-1

<details>
<summary>자세히</summary>

- BE: `42a369e` (on `3342938` allow-recovered-auth)
- V180: 165L — cross-branch group reference·inactive client INSERT guard · purge index
- health: disabled vs service-unavailable **G21 detail split**

</details>

### ✅ QA-B95 neutral operation blocker markers (`7e7c296`)
- **에이전트**: COD
- **한 일**: **`liveBackendProbe.js`·`liveConfig.js`** — **`NEUTRAL_BLOCKERS={"none","ok"}`** — health·persisted state blocker normalize 시 **필터** · **`liveE2eHarness.test`** regression lock
- **내 화면/업무에 영향**: 없음 — **live E2E harness** triage only
- **상태**: FE 완료 · FAQ **Q720** · DEPLOYMENT **§11-3** · ADMIN_GUIDE **§1-4**

<details>
<summary>자세히</summary>

- FE: `7e7c296` (on `b7004ca` singular blocker)
- before: **`liveE2eOperationBlockers: "none, bootstrap-unavailable"`** → false blocker count
- after: **`bootstrap-unavailable` only** — **`liveE2eOperationReason: "none"`** also neutral

</details>

### ✅ UXD-165 Staff schedule a11y + refund fee preview CSS (`bee97b9`)
- **에이전트**: UXD
- **한 일**: **`StaffMonthlySchedulePage`** — **`role="group" aria-label="근무 요약"`** · **`aria-busy={loading}`** on 조회 · **`components.css`** — **`.ds-refund-fee-preview`** grid·surface-muted·forced-colors (FE-16)
- **내 화면/업무에 영향**: **직원 근무일정표**·**환불 처리 Modal** — 스크린리더·고대비 표시 개선
- **상태**: FE 완료 · FAQ **Q717·Q712 deepen** · USER_MANUAL **§4-7** · ADMIN_GUIDE **§6-2-21**

<details>
<summary>자세히</summary>

- FE: `bee97b9` — 2-file +45/-2 · US-R09 `@33944e4` a11y regression fix
- CSS: **`RefundRecordModal`** fee preview `<dl>` alignment restore

</details>

### 📄 TWR 375차 — ops 운영 문서 보강 (doc-only)
- **에이전트**: TWR
- **한 일**: **Q717 신규** — **G-STAFF-MONTHLY-SCHEDULE-FE-WIRE** `/staff/schedules` (`33944e4`) · **Q718 신규** — singular **`liveE2eOperationBlocker`** merge (`b7004ca`) · **Q713 deepen** — BE **`allow-recovered-auth`** health/probe align (`3342938`) · baseline **`3342938`/`b7004ca`**
- **내 화면/업무에 영향**: 없음 — 문서만 갱신
- **상태**: FAQ **Q717·Q718·Q713 deepen** · USER_MANUAL **§1-3·§4-7-0c·StaffContextNav** · ADMIN_GUIDE **§1-4·§6-2** · DEPLOYMENT **§1-4·§11-3** · README **§6**

<details>
<summary>자세히</summary>

- 대상: **케어포 8-2 근무일정표 FE closure** · **live E2E blocker shape variants** (plural string · singular key)
- P2 carry: **program reports FE `branchId`** · **7-5 live PG** · **J03 Solapi live dispatch** · **M6 6-2~6-4 `/safety/*`**

</details>

### ✅ G-STAFF-MONTHLY-SCHEDULE-FE-WIRE (`33944e4`)
- **에이전트**: COD
- **한 일**: **`StaffMonthlySchedulePage`** — **`/staff/schedules`** · **`StaffContextNav`「근무일정표」** · **`fetchVisitsApi`** PLAN 일정 직원별·월별 조회 · **`StaffNotificationDispatchPanel`** G-SMS message_kind=21 · **`StaffMonthlySchedulePage.test`**
- **내 화면/업무에 영향**: **직원 관리** — 케어포 **8-2 근무일정표** 화면에서 **확정 방문 일정(PLAN)** 월간 조회·**월간 일정표 알림톡** 발송
- **상태**: FE 완료 · FAQ **Q717** · USER_MANUAL **§4-7-0c** · ADMIN_GUIDE **§6-2-21** · DEPLOYMENT **§1-4**

<details>
<summary>자세히</summary>

- FE: `33944e4` — 8-file +535L · Route **118** · page **93**
- data: **`GET /api/v1/visits?from=&to=&branchId=&scheduleKind=PLAN`** — 일정 등록·수정은 **`/visits`**
- RBAC: 조회·발송 **`hq_admin`·`branch_admin`·`social_worker`**

</details>

### ✅ QA-B95 legacy singular operation blocker keys (`b7004ca`)
- **에이전트**: COD
- **한 일**: **`liveBackendProbe.extractLiveE2eHealthFields`** — **`liveE2eOperationBlocker`**(singular) + **`liveE2eOperationBlockers`** merge · **`liveConfig.getLiveE2eOperationBlockers`** — persisted **`liveE2eOperationBlocker`/`liveE2eEffectiveOperationBlocker`** fallback · **`liveE2eHarness.test`** regression lock
- **내 화면/업무에 영향**: 없음 — **live E2E harness** triage only
- **상태**: FE 완료 · FAQ **Q718** · DEPLOYMENT **§11-3** · ADMIN_GUIDE **§1-4**

<details>
<summary>자세히</summary>

- FE: `b7004ca` (on `33944e4` staff schedule)
- before: health **`liveE2eOperationBlocker`** only → **빈 blocker 배열** → false-ready/silent skip
- after: singular + plural **dedupe merge**

</details>

### ✅ QA-B95 BE honor recovered auth in health and live-e2e probe (`3342938`)
- **에이전트**: COD
- **한 일**: **`ogada.live-e2e.allow-recovered-auth`** (기본 **`true`**) — bootstrap **disabled** 이어도 **`LiveE2eBootstrapService` bean** 존재 시 **full operation gate** 평가 · health **`liveE2eAllowRecoveredAuth`** · **`HealthControllerTest`·`LiveE2eControllerTest`** regression lock
- **내 화면/업무에 영향**: 없음 — **health/probe diagnostics** · FE auth-recovery harness와 **BE raw readiness align**
- **상태**: BE 완료 · FAQ **Q713 deepen** · DEPLOYMENT **§1-4·§11-3** · ADMIN_GUIDE **§1-4**

<details>
<summary>자세히</summary>

- BE: `3342938` (on `49fe2e7` program reports branch filter)
- env: **`OGADA_LIVE_E2E_ALLOW_RECOVERED_AUTH`** · **`LIVE_E2E_ALLOW_RECOVERED_AUTH`**
- pairs with FE **`liveE2eEffectiveOperationReady`** auth-recovery filter (Q713·Q716·Q718 cluster)

</details>

### 📄 TWR 374차 — ops 운영 문서 보강 (doc-only)
- **에이전트**: TWR
- **한 일**: **Q716 신규** — **QA-B95 string-form operation blocker normalize** (`2c9abd6`·`bd3253a`) · **Q713 deepen** — probe state **`.live-backend-state.json`** string blocker persistence · baseline **`49fe2e7`/`bd3253a`**
- **내 화면/업무에 영향**: 없음 — 문서만 갱신
- **상태**: FAQ **Q716·Q713 deepen** · DEPLOYMENT **§11-3** · ADMIN_GUIDE **§1-4 live E2E harness** · README **§6**

<details>
<summary>자세히</summary>

- 대상: **IT live E2E triage** — health **`liveE2eOperationBlockers`** 가 **문자열**(`comma`/`semicolon`/`newline`)로 내려와도 harness가 **개별 blocker** 로 파싱
- P2 carry: **program reports FE `branchId`** · **7-5 live PG** · **J03 Solapi live dispatch** · **M6 6-2~6-4 `/safety/*`**

</details>

### ✅ QA-B95 string-form operation blocker normalize (`bd3253a` · carry `2c9abd6`)
- **에이전트**: COD
- **한 일**: **`liveBackendProbe.extractLiveE2eHealthFields`** — health **`liveE2eOperationBlockers`** **string·array** 모두 **`normalizeOperationBlockers`** (`2c9abd6`) · **`liveConfig.getLiveE2eOperationBlockers`**·**`liveGlobalSetup`** — persisted probe state **string blocker** split (`bd3253a`) · **`liveE2eHarness.test`** regression lock
- **내 화면/업무에 영향**: 없음 — **live E2E harness** triage only
- **상태**: FE 완료 · FAQ **Q716** · DEPLOYMENT **§11-3** · ADMIN_GUIDE **§1-4**

<details>
<summary>자세히</summary>

- FE: `2c9abd6` (`liveBackendProbe.js`) → `bd3253a` (`liveConfig.js`·`liveGlobalSetup.js`)
- split: **`/[,\\n;]+/`** — 예 `"bootstrap-unavailable; guardian-auth-not-ready, g21-seed-missing"` → **3개 blocker**
- before: string-form → **빈 배열** → suite **silent false-ready** 또는 **generic skip**

</details>

## 2026-06-25

### 📄 TWR 373차 — ops 운영 문서 보강 (doc-only)
- **에이전트**: TWR
- **한 일**: **Q714 deepen** — **5-9 group-history** V179 membership 집계 (`337453d`) · **Q715 신규** — program reports **`branchId`** query (`49fe2e7`) · **Q713 deepen** — **`liveBackendProbe` health reason** (`f74a6e7`) · baseline **`49fe2e7`/`f74a6e7`**
- **내 화면/업무에 영향**: 없음 — 문서만 갱신
- **상태**: FAQ **Q714 deepen·Q715·Q713 deepen** · USER_MANUAL **§1-3·§5-9** · ADMIN_GUIDE **§10-11-2** · DEPLOYMENT **§1-4·§11-3** · README **§6**

<details>
<summary>자세히</summary>

- 대상: **프로그램 리포트 5-9**·**HQ 지점 스코프 API**·**live E2E triage** — BNK-620~621 G-REPORT-DENSITY deepen
- P2 carry: **5-9 그룹 CRUD UI** (G-PROGRAM-GROUP-CONFIG P3) · **program reports FE `branchId`** · **7-5 live PG** · **J03 Solapi live dispatch**

</details>

### ✅ G-REPORT-DENSITY program report branch filter (`49fe2e7`)
- **에이전트**: COD
- **한 일**: **`ProgramReportController`** — 4 GET **`/programs/reports/*`** 에 optional **`branchId`** query · **`resolveBranchScope`** JWT 검증 · **`ProgramReportControllerRoutingTest`**·**`ProgramReportServiceTest`** regression lock
- **내 화면/업무에 영향**: **프로그램 리포트** — Swagger·API로 **명시 지점** 집계 가능 · UI는 **활성 지점** 기준 유지 (P2)
- **상태**: BE 완료 · FAQ **Q715** · ADMIN_GUIDE **§10-11-2** · DEPLOYMENT **§1-4**

<details>
<summary>자세히</summary>

- BE: `49fe2e7` (on `337453d` group-history fill)
- scope: **`branchId` 생략** → JWT active branch · **지정 시** `validateBranchReadScope` · 스코프 밖 → **403**

</details>

### ✅ G-REPORT-DENSITY 5-9 group-history fill (`337453d`)
- **에이전트**: COD
- **한 일**: **V179** `program_client_groups`·`program_client_group_members` · **`aggregateHistoryWindows`** → **`GET /programs/reports/group-history`** **`groupConfigAvailable=true`** · 행 **`groupName`·`effectiveFrom`·`effectiveTo`·`clientCount`**
- **내 화면/업무에 영향**: **프로그램 리포트 5-9** — 멤버십 데이터 있으면 **그룹 이력 표** 표시 · 없으면 **빈 목록** (P3 warning 제거)
- **상태**: BE 완료 · FAQ **Q714 deepen** · USER_MANUAL **§5-9** · ADMIN_GUIDE **§10-11-2** · DEPLOYMENT **§1-4**

<details>
<summary>자세히</summary>

- BE: `337453d` (on `0e55f3b` bootstrap probe)
- migration: **V179** — US-P01·G-PROGRAM-GROUP-CONFIG read path · **그룹 등록 UI는 P3**
- empty: memberships 없음 → **`items:[]`** · **`groupConfigAvailable=true`**

</details>

### ✅ QA-B95 live E2E health reason surfacing (`f74a6e7`)
- **에이전트**: COD
- **한 일**: **`liveBackendProbe.js`** — backend **reachable·`ready=false`** 시 **`body.reason`** 또는 **`liveE2eOperationReason`** 을 skip 메시지에 노출 · **`status=UP`·`ready` 미명시** 시 ready guard · **`liveE2eHarness.test`** regression lock
- **내 화면/업무에 영향**: 없음 — **live E2E harness** triage only
- **상태**: FE 완료 · FAQ **Q713 deepen** · DEPLOYMENT **§11-3**

<details>
<summary>자세히</summary>

- FE: `f74a6e7` (on `75c0f51` bootstrap-unavailable recovery)
- probe: **`providedReason || operationReason || "backend reachable but not ready"`**

</details>

### 📄 TWR 372차 — ops 운영 문서 보강 (doc-only)
- **에이전트**: TWR
- **한 일**: **Q713 deepen** — **`bootstrapServiceAvailable` probe field** (`0e55f3b`) · **`bootstrap-unavailable` blocker auth-recovery filter** (`75c0f51`) · **baseline 정합** — FAQ·DEPLOYMENT·ADMIN **`0e55f3b`/`75c0f51`**
- **내 화면/업무에 영향**: 없음 — 문서만 갱신
- **상태**: FAQ **Q713 deepen** · DEPLOYMENT **§1-4·§11-3** · ADMIN_GUIDE **§1-4·live E2E harness** · README **§6**

<details>
<summary>자세히</summary>

- 대상: **IT live E2E triage** — bootstrap **disabled** vs **bean missing** vs **auth-recovered false skip** 구분
- P2 carry: **5-9 group-history fill** · **7-5 live PG** · **J03 Solapi live dispatch** · **M6 6-2~6-4 `/safety/*`**

</details>

### ✅ QA-B95 bootstrap-unavailable blocker recovery (`75c0f51`)
- **에이전트**: COD
- **한 일**: **`liveConfig.js`·`liveGlobalSetup.js`** — **`bootstrap-unavailable`** label을 **`bootstrap-disabled`/`bootstrap-service-unavailable`** 과 동일하게 **auth 복구 시 recoverable** 처리 · **`liveE2eHarness.test`** regression lock
- **내 화면/업무에 영향**: 없음 — **live E2E harness** only
- **상태**: FE 완료 · FAQ **Q713 deepen** · DEPLOYMENT **§11-3**

<details>
<summary>자세히</summary>

- FE: `75c0f51` (on `15a3b7f` Q714 program reports)
- tests: **`liveE2eHarness.test`** — **`bootstrap-unavailable`** only blocker + staff auth recovered → effective ready

</details>

### ✅ QA-B95 bootstrap service availability probe (`0e55f3b`)
- **에이전트**: COD
- **한 일**: **`LiveE2eProbeResponse.bootstrapServiceAvailable`** — **`bootstrapEnabled`**(설정) vs **runtime bean wiring**(서비스) 분리 · bean missing 시 **`bootstrapEnabled=true`·`bootstrapServiceAvailable=false`** · **`LiveE2eControllerTest`** lock
- **내 화면/업무에 영향**: 없음 — **health/probe diagnostics** only
- **상태**: BE 완료 · FAQ **Q713 deepen** · DEPLOYMENT **§1-4·§11-3** · ADMIN_GUIDE **§1-4**

<details>
<summary>자세히</summary>

- BE: `0e55f3b` (on `650801b` Q714 program reports API)
- probe: disabled → **`bootstrapEnabled=false`** · enabled·bean null → **`bootstrapEnabled=true`·`bootstrapServiceAvailable=false`** · detail **`bootstrap=service-unavailable`**

</details>

### 📄 TWR 371차 — ops 운영 문서 보강 (doc-only)
- **에이전트**: TWR
- **한 일**: **Q714 신규** — **G-REPORT-DENSITY M5 program reports** (5-7~5-10) · **USER_MANUAL §5-9** · **ADMIN_GUIDE §10-11-2** · **DEPLOYMENT §1-4 smoke** · baseline **`650801b`/`15a3b7f`**
- **내 화면/업무에 영향**: 없음 — 문서만 갱신
- **상태**: FAQ **Q714** · USER_MANUAL **§5-9·§1-3** · ADMIN_GUIDE **§10-11-2** · DEPLOYMENT **§1-4** · README **§6**

<details>
<summary>자세히</summary>

- 대상: **케어포 5-7~5-10 프로그램 리포트** 현장·IT — BNK-620 M5 report density gap closure
- P2 carry: **5-9 group-history shell 집계** (G-PROGRAM-GROUP-CONFIG P3) · **7-5 live PG** · **J03 Solapi live dispatch** · **M6 6-2~6-4 `/safety/*`**

</details>

### ✅ G-REPORT-DENSITY M5 program report FE wire (`15a3b7f`)
- **에이전트**: COD
- **한 일**: **`ProgramReportsPage`** — **`GET /api/v1/programs/reports/*`** 4종 연동 · **`ProgramReportNav`** · **`ProgramReportPanel`** · **`RecordsContextNav`** 「프로그램 리포트」 · routes **`/programs/reports/{participations|provision-records|group-history|schedules}`**
- **내 화면/업무에 영향**: **프로그램 급여** — **5-7~5-10 기간별 리포트** 화면 확인·인쇄 가능 · **5-9 그룹 이력** — shell 안내만 (집계 P3)
- **상태**: FE 완료 · FAQ **Q714** · USER_MANUAL **§5-9**

<details>
<summary>자세히</summary>

- FE: `15a3b7f` (on `5914b2f` Q709/Q710 wire)
- tests: **`ProgramReportsPage.test`** · **`ProgramReportPanel.test`** · **`programReportServices.test`**

</details>

### ✅ G-REPORT-DENSITY M5 program report API (`650801b`)
- **에이전트**: COD
- **한 일**: **`ProgramReportController`** — 4 GET **`/api/v1/programs/reports/*`** (participations·schedules·provision-records·group-history shell) · **`ProgramReportService`** · **`ProgramReportControllerRoutingTest`**·**`ProgramReportServiceTest`**
- **내 화면/업무에 영향**: **프로그램 급여** — API·Swagger로 **5-7~5-10** 기간 집계 조회 · **5-9** — `groupConfigAvailable=false` shell
- **상태**: BE 완료 · FAQ **Q714** · ADMIN_GUIDE **§10-11-2**

<details>
<summary>자세히</summary>

- BE: `650801b` (on `9f67954` bootstrap enforcement)
- RBAC: **`hq_admin`·`branch_admin`·`social_worker`** · **`caregiver`/`guardian` → 403**
- date default: **당월 1일~오늘** · `toDate < fromDate` → **`422`**

</details>

### 📄 TWR 370차 — ops 운영 문서 보강 (doc-only)
- **에이전트**: TWR
- **한 일**: **Q705 deepen** — §1-5·§5-26 bathing **FE full-stack ✅** 정합 (`3d7f13b`) · **Q712 deepen** — §5-10-0 M7 **7-9 refund fee** lifecycle · **baseline 정합** — FAQ·DEPLOYMENT **`9f67954`/`5914b2f`** · README §6 현행화
- **내 화면/업무에 영향**: 없음 — 문서만 갱신
- **상태**: USER_MANUAL **§1-5·§5-10-0·§5-26** · FAQ **baseline** · DEPLOYMENT **§1-4** · README **§6**

<details>
<summary>자세히</summary>

- 대상: **목욕 평가지표 27**·**7-9 환불 수수료** 현장 인수 — 369차 이후 잔여 P2 라벨 정리
- P2 carry: **7-5 live PG** · **J03 Solapi live dispatch** · **M6 6-2~6-4 `/safety/*`**

</details>

### 📄 TWR 369차 — ops 운영 문서 보강 (doc-only)
- **에이전트**: TWR
- **한 일**: **Q709 deepen** — **`EasyPayProviderCatalogPanel`** catalog FE wire (`5914b2f`) · **Q710 deepen** — **`TransportParityRulesPanel`** `/transport/service-fees` mount (`5914b2f`) · **Q713 deepen** — **`enforce-bootstrap-readiness`** BE config (`9f67954`) · baseline **`9f67954`/`5914b2f`**
- **내 화면/업무에 영향**: 없음 — 문서만 갱신
- **상태**: FAQ **Q709·Q710·Q713 deepen** · USER_MANUAL **§4-6·§5-8-1** · ADMIN_GUIDE **§10-14·G16** · DEPLOYMENT **§1-4·§11-3**

<details>
<summary>자세히</summary>

- 대상: **7-5 간편결제 catalog**·**G16 NHIS #44 parity rules** 현장·IT — P2 carry **closure**
- P2 carry: 없음 (Q709·Q710 FE wire 완료)

</details>

### ✅ G2/7-5 easy-pay provider catalog FE wire (`5914b2f`)
- **에이전트**: COD
- **한 일**: **`EasyPayProviderCatalogPanel`** — **`GET /billing/easy-pay/provider-catalog`** 연동 · CARD·KAKAO_PAY 표 · **`pgMode`** badge · **`EasyPayPage`** 상단 mount · **`TransportParityRulesPanel`** — **`/transport/service-fees`** mount · **`description`/`bodyKo` 정규화** · **`TransportServiceFeePanel`** parity 중복 제거
- **내 화면/업무에 영향**: **7-5 간편결제** — **PG 제공자 catalog** 화면 확인 가능 · **이동서비스비** — **NHIS #44 산정 기준** 동적 catalog 표시
- **상태**: FE 완료 · FAQ **Q709·Q710 deepen** · USER_MANUAL **§4-6·§5-8-1**

<details>
<summary>자세히</summary>

- FE: `5914b2f` (on `e070c45` Q713 effective readiness)
- tests: **`EasyPayProviderCatalogPanel.test`** · **`TransportParityRulesPanel.test`** · **`TransportServiceFeePage.test`**

</details>

### ✅ QA-B95 bootstrap readiness enforcement (`9f67954`)
- **에이전트**: COD
- **한 일**: **`ogada.live-e2e.enforce-bootstrap-readiness`** (기본 **`true`**) — **`false`** 시 bootstrap disabled·service-unavailable blocker **미적용** · health/probe **`liveE2eBootstrapReadinessEnforced`** · **`HealthControllerTest`**·**`LiveE2eControllerTest`** regression lock
- **내 화면/업무에 영향**: 없음 — **live E2E harness·health probe** only
- **상태**: BE 완료 · FAQ **Q713 deepen** · DEPLOYMENT **§4-3·§11-3**

<details>
<summary>자세히</summary>

- BE: `9f67954` (on `79725eb` feePolicyCode validation)
- env: **`OGADA_LIVE_E2E_ENFORCE_BOOTSTRAP_READINESS`** · **`LIVE_E2E_ENFORCE_BOOTSTRAP_READINESS`**

</details>

### 📄 TWR 368차 — ops 운영 문서 보강 (doc-only)
- **에이전트**: TWR
- **한 일**: **Q712 deepen** — **`feePolicyCode` `@Pattern` Bean Validation** (`79725eb`) · **Q713** — **live E2E effective operation readiness** after auth recovery (`e070c45`) · baseline **`79725eb`/`e070c45`**
- **내 화면/업무에 영향**: 없음 — 문서만 갱신
- **상태**: FAQ **Q712·Q713** · ADMIN_GUIDE **§10-4** · DEPLOYMENT **§1-4·§11-3**

<details>
<summary>자세히</summary>

- 대상: **7-9 환불 API 직접 호출**·**IT live E2E triage** 담당
- P2 carry: **easy-pay provider-catalog FE wire** · **`TransportParityRulesPanel` page mount**

</details>

### ✅ QA-B95 — honor recovered auth for live operation readiness (`e070c45`)
- **에이전트**: COD
- **한 일**: **`liveGlobalSetup`** — auth 복구 후 **`liveE2eEffectiveOperationReady`·`liveE2eEffectiveOperationBlockers`** persist · **`liveConfig.isLiveOperationReady()`** effective 필드 우선 · **`liveE2eHarness.test`** regression lock
- **내 화면/업무에 영향**: 없음 — **live E2E harness** only (QA-B95 operation 승격 triage)
- **상태**: FE 완료 · FAQ **Q713** · DEPLOYMENT **§11-3**

<details>
<summary>자세히</summary>

- FE: `e070c45` (on `cadd74a` Q712 wire)
- ignorable when auth recovered: **`bootstrap-disabled`** · staff/guardian bootstrap·credential recovery labels

</details>

### ✅ 7-9 refund fee policy input validation (`79725eb`)
- **에이전트**: COD
- **한 일**: **`RecordCopayRefundRequest.feePolicyCode`** — **`@Pattern`** 3종 catalog code only · case-insensitive · invalid → **`400`**「허용되지 않는 환불 수수료 정책입니다.」 · **`BillingServiceTest`** net mismatch regression
- **내 화면/업무에 영향**: **7-9 환불** — Swagger·API 직접 호출 시 **오타 policy code 거부** (UI는 catalog Select만 노출)
- **상태**: BE 완료 · FAQ **Q712 deepen** · ADMIN_GUIDE **§10-4**

<details>
<summary>자세히</summary>

- BE: `79725eb` (on `aeecc1b` net validation)
- allowed: `CARD_VOID_SAME_MONTH` · `CARD_PARTIAL_OR_EXPIRED` · `BANK_OR_CMS_TRANSFER`

</details>

### 📄 TWR 367차 — ops 운영 문서 보강 (doc-only)
- **에이전트**: TWR
- **한 일**: **Q712 deepen** 7-9 **환불 수수료 full-stack** — **`RefundRecordModal`** catalog·preview·`feePolicyCode` wire (`cadd74a`) · BE **net amount validation** (`aeecc1b`) · baseline **`aeecc1b`/`cadd74a`**
- **내 화면/업무에 영향**: 없음 — 문서만 갱신
- **상태**: FAQ **Q712·Q261 deepen** · USER_MANUAL **§5-10** · ADMIN_GUIDE **§10-4** · DEPLOYMENT **§1-4·§8-1**

<details>
<summary>자세히</summary>

- 대상: **7-9 환불** 현장·IT — 카드/계좌/CMS 환불 시 **실환불액(net)** 자동 계산·검증
- P2 carry: **easy-pay provider-catalog FE wire** · **`TransportParityRulesPanel` page mount**

</details>

### ✅ G-REFUND-FEE-FE-WIRE — RefundRecordModal catalog + preview (`cadd74a`)
- **에이전트**: COD
- **한 일**: **`RefundRecordModal`** — **`GET/POST /billing/copay/refund-fee-*`** 연동 · 결제수단별 **호환 정책 필터** · **본인부담금/수수료/실환불액** 미리보기 · **`feePolicyCode`** 제출 · **`RefundRecordModal.test`**·**`copayRefundFee.js`**
- **내 화면/업무에 영향**: **7-9 환불** — **`/billing/claims/:id`「환불 처리」** 에서 **KCP 수수료 차감 net 금액** 확인·저장 가능 (Q712 FE closure)
- **상태**: FE 완료 · FAQ **Q712 deepen** · USER_MANUAL **§5-10**

<details>
<summary>자세히</summary>

- FE: `cadd74a` (on `2adae59` BE catalog)
- lineage: EASY_PAY→CARD 정책 · BANK_TRANSFER/CMS→BANK_OR_CMS 정책

</details>

### ✅ 7-9 refund fee net amount validation (`aeecc1b`)
- **에이전트**: COD
- **한 일**: **`POST /api/v1/billing/claims/{claimId}/refunds`** — 선택 **`feePolicyCode`** · 결제수단 호환 검증 · **net amount 일치** 필수 · **`BillingServiceTest`** +122L · **`CopayRefundFeePolicyCatalogTest`** deepen
- **내 화면/업무에 영향**: **7-9 환불** — 카드/계좌/CMS 환불 시 **수수료 정책과 불일치 금액 거부** (`422` BusinessRule)
- **상태**: BE 완료 · FAQ **Q712·Q261 deepen** · ADMIN_GUIDE **§10-4**

<details>
<summary>자세히</summary>

- BE: `aeecc1b` (on `2adae59` catalog)
- `feePolicyCode` 생략 시 기존 동작 — **환불 금액 = 본인부담금 전액**

</details>

### 📄 TWR 366차 — ops 운영 문서 보강 (doc-only)
- **에이전트**: TWR
- **한 일**: **Q712** 7-9 **`GET/POST /billing/copay/refund-fee-policy-catalog`** KCP 환불 수수료 catalog·preview (`2adae59`) · **Q705 deepen** 목욕 **전·후 관찰 폼·지표27 패널 FE wire** (`3d7f13b`) · baseline **`2adae59`/`3d7f13b`**
- **내 화면/업무에 영향**: 없음 — 문서만 갱신
- **상태**: FAQ **Q712·Q705 deepen** · USER_MANUAL **§5-10·§5-26** · ADMIN_GUIDE **§6-2-16·§10-4** · DEPLOYMENT **§1-4·§8-1**

<details>
<summary>자세히</summary>

- 대상: **7-9 환불 수수료 안내**·**목욕 평가지표 27** 현장 담당
- P2 carry: **refund-fee catalog FE wire** (`RefundRecordModal`) · **easy-pay provider-catalog FE wire** · **`TransportParityRulesPanel` page mount**

</details>

### ✅ US-O01 — bathing indicator-27 + pre/post observation FE wire (`3d7f13b`)
- **에이전트**: COD
- **한 일**: **`BathingSchedulePage`** — **`BathingScheduleIndicator27Panel`** compliance 패널 · **`BathingScheduleForm`** **`preObservationNotes`/`postObservationNotes`** 필드 · **`COMPLETED` 시 필수 검증** · **`BathingSchedulePage.test`**·**`BathingScheduleIndicator27Panel.test`**
- **내 화면/업무에 영향**: **목욕 일정(L02_M03)** — 화면에서 **전·후 관찰 입력**·**평가지표 27 준수 표** 확인 가능 (Q705 FE closure)
- **상태**: FE 완료 · FAQ **Q705 deepen** · USER_MANUAL **§5-26**

<details>
<summary>자세히</summary>

- FE: `3d7f13b` (US-O01 wire on `e12b084` BE)
- lineage: V177 pre/post guard · indicator-27 compliance API

</details>

### ✅ G-REFUND-FEE-DEDUCTION — 7-9 copay refund fee policy catalog API (`2adae59`)
- **에이전트**: COD
- **한 일**: **`GET /api/v1/billing/copay/refund-fee-policy-catalog`** — KCP **3종 정책** (`CARD_VOID_SAME_MONTH`·`CARD_PARTIAL_OR_EXPIRED`·`BANK_OR_CMS_TRANSFER`) · **`POST …/refund-fee-preview`** — gross→fee→net 계산 · **`CopayRefundFeePolicyCatalogTest`**·RBAC·routing lock
- **내 화면/업무에 영향**: **7-9 환불** — Swagger·IT에서 **PG 수수료 차감 net 환불액** 미리보기 가능 · **실제 환불 기록(`POST …/refunds`)은 기존과 동일** — **catalog FE wire P2** (Q712)
- **상태**: BE 완료 · FAQ **Q712** · ADMIN_GUIDE **§10-4**

<details>
<summary>자세히</summary>

- BE: `2adae59` (v2/7-9, carefor KCP parity)
- RBAC: **`HQ_ADMIN`·`BRANCH_ADMIN`** — **`SOCIAL_WORKER` 403**
- catalog-only: **live PG 정산 없음** · disclaimer KCP verbatim

</details>

### 📄 TWR 365차 — ops 운영 문서 보강 (doc-only)
- **에이전트**: TWR
- **한 일**: **Q711** 연차 **`branchName` 공백·trim fallback** (`58f3858`) · **Q709 deepen** **`EasyPayControllerRoutingTest`** RBAC·`pgMode` lock (`5a5174a`) · **QA-B312** vitest isolation carry · baseline **`5a5174a`/`58f3858`**
- **내 화면/업무에 영향**: 없음 — 문서만 갱신
- **상태**: FAQ **Q711** · USER_MANUAL **§4-7-0a** · ADMIN_GUIDE **§10-14** · DEPLOYMENT **§8-1**

<details>
<summary>자세히</summary>

- 대상: 현장 **연차휴가 조회 지점** 표시·IT **7-5 provider-catalog** 스모크 담당
- P2 carry: **easy-pay provider-catalog FE wire** · **`TransportParityRulesPanel` page mount** · **목욕 전후관찰 FE** (Q705)

</details>

### ✅ QA-B312 — annual leave branch scope whitespace fallback (`58f3858`)
- **에이전트**: COD
- **한 일**: **`StaffAnnualLeavePage`** — **`normalizeBranchScope`** 가 API·user **`branchId`·`branchName` trim** · 공백만인 **`branchName`** 시 **`BranchScopeNotice`** 가 **지점 ID 라벨**로 fallback · **`StaffAnnualLeavePage.test`** whitespace regression
- **내 화면/업무에 영향**: **연차휴가** — API가 **공백 지점명**을 반환해도 **「조회 지점」** 이 사라지지 않음 (Q711)
- **상태**: FE 완료 · FAQ **Q711** · USER_MANUAL **§4-7-0a**

<details>
<summary>자세히</summary>

- FE: `58f3858` (QA-B312 deepen, `892122d` isolation carry)
- lineage: B266/B270/B291/B312 vitest pollution + branch scope UX

</details>

### ✅ easy-pay provider-catalog routing test lock (`5a5174a`)
- **에이전트**: COD
- **한 일**: **`EasyPayControllerRoutingTest`** — **`GET /billing/easy-pay/provider-catalog`** WebMvcTest — **`pgMode`·`entries[]`·`paymentImplementedCount`** · **`HQ_ADMIN`·`BRANCH_ADMIN` 200** · **`GUARDIAN` 403**
- **내 화면/업무에 영향**: 없음 — CI·routing 회귀 방지 · **Swagger·스모크 동작 동일** (Q709)
- **상태**: BE 완료 · FAQ **Q709 deepen** · ADMIN_GUIDE **§10-14** · DEPLOYMENT **§8-1**

<details>
<summary>자세히</summary>

- BE: `5a5174a` (test lock on `56831fc` catalog API)
- complements: **`RoleBasedControllerAccessTest`** · **`EasyPayProviderCatalogServiceTest`**

</details>

### 📄 TWR 364차 — ops 운영 문서 보강 (doc-only)
- **에이전트**: TWR
- **한 일**: **Q709** 7-5 **`GET /billing/easy-pay/provider-catalog`** (케어포 npay_manage parity) · **Q710** G16 **`TransportParityRulesPanel`** scaffold·**`description` wire P2 carry** · **V178** CMS collection·목욕 관찰 DB CHECK · **QA-B312** vitest isolation · baseline **`56831fc`/`892122d`**
- **내 화면/업무에 영향**: 없음 — 문서만 갱신
- **상태**: FAQ **Q709·Q710** · USER_MANUAL **§1-3·§4-6·§5-8-1** · ADMIN_GUIDE **§6-2-16·§10-14** · DEPLOYMENT **§1-3·§1-4**

<details>
<summary>자세히</summary>

- 대상: **7-5 간편결제**·**G16 parity-rules**·**Flyway V178** 배포·QA 담당
- P2 carry: **easy-pay provider-catalog FE wire** · **`TransportParityRulesPanel` page mount** · **목욕 전후관찰 FE** (Q705)

</details>

### ✅ G-EASYPAY-PROVIDER-CATALOG — 7-5 provider catalog API (`56831fc`)
- **에이전트**: COD
- **한 일**: **`GET /api/v1/billing/easy-pay/provider-catalog`** — **`EasyPayProviderCatalog.CAREFOR_PARITY_ENTRIES`** CARD·KAKAO_PAY · 응답 **`entries[]`·`paymentImplementedCount`·`totalCount`·`pgMode`** (stub/live) · **`RoleBasedControllerAccessTest`** · **`EasyPayProviderCatalogServiceTest`**
- **내 화면/업무에 영향**: **간편결제(7-5)** — Swagger·IT에서 **지원 PG 수단 catalog** 확인 가능 · **UI는 기존 CARD/KAKAO_PAY 선택** (`EasyPayPanel`) — **provider-catalog FE wire P2** (Q709)
- **상태**: BE 완료 · FAQ **Q709** · USER_MANUAL **§4-6**

<details>
<summary>자세히</summary>

- BE: `56831fc` (v2/7-5)
- RBAC: **`HQ_ADMIN`·`BRANCH_ADMIN`** — **`GUARDIAN` 403**
- catalog: **2/2 `paymentImplemented=true`** · route **`/billing/easy-pay`**

</details>

### ✅ V178 — CMS collection + bathing observation DB integrity (`3c1fdce`)
- **에이전트**: COD/DBA
- **한 일**: **V178** — **`cms_collection_requests`** amount·lifecycle·FCMS tx·bank_code CHECK 9건 · **`bathing_schedules`** pre/post observation **nonempty** CHECK 2건 (V177 보완)
- **내 화면/업무에 영향**: 없음 — raw SQL·webhook 우회 방어 · 앱 동작 동일
- **상태**: BE 완료 · ADMIN_GUIDE **§6-2-16** · DEPLOYMENT **§1-3**

<details>
<summary>자세히</summary>

- BE: `3c1fdce` (db/V178)
- 패턴: V110 easy_pay · V155 waypoint · V158 cash_receipt 동일 defense-in-depth

</details>

### ✅ UXD-163 — TransportParityRulesPanel + NHIS audit badge CSS (`7b4c6f9`)
- **에이전트**: COD
- **한 일**: **`TransportParityRulesPanel.jsx`** — **`fetchTransportServiceFeeParityRulesApi`** · **`labelKo`/`descriptionKo`/`bodyKo` normalize** · static fallback · **`components.css`** **`ds-nhis-alt-key-badge`**
- **내 화면/업무에 영향**: **이동서비스비** — **전용 parity 패널 컴포넌트 준비** · **`/transport/service-fees` page mount P2** · 현재 **`TransportServiceFeePanel`** 은 **`bodyKo` 매핑** 유지 (Q710)
- **상태**: FE partial · FAQ **Q710**

<details>
<summary>자세히</summary>

- FE: `7b4c6f9` (UXD-163)
- 미연결: **`TransportParityRulesPanel` grep mount 0 hit** — coder 후속 wire

</details>

### ✅ QA-B312 — StaffAnnualLeavePage vitest isolation (`892122d`)
- **에이전트**: COD
- **한 일**: **`StaffAnnualLeavePage.test.jsx`** — branch scope mock·cleanup hardening · full-suite **`조회 지점`** pollution lineage 해소
- **내 화면/업무에 영향**: 없음 — CI·test harness만
- **상태**: FE 완료 · DEPLOYMENT **§8-1** 참고

<details>
<summary>자세히</summary>

- FE: `892122d` (QA-B312)
- lineage: B266/B270/B291 vitest pollution carry

</details>

### 📄 TWR 363차 — ops 운영 문서 보강 (doc-only)
- **에이전트**: TWR
- **한 일**: **Q708** CMS catalog **`EmptyState`** 현장·sysadmin FAQ · **USER_MANUAL §4-6-1** NHIS **자동 매칭 의사결정표** (Q706·Q707) · **§5-26** 목욕 **Swagger 전·후 관찰** 절차 · **§5-8-1** G16 **`description`/`bodyKo` fallback** 안내 · **ADMIN_GUIDE**·**DEPLOYMENT**·**README** 동기화
- **내 화면/업무에 영향**: 없음 — 문서만 갱신 (코드 HEAD **`4963535`/`5bb84a6`** 유지)
- **상태**: FAQ **Q708** · USER_MANUAL **§4-6-1·§5-8-1·§5-26** · ADMIN_GUIDE **§1-4** · DEPLOYMENT **§1-4**

<details>
<summary>자세히</summary>

- 대상: 현장 **NHIS import·CMS·목욕 평가지표 27** 월말 점검 담당
- P2 carry: **`BathingScheduleForm` FE wire** · **G16 `description` FE wire** — 문서에 Swagger·static fallback 대체 절차 명시

</details>

### ✅ G-NHIS-ALT-KEY-AUDIT-BADGE — altKeyMatched API + UI badge (`4963535` · `5bb84a6`)
- **에이전트**: COD
- **한 일**: NHIS import·대사·방문 비교 응답에 **`altKeyMatched: boolean`** 추가 — **`NhisImportRowResponse`·`NhisReconciliationRowResponse`·`NhisVisitScheduleImportRowResponse`·`VisitNhisComparisonItemResponse`** · FE **`NhisAltKeyMatchedBadge`** — **`NhisReconciliationTable`**·**`VisitNhisComparisonDetail`** 수급자명 옆 warning Badge · tooltip **`matchStatusReason` 정본** (`nhisAltKeyMatch.js`)
- **내 화면/업무에 영향**: **NHIS 청구 대사**·**방문 공단 비교** — 마스킹 이름 alt-key로 자동 매칭된 행에 **「대체 매칭됨 — 검증 필요」** 표시 · 운영자 **이름·생년월일 spot-check** 유도 (Q707)
- **상태**: BE+FE 완료 · FAQ **Q707** · USER_MANUAL **§4-6-1** · ADMIN_GUIDE **§10-6**

<details>
<summary>자세히</summary>

- BE: `4963535` (G-NHIS-ALT-KEY-AUDIT-BADGE)
- FE: `5bb84a6` — **`NhisAltKeyMatchedBadge.test`** · **`NhisReconciliationTable.test`** · **`VisitNhisComparisonDetail.test`**
- Badge 라벨: **「대체 매칭됨 — 검증 필요」** · `aria-label`+`title` = **`NhisClientResolver.ALT_KEY_MATCH_REASON`**
- 테스트: **`NhisClientResolverTest.altKeyMatched`** · **`NhisImportServiceTest`** · **`VisitServiceTest`**

</details>

### ✅ G-NHIS-MASKED-NAME-FALLBACK — alt-key client resolution (`37416ac`)
- **에이전트**: COD
- **한 일**: **`NhisClientResolver`** — LTC cert 조회 실패 시 **마스킹 수급자명(`홍*동`) + 생년월일** 또는 **생년월일 + 주민등록 앞 6자리** 로 ogada 이용자 자동 매칭 · **`NhisImportService`**·**`VisitService`** NHIS import 경로 공통 적용 · **`matchStatusReason`** = 「공단 이름 마스킹 — 대체 키(생년월일·이름 패턴)로 매칭됨」
- **내 화면/업무에 영향**: **NHIS 청구내역 import**·**방문일정 import** — 2026 공단 **이름 마스킹** 엑셀에서 **인정번호 누락·불일치**여도 **단일 후보**면 **`MATCHED`** · 대사 표 **「보류 사유」** 열에 alt-key 안내 (Q706)
- **상태**: BE 완료 · FAQ **Q706** · USER_MANUAL **§4-6-1** · ADMIN_GUIDE **§10-6**

<details>
<summary>자세히</summary>

- BE: `37416ac` (G-NHIS-MASKED-NAME-FALLBACK)
- 매칭 순서: **LTC cert** → **마스킹 이름 + birthDate (단 1명)** → **birthDate + residentRegistrationPrefix (단 1명)**
- 패턴: **`NhisMaskedNameMatcher`** — `^[가-힣]\*[가-힣]+$` · 첫·끝 글자 일치
- 테스트: **`NhisClientResolverTest`** · **`NhisImportServiceTest.importShouldMatchClientByMaskedNameAltKeyWhenLtcCertMissing`** · **`VisitServiceTest.importNhisShouldMatchClientByMaskedNameAltKeyWhenLtcCertMissing`**

</details>

### ✅ CMS payment-method-catalog — empty state UX (`9a583ec`)
- **에이전트**: COD
- **한 일**: **`CmsPaymentMethodCatalogPanel`** — catalog **`entries[]` 빈 배열** 시 **`EmptyState`** 「카탈로그 정보 없음」 표시 · 회귀 테스트 추가
- **내 화면/업무에 영향**: **CMS 자동이체** — API가 빈 catalog를 반환해도 **빈 표 대신 안내** (정상 5-method catalog는 기존과 동일, Q701)
- **상태**: FE 완료

<details>
<summary>자세히</summary>

- FE: `9a583ec`
- 테스트: **`CmsPaymentMethodCatalogPanel.test`** — empty entries friendly state

</details>

### ✅ G16 parity-rules — API spec alignment + RBAC (`e4f83af`)
- **에이전트**: COD
- **한 일**: **`GET /api/v1/transport/service-fee-parity-rules`** 응답을 API_SPEC과 일치 — **`rules[].code`·`label`·`description`** · **`social_worker`·`caregiver` 403** (`RoleBasedControllerAccessTest`) · FE **`TransportServiceFeePanel`** 은 아직 **`bodyKo` 매핑** — **P2 wire** (`5a717ac`·`e4f83af`)
- **내 화면/업무에 영향**: **이동서비스비** — **`branch_admin`/`hq_admin`** 만 catalog API 직접 호출 · **사회복지사** Swagger 호출 **403** · 화면 안내 문구는 **static fallback 또는 빈 목록** 가능 (Q703)
- **상태**: BE 완료 · FE **`description` 필드 wire P2** · FAQ **Q703·Q578** 갱신

<details>
<summary>자세히</summary>

- BE: `e4f83af` (BNK-602 · G16)
- 응답: **`TransportServiceFeeParityRuleResponse`** — `code`·`label`·`description` (구 `ruleCode`·`bodyKo` 폐기)
- RBAC: **`HQ_ADMIN`·`BRANCH_ADMIN` only** — `SOCIAL_WORKER` **403** (`e4f83af`)
- 테스트: **`TransportServiceFeeParityCatalogTest`** · **`RoleBasedControllerAccessTest$TransportAccess`**

</details>

### ✅ live E2E — placeholder credential normalization (`5afef2d`)
- **에이전트**: COD
- **한 일**: **`liveConfig.js`**·**`liveGlobalSetup.js`** — placeholder 검사 시 **trim·소문자 정규화** (` Test@Test.com `·` OGADA1234 ` 등) · stale example 값이 auth fallback을 우회하지 않도록 회귀 테스트 추가
- **내 화면/업무에 영향**: 없음 — 스테이징 **`npm run test:live-e2e`** harness만 (FAQ **Q578**)
- **상태**: FE 완료

<details>
<summary>자세히</summary>

- FE: `5afef2d` (QA-B95)
- 테스트: **`liveE2eHarness.test`** — staff·guardian placeholder casing/whitespace variants

</details>

### ✅ G2b CMS collection + G16 parity-rules — FE wire (`9aeedfe`)
- **에이전트**: COD
- **한 일**: **`CmsCollectionPanel`** — **`/billing/cms` → 「가상계좌·다계좌」** 3번째 탭 · **`requestCmsVirtualAccountApi`·`requestCmsMultiAccountSettlementApi`** · 입금 은행 선택·상태 조회 · **`TransportServiceFeePanel`** — **`fetchTransportServiceFeeParityRulesApi`** 로 NHIS #44 4-rule 동적 로드 · **module 7-4 coverage 1.0**
- **내 화면/업무에 영향**: **CMS 자동이체** — 가상계좌·다계좌 정산을 **Swagger 없이 UI**에서 요청 · **이동서비스비 청구** — parity 안내 문구가 **BE catalog와 실시간 동기화** (Q701·Q703·Q704)
- **상태**: FE 완료 · **목욕 전후관찰 FE wire는 P2 carry** (Q705)

<details>
<summary>자세히</summary>

- FE: `9aeedfe` (BNK-602 UXD-162)
- 화면: **`/billing/cms`** — 탭 **등록 관리·CMS 출금·가상계좌·다계좌** · **`CmsCollectionPanel`** · **`ClaimGenerationGuardBanner`** 7-4 선행입금 가드
- API wire: **`fetchTransportServiceFeeParityRulesApi`** · **`requestCmsVirtualAccountApi(claimId, { bankCode })`** · **`requestCmsMultiAccountSettlementApi(claimId)`**
- 테스트: **`CmsCollectionPanel.test`** · **`CmsPage.test`** · **`TransportServiceFeePanel.test`** · **`settingsServices.test`**
- stub: 패널 footnote — **FCMS stub** · live FCMS는 운영 env 후속

</details>

### ✅ US-O01 목욕 전·후 관찰 + 평가지표 27 compliance — BE API (`e12b084`)
- **에이전트**: COD
- **한 일**: **V177** — `bathing_schedules.pre_observation_notes`·`post_observation_notes` 컬럼 · **COMPLETED 시 전·후 관찰 필수** DB CHECK · **`GET /api/v1/care/bathing-schedules/indicator-27-compliance?yearMonth=&clientId=`** — silverangel **평가지표 27**(월 5회+·전후 관찰) 월별 준수 집계
- **내 화면/업무에 영향**: **목욕 일정(L02_M03)** — **제공 완료** 시 API·Swagger에서 **목욕 전·후 상태 관찰** 입력 필요 · **월 5회+ 전후관찰** 준수는 compliance API로 확인 (FE 폼·패널 **P2**, Q705)
- **상태**: BE 완료 · FE **`BathingScheduleForm` wire P2** · FAQ **Q705** · USER_MANUAL **§5-26** 보강

<details>
<summary>자세히</summary>

- BE: `e12b084` (BNK-602 · US-O01)
- V177: `chk_bathing_schedules_completed_requires_pre_post_observation`
- API 응답: **`requiredMonthlyCompletedCount=5`** · **`monthlyFrequencyNote`** · **`prePostObservationNote`** · 이용자별 **`completedCount`·`withPrePostObservationCount`·`indicator27Met`**
- **`422`**: COMPLETED인데 **`preObservationNotes`/`postObservationNotes` 누락** → 「목욕 제공 완료 시 목욕 전·후 상태 관찰 내용을 입력하세요.」
- RBAC: **`HQ_ADMIN`·`BRANCH_ADMIN`·`SOCIAL_WORKER`·`CAREGIVER`**
- 테스트: **`BathingScheduleIndicator27ComplianceTest`** · **`BathingScheduleServiceTest`** · **`MustApiEndpointRoutingTest`**

</details>

---

## 2026-06-24

### ✅ G2b CMS collection methods closure — BE API (`dac8ebd`)
- **에이전트**: COD
- **한 일**: **`POST/GET /billing/cms/claims/{claimId}/virtual-account`** (가상계좌 발급·조회) · **`POST/GET /billing/cms/claims/{claimId}/multi-account-settlement`** (다계좌 정산 요청·조회) — **V176 DB 마이그레이션** · **`CmsPaymentMethodCatalog` 5/5 완성**
- **내 화면/업무에 영향**: **청구 수납** — **가상계좌·다계좌 정산 API 사용 가능** (FE UI는 P2 후속, 현재 Swagger only) · 엔젤 CMS 5-method **모두 지원** (Q704)
- **상태**: BE 완료 · FE UI **P2 후보** · FAQ Q701·Q704 신규 추가 · USER_MANUAL §4-6-3·4-6-4 신규 섹션

<details>
<summary>자세히</summary>

- BE: `dac8ebd` (BNK-595·BNK-596)
- V176 마이그레이션: `virtual_account_issued_at`, `virtual_account_number`, `settlement_requested_at` 컬럼 추가
- **가상계좌**: `POST …/virtual-account` — 청구 CONFIRMED 시 FCMS 가상계좌 발급 · `virtual_account_number`·`issuedAt`·`expiresAt` 반환 · 보호자 입금 시 자동 **`PAID`** 전환
- **다계좌 정산**: `POST …/multi-account-settlement` — 정산 계좌 배열 요청 · 효성 FCMS 정산 완료 시 **`PAID`** 전환
- 테스트: **`CmsVirtualAccountServiceTest`**·**`CmsMultiAccountSettlementServiceTest`** · **`MustApiEndpointRoutingTest`**
- RBAC: `HQ_ADMIN`·`BRANCH_ADMIN` (모두 쓰기 가능)
- stub 환경: `FCMS_PROVIDER=stub` — 응답 시뮬레이션 (실제 입금·정산 없음)

</details>

### ✅ G16 NHIS #44 transport service fee parity rules — BE API (`bd1e87e`)
- **에이전트**: COD
- **한 일**: **`GET /api/v1/transport/service-fee-parity-rules`** — NHIS #44 **러-1~4·편도50%·1일1회·별지 제22호** 4-rule machine-readable catalog · **`TransportServiceFeeParityCatalog`** 정본
- **내 화면/업무에 영향**: **이동서비스비 청구** — 화면 안내 문구 **동일** (FE static config 유지) · Swagger·Postman·인수 smoke에서 **BE/FE 문구 1:1** 검증 가능 (FAQ **Q703**)
- **상태**: BE 완료 · FE API wire **P2 후보**

<details>
<summary>자세히</summary>

- BE: `bd1e87e` (BNK-562 deepen)
- RBAC: **`HQ_ADMIN`·`BRANCH_ADMIN` only** · **`SOCIAL_WORKER`·`CAREGIVER` 403** (`e4f83af` — 360차에서 `social_worker` 제외)
- 응답: **`totalCount=4`** · **`oneWayRatio=0.5`** · **`rules[]`** (`DISTANCE_BANDS`·`ONE_WAY_RATIO`·`ONE_PER_DAY`·`SERVICE_LOG`)
- 테스트: **`TransportServiceFeeParityCatalogTest`** · **`MustApiEndpointRoutingTest`**

</details>

### ✅ live E2E — operation readiness skip reason dedupe (`c3c6272`)
- **에이전트**: COD
- **한 일**: **`liveConfig.js`** — bootstrap·auth blocker **중복 skip reason** 제거 · **`liveE2eHarness.test.js`** regression lock
- **내 화면/업무에 영향**: 없음 — 스테이징 live E2E harness만 (FAQ **Q702** carry)
- **상태**: FE 완료

<details>
<summary>자세히</summary>

- FE: `c3c6272`
- 대상: **`npm run test:live-e2e`** operation readiness gating

</details>

### ✅ G2b CMS payment-method-catalog — FE panel wire (`4875937`)
- **에이전트**: COD
- **한 일**: **`CmsPaymentMethodCatalogPanel`** — **`/billing/cms`** 등록 관리 상단에 **엔젤 5-method 수납 카탈로그** 표 · **`fetchCmsPaymentMethodCatalogApi`** · 수납 **3/5 구현** Alert·badge
- **내 화면/업무에 영향**: **CMS 자동이체** — 결제수단·수수료(효성CMS 안내)·ogada 화면 링크·**미구현 2종(가상계좌·다계좌 정산)** 한눈에 확인 (FAQ **Q701**)
- **상태**: FE 완료 · module **7-4 △0.65 carry** (2-method 수납 backend 미구현)

<details>
<summary>자세히</summary>

- FE: `4875937` (BNK-596)
- 화면: **`/billing/cms`** — **`CmsPaymentMethodCatalogPanel`** L314
- 테스트: **`CmsPaymentMethodCatalogPanel.test`** · **`CmsPage.test`**

</details>

### ✅ G2b CMS payment-method-catalog — BE API (`2eaf17e`)
- **에이전트**: COD
- **한 일**: **`GET /api/v1/billing/cms/payment-method-catalog`** — silverangel extraService **5-method** crosswalk · **`collectionImplemented` 3/5** (자동이체·카드·현금영수증)
- **내 화면/업무에 영향**: **CMS·간편결제·현금영수증** 화면 매핑 참조 · Swagger·Postman catalog 확인 (FAQ **Q701**)
- **상태**: BE 완료 · FE wire **`4875937`**

<details>
<summary>자세히</summary>

- BE: `2eaf17e` (BNK-595)
- RBAC: **`HQ_ADMIN`·`BRANCH_ADMIN`** · **`guardian` 거부**
- 테스트: **`CmsPaymentMethodCatalogServiceTest`** · **`MustApiEndpointRoutingTest`**

</details>

### ✅ live E2E — bootstrap env toggle + blocker gating (`670756a`·`64a7648`)
- **에이전트**: COD
- **한 일**: BE **`OGADA_LIVE_E2E_BOOTSTRAP_ENABLED`** namespaced toggle 수용 · FE **auth 준비 후 bootstrap blocker 필터** (QA-B95 false skip 완화)
- **내 화면/업무에 영향**: 없음 — 스테이징 live E2E·health 진단만 (FAQ **Q702** · DEPLOYMENT §11-3)
- **상태**: BE+FE 완료

<details>
<summary>자세히</summary>

- BE: `670756a` · FE: `64a7648`
- env: **`OGADA_LIVE_E2E_BOOTSTRAP_ENABLED`** (기존 toggle path 병행)

</details>

### ✅ M7 본인부담 7-x lifecycle crosswalk 재입증 (BNK-592)
- **에이전트**: TWR (문서) · BNK-592 (실측)
- **한 일**: 케어포 func.php **7-1~7-10** 10-leaf ↔ ogada **`/billing/*` Route 1:1** 교차표 정본화 — **9✅ + 1△(7-4 CMS 0.65)** · ogada **superset 5**(현금영수증·본인부담률·수가표·공단 import·통계)
- **내 화면/업무에 영향**: **청구·입금·미납·CMS·간편결제·대장·계산기** — 기존 화면·경로 동일 · **인수·교육용 빠른 참조표** 추가 (FAQ **Q700** · USER_MANUAL **§5-10-0**)
- **상태**: 문서 완료 · 기능 변화 없음

<details>
<summary>자세히</summary>

- 실측: FE `@216ab7a` · BE `@a12873c` · merge gate **771**
- 스냅샷: `docs/planning/research/snapshots/carefor_m7_copay_lifecycle_crosswalk_bnk592.txt`
- 잔여 △: **7-4 CMS** — 지점 roster FE wire 시 coverage **0.65→1** 후보 (P2)

</details>

### ✅ G-SMS-TEMPLATE-CATALOG — guardian dispatch `ezcareMessageKind` test lock (`a12873c`)
- **에이전트**: COD
- **한 일**: **`MustApiEndpointRoutingTest`** — **`client-monthly-schedule`(12)·`elder-abuse-prevention-guideline`(19)** routing에 **`ezcareMessageKind`** assert 추가 — catalog **6/6** 회귀 커버리지 완성
- **내 화면/업무에 영향**: 없음 — API·UI 동작 동일 · 테스트 lock만
- **상태**: BE 완료

<details>
<summary>자세히</summary>

- BE: `a12873c`
- 대상: **`POST …/clients/{id}/notifications/client-monthly-schedule`** · **`POST …/notifications/elder-abuse-prevention-guideline`**

</details>

### ✅ G-SMS-TEMPLATE-CATALOG — billing dispatch Alert label test lock (`216ab7a`)
- **에이전트**: COD
- **한 일**: **`BillingDetailPage`·`OverduePage`·pilot overdue E2E** mock에 **`templateCode`** 반영 — **`formatGsmDispatchSuccessMessage`** BE contract 정합
- **내 화면/업무에 영향**: 없음 — 성공 Alert 문구 규칙(Q699) 유지 · 테스트 lock만
- **상태**: FE 완료

<details>
<summary>자세히</summary>

- FE: `216ab7a`
- 테스트: **`BillingDetailPage.test`** · **`OverduePage.test`** · **`pilotPageFlows.test`**

</details>

### ✅ G-SMS-TEMPLATE-CATALOG — 발송 성공 Alert 템플릿 라벨 (`c7d0982`)
- **에이전트**: COD
- **한 일**: **`formatGsmDispatchSuccessMessage`** — API **`templateCode`** 로 ezCare 한글명을 조회해 성공 Alert 끝에 **`(본인부담 안내)`** 등 괄호 표기 · **`ezcareMessageKind` 숫자는 화면 미표시** (Q692 유지)
- **내 화면/업무에 영향**: **이용자·직원·청구·미납·급여제공기록지** — 발송 성공 초록 Alert 문구에 **어떤 템플릿으로 보냈는지** 한글 라벨 확인 가능
- **상태**: FE 완료

<details>
<summary>자세히</summary>

- FE: `c7d0982`
- 대상: **`GuardianDocumentNotifyPanel`** · **`StaffNotificationDispatchPanel`** · **`ProvisionResultDispatchPanel`** · **`BillingDetailPage`** · **`OverduePage`** (`interpretBillingNotifyResult`)
- 예: **「급여제공기록지를 발송했습니다. (급여제공내역)」**
- 테스트: **`notificationChannelStatus.test.js`** · 각 dispatch panel test

</details>

### ✅ G-SMS-TEMPLATE-CATALOG — 직원 발송 API `ezcareMessageKind` (`2f83563`)
- **에이전트**: COD
- **한 일**: **`StaffAccessKeyNotifyResponse`**·**`StaffMonthlyScheduleNotifyResponse`** 성공 응답에 **`ezcareMessageKind`** 추가 — catalog **6/6 crosswalk parity** (청구·보호자와 동일)
- **내 화면/업무에 영향**: **직원 접속키·일정표 발송** — Swagger·Postman에서 **`message_kind=1`·`21`** 확인 (UI 숫자 표시 없음)
- **상태**: BE 완료

<details>
<summary>자세히</summary>

- BE: `2f83563`
- API: **`POST …/staff/notifications/staff-access-key`** → **`ezcareMessageKind=1`** · **`POST …/staff/notifications/staff-monthly-schedule`** → **21**
- 테스트: **`StaffAccessKeyNotificationServiceTest`** · **`MustApiEndpointRoutingTest`**

</details>

### ✅ UXD-161 — G-SMS 발송 패널 form-stack 간격 (`4adeb1c`)
- **에이전트**: UXD / COD
- **한 일**: **`components.css`** — **`.ds-form-stack`** flex column(`gap var(--space-4)`) 승격 · **`StaffNotificationDispatchPanel`**·**`GuardianDocumentNotifyPanel`** 섹션 제목·필드 수직 간격 복원
- **내 화면/업무에 영향**: **이용자 상세·직원 상세** — 알림톡·SMS 발송 카드 **필드 간격·가독성** 개선 (기능 동일)
- **상태**: FE 완료

<details>
<summary>자세히</summary>

- FE: `4adeb1c`/`c06d581` (UXD-161)
- ARIA·validation·live-region은 기존 §83 표준 유지 — JSX 변경 없음
- 테스트: **`StaffNotificationDispatchPanel.test`** · **`GuardianDocumentNotifyPanel.test`**

</details>

### ✅ G-SMS-TEMPLATE-CATALOG — readiness fallback 라벨 ezCare parity (`3f686e3`)
- **에이전트**: COD
- **한 일**: **`notificationChannelStatus.js`** — **`NOTIFICATION_TEMPLATE_LABELS`**·**`EZCARE_MESSAGE_KIND_BY_TEMPLATE`** BE catalog와 동기 — **본인부담 안내·급여제공내역·직원인권보호** 등 ezCare **`mobile-sendW`** 명칭 정합
- **내 화면/업무에 영향**: **조직 설정·대시보드** readiness 패널·발송 UI **한글 라벨**이 ezCare와 일치
- **상태**: FE 완료

<details>
<summary>자세히</summary>

- FE: `3f686e3`
- vitest: **`notificationChannelStatus.test.js`** — 6종 message_kind·라벨 lock
- 관련: Q697 · USER_MANUAL §5-5 · FAQ Q686

</details>

### ✅ live E2E — health G21 seed fallback contract lock (`88a58d9`)
- **에이전트**: COD
- **한 일**: **`HealthControllerTest`** — bootstrap service-unavailable 시 **`liveE2eG21SeedStatusDetail=g21-seed=disabled`** assert 추가 — QA-B95 probe drift 방지
- **내 화면/업무에 영향**: 없음 — 스테이징 live E2E·health 진단 테스트만 강화
- **상태**: BE 완료

<details>
<summary>자세히</summary>

- BE: `88a58d9`
- 필드: **`GET /api/v1/health`** **`liveE2eG21SeedStatusDetail`** (기존 Q515·DEPLOYMENT §11-3)

</details>

### ✅ G-SMS-TEMPLATE-CATALOG — 발송 API `ezcareMessageKind` 응답 (`ef8bb4e`)
- **에이전트**: COD
- **한 일**: 청구·보호자 서류 **수동 발송 API** 응답에 **`templateCode`·`ezcareMessageKind`** 추가 — ezCare **`mobile-sendW`** crosswalk(11·12·13·19)와 catalog 정합
- **내 화면/업무에 영향**: **청구 상세·이용자 상세** — Swagger·Postman에서 발송 결과 **message_kind** 확인 가능 (UI 표시 변화 없음)
- **상태**: BE 완료

<details>
<summary>자세히</summary>

- BE: `ef8bb4e` (BNK-584)
- 대상: **`POST …/billing/claims/{id}/notify`** · **`POST …/clients/{id}/notifications/*`** (care-provision·elder-abuse 등)
- 예: **`BILLING_STATEMENT` → `ezcareMessageKind=11`** · **`CARE_PROVISION_RECORD` → 13** · **`ELDER_ABUSE_PREVENTION_GUIDELINE` → 19**

</details>

### ✅ G-SMS-TEMPLATE-CATALOG — `dispatchReady` 채널 자격 검증 (`fed6f1f`)
- **에이전트**: COD
- **한 일**: **`GET /notifications/template-catalog`** — **`dispatchReady`** 가 Solapi **채널 자격**(SMS: key·secret·sender · ALIMTALK: + **`kakaoPfId`**)까지 충족해야 **true**
- **내 화면/업무에 영향**: **조직 설정·대시보드** — templateId만 설정·PF ID 미설정 시 **「발송 대기」** 로 표시 (false positive 방지)
- **상태**: BE 완료

<details>
<summary>자세히</summary>

- BE: `fed6f1f` (BNK-584)
- SMS **`dispatchReady`**: `NOTIFICATION_PROVIDER=solapi` + apiKey + apiSecret + senderId + template configured
- ALIMTALK **`dispatchReady`**: SMS 자격 + **`SOLAPI_KAKAO_PF_ID`** + template configured
- 테스트: **`NotificationSmsTemplateCatalogServiceTest`** SMS vs Alimtalk readiness regression

</details>

### ✅ G-SMS-TEMPLATE-CATALOG — message_kind 11·13·19 발송 UI 라벨 (`5a6d42c`)
- **에이전트**: COD
- **한 일**: **`GuardianDocumentNotifyPanel`** — **급여제공내역·직원인권보호** 알림톡 버튼·설명에 **ezCare message_kind** 표기 · **`BillingDetailPage`** **「본인부담 안내 알림톡 발송」** (message_kind=11)
- **내 화면/업무에 영향**: **이용자 상세·청구 상세** — 발송 버튼·도움말 문구가 ezCare parity와 일치
- **상태**: FE 완료

<details>
<summary>자세히</summary>

- FE: `5a6d42c` (BNK-584)
- 화면: **`/clients/:id`** · **`/billing/claims/:id`**
- module 10 KPI: **0.75**

</details>

### ✅ G-SMS-TEMPLATE-CATALOG — message_kind 1·12·21 발송 UI wire (`9c25d44`)
- **에이전트**: COD
- **한 일**: **`StaffNotificationDispatchPanel`**(직원 상세) — **일정표-직원**·**접속키 발송** · **`GuardianDocumentNotifyPanel`** — **일정표-수급자** 추가 · **`notifyClientMonthlyScheduleApi`·`notifyStaffMonthlyScheduleApi`·`notifyStaffAccessKeyApi`**
- **내 화면/업무에 영향**: **이용자 상세·직원 상세** — Swagger 없이 **월간 일정표·접속키 SMS** 발송 가능
- **상태**: FE 완료 · catalog **6/6 dispatchImplemented** (BE `1d5d441` 연동)

<details>
<summary>자세히</summary>

- FE: `9c25d44` (BNK-583)
- 화면: **`/clients/:id`** 기본정보 **「보호자 서류 발송」** — 문서 유형 **일정표-수급자** · **`/staff/:id`** 기본정보 **「알림톡·SMS 발송」**
- 권한: 이용자 — **`branch_admin`·`social_worker`** · 직원 — **`hq_admin`·`branch_admin`·`social_worker`**
- 테스트: **`StaffNotificationDispatchPanel.test`** · **`GuardianDocumentNotifyPanel.test`** · module 10 KPI **0.7**

</details>

### ✅ G-SMS-TEMPLATE-CATALOG — 직원 접속키 SMS 발송 API (`1d5d441`)
- **에이전트**: COD
- **한 일**: **`POST /api/v1/staff/notifications/staff-access-key`** — ezCare **`message_kind=1`** (`STAFF_ACCESS_KEY`) · 6자리 일회용 키·`password_reset_tokens` 저장 · catalog **`dispatchImplemented` 5/6→6/6**
- **내 화면/업무에 영향**: **직원 상세** — **접속키 SMS** API·UI (`9c25d44`) · **조직 설정·대시보드** readiness **「접속키 발송」발송 구현 ✅**
- **상태**: BE 완료 · FE wire **`9c25d44`**

<details>
<summary>자세히</summary>

- BE: `1d5d441` (BNK-583)
- RBAC: **`HQ_ADMIN`·`BRANCH_ADMIN`·`SOCIAL_WORKER`**
- 요청: `{ "staffUserId": "uuid" }`
- guard: **휴대전화 미등록** · **퇴사·비활성** · **비직원 역할** → **`422`**
- 접속키: **6자리 숫자** · TTL **`ogada.security.password-reset-ttl-minutes`**(기본 60분) · **화면에 키 미표시**

</details>

### ✅ G-SMS-TEMPLATE-CATALOG — 직원 월간 일정표 알림톡 발송 API (`b9d0599`)
- **에이전트**: COD
- **한 일**: **`POST /api/v1/staff/notifications/staff-monthly-schedule`** — ezCare **`message_kind=21`** (`STAFF_MONTHLY_SCHEDULE`) · 해당 월 **직원 배정 확정 PLAN 방문** guard · catalog **`dispatchImplemented` 4/6→5/6**
- **내 화면/업무에 영향**: **직원 상세·방문요양** — **화면 UI 없음**(Swagger·API) · **조직 설정·대시보드** readiness 패널에서 **「일정표-직원」발송 구현 ✅** 확인
- **상태**: BE 완료 · FE **직원 일정표 발송 버튼 △ P2**

<details>
<summary>자세히</summary>

- BE: `b9d0599` (BNK-581)
- RBAC: **`HQ_ADMIN`·`BRANCH_ADMIN`·`SOCIAL_WORKER`**
- 요청: `{ "staffUserId": "uuid", "yearMonth": "2026-06", "summary": "선택" }`
- guard: 해당 월 **직원 배정 확정(`CONFIRMED`) PLAN 방문 0건** → **`422`「해당 월에 확정된 방문일정 배정이 없어…」**
- FE wire: **없음** — Swagger·Postman (FAQ Q689)

</details>

### ✅ G-SMS-TEMPLATE-CATALOG — readiness 패널 발송 대기 표시 (`c04968c`)
- **에이전트**: COD
- **한 일**: **`NotificationChannelReadinessPanel`** — **`dispatchImplemented && !dispatchReady`** 항목을 **「발송 대기 N종」** Alert·목록으로 표시 · 요약 Alert에 **발송 대기 건수** 병기
- **내 화면/업무에 영향**: **조직 설정·대시보드** — Solapi templateId 미설정 등 **구현은 됐으나 아직 발송 불가**한 템플릿을 한눈에 확인
- **상태**: 완료

<details>
<summary>자세히</summary>

- FE: `c04968c` (BNK-582)
- **`pendingReadyEntries`** — 구현됨·설정 미완료 항목 필터
- dl **「발송 대기」** · warning Alert **「발송 대기 템플릿: …」**
- 테스트: **`NotificationChannelReadinessPanel.test`** pending catalog case

</details>

### ✅ G-SMS-TEMPLATE-CATALOG — 수급자 월간 일정표 알림톡 발송 API (`8631d1e`)
- **에이전트**: COD
- **한 일**: **`POST /api/v1/clients/{clientId}/notifications/client-monthly-schedule`** — ezCare **`message_kind=12`** (`CLIENT_MONTHLY_SCHEDULE`) · 해당 월 **확정 PLAN 방문일정** guard · catalog **`dispatchImplemented` 3/6→4/6**
- **내 화면/업무에 영향**: **이용자 상세 보호자 알림** — **화면 UI 없음**(Swagger·API) · **조직 설정·대시보드** readiness 패널에서 **「일정표-수급자」발송 구현 ✅** 확인
- **상태**: BE 완료 · FE **`GuardianDocumentNotifyPanel` wire △ P2**

<details>
<summary>자세히</summary>

- BE: `8631d1e` (BNK-580)
- RBAC: **`BRANCH_ADMIN`·`SOCIAL_WORKER`**
- guard: 해당 월 **확정(`CONFIRMED`) PLAN 방문 0건** → **`422`「해당 월에 확정된 방문일정이 없어…」**
- FE wire: **없음** — `POST …/client-monthly-schedule` 는 Swagger·Postman (FAQ Q687)

</details>

### ✅ G-SMS-TEMPLATE-CATALOG — catalog `dispatchReadyCount` 집계 (`fb323ae`)
- **에이전트**: COD
- **한 일**: **`GET /api/v1/notifications/template-catalog`** — **`dispatchReadyCount`**·항목별 **`dispatchReady`** 명시 · **configured-only vs 실발송 가능** 구분
- **내 화면/업무에 영향**: **조직 설정·대시보드** — readiness 패널 **「발송 구현 N종 중 M종 발송 가능」** Alert (FE `15f2195`)
- **상태**: 완료

<details>
<summary>자세히</summary>

- BE: `fb323ae` (BNK-579)
- `dispatchReady` = **`dispatchImplemented && configured`** (Q679 fail-closed 동일)

</details>

### ✅ UXD-160 — 템플릿 카탈로그·FAQ21823 보관 a11y (`15f2195`·`068049b`)
- **에이전트**: UXD / COD
- **한 일**: **`NotificationChannelReadinessPanel`** catalog **`role="status"` Alert**·표 **`caption`** · FAQ21823 **보관 D-day Alert**·목록 패널 **`aria-*`** · **「재계약 완료 기록」** 버튼 accessible name = **표시 텍스트** (`068049b`, QA-B289)
- **내 화면/업무에 영향**: **조직 설정·대시보드·직원 lifecycle** — 스크린리더·키보드 조작 개선 (기능 동일)
- **상태**: 완료

<details>
<summary>자세히</summary>

- FE: `15f2195` (UXD-160) · `068049b` (QA-B289)
- module 10 KPI: **0.65** (`ef3948c`)

</details>

### ✅ G-SMS-TEMPLATE-CATALOG — ezCare 템플릿 카탈로그 FE wire (`c9cf03b`)
- **에이전트**: COD
- **한 일**: **`NotificationChannelReadinessPanel`** — **`GET /notifications/template-catalog`** 병렬 조회 · **「이지케어 메시지 종류 (템플릿 카탈로그)」** 섹션 — 6종 **`dispatchReady`** 표 · **`fetchNotificationTemplateCatalogApi`**
- **내 화면/업무에 영향**: **조직 설정·대시보드** — **`hq_admin`·`branch_admin`** 이 화면에서 **ezCare message_kind ↔ Solapi 매핑·발송 가능** 상태 확인 (Swagger 불필요)
- **상태**: 완료 (BE `b6c9b16` + FE `c9cf03b` full-stack)

<details>
<summary>자세히</summary>

- FE: `c9cf03b` (BNK-576, Q686 deepen)
- 화면: **`/organization/settings`** · **`/dashboard`·`/dashboard/hq`** 하단 **`NotificationChannelReadinessPanel`**
- 표 열: 메시지 · 종류 · 채널 · 발송 구현 · Solapi 설정 · 발송 가능
- 테스트: **`NotificationChannelReadinessPanel.test`** · **`settingsServices.test`** (`fetchNotificationTemplateCatalogApi`)

</details>

### ✅ G-SMS-TEMPLATE-CATALOG — Solapi 템플릿 카탈로그 API (`b6c9b16`)
- **에이전트**: COD
- **한 일**: **`GET /api/v1/notifications/template-catalog`** — ezCare `message_kind` ↔ ogada Solapi 템플릿 **6종 parity catalog** · `configured`·`dispatchImplemented`·`dispatchReady` 집계
- **내 화면/업무에 영향**: **조직 설정·대시보드** — readiness 패널에서 **6종 카탈로그** 표시 (FE `c9cf03b`)
- **상태**: 완료

<details>
<summary>자세히</summary>

- BE: `b6c9b16` (BNK-575)
- 6종: `STAFF_ACCESS_KEY`(SMS) · `BILLING_STATEMENT`·`CLIENT_MONTHLY_SCHEDULE`·`CARE_PROVISION_RECORD`·`ELDER_ABUSE_PREVENTION_GUIDELINE`·`STAFF_MONTHLY_SCHEDULE`(ALIMTALK)
- `dispatchReadyCount` — **실제 발송 가능** 항목만 (Q679 fail-closed와 연동)
- FE wire: **`c9cf03b`** — `NotificationChannelReadinessPanel` (Q686)

</details>

### ✅ FAQ21823 — BE 규정 준수 API 신규 추가 (`9aaefa0`)
- **에이전트**: COD
- **한 일**: **`GET /api/v1/staff/employment-contracts/compliance`** — 관리자용 직원 근로계약 규정 준수 집계 API · **`renewalGapCount`** (재계약 기한 초과), **`retentionExpiringCount`** (보관 임박 90일), **`retentionExpiredCount`** (보관 만료), **`renewalAlerts[]`** (미충족 직원 상세)
- **Dashboard 통합**: **`GET /api/v1/dashboard/{branch|hq}`** 응답에 **`employmentContractRetentionExpiringCount`**, **`employmentContractRetentionExpiredCount`** 필드 추가 (snapshot aggregation)
- **내 화면/업무에 영향**: **대시보드** — 근로재계약 미충족 + 보관 기한 임박/만료 **공식 집계** (기존 FE 계산에서 API 기반 전환)
- **상태**: 완료

<details>
<summary>자세히</summary>

- BE: `9aaefa0` (Q685 deepen)
- API 경로: **`/api/v1/staff/employment-contracts/compliance?branchId=&referenceDate=`**
- 권한: **`HQ_ADMIN`, `BRANCH_ADMIN`, `SOCIAL_WORKER`**
- FE: `EmploymentContractRenewalAlertsPanel` 에서 compliance API 호출 (기존 `fetchUsersApi` fallback 제거)
- P2 잔여: 보관 기간별 자동 폐기 workflow

</details>

### ✅ FAQ21823 — 3년 보관 D-day 알림·근로계약서 서식 인쇄
- **에이전트**: COD
- **한 일**: **`StaffEmploymentContractRenewalPanel`** — 보관 기한 **90일 이내 warning Alert**·**만료 후 info Alert** · **「근로계약서 서식 보기」Modal → 「서식 인쇄」**(`window.print`·`@media print` CSS)
- **내 화면/업무에 영향**: **직원 상세 → 입사~퇴사** — 근로계약 **3년 보관 기한** 임박·만료 안내 · **필기용 서식 인쇄** 가능 (기능 동일·안내 강화)
- **상태**: 완료

<details>
<summary>자세히</summary>

- FE: `a43bcb7` (Q685)
- 상수: **`EMPLOYMENT_CONTRACT_RETENTION_WARNING_DAYS=90`** · **`EMPLOYMENT_CONTRACT_RENEWAL_TEMPLATE`**
- P2 잔여: BE PDF 자동 생성·전자서명 workflow
</details>

### ✅ live E2E — health·probe `liveE2eOperationReason` 정본 필드
- **에이전트**: COD
- **한 일**: **`GET /api/v1/health`**·**`/live-e2e/probe`** 에 **`liveE2eOperationReason`** 노출 — blocker와 **1:1 대응** (`bootstrap-disabled`·`bootstrap-service-unavailable`·`staff-bootstrap-not-ready`·`none` 등)
- **내 화면/업무에 영향**: 없음 — 스테이징 live E2E·health 진단만 개선
- **상태**: 완료

<details>
<summary>자세히</summary>

- BE: `d11263b` (Q684 deepen)
- FE live E2E harness는 health **`liveE2eOperationReason`** 파싱 유지 (Q684 carry)
</details>

### ✅ live E2E bootstrap — disabled vs service-unavailable 진단 분리
- **에이전트**: COD
- **한 일**: bootstrap **enabled** 이지만 service bean **미주입** 시 **`bootstrap=service-unavailable`**·**`bootstrap-service-unavailable` blocker**·**`liveE2eBootstrapEnableHint`** 별도 문구 노출 — disabled와 혼동 방지
- **내 화면/업무에 영향**: 없음 — 스테이징 live E2E·health 진단만 개선
- **상태**: 완료

<details>
<summary>자세히</summary>

- BE: `0494334` (Q684)
- hint (enabled·bean missing): `LIVE_E2E_BOOTSTRAP_ENABLED=true is set but bootstrap service is unavailable.`
- FE: `cba9ff8` — **`liveE2eOperationReason`** health 파싱·skip 진단 보존 (QA-B95)
</details>

### ✅ live E2E bootstrap — health·probe enable hint
- **에이전트**: COD
- **한 일**: bootstrap **disabled** 시 **`GET /api/v1/health`**·**`/live-e2e/probe`** 에 **`liveE2eBootstrapEnableHint`** 노출 — env 조치 문구를 로그 없이 확인
- **내 화면/업무에 영향**: 없음 — 스테이징 live E2E 장애 진단만 개선
- **상태**: 완료

<details>
<summary>자세히</summary>

- BE: `c8358e9` (Q680)
- hint: `Set LIVE_E2E_BOOTSTRAP_ENABLED=true to enable live E2E bootstrap.`
</details>

### ✅ FAQ21823 근로재계약 — 대시보드 pilot harness
- **에이전트**: COD
- **한 일**: **`pilotChecklist` R03-c** (`fetchUsersApi`) · **`pilotPageFlows`** dashboard **「근로재계약 미충족」**·**`EmploymentContractRenewalAlertsPanel`** assertion
- **내 화면/업무에 영향**: 없음 — QA·인수 테스트 자동화
- **상태**: 완료

<details>
<summary>자세히</summary>

- FE: `28033cf` (Q682)
</details>

### ✅ G16·이용자 수정 — 접근성(UXD-159)
- **에이전트**: UXD
- **한 일**: **`TransportServiceFeePanel`** busy·row action labels·표 caption · **`ClientDetailPage`** 수정 링크 **`aria-label`** 복원
- **내 화면/업무에 영향**: **이동 → 이동서비스비 청구**·**이용자 상세 → 수정** — 스크린리더·키보드 조작 개선 (기능 동일)
- **상태**: 완료

<details>
<summary>자세히</summary>

- FE: `0869589` (Q683)
</details>

### ✅ live E2E bootstrap — 기본 비활성(opt-in) 유지
- **에이전트**: COD
- **한 일**: `application.yml`에 **기본 비활성** 주석을 명시 — **`LIVE_E2E_BOOTSTRAP_ENABLED`/`LIVE_E2E` env로만** bootstrap 허용
- **내 화면/업무에 영향**: 없음 — 운영·스테이징 live E2E 실행 절차만 명확해짐
- **상태**: 완료

<details>
<summary>자세히</summary>

- BE: `8b3fdcd` (QA-B277)
- 운영: `./scripts/run-live-e2e.sh` 또는 env 명시적 설정 필요 (FAQ Q680)
</details>

### ✅ Solapi 알림톡 — templateId 미매핑 시 발송 거부
- **에이전트**: COD
- **한 일**: `NOTIFICATION_PROVIDER=solapi`에서 **내부 템플릿 코드 → Solapi templateId** 매핑이 없거나 placeholder면 **발송 실패**로 처리 (무음 발송 방지)
- **내 화면/업무에 영향**: live 알림톡 전환 시 **승인 templateId env 매핑** 필수 — 미매핑이면 `notifications`가 실패 상태로 남음
- **상태**: 완료

<details>
<summary>자세히</summary>

- BE: `SolapiMessageClient` (`f600fd6`)
- readiness Q644와 별도로 **런타임 dispatch** 단계에서도 fail-closed (FAQ Q679)
</details>

### ✅ 연차·유급휴일 대장 — live E2E·pilot harness
- **에이전트**: COD
- **한 일**: **`staffLeaveLedgerLiveApi.e2e.test.js`** · **`pilotPageFlows`** CRUD flow · **`relatedSurfaces` AVAILABLE** assertion 추가
- **내 화면/업무에 영향**: 없음 — QA·인수 테스트 자동화 보강
- **상태**: 완료

<details>
<summary>자세히</summary>

- FE: `bc6180e` (US-R01-c)
</details>

### ✅ 이동서비스비 — pilot checklist·NHIS #44 노트 검증
- **에이전트**: COD
- **한 일**: G16 **`pilotChecklist`** API 항목 · **`/transport/service-fees`** Must route · **NHIS #44 parity copy** 테스트 assertion
- **내 화면/업무에 영향**: 없음 — QA 자동화
- **상태**: 완료

<details>
<summary>자세히</summary>

- FE: `87da06d` (v1.3-C/G16)
</details>

---

## 2026-06-23

### ✅ 상세주소만 바꿔도 저장됨
- **에이전트**: COD
- **한 일**: 이용자 수정 시 **도로명은 그대로** 두고 **상세주소(`addressDetail`)만** 보내도 반영되도록 수정
- **내 화면/업무에 영향**: 수정 화면에서 **상세주소만** 고치고 저장하면 **무시되지 않음**
- **상태**: 완료

<details>
<summary>자세히</summary>

- BE: `ClientService.applyAddressDetailOnlyUpdate` (`2cae74c`)
- FE: 기존 `KoreanAddressFields` prefill과 연동 — 도로명 재전송 불필요
</details>

### ✅ 이동서비스비 — NHIS #44 산정 기준 안내
- **에이전트**: COD
- **한 일**: 이동서비스비 청구 화면에 **러-1~4·편도 50%·1일 1회·별지 제22호 일지** 안내를 **고정 표시**
- **내 화면/업무에 영향**: **이동 → 이동서비스비 청구**에서 수가표 아래 **「NHIS #44 산정 기준」** 목록 확인
- **상태**: 완료

<details>
<summary>자세히</summary>

- FE: `TransportServiceFeePanel` · `transportServiceFee.js` (`a531ed6`)
- BE: `TransportServiceFeeService` 문구와 동일 패리티
</details>

### ✅ 요양보호사도 이용자 정보 수정 가능
- **에이전트**: COD
- **한 일**: 요양보호사(`caregiver`)가 기존 이용자 **수정** 가능 — **신규 등록**은 사회복지사 이상만
- **내 화면/업무에 영향**: 요양보호사 계정 → 이용자 상세 → **수정** → 저장 가능. **신규 등록** 버튼·`/clients/new` 는 **표시되지 않음**
- **상태**: 완료

<details>
<summary>자세히</summary>

- BE: `RoleHierarchy` · `PATCH /clients` — `HQ_ADMIN`·`CAREGIVER` 포함 (`01edba7`)
- FE: `clientPermissions.js` · `roleNav.js` route guard (`77584a0`/`2e7374b`)
</details>

### ✅ 이용자 주소 — 도로명·상세 분리 조회
- **에이전트**: COD
- **한 일**: 이용자 조회 API·수정 화면에서 **도로명(`addressSearch`)** 과 **상세주소(`addressDetail`)** 를 분리해 표시
- **내 화면/업무에 영향**: **수정** 화면 진입 시 기존 주소가 **검색 결과·상세** 입력란에 맞게 채워짐
- **상태**: 완료

<details>
<summary>자세히</summary>

- BE: `ClientResponse.addressSearch`·`addressDetail` (`deda5b4`)
- FE: `ClientFormPage` prefill (`1193761` carry)
</details>

### ✅ 수급자 정보 수정
- **에이전트**: COD
- **한 일**: 수급자 상세에서 「수정」으로 들어가 이름·주소·연락처·장기요양·배차 정보를 고칠 수 있게 함
- **내 화면/업무에 영향**: 목록에서 이름 클릭 → 상세 → **수정** → 저장. 본사·지점장·사회복지사·요양보호사 등 현장 직원 계정에서 가능
- **상태**: 완료

<details>
<summary>자세히</summary>

- FE: `ClientDetailPage`, `ClientFormPage`
- 경로: `/clients/:id/edit`
</details>

### ✅ 주소 입력 — 카카오 우편번호 검색
- **에이전트**: COD · DBA
- **한 일**: 수급자·지점 등록/수정 시 「주소 검색」→ 기본주소 + 상세주소 입력 방식으로 통일
- **내 화면/업무에 영향**: 신규 등록·수정 화면에서 주소를 다른 사이트처럼 검색해서 넣을 수 있음
- **상태**: 완료

<details>
<summary>자세히</summary>

- FE: `KoreanAddressFields`, `kakaoPostcode.js`
- BE: `addressSearch` + `addressDetail` 분리 저장
</details>

### ✅ 거주지 주소 전체 표시
- **에이전트**: COD
- **한 일**: 수급자 목록·상세에서 거주지 주소를 `***` 마스킹 없이 전체 표시 (픽업 주소만 마스킹 유지)
- **내 화면/업무에 영향**: 수급자 목록·상세에서 **거주지 주소를 끝까지** 볼 수 있음
- **상태**: 완료

### ✅ 배차 — 거주지 주소와 동일
- **에이전트**: COD
- **한 일**: 배차 이용 시 픽업 주소를 거주지와 같게 쓸 수 있는 「거주지 주소와 동일」 옵션 추가
- **내 화면/업무에 영향**: 수급자 등록·수정 시 배차 켜면 별도 픽업 주소 없이 거주지로 배차 가능
- **상태**: 완료

### ✅ 수급자 목록 필터
- **에이전트**: COD
- **한 일**: 목록에서 등급·성별·배차 이용·지점 열로 필터
- **내 화면/업무에 영향**: 수급자 많을 때 원하는 조건만 골라서 볼 수 있음
- **상태**: 완료

### ✅ 직원 연차·휴가가 화면 연결
- **에이전트**: COD
- **한 일**: 직원 출근·연차·휴가가 링크로 서로 이동 가능하게 정리, 지점명 표시 보강
- **내 화면/업무에 영향**: 직원 메뉴(출근·연차·휴가가) 사이를 클릭으로 오갈 수 있음
- **상태**: 완료

### 📝 변경 기록 양식 개편
- **에이전트**: TWR
- **한 일**: 이 파일을 사람이 읽기 쉬운 카드 형식으로 새로 작성 (과거 장문 기록 삭제)
- **내 화면/업무에 영향**: 없음 — 문서만 바뀜
- **상태**: 완료
