<!-- doc:owner=TWR doc:audience=PLN,COD updated=2026-06-18T05:00:00+09:00 -->
# ogada 자주 묻는 질문 (ops/FAQ.md)

> **작성**: tech_writer 에이전트  
> **최초 작성일**: 2026-06-05  
> **최종 갱신**: 2026-06-18 (208차 — **G15 일지 감사·보관 UX · 월간 리포트 2-7/2-8 · probe seed guard · docs sync**)  
> **상태**: 초안 (Draft)  
> **대상 독자**: 주간보호센터 **현장 사용자**, **센터 운영·IT 담당**, **ogada 플랫폼 운영자**  
> **기준 문서**: `docs/planning/REQUIREMENTS.md`, `docs/technical/API_SPEC.md`, `docs/planning/FLOWCHART.md`, `docs/ops/USER_MANUAL.md`, `docs/ops/ADMIN_GUIDE.md`  
> **기술 스택**: Java Spring Boot 3.x + React (Vite SPA) + PostgreSQL

---

## 1. 이 FAQ에 대하여

ogada 도입·운영 과정에서 자주 반복되는 질문을 **역할·기능별**로 정리했습니다.  
상세 조작 절차는 [`USER_MANUAL.md`](ops/USER_MANUAL.md), 플랫폼·기술 관리는 [`ADMIN_GUIDE.md`](ops/ADMIN_GUIDE.md), 배포·인프라는 [`DEPLOYMENT_GUIDE.md`](ops/DEPLOYMENT_GUIDE.md)를 참고하세요.

### 구현 상태 안내 (2026-06-17 develop HEAD `aa42b9c` / frontend `6a18dfd` 기준)

| 영역 | 상태 | FAQ에서의 의미 |
|------|------|----------------|
| 백엔드 API | **Must + … + G15 service log audit @ `aa42b9c` · monthly reports 2-7/2-8 @ `5d27ad3` · QA-B95 probe guard @ `0b5657a` · V148 · US-T02·…** | **`TRANSPORT_SERVICE_LOG_UPSERT`** · **`GET /transport/reports/monthly-*`** (Q410·Q411) |
| 데이터베이스 | Flyway **V1–V148** | **V148** service log compliance · 월간 리포트는 **기존 데이터 집계** |
| 프론트엔드 | **106 route · G15 `TransportServiceLogPanel` archive @ `088e906` · `TransportMonthlyReportsPage` @ `6a18dfd` · QA-B116 a11y @ `dff2f32` · US-E04·US-T02·compliance·SEC-005·L02·G26·G21** | **일지 보관·감사 추적** · **`/reports/transport-monthly`** (Q410) |
| 본 FAQ | **Q410·Q411 신규** · **Q236·Q407·Q409 갱신** · Q408 carry | **월간 리포트** · **일지 감사·보관 UX** · **probe 500 방지** |

---

## 2. 서비스 개요

### Q1. ogada는 무엇인가요?

**A.** ogada는 전국 주간보호센터·요양기관 운영법인을 위한 **B2B SaaS 클라우드 웹 시스템**입니다. 이용자 관리, 출석(수기·QR), 건강 기록, 청구·정산, 다지점 대시보드 등 일상 운영 업무를 디지털화합니다. PC·태블릿·스마트폰 브라우저에서 반응형으로 사용합니다.

### Q2. 개인 센터 1곳만 쓰는 전용 프로그램인가요?

**A.** 아닙니다. **전국 판매용 멀티테넌트 SaaS**입니다. 운영법인 1곳이 `Organization`(Tenant) 1개이며, 여러 법인이 동일 플랫폼을 사용하되 **데이터는 완전히 분리**됩니다.

### Q3. 케어포·이지케어 같은 기존 ERP와 무엇이 다른가요?

**A.** ogada는 **주간보호센터 운영에 특화된 SaaS**로 설계되었습니다. 청구·정산은 케어포와 유사한 **2단계 모델**(내부 계산 + 공단 엑셀 import)을 따르며, **다지점 통합 대시보드**, **보호자 QR 셀프 체크인(B방식)**, **테넌트 격리**를 MVP부터 포함합니다. **본인부담금 CMS 자동이체(7-4)**·**간편결제(7-5)** 는 v2 **BE·FE skeleton Fixed**(Q206–Q208·Q326, stub FCMS·stub PG)이며, **효성 FCMS·live PG 실연동**·공단 포털 직접 전송은 후속입니다.

### Q4. 어떤 브라우저·기기를 지원하나요?

**A.** Chrome, Safari, Edge **최신 2버전**을 권장합니다. 화면 너비 360px(모바일)~1200px(PC) 반응형을 목표로 합니다. 보호자 QR 체크인은 **스마트폰 카메라** 또는 브라우저 QR 스캔이 필요합니다.

---

## 3. 계정·온보딩

### Q5. 새 센터가 ogada를 쓰려면 계정은 누가 만들어 주나요?

**A.** **ogada 직원(`platform_admin`)**이 신규 고객을 등록합니다. 센터가 스스로 공개 가입(`/signup`)하는 방식은 MVP에 **포함하지 않습니다**.

| 순서 | 담당 | 작업 |
|------|------|------|
| 1 | ogada `platform_admin` | `/platform`에서 법인(Tenant) 등록 |
| 2 | ogada `platform_admin` | 첫 **통합 관리자(`hq_admin`)** 계정 발급 |
| 3 | 고객 `hq_admin` | 지점 등록, 직원·이용자 등록, 운영 시작 |

> 비유: 통신사 매장이 **새 회선을 개통**해 주는 것과 같습니다. (REQUIREMENTS §1-3)

### Q6. 센터장·요양보호사·보호자 계정은 누가 만드나요?

**A.** 고객 센터 **`hq_admin` 또는 `branch_admin`**이 직원 계정을 생성하고 역할·소속 지점을 배정합니다. 보호자(`guardian`) 계정은 이용자 등록 시 **보호자 연결** 과정에서 발급·연결합니다.

### Q7. 로그인 정보(이메일·비밀번호)를 잊었어요.

**A.** 로그인 화면(`/`)의 **비밀번호 찾기**로 재설정 메일을 요청합니다 (`POST /api/v1/auth/password/reset-request`). 등록된 이메일로 링크가 발송됩니다. 계정 자체가 없거나 이메일을 모르면 **소속 센터 `hq_admin`·`branch_admin`** 또는 ogada 고객 지원에 문의하세요.

### Q8. 로그인했는데 화면이 역할과 다른 것 같아요.

**A.** 로그인 후 이동 경로는 JWT의 `role`에 따라 자동 분기됩니다.

| 역할 | 홈 화면 |
|------|---------|
| `platform_admin` | `/platform` |
| `hq_admin` | `/dashboard/hq` |
| `branch_admin`, `social_worker`, `caregiver` | `/dashboard` |
| `guardian`, `client_user` | `/guardian` |
| `sysadmin` | `/settings` |

권한이 잘못 배정된 경우 센터 **`hq_admin`**에게 역할 수정을 요청하세요.

---

## 4. 역할·권한

### Q9. ogada에는 몇 가지 역할이 있나요?

**A.** MVP v1 기준 **7개 역할** + 보조 유형 `client_user`입니다.

| 역할 | 코드 | 주요 업무 |
|------|------|----------|
| 플랫폼 관리자 | `platform_admin` | 신규 Tenant 등록, 첫 `hq_admin` 발급 (ogada 내부) |
| 통합 관리자 | `hq_admin` | 다지점 통합 대시보드, 지점·계정·수가표·청구 |
| 지점장 | `branch_admin` | 지점 운영 총괄, 이용자·출석·건강·청구 |
| 사회복지사 | `social_worker` | 이용자·건강 기록, 출석 조회 |
| 요양보호사 | `caregiver` | 수기 출석·건강 기록 입력 |
| 보호자 | `guardian` | 연결 이용자 기록 열람, QR 체크인 |
| 시스템 관리자 | `sysadmin` | 자기 Tenant 백업·감사·기술 설정 |
| 이용자 본인 | `client_user` | 본인 1명 QR 체크인·기록 열람 (조건부) |

### Q10. `platform_admin`과 `sysadmin`은 같은 관리자인가요?

**A.** **다릅니다.**

| 구분 | `platform_admin` | `sysadmin` |
|------|------------------|------------|
| 소속 | ogada 내부 | 고객 센터(Tenant) |
| 범위 | 전국 Tenant **메타데이터** | **자기 Tenant** 기술 영역 |
| 할 수 있는 일 | 신규 센터 등록, 요금제·활성 상태 | 백업·감사 로그·기술 설정 |
| 할 수 없는 일 | 센터 이용자·출석 데이터 조회 | 다른 Tenant 접근, 운영 데이터 CRUD |

### Q11. `hq_admin`은 모든 지점 데이터를 수정할 수 있나요?

**A.** **조회·집계는 전 지점** 가능하지만, **등록·수정(CRUD)은 지점 선택기로 `active_branch_id`를 고른 뒤 해당 지점만** 가능합니다. 지점을 바꾸지 않고 다른 지점 데이터를 수정하려 하면 `403 FORBIDDEN_SCOPE` 오류가 발생합니다.

### Q12. 요양보호사는 이용자를 등록할 수 있나요?

**A.** **이용자 등록·수정은 `hq_admin`, `branch_admin`, `social_worker`** 권한입니다 (BE `208b37e`, Q267). `caregiver`는 **출석·건강 기록 입력**과 이용자 목록 **조회**가 주 업무입니다.

> **`hq_admin` 주의**: 다지점 통합 관리자는 **지점 선택기(Branch Switcher)로 활성 지점을 선택한 뒤** 해당 지점에만 등록할 수 있습니다. 활성 지점이 없으면 **403**(`활성 지점이 선택되지 않았습니다.`)이 반환됩니다.

---

## 5. 다지점·데이터 보안

### Q13. 지점이 2곳 이상일 때 데이터가 섞이지 않나요?

**A.** 이용자·출석·건강·청구 등 운영 데이터는 **`branch_id`로 소속 지점**이 식별됩니다. `branch_admin` 이하 역할은 **자신의 `branch_ids` 범위만** 접근합니다. `hq_admin`은 통합 조회가 가능하나, 쓰기는 선택 지점으로 제한됩니다.

### Q14. 다른 센터(법인) 데이터를 볼 수 있나요?

**A.** **불가능합니다.** 모든 API는 JWT의 `organization_id`로 **테넌트 격리**를 강제합니다. A센터 계정으로 B센터 이용자·출석 데이터에 접근할 수 없습니다.

### Q15. 30분 동안 아무 것도 안 하면 어떻게 되나요?

**A.** FE `9bdf59f` — **`SessionTimeoutProvider`**(US-B03)가 로그인 세션에 적용됩니다.

| 상황 | 동작 |
|------|------|
| **30분 무활동** | **`SessionTimeoutModal`** — 60초 카운트다운 후 자동 로그아웃 (Q112) |
| **연장** | 모달 **「세션 연장」** — idle 타이머 리셋 |
| **페이지 새로고침 (같은 탭)** | **`restoreSession()`** — refresh token(`sessionStorage`)으로 **로그인 유지** (Q396) |
| **탭 닫기** | refresh token 소멸 → **재로그인** |
| **30분 후 API 호출** | access token 만료 → `401` → 재로그인 필요 |

공용 PC 사용 후에는 AppShell **로그아웃** 버튼 또는 **브라우저 탭 종료**를 권장합니다.

---

## 6. 이용자·개인정보

### Q16. 주민등록번호를 꼭 입력해야 하나요?

**A.** **예.** 노인장기요양보험법 시행규칙상 공단 청구명세서에 수급자 주민등록번호 기재가 **법정 필수**이므로 ogada에서도 수집합니다. 다만 다음 보호 조치가 적용됩니다.

| 항목 | 정책 |
|------|------|
| 저장 | AES-GCM **암호화** |
| 화면·목록 | `******-*******` **마스킹** |
| 수집 | **별도 수집·이용 동의** 필수 (미동의 시 저장 불가) |
| 열람 | 청구 등 법정 목적 시에만 복호화, **감사 로그** 기록 |

### Q17. 이용자 연락처·주소도 암호화되나요?

**A.** **권장 정책으로 암호화 저장**합니다. 연락처는 화면에서 부분 마스킹될 수 있습니다. 장기요양인정번호는 검색·청구 키로 **평문** 저장합니다.

### Q18. 보호자는 몇 명까지 연결할 수 있나요?

**A.** **1명 이상** 연결이 필요합니다. 복수 보호자 연결 시 QR 체크인 때 **대상 이용자 선택** UI가 표시됩니다.

### Q19. 이용자 본인 계정(`client_user`)은 언제 만드나요?

**A.** 어르신이 스마트폰으로 **직접 QR 체크인**을 할 때 선택적으로 발급합니다. 센터 **`hq_admin`**이 Organization 설정 `allow_client_self_checkin`을 **켜야** 본인 계정 QR 스캔이 허용됩니다 (기본값: **꺼짐**).

---

## 7. 출석·QR

### Q20. 출석 입력 방법은 몇 가지인가요?

**A.** MVP에서 **2가지**를 지원합니다.

| 방식 | 담당 | `check_in_method` | 설명 |
|------|------|-------------------|------|
| **수기** | `caregiver` 이상 직원 | `manual` | 웹에서 이용자 목록 체크인/아웃 |
| **QR 셀프 (B방식)** | `guardian`, `client_user` | `qr_self` | 지점 입구 QR을 보호자·이용자 폰으로 스캔 |

> **A방식**(직원이 이용자 명창 QR 스캔)은 MVP **미포함**입니다.

### Q21. QR 체크인은 어떻게 동작하나요? (B방식)

**A.** 흐름은 다음과 같습니다.

1. 직원이 `/attendance/qr/generate`에서 **입소/귀가 QR** 생성·게시 (유효 시간 있음)
2. 보호자(또는 허용된 `client_user`)가 **로그인** 후 QR 스캔
3. 연결 이용자가 여러 명이면 **대상 선택**
4. 유효한 QR 토큰이면 출석 기록 생성

지점 QR만으로는 이용자를 특정할 수 없으므로 **반드시 로그인 계정**이 필요합니다.

### Q22. QR 스캔이 안 되거나 「유효하지 않은 QR」 오류가 나요.

**A.** 다음을 확인하세요.

| 원인 | 해결 |
|------|------|
| QR **유효 시간 만료** | 직원이 새 QR 생성·게시 |
| **로그인 안 됨** | 보호자·이용자 계정으로 먼저 로그인 |
| 연결 이용자 **미선택** | 복수 연결 시 대상 선택 |
| `client_user`인데 설정 off | `hq_admin`에게 `allow_client_self_checkin` 활성화 요청 |
| 이미 체크인됨 | 중복 체크인은 `422 BUSINESS_RULE` — 수기 확인 |

### Q23. 보호자가 오지 않고 어르신만 도착하면?

**A.** **직원 수기 체크인**(`manual`)으로 처리합니다. 또는 센터 정책에 따라 `client_user` 계정·셀프 체크인 허용을 검토할 수 있습니다.

### Q24. 파일럿 현장에서는 누가 출석 기능을 쓰나요?

**A.** 파일럿(지점 2, 센터장 1, 요양보호사 5)에서는 **`branch_admin` + `caregiver`**가 수기 출석 중심으로 검증합니다. QR 기능은 MVP에 포함되나 파일럿 범위 밖 역할(보호자 등)은 후속 확대 시 검증합니다.

---

## 8. 건강 기록

### Q25. 누가 건강 기록을 입력할 수 있나요?

**A.** **`caregiver` 이상** (`caregiver`, `social_worker`, `branch_admin`)이 입력합니다. 기록 유형: 일일 바이탈(혈압·체온·혈당·SpO2), 투약, 낙상·사고, 특이사항 메모.

### Q26. 건강 이상 알림은 어디에 표시되나요?

**A.** **지점 대시보드**(`/dashboard`)와 **`hq_admin` 통합 대시보드**(`/dashboard/hq`)의 건강 이상 목록에 표시됩니다. 이상 수치 기준은 시스템 규칙에 따릅니다.

---

## 9. 청구·정산

### Q27. ogada가 공단에 청구서를 직접 전송하나요?

**A.** **MVP에서는 하지 않습니다.** 공단 급여 청구는 **장기요양정보시스템(롱텀) 포털**에서 수행하고, ogada는 **내부 계산·명세서·엑셀 대조**를 담당합니다.

### Q28. 월별 청구서는 어떻게 만들어지나요?

**A.** 사전에 `hq_admin`이 **수가표**(`fee_schedules`)와 **본인부담 비율표**(`copay_rates`)를 설정한 뒤:

```
총 급여비용 = 등급별 1일 수가 × 해당 월 출석일수
본인부담금 = 총액 × 이용자별 copayType 비율
공단부담 = 총액 − 본인부담금
```

`/billing`에서 지점·대상월을 선택해 **청구서 생성** (`POST /api/v1/billing/claims/generate`)합니다.

### Q29. 수가표는 코드에 박혀 있나요? 매년 바뀌면 어떻게 하나요?

**A.** **화면에서 관리**합니다(B방식). `hq_admin`이 **연도·등급·이용시간 밴드**별 1일 수가를 `/billing/fee-schedules`에서 입력·수정하며(G9, Q210–Q211), 개정 이력이 보존됩니다. 과거 확정 청구는 **당시 수가 버전**을 유지합니다.

### Q30. 본인부담률(15%/9%/6%/0%)은 이용자마다 다른가요?

**A.** **예.** 이용자 등록 시 **본인부담 구분**(`copayType`)을 저장합니다. 화면에서는 UI 약칭과 **법·고시 정식 용어**를 함께 표시합니다 (G9-COPAY-NAMING, Q313).

| 코드 | UI 약칭 | 정식 용어 (`statutoryLabel`) | 대표 비율 |
|------|---------|------------------------------|----------|
| `GENERAL` | 일반 | 일반 (감경 없음) | 15% |
| `REDUCED_40` | 감경 40% | **100분의 40 감경** | 9% |
| `REDUCED_60` | 감경 60% | **100분의 60 감경** | 6% |
| `MEDICAID` | 기초수급 | 의료급여 (본인부담 면제) | 0% |

> **주의**: 「감경 40%」는 **본인부담률 40%**가 아니라 **감경 비율**입니다. 실제 본인부담률은 **9%**입니다 (longterm 503·노인장기요양보험법 제40조, BNK-166 §166-3).

실제 비율 수치는 `copay_rates` 테이블에서 개정 대응 가능합니다. **`CopayTypeSelect`**·**`CopayRateTable`** 에서 정식 용어가 help·설명에 병기됩니다 (`e77b7e4`).

### Q31. 공단 「청구내역상세」엑셀은 어떻게 쓰나요?

**A.** 롱텀에서 다운로드한 엑셀을 ogada **`/billing` → 엑셀 import** (`POST /api/v1/billing/imports/nhis`)로 업로드하면 공단 청구 건수와 내부 데이터를 **대조**합니다. 케어포식 연동과 동일한 2단계 모델의 일부입니다.

업로드 후 각 행은 다음 상태로 표시됩니다.

| 상태 | 의미 |
|------|------|
| `MATCHED` | 공단 데이터와 ogada 이용자·청구 일치 |
| `UNMATCHED` | 이용자 매칭 실패 — 인정번호·이름 확인 |
| `DISCREPANCY` | 이용자는 매칭되었으나 일수·금액 불일치 |
| `PENDING_REVIEW` | 공단 처리 **대기·보류** — 심사 완료 후 재import (Q181) |

> **구현됨**: `NhisImportService`, Flyway V19–V20 대사 무결성 제약. **G7 `PENDING_REVIEW`** — V54 (Q181).

### Q32. 본인부담금 청구서를 보호자에게 자동 발송하나요?

**A.** **MVP 제외**입니다. v1 이후 알림톡·SMS·CMS/간편결제 연동을 검토합니다.

### Q33. 청구서 상태(작성중·확정·수납완료)는 무엇인가요?

**A.** 청구 워크플로 상태입니다.

| 상태 | 의미 |
|------|------|
| 작성중 | 생성·검토 단계, 수정 가능 |
| 확정 | 검토 완료, 명세서 PDF 출력 가능 |
| 수납완료 | 본인부담금 수납 기록 완료 |

확정 이후 변경 규칙은 업무 정책·시스템 제약을 따릅니다.

---

## 10. 대시보드·리포트

### Q34. 지점 대시보드와 통합 대시보드의 차이는?

**A.**

| 화면 | 역할 | 내용 |
|------|------|------|
| `/dashboard` | `branch_admin` 이하 | **선택 지점** 오늘 출석·이용자 통계·건강 이상·월별 출석률 |
| `/dashboard/hq` | `hq_admin` | **전 지점** 출석·이용자·출석률 비교, 통합 건강 이상 목록 |

### Q35. 대시보드에 데이터가 비어 있어요.

**A.** 다음을 확인하세요.

- **지점 선택기**가 올바른 지점인지 (`hq_admin`·다지점 권한)
- 해당 일자·지점에 **이용자·출석·건강 기록**이 실제로 입력되었는지
- 로그인 **역할**이 해당 대시보드 API 권한을 갖는지 (`GET /api/v1/dashboard/branch` 또는 `/hq`)

---

## 11. 기술·배포

### Q36. ogada 기술 스택은 무엇인가요?

**A.**

| 계층 | 기술 |
|------|------|
| 백엔드 | Java 17, Spring Boot 3.5.x, REST API `/api/v1` |
| 프론트엔드 | React 18, **Vite 6** SPA (Vitest 4) |
| DB | PostgreSQL 15+, Flyway 마이그레이션 |
| 인증 | JWT (RS256), RBAC, 30분 access / 7일 refresh |

### Q37. 온프레미스(센터 서버) 설치가 가능한가요?

**A.** 기본 모델은 **SaaS 클라우드**입니다. 아키텍처는 Docker + PostgreSQL 기준 **이식 가능** 구조를 목표로 하나, 온프레미스 단독 배포는 별도 계약·검토 사항입니다. 배포 절차는 [`DEPLOYMENT_GUIDE.md`](ops/DEPLOYMENT_GUIDE.md)를 참고하세요.

### Q38. API를 외부 시스템과 연동할 수 있나요?

**A.** MVP는 **React SPA ↔ Spring Boot REST** 내부 연동이 주입니다. 공단 포털 **직접 API 연동·외부 EMR**은 v1 범위 **외**(Won't)입니다. 연동 필요 시 ogada 운영팀과 별도 협의가 필요합니다.

---

## 12. MVP 범위·로드맵

### Q39. MVP v1에 포함되는 기능은?

**A.** Must 우선순위 전체:

- 인증·7역할 RBAC·지점 선택기
- 플랫폼 고객 등록 (`platform_admin`)
- 다지점·이용자·출석(수기+QR B)·건강 기록
- **청구·정산**(수가표, 월별 청구서, 공단 엑셀 import)
- 지점·통합 대시보드

### Q40. MVP v1에 **없는** 기능은?

**A.** 다음은 **v1 이후(Should/Could)** 또는 **제외**입니다.

| 제외 항목 | 비고 |
|----------|------|
| 식사·프로그램 관리 | Should |
| 보호자 알림톡·SMS 자동 발송 | Should |
| 직원 근태·교대 스케줄 상세 | Should |
| 공단 포털 직접 전송·API | Could / Won't (v1) |
| 본인부담금 CMS·간편결제 | **CMS·7-5 skeleton Fixed**(Q206–Q208·Q326) · **FCMS·live PG** 후속 |
| QR A방식(직원→이용자 QR) | 후속 |
| 외부 EMR·생체인식 로그인 | Won't (v1) |
| 센터 셀프 가입(`/signup`) | 비권장, 후속 검토 |

### Q41. 변경 이력은 어디서 보나요?

**A.** [`CHANGELOG.md`](ops/CHANGELOG.md)에서 버전별 Added/Changed/Fixed 항목을 확인합니다.

---

## 13. 문제 해결 (Troubleshooting)

### Q42. 「권한이 없습니다」(`403 FORBIDDEN_SCOPE`) 오류가 나요.

**A.**

| 상황 | 조치 |
|------|------|
| 다른 지점 데이터 수정 시도 | **지점 선택기**로 `active_branch_id` 변경 |
| `caregiver`가 이용자 등록 시도 | `branch_admin`·`social_worker`에게 요청 |
| `sysadmin`이 이용자 메뉴 접근 | 정상 — `sysadmin`은 운영 CRUD 권한 없음 |
| `platform_admin`이 출석 조회 | 정상 — 플랫폼 역할은 Tenant 메타만 관리 |

### Q43. API 오류 메시지에 `traceId`가 붙어 있어요.

**A.** 지원 요청 시 **`traceId`를 함께 전달**하면 서버 로그 추적에 도움이 됩니다. 응답에는 DB 스키마·스택 등 **내부 구현 상세가 노출되지 않습니다** (보안 정책).

### Q44. 백업·감사 로그는 누가 보나요?

**A.** 고객 센터 **`sysadmin`**이 `/settings`에서 **자기 Tenant** 백업 상태·감사 로그를 조회합니다 (`GET /api/v1/settings/backups`, `/audit-logs`). 플랫폼 전체 백업 정책은 ogada 인프라 운영([`DEPLOYMENT_GUIDE.md`](ops/DEPLOYMENT_GUIDE.md) §8-2)을 따릅니다.

> **구현됨**: `SettingsController`, `BackupRunService`. MVP는 Tenant별 manifest 백업이며, 프로덕션 `pg_dump` 교체 예정.

### Q45. `hq_admin`과 센터장(`branch_admin`)의 차이는?

**A.** `hq_admin`은 **다지점 통합 조회·집계**, 지점·직원·**수가표** 관리가 가능합니다. 일상 CRUD는 **지점 선택기**로 고른 `active_branch_id` 지점만 수정할 수 있습니다. `branch_admin`은 **소속 지점 1곳** 운영 총괄이며 수가표 관리 권한은 없습니다. 상세는 [`USER_MANUAL.md`](ops/USER_MANUAL.md) §5를 참고하세요.

### Q46. 요양보호사는 무엇을 할 수 있나요?

**A.** **`caregiver`**는 **수기 출석**(체크인/아웃·결석)과 **건강 기록 입력**, 이용자 목록 **조회**가 주 업무입니다. 이용자 등록·청구·QR 생성은 할 수 없습니다. 파일럿 현장의 핵심 사용 역할입니다. [`USER_MANUAL.md`](ops/USER_MANUAL.md) §6 참고.

### Q47. 월별 출석 통계 API는 있나요?

**A.** **예.** `GET /api/v1/attendance/stats/monthly`로 지점·기간별 출석 통계를 조회합니다 (2026-06-06 구현). 프론트엔드 **`/attendance/stats` 화면은 등록**되어 있으나 쿼리·응답 구조 불일치로 숫자가 비어 있을 수 있습니다 (FAQ Q106). **지점 대시보드**(`/dashboard`)는 US-M02부터 실데이터 API와 연동됩니다 (Q85).

### Q48. 수가표를 수정하면 과거 청구에 영향을 주나요?

**A.** **아니요.** `PATCH /api/v1/billing/fee-schedules/{id}`는 **이력 보존** 방식으로 새 버전을 생성합니다. 이미 **확정**된 청구는 생성 시점의 수가 스냅샷(`daily_rate_snapshot`)을 유지합니다 (Flyway V8 확정 청구 불변성).

**적용일 규칙 (BE `06d68dd`)** — 새 버전의 **`effectiveFrom`** 은 **기존 버전 적용일 이후**여야 합니다. 과거 날짜로 소급 수정하려 하면 「새 수가표 적용일은 기존 버전 이후 날짜여야 합니다.」 오류가 반환됩니다. 종료된(`effectiveTo` 설정) 버전은 수정할 수 없습니다.

---

## 13-1. 파일럿 운영 (2026-06-06 신규)

### Q49. 파일럿 현장은 어떻게 진행되나요?

**A.** ogada는 **지점 2곳, 센터장 1명, 요양보호사 5명**이 참여하는 실제 운영 센터에서 테스트합니다 (REQUIREMENTS §1-3-1).

| 항목 | 내용 |
|------|------|
| **참여 역할** | `branch_admin`(센터장) + `caregiver`(요양보호사)만 |
| **검증 포인트** | 수기 출석·건강 기록 입력, QR 스캔, 2지점 전환 UX |
| **비참여** | `hq_admin`, `social_worker`, `guardian`, `sysadmin`(MVP 구현하되 현장 미참여) |
| **목표** | 기능 완성도·UX 피드백·운영 정책 확인 |

### Q50. 파일럿 후 무엇을 개선하나요?

**A.** 파일럿 피드백과 테스트 결과에 따라 다음을 우선 검토합니다.

1. **출석·건강 입력 UI** — 요양보호사 입장에서 가장 자주 쓰는 화면 개선
2. **QR 스캔 안정성** — 보호자·이용자 스마트폰 호환성
3. **다지점 전환 편의성** — `hq_admin` Branch Switcher UX
4. **성능** — 실제 데이터 규모에서 페이지 로딩 속도 (목표 3초 이내)
5. **보호자 알림** — 도착·귀가·건강 이상 알림 요구 확인

---

## 13-2. 청구·정산 구체 (2026-06-06 신규)

### Q51. 청구서 생성은 수동인가요?

**A.** **반반입니다.**

- **자동 생성**: `POST /api/v1/billing/claims/generate`로 월별(지점·년월 기준) 청구서를 **자동으로** 계산·생성합니다.
- **수동 조정**: `hq_admin`이 생성 후 상세 확인·수정 후 상태를 `확정`으로 변경합니다.
- **공단 업로드**: 확정된 청구서 데이터를 공단 포털에 수동으로 전송 (공단 직접 API는 후속).

### Q52. 공단 청구내역 import는 어떻게 하나요? (B방식 2단계 모델, 2026-06-06 신규)

**A.** ogada는 케어포 벤치마킹 **2단계 모델**로 청구를 처리합니다.

| 단계 | 주체 | 작업 | 결과 |
|------|------|------|------|
| ① **내부 계산** | ogada | 출석·등급·수가·부담률 → 청구서 생성 | `/api/v1/billing/claims/generate` 자동 계산·저장 |
| ② **공단 청구** | 공단 포털(롱텀) | 센터 직원이 공단 포털에서 청구 → 공단 심사·지급 | ogada 밖에서 수행 |
| ③ **대사 및 연동** | ogada + 공단 | 공단 「청구내역상세」엑셀 import → 대조 | `/api/v1/billing/imports/nhis` 상태 기록 |

**절차**

1. 월말에 센터장이 `/billing`에서 **청구서 생성** (`generate`) — 지점·연월·대상 이용자의 출석·등급을 기반으로 급여·부담금 계산
2. 공단 포털에서 센터 담당자가 청구 → 공단 심사 → 지급
3. 공단에서 **「청구내역상세」엑셀** 다운로드
4. ogada에서 `POST /api/v1/billing/imports/nhis`로 파일 업로드 → 행별 대사

### Q53. 공단 청구내역을 import하면 무엇이 되나요?

**A.** `POST /api/v1/billing/imports/nhis`로 공단 엑셀을 업로드하면:

1. **배치 생성** (`nhis_import_batches`) — 파일 메타·상태 기록
2. **행 단위 매칭** (`nhis_import_rows`) — 각 행을 `client_id` + 청구 라인과 매핑 (지점·인정번호 기준, V27 인덱스)
3. **상태 판정** — `MATCHED` / `UNMATCHED` / `DISCREPANCY` 부여
4. **`UNMATCHED` 보정** — `GET .../candidates` 후 `PATCH .../rows/{rowId}/match`로 수동 연결 (Q73)
5. **대사 리포트** — 불일치 내역 조회 후 수정·재import

요청 파라미터: `branchId`, `yearMonth`(YYYY-MM), (선택) `claimId`, `file`(xlsx).

### Q54. 본인부담금 계산 예시를 알려 주세요.

**A.** 다음 공식으로 자동 계산됩니다:

```
총 급여비용 = 이용자 등급 수가(수가표 조회) × 월 출석일수
본인부담금 = 총 급여비용 × 이용자 부담 구분 비율(copay_rates)
공단부담금 = 총 급여비용 - 본인부담금
```

예) 3등급 수가 68,000원/일, 월 20일 출석, 일반(15%) 부담

```
총액 = 68,000 × 20 = 1,360,000원
공단 = 1,360,000 × 85% = 1,156,000원
본인 = 1,360,000 × 15% = 204,000원
```

---

## 13-3. QR 체크인 상세 (2026-06-06 신규)

### Q55. 보호자가 QR을 스캔할 때 어떤 권한이 필요하나요?

**A.** **`guardian`(보호자) 계정**으로 로그인한 후 스캔합니다:

```
보호자 로그인(`guardian`) → `/guardian/checkin`으로 이동 → 지점 입구 QR 스캔
→ 연결된 이용자 중 대상 선택(1명) → 체크인/아웃 버튼
```

복수 이용자 보호 시 스캔 전 **「누가」선택** UI가 표시됩니다.

### Q56. 이용자 본인도 QR을 스캔할 수 있나요?

**A.** **조건부입니다.** Organization 설정 `allow_client_self_checkin`을 **on**으로 설정하면:

- 이용자 본인 계정(`client_user`) 발급 가능
- 본인도 `/guardian/checkin`과 동일한 화면에서 **자신만** QR 스캔 가능

대부분의 센터는 **보호자만**(기본값 off) 스캔하도록 운영합니다.

### Q57. QR이 만료되나요?

**A.** **예.** 지점 QR 토큰은 **유효 시간(분)**이 포함된 서명 토큰입니다.

| 항목 | 값 |
|------|-----|
| 기본 유효 시간 | **60분** (`DEFAULT_QR_EXPIRES_MINUTES`) |
| 생성 시 설정 범위 | 1–720분 (`POST /api/v1/branches/{id}/qr`의 `expiresInMinutes`) |
| 재조회 | `GET /api/v1/branches/{id}/qr` — 당일 유효 QR 출력·없으면 자동 재발급(60분) |

만료·위조 토큰 스캔 시 `422 BUSINESS_RULE` 오류가 반환됩니다. 센터 직원이 새 QR을 생성·게시하세요.

---

## 13-4. 마이그레이션 및 기술 (2026-06-06 신규)

### Q58. 기존 센터 데이터를 import할 수 있나요?

**A.** **현재는 불가능합니다.** MVP v1에는 데이터 마이그레이션 도구가 없습니다. 신규 고객 온보딩 시:

1. `platform_admin`이 새 Tenant 생성 (`POST /api/v1/platform/organizations`)
2. 센터장(`hq_admin`) 첫 계정 발급
3. 센터장이 수동으로 이용자·직원 등록

기존 ERP 데이터 대량 import는 **v1 이후 고객 요청 기반**으로 구현합니다.

### Q59. 데이터 백업은 어떻게 되나요?

**A.** 

| 주체 | 방식 | 주기 | 보관 |
|------|------|------|------|
| **ogada 플랫폼** | 자동 Tenant 격리 백업 | 일 1회 | 30일 |
| **고객 센터(`sysadmin`)** | `/settings` → 백업 이력 조회 | — | — |
| **프로덕션** | `pg_dump` (구현 예정) | 별도 정책 | 별도 정책 |

현재 MVP는 **파일 시스템 manifest 백업**이며, 프로덕션은 `pg_dump`로 교체할 예정입니다. V28에서 백업 대상 Tenant 스캔 인덱스가 추가되었습니다.

---

## 13-5. 이용자·보호자 API 보강 (2026-06-06 신규)

### Q60. 이용자 상세의 출석·청구 탭은 어떤 API를 쓰나요?

**A.** 이용자 프로필(`/clients/:id`) 탭별 전용 API가 **백엔드에 구현**되어 있습니다.

| 탭 | 백엔드 API | 권한 |
|----|-----------|------|
| 기본정보 | `GET /api/v1/clients/{id}` | 스코프 내 조회 |
| 출석 | `GET /api/v1/clients/{id}/attendance?from=&to=` | `hq_admin`, `branch_admin`, `social_worker`, `caregiver` |
| 청구 | `GET /api/v1/clients/{id}/billing` | `hq_admin`, `branch_admin` |
| 건강 | `GET /api/v1/clients/{id}/health` | caregiver 이상 |

| 탭 | UI 상태 (2026-06-06) |
|----|---------------------|
| **기본정보** | **연동됨** — 프로필·마스킹 주민번호·**[열람]** 버튼 |
| **청구** | **부분** — `GET /billing/claims?clientId=` 사용 → `GET /clients/{id}/billing` 정합 필요 (Q83) |
| **건강** | **부분** — `GET /clients/{id}/health` 호출·표 UI. `payload` vs flat 필드 불일치 (Q102) |
| **출석** | **부분** — `GET /attendance?clientId=` vs 정식 `GET /clients/{id}/attendance` (Q102) |

### Q61. 주민등록번호를 화면에서 풀 번호로 볼 수 있나요?

**A.** **법정 목적(청구·서류)** 에 한해 권한자가 복호화 열람을 요청할 수 있습니다.

| 항목 | 내용 |
|------|------|
| 백엔드 API | `POST /api/v1/clients/{id}/resident-registration/reveal` |
| 허용 역할 (API) | `branch_admin`, `social_worker`, `hq_admin` |
| UI **[열람]** 버튼 (2026-06-06) | `/clients/:id` 기본정보 탭 — **`branch_admin`·`hq_admin`만** 표시 |
| 감사 | `PII_DECRYPT_VIEW` — `audit_logs` 자동 기록 |
| 목록·일반 조회 | `******-*******` 마스킹 유지 |

> **경로 정합 (Q83)**: UI는 `GET /clients/{id}/ssn`을 호출합니다. 백엔드는 POST reveal만 제공 — **[열람] 클릭 실패 시** Swagger POST 또는 coder 정합을 요청하세요.

### Q62. 보호자 포털에서 오늘 기록은 어떻게 조회하나요?

**A.** 보호자·이용자 본인(`guardian`, `client_user`)은 **`/guardian`** 포털에서 확인합니다.

| UI (2026-06-06) | 설명 |
|-----------------|------|
| **오늘 현황** 탭 | 출석 상태·체온·혈압·건강 이상 알림 StatCard |
| **명세·청구** 탭 | 월별 본인부담 청구 표 (v1.1 UI) |
| 이용자 선택 | 복수 연결 시 상단 버튼으로 전환 |

**백엔드 정식 API**

| API | 용도 |
|-----|------|
| `GET /api/v1/guardian/checkin-targets` | 연결 이용자(체크인 대상) 목록 |
| `GET /api/v1/guardian/daily-records?clientId=<uuid>&date=YYYY-MM-DD` | 당일 출석·건강 요약 (`date` 생략 시 오늘) |
| `GET /api/v1/guardian/clients/{clientId}/billing` | 명세·청구 탭 — 월별 `yearMonth`, `claimStatus`, `copayAmount` (2026-06-06) |

> **경로 정합 (Q83)**: 프론트 `services.js`는 `/guardian/clients`·`/clients/:id/summary`를 호출합니다. 백엔드와 불일치 시 포털 로드 오류 — coder가 `checkin-targets`·`daily-records`로 정합하거나 백엔드 alias 추가 예정. **명세·청구 탭**은 `GET /guardian/clients/{clientId}/billing` 경로가 **일치**하나 UI 필드 매핑(`billingMonth`·`status`)은 Q98·Q102와 동일 이슈.

### Q63. platform_admin이 고객 센터를 검색할 수 있나요?

**A.** **예.** `GET /api/v1/platform/organizations?query=행복`처럼 **법인명·사업자번호 부분 검색**이 지원됩니다 (V27 법인명 trigram + V29 사업자번호 trigram). 사업자번호 **완전 일치**는 등록 시 UK로 중복 검증됩니다.

---

## 13-6. 계정·청구 DB 보강 (2026-06-06 신규)

### Q64. 같은 센터에 `Kim@center.com`과 `kim@center.com` 두 계정을 만들 수 있나요?

**A.** **아니요.** V30부터 Tenant(Organization) 내 직원 이메일은 **대소문자 무시 UK**(`uq_users_org_email_lower`)로 중복이 차단됩니다. `POST /api/v1/users` 저장 시 이메일은 trim+소문자로 정규화됩니다.

### Q65. 비밀번호를 재설정하면 다른 기기 로그인도 끊기나요?

**A.** **예.** 비밀번호 재설정 완료(`POST /api/v1/auth/password/reset`) 시 해당 계정의 **활성 refresh 토큰이 모두 폐기**됩니다 (V30). 다른 PC·스마트폰에서 로그인 중이었다면 **새 비밀번호로 다시 로그인**해야 합니다.

### Q66. 청구 목록을「확정」상태만 보려면 어떻게 하나요?

**A.** `GET /api/v1/billing/claims?status=CONFIRMED`로 **상태 필터**가 지원됩니다 (2026-06-06 API 구현, V31 인덱스 활용).

| API 값 | 화면 표기(예) | 의미 |
|--------|-------------|------|
| `DRAFT` | 작성중 | 검토·수정 가능 |
| `CONFIRMED` | 확정 | 명세서 출력·공단 청구 기준 확정 |
| `PAID` | 수납완료 | 본인부담금 수납 처리 완료 |

- `branchId`와 함께 사용: `?branchId=<uuid>&status=DRAFT`
- 잘못된 상태값은 `400` 오류
- **프론트엔드 UI 필터**: `/billing` 화면 상단 **상태 선택** 드롭다운으로 동일 필터 적용 (2026-06-06 UI 연동)

### Q67. 이용자에게 보호자가 여러 명일 때「대표 보호자」는 무엇인가요?

**A.** 이용자당 **대표 보호자(`is_primary`)는 1명**만 지정할 수 있습니다 (V7 UK). 새 보호자를 대표로 지정하면 기존 대표는 자동 해제됩니다 (`clearPrimaryForClient`, V31 인덱스). QR 체크인 대상 목록에서 대표 여부가 표시됩니다.

### Q68. 청구 상태를「작성중」에서 다시「작성중」으로 바꿀 수 있나요?

**A.** **아니요.** 동일 상태로의 변경(no-op)은 API에서 **`422 BUSINESS_RULE`**(`동일한 청구 상태로는 변경할 수 없습니다.`, **`b0a88ac` QA-B21 Fixed**)로 거부되며, V31 `chk_claim_status_history_distinct_transition` CHECK로 **상태 이력에도 기록되지 않습니다**. 실제 전이(`DRAFT→CONFIRMED→PAID`)만 허용됩니다.

---

## 13-7. Actor 감사·데이터 보존 (2026-06-06 신규)

### Q69. 출석·건강·청구 기록에「누가 입력했는지」남나요?

**A.** **예.** MVP에서 다음 컬럼에 **행위자 UUID**가 기록됩니다.

| 기록 | 컬럼 | 설정 방식 |
|------|------|----------|
| 출석(수기·QR·결석) | `attendance.created_by` | 앱 `DbSessionContext` + V32 DB 트리거 backstop |
| 건강 기록 | `health_records.recorded_by` | 앱 JWT subject + V33 트리거 backstop |
| 청구서 생성 | `billing_claims.generated_by` | 앱 + V32 트리거 backstop |
| NHIS import | `nhis_import_batches.imported_by` | 앱 + V33 트리거 backstop |
| **수가표 등록** | `fee_schedules.created_by` | V35 트리거 backstop (`createFeeSchedule` 앱 미설정) |
| **지점 QR 발급** | `branch_qr_tokens.created_by` | 앱 JWT subject + V35 트리거 backstop |

감사 로그(`audit_logs`)와 별도로, **엔티티 행에 직접 actor UUID**가 남아「누가 이 출석/기록을 만들었는지」추적할 수 있습니다. 로그·화면에는 UUID만 표시하고 PII는 노출하지 않습니다.

### Q70. 퇴소한 이용자 데이터는 언제 삭제되나요?

**A.** **퇴소 즉시 삭제되지 않습니다.** `DATA_RETENTION_POLICY` 기준 **퇴소 후 5년** 보관 후 purge 배치가 실행됩니다 (배치 자체는 후속 구현).

- V32 `idx_clients_org_discharged_at`: Tenant별 퇴소 cohort 스캔
- V33 `idx_attendance_client_purge` 등: cohort의 `client_id`로 child 행 일괄 삭제·익명화 스캔 지원
- 퇴소 처리 직후에는 **신규 출석·건강 기록 입력이 차단**됩니다 (V13 가드)

### Q71. NHIS import가 완료됐는데 `imported_at`이 비어 있으면?

**A.** V32 `trg_nhis_batches_set_imported_at` 트리거가 `status = COMPLETED`인데 `imported_at`이 NULL이면 **`created_at`(또는 NOW())로 자동 설정**합니다. JPA `@PrePersist` 우회·raw SQL에 대한 DB 방어입니다.

### Q72. 활성 이용자 목록이 느려질 수 있나요?

**A.** V33 `idx_clients_org_branch_active_created` partial 인덱스가 **지점별 활성 이용자 목록**(`GET /clients`, 검색어 없음) pagination을 지원합니다. 이름·인정번호 검색(`?q=`)은 V12/V26 trigram 인덱스를 사용합니다.

---

## 13-8. NHIS 수동 매칭·퇴소 무결성 (2026-06-06 신규)

### Q73. 공단 엑셀 import 후 `UNMATCHED` 행은 어떻게 처리하나요?

**A.** 자동 매칭(인정번호·이름·생년월일)에 실패한 행은 **수동 연결** API로 보정합니다.

| 단계 | API | 설명 |
|------|-----|------|
| 1 | `GET /api/v1/billing/imports/nhis/{batchId}` | 배치 상세·행별 `matchStatus` 확인 |
| 2 | `GET /api/v1/billing/imports/nhis/{batchId}/candidates?q=` | 같은 지점 소속 **후보 이용자** 검색 |
| 3 | `PATCH /api/v1/billing/imports/nhis/rows/{rowId}/match` | `{ "clientId": "uuid" }` — **단일 트랜잭션**으로 연결 |

연결 후 상태는 **`MATCHED`** 또는 금액·일수 차이 시 **`DISCREPANCY`**로 전환됩니다. 이미 `MATCHED`/`DISCREPANCY`인 행은 재연결할 수 없습니다 (`422 BUSINESS_RULE`).

> **구현됨**: `NhisImportService.matchRow()`. UI는 `/billing/imports/nhis` reconciliation 화면 후속.

### Q74. 퇴소 처리 시 과거 날짜로 퇴소 시각을 넣을 수 있나요?

**A.** **아니요.** V34 `chk_clients_discharged_after_created` CHECK로 **`discharged_at`은 `created_at` 이후**만 허용됩니다. API `POST /api/v1/clients/{id}/discharge`는 현재 시각(`NOW()`)을 기록하므로 정상 흐름에서는 위반되지 않습니다. 잘못된 SQL·백필은 DB에서 거부됩니다.

### Q75. 출석 API 경로에 `/check-in`과 `/checkin` 두 가지가 있나요?

**A.** **예, 동일합니다.** 하위 호환을 위해 다음 별칭이 모두 수용됩니다.

| 동작 | 경로 (동등) |
|------|------------|
| 수기 체크인 | `POST /api/v1/attendance/check-in` · `/checkin` |
| 수기 체크아웃 | `POST /api/v1/attendance/check-out` · `/checkout` |

API 명세·프론트엔드는 **하이픈 형식**(`/check-in`, `/check-out`)을 권장합니다.

### Q76. 수가표를 등록한 사람은 어떻게 확인하나요?

**A.** `fee_schedules.created_by` 컬럼에 **등록자 UUID**가 저장됩니다 (V35).

| 항목 | 내용 |
|------|------|
| API | `POST /api/v1/billing/fee-schedules` (`hq_admin`) |
| 앱 동작 | `BillingService.createFeeSchedule`은 `createdBy`를 앱에서 설정하지 않음 |
| DB 방어 | V35 `trg_fee_schedules_set_created_by`가 세션 actor(`ogada.actor_user_id`)로 자동 적재 |
| 활용 | 감사·분쟁 대응 —「누가 언제 수가 버전을 등록했는지」추적 |

지점 QR 발급(`branch_qr_tokens.created_by`)도 V35 동일 패턴으로 감사됩니다.

### Q77. Must 기능 중 아직 화면이 없는 것은 어떻게 쓰나요?

**A.** **백엔드 Must API는 구현 완료**입니다. 프론트 HEAD `42f48e1`는 **v1.2 P1 Must 화면** — **31 라우트**·**ModulePage 제거**·15 Must UI + P1–P8·J01·J02 REST (Q149·Q151).

| 화면 (등록됨) | UI 상태 | 백엔드 API |
|--------------|---------|-----------|
| `/login` | **JWT 로그인** | `POST /auth/login` |
| `/dashboard`, `/dashboard/hq` | **위젯 + HealthAlertList** | `GET /dashboard/branch`, `/hq` |
| `/clients`, `/clients/new`, `/clients/:id/edit` | **목록·등록·수정 폼** — 본문 필드 **불일치** (Q83·Q151) | `GET/POST/PATCH /clients` |
| `/clients/:id` | **상세 + 보호자 초대** | `GET /clients/{id}`, `…/guardians/invitations` |
| `/branches` | **`BranchesPage` CRUD UI** — 경로·페이지네이션 갭 (Q104·Q151) | `GET/POST/PATCH /branches` |
| `/guardians`, `/guardians/:id` | **보호자 목록·상세** | `GET /users?branchId=` 필터 |
| `/attendance`, `/attendance/checkin` | **당일 목록 + 입소·귀가·결석 버튼**(US-E01·E02) — roster·`status` 갭 (Q94) | `GET /attendance` |
| `/attendance/stats` | **`AttendanceStatsPage`** — `yearMonth` 쿼리 불일치 (Q106) | `GET /attendance/stats/monthly` |
| `/attendance/qr/generate` | **`QrGeneratePage`** — branch-scoped **Partial**(Q109) | `POST/GET /branches/{id}/qr` |
| `/attendance/checkin/qr` | **`GuardianCheckinPage`** — **Fixed** (Q109) | `POST /attendance/qr/scan` |
| `/health`, `/health/:clientId` | **목록 + 추이** — `payload` 매핑 갭 (Q119) | `GET /clients/{id}/health` |
| `/billing` | **청구 목록 + FilterChips** | `GET /billing/claims` |
| `/billing/claims/:claimId` | **`BillingDetailPage`** | `GET /billing/claims/{id}` |
| `/billing/imports/nhis`, `…/:batchId` | **import + reconciliation** | P7/P8 REST |
| `/billing/payments`, `/billing/overdue` | **입금·미납 UI** — **수납 POST·미납 pagination·notify Fixed**(Q174·Q196·Q197·Q198) · 전용 수납 목록 GET **갭** | 부분 |
| `/billing/fee-schedules`, `/copay-rates` | **수가·본인부담 표** — 경로·본문 불일치 (Q91·Q151) | `/billing/fee-schedules`, `/copay-rates` |
| `/platform`, `/settings` | **`PlatformPage`·`SettingsPage`** — API 경로 갭 (Q97·Q121·Q151) | `/platform/organizations`, `/organization/settings`, `/settings/*` |
| `/guardian` | **보호자 포털** (J02) | `GET /guardian/checkin-targets`, `/daily-records`, `/clients/{id}/billing` |
| `/guardian/invitations/:token/accept` | **공개 수락** | `POST /guardian/invitations/{token}/accept` |

**Swagger·Postman 우회 (쓰기·API 정합 필요 시)**

| 기능 | API | 비고 |
|------|-----|------|
| 수기 체크인/아웃·결석 | `POST /attendance/check-in`, `/check-out`, `/absence` | UI 버튼 **없음** (Q86) |
| Recharts 차트 | 대시보드·출석 통계·건강 추이 | **Fixed** (UXD-48, Q118·Q119) — 출석 통계 **API 응답 갭**(Q106)·건강 **기간 `?days=` 갭**(Q165) 잔존 |

미등록 Must 기능은 **Swagger UI**로 검증하세요.

---

## 13-9. 인증·DB 보강 (2026-06-06 신규)

### Q78. 로그인을 여러 번 시도하면 「요청이 너무 많습니다」 오류가 나요.

**A.** **인증 rate limit**이 적용됩니다 (`AuthRateLimitService`).

| 엔드포인트 | 기본 한도(분당) |
|-----------|----------------|
| 로그인 — IP | 30회 |
| 로그인 — 계정(이메일) | 10회 |
| refresh — IP | 40회 |
| refresh — 토큰 | 20회 |
| 비밀번호 재설정 요청 — IP | 20회 |
| 비밀번호 재설정 요청 — 계정 | 6회 |
| 비밀번호 재설정 확인 — IP | 20회 |
| 비밀번호 재설정 확인 — 토큰 | 8회 |

초과 시 `429 RATE_LIMITED` — 「요청이 너무 많습니다. 잠시 후 다시 시도해주세요.」 **1분 후 재시도**하세요. 운영 환경에서는 `AUTH_*_RATE_LIMIT_*` 환경변수로 조정합니다 (`DEPLOYMENT_GUIDE.md` §3-3).

### Q79. 이용자 등록 시 인정 시작일을 생년월일 이전으로 넣을 수 있나요?

**A.** **아니요.** V36 `chk_clients_ltc_cert_valid_from_after_birth` CHECK로 **인정 시작일(`ltc_cert_valid_from`)은 생년월일(`birth_date`) 이후**만 허용됩니다. 오타·잘못된 import는 DB에서 거부됩니다.

### Q80. PII 수집 동의 시각을 등록일 이전으로 넣을 수 있나요?

**A.** **아니요.** V36 `chk_clients_consent_after_created` CHECK로 **`consent_collected_at`은 `created_at` 이후**만 허용됩니다. 정상 등록 흐름(행 생성 → 동의 수령 → 동의 시각 기록)에서는 문제가 없습니다.

### Q81. NHIS import 배치를 청구서(`claimId`)별로 조회할 수 있나요?

**A.** **예.** `GET /api/v1/billing/imports/nhis?branchId=&claimId=` 필터가 지원됩니다 (V37 `idx_nhis_import_batches_org_branch_claim_created` 인덱스). 월별·지점별 목록과 함께 특정 청구서에 연결된 import 이력을 빠르게 조회할 수 있습니다.

### Q82. 프론트엔드 로그인은 JWT를 쓰나요?

**A.** **예.** 로그인 화면(`/`)에서 `POST /api/v1/auth/login`으로 access·refresh 토큰을 발급받습니다.

| 항목 | 상태 (FE `84e75ec`, SEC-005 + 결정 96) |
|------|----------------------------------------|
| JWT 로그인·역할 가드 | **구현됨** — `AuthContext` + `ProtectedRoute` + `roleNav.allowedRolesForPath` |
| access token 저장 | **메모리 전용** (`src/api/session.js`) — localStorage **미사용** |
| refresh token 저장 | **`sessionStorage`** — 키 **`ogada.refreshToken`** (탭 범위, SEC-005 예외) |
| 세션 지속 | **같은 탭** 새로고침·뒤로가기 → **`restoreSession()`** 으로 **로그인 유지** (Q396). **탭 닫기**·로그아웃 → 재로그인 |
| AppShell **로그아웃** | **구현됨** — `LogoutButton` + `POST /auth/logout` (Q141) |
| 지점 전환 | **`BranchSwitcher`** UI + `POST /auth/active-branch` (Q89) |
| idle 세션 | **`SessionTimeoutProvider`** — 30분 무활동·60초 경고 (Q112) |
| refresh 자동 갱신 | **부분** — `restoreSession()`·`refreshAccessToken()` 존재 · access 만료(30분) 중 API 401 시 재로그인 필요할 수 있음 |

### Q83. 화면은 있는데 API 호출이 실패합니다. 경로가 다른가요?

**A.** **예.** 2026-06-06 기준 프론트 `src/api/services.js`와 백엔드 구현 간 **경로·메서드 불일치**가 있습니다. coder 정합 전까지 Swagger·Postman으로 백엔드 정식 API를 사용하세요.

| 화면·기능 | 프론트 호출 (현재) | 백엔드 정식 API | 증상 |
|----------|-------------------|----------------|------|
| 이용자 상세 주민번호 [열람] | `GET /clients/{id}/ssn` | `POST /clients/{id}/resident-registration/reveal` | [열람] 클릭 시 404·405 |
| 이용자 상세 청구 탭 | `GET /billing/claims?clientId=` | `GET /clients/{id}/billing` | 청구 탭 빈 목록·전체 청구 혼입 |
| `/billing` 월·이용자 필터 | `GET /billing/claims?yearMonth=&clientId=` | `GET /billing/claims?branchId=&status=` (`yearMonth`·`clientId` **미지원**) | 월 선택이 목록에 반영되지 않음 |
| `/platform` 고객 검색 | `GET /platform/organizations?q=` | `GET /platform/organizations?query=` | 검색어 무시·전체 목록 |
| 이용자 등록·수정 (`/clients/new`) | ~~`ssnConsentGiven`·`guardianName`~~ → **정합됨 (UXD 10차)** | `consentToCollectResidentRegistrationNo`·`primaryGuardian` 전송. **`issueClientUser`·사진·`notes` 미연동**(Q113) |
| 보호자 포털 목록·요약 | `GET /guardian/clients`, `GET /guardian/clients/{id}/summary` | `GET /guardian/checkin-targets`, `GET /guardian/daily-records?clientId=` | 포털 로드 오류 |
| 보호자 명세·청구 탭 | `GET /guardian/clients/{id}/billing` | 동일 경로 **구현됨** | UI가 `billingMonth`·`status` 표시 시 빈 칸 (Q98·Q102) |
| 플랫폼 목록 페이지네이션 | `?page=&size=` 전송 | `List` 반환(페이지 필드 없음) | 페이지 UI만 동작, 실제 분할 없음 |
| 청구 목록 페이지네이션 | `?page=&size=` 전송 | `?branchId=&status=`만 지원 | 페이지 UI만 동작 |
| 출석 목록 필드 | `name`, `status`, `checkInTime`, `checkOutTime`, `PENDING` | `clientId`, `checkInAt`, `checkOutAt`, 상태 없음, **기록 있는 행만** | 이름·시각 빈칸, 체크인 버튼 미노출 (FAQ Q94) |
| 체크아웃 교통편 | `transportMethod`: "자가용" 등 | `transportType`: `SELF`/`CENTER_VEHICLE`/`WALK`/`OTHER` | 교통편 미저장 (FAQ Q96) |
| 건강 투약 | `drugName`, `administeredAt`(시간), `notes` | `recordedAt`, `medicationName`, `administeredAt`(ISO), `administeredBy` | `400 VALIDATION_ERROR` (FAQ Q95) |
| 건강 사고 | `eventType`, `description`, `occurredAt` | `recordedAt`, `incidentType`, `detail` | `400 VALIDATION_ERROR` (FAQ Q95) |
| 바이탈 `notes` | 전송함 | `VitalsCreateRequest`에 필드 없음 | 메모 무시 |
| 플랫폼 목록 응답 | `{ items, totalPages }` 기대 | `List` 직접 반환 | **빈 테이블** (FAQ Q97) |
| 플랫폼 hq_admin 발급 | `{ email }` | `{ email, password, displayName }` | 발급 실패 (FAQ Q97) |
| 청구 월 표시 | `claim.billingMonth` | `yearMonth` | 월 컬럼 빈칸 (FAQ Q98) |
| 보호자 요약 필드 | `attendanceStatus`, `bloodPressure`, `healthAlerts` | `attendance.status`, `health.systolic/diastolic`, `health.alerts` | 경로 수정 후에도 빈 요약 (FAQ Q99) |
| NHIS import 이력 (`/billing/nhis-import`) | `targetMonth`, `totalRows`, `matchedRows`, `branchName` | `yearMonth`, `rowCount` (요약에 matched·지점명 없음) | 대상 월·행수·지점 빈칸 (FAQ Q100) |
| NHIS 대사 배치 요약 | `batch.targetMonth`, `batch.branchName` | `yearMonth`, `branchId`만 | 상단 요약 빈칸 (FAQ Q101) |
| NHIS 대사 행 | `name`, `billingDays`, `billingAmount`, `diffAmount` | `ltcCertNo`, `serviceDays`, `nhisAmount`, `amountDifference` | 이름·일수·금액·차이 빈칸 (FAQ Q101) |
| 이용자 청구 탭 상태 | `status` | `claimStatus` | 상태 Badge 빈값 (FAQ Q102) |
| 출석 통계 (`/attendance/stats`) | `?branchId=&yearMonth=`, 응답 `{ summary, clients }` | `?from=&to=&branchId=`, 응답 `{ from, to, branches: [{ months: [...] }] }` | 요약·이용자별 표 빈칸 (FAQ Q106) |
| 이용자 상세 건강 탭 | `row.systolic`, `row.temperature` 등 flat 필드 | `{ items: [{ recordType, payload, recordedAt }] }` | API 성공해도 **혈압·체온 열 `-`** (FAQ Q102) |
| 이용자 상세 출석 탭 | `GET /attendance?clientId=&from=&to=` | `GET /clients/{id}/attendance?from=&to=` (`clientId`·기간 쿼리 **미지원**) | 출석 탭 **빈 목록** 또는 당일 지점 전체 행 (FAQ Q102) |
| 비밀번호 변경 (`SettingsPage`·`LoginPage`) | `POST /auth/change-password` | **`POST /auth/change-password` Fixed** (`fe5b38b`, Q122) | **Fixed** — `mustChangePassword`·보안 탭 모달 |
| ~~비밀번호 재설정 요청~~ | ~~`POST /auth/password-reset/request`~~ | `POST /auth/password/reset-request` | **Fixed** (`3803247`, Q126) |
| ~~로그인 이력 (`/settings` 탭)~~ | `GET /auth/login-history` | 동일 | **조회 Fixed** — UI 필터는 클라이언트 측 (Q121) |
| ~~백업 설정 토글~~ | `PATCH /settings/system` `{ backupEnabled }` | 동일 | **Fixed** (Q121) |
| 수동 백업 트리거 | `POST /settings/backup/trigger` | **미구현** | 수동 백업 버튼 실패 (Q121) |
| 감사 로그 필터 | UI `eventType`·`from`/`to` | API `?page=&size=`만 | **목록 Fixed** — 필터는 클라이언트 측 (Q121) |
| 플랫폼 관리자 발급 (`PlatformOrgDetailModal`) | `{ email }` | `{ email, password, displayName }` **필수** | 발급 `400` (Q127·Q97) |
| **지점 등록 (`BranchesPage`)** | `POST /branches` `{ name, address, phone, licenseNo }` | `POST /branches` `{ name, address?, phone?, … }` | 필드명·응답 래퍼 갭 (Q151) |
| **수가표 (`FeeSchedulePage`)** | `GET /billing/fee-schedule` | `GET /billing/fee-schedules?year=` | **404** — 경로·복수형 (Q151) |
| **조직 설정 (`SettingsPage`)** | `GET/PATCH /settings/organization` | `GET/PATCH /organization/settings` | 설정 저장 **404** (Q151) |
| **QR 생성 (`QrGeneratePage`)** | `POST /branches/current/qr` `{ type, validMinutes }` | `POST /branches/{branchId}/qr` `{ direction, expiresInMinutes }` | QR 생성 실패 (Q109·Q151) |
| **QR 스캔 (`GuardianCheckinPage`)** | `POST /attendance/qr/scan` `{ token, type }` | `{ qrToken, clientId, transportType? }` | 스캔 실패 (Q109·Q151) |
| **이용자 등록 (`ClientFormPage`)** | `birthdate`·`ssn`·`ssnConsent`·`primaryGuardian.name/phone` | `birthDate`·`residentRegistrationNo`·`consentToCollectResidentRegistrationNo`·`primaryGuardian.guardianUserId` | 등록 **400** (Q151) |

**역할 가드 불일치** (경로가 아닌 권한):

| 화면 | `ProtectedRoute` 허용 역할 | 백엔드 API 실제 권한 | 증상 |
|------|---------------------------|---------------------|------|
| `/settings` | `sysadmin`, `hq_admin` | `SettingsController` — **`SYSADMIN`만** | `hq_admin`이 화면 진입 후 API 403. `platform_admin`은 라우트 가드에서 **차단** (`/forbidden`, FAQ Q87) |
| `/billing/fee-schedules` | `hq_admin`, `platform_admin` | 수가표 API — **`HQ_ADMIN`만** | `platform_admin` 403 |

정합 작업은 프론트 `services.js` 수정 또는 백엔드 alias·쿼리 파라미터 수용 중 택일 — `PLAN_NOTES.md` §문서 작성 질문 TWR-Q1 참고.

### Q84. 역할마다 보이는 메뉴는 어디서 정의되나요?

**A.** 프론트 **`src/layout/navConfig.js`**의 `navGroupsForRole()`이 JWT `role`별 **2단 SideNav**(US-UX-02)를 결정합니다. `AppShell` 좌측 `SideNav`가 **운영·출석·기록·청구** 그룹으로 render됩니다. `ProtectedRoute`는 `roleNav.js`의 `allowedRolesForPath()`로 경로별 역할을 검사합니다.

| 역할 | SideNav 그룹 (FE `42f48e1`) |
|------|----------------------------|
| `branch_admin` | 운영(대시보드·지점·이용자·보호자) · 출석(현황·수기 체크인·통계·QR) · 기록 · 청구 |
| `social_worker`, `caregiver` | 운영 · 출석 · 기록 (청구 **없음**) |
| `hq_admin` | 운영(통합 대시보드·지점·이용자·보호자) · 출석 · 기록 · 청구(수가표·본인부담 포함) |
| `guardian`, `client_user` | 운영(보호자 포털) |
| `platform_admin` | 운영(플랫폼·통합 대시보드) |
| `sysadmin` | 운영(시스템 설정) — **라우트 가드는 `sysadmin`만** (`hq_admin` 메뉴 노출 시 `/forbidden`, Q87) |

**SideNav에 없는 Must 화면** — 목록 **행 클릭** 또는 버튼 링크로 진입:

| 화면 | 진입 경로 |
|------|----------|
| NHIS import | `/billing` → **「NHIS 엑셀 import (P7)」** |
| NHIS reconciliation | `/billing/imports/nhis` 배치 링크 → `/billing/imports/nhis/:batchId` |
| 이용자 상세·초대 | `/clients` 목록 링크 → `/clients/:id` |
| 보호자 초대 수락 | 이메일 링크 → `/guardian/invitations/:token/accept` (공개) |

### Q85. 대시보드(`/dashboard`) 숫자가 실제와 다릅니다. API는 있나요?

**A.** **FE `a53db39` (US-M02·US-L02)** — `DashboardPage`가 **`GET /api/v1/dashboard/branch`**·**`/dashboard/hq`** 와 연동되어 **`DashboardWidgetGrid`**·**`HealthAlertList`**를 표시합니다.

| 역할 | API | 화면 표시 |
|------|-----|----------|
| 센터장·요양보호사 등 | `GET /dashboard/branch` | 입소·결석·건강 알림·NHIS 미매칭·미처리·NHIS 대기(보류) 위젯 + 건강 이상 목록 |
| 센터장·통합 관리자 | 위 + 병렬 NHIS·미납 조회 | **「미납 본인부담」** 7번째 위젯 — `overdueCount` · `/billing/overdue` (Q202) |
| 통합 관리자 | `GET /dashboard/hq` + alerts | 전 지점 집계 + 동일 위젯 세트 |

**BE `f755428`·`15b3c7e` (Q282)**: `GET /dashboard/branch` 응답에 **`nhisUnmatchedCount`·`pendingReviewCount`·`overdueCount`·`monthlyCapWarningCount`** 가 포함됩니다. **`GET /dashboard/hq`** 는 전 지점 **NHIS·미납·월한도** 집계를 동일 필드로 반환합니다. FE는 현재 NHIS 배치·미납·월한도 API를 **병렬 조회**하며, 스냅샷 필드는 **`dashboardSummary.js` 폴백**으로 사용합니다 (Q183·Q202).

**BE `7ba18c1`·`70d76a4`·FE `8fa9f3d` (Q280·Q282)**: **`GET /dashboard/branch`**·**`/dashboard/hq`** 응답에 **G17·G32·G38·G39 준수지표 위젯 count·met 필드**가 **스냅샷**으로 내장됩니다. **`DashboardPage`** 는 **도메인별** `hasSnapshotFields()` 로 스냅샷이 있는 준수지표만 **별도 compliance API를 생략**하고, **누락된 도메인만** `fetchCaseManagementComplianceApi` 등 **폴백**을 호출합니다. compliance API 실패 시 **partial-load warning**이 표시됩니다 (`4b2b082`, Q277).

**Recharts 차트 (UXD-48, `8a764df`)**: 지점 **`AttendanceRateChart`**·통합 **`BranchCompareChart`** 가 대시보드 하단에 표시됩니다 (Q118). 위젯 클릭 시 `/attendance`·`/health`·`/billing` 등으로 이동합니다.

숫자가 `—`이면 당일 기록 없음·JWT 만료·지점 스코프 오류를 확인하세요. Swagger로 동일 API를 대조합니다.

### Q86. 출석 화면에서 결석 사유·체크인 버튼이 없어요.

**A.** **FE `a627c6d` (US-E01·E02)** — `/attendance`·`/attendance/checkin`에 **입소·귀가·결석 버튼**과 `CheckoutModal`·`AttendanceAbsentModal`이 추가되었습니다.

| 항목 | UI (2026-06-07) | 백엔드 API | 잔여 갭 |
|------|----------------|-----------|---------|
| 목록 | StatCard 요약 + 이용자별 **입소/귀가/결석** 버튼 | `GET /attendance` | **`status`·`clientName` 미제공** → 이름 UUID·버튼 미노출 가능 (Q94) |
| 체크인 | **입소** 버튼 | `POST /attendance/check-in` `{ clientId }` | ✅ 경로·본문 정합 |
| 체크아웃 | **귀가** → 교통편 모달 | `POST /attendance/check-out` `{ clientId, transportType }` | 프론트 **`transportMethod`** 필드명 (Q96) |
| 결석 | **결석** → 사유 모달 | `POST /attendance/absence` | ✅ |

> **roster 갭**: API는 **당일 출석 기록이 있는 행만** 반환 — 미처리 이용자는 목록에 **없음**(Q94). 파일럿 수기 출석은 Swagger 또는 roster API 확장 후속.

---

## 13-10. 프론트 라우트·UX 갭 (2026-06-07 신규)

### Q87. `/settings`에 들어갔는데 「권한이 없습니다」가 나와요. `hq_admin`인데요.

**A.** **FE `f749311` (Q178 Fixed)** — **`/settings`는 `sysadmin` 전용**입니다. **`hq_admin`은 `/organization/settings`** 를 사용하세요.

| 역할 | 화면 | 경로 | API |
|------|------|------|-----|
| **`sysadmin`** | 시스템 설정 | `/settings` | 백업·감사·로그인 이력·비밀번호 (`/settings/*`, **`SYSADMIN` only**) |
| **`hq_admin`** | 조직 설정 | **`/organization/settings`** | **`GET/PATCH /organization/settings`** — 셀프 QR 체크인 등 **운영 정책** |

| 계층 | `/settings` 접근 |
|------|-----------------|
| `App.jsx` `ProtectedRoute` | **`sysadmin` only** (`hq_admin` → `/forbidden`) |
| `SettingsController` (`/settings/*`) | **`SYSADMIN` only** (`@PreAuthorize`) |

**`hq_admin` 조직 정책 변경** — SideNav **조직 설정** → **`OrganizationSettingsPage`** — **`allowClientSelfCheckin` Switch 저장 Fixed**(Q116). **`platform_admin`** 은 `/settings`·`/organization/settings` 모두 **차단**됩니다.

> 관련: Q116 · Q178 · USER_MANUAL §5-5 · ADMIN_GUIDE §6-3

### Q88. 메뉴에 있는데 「페이지를 찾을 수 없습니다」/로그인으로 돌아가요. 라우트가 없나요?

**A.** **FE `73f7d39`** 기준 **대부분 경로는 `App.jsx`에 등록**되었습니다. **직원 관리**는 `/staff`(`StaffPage`)로 등록되었으며, `/users` URL은 **미등록**입니다 (Q162).

| 경로 | Must 여부 | UI (2026-06-08) | 백엔드 API |
|------|----------|-----------------|-----------|
| `/staff` | Should (§3-8) | **`StaffPage`** — **`StaffRoleSelect`**·필드 검증·등록 모달 (Q162) | `GET/POST /users` |
| `/users` | — | **미등록** — `/staff` 사용 | `/users` CRUD |

**등록됨·API 미연동 (화면은 열리나 동작 안 함)**

| 경로 | UI | 백엔드 API | 비고 |
|------|-----|-----------|------|
| `/attendance/qr/generate` | `QrGeneratePage` — 유형 선택·인쇄 레이아웃 | `POST/GET /branches/{id}/qr` | **QR 생성 버튼 TODO** (FAQ Q105) |
| `/guardian/checkin` | `GuardianCheckinPage` — 대상 선택·스캔 버튼 | `GET /guardian/checkin-targets`, `POST /attendance/qr/scan` | **카메라·API TODO** (FAQ Q105) |
| `/billing/fee-schedules` | `FeeSchedulePage` — 등급별 입력 폼 | `GET/POST/PATCH /billing/fee-schedules` | **저장·조회 미연동** (FAQ Q91) |
| `/billing/copay-rates` | `CopayRatePage` — 4구분 비율 폼 | `GET/PATCH /billing/copay-rates` | **저장·조회 미연동** |
| `/settings` | `SettingsPage` — Switch·`BackupSettingsPanel`·`AuditLogPanel` (Q121) | `/settings/*` (**`SYSADMIN`만**) | **API 미연동·역할 불일치** (FAQ Q87) |
| `/health/:clientId` | `HealthDetailPage` — `HealthTrendChart` | `GET /clients/{id}/health?days=` | **API 호출·`payload` 매핑 갭** (FAQ Q119) |

SideNav **「QR 생성」**·**「QR 체크인」**·**「수가표 관리」** 등은 이제 **404 없이** 해당 화면으로 이동합니다. 실제 업무 처리는 Swagger 또는 coder API 연동 완료 후 가능합니다.

### Q89. 지점 선택기에 지점명이 아니라 긴 영문·숫자(UUID)만 보여요.

**A.** **2026-06-07 US-M02**부터 `/dashboard`·`/attendance`·`/guardians`는 마운트 시 `GET /api/v1/branches`를 호출해 **지점명**을 표시합니다.

| 화면 | 지점명 표시 | 비고 |
|------|:----------:|------|
| `/dashboard`, `/attendance`, `/guardians` | ✅ | `fetchBranchesApi` → `branch.name` |
| `/billing`, `/health` 등 | ❌ | JWT `branchIds`를 UUID 라벨로 폴백 |

| 항목 | 내용 |
|------|------|
| 동작 | 지점 전환은 `POST /auth/active-branch`로 **정상** |
| API 실패 시 | 네트워크·권한 오류면 **UUID 폴백** — 새로고침 또는 Swagger `GET /branches` 대조 |
| 수정 | 나머지 Must 화면에 `fetchBranchesApi` 확산 예정 |

### Q90. 로그인 화면에 「비밀번호 찾기」가 없어요.

**A.** **FE `3803247` (SEC-D17 Fixed)** — 로그인 화면(`/`) 하단 **「재설정 요청」** 링크·`PasswordResetRequestModal`이 **`POST /auth/password/reset-request`** 를 호출합니다 (FAQ **Q126 Fixed**).

| API (백엔드 정식) | 용도 |
|-------------------|------|
| `POST /api/v1/auth/password/reset-request` | 등록 이메일로 재설정 링크 발송 |
| `POST /api/v1/auth/password/reset` | 토큰으로 새 비밀번호 설정 |

비밀번호 분실 시 로그인 화면 **「재설정 요청」** 또는 **`sysadmin` `/settings` → 보안** 탭을 사용하세요. 재설정 완료 시 **모든 refresh 세션이 폐기**됩니다 (FAQ Q65). **로그인 중 비밀번호 변경**은 **`POST /auth/change-password`** (**Fixed**, Q122).

### Q91. 수가표·본인부담 비율은 화면 없이 어떻게 등록하나요?

**A.** **수가표는 화면 연동 Fixed (FE `3f96d95`, G9)** — `/billing/fee-schedules`(`FeeSchedulePage`)에서 **`FeeScheduleMatrix`** 2차원 표·**「공단 2026 수가 시드」**·등록·수정·목록·이력 보기가 `fetchFeeSchedulesApi`·`upsertFeeScheduleApi`·`fetchFeeScheduleHistoryApi`로 동작합니다. **이용시간 밴드**(`durationBand`) 선택이 필수 차원입니다 (FAQ **Q210–Q214**). **본인부담 비율**(`/copay-rates`)은 **저장 API 미연동**이 남아 있습니다 — Swagger 우회.

**수가표 등록 (화면 또는 Swagger)** — `POST /api/v1/billing/fee-schedules`

```json
{ "year": 2026, "ltcGrade": 3, "durationBand": "H10_13", "dailyRate": 68000, "effectiveFrom": "2026-01-01" }
```

**본인부담 비율 확인·수정** — `GET /api/v1/billing/copay-rates`, `PATCH /api/v1/billing/copay-rates/{copayType}`

```json
{ "rate": 0.15 }
```

등록 시 `fee_schedules.created_by`에 행위자 UUID가 자동 기록됩니다 (V35). 월말 청구 전 **해당 연도·등급·이용시간 밴드** 수가가 1건 이상 있어야 `POST /billing/claims/generate`가 성공합니다. 이용자의 `durationBand`와 일치하는 수가가 없으면 청구 생성이 실패합니다 (G9).

### Q92. 이용자 등록 화면에서 「저장 실패」·「동의가 필요합니다」가 나와요.

**A.** **2026-06-07 UXD 10차** 이후 `/clients/new`(`ClientFormPage`)는 백엔드 `CreateClientRequest`와 **핵심 필드가 정합**됩니다. 아래 조건을 충족하면 등록이 성공하고 `guardian_link_status`가 **`LINKED`**로 설정됩니다 (V39).

| UI 입력 | API 전송 | 비고 |
|---------|---------|------|
| 주민번호 + 동의 체크 | `residentRegistrationNo` + `consentToCollectResidentRegistrationNo: true` | 동의 없으면 저장 버튼 비활성 |
| **기존 보호자** 드롭다운 | `primaryGuardian: { guardianUserId, relationship }` | `GET /users?branchId=`로 `guardian` 역할 목록 로드 |
| **「신규 보호자 계정 생성」** 체크 | `POST /users`(guardian) → `POST /clients` | 이메일·임시 비밀번호(8자+)·관계 필수 |
| `CopayTypeSelect` | `copayType` (`GENERAL` 등) | 비율 help 텍스트 표시 |

**여전히 UI-only (저장 후 별도 API 필요 — FAQ Q113)**

| UI | 미연동 API |
|----|-----------|
| 「이용자 본인 계정 발급」체크 + 이메일 | `POST /clients/{id}/client-user` |
| 프로필 사진 선택 | `POST /clients/{id}/photo` (multipart) |
| 특이사항 메모 | *(백엔드 필드 없음 — 무시)* |

**수정 모드(`/clients/:id/edit`)**

- `PATCH /clients/{id}` — 기본·장기요양·동의(주민번호 재입력 시) 정상.
- **보호자 연결 변경**은 폼에서 안내하듯 상세 화면·`POST /clients/{id}/guardians` 사용.

**Swagger 우회 (레거시·자동화)**

1. `POST /api/v1/users` — 보호자(`guardian`) 계정 생성.
2. `POST /api/v1/clients` — `primaryGuardian` 포함:

```json
{
  "branchId": "<uuid>",
  "name": "홍길동",
  "birthDate": "1945-03-02",
  "gender": "M",
  "phone": "010-0000-0000",
  "address": "서울시 ...",
  "residentRegistrationNo": "450302-1234567",
  "consentToCollectResidentRegistrationNo": true,
  "ltcGrade": 3,
  "ltcCertNo": "L0000000000",
  "ltcCertValidFrom": "2026-01-01",
  "copayType": "GENERAL",
  "primaryGuardian": {
    "guardianUserId": "<guardian-uuid>",
    "relationship": "자녀"
  }
}
```

### Q93. URL을 직접 입력했더니 「권한이 없습니다」(`/forbidden`) 화면이 나와요.

**A.** **역할과 경로가 맞지 않을 때** `ProtectedRoute`가 `/forbidden`(`ForbiddenPage`)으로 보냅니다. 로그인 화면(`/`)으로 돌아가는 **미등록 라우트(Q88)** 와 다릅니다.

| 상황 | 이동 경로 | 화면 |
|------|----------|------|
| 미로그인 | 보호 경로 접근 | `/` 로그인 |
| 로그인했으나 역할 불일치 | 예: `caregiver`가 `/billing` 직접 입력 | `/forbidden` |
| 라우트 미등록 | 예: `/users`(직접 입력) | `/` (fallback) |

**조치**: SideNav 메뉴·역할별 홈(`AuthContext` `roleHomePaths`)으로 이동하세요. 권한 변경이 필요하면 센터 **`hq_admin`**에게 역할 수정을 요청합니다.

---

## 13-11. 프론트 응답·본문 정합 (2026-06-07 6차)

### Q94. 출석 화면에 이용자 이름이 없고 체크인 버튼이 안 보여요.

**A.** **FE `a627c6d`** — 입소·귀가·결석 **버튼 UI는 추가**(US-E01·E02)되었으나, 백엔드 `AttendanceItemResponse`와 **필드·roster 구조 불일치**가 잔존합니다 (Q83 확장).

| 프론트 기대 | 백엔드 실제 | 증상 |
|------------|------------|------|
| `clientName`, `status`(`CHECKED_IN`/`CHECKED_OUT`/`ABSENT`) | `clientId`만, **`status`·이름 없음** | 이름 UUID·**모든 행「미처리」** → 버튼 미노출 가능 |
| `checkInTime`, `checkOutTime` | `checkInAt`, `checkOutAt`(ISO 8601) | 시각 열 빈칸 |
| 당일 **전체 이용자** 명단 | **당일 출석 기록이 있는 행만** 반환 | 미처리 이용자가 목록에 **아예 없음** |

**우회 (파일럿 수기 출석)**

1. **지점 선택기**로 작업 지점을 확인합니다.
2. `/clients`에서 이용자 **이름·UUID**를 확인합니다 — 목록에 없으면 `GET /api/v1/clients?branchId=<uuid>&q=이름`으로 검색.
3. Swagger **Authorize**에 `caregiver` 또는 `branch_admin` JWT를 입력합니다.
4. **입소**: `POST /api/v1/attendance/check-in` — `{ "clientId": "<uuid>" }` (별칭 `/checkin` 동일).
5. **귀가**: `POST /api/v1/attendance/check-out` — `{ "clientId": "<uuid>", "transportType": "SELF" }` (FAQ Q96).
6. **결석**: `POST /api/v1/attendance/absence` — `{ "clientId": "<uuid>", "reason": "개인사정" }`.
7. `/attendance`를 **새로고침**하면 해당 이용자 행이 표시될 수 있으나, **이름·상태 갭**으로 버튼이 여전히 비활성일 수 있습니다 — 4~6단계 Swagger가 **정식 API**입니다 (USER_MANUAL §4-4).

> coder 정합: `GET /clients?branchId=` roster와 출석 행을 병합하거나, 백엔드가 전체 roster+상태를 반환하도록 확장 예정 (`PLAN_NOTES.md` TWR-Q1).

### Q95. 건강 기록「투약」「바이탈」저장이 실패합니다.

**A.** **FE `95b92b9` (Q154 Fixed + UXD-41)** — `/health` **`VitalsRecordForm`**·**`MedicationRecordForm`**·**`IncidentRecordForm`** 이 **`healthApiPayload.js`** 로 백엔드 DTO와 **정합**됩니다. UI에서 **정상 저장**이 가능합니다.

| 유형 | 폼 → API (`healthApiPayload.js`) | 백엔드 기대 |
|------|----------------------------------|------------|
| **바이탈** | `bloodSugar`(폼) → **`bloodGlucose`**, **`recordedAt`** 자동(KST ISO) | `recordedAt`, `systolic`, `diastolic`, `temperature`, `bloodGlucose`, `spo2` |
| **투약** | `scheduledTime` → **`administeredAt`**, JWT `user.name` → **`administeredBy`**, **`recordedAt`** 자동 | `recordedAt`, `medicationName`, `dosage`, `administeredAt`, `administeredBy` |
| **사고** | **`IncidentRecordForm`** — `description` → **`detail`**, `occurredTime` → **`recordedAt`**, `incidentType` (`FALL`/`ACCIDENT`/`SYMPTOM`/`OTHER`) | `recordedAt`, `incidentType`, `detail` — **`POST …/health/incidents`** (Q154·UXD-41) |

> **여전히 실패할 때** — 필수 항목 누락·퇴소 이용자·세션 만료. **`400 VALIDATION_ERROR`** 시 Swagger로 본문 확인.

> **투약 중복** — `MedicationDuplicateAlert`가 **클라이언트 측** 동일 약품·시간 중복을 차단합니다. 서버 `409`도 동일 UI로 표시됩니다.

> **바이탈 저장 성공 시** J03 **`DAILY_CARE` 알림 dispatch** (Q147). **낙상(`FALL`) 사고 저장 시** **`EMERGENCY` dispatch** — 방해 금지(22:00–08:00) **우회**(Q147·Q156). **비정상 수치 경고**는 UXD-40(Q155) — 저장은 **차단하지 않음**.

**Swagger 참고 — 사고** `POST /api/v1/clients/{id}/health/incidents`

```json
{
  "recordedAt": "2026-06-06T14:30:00+09:00",
  "incidentType": "FALL",
  "detail": "복도에서 미끄러짐, 경상"
}
```

> 바이탈 폼의 `notes`는 `VitalsCreateRequest`에 **필드가 없어** 저장되지 않습니다. 특이사항은 `POST .../health/notes` API를 사용하세요.

### Q96. 체크아웃 후 귀가 교통편이 저장되지 않아요.

**A.** **FE `a627c6d`** — `CheckoutModal`이 **`CENTER_VEHICLE`·`SELF` 등 코드**를 전송하도록 개선(US-E01)되었으나, **필드명**이 백엔드와 다릅니다.

| 프론트 (현재) | 백엔드 |
|------|--------|
| `transportMethod`: `CENTER_VEHICLE`, `SELF`, `FAMILY`, `OTHER` | `transportType`: 동일 코드값 |

프론트가 **`transportMethod`** 키로 전송하면 백엔드는 **`transportType`** 만 인식 — 교통편 **미저장** 가능.

**Swagger**: `POST /api/v1/attendance/check-out`

```json
{ "clientId": "<uuid>", "transportType": "SELF" }
```

| 코드 | 의미 |
|------|------|
| `SELF` | 자가용·도보 |
| `CENTER_VEHICLE` | 센터 차량 |
| `FAMILY` | 보호자 동행 |
| `OTHER` | 기타 |

### Q97. `/platform` 고객 목록이 비어 있거나 hq_admin 발급이 실패해요.

**A.** **응답 래퍼**와 **관리자 발급 본문** 두 가지 불일치가 있습니다.

| 문제 | 프론트 | 백엔드 | 증상 |
|------|--------|--------|------|
| 목록 | `result.items` 기대 | `List<OrganizationResponse>` **직접 반환** | API 성공해도 **빈 테이블** |
| hq_admin 발급 | `{ email }` | `{ email, password, displayName }` **필수** | `400 VALIDATION_ERROR` |

**Swagger 우회**

1. `GET /api/v1/platform/organizations?query=행복` — JSON **배열** 직접 수신.
2. Tenant 생성 후 `POST /api/v1/platform/organizations/{orgId}/admins`:

```json
{
  "email": "kim@happy-care.com",
  "displayName": "김센터장",
  "password": "<초기 비밀번호>"
}
```

> 상세 절차는 [`ADMIN_GUIDE.md`](ops/ADMIN_GUIDE.md) §3-2. 검색 파라미터 `?q=` vs `?query=` 불일치는 Q83 참고.

### Q98. 청구 목록「대상 월」컬럼이 비어 있어요.

**A.** API 응답 필드는 **`yearMonth`**(예: `"2026-05"`). 프론트 `BillingPage`·`ClientDetailPage`·`GuardianPage`는 **`claim.billingMonth`**를 표시합니다.

| 항목 | 내용 |
|------|------|
| 영향 | 월 컬럼만 빈칸 — **청구 생성·상태 변경·NHIS 대사는 정상** |
| 확인 | Swagger `GET /api/v1/billing/claims` 응답의 `yearMonth` 필드 |
| `/billing` 월 필터 | `?yearMonth=` 전송은 백엔드 **미지원** (Q83) — `?branchId=&status=`만 동작 |

### Q99. 보호자 포털 API 경로를 맞춰도 출석·건강이 비어 있어요.

**A.** Q83의 **경로 불일치** 외에 **응답 필드 매핑**도 다릅니다.

| 화면·기대 | 백엔드 실제 | 증상 |
|----------|------------|------|
| 연결 이용자 `id`, `name` | `clientId`, `clientName` (`CheckinTargetResponse`) | 선택기·목록 빈칸 |
| 요약 `attendanceStatus` | `attendance.status` (`GuardianDailyRecordResponse`) | 출석 StatCard 빈값 |
| 요약 `bloodPressure` | `health.systolic` / `health.diastolic` | 혈압 미표시 |
| 요약 `healthAlerts` | `health.alerts` (배열) | 알림 목록 빈값 |

**백엔드 정식 API**

| 용도 | API |
|------|-----|
| 연결 이용자 | `GET /api/v1/guardian/checkin-targets` |
| 당일 요약 | `GET /api/v1/guardian/daily-records?clientId=<uuid>&date=YYYY-MM-DD` |

명세·청구 탭(`GET /guardian/clients/{clientId}/billing`)은 **2026-06-06 백엔드 구현** — 경로는 `services.js`와 일치. UI 필드(`billingMonth`·`status`) 매핑은 Q98·Q102와 동일 이슈.

### Q100. NHIS import 이력(`/billing/nhis-import`)에서 월·행수·지점이 비어 있어요.

**A.** 업로드 API는 정상 동작하지만, **배치 목록 응답 필드명**이 UI 기대와 다릅니다 (Q83 확장).

| 화면·기대 | 백엔드 `NhisImportBatchSummaryResponse` | 증상 |
|----------|----------------------------------------|------|
| `targetMonth` | `yearMonth` | **대상 월** 열 빈칸 |
| `totalRows` | `rowCount` | **총 행수** 0 또는 빈칸 |
| `matchedRows` | *(요약에 없음 — 상세 API의 `matchedCount`만)* | **매칭 완료** `undefined / N` |
| `branchName` | `branchId`만 반환 | **지점** UUID 또는 빈칸 |

**백엔드 정식 API**

| 용도 | API |
|------|-----|
| 배치 목록 | `GET /api/v1/billing/imports/nhis?branchId=<uuid>&yearMonth=YYYY-MM` |
| 업로드 | `POST /api/v1/billing/imports/nhis` (multipart: `branchId`, `yearMonth`, `file`) |

> 업로드·대사 자체는 Swagger로 확인 가능합니다. **「매칭 보정」** 버튼은 `status=COMPLETED` 배치에만 표시됩니다.

### Q101. NHIS 매칭 보정(`/billing/nhis-import/:batchId`) 표가 비어 있거나 금액·이름이 안 보여요.

**A.** 대사 상세 API는 구현되어 있으나 **배치·행 필드 매핑**이 UI와 다릅니다.

**배치 요약**

| UI | API (`NhisImportBatchDetailResponse`) |
|----|--------------------------------------|
| `batch.targetMonth` | `yearMonth` |
| `batch.branchName` | 없음 — `branchId`만 |

**행 목록** (`rows[]`, `matchStatus`는 일치)

| UI | API (`NhisReconciliationRowResponse`) | 증상 |
|----|--------------------------------------|------|
| `name` (공단 수급자명) | **없음** — `ltcCertNo`, `clientName`(매칭 후) | **이름** 열 빈칸 |
| `billingDays` | `serviceDays` | **청구 일수** 빈칸 |
| `billingAmount` | `nhisAmount` | **청구 금액** 빈칸 |
| `diffAmount` | `amountDifference` | **차이** 열 `-` 고정 |

**수동 연결**은 `PATCH /api/v1/billing/imports/nhis/rows/{rowId}/match` `{ "clientId": "<uuid>" }`로 **정상 동작**합니다. UI 모달의 후보 검색(`GET .../candidates?q=`)도 API는 동작하나, 후보 `id`·`name`·`ltcCertNo` 필드는 이용자 API와 동일합니다.

> `ReconciliationPage`는 `result.batch`·`result.rows` 래퍼를 기대하지만 API는 **평면 객체**(`yearMonth`, `rows` 최상위)를 반환합니다. **`NhisReconciliationTable`(UXD-39, `4957bd3` 부분 정합)** — `nhisAmount`·`amountDifference`·`clientName` **fallback**·`MATCH_STATUS` Badge·`DISCREPANCY`/`UNMATCHED` **행 강조**. **배치 요약 래퍼·공단 수급자명** 열은 **갭 잔존**.

### Q102. 이용자 상세(`/clients/:id`) 건강·출석 탭과 청구 상태가 비어 있어요.

**A.** `ClientDetailPage`는 **5탭 UI**(기본·등급·건강·출석·청구)이며, 2026-06-06 **US-D03**으로 건강·출석 탭에 API 호출이 추가되었습니다. 탭별 정합 수준은 다릅니다.

| 탭 | UI (2026-06-06) | 백엔드 API | 증상 |
|----|----------------|-----------|------|
| 기본정보 | **연동** (SSN [열람]은 Q83 경로 불일치) | `GET /clients/{id}` | — |
| 등급 이력 | **Fixed (US-M01, Q176)** — **`GradeHistoryTimeline`** · `GET /clients/{id}/ltc-grade-history` · **인정기간 첨부 Fixed (G37, Q274)** | **`GET/POST/DELETE …/ltc-grade-history/{historyId}/attachments*`** | 탭 선택 시 lazy load · V48 트리거 자동 이력 · **PDF/PNG ≤10MB** |
| 건강 | **부분 Fixed** — `healthRecords.js`가 `items[].recordType`·`payload` → flat 필드 파싱 (`4957bd3`) | `GET /clients/{id}/health?days=7` | `/health` **이력 탭**은 정상 표시. **이용자 상세 건강 탭**은 별도 fetch 경로·갭 잔존 가능 |
| 출석 | **부분** — `fetchAttendanceApi({ clientId, from, to })` | **`GET /clients/{id}/attendance?from=&to=`** 정식 | `/attendance`는 `date`·`branchId`만 — **출석 탭 빈 목록** |
| 청구 | **부분** — `fetchClaimsApi(?clientId=)` 사용 | `GET /clients/{id}/billing` | 목록 빈칸 또는 전체 청구 혼입 (Q83) |

**청구 탭 필드** (API 연결 후에도 Badge가 비면):

| UI | API (`ClientBillingHistoryItemResponse`) |
|----|------------------------------------------|
| `billingMonth` | `yearMonth` |
| `status` | `claimStatus` |

**Swagger 우회 — 출석 탭**

`GET /api/v1/clients/{id}/attendance?from=2026-05-07&to=2026-06-06`

**Swagger 우회 — 건강 탭**

`GET /api/v1/clients/{id}/health` — `items[].recordType`(VITALS 등)과 `payload` 맵에서 수치 확인.

### Q103. 이용자 **수정**은 어디서 하나요? `/clients/:id/edit`이 있나요?

**A.** **예.** 2026-06-06 UXD 2차 이후 **`/clients/:id/edit` 라우트가 등록**되어 있으며, 상세 화면 우측 **「수정」** 버튼으로 이동합니다 (`ClientFormPage` 수정 모드).

| 항목 | 내용 |
|------|------|
| 권한 | `branch_admin`, `social_worker`, `hq_admin` |
| API | `PATCH /api/v1/clients/{id}` |
| 신규 등록 | **정합됨 (UXD 10차)** — `consentToCollectResidentRegistrationNo`·`primaryGuardian` (FAQ Q92) |
| 수정 모드 | `PATCH` — 기본·장기요양·주민번호(재입력 시 동의 포함). **보호자 변경 UI 없음** — 상세·`POST /clients/{id}/guardians` |
| 주민번호 | 수정 시 `residentRegistrationNo` 재전송 없으면 기존 값 유지 — 변경 시 동의 체크 필요 |

퇴소·**등록 폼 사진**은 **UI만** — `POST /clients/{id}/discharge`, `POST /clients/{id}/photo` (Swagger, FAQ Q113).

---

## 13-12. 프론트 라우트·UI 골격 (2026-06-08 8차)

### Q104. `/branches` 지점 관리는 어떻게 쓰나요?

**A.** FE `42f48e1` — **`BranchesPage`**가 SideNav **운영 → 지점**에 연결되어 **목록·검색·등록/수정 모달** UI를 제공합니다 (UXD 36차, Q151).

| 항목 | 내용 |
|------|------|
| API | `GET/POST/PATCH /api/v1/branches` — **백엔드 구현됨** |
| 프론트 | **`BranchesPage`** — `fetch('/api/v1/branches?page=&q=')` 직접 호출. 응답 `{ items }` 래퍼·필드명 **불일치** 시 빈 목록 (Q83·Q151) |
| 권한 | `hq_admin` CRUD, `branch_admin` 조회·등록(백엔드 인가) |
| 우회 | Swagger·Postman으로 지점 등록·수정 |

> V40 지점명 case-insensitive UK — FAQ **Q146**.

### Q105. QR·설정·건강 추이·수가표 화면은 어디 있나요?

**A.** FE `42f48e1` — 아래 경로가 **정식 페이지 컴포넌트**로 등록되어 SideNav에서 진입 가능합니다 (UXD 36차, Q151). **API 경로·본문 불일치**로 일부 기능은 Swagger 우회가 필요합니다.

| 경로 | SideNav | UI | 백엔드 API |
|------|---------|-----|-----------|
| `/attendance/qr/generate` | 출석 → QR 생성 | **`QrGeneratePage`** — **저장·인쇄**(US-E03) | `POST /branches/{branchId}/qr` — payload·이미지 **Partial**(Q109) |
| `/attendance/stats` | 출석 → 출석 통계 | **`AttendanceStatsPage`** (US-E05) | `GET /attendance/stats/monthly` — `yearMonth` vs `from`/`to` (Q106) |
| `/attendance/checkin/qr` | *(보호자 포털·직접 URL)* | **`GuardianCheckinPage`** — **Fixed** (Q109) | `POST /attendance/qr/scan` |
| `/attendance/checkin` | 출석 → 수기 체크인 | **`AttendancePage`** — 입소·귀가·결석 버튼 | `POST /attendance/check-in` — roster·`status` 갭 (Q94) |
| `/billing/fee-schedules` | 청구 → 수가표 | **`FeeSchedulePage`** | `/billing/fee-schedules` — UI `/fee-schedule` 오타 (Q151) |
| `/billing/copay-rates` | 청구 → 본인부담 비율 | **`CopayRatePage`** | `/billing/copay-rates` |
| `/billing/payments` | 청구 → 입금 처리 | **`PaymentPage`** — 이용자명·페이지네이션 | **`POST /claims/{id}/payments` Fixed** · 목록 GET **갭**(claims 필터 우회, Q174·Q198) |
| `/billing/overdue` | 청구 → 미납 관리 | **`OverduePage`** | **`GET /billing/overdue`·`POST …/notify` Fixed** (Q174·Q196) |
| `/settings` | 운영 → 시스템 설정 | **`SettingsPage`** 4탭 | `/organization/settings`, `/settings/*` — 경로 갭 (Q121·Q151) |
| `/platform` | 운영 → 플랫폼 관리 | **`PlatformPage`** | `/platform/organizations` — `?q=` vs `?query=` (Q97) |
| `/guardians` | 운영 → 보호자 | **`GuardiansPage`** | `GET /users?branchId=` 필터 |
| `/health/:clientId` | — (건강 목록 링크) | **`HealthDetailPage`** | `GET /clients/{id}/health?days=` — `payload` 갭 (Q119) |

> 과거 `/guardian/checkin` 경로는 **`/attendance/checkin/qr`** 로 이동했습니다.

### Q106. 출석 통계(`/attendance/stats`) 화면에 숫자가 비어 있어요.

**A.** FE `a627c6d` (US-E05) — **`AttendanceStatsPage`**가 등록되어 **`MonthInput`**으로 월을 선택합니다. 백엔드 API와 **쿼리·응답 구조 불일치**로 숫자가 비거나 오류가 날 수 있습니다 (Q151).

| 항목 | 프론트 (현재) | 백엔드 정식 API |
|------|--------------|----------------|
| 쿼리 | `?branchId=&yearMonth=YYYY-MM` | `?from=YYYY-MM-DD&to=YYYY-MM-DD&branchId=` (`yearMonth` **미지원**) |
| 응답 기대 | `{ summary: { operatingDays, avgAttendanceRate, ... }, clients: [...] }` | `{ from, to, branches: [{ branchId, branchName, months: [{ yearMonth, activeClientCount, attendedDays, attendanceRate }] }] }` |

**증상**: StatCard 요약·이용자별 표가 **빈 값** 또는 로드 오류.

**백엔드 집계 의미** (지점·월 단위):

| 필드 | 의미 |
|------|------|
| `activeClientCount` | 해당 월 말 기준 활성 이용자 수 |
| `attendedDays` | 해당 월·지점 전체 **출석 행** 수 (`check_in_at` 기준, 이용자별 합이 아님) |
| `attendanceRate` | `attendedDays ÷ (activeClientCount × 해당 월 일수)` — **0~1** (UI는 ×100 표시) |

`from`/`to` 생략 시 `to`=오늘, `from`=6개월 전 월 1일이 기본값입니다. **이용자별 일수 breakdown API는 없습니다** — UI의 `clients[]` 표는 백엔드 확장 또는 클라이언트 집계 없이는 채울 수 없습니다.

**Swagger 우회** — `GET /api/v1/attendance/stats/monthly?branchId=<uuid>&from=2026-06-01&to=2026-06-30`

응답 `branches[0].months`에서 월별 `attendanceRate`·`attendedDays`를 확인하세요.

> coder 정합: `yearMonth` → `from`/`to` 변환, `branches[].months` → UI summary 매핑, 이용자별 표는 API 확장 또는 별도 집계 (`PLAN_NOTES.md` TWR-Q1).

---

## 13-13. v1.2 UI·V39 보호자 (2026-06-06 11차)

### Q107. 「보호자 관리」「입금 처리」「미납 관리」메뉴는 어떻게 쓰나요?

**A.** FE `9bdf59f` — SideNav **운영·청구** 그룹에서 **`GuardiansPage`·`PaymentPage`·`OverduePage`** 로 진입합니다 (Q151·Q152).

| 경로 | SideNav | UI | 백엔드 API |
|------|---------|-----|-----------|
| `/guardians`, `/guardians/:id` | 운영 → 보호자 | **`GuardiansPage`·`GuardianDetailPage`** — **「보호자 초대」** 모달(`createGuardianInvitationApi`)·상세 **수정** 버튼 | `GET /guardians` **미구현** — `GET /users?branchId=` 필터 우회 (Q151) |
| `/billing/payments` | 청구 → 입금 처리 | **`PaymentPage`** + **`PaymentRecordModal`** (Q134) | **`POST /claims/{id}/payments` Fixed** · 목록 GET **미구현**(claims 우회, Q174) |
| `/billing/overdue` | 청구 → 미납 관리 | **`OverduePage`** — **「안내 발송」** + **`Pagination`** | **`GET /billing/overdue`·`POST …/notify` Fixed** (Q174·Q196·Q197) |
| `/billing/claims/:claimId` | — (목록 링크) | **`BillingDetailPage`** — **「보호자 발송」** (G2) | `GET /billing/claims/{claimId}` · **`POST …/notify`** (Q196) |

**대체**: 보호자 초대는 **`/clients/:id`**(J01) 또는 **`/guardians`** 초대 모달. 보호자 포털은 **`/guardian`** (J02). 청구·NHIS는 **`/billing`**·**`/billing/imports/nhis`**. 수납 우회는 `/billing` **수납완료** 버튼 또는 Swagger `PATCH …/status` `{ "status": "PAID" }` (Q128).

### Q108. 보호자 포털에서 본인부담금 명세를 볼 수 있나요?

**A.** **예 (BE `598d108`·FE `c7c8f07`, US-J02).** 연결 이용자의 청구 이력 API와 **`GuardianPortalPage`** UI가 연동되었습니다.

| API | 권한 | 응답 |
|-----|------|------|
| `GET /api/v1/guardian/clients/{clientId}/billing` | `guardian`, `client_user` | `{ clientId, items[] }` — 각 `yearMonth`, `claimStatus`, `copayAmount` 등 |

| UI (UXD-55) | 내용 |
|-------------|------|
| 목록 | `/guardian` **「본인부담금 명세」** 표 — 이용자 선택 시 자동 로드 |
| 상세 | 행 **「상세」** → **`GuardianBillingDetailModal`** (Q132·Q175) |

명세가 비면 센터에서 청구 **확정** 여부를 확인하세요. 연결 이용자가 없으면 `checkin-targets`·초대 수락(Q139)을 먼저 확인합니다.

### Q109. QR 생성·체크인이「실패」하거나 미리보기가 비어요.

**A.** **Partial Fixed (FE `bf3d40d`·`b046444`·`99f2f3e`, US-E04)** — **`GuardianCheckinPage`** 체크인 대상·스캔 API가 **정합**되었습니다. 연결 이용자가 **2명 이상**이면 **`QrCheckinTargetsPanel`**(Q406)로 대상을 고릅니다. **`QrGeneratePage`** 는 **지점 스코프 경로**(`POST /branches/{branchId}/qr`)로 연동되었으나, **요청 본문·QR 이미지 응답 갭**이 잔존합니다.

**체크인 (Fixed, `bf3d40d`·`99f2f3e`)**

| 항목 | 내용 |
|------|------|
| 대상 목록 | `GET /guardian/checkin-targets` → `clientId`·`clientName`·`primary` 매핑 |
| 스캔 | `POST /attendance/qr/scan` — `{ qrToken, clientId, transportType? }` (귀가 시 교통편 필수) |
| UI | 입소/귀가 `FilterChips` · 연결 이용자 **1명**이면 이름 자동 표시(대표면 **「(대표)」**) · **2명 이상**이면 **`QrCheckinTargetsPanel`** — **←→↑↓**·Home/End 키보드 · **「대표」** Badge · 카메라 스캔은 **준비 중** — 토큰 직접 입력 |

**QR 생성 (Partial, `b046444`)**

| 프론트 (현재) | 백엔드 기대 | 결과 |
|--------------|------------|------|
| `POST /branches/{branchId}/qr` `{ type: "checkin", validMinutes: 480 }` | `{ direction: "in"\|"out", expiresInMinutes?: 1–720 }` | **`400` 가능** (`type` 미인식) |
| `qrDataUrl` / `validUntil` 기대 | `{ qrToken, direction, expiresAt }` — **이미지 URL 없음** | 미리보기 **빈 칸** (저장·인쇄 버튼 비활성) |
| 지점 미선택 | `activeBranchId` 없으면 생성 버튼 **비활성** + 안내 | ✅ |

**Swagger 우회 — QR 생성·체크인**

```json
POST /api/v1/branches/{branchId}/qr
{ "direction": "in", "expiresInMinutes": 480 }
```

응답 `qrToken`을 보호자 `/guardian/checkin` **토큰 입력란**에 붙여 넣거나, `POST /attendance/qr/scan` `{ "qrToken": "...", "clientId": "<uuid>" }`로 처리합니다.

> 관련: USER_MANUAL §4-4 · §8-4

### Q110. `guardian_link_status`(PENDING/LINKED)는 무엇인가요?

**A.** V39부터 이용자(`clients`)마다 **보호자 연결 상태**가 저장됩니다.

| 값 | 의미 | 현장 조치 |
|----|------|----------|
| `LINKED` | `guardian_clients`에 **1명 이상** 연결됨 | 정상 — QR·포털 사용 가능 |
| `PENDING` | 연결된 보호자 **없음** | 보호자 계정 생성 후 `POST /clients/{id}/guardians`로 연결 |

**신규 등록 (Must 흐름 — 단일 트랜잭션)**

1. `POST /api/v1/users` — `roleCode: "guardian"` 보호자 계정 **선행** 생성.
2. `POST /api/v1/clients` — `consentToCollectResidentRegistrationNo: true` + **`primaryGuardian: { guardianUserId, relationship }` 필수** → 등록 즉시 **`LINKED`**.

마지막 보호자 연결을 삭제하면 DB 트리거(V39)가 **`PENDING`**으로 되돌립니다. **2026-06-07 UXD 10차**부터 `/clients/new`는 기존 보호자 선택 또는 신규 계정 생성으로 **`primaryGuardian`을 전송**합니다 (Q92). `is_primary`(대표 보호자 1명)는 Q67과 별개 — V39는 **「연결 자체」**를 강제합니다.

### Q111. 공단 엑셀 import 전에 브라우저·다운로드 방법을 안내받을 수 있나요?

**A.** **예 (2026-06-06).** 백엔드가 롱텀(장기요양정보시스템) 2026 개편 기준 **온보딩 안내** API를 제공합니다.

| 항목 | 내용 |
|------|------|
| API | `GET /api/v1/billing/imports/nhis/guidance` |
| 권한 | `hq_admin`, `branch_admin` |
| DB | **미사용** — 정적 텍스트 응답 |
| 브라우저 | **Chrome 또는 Edge 최신 버전 필수** — Internet Explorer **미지원** |
| 응답 필드 | `portalUrl`, `browserRequirement`, `exportSteps[]`, `insecureContentHint`, `leadingStatusColumnNote`, `message`/`guidanceMessage` |
| 복원 (BE `9a97a1c`) | 일시 404 회귀 후 **`NhisImportGuidance`** 정적 응답 **재등록** — **`NhisImportGuidanceTest`**·RBAC 회귀 |

**exportSteps 요약**

1. Chrome/Edge에서 [longtermcare.or.kr](https://www.longtermcare.or.kr/) 로그인
2. 급여비용 청구 → 청구내역상세에서 대상 월 선택
3. 「엑셀 다운로드」로 파일 저장
4. ogada **청구 → NHIS import**에서 업로드

> **처리상태 열**: 엑셀 첫 열이 「처리상태」이면 파서가 자동 스킵 후 표준 컬럼(인정번호·급여일수·공단부담금)을 매핑합니다.  
> **프론트 UI (FE `1220bfb`·`2b6024a`·`0abf164`, QA-B24 Fixed, Q133)**: `/billing/imports/nhis` 상단 **`NhisImportGuidePanel`** — Chrome/Edge·4단계 절차 **정적 안내** + **`GET /billing/imports/nhis/guidance`** 응답을 **「실서버 안내」** warning Alert로 **동적 표시**합니다. BE **`9a97a1c`** 로 guidance API **404 회귀 복원**.

### Q112. 「세션이 곧 만료됩니다」 모달이 뜨나요?

**A.** **FE `42f48e1`** — **`SessionTimeoutProvider`**(US-B03)가 `App.jsx`에 적용되어 **30분 무활동 시 60초 전 경고** 모달이 표시됩니다.

| 항목 | 동작 |
|------|------|
| idle 경고 | **`SessionTimeoutModal`** — 60초 카운트다운 |
| 연장 | **「세션 연장」** — idle 타이머 리셋 |
| 토큰 저장 | access **메모리** + refresh **`sessionStorage`** — **같은 탭** 새로고침 시 **`restoreSession()`** (Q82·Q396) |
| 수동 로그아웃 | AppShell **LogoutButton** (Q141) |
| access 만료 | 30분 후 API `401` — 재로그인 |

마우스·키보드·스크롤·터치 입력이 있으면 idle 타이머가 리셋됩니다.

### Q113. 이용자 등록 화면(`/clients/new`)은 어디 있나요?

**A.** FE `42f48e1` — **`/clients/new`·`/clients/:clientId/edit`** 라우트와 **`ClientFormPage`** 가 등록되었습니다 (UXD 36차, US-D01, Q151).

| 항목 | 내용 |
|------|------|
| 진입 | SideNav **운영 → 이용자** → **등록** 또는 목록 **신규 등록** |
| UI | 이름·생년월일·등급·본인부담·주민번호 동의·**대표 보호자 이름·연락처** 입력 |
| **API 갭** | `createClientApi`가 `birthdate`·`ssn`·`primaryGuardian.name/phone` 전송 — 백엔드 `birthDate`·`residentRegistrationNo`·`primaryGuardian.guardianUserId` **불일치** → 저장 **400** 가능 (Q83·Q151) |
| 우회 | Swagger `POST /api/v1/clients` — Q92 본문 예시 |

> `client_user`·사진은 등록 후 별도 API (Q113). coder **services.js 정합** 후 현장 UI로 등록 가능합니다.

### Q114. 화면 상단 「라이트/다크」버튼은 무엇인가요?

**A.** **UXD 11차(2026-06-07)** 에 추가된 **`ThemeToggle`** 입니다. AppShell 상단 우측에서 **라이트·다크 테마**를 전환합니다.

| 항목 | 내용 |
|------|------|
| 위치 | 모든 `AppShell` 화면 상단 (로그인 화면 제외) |
| 저장 | `localStorage` 키 `ogada-theme` — 브라우저·기기별 유지 |
| 초기값 | 저장값 없으면 **OS 다크모드 설정** 추종 (`prefers-color-scheme`) |
| 접근성 | `aria-pressed`·`aria-label`·텍스트 라벨(「라이트」/「다크」) — 색상만으로 구분하지 않음 |
| 용도 | 야간 근무·조도 낮은 환경에서 눈 피로 완화 |

다크 모드는 `tokens.css`의 `[data-theme="dark"]` 토큰으로 전 화면 색상이 일괄 전환됩니다. 인쇄·PDF 출력 시에는 **라이트 모드**를 권장합니다.

### Q115. Windows 고대비·로그인 화면·모달 키보드 조작은 어떻게 되나요?

**A.** **UXD 12차(2026-06-07, `404a30e`)** 에 접근성·로그인 UI가 보강되었습니다.

| 항목 | 내용 |
|------|------|
| **로그인 카드** | `/` 화면이 **`.ds-login` 카드**·ogada 모노그램·디자인 시스템 `Field`/`TextInput`/`Alert`로 통일 — 라벨·오류 메시지 스크린리더 호환 |
| **Modal 포커스 트랩** | 결석·체크아웃·세션 만료·NHIS 매칭 등 **모든 모달**에서 Tab/Shift+Tab이 다이얼로그 **내부만** 순환. ESC·배경 클릭으로 닫기 |
| **`prefers-contrast: more`** | OS·브라우저「색 대비 높임」설정 시 보조 텍스트 대비·포커스 링(3px) 강화 |
| **`forced-colors: active`** | Windows **고대비 테마** 등 강제 색상 모드에서 버튼·카드·모달·로그인 카드에 **경계선**을 두어 배경 틴트 없이도 식별 가능 |
| **배차 화면 확장 (Q168)** | **UXD-50** — `/transport` 지도 캔버스·정차 카드·마커·순번 Badge·강조 정차도 동일 규칙 적용 |
| **ThemeToggle과 별개** | 고대비는 **OS/브라우저 설정**을 따릅니다. 다크 모드는 상단 ThemeToggle(Q114)로 별도 전환 |

현장 PC에서 Windows **설정 → 접근성 → 대비 테마 → 고대비 켜기**를 사용하면 ogada UI가 자동으로 경계선 중심 표시로 전환됩니다. 배차 화면 상세는 **Q168**을 참고하세요.

### Q116. `/settings`에서 「이용자 셀프 QR 체크인 허용」스위치는 무엇인가요?

**A.** **UXD 13차(2026-06-07, `07fd305`)** 에 추가된 **`Switch` 토글**입니다. 통합 관리자(`hq_admin`)·시스템 관리자(`sysadmin`)가 `/settings` → **일반** 탭 → **조직 설정** 카드에서 **이용자 본인(`client_user`) QR 셀프 체크인** 허용 여부를 켜거나 끕니다.

| 항목 | 내용 |
|------|------|
| UI | WAI-ARIA `switch` 패턴 — `role="switch"`·`aria-checked`·**켜짐/꺼짐 텍스트** 병행(색만 의존 금지), 44px 트랙, Windows **고대비**(`forced-colors`) 경계선 |
| 정책 필드 | Organization `allow_client_self_checkin` (REQUIREMENTS §3-3) |
| 기본값 | **꺼짐** — 보호자(`guardian`)만 QR 셀프 체크인 |
| 초기 표시 | JWT `user.allowClientSelfCheckin` 또는 로그인 세션 값 (실제 Tenant 설정과 다를 수 있음) |

**저장·권한 주의 (FAQ Q87 연계)**

| 계층 | 동작 |
|------|------|
| **UI 토글** | 클릭 시 **화면 상태만** 변경 — **아직 서버에 저장되지 않습니다** |
| **정식 API** | `PATCH /api/v1/organization/settings` `{ "allowClientSelfCheckin": true\|false }` — **`hq_admin` 전용** |
| **`/settings/*` 기술 API** | 백업·감사 — **`sysadmin`만** (`SettingsController`) |

**Swagger 우회 (`hq_admin` JWT)**

```json
PATCH /api/v1/organization/settings
{ "allowClientSelfCheckin": true }
```

켜면 이용자 등록 시 **`client_user` 계정 발급**·QR 체크인(설정 on + 계정 발급 후)이 허용됩니다 (Q56·Q113). 끄면 보호자만 `/guardian/checkin`에서 QR 스캔 가능합니다.

> coder 후속: `SettingsPage`의 TODO 주석은 `PATCH /settings/organization`으로 적혀 있으나 **백엔드 정식 경로는 `/organization/settings`** 입니다 (API_SPEC §3).

### Q117. 수가표 「이력 보기」·NHIS import 배치 상태 뱃지는 무엇인가요?

**A.** **UXD 14차(2026-06-07, `a42d6fb`)** 에 추가·정리된 UI입니다.

#### 수가표 이력 보기 (`/billing/fee-schedules`)

| 항목 | 내용 |
|------|------|
| 진입 | **청구·정산** → **수가표 관리** → 상단 **「이력 보기」** 버튼 |
| UI | `Modal` + **`FeeRateHistoryPanel`** — 연도별 그룹, 등급·1일 수가·시행일·등록일·등록자 표 |
| 접근성 | 표 `caption`(sr-only), 수가 셀 `aria-label`, `tabular-nums` 정렬 |
| **현재 한계** | 패널 데이터가 **빈 배열** — `GET /api/v1/billing/fee-schedules?year=` **미호출**. 별도 `/history` 엔드포인트는 **없음** (API_SPEC §7) |

**Swagger 우회** — `GET /api/v1/billing/fee-schedules?year=2026` 응답으로 등급별 수가 버전을 확인합니다. `created_by`는 UUID이며 `users` 조회로 이름을 매핑할 수 있습니다 (Q76).

#### NHIS import 배치 상태 뱃지

| 상태 코드 | 한국어 라벨 | Badge tone |
|----------|------------|------------|
| `PENDING` | 대기 | neutral |
| `PROCESSING` | 처리중 | info |
| `COMPLETED` | 완료 | success |
| `FAILED` | 실패 | danger |

`Badge.jsx` **`BATCH_STATUS`** 공유 상수로 `/billing/nhis-import` 목록·상세 뱃지가 **단일 소스**로 표시됩니다 (이전 `NHISImportPage` 로컬 정의 제거).

#### 건강 추이 차트 색상 (후속)

`chartColors.js`·`tokens.css` `--chart-color-1~6`이 Recharts용 **라이트/다크 팔레트**를 제공합니다. `/health/:clientId`·대시보드 차트에 적용됩니다 (FAQ Q118·Q119).

---

## 13-14. Recharts·설정·인증 UX (2026-06-07 18차)

### Q118. 대시보드에 차트가 보이는데 숫자가 이상해요.

**A.** **UXD-48 (`8a764df`)** — codebase에서 소실됐던 Recharts 레이어가 **재구현·연동**되었습니다. `ChartContainer` 래퍼·`chartColors.js` 팔레트·라이트/다크 테마를 사용합니다.

| 화면 | 차트 | 데이터 소스 |
|------|------|------------|
| `/dashboard` (지점) | `AttendanceRateChart` — 월별 출석률 추이 (US-H01) | `GET /dashboard/branch` → `monthlyAttendanceRates[]` |
| `/dashboard/hq` (통합) | `BranchCompareChart` — 지점별 비교 | `GET /dashboard/hq` → `branches[]` |
| `/attendance/stats` | `AttendanceRateChart` (막대, US-E05) | `GET /attendance/stats/monthly?yearMonth=` → `dailyRates[]` — **응답 구조 불일치** 잔존 (Q106) |

**알려진 표시 갭**

| 항목 | 증상 | 원인 |
|------|------|------|
| 출석률 `%` | `0.85%` 과소 표기 | API `attendanceRate`는 **0~1** 소수, UI가 `×100` 없이 `%`만 붙임 (Q85와 동일) |
| 통합 지점 비교 | 일부 지점 막대 0 | 당일·기간 내 출석 데이터 없음 또는 `hq` 응답 필드 매핑 갭 |

차트는 **접근성** `ChartContainer` 래퍼·`chartColors.js` 팔레트를 사용합니다. 데이터가 없으면 「월별 출석률 데이터가 아직 없습니다」등 **emptyMessage**가 표시됩니다.

### Q119. `/health/:clientId` 건강 추이가 비어 있거나 차트가 없어요.

**A.** **UXD-48 (`8a764df`)** — `HealthDetailPage`에 **`HealthTrendChart`**(혈압·체온·혈당·SpO₂ 추이, US-F04)와 **표 이력**이 **병행** 표시됩니다.

| 항목 | 내용 |
|------|------|
| UI | **`HealthTrendChart`** + **표** — 날짜·혈압·체온·혈당·SpO₂·기록자 열 |
| API | `GET /api/v1/clients/{id}/health` — 경로 **정합** |
| 매핑 | **`healthRecords.js`** — `items[].recordType`·`payload` → flat 필드 (`4957bd3`) |
| 기간 필터 | **`FilterChips`** 7일·30일 UI — **`?days=` 쿼리 미호출** (Q165) |

**Swagger 확인** — `GET /api/v1/clients/{id}/health?days=30`. 당일 입력은 `/health` **일일 건강·투약 탭** — **저장 Fixed**(Q154·Q95).

### Q120. NHIS import 목록에 「처리 단계」막대가 보여요.

**A.** **UXD 16차** 에 **`BatchProgressSteps`** 컴포넌트가 추가되었습니다.

| 항목 | 내용 |
|------|------|
| 위치 | `/billing/nhis-import` 이력 — `COMPLETED`가 **아닌** 배치 행 / 대사 상세(`/billing/nhis-import/:batchId`) 상단 |
| 단계 | **대기**(`PENDING`) → **처리중**(`PROCESSING`) → **완료**(`COMPLETED`) 또는 **실패**(`FAILED`) |
| 접근성 | `role="list"`·단계별 `aria-current`·`aria-label` — 색상만으로 구분하지 않음 |
| 연동 | 배치 `status` 필드와 **동기** — 업로드·파싱은 기존 API 정상 (Q100–Q101 필드명 갭은 별도) |

`FAILED` 시 배치 상세에서 오류 메시지를 확인하고 엑셀·브라우저(Chrome/Edge, Q111)를 점검하세요.

### Q121. `/settings` 백업·감사 로그 탭이 비어 있어요.

**A.** **FE `3803247` (SEC-D17, Partial Fixed)** — `SettingsPage` **4탭**(보안·로그인 이력·감사·백업) 패널이 **`services.js` `apiFetch` 정식 경로**로 갱신되었습니다. **백업·감사·로그인 이력 조회**는 정상 동작할 수 있으나, **일부 기능·필터 갭**이 잔존합니다.

| 탭 | UI | 프론트 (FE `3803247`) | 백엔드 정식 API | 잔여 갭 |
|----|-----|----------------------|----------------|---------|
| **보안** | `PasswordChangeModal`·`PasswordResetRequestModal` | `POST /auth/change-password` · `POST /auth/password/reset-request` | **둘 다 Fixed** (Q122·Q126) | — |
| **백업** | `BackupSettingsPanel` | `GET /settings/backups` · `PATCH /settings/system` `{ backupEnabled }` | 동일 | **수동 백업 트리거** 미구현 |
| **감사** | `AuditLogPanel` | `GET /settings/audit-logs?page=&size=` | 동일 | UI `eventType`·`from`/`to` 필터는 **클라이언트 필터**(API 미지원) |
| **로그인 이력** | `LoginHistoryPanel` (Q125) | `GET /auth/login-history` | 동일 | UI `role`·`from`/`to` 필터는 **클라이언트 필터** |

| 역할 | 탭 접근 |
|------|---------|
| `sysadmin` | 4탭 전체 |
| `hq_admin` | **`/settings` 차단** — 조직 정책은 **`/organization/settings`** (Q178) |
| `platform_admin` | 라우트 가드 **`/forbidden`** (Q87) |

**우회 (`sysadmin` JWT)** — Swagger `GET /api/v1/settings/backups`, `GET /api/v1/settings/audit-logs?page=0&size=20`, `GET /api/v1/auth/login-history`.

### Q122. 로그인 후 「비밀번호 변경」 모달이 뜨는데 저장이 안 돼요.

**A.** **Fixed (BE `fe5b38b` + FE `3803247` lineage, US-A02)** — **`POST /api/v1/auth/change-password`** 가 구현되어 **`PasswordChangeModal`**·`/settings` **보안** 탭에서 저장이 동작합니다.

| 항목 | 내용 |
|------|------|
| 표시 조건 | 로그인 응답·JWT **`mustChangePassword`** true 시 로그인 화면 모달 (필수 변경 — ESC·바깥 클릭 닫기 불가) |
| 설정 화면 | **보안** 탭 **「비밀번호 변경」** — `sysadmin`·`hq_admin`·`platform_admin` |
| 프론트 API | `changePasswordApi` → `POST /api/v1/auth/change-password` — `{ "newPassword" }` |
| **백엔드** | **`AuthService.changePassword`** — JWT subject 기준 변경 · **기존 비밀번호와 동일하면 `422`** |
| **필드 오류** | `@Size(min=8)` 위반 시 **`error.fieldErrors.newPassword`** (Q190) |
| 테스트 | **`AuthServiceTest.changePassword*`** · **`MustApiEndpointRoutingTest.changePasswordRouteShouldAcceptPost`** |

**분실·잊음** — IT 담당이 Swagger `POST /auth/password/reset-request` → 메일 링크 → `POST /auth/password/reset` (**Q126 Fixed**).

> 관련: Q126 · Q190 · USER_MANUAL §2-3 · ADMIN_GUIDE §4-2

### Q123. 이용자 상세에서 「보호자 초대」가 실패해요.

**A.** **백엔드 + 프론트 연동 (V43 + FE `7170b2a`)** — `ClientDetailPage` **보호자 초대** 카드에서 발송·이력·재발송·취소가 가능합니다 (Q143).

| 항목 | 내용 |
|------|------|
| 발송 API | `POST /api/v1/clients/{clientId}/guardians/invitations` — `{ "email", "relationship", "channel": "EMAIL" }` |
| 이력 API | `GET /api/v1/clients/{clientId}/guardians/invitations` |
| 수락 API | `POST /api/v1/guardian/invitations/{token}/accept` — `{ "name", "phone", "password" }` (공개, Q139) |
| 프론트 | **연동** — `GuardianInvitationList` |

**실패 시 점검**

| 증상 | 조치 |
|------|------|
| `409` 이메일 중복 | 이미 등록된 보호자 — 연결 API 또는 다른 이메일 |
| `403` | 역할·지점 스코프 — `branch_admin`·`social_worker` 확인 |
| `400` channel | v1.1은 **`EMAIL`만** 허용 (Q145) |
| 수락 실패 | 토큰 만료·이미 수락 — 센터에서 **재발송** |

**우회** — Swagger 발송·`POST /users`(guardian) + `POST /clients/{id}/guardians` 또는 등록 시 `primaryGuardian`(Q92·Q110).

### Q124. 보호자 알림(푸시·이메일) 설정 API가 있나요?

**A.** **B08 / V41 + V42 (2026-06-07, TSR 48·54차 Fixed)** — 보호자 알림 수신 설정 API가 **백엔드에 구현**되었습니다. **V42**에서 카카오·SMS 채널 on 시 **`consent_at` 필수** DB CHECK가 추가되었습니다 (FAQ **Q142**).

| 구분 | 메서드 | 경로 | 권한 |
|------|--------|------|------|
| **보호자 본인** | `GET` / `PUT` | `/api/v1/guardian/notification-preferences` | `guardian`, `client_user` |
| **직원 대리** | `GET` / `PUT` | `/api/v1/clients/{clientId}/guardians/{guardianUserId}/notification-preferences` | `branch_admin`, `social_worker` |

직원 API는 **`guardian_clients` 연결**·지점 스코프를 검증한 뒤 보호자 대신 온보딩 시 수신 채널을 설정합니다. 프론트 UI는 **미구현** — Swagger 사용 (Q137-1).

**채널·이벤트 필드** (`NotificationPreferenceResponse` / `NotificationPreferenceRequest`)

| API 필드 | DB 컬럼 | 기본값 |
|----------|---------|--------|
| `channelInApp` | `channel_in_app` | true |
| `channelPush` | `channel_push` | false |
| `channelEmail` | `channel_email` | false |
| `channelKakao` | `channel_kakao` | false |
| `channelSms` | `channel_sms` | false |
| `notifyAttendance` | `notify_attendance` | true |
| `notifyDailyCare` | `notify_daily_care` | true |
| `notifyBilling` | `notify_billing` | false |
| `notifyEmergency` | `notify_emergency` | true |
| `consentAt` | `consent_at` | null (응답만) |

- 보호자 1명당 Tenant 스코프 **1행** (UK `organization_id` + `guardian_user_id`).
- **방해 금지 시간**은 preference API가 아닌 **`NotificationService` 내부**(22:00–08:00 KST, 긴급 제외) — FAQ **Q147**.
- **직원 대리 설정** API 구현됨 — **실제 카카오/SMS 중계**는 stub provider(Q147).
- **프론트 UI**: 미구현 — Swagger로 조회·갱신.

**PUT 예시**

```json
{
  "channelInApp": true,
  "channelPush": false,
  "channelEmail": true,
  "channelKakao": false,
  "channelSms": false,
  "notifyAttendance": true,
  "notifyDailyCare": true,
  "notifyBilling": false,
  "notifyEmergency": true
}
```

카카오·SMS를 `true`로 설정하면 **V42** CHECK로 `consent_at`이 자동 기록됩니다 (FAQ Q142). `quietHoursStart`/`End` 필드는 **현재 API에 없습니다**.

---

## 13-15. 계정 보안·플랫폼 상세 UI (2026-06-07 19차, TSR 39차)

### Q125. `/settings` 「로그인 이력」탭은 무엇인가요?

**A.** **TSR 39차** 에 `LoginHistoryPanel`이 추가되었습니다. `sysadmin`이 `/settings` → **로그인 이력** 탭에서 Tenant 소속 계정의 로그인 시도를 조회합니다 (REQUIREMENTS §3-1).

| 항목 | 내용 |
|------|------|
| UI | 역할·시작일·종료일 필터, 표(일시·계정·역할·지점·결과·IP), `LOGIN_RESULT_STATUS` Badge(성공/실패/잠금) |
| 마스킹 | `emailMasked`·`ipMasked` — PII 미노출 |
| 프론트 API | `GET /api/v1/settings/login-history?role=&from=&to=&page=` |
| 백엔드 정식 | `GET /api/v1/auth/login-history` — **쿼리·페이지네이션 없음**, 응답 `{ items: [{ id, userId, roleCode, ipAddress, success, createdAt }] }` |
| 필드 갭 | UI `result`(SUCCESS/FAILURE/LOCKED) vs API `success`(boolean), UI `emailMasked`/`branchName` vs API 미제공 |

**우회** — `sysadmin` JWT로 Swagger `GET /api/v1/auth/login-history`. 관리자 역할(`hq_admin` 등)은 Tenant 전체 이력, 일반 역할은 본인 이력만 반환합니다 (`AuthService.loginHistory`).

### Q126. 「비밀번호 재설정 요청」모달은 어디서 쓰나요?

**A.** **FE `3803247` (SEC-D17 Fixed)** — `PasswordResetRequestModal`이 **로그인·설정** 양쪽에서 **`POST /api/v1/auth/password/reset-request`** 를 호출합니다.

| 진입 | 역할 | API 연동 |
|------|------|----------|
| 로그인 `/` 하단 **「재설정 요청」** | 비로그인 | **`requestPasswordResetApi` Fixed** |
| `/settings` → **보안** → **재설정 요청** | `sysadmin` | **`requestPasswordResetApi` Fixed** |

| 프론트 | 백엔드 |
|--------|--------|
| `POST /auth/password/reset-request` `{ email }` | 동일 |

요청 완료 후 모달에 안내 문구가 표시됩니다. 등록되지 않은 이메일도 **동일 응답**(계정 열거 방지). rate limit 적용 시 `429` (Q78). 검증 실패 시 **`fieldErrors.email`** 로 필드 아래 메시지 표시 (Q190).

### Q127. `/platform` 「관리」버튼·고객사 상세 모달은 무엇인가요?

**A.** **TSR 39차** 에 `PlatformOrgDetailModal`(US-A01 Tenant 상세)이 추가되었습니다.

| 항목 | 내용 |
|------|------|
| 진입 | `/platform` 고객 목록 행 **「관리」** 클릭 |
| 표시 | 법인명·사업자번호·지점 수·활성 상태·등록일 + **관리자 계정 발급** 폼 |
| 발급 API | `POST /api/v1/platform/organizations/{orgId}/admins` |
| 프론트 본문 | `{ email }` **만** 전송 (`handleIssueAdmin`) |
| 백엔드 필수 | `{ email, displayName, password }` — Q97과 동일 |

목록이 비어 보이거나 검색이 안 되면 Q97·Q83(목록 `List` vs `items`, `?q=` vs `?query=`)을 먼저 확인하세요. 신규 Tenant 등록 모달은 기존과 동일하게 동작합니다.

---

## 13-16. 청구·대시보드·보호자 UI (2026-06-07 20차, UXD 20–21차)

### Q128. `/billing` 상태 필터·「확정」확인 모달은 무엇인가요?

**A.** **UXD 20차 (US-G07)** — `BillingPage`·`BillingDetailPage`에 청구 상태 관리 UI가 추가되었습니다.

| 컴포넌트 | 위치 | 기능 |
|----------|------|------|
| **`FilterChips`** | `/billing` 목록 상단 | **전체·작성중·확정·수납완료** 칩 필터 — API `?status=DRAFT\|CONFIRMED\|PAID` 연동. 건수(`statusCounts`)가 있으면 칩 옆 숫자 표시 |
| **`BillingStatusConfirmModal`** | 목록·상세 **확정**·**수납완료** 버튼 | `DRAFT→CONFIRMED`·`CONFIRMED→PAID` 전이 **확인 모달** — 확정 후 금액·라인 **되돌릴 수 없음** 경고 |

| 항목 | 내용 |
|------|------|
| 상태 전이 API | `PATCH /api/v1/billing/claims/{id}/status` `{ "status": "CONFIRMED" }` — **백엔드 구현됨** |
| 목록 API | `GET /api/v1/billing/claims?branchId=&status=&yearMonth=` — `yearMonth` 쿼리 **무시** 잔존 (Q83·Q98) |
| 청구 상세 | `/billing/:id` — `BillingStatusConfirmModal`·`ClaimStatusTimeline` UI. **`GET /claims/{id}` 미연동** — 상세 본문 빈 상태 |

**현장 팁** — 목록에서 **확정** 클릭 → 모달에서 이용자명·월·금액 확인 → **확정** 제출. 이미 `CONFIRMED`인 청구는 **수납완료**만 가능합니다.

### Q129. 대시보드 「건강 이상 알림」목록이 달라졌어요.

**A.** **UXD 20차 (US-F01·US-H01)** — `DashboardPage`가 **`HealthAlertList`** 컴포넌트로 건강 이상 이용자를 표시합니다.

| 항목 | 내용 |
|------|------|
| 위치 | `/dashboard`(지점)·`/dashboard/hq`(통합) — 위젯 그리드 아래 **건강 이상 알림** 카드 |
| 데이터 | `dashboardWidgets.js` → `buildHealthAlertList()` — `GET /dashboard/branch`·`/dashboard/hq` 응답의 `healthAlerts[]` 매핑 |
| UI | 이용자명·이상 유형·기록 시각 — 알림 없으면 「건강 이상 알림이 없습니다」 |
| **HQ 지점명 (UXD-49, US-H02)** | `/dashboard/hq` — `healthAlerts[].branchName`이 있으면 **중립 Badge**로 지점명 표시 · `ds-sr-only` 「지점」 접두 라벨 병행 (색만 의존 금지) |
| 지점 대시보드 | `/dashboard` — `branchName` **미표시**(단일 지점 스코프, 하위 호환) |
| 접근성 | `role="list"`·항목별 `aria-label` |

통합 대시보드는 **전 지점** 알림에 **지점 Badge**가 함께 표시됩니다 (Q167). 상세 기록은 `/health` 또는 이용자 상세에서 확인하세요.

### Q130. 보호자 포털 「일일 기록」카드가 바뀌었어요.

**A.** **FE `ac5638e` (US-I02, UXD-20·UXD-62)** — `/guardian` **「일일 기록」** 탭의 **`GuardianDailySummary`** 가 FLOWCHART §9(출석·건강·**식사**)에 맞춰 갱신되었습니다. (구 `GuardianPage` **오늘 현황** 탭 서술 **정정**)

| 영역 | 표시 |
|------|------|
| 출석 | `StatusBadge` — 입소·미입소·퇴소·체크인/아웃 시각 |
| 건강 | 당일 혈압·체온·투약 건수 |
| **식사 (UXD-62)** | `meals[]` — 구분(아침·점심·간식) + 섭취량 Badge — **API `meals[]` 미반환 시 「—」**(Q188) |
| 이상 알림 | `health.alerts[]` — 이상 수치가 있으면 경고 `Alert` |

| API | 현재 |
|-----|------|
| 프론트 | `fetchGuardianDailyRecordsApi` → **`GET /guardian/daily-records?clientId=`** |
| 백엔드 | `attendance`·`health` 요약 반환 — **`meals[]` 필드 미포함**(Q188) |

API 오류 시 「오늘 기록을 불러오지 못했습니다」가 표시됩니다.

### Q131. 수가표·본인부담 화면에 표(테이블)가 생겼어요.

**A.** **UXD 21차 (US-G00a·US-G00b)** — 등급별 입력 UI가 테이블 컴포넌트로 교체되었습니다.

| 화면 | 컴포넌트 | 내용 |
|------|----------|------|
| `/billing/fee-schedules` | **`FeeScheduleTable`** | 등급 1~5 × 1일 수가·시행일 편집 표. **「이력 보기」** → `FeeRateHistoryPanel` 모달(Q117) |
| `/copay-rates` | **`CopayRateTable`** | `GENERAL`/`REDUCED_40`/`REDUCED_60`/`MEDICAID` 구분별 **비율(%)** 편집 표 |

| 항목 | 현재 |
|------|------|
| 저장 | **TODO** — `PATCH /billing/fee-schedules`·`PATCH /billing/copay-rates` **미호출**. 저장 클릭 시 로컬 성공 메시지만 |
| 이력 | `FeeRateHistoryPanel` — **`GET /billing/fee-schedules?year=` 미연동**, 빈 목록 (Q117) |
| 기본값 | `CopayRatePage` — 15/9/6/0% **하드코딩** 초기값 |

**우회** — `hq_admin` JWT로 Swagger `POST/PATCH /billing/fee-schedules`·`GET /billing/copay-rates` 사용 (Q91).

### Q132. 보호자 포털에서 본인부담금 명세 「상세」를 누르면 모달이 떠요.

**A.** **FE `c7c8f07` (UXD-55, US-J02)** — **`GuardianPortalPage`**(`/guardian`) **「본인부담금 명세」** 카드에 월별 목록 표 + **`GuardianBillingDetailModal`** 상세 UI가 연동되었습니다. (구 UXD 20차 `GuardianPage` 탭 서술 **정정**)

| 항목 | 내용 |
|------|------|
| 진입 | `/guardian` → 이용자 선택 → 명세 표 행 **「상세」** (`aria-label`에 청구월 포함) |
| 목록 | 청구월·본인부담금·`BILLING_STATUS` Badge — `GET /guardian/clients/{clientId}/billing` 자동 로드 |
| 상세 Modal | 청구월·이용일수·총 급여·공단부담·본인부담률·**본인부담금**(강조 행)·상태 Badge |
| 인쇄 | Modal **「인쇄」** → `window.print()` — `body.ds-statement-printing` 스코프 (Q175) |
| API | `GET /api/v1/guardian/clients/{clientId}/billing` — **BE `598d108` Fixed** (Q108) |
| 범위 | **열람 전용** — CMS·간편결제·알림 발송 없음 (모달 하단 안내) |

명세가 비어 있으면 센터에서 청구 **확정** 여부를 확인하세요. 금액·상태가 `-`이면 API 필드 fallback(`yearMonth`·`copayAmount`·`status`)을 확인합니다 (Q98·Q83).

### Q133. NHIS import 화면 상단에 Chrome 안내·4단계 절차가 보여요.

**A.** **Fixed (FE `1220bfb`·`2b6024a`·`0abf164`, BE `9a97a1c`, QA-B24, US-G04)** — `NHISImportPage`(`/billing/imports/nhis`) 상단 **`NhisImportGuidePanel`**이 **정적 4단계 안내**와 **실서버 guidance API**를 함께 표시합니다 (Q111 UI 연동).

| 항목 | 내용 |
|------|------|
| 브라우저 안내 | **Chrome 또는 Edge 필수** — IE 미지원 (`Alert` info) |
| 4단계 | ① longtermcare.or.kr 로그인 → ② 청구내역상세 엑셀 다운로드 → ③ ogada 업로드 → ④ 대사·미매칭 보정 |
| **실서버 안내** | **`fetchNhisImportGuidanceApi()`** — 페이지 로드 시 배치·청구 목록과 **병렬** 호출 · 응답 `message` 또는 `guidanceMessage` → **warning `Alert`(`role=alert`)** |
| 접근성 | 단계 목록 `aria-label`·실서버 안내 **`role=alert`** |
| 실패 시 | guidance API 오류는 **조용히 무시** — **이미 표시된 실서버 안내는 유지** (`0abf164`, `Promise.allSettled` — 성공·비어 있지 않은 `message`/`guidanceMessage`일 때만 갱신) |

업로드·이력·`BatchProgressSteps`(Q120)는 기존과 동일합니다. import 이력 필드명 갭은 Q100 참고.

> 관련: Q111 · Q209 · USER_MANUAL §4-6-1

---

## 13-17. 입금·대사·월 선택 UI (2026-06-07 21차, UXD 22차)

### Q134. `/billing/payments` 「입금 기록」모달은 무엇인가요?

**A.** **FE `9bdf59f` (US-L01)** — `PaymentPage`의 **`PaymentRecordModal`**이 **수납 입력 모드**를 지원합니다. **BE `598d108` (v2)** 에서 **수납 저장 API가 구현**되었으나 FE 경로·목록 API 갭이 잔존합니다 (Q174).

| 항목 | 내용 |
|------|------|
| 진입 | **청구 → 입금 처리**(`/billing/payments`) — 미수납 행 **「수납」** 버튼 |
| 목록 API | `GET /api/v1/billing/payments?month=&page=&q=` — **미구현** — 목록 **404** 가능 |
| 모달 입력 | **입금일**·**입금액(원)**·**수단**(현금 `CASH` / 계좌이체 `BANK_TRANSFER`)·메모 |
| 저장 API (BE Fixed) | **`POST /api/v1/billing/claims/{claimId}/payments`** `{ paidAt, paymentMethod, amount? }` — **`CONFIRMED`→`PAID`** · V50 메타 · J03 **`BILLING_PAYMENT_RECEIVED`** dispatch |
| FE 호출 (갭) | `POST /api/v1/billing/claims/{claimId}/payment` — **단수 `/payment`** · 본문 `{ amount, method, note, paidAt }` — **404** |
| Vitest | `PaymentRecordModal.test.jsx` — 수납 모드·읽기 전용 모드 |
| 안내 | CMS·간편결제는 v2 |

**Swagger 우회 — 수납 (US-L01)**

```json
POST /api/v1/billing/claims/{claimId}/payments
{ "paidAt": "2026-06-08", "paymentMethod": "CASH", "amount": 150000 }
```

> **우회 (기존)**: `/billing` 목록 **수납완료** 또는 **`PATCH …/status`** `{ "status": "PAID" }` (Q128) — `paid_at`·`payment_method` 없이 상태만 전환.

### Q135. NHIS 대사 상단 요약 바·「비교」모달은 무엇인가요?

**A.** **UXD 22차 + US-G06 강화 (FE `fd4e8f3`·`c510f5c`)** — `ReconciliationPage`(`/billing/nhis-import/:batchId`)에 대사 요약·비교 UI가 있습니다.

| 컴포넌트 | 위치 | 기능 |
|----------|------|------|
| **`ReconciliationSummaryBar`** | 대사 상세 상단 (`BatchProgressSteps` 아래) | 배치 ID·지점·대상 월·배치 상태 + **전체/일치/차이/미매칭** 건수 Badge — sr-only 「N건」 병행 |
| **`NhisReconciliationTable`** | 행 목록 | `MATCH_STATUS` Badge · `DISCREPANCY`/`UNMATCHED` 행 강조 · **`onCompare` 제공 시 `DISCREPANCY` 행만 「비교」** 버튼(행별 `aria-label`에 이용자명) |
| **`DiscrepancyComparePanel`** | **「비교」** 클릭 → Modal(`role=dialog`, 포커스 트랩) | 공단(NHIS) vs ogada **청구액·이용일수** 4열 표 — `caption`·`scope=col`/`scope=row` · 차이는 색 + **「공단 초과/부족」Badge** 텍스트 병행 |

| 항목 | 내용 |
|------|------|
| 청구 상세 링크 | `claimId`가 있으면 Modal 하단 **「ogada 청구 라인 상세 보기」** → `/billing/claims/{claimId}` |
| 통계 | 프론트가 행 목록 `matchStatus`로 **클라이언트 집계** — API `matchedCount`와 무관 |
| 필드 갭 | 요약 `targetMonth`/`branchName`·비교 `nhisAmount`/`ogadaDays` vs API `yearMonth`/`serviceDays`/`amountDifference` (Q101) — **바·모달이 비거나 `-` 표시** 가능 |
| **UNMATCHED 후보 검색** | **`ReconciliationPage`** 하단 폼 (FE `f01e3a8`, UXD-43) | 미매칭 행 선택 → **`SearchInput`**(이름·인정번호) → `GET …/candidates?q=` 후보 목록 → **수동 연결** (`PATCH …/rows/{rowId}/match`) |
| 수동 연결 | `UNMATCHED` **수동 연결**·`PATCH .../rows/{rowId}/match` — **UI 폼 연동 완료** |
| Vitest | `DiscrepancyComparePanel.test` · `NhisReconciliationTable.test` · **`ReconciliationPage.test`**(후보 검색) · `pilotPageFlows` US-G06 E2E |

> Q101의 「DISCREPANCY 비교 후속」은 **UI 구현 완료**. **`UNMATCHED` 후보 검색**도 **UI 구현 완료**(UXD-43). 숫자가 비면 API 필드 매핑(Q101)을 확인하세요.

### Q136. 「대상 월」입력이 달력 형태로 바뀌었어요.

**A.** **UXD 22차 (US-E05·US-G04)** — **`MonthInput`**(`type="month"`) 컴포넌트가 추가되었습니다.

| 화면 | 용도 |
|------|------|
| `/billing/nhis-import` | 공단 엑셀 업로드 **대상 월** 선택 |
| `/attendance/stats` | 출석 통계 **조회 월** 선택 |

| 항목 | 내용 |
|------|------|
| 접근성 | `Field` 라벨과 연결 — 키보드·스크린리더로 월 선택 가능 |
| API 정합 | 출석 통계는 여전히 `yearMonth` 쿼리 vs 백엔드 `from`/`to` **불일치** (Q106) — 월 선택 UI만 개선 |

---

## 13-18. 백엔드 JWT E2E·번들 성능 (2026-06-07 22차, TSR 48·49차)

### Q137. 파일럿 P1–P8이 JWT로 자동 검증된다는 말은 무엇인가요?

**A.** **TSR 48차 (B02 #5, QA-B02 Fixed)** — 백엔드에 **`PilotChecklistJwtE2eTest`**(22 @Test)가 추가되었습니다. USER_STORIES §13 파일럿 체크리스트 P1–P8을 **실제 JWT 필터 체인**(`SecurityConfig` + Bearer 토큰)으로 검증합니다.

| 시나리오 | 검증 API 예시 | 역할 |
|----------|--------------|------|
| **P1** 이용자 등록 | `POST /clients` (`primaryGuardian` 포함) | `branch_admin`, `social_worker` |
| **P2** 수기 체크인 | `POST /attendance/check-in` | `caregiver` |
| **P3** 건강 기록 | `POST /clients/{id}/health/vitals`, `/medications` | `caregiver` |
| **P4** 지점 전환 | `POST /auth/active-branch` | `hq_admin` |
| **P5** 대시보드 | `GET /dashboard/branch`, `/dashboard/hq` | `branch_admin`, `hq_admin` |
| **P6** 월별 청구 | `POST /billing/claims/generate` | `branch_admin` |
| **P7** NHIS import | `POST /billing/imports/nhis` | `branch_admin` |
| **P8** 대사·수동 매칭 | `GET .../candidates`, `PATCH .../rows/{id}/match` | `branch_admin` |

추가로 **7역할 설정 접근**(`sysadmin`만 `/settings`)·**역할 경계**(예: `caregiver`가 청구 생성 불가)를 같은 테스트 클래스에서 확인합니다.

> **현장 사용자에게**: 이 테스트는 **개발·배포 검증용**입니다. 화면 동작과 1:1 대응하지 않을 수 있으며, 프론트 API 경로 불일치(Q83)는 별도 이슈입니다. develop HEAD `mvn test` **249/249 PASS**.

#### Q137-1. 센터장이 보호자 알림 수신 설정을 대신 바꿀 수 있나요?

**A.** **API만 구현됨 (B08 Fixed)** — `branch_admin`·`social_worker`가 연결된 보호자의 설정을 조회·갱신할 수 있습니다.

| 메서드 | 경로 |
|--------|------|
| `GET` | `/api/v1/clients/{clientId}/guardians/{guardianUserId}/notification-preferences` |
| `PUT` | `/api/v1/clients/{clientId}/guardians/{guardianUserId}/notification-preferences` |

본문·응답 스키마는 보호자 본인 API(Q124)와 동일합니다. **프론트 UI 없음** — 이용자 상세·보호자 관리 화면 연동은 v1.1 후속.

### Q138. ogada 웹이 예전보다 빨리 열리나요? (번들 분할)

**A.** **TSR 49차 (FE-15 Fixed, COD 33차)** — 프론트 빌드가 **코드 스플릿**(`vite.config.js` `manualChunks`)으로 변경되었습니다.

| 청크 | 크기 (gzip) | 포함 |
|------|------------|------|
| `react-vendor` | 166 kB (54 kB) | React·React Router |
| `index` | 183 kB (48 kB) | 앱 코드·라우트 |
| `recharts` | 394 kB (108 kB) | 대시보드·건강 차트(Recharts) |

이전 단일 JS **745 kB**(>500 kB vite 경고)에서 **최대 394 kB**로 분할되어, 특히 **모바일·저사양 PC**에서 초기 파싱 부담이 줄어듭니다. 차트가 없는 화면(출석·이용자 등록)은 Recharts 청크 로드를 브라우저가 지연할 수 있습니다.

> **배포 담당**: `npm run build` 후 `dist/assets/`에 3개 JS 청크가 생성되는지 확인하세요 (DEPLOYMENT §5-2). CDN 캐시는 청크별 해시 파일명으로 무효화됩니다.

---

## 13-19. 보호자 초대 수락·레이아웃 유틸리티 (2026-06-07 23차, COD 34차)

### Q139. 보호자 초대 링크(`/guardian/invitations/.../accept`)는 어떻게 쓰나요?

**A.** **백엔드 + 프론트 연동 완료 (V43 + FE `7170b2a`)** — 공개 수락 화면이 API와 연결되었습니다.

| 항목 | 내용 |
|------|------|
| URL 형식 | `https://{서비스도메인}/guardian/invitations/<토큰>/accept` |
| 인증 | 수락 API **공개** — JWT 불필요 |
| 화면 입력 | **이름**·**연락처**·**비밀번호** (`GuardianInvitationAcceptPage`) |
| 수락 본문 | `{ "name", "phone", "password" }` — **이메일 필드 없음**(초대 시 수신 이메일 사용) |
| API | `POST /api/v1/guardian/invitations/{token}/accept` |
| 성공 | `guardian` 계정·`guardian_clients` 연결 → `/guardian` 포털로 이동 |

> 연락처는 **V44** `users.phone_encrypted`·`phone_masked`에 저장되어 이후 알림톡/SMS 수신자로 사용됩니다 (Q148).

### Q140. `ds-form-row`·`ds-action-bar` 같은 클래스는 무엇인가요?

**A.** **COD 34차 (FE-16)** — Must 모달·페이지의 인라인 style을 **디자인 시스템 유틸리티 클래스**(`components.css`)로 통일했습니다.

| 클래스 | 용도 | 예시 화면 |
|--------|------|----------|
| `ds-form-row` | 폼 2열 그리드 | 초대 수락·건강 입력·QR 생성 |
| `ds-action-bar` | 목록 상단 검색·필터·액션 | `/billing`·`/guardians`·`/platform` |
| `ds-month-input` | 월 선택 래퍼 | `MonthInput` (NHIS import·출석 통계) |
| `ds-inline-actions` | 폼 하단 버튼 행 | 초대 수락·모달 푸터 |
| `ds-page-alert` | 페이지 내 Alert 여백 | 오류·성공 메시지 |

**회귀 테스트** — `AttendancePage.layout.test.jsx`·`BillingPage.layout.test.jsx`·`ClientDetailPage.layout.test.jsx`가 레이아웃 클래스 존재를 검증합니다. develop HEAD Vitest **40/199** · WT **44/210**(1 FAIL, Q143).

> 사용자에게 보이는 UI 동작은 변하지 않습니다. Windows **고대비**·`prefers-contrast` 지원은 기존과 동일합니다 (Q115).

### Q141. AppShell 「로그아웃」은 어떻게 동작하나요?

**A.** **FE `42f48e1`** — `AppShell` 상단 우측 **`LogoutButton`**이 세션을 종료합니다.

| 항목 | 내용 |
|------|------|
| 위치 | **`AppShell` 상단 우측** — `BranchSwitcher`·`ThemeToggle` 옆 (로그인·공개 수락 화면 제외) |
| 동작 | 클릭 → `AuthContext.logout()` → `POST /api/v1/auth/logout` → `clearTokens()` → `/login` 이동 |
| 공개 수락 | **`GuardianInvitationAcceptPage`** — `PublicAuthLayout` 카드 레이아웃 (AppShell 없음) |

### Q142. 보호자 알림 V42에서 consent CHECK는 무엇인가요?

**A.** **COD 36차 (2026-06-07, `428ba7d`, B02 #6·B08 #2 Fixed)** — Flyway **V42**가 `guardian_notification_preferences` 테이블에 **수신 동의·시간 무결성** CHECK를 추가했습니다.

| CHECK | 규칙 | 목적 |
|-------|------|------|
| `chk_..._kakao_consent` | `channel_kakao = FALSE` **또는** `consent_at IS NOT NULL` | 알림톡 on 시 **수신 동의 시각** 필수 (개인정보보호법) |
| `chk_..._sms_consent` | `channel_sms = FALSE` **또는** `consent_at IS NOT NULL` | SMS on 시 동일 |
| `chk_..._updated_after_created` | `updated_at >= created_at` | 행 lifecycle 무결성 (V37 패턴) |
| `chk_..._consent_after_created` | `consent_at IS NULL` **또는** `consent_at >= created_at` | 동의 시각 ≥ 등록 시각 |

**앱 동작** — `NotificationPreferenceService.applyUpdate()`가 카카오·SMS를 켤 때 `consent_at = now()`를 자동 기록하므로, **정상 API 경로**로는 CHECK 위반이 없습니다. CHECK는 raw SQL·ORM 우회 방어용 backstop입니다.

**테스트** — `NotificationPreferenceServiceTest` **4 @Test**. develop HEAD **`mvn test` 253/253 PASS**.

> 인앱·Web Push·이메일(무료 채널)은 V42 consent CHECK 대상 **아님**. v2 발송 API·실제 알림톡/SMS 중계는 후속.

### Q143. 이용자 상세 보호자 초대 UI는 어디에 있나요?

**A.** **Fixed (FE `7170b2a`, US-J01)** — `ClientDetailPage`(`/clients/:id`)에 **보호자 초대** 카드가 API와 연동되었습니다.

| 항목 | 내용 |
|------|------|
| 위치 | 이용자 상세 — 기본 정보 카드 아래 **「보호자 초대 (US-J01)」** |
| 초대 발송 | 이메일·관계 입력 → **초대 발송** → `POST /clients/{id}/guardians/invitations` |
| 초대 이력 | **`GuardianInvitationList`** — 상태·만료일·**재발송**·**취소** |
| 수락 후 | 보호자 `/guardian` 포털·알림 수신 설정(Q124) 사용 |

#### `MaskedPhone` (US-K01)

| 항목 | 내용 |
|------|------|
| 표시 | `010-1234-5678` → **`010-****-5678`** (중간 4자리 마스킹) |
| 테스트 | `MaskedPhone.test.jsx`·`GuardianInvitationList.test.jsx` — Vitest **40/40 PASS** |

> **탭·고급 UI 후속** — 이용자 상세 **건강·출석·청구 탭**·`GuardianListCard` 일부 갭 잔존(Q102·Q113). **Recharts**는 UXD-48에서 **Fixed**(Q118·Q119).

### Q144. 보호자 초대 백엔드 V43은 어디까지 구현됐나요?

**A.** **Fixed (2026-06-08, develop `f47ffa1`)** — 보호자 이메일 초대·수락 API가 develop HEAD에 **커밋**되었습니다.

| 구분 | 산출물 | 상태 |
|------|--------|------|
| 마이그레이션 | `V43__guardian_invitations.sql` | **적용 대상** (Flyway) |
| 발송·이력 | `GuardianInvitationController` — POST/GET/POST resend/DELETE | **Fixed** |
| 수락 | `GuardianInvitationAcceptController` — `POST /guardian/invitations/{token}/accept` | **Fixed** (공개, rate limit) |
| 도메인 | `GuardianInvitationService`·`InvitationTokenService`·`InvitationAcceptRateLimiter` | **Fixed** |
| 테스트 | `GuardianInvitationServiceTest` | **Fixed** |

**V43 상태값** (DB CHECK): `PENDING` · `ACCEPTED` · `CANCELLED` · `REVOKED` — **`SENT`/`EXPIRED` 컬럼 없음**. 만료는 `PENDING`+`expires_at` 경과로 판단.

**API 요약** (API_SPEC §4-1)

| 메서드 | 경로 | 설명 |
|--------|------|------|
| POST | `/clients/{clientId}/guardians/invitations` | `{ "email", "relationship", "channel": "EMAIL" }` — 초대 발송 |
| GET | `/clients/{clientId}/guardians/invitations` | 초대 이력 (`branch_admin`·`social_worker`·`hq_admin`) |
| POST | `/clients/{clientId}/guardians/invitations/{id}/resend` | 재발송 (기존 PENDING → REVOKED) |
| DELETE | `/clients/{clientId}/guardians/invitations/{id}` | PENDING 취소 |
| POST | `/guardian/invitations/{token}/accept` | `{ "name", "phone", "password" }` — 공개 수락·JWT 발급 |

> develop HEAD **`mvn test` 152/152 PASS**. **프론트** `7170b2a` — 이용자 상세 **초대 발송·이력**·공개 **수락 화면** 연동(Q139·Q143). Swagger 없이도 현장 UI로 검증 가능합니다.

### Q145. 보호자 초대는 SMS가 아니라 이메일만인가요?

**A.** **예 (2026-06-07, 결정 59, REQUIREMENTS §8-1)** — v1.1 US-J01 보호자 초대 채널은 **이메일 링크 단일**입니다. SMS·카카오 알림톡 초대는 **v2**(US-J03) 후속입니다.

| 항목 | v1.1 정책 |
|------|----------|
| 채널 | **`EMAIL` 단일** — 보호자 **이메일**로 초대 URL 발송 |
| 초대 링크 | `https://{서비스도메인}/guardian/invitations/{token}/accept` |
| 토큰 만료 | **7일** (가정) — 만료 시 센터장 **재발송** |
| 재발송 | 동일 이메일 재발송 시 **이전 토큰 무효화** |
| 수락 후 | 보호자가 비밀번호 설정 → `guardian` 계정·`guardian_clients` 연결 |

**현장 절차 (UI 연동, `7170b2a`)**

1. 이용자 등록 시 **대표 보호자 이메일**을 정확히 입력합니다 (Q92). (`/clients/new` 폼은 **후속** — 당분간 Swagger·기존 등록 API)
2. 이용자 상세 → **보호자 초대** — 이메일·관계 입력 후 **초대 발송** (Q143).
3. 보호자가 메일 링크 → **`/guardian/invitations/{token}/accept`** 에서 이름·연락처·비밀번호 입력 (Q139).
4. 보호자 포털 **`/guardian`** — 오늘 기록·본인부담금 명세 열람 (Q148·US-J02).

> 이메일이 없으면 Swagger `POST /users`(guardian) + `POST /clients/{id}/guardians` 우회(Q123).

### Q147. 출석 체크인하면 보호자에게 알림이 가나요?

**A.** **백엔드 발송 연동 (J03, `78e8928`)** — 출석·청구·건강 기록 시 `NotificationService.dispatchClientEvent`가 호출됩니다.

| 항목 | 내용 |
|------|------|
| 이벤트 | `ATTENDANCE_CHECK_IN` · `ATTENDANCE_CHECK_OUT` · **`BILLING`** · **`DAILY_CARE`**(투약·케어 메모) · **`EMERGENCY`**(낙상 등 긴급 사고) |
| 트리거 | `AttendanceService` · `BillingService` · **`HealthRecordService`** — **`createVitals`·`createMedication`·`createNote` → DAILY_CARE** (`0832fbf` vitals 추가), `createIncident`(긴급 유형) → **EMERGENCY** |
| 수신자 | 연결 보호자 — `notifyAttendance`·`notifyDailyCare`·`notifyBilling`·`notifyEmergency` preference on |
| 채널 | **`channelEmail`**(BE `fbedcc3`, Q204) · `channelKakao`·`channelSms` — **기본 stub** (`NOTIFICATION_PROVIDER=stub`) |
| 방해 금지 | **22:00–08:00 KST** — **`EMERGENCY`만 우회** |
| 이력 | `notifications` 테이블 — V45 `sent_at` CHECK (FAQ Q150). **조회 API** — `GET /guardian/notifications`·`GET /clients/{clientId}/notifications` (Q152) |

**운영 중계** — `NOTIFICATION_PROVIDER=solapi` + `SOLAPI_*` 설정 시 Solapi 알림톡·SMS 발송(Q148). **이메일**은 **`StubEmailProvider`**(dev) — 보호자 계정 **`users.email`** 기반(Q204). **`NotificationAlimtalkDispatchE2eTest`**·**`J03AlimtalkServiceFlowE2eTest`**(Q156)·**`J03EmailServiceFlowE2eTest`**(Q204)로 E2E 검증.

### Q148. Solapi 알림톡·보호자 휴대폰(V44)은 어떻게 설정하나요?

**A.** **J03 v2 (`136239e`)** — 보호자 초대 **수락 시 입력한 연락처**가 V44로 암호화 저장되고, 알림 발송 시 수신자로 해석됩니다.

| 항목 | 내용 |
|------|------|
| DB | Flyway **V44** — `users.phone_encrypted`(AES-GCM)·`phone_masked`(`010-****-5678`) |
| 수집 시점 | `POST /guardian/invitations/{token}/accept` 본문 `phone` |
| Provider | `ogada.notification.provider` — **`stub`**(기본) 또는 **`solapi`** |
| 필수 env (solapi) | `NOTIFICATION_PROVIDER=solapi`, `SOLAPI_API_KEY`, `SOLAPI_API_SECRET`, `SOLAPI_SENDER_ID`, `KAKAO_PF_ID` |
| 템플릿 | `KAKAO_TPL_ATTENDANCE_ARRIVAL` 등 — Solapi에 등록된 템플릿 ID와 매핑 |

> **초대 채널(Q145)** 은 여전히 **이메일 단일**입니다. SMS·알림톡은 **수락 후 운영 알림(J03)** 용도입니다. 스테이징은 **stub**로 `notifications` 행만 검증하세요 (DEPLOYMENT §8-1).

### Q146. 지점명이 「이미 존재」한다고 나오는데 글자가 달라 보여요.

**A.** **V40 (2026-06-06)** — 지점명은 Tenant(법인) 내에서 **대소문자를 구분하지 않고** 유일해야 합니다.

| 예시 | 결과 |
|------|------|
| 기존 `행복점` + 신규 `행복점` | ❌ 중복 |
| 기존 `Happy Care` + 신규 `happy care` | ❌ 중복 (DB `lower(name)` UK) |
| 기존 `○○점` + 신규 `△△점` | ✅ 다른 이름이면 허용 |

| 항목 | 내용 |
|------|------|
| DB | `uq_branches_org_name_lower (organization_id, lower(name))` |
| 앱 | `BranchService.existsByOrganizationIdAndNameIgnoreCase` — 등록·수정 전 검사 |
| HTTP | `409 CONFLICT` |
| 대칭 정책 | 직원 이메일도 Tenant 내 `lower(email)` UK (V30, USER_MANUAL §5-3) |

**현장 대응**: 지점명에 의도적 대소문자 구분을 넣지 말고, 구분이 필요하면 **접미사**(예: `행복점 2관`)를 사용하세요.

### Q149. v1.2 P1 Must 화면 프론트(`c510f5c`)란 무엇인가요?

**A.** UXD 36차 이후 develop HEAD는 **Must API 연동 + 15개 정식 Must UI**입니다. FE `c510f5c`에서 **NHIS DISCREPANCY 비교 Modal**(US-G06, `fd4e8f3`)·`pilotPageFlows` US-G06 E2E가 추가되었고, FE `95b92b9`의 **건강·투약·사고 입력·저장 API 정합 Fixed**(Q154·UXD-41)·**활력징후 비정상 경고**(UXD-40, Q155)·`c5708c7`(UXD-39) 건강·NHIS UI·`a627c6d` **수기 출석 UI(US-E01·E02)**·QR 저장(US-E03)·출석 통계 UI(US-E05)를 포함합니다.

| 항목 | v1.2 P1 Must 화면 (`c510f5c`) |
|------|-------------------------------|
| `App.jsx` 라우트 | **38개** — Must 전 화면 + **배차 3** + **식사·프로그램 2** + 공개 수락·forbidden |
| **ModulePage** | **라우트에서 제거** — import만 잔존 |
| **FE `c510f5c` 추가** | **`DiscrepancyComparePanel`** — `claimHref`·접근성 표 · **`NhisReconciliationTable` `onCompare`** · `pilotPageFlows` US-G06 |
| **FE `95b92b9` 포함** | **`IncidentRecordForm`** — US-F03 · **`buildIncidentApiPayload`** `detail` 정합 |
| **FE `4957bd3` 포함** | **`healthApiPayload.js`**·**`healthRecords.js`** · **`vitalsRanges.js`** (Q154·Q155) |
| **FE `c5708c7` 포함 (UXD-39)** | **`HealthPage`** `VitalsRecordForm`·`MedicationRecordForm` · **`HealthDetailPage`** 표 추이 · **`NhisReconciliationTable`** |
| **FE `a627c6d` 포함** | **`AttendancePage`** 입소·귀가·결석 · **`QrGeneratePage`** QR 저장·인쇄 · **`AttendanceStatsPage`** |
| 네비게이션 | `navConfig.js` **2단 SideNav** + `SessionTimeoutProvider` + JWT **메모리** |
| 연동 Must | P1–P8·J01·J02 + **DashboardWidgetGrid**·**FilterChips**·**HealthAlertList** |
| **FE `8a764df` 추가** | **UXD-48 Recharts** — `ChartContainer`·`AttendanceRateChart`·`BranchCompareChart`·`HealthTrendChart` · Vitest **60/183** |
| **잔여 갭** | roster·QR·통계 **API 정합**(Q94·Q109·Q106·Q151) · **건강 추이 `?days=`**(Q165) · **입금·보호자 목록 API** · **이용자 상세 건강 탭** |
| **FE `e8d1854` 추가** | **`TransportPage`**·`TransportRunNewPage`·`TransportRunDetailPage` — v1.3-A 배차 (Q159) |
| **FE `362dbf0` 추가** | **`MealsPage`·`ProgramsPage`** — v3 Should **FE·BE 연동** (Q160) · **`pilotPageFlows`** US-N01·US-N02 |
| **BE `dfd9be2` 추가** | **`/api/v1/meals/*`·`/programs/*` Fixed** — V49 (Q160) · **식단·일정 등록 API 미구현** (Q161) |
| **BE `53a1ffe`** | **`/api/v1/transport/*` Fixed** — roster·runs·confirm·geocode (Q159) |
| 테스트 | Vitest **53파일/157건** — transport·meals·programs 테스트 추가 |

**현장 사용 가이드**

1. **건강 기록** — `/health` **4탭**(일일 건강·투약·낙상·특이사항·이력) UI **저장 Fixed**(Q154·Q95·UXD-41).
2. **NHIS 대사** — `DISCREPANCY` 행 **「비교」** Modal로 공단 vs ogada 확인 (Q135).
3. **수기 출석** — `/attendance` 버튼 사용. 이름·상태가 비면 Swagger(Q94).
4. **QR** — 생성 UI + 저장·인쇄(US-E03). API 오류 시 Swagger(Q109).
5. **입금 API** — coder 후속. Recharts는 **UXD-48 Fixed**(Q118·Q119).

### Q151. 새로 생긴 Must 화면인데 저장·조회가 실패해요.

**A.** **UXD 36차 (`0d83a42`)** — 15개 Must 페이지가 **`ModulePage` 대신 정식 UI**로 교체되었으나, 다수가 **`fetch()` 직접 호출**로 백엔드 정식 API와 **경로·본문·응답 래퍼**가 다릅니다 (Q83 확장).

| 화면 | 프론트 (현재) | 백엔드 정식 | 증상 |
|------|--------------|------------|------|
| ~~**건강 입력 (`/health`)**~~ | ~~`bloodSugar`·`description`→`detail` 갭~~ | ~~`bloodGlucose`·`administeredAt`·`detail`~~ | **Fixed** (`95b92b9`, Q154·Q95·UXD-41) |
| 보호자 목록 (`/guardians`) | `GET /guardians?page=&q=` | `GET /users?branchId=` (guardian 필터) | 목록 **404** (Q107) |
| 입금 처리 (`/billing/payments`) | `GET /billing/payments` · `POST /claims/{id}/payments` | **`POST /claims/{id}/payments` Fixed** · 목록 claims **우회**·UI Fixed (Q198) | 전용 목록 API **갭** (Q134·Q174) |
| 지점 (`/branches`) | `GET /branches?page=&q=` | `GET /branches` (List 또는 page) | 빈 목록·페이지 UI만 동작 |
| 플랫폼 (`/platform`) | `?q=` · `{ items }` 기대 | `?query=` · List 직접 반환 | 검색·목록 실패 (Q97) |
| 수가표 | `GET /billing/fee-schedule` | `GET /billing/fee-schedules?year=` | **404** |
| 설정 조직 | `GET/PATCH /settings/organization` | `GET/PATCH /organization/settings` | 토글 저장 **404** (Q116) |
| QR 생성 | `POST /branches/current/qr` `{ type }` | `POST /branches/{branchId}/qr` `{ direction }` | QR 생성 실패 (Q109) |
| QR 스캔 | `/attendance/checkin/qr` `{ token, type }` | `{ qrToken, clientId }` | 스캔 실패 |
| 이용자 등록 | `birthdate`·`ssn`·`primaryGuardian.name` | `birthDate`·`residentRegistrationNo`·`guardianUserId` | **400** (Q92) |
| 출석 통계 | `?yearMonth=` | `?from=&to=` | StatCard 빈 값 (Q106) |

**우회** — Swagger로 동일 업무 수행. **정식 수정** — `services.js`·각 Page의 `fetch` 경로를 API_SPEC에 맞게 정합 (`PLAN_NOTES.md` TWR-Q1).

> **ModulePage는 더 이상 SideNav 대상 경로에 사용되지 않습니다** — 「구현 진행 중」 안내 대신 **실제 UI + API 오류 Alert**가 표시됩니다.

### Q150. Flyway V45는 무엇을 추가하나요?

**A.** **BE `78e8928`** — J03·V44 후속 무결성 강화입니다.

| 대상 | CHECK/제약 | 목적 |
|------|-----------|------|
| `users` | `chk_users_phone_pair` | `phone_encrypted`·`phone_masked` **쌍으로만** 저장 (V44) |
| `notifications` | `chk_notifications_sent_requires_at` | `SENT` ⇒ `sent_at` NOT NULL |
| `notifications` | `chk_notifications_sent_after_created` | `sent_at` ≥ `created_at` |
| `guardian_notification_preferences` | `fk_…_user_org` + role guard 트리거 | Tenant 스코프 FK·`guardian` 역할만 |
| `guardian_invitations` | `idx_…_email_pending` partial | PENDING 초대 이메일 조회 |

스테이징: stub provider로 체크인·건강 기록 후 `notifications` 행의 `status`·`sent_at` 정합 확인 (DEPLOYMENT §8-1).

### Q152. 보호자·직원이 알림톡/SMS 발송 이력을 조회할 수 있나요?

**A.** **Fixed (`e39164d`, BNK-22, US-J03-h)** — **화면 UI + API** 모두 제공됩니다. 케어포 **10-7 안내발송내역** 패리티를 목표로, **수신 연락처는 표시하지 않습니다**(PIPA).

| 구분 | 화면 | API | 권한 |
|------|------|-----|------|
| **보호자 본인** | `/guardian` → **「알림 이력」** 탭 · **`NotificationHistoryPanel`** | `GET /api/v1/guardian/notifications?page=0&size=20` | `guardian` |
| **직원(이용자별)** | `/clients/:id` → **「보호자 알림 이력 (US-J03)」** 카드 | `GET /api/v1/clients/{clientId}/notifications?page=0&size=20` | `branch_admin`, `social_worker` |

**표시 항목**: **발송 시각** · **채널**(`StatusBadge`, KAKAO/SMS 등) · **유형**(`notificationEventLabel` — 출석·일일 케어·본인부담금·입금 확인·긴급 등) · **상태**(`PENDING`/`SENT`/`FAILED`).

| 규칙 | 내용 |
|------|------|
| Tenant 격리 | JWT `organization_id` 강제 |
| 보호자 | 본인 수신 이력만 |
| 직원 | 연결 보호자들의 해당 이용자 관련 이력 — 지점 스코프 검증 |
| 페이지 | UI **`Pagination`** — `page` 0부터, `size` 20 |
| 빈 목록 | stub 환경·알림톡 미연동 시 「알림 이력 없음」 — **정상** (Q147) |

**스모크** — stub 환경에서 체크인 후 보호자 포털 **「알림 이력」** 탭 또는 Swagger `GET /guardian/notifications` → `items[]` 1건 이상·`sentAt` NOT NULL (DEPLOYMENT §8-1). 상세 UI는 **Q187** 참고.

### Q153. Flyway V46은 무엇을 추가하나요?

**A.** **BE `8ce1151`** — J03 알림 이력 조회 API(`c53dd3b`) 성능용 인덱스입니다.

| 대상 | 인덱스 | 목적 |
|------|--------|------|
| `notifications` | `idx_notifications_org_recipient_created (organization_id, recipient_user_id, created_at DESC)` | `GET /guardian/notifications`·`GET /clients/{id}/notifications` Tenant+수신자+시각 정렬 조회 가속 |

기존 V2 인덱스(`idx_notifications_recipient`·`idx_notifications_org_created`)는 **organization_id+recipient_user_id 복합 prefix**가 없어 대량 Tenant 환경에서 이력 페이지네이션이 느려질 수 있었습니다. V46은 **조회 전용** — 애플리케이션 동작 변경 없음.

### Q154. `/health`에 건강·투약 입력 폼이 생겼는데 저장이 실패해요.

**A.** **Fixed (`95b92b9`, Q154 + UXD-41)** — `/health` **4탭 UI**가 **`healthApiPayload.js`** 로 백엔드 DTO와 **정합**되어 **바이탈·투약·사고 저장이 UI에서 동작**합니다 (Q95).

| 구성 | 설명 |
|------|------|
| **`VitalsRecordForm`** | 수축/이완기 혈압·체온·혈당·SpO₂ — `buildVitalsApiPayload` → `bloodGlucose`·`recordedAt` |
| **`MedicationRecordForm`** | 약품명·용량·시간 — `buildMedicationApiPayload` → `administeredAt`·`administeredBy`·`recordedAt` |
| **`IncidentRecordForm`** (UXD-41, US-F03) | 이벤트 유형·내용·발생 시각 — `buildIncidentApiPayload` → `incidentType`·**`detail`**·`recordedAt` |
| **`MedicationDuplicateAlert`** | 동일 약품·시간 **클라이언트 중복 경고** |
| **`HealthAbnormalBanner`** | 비정상 수치 요약 (대시보드 알림과 연계) |
| **비정상 범위 경고 (UXD-40)** | 필드 아래 **인라인 경고** — 저장 **비차단** (Q155) |
| **기록 이력 탭** | `healthRecords.js` — 바이탈·투약·**사고** `items[].payload` 파싱 |

**관련** — `/health/:clientId` **표 형식 추이**(Q119), NHIS **`NhisReconciliationTable`**(Q101), J03 **바이탈 DAILY_CARE·낙상 EMERGENCY dispatch**(Q147·Q156, BE `0832fbf`·`4c74f84`).

**잔여** — **이용자 상세 건강 탭**은 별도 fetch 갭(Q102). **특이사항 자유 메모**(`POST …/health/notes`) UI **미포함**.

### Q155. `/health` 입력 시 혈압·체온 아래 노란 경고가 떠요. 저장이 안 되나요?

**A.** **UXD-40 (`9863312`, US-F01)** — **`vitalsRanges.js`** 단일 원천으로 **정상 범위를 벗어난 수치**에 **필드 아래 경고**(`role="status"`, `polite`)를 표시합니다. **저장은 차단하지 않습니다** — 요양보호사가 의도적으로 비정상 수치를 기록할 수 있습니다.

| 항목 | 정상 범위 (참고치) | 비정상 예 |
|------|-------------------|----------|
| 수축기 혈압 | 90–140 mmHg | ≥140 또는 ≤90 |
| 체온 | 35.5–37.5 °C | ≥37.5 또는 ≤35.5 |
| 혈당 | 70–200 mg/dL | ≥200 또는 ≤70 |
| SpO₂ | 92% 이상 | &lt;92 |

> **접근성** — 경고는 **텍스트 + `--color-warning-text` 색**을 병행합니다. 색상만으로 의미를 전달하지 않습니다 (USER_MANUAL §3-2).

> **`HealthAbnormalBanner`**(당일 요약)와 **`HealthPage` 이상 감지**도 동일 `vitalsRanges.js`를 사용합니다.

### Q156. J03 알림톡 서비스 플로우는 어떻게 검증하나요?

**A.** **BE `32a1f8f`·`52e0621`** — **`J03AlimtalkServiceFlowE2eTest`**(**8 @Test**)가 **도메인 서비스 레이어**에서 출석·건강·청구 이벤트 → `NotificationService` → stub provider → `notifications` 이력까지 **End-to-End**를 검증합니다.

| 검증 범위 | 내용 |
|----------|------|
| 출석 | 체크인·**체크아웃** dispatch (`AttendanceServiceTest` 확장 포함) |
| 건강 | 바이탈·투약·메모 → **`DAILY_CARE`** |
| 청구 | 청구 확정(`CONFIRMED`) → **`BILLING`** · 수납 완료(`PAID`) → **`BILLING_PAYMENT_RECEIVED`** (`52e0621`, Q159) |
| 긴급 | 사고 → **`EMERGENCY`** (방해 금지 우회) |

스테이징: **`NOTIFICATION_PROVIDER=stub`** 으로 `mvn test` **224/224 PASS** 확인 후, 체크인·건강 기록·청구 **PAID** 전환 → `notifications` 행·`GET /guardian/notifications` 이력 조회 (DEPLOYMENT §3-6·§8-1, Q147·Q152·Q159).

### Q157. Solapi 알림톡 템플릿 변수는 어떻게 매핑되나요?

**A.** **BE `4c74f84`·`ac17ad8`·`52e0621`** — **`AlimtalkTemplateVariables`** 가 `notifications.payload` JSON을 Solapi **`kakaoOptions.variables`** 로 변환합니다. `NOTIFICATION_PROVIDER=solapi` 시 **`SolapiKakaoAlimtalkProvider`** 가 발송 직전 호출합니다.

| ogada 템플릿 코드 | payload → variables 키 |
|-------------------|------------------------|
| `ATTENDANCE_ARRIVAL` / `ATTENDANCE_DEPARTURE` | `clientId`, `attendanceDate` |
| `DAILY_CARE_SUMMARY` | `clientId`, `category`, `detail` |
| `EMERGENCY_ALERT` | `clientId`, `category`, `detail` — **`incidentType`도 `category` alias** (`ac17ad8`) |
| `BILLING_STATEMENT` | `clientId`, `yearMonth`, `copayAmount` |
| `BILLING_PAYMENT_RECEIVED` | `clientId`, `yearMonth`, `copayAmount` — **`CONFIRMED`→`PAID` 전환 시** (`52e0621`, Q159) |

| 규칙 | 내용 |
|------|------|
| 변수 키 | Solapi **사전 승인 템플릿** placeholder와 **1:1 정합** 필요 |
| payload 누락·파싱 실패 | **빈 variables** — **`AlimtalkFallbackText`** 한국어 SMS 본문으로 relay (Q158) |
| 환경변수 | `KAKAO_TPL_*` — ogada 내부 코드 → Solapi `templateId` (DEPLOYMENT §4-5) |
| 테스트 | **`AlimtalkTemplateVariablesTest`** · **`AlimtalkFallbackTextTest`** · **`SolapiKakaoAlimtalkProviderTest`** HMAC·templateId·fallback 검증 |

**운영 절차** — Solapi 콘솔에서 template placeholder 이름을 위 표와 **동일하게** 등록한 뒤, 스테이징에서 stub → solapi 전환·체크인·건강 기록 후 Solapi 발송 로그와 `notifications.status=SENT`를 대조하세요 (ADMIN_GUIDE §10-8).

### Q158. 알림톡 실패 시 SMS fallback 문구는 어떻게 생성되나요?

**A.** **BE `ac17ad8`·`52e0621`** — **`AlimtalkFallbackText`** 가 Kakao 알림톡 전달 실패 시 **`SolapiSmsProvider`** relay용 **한국어 SMS 본문**을 생성합니다. 내부 `templateCode`·원시 UUID는 **노출하지 않습니다**.

| ogada 템플릿 | SMS fallback 예시 |
|-------------|-------------------|
| `ATTENDANCE_ARRIVAL` | `[ogada] 이용자가 센터에 도착했습니다. (YYYY-MM-DD)` |
| `ATTENDANCE_DEPARTURE` | `[ogada] 이용자가 센터에서 귀가했습니다. (YYYY-MM-DD)` |
| `DAILY_CARE_SUMMARY` | `[ogada] 일일 케어 기록: {category} - {detail}` |
| `EMERGENCY_ALERT` | `[ogada] 긴급 알림: {category} - {detail}` — **`incidentType` → category** |
| `BILLING_STATEMENT` | `[ogada] {yearMonth} 본인부담금 명세: {copayAmount}원` |
| `BILLING_PAYMENT_RECEIVED` | `[ogada] {yearMonth} 본인부담금 수납 완료: {copayAmount}원` (`52e0621`, Q159) |
| 기타/파싱 실패 | `[ogada] 새 알림이 도착했습니다.` |

| 규칙 | 내용 |
|------|------|
| 접두사 | 모든 본문 **`[ogada] `** 로 시작 |
| 상세 길이 | `detail`·`category` **80자 초과 시 `...` 절단** |
| Provider 연동 | `SolapiKakaoAlimtalkProvider`·`SolapiSmsProvider`가 **`AlimtalkFallbackText.from(templateCode, payloadJson)`** 호출 |
| 테스트 | **`AlimtalkFallbackTextTest`** · **`AlimtalkTemplateVariablesTest`** incident alias · **`SolapiKakaoAlimtalkProviderTest`** fallback body 검증 |

> **운영**: Solapi 콘솔에서 알림톡·SMS **동일 발신번호** 등록 여부를 확인하세요. stub 환경에서는 SMS가 실제 발송되지 않고 `notifications` 이력만 적재됩니다 (Q147).

### Q159. SideNav 「배차」메뉴·본인부담금 수납 알림·transport API는 무엇인가요?

**A.** **BE `53a1ffe` + FE `7ef1083`·`f0b174a`** — J03 수납 알림, v1.3-A **배차 UI·API 연동**, 배차 접근성 재점검이 반영되었습니다.

#### 본인부담금 수납 알림 (J03, BE `52e0621`)

| 항목 | 내용 |
|------|------|
| 트리거 | `BillingService.updateClaimStatus` — 상태 **`CONFIRMED` → `PAID`** |
| 이벤트 | **`BILLING_PAYMENT_RECEIVED`** (`NotificationEventType`) |
| 템플릿 | **`BILLING_PAYMENT_RECEIVED`** — Solapi `KAKAO_TPL_BILLING_PAYMENT` (DEPLOYMENT §4-3) |
| 수신 조건 | 보호자 preference **`notifyBilling=true`** (B08) |
| SMS fallback | `[ogada] {yearMonth} 본인부담금 수납 완료: {copayAmount}원` (Q158) |
| 테스트 | **`J03AlimtalkServiceFlowE2eTest.billingClaimPaymentShouldPersistSentAlimtalkNotification`** · **`BillingServiceTest`** |

> **현장**: 입금 처리 UI(`PaymentPage`)는 **백엔드 입금 API 미구현**(Q134). 청구를 `PAID`로 바꾸는 작업은 Swagger **`PATCH /billing/claims/{id}/status`** `{ "status": "PAID" }`로 수행할 수 있으며, 성공 시 보호자에게 수납 알림이 dispatch됩니다 (stub 환경에서는 `notifications` 이력만 생성).

#### 배차·이동경로 (v1.3-A, BE `53a1ffe` + FE `e8d1854`/`f0b174a`, US-T01~T03)

| 화면 | 경로 | 역할 | 기능 |
|------|------|------|------|
| 배차 홈 | `/transport` | `hq_admin`·`branch_admin`·`caregiver`·`social_worker` | 당일 픽업 명단·운행 루트 목록·운행일 선택 |
| 새 픽업 배차 | `/transport/runs/new` | **`hq_admin` only** | 명단 다중 선택·수동 순서·지도 미리보기·**임시 저장(DRAFT)** |
| 루트 상세 | `/transport/runs/:runId` | `hq_admin`(편집·**확정 취소**) · 직원(**`CONFIRMED`만** 조회) | 정차 목록·**KakaoTransportMap**·배차 확정·**TransportUnconfirmModal**(Q163) |

| 항목 | 내용 |
|------|------|
| SideNav | **`navConfig.js` 「이동」** 그룹 — **배차·이동경로** |
| 고지 | **`TransportDisclaimer`** — 운영 편의용·이동서비스비 청구(G15) **미포함**·경로 최적화는 v1.3-B |
| 정원 | **`MAX_TRANSPORT_STOPS=15`** — 초과 시 저장 차단 |
| **백엔드 API** | **`/api/v1/transport/*` Fixed** — roster·runs CRUD·confirm·**unconfirm PATCH+POST alias**(Q163·Q164)·geocode (ADMIN_GUIDE §10-10) |
| **확정 취소 UI** | **`hq_admin`** — 루트 상세 **「확정 취소」** → **`TransportUnconfirmModal`** (UXD-47, `73f7d39`) |
| 지도 | **`VITE_KAKAO_MAP_JS_KEY`**(프론트 **`loadKakaoMapSdk`**) + **`KAKAO_REST_KEY`**(서버 geocode·경로) — **`kakaoMapInstance.js`**·**`KakaoTransportMapView`** 도로 경로 Polyline (**Q370·Q394·Q395**, FE `5ebaade`) |
| 이용 조건 | 이용자 **`usesTransport=true`** — **BE `1ec538b` + FE `3c55339`에서 `POST/PATCH /clients` DTO·`ClientFormPage` UI 연동 Fixed**(Q166) |

**현장 대응**: 배차 명단이 **비어 있으면** 해당 이용자에 `usesTransport=true`가 설정되지 않았을 수 있습니다. **이용자 등록·수정** 화면 **「배차·픽업 정보」**에서 설정하거나, Swagger **`PATCH /api/v1/clients/{id}`** 로 설정하세요 (Q166·USER_MANUAL §4-3·§5-8).

### Q160. SideNav 「식사 관리」·「프로그램 관리」메뉴는 무엇인가요?

**A.** **BE `dfd9be2` + FE `362dbf0`** — REQUIREMENTS **§3-5·§3-6 (Should, v3)** 기능입니다. **섭취·참여 기록 API는 FE·BE 연동 완료**입니다.

| 화면 | 경로 | 역할 | 기능 |
|------|------|------|------|
| 식사 관리 | `/meals` | `hq_admin`·`branch_admin`·`caregiver`·`social_worker` | **기록일** 선택 → `GET /meals/menus` 당일 식단 · `GET /meals/records` 섭취 목록 · **`MealRecordForm`** → `POST /meals/records` |
| 프로그램 관리 | `/programs` | 동일 4역할 | **기록일** 선택 → `GET /programs/schedule` 일정 · `GET /programs/participations` 참여 목록 · **`ProgramParticipationForm`** → `POST /programs/participations` |

| 항목 | 내용 |
|------|------|
| SideNav | **기록** 그룹 — 건강 기록 아래 **식사 관리**·**프로그램 관리** |
| 백엔드 API | **`MealController`**·**`ProgramController`** — RBAC 4역할 · active branch 스코프 |
| DB | **Flyway V49** — `meal_menus`·`meal_records`·`activity_programs`·`program_participations` |
| 테스트 | **`MealServiceTest`**·**`MealControllerRoutingTest`**·**`ProgramServiceTest`**·**`ProgramControllerRoutingTest`** · **`pilotPageFlows`** US-N01·US-N02 · **`mvn test` 224/224** · Vitest **54/164** |
| MVP 범위 | **Must 아님** — v3 Should. Must 파일럿 검증 대상 **외** |

**POST `/meals/records` 본문 예시**

```json
{
  "clientId": "uuid",
  "mealType": "LUNCH",
  "intakeLevel": "NORMAL",
  "dietRestriction": "NONE",
  "nutritionistNote": null,
  "recordDate": "2026-06-08"
}
```

**POST `/programs/participations` 본문 예시**

```json
{
  "clientId": "uuid",
  "programId": "uuid",
  "status": "ATTENDED",
  "satisfaction": "4",
  "recordDate": "2026-06-08"
}
```

> **등록 UI Fixed (Q161)**: **`hq_admin`·`branch_admin`** 은 `/meals`·`/programs`에서 **`MealMenuForm`·`ProgramScheduleForm`** 으로 당일 식단·일정을 등록할 수 있습니다.

### Q161. 식사 화면에 식단이 비어 있거나 프로그램 일정이 없어요.

**A.** **BE `dfd9be2` + FE `1794e1c` (BNK-19) Fixed** — **조회·기록·등록 API가 모두 구현**되었고, **`hq_admin`·`branch_admin`** 은 화면에서 식단·일정을 등록할 수 있습니다.

| API | 상태 | 설명 |
|-----|------|------|
| `GET /api/v1/meals/menus?date=` | ✅ | 당일 식단 조회 |
| `POST /api/v1/meals/menus` | ✅ | 식단 등록 — `menuDate`·`mealType`·`menuName`·`calories`(선택) |
| `GET/POST /api/v1/meals/records` | ✅ | 이용자별 섭취 기록 조회·저장 |
| `GET /api/v1/programs/schedule?date=` | ✅ | 당일 프로그램 일정 조회 |
| `POST /api/v1/programs/schedule` | ✅ | 일정 등록 — `scheduleDate`·`programName`·`startTime`·`endTime` 등 |
| `GET/POST /api/v1/programs/participations` | ✅ | 참여·만족도 조회·저장 |

| 항목 | 내용 |
|------|------|
| 스키마 | **V49** — `meal_menus`(지점×일자×`BREAKFAST`/`LUNCH`/`SNACK` UK) · `activity_programs`(지점×일자 프로그램) |
| 화면 | `/meals` — **`MealMenuForm`**(관리 역할만) · `/programs` — **`ProgramScheduleForm`**(관리 역할만) |
| 빈 목록 | **데이터 미등록** — `caregiver`·`social_worker`는 등록 폼 없음. 관리자에게 등록 요청 |
| 참여 저장 | 프로그램 일정이 없으면 **`ProgramParticipationForm`에서 프로그램 선택 불가** |

**현장 대응**

1. **`hq_admin`·`branch_admin`**: SideNav **기록 → 식사·프로그램 관리**에서 **기록일** 선택 후 식단·일정을 등록합니다 (USER_MANUAL §5-9).
2. **섭취·참여 기록**: 식단·일정 등록 후 **`MealRecordForm`·`ProgramParticipationForm`** 저장이 정상 동작합니다 (`pilotPageFlows` US-N01·US-N02).
3. **퇴소 이용자**: V49 가드로 섭취·참여 **INSERT 거부** — 활성 이용자만 기록 가능합니다.

> 상세 조작: USER_MANUAL §5-9 · API 명세: ADMIN_GUIDE §10-11

### Q162. SideNav 「직원 관리」(`/staff`) 메뉴는 무엇인가요?

**A.** **FE `73f7d39`** — REQUIREMENTS **§3-8 (Should, v3)** 직원 관리 UI입니다. **`hq_admin`·`branch_admin`** 만 SideNav **운영 → 직원 관리**에서 접근할 수 있습니다.

| 화면 | 경로 | 역할 | 기능 |
|------|------|------|------|
| 직원 관리 | `/staff` | `hq_admin`·`branch_admin` | **`GET /users`** 목록 · **+ 직원 등록** 모달 → **`POST /users`** |

| 항목 | 내용 |
|------|------|
| 백엔드 API | **`UserController`** — 목록·생성·수정 (`hq_admin`, `branch_admin`) — 기존 Must API 재사용 |
| UXD-47 (`73f7d39`) | **`StaffRoleSelect`**(요양보호사·사회복지사·지점장·통합 관리자 한국어 라벨) · **`Field`+`TextInput`** 필드 단위 검증(이름·이메일 필수) · 폼 `aria-label`·저장 `aria-busy` |
| 테스트 | **`StaffPage.test`** 4건 · **`StaffRoleSelect.test`** 2건 · **`pilotPageFlows`** `/staff` · **`sevenRoleRouteGuard`** `branch_admin` 허용·`social_worker` 거부 |
| MVP 범위 | **Must 아님** — v3 Should. 근무 일정·근태·자격증 **후속**(REQUIREMENTS §3-8) |

**API 필드 매핑 갭 (현장 주의 — UXD-47 이후에도 잔존)**

| UI·프론트 | 백엔드 DTO | 증상 |
|----------|-----------|------|
| `name` | `displayName` | 목록 **이름 `-`** 표시 가능 |
| `role` | `roleCode` | 등록 시 **`400 VALIDATION_ERROR`** (`roleCode` 필수) — UI는 `role` 전송 |
| `branchId` | `branchIds[]` | **소속 지점 `-`** — 지점명 조회·다중 지점 배열 미연동 |

**현장 대응**: 등록·수정이 실패하면 Swagger **`POST /api/v1/users`** 로 `{ "email", "displayName", "roleCode", "branchIds": ["uuid"] }` 형식을 사용하세요 (ADMIN_GUIDE §6-3-1). UI DTO 정합은 후속 패치 예정입니다.

> 상세 조작: USER_MANUAL §4-7·§5-3

### Q163. 확정된 배차를 다시 수정하려면 어떻게 하나요?

**A.** **BE `767d977` + FE `73f7d39`** — **`hq_admin`** 이 확정 루트를 **`DRAFT`** 로 되돌린 뒤 순서를 재편집할 수 있습니다. **화면 버튼과 Swagger 모두** 사용 가능합니다.

| 항목 | 내용 |
|------|------|
| **화면 (US-T02, UXD-47)** | `/transport/runs/:runId` — **`CONFIRMED`** 상태에서 **`hq_admin`** 전용 **「확정 취소」** 버튼 → **`TransportUnconfirmModal`** 확인 |
| API (정식) | **`PATCH /api/v1/transport/runs/{runId}/unconfirm`** — **`hq_admin` only** |
| API (레거시) | **`POST …/unconfirm`** — 구 클라이언트·현재 FE `unconfirmTransportRunApi` 호환 alias (Q164) |
| 효과 | `status=DRAFT` — 정차 순서 **재편집 가능** · `unconfirmed_at`·`unconfirmed_by` 기록 (V47) |
| 제한 | 이미 **`DRAFT`** 인 루트는 `422 BUSINESS_RULE` — 확정된 루트만 대상 |
| 직원 조회 | `DRAFT` 루트는 **`branch_admin`·`caregiver`·`social_worker` 목록에서 숨김** — unconfirm 후 직원 화면에서 사라짐 |
| 테스트 | **`TransportServiceTest.unconfirmRunShould*`** 2건 · **`TransportControllerRoutingTest`** PATCH·POST · **`TransportRunDetailPage.test`** · **`MustApiEndpointRoutingTest`** |

**화면 절차 (`hq_admin`)**

1. SideNav **이동 → 배차·이동경로** → 해당 **운행일** 루트 상세(`/transport/runs/:runId`)로 이동합니다.
2. 상태가 **확정(CONFIRMED)** 이면 하단 **「확정 취소」** 버튼을 누릅니다.
3. **`TransportUnconfirmModal`**에서 운행일·정차 수를 확인하고 **확정 취소**를 선택합니다.
4. `DRAFT`로 복원되면 **순서 저장** → **배차 확정**으로 재확정합니다.

**Swagger 절차 (대체)**

1. `hq_admin` JWT로 **Authorize**.
2. **`PATCH /api/v1/transport/runs/{runId}/unconfirm`** 호출 (`POST` alias도 동작).
3. 응답 `status: DRAFT` 확인 후 **`PATCH /runs/{runId}`** 로 순서 수정 → **`POST …/confirm`** 재확정.

> USER_MANUAL §5-8 · ADMIN_GUIDE §10-10

### Q164. 배차 unconfirm API는 PATCH인가요 POST인가요?

**A.** **BE `767d977`** — v1.3-A API 계약상 **정식 메서드는 `PATCH`** 입니다. **`POST …/unconfirm`** 은 구버전·프론트 호환을 위한 **레거시 alias**이며, 동일한 `TransportService.unconfirmRun`을 호출합니다.

| 클라이언트 | 권장 | 비고 |
|-----------|------|------|
| Swagger·신규 연동 | **`PATCH /api/v1/transport/runs/{runId}/unconfirm`** | API_SPEC §12·ADMIN_GUIDE §10-10 |
| 현재 FE (`73f7d39`) | **`POST`** (`unconfirmTransportRunApi`) | alias로 동작 — 후속 PATCH 전환 예정 |
| 구 POST 전용 스크립트 | **`POST`** | 계속 동작 (backward compatibility) |

> 상세: Q163 · USER_MANUAL §5-8

### Q165. 건강 추이에서 7일·30일을 바꿔도 차트가 같아 보여요.

**A.** **UXD-48 (`8a764df`)** — `HealthDetailPage`에 **`HealthTrendChart`** 가 표시되지만, **`FilterChips` 기간 변경이 API `?days=` 쿼리에 반영되지 않습니다**.

| 항목 | 현재 동작 | 기대 동작 |
|------|----------|----------|
| UI | 7일·30일 **FilterChips** 표시 | 선택 기간에 맞는 추이 |
| API 호출 | `GET /clients/{id}/health` (**`days` 미전달**) | `GET /clients/{id}/health?days=7\|30` |
| 차트·표 | 서버 기본 전체 응답을 클라이언트 표시 | 기간 필터링된 데이터 |

**현장 우회** — Swagger·Postman으로 `GET /api/v1/clients/{id}/health?days=30` 을 직접 호출해 기간별 데이터를 확인하세요. 당일 입력·수정은 `/health` **일일 건강·투약 탭**(Q154).

> 관련: Q119 · USER_MANUAL §7-6

### Q166. 배차 명단이 비어 있거나 이용자 픽업 주소를 설정하려면?

**A.** **Fixed (FE `3c55339`, US-T01)** — 이용자 **배차 프로필**은 **`ClientFormPage`** 등록·수정 화면 **「배차·픽업 정보」** 카드에서 설정합니다. 백엔드 **`POST/PATCH /api/v1/clients`** DTO와 연동됩니다.

| 화면 필드 | API 필드 | 용도 |
|----------|---------|------|
| 이동서비스(픽업 배차) 이용 | `usesTransport` | `true`만 **`GET /transport/roster`** 에 표시 (V47) |
| 픽업 주소 | `pickupAddress` | 미입력 시 거주지 주소 · 저장 시 암호화 → 조회 `pickupAddressMasked` |
| 픽업 연락처 | `pickupContact` | 미입력 시 이용자 연락처 → 조회 `pickupContactMasked` |
| 기본 픽업 시각 | `defaultPickupTime` | `HH:mm` — 명단 기본 시각 |

| 규칙 | 내용 |
|------|------|
| 수정 모드 | 입력란은 비워 두고 help에 **마스킹된 기존 값** 안내 — 변경 시에만 새 값 입력 |
| 주소 변경 | 픽업 주소 변경 시 **geocode 캐시 무효화** — 다음 배차 시 `POST /transport/geocode` 재호출 |
| a11y | 픽업 필드 **`role="group"`** · 스크린리더용 **「픽업 상세 정보」** 제목 (UXD-52) |
| 테스트 | **`ClientFormPage.test`** · **`ClientTransportProfileSection.test`** · **`ClientServiceTest`** · **`TransportPilotServiceFlowE2eTest`** US-T01~T03 · Vitest **68/208** · **`mvn test` 241/241** |

**현장 절차** — 배차 명단이 비어 있을 때:

1. SideNav **이용자** → 대상 이용자 **수정** (`/clients/:id/edit`) 또는 **신규 등록**.
2. **「배차·픽업 정보」** — **이동서비스 이용** 체크 · 픽업 주소·연락처·시각 입력 후 **저장**.
3. **`/transport`** — 운행일 선택 후 명단 새로고침.
4. **`hq_admin`** — **새 픽업 배차**로 루트 생성 (USER_MANUAL §5-8).

> API만 사용할 때 — Swagger **`PATCH /api/v1/clients/{id}`** 본문에 동일 필드 전달 가능.

> 관련: Q159 · Q171 · USER_MANUAL §4-3·§5-8 · ADMIN_GUIDE §10-10

### Q167. 통합 대시보드 건강 이상 목록에 지점 이름 Badge가 보여요.

**A.** **UXD-49 (`00375f6`, US-H02)** — `hq_admin` **통합 대시보드**(`/dashboard/hq`)의 **`HealthAlertList`** 가 전 지점 건강 이상에 **지점명 Badge**를 표시합니다.

| 항목 | 내용 |
|------|------|
| 데이터 | `GET /api/v1/dashboard/hq` → `healthAlerts[].branchName` |
| UI | 이용자명 옆 **중립 Badge** — `ds-sr-only` 「지점」 접두 + 지점명 텍스트 (색상만으로 구분하지 않음) |
| 지점 대시보드 | `/dashboard` — 단일 지점 스코프이므로 **Badge 미표시** (하위 호환) |
| 빈 목록 | 「전 지점 건강 이상 알림이 없습니다」 (HQ variant `emptyMessage`) |
| 테스트 | **`HealthAlertList.test.jsx`** +2 (지점명 노출·지점 스코프 미노출) · Vitest **60/189** |

다지점 센터에서 **어느 지점 이용자인지** 한눈에 구분할 수 있습니다. 해당 지점 상세 작업은 **지점 선택기**로 전환 후 `/dashboard`·`/health`에서 진행하세요.

> 관련: Q129 · USER_MANUAL §5-2 · FLOWCHART §8 HQ E3

### Q168. 배차·이동경로 화면에서 Windows 고대비 모드가 적용되나요?

**A.** **예.** **UXD-50 (`511c240`, US-T01~T03)** — 배차 3화면(`/transport`·`/transport/runs/new`·`/transport/runs/:runId`)의 지도·정차 UI에 **Q115**와 동일한 **`forced-colors: active`** 규칙이 확장되었습니다.

| CSS 클래스 | 고대비 모드 동작 |
|-----------|----------------|
| `.ds-transport-map__canvas` | 지도 영역 **1px `CanvasText` 경계선** — 배경 틴트 없이 영역 식별 |
| `.ds-transport-stop` | 정차 카드 **경계선** 유지 |
| `.ds-transport-map-marker` | 지도 마커 **경계선** 유지 |
| `.ds-transport-map-marker--active` · `.ds-transport-stop__order` | **`Highlight`/`HighlightText`** 강제 — 활성 마커·순번 Badge 식별 |
| `.ds-transport-stop--highlighted` | `box-shadow` 대신 **`outline: 3px solid Highlight`** — 강조 정차가 고대비에서도 보임 |

| 항목 | 내용 |
|------|------|
| 표준 | WCAG 2.1 AA **1.4.11 Non-text Contrast** — 색상만으로 정차 순서·활성 마커를 구분하지 않음 |
| geocode Badge | 정상·오류 상태는 **텍스트 Badge** 병행(UXD-48) — 고대비와 무관하게 스크린리더·시각 모두 식별 |
| 테스트 | CSS 전용 변경 — Vitest **60/189** 회귀 없음 |
| 백엔드 | **`f8d1b02`** — **`TransportPilotServiceFlowE2eTest`**·**`RoleBasedControllerAccessTest$TransportAccess`** 로 US-T01~T03 service·RBAC 검증 · **`mvn test` 240/240** |

**확인 방법** — Windows **설정 → 접근성 → 대비 테마 → 고대비 켜기** 후 `/transport/runs/:runId`에서 정차 목록·지도 마커·순번 Badge가 **경계선·강조 outline**으로 표시되는지 확인하세요.

> 관련: Q115 · Q159 · USER_MANUAL §3-2·§5-8 · ADMIN_GUIDE §10-10

### Q169. 배차 화면에서 픽업 주소가 `***`로 보여요.

**A.** **BE PII 최소 노출** — **`hq_admin`이 아닌 역할**(`branch_admin`·`social_worker`·`caregiver`)이 **`GET /api/v1/transport/roster`** 또는 **`GET /api/v1/transport/runs/{runId}`** 로 조회할 때, 응답 **`pickupAddress`·`pickupContact`** 가 **마스킹**됩니다.

| 커밋 | 필드 | 규칙 |
|------|------|------|
| **`e7d4cf6`** | `pickupAddress` | 시·구 + ` ***` (예: `서울시 중구 ***`) |
| **`c7941e9`** | `pickupContact` | `010-****-5678` 형식 |

| 역할 | `pickupAddress` | `pickupContact` |
|------|-----------------|-----------------|
| **`hq_admin`** | **평문 전체** | **평문 전체** + UI **`tel:` 링크** (Q171) |
| **`branch_admin`·`social_worker`·`caregiver`** | **시·구 + ` ***`** (예: `서울시 중구 ***`) | **`010-****-5678`** 형식 |

| 규칙 | 내용 |
|------|------|
| 마스킹 대상 | roster 목록 · **확정(`CONFIRMED`) 루트 상세** 조회 |
| 마스킹 제외 | `hq_admin`의 DRAFT 생성·수정·confirm·unconfirm **응답** — 편집 흐름에서 평문 유지 |
| 이용자 API | `GET /clients/{id}` — **`pickupAddressMasked`·`pickupContactMasked`** (Q166) |
| 테스트 | **`TransportServiceTest.listRosterShouldMaskPickupAddressForNonHqRole`**(주소·연락처) · **`TransportPilotServiceFlowE2eTest`** caregiver 연락처 마스킹(`c7941e9`) · **`mvn test` 241/241** |

**현장 안내** — 요양보호사·사회복지사는 **이름·픽업 시각·지도 마커·geocode Badge**로 운행을 확인하고, **상세 주소·전화번호**가 필요하면 **`hq_admin`** 에게 요청하거나 이용자 **수정 화면**(Q166)에서 확인하세요 (USER_MANUAL §5-8).

> 관련: Q166 · Q171 · Q159 · ADMIN_GUIDE §10-10 · DATA_RETENTION_POLICY PII

### Q170. 설정·수가표·청구 화면 UI가 갑자기 정식 컴포넌트로 바뀌었어요.

**A.** **UXD-51 (`2a0ef3d`, FE-13·FE-14 복원)** — DESIGN_SYSTEM에만 정의되어 있던 **Must UI 11종**이 코드베이스 소실 후 **재구현·페이지 연동**되었습니다.

| 컴포넌트 | 연동 페이지 | 용도 |
|----------|------------|------|
| `AuditLogPanel` | `/settings` 감사 탭 | 감사 로그 표·필터 UI |
| `BackupSettingsPanel` | `/settings` 백업 탭 | 백업 스케줄·수동 실행 UI |
| `LoginHistoryPanel` | `/settings` 로그인 이력 탭 | 역할·기간 필터·마스킹 표 |
| `PasswordChangeModal` | `/settings` 보안 탭 | 비밀번호 변경 |
| `PasswordResetRequestModal` | `/`·`/settings` | 재설정 메일 요청 |
| `PlatformOrgDetailModal` | `/platform` | Tenant 상세·관리자 발급 |
| `FeeScheduleTable`·`FeeRateHistoryPanel` | `/billing/fee-schedules` | 수가표 편집·이력 |
| `CopayRateTable` | `/billing/copay-rates` | 본인부담 비율 표 |
| `BillingStatusConfirmModal` | `/billing`·`/billing/claims/:id` | 청구 확정 확인 |
| `GuardianDailySummary` | `/guardian` | 보호자 일일 기록 요약 — 출석·건강·**식사**(UXD-62, Q188) |

| 개선 | 내용 |
|------|------|
| 접근성 | `window.confirm` → **`Modal`** · raw 상태코드 → **`StatusBadge`** |
| API | **저장·조회 API 갭은 잔존** — 수가표(Q91)·설정 경로(Q125·Q126)·비밀번호 change(Q122) 등 Swagger 우회 |
| 테스트 | 컴포넌트 Vitest 추가 · Vitest **65/199** |

> 관련: Q91 · Q117 · Q125 · Q126 · Q128 · USER_MANUAL §5-4·§5-5 · ADMIN_GUIDE §10-6

### Q171. 배차 명단에서 연락처가 마스킹되거나 전화 링크가 없어요.

**A.** **UXD-52 (`37be0a3`, US-T03)** — 배차 화면 연락처는 **`TransportPickupContact`** 컴포넌트가 **역할별**로 다르게 표시합니다. 백엔드 non-HQ 마스킹(Q169)과 일치합니다.

| 역할 | UI 동작 |
|------|---------|
| **`hq_admin`** | API **평문** `pickupContact` → **`tel:` 클릭·통화 링크** · `aria-label` 「전화 걸기 …」 |
| **`branch_admin`·`social_worker`·`caregiver`** | API **마스킹값**(`010-****-5678`)만 표시 · **`tel:` 링크 없음** (`MaskedPhone withLink={false}`) |

| 화면 | 적용 |
|------|------|
| `/transport` | 당일 명단 테이블 — `showFullContact={isHqAdmin}` |
| `/transport/runs/:runId` | 정차 목록(`TransportStopList`) — 동일 |

| 항목 | 내용 |
|------|------|
| 데이터 | `GET /transport/roster` · `GET /transport/runs/{id}` — non-HQ는 `pickupContact`가 이미 마스킹 |
| 접근성 | 마스킹 번호도 **텍스트로 읽힘** — 색상만으로 구분하지 않음 |
| 테스트 | **`TransportPickupContact.test`** · **`TransportPage.test`** · **`TransportStopList.test`** · **`pilotPageFlows` T03 E2E**(Q172) · Vitest **69/211** |

**현장 안내** — 운행 중 전화가 필요한 직원은 **`hq_admin`** 계정으로 조회하거나, 센터장에게 연락처 확인을 요청하세요.

> 관련: Q169 · Q166 · Q172 · USER_MANUAL §5-8 · ADMIN_GUIDE §10-10

### Q172. `pilotPageFlows`에서 배차 연락처 마스킹이 검증되나요?

**A.** **FE `1d910c2` (US-T03)** — **`pilotPageFlows.test.jsx`** 가 **caregiver** 역할 read-only 배차 흐름에서 백엔드 마스킹 응답을 fetch-mock으로 재현하고, UI가 **`010-****-5678`** 표시·**`tel:` 링크 미노출**을 검증합니다.

| 검증 | 내용 |
|------|------|
| 역할 | `caregiver` — `CONFIRMED` 루트 상세 조회만 |
| mock | roster·run detail `pickupContact` = `010-****-5678` |
| UI | **`TransportPickupContact`** — 마스킹 텍스트 표시 · `queryByRole('link')` **null** |
| 대응 | **`hq_admin`** mock에서는 평문 + `tel:` 링크 존재 (Q171) |

| 관련 테스트 | Vitest **70파일/217건** — `pilotPageFlows` + `transportLiveApi` US-T01~T03 |

> 관련: Q169 · Q171 · Q168 · USER_MANUAL §5-8 · DEPLOYMENT §3-7

### Q173. 출석·QR·배차 화면 상단 「조회 지점」안내는 무엇인가요?

**A.** **FE `7cd9293` (UXD-53·UXD-54, US-B02·US-UX-04)** — **`BranchScopeNotice`** 컴포넌트가 **현재 `active_branch_id` 기준 조회 범위**를 텍스트로 표시합니다.

| 화면 | 경로 | 표시 |
|------|------|------|
| 출석 현황 | `/attendance` | **조회 지점: ○○점** + 「상단 지점 선택기로 변경할 수 있습니다.」 |
| 출석 통계 | `/attendance/stats` | 동일 |
| QR 생성 | `/attendance/qr/generate` | 동일 — **다른 지점 QR 오발급 방지** |
| 배차 | `/transport`·`/transport/runs/new`·`/transport/runs/:id` | 동일 |

| 항목 | 내용 |
|------|------|
| 접근성 | `role="status"` · 지점명 없으면 **렌더 생략** |
| 다지점 `hq_admin` | **BranchSwitcher**로 지점 전환 → **조회 지점** 라벨 갱신 → 목록 재조회 |
| Vitest | **`BranchScopeNotice.test.jsx`** · **`pilotPageFlows`** US-E01/E05 E2E (`e641f62`) |

> 관련: Q89 · Q11 · USER_MANUAL §3-2·§4-4·§5-7·§5-8

### Q174. 입금·미납 API가 구현되었는데 화면에서 404가 납니다.

**A.** **Partial Fixed (FE `dd72ff8`, US-L01·US-L02·G2)** — **수납 저장·미납 조회·보호자 발송** 경로가 백엔드와 **정합**되었습니다. **전용 수납 목록 API**는 여전히 **미구현**이나 **`PaymentPage`** 에서 claims 기반 목록·**이용자명**·페이지네이션이 동작합니다 (Q198).

| 기능 | 백엔드 | 프론트 (`dd72ff8`) | 상태 |
|------|--------|-------------------|------|
| 수납 저장 | `POST /billing/claims/{id}/payments` `{ paidAt, paymentMethod, amount? }` | `recordBillingClaimPaymentApi` — 동일 경로·`paymentMethod` | **Fixed** |
| 수납 목록 | **미구현** (`GET /billing/payments`) | `fetchBillingPaymentsApi` — `GET /billing/claims` **클라이언트 필터**·월·검색·페이지네이션 | **우회** (Q198 UI Fixed) |
| 미납 목록 | `GET /billing/overdue?branchId=&page=&size=&q=` | `fetchBillingOverduesApi` — `/billing/overdue` + **`Pagination`** (Q197) | **Fixed** |
| 보호자 명세 발송 | **`POST /billing/claims/{id}/notify`** (Q196) | `notifyBillingClaimGuardiansApi` — **`BillingDetailPage`·`OverduePage`** | **Fixed** |

| BE 규칙 | 내용 |
|---------|------|
| 수납 대상 | **`CONFIRMED` 청구만** — `DRAFT` 거부 |
| 수단 | `CASH` · `BANK_TRANSFER` (V50 CHECK) |
| **금액 검증** | **`amount` ≤ 0 거부** · **본인부담금과 불일치 거부** · 생략 시 전액 (Q218, `4109680`) |
| **FE 과납 차단** | **`PaymentRecordModal`** — 미납 본인부담금 **초과 입력 불가** (Q218, `dd72ff8`) |
| PAID 전환 | `paid_at`·`payment_method`·`payment_recorded_by` 저장 + J03 **`BILLING_PAYMENT_RECEIVED`** |
| 미납 정의 | **`CONFIRMED`** + **`yearMonth` < 당월** |

**UI 절차** — USER_MANUAL §4-6. 수납 목록이 비면 **청구 목록 기반 우회**이므로 Swagger **`GET /billing/claims?status=CONFIRMED`** 로 claimId를 확인할 수 있습니다.

> 관련: Q107 · Q134 · Q196 · USER_MANUAL §4-6 · ADMIN_GUIDE §10-6

### Q175. 보호자 포털에서 본인부담금 명세서를 인쇄할 수 있나요?

**A.** **예 (FE `c7c8f07`, UXD-55, US-J02)** — **`GuardianBillingDetailModal`**이 **인쇄 전용 레이아웃**을 제공합니다.

| 항목 | 내용 |
|------|------|
| 진입 | `/guardian` → **「상세」** → Modal **「인쇄」** |
| 동작 | `window.print()` — 모달 열림 동안 `body`에 `ds-statement-printing` 클래스 → `@media print`에서 **명세서 영역만** 출력 |
| 접근성 | 표 `caption`(sr-only)·`scope=row` · 본인부담금 행은 **색 + sr-only 텍스트** 병행 (색만 의존 금지) |
| 제한 | **열람·인쇄만** — CMS·간편결제·알림톡 발송은 v1.1 범위 밖 |
| API | `GET /api/v1/guardian/clients/{clientId}/billing` — **`page`·`size` 페이지네이션** + **「더 보기」** (Q192, `75fc91e`) |
| Vitest | `GuardianBillingDetailModal.test.jsx` · `GuardianPortalPage.test.jsx` |

> 센터 직원용 **PDF 명세서**는 `GET /billing/claims/{claimId}/statement` (Swagger)를 사용하세요. 보호자는 **연결 이용자** 명세만 열람할 수 있습니다 (Q108).

> 관련: Q132 · Q108 · USER_MANUAL §8-2·§8-3

### Q176. 이용자 상세 「등급 이력」 탭이 비어 있어요.

**A.** **FE `6d0a03a`·`e026ae9` + BE `15e41e3`·`0325d95` (G14 Fixed, US-M01 / G37 US-M01-g)** — **`GradeHistoryTimeline`** 이 **`GET /api/v1/clients/{clientId}/ltc-grade-history`** 를 호출합니다.

| 항목 | 내용 |
|------|------|
| 진입 | `/clients/:id` → **「등급 이력」** 탭 |
| API | `page`·`size` 페이지네이션 · `items[]`: `previousGrade`, `newGrade`, `changedAt`, `reason`, `changedBy`, **`attachmentCount`** |
| **인정기간 첨부 (G37, Q274)** | 각 이력 행 **「인정기간 첨부 (N)」** — PDF/PNG 업로드·미리보기·삭제 · **`branch_admin`·`social_worker`만 업로드** |
| 자동 이력 | 이용자 등록 시 최초 등급 · `PATCH` 등급 변경 시 **V48 트리거** append |
| 권한 | `hq_admin`, `branch_admin`, `social_worker`, `caregiver` (지점 스코프) |
| Vitest | `GradeHistoryTimeline.test.jsx` · **`GradeHistoryAttachmentPanel.test.jsx`** · `ClientDetailPage.test.jsx` · `pilotPageFlows` |

> 관련: Q102 · Q274 · USER_MANUAL §3-3 · API_SPEC §4-2 G37

### Q177. 대시보드 위젯 숫자가 API와 다르게 보여요.

**A.** **FE `6d0a03a` (US-M02 Fixed)** — **`dashboardSummary.js`** 가 nested 응답을 위젯 필드에 매핑합니다.

| API 필드 | UI 위젯 |
|----------|---------|
| `todayAttendance.checkedIn` | 입소 |
| `todayAttendance.absent` | 결석 |
| `todayAttendance.notYetArrived` | 미처리 |
| `monthlyAttendanceRates[]` | `AttendanceRateChart` |
| HQ `branches[].todayAttendance` | `BranchCompareChart`·통합 위젯 |
| `GET /dashboard/hq/alerts` | HQ `HealthAlertList` |
| `nhisUnmatchedCount`·`pendingReviewCount` | NHIS 미매칭·대기(보류) 위젯 (BE `f755428`, Q183) |
| `overdueCount` | **미납 본인부담** 위젯 — `branch_admin`·`hq_admin` only (Q202) |

> 관련: Q85 · Q118 · Q202 · USER_MANUAL §4-2·§5-2

### Q178. `hq_admin`은 설정을 어디서 바꾸나요? `/settings`와 `/organization/settings` 차이는?

**A.** **FE `f749311` (Q178 Fixed)** — 역할별 **설정 화면 분리**입니다.

| 역할 | 경로 | 내용 |
|------|------|------|
| `sysadmin` | `/settings` | 백업·감사·로그인 이력·비밀번호 (`SettingsPage` 5탭) |
| `hq_admin` | **`/organization/settings`** | **`OrganizationSettingsPage`** — `allowClientSelfCheckin` **저장 연동 Fixed**(Q116) |

`hq_admin`이 `/settings` 접근 시 **`/forbidden`**. 조직 정책 API: `GET /organization` · `PATCH /organization/settings`.

> 관련: Q87 · Q116 · USER_MANUAL §5-5 · ADMIN_GUIDE §6-3

### Q179. 청구대장·입금대장·수납대장·환불대장·간편계산기는 어떻게 쓰나요?

**A.** **Fixed (BE `de49b21`·FE `212e010`, US-M03, UXD-56)** — SideNav **청구** 그룹에 **5개 대장**·간편계산기 메뉴가 있습니다. **월별 청구 생성·가드·생성 기준**은 **`/billing`**·**`/organization/settings`** 에서 **Fixed**(Q224·Q225). **환불 처리**는 청구 상세에서 **Fixed**(Q261).

| 화면 | 경로 | 컴포넌트 |
|------|------|----------|
| **월별 청구 생성** | `/billing` | **`ClaimGenerationPanel`** + **`ClaimGenerationGuardBanner`** (Q225) |
| **청구 생성 기준** | `/organization/settings` | **`BillingSettingsPanel`** (Q224) |
| 청구대장 | `/billing/reports/charges` | **`BillingReportPage`** + **`BillingLedgerTable`** |
| 입금대장 | `/billing/reports/deposits` | 동일 |
| 수납대장 | `/billing/reports/receipts` | 동일 |
| **환불대장** | `/billing/reports/refunds` | 동일 — **`refundAmount`·`refundReason`·`refundedAt`** 열 |
| 간편계산기 | `/billing/calculator` | `CopayCalculatorPage` + `CopayCalculatorPanel` |

| 기능 | API | 상태 |
|------|-----|------|
| 청구 생성·가드 | `POST /billing/claims/generate` · `GET /billing/claims/generation-guard` | **Fixed** (Q225) |
| 생성 기준 | `GET/PATCH /settings/billing` | **Fixed** (Q224, V63) |
| **청구대장** | `GET /billing/reports/charges?month=YYYY-MM&q=&page=` | **Fixed** — `CONFIRMED`/`PAID`/`REFUNDED` 청구 라인·요약 |
| **입금대장** | `GET /billing/reports/deposits?month=` | **Fixed** — `PAID` 청구·`paidAt` 월 필터 |
| **수납대장** | `GET /billing/reports/receipts?month=` | **Fixed** — 입금대장 + **`receiptNo`** |
| **환불대장** | `GET /billing/reports/refunds?month=` | **Fixed** — `REFUNDED` 청구·환불일(`refundedAt`) 월 필터 |
| **환불 처리** | `POST /billing/claims/{claimId}/refunds` | **Fixed** — `PAID`→`REFUNDED` (Q261) |
| 간편계산기 | `GET /billing/fee-schedules` · `GET /billing/copay-rates` | **연동됨** — 클라이언트 계산 |

| 조작 | |
|------|--|
| 1 | **대상 월**(`MonthInput`) 선택 → **조회** |
| 2 | (선택) **이용자 검색** — 이름·인정번호(`q`) |
| 3 | 상단 **StatCard** 요약·표 **`BillingLedgerTable`** 확인 |
| 4 | **인쇄** — `ds-billing-report-print-zone` (`window.print()`) |

| 테스트 | **`BillingServiceTest`** listBillingReport·recordCopayRefund · **`BillingReportPage.test`** refunds variant · **`RefundRecordModal.test`** · **`pilotPageFlows`** refunds ledger E2E |

> 관련: Q224 · Q225 · Q261 · USER_MANUAL §5-10 · ADMIN_GUIDE §10-4 · REQUIREMENTS US-M03

### Q180. 방문요양 일정은 어디서 등록하나요? 주야간 지점에서 안 됩니다.

**A.** **FE `16402b2` lineage (Epic V, US-V01~V03) + BE `d768820`·`1812165` (G21, V53) Fixed** — SideNav **기록 → 방문 일정**(`/visits`)에서 **달력·일정 등록·확정·체크인/아웃**을 수행합니다.

| 항목 | 내용 |
|------|------|
| 화면 | **`VisitsPage`** — **`VisitCalendar`**(a11y 월간 달력)·**`VisitScheduleForm`** · PLAN/BILLING 탭 |
| 지점 제한 | **`HOME_VISIT`(방문요양) 지점만** — `DAY_CARE`·`INTEGRATED_HOME` 지점에서 API·화면 모두 「방문요양 일정은 방문요양 지점에서만 등록할 수 있습니다.」(BE `e304fd3`) · **`HOME_CARE` 레거시 별칭**은 **`HOME_VISIT`으로 정규화**되어 동일 허용 (`894e246`, Q248) |
| 역할 | **등록·확정·취소**: `branch_admin`, `social_worker` · **체크인/아웃**: `social_worker`, `caregiver` |
| 이중 일정 | `scheduleKind`: `PLAN`(계획) \| `BILLING`(청구) · **소문자·공백 trim 후 대문자 정규화** (Q275, `e8de0eb`) · 페어 일정은 행에 **(페어)** 표시 |
| 상태 | `DRAFT` → **확정** → **체크인** → **체크아웃** → `COMPLETED` · **취소** 가능 |
| API | `GET /visits?from=&to=&scheduleKind=` · `POST /visits` · `POST …/confirm` · `…/check-in` · `…/check-out` · `…/cancel` · **`POST /visits/imports/nhis`** (Q189) |
| DB | **V53** `visit_schedules` · **V51** `branches.service_type` |
| 테스트 | **`VisitsPage.test`** · **`VisitCalendar.test`** · **`VisitServiceTest`** · **`mvn test` 288/288** · Vitest **81/267** |

> 관련: USER_MANUAL §5-11 · REQUIREMENTS G21 · ERD V53

### Q181. NHIS import 후 「대기」·「보류」 행은 어떻게 처리하나요?

**A.** **BE `dd49204` lineage (G7, V54)** — 공단 엑셀 **「처리상태」** 열이 `대기`·`보류`·`pending`·`검토중` 등이면 행 상태가 **`PENDING_REVIEW`**(화면 Badge **「대기」**)로 저장됩니다. **FE `16402b2` (UXD-58)** 에서 대사 화면 안내·요약 UI가 보강되었습니다.

| 항목 | 내용 |
|------|------|
| 의미 | 공단 측 청구 **심사·처리가 아직 끝나지 않음** — ogada 내부 대사(MATCHED/DISCREPANCY) 전 단계 |
| 안내 문구 | `match_status_reason`: 「공단 처리가 대기(보류) 중입니다. 해당 월 청구 전송·심사 완료 후 다시 import 하세요.」 |
| 화면 | **`NhisReconciliationTable`** — `PENDING_REVIEW` 행 **info 강조** · **「보류 사유」**열에 `matchStatusReason` · 수동 연결·비교 버튼 **없음** |
| 요약·가이드 (UXD-58) | **`ReconciliationPage`** 상단 **StatCard**(일치·차이·미매칭·**대기(보류)**) · **`NhisPendingReviewGuide`** — 대기 행 1건 이상 시 3단계 조치 안내 (FAQ **Q182**) |
| 조치 | 해당 월 **공단 심사 완료 후** 롱텀에서 엑셀을 **다시 다운로드·import** — 그 전까지는 출석·청구 내부 검증만 수행 |
| DB | **V54** — `match_status` CHECK 확장 · `match_status_reason` NOT NULL · `idx_nhis_import_rows_org_pending_review` |
| 테스트 | **`NhisReconciliationMatcherTest`** · **`NhisImportServiceTest.importShouldMarkPendingReviewRowsFromProcessingStatus`** · **`NhisPendingReviewGuide.test`** · **`ReconciliationPage.test`** · **`pilotPageFlows`** G7 E2E |

> 관련: Q31 · Q182 · USER_MANUAL §4-6-1 · DATA_RETENTION_POLICY §4-2 · ADMIN_GUIDE §10-5

### Q182. NHIS reconciliation 화면에서 「대기(보류)」 요약과 안내는 어디에 표시되나요?

**A.** **FE `16402b2` (UXD-58, US-G06)** — 대사 상세(`/billing/imports/nhis/:batchId`) 상단에 **매칭 상태 요약 StatCard**와 **`NhisPendingReviewGuide`**가 표시됩니다.

| UI | 내용 |
|----|------|
| StatCard 4종 | **일치**·**차이**·**미매칭**·**대기(보류)** 건수 — `role="group"` · `aria-label="매칭 상태 요약"` |
| `NhisPendingReviewGuide` | 대기 행 **1건 이상**일 때만 표시 — ① 롱텀 포털 심사 확인 → ② 처리상태 확정 엑셀 재다운 → ③ ogada 재import 후 일치·차이·미매칭만 보정 |
| 보류 사유 열 | **`NhisReconciliationTable`** — `PENDING_REVIEW` 행에 **`matchStatusReason`** 텍스트(예: 「공단 처리가 대기(보류) 중입니다…」) |
| 접근성 | info 톤 **Alert** · `role="status"` 각주 — 색상만으로 의미 전달하지 않음 (USER_MANUAL §3-2) |
| 배치 API | `GET …/imports/nhis/{batchId}` 응답 **`pendingReviewCount`** 가 있으면 StatCard에 우선 사용 |

> 관련: Q181 · Q183 · USER_MANUAL §4-6-1 · ADMIN_GUIDE §10-5

### Q183. 대시보드에 「NHIS 대기(보류)」 위젯이 표시됩니다. 무엇인가요?

**A.** **FE `1794e1c` (BNK-19, US-M02-b) + BE `f755428` (US-M02)** — 지점·통합 대시보드 **6번째 운영 위젯**. ReconciliationPage **「대기(보류)」** StatCard와 동일한 집계입니다.

| 항목 | 내용 |
|------|------|
| 위젯 | **`DashboardWidgetGrid`** — 라벨 **「NHIS 대기(보류)」** · `nhisPendingReviewCount` 건수 · 1건 이상이면 **`tone=warning`** |
| 집계 (FE) | `fetchNhisImportBatchesApi()` → **`sumNhisPendingReviewFromBatches`** — 배치별 `pendingReviewCount` 합산 |
| 집계 (BE) | **`GET /dashboard/branch`** 응답 **`pendingReviewCount`** — NHIS 행 `PENDING_REVIEW` 건수 (Q202) |
| 링크 | 클릭 시 **`/billing/imports/nhis`** — 대사 상세에서 **`NhisPendingReviewGuide`** 로 조치 (Q181·Q182) |

> 관련: Q181 · Q182 · Q202 · USER_MANUAL §4-2 · §5-2

### Q184. 지점 등록 시 「행정구역」은 어떻게 선택하나요?

**A.** **FE `1794e1c` (BNK-19)** — **`BranchesPage`** 등록·수정 모달에 **`RegionSelector`** 3단 연계 선택이 추가되었습니다 (V51).

| 단계 | API | UI |
|------|-----|-----|
| 1 | `GET /api/v1/regions/sidos` | **시·도** Select |
| 2 | `GET /api/v1/regions/sigungus?sidoCode=` | **시·군·구** Select — 상위 미선택 시 disabled |
| 3 | `GET /api/v1/regions/dongs?sigunguCode=` | **읍·면·동** Select — 최종 `regionDongCode` 저장 |

| 항목 | 내용 |
|------|------|
| 급여종 | **`serviceType`** — `DAY_CARE`·`HOME_VISIT`·`HOME_CARE`(→`HOME_VISIT` 정규화, Q248)·`INTEGRATED_HOME` (Q180 방문요양 연계) |
| 접근성 | 각 Select에 **`Field`** 라벨·하위 단계 disabled·로딩 **`Spinner`** |
| 오류 | 지역 API 실패 시 「지역 목록을 불러오지 못했습니다」 — Swagger로 `regionDongCode` 직접 입력 우회 |

> 관련: Q180 · USER_MANUAL §5-3 · ADMIN_GUIDE §6-4

### Q185. 보호자 상세에서 「연결 이용자」와 대표 보호자는 어떻게 관리하나요?

**A.** **FE `6db762a` (UXD-59, US-K02)** — **`GuardianDetailPage`** 에 **`GuardianClientLinks`** 패널이 추가되었습니다.

| 기능 | UI | 권한 |
|------|-----|------|
| 연결 이용자 목록 | 이용자명 링크(`/clients/:id`) · **대표** Badge | 조회: 스코프 내 전 역할 |
| 대표 보호자 지정 | 행별 **`Switch`** — 1명만 primary | **`branch_admin`·`social_worker`·`hq_admin`** (`canEdit`) |
| 빈 상태 | 「연결 이용자 없음」 — 이용자 상세 초대·수락 안내 | — |

| 항목 | 내용 |
|------|------|
| 데이터 | `GET /guardians/{id}` 응답 `linkedClients[]` — `clientId`·`clientName`·`isPrimary` |
| API 갭 | 대표 지정 **`onSetPrimary`** — 백엔드 전용 PATCH 경로·FE DTO 정합 **후속** 가능. 실패 시 Swagger |
| 목록 | **`GuardiansPage`** — 보호자 검색·초대·상세 링크 보강 (US-K01) |

> 관련: USER_MANUAL §4-3 · §8-2

### Q186. 미납 관리 화면 상단 요약 바는 무엇인가요?

**A.** **FE `6db762a` (UXD-59, US-L02)** — **`OverduePage`**(`/billing/overdue`) 상단에 **`OverdueSummaryBar`** 가 표시됩니다.

| 항목 | 내용 |
|------|------|
| 표시 | **미납 건수**·**미납 총액** 요약 — `role="status"` |
| 목록 | `GET /billing/overdue` 응답 `items[]` — 이용자명·청구월·본인부담금·경과일 |
| FE 경로 갭 | 일부 빌드에서 **`/billing/overdues`**(복수) raw `fetch` — 정식 경로는 **`/billing/overdue`** (Q174) |
| 안내 발송 | **「안내 발송」** 버튼 — **`POST …/notify` Fixed** (Q196) — 연결 보호자에게 명세 알림 |

> 관련: Q174 · USER_MANUAL §4-6 · §5-7

### Q187. 「알림 이력」 화면은 어디서 보나요? 무엇이 표시되나요?

**A.** **FE `e39164d` (BNK-22, US-J03-h, UXD-61)** — **`NotificationHistoryPanel`** 이 보호자 포털·이용자 상세에 연동되었습니다. 케어포 **10-7 안내발송내역**과 동일하게 **발송 결과만** 조회하며, **수신 휴대폰·이메일은 표시하지 않습니다**.

| 진입 경로 | 역할 | UI |
|----------|------|-----|
| `/guardian` → **「알림 이력」** 탭 | `guardian` | 포털 하단 **Tabs** — `fetchGuardianNotificationHistoryApi` |
| `/clients/:id` → 기본정보 탭 | `branch_admin`·`social_worker` | **「보호자 알림 이력 (US-J03)」** `Card` — `fetchClientNotificationHistoryApi(clientId)` |

| 표 열 | 내용 |
|------|------|
| 발송 시각 | `sentAt` 또는 `createdAt` — `ko-KR` 로케일 |
| 채널 | `StatusBadge` + `NOTIFICATION_CHANNEL` — KAKAO·SMS 등 |
| 유형 | `notificationEventLabel(eventType)` — 출석(입소/귀가)·일일 케어·본인부담금 명세·입금 확인·긴급 알림 |
| 상태 | `NOTIFICATION_STATUS` — PENDING·SENT·FAILED |

| 항목 | 내용 |
|------|------|
| 접근성 | 표 `caption`·`captionVisuallyHidden` · 안내 `role="note"` · 로딩 **`Spinner`** |
| 빈 상태 | 「알림 이력 없음」 — stub provider·알림톡 미연동 시 **정상** (Q147) |
| 실발송 | Solapi live 연동·케어포 **10-1 문자메시지 발송**은 **v1.1/v2 잔여** — UI는 이력 조회만 제공 |

> 관련: Q152 · Q147 · USER_MANUAL §4-7-2 · §8-2 · ADMIN_GUIDE §10-9

### Q188. 보호자 포털 「일일 기록」에 식사가 보이나요?

**A.** **FE `ac5638e` (UXD-62, US-I02·FLOWCHART §9)** — **`GuardianDailySummary`** **「식사」** 행이 추가되었습니다.

| 표시 | 내용 |
|------|------|
| 식사 구분 | `mealType` — 아침(`BREAKFAST`)·점심(`LUNCH`)·간식(`SNACK`) — `config/meals.js` **`MEAL_TYPES`** |
| 섭취량 | `intakeLevel` — **`StatusBadge`** (`MEAL_INTAKE_BADGE`) — 잘 먹음·보통·적게 (색상+텍스트 병행) |
| 빈 상태 | `meals[]` 없거나 API 미반환 시 **「—」** |

| 항목 | 현재 |
|------|------|
| 센터 입력 | **`/meals`** — `POST /meals/records` 로 당일 섭취 기록 저장 (Q161) |
| API 갭 | **`GET /guardian/daily-records`**(BE `dd49204`) 응답에 **`meals[]` 미포함** — UI만 준비, 실데이터 연동 **후속** |
| 우회 | 보호자에게 식사 내용을 전달하려면 당분간 **직원이 직접 안내**하거나 Swagger로 `GET /meals/records?clientId=&date=` 조회 |

> 관련: Q189 · USER_MANUAL §5-11 · REQUIREMENTS G21 · ERD V53

### Q189. 공단 방문요양 급여계획·청구일정 엑셀을 일괄 import 할 수 있나요?

**A.** **BE `ee3fa3a` + FE `60cea98` (UXD-63, US-V04, G21)** — **`POST /api/v1/visits/imports/nhis`** API와 **`/visits`** 화면 **「공단 방문일정 엑셀 import」** 패널이 모두 제공됩니다.

| 파라미터 | 설명 |
|----------|------|
| `branchId` | **필수** — `HOME_VISIT` 급여종 지점 UUID |
| `scheduleKind` | `PLAN`(기본) \| `BILLING` |
| `createPairedBillingSchedule` | `true` — PLAN import 시 **페어 BILLING 일정** 자동 생성 |
| `file` | xlsx — 헤더: 장기요양인정번호·방문일·시작/종료시간·제공시간(분) 등 |

| 행 `importStatus` | 의미 |
|-------------------|------|
| `IMPORTED` | `DRAFT` 방문 일정 생성 성공 |
| `UNMATCHED` | 인정번호로 이용자 미매칭 |
| `SKIPPED` | 퇴소·비활성·시간 검증 실패·**제공시간 1–480분 범위 밖**(Q193) |

| UI (`VisitNhisImportPanel`) | 설명 |
|-------------------------------|------|
| 진입 | SideNav **기록 → 방문 일정**(`/visits`) — `branch_admin`·`social_worker` |
| 일정 종류 | `Select` — 계획/청구 |
| 페어 토글 | PLAN 선택 시 **「청구 일정도 함께 생성」** `Switch` |
| 결과 | 업로드 후 **등록·미매칭·건너뜀** 건수 Alert + 행별 **`StatusBadge`** 표 |

| 항목 | 내용 |
|------|------|
| 권한 | `branch_admin`, `social_worker` |
| 지점 | **`HOME_VISIT` only** — 주야간·통합재가 지점 **422** (Q180) |
| 파서 | 「처리상태」에 **「오류」** 포함 행은 **파서에서 제외** |
| 테스트 | **`NhisVisitScheduleExcelParserTest`** · **`VisitServiceTest.importNhis*`** · **`VisitNhisImportPanel.test`** |

> 관련: Q180 · Q193 · USER_MANUAL §5-11 · ADMIN_GUIDE §10-12

### Q190. 폼 저장 실패 시 필드 아래에 오류가 표시되나요?

**A.** **BE `8068148` + FE `3803247` (SEC-D17)** — 검증 실패(`400 VALIDATION_ERROR`) 시 API가 **`error.fieldErrors`** `{ "필드명": "한국어 메시지" }` 를 반환하고, 프론트 **`applyApiErrorToForm`** 이 **`Field` `error` prop**으로 매핑합니다.

| 화면 | 적용 |
|------|------|
| **`LoginPage`** | `email`·`password` 필드 + 상단 Alert |
| **`StaffPage`** | 직원 등록 모달 — `displayName`·`email`·`password` 등 |
| **`BranchesPage`** | 지점 등록 모달 — `name`·`serviceType`·`regionDongCode` |
| **`PasswordChangeModal`** | `newPassword` → `newPwd` 필드 매핑 · **`POST /auth/change-password` Fixed** (Q122) |

| 항목 | 내용 |
|------|------|
| HTTP | `400` · `code: VALIDATION_ERROR` |
| FE 파서 | `http.js` **`parseApiErrorPayload`** — `error.fieldErrors` · **`errors[]` string array** message 승격(QA-B62·`9f80082`) · `formErrors.js` `fieldMap` 옵션 |
| 테스트 | **`GlobalExceptionHandlerTest`** · **`formErrors.test.js`** · **`http.test.js`** · **`settingsServices.test.js`** |

> 관련: Q122 · Q151 · USER_MANUAL §3-2

### Q191. 이용자 목록에 보호자·지역·나이 열이 보입니다.

**A.** **BE `a49e496` + FE `1794e1c` lineage** — `GET /api/v1/clients` 목록 응답·**`ClientListPage`** Table 8열이 확장되었습니다.

| 열 | API 필드 | 설명 |
|----|---------|------|
| 나이 | `ageYears` (또는 `birthDate` 폴백) | 만 나이 |
| 지역 | `regionLabel` | 지점 행정구역 라벨 (V51) |
| 보호자 | `primaryGuardianName` | 대표 보호자 표시명 |
| (검색) | — | 이름·지역·보호자명·성별 **`q`** 검색 (BNK-19) |

| 항목 | 내용 |
|------|------|
| PII | 보호자 연락처는 목록에 **`primaryGuardianPhoneMasked`** 만 — `tel:` 링크 없음 |
| 상세 | 이용자 상세·보호자 카드는 기존과 동일 (§3-3) |

> 관련: Q184 · USER_MANUAL §4-3

### Q192. 보호자 포털 본인부담금 명세 목록이 많을 때 어떻게 보나요?

**A.** **FE `75fc91e` (US-J02)** — **`GuardianPortalPage`** **「명세·청구」** 탭에서 **`GET /api/v1/guardian/clients/{clientId}/billing?page=&size=`** 페이지네이션을 사용합니다.

| 항목 | 내용 |
|------|------|
| 초기 로드 | 연결 이용자 선택 시 **첫 페이지** 명세 표 |
| 더 보기 | 목록 하단 **「더 보기」** — 다음 `page`를 이어 붙여 표시 |
| 상세 | 행 **「상세」** → **`GuardianBillingDetailModal`** (Q175) |
| 테스트 | **`GuardianPortalPage.test.jsx`** — 페이지 증가·API `page` 파라미터 검증 |

> 관련: Q175 · Q108 · USER_MANUAL §8-2

### Q193. 방문일정 import에서 「건너뜀(SKIPPED)」 행이 나옵니다.

**A.** **BE `0c069b5` (G21)** — **`VisitService.validateServiceMinutes`** 가 **제공시간(분)** 을 **1–480** 범위로 검증합니다. 범위 밖·null(필수인 경우)·퇴소·비활성 이용자 행은 **`SKIPPED`** + `reason` 으로 응답합니다.

| 원인 | `reason` 예시 |
|------|---------------|
| 제공시간 범위 | 0분·481분 이상 |
| 이용자 상태 | 퇴소·비활성 |
| 시간 형식 | 시작/종료 시각 파싱 실패 |

| 항목 | 내용 |
|------|------|
| 수기 등록 | `POST /visits` — 범위 밖이면 **`422`** |
| import | 해당 행만 **`SKIPPED`** — 배치 전체 실패 아님 |
| UI | **`VisitNhisImportPanel`** 결과 표 **「건너뜀」** Badge + 사유 열 (Q189) |
| 테스트 | **`VisitServiceTest`** — create/update/import 분 단위 검증 |

> 관련: Q189 · USER_MANUAL §5-11 · ADMIN_GUIDE §10-12

### Q194. 방문 일정을 취소하면 페어(계획↔청구) 일정은 어떻게 되나요?

**A.** **BE `b63bb1f` (US-V02, G21)** — PLAN/BILLING **이중 일정**에서 한쪽을 **취소**하면, 연결된 페어 일정도 **자동 취소**됩니다. 완료(`COMPLETED`)·이미 취소된 페어는 **변경하지 않습니다**.

| 항목 | 내용 |
|------|------|
| API | `POST /api/v1/visits/{id}/cancel` |
| 연쇄 대상 | `pairedScheduleId`로 연결된 PLAN 또는 BILLING — `DRAFT`·`CONFIRMED`·`IN_PROGRESS` |
| 스킵 | 페어가 `COMPLETED` 또는 `CANCELLED` |
| 목적 | 확정·청구 가능한 **고아(orphan) 일정** 방지 |
| UI | `/visits` 당일 목록 **「취소」** 버튼 (`branch_admin`, `social_worker`) |
| 테스트 | **`VisitServiceTest`** — cascade·completed-skip·no-paired 3건 |

> 관련: Q180 · USER_MANUAL §5-11 · ADMIN_GUIDE §10-12

### Q195. 확정된 방문 일정이 있는데 공단 import가 안 됩니다.

**A.** **BE `84f3441` + FE `bf3d40d` (BNK-26, G21)** — 이지케어 FAQ 21473과 동일하게, **확정(`CONFIRMED`) 계획 일정**이 존재하면 **청구(BILLING) NHIS import** 및 **페어 청구 동시 생성**이 **차단**됩니다.

| 항목 | 내용 |
|------|------|
| BE 규칙 | BILLING import 또는 PLAN+`createPairedBillingSchedule` 시 해당 이용자·방문일에 **확정 계획** 존재 → 행 **`SKIPPED`** |
| `reason` | `확정된 계획일정이 있어 청구일정을 반영할 수 없습니다. 확정 취소 후 다시 시도하세요.` |
| FE UI | **`VisitNhisImportPanel`** — 달력에 확정 일정 1건 이상이면 패널 **비활성** + 경고 Alert |
| 조치 | `/visits`에서 해당 일정 **「취소」**(Q194 연쇄) 또는 확정 해제 후 **재import** |

> 관련: Q189 · Q193 · **Q209** · USER_MANUAL §5-11 · ADMIN_GUIDE §10-12

### Q196. 청구 확정 후 보호자에게 본인부담금 명세를 수동 발송할 수 있나요?

**A.** **예 (BE `84f3441` + FE `c48fb67`, G2, US-J03)** — **`POST /api/v1/billing/claims/{claimId}/notify`** 로 연결 보호자에게 **명세 알림**을 수동 발송합니다.

| 항목 | 내용 |
|------|------|
| API | `POST /api/v1/billing/claims/{claimId}/notify` — 응답 `{ claimId, dispatchedCount }` — **`dispatchedCount` = 연결 이용자 수**(동일 `clientId` 중복 라인 1회, Q219, `40567a2`) |
| 권한 | `hq_admin`, `branch_admin` |
| 대상 상태 | **`CONFIRMED`·`PAID`만** — `DRAFT` 거부 |
| UI | **`BillingDetailPage`** **「보호자 발송」** · **`OverduePage`** **「안내 발송」**(→ 동일 notify API) |
| 알림 | J03 **`BILLING_STATEMENT`**(stub 환경은 `notifications` 이력만) |
| 수납 연동 | 이후 **`POST …/payments`** 수납 시 **`BILLING_PAYMENT_RECEIVED`** 별도 dispatch (Q159) |
| 테스트 | **`BillingServiceTest`** · **`BillingDetailPage.test`** · **`J03AlimtalkServiceFlowE2eTest`** |

> 관련: Q174 · Q147 · Q219 · USER_MANUAL §4-6 · ADMIN_GUIDE §10-6

### Q197. 미납 관리 목록이 많을 때 어떻게 보나요?

**A.** **Fixed (BE `4ee652d` + FE `1462396`, US-L02)** — **`GET /api/v1/billing/overdue`** 가 **서버 페이지네이션**·**이용자명 검색(`q`)** 을 지원합니다.

| 항목 | 내용 |
|------|------|
| API | `GET /api/v1/billing/overdue?page=0&size=20&q=김` — `page`는 **0-based** |
| 응답 필드 | `claimId`, `clientName`, `yearMonth`, `copayAmount`, `daysOverdue`, `guardianPhoneMasked`, `lastReminderAt` |
| UI | **`OverduePage`** — **`OverdueSummaryBar`** · **`SearchInput`** · **`Pagination`** · 보호자 **`MaskedPhone`** |
| 발송 | 행별 **「안내 발송」** → `POST /claims/{id}/notify` (Q196) |
| 수납 후 | `POST …/payments` 로 **PAID** 전환 시 미납 목록에서 **자동 제외** (`09932ef` lifecycle test) |

> 관련: Q174 · Q196 · USER_MANUAL §4-6 · ADMIN_GUIDE §10-6

### Q198. 입금 처리 화면에 이용자 이름이 안 보였어요.

**A.** **Fixed (FE `69aff5d`, US-L01)** — **`PaymentPage`** 표 **「이용자」** 열에 `clientName`이 표시됩니다.

| 항목 | 내용 |
|------|------|
| 데이터 | `fetchBillingPaymentsApi` — `GET /billing/claims` 결과에서 `CONFIRMED`/`PAID` 필터 후 `mapClaimToPaymentRow` |
| UI | **기준 월**(`MonthInput`) · **이용자 검색** · **`Pagination`** · 미수납 행 **「수납」** |
| 잔여 갭 | **`GET /billing/payments` 전용 API 미구현** — 대량 청구 시 **클라이언트 필터** 한계 (Q174) |

> 관련: Q134 · Q174 · USER_MANUAL §4-6

### Q199. 방문 일정(계획·청구 페어)을 수정하면 반대쪽도 같이 바뀌나요?

**A.** **예 — `DRAFT` 상태에서만 (BE `3e4d3e6`, G21)** — PLAN/BILLING이 `pairedScheduleId`로 연결되어 있고 **양쪽 모두 `DRAFT`** 이면, 한쪽 **수정** 시 담당·방문일·시작/종료·제공분·메모가 **페어에 미러링**됩니다.

| 항목 | 내용 |
|------|------|
| 동기화 필드 | `assignedUserId`, `visitDate`, `plannedStartTime`, `plannedEndTime`, `serviceMinutes`, `notes` |
| 미동기화 | **`CONFIRMED` 이상** 상태 — 확정 후에는 페어 **필드 수정 동기화 미적용** |
| **확정** | **Fixed (BE `aacf20b`, G21 / US-V02, Q259)** — PLAN 또는 BILLING **한쪽 확정** 시 **페어가 `DRAFT`이면 양쪽 `CONFIRMED`** — orphan billing DRAFT 방지 |
| 취소 | **양쪽 취소**는 US-V02(Q194) — 완료·이미 취소된 페어는 스킵 |

> 관련: Q194 · Q234 · Q259 · USER_MANUAL §5-11 · ADMIN_GUIDE §10-12

### Q200. 공단 방문일정 엑셀 import에서 날짜·시간이 건너뜀(SKIPPED)됩니다.

**A.** **Partial Fixed (BE `7fbd219` + V57 `469d08c`, G21)** — `NhisVisitScheduleExcelParser`가 다양한 **한국어·숫자 날짜·시간 형식**을 정규화합니다.

| 지원 예시 | 정규화 |
|----------|--------|
| `20260609`, `2026.06.09`, `2026년6월9일` | `2026-06-09` |
| `930`, `0930`, `오전 9:30`, `PM 2:00` | `09:30`, `14:00` |
| 파싱 실패 | 행 **`SKIPPED`** + `reason` — 엑셀 원본 형식 확인 |
| 성능 | **V57** `idx_visit_schedules_org_branch_client_plan_blocking` — 확정 계획 EXISTS 가드 (Q195) |

> 관련: Q189 · Q193 · Q195 · USER_MANUAL §5-11 · DEPLOYMENT §8-1

### Q201. 시스템 설정(`/settings`) 화면 탭·날짜 입력이 바뀌었나요?

**A.** **Fixed (FE `fed457f`·`8818e0a`, UXD-64)** — **`sysadmin`** 전용 **`SettingsPage`** 가 **4탭**으로 정리되었고, 날짜 필드는 **`DateInput`** 컴포넌트로 통일됩니다.

| 탭 | 내용 |
|----|------|
| **보안** (기본) | **「비밀번호 변경」** → **`PasswordChangeModal`** (`POST /auth/change-password`, Q122) |
| 로그인 이력 | **`LoginHistoryPanel`** (Q126) |
| 감사 로그 | **`AuditLogPanel`** (Q121) |
| 백업 | **`BackupSettingsPanel`** (Q121) |

**`DateInput` (UXD-64)** — `Field` 안에서 `type="date"` 입력 — 이용자 생년월일·수납일·배차 운행일 등 **너비·라벨 일관**.

> 관련: Q122 · Q121 · USER_MANUAL §5-5 · ADMIN_GUIDE §4-2

### Q202. 대시보드에 「미납 본인부담」 위젯이 보입니다. 누가 볼 수 있나요?

**A.** **Fixed (FE `a53db39` + BE `f755428`, US-M02·US-L02)** — **`branch_admin`·`hq_admin`** 역할에게만 **7번째 운영 위젯**이 표시됩니다.

| 항목 | 내용 |
|------|------|
| 위젯 | 라벨 **「미납 본인부담」** · `overdueCount` 건수 · 1건 이상이면 **`tone=danger`** |
| 의미 | 당월 **이전** **`CONFIRMED`** 상태·미수납 본인부담금 청구 건수 — `GET /billing/overdue`와 동일 규칙 (Q197) |
| 링크 | 클릭 시 **`/billing/overdue`** — 미납 목록·안내 발송 (Q196) |
| BE API | **`GET /dashboard/branch`** 응답 **`overdueCount`** — 단일 호출로 집계 가능 |
| FE | 병렬 **`fetchBillingOverduesApi({ page:1, size:1 })`** → `totalElements` 로 위젯 갱신 · API 필드 **폴백** (`dashboardSummary.js`) |
| 미표시 역할 | `social_worker`·`caregiver`·`guardian` 등 — 청구 수납 권한 없음 |

> 관련: Q174 · Q197 · Q203 · USER_MANUAL §4-2 · §4-6

### Q203. 입금 처리와 미납 관리 화면 상단 탭은 무엇인가요?

**A.** **Fixed (FE `a53db39`·`6c6dc7a`·`c9baca2`, US-L01·L02·L03)** — **`BillingContextNav`** 가 **`PaymentPage`**(`/billing/payments`)·**`OverduePage`**(`/billing/overdue`)·**`CmsPage`**(`/billing/cms`)·**`EasyPayPage`**(`/billing/easy-pay`) 상단에 표시됩니다.

| 항목 | 내용 |
|------|------|
| 구성 | **「입금 처리」** · **「미납 관리」** · **「CMS 자동이체」** · **「간편결제」** — `NavLink` 활성 탭 강조 |
| 접근성 | `nav` · `aria-label="본인부담 수납 하위 메뉴"` · 키보드 Tab 이동 |
| 용도 | 수납 입력 ↔ 미납 안내 ↔ CMS ↔ **7-5 간편결제** **화면 전환** — SideNav **청구** 그룹 진입 후에도 컨텍스트 유지 |
| 테스트 | **`BillingContextNav.test.jsx`** · **`CmsPage.test`** · **`EasyPayPage.test`** · **`pilotPageFlows`** billing E2E |

> 관련: Q174 · Q198 · Q202 · Q207 · Q326 · USER_MANUAL §4-6

### Q204. 보호자 알림 **이메일**(`channelEmail`)도 발송되나요?

**A.** **예 (BE `fbedcc3`·`f77a268`, US-J03 v2 email + G2 templates)** — preference **`channelEmail=true`** 이면 **`NotificationService`** 가 **email 채널**을 **Kakao/SMS와 독립**으로 dispatch합니다.

| 항목 | 내용 |
|------|------|
| Provider | **`StubEmailProvider`** — dev/staging 기본 · 로그에 **마스킹된 수신 이메일**·subject 기록 |
| 수신자 해석 | **`GuardianEmailResolver`** — Tenant 스코프 **`users.email`** (보호자 계정 등록·초대 수락 시 저장) |
| **엔젤 패리티 템플릿 5종** | **`BILLING_STATEMENT`**(명세) · **`CARE_PROVISION_RECORD`**(급여제공기록지) · **`HOME_NEWSLETTER`**(가정통신문) · **`ELDER_ABUSE_PREVENTION_GUIDELINE`**(학대예방 지침, `0854fbd`) · **`BILLING_PAYMENT_RECEIVED`**(납부확인서, `588b8e6` payload 보강) — **`EmailNotificationContent`** |
| **금액 표기** | **`formatWon`** — 본인부담금·수납 금액 **한국어 원화** (예: `150,000원`) |
| 기타 템플릿 | 출석·**`DAILY_CARE_SUMMARY`**·긴급 |
| consent | **카카오·SMS** — V42 **`consent_at`** 규칙 **유지** · **email은 consent 불필요** |
| 트리거 | 출석·건강·**`POST /claims/{id}/notify`**·**`POST …/payments`**(자동) · **`POST …/payment-receipt-notify`**(수동, Q221) · **§4-7-3 서류 발송** (Q216–Q217·Q222) |
| 이력 | `notifications.channel=email` · **`GET /guardian/notifications`** 에서 확인 (연락처·이메일 주소 **비표시**, Q187) |
| live SMTP | **Partial Fixed (`6ed48ff`·`f23f15a`)** — **`NOTIFICATION_EMAIL_PROVIDER=smtp`** + **`SMTP_*`** + 유효 **`NOTIFICATION_EMAIL_FROM`** 시 **`SmtpEmailProvider`** 실발송 · 기본 **`stub`** |
| 검증 | 보호자 **`users.email`** 형식 불량 → **스킵**(`Guardian email format is invalid`) · FROM/Reply-To 설정 오류 → **기동 실패** (`f23f15a`) |

> **설정**: Swagger **`PUT /clients/{id}/guardians/{guardianUserId}/notification-preferences`** — `"channelEmail": true` (Q137-1). 보호자 이메일 미등록 시 **스킵**(`Guardian email not registered`). 운영 SMTP env — DEPLOYMENT §4-8.

> 관련: Q147 · Q148 · Q196 · Q209 · Q216–Q217 · Q221–Q222 · USER_MANUAL §4-7 · §4-7-3 · ADMIN_GUIDE §10-8

### Q205. 퇴소한 이용자도 미납 목록에 이름이 보이나요?

**A.** **예 (BE `a401537`, US-L02 Fixed)** — **`GET /api/v1/billing/overdue`** 가 이용자명을 **Tenant 스코프 batch 조회**(`loadClientNamesById`)로 로드하므로, **퇴소(`discharged`) 이용자**도 **`clientName`** 이 **「—」로 빠지지 않습니다**.

| 항목 | 내용 |
|------|------|
| 증상(수정 전) | 퇴소 후 미납 청구 행에서 이용자명 누락·검색(`q`) 불일치 |
| 수정 | `BillingService.listOverdueClaims` — claim별 `clientId` 집합 → **org-scoped 1회 조회** |
| UI | **`OverduePage`** · **`DashboardPage`** 미납 위젯 — 동일 API 필드 사용 (Q202) |
| 업무 | 퇴소 전·후 **미수납 본인부담금** 추심 시 **이름으로 식별** 가능 |

> 관련: Q197 · Q202 · USER_MANUAL §4-6

### Q206. ogada에서 **CMS 자동이체**(본인부담금)를 지원하나요?

**A.** **예 (v2 P1 skeleton, BE `2c6e57e`·FE `6c6dc7a`, US-L03)** — 케어포 **7-4**에 대응하는 **효성 FCMS** 연동 골격이 구현되었습니다. **등록·출금 API·화면**은 동작하나, 기본값 **`FCMS_PROVIDER=stub`** 이므로 **실제 계좌 출금은 없습니다** (Q208).

| 항목 | 내용 |
|------|------|
| 벤더 | **효성 CMS (FCMS)** — 엔젤시스템·케어포와 동일 계열 (REQUIREMENTS G2) |
| API | `POST/GET/DELETE /api/v1/billing/cms/enrollments*` · `POST/GET /api/v1/billing/cms/claims/{claimId}/debit` |
| UI | **`/billing/cms`** — SideNav **청구 → CMS 자동이체** — **등록·출금·해지** (`9a6fdb6`, Q299) |
| 수납 연동 | CMS 출금 **성공** 시 청구 **`PAID`** · `payment_method=CMS` (V59) · J03 **`BILLING_PAYMENT_RECEIVED`** 알림 |
| 실연동 | **`FCMS_API_KEY`·`FCMS_MERCHANT_ID`** + live provider — 후속 (DEPLOYMENT §4-6) |

> 관련: Q207 · Q208 · USER_MANUAL §4-6 · ADMIN_GUIDE §10-13

### Q207. CMS 자동이체 **등록**은 어떻게 하나요?

**A.** 센터 **`hq_admin`·`branch_admin`** 이 **`/billing/cms`** → **등록 관리** 탭에서 수행합니다.

| 단계 | 내용 |
|------|------|
| 1 | **이용자** 선택 — 활성 이용자만 |
| 2 | **연결 보호자** 선택 — `guardian_clients` 연결 필수 |
| 3 | **예금주명**·**은행**(3자리 코드)·**계좌번호 끝 4자리** 입력 |
| 4 | **CMS 자동이체 등록** 클릭 — FCMS stub 등록 후 **`cms_enrollments`** `ACTIVE` |
| 5 | 보호자 **서면 자동이체 동의서** 원본은 센터가 별도 보관 (ogada는 **끝 4자리만** 저장, DATA_RETENTION §2) |

| 규칙 | 내용 |
|------|------|
| 중복 | 동일 이용자·보호자 **ACTIVE** 1건 — **다른 보호자 ACTIVE** 등록 **거부**(`72aff00`, Q299) · **`CANCELLED`** 건 재등록 시 **기존 행 UPDATE**(`8431b5c`·`fee710d`, Q207) |
| 이력 | **`GET …/enrollments?clientId=`** — **ACTIVE·CANCELLED** 전체 (`4a622ab`, Q299) |
| PII | 전체 계좌번호·비밀번호 **저장 금지** — `account_last4`·`bank_code`·`payer_name`만 |
| 표시 | 목록·표에서 계좌는 **`****1234`** 형식 · **ACTIVE** 행만 **「해지」** 버튼 (`CmsEnrollmentTable`) |

> **Swagger**: `POST /api/v1/billing/cms/enrollments` — `{ "clientId", "guardianUserId", "payerName", "bankCode", "accountLast4" }`

> 관련: Q206 · Q208 · Q299 · USER_MANUAL §4-6

### Q208. CMS **출금 요청** 후 청구 상태는 어떻게 되나요?

**A.** **확정(`CONFIRMED`)** 청구만 출금 가능합니다. **`POST /api/v1/billing/cms/claims/{claimId}/debit`** 성공 시:

| 항목 | 내용 |
|------|------|
| 출금 이력 | `cms_debit_requests.status=SUCCEEDED` · `fcms_transaction_id` (stub: `stub-fcms-txn-*`) |
| 청구 | **`PAID`** · `paid_at` · **`payment_method=CMS`** |
| UI | **`CmsPage`** **CMS 출금** 탭 — 성공 후 **확정 청구 목록에서 해당 행 제외** (`c0a01b4`) |
| 알림 | J03 **`BILLING_PAYMENT_RECEIVED`** dispatch (Q147) |
| 실패 | `422` + `failure_reason` — 청구는 **CONFIRMED 유지** |

| stub 환경 | **`FCMS_PROVIDER=stub`** — **`StubFcmsClient`** 가 즉시 성공 반환. 실제 은행 출금 없음 |
| 선행 조건 | 이용자에 **ACTIVE CMS 등록** 필요 — 없으면 「CMS 자동이체가 등록되지 않았습니다.」 |
| 중복 | 동일 청구 **진행 중(`REQUESTED`)** 출금 재요청 거부 · **성공(`SUCCEEDED`)** 이력 있으면 **청구·금액 무결성 검증 후** 상태 조회만 (`6bf51c8`, Q256) |
| 무결성 | **본인부담금 ≤ 0** 청구 출금 거부 · FCMS 응답 **금액 ≠ 청구 금액** 시 **`PAID` 미전환**·`FAILED` (`27f20de`, Q256) |

> **UI**: **CMS 출금** 탭 → 청구 선택 → **CMS 출금 요청** · 하단 **출금 상태** 패널(`StatusBadge`)

> **연말정산**: CMS로 수납된 본인부담금은 **의료비공제 집계에서 제외**됩니다 (Q254).

> 관련: Q174 · Q206 · Q254 · Q256 · USER_MANUAL §4-6 · DEPLOYMENT §4-6

### [TWR] Q299. CMS 자동이체 **해지**는 어떻게 하나요?

**A.** **Fixed (BE `a34d0eb`·`4a622ab`·FE `9a6fdb6`, G2/US-L03)** — 센터 **`hq_admin`·`branch_admin`** 이 **`/billing/cms`** → **등록 관리** 탭에서 수행합니다.

| 단계 | 내용 |
|------|------|
| 1 | **이용자** 선택 |
| 2 | **등록 이력** 표에서 **등록완료(`ACTIVE`)** 행의 **해지** 클릭 |
| 3 | Modal에서 예금주·은행·계좌 끝 4자리 확인 → **해지 확인** |
| 4 | FCMS **`unregisterMember`** 후 **`cms_enrollments.status=CANCELLED`** |
| 5 | **해지 이력은 목록에 유지** — 재등록·감사 추적 (`4a622ab`) |

| 제한 | 내용 |
|------|------|
| 대상 | **ACTIVE** 등록만 — 이미 **CANCELLED** 이면 **`422`** |
| 출금 진행 중 | **`cms_debit_requests.status=REQUESTED`** 이면 「CMS 출금 요청이 진행 중이어서…」 **`422`** |
| 재등록 | 해지 후 **동일 보호자**로 재등록 시 **기존 행 재활성화** · **최초 `created_at` 보존** (Q207) |
| 다른 보호자 | 동일 이용자에 **다른 보호자 ACTIVE** 가 남아 있으면 **새 보호자 등록 거부** — 기존 등록 **해지 후** 등록 (`72aff00`) |

| API | `DELETE /api/v1/billing/cms/enrollments/{enrollmentId}` |
| UI | **`CmsPage`** 해지 Modal · **`cancelCmsEnrollmentApi`** · **`CmsPage.test`** |
| RBAC | **`hq_admin`·`branch_admin`** — **`caregiver`** 등 **403** |

> 관련: Q206 · Q207 · Q208 · USER_MANUAL §4-6 · ADMIN_GUIDE §10-13 · DEPLOYMENT §4-6

### Q209. 청구 **확정·수납** 후 NHIS 엑셀을 **재업로드**할 수 있나요?

**A.** **UI에서는 차단됩니다 (FE `190b2b1`·`c4fb7ff`, G21 weekly confirm-lock)** — 선택 **청구 월**에 **`CONFIRMED` 또는 `PAID`** 본인부담 청구가 1건 이상이면 **`/billing/imports/nhis`** **업로드** 버튼이 **비활성**됩니다. 이지케어 FAQ **21474**와 동일한 **「확정 잠금」** 운영 흐름입니다.

| 항목 | 내용 |
|------|------|
| 안내 UI | **`NhisScheduleConfirmLockGuide`** — 「청구 확정 잠금 (주간보호)」 5단계 · locked 시 **warning** 톤 |
| 차단 조건 | `GET /billing/claims` — 해당 **`yearMonth`** · **`CONFIRMED`/`PAID`** 건수 ≥ 1 |
| 오류 메시지 | `{month}에 확정·수납된 청구서가 {N}건 있어 재업로드할 수 없습니다…` |
| 해제 방법 | 해당 월 청구 **상태 조정**(드물게) · **대사(reconciliation) 보정** 후 재시도 — §4-6-1 |
| 대사 화면 | **`/billing/imports/nhis/:batchId`** — guide **경고만** 표시 · **수동 매칭은 계속 가능** |
| 방문 일정 | **`/visits`** — **별도 규칙**: (1) **billing** confirm-lock guide(청구 확정) · (2) **visit** import lock — **확정 방문 일정** 존재 시 import 차단 (Q195) |

| API 주의 | **백엔드 upload API는 confirm-lock을 강제하지 않음** — Swagger로 직접 `POST /billing/imports/nhis` 호출 시 업로드 **가능** (운영자만 사용) |

> 관련: Q195 · Q181 · USER_MANUAL §4-6-1 · §5-11 · DEPLOYMENT §8-1

### Q210. 이용시간 밴드(`duration_band`)란 무엇인가요?

**A.** **G9 (BE `425a05f`·`0719648`, FE `3f96d95`)** — 공단 주야간보호 수가는 **장기요양등급**뿐 아니라 **1일 이용시간대**에 따라 달라집니다. ogada는 2026 NHIS 기준 **5개 밴드**를 지원합니다.

| 코드 | 의미 |
|------|------|
| `H3_6` | 3~6시간 |
| `H6_8` | 6~8시간 |
| `H8_10` | 8~10시간 |
| `H10_13` | 10~13시간 (파일럿 **기본값**) |
| `H13_PLUS` | 13시간 이상 |

| 저장 위치 | 용도 |
|----------|------|
| `clients.duration_band` | 이용자별 적용 밴드 — **신규** 청구 생성 시 수가 조회 키 |
| `fee_schedules.duration_band` | 등급×연도×밴드별 1일 수가 |
| `billing_claim_items.duration_band_snapshot` | 청구 **생성 시점** 밴드 고정 — 확정 후 이용자 밴드 변경과 무관 (V62, Q213) |

파일럿 센터(08:00~20:00, 12시간)는 기본 **`H10_13`** 입니다. Flyway **V61**·**V62**가 스키마·스냅샷을 갱신합니다.

> 관련: Q211 · Q213 · USER_MANUAL §5-4 · ADMIN_GUIDE §6-3-1 · DEPLOYMENT §8-1

### Q211. 수가표·이용자 등록에 「이용시간대」 선택이 생겼어요.

**A.** **G9 UI Fixed (FE `3f96d95`)** — 아래 화면에 **`DurationBandSelect`**·**`FeeScheduleMatrix`** 가 추가되었습니다.

| 화면 | 경로 | 동작 |
|------|------|------|
| 수가표 관리 | `/billing/fee-schedules` | **`FeeScheduleMatrix`** — 등급×이용시간대 **2차원 표** · 셀 클릭 등록·수정 · **「공단 2026 수가 시드」** 25건 일괄 등록 (Q214) |
| 이용자 등록·수정 | `/clients/new`, `/clients/:id/edit` | 이용자 **`durationBand`** 저장 — **신규** 청구 시 해당 밴드 수가 자동 적용 |
| 수가 이력 | `FeeRateHistoryPanel` | 연도·등급·**밴드**별 이력 필터 |
| 청구 상세 | `/billing/claims/:id` | 급여 항목·요약에 **`durationBandSnapshot`** 표시 (Q213) |

**운영 절차** — 월말 청구 전 ① 이용자별 밴드 확인 ② **모든 사용 밴드×등급** 조합에 대해 해당 연도 수가 등록(또는 시드) ③ 청구 생성.

> 관련: Q91 · Q210 · Q214 · USER_MANUAL §5-4

### Q212. 보호자 포털에서 초안(DRAFT) 명세가 안 보여요.

**A.** **의도된 동작 — FE·BE 이중 필터 (FE `0dc4c4a`·`3f96d95` + BE `3def542`, US-J02)** — 보호자 **「명세·청구」** 탭은 **`CONFIRMED`(확정)·`PAID`(수납)** 청구만 표시합니다. 센터가 아직 확정하지 않은 `DRAFT` 청구는 보호자에게 노출되지 않습니다.

| 항목 | 내용 |
|------|------|
| API | `GET /guardian/clients/{clientId}/billing` — **`BillingService.listGuardianClientBillingHistory`** — **`CONFIRMED`·`PAID`만** 서버 WHERE 필터 (`3def542`) |
| FE 필터 | **`guardianBilling.js`** — CONFIRMED/PAID 클라이언트 필터 · 페이지 병합 시 **중복 제거** |
| UI | **「더 보기」** — 다음 페이지를 기존 목록에 **병합** |
| 오류 | 명세 로드 실패 시 **「다시 시도」** 버튼 — `aria-label`·로딩 상태 분리 |
| 인쇄·상세 | 행 **「상세」** → `GuardianBillingDetailModal` — **이용시간대** 스냅샷 표시 · **「인쇄」** (Q175) |

> **보안**: FE 필터만으로는 Swagger 직접 호출 시 DRAFT가 노출될 수 있었으나, **`3def542`부터 API 응답에서 DRAFT가 제외**됩니다.

> 관련: Q132 · Q175 · Q213 · USER_MANUAL §8-2

### Q213. 청구서의 「이용시간대」가 이용자 프로필과 달라요. 왜 그런가요?

**A.** **G9 V62 Fixed (BE `0719648`·`a4a1393`, FE `eb3f0fd`)** — 청구 **생성 시점**에 적용된 이용시간 밴드가 **`duration_band_snapshot`** 으로 **라인별 고정**됩니다. 이후 이용자 `duration_band`를 바꿔도 **이미 생성·확정된 청구**는 당시 밴드·수가를 유지합니다 (REQUIREMENTS §3-9-1 「과거 청구는 당시 수가 유지」).

| 위치 | 필드 | 의미 |
|------|------|------|
| DB | `billing_claim_items.duration_band_snapshot` | Flyway **V62** — CHECK 5밴드 |
| API | `BillingClaimItemResponse.durationBandSnapshot` | 청구 상세 `GET /billing/claims/{id}` |
| API | `ClientBillingHistoryItemResponse.durationBandSnapshot` | 보호자 `GET /guardian/clients/{id}/billing` |
| UI | `BillingDetailPage`·`GuardianBillingDetailModal` | **`resolveDurationBand`** — **스냅샷 → 현재 밴드** 순 표시 (`durationBandLabel`) |
| UI | `resolveClaimDurationBand` | 청구 요약 — **주 라인 스냅샷 → 청구 헤더 밴드** fallback (`guardianBilling.js`) |

| 상황 | 동작 |
|------|------|
| 이용자 밴드 변경 **후** | **다음 달 신규 청구**부터 새 밴드 수가 적용 |
| 기존 `CONFIRMED`/`PAID` 청구 | 스냅샷 **불변** — 대사·명세 감사 추적용 |
| V61 이전 라인 | backfill 기본값 **`H10_13`** (파일럿 10~13시간) |
| 스냅샷·현재 밴드 둘 다 있음 | UI는 **스냅샷 우선** — 프로필과 달라 보이는 것이 **정상** |

> 관련: Q210 · Q211 · USER_MANUAL §5-4 · §4-6 · ADMIN_GUIDE §6-3-1 · DEPLOYMENT §8-1

### Q214. 「공단 2026 수가 시드」 버튼은 무엇인가요?

**A.** **G9 UI Fixed (FE `0c34f85`)** — `/billing/fee-schedules` 상단 **등급×이용시간대 2차원 표**(`FeeScheduleMatrix`) 아래에, **아직 등록되지 않은 셀**만 대상으로 **롱텀 2026 공식 주야간 1일 수가 25건**을 일괄 등록합니다.

| 항목 | 내용 |
|------|------|
| 데이터 | `NHIS_2026_DAYCARE_RATES` — 등급 1~5 × 밴드 5종 (`feeSchedules.js`) |
| API | 미등록 셀마다 `POST /billing/fee-schedules` — `{ year: 2026, ltcGrade, durationBand, dailyRate, effectiveFrom: "2026-01-01" }` |
| UI | 버튼 라벨 **「공단 2026 수가 시드 (N건)」** — N = 미등록 셀 수 · 전부 등록되면 버튼 **숨김** |
| 매트릭스 | 셀 클릭 → 등록·수정 모달 · `aria-label`에 연도·등급·밴드·금액 |

> **주의**: 시드는 **누락 셀만** 채웁니다. 이미 다른 금액이 등록된 셀은 **덮어쓰지 않습니다**. 개정 수가는 **수정 모달** 또는 Swagger로 forward-only 적용 (Q48).

> 관련: Q91 · Q210 · Q211 · USER_MANUAL §5-4

### Q215. CMS 출금 시 「이용자 단건 청구서에서만」 오류가 나요.

**A.** **G2 CMS guard Fixed (BE `a4a1393`)** — `POST /billing/cms/claims/{claimId}/debit` 는 청구 **라인이 모두 동일 이용자**일 때만 허용됩니다. 한 청구서에 **여러 이용자** 항목이 섞이면 `422 BUSINESS_RULE` — 「CMS 출금은 이용자 단건 청구서에서만 요청할 수 있습니다.」

| 규칙 | 이유 |
|------|------|
| 단건 이용자 | CMS 등록(`cms_enrollments`)은 **이용자·보호자·계좌** 단위 |
| 혼합 청구 | 월별 **이용자별 개별 청구** 생성 후 각각 CMS 출금 |
| 기타 전제 | **`CONFIRMED`** 상태 · **ACTIVE** CMS 등록 · stub/live FCMS (Q206–Q208) |

> 관련: Q206 · Q207 · USER_MANUAL §4-6 · ADMIN_GUIDE §10-13

### Q216. 급여제공기록지를 보호자에게 **이메일**로 보낼 수 있나요?

**A.** **Partial Fixed (BE `f77a268`·`8bdead6` + FE `08dbcf0`, G2·G15)** — **월간 조회 UI Fixed**(Q243). **이메일 발송**은 여전히 **Swagger** — **`POST /api/v1/clients/{clientId}/notifications/care-provision-record`**.

| 항목 | 내용 |
|------|------|
| **조회 UI** | **`/clients/:id` → 「급여제공」** 탭 — **`CareProvisionRecordPanel`** — 출석·확정 배차·차량번호 일별 대조 (Q243) |
| 발송 API | `POST …/notifications/care-provision-record` — **`branch_admin`·`social_worker`** |
| 요청 | `{ "yearMonth": "YYYY-MM", "summary": "요약 (500자 이하, 선택)" }` |
| 템플릿 | `CARE_PROVISION_RECORD` — subject **`[ogada] 급여제공기록지 안내`** |
| 본문 보강 | **`transportServiceProvided`** · **`vehiclePlateNumber`** — 확정 배차·차량 마스터 연계 (`8bdead6`) |
| 전제 | 보호자 **`channelEmail=true`** · **`users.email`** 등록 (Q204) |
| 이력 | `notifications.channel=email` · §4-7-2 이력 패널에서 확인 |

> **발송 UI**는 후속 — Swagger (USER_MANUAL §4-7-3). *(노인학대예방 지침은 Q222 UI Fixed.)*

> 관련: Q204 · Q217 · Q243 · USER_MANUAL §3-3·§4-7-3 · ADMIN_GUIDE §10-9

### Q217. 가정통신문을 보호자에게 **이메일**로 보낼 수 있나요?

**A.** **예 — API 구현됨 (BE `f77a268`, G2)** — **`POST /api/v1/clients/{clientId}/notifications/home-newsletter`** 로 **가정통신문** 이메일을 dispatch합니다. **화면 UI는 후속** — Swagger (USER_MANUAL §4-7-3). *(노인학대예방 지침·납부확인서는 Q221·Q222 UI Fixed.)*

| 항목 | 내용 |
|------|------|
| 권한 | `branch_admin`, `social_worker` |
| 요청 | `{ "yearMonth": "YYYY-MM", "summary": "통신문 본문 요약" }` |
| 템플릿 | `HOME_NEWSLETTER` — subject **`[ogada] 가정통신문 안내`** |
| 본문 | 센터명·이용자명·연월·요약 |
| 전제 | Q204와 동일 — email preference·등록 이메일 |
| DB | **신규 마이그레이션 없음** — 기존 `notifications` 테이블·1년 보존 정책 (DATA_RETENTION_POLICY §4-1) |

> 관련: Q204 · Q216 · USER_MANUAL §4-7-3 · ADMIN_GUIDE §10-9

### Q218. 입금 처리에서 **0원·과납**을 입력하면 어떻게 되나요?

**A.** **Fixed (BE `4109680` + FE `dd72ff8`, US-L01/L02, G2)** — 본인부담금 수납 시 **금액 검증**이 백엔드·프론트 **양쪽**에 적용됩니다.

| 계층 | 규칙 | 오류 메시지(예) |
|------|------|----------------|
| **FE `PaymentRecordModal`** | **0 이하** · **미납 본인부담금 초과** 입력 시 **저장 버튼 제출 차단** | 「양수 입금 금액을 입력하세요.」·「입금 금액은 미납 본인부담금을 초과할 수 없습니다.」 |
| **BE `recordCopayPayment`** | **`amount` ≤ 0** → `422` · **`copayAmount` NULL** → `422` · **본인부담금과 불일치** → `422` · **생략** 시 전액 수납 | 「입금 금액은 0보다 커야 합니다.」·「청구서 본인부담금이 설정되지 않아 입금 처리할 수 없습니다.」(Q257) · 「입금 금액이 본인부담금과 일치하지 않습니다.」 |
| 대상 상태 | **`CONFIRMED`만** — `DRAFT`·이미 `PAID` 거부 | — |
| CMS 연동 | CMS 출금 성공 시에도 동일 **`recordCopayPayment`** 경로 (Q208) | — |

> **현장 팁** — 모달을 열면 **미납 본인부담금 전액**이 기본값으로 채워집니다. 부분 수납은 **현재 MVP에서 지원하지 않습니다** — `amount`는 본인부담금과 **정확히 일치**해야 합니다.

> 관련: Q174 · Q208 · Q257 · USER_MANUAL §4-6 · ADMIN_GUIDE §10-6

### Q219. 「보호자 발송」건수(`dispatchedCount`)가 청구 라인 수와 다른 이유는?

**A.** **의도된 동작 (BE `40567a2`, G2)** — 한 청구서에 **동일 이용자 라인이 여러 개** 있어도, 보호자 알림은 **이용자(`clientId`)당 1회**만 발송됩니다.

| 항목 | 내용 |
|------|------|
| 원인 | 과거 데이터·import 오류 등으로 **중복 `billing_claim_items`** 가 있을 수 있음 |
| BE 처리 | **`dispatchBillingNotifications`** — `LinkedHashMap`으로 **첫 라인만** dispatch |
| 응답 | `{ claimId, dispatchedCount }` — **unique 이용자 수** |
| UI | 「보호자 **N**건에게 명세 안내를 발송했습니다.」— **N = dispatchedCount** |
| 테스트 | **`BillingServiceTest.notifyClaimGuardiansShouldDeduplicateDuplicateClientLineItems`** |

> **알림톡·SMS·email** 채널 모두 동일 dedupe 규칙입니다. 수납 완료 알림(`BILLING_PAYMENT_RECEIVED`)도 동일합니다.

> 관련: Q196 · Q147 · USER_MANUAL §4-6 · ADMIN_GUIDE §10-6

### Q220. 청구·보호자 명세 금액이 **NaN** 또는 **빈 칸**으로 보여요.

**A.** **Fixed (FE `8a771cf`·`382e553`·`00a8a57`, US-G02·J02·L01)** — API가 BigDecimal을 **JSON 문자열**(`"150000"`, `"150,000"`)로 반환해도 UI가 **안전하게 원화 표기**합니다.

| 컴포넌트 | 처리 |
|----------|------|
| **`guardianBilling.js` `normalizeAmount`** | string·number → **finite number** — 보호자 포털·입금 모달 공유 |
| **`services.js`** | claims·overdue 목록 **`copayAmount`·`totalAmount`** 정규화 |
| **`BillingDetailPage.formatWon`** | 콤마 제거 후 **`toLocaleString('ko-KR')`** — NaN 시 원문 fallback |
| **`PaymentRecordModal`** | 수납 금액 기본값·검증에 **`normalizeAmount`** 사용 (Q218) |
| Vitest | **`BillingDetailPage.test`** · **`PaymentRecordModal.test`** · **`guardianBilling.test`** · **`billingGuardianPlatformServices.test`** |

> **백엔드**는 금액을 **숫자 또는 문자열** 모두 반환할 수 있습니다. 프론트는 **표시·입력 검증**만 담당하며, **수납 저장 규칙**(Q218)은 백엔드가 최종 검증합니다.

> 관련: Q174 · Q213 · USER_MANUAL §4-6 · §8-2

### Q221. 청구 상세 **「납부확인서 발송」** 버튼은 언제 보이나요?

**A.** **Fixed (BE `0854fbd`·`588b8e6` + FE `eedcc80`, G2)** — **`POST /api/v1/billing/claims/{claimId}/payment-receipt-notify`** 로 연결 보호자에게 **`BILLING_PAYMENT_RECEIVED`** 알림을 **수동 재발송**합니다.

| 항목 | 내용 |
|------|------|
| 표시 조건 | 청구 **`PAID`** · **`paidAt`(입금일) NOT NULL** · **`paymentMethod` NOT NULL** — `CONFIRMED`만이면 **버튼 없음** (`64ebf6e`, Q249) |
| 권한 | `hq_admin`·`branch_admin` — 지점 스코프 검증 |
| 본문 | **수납일·수납 수단**(`CASH`/`BANK_TRANSFER`/`CMS`)·본인부담금·센터명·이용자명 (`588b8e6`) |
| dedupe | 동일 청구 **이용자(`clientId`)당 1회** dispatch (Q219) |
| 자동 vs 수동 | **`POST …/payments`**·CMS 출금 성공 시 **자동** 발송(J03) + 필요 시 **수동 재발송** |
| UI | **`BillingDetailPage`** — 성공 시 「보호자 N건에게 납부확인서를 발송했습니다.」 |

> 관련: Q174 · Q204 · Q208 · Q219 · USER_MANUAL §4-6 · ADMIN_GUIDE §10-8

### Q222. 이용자 상세 **「노인학대예방 지침 발송」** 카드는 무엇인가요?

**A.** **Fixed (BE `0854fbd` + FE `eedcc80`, G2)** — **`GuardianDocumentNotifyPanel`** 이 **`POST /api/v1/clients/{clientId}/notifications/elder-abuse-prevention-guideline`** 를 호출합니다.

| 항목 | 내용 |
|------|------|
| 화면 | `/clients/:id` → **기본정보** 탭 — **「노인학대예방 지침 발송 (G2)」** 카드 |
| 입력 | **대상 연월**(`MonthInput`, 필수) · **요약**(선택, 500자 이하) |
| 템플릿 | `ELDER_ABUSE_PREVENTION_GUIDELINE` — subject **`[ogada] 노인학대예방 및 대응지침 안내`** |
| 권한 | `branch_admin`·`social_worker` |
| 전제 | 보호자 **`channelEmail=true`** · **`users.email`** (Q204) · **`notify_daily_care`** 동의 재사용 |
| DB | **신규 마이그레이션 없음** — `notifications` 1년 보존 (DATA_RETENTION_POLICY §4-1) |

> **급여제공기록지** — **조회 UI Fixed**(Q243) · **발송 UI 없음** — Swagger (Q216). **가정통신문** 발송 UI **없음** (Q217).

> 관련: Q204 · Q216 · Q217 · USER_MANUAL §4-7-3 · ADMIN_GUIDE §10-9

### Q223. 지점 등록 시 **「통합재가 가산」** 안내가 보입니다 (G19).

**A.** **UI 안내 Fixed (FE `4c7c994`·`9afa30e`, G19)** — 급여종 **`INTEGRATED_HOME`(통합재가)** 선택 시 등록 모달에 **warning `Alert`** 와 **롱텀 포털 기관 검색 안내 패널**이 표시됩니다.

| 항목 | 내용 |
|------|------|
| 가산 문구 | 「통합재가 주·야간보호형 가산(월 100,000원/인, 고시 제55조의2)은 v1에서 자동 청구·정산하지 않습니다.」 |
| **기관 검색 안내 (171차)** | **`IntegratedHomeProviderDiscoveryPanel`** — BE **`GET /api/v1/branches/integrated-home/provider-discovery`** (`f44ee73`) — 국민건강보험공단 [**장기요양기관 검색**](https://www.longtermcare.or.kr/npbs/r/a/201/selectLtcoSrch.web?menuId=npe0000002783) 링크 · 필터 **`ltcAdminKindChoiceYn8=Y`**(통합재가) · **`searchAdminKindCd=06`**(주야간) · **`07`**(단기) 코드 안내 |
| 범위 | **안내·외부 링크만** — ogada는 공단 포털 검색을 **대체하지 않음** · v1 **Won't**: 가산 자동 청구·정산 |
| 근거 | MOHW 고시 **제2025-247호 제55조의2** (BNK-44 P1) |
| 운영 | 통합재가 지점은 **수동**으로 가산 여부·금액을 확인·기록해야 합니다 |

> 관련: Q180 · Q357 · USER_MANUAL §5-3 · REQUIREMENTS G19

### Q224. **청구명세서 생성 기준**(케어포 9-1)은 어디서 바꾸나요?

**A.** **Fixed (BE `b953662` + FE `ac23529`, US-M03, V63)** — Tenant(조직) 단위 **`claim_generation_basis`** 설정입니다. FE는 레거시 값 **`ATTENDANCE`/`NHIS`** 를 **`ATTENDANCE_SCHEDULE`/`NHIS_IMPORT`** 로 자동 정규화합니다 (`5bdb476`·`ac23529`).

| 항목 | 내용 |
|------|------|
| 화면 | **`/organization/settings`** → **「청구·정산」** 카드 — **`BillingSettingsPanel`** (`hq_admin` only) |
| 옵션 | **`ATTENDANCE_SCHEDULE`** — 급여일정(출석) 기반 **(기본값)** · **`NHIS_IMPORT`** — 공단 청구내역 엑셀 import 기반 |
| API 조회 | `GET /api/v1/settings/billing` — `hq_admin`·`branch_admin` |
| API 저장 | `PATCH /api/v1/settings/billing` `{ "claimGenerationBasis": "NHIS_IMPORT" }` — **`hq_admin` only** |
| DB | **V63** `organizations.claim_generation_basis` CHECK |

**`NHIS_IMPORT` 선택 시** — 해당 월 **NHIS 엑셀 import**가 선행되어야 `POST /billing/claims/generate`가 성공합니다. import 없으면 「공단 청구내역 import가 필요합니다」 오류 (USER_MANUAL §5-5·§4-6).

> 관련: Q179 · Q225 · USER_MANUAL §5-5 · ADMIN_GUIDE §6-3

### Q225. 전월 **미입금** 청구가 있으면 이번 달 청구를 만들 수 없나요?

**A.** **Fixed (BE `857bd32` + FE `911e732`·`60dc5d0`, US-M03, 케어포 7-1/7-2)** — **전월(`yearMonth - 1`)** 에 **`CONFIRMED`(확정·미수납)** 상태 청구가 **1건 이상**이면 차단됩니다.

| 항목 | 내용 |
|------|------|
| 사전 점검 | `GET /api/v1/billing/claims/generation-guard?branchId=&yearMonth=` — `blocked`·`unpaidPriorMonthClaimCount`·`message` |
| 생성 API | `POST /api/v1/billing/claims/generate` — 동일 규칙 위반 시 **`BusinessRuleException`** |
| UI | **`BillingPage`** **`ClaimGenerationPanel`** — **`ClaimGenerationGuardBanner`** warning · **「월별 청구 생성」** 버튼 비활성 · **`LifecycleWorkflowPanel`** 7-2→7-1 단계 안내 (`338c014`, Q310) |
| API 실패 시 | **`60dc5d0`** — generation-guard API **오류·일시 장애** 시에도 생성 버튼 **비활성** — 전월 미납 가드 **우회 방지** |
| 해제 | 전월 청구를 **`/billing/payments`** 에서 **수납(`PAID`)** 처리하거나, 확정 취소가 필요한 경우 운영 정책에 따라 조치 |

> **`PAID` 전월 청구**는 차단 대상이 **아닙니다**. **`DRAFT`만** 있는 경우도 차단하지 않습니다 — **확정 후 미수납**만 집계합니다.

> 관련: Q174 · Q218 · USER_MANUAL §4-6 · ADMIN_GUIDE §10-4

### Q226. **재가급여 월한도액** 초과 경고는 어디서 보나요?

**A.** **Fixed (`a92e625`·`20bc1be`·`fba5ea8`, BNK-47·49·51, US-M04, G27)** — 2026 시행 **재가급여 월한도액**(MOHW 제2025-247호) 대비 **공단부담금(`nhisAmount`) 초과** 이용자를 **사전 점검**합니다. **청구 생성을 차단하지 않습니다**(non-blocking warning).

| 항목 | 내용 |
|------|------|
| 참조표 | `GET /api/v1/billing/monthly-benefit-caps?year=2026` — **1~5등급 + 인지지원등급** 월한도(원) |
| 사전 점검 | `GET /api/v1/billing/claims/monthly-cap-guard?branchId=&yearMonth=YYYY-MM` — `warningCount`·`exceededClients[]`·`message` |
| 권한 | 참조표 — `hq_admin`·`branch_admin`·`social_worker` · 가드 — `hq_admin`·`branch_admin` |
| 2026 월한도 (예) | 1등급 **2,512,900** · 2등급 **2,331,200** · 3등급 **1,528,200** · 4등급 **1,409,700** · 5등급 **1,208,900** · **인지지원등급 `COGNITIVE_SUPPORT` 676,320** |
| UI — 지점·월 | **`/billing`** · **`/dashboard`** — **`MonthlyBenefitCapGuardPanel`** + **`MonthlyBenefitCapGuardBanner`** — 초과 시 `role="alert"` 경고·이용자 최대 3명 미리보기 · **초과 0건 시** **「재가급여 월한도 점검 완료」** success (`62f022d`) |
| UI — 청구 상세 | **`/billing/claims/:id`** — **`MonthlyBenefitCapBanner`** — 해당 이용자 **등급별 한도·현재 공단부담·초과액** 표시 |
| 인지지원등급 | BE **`MonthlyBenefitCapCatalog`** + FE **`feeSchedules.js`** — **676,320원 동기화** (`20bc1be`·`fba5ea8`) |

**`exceededClients[]` 필드**: `clientId`·`clientName`·`ltcGrade`·`nhisAmount`·`capAmount`·`exceededAmount`(초과액).

> 관련: Q179 · Q224 · Q228 · USER_MANUAL §4-6 · ADMIN_GUIDE §10-4

### Q227. 은행 **거래내역 엑셀**으로 본인부담금을 한꺼번에 입금 처리할 수 있나요?

**A.** **Fixed (`e50533f`·`95bb34d`·`f4bb171`·`758e590`, BNK-48·49, US-L01, 케어포 7-2)** — 은행 **입금 내역 xlsx**를 업로드해 **확정(`CONFIRMED`) 청구**에 자동 수납합니다. **`/billing/payments`** **`BankDepositImportPanel`** 이 JWT **`activeBranchId`** 를 **`branchId`** 로 전송합니다 (`f4bb171`).

| 항목 | 내용 |
|------|------|
| API | `POST /api/v1/billing/imports/bank-deposits` — `multipart/form-data` — **`branchId`(필수)** + `file` + `yearMonth`(선택) |
| UI | **`/billing/payments`** 하단 **`BankDepositImportPanel`** — 「은행 입금 엑셀 일괄 등록」·적용 월·파일 업로드 · 성공 시 **`appliedCount`** 요약 |
| **지원 은행 8종** | **Fixed (FE `758e590`)** — 패널 **「지원 은행 8종 엑셀 형식 (케어포 7-2 p.88)」** `<details>` 표 — **KB국민·우리·NH농협·신한·하나·부산·대구·광주** 컬럼 예시 (`bankDepositFormats.js`) |
| 권한 | `hq_admin`·`branch_admin` |
| 엑셀 헤더 | **거래일**(`거래일`·`입금일` 등) · **입금자**(`입금자`·`적요`·`거래내용` 등) · **금액**(`입금액`·`거래금액` 등) — 한국 은행 export **유연 매칭** |
| 매칭 규칙 | **입금자명 ≈ 이용자명** + **금액 = 본인부담금** + **`CONFIRMED` 단일 라인 청구** |
| 월 disambiguation | 동일 이름·금액 청구가 **여러 달**이면 **거래일 월**로 자동 선택 (`95bb34d`) |
| 동월 중복 | **같은 달**에 동일 조건 청구가 2건 이상 → **`UNMATCHED`** — 수동 입금 (`/billing/payments`) |
| 다수 이용자 청구 | 한 청구에 **이용자 2명 이상** → **`SKIPPED`** — 수동 입금 |
| 성공 시 | `recordCopayPayment` — **`PAID`·`payment_method=BANK_TRANSFER`** · J03 수납 알림 |
| 행 상태 | `APPLIED` · `SKIPPED` · `UNMATCHED` — 응답 `rows[]`에 `message` |

**다지점 주의**: `hq_admin`은 **BranchSwitcher**로 작업 지점을 선택한 뒤 업로드하세요. 활성 지점이 없으면 패널이 **「활성 지점이 없습니다」** 오류를 표시합니다 (Q228).

> 관련: Q174 · Q218 · Q225 · Q228 · Q258 · USER_MANUAL §4-6 · ADMIN_GUIDE §10-13

### Q228. **인지지원등급** 월한도·은행 일괄입금 UI에서 주의할 점은?

**A.** **Fixed (`20bc1be`·`f4bb171`·`fba5ea8`, BNK-51·US-L01·G27)** — 이전 BNK-49 갭(**BE catalog·`branchId`**)이 **2026-06-10 74차**에 해소되었습니다. 아래는 **현장 운영 시** 확인 사항입니다.

| 항목 | 내용 |
|------|------|
| 인지지원등급 cap | BE **`MonthlyBenefitCapCatalog`** + FE — **`COGNITIVE_SUPPORT` 676,320원** · `ltcGrade=0` · API·가드·배너 **동일 값** |
| 은행 일괄입금 | **`BankDepositImportPanel`** — `branchId` + `file` + `yearMonth` 전송 · **`appliedCount`/`unmatchedCount`/`skippedCount`** 요약 표시 |
| 다지점 | `hq_admin` — **BranchSwitcher**로 대상 지점 선택 후 업로드 (`activeBranchId`) |
| 미매칭 시 | **`UNMATCHED`/`SKIPPED`** 행은 **`PaymentRecordModal`** 개별 수납 (Q174) |

> 관련: Q226 · Q227 · USER_MANUAL §4-6 · ADMIN_GUIDE §10-4

### Q229. **야간·심야·휴일 가산율** 안내는 어디서 보나요?

**A.** **Fixed (`904072b`·`d7475fd`·`f987b9d`, G11, BNK-20·56)** — MOHW 2026 **급여 가산율** 참고표·**미리보기**·**출석 기반 청구 생성 시 일별 자동 반영**을 제공합니다.

| 항목 | 내용 |
|------|------|
| UI | **`/billing/fee-schedules`** 하단 **`FeeSurchargeGuidePanel`** — 가산율 표 · **유형별 미리보기** · **제공일·입·퇴소 시각 미리보기**(API) · **계획일정 vs 청구일정 차이** 8종 안내 |
| 2026 가산율 | **야간** +20% (18:00~22:00) · **심야** +30% (22:00~06:00) · **주말·공휴일(일요일)** +30% · **유급휴일·근로자의 날** +50% |
| 중복 규칙 | **가산은 중복 적용하지 않음** — 제공 시간 기준 **가장 높은 가산율 1종만** 적용 |
| **자동 청구** | 조직 설정 **`ATTENDANCE_SCHEDULE`**(출석 기준) 시 **`POST /billing/claims/generate`** 가 출석 **입·퇴소 시각·휴일**로 **일별 가산 자동 반영** (`d7475fd`) · **`ClaimGenerationPanel`** 안내 문구 표시 |
| **가산 미적용** | **`NHIS_IMPORT`**(공단 엑셀 기준) — **일수×기준 1일 수가** (가산 없음) |
| API — catalog | `GET /api/v1/billing/fee-surcharge-rates` — `rates[]`·`noStackingNote`·`v1Notice` |
| API — preview | `POST /api/v1/billing/fee-surcharge-preview` — ① `{ "baseAmount", "surchargeCode" }` 또는 ② `{ "baseAmount", "serviceStartAt", "serviceEndAt" }` → `surchargedAmount`·`surchargeCode` |
| `surchargeCode` | `NIGHT` · `LATE_NIGHT` · `WEEKEND_HOLIDAY` · `PAID_HOLIDAY` |
| 권한 | `hq_admin` · `branch_admin` · `social_worker` (`caregiver` **403**) |
| 운영 | 정확한 **입·퇴소 시각** 기록이 가산 반영의 전제 — 출석 화면에서 체크아웃 누락 시 기본 수가만 적용될 수 있음 |

> 관련: Q210 · Q214 · Q224 · USER_MANUAL §4-6·§5-4 · ADMIN_GUIDE §10-4

### Q230. **이동서비스 수칙·계약서** 체크리스트는 어디에 있나요?

**A.** **✅ full stack (`3c8f9fe`·`9e3cab5`·`0cfa970`·`aaaeb10`·`7a4b310`·`9dfef92`, G15 v1.3-C + G16 partial)** — 2026 평가 지표 **41·42** 대응 **운영 체크리스트**입니다. **수칙·서명·일지 준수 기록은 서버에 저장**됩니다 (Q231·**Q407**). **G16 이동서비스비 청구 기록 생성 UI Fixed**(Q239) — **공단 포털 자동 제출**은 **미지원**(Q237).

| 항목 | 내용 |
|------|------|
| UI | **`/transport/compliance`** **`TransportCompliancePanel`** — **이동서비스 수칙·계약 (G15)** (Q397) |
| 워크플로 | ① **수칙 5필수** 마련 → ② **계약서에 수칙 포함** → ③ **이동서비스일지(제22호)** 작성·**저장**·출력 (Q236·Q407) → ④ **별지 제18호** 공단 신청 (Q237) |
| 체크리스트 5항목 | 운전자 자격 · 동승 직원 · 차량 안전 · 사고 조치 · 차량 운행표(별지 제22호) |
| Modal | **「계약서 템플릿 보기」** — 인쇄·별도 문서화 후 현장 보관 |
| 일지 | **`TransportRunDetailPage`** **`TransportServiceLogPanel`** — **`GET/PUT /service-log`** · 인쇄·텍스트 저장 (Q407) |
| 저장 | **`PUT /api/v1/transport/contracts/{clientId}`** — 5항목·보호자·기관 서명 **DB 영속화** (V64) |
| 권한 | **저장**: `hq_admin`·`branch_admin`·`social_worker` · **조회만**: `caregiver` |
| 범위 | v1.3-A **배차·지도**와 별개 — **G16 청구 기록 UI Fixed**(Q239) · **케어포 2-x 외출 리포트 Fixed**(Q240) |

> 관련: Q159 · Q163 · Q231 · Q236 · Q237 · USER_MANUAL §5-8 · ADMIN_GUIDE §10-10

### Q231. **이동서비스 계약서** API는 어떻게 쓰나요?

**A.** **Fixed (`3c8f9fe`·`9e3cab5`, G15, US-T05, BNK-53 P1)** — 이용자별 **이동서비스 이용 계약서**를 조회·저장합니다.

| 메서드 | 경로 | 설명 | 권한 |
|--------|------|------|------|
| GET | `/api/v1/transport/contracts/{clientId}` | 저장된 계약서 조회 | `hq_admin`·`branch_admin`·`social_worker`·`caregiver` |
| PUT | `/api/v1/transport/contracts/{clientId}` | 수칙·서명 저장 | `hq_admin`·`branch_admin`·`social_worker` |

**PUT 요청 본문**

```json
{
  "completedRuleIds": [
    "driver_qualification",
    "companion_staff",
    "vehicle_safety",
    "accident_response",
    "vehicle_log"
  ],
  "guardianSignatoryName": "홍길동",
  "guardianSignedOn": "2026-06-01",
  "institutionSignatoryName": "김센터장",
  "institutionSignedOn": "2026-06-01"
}
```

| 규칙 | 내용 |
|------|------|
| 5항목 필수 | `completedRuleIds` **5개 모두** 포함 — 미완료 시 `422 BUSINESS_RULE` |
| `fullySigned` | 5항목 + 보호자·기관 **서명·서명일** 모두 입력 시 `true` |
| 404 | 계약 미저장 시 GET — FE는 **빈 폼**으로 시작 |
| DB | **V64** `transport_service_contracts` — Tenant·지점·이용자 UK |
| FE | **`fetchTransportContractApi`·`saveTransportContractApi`** (`services.js`) |

> 관련: Q230 · USER_MANUAL §5-8 · ADMIN_GUIDE §10-10 · DEPLOYMENT §8-1

### Q232. **탑승 출석**과 **현장 출석** 화면이 나뉘어 있나요?

**A.** **Fixed (`d6d7e7f`·`6c4c151`, G15 v1.3-C, US-E06, BNK-58)** — 케어포 **2-2(탑승·차량 이용)** / **2-3(현장·차량 미이용)** 에 맞춰 출석 화면을 분리했습니다.

| 경로 | SideNav | 대상 | API |
|------|---------|------|-----|
| `/attendance` | 출석 현황 | 전체 | `GET /attendance?transportMode=all` |
| `/attendance/boarding` | 탑승(차량) | `usesTransport=true` | `?transportMode=boarding` |
| `/attendance/on-site` | 현장 출석 | `usesTransport=false` | `?transportMode=on_site` |

| 규칙 | 내용 |
|------|------|
| 분류 기준 | 이용자 **`usesTransport`** 프로필 (이용자 등록·수정 **「배차·픽업 정보」**, Q166) |
| BE 필터 | **`AttendanceTransportMode`** — 잘못된 값은 `422 BUSINESS_RULE` |
| FE | **`attendanceTransportMode.js`** — 경로별 mode 해석 · **`AttendancePage`** 공유 컴포넌트 |
| 조작 | 입소·귀가·결석 API는 **전체 출석과 동일** — 화면만 대상 이용자가 다름 |

> 관련: Q166 · Q230 · USER_MANUAL §4-4 · API_SPEC 출석 transportMode

### Q233. 배차 **「지도에서 제외된 주소」** 경고가 뜨고 저장이 안 됩니다.

**A.** **Fixed (`318411d`·`48d90d5`, QA-B19, US-T05)** — 픽업 주소 **지오코딩 실패**(`geocode_status=FAILED`) 정차 또는 **`lat`/`lng` 좌표가 없는** 정차가 있으면 **임시 저장·순서 저장·배차 확정**이 **차단**됩니다.

| 항목 | 내용 |
|------|------|
| 감지 | **`countGeocodeFailures`**(`transportUtils.js`) — `GEOCODE_STATUS.FAILED` **또는 좌표 미보유** 정차 건수 |
| UI | **`Alert tone=warning`** — `id="transport-geocode-warning"` · 저장 버튼 **`disabled`** · **`aria-describedby`** 연결 |
| 적용 화면 | **`TransportRunNewPage`**(임시 저장) · **`TransportRunDetailPage`**(순서 저장·배차 확정) |
| 조치 | ① 이용자 **픽업 주소** 확인·수정(§4-3) ② **`KAKAO_REST_KEY`** 설정 확인(DEPLOYMENT §4-6) ③ 주소 수정 후 배차 화면 **재조회** |
| 정책 | 주소는 DB에 저장되나 **지도·배차 확정 전** 운영자가 반드시 보정해야 함 (PLAN_NOTES QA-B19) |

> 관련: Q166 · Q169 · USER_MANUAL §5-8 · ADMIN_GUIDE §10-10

### Q234. 방문일정 엑셀 import에서 **「동일한 방문일정이 이미 등록되어 있어 import를 건너뜁니다.」** 가 나옵니다.

**A.** **Fixed (`9aafa3e`·`ff12473`, G21)** — 동일 이용자·방문일·일정 종류(`PLAN`/`BILLING`)·시간대에 **취소되지 않은** 방문일정이 이미 있으면 **재import·수기 등록·수정** 모두 차단됩니다.

| 항목 | 내용 |
|------|------|
| 중복 기준 | `clientId` + `visitDate` + `scheduleKind` + `plannedStartTime`/`plannedEndTime` |
| **NHIS import** | 행 **`SKIPPED`** + `reason` 「동일한 방문일정이 이미 등록되어 있어 import를 건너뜁니다.」 (`9aafa3e`) |
| **수기 등록·수정** | **`422 BUSINESS_RULE`** — 「동일한 방문일정이 이미 등록되어 있습니다.」 (`ff12473`) |
| 제외 | **`CANCELLED`** 상태 일정은 중복 판정에서 제외 — 취소 후 재등록·재import 가능 |
| UI | **`VisitNhisImportPanel`** 결과 표 **「건너뜀」** Badge + **사유** 열 · **`VisitsPage`** 등록 폼 **Alert** |
| 조치 | ① 기존 일정 확인 ② 불필요하면 **취소** 후 재시도 ③ 공단 엑셀 **중복 행** 제거 |

> 관련: Q189 · Q195 · Q200 · Q259 · USER_MANUAL §5-11 · ADMIN_GUIDE §10-12

### Q235. **퇴소 이용자** 또는 **이동서비스 미사용** 이용자에게 이동서비스 계약서를 저장할 수 없나요?

**A.** **Fixed (`24733c7`, V65, G15)** — **아니요.** 앱(`TransportContractService`)과 DB 트리거(`trg_transport_service_contracts_guard_client`)가 **이중으로** 차단합니다.

| 조건 | 거부 사유 |
|------|----------|
| `usesTransport=false` | 이동서비스 미사용 이용자 |
| `discharged_at` 존재 또는 `is_active=false` | 퇴소·비활성 이용자 |
| 계약 `branch_id` ≠ 이용자 `branch_id` | 지점 불일치(저장 시 **자동 resync**) |
| 서명일만 있고 서명자 이름 없음 | V65 CHECK — 보호자·기관 **서명 쌍** 필수 |

| 스키마 | **V65** — actor backstop · client guard trigger · dual-signature CHECK · purge 인덱스 |
| UI | **`TransportCompliancePanel`** — 위 조건 미충족 시 저장 **`422`** · 필드 오류 표시 |
| 보존 | 퇴소 후 **5년** — `idx_transport_service_contracts_client_purge`(DATA_RETENTION_POLICY §3) |

> 관련: Q230 · Q231 · USER_MANUAL §5-8 · ADMIN_GUIDE §10-10 · DEPLOYMENT §8-1 V65

### Q236. **이동서비스일지(별지 제22호)** 는 어디서 출력하나요?

**A.** **✅ full stack (`0cfa970`·`aaaeb10`·`aa42b9c`·`088e906`·`dff2f32`, G15 v1.3-C, US-T05, Q407·Q411)** — **확정 배차** 루트 상세에서 법정 형식 일지를 **서버 저장·감사 추적·보관 안내·인쇄·텍스트 다운로드**할 수 있습니다.

| 항목 | 내용 |
|------|------|
| UI | **`/transport/runs/:runId`** **`TransportServiceLogPanel`** — `run.status=CONFIRMED` 권장 |
| 조회 API | **`GET /api/v1/transport/runs/{runId}/service-log`** — 차량번호·운전자·정차별 행·**`summary`** (recorded/onTime/total) |
| 저장 API | **`PUT /api/v1/transport/runs/{runId}/service-log`** — **CONFIRMED only** · 동승 직원·정차별 **실제 픽업**·**동승 여부**·**하차 시각** |
| 감사 | 저장 성공 시 **`TRANSPORT_SERVICE_LOG_UPSERT`** — **`/settings` → 감사 로그** (`aa42b9c`, Q411) |
| 보관 UX | **「일지 보관·감사 추적」** — 확정 시각·DB 저장 건수·마지막 저장·저장 상태 · **법정 보관 안내** (`088e906`) |
| 입력 | **동승 직원**(`companionName`) · 정차별 **실제 픽업** · **동승 여부** · **하차 시각** — **차량번호·운전자**는 API **읽기 전용** · 정차별 **Field 라벨**(QA-B116) |
| 시간 준수 | **`StatusBadge`** + **`TransportTimeCompliance`** — 계획 픽업 대비 **±15분** 이내 **「준수」** · 초과 **「지연」** · 미입력 **「미기록」** (색상만 의존 제거) |
| 출력 | **「일지 기록 저장」** — 서버 영속화 (**V148**) · **미저장·일부 미기록 시 인쇄·텍스트 저장 차단** · 저장 후 **「인쇄」**·**「텍스트 저장」** |
| DRAFT | 미확정 루트는 **미리보기**만 — **저장 버튼 없음** · **「배차 확정 후 제출용 일지로 출력」** 경고 |
| 권한 | **`hq_admin`·`branch_admin`·`social_worker`·`caregiver`** — 조회·저장 동일 |
| 연동 | 상단 안내에서 **`/transport/compliance`** **별지 제18호** 패널(Q237) 교차 참조 |

> 관련: Q230 · Q233 · Q237 · Q407 · Q411 · USER_MANUAL §5-8 · ADMIN_GUIDE §10-10

### Q237. **별지 제18호 이동서비스비** 신청은 ogada에서 하나요?

**A.** **Fixed (`eecf0be`·`ba020d4`·`9dfef92`·`fcf713a`, G15 v1.3-C + G16 partial, US-T05)** — **아니요.** ogada는 **공단 포털 선행 절차 안내**와 **G16 청구 기록 생성**만 제공합니다. 실제 신청·승인은 **장기요양보험 공단 포털**에서 수행합니다.

| 항목 | 내용 |
|------|------|
| UI | **`/transport`** · **`/transport/service-fees`** **`TransportForm18GuidePanel`** — **「이동서비스비 신청 안내 (별지 제18·19·20호 · G15)」** |
| 5단계 | ① 수칙·계약 → ② **제22호 일지** → ③ **공단 포털 제18호** → ④ **제19호 변경·중단 / 제20호 통보** → ⑤ **월간 대조·G16 청구 생성**(Q239) |
| **3분리 신청 유형** (`fcf713a`) | **적용신청**(제18호) · **변경신청**(제19호, 7일 이내) · **중단신청**(제19호 → 공단 **제20호** 통보) — `transportForm18.js` 표 |
| **등록상태 4단** (`fcf713a`) | **작성중** → **진행중** → **적용**(월간 청구 반영 가능) / **적용불가**(재신청 필요) |
| 전제 | `usesTransport`·픽업 주소 · 배차 확정 후 일지 · **수급자별 1일 1회** · 차량·동승·시간 준수 |
| 범위 | **공단 API 직접 전송** — **미지원** · ogada **청구 기록 generate·confirm** — **Fixed**(Q239) |

> 관련: Q230 · Q236 · Q247 · USER_MANUAL §5-8 · REQUIREMENTS §3-13 G16

### Q247. 다지점에서 **다른 지점** 이동서비스비 기록을 수정할 수 있나요?

**A.** **Fixed (`b5218a9`, G16, US-T05)** — **아니요.** `PATCH /api/v1/transport/service-fees/{recordId}` 는 JWT **`activeBranchId`** 와 기록의 **`branchId`** 가 일치할 때만 허용됩니다.

| 상황 | 동작 |
|------|------|
| `hq_admin`이 **BranchSwitcher**로 A지점 선택 후 A지점 기록 수정 | ✅ 허용 |
| A지점 선택 상태에서 **B지점** 기록 수정 시도 | ❌ **`403 FORBIDDEN_SCOPE`** — `다른 지점의 이동서비스비 기록은 수정할 수 없습니다.` |
| 조회(`GET /transport/service-fees`) | 지점 스코프 내 목록만 반환 — **수정은 활성 지점만** |

> **운영 팁**: 다지점 통합 관리자는 수정 전 **BranchSwitcher**로 작업 지점을 맞춘 뒤 `/transport/service-fees`를 새로고침하세요 (Q11·Q173).
>
> 관련: Q239 · Q241 · USER_MANUAL §5-8-1 · ADMIN_GUIDE §10-10

### Q238. 방문일정 **체크인·체크아웃** 시 **페어(계획↔청구)** 일정도 같이 갱신되나요?

**A.** **Fixed (`9d7c17f`·`6bfc745`·`45b8147`·`209f05d`·`b7cfc92`·`728339e`·`82bdbcd`, G21, US-V02)** — **예.** PLAN/BILLING **이중 일정**이 연결(`pairedScheduleId`)되어 있으면, 한쪽에서 **체크인·체크아웃**이 진행될 때 **페어 일정의 상태·시각**도 동기화됩니다. **페어 연결이 깨졌거나 상태가 어긋나면 한쪽만 진행되지 않습니다.**

| 항목 | 내용 |
|------|------|
| API | `POST /api/v1/visits/{id}/check-in` · `POST …/check-out` · **확정·취소** 전환도 동일 가드 (`209f05d`·`b7cfc92`) |
| 동기화 | 페어가 **허용 전이**에 해당할 때만 — **`CONFIRMED`→`IN_PROGRESS`(체크인)** · **`IN_PROGRESS`→`COMPLETED`(체크아웃)** (`6bfc745`) |
| 거부 | 페어 일정 **없음** → **`422`** 「연결된 계획/청구 일정을 찾을 수 없습니다.」 · 페어 **상태 불일치** → **`422`** 「연결된 계획/청구 일정 상태가 맞지 않아…」 (`45b8147`) · **연결 무결성 위반** → **`422`** (`209f05d`) · **확정 시 페어 DRAFT/CONFIRMED 외 상태** → **`422`** (`b7cfc92`) · **레거시 슬롯 불일치**(`pairedScheduleId` null) → **`422`** (`728339e`, Q289) |
| DRAFT 수정 | **필드 동기화**는 `DRAFT` 페어만 (Q199) — **`syncPairedDraftScheduleOnUpdate`** 전 **`isValidPairedScheduleLink`** 검증 (`82bdbcd`) · 깨진 링크 시 **`422`** · **확정 후**에는 필드 수정 동기화 **미적용** |
| 취소 | **연쇄 취소**는 별도 규칙 (Q194) — 완료된 페어는 스킵 |
| 목적 | 모바일·수기 체크인 후 **청구 일정이 계획과 어긋나 청구 누락**·**한쪽만 COMPLETED** 되는 것을 방지 |

> 관련: Q194 · Q199 · Q234 · **Q289** · USER_MANUAL §5-11 · ADMIN_GUIDE §10-12

### Q239. **이동서비스비 청구** 화면은 어디에 있나요?

**A.** **Fixed (`88d4c59`·`9dfef92`, G16, BNK-25, US-T05)** — **`/transport/service-fees`** **`TransportServiceFeePage`** 에서 **확정 배차 기반** 청구 기록을 생성·확정합니다.

| 항목 | 내용 |
|------|------|
| 진입 | **`TransportContextNav`** **「이동서비스비 청구」** — SideNav **이동** 그룹에는 **미등록**(배차·외출만) |
| 워크플로 | 기간 선택 → **거리구간 수가**(RU_1 830 ~ RU_4 6,230원) 확인 → **「확정 배차에서 생성」** → DRAFT 행 수정 → **「확정」** |
| 규칙 | **수급자·일자당 1회** (V68 UNIQUE) · **이동서비스 계약 이중 서명** 필수 (Q231) · 편도 = 기본금액 **50%** |
| 스킵 | 동일 일자 기록 존재 · 계약 미서명 — UI **skipped** 목록에 사유 표시 |
| 권한 | **`hq_admin`·`branch_admin`·`social_worker`** — **`caregiver`** API **403** (라우트만 허용) |
| 갭 | **공단 포털 자동 제출 없음** · 거리구간 **자동 산출 미연동**(기본 RU_1) |

> 관련: Q237 · Q241 · USER_MANUAL §5-8-1 · ADMIN_GUIDE §10-10 · DEPLOYMENT §8-1 V68

### Q240. **이용자 외출** 관리는 어떻게 하나요?

**A.** **Fixed (`7dfcc9e`·`a0dcfc0`, G15 2-1-1·2-9, US-T05)** — **외출 예정·출발·복귀·취소** lifecycle과 **월간 리포트**를 지원합니다.

| 항목 | 내용 |
|------|------|
| UI | **`/transport/outings`** **`ClientOutingsPage`** · **`/reports/client-outings`** · 이용자 상세 **「외출」** 탭 **`ClientOutingPanel`** |
| 상태 | `PLANNED` → **출발** → `OUT` → **복귀** → `RETURNED` · **취소** — `PLANNED`/`OUT`에서만 |
| 수정 | **`PLANNED`만** PATCH 가능 · 복귀 후·취소 후 수정 **불가** |
| 리포트 | `GET /reports/client-outings?yearMonth=` — **`CANCELLED` 제외** · **인쇄** only · **`caregiver` 403** |
| 스키마 | **V67** `client_outings` |

> 관련: USER_MANUAL §5-8-2 · ADMIN_GUIDE §10-10 · DEPLOYMENT §8-1 V67

### Q241. **차량 마스터**는 화면에서 등록할 수 있나요?

**A.** **Fixed (BE `bd375e6`·FE `107bfb3`·`08dbcf0`, G16, 케어포 2-4)** — **`VehiclesPage`**(`/transport/vehicles`)에서 지점 차량을 등록·수정합니다.

| 메서드 | 경로 | 권한 |
|--------|------|------|
| GET | `/api/v1/transport/vehicles` | 직원 4역할 (목록·조회) |
| POST | `/api/v1/transport/vehicles` | `hq_admin`·`branch_admin` |
| PATCH | `/api/v1/transport/vehicles/{vehicleId}` | 동일 |

| 화면 | 내용 |
|------|------|
| **`VehiclesPage`** | 차량번호·정원(1–15)·별칭·활성 토글 · **`BranchScopeNotice`** · **`TransportContextNav`** |
| **배차 연동** | **`TransportVehicleSelect`** — **`TransportRunNewPage`·`TransportRunDetailPage`** — `vehicleId` 선택 · 정차 수 > capacity 시 경고 |
| **급여제공 연계** | 확정 배차 + `vehicleId` → **「급여제공」** 탭 일별 **차량번호** 표시 (Q243) |

| 규칙 | 내용 |
|------|------|
| 필드 | `plateNumber` · `capacity`(1–15) · `label`(선택) · `active` |
| UK | Tenant 내 **차량번호 중복 불가** — 중복 시 **422** |
| 스키마 | **V69** `vehicles` · `transport_runs.vehicle_id` FK |
| 일지 | **`TransportServiceLogPanel`** — **운전자·동승** 등은 여전히 **자유 입력** — 차량번호는 배차 **`vehicleId`** 연계 권장 |

> 관련: Q243 · USER_MANUAL §5-8·§5-8-3 · ADMIN_GUIDE §10-10 · DEPLOYMENT §8-1 V69

### Q242. 출석 화면 **상단 탭**(현황·탑승·QR 등)은 무엇인가요?

**A.** **Fixed (`420b4d7`, UXD-73, US-E01~E06)** — **`AttendanceContextNav`** in-page **서브 네비**입니다.

| 항목 | 내용 |
|------|------|
| 위치 | **`AttendancePage`** · **`AttendanceStatsPage`** · **`QrGeneratePage`** 상단 |
| 링크 | 출석 현황 · 탑승(차량) · 현장 출석 · 수기 체크인 · 출석 통계 · QR 생성 |
| a11y | `aria-current="page"` — 현재 탭 표시 · **`AttendanceContextNav.test`** 2건 |
| SideNav | **출석** 그룹 6항목과 **동일 경로** — context nav는 **페이지 내 빠른 전환**용 |

> 관련: Q232 · USER_MANUAL §3-2·§4-4 · CHANGELOG TWR 81차

### Q243. 이용자 상세 **「급여제공」** 탭은 무엇인가요?

**A.** **Fixed (BE `8bdead6` + FE `08dbcf0`, G15 v1.3-C, 케어포 3-1)** — 월간 **출석·이동서비스 제공·차량번호**를 한 화면에서 대조합니다.

| 항목 | 내용 |
|------|------|
| 위치 | **`/clients/:id` → 「급여제공」** — **`CareProvisionRecordPanel`** |
| API | **`GET /api/v1/clients/{clientId}/care-provision-records/{yearMonth}`** |
| 권한 | **`branch_admin`·`social_worker`·`caregiver`** — 지점 스코프 (`hq_admin` **미포함**) |
| 요약 | 출석 일수 · 이동서비스 제공 일수 · **주 사용 차량**(가장 많이 배정된 번호판) |
| 일별 표 | 일자 · 출석 여부 · 이동서비스 제공 · **차량번호** — **확정(`CONFIRMED`) 배차** + **`vehicles`** 마스터 조인 |
| 전제 | 이용자 **`usesTransport=true`** · 해당 일 **확정 배차**에 정차 포함 · 배차에 **`vehicleId`** 지정(Q241) |
| 이메일 연계 | 발송 API 본문에 **`transportServiceProvided`·`vehiclePlateNumber`** 자동 포함 (Q216) |

> **발송 버튼 UI 없음** — 보호자 이메일 발송은 Swagger (Q216).

> 관련: Q216 · Q241 · USER_MANUAL §3-3 · ADMIN_GUIDE §10-10

### Q244. 청구 상태를 **`PAID`로 직접 변경**하면 **`paidAt`** 이 기록되나요?

**A.** **Fixed (BE `e16534c`·`64ebf6e`, G2, QA-B23)** — **`PATCH /billing/claims/{id}`** 또는 **`updateClaimStatus`** 로 **`CONFIRMED`→`PAID`** 전환 시, **`paidAt`이 비어 있으면** **전환 시각(KST)** 과 **`paymentRecordedBy`(JWT actor)** 가 자동 저장됩니다. **`paymentMethod`가 없으면 `PAID` 전환 자체가 거부**됩니다 (Q249).

| 경로 | 동작 |
|------|------|
| **`POST /billing/claims/{id}/payments`** | **`paidAt`·`paymentMethod` 요청 본문 필수** — `paidAt` null → **`422`** `입금일을 입력해주세요.` (`4001510`, Q250) |
| **`updateClaimStatus` → `PAID`** | **`paymentMethod` 미기록** → **`422`** — `수납완료 처리 전 입금 수단을 먼저 기록하세요.` · **`paidAt` NULL** 이면 **now** + actor (status-only PATCH, Q244) |
| **납부확인서 UI** | **「납부확인서 발송」** — **`paidAt` + `paymentMethod` NOT NULL** 필요 (Q221) |

> **CMS 출금**·**은행 일괄입금** 등 다른 `PAID` 경로도 동일 규칙을 따릅니다. 이미 `paidAt`이 있으면 **덮어쓰지 않습니다**.

> 관련: Q174 · Q221 · Q250 · USER_MANUAL §4-6 · ADMIN_GUIDE §10-6

### Q245. 필수 입력란에 `*` 표시만 있고 스크린리더가 「필수」라고 안내하지 않아요.

**A.** **Fixed (FE `1f71335`)** — 공통 **`Field`** 컴포넌트가 **`required` prop** 시 자식 입력에 **`aria-required="true"`** 를 전달합니다 (WCAG 1.3.1·3.3.2).

| 항목 | 내용 |
|------|------|
| 범위 | **전 폼 일괄 적용** — 이용자 등록·출석·청구·배차·NHIS import 등 **`Field` 사용 화면** |
| 시각 표시 | 라벨 옆 `*` — **`aria-hidden="true"`** (중복 낭독 방지) |
| 네이티브 `required` | **사용하지 않음** — 브라우저 기본 검증 대신 **`aria-required` + 서버 `fieldErrors`** 패턴 유지 |
| 테스트 | **`Field.test.jsx`** — `TextInput`·`Select`·`TextArea` **`aria-required`** 회귀 7건 |

> 관련: Q115 · USER_MANUAL §3-2

### Q246. Flyway V70은 무엇을 보호하나요?

**A.** **Fixed (BE `ba4c9d9`, G15/G16 v1.3-C)** — **V70**은 v1.3-C **외출·이동서비스비·차량·배차** 데이터의 **Tenant·지점·활성 이용자** 정합을 DB 트리거로 강제합니다.

| 대상 | V70 보호 |
|------|----------|
| **`client_outings`** | Tenant·지점 자동 설정 · **퇴소·비활성 이용자 INSERT 차단** · actor backstop · purge 인덱스 |
| **`transport_service_fee_records`** | **`uses_transport`/활성/지점 일치** guard · purge 인덱스 |
| **`vehicles`** | actor backstop |
| **`transport_runs`** | **`vehicleId` ↔ 지점 일치** guard |

앱 **`BusinessRuleException`** 과 **이중 방어** — raw SQL·마이그레이션 실수 시에도 cross-tenant·퇴소 이용자 데이터 오염을 줄입니다.

> 관련: Q240 · Q241 · Q235 · ADMIN_GUIDE §1-4 · DEPLOYMENT §8-1 · DATA_RETENTION_POLICY §3

### Q248. 지점 등록 시 **`HOME_CARE`** 급여종을 써도 방문 일정이 되나요?

**A.** **Fixed (BE `894e246`, G21)** — **`HOME_CARE`는 레거시 별칭**으로, 내부적으로 **`HOME_VISIT`(방문요양)** 로 정규화됩니다. 이지케어·REQUIREMENTS §1-2의 **`HOME_CARE` 코드**와 API **`HOME_VISIT`** 불일치를 흡수합니다.

| 항목 | 내용 |
|------|------|
| 지점 등록 | `POST/PATCH /branches` — **`serviceType`: `HOME_CARE` \| `HOME_VISIT`** 모두 허용 |
| 저장값 | DB·내부 로직에는 **`HOME_VISIT`** 로 정규화 |
| 방문 일정 | **`HOME_CARE` 지점**에서도 **`VisitsPage`**·`POST /visits` **허용** (Q180) |
| 주야간 | `DAY_CARE`·`INTEGRATED_HOME` 지점은 **여전히 거부** (Q180) |
| 테스트 | **`BranchServiceTypeTest`** · **`VisitServiceTest`** · **`mvn test` 508/508** |

> 관련: Q180 · USER_MANUAL §5-3·§5-11 · ADMIN_GUIDE §6-4

### Q249. **`PAID` 처리·납부확인서 발송** 전에 **입금 수단**이 꼭 필요한가요?

**A.** **Fixed (BE `64ebf6e`, G2)** — **예.** 수납 알림 본문에 **`paymentMethod`** 가 포함되므로, **`paymentMethod` 없이 `PAID` 전환·납부확인서 발송**은 거부됩니다.

| API | 규칙 |
|-----|------|
| **`POST /billing/claims/{id}/payments`** | **`paidAt`·`paymentMethod` 필수** — `paidAt` null → `422` `입금일을 입력해주세요.` (`4001510`, Q250) · `CASH` \| `BANK_TRANSFER` \| `CMS` (Q174) |
| **`PATCH`/`updateClaimStatus` → `PAID`** | **`paymentMethod` 미기록** → **`422 BUSINESS_RULE`** — `수납완료 처리 전 입금 수단을 먼저 기록하세요.` |
| **`POST …/payment-receipt-notify`** | **`PAID` + `paidAt` + `paymentMethod`** 모두 필요 (Q221) |

**권장 운영 순서**: **`/billing/payments`** 입금 모달에서 **수납일·수납 수단**을 함께 입력 → 자동 **`BILLING_PAYMENT_RECEIVED`** 발송 (Q174·Q204). 상태만 `PAID`로 바꾸려면 **먼저 입금 API**로 메타를 기록하세요.

> 관련: Q174 · Q221 · Q244 · Q250 · USER_MANUAL §4-6 · ADMIN_GUIDE §10-6

### Q250. 입금 처리 API에서 **입금일(`paidAt`)** 을 비우면 어떻게 되나요?

**A.** **Fixed (BE `4001510`, G2)** — **`POST /billing/claims/{id}/payments`** 요청 본문에 **`paidAt`이 없거나 null** 이면 **`422 BUSINESS_RULE`** — `입금일을 입력해주세요.` — 가 반환됩니다. **`CONFIRMED`→`PAID` 입금 처리**는 **수납일·수납 수단**을 함께 기록하는 경로이므로, UI **`PaymentRecordModal`**에서 **입금일(`DateInput`)** 을 반드시 입력해야 합니다 (Q174).

| 경로 | `paidAt` 규칙 |
|------|------|
| **`POST …/payments`** | **요청 본문 필수** — null → **`422`** (`4001510`, Q250) |
| **`updateClaimStatus` → `PAID`** | **`paidAt` NULL** 이면 **전환 시각(KST) 자동 기록** — status-only PATCH (Q244) |
| **납부확인서 UI** | **`paidAt` + `paymentMethod` NOT NULL** (Q221·Q249) |

> **권장**: **`/billing/payments`** 입금 모달에서 **수납일·수납 수단**을 함께 입력하세요 — CMS·은행 일괄입금도 동일 메타를 기록합니다 (Q174·Q228).

> 관련: Q174 · Q244 · Q249 · USER_MANUAL §4-6

### Q251. 보호자 포털에서 **이용자를 바꿨는데 이전 오류 메시지**가 남아요.

**A.** **Fixed (FE `189a00d`·`62058d3`·`bed612c`, US-J02)** — **`GuardianPortalPage`** 가 연결 이용자·일일 기록·명세 로드를 **요청 순번(`requestSeqRef`)** 으로 관리합니다. 느린 네트워크에서 **이전 요청 응답이 늦게 도착**해도 **최신 선택 이용자 데이터만** 반영됩니다. **이용자 미선택**(연결 0건) 상태로 전환되면 **명세 탭 오류(`billingError`)** 가 **자동 초기화**됩니다 (`189a00d`).

| 증상 | 조치 |
|------|------|
| A 이용자 명세 오류 후 B 이용자 선택 | B 선택 시 **오류 배너 사라짐** Fixed (Q251) |
| 빠르게 이용자 전환 | **늦게 도착한 API 응답 무시** Fixed (Q251) |
| 명세 로드 실패 | **「다시 시도」** 버튼 — 기존과 동일 (Q192) |

> 관련: Q192 · USER_MANUAL §8-2

### Q252. **연말정산 의료비공제**(케어포 7-2-1) 납입 내역은 어디서 보나요?

**A.** **Fixed (BE `7f10449`·FE `7e5c806`, G26 / US-L04)** — **`PAID` 상태**이고 **`paidAt`·`paymentMethod`** 가 기록된 본인부담금만 **귀속 연도(`taxYear`)** 기준으로 집계합니다. 입금일(`paidAt`)의 **연도**가 귀속 연도입니다 (KST).

| 화면 | 경로 | API |
|------|------|-----|
| **직원** — 이용자 상세 **「청구」** 탭 | `/clients/:id` | **`GET /api/v1/clients/{clientId}/medical-expense-deduction?taxYear=`** |
| **보호자** — 포털 **「연말정산」** 탭 | `/guardian` | **`GET /api/v1/guardian/clients/{clientId}/medical-expense-deduction?taxYear=`** |

**UI (`MedicalExpenseDeductionPanel`)**

| 기능 | 설명 |
|------|------|
| **귀속 연도** | 2000년 ~ 올해 — **입력 중 API 미호출** · **「조회」** 제출 시에만 fetch (`13272bc`, Q255) |
| **표** | 청구월 · 본인부담금 · 입금일 · 입금수단 · 합계 |
| **인쇄** | 브라우저 인쇄 (`ds-billing-report-print-zone`) |
| **CSV** | UTF-8 BOM — 연말정산 신고 참고용 |
| **국세청 엑셀** | **Fixed (FE `e2c2ffe`·`fd569d7`, G26 / US-L04, Q258)** — **「국세청 엑셀 다운로드」** — NTS 제출용 `.xlsx` (`ogada-medical-expense-deduction-nts-{이용자}-{연도}.xlsx`) · **공제대상여부**·**CMS/간편결제 제외 비고** 열 포함 |
| **빈 목록** | 해당 연도 **집계 대상 납입 0건** |

| 규칙 | 내용 |
|------|------|
| 집계 대상 | **`PAID`** + **`paidAt` NOT NULL** + **`paymentMethod` NOT NULL** — **`CASH`·`BANK_TRANSFER`만** |
| 제외 | **`CMS`·`EASY_PAY`(간편결제)** — 케어포 7-4·7-5 (`970f547`, Q254) · `DRAFT`·`CONFIRMED` 미수납 · 입금일·수단 누락 청구 |
| 잘못된 연도 | **`422`** `유효한 귀속 연도를 입력해 주세요.` (2000 미만·미래 연도) — **조회 전** FE에서도 동일 메시지 표시 (Q255) |
| 보호자 접근 | **연결 이용자만** — 타 이용자 `403` |

> **선행 조건**: **`/billing/payments`**·**은행 일괄입금**으로 **현금·계좌이체** 수납 시 **입금일·수단**을 기록해야 집계에 포함됩니다 (Q250·Q174). **CMS 자동이체 수납분은 연말정산 의료비공제 대상이 아닙니다** (Q254).

> 관련: Q174 · Q250 · Q254 · Q255 · Q258 · USER_MANUAL §3-3·§4-6·§8-2 · ADMIN_GUIDE §10-6

### Q253. **차량 관리** 화면에서 수정 버튼이 스크린리더에 어떻게 읽히나요?

**A.** **Fixed (FE `04f2f89`, UXD-76 / US-T05)** — **`VehiclesPage`** 목록 각 행의 **수정** 버튼에 **`aria-label="{차량번호} 차량 수정"`** 이 지정되어, 동일 라벨 버튼이 여러 개일 때도 **어느 차량인지** 구분됩니다 (WCAG 2.4.6).

| 이전 | 이후 |
|------|------|
| 모든 행 **「수정」** 동일 | **「12가3456 차량 수정」** 등 차량번호 포함 |

> 관련: USER_MANUAL §5-8-3

### Q254. **CMS·간편결제**로 납부한 본인부담금이 연말정산 의료비공제에 안 나와요.

**A.** **의도된 동작 (BE `970f547`, G26 / US-L04)** — 케어포 **7-4(CMS)·7-5(간편결제)** 와 동일하게, **`paymentMethod`가 `CMS` 또는 `EASY_PAY`인 `PAID` 청구**는 **의료비공제 집계에서 제외**됩니다. **UI 안내 Fixed (FE `c1d9788`, Q254)** — **`MedicalExpenseDeductionPanel`** 상단에 **CMS·간편결제 제외** 문구가 표시됩니다.

| 수단 | 연말정산 의료비공제 집계 |
|------|------------------------|
| **`CASH`** (현금) | ✅ 포함 |
| **`BANK_TRANSFER`** (계좌이체) | ✅ 포함 |
| **`CMS`** (자동이체) | ❌ 제외 |
| **`EASY_PAY`** (간편결제) | ❌ 제외 |

| 확인 방법 | 내용 |
|-----------|------|
| API | `GET …/medical-expense-deduction?taxYear=` — 응답 `items[]`에 CMS 건 **없음** |
| UI | **`MedicalExpenseDeductionPanel`** — 표·합계에 **현금·계좌이체만** 반영 |
| CMS 수납 | **`/billing/cms`** 출금 성공 시 `payment_method=CMS` — Q208 |

> **현장**: 보호자 연말정산 자료는 **현금·계좌이체 입금분**만 CSV·인쇄로 제공하세요. CMS 납부분은 **별도 증빙**(은행·FCMS)을 안내합니다.

> 관련: Q208 · Q252 · USER_MANUAL §4-6·§8-2 · ADMIN_GUIDE §10-6

### Q255. 연말정산 화면에서 **연도를 입력하는 동안** API가 계속 호출돼요.

**A.** **Fixed (FE `13272bc`, G26 / US-L04)** — **`MedicalExpenseDeductionPanel`** 은 **귀속 연도 입력란을 타이핑하는 동안 API를 호출하지 않습니다**. **「조회」** 버튼(폼 submit)을 눌렀을 때만 `GET …/medical-expense-deduction?taxYear=` 가 실행됩니다.

| 상황 | 동작 |
|------|------|
| 연도 숫자 입력 중 | **API 미호출** — 잘못된 연도면 필드 아래 **검증 메시지**만 표시 |
| **「조회」** 클릭 | 유효 연도(2000~올해)일 때만 fetch · **`requestSeqRef`** 로 stale 응답 무시 |
| 이용자·탭 전환 | 마지막 **조회 성공 연도** 기준으로 재로드 |

> 관련: Q252 · USER_MANUAL §3-3·§8-2

### Q256. CMS 출금이 **성공했는데 청구가 PAID가 아니거나**, 금액이 맞지 않는다고 나와요.

**A.** **Fixed (BE `27f20de`·`6bf51c8`·`838a7f6`, G2)** — **`CmsService.requestClaimDebit`** 가 **금액·상태 무결성**을 강제합니다. 불일치 시 **`PAID`로 전환하지 않습니다**.

| 가드 | 내용 |
|------|------|
| **copay ≤ 0** | 「본인부담금이 0원 이하인 청구서는 CMS 출금을 요청할 수 없습니다.」(`27f20de`) |
| **FCMS 실패·금액 불일치** | provider 실패 또는 반환 금액 ≠ 청구 `copayAmount` → `cms_debit_requests` **`FAILED`** · 청구 **CONFIRMED 유지** · **HTTP 200 + `status=FAILED` 응답** — **`422` 예외 아님** (`838a7f6`) · **`failureReason`** 노출 |
| **UI** | **`CmsDebitPanel`** — **출금실패** Badge · **실패 사유** 표시 · 동일 청구 **재요청** 가능 (이력 보존, `c5a6cec`) |
| **SUCCEEDED 재조회** | 기존 성공 이력이 있어도 청구가 **`PAID`·`paymentMethod=CMS`·금액 일치**하지 않으면 **`422`** (`6bf51c8`) |

| 테스트 | `CmsServiceTest` · **`CmsCopayLifecycleE2eTest`** — failed response·amount mismatch·succeeded integrity · **`CmsPilotServiceFlowE2eTest`** (BNK-104) |

> **운영**: FCMS live 연동 시에도 **청구 금액과 출금 응답 금액**이 다르면 수납 처리되지 않습니다. stub 환경에서는 정상 금액으로만 성공합니다.

> 관련: Q208 · Q254 · USER_MANUAL §4-6 · ADMIN_GUIDE §10-13 · DEPLOYMENT §4-6

### Q257. 입금·수납완료 처리 시 **「본인부담금이 설정되지 않아…」** 오류가 나요.

**A.** **Fixed (BE `1af5b1f`·`923e610`, G2 / US-L01)** — 청구 헤더 **`copayAmount`가 NULL**인 경우 **입금 API**와 **상태 `PAID` 전환** 모두 **`422 BUSINESS_RULE`**로 거부됩니다.

| 경로 | 오류 메시지 |
|------|------------|
| **`POST …/payments`** | 「청구서 본인부담금이 설정되지 않아 **입금 처리**할 수 없습니다.」 |
| **`PATCH …/status` → `PAID`** | 「청구서 본인부담금이 설정되지 않아 **수납완료 처리**할 수 없습니다.」 |

| 원인 | 조치 |
|------|------|
| 청구 생성·import 오류로 **본인부담금 미계산** | **수가표·출석·등급** 확인 후 청구 **재생성** |
| 레거시·수동 DB 데이터 | IT 담당과 **`copay_amount` 보정** 후 재시도 |

| 테스트 | **`BillingServiceTest.recordCopayPaymentShouldRejectMissingCopayAmountOnClaim`** · **`updateClaimStatusShouldRejectPaidWhenCopayAmountMissing`** |

> 관련: Q218 · Q250 · USER_MANUAL §4-6 · ADMIN_GUIDE §10-6

### Q258. 연말정산 **국세청 엑셀**·은행 **8종 형식 안내**·**샘플 엑셀**은 어디서 보내요?

**A.** **Fixed (FE `e2c2ffe`·`fd569d7`·`758e590`·`b9845ac`, G26 / US-L04 + US-L01)** — 연말정산 의료비공제와 은행 일괄입금 UI에 **제출·업로드용 안내**가 추가되었습니다.

| 기능 | 화면 | 설명 |
|------|------|------|
| **국세청 엑셀** | **`MedicalExpenseDeductionPanel`** — **「국세청 엑셀 다운로드」** | NTS 제출용 `.xlsx` — 이용자·귀속연도·월별 납입·**공제대상여부(Y/N)** · CMS/간편결제 **비고** 열 (`buildMedicalExpenseDeductionNtsRows`) |
| 파일명 | — | `ogada-medical-expense-deduction-nts-{이용자}-{연도}.xlsx` |
| **8종 은행 형식** | **`BankDepositImportPanel`** — **「지원 은행 8종 엑셀 형식」** `<details>` | KB국민·우리·NH농협·신한·하나·부산·대구·광주 — 케어포 7-2 p.88 컬럼 예시 (`bankDepositFormats.js`) |
| **은행별 샘플** | 동일 `<details>` 표 **「샘플」** 열 | **`downloadBankDepositSampleXlsx`** — 은행별 최소 컬럼 레이아웃 `.xlsx` 다운로드 (`b9845ac`, `bankDepositFixture.js`) |
| E2E | — | **`BankDepositImportPanel.formats.e2e.test`** — 8종 fixture 업로드 parametrized 회귀 |

> **참고**: 국세청 **공식 전자신고 양식 자동 제출**은 **미지원** — ogada는 **납입증명 데이터 export**만 제공합니다 (PLAN_NOTES G26 xlsx P3 잔여).

> 관련: Q227 · Q252 · USER_MANUAL §3-3·§4-6 · ADMIN_GUIDE §10-6·§10-13 · DEPLOYMENT §3-7

### Q260. NHIS import 전 **수가표 25칸** 미등록이면 업로드가 막혀요.

**A.** **Fixed (BE `970c7af`·`8f208e4`·`8bb6583`·FE `c30aaac`·`6ef671b`, US-G04 / BNK-79·BNK-166)** — 공단 엑셀 import **귀속 연도**의 **등급(1~5)×이용시간대(5밴드) = 25칸** 수가표가 **항상** 등록되어야 import가 가능합니다. **추가로**, 해당 지점에 **활성 인지지원등급(`ltcGrade=0`) 이용자**가 있으면 **인지지원 5칸**도 필수입니다 (`8bb6583`, Q311).

| 구분 | 동작 |
|------|------|
| **표준 gate (항상)** | **25/25칸** 미완비 → **`422`** 「{year}년 수가표가 {n}/25칸만…」 |
| **인지지원 gate (조건부)** | 지점에 **활성 `ltcGrade=0` 이용자** 존재 시 **5/5칸** 미완비 → **`422`** 「인지지원등급 수가표가 {n}/5칸만…」 |
| **인지지원 gate (해당 없음)** | 인지지원 이용자 **없음** → 표준 25칸만 검사 (Q311 141차와 동일) |
| **사전 점검 API** | **`GET /billing/fee-schedules/year-coverage?year=`** — `{ registered, expected, complete, cognitiveRegistered, cognitiveExpected, cognitiveComplete, message }` (`8f208e4`·`2efc557`·`8bb6583`) |
| **화면** | **`NHISImportPage`** — **`fetchFeeScheduleYearCoverageApi`** 병렬 로드 · **`FeeScheduleYearGuardBanner`** — **표준 25칸** 미완비 시 **warning** + backend **`message`** 우선 표시 (`57114b8`, Q392) + **「수가표 등록」** 링크 · 인지지원 진행률 **별도 표시** |
| **업로드 차단** | FE — **표준 25칸** 미만 · **API 로딩 중** · **API 오류** 시 **업로드 버튼 비활성** (`fee-schedule-year-coverage-guard-warning`) |
| **서버 import** | **`POST /billing/imports/nhis`** — **`FeeScheduleYearCoverage.requireCompleteYearCoverage`** — 표준 25칸 **`422`** · **인지지원 이용자 있을 때** 인지 5칸 **`422`** (`8bb6583`) |
| **완비 시** | 배너 **숨김** — 청구 확정 잠금(Q209)과 **별도** 검사 |

| 조치 | |
|------|--|
| 1 | **`/billing/fee-schedules`** — **「공단 2026 수가 시드 (N건)」** 또는 셀별 수동 등록 — **표준+인지지원 미등록 셀 모두** (Q214·Q311) |
| 2 | **`year-coverage` API** 또는 배너에서 **25/25** 확인 후 NHIS import 재시도 |

| 테스트 | **`FeeScheduleYearCoverageTest`** · **`BillingServiceTest`** year-coverage · **`NhisImportServiceTest`** · **`FeeScheduleYearGuardBanner.test`** · **`NHISImportPage.test`** |

> 관련: Q111 · Q214 · Q209 · USER_MANUAL §4-6-1 · ADMIN_GUIDE §6-3-1·§10-5 · DEPLOYMENT §3-6

### Q259. 방문 일정 **수기 등록**·**확정** 시 중복·페어 오류가 나요.

**A.** **Fixed (BE `ff12473`·`aacf20b`, G21 / US-V02)** — NHIS import 중복 가드(Q234)를 **수기 create/update·확정**에도 동일 적용합니다.

| 상황 | 동작 |
|------|------|
| **동일 슬롯 재등록·수정** | `POST/PATCH /visits` — **`422`** 「동일한 방문일정이 이미 등록되어 있습니다.」 |
| **PLAN/BILLING 한쪽만 확정** | **Fixed** — **`POST …/confirm`** 시 **페어가 `DRAFT`이면 양쪽 `CONFIRMED`** (`confirmPairedSchedule`) |
| **orphan DRAFT 방지** | 계획만 확정·청구 DRAFT 잔존 → NHIS import·대사 **차단** 가능 — **양쪽 동시 확정**으로 예방 |
| **확정 후** | 페어 **필드 수정 동기화 없음** (Q199) — 취소는 **양쪽 연쇄**(Q194) |

| 테스트 | **`VisitServiceTest`** duplicate slot·paired confirm · **`VisitPilotServiceFlowE2eTest`** |

> 관련: Q194 · Q199 · Q234 · USER_MANUAL §5-11 · ADMIN_GUIDE §10-12

### Q261. 수납 완료된 청구서를 **환불** 처리하려면?

**A.** **Fixed (BE `de49b21`·FE `212e010`, US-M03 7-9 / 케어포 7-9)** — **`PAID`** 상태 청구서만 환불할 수 있습니다. 처리 후 상태는 **`REFUNDED`** 로 전환되며 **환불대장**에 집계됩니다.

| 구분 | 동작 |
|------|------|
| **화면** | **`/billing/claims/:claimId`** — **`BillingDetailPage`** — **`PAID`+`paidAt`** 일 때 **「환불 처리」** → **`RefundRecordModal`** |
| **입력** | **환불일**(`DateInput`) · **환불 금액**(기본=본인부담금 전액, **부분 환불 불가**) · **환불 사유**(선택) |
| **API** | **`POST /billing/claims/{claimId}/refunds`** — `{ refundedAt, amount?, reason? }` |
| **서버 검증** | **`PAID`만 허용** · **`paidAt`·`paymentMethod` 필수** · **환불 금액 = `copayAmount`** · **미래 환불일 거부** · **이미 `REFUNDED` 거부** |
| **DB** | **V71** — `refunded_at`·`refund_amount`·`refund_reason`·`refund_recorded_by` · 상태 전이 **`PAID`→`REFUNDED` only** |
| **연말정산** | **`getMedicalExpenseDeduction`** — 환불된 청구는 **귀속 연도 집계에서 제외** (Q252 연계) |
| **권한** | **`hq_admin`·`branch_admin`** — `social_worker`·`caregiver` **거부** |

| 조치 | |
|------|--|
| 1 | 청구 상세에서 **수납 정보**(`paidAt`·결제수단) 확인 |
| 2 | **「환불 처리」** → 금액·환불일·사유 입력 → 저장 |
| 3 | **환불대장**(`/billing/reports/refunds`)에서 월별 내역 확인 |

| 테스트 | **`BillingServiceTest.recordCopayRefund*`** · **`CopayGuardianNotifyPaymentE2eTest`** · **`BillingDetailPage.test`** · **`RefundRecordModal.test`** |

> 관련: Q179 · Q252 · USER_MANUAL §4-6·§5-10 · ADMIN_GUIDE §10-4 · DEPLOYMENT §8-1

### Q262. **기능회복 훈련** 계획·평가 지표는 어디서 관리하나요?

**A.** **BE·FE Fixed (BE `73e169a`·FE `0821ce8`, G17 / US-T06)** — SideNav **기록 → 기능회복훈련 (G17)** 또는 **`/programs/functional-recovery`** 화면에서 **지표 25–27** 준수 현황·계획 목록·등록을 처리합니다.

| 화면 | 동작 |
|------|------|
| **`FunctionalRecoveryPage`** | 상단 StatCard(지표25·26·27) · 연도별 계획 목록 · **등록 폼**(`hq_admin`·`branch_admin`·`social_worker`) |
| **`RecordsContextNav`** | 건강·식사·프로그램·기능회복훈련·방문·사례관리 6화면 서브 탭 |

| API | 용도 | 권한 |
|-----|------|------|
| `GET /programs/functional-recovery/plans?year=&clientId=` | **연간 기능회복 계획** 목록 | `hq_admin`·`branch_admin`·`social_worker`·`caregiver`(조회) |
| `POST /programs/functional-recovery/plans` | 계획 등록 | `hq_admin`·`branch_admin`·`social_worker` |
| `PATCH /programs/functional-recovery/plans/{planId}` | 계획 수정 | 동일 3역할 — 목록 **「수정」** → 폼 로드 → PATCH (**UI Fixed**, `26499b3`, Q279) |
| `GET /programs/functional-recovery/compliance?year=` | 지표 25–27 충족 요약 | `hq_admin`·`branch_admin`·`social_worker` |

| DB | **V72** — `functional_recovery_plans` · **`activity_programs.program_type`** `FUNCTIONAL_RECOVERY` |

| compliance 매핑 | **`mapFunctionalRecoveryComplianceView`** — API `indicator25MetCount` 등 count 필드 정합 (`0821ce8`) |

| 테스트 | **`FunctionalRecoveryServiceTest`** · **`FunctionalRecoveryPage.test`** · **`mvn test` 576/576** · Vitest **631/631** |

> 관련: USER_MANUAL §5-9 · ADMIN_GUIDE §10-11-1 · REQUIREMENTS G17

### Q263. **사례관리 회의록**(평가 지표 43)은 어디서 등록하나요?

**A.** **BE·FE Fixed (BE `2225a7a`·FE `0821ce8`, G32 / US-T07)** — SideNav **기록 → 사례관리 회의록 (G32)** 또는 **`/case-management/meetings`** 에서 분기별 회의록을 등록·조회합니다. **`caregiver`** 는 SideNav에 메뉴가 없습니다(API 조회만 허용).

| 화면 | 동작 |
|------|------|
| **`CaseManagementPage`** | 지표43 StatCard · 연도·분기 필터 · **7필드 등록 폼**(FE `443f379`, Q265 Fixed) |
| **필수 입력 (FE 7필드)** | 이용자 · 회의일 · 선정사유 · 회의내용 · 회의결과 · **`caseManagementPlan`**(사례관리 계획) · **참석자(쉼표·세미콜론·슬래시 구분, ≥2인)** |
| **지표29 compliance (BE `11277b9`·FE `fa2ad1e`)** | **`evaluationConductedMet`** — 회의 후 30일 내 **기능회복훈련 출석** 또는 **계획 갱신** — **`CaseManagementPage` StatCard Fixed**(Q266) |
| **대시보드 위젯** | **`/dashboard`** — **「사례관리 30일 미반영」** (`0821ce8`, Q263) · **「사례관리 평가 미실시」**·**「사례관리 평가실시」** (`7f2289b`, Q266) — `hq_admin`·`branch_admin`·`social_worker` |

| API | 용도 | 권한 |
|-----|------|------|
| `GET /case-management/meetings?year=&quarter=&clientId=` | 회의록 목록 | `hq_admin`·`branch_admin`·`social_worker`·`caregiver`(조회) |
| `POST /case-management/meetings` | 회의록 등록 | `hq_admin`·`branch_admin`·`social_worker` |
| `PATCH /case-management/meetings/{meetingId}` | 회의록 수정 | 동일 3역할 — 목록 **「수정」** → 폼 로드 → PATCH (**UI Fixed**, `26499b3`, Q279) |
| `GET /case-management/compliance?year=&quarter=` | 지표43·**30일 급여반영** compliance | `hq_admin`·`branch_admin`·`social_worker` |

| 서버 규칙 | 내용 |
|----------|------|
| 분기 UNIQUE | **이용자·연도·분기**당 회의록 1건 — 중복 시 **422** |
| 참석자 | **2인 이상** — FE·BE 모두 검증 · **`,;/\n·` 구분자** 정규화 후 저장 (`7eebd8c`·`2225a7a`, QA-B40) |
| 30일 반영 | compliance — 회의일+30일 이내 **프로그램 참여** 또는 **청구 라인** 변경 1건 이상 · **미반영 건수**는 대시보드 위젯·compliance `items[]` 로 집계 |
| compliance 매핑 | **`mapCaseManagementComplianceView`** — `reflectionGapCount`·`items[]` 정합 (`0821ce8`) |
| DB | **V73** `case_management_meetings` · **V74** integrity · **V75** `case_management_plan` (이지케어 FAQ 21797 7항 패리티) |

| 테스트 | **`CaseManagementServiceTest`** · **`CaseManagementPage.test`** · **`DashboardPage.test`** · **`RoleBasedControllerAccessTest$CaseManagementAccess`** |

> 관련: USER_MANUAL §4-2·§5-9 · ADMIN_GUIDE §10-11-2 · REQUIREMENTS G32 · DATA_RETENTION_POLICY §2

### Q264. 청구 **확정 전** 내부 청구와 NHIS import 금액을 비교하려면?

**A.** **BE·FE Fixed (BE `2225a7a`·FE `18f5173`, BNK-87·BNK-91 P2)** — **`DRAFT`** 청구 상세(`/billing/claims/:id`)의 **「공단 명세 비교」** 카드(`BillingNhisComparisonPanel`)에서 이용자별 **서비스일수·공단부담금·본인부담금**을 최신 NHIS import 배치와 대조합니다.

**화면 절차**

1. **청구·정산**(`/billing`)에서 **작성중(`DRAFT`)** 청구 행을 클릭해 상세로 이동합니다.
2. **「공단 명세 비교 (확정 전)」** 섹션에서 StatCard **일치·불일치·공단 미매칭** 건수를 확인합니다.
3. 이용자별 표에서 ogada 일수·공단 일수·ogada 공단부담·공단 청구액·**ogada 본인부담**·상태 Badge를 대조합니다.
4. 공단 청구액 불일치 시 **「공단 초과」** 또는 **「공단 부족」** Badge가 표시됩니다 (`18f5173`, BNK-91 P2). 스크린리더는 **`ds-sr-only`** 힌트로 일수·금액 불일치를 안내합니다.
5. 불일치가 있으면 패널의 **`/billing/reconciliation`** 링크로 대사 화면 이동 후 §4-6-1에서 보정한 뒤 **확정**합니다.

| API | **`GET /api/v1/billing/claims/{claimId}/nhis-comparison`** (`fetchBillingClaimNhisComparisonApi`) |
| 표시 조건 | **`DRAFT` 청구만** — **`BillingDetailPage`** 가 확정·수납 청구에서는 **패널 자체를 렌더하지 않음**(comparison API 미호출, `18f5173`) |
| 배치 없음 | `nhisBatchPresent=false` — 「NHIS import 배치가 없어…」 안내. 먼저 공단 엑셀 import (§4-6-1) |

| 응답 필드 | 의미 |
|----------|------|
| `nhisBatchPresent` | 해당 청구월 NHIS import 배치 존재 여부 |
| `matchedLineCount` | 일수·공단금액 모두 일치한 라인 수 |
| `discrepancyLineCount` | 불일치 라인 수 |
| `missingNhisLineCount` | NHIS 행이 없는 이용자 수 |
| `items[]` | 이용자별 `internalServiceDays`·`nhisServiceDays`·`internalNhisAmount`·`nhisImportAmount`·**`internalCopayAmount`**·`nhisMatchStatus` |

| 권한 | **`hq_admin`·`branch_admin`** — `social_worker`·`caregiver` **거부** |
| 용도 | 청구 **확정(`CONFIRMED`) 전** 내부 계산과 공단 엑셀 import 결과의 **사전 점검** (케어포 7-1 대사 패리티) |

| 테스트 | **`BillingServiceTest.getClaimNhisComparison*`** · **`BillingNhisComparisonPanel.test`** · **`BillingDetailPage.test`** · **`pilotPageFlows`** · **`RoleBasedControllerAccessTest$BillingAccess`** |

> 관련: USER_MANUAL §4-6 · ADMIN_GUIDE §10-4 · REQUIREMENTS US-M03 · FAQ Q100·Q181

### Q265. 사례관리 회의록 **`caseManagementPlan`**(사례관리 계획) 필드는 어디서 입력하나요?

**A.** **BE·FE Fixed (BE `0a270a2`, V75 · FE `443f379`·`932078b`, BNK-92 P2 / G32)** — 이지케어 FAQ 21797 **7항 패리티**에 맞춰 **`caseManagementPlan`**(사례관리 계획)이 **`meetingResult`**(회의 결과)와 **분리**되었고, 화면에서도 입력·목록 표시가 연동되었습니다.

| 항목 | 내용 |
|------|------|
| API | **`POST/PATCH /api/v1/case-management/meetings`** — **`caseManagementPlan` `@NotBlank` 필수** |
| FE UI | **`CaseManagementPage`** — **「사례관리 계획」** `Textarea` · 목록 **「사례관리 계획」** 열 · 서버 `fieldErrors` 매핑 |
| 응답 정규화 | **`normalizeMeeting`** — `case_management_plan` snake_case 응답도 표시 (`932078b`) |
| DB | **Flyway V75** — `case_management_meetings.case_management_plan` |

> 관련: Q263 · USER_MANUAL §5-9 · ADMIN_GUIDE §10-11-2 · REQUIREMENTS G32

### Q266. 사례관리 **지표29 「평가 실시」**(`evaluationConductedMet`)는 어디서 확인하나요?

**A.** **BE·FE Fixed (BE `11277b9` BNK-92 P1 · FE `fa2ad1e`·`7f2289b` UXD-79 / G32)** — MOHW **지표29** 「회의 결과 30일 이내 급여 반영 **+ 평가 실시**」 compliance를 API·화면 모두에서 확인할 수 있습니다.

| 항목 | 내용 |
|------|------|
| API | **`GET /api/v1/case-management/compliance`** — 항목별 **`evaluationConductedMet`** · 집계 **`evaluationConductedMetCount`** |
| 충족 조건 | 회의일 기준 **30일 이내** — **기능회복훈련 프로그램 출석**(`FUNCTIONAL_RECOVERY` 참여) **또는** **기능회복 계획 갱신** |
| **`CaseManagementPage`** | **「지표29 — 평가 실시」** StatCard — 미충족 시 warning Alert |
| **`/dashboard`** | **「사례관리 평가 미실시」**(gap 건수) · **「사례관리 평가실시」**(충족/미충족) 위젯 — 클릭 시 **`/case-management/meetings`** |
| Solapi 연동 | **`NOTIFICATION_PROVIDER=solapi`** 시 **`KAKAO_TPL_*` placeholder**(내부 코드명 그대로)면 **기동 실패** (`98e40a3`) — 승인된 Solapi 템플릿 ID 필수 |

> 관련: Q262(기능회복훈련) · Q263 · USER_MANUAL §4-2·§5-9 · ADMIN_GUIDE §10-11-2 · DEPLOYMENT §4-3

### [TWR] Q268. 파일럿 테스트 데이터를 화면에서 한 번에 준비할 수 있나요?

**A.** **FE Fixed (`37e6b00`·`c89a82b`, pilot)** — **`hq_admin`·`branch_admin`** 이 **`/organization/settings`**(조직 설정) 하단 **「파일럿 테스트 데이터 (프론트 API)」** 카드에서 차량·이용자·NHIS import·방문일정·청구까지 **프론트 API만**으로 일괄 준비할 수 있습니다.

| 항목 | 내용 |
|------|------|
| 표시 조건 | **`import.meta.env.DEV`**(로컬 개발) **또는** 빌드 시 **`VITE_ENABLE_PILOT_FIXTURE=true`** — **운영 빌드 기본 비노출** (`c89a82b`) |
| 일괄 준비 | **「파일럿 데이터 일괄 준비」** — `runPilotFixtureSetup` — 월(`yearMonth`)·**활성 지점** 필수 |
| 샘플 xlsx | **「NHIS 청구 샘플.xlsx」** · **「방문일정 샘플.xlsx」** — 파일럿 이용자 인정번호와 **일치** |
| 범위 | **DB 직접 조작 없음** — 스테이징·데모·QA용. 프로덕션 Tenant에는 **사용 금지** |

> 관련: DEPLOYMENT §3-7 · USER_MANUAL §4-3 · ADMIN_GUIDE §6-2

### Q267. 통합 관리자(`hq_admin`)도 이용자를 등록할 수 있나요?

**A.** **Fixed (BE `208b37e`)** — **`POST /api/v1/clients`** 가 **`hq_admin`** 에게도 허용됩니다. 다지점 센터에서 **통합 관리자가 직접 이용자를 등록**할 수 있습니다.

| 항목 | 내용 |
|------|------|
| 권한 | **`hq_admin`·`branch_admin`·`social_worker`** — `caregiver`는 **조회만** (Q12) |
| 활성 지점 | **`hq_admin`** 은 **Branch Switcher로 작업 지점을 선택**한 뒤, 요청 본문 `branchId`가 **활성 지점과 일치**해야 합니다 |
| 실패 시 | 활성 지점 미선택 → **403** `활성 지점이 선택되지 않았습니다.` · 다른 지점 → **403** `활성 지점에서만 수정할 수 있습니다.` |
| 화면 | **`ClientFormPage`**(`/clients/new`) — 역할 가드는 프론트 라우트 기준; 저장은 위 RBAC를 따릅니다 |

> 관련: Q12 · Q268 · USER_MANUAL §4-3 · ADMIN_GUIDE §6-2

### Q322. 기관 교육일지(8-7)는 어디서 등록하나요?

**A.** SideNav **운영 → 직원 관리**에서 **「교육일지 (8-7)」** 탭 또는 직접 **`/staff/training-logs`**로 이동합니다 (USER_MANUAL §5-14, G41 BE `6191b91` · FE `45a724a`).

**화면 구성**:
1. **반기·연간 compliance** — StatCard — 노인인권 상·하반기 · 운영규정 · **G41b 3종(BE API)** · 신규 7일
2. **교육 유형 필터** — 5가지 유형 선택
3. **직원별 기록** — 교육일·방법·강사·참석자·내용
4. **+ 교육 등록** — Modal에서 입력 후 저장

**편의 팁**: 신규직원 **운영규정 + 신규직원 교육** 7일 이내 (FAQ21828). 모니터링(`/compliance/monitoring`, Q320·Q324).

> **API** (V104–V107):
> - `GET /api/v1/staff/training-logs/compliance` — G41b `*AnnualMet` · 신규 7일 (BNK-185)
> - `GET /api/v1/staff/training-logs/compliance` — 직원별 연간 이수 현황 집계

### Q323. 5가지 교육 유형은 무엇이고 몇 년에 한 번 하나요?

**A.** 법정 의무 교육 5가지 (공단 지표 기준, Flyway V104–V106):

| 유형 | 코드 | 주기 | 신규직원 | 설명 |
|------|:----:|:---:|:------:|------|
| 노인인권 | ELDERLY_HUMAN_RIGHTS | 반기 1회 | 예 | 학대·방임·차별 예방 · FAQ21807 |
| 운영규정 | OPERATING_REGULATION | 연 1회 | 예 7일내 | 센터 규칙·직무 안내 · FAQ21828 지표11 |
| 재난대응 | DISASTER_RESPONSE | 연 1회 | 예 | 화재·지진·긴급 대처 · 지표10 |
| 소화기안전 | FIRE_SAFETY_EQUIPMENT | 연 1회 | 예 | 소화기·비상구·피난 방법 |
| 직원권익 | STAFF_RIGHTS | 연 1회 | 예 | 고충·근로조건·권리 보호 |

**신규직원 기한**: 입사일 + 7일 이내 `OPERATING_REGULATION` + **신규직원 교육** 플래그. compliance는 **지점 스코프** · **가장 이른 `trained_at`** 기준 (BNK-187). help 문구는 하드코딩 없이 API 기반 (`e14ba10`).

**자동 검증**:
- `/staff/training-logs` StatCard — **BE compliance API** (`disasterResponseAnnualMet` 등, BNK-185)
- `/staff` **입사 처리 compliance** 패널 — 7일 기한 (Q300)
- G41b StatCard — API 우선 · 목록 fallback (`38d24b6`)

### Q324. 기관 교육일지가 모니터링 체크리스트와 어떤 관계가 있나요?

**A.** 모니터링 체크리스트(`/compliance/monitoring`, G30 integrated checklist)는 공단 평가 기준에 따라 센터의 월/반기/연 주기 업무를 자동 집계합니다.

**8가지 모니터링 문항 중 기관 교육 관련** (V104–V106, BNK-184):

| 문항 | 체크 기준 | ogada 화면·API |
|------|:------:|---------|
| 신규직원 운영규정 교육 | 입사 + 7일 이내 · 자동 기한 검증 | /staff/training-logs · StatCard 기한 배지 · GET .../compliance |
| 연간 노인인권 교육 | 반기 1회 이상 · FAQ21807 | /staff/training-logs 유형 필터 · count 자동 집계 |
| 연간 재난·소화기·권익 | 각 연 1회 이상 · 지표10 | /staff/training-logs StatCard 통계 |
| 팀장급 자격 | 실무경력 5년 기준 · FAQ21837 | /staff/lead-caregiver-log 자격 자동 검증 (Q319) |
| 선임 업무수행일지 | 월 작성 · /staff/lead-caregiver-log | 모니터링 checklist 집계 · GET /compliance/monitoring/checklist |
| 관리자 라운딩 | 월 1회 · 수동 입력 | /compliance/monitoring · AdminRoundingCheckPanel |
| 6개월 자가진단 | 직전 6개월 매월 · FAQ21842 | MonitoringSelfDiagnosisChecklistCard |
| 시정 기한 추적 | 3개월 내 | ComplianceIssuePanel · 문제 자동 생성·추적 |

**활용 팁** (USER_MANUAL §5-12~14):
1. 기관 교육 연간 이수율 ≥ 100% 를 `/staff/training-logs` StatCard에서 확인
2. `/compliance/monitoring`의 integrated checklist 에 자동 반영 확인 (GET /api/v1/compliance/monitoring/checklist · BE V101–V106)
3. 신규직원 입사 시 기한 초과 방지 — `/staff` 목록 상단 「입사 처리 compliance 현황」 패널에서 7일 기한 내에 운영규정 교육 등록
4. 월별 모니터링 패널 상단 「기한 초과」 StatCard 확인하여 센터 컴플라이언스 추적

---

### [TWR] Q269. ogada 도입 전 **미납·선납 잔액**(청구시작 기준금액, G33)은 어디서 설정하나요?

**A.** **BE·FE Fixed (BE `3d5eb3e`·`e7df238`·`deaae7a`·`70e6191` · FE `9e1a2ed`·`eba413a`·`7564c2a`·`0ba2b68` / G33·BNK-94~98)** — 케어포 PDF **「7-3.청구시작 금액설정」**에 대응하는 **1회성 온보딩 잔액**을 설정합니다. 기존 ERP·엑셀에서 이관할 때 **ogada 사용 시작 이전**의 본인부담금 미수·선납을 반영합니다.

| 항목 | 내용 |
|------|------|
| 화면 | **`/organization/settings`** → **「청구·정산」** 카드 하단 **「청구시작 기준금액 (G33)」** — **`BillingSettingsPanel`** (`9e1a2ed`·`0ba2b68`) |
| 권한 | **설정** — **`hq_admin` only** · **조회** — `GET /settings/billing` (`hq_admin`·`branch_admin`) |
| API | **`POST /api/v1/settings/billing/start-balance`** — `{ "amount": 125000, "effectiveMonth": "2026-04", "memo": "도입 전 미납" }` — **201 Created** |
| 부호 규칙 (서버) | **양수(+)** = 도입 전 **미납** 잔액 · **음수(-)** = 도입 전 **선납** 잔액 |
| 변경 | **1회만** 설정 가능 — **`lockedAt`** 기록 후 **재설정 `422`** · FE는 **`lockedAt`/`amount`/`effectiveMonth` 스냅샷**으로 폼 재노출도 차단 (`0ba2b68`) |
| 청구대장 | **적용 시작월** 조회 시 **`OPENING_BALANCE`** 행이 **맨 위**에 표시 (`e7df238`·`eba413a`) |
| 미납 목록 | **양수 미납**이고 적용월이 **당월 이전**이면 **`/billing/overdue`** 에 **「청구시작 기준금액 (G33)」** 행 표시 — **「안내 발송」** 없음 (`7564c2a`) |
| 정산 | **`POST /settings/billing/start-balance/settle`** — **BE+FE Fixed** (`70e6191`·`359cf0c`, Q270) — **`/organization/settings`** **「미납 정산」** · **`/billing/overdue`** G33 행 **「미납 정산」** |
| DB | **Flyway V76** — `organizations.billing_start_balance_*` · **V77** — post-lock integrity·settlement guard |

> **온보딩 순서**: Tenant 개통 → **`hq_admin`** 로그인 → **조직 설정**에서 G33 기준금액(필요 시) → 청구 생성 기준(Q224) → 이용자·출석 운영 시작.

> **UI 표시 주의**: **`formatBillingStartBalanceAmount`** 라벨이 서버 부호와 **반대**로 붙을 수 있습니다(양수=미납인데 「선납」). **금액 부호·미납 목록·청구대장**을 기준으로 판단하세요 (Q270).

> 관련: Q224 · Q270 · Q179 · Q197 · USER_MANUAL §5-5-1 · ADMIN_GUIDE §6-3 · DEPLOYMENT §8-1

### [TWR] Q270. G33 **도입 전 미납**은 어떻게 정산하나요? 청구 생성이 막힐 때는?

**A.** **BE+FE Fixed (BE `70e6191`·`42bc06e` · FE `359cf0c` / G33·BNK-94~99)** — 1회 설정한 **양수(미납) 잔액**에 대해 **입금 반영**으로 잔액을 줄입니다. **선납(음수)** 잔액은 정산 대상이 **아닙니다**.

| 항목 | 내용 |
|------|------|
| API | **`POST /api/v1/settings/billing/start-balance/settle`** |
| 권한 | **`hq_admin`·`branch_admin`** |
| 본문 | `{ "paidAt": "2026-06-10", "paymentMethod": "BANK_TRANSFER", "amount": 50000 }` — **`amount` 생략 시 잔액 전액** |
| 수단 | **`CASH`** · **`BANK_TRANSFER`** · **`CMS`** (API) · **화면 UI**는 **현금·계좌이체만** (`359cf0c`) |
| 성공 응답 | **`settledAmount`**(이번 입금) · **`remainingAmount`**(잔여 미납) · **`billingStartBalance`**(갱신된 G33 스냅샷) |
| 거부 (`422`) | G33 **미설정** · **미납 잔액 없음**(0 이하) · **입금일 미래** · **원 단위 아님** · **과납** · **수단 누락/미지원** |
| DB | **V77** — 잠금 후 **설정 필드 immutable** · **양수 미납만 감소** 허용(trigger backstop) |
| 화면 | **`/organization/settings`** → **「청구·정산」** — 미납 잔액 요약 옆 **「미납 정산」** → **`BillingStartBalanceSettlementModal`** · **`/billing/overdue`** G33 행 **「미납 정산」** (USER_MANUAL §5-5-1) |

**청구 생성 가드 (`GET /billing/claims/generation-guard`, Q225 확장)**

| 조건 | `blocked` |
|------|-----------|
| 전월 **`CONFIRMED`** 미입금 청구 존재 | **true** (기존) |
| G33 **양수 미납** — **`effectiveMonth` ≤ 대상 청구월**(`YearMonth` 비교, BE `21eb0af`) | **true** (`70e6191`·`21eb0af`) |
| 둘 다 해당 | 병합 안내 — 「전월 미입금 N건 + 청구시작 기준금액 미정산」 |

정산 후 **`remainingAmount=0`** 이면 미납 목록·청구 생성 가드에서 G33 미납 조건이 해소됩니다.

> 관련: Q269 · Q225 · Q227 · USER_MANUAL §5-5-1 · ADMIN_GUIDE §6-3 · DEPLOYMENT §3-6

### [TWR] Q271. 기능회복훈련 **지표27**(제공·기록·급여시작 전 계획)은 어디서 확인하나요?

**A.** **BE+FE Fixed (BE `0048105`·`e820b28` · FE `21b1855`·`7450161` / G17·BNK-100~102)** — silverangel **평가 지표27** 3행(개인별 계획·제공·기록·급여시작 전 수립)을 compliance API·화면·대시보드에서 확인합니다.

| 항목 | 내용 |
|------|------|
| 화면 | **`/programs/functional-recovery`** — **`FunctionalRecoveryPage`** StatCard 5종 (지표25–27 + **제공·기록** + **지표27 — 급여제공 시작일까지 기능회복훈련 계획 수립** verbatim, BNK-102) |
| 대시보드 | **`/dashboard`** — **「급여제공 시작일까지 계획 미충족」**·**「급여제공 시작일까지 계획」** gap·상태 위젯 (`7450161`) |
| API | **`GET /api/v1/programs/functional-recovery/compliance?year=`** — **`provisionRecordedMet`** · **`planEstablishedBeforeBenefitStartMet`** (이용자별·집계 count) |
| 지표27 row 2 | **`provisionRecordedMet`** — 해당 연도 **기능회복훈련 출석·기록** 존재 |
| 지표27 row 3 | **`planEstablishedBeforeBenefitStartMet`** — 계획 **`createdAt` < `ltcCertValidFrom`** (급여제공 시작일 이전 수립) |
| 등록 가드 | **BE** — **`POST …/plans`** — **오늘 ≥ 급여제공 시작일**이면 **`422`** (`e820b28`) · **FE** — **`isFunctionalRecoveryPlanCreateBlocked`** 로 폼 **사전 비활성**·안내 (`7450161`) |
| 권한 | 조회 — **`caregiver`** 포함 · 등록 — **`hq_admin`·`branch_admin`·`social_worker`** |

> **선행 데이터**: **`ltcCertValidFrom`**(급여인정 유효 시작일)은 이용자 등록·등급 이력에서 설정되어야 row 3·등록 가드가 동작합니다.

> 관련: Q262 · Q266 · USER_MANUAL §4-2·§5-9 · ADMIN_GUIDE §10-11-1 · DEPLOYMENT §3-6

### [TWR] Q272. 보호자 알림이 **여러 보호자에게 중복** 발송되나요?

**A.** **Fixed (BE `555a19f`, J03)** — **`NotificationService.dispatchClientEvent`** 는 연결 보호자 중 **수신 가능한 1명만** 선택해 발송합니다.

| 정책 | 내용 |
|------|------|
| 우선순위 | **대표 보호자(`is_primary`)** — 해당 이벤트 preference·채널(이메일 또는 카카오/SMS+consent)이 활성이면 **대표만** 수신 |
| fallback | 대표가 수신 불가(채널 off·consent 없음)이면 **첫 번째 수신 가능한 부 보호자** 1명에게만 발송 |
| 중복 방지 | 동일 이벤트에 **연결된 모든 보호자에게 일괄 발송하지 않음** — 청구 알림 dedupe(Q219)와 별도 **수신자 1명** 정책 |
| 정렬 | `findByOrganizationIdAndClientIdOrderByPrimaryGuardianDescCreatedAtAsc` — 대표 우선 조회 |

| 테스트 | **`NotificationServiceTest`** — primary 우선·secondary fallback·multi-guardian 미중복 (+91 @Test) |

> **수동 발송**(`POST …/notify`·서류 발송)은 별도 API이며, 자동 이벤트(출석·DAILY_CARE·청구·수납)에만 적용됩니다.

> 관련: Q67 · Q147 · Q219 · ADMIN_GUIDE §10-8 · USER_MANUAL §4-7

### [TWR] Q273. G33 **1회 설정 안내**·**청구대장 하위 메뉴**·정산 후 화면이 안 바뀌어요.

**A.** **Fixed (FE `63361c0`·`eb48879`, UXD-81 / US-L05·US-M03)** — 조직 설정·대장·정산 UX가 보강되었습니다.

| 기능 | 화면 | 설명 |
|------|------|------|
| **1회 설정 경고** | **`BillingSettingsPanel`** — **`BillingStartBalanceOneTimeWarning`** | G33 입력 **전** warning Alert — 「1회만 설정 가능」·케어포 7-3 안내 (`role=status`) |
| **잠금 안내** | 동일 패널 — **`BillingStartBalanceLockedNotice`** | 설정 완료 후 info Alert — 금액·적용월 **변경 불가**·**미납 정산**만 가능 |
| **대장 컨텍스트 nav** | **`BillingReportsContextNav`** | 청구·입금·수납·환불·간편계산기 5화면 **in-page sub-nav** — SideNav 재진입 없이 전환 (`aria-label`) |
| **NHIS 비교 링크** | **`BillingNhisComparisonPanel`** | 불일치 시 **`/billing/imports/nhis`** 링크 경로 정정 |
| **정산 후 갱신** | **`BillingSettingsPanel`** (`eb48879`) | 정산 응답에 `billingStartBalance`가 없어도 **`fetchBillingSettingsApi` 재조회** — 모달 흐름 중 잔액·잠금 상태 동기화 |

| 테스트 | **`BillingStartBalanceNotice.test`** · **`BillingReportsContextNav.test`** · **`BillingSettingsPanel.test`**(settlement reload) · **`pilotPageFlows`** G32/G33 |

> 관련: Q269 · Q270 · USER_MANUAL §5-5-1·§5-10 · ADMIN_GUIDE §6-3

### [TWR] Q274. 등급 이력 **「인정기간 첨부」**에 PDF를 올릴 수 없어요.

**A.** **Fixed (BE `0325d95`·FE `e026ae9`, G37 / US-M01-g / BNK-105)** — 이용자 상세 **「등급 이력」** 탭의 각 행에 **`GradeHistoryAttachmentPanel`** 이 연동되었습니다.

| 항목 | 내용 |
|------|------|
| 진입 | `/clients/:id` → **「등급 이력」** → 행별 **「인정기간 첨부 (N)」** 펼치기 |
| 허용 형식 | **PDF**(`application/pdf`) · **PNG**(`image/png`) — **최대 10MB** |
| 업로드 | **`branch_admin`·`social_worker`** — **`FileUpload`** 선택 후 **「업로드」** |
| 조회·삭제 | **`hq_admin`·`branch_admin`·`social_worker`·`caregiver`** — 목록·**「미리보기」** · 삭제는 업로드 권한 역할만 |
| API | `POST …/ltc-grade-history/{historyId}/attachments` (`multipart`, field `file`) · `GET` 목록/다운로드 · `DELETE` |
| 저장 | 서버 로컬 **`ogada.storage.ltc-grade-attachments.storage-dir`** (기본 `./data/ltc-grade-attachments`) — 운영 시 백업·용량 모니터링 필요 (DEPLOYMENT §4-8) |
| DB | **V78** 첨부 메타 · **V79** cross-client 연결 차단·`uploaded_by` backstop |

| 오류 | 원인·조치 |
|------|----------|
| 업로드 버튼 없음 | **`caregiver`**·**`hq_admin`** 은 **조회만** — **`branch_admin`·`social_worker`** 로 로그인 |
| 「PDF 또는 PNG만…」 | JPEG 등 미지원 — PDF/PNG로 변환. **MIME이 비어 있거나 `application/octet-stream`인 경우에만** 파일명 **`.pdf`/`.png` 확장자**로 허용 (`e9d1178`, Q274). **`text/plain` 등 잘못된 MIME + `.pdf` 확장자**는 **거부** |
| 「10MB 이하여야…」 | 파일 압축 또는 분할 스캔 후 재업로드 |
| `422` / `400` | 등급 이력 `historyId` 불일치·퇴소 이용자 — 페이지 새로고침 후 재시도 |

| 테스트 | **`LtcGradeHistoryAttachmentServiceTest`** · **`GradeHistoryAttachmentPanel.test.jsx`** · **`gradeHistoryAttachments.test.js`** · **`pilotPageFlows`** G37 E2E · **`gradeHistoryAttachmentLiveApi.e2e.test.js`** (BNK-106) |

> **벤치마크**: 이지케어 인정기간별 장기요양이용계획서 첨부 (BNK-105).  
> 관련: Q176 · DATA_RETENTION_POLICY §2-1 · ADMIN_GUIDE §6-2

### [TWR] Q275. Swagger로 방문 일정을 등록할 때 `scheduleKind`를 소문자로 보냈더니 400 오류가 났어요.

**A.** **Fixed (BE `e8de0eb`·`225b104`, G21 / Epic V)** — **`VisitService`** 가 **`scheduleKind`**·**`checkInMethod`** 를 **trim + 대문자**로 정규화합니다. Swagger·연동 스크립트에서 **`plan`/`billing`·`mobile`/`manual`** 소문자·앞뒤 공백을 보내도 **`PLAN`/`BILLING`·`MOBILE`/`MANUAL`** 로 처리됩니다.

| 필드 | 허용 입력 예 | 저장·처리 값 |
|------|-------------|-------------|
| `scheduleKind` | `plan`, ` billing `, `PLAN` | `PLAN` 또는 `BILLING` |
| `checkInMethod` (체크인) | `mobile`, `manual` | `MOBILE` 또는 `MANUAL` |

| 오류 | 원인·조치 |
|------|----------|
| `400 VALIDATION_ERROR` | **`PLAN`/`BILLING`·`MOBILE`/`MANUAL` 이외** 값 — enum 범위 확인 |
| `422 BUSINESS_RULE` | **중복 슬롯**·**HOME_VISIT 지점 아님** 등 업무 규칙 — FAQ Q234·Q180 참고 |

| 테스트 | **`VisitServiceTest`** normalize cases · **`VisitControllerRoutingTest`** · **`VisitPilotServiceFlowE2eTest`**

> 관련: Q180 · Q189 · USER_MANUAL §5-11 · ADMIN_GUIDE §10-12 · API_SPEC §5-8 G21

### [TWR] Q276. **「급여제공결과 평가 (G39)」** 메뉴·대시보드 위젯은 무엇인가요?

**A.** **Fixed (BE `f082933`·FE `1c99bcd`·`8e66ae8`·`4d1a4f2`, G39 / US-T08 / BNK-107·109·234)** — MOHW **평가 지표 44** 대응 **연간 급여제공결과 평가** 화면과 대시보드 compliance 위젯이 연동되었습니다. **172차**에서 **월간 급여제공기록지 보호자 발송 UI**가 추가되었습니다 (Q358).

| 항목 | 내용 |
|------|------|
| 진입 | SideNav **기록 → 급여제공결과 평가 (G39)** — `/programs/provision-result-evaluations` · **`RecordsContextNav`** 서브 탭 |
| StatCard | **지표44 4-pillar** — 주1 상태변화 · 월1 급여제공기록지 · **연1 평가** · **30일 반영** (silverangel verbatim, BNK-107) |
| 등록 | **`hq_admin`·`branch_admin`·`social_worker`** — 이용자·평가일·총평·작성자 · **이용자×연도 1건** |
| **월간 기록지 발송** | **`ProvisionResultDispatchPanel`** — 미제공 이용자 표 · **「기록지 발송」** · **`POST …/notifications/care-provision-record`** (Q358, `4d1a4f2`) |
| 조회 | **`caregiver`** 포함 4역할 — 목록·compliance StatCard **조회만** |
| 대시보드 | **`DashboardPage`** — gap **4종**(**「주간 상태변화 미기록」**·**「월간 기록지 미제공」**·**「급여제공결과 평가 미등록」**·**「평가 30일 미반영」**) + 상태 StatCard **4종** (`8e66ae8`) |
| API | `GET/POST/PATCH /api/v1/provision-result-evaluations*` · `GET …/compliance?year=` · **`POST /clients/{id}/notifications/care-provision-record`** |
| DB | **V80** `provision_result_evaluations` · **V81** integrity |

| 오류 | 원인·조치 |
|------|----------|
| `422` 중복 연도 | 해당 이용자·연도 평가 **이미 존재** — 목록에서 **수정** 사용 |
| compliance 0건 | **활성 지점 미선택** — Branch Switcher 확인 |

| 테스트 | **`ProvisionResultEvaluationServiceTest`** · **`CareProvisionRecordDispatchPilotServiceFlowE2eTest`** (`73df04d`) · **`ProvisionResultEvaluationPage.test.jsx`** · **`ProvisionResultDispatchPanel.test.jsx`** · **`careProvisionRecordDispatchLiveApi.e2e.test.js`** · **`provisionResultCompliance.test.js`** · **`DashboardPage.test.jsx`** · **`programComplianceServices.test.js`**

> 관련: Q271 · Q358 · USER_MANUAL §5-9 · ADMIN_GUIDE §10-11-3 · DATA_RETENTION_POLICY §2-1 G39

### [TWR] Q277. 급여계획서 **5·11개월 통보**·**재발급 첨부 미반영**을 어디서 확인하나요?

**A.** **Fixed (BE `5fd35a6`·`03211e6` + FE `28c22b0`·`4b2b082`, G38 / BNK-106)** — 이지케어 FAQ 21802 대응 **급여계획 통보 모니터링** 화면·대시보드 위젯이 연동되었습니다.

| 항목 | 내용 |
|------|------|
| 화면 | **`/clients/care-plan-notifications`** — SideNav **운영 → 급여계획 통보 (G38)** |
| API | `GET /api/v1/clients/care-plan-notifications/compliance` — 선택 **`?branchId=`** (JWT 스코프 내, BE `03211e6`) |
| 권한 | **`hq_admin`·`branch_admin`·`social_worker`** — `caregiver` **메뉴 미표시** |
| StatCard | **전체 이용자** · **급여 5개월 경과** · **급여 11개월 경과** · **이용계획서 재발급 미반영** |
| 표 | **알림 대상만** / **전체 이용자** 필터 · Badge(`WARNING`/`CRITICAL`) · **「등급 이력」** 링크 → G37 첨부 |
| 대시보드 | **`/dashboard`** — 위 3종 gap 위젯 · compliance API 실패 시 **warning Alert**(다른 위젯은 유지, `4b2b082`) |
| CRITICAL | 최신 등급 이력 행에 **인정기간 첨부(G37) 없음** — 이용자 상세 **「등급 이력」** 탭에서 PDF/PNG 업로드 (Q274) |
| WARNING | 급여시작 **≥5개월** 또는 **≥11개월** — 첨부는 있으나 milestone 안내 |

| 테스트 | **`CarePlanNotificationComplianceServiceTest`** · **`CarePlanNotificationPage.test.jsx`** · **`carePlanNotificationCompliance.test.js`** · **`DashboardPage.test.jsx`** · **`pilotPageFlows`** · **`programComplianceLiveApi.e2e.test.js`**

> 관련: Q274 · USER_MANUAL §4-2·§4-3 · ADMIN_GUIDE §6-2-2

### [TWR] Q278. 방문일정 NHIS import 시 「xlsx 파일 콘텐츠 타입만…」 오류가 나요.

**A.** **Fixed (BE `3c7b247`·`18e2b4c`·`e21c12f`, G21 / Epic V)** — **`VisitService.validateImportFile`** 이 업로드 파일을 **사전 검증**합니다.

| 규칙 | 내용 |
|------|------|
| 확장자 | 파일명 **`.xlsx` 필수** — `.xls`·`.csv`·`.pdf` **거부** |
| Content-Type | 브라우저가 `Content-Type`을 보낸 경우 **`application/vnd.openxmlformats-officedocument.spreadsheetml.sheet`** · **`application/vnd.ms-excel`** · **`application/octet-stream` 허용** — **`text/plain` 등 거부** |
| 파라미터 | `application/vnd…; charset=UTF-8` 등 **세미콜론 뒤 파라미터는 strip** 후 비교 (`e21c12f`) |
| MIME 생략 | 일부 클라이언트가 MIME을 생략하면 **확장자만**으로 진행 |
| 빈 파일 | **「업로드할 엑셀 파일이 필요합니다.」** |

| 조치 | Chrome·Edge에서 공단 포털 **원본 `.xlsx` 다운로드** 후 재업로드 · CSV를 xlsx로 저장한 파일은 **MIME·확장자 모두** 확인 |

| 테스트 | **`VisitServiceTest`** — reject text/plain · allow octet-stream · allow ms-excel · parameterized Content-Type · **`VisitPilotServiceFlowE2eTest`**

> 관련: Q189 · Q275 · USER_MANUAL §5-11 · ADMIN_GUIDE §10-12

### [TWR] Q279. 기능회복훈련·사례관리 회의록을 **수정**하려면?

**A.** **Fixed (FE `26499b3`, G17/G32)** — 이전에는 등록만 가능하고 **`PATCH` API가 UI에서 호출되지 않았습니다**. 현재는 목록 행 **「수정」** 으로 기존 기록을 폼에 불러와 저장합니다.

| 화면 | 수정 절차 | 잠금 필드 |
|------|----------|----------|
| **`FunctionalRecoveryPage`** (`/programs/functional-recovery`) | 목록 **「수정」** → 폼 로드 → **「계획 수정」** 저장 | **이용자·연도** — 변경 불가 |
| **`CaseManagementPage`** (`/case-management/meetings`) | 목록 **「수정」** → 7필드 폼 로드 → **「회의록 수정」** 저장 | **이용자** — 변경 불가 |

| API | 용도 |
|-----|------|
| `PATCH /api/v1/programs/functional-recovery/plans/{planId}` | 기능회복 계획 수정 |
| `PATCH /api/v1/case-management/meetings/{meetingId}` | 사례관리 회의록 수정 |

| 규칙 | 내용 |
|------|------|
| 급여시작 가드 | **신규 등록** 시에만 `isFunctionalRecoveryPlanCreateBlocked` 적용 — **수정 시 생략** (Q271·Q279) |
| 권한 | **`hq_admin`·`branch_admin`·`social_worker`** — **`caregiver`** 는 조회만 |
| 대시보드 집계 | **`GET /dashboard/branch`**·**`/dashboard/hq`** — G17/G32/G38/G39 **준수지표 스냅샷** (BE `7ba18c1`·`70d76a4`, Q280) · NHIS·미납·월한도 스냅샷 (`15b3c7e`, Q282) |

| 테스트 | **`FunctionalRecoveryPage.test`** · **`CaseManagementPage.test`** · **`DashboardServiceTest`**(+163 snapshot) · **`CarePlanProvisionCompliancePilotServiceFlowE2eTest`** (BNK-112, `a9f8bda`)

> 관련: Q262 · Q263 · Q276 · Q280 · USER_MANUAL §5-9 · ADMIN_GUIDE §10-11-1~2

### [TWR] Q280. 대시보드 준수지표 위젯(G17/G32/G38/G39)은 어떤 API로 불러오나요?

**A.** **Fixed (BE `7ba18c1`·`70d76a4`, FE `8fa9f3d`, QA-B49)** — **`GET /api/v1/dashboard/branch`**(지점)·**`GET /api/v1/dashboard/hq`**(통합) 응답에 **준수지표 위젯 count·met 필드가 스냅샷으로 내장**됩니다. **`DashboardPage`** 는 **도메인별** 스냅샷이 있으면 **해당 compliance API만 생략**합니다.

| API | 스냅샷 필드 예시 | 대시보드 위젯 |
|-----|----------------|-------------|
| `GET /dashboard/branch` | **`caseManagementReflectionGapCount`** · **`functionalRecoveryProvisionGapCount`** · **`provisionResultWeeklyStateChangeGapCount`** · **`carePlanFiveMonthWarningCount`** · **`carePlanReissueGapCount`** 등 | 사례관리 30일·평가 · 기능회복 지표27 · 지표44 4-pillar · G38 급여계획 통보 |
| `GET /dashboard/hq` | 지점별 **`branches[]`** + **전 지점 compliance 집계** 동일 필드 | **`hq_admin` 통합 대시보드** — 지점 비교·준수지표 위젯 |

| FE 동작 | 내용 |
|---------|------|
| **도메인별 스냅샷 우선** | `CASE_MANAGEMENT_SNAPSHOT_KEYS` 등 4도메인 — 키 **전부** 존재 시 해당 **`fetch*ComplianceApi` 생략** (`8fa9f3d`) |
| **부분 폴백** | 일부 도메인만 스냅샷 누락 — **누락 도메인만** compliance API **병렬** 호출 (`Promise.all`, `f72da41`, Q280) |
| **전체 폴백** | 구버전 BE — 4 compliance API **병렬 조회** |
| **partial-load** | compliance API만 실패 — **「일부 준수지표를 불러오지 못했습니다: …」** warning · 나머지 위젯 유지 (Q277) |

| 테스트 | **`DashboardServiceTest`**(+163) · **`DashboardPage.test`** — partial snapshot 시 redundant call skip · **`mvn test` 675/675** · Vitest **782건**

> 관련: Q85 · Q277 · Q276 · Q282 · USER_MANUAL §4-2·§5-2 · ADMIN_GUIDE §1-4

### [TWR] Q281. 가산율 미리보기·이동서비스 계약서의 날짜 입력이 다른 화면과 다르게 보여요.

**A.** **Fixed (FE `4903173`, FE-16)** — G11 **`FeeSurchargeGuidePanel`** **「제공일」**·G15 **`TransportCompliancePanel`** **보호자·기관 「서명일」** 이 raw `<input type="date">` 로 남아 **`.ds-date-input` 폭·라벨**이 적용되지 않던 회귀를 **`DateInput`** 으로 통일했습니다.

| 화면 | 필드 | 컴포넌트 |
|------|------|---------|
| **`FeeSchedulePage`** → **`FeeSurchargeGuidePanel`** | **제공일** | **`DateInput`** — **시간** 필드는 `type="time"` 유지 |
| **`TransportPage`** → **`TransportCompliancePanel`** | 보호자·기관 **서명일** | **`DateInput`** — `max=todayIsoDate` · disabled · **`Field` error `aria-invalid`** 보존 |

| 규칙 | 내용 |
|------|------|
| FE-16 | 폼 **`type="date"` raw input 0건** — **`DateInput`/`MonthInput`만** 허용 |
| 접근성 | **`Field` + `DateInput`** — label·id 연결 · 키보드 조작 일관 |

| 테스트 | **`FeeSurchargeGuidePanel.test`** · **`TransportCompliancePanel.test`** — `.ds-date-input`·`type=date` 검증 · Vitest **176파일/773건 PASS**

> 관련: Q201 · Q229 · Q230 · USER_MANUAL §3-2·§5-4·§5-8 · ADMIN_GUIDE §10-4·§10-10

### [TWR] Q282. 대시보드 NHIS·미납·월한도 위젯도 스냅샷 API에 포함되나요?

**A.** **BE Fixed (`15b3c7e`, QA-B49)** — **준수지표(G17/G32/G38/G39)와 별도로** 청구·NHIS·월한도 집계 필드가 대시보드 스냅샷에 추가되었습니다. FE는 아직 **NHIS 배치·미납·월한도 API를 병렬 조회**합니다.

| API | 스냅샷 필드 | 의미 |
|-----|------------|------|
| `GET /dashboard/branch` | **`nhisUnmatchedCount`** · **`pendingReviewCount`** · **`overdueCount`** · **`monthlyCapWarningCount`** | 지점 NHIS 미매칭·대기(보류)·미납 본인부담·**재가급여 월한도 경고** |
| `GET /dashboard/hq` | 동일 4필드 — **전 지점 합산** | 통합 대시보드 NHIS·미납·월한도 위젯 |

| FE 현재 동작 | 내용 |
|-------------|------|
| NHIS | **`fetchNhisImportBatchesApi`** 병렬 — 배치 `unmatchedCount`·`pendingReviewCount` 합산 (Q183) |
| 미납 | **`fetchBillingOverduesApi`** — `totalElements` → **「미납 본인부담」** (Q202) |
| 월한도 | **`fetchMonthlyBenefitCapGuardApi`** — `warningCount` → **「월한도 초과 경고」** (Q226) |
| 폴백 | `dashboardSummary.js` — `extras.* ?? data?.*` 로 스냅샷 필드 **대체 가능** |

| 향후 | BE 스냅샷만으로 NHIS·미납·월한도 fetch **생략** — QA-B49 후속 |

| 테스트 | **`DashboardServiceTest`** — `monthlyCapWarningCount`·HQ NHIS/overdue 집계 assertion · **`mvn test` 667/667**

> 관련: Q85 · Q202 · Q226 · Q280 · USER_MANUAL §4-2·§5-2 · DEPLOYMENT §3-6

### [TWR] Q283. 기능회복훈련·사례관리 **수정(PATCH)** 이 E2E에서 검증되나요?

**A.** **Fixed (BE `0ed781f`·`3ad2a90`, FE `2cd2cd8`, G17/G32)** — 파일럿 E2E가 **등록뿐 아니라 수정 흐름**까지 커버합니다.

| 검증 | 내용 |
|------|------|
| FE **`pilotPageFlows`** | **`FunctionalRecoveryPage`**·**`CaseManagementPage`** — 목록 **「수정」** → 폼 로드 → **`PATCH`** — **이용자·연도(계획)·이용자(회의) 필드 잠금** · 요청 본문 **`clientId` 미전송** |
| BE **`ProgramCompliancePilotServiceFlowE2eTest`** | **`updatePlan`** · **`updateMeeting`** edit-flow |
| BE **`PilotChecklistJwtE2eTest`** | visit **cancel** · case-management **PATCH** JWT routing |

| 테스트 | Vitest **778건** · **`mvn test` 672/672** (116차 baseline) · 117차 BE **675/675**

> 관련: Q279 · Q287 · USER_MANUAL §5-9 · ADMIN_GUIDE §10-11-1~2

### [TWR] Q284. **선임 요양보호사 업무수행일지**(G34)는 ogada에 있나요?

**A.** **Fixed (BE `559648f`·FE `6d6b426`·`8ccd287`·`0ce04ad`, G34·G34b, US-S01)** — **예.** 케어포 **func.php `8-1-2`** 에 대응하는 **`/staff/lead-caregiver-log`** 화면과 **`/api/v1/staff/lead-caregiver-logs*`** API가 **구현**되었습니다.

| 항목 | 내용 |
|------|------|
| UI | **`LeadCaregiverWorkLogPage`** — **`RecordsContextNav`** **「선임 업무수행일지」** · 일별 일지 **등록·수정·전자서명** · **「욕구사정·계획 불러오기」**(G34b, Q303, `0ce04ad`) · StatCard·**`LifecycleWorkflowPanel`** · 목록 **서명자·서명 시각** 열 (`8ccd287`) |
| API | `GET/POST/PATCH /staff/lead-caregiver-logs` · `POST …/{logId}/sign` — 이용자·**일자당 1건** · **DRAFT→SIGNED** 잠금 |
| 서명 | **`DIRECT`**(직접 서명) · **`SMS_VERIFIED`**(문자 인증) — **메타데이터 저장만** (실제 SMS 발송·검증 live **미연동**, Q288) |
| 권한 | **`hq_admin`·`branch_admin`·`social_worker`·`caregiver`** — JWT **활성 지점** 스코프 |
| DB | **Flyway V82** `lead_caregiver_work_logs` |

| P2 잔여 | **보수교육(`8-7-1`)** · **K-MMSE** · **인쇄** · **SMS 실연동** · **FAQ21813 30일 rolling 자동 반영** |

> 관련: Q287 · Q288 · **Q303(G34b)** · USER_MANUAL §5-9 · REQUIREMENTS G34

### [TWR] Q285. **수급자 계약 갱신·해지**(이지케어 FAQ21805)는 ogada에서 하나요?

**A.** **Partial Fixed (BE `6f3315a`·FE `2642838`·`479e064`)** — **급여계약서 파일함은 화면에서 사용할 수 있습니다.** 이지케어 [**FAQ 21805 [비정기] 수급자 계약**](https://ezcare.easyms.co.kr/help/faq.ez?rowid=21805&type=web)에 대응하는 **계약서 PDF/PNG 업로드·미리보기·삭제**는 이용자 상세 **「급여계약」** 탭에서 동작합니다. 다만 **비정기 갱신·해지·전자서명 상태 전이** workflow는 아직 P2입니다.

| 구현됨 (Fixed) | 미구현 (P2) |
|----------------|------------|
| **등급 변동 이력** UI+GET API (G14, US-M01, Q176) | **비정기 계약 갱신/해지** 상태 전이 API |
| **등급 이력 인정기간 첨부** (G37, Q274) | **계약서 전자서명**·갱신 알림 |
| **급여계약서 파일함** — `ClientBenefitContractAttachmentPanel` (US-T10) | FAQ21805 **lifecycle CRUD** 전체 |
| **`LifecycleWorkflowPanel`** — 계약 단계 시각 안내 (Q287) | |

**화면 경로**: 이용자 목록 → 상세(`/clients/:id`) → **「급여계약」** 탭. **`branch_admin`·`social_worker`·`hq_admin`** 이 PDF/PNG(≤10MB)를 업로드할 수 있습니다. **`caregiver`** 는 조회만 가능합니다.

> 관련: Q274 · Q286 · Q287 · API_SPEC.md §9-3 · USER_MANUAL §3-3

### [TWR] Q286. **정기 욕구사정**(이지케어 FAQ21800)은 어디서 하나요?

**A.** **Fixed (BE `6f3315a`·`45fb6d9`·`98002d4`·FE `2642838`·`49fbf67`·`8989bf4`·`ca0b627`·`b5af5fa`·`479e064`)** — **이용자 상세 「기초평가」 탭에서 회계연도별 욕구사정을 작성·저장할 수 있습니다.** 이지케어 FAQ **21800 [연간] 욕구사정**에 대응하는 **8-area 가정방문 평가**는 `ClientNeedsAssessmentForm`에서 **`PUT /clients/{clientId}/needs-assessments`** 로 저장됩니다. **G24b(V128)** 로 **질병·의사소통·영양·환경·자원이용** 5항목이 추가되었습니다 (Q354). **연간 compliance 집계 API**는 BE `98002d4`·**대시보드 StatCard**는 FE `ca0b627`·**전용 현황 화면**은 FE `b5af5fa` (`/clients/needs-assessments`, Q357)에서 제공됩니다. **연간 리포트 일괄 출력**은 P2입니다.

**화면 경로**: 이용자 목록 → 상세(`/clients/:id`) → **「기초평가」** 탭.

**조작 요약**:
1. **가정방문 일자**·**기본 8항목**(신체·인지·가족·경제·사회·서비스 필요·방문 기록·만족도)을 입력합니다.
2. **G24b 5항목**(질병상태·의사소통·영양상태·환경상태·자원이용 욕구)을 입력합니다 (`49fbf67`).
3. **저장** — 동일 회계연도 기록이 있으면 **갱신(upsert)** 됩니다.
4. **이전 회계연도 비교** — 전년도 기록이 있으면 항목별 변화가 표시됩니다 (`ClientNeedsAssessmentCompare`).
5. **회계연도 선택** — FE **`4e4bdf6`·`479e064`** 에서 fiscal-year 파싱이 강화되어, 연도·가정방문 일자·비교 연도가 **일관되게** 매핑됩니다.
6. **가정방문 일자**는 선택한 **회계연도(1/1~12/31) 범위** 밖이면 `422 BUSINESS_RULE` 오류가 반환됩니다 (BE `b238779`).

| 구현됨 (Fixed) | 미구현 (P2) |
|----------------|------------|
| **GET/PUT needs-assessments** API (G24 + **G24b V128**) | FAQ21800 **연간 리포트** 일괄 출력 |
| **GET needs-assessments/compliance** (G24b, Q355) | ~~**지표15** 대시보드 위젯·현황 화면~~ → **대시보드 StatCard ✅** (Q356) · **현황 화면 ✅** (Q357, `b5af5fa`) |
| **G34b 불러오기** — G24b 5항목 포함 (`45fb6d9`) | 전 이용자 **회계연도별 리포트 전수** (P3) |
| **`LifecycleWorkflowPanel`** 단계 안내 (Q287) | |

**권한**: **조회** — `hq_admin`·`branch_admin`·`social_worker`·`caregiver`. **작성·저장** — `branch_admin`·`social_worker`만 (`hq_admin`·`caregiver`는 조회만).

> 관련: Q276 · Q285 · Q287 · USER_MANUAL §3-3 · REQUIREMENTS G24 · API_SPEC.md §9-2

### [TWR] Q287. **LifecycleWorkflowPanel**은 무엇을 보여 주나요?

**A.** **Fixed (FE `c70b908`·`22bd6b7`·`6d6b426`·`c8c727e`, UX/a11y)** — compliance StatCard 아래 **준수지표·업무 단계별 lifecycle** 을 표시하는 **접근성 패널**입니다. **FAQ21805·FAQ21800 본 기능이 아닙니다.**

| 화면 | 패널 제목 | 단계 예시 |
|------|----------|----------|
| **`FunctionalRecoveryPage`** | 기능회복훈련 준수 lifecycle (G17/G32) | 지표25 급여계획 포함 · 지표26 연1회 실시 · 지표27 계획·제공·급여시작 전 수립 |
| **`CaseManagementPage`** | 사례관리 준수 lifecycle (G32) | 지표43 분기 회의 · 참석자 2인 · 30일 급여반영 · 지표29 평가 실시 |
| **`LeadCaregiverWorkLogPage`** | 선임 업무수행일지 lifecycle (G34) | 일지 등록 · 선임 요양보호사 지정 · 업무 기록 · 전자서명 (Q284) |

| UI | **`StatusBadge`**(완료/지연) · 증빙 목록 · **색상만으로 의미 전달 금지** · `<ol>` 단계 목록 |
| 데이터 | **`buildFunctionalRecoveryLifecycleSteps`** · **`buildCaseManagementLifecycleSteps`** · **`buildLeadCaregiverWorkLogLifecycleSteps`** |
| QA-B50 | **`352968b`** — 중복 lifecycle 라벨 제거 |
| QA-B52 | **`c8c727e`** — 증빙 목록 **React key 안정화** |

| 테스트 | **`LifecycleWorkflowPanel.test`** · **`LeadCaregiverWorkLogPage.test`** · Vitest **800건 PASS**

> 관련: Q279 · Q284 · Q285~Q286 · USER_MANUAL §5-9 · ADMIN_GUIDE §1-4

### [TWR] Q288. G34 **문자 인증 서명**(`SMS_VERIFIED`)은 실제로 동작하나요?

**A.** **Partial Fixed (BE `559648f`·FE `6d6b426`·`314b380`)** — **서명 확인 Modal UI는 구현**되었으나, **live SMS OTP 연동은 없습니다.** **`SignLeadCaregiverWorkLogModal`** 에서 서명 방식을 고르고 **「서명 확정」** 을 누르면 API는 **`signatureMethod=SMS_VERIFIED`** 를 **저장**하지만, **실제 문자 발송·인증번호 검증**은 수행하지 않습니다.

| 구현됨 | 미구현 (P2) |
|--------|------------|
| **`SignLeadCaregiverWorkLogModal`** — 서명 전 내용 확인·취소·`aria-busy` (`314b380`) | **Solapi/SMS OTP 발송·검증** workflow |
| **`DIRECT`** 직접 서명 — 로그인 사용자 ID로 **`signedByUserId`** 기록 | **문자 부가과금 안내** · Channel.io **2974fadd** 수준 인증 |
| **`SMS_VERIFIED`** — Modal에서 **「문자 인증 확인」Checkbox** 필수 후 제출 (live OTP 없음) | 실제 SMS 발송·코드 검증 |
| **서명 완료 후 DRAFT 수정 차단** | **K-MMSE** · **인쇄** |

> 관련: Q284 · Q294 · REQUIREMENTS G34 · USER_MANUAL §5-9

### [TWR] Q289. **레거시 방문일정**(`pairedScheduleId` 없음)도 페어 검증을 받나요?

**A.** **Fixed (BE `728339e`, G21)** — **예.** NHIS import 이전 등 **`pairedScheduleId`가 비어 있는 PLAN/BILLING 쌍**도, confirm·check-in/out·cancel 전 **`hasSameVisitSlot`** 으로 **동일 이용자·일자·시간·종류** 일치를 검증합니다. 슬롯이 다르면 **`422 BUSINESS_RULE`** 로 거부됩니다.

| 항목 | 내용 |
|------|------|
| 대상 | `pairedScheduleId` null인 **레거시 이중 일정** |
| 검증 | **`hasSameVisitSlot`** — PLAN/BILLING 슬롯 키 일치 |
| 오류 | 불일치 시 confirm·진행·체크인/아웃 **차단** |
| 목적 | ID 연결 없이 **우연히 매칭된 다른 슬롯**과 페어 동기화되는 것 방지 |

> 관련: Q238 · USER_MANUAL §5-11 · ADMIN_GUIDE §10-12

### [TWR] Q290. **직원 입사~퇴사 lifecycle**(이지케어 FAQ21825)은 ogada에 있나요?

**A.** **Partial Fixed (BE `75440bc`·`bbb8e35`·`d4ee057`·`c976f55`·`cc7da1a`·FE `e7c289e`·`bc3c967`·`e76ca06`·`b3e59e2`·`37dc785` / US-R03·BNK-129·BNK-139·BNK-146, G-Staff-LC)** — **예.** 이지케어 FAQ21825 **4단계** 체크리스트·진행 상태를 **직원 목록·상세 화면**에서 관리할 수 있습니다. **입사/퇴사 서류 PDF·이미지 업로드(FAQ21806)** 는 **`/staff/{userId}` 「HR 파일함」** 탭에서 사용할 수 있습니다(Q298). **`/staff` 목록 상단**에서 **입사 처리 compliance 현황**(FAQ21806 7종 서류·신규교육 7일)을 **지점별 집계**로 확인할 수 있습니다(Q300). **급여명세·G-Payroll 연동·전자서명 workflow**는 P2 잔여입니다.

| 항목 | 화면·API | 비고 |
|------|----------|------|
| 진입 | **`/staff`** 목록 → 이름·**「상세」** → **`/staff/{userId}`** | `hq_admin`·`branch_admin` (Q162) |
| lifecycle 필터 | **`StaffPage`** 상단 **lifecycle 상태 Select** | 입사 진행·재직·퇴사 진행·퇴사 완료·전체 (`37dc785`) |
| lifecycle Badge | **`StaffPage`** 목록 · **`StaffDetailPage`** 기본정보 | **`StatusBadge`** + **`STAFF_LIFECYCLE_STATUS`** — 입사 진행·재직·퇴사 진행·퇴사 완료 (`b3e59e2`) |
| 진행률 | **`StaffLifecyclePanel`** | **`computeStaffLifecycleProgress`** — 단계별 완료 % (`37dc785`) |
| 탭 | **「기본정보」** · **「입사~퇴사」** · **「HR 파일함」** | **`StaffDetailPage`** — HR 탭에 **입사/퇴사 서류·이수증·건강검진 이력** 통합 (`bc3c967`) |
| 4단계 패널 | **`StaffLifecyclePanel`** + **`LifecycleWorkflowPanel`** | FAQ21825 ①~④ 체크리스트 · **근로계약서 서명일 `DateInput`** · 저장 **`aria-busy`** |
| 조회 | **`GET /api/v1/users/{userId}`** | lifecycle 필드 포함 · **`findUserByIdApi`** 404/405만 pagination fallback (QA-B55) |
| 저장 | **`PATCH /api/v1/users/{userId}`** | `lifecycleStatus`·`hiredAt`·`terminatedAt`·`onboardingComplete`·`reportingComplete`·`contractSignedAt`·`lifecycleChecklist` · **날짜 필드 API·폼 정규화** (`bb4c1af`) |
| 상태값 | `ONBOARDING` · `ACTIVE` · `OFFBOARDING` · `TERMINATED` | **Flyway V86** · UI Badge 라벨: 입사 진행·재직·퇴사 진행·퇴사 완료 |
| 퇴사 완료 | `lifecycleStatus=TERMINATED` + **`terminatedAt` 필수** + **`reportingComplete=true`** 또는 **「퇴사보고(`offboarding-report`)」** 체크 | 서버가 **`active=false`** 자동 설정 (`c976f55`) |
| 날짜 정합 | **`terminatedAt >= hiredAt`** · `TERMINATED` 시 **`terminatedAt` NOT NULL** | 앱 `validateLifecycleState` + **V87** DB CHECK (Q293) |

**FAQ21825 체크리스트 (체크박스 — 파일 첨부 아님)**

| 단계 | 항목 예시 |
|------|----------|
| ① 입사 | 신분증·자격증·통장·건강검진·치매교육·**근로계약서(서명 필요)**·범죄경력조회 |
| ② 신고 | 인력변경·RFID·배상책임보험·4대보험 취득 |
| ③ 근로 | 급여명세서·임금대장·보수교육·법정의무교육·건강검진 갱신 |
| ④ 퇴사 | 사직서(서명)·퇴사보고·4대보험 상실·퇴직정산·인수인계 |

| P2 잔여 | 설명 |
|---------|------|
| **건강검진 결과통보서 파일함** | FAQ21799 **결과통보서 PDF** 전용 업로드 — checklist `health-check`와 별도 |
| **급여·퇴직금** | **G-Payroll** Epic 연계 검토 |
| **전자서명** | G34 선임일지 수준 **서명 잠금 workflow** 미구현 |

> **HR 파일함**: FAQ **Q298** · USER_MANUAL §5-3 · ADMIN_GUIDE §6-2-5

> **퇴사 완료 가드**: `TERMINATED` 시 **`terminatedAt` 필수** + **`reportingComplete=true`** 또는 **「퇴사보고(`offboarding-report`)」** 체크 — 미충족 시 `422 BUSINESS_RULE` (`c976f55`).

> **입사 완료 가드**: `onboardingComplete=true` 시 **`contractSignedAt`** 또는 **「근로계약서」** 체크 필요 — 미충족 시 `422 BUSINESS_RULE`.

> 관련: Q162 · Q293 · Q294 · Q298 · **Q300** · Q284·Q287(lifecycle 패널 패턴) · USER_MANUAL §5-3 · ADMIN_GUIDE §1-4

### [TWR] Q298. **직원 입사 서류 파일함**(이지케어 FAQ21806)은 어디서 올리나요?

**A.** **Fixed (BE `bbb8e35`·FE `bc3c967` / US-R03·BNK-139, FAQ21806·FAQ21825)** — **`/staff/{userId}` → 「HR 파일함」** 탭의 **`StaffHrFilePanel`** 에서 **8종 입사/퇴사 서류**를 PDF·PNG·JPEG(**≤10MB**)로 업로드합니다.

| 항목 | 내용 |
|------|------|
| 진입 | **`/staff`** → 직원 **상세** → **「HR 파일함」** 탭 |
| 문서 유형 | 신분증·자격증·통장 사본·건강검진 결과·치매교육 이수·근로계약서·범죄경력조회·**사직서** |
| 교체 규칙 | **문서 유형당 1건** — 재업로드 시 기존 파일·스토리지 교체 |
| checklist | 업로드 시 **`lifecycleChecklist[documentType]=true`** · 삭제 시 **false** 자동 반영 |
| FAQ21806 ③ | **입사일 + 7일** 이내 **신규직원교육** — **`StaffLifecyclePanel`**·**`LifecycleWorkflowPanel`** 안내 (`NEW_HIRE_TRAINING_DEADLINE_DAYS=7`) |
| 동일 탭 | **`StaffRefresherCertificatePanel`**(8-7-1 이수증) · **`StaffHealthCheckupRecordsPanel`**(8-10 검진 이력) |
| RBAC | **업로드·삭제**: `branch_admin`·`social_worker` · **조회**: `hq_admin` 포함 · **`hq_admin` 업로드 UI 숨김** |
| API | **`GET/POST/DELETE /api/v1/staff/hr-files/users/{userId}*`** · **`GET …/{fileId}`** download |
| DB | **Flyway V91** `staff_hr_files` — V90 user-branch FK 패턴 · **V90** V88/V89 integrity (`a206508`) · **V92** org sync·`uploaded_by` backstop·purge index (`d4ee057`) |

| P2 잔여 | **건강검진 결과통보서** 전용 파일함(FAQ21799) · **4대보험·급여명세** 자동화 · **대시보드 위젯** |

> 관련: Q290 · Q296 · **Q300**(compliance 집계) · USER_MANUAL §5-3 · ADMIN_GUIDE §6-2-5

### [TWR] Q300. FAQ21806 **입사 처리 compliance 현황**은 어디서 확인하나요?

**A.** **Fixed (BE `d4ee057`·`60789d6`·FE `e76ca06`·`9ebb87f`·`4efa168` / US-R03·BNK-146, FAQ21806)** — **지점 집계**는 **`/staff`** 목록 상단 **`StaffOnboardingCompliancePanel`**, **직원별**은 **`/staff/{userId}` → 「입사~퇴사」** 탭 **`StaffMemberOnboardingComplianceCard`** 에서 확인합니다.

| 항목 | 내용 |
|------|------|
| **지점 집계** | SideNav **운영 → 직원 관리**(`/staff`) — 목록 **위** compliance 패널 |
| **직원별** | **`/staff/{userId}`** — **「입사~퇴사」** 탭 상단 카드 — 상태·서류 진행·신규교육 마감·미비 서류 |
| StatCard (목록) | **대상 직원** · **입사 완료** · **진행 중** · **기한 초과** 4종 |
| workflow | **`LifecycleWorkflowPanel`** — FAQ21806 **6단계**(자격확인·근로계약·신규교육 7일·신고·파일함·건강검진) 요약 |
| **HR 연동** | 미비 서류 **「○○ 업로드」** 버튼 → **「HR 파일함」** 탭으로 이동·해당 `documentType` 선택 (`4efa168`) · 업로드 후 compliance **자동 갱신** |
| 목록 표 | 직원별 **서류 진행(7종)** · **신규교육 마감일** · **미비 서류** · **상태 Badge** — 이름 클릭 시 상세 |
| 상태 | **입사 완료**(`COMPLETED`) · **진행 중**(`IN_PROGRESS`) · **기한 초과**(`OVERDUE`) · **미착수**(`DRAFT`) |
| 7종 서류 | 신분증·자격증·통장·건강검진·치매교육·근로계약서·범죄경력 — **HR 파일함 업로드** 또는 **lifecycle checklist 체크** 중 하나만 있어도 **제출로 인정** |
| 신규교육 | **입사일 + 7일**(`NEW_HIRE_TRAINING_DEADLINE_DAYS`) — 마감 초과·서류 미비 시 **`OVERDUE`** |
| API | **`GET /api/v1/staff/hr-files/onboarding-compliance?branchId=&referenceDate=`** — BE **`60789d6`** 지점 스코프 batch lookup |
| RBAC | **`hq_admin`·`branch_admin`·`social_worker`** — `caregiver`·`guardian` **접근 불가** |
| 지점 | JWT **`activeBranchId`**(또는 첫 `branchId`) 기준 — **`hq_admin`** 은 **지점 선택기**로 활성 지점 전환 후 조회 |

| P2 잔여 | **대시보드 위젯** · **4대보험·급여명세** 자동화 · **이메일 알림** |

> 관련: Q290 · Q298 · USER_MANUAL §5-3 · ADMIN_GUIDE §6-2-6

### [TWR] Q294. **직원 보수교육(8-7-1)** 이수 현황은 어디서 보나요?

**A.** **Fixed (BE `9c9fd5b`·`51477bd`·FE `314b380`·`0a7fe16`·`50bdb6e` / US-S02, FAQ21825)** — 케어포 **8-7-1**·이지케어 FAQ21825 **③ 근로활동** 「보수교육」 항목에 대응합니다. **입사일 기준 2년마다** 이수 여부를 집계합니다.

| 항목 | 내용 |
|------|------|
| 화면 | **`/staff/training`** — SideNav **운영 → 직원** 또는 **`StaffContextNav`** **「보수교육 (8-7-1)」** |
| 대상 역할 | **`caregiver`·`social_worker`·`branch_admin`** |
| 상태 | **이수 완료** · **이수 필요**(입사 2년 경과·미이수) · **이수 예정** · **입사일 미등록** |
| StatCard | **전체·이수 완료·이수 필요·이수 예정·입사일 미등록** — **`입사일 미등록`** 직원도 **`requiredCount`(이수 필요)** 집계에 포함 (`50bdb6e`, QA-B59) |
| 이수 기록 | 목록 **「이수 완료」** → **`POST /staff/refresher-training/compliance`** — `{ userId, completed: true }` (`510dbd1`, Q294) · 구버전 BE는 **`PATCH /users/{userId}`** lifecycle fallback · 또는 **「이수증」** 업로드 시 **자동 반영** (Q295) |
| 이수증 | 목록 **「이수증」** Modal — PDF/PNG/JPEG **≤10MB** 업로드·목록·미리보기·삭제 — **`branch_admin`·`social_worker`만** 업로드·삭제 (`0a7fe16`) |
| compliance API | **`GET /api/v1/staff/refresher-training/compliance?branchId=&referenceDate=`** — `hq_admin`·`branch_admin`·`social_worker` (BE 집계; FE **`StaffRefresherTrainingPage`** 가 동일 API 사용) |
| lifecycle 연동 | **`StaffLifecyclePanel`** ③ 근로 체크리스트 **「보수교육 (8-7-1)」** 와 **동일 checklist id** |

| P2 잔여 | **교육기관 API 연동** · **대시보드 위젯** |

> 관련: Q290 · Q295 · Q288 · USER_MANUAL §5-3 · ADMIN_GUIDE §1-4

### [TWR] Q295. 보수교육 **이수증 파일**은 어떻게 올리고 보관하나요?

**A.** **Fixed (BE `51477bd`·FE `0a7fe16` / US-S02, BNK-136)** — **`/staff/training`** 목록에서 직원별 **「이수증」** 버튼으로 Modal을 열어 관리합니다.

| 항목 | 내용 |
|------|------|
| 허용 형식 | **PDF** · **PNG** · **JPEG** — 최대 **10MB** (FE·BE·**V88** CHECK 동일) |
| 업로드 | **`POST /api/v1/staff/refresher-training/users/{userId}/certificates`** (multipart `file`) — **`branch_admin`·`social_worker`만** |
| 조회 | **`GET …/certificates`** 목록 · **`GET …/certificates/{certificateId}`** inline 미리보기 — **`hq_admin` 포함** 3역할 |
| 삭제 | **`DELETE …/certificates/{certificateId}`** — **`branch_admin`·`social_worker`만** |
| 자동 연동 | 업로드 성공 시 **`lifecycleChecklist["refresher-training"]=true`** 자동 저장 — **「이수 완료」** 버튼과 동일 효과 |
| 저장 | **Flyway V88** `staff_refresher_training_certificates` · 오브젝트 **`staff-refresher-training-certificates/{org}/{user}/…`** (기존 첨부 스토리지 디렉터리 재사용) |
| UI | PDF는 **새 탭** · 이미지는 **Modal 미리보기** · **`hq_admin`** 은 **조회·미리보기만** (업로드 UI 숨김) |

> 관련: Q294 · Q290 · USER_MANUAL §5-3 · ADMIN_GUIDE §6-2-3 · DATA_RETENTION_POLICY §3

### [TWR] Q296. **직원 건강검진(8-10)** 현황은 어디서 보나요?

**A.** **Fixed (BE `f1268c6`·`bad88f5`·FE `604787f` / US-R02, FAQ21799)** — 케어포 **8-10**·이지케어 FAQ21799 **지표9** 「연간 직원 건강검진」에 대응합니다. **일반 직원 1년** · **사무직 2년** 주기로 검진 여부를 집계합니다.

| 항목 | 내용 |
|------|------|
| 화면 | **`/staff/health-checkups`** — SideNav **운영 → 직원** 또는 **`StaffContextNav`** **「건강검진 (8-10)」** |
| 5개 영역 | **신체계측** · **요검사** · **혈액** · **영상** · **결과판정** — 기록 시 Checkbox (최소 1개 필수) |
| 상태 | **검진 완료** · **검진 필요** · **검진 예정** · **입사일 미등록** |
| 기록 | 목록 **「검진 기록」** Modal — **`POST /staff/health-checkups/users/{userId}`** |
| 이력 | **「이력」** Modal — **`GET /staff/health-checkups/users/{userId}`** |
| compliance API | **`GET /api/v1/staff/health-checkups/compliance?branchId=&referenceDate=`** — `hq_admin`·`branch_admin`·`social_worker` · **`bad88f5`** 지점 스코프 강제 |
| lifecycle | **`StaffLifecyclePanel`** ① **「건강검진」**(`health-check`) · ③ **「건강검진 갱신」**(`health-check-renewal`) — checklist id 동일 도메인 |

| P2 잔여 | **결과통보서 PDF·이미지 파일함**(FAQ21799·FAQ21806) · **대시보드 위젯** · 검진 기록 시 checklist **자동 반영** |

> 관련: Q290 · USER_MANUAL §5-3 · ADMIN_GUIDE §6-2-4 · DATA_RETENTION_POLICY §3

### [TWR] Q297. NHIS 방문일정 import에서 **`.xls`**(구형 엑셀)도 되나요?

**A.** **Fixed (BE `3f444a1`·`1817c36`·`b864272` / G21)** — 이전에는 **`.xlsx`만** 허용했으나, 공단·레거시 시스템이 보내는 **`.xls`** 파일도 import할 수 있습니다.

| 항목 | 내용 |
|------|------|
| 허용 확장자 | **`.xlsx`** · **`.xls`** |
| Content-Type | **`application/vnd.ms-excel`** · **`application/vnd.openxmlformats-officedocument.spreadsheetml.sheet`** · **`application/xls`** · **`application/x-excel`** · **`application/octet-stream`** · **대소문자·공백 혼합**(`Application/VND.MS-EXCEL; charset=UTF-8` 등) — **`;charset=…` strip** 후 허용 (`1817c36`·`b864272`) |
| 화면 | **`/visits`** — **「공단 방문일정 엑셀 import」** (`VisitNhisImportPanel`) |
| API | **`POST /api/v1/visits/imports/nhis`** multipart |

> 관련: Q278 · Q189 · USER_MANUAL §5-11 · ADMIN_GUIDE §1-4

### [TWR] Q301. **신규입소 위험도평가**(낙상·욕창·인지기능, silverangel 지표21)는 ogada에 있나요?

**A.** **Fixed (BE `22d736b`·`686d686`·`f0752b6`·`2589b94` / FE `328d697`·`2f5af63` / G40·BNK-150~152)** — 엔젤 silverangel **「신규입소시」** 9-step 중 ③④⑤(낙상위험도·욕창위험도·인지기능평가)에 대응하는 **REST API·DB(V93/V94)·이용자 상세 UI·대시보드 compliance 위젯**이 제공됩니다.

| 항목 | 내용 |
|------|------|
| 화면 | **`/clients/:id`** → **「위험도평가」** 탭 — **`ClientRiskAssessmentPanel`** — 3종 폼·**StatCard (N/3)** · **`LifecycleWorkflowPanel`** |
| 대시보드 | **`/dashboard`**·**`/dashboard/hq`** — **「신규입소 위험도평가 미완료」** StatCard — **`admissionRiskAssessmentGapCount`** — 1명 이상이면 **danger** 톤 · 클릭 시 **`/clients`** (`2f5af63`) |
| 평가 3종 | **`FALL_RISK`**(낙상) · **`PRESSURE_ULCER`**(욕창) · **`COGNITIVE_FUNCTION`**(인지기능) |
| 준수 규칙 | **`ltcCertValidFrom`(급여개시일) 이전** 3종 모두 **`assessedOn` 기록** — 미완료 시 **`admissionComplete=false`** warning |
| 이용자별 CRUD | **`GET /api/v1/clients/{clientId}/risk-assessments`** · **`PUT /api/v1/clients/{clientId}/risk-assessments`** — 유형당 1건 upsert |
| 요청 본문 | `{ "assessmentType": "FALL_RISK", "assessedOn": "2026-01-15", "scaleScore": 12, "riskLevel": "MODERATE", "notes": "…" }` — **`riskLevel`**: `LOW`·`MODERATE`·`HIGH` |
| 지점 compliance | **`GET /api/v1/clients/admission-risk-assessments/compliance?branchId=`** — 이용자별 **`admissionComplete`**·`missingTypes[]`·`lateTypes[]` — 동일 유형 중복 시 **가장 이른 `assessedOn`/`recordedAt`** 기준(`2589b94`) |
| RBAC | **`hq_admin`·`branch_admin`·`social_worker`** — 조회·등록 · **`caregiver`** — 조회만 · **`guardian`** — **403** |
| DB | **Flyway V93** `client_risk_assessments` — org·branch·client composite FK · active client guard · **V94** integrity index·**`recorded_at >= created_at`** CHECK |
| G24와 구분 | **G24 욕구사정(지표20)** — **「기초평가」** 탭(Q286) · **G40 위험도평가(지표21)** — **「위험도평가」** 탭 **상단 패널**(Q301) · **G40b 반기 재평가(지표16)** — **동일 탭 하단 패널**(Q302) |

| P2 잔여 | **급여개시 전 알림**(push/이메일) |

> 관련: Q286(G24) · **Q302(G40b)** · USER_MANUAL §3-3 · ADMIN_GUIDE §6-2-7 · BENCHMARK_REPORT §152

### [TWR] Q302. **반기 기초평가 위험도**(낙상·욕창·인지기능 재평가, silverangel 지표16·FAQ21811)는 ogada에 있나요?

**A.** **Fixed (BE `84e59d2`·`bdfc140`·`a7b4a39` / FE `22325f4`·`7b68f54`·`fad6df1` / G40b·BNK-153~154)** — 이지케어 **「2.2 정기욕구평가현황」**·silverangel **지표16**에 대응하는 **반기 1회** 위험도 재평가 REST API·DB(V95/V96)·이용자 상세 UI·지점 현황 화면·대시보드 compliance 위젯이 제공됩니다.

| 항목 | 내용 |
|------|------|
| G40과 구분 | **G40(Q301)** = 급여개시 **전** 1회(지표21) · **G40b(Q302)** = **반기 1회** 재평가(지표16) — **동일 「위험도평가」 탭**에 **`ClientRiskAssessmentPanel`** + **`ClientPeriodicRiskAssessmentPanel`** |
| 이용자 상세 | **`/clients/:id`** → **「위험도평가」** — **`ClientPeriodicRiskAssessmentPanel`** — 반기 라벨·3종 폼·**StatCard (N/3)** · **`periodicComplete`** warning |
| 정기욕구평가 현황 | **`/clients/periodic-risk-assessments`** — **`PeriodicRiskAssessmentStatusPage`** — 회계연도·반기 선택 · StatCard·미완료 표 · **「이용자 상세」** 링크 (`7b68f54`) · SideNav **「정기욕구평가 현황 (G40b)」** |
| 대시보드 | **`/dashboard`**·**`/dashboard/hq`** — **「반기 기초평가 위험도 미완료」** — **`periodicRiskAssessmentGapCount`** — 클릭 **`/clients/periodic-risk-assessments`** (`22325f4`) |
| 평가 3종 | G40과 동일 — **`FALL_RISK`** · **`PRESSURE_ULCER`** · **`COGNITIVE_FUNCTION`** |
| 반기 | **`fiscalYear`** · **`fiscalHalf`**(1=상반기 1~6월, 2=하반기 7~12월) — `(org, client, year, half, type)` **UNIQUE** |
| 준수 규칙 | 급여 수급 중 활성 이용자 · **반기 윈도우 내 3종 완료** · **`periodicComplete`** · 평가일 **`max(반기시작, 급여개시일)` ~ 반기종료** |
| CRUD | **`GET/PUT /api/v1/clients/{clientId}/periodic-risk-assessments?fiscalYear=&fiscalHalf=`** |
| 지점 compliance | **`GET /api/v1/clients/periodic-risk-assessments/compliance?fiscalYear=&fiscalHalf=&branchId=`** — `items[]` · `gapCount` |
| RBAC | **`hq_admin`·`branch_admin`·`social_worker`** — 조회·등록 · **`caregiver`** — 조회만 |
| DB | **Flyway V95** `client_periodic_risk_assessments` · **V96** integrity index·**`recorded_at >= created_at`** CHECK |
| 접근성 | UXD-91 — 동일 탭 6개 액션 버튼 **`aria-label`**에 **「반기」**·유형명 컨텍스트 (`fad6df1`) |

| P2 잔여 | **G40/G40b live API E2E run** — harness **`riskAssessmentLiveApi.e2e.test.js`** 추가(`0ce04ad`) · 스테이징 **`LIVE_E2E=1`** 실행 |

> 관련: Q301(G40) · USER_MANUAL §3-3·§4-3 · ADMIN_GUIDE §6-2-8 · API_SPEC §9-9 · BENCHMARK_REPORT §153

### [TWR] Q303. **선임 업무수행일지「불러오기」**(이지케어 FAQ21813, G34b)는 ogada에 있나요?

**A.** **Fixed (FE `0ce04ad` / G34b·BNK-157)** — **예.** **`/staff/lead-caregiver-log`** **업무수행일지 등록** 폼에 **「욕구사정·계획 불러오기」** 버튼이 제공됩니다. 이용자 상세에 이미 저장된 **G24 욕구사정**·**G17 기능회복훈련 계획**을 읽어 **업무 수행 내용·특이사항** 초안을 채웁니다.

| 항목 | 내용 |
|------|------|
| 전제 | **이용자**를 먼저 선택 · **기록 일자**의 **회계연도**로 욕구사정 조회 |
| 데이터 원천 | **`GET /clients/{clientId}/needs-assessments?fiscalYear=`** (G24, Q286) · **`GET /functional-recovery/plans?year=&clientId=`** (G17, Q262) · **또는 BE `GET /staff/lead-caregiver-logs/import-draft?source=needs_assessment`** (`8487667`) |
| 불러오는 항목 | 욕구사정 **13항목** — 기본 8항목 + **G24b 5항목**(질병·의사소통·영양·환경·자원이용, `45fb6d9`) · **가정방문 일자** · 기능회복훈련 **최신 계획 본문** |
| 병합 규칙 | **`workContent`·`careNotes`가 비어 있으면** draft로 **대체** · **이미 입력된 경우** 기존 내용 **아래에 append** |
| 빈 결과 | 해당 연도 기록 없음 → 「…기록이 없어 불러올 내용이 없습니다.」 |
| 권한 | G34과 동일 — **`hq_admin`·`branch_admin`·`social_worker`·`caregiver`** |
| 접근성 | 버튼 **`aria-label="욕구사정·기능회복훈련 계획 불러오기"`** · 진행 중 **「불러오는 중…」** |

| P2 잔여 | **30일 rolling 자동 반영**(FAQ21813 모니터링 7) · **관리자 라운딩(FAQ21812)** · **K-MMSE·인쇄** |

> 관련: Q284(G34) · Q286(G24) · Q262(G17) · USER_MANUAL §5-9 · ADMIN_GUIDE §6-2-9 · BENCHMARK_REPORT §157

### [TWR] Q304. 방문일정에 **퇴사한 직원**을 담당자로 배정할 수 있나요?

**A.** **Fixed (BE `dc48933`, G21, US-V02)** — **아니요.** 방문일정 **등록·수정** 시 **`assignedUserId`**(담당 직원)에 대해 **활성·재직·지점 소속** 검증이 적용됩니다.

| 상황 | API 응답 |
|------|----------|
| 존재하지 않는 직원 ID | **`404`** 「배정할 직원을 찾을 수 없습니다.」 |
| **`active=false`** 또는 **`terminatedAt` 설정** | **`422 BUSINESS_RULE`** 「퇴사 또는 비활성화된 직원은 배정할 수 없습니다.」 |
| **다른 지점 소속**(`user_branches`에 활성 지점 없음) | **`422 BUSINESS_RULE`** 「해당 지점 직원만 방문일정에 배정할 수 있습니다.」 |

| API | `POST /api/v1/visits` · `PATCH /api/v1/visits/{id}` — **`assignedUserId` optional** · null이면 검증 생략 |
| 테스트 | **`VisitServiceTest`** +196 · **`VisitPilotServiceFlowE2eTest`** +19 |

> 관련: Q238 · Q289 · **Q307(체크인 가드)** · USER_MANUAL §5-11 · ADMIN_GUIDE §10-12 · API_SPEC G21

### [TWR] Q305. **고충상담 기록**(케어포 8-8·이지케어 FAQ21814, G42)은 ogada에 있나요?

**A.** **Partial+ Fixed (BE `bcb1d9f`·`6f6094d`·`bcdc411` / FE `6012044`·`892450a`·`a7a6004` / G42·US-T14·BNK-161~174)** — **예.** **`/staff/grievance-counselings`** 화면에서 **수급자·요양보호사·기타** 고충 접수·상담 기록을 등록하고 **전자결재 요청·승인**·**사후관리(재발 확인)** 까지 처리할 수 있습니다.

| 항목 | 내용 |
|------|------|
| 화면 | **`GrievanceCounselingPage`** — **`StaffContextNav`** **「고충상담 (8-8 G42)」** · **`ComplaintConsultationPanel`** |
| **결재 대기** | **`hq_admin`·`branch_admin`** — 상단 **결재 대기** StatCard·표 — **`GET …/pending-approval`** 병렬 로드 (Q309·Q316) |
| **사후관리 대기** | **`APPROVED`** 후 **사후관리 미기록** 건 — **사후관리 대기** StatCard·표 · **「사후관리 기록」** → **`GrievanceFollowUpModal`** |
| 접수 경로 | `WRITTEN`·`PHONE`·`SMS`·`IN_PERSON`·**`ANONYMOUS_BOX`(익명함)** — DB·API enum 지원 |
| **익명함 마스킹** | **Fixed (`4b54da5`)** — 접수 경로가 **`ANONYMOUS_BOX`** 이면 목록·결재 문맥에서 대상명 **「익명」**·**「익명함」** 으로 표시 — PII 비노출 (FAQ21814) |
| **익명함 접수 폼** | **Partial+ Fixed (`8a8b930`)** — **`ComplaintConsultationForm`** — **`ANONYMOUS_BOX`** 선택 시 **대상 유형·이용자/직원·대상명 필드 숨김** · payload **`targetType=OTHER`·`targetName=익명`** 자동 · **`ComplaintConsultationForm.test`**·**`pilotPageFlows`** E2E |
| 대상 유형 | **`CLIENT`**(이용자) · **`CAREGIVER`**(직원) · **`OTHER`**(기타) |
| 결재 흐름 | **`DRAFT` → `SUBMITTED`(전자결재 요청) → `APPROVED`(센터장·통합관리자 결재)** — **중복 결재 버튼 방지** (`892450a`) |
| 권한 | **등록·수정·결재요청·사후관리** — `hq_admin`·`branch_admin`·`social_worker` · **결재** — `hq_admin`·`branch_admin` · **`caregiver` 조회만** |
| API | `GET/POST/PATCH /api/v1/staff/grievance-counselings*` · `POST …/{id}/submit` · `POST …/{id}/approve` · **`GET …/pending-approval`**(Q309) · **`POST …/{id}/follow-up`** · **`GET …/follow-up/pending`** · **`GET …/follow-up/compliance`**(Q316) |
| DB | **Flyway V97** `grievance_counseling_records` · **V98** integrity (`6f6094d`) |

| P2 잔여 | FAQ21814 **서류함 PDF 저장** · **전자결재 다단계** · **결재함 전용 별도 라우트** · **익명함 별도 라우트** |

> 관련: Q284(lifecycle 패턴) · USER_MANUAL §5-3 · ADMIN_GUIDE §6-2-10 · BENCHMARK_REPORT §161

### [TWR] Q306. 업무수행일지 **「전월 일지 복제」**와 **인지활동 편집 제한**(G34b)은 무엇인가요?

**A.** **Fixed (FE `1b5fabe` / G34b·BNK-160)** — **`/staff/lead-caregiver-log`** 등록 폼에 **「전월 일지 복제」** 버튼이 추가되었습니다. 선택한 이용자의 **전월(기록 일자 −1개월) 최신 일지** 내용을 읽어 **업무 수행 내용·특이사항**에 붙여 넣습니다.

| 항목 | 내용 |
|------|------|
| 전제 | **이용자** 선택 · 전월에 **복제할 내용이 있는 DRAFT/SIGNED 일지** 존재 |
| 병합 | **`[전월 일지 복제 — YYYY-MM-DD]`** 헤더 + 본문 — 기존 입력 **append** |
| 빈 결과 | 전월 일지 없음 → 「전월에 복제할 업무수행일지가 없습니다.」 |
| **인지활동 role guard** | FAQ21813 — **`[인지활동]`·「인지·정서」** 항목은 **`hq_admin`·`branch_admin`·`social_worker`만** 불러오기·복제에 포함 · **`caregiver`** 는 해당 구간 **자동 제외** + 안내 Alert · **저장 시 BE·FE 이중 검증** (`b6ecc35`·`994f5ea`, Q306) |
| API | **`GET /staff/lead-caregiver-logs/import-draft?clientId=&logDate=&source=previous_month`** (BE `8487667`) — FE는 기존 목록 API 또는 import-draft 재사용 |

> 관련: Q303(불러오기) · Q284(G34) · USER_MANUAL §5-9 · ADMIN_GUIDE §6-2-9

### [TWR] Q307. 방문일정 **체크인·체크아웃**은 담당 직원만 할 수 있나요?

**A.** **Fixed (BE `b459f4c`·`c16f4fe`, G21, US-V02, QA-B73)** — **예(요양보호사 한정).** 일정에 **`assignedUserId`(담당 직원)** 가 배정되어 있으면 **`caregiver`** 는 **본인이 배정된 일정만** 체크인·체크아웃할 수 있습니다.

| 상황 | 동작 |
|------|------|
| **`caregiver`** + 배정 직원 ≠ 로그인 사용자 | **`422 BUSINESS_RULE`** 「배정된 요양보호사만 체크인·체크아웃할 수 있습니다.」 |
| **`hq_admin`·`branch_admin`·`social_worker`** | **감독 역할**(`CHECK_IN_SUPERVISORY_ROLES`) — 배정과 무관하게 체크인·체크아웃 가능 |
| **`assignedUserId` null** | 기존과 동일 — 배정 없으면 가드 **생략** |
| 검증 시점 | **`POST /visits/{id}/check-in`** · **`POST /visits/{id}/check-out`** — confirm 시 **재검증**(`b459f4c`·`c16f4fe`) |

> 관련: Q304(배정 검증) · Q238(페어 동기화) · USER_MANUAL §5-11 · ADMIN_GUIDE §10-12

### [TWR] Q308. **직원현황 리포트**(케어포 8-12, US-R02)는 ogada에 있나요?

**A.** **Fixed (BE `aaa16f8`·`5692662` / FE `bf6dd25`·`07956f5` / US-R02·BNK-142~171)** — 케어포 **8-12** 「직원현황 리포트」에 대응하는 **`/staff/reports/status`** 화면이 있습니다. **2026-06-13** 기준 FE는 **aggregated API 단일 호출**로 전환되었고, **출력물 7종**(Q315)도 추가되었습니다.

| 항목 | 내용 |
|------|------|
| 진입 | SideNav **운영 → 직원** · **`StaffContextNav` 「직원현황 리포트 (8-12)」** |
| 기준일 | **`referenceDate`** DateInput — **조회** 시 서버 집계 |
| StatCard | **대상 직원** · **조치 필요** · **입사 기한 초과** · **보수교육 미이수** · **건강검진 필요** |
| lifecycle | **`LifecycleWorkflowPanel`** — 8-12 단계별 **지연 건수** |
| 표 | 직원별 **입사 처리·보수교육·건강검진·종합** Badge |
| 출력물 7종 | **직원현황·명부·사진게시·연락처·월간명부·입퇴사**(인쇄) · **엑셀**(CSV) — `staffStatusReportExports.js` |
| RBAC | **`hq_admin`·`branch_admin`·`social_worker`** 조회 · **`caregiver`·`guardian` 403** |

| API | 용도 |
|-----|------|
| **`GET /api/v1/staff/reports/status?branchId=&referenceDate=`** | **aggregated** items[] + summary — onboarding·refresher·health **서버 병합** (BE `aaa16f8`) |

| P2 잔여 | **대시보드 위젯** · **공식 PDF 서식**(현재 인쇄·CSV) · **live E2E** |

> 관련: Q296 · Q294 · Q300 · Q315 · USER_MANUAL §5-3 · ADMIN_GUIDE §6-2-4

### [TWR] Q309. 고충상담 **결재 대기 목록 API**(G42 결재함)는 있나요?

**A.** **Fixed (BE `6f6094d` / FE `6012044`·`892450a`, G42·BNK-161~174)** — **예.** 센터장·통합 관리자가 **`SUBMITTED`** 상태 고충상담 기록을 한 번에 조회할 수 있습니다. **2026-06-14** 기준 FE **`ComplaintConsultationPanel`** 에 **결재 대기** StatCard·표가 연동되었습니다.

| 항목 | 내용 |
|------|------|
| API | **`GET /api/v1/staff/grievance-counselings/pending-approval`** |
| 응답 | 일반 목록과 동일 **`GrievanceCounselingListResponse`** — 활성 지점 스코프 내 **`SUBMITTED`** 만 |
| 권한 | **`hq_admin`·`branch_admin`** — `social_worker` **403** |
| DB | **Flyway V98** — temporal CHECK·actor backstop·approval queue index |
| FE | **`GrievanceCounselingPage`** — **`fetchGrievancePendingApprovalsApi`** 병렬 로드 · 패널 **결재 대기** 섹션 · 목록 **「결재 승인」** 버튼 (`6012044`) |

> 관련: Q305 · ADMIN_GUIDE §6-2-10 · API_SPEC G42

### [TWR] Q310. 청구 생성이 막혔을 때 **7-2→7-1 workflow** 안내는 어디서 보나요?

**A.** **Fixed (FE `338c014`, G-7x-1-guard·BNK-160, US-M03)** — **`/billing`** **`ClaimGenerationGuardBanner`** 가 전월 미입금·**G33 미정산** 차단 시 **케어포 PDF p.86–87** 순서를 **`LifecycleWorkflowPanel`** 로 안내합니다.

| 항목 | 내용 |
|------|------|
| 단계 1 | **7-2 입금 처리 (전월)** — `CONFIRMED` 미수납 건수·**`paidAt` 필수** 안내 |
| 단계 2 | **7-1 월별 청구 생성** — 선행 입금 완료 후 진행 |
| G33 분기 | 메시지에 **「청구시작 기준금액」**·**「도입 전 미납」** 포함 시 **미납 정산** 링크 표시 |
| 바로가기 | **입금 처리**(`/billing/payments`) · **미납 관리**(`/billing/overdue`) · **청구시작 기준금액 정산**(`/organization/settings`) |
| 유틸 | **`claimGenerationGuard.js`** — **`analyzeClaimGenerationGuard`**·**`buildClaimGenerationWorkflowSteps`** |

> 관련: Q225 · Q270 · USER_MANUAL §4-6 · ADMIN_GUIDE §6-3

### [TWR] Q311. **인지지원등급(ltcGrade 0)** 수가표 5칸은 NHIS import와 별도인가요?

**A.** **Fixed (BE `2efc557`·`edd2771`·`8bb6583`·FE `6ef671b`, G9-COG·BNK-166, US-G04)** — **표준 25칸**과 **인지지원 5칸**은 **별도 그리드**이지만, import gate는 **두 단계**입니다.

| gate | 조건 | 미완비 시 |
|------|------|----------|
| **표준 (항상)** | 1~5등급×5밴드 = **25칸** | **`422`** — NHIS import 불가 |
| **인지지원 (조건부)** | 지점에 **활성 `ltcGrade=0` 이용자** | 인지지원 **5칸** 미완비 시 **`422`** (`8bb6583`) |
| **인지지원 (해당 없음)** | 인지지원 이용자 **없음** | 5칸 **권장·별도 집계**만 — import **차단 없음** |

| 항목 | 내용 |
|------|------|
| BE catalog | **`Nhis2026DaycareRateCatalog`** — longterm.or.kr 502 표② 인지지원등급 행 (MOHW 제2025-247호) |
| DB | **Flyway V99** — **`ltc_grade` CHECK 0–5** (`edd2771`) |
| seed payloads | **`GET /api/v1/billing/fee-schedules/nhis-seed-payloads?year=`** — 미등록 셀 NHIS 참조 payload 목록 |
| bulk seed | **`POST /api/v1/billing/fee-schedules/apply-nhis-seeds?year=`** — 미등록 **표준+인지지원** 셀 **일괄 등록** (`edd2771`) — UI는 셀별 `POST` 반복과 동일 결과 |
| year-coverage | **`cognitiveRegistered`·`cognitiveExpected`(5)·`cognitiveComplete`** — 표준 25칸과 **분리 집계** |
| FE matrix | **`FeeScheduleMatrix`** — **6행**(1~5등급 + 인지지원) × 5밴드 = **30칸** · **「공단 2026 수가 시드 (N건)」** |
| 등록 API | **`POST /billing/fee-schedules`** — **`ltcGrade: 0`** 허용 · **`POST/PATCH /clients`** **`ltcGrade: 0`** (V99) |
| 월한도 | **`COGNITIVE_SUPPORT` 676,320원** — Q228과 동일 catalog 연계 |
| E2E | **`CognitiveSupportFeeSchedulePilotServiceFlowE2eTest`** — seed apply → NHIS import unblock (`8bb6583`) |

> **P2**: 인지지원등급 이용자 **전용 onboarding wizard** — FAQ21824 Epic 잔여.

> 관련: Q260 · Q214 · Q228 · USER_MANUAL §5-4 · ADMIN_GUIDE §6-3-1

### [TWR] Q313. **「감경 40%」**와 **본인부담률 9%**가 헷갈려요.

**A.** **Fixed (FE `e77b7e4`, G9-COPAY-NAMING·BNK-166 §166-3)** — ogada는 UI 약칭과 **법·고시 정식 용어**를 **동시에** 표시합니다.

| UI 약칭 (`label`) | 정식 용어 (`statutoryLabel`) | 실제 본인부담률 |
|-------------------|------------------------------|----------------|
| 일반 | 일반 (감경 없음) | 15% |
| 감경 40% | **100분의 40 감경** | **9%** (15%×60%) |
| 감경 60% | **100분의 60 감경** | **6%** (15%×40%) |
| 기초수급 | 의료급여 (본인부담 면제) | 0% |

| 화면 | 표시 위치 |
|------|----------|
| 이용자 등록·수정 | **`CopayTypeSelect`** — 옵션·선택 help에 **`statutoryLabel · 본인부담률`** |
| 본인부담 비율표 | **`CopayRateTable`** — 구분 설명 fallback |
| 접근성 | **`Field` `help`** → **`aria-describedby`** 연결 (UXD-94, `a5c2736`) |

> **근거**: longterm.or.kr **503 본인부담금 감경**·노인장기요양보험법 **제40조**·고시 용어. **코드·비율 수치는 변경 없음** — 표기만 명확화.

> 관련: Q30 · USER_MANUAL §5-4 · REQUIREMENTS BNK-166 §166-3

### [TWR] Q314. **모니터링 자가진단·유선상담**(G30, FAQ21836/21841/21842)은 어디서 하나요?

**A.** **Fixed (BE `6a72b70`·`b1dfd34` / FE `574bd08` / G30·BNK-169~171·181)** — SideNav **운영 → 모니터링 자가진단 (G30)** · URL **`/compliance/monitoring`** 에서 **월별 15문항 자체점검**·**월 5명 유선상담**·**통합 checklist 8문항**을 기록·확인합니다.

| 항목 | 내용 |
|------|------|
| 통합 checklist | FAQ21838~21842 **문항 6~15** — **`GET …/checklist`** 자동 집계 · **`MonitoringIntegratedChecklistPanel`** (Q320) |
| checklist 상태 | **`MET`(충족)·`PARTIAL`(일부)·`UNMET`(미충족)·`MANUAL`(수동)** — **RFID(문항10)** 는 항상 **MANUAL** |
| 자가진단 | **15문항** — **점검방향·관련근거·점검기준·점검결과·점검방법** 5필드 · **문항×월 1건** |
| 6개월 준수 | FAQ21842 — **`GET …/self-diagnoses/compliance`** rolling **6개월** StatCard |
| 유선상담 | FAQ21836 — **월 5명** **`REQUIRED_PHONE_CONSULTATIONS=5`** · **`GET …/suggestions`** 추천 |
| 관련근거 fallback | **`DEFAULT_MONITORING_RELATED_BASIS`** — 고시·세부사항 조문 (`0da41c6`) |
| RBAC | **`hq_admin`·`branch_admin`·`social_worker`** · **`caregiver`·`guardian` 403** |
| DB | **Flyway V100** tables · **V101** active-client guard·`created_by` backstop |

| API | 용도 |
|-----|------|
| `GET /api/v1/compliance/monitoring/checklist` | **통합 checklist** 8문항 (Q320) |
| `GET /api/v1/compliance/monitoring/items` | 15문항 템플릿 |
| `GET/POST/PATCH …/self-diagnoses*` | 월별 자가진단 CRUD |
| `GET …/self-diagnoses/compliance` | 6개월 compliance |
| `GET/POST …/phone-consultations*` | 유선상담 CRUD·compliance |

| P2 잔여 | FAQ21812 **관리자 라운딩** · **live E2E** |

> 관련: Q320 · Q306(G34b) · DATA_RETENTION §3(5년 보관) · USER_MANUAL §4-3 · ADMIN_GUIDE §6-2-11

### [TWR] Q315. **8-12 직원현황** PDF·엑셀 출력은 되나요?

**A.** **Partial+ Fixed (BE `bc927f7`·`c4dbe43` / FE `488f547`·`5bba7a2`·`ff173af` / US-R02·BNK-175)** — **케어포 PDF p.106 7종**에 대응하는 **브라우저 인쇄 6종 + 서버 CSV(엑셀 호환) 1종**이 **`/staff/reports/status`** 에 있습니다. **엑셀**은 FE 클라이언트 생성이 아닌 **BE CSV API**를 사용합니다. **공식 PDF 서식 파일**은 아직 없습니다.

| 출력물 | 방식 | 데이터 |
|--------|------|--------|
| 직원현황(기준일) | 인쇄 | aggregated compliance 표 — 인쇄 전 행 안정화 (`5bba7a2`) |
| 명부·사진게시 | 인쇄 | 이름·역할 · 사진게시는 HR 파일 미리보기 |
| 연락처·월간명부·입퇴사 | 인쇄 | **`GET /users` page-through**(size=200, max 50 pages) 프로필 enrich (`ff173af`) |
| 엑셀 | **CSV 다운로드 (BE)** | **`GET /staff/reports/status/export?referenceDate=&outputType=excel`** — UTF-8 BOM (`bc927f7`) |

| API | 용도 |
|-----|------|
| **`GET /api/v1/staff/reports/status/export`** | 서버 집계 CSV — `Content-Disposition: attachment` |

| P2 잔여 | **공식 PDF 서식** · **대시보드 위젯** · export **live E2E** |

> 관련: Q308 · USER_MANUAL §5-3 · ADMIN_GUIDE §6-2-4

### [TWR] Q316. 고충상담 **사후관리(재발 확인)**(G42, FAQ21814)는 어떻게 하나요?

**A.** **Fixed (BE `bcb1d9f` / FE `6012044`, G42·BNK-174, US-T14)** — **`APPROVED`** 고충상담 기록에 대해 **사후관리(재발 확인)** 를 기록합니다.

| 항목 | 내용 |
|------|------|
| 진입 | **`/staff/grievance-counselings`** — **사후관리 대기** StatCard·표 · 목록 **「사후관리 기록」** 버튼 |
| 모달 | **`GrievanceFollowUpModal`** — **사후관리 내용**(필수) · **재발 확인** Checkbox |
| API | **`POST /api/v1/staff/grievance-counselings/{id}/follow-up`** — body: `followUpNotes`·`recurrenceConfirmed` |
| 대기 목록 | **`GET …/follow-up/pending`** — 승인 후 사후관리 미기록 건 |
| compliance | **`GET …/follow-up/compliance`** — `pendingFollowUpCount`·`recordedFollowUpCount` |
| 표시 | 사후관리 완료 시 목록에 **「사후관리」** Badge (`followUpRecordedAt`) |
| RBAC | **`hq_admin`·`branch_admin`·`social_worker`** |

| P2 잔여 | FAQ21814 **서류함 PDF 저장** · **사후관리 기한 자동 알림** |

> 관련: Q305 · Q309 · USER_MANUAL §5-3 · ADMIN_GUIDE §6-2-10

### [TWR] Q317. **이동서비스비 RU_3·RU_4** 수가가 바뀌었나요? (#44 P0)

**A.** **Fixed (BE `39ee679`, G16·#44·BNK-174)** — **예.** NHIS **제34조 lawImg** 정본(5,230원·8,630원)에 맞춰 **Flyway V103** 이 기존 시드 오차를 보정했습니다.

| 거리대 | 변경 전 (V68 시드) | 변경 후 (V103·#44 정본) |
|--------|-------------------|------------------------|
| **RU_3** (10~20km) | 4,430원 | **5,230원** |
| **RU_4** (20km 이상) | 6,230원 | **8,630원** |

| 항목 | 내용 |
|------|------|
| 영향 | **신규** `transport_service_fee_records` 생성 시 보정된 catalog 적용 |
| 기존 기록 | 이미 확정된 fee record **금액은 변경되지 않음** — 감사·재현 목적 |
| 운영 | 배포 후 Flyway **V103** 자동 적용 — DEPLOYMENT §3-6 |

> 관련: Q239 · Q247 · DATA_RETENTION §3 · ADMIN_GUIDE §1-4 G16

### [TWR] Q318. **알림톡·이메일** live 연동 준비 상태는 어디서 보나요?

**A.** **Fixed (BE `726b3de` / FE `6b1258c`·`d695923`·`76b5ff0`, J03·US-J03, BNK-177)** — **`hq_admin`·`branch_admin`** 이 화면 또는 API로 **비밀값 없이** 채널 readiness를 확인할 수 있습니다.

| 항목 | 내용 |
|------|------|
| **화면** | **`/organization/settings`** **「알림 채널 준비 상태」** 카드(`hq_admin`) · **`/dashboard`·`/dashboard/hq`** 하단 동일 패널(`hq_admin`·`branch_admin`) — **`NotificationChannelReadinessPanel`** |
| **접근성 (UXD-97)** | Solapi·SMTP·템플릿 설정 표는 **`.ds-dl-grid`** 레이아웃 · 각 표 앞 **`<h3>` 섹션 제목**(시각 사용자·스크린리더 구분, `76b5ff0`) |
| API | **`GET /api/v1/notifications/channel-status`** |
| 응답 | `alimtalkProvider`·`emailProvider` · Solapi **apiKey/secret/senderId/kakaoPfId configured** · **`smtpHostConfigured`** · **`liveAlimtalkDispatchReady`·`liveEmailDispatchReady`** · **`quietHoursActive`**(KST **22:00–08:00**) · 필수 알림톡 템플릿 목록 |
| 보안 | **API 키·시크릿 값 미노출** — configured boolean만 |
| 조용한 시간대 | **`quietHoursActive=true`** 이면 UI에 **22:00~08:00 (Asia/Seoul)** 안내 — **긴급(`EMERGENCY`) 알림은 발송 우회**(Q147) · **청구 화면 발송 버튼도 동일 시간대 비활성**(Q329, `111f056`) |
| RBAC | **`hq_admin`·`branch_admin`** 조회 · **`sysadmin`·`caregiver`·`guardian` 403** |

| P2 잔여 | **live E2E 발송 검증** — readiness UI는 Fixed |

> 관련: Q204 · Q266 · Q147 · ADMIN_GUIDE §10-8 · DEPLOYMENT §4-3·§4-8 · USER_MANUAL §2-2·§5-5

### [TWR] Q319. **선임 요양보호사**(G34) 지정 시 **팀장급 자격**(FAQ21837)은 어떻게 확인하나요?

**A.** **Fixed (BE `726b3de`·`9a8bd2a` / FE `574bd08`, G34-QUAL, FAQ21837)** — **`/staff/lead-caregiver-log`** 화면 **compliance 패널**·**일지 저장 API** 모두 **팀장급 요양보호사 자격기준(실무경력 5년)** 을 **입사일(`hiredAt`) 기준**으로 안내·검증합니다.

| 항목 | 내용 |
|------|------|
| 기준 | FAQ21837·고시 제48~58조 — **실무경력 5년**(월 60시간×60개월) · ogada v1은 **`hiredAt` 근속 개월**로 근사 |
| compliance 패널 | **`TeamLeadQualificationCompliancePanel`** — **대상·자격 충족·실무경력 미달·입사일 미등록** StatCard · 직원별 표 · **`/staff/{id}`** HR 링크 (`574bd08`) |
| compliance API | **`GET /staff/team-lead-qualification/compliance?branchId=&referenceDate=`** — 지점별 집계 (`9a8bd2a`) |
| FE 저장 가드 | 선임 지정 시 **자격 미충족·입사일 미등록**이면 폼 **저장 차단** |
| **BE 서버 가드** | **`POST/PATCH /staff/lead-caregiver-logs*`** — **`TeamLeadQualificationCompliance.deriveStatus`** — 미충족 시 **`422 BUSINESS_RULE`** — **API 직접 호출·FE 우회 방지** (`726b3de`) |
| 입사일 없음 | **「입사일이 없어 팀장급 자격… 확인할 수 없습니다」** — HR **「입사~퇴사」** 탭에서 `hiredAt` 등록 필요 |
| 유틸 | FE **`teamLeadQualificationCompliance.js`** · BE **`TeamLeadQualificationCompliance.java`** — 동일 **60개월** 규칙 |

| P2 잔여 | **자격증·교육이수 서류 파일함 연동** · **실무경력 서류 기반 정밀 검증**(현재 입사일 근사) |

> 관련: Q284 · USER_MANUAL §5-9 · REQUIREMENTS FAQ21837

### [TWR] Q320. **모니터링 통합 checklist**(G30, FAQ21838~21842)는 어디서 보나요?

**A.** **Fixed (BE `b1dfd34`·`73df04d`·`344a28b` / FE `574bd08`·`73094f9`, G30·BNK-181·234·244)** — **`/compliance/monitoring`** 화면 **상단「통합 모니터링 checklist」** 패널에서 **선택 연·월** 기준 **8문항 자동 집계**를 확인합니다. **172차**에서 **FAQ21838 증빙 수집 기간(전전월 ±2개월)** 이 패널에 표시됩니다. **176차**에서 **FAQ21841 유선상담**은 **월 5명 + 60% 이상 만족(Y)** 기준으로 집계됩니다 (`V138` `satisfied`, Q365).

| 문항 | FAQ | 점검방향 (요약) |
|------|-----|----------------|
| 6 | FAQ21838 | 월별 **모니터링 자가진단** |
| 7 | FAQ21838 | **서명된 업무수행일지**(별지 제24호) |
| 8 | FAQ21839 | **월 1회 이상** 방문·면담 |
| 9 | FAQ21839 | **3개월 내 시정** 조치 |
| 10 | FAQ21839 | **RFID** 전송 (수동 점검) |
| 11 | FAQ21841 | **20분 이상** 면담 |
| 12 | FAQ21841 | **월 5명** 유선상담 · **60% 이상 만족(Y)** (`satisfied`, `344a28b`) |
| 13 | FAQ21842 | **직전 6개월** 자가진단 rolling |

| 항목 | 내용 |
|------|------|
| API | **`GET /api/v1/compliance/monitoring/checklist?branchId=&referenceYear=&referenceMonth=`** — 응답 **`evidenceWindowStart`·`evidenceWindowEnd`** (BE `MonitoringEvidenceWindow`, `73df04d`) |
| 증빙 기간 | **모니터링 실시 월의 전전월 ±2개월** — 예: 2026-06 → **2026-02-01 ~ 2026-06-30** |
| FE | **`MonitoringIntegratedChecklistPanel`** · **`resolveMonitoringEvidenceWindow`** — **증빙 기간 SR 노출** (`85bfb4a`) · **`fetchMonitoringIntegratedChecklistApi`** · **`monitoringCompliance.js`** |
| 상태 | **`MET`·`PARTIAL`·`UNMET`·`MANUAL`** — **RFID** 는 ogada v1에서 **MANUAL** 고정 |
| RBAC | **`hq_admin`·`branch_admin`·`social_worker`** |

| P2 잔여 | FAQ21812 **관리자 라운딩** · **live E2E verify** (`monitoringLiveApi.e2e.test.js`, merge 후 권장) |

> 관련: Q314 · USER_MANUAL §4-3 · ADMIN_GUIDE §6-2-11

### [TWR] Q321. **기관 교육일지 8-7**(G41/G41b, FAQ21807/21828)은 어디서 등록하나요?

**A.** **Fixed (BE `6191b91`·`0f11158`·`ee42e5d`·`345c0cb` / FE `f5658de`·`38d24b6`·`45a724a`, G41·G41b·BNK-184~188, US-S04)** — 케어포 **func.php `8-7.교육일지`** 를 **`/staff/training-logs`** 에서 등록·조회합니다. **보수교육(8-7-1)** 은 **`/staff/training`** (Q294). **`trainingType`** 입력은 BE에서 **`Locale.ROOT` 대문자 정규화**로 서버 locale에 관계없이 동일하게 검증됩니다 (`345c0cb`).

| 항목 | 내용 |
|------|------|
| 화면 | **`/staff/training-logs`** — **`StaffContextNav`** **「교육일지 (8-7)」** |
| G41 | **노인인권**(반기) · **운영규정**(연 1회 + **신규 7일**) |
| G41b | **재난·소화·직원권익** — 각 **연 1회** — **BE compliance StatCard Fixed** (BNK-185) |
| compliance API | **`GET /api/v1/staff/training-logs/compliance`** — G41b `*AnnualMet` · 신규 `newHireItems` · **지점 스코프** (`32f87f1`) |
| G41b StatCard | **`mapG41bComplianceCards`** — BE 우선 · 목록 fallback (`38d24b6`) |
| 등록 | **노인인권만 `referenceHalf`** · G41b·운영규정 연간은 **반기 없음** (V107, Q325) |
| RBAC | **`hq_admin`·`branch_admin`·`social_worker`** |
| DB | **V104–V107** |

| P2 잔여 | **대시보드 위젯** · **인쇄** · **G-STAFF-WELFARE(8-6, FAQ21796, P3)** |

> 관련: Q294 · Q325 · USER_MANUAL §5-14 · ADMIN_GUIDE §10-12 · DATA_RETENTION V107

### [TWR] Q325. G41b **연간 교육**에 반기(`referenceHalf`)를 넣으면 어떻게 되나요?

**A.** **Fixed (BE `ee42e5d` BNK-188 / FE `45a724a`)** — **운영규정(연간)·재난·소화·직원권익** 3+1종은 **연 1회** 집계이므로 **`referenceHalf`를 보내면 안 됩니다**.

| 규칙 | 내용 |
|------|------|
| 허용 `referenceHalf` | **노인인권(`ELDERLY_HUMAN_RIGHTS`)만** — `1`(상반기) 또는 `2`(하반기) |
| 거부 | G41b 3종 · 운영규정 연간 — **`referenceHalf` 포함 시 `422`** |
| DB | **Flyway V107** `chk_staff_training_logs_g41b_annual_no_half` — raw SQL 방어 |
| FE | **`buildStaffTrainingLogPayload`** — annual 유형은 **`referenceHalf` 생략** |

> 관련: Q321 · Q323 · USER_MANUAL §5-14 · DEPLOYMENT §3-6

### [TWR] Q326. ogada에서 **본인부담금 간편결제(7-5)** 를 지원하나요?

**A.** **예 (v2 P1 skeleton, BE `438f5c7`·FE `c9baca2`, US-L03·BNK-189)** — 케어포 **7-5**(view.npay_manage)에 대응하는 **카드·카카오페이** 간편결제 골격이 구현되었습니다. **요청·상태 API·화면**은 동작하나, 현재 **`StubEasyPayProvider`** 이므로 **실제 PG 결제창·승인은 없습니다** (live PG P2).

| 항목 | 내용 |
|------|------|
| API | **`POST/GET /api/v1/billing/easy-pay/claims/{claimId}/payment`** |
| 수단 | **`CARD`**(카드) · **`KAKAO_PAY`**(카카오페이) — **대소문자·공백 허용** 후 canonical 저장 (Q328) |
| UI | **`/billing/easy-pay`** — SideNav **청구 → 간편결제** · **`BillingContextNav`** 4탭 (Q203) · **US-L06 a11y** — 필드 오류·`<time>` 시각·결제 상태 섹션 (Q328) |
| 선행 | 청구 **`CONFIRMED`** · **단일 이용자** · **copay > 0** · **전월 미입금·G33 미정산 없음** (Q327) |
| 수납 연동 | 간편결제 **성공** 시 청구 **`PAID`** · `payment_method=EASY_PAY` (V108) · J03 **`BILLING_PAYMENT_RECEIVED`** |
| 연말정산 | **`EASY_PAY` 수납분은 의료비공제 집계 제외** (Q254) |
| 실연동 | **live PG 벤더** — P2 (DEPLOYMENT §4-6-1) |

> 관련: Q203 · Q327 · Q254 · USER_MANUAL §4-6 · ADMIN_GUIDE §10-14

### [TWR] Q327. 간편결제 요청 시 **「전월 미입금」** 으로 막히면 어떻게 하나요?

**A.** **Fixed (BE `b893e97`·FE `bebd874`, BNK-189)** — **7-5 간편결제**는 **월별 청구 생성 가드(Q310)와 동일한 선행입금 규칙**을 적용합니다. 전월 **`CONFIRMED` 미수납** 또는 **G33 청구시작 기준금액 미정산**이 있으면 **`422 BUSINESS_RULE`**(BE) · UI **`ClaimGenerationGuardBanner`** + **요청 버튼 비활성**(FE)입니다.

| 항목 | 내용 |
|------|------|
| BE | **`EasyPayService`** — **`BillingService.getClaimGenerationGuard(branchId, claim.yearMonth)`** |
| FE | **`EasyPayPanel`** — 청구 선택 시 **`fetchClaimGenerationGuardApi`** · 배너 제목 **「간편결제 제한 (7-5 선행입금 가드)」** |
| 조치 | 배너 **입금 처리**·**미납 관리** 링크 → **`/billing/payments`**·**`/billing/overdue`** 에서 선행 수납 |
| 케어포 대응 | **7-2(입금) 선행 → 7-5(간편결제)** workflow — **`ClaimGenerationGuardBanner`** 와 동일 **`LifecycleWorkflowPanel`** |

> 관련: Q310 · Q326 · Q328 · USER_MANUAL §4-6 · ADMIN_GUIDE §10-14

### [TWR] Q328. 간편결제 **provider 대소문자**·**화면 접근성(US-L06)** 은 어떻게 동작하나요?

**A.** **Fixed (BE `16a0734`·`82054f1`·`0cd8ea8`·`3dd94e6` / FE `51f2505`·`745a2f6`·`7ec7cd4`·`3a17543`, BNK-189~193·230 follow-up)** — 7-5 간편결제는 **API 입력 관용성**·**오입력 거부**·**WCAG 접근성**을 보강했습니다.

| 항목 | 내용 |
|------|------|
| **provider 정규화 (BE)** | **`EasyPayService.normalizeProvider`** — **`Locale.ROOT`** uppercase · `" card "`, `"kakao_pay"`, **`"kakao-pay"`**, **`"KAKAOPAY"`** 등 **대소문자·공백·하이픈** 수용 → **`CARD`·`KAKAO_PAY`** canonical 저장 (`0cd8ea8`) |
| **기존 성공 건 정규화 (QA-B93, `b45830d`·`3dd94e6`)** | **SUCCEEDED** 상태 **재조회** 시 DB에 **소문자·비정규 provider** 가 남아 있으면 **자동 canonicalize 후 저장** — 응답·후속 조회 일관성(self-heal) |
| **provider 정규화 (FE)** | **`normalizeEasyPayProvider`** — NFKC·전각(`ｋａｋａｏ pay`)·공백/하이픈 → `_` alias · **`KAKAOPAY`→`KAKAO_PAY`** · **`card1`·`kakao/pay`·`카카오페이` 등 malformed → 거부**(빈 문자열, 필드 오류) |
| **route alias (BE)** | **`POST/GET /api/v1/billing/easy-pay/claims/{claimId}`** — **`/payment` 경로와 동등** (`8f9ad0c`) |
| **V110 DB 무결성** | **`easy_pay_requests`** — 복합 Tenant FK · **퇴소·비활성 이용자 INSERT 차단** · lifecycle CHECK(PENDING/SUCCEEDED/FAILED) |
| **US-L06 a11y (FE)** | **`EasyPayPanel`** — **`Field` 필드 단위 오류**(청구·수단) · stub footnote·가드 배너 **`aria-describedby`** · **`<time dateTime>`** 요청·완료 시각 · **`.ds-easy-pay-status`** `<section role="status">` |

| **live routing E2E (BE, `1e21b20`)** | **`EasyPayLiveApiRoutingE2eTest`** — CARD·KAKAO_PAY **alias 경로**·status 재조회 provider 일관성 |

> 관련: Q326 · Q327 · USER_MANUAL §4-6 · ADMIN_GUIDE §10-14 · DEPLOYMENT §4-6-1

### [TWR] Q329. **22:00~08:00 조용한 시간대**에 청구 **보호자 발송**이 안 되면?

**A.** **Fixed (BE `328874d`·FE `111f056`, J03·BNK-193)** — ogada는 보호자 알림 **방해 금지 시간대**를 **Asia/Seoul 22:00~08:00** 로 고정합니다. **긴급(`EMERGENCY`)** 알림(예: 낙상 사고)만 **우회 발송**됩니다 (Q147).

| 항목 | 내용 |
|------|------|
| **BE 동작** | **`NotificationService.isQuietHoursAt`** — **22:00 ≤ 시각 < 08:00** KST · **non-emergency dispatch skip** · **`EMERGENCY` bypass** · 경계 **22:00·07:59** 단위 테스트 (`328874d`·`9a4ab8e`) |
| **readiness UI** | **`NotificationChannelReadinessPanel`** — **`quietHoursActive`** Badge (Q318) |
| **청구 UI (신규)** | **`BillingDetailPage`** — **「보호자 발송」·「납부확인서 발송」** 버튼 **비활성** + 상단 Alert · **`OverduePage`** — 행별 **「안내 발송」** **비활성** · **`notificationQuietHoursBlockedMessage()`** |
| **발송 0건 해석** | **`interpretBillingNotifyResult`** — quiet hours + 0건 → **「조용한 시간대… 발송 제한」** warning (무응답·설정 누락과 구분) |
| **조치** | **08:00 이후** 재시도 · 긴급 건은 **건강 기록 `FALL` 등 EMERGENCY** 경로 사용 |

> 관련: Q318 · Q147 · Q196 · USER_MANUAL §4-6 · ADMIN_GUIDE §10-8

### [TWR] Q330. 방문일정 **일괄확정**(G21 batch-confirm, FAQ21782)은 어떻게 하나요?

**A.** **Partial+ Fixed (BE `0b807d8`·`c22a5dc`·`230659a` / FE `d5ff3f8`·`13e691e`, G21·US-V04·BNK-197~198·213)** — **`/visits`** 하단 **`VisitBatchConfirmPanel`** 에서 **달력 표시 월·계획/청구 탭** 기준 **DRAFT 일정을 한 번에 확정**할 수 있습니다.

| 항목 | 내용 |
|------|------|
| 사전 점검 | **`GET /api/v1/visits/confirm-readiness`** — `draftCount`·`confirmedCount`·`unassignedDraftCount`·`pairedDivergedCount`·`ready`·`blockers[]`·`draftVisitIds[]` |
| **기간 필수 (BNK-213)** | **`POST /api/v1/visits/batch-confirm`** — **`fromDate`·`toDate` 필수** — 누락 시 **「일괄확정 기간(시작일/종료일)을 입력해주세요.」** (`422 BUSINESS_RULE`, `230659a`) · 종료일이 시작일보다 이르면 **「종료일은 시작일 이후여야 합니다.」** |
| 차단 조건 | **DRAFT 0건** · **페어 PLAN/BILLING 확정 상태 불일치** — `ready=false` · **담당자 미배정**은 **경고만**(일괄확정 가능) |
| 필수 확인 | Modal Checkbox 2종 — **`nhisComparisonAcknowledged`** · **`changeHistoryChecked`** — **모두 `true` 필수** — 미충족 **`422 BUSINESS_RULE`** |
| 실행 | **`POST /api/v1/visits/batch-confirm`** — 범위 내 **모든 DRAFT** → **`CONFIRMED`** (페어 확정 규칙 Q259 동일) |
| a11y | **UXD-102** — blockers·ack **`aria-describedby`** · **`VisitBatchConfirmPanel.test`** · **`pilotPageFlows`** G21 E2E |
| pilot E2E | **`VisitPilotServiceFlowE2eTest`** — batch-confirm **readiness→ack→confirm** flow coverage (`5edc45c`) |
| 권한 | **`branch_admin`·`social_worker`** — **`caregiver` 거부** |

| P2 잔여 | G21 **live E2E** · FAQ21782 **5단 전체 자동화** |

> 관련: Q259 · Q307 · USER_MANUAL §5-11 · ADMIN_GUIDE §10-12 · API_SPEC §14

### [TWR] Q331. SideNav **그룹 접힘/펼침**(US-UX-05)은 어떻게 동작하나요?

**A.** **Fixed (FE `1e111be`·`4ba7ea6`·`8a8b930`·`edfba7f`·`3845f0c`, US-UX-05, BNK-198~218)** — 좌측 **2단 SideNav** 5그룹(운영·이동·출석·기록·청구) 헤더를 클릭하면 하위 메뉴가 **토글**됩니다.

| 항목 | 내용 |
|------|------|
| 초기 상태 | **모든 그룹 접힘** — **현재 URL의 부모 그룹만** 자동 펼침 (`buildNavGroupExpandedState`) |
| route 변경 | **활성 route 부모 그룹** 펼침 상태 **재계산** — **`edfba7f`부터** 사용자가 **수동으로 펼친 다른 그룹은 닫히지 않고 유지** |
| **세션 유지 (`3845f0c`)** | **`sessionStorage`** 키 **`ogada:sidenav-expanded:{role}`** — **브라우저 탭 세션** 동안 수동 펼침 **복원** (AppShell remount 후에도) — **JWT와 별개**(JWT는 메모리 전용, Q82) |
| 다중 펼침 | **허용** — 한 그룹을 열어도 다른 그룹이 자동으로 닫히지 않음 |
| 접근성 | 그룹 헤더 **`aria-expanded`·`aria-controls`** · **`SideNav.test`** |
| 모바일 | collapsed 서브메뉴 **`aria-hidden`** (UXD-75, Q84) |

> 관련: Q84 · Q149 · USER_MANUAL §3-1 · USER_STORIES US-UX-05

### [TWR] Q332. 간편결제 **보호자 연결 무결성**(V111)과 J03 **조용한 시간대 정책 공유**는?

**A.** **Fixed (BE `dbecd72`·`a057739`, G2/7-5·J03, BNK-195~196)** — **Flyway V111** 과 **`NotificationQuietHoursPolicy`** 가 각각 **7-5 DB defense-in-depth**·**J03 dispatch/readiness 일관성**을 보강합니다.

| 항목 | 내용 |
|------|------|
| **V111 guardian link** | **`trg_easy_pay_requests_validate_guardian_link`** — `guardian_user_id` 지정 시 **`role_code=guardian`** · **`guardian_clients`** 로 **동일 이용자 연결** 필수 — 위반 시 INSERT/UPDATE **거부** |
| 배포 주의 | 기존 **`easy_pay_requests`** 행에 **orphan guardian** 이 있으면 V111 **마이그레이션 실패** — 배포 전 데이터 정합 필요 (DEPLOYMENT §8-1) |
| **J03 shared policy** | **`NotificationQuietHoursPolicy`** — **`NotificationService`**·**`NotificationChannelReadinessService`**·**`BillingService` manual notify** 가 **동일 22:00~08:00 KST** 규칙 사용 — UI readiness(`quietHoursActive`)와 **실제 발송 차단** drift 방지 (Q329) |
| 테스트 | **`NotificationServiceTest`** · **`J03BillingManualNotifyQuietHoursE2eTest`** · **`BillingServiceTest`** quiet-hours guard |

> 관련: Q326~Q329 · USER_MANUAL §4-6 · ADMIN_GUIDE §10-8·§10-14 · DEPLOYMENT §8-1

### [TWR] Q333. **인지활동형 프로그램 미제공 사유**(G17b, MOHW 2025-247 제32조)는 무엇인가요?

**A.** **Fixed (BE `6b7e6cb`·`ba7d84f`·`3bd6a43` / FE `c26cfa7`·`487416d`, G17b, BNK-198~203)** — 장기요양법 **제32조**에 따라 주야간보호 **인지활동형 프로그램을 제공하지 못한 경우**, 급여제공기록지에 **사유를 기재**해야 합니다. ogada는 **두 화면**에서 이를 강제합니다.

| 화면 | 경로 | 입력 방식 |
|------|------|----------|
| **프로그램 참여 기록** | `/programs` | **인지활동형(`COGNITIVE`)** + **불참(`ABSENT`)** 시 **4종 사유 Select 필수** |
| **기능회복훈련 계획** | `/programs/functional-recovery` | **「인지활동형 프로그램 제공」= 미제공** 시 **자유 서술 Textarea 필수** |

| 미제공 사유 코드 (참여 기록) | 화면 라벨 |
|------------------------------|----------|
| `STAFF_SHORTAGE` | 인력 부족 |
| `EQUIPMENT_FAILURE` | 시설·장비 장애 |
| `CLIENT_REFUSAL` | 수급자 거부 |
| `OTHER` | 기타 |

| 서버 규칙 (BE) | 내용 |
|----------------|------|
| 참여 + 사유 | **`ATTENDED`** 또는 **일반 프로그램 불참** — `skipReason` **입력 불가** → `422 BUSINESS_RULE` |
| 불참 + 만족도 | **`ABSENT`** — `satisfaction` **입력 불가** (`3bd6a43`) |
| 인지활동형 불참 | **`COGNITIVE` + `ABSENT`** — `skipReason` **필수** · 미입력·잘못된 코드 → `422` |
| 기능회복 계획 | **`cognitiveActivityProvided=false`** — `cognitiveActivityNotProvidedReason` **trim>0 필수** (V112 CHECK) |

> **DB**: Flyway **V112** `functional_recovery_plans` · **V113** `program_participations.skip_reason` — DEPLOYMENT §3-6·ADMIN_GUIDE §10-14.

> 관련: Q334 · Q335 · USER_MANUAL §5-9 · ADMIN_GUIDE §10-11·§10-11-1 · REQUIREMENTS G17b

### [TWR] Q334. 프로그램 관리 화면에서 **미제공 사유**는 어디에 보이나요?

**A.** **Fixed (FE `487416d`, G17b, BNK-203)** — **`/programs`** 참여 기록 **목록 표**에 **「미제공 사유 (G17b)」** 열이 추가되었습니다.

| 항목 | 내용 |
|------|------|
| 표시 조건 | **인지활동형 프로그램** + **불참** 기록만 사유 라벨 표시 — 그 외 **「—」** |
| 입력 폼 | **`ProgramParticipationForm`** — 불참 선택 + 인지활동형 프로그램 선택 시 **「인지활동형 미제공 사유 (G17b)」** `Field` Select 표시 |
| 필드 오류 | 미선택 시 「인지활동형 프로그램 미제공 사유를 선택하세요.」 — **`Field` render-prop** label·id 연결 (Q333) |
| 테스트 | **`ProgramsPage.test`** · **`ProgramParticipationForm.test`** · **`pilotPageFlows`** G17b E2E |

> 관련: Q333 · USER_MANUAL §5-9 · `config/programs.js` `COGNITIVE_ACTIVITY_SKIP_REASONS`

### [TWR] Q335. 기능회복훈련 계획의 **인지활동형 제공 여부**(G17b)는 어떻게 입력하나요?

**A.** **Fixed (BE `6b7e6cb` / FE `c26cfa7`, G17b, BNK-201~202)** — **`/programs/functional-recovery`** 계획 등록·수정 폼에 **인지활동형 프로그램 제공 Switch** 와 **미제공 사유 Textarea** 가 있습니다.

| 단계 | 조작 |
|------|------|
| 1 | **「인지활동형 프로그램 제공 (G17b)」** Switch — 기본 **제공** |
| 2 | **미제공** 선택 시 — **「인지활동형 미제공 사유 (G17b)」** Textarea **필수** — MOHW 제32조 안내 placeholder |
| 3 | **저장** — `POST/PATCH /api/v1/programs/functional-recovery/plans` — payload에 **`cognitiveActivityProvided`** · **`cognitiveActivityNotProvidedReason`** 포함 |
| 4 | 목록 **「인지활동형 (G17b)」** 열에서 **제공/미제공** Badge 확인 |

| API 필드 | 제공=true | 제공=false |
|----------|-----------|------------|
| `cognitiveActivityProvided` | `true` | `false` |
| `cognitiveActivityNotProvidedReason` | `null` (필수) | **비공백 문자열** (필수) |

> **P2 잔여**: 급여제공기록지 **PDF 자동 출력**에 G17b 사유 병기 — 현재는 화면·API 기록만.

> 관련: Q333 · Q262 · Q271 · USER_MANUAL §5-9 · ADMIN_GUIDE §10-11-1

### [TWR] Q336. **욕창 케어 lifecycle**(US-O03, G-NURSING)이란 무엇인가요?

**A.** v3.1 Must **6번째** 기능 — silverangel **「욕창위험도 연 1회+」**·**「14일 6대 수칙」**·케어포 demo L03 **간호급여 4 leaf** 패리티를 **4단 lifecycle**로 구현합니다 (BNK-203~204).

| 단계 | 화면 | 설명 |
|------|------|------|
| 1 | **위험평가** | Braden 6~23·위험도 `LOW`/`MODERATE`/`HIGH` |
| 2 | **예방계획** | 6대 수칙·장기요양이용계획서 반영 |
| 3 | **일별 간호 기록** | 부위·NPUAP 단계·처치·예방 조치 |
| 4 | **분기 코호트 리포트** | 분기별 집계·StatCard·인쇄 |

SideNav **기록 → 욕창 케어 (US-O03)** · **`/nursing/pressure-ulcer/*`** · 상단 **`NursingContextNav`** 4탭 · **`LifecycleWorkflowPanel`** 진행 표시.

> **G40·G40b와 구분**: 이용자 상세 **「위험도평가」** 탭의 **욕창(`PRESSURE_ULCER`)** 은 **입소 1회·반기 1회** 스크리닝(지표21·16)입니다. 본 lifecycle은 **간호급여 전용** 기록 — **별도 API·테이블(V114)**.

> 관련: Q337~Q339 · USER_MANUAL §5-15 · ADMIN_GUIDE §6-2-9 · REQUIREMENTS v3.1 Must

### [TWR] Q337. 욕창 **위험평가·예방계획**은 누가 등록하나요?

**A.** **`hq_admin`·`branch_admin`·`social_worker`** 만 위험평가·예방계획을 **등록·수정**할 수 있습니다. **`caregiver`** 는 **조회만** 가능합니다.

| 작업 | API | 필수 입력 |
|------|-----|----------|
| 위험평가 | `POST /api/v1/nursing/pressure-ulcer/assessments` | 이용자·평가일·위험도 등급 |
| 예방계획 | `POST /api/v1/nursing/pressure-ulcer/plans` | 선행 위험평가·6대 수칙·적용 시작일 |

**동일 이용자·동일 평가일** 중복 등록 시 **`422`** — 「해당 일자 욕창위험도 평가가 이미 존재합니다.」. Braden 점수는 **6~23** 범위 (FE·BE 이중 검증, `d638493`).

> 관련: Q336 · Q338 · USER_MANUAL §5-15 · `config/pressureUlcer.js`

### [TWR] Q338. **요양보호사**도 욕창간호 기록을 입력할 수 있나요?

**A.** **예.** **`caregiver`** 는 **`/nursing/pressure-ulcer/records`** 에서 **일별 간호 기록**을 **등록·수정**할 수 있습니다 (`POST/PATCH …/records`).

| 역할 | 위험평가·예방계획 | 간호 기록 | 분기 리포트 |
|------|:----------------:|:--------:|:----------:|
| `caregiver` | 조회만 | ✅ | ❌ |
| `social_worker` | ✅ | ✅ | ✅ |
| `branch_admin`·`hq_admin` | ✅ | ✅ | ✅ |

**부위**·**NPUAP 단계**·**처치 내용**(필수)을 **`Field` render-prop** 으로 입력 — 동일 날짜·동일 부위 중복 시 **`422`**.

> 관련: Q336 · USER_MANUAL §5-15·§6-1 · ADMIN_GUIDE §6-2-9 RBAC

### [TWR] Q339. **분기 코호트 리포트**는 어떻게 조회하나요?

**A.** **`/nursing/pressure-ulcer/reports`** — **`PressureUlcerCohortReportPanel`** (FE `e214da1`/`3ec39f6`).

1. **연도·분기**(Q1~Q4) 선택 → **조회**
2. **`GET /api/v1/nursing/pressure-ulcer/reports?year=&quarter=`** — 지점 스코프 코호트 집계
3. **StatCard** — 대상·평가 완료·예방계획·기록 보유·미완료
4. **표** — 이용자별 위험도·Braden·최근 NPUAP 단계
5. **인쇄** — 브라우저 인쇄 (`aria-label` 연도·분기 포함)

**`caregiver`·`guardian`** 은 분기 리포트 API **403**. **`hq_admin`·`branch_admin`·`social_worker`** 만 조회.

> **P2**: **PDF 공식 서식** · **`LIVE_E2E=1`** live backend harness (`pressureUlcerLiveApi.e2e.test.js`)

> 관련: Q336 · USER_MANUAL §5-15 · DEPLOYMENT §3-6 · BENCHMARK_REPORT §204

### [TWR] Q340. **통합 바이탈 점검**(L03_M11, G-NURSING)이란 무엇인가요?

**A.** 케어포 **view.total_vital_check** 대응 — 혈압·맥박·호흡·체온·SpO₂·체중·혈당을 **한 번에** 기록하는 간호급여 화면입니다 (BNK-207, FE `8570fa2`/BE `80c0bd5`).

| 항목 | 내용 |
|------|------|
| 화면 | **`/nursing/vital-checks`** — **`NursingVitalCheckPage`** |
| 네비 | SideNav **기록 → 통합 바이탈 (L03_M11)** · **`NursingContextNav`** 첫 탭 |
| API | **`GET/POST /api/v1/nursing/vital-checks`** · **`PATCH /{checkId}`** |
| DB | **Flyway V115** `nursing_vital_checks` |

> **`/health` 와 구분**: 일반 건강·투약·사건은 `/health` — 본 기능은 **간호급여 L03_M11 전용** (USER_MANUAL §5-16).

> 관련: Q341~Q342 · USER_MANUAL §5-16 · ADMIN_GUIDE §6-2-9a

### [TWR] Q341. 통합 바이탈은 **어떤 항목**을 입력하나요?

**A.** **`NursingVitalCheckForm`** — `Field` render-prop으로 label·id·서버 오류를 필드 단위 표시합니다.

| 구분 | 항목 | 범위·비고 |
|------|------|----------|
| 필수 | 이용자·점검일·점검 시각 | 동일 이용자·일시 **중복 불가** |
| 필수 | 수축기·이완기 혈압 (mmHg) | 60~250 / 30~150 · 수축기 > 이완기 |
| 필수 | 맥박 (회/분) | 30~200 |
| 필수 | 호흡수 (회/분) | 8~40 |
| 필수 | 체온 (°C) | 30.0~43.0 |
| 필수 | SpO₂ (%) | 50~100 |
| 선택 | 체중 (kg) | 20.0~200.0 |
| 선택 | 혈당 (mg/dL) | 30~600 |
| 선택 | 특이사항 | 자유 텍스트 |

정상 범위 이탈 시 **`vitalsRanges.js`** 경고가 표시되나 **저장은 허용**됩니다 (건강 기록 Q155와 동일).

> 관련: Q340 · USER_MANUAL §5-16 · `config/nursingVitalCheck.js`

### [TWR] Q342. **요양보호사**도 통합 바이탈을 입력할 수 있나요?

**A.** **예.** `hq_admin`·`branch_admin`·`social_worker`·**`caregiver`** 모두 **조회·등록·수정** 가능합니다 (`NursingVitalCheckController` `@PreAuthorize`).

1. **`/nursing/vital-checks`** — 최근 30일 목록 자동 로드
2. 좌측 폼에서 이용자·바이탈 입력 → **저장**
3. 목록 **수정** — 이용자·점검일·시각은 변경 불가
4. **`guardian`** 은 API **403**

> 관련: Q340 · USER_MANUAL §5-16·§6-1 · ADMIN_GUIDE §6-2-9a RBAC

### [TWR] Q343. **체중 관리**(L03_M14)는 화면이 있나요?

**A.** **예, Fixed** (BE `e95df4c`/`090b2d7` · FE `a7f97a6`/`97108f2`, **V116**, BNK-209).

| 화면·API | 용도 |
|----------|------|
| **`/nursing/weight-records`** — **`NursingWeightRecordPage`** | 체중 기록 목록·등록·수정 UI |
| `GET /api/v1/nursing/weight-records` | `fromDate`·`toDate`·`clientId` 목록 |
| `POST /api/v1/nursing/weight-records` | 측정일·체중(필수)·신장·목표체중·특이사항 |
| `PATCH /{recordId}` | 기존 기록 수정 |

동일 이용자·**동일 측정일** 중복 등록 시 `422 BUSINESS_RULE`. 통합 바이탈 폼의 **선택 체중**과 **별도 테이블**입니다.

1. SideNav **기록 → 체중 기록 (L03_M14)** 또는 **`NursingContextNav`** **체중 기록** 탭
2. 좌측 폼에서 이용자·측정일·체중(20~200 kg) 입력 → **저장**
3. 우측 목록에서 **BMI**·**전회 대비 변화량** 확인 · **수정** — 이용자·측정일 변경 불가

> 관련: Q340 · Q344 · USER_MANUAL §5-17 · ADMIN_GUIDE §6-2-9b

### [TWR] Q344. 간호급여 기록에 **미래 날짜**를 넣을 수 있나요?

**A.** **아니요.** FE·BE **이중 가드**로 **오늘 이후 점검일·측정일·발생일 입력을 차단**합니다 (QA-B85~B87, `090b2d7`/`97108f2`).

| 기능 | FE 검증 | BE 검증 | 오류 메시지 |
|------|---------|---------|------------|
| **L03_M11** 통합 바이탈 | **`validateCheckDateNotFuture`** (`nursingVitalCheckApiPayload.js`) | **`NursingVitalCheckService`** · injectable `Clock` | 「점검일은 오늘 이후로 입력할 수 없습니다.」 |
| **L03_M14** 체중 기록 | **`validateMeasureDateNotFuture`** (`NursingWeightRecordForm`) | **`NursingWeightRecordService`** | 「측정일은 오늘 이후로 입력할 수 없습니다.」 |
| **L03_M13** 구강상태 | **`validateCheckDateNotFuture`** (`NursingOralCareCheckForm`) | **`NursingOralCareCheckService`** | 「점검일은 오늘 이후로 입력할 수 없습니다.」 |
| **L03_M04** 응급상황 | **`validateOccurrenceDateNotFuture`** (`NursingEmergencyRecordForm`) | **`NursingEmergencyRecordService`** | 「발생일은 오늘 이후로 입력할 수 없습니다.」 |

> 관련: Q340 · Q343 · Q345 · Q346 · USER_MANUAL §5-16~§5-19 · ADMIN_GUIDE §6-2-9a~§6-2-9d

### [TWR] Q345. **구강상태 점검**(L03_M13) 화면은 어디에 있나요?

**A.** **Fixed (BNK-209, FE `bb3dee8`/`97108f2`, BE V118 `3540b4f`)** — SideNav **기록 → 구강상태 점검 (L03_M13)** 또는 **`/nursing/oral-care-checks`** 입니다.

| 항목 | 내용 |
|------|------|
| UI | **`NursingOralCareCheckPage`** · **`NursingOralCareCheckForm`** · **`NursingContextNav`** 8탭(구강상태 점검) |
| API | **`GET/POST/PATCH /api/v1/nursing/oral-care-checks`** — `apiFetch` only (`services.js`) |
| 필드 | **이용자·점검일·양치 도움·구강상태(`GOOD`/`FAIR`/`POOR`)** 필수 · **틀니 착용**·**특이사항** 선택 |
| 중복 | **이용자·점검일** 1건 — 중복 시 `422` 「해당 일자 구강상태 점검 기록이 이미 존재합니다.」 |
| 권한 | `hq_admin`·`branch_admin`·`social_worker`·`caregiver` |

> 관련: Q344 · USER_MANUAL §5-18 · ADMIN_GUIDE §6-2-9c · BENCHMARK_REPORT L03_M13

### [TWR] Q346. **응급상황 기록**(L03_M04)은 어디서 등록하나요?

**A.** **Fixed (BNK-211, FE `97108f2`, BE V119 `81bca68`)** — SideNav **기록 → 응급상황 기록 (L03_M04)** 또는 **`/nursing/emergency-records`** 입니다.

| 항목 | 내용 |
|------|------|
| UI | **`NursingEmergencyRecordPage`** · **`NursingEmergencyRecordForm`** · **`NursingContextNav`** 8탭(응급상황 기록) |
| API | **`GET/POST/PATCH /api/v1/nursing/emergency-records`** |
| 필드 | **이용자·발생일·응급 유형·조치내용** 필수 · **상세·보호자 통보·특이사항** 선택 |
| 유형 | `FALL`(낙상) · `CHOKING`(기도폐쇄) · `CARDIAC`(심장·호흡) · `SEIZURE`(경련) · `BLEEDING`(출혈) · `OTHER`(기타) |
| 중복 | **동일 이용자·동일 발생일 여러 건** 허용 (일자 UNIQUE 없음) |
| `/health` 낙상 기록 | **별도** — 일반 건강 incident API와 테이블 분리 |

> 관련: Q344 · USER_MANUAL §5-19 · ADMIN_GUIDE §6-2-9d · BENCHMARK_REPORT L03_M04

### [TWR] Q347. **배차 자동 제안**(v1.3-B suggest-run API)은 무엇인가요?

**A.** **BE·FE Fixed (BNK-212~214, BE `db94a65`·FE `2ffe59f`, 결정 75)** — **`POST /api/v1/transport/runs/suggest`** 로 당일 **픽업(PICKUP) 배차 명단**을 **OR-Tools VRP** 기반으로 **DRAFT 운행 루트**에 자동 배치합니다. **`/transport`** 화면 **`TransportSuggestPanel`**·**`BranchTransportSettingsPanel`** 에서 **`hq_admin`** 이 실행·설정합니다.

| 항목 | 내용 |
|------|------|
| 요청 | `{ runDate, direction: "PICKUP", vehicleIds?: UUID[] }` — **`direction`은 PICKUP만** 허용 |
| 권한 | **`hq_admin` only** — suggest·settings 모두 **`branch_admin`·직원 거부** |
| 상한 | **지점당 일 10회** (`ogada.transport.suggest-daily-limit-per-branch`, 기본 10) — 초과 시 **「오늘 자동 배차 제안 횟수(10회)를 초과했습니다.」** · UI에 **오늘 n/10회** 표시 |
| 전제 | **`uses_transport=true`** 이용자 roster · **좌표(geocode) 보유** 필수 — 미보유 시 **「좌표가 없는 이용자가 있습니다」** |
| 응답 | `runs[]`(차량별 DRAFT 루트) · `assignmentChanges` · `distanceSpreadKm` · `totalDistanceKm` · `suggestCountToday`·`suggestDailyLimit` |
| 설정 | **`GET/PUT /api/v1/transport/settings`** — 픽업 허용 ±분(기본 15) · OR-Tools 가중치 **w1 안정성 0.5 · w2 공정성 0.3 · w3 거리 0.2** |
| DB | **V120** `branch_transport_settings`·`transport_suggest_events` · **V122** integrity · **`clients.transport_notes`** |
| FE | **`TransportPage`** — **「자동 배차 제안」** → DRAFT 생성 → **DRAFT 검토** 링크 · **기존 DRAFT는 새 제안 시 대체** |

> 관련: Q159 · Q241 · USER_MANUAL §5-8 · ADMIN_GUIDE §10-10 · DEPLOYMENT §3-6 · DATA_RETENTION §2 transport_suggest_events 90일

### [TWR] Q348. **간호급여 제공기록**(L03_M01)은 어디서 입력하나요?

**A.** **FE+BE Fixed (BNK-215/217, FE `12591d4`, BE `9bd1660`, V123)** — SideNav **기록 → 간호급여 제공기록 (L03_M01)** 또는 **`/nursing/service`** 에서 등록·수정합니다.

| 항목 | 내용 |
|------|------|
| UI | **`NursingServiceRecordPage`** — **`NursingServiceRecordForm`** · **`NursingContextNav` → 제공기록** |
| API | **`GET/POST /api/v1/nursing/service-records`** · **`PATCH /{recordId}`** |
| 권한 | **`hq_admin`·`branch_admin`·`social_worker`·`caregiver`** |
| 필드 | **`nursingProvided`·`medicationProvided`·`medicalVisit`** 3-flag + 각 메모 · **`medicalInstitution`**(진료 시) |
| UNIQUE | **이용자×`serviceDate` 1건** — 중복 **422** |
| CHECK | **3-flag 중 최소 1개 true** · **`serviceDate` 오늘 이후 불가** |
| DB | **V123** `nursing_service_records` — composite FK·active-client guard |

> 관련: USER_MANUAL §5-20 · §5-22 제공 리포트 · ADMIN_GUIDE §6-2-9f · BENCHMARK_REPORT L03_M01

### [TWR] Q349. **배설·경관·유치도뇨 관리**(L03_M06)는 어디서 입력하나요?

**A.** **FE+BE Fixed (BNK-216/217, FE `12591d4`, BE `a4352a8`, V124)** — **`/nursing/excretion-tubes`** 또는 **`NursingContextNav` → 배설·경관** 에서 등록합니다.

| 항목 | 내용 |
|------|------|
| UI | **`NursingExcretionTubeRecordPage`** — **`NursingExcretionTubeRecordForm`** · **`NursingExcretionTubeReportPanel`** |
| 관 종류 | `EXCRETION`(배설) · `NG_TUBE`(비위관) · `URINARY_CATHETER`(유치도뇨관) |
| API | **`GET/POST /api/v1/nursing/excretion-tube-records`** · **`PATCH /{recordId}`** · **`GET …/reports`** |
| DB | **V124** `nursing_excretion_tube_records` · **V125** integrity triggers |

> 관련: USER_MANUAL §5-21 · ADMIN_GUIDE §6-2-9g · 케어포 `view.excretion_hose`

### [TWR] Q350. **간호급여 제공 리포트**(L03_M07/M09/M10)는 어디서 보나요?

**A.** **FE+BE Fixed (FE `2a05271`·`c97706b`, BE V123 report endpoints)** — **`/nursing/service/reports/*`** 3탭에서 기간·이용자별 집계를 조회합니다. BE가 **snake_case**(`nursing_notes` 등)만 반환해도 FE **`normalizeRecord`** 가 비고 열에 표시합니다 (`c97706b`).

| 경로 | PAM | API |
|------|-----|-----|
| `/nursing/service/reports/total` | L03_M07 | `GET …/service-records/reports/total` |
| `/nursing/service/reports/hospital-visits` | L03_M09 | `GET …/reports/hospital-visits` |
| `/nursing/service/reports/medication-delivery` | L03_M10 | `GET …/reports/medication-delivery` |

| UI | **`NursingServiceReportsPage`** · **`NursingServiceReportNav`** 3탭 · **`NursingServiceReportPanel`** |

> 관련: USER_MANUAL §5-22 · ADMIN_GUIDE §6-2-9h · §5-20 제공기록

### [TWR] Q351. **욕창간호 제공 리포트**(L03_M15)는 어디서 보나요?

**A.** **FE+BE Fixed (BNK-217, FE `efa4472`, BE `75bddee`)** — **`/nursing/pressure-ulcer/reports/provision`** 또는 **`NursingContextNav` → 욕창 제공 리포트** 에서 조회합니다.

| 항목 | 내용 |
|------|------|
| UI | **`PressureUlcerProvisionReportPanel`** on **`PressureUlcerPage`** |
| API | **`GET /api/v1/nursing/pressure-ulcer/reports/provision`** — alias `…/provisions` |
| 데이터 | L03_M01 욕창 **일별 간호 기록** 기반 제공 집계 — 케어포 `view.provide_YC_nursing` |
| a11y | 로딩 **`aria-busy`** · 인쇄 레이아웃 (`671a704`) |

> 관련: USER_MANUAL §5-15 5단 · ADMIN_GUIDE §6-2-9i · FAQ Q336~Q339 욕창 케어

### [TWR] Q352. 간호급여 기록 **과거 기간 조회** 시 날짜 범위는 어떻게 잡히나요?

**A.** **Fixed (BE `6b0238a`, L03, BNK-218)** — **L03_M01 제공기록**·**L03_M14 체중** 등 `fromDate`/`toDate` 필터 API는 **종료일(`toDate`) 기준**으로 시작일을 계산합니다.

| 입력 | 동작 |
|------|------|
| **둘 다 미지정** | `toDate` = **오늘** · `fromDate` = **오늘 − 90일** |
| **`toDate`만 지정**(과거 월 등) | `fromDate` = **`toDate − 90일`** — **오늘 기준이 아님** |
| **`fromDate`·`toDate` 모두 지정** | 그대로 사용 — `toDate < fromDate` 시 **422** |

| 영향 화면 | API |
|----------|-----|
| **간호급여 제공기록 (L03_M01)** | `GET /api/v1/nursing/service-records?fromDate=&toDate=` |
| **체중 기록 (L03_M14)** | `GET /api/v1/nursing/weight-records?fromDate=&toDate=` |
| **제공 리포트 (L03_M07/M09/M10)** | 동일 window 규칙 — 기간 선택 시 **해당 90일** 집계 |

> **현장 팁**: 3개월 이전 기록을 보려면 UI에서 **종료일을 해당 월 말일**로 먼저 선택하거나, API 호출 시 **`fromDate`·`toDate`를 명시**하세요.

> 관련: Q348 · Q343 · USER_MANUAL §5-20 · ADMIN_GUIDE §6-2-9f

### [TWR] Q353. **지점 도입 후 관리 체크list**(G-ONBOARD-SUPPORT)는 어디서 쓰나요?

**A.** **Fixed (FE `79d593c`·BE `735dd53`/`4c1fd43`/`43c4b08`, US-O05, BNK-223)** — SideNav **운영 → 지점**(`/branches`) → 지점 행 **「도입 체크list」** → Modal **`BranchOnboardingSupportPanel`**.

| 구분 | G-ONBOARD-SUPPORT (Q353) | 직원 입사 준수 (Q300) |
|------|--------------------------|----------------------|
| 대상 | **지점 1곳** 도입 SLA | **직원 1명** 입사 7종 서류·교육 |
| 화면 | **`/branches`** Modal | **`/staff`**·**`/staff/:id`** 패널 |
| API | `/branches/{id}/onboarding-support` | `/staff/hr-files/onboarding-compliance` |
| 근거 | silverangel businessSupport 1~4회차 | FAQ21806 |

| 역할 | 오픈일 설정 | 회차 체크·메모 |
|------|:-----------:|:-------------:|
| `hq_admin` | ✅ | ✅ |
| `branch_admin` | ✅ | ✅ |
| `social_worker` | ❌ | ✅ |

| 회차 | SLA | 항목 수(대표) |
|------|-----|-------------|
| 1회차 | 오픈 **+10일** | 20 — ID·권한·간호·프로그램·기록지 등 |
| 2회차 | 1회차 **+10일** | 13 — 사후관리·유선상담·보고서 활용 등 |
| 3회차 | 오픈 **+6주** | 1 — **직무교육** |
| 4회차 | 3회차 **+10일** | 2 — 묻고 답하기·KPI·계획평가달력 |

| API | 용도 |
|-----|------|
| `GET /api/v1/branches/{branchId}/onboarding-support` | 조회 — SLA `dueDate`·`StatusBadge`·StatCard |
| `PUT …/onboarding-support` | **`openedOn`** — SLA 기준일 (`hq_admin`·`branch_admin`) — **미래일·2000-01-01~2099-12-31 범위 밖 거부** (QA-B94, `43c4b08`) |
| `PATCH …/sessions/{roundNumber}` | **`completedItemKeys`**·**`notes`** — 회차별 저장 |

> **오픈일 검증 (QA-B94)**: `openedOn`이 **오늘 이후**이거나 **2000-01-01~2099-12-31** 밖이면 `422 BUSINESS_RULE` — SLA 기한이 잘못 계산되는 것을 방지합니다.

> **주의**: 회차 **메모**에는 개인식별정보를 적지 마세요. **기한 초과** 회차는 Modal 내 **경고 보더**·**「기한 초과」** Badge로 표시됩니다.

> 관련: USER_MANUAL §4-3 · ADMIN_GUIDE §6-2-10 · DATA_RETENTION §3 · USER_STORIES US-O05

### [TWR] Q354. **G24b 욕구사정 8-area 확장 필드**는 무엇인가요?

**A.** **Fixed (BE `45fb6d9`·FE `49fbf67`, G24b, BNK-225)** — 이지케어 [**FAQ 21800**](https://ezcare.easyms.co.kr/help/faq.ez?rowid=21800&type=web) **8 세부항목**과 1:1 대응하는 **5개 확장 필드**가 V84 기본 8항목 위에 추가되었습니다.

| G24b 필드 (V128) | 폼 라벨 | FAQ21800 영역 |
|------------------|---------|---------------|
| `disease` | 질병상태 | 과거병력·진단명 |
| `communication` | 의사소통 | 청취·발음 |
| `nutrition` | 영양상태 | 기피식품·섭취·배설 |
| `livingEnvironment` | 환경상태 | 거주환경·수발부담 |
| `resourceUtilization` | 자원이용 욕구 | 의료기관·사회복지기관 |

| 구분 | 내용 |
|------|------|
| 화면 | **`/clients/:id`** **「기초평가」** 탭 — **`ClientNeedsAssessmentForm`** |
| API | **`PUT /api/v1/clients/{clientId}/needs-assessments`** — DTO 5필드 추가 |
| DB | **Flyway V128** — `client_needs_assessments` 5 TEXT columns |
| G34b 연동 | **`GET /staff/lead-caregiver-logs/import-draft?source=needs_assessment`** — 불러오기 초안에 G24b 5항목 포함 (`45fb6d9`) |
| 테스트 | **`ClientNeedsAssessmentServiceTest.upsertAssessmentShouldPersistG24bExtendedFields`** · FE **`needsAssessmentForm.test`**·**`ClientNeedsAssessmentForm.test`**·**`ClientNeedsAssessmentCompare.test`** (`8989bf4`) · **`clientLifecycleLiveApi.e2e.test.js`** |

| P2 잔여 | FAQ21800 **연간 리포트 일괄 출력** |

> 관련: Q286 · Q355 · Q303 · USER_MANUAL §3-3 · ADMIN_GUIDE §6-2-6a · DATA_RETENTION §2 V128

### [TWR] Q355. **G24b 연간 욕구사정 compliance**는 어떻게 확인하나요?

**A.** **Fixed (BNK-226~229, BE `98002d4`·`f4c8beb` / FE `ca0b627`·`baa6d6d`)** — 이지케어 [**FAQ 21800**](https://ezcare.easyms.co.kr/help/faq.ez?rowid=21800&type=web) **연 1회 가정방문 욕구사정** 준수를 **지점·회계연도** 단위로 집계합니다. **대시보드 StatCard 2종**도 연동되었습니다 (Q356).

| 항목 | 내용 |
|------|------|
| API | **`GET /api/v1/clients/needs-assessments/compliance?fiscalYear=&branchId=`** |
| 권한 | **`hq_admin`·`branch_admin`·`social_worker`** — `caregiver` **403** |
| 집계 | 활성 이용자별 **`annualComplete`** — 회계연도 기록 존재 + **가정방문 일자** + **G24b 5필드 전부** + **등급 변경 재평가 미필요** |
| gap 사유 | **`missingG24bFields[]`** — `disease`·`communication`·`nutrition`·`livingEnvironment`·`resourceUtilization` · **`gradeChangeReassessmentDue`** — 평가 이후 회계연도 내 등급 변경(시행령 제13조제5항) |
| **대시보드 (FE)** | **`/dashboard`**·**`/dashboard/hq`** — **「연간 욕구사정 미완료」**·**「등급변경 재사정 필요」** StatCard — 클릭 **`/clients/needs-assessments`** (Q357, `b5af5fa`) · 스냅샷 누락 시 **`fetchNeedsAssessmentComplianceApi`** 병렬 폴백 |
| 응답 | `fiscalYear`·`totalClients`·`compliantCount`·`gapCount`·`items[]` — `clientId`·`clientName`·`hasRecord`·`homeVisitDate` |
| 검증 | **`fiscalYear` 2000~2100** 범위 밖 → `422` (`f4c8beb`) |
| 테스트 | **`ClientNeedsAssessmentServiceTest.getCompliance*`** · FE **`DashboardPage.test`** · **`needsAssessmentComplianceLiveApi.e2e.test.js`** |

| P2 잔여 | FAQ21800 **연간 리포트 일괄 출력** |

> 관련: Q286 · Q354 · Q356 · Q357 · USER_MANUAL §4-2·§4-3 · ADMIN_GUIDE §6-2-6a

### [TWR] Q356. **G24b 대시보드 위젯**과 **G41 FAQ21808 교육 28종**은 어떻게 동작하나요?

**A.** **G24b dashboard ✅ full (FE `ca0b627`·`baa6d6d`, BNK-227~229)** · **G41 V129 △ BE Fixed (BE `b1c92e1`, BNK-229)** — 170차에서 **지표15 gap 가시화**와 **교육일지 enum 확장**이 반영되었습니다.

| 구분 | 항목 | 내용 |
|------|------|------|
| **G24b FE** | 위젯 | **`DashboardPage`** — **`hq_admin`·`branch_admin`·`social_worker`** — **「연간 욕구사정 미완료」**·**「등급변경 재사정 필요」** StatCard · **`needsAssessmentCompliance.js`** |
| **G24b FE** | 폴백 | 대시보드 스냅샷에 **`needsAssessmentGapCount`·`gradeChangeReassessmentDueCount`** 없으면 **`fetchNeedsAssessmentComplianceApi(현재연도, branchId)`** 병렬 호출 |
| **G24b FE** | 실패 UX | compliance API 실패 시 **「일부 준수지표를 불러오지 못했습니다: 연간 욕구사정 준수」** warning — 나머지 위젯 유지 |
| **G41 BE** | V129 | **`staff_training_logs.training_type` CHECK 28종** — 기존 5종 + **운영규정 11**(`OP_REG_*`) + **급여제공지침 12**(`GUIDELINE_*`) — 이지케어 **FAQ21808** 23 topics parity |
| **G41 BE** | 규칙 | **`ELDERLY_HUMAN_RIGHTS` 외 27종** — **`reference_half` NULL** (연간) · API **`Locale.ROOT` uppercase** 유지 |
| **G41 FE** | P2 | **`staffTrainingLogs.js`** Modal 드롭다운은 **5종**만 — V129 세부 23종 UI wire 잔여 |

| P2 잔여 | G41 **FE dropdown 28종** · FAQ21800 **연간 리포트 일괄 출력** · **QA-B95** `./scripts/run-live-e2e.sh` 1회 RUN 확인 (guardian bootstrap fallback @ `b3bd0cc`) |

> 관련: Q321 · Q325 · Q355 · Q357 · USER_MANUAL §4-2·§5-3 · ADMIN_GUIDE §6-2-12 · DATA_RETENTION §2 V129

### [TWR] Q357. **G24b 연간 욕구사정 현황 화면**과 **G19 통합재가 기관 검색 안내**는 어디서 보나요?

**A.** **G24b status ✅ full (FE `b5af5fa`, US-T09, BNK-231)** · **G19 provider discovery ✅ full (BE `f44ee73`/`41d8de5` · FE `9afa30e`)** — 171차에서 **G40b 패턴 현황 화면**과 **롱텀 포털 검색 가이드**가 연동되었습니다.

| 구분 | 화면·API | 내용 |
|------|----------|------|
| **G24b 현황** | **`/clients/needs-assessments`** | SideNav **이용자 → 「연간 욕구사정 현황 (G24b)」** · **`NeedsAssessmentStatusPage`** — 회계연도(2000~2100)·**「조치 필요만」**/`전체` 필터 · StatCard 4종 · 이용자별 **가정방문 일자**·**연간 사정**·**등급변경 재사정**·**미기록 G24b 항목** · **「욕구사정」** 링크 → **`/clients/:id`** 기초평가 탭 |
| **G24b 역할** | RBAC | **`hq_admin`·`branch_admin`·`social_worker`** 조회 · **`caregiver`·`guardian`** 접근 불가 |
| **G24b 대시보드** | StatCard | **「연간 욕구사정 미완료」**·**「등급변경 재사정 필요」** 클릭 → **`/clients/needs-assessments`** (이전 `/clients`에서 변경, `ca0b627` carry) |
| **G19 검색 안내** | **`/branches`** 등록 모달 | **`INTEGRATED_HOME`** 선택 시 **`IntegratedHomeProviderDiscoveryPanel`** — **`ds-dl-grid`** 레이아웃·스크린리더 라벨 (`85bfb4a`) — prefilled [**롱텀 포털 검색**](https://www.longtermcare.or.kr/npbs/r/a/201/selectLtcoSrch.web?menuId=npe0000002783) 새 탭 링크 |
| **G19 live E2E** | harness | **`integratedHomeProviderDiscoveryLiveApi.e2e.test.js`** (`98102c3`) · BE **`IntegratedHomeProviderDiscoveryPilotServiceFlowE2eTest`** (`4aac676`) |
| **G19 필터** | API 응답 | `ltcAdminKindChoiceYn8=Y` · `searchAdminKindCd=06`(주야간보호) · `07`(단기보호) · `monthlyAddonNotice` 가산 안내 |

| P2 잔여 | FAQ21800 **연간 리포트 일괄 출력** · G41 **FE dropdown 28종** · **QA-B95** — bootstrap enabled + `./scripts/run-live-e2e.sh` 1회 RUN 확인 (`b3bd0cc`) |

> 관련: Q223 · Q355 · Q356 · USER_MANUAL §4-3·§5-3 · ADMIN_GUIDE §6-2-6a · DEPLOYMENT_GUIDE §3-6

### [TWR] Q357-1. G24b/G19가 실제 서버에서 정상인지 가장 빠르게 확인하는 방법은?

**A.** 운영 계정 토큰으로 아래 2개 API만 호출해도 Must 핵심 동작을 1분 내 확인할 수 있습니다.

```bash
curl -sS -H "Authorization: Bearer <ACCESS_TOKEN>" \
  "https://<host>/api/v1/clients/needs-assessments/compliance?fiscalYear=2026" | jq

curl -sS -H "Authorization: Bearer <ACCESS_TOKEN>" \
  "https://<host>/api/v1/branches/integrated-home/provider-discovery" | jq
```

| API | 정상 확인 포인트 |
|-----|------------------|
| `GET /clients/needs-assessments/compliance` | `gapCount`·`items[].missingG24bFields`·`items[].gradeChangeReassessmentDue` 존재 |
| `GET /branches/integrated-home/provider-discovery` | `providerSearchUrl`·`integratedHomeFilterParam`·`daytimeCareServiceCode`·`shortTermCareServiceCode` 존재 |

> `403 FORBIDDEN_SCOPE`가 나오면 토큰 역할/지점 스코프를 먼저 확인하세요 (`hq_admin` 또는 지점 범위가 맞는 `branch_admin`·`social_worker`).

추가로 운영 점검을 확장하려면 아래 2개를 더 확인하세요.
- `GET /api/v1/staff/training-logs/compliance?referenceYear=2026`
- `GET /api/v1/billing/easy-pay/claims/{claimId}/payment`

### [TWR] Q358. **급여제공결과 평가** 화면에서 **월간 급여제공기록지**를 보호자에게 내려면?

**A.** **Fixed (FE `4d1a4f2`·BE `73df04d`, G39 / US-T08 / BNK-234, 지표44 pillar 2)** — 이전에는 이용자 상세 **「급여제공」** 탭(Q243)에서 **조회만** 가능하고, 평가 화면에서는 compliance **미제공 건수만** 표시되었습니다. **172차**부터 **`/programs/provision-result-evaluations`** 에 **발송 패널**이 연동되었습니다.

| 항목 | 내용 |
|------|------|
| 표시 조건 | **`hq_admin`·`branch_admin`·`social_worker`** · compliance에서 **`monthlyProvisionRecordProvidedMet === false`** 인 이용자가 1명 이상 |
| UI | **`ProvisionResultDispatchPanel`** — **발송 대상 연월**(`MonthInput`) · 미제공 이용자 표 · 행별 **「기록지 발송」** 버튼 · **행 `aria-label`·상태 Badge** (`85bfb4a`) |
| API | **`POST /api/v1/clients/{clientId}/notifications/care-provision-record`** — body `{ "yearMonth": "YYYY-MM" }` |
| 템플릿 | **`CARE_PROVISION_RECORD`** — subject **`[ogada] 급여제공기록지 안내`** (Q216) |
| quiet-hours | **22:00~08:00 KST** non-emergency 발송 차단 가능 — FAQ Q329 |
| 발송 후 | 지표44 pillar 2 compliance·대시보드 **「월간 기록지 미제공」** 위젯 갱신 |

| 오류 | 원인·조치 |
|------|----------|
| 패널 미표시 | 미제공 이용자 없음 · 권한 부족(`caregiver`) · 활성 지점 미선택 |
| `422` | 연월 형식 오류 · 보호자 미연결 · quiet-hours |

| 테스트 | **`ProvisionResultDispatchPanel.test.jsx`** · **`ProvisionResultEvaluationPage.test.jsx`** · **`CareProvisionRecordDispatchPilotServiceFlowE2eTest`** · **`careProvisionRecordDispatchLiveApi.e2e.test.js`**

> 관련: Q216 · Q243 · Q276 · USER_MANUAL §5-9 · ADMIN_GUIDE §10-11-3

### [TWR] Q359. **집중배설관찰**(L02_M02, 케어포 2-2)은 어디서 기록하나요?

**A.** **✅ full Fixed (FE `1264c16`·BE `fd42b7e`, L02 v3.1 Must / BNK-239)** — SideNav **기록 → 집중배설관찰 (L02_M02)** 또는 **`/care/intensive-excretion`** 에서 등록·조회·수정합니다.

| 항목 | 내용 |
|------|------|
| 대응 | 케어포 **`view.care_excretion`** (2-2 집중배설관찰) |
| 화면 | **`IntensiveExcretionObservationPage`** — 목록 표 + **`IntensiveExcretionObservationForm`** |
| API | **`GET/POST/PATCH /api/v1/care/intensive-excretion-observations`** (`apiFetch` 경유) |
| 권한 | `hq_admin`·`branch_admin`·`social_worker`·`caregiver` — **활성 지점 필수** |
| 배설 유형 | `URINATION` · `DEFECATION` · `BOTH` |
| 배변 상태 | `NORMAL`·`LOOSE`·`HARD`·`BLOODY`·`OTHER` — **소변 관찰 시 입력 불가** |
| 필수 검증 | **관찰내용·조치내용 중 1개 이상** · **관찰일 미래 불가** |
| 조회 기간 | `fromDate`·`toDate` 생략 시 **최근 90일** |
| DB | **Flyway V130** `intensive_excretion_observation_records` |

| 구분 | L02_M02 (요양기록) | L03_M06 (`/nursing/excretion-tubes`) |
|------|-------------------|--------------------------------------|
| 모듈 | 요양기록 L02 | 간호급여 L03 |
| 내용 | 집중 배설 **관찰·조치** | 배설관리·경관·유치도뇨 **간호 기록** |
| UI | **있음** (`/care/intensive-excretion`) | **있음** |

| 테스트 | **`IntensiveExcretionObservationPage.test`** · **`IntensiveExcretionObservationForm.test`** · **`intensiveExcretionObservationServices.test`** · **`intensiveExcretionObservationLiveApi.e2e.test.js`** · BE **`IntensiveExcretionObservationPilotServiceFlowE2eTest`**

> 관련: USER_MANUAL §5-23 · ADMIN_GUIDE §6-2-13 · REQUIREMENTS L02 v3.1 Must

### [TWR] Q360. **`npm run test:live-e2e`** 가 전부 skip 되거나 API 연결 오류가 나요.

**A.** **Fixed (BE `6bd16b9`·`8b7e476`·`e4c240f`·`221bde7`·`a25c9de`·`472cb1d`·`aa6816a`·`c5f1325`·`8a92179`·`f6f1756`·`304bb2a`·`f5205e3`·`ec142db`·`22396e0`·`b1a6aff`·`440ed84`·`d8d51a7`·`8a1f342`·`2926287`·`c13800c` / FE `5f17beb`·`10f32c4`·`61141a6`·`4299914`·`3a14caf`·`9006a53`·`e10113f`·`64f6753`·`7106106`·`b23f5bf`·`b3bd0cc`·`4e99ae1`·`ddd4489`·`6f2a4eb`·`825c6b0`·`b69c8ae`·`af4d7f8`, QA-B96/SEC-D29/QA-B95 deepen)** — live E2E는 기동 전 **`GET /api/v1/health`** readiness를 1회 조회합니다. 백엔드가 꺼져 있거나 DB가 내려가면 **FAIL 대신 SKIP** 으로 보고합니다. **`c13800c`** — 재사용 dev DB에서 시드 이용자 insert 충돌 시 **`ensureClientWithFallback`** 이 동일 tenant·지점 **기존 이용자**를 재사용해 bootstrap **HTTP 500** 을 방지합니다. **`af4d7f8`** — staff bootstrap 응답에 **`guardianAccessToken`/`guardianRefreshToken`/`guardianEmail`** 이 포함되면 **`bootstrap-guardian` 2차 호출 없이** guardian suite creds를 채웁니다. **`2926287`** — health 응답에 **`liveE2eClientReady`·`liveE2eSeedClientId`** 가 추가되어 probe 없이도 **시드 이용자 존재 여부**를 확인할 수 있습니다. **`8a1f342`** — probe가 guardian bootstrap 전 **seeded client** 를 노출합니다. **`825c6b0`** — staff bootstrap **`clientId`** 를 guardian auth 전에 persist합니다. **`221bde7`** 에서 **인증 없이** **`GET /api/v1/system/live-e2e/probe`** 로 bootstrap readiness·status/bootstrap endpoint 경로를 preflight 할 수 있습니다. **`a25c9de`** — probe 응답에 **`organizationReady`·`branchReady`·`userReady`·`mappingReady`** 구조화 플래그가 추가되어 bootstrap 실패 원인을 `detail` 문자열 파싱 없이 확인할 수 있습니다. **`c5f1325`** — probe·health 응답에 **`credentialsConfigured`** 가 추가되어 **staff/guardian creds 미설정**과 **백엔드 readiness 실패**를 구분할 수 있습니다. **`f5205e3`** — probe에 **`guardianReady`·`guardianBootstrapEndpoint`**·**`guardianCredentialsConfigured`** 가 추가되었고, **`POST /api/v1/system/live-e2e/bootstrap-guardian`** 으로 보호자·연결 이용자·토큰을 시드할 수 있습니다. **`b3bd0cc`** — guardian env 미설정 시 **`liveGlobalSetup`** 이 **`bootstrap-guardian`** 을 호출해 **`LIVE_E2E_GUARDIAN_*`·`LIVE_E2E_CLIENT_ID`** 를 자동 채웁니다. **`4e99ae1`** — **`resolveGuardianClientId`** 가 psql 등으로 채워진 **stale `LIVE_E2E_CLIENT_ID`** 를 guardian-linked client보다 우선하지 않도록 정합합니다. **`22396e0`** — **V147** guardian link trigger가 **`updated_at ≥ created_at`** 을 보장해 bootstrap 시 **`clients` 제약 위반**을 방지합니다. **`b1a6aff`** — staff bootstrap 시 **legacy onboarding support row**를 재사용·**`organizationId` backfill** 합니다. **`440ed84`/`d8d51a7`** — staff bootstrap이 **`ensureClient`** 로 live-e2e 이용자를 **항상 시드**하고 **`LiveE2eBootstrapResponse.clientId`** 를 반환합니다. probe에 **`clientReady`·`seedClientId`** 가 추가되어 harness preflight에서 이용자 시드 여부를 확인할 수 있습니다. **`ddd4489`** — bootstrap endpoint가 **HTTP 500/503** 이더라도 env에 유효 creds가 있으면 **`POST /auth/login` fallback** 으로 suite를 **SKIP하지 않고** 진행합니다 (`login-fallback-ok`). **`6f2a4eb`** — **`pilotLivePages.e2e.test.jsx`** 가 **`AuthProvider` passthrough** 로 `restoreSession` jsdom race를 제거해 **`npm run test:live-e2e`** 가 **118 passed / 0 unhandled errors** 로 완료됩니다. **`7106106`** — **`dev-live-e2e.env.example`** 의 placeholder 값은 **configured=false** 로 처리되어 **false login probe** 를 방지합니다. **`304bb2a`/`f6f1756`** — bootstrap endpoint가 **`ResponseStatusException`** 을 **500 대신 선언 status(503 등)** 로 반환하도록 수정되어 staff bootstrap **HTTP 500** 회귀가 해소되었습니다. **`b69c8ae`** — stale shell **`LIVE_E2E_*`** env 오염 regression 해소 (FAQ **Q408**).

| 증상 | 원인 | 조치 |
|------|------|------|
| 전 suite **SKIP** | `LIVE_E2E` 미설정 · health `ready=false` · **ECONNREFUSED** | 백엔드 기동(`mvn spring-boot:run`) · PostgreSQL 연결 확인 |
| env **미로드** (checkout 경로) | `frontend-test` 등 서브모듈에서 실행 | **`61141a6`** — git root `scripts/` 자동 resolve |
| authenticated suite **SKIP** | `LIVE_E2E_EMAIL`/`PASSWORD`·`LIVE_E2E_CLIENT_ID`·guardian creds 미설정 | `scripts/dev-live-e2e.env` 설정 (`a5e7722`/`8ae34f5`) · **`b3bd0cc`** — bootstrap enabled 시 **`bootstrap-guardian`** 자동 fallback |
| authenticated suite **SKIP** (env 있음) | staff/guardian **로그인 probe 실패** · **placeholder creds** · **bootstrap disabled** · **stale `LIVE_E2E_CLIENT_ID`** · **client 미시드** | `4299914`/`64f6753` — 백엔드 기동·시드 계정·비밀번호 확인 · **`7106106`** — example placeholder는 configured=false · **`4e99ae1`** — guardian-linked client와 env `clientId` 불일치 시 **`resolveGuardianClientId`** · **`GET /api/v1/system/live-e2e/probe`** — `organizationReady`·`credentialsConfigured`·**`guardianReady`·`clientReady`·`seedClientId`** 확인 (`c5f1325`/`f5205e3`/`d8d51a7`) |
| **bootstrap HTTP 500/503** (env creds 있음) | bootstrap endpoint 오류 · bean wiring 불일치 | **`ddd4489`** — **`liveGlobalSetup`** 이 **`login-fallback-ok`** 로 env creds 재로그인 시도 · **`304bb2a`/`f6f1756`** — **`GlobalExceptionHandler`** status 매핑 · probe **`ready=false`** 시 **`503`** 확인 |
| **503 DEGRADED** | DB down | `DB_URL`·DB 기동 확인 후 `/api/v1/health` 재조회 · `databaseStatusDetail` 확인 |
| env 파일 없음 | **QA-B95** | `cp scripts/dev-live-e2e.env.example scripts/dev-live-e2e.env` |
| suite **SKIP** (setup marked skipped) | **`liveGlobalSetup`** probe **`skipped=true`** persist | **`9006a53`** — bootstrap/probe 실패 후 **명시적 skip 플래그** · creds 교체·백엔드 재기동 후 재실행 |
| cross-tenant bootstrap collision | 시드 이메일이 **다른 Organization** 에 이미 존재 | **`472cb1d`** — bootstrap이 user **org 재할당하지 않음** · env 이메일·시드 tenant 일치 확인 |
| env **값 미적용** (파일은 있음) | **`export KEY=...`** · **`${VAR:-default}`** 구문 미파싱 | **`e10113f`** — **`liveGlobalSetup`** 이 shell export·default 구문을 Node에서 직접 해석 · `scripts/dev-live-e2e.env` 재확인 |
| harness **false positive** (shell env 오염) | 이전 **`run-live-e2e.sh`**·shell에 stale **`LIVE_E2E_*`** 잔존 | **`b69c8ae`** — **`liveE2eHarness.test`** env isolation · **새 터미널**에서 재실행 (FAQ **Q408**) |
| **bootstrap HTTP 500** (reused dev DB) | 시드 이용자 **`LIVE-E2E-0001`** 중복 insert 충돌 | **`c13800c`** — **`ensureClientWithFallback`** 이 동일 tenant·지점 **기존 이용자 재사용** (FAQ **Q409**) |
| guardian bootstrap **2회 호출** | staff bootstrap 응답에 guardian token embedded | **`af4d7f8`** — **`liveGlobalSetup`** 이 embedded token 재사용 · **`bootstrap-guardian` 생략** (FAQ **Q409**) |

**readiness 응답 예** (`ready=true`, HTTP 200):

```json
{"status":"UP","ready":true,"service":"ogada-backend","databaseStatus":"UP","databaseStatusDetail":"SELECT_1_OK","liveE2eClientReady":true,"liveE2eSeedClientId":"00000005-0005-4000-8000-000000000001",...}
```

**liveness ping** (`GET /api/v1/health/ping`, HTTP 200, DB 무관):

```json
{"status":"UP","service":"ogada-backend","timestamp":"..."}
```

**live E2E probe** (`GET /api/v1/system/live-e2e/probe`, HTTP 200, 인증 없음):

```json
{
  "backendUp": true,
  "bootstrapEnabled": true,
  "ready": true,
  "detail": "organization=present branch=present user=present mapping=present",
  "organizationReady": true,
  "branchReady": true,
  "userReady": true,
  "mappingReady": true,
  "credentialsConfigured": true,
  "guardianCredentialsConfigured": true,
  "guardianReady": true,
  "guardianDetail": "guardian-user=present client=present mapping=present",
  "clientReady": true,
  "seedClientId": "00000005-0005-4000-8000-000000000001",
  "statusEndpoint": "/api/v1/system/live-e2e/status",
  "bootstrapEndpoint": "/api/v1/system/live-e2e/bootstrap",
  "guardianBootstrapEndpoint": "/api/v1/system/live-e2e/bootstrap-guardian"
}
```

| 테스트 | **`HealthControllerTest`** · **`LiveE2eControllerTest`** (`221bde7`/`a25c9de`/`aa6816a`/`304bb2a`/`d8d51a7`) · **`LiveE2eControllerRoutingTest`** · **`LiveE2eBootstrapLiveApiRoutingE2eTest`** (`440ed84`) · **`GlobalExceptionHandlerTest`** · **`LiveReadinessProbeTest`** · **`ProductionSecretValidatorTest`** · FE **`liveE2eHarness.test.js`** (`ddd4489`) · **`pilotLivePages.e2e.test.jsx`** (`6f2a4eb`) · **`liveGlobalSetup.js`**

> **prod 주의 (Q384)**: **`SPRING_PROFILES_ACTIVE=prod`** 에서 live E2E bootstrap 플래그가 켜져 있으면 **기동 자체가 거부**됩니다.

### [TWR] Q384. **운영(prod) 환경**에서 live E2E bootstrap을 켤 수 있나요?

**A.** **Fixed (BE `aa6816a`, SEC, BNK-272, Q384)** — **불가능합니다.** `prod` 프로필 기동 시 **`ProductionSecretValidator`** 가 다음 중 하나라도 `true` 이면 **`IllegalStateException`** 으로 **fail-fast** 합니다.

| 환경변수·설정 | 의미 |
|--------------|------|
| `LIVE_E2E=true` | live E2E 전역 플래그 |
| `LIVE_E2E_BOOTSTRAP_ENABLED=true` | bootstrap endpoint 활성 |
| `ogada.live-e2e.bootstrap-enabled=true` | Spring property bootstrap 활성 |

**추가 보안 (동일 커밋)**: **`POST /api/v1/system/live-e2e/bootstrap`** 응답 **`LiveE2eBootstrapResponse`** 에서 **평문 `password` 필드가 제거**되었습니다. dev/staging에서 bootstrap을 사용할 때도 **비밀번호는 env(`ogada.live-e2e.password`)·문서**로만 관리하고 API 응답·로그에 노출하지 마세요.

| 환경 | live E2E bootstrap |
|------|-------------------|
| **로컬·스테이징** | `ogada.live-e2e.bootstrap-enabled=true` 허용 (dev 전용) |
| **prod** | **모든 live E2E 플래그 OFF 필수** — 기동 거부 |

> 관련: Q360 · DEPLOYMENT_GUIDE §4-7 · ADMIN_GUIDE §2-3 · **`ProductionSecretValidatorTest`**

> 관련: DEPLOYMENT_GUIDE §3-7·§9-1

### [TWR] Q366. **통합식사도움기록**(L02_M13, 케어포 2-1-1)은 어디서 기록하나요?

**A.** **✅ full Fixed (BE `81a2223` / FE `9ad8346`, L02 v3.1 Must / BNK-248)** — SideNav **기록 → 통합식사도움기록 (L02_M13)** 또는 **`/care/meal-assistance-records`** 에서 목록·등록·수정합니다.

| 항목 | 내용 |
|------|------|
| UI | **`MealAssistanceRecordPage`** · **`MealAssistanceRecordForm`** Field render-prop · 목록 **수정** 버튼 |
| API | **`GET/POST/PATCH /api/v1/care/meal-assistance-records`** |
| `mealType` | `BREAKFAST`(아침) · `LUNCH`(점심) · `SNACK`(간식) |
| `intakeLevel` | `WELL`(잘 먹음) · `NORMAL`(보통) · `LESS`(적게) |
| `dietRestriction` | `NONE` · `LOW_SALT` · `DIABETIC` · `SOFT` · `OTHER` |
| guards | **기록일 미래 불가** · **`assistanceDetail` 공백 불가** · **(이용자, 기록일, mealType) UNIQUE** |
| DB | **Flyway V140** `meal_assistance_records` |
| RBAC | **`hq_admin`·`branch_admin`·`social_worker`·`caregiver`** |

| 테스트 | **`MealAssistanceRecordPage.test`** · **`mealAssistanceRecordServices.test`** · **`mealAssistanceRecordLiveApi.e2e.test.js`** · BE **`MealAssistanceRecordServiceTest`** · **`MealAssistanceRecordPilotServiceFlowE2eTest`**

> **L02_M01 주간 기록·식사 모듈(`/meals`)과 구분** — L02_M13은 **일별·식사 구분별 통합 식사 도움** 전용입니다.

> 관련: USER_MANUAL §5-27 · ADMIN_GUIDE §6-2-18 · REQUIREMENTS L02 v3.1 Must

### [TWR] Q367. 알림 채널 준비 상태에서 **live 발송이 안 될 때** 무엇을 확인하나요?

**A.** **Fixed (BE `de25b3e`, J03 / BNK-248)** — **`GET /api/v1/notifications/channel-status`** 응답에 **`readinessBlockers[]`** 가 추가되어, Solapi·SMTP live 연동 전 **누락 원인 코드**를 확인할 수 있습니다. 비밀값(API 키 등)은 노출하지 않습니다.

| blocker 코드 | 의미 | 조치 |
|-------------|------|------|
| `ALIMTALK_PROVIDER_NOT_SOLAPI` | 알림톡 provider가 `solapi`가 아님 | `application.yml` / env `NOTIFICATION_PROVIDER=solapi` |
| `MISSING_SOLAPI_CONFIG` | Solapi 키·발신번호·카카오 PF ID 누락 | `missingSolapiConfigKeys[]` 참고 — `SOLAPI_API_KEY` 등 설정 |
| `MISSING_TEMPLATE_MAPPING` | 필수 알림톡 템플릿 미매핑 | `missingTemplateCodes[]` · Solapi 템플릿 등록 |
| `EMAIL_PROVIDER_NOT_SMTP` | 이메일 provider가 `smtp`가 아님 | `NOTIFICATION_EMAIL_PROVIDER=smtp` |
| `MISSING_SMTP_CONFIG` | SMTP 호스트 미설정 | `SMTP_HOST` 등 mail 설정 |

| UI | **`/organization/settings`**·대시보드 **`NotificationChannelReadinessPanel`** — Solapi·SMTP·템플릿 표 (Q318) · **P2**: `readinessBlockers` 목록 FE 표시 |

| 테스트 | **`NotificationChannelReadinessServiceTest`** · **`notificationChannelStatusLiveApi.e2e.test.js`**

> 관련: ADMIN_GUIDE §6-2-4 · DEPLOYMENT_GUIDE §4-3 · Q318 · Q329(quiet-hours)

### [TWR] Q361. **신체제재 기록**(L02_M07, 케어포 2-4)은 어디서 기록하나요?

**A.** **✅ full Fixed (BE `ea6092a` / FE `14a2bb9`, L02 v3.1 Must / BNK-241)** — SideNav **기록 → 신체제재 기록 (L02_M07)** 또는 **`/care/body-restraint`** 에서 목록·등록·수정합니다.

| 항목 | 내용 |
|------|------|
| 대응 | 케어포 **`view.care_sanction`** (2-4 신체제재) — **func.php 2-4(차량관리)와 무관** |
| UI | **`BodyRestraintRecordPage`** · **`BodyRestraintRecordForm`** Field render-prop · 목록 **수정** 버튼 |
| 권한 | `hq_admin`·`branch_admin`·`social_worker`·`caregiver` — **활성 지점 필수** |
| 제재 방법 | 침대 난간 · 조끼형 · 의자·테이블 · 손싸개 · 안전벨트 · 기타 (`BED_RAIL` 등 6종) |
| 필수 검증 | **`reason` 공백 불가** · **제재일 미래 불가** · **`endedAt ≥ startedAt`** |
| 보호자 통지 | `guardianNotified` 체크박스 (기본 미통지) |
| 조회 기간 | `fromDate`·`toDate` 생략 시 **최근 90일** |
| DB | **Flyway V131** `body_restraint_records` · **V132** integrity triggers |

| 구분 | L02_M07 (요양기록) | L02_M02 (`/care/intensive-excretion`) |
|------|-------------------|--------------------------------------|
| 모듈 | 요양기록 L02 | 요양기록 L02 |
| 내용 | **신체제재** 인권 기록 | 집중 **배설 관찰** |

| 테스트 | **`BodyRestraintRecordPage.test`** · **`BodyRestraintRecordForm.test`** · **`bodyRestraintRecordServices.test`** · **`bodyRestraintRecordLiveApi.e2e.test.js`** · BE **`MustApiEndpointRoutingTest$BodyRestraintRecordRouting`** · **`RoleBasedControllerAccessTest$BodyRestraintRecordAccess`**

> 관련: USER_MANUAL §5-24 · ADMIN_GUIDE §6-2-14 · REQUIREMENTS L02 v3.1 Must

### [TWR] Q362. **요양급여 주간 제공기록**(L02_M01, 케어포 2-1)은 어디서 기록하나요?

**A.** **✅ full Fixed (BE `13b8a37` / FE `41b2123`, L02 v3.1 Must / BNK-244)** — SideNav **기록 → 요양급여 제공기록 (L02_M01)** 또는 **`/care/weekly-service-records`** 에서 목록·등록·수정합니다.

| 항목 | 내용 |
|------|------|
| 대응 | 케어포 **`view.care_service_weekly`** (2-1 요양급여 제공기록) |
| UI | **`CareServiceWeeklyRecordPage`** · **`CareServiceWeeklyRecordForm`** Field render-prop · 7 note 영역 |
| 권한 | `hq_admin`·`branch_admin`·`social_worker`·`caregiver` — **활성 지점 필수** |
| 주 시작일 | **월요일만** (`week_start_date` CHECK) |
| 필수 검증 | **7개 note 중 1개 이상** 공백 아님 · 이용자·주당 **1건** UNIQUE |
| DB | **Flyway V134** `care_service_weekly_records` · **V135** integrity triggers |

| 테스트 | **`CareServiceWeeklyRecordPage.test`** · **`CareServiceWeeklyRecordForm.test`** · **`careServiceWeeklyRecordServices.test`** · **`careServiceWeeklyRecordLiveApi.e2e.test.js`** · **`pilotPageFlows`** L02_M01 · BE **`CareServiceWeeklyRecordServiceTest`**

> 관련: USER_MANUAL §5-25 · ADMIN_GUIDE §6-2-15 · REQUIREMENTS L02 v3.1 Must

### [TWR] Q363. **목욕 일정·제공현황**(L02_M03, 케어포 2-3)은 어디서 관리하나요?

**A.** **✅ full Fixed (BE `e703252`·`47a4e25` / FE `950415d`, L02 v3.1 Must / BNK-245)** — SideNav **기록 → 목욕 일정·제공현황 (L02_M03)** 또는 **`/care/bathing-schedules`** 에서 일정·제공 상태를 관리합니다.

| 항목 | 내용 |
|------|------|
| 대응 | 케어포 **`view.care_bath_manage`** (2-3 목욕일정 및 제공현황) |
| UI | **`BathingSchedulePage`** · **`BathingScheduleForm`** Field render-prop |
| 목욕 유형 | 전신·부분·족욕·샴푸만 (`FULL_BATH` 등 4종) |
| 제공 상태 | 예정 · 제공 완료 · 취소 · 미제공 |
| 필수 검증 | **제공 완료** → `provisionNotes` 필수 · **취소/미제공** → `notes`(사유) 필수 (`47a4e25`) |
| DB | **Flyway V136** `bathing_schedules` · **V137** integrity triggers |

| 테스트 | **`BathingSchedulePage.test`** · **`BathingScheduleForm.test`** · **`bathingScheduleLiveApi.e2e.test.js`** · BE **`BathingScheduleServiceTest`** · **`BathingSchedulePilotServiceFlowE2eTest`**

> 관련: USER_MANUAL §5-26 · ADMIN_GUIDE §6-2-16 · L02_M01(`/care/weekly-service-records`)과 **별도 도메인**

### [TWR] Q364. 청구 상세 **「명세 4채널 발송」**(G-7-1-4CHANNEL, 케어포 7-1)은 무엇인가요?

**A.** **✅ full Fixed (BE `3a2e82e` / FE `1fd1434`, G-7-1-4CHANNEL / BNK-241)** — 확정·수납 청구 상세(`/billing/claims/:id`)에서 **본인부담금 명세서**를 **우편·문자·이메일·직접수령** 4채널로 **이용자별 일괄 발송 기록**합니다.

| 항목 | 내용 |
|------|------|
| 대응 | 케어포 **PDF p.87** 본인부담금 명세 발송 |
| UI | **`BillingDetailPage`** **「명세 4채널 발송」** · **`BillingStatementDispatchPanel`** |
| 표시 조건 | 청구 **`CONFIRMED` 또는 `PAID`** · 급여 항목 1건 이상 |
| 채널 | `POSTAL` · `SMS` · `EMAIL` · `IN_PERSON` |
| 발송일 | **우편만** `PATCH`로 수정 가능 · 문자·이메일은 **자동 기록·수정 불가** |
| quiet-hours | **22:00~08:00 KST** 문자·이메일 **비활성** (J03, Q329) |
| API | **`GET/POST /billing/claims/{id}/statement-dispatches`** · **`PATCH …/{dispatchId}`** |
| DB | **Flyway V133** `billing_statement_dispatches` |

| 구분 | 4채널 명세 발송 | 보호자 일괄 알림 (`notify`, Q196) |
|------|----------------|----------------------------------|
| 목적 | **명세 전달 경로** 기록 | 알림·이메일/알림톡 dispatch |
| 화면 | 청구 상세 **명세 4채널 발송** | 청구 상세 **보호자 발송** |

| 테스트 | **`BillingStatementDispatchPanel.test`** · **`billingStatementDispatchServices.test`** · **`BillingDetailPage.test`** · BE **`BillingStatementDispatchServiceTest`** · **`BillingStatementDispatchPilotServiceFlowE2eTest`**

> 관련: USER_MANUAL §4-6-0 · ADMIN_GUIDE §6-2-17 · REQUIREMENTS 7-1

### [TWR] Q365. G30 **유선상담 60% 만족**(FAQ21841)은 어떻게 집계되나요?

**A.** **✅ full Fixed (BE `344a28b` / FE `9ad8346`, G30 / BNK-247)** — 모니터링 **통합 checklist** 문항 12(유선상담 5명)는 **등록 건수**와 **만족(Y) 비율**을 함께 봅니다. **`/compliance/monitoring`** 화면에서 **유선상담 실시**·**만족(Y) 비율** StatCard로 **`satisfiedCount`/`satisfactionMet`** 를 확인합니다.

| 항목 | 내용 |
|------|------|
| 기준 | FAQ21841 — **월 5명** 유선상담 · **기록된 상담 중 60% 이상 `satisfied=true`** |
| API | **`POST /compliance/monitoring/phone-consultations`** — body에 **`satisfied`** (boolean) |
| compliance | **`GET …/phone-consultations/compliance`** — `recordedCount`·`satisfiedCount`·`satisfactionMet` |
| checklist | **`GET …/checklist`** 문항 12 — **「유선상담 5명·60% 만족」** 메시지 |
| DB | **Flyway V138** `monitoring_phone_consultations.satisfied` |
| UI | **`MonitoringSelfDiagnosisPage`** — **`monitoringCompliance.js`** · 5명 미달·60% 미달 **warning Alert** |

| 테스트 | **`MonitoringSelfDiagnosisPage.test`** · **`monitoringCompliance.test`** · **`monitoringLiveApi.e2e.test.js`** · BE **`MonitoringServiceTest`**

> 관련: Q320 · USER_MANUAL §4-3 · ADMIN_GUIDE §6-2-11 · REQUIREMENTS FAQ21841

### [TWR] Q368. **요양급여 특이사항**(L02_M15, 케어포 2-1-3)은 어디서 기록하나요?

**A.** **✅ full Fixed (FE `3549896`, L02 v3.1 Must / BNK-248)** — SideNav **기록 → 요양급여 특이사항 (L02_M15)** 또는 **`/care/service-special-notes`** 에서 **`specialNotes`** 를 등록·수정합니다.

| 항목 | 내용 |
|------|------|
| 대응 | 케어포 **`view.care_service_bigo_all`** (2-1-3 요양급여 특이사항) |
| UI | **`CareServiceSpecialNotesPage`** · **`CareServiceSpecialNotesForm`** Field render-prop |
| API | V134 **`weekly-service-records`** — **`specialNotes`** 필드 (다른 7 note 보존 PATCH) |
| guards | **주 시작일 월요일** · **특이사항 공백 불가** · 신규 시 이용자 필수 |
| RBAC | **`hq_admin`·`branch_admin`·`social_worker`·`caregiver`** |

| 구분 | L02_M15 (특이사항) | L02_M01 (`/care/weekly-service-records`) |
|------|-------------------|------------------------------------------|
| 초점 | **`specialNotes` 단일 필드** | 7 note 영역 **주간 제공기록** |
| API | 동일 weekly-service-records | 동일 |

| 테스트 | **`CareServiceSpecialNotesPage.test`** · **`careServiceSpecialNotesLiveApi.e2e.test.js`**

> 관련: USER_MANUAL §5-28 · ADMIN_GUIDE §6-2-19 · FAQ Q362

### [TWR] Q369. **요양/식사/화장실·목욕도움 리포트**(L02_M04/M05)는 어디서 보나요?

**A.** **✅ full stack Fixed (BE `c655743`/`27b40cd` + FE `c5f82a6`/`d2145b0`/`46971e1`, L02 v3.1 Must / BNK-252~253)** — SideNav **기록** 그룹에서 **전용 리포트 화면**으로 조회·**인쇄**할 수 있습니다.

| 항목 | L02_M04 (2-5 요양/식사/화장실) | L02_M05 (2-6 목욕도움) |
|------|-------------------------------|------------------------|
| 화면 | **`/care/reports/meal-excretion`** — **`CareMealExcretionReportPage`** | **`/care/reports/bath-help`** — **`BathHelpReportPage`** |
| API | **`GET /api/v1/care/reports/care-meal-excretion`** | **`GET /api/v1/care/reports/bath-help`** |
| 집계 | L02_M13 식사·L02_M02 배설·L02_M01 weekly notes | L02_M03 목욕 일정 **상태별 건수·목록** |
| 필터 | **시작일·종료일·이용자(선택)** — `Field` render-prop | 동일 |
| 기본 기간 | **`fromDate`/`toDate` 생략** 시 BE가 데이터 기준 자동 (`27b40cd`) | 동일 |
| 인쇄 | **「인쇄」** — `window.print()` · **`ds-care-report-print-root`** (`d2145b0`) | 동일 |
| RBAC | **`hq_admin`·`branch_admin`·`social_worker`·`caregiver`** | 동일 |

| 테스트 | BE **`CareReportServiceTest`** · **`CareReportLiveApiRoutingE2eTest`** · FE **`CareMealExcretionReportPage.test`** · **`BathHelpReportPage.test`** · **`pilotPageFlows`** · live E2E |

> **P2 잔여**: CSV 다운로드 · **QA-B95** `./scripts/run-live-e2e.sh` 1회 RUN 확인 (guardian bootstrap @ `b3bd0cc`)  
> 관련: USER_MANUAL §5-29·§5-30 · ADMIN_GUIDE §6-2-20 · REQUIREMENTS L02 v3.1 rpt cluster

### [TWR] Q370. 배차 지도에 **직선이 아닌 도로 경로**가 안 보여요.

**A.** **Fixed (BE `e8b8398`/`3eeac92` + FE `0c523cd`/`15e9b64`/`1daeda7`/`b000d92`/`5ebaade`, v1.3-A / BNK-253·BNK-285, Q370·Q394·Q395)** — **`KakaoTransportMap`** 이 **`loadKakaoMapSdk`** 로 Kakao Maps **JavaScript SDK**를 동적으로 로드한 뒤, **`kakaoMapInstance.js`**·**`useKakaoMap`** 으로 지도를 생성하고 **`KakaoTransportMapView`** 에서 마커·도로 폴리라인을 렌더합니다. 백엔드 **`POST /api/v1/transport/route-preview`** 로 Kakao Mobility **도로 경로**를 받아 Polyline으로 표시합니다. route-preview 실패 시 **마커·정차 안내선**만 표시됩니다 (SVG fallback **제거**, `b000d92`). **`5ebaade`** — route-preview **전** 좌표 기반 **seed markers** 선표시.

| 항목 | 내용 |
|------|------|
| API | **`POST /api/v1/transport/route-preview`** — 지점·정차 좌표(`lat`/`lng` 또는 **`pickupLat`/`pickupLng`**) → `path[]`·`distanceMeters`·`durationSeconds` |
| RBAC | **`hq_admin`·`branch_admin`·`social_worker`·`caregiver`** |
| 프론트 키 | **`VITE_KAKAO_MAP_JS_KEY`** — **`loadKakaoMapSdk.js`** (`libraries=services`, DEPLOYMENT §4-7) |
| 서버 키 | **`KAKAO_REST_KEY`** — geocode + directions proxy |
| 도메인 | JS 키에 **접속 origin 미등록** 시 **`KAKAO_MAP_SDK_LOAD_FAILED`** Alert + Web 도메인 등록 안내 (FAQ **Q394**) |
| UI | 루트 상세·새 배차 **지도 영역** — 거리·예상 시간 요약 · **`role="status" aria-live="polite"`** · canvas **`role="application"`** (`5ebaade`) · SDK 미설정 시 **Alert**(Spinner 제거) |

| 테스트 | **`TransportRoutePreviewServiceTest`** · **`KakaoDirectionsClientTest`** · FE **`KakaoTransportMap.test.jsx`** · **`kakaoMapInstance.test`** · **`transportSuggestServices.test`** |

> 관련: FAQ Q159 · USER_MANUAL §5-8 · ADMIN_GUIDE §10-10 · DEPLOYMENT §4-7

### [TWR] Q371. **집중배설 리포트**(L02_M17)는 어디서 보나요?

**A.** **✅ full Fixed (BE `ae7e744` / FE `fa20943`, L02 v3.1 Must / BNK-256)** — SideNav **기록 → 집중배설 리포트 (L02_M17)** 또는 **`/care/reports/intensive-excretion`** 에서 기간·이용자별 집계를 조회·인쇄합니다.

| 항목 | 내용 |
|------|------|
| 케어포 대응 | **2-8.집중배설관찰 리포트** (`view.total_excretion`) |
| API | **`GET /api/v1/care/reports/intensive-excretion?fromDate=&toDate=&clientId=`** |
| 집계 | L02_M02 **집중배설관찰** 기록 — `totalObservationCount`·`urinationCount`·`defecationCount`·`bothCount`·`interventionCount` |
| 데이터 | **V130** `intensive_excretion_observation_records` — read-only aggregate |
| RBAC | **`hq_admin`·`branch_admin`·`social_worker`·`caregiver`** |
| FE | **`IntensiveExcretionReportPage`** · **`CareReportContextNav`** 4탭 · **인쇄** · **`careReports.js`** |

| 테스트 | **`CareReportServiceTest`** · **`CareReportLiveApiRoutingE2eTest`** · FE **`IntensiveExcretionReportPage.test`** · **`intensiveExcretionReportLiveApi.e2e.test.js`** · **`pilotPageFlows`** |

> 입력 원본: **`/care/intensive-excretion`** (L02_M02, Q359).  
> 관련: USER_MANUAL §5-31 · ADMIN_GUIDE §6-2-21 · REQUIREMENTS L02 v3.1 rpt cluster

### [TWR] Q372. **체위변경 대상자 리포트**(L02_M06)는 어디서 보나요?

**A.** **✅ full Fixed (BE `9cc0c1d` / FE `fa20943`, L02 v3.1 Must / BNK-256)** — SideNav **기록 → 체위변경 대상자 리포트 (L02_M06)** 또는 **`/care/reports/position-change`** 에서 위험평가·체위변경 케어 집계를 조회·인쇄합니다.

| 항목 | 내용 |
|------|------|
| 케어포 대응 | **2-7.체위변경 대상자 관리 리포트** (`view.position_YC_report`) |
| API | **`GET /api/v1/care/reports/position-change?fromDate=&toDate=&clientId=`** |
| 집계 | US-O03 **욕창 위험평가** + **체위변경 케어 기록** — `highRiskCount`·`moderateRiskCount`·`lowRiskCount`·`targetClientCount`·`preventionPlanCount`·`careRecordCount`·`preventionMeasureCount` |
| 데이터 | **V114** `pressure_ulcer_*` — read-only aggregate |
| RBAC | **`hq_admin`·`branch_admin`·`social_worker`·`caregiver`** |
| FE | **`PositionChangeReportPage`** · **`CareReportContextNav`** · 위험 Badge · **인쇄** |

| 테스트 | **`CareReportServiceTest`** · **`CareReportLiveApiRoutingE2eTest`** · FE **`PositionChangeReportPage.test`** · **`positionChangeReportLiveApi.e2e.test.js`** · **`pilotPageFlows`** |

> 입력 원본: **`/nursing/pressure-ulcer`** (US-O03, Q340~Q346).  
> 관련: USER_MANUAL §5-32 · ADMIN_GUIDE §6-2-22 · REQUIREMENTS L02 v3.1 rpt cluster

### [TWR] Q373. **수급자별 급여제공 리포트**(L02_M11)는 어디서 보나요?

**A.** **✅ full Fixed (BE `2cf0908` / FE `ff9c8c5`, L02 v3.1 Must / BNK-258)** — SideNav **기록 → 수급자별 급여제공 리포트 (L02_M11)** 또는 **`/care/reports/patient-service`** 에서 이용자 1명의 L02 입력을 cross-source 집계·조회·**인쇄**합니다.

| 항목 | 내용 |
|------|------|
| 케어포 대응 | **수급자별 급여제공** (`view.patient_service`) |
| API | **`GET /api/v1/care/reports/patient-service?fromDate=&toDate=&clientId=`** |
| UI | **`PatientServiceReportPage`** · **`CareReportContextNav`** 6탭 · StatCard·5종 상세 표 · **인쇄** |
| 집계 | L02_M01·M13·M03(COMPLETED)·M02·M07 — counts + 5 detail arrays |
| RBAC | **`hq_admin`·`branch_admin`·`social_worker`·`caregiver`** |

| 테스트 | **`CareReportServiceTest.getPatientServiceReport*`** · **`CareReportLiveApiRoutingE2eTest`** · FE **`PatientServiceReportPage.test`** · **`patientServiceReportLiveApi.e2e.test.js`** · **`pilotPageFlows`** |

> **`clientId` 필수** — 미선택 시 조회 오류.  
> 관련: USER_MANUAL §5-33 · ADMIN_GUIDE §6-2-23 · REQUIREMENTS L02 v3.1 rpt cluster

### [TWR] Q374. **급여제공 서비스 집계 리포트**(L02_M12)는 어디서 보나요?

**A.** **✅ full Fixed (BE `2cf0908` / FE `ff9c8c5`, L02 v3.1 Must / BNK-258)** — SideNav **기록 → 급여제공 서비스 집계 리포트 (L02_M12)** 또는 **`/care/reports/service-summary`** 에서 활성 지점 **전체 이용자** L02 건수를 **이용자별 행**으로 조회·**인쇄**합니다.

| 항목 | 내용 |
|------|------|
| 케어포 대응 | **급여제공 서비스 집계** (`view.service`) |
| API | **`GET /api/v1/care/reports/service-summary?fromDate=&toDate=`** (`clientId` 없음) |
| UI | **`ServiceSummaryReportPage`** · **`CareReportContextNav`** · StatCard·이용자별 표 · **인쇄** |
| 집계 | `clientCount`·branch totals·`rows[]` per-client 5종 counts + `totalServiceEntries` |
| RBAC | **`hq_admin`·`branch_admin`·`social_worker`·`caregiver`** (활성 지점 스코프) |

| 테스트 | **`CareReportServiceTest.getServiceSummaryReport*`** · **`CareReportLiveApiRoutingE2eTest`** · FE **`ServiceSummaryReportPage.test`** · **`serviceSummaryReportLiveApi.e2e.test.js`** · **`pilotPageFlows`** |

> **P2 잔여**: CSV export  
> 관련: USER_MANUAL §5-34 · ADMIN_GUIDE §6-2-24 · REQUIREMENTS L02 v3.1 rpt cluster

### [TWR] Q375. **식사(간식) 선호도 조사**(L02_M16)는 어디서 등록하나요?

**A.** **✅ full Fixed (BE `f33252a` / FE `8b804fc`, G-MEAL-PREFERENCE / BNK-258)** — SideNav **기록 → 식사 선호도 조사 (L02_M16)** 또는 **`/care/meal-preference-surveys`** 에서 이용자별 **만족도·선호/비선호 음식·식단 반영 여부**를 등록·수정합니다.

| 항목 | 내용 |
|------|------|
| 케어포 대응 | **2-1-4 식사(간식) 선호도 조사 및 반영** (`view.meal_satisfaction`) |
| API | **`GET/POST/PATCH /api/v1/care/meal-preference-surveys`** · **V142** |
| UI | **`MealPreferenceSurveyPage`** · **`MealPreferenceSurveyForm`** Field render-prop |
| 필드 | **`mealType`** BREAKFAST/LUNCH/SNACK · **`satisfactionLevel`** SATISFIED/NORMAL/DISSATISFIED · **`menuReflected`** |
| 중복 | **이용자+조사일+식사구분** UNIQUE — 중복 **`422`** → 기존 행 **수정** |
| RBAC | **`hq_admin`·`branch_admin`·`social_worker`·`caregiver`** — 등록·조회 |

| 테스트 | **`MealPreferenceSurveyServiceTest`** · **`MealPreferenceSurveyLiveApiRoutingE2eTest`** · FE **`MealPreferenceSurveyPage.test`** · **`mealPreferenceSurveyLiveApi.e2e.test.js`** |

> 퇴소·비활성 이용자 신규 등록 **거부** (V142 trigger).  
> 관련: USER_MANUAL §5-35 · ADMIN_GUIDE §6-2-25 · REQUIREMENTS G-MEAL-PREFERENCE

### [TWR] Q385. L02_M16 **식사 선호도 집계 리포트 API**는 어디서 확인하나요?

**A.** **Fixed (BE `98ef09b`, Q385)** — L02_M16 입력 데이터를 기간·이용자 기준으로 만족도 집계하는 API가 추가되었습니다. 현재는 **운영/연동 점검용 API**이며 전용 FE 화면은 없습니다.

| 항목 | 내용 |
|------|------|
| API | **`GET /api/v1/care/reports/meal-preference?fromDate=&toDate=&clientId=`** |
| 권한 | **`hq_admin`·`branch_admin`·`social_worker`** (`caregiver` 403) |
| 응답 요약 | `totalSurveyCount` · `satisfiedCount` · `normalCount` · `dissatisfiedCount` · `items[]` |
| 데이터 원본 | **`meal_preference_surveys`** (V142) |
| 점검 방법 | Swagger 또는 API 클라이언트에서 호출 후 `items[].satisfactionLevel` 분포와 요약 카운트 일치 확인 |

> 관련: USER_MANUAL §5-35 · DEPLOYMENT §11-3 · ADMIN_GUIDE §6-2-25

### [TWR] Q376. 방문일정 **청구반영 상태**(`billingClaimReflectionStatus`)는 무엇인가요?

**A.** **Fixed (BE `6da49aa`·FE `25ca88e`·a11y `25291b3`, G21 / BNK-258)** — PLAN/BILLING **페어 일정**이 공단 청구 반영 기준과 **일치하는지** API가 계산해 **`GET /api/v1/visits`** 목록·상세 응답에 **`billingClaimReflectionStatus`** 를 포함하고, **`/visits`** 당일 목록 **「청구반영」** 열에 **Badge**로 표시합니다. 이지케어 Channel.io **검은=반영·빨간=미반영** UX parity (bc7f4cd9) — **접근성 강화**(`25291b3`)로 Badge는 **텍스트 라벨**(청구반영·미반영·페어 없음)을 병행하고 Alert에서 **색상만 설명을 제거**했습니다.

| 값 | Badge 라벨 | tone | 의미 |
|----|-----------|------|------|
| **`REFLECTED`** | **청구반영** | `dark` | 페어 PLAN/BILLING **날짜·시간·제공분·담당** 5필드 일치 |
| **`NOT_REFLECTED`** | **미반영** | `danger` | 페어 있으나 슬롯 불일치·링크 무결성 실패 |
| **`UNPAIRED`** | **페어 없음** | `neutral` | `pairedScheduleId` null **또는 페어 엔티티 누락** (`e54a699`, Q388) |

| 항목 | 내용 |
|------|------|
| 계산 | **`VisitService.resolveBillingClaimReflectionStatus`** — `visitDate`·`plannedStartTime`·`plannedEndTime`·`serviceMinutes`·`assignedUserId` 5필드 비교 |
| FE | **`VisitsPage`** — **`BILLING_CLAIM_REFLECTION_STATUS`** (`visits.js`) · **청구 일정** 탭·**RFID split-view**(Q377) 청구 열 · **split-view 요약 chip**(`4c9103d`, Q387) · **후속 확인 목록**(`cb457b7`, Q387) · **안내 Alert** · **`StatusBadge`** — **텍스트 라벨** 병행 · **`ds-badge--dark` forced-colors outline** (`25291b3`) |
| 확인 절차 | SideNav **기록 → 방문 일정** → **청구 일정** 탭 또는 **RFID split-view** ON → 날짜 선택 → **「청구반영」** 열 확인 — **미반영**이면 페어 PLAN/BILLING **날짜·시간·담당·제공분**을 맞춘 뒤 NHIS 일괄확정(Q330) |
| 테스트 | **`VisitServiceTest`** · **`VisitPilotServiceFlowE2eTest`** · **`VisitLiveApiRoutingE2eTest`** · FE **`VisitsPage.test`** |

> 관련: USER_MANUAL §5-11 · ADMIN_GUIDE §10-12 · REQUIREMENTS G21 plan/claim

### [TWR] Q377. 방문일정 **계획·청구 분할 비교(RFID split-view)** 는 무엇인가요?

**A.** **Fixed (FE `55fdbd0`, G21 / BNK-262)** — **`/visits`** 화면에서 **계획 일정(PLAN)** 과 **청구 일정(BILLING)** 을 **나란히** 비교하는 UI입니다. 이지케어 **change_work** 패턴 parity — NHIS **일괄확정(Q330) 전** 페어 불일치를 빠르게 찾을 때 사용합니다.

| 항목 | 내용 |
|------|------|
| 토글 | **`Switch`「계획·청구 분할 비교 (RFID split-view)」** — 켜면 **계획/청구 탭 숨김** |
| 레이아웃 | **`ds-visits-split-compare`** — 왼쪽 **계획 일정** · 오른쪽 **청구 일정** + **「청구반영」** 열 |
| API | 기존 **`GET /api/v1/visits?scheduleKind=PLAN`** · **`…=BILLING`** — **양쪽 병렬 조회** (신규 API 없음) |
| 연동 | **청구반영 상태(Q376)** — split-view **청구 열**에서 Badge 확인 · **요약 chip·후속 목록**(Q387) |
| 테스트 | FE **`VisitsPage.test`** — split-view switch·dual table |

> 관련: Q376 · USER_MANUAL §5-11 · REQUIREMENTS G21 · FAQ21824 ③ 서비스·RFID 확인

### [TWR] Q378. SideNav **기록**에 **간호급여(L02_M14)·병의원/투약 리포트(L03_M09/M10)** 메뉴가 생겼나요?

**A.** **Fixed (FE `58ee122`·`6759bf6`·`5ebaade`, BNK-262/273, Q378·Q386·Q395)** — 케어포 demo **2-x ↔ 3-x** parity를 위해 **기록** 그룹에 **입력 화면**과 **care-scoped 리포트**가 분리되어 있습니다.

| SideNav 라벨 | pamcode | 경로 | 비고 |
|-------------|---------|------|------|
| **간호급여 제공기록 (L03_M01)** | L03_M01 | **`/nursing/service`** | **입력** — 케어포 `view.nursing_service` |
| **통합 간호제공 리포트 (L02_M14)** | L02_M14 | **`/care/reports/nursing-service`** | **집계 리포트** — care proxy API (`58ee122`) |
| **병의원 진료내역 리포트 (L02·L03_M09)** | L03_M09 | **`/care/reports/hospital-visits`** | `medicalVisit=true` 필터 |
| **투약제공 리포트 (L02·L03_M10)** | L03_M10 | **`/care/reports/medication-delivery`** | `medicationProvided=true` 필터 |

| 항목 | 내용 |
|------|------|
| API | **`GET /api/v1/care/reports/nursing-service`** · **`…/hospital-visits`** · **`…/medication-delivery`** (`002e3eb`) |
| UI | **`CareNursingServiceReportPage`** · **`CareNursingServiceReportNav`** 3탭 |
| 레거시 | **`/nursing/service/reports/*`** — 간호 모듈 컨텍스트 유지 (Q350) |
| L02_M14 nav dedup | **`5ebaade`** — **`/nursing/service`** SideNav **중복 항목 제거** · 입력=L03_M01·리포트=L02_M14 only (Q395) |
| L02_M09 | 케어포 **2-8.건강상태 평가 리포트(삭제예정)** — ogada v1.2.1 **Won't** · **`/health` 건강 기록**으로 대체 |
| 테스트 | **`careLeafParity.test`** · **`SideNav.test`** · **`CareNursingServiceReportPage.test`** |

> 관련: USER_MANUAL §3-1·§5-36 · ADMIN_GUIDE §6-2-26 · REQUIREMENTS L02/L03 parity

### [TWR] Q386. **L02 care-scoped 간호 리포트**(`/care/reports/nursing-*`)는 무엇인가요?

**A.** **✅ full stack (BE `002e3eb` / FE `58ee122`, BNK-273, Q386)** — L03 간호 집계 API를 **`/api/v1/care/reports/*`** proxy로 노출하여 SideNav **기록** 그룹에서 **L02 RBAC**으로 조회하는 리포트입니다.

| 경로 | PAM | API |
|------|-----|-----|
| `/care/reports/nursing-service` | L02_M14 | `GET /api/v1/care/reports/nursing-service` |
| `/care/reports/hospital-visits` | L03_M09 | `GET …/hospital-visits` |
| `/care/reports/medication-delivery` | L03_M10 | `GET …/medication-delivery` |

| 항목 | 내용 |
|------|------|
| 권한 | **`hq_admin`·`branch_admin`·`social_worker`** — **`caregiver` 403** (Q383) |
| UI | **`CareNursingServiceReportPage`** 공통 패널 · **`CareNursingServiceReportNav`** 3탭 |
| 입력 vs 리포트 | **제공기록 입력** = `/nursing/service` · **집계 리포트** = `/care/reports/*` |
| 테스트 | **`CareReportServiceTest`** · **`CareReportLiveApiRoutingE2eTest`** · FE **`CareNursingServiceReportPage.test`** |

> 관련: Q378·Q350 · USER_MANUAL §5-36 · ADMIN_GUIDE §6-2-26

### [TWR] Q387. RFID split-view에서 **청구반영 요약·후속 확인**은 무엇인가요?

**A.** **Fixed (FE `4c9103d`·`cb457b7`, BNK-273, Q387)** — **`/visits`** split-view ON 시 선택 날짜 **청구 일정** 기준으로 **청구반영 현황**과 **후속 확인 목록**이 추가됩니다.

| UI | 설명 |
|----|------|
| **청구반영 현황** chip | **청구반영·미반영·페어 없음** 건수 3종 (`ds-visits-reflection-summary`) |
| **청구반영 후속 확인** 목록 | **미반영**·**페어 없음** 당일 청구 일정 — 이용자·시간·상태 (`ds-visits-reflection-followup`) |
| 접근성 | 요약 **`role="group" aria-label="청구반영 현황"`** · 후속 **`aria-label="청구반영 후속 확인 목록"`** |

| 테스트 | FE **`VisitsPage.test`** — summary counts·follow-up list |

> 관련: Q376·Q377 · USER_MANUAL §5-11 · ADMIN_GUIDE §10-12

### [TWR] Q388. **페어 없음(UNPAIRED)** 과 **미반영(NOT_REFLECTED)** 의 차이는?

**A.** **Fixed (BE `e54a699`, QA-B110, Q388)** — `billingClaimReflectionStatus` 계산이 **페어 엔티티 누락** 시에도 일관되게 **`UNPAIRED`** 를 반환합니다.

| 값 | 의미 | 조치 |
|----|------|------|
| **`REFLECTED`** | PLAN/BILLING 5필드 일치 | 일괄확정 진행 가능 |
| **`NOT_REFLECTED`** | 페어는 있으나 슬롯 불일치 | DRAFT에서 페어 수정(Q199) 또는 재import |
| **`UNPAIRED`** | `pairedScheduleId` 없음 **또는 페어 레코드 누락** | 페어 생성·import 재검토 |

| 테스트 | **`VisitServiceTest`** null-pair regression (`e54a699`) |

> 관련: Q376 · USER_MANUAL §5-11 · DEPLOYMENT §11-3

### [TWR] Q389. **L02 care-scoped 간호 리포트** pilot E2E·live E2E bootstrap은 어떻게 점검하나요?

**A.** **Fixed (BE `2ba2761`/`304bb2a`·`f6f1756`·`ec142db`·`22396e0`·`b1a6aff` / FE `6b34d31`·`b3bd0cc`·`4e99ae1`, BNK-279~283, Q389·Q393)** — L02_M09/M10/M14 care-scoped 리포트와 G21 RFID split-view는 **FE·BE pilot flow** 모두 추가되었습니다. live backend E2E는 bootstrap **HTTP 500** 회귀가 **`304bb2a`** 에서 해소되었고, **`f5205e3`/`b3bd0cc`** 에서 **guardian bootstrap 자동 시드**가 추가되었습니다. **`22396e0`/`b1a6aff`** — **V147** guardian trigger·**legacy onboarding reuse**로 bootstrap 정합을 강화했습니다. **`4e99ae1`** — **`resolveGuardianClientId`** 로 guardian-linked **`clientId`** 를 우선합니다. **`ec142db`** — **`CareNursingReportsLiveApiRoutingE2eTest`** 등 **live API routing harness** 3종 추가. operation 승격은 **`./scripts/run-live-e2e.sh`** 1회 **RUN** 확인이 잔여입니다 (QA-B95).

| 항목 | 내용 |
|------|------|
| BE pilot flow | **`CareNursingReportsPilotServiceFlowE2eTest`** — **`/care/reports/nursing-service`** · **`…/hospital-visits`** · **`…/medication-delivery`** — CareReportController → CareReportService → NursingServiceRecordService delegation·aggregate field contracts (`2ba2761`) · **mvn test 1374/1374 PASS** |
| FE pilot flow | **`pilotPageFlows.test`** — care-scoped nursing reports·**`/visits`** split-view reflection summary (`6b34d31`) |
| unit test | **`CareNursingServiceReportPage.test`** · **`VisitsPage.test`** · **`careReportServices.test`** |
| live E2E bootstrap | **`POST /api/v1/system/live-e2e/bootstrap`** · **`POST …/bootstrap-guardian`** — disabled 시 **`503`** (500 아님, `304bb2a`) · **`LiveE2eControllerRoutingTest`** |
| env 준비 | `cp scripts/dev-live-e2e.env.example scripts/dev-live-e2e.env` · **`ogada.live-e2e.bootstrap-enabled=true`** · guardian env **선택**(미설정 시 **`b3bd0cc`** auto-fallback) |
| live API routing | **`CareNursingReportsLiveApiRoutingE2eTest`** · **`BranchOnboardingSupportLiveApiRoutingE2eTest`** · **`StaffStatusReportLiveApiRoutingE2eTest`** (`ec142db`) |
| operation 승격 | bootstrap enabled + backend UP 상태에서 **`./scripts/run-live-e2e.sh`** 1회 **RUN** 확인 (QA-B95 잔여) |

| 상태 | BNK-279~280 |
|------|-------------|
| UI·API | **✅ full stack** (`58ee122`/`002e3eb`) |
| pilot E2E | **✅ BE+FE partial+** — BE service flow (`2ba2761`) + FE page flow (`6b34d31`) · **live API routing harness ✅** (`ec142db`) · full guardian portal live suite **QA-B95 RUN 확인 잔여** |

> 관련: Q386 · Q360 · DEPLOYMENT §3-6 · USER_MANUAL §5-36

### [TWR] Q390. **CareNursingServiceReportNav** 서브 탭이 다른 리포트 탭과 다르게 보이나요?

**A.** **Fixed (FE `8ed937c`, UXD, Q390)** — L02 care-scoped 간호 리포트 3탭은 **`CareNursingServiceReportNav`** (`.ds-context-nav--sub`)로 표시되며, 상위 **`CareReportContextNav`** 와 **시각적으로 구분**됩니다.

| 항목 | 내용 |
|------|------|
| CSS | **`.ds-context-nav--sub`** — xs font-size · control-height-sm · surface-muted 배경 |
| a11y | forced-colors outline은 기존 **`.ds-context-nav`** 선택자 상속 |
| 화면 | **`/care/reports/nursing-service`** · **`/hospital-visits`** · **`/medication-delivery`** |
| 테스트 | FE develop HEAD **1526/1526 PASS** @ `8ed937c` |

> 관련: Q386 · USER_MANUAL §5-36 · ADMIN_GUIDE §6-2-26

### [TWR] Q391. **G26·G24b·G30** 모니터링 근거 표시가 화면마다 다른가요?

**A.** **Fixed (FE `d499130`, BNK-273, Q391)** — G30 FAQ21841 StatCard 패턴에 맞춰 **G24b·G26** 화면에도 **FAQ 근거 번호**가 표시됩니다.

| 화면 | 변경 |
|------|------|
| **`/clients/needs-assessments`** (G24b) | StatCard — **「연간 완료 (FAQ 21800)」** · **「연간 미완료 (FAQ 21800)」** · **「등급변경 재사정 필요 (FAQ 21810)」** |
| **`/billing/reports/statistics`** (G26) | ② 본인부담금 월별 — **G30 FAQ21836/21842** cross-ref lede · ③ 이동서비스비 — **G24b FAQ 21800/21810** cross-ref lede |
| 참조 패턴 | G30 **`/compliance/monitoring`** — FAQ21841 StatCard suffix (기존) |

| 테스트 | **`NeedsAssessmentStatusPage.test`** · **`BillingStatisticsReportPage.test`** |

> 관련: Q355·Q357·Q379·Q365 · USER_MANUAL §4-2·§5-10 · ADMIN_GUIDE §6-2-6b · PLAN_NOTES BNK-273 P1 closure

### [TWR] Q392. NHIS import **수가표 미완료** 배너에 서버 메시지가 그대로 보이나요?

**A.** **Fixed (FE `57114b8`, G7, Q392)** — **`GET /billing/fee-schedules/year-coverage?year=`** 응답 **`message`** 가 **`FeeScheduleYearGuardBanner`**·업로드 차단 오류에 **우선 표시**됩니다. 운영자는 FE 하드코딩 문구 대신 **백엔드와 동일한 조치 사유**를 확인할 수 있습니다.

| 항목 | 내용 |
|------|------|
| API | **`GET /api/v1/billing/fee-schedules/year-coverage?year=`** — `{ registered, expected, complete, message, … }` |
| 화면 | **`/billing/imports/nhis`** — **`fetchFeeScheduleYearCoverageApi`** 병렬 로드 · **`FeeScheduleYearGuardBanner`** — `coverage.message` 우선 · 업로드 버튼 비활성 시 동일 문구 |
| 서버 gate | **`POST /billing/imports/nhis`** — 표준 25칸 미완비 **`422`** (Q260·기존 동작 유지) |

> 관련: Q260 · USER_MANUAL §4-6-1 · ADMIN_GUIDE §6-3-1 · DEPLOYMENT §3-6

### [TWR] Q393. **보호자 live E2E** 를 env 없이 실행할 수 있나요?

**A.** **Fixed (BE `f5205e3`·`ec142db`·`7ac0a46`·`22396e0`·`b1a6aff`·`440ed84`·`d8d51a7`·`8a1f342`·`2926287` / FE `b3bd0cc`·`4e99ae1`·`ddd4489`·`6f2a4eb`·`825c6b0`, BNK-283·BNK-285, QA-B95 deepen, Q393·Q394)** — dev/staging에서 bootstrap이 활성(`ogada.live-e2e.bootstrap-enabled=true`)이면, **`LIVE_E2E_GUARDIAN_EMAIL`/`PASSWORD` 미설정** 시에도 **`liveGlobalSetup`** 이 **`POST /api/v1/system/live-e2e/bootstrap-guardian`** 을 호출해 보호자 JWT·연결 **`clientId`** 를 자동 발급합니다. **`8a1f342`** — probe가 guardian bootstrap **전** seeded client를 노출합니다. **`2926287`** — **`GET /api/v1/health`** 에 **`liveE2eClientReady`·`liveE2eSeedClientId`** 가 추가되어 health만으로 시드 이용자를 확인할 수 있습니다. **`825c6b0`** — staff bootstrap **`clientId`** 를 guardian auth **전**에 persist합니다. **`7ac0a46`** — staff/guardian bootstrap email fallback 시 **동일 tenant·동일 이메일·다른 역할** 계정 재사용을 **차단**합니다. **`22396e0`** — **V147** guardian link trigger가 bootstrap 트랜잭션에서 **`clients.updated_at`** 제약을 위반하지 않도록 **`GREATEST(created_at, NOW())`** 로 갱신합니다. **`b1a6aff`** — staff bootstrap 시 **legacy onboarding support** row가 있으면 **`organizationId` backfill** 후 재사용합니다. **`440ed84`/`d8d51a7`** — staff bootstrap이 **`ensureClient`** 로 live-e2e 이용자를 **항상 시드**하고 **`LiveE2eBootstrapResponse.clientId`** 를 반환합니다. probe **`clientReady`·`seedClientId`** 로 harness preflight가 이용자 시드 여부를 확인합니다. **`4e99ae1`** — **`liveConfig.resolveGuardianClientId`** 가 보호자 포털 **`/auth/me` targets** 와 env **`LIVE_E2E_CLIENT_ID`** 를 대조해 **연결 이용자**를 우선 선택합니다. **`ddd4489`** — bootstrap endpoint 실패 시 env creds로 **`login-fallback-ok`** 재로그인을 시도합니다.

| 항목 | 내용 |
|------|------|
| BE endpoint | **`POST /api/v1/system/live-e2e/bootstrap`** — **`LiveE2eBootstrapResponse`**: `accessToken`·`refreshToken`·`email`·`organizationId`·`branchId`·`userId`·**`clientId`** (`440ed84`) |
| BE endpoint (guardian) | **`POST /api/v1/system/live-e2e/bootstrap-guardian`** — **`LiveE2eGuardianBootstrapResponse`**: `accessToken`·`refreshToken`·`email`·`organizationId`·`branchId`·`guardianUserId`·`clientId` |
| client seed | **`LiveE2eBootstrapService.ensureClient`** — staff/guardian bootstrap 시 configured **`ogada.live-e2e.client-id`** 이용자 **항상 시드** (`d8d51a7`) |
| role guard | **`LiveE2eBootstrapService.resolveScopedEmailMatch`** — **`expectedRoleCode`** 일치 계정만 재사용 (`7ac0a46`, Q394) |
| 기본 시드 | **`LIVE_E2E_GUARDIAN_EMAIL`** 기본 `live-e2e-guardian@ogada.test` · **`LIVE_E2E_GUARDIAN_PASSWORD`** 기본 `ogada-guardian-e2e` (`application.yml`) |
| FE fallback | **`liveGlobalSetup.js`** — guardian creds absent → **`bootstrap-guardian`** → env에 token·`LIVE_E2E_CLIENT_ID` 주입 → **`/auth/me` probe** (`guardian-bootstrap-token-ok`) · bootstrap 실패 시 **`login-fallback-ok`** (`ddd4489`) · **`resolveGuardianClientId`** — linked client 우선 (`4e99ae1`) |
| probe | **`GET /api/v1/system/live-e2e/probe`** — **`guardianReady`·`guardianBootstrapEndpoint`·`guardianCredentialsConfigured`·`clientReady`·`seedClientId`** (`d8d51a7`/`8a1f342`) |
| health seed | **`GET /api/v1/health`** — **`liveE2eClientReady`·`liveE2eSeedClientId`** (`2926287`) — bootstrap disabled·오류 시 false/null |
| staff seed deepen | **`ec142db`** — staff bootstrap 시 **branch onboarding `openedOn`** (US-O05) 함께 시드 · **`b1a6aff`** — **legacy onboarding row reuse**·`organizationId` backfill |
| DB trigger | **V147** — **`trg_guardian_clients_refresh_link_status`** — **`updated_at = GREATEST(created_at, NOW())`** (`22396e0`) |
| prod | **`aa6816a`** — prod에서 bootstrap **기동 거부** (FAQ **Q384**) |

| 테스트 | **`LiveE2eBootstrapServiceTest`** (+ role-collision @ `7ac0a46` · legacy onboarding @ `b1a6aff` · client seed @ `d8d51a7`) · **`LiveE2eControllerTest`** · **`LiveE2eControllerRoutingTest`** · **`LiveE2eBootstrapLiveApiRoutingE2eTest`** (`440ed84`) · **`ClientEntityTest`** (V147) · FE **`liveE2eHarness.test`** (`ddd4489`) · **`guardianLiveApi.e2e.test.js`** (`4e99ae1`) · **`pilotLivePages.e2e.test.jsx`** (`6f2a4eb`) |

> **QA-B95 잔여**: harness 안정화는 **`6f2a4eb`** 에서 **`npm run test:live-e2e` 118 passed / 0 errors** 로 확인되었습니다. **staging** 에서 백엔드 UP + bootstrap enabled 상태로 **`./scripts/run-live-e2e.sh`** 1회 **RUN** 확인을 권장합니다. bootstrap disabled·prod·health `ready=false` 이면 여전히 **SKIP** 됩니다.

> 관련: Q360 · Q389 · Q394 · DEPLOYMENT §3-6·§11-3 · ADMIN_GUIDE §1-4

### [TWR] Q394. 배차 지도에 **「카카오맵 SDK를 불러오지 못했습니다」** 가 뜨거나 지도가 비어요.

**A.** **Fixed (FE `b000d92`/`27a3996`/`5ebaade`, v1.3-A / QA-B113·QA-B114, BNK-285, Q394·Q395)** — **`KakaoTransportMap`** 은 SVG 대신 **`loadKakaoMapSdk`** 로 Kakao Maps **JavaScript SDK**를 로드합니다. **`kakaoMapInstance.js`**·**`useKakaoMap`** 으로 지도 인스턴스를 관리합니다. 아래를 순서대로 확인하세요.

| 증상 | 원인 | 조치 |
|------|------|------|
| **「JavaScript 키가 설정되지 않았습니다」** | **`VITE_KAKAO_MAP_JS_KEY`** 미설정 | 프론트 `.env` 또는 빌드 CI에 키 주입 후 **재빌드** (DEPLOYMENT §4-7) |
| **「SDK를 불러오지 못했습니다 … Web 도메인」** | JS 키 **Web 플랫폼 origin** 미등록 | [Kakao Developers](https://developers.kakao.com/) → 앱 → 플랫폼 → Web → **현재 접속 URL**(예: `https://staging.example.com`) 등록 |
| **「지도에 표시할 좌표가 없습니다」** | 정차 **`pickupLat`/`pickupLng`**·geocode 미완료 | 이용자 **픽업 주소** 저장 → **`POST /transport/geocode`** 성공 확인 (FAQ Q233) |
| 마커만·폴리라인 없음 | **`KAKAO_REST_KEY`** 미설정 또는 route-preview 실패 | 서버 REST 키 설정 · **`POST /transport/route-preview`** 스모크 (DEPLOYMENT §4-7) |

| 구현 | **`KakaoTransportMapView.jsx`** — **`mapEnabled`** overlay guard · Marker·Polyline·CustomOverlay · **`pickupLat`/`pickupLng`** · seed markers · canvas **`role="application"`** · **`KakaoTransportMap.test.jsx`** · **`kakaoMapInstance.test`** (`5ebaade`) |

> 관련: Q370 · Q395 · USER_MANUAL §5-8 · DEPLOYMENT §4-7 · ADMIN_GUIDE §10-10

### [TWR] Q396. 페이지를 **새로고침**해도 로그아웃되지 않나요?

**A.** **같은 브라우저 탭**에서는 **로그인이 유지**됩니다 (FE `84e75ec`, SEC-005 예외, 결정 96).

| 저장 위치 | 토큰 | 동작 |
|-----------|------|------|
| 메모리 | access token | 새로고침 시 소멸 → **`restoreSession()`** 이 refresh로 재발급 |
| **`sessionStorage`** | refresh token (`ogada.refreshToken`) | **탭이 열려 있는 동안** 유지 |

**탭을 닫으면** refresh token이 사라져 **다시 로그인**해야 합니다. **localStorage에는 저장하지 않습니다.** 공용 PC에서는 작업 후 **로그아웃** 또는 **탭 종료**를 권장합니다.

> 관련: Q82 · Q112 · USER_MANUAL §2-2 · ADMIN_GUIDE §1-4

### [TWR] Q397. 이동서비스 **수칙·계약** 화면이 `/transport` 에 없어졌어요.

**A.** **Fixed (FE `84e75ec`/`8763b54`, BNK-288, QA-B115, 결정 96·154차)** — G15 **수칙·계약·제18호 안내**는 **`/transport/compliance`** **`TransportCompliancePage`** 로 **분리**되었습니다.

| 경로 | 내용 |
|------|------|
| **`/transport`** | **운행 루트**(최상단) · **배차 명단** · **`hq_admin`** 자동·수동 배차 |
| **`/transport/compliance`** | **`TransportCompliancePanel`**(5항목 수칙·계약) · **`TransportForm18GuidePanel`**(별지 제18·19·20호) |

SideNav **이동 → 수칙·계약 (G15)** 또는 **`TransportContextNav`** **수칙·계약** 탭으로 이동하세요.

> 관련: Q231 · Q237 · USER_MANUAL §5-8-0 · ADMIN_GUIDE §1-4

### [TWR] Q398. 배차 명단에 **보호자 연락처** 열이 추가됐나요?

**A.** **Fixed (BE `35e03ef` / FE `84e75ec`, BNK-288)** — **`GET /api/v1/transport/roster`** 응답에 **`guardianContact`** 가 포함됩니다. 이용자 **주 보호자** 매핑에서 전화번호를 조회합니다.

| 역할 | `contact` (이용자) | `guardianContact` (보호자) |
|------|-------------------|---------------------------|
| **`hq_admin`** | 전체 번호 · `tel:` 링크 | 전체 번호 · `tel:` 링크 |
| 그 외 | **`010-****-5678`** 마스킹 | **`010-****-5678`** 마스킹 |

보호자가 등록되지 않았거나 연락처가 없으면 **빈 칸**(`""`)입니다 — **`/guardians`** 또는 이용자 등록 **주 보호자**를 확인하세요.

> 관련: Q171 · Q172 · USER_MANUAL §5-8 · DEPLOYMENT §11-3

### [TWR] Q399. 배차에서 **승차**와 **하차**를 나눠 볼 수 있나요?

**A.** **Fixed (BE `114411f` / FE `45bd923`, US-T02, QA-B115·QA-B116)** — `/transport` 상단 **「운행 방향」** 에서 **승차(PICKUP)** / **하차(DROPOFF)** 를 전환합니다.

| 방향 | 의미 | API |
|------|------|-----|
| **승차** | 아침 픽업 배차 | `GET /transport/roster?direction=PICKUP` · `GET /transport/runs?direction=PICKUP` |
| **하차** | 귀가·센터 하차 배차 | `GET /transport/roster?direction=DROPOFF` · `GET /transport/runs?direction=DROPOFF` |

- **운행 루트**·**배차 명단**·**수동 배차** 카드 제목이 **「승차/하차 운행 루트」** 등 **선택 방향**에 맞게 바뀝니다 (`45bd923`).
- **`/transport/runs/new`**·**`/transport/runs/:runId`** 에도 **승차/하차** 방향 라벨이 표시됩니다.
- **자동 배차 제안**(`POST /transport/runs/suggest`)은 **승차**에서만 표시됩니다.
- **하차** 수동 배차 생성 시, 해당 일자에 **이미 확정 하차 배차에 포함된 이용자**는 선택할 수 없습니다.

> 관련: Q400 · USER_MANUAL §5-8 · DEPLOYMENT §11-3

### [TWR] Q400. **희망 탑승·하차 시각**은 어디서 입력하나요?

**A.** **Fixed (BE `114411f` / FE `d3bef42`, V146)** — 이용자 등록·수정 **「배차·픽업 정보」** 카드에서 **희망 탑승 시각**·**희망 하차 시각**을 입력합니다.

| 필드 | API | 배차 명단 표시 |
|------|-----|----------------|
| 희망 탑승 시각 | `desiredBoardingTime` | 승차 roster·정차 기본 시각 |
| 희망 하차 시각 | `desiredDropoffTime` | 하차 roster·정차 기본 시각 |

**희망 탑승 시각** 저장 시 레거시 **`defaultPickupTime`** 도 함께 갱신됩니다. `/transport` 명단 표에는 두 시각 열이 모두 표시됩니다.

> 관련: Q166 · USER_MANUAL §4-3 · §5-8

### [TWR] Q401. 수동 배차에서 **지점(센터) 경유**와 **split-view** 편집이 뭔가요?

**A.** **Fixed (BE `f5b2b42` / FE `d3bef42`/`84e75ec`, US-T02, QA-B115)** — `/transport/runs/new`·루트 상세에서 **`TransportRouteSplitView`** 로 **정차 목록**과 **경로 지도**를 동시에 편집합니다.

| 기능 | 설명 |
|------|------|
| **지점 추가** | 센터 depot를 **`stopKind=BRANCH`** 정차로 삽입 — 출발·귀가 경유 |
| **번호 마커** | 지도 마커에 정차 순번 표시 · 목록 클릭 시 **하이라이트 동기화** |
| **정차 상한** | 이용자 **최대 15명** + 지점 포함 **최대 17** 정차 (V143) |
| **한글 geocode** | **`KoreanGeocodeUtil`**·**`koreanGeocode.js`** — 시·도 접두 주소 보강 · **건물번호 일치 시 Kakao 후보 우선** (`1d1a71f`, Q401) |

지점 주소 좌표가 없으면 geocode 실패로 **저장·확정이 차단**될 수 있습니다 (Q233).

> 관련: Q370 · Q394 · Q404 · USER_MANUAL §5-8 · DEPLOYMENT §11-3

### [TWR] Q402. 차량 **기본 운전자명**은 어떻게 등록하나요?

**A.** **Fixed (BE `114411f` / FE `d3bef42`, V145)** — `/transport/vehicles` **차량 등록·수정** Modal에서 **기본 운전자명**(`defaultDriverName`)을 **한글 성명**으로 입력합니다.

- 직원 계정 연결 없이 **자유 텍스트**로 저장합니다 (레거시 `default_driver_id` 마이그레이션 시 display name 이관).
- **수동 배차** **`TransportVehicleSelect`** 에 차량번호와 함께 운전자명이 표시됩니다.
- 확정 루트 **`TransportServiceLogPanel`** 의 **운전자**·**차량번호**는 **`GET /service-log`** 로 **차량 마스터·배차**에서 자동 채움 (**읽기 전용**, Q407).

> 관련: Q241 · USER_MANUAL §5-8-3 · ADMIN_GUIDE §1-4

### [TWR] Q403. **임시 저장(DRAFT)** 배차를 삭제할 수 있나요?

**A.** **Fixed (BE `1d1a71f` / FE `45bd923`, QA-B117)** — **`hq_admin`** 만 **DRAFT** 상태 루트를 삭제할 수 있습니다.

| 항목 | 내용 |
|------|------|
| API | **`DELETE /api/v1/transport/runs/{runId}`** → **204 NO_CONTENT** |
| 권한 | **`hq_admin` only** · 지점 쓰기 스코프 검증 |
| 제한 | **CONFIRMED(확정)** 루트는 삭제 불가 — **`422 BUSINESS_RULE`** · 확정 취소 후 편집하거나 **확정 취소**(`unconfirm`) 사용 (Q163) |
| UI | **`/transport/runs/:runId`** 하단 **「삭제」** → **`TransportDeleteRunModal`** — 운행일·정차 수 확인 · **`deleteTransportRunApi`** · 삭제 후 **`/transport`** 로 이동 |

삭제된 DRAFT 루트와 정차는 **복구할 수 없습니다**.

> 관련: Q163 · USER_MANUAL §5-8 · DEPLOYMENT §11-3

### [TWR] Q404. 배차 지도에서 **「센」 핀**이나 **범례**가 스크린리더에 어떻게 읽히나요?

**A.** **Fixed (FE `10489a7`, US-T02, WCAG 1.1.1/4.1.2/1.4.1)** — **`KakaoTransportMapView`** 가 지도 마커·범례 접근성을 보강했습니다.

| 요소 | 스크린리더·시각 |
|------|----------------|
| **지점(센터) 핀** | **`aria-label`「지점(센터) 정차」** — 시각 배지 **「센」** 은 **`aria-hidden`** (이전 **「센번 정차」** 오독 해소) |
| **이용자 정차 핀** | **「N번 정차」** (`orderNumber` 기반) |
| **범례** | **파란 선 = 도로 경로** · **회색 점선 = 정차 안내선**(route-preview 미응답 시) · **숫자 핀 = 정차 순서** · **「센」 핀 = 지점(센터)** |

지도 동작·마커 위치·색상은 변경하지 않는 **a11y 전용** 수정입니다.

> 관련: Q168 · Q395 · Q401 · USER_MANUAL §5-8

### [TWR] Q405. 이지케어 **「이지링크(EzLink)」**처럼 공단 PC 프로그램이 필요한가요?

**A.** **아닙니다.** ogada는 **web-first SaaS**로, 공단 자료는 **브라우저에서 엑셀 다운로드 → ogada 업로드**(`POST /api/v1/billing/imports/nhis`) 방식을 사용합니다 (G7, BNK-297, REQUIREMENTS §3-9).

| 구분 | 이지케어 **이지링크**(EzLink) | ogada |
|------|---------------------------|-------|
| 연동 방식 | **설치형 PC 클라이언트**(구 `smartaib4pc`) — 공단자료 조회·직원/수급자 등록·방문일정 가져오기 | **웹 브라우저** + **공단 엑셀 import** |
| PC 에이전트 | **필수** (센터 PC에 별도 설치·재설치) | **불필요** |
| ogada MVP 범위 | 경쟁사 기능 (참고) | **Must** — NHIS import·대사·`PENDING_REVIEW` (Q52·Q181) |
| 공단 포털 직접 전송 | 이지케어 자체 연동 | **후속** — MVP는 엑셀 2단계 모델 |

**현장 절차 (ogada)**

1. [롱텀케어](https://www.longtermcare.or.kr) 등 공단 포털에서 **청구내역상세** 엑셀을 다운로드합니다.
2. ogada **`/billing/imports/nhis`** 에 업로드합니다 (FAQ **Q52**).
3. `MATCHED`·`DISCREPANCY`·`UNMATCHED`·`PENDING_REVIEW` 상태로 대조합니다.

> **참고**: 이지링크는 이지케어 FAQ 21764 기준 **경쟁사 차별화 참고**이며, ogada에 **PC 에이전트 설치 요구사항은 없습니다**. 방문요양 전용 「이지링크 일정 가져오기」와 주야간보호 ogada **G21 방문일정**은 별개 모듈입니다.

> 관련: Q3 · Q52 · Q181 · USER_MANUAL §4-6-1 · REQUIREMENTS G7 · COMPETITOR_MATRIX BNK-297

### [TWR] Q406. QR 체크인에서 **복수 이용자 선택**을 키보드·스크린리더로 할 수 있나요?

**A.** **Fixed (FE `99f2f3e`, US-E04, WCAG 2.1)** — 연결 이용자가 **2명 이상**이면 **`GuardianCheckinPage`** 가 **`QrCheckinTargetsPanel`** 을 표시합니다.

| 항목 | 내용 |
|------|------|
| 화면 | **`/guardian/checkin`** · **`/attendance/checkin/qr`** — 동일 **`GuardianCheckinPage`** |
| 1명 | 이용자 이름만 표시 — 대표 보호자 연결이면 **「(대표)」** 텍스트 |
| 2명 이상 | **`role="radiogroup"`** 버튼 목록 — **「대표」** Badge |
| 키보드 | **←→↑↓** — 다음/이전 이용자 · **Home/End** — 처음/끝 · **Space/Enter** — 선택 |
| 스크린리더 | 각 버튼 **`aria-label`** — `「이름, 대표」` 또는 `「이름」` |
| API | 선택 후 `POST /attendance/qr/scan` — `{ qrToken, clientId, transportType? }` |

| 테스트 | **`QrCheckinTargetsPanel.test`** · **`GuardianCheckinPage`** 연동 |

> 관련: Q109 · Q21 · USER_MANUAL §8-4 · FLOWCHART §5-2

### [TWR] Q407. **이동서비스일지(별지 제22호)** 를 서버에 저장할 수 있나요?

**A.** **✅ full stack (BE `0cfa970`·`aaaeb10`·`aa42b9c` / FE `088e906`/`dff2f32`, G15 v1.3-C, US-T05, Q407·Q411)** — **확정(CONFIRMED)** 배차 루트에서만 **일지 준수 기록**을 서버에 저장합니다.

| 항목 | 내용 |
|------|------|
| 조회 | **`GET /api/v1/transport/runs/{runId}/service-log`** — **`TransportServiceLogResponse`** — header·rows·summary |
| 저장 | **`PUT /api/v1/transport/runs/{runId}/service-log`** — **`UpsertTransportServiceLogRequest`** — `companionName` + `stops[]` (`clientId`·`actualPickupTime`·`companionAccompanied`·`dropoffTime`) |
| 감사 | **`TRANSPORT_SERVICE_LOG_UPSERT`** — `runDate`·`stopUpdateCount`·`summary` — **`/settings` 감사 로그** (`aa42b9c`) |
| 제한 | **DRAFT** 루트 저장 시 **`422`** — `확정된 운행만 일지를 기록할 수 있습니다.` |
| DB | **V148** — `transport_runs.service_log_companion_name` · `transport_run_stops.actual_pickup_time`·`companion_accompanied`·`dropoff_time` |
| UI | **`TransportServiceLogPanel`** — **일지 보관·감사 추적** · CONFIRMED 시 **「일지 기록 저장」** · **미저장 시 인쇄·텍스트 저장 차단** |
| 권한 | **`hq_admin`·`branch_admin`·`social_worker`·`caregiver`** |
| 검증 | **`TransportServiceTest`** · **`TransportTimeComplianceTest`** · **`TransportServiceLogPanel.test`** |

> 관련: Q236 · Q411 · USER_MANUAL §5-8 · DEPLOYMENT §11-3

### [TWR] Q408. **`npm test`** 는 통과하는데 **`npm run test:live-e2e`** harness만 이전 shell env 때문에 실패해요.

**A.** **Fixed (FE `b69c8ae`, QA-B119)** — 이전 **`run-live-e2e.sh`** 또는 shell에서 남은 **`LIVE_E2E_*`·refresh token** 이 Vitest harness에 오염되면 **false positive**가 발생할 수 있었습니다.

| 항목 | 내용 |
|------|------|
| 원인 | shell **`process.env`** 에 stale **`LIVE_E2E_EMAIL`/`PASSWORD`/`REFRESH_TOKEN`** 잔존 |
| 수정 | **`liveE2eHarness.test`** — credential key **stub/clear** · stale guardian token·refresh token **격리** regression |
| 운영 | harness 실패 시 **새 터미널**에서 재실행하거나 **`scripts/dev-live-e2e.env`** 만으로 creds 관리 — **`.env` 커밋 금지** |
| live E2E | authenticated suite 실행은 여전히 **QA-B95** — healthy backend@8080 + **`./scripts/run-live-e2e.sh`** RUN 확인 |

> 관련: Q360 · Q393 · DEPLOYMENT §3-6 · ADMIN_GUIDE §1-4

### [TWR] Q409. live E2E bootstrap 시 **이용자 중복** 또는 **guardian bootstrap 2회 호출**이 발생해요.

**A.** **Fixed (BE `c13800c` / FE `af4d7f8`, QA-B95)** — 재사용 dev/staging DB에서 bootstrap이 실패하거나 guardian creds가 중복 발급되는 경우를 방지합니다.

| 증상 | 원인 | 수정 |
|------|------|------|
| **`POST /bootstrap` HTTP 500** | 시드 이용자 **`LIVE-E2E-0001`** insert **`DataIntegrityViolationException`** (이전 run 잔여 row) | BE **`ensureClientWithFallback`** — 동일 `organizationId`·`branchId` **기존 active 이용자**(`clientId` 또는 `ltcCertNo`) 재사용 · **`LiveE2eBootstrapServiceTest`** |
| **`GET /probe` HTTP 500** | **`resolveSeedClientId`** lookup 예외 | BE **`0b5657a`** — **`clientReady=false`** · **`seedClientId=null`** 반환 · **`LiveE2eControllerTest`** |
| **`bootstrap-guardian` 불필요 호출** | staff bootstrap 응답에 guardian token이 이미 포함 | FE **`applyBootstrapTokens`** — **`guardianAccessToken`/`guardianRefreshToken`/`guardianEmail`** embedded 시 **`LIVE_E2E_GUARDIAN_*`** persist · **`bootstrap-guardian` 미호출** · **`liveE2eHarness.test`** |

**운영 절차**

1. **`GET /api/v1/system/live-e2e/probe`** — **`clientReady`·`seedClientId`** 확인 (Q360).
2. bootstrap 실패 시 **`GET /api/v1/health`** — **`liveE2eClientReady`·`liveE2eSeedClientId`** 확인 (`2926287`).
3. harness 재실행 전 stale shell env 제거 — FAQ **Q408** (`b69c8ae`).
4. authenticated suite는 **`./scripts/run-live-e2e.sh`** 1회 RUN 확인 (QA-B95).

> 관련: Q360 · Q393 · Q408 · DEPLOYMENT §3-6 · ADMIN_GUIDE §1-4

### [TWR] Q410. **이동서비스 월간 리포트**(케어포 2-7·2-8)는 어디서 보나요?

**A.** **✅ full stack (BE `5d27ad3` / FE `6a18dfd`, G15 2-7/2-8)** — **`/reports/transport-monthly`** 에서 지점·월별 **서비스 변동**과 **입소자·일정·서비스 현황**을 조회합니다.

| 항목 | 내용 |
|------|------|
| UI | **`TransportMonthlyReportsPage`** — **`TransportContextNav` → 「월간 리포트」** · **대상 월** `MonthInput` · **조회**·**인쇄** |
| 2-7 API | **`GET /api/v1/transport/reports/monthly-service-variation?yearMonth=YYYY-MM`** — 신규 등록·퇴소·계약 변동 `summary`·`rows[]` |
| 2-8 API | **`GET /api/v1/transport/reports/monthly-resident-status?yearMonth=YYYY-MM`** — 이동 대상·확정 배차·탑승 정차·계약 서명 `summary`·`rows[]` |
| 변동 유형 | **NEW_TRANSPORT** · **DISCHARGED** · **CONTRACT_CREATED** · **CONTRACT_UPDATED** |
| 권한 | **`hq_admin`·`branch_admin`·`social_worker`** — **`caregiver` 403** |
| 데이터 | 기존 roster·runs·stops·contracts **집계** — **신규 Flyway 없음** |
| 검증 | **`TransportMonthlyReportServiceTest`** · **`TransportMonthlyReportsPilotServiceFlowE2eTest`** · **`TransportMonthlyReportsPage.test`** |

> 관련: Q397 · USER_MANUAL §5-8-0-2 · ADMIN_GUIDE §1-4 · DEPLOYMENT §11-3

### [TWR] Q411. **이동서비스일지** 저장 이력은 어디서 확인하나요? 인쇄가 막혀요.

**A.** **✅ full stack (BE `aa42b9c` / FE `088e906`/`dff2f32`, G15 v1.3-C, Q411)** — 일지 저장은 **감사 로그**에 남고, 화면에서는 **보관·저장 상태**를 확인할 수 있습니다.

| 항목 | 내용 |
|------|------|
| 감사 로그 | **`PUT /service-log`** 성공 시 **`TRANSPORT_SERVICE_LOG_UPSERT`** — `runDate`·`stopUpdateCount`·`recorded`·`onTime`·`total` |
| 확인 경로 | **`sysadmin`·`hq_admin`** — **`/settings` → 감사 로그** 탭 · **`GET /api/v1/settings/audit-logs`** |
| 화면 패널 | **`TransportServiceLogPanel`** **「일지 보관·감사 추적」** — 배차 확정 시각 · DB 저장 건수 · 마지막 저장 · 저장 상태 |
| 보관 안내 | 시행규칙 제34조 일지 작성·보관 의무 · 인쇄·`.txt`는 **기관 내부 보관용** |
| 인쇄 차단 | **미저장 변경** 또는 **일부 정차 미기록** 시 **「인쇄」**·**「텍스트 저장」** 차단 — 저장 후 재시도 |
| 접근성 | 정차별 Field 라벨 · **`StatusBadge`** 준수 토큰 (QA-B116, `dff2f32`) |

> 관련: Q407 · Q236 · USER_MANUAL §5-8-0-1 · ADMIN_GUIDE §1-4

### [TWR] Q395. 배차 지도가 **잠깐 비었다가** 마커가 나타나거나, SideNav에 **간호 메뉴가 두 번** 보였어요.

**A.** **Fixed (FE `5ebaade`, v1.3-A / QA-B114, BNK-285, Q395)** — 두 증상 모두 **198차**에서 정리되었습니다.

| 증상 | 원인 | 조치·동작 |
|------|------|----------|
| 지도가 비었다가 마커 표시 | route-preview **응답 대기** 중 overlay 미렌더 | **`5ebaade`** — 좌표가 있으면 **seed markers**로 route-preview **전** 마커 선표시 · SDK ready 후 **`mapEnabled=true`** 로 폴리라인 추가 |
| **「JavaScript 키가 설정되지 않았습니다」** Alert만 | **`VITE_KAKAO_MAP_JS_KEY`** 미설정 | Spinner 대신 **Alert** — 정차 목록은 계속 확인 (DEPLOYMENT §4-7) |
| SideNav **간호급여** 메뉴 중복 | **`/nursing/service`** 가 L02_M14·L03_M01 **이중 등록** | **`navConfig.js`** — **L03_M01 입력 1건** + **L02_M14 리포트** `/care/reports/nursing-service` **1건**만 표시 |

| 구현 | **`kakaoMapInstance.js`** · **`useKakaoMap.js`** · **`KakaoBareMap.jsx`** · **`KakaoTransportMap.jsx`** · CSS **`ds-transport-map__canvas-wrap`** |

| 테스트 | **`kakaoMapInstance.test`** · **`KakaoTransportMap.test.jsx`** · **`SideNav.test`** |

> 관련: Q370 · Q378 · Q394 · USER_MANUAL §3-1·§5-8

### [TWR] Q379. **본인부담금 월별 통계**(케어포 PDF p.92 7-8 ②)는 어디서 보내요?

**A.** **✅ full stack (FE `09e4ec1`·BE `6d10e0d`, G26 / L07_M09, BNK-269, Q379)** — SideNav **청구 → 본인부담 통계**(`/billing/reports/statistics`) 또는 **청구 리포트 서브 탭**에서 **② 본인부담금 월별 통계** 섹션으로 확인합니다. 동일 화면에서 **① 의료비공제**·**③ 이동서비스비**(Q382)도 함께 조회됩니다.

| 항목 | 내용 |
|------|------|
| 화면 | **`BillingStatisticsReportPage`** — **`/billing/reports/statistics`** · **`BillingReportsContextNav`** |
| API | **`GET /api/v1/billing/reports/copay-monthly-statistics?year=&branchId=`** |
| 권한 | **`hq_admin`·`branch_admin`** |
| `year` | 필수 — 달력 연도 (2000~올해). UI에서 **필드 오류**로 선검증 (Q381) · 서버 **`422`** |
| **`items[]`** | `yearMonth` · `claimCount` · `claimCountChange`(전월 대비) · `totalClaimAmount` · `claimAmountChange` · `totalDepositAmount` · `totalOutstandingAmount` |
| **`summary`** | 연간 `totalClaimCount` · `totalClaimAmount` · `totalDepositAmount` · `totalOutstandingAmount` |
| 집계 규칙 | 청구 상태 **`CONFIRMED`·`PAID`·`REFUNDED`** · **`PAID`** → 입금액 · **`CONFIRMED`** → 미수액 |
| 검증 | **`G26StatisticsReportsLiveApiRoutingE2eTest`** @ `92ae60b`/`3672bbe` — **3 endpoint** harness · **`G26StatisticsReportsPilotServiceFlowE2eTest`** @ `30f03e8` — **3-function** service flow · **`BillingStatisticsReportPage.test`** @ `09e4ec1` |

> 관련: Q252 · Q380 · Q381 · Q382 · USER_MANUAL §5-10 · ADMIN_GUIDE §6-2 G26

### [TWR] Q380. **지점 연말정산 의료비공제 통계**(케어포 7-2-1)는 이용자별로 한 번에 볼 수 있나요?

**A.** **✅ full stack (FE `d8f1fdf`·BE `903f462`, G26 / L07_M09, BNK-268, Q380)** — **개별 이용자** 상세는 Q252 **`MedicalExpenseDeductionPanel`** 이고, **지점 전체 이용자 집계**는 **`/billing/reports/statistics`** 화면 **① 국세청 의료비공제 통계** 섹션에서 확인합니다.

| 항목 | 내용 |
|------|------|
| 화면 | **`BillingStatisticsReportPage`** — 이용자 검색·페이지네이션·요약 StatCard |
| API | **`GET /api/v1/billing/reports/medical-deduction?taxYear=&branchId=&q=&page=&size=`** |
| 권한 | **`hq_admin`·`branch_admin`** |
| `taxYear` | 필수 — 귀속 연도 (Q252와 동일 검증) |
| `q` | 선택 — 이용자 이름·인정번호 검색 |
| **`items[]`** | `clientId` · `clientName` · `certNo` · `totalPaidAmount` · `paymentCount` |
| **`summary`** | `clientCount` · `totalPaidAmount` · `totalPaymentCount` |
| 집계 규칙 | Q252·Q254와 동일 — **`PAID`+`paidAt`** · **`CASH`·`BANK_TRANSFER`만** · **`CMS`·`EASY_PAY` 제외** |
| 검증 | **`G26StatisticsReportsLiveApiRoutingE2eTest`** @ `92ae60b` · **`G26StatisticsReportsPilotServiceFlowE2eTest`** @ `30f03e8` · **`BillingStatisticsReportPage.test`** |

> 관련: Q252 · Q254 · Q379 · Q381 · USER_MANUAL §5-10 · ADMIN_GUIDE §6-2 G26

### [TWR] Q381. **본인부담 통계** 화면에서 조회 연도를 잘못 입력하면 어떻게 되나요?

**A.** **Fixed (FE `31544cf`·BE `92ae60b`, G26 / UXD, BNK-268)** — **2000년 미만·올해 초과** 연도는 **API 호출 전** **`Field error`** 로 표시됩니다 (WCAG 3.3.1). 입력값을 수정하면 오류가 자동 해제됩니다. 서버에 잘못된 값이 전달되면 **`422`** 가 반환됩니다.

| 항목 | 내용 |
|------|------|
| UI | **`BillingStatisticsReportPage`** — **`Field label="조회 연도"`** · **`aria-invalid`** · **`Button aria-busy`** |
| a11y | StatCard **`role="group"`** · 표 **`captionVisuallyHidden`** · **`.ds-billing-report__summary` forced-colors** 경계선 |
| G21 연계 | **`VisitsPage`** RFID split-view — 청구반영 안내 **텍스트 라벨 전용**(색상 설명 제거) · split-view **`<section aria-labelledby>`** |
| 테스트 | **`BillingStatisticsReportPage.test`** · **`VisitsPage.test`** |

> 관련: Q379 · Q380 · Q377 · USER_MANUAL §5-10 · DESIGN_SYSTEM §43

### [TWR] Q382. **이동서비스비 월별 통계**(케어포 func module 2)는 어디서 보나요?

**A.** **✅ full stack (FE `09e4ec1`·BE `3672bbe`, G26 ③ / G16, BNK-269, Q382)** — **`/billing/reports/statistics`** 화면 **③ 이동서비스비 월별 통계** 섹션에서 확인합니다. **①·②와 동일한 조회 연도**로 **동시 로드**됩니다.

| 항목 | 내용 |
|------|------|
| 화면 | **`BillingStatisticsReportPage`** — **`/billing/reports/statistics`** · 요약 StatCard 4종 · 월별 표 7열 |
| API | **`GET /api/v1/billing/reports/transport-service-fee-statistics?year=&branchId=`** |
| 권한 | **`hq_admin`·`branch_admin`** |
| `year` | 필수 — 달력 연도 (2000~올해). Q381과 동일 선검증 · 서버 **`422`** |
| **`items[]`** | `yearMonth` · `recordCount` · `recordCountChange` · `totalAmount` · `amountChange` · `confirmedAmount` · `draftAmount` |
| **`summary`** | `totalRecordCount` · `totalAmount` · `totalConfirmedAmount` · `totalDraftAmount` |
| 집계 규칙 | **`transport_service_fee_records`** · 서비스일 기준 월별 · **`CONFIRMED`** → 확정 · **`DRAFT`** → 임시 |
| 선행 | **이동 → 이동서비스비 청구**(`/transport/service-fees`) — 배차 기반 생성·확정 (USER_MANUAL §5-8) |
| 검증 | **`TransportServiceFeeServiceTest`** · **`G26StatisticsReportsLiveApiRoutingE2eTest`** 3-endpoint · **`BillingStatisticsReportPage.test`** · **`g26StatisticsReports.test`** |

> 관련: Q379 · Q380 · Q381 · USER_MANUAL §5-10 · ADMIN_GUIDE §6-2 G26 · REQUIREMENTS G16

### [TWR] Q383. 요양보호사가 **L02 케어 리포트**(§5-29~§5-34)를 열면 오류가 납니다. 정상인가요?

**A.** **Fixed (BE `2495753`, BNK-270, Q383)** — **정상 동작**입니다. L02 **집계 리포트** API(`GET /api/v1/care/reports/*`)는 **`hq_admin`·`branch_admin`·`social_worker`만** 허용하며, **`caregiver`는 `403 FORBIDDEN`** 입니다.

| 항목 | 내용 |
|------|------|
| 대상 API | **`/care/reports/care-meal-excretion`** · **`bath-help`** · **`intensive-excretion`** · **`position-change`** · **`patient-service`** · **`service-summary`** |
| `caregiver` | **입력 기록**(L02_M01~M17 leaf)은 **등록·조회 가능** — **집계 리포트만 거부** |
| FE 갭 | SideNav **기록** 그룹에 리포트 메뉴가 **아직 표시**될 수 있음 — **P2**: `navConfig.js` `roles`에서 `caregiver` 제거 |
| 조치 | 요양보호사에게 리포트가 필요하면 **센터장·사회복지사**에게 조회를 요청하세요 |

> 관련: USER_MANUAL §5-29~§5-34 · ADMIN_GUIDE §6-2-20~24 · FAQ Q12

### [TWR] Q312. 이용자 상세 **FAQ21824 계약→청구 lifecycle**은 어디서 보나요?

**A.** **Fixed (FE `58256c6`, FAQ21824·BNK-165)** — **`/clients/:id`** **「기본정보」** 탭 상단 **「계약→청구 업무흐름 (FAQ21824)」** 카드에서 **4단 checklist**를 확인합니다.

| 단계 | 모듈 | 확인 데이터 |
|------|------|------------|
| 1. 계약·안내문 | G14 | 급여계약 서명·파일함 |
| 2. 공단등록·계획통보 | G38·G37 | 인정번호·급여계획 통보·등급 이력 PDF |
| 3. 서비스·RFID 확인 | G21·출석 | 확정 방문일정·출석 기록 |
| 4. 월말 청구·수납 | 7-x | 청구 이력·**ClaimGenerationGuard** |

| 항목 | 내용 |
|------|------|
| UI | **`ClientFaq21824LifecyclePanel`** · **`LifecycleWorkflowPanel`** · 미완료 warning · **관련 화면 바로가기** nav |
| 유틸 | **`faq21824Lifecycle.js`** — **`buildFaq21824LifecycleSteps`** · **`analyzeClientVisitServiceContext`** · **`analyzeClientBillingContext`** |
| hydrate | G14 계약·G38 compliance·방문·청구·출석·generation-guard API **병렬 로드** |
| P2 잔여 | FAQ21824 **단일 wizard UI** · RFID↔공단계획 **자동 대조** · **9종 안내문 일괄 출력** |

> 관련: Q269 · Q270 · Q310 · USER_MANUAL §3-3 · ADMIN_GUIDE §6-2-11 · REQUIREMENTS FAQ21824

### [TWR] Q293. 직원 lifecycle **입사일·퇴사일**을 잘못 입력하면 어떻게 되나요?

**A.** **Fixed (BE `cc7da1a`·`61336df` / US-R03, V87)** — ogada는 **앱·DB 이중 검증**으로 잘못된 날짜 조합을 거부합니다.

| 규칙 | 검증 위치 | 위반 시 |
|------|----------|---------|
| **퇴사일 ≥ 입사일** | `UserService.validateLifecycleState` + **V87** `chk_users_terminated_after_hired` | **`422 BUSINESS_RULE`** |
| **`TERMINATED` 시 퇴사일 필수** | 동일 + **V87** `chk_users_terminated_requires_date` | **`422 BUSINESS_RULE`** |

> **V87**은 raw SQL·잘못된 backfill에 대한 **defense-in-depth**입니다 (V36 temporal-sanity 패턴). 운영 DB 마이그레이션은 Flyway 자동 적용 — DEPLOYMENT §3-6.

> 관련: Q290 · DATA_RETENTION_POLICY §3·§4-3 · USER_MANUAL §5-3

### [TWR] Q291. **엔젤(LCMS) CMS 3-method**(계좌+카드+가상계좌)와 ogada 차이는?

**A.** **P2 Planned (BNK-127, REQUIREMENTS G2·7-5)** — ogada v2는 **본인부담금 CMS 자동이체 단일** stub만 Fixed(Q206–Q208)이며, **효성 FCMS 실연동**·**다중 결제 수단**은 후속입니다.

| 항목 | 엔젤 LCMS (BNK-127) | ogada 현재 |
|------|---------------------|-----------|
| CMS | **계좌+카드+가상계좌** 3-method | **자동이체 단일** skeleton (`/billing/cms`) |
| FCMS | 효성 FCMS live | **`FCMS_PROVIDER=stub`** |
| v2 우선순위 | 경쟁 벤치마크 | **FCMS 실연동 P1** → **7-5/다중결제 P2** |

> 관련: Q206–Q208 · REQUIREMENTS G2 · ADMIN_GUIDE §1-4

### [TWR] Q292. ogada에 **자동저장(autosave)** 기능이 있나요?

**A.** **P3 Planned (BNK-127, G-UX-Autosave)** — **아직 없습니다.** LCMS 「큰화면·자동저장」 UX는 v1.3+ 후보이며, ogada는 **DESIGN_SYSTEM** 큰폰트·터치 44px·다크모드만 적용되어 있습니다.

| 구현됨 | 미구현 (P3) |
|--------|------------|
| **Field** 단위 저장·서버 오류 표시 | **debounced autosave** (입력 중 자동 PUT) |
| 폼 **「저장」** 버튼 명시 | 기록지 **큰화면 전용 autosave** 패턴 |
| JWT **30분 idle** SessionTimeoutModal (Q112) | autosave와 **세션 만료** UX 정합 |

> 관련: REQUIREMENTS G-UX-Autosave · `docs/product/DESIGN_SYSTEM.md`

---

## 14. 관련 문서

| 문서 | 대상 | 내용 |
|------|------|------|
| [`USER_MANUAL.md`](ops/USER_MANUAL.md) | 센터장·사회복지사·보호자 | 일상 업무 조작 절차 |
| [`ADMIN_GUIDE.md`](ops/ADMIN_GUIDE.md) | `platform_admin`, `sysadmin`, `hq_admin` | 온보딩·권한·PII·감사 |
| [`DEPLOYMENT_GUIDE.md`](ops/DEPLOYMENT_GUIDE.md) | DevOps·IT | 배포·환경변수·마이그레이션·백업 |
| [`API_SPEC.md`](technical/API_SPEC.md) | 개발·연동 | REST 엔드포인트 명세 |
| [`REQUIREMENTS.md`](planning/REQUIREMENTS.md) | 기획·전체 | 요구사항·역할·MVP 범위 |
| [`FLOWCHART.md`](planning/FLOWCHART.md) | 기획·UX | 화면 흐름도 |
| [`DATA_RETENTION_POLICY.md`](ops/DATA_RETENTION_POLICY.md) | IT·개인정보 | 보관·파기 정책 |
| [`CHANGELOG.md`](ops/CHANGELOG.md) | 개발·운영 | 버전별 변경 이력 |

---

## 15. 용어 빠른 참조

| 용어 | 설명 |
|------|------|
| Tenant | SaaS 고객 1법인 = `Organization` |
| Branch | Tenant 소속 주간보호센터 지점 1곳 |
| Branch Switcher | 다지점 권한 사용자의 작업 지점 선택 UI |
| B방식 QR | 보호자/이용자가 **지점 입구 QR** 스캔 |
| copayType | 이용자별 본인부담 구분 코드 |
| fee_schedules | 등급·연도별 1일 수가표 |
| NHIS import | 공단 청구내역상세 엑셀 업로드·대조 |
| FCMS / CMS | **효성 CMS** 본인부담금 **자동이체** — ogada v2 G2 (Q206–Q208) |

---

## 16. 변경 이력

| 날짜 | 변경 내용 |
|------|----------|
| 2026-06-17 | **208차** — BE `aa42b9c`·FE `6a18dfd` G15 일지 감사·보관 UX·월간 리포트 2-7/2-8·probe seed guard·**Q236·Q407·Q409 갱신·Q410·Q411** |
| 2026-06-17 | **207차** — BE `c13800c`·FE `af4d7f8` QA-B95 bootstrap client fallback·guardian token reuse·**Q360 갱신·Q409** |
| 2026-06-17 | **206차** — BE `aaaeb10`·FE `7a4b310` G15 service log API full stack·V148·QA-B119·**Q236·Q402·Q360 갱신·Q407·Q408** |
| 2026-06-17 | **205차** — BE `2926287`·FE `0ebd0f8` QA-B95 health seed metadata·US-E04 QrCheckinTargetsPanel·**Q360·Q393·Q109·Q405·Q406** |
| 2026-06-17 | **204차** — BE `d8d51a7`·FE `6f2a4eb` QA-B95 staff clientId·probe·login fallback·pilot E2E stabilize·**Q360·Q393 갱신** |
| 2026-06-16 | **203차** — BE `b1a6aff`·FE `4e99ae1` QA-B95 live E2E deepen·V147 guardian trigger·**Q360·Q393 갱신** |
| 2026-06-17 | **202차** — BE `1d1a71f`·FE `45bd923` QA-B116 direction-aware runs·TransportDeleteRunModal FE closure·**Q399·Q403 갱신** |
| 2026-06-16 | **201차** — BE `1d1a71f`·FE `10489a7` QA-B117 DELETE draft runs·geocode scoring·US-T02 map pin a11y·**Q403~Q404** |
| 2026-06-17 | **200차** — BE `114411f`·FE `d3bef42` US-T02 branch waypoints·DROPOFF·desired times·defaultDriverName·**Q399~Q402** |
| 2026-06-17 | **199차** — BE `35e03ef`·FE `84e75ec` BNK-288 transport compliance·SEC-005 tab session·roster guardianContact·**Q82·Q396~Q398** |
| 2026-06-17 | **198차** — BE `7ac0a46`·FE `5ebaade` QA-B114 Kakao map instance refactor·SideNav L02_M14 dedup·**Q370·Q378·Q394·Q395** |
| 2026-06-17 | **197차** — BE `7ac0a46`·FE `b000d92` QA-B113 Kakao Maps JS SDK preview·QA-B95 role-mismatch seed guard·**Q370·Q393·Q394** |
| 2026-06-17 | **196차** — BE `ec142db`·FE `b3bd0cc` QA-B95 guardian bootstrap·live API routing E2E·**Q393·Q360·Q389 갱신** |
| 2026-06-17 | **195차** — BE `2ba2761`·FE `d499130` L02 nursing BE pilot E2E·G26/G24b monitoring labels·G7 year-coverage message·**Q391~Q392·Q389 갱신** |
| 2026-06-17 | **194차** — BE `304bb2a`·FE `8ed937c` live E2E bootstrap fix·L02/G21 pilot E2E·**Q389~Q390·Q360 갱신** |
| 2026-06-17 | **193차** — BE `002e3eb`·FE `58ee122` L02 care-scoped nursing reports·G21 split-view deepen·**Q386~Q388·Q378·Q360·Q376 갱신** |
| 2026-06-17 | **189차** — BE `aa6816a`·FE `14d210c` live E2E prod security·G26 3-function pilot E2E·QA-B108/B109·**Q384·Q360 갱신** |
| 2026-06-17 | **188차** — BE `2495753`·FE `09e4ec1` G26 ③ transport fee statistics·L02 care report RBAC·**Q382·Q383·Q379 갱신** |
| 2026-06-17 | **187차** — BE `3481eb8`·FE `31544cf` G26 statistics dashboard FE full stack·G26/G21 a11y·**Q379·Q380·Q381** |
| 2026-06-16 | **186차** — BE `92ae60b`·FE `e10113f` G26 dual statistics E2E harness·live E2E env parse·**Q360·Q379·Q380 갱신** |
| 2026-06-16 | **185차** — BE `472cb1d`·FE `9006a53` G26 branch billing reports·live E2E harness·**Q379·Q380 신규·Q360 갱신** |
| 2026-06-16 | **184차** — BE `b38c6f7`·FE `6759bf6` G21 RFID split-view·L02 care nav cross-links·L02/G21 a11y·**Q377·Q378 신규·Q376 갱신** |
| 2026-06-16 | **183차** — BE `b38c6f7`·FE `25ca88e` G21 claim reflection FE full·pilot E2E·**Q376 갱신** |
| 2026-06-16 | **182차** — BE `6da49aa`·FE `8b804fc` L02_M11/M12 FE·L02_M16·G21 claim reflection·**Q373·Q374·Q375·Q376 갱신** |
| 2026-06-16 | **181차** — BE `2cf0908`·FE `40684a9` L02_M17/M06 report FE·L02_M11/M12 BE·**Q371·Q372·Q373·Q374·Q360·Q369 갱신** |
| 2026-06-16 | **180차** — BE `9cc0c1d`·FE `1daeda7` L02_M17/M06 report BE·transport a11y·**Q371·Q372·Q369·Q370 갱신** |
| 2026-06-16 | **179차** — BE `3eeac92`·FE `46971e1` L02_M04/M05 report FE·print·route-preview·**Q369·Q370·Q159 갱신** |
| 2026-06-16 | **178차** — BE `c655743`·FE `3549896` L02_M13·L02_M15·G30 phone panel·L02_M04/M05 report BE·live E2E probe·**Q366·Q368·Q365·Q369·Q360 갱신** |
| 2026-06-15 | **177차** — BE `81a2223`·FE `15b09df` L02_M13 BE·V139/V140·J03 blockers·L02 a11y·**Q366·Q367·Q360 갱신**·1437/1441·1284/1284 |
| 2026-06-16 | **176차** — BE `344a28b`·FE `1fd1434` L02_M01/M03·G-7-1-4CHANNEL·G30 satisfied·**Q362~Q365·Q320 갱신**·1432/1432·1272/1272 |
| 2026-06-16 | **175차** — BE `8b7e476`·FE `10f32c4` L02_M07 FE·V132·health databaseStatusDetail·live E2E placeholder guard·**Q361·Q360 갱신**·1393/1393·1231/1231 |
| 2026-06-16 | **174차** — BE `df14e15`·FE `95e7e96` L02_M02 FE·L02_M07 BE·health ping·G19 guard·**Q359·Q360·Q361**·1381/1381·1228/1228 |
| 2026-06-15 | **173차** — BE `fd42b7e`·FE `5f17beb` L02_M02·health readiness·G19 harness·a11y·**Q359**·**Q360**·1367/1367·1214/1214 |
| 2026-06-15 | **172차** — BE `73df04d`·FE `73094f9` G39 dispatch·G30 evidence window·live E2E harness·**Q358**·**Q276·Q320 갱신**·1357/1357·1201/1201 |
| 2026-06-15 | **171차** — BE `41d8de5`·FE `9afa30e` G24b status·G19 discovery·live E2E env·**Q357**·1355/1355·1197/1197 |
| 2026-06-15 | **170차** — BE `1e21b20` / FE `3cbe582` G24b dashboard·G41 V129·7-5 alias·**Q356**·**Q355·Q328·Q286 갱신**·1347/1347·1192/1192 |
| 2026-06-15 | **169차** — BE `98002d4`/`345c0cb` / FE `8989bf4`/`c97706b` G24b compliance·a11y·L03 notes·**Q355**·**Q354·Q286·Q350·Q321 갱신**·1325/1327·1182/1182 |
| 2026-06-15 | **168차** — BE `45fb6d9`/`43c4b08` / FE `49fbf67` G24b 8-area·QA-B94 openedOn·**Q354**·**Q286·Q353 갱신**·1323/1323·1173/1173 |
| 2026-06-15 | **167차** — BE `4c1fd43`/`735dd53` / FE `79d593c` G-ONBOARD-SUPPORT FE wire·V126/V127·**Q353**·1320/1320·1171/1171 |
| 2026-06-15 | **165차** — BE `5edc45c` / FE `671a704` L03_M01/M06/M07/M09/M10/M15 FE·**Q348 갱신·Q349~Q351**·1315/1315·246/246 |
| 2026-06-15 | **164차** — BE `9bd1660` / FE `edfba7f` v1.3-B FE wire·L03_M01 BE·**Q331·Q347 갱신·Q348**·1274/1274·1131/1131 |
| 2026-06-14 | **163차** — BE `230659a` / FE `c865d2b` G21 기간 가드·v1.3-B suggest API·**Q330 갱신·Q347**·1267/1267·1121/1121 |
| 2026-06-14 | **162차** — BE `090b2d7` / FE `97108f2` L03_M13·L03_M04 FE wire·**Q344 갱신·Q345~Q346**·1261/1263·1115/1115 |
| 2026-06-14 | **161차** — BE `63cb193` / FE `962858b` L03_M14 체중 FE wire·미래일자 가드·**Q343 갱신·Q344**·1228/1228 |
| 2026-06-14 | **160차** — BE `e95df4c` / FE `5780c65` L03_M11 통합 바이탈·L03_M14 BE·**Q340~Q343**·1209/1209 |
| 2026-06-14 | **159차** — BE `24a1c5c` / FE `024e720` G-NURSING-PRESSURE-ULCER 욕창 케어 lifecycle·**Q336~Q339**·1073/1192 |
| 2026-06-14 | **158차** — BE `3bd6a43` / FE `487416d` G17b 인지활동형 미제공 사유·**Q333~Q335**·1060/1164 |
| 2026-06-14 | **157차** — BE `ba7d84f` / FE `c26cfa7` G21 batch-confirm·G42 익명함 intake·US-UX-05 SideNav·**Q330~Q332**·Q305 갱신·1060/1160 |
| 2026-06-14 | **154차** — BE `9a4ab8e` / FE `111f056` J03 quiet-hours billing UI·7-5 provider deepen·**Q329**·1030/1141 |
| 2026-06-14 | **153차** — BE `16a0734` / FE `51f2505` G2/7-5 V110·US-L06 a11y·**Q328**·1024/1133 |
| 2026-06-14 | **152차** — BE `438f5c7`·`b893e97` / FE `c9baca2`·`bebd874` G2/7-5 easy payment·V108–V109·**Q326·Q327**·1023/1126 |
| 2026-06-14 | **151차** — BE `0f11158`·`ee42e5d` / FE `38d24b6`·`45a724a` G41b compliance API wire·V107·**Q321·Q325**·246/1110 |
| 2026-06-14 | **149차** — BE `6191b91`·`613b6af` / FE `f5658de`·`e69bf00` G41/G41b 기관 교육일지·V104–V106·**Q321**·1004/1099 |
| 2026-06-14 | **148차** — BE `b1dfd34`·`9a8bd2a`·`997831c` / FE `574bd08`·`510dbd1` G30 checklist·G34-QUAL panel·US-S02 POST·**Q314·Q319·Q320·Q294 갱신**·989/1088 |
| 2026-06-14 | **147차** — BE `726b3de`·`8615e3c` / FE `76b5ff0`·`cfd87c5`·`dbf0299` G34-QUAL BE guard·QA-B74 Fixed·UXD-97 J03 a11y·**Q318·Q319 갱신**·975/1084 |
| 2026-06-14 | **146차** — BE `fffd355`·`229f84c`·`c16f4fe` / FE `6b1258c`·`ff173af`·`443efca` J03 readiness UI·8-12 profile pagination·G34-QUAL·**Q307·Q318·Q315 갱신**·**Q319**·968/1081 |
| 2026-06-14 | **145차** — BE `bc927f7`·`bcb1d9f`·`39ee679`·`d4acab7` / FE `488f547`·`6012044`·`5bba7a2` 8-12 BE CSV·G42 결재·사후관리·#44 V103·J03 channel-status·**Q305·Q309·Q315 갱신**·**Q316~Q318**·960/1071 |
| 2026-06-13 | **144차** — BE `6a72b70`·`aaa16f8` / FE `6f6915f`·`07956f5` G30 모니터링·8-12 aggregated·export 7종·**Q308·Q314·Q315**·935/1051 |
| 2026-06-13 | **142차** — BE `8bb6583`·FE `a5c2736` G9-COG import gate·V99·apply-nhis-seeds·G9-COPAY-NAMING·UXD-94·**Q260·Q311·Q313**·902/1022 |
| 2026-06-13 | **141차** — BE `2efc557`·FE `6ef671b` G9-COG·FAQ21824 lifecycle·G-7x-1 YearMonth·**Q260·Q270·Q311·Q312**·894/1017 |
| 2026-06-13 | **140차** — BE `6f6094d`·FE `338c014` G42 pending-approval·G-7x-1-guard·US-T14 익명함 마스킹·**Q309·Q310**·886/1009 |
| 2026-06-13 | **139차** — BE `8487667`·FE `02cbd05` US-R02 직원현황 리포트·G34b import-draft API·**Q308**·882/1001 |
| 2026-06-13 | **138차** — BE `0460e9b`·FE `b0a9e06` G42 고충상담·G34b 전월 복제·G21 check-in guard·V97·**Q305·Q306·Q307**·872/989 |
| 2026-06-13 | **137차** — BE `dc48933`·FE `0ce04ad` G34b 업무수행일지 불러오기·G21 assignedUser guard·**Q303·Q304**·850/960 |
| 2026-06-13 | **136차** — BE `a7b4a39`·V95/V96·FE `22325f4`·`7b68f54`·`fad6df1` G40b 반기 기초평가·**Q302**·845/948 |
| 2026-06-13 | **135차** — BE `2589b94`·`f0752b6`·FE `2f5af63`·`e89175e` G40 대시보드 widget·V94·duplicate compliance·**Q301 갱신**·831/931 |
| 2026-06-13 | **134차** — BE `686d686`·FE `328d697`·`9f80082` G40 FE 위험도평가 UI·QA-B62·**Q301 Fixed**·**Q190 갱신**·830/925 |
| 2026-06-13 | **133차** — BE `22d736b`·`b864272`·`60789d6`·FE `4efa168` G40 admission risk assessment·V93·US-R03 per-staff compliance·G21 MIME·**Q297·Q300 갱신**·**Q301**·827/917 |
| 2026-06-14 | **132차** — BE `d4ee057`·FE `e76ca06` FAQ21806 onboarding compliance·V92·**Q290·Q298 갱신**·**Q300**·813/908 |
| 2026-06-13 | **131차** — BE `a34d0eb`·`4a622ab`·FE `9a6fdb6` G2 CMS 해지·이력·duplicate guard·**Q207·Q206 갱신**·**Q299**·807/900 |
| 2026-06-13 | **129차** — BE `1817c36`·FE `50bdb6e` G21 xls Content-Type casing·US-S02 입사일 미등록 StatCard·**Q294·Q297 갱신**·786/883 |
| 2026-06-13 | **128차** — BE `3f444a1`·FE `46f1ac0` US-R02 staff health checkup 8-10·G21 legacy xls·**Q296·Q297**·785/883 |
| 2026-06-13 | **127차** — BE `51477bd`·FE `0a7fe16` US-S02 refresher training certificate upload·**Q295**·764/871 |
| 2026-06-13 | **126차** — BE `9c9fd5b`·FE `314b380` US-S02 refresher training·G34 sign modal·US-R03 lifecycle UX·G21 import MIME·**Q278·Q288·Q294**·755/866 |
| 2026-06-13 | **125차** — BE `61336df`·FE `b3e59e2` US-R03 V87 date integrity·lifecycle Badge·**Q293**·743/853 |
| 2026-06-13 | **124차** — BE `82bdbcd`·FE `a018e71` US-R03 offboarding guard·G21 draft sync·G34 signature audit·**QA-B55 Fixed**·741/844 |
| 2026-06-13 | **123차** — BE `75440bc`·FE `f8f47e1` US-R03 staff lifecycle BE+FE·G21 `588bfb1`·**Q290 Partial Fixed**·731/843(840 PASS) |
| 2026-06-12 | **122차** — BE `728339e`·FE `479e064` G21 legacy paired guard·G24 fiscal-year parsing·G34 live E2E harness·BNK-125~127·**Q238·Q286 갱신**·**Q289~Q292**·724/827 |
| 2026-06-12 | **118차** — BE `559648f`·`209f05d`·FE `6d6b426` G34 lead caregiver work log BE+FE·G21 paired linkage guard·**Q284 Fixed**·**Q287·Q238 갱신**·**Q288**·689/800 |
| 2026-06-12 | **117차** — BE `6bfc745`·`45b8147`·FE `22bd6b7`·`352968b` LifecycleWorkflowPanel·G21 paired visit guard·**Q238 갱신**·**Q283~Q287**·675/782 |
| 2026-06-12 | **116차** — BE `3ad2a90`·FE `2cd2cd8` QA-B49 parallel fallback·G17/G32 edit-flow pilot E2E·672/778 |
| 2026-06-12 | **115차** — BE `15b3c7e`·FE `8fa9f3d` QA-B49 billing/NHIS snapshot·FE compliance snapshot-first·**Q85·Q280 갱신**·**Q282**·667/773 |
| 2026-06-12 | **114차** — BE `70d76a4`·FE `4903173` G17/G32/G38/G39 dashboard compliance snapshot·DateInput G11/G15·**Q85 갱신**·**Q280·Q281**·667/772 |
| 2026-06-12 | **113차** — BE `a0a7f9c`·FE `26499b3` G17/G32 edit UI·G39 dashboard 4-pillar·dashboard compliance counts·**Q262·Q263·Q276 갱신**·**Q279**·666/769 |
| 2026-06-12 | **112차** — BE `03211e6`·FE `4b2b082` G38 monitoring UI·branch-scoped compliance·dashboard partial-load·**Q277 Fixed**·661/765 |
| 2026-06-12 | **111차** — BE `3c7b247`·FE `a16e1fe` G38·G39·G21 import validation·G37 MIME tighten·**Q274 갱신**·**Q276~Q278**·659/751 |
| 2026-06-12 | **110차** — BE `e8de0eb`·FE `12d3b7f` G21 visit enum normalize·G37 attachment E2E·MIME fallback·**Q274 갱신**·**Q275**·642/735 |
| 2026-06-12 | **109차** — BE `0325d95`·FE `e026ae9` G37 grade history attachments·BNK-105·V78/V79·**Q176 갱신**·**Q274**·637/725 |
| 2026-06-12 | **108차** — BE `555a19f`·`838a7f6`·BNK-103~104·FE `63361c0`·`7450161`·`eb48879` J03 primary guardian·CMS FAILED response·UXD-81·BNK-102·**Q256·Q271 갱신**·**Q272·Q273**·623/705 |
| 2026-06-12 | **102차** — BE `0048105`·`e820b28`·`c5a6cec`·FE `359cf0c`·`21b1855`·`f1c60fe` G33 settle UI·G17 BNK-100/101·CMS failed debit·**Q270 Fixed**·**Q271**·608/693 |
| 2026-06-11 | **101차** — BE `70e6191`·`42bc06e`·FE `0ba2b68` G33 settle API·V77·claim guard·lock fallback·**Q270**·604/682 |
| 2026-06-11 | **100차** — BE `deaae7a`·`e7df238`·`3d5eb3e`·FE `7564c2a`·`9e1a2ed` G33 BNK-94 billing start balance·V76·**Q269**·603/679 |
| 2026-06-11 | **99차** — BE `0441a07`·`cbb7f55`·FE `7f2289b`·`fa2ad1e`·`37e6b00` UXD-79 지표29 StatCard·파일럿 fixture·US-D01 primaryGuardian·tenant filter·**Q266 Fixed**·**Q268**·584/662 |
| 2026-06-11 | **98차** — BE `208b37e`·`11277b9`·`98e40a3`·FE `932078b`·`443f379` BNK-92 G32 plan FE·지표29 compliance·hq_admin 이용자 등록·Solapi template guard·**Q265 Fixed**·**Q266·Q267**·581/654 |
| 2026-06-11 | **97차** — BE `8431b5c`·`0a270a2`·FE `18f5173` BNK-91 P2 NHIS copay·discrepancy UX·G32 plan field·CMS re-register·**Q264·Q263·Q207 갱신**·**Q265**·577/649 |
| 2026-06-11 | **96차** — BE `5e1828c`·FE `0adf8c6` BNK-87 NHIS comparison FE UI·**Q264 Fixed**·576/646 |
| 2026-06-11 | **95차** — BE `2225a7a`·`622b5e5`·FE `0821ce8`·`7eebd8c` BNK-87 NHIS comparison API·V74·G17/G32 compliance·dashboard 30일 widget·**Q262·Q263 갱신**·**Q264**·576/631 |
| 2026-06-11 | **94차** — BE `55fae99`·FE `c288fdd`·`53e4016` G17·G32 FE·G32 case management API·**Q262 Fixed**·**Q263**·569/626 |
| 2026-06-11 | **92차** — BE `22d82e2`·`8f208e4`·FE `c30aaac` US-M03 billing ledger report API·US-G04 year-coverage pre-check·**Q179 Fixed**·**Q260 갱신**·491/607 |
| 2026-06-11 | **91차** — BE `970c7af`·FE `5c0d83d`·`b9845ac` US-G04 fee schedule year guard·US-L01 bank sample xlsx·**Q258 갱신**·**Q260**·532/602 |
| 2026-06-11 | **90차** — BE `ff12473`·`aacf20b`·FE `e2c2ffe`·`758e590` G26 NTS xlsx·US-L01 8-bank guide·G21 visit slot guards·**Q227·Q252·Q234·Q199 갱신**·**Q258–Q259**·528/593 |
| 2026-06-11 | **89차** — BE `1af5b1f`·`923e610`·FE `c1d9788`·`8014dcf` G2 copayAmount null guard·G26 UI exclusion guidance·UXD-77·**Q218·Q254 갱신**·**Q257**·521/574 |
| 2026-06-11 | **88차** — BE `970f547`·`27f20de`·`6bf51c8`·FE `13272bc` G26 CMS·EASY_PAY 의료비공제 제외·G2 CMS debit integrity·US-L04 조회 UX·**Q252·Q208 갱신**·**Q254–Q256**·519/569 |
| 2026-06-11 | **87차** — BE `7f10449`·FE `7e5c806`·`0024c88`·`04f2f89` G26 medical expense deduction API·US-L04 UI·UXD-76 VehiclesPage a11y·**Q250 갱신**·**Q252–Q253**·514/567 |
| 2026-06-11 | **86차** — BE `4001510`·FE `189a00d`·`bed612c` G2 recordCopayPayment paidAt guard·US-J02 guardian portal race guards·**Q174·Q244·Q249 갱신**·**Q250–Q251**·509/555 |
| 2026-06-11 | **85차** — BE `894e246`·`64ebf6e`·FE `a03a9f9` G21 HOME_CARE alias·G2 paymentMethod guard·UXD-75 RecordsContextNav·**Q180·Q221·Q244 갱신**·**Q248–Q249**·508/553 |
| 2026-06-11 | **84차** — BE `9a97a1c`·`b5218a9`·FE `fcf713a`·`0abf164` G7 guidance API restore·G16 cross-branch fee guard·Form18 3-way workflow·**Q111·Q133·Q237 갱신**·**Q247**·503/547 |
| 2026-06-11 | **83차** — BE `ba4c9d9`·`3def542`·FE `1220bfb`·`2b6024a`·`1f71335` QA-B24 guidance UI·V70 integrity·guardian DRAFT filter·**Q111·Q133·Q212 갱신**·**Q245–Q246**·498/543 |
| 2026-06-11 | **82차** — BE `8bdead6`·`e16534c`·FE `107bfb3`·`08dbcf0` G15 care-provision·G16 VehiclesPage·G2 paidAt·**Q216·Q241 갱신**·**Q243–Q244**·497/534 |
| 2026-06-11 | **80차** — BE `9d7c17f`·FE `eef07e5` G15 Form22 log·Form18 guide·time compliance·G21 paired check-in sync·**Q230 갱신**·**Q236–Q238**·459/508 |
| 2026-06-11 | **79차** — BE `b0a88ac`·FE `49678a5` V65 transport contract integrity·G21 duplicate visit import·G2 no-op status·QA-B19 geocode guard 강화·**Q233 갱신**·**Q234·Q235**·457/485 |
| 2026-06-11 | **78차** — BE `d6d7e7f`·FE `318411d` G15 출석 transportMode 이원화·QA-B19 geocode 저장 차단·**Q232·Q233**·455/484 |
| 2026-06-10 | **77차** — BE `3d8370a`·FE `60dc5d0` G11 출석 기반 자동 가산·preview API·가드 보강·**Q225·Q229 갱신**·450/450·126/476 |
| 2026-06-10 | **76차** — BE `754160f`·FE `7387ab9` G15 transport contract API·FE 연동·V64·**Q230 갱신**·**Q231**·444/444·126/472 |
| 2026-06-10 | **75차** — BE `d5e0e01`·FE `62f022d` G11 가산율 catalog·G15 수칙 UI·US-M04 cap success banner·**Q226 갱신**·**Q229–Q230**·434/434·126/467 |
| 2026-06-10 | **74차** — BE `20bc1be`·FE `fba5ea8` G27 인지지원 월한도 BE·US-L01 bank `branchId` Fixed·**Q226·Q227·Q228 Fixed**·420/420·122/451 |
| 2026-06-10 | **73차** — BE `467cd70`·FE `9ffff0c` BNK-49 US-M04 월한도 UI·US-L01 bank UI·**Q226·Q227 갱신**·**Q228**·414/414·122/447 |
| 2026-06-10 | **72차** — BE `a92e625`·FE `ac23529` BNK-47 월한도 가드·BNK-48 은행 일괄입금·BillingSettings alias·**Q226–Q227**·401/401·118/432 |
| 2026-06-10 | **71차** — BE `b953662`·FE `25f3225` US-M03 청구 생성 기준·전월 미납 가드·V63·**Q179 갱신**·**Q224–Q225**·390/390·118/428 |
| 2026-06-10 | **70차** — BE `0854fbd`·FE `eedcc80` G2 templates 5종·납부확인서·노인학대예방 UI·G19·**Q204·Q216·Q217 갱신**·**Q221–Q223**·383/383·114/413 |
| 2026-06-10 | **69차** — BE `399bc22`·FE `dd72ff8` US-L01 payment guard·notify dedupe·normalizeAmount·**Q174·Q196 갱신**·**Q218–Q220**·377/377·113/408 |
| 2026-06-10 | **68차** — BE `f77a268`·FE `eb3f0fd` G2 email templates 3종·resolveDurationBand·**Q204·Q213 갱신**·**Q216–Q217**·371/371·113/402 |
| 2026-06-10 | **67차** — BE `0719648`·FE `3f96d95` G9 V62 snapshot·FeeScheduleMatrix·NHIS 2026 seed·**Q210–Q212 갱신**·**Q213–Q215**·365/365·110/382 |
| 2026-06-10 | **66차** — BE `06d68dd`·FE `147048c` G9 duration_band·수가표 API·US-J02·**Q48·Q91 갱신**·**Q210–Q212**·363/363·108/373 |
| 2026-06-10 | **65차** — BE `f23f15a`·FE `c4fb7ff` G21 confirm-lock UX·G2 SMTP email·V60 CMS FK·**Q204 갱신**·**Q209**·361/361·106/367 |
| 2026-06-10 | **64차** — BE `2c6e57e`·FE `c0a01b4` US-L03 CMS·FCMS stub·V59/V60·**Q41·Q287·Q203 갱신**·**Q206–Q208**·353/353·103/358 |
| 2026-06-10 | **63차** — BE `6eba2ef`·FE `c72e9df` US-J03 email channel·G2 email content·US-L02 discharged names·**Q147 갱신**·**Q204–Q205**·342/342·100/350 |
| 2026-06-10 | **62차** — BE `f755428`·FE `20bfac1` US-M02 dashboard counts·US-L02 overdue widget·BillingContextNav·V58·**Q85·Q177·Q183 갱신**·**Q202–Q203**·335/335·99/346 |
| 2026-06-09 | **61차** — BE `09932ef`·FE `69aff5d` US-L02 overdue pagination·US-L01 payment names·G21 paired sync·NHIS parse·V57·UXD-64·**Q174 갱신**·**Q197–Q201**·334/334·97/340 |
| 2026-06-09 | **60차** — BE `b63bb1f`·FE `b046444` G2 notify·US-L01/L02·US-V02 cascade cancel·BNK-26 import guard·**Q109·Q174 Partial Fixed**·**Q194–Q196**·329/329·93/323 |
| 2026-06-09 | **59차** — BE `0c069b5`·FE `75fc91e` change-password·UXD-63 visit import UI·US-J02 pagination·V56·**Q122 Fixed**·**Q189 Fixed**·**Q192–Q193**·311/311·92/316 |
| 2026-06-09 | **58차** — BE `ee3fa3a`·FE `3803247` G21 visit import·SEC-D17 settings·fieldErrors·**Q121 Partial Fixed**·**Q126 Fixed**·**Q189–Q191**·306/306·90/298 |
| 2026-06-10 | **57차** — BE `dd49204`·FE `ac5638e` UXD-62 GuardianDailySummary 식사·**Q130 Fixed**·**Q188**·288/288·89/289 |
| 2026-06-10 | **56차** — BE `dd49204`·FE `e39164d` BNK-22 US-J03-h NotificationHistoryPanel·**Q152 Fixed**·**Q187**·288/288·89/287 |
| 2026-06-10 | **55차** — BE `dd49204`·FE `1794e1c` BNK-19 US-M02-b·UXD-59 Epic K·L·**Q161 Fixed**·**Q183–Q186**·294/294·86/277 |
| 2026-06-09 | **54차** — BE `dd49204`·FE `16402b2` UXD-58 NHIS 대기 보류 UI·Region/NHIS 테스트·**Q181 Fixed**·**Q182**·288/288·81/267 |
| 2026-06-09 | **53차** — BE `4cc328d`·FE `371794f` Epic V `/visits` UI·G7 PENDING_REVIEW·V54·**Q180 Fixed**·**Q181**·269/269·80/259 |
| 2026-06-09 | **52차** — BE `1812165`·FE `dbf485e` v1.2.1 G14·US-M01~M03·V51–V53·설정 RBAC·**Q87·Q102 Fixed**·**Q176–Q180**·264/264·235/235 |
| 2026-06-09 | **51차** — FE `c7c8f07` UXD-55 GuardianBillingDetailModal·GuardianPortalPage 명세 인쇄·**Q132 Fixed**·**Q175**·217/217 |
| 2026-06-08 | **50차** — BE `598d108` v2 copay payment·overdue·V50·UXD-53/54 BranchScopeNotice·**Q173·Q174**·Q107·Q134 정정·246/246·214/214 |
| 2026-06-08 | **49차** — BE `c7941e9` pickup contact masking·pilotPageFlows T03 E2E·Q94·Q109 매뉴얼·**Q172**·Q159 정정·241/241·208/211 |
| 2026-06-08 | **48차** — ClientForm transport UI·UXD-52·**Q166 Fixed**·Q169 연락처 보강·**Q171**·241/241·68/208 |
| 2026-06-08 | **47차** — transport pickup masking·UXD-51 FE-13·FE-14·FE-15·transport live E2E·**Q169·Q170**·Q166 갱신·241/241·65/199 |
| 2026-06-08 | **46차** — transport pilot E2E·RBAC·UXD-50 forced-colors a11y·Q115 갱신·**Q168**·240/240·60/189 |
| 2026-06-08 | **45차** — US-T01 Client transport profile API·UXD-49 HQ 지점명·pilotPageFlows transport·Q129·Q159 갱신·**Q166·Q167**·231/231·60/189 |
| 2026-06-08 | **44차** — UXD-48 Recharts 복원·대시보드/출석/건강 연동·Q85·Q118·Q119 Fixed·**Q165**·226/226·60/183 |
| 2026-06-08 | **43차** — UXD-47 transport unconfirm UI·StaffPage a11y·PATCH contract·Q162·Q163 Fixed·**Q164**·226/226·58/179 |
| 2026-06-08 | **42차** — v3 §3-8 StaffPage·transport unconfirm·UXD-46·Q88 Fixed·**Q162·Q163**·226/226·55/170 |
| 2026-06-08 | **41차** — v3 meals/programs API·V49·FE·BE 연동·Q160 Fixed·**Q161**·224/224·54/164 |
| 2026-06-08 | **40차** — v1.3-A transport API Fixed·V47·V48·식사·프로그램 UI shell·Q149·Q159·**Q160**·212/212·53/157 |
| 2026-06-08 | **38차** — US-G06 DISCREPANCY compare·AlimtalkFallbackText·Q135·Q157·**Q158**·198/198·46/143 |
| 2026-06-08 | **37차** — UXD-41 US-F03 IncidentRecordForm·AlimtalkTemplateVariables·Q95·Q149·Q154·Q156·**Q157**·191/191·45/137 |
| 2026-06-08 | **36차** — Q154 Fixed·UXD-40 vitalsRanges·J03 service E2E·Q95·Q101·Q102·Q151·**Q155·Q156**·185/185·44/130 |
| 2026-06-08 | **35차** — UXD-39 건강·NHIS UI·J03 vitals DAILY_CARE·Q95·Q101·Q119·Q147·**Q154**·179/179·40/115 |
| 2026-06-07 | **34차** — US-E01~E05 출석 UI·V46·Q86·Q94·Q96·Q109·Q149·**Q153**·178/178·36/110 |
| 2026-06-07 | **32차** — UXD 15 Must 화면·ModulePage 제거·J03 투약 DAILY_CARE·Q77·Q83·Q104–Q107·Q109·Q113·Q147·Q149·**Q151**·171/171·28/89 |
| 2026-06-08 | **31차** — v1.2 P0 shell·V45·J03 DAILY_CARE/EMERGENCY·Q15·Q84·Q85·Q104–Q107·Q112·Q147·Q149·**Q150**·170/170·27/82 |
| 2026-06-08 | **30차** — Must API baseline FE 범위 정정·Q149·Q77·Q84·Q85·Q86·Q104–Q107·Q112·Q141·in-memory JWT·roleNav |
| 2026-06-08 | **29차** — Must API FE 연동·Q139·Q143·Q145·Q147·**Q148**(Solapi·V44)·152/152·40/40·baseline `136239e`/`7170b2a` |
| 2026-06-08 | **28차** — Q144 Fixed·Q147(J03 dispatch)·Q124 API 필드명·Q123·Q139 수락 본문·프론트 baseline 정정 |
| 2026-06-07 | **27차** — Q146(V40 지점명 UK)·Q123·Q144 상태값 정정, USER_MANUAL §4-7-1 B08 직원 API |
| 2026-06-07 | **26차** — Q144–Q145(TSR 56–57 V43 backend WIP·결정 59 이메일 초대·FE-18), Q123 갱신, 테스트 253/253·209/210(WT FAIL)·758 modules·27+20 dirty |
| 2026-06-07 | **25차** — Q142–Q143(COD 36 V42·GuardianListCard·MaskedPhone WIP), Q123·Q124 갱신, 테스트 253/253·209/44(WT)·758 modules |
| 2026-06-07 | **24차** — Q141(COD 35 FE-17 LogoutButton·PublicAuthLayout), Q82·Q112·Q139 갱신, 테스트 40/199·756 modules |
| 2026-06-07 | **23차** — Q139–Q140(COD 34차 GuardianInvitationAcceptPage·FE-16 ds-*·layout tests), Q123 갱신, 테스트 35/187·752 modules |
| 2026-06-07 | **22차** — Q137–Q138(TSR 48·49차 PilotChecklistJwtE2eTest·B08 staff API·FE-15 manualChunks), Q124 갱신, 테스트 34/249·34/186·393.53 kB |
| 2026-06-07 | **21차** — Q134–Q136(UXD 22차 PaymentRecordModal·ReconciliationSummaryBar·DiscrepancyComparePanel·MonthInput), Q107·Q101 부분 정정, 테스트 33/185·752 modules |
| 2026-06-07 | **20차** — Q128–Q133(UXD 20–21차 FilterChips·BillingStatusConfirmModal·HealthAlertList·GuardianDailySummary·FeeScheduleTable·CopayRateTable·NhisImportGuidePanel), Q111 부분 정정, 테스트 30/181·33/243·749 modules |
| 2026-06-07 | **19차** — Q125–Q127(LoginHistoryPanel·PasswordResetRequestModal·PlatformOrgDetailModal·SettingsPage 5탭), Q83·Q90·Q121–Q122 갱신, TSR 39차·테스트 24/169·743 modules |
| 2026-06-07 | **18차** — Q118–Q124(Recharts·HealthTrendChart·BatchProgressSteps·설정 패널·PasswordChangeModal·GuardianInvite·V41 notification), UXD 15–16차·테스트 20/161·33/240 |
| 2026-06-07 | **17차** — Q117(UXD 14차 FeeRateHistoryPanel·BATCH_STATUS·chartColors), Q91·Q105·Q77 수가표 이력 UI 부분 정정, COD 21차 `pilotPageFlows`·프론트 13파일/144건 |
| 2026-06-07 | **16차** — Q116(Switch·셀프 체크인 토글 UXD 13차), Q47·Q77·Q105 데모/설정 서술 정정, COD 20차 프론트 10파일/130건·백엔드 31클래스/213건 |
| 2026-06-07 | **15차** — Q115(UXD 12차 로그인·Modal 포커스 트랩·고대비), Q36(Vite 6)·Q112 갱신, 테스트 30클래스/190건·프론트 7파일/32건 |
| 2026-06-07 | **14차** — Q114(ThemeToggle), Q85·Q86·Q89·Q107 갱신(US-M02 대시보드·출석 모달·지점명·보호자 목록) |
| 2026-06-07 | **13차** — Q113(client_user·사진 UI-only), Q92·Q83·Q77·Q110 갱신(UXD 10차 primaryGuardian·동의 정합) |
| 2026-06-06 | **12차** — Q111–Q112(NHIS guidance·SessionTimeoutModal), Q102·Q60·Q83·Q15 갱신(US-D03 건강·출석 탭), 테스트 28클래스/127건 |
| 2026-06-06 | **11차** — Q107–Q110(v1.2 라우트·보호자 청구 API·QR 부분 연동·V39), Q62·Q84·Q87·Q105·Q106 갱신, SideNav US-UX-02 |
| 2026-06-06 | **10차** — CHANGELOG V38–V39·라우트 등록 반영, Q106 출석 통계 API 응답 불일치 정정, Q104 정정 |
| 2026-06-08 | Q104–Q105(BranchesPage 미등록·QR·설정·건강 추이 UI 골격), Q88·Q77·Q91 갱신 — App.jsx 2차 라우트 등록 반영 |
| 2026-06-07 | Q100–Q103(NHIS import·대사 필드·이용자 상세 탭·`/clients/:id/edit`), Q83 NHIS·청구 탭 행 4건 추가 |
| 2026-06-07 | Q94–Q99(출석 roster·건강 투약/사고·체크아웃 교통편·플랫폼 목록/발급·청구 yearMonth·보호자 필드 매핑), Q83 응답·본문 행 9건 추가 |
| 2026-06-07 | Q87–Q91(설정 역할 불일치·미등록 라우트·BranchSwitcher UUID·비밀번호 UI·수가표 API), Q83 역할·페이지네이션 행 추가 |
| 2026-06-07 | Q85–Q86(대시보드·결석 API-only), Q83 확장(플랫폼 검색·청구 필터), Q84 SideNav 진입 경로 표 |
| 2026-06-06 | Q83–Q84(프론트·백엔드 API 경로 불일치·SideNav), Q60–Q62·Q77 갱신 |
| 2026-06-06 | 프론트 Must 화면 API 연동 반영 — Q77·Q82·Q66·구현 상태·Q60 갱신 |
| 2026-06-06 | V36–V37·Q78–Q82(인증 rate limit·temporal sanity·NHIS claimId·프론트 JWT 미연동) |
| 2026-06-06 | V35·Q76–Q77(수가표·QR actor·Must UI 미구현 경로), Q69 actor 표 확장 |
| 2026-06-06 | V34·Q73–Q75(NHIS 수동 매칭·퇴소 시각 무결성·출석 경로 별칭) |
| 2026-06-06 | V32–V33·Q69–Q72(actor 감사·퇴소 purge·NHIS imported_at·활성 이용자 목록), Q66 청구 상태 필터 API 구현 반영 |
| 2026-06-06 | V29–V31·Q64–Q68(이메일 UK·비밀번호 재설정 세션·청구 상태 필터·대표 보호자) 추가 |
| 2026-06-06 | V28·이용자 탭 API·주민번호 복호화·QR 60분·FAQ Q53 중복 수정, Q60–Q63 추가 |
| 2026-06-06 | NHIS 대사·`hq_admin`/`caregiver`·백업·출석 통계 FAQ 추가, 구현 상태 갱신 |
| 2026-06-05 | 초안 작성 — 역할·기능별 44문항 |

---

*이 문서는 tech_writer 에이전트가 관리합니다. 요구사항·구현 변경 시 `REQUIREMENTS.md`·`CHANGELOG.md`와 동기화하세요.*
