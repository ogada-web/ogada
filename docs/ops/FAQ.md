<!-- doc:owner=TWR doc:audience=PLN,COD updated=2026-06-06T22:35:00+09:00 -->
# ogada 자주 묻는 질문 (ops/FAQ.md)

> **작성**: tech_writer 에이전트  
> **최초 작성일**: 2026-06-05  
> **상태**: 초안 (Draft)  
> **대상 독자**: 주간보호센터 **현장 사용자**, **센터 운영·IT 담당**, **ogada 플랫폼 운영자**  
> **기준 문서**: `docs/planning/REQUIREMENTS.md`, `docs/technical/API_SPEC.md`, `docs/planning/FLOWCHART.md`, `docs/ops/USER_MANUAL.md`, `docs/ops/ADMIN_GUIDE.md`  
> **기술 스택**: Java Spring Boot 3.x + React (Vite SPA) + PostgreSQL

---

## 1. 이 FAQ에 대하여

ogada 도입·운영 과정에서 자주 반복되는 질문을 **역할·기능별**로 정리했습니다.  
상세 조작 절차는 [`USER_MANUAL.md`](ops/USER_MANUAL.md), 플랫폼·기술 관리는 [`ADMIN_GUIDE.md`](ops/ADMIN_GUIDE.md), 배포·인프라는 [`DEPLOYMENT_GUIDE.md`](ops/DEPLOYMENT_GUIDE.md)를 참고하세요.

### 구현 상태 안내 (2026-06-06 기준)

| 영역 | 상태 | FAQ에서의 의미 |
|------|------|----------------|
| 백엔드 API | **Must 범위 구현** | 인증(rate limit 포함)·플랫폼·이용자·출석·건강·청구·대시보드·설정 REST API 동작 |
| 데이터베이스 | Flyway **V1–V39** | V38 NHIS 지점 목록 인덱스, V39 `guardian_link_status`·보호자 연결 트리거 |
| 프론트엔드 | **Must 핵심 화면 API 연동** | JWT·SideNav·이용자·출석·건강·청구·NHIS 대사·플랫폼·보호자 포털 UI. **`/branches`·`/attendance/stats` 라우트 등록**(Q104 정정·Q106). `services.js` 경로·응답·본문 불일치(Q83·Q92·Q94–Q101)·대시보드·결석·API 미연동 UI 후속 |
| 본 FAQ | **구현·목표 병기** | UI 연동 완료 항목은 「화면 구현됨」, API만 있는 항목은 「API 구현됨」으로 구분 |

---

## 2. 서비스 개요

### Q1. ogada는 무엇인가요?

**A.** ogada는 전국 주간보호센터·요양기관 운영법인을 위한 **B2B SaaS 클라우드 웹 시스템**입니다. 이용자 관리, 출석(수기·QR), 건강 기록, 청구·정산, 다지점 대시보드 등 일상 운영 업무를 디지털화합니다. PC·태블릿·스마트폰 브라우저에서 반응형으로 사용합니다.

### Q2. 개인 센터 1곳만 쓰는 전용 프로그램인가요?

**A.** 아닙니다. **전국 판매용 멀티테넌트 SaaS**입니다. 운영법인 1곳이 `Organization`(Tenant) 1개이며, 여러 법인이 동일 플랫폼을 사용하되 **데이터는 완전히 분리**됩니다.

### Q3. 케어포·이지케어 같은 기존 ERP와 무엇이 다른가요?

**A.** ogada는 **주간보호센터 운영에 특화된 SaaS**로 설계되었습니다. 청구·정산은 케어포와 유사한 **2단계 모델**(내부 계산 + 공단 엑셀 import)을 따르며, **다지점 통합 대시보드**, **보호자 QR 셀프 체크인(B방식)**, **테넌트 격리**를 MVP부터 포함합니다. 공단 포털 직접 전송·CMS 결제·알림톡은 MVP 이후 검토입니다.

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

**A.** **이용자 등록·수정은 `branch_admin`, `social_worker`** 권한입니다. `caregiver`는 **출석·건강 기록 입력**과 이용자 목록 **조회**가 주 업무입니다.

---

## 5. 다지점·데이터 보안

### Q13. 지점이 2곳 이상일 때 데이터가 섞이지 않나요?

**A.** 이용자·출석·건강·청구 등 운영 데이터는 **`branch_id`로 소속 지점**이 식별됩니다. `branch_admin` 이하 역할은 **자신의 `branch_ids` 범위만** 접근합니다. `hq_admin`은 통합 조회가 가능하나, 쓰기는 선택 지점으로 제한됩니다.

### Q14. 다른 센터(법인) 데이터를 볼 수 있나요?

**A.** **불가능합니다.** 모든 API는 JWT의 `organization_id`로 **테넌트 격리**를 강제합니다. A센터 계정으로 B센터 이용자·출석 데이터에 접근할 수 없습니다.

### Q15. 30분 동안 아무 것도 안 하면 어떻게 되나요?

**A.** **세션이 만료**되어 로그인 화면으로 돌아갑니다 (access token 30분). 공용 PC 사용 후에는 **로그아웃** 또는 브라우저 종료를 권장합니다.

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

**A.** **화면에서 관리**합니다(B방식). `hq_admin`이 **연도·등급별 1일 수가**를 입력·수정하며, 개정 이력이 보존됩니다. 과거 확정 청구는 **당시 수가 버전**을 유지합니다.

### Q30. 본인부담률(15%/9%/6%/0%)은 이용자마다 다른가요?

**A.** **예.** 이용자 등록 시 **본인부담 구분**(`copayType`)을 저장합니다.

| 구분 코드 | 대표 비율 |
|-----------|----------|
| `GENERAL` | 15% |
| `REDUCED_40` | 9% |
| `REDUCED_60` | 6% |
| `MEDICAID` | 0% |

실제 비율 수치는 `copay_rates` 테이블에서 개정 대응 가능합니다.

### Q31. 공단 「청구내역상세」엑셀은 어떻게 쓰나요?

**A.** 롱텀에서 다운로드한 엑셀을 ogada **`/billing` → 엑셀 import** (`POST /api/v1/billing/imports/nhis`)로 업로드하면 공단 청구 건수와 내부 데이터를 **대조**합니다. 케어포식 연동과 동일한 2단계 모델의 일부입니다.

업로드 후 각 행은 다음 상태로 표시됩니다.

| 상태 | 의미 |
|------|------|
| `MATCHED` | 공단 데이터와 ogada 이용자·청구 일치 |
| `UNMATCHED` | 이용자 매칭 실패 — 인정번호·이름 확인 |
| `DISCREPANCY` | 이용자는 매칭되었으나 일수·금액 불일치 |

> **구현됨**: `NhisImportService`, Flyway V19–V20 대사 무결성 제약.

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
| 프론트엔드 | React 18, Vite 5 SPA |
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
| 본인부담금 CMS·간편결제 | 후속 |
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

**A.** **예.** `GET /api/v1/attendance/stats/monthly`로 지점·기간별 출석 통계를 조회합니다 (2026-06-06 구현). 프론트엔드 **월별 출석 리포트 화면**은 아직 미구현이며, 대시보드(`/dashboard`)도 데모 데이터만 표시합니다.

### Q48. 수가표를 수정하면 과거 청구에 영향을 주나요?

**A.** **아니요.** `PATCH /api/v1/billing/fee-schedules/{id}`는 **이력 보존** 방식으로 새 버전을 생성합니다. 이미 **확정**된 청구는 생성 시점의 수가 스냅샷(`daily_rate_snapshot`)을 유지합니다 (Flyway V8 확정 청구 불변성).

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
| **청구** | **부분** — 표 UI 있음. 프론트가 `GET /billing/claims?clientId=`를 호출 중이면 백엔드가 무시해 **빈 목록** 가능 → `GET /clients/{id}/billing` 정합 필요 (Q83) |
| **출석·건강** | **탭 스텁** — 안내 문구·`/health?clientId=` 링크만. API는 Swagger로 확인 가능 |

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

> **경로 정합 (Q83)**: 프론트 `services.js`는 `/guardian/clients`·`/clients/:id/summary`·`/billing`을 호출합니다. 백엔드와 불일치 시 포털 로드 오류 — coder가 `checkin-targets`·`daily-records`로 정합하거나 백엔드 alias 추가 예정.

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

**A.** **아니요.** 동일 상태로의 변경(no-op)은 API에서 거부되며, V31 `chk_claim_status_history_distinct_transition` CHECK로 **상태 이력에도 기록되지 않습니다**. 실제 전이(`DRAFT→CONFIRMED→PAID`)만 허용됩니다.

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

**A.** 2026-06-06 기준 **백엔드 Must API는 구현 완료**이며, 프론트엔드 **핵심 업무 화면도 JWT·REST API 연동**이 진행되었습니다.

| 화면 | UI 상태 | 비고 |
|------|---------|------|
| `/`(로그인) | **구현됨** | 이메일·비밀번호 JWT 로그인 |
| `/clients` 이용자 CRUD | **구현됨** | 목록·등록·수정·상세(기본·청구 탭, SSN [열람]) |
| `/attendance` 수기 출석 | **구현됨** | 체크인/아웃. 결석 사유 입력 UI 후속 |
| `/health` 건강 기록 | **부분** | 입력 UI만 — 이력 조회·그래프 후속 |
| `/billing` 청구·상태 필터 | **구현됨** | 생성·상태 변경·필터 |
| `/billing/nhis-import`·`:batchId` | **구현됨** | 업로드·배치 목록·`ReconciliationPage` 수동 매칭 |
| `/platform` Tenant 온보딩 | **구현됨** | 등록·검색·첫 `hq_admin` 발급 |
| `/guardian` 보호자 포털 | **부분** | 탭 UI(오늘 현황·명세·청구). **API 경로 불일치** — Q62·Q83 |
| `/dashboard`, `/dashboard/hq` | **데모** | StatCard 하드코딩 — `GET /dashboard/*` 연동 후속 |
| `/settings`, `/billing/fee-schedules`, `/billing/copay-rates` | **UI 골격** | 탭·폼 레이아웃 있음. **API·저장 미연동** (FAQ Q91·Q105) |
| `/attendance/qr/generate`, `/guardian/checkin` | **UI 골격** | 라우트 등록됨. **QR 생성·스캔 API 미연동** — Swagger (FAQ Q88·Q105) |
| `/health/:clientId` | **UI 골격** | 차트 플레이스홀더. `GET /clients/{id}/health` 미연동 (FAQ Q105) |
| `/branches` | **구현됨** | `BranchesPage` — 목록·등록/수정 모달·`GET/POST/PATCH /branches` 연동 (FAQ Q104) |
| `/attendance/stats` | **부분** | `AttendanceStatsPage` — UI·API 호출 있음. **쿼리·응답 구조 불일치** (FAQ Q106) |

미연동 화면은 **Swagger UI**·Postman으로 검증할 수 있습니다.

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

**A.** **예.** 로그인 화면(`/`)에서 `POST /api/v1/auth/login`으로 access·refresh 토큰을 발급받고, `AuthContext`가 `localStorage`(`ogada.session`)에 세션을 저장합니다. 이후 `src/api/http.js`가 `Authorization: Bearer` 헤더로 API를 호출합니다.

| 항목 | 상태 |
|------|------|
| JWT 로그인·역할 가드 | **구현됨** |
| 지점 전환(`active-branch`) | **구현됨** — Branch Switcher |
| 로그아웃 UI | **미구현** — `POST /auth/logout` API는 존재 |
| refresh 자동 갱신 | **후속** — 토큰 만료 시 수동 재로그인 |

> 보안 권장: refresh 토큰을 httpOnly cookie로 이전하는 작업은 `SECURITY_CHECKLIST.md` A-3-4 항목을 참고하세요.

### Q83. 화면은 있는데 API 호출이 실패합니다. 경로가 다른가요?

**A.** **예.** 2026-06-06 기준 프론트 `src/api/services.js`와 백엔드 구현 간 **경로·메서드 불일치**가 있습니다. coder 정합 전까지 Swagger·Postman으로 백엔드 정식 API를 사용하세요.

| 화면·기능 | 프론트 호출 (현재) | 백엔드 정식 API | 증상 |
|----------|-------------------|----------------|------|
| 이용자 상세 주민번호 [열람] | `GET /clients/{id}/ssn` | `POST /clients/{id}/resident-registration/reveal` | [열람] 클릭 시 404·405 |
| 이용자 상세 청구 탭 | `GET /billing/claims?clientId=` | `GET /clients/{id}/billing` | 청구 탭 빈 목록·전체 청구 혼입 |
| `/billing` 월·이용자 필터 | `GET /billing/claims?yearMonth=&clientId=` | `GET /billing/claims?branchId=&status=` (`yearMonth`·`clientId` **미지원**) | 월 선택이 목록에 반영되지 않음 |
| `/platform` 고객 검색 | `GET /platform/organizations?q=` | `GET /platform/organizations?query=` | 검색어 무시·전체 목록 |
| 이용자 등록·수정 (`/clients/new`) | `ssnConsentGiven`, `guardianName`·`guardianPhone`·`notes` 등 | `consentToCollectResidentRegistrationNo`만 허용, 보호자는 **별도 API** | `400 VALIDATION_ERROR`·보호자 미연결 (FAQ Q92) |
| 보호자 포털 목록·요약 | `GET /guardian/clients`, `GET /guardian/clients/{id}/summary` | `GET /guardian/checkin-targets`, `GET /guardian/daily-records?clientId=` | 포털 로드 오류 |
| 보호자 명세·청구 탭 | `GET /guardian/clients/{id}/billing` | **미구현** (v1.1) | 탭 빈 목록 |
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

**역할 가드 불일치** (경로가 아닌 권한):

| 화면 | `ProtectedRoute` 허용 역할 | 백엔드 API 실제 권한 | 증상 |
|------|---------------------------|---------------------|------|
| `/settings` | `sysadmin`, `hq_admin`, `platform_admin` | `SettingsController` — **`SYSADMIN`만** | `hq_admin`이 화면 진입 후 API 403 |
| `/billing/fee-schedules` | `hq_admin`, `platform_admin` | 수가표 API — **`HQ_ADMIN`만** | `platform_admin` 403 |

정합 작업은 프론트 `services.js` 수정 또는 백엔드 alias·쿼리 파라미터 수용 중 택일 — `PLAN_NOTES.md` §문서 작성 질문 TWR-Q1 참고.

### Q84. 역할마다 보이는 메뉴(SideNav)는 어디서 정의되나요?

**A.** 프론트 `src/components/ui/SideNav.jsx`의 `NAV_CONFIG`가 JWT `role`별 메뉴를 결정합니다. `App.jsx` `ProtectedRoute allow`와 **함께** 권한을 제한합니다.

| 역할 | 주요 메뉴 (2026-06-06) |
|------|------------------------|
| `caregiver` | 대시보드, 출석 체크인, QR 생성, 건강 기록 |
| `social_worker` | 대시보드, 이용자, 출석 통계, 건강 기록 |
| `branch_admin` | 대시보드, **지점 관리**, 이용자, 출석, **출석 통계**, QR 생성, 건강, 청구 |
| `hq_admin` | 통합·지점 대시보드, **지점 관리**, 이용자, 출석, **출석 통계**, QR 생성, 건강, 청구, 수가표(스텁), 본인부담(스텁), 설정(스텁) |
| `guardian` / `client_user` | 이용자 현황, **QR 체크인** |
| `platform_admin` | 고객사 관리, 설정(스텁) |
| `sysadmin` | 시스템 설정(스텁) |

Must 화면 중 **라우트만 있고 SideNav 미노출** — `/billing/nhis-import`, `/clients/:id` 상세 등은 청구·이용자 화면 내 링크로 진입합니다.

| 화면 | 진입 경로 |
|------|----------|
| 공단 엑셀 import | `/billing` → **「공단 엑셀 import」** 버튼 |
| NHIS 대사 상세 | `/billing/nhis-import` 배치 클릭, 또는 청구 행 **「대조」** |
| 이용자 상세 | `/clients` 목록 행 클릭 |

### Q85. 대시보드(`/dashboard`) 숫자가 실제와 다릅니다. API는 있나요?

**A.** **예.** 백엔드 Must API는 구현되어 있으나, 프론트 `DashboardPage`는 **StatCard 데모 값(하드코딩)** 만 표시합니다.

| 역할 | API | 주요 응답 |
|------|-----|----------|
| 센터장·요양보호사 등 | `GET /api/v1/dashboard/branch` | `todayAttendance`(입소·결석·퇴소), `clientStats`, `healthAlerts`, `monthlyAttendanceRates` |
| 통합 관리자 | `GET /api/v1/dashboard/hq` | 지점별 `branchSummaries`, 통합 집계 |
| 통합 관리자 | `GET /api/v1/dashboard/hq/alerts` | 전 지점 건강 이상 목록 |

공통 쿼리: `?date=YYYY-MM-DD&from=YYYY-MM-DD&to=YYYY-MM-DD&branchId=<uuid>` (`date` 생략 시 오늘, `from`/`to` 생략 시 최근 6개월).

> UI 연동 전까지 **Swagger UI**·Postman으로 JWT와 함께 호출해 실데이터를 확인하세요. [`USER_MANUAL.md`](ops/USER_MANUAL.md) §4-2·§5-2.

### Q86. 출석 화면에서 결석 사유를 입력할 수 없어요.

**A.** `/attendance` UI는 **체크인/아웃만** 구현되어 있고, **결석 사유 입력 버튼은 후속**입니다. 백엔드 API는 동작합니다.

| 항목 | 내용 |
|------|------|
| API | `POST /api/v1/attendance/absence` |
| 본문 | `{ "clientId": "<uuid>", "absenceReason": "병원 방문" }` |
| 권한 | `caregiver`·`branch_admin`·`social_worker`·`hq_admin` |
| 규칙 | 당일 1행, 출석(`check_in_at`)과 **상호 배타**(V11). 결석은 **수기(`manual`)만** (V14) |

Swagger로 등록한 뒤 `/attendance` 목록을 새로고침하면 **결석** StatCard·행 상태가 반영됩니다.

---

## 13-10. 프론트 라우트·UX 갭 (2026-06-07 신규)

### Q87. `/settings`에 들어갔는데 「권한이 없습니다」가 나와요. `hq_admin`인데요.

**A.** **프론트 라우트 가드와 백엔드 API 권한이 다릅니다.**

| 계층 | `/settings` 접근 |
|------|-----------------|
| `App.jsx` `ProtectedRoute` | `sysadmin`, `hq_admin`, `platform_admin` **허용** |
| `SettingsController` (`/settings/*`) | **`SYSADMIN`만** (`@PreAuthorize`) |

`hq_admin`·`platform_admin`은 화면(플레이스홀더)까지는 열리지만, 감사·백업 API 호출 시 `403 FORBIDDEN_SCOPE`가 납니다. **Tenant 기술 설정은 `sysadmin` 계정**으로 Swagger·Postman을 사용하세요. 전사 운영 정책(`allow_client_self_checkin`)은 `hq_admin`이 `PATCH /api/v1/organization/settings`로 변경합니다 (§6-3, ADMIN_GUIDE).

### Q88. 메뉴에 있는데 「페이지를 찾을 수 없습니다」/로그인으로 돌아가요. 라우트가 없나요?

**A.** 2026-06-06 기준 **대부분 Must 경로는 `App.jsx`에 등록**되었습니다. 아래만 **미등록**이며, `*` fallback으로 `/` 로그인 화면으로 리다이렉트됩니다.

| 경로 | Must 여부 | UI (2026-06-06) | 백엔드 API |
|------|----------|-----------------|-----------|
| `/users` | Should→MVP 일부 | **페이지 파일 없음** | `/users` CRUD |

**등록됨·API 미연동 (화면은 열리나 동작 안 함)**

| 경로 | UI | 백엔드 API | 비고 |
|------|-----|-----------|------|
| `/attendance/qr/generate` | `QrGeneratePage` — 유형 선택·인쇄 레이아웃 | `POST/GET /branches/{id}/qr` | **QR 생성 버튼 TODO** (FAQ Q105) |
| `/guardian/checkin` | `GuardianCheckinPage` — 대상 선택·스캔 버튼 | `GET /guardian/checkin-targets`, `POST /attendance/qr/scan` | **카메라·API TODO** (FAQ Q105) |
| `/billing/fee-schedules` | `FeeSchedulePage` — 등급별 입력 폼 | `GET/POST/PATCH /billing/fee-schedules` | **저장·조회 미연동** (FAQ Q91) |
| `/billing/copay-rates` | `CopayRatePage` — 4구분 비율 폼 | `GET/PATCH /billing/copay-rates` | **저장·조회 미연동** |
| `/settings` | `SettingsPage` — 일반·백업·감사 탭 | `/settings/*` (**`SYSADMIN`만**) | **API 미연동·역할 불일치** (FAQ Q87) |
| `/health/:clientId` | `HealthDetailPage` — 차트 플레이스홀더 | `GET /clients/{id}/health?days=` | **데이터·차트 미연동** (FAQ Q105) |

SideNav **「QR 생성」**·**「QR 체크인」**·**「수가표 관리」** 등은 이제 **404 없이** 해당 화면으로 이동합니다. 실제 업무 처리는 Swagger 또는 coder API 연동 완료 후 가능합니다.

### Q89. 지점 선택기에 지점명이 아니라 긴 영문·숫자(UUID)만 보여요.

**A.** **프론트가 지점명 API를 호출하지 않습니다.** `AttendancePage`·`BillingPage` 등에서 `BranchSwitcher`에 전달하는 목록이 JWT `branchIds`를 `{ id, name: id }`로 매핑한 결과입니다 (`GET /api/v1/branches` 미호출).

| 항목 | 내용 |
|------|------|
| 동작 | 지점 전환 자체는 `POST /auth/active-branch`로 **정상** |
| 표시 | 옵션 라벨이 **UUID**로 보임 — UX 혼동 가능 |
| 우회 | Swagger로 `GET /branches` 조회 후 UUID↔지점명 대조 |
| 수정 | coder가 `fetchBranchesApi` 연동 후 `branch.name` 표시 예정 |

### Q90. 로그인 화면에 「비밀번호 찾기」가 없어요.

**A.** **백엔드 API는 구현**되어 있으나 **로그인 UI에는 링크·폼이 없습니다** (`LoginPage.jsx`).

| API | 용도 |
|-----|------|
| `POST /api/v1/auth/password/reset-request` | 등록 이메일로 재설정 링크 발송 |
| `POST /api/v1/auth/password/reset` | 토큰으로 새 비밀번호 설정 |

비밀번호 분실 시 **센터 `hq_admin`·`branch_admin`**에게 계정 확인을 요청하거나, IT 담당이 Swagger로 `reset-request`를 호출합니다. 재설정 완료 시 **모든 refresh 세션이 폐기**됩니다 (FAQ Q65).

### Q91. 수가표·본인부담 비율은 화면 없이 어떻게 등록하나요?

**A.** `/billing/fee-schedules`·`/billing/copay-rates`는 **2026-06-08 UI 골격이 등록**되어 등급·비율 입력 폼이 보이지만, **`services.js`에 API 함수가 없고 저장 버튼이 연동되지 않았습니다**. 당분간 `hq_admin` JWT로 Swagger에서 호출합니다.

**수가표 등록** — `POST /api/v1/billing/fee-schedules`

```json
{ "year": 2026, "ltcGrade": 3, "dailyRate": 68000, "extras": { "meal": 0 } }
```

**본인부담 비율 확인·수정** — `GET /api/v1/billing/copay-rates`, `PATCH /api/v1/billing/copay-rates/{copayType}`

```json
{ "rate": 0.15 }
```

등록 시 `fee_schedules.created_by`에 행위자 UUID가 자동 기록됩니다 (V35). 월말 청구 전 **해당 연도·등급 수가가 1건 이상** 있어야 `POST /billing/claims/generate`가 성공합니다.

### Q92. 이용자 등록 화면에서 「저장 실패」·「동의가 필요합니다」가 나와요.

**A.** `/clients/new`(`ClientFormPage`)는 UI에서 보호자·동의 필드를 수집하지만, **백엔드 `CreateClientRequest`와 본문 필드명·구조가 다릅니다** (Q83 확장).

| 프론트 전송 (현재) | 백엔드 기대 | 결과 |
|-------------------|------------|------|
| `ssnConsentGiven: true` | `consentToCollectResidentRegistrationNo: true` | 동의 미인식 → `400` (「주민등록번호 수집·이용 동의가 필요합니다」) |
| `guardianName`·`guardianPhone`·`guardianRelation` | **`primaryGuardian: { guardianUserId, relationship }` 필수** (V39) | `400` — 보호자 미연결·`guardian_link_status=PENDING` 잔존 금지 |
| `notes` | **미지원** | 무시됨 |

**Swagger 우회 (Must 목표 흐름 — 단일 트랜잭션)**

1. `POST /api/v1/users` — 보호자(`guardian`) 계정을 **먼저** 생성 (`hq_admin`·`branch_admin` JWT).
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

등록 성공 시 `clients.guardian_link_status`가 **`LINKED`**로 설정됩니다 (V39). 추가 보호자는 `POST /api/v1/clients/{clientId}/guardians`로 연결합니다.

> UI 연동 전까지 등록 화면의 보호자 입력란은 **참고용**이며, 백엔드는 **기존 `guardian` 계정 UUID**가 필요합니다.

### Q93. URL을 직접 입력했더니 「권한이 없습니다」(`/forbidden`) 화면이 나와요.

**A.** **역할과 경로가 맞지 않을 때** `ProtectedRoute`가 `/forbidden`(`ForbiddenPage`)으로 보냅니다. 로그인 화면(`/`)으로 돌아가는 **미등록 라우트(Q88)** 와 다릅니다.

| 상황 | 이동 경로 | 화면 |
|------|----------|------|
| 미로그인 | 보호 경로 접근 | `/` 로그인 |
| 로그인했으나 역할 불일치 | 예: `caregiver`가 `/billing` 직접 입력 | `/forbidden` |
| 라우트 미등록 | 예: `/users` | `/` (fallback) |

**조치**: SideNav 메뉴·역할별 홈(`AuthContext` `roleHomePaths`)으로 이동하세요. 권한 변경이 필요하면 센터 **`hq_admin`**에게 역할 수정을 요청합니다.

---

## 13-11. 프론트 응답·본문 정합 (2026-06-07 6차)

### Q94. 출석 화면에 이용자 이름이 없고 체크인 버튼이 안 보여요.

**A.** `/attendance`는 백엔드 `AttendanceItemResponse`와 **UI가 기대하는 필드·roster 구조가 다릅니다** (Q83 확장).

| 프론트 기대 | 백엔드 실제 | 증상 |
|------------|------------|------|
| `name`, `status`(`PENDING`/`CHECKED_IN`/`CHECKED_OUT`/`ABSENT`) | `clientId`만, **상태 필드 없음** | 이름 빈칸, `PENDING` 미표시 → **체크인 버튼 미노출** |
| `checkInTime`, `checkOutTime` | `checkInAt`, `checkOutAt`(ISO 8601) | 시각 열 빈칸 |
| 당일 **전체 이용자** 명단 | **당일 출석 기록이 있는 행만** 반환 | 미처리 이용자가 목록에 **아예 없음** |

**우회 (파일럿 수기 출석)**

1. `/clients`에서 이용자 UUID 확인.
2. Swagger `POST /api/v1/attendance/check-in` — `{ "clientId": "<uuid>" }` (경로 별칭 `/checkin` 동일).
3. 귀가: `POST /api/v1/attendance/check-out` — `{ "clientId": "<uuid>", "transportType": "SELF" }` (FAQ Q96).

> coder 정합: `GET /clients?branchId=` roster와 출석 행을 병합하거나, 백엔드가 전체 roster+상태를 반환하도록 확장 예정 (`PLAN_NOTES.md` TWR-Q1).

### Q95. 건강 기록「투약」「낙상·사고」저장이 실패합니다. 바이탈은 됩니다.

**A.** `/health`의 **투약·사고 폼 본문**이 백엔드 DTO와 다릅니다. 바이탈(`POST .../health/vitals`)은 정상 동작합니다.

| 유형 | 프론트 전송 (현재) | 백엔드 기대 |
|------|-------------------|------------|
| 투약 | `drugName`, `dosage`, `administeredAt`(시간), `notes` | `recordedAt`, `medicationName`, `dosage`, `administeredAt`(OffsetDateTime), **`administeredBy`** |
| 사고 | `eventType`, `description`, `occurredAt` | **`recordedAt`**, `incidentType`, `detail` |

`administeredBy`·`recordedAt` 누락 시 `400 VALIDATION_ERROR` — 「건강 기록 저장에 실패했습니다」.

**Swagger 우회 — 투약** `POST /api/v1/clients/{id}/health/medications`

```json
{
  "recordedAt": "2026-06-06T10:00:00+09:00",
  "medicationName": "타이레놀",
  "dosage": "500mg",
  "administeredAt": "2026-06-06T10:00:00+09:00",
  "administeredBy": "요양보호사 김"
}
```

**Swagger 우회 — 사고** `POST /api/v1/clients/{id}/health/incidents`

```json
{
  "recordedAt": "2026-06-06T14:30:00+09:00",
  "incidentType": "FALL",
  "detail": "복도에서 미끄러짐, 경상"
}
```

> 바이탈 폼의 `notes`는 `VitalsCreateRequest`에 **필드가 없어** 저장되지 않습니다. 특이사항은 `POST .../health/notes` API를 사용하세요.

### Q96. 체크아웃 후 귀가 교통편이 저장되지 않아요.

**A.** 체크아웃 본문 필드명·값 형식이 다릅니다.

| 프론트 | 백엔드 |
|------|--------|
| `transportMethod`: `"자가용"`, `"센터 차량"` 등 한글 | `transportType`: `SELF`, `CENTER_VEHICLE`, `WALK`, `OTHER` |

프론트 한글 문자열은 검증 후 **무시**되거나 저장되지 않을 수 있습니다.

**Swagger**: `POST /api/v1/attendance/check-out`

```json
{ "clientId": "<uuid>", "transportType": "SELF" }
```

| 코드 | 의미 |
|------|------|
| `SELF` | 자가용 |
| `CENTER_VEHICLE` | 센터 차량 |
| `WALK` | 도보 |
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

명세·청구 탭(`GET /guardian/clients/{id}/billing`)은 v1.1 범위로 **미구현**입니다 (Q83).

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

> `ReconciliationPage`는 `result.batch`·`result.rows` 래퍼를 기대하지만 API는 **평면 객체**(`yearMonth`, `rows` 최상위)를 반환합니다. `loadDetail`의 `result.batch \|\| result` 폴백으로 배치 메타는 일부 표시되나 필드명 불일치는 남습니다.

### Q102. 이용자 상세(`/clients/:id`) 건강·출석 탭과 청구 상태가 비어 있어요.

**A.** `ClientDetailPage`는 **4탭 UI**가 있으나 탭별 API 연동 수준이 다릅니다.

| 탭 | UI (2026-06-07) | 백엔드 API | 증상 |
|----|----------------|-----------|------|
| 기본정보 | **연동** (SSN [열람]은 Q83 경로 불일치) | `GET /clients/{id}` | — |
| 건강 | **스텁** — 「전체 기록 보기」링크만 | `GET /clients/{id}/health` (기록 목록) | 탭 본문 빈 안내 |
| 출석 | **스텁** — 안내 문구만 | `GET /clients/{id}/attendance?from=&to=` | 최근 한 달 이력 미표시 |
| 청구 | **부분** — `fetchClaimsApi(?clientId=)` 사용 | `GET /clients/{id}/billing` | 목록 빈칸 또는 전체 청구 혼입 (Q83) |

**청구 탭 필드** (API 연결 후에도 Badge가 비면):

| UI | API (`ClientBillingHistoryItemResponse`) |
|----|------------------------------------------|
| `billingMonth` | `yearMonth` |
| `status` | `claimStatus` |

건강·출석 탭 실데이터는 **`/health?clientId=`** 또는 Swagger로 각 API를 호출하세요.

### Q103. 이용자 **수정**은 어디서 하나요? `/clients/:id/edit`이 있나요?

**A.** **예.** 2026-06-06 UXD 2차 이후 **`/clients/:id/edit` 라우트가 등록**되어 있으며, 상세 화면 우측 **「수정」** 버튼으로 이동합니다 (`ClientFormPage` 수정 모드).

| 항목 | 내용 |
|------|------|
| 권한 | `branch_admin`, `social_worker`, `hq_admin` |
| API | `PATCH /api/v1/clients/{id}` |
| 신규 등록과 동일 이슈 | `ssnConsentGiven` → `consentToCollectResidentRegistrationNo`, 보호자 필드 본문 미지원 (FAQ Q92) |
| 주민번호 | 수정 시 `residentRegistrationNo` 재전송 없으면 기존 값 유지 — 동의 체크만으로는 PATCH 검증 실패 가능 |

퇴소·사진 업로드는 **여전히 UI 없음** — `POST /clients/{id}/discharge`, `POST /clients/{id}/photo` (Swagger).

---

## 13-12. 프론트 라우트·UI 골격 (2026-06-08 8차)

### Q104. `/branches` 지점 관리는 어떻게 쓰나요?

**A.** **`/branches` 라우트가 `App.jsx`·`SideNav`에 등록**되어 있으며, `BranchesPage`가 백엔드 `/branches` CRUD와 연동됩니다.

| 항목 | 내용 |
|------|------|
| 페이지 | `src/pages/BranchesPage.jsx` — 목록·등록/수정 모달·비활성 |
| API | `GET/POST/PATCH /api/v1/branches` — **연동됨** |
| 권한 | `hq_admin` CRUD, `branch_admin` 조회·등록(백엔드 최종 인가) |
| SideNav | `hq_admin`·`branch_admin` **「지점 관리」** 메뉴 |

> `/users` 직원 관리는 **페이지 파일이 없습니다** (Q88). 직원 계정은 Swagger `POST /users`를 사용하세요.

### Q105. QR·설정·건강 추이 화면은 열리는데 버튼이 동작하지 않아요.

**A.** 2026-06-08 **`App.jsx` 2차 라우트 등록**으로 아래 화면이 **404 없이 열립니다**. 공통적으로 **UI 레이아웃만 있고 API·카메라 연동은 TODO**입니다.

| 경로 | 컴포넌트 | 미연동 항목 | 백엔드 API |
|------|---------|------------|-----------|
| `/attendance/qr/generate` | `QrGeneratePage` | **QR 생성** 클릭 시 `setQrPreview(null)` — API 미호출 | `POST/GET /branches/{id}/qr` |
| `/guardian/checkin` | `GuardianCheckinPage` | `checkin-targets` 목록 빈 배열, **카메라 스캐너 미구현** | `GET /guardian/checkin-targets`, `POST /attendance/qr/scan` |
| `/health/:clientId` | `HealthDetailPage` | 차트 **플레이스홀더** (`ds-chart-placeholder`) | `GET /clients/{id}/health?days=7\|30` |
| `/billing/fee-schedules` | `FeeSchedulePage` | **저장·이력** 버튼 미연동 | `/billing/fee-schedules` |
| `/billing/copay-rates` | `CopayRatePage` | **저장** 버튼 미연동 | `/billing/copay-rates` |
| `/settings` | `SettingsPage` | 탭 본문 **TODO** 주석 | `/settings/system`, `/audit-logs`, `/backups` |

**우회**: QR·체크인·수가·설정은 Swagger. 건강 추이는 `/health` 당일 입력 또는 Swagger `GET /clients/{id}/health`.

### Q106. 출석 통계(`/attendance/stats`) 화면에 숫자가 비어 있어요.

**A.** `AttendanceStatsPage`는 API를 호출하지만, **쿼리 파라미터·응답 구조가 백엔드와 다릅니다** (Q83 확장).

| 항목 | 프론트 (현재) | 백엔드 정식 API |
|------|--------------|----------------|
| 쿼리 | `?branchId=&yearMonth=YYYY-MM` | `?from=YYYY-MM-DD&to=YYYY-MM-DD&branchId=` (`yearMonth` **미지원**) |
| 응답 기대 | `{ summary: { operatingDays, avgAttendanceRate, ... }, clients: [...] }` | `{ from, to, branches: [{ branchId, branchName, months: [{ yearMonth, activeClientCount, attendedDays, attendanceRate }] }] }` |

**증상**: StatCard 요약·이용자별 표가 **빈 값** 또는 로드 오류.

**Swagger 우회** — `GET /api/v1/attendance/stats/monthly?branchId=<uuid>&from=2026-06-01&to=2026-06-30`

응답 `branches[0].months`에서 월별 `attendanceRate`·`attendedDays`를 확인하세요. 이용자별 일수는 **별도 집계 API가 없으며** — 현재 백엔드는 **지점·월 단위 집계**만 반환합니다.

> coder 정합: `yearMonth` → `from`/`to` 변환, `branches[].months` → UI summary/clients 매핑, 또는 백엔드에 이용자별 breakdown 추가 (`PLAN_NOTES.md` TWR-Q1).

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

---

## 16. 변경 이력

| 날짜 | 변경 내용 |
|------|----------|
|| 2026-06-06 | **10차** — CHANGELOG V38–V39·라우트 등록 반영, Q106 출석 통계 API 응답 불일치 정정, Q104 정정 |
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
