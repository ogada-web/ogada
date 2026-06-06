# 주요 설계 결정 이력 (decisions.md)

> 에이전트 간 공유. 신규 결정은 최상단에 추가한다.

---

## 2026-06-06 — benchmark_researcher: 4차 경쟁사 재검증 (이지케어 요금·2026 수가·G9)

공식 사이트·요금표·롱텀 수가·케어포 2026 매뉴얼 재조사(조사일 **2026-06-06**). 산출물:
`docs/BENCHMARK_REPORT.md`, `docs/COMPETITOR_MATRIX.md` 4차 갱신.

| # | 결정·권고 | 근거 | planner/coder 영향 |
|---|----------|------|-------------------|
| 1 | **`fee_schedules`에 duration_band(이용시간대) 축 검토** — 공단 2026 수가는 **등급×시간(3~6h…13h+)** 2차원 | [롱텀 2026 수가](https://www.longtermcare.or.kr/npbs/e/b/502/npeb502m01.web?menuId=npe0000002742), [케어포 2026 고시](https://www.carefor.co.kr/cs/view_pds.php?calmgno=46327) | G9 — MVP는 파일럿 **1밴드 고정** 가능, v1.1 다밴드; §3-9-1·ERD 보강 |
| 2 | **이지케어 공개 tier 요금** — 10,000 + (일정관리 N−10)×500 + VAT; 37명=25,850 | [ezCare_charge](https://ezcare.easyms.co.kr/new/ezCare_charge.html) | G10 — ogada 가격: 케어포 **flat 33k** vs 이지케어 **인원 비례** (PLAN_NOTES #31) |
| 3 | **롱텀 엑셀 다운로드** — Chrome/Edge 「안전하지 않은 콘텐츠」 허용 필수 | [케어포 FAQ cscmgno=1237](https://www.carefor.co.kr/cs/view_notice.php?cscmgno=1237) | USER_MANUAL·파일럿 NHIS import 온보딩 체크리스트 |
| 4 | **케어포 다지점** — getting_started에 **다기관 통합 매뉴얼 없음** 재확인; 1기관번호=1계정 유지 | [getting_started](https://www.carefor.co.kr/cs/getting_started.php) | ogada `/dashboard/hq` 차별 유지 — PLAN_NOTES #32 |
| 5 | **copay 15/9/6/0%** — 2026 공단·센터 안내와 ogada 4구분 **일치** 확인 | [강남구청 2026 안내](https://www.gangnam.go.kr/board/happyapgu_faq/613/view.do) | §3-9-2 유지; 케어포 3구분(7.5%)과의 UI 라벨 차이만 주의 |
| 6 | **이지케어 EZCARE 보호자** — **기관 초대 → 프로필 수락** 후 명세·청구 조회 | [Google Play](https://play.google.com/store/apps/details?hl=ko&id=com.easyms.ezcare) | v1.1 G8 — ogada `guardian` 초대 흐름 벤치마크 |

**미변경(3차와 동일)**: 청구 2단계, QR B, platform_admin, NHIS `처리상태` 파서, MVP 제외(평가·회계·CMS).

---

## 2026-06-06 — benchmark_researcher: 3차 경쟁사 재검증 (EZCARE·NHIS·롱텀2026)

공식 사이트·매뉴얼·앱스토어·공지 재조사(조사일 **2026-06-06**). 산출물:
`docs/BENCHMARK_REPORT.md`, `docs/COMPETITOR_MATRIX.md` 3차 갱신.

| # | 결정·권고 | 근거 | planner/coder 영향 |
|---|----------|------|-------------------|
| 1 | **NHIS 엑셀 파서** — 선행 `처리상태` 열 **스킵·정규화** 필수 | 케어포 [44438](https://www.carefor.co.kr/cs/view_notice.php?calmgno=44438), [visitcare.pdf §4-1](https://www.carefor.co.kr/pdf_manual/visitcare.pdf) | import 파서·reconciliation — G7 파일럿 샘플과 병행 검증 |
| 2 | **롱텀 2026.01.16 개편** — IE 불가, Chrome/Edge 필수 안내 | [longtermcare 개편 공지](https://longtermcare.or.kr/npbs/e/g/540/openCyberCstMain.web?menuId=npe0000002594) | USER_MANUAL·파일럿 온보딩: 엑셀 export 전 브라우저 체크 |
| 3 | **이지케어 EZCARE 앱** — 보호자 **초대·명세 조회** 지원 확인 | [App Store](https://apps.apple.com/kr/app/%EC%9D%B4%EC%A7%80%EC%BC%80%EC%96%B4-ezcare/id6740553966), 2026.03 주야간 확대 | G8 신규 — v1.1 보호자 포털은 **초대 흐름+명세 탭**이 최소 패리티 |
| 4 | **다지점 HQ** — 경쟁사는 **1기관번호=1계정** 모델(△), ogada Org-Branch **차별 유지** | 케어포 가입·기관기호 11자리; 공식 HQ 대시보드 **미확인** | `/dashboard/hq` Must — PLAN_NOTES #32 |
| 5 | **엔젤 CMS TCO** — 월 30,000원 + 건당 수수료 벤치마크 | [silverangel extraService](https://www.silverangel.kr/newSilverangel/service/extraService.do) | v2 CMS·가격 정책(PLAN_NOTES #31) 입력 |
| 6 | **이지케어 규모** — 9,210 재가기관(2026.06.06 실시간) | [ezcare.easyms.co.kr](https://ezcare.easyms.co.kr/) | 영업·경쟁 포지셔닝 참고 |

**미변경(2차와 동일)**: 청구 2단계, QR B, platform_admin, MVP 제외(평가·회계·CMS).

---

## 2026-06-06 — planner(PLN): 자동 기획 동기화 3차 (QA 0건·문서 식별자 PLA→PLN 정렬)

`build --role planner` 자동 동기화. 입력 문서 재확인 결과 **신규 기획 변경 없음** —
정합성 정렬과 기록만 수행.

| # | 점검·반영 | 산출물 |
|---|----------|--------|
| 1 | `QA_FEEDBACK.md` Open **0건**, `TEST_REPORT.md` 미작성 — Planned 이동 없음 | (변경 없음) |
| 2 | BENCHMARK·COMPETITOR_MATRIX 2차 조사(결정 29–35) **이미 반영** 확인 | (변경 없음) |
| 3 | planner 문서 식별자 정본 정렬: `agents.yaml` 기준 `PLA→PLN`, audience `coder,tester→COD,TSR,UXD,DBA,BNK,TWR` (BNK는 선행 마이그레이션 완료) | `ROADMAP.md`·`PLAN_NOTES.md`·`FLOWCHART.md`·`API_SPEC.md`·`REQUIREMENTS.md`·`USER_STORIES.md` 메타, PLAN_NOTES 섹션 `[PLA]→[PLN]` |
| 4 | 자동 동기화 3차 기록 | `PLAN_NOTES.md` `### [PLN] 자동 기획 동기화 — 3차`, `ROADMAP.md` 변경 이력 |

**트레이드오프**: 식별자 정렬은 본문 메타 주석만 변경(파일명·git 충돌 회피). REQUIREMENTS·
USER_STORIES는 기존에 메타 주석이 없어 신규 추가 — 향후 `doc:owner`/`audience` 자동 점검과 정합.
**미해결 추적**: 추가질문 #27(공단 엑셀 실컬럼·G7), #31(가격 tier), #32(다지점 HQ 사례) — 신규 입력 없어 변동 없음.

---

## 2026-06-06 — planner: 자동 기획 동기화 (벤치마크 2차 → ROADMAP·API·FLOWCHART)

`build --role planner` 자동 동기화. QA_FEEDBACK Open **0건**, TEST_REPORT 미작성.

| # | 반영 | 산출물 |
|---|------|--------|
| 1 | v1 ROADMAP에 P0–P3·NHIS reconciliation 완료 기준·파일럿 P8 추가 | `docs/ROADMAP.md` |
| 2 | API_SPEC §7-4 NHIS reconciliation 5엔드포인트·`?status=` 필터 명세 | `docs/API_SPEC.md` |
| 3 | FLOWCHART §7-1 reconciliation Mermaid 흐름 | `docs/FLOWCHART.md` |
| 4 | PLAN_NOTES `[PLA]` QA·벤치마크 동기화 섹션, 결정 29–35, 추가질문 #30–32 | `docs/PLAN_NOTES.md` |
| 5 | USER_STORIES 파일럿 P8(US-G06) | `docs/USER_STORIES.md` |

**미변경(기존 반영 완료)**: REQUIREMENTS §1-5·§6-2, USER_STORIES US-G06, BENCHMARK/COMPETITOR_MATRIX.

---

## 2026-06-06 — benchmark_researcher: 2차 경쟁사 벤치마크 (케어포·이지케어·엔젤·롱텀)

공식 사이트·매뉴얼·FAQ·공지(조사일 **2026-06-06**) 재조사. 산출물:
`docs/BENCHMARK_REPORT.md`, `docs/COMPETITOR_MATRIX.md` 전면 갱신.

| # | 결정·권고 | 근거 | planner/coder 영향 |
|---|----------|------|-------------------|
| 1 | **청구 2단계(내부계산 + 롱텀 + 엑셀 import + 본인부담)** — ogada MVP 방향 **유지** | 케어포·이지케어 공통 패턴 ([케어포 교육](https://www.carefor.co.kr/cs/view_notice.php?calmgno=43619), [이지케어 fnc](https://ezcare.easyms.co.kr/new/ezCare_fnc.html)) | §3-9·NHIS import 우선 구현 |
| 2 | **QR B방식(보호자→지점 QR)** — **차별화 유지**, NFC/RFID MVP **불필요** | 케어포=NFC 직원앱, 이지케어=RFID(방문), 공개 자료에 보호자 QR **없음** | 파일럿 P1; 하드웨어 제외 |
| 3 | **`platform_admin` Tenant 개통** — 경쟁사 셀프/상담 가입과 **의도적 차별** 유지 | 케어포 셀프+1mo무료, 이지케어 상담, 엔젤 온라인 | §1-3 A방식 확정 재확인 |
| 4 | **다지점 HQ 대시보드** — MVP **Must** (경쟁사 공개 자료 동등 기능 **미확인**) | ogada 파일럿 2지점 | `/dashboard/hq` 파일럿 핵심 |
| 5 | **평가·재무회계·CMS·이동서비스** — MVP **제외** 유지 | 케어포/엔젤=평가·CMS, 이지케어=회계 | Should/Could 로만 로드맵 |
| 6 | **NHIS 엑셀 실컬럼** — 파일럿 센터 샘플 확보 **P0** (PLAN_NOTES #27) | 업계 import 공통이나 ogada 스키마 검증 필요 | import 파서·reconciliation UI |
| 7 | **보호자 포털** — MVP는 **QR+기록열람 골격**, 알림톡/CMS는 **v1.1** | 케어포 가족돌봄앱 성숙 | Should Epic 우선순위 |
| 8 | **가격 벤치마크** — 케어포 주야간 **월 33,000원(VAT포함)** 참고 ([cost.php](https://www.carefor.co.kr/price/cost.php)) | ogada 가격 미정 | 영업·플랫폼 정책 별도 |

**트레이드오프**: 경쟁사는 **기능 폭**(평가·회계·NFC)으로 lock-in; ogada는 **SaaS 다지점·QR·MVP 속도**로 파일럿→전국 판매.

---

## 2026-06-06 — db_architect: V19 마이그레이션 (공단 reconciliation 매칭·배치 무결성)

ERD·V1–V18·API_SPEC·USER_STORIES 재대조. 청구(billing) Must 엔티티 커버리지
점검 중 공단 import reconciliation 결과와 그 전제 데이터를 묶는 무결성 규칙이
없던 3개 공백을 `V19`로 마감. 동시에 ERD 문서 드리프트(V18 미기재,
`clients.discharged_at` 타입 표기 오류)를 정정.

| # | 결정 | 근거 |
|---|------|------|
| 1 | `nhis_import_rows`: `match_status`가 `MATCHED`/`DISCREPANCY`이면 `client_id` 필수 (`chk_nhis_import_rows_match_requires_client`) | 매칭 결과와 매칭 대상 이용자가 항상 함께 존재 — 이용자별 reconciliation 뷰 정합(API §7-3). `UNMATCHED`만 `client_id` NULL 허용 |
| 2 | `nhis_import_batches.row_count >= 0` | 파싱 행 수 음수 방어 |
| 3 | `nhis_import_batches`: `status = COMPLETED`이면 `imported_at` 필수 | `backup_runs` 완료 시각 패턴(V9/V12)과 정합 — 완료된 import는 완료 시각 보유 |

**트레이드오프**
- 세 제약 모두 유효 데이터에 대해 항상 참 → greenfield 기존 행 거부 없음. CHECK로
  표현 가능(교차 테이블 아님)하여 트리거 대신 ALTER ADD CONSTRAINT 사용.
- 배치 제약은 `COMPLETED`만 대상(`FAILED`/`PENDING`/`PROCESSING`은 `imported_at` NULL 허용).

**문서 정정**: ERD §4-3 `discharged_at` 타입 `date → timestamptz`(V2 실제와 일치),
§4-4 `branch_qr_tokens.token_value`(V18) 반영, §7 마이그레이션 표 V18·V19 추가.

**coder 영향**: 공단 엑셀 매칭 서비스는 행을 `MATCHED`/`DISCREPANCY`로 전이할 때
반드시 `client_id`를 함께 세팅해야 한다(부분 업데이트 금지). 배치 완료 처리 시
`status=COMPLETED`와 `imported_at`을 같은 트랜잭션에서 기록한다.

---

## 2026-06-05 — db_architect: V8 마이그레이션 (Tenant 무결성 + 청구 불변)

ERD·V1–V7·API_SPEC·USER_STORIES 대조 후, 문서엔 명시됐으나 DB로 강제되지
않던 4개 공백을 `V8`로 마감.

| # | 결정 | 근거 |
|---|------|------|
| 1 | `users.active_branch_id` 복합 FK `(organization_id, active_branch_id)` → `branches` | 활성 지점이 타 Tenant 지점일 수 없도록 차단 (V4/V5/V7 Tenant FK 패턴 일관화) |
| 2 | 청구 확정 후 **불변** 트리거 (`billing_claims`·`billing_claim_items`) + 단방향 상태 전이 | REQUIREMENTS §3-9-1 이력 보존, USER_STORIES US-G05 "확정 후 수정 제한", ERD §4-6 "확정 후 불변" |
| 3 | `nhis_import_rows`에 `organization_id` + 복합 FK(배치·이용자) | reconciliation 매칭이 타 Tenant 이용자로 새는 것 방지 (API §7-3) |
| 4 | `health_records (organization_id, record_type, recorded_at DESC)` 인덱스 | `GET /dashboard/hq/alerts` 전 지점 건강 이상 집계 (V7 attendance HQ 인덱스와 동형) |

**결정 배경 / 트레이드오프**
- 청구 불변은 CHECK로 표현 불가(이전 상태 비교 필요)하므로 BEFORE UPDATE/INSERT/DELETE
  **트리거**로 구현. `status` 전이와 `updated_at`은 허용, 금액·스코프만 잠금.
- `billing_claim_items` 동결 트리거는 부모 cascade 삭제 시 부모 행이 먼저 제거되어
  `SELECT status`가 NULL → 정상 cascade 허용(직접 조작만 차단).
- `nhis_import_rows.client_id`는 매칭 전 NULL이므로 복합 FK는 MATCH SIMPLE로 NULL 스킵.
- 기존 단순 FK는 유지(중복이나 무해), 복합 FK로 Tenant 스코프만 추가.

**coder 영향**: 청구 확정(`PATCH /billing/claims/{id}/status`)은 금액 재계산 없이
상태만 전이해야 함. 확정 후 라인/금액 수정 시도는 DB가 거부 → 애플리케이션은
DRAFT 단계에서만 generate/재계산 수행.
