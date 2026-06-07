<!-- doc:owner=UXD doc:audience=PLN,COD,TSR updated=2026-06-07T00:16:00+09:00 -->
# ogada 디자인 시스템 (product/DESIGN_SYSTEM.md)

> **작성**: ux_designer 에이전트 (`UXD`)
> **최초 작성일**: 2026-06-06
> **최종 갱신**: 2026-06-07 (14차 — **`BATCH_STATUS` 공유 상수 승격**(NHISImportPage 로컬 정의 → Badge 모듈), **`FeeRateHistoryPanel`** 신설(US-G00a 수가 이력·연도별 그룹), **Recharts 차트 색상 토큰**(토큰·chartColors.js·다크 팔레트), **`ds-progress-steps`·`ds-fee-history`·`ds-fee-table-cell`** CSS, §2-3 BATCH_STATUS 도메인 매핑 추가, UXD-1·UXD-4 해소)
> **이전 갱신**: 2026-06-06 (13차 — **전사 설정 토글** 누락 보강: WAI-ARIA `switch` 패턴 `Switch` 컴포넌트 신설(`role="switch"`·`aria-checked`·키보드·44px·켜짐/꺼짐 텍스트 병행), `SettingsPage` `allow_client_self_checkin`(REQUIREMENTS §3-3·FLOWCHART §2) 정적 안내 → 실 토글 컨트롤로 교체, `forced-colors` 식별성)
> **이전 갱신**: 2026-06-06 (12차 — **로그인 진입 화면** 스타일 정비(미정의 `.ds-label` 해소·`.ds-login`), **Modal 포커스 트랩**(WAI-ARIA dialog), **고대비/강제 색상 모드**(`forced-colors`·`prefers-contrast`, WCAG 1.4.11) 지원)
> **이전 갱신**: 2026-06-06 (11차 — **다크 모드** 토큰·`ThemeToggle` 추가: agents.yaml design_principles 「다크모드 지원(운영자 야간 근무)」 구현, §2-4 다크 대비표·§10 해소)
> **이전 갱신**: 2026-06-06 (10차 — US-D01/FLOWCHART §4 이용자 본인(client_user) 계정 발급 필드, CopayTypeSelect 실적용, 대비비 실측 현행화)
> **상태**: 초안 (Draft)
> **대상**: planner(PLN) 검토 · coder(COD) 구현 · tester(TSR) 검증
> **근거 문서**: `docs/planning/REQUIREMENTS.md`(§4 비기능 — 접근성 WCAG 2.1 AA, 반응형), `docs/planning/USER_STORIES.md`, `docs/planning/FLOWCHART.md`

---

## 0. 산출물 위치 [UXD]

| 구분 | 경로 | 설명 |
|------|------|------|
| 디자인 토큰 | `src/frontend/src/styles/tokens.css` | 색상·타이포·간격·radius·shadow·터치 타깃 CSS 변수 (단일 진실 원천) |
| 컴포넌트 스타일 | `src/frontend/src/styles/components.css` | `.ds-*` 클래스 (BEM-lite), 토큰만 참조 |
| UI 컴포넌트 | `src/frontend/src/components/ui/` | React(JSX) 컴포넌트 + barrel `index.js` |
| 전역 베이스 | `src/frontend/src/styles.css` | body·링크·로그인 레이아웃 (토큰 기반) |
| 테마 유틸 | `src/frontend/src/theme.js` | 라이트/다크 결정·적용·저장 (`<html data-theme>`, 11차) |
| 페이지 스켈레톤 | `src/frontend/src/pages/` | 화면 구조 + 컴포넌트 조합 예시 (API 연동은 coder 담당) |

> **브랜치**: `src/frontend` submodule의 `develop`.
> **스택 메모**: 현재 `src/frontend`는 **JSX(JavaScript)** 로 구현. TS 전환 시 아래 §7 props 표를 인터페이스로 그대로 옮길 수 있다.

---

## 1. 디자인 원칙 [UXD]

1. **접근성 우선** — WCAG 2.1 AA. 모든 인터랙티브 요소는 키보드로 동작하고 포커스가 보인다.
2. **색상만으로 의미 전달 금지** — 상태(청구/매칭/출석)는 항상 **텍스트 라벨 + 색상**을 함께 제공.
3. **모바일 친화** — 터치 타깃 최소 44×44px, 입력 글자 16px(iOS 자동 줌 방지), 360px 폭 지원.
4. **토큰 단일 원천** — 컴포넌트는 raw hex 금지, 시맨틱 토큰(`--color-*` 등)만 사용.
5. **현장 사용자 배려** — 파일럿은 센터장·요양보호사. 큰 글자·명확한 라벨·낮은 인지 부하.

---

## 2. 색상 토큰 [UXD]

### 2-1. 시맨틱 토큰 (컴포넌트에서 사용)

| 토큰 | 값(primitive) | 용도 |
|------|--------------|------|
| `--color-bg` | gray-100 | 페이지 배경 |
| `--color-surface` | white | 카드·패널 표면 |
| `--color-surface-muted` | gray-50 | 표 헤더·비활성 입력 |
| `--color-text` | gray-900 | 기본 본문 |
| `--color-text-secondary` | gray-600 | 보조 텍스트 (on white 7.46:1) |
| `--color-text-muted` | gray-500 | 플레이스홀더 (on white 4.76:1) |
| `--color-primary` | blue-600 | 기본 액션 (on white 5.17:1) |
| `--color-primary-hover` | blue-700 | hover |
| `--color-focus-ring` | blue-600 | 키보드 포커스 링 |
| `--color-success` / `-text` | green-600 / 700 | 수납완료·일치 |
| `--color-warning` / `-text` | amber-600 / 700 | 차이(DISCREPANCY) |
| `--color-danger` / `-text` | red-600 / 700 | 미매칭·삭제·오류 |
| `--color-border-strong` | gray-400 | 입력 테두리 |

### 2-2. 대비비(WCAG AA) 확인

> **10차 실측 (2026-06-06)**: 아래 값은 `tokens.css`의 실제 hex로 재계산한 값이다(이전 표는 토큰을 darken 하기 전 보수적 추정치였음). 모든 시맨틱 조합이 AA(본문 4.5:1)를 충족하며, 실측값은 기존 표기보다 높다.

| 조합 (실제 토큰 hex) | 대비비(실측) | 기준 | 결과 |
|------|--------|------|------|
| text(gray-900 #0f172a) / white | ~17:1 | 4.5:1 | ✅ |
| text-secondary(gray-600 #475569) / white | 7.58:1 | 4.5:1 | ✅ |
| text-muted(gray-500 #64748b) / white | 4.76:1 | 4.5:1 | ✅ |
| on-primary(white) / primary(blue-600 #1d4ed8) | 6.70:1 | 4.5:1 | ✅ |
| primary-hover(blue-700 #1e40af) / white | 8.72:1 | 4.5:1 | ✅ |
| success(green-600 #15803d) / white | 5.02:1 | 4.5:1 | ✅ |
| warning(amber-600 #b45309) / white | 5.02:1 | 4.5:1 | ✅ |
| danger(red-600 #dc2626) / white | 4.83:1 | 4.5:1 | ✅ |
| info(info-600 #0e7490) / white | 5.36:1 | 4.5:1 | ✅ |
| success-text(green-700) / success-soft(green-50) (badge) | 6.77:1 | 4.5:1 | ✅ |
| warning-text(amber-700) / warning-soft(amber-50) (badge) | 6.84:1 | 4.5:1 | ✅ |
| danger-text(red-700) / danger-soft(red-50) (badge) | 5.91:1 | 4.5:1 | ✅ |
| neutral-text(gray-700) / neutral-soft(gray-100) (badge) | 9.45:1 | 4.5:1 | ✅ |

> 본문 텍스트(<18.66px)는 4.5:1, 큰 텍스트·UI 컴포넌트 경계는 3:1 기준. Badge 소프트 배경 위 `*-text` 토큰은 진한 색으로 대비 확보. 솔리드 뱃지(white on success/warning/danger-600)도 5.0:1 이상.

### 2-3. 상태 색상 매핑 (도메인)

| 도메인 | 코드 | tone | 라벨 |
|--------|------|------|------|
| 청구 상태 (US-G07) | `DRAFT` | neutral | 작성중 |
| | `CONFIRMED` | info | 확정 |
| | `PAID` | success | 수납완료 |
| NHIS 매칭 (US-G06) | `MATCHED` | success | 일치 |
| | `DISCREPANCY` | warning | 차이 |
| | `UNMATCHED` | danger | 미매칭 |
| 출석 상태 | `CHECKED_IN` | success | 입소 |
| | `CHECKED_OUT` | neutral | 귀가 |
| | `ABSENT` | warning | 결석 |
| Tenant 상태 | `active` | success | 활성 |
| | `inactive` | neutral | 비활성 |
| NHIS 배치 (US-G04) | `PENDING` | neutral | 대기 |
| | `PROCESSING` | info | 처리중 |
| | `COMPLETED` | success | 완료 |
| | `FAILED` | danger | 실패 |

> 매핑 객체는 `components/ui/Badge.jsx`의 `BILLING_STATUS`·`MATCH_STATUS`·`ATTENDANCE_STATUS`·`BRANCH_STATUS`·`BATCH_STATUS`로 코드화 → `<StatusBadge status map>` 사용. `BATCH_STATUS`는 14차에 NHISImportPage 로컬 정의 → Badge 모듈로 승격.

### 2-4. 다크 모드 토큰 (11차, 운영자 야간 근무) [UXD]

> agents.yaml `design_principles` 「다크모드 지원(운영자 야간 근무 고려)」 구현. 컴포넌트는 시맨틱 토큰만 참조하므로 **토큰 재정의만으로** 전 화면이 전환된다(컴포넌트 코드 변경 0). 활성화는 `<html data-theme="dark">` — `src/theme.js`/`ThemeToggle`가 설정.

**설계 원칙**: 다크에서는 `primary`/`danger`를 **더 밝은 색**으로 올리고 라벨 텍스트(`--color-on-primary`/`--color-on-danger`)를 **진한 남색(#0f172a)**으로 두어 버튼 대비를 확보한다. 상태 뱃지·알림은 반투명 틴트(`*-soft`) 위 **밝은 `*-text`** 조합.

| 다크 조합 | 대비비(계산) | 기준 | 결과 |
|------|--------|------|------|
| text(#f1f5f9) / surface(#1e293b) | ~12.8:1 | 4.5:1 | ✅ |
| text-secondary(#cbd5e1) / surface | ~9.6:1 | 4.5:1 | ✅ |
| text-muted(#94a3b8) / surface | ~5.1:1 | 4.5:1 | ✅ |
| text-link(#93c5fd) / surface | ~8.1:1 | 4.5:1 | ✅ |
| on-primary(#0f172a) / primary(#60a5fa) | ~6.7:1 | 4.5:1 | ✅ |
| on-danger(#0f172a) / danger(#f87171) | ~6.0:1 | 4.5:1 | ✅ |
| primary(#60a5fa) / primary-soft(다크 위) (nav active) | ~4.8:1 | 4.5:1 | ✅ |
| success-text(#86efac) / success-soft(badge) | ≥7:1 | 4.5:1 | ✅ |
| warning-text(#fcd34d) / warning-soft(badge) | ≥7:1 | 4.5:1 | ✅ |
| danger-text(#fca5a5) / danger-soft(badge) | ~5.7:1 | 4.5:1 | ✅ |

> 값은 `tokens.css` `[data-theme="dark"]` 실제 hex로 계산한 추정치. `color-scheme: dark`를 함께 설정해 스크롤바·네이티브 날짜선택기 등도 다크로 렌더한다. **tester 검증 권장**: 대시보드·청구 표·모달·뱃지를 다크에서 캡처해 대비 확인(자동 흐름 §6).

---

## 3. 타이포그래피 [UXD]

| 토큰 | 크기 | 용도 |
|------|------|------|
| `--font-size-xs` | 12px | 캡션·뱃지·도움말 |
| `--font-size-sm` | 14px | 보조 본문·표 |
| `--font-size-md` | 16px | **기본 본문·입력(모바일 최소)** |
| `--font-size-lg` | 18px | 카드 부제 |
| `--font-size-xl` | 20px | 섹션/카드 제목 |
| `--font-size-2xl` | 24px | 페이지 제목 `h1` |
| `--font-size-3xl` | 30px | 대시보드 지표 숫자 |

- Weight: `regular 400 / medium 500 / semibold 600 / bold 700`
- Line-height: `tight 1.25 / normal 1.5 / relaxed 1.7`
- Font: `Noto Sans KR` 우선(한국어), `Pretendard` 폴백 — 본문 16px 이상 권장.

---

## 4. 간격·radius·shadow·z-index [UXD]

- **Spacing**: 4px 베이스. `--space-1`(4) ~ `--space-16`(64). 컴포넌트 패딩·간격은 토큰만 사용.
- **Radius**: `sm 4 / md 8 / lg 12 / xl 16 / full`. 버튼·입력 `md`, 카드 `lg`, 뱃지 `full`.
- **Shadow**: `sm`(카드 기본) / `md`(드롭다운·토스트) / `lg`(모달).
- **z-index**: sticky 100 / overlay 1000 / modal 1100 / toast 1200.

---

## 5. 반응형 & 터치 [UXD]

| 브레이크포인트 | 폭 | 기준 |
|---------------|-----|------|
| 모바일 | 360px~ | 단일 컬럼, 카드 패딩 축소, 사이드바 → 수평 스크롤 탭 |
| 태블릿 | 768px~ | 2컬럼 그리드 |
| 데스크톱 | 1200px | 컨테이너 최대폭 + 240px 사이드바 |

- 터치 타깃: `--touch-target-min: 44px`. 버튼·탭·체크박스 래퍼·입력 모두 최소 44px 높이.
- 컨트롤 높이: `sm 36 / md 44(기본) / lg 52(모바일 주요 액션)`.
- `@media (prefers-reduced-motion: reduce)` → 트랜지션 0ms.
- 사이드바: 데스크톱 240px 고정. 모바일에서 수평 스크롤 탭으로 전환.

---

## 6. 접근성 체크리스트 (tester 검증 기준) [UXD]

> **5차 현행화 (2026-06-06)**: 구현 완료 항목을 `[x]`로 갱신.
> **6차 (2026-06-06)**: v1.2 P0 화면·컴포넌트 추가 — SideNav 2단 그룹, 등급 타임라인, 대시보드 위젯, 연락처 마스킹.
> **7차 (2026-06-06)**: USER_STORIES·FLOWCHART 대비 누락 보강 — `/billing/:id` 상세, 결석 사유 모달(US-E01), 이용자 사진+alt(US-D01), 보호자 초대 모달(US-J01), 청구 상태 이력 타임라인(US-G07), SideNav NHIS import, ClientPicker 키보드 탐색.
> **8차 (2026-06-06)**: FLOWCHART §5·§7·§9 갭 — `CheckoutModal`(US-E01 교통편), `DiscrepancyComparePanel`(US-G06), `GuardianBillingDetailModal`(US-J02), `ClientSelector`(복수 이용자 radiogroup), `CopayTypeSelect`(US-D01), `QrScanPanel`(US-E04), `branch_admin` SideNav 수기 체크인.
> **9차 (2026-06-06)**: USER_STORIES 잔여 갭 — `MedicationDuplicateAlert`(US-F02), `HealthAbnormalBanner`(US-F01), `SessionTimeoutProvider`(US-B03), 페이지 통합(GuardianPage·GuardianCheckinPage·AttendancePage·ReconciliationPage·HealthPage), `ToastProvider`/`SessionTimeoutProvider` 앱 루트 배선.
> **11차 (2026-06-06)**: **다크 모드** — `tokens.css` `[data-theme="dark"]` 토큰, `ThemeToggle`(AppShell topbar), `theme.js`. 다크 대비 AA 검증(§2-4).
> **12차 (2026-06-06)**: **로그인 진입 화면**(US-B01) 스타일 정비 — `LoginPage`가 참조하던 미정의 `.ds-label`로 라벨이 무스타일이던 문제를 `Field`/`TextInput`/`Button`(block·lg) 전환으로 해소, `.ds-login` 카드 레이아웃·브랜드 모노그램. **Modal 포커스 트랩**(Tab/Shift+Tab 순환). **고대비/강제 색상 모드**(`forced-colors`·`prefers-contrast: more`) — 배경 틴트 제거 시 경계선·시스템 강조색으로 식별성 보장.
> **13차 (2026-06-06)**: **전사 설정 토글 누락 보강**(US-I03·REQUIREMENTS §3-3·FLOWCHART §2) — `SettingsPage` 「조직 설정」의 `allow_client_self_checkin`이 정적 `<dl>` 설명 + `TODO`뿐이어서 조작 컨트롤이 없던 갭을 WAI-ARIA `switch` 패턴 `Switch` 컴포넌트로 해소. 켜짐/꺼짐 **텍스트 라벨 병행**(색·노브 위치만 의존 금지), 네이티브 `<button>` Enter/Space 토글, 44px 트랙, `forced-colors`에서 경계선+`Highlight` 채움으로 식별성.

- [x] 모든 폼 컨트롤에 `<label htmlFor>` 연결 — `Field` render-prop 패턴이 강제 (`htmlFor` ↔ `id` 자동 연결).
- [x] 오류는 색상 + 텍스트(`role="alert"`) + `aria-invalid`로 표기 — `Field error` prop 사용 시 자동 적용.
- [ ] 키보드만으로 로그인→대시보드→이용자 등록 핵심 흐름 완주 가능 — **tester E2E 검증 필요**.
- [x] `:focus-visible` 포커스 링이 모든 인터랙티브 요소에 보임 — `components.css §0` 전역 `:focus-visible` 규칙.
- [x] 탭(Tabs)은 WAI-ARIA 패턴(좌우/Home/End 키 이동, `aria-selected`, TabPanel `aria-labelledby` Context 연결).
- [x] 의미 있는 이미지에 `alt`, 장식 이미지에 `alt=""` — `ClientPhotoField`가 미리보기 `alt` 입력·플레이스홀더 `role="img"` 제공 (`ClientFormPage`).
- [x] 상태 뱃지는 색상만으로 의미를 전달하지 않음 — `StatusBadge`가 텍스트 라벨 + 색상을 항상 함께 출력.
- [x] 본문 바로가기(skip link) 제공 — `AppShell`의 `<a class="ds-skip-link" href="#main-content">`.
- [x] 색 대비 AA 충족 — §2-2 표 참조 (모든 시맨틱 조합 4.5:1 이상).
- [x] DISCREPANCY/UNMATCHED 표 행: 배경 + **좌측 4px 보더** (색상만 의존 금지).
- [x] Modal: `role="dialog"`, `aria-modal="true"`, `aria-labelledby` 연결 (인스턴스별 고유 ID — `useId()` 사용), ESC 닫기, 열림/닫힘 포커스 복원.
- [x] FileUpload: 숨겨진 input에 라벨·`aria-describedby` 연결. 드롭존 `role="button"` + Enter/Space 키.
- [x] Pagination: `<nav>`, 현재 페이지 `aria-current="page"`, 이전/다음 `aria-label`.
- [x] SideNav: `<nav aria-label="주 메뉴">`, 활성 링크 `.ds-nav-item--active`.
- [x] 주민번호 열람: `aria-label="주민번호 열람 (audit 기록됨)"` + 마스킹 표시(US-D04).
- [x] FilterChips: `role="radiogroup"` + `role="radio"` + `aria-checked` (US-G07).
- [x] 건강 수치 비정상 시 `aria-invalid="true"` + `role="alert"` 오류 메시지 — `HealthPage` `Field error` + `Alert` (US-F01).
- [x] 수동 매칭 모달(US-G06): 지점·Tenant 제약 안내 `Alert tone="warning"` 포함 — `ReconciliationPage`.
- [x] 지점 관리(US-C01): 등록/수정 `Modal`(role=dialog)·`Field` 라벨 연결, 지점명 빈 값 시 `Field error`(role="alert"·`aria-invalid`), 상태 `BRANCH_STATUS` 텍스트+색.
- [x] 월별 출석 통계(US-E05): `<input type="month">` `Field` 라벨 연결, 표 `caption`, 차트 `role="img"`+`aria-label`, 조회 오류 `role="alert"`.
- [x] 보호자 목록(US-D01·US-J01): `GuardianListCard` — `aria-labelledby` 섹션 제목, 전화번호 `<a href="tel:">` + `aria-label`, 초대 스텁 `aria-disabled="true"` + `title` 설명.
- [x] 2단 SideNav(US-UX-02): 그룹 토글 `aria-expanded`/`aria-controls`, 하위 항목 `.ds-nav-item--nested`, 데스크톱 항상 펼침·모바일 접힘/펼침.
- [x] 등급 이력(US-M01): `GradeHistoryTimeline` — `<ol aria-label="등급 변동 이력">`, 등급 변경 `sr-only` 텍스트, 화살표는 `aria-hidden`.
- [x] 연락처 마스킹(US-K01·L02): `MaskedPhone` — 부분 마스킹 + `tel:` 링크 + `aria-label`.
- [x] 보호자 연결(US-K02): `LinkedClientsCard` — 대표 보호자 `Checkbox` 라벨 연결, `aria-labelledby` 섹션 제목.
- [x] 입금 처리(US-L01): `PaymentPage` — `Field` 라벨·`type="date"`/`inputMode="numeric"`, Modal `useId()` 패턴 재사용.
- [x] 미납 목록(US-L02): `OverduePage` — `.ds-row--warning` 행 강조 + 「미납」텍스트 Badge(색상만 의존 금지).
- [x] 대시보드 위젯(US-M02): `DashboardWidgetGrid` — 위젯 링크 `sr-only` 보조 텍스트, 로딩 `role="status"`.
- [x] 청구 상세(US-G02): `BillingDetailPage` — 상태 이력 `ClaimStatusTimeline`, 확정 후 불변 `Alert`, 인쇄 `@media print` 사이드바 숨김.
- [x] 결석 처리(US-E01): `AttendanceAbsentModal` — 사유 `Field`+`role="alert"`, 미처리 행 「결석」버튼 `aria-label`.
- [x] 보호자 초대(US-J01): `GuardianInviteModal` — `Modal`+`Field` 라벨 연결, `ClientDetailPage`에서 재사용.
- [x] ClientPicker(US-G06): combobox `aria-activedescendant` + Arrow/Enter/Escape 키 탐색.
- [x] SideNav 그룹 토글: `aria-label="{그룹} 메뉴 그룹"` (모바일 접힘/펼침).
- [x] GuardianListCard·GuardianPage: 연락처 `MaskedPhone`, 청구 상태 `StatusBadge`+`BILLING_STATUS` (색상만 의존 금지).
- [x] CheckoutModal(US-E01): 귀가 교통편 `Field`+`Select` 라벨, 미선택 시 확인 버튼 `disabled`, 오류 `role="alert"`.
- [x] ClientSelector(US-E04·J02): `role="radiogroup"` + `role="radio"` + `aria-checked`, 1명일 때 `hideWhenSingle` 숨김.
- [x] DiscrepancyComparePanel(US-G06): 차이 컬럼 `Badge` 텍스트 라벨 + 좌측 4px `--color-compare-highlight` 보더.
- [x] GuardianBillingDetailModal(US-J02): `<table>` `caption`·`scope`, 본인부담금 행 강조, 인쇄 `@media print`.
- [x] QrScanPanel(US-E04): 카메라 `aria-busy`, 수동 입력 `Field` 라벨, 카메라 불가 `Alert` 안내.
- [x] CopayTypeSelect(US-D01): 구분별 비율 help 텍스트, `aria-invalid` 오류 연동.
- [x] MedicationDuplicateAlert(US-F02): 동일 시각 투약 `role="alert"` 경고 + 「확인 후 계속」 링크 버튼 — `HealthPage`.
- [x] HealthAbnormalBanner(US-F01): 비정상 수치 항목별 `Badge` 텍스트 라벨 + 값 목록.
- [x] SessionTimeoutProvider(US-B03): 30분 비활성 → 60초 전 `SessionTimeoutModal`, `App`+`AuthProvider` 하위 배치.
- [x] ClientUserAccountField(US-D01): 발급 토글 `Checkbox`(라벨 44px), 체크 시에만 로그인 이메일 `Field`(`type="email"`·`aria-invalid`) 노출, `allow_client_self_checkin` off면 `Alert tone="info"` 안내 — `ClientFormPage`.
- [x] 다크 모드(11차): `ThemeToggle` `aria-pressed`+아이콘(`aria-hidden`)+텍스트 라벨 병행, 44px. `[data-theme="dark"]` 토큰 전 조합 AA(§2-4). `color-scheme: dark`로 네이티브 위젯도 다크.
- [x] 로그인 화면(12차, US-B01): `LoginPage` → `Field`(label↔id 연결)·`TextInput`(`autoComplete` 보존)·`Button block size=lg`(44px↑)·오류 `Alert tone="danger"`(role=alert). 미정의 `.ds-label` 무스타일 라벨 제거.
- [x] Modal 포커스 트랩(12차): 열린 다이얼로그에서 Tab/Shift+Tab이 내부 포커스 가능 요소만 순환(`aria-modal` 보강). ESC 닫기·포커스 복원 유지.
- [x] 고대비/강제 색상(12차, WCAG 1.4.11): `forced-colors: active` 시 버튼·뱃지·카드·모달·표 주의행에 경계선 강제 + 포커스/활성 내비 `Highlight`. `prefers-contrast: more` 시 보조 텍스트 대비 상향·포커스 링 3px.
- [x] Switch(13차, US-I03·§3-3): `role="switch"` + `aria-checked`, 라벨 `aria-labelledby`·설명 `aria-describedby` 연결, 켜짐/꺼짐 텍스트 병행(색만 의존 금지), 네이티브 `<button>` 키보드 토글, 44px 트랙, `forced-colors`에서 트랙 경계선+`Highlight` 채움. `SettingsPage` `allow_client_self_checkin` 적용.
- [x] CopayTypeSelect 실적용(US-D01): `ClientFormPage` 본인부담 구분 raw `<Select>` → `CopayTypeSelect`(비율 help·`aria-invalid`).
- [x] GuardianPage(US-J02): `ClientSelector` radiogroup + 명세 행 「상세」→ `GuardianBillingDetailModal`.
- [x] GuardianCheckinPage(US-E04): `QrScanPanel`+`ClientSelector` 통합, 피드백 `.ds-feedback--success/danger`.
- [x] AttendancePage(US-E01): 「귀가」→ `CheckoutModal` (표 인라인 select 제거, 모바일 터치 우선).
- [x] ReconciliationPage(US-G06): DISCREPANCY 「비교」→ `DiscrepancyComparePanel` 모달, 수동 매칭 `ClientPicker`.
- [x] ToastProvider: `main.jsx` 루트 — API 피드백 전역 준비.
- [ ] 키보드만으로 로그인→대시보드→이용자 등록 핵심 흐름 완주 가능 — **tester E2E 검증 필요**.
- [x] NHIS 배치 상태(US-G04): `BATCH_STATUS` Badge 모듈로 승격(14차) — NHISImportPage 로컬 중복 제거, 색상+텍스트 라벨 일관성.
- [x] 수가 이력(US-G00a): `FeeRateHistoryPanel` — 표 `caption` 스크린리더 행 설명, 수가 숫자 `aria-label` 포함.
- [x] NHIS 배치 진행(US-G04): `.ds-progress-steps` — 단계별 텍스트 라벨(`ds-progress-steps__label`) 병행(색만 의존 금지), `ds-sr-only` 단계 설명 포함.

---

## 7. UI 컴포넌트 가이드 (coder 구현 메모) [UXD]

import: `import { Button, Card, Field, Modal, Pagination } from "../components/ui";`

### 7-1. 기존 컴포넌트

| 컴포넌트 | 주요 props | 용도 / 화면 |
|----------|-----------|------------|
| `Button` | `variant(primary/secondary/danger/ghost)`, `size(sm/md/lg)`, `block` | 전 화면 액션 |
| `Field` | `label`, `required`, `help`, `error`, `children(render prop)` | 폼 라벨·오류 접근성 래퍼 (이용자 등록 §US-D01) |
| `TextInput`/`Textarea`/`Select` | 네이티브 props 패스스루 | Field 안에서 사용 |
| `Checkbox` | `label`, `checked`, `onChange` | **주민번호 수집 동의**(US-D04) 등 |
| `Card` / `StatCard` | `title`,`actions` / `label`,`value`,`unit` | 카드 · 대시보드 지표(US-H01) |
| `Badge` / `StatusBadge` | `tone` / `status`,`map` | 청구·매칭·출석 상태 (`BILLING_STATUS`·`MATCH_STATUS`·`ATTENDANCE_STATUS`) |
| `Alert` | `tone`, `title` | 안내·경고(예: 롱텀 Chrome/Edge 안내 US-G04) |
| `Tabs` / `TabPanel` | `tabs`,`activeId`,`onChange` | 이용자 상세 탭(기본/건강/출석/청구 US-D03) |
| `Table` | `columns`, `caption` + 행 강조 `ds-row--warning/danger` | 청구 목록·NHIS reconciliation 행(US-G06) |
| `BranchSwitcher` | `branches`,`value`,`onChange` | 지점 전환(US-B02, `active_branch_id`) |
| `AppShell` | `brand`,`topbarRight`,`title`,`nav` | 로그인 이후 공통 레이아웃 + skip link + 사이드바 |

### 7-2. 신규·보강 컴포넌트 (2026-06-06)

| 컴포넌트 | 주요 props | 용도 / 화면 |
|----------|-----------|------------|
| `Modal` | `isOpen`,`onClose`,`title`,`size(sm/md/lg)`,`footer` | 확인 다이얼로그, NHIS 수동 매칭(US-G06), 고객사 등록(US-A01). **`useId()`로 인스턴스별 고유 `aria-labelledby` ID 생성** |
| `Pagination` | `page`,`totalPages`,`onChange` | 이용자·청구서 목록 페이지 이동(US-D02, US-G07) |
| `FileUpload` | `accept`,`label`,`help`,`onChange`,`error` | NHIS 엑셀 업로드(US-G04) |
| `EmptyState` | `title`,`description`,`action` | 빈 목록 안내 (모든 목록 화면) |
| `Spinner` / `LoadingOverlay` | `size(sm/md/lg)`,`label` | API 대기 상태 |
| `SideNav` | `role` | 역할별 사이드 네비게이션 자동 생성 |
| `FilterChips` | `options`,`value`,`onChange`,`label` | 청구 상태 필터 radiogroup (US-G07) |
| `SearchInput` | `value`,`onChange`,`label`,`placeholder` | 이용자 목록 검색 (US-D02) |
| `MaskedRevealField` | `maskedValue`,`revealed`,`onReveal`,`canReveal` | 주민번호 마스킹·열람 (US-D04) |
| `ClientPicker` | `candidates`,`value`,`onChange`,`onSearch` | NHIS 수동 매칭 이용자 선택 (US-G06) |
| `QrCodePanel` | `title`,`qrDataUrl`,`validUntil`,`onPrint` | 지점 QR 표시·인쇄 (US-E03) |
| `ToastProvider` / `useToast` | `success/warning/danger/info` | 저장·오류 피드백 (App 루트 감싸기) |
| `SessionTimeoutModal` | `isOpen`,`secondsLeft`,`onExtend`,`onLogout` | 30분 비활성 경고 (US-B03) |

### 7-3. 5차 보강 컴포넌트 (2026-06-06)

| 컴포넌트 | 주요 props | 용도 / 화면 |
|----------|-----------|------------|
| `GuardianListCard` | `guardians[]`,`canInvite` | 이용자 상세 기본정보 탭 — 연결 보호자 목록 표시(US-D01) + 초대 발송 스텁(US-J01, v1.1 disabled). `aria-labelledby` 섹션 제목, 전화번호 `tel:` 링크 |

### 7-4. 6차 보강 컴포넌트 (2026-06-06, v1.2 P0)

| 컴포넌트 | 주요 props | 용도 / 화면 |
|----------|-----------|------------|
| `GradeHistoryTimeline` | `entries[]`,`emptyMessage` | 이용자 상세 **등급 이력** 탭 (US-M01). `{ changedAt, previousGrade, newGrade, reason? }` |
| `DashboardWidgetGrid` | `widgets[]`,`ariaLabel` | 대시보드 실데이터 위젯 3블록+ (US-M02). `href`·`loading`·`badge` 지원 |
| `MaskedPhone` | `phone`,`masked` | 보호자·미납 목록 연락처 부분 마스킹 + `tel:` (US-K01, US-L02) |
| `LinkedClientsCard` | `clients[]`,`canEdit`,`onPrimaryChange`,`onAddLink` | 보호자 상세 연결 이용자·대표 지정 (US-K02) |
| `SideNav` (2단) | `role` | **US-UX-02** — 운영·출석·기록·청구 그룹, `NAV_CONFIG` 그룹 구조 |

### 7-5. 7차 보강 컴포넌트 (2026-06-06, 누락·접근성)

| 컴포넌트 | 주요 props | 용도 / 화면 |
|----------|-----------|------------|
| `ClaimStatusTimeline` | `entries[]` | 청구서 상세 상태 전이 이력 (US-G07). `{ fromStatus?, toStatus, changedAt, changedBy? }` |
| `GuardianInviteModal` | `isOpen`,`form`,`onChange`,`onSubmit` | 보호자 초대 발송 폼 (US-J01). `ClientDetailPage`에서 사용 |
| `ClientPhotoField` | `photoUrl`,`altText`,`onPhotoChange`,`onAltChange` | 이용자 등록 사진+alt (US-D01). `ClientFormPage` |
| `AttendanceAbsentModal` | `client`,`reason`,`onConfirm` | 수기 출석 결석 사유 입력 (US-E01). `AttendancePage` |

### 7-6. 8차 보강 컴포넌트 (2026-06-06, FLOWCHART·USER_STORIES 갭)

| 컴포넌트 | 주요 props | 용도 / 화면 |
|----------|-----------|------------|
| `CheckoutModal` | `client`,`transport`,`onConfirm` | 귀가 교통편 선택 (US-E01). `AttendancePage` — 표 인라인 select 대체·모바일 권장 |
| `ClientSelector` | `clients[]`,`value`,`onChange`,`hideWhenSingle` | 복수 이용자 radiogroup (US-E04, US-J02). `GuardianPage`·`GuardianCheckinPage` |
| `CopayTypeSelect` | `value`,`onChange`,`error` | 본인부담 구분 4종+비율 help (US-D01). `ClientFormPage` |
| `DiscrepancyComparePanel` | `data{ nhis, ogada, diff }` | NHIS vs ogada 청구 비교 (US-G06). `ReconciliationPage` 모달 내부 |
| `GuardianBillingDetailModal` | `statement`,`isOpen` | 보호자 명세 상세·인쇄 (US-J02 v1.1). `GuardianPage` billing 탭 |
| `QrScanPanel` | `token`,`onTokenChange`,`onStartScan` | QR 카메라 placeholder + 수동 토큰 (US-E04). `GuardianCheckinPage` |

### 7-7. 9차 보강 컴포넌트 (2026-06-06, US-F02·US-B03·페이지 통합)

| 컴포넌트 | 주요 props | 용도 / 화면 |
|----------|-----------|------------|
| `MedicationDuplicateAlert` | `visible`,`duplicates[]`,`onDismiss` | 동일 시각 투약 중복 경고 (US-F02). `findMedicationDuplicates()` 헬퍼 export |
| `HealthAbnormalBanner` | `abnormalFields[]` | 건강 수치 비정상 요약 — Badge+값 목록 (US-F01). `HealthPage` |
| `SessionTimeoutProvider` | (children) | 30분 idle + 60초 경고 (US-B03). `App.jsx` AuthProvider 하위 |

### 7-7c. 11차 보강 컴포넌트 (2026-06-06, 다크 모드)

| 컴포넌트 | 주요 props | 용도 / 화면 |
|----------|-----------|------------|
| `ThemeToggle` | `className?` | 라이트/다크 전환 버튼. `aria-pressed` + 아이콘(`aria-hidden`)+텍스트 라벨 병행, 44px. `AppShell` topbar에 기본 탑재 — 전 화면 우상단 노출 |

> **테마 동작**: `src/theme.js`가 단일 진실 원천. 최초값 = **저장된 사용자 선택 > OS `prefers-color-scheme`**(기본 라이트). 명시 선택 전에는 OS 변경을 추종한다. `main.jsx`가 `import "./theme"`로 시작 시 적용(FOUC 최소화). 저장은 `localStorage["ogada-theme"]` — **비민감 UI 설정만**(JWT 등 민감정보는 메모리 세션, SEC-005).

### 7-7d. 13차 보강 컴포넌트 (2026-06-06, 전사 설정 토글)

| 컴포넌트 | 주요 props | 용도 / 화면 |
|----------|-----------|------------|
| `Switch` | `label`,`checked`,`onChange(next)`,`description?`,`onLabel?`,`offLabel?`,`disabled?` | 설정 on/off 토글 (WAI-ARIA `switch`). `SettingsPage` `allow_client_self_checkin`(US-I03·§3-3). **Checkbox(동의·선택)와 구분** — 즉시 적용되는 설정값에 사용 |

> **Switch vs Checkbox**: `Checkbox`는 폼 제출 시 반영되는 **동의/선택**(예: 주민번호 수집 동의 US-D04)에, `Switch`는 즉시 적용되는 **on/off 설정**(예: 전사 셀프 체크인 허용)에 쓴다. `Switch`는 `onChange`가 **다음 boolean 값**을 인자로 받는다(이벤트 객체 아님).

### 7-7e. 14차 보강 컴포넌트 (2026-06-07, 수가 이력·Recharts 토큰)

| 컴포넌트 | 주요 props | 용도 / 화면 |
|----------|-----------|------------|
| `FeeRateHistoryPanel` | `entries[]`, `title?`, `emptyMessage?` | 수가 변경 이력 표시 (US-G00a). `{ year, grade, dailyRate, effectiveFrom, createdAt, createdByName? }`. `FeeSchedulePage` 「이력 보기」 모달 내부 |

> **Recharts 통합 (UXD-1 해소)**: 차트 색상은 `src/styles/chartColors.js`의 `CHART_COLORS`·`useChartColors()` 훅으로 주입. 다크 모드 대응은 `useChartColors()` 훅이 `html[data-theme]`를 읽어 팔레트 전환. `tokens.css`의 `--chart-color-*` 토큰과 1:1 동기화.

### 7-7b. 10차 보강 컴포넌트 (2026-06-06, US-D01 잔여 갭)

| 컴포넌트 | 주요 props | 용도 / 화면 |
|----------|-----------|------------|
| `ClientUserAccountField` | `enabled`,`onEnabledChange`,`loginId`,`onLoginIdChange`,`allowSelfCheckin`,`error` | 이용자 등록 시 **이용자 본인(`client_user`) 계정 발급·연결** (US-D01 선택, FLOWCHART §4 J). 토글 체크 시 로그인 이메일 `Field` 노출, `allow_client_self_checkin` off면 QR 셀프 비활성 `Alert` 안내. `ClientFormPage` |

> **CopayTypeSelect 실적용**: `ClientFormPage`의 본인부담 구분 입력을 raw `<Select>`에서 `CopayTypeSelect`로 교체 완료(§7-9 인계 메모 이행). 구분별 비율 help 텍스트·`aria-invalid`가 자동 적용된다.

### 7-8. 사용 예시

```jsx
// 이용자 등록 — 동의 없이는 저장 차단(US-D04)
<Field label="주민등록번호" required help="공단 청구 목적, 암호화 저장됩니다." error={err.ssn}>
  {(p) => <TextInput {...p} inputMode="numeric" placeholder="______-_______" />}
</Field>
<Checkbox label="주민등록번호 수집·이용에 동의합니다." checked={agree} onChange={...} />
<Button variant="primary" disabled={!agree}>저장</Button>
```

```jsx
// NHIS reconciliation 행 (US-G06)
<Table columns={["인정번호","이름","청구액","이용자","매칭상태"]} caption="공단 청구내역 매칭">
  {rows.map((r) => (
    <tr key={r.id} className={r.matchStatus === "DISCREPANCY" ? "ds-row--warning" : ""}>
      <td>{r.certNo}</td><td>{r.name}</td><td>{r.amount}</td><td>{r.clientName ?? "-"}</td>
      <td><StatusBadge status={r.matchStatus} map={MATCH_STATUS} /></td>
    </tr>
  ))}
</Table>
```

```jsx
// 수동 매칭 모달 (US-G06)
<Modal isOpen={open} onClose={onClose} title="이용자 수동 연결" size="md"
  footer={<><Button variant="secondary" onClick={onClose}>취소</Button><Button onClick={handleMatch}>연결</Button></>}
>
  <Select value={clientId} onChange={...}>...</Select>
  <Alert tone="warning" title="주의">동일 지점 이용자만 연결 가능합니다.</Alert>
</Modal>
```

```jsx
// AppShell + SideNav (로그인 후 전 화면)
<AppShell title="이용자 관리" nav={<SideNav role={user.role} />}
  topbarRight={<BranchSwitcher branches={...} value={activeBranch} onChange={...} />}
>
  {children}
</AppShell>
```

```jsx
// GuardianListCard — 이용자 상세 기본정보 탭 (US-D01, US-J01)
// client.guardians는 API GET /api/v1/clients/:id 응답에 포함되어야 함 (coder 담당)
<GuardianListCard
  guardians={client.guardians ?? []}
  canInvite={user?.role === "branch_admin" || user?.role === "hq_admin"}
/>
```

### 7-9. coder 인계 메모

- **지점 관리(US-C01)** — `BranchesPage`(`/branches`): 목록 표 + 등록/수정 `Modal`. 쓰기 액션은 hq_admin·branch_admin에 노출(백엔드가 최종 인가). API: `GET/POST /branches`, `PATCH /branches/{id}`(`isActive` 비활성). 상태는 `BRANCH_STATUS`.
- **월별 출석 통계(US-E05)** — `AttendanceStatsPage`(`/attendance/stats`): 대상 월(`<input type="month">`)·지점 필터 → `StatCard` 요약 + 일자별 출석률 `.ds-chart-placeholder` + 이용자별 출석 일수 표. API: `GET /attendance/stats/monthly?branchId=&yearMonth=`.
- **보호자 관리(US-K01~K02)** — `GuardiansPage`(`/guardians`), `GuardianDetailPage`(`/guardians/:id`). API: `GET /guardians`, `GET/PATCH/POST /guardians/:id/clients`. `MaskedPhone`·`LinkedClientsCard` 사용.
- **입금·미납(US-L01~L02)** — `PaymentPage`(`/billing/payments`), `OverduePage`(`/billing/overdue`). API: `POST /billing/claims/:id/payments`, `GET /billing/overdue`. CMS 제외(v2).
- **등급 이력(US-M01)** — `ClientDetailPage` 「등급 이력」탭. API: `GET /clients/:id` 응답에 `ltcGradeHistory: [{ changedAt, previousGrade, newGrade, reason? }]` 포함.
- **대시보드 실데이터(US-M02)** — `DashboardWidgetGrid` + `GET /api/v1/dashboard/branch|hq`. StatCard 데모 제거, 3블록: 출석·미납·건강/NHIS.
- **2단 SideNav(US-UX-02)** — `SideNav.jsx` `NAV_CONFIG` 그룹 구조. 청구 그룹에 **공단 엑셀 import**(`/billing/nhis-import`) 포함. 신규 route는 해당 그룹 `items`에 등록.
- **청구 상세(US-G02)** — `BillingDetailPage`(`/billing/:id`): `GET /billing/claims/:id`, items, status-history. 목록에서 이용자명 링크로 진입. `window.print()` + `@media print` 레이아웃.
- **결석(US-E01)** — `AttendanceAbsentModal` + `POST /attendance/absent`. 미처리(`PENDING`) 행에 「결석」버튼.
- **이용자 사진(US-D01)** — `ClientPhotoField` + `POST /clients/:id/photo` (multipart). `altText` 필수 when photo present.
- **보호자 초대(US-J01)** — `GuardianInviteModal` + `POST /clients/:id/guardian-invites`. v1.1 API 미준비 시 404/501 안내.
- **보호자 목록(US-D01·US-J01)** — `GET /clients/:id` 응답 `guardians[]`. `GuardianListCard` 초대 API는 v1.1.
- **귀가 처리(US-E01)** — `AttendancePage`: 「귀가」클릭 → `CheckoutModal` + `POST /attendance/checkout` `{ transportMethod }`. 표 교통편 컬럼은 저장 후 `transportMethod` 표시만.
- **NHIS 비교(US-G06)** — `ReconciliationPage` 「비교」버튼 → `Modal` + `DiscrepancyComparePanel`. API: `GET /billing/nhis-imports/:batchId/rows/:rowId/compare`.
- **보호자 명세(US-J02)** — `GuardianPage` billing 탭 행 클릭 → `GuardianBillingDetailModal`. API: `GET /guardian/clients/:id/billing/:claimId`.
- **본인부담 구분(US-D01)** — ✅ **10차 완료**: `ClientFormPage`의 copay `<Select>`를 `CopayTypeSelect`로 교체함. `COPAY_TYPES` 상수 공유.
- **이용자 본인 계정(US-D01·FLOWCHART §4 J)** — `ClientFormPage` 하단 「이용자 본인 계정」 섹션의 `ClientUserAccountField`. 폼 payload에 `issueClientUser`(boolean)·`clientUserLoginId`(발급 시 email)를 포함한다. 백엔드: `POST /api/v1/clients` 응답·요청에 이 두 필드 처리 — 발급 시 `client_user` 계정 생성 + 이용자 연결, 임시 비밀번호 메일. `allowSelfCheckin` 값은 Organization `allow_client_self_checkin` 설정(현재 `user.allowClientSelfCheckin` 가정 — coder가 실제 소스에 맞게 배선). QR 셀프 체크인은 설정 on일 때만 동작(§3-3, US-E04).
- **QR 체크인(US-E04)** — `GuardianCheckinPage`: `QrScanPanel` + `ClientSelector`. html5-qrcode는 `#qr-reader`를 `.ds-qr-scan__viewport` 내부에 마운트 (UXD-2).
- **투약 중복(US-F02)** — `HealthPage`: `GET /clients/:id/medications?date=today`로 `recentMedications` 초기화. API 409 시 `MedicationDuplicateAlert`와 동일 UX 유지.
- **전사 설정 토글(US-I03·§3-3)** — `SettingsPage` 「조직 설정」탭의 `Switch`(`allow_client_self_checkin`). 초기값은 `GET /api/v1/settings/organization`으로 주입(현재 `user.allowClientSelfCheckin` 가정 — coder가 실제 소스에 배선), 변경 시 `PATCH /api/v1/settings/organization { allowClientSelfCheckin }` 호출(낙관적 업데이트 또는 응답 후 확정). 이 값은 US-E04 QR 셀프 체크인(`client_user`) 허용과 `ClientUserAccountField`(US-D01) 안내에 연동된다.
- **세션 만료(US-B03)** — `SessionTimeoutProvider`가 idle 감지. refresh 토큰 연장 API는 coder가 `onExtend`에 연동.
- **수가 이력(US-G00a)** — `FeeSchedulePage` 「이력 보기」 → `Modal` + `FeeRateHistoryPanel`. API: `GET /api/v1/billing/fee-schedules/history?year=` 응답에 `[{ year, grade, dailyRate, effectiveFrom, createdAt, createdByName? }]` 배열 포함. 현재 `historyEntries` 빈 배열 스켈레톤 — coder가 API 연동.
- **NHIS 배치 상태(US-G04)** — `BATCH_STATUS` 상수를 `import { BATCH_STATUS } from "../components/ui"` 로 가져온다(NHISImportPage 로컬 정의 제거·14차). coder는 모든 신규 페이지에서 Badge 모듈 상수를 사용.
- **ToastProvider** — `main.jsx`에서 `<BrowserRouter>` 안 `<App />`을 감싼다. `SessionTimeoutProvider`는 `App.jsx` `AuthProvider` **내부**.
- **FileUpload `accept`**: NHIS 엑셀은 `".xlsx,.xls"`.
- **Modal `aria-labelledby`**: `useId()` 기반 고유 ID — 동일 페이지에 Modal 복수 렌더 시 중복 ID 없음. React 18+ 필수.

---

## 8. 화면 목록 & 라우트 (develop 기준) [UXD]

### 8-1. 전체 라우트

| 경로 | 컴포넌트 | 허용 역할 | User Story |
|------|---------|---------|-----------|
| `/` | `LoginPage` | 공개 | US-B01 |
| `/dashboard` | `DashboardPage` | branch_admin, social_worker, caregiver, hq_admin | US-H01 |
| `/dashboard/hq` | `DashboardPage` | hq_admin | US-H02 |
| `/branches` | `BranchesPage` | hq_admin, branch_admin | US-C01 |
| `/clients` | `ClientListPage` | branch_admin, social_worker, caregiver, hq_admin | US-D02 |
| `/clients/new` | `ClientFormPage` | branch_admin, social_worker, hq_admin | US-D01 |
| `/clients/:id` | `ClientDetailPage` | branch_admin, social_worker, caregiver, hq_admin | US-D03, **US-M01** |
| `/guardians` | `GuardiansPage` | branch_admin, hq_admin, social_worker | **US-K01** |
| `/guardians/:id` | `GuardianDetailPage` | branch_admin, hq_admin, social_worker | **US-K02** |
| `/clients/:id/edit` | `ClientFormPage` | branch_admin, social_worker, hq_admin | US-D01 |
| `/attendance` | `AttendancePage` | branch_admin, social_worker, caregiver, hq_admin | US-E02 |
| `/attendance/checkin` | `AttendancePage` | branch_admin, social_worker, caregiver, hq_admin | US-E01 |
| `/attendance/qr/generate` | `QrGeneratePage` | branch_admin, social_worker, caregiver, hq_admin | US-E03 |
| `/attendance/stats` | `AttendanceStatsPage` | branch_admin, social_worker, caregiver, hq_admin | US-E05 |
| `/health` | `HealthPage` | branch_admin, social_worker, caregiver, hq_admin | US-F01~F03 |
| `/health/:clientId` | `HealthDetailPage` | branch_admin, social_worker, caregiver, hq_admin | US-F04 |
| `/billing` | `BillingPage` | branch_admin, hq_admin | US-G02, US-G07 |
| `/billing/:id` | `BillingDetailPage` | branch_admin, hq_admin | **US-G02**, US-G07 |
| `/billing/payments` | `PaymentPage` | branch_admin, hq_admin | **US-L01** |
| `/billing/overdue` | `OverduePage` | branch_admin, hq_admin | **US-L02** |
| `/billing/nhis-import` | `NHISImportPage` | branch_admin, hq_admin | US-G04 |
| `/billing/nhis-import/:batchId` | `ReconciliationPage` | branch_admin, hq_admin | US-G06 |
| `/billing/fee-schedules` | `FeeSchedulePage` | hq_admin | US-G00a |
| `/billing/copay-rates` | `CopayRatePage` | hq_admin | US-G00b |
| `/platform` | `PlatformPage` | platform_admin | US-A01, US-A02 |
| `/guardian` | `GuardianPage` | guardian, client_user | US-I02, US-J02 |
| `/guardian/checkin` | `GuardianCheckinPage` | guardian, client_user | US-E04 |
| `/settings` | `SettingsPage` | sysadmin, hq_admin, platform_admin | US-I03 |
| `/forbidden` | `ForbiddenPage` | 공개 | — |

### 8-2. 사이드 네비게이션 (SideNav.jsx) — **2단 그룹 (US-UX-02)**

역할별 메뉴는 `SideNav.jsx`의 `NAV_CONFIG` **그룹 배열**에 정의. 각 그룹: `{ id, label, items: [{ label, path }] }`.

| 그룹 | 하위 예시 |
|------|----------|
| 운영 | 대시보드, 지점, 이용자, **보호자** |
| 출석 | 현황, 통계, QR |
| 기록 | 건강 |
| 청구 | 청구·정산, **공단 엑셀 import**, **입금**, **미납**, 수가표(hq) |

> **모바일**: 그룹별 접힘/펼침(`aria-expanded`). **데스크톱**: 항상 펼침(769px+).

> **active 매칭**: 동일 prefix의 하위 메뉴가 있는 경로(`/dashboard`, `/guardian`, `/attendance`, `/billing`)는 `EXACT_MATCH_PATHS`에 등록해 `NavLink end`로 **정확히 일치할 때만** 활성 처리한다(예: `/attendance/stats` 진입 시 「출석 관리」가 동시 활성화되지 않음).

| 역할 | 메뉴 항목 |
|------|---------|
| branch_admin | **운영**(대시보드·지점·이용자·보호자) · **출석** · **기록** · **청구**(입금·미납) |
| caregiver | 운영(대시보드) · 출석(체크인·QR) · 기록(건강) |
| social_worker | 운영(대시보드·이용자·보호자) · 출석(통계) · 기록(건강) |
| hq_admin | 운영(+통합/지점 대시보드) · 출석 · 기록 · **청구**(수가·copay·입금·미납) · 설정 |
| platform_admin | 고객사 관리, 시스템 설정 |
| guardian / client_user | 이용자 현황, QR 체크인 |

### 8-3. 미구현·후속 (coder TODO)

> **2026-06-06 4차 보강**: `BranchesPage`(US-C01)·`AttendanceStatsPage`(US-E05) **스켈레톤 추가 완료**.
> **2026-06-06 6차 보강 (v1.2 P0)**: `SideNav` 2단 그룹, `GuardiansPage`·`GuardianDetailPage`, `PaymentPage`·`OverduePage`, `GradeHistoryTimeline` 탭, `DashboardWidgetGrid`.
> **2026-06-06 7차 보강**: `BillingDetailPage`, `ClaimStatusTimeline`, `GuardianInviteModal`, `ClientPhotoField`, `AttendanceAbsentModal`, SideNav NHIS import.

| 화면/기능 | 경로/파일 | 비고 |
|----------|-----------|------|
| 청구 상세 API | `BillingDetailPage` | US-G02 — `GET /billing/claims/:id` + items + status-history |
| 결석 API | `AttendancePage` | US-E01 — `POST /attendance/absent` |
| 이용자 사진 API | `ClientFormPage` | US-D01 — `POST /clients/:id/photo` multipart |
| 보호자 API 연동 | `GuardiansPage`, `GuardianDetailPage` | US-K01~K02 — `GET /guardians*` |
| 입금·미납 API | `PaymentPage`, `OverduePage` | US-L01~L02 |
| 등급 이력 API | `ClientDetailPage` grade 탭 | US-M01 — `ltcGradeHistory[]` |
| 대시보드 API | `DashboardPage` | US-M02 — `/dashboard/*` |
| 직원 관리 | `/staff` | Should — v1 이후 |
| 보호자 초대 실 API 연동 | `GuardianListCard` 내 버튼 | US-J01 v1.1 — `POST /clients/:id/guardian-invites` |
| QR 카메라 스캔 | `GuardianCheckinPage` | html5-qrcode 등 라이브러리 연동 (§10 UXD-2) |
| 건강·대시보드·출석통계 차트 | `HealthDetailPage`, `DashboardPage`, `AttendanceStatsPage` | Recharts 등 — §10 참고 (`.ds-chart-placeholder` 위치) |

---

## 9. CSS 유틸리티 클래스 [UXD]

| 클래스 | 용도 |
|--------|------|
| `.ds-sr-only` | 스크린리더 전용 텍스트 (시각적 숨김) |
| `.ds-skip-link` | 본문 바로가기 키보드 링크 |
| `.ds-grid` | `auto-fit minmax(220px,1fr)` 대시보드 카드 그리드 |
| `.ds-form-row` | `auto-fit minmax(200px,1fr)` 폼 필드 그리드 |
| `.ds-form-section` | 폼 섹션 구분 박스 |
| `.ds-action-bar` | 목록 상단 검색/필터/액션 바 |
| `.ds-consent-box` | 주민번호 수집 동의 안내 박스 (warning 배경) |
| `.ds-masked` | 마스킹 텍스트 (모노스페이스 + 연회색) |
| `.ds-avatar` | 이용자 이니셜 아바타 원형 |
| `.ds-status-dot` | 인라인 상태 점 (success/warning/neutral) |
| `.ds-row--warning` | 표 행 경고 강조 (DISCREPANCY) |
| `.ds-row--danger` | 표 행 위험 강조 (UNMATCHED) |
| `.ds-filter-chip` | 상태 필터 칩 (FilterChips) |
| `.ds-chart-placeholder` | 차트 연동 전 플레이스홀더 |
| `.ds-qr-panel` | QR 생성·인쇄 패널 |
| `.ds-client-picker` | NHIS 수동 매칭 combobox |
| `.ds-dl-grid` | 설정·상세 description list 그리드 |
| `.ds-linked-clients` | 보호자 상세 연결 이용자 카드 (US-K02) |
| `.ds-timeline` | 등급 변동 이력 타임라인 (US-M01) |
| `.ds-dashboard-widgets` | 대시보드 위젯 그리드 (US-M02) |
| `.ds-masked-phone` | 마스킹 연락처 링크 |
| `.ds-sidenav__sublist` | 2단 SideNav 하위 메뉴 (US-UX-02) |
| `.ds-grid--2` | 2열 폼 그리드 (초대 모달 등) |
| `.ds-photo-field` | 이용자 사진 업로드+미리보기 (US-D01) |
| `.ds-select--inline` | 표 내 인라인 select — 44px 터치 타깃 |
| `.ds-client-picker__option--active` | combobox 키보드 활성 옵션 |
| `.ds-timeline--compact` | 청구 상태 이력 등 컴팩트 타임라인 |
| `.ds-client-selector` | 복수 이용자 radiogroup (US-E04, US-J02) |
| `.ds-compare-panel` | NHIS vs ogada 청구 비교 패널 (US-G06) |
| `.ds-billing-statement` | 보호자 본인부담금 명세서 (US-J02) |
| `.ds-qr-scan` | QR 카메라 + 수동 토큰 입력 (US-E04) |
| `.ds-health-abnormal-list` | 건강 비정상 수치 목록 (US-F01) |
| `.ds-health-alert-list` | 보호자 포털 건강 알림 — 텍스트+배지 (US-I02) |
| `.ds-link-button` | Alert 내 텍스트 액션 링크 (투약 중복 확인) |
| `.ds-feedback--success/danger` | QR·폼 결과 피드백 (role=alert) |
| `.ds-client-user-account` | 이용자 본인 계정 발급 필드 묶음 (US-D01) |
| `.ds-topbar__actions` | 상단바 우측 액션 묶음 (테마 토글 + topbarRight) |
| `.ds-theme-toggle` | 라이트/다크 전환 버튼 (11차, 480px 이하 라벨 숨김) |
| `.ds-label` | 단독 라벨 (Field 래퍼 미사용 시, 12차) |
| `.ds-login` / `.ds-login__brand`·`__logo`·`__wordmark`·`__title`·`__subtitle`·`__error` | 로그인 진입 카드·브랜드 모노그램 (12차, US-B01) |
| `.ds-switch` / `.ds-switch__text`·`__label`·`__description`·`__control`·`__track`·`__thumb`·`__state` | 설정 on/off 토글 (13차, US-I03 — WAI-ARIA switch) |
| `.ds-progress-steps` / `__step`·`__dot`·`__label` / `--done`·`--active`·`--failed` | NHIS 배치 진행 단계 시각화 (14차, US-G04) |
| `.ds-fee-history` / `__title`·`__empty`·`__year-group`·`__year-label`·`__table` | 수가 이력 패널 (14차, US-G00a — FeeRateHistoryPanel) |
| `.ds-fee-table-cell` | 표 내 수가 인라인 입력 셀 (14차, FeeSchedulePage) |

---

## 11. 브랜드·파비콘 (US-UX-01) [UXD]

> **2026-06-06 planner 지시**: v1.1 Must — 탭·북마크·모바일 홈추가 아이콘. COD 구현 전 **본 절 확정안** 따름.

### 11-1. 컨셉

| 항목 | 값 |
|------|-----|
| 브랜드명 | **ogada** (소문자, 로고 타입) |
| 심볼 | 원형 배경 + 흰색 **「o」** 모노그램 (주간보호·케어 연상) |
| Primary | `--color-primary` = blue-600 (`#1d4ed8`). ※ favicon `theme-color`도 동일 토큰값 사용 권장 (이전 표기 `#2563eb`는 blue-500 — 토큰 darken 후 불일치, `#1d4ed8`로 통일) |
| 배경 | Primary fill, 심볼 `#ffffff` |
| 톤 | 과도한 의료 적십자·하트 **금지** — B2B SaaS·신뢰·접근성 |

### 11-2. 파일·경로 (COD)

| 파일 | 크기 | 용도 |
|------|------|------|
| `public/favicon.svg` | 벡터 | 최신 브라우저 기본 |
| `public/favicon.ico` | 16+32 multi | 레거시 탭 |
| `public/apple-touch-icon.png` | 180×180 | iOS 홈 화면 |
| `index.html` | — | `<link rel="icon" href="/favicon.svg" type="image/svg+xml">`, `rel="apple-touch-icon"`, `<meta name="theme-color" content="#1d4ed8">` (= `--color-primary`) |

### 11-3. SVG 가이드 (COD 생성 기준)

- viewBox `0 0 32 32`, 원형 배경 radius 16, 중앙 「o」 sans-serif **700**, font-size ~18
- 32px에서 「o」 식별 가능 — 16px 축소 시 실루엣 유지
- 다크 모드: 동일 primary (후속 §10 다크 토큰과 별도 `media (prefers-color-scheme: dark)` 검토)

### 11-4. 완료 검증

- [ ] Chrome·Safari 탭에 ogada 파란 원 아이콘 표시
- [ ] iOS 「홈 화면에 추가」 180px 아이콘 선명
- [ ] `npm run build` 후 `dist/`에 favicon 자산 포함
- [ ] **(10차)** 브랜드 색을 `--color-primary`(`#1d4ed8`)로 통일 — `favicon.svg`·`theme-color` 반영 완료. 래스터 자산(`favicon.ico`·`apple-touch-icon.png`)은 **coder가 동일 색(`#1d4ed8`)으로 재생성** 필요(바이너리라 UXD가 직접 생성하지 않음).

---

## 10. 미해결·후속 (UX) [UXD]

- 아이콘 세트 미선정 — 의존성 추가는 coder/planner 협의 필요(현재 텍스트 기반).
- ~~차트(월별 출석률 US-H01/F04) — Recharts vs Chart.js 미선정~~ → **14차 UXD-1 해소**: **Recharts** 채택. 토큰: `tokens.css` `--chart-color-*`, JS 매핑: `src/styles/chartColors.js` `CHART_COLORS` / `useChartColors()` 훅. 다크 팔레트 `CHART_COLORS_DARK` 동기화.
- QR 스캐너 — **html5-qrcode** vs native BarcodeDetector → #UXD-2. `GuardianCheckinPage`는 현재 토큰 수동입력 폴백 제공.
- ~~다크 모드 미정~~ → **11차 구현 완료**: `tokens.css` `[data-theme="dark"]` 토큰 오버라이드 + `ThemeToggle`(AppShell topbar) + `theme.js`. 컴포넌트가 시맨틱 토큰만 쓰므로 코드 변경 0. 대비 AA 검증 §2-4. 후속: 차트(Recharts 등) 도입 시 다크 팔레트 색 매핑 별도 확인.
- 미확정 사항은 `docs/planning/PLAN_NOTES.md`의 `### [UXD] UX 설계 질문` 섹션에 기록.
- Toast: `ToastProvider`를 `main.jsx`에 추가 후 `useToast()`로 API 연동 피드백. **9차 배선 완료**.
- SessionTimeoutModal: `SessionTimeoutProvider`가 AuthContext 30분 타이머와 연동 (US-B03). **9차 배선 완료**.
- 보호자 초대(US-J01 v1.1): `GuardianListCard` 「초대 발송」 버튼은 현재 `disabled` — v1.1 착수(v1 backend merged 이후) 시 활성화.
- **고대비/강제 색상(12차)**: `forced-colors`/`prefers-contrast` 규칙은 CSS만으로 동작(컴포넌트 코드 변경 0). **tester 검증 권장**: Windows 고대비 모드·`prefers-contrast: more`에서 로그인·대시보드·청구 표·모달 캡처해 경계선·포커스 식별성 확인.
- `styles.css`의 데모 잔여 클래스(`.role-link`·`.demo-grid`)는 LoginPage 정비(12차)로 미사용 — 별도 데모 화면 부활 전까지 제거 후보(coder 정리 시).

---

*이 문서는 ux_designer 에이전트(UXD)가 관리합니다. 토큰·컴포넌트 변경 시 본 문서와 `memory/decisions.md`를 동기화하세요.*
