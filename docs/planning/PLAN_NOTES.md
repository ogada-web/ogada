<!-- doc:owner=PLN doc:audience=COD,TSR,UXD,DBA,BNK,TWR updated=2026-06-08T06:39:00+00:00 -->
# 기획 메모 (planning/PLAN_NOTES.md)

> **작성**: planner 에이전트 (`PLN`)  
> **최종 갱신**: 2026-06-08 (63차 — TSR 87·88차 + v1.3-A transport unconfirm + v3 StaffPage + merge 게이트 정의 · baseline `0d8968d`/`fe33e7c`)  
> **상태**: 초안 (사용자 승인 전)

---

### [COD] 현재 baseline (planner 63차 git 실측 — 단일 진실 원천)

| stream | develop HEAD | test HEAD | WT | ahead of test | 비고 |
|--------|--------------|-----------|-----|---------------|------|
| backend | **`0d8968d`** | `2799e29` | **CLEAN** | **19** | v1.3-A transport unconfirm hq_admin @ `0d8968d` · v3 meals/programs @ `dfd9be2`+ · **`mvn test` 226/226** |
| frontend | **`fe33e7c`** | `c510f5c` | **CLEAN** | **8** | v3 StaffPage UI @ `fe33e7c` · v3 meals/programs+E2E @ `362dbf0`+ · v1.3 transport @ `e8d1854`+ · **`npm test` 170/55** · **140 modules** |

> **폐기 SHA**: `d5654c0`(TSR57)·`e5fd48d`(스켈레톤)·`428ba7d`(TSR56)·**`4be0938`**(24 route — git object 없음) — checkout 재현 **금지**.  
> **확정 파일**: `.agents/workspace_baseline.yaml` · `run_agent.py` build 시 **실측 git HEAD 자동 주입** — **63차 git 실측이 stale baseline보다 우선**.  
> **Fixed @ 63차**: v3 §3-5·§3-6 @ `dfd9be2`+·v3 StaffPage UI @ `fe33e7c` **PRESENT** · v1.3-A transport API+unconfirm @ `0d8968d` **PRESENT** · v1.3 transport UI @ `e8d1854`+ **PRESENT** · US-T01~T03 live E2E + unconfirm 프론트 UI **잔여**.

---

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

#### #74-1. 본인부담 부분입금 스키마 (Epic L, US-L01/L02)

| 항목 | 현황 | 결정 대기 |
|------|------|-----------|
| MVP | `billing_claims.status` DRAFT→CONFIRMED→PAID + `billing_claim_status_history` | TSR 82 PAID 알림 연동 완료 |
| v1.2 P0 | 입금일·금액·수단(현금/계좌)·부분입금 | API_SPEC 엔드포인트 **미작성** |
| 설계 가설 | ① `billing_payments` 자식 테이블(복수 입금) 또는 ② `billing_claims`에 `paid_at`/`payment_method` 단일 컬럼 | 부분입금 허용 여부·미납 집계 규칙 확정 후 **V50** |

### 추가 질문

다음 항목이 확정되기 전까지 상세 스펙·일정·구현 범위는 가정으로만 기재한다.

#### [PLN] v3 StaffPage 완전 기능 범위 미확정 (2026-06-08, 63차)
- **관측**: `fe33e7c`에 StaffPage v3 UI develop 진입 확인(TSR 88차). 그러나 API 연동·Vitest·근태 관리 상세 범위 미확정.
- **미확정 항목**:
  - 직원 정보 CRUD API 엔드포인트 스펙 (`/api/v1/staff/*` 또는 기존 `users` 재활용 여부)
  - 근태(출퇴근) 기록 — 별도 테이블 vs `attendance_records` 유사 패턴
  - 직원 앱/모바일 뷰 필요 여부 (케어포 §8-4 방식)
- **가정**: API_SPEC v3 직원 섹션 확정 전까지 frontend UI shell 유지, backend API는 v3 merge-blocking 완료 기준 충족 시 함께 merge.

#### [PLN] v1.3-A unconfirm 프론트 UI 범위 (2026-06-08, 63차)
- **관측**: backend `0d8968d`에 `PATCH /api/v1/transport/runs/{id}/unconfirm` hq_admin API 구현 완료. frontend `TransportRunDetailPage` unconfirm 버튼·확인 다이얼로그 잔여.
- **미확정**: unconfirm 후 UI 상태(DRAFT 뷰 복귀 vs 별도 메시지) — coder가 UXD와 협의 후 구현 가능.
- **블로커 아님**: v1.3 merge_status: ready 판단은 frontend unconfirm UI + US-T01~T03 live E2E 충족 후.

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

#### 배차(Geocoding) 정책: 결정 필요
- 서버 프록시 Geocoding의 운영 정책을 확정해야 합니다.
  - 선택 항목: 캐시 TTL (예: 30일) 여부 및 값
  - 실패 처리: (A) 주소 저장 차단 + 사용자 경고, 또는 (B) 주소는 저장하되 `geocode_status=FAILED`로 표기(경고 아이콘)하고 후속 보정 허용
  - 권한: `geocode_status=FAILED`인 정차는 저장 가능하되 `hq_admin`이 확인/수정 권한 보유 권고
  - 결정 필요: 캐시 갱신 주기(수동 재지오코드 vs 자동 재시도 정책)
 
설명 및 권고안 (간단)
- Geocoding이란: 주소 텍스트(예: "서울 중구 OO로 12")를 지도 좌표(위도/경도)로 변환하는 과정입니다. 지도 마커·폴리라인을 그리려면 좌표가 필요합니다.
- 캐시 정책(사용자 확정): 지오코딩 결과(`clients.pickup_lat`/`pickup_lng`)는 **영구 보관(무기한 캐시)**으로 처리합니다. 자동 만료는 적용하지 않습니다.
- 실패 처리(사용자 확정): 지오코드 실패 시에도 주소는 저장되며, 해당 정차에 `geocode_status=FAILED`를 기록합니다. 지도에는 경고(⚠)로 표시되고, `hq_admin`이 보정·재시도할 책임을 집니다.
- 재지오코드 권한: `hq_admin` 전용 UI(예: "재지오코드" 버튼)를 통해 해당 정차에 대해 재시도하거나 수동으로 좌표를 입력할 수 있습니다. 자동 재시도/주기적 백그라운드 재시도는 적용하지 않습니다.
- 주소 필드 검증 추가 요구사항(사용자 요청)
 - 주소는 두 컬럼으로 관리합니다: `clients.address_search`(필수, 정규화된 검색/검증 단위) 및 `clients.address_detail`(상세주소, 선택).
 - 이용자 생성/수정 시 서버에서 `address_search` 형식 검증(시/도·시군구·도로명/지번 또는 우편번호 포함) 및 정규화(카카오 Geocoding 또는 주소 정규화 엔진)를 수행해야 합니다.
 - `address_detail`은 상세(호수·층·참고사항 등)로 자유 입력 허용. `address_search` 검증 실패 시 기본 동작은 저장 거부(400). `hq_admin` 전용 강제 저장 옵션 허용(강제 저장 시 `address_verified=false` 표기 및 감사 로그 필요).
 - 저장된 주소는 PII로 취급하여 암호화/접근로그 적용 권고.

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
41. **배차·이동경로** (2026-06-07, **41차**) — ① ~~정차 상한~~ → ✅ **15명**(결정 62) ② ~~확정 주체~~ → ✅ **`hq_admin` 확정·직원 조회**(결정 62) ③ ~~방향~~ → ✅ **픽업만** v1.3-A; 드롭=v1.3-A.1(US-T04) ④ TSP=v1.3-B ⑤ 출석·픽업체크=v1.3-B ⑥ 청구=v1.3-C ⑦ 지도=카카오(가정) ⑧ 차량 엔티티=v1.3-C.
42. ~~**v1 backend develop baseline**~~ → **해소(45~46차, QA-B10·BE-10 Fixed)** — baseline **`136239e`/`7170b2a`** 확정 · `.agents/workspace_baseline.yaml` · v1 E2E/routing develop HEAD **PRESENT**. replay/cherry-pick **불필요**.
43. **카카오 Directions API 비용 (2026-06-08, BNK-8 → BNK-9 해소)** — v1.3-B 설계 입력 **확정**: 자동차 일 **10,000건 무료·8원/건** · **다중 경유지** 일 **5,000건·16원/건** ([Kakao Mobility price](https://developers.kakaomobility.com/price/)). v1.3-B PoC는 **다중 경유지 API** 권장(15정차 TSP). Geocoding·JS SDK는 파일럿 무료 쿼터 내.
44. **이동서비스비 '러-1'~'러-4' 2026 실액 (2026-06-08, BNK-8·BNK-9 §12-2)** — v1.3-C **`transport_service_fee` 테이블** 시드 전 [law.go.kr](https://www.law.go.kr) **1차 확인 잔여**. BNK-9 2차 출처: **830/2,630/4,440/6,240원**(편도·러-1~4). **상수 하드코딩 금지** — law.go.kr 확정 후 Flyway 시드.
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

### [TWR] 문서 작성 질문

> tech_writer (`TWR`) — 2026-06-06 **12차 자율 실행 완료**.
> 
> ✅ **문서화 완료**:
> - Q111: `GET /billing/imports/nhis/guidance` — 롱텀 2026 Chrome/Edge·export 절차
> - Q112: `SessionTimeoutProvider` US-B03 — 30분 idle·60초 경고 모달
> - Q102·Q60·Q83 갱신: `ClientDetailPage` US-D03 건강(경로 정합·payload 불일치)·출석(API 경로 불일치)
> - CHANGELOG·USER_MANUAL·ADMIN_GUIDE·DEPLOYMENT·FAQ — 테스트 **28클래스/127건**·`fac3d07` 동기화
>
> ⏳ **대기 중** (COD/PLN 검토 필요):
> - TWR-Q1: `services.js` 정합 — 출석 탭 `GET /clients/{id}/attendance`, 건강 `payload` 매핑, SSN reveal POST
> - TWR-Q4: `social_worker` SSN [열람] UI 추가 후 반영

**이전 질문 내용**:
- **TWR-Q1**: `POST /clients/{id}/resident-registration/reveal`, `/guardian/checkin-targets`, `/clients/{id}/billing` 등 API 경로 불일치 → services.js 정합 대기 중
- **TWR-Q2**: v1 vs v1.1 구현 범위 확정 필요 → 기획팀 판단 대기
- **TWR-Q3**: guardian API 스키마 상세 기술 필요 → 기획팀 작업 대기
- **TWR-Q4**: 역할별 UI 버튼 노출 정책 필요 → 코더 구현 확인 대기

---
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
