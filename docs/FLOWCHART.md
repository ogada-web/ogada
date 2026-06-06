# 주간보호센터 웹 시스템 — 화면 흐름도 (FLOWCHART.md)

> **작성**: planner 에이전트
> **최초 작성일**: 2026-06-05
> **상태**: 초안 (Draft) — 사용자 승인 전
> **범위**: MVP v1 (Must) — 7역할 + `client_user`
> **기준 문서**: `REQUIREMENTS.md`(§2-4 역할별 홈, §5 화면 목록), `API_SPEC.md`

> 다이어그램은 Mermaid 문법. GitHub·VS Code 등에서 렌더링됩니다.

---

## 1. 로그인 → 역할별 홈 라우팅 (전체 진입)

REQUIREMENTS §2-4 기준. 로그인 후 JWT의 `role`로 홈 화면을 분기한다.

```mermaid
flowchart TD
  A[/ 로그인 화면/] --> B{인증 성공?}
  B -- 아니오 --> A
  B -- 예 --> C{role 분기}
  C -->|platform_admin| P[/platform 고객사 관리/]
  C -->|hq_admin| H[/dashboard/hq 통합 대시보드/]
  C -->|branch_admin| D[/dashboard 지점 대시보드/]
  C -->|social_worker| D
  C -->|caregiver| D
  C -->|guardian| G[/guardian 보호자 포털/]
  C -->|client_user| G
  C -->|sysadmin| S[/settings 시스템 설정/]
```

> 세션 30분 비활성 시 자동 만료 → 로그인 화면 복귀(§3-1).

---

## 2. 신규 고객 온보딩 (platform_admin) — §1-3

ogada 직원이 새 센터(Tenant)와 첫 `hq_admin`을 만든 뒤, 고객이 운영을 시작하는 전체 흐름.

```mermaid
flowchart TD
  subgraph OGADA[ogada 직원 - platform_admin]
    A1[/platform 진입/] --> A2[고객 등록: 법인명·요금제]
    A2 --> A3[Organization Tenant 생성]
    A3 --> A4[첫 hq_admin 계정 발급]
    A4 --> A5[로그인 정보 고객 전달]
  end
  subgraph CUST[고객 센터]
    B1[hq_admin 로그인] --> B2[지점 Branch 등록]
    B2 --> B3[직원 계정 생성·역할·지점 배정]
    B3 --> B4[전사 설정: allow_client_self_checkin 등]
    B4 --> B5[운영 시작]
  end
  A5 --> B1
```

---

## 3. 다지점 권한·지점 전환 (hq_admin) — §2-3

`hq_admin`은 전 지점 조회·집계가 기본이며, **쓰기**는 지점 선택기로 `active_branch_id`를 정한 경우 해당 지점만.

```mermaid
flowchart TD
  A[/dashboard/hq 통합 대시보드/] --> B{작업 유형}
  B -->|조회·집계| C[전 지점 데이터 열람]
  B -->|등록·수정 쓰기| D[지점 선택기 Branch Switcher]
  D --> E[active_branch_id 설정]
  E --> F[선택 지점 범위 CRUD]
  F --> G{다른 지점 작업?}
  G -- 예 --> D
  G -- 아니오 --> A
```

---

## 4. 이용자 등록 (branch_admin / social_worker) — §3-2

```mermaid
flowchart TD
  A[/clients 이용자 목록/] --> B[신규 등록 클릭]
  B --> C[기본정보 입력: 이름·생년월일·연락처·주소]
  C --> D[장기요양 정보: 등급·인정번호·유효기간]
  D --> E[주민등록번호 입력]
  E --> F{수집·이용 동의 확인}
  F -- 미동의 --> X[저장 불가 안내]
  F -- 동의 --> G[본인부담 구분 copayType 선택]
  G --> H[보호자 연결 1명 이상]
  H --> I{이용자 본인 계정?}
  I -- 필요 --> J[client_user 계정 발급·연결]
  I -- 불필요 --> K[저장]
  J --> K
  K --> L[/clients/:id 상세 - 탭: 기본·건강·출석·청구/]
```

> 주민등록번호는 암호화 저장·마스킹 표시(§3-2-1). 동의 미완료 시 저장 차단.

---

## 5. 출석 — 2경로 (수기 + QR B방식) — §3-3

### 5-1. 수기 체크인/아웃 (직원)

```mermaid
flowchart TD
  A[/attendance 출석 현황/] --> B[/attendance/checkin 수기 처리/]
  B --> C[이용자 목록에서 대상 선택]
  C --> D{도착 / 귀가}
  D -->|도착| E[체크인 - method manual, 시각 자동]
  D -->|귀가| F[체크아웃 + 교통편 기록]
  E --> G[현황 갱신]
  F --> G
  C --> H[결석 처리: 사유 입력]
  H --> G
```

### 5-2. QR 셀프 체크인 (보호자 / 이용자 본인 — B방식)

```mermaid
flowchart TD
  subgraph STAFF[직원 준비]
    S1[/attendance/qr/generate/] --> S2[지점 QR 생성: 입소/귀가·유효시간]
    S2 --> S3[지점 입구에 QR 게시]
  end
  subgraph SCAN[보호자/이용자 스캔]
    U1[지점 QR 스캔] --> U2[guardian/client_user 로그인]
    U2 --> U3{연결 이용자 수}
    U3 -->|1명| U4[자동 선택]
    U3 -->|복수| U5[체크인 대상 선택 UI]
    U4 --> U6[체크인/아웃 전송]
    U5 --> U6
    U6 --> U7{QR 토큰 유효?}
    U7 -- 만료·위조 --> U8[오류 안내]
    U7 -- 유효 --> U9[출석 기록 - method qr_self]
  end
  S3 --> U1
```

> `client_user` 스캔은 Organization `allow_client_self_checkin`이 on일 때만 허용(§3-3).

---

## 6. 건강 기록 입력 (caregiver 이상) — §3-4

```mermaid
flowchart TD
  A[/clients/:id 또는 /health/] --> B{기록 유형}
  B -->|일일 건강| C[혈압·체온·혈당·SpO2 입력]
  B -->|투약| D[약품·용량·시간·투약자]
  B -->|낙상·사고| E[이벤트 기록]
  B -->|특이사항| F[메모]
  C --> G[저장 → 이력·그래프 반영]
  D --> G
  E --> H{이상 징후?}
  E --> G
  H -- 예 --> I[대시보드 건강 이상 알림 등록]
```

---

## 7. 청구·정산 (hq_admin / branch_admin) — §3-9

수가표·본인부담 비율표를 선행 설정한 뒤 월별 청구서를 생성한다.

```mermaid
flowchart TD
  subgraph SETUP[사전 설정 - hq_admin]
    P1[/billing/fee-schedules 수가표/] --> P2[연도·등급별 1일 수가 등록]
    P3[/billing/copay-rates 본인부담 비율/] --> P4[구분별 비율 확인·수정]
  end
  subgraph RUN[월별 청구]
    R1[/billing 청구 화면/] --> R2[지점·대상월 선택 → 생성]
    R2 --> R3[자동 계산: 등급수가 × 출석일수]
    R3 --> R4[이용자별 본인부담금·공단부담 산출]
    R4 --> R5[청구서·명세서 목록]
    R5 --> R6{상태}
    R6 -->|작성중| R7[검토·수정]
    R6 -->|확정| R8[명세서 PDF 출력]
    R6 -->|수납완료| R9[수납 기록]
    R5 --> R10[공단 청구내역상세 엑셀 import]
  end
  P2 --> R2
  P4 --> R4
```

> 공단 포털 직접 전송·보호자 발송·CMS 결제는 MVP 제외(후속).

---

## 8. 대시보드 — §3-11

```mermaid
flowchart TD
  subgraph BR[지점 대시보드 - branch scope]
    D1[오늘 출석 현황 요약]
    D2[이용자 통계: 입소/퇴소/이용]
    D3[건강 이상 알림 목록]
    D4[월별 출석률 차트]
  end
  subgraph HQ[통합 대시보드 - hq scope]
    E1[전 지점 출석 한눈에 - 카드/표]
    E2[지점별 이용자수·출석률 비교]
    E3[전 지점 건강 이상 통합 목록 - 지점명 표시]
    E4[지점·기간 필터]
    E4 --> E5{특정 지점 상세}
    E5 -->|쓰기 필요| F[지점 선택기 → active_branch_id]
  end
```

---

## 9. 보호자 포털 (guardian / client_user) — §3-7 일부 (MVP는 열람+QR)

```mermaid
flowchart TD
  A[/guardian 보호자 포털/] --> B[연결 이용자 일일 기록 열람]
  B --> C{출석·건강·식사 기록}
  A --> D[/guardian/checkin QR 체크인/]
  D --> E[5-2 QR 셀프 흐름]
```

> MVP 보호자 포털은 **기록 열람 + QR 체크인** 중심. 알림(알림톡/SMS)은 v1 이후(§3-7).

---

## 10. 화면 ↔ 역할 ↔ API 매핑 요약

| 화면 | 주 역할 | 주요 API(§API_SPEC) |
|------|---------|----------------------|
| `/` 로그인 | 전체 | `POST /auth/login` |
| `/platform` | platform_admin | `/platform/organizations*` |
| `/dashboard/hq` | hq_admin | `/dashboard/hq*`, `/auth/active-branch` |
| `/dashboard` | branch_admin·social_worker·caregiver | `/dashboard/branch` |
| `/clients*` | branch_admin·social_worker | `/clients*` |
| `/attendance*` | caregiver 이상 | `/attendance*`, `/branches/{id}/qr` |
| `/guardian*` | guardian·client_user | `/attendance/qr/scan`, `/guardian/checkin-targets` |
| `/health*` | caregiver 이상 | `/clients/{id}/health*` |
| `/billing*` | hq_admin·branch_admin | `/billing/*` |
| `/settings` | sysadmin | `/settings/*` |

---

*이 문서는 planner 에이전트가 관리합니다. 흐름 변경 시 `REQUIREMENTS.md`·`API_SPEC.md`와 동기화하세요.*
