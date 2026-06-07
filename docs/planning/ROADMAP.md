<!-- doc:owner=PLN doc:audience=TSR,COD,SEC updated=2026-06-08T15:00:00+00:00 -->
# ogada 구현 로드맵

> **작성·유지**: `planner`  
> **구현**: `coder`는 `status: in_progress` 버전 **하나만** 작업  
> **검증**: `tester`는 `merge_status: merged` 이후 `test` 브랜치에서 검증  
> **피드백**: `tester` → `docs/qa/QA_FEEDBACK.md` → `planner` 반영 → `coder` 수정  
> **벤치마크 입력**: `docs/planning/research/BENCHMARK_REPORT.md`, `docs/planning/research/COMPETITOR_MATRIX.md`, `memory/decisions.md`

> **CURRENT BASELINE (43차 — ROADMAP/QA 과거 SHA보다 우선)**: backend develop **`3f9264f`** · frontend develop **`e043eac`** · `.agents/workspace_baseline.yaml` · run_agent build 실측 주입. **`d5654c0`/`e5fd48d` checkout 재현 금지**.

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

> **43차 동기화 (2026-06-08T15:00) — workspace baseline 확정 + SEC-D12/QA-B11/SEC-D11 Fixed**: ① **신규 baseline** — backend **`3f9264f`** · frontend **`7c0ecdc`** (`.agents/workspace_baseline.yaml` + run_agent 실측). ② **`d5654c0`/`e5fd48d` checkout 폐기** — TSR57 frontend 유실·재현 불가. ③ **SEC-D12·QA-B11·SEC-D11 Fixed** @ `7c0ecdc`/`3f9264f`. ④ **QA-B10 Fixed** @ `3f9264f` 유지. ⑤ **잔여 BLOCK**: **backend merge(3커밋) + FE-18·FE-19 + B03** — INFRA-B12 checkout 게이트 **소멸**.

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

### 핵심 진단 (planner, 63차 갱신 — baseline 43차 확정)

- **CURRENT BASELINE (43차)**: backend develop **`3f9264f`**(CLEAN, BE-10·J01·v2/J03) · frontend develop **`e043eac`**(CLEAN, JWT·ProtectedRoute·AppShell·vitest). **`.agents/workspace_baseline.yaml`** + run_agent build **실측 주입** — ROADMAP/QA 과거 SHA보다 **우선**.
- **폐기 SHA**: `d5654c0`(TSR57 frontend)·`e5fd48d`(스켈레톤)·`428ba7d`(TSR56) — **checkout 재현 금지**. v1.1 Recharts·FE-17·GuardianInvitationAccept 등은 **`e043eac` lineage 위에서 재구현**.
- **SEC-D12·QA-B11·SEC-D11 Fixed @ 43차**: frontend route 가드·baseline 단절·submodule drift — **`e043eac`/`3f9264f` 기준**.
- **QA-B10 Fixed @ `3f9264f`**: v1 E2E/routing/SEC-007 develop HEAD **PRESENT** — BE-10 **완료**.
- **backend merge gap**: develop **3커밋 ahead** of test (`f47ffa1`·`cf6116c`·`3f9264f`) — merge 게이트 **BLOCK**.
- **frontend merge gap**: develop **`e043eac`** vs test **`e5fd48d`** — B03 merge 게이트 **BLOCK**.
- **잔여 Planned BLOCK**: **backend merge(3커밋) + FE-18·FE-19 + B03** — INFRA-B12 checkout **`d5654c0` 폐기**.
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
| QA-20260606-B03 | BLOCK | v1.1 | v1.1 완료 기준 충족 후 `merge_status: ready` | develop→test merged |
| QA-20260606-B04 | BLOCK | v1.1 | ~~develop 커밋 규율~~ **Fixed `998ac87`** | `git -C src/frontend status` clean |
| QA-20260606-B05 | BLOCK | v1.1 | **선행 게이트** — v1 `merged` 후 v1.1 이관 착수 | v1 merge_status: merged |
| QA-20260606-H03 | HIGH | v1.1 | SEC-003(ProtectedRoute·역할 가드) develop 커밋 | develop HEAD `/platform`·`/settings` 가드 |
| QA-20260606-H04 | HIGH | v1.1 | ~~Must 화면 API 연동~~ **Fixed `998ac87`** | develop HEAD `src/api/`·페이지 연동 |
| QA-20260606-M01 | MEDIUM | v1.1 | ~~Vitest + RTL~~ **Fixed `998ac87`** | `npm test` 6/6 PASS |
| QA-20260606-B06 | BLOCK | v1 | ~~client↔guardian develop 커밋~~ **Fixed `4d476c6`** | develop HEAD + clean tree |
| QA-20260606-B07 | BLOCK | v1.1/v1.2 | ~~recurrence #5 Fixed `d5654c0`~~ **recurrence #6 Planned** — DateInput·GuardianInvitationList J01·ClientDetail·PaymentRecordModal·**20 files WT 미커밋**·WT `npm test` **209/210 FAIL**(QA-H05·FE-7)·HEAD `d5654c0` Fixed(FE-17) 규율 5 유효 | develop HEAD `d5654c0` + working tree clean + **npm test PASS**(FE-18·FE-19) |
| QA-20260607-B09 | BLOCK | v1.1 J01 | ~~Planned~~ **Fixed @ `f47ffa1`**(TSR 58차) — J01 `guardian_invitations` API·V43·`SecurityConfig`·SEC-D8 **HEAD PRESENT** | develop HEAD `f47ffa1` + clean tree ✓ |
| QA-20260608-B10 | BLOCK | v1 | ~~Planned~~ **Fixed @ `3f9264f`** — v1 E2E/routing/SEC-007 develop HEAD PRESENT | BE-10 ✓ |
| SEC-20260608-011 | BLOCK | v1/v1.1 | ~~Planned~~ **Fixed @ 43차** — baseline `3f9264f`/`7c0ecdc` 확정 · workspace_baseline.yaml | INFRA-B12 checkout **폐기** ✓ |
| SEC-20260608-012 | BLOCK | v1 | ~~Planned~~ **Fixed @ `e043eac`** — ProtectedRoute·AuthContext HEAD PRESENT | FE-20 ✓ |
| QA-20260608-B11 | BLOCK | v1.1 | ~~Planned~~ **Fixed @ 43차** — 신규 baseline `e043eac` (d5654c0 replay 폐기) | baseline 확정 ✓ |
| QA-20260607-H05 | HIGH | v1.1 FE-7 | **Planned** — `GuardianListCard.test.jsx` MaskedPhone 마스킹 vs 평문 기대·209/210 FAIL·B07 #6 commit 게이트·**SEC-D9 PII 마스킹 게이트 동반** | WT `npm test` 전량 PASS (FE-19+SEC-D9) |
| SEC-20260607-009 | BLOCK | v1.1 J01 | ~~Planned~~ **Fixed @ `f47ffa1`**(TSR 58차) — SEC-D8 accept 단일 permitAll·토큰 hash·rate limit | BE-8 ✓ |
| SEC-20260607-010 | MEDIUM | v1.1 FE-7 | **Planned** — SEC-D9 MaskedPhone PII `010-****-5678` 유지·테스트·`aria-label` 정합·마스킹 제거 금지 | FE-19 PASS 후 FE-18 커밋 |
| QA-20260607-B08 | BLOCK | v2 | ~~Fixed `feac558`~~ ~~recurrence #2 Planned~~ **recurrence #2 Fixed `428ba7d`** — V42 consent CHECK·temporal + `NotificationPreferenceServiceTest` 4 @Test develop HEAD PRESENT·working tree clean | V42 + test @HEAD ✓ |
| SEC-20260606-005 | HIGH | v1.1 | ~~JWT localStorage 제거~~ **Fixed `998ac87`** | `AuthContext.jsx` HEAD 메모리 세션 |
| SEC-20260606-007 | BLOCK | v1 | ~~develop→test 승격(B01 동반)~~ **Fixed** — test `@e8750d2` `ProductionSecretValidator`·Boot 3.5.3 **PRESENT**(TSR 34차) | B01 merged ✓ |
| SEC-20260606-008 | MEDIUM | v1.1 | ~~npm audit dev chain critical(esbuild·vite·vitest)~~ **Fixed `ed1bf22`(COD 17차, TSR 25차 독립 검증 — 18차 planner 반영)** — vite `^6.4.3`·vitest `^4.1.8`·`overrides.esbuild ^0.25.0` upgrade | `npm audit --audit-level=high` 0 vulnerabilities |

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
- **(QA-B10, 42차)** v1 `merge_status: merged` 유지하나 test `@2799e29` **stale** — develop `@f47ffa1`에 v1 E2E/routing 산출물 **ABSENT**. **BE-10** baseline 결정(#42) + test 재동기화 전 추가 operation sign-off **금지**

---

## v1.1 — 프론트엔드 MVP + 보호자 확장

- **status**: in_progress
- **merge_status**: pending
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

- [x] `npm run build` 성공
- [x] 7역할 화면·메뉴·권한 분리 *(develop HEAD `998ac87` — `ProtectedRoute`·`App.jsx` 7역할 가드; develop HEAD `57ff3c0`(COD 20차) — `sevenRoleJwtLogin.test.jsx`(132 lines AuthProvider login·LoginPage 폼 7역할 매트릭스)·`sevenRoleRouteGuard.test.jsx`(83 lines ProtectedRoute 허용·거부 매트릭스)·`sevenRoleRouteMatrix.js`(75 lines 라우트 접근 매트릭스 모듈)·`roleHomePaths.test.jsx`(+26)로 단위 E2E 자동화 정식 충족 — `npm test` 130/10 PASS)*
- [x] **(QA-H03)** ProtectedRoute·역할 가드(SEC-003) **develop 커밋** — HEAD에서 `/platform`·`/settings`·`/dashboard/hq` 무방비 차단
- [x] **(QA-H04)** Must 화면 **REST API(JWT) 연동** — 이용자·출석·건강·청구·NHIS reconciliation·보호자 명세; **localStorage 역할 데모 제거**, `fetch`로 `/api/v1/*` 호출 *(develop `998ac87` — `src/api/`·15+ 페이지 연동, 보호자 초대는 백엔드 API 미구현으로 스텁 유지)*
- [ ] Must 화면 API 연동 E2E 수동 시나리오 PASS (파일럿 P1–P8 프론트 재현) *(develop `3fdc266`(COD 22차) — `pilotPageFlows.test.jsx`(433 lines) P1–P8 Must 화면 RTL fetch-mock JWT API 호출·페이지 렌더 통합 E2E + `cc34f23`(COD 19차) `pilotChecklist.js/.test.js` fetch-mock + `57ff3c0`(COD 20차) 7역할 JWT·라우트 가드 매트릭스, `npm test` 32/7→**140/11 PASS**(+108 tests/+3 files vs 27차) = **PARTIAL 강화**; **라이ve 수동 시나리오·J01 백엔드 API는 v1 test 승격 후** — B01·B05 선행)*
- [x] `/billing/imports/nhis/{batchId}` reconciliation 행 매칭·수동 연결 UI *(develop `998ac87` — `ReconciliationPage` API 연동·수동 매칭 모달)*
- [ ] 보호자 **초대·명세 열람** E2E (US-J01·J02 — G8) *(J02 명세 탭 API 연동 완료; develop `d5654c0`(COD 35차) — J01 수락 UI **HEAD 반영** + `cc34f23` `GuardianInviteModal.test.jsx` 발송 UI 회귀 PARTIAL; **58차 — J01 백엔드 API Fixed @ `f47ffa1`**(BE-8·`GuardianInvitationController`·V43·API_SPEC §4-1)·**INFRA-B12 checkout 후 FE-18·FE-19**·live E2E)*
- [x] **(US-UX-01)** **파비콘·앱 아이콘** — `public/favicon.svg`·`favicon.ico`·`apple-touch-icon.png`, `index.html` `<link rel="icon">`·`theme-color` *(develop `998ac87`)*
- [x] **(QA-M01)** Vitest + React Testing Library `test` 스크립트 — ProtectedRoute·역할 라우팅·P1–P8 페이지 E2E 회귀 자동화 (`npm test` PASS) *(develop `d5654c0` — **199 tests/40 files PASS**, vitest 4.1.8)*
- [x] **(SEC-005)** JWT access/refresh **localStorage 영구 저장 제거 → 메모리 세션** — `AuthContext.jsx` HEAD에서 `localStorage.get/set/removeItem(STORAGE_KEY)` 부재 *(develop `998ac87`)*
- [x] **(QA-B04·B07 @HEAD)** `src/frontend` develop working tree clean — 미커밋 변경 없음 *(develop `d5654c0`(COD 35차) — B07 recurrence #5 25 files 일괄 커밋(FE-17 J01·LogoutButton·BillingPage.layout), `git -C src/frontend status` **CLEAN**, HEAD `npm test` **199/40 PASS**·build **756 modules**·audit 0건)*
- [x] **(SEC-008)** npm audit dev chain critical 해소 — vite/vitest/esbuild 메이저 업그레이드(devDep 전용, prod 번들 무관) *(develop `ed1bf22`(COD 17차) — vite `^6.4.3`·vitest `^4.1.8`·`overrides.esbuild ^0.25.0`, `npm audit --audit-level=high` 0건·all 0 vulnerabilities — TSR 25차 독립 검증)*

> **B07 recurrence(14·16·19·20차→21차 Fixed)**: 19~20차 dirty 42 files → 21차 `a72e249` 일괄 커밋으로 working tree clean. v1.1 HEAD Fixed **유효 유지**. v1.2 P0 산출물은 **결정 52**에 따라 v1.1 merge에 동반 흡수(별도 분리 안 함).
> **B07 recurrence #2(23차 Open→17차 Planned→25차 Fixed)**: 21차 clean → 23차 `5656e19`(UXD 10차) 위 v1.2 P0 US-M02 대시보드 위젯 실데이터 8 files WIP 미커밋(17차 planner Planned) → **COD 17차 `a84473f` 일괄 커밋(8 files +636/-170 — `dashboardWidgets.js`·`.test.js`·`DashboardPage`·`AttendancePage`·`ClientFormPage`·`GuardiansPage`·`GuardianListCard`·`services.js`)** → working tree CLEAN, HEAD `npm test` 13/5·build 111 modules PASS, **TSR 25차 정식 Fixed 확정**(이관 규율 5·6·7 PASS).
> **SEC-008(24차 Open→25차 Fixed)**: 24차 npm audit 5 vulnerabilities(4 moderate·1 critical, esbuild GHSA·vite·vitest dev chain 에스컬레이션) → **COD 17차 `ed1bf22`** vite `^6.4.3`·vitest `^4.1.8`·`overrides.esbuild ^0.25.0` 메이저 업그레이드 → develop `npm audit --audit-level=high` **0 vulnerabilities**, all 0건. dev 환경 전용 취약점 — prod 번들 영향 없음. **TSR 25차 정식 Fixed 확정**.
> **R-05 P1–P8 페이지 단위 E2E PARTIAL 강화(31차 — COD 22차 `3fdc266`)**: `pilotPageFlows.test.jsx`(433 lines — AttendancePage·DashboardPage·HealthPage·BillingPage·NHISImportPage·ReconciliationPage·ClientDetailPage·GuardianPage RTL fetch-mock JWT API 호출·페이지 렌더 통합 검증) develop HEAD 커밋. `npm test` 130/10→**140/11 PASS**(+10/+1), build 113 modules PASS, audit 0건. → **R-05 frontend P1–P8 페이지 단위 E2E PARTIAL 강화** — fetch-mock 라우팅(FE-9) + 7역할 매트릭스(FE-9) 위 **페이지 통합 회귀(FE-11)** 충족. 라이ve backend·J01 API 잔여. 결정 52에 따라 v1.1 develop→test merge에 동반 흡수.
> **UXD 14차 `a42d6fb` — 수가표 이력 UI(US-G00a PARTIAL)**: `FeeRateHistoryPanel.jsx`·`FeeSchedulePage` 이력 모달·`chartColors.js`·Recharts 토큰·`BATCH_STATUS` 공유 상수 8 files. v1.1 merge 동반 흡수(결정 52).
> **B07 recurrence #3(33차 Open→23차 Planned→31차 Fixed)**: 31차 CLEAN → … → **COD 31차 `4be0938` 82 files 일괄 커밋** → working tree **CLEAN**, HEAD `npm test` **185/33 PASS**·build **752 modules** — FE-6 #3 해소. v1.2 FE-12·FE-13·FE-14 develop HEAD 반영.
> **FE-15 코드 스플릿 Fixed(32차 — COD 33차 `c98f98d`)**: `vite.config.js` `manualChunks` — 단일 JS 744.95 kB → 최대 393.53 kB(<500 kB). HEAD `npm test` **186/34 PASS**·build **752 modules**·audit 0. 결정 52 흡수 **⑩묶음** 추가.
> **B07 recurrence #5 Fixed(35차 — COD 35차 `d5654c0`, TSR 53차 독립 검증 PASS)**: 52차 CLEAN→DIRTY 20 files → **25 files 일괄 커밋** — FE-17 J01 수락 UI·LogoutButton·BillingPage.layout 등. working tree **CLEAN**, HEAD `npm test` **199/40 PASS**·build **756 modules**·audit 0 — **FE-17** 매핑·결정 52 흡수 ⑪묶음.
> **B07 recurrence #6 Planned(37차 — TSR 56·57차, HEAD Fixed 유지)**: 53차 `d5654c0` CLEAN 직후 **15→18→20 files** WIP — `DateInput`·`GuardianInvitationList` J01·`ClientDetailPage`·`PaymentRecordModal`·`GuardianListCard`(+test, **QA-H05 MaskedPhone 불일치**)·기타 J01/설정 UI. WT build **758 modules PASS**·WT `npm test` **209/210 FAIL**(FE-7) — **FE-18·FE-19** 매핑·#36 FE-6 #5 유지. **HEAD `d5654c0` Fixed(FE-17) 규율 5 유효** — recurrence는 미커밋 dirty-tree 단일.

### 선행·test merge

- **(QA-B05)** 선행: v1 `merge_status: merged` 충족 후 v1.1 이관 착수
- **(QA-B03)** 위 체크리스트 전 항목 `[x]` 후 `merge_status: ready` 설정 → develop→test merge

---

## v1.2 — 프론트 기능 밀도·경쟁사 UI 패리티 (벤치마크 6차 — BNK-6 완료)

- **status**: in_progress (P0 산출물 develop 선행 커밋·v1.1 merge 흡수 대기)
- **merge_status**: pending (결정 52 — v1.1 merge에 동반 흡수)
- **stream**: frontend (+ backend API 보강 병행)
- **목표**: 사용자 체감 「기능이 적다」 해소 — **모듈 커버리지 25~30% → ≥60%**(결정 49) — 케어포 12모듈 대비 **low-cost high-density** 화면 추가
- **선행**: v1.1 `merge_status: merged` (단, **P0 산출물은 develop 선행 커밋·v1.1 merge 동반 흡수** — 결정 52)
- **벤치마크 근거**: `BENCHMARK_REPORT.md` §9·`COMPETITOR_MATRIX.md` §8 (BNK-6, 2026-06-06 **완료**)

> **배경**: ogada v1.1 **24 route**(21 page, SideNav 1단 flat) vs 케어포 **80+ 화면**(2~3단). 갭의 본질은 **신규 도메인 부재**가 아니라 **기존 DB(billing·guardian_clients·clients)의 화면 부재** — P0 5건은 신규 테이블 ≤1개.

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
- [ ] P0 5건 **프론트 E2E** — 보호자 CRUD·입금·미납·등급이력·실데이터 대시보드 (v1.1 merged 후 v1.2 사이클)
- [ ] SideNav **2단 깊이** + 모듈 가중 커버리지 ≥60% (결정 49 KPI) — `routeAccess.js`·`SideNav` 구조 커밋 완료, **수치 측정·튜닝**은 v1.2 사이클
- [x] **(US-M02)** `dashboardWidgets.js` 위젯 집계 로직(오늘 출석/결석·미납·미매칭 NHIS) + `dashboardWidgets.test.js` 3 PASS — develop `a84473f` HEAD 커밋
- [x] **(US-M02·FE-12)** Recharts **차트 레이어** — `ChartContainer`·`AttendanceRateChart`·`BranchCompareChart`·`HealthTrendChart` + `HealthAlertList`(+test) + `ChartContainer.test.jsx`·`HealthTrendChart.test.jsx` develop 커밋 *(develop `4be0938` — `recharts ^2.15.4`, HEAD `npm test` 185/33·752 modules)*
- [x] **(FE-13)** Platform·NHIS 배치·reconciliation·청구·수가표 UI — `BatchProgressSteps`·`PlatformOrgDetailModal`·`BillingStatusConfirmModal`(+test)·`CopayRateTable`(+test)·**`FeeScheduleTable`(+test, US-G00a)**·`NhisImportGuidePanel`(+test)·`GuardianDailySummary`(+test)·Platform/NHIS/Reconciliation/Forbidden 페이지 develop 커밋 *(develop `4be0938`)*
- [x] **(FE-14)** 운영·보안 설정 UI — `AuditLogPanel`(+test)·`BackupSettingsPanel`(+test)·`PasswordChangeModal`(+test)·`FilterChips`·`LoginHistoryPanel`·`PasswordResetRequestModal`·`SettingsPage.test.jsx` develop 커밋 *(develop `4be0938` — SettingsPage 보안 탭 연동 포함)*
- [x] **(FE-15)** 프런트 번들 코드 스플릿 — `vite.config.js` `manualChunks`로 recharts·vendor 분리, 최대 청크 <500 kB *(develop `c98f98d` — COD 33차, TSR 49차 Fixed)*
- [ ] P1 3건(급여제공 세분화·직원근태·간편계산기) — v1.2 후반 또는 v1.2.1
- [ ] `merge_status: ready` 전 체크리스트 전 항목 `[x]` *(결정 52: v1.1 merge에 P0 산출물 동반 흡수, v1.2 별도 ready는 P0 E2E·≥60% KPI 충족 후 — v1.1 merged 후)*

### USER_STORIES 매핑

| Epic | v1.2 범위 |
|------|-----------|
| **K** — 보호자 관리 | US-K01~K02 (P0) |
| **L** — 본인부담 수납 | US-L01~L02 입금·미납 (P0) |
| **M** — 등급·대시보드 | US-M01 등급이력·US-M02 실데이터 위젯 (P0) |
| **UX** — 네비게이션 | US-UX-02 2단 SideNav (P0) |

---

## v1.3 — 배차·이동경로 (결정 60·61·**62**, BNK-7·**BNK-8** G15·G16)

- **status**: planned
- **merge_status**: pending
- **stream**: backend + frontend
- **목표**: **v1.3-A** 픽업 배차 — `hq_admin` 확정 → 직원 명단·지도 조회 (최대 15명). **v1.3-A = 케어포 이동서비스 지도보기 패리티**(BNK-8 — 차별화 아님). **영업 차별 = v1.3-B(TSP·도로경로)**. v1.3-A는 **운영 시각화 한정** — 청구·평가(G15) 미대응(BNK-7 §10-3).
- **선행**: v1.1 `merge_status: merged`

### 범위

| 단계 | 내용 | USER_STORIES | Must |
|------|------|--------------|------|
| **v1.3-A** | 픽업 명단·`hq_admin` 편집·**확정**·직원 **읽기 전용** 조회·지도 (**청구·일지 제외**) | US-T01·T02·T03 | **◎** |
| **v1.3-A.1** | 드롭(DROPOFF) 배차 (픽업과 동일 패턴) | US-T04 | Should |
| **v1.3-B** | TSP·Directions 도로 경로 (**영업 차별 핵심**, BNK-8) | US-T02(B) | Should |
| **v1.3-C** | `vehicles`·이동서비스비 청구·**G15 법정 서식** | US-T05 | Could |

### 완료 기준 (v1.3-A)

- [ ] DBA: `uses_transport`·`pickup_*`·`transport_runs`(DRAFT/CONFIRMED·PICKUP)·`stops`·`confirmed_*`
- [ ] Geocoding 서버 프록시 + `KAKAO_*` env (Directions 제외)
- [ ] API: roster·runs CRUD·**confirm**·RBAC(DRAFT=hq_admin only, CONFIRMED=직원 read)
- [ ] UI: `/transport`·`/transport/runs/new`·`/transport/runs/:id` + 카카오맵
- [ ] **15명 상한** 서버·UI 검증
- [ ] US-T01~T03 E2E — 확정 게이트·마스킹·Geocoding 실패
- [ ] UI·문서에 **「운영 편의용 — 이동서비스비 청구·평가 일지(G15) 미포함」** 고지 (BNK-7 §10-3) + **「케어포 이동서비스 지도보기와 동등 — 경로 최적화는 v1.3-B」** (BNK-8)

### 완료 기준 (v1.3-C — G15·G16)

- [ ] `vehicles` 마스터·정원·차량번호 — `transport_runs` 배정 연계 (G16)
- [ ] 공단 **별지 제22호 이동서비스일지** export·**별지 제18호** 신청 전제 안내 (G15)
- [ ] 급여제공기록지 **이동서비스 제공·차량번호** 연계 (G15)
- [ ] **이동서비스비** 산정·청구 입력 — 고시 제34조 (G16, 케어포 2-5 패리티)

### 미확정 (#41 잔여)

> 지도 벤더(카카오 가정)·출석 연동·픽업 체크 — v1.3-B. 드롭 — v1.3-A.1

---

## v2 — 보호자·알림·결제

- **status**: in_progress
- **merge_status**: pending
- **stream**: backend
- **목표**: 보호자 풀 포털, **카카오톡 채널(비즈메시지) 알림톡**·SMS, CMS·간편결제 (BENCHMARK G1·G2 — 케어포·엔젤 패리티; 엔젤 CMS **월 30,000원+건당 수수료** TCO 벤치마크)
- **선행**: v1.1 프론트 MVP

### 범위

1. 보호자 풀 포털 (명세·기록·사진 열람 — 케어포 가족돌봄앱 수준)
2. **카카오톡 채널 알림톡** 연동 (출석·일일 케어·명세·긴급 알림) + SMS fallback (솔라피·NHN 등 중계 1종)
3. `NotificationService` + `notification_preferences` (보호자별 채널·수신 동의)
4. 본인부담금 **CMS·간편결제** (엔젤 LCMS 벤치마크)

### 알림 채널 단계 (확정 2026-06-06)

| 단계 | 채널 | 비용 | 범위 |
|------|------|------|------|
| v1.1 | 인앱·FCM Web Push·이메일(선택) | 무료~저비용 | 포털·명세 안내 |
| **v2** | **카카오톡 채널 알림톡** | 건당 과금 | 앱 미사용 보호자·출석·긴급 |
| v2 | SMS/LMS | 건당 과금 | 알림톡 실패 fallback |

### 완료 기준

- [x] **(BE-7·QA-B08)** `notification_preferences` — V41 `guardian_notification_preferences`·`NotificationPreferenceService`·`GuardianNotificationPreferenceController` + 단위 테스트 **8 @Test** develop 반영 *(develop `feac558` — V41 + 7 java + 8 @Test HEAD PRESENT, `MustApiEndpointRoutingTest`·`RoleBasedControllerAccessTest` notification routing/RBAC, Maven PASS, 이관 규율 5·8 PASS)*
- [x] **(QA-B08 recurrence #2)** v2 follow-up **develop 반영·working tree clean** — `V42__guardian_notification_preferences_consent_temporal.sql`(kakao/sms 유료 채널 consent CHECK + `consent_at`/`updated_at` temporal monotonicity, API_SPEC §11-3·ERD §4-7-1) + `NotificationPreferenceServiceTest`(4 @Test — paid channel consent stamp·upsert) *(develop `428ba7d` — COD 36차 커밋·working tree **CLEAN**, B08 #2 Fixed)*
- [ ] USER_STORIES Epic J·**J03**·**N**(v2 CMS·결제) 스토리 구현 (보호자 알림·결제)
- [ ] **카카오 비즈니스 채널** 개설·템플릿 심사·발송 API 연동 (US-J03)
- [ ] 출석(도착/귀가)·일일 케어·명세·긴급 알림 **알림톡 E2E** (연결 보호자 `guardian_clients` 대상)
- [ ] QA_FEEDBACK v2 범위 항목 0건 OPEN
- [ ] 본인부담금 보호자 발송·수납 E2E (MVP에서 제외했던 §3-9-3 후속)

---

## v3 — 확장 모듈

- **status**: planned
- **merge_status**: pending
- **stream**: backend
- **목표**: 식사·프로그램·**이동서비스(풀·청구)**·직원·평가·서류 (BENCHMARK G3·G5 — **배차 루트는 v1.3으로 분리**)

### 범위

- Should/Could 모듈 (REQUIREMENTS §3-5~§3-8, §3-10)
- **제외 유지**: 재무회계·세무·4대보험 (이지케어 G4 — Won't, 별도 연동 검토)
- **제외 유지**: NFC/RFID 출석 (G6 — QR B방식 차별화)

### 완료 기준

- [ ] planner·REQUIREMENTS v3 범위 확정 후 갱신
- [ ] 공단 평가 2026 지표 자동화 여부 결정 (Could — 영업 차별 아님)

---

## 변경 이력

| 날짜 | 변경 |
|------|------|
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
