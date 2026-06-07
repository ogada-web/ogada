<!-- doc:owner=UXD doc:audience=PLN,COD,TSR updated=2026-06-07T19:30:00+09:00 -->
# ogada 디자인 시스템 (product/DESIGN_SYSTEM.md)

> **작성**: ux_designer 에이전트 (`UXD`)
> **최초 작성일**: 2026-06-06
> **최종 갱신**: 2026-06-07 (36차 — **15개 누락 화면 전체 구현 완료** — ModulePage 스텁 → 실 구현 페이지 교체: `ClientFormPage`(US-D01)·`QrGeneratePage`(US-E03)·`GuardianCheckinPage`(US-E04)·`AttendanceStatsPage`(US-E05)·`HealthDetailPage`(US-F04)·`BillingDetailPage`(US-G02/G07)·`PaymentPage`(US-G04/G05)·`OverduePage`(US-G06)·`FeeSchedulePage`(US-G01)·`CopayRatePage`(US-G01)·`GuardiansPage`(US-H01-H04)·`GuardianDetailPage`(US-K02)·`BranchesPage`(US-B01-B04)·`PlatformPage`(US-A01/A02)·`SettingsPage`(US-I03). `App.jsx` 전체 라우트 신규 경로 추가(`/clients/new`, `/clients/:id/edit`, `/billing/claims/:id`, `/health/:clientId`, `/attendance/checkin/qr`, `/guardians/:id`). `npm run build` 114 modules PASS. `git push origin develop` 완료.)
> **이전 갱신**: 2026-06-07 (34차 — **USER_STORIES·FLOWCHART Must 페이지 연동 + 도메인 UI 보강 + 접근성 재점검** — ① **이용자 상세 탭**(US-D03 `Tabs`/`TabPanel` 기본·건강·출석·청구)·`MaskedRevealField`(US-D04 주민번호)·`GuardianInviteModal`(US-J01). ② **목록/대시보드/청구** — `ClientListPage` `SearchInput`+`Pagination`(US-D02)·`DashboardWidgetGrid`+`StatCard`(US-H01/M02)·`BillingPage` `FilterChips`+`MonthInput`(US-G07). ③ **NHIS/건강/세션** — `NhisImportGuidePanel`+`FileUpload`(US-G04)·`HealthAbnormalBanner`(US-F01)·`SessionTimeoutProvider`+`SessionTimeoutModal`(US-B03). ④ 페이지 오류 `Alert`+`.ds-page-alert` 통일(redundant `role=alert` 제거). 회귀 +11(`Switch`·`MaskedRevealField`·`NhisImportGuidePanel`·`FileUpload`·`ClientDetailPage` 탭/모달), `npm test` 69/22·build PASS)
> **이전 갱신**: 2026-06-07 (33차 — **USER_STORIES·FLOWCHART 대비 기반 UI·레이아웃 보강 + 접근성 재점검** — ① **2단 `SideNav`**(US-UX-02, `layout/navConfig.js`+`SideNav.jsx`) 운영·출석·기록·청구 4그룹·모바일 `aria-expanded` 토글. ② **Must 목록/상세 기반 컴포넌트** `StatCard`·`SearchInput`·`FilterChips`·`Pagination`·`Table`·`Tabs`/`TabPanel`·`BranchSwitcher`(US-B02)·`LogoutButton`(US-B03) 신설 + barrel export. ③ **`AppShell` 통합** — flat NavLink → `SideNav`+`LogoutButton`+`BranchSwitcher` topbar. ④ **`LoginPage` → `PublicAuthLayout`**(US-B01) 공개 인증 h1·skip 일관. ⑤ **누락 CSS** `.ds-list*`·`.ds-breadcrumb`·`.ds-form-grid`·`.ds-tabs*`·`.ds-pagination`·`.ds-sidenav__*`·`.ds-branch-switcher` 승격. 회귀 `FilterChips`·`Tabs`·`BranchSwitcher`·`LogoutButton`·`SideNav` test +12, `npm test` 58/18·build 86 modules PASS)
> **이전 갱신**: 2026-06-07 (32차 — **실측 baseline `7170b2a` 접근성 재점검** — ① **`Alert` 라이브 리전 정중도(politeness)를 tone 기준으로 분기**: `danger`/`warning`→`role="alert"`(assertive), `info`/`success`/`neutral`→`role="status"`(polite). 정적 안내(info)가 assertive로 스크린리더를 끊던 갭 해소, `role` 명시 override는 유지. ② **`PublicAuthLayout` 컴포넌트 신설**(§7-7n 문서화만 있고 재이관 baseline엔 부재) — skip link + 브랜드 + **페이지 `h1`** 제공. ③ **`GuardianInvitationAcceptPage`(US-J01) 헤딩 계층 결함 수정** — 기존엔 `<h1>` 없이 `Card` `<h2>`만 있던 공개 화면을 `PublicAuthLayout`로 전환해 단일 h1·skip link·브랜드 일관성 확보. `Alert.test.jsx`(4)·`PublicAuthLayout.test.jsx`(2) 추가, `npm test` 46/13·build 75 modules·audit 0 PASS)
> **이전 갱신**: 2026-06-07 (31차 — **실측 baseline `c3b863e` 접근성 재점검** — `GuardianInvitationList`(US-J01) 행별 재발송/취소 `Button`에 보호자명 포함 `aria-label` 추가(여러 행에서 SR이 동작 대상을 식별 가능)·`aria-busy` 처리, 회귀 테스트 `GuardianInvitationList.test.jsx` +1. `NavLink`는 활성 시 `aria-current="page"` 기본 적용 확인. `npm test` 10/10·build 70 modules PASS)
> **이전 갱신**: 2026-06-07 (30차 — **스켈레톤 재이관 baseline 위에 폼 입력·토글·연락처 마스킹 컴포넌트 보강** — `Switch`(US-I03·§3-3)·`DateInput`(US-D01·§3-1)·`MonthInput`(US-E05·G02/G04/G07)·`MaskedPhone`(US-K01·L02), `DashboardPage` AppShell skip-link/topbar 적용·존재하지 않는 `ds-stack*` 클래스 제거, `ForbiddenPage` `.ds-auth-page` 패턴 적용)
> **이전 갱신**: 2026-06-07 (29차 — **스켈레톤 재이관 후 CSS 토큰·컴포넌트 스타일·핵심 UI 초안** — `tokens.css`·`components.css`·`theme.js`·`chartColors.js`·`components/ui/` Button/Field/TextInput/Card/Alert/Badge/Modal/ThemeToggle 등 + `LoginPage` DS 적용)
> **이전 갱신**: 2026-06-08 (28차 — **`DateInput` 표준화 잔여**(US-D01 `ClientFormPage` 생년월일·인정유효일·US-L01 `PaymentRecordModal` 입금일)·**접근성 재점검**(`ClientPhotoField` 사진 버튼 `aria-label`·`GuardianInviteModal` `aria-busy`·`ClientDetailPage` 초대 Alert `ds-page-alert`))
> **이전 갱신**: 2026-06-08 (27차 — **`DateInput`**(§3-1 감사·로그인 이력 기간 필터)·**`GuardianInvitationList`**(US-J01 초대 이력·`INVITATION_STATUS`·재발송/취소 `aria-label`)·`GuardianListCard` 초대 이력 통합·`AuditLogPanel`/`LoginHistoryPanel`/`ClientPhotoField` raw input→`TextInput`/`DateInput`·만료 토큰 수락 폼 잠금)
> **이전 갱신**: 2026-06-08 (26차 — **US-J01 보호자 초대 수락 UI** `PublicAuthLayout`+`GuardianInvitationAcceptForm`(LoginPage 카드 패턴·AppShell 금지)·**`INVITATION_STATUS` Badge**(PENDING/SENT/ACCEPTED/EXPIRED/REVOKED)·`.ds-auth-page*` CSS·접근성 `autoComplete`·수락 완료 폼 잠금)
> **이전 갱신**: 2026-06-07 (23차 — **`ClientDetailPage`(US-D03/D04/M01) 잔여 인라인 style 전량 제거** → `.ds-inline-actions`·`.ds-client-summary*`·`.ds-dl-grid`·`.ds-section-gap`·`.ds-table-empty` 유틸 승격, `ClientFormPage` 폼 액션 `.ds-form-actions--end`, `PlatformPage` 사업자번호 `.ds-mono`, `GuardiansPage` `.ds-text-muted` — 다크/forced-colors 일관성·접근성 재점검)
> **이전 갱신**: 2026-06-07 (21차 — **`FeeScheduleTable`**(US-G00a)·**`BillingDetailPage` 상태 확인 모달**(US-G07)·**`StatCard tone=danger`**(US-L02)·텍스트 유틸(`.ds-text-*`·`.ds-mono`·`.ds-diff-amount`)·Must 페이지 **`ds-page-alert`** 잔여 통일·접근성 재점검)
> **이전 갱신**: 2026-06-07 (20차 — **`BillingStatusConfirmModal`**(US-G07)·**`NhisImportGuidePanel`**(US-G04)·**`CopayRateTable`**(US-G00b)·**`GuardianDailySummary`**·**`HealthAlertList`**(US-I02/H01)·Must 페이지 **`ds-page-alert`** 잔여 통일·접근성 재점검)
> **이전 갱신**: 2026-06-07 (19차 — **`SettingsPage` 보안 탭** `PasswordChangeModal`+`PasswordResetRequestModal` 통합·`token` useAuth 누락 버그 수정·`.ds-security-panel` CSS 신설·§8-3 미구현 현행화·접근성 재점검 완료)
> **이전 갱신**: 2026-06-07 (18차 — **`LoginHistoryPanel`**(REQUIREMENTS §3-1)·**`PasswordResetRequestModal`**(§3-1)·페이지 오류 **`Alert`+`ds-page-alert` 통일**·`PlatformOrgDetailModal.test.jsx`)
> **이전 갱신**: 2026-06-07 (17차 — **`AuditLogPanel`**·**`BackupSettingsPanel`**(US-I03)·**`PasswordChangeModal`**(US-A02)·**`FilterChips` counts**(US-G07)·페이지 `Alert`/`ds-link` 통일·`Modal` 필수 모드 props)
> **이전 갱신**: 2026-06-07 (15차 — **Recharts 접근성 차트 컴포넌트**(`ChartContainer`·`AttendanceRateChart`·`HealthTrendChart`·`BranchCompareChart`) 신설, 플레이스홀더→실차트 교체(US-F04/H01/E05/H02), `useChartColors` 테마 실시간 반영, `.ds-chart`·`.ds-link` CSS, UXD-1·UXD-4 완료)
> **이전 갱신**: 2026-06-07 (14차 — **`BATCH_STATUS` 공유 상수 승격**(NHISImportPage 로컬 정의 → Badge 모듈), **`FeeRateHistoryPanel`** 신설(US-G00a 수가 이력·연도별 그룹), **Recharts 차트 색상 토큰**(토큰·chartColors.js·다크 팔레트), **`ds-progress-steps`·`ds-fee-history`·`ds-fee-table-cell`** CSS, §2-3 BATCH_STATUS 도메인 매핑 추가, UXD-1·UXD-4 해소)
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
| 보호자 초대 (US-J01) | `PENDING` | neutral | 대기 |
| | `SENT` | info | 발송됨 |
| | `ACCEPTED` | success | 수락됨 |
| | `EXPIRED` | warning | 만료 |
| | `REVOKED` | danger | 취소됨 |

> 매핑 객체는 `components/ui/Badge.jsx`의 `BILLING_STATUS`·`MATCH_STATUS`·`ATTENDANCE_STATUS`·`BRANCH_STATUS`·`BATCH_STATUS`·**`INVITATION_STATUS`**로 코드화 → `<StatusBadge status map>` 사용. `BATCH_STATUS`는 14차에 NHISImportPage 로컬 정의 → Badge 모듈로 승격.

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

> **35차 (2026-06-07)**: v1.2 P0 컴포넌트·SideNav 보강 — ① **`HealthAlertList`**(US-M02) Badge 「주의」+이름+사유, `aria-label` list. ② **`GuardianListCard`**(US-D01/K01) `MaskedPhone`·대표 Badge·`aria-label` 초대 버튼·`Card titleId`→`aria-labelledby`. ③ **`GradeHistoryTimeline`**(US-M01) `<ol aria-label="등급 변동 이력">`+sr-only 등급 변경. ④ **`BatchProgressSteps`**(US-G04) `nav`+sr-only 단계 상태·FAILED 처리. ⑤ **`CopayTypeSelect`**(US-D01) Field 라벨·비율 help. ⑥ **SideNav v1.2** — 지점·보호자·입금·미납·수가표 등 4그룹 하위 route 확장(US-UX-02 인수 조건 진전). `npm test` **78/27 PASS**·build **99 modules**.
> **34차 (2026-06-07)**: USER_STORIES·FLOWCHART Must 페이지 연동 — ① **ClientDetailPage** `Tabs`/`TabPanel`(US-D03 기본·건강·출석·청구)·`MaskedRevealField`(US-D04)·`GuardianInviteModal`(US-J01). ② **ClientListPage** `SearchInput`+`Pagination`(US-D02). ③ **DashboardPage** `DashboardWidgetGrid`+`StatCard`(US-H01/M02). ④ **BillingPage** `FilterChips`+`MonthInput`(US-G07). ⑤ **NHISImportPage** `NhisImportGuidePanel`+`FileUpload`(US-G04). ⑥ **HealthPage** `HealthAbnormalBanner`(US-F01). ⑦ **SessionTimeoutProvider**+`SessionTimeoutModal`(US-B03) `App.jsx` 배선. ⑧ Must 페이지 `Alert`+`.ds-page-alert` 통일. `Switch.test.jsx`·`MaskedRevealField.test.jsx`·`NhisImportGuidePanel.test.jsx`·`FileUpload.test.jsx` 회귀. `npm test` 69/22 PASS.
> **33차 (2026-06-07)**: USER_STORIES·FLOWCHART 대비 기반 UI 보강 — ① **2단 SideNav**(US-UX-02): `layout/SideNav.jsx`+`navConfig.js` 4그룹(운영·출석·기록·청구), `EXACT_MATCH_PATHS` prefix 충돌 방지, 모바일 그룹 토글 `aria-expanded`/`aria-controls`, 데스크톱 항상 펼침. ② **목록·상세 기반 컴포넌트**: `StatCard`(US-H01/M02)·`SearchInput`(US-D02)·`FilterChips`(US-G07 radiogroup+counts)·`Pagination`(nav+aria-current)·`Table`(caption 래퍼)·`Tabs`/`TabPanel`(WAI-ARIA 좌우/Home/End)·`BranchSwitcher`(US-B02, 2지점+ 시 노출)·`LogoutButton`(US-B03, `{이름} 로그아웃` aria-label). ③ **AppShell**: flat 1단 NavLink 제거 → `SideNav`+topbar `BranchSwitcher`+`LogoutButton`. ④ **LoginPage**: `PublicAuthLayout` 전환 — 공개 인증 화면 h1·skip·브랜드 일관(US-B01). ⑤ **CSS 갭 해소**: 페이지가 참조하던 `.ds-list`/`.ds-breadcrumb`/`.ds-form-grid` 미정의 → `components.css` 승격 + tabs·pagination·sidenav group·branch-switcher 스타일. `npm test` 58/18·build 86 modules PASS.
> **32차 (2026-06-07)**: 실측 baseline `7170b2a` 접근성 재점검 — ① **`Alert` 라이브 리전 정중도**: 기존 모든 tone이 `role="alert"`(assertive)이라 정적 info/success 배너가 스크린리더 흐름을 끊던 갭을 **tone 기준 분기**로 해소(`danger`/`warning`→`alert`, `info`/`success`/`neutral`→`status`). 호출부의 `role` 명시는 그대로 우선(override). ② **공개 인증 화면 헤딩 계층**: `GuardianInvitationAcceptPage`(US-J01)가 페이지 `<h1>` 없이 `Card` 제목(`<h2>`)만 노출하던 결함을 **`PublicAuthLayout`** 도입으로 수정 — 단일 h1·skip link(`#public-auth-content`)·브랜드 모노그램을 LoginPage와 일관되게 제공(미인증 화면은 AppShell/SideNav 금지 원칙 유지, §7-7n). `Alert.test.jsx`·`PublicAuthLayout.test.jsx` 회귀 추가.
> **31차 (2026-06-07)**: 실측 baseline `c3b863e` 접근성 재점검 — `GuardianInvitationList`(US-J01) 표 행의 「재발송」/「취소」`Button`이 동일 라벨이라 여러 행에서 SR이 **어느 보호자 동작인지 식별 불가**하던 갭을 보호자명 포함 `aria-label`(예: `홍보호 초대 재발송`)로 해소(27차 체크리스트 의도가 실측 baseline에 미반영이던 것을 반영). 동작 묶음 `aria-busy` 처리. `NavLink`(AppShell SideNav)는 활성 시 react-router 기본 `aria-current="page"` 노출 확인(색만 의존 아님). `GuardianInvitationList.test.jsx` 행 동작 라벨 회귀 +1.
> **30차 (2026-06-07)**: 스켈레톤 재이관(29차) 위 **폼 입력·토글·연락처 마스킹 컴포넌트 보강** — `Switch`(WAI-ARIA `role="switch"`·켜짐/꺼짐 텍스트 병행·44px·CSS 토큰 재사용, US-I03·§3-3), `DateInput`(US-D01 생년월일/인정유효일·US-L01 입금일·§3-1 기간 필터 — raw `<input type=date>` 차단), `MonthInput`(US-E05 통계·US-G02/G04/G07 청구·NHIS 대상월 — raw `<input type=month>` 차단), `MaskedPhone`(US-K01·L02 — `010-****-5678` 부분 마스킹 + `tel:` 링크 + `aria-label` 다이얼 안내). `DashboardPage` 미정의 `ds-stack*` 클래스 제거 → `.ds-app/.ds-topbar/.ds-main`+skip link 적용으로 키보드/SR 진입 흐름 수정. `ForbiddenPage` `.ds-auth-page`+`Card`로 LoginPage와 일관된 미인증 레이아웃.
> **5차 현행화 (2026-06-06)**: 구현 완료 항목을 `[x]`로 갱신.
> **6차 (2026-06-06)**: v1.2 P0 화면·컴포넌트 추가 — SideNav 2단 그룹, 등급 타임라인, 대시보드 위젯, 연락처 마스킹.
> **7차 (2026-06-06)**: USER_STORIES·FLOWCHART 대비 누락 보강 — `/billing/:id` 상세, 결석 사유 모달(US-E01), 이용자 사진+alt(US-D01), 보호자 초대 모달(US-J01), 청구 상태 이력 타임라인(US-G07), SideNav NHIS import, ClientPicker 키보드 탐색.
> **8차 (2026-06-06)**: FLOWCHART §5·§7·§9 갭 — `CheckoutModal`(US-E01 교통편), `DiscrepancyComparePanel`(US-G06), `GuardianBillingDetailModal`(US-J02), `ClientSelector`(복수 이용자 radiogroup), `CopayTypeSelect`(US-D01), `QrScanPanel`(US-E04), `branch_admin` SideNav 수기 체크인.
> **9차 (2026-06-06)**: USER_STORIES 잔여 갭 — `MedicationDuplicateAlert`(US-F02), `HealthAbnormalBanner`(US-F01), `SessionTimeoutProvider`(US-B03), 페이지 통합(GuardianPage·GuardianCheckinPage·AttendancePage·ReconciliationPage·HealthPage), `ToastProvider`/`SessionTimeoutProvider` 앱 루트 배선.
> **11차 (2026-06-06)**: **다크 모드** — `tokens.css` `[data-theme="dark"]` 토큰, `ThemeToggle`(AppShell topbar), `theme.js`. 다크 대비 AA 검증(§2-4).
> **12차 (2026-06-06)**: **로그인 진입 화면**(US-B01) 스타일 정비 — `LoginPage`가 참조하던 미정의 `.ds-label`로 라벨이 무스타일이던 문제를 `Field`/`TextInput`/`Button`(block·lg) 전환으로 해소, `.ds-login` 카드 레이아웃·브랜드 모노그램. **Modal 포커스 트랩**(Tab/Shift+Tab 순환). **고대비/강제 색상 모드**(`forced-colors`·`prefers-contrast: more`) — 배경 틴트 제거 시 경계선·시스템 강조색으로 식별성 보장.
> **13차 (2026-06-06)**: **전사 설정 토글 누락 보강**(US-I03·REQUIREMENTS §3-3·FLOWCHART §2) — `SettingsPage` 「조직 설정」의 `allow_client_self_checkin`이 정적 `<dl>` 설명 + `TODO`뿐이어서 조작 컨트롤이 없던 갭을 WAI-ARIA `switch` 패턴 `Switch` 컴포넌트로 해소. 켜짐/꺼짐 **텍스트 라벨 병행**(색·노브 위치만 의존 금지), 네이티브 `<button>` Enter/Space 토글, 44px 트랙, `forced-colors`에서 경계선+`Highlight` 채움으로 식별성.
> **16차 (2026-06-07)**: USER_STORIES·FLOWCHART 잔여 — `BatchProgressSteps`(US-G04), `PlatformOrgDetailModal`(US-A02), `PlatformPage` SearchInput·관리 모달, `ForbiddenPage` `ds-link`, 차트·진행단계 `forced-colors`.
> **17차 (2026-06-07)**: FLOWCHART §2·US-A02/I03/G07 — `AuditLogPanel`(sysadmin 감사 로그)·`BackupSettingsPanel`(백업 정책)·`PasswordChangeModal`(최초 로그인 필수 변경)·`FilterChips` 상태 카운트 배지·`LoginPage` 재설정 링크 스텁·`BillingPage`/`GuardianPage` raw `role=alert` → `Alert`·`Modal` `closeOnOverlay`/`closeOnEscape`/`showCloseButton`.
> **18차 (2026-06-07)**: REQUIREMENTS §3-1 잔여 — `LoginHistoryPanel`(sysadmin 로그인 이력 탭)·`PasswordResetRequestModal`(로그인 재설정 요청 UI)·Must 페이지 13곳 inline `role=alert` → `Alert tone=danger`+`.ds-page-alert` 통일(고대비 배경·경계선)·`GuardianCheckinPage` 피드백 `Alert tone=success|danger`·`PlatformOrgDetailModal.test.jsx` 회귀.
> **19차 (2026-06-07)**: `SettingsPage` security 탭 통합·`.ds-security-panel`·`token` useAuth 버그 수정.
> **20차 (2026-06-07)**: USER_STORIES·FLOWCHART 잔여 — `BillingStatusConfirmModal`·`NhisImportGuidePanel`·`CopayRateTable`·`GuardianDailySummary`·`HealthAlertList`·Must 페이지 `ds-page-alert` 잔여 5곳 통일.
> **21차 (2026-06-07)**: USER_STORIES·FLOWCHART 잔여 — `FeeScheduleTable`(US-G00a raw input 제거)·`BillingDetailPage` `BillingStatusConfirmModal` 연동(US-G07)·`StatCard tone=danger`(US-L02)·`.ds-text-secondary`·`.ds-mono`·`.ds-diff-amount`·`.ds-table-actions` 유틸·`HealthDetailPage`·`QrGeneratePage`·`ClientDetailPage` 탭·`ForbiddenPage` 접근성·Alert 통일.
> **22차 (2026-06-07)**: USER_STORIES·FLOWCHART 잔여 — `MonthInput`(US-E05·G04 raw month input 제거)·`PaymentRecordModal`(US-L01 PaymentPage 모달 추출)·`ReconciliationSummaryBar`(US-G06 `role=group`+sr-only 건수)·`ClientListPage` `SearchInput`·`NHISImportPage`/`AttendanceStatsPage`/`ReconciliationPage` 인라인 style→유틸 클래스·`.ds-page-alert` NHIS 업로드 오류.
> **23차 (2026-06-07)**: 인라인 style→유틸 클래스 잔여 정리 — Must 화면 `ClientDetailPage`(US-D03 탭·US-D04 주민번호 마스킹·US-M01 등급 이력)의 inline `style={{}}` 16건을 전량 제거하고 `.ds-inline-actions`(버튼·뱃지 중앙 정렬)·`.ds-client-summary*`(요약 헤더)·`.ds-dl-grid`(기본정보 정의 목록)·`.ds-section-gap`·`.ds-table-empty`로 승격. `ClientFormPage` 폼 하단 액션 `.ds-form-actions--end`(우측 정렬)·`PlatformPage` 사업자번호 `.ds-mono`·`GuardiansPage` 미지정 표시 `.ds-text-muted`. 토큰 기반이라 시각 동작 동일하나 다크/`forced-colors`에서 일관 적용 보장. `npm run build`·`npm test` 185/33 PASS(회귀 없음).
> **25차 (2026-06-08)**: USER_STORIES·FLOWCHART 잔여 — `BillingPage` raw month input → `MonthInput`(US-G02/G07)·`ChartContainer` `axisTextColor` prop + `.ds-chart__legend-label`(HealthTrendChart·BranchCompareChart 인라인 style 제거)·`PaymentPage` `.ds-section-gap`/`.ds-table-actions`·`GuardianDetailPage` 빈 상태 `EmptyState`(US-K02)·`LogoutButton` `aria-label` 회귀 테스트·`styles.css` 데모 `.role-link`/`.demo-grid` 제거·`.ds-input--month` → `.ds-month-input` 통합. `BillingPage.layout.test.jsx`·`LogoutButton.test.jsx`·`ChartContainer.test.jsx` axisTextColor 회귀.
> **26차 (2026-06-08)**: USER_STORIES·FLOWCHART **US-J01(FE-17) 잔여** — `GuardianInvitationAcceptPage`가 AppShell+SideNav를 사용하던 패턴을 **`PublicAuthLayout`**(LoginPage `.ds-login` 카드·skip link·브랜드) + **`GuardianInvitationAcceptForm`**(Field 라벨·`autoComplete` name/email/new-password·비밀번호/확인 구분·수락 완료 시 입력 잠금+「로그인하기」CTA)로 분리. **`INVITATION_STATUS`** Badge 상수(PENDING/SENT/ACCEPTED/EXPIRED/REVOKED). `.ds-auth-page*` CSS. `PublicAuthLayout.test.jsx`·`GuardianInvitationAcceptForm.test.jsx` 회귀.
> **27차 (2026-06-08)**: USER_STORIES·FLOWCHART **US-J01 초대 이력·§3-1 기간 필터** — **`DateInput`**(`MonthInput` 패턴, `AuditLogPanel`·`LoginHistoryPanel` raw `type=date` 제거)·**`GuardianInvitationList`**(`INVITATION_STATUS`+표 `caption`+재발송/취소 `aria-label`+`MaskedPhone`)·`GuardianListCard` 초대 이력 섹션·`ClientDetailPage` `guardianInvitations[]` 연동·`GuardianInvitationAcceptPage` 404/410 만료 시 `disabled` 폼 잠금·`ClientPhotoField` alt→`TextInput`·`GuardianInviteModal` `autoComplete`.
> **28차 (2026-06-08)**: USER_STORIES·FLOWCHART **DateInput·J01 접근성 잔여** — `ClientFormPage`(US-D01) 생년월일·인정 유효 시작일 raw `type=date` → **`DateInput`**·`PaymentRecordModal`(US-L01) 입금일 → **`DateInput`**·`ClientPhotoField` 사진 선택/변경/삭제 **`aria-label`**·`GuardianInviteModal` 발송 중 **`aria-busy`**·`ClientDetailPage` 초대 피드백 Alert **`ds-page-alert`** 통일. Must 화면 `type=date` raw input **0건**(DateInput·MonthInput만 허용).
> **24차 (2026-06-08)**: Must 페이지·모달 인라인 style 잔여 — `AttendancePage`(US-E01/E02 `.ds-page-lede`·`.ds-grid--gap-bottom`·`.ds-table-actions`)·`DashboardPage`(US-H01 `.ds-section-gap--lg`·`.ds-card-link`)·`GuardianPage`(US-J02 `.ds-card--mb`·`.ds-tab-panel-body`·`.ds-table-empty`)·`HealthPage`(US-F01~F03 `.ds-section-gap`)·`QrGeneratePage`(US-E03 `.ds-form-row__action`·`.ds-section-gap--bottom`)·`OverduePage`(US-L02 `.ds-page-footnote`+`.ds-link`)·`GuardianCheckinPage`(US-E04 `.ds-submit-block`)·모달 `CheckoutModal`/`AttendanceAbsentModal`/`SessionTimeoutModal`→`.ds-modal-intro`/`.ds-page-footnote`·`MedicationDuplicateAlert`/`HealthAbnormalBanner`→`.ds-alert-body*`·`PlatformOrgDetailModal`(US-A02 `.ds-mono`·`.ds-dl-grid--spaced`)·`BatchProgressSteps`/`FeeRateHistoryPanel` CSS 승격. `AttendancePage.layout.test.jsx` 회귀 추가.

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
- [x] Recharts 차트(15차, US-F04/H01/E05/H02): `ChartContainer` — `role="figure"`+`figcaption`+`aria-describedby` sr-only 데이터 요약, 빈 데이터 `role="status"`. `HealthTrendChart` Legend 텍스트 라벨 병행(색만 의존 금지). `useChartColors` MutationObserver로 다크 전환 실시간 반영.
- [x] 수가표 1밴드 안내(15차, UXD-4): `FeeSchedulePage` Alert·Card actions에 「표준 이용시간 8~10h · 1밴드 고정」help 텍스트.
- [x] 인라인 링크(15차): `.ds-link` — `DashboardPage` `role-link` → `ds-link` 전환, `forced-colors` LinkText.
- [x] NHIS 배치 진행(16차, US-G04): `BatchProgressSteps` — `nav`+`aria-label`+`sr-only` 현재 단계 안내, 단계별 텍스트 라벨 병행, `FAILED` 시 처리중 단계 실패 표시.
- [x] 플랫폼 고객사(16차, US-A01/A02): `PlatformPage` `SearchInput` 라벨 연결, Tenant 상태 `StatusBadge`+`BRANCH_STATUS`, 「관리」`aria-label`, `PlatformOrgDetailModal` 관리자 발급 `Field`+`Alert`.
- [x] 403 페이지(16차): `ForbiddenPage` 로그인 링크 `ds-link` 통일.
- [x] 보호자 초대(16차): `GuardianListCard` 「초대 발송」`aria-label` 명시.
- [x] 차트·진행단계 고대비(16차): `forced-colors` 시 `.ds-chart__viewport`·`.ds-progress-steps__dot` 경계선 보강.
- [x] 감사 로그(17차, US-I03): `AuditLogPanel` — `Field` 라벨·이벤트 `Badge` 텍스트 라벨·표 `caption`·PII `ds-masked`·로딩 `Spinner` `aria-label`.
- [x] 백업 설정(17차, US-I03): `BackupSettingsPanel` — `Switch` 자동 백업·상태 `Badge` 텍스트·수동 백업 `Button` `aria-busy`.
- [x] 최초 비밀번호 변경(17차, US-A02): `PasswordChangeModal` — 필수 모드 ESC/오버레이/✕ 차단·`Alert` 보안 안내·`Field`+`autoComplete=new-password`.
- [x] 청구 상태 카운트(17차, US-G07): `FilterChips` `counts` prop — 숫자 배지 + `aria-label` 「N건」 병행(색만 의존 금지).
- [x] 페이지 오류 표시(17차): `BillingPage`·`GuardianPage` inline `role=alert` → `Alert tone=danger` 통일.
- [x] 테이블 내 링크(17차): `BillingPage` 이용자명 `button.ds-link`(키보드·포커스 링 일관).
- [x] 로그인 이력(18차, §3-1): `LoginHistoryPanel` — `Field` 필터·표 `caption`·이메일/IP `ds-masked`·결과 `Badge` 텍스트 라벨·`SettingsPage` 「로그인 이력」탭.
- [x] 비밀번호 재설정(18차, §3-1): `PasswordResetRequestModal` — `Field`+`autoComplete=username`·요청 완료 `Alert tone=success`·`LoginPage` `button.ds-link` 진입.
- [x] 페이지 오류 표시(18차): Must 페이지 API 오류 — inline `<p role=alert>` 금지, `Alert tone=danger`+`.ds-page-alert` 통일(`forced-colors` 배경·테두리 포함). 대상: ClientList/Detail, Attendance/Stats, Health, Branches, Guardians/Detail, BillingDetail, Payment, Overdue, Reconciliation matchError, GuardianCheckin 피드백.
- [x] 보안 탭 통합(19차, §3-1): `SettingsPage` security 탭 — `PasswordChangeModal`(비밀번호 변경)·`PasswordResetRequestModal`(재설정 요청)을 LoginPage 진입 외 SettingsPage에서도 독립 접근 가능. `.ds-security-panel`(flex 컨테이너) 내 `Alert tone=info` 안내 + `ds-action-bar__actions` 버튼 그룹. sysadmin·hq_admin·platform_admin 역할만 노출, 외 역할은 `Alert tone=info` 권한 안내.
- [x] `token` 세션 버그(19차): `SettingsPage.jsx` `handlePasswordChange` 내 `token` 참조 — `useAuth()` 구조분해에 `token` 누락 → 수정 완료(`const { user, token } = useAuth()`). REQUIREMENTS §3-1 세션 만료 감지.
- [x] 청구 상태 전이 확인(20차, US-G07): `BillingStatusConfirmModal` — 확정(CONFIRMED) 시 「수정 불가」`Alert tone=warning`, `StatusBadge`+금액 요약 `dl`, `BillingPage` 목록 액션 전 확인 모달. `BILLING_STATUS_TRANSITIONS` 상수 export.
- [x] NHIS import 온보딩(20차, US-G04): `NhisImportGuidePanel` — Chrome/Edge `Alert`, 4단계 `ol`+`sr-only` 단계 번호, `처리상태` 선행열 안내, `NHISImportPage` 인라인 중복 제거.
- [x] 본인부담 비율표(20차, US-G00b): `CopayRateTable` — `TextInput type=number`+`aria-label`, `COPAY_TYPES` 기본값·변경 `sr-only` 안내, `CopayRatePage` raw `<input>` 제거.
- [x] 보호자 포털 요약(20차, US-I02): `GuardianDailySummary` — `ATTENDANCE_STATUS` 라벨 StatCard, `HealthAlertList` 연동, `GuardianPage` `EmptyState` 빈 연결 이용자.
- [x] 건강 이상 목록 공통(20차): `HealthAlertList` — `Badge tone=warning` 「주의」텍스트+색 병행, `DashboardPage`·`GuardianDailySummary` 재사용.
- [x] 페이지 오류 Alert 잔여(20차): `PlatformPage`·`BillingPage`·`DashboardPage`·`GuardianPage`·`CopayRatePage` → `Alert`+`.ds-page-alert` 패턴 통일.
- [x] 수가표 편집(21차, US-G00a): `FeeScheduleTable` — `TextInput`+`aria-label`+`caption`, `FeeSchedulePage` raw `<input>` 제거.
- [x] 청구 상세 상태 전이(21차, US-G07): `BillingDetailPage` topbar 「확정」/「수납완료」→ `BillingStatusConfirmModal` — 목록과 동일 패턴.
- [x] 미납 지표(21차, US-L02): `OverduePage` 인라인 danger 색상 → `StatCard tone=danger`+`.ds-stat__value--danger`(텍스트 라벨 병행).
- [x] NHIS reconciliation 차이(21차, US-G06): `ReconciliationPage` 차이 금액 `.ds-diff-amount`+`sr-only` 「차이」+`aria-label`, 인정번호 `.ds-mono`.
- [x] 페이지 오류 Alert 잔여(21차): `HealthDetailPage`·`QrGeneratePage`·`ClientDetailPage` 건강/출석 탭 → `Alert tone=danger`+`.ds-page-alert`.
- [x] 403 페이지(21차): `ForbiddenPage` 인라인 style → `.ds-forbidden-page__desc`·`__actions`+`.ds-link`.
- [x] 대상 월 입력(22차, US-E05·G04): `MonthInput` — `Field`+`TextInput type=month`+`.ds-month-input`, raw `<input class=ds-input>` 금지. `AttendanceStatsPage`·`NHISImportPage`.
- [x] 입금 기록(22차, US-L01): `PaymentRecordModal` — `Field` 라벨·`aria-invalid`·수단 `Select`·`.ds-modal-intro` 요약. `PaymentPage` 목록 「입금 기록」`aria-label`.
- [x] NHIS reconciliation 요약(22차, US-G06): `ReconciliationSummaryBar` — `role=group`·Badge 숫자+`sr-only` 「N건」·`.ds-summary-bar`. `ReconciliationPage`.
- [x] 이용자 검색(22차, US-D02): `ClientListPage` raw search → `SearchInput hideLabel` (`htmlFor`·`type=search`).
- [x] 인라인 style 잔여 제거(23차, US-D03/D04/M01): `ClientDetailPage` inline `style={{}}` 16건 → `.ds-inline-actions`·`.ds-client-summary*`·`.ds-dl-grid`·`.ds-section-gap`·`.ds-table-empty`. `ClientFormPage` `.ds-form-actions--end`·`PlatformPage` `.ds-mono`·`GuardiansPage` `.ds-text-muted`. 토큰 기반이라 `forced-colors`·다크에서 일관 적용.
- [x] 청구 목록 월 필터(25차, US-G02/G07): `BillingPage` `MonthInput`+`Field` — raw `ds-input--month` 제거.
- [x] 차트 범례 텍스트(25차): `ChartContainer` `axisTextColor` → `--chart-axis-text` CSS 변수, `.ds-chart__legend-label` — 다크/`forced-colors` 일관.
- [x] 입금 처리(25차, US-L01): `PaymentPage` 안내 `Alert` `.ds-section-gap`, 표 액션 `.ds-table-actions`.
- [x] 보호자 상세 빈 상태(25차, US-K02): `GuardianDetailPage` API 미응답 시 `EmptyState`+`ds-page-alert` — raw `role=status` 문단 제거.
- [x] 로그아웃 버튼(25차, US-B03): `LogoutButton` AppShell topbar — `aria-label="{이름} 로그아웃"`, 미인증 시 null 렌더.
- [x] 보호자 초대 수락(26차, US-J01): `PublicAuthLayout`+`GuardianInvitationAcceptForm` — 미인증 공개 화면은 **AppShell/SideNav 금지**, LoginPage와 동일 `.ds-login` 카드·skip link, Field+`autoComplete`, 비밀번호/확인 라벨 분리, 수락 완료 `Alert tone=success`+입력 `disabled`+「로그인하기」CTA, 만료 `Alert tone=danger`.
- [x] 보호자 초대 상태(26차, US-J01): `INVITATION_STATUS` — `StatusBadge` 텍스트+색(PENDING/SENT/ACCEPTED/EXPIRED/REVOKED).
- [x] 기간 필터 DateInput(27차, §3-1): `AuditLogPanel`·`LoginHistoryPanel` — raw `type=date`+`ds-input` → `DateInput`+`Field` 라벨 연결, `.ds-date-input` max-width.
- [x] 보호자 초대 이력(27차, US-J01): `GuardianInvitationList` — 표 `caption`·`scope`·`INVITATION_STATUS` Badge·`MaskedPhone`·재발송/취소 `Button` `aria-label`·`GuardianListCard` 「초대 이력」섹션.
- [x] 만료 초대 수락(27차, US-J01): `GuardianInvitationAcceptPage` API 404/410 → `GuardianInvitationAcceptForm disabled` 입력 잠금.
- [x] alt·사진 설명(27차, US-D01): `ClientPhotoField` alt 입력 raw `<input>` → `TextInput`+`Field`.
- [x] DateInput 표준화(28차, US-D01·US-L01): `ClientFormPage` 생년월일·인정 유효 시작일·`PaymentRecordModal` 입금일 — raw `TextInput type=date` → `DateInput`+`Field`. 신규 `type=date`는 **DateInput만** 사용(MonthInput과 대칭).
- [x] 사진 업로드 버튼(28차, US-D01): `ClientPhotoField` — 선택/변경/삭제 `Button`에 `aria-label`+`aria-controls`(숨김 file input id) 연결.
- [x] 보호자 초대 발송(28차, US-J01): `GuardianInviteModal` — 발송 중 `Button` `aria-busy`. `ClientDetailPage` 초대 성공/오류 `Alert`+`.ds-page-alert`.
- [x] Must 페이지 인라인 style 잔여(24차, US-E01~E04/H01/F01~F03/J02/L02/A02): `AttendancePage` `.ds-page-lede`·`.ds-grid--gap-bottom`·`.ds-table-actions`·`DashboardPage` `.ds-section-gap--lg`·`.ds-card-link`·`GuardianPage` `.ds-card--mb`·`.ds-tab-panel-body`·`.ds-table-empty`·`HealthPage` `.ds-section-gap`·`QrGeneratePage` `.ds-form-row__action`·`OverduePage` `.ds-page-footnote`·`GuardianCheckinPage` `.ds-submit-block`·모달 `.ds-modal-intro`/`.ds-alert-body*`. `AttendancePage.layout.test.jsx` 회귀.
- [ ] 키보드만으로 로그인→대시보드→이용자 등록 핵심 흐름 완주 가능 — **tester E2E 검증 필요** (중복 항목 — 구현 완료 후 tester 검증 대기).
- [x] Switch(30차, US-I03·§3-3): `Switch` 컴포넌트 재도입 — `role="switch"` + `aria-checked`, 라벨 `aria-labelledby`·설명 `aria-describedby` 연결, 켜짐/꺼짐 **텍스트 병행**(색·노브 위치만 의존 금지), `<button type=button>` 네이티브 키보드 토글, 44px 트랙 hit target, `forced-colors`에서 트랙 경계선+`Highlight` 채움(§9 CSS). `onChange(next)`가 다음 boolean 값을 인자로 받음(이벤트 객체 아님).
- [x] DateInput(30차, US-D01·US-L01·§3-1): `DateInput` 컴포넌트 재도입 — `Field` 안 `TextInput type=date` 래퍼 + `.ds-date-input` max-width. raw `<input type=date class=ds-input>` **금지**.
- [x] MonthInput(30차, US-E05·G02/G04/G07): `MonthInput` 컴포넌트 재도입 — `Field` 안 `TextInput type=month` 래퍼 + `.ds-month-input` max-width. raw `<input type=month>` **금지**.
- [x] MaskedPhone(30차, US-K01·L02): `MaskedPhone` 컴포넌트 — 가운데 그룹 마스킹(`010-****-5678`, 10자리·11자리·기타 포맷 허용)·`<a href="tel:">` 링크·`aria-label`로 SR 다이얼 안내. **PII 보호**: 시각 UI는 항상 마스킹 유지, `withLink=false`이면 `<span>` 정적 표시.
- [x] DashboardPage 골격(30차): 존재하지 않는 `.ds-stack*`/`.ds-gap-sm` 잔재 제거 → `.ds-app`+`.ds-topbar`(`ThemeToggle`+`로그아웃` `aria-label`)+`.ds-main`+skip link로 AppShell 패턴 확립. `<dl class=ds-dl-grid>`로 역할/세션/다음 단계 요약(색만 의존 금지).
- [x] ForbiddenPage(30차): `.ds-auth-page`+`Card` 사용으로 LoginPage와 동일한 미인증 카드 레이아웃, `aria-labelledby` 연결, 「로그인으로 이동」 primary 버튼.
- [x] 초대 이력 행 동작 라벨(31차, US-J01): `GuardianInvitationList` 표 「재발송」/「취소」`Button` — 보호자명 포함 `aria-label`(`{이름} 초대 재발송|취소`)로 다중 행에서 SR 동작 대상 식별, `ds-table-actions` `aria-busy={pending}`. 시각 버튼 텍스트는 「재발송」/「취소」 유지(공간 절약), 접근성 이름만 컨텍스트 보강. `GuardianInvitationList.test.jsx` 회귀.
- [x] SideNav 활성 표시(31차): `AppShell`의 react-router `NavLink`가 활성 시 `aria-current="page"`를 기본 출력 — 활성 메뉴를 색(`.ds-nav-item--active`) 외 SR/접근성 트리에도 노출(색만 의존 금지 원칙 충족).
- [x] Alert 라이브 리전 정중도(32차): `Alert` 기본 `role`을 tone 기준 분기 — `danger`/`warning`→`role="alert"`(assertive), `info`/`success`/`neutral`→`role="status"`(polite). 정적 안내가 스크린리더 흐름을 끊지 않도록 함. `role` prop 명시 시 그대로 우선. `Alert.test.jsx` 회귀.
- [x] 공개 인증 화면 헤딩 계층(32차, US-J01): `GuardianInvitationAcceptPage`를 `PublicAuthLayout`로 전환 — 페이지 단일 `<h1>`(화면 제목)·skip link(`#public-auth-content`)·브랜드 모노그램(LoginPage 일관). 기존 `Card`(`<h2>`)만 있던 헤딩 결함 해소. `PublicAuthLayout.test.jsx` 회귀.
- [x] 2단 SideNav(33차, US-UX-02): `SideNav`+`navConfig.js` — 운영·출석·기록·청구 4그룹, `aria-expanded`/`aria-controls` 모바일 토글, `NavLink` `aria-current="page"`, `EXACT_MATCH_PATHS` prefix 활성 충돌 방지. `SideNav.test.jsx` 회귀.
- [x] 목록·필터·페이지네이션(33차, US-D02/G07): `SearchInput`(`type=search`+`aria-label`)·`FilterChips`(`role=radiogroup`+counts `aria-label`)·`Pagination`(`nav`+`aria-current=page`+이전/다음 `aria-label`). `FilterChips.test.jsx`·`Pagination` 회귀는 Tabs/BranchSwitcher/LogoutButton 일괄.
- [x] 이용자 상세 탭 골격(33차, US-D03): `Tabs`/`TabPanel` — `role=tablist/tab/tabpanel`, `aria-selected`, Arrow/Home/End 키. `Tabs.test.jsx` 회귀.
- [x] 지점 선택기(33차, US-B02): `BranchSwitcher` — 2지점 이상 시만 노출, `Field`+`Select`, `aria-label=작업 지점 선택`. API `PATCH /auth/active-branch` 연동은 coder.
- [x] 로그아웃 접근성(33차, US-B03): `LogoutButton` — `aria-label="{이름} 로그아웃"`, 미인증 null. `AppShell` topbar 기본 탑재.
- [x] 로그인 PublicAuthLayout(33차, US-B01): `LoginPage` → `PublicAuthLayout` — 공개 인증 화면 단일 h1·skip·브랜드 일관.
- [x] 목록 CSS 갭(33차): `.ds-list`/`.ds-list__item`/`.ds-breadcrumb`/`.ds-form-grid` — Must 페이지 참조 클래스 `components.css` 정의.
- [x] 이용자 상세 탭(34차, US-D03): `ClientDetailPage` — `Tabs`/`TabPanel` 기본·건강·출석·청구, breadcrumb·요약 헤더.
- [x] 주민번호 열람(34차, US-D04): `MaskedRevealField` — 마스킹·`aria-label`·열람 버튼 `aria-label="주민번호 열람 (audit 기록됨)"`.
- [x] 보호자 초대 모달(34차, US-J01): `GuardianInviteModal` — `Modal`+`Field`+`aria-busy`, `ClientDetailPage`에서 사용.
- [x] 이용자 검색·페이지네이션(34차, US-D02): `ClientListPage` — `SearchInput hideLabel`+클라이언트 `Pagination`.
- [x] 대시보드 위젯(34차, US-M02): `DashboardWidgetGrid` — `StatCard` 5블록·링크 `sr-only`·로딩 `role=status`.
- [x] 청구 상태 필터(34차, US-G07): `BillingPage` — `FilterChips` counts+`MonthInput`.
- [x] NHIS import(34차, US-G04): `NhisImportGuidePanel` 4단계+Chrome/Edge 안내·`FileUpload` role=button+키보드.
- [x] 건강 비정상(34차, US-F01): `HealthAbnormalBanner` — `Badge` 「주의」+`role=alert`+항목 목록.
- [x] 세션 만료(34차, US-B03): `SessionTimeoutProvider` 30분 idle+60초 `SessionTimeoutModal`, `App.jsx` 배선.
- [x] Switch 회귀(34차, US-I03): `Switch.test.jsx` 5건 — ARIA·키보드·disabled·description.
- [x] 페이지 오류 Alert(34차): Must 페이지 redundant `role=alert` 제거 → `Alert tone=danger`+`.ds-page-alert` (tone 기본 role 사용).
- [x] 건강 알림 목록(35차, US-M02): `HealthAlertList` — Badge 「주의」+이름+사유, `aria-label` list. `DashboardPage` 연동.
- [x] 보호자 목록 카드(35차, US-D01/K01): `GuardianListCard` — `MaskedPhone`·대표 Badge·초대 `aria-label`. `ClientDetailPage` 연동.
- [x] 등급 이력(35차, US-M01): `GradeHistoryTimeline` — `<ol aria-label>`+sr-only 등급 변경. `ClientDetailPage` 「등급 이력」탭.
- [x] NHIS 배치 진행(35차, US-G04): `BatchProgressSteps` — `nav`+sr-only 단계·FAILED 표시. `NHISImportPage` 배치 행.
- [x] 본인부담 구분(35차, US-D01): `CopayTypeSelect` — 4구분+비율 help·`Field` 라벨. `COPAY_TYPES` export.
- [x] SideNav v1.2 메뉴(35차, US-UX-02): `navConfig` — 지점·보호자·수기 체크인·출석 통계·QR·입금·미납·수가표·copay 하위 route.
- [x] Card 섹션 제목(35차): `Card` `titleId` prop → `h2#id` for `aria-labelledby` 연결.

---

## 7. UI 컴포넌트 가이드 (coder 구현 메모) [UXD]

import: `import { Button, Card, Field, Modal, Pagination } from "../components/ui";`

### 7-1. 기존 컴포넌트

> **34차 baseline 현황 (2026-06-07)**: `components/ui/` **40종** — 34차 35종 + 35차 `HealthAlertList`·`GuardianListCard`·`GradeHistoryTimeline`·`BatchProgressSteps`·`CopayTypeSelect`. SideNav `navConfig.js` v1.2 P0 메뉴(지점·보호자·입금·미납·수가표 등) 반영. `npm test` **78/27 PASS**·build **99 modules**.
> **34차 baseline 현황 (2026-06-07)**: `components/ui/` **35종** — 33차 27종 + 34차 `SessionTimeoutModal`·`SessionTimeoutProvider`·`MaskedRevealField`·`GuardianInviteModal`·`FileUpload`·`NhisImportGuidePanel`·`HealthAbnormalBanner`·`DashboardWidgetGrid`. Must 페이지(`ClientDetailPage`·`ClientListPage`·`DashboardPage`·`BillingPage`·`NHISImportPage`·`HealthPage`) DS 컴포넌트 연동 완료.
> **33차 baseline 현황 (2026-06-07)**: `components/ui/` **27종** — 32차 18종 + 33차 `StatCard`·`SearchInput`·`FilterChips`·`Pagination`·`Table`·`Tabs`·`TabPanel`·`BranchSwitcher`·`LogoutButton`. 레이아웃: `layout/AppShell.jsx`(SideNav·BranchSwitcher·LogoutButton 통합)·`layout/SideNav.jsx`(US-UX-02 2단)·`layout/navConfig.js`. 아래 표 ⏳ COD 항목 중 도메인 특화(차트·모달·NHIS 등)는 coder가 페이지 연동 시 재사용.

| 컴포넌트 | 주요 props | 용도 / 화면 | baseline |
|----------|-----------|------------|---------|
| `Button` | `variant(primary/secondary/danger/ghost)`, `size(sm/md/lg)`, `block` | 전 화면 액션 | ✅ 29차 |
| `Field` | `label`, `required`, `help`, `error`, `children(render prop)` | 폼 라벨·오류 접근성 래퍼 (이용자 등록 §US-D01) | ✅ 29차 |
| `TextInput`/`Textarea`/`Select` | 네이티브 props 패스스루 | Field 안에서 사용 | ✅ 29차 |
| `Checkbox` | `label`, `checked`, `onChange` | **주민번호 수집 동의**(US-D04) 등 | ✅ 29차 |
| `Card` / `StatCard` | `title`,`actions` / `label`,`value`,`unit`,`tone?` | 카드 · 대시보드 지표(US-H01) | Card ✅ 29차 / StatCard ✅ 33차 |
| `Badge` / `StatusBadge` | `tone` / `status`,`map` | 청구·매칭·출석 상태 (`BILLING_STATUS`·`MATCH_STATUS`·`ATTENDANCE_STATUS`·`BATCH_STATUS`·`INVITATION_STATUS`) | ✅ 29차 |
| `Alert` | `tone`, `title` | 안내·경고(예: 롱텀 Chrome/Edge 안내 US-G04) | ✅ 29차 |
| `Modal` | `isOpen`,`onClose`,`title`,`size`,`footer`,`closeOnOverlay/Escape`,`showCloseButton` | 다이얼로그 — `useId()` 인스턴스별 고유 `aria-labelledby`, 포커스 트랩, ESC | ✅ 29차 |
| `Spinner` / `EmptyState` | — | 로딩·빈 목록 | ✅ 29차 |
| `ThemeToggle` | `className?` | 라이트/다크 전환 (다크모드 §2-4) | ✅ 29차 |
| `Tabs` / `TabPanel` | `tabs`,`activeId`,`onChange` | 이용자 상세 탭(기본/건강/출석/청구 US-D03) | ✅ 33차 |
| `Table` | `caption`, children + 행 강조 `ds-row--warning/danger` | 청구 목록·NHIS reconciliation 행(US-G06) | ✅ 33차 |
| `BranchSwitcher` | `branches`,`value`,`onChange` | 지점 전환(US-B02, `active_branch_id`) | ✅ 33차 |
| `SearchInput` | `value`,`onChange`,`label`,`hideLabel` | 이용자 목록 검색 (US-D02) | ✅ 33차 |
| `FilterChips` | `options`,`value`,`onChange`,`counts` | 청구 상태 필터 (US-G07) | ✅ 33차 |
| `Pagination` | `page`,`totalPages`,`onChange` | 목록 페이지 이동 | ✅ 33차 |
| `LogoutButton` | (없음 — `useAuth` 내부) | topbar 로그아웃 (US-B03) | ✅ 33차 |
| `AppShell` | `title`,`branches?`,`activeBranchId?`,`onBranchChange?` | 로그인 이후 공통 레이아웃 + SideNav + skip link | ✅ 33차 (`layout/AppShell.jsx`) |
| `SideNav` | `role` | 2단 그룹 네비 (US-UX-02) | ✅ 33차 (`layout/SideNav.jsx`) |

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

### 7-7h. 17차 보강 컴포넌트 (2026-06-07, Settings·비밀번호·상태 카운트)

| 컴포넌트 | 주요 props | 용도 / 화면 |
|----------|-----------|------------|
| `AuditLogPanel` | `entries[]`, `loading`, `eventFilter`, `onEventFilterChange`, `dateFrom/To`, `page`, `totalPages` | sysadmin 감사 로그 (US-I03). `AUDIT_EVENT_TYPES` 상수 export |
| `BackupSettingsPanel` | `autoBackupEnabled`, `onAutoBackupChange`, `lastBackupAt`, `lastBackupStatus`, `retentionDays`, `onManualBackup` | Tenant 백업 설정 (US-I03). `SettingsPage` backup 탭 |
| `PasswordChangeModal` | `isOpen`, `required`, `onSubmit({ newPassword })`, `loading`, `error` | 최초 로그인·비밀번호 변경 (US-A02). `LoginPage` + `AuthContext.mustChangePassword` |

> **FilterChips counts (US-G07)**: `counts={{ __all__: 12, DRAFT: 3, ... }}` — API `statusCounts` 응답을 `BillingPage`에서 매핑. **Modal 필수 모드**: `closeOnOverlay={false}`·`closeOnEscape={false}`·`showCloseButton={false}` — `PasswordChangeModal required` 패턴.

### 7-7k. 21차 보강 컴포넌트 (2026-06-07, 수가표·청구 상세·StatCard·텍스트 유틸)

| 컴포넌트 | 주요 props | 용도 / 화면 |
|----------|-----------|------------|
| `FeeScheduleTable` | `rows[]`, `onRowChange(grade, field, value)`, `disabled?` | 등급별 1일 수가 편집 (US-G00a). `FeeSchedulePage` — `CopayRateTable`과 동일 접근성 패턴 |
| `StatCard` (확장) | `tone?: 'default' \| 'danger'` | 미납 총액 등 위험 지표 강조 (US-L02). 라벨 텍스트 병행 — 색만 의존 금지 |

> **BillingDetailPage 상태 전이 (21차)**: topbar 「확정」/「수납완료」→ `BillingStatusConfirmModal` → `PATCH /billing/claims/:id/status`. `BillingPage`와 동일 UX.

> **텍스트 유틸 (21차)**: `.ds-text-secondary`·`.ds-text-muted`·`.ds-mono`·`.ds-diff-amount`·`.ds-table-actions`·`.ds-section-gap`·`.ds-table-empty` — 인라인 `style={{ color }}` 금지, `forced-colors` 대응 포함.

### 7-7l. 22차 보강 컴포넌트 (2026-06-07, MonthInput·입금·reconciliation 요약)

| 컴포넌트 | 주요 props | 용도 / 화면 |
|----------|-----------|------------|
| `MonthInput` | native `type=month` props | 대상 월 선택 (US-E05·US-G04). `Field` 안에서 `TextInput` 래퍼 — `.ds-month-input` max-width |
| `PaymentRecordModal` | `isOpen`, `claim`, `form`, `onFormChange(patch)`, `onSubmit`, `error` | 본인부담 입금 기록 (US-L01). `PAYMENT_METHODS` export. `PaymentPage` |
| `ReconciliationSummaryBar` | `batchId`, `branchName`, `targetMonth`, `batchStatus`, `stats` | NHIS 배치 매칭 요약 (US-G06). Badge+sr-only 건수. `ReconciliationPage` |

> **MonthInput (22차)**: `AttendanceStatsPage`·`NHISImportPage`의 raw `<input type=month class=ds-input>` 제거. coder 신규 월 필터도 `MonthInput`+`Field` 패턴 준수.
>
> **PaymentRecordModal (22차)**: `PaymentPage` 인라인 Modal 폼 → 컴포넌트 추출. API: `POST /billing/claims/:id/payments { paidAt, amount, method }`.

### 7-7j. 20차 보강 컴포넌트 (2026-06-07, 청구 확인·NHIS 가이드·copay·보호자 요약)

| 컴포넌트 | 주요 props | 용도 / 화면 |
|----------|-----------|------------|
| `BillingStatusConfirmModal` | `isOpen`, `onClose`, `claim`, `nextStatus`, `onConfirm`, `loading`, `error` | 청구 상태 전이 확인 (US-G07). `BILLING_STATUS_TRANSITIONS` export. `BillingPage`·`BillingDetailPage`(후속) |
| `NhisImportGuidePanel` | `className?` | 공단 엑셀 import 4단계 온보딩 + Chrome/Edge 안내 (US-G04). `NHISImportPage` |
| `CopayRateTable` | `rates[]`, `onRateChange(code, rate)`, `disabled?` | 본인부담 구분별 비율 편집 (US-G00b). `CopayRatePage` |
| `HealthAlertList` | `items[]`, `emptyMessage?`, `ariaLabel?` | 건강 이상 알림 — Badge 「주의」+이름+사유 (US-F01/H01/I02). `DashboardPage`·`GuardianDailySummary` |
| `GuardianDailySummary` | `summary`, `clientName?` | 보호자 포털 오늘 출석·건강 지표 (US-I02). `GuardianPage` summary 탭 |

> **BillingPage 상태 전이 (20차)**: 목록 「확정」/「수납완료」 클릭 → `BillingStatusConfirmModal` → 확인 시 `PATCH /billing/claims/:id/status`. 즉시 PATCH 금지 — 되돌릴 수 없음(US-G07 V8) UX 보장.

### 7-7i. 18차 보강 컴포넌트 (2026-06-07, 인증·로그인 이력·오류 Alert 통일)

| 컴포넌트 | 주요 props | 용도 / 화면 |
|----------|-----------|------------|
| `LoginHistoryPanel` | `entries[]`, `loading`, `roleFilter`, `dateFrom/To`, `page`, `totalPages` | sysadmin 로그인 이력 (REQUIREMENTS §3-1). `LOGIN_RESULT_STATUS` export. `SettingsPage` login-history 탭 |
| `PasswordResetRequestModal` | `isOpen`, `onClose`, `onSubmit(email)`, `loading`, `error`, `submitted` | 비밀번호 재설정 요청 (§3-1). `LoginPage` 「재설정 요청」 |

> **페이지 오류 패턴 (18차)**: `{error && <Alert tone="danger" className="ds-page-alert">{error}</Alert>}`. raw `style={{ color: danger-text }}` + `<p role=alert>` **금지** — 고대비·다크에서 배경 틴트·경계선 일관.

### 7-7g. 16차 보강 컴포넌트 (2026-06-07, NHIS 배치 진행·플랫폼 고객사)

| 컴포넌트 | 주요 props | 용도 / 화면 |
|----------|-----------|------------|
| `BatchProgressSteps` | `status`(PENDING/PROCESSING/COMPLETED/FAILED), `ariaLabel?` | NHIS import 배치 처리 단계 (US-G04). `ReconciliationPage`·`NHISImportPage` |
| `PlatformOrgDetailModal` | `isOpen`,`onClose`,`org`,`onIssueAdmin(email)`,`issuing?`,`issueError?` | platform_admin 고객사 상세 + hq_admin 발급 (US-A02). `PlatformPage` |

### 7-7o. 27차 보강 컴포넌트 (2026-06-08, DateInput·초대 이력)

| 컴포넌트 | 주요 props | 용도 / 화면 |
|----------|-----------|------------|
| `DateInput` | native `type=date` props | 날짜 입력·기간 필터 (US-D01·US-L01·§3-1). `Field` 안 `TextInput` 래퍼 — `.ds-date-input`. `ClientFormPage`·`PaymentRecordModal`·`AuditLogPanel`·`LoginHistoryPanel` |
| `GuardianInvitationList` | `invitations[]`, `canManage`, `onResend`, `onRevoke`, `busyId` | 보호자 초대 이력·상태·재발송/취소 (US-J01). `GuardianListCard`·`ClientDetailPage` |

> **`GuardianListCard` 확장 (27차)**: `invitations` prop + 「초대 이력」하위 `GuardianInvitationList`. API: `GET /clients/:id` 응답 `guardianInvitations[]` — `{ id, guardianName, email?, phone?, status, expiresAt? }`. 재발송 `POST /guardian/invitations/{id}/resend`, 취소 `DELETE /guardian/invitations/{id}` (coder J01).
>
> **DateInput (27·28차)**: `MonthInput`과 동일 패턴. 신규 `type=date`는 **`DateInput`+`Field`만** 허용 — raw `<input class=ds-input type=date>` **금지**. 대상: 이용자 등록(생년월일·인정유효일)·입금일·감사/로그인 이력 기간 필터.

### 7-7n. 26차 보강 컴포넌트 (2026-06-08, US-J01 수락 UI)

| 컴포넌트 | 주요 props | 용도 / 화면 |
|----------|-----------|------------|
| `PublicAuthLayout` | `title`, `subtitle?`, `wide?`, `footer?` | 미인증 공개 인증 화면 레이아웃 (US-B01·US-J01). LoginPage `.ds-login` 카드 패턴 — **AppShell/SideNav 사용 금지** |
| `GuardianInvitationAcceptForm` | `form`, `onChange`, `onSubmit`, `onGoLogin`, `isSubmitting?`, `error?`, `success?`, `disabled?` | 보호자 초대 수락 폼 (US-J01). `/guardian/invitations/:token/accept` |

> **`INVITATION_STATUS` (26차)**: `Badge.jsx` export — 초대 목록·상세(향후 ClientDetailPage)에서 `StatusBadge status map={INVITATION_STATUS}` 사용.
>
> **GuardianInvitationAcceptPage 마이그레이션 (COD)**: 현재 WIP 페이지는 AppShell+SideNav — 아래 패턴으로 교체:
> ```jsx
> <PublicAuthLayout title="보호자 초대 수락" subtitle="센터에서 보낸 초대 링크로 계정을 활성화합니다." wide>
>   <GuardianInvitationAcceptForm form={form} onChange={setField} onSubmit={handleSubmit} onGoLogin={() => navigate("/")} ... />
> </PublicAuthLayout>
> ```

### 7-7m. 25차 보강 컴포넌트 (2026-06-08, MonthInput 잔여·로그아웃·차트 범례)

| 컴포넌트 | 주요 props | 용도 / 화면 |
|----------|-----------|------------|
| `LogoutButton` | (없음 — `useAuth` 내부) | AppShell topbar 공통 로그아웃 (US-B03). `aria-label="{이름} 로그아웃"`, `Button secondary size=sm` |

> **ChartContainer 확장 (25차)**: `axisTextColor` prop → viewport `--chart-axis-text` CSS 변수. 범례 라벨은 `.ds-chart__legend-label` 클래스 사용(인라인 `style={{ color }}` 금지).
>
> **MonthInput 잔여 (25차)**: `BillingPage` 조회 월 필터 — 22차 `AttendanceStatsPage`·`NHISImportPage`와 동일 패턴. `.ds-input--month` deprecated → `.ds-month-input`만 사용.

### 7-7f. 15차 보강 컴포넌트 (2026-06-07, Recharts 접근성 차트)

| 컴포넌트 | 주요 props | 용도 / 화면 |
|----------|-----------|------------|
| `ChartContainer` | `title`, `description?`, `height?`, `axisTextColor?`, `empty?`, `emptyMessage?`, `children` | Recharts 공통 래퍼 — `role="figure"`+`figcaption`+sr-only 요약 |
| `AttendanceRateChart` | `data[{label,rate}]`, `variant(line\|bar)`, `title?` | 월별 출석률 추이(US-H01 `DashboardPage`), 일자별 막대(US-E05 `AttendanceStatsPage`) |
| `HealthTrendChart` | `data[{date,systolic,diastolic,temperature,bloodSugar,spo2}]`, `metrics?` | 이용자 건강 추이 다중 라인(US-F04 `HealthDetailPage`) |
| `BranchCompareChart` | `branches[{branchName,attendanceRate,clientCount?}]` | HQ 지점별 출석률 비교 막대(US-H02 `DashboardPage` hq) |

> **의존성**: `recharts@^2.15` (package.json). 색상은 `useChartColors()` 훅으로 라이트/다크 자동 전환 — coder는 raw hex 금지.

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

### 7-7q. 32차 보강 컴포넌트 (2026-06-07, 공개 인증 레이아웃·Alert 정중도)

| 컴포넌트 | 주요 props | 용도 / 화면 |
|----------|-----------|------------|
| `PublicAuthLayout` | `title`(h1로 렌더), `subtitle?`, `wide?`, `children` | 미인증 공개 인증 화면 레이아웃 (US-B01·US-J01). LoginPage `.ds-login` 카드·브랜드 재사용 + skip link(`#public-auth-content`) + **페이지 h1**. **AppShell/SideNav 금지**. `GuardianInvitationAcceptPage` 적용 |

> **Alert 정중도 (32차)**: `Alert`의 기본 `role`은 이제 tone에서 파생된다 — `danger`/`warning`→`alert`(assertive), `info`/`success`/`neutral`→`status`(polite). 정적 안내(예: NHIS Chrome/Edge 가이드 info)가 스크린리더를 끊지 않는다. 긴급도를 직접 지정하려면 `role` prop으로 override(`<Alert tone="danger" role="status">`). 기존에 `role`을 명시하던 페이지는 동작 불변.
>
> **PublicAuthLayout (32차)**: 26차 §7-7n에 문서화됐으나 재이관 baseline에는 부재하던 컴포넌트를 실제 구현. 26차의 `GuardianInvitationAcceptForm`(별도 폼 컴포넌트)·`success`/`disabled`(만료 잠금) 패턴은 백엔드 J01 API live 연동 시점에 후속. 현재는 레이아웃(h1·skip·브랜드)만 우선 도입해 헤딩 계층 결함을 해소.

### 7-7p. 30차 보강 컴포넌트 (2026-06-07, 폼 입력·토글·연락처 마스킹)

| 컴포넌트 | 주요 props | 용도 / 화면 |
|----------|-----------|------------|
| `Switch` | `label`,`checked`,`onChange(next)`,`description?`,`onLabel?`,`offLabel?`,`disabled?`,`className?` | 즉시 적용 on/off 설정 (US-I03 — `allow_client_self_checkin` 등). WAI-ARIA `role="switch"` + `aria-checked` |
| `DateInput` | native `type=date` props 패스스루 | 날짜 입력·기간 필터 (US-D01·US-L01·§3-1). `Field` 안 `TextInput` 래퍼 — `.ds-date-input` |
| `MonthInput` | native `type=month` props 패스스루 | 대상 월 입력 (US-E05·US-G02/G04/G07). `Field` 안 `TextInput` 래퍼 — `.ds-month-input` |
| `MaskedPhone` | `phone`,`masked?`,`withLink?`,`className?` | 보호자·미납 목록 연락처 부분 마스킹 + `tel:` (US-K01·US-L02). `maskPhone(raw)` 헬퍼 export — 11자리 `010-****-5678`, 10자리 `02-***-5678` |

> **Switch vs Checkbox 재확인 (30차)**: `Checkbox`는 폼 제출 시 반영되는 **동의/선택**(US-D04 주민번호 수집 동의)에, `Switch`는 즉시 적용되는 **on/off 설정**(US-I03 셀프 체크인 허용)에 사용. `Switch.onChange`는 **다음 boolean 값**을 인자로 받는다(이벤트 객체 아님).
>
> **DateInput / MonthInput 사용 규칙 (30차)**: 신규 `type=date|month` 입력은 **`DateInput`/`MonthInput` + `Field`만** 허용 — raw `<input type="date" class="ds-input">` **금지**(접근성·다크/forced-colors 일관성·max-width 일관). 기존에 raw input을 사용한 페이지는 COD가 이 컴포넌트로 교체.
>
> **MaskedPhone PII (30차)**: 마스킹 결과는 시각 UI 기본값. `aria-label`은 마스킹된 값을 그대로 사용해 SR도 평문 노출 없음. `tel:` 링크의 href는 다이얼 가능한 raw digits(`01012345678`)로 — 모바일에서 「전화 걸기」를 트리거하기 위한 최소 노출이며, 백엔드는 이 컴포넌트에 가능한 한 **이미 마스킹된 값**을 전달해 클라이언트 메모리에 평문 잔류 시간을 줄인다(SEC).

```jsx
// 30차 사용 예시 — Switch (조직 설정)
<Switch
  label="이용자 본인 셀프 체크인 허용"
  description="QR 셀프 체크인 시 client_user 계정도 출석을 처리할 수 있습니다."
  checked={form.allowClientSelfCheckin}
  onChange={(next) => updateOrg({ allowClientSelfCheckin: next })}
/>
```

```jsx
// 30차 사용 예시 — DateInput / MonthInput / MaskedPhone
<Field label="생년월일" required error={err.birthdate}>
  {(p) => <DateInput {...p} value={form.birthdate} onChange={(e) => set({ birthdate: e.target.value })} />}
</Field>

<Field label="대상 월">
  {(p) => <MonthInput {...p} value={month} onChange={(e) => setMonth(e.target.value)} />}
</Field>

<MaskedPhone phone={guardian.phone} masked={guardian.phoneMasked} />
```

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
- **건강 추이 차트(US-F04)** — `HealthDetailPage`: `GET /api/v1/clients/:id/health?days=7|30` 응답을 `HealthTrendChart` `data` prop에 주입. 각 항목: `{ date, systolic, diastolic, temperature, bloodSugar, spo2 }`.
- **월별 출석률 차트(US-H01)** — `DashboardPage`: `branchDashboard.monthlyAttendanceRates[]` → `AttendanceRateChart` `data={ label: yearMonth, rate: attendanceRate }`.
- **일자별 출석률(US-E05)** — `AttendanceStatsPage`: `summary.dailyRates[]` → `AttendanceRateChart variant="bar"`. API 미포함 시 빈 상태 안내.
- **HQ 지점 비교(US-H02)** — `DashboardPage` hq: `hqDashboard.branches[]` → `BranchCompareChart`. 각 지점 `attendanceRate` 필수.
- **NHIS 배치 상태(US-G04)** — `BATCH_STATUS` 상수를 `import { BATCH_STATUS } from "../components/ui"` 로 가져온다(NHISImportPage 로컬 정의 제거·14차). coder는 모든 신규 페이지에서 Badge 모듈 상수를 사용.
- **플랫폼 고객사 관리(US-A01/A02)** — `PlatformPage` 「관리」→ `PlatformOrgDetailModal`. Tenant 상세 `dl` + `POST /api/v1/platform/organizations/:id/admins { email }` 발급. 목록 검색은 `SearchInput`, 상태는 `StatusBadge`+`BRANCH_STATUS`.
- **NHIS 배치 진행(US-G04)** — `BatchProgressSteps`로 PENDING→PROCESSING→COMPLETED 파이프라인 표시. `ReconciliationPage` 배치 카드 상단, `NHISImportPage` 미완료 배치 행에 인라인 표시. FAILED 시 처리중 단계 `--failed` 스타일.
- **감사 로그(US-I03)** — `SettingsPage` audit 탭 → `AuditLogPanel`. API: `GET /api/v1/settings/audit-logs?eventType=&from=&to=&page=`. `actorLabel`·`ipMasked`는 마스킹 문자열.
- **백업 설정(US-I03)** — `BackupSettingsPanel`. API: `GET/PATCH /api/v1/settings/backup`, `POST /api/v1/settings/backup/trigger`.
- **최초 비밀번호 변경(US-A02)** — `login()` 응답 `mustChangePassword` → `LoginPage` `PasswordChangeModal required`. API: `POST /api/v1/auth/change-password { newPassword }`. 완료 후 `clearMustChangePassword()` + 홈 이동.
- **청구 상태 카운트(US-G07)** — `GET /billing/claims` 응답 `statusCounts: { total, draft, confirmed, paid }` → `FilterChips counts`.
- **로그인 이력(§3-1)** — `SettingsPage` login-history 탭 → `LoginHistoryPanel`. API: `GET /api/v1/settings/login-history?role=&from=&to=&page=`. `emailMasked`·`ipMasked` 마스킹 문자열.
- **비밀번호 재설정(§3-1)** — `LoginPage` → `PasswordResetRequestModal`. API: `POST /api/v1/auth/password-reset/request { email }`. v1.1 실발송 전 스텁 UI.
- **페이지 오류 Alert(18·20차)** — 모든 Must 페이지 API 오류는 `Alert tone=danger`+`ds-page-alert`. coder 신규 페이지도 동일 패턴 준수. 20차 대상: `PlatformPage`·`BillingPage`·`DashboardPage`·`GuardianPage`·`CopayRatePage`.
- **청구 상태 확인(US-G07)** — `BillingPage` `openStatusConfirm(claim, nextStatus)` → `BillingStatusConfirmModal`. `BillingDetailPage` 상태 버튼도 동일 패턴 적용 권장.
- **NHIS 가이드(US-G04)** — `NhisImportGuidePanel`을 import 페이지 상단에 배치. 중복 Alert/ol 인라인 금지.
- **본인부담 비율(US-G00b)** — `CopayRateTable`+`PATCH /api/v1/billing/copay-rates`. `COPAY_TYPES`와 테이블 기본값 동기화.
- **보호자 포털(US-I02)** — `GuardianDailySummary`+`GET /guardian/clients/:id/summary`. `attendanceStatus`는 `ATTENDANCE_STATUS` 키.
- **건강 알림 공통** — 대시보드·보호자 포털 모두 `HealthAlertList` 사용. raw `<span class=ds-health-alert-list__badge>` 인라인 금지.
- **수가표 편집(US-G00a)** — `FeeScheduleTable`+`FeeSchedulePage`. raw `<input class=ds-input>` 인라인 금지 — `TextInput`+`aria-label` 패턴.
- **청구 상세 상태(US-G07)** — `BillingDetailPage` `openStatusConfirm` → `BillingStatusConfirmModal`. 목록 `BillingPage`와 동일.
- **미납 지표(US-L02)** — `OverduePage` `StatCard tone=danger`. 인라인 `color: danger-text` 금지.
- **페이지 오류 Alert(21차)** — `HealthDetailPage`·`QrGeneratePage`·`ClientDetailPage` 탭 오류도 `Alert tone=danger`+`.ds-page-alert`.
- **대상 월(22차)** — `MonthInput`+`Field`. raw month input 금지.
- **입금(22차)** — `PaymentRecordModal`+`PaymentPage`. inline Modal 폼 금지.
- **reconciliation 요약(22차)** — `ReconciliationSummaryBar`. inline flex summary 금지.
- **이용자 검색(22차)** — `SearchInput hideLabel`. action bar raw search 금지.
- **Must 페이지 레이아웃(24차)** — Card `className="ds-section-gap|ds-section-gap--lg|ds-card--mb"`·페이지 `.ds-page-lede`/`.ds-page-footnote`·표 빈 셀 `.ds-table-empty`·액션 `.ds-table-actions`. raw `style={{ marginTop/color }}` **금지** — ChartContainer `height`·`axisTextColor` prop 등 동적 값만 예외.
- **청구 월 필터(25차)** — `BillingPage` `MonthInput`+`Field`. raw `type=month`+`ds-input--month` **금지**.
- **차트 범례(25차)** — `HealthTrendChart`·`BranchCompareChart` Legend `formatter` → `<span className="ds-chart__legend-label">`. `ChartContainer`에 `axisTextColor={axisText}` 전달.
- **로그아웃(25차)** — `AppShell`이 `LogoutButton`을 topbar에 기본 탑재. 페이지별 로그아웃 버튼 중복 추가 금지.
- **보호자 초대 수락(26차, US-J01)** — `GuardianInvitationAcceptPage` → `PublicAuthLayout wide` + `GuardianInvitationAcceptForm`. AppShell/SideNav **금지**. API: `POST /guardian/invitations/{token}/accept`. 만료(404/410) → `error` Alert + `disabled`. 성공 → `success` + 폼 잠금 + `navigate("/")`. **`INVITATION_STATUS`** — 초대 목록 Badge.
- **보호자 초대 이력(27차, US-J01)** — `ClientDetailPage` `client.guardianInvitations[]` → `GuardianListCard` → `GuardianInvitationList`. 재발송/취소 API 연동 후 `handleResendInvitation`·`handleRevokeInvitation` 스텁 제거.
- **기간 필터(27·28차, §3-1·US-D01·US-L01)** — `AuditLogPanel`·`LoginHistoryPanel`·`ClientFormPage`·`PaymentRecordModal` `DateInput`+`Field`. raw `type=date` 금지.
- **사진 업로드(28차, US-D01)** — `ClientPhotoField` 트리거 버튼 `aria-label`+`aria-controls`. alt는 `TextInput`+`Field`.
- **보호자 초대 피드백(28차, US-J01)** — `ClientDetailPage` 초대 성공/오류 `Alert tone=success|warning`+`.ds-page-alert`. `GuardianInviteModal` 발송 `aria-busy`.
- **보호자 상세 빈 상태(25차)** — `GuardianDetailPage` API 실패/미응답 → `EmptyState`+`Alert tone=danger`+`ds-page-alert`.
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
| `/guardian/invitations/:token/accept` | `GuardianInvitationAcceptPage` | **공개**(미인증) | **US-J01** |
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

> **2026-06-07 36차**: 전체 15개 누락 페이지 UI 구현 완료. 아래는 coder가 API 연동해야 할 잔여 항목.

| 화면/기능 | 경로/파일 | 비고 |
|----------|-----------|------|
| 청구 상세 API | `BillingDetailPage` | US-G02 — `GET /billing/claims/:id` + items + status-history 응답 구조 확인 필요 |
| 결석 API | `AttendancePage` | US-E01 — `POST /attendance/absent` |
| 이용자 사진 API | `ClientFormPage` | US-D01 — `POST /clients/:id/photo` multipart |
| 등급 이력 API | `ClientDetailPage` grade 탭 | US-M01 — `ltcGradeHistory[]` |
| 대시보드 API | `DashboardPage` | US-M02 — `/dashboard/*` 통합 응답 |
| QR 카메라 스캔 | `GuardianCheckinPage` | `html5-qrcode` 라이브러리 연동 — 현재 수동 토큰 입력만 지원 (§10 UXD-2) |
| 건강·출석통계 차트 API | `HealthDetailPage`, `AttendanceStatsPage` | `HealthTrendChart`/`AttendanceRateChart` data prop에 API 응답 연동 |
| 로그인 이력 API | `SettingsPage` 감사 탭 | `GET /settings/login-history` |
| 직원 관리 | `/staff` | Should — v1 이후 |

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
| `.ds-masked-phone` | 마스킹 연락처 + `tel:` 링크 (30차 — `MaskedPhone`) |
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
| `.ds-chart` / `__title`·`__viewport`·`__empty`·`__hint`·`__legend-label` | Recharts 접근성 래퍼 (15차, ChartContainer; 25차 범례 라벨) |
| `.ds-link` | 인라인 텍스트 링크 — `role-link` 대체 (15차) |
| `.ds-audit-log` / `__filters`·`__loading` | 감사 로그 패널 (17차, AuditLogPanel) |
| `.ds-backup-settings` / `__summary`·`__actions`·`__note` | 백업 설정 패널 (17차) |
| `.ds-filter-chip__count` | FilterChips 상태 건수 배지 (17차, US-G07) |
| `.ds-login__footer` | 로그인 하단 재설정 링크 (17차) |
| `button.ds-link` | 표·목록·로그인 내 텍스트 링크 버튼 (17·18차) |
| `.ds-page-alert` | 페이지 상단/본문 API 오류·피드백 Alert 여백 (18차) |
| `.ds-login-history` / `__title`·`__help`·`__filters`·`__loading` | 로그인 이력 패널 (18차, LoginHistoryPanel) |
| `.ds-security-panel` | 보안 탭 PasswordChange·PasswordReset 액션 컨테이너 (19차, SettingsPage) |
| `.ds-billing-confirm__summary` | 청구 상태 확인 모달 요약 dl (20차) |
| `.ds-nhis-guide` / `__steps`·`__note`·`__intro` | NHIS import 온보딩 패널 (20차, US-G04) |
| `.ds-copay-rate-cell` / `__unit` | 본인부담 비율 입력 셀 (20차, US-G00b) |
| `.ds-guardian-summary` / `__stats`·`__alerts` | 보호자 포털 오늘 현황 (20차, US-I02) |
| `.ds-health-alert-list__empty`·`__reasons` | HealthAlertList 빈 상태·사유 (20차) |
| `.ds-action-bar__actions--start` | action-bar 좌측 정렬 (20차, CopayRatePage) |
| `.ds-text-secondary` / `.ds-text-muted` | 보조·플레이스홀더 텍스트 (21차) |
| `.ds-mono` | 인정번호·배치 ID 등 고정폭 (21차) |
| `.ds-diff-amount` | NHIS reconciliation 차이 금액 강조 (21차, US-G06) |
| `.ds-table-actions` | 표 내 액션 버튼 flex 래퍼 (21차) |
| `.ds-section-gap` | 카드·섹션 상단 여백 (21차) |
| `.ds-table-empty` | 표 빈 상태 셀 (21차) |
| `.ds-stat__value--danger` | StatCard 위험 지표 값 색 (21차, US-L02) |
| `.ds-fee-schedule-hint` | 수가표 1밴드 안내 텍스트 (21차) |
| `.ds-forbidden-page__desc` / `__actions` | 403 페이지 본문·링크 (21차) |
| `.ds-summary-bar` / `.ds-summary-item` | NHIS reconciliation 배치 요약 (22차, US-G06) |
| `.ds-month-input` | 대상 월 입력 max-width (22차, US-E05·G04) |
| `.ds-modal-intro` | 모달 상단 요약 텍스트 (22차, US-L01) |
| `.ds-form-actions` | 카드·폼 하단 액션 버튼 여백 (22차) |
| `.ds-section-gap--lg` | 섹션 간 24px 여백 (22차) |
| `.ds-batch-progress-inline` | 표 셀 내 NHIS 진행 단계 (22차) |
| `.ds-summary-item__label` / `__value` | Reconciliation 배치 요약 항목 (21차) |
| `.ds-inline-actions` | 버튼·뱃지 수평 중앙 정렬 묶음 (23차, ClientDetailPage 등) |
| `.ds-client-summary` / `__avatar`·`__name`·`__meta` | 이용자 상세 요약 헤더 (23차, US-D03) |
| `.ds-form-actions--end` | 폼 하단 액션 버튼 우측 정렬 (23차, ClientFormPage) |
| `.ds-page-lede` | 페이지 상단 보조 텍스트(날짜·안내) (24차, AttendancePage) |
| `.ds-grid--gap-bottom` | StatCard 그리드 하단 여백 (24차, AttendancePage) |
| `.ds-card--mb` | Card 하단 간격 (24차, GuardianPage) |
| `.ds-form-row__action` | 폼 행 내 버튼 정렬 (24차, QrGeneratePage) |
| `.ds-page-footnote` | 페이지 하단 각주·v2 안내 (24차, OverduePage·SessionTimeoutModal) |
| `.ds-card-link` | 카드 내부 링크 여백 (24차, DashboardPage) |
| `.ds-dl-grid--spaced` | description list 하단 여백 (24차, PlatformOrgDetailModal) |
| `.ds-alert--stack` / `.ds-form--stack` | Alert·폼 스택 여백 (24차) |
| `.ds-tab-panel-body` / `.ds-submit-block` | 탭 패널·주요 CTA 상단 여백 (24차, GuardianPage·GuardianCheckinPage) |
| `.ds-alert-body` / `.ds-alert-body--flush` / `.ds-alert-action` | Alert 본문·액션 (24차, MedicationDuplicateAlert·HealthAbnormalBanner) |
| `.ds-tabular-nums` | 표 숫자 열 (24차, FeeRateHistoryPanel) |
| `.ds-progress-steps__list` | NHIS 배치 진행 ol (24차, BatchProgressSteps) |
| `.ds-section-gap--bottom` | 하단만 24px 여백 (24차, QrGeneratePage) |
| `.ds-auth-page` / `--wide` / `__lede` / `__actions` | 공개 인증 카드 (26차, US-J01 — LoginPage `.ds-login` 확장, AppShell 대체) |
| `.ds-date-input` | 기간 필터 date input max-width (27차, §3-1) |
| `.ds-guardian-card__subtitle` / `__invitations` | 보호자 카드 초대 이력 섹션 (27차, US-J01) |
| `.ds-guardian-invitations` | 초대 이력 표 overflow (27차) |
| `.ds-list` / `.ds-list__item` | Must 목록 ul/li 레이아웃 (33차) |
| `.ds-breadcrumb` | 상세 페이지 경로 (33차, ClientDetailPage) |
| `.ds-form-grid` | 폼 2열 그리드 (33차, ClientDetailPage·NHISImportPage) |
| `.ds-tabs__list` / `.ds-tab` / `.ds-tab--active` / `.ds-tabpanel` | WAI-ARIA 탭 (33차, US-D03) |
| `.ds-pagination` / `.ds-pagination__status` | 목록 페이지네이션 (33차) |
| `.ds-sidenav__group` / `__toggle` / `__sublist` / `__chevron` | 2단 SideNav 그룹 (33차, US-UX-02) |
| `.ds-branch-switcher` | topbar 지점 선택기 (33차, US-B02) |

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
- ~~차트(월별 출석률 US-H01/F04) — Recharts vs Chart.js 미선정~~ → **15차 UXD-1 완료**: **Recharts** 채택 + `ChartContainer`·`AttendanceRateChart`·`HealthTrendChart`·`BranchCompareChart` 구현. 플레이스홀더 제거. coder는 API data prop 연동만 남음.
- ~~NHIS 배치 진행 UI — CSS만 존재~~ → **16차 완료**: `BatchProgressSteps` React 컴포넌트 + `ReconciliationPage`/`NHISImportPage` 통합.
- ~~플랫폼 고객사 「관리」버튼 무기능~~ → **16차 완료**: `PlatformOrgDetailModal` + US-A02 관리자 발급 폼.
- QR 스캐너 — **html5-qrcode** vs native BarcodeDetector → #UXD-2. `GuardianCheckinPage`는 현재 토큰 수동입력 폴백 제공.
- ~~다크 모드 미정~~ → **11차 구현 완료**: `tokens.css` `[data-theme="dark"]` 토큰 오버라이드 + `ThemeToggle`(AppShell topbar) + `theme.js`. 컴포넌트가 시맨틱 토큰만 쓰므로 코드 변경 0. 대비 AA 검증 §2-4. 후속: 차트(Recharts 등) 도입 시 다크 팔레트 색 매핑 별도 확인.
- 미확정 사항은 `docs/planning/PLAN_NOTES.md`의 `### [UXD] UX 설계 질문` 섹션에 기록.
- Toast: `ToastProvider`를 `main.jsx`에 추가 후 `useToast()`로 API 연동 피드백. **9차 배선 완료**.
- SessionTimeoutModal: `SessionTimeoutProvider`가 AuthContext 30분 타이머와 연동 (US-B03). **9차 배선 완료**.
- 보호자 초대(US-J01 v1.1): `GuardianListCard` 「초대 발송」 버튼은 현재 `disabled` — v1.1 착수(v1 backend merged 이후) 시 활성화.
- **고대비/강제 색상(12차)**: `forced-colors`/`prefers-contrast` 규칙은 CSS만으로 동작(컴포넌트 코드 변경 0). **tester 검증 권장**: Windows 고대비 모드·`prefers-contrast: more`에서 로그인·대시보드·청구 표·모달 캡처해 경계선·포커스 식별성 확인.
- ~~`styles.css`의 데모 잔여 클래스(`.role-link`·`.demo-grid`)~~ → **25차 제거 완료**. 신규 링크는 `.ds-link`·`button.ds-link`만 사용.
- **33차 baseline 후속 (COD 우선순위)**:
  1. ~~`AppShell`·`SideNav`(2단)·`Table`/`Tabs`·`BranchSwitcher`·`StatCard`·`SearchInput`·`FilterChips`·`Pagination`·`LogoutButton`~~ → **33차 완료**.
  2. **페이지 연동**: `ClientDetailPage` raw 섹션 → `Tabs`/`TabPanel`(기본/건강/출석/청구 US-D03). `ClientListPage`·`BillingPage` → `SearchInput`·`Table`·`Pagination`·`FilterChips`. `DashboardPage` → `StatCard` 그리드(US-M02).
  3. **`BranchSwitcher` API**: `AppShell` `onBranchChange` → `PATCH /api/v1/auth/active-branch` + AuthContext `activeBranchId` 갱신.
  4. **`ToastProvider`·`SessionTimeoutProvider`·`SessionTimeoutModal`** — 30분 비활성(US-B03)·전역 피드백 (US-B03).
  5. 도메인 특화 컴포넌트(차트·NHIS·모달 등) — DESIGN_SYSTEM §7-2~7-7 카탈로그 참조, coder 페이지 연동.

---

*이 문서는 ux_designer 에이전트(UXD)가 관리합니다. 토큰·컴포넌트 변경 시 본 문서와 `memory/decisions.md`를 동기화하세요.*
