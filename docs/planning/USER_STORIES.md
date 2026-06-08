<!-- doc:owner=PLN doc:audience=COD,TSR,UXD,DBA,BNK,TWR updated=2026-06-08T14:00:00+09:00 -->
# 주간보호센터 웹 시스템 — 사용자 스토리 (planning/USER_STORIES.md)

> **작성**: planner 에이전트  
> **최초 작성일**: 2026-06-05  
> **최종 갱신**: 2026-06-08 (62차 — v3 meals/programs full stack + v1.3 live E2E 잔여 + BNK-9 재확인)  
> **상태**: 초안 (Draft) — 사용자 승인 전  
> **근거 문서**: `docs/planning/REQUIREMENTS.md`, `docs/planning/PLAN_NOTES.md`, `docs/planning/research/BENCHMARK_REPORT.md`, `docs/qa/QA_FEEDBACK.md`

---

## 1. 문서 개요

| 항목 | 내용 |
|------|------|
| 프로젝트 | ogada — 전국 판매 B2B SaaS 주간보호센터 운영 관리 |
| MVP 범위 | 플랫폼관리, 다지점, 인증, 이용자, 출석(수기+QR), 건강, 청구(케어포식), 대시보드 |
| 파일럿 | 실제 센터, **지점 2곳**, **센터장 1 + 요양보호사 5** |
| 파일럿 역할 | `branch_admin`, `caregiver` **만** 현장 검증 |
| 스토리 ID | `US-{Epic}{순번}` (예: US-A01) |

### 우선순위·파일럿 표기

| 표기 | 의미 |
|------|------|
| **Must** | MVP v1 필수 |
| **Should** | v1 이후 |
| **Pilot** | 파일럿 현장에서 검증할 스토리 |

---

## 2. 파일럿 핵심 시나리오 (요약)

**전제**: 2지점 운영 센터, 센터장 1명이 두 지점 총괄, 요양보호사 5명이 지점별 출석·건강 기록.

```
[아침] 요양보호사 → 수기 체크인 → 건강·투약 기록
[월말] 센터장 → 출석·등급 기반 청구서 확인 → 공단 엑셀 import → reconciliation 매칭 보정 → 본인부담금 명세서 생성
[상시] 센터장 → 지점 전환 → 지점별 대시보드·이용자 관리
```

---

## 3. Epic A — 플랫폼·고객 온보딩 (`platform_admin`)

### US-A01 — 신규 고객 센터 등록

| 항목 | 내용 |
|------|------|
| 역할 | `platform_admin` (ogada 직원) |
| 스토리 | ogada 직원으로서, **새 주간보호센터 법인을 시스템에 등록**하고 싶다. 그래야 전국 판매 고객이 서비스를 시작할 수 있다. |
| 우선순위 | Must |
| Pilot | No |

**인수 조건**
- [ ] `/platform`에서 Organization(법인명, 연락처 등) 생성 가능
- [ ] 생성된 Tenant는 다른 Organization 데이터에 접근 불가
- [ ] Tenant 목록 조회·검색 가능

### US-A02 — 센터장 첫 계정 발급

| 항목 | 내용 |
|------|------|
| 역할 | `platform_admin` |
| 스토리 | ogada 직원으로서, 신규 Tenant에 **첫 `hq_admin` 또는 `branch_admin` 계정**을 발급하고 싶다. 그래야 고객이 로그인해 운영을 시작할 수 있다. |
| 우선순위 | Must |
| Pilot | No |

**인수 조건**
- [ ] Tenant 생성 시 또는 생성 후 관리자 계정(이메일·임시 비밀번호) 발급
- [ ] 발급된 계정으로 최초 로그인·비밀번호 변경 가능

---

## 4. Epic B — 인증·권한 (공통)

### US-B01 — 역할별 로그인

| 항목 | 내용 |
|------|------|
| 역할 | 전 역할 |
| 스토리 | 사용자로서, **내 역할에 맞는 홈 화면**으로 로그인하고 싶다. 그래야 권한 밖 메뉴에 접근하지 않는다. |
| 우선순위 | Must |
| Pilot | Yes (`branch_admin`, `caregiver`) |

**인수 조건**
- [ ] 이메일·비밀번호 로그인
- [ ] JWT에 `role`, `organization_id`, `branch_ids`, `active_branch_id` 포함
- [ ] `branch_admin` → `/dashboard`, `caregiver` → `/dashboard` (메뉴 차이)
- [ ] 권한 없는 URL 접근 시 403 또는 리다이렉트

### US-B02 — 지점 선택 (Branch Switcher)

| 항목 | 내용 |
|------|------|
| 역할 | `branch_admin` (다지점 권한 시) |
| 스토리 | 센터장으로서, **2개 지점 중 작업할 지점을 선택**하고 싶다. 그래야 해당 지점 데이터만 보고 수정할 수 있다. |
| 우선순위 | Must |
| Pilot | Yes |

**인수 조건**
- [ ] UI 지점 선택기로 `active_branch_id` 변경
- [ ] 변경 후 이용자·출석·건강·대시보드가 선택 지점 기준으로 갱신
- [ ] 타 지점 데이터 CRUD 불가

### US-B03 — 세션 만료

| 항목 | 내용 |
|------|------|
| 역할 | 전 역할 |
| 스토리 | 사용자로서, 30분 비활성 시 **자동 로그아웃**되길 원한다. 그래야 공용 PC에서 개인정보가 노출되지 않는다. |
| 우선순위 | Must |
| Pilot | No |

**인수 조건**
- [ ] 30분 비활성 후 재인증 필요
- [ ] 민감 화면 재접근 시 로그인 페이지 이동

---

## 5. Epic C — 다지점·조직

### US-C01 — 지점 등록

| 항목 | 내용 |
|------|------|
| 역할 | `branch_admin` 또는 `hq_admin` |
| 스토리 | 센터장으로서, **우리 법인의 지점(2곳)을 등록**하고 싶다. 그래야 지점별 이용자·출석을 분리 관리할 수 있다. |
| 우선순위 | Must |
| Pilot | Yes |

**인수 조건**
- [ ] 지점명, 주소, 연락처 등록·수정
- [ ] 등록된 지점에 `branch_id` 부여
- [ ] 파일럿: 2지점 등록·구분 조회 가능

### US-C02 — 테넌트 데이터 격리

| 항목 | 내용 |
|------|------|
| 역할 | 시스템 (비기능) |
| 스토리 | 운영자로서, **다른 센터 법인 데이터가 절대 섞이지 않**길 원한다. 그래야 전국 SaaS로 판매할 수 있다. |
| 우선순위 | Must |
| Pilot | No |

**인수 조건**
- [ ] 모든 API·쿼리에 `organization_id` 강제
- [ ] 타 Tenant ID로 요청 시 404/403

---

## 6. Epic D — 이용자 관리

### US-D01 — 이용자 등록

| 항목 | 내용 |
|------|------|
| 역할 | `branch_admin` |
| 스토리 | 센터장으로서, **소속 지점 이용자(어르신)를 등록**하고 싶다. 그래야 출석·건강·청구의 기준 데이터가 생긴다. |
| 우선순위 | Must |
| Pilot | Yes |

**인수 조건**
- [ ] 이름, 생년월일, 성별, 주소, 연락처, 장기요양등급, 인정번호 입력
- [ ] **주민등록번호 입력** — 수집·이용 **별도 동의** 체크 전에는 저장 차단 (§3-2-1)
- [ ] 주민등록번호는 **암호화 저장**, 화면·목록에는 **마스킹** 표시
- [ ] **본인부담 구분(`copayType`)** 선택: 일반 15% / 감경 9% / 감경 6% / 기초수급 0%
- [ ] `branch_id` 필수 (현재 `active_branch_id` 지점)
- [ ] 보호자 **1명 이상 필수** — `POST /clients` 요청에 `primaryGuardian`(기존 `guardian` 계정 ID) 포함, 등록과 동시 `guardian_clients` 연결
- [ ] 사진 업로드 (선택)
- [ ] (선택) 이용자 본인 `client_user` 계정 발급·연결

### US-D02 — 이용자 목록·검색

| 항목 | 내용 |
|------|------|
| 역할 | `branch_admin`, `caregiver`(읽기) |
| 스토리 | 직원으로서, **지점별 이용자 목록을 검색·필터**하고 싶다. 그래야 빠르게 대상자를 찾을 수 있다. |
| 우선순위 | Must |
| Pilot | Yes |

**인수 조건**
- [ ] 이름·인정번호 검색, 페이지네이션
- [ ] `caregiver`는 읽기만, `branch_admin`은 CRUD
- [ ] 현재 선택 지점 이용자만 표시

### US-D03 — 이용자 상세 (탭)

| 항목 | 내용 |
|------|------|
| 역할 | `branch_admin` |
| 스토리 | 센터장으로서, 이용자 **기본정보·건강·출석·청구를 한 화면(탭)**에서 보고 싶다. |
| 우선순위 | Must |
| Pilot | Yes (청구 탭은 월말) |

**인수 조건**
- [ ] `/clients/:id` 탭: 기본정보 / 건강 / 출석 / 청구
- [ ] 각 탭에 해당 모듈 이력 표시
- [ ] 기본정보 탭의 주민등록번호는 마스킹, 권한자가 명시적으로 펼칠 때만 복호화·audit_log 기록

### US-D04 — 주민등록번호 수집·동의 처리

| 항목 | 내용 |
|------|------|
| 역할 | `branch_admin`, `social_worker` |
| 스토리 | 센터장으로서, **법령에 따라 주민등록번호를 안전하게 수집·보관**하고 싶다. 그래야 공단 청구를 할 수 있으면서 개인정보보호법을 지킬 수 있다. |
| 우선순위 | Must |
| Pilot | Yes |

**인수 조건**
- [ ] 수집·이용 **동의 체크** 없이는 주민번호 저장 불가
- [ ] 저장 시 **암호화**, 응답·목록·로그·에러에는 **마스킹**(`******-*******`)
- [ ] 복호화·열람 시 **audit_log** 기록 (누가·언제)
- [ ] 청구·법정 목적 외 사용 차단

---

## 7. Epic E — 출석 관리

### US-E01 — 수기 체크인/아웃 (파일럿 핵심)

| 항목 | 내용 |
|------|------|
| 역할 | `caregiver` |
| 스토리 | 요양보호사로서, **이용자 목록에서 입소·퇴소(체크인/아웃)를 수기 처리**하고 싶다. 그래야 아침 업무 때 빠르게 출석을 기록할 수 있다. |
| 우선순위 | Must |
| Pilot | **Yes** |
| **55차 진전 (TSR 75 @ `6f3f746`)** | 수기 체크인/아웃 UI — `/attendance/checkin` **WIP** |

**인수 조건**
- [ ] `/attendance/checkin`에서 당일 이용자 목록 표시
- [ ] 체크인/아웃 시각 자동 기록
- [ ] `check_in_method` = `manual`
- [ ] 귀가 교통편 선택 (자가용, 차량 서비스 등)
- [ ] 결석 사유 입력 가능

### US-E02 — 일일 출석 현황

| 항목 | 내용 |
|------|------|
| 역할 | `branch_admin`, `caregiver` |
| 스토리 | 직원으로서, **오늘 지점 출석 현황(입소/미입소/퇴소)**을 한눈에 보고 싶다. |
| 우선순위 | Must |
| Pilot | Yes |
| **55차 진전 (TSR 75 @ `6f3f746`)** | 일일 출석 현황 UI — `/attendance` 당일 집계 **WIP** |

**인수 조건**
- [ ] `/attendance` 당일 집계: 입소 N명, 결석 N명, 퇴소 완료 N명
- [ ] 지점 스코프만 표시

### US-E03 — 지점 QR 생성

| 항목 | 내용 |
|------|------|
| 역할 | `branch_admin` 또는 `caregiver` |
| 스토리 | 직원으로서, **지점 입구용 QR(입소/귀가)**를 생성·출력하고 싶다. 그래야 보호자 셀프 체크인을 지원할 수 있다. |
| 우선순위 | Must |
| Pilot | No (파일럿은 수기 중심, QR는 MVP 구현) |
| **55차 진전 (TSR 75 @ `a627c6d`)** | 지점 QR 생성 UI — `/attendance/qr/generate` **WIP** |

**인수 조건**
- [ ] `/attendance/qr/generate`에서 지점·유형(입소/귀가)·유효기간 포함 QR 생성
- [ ] 인쇄·이미지 저장 가능

### US-E04 — 보호자 QR 셀프 체크인

| 항목 | 내용 |
|------|------|
| 역할 | `guardian`, `client_user`(조건부) |
| 스토리 | 보호자로서, **입구 QR을 스캔해 연결 이용자 출석**을 처리하고 싶다. |
| 우선순위 | Must |
| Pilot | No (파일럿 역할 제외, MVP 구현) |
| **53차 진전 (TSR 73 @ `a68f150`)** | `GuardianCheckinPage` DS **FilterChips** 적용 — DESIGN_SYSTEM 유틸리티 전환 |

**인수 조건**
- [ ] `/guardian/checkin` QR 스캔 → 연결 이용자 체크인/아웃
- [ ] 복수 이용자 시 대상 선택
- [ ] `check_in_method` = `qr_self`
- [ ] `allow_client_self_checkin` on 시 `client_user`도 동일

### US-E05 — 월별 출석 통계

| 항목 | 내용 |
|------|------|
| 역할 | `branch_admin` |
| 스토리 | 센터장으로서, **월별 출석률·결석 통계**를 보고 싶다. 그래야 청구·운영 보고에 활용할 수 있다. |
| 우선순위 | Must |
| Pilot | Yes |
| **55차 진전 (TSR 75 @ `a627c6d`)** | 월별 출석 통계 API·UI — 지점·기간 필터 **WIP** |

**인수 조건**
- [ ] 지점·기간 필터
- [ ] 이용자별·지점별 출석 일수 집계

---

## 8. Epic F — 건강 기록

### US-F01 — 일일 건강 체크 (파일럿 핵심)

| 항목 | 내용 |
|------|------|
| 역할 | `caregiver` |
| 스토리 | 요양보호사로서, **이용자별 혈압·체온·혈당·산소포화도**를 기록하고 싶다. |
| 우선순위 | Must |
| Pilot | **Yes** |

**인수 조건**
- [x] `/health` 또는 이용자별 화면에서 당일 건강 수치 입력 — **`VitalsRecordForm` UI @ `c5708c7`(UXD-39)** · **API DTO 정합 Fixed @ `4957bd3`(Q154)** — `healthApiPayload.js` → `bloodGlucose`·`recordedAt`
- [x] 필수값 검증 (비정상 범위 시 표시·알림 목록 반영) — **`vitalsRanges.js`·인라인 경고 @ `9863312`(UXD-40)** *(저장 비차단)*
- [x] 기록자·시각 자동 저장 — **`recordedAt` KST ISO 자동 @ `4957bd3`(Q154)** · `administeredBy` JWT 연동(투약)

### US-F02 — 투약 기록

| 항목 | 내용 |
|------|------|
| 역할 | `caregiver` |
| 스토리 | 요양보호사로서, **약품명·용량·시간·투약자**를 기록하고 싶다. 그래야 복약 누락을 방지할 수 있다. |
| 우선순위 | Must |
| Pilot | Yes |

**인수 조건**
- [x] 투약 기록 CRUD — **`MedicationRecordForm` UI @ `c5708c7`(UXD-39)** · **API DTO 정합 Fixed @ `4957bd3`(Q154)** — `administeredAt`·`administeredBy`·`recordedAt`
- [x] 동일 이용자·동일 시간 중복 경고 — **`MedicationDuplicateAlert` @ `c5708c7`**

### US-F03 — 낙상·특이사항

| 항목 | 내용 |
|------|------|
| 역할 | `caregiver`, `branch_admin` |
| 스토리 | 직원으로서, **낙상·사고·특이사항 메모**를 남기고 싶다. |
| 우선순위 | Must |
| Pilot | Yes |

**인수 조건**
- [x] 이벤트 유형·내용·시각 기록 — **`IncidentRecordForm` UI @ `3ec8206`(UXD-41)** · **API DTO 정합 Fixed @ `95b92b9`(Q154)** — `healthApiPayload.js` → `incidentType`·`detail`·`recordedAt`
- [x] 대시보드 「건강 이상」목록에 반영 — **`HealthAlertList` @ `DashboardPage`** · `pilotPageFlows` US-F03 dashboard E2E PASS

### US-F04 — 건강 이력·그래프

| 항목 | 내용 |
|------|------|
| 역할 | `branch_admin` |
| 스토리 | 센터장으로서, 이용자 **건강 추이 그래프**를 보고 싶다. |
| 우선순위 | Must |
| Pilot | No |

**인수 조건**
- [x] `/health/:client_id` 기간별 혈압·체온 등 차트 — **`HealthDetailPage` 표+`FilterChips` 7/30일 @ `c5708c7`(UXD-39)** *(Recharts → 표 형식, flat 필드 매핑)*
- [x] 최소 7일·30일 조회

---

## 9. Epic G — 청구·정산 (케어포식)

### US-G00a — 수가표 관리 (B방식)

| 항목 | 내용 |
|------|------|
| 역할 | `hq_admin` |
| 스토리 | 통합 관리자로서, **등급별·연도별 수가(1일 단가)를 화면에서 직접 등록·수정**하고 싶다. 그래야 공단 수가가 개정돼도 코드 변경 없이 청구에 반영할 수 있다. |
| 우선순위 | Must |
| Pilot | Yes (월말 청구 전 1회 설정) |

**인수 조건**
- [ ] `/billing/fee-schedules`에서 연도·등급별 1일 수가 입력·수정
- [x] 수가 변경 시 **버전·이력 보존** UI — `FeeRateHistoryPanel`(UXD 14차 `a42d6fb`) 이력 모달·Recharts 토큰(`chartColors.js`) *(과거 청구 당시 수가 유지는 백엔드 이력 API live 연동 후 완료 — v1.1 merge 후)*
- [ ] (선택) 가산·식대 등 부가 항목 입력 구조
- [ ] 코드 하드코딩 금지 — 전적으로 테이블 기반
- [ ] **(G9, 4차 벤치마크)** 2026 공단 수가는 **등급×이용시간대(3~6h…13h+)** 2차원 — **v1: 센터 표준 이용시간 1밴드 고정**, **v1.1: `duration_band` 다밴드** 입력 (추가질문 #35, §3-9-1 보강)

### US-G00b — 본인부담 비율표 관리

| 항목 | 내용 |
|------|------|
| 역할 | `hq_admin` |
| 스토리 | 통합 관리자로서, **본인부담 구분별 비율(일반/감경/기초)**을 관리하고 싶다. 그래야 정책 변경 시에도 청구가 정확하다. |
| 우선순위 | Must |
| Pilot | No (기본값 제공, 필요 시 수정) |

**인수 조건**
- [ ] `/billing/copay-rates`에서 구분별 비율 조회·수정 (GENERAL 15% / REDUCED_40 9% / REDUCED_60 6% / MEDICAID 0%)
- [ ] 이용자별 `copayType`(US-D01)이 이 비율을 참조해 계산에 사용

### US-G01 — 급여 항목 자동 계산

| 항목 | 내용 |
|------|------|
| 역할 | `branch_admin` |
| 스토리 | 센터장으로서, **이용자 등급·출석일수 기준으로 급여 항목이 자동 계산**되길 원한다. |
| 우선순위 | Must |
| Pilot | Yes |

**인수 조건**
- [ ] 월·지점·이용자 단위 급여 산정
- [ ] **수가표(US-G00a)** 기반: `총 급여비용 = 등급 수가 × 출석일수`
- [ ] 출석 데이터(`attendance`)와 연동
- [ ] 이용자 `copayType` 비율(US-G00b)로 본인부담금·공단부담 자동 분리

### US-G02 — 월별 청구서·명세서 생성

| 항목 | 내용 |
|------|------|
| 역할 | `branch_admin` |
| 스토리 | 센터장으로서, **월별 청구서·급여비용 명세서를 생성·출력**하고 싶다. (케어포 유사) |
| 우선순위 | Must |
| Pilot | Yes |

**인수 조건**
- [ ] `/billing` 목록: 월·지점·상태(작성중/확정/수납완료)
- [ ] 개별·일괄 생성
- [ ] PDF 또는 인쇄 가능 명세서

### US-G03 — 본인부담금 계산·청구서

| 항목 | 내용 |
|------|------|
| 역할 | `branch_admin` |
| 스토리 | 센터장으로서, **본인부담금을 계산하고 청구서를 만들**고 싶다. (공단 청구와 별도) |
| 우선순위 | Must |
| Pilot | Yes |

**인수 조건**
- [ ] 이용자별 `copayType` 비율(US-G00b)·등급 수가 반영
- [ ] 이용자별 본인부담금 명세 (`본인부담금 = 총액 × 부담률`)
- [ ] 보호자 발송·CMS는 MVP 제외

### US-G04 — 공단 청구내역 엑셀 import

| 항목 | 내용 |
|------|------|
| 역할 | `branch_admin` |
| 스토리 | 센터장으로서, **공단에서 받은 청구내역상세 엑셀을 업로드**해 ogada에 반영하고 싶다. (케어포 4단계) |
| 우선순위 | Must |
| Pilot | Yes |

**인수 조건**
- [ ] 공단 표준 형식 엑셀 업로드 UI (지점·대상월 선택)
- [ ] 업로드 시 배치(`nhis_import_batches`) 생성 — `PENDING → PROCESSING → COMPLETED`
- [ ] 행별 자동 매칭: 인정번호·이름·생년월일로 ogada 이용자(`client_id`) 연결
- [ ] **엑셀 파서**: 선행 **`처리상태` 열 자동 스킵·헤더 정규화** (케어포 공지 44438 — 컬럼 변동 대응)
- [ ] **(QA-H01)** 선행열 포함 샘플 엑셀 **import 테스트** — `NhisExcelParserTest`에 `처리상태` 선행열·헤더 정규화 케이스 추가, PASS (TEST_REPORT §4 FAIL 해소)
- [ ] **공단 포털 직접 전송 기능 없음** — UI에 「공단 longtermcare에서 전송 후 청구내역상세 엑셀 다운로드」 안내
- [ ] import 안내: **롱텀 2026** — IE 불가, **Chrome/Edge** 사용 권장 (엑셀 export 전제)

### US-G06 — NHIS Reconciliation UI (매칭 보정) ← **신규 (2026-06-06)**

| 항목 | 내용 |
|------|------|
| 역할 | `branch_admin` |
| 스토리 | 센터장으로서, 업로드한 공단 엑셀의 **행별 매칭 상태를 한눈에 보고**, 자동 매칭에 실패한 행을 직접 이용자에 **수동 연결**하고 싶다. 그래야 공단 청구 결과와 ogada 내부 청구가 정확히 대조된다. |
| 우선순위 | Must |
| Pilot | Yes (월말 청구 직후) |
| 근거 | BENCHMARK §5-3 P1 (케어포 4단계 UX), `memory/decisions.md` 2026-06-06 (V19/V21–V27) |

**인수 조건**
- [x] 배치 상세 화면에서 행 목록 표시 — **`NhisReconciliationTable` @ `c5708c7`(UXD-39)** · **필드 fallback Fixed @ `4957bd3`(Q154)**
- [x] **매칭 상태 3종**: `MATCHED`(정상) / `DISCREPANCY`(이용자 OK, 금액·일수 차이) / `UNMATCHED`(자동 매칭 실패) — **`NhisReconciliationTable` StatusBadge·행 강조 @ `fd4e8f3`**
- [x] `DISCREPANCY` 행은 강조 표시 + 차이 컬럼·청구 라인 비교 링크 — **`DiscrepancyComparePanel`·`onCompare` @ `fd4e8f3`** · **`pilotPageFlows` US-G06 E2E @ `c510f5c`**
- [ ] `UNMATCHED` 행은 **후보 이용자 검색·수동 연결** UI — 연결 시 `client_id` 설정과 매칭 상태 전이가 **단일 트랜잭션**(부분 업데이트 금지, `chk_nhis_import_rows_match_requires_client`) — **PARTIAL @ `f01e3a8`(UXD-43)**: `ReconciliationPage` 후보 이용자 검색·선택 UI **HEAD PRESENT** · 매칭 API·트랜잭션 **잔여**
- [ ] 매칭 이용자는 **배치 지점과 동일 지점**만 허용 (`trg_nhis_rows_client_branch`)
- [ ] 매칭 보정 완료 후 청구서와 reconciliation 결과 대조 가능
- [ ] 다른 Tenant 이용자로 연결 불가 (`organization_id` 자동 복사 — V22)

### US-G07 — 청구 상태 관리·필터 (US-G05 통합·확장)

| 항목 | 내용 |
|------|------|
| 역할 | `branch_admin`, `hq_admin` |
| 스토리 | 센터장으로서, 청구서 **작성중 → 확정 → 수납완료** 상태를 관리하고, **상태별로 목록을 필터**하고 싶다. 그래야 월말 마감과 미수금 추적이 수월하다. |
| 우선순위 | Must |
| Pilot | Yes |

**인수 조건**
- [ ] 상태 전이 버튼·이력 (V10/V21 `trg_billing_claims_status_history`)
- [ ] 확정 후 라인·금액 **불변** (V8 트리거) — 상태·`updated_at`만 변경 가능
- [ ] 동일 상태로의 no-op 전이 거부 (V31 `chk_claim_status_history_distinct_transition`)
- [ ] `/billing` 목록에 **상태 필터** 쿼리 파라미터(`?status=DRAFT|CONFIRMED|PAID`) — V31 `idx_billing_claims_org_branch_status_generated` 활용
- [ ] 상태별 카운트 배지 (옵션, 후속)

---

## 10. Epic H — 대시보드

### US-H01 — 지점 대시보드 (파일럿 핵심)

| 항목 | 내용 |
|------|------|
| 역할 | `branch_admin`, `caregiver`(읽기) |
| 스토리 | 직원으로서, 로그인 후 **오늘 지점 출석·이용자 수·건강 이상**을 한 화면에서 보고 싶다. |
| 우선순위 | Must |
| Pilot | **Yes** |

**인수 조건**
- [ ] `/dashboard`: 당일 출석 요약, 이용자 수(입소/퇴소/이용)
- [ ] 건강 이상 이용자 목록
- [ ] 월별 출석률 차트 (간단)
- [ ] 1주차 완료 기준 충족

### US-H02 — 통합 대시보드

| 항목 | 내용 |
|------|------|
| 역할 | `hq_admin` |
| 스토리 | 통합 관리자로서, **2개 지점 출석·이용자를 비교**하고 싶다. |
| 우선순위 | Must |
| Pilot | No |

**인수 조건**
- [ ] `/dashboard/hq`: 지점별 카드/표
- [ ] 지점 필터·기간 필터
- [ ] 전 지점 건강 이상 통합 목록

---

## 11. Epic I — 기타 역할 (MVP 구현, 파일럿 제외)

### US-I01 — 통합 관리자 지점 전환 후 수정

| 항목 | 내용 |
|------|------|
| 역할 | `hq_admin` |
| 스토리 | 통합 관리자로서, `active_branch_id` 선택 후 **해당 지점 데이터만 수정**하고 싶다. |
| 우선순위 | Must |
| Pilot | No |

### US-I02 — 보호자 기록 열람

| 항목 | 내용 |
|------|------|
| 역할 | `guardian` |
| 스토리 | 보호자로서, **연결 이용자의 일일 출석·건강 요약**을 보고 싶다. |
| 우선순위 | Must (포털 최소) |
| Pilot | No |

### US-I03 — 시스템 관리자 설정

| 항목 | 내용 |
|------|------|
| 역할 | `sysadmin` |
| 스토리 | IT 담당으로서, **자기 Tenant 백업·감사 로그**를 관리하고 싶다. |
| 우선순위 | Must |
| Pilot | No |

### US-I04 — 사회복지사 이용자·건강 관리

| 항목 | 내용 |
|------|------|
| 역할 | `social_worker` |
| 스토리 | 사회복지사로서, 이용자 정보와 건강 기록을 **관리(직원관리 제외)**하고 싶다. |
| 우선순위 | Must |
| Pilot | No |

---

## 12. Epic T — 배차·이동경로 (v1.3, G5·**G15·G16·G17**) ← **신규 (2026-06-07, 결정 60·61·62, BNK-7·BNK-8·BNK-9)**

> **v1.3-A**: `hq_admin` 확정 + 직원 조회 + **픽업만** + 최대 15명 — **케어포 이동서비스 지도보기 패리티**(BNK-8, 차별화 아님). **v1.3-B**: TSP·도로 경로(**영업 차별 핵심**). **v1.3-C**: 차량·이동서비스비·법정 서식(G15·G16). 파일럿 1주차 **제외**.

### US-T01 — 배차 픽업 명단 (v1.3-A Must)

| 항목 | 내용 |
|------|------|
| 역할 | `hq_admin` (편집), `caregiver`·`branch_admin` (확정 후 조회) |
| 스토리 | 본사 관리자로서, **배차 이용자만** 골라 당일 **픽업** 명단을 만들고 싶다. |
| 우선순위 | **v1.3-A Must** |
| Pilot | No |

**인수 조건**
- [ ] 이용자 프로필 `uses_transport`·픽업 주소(미입력 시 거주지)
- [x] `/transport` — 지점·날짜·**픽업** 명단 (`direction=PICKUP` 고정) — **@ `53a1ffe`/`e8d1854`+**: `TransportPage`·`GET /transport/roster`·`TransportDisclaimer` **HEAD PRESENT**
- [x] UI에 **「운영 편의용 — 이동서비스비·평가 일지 미포함」** + **「케어포 지도보기 패리티 — 경로 최적화는 v1.3-B」** 안내 (G15 오해 방지, BNK-7·BNK-8) — **`TransportDisclaimer` @ `e8d1854`**
- [ ] 퇴소·비활성 제외, 주소·연락처 마스킹
- [x] 선택 인원 **최대 15명** — 초과 시 UI·API 거부 (결정 62) — **`MAX_STOPS=15` @ `53a1ffe`** + UI `MAX_TRANSPORT_STOPS=15`

### US-T02 — 배차 루트 편집·확정 (`hq_admin`)

| 항목 | 내용 |
|------|------|
| 역할 | `hq_admin` |
| 스토리 | 본사 관리자로서, 픽업 대상을 고르고 **순서를 정한 뒤 배차를 확정**하고 싶다. |
| 우선순위 | **v1.3-A Must** |
| Pilot | No |

**인수 조건 — v1.3-A**
- [x] 다중 선택 → `transport_run`(`DRAFT`) 생성 — **@ `53a1ffe`**: `POST /transport/runs`·`TransportRunNewPage` **HEAD PRESENT**
- [ ] 정차 **수동 드래그** (TSP 제외), **≤15명** — **UI 드래그·15명 상한 @ `e8d1854`**
- [ ] 지도: 센터·**순번 마커**·**직선 폴리라인** — **`KakaoTransportMap` @ `e8d1854`**
- [ ] Geocoding 실패 주소 경고
- [x] 「**배차 확정**」→ `CONFIRMED` — 이후 순서·인원 **수정 불가** — **`POST /transport/runs/{id}/confirm` @ `53a1ffe`** + `TransportRunDetailPage`
- [ ] `confirmed_at`·`confirmed_by` 기록
- [x] 「**확정 취소(unconfirm)**」→ `CONFIRMED`→`DRAFT` 복귀 — `hq_admin` 전용 — **`PATCH /api/v1/transport/runs/{id}/unconfirm` @ backend `0d8968d`** — **frontend UI 잔여**

**인수 조건 — v1.3-B (후속, BNK-9)**
- [ ] TSP 자동 순서 + **카카오 Directions 다중 경유지 API** 도로 경로·거리/시간 (일 5,000건 무료·16원/건)

### US-T03 — 확정 배차 조회 (직원, v1.3-A Must)

| 항목 | 내용 |
|------|------|
| 역할 | `caregiver`, `social_worker`, `branch_admin` |
| 스토리 | 요양보호사로서, **확정된 픽업 배차**의 **명단·순서·지도**를 모바일에서 확인하고 싶다. |
| 우선순위 | **v1.3-A Must** |
| Pilot | No |

**인수 조건**
- [x] `CONFIRMED` 루트만 목록·상세 노출 (`DRAFT` 403/숨김) — **@ `53a1ffe`**: RBAC·`TransportPage` 역할별 필터 **HEAD PRESENT** · live E2E **잔여**
- [ ] 정차 명단(순번·이름·주소 마스킹)·지도 **읽기 전용**
- [ ] 반응형·터치 44px (WCAG)
- [ ] 픽업 완료 체크·출석 연동 — **v1.3-B 이후**

### US-T04 — 드롭(DROPOFF) 배차 (후속)

| 항목 | 내용 |
|------|------|
| 역할 | `hq_admin` |
| 스토리 | 본사 관리자로서, 오후 **귀가 드롭** 배차도 픽업과 같이 운영하고 싶다. |
| 우선순위 | **v1.3-A.1 Should** |
| Pilot | No |

**인수 조건**
- [ ] `direction=DROPOFF` run·명단·확정·조회 (US-T01~T03 패턴 동일)

### US-T05 — 차량·이동서비스비·법정 서식 (v1.3-C, G15·G16)

| 항목 | 내용 |
|------|------|
| 역할 | `hq_admin`, `branch_admin` |
| 스토리 | 센터장으로서, **차량을 등록**하고 이동서비스 **운행일지·이동서비스비**를 공단 서식에 맞게 관리하고 싶다. |
| 우선순위 | **v1.3-C Could** |
| Pilot | No |

**인수 조건**
- [ ] `vehicles` CRUD — 차량번호·정원·지점 스코프 (G16)
- [ ] `transport_runs`에 차량 배정·운행일지 **별지 제22호** export (G15)
- [ ] **별지 제18호** 신청 전제 안내(공단 포털)
- [ ] 급여제공기록지 **이동서비스 제공·차량번호** 연계 (G15)
- [ ] **이동서비스비** 산정·청구 입력 — 고시 제34조 (G16, 케어포 2-5 패리티)
- [ ] **`transport_service_fee` 테이블** — 러-1~4 **830/2,630/4,440/6,240원** 시드(BNK-9) · law.go.kr 1차 확인 전 **하드코딩 금지**

### US-T06 — 2026 평가 #27 기능회복훈련 (G17, v2+ Could)

| 항목 | 내용 |
|------|------|
| 역할 | `social_worker`, `branch_admin` |
| 스토리 | 사회복지사로서, **기능회복훈련** 급여계획·실시 기록을 공단 평가 #27(3점)에 맞게 관리하고 싶다. |
| 우선순위 | **Could v2+** (BNK-9 — 케어포·이지케어 반영, ogada **Won't v1**) |
| Pilot | No |

**인수 조건**
- [ ] 급여계획 포함·연 1회 실시 기록 UI (경쟁사 UI 흐름 벤치마크 후 상세화)
- [ ] v1.3·v1.2 범위 **미포함** — ROADMAP Won't v1

---

## 13. Epic J — 보호자 초대·명세 (v1.1, G8) ← **신규 (2026-06-06, 3차 벤치마크)**

> 이지케어 EZCARE·케어포 가족돌봄앱 **최소 패리티**. v1 백엔드 API 선행, **프론트 MVP(v1.1)** 에서 E2E.

### US-J01 — 보호자 초대·온보딩

| 항목 | 내용 |
|------|------|
| 역할 | `branch_admin`, `hq_admin` (초대) / `guardian` (수락) |
| 스토리 | 센터장으로서, **보호자에게 앱/웹 포털 초대**를 보내 연결 이용자를 등록하고 싶다. (이지케어 EZCARE — 기관 초대 후 이용 패턴) |
| 우선순위 | Should → **v1.1 Must** (G8) |
| Pilot | No (v1.1) |
| 근거 | BENCHMARK §5-2 G8, `memory/decisions.md` 2026-06-06 3차 #3 |

**인수 조건**
- [ ] 이용자 프로필에서 보호자 **이메일** 입력 → **이메일 초대 링크 발송** (`channel: EMAIL` 단일 — 결정 59)
- [ ] 보호자가 초대 수락 시 `guardian` 계정 생성·`guardian_clients` 연결
- [ ] 초대 만료·재발송 UI *(develop `cc34f23` — `GuardianInviteModal.test.jsx` invite/expire/resend/scope 4건 회귀 자동화 PARTIAL; 라이브 동작은 백엔드 API 구현 후)*
- [x] **초대 목록 UI** *(44차 — FE-18 Fixed @ `f506c90` — `GuardianInvitationList`(+test)·`GuardianPortalPage`·`PaymentRecordModal` HEAD PRESENT)*
- [x] **`ClientDetailPage` 보호자/초대 연동** *(45차 — COD `7170b2a` — `ClientDetailPage.test.jsx` J01 fetch-mock 회귀 PASS)*
- [x] **백엔드 초대 API** *(BE-8 Fixed @ `f47ffa1`·backend lineage `136239e` — `GuardianInvitationController`·V43 HEAD PRESENT)*
- [ ] **live API E2E** — guardian 초대·수락·명세 **live backend** 연동 검증 *(post-merge·권장 — **결정 73 merge 게이트 제외**)* 
- [ ] Tenant·지점 스코프 격리 — 타 센터 초대 불가

> **48차 갱신 — 결정 73**: live E2E run **merge 선행 조건 아님** · merge 후 post-merge 권장.

### US-J02 — 보호자 명세·청구서 모바일 열람

| 항목 | 내용 |
|------|------|
| 역할 | `guardian` |
| 스토리 | 보호자로서, **연결 이용자의 본인부담금 명세·청구서**를 모바일에서 조회하고 싶다. (케어포 가족돌봄앱·EZCARE 명세 탭) |
| 우선순위 | Should → **v1.1 Must** (G8) |
| Pilot | No (v1.1) |

**인수 조건**
- [ ] `/guardian` **명세·청구 탭** — 월별 본인부담금 명세 목록·상세(PDF/인쇄)
- [ ] 연결 이용자 복수 시 이용자 선택 후 조회
- [ ] CMS·결제·알림톡 발송 **제외** (v2)
- [ ] US-I02(일일 기록 열람)와 동일 포털 내 탭 통합

### US-J03 — 카카오톡 채널 보호자 알림 (v2, G1)

| 항목 | 내용 |
|------|------|
| 역할 | 시스템(`NotificationService`) / `branch_admin`(발송 정책) / `guardian`(수신) |
| 스토리 | 보호자로서, **앱을 열지 않아도** 출석·일일 케어·명세·긴급 소식을 **카카오톡 알림톡**으로 받고 싶다. (케어포·이지케어 문자/알림 패리티) |
| 우선순위 | Should → **v2 Must** (G1) |
| Pilot | No (v2) |
| 선행 | v1.1 무료 채널(인앱·FCM) 골격, `guardian_clients` 연결 완료 |
| **52차 follow-up (TSR 70 @ `78e8928`)** | `HealthRecordService` — **투약(medication) 기록 생성 시 DAILY_CARE alimtalk dispatch** · `HealthRecordServiceTest` 단위 테스트 |
| **53차 follow-up (TSR 72 @ `c53dd3b`)** | `GuardianNotificationHistoryController`·`StaffClientNotificationHistoryController`·`NotificationHistoryService`(+test) — **알림 이력 조회 API** · 템플릿 심사·발송 UI·프론트 연동 **잔여** |
| **56차 follow-up (TSR 76 @ `0832fbf`)** | `HealthRecordService` — **활력징후(vitals) 기록 생성 시 DAILY_CARE alimtalk dispatch** · `HealthRecordServiceTest`(+53 lines) · 템플릿 심사·발송 UI·프론트 연동 **잔여** |
| **57차 follow-up (TSR 78 @ `32a1f8f`)** | **`J03AlimtalkServiceFlowE2eTest`** — attendance·health·billing 도메인 액션을 `NotificationService` 경유 service-layer alimtalk flow E2E 5건 · `AttendanceServiceTest` check-out dispatch · 템플릿 심사·발송 UI·프론트 연동 **잔여** |
| **59차 follow-up (TSR 80 @ `ac17ad8`)** | **`AlimtalkFallbackText`** — 알림톡 실패 시 **한국어 SMS relay 본문** 생성 · `incidentType`→`category` alias · `AlimtalkFallbackTextTest` · live Solapi·프론트 연동 **잔여** |
| **60차 follow-up (TSR 82 @ `52e0621`)** | copay claim **CONFIRMED→PAID** 전환 시 **`BILLING_PAYMENT_RECEIVED`** alimtalk dispatch · `notifyBilling` consent 재사용 · `BillingServiceTest`·`J03AlimtalkServiceFlowE2eTest` 확장 · live Solapi·프론트 연동 **잔여** |

**인수 조건**
- [ ] 센터(Tenant) **카카오 비즈니스 채널** 연동 설정 (채널 ID·발신 프로필·중계 API 키)
- [ ] 알림톡 **템플릿 사전 심사** — 출석(도착/귀가), 일일 케어 요약, 명세 등록, 긴급(낙상 등) 최소 4종
- [ ] 발송 대상: 이용자에 연결된 보호자(`guardian_clients`) — **대표 보호자 우선**, 복수 시 정책 확정
- [x] 알림톡 실패 시 SMS fallback — **`AlimtalkFallbackText`·`SolapiSmsProvider` @ `ac17ad8`** (한국어 relay 본문, 내부 templateCode·UUID 미노출)
- [ ] 보호자 **수신 동의**·야간 발송 제한·발송 이력 `notifications` 테이블 기록
- [ ] v1.1 무료 채널(FCM·인앱)과 **병행** — 앱 사용자는 푸시, 미가입자는 알림톡

---

## 12a. Epic UX — 네비게이션·브랜드 (v1.1~v1.2)

### US-UX-01 — 파비콘·앱 아이콘 (v1.1 Must)

| 항목 | 내용 |
|------|------|
| 역할 | 전 사용자 |
| 스토리 | 사용자로서, 브라우저 탭·북마크·모바일 홈추가에서 **ogada를 식별**할 수 있는 아이콘을 보고 싶다. |
| 우선순위 | Must (v1.1) |
| 상태 | develop `998ac87` 반영 |

**인수 조건**
- [x] `public/favicon.svg`·`favicon.ico`·`apple-touch-icon.png`, `index.html` link·theme-color

### US-UX-02 — 2단 SideNav 그룹화 (v1.2 P0)

| 항목 | 내용 |
|------|------|
| 역할 | `hq_admin`, `branch_admin` |
| 스토리 | 센터장으로서, 케어포처럼 **청구·출석·기록·이용자**를 그룹별 하위 메뉴로 탐색하고 싶다. |
| 우선순위 | **v1.2 P0** (BNK-6, 결정 49) |
| 근거 | `COMPETITOR_MATRIX §8-4` — ogada 1단 flat vs 케어포 2~3단 |
| 상태 | **진전** — UXD **`0d83a42`** @ develop `9bdf59f`(TSR 71·73): **15 missing pages** · P0 E2E·module coverage KPI @ `9bdf59f` · **33 route** · **≥60% KPI PASS** · 2단 depth **잔여** |

**인수 조건**
- [ ] `SideNav.jsx` **2단 depth** — 최소 4그룹(운영·출석·기록·청구) + 하위 route
- [ ] 역할별(`hq_admin` 12→4~5그룹) 메뉴 노출 — flat 12항목 대비 정보밀도↑
- [ ] 모바일 반응형 — 접힘/펼침 유지

### US-UX-03 — 전사 설정 Switch·셀프 체크인 토글 (v1.1) ← **신규 (2026-06-06, 20차 — UXD 13차 `07fd305`)**

| 항목 | 내용 |
|------|------|
| 역할 | `hq_admin`, `branch_admin`, `sysadmin` |
| 스토리 | 관리자로서, **이용자 본인(`client_user`) QR 셀프 체크인 허용** 같은 전사·지점 정책을 한 화면에서 직관적인 토글로 켜고 끄고 싶다. |
| 우선순위 | **v1.1** (Should — 결정 16 안 3 UI 정착) |
| 근거 | 결정 16(`allow_client_self_checkin` Organization 설정 on/off), DESIGN_SYSTEM §1 컴포넌트·§9 접근성, UXD 13차 `07fd305` |
| 상태 | develop `07fd305` 반영 (UXD 13차 — 7 files +218/-7) |

**인수 조건**
- [x] `Switch.jsx` WAI-ARIA — `role="switch"` + `aria-checked` 상태 노출
- [x] **44px 최소 hit target** + 키보드 포커스(`Tab`/`Space`/`Enter`)
- [x] `forced-colors` 미디어 쿼리 — 강제 색 모드 (Windows High Contrast 등) 대비 시각 보존
- [x] `SettingsPage.jsx` `allow_client_self_checkin` 토글 컨트롤(전사) — `OrganizationSettingsRepository` 1행 갱신 API 연동 골격
- [x] `Switch.test.jsx` 5건 회귀 (ARIA·키보드·on/off·focus·disabled)
- [ ] 라이브 backend 연동 검증 (v1.1 develop→test merge 후 — B03 ready 동반)

> **결정 52 흡수**: UXD 13차 `07fd305`는 v1.1 develop→test merge에 동반 흡수 — `Switch.jsx`·`Switch.test.jsx`·`SettingsPage.jsx`·`tokens.css` 등 7 files. DESIGN_SYSTEM §1 컴포넌트 라이브러리 확장(향후 `Toggle`·`Checkbox`와 함께 boolean 컨트롤 표준화).

---

## 12b. Epic K — 보호자 관리 (v1.2 P0, BNK-6)

> 케어포 1-3 보호자관리. v1은 `createClient` `primaryGuardian`만 — **전용 CRUD·연결 화면**은 v1.2.

### US-K01 — 보호자 목록·검색

| 항목 | 내용 |
|------|------|
| 역할 | `branch_admin`, `hq_admin`, `social_worker` |
| 스토리 | 센터장으로서, **지점 소속 보호자를 목록·검색**하고 연결 이용자 수를 한눈에 보고 싶다. |
| 우선순위 | **v1.2 P0** |
| 근거 | `guardian_clients`(V7·V23·V39), BENCHMARK §9-3 #1 |
| **53차 진전 (TSR 73 @ `9bdf59f`)** | P0 CRUD E2E·보호자 초대/수정 UI — Epic K **WIP** |

**인수 조건**
- [ ] `/guardians` 목록 — 이름·연락처(마스킹)·연결 이용자 수·대표 여부
- [ ] 지점 스코프·Tenant 격리
- [ ] 이용자 상세에서만이 아닌 **독립 메뉴** 진입

### US-K02 — 보호자–이용자 연결 관리

| 항목 | 내용 |
|------|------|
| 역할 | `branch_admin`, `social_worker` |
| 스토리 | 사회복지사로서, **기존 보호자와 이용자 연결·해제·대표 보호자 지정**을 전용 UI에서 하고 싶다. |
| 우선순위 | **v1.2 P0** |

**인수 조건**
- [ ] 보호자 상세 — 연결 이용자 목록·`is_primary` 토글
- [ ] 이용자 없이 보호자만 등록 후 연결 추가 가능
- [ ] US-D01(대표 보호자 1명 이상) 정책 유지

---

## 12c. Epic L — 본인부담 수납 (v1.2 P0, G13)

> 케어포 7-2 입금·7-3 미납. MVP는 청구·명세(7-1)만 — **수납 lifecycle**은 v1.2 P0.

### US-L01 — 본인부담 입금 처리

| 항목 | 내용 |
|------|------|
| 역할 | `branch_admin`, `hq_admin` |
| 스토리 | 센터장으로서, **확정된 본인부담 청구에 입금을 기록**하고 수납 상태를 갱신하고 싶다. |
| 우선순위 | **v1.2 P0** (G13) |
| 근거 | `billing_claims`·`billing_claim_items`, COMPETITOR_MATRIX §8-1 7-2 |
| **53차 진전 (TSR 73 @ `9bdf59f`)** | `PaymentRecordModal`(+test) — 입금 모달 UI·P0 E2E **WIP** |

**인수 조건**
- [ ] `/billing/payments` 또는 `/billing/claims?status=CONFIRMED` — 입금일·금액·수단(현금/계좌) 입력
- [ ] `billing_claims` 상태 `PAID`(또는 부분입금) 전이
- [ ] CMS·간편결제 **제외** (v2)

### US-L02 — 미납 관리·독려 목록

| 항목 | 내용 |
|------|------|
| 역할 | `branch_admin` |
| 스토리 | 센터장으로서, **미납 본인부담금 목록**을 보고 독려 대상을 파악하고 싶다. |
| 우선순위 | **v1.2 P0** (G13) |

**인수 조건**
- [ ] `/billing/overdue` — 기한 경과·미수금액·이용자·보호자 연락처(마스킹)
- [ ] 대시보드 미처리 위젯(US-M02)과 연동
- [ ] 알림톡·SMS 발송 **제외** (v2)

---

## 12d. Epic M — 등급·대시보드 실데이터 (v1.2 P0, G14)

### US-M01 — 등급 변동 이력

| 항목 | 내용 |
|------|------|
| 역할 | `branch_admin`, `social_worker`, `hq_admin` |
| 스토리 | 센터장으로서, 이용자 **등급 상·하향 이력**을 타임라인으로 추적하고 싶다. (케어포 1-9) |
| 우선순위 | **v1.2 P0** (G14) |

**인수 조건**
- [ ] 이용자 상세 **등급 이력 탭** — 변경일·이전/이후 등급·변경 사유(선택)
- [ ] `ltc_grade_history` (또는 동등) 테이블 — 등록·수정 시 이력 append
- [ ] 기존 `clients.ltc_grade` 단일값과 정합

### US-M02 — 대시보드 실데이터 위젯

| 항목 | 내용 |
|------|------|
| 역할 | `branch_admin`, `hq_admin`, `caregiver` |
| 스토리 | 센터장으로서, 케어포처럼 **오늘 출석·미처리 업무·공지**를 실데이터로 대시보드에서 보고 싶다. |
| 우선순위 | **v1.2 P0** (BNK-6-4) |

**인수 조건**
- [ ] StatCard 데모 제거 — `/api/v1/dashboard/*` 집계 API 연동
- [ ] 위젯 최소 3블록: **오늘 출석/결석**, **미납·미매칭 NHIS**, **건강 알림**(또는 공지)
- [ ] HQ `/dashboard/hq` — 지점별 비교 차트(Recharts, UXD-1)

> **52차 진전 (2026-06-08, planner 52차 — UXD 15 pages @ `0d83a42` + P0 KPI @ `42f48e1`)**: **18→33 route·33 page** — US-D01·E03-E05·F04·G01-G07·H01-H04·B01·A01 화면 **develop 커밋** · P0 page-flow tests·module coverage KPI · WT **CLEAN** · **`npm test` 89/28 PASS** · build **114 modules** · develop **4 ahead** of test. → **모듈 커버 ~45–50% 추정** · 결정 49 **≥60% 잔여** · P0 E2E·SideNav 2단 depth **잔여**.
> **51차 진전 (2026-06-08, planner 51차 — UXD 35 develop 커밋 @ `64468a3`/`e0eaf32`)**: 50차 **24 files WIP → develop 커밋** — `DashboardWidgetGrid`(+test)·`FileUpload`(+test)·`GuardianInviteModal`·`NhisImportGuidePanel`·`MaskedRevealField` + Must 페이지 6종 DS integration · **`e0eaf32`** `/guardians` RBAC·page-flow 회귀. WT **CLEAN** · **`npm test` 82/27 PASS** · develop **2 ahead** of test `4f71543`(v1.1 merged). → **FE-12·FE-13 lineage 진전** · #36 FE-6 dirty-tree **해소** · ≥60% KPI·P0 E2E **잔여**.

> **50차 진전 WIP (2026-06-08, planner 50차 — frontend dirty-tree 재확대 @ `4f71543`)**: 49차 1M → **24 files** WIP — Must 페이지 6종 modified(`AttendancePage`·`BillingPage`·`ClientDetailPage`·`HealthPage`·`NHISImportPage`·`DashboardPage`) + 공통 UI **`DashboardWidgetGrid`(+test)·`FileUpload`(+test)·`GuardianInviteModal`·`HealthAbnormalBanner`·`NhisImportGuidePanel`·`MaskedRevealField`** + `components.css`·`services.js`·`index.js`. **HEAD `4f71543` Fixed(FE-22·UXD SideNav) 규율 5 유효** — recurrence는 미커밋 v1.2/Must UI cluster 단일. develop=test merged · frontend merge gap **0**. → **FE-12·FE-13 lineage WIP**·#36 FE-6 recurrence 관측(HEAD Fixed 유효).

> **55차 Planned (2026-06-07, TSR 55차 — B07 recurrence #6·FE-18)**: 53차 `d5654c0` CLEAN 직후 **15 files** WIP — `DateInput`+test(DS)·`GuardianInvitationList`+test(J01 **초대 목록** UI)·`ClientDetailPage`(+98 보호자/초대 연동)·`GuardianInviteModal`·`GuardianListCard`·`LoginHistoryPanel`·`AuditLogPanel`·`ClientPhotoField`·`services.js`·`GuardianInvitationAcceptPage`+test·`components.css`. **HEAD `d5654c0` Fixed(FE-17) 규율 5 유효**. WT `npm test` **205/42 PASS**·build **758 modules**·audit **0**. → **FE-18 Planned**·#36 FE-6 #5 재오픈. 백엔드 J01 초대/목록 API(#33) 연동 전 fetch-mock/스텁.

> **53차 Fixed (2026-06-07, TSR 53차 — B07 recurrence #5 정식 Fixed `d5654c0`·FE-17)**: 52차 20 files WIP → COD 35차 `d5654c0`(25 files +823/-57, **18 ahead**) 일괄 커밋, working tree **20→0 CLEAN**. 산출물: `GuardianInvitationAcceptPage`(+test, J01 수락 프론트 `/guardian/invitations/:token/accept`)·`GuardianInvitationAcceptForm`·`PublicAuthLayout`·`LogoutButton`(+test, AppShell)·`BillingPage.layout.test`·`acceptGuardianInvitationApi`·AuthContext logout best-effort·Recharts·청구/보호자 페이지. **TSR 독립 검증 PASS** — `git status` 0줄·`git cat-file -e HEAD:` 산출물 PRESENT·SEC-005 0건. HEAD `npm test` **199/40 PASS**·build **756 modules**·audit **0**. → **FE-17 @HEAD 충족**·잔여 frontend BLOCK = **B03 merge 게이트 단일**(develop→test 18커밋 미머지). 결정 52 흡수 ⑪묶음.

> **45차 진전 WIP (2026-06-07, TSR 45차 — B07 #3 Planned 범위 확대)**: 43차 72 files → **76 files**(40M+36U) — 신규 **`FeeScheduleTable`(+test, 수가표 목록·등급×연도 테이블·US-G00a·케어포 9-x 수가설정·HEAD `FeeRateHistoryPanel` 이력 UI 연계)** + 기존 Recharts·청구·copay·건강·NHIS·설정 WIP. WT `npm run build` **749 modules PASS**(+1)·`npm test` **181/30 PASS**(+2/+1)·audit **0건**(FE-7). develop HEAD 미커밋(FE-6 #3).

> **43차 진전 WIP (2026-06-07, TSR 43차 — B07 #3 Planned 범위 확대)**: 41차 61 files → **72 files**(38M+34U) — 신규 **`BillingStatusConfirmModal`(+test, 청구 상태 확인·US-G06)·`CopayRateTable`(+test, 본인부담률·Epic G)·`GuardianDailySummary`(+test, 보호자 일일 요약·Epic J/K)·`HealthAlertList`(+test, 건강 알림·US-M02)·`NhisImportGuidePanel`(+test, NHIS import 가이드·결정 37)** + 기존 Recharts·Platform·운영/보안·계정 보안 WIP. WT `npm run build` **748 modules PASS**(+5)·`npm test` **179/29 PASS**(+10/+5)·audit **0건**(FE-7). develop HEAD 미커밋(FE-6 #3).

> **41차 진전 WIP (2026-06-07, TSR 41차 — B07 #3 Planned, 상태 불변 ±1 modified)**: 39차 60 files → **61 files**(37M+24U, ±1 modified) — FE-12·FE-13·FE-14 WIP 동일 범위. WT `npm run build` **743 modules PASS**·`npm test` **169/24 PASS**·audit **0건**(FE-7). develop HEAD 미커밋(FE-6 #3) — **FE-12·FE-13·FE-14**·v1.2 P0·BNK-6 운영/보안·계정 보안 모듈 패리티(§3-1 인증 매핑).

> **39차 진전 WIP (2026-06-07, TSR 39차 — B07 #3 Planned 범위 확대)**: 37차 44 files → **60 files**(36M+24U) — Recharts·Platform·배치·운영/보안 설정 + 신규 **계정 보안·로그인 이력 UI** `LoginHistoryPanel`(+test, §3-1 로그인 이력 조회)·`PasswordChangeModal`(+test, §3-1 비밀번호 재설정 — COD 03:08 SettingsPage 보안 탭 연결)·`PasswordResetRequestModal`(+test, §3-1)·`PlatformOrgDetailModal`(+test, US-A01 Tenant 상세)·`SettingsPage.test.jsx`·`HealthTrendChart.test.jsx`(FE-12 회귀 강화). WT `npm run build` **743 modules PASS**·`npm test` **169/24 PASS**·audit **0건**(FE-7). develop HEAD 미커밋(FE-6 #3) — **FE-12·FE-13·FE-14**·v1.2 P0·BNK-6 운영/보안·계정 보안 모듈 패리티(§3-1 인증 매핑).

> **37차 진전 WIP (2026-06-07, TSR 37차 — B07 #3 Planned 범위 확대)**: 35차 26 files → **44 files**(26M+18U) — Recharts·Platform·배치 레이어 + 신규 운영/보안 설정 UI `AuditLogPanel`(+test)·`BackupSettingsPanel`(+test)·`PasswordChangeModal`(+test)·`FilterChips.test`. WT `npm run build` **741 modules PASS**·`npm test` **161/20 PASS**·audit **0건**(FE-7). develop HEAD 미커밋(FE-6 #3) — **FE-12·FE-13·FE-14**·v1.2 P0·BNK-6 운영/보안 모듈 패리티.

> **35차 진전 WIP (2026-06-07, TSR 35차 — B07 #3 Planned 범위 확대)**: 33차 18 files → **26 files** — Recharts 레이어 + `BatchProgressSteps`(+test)·`PlatformOrgDetailModal`·Platform/NHIS/Reconciliation/Forbidden 페이지 WIP. WT `npm run build` **738 modules PASS**·`npm test` **144/13 PASS**·audit **0건**(FE-7). develop HEAD 미커밋(FE-6 #3) — **FE-12·FE-13**·v1.2 P0·BNK-6 HQ/플랫폼 패리티.

> **33차 진전 WIP (2026-06-07, TSR 33차 — B07 #3 Planned)**: 31차 CLEAN(`3fdc266`) 이후 working tree **18 files** Recharts 차트 레이어 WIP — `recharts ^2.15.4`·`ChartContainer`·`AttendanceRateChart`·`BranchCompareChart`·`HealthTrendChart`·`ChartContainer.test.jsx` + Dashboard·HealthDetail·AttendanceStats 페이지 연동. WT `npm run build` **736 modules PASS**·`npm test` **142/12 PASS**·audit **0건**(FE-7). develop HEAD 미커밋(FE-6 #3) — **FE-12**·v1.2 P0 범위. UXD 14차 `chartColors.js` 토큰과 연계.

> **18차 진전 Fixed (2026-06-06, COD 17차 `a84473f` 일괄 커밋)**: 17차 WIP 8 files → COD 17차 `a84473f feat(v1.2-p0): 대시보드 실데이터 위젯·Must 페이지 API 보강 (US-M02)`(8 files +636/-170)로 develop HEAD 일괄 커밋. 산출물: `src/pages/dashboardWidgets.js` 위젯 집계 로직(오늘 출석/결석·미납·미매칭 NHIS 등 3블록) + `dashboardWidgets.test.js`(3 tests PASS) + `DashboardPage.jsx` branch/HQ API 연동 + `AttendancePage`·`ClientFormPage`·`GuardiansPage`·`GuardianListCard`·`services.js` 보강. develop CLEAN·HEAD `npm run build` **111 modules PASS**(vite 6.4.3)·`npm test` **13/5 PASS** — TSR 25차 독립 검증, 이관 규율 5·6·7 PASS, FE-7 회귀 없음. **인수 조건 첫 2항 [x] 부분 충족**(StatCard 데모 제거·API 연동·위젯 3블록 진전). 결정 52에 따라 v1.1 develop→test merge에 동반 흡수, **정식 E2E·HQ 비교 차트(Recharts UXD-1)는 v1.1 merged 후 v1.2 사이클**.

---

## 12e. Epic N — 식사·프로그램 (v3, G5-b) ← **신규 (2026-06-08, 61차 — BNK-6·케어포 3·5장)**

> **v3 §3-5·§3-6 develop 완료 @ `dfd9be2`/`362dbf0`**: backend V49·REST·frontend UI·a11y·`pilotPageFlows` E2E — **프로그램 사진 업로드**·직원·평가 **후속**.

### US-N01 — 당일 식단·식사량 기록 (§3-5 Should)

| 항목 | 내용 |
|------|------|
| 역할 | `branch_admin`, `social_worker`, `caregiver`, `hq_admin` |
| 스토리 | 요양보호사로서, **당일 식단과 이용자별 식사량·식이 제한**을 기록하고 싶다. |
| 우선순위 | **v3 Should** (케어포 3-1 식사 리포트 패리티 — BNK-6) |
| Pilot | No |

**인수 조건**
- [x] `/meals` — 당일 식단·이용자 식사량·식이 제한·영양사 소견 UI — **`7ef1083`+ lineage**: `MealsPage`·`MealRecordForm`·`services.js` **HEAD PRESENT**
- [x] `GET/POST /api/v1/meals/*` backend 연동 — **PRESENT @ `dfd9be2`**: V49·`MealController`·routing test
- [x] 식단 등록·이용자별 기록 E2E — **PRESENT @ `362dbf0`**: `pilotPageFlows`·`pilotChecklist` N01

### US-N02 — 프로그램 일정·참여·만족도 (§3-6 Should)

| 항목 | 내용 |
|------|------|
| 역할 | `branch_admin`, `social_worker`, `caregiver`, `hq_admin` |
| 스토리 | 사회복지사로서, **당일 프로그램 일정·참여·만족도**를 기록하고 싶다. |
| 우선순위 | **v3 Should** (케어포 5-1 프로그램 일지 — BNK-6) |
| Pilot | No |

**인수 조건**
- [x] `/programs` — 당일 일정·참여·만족도 UI — **`7ef1083`+ lineage**: `ProgramsPage`·Vitest **HEAD PRESENT**
- [x] `GET/POST /api/v1/programs/*` backend 연동 — **PRESENT @ `dfd9be2`**: V49·`ProgramController`·routing test
- [x] 프로그램 일정·참여 E2E — **PRESENT @ `362dbf0`**: `pilotPageFlows`·`pilotChecklist` N02
- [ ] 프로그램 사진 업로드 — **후속**

---

## 14. 파일럿 검증 체크리스트

### 13-1. 1주차 우선 3시나리오 (planner 확정: 2026-06-07, 결정 57)

> 파일럿 참여 역할·일일 운영 루프 기준. **2주차+**: P4(지점 B)·P5(대시보드)·P6–P8(청구·NHIS).

| 우선 | # | 시나리오 | 담당 | 스토리 |
|------|---|----------|------|--------|
| **1** | P1 | 지점 A 이용자 등록 + 대표 보호자 연결 | 센터장 | US-D01 |
| **2** | P2 | 지점 A 아침 수기 체크인 ~10명 | 요양보호사 | US-E01 |
| **3** | P3 | 건강·투약 기록 입력 | 요양보호사 | US-F01, F02 |

### 13-2. 전체 체크리스트 (P1–P8)

| # | 시나리오 | 담당 | 완료 기준 |
|---|----------|------|----------|
| P1 | 지점 A에서 이용자 등록 | 센터장 | US-D01 |
| P2 | 지점 A 아침 수기 체크인 10명 | 요양보호사 | US-E01 |
| P3 | 건강·투약 기록 입력 | 요양보호사 | US-F01, F02 |
| P4 | 지점 B로 전환 후 동일 작업 | 센터장·요양보호사 | US-B02, C01 |
| P5 | 지점별 대시보드 수치 확인 | 센터장 | US-H01 |
| P6 | 월말 청구서 생성 | 센터장 | US-G02, G03 |
| P7 | 공단 엑셀 import | 센터장 | US-G04 |
| P8 | NHIS reconciliation 행 매칭·수동 보정 | 센터장 | US-G06 |

> **단위 자동화 PARTIAL 진전 (2026-06-07, TSR 30·31·32·33·34·35차)**:  
> ① **backend** `PilotChecklistApiAccessTest`(`c3f3146`, 29 @Test) — P1–P8 × 7역할 `@PreAuthorize` `@WebMvcTest` 자동 검증. **`SevenRoleJwtLoginE2eTest.java`**(`e8750d2`, COD 21차, 16+ @Test) — live 7역할 JWT 로그인 E2E Fixed(B02 #4). **`PilotChecklistJwtE2eTest.java`**(634 lines, **22 @Test**, P1–P8 live Bearer JWT filter-chain E2E) — **develop HEAD ABSENT**, untracked WIP only(B02 #5 Planned, planner 22차 false `[x]` 철회). develop HEAD `@Test` **199**·WT **225**(+v2 `notification_preferences` WIP, B08 Planned).  
> ② **frontend** `pilotChecklist.js/.test.js`(211/104) — P1–P8 services.js 경로·JWT·HTTP fetch-mock 계약 사전.  
> ③ **frontend 7역할 매트릭스 단위 E2E**(COD 20차 `57ff3c0` 4 files +316).  
> ④ **frontend P1–P8 페이지 단위 E2E**(COD 22차 `3fdc266`): `pilotPageFlows.test.jsx`(433 lines). WT `npm test` **144/13 PASS**(+Recharts·Platform WIP), build **738 modules**.  
> ⑤ **라이ve E2E 잔여** — `PilotChecklistJwtE2eTest` develop commit + v1 merged 후 실 JWT·실 DB 통합은 파일럿 센터에서 검증.

---

## 15. 스토리 ↔ 요구사항 매핑

| Epic | REQUIREMENTS | 스토리 수 |
|------|------------|----------|
| A | §1-3, §3-12 | 2 |
| B | §3-1, §2-3 | 3 |
| C | §3-12 | 2 |
| D | §3-2, §3-2-1 | 4 |
| E | §3-3 | 5 |
| F | §3-4 | 4 |
| G | §3-9 (수가표·본인부담·**reconciliation** 포함), §1-5 | **8** (G00a·G00b·G01–G07) |
| H | §3-11 | 2 |
| I | §2-4 | 4 |
| J | §3-7 (G8·G1) | **3** (v1.1: J01·J02, v2: J03) |
| K | §3-7, §1-5-2 | **2** (v1.2 P0: 보호자 관리) |
| L | §3-9, G13 | **2** (v1.2 P0: 입금·미납) |
| M | §3-2, §3-11, G14 | **2** (v1.2 P0: 등급이력·대시보드) |
| UX | DESIGN_SYSTEM §1·§9 | **3** (v1.1: UX-01·UX-03, v1.2: UX-02) |
| **합계** | | **46** (v1: 34, v1.1: +3, v1.2: +6, v2: +1) |

---

## 16. 미포함 (v1 이후) — 벤치마크 갭 로드맵 (2026-06-06)

> `BENCHMARK_REPORT.md` §5-2 / REQUIREMENTS §1-5-1 갭과 정합. **시점**은 우선순위 — 일정 무관(결정 18) 기조 유지.

| 갭 | 경쟁사 | 시점 | 후보 Epic·스토리 |
|----|--------|------|-----------------|
| G1 — 보호자 풀 포털·알림(SMS·알림톡) | 케어포 가족돌봄앱, 이지케어 문자 | **v2** (알림톡) / v1.1 (무료 푸시) | Epic J — US-J03 **카카오톡 채널 알림톡**, 일일 케어 리포트 |
| G8 — 보호자 **초대·명세 모바일** | 케어포·**이지케어 EZCARE** | **v1.1 Must** | Epic J — **US-J01·J02** (초대·명세 탭) |
| G2 — 본인부담금 **CMS·간편결제** | 케어포 부가, 엔젤 CMS(월 30,000원+건당) | **v2** | Epic **N**(v2) — CMS·자동이체 |
| G3 — 공단 평가 2026 지표 자동화·서식 | 케어포·엔젤·이지케어 | **Could** | v3 / 별도 Epic — 평가지표 체크리스트 |
| G4 — 재무회계·세무·4대보험 | 이지케어 | **Won't v1** | — (별도 모듈 또는 외부 연동) |
| G5 — **배차·이동경로** | 케어포 2장(일정·차량) + ogada **경로 최적화** | **v1.3** (결정 60) | Epic **T** — US-T01~T03(A)·T04(A.1)·**T05(C, G15·G16)** |
| **G15** — **이동서비스 법정 서식** | 케어포·엔젤·이지케어 | **v1.3-C** | Epic **T** — US-T05 |
| **G16** — **차량·이동서비스비 청구** | 케어포 2-4·2-5 | **v1.3-C** | Epic **T** — US-T05 · **`transport_service_fee`** (BNK-9) |
| **G17** — **2026 평가 #27 기능회복훈련** | 케어포·이지케어 ✅ | **Won't v1** | Epic **T** — **US-T06** (Could v2+) |
| **G18** — **단기보호 시범** | 케어포 ✅ | **Won't v1** | ROADMAP v1.3 Won't (BNK-9) |
| **G19** — **통합재가서비스** | 케어포 ✅ | **Won't v1** | ROADMAP v1.3 Won't (BNK-9) |
| G5-b — 프로그램·식단 풀 모듈 | 케어포 3·5장 | **v3 develop 완료** (`dfd9be2`/`362dbf0`) | Epic **N** — US-N01·N02 · 사진 업로드 잔여 |
| G3-b — 직원 관리 UI | 케어포 8장(자격·배치·근태) | **v3 StaffPage develop 진입** (`fe33e7c`) | v3 §3-8 — CRUD·API 연동·Vitest **후속** |
| G13 — 본인부담 **입금·미납** | 케어포 7-2·7-3 | **v1.2 P0** | Epic **L** — US-L01·L02 |
| G14 — **등급변동 이력** | 케어포 1-9·엔젤 | **v1.2 P0** | Epic **M** — US-M01 |
| G6 — NFC/RFID 출석 | 케어포·이지케어 | **의도적 미채택** | 없음 — QR B방식 차별화 유지 |
| G7 — 공단 엑셀 컬럼 스펙·**`처리상태`열** | 업계 공통 (케어포 44438) | **즉시** | US-G04/G06 — 파서 스킵·정규화 Must; 파일럿 샘플 확보 후 검증 |

**기존 v1 이후 항목 (재확인)**

- 식사·프로그램 관리 (Should — G5)
- 보호자 알림톡·SMS (Should — G1)
- 공단 포털 직접 전송·API (Could — REQUIREMENTS §3-9-3)
- 본인부담금 CMS·간편결제 (v2 — G2)
- 서류 PDF 자동 생성 (Could — §3-10)
- 직원 관리 풀 모듈 (Should — §3-8) — **v3 StaffPage UI develop 진입 @ `fe33e7c`** (63차)

---

## 17. 프론트엔드 구현 규약 (v1.1 — QA 반영 2026-06-06)

> tester 검증 결과(QA-H04·M01·H03, TEST_REPORT F-3) — 프론트가 **스켈레톤+localStorage 데모** 수준이어서 v1.1 Must 스토리(US-B01~US-J02)가 실제로 동작하지 않음. v1.1은 아래 규약을 만족해야 각 스토리 인수 조건이 충족된 것으로 본다.

| # | 규약 | 근거 QA | 검증 |
|---|------|---------|------|
| FE-1 | Must 화면은 `/api/v1/*` **REST API를 JWT로 호출**한다 (localStorage 역할 데모 금지) | QA-H04 | P1–P8 프론트 E2E |
| FE-2 | 미인증/역할 불일치 접근은 **ProtectedRoute**로 차단(`/`·403) — develop HEAD 기준 | QA-H03 | `/platform`·`/settings`·`/dashboard/hq` 가드 |
| FE-3 | **Vitest + React Testing Library** `test` 스크립트로 ProtectedRoute·역할 라우팅·Must·J01/J02 **회귀 자동화** | **45차 QA-M01 Fixed @ `811aef3`** | `npm test` **40/11 PASS** @ `7170b2a` |
| FE-4 | v1.1 착수는 **v1 backend `merged`** 이후 (선행 게이트) | QA-B05 | ROADMAP v1 merge_status |
| FE-5 | JWT **access/refresh 토큰을 localStorage에 영구 저장 금지** — 메모리 세션(+필요 시 httpOnly refresh)으로 XSS 토큰 탈취면 축소 | SEC-005 | `AuthContext.jsx` HEAD에 `localStorage.get/set/removeItem(STORAGE_KEY)` 부재 |
| FE-6 | v1.1 `merge_status: merged` **전** v1.2 P0 착수 시에도 **완료 단위 develop 커밋** 또는 stash/revert로 working tree clean — v1.2 WIP를 미커밋으로 두면 **B07 recurrence BLOCK**. **#5(=recurrence #6)**(55차 Open→36차 Planned — 53차 `d5654c0` CLEAN 직후 15→**57차 20 files**: DateInput·GuardianInvitationList J01·ClientDetail·PaymentRecordModal·GuardianListCard(+test, **QA-H05**) → **FE-18·FE-19** 매핑·WT **209/210 FAIL**) | QA-B07 recurrence #1·#2·**#3·#5 Fixed**(#5=FE-6 #4); **#6 Planned**(#6=FE-6 #5) | `git -C src/frontend status` clean @ `d5654c0`·HEAD 199/40·756 modules(이관 규율 5·6·7 PASS) — **WT DIRTY 20 files·npm test FAIL** |
| FE-7 | v1.2 WIP develop 커밋 **전** `npm test`·`npm run build` **PASS** 필수 — duplicate symbol·빌드 FAIL 상태 커밋 금지 (16차 `routeAccess.js` duplicate 회귀; 19차 WT 10/4·107 modules PASS 회복; **21차 `a72e249` → HEAD `npm test` 10/4·build 110 PASS**; **25차 COD 17차 `a84473f` → HEAD `npm test` 13/5·build 111 PASS·`npm audit` 0건**; **26차 UXD 12차 `404a30e` LoginPage DS·Modal 접근성 → HEAD `npm test` 13/5·build 111 PASS·audit 0건**; **27차 COD 19차 `cc34f23` pilotChecklist fetch-mock → HEAD `npm test` 13/5 → **32/7 PASS**(+19 tests/+2 files)·build 111 modules PASS·audit 0건, FE-7 회귀 없음 정식 충족 — 4커밋 무재발**; **31차 COD 22차 `3fdc266` pilotPageFlows → HEAD `npm test` **140/11 PASS**(+10/+1)·build 113 modules·audit 0건**; **35차 Recharts·Platform WIP → WT `npm test` **144/13 PASS**(+2/+1)·build **738 modules**·audit 0건; **37차 운영/보안 설정 UI WIP → WT `npm test` **161/20 PASS**(+17/+7)·build **741 modules**·audit 0건; **39차 계정 보안·로그인 이력 UI WIP → WT `npm test` **169/24 PASS**(+8/+4)·build **743 modules**·audit 0건; **43차 청구·copay·건강·NHIS·보호자 UI WIP → WT `npm test` **179/29 PASS**(+10/+5)·build **748 modules**·audit 0건; **45차 `FeeScheduleTable`(+test) WIP → WT `npm test` **181/30 PASS**(+2/+1)·build **749 modules**·audit 0건; **47차 COD 31차 `4be0938` 커밋 후 HEAD `npm test` **185/33 PASS**(+4/+3)·build **752 modules**·audit 0건 — B07 #3 Fixed·FE-7 회귀 없음**) | QA-B07 recurrence **#3 Fixed**(47차 HEAD PASS·WT CLEAN) | develop HEAD `npm test`·`npm run build`·`npm audit` SUCCESS |
| FE-8 | dev 의존성 npm audit critical/high 발견 시 **메이저 업그레이드 또는 overrides**로 동일 라운드 해소 권장 — prod 번들 무관해도 dev server 공급망 위험 | SEC-008 Fixed via `ed1bf22`(vite `^6.4.3`·vitest `^4.1.8`·`overrides.esbuild ^0.25.0` → audit 0건; 26·27·31차 audit 0건 유지) | `npm audit --audit-level=high` 0 vulnerabilities |
| FE-9 | v1.1 Must API JWT 라우팅·HTTP 메서드·경로·페이로드는 **`src/api/pilotChecklist.js` 계약 사전 + Vitest fetch-mock으로 단위 자동 검증**·**7역할 라우트 가드/홈 경로/로그인 동작은 `sevenRoleJwtLogin.test.jsx`·`sevenRoleRouteGuard.test.jsx`·`sevenRoleRouteMatrix.js` 매트릭스 단위 E2E로 자동화** — USER_STORIES §13 P1–P8 시나리오를 services.js 경로에 1:1 매핑하고 7역할 × 라우트 매트릭스를 Vitest로 회귀, 라이ve E2E 전 단위 회귀를 보장한다 | **45차 TSR 63 Fixed @ `811aef3`** | `pilotChecklist`·`sevenRole*`·Must pages HEAD PRESENT — **`npm test` 40/11** @ `7170b2a` |
| FE-10 | 전사 설정 Switch 컴포넌트는 **WAI-ARIA `role=switch` + `aria-checked` + 44px hit target + `forced-colors`** 패턴 준수(DESIGN_SYSTEM §1·§9) — 셀프 체크인 토글(`allow_client_self_checkin`, 결정 16 안 3) 등 boolean 전사 정책 UI에 재사용 | UXD 13차 `07fd305` US-UX-03 충족 | `Switch.test.jsx` 5건 PASS·`SettingsPage` 토글 라이브 동작 |
| FE-11 | v1.1 Must 화면(P1–P8) **페이지 단위 RTL E2E** — `pilotPageFlows.test.jsx`로 각 Must 페이지 렌더·fetch-mock JWT API 호출·핵심 UI 요소를 Vitest+RTL로 통합 검증, fetch-mock 라우팅(FE-9) 위 **페이지 회귀**를 보장한다 | **45차 TSR 63 Fixed @ `811aef3`**(fetch-mock) | `pilotPageFlows.test.jsx` PASS — **`npm test` 40/11** @ `7170b2a` — **라이ve backend E2E 잔여** |
| FE-12 | v1.2 **Recharts 차트 레이어** — `ChartContainer`·`AttendanceRateChart`·`BranchCompareChart`·`HealthTrendChart` + **`HealthAlertList`(+test, US-M02 건강 알림)** + DESIGN_SYSTEM `chartColors.js` 토큰으로 대시보드·건강·출석 통계 차트를 구현하고 `ChartContainer.test.jsx`·`HealthTrendChart.test.jsx`로 회귀 자동화(BNK-6-4·US-M02) | **47차 COD 31차 `4be0938` develop HEAD 반영(B07 #3 Fixed)** | develop HEAD `ChartContainer`·`AttendanceRateChart`·`HealthTrendChart` PRESENT + HEAD `npm test` 185/33·build 752 modules PASS |
| FE-13 | v1.2 **Platform·NHIS 배치·reconciliation·청구·수가표 UI** — `BatchProgressSteps`(+test)·`PlatformOrgDetailModal`(+test, US-A01 Tenant 상세)·**`BillingStatusConfirmModal`(+test, US-G06)·`CopayRateTable`(+test, Epic G)·`FeeScheduleTable`(+test, US-G00a·케어포 9-x)·`NhisImportGuidePanel`(+test, 결정 37)·`GuardianDailySummary`(+test, Epic J/K)**·Platform/NHIS/Reconciliation/Forbidden 페이지로 HQ/플랫폼·NHIS import·청구·copay·수가표·보호자 UX를 보강(BNK-6·US-A01·US-G04·US-G06·Epic L) | **47차 COD 31차 `4be0938` develop HEAD 반영(B07 #3 Fixed)** | develop HEAD `BillingStatusConfirmModal`·`CopayRateTable`·`FeeScheduleTable`·`NhisImportGuidePanel`·`GuardianDailySummary` PRESENT·build 752 modules·`npm test` 185/33 PASS |
| FE-14 | v1.2 **운영·보안·계정 보안 설정 UI** — `AuditLogPanel`(+test)·`BackupSettingsPanel`(+test)·`FilterChips`로 감사 로그·백업 정책·필터 칩 UX, **§3-1 인증 모듈 매핑**으로 `PasswordChangeModal`(+test, 비밀번호 재설정 — SettingsPage 보안 탭 연결)·`PasswordResetRequestModal`(+test, 이메일 재설정 요청)·`LoginHistoryPanel`(+test, 로그인 이력 조회)·`SettingsPage.test.jsx`로 계정 보안 화면을 보강해 케어포 대비 운영/보안 모듈 패리티를 높인다(BNK-6 모듈 커버리지·보안 §3·접근성 §7·REQUIREMENTS §3-1) | **47차 COD 31차 `4be0938` develop HEAD 반영(B07 #3 Fixed, 26→44→60→61→72→76→0 정체 종결)** | develop HEAD `AuditLogPanel`·`BackupSettingsPanel`·`PasswordChangeModal`·`LoginHistoryPanel` PRESENT·build 752 modules·`npm test` 185/33 PASS |
| FE-15 | v1.2 **프런트 번들 코드 스플릿(성능, 비차단 LOW)** — B07 #3 Fixed 후 `npm run build`가 단일 JS 청크 **744.95 kB**(>500 kB) 경고. `manualChunks`로 `recharts`·vendor 분리해 초기 번들·LCP를 개선한다(BNK-6 모바일 UX·DESIGN_SYSTEM 성능) | **49차 COD 33차 `c98f98d` Fixed** — `manualChunks` 3청크(최대 393.53 kB <500 kB) | develop HEAD `npm run build` 최대 청크 ≤500 kB·`npm test` **186/34 PASS** |
| FE-16 | v1.1/v1.2 **DESIGN_SYSTEM ds-* 유틸리티 마이그레이션(일관성·유지보수)** — Must 페이지·모달·배너 컴포넌트의 **인라인 style을 ds-* 유틸리티 클래스로 전환**해 디자인 토큰 일관성을 높이고, 레이아웃 회귀를 `*.layout.test.jsx`로 자동화한다(DESIGN_SYSTEM §1·§9, UXD 협업) | **50차 COD 34차 `0b9b001`** — 9 컴포넌트(`AttendanceAbsentModal`·`BatchProgressSteps`·`CheckoutModal`·`FeeRateHistoryPanel`·`HealthAbnormalBanner`·`MedicationDuplicateAlert`·`PasswordResetRequestModal`·`PlatformOrgDetailModal`·`SessionTimeoutModal`) ds-* 전환 + `AttendancePage.layout.test.jsx` | develop HEAD `npm test` **187/35 PASS**·build **752 modules**·audit 0·WT CLEAN @HEAD |
| FE-17 | v1.1 **보호자 초대 수락 UI·로그아웃·레이아웃 회귀(J01·G8/EZCARE 패턴)** — `GuardianInvitationAcceptPage`(+test, `/guardian/invitations/:token/accept` 수락 흐름)·`LogoutButton`(+test)·`BillingPage.layout.test.jsx`·`AuthContext` logout·청구/보호자/Recharts 연동 WIP를 **완료 단위 develop 커밋**한다(BENCHMARK G8·US-J01, API_SPEC §4 연동은 백엔드 API 후) | **53차 COD 35차 `d5654c0` Fixed** — 25 files +823/-57 일괄 커밋·`GuardianInvitationAcceptPage`(+test)·`GuardianInvitationAcceptForm`·`PublicAuthLayout`·`LogoutButton`(+test)·`BillingPage.layout.test`·`acceptGuardianInvitationApi`·AuthContext logout, WT CLEAN·TSR 53차 독립 검증 PASS | develop HEAD `d5654c0` `npm test` **199/40 PASS**·build **756 modules**·audit 0·`git cat-file -e HEAD:` 산출물 PRESENT·**WT CLEAN** |
| FE-18 | v1.1 **보호자 초대 목록·수락·명세 모달 UI(J01·G8/EZCARE 패턴)** — `GuardianInvitationList.jsx`(+test)·`PaymentRecordModal.jsx`·`GuardianPortalPage.jsx`·`GuardianInvitationAcceptPage.jsx`·`/guardian/invitations/:token/accept` 라우트·`services.js` API 헬퍼를 develop 반영 | **44차 COD `f506c90` Fixed** — HEAD @ `c3b863e` · `npm test` **9/9 PASS**·build **70 modules**·WT CLEAN | develop HEAD `c3b863e` + clean tree |
| FE-19 | v1.1 **MaskedPhone 테스트 정합(FE-7·QA-H05·SEC-D9)** — 초대 목록 회귀 테스트에서 `010-****-5678` 마스킹 기준을 검증하고 평문 노출을 차단 | **44차 COD `f506c90` Fixed** — `GuardianInvitationList.test.jsx`·`MaskedPhone` 재사용 | `npm test` 9/9 PASS·마스킹 유지 |
| FE-20 | v1 **ProtectedRoute·AuthContext develop HEAD 반영(SEC-D12·QA-H03 회귀)** | **45차 Fixed @ `7170b2a`** — ProtectedRoute·AuthContext HEAD PRESENT | develop HEAD `ProtectedRoute` PRESENT·`/platform` 미인증 → `/login` |
| FE-21 | v1.1 **보호자 포털 REST API 연동(J01·J02 live 전 fetch-mock 회귀)** — `ClientDetailPage` 초대 발송·`GuardianPortalPage` 명세/청구 API 호출을 `services.js` 경로로 연결하고 Vitest fetch-mock으로 회귀 | **45차 COD `7170b2a` Fixed**(fetch-mock) | `ClientDetailPage.test.jsx`·`GuardianPortalPage.test.jsx` PASS — **live API E2E 잔여** |
| FE-22 | v1.1 **Must·J01 live E2E harness** — P1–P8·J01/J02 live run 스크립트 @ `d592a17` | **48차 Fixed(harness)** · **live run** = post-merge 권장(결정 73) | TSR 65 · `src/e2e/*` · merge 게이트 **제외** |
| INFRA-B12 | **workspace submodule baseline 정합**(SEC-D11·QA-B11·SEC-D12) | **45차 Fixed** — baseline `136239e`/`7170b2a` · `d5654c0` checkout **폐기** | `.agents/workspace_baseline.yaml` 확정 |

- 대상 스토리: US-B01·B02(인증·Branch Switcher), US-D01~D04(이용자), US-E01~E05(출석), US-F01~F04(건강), US-G01~G07(청구·reconciliation), US-J01·J02(보호자 초대·명세), **v1.2 Epic K·L·M·UX**(commit 단위).
- 이관 규율: develop 커밋 후 `merge_status: ready` (ROADMAP `## QA 피드백 반영` 이관 규율). **(7차)** 완료 단위마다 develop 커밋·working tree clean(QA-B07), API 계약 변경은 API_SPEC 선반영(이관 규율 6). **(12차)** v1.2 선행 WIP도 동일 — FE-6·이관 규율 7. **(13차)** 커밋 전 build/test 품질 게이트 — FE-7.

---

## 18. 백엔드 구현 규약 (v1 — QA 반영 2026-06-06)

> tester 검증 결과(QA-B02 recurrence, TEST_REPORT §1 15차·20차·**22차 recurrence #3 Fixed**) — RBAC·NHIS import·Billing 라우팅 테스트 등 working tree WIP가 develop HEAD 미커밋으로 남으면 v1 merge 게이트 BLOCK 반복.

| # | 규약 | 근거 QA | 검증 |
|---|------|---------|------|
| BE-8 | v1.1 **J01 `guardian_invitations` API(V43·Controller·Service·token·EMAIL·SEC-D8)** — develop `@f47ffa1` HEAD **Fixed**(TSR 58차). Controller·V43·`SecurityConfig`·rate limit **PRESENT** | **58차 TSR — QA-B09 Fixed @ `f47ffa1`** + **SEC-D8 Fixed** | develop HEAD `f47ffa1` + clean tree ✓ |
| BE-10 | v1 **merged baseline 정합(QA-B10)** — develop `@136239e` v1 E2E/routing **PRESENT** · test `@2799e29` **stale(4 behind)** | **45차 TSR 62·BE-10 Fixed** | develop HEAD v1 산출물 PRESENT · merge 후 test 재검증 |
| BE-11 | v1 **인증 API rate limiting(SEC-D13)** — `AuthRateLimitService`로 login·refresh·password-reset-request·password-reset에 IP+email 슬라이딩 윈도우 적용 · J01 `InvitationAcceptRateLimiter` 패턴 재사용 · 단위 테스트 | **47차 Fixed @ `8d42bdd`**(TSR 64) — SEC-20260608-014 **Fixed** | `AuthRateLimitService` HEAD PRESENT · `SECURITY_AUDIT.md` A04-1 해소 |
| BE-6 | RBAC·단위 테스트 확장 등 **완료 단위 develop 커밋** 또는 stash/revert — working tree에 WIP 미커밋 금지 | QA-B02 recurrence (#1·#2 Fixed `b5d70a8`; **#3 Fixed `4274459`**; **#4 Fixed `e8750d2`**; **#5 Fixed `c3b8716`**; **#6 Fixed `428ba7d`** TSR 54차 — V42 + `NotificationPreferenceServiceTest` 4 @Test develop 커밋); **#7 Planned B09**(56차 J01 API WIP recurrence) | `git -C src/backend status` clean @ `428ba7d` — 253/253 PASS |
| BE-7 | v1 **`merged` 후** v2 착수 시에도 **완료 단위 develop 커밋** 또는 stash/revert — v2 WIP(`notification_preferences`·V41·**V42 consent CHECK** 등)를 working tree에만 두면 **B08 BLOCK**(이관 규율 8) | **QA-B08 Fixed `feac558`**(V41 + 7 java + 8 @Test HEAD PRESENT); **recurrence #2 Fixed `428ba7d`** TSR 54차 — V42 + `NotificationPreferenceServiceTest` 4 @Test develop HEAD PRESENT·WT CLEAN | V42 + `NotificationPreferenceServiceTest` @HEAD `428ba7d` ✓ |

- 대상: `RoleBasedControllerAccessTest`(guardian·client_user RBAC·billing/guardian 확장), v1 7역할 E2E 선행 단위 테스트, **NHIS import 테스트**(`NhisImportServiceTest` 지점 검증·수동 매칭), **Billing 라우팅 테스트**(`BillingControllerRoutingTest` 3 `@Test`), **Must API 엔드포인트 라우팅**(`MustApiEndpointRoutingTest` §1–§9 26+ @Test — R-02 [x] 승격), **prod 시크릿 검증**(`ProductionSecretValidatorTest`), **파일럿 체크리스트 `@PreAuthorize` 자동화**(`PilotChecklistApiAccessTest` P1–P8 × 7역할 29 @Test — R-04 `@WebMvcTest` 65건 PARTIAL 승격), **`PilotChecklistJwtE2eTest`**(P1–P8 live Bearer JWT filter-chain E2E, 22 @Test — B02 #5 Planned), **v2 `notification_preferences`**(`NotificationPreferenceService`·`GuardianNotificationPreferenceController`·V41 — B08 Planned), 기타 `@WebMvcTest` 확장.
- 커밋 전 **`mvn -q test` PASS** 권장(결정 51).
- **BE-6 패턴 #5 Fixed(32차)**: COD 32차 `c3b8716` — `PilotChecklistJwtE2eTest.java`(634 lines/22 @Test) develop HEAD 반영·WT CLEAN. TSR 48차 독립 검증 PASS. **#36 대칭 종결**.
- **BE-7 v2 선행 dirty-tree Fixed(32차)**: COD 32차 `feac558` — `notification_preferences`·V41 + 7 java + 8 @Test develop HEAD 반영. v2 test 검증은 v2 사이클 별도(결정 54).
- **BE-6 #6 / BE-7 recurrence #2 재발(33차 — TSR 50차)**: 48차 `c3b8716` CLEAN 직후 v2 follow-up **미커밋 재오염** — `V42__guardian_notification_preferences_consent_temporal.sql`(54 lines kakao/sms consent CHECK·temporal monotonicity) + `NotificationPreferenceServiceTest`(3 @Test). **HEAD Fixed(B02 #5·B08) 규율 5 유효** — recurrence는 미커밋 v2 follow-up 단일. develop WT `mvn test` 252/252 PASS. **#36 backend 단독 재오픈**(결정 53 — frontend는 COD 33·34차 연속 CLEAN). coder: 완료 단위 develop 커밋 후 working tree clean.
- **FE-16 ds-* 유틸리티 마이그레이션(33차 — TSR 50차)**: COD 34차 `0b9b001` — 9 컴포넌트 인라인 style→ds-* 전환 + `AttendancePage.layout.test.jsx` 레이아웃 회귀. HEAD @ `0b9b001`·187/35·752 modules·FE-16 @HEAD Fixed. v1.1 develop→test merge 동반 흡수(결정 52).
- **FE-17 J01 수락 UI·LogoutButton Fixed(35차 — TSR 53차)**: COD 35차 `d5654c0`(25 files +823/-57) 일괄 커밋 — `GuardianInvitationAcceptPage`(+test, J01 수락 프론트)·`GuardianInvitationAcceptForm`·`PublicAuthLayout`·`LogoutButton`(+test)·`BillingPage.layout.test`·`acceptGuardianInvitationApi`·AuthContext logout·Recharts·청구/보호자 페이지. working tree **20→0 CLEAN**, `git cat-file -e HEAD:` 산출물 PRESENT(이관 규율 5·6·7 PASS), HEAD `npm test` **199/40 PASS**·build **756 modules**·audit 0 → **B07 #5 Fixed·FE-17 @HEAD 충족**·결정 52 흡수 ⑪묶음. 백엔드 J01 초대/수락 API(#33·#35) 연동 전 `acceptGuardianInvitationApi` fetch-mock/스텁 유지 — 라이ve E2E는 백엔드 API 후.
- **BE-6 #6 / BE-7 recurrence #2 — COD 35 false Fixed(34차 — TSR 51차)**: COD 35 Fixed 주장 **TSR FAIL** — V42 + `NotificationPreferenceServiceTest` WT untracked·HEAD ABSENT. ROADMAP v1 QA-B02·v2 B08 recurrence #2 `[x]` 철회·**Planned 유지**.
- **BE-6 #6 / BE-7 recurrence #2 Fixed(36차 — TSR 54차)**: COD 36 `428ba7d` — V42 consent CHECK·temporal + `NotificationPreferenceServiceTest` 4 @Test develop HEAD 반영·WT CLEAN. TSR 54차 독립 검증 PASS. develop **3 ahead of test**(결정 54 갱신). **#36 backend BE-6/BE-7 해소**.
- **BE-8 J01 API Fixed(42차 — TSR 58차)**: develop `@f47ffa1` — `GuardianInvitationController`·V43·`SecurityConfig`·SEC-D8 **HEAD PRESENT**. backend merge **1 commit** 잔여. **BE-10**(QA-B10) baseline 정합 선행 또는 병행.
- **INFRA-B12·FE-20·SEC-D12(45차 Fixed)**: baseline `7170b2a`/`136239e` 확정 · `d5654c0` checkout **폐기**.
- **FE-18·FE-19 Fixed(44차 — COD `f506c90`)**: J01 UI·MaskedPhone 회귀 develop 반영.
- **FE-9·FE-11·FE-3·SEC-008 Fixed(45차 — TSR 63 @ `811aef3`)**: Must API·pilot·7-role·audit 0 develop HEAD 반영.
- **FE-21 Fixed(45차 — COD `7170b2a`, fetch-mock)**: J01 `ClientDetailPage`·J02 `GuardianPortalPage` REST 연동 회귀. **잔여**: Must·J01 **live E2E** → **FE-22**.
- **BE-11 Planned(46차 — SEC 6차 SEC-D13)**: `AuthService` login·refresh·reset rate limit 부재 — credential stuffing·reset flood 방어. merge 전 구현 권고.
- **FE-22 PARTIAL(47차 — COD `d592a17`, TSR 65)**: live E2E **harness** develop HEAD 반영. **48차 결정 73**: live run → **merge 후** post-merge 권장(merge BLOCK 제외).
- **BE-11 Fixed(47차 — TSR 64 @ `8d42bdd`)**: SEC-20260608-014 **Fixed**.
- **BE-6 #6 / BE-7 recurrence #2 — backend 단독 잔존(35차 — TSR 53차, 이력)**: 51차 대비 develop HEAD `c3b8716`·dirty-tree **완전 불변**(V42 + `NotificationPreferenceServiceTest` 4 @Test HEAD ABSENT). → **36차 COD 36 `428ba7d` Fixed로 해소**.

---

*이 문서는 planner 에이전트가 관리합니다. 변경 시 `docs/planning/REQUIREMENTS.md`와 동기화하세요.*
