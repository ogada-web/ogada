<!-- doc:owner=TWR doc:audience=human updated=2026-07-15T05:24:00+09:00 -->
# ogada 변경 기록

> **누가 쓰나**: TWR(문서 에이전트)  
> **누가 읽나**: 운영·기획 담당자 — 개발 세부사항은 각 카드 맨 아래 「자세히」만 보면 됩니다.  
> **기준**: develop 최신 코드 기준 (J03 channel-status 필드 별칭 · G2 초안 수정 시 상세 재조회 · M12 SSO 오류 안내 · 기관 공지 DRAFT 수정·첨부 URL · M12 SSO 보안 · V192 · M11 급여)

## 읽는 법

1. **최근 7일 요약**만 봐도 됩니다.
2. 카드의 **내 화면/업무에 영향**이 「없음」이면 앱 체감 변화 없음(문서·테스트·내부 작업).
3. **3개월 지난 날짜**는 이 파일에서 삭제합니다. 오래된 내용은 남기지 않습니다.

## 최근 7일 요약

- **2026-07-14** — 알림 채널 **API 필드 별칭** · 기관 공지 **수정 시 상세 재조회** · 재무회계 SSO **429·비허용 URL 안내 문구** · 초안 수정·첨부 URL · M12 SSO 호스트 제한 · 기관 공지 게시판 · 서버 DRAFT · V192 · suppressed bootstrap · 발송 이력 필터 · M11 급여 — **모듈 KPI 93.6% · BE `1f3698d`·FE `71839a6` SYNCED · 문서 전수 최신화**
- **2026-07-13** — 차량 **송영 주소** trim·연속 공백 정리 · health **V190** · **금일 배차 제외** UI·서버 이중 잠금 · 송영표 스크린리더 목록 구조
- **2026-07-07~12** — develop HEAD 유지 (이전 baseline 대비 코드 변경 없음)
- **2026-06-27** — 위생·안전 checklist 필수/선택 semantics 확정 · NHIS 수가 seed 미지원 연도 오류 메시지 개선
- **2026-06-28** — 이동서비스비 1일 1회 안내가 parity catalog와 연동 · live E2E bootstrap health probe 회귀 lock


---

## 2026-07-14

### 📝 J03 채널 별칭 · G2 상세 재조회 · M12 SSO 오류 ops 문서화
- **에이전트**: TWR
- **한 일**: develop HEAD 실측 후 FAQ·매뉴얼·관리/배포 가이드에 **channel-status API_SPEC 별칭**·**기관 공지 수정 시 GET 상세**·**재무회계 SSO 429/비허용 URL 화면 안내** 를 반영했습니다.
- **내 화면/업무에 영향**: 없음 — 문서·운영 가이드만 갱신
- **상태**: 완료

<details><summary>자세히</summary>

- 실측: BE develop **`1f3698d`** · FE develop **`71839a6`** — **132 route** · **105 page** · Flyway **V1–V192** · 모듈 **~93.6%**
- FAQ · ADMIN §6-2-24f/h·§10-8 · USER_MANUAL §4-6-5·§4-7-3a·§5-5 · DEPLOYMENT §1-4·§4-3

</details>

### ✅ J03 알림 채널 상태 API 필드 별칭 (BE·FE)
- **에이전트**: COD
- **한 일**: **`GET …/notifications/channel-status`** 응답에 API 명세와 맞는 **별칭 필드**를 추가하고, 준비 상태 패널이 **구현 키·별칭 둘 다** 읽도록 맞췄습니다. 기존 연동은 깨지지 않습니다.
- **내 화면/업무에 영향**: **센터장** — 조직 설정·대시보드 **「알림 채널 준비 상태」** 표시는 동일. IT·연동 스크립트가 명세 이름(`solapiSenderNumberConfigured` 등)을 써도 동작
- **상태**: 완료

<details><summary>자세히</summary>

- 별칭: `solapiSenderNumberConfigured` ↔ `solapiSenderIdConfigured` · `kakaoChannelIdConfigured` ↔ `solapiKakaoPfIdConfigured` · `requiredAlimtalkTemplates` ↔ `templates`
- FE: `normalizeNotificationChannelStatus` · `NotificationChannelReadinessPanel`

</details>

### ✅ G2 초안 수정 시 서버 상세 재조회 · M12 SSO 오류 문구 (FE)
- **에이전트**: COD
- **한 일**: 기관 공지 **「수정」** 시 목록 값이 아니라 **`GET …/facility-notices/{id}`** 로 최신 본문·첨부 URL을 불러옵니다. 재무회계 **SSO 실패** 시 분당 제한·비허용 포털 URL을 **한국어로 안내**합니다.
- **내 화면/업무에 영향**: **센터장·사회복지사** — 초안 수정 시 다른 탭에서 고친 내용이 반영됨. **센터장** — `/accounting` SSO 버튼 실패 사유가 화면에서 읽힘
- **상태**: 완료

<details><summary>자세히</summary>

- G2: 게시된 글이면 편집 취소·안내 · 상세 실패 시 목록 값으로 편집 계속
- M12: 429 「요청이 너무 많습니다…」 · 비허용 URL 안내 · 서버 한글 메시지 우선

</details>

### 📝 G2 초안 수정·첨부 URL · M12 SSO 보안 ops 문서화
- **에이전트**: TWR
- **한 일**: develop HEAD 실측 후 FAQ·매뉴얼·관리/배포 가이드에 **기관 공지 DRAFT PATCH·첨부 URL**·**SSO 포털 allowlist·분당 rate limit·HQ/BRANCH만 handoff** 를 반영했습니다.
- **내 화면/업무에 영향**: 없음 — 문서·운영 가이드만 갱신
- **상태**: 완료

<details><summary>자세히</summary>

- 실측: BE develop **`bf96c29`** · FE develop **`4d1b01c`** — **132 route** · **105 page** · Flyway **V1–V192** · 모듈 **~93.6%**
- FAQ · ADMIN §6-2-24f/h · USER_MANUAL §4-6-5·§4-7-3a · DEPLOYMENT §1-4·§4-9

</details>

### ✅ G2 기관 공지 초안 수정·자료실 첨부 URL (FE)
- **에이전트**: COD
- **한 일**: **`/clients/home-newsletter`** 기관 공지·자료실에서 **DRAFT 초안을 다시 고쳐 저장**할 수 있게 했고, 자료실용 **첨부 URL**(선택) 필드를 붙였습니다. **게시(PUBLISHED) 후에는 본문을 고칠 수 없습니다.**
- **내 화면/업무에 영향**: **센터장·사회복지사** — 초안 행 **「수정」** → 제목·본문·첨부 URL 고친 뒤 **「초안 수정 저장」**. 자료실에 외부 자료 링크를 남길 수 있음
- **상태**: 완료

<details><summary>자세히</summary>

- API: **`PATCH …/facility-notices/{id}`** (DRAFT만) · 필드 `attachmentUrl`(최대 500자)
- UI: 수정 중 안내 배너 · **수정 취소** · 게시 후 수정 버튼 숨김

</details>

### ✅ M12 재무회계 SSO handoff 보안 강화 (BE)
- **에이전트**: COD
- **한 일**: 수지파인 SSO 진입이 **허용된 호스트(sujifine)** 로만 가고, **분당 요청 횟수**를 제한하며, **OTP mint는 본사·지점 관리자만** 가능하게 했습니다. 잘못된 포털 URL·OTP 남용을 막습니다.
- **내 화면/업무에 영향**: **센터장(`hq_admin`/`branch_admin`)** — SSO 자동 로그인은 그대로. **사회복지사** — **공개 로그인은 가능**, **SSO 자동 로그인은 403**. IT가 포털 URL을 잘못 넣으면 SSO가 꺼지고 안내됨
- **상태**: 완료

<details><summary>자세히</summary>

- allowlist: `https://sujifine.co.kr` · `https://www.sujifine.co.kr` (https만)
- rate limit 기본: 행위자 **10회/분** · 기관 **30회/분** → **429 `RATE_LIMITED`**
- RBAC: `POST …/bpo-sso-handoff` — **HQ/BRANCH only** (social_worker 제외)
- health blocker: **`sso-portal-url-not-allowlisted`**

</details>

### 📝 G2 기관 공지 게시판·DRAFT 영속·suppressed gate ops 문서화
- **에이전트**: TWR
- **한 일**: develop HEAD 실측 후 FAQ·매뉴얼·관리/배포 가이드에 **기관 공지·자료실 CRUD(10-4)**·**미리보기→facility-notice DRAFT**·**V192**·health **`liveE2eSuppressedBootstrapOperationBlockers`** 를 반영하고, 잔여 `board-ui-planned` 문구를 정리했습니다.
- **내 화면/업무에 영향**: 없음 — 문서·운영 가이드만 갱신
- **상태**: 완료

<details><summary>자세히</summary>

- 실측: BE develop **`82a83e3`** · FE develop **`0210aaa`** — **132 route** · **105 page** · Flyway **V1–V192** · 모듈 **~93.6%**
- FAQ · ADMIN §6-2-24h · USER_MANUAL §4-7-3a · DEPLOYMENT §1-3·§1-4

</details>

### ✅ live E2E suppressed bootstrap blockers 노출 (BE)
- **에이전트**: COD
- **한 일**: health·live-e2e probe에 **`liveE2eSuppressedBootstrapOperationBlockers`** 를 추가했습니다. effective gate가 초록이어도 bootstrap만 꺼진 이유를 IT가 바로 볼 수 있습니다.
- **내 화면/업무에 영향**: 없음 — **IT·QA** 의 live E2E·배포 스모크 판정용
- **상태**: 완료

<details><summary>자세히</summary>

- 억제 대상: `bootstrap-disabled` · `bootstrap-service-unavailable`
- health/probe: `liveE2eEffectiveOperation*` + **`liveE2eSuppressedBootstrapOperationBlockers`**
- 현장 앱 메뉴·업무 화면 변경 없음

</details>

### ✅ G2 가정통신문 초안을 서버 DRAFT로 저장 (FE)
- **에이전트**: COD
- **한 일**: `/clients/home-newsletter` 에서 미리보기 후 **「서버 초안(DRAFT) 저장」** 하면 **기관 공지 DRAFT**로 DB에 남깁니다. 작성 폼 복원용 연월·이용자·센터 메타는 세션에도 같이 둡니다.
- **내 화면/업무에 영향**: **센터장·사회복지사** — 브라우저를 닫아도 **서버 초안 목록**에서 다시 찾아 게시·삭제할 수 있음. **이메일은 여전히 발송되지 않음**
- **상태**: 완료

<details><summary>자세히</summary>

- `HomeNewsletterLaunchPage` — `POST …/facility-notices` (NOTICE·제목·본문) · 세션 메타 병행
- 버튼 문구: **「서버 초안(DRAFT) 저장」** (구 세션 전용 저장에서 확장)

</details>

### ✅ G2 기관 공지·자료실 게시판 CRUD (BE·FE)
- **에이전트**: COD
- **한 일**: 케어포 **10-4** 패리티로 **기관 공지·자료실** 게시판 API·화면을 붙였습니다. 초안 작성·분류/상태 필터·게시·삭제까지 한 화면(`/clients/home-newsletter`)에서 됩니다. DB **V192** `facility_notices` 테이블이 추가됩니다.
- **내 화면/업무에 영향**: **센터장·사회복지사** — 가정통신문 화면에 **「기관 공지 · 자료실 게시판」** 카드가 생김. **공지(NOTICE)·자료실(RESOURCE)** 초안을 만들고 **게시**할 수 있음
- **상태**: 완료

<details><summary>자세히</summary>

- API: `GET/POST /api/v1/notifications/facility-notices` · `GET/PATCH/DELETE …/{id}` · `POST …/{id}/publish`
- 분류 `NOTICE`/`RESOURCE` · 상태 `DRAFT`/`PUBLISHED` · 권한 `hq_admin`·`branch_admin`·`social_worker`
- authoring 잔여 blocker `board-ui-planned` **해제**(빈 목록) · 모듈 KPI **~93.6%**

</details>

### 📝 G2 이력 필터·세션 초안 ops 문서화
- **에이전트**: TWR
- **한 일**: develop HEAD 실측 후 FAQ·매뉴얼·관리/배포 가이드에 **발송 이력 board 필터**(연월·상태·검색)·**센터명/요약 표시**·**세션 초안 게시판·이력→작성 재사용**·**V191** 인덱스를 반영했습니다.
- **내 화면/업무에 영향**: 없음 — 문서·운영 가이드만 갱신
- **상태**: 완료

<details><summary>자세히</summary>

- 실측: BE develop **`24f555d`** · FE develop **`bb48b6c`** — **132 route** · **105 page** · Flyway **V1–V191** · 모듈 **~92.4%**
- FAQ · ADMIN §6-2-24h · USER_MANUAL §4-7-3a · DEPLOYMENT §1-3·§1-4

</details>

### ✅ G2 가정통신문 세션 초안·이력 재사용 (FE)
- **에이전트**: COD
- **한 일**: **`/clients/home-newsletter`** 에 **세션 초안 게시판**(브라우저 세션만, 서버 미저장)을 넣고, 미리보기 결과·발송 이력 행을 **작성 폼에 다시 불러** 쓸 수 있게 했습니다. 서버 게시판·기관 공지 저장은 아직 후속입니다.
- **내 화면/업무에 영향**: **센터장·사회복지사** — 같은 화면에서 초안을 잠깐 모아 두고, 이전 발송 내용을 작성 폼에 가져와 미리보기할 수 있음. **브라우저를 닫으면 초안은 사라짐**
- **상태**: 완료

<details><summary>자세히</summary>

- `HomeNewsletterLaunchPage` — 세션 초안 저장/불러오기/삭제 · 이력 「작성에 불러오기」 · 최대 20건
- 안내: 서버 10-4 CRUD(`board-ui-planned`) 잔여 · 발송은 이용자 상세

</details>

### ✅ G2 가정통신문 발송 이력 board 필터 (BE·FE)
- **에이전트**: COD
- **한 일**: 발송 이력에서 **대상 연월·상태·검색어**로 **서버 쪽 필터**가 돌아가도록 맞췄습니다. 표에 **센터명·요약**도 보이며, 현재 페이지만이 아니라 전체 이력에서 걸러집니다.
- **내 화면/업무에 영향**: **센터장·사회복지사** — `/clients/home-newsletter` **발송 이력**에서 연월·발송됨/실패/대기·수급자·센터·요약 검색으로 원하는 건만 조회
- **상태**: 완료

<details><summary>자세히</summary>

- API: `GET …/dispatch-history?yearMonth=&status=&q=` (+ 기존 `branchId`·`page`·`size`)
- 응답 행: `centerName`·`summary` · 상태 필터 `ALL`/`PENDING`/`SENT`/`FAILED`
- BE 조회 인덱스 **V191** (`idx_notifications_org_branch_template_created`)

</details>

### 📝 G2 작성 미리보기·live E2E effective gate ops 문서화
- **에이전트**: TWR
- **한 일**: develop HEAD 실측 후 FAQ·매뉴얼·관리/배포 가이드에 **가정통신문 작성 미리보기 화면**과 **live E2E effective operation gate**(health/probe)를 반영했습니다.
- **내 화면/업무에 영향**: 없음 — 문서·운영 가이드만 갱신
- **상태**: 완료

<details><summary>자세히</summary>

- 실측: BE develop **`5d6c007`** · FE develop **`3bd50ac`** — **132 route** · **105 page** · Flyway **V1–V190** · 모듈 **~92.4%**
- FAQ 정정·신규 · ADMIN §6-2-24h · USER_MANUAL §4-7-3a · DEPLOYMENT §1-4 smoke

</details>

### ✅ G2 가정통신문 작성·미리보기 화면 (FE)
- **에이전트**: COD
- **한 일**: **`/clients/home-newsletter`** 에 **「가정통신문 작성 미리보기」** 카드를 넣었습니다. 대상 연월·요약을 입력하면 **이메일 제목·본문 초안**을 바로 확인할 수 있습니다. **실제 발송은 하지 않습니다.**
- **내 화면/업무에 영향**: **센터장·사회복지사** — 발송 전에 초안을 같은 화면에서 미리 확인. 게시판형 작성·관리 UI는 아직 후속
- **상태**: 완료

<details><summary>자세히</summary>

- `HomeNewsletterLaunchPage` — `GET …/authoring` · `POST …/compose-preview` · Field 연동·필드 오류
- 필수: 연월 `YYYY-MM` · 선택: 요약(500자)·이용자명·센터명 placeholder
- 잔여: 게시판 UI(`board-ui-planned`) · 발송은 이용자 상세

</details>

### ✅ live E2E effective operation gate (BE·FE)
- **에이전트**: COD
- **한 일**: health·live-e2e probe에 **`liveE2eEffectiveOperationReady`** 등 **effective gate** 필드를 내려주고, 프론트 live harness가 이를 우선 쓰도록 맞췄습니다. bootstrap만 꺼져 있어도(자격 로그인으로 복구 가능하면) suite가 잘못 막히지 않습니다.
- **내 화면/업무에 영향**: 없음 — **IT·QA** 의 live E2E·배포 스모크 판정용
- **상태**: 완료

<details><summary>자세히</summary>

- health/probe: `liveE2eEffectiveOperationReady` · `…Blockers` · `…Reason` — `bootstrap-disabled` / `bootstrap-service-unavailable` 필터
- FE: `liveBackendProbe` · `liveGlobalSetup` — backend effective 우선
- 현장 앱 메뉴·업무 화면 변경 없음

</details>

### 📝 G2 가정통신문 authoring·지점 이력 ops 문서화
- **에이전트**: TWR
- **한 일**: develop HEAD 실측 후 FAQ·매뉴얼·관리/배포 가이드에 **가정통신문 authoring catalog·compose-preview API**·**지점별 발송 이력 스코프** 를 반영하고, health **authoringAvailability=AVAILABLE** 정정을 반영했습니다.
- **내 화면/업무에 영향**: 없음 — 문서·운영 가이드만 갱신
- **상태**: 완료

<details><summary>자세히</summary>

- 실측: BE develop **`ac422cc`** · FE develop **`5805d68`** — **132 route** · **105 page** · Flyway **V1–V190** · 모듈 **~92.4%**
- FAQ · ADMIN §6-2-24h · USER_MANUAL §4-7-3a · DEPLOYMENT §1-4 smoke

</details>

### ✅ G2 가정통신문 발송 이력 지점 스코프 (FE)
- **에이전트**: COD
- **한 일**: **`/clients/home-newsletter`** 에서 발송 이력 조회 시 로그인 사용자 **소속 지점(`branchId`)** 을 API에 넘기도록 고쳤습니다. **지점 관리자**는 다른 지점 기록이 섞이지 않습니다.
- **내 화면/업무에 영향**: **지점 관리자·사회복지사** — 가정통신문 **발송 이력 표**에 **본인 지점 기록만** 표시(HQ는 기존처럼 전체·지점 선택 가능)
- **상태**: 완료

<details><summary>자세히</summary>

- `HomeNewsletterLaunchPage` — `branchId` query 전달 · `HomeNewsletterLaunchPage.test` 회귀
- API: `GET …/dispatch-history?branchId=` (기존 파라미터, FE wire 보강)

</details>

### ✅ G2 가정통신문 authoring catalog·compose-preview (BE)
- **에이전트**: COD
- **한 일**: **`GET /api/v1/notifications/home-newsletter/authoring`** 과 **`POST …/compose-preview`** 로 가정통신문 **작성 필드 catalog**·**이메일 초안 미리보기**를 제공합니다. **발송은 하지 않습니다**. health·launch catalog의 **authoringAvailability** 가 **AVAILABLE** 로 바뀌었고, 잔여 blocker는 **게시판 UI(`board-ui-planned`)** 만 남습니다.
- **내 화면/업무에 영향**: 없음 — **작성·미리보기 화면은 후속**. API·health만 준비됨. 발송은 여전히 **이용자 상세** (Q217)
- **상태**: 완료

<details><summary>자세히</summary>

- compose 필드: **`yearMonth`(필수)** · **`summary`(선택, 500자)** · preview에 `clientName`·`centerName` optional
- 권한: `hq_admin`·`branch_admin`·`social_worker`
- 회귀: `GuardianHomeNewsletterAuthoringServiceTest` · routing·RBAC · `HealthControllerTest`

</details>

### 📝 M12 SSO handoff·가정통신문 이력 ops 문서화
- **에이전트**: TWR
- **한 일**: develop HEAD 실측 후 FAQ·매뉴얼·관리/배포 가이드에 **M12 SSO handoff 422 오류**·**가정통신문 발송 이력 페이지 크기(Q790)** 를 반영하고, DEPLOYMENT §1-3 baseline을 **132 route · 105 page**로 정정했습니다.
- **내 화면/업무에 영향**: 없음 — 문서·운영 가이드만 갱신
- **상태**: 완료

<details><summary>자세히</summary>

- 실측: BE develop **`3ea0832`** · FE develop **`b7c9fa4`** — **132 route** · **105 page** · Flyway **V1–V190** · 모듈 **~92.4%**
- FAQ **Q790** · Q787 정정 · DEPLOYMENT §1-3 baseline · ADMIN §6-2-24f/h · USER_MANUAL §4-7-3a

</details>

### ✅ M12 재무회계 SSO handoff HTTP 회귀 테스트 (BE)
- **에이전트**: TSR
- **한 일**: **`POST /api/v1/billing/accounting/bpo-sso-handoff`** 에 대해 **200 OTP 응답**과 **자격 미설정 422 BUSINESS_RULE** 을 컨트롤러 단위 테스트로 고정했습니다.
- **내 화면/업무에 영향**: 없음 — API 동작·오류 형식은 기존과 동일
- **상태**: 완료

<details><summary>자세히</summary>

- `AccountingBpoControllerTest` — `@WebMvcTest` · HQ_ADMIN 200 · credentials missing → **422** · `error.code=BUSINESS_RULE`
- 회귀: `AccountingBpoServiceTest` · `HealthControllerTest` carry

</details>

### 📝 G2 가정통신문 진입·발송 이력 ops 문서화
- **에이전트**: TWR
- **한 일**: develop HEAD 실측 후 FAQ·매뉴얼·관리/배포 가이드에 **가정통신문 진입 화면**·**발송 이력 API**·**health 준비 필드**를 반영했습니다.
- **내 화면/업무에 영향**: 없음 — 문서·운영 가이드만 갱신
- **상태**: 완료

<details><summary>자세히</summary>

- 실측: BE·FE develop — **132 route** · **105 page** · Flyway **V1–V190** · 모듈 커버리지 **~92.4%**
- FAQ Q217 정정 · **Q788**·**Q789** · USER_MANUAL §4-7-3a · ADMIN §6-2-24h · DEPLOYMENT 스모크

</details>

### ✅ G2 가정통신문 진입·발송 이력 화면 (FE)
- **에이전트**: COD
- **한 일**: SideNav **이용자 → 가정통신문**(`/clients/home-newsletter`)에서 **운영 준비·연계 안내·지점별 발송 이력**을 한 화면으로 볼 수 있게 했습니다. 실제 발송은 기존처럼 **이용자 상세**에서 합니다. **작성·게시판 UI는 아직 후속**입니다.
- **내 화면/업무에 영향**: **센터장·사회복지사** — 가정통신문 준비 상태와 **최근 발송 목록**을 메뉴에서 바로 확인. 요양보호사는 권한상 메뉴 진입 불가
- **상태**: 완료

<details><summary>자세히</summary>

- `HomeNewsletterLaunchPage` · `homeNewsletter.js` · ClientsContextNav·SideNav
- API: `GET …/home-newsletter/launch` · `GET …/dispatch-history` · `GET /api/v1/health` 병합
- 회귀: `HomeNewsletterLaunchPage.test` · `homeNewsletter.test` · `competitorModuleCoverage.test`

</details>

### ✅ G2 가정통신문 발송 이력 API (BE)
- **에이전트**: COD
- **한 일**: **`GET /api/v1/notifications/home-newsletter/dispatch-history`** 로 지점 범위의 **가정통신문 이메일 발송 기록**을 페이지 단위로 조회합니다. 개인 연락처는 응답에 넣지 않습니다.
- **내 화면/업무에 영향**: **센터장·사회복지사** — `/clients/home-newsletter` 하단에 **발송 시각·이용자명·연월·상태** 표가 채워짐
- **상태**: 완료

<details><summary>자세히</summary>

- 템플릿 `HOME_NEWSLETTER` · 지점 스코프 · `page`/`size`(기본 20·최대 100)
- 권한: `hq_admin`·`branch_admin`·`social_worker`
- 회귀: `GuardianHomeNewsletterDispatchHistoryServiceTest` · routing·RBAC

</details>

### ✅ G2 가정통신문 launch catalog·health readiness (BE)
- **에이전트**: COD
- **한 일**: **`GET /api/v1/notifications/home-newsletter/launch`** 로 가정통신문 **진입 안내·이메일 발송 준비**를 내리고, **`GET /api/v1/health`** 에 **가정통신문 readiness** 필드를 추가했습니다. SMTP가 준비되면 dispatch가 **AVAILABLE**로 바뀝니다.
- **내 화면/업무에 영향**: 없음 — **IT·배포**가 health로 이메일 준비 점검. 현장은 진입 화면의 운영 준비 카드로 동일 상태를 봄
- **상태**: 완료

<details><summary>자세히</summary>

- health: `homeNewsletterCatalogAvailable` · `homeNewsletterDispatchReady` · `homeNewsletterDispatchAvailability` · `homeNewsletterAuthoringAvailability` · `homeNewsletterReadinessBlockers[]`
- blocker 예: `email-dispatch-not-ready` · `home-newsletter-status-error`
- 회귀: `GuardianHomeNewsletterLaunchServiceTest` · `HealthControllerTest`

</details>

### ✅ M12 외부 포털 새 창 안내 (a11y)
- **에이전트**: UXD
- **한 일**: 재무회계 **수지파인 열기** 링크에 스크린리더용 **「새 탭」** 안내를 넣었습니다.
- **내 화면/업무에 영향**: **스크린리더 사용자** — `/accounting` 에서 외부 포털이 **새 탭**으로 열림을 미리 알 수 있음. 시각적 변화는 거의 없음
- **상태**: 완료

<details><summary>자세히</summary>

- `AccountingBpoPage` — 외부 링크 `aria`/`sr-only` 새 탭 안내
- 회귀: `AccountingBpoPage.test`

</details>

### 📝 M12 SSO handoff BE·자격 env ops 문서화
- **에이전트**: TWR
- **한 일**: develop HEAD 실측 후 FAQ·매뉴얼·관리/배포 가이드에 **재무회계 SSO OTP handoff API**·**기관 자격 환경변수**·**blocker `sso-otp-credentials-missing`** 를 반영했습니다.
- **내 화면/업무에 영향**: 없음 — 문서·운영 가이드만 갱신
- **상태**: 완료

<details><summary>자세히</summary>

- 실측(당시): BE·FE develop — **131 route** · **104 page** · Flyway **V1–V190** · 모듈 커버리지 **~91.9%**
- FAQ Q782·Q784·Q785 정정 · **Q787** · USER_MANUAL §4-6-5 · ADMIN §6-2-24f/g · DEPLOYMENT env·스모크

</details>

### ✅ M12 재무회계 SSO OTP handoff API (BE)
- **에이전트**: COD
- **한 일**: **`POST /api/v1/billing/accounting/bpo-sso-handoff`** 로 케어포처럼 **기관 usmusid + 일회용 OTP** 를 내려줍니다. **`ACCOUNTING_BPO_USMUSID`·`ACCOUNTING_BPO_OTP_SECRET`** 가 있으면 SSO가 **AVAILABLE** 되고, 없으면 health blocker만 바뀝니다. **비밀번호는 저장·반환하지 않습니다**.
- **내 화면/업무에 영향**: **센터장·사회복지사** — 기관 자격을 IT가 env에 넣으면 **`/accounting`** 에 **「SSO 자동 로그인」** 이 보입니다. **미설정 시 공개 로그인만**(화면 변화 작음)
- **상태**: 완료

<details><summary>자세히</summary>

- API: `POST …/bpo-sso-handoff` — `usmusid` · `otp` · `ssoPortalUrl`(기본 `carefor_login`) · `handoffReady`
- health: `accountingBpoSsoReady` · `accountingBpoSsoAvailability` · blocker **`sso-otp-credentials-missing`**
- OTP: HMAC-SHA256 · 5분 창 · hex 16자
- 권한: `hq_admin`·`branch_admin`·`social_worker`
- 회귀: `AccountingBpoServiceTest` · `HealthControllerTest` · `MustApiEndpointRoutingTest`

</details>

### ✅ M12 SSO blocker·모듈 커버리지 정합 (FE)
- **에이전트**: COD
- **한 일**: health blocker 문구를 BE와 같이 **`sso-otp-credentials-missing`** 로 맞추고, 경쟁사 모듈 표에서 **재무회계(M12)** 커버리지를 SSO handoff full-stack 반영값으로 올렸습니다.
- **내 화면/업무에 영향**: **센터장·사회복지사** — **`/accounting`** 운영 준비에서 SSO 미설정 안내가 **「자격 미설정」** 톤으로 명확해짐. 업무 절차 자체는 동일
- **상태**: 완료

<details><summary>자세히</summary>

- `accountingBpo.js` — blocker 상수 `ACCOUNTING_BPO_SSO_BLOCKER_CREDENTIALS_MISSING`
- `competitorModuleCoverage` — id=12 **0.7** · id=1-5 **0.5** · 가중 **~91.9%**
- 회귀: `AccountingBpoPage.test` · `accountingBpo.test` · `competitorModuleCoverage.test`

</details>

### 📝 M12 SSO·health 연동 · 송영 readiness 분리 ops 문서화
- **에이전트**: TWR
- **한 일**: develop HEAD 실측 후 FAQ·매뉴얼·관리/배포 가이드에 **재무회계 SSO OTP 어댑터(FE)**·**`/accounting` health 연동**·**송영 V189/V190 health 필드 분리**를 반영했습니다.
- **내 화면/업무에 영향**: 없음 — 문서·운영 가이드만 갱신
- **상태**: 완료

<details><summary>자세히</summary>

- baseline 실측: BE develop · FE develop — **131 route** · **104 page** · Flyway **V1–V190**
- FAQ Q782·Q784·Q771 정정 · **Q785** · **Q786** · USER_MANUAL §4-6-5 · ADMIN §6-2-24f/g · DEPLOYMENT 스모크

</details>

### ✅ M12 재무회계 BPO health readiness 화면 연동 (FE)
- **에이전트**: COD
- **한 일**: **`/accounting`** 이 **`GET /api/v1/health`** 의 재무회계 BPO 필드를 **카탈로그와 함께** 읽어, **운영 준비(카탈로그·공개 진입·SSO)** 상태를 카드에 표시합니다. SSO 가능 여부는 health가 우선합니다.
- **내 화면/업무에 영향**: **센터장·사회복지사** — **`/accounting`** 에 **「운영 준비 (/health)」** 요약이 추가됨. **공개 로그인 자체는 동일**(SSO는 아직 후속)
- **상태**: 완료

<details><summary>자세히</summary>

- `AccountingBpoPage` — `fetchSystemHealthApi()` · `normalizeAccountingBpoHealthReadiness()` · `mergeAccountingBpoLaunchWithHealth()`
- 회귀: `AccountingBpoPage.test` · `accountingBpo.test`

</details>

### ✅ M12 재무회계 SSO OTP 어댑터 (FE)
- **에이전트**: COD
- **한 일**: 케어포 **`open_sujifine()`** 와 같이 **기관 usmusid+OTP** 를 수지파인 **`carefor_login`** 으로 POST하는 SSO handoff 흐름을 프론트에 넣었습니다. **BE가 SSO를 PLANNED로 두면** 기존처럼 **공개 로그인만** 엽니다. **비밀번호는 ogada에 저장하지 않습니다**.
- **내 화면/업무에 영향**: **센터장·사회복지사** — 지금은 **「수지파인 공개 로그인 열기」** 만 사용. BE SSO 준비 후 **「SSO 자동 로그인」** 버튼이 노출됩니다
- **상태**: 완료

<details><summary>자세히</summary>

- `launchAccountingBpoPortal()` · `submitAccountingBpoSsoPortal()` · `POST /api/v1/billing/accounting/bpo-sso-handoff`(BE 후속)
- SSO URL 기본: `https://www.sujifine.co.kr/carefor_login`
- 회귀: `AccountingBpoPage.test` · `accountingBpo.test`

</details>

### ✅ 송영 health readiness V189·V190 분리 (BE)
- **에이전트**: COD
- **한 일**: 이동 송영 **스키마(V186–V189)** 와 **무결성(V190)** 을 health·live probe에서 **서로 다른 준비 플래그·blocker**로 나눴습니다. 예전처럼 한 신호로 묶이지 않습니다.
- **내 화면/업무에 영향**: 없음 — **IT·배포**가 마이그레이션 누락을 **스키마 vs 무결성**으로 구분 진단. 현장 배차 화면 변화 없음
- **상태**: 완료

<details><summary>자세히</summary>

- 필드: `v189TransportShuttleSchemaCheckReady` · `v190TransportShuttleIntegrityCheckReady`
- blocker: `v189-transport-shuttle-schema-missing` · `v190-transport-shuttle-integrity-missing`
- live E2E·`LiveE2eOperationReadinessSupport` 동일 분리
- 회귀: `HealthControllerTest` · `V189TransportShuttleSchemaReadinessProbeTest` · `LiveE2eControllerTest`

</details>

### 📝 M12 BPO API·health ops 문서화
- **에이전트**: TWR
- **한 일**: develop HEAD 실측 후 FAQ·매뉴얼·관리/배포 가이드에 **재무회계 BPO API 연동 화면**·**BPO readiness health**를 반영했습니다.
- **내 화면/업무에 영향**: 없음 — 문서·운영 가이드만 갱신
- **상태**: 완료

<details><summary>자세히</summary>

- baseline 실측: BE develop · FE develop — **131 route** · **104 page** · Flyway **V1–V190**
- FAQ Q782 정정 · **Q784** · USER_MANUAL §4-6-5 · ADMIN §6-2-24f/g · DEPLOYMENT 스모크

</details>

### ✅ M12 재무회계 BPO readiness health (BE)
- **에이전트**: COD
- **한 일**: **`GET /api/v1/health`** 에 **재무회계 BPO(수지파인) 준비 여부**를 추가했습니다. J03 알림 readiness와 같은 패턴으로 **포털 진입·SSO·blocker 코드**만 노출합니다.
- **내 화면/업무에 영향**: 없음 — **IT·배포**가 health로 BPO/SSO 전환 전 점검. 현장 화면 변화 없음
- **상태**: 완료

<details><summary>자세히</summary>

- 필드: `accountingBpoCatalogAvailable` · `accountingBpoPortalLaunchReady` · `accountingBpoSsoReady` · `accountingBpoSsoAvailability` · `accountingBpoReadinessBlockers[]`
- blocker 예: `sso-otp-adapter-planned` · 서비스 오류 시 `accounting-bpo-status-error`
- 회귀: `HealthControllerTest` · `AccountingBpoServiceTest`

</details>

### ✅ M12 재무회계 BPO 카탈로그 API 연동 (FE)
- **에이전트**: COD
- **한 일**: **`/accounting`** 화면이 **`GET /api/v1/billing/accounting/bpo-launch`** 응답을 **실제 조회**해 포털 제목·URL·연계 화면을 표시합니다. 하드코딩 metadata를 제거했습니다.
- **내 화면/업무에 영향**: **센터장·사회복지사** — **`/accounting`** 에서 API와 동일한 **포털 안내·연계 링크**가 표시됨. **수지파인 로그인 동작은 동일**
- **상태**: 완료

<details><summary>자세히</summary>

- `AccountingBpoPage` — `fetchAccountingBpoLaunchApi()` · `normalizeAccountingBpoLaunch()`
- 권한: `hq_admin`·`branch_admin`·`social_worker`
- 회귀: `AccountingBpoPage.test` · `accountingBpo.test`

</details>

### 📝 M11 퇴직적립·M12 BPO·J03 health ops 문서화
- **에이전트**: TWR
- **한 일**: develop HEAD 실측 후 FAQ·매뉴얼·관리/배포 가이드에 **퇴직적립금 화면**·**재무회계 BPO 진입**·**알림 채널 readiness health**를 반영했습니다.
- **내 화면/업무에 영향**: 없음 — 문서·운영 가이드만 갱신
- **상태**: 완료

<details><summary>자세히</summary>

- baseline 실측: BE develop · FE develop — **129 route** · **104 page** · Flyway **V1–V190** · StaffContextNav **17탭**
- FAQ Q781 정정 · **Q782** · **Q783** · USER_MANUAL §4-6-5 · §4-7-0i · ADMIN §6-2-24d/e/f · DEPLOYMENT 스모크

</details>

### ✅ M12 재무회계 BPO 카탈로그 API (BE)
- **에이전트**: COD
- **한 일**: 케어포 **M12 수입지출**과 같이 **외부 BPO(수지파인)** 진입 정보를 **`GET /api/v1/billing/accounting/bpo-launch`** 로 제공합니다. 포털 URL·안내 문구·연계 화면(급여대장·본인부담 청구)을 돌려줍니다. **SSO 자동 로그인은 아직 없음**.
- **내 화면/업무에 영향**: 없음 — **센터장·사회복지사**는 Swagger 등으로만 조회 가능. **`/accounting` 화면은 FE 카드 참고**
- **상태**: 완료

<details><summary>자세히</summary>

- `GET /api/v1/billing/accounting/bpo-launch` — `documentCode=M12-BPO` · `portalUrl=https://sujifine.co.kr/login` · `ssoAvailability=PLANNED`
- `relatedSurfaces[]` — `/payroll/ledger` · `/billing` · `/accounting`
- 권한: `hq_admin`·`branch_admin`·`social_worker`
- 회귀: `AccountingBpoServiceTest` · `MustApiEndpointRoutingTest` · `RoleBasedControllerAccessTest`

</details>

### ✅ M12 재무회계 BPO 진입 화면 (FE)
- **에이전트**: COD
- **한 일**: 케어포 **`open_sujifine()`** 와 같이 **수지파인 공개 로그인**으로 연결하는 **`/accounting`** 화면을 추가했습니다. ogada에 비밀번호를 입력하지 않고 **새 창**으로 포털만 엽니다.
- **내 화면/업무에 영향**: **센터장·사회복지사** — SideNav **청구 → 재무회계 (BPO)** 또는 **`BillingContextNav`「재무회계 (BPO)」**. **수입·지출·결의는 수지파인에서 처리**
- **상태**: 완료

<details><summary>자세히</summary>

- `AccountingBpoPage` — `openAccountingBpoPortal()` · **`BillingContextNav`** 5탭
- 권한: `hq_admin`·`branch_admin`·`social_worker`
- 회귀: `AccountingBpoPage.test` · `accountingBpo.test` · `competitorModuleCoverage.test`

</details>

### ✅ M11 퇴직적립금 미리보기 화면 (FE)
- **에이전트**: COD
- **한 일**: 퇴직적립금 미리보기 API를 **`/payroll/retirement-accrual`** 화면에 연결했습니다. 급여 월·적립기준 급여·이전 잔여·근속 개월을 넣으면 **당월 적립(1/12)**·**예상 누적**·**적립 가능 여부**를 바로 볼 수 있습니다.
- **내 화면/업무에 영향**: **센터장·사회복지사** — SideNav **운영 → 퇴직적립금** 또는 **`StaffContextNav`「퇴직적립금」**. **저장·4대보험 연동은 아직 없음**(미리보기 전용)
- **상태**: 완료

<details><summary>자세히</summary>

- `StaffPayrollRetirementAccrualPage` — `POST …/retirement-accrual-preview`
- 권한: `hq_admin`·`branch_admin`·`social_worker`
- 회귀: `StaffPayrollRetirementAccrualPage.test` · `staffPayrollServices.test`

</details>

### ✅ J03 알림 채널 readiness health 노출 (BE)
- **에이전트**: COD
- **한 일**: **`GET /api/v1/health`** 에 Solapi 알림톡·SMS·이메일 **live 발송 준비 여부**를 추가했습니다. 비밀값은 노출하지 않고 **blocker 코드**만 표시합니다.
- **내 화면/업무에 영향**: 없음 — **IT·배포**가 health로 알림 live 전환 전 점검. 현장 화면 변화 없음
- **상태**: 완료

<details><summary>자세히</summary>

- 필드: `notificationChannelStatusAvailable` · `notificationLiveAlimtalkDispatchReady` · `notificationLiveEmailDispatchReady` · `notificationReadinessBlockers[]`
- blocker 예: `missing-solapi-config` · `missing-smtp-config` · `channel-status-unavailable`
- 회귀: `HealthControllerTest` · `NotificationChannelStatusPilotServiceFlowE2eTest`

</details>

### 📝 M11 인건비비율 화면·퇴직적립 API ops 문서화
- **에이전트**: TWR
- **한 일**: develop HEAD 실측 후 FAQ·매뉴얼·관리/배포 가이드에 **인건비 지출비율 화면**·**퇴직적립금 미리보기 API**를 반영했습니다. **퇴직적립 화면(`/payroll/retirement-accrual`)은 아직 없음**을 명시했습니다.
- **내 화면/업무에 영향**: 없음 — 문서·운영 가이드만 갱신
- **상태**: 완료

<details><summary>자세히</summary>

- baseline 실측: BE develop · FE develop — **127 route** · **103 page** · Flyway **V1–V190** · StaffContextNav **16탭**
- FAQ Q780 정정 · **Q781** · USER_MANUAL §4-7-0h/i · ADMIN §6-2-24d/e · DEPLOYMENT 스모크

</details>

### ✅ M11 급여 미리보기 4화면 접근성 보강 (FE)
- **에이전트**: UXD
- **한 일**: 급여대장·간이지급·급여기초·인건비 지출비율 화면의 요약 목록·월 입력·도움말·제출 중 상태를 접근성 규칙에 맞춰 다듬었습니다. 계산 결과는 같고, 키보드·스크린리더 이용이 더 안정적입니다.
- **내 화면/업무에 영향**: **센터장·사회복지사** — `/payroll/ledger`·`/reports`·`/basis`·`/labor-cost-ratio` 에서 월 선택·도움말·계산 중 표시가 더 분명함
- **상태**: 완료

<details><summary>자세히</summary>

- `.ds-summary-list` · `Field` `help` · `MonthInput` · form `aria-label` · submit `aria-busy`
- 회귀: 급여 4페이지 a11y 단언

</details>

### ✅ M11 퇴직적립금 미리보기 API (BE)
- **에이전트**: COD
- **한 일**: 케어포 **11-2 퇴직적립금** 미리보기 API를 추가했습니다. 급여 월·적립기준 급여·이전 잔여·근속 개월을 넣으면 **당월 적립액(1/12)**·**예상 누적**·**적립 가능 여부**를 돌려줍니다. **화면은 아직 없음**(Swagger·연동 테스트용).
- **내 화면/업무에 영향**: 없음 — **센터장·사회복지사**는 Swagger 등으로만 호출 가능. **`/payroll/retirement-accrual` 화면은 예정**
- **상태**: 완료

<details><summary>자세히</summary>

- `POST /api/v1/staff/payroll/retirement-accrual-preview` — `yearMonth` · `accrualBasePay` · `priorAccumulatedBalance` · `continuousServiceMonths`
- 응답: `monthlyAccrualAmount` · `projectedAccumulatedBalance` · `accrualEligible` · `riskLevel`(`ACCRUING`/`INELIGIBLE`) · `documentCode=M11-2`
- 규칙: 근속 **1개월 이상**만 당월 적립 · 미만이면 당월 0·잔여 유지
- 권한: `hq_admin`·`branch_admin`·`social_worker`
- 회귀: `StaffPayrollLedgerServiceTest` · `MustApiEndpointRoutingTest` · `RoleBasedControllerAccessTest`

</details>

### ✅ M11 인건비 지출비율 준수 화면 (FE)
- **에이전트**: COD
- **한 일**: 인건비 지출비율 60% 미리보기 API를 **`/payroll/labor-cost-ratio`** 화면에 연결했습니다. 급여 월·직접인건비·요양수익을 넣으면 **지출비율(%)**·**충족 여부**·**안내 문구**를 바로 볼 수 있습니다.
- **내 화면/업무에 영향**: **센터장·사회복지사** — SideNav **운영 → 인건비 지출비율** 또는 **`StaffContextNav`「인건비 지출비율」**. **자동 집계·저장은 아직 없음**(수동 입력 미리보기)
- **상태**: 완료

<details><summary>자세히</summary>

- `StaffPayrollLaborCostRatioPage` — `POST …/labor-cost-ratio-preview`
- 권한: `hq_admin`·`branch_admin`·`social_worker`
- 회귀: `StaffPayrollLaborCostRatioPage.test` · `staffPayrollServices.test`

</details>

### 📝 M11 인건비 지출비율 API 초기 ops 문서화
- **에이전트**: TWR
- **한 일**: 인건비 지출비율 **API만** 착지 시점에 FAQ·매뉴얼에 반영했습니다. (이후 **화면 연결**은 위 FE·TWR 카드)
- **내 화면/업무에 영향**: 없음 — 문서만
- **상태**: 완료

<details><summary>자세히</summary>

- FAQ Q780 초안 · USER_MANUAL §4-7-0h · ADMIN §6-2-24d

</details>

### ✅ M11 인건비 지출비율 준수 미리보기 API (BE)
- **에이전트**: COD
- **한 일**: 케어포 **11-5 인건비 지출비율** 준수 미리보기 API를 추가했습니다. 급여 월·직접인건비·요양수익을 넣으면 **지출비율(%)**·**60% 기준 충족 여부**·**안내 문구**를 돌려줍니다. **화면은 아직 없음**(Swagger·연동 테스트용).
- **내 화면/업무에 영향**: 없음 — **센터장·사회복지사**는 Swagger 등으로만 호출 가능. **`/payroll/labor-cost-ratio` 화면은 예정**
- **상태**: 완료

<details><summary>자세히</summary>

- `POST /api/v1/staff/payroll/labor-cost-ratio-preview` — `yearMonth` · `totalLaborCost` · `totalCareRevenue`
- 응답: `laborCostRatioPercent` · `statutoryThresholdPercent=60` · `complianceMet` · `riskLevel` · `guidance` · `documentCode=M11-5`
- 권한: `hq_admin`·`branch_admin`·`social_worker`
- 회귀: `StaffPayrollLedgerServiceTest` · `MustApiEndpointRoutingTest` · `RoleBasedControllerAccessTest`

</details>

### ✅ M11 간이지급명세서 화면 (FE)
- **에이전트**: COD
- **한 일**: 간이지급명세서 미리보기 API를 **`/payroll/reports`** 화면에 연결했습니다. 급여대장과 같이 직원·급여 월·기본급·수당·공제를 넣으면 **지급·공제 라인**과 **실지급액**을 바로 볼 수 있습니다.
- **내 화면/업무에 영향**: **센터장·사회복지사** — SideNav **운영 → 간이지급명세서** 또는 **`StaffContextNav`「간이지급명세서」**. **저장·PDF 출력은 아직 없음**(미리보기 전용)
- **상태**: 완료

<details><summary>자세히</summary>

- `StaffPayrollReportsPage` — `POST …/simple-payment-statement-preview`
- 권한: `hq_admin`·`branch_admin`·`social_worker`
- 회귀: `StaffPayrollReportsPage.test` · `staffPayrollServices.test`

</details>

### ✅ M11 급여기초 설정 — 수당/공제 마스터 (BE+FE)
- **에이전트**: COD
- **한 일**: 케어포 **11-4 급여기초 설정**용 **수당·공제 마스터 카탈로그** API와 **`/payroll/basis`** 화면을 추가했습니다. 수당 3종·공제 6종(4대보험·소득세·지방소득세)을 조회할 수 있습니다. **항목 편집·DB 저장은 아직 없음**(정적 목록).
- **내 화면/업무에 영향**: **센터장·사회복지사** — SideNav **운영 → 급여기초 설정** 또는 **`StaffContextNav`「급여기초 설정」** 에서 마스터 항목 확인
- **상태**: 완료

<details><summary>자세히</summary>

- `GET /api/v1/staff/payroll/allowance-deduction-catalog` — `documentCode=M11-4` · 수당 3 · 공제 6
- `StaffPayrollBasisPage` · `StaffPayrollAllowanceDeductionCatalog`
- 회귀: `StaffPayrollAllowanceDeductionCatalogTest` · `StaffPayrollBasisPage.test`

</details>

### 📝 M11 간이지급·급여기초 ops 문서화
- **에이전트**: TWR
- **한 일**: develop HEAD 실측 후 FAQ·매뉴얼·관리/배포 가이드에 **간이지급명세서 화면**·**급여기초 설정**·**StaffContextNav 15탭**을 반영했습니다.
- **내 화면/업무에 영향**: 없음 — 문서·운영 가이드만 갱신
- **상태**: 완료

<details><summary>자세히</summary>

- baseline 실측: BE develop · FE develop — **127 route** · **101 page** · Flyway **V1–V190**
- FAQ · USER_MANUAL §4-7-0e/f/g · ADMIN §6-2-24a/b/c · DEPLOYMENT 스모크

</details>

### ✅ M11 직원 급여대장 화면 (FE)
- **에이전트**: COD
- **한 일**: 케어포 **11-1·11-3** 급여대장 미리보기 API를 **`/payroll/ledger`** 화면에 연결했습니다. 직원·급여 월·기본급·수당·공제를 입력하면 **출근일수**·**지급총액**·**실지급액**을 바로 확인할 수 있습니다.
- **내 화면/업무에 영향**: **센터장·사회복지사** — SideNav **운영 → 직원 급여대장** 또는 **`StaffContextNav`「직원 급여대장」** 에서 월별 급여를 미리 계산. **저장·확정·명세서 출력은 아직 없음**(미리보기 전용)
- **상태**: 완료

<details><summary>자세히</summary>

- `StaffPayrollLedgerPage` · `StaffPayrollRelatedSurfacesPanel` — 출퇴근·근로계약 cross-link
- 권한: `hq_admin`·`branch_admin`·`social_worker` · `caregiver` 접근 시 안내 Alert
- 회귀: `StaffPayrollLedgerPage.test` · `staffPayrollLedger.test` · `StaffContextNav.test`

</details>

### ✅ M11 간이지급명세서 미리보기 API (BE)
- **에이전트**: COD
- **한 일**: 케어포 **11-6 간이지급명세서** 미리보기 API를 추가했습니다. 급여대장과 동일 입력으로 **지급·공제 라인**·**합계**·**실지급액**을 돌려줍니다. **화면은 `/payroll/reports`에 연결됨**(위 FE 카드).
- **내 화면/업무에 영향**: **센터장·사회복지사** — **`/payroll/reports`** 에서 동일 API 사용
- **상태**: 완료

<details><summary>자세히</summary>

- `POST /api/v1/staff/payroll/simple-payment-statement-preview` — ledger-preview와 동일 요청 body
- 응답: `paymentLines[]` · `deductionLines[]` · `paymentTotal` · `deductionTotal` · `netPay` · `documentTitle=간이지급명세서`
- 회귀: `StaffPayrollLedgerServiceTest`

</details>

### 📝 M11 급여대장·간이지급 API 초기 ops 문서화
- **에이전트**: TWR
- **한 일**: 급여대장 화면·간이지급 API 착지 시점에 FAQ·매뉴얼·관리/배포 가이드를 먼저 맞췄습니다. (이후 간이지급·급여기초 화면 문서화는 위 카드)
- **내 화면/업무에 영향**: 없음 — 문서만
- **상태**: 완료

<details><summary>자세히</summary>

- USER_MANUAL §4-7-0e · ADMIN §6-2-24a/b 초안

</details>

### ✅ M11 직원 급여대장 미리보기 API (BE)
- **에이전트**: COD
- **한 일**: 케어포 **11-1 월별 급여대장**·**11-3 수당/공제** 최소 세트의 첫 API를 추가했습니다. 직원 1명·연월·기본급·수당·공제를 넣으면 **출근일수**·**지급총액**·**실지급액**을 계산해 돌려줍니다.
- **내 화면/업무에 영향**: **센터장·사회복지사** — **`/payroll/ledger`** 화면에서 동일 API를 사용 (아래 FE 카드)
- **상태**: 완료

<details><summary>자세히</summary>

- `POST /api/v1/staff/payroll/ledger-preview` — `hq_admin`·`branch_admin`·`social_worker`
- 요청: `userId` · `yearMonth`(yyyy-MM) · `basePay` · `allowances` · `deductions`
- 응답: `attendanceDays` · `grossPay` · `netPay` · `relatedSurfaces[]`(출퇴근·근로계약)
- 가드: 공제>지급총액 **422** · 비직원 역할 **422** · 지점 스코프 검증
- 회귀: `StaffPayrollLedgerServiceTest`

</details>

### ✅ 기능회복 compliance — 지표 27 소유 메타데이터 (BE)
- **에이전트**: COD
- **한 일**: `GET /programs/functional-recovery/compliance` 응답에 **`indicator27Code`·`indicator27Label`·`scopeNote`·`daycareEvaluationRequired`** 를 넣어 **주야간 평가 지표 27=기능회복**과 **목욕 청구 준수**를 API에서 구분할 수 있게 했습니다.
- **내 화면/업무에 영향**: 없음 — 기능회복 화면 각주·링크가 이 필드를 사용 (아래 FE 카드)
- **상태**: 완료

<details><summary>자세히</summary>

- `FunctionalRecoveryComplianceResponse` — owner `FUNCTIONAL_RECOVERY` · scopeNote에 G-BATHING 안내
- 회귀: `FunctionalRecoveryServiceTest` · `MustApiEndpointRoutingTest`

</details>

### ✅ 기능회복↔목욕 청구 준수 — 화면 상호 링크 (FE)
- **에이전트**: COD
- **한 일**: **목욕 일정** 패널 제목을 **「목욕 청구 준수」** 로 바꾸고 각주·**기능회복훈련(평가지표 27)로 이동** 링크를 넣었습니다. **기능회복훈련** 화면에도 **목욕 청구 준수 보기** 링크와 `scopeNote`를 표시합니다.
- **내 화면/업무에 영향**: **요양보호사·사회복지사** — `/care/bathing-schedules` 패널 제목·각주·링크 변경 · `/programs/functional-recovery` 준수 현황 아래 상호 링크
- **상태**: 완료

<details><summary>자세히</summary>

- `BathingScheduleIndicator27Panel` — `BATHING_CLAIM_COMPLIANCE` · `scopeNote` · deep-link
- `FunctionalRecoveryPage` · `functionalRecoveryCompliance.js`
- 회귀: `BathingScheduleIndicator27Panel.test` · `FunctionalRecoveryPage.test` · `functionalRecoveryCompliance.test`

</details>

### ✅ 금일 배차 제외 명단 — 행 배경 시각 구분 (FE)
- **에이전트**: UXD
- **한 일**: 수동 배차 **「명단에서 추가」**·**수동 배차 생성**에서 **금일 배차 제외** 이용자 행에 경고 톤 배경·테두리를 추가했습니다. **「금일 배차 제외」** Badge가 주 신호이고, 색만으로 의미를 전달하지 않습니다.
- **내 화면/업무에 영향**: **통합 관리자** — `/transport/runs/new`·루트 상세 명단에서 제외 이용자 행이 일반 잠금 행과 시각적으로 구분됨
- **상태**: 완료

<details><summary>자세히</summary>

- `.ds-transport-roster-item--excluded` — `components.css` (UXD-173)
- 대상: `TransportAddRosterModal` · `TransportRunNewPage`

</details>

### 📝 M11·G17 상호 링크·배차 제외 시각 ops 문서화
- **에이전트**: TWR
- **한 일**: develop HEAD 실측 후 FAQ·매뉴얼·관리/배포 가이드에 **급여대장 미리보기 API**·**기능회복↔목욕 링크**·**목욕 패널 제목 정정**·**배차 제외 행 스타일**을 반영했습니다.
- **내 화면/업무에 영향**: 없음 — 문서·운영 가이드만 갱신
- **상태**: 완료

<details><summary>자세히</summary>

- baseline: BE `5beaffb` · FE `bc9389d` — **124 route** · Flyway **V1–V190**
- FAQ **Q775**(M11 preview) · **Q776**(G17 cross-link) · **Q777**(배차 제외 시각) · Q774 정정

</details>

### ✅ 목욕 일정 패널 — 지표 27=기능회복 안내 문구 (FE)
- **에이전트**: COD
- **한 일**: **`/care/bathing-schedules`** 상단 패널·카드 제목과 각주를 **「평가지표 27 — 기능회복훈련 준수」** 로 맞추고, **평가 지표 27은 기능회복훈련**·**목욕은 청구 시 선택 준수**임을 화면에서 안내합니다. API·집계 데이터는 **목욕 청구 준수**(`BATHING_CLAIM_COMPLIANCE`) 그대로입니다.
- **내 화면/업무에 영향**: **요양보호사·사회복지사** — 목욕 일정 화면 패널 제목·안내 문구가 바뀝니다. 표의 **완료 횟수·전·후 관찰·월 5회**는 **목욕 제공** 기준입니다. **공단평가 지표 27** 점검은 **`/programs/functional-recovery`** 로 이동하세요 (Q773·Q774).
- **상태**: 완료

<details><summary>자세히</summary>

- `BathingScheduleIndicator27Panel` · `BathingSchedulePage` — 제목·각주·오류 메시지
- API 경로 `…/indicator-27-compliance` 유지 · 응답 `indicatorCode=BATHING_CLAIM_COMPLIANCE`
- 회귀: `BathingScheduleIndicator27Panel.test` · `BathingSchedulePage.test`

</details>

### ✅ 주야간 평가지표 27 — 기능회복훈련이 정본 (BE)
- **에이전트**: COD
- **한 일**: 주야간보호 **공단평가 지표 27**의 소유를 **기능회복훈련**으로 명확히 했습니다. 목욕 일정 compliance는 **청구 시 선택 준수**(`BATHING_CLAIM_COMPLIANCE`)이며, 평가 필수 지표가 아닙니다. API 경로 이름(`…/indicator-27-compliance`)은 호환을 위해 유지합니다.
- **내 화면/업무에 영향**: **센터장·사회복지사** — 공단평가 **지표 27** 점검은 **`/programs/functional-recovery`**. **`/care/bathing-schedules`** 상단 패널은 **목욕을 제공할 때** 월 5회·전후 관찰을 챙기는 **청구 준수**용. 목욕을 안 해도 지표 27 미충족으로 보지 않음
- **상태**: 완료

<details><summary>자세히</summary>

- `FunctionalRecoveryIndicatorCatalog` — INDICATOR_25~27 · scope note
- `BathingScheduleIndicator27Catalog` — `COMPLIANCE_CODE=BATHING_CLAIM_COMPLIANCE` · `daycareEvaluationRequired=false` · owner `FUNCTIONAL_RECOVERY`
- 응답 필드: `daycareEvaluationRequired` · `daycareEvaluationIndicator27Owner` · `scopeNote`
- 회귀: `FunctionalRecoveryIndicatorCatalogTest` · `BathingScheduleIndicator27ComplianceTest`

</details>

### ✅ 차량 송영 주소 — 비우면 지점 주소로 다시 저장 (FE)
- **에이전트**: COD
- **한 일**: 차량 **수정**에서 송영 시작/종료 주소를 지우면 서버에 **빈 문자열(`""`)** 을 보냅니다. `null`로내면 서버가 필드를 건너뛰어 **옛 주소가 남는** 문제를 고쳤습니다.
- **내 화면/업무에 영향**: **센터장·통합 관리자** — `/transport/vehicles` 에서 주소를 지우고 저장하면 **지점(센터) 주소**로 되돌아감. 신규 등록·공백 정리는 이전과 동일
- **상태**: 완료

<details><summary>자세히</summary>

- `toVehicleShuttleAddressPayload` — blank → `""` (null 금지)
- `VehiclesPage` · `vehicles.test.js` · `VehiclesPage.test.jsx` 회귀

</details>

### 📝 목욕 패널 문구·지표 27 정본 ops 문서화
- **에이전트**: TWR
- **한 일**: develop HEAD(`6e874df`/`95192f5`) 실측 후 FAQ·매뉴얼·관리/배포 가이드에 **목욕 패널 UI 문구 정렬**·**지표 27=기능회복**·**목욕=청구 준수**·**송영 주소 PATCH 빈 문자열**·**live E2E V185/V189 스키마 플래그 게이트**를 반영했습니다.
- **내 화면/업무에 영향**: 없음 — 문서·운영 가이드만 갱신
- **상태**: 완료

<details><summary>자세히</summary>

- baseline: BE `6e874df` · FE `95192f5` — **124 route** · Flyway **V1–V190**
- FAQ **Q774**(목욕 패널 제목 vs 집계) · **Q772** · **Q773** · Q705·Q765 deepen · USER_MANUAL §5-26 · ADMIN/DEPLOYMENT

</details>

---

## 2026-07-13

### ✅ 차량 송영 주소 — 공백·연속 스페이스 정규화 (BE·FE)
- **에이전트**: COD
- **한 일**: 차량 등록·수정 시 송영 시작/종료 주소를 **앞뒤 trim + 연속 공백을 한 칸으로** 맞춥니다. 화면과 서버가 같은 규칙을 쓰고, 비우면 서버가 **지점 주소**로 넣습니다.
- **내 화면/업무에 영향**: **센터장·통합 관리자** — `/transport/vehicles` 에서 주소에 여러 칸 띄어쓰기를 넣어도 저장 후 **정리된 한 줄**로 보임. 공백만 입력하면 **지점 주소**로 저장(이전과 동일)
- **상태**: 완료

<details><summary>자세히</summary>

- BE `VehicleService.normalizeAddress` — trim · `\\s+` → 단일 space · blank→null(지점 폴백)
- FE `normalizeVehicleShuttleAddress` / `toVehicleShuttleAddressPayload` · `VehiclesPage`
- 회귀: `VehicleServiceTest` · `vehicles.test.js` · `VehiclesPage.test.jsx`

</details>

### ✅ 이동 스키마 health — V190 무결성까지 검사 (BE)
- **에이전트**: COD
- **한 일**: 기존 송영 스키마 health가 **V190** 주소 nonempty CHECK·명단 플래그 동기 CHECK·수정자 테넌트 FK까지 확인하도록 넓혔습니다. 빠지면 같은 blocker로 live 점검을 막습니다.
- **내 화면/업무에 영향**: 없음 — IT·QA가 배포 후 `GET /api/v1/health` 로 **V186–V190** 누락을 한 번에 확인. 현장 화면 동일
- **상태**: 완료

<details><summary>자세히</summary>

- `V189TransportShuttleSchemaReadinessProbe` — 검사 **9건**(V186–V189 기본 5 + V190 무결성 4)
- health `v189TransportShuttleSchemaCheckReady` · blocker `v189-transport-shuttle-schema-missing`
- `V189TransportShuttleSchemaReadinessProbeTest` 회귀

</details>

### 📝 송영 주소 정규화·V190 health 확장 ops 문서화
- **에이전트**: TWR
- **한 일**: develop HEAD 실측 후 FAQ·매뉴얼·관리/배포 가이드에 **주소 정규화**와 **V190 health 확장**을 반영했습니다.
- **내 화면/업무에 영향**: 없음 — 문서·운영 가이드만 갱신
- **상태**: 완료

<details><summary>자세히</summary>

- baseline: BE `bd43f59` · FE `654b2c6` — **124 route** · Flyway **V1–V190**
- FAQ **Q770**(주소 정규화) · **Q771**(V190 probe 확장) · USER_MANUAL §5-8-4 · ADMIN/DEPLOYMENT

</details>

### ✅ 금일 배차 제외 — 수동 배차 화면 선택 가드 (FE)
- **에이전트**: COD
- **한 일**: 수동 배차 생성·명단에서 추가·이전 배차 불러오기에서 「금일 배차 제외」 이용자를 **체크 잠금·경고 뱃지·서버와 동일 안내**로 막습니다. 저장 전에 우회를 차단합니다.
- **내 화면/업무에 영향**: **통합 관리자** — `/transport/runs/new`·루트 상세 **「명단에서 추가」** 에서 제외 이용자 체크 불가 · **「금일 배차 제외」** Badge · 클릭 시 **「금일 배차 제외로 표시된 이용자가 포함되어 있습니다: …」** · **이전 배차 불러오기** 시 제외자는 건너뛰기
- **상태**: 완료

<details><summary>자세히</summary>

- `TransportRunNewPage` · `TransportRunDetailPage` · `TransportAddRosterModal`
- `formatDayStatusExcludedClientsMessage` · `isRosterExcludedFromDispatch` · `buildStopsFromPreviousRun` skip 「금일 배차 제외」

</details>

### ✅ 송영 주소·금일 배차 제외 DB 무결성 (BE)
- **에이전트**: COD
- **한 일**: 차량 송영 주소 **공백 문자열**을 DB에서 거부하고, 명단 제외 플래그(`absentToday`=`skipDispatch`)를 **항상 동일**하게 맞추며, 수정자 **테넌트 FK**를 걸었습니다. 빈 송영 주소는 앱이 **지점 주소**로 정규화합니다.
- **내 화면/업무에 영향**: **센터장·통합 관리자** — `/transport/vehicles` 에서 송영 시작/종료 주소를 **공백만** 넣으면 지점 주소로 저장. 현장 배차·송영표 흐름은 동일
- **상태**: 완료

<details><summary>자세히</summary>

- Flyway **V190** — `chk_vehicles_shuttle_*_nonempty` · `chk_transport_roster_day_status_flags_synced` · `fk_…_updated_by_org`
- `VehicleService` blank→branch trim · `VehicleServiceTest` 회귀

</details>

### ✅ 송영표 스크린리더 표 구조 수정 (FE)
- **에이전트**: UXD
- **한 일**: 송영표·스케줄 보드가 잘못된 **표(table) 역할**로 읽히던 문제를 **목록(list)** 구조로 바꿨습니다. 화면 레이아웃은 그대로입니다.
- **내 화면/업무에 영향**: **스크린리더 사용자** — `/transport/shuttle-sheet` 차량 열이 **목록·항목**으로 올바르게 안내됨. 시각적 배치는 변화 없음
- **상태**: 완료

<details><summary>자세히</summary>

- `TransportShuttleScheduleView` · `TransportShuttleSheetView` — `role="list"`/`listitem` · `aria-label="차량별 송영 명단"`

</details>

### 📝 금일 배차 UI 가드·V190·송영표 접근성 ops 문서화
- **에이전트**: TWR
- **한 일**: develop HEAD 실측 후 ops baseline을 갱신하고, FAQ·매뉴얼·관리/배포 가이드에 **수동 배차 UI 잠금**·**V190**·**송영표 a11y**를 반영했습니다.
- **내 화면/업무에 영향**: 없음 — 문서·운영 가이드만 갱신
- **상태**: 완료

<details><summary>자세히</summary>

- baseline: BE `2b3f3d9` · FE `175c570` — **124 route** · Flyway **V1–V190**
- FAQ **Q767**(FE 선택 가드) · **Q768**(V190) · **Q769**(송영표 list a11y) · USER_MANUAL §5-8 · ADMIN/DEPLOYMENT

</details>

### ✅ 금일 배차 제외 — 수동 배차 생성·수정·확정 거부 (BE)
- **에이전트**: COD
- **한 일**: 「금일 배차 제외」 이용자가 정차에 섞여 있으면 **DRAFT 생성·수정·확정**을 서버가 거부합니다. 자동 제안만 막히고 수동으로 우회되던 구멍을 닫았습니다.
- **내 화면/업무에 영향**: **센터장·통합 관리자** — 제외 표시된 이용자를 수동 배차에 넣으면 **「금일 배차 제외로 표시된 이용자가 포함되어 있습니다: …」** 오류로 저장·확정이 막힘. 제외를 해제한 뒤 다시 시도
- **상태**: 완료

<details><summary>자세히</summary>

- `TransportService.validateNoDayStatusExcludedClients` — create · update · confirm
- 회귀: `TransportServiceTest` — 제외 클라이언트 create/update/confirm 거부

</details>

### ✅ 금일 배차 제외 — 전원 제외 시 자동 제안 안내 (BE·FE)
- **에이전트**: COD
- **한 일**: 자동 배차 제안이 제외 명단을 빼는 계약을 테스트로 고정했고, **전원 제외**이면 서버·화면이 같은 안내 문구를 보여 줍니다.
- **내 화면/업무에 영향**: **통합 관리자** — `/transport` 자동 배차에서 **「제안 대상 0/N명 (금일 배차 제외 반영)」** · 경고 **「자동 배차 제안 대상 이용자가 없습니다. 금일 배차 제외 표시를 확인하세요.」** · 제안 버튼 비활성
- **상태**: 완료

<details><summary>자세히</summary>

- BE: `TransportSuggestService` — 전원 day-status 제외 시 `BusinessRuleException` · suggest omit 회귀 lock
- FE: `TransportSuggestPanel` · `TRANSPORT_SUGGEST_ALL_EXCLUDED_MESSAGE` · `TransportPage` `rosterCount`/`totalRosterCount`

</details>

### 📝 금일 배차 제외 강제·전원 제외 안내 ops 문서화
- **에이전트**: TWR
- **한 일**: develop HEAD 실측 후 ops baseline을 갱신하고, FAQ·매뉴얼·관리/배포 가이드에 **수동 배차 거부**와 **전원 제외 suggest 안내**를 추가했습니다.
- **내 화면/업무에 영향**: 없음 — 문서·운영 가이드만 갱신
- **상태**: 완료

<details><summary>자세히</summary>

- baseline: BE `5366944` · FE `d285899` — **124 route** · Flyway **V1–V189**
- FAQ **전원 제외·수동 우회 차단** · USER_MANUAL §5-8 · ADMIN/DEPLOYMENT baseline 정합

</details>

### ✅ 이동서비스 V186–V189 스키마 준비 상태 점검 (BE)
- **에이전트**: COD
- **한 일**: 출발 회차·차량 송영 주소·금일 배차 제외 테이블/컬럼이 DB에 실제로 있는지 health가 검사하고, 빠지면 운영 준비 **blocker**로 표시합니다.
- **내 화면/업무에 영향**: 없음 — IT·QA가 배포·마이그레이션 누락을 조기에 발견. 현장 화면 동작은 동일
- **상태**: 완료

<details><summary>자세히</summary>

- probe: `V189TransportShuttleSchemaReadinessProbe` — 컬럼 5 · 제약 5
- health: `v189TransportShuttleSchemaCheckReady` · blocker `v189-transport-shuttle-schema-missing`
- `HealthController` · `LiveE2eController` · `LiveE2eOperationReadinessSupport` 연동 · 회귀 테스트 잠금

</details>

### ✅ 금일 배차 제외 API 권한·저장 회귀 잠금 (BE)
- **에이전트**: COD
- **한 일**: `PATCH …/roster/{clientId}/day-status` 의 역할별 허용/거부와 저장·해제 경로를 테스트로 고정했습니다.
- **내 화면/업무에 영향**: 없음 — 권한은 기존과 동일(**통합·센터 관리자만** 토글, 요양보호사는 거부)
- **상태**: 완료

<details><summary>자세히</summary>

- `RoleBasedControllerAccessTest` · `TransportControllerRoutingTest` · `TransportServiceTest` — RBAC·persist/clear

</details>

### ✅ 이동·위생 live 점검 스키마 blocker 범위 분리 (FE)
- **에이전트**: COD
- **한 일**: 이동(V189)·위생(V185) 스키마 blocker가 있을 때 **해당 live 스위트만** 건너뛰고, 직원 등 다른 live 점검은 계속 돌리도록 가드를 나눴습니다. 금일 배차 제외 토글 단위 테스트도 보강했습니다.
- **내 화면/업무에 영향**: 없음 — QA·IT 검증 흐름. 현장 화면 동일
- **상태**: 완료

<details><summary>자세히</summary>

- `liveConfig.js` / `liveDescribe.js` — `requireTransportShuttleReady` · `requireSafetyCheckReady`
- `transportLiveApi.e2e` · `safetyCheckLiveApi.e2e` · `TransportPage.test` · harness suite guard

</details>

### ✅ 월 경계 테스트 고정값 보정 (FE)
- **에이전트**: COD
- **한 일**: 청구·방문·모니터링·배차·직원 lifecycle 테스트가 특정 달(6월)에 묶이지 않도록 **현재 달** 기준으로 맞췄습니다.
- **내 화면/업무에 영향**: 없음 — 자동 테스트만
- **상태**: 완료

<details><summary>자세히</summary>

- `BillingPage.test` · `VisitsPage.test` · `MonitoringSelfDiagnosisPage.test` · `TransportRunNewPage.test` · `StaffLifecyclePanel.test`

</details>

### 📝 이동 스키마 준비·live 가드 ops 문서화
- **에이전트**: TWR
- **한 일**: develop HEAD 실측 후 ops baseline을 갱신하고, FAQ·매뉴얼·관리/배포 가이드에 **스키마 준비 점검**과 **live 스위트 분리 가드**를 추가했습니다.
- **내 화면/업무에 영향**: 없음 — 문서·운영 가이드만 갱신
- **상태**: 완료

<details><summary>자세히</summary>

- baseline: BE `41cbc8a` · FE `e48db91` — **124 route** · Flyway **V1–V189** · BE Test **280** · @Test **2068**
- 신규: FAQ **Q764**(V189 health probe) · **Q765**(live suite schema gate) · Q763 RBAC deepen
- P2 carry(문서화만): 프로그램 리포트 FE `branchId` · 7-5 live PG · J03 Solapi live · M11/M12 급여·회계 scope

</details>

### ✅ 이동서비스 송영표·출발 회차·명단 제외·차량 송영 주소 (BE)
- **에이전트**: COD
- **한 일**: 배차 도메인에 **출발 회차(`departureRound`)**·**차량 송영 시작/종료 주소**·**당일 명단 상태(`transport_roster_day_status`)** 를 DB·API에 반영했습니다. 운행 생성·목록·자동 배차 제안·차량 CRUD 계약을 확장하고 서비스·라우팅 테스트를 갱신했습니다.
- **내 화면/업무에 영향**: **센터장·통합 관리자** — 같은 차량·같은 날 **2·3회차** 배차 저장 · **승차 명단**에서 **금일 배차 제외** 토글이 서버에 유지 · **차량 관리**에 송영 정류장 주소 필드 추가
- **상태**: 완료

<details><summary>자세히</summary>

- migration: **V186** `transport_runs.departure_round` · **V187** `vehicles.shuttle_{start,end}_address` · **V188/V189** `transport_roster_day_status`
- API: `PATCH /api/v1/transport/roster/{clientId}/day-status` — `absentToday`·`skipDispatch` · roster 응답에 동일 필드 노출
- API: `POST /api/v1/transport/runs` — optional `departureRound`(미입력 시 차량·일자 다음 회차 자동) · runs 목록·상세에 `departureRound`·`plannedDepartureTime`
- API: `POST/PATCH /api/v1/transport/vehicles` — `shuttleStartAddress`·`shuttleEndAddress`(미입력 시 지점 주소 fallback)
- suggest: `absentToday` 또는 `skipDispatch` 이용자 **자동 배차 제안 제외**

</details>

### ✅ 이동서비스 송영표 화면·배차 UI 연동 (FE)
- **에이전트**: COD
- **한 일**: **`/transport/shuttle-sheet`** 송영표 화면과 **`TransportShuttleScheduleView`** 를 추가해 차량별·회차별 탑승자를 한눈에 보이게 했습니다. 배차 홈 **금일 배차 제외** 토글·수동 배차 **출발 회차** 입력·차량 **송영 시작/종료 주소** 폼·`TransportContextNav` **송영표** 탭을 연동했습니다.
- **내 화면/업무에 영향**: **센터 직원** — **이동 → 송영표**에서 당일 **승차/하차** 차량·회차·탑승자 확인 · **배차 명단**에서 당일 미이용 이용자 **제외 표시** · 배차 라벨(운전자·차량번호) 정합 개선
- **상태**: 완료

<details><summary>자세히</summary>

- route: `/transport/shuttle-sheet` — `TransportShuttleSheetPage` · `TransportContextNav` 「송영표」
- lib: `transportShuttleSheet.js` — 열·차량 그리드·회차 라벨·경로 legs 병렬 조회
- `/transport` — `updateTransportRosterDayStatusApi` 「금일 배차 제외」(승차·`hq_admin`/`branch_admin`)
- `/transport/runs/new` — optional **출발 회차** · `/transport/vehicles` — **송영 시작/종료 주소**
- tests: `TransportShuttleSheetPage.test` · `TransportShuttleScheduleView.test` · `transportShuttleSheet.test` 등

</details>

### 📝 이동서비스 송영표·배차 확장 ops 문서화
- **에이전트**: TWR
- **한 일**: develop HEAD 실측 후 ops baseline을 **BE `60c4e36` · FE `d873894`** 로 갱신했습니다. FAQ **Q762**(송영표)·**Q763**(금일 배차 제외·출발 회차·차량 송영 주소)·USER_MANUAL §5-8·§5-8-4·ADMIN_GUIDE §1-4·DEPLOYMENT §1-4·§11-3를 추가·정정했습니다.
- **내 화면/업무에 영향**: 없음 — 문서·운영 가이드만 갱신
- **상태**: 완료

<details><summary>자세히</summary>

- baseline: BE `60c4e36` · FE `d873894` — **124 route** · Flyway **V186–V189**
- 신규: FAQ **Q762** · **Q763** — `TransportShuttleScheduleView` · `PATCH …/roster/{clientId}/day-status`
- P2 carry(문서화만): 프로그램 리포트 FE `branchId` · 7-5 live PG · J03 Solapi live · M11/M12 급여·회계 scope

</details>

### ✅ 위생·안전 최근 기록 「결과」열 StatusBadge 한국어 표시
- **에이전트**: UXD
- **한 일**: 일일·정기점검 화면 하단 **최근 기록** 테이블의 「결과」열이 서버 enum(`PASS`/`FAIL`/`NA`/`PARTIAL`)을 그대로 보여주던 문제를 수정했습니다. 체크리스트 요약과 동일한 **`StatusBadge` + `SAFETY_CHECK_RESULT`**(적합·부적합·해당 없음·일부 미흡)로 통일했습니다.
- **내 화면/업무에 영향**: **센터 직원** — `/safety/daily-checks` · `/safety/periodic-checks` **최근 기록**에서 점검 결과를 **한국어 뱃지**로 확인 (색상+텍스트, WCAG 1.4.1)
- **상태**: 완료

<details><summary>자세히</summary>

- 화면: `SafetyDailyChecksPage` · `SafetyPeriodicChecksPage` — `SafetyRecentDraftsPanel` 「결과」 column render
- config: `SAFETY_CHECK_RESULT` — PASS→적합 · FAIL→부적합 · NA→해당 없음 · PARTIAL→일부 미흡
- tests: `SafetyDailyChecksPage.test.jsx` · `SafetyPeriodicChecksPage.test.jsx` — localized label·raw code absent

</details>

### 📝 위생·안전 결과 열 문서화 및 baseline 갱신
- **에이전트**: TWR
- **한 일**: FE develop HEAD 실측 후 ops 문서 baseline을 갱신했습니다. FAQ **Q761**(최근 기록 「결과」열 StatusBadge)·USER_MANUAL §5-9·ADMIN_GUIDE §1-4·DEPLOYMENT §11-3 테스트 행을 추가·정정했습니다. 기존 **Q760** 현장 체크리스트와 연계했습니다.
- **내 화면/업무에 영향**: 없음 — 문서·운영 가이드만 갱신
- **상태**: 완료

<details><summary>자세히</summary>

- baseline: BE `2f4bfdf` · FE `2704fd8` — 위생·안전 4 Route · template catalog · V184+V185
- 신규: FAQ **Q761** — `SAFETY_CHECK_RESULT` StatusBadge 매핑 · Q760 step 7 연계
- 갱신: FAQ · USER_MANUAL · ADMIN_GUIDE · DEPLOYMENT · CHANGELOG 「최근 7일 요약」
- P2 carry(문서화만): 프로그램 리포트 FE `branchId` · 7-5 live PG · J03 Solapi live · M11/M12 급여·회계 scope

</details>

## 2026-06-28

### 📄 TWR 396차 — ops 운영 문서 보강 (doc-only)
- **에이전트**: TWR
- **한 일**: **Q743 deepen** — G16 **`resolveTransportServiceFeeOnePerDayNoteFromRules`** parity **`ONE_PER_DAY` description 우선** (`e19328a`) · **Q744 신규** — QA-B95 **`HealthControllerTest` bootstrap service-unavailable probe lock** (`7fcdfde`) · baseline **`7fcdfde`/`e19328a`**
- **내 화면/업무에 영향**: 없음 — 문서만 갱신
- **상태**: FAQ **Q743·Q744** · USER_MANUAL **§1-3·§5-8-1** · ADMIN_GUIDE **§1-4 G16·QA-B95** · DEPLOYMENT **§1-4·§11-3**

<details>
<summary>자세히</summary>

- 대상: G16 footnote — rates **`onePerDayNote`** 단독 → parity catalog **`ONE_PER_DAY.description`** 우선(395차 static-only 정정)
- 대상: QA-B95 **20th layer** — bootstrap enabled·bean missing health 응답 필드 matrix 회귀 lock
- P2 carry: **program reports FE `branchId`** · **7-5 live PG** · **J03 Solapi live dispatch**

</details>

### ✅ G16 onePerDayNote parity-rules derive + QA-B95 health probe lock (`e19328a`/`7fcdfde`)
- **에이전트**: COD
- **한 일**: **`resolveTransportServiceFeeOnePerDayNoteFromRules(rules, note)`** — parity **`ONE_PER_DAY`** **`description` 우선** · rates **`onePerDayNote`** · **`TRANSPORT_SERVICE_FEE_ONE_PER_DAY_NOTE`** static cascade · **`TransportServiceFeePanel`** parallel **`fetchTransportServiceFeeParityRulesApi`** · **`HealthControllerTest.healthShouldSurfaceServiceUnavailableWhenBootstrapServiceMissing`** +1
- **내 화면/업무에 영향**: **이동서비스비** — footnote가 **parity catalog copy**와 **동일 source** 우선 정합 · **IT·QA** — bootstrap service-unavailable health contract **회귀 lock**
- **상태**: FE+BE 완료 · FAQ **Q743·Q744** · USER_MANUAL **§5-8-1** · ADMIN_GUIDE **§1-4** · CHANGELOG 396차

<details>
<summary>자세히</summary>

- G16: **`transportServiceFee.js`** — **`resolveTransportServiceFeeOnePerDayNoteFromRules`** · **`TransportServiceFeePanel.test`** — parity description 우선·dual-missing static fallback
- QA-B95: **`HealthControllerTest`** — **`bootstrap=service-unavailable`** · **`liveE2eG21SeedStatusCode=service-unavailable`** · **`liveE2eOperationBlockers=[bootstrap-service-unavailable]`**
- tests: **`transportServiceFee.test.js`** +2 · **`TransportServiceFeePanel.test.jsx`** +2 · BE **@Test 1999** (+1)

</details>

### 📄 TWR 395차 — ops 운영 문서 보강 (doc-only)
- **에이전트**: TWR
- **한 일**: **Q743 deepen** — G16 **`resolveTransportServiceFeeOnePerDayNote` static fallback** (`aa0559b`) · **Q735 deepen** — **zero-import PARTIAL vs ALL_SKIPPED UI regression test lock** · baseline **`eb6dd67`/`aa0559b`**
- **내 화면/업무에 영향**: 없음 — 문서만 갱신
- **상태**: FAQ **Q743·Q735 deepen** · USER_MANUAL **§1-3·§1-5·§5-8-1·§5-11** · ADMIN_GUIDE **§1-4 G16·G21** · DEPLOYMENT **§1-4**

<details>
<summary>자세히</summary>

- 대상: G16 **rates `onePerDayNote` blank 시 NHIS copy 유지** — 394차 「footnote 숨김」 정정
- 대상: NHIS import **반영 0건+미매칭+건너뜀 → PARTIAL** 인라인 복구 UI vitest lock
- P2 carry: **program reports FE `branchId`** · **7-5 live PG** · **J03 Solapi live dispatch**

</details>

### ✅ G16 onePerDayNote fallback + NHIS PARTIAL UI regression (`aa0559b`)
- **에이전트**: COD
- **한 일**: **`resolveTransportServiceFeeOnePerDayNote`** — rates API **`onePerDayNote` omit 시 `TRANSPORT_SERVICE_FEE_ONE_PER_DAY_NOTE` static fallback** · **`TransportServiceFeePanel`** wire · **`VisitNhisImportPanel.test`** — **importedCount=0 + unmatched + skipped → PARTIAL recovery (not ALL_SKIPPED)** regression +2
- **내 화면/업무에 영향**: **이동서비스비** — rates API가 footnote를 생략해도 **1일 1회 안내 유지** · **방문일정 import** — 반영 0건 혼합 배치에서 **PARTIAL 복구 문구** 정확 노출
- **상태**: FE 완료 · FAQ **Q743·Q735 deepen** · USER_MANUAL **§5-8-1·§5-11** · CHANGELOG 395차

<details>
<summary>자세히</summary>

- G16: **`transportServiceFee.js`** — **`resolveTransportServiceFeeOnePerDayNote(note)`** · BE catalog **`ONE_PER_DAY`** description과 **동일 copy**
- NHIS: **`VisitNhisImportPanel.test`** — **`treats zero-import with unmatched and skipped rows as PARTIAL`** · **`surfaces recovery steps when outcomeStatus is ALL_SKIPPED`**
- tests: **`transportServiceFee.test.js`** +2 · **`TransportServiceFeePanel.test.jsx`** +1 · **`VisitNhisImportPanel.test.jsx`** +2

</details>

### 📄 TWR 394차 — ops 운영 문서 보강 (doc-only)
- **에이전트**: TWR
- **한 일**: **Q743 신규** — G16 **`TransportParityRulesPanel` BE DTO wire + `onePerDayNote` rates API** (`afbbaa7`) · **Q742 deepen** — **4-outcome keyword alignment test lock** (`eb6dd67`) · baseline **`eb6dd67`/`afbbaa7`**
- **내 화면/업무에 영향**: 없음 — 문서만 갱신
- **상태**: FAQ **Q743·Q742 deepen** · USER_MANUAL **§1-3·§1-5·§5-8-1** · ADMIN_GUIDE **§1-4 G16** · DEPLOYMENT **§1-4**

<details>
<summary>자세히</summary>

- 대상: G16 **parity-rules DTO full-stack closure** — Q710 P2 carry 해소
- P2 carry: **program reports FE `branchId`** · **7-5 live PG** · **J03 Solapi live dispatch**

</details>

### ✅ G16 parity-rules BE catalog DTO FE wire (`afbbaa7`)
- **에이전트**: COD
- **한 일**: **`TransportParityRulesPanel`** — **`normalizeTransportParityRule()`** 로 BE **`code`·`label`·`description`** 매핑 · **`STATIC_TRANSPORT_PARITY_RULES`** error fallback · **`TransportServiceFeePanel`** — rates API **`onePerDayNote`** footnote · **`transportServiceFee.js`** config centralize · tests +4 files
- **내 화면/업무에 영향**: **센터장·사회복지사** — **`/transport/service-fees`** **1일 1회 footnote** + **NHIS 기준 규칙 4항**이 **서버 copy**와 정합 · API 장애 시 **동일 static fallback**
- **상태**: FE 완료 · FAQ **Q743·Q710 deepen** · USER_MANUAL **§5-8-1** · ADMIN_GUIDE **§1-4 G16** · DEPLOYMENT **§1-4** · CHANGELOG 394차

<details>
<summary>자세히</summary>

- FE: `afbbaa7` (on `5636508` NHIS keyword consume)
- contract: parity-rules **`rules[].description`** primary · rates **`onePerDayNote`** optional footnote
- tests: **`transportServiceFee.test.js`** · **`TransportParityRulesPanel.test.jsx`** · **`TransportServiceFeePanel.test.jsx`**

</details>

### ✅ G-NHIS-IMPORT-ERROR-STATUS-SURFACE 4-outcome keyword test lock (`eb6dd67`)
- **에이전트**: COD
- **한 일**: **`NhisVisitScheduleImportRecoveryKeywordAlignmentTest`** +2 — **ALL_SKIPPED·EMPTY** keyword filter alignment · **`VisitControllerRoutingTest`** — **`errorRecoveryKeywordNotes[2].keywords[0]=건너뜀`** · **`[3].keywords[2]=엑셀`** · **`NhisVisitScheduleImportGuidanceTest`** extend
- **내 화면/업무에 영향**: 없음 — import UI 동작 **변화 없음** · **IT·QA** — 4-outcome keyword contract **회귀 lock**
- **상태**: BE 완료 · FAQ **Q742 deepen** · ADMIN_GUIDE **§1-4 G21** · DEPLOYMENT **§1-4** · CHANGELOG 394차

<details>
<summary>자세히</summary>

- BE: `eb6dd67` (on `331f24b` recovery keyword notes)
- tests: alignment **4건** · routing JSON path lock for ALL_SKIPPED/EMPTY

</details>

## 2026-06-27

### 📄 TWR 404차 — ops 운영 문서 보강 (doc-only)
- **에이전트**: TWR
- **한 일**: **Q759 신규** — QA-B358 **safety required-flag unit test lock** (`154ebee`) · **Q758 deepen** — **`safetyCheckCatalog.test.js`·`safetyChecks.test.js`** explicit boolean semantics regression lock · baseline **`2f4bfdf`/`154ebee`**
- **내 화면/업무에 영향**: 없음 — 문서만 갱신
- **상태**: FAQ **Q759·Q758 deepen** · USER_MANUAL **§1-3·§5-9** · ADMIN_GUIDE **§1-4 US-Q01** · DEPLOYMENT **§11-3**

<details>
<summary>자세히</summary>

- 대상: M6 semantics test lock — **`required: false` explicit preserve** · **`required` 미포함 = optional** · **`findUncheckedRequiredItems`** optional 미체크 허용
- 대상: mapper test — periodic item **`required: false`** round-trip (`safetyCheckCatalog.test.js`)
- P2 carry: **program reports FE `branchId`** · **7-5 live PG** · **J03 Solapi live dispatch** · **M11/M12 P1 scope**

</details>

### ✅ QA-B358 safety required-flag unit test sync (`154ebee`)
- **에이전트**: COD
- **한 일**: **`safetyCheckCatalog.test.js`** — periodic item **`required: false`** mapper assertion · **`safetyChecks.test.js`** — **`isSafetyCheckItemRequired`** unspecified/false/true matrix · **`findUncheckedRequiredItems`** optional skip lock
- **내 화면/업무에 영향**: 없음 — **앱 동작 변화 없음** · Q758 semantics **회귀 테스트 lock**
- **상태**: FE test 완료 · FAQ **Q759** · DEPLOYMENT **§11-3** · CHANGELOG 404차

<details>
<summary>자세히</summary>

- FE: `154ebee` — `safetyCheckCatalog.test.js` · `safetyChecks.test.js` (+5/-3)
- follow-up: Q758 implementation @ `b10c5bb` — test-only sync @ `154ebee`
- tests: **`treats only server-declared required=true items as required`** · **`finds unchecked required checklist items`** — optional row excluded

</details>

### 📄 TWR 403차 — ops 운영 문서 보강 (doc-only)
- **에이전트**: TWR
- **한 일**: **Q757 신규** — US-Q01 **`SafetyChecklistForm` server-driven required validation** (`de12f525`) · **Q758 신규** — **optional `required` semantics regression fix** (`b10c5bb`) · **Q747 deepen** — NHIS seed **year-specific `422` message** (`2f4bfdf`) · **Q752 deepen** — live fee seed **base URL·network preflight** (`6dcf7d1`) · baseline **`2f4bfdf`/`b10c5bb`**
- **내 화면/업무에 영향**: 없음 — 문서만 갱신
- **상태**: FAQ **Q757·Q758·Q747·Q752 deepen** · USER_MANUAL **§1-3·§1-5·§5-9** · ADMIN_GUIDE **§1-4 US-Q01·§6-3-1** · DEPLOYMENT **§1-4·§11-3**

<details>
<summary>자세히</summary>

- 대상: M6 checklist — **`required: true` 항목만** submit 전 필수 검증 · **「(필수)」** 라벨 · 필드별 오류
- 대상: semantics — **서버가 명시한 boolean(`true`|`false`)만 신뢰** · **`required` 미명시 = optional** (BNK-691 stage9 regression 정정)
- 대상: fee seed — **`2027년 수가 seed는 지원하지 않습니다. …`** year-specific guidance
- P2 carry: **program reports FE `branchId`** · **7-5 live PG** · **J03 Solapi live dispatch** · **M11/M12 P1 scope**

</details>

### ✅ QA-B358 optional safety template required semantics (`b10c5bb`)
- **에이전트**: COD
- **한 일**: **`isSafetyCheckItemRequired`** — **`item?.required === true`** 만 필수 · **`mapChecklistItem`** — explicit boolean preserve · BNK-691 stage9 regression(**미명시 item 전부 필수 처리**) closure
- **내 화면/업무에 영향**: **센터장·사회복지사** — 위생·안전 **일일·정기점검 저장·success toast 정상 복구** · **`required: true` 항목만** submit 차단 유지
- **상태**: FE 완료 · FAQ **Q758** · USER_MANUAL **§5-9** · CHANGELOG 403차

<details>
<summary>자세히</summary>

- FE: `b10c5bb` — `safetyCheckCatalog.js` · `safetyChecks.js` (+3/-3)
- semantics: catalog **`required` 미포함** → optional · **`required: false`** → optional · **`required: true`** → 필수 + **「(필수)」** checkbox
- tests: `safetyChecks.test.js` name carry — **implementation `=== true`** (test sync P2)

</details>

### ✅ QA-B357 NHIS seed unsupported year message (`2f4bfdf`)
- **에이전트**: COD
- **한 일**: **`BillingService.validateNhisSeedCatalogYear`** — **`{year}년 수가 seed는 지원하지 않습니다.`** prefix · **`BillingServiceTest`** assertion 갱신
- **내 화면/업무에 영향**: **통합 관리자·IT** — Swagger/curl **미지원 연도 `422`** 시 **요청 연도가 오류 본문에 표시** · live E2E **`feeScheduleSeedReason`** 에 year-specific detail 노출 가능
- **상태**: BE 완료 · FAQ **Q747 deepen** · ADMIN_GUIDE **§6-3-1** · CHANGELOG 403차

<details>
<summary>자세히</summary>

- BE: `2f4bfdf` — `BillingService.java` · `BillingServiceTest.java` (+6/-2)
- example: `year=2027` → **`2027년 수가 seed는 지원하지 않습니다. 공단 수가 seed는 2026년 기준만 지원합니다.`**
- UI: **`/billing/fee-schedules`** 「공단 2026 수가 시드」 — **2026 전용** unchanged (Q214)

</details>

### ✅ US-Q01 server-driven required checklist validation (`de12f525`)
- **에이전트**: COD
- **한 일**: **`SafetyChecklistForm`** — **`findUncheckedRequiredItems`** submit guard · **`required`/`helpText` catalog mapper** · per-item **`aria-invalid`** · regression tests
- **내 화면/업무에 영향**: **센터장·사회복지사** — **`required: true` checklist 항목 미체크 시 저장 차단** · **「필수 점검 항목을 모두 확인하세요.」** Alert
- **상태**: FE 완료 · FAQ **Q757** · USER_MANUAL **§5-9** · CHANGELOG 403차

<details>
<summary>자세히</summary>

- FE: `de12f525` — `SafetyChecklistForm.jsx` · `safetyCheckCatalog.js` · `safetyChecks.js` · tests (+142/-14)
- UX: checkbox **`(필수)`** suffix · item-level **「{label} 항목을 확인하세요.」**
- follow-up: **`b10c5bb`** semantics fix — unspecified optional default

</details>

### 📄 TWR 402차 — ops 운영 문서 보강 (doc-only)
- **에이전트**: TWR
- **한 일**: **Q756 신규** — US-Q01 **`SafetyChecklistTemplateItemResponse`** **`helpText`·`required`** schema metadata (`81e3c11`) · **Q750·Q755 deepen** — catalog response 필드·routing jsonPath contract 정정 · baseline **`81e3c11`/`2e35298`**
- **내 화면/업무에 영향**: 없음 — 문서만 갱신
- **상태**: FAQ **Q756** · USER_MANUAL **§1-3·§1-5·§5-9** · ADMIN_GUIDE **§1-4 US-Q01** · DEPLOYMENT **§1-4·§11-3**

<details>
<summary>자세히</summary>

- 대상: M6 template catalog — **checklist item별 `helpText`(점검 가이드 copy)·`required`(필수 플래그)** — FE **`SafetyChecklistForm`** **`aria-describedby`** 연동
- 대상: routing lock — **`dailyItems[0].required=true`** · **`helpText` isString** · **`periodicSubForms[0].items[0].required=true`**
- P2 carry: **program reports FE `branchId`** · **7-5 live PG** · **J03 Solapi live dispatch** · **optional checklist item (`required=false`)**

</details>

### ✅ US-Q01 safety template catalog schema metadata (`81e3c11`)
- **에이전트**: COD
- **한 일**: **`SafetyChecklistTemplateItemResponse`** — **`helpText`·`required`** 필드 추가 · **`SafetyCheckTemplateCatalog`** 전 item contextual help copy · **`SafetyCheckControllerRoutingTest`** · **`SafetyCheckTemplateCatalogTest`** contract lock
- **내 화면/업무에 영향**: **센터장·사회복지사** — **일일·정기점검** checklist 각 항목 아래 **API 기반 안내 문구** 표시 (FE **`SafetyChecklistForm`** 기존 wire)
- **상태**: BE 완료 · FAQ **Q756** · USER_MANUAL **§5-9** · ADMIN_GUIDE **§1-4** · CHANGELOG 402차

<details>
<summary>자세히</summary>

- BE: `81e3c11` — **`SafetyChecklistTemplateItemResponse(id, label, helpText, required)`** · 8 daily + 6×N periodic items with help copy
- tests: **`SafetyCheckTemplateCatalogTest.catalogItemsShouldExposeHelpTextAndRequiredFlag`** · **`hygieneTemplateShouldMatchFrontendPeriodicSchema`** · routing jsonPath +3 assertions
- FE: no new commit — **`mapSafetyCheckTemplateCatalogResponse`** · **`SafetyChecklistForm`** already consume **`helpText`**

</details>

### 📄 TWR 401차 — ops 운영 문서 보강 (doc-only)
- **에이전트**: TWR
- **한 일**: **Q750 정정** — FE **3 `/safety/*` page**가 **`useSafetyCheckTemplateCatalog`** 로 **API-driven template full-stack closure** (`cf73ae8`) · **Q754 신규** — catalog API 실패 시 **로컬 fallback info Alert** + vitest lock (`db15b56`/`2e35298`) · **Q755 신규** — BE **9-endpoint routing·JSON contract** 회귀 lock (`72924bb`/`fbd403c`) · baseline **`fbd403c`/`2e35298`**
- **내 화면/업무에 영향**: 없음 — 문서만 갱신
- **상태**: FAQ **Q750·Q754·Q755** · USER_MANUAL **§1-3·§1-5·§5-9** · ADMIN_GUIDE **§1-4 US-Q01** · DEPLOYMENT **§1-4·§11-3**

<details>
<summary>자세히</summary>

- 대상: M6 template catalog FE wire — **일일·정기·감염병** 3 page가 **`GET /safety/check-template-catalog`** 우선 · **`mapSafetyCheckTemplateCatalogResponse`** · **`getLocalSafetyCheckCatalog()`** fallback
- 대상: fallback UX — **「점검 템플릿 API 응답이 없어 로컬 기본 템플릿을 사용합니다…」** info Alert · **`PageLoading`** 「점검 템플릿 불러오는 중」
- 대상: BE routing lock — catalog **`dailyItems=8`/`periodicSubForms=6`/`infectionSymptoms=5`/`infectionActions=4`** jsonPath · 4 list+create route smoke
- P2 carry: **program reports FE `branchId`** · **7-5 live PG** · **J03 Solapi live dispatch**

</details>

### ✅ US-Q01 safety FE template catalog wire + local fallback (`cf73ae8` · `db15b56` · `2e35298`)
- **에이전트**: COD
- **한 일**: **`useSafetyCheckTemplateCatalog`** hook — **`fetchSafetyCheckTemplateCatalogApi`** → **`safetyCheckCatalog.js`** mapper · **`SafetyDailyChecksPage`·`SafetyPeriodicChecksPage`·`SafetyInfectionControlPage`** catalog wire · API 실패 시 **로컬 fallback Alert** + page tests
- **내 화면/업무에 영향**: **센터장·사회복지사** — 위생·안전 **3 화면 checklist·코드가 서버 catalog와 동기화** · API 장애 시 **동일 로컬 템플릿으로 계속 입력 가능** + 안내 Alert
- **상태**: FE 완료 · FAQ **Q750·Q754** · USER_MANUAL **§5-9** · CHANGELOG 401차

<details>
<summary>자세히</summary>

- FE: `cf73ae8` catalog wire · `db15b56` fallback Alert · `2e35298` regression tests (+3 page tests)
- hook: **`source`** = `api` | `local` · **`reload()`** on mount
- operation-log: catalog 미사용 — 자유 입력 폼 유지

</details>

### ✅ US-Q01 safety 9-endpoint routing contract lock (`72924bb` · `fbd403c`)
- **에이전트**: COD
- **한 일**: **`MustApiEndpointRoutingTest.SafetyCheckRouting`** — 9 US-Q01 endpoint GET/POST routing · catalog jsonPath FE alignment · **`SafetyCheckControllerRoutingTest`** extend **`checkTemplateCatalogShouldExposeFeAlignedContract`**
- **내 화면/업무에 영향**: 없음 — **IT·QA** 회귀 lock만
- **상태**: BE 완료 · FAQ **Q755** · ADMIN_GUIDE **§1-4** · DEPLOYMENT **§11-3** · CHANGELOG 401차

<details>
<summary>자세히</summary>

- BE: `72924bb` MustApi routing nested class · `fbd403c` SafetyCheckControllerRoutingTest deepen
- contract: **`floor_clean`/`HYGIENE`/`FEVER`/`ISOLATION`** first-item shape lock

</details>

### 📄 TWR 400차 — ops 운영 문서 보강 (doc-only)
- **에이전트**: TWR
- **한 일**: **Q750 신규** — US-Q01 **`GET /api/v1/safety/check-template-catalog`** · checklist item ID validate · **`SafetyCheckTemplateCatalogTest`** (`aa9565c`) · **Q751 신규** — **V185** `safety_check_records` 3 CHECK (`7a9ed71`) · **Q752 deepen** — live E2E fee seed **401/403 auth hint** (`dd5571d`) · **Q753 신규** — **`safetyCheckLiveApi.e2e.test.js`** M6 4-endpoint live harness (`bf9b4b1`) · **Q745·Q749 deepen** — safety a11y **`58599c0`** · baseline **`aa9565c`/`bf9b4b1`**
- **내 화면/업무에 영향**: 없음 — 문서만 갱신
- **상태**: FAQ **Q750~Q753** · USER_MANUAL **§1-3·§5-9** · ADMIN_GUIDE **§1-4 US-Q01·V185** · DEPLOYMENT **§1-4·§11-3·§14**

<details>
<summary>자세히</summary>

- 대상: M6 template catalog — **8 daily · 6 periodic sub-form · infection symptom/action codes** — FE `safetyChecks.js` parity · create 시 **unknown item ID → 422**
- 대상: V185 — **`payload_json` object CHECK** · **`sub_form_code` PERIODIC-only enum** · **`result_code` DAILY/PERIODIC vs INFECTION/OPERATION shape**
- 대상: live E2E — **`fetchSafetyCheckTemplateCatalogApi`** · 4 list endpoint branch-scoped smoke · fee seed **401 → token guidance**
- P2 carry: **program reports FE `branchId`** · **7-5 live PG** · **J03 Solapi live dispatch**

</details>

### ✅ US-Q01 safety template catalog API + V185 DB integrity (`aa9565c` · `7a9ed71`)
- **에이전트**: COD
- **한 일**: **`GET /api/v1/safety/check-template-catalog`** — **`dailyItems`·`periodicSubForms`·`infectionSymptoms`·`infectionActions`** · create 경로 **checklist item ID validate** · **V185** 3 CHECK on **`safety_check_records`**
- **내 화면/업무에 영향**: **없음(백엔드)** — checklist 항목·라벨은 기존 FE static config와 **동일** · DB 무결성만 강화
- **상태**: BE 완료 · FAQ **Q750·Q751** · ADMIN_GUIDE **§1-4·V185** · DEPLOYMENT **§1-4·§11-3** · CHANGELOG 400차

<details>
<summary>자세히</summary>

- BE: `7a9ed71` V185 migration · `aa9565c` catalog API + service validate
- tests: **`SafetyCheckTemplateCatalogTest`** · **`RoleBasedControllerAccessTest$SafetyCheckAccess`** +2 template catalog RBAC · BE **@Test 2041** (+17 vs `92770fd`)

</details>

### ✅ US-Q01 safety live harness + a11y + fee seed auth hints (`bf9b4b1` · `58599c0` · `dd5571d`)
- **에이전트**: COD · UXD
- **한 일**: **`fetchSafetyCheckTemplateCatalogApi`** · **`safetyCheckLiveApi.e2e.test.js`** — template catalog + 4 safety list endpoints · **4 Safety pages `<time dateTime>`** · form **`useId()`** · fee seed **401/403 actionable reason**
- **내 화면/업무에 영향**: **접근성** — 점검일·기록일 **시맨틱 `<time>`** · 스크린리더 날짜 해석 개선 · **IT** — live E2E·fee seed triage 문구 개선
- **상태**: FE 완료 · FAQ **Q753·Q752·Q745 deepen** · USER_MANUAL **§5-9** · DEPLOYMENT **§11-3** · CHANGELOG 400차

<details>
<summary>자세히</summary>

- FE: `58599c0` UXD a11y · `dd5571d` fee seed auth hint · `bf9b4b1` live harness + services wire
- tests: **`safetyCheckServices.test.js`** · **`safetyCheckLiveApi.e2e.test.js`** · **`liveFeeScheduleSeed.test.js`** auth case · **`SafetyDailyChecksPage.test`** `<time>` assert

</details>

### 📄 TWR 399차 — ops 운영 문서 보강 (doc-only)
- **에이전트**: TWR
- **한 일**: **Q748 신규** — US-Q01 **`RoleBasedControllerAccessTest$SafetyCheckAccess`** 10 @Test RBAC HTTP lock (`92770fd`) · **Q749 신규** — live E2E **`ensureLiveFeeSchedules`** · **`LIVE_E2E_SKIP_FEE_SEED`** · 404/network diagnostics (`d1d0adf`) · **Q747 deepen** — fee seed **`hq_admin` only apply** HTTP contract · baseline **`92770fd`/`d1d0adf`**
- **내 화면/업무에 영향**: 없음 — 문서만 갱신
- **상태**: FAQ **Q748·Q749** · USER_MANUAL **§1-3·§5-4·§5-9** · ADMIN_GUIDE **§1-4 US-Q01·§6-3-1** · DEPLOYMENT **§1-4·§11-3·§14**

<details>
<summary>자세히</summary>

- 대상: M6 safety — **`caregiver`·`guardian`·`client_user` → 403** · **`hq_admin`·`branch_admin`·`social_worker` → 200** — `@WebMvcTest` 회귀 lock
- 대상: live E2E P5b — **`ensureLiveFeeSchedulesForSession`** **`hq_admin`만** seed 시도 · **`LIVE_E2E_SKIP_FEE_SEED=1|true|yes`** bypass · **404** 시 actionable reason
- P2 carry: **program reports FE `branchId`** · **7-5 live PG** · **J03 Solapi live dispatch**

</details>

### ✅ US-Q01 safety RBAC + NHIS fee seed HTTP contract test lock (`92770fd`)
- **에이전트**: COD
- **한 일**: **`RoleBasedControllerAccessTest`** — **`SafetyCheckAccess`** `@Nested` **10 @Test** (4 endpoint × allow/deny matrix) · **fee seed HTTP** **4 @Test** — **`applyNhisSeedsShouldAllowHqAdmin` 200** · **`applyNhisSeedsShouldDenyBranchAdmin` 403** · unsupported year **`422`**
- **내 화면/업무에 영향**: 없음 — **RBAC·HTTP contract 회귀 lock** · 현장 권한은 Q745·Q747과 동일
- **상태**: BE 완료 · FAQ **Q748·Q747 deepen** · ADMIN_GUIDE **§1-4** · DEPLOYMENT **§1-4·§11-3** · CHANGELOG 399차

<details>
<summary>자세히</summary>

- BE: `92770fd` — +256L `RoleBasedControllerAccessTest.java`
- tests: safety **10 @Test** · fee seed **4 @Test** · BE **@Test 2024** (+14 vs `1f2803c`)

</details>

### ✅ live E2E fee schedule seed harness harden (`d1d0adf`)
- **에이전트**: COD
- **한 일**: **`liveFeeScheduleSeed.js`** — **`LIVE_E2E_SKIP_FEE_SEED`** truthy bypass · **`apply-nhis-seeds` 404/network** explicit **`feeScheduleSeedReason`** · **`ensureLiveFeeSchedulesForSession`** non-`hq_admin` skip · **`liveFeeScheduleSeed.test.js`** +3 vitest
- **내 화면/업무에 영향**: 없음 — **IT·QA** live E2E triage 개선 · 앱 UI 변화 없음
- **상태**: FE 완료 · FAQ **Q749** · DEPLOYMENT **§3-7·§11-3** · CHANGELOG 399차 · **QA-B355 Fixed**

<details>
<summary>자세히</summary>

- FE: `d1d0adf` — `liveFeeScheduleSeed.js` +46/-7 · `liveFeeScheduleSeed.test.js` 58L NEW
- env: **`LIVE_E2E_SKIP_FEE_SEED`** = `1` · `true` · `yes` (case-insensitive trim)
- FE test **497** (+3 vs `f7061c4`)

</details>

### 📄 TWR 398차 — ops 운영 문서 보강 (doc-only)
- **에이전트**: TWR
- **한 일**: **Q747 신규** — G9-COG **`validateNhisSeedCatalogYear`** · **`year≠2026` → `422`** (`1f2803c`) · **Q214·Q311 deepen** — seed API **2026 catalog only** contract · baseline **`1f2803c`/`f7061c4`**
- **내 화면/업무에 영향**: 없음 — 문서만 갱신
- **상태**: FAQ **Q747** · USER_MANUAL **§5-4** · ADMIN_GUIDE **§6-3-1** · DEPLOYMENT **§1-4·§14**

<details>
<summary>자세히</summary>

- 대상: NHIS fee seed — **`GET/POST …/fee-schedules/*nhis-seed*?year=`** 미지원 연도 **fail-fast** (live E2E ambiguous 404/500 방지)
- UI: **`FeeScheduleMatrix`** 「공단 2026 수가 시드」는 **2026 전용** — 현장 체감 변화 없음
- P2 carry: **program reports FE `branchId`** · **7-5 live PG** · **J03 Solapi live dispatch**

</details>

### ✅ G9-COG NHIS fee seed unsupported year guard (`1f2803c`)
- **에이전트**: COD
- **한 일**: **`BillingService.validateNhisSeedCatalogYear`** — **`Nhis2026DaycareRateCatalog.cellsForYear(year)` empty → `422`** 「공단 수가 seed는 2026년 기준만 지원합니다.」 · **`listMissingNhisSeedPayloads`** · **`applyMissingNhisSeedFeeSchedules`** 양쪽 적용 · **`BillingServiceTest` +2**
- **내 화면/업무에 영향**: **통합 관리자** — UI 「공단 2026 수가 시드」 **동작 동일** · **Swagger·live E2E·자동화** — **2027 등 미지원 연도 즉시 `422`** (이전 ambiguous 후속 오류 방지)
- **상태**: BE 완료 · FAQ **Q747·Q214·Q311 deepen** · USER_MANUAL **§5-4** · ADMIN_GUIDE **§6-3-1** · DEPLOYMENT **§1-4** · CHANGELOG 398차

<details>
<summary>자세히</summary>

- BE: `1f2803c` (on `ac69919` US-Q01 safety)
- guard: **scope/DB 조회 전** reject — **`verifyNoInteractions(scopeResolver)`** · **`verifyNoInteractions(feeScheduleRepository)`**
- tests: **`listMissingNhisSeedPayloadsShouldRejectUnsupportedYear`** · **`applyMissingNhisSeedFeeSchedulesShouldRejectUnsupportedYear`** — BE **@Test 2010** (+2)

</details>

### 📄 TWR 393차 — ops 운영 문서 보강 (doc-only)
- **에이전트**: TWR
- **한 일**: **Q742 deepen** — **FE guidance API keyword consume full-stack closure** (`5636508`) · **`resolveVisitImportRecoveryKeywords` API 우선·static fallback** · baseline **`331f24b`/`5636508`**
- **내 화면/업무에 영향**: 없음 — 문서만 갱신
- **상태**: FAQ **Q742 deepen** · USER_MANUAL **§1-3·§1-5·§5-11** · ADMIN_GUIDE **§1-4 G21** · DEPLOYMENT **§1-4**

<details>
<summary>자세히</summary>

- 대상: NHIS import **서버 권위 복구 키워드 FE wire** — Q742 P2 carry **closure**
- P2 carry: **program reports FE `branchId`** · **7-5 live PG** · **J03 Solapi live dispatch**

</details>

### ✅ G-NHIS-IMPORT-ERROR-STATUS-SURFACE FE guidance keyword consume (`5636508`)
- **에이전트**: COD
- **한 일**: **`VisitNhisImportPanel`** — guidance **`errorRecoveryKeywordNotes[]`** → **`resolveVisitImportRecoverySteps(…, keywordNotes)`** · **`resolveVisitImportRecoveryKeywords`** — API keywords **우선** · guidance 미로드·빈 keywords 시 **`VISIT_IMPORT_RECOVERY_KEYWORDS` static fallback** · **`visits.test`**·**`VisitNhisImportPanel.test`** +2
- **내 화면/업무에 영향**: **사회복지사·센터장** — import 복구 단계 **동작 동일** · **BE guidance copy 변경 시 FE drift 없음** · guidance API 장애 시 **기존 static fallback** 유지
- **상태**: FE 완료 · FAQ **Q742** · USER_MANUAL **§5-11** · ADMIN_GUIDE **§1-4 G21** · DEPLOYMENT **§1-4** · CHANGELOG 393차

<details>
<summary>자세히</summary>

- FE: `5636508` (on `2d9b9d3` branch-aware recovery)
- contract: **`keywordNotes` non-empty → API keywords** · **empty/missing → static map**
- tests: **`prefers guidance API errorRecoveryKeywordNotes over static keywords`**

</details>

### 📄 TWR 392차 — ops 운영 문서 보강 (doc-only)
- **에이전트**: TWR
- **한 일**: **Q742 신규** — **`errorRecoveryKeywordNotes`** guidance API (`331f24b`) · **Q740 deepen** — FE **`VISIT_IMPORT_RECOVERY_KEYWORDS`** static mirror · baseline **`331f24b`/`2d9b9d3`**
- **내 화면/업무에 영향**: 없음 — 문서만 갱신
- **상태**: FAQ **Q742** · USER_MANUAL **§1-3·§1-5·§5-11** · ADMIN_GUIDE **§1-4 G21** · DEPLOYMENT **§1-4**

<details>
<summary>자세히</summary>

- 대상: NHIS import **서버 권위 복구 키워드** — outcome별 **`errorRecoverySteps` 필터** contract
- P2 carry: **FE guidance API keyword consume** · **program reports FE `branchId`** · **7-5 live PG** · **J03 Solapi live dispatch**

</details>

### ✅ G-NHIS-IMPORT-ERROR-STATUS-SURFACE recovery keyword notes BE (`331f24b`)
- **에이전트**: COD
- **한 일**: **`GET /visits/imports/nhis/guidance`** — **`errorRecoveryKeywordNotes[]`** 4종(`UNMATCHED`/`PARTIAL`/`ALL_SKIPPED`/`EMPTY`) · 각 **`code`·`keywords[]`** — 7단계 복구 copy와 **정합 회귀 lock** · **`NhisVisitScheduleImportRecoveryKeywordAlignmentTest` +2**
- **내 화면/업무에 영향**: **사회복지사·센터장** — import UI 동작 **변화 없음**(FE는 현재 static keyword mirror) · **IT·연동** — guidance API로 **서버 권위 키워드** 조회 가능
- **상태**: BE 완료 · FAQ **Q742** · ADMIN_GUIDE **§1-4 G21** · DEPLOYMENT **§1-4** · CHANGELOG 392차

<details>
<summary>자세히</summary>

- BE: `331f24b` (on `3d4e58a` counter integrity)
- response: **`errorRecoveryKeywordNotes.length()=4`** · UNMATCHED keywords include **「지점 필터」** · PARTIAL include **`outcomeStatus=PARTIAL`**
- P2: FE **`resolveVisitImportRecoverySteps`** → guidance API keyword consume (현재 **`visits.js` static**)

</details>

### 📄 TWR 391차 — ops 운영 문서 보강 (doc-only)
- **에이전트**: TWR
- **한 일**: **Q740 신규** — **outcome counter integrity** (`3d4e58a`) · **guidance 7단계·branch-aware recovery** (`45acb75`/`2d9b9d3`) · **Q741 신규** — **QA-B350 stale `branchId` → 전체 fallback** (`320ba06`) · baseline **`3d4e58a`/`2d9b9d3`**
- **내 화면/업무에 영향**: 없음 — 문서만 갱신
- **상태**: FAQ **Q740·Q741** · **Q738·Q739 deepen** · USER_MANUAL **§1-5·§5-11** · ADMIN_GUIDE **§1-4 G21** · DEPLOYMENT **§1-4**

<details>
<summary>자세히</summary>

- 대상: NHIS import **outcome 집계 방어** · **복구 안내 7단계** · **수급자 찾기** deep-link **빈 목록 stuck 방지**
- P2 carry: **program reports FE `branchId`** · **7-5 live PG** · **J03 Solapi live dispatch**

</details>

### ✅ G-NHIS-IMPORT-ERROR-STATUS-SURFACE outcome counter integrity BE (`3d4e58a`)
- **에이전트**: COD
- **한 일**: **`NhisVisitScheduleImportOutcome.validateCounts`** — **음수·합계 초과·totalRows=0 비정상 카운터** → **`IllegalArgumentException`** · **`NhisVisitScheduleImportOutcomeTest` +3**
- **내 화면/업무에 영향**: **사회복지사·센터장** — 파서·집계 버그 시 **잘못된 PARTIAL/ALL_SKIPPED Alert 노출 전 서버 오류** · 운영자에게 **오해 유발 outcome 방지**
- **상태**: BE 완료 · FAQ **Q740** · ADMIN_GUIDE **§1-4 G21** · DEPLOYMENT **§1-4** · CHANGELOG 391차

<details>
<summary>자세히</summary>

- BE: `3d4e58a` (on `45acb75` branch-aware copy)
- tests: **`resolveShouldThrowWhenAnyCounterIsNegative`** · **`resolveShouldThrowWhenCountersExceedTotalRows`** · **`resolveShouldThrowWhenZeroTotalRowsHasNonZeroCounters`**

</details>

### ✅ G-NHIS-IMPORT-ERROR-STATUS-SURFACE branch-aware recovery steps FE (`2d9b9d3`)
- **에이전트**: COD
- **한 일**: **`visits.js`** — **`VISIT_IMPORT_RECOVERY_KEYWORDS`** — **`UNMATCHED`·`PARTIAL`** 에 **「지점 필터」** 키워드 추가 · BE **`NhisVisitScheduleImportGuidance` 7단계** 와 인라인 복구 필터 정합 · **`visits.test`**·**`VisitNhisImportPanel.test`** +1
- **내 화면/업무에 영향**: **사회복지사·센터장** — import 실패 후 **지점 필터 유지·지점 수정** 복구 단계가 **UNMATCHED/PARTIAL** Alert 아래에 노출
- **상태**: FE 완료 · FAQ **Q740** · USER_MANUAL **§5-11** · CHANGELOG 391차

<details>
<summary>자세히</summary>

- FE: `2d9b9d3` (on `320ba06` QA-B350)
- aligns: BE step 4 「미매칭 행을 클릭하면 해당 지점 필터가 유지…」 copy

</details>

### ✅ QA-B350 stale branch query filter reset FE (`320ba06`)
- **에이전트**: COD
- **한 일**: **`ClientListPage`** — URL **`branchId`** 가 **선택 가능한 지점 옵션에 없으면** FilterChip **`전체`** 로 reset · **빈 목록 stuck** 방지 · **`ClientListPage.test`** +1
- **내 화면/업무에 영향**: **통합 관리자·다지점** — NHIS import **「수급자 찾기」** deep-link 후 **해당 지점에 등록 수급자 0명**이어도 **검색어(`q`) 매칭 수급자**가 다른 지점에 있으면 **목록에 표시**
- **상태**: FE 완료 · FAQ **Q741** · USER_MANUAL **§5-11** · CHANGELOG 391차

<details>
<summary>자세히</summary>

- FE: `320ba06` (on `562560a` branch deep-link)
- guard: **`branchOptions`에 없는 `branchId`** → **`CLIENT_LIST_FILTER_ALL`**

</details>

### ✅ G-NHIS-IMPORT-ERROR-STATUS-SURFACE branch-aware recovery copy BE (`45acb75`)
- **에이전트**: COD
- **한 일**: **`NhisVisitScheduleImportGuidance.ERROR_RECOVERY_STEPS`** step 4 — **지점 필터 유지 deep-link**·**잘못된 지점 시 branches 수정** copy · **`NhisVisitScheduleImportGuidanceTest`** 갱신
- **내 화면/업무에 영향**: **사회복지사·센터장** — 정적 import 안내·API **`errorRecoverySteps`** 가 **7단계** (390차 6단계 → +branch-aware step 4 확장)
- **상태**: BE 완료 · FAQ **Q740** · DEPLOYMENT **§1-4** · CHANGELOG 391차

<details>
<summary>자세히</summary>

- BE: `45acb75` (on `9b91e0f` test lock)
- guidance: **`errorRecoverySteps.length()=7`**

</details>

### 📄 TWR 390차 — ops 운영 문서 보강 (doc-only)
- **에이전트**: TWR
- **한 일**: **Q739 신규** — **G-NHIS import 수급자 찾기 지점 필터 유지** (`562560a`) · **Q738 deepen** — service-layer PARTIAL test lock · guidance **6단계** (`9b91e0f`) · baseline **`9b91e0f`/`562560a`**
- **내 화면/업무에 영향**: 없음 — 문서만 갱신
- **상태**: FAQ **Q739** · **Q738 deepen** · USER_MANUAL **§1-5·§5-11** · ADMIN_GUIDE **§1-4 G21** · DEPLOYMENT **§1-4**

<details>
<summary>자세히</summary>

- 대상: 다지점(`hq_admin`) NHIS import **「수급자 찾기」** — **`/clients?branchId=&q=`** deep-link · import 지점과 목록 필터 정합
- P2 carry: **program reports FE `branchId`** · **7-5 live PG** · **J03 Solapi live dispatch**

</details>

### ✅ G-NHIS-IMPORT-ERROR-STATUS-SURFACE branch filter on import links FE wire (`562560a`)
- **에이전트**: COD
- **한 일**: **`VisitNhisImportPanel`** — **`buildClientListSearchHref(ltcCertNo, branchId)`** · **`ClientListPage`** — **`readClientListBranchFromQuery`** URL **`branchId`** 초기화 · invalid branch guard · tests +24
- **내 화면/업무에 영향**: **통합 관리자·다지점 센터** — import 미매칭 **「수급자 찾기」** 시 **해당 지점 필터 유지** · 타 지점 수급자 혼선 감소
- **상태**: FE 완료 · FAQ **Q739** · USER_MANUAL **§5-11** · CHANGELOG 390차

<details>
<summary>자세히</summary>

- FE: `562560a` (on `cda2a10` client search deep-link)
- URL: **`/clients?branchId={uuid}&q={ltcCertNo}`** — query key **`branchId`** · **`q`**

</details>

### ✅ G-NHIS-IMPORT-ERROR-STATUS-SURFACE zero-import partial outcome test lock (`9b91e0f`)
- **에이전트**: COD
- **한 일**: **`VisitServiceTest`** + **`VisitControllerRoutingTest`** — **반영 0건 + 미매칭·건너뜀 혼합 → `PARTIAL`** service·routing regression lock · **`NhisVisitScheduleImportGuidance`** errorRecoverySteps **+1** (PARTIAL vs ALL_SKIPPED 운영자 copy)
- **내 화면/업무에 영향**: **사회복지사·센터장** — import **복구 안내 6단계**에 **「반영 0건+미매칭·건너뜀 → PARTIAL」** 문구 추가 · 분류 회귀 방지
- **상태**: BE 완료 · FAQ **Q738 deepen** · ADMIN_GUIDE **§1-4 G21** · DEPLOYMENT **§1-4** · CHANGELOG 390차

<details>
<summary>자세히</summary>

- BE: `9b91e0f` (on `ffa57ea` ALL_SKIPPED fix)
- tests: **`importNhisShouldReturnPartialOutcomeWhenZeroImportedWithUnmatchedAndSkippedRows`** + **`nhisImportRouteShouldExposePartialOutcomeWhenZeroImportedWithUnmatchedAndSkipped`**
- guidance: **`errorRecoverySteps.length()=6`** (기존 5 → +1)

</details>

### 📄 TWR 389차 — ops 운영 문서 보강 (doc-only)
- **에이전트**: TWR
- **한 일**: **Q738 신규** — **G-NHIS-IMPORT-ERROR-STATUS-SURFACE deepen** (`ffa57ea`/`e4dbe9a`/`cda2a10`) — inline recovery · **수급자 찾기** deep-link · **ALL_SKIPPED 분류 정정** · **Q735 deepen** · baseline **`ffa57ea`/`cda2a10`**
- **내 화면/업무에 영향**: 없음 — 문서만 갱신
- **상태**: FAQ **Q738** · USER_MANUAL **§1-3·§1-5·§5-11** · ADMIN_GUIDE **§1-4 G21** · DEPLOYMENT **§1-4** · README **§6**

<details>
<summary>자세히</summary>

- 대상: ezCare FAQ **21845** incident pattern — ogada **`/visits`** import **복구 루프 closure** (정적 guide → 인라인 recovery → 수급자 목록 deep-link)
- P2 carry: **program reports FE `branchId`** · **7-5 live PG** · **J03 Solapi live dispatch**

</details>

### ✅ G-NHIS-IMPORT-ERROR-STATUS-SURFACE unmatched row client search FE wire (`cda2a10`)
- **에이전트**: COD
- **한 일**: **`VisitNhisImportPanel`** — **`UNMATCHED`** 행 **「수급자 찾기」** → **`/clients?q={ltcCertNo}`** · **`clientListFilters.js`** · **`ClientListPage`** query prefill · tests +31
- **내 화면/업무에 영향**: **사회복지사·센터장** — NHIS import **미매칭 행**에서 **인정번호로 수급자 목록** 바로 검색 · 등록·수정 후 **재import** 루프 단축
- **상태**: FE 완료 · FAQ **Q738** · USER_MANUAL **§5-11** · CHANGELOG 389차

<details>
<summary>자세히</summary>

- FE: `cda2a10` (on `e4dbe9a` inline recovery)
- UI: 결과 표 **「조치」** 열 — **`buildClientListSearchHref(ltcCertNo)`** · **`aria-label`** 인정번호 안내

</details>

### ✅ G-NHIS-IMPORT-ERROR-STATUS-SURFACE inline recovery steps FE wire (`e4dbe9a`)
- **에이전트**: COD
- **한 일**: **`VisitNhisImportRecoverySteps`** · **`resolveVisitImportRecoverySteps`** — outcome·API 오류 직후 **맥락형 복구 `<ol>`** · **`visits.js`** keyword filter · tests +121
- **내 화면/업무에 영향**: **사회복지사·센터장** — import **부분 반영·미매칭·API 오류** 직후 **정적 guide 없이** Alert 아래 **즉시 조치 단계** 확인
- **상태**: FE 완료 · FAQ **Q738** · USER_MANUAL **§5-11** · CHANGELOG 389차

<details>
<summary>자세히</summary>

- FE: `e4dbe9a` (on `91675f1` outcome Alert wire)
- pattern: **`data-testid="visit-import-inline-recovery"`** · **`SUCCESS`** 시 미노출

</details>

### ✅ G-NHIS-IMPORT-ERROR-STATUS-SURFACE mixed zero-import outcome BE fix (`ffa57ea`)
- **에이전트**: COD
- **한 일**: **`NhisVisitScheduleImportOutcome.resolve`** — **반영 0건 + 미매칭·건너뜀 혼합** → **`PARTIAL`** (기존 **`ALL_SKIPPED`** 오분류 수정) · **`NhisVisitScheduleImportOutcomeTest`** +1
- **내 화면/업무에 영향**: **사회복지사·센터장** — **미매칭 인정번호**가 **전체 건너뜀** Alert에 가려지지 않음 · **인정번호·성명 수정** 조치 누락 방지
- **상태**: BE 완료 · FAQ **Q738** · ADMIN_GUIDE **§1-4 G21** · CHANGELOG 389차

<details>
<summary>자세히</summary>

- BE: `ffa57ea` (on `c38388d` outcome expose)
- rule: **`ALL_SKIPPED`** = **건너뜀만** · **미매칭 0건**

</details>

## 2026-06-26

### 📄 TWR 387차 — ops 운영 문서 보강 (doc-only)
- **에이전트**: TWR
- **한 일**: **Q735 신규** — **G-NHIS-IMPORT-ERROR-STATUS-SURFACE** full-stack (`c38388d`/`91675f1`) · **Q736 deepen** — QA-B95 **3축 component code FE wire** (`3eebddb`) · **Q737 deepen** — null g21 seed normalize (`1c7064d`) · **V183** bulk-export index (`547c85f`) · baseline **`c38388d`/`91675f1`**
- **내 화면/업무에 영향**: 없음 — 문서만 갱신
- **상태**: FAQ **Q735·Q736·Q737** · USER_MANUAL **§1-3·§1-5·§5-11** · ADMIN_GUIDE **§1-4·§6-2-2a** · DEPLOYMENT **§1-4·§11-3** · README **§6**

<details>
<summary>자세히</summary>

- 대상: **FAQ 21845 공단 엑셀 incident pattern** — ogada **`/visits`** import **실시간 outcome surfacing** (ezCare 사후 FAQ 대비 차별화)
- P2 carry: **program reports FE `branchId`** · **7-5 live PG** · **J03 Solapi live dispatch**

</details>

### ✅ G-NHIS-IMPORT-ERROR-STATUS-SURFACE visit import outcome FE wire (`91675f1`)
- **에이전트**: COD
- **한 일**: **`VisitNhisImportGuidePanel`** — **`outcomeStatusNotes`·`errorRecoverySteps`** · **`VisitNhisImportPanel`** — **`resolveVisitImportOutcome`** Alert · **`visits.js`** tone map · tests +78
- **내 화면/업무에 영향**: **사회복지사·센터장** — **`/visits`** NHIS import 후 **전체/부분/미매칭/건너뜀** 결과를 **Alert·안내 패널**에서 즉시 확인 · FAQ 21845 유형 **수동 공지 없이** 현장 triage
- **상태**: FE 완료 · FAQ **Q735** · USER_MANUAL **§5-11** · CHANGELOG 387차

<details>
<summary>자세히</summary>

- FE: `91675f1` (on `3eebddb` QA-B95 component wire)
- UI: **`VisitNhisImportGuidePanel`** — **「import 결과 상태」** · **「오류·부분 반영 시 조치」**
- import: **`outcomeStatus`/`outcomeSummary`** → success/warning/danger Alert

</details>

### ✅ G-NHIS-IMPORT-ERROR-STATUS-SURFACE visit import outcome BE expose (`c38388d`)
- **에이전트**: COD
- **한 일**: **`NhisVisitScheduleImportOutcome`** 5-state · **`POST /visits/imports/nhis`** — **`outcomeStatus`·`outcomeSummary`** · **`GET …/guidance`** — **`outcomeStatusNotes[]`·`errorRecoverySteps[]`** · **`NhisVisitScheduleImportOutcomeTest`** +5
- **내 화면/업무에 영향**: **사회복지사·센터장** — Swagger/API·화면 모두 **동일 outcome code** — **`SUCCESS`/`PARTIAL`/`UNMATCHED`/`ALL_SKIPPED`/`EMPTY`**
- **상태**: BE 완료 · FAQ **Q735** · ADMIN_GUIDE **§1-4 G21** · DEPLOYMENT **§1-4** · CHANGELOG 387차

<details>
<summary>자세히</summary>

- BE: `c38388d` (on `547c85f` V183 index)
- pattern: ezCare FAQ **21845** — ogada **real-time surfacing** 우위

</details>

### ✅ QA-B95 g21 component status codes FE wire (`3eebddb`)
- **에이전트**: COD
- **한 일**: **`liveBackendProbe.js`·`liveConfig.js`·`liveGlobalSetup.js`** — 3축 component code parse·skip · **`liveE2eHarness.test`** +117
- **내 화면/업무에 영향**: 없음 — live E2E triage만
- **상태**: FE 완료 · FAQ **Q736** · DEPLOYMENT **§11-3** · CHANGELOG 387차

<details>
<summary>자세히</summary>

- FE: `3eebddb` — Q733 BE expose(`59e4e7f`) FE wire closure

</details>

### ✅ V183 care plan bulk-export branch×plan_year index (`547c85f`)
- **에이전트**: COD/DBA
- **한 일**: **`V183__client_care_plan_forms_branch_plan_year_index.sql`** — **`idx_client_care_plan_forms_org_branch_plan_year`**
- **내 화면/업무에 영향**: **사회복지사·센터장** — **`/clients/care-plan-notifications`** 일괄 출력 **지점×연도 조회 성능** 개선 · 동작 동일
- **상태**: BE 완료 · FAQ **Q726 deepen** · ADMIN_GUIDE **§6-2-2a** · CHANGELOG 387차

<details>
<summary>자세히</summary>

- BE: `547c85f` — G-CLIENT-CONTRACT-BULK-PRINT backing index

</details>

### ✅ QA-B95 null g21 seed status normalize (`1c7064d`)
- **에이전트**: COD
- **한 일**: **`LiveE2eOperationReadinessSupport.normalizeG21SeedStatus`** — null aggregate → applicable+component missing · **`LiveE2eControllerTest`** +48 lines
- **내 화면/업무에 영향**: 없음 — health/probe·live E2E만
- **상태**: BE 완료 · FAQ **Q737** · DEPLOYMENT **§11-3** · CHANGELOG 387차

<details>
<summary>자세히</summary>

- BE: `1c7064d` (on `9664f29` component test lock)

</details>

### 📄 TWR 386차 — ops 운영 문서 보강 (doc-only)
- **에이전트**: TWR
- **한 일**: **Q734 deepen** — **G-CLIENT-CONTRACT-BULK-PRINT** FE **`branchId`/`clientIds` 정규화** (`d759ade`) · **Q726 deepen** — vitest 5/5 · baseline **`9664f29`/`d759ade`**
- **내 화면/업무에 영향**: 없음 — 문서만 갱신
- **상태**: FAQ **Q734·Q726 deepen** · USER_MANUAL **§3-3·§4-3** · ADMIN_GUIDE **§6-2-2a** · DEPLOYMENT **§1-4** · README **§6**

<details>
<summary>자세히</summary>

- 대상: **FAQ 21507 급여제공 변경계약서 일괄 출력** — FE payload **공백 trim·중복 clientId 제거**로 API 필터 오류 예방
- P2 carry: **program reports FE `branchId`** · **7-5 live PG** · **J03 Solapi live dispatch**

</details>

### ✅ G-CLIENT-CONTRACT-BULK-PRINT bulk export branch/client id normalize (`d759ade`)
- **에이전트**: COD
- **한 일**: **`ClientCarePlanBulkExportPanel`** — **`branchId` trim** · **`clientOptions` dedupe**(공백·중복 UUID) · **`resolveCarePlanBulkExportClientIds`** 연동 · **`ClientCarePlanBulkExportPanel.test`** +1 (5/5)
- **내 화면/업무에 영향**: **사회복지사·센터장** — G38 통보 목록에서 **공백·중복 ID**가 섞여도 **일괄 다운로드 실패 감소** · 동작 동일
- **상태**: FE 완료 · FAQ **Q734·Q726 deepen** · USER_MANUAL **§3-3** · ADMIN_GUIDE **§6-2-2a** · CHANGELOG 386차

<details>
<summary>자세히</summary>

- FE: `d759ade` (on `96196ed` UXD-167 a11y)
- utils: **`clientCarePlanBulkExport.js`** — query builder · **`normalizedBranchId`** API 전송 전 trim
- test: **`normalizes branchId and deduplicates whitespace client ids before export`**

</details>

### 📄 TWR 385차 — ops 운영 문서 보강 (doc-only)
- **에이전트**: TWR
- **한 일**: **Q726 full-stack 정정** — **G-CLIENT-CONTRACT-BULK-PRINT** **`ClientCarePlanBulkExportPanel`** FE wire (`0d0b587`/`96196ed`) · **Q733 deepen** — QA-B95 **17th layer** component code test lock (`9664f29`) · baseline **`9664f29`/`96196ed`**
- **내 화면/업무에 영향**: 없음 — 문서만 갱신
- **상태**: FAQ **Q726·Q733 deepen** · USER_MANUAL **§1-3·§3-3·§4-3 G38** · ADMIN_GUIDE **§6-2-2·§6-2-2a** · DEPLOYMENT **§1-4** · README **§6**

<details>
<summary>자세히</summary>

- 대상: **FAQ 21507 급여제공 변경계약서 일괄 출력** — BE bulk-export API + **FE `CarePlanNotificationPage` embed** full-stack closure
- P2 carry: **program reports FE `branchId`** · **7-5 live PG** · **J03 Solapi live dispatch**

</details>

### ✅ UXD-167 bulk export a11y + NHIS guide heading CSS (`96196ed`)
- **에이전트**: UXD
- **한 일**: **`ClientCarePlanBulkExportPanel`** — 폼 `aria-label`·연도 범위 `Field error`·submit `aria-busy` · **`VisitNhisImportGuidePanel`** — **`.ds-nhis-guide__heading`** CSS 승격 · 외부 링크 sr-only 「(새 탭)」
- **내 화면/업무에 영향**: **사회복지사·센터장** — 일괄 출력·NHIS import 안내 **스크린리더·키보드** 개선 · 동작 동일
- **상태**: FE 완료 · FAQ **Q726 deepen** · USER_MANUAL **§3-3·§5-11** · CHANGELOG 385차

<details>
<summary>자세히</summary>

- FE: `96196ed` (on `0d0b587` bulk export wire)
- test: **`ClientCarePlanBulkExportPanel.test`** 4/4 PASS

</details>

### ✅ G-CLIENT-CONTRACT-BULK-PRINT care plan bulk export FE wire (`0d0b587`)
- **에이전트**: COD
- **한 일**: **`ClientCarePlanBulkExportPanel`** — **`exportClientCarePlanFormsBulkApi`** · **`CarePlanNotificationPage`** embed · plan-year·지점 전체/선택 수급자 · **`ClientCarePlanBulkExportPanel.test`**
- **내 화면/업무에 영향**: **사회복지사·센터장** — **`/clients/care-plan-notifications`** 에서 **「급여제공 변경계약서 일괄 출력」** 카드로 **Swagger 없이** 다운로드
- **상태**: FE 완료 · FAQ **Q726 full-stack** · USER_MANUAL **§3-3·§4-3** · ADMIN_GUIDE **§6-2-2·§6-2-2a** · DEPLOYMENT **§1-4** · CHANGELOG 385차

<details>
<summary>자세히</summary>

- FE: `0d0b587` (on `8ceb25c` NHIS guide wire)
- UI: **`ClientCarePlanBulkExportPanel`** — **`BranchScopeNotice`** · **지점 전체 출력** Checkbox · 선택 수급자 fieldset · **`benefit-change-contracts-{year}.txt`** blob download
- services: **`exportClientCarePlanFormsBulkApi`** (`services.js`)
- route: **`/clients/care-plan-notifications`** — G38 compliance 목록 위에 패널 mount

</details>

### ✅ QA-B95 g21 component status code test lock (`9664f29`)
- **에이전트**: COD
- **한 일**: **`LiveE2eOperationReadinessSupportTest`** +3 — **`resolveG21SeedComponentStatusCode`** matrix (not-applicable·branch-missing·applicable present/missing)
- **내 화면/업무에 영향**: 없음 — live E2E·IT triage만
- **상태**: BE 완료 · FAQ **Q733 deepen** · DEPLOYMENT **§11-3** · CHANGELOG 385차

<details>
<summary>자세히</summary>

- BE: `9664f29` (on `59e4e7f` component code expose)
- regression-safe contract lock — **17th layer** QA-B95

</details>

### 📄 TWR 384차 — ops 운영 문서 보강 (doc-only)
- **에이전트**: TWR
- **한 일**: **Q731 full-stack 정정** — **G-NHIS-SCHEDULE-IMPORT** **`VisitNhisImportGuidePanel`** FE wire (`8ceb25c`) · **Q733 신규** — QA-B95 **G21 seed 3축 component status code** (`59e4e7f`) · baseline **`59e4e7f`/`8ceb25c`**
- **내 화면/업무에 영향**: 없음 — 문서만 갱신
- **상태**: FAQ **Q731·Q733** · USER_MANUAL **§1-3·§1-5·§5-11** · ADMIN_GUIDE **§1-4 G21** · DEPLOYMENT **§1-4·§11-3** · README **§6**

<details>
<summary>자세히</summary>

- 대상: **FAQ 21298 공단 등록 일정 업로드** — BE guidance API + **FE import 패널 안내** full-stack closure
- P2 carry: **G-CLIENT-CONTRACT-BULK-PRINT FE wire** · **program reports FE `branchId`** · **7-5 live PG** · **J03 Solapi live dispatch**

</details>

### ✅ G-NHIS-SCHEDULE-IMPORT visit NHIS import guidance FE wire (`8ceb25c`)
- **에이전트**: COD
- **한 일**: **`VisitNhisImportGuidePanel`** — **`GET /visits/imports/nhis/guidance`** fetch · **`VisitNhisImportPanel`** 상단 PLAN/BILLING 4단계 안내 · **`VisitNhisImportGuidePanel.test`** · guidance 실패 시 import **유지**
- **내 화면/업무에 영향**: **사회복지사·센터장** — **`/visits`** import 패널에서 **공단 다운로드·업로드 절차**를 화면에서 확인 · Swagger 불필요
- **상태**: FE 완료 · FAQ **Q731 deepen** · USER_MANUAL **§5-11** · DEPLOYMENT **§1-4** · CHANGELOG 384차

<details>
<summary>자세히</summary>

- FE: `8ceb25c` (on `6009ba7` g21 status code wire)
- UI: **`VisitNhisImportGuidePanel`** — browser Alert · portal link · PLAN/BILLING `<ol>` · **`scheduleKindNote`·`confirmedScheduleResetNote`** · **`/visits?tab=nhis-comparison`** link · **`message` warning Alert**
- services: **`fetchVisitNhisImportGuidanceApi`** (`services.js`)
- test: **`VisitNhisImportGuidePanel.test`** · **`VisitNhisImportPanel.test`** — guide mount

</details>

### ✅ QA-B95 g21 seed component readiness codes BE expose (`59e4e7f`)
- **에이전트**: COD
- **한 일**: **`liveE2eVisitScheduleStatusCode`·`liveE2eBillingVisitScheduleStatusCode`·`liveE2eNhisImportStatusCode`** — health/probe · probe alias **`visitScheduleStatusCode`·`billingVisitScheduleStatusCode`·`nhisImportStatusCode`** · **`resolveG21SeedComponentStatusCode`**
- **내 화면/업무에 영향**: 없음 — live E2E·IT triage만
- **상태**: BE 완료 · FAQ **Q733·Q729 deepen** · DEPLOYMENT **§11-3** · CHANGELOG 384차

<details>
<summary>자세히</summary>

- BE: `59e4e7f` (on `4567030` visit guidance API)
- component codes: **`present`·`missing`** (applicable) · **`disabled`·`service-unavailable`·`error`·`not-applicable`·`branch-missing-or-inactive`** (aggregate와 동일)
- detail 문자열(`liveE2eG21SeedStatusDetail`) **기존 유지** — component code는 **3축 분류 전용**
- test: **`HealthControllerTest`** · **`LiveE2eControllerTest`** — disabled·service-unavailable·present·not-applicable·branch-missing assert

</details>

### 📄 TWR 383차 — ops 운영 문서 보강 (doc-only)
- **에이전트**: TWR
- **한 일**: **Q731 신규** — **G-NHIS-SCHEDULE-IMPORT** `GET /api/v1/visits/imports/nhis/guidance` (`4567030`) · **Q732 신규** — QA-B95 **`liveE2eG21SeedStatusCode` FE code-first wire** (`6009ba7`) · baseline **`4567030`/`6009ba7`**
- **내 화면/업무에 영향**: 없음 — 문서만 갱신
- **상태**: FAQ **Q731·Q732** · USER_MANUAL **§1-5·§5-11** · ADMIN_GUIDE **§1-4 G21** · DEPLOYMENT **§1-4·§11-3** · README **§6**

<details>
<summary>자세히</summary>

- 대상: **FAQ 21298 공단 등록 일정 업로드** — BE guidance API only · **FE wire P2**
- P2 carry: **G-CLIENT-CONTRACT-BULK-PRINT FE wire** · **program reports FE `branchId`** · **7-5 live PG** · **J03 Solapi live dispatch**

</details>

### ✅ G-NHIS-SCHEDULE-IMPORT visit NHIS import guidance API (`4567030`)
- **에이전트**: COD
- **한 일**: **`GET /api/v1/visits/imports/nhis/guidance`** — **PLAN/BILLING dual-workflow** static onboarding copy (FAQ 21298) · **`NhisVisitScheduleImportGuidance`** domain · **`MustApiEndpointRoutingTest`** lock
- **내 화면/업무에 영향**: **사회복지사·센터장** — Swagger·연동으로 **공단 방문일정 import 절차** 확인 가능 · **화면 패널은 아직 없음 (P2)**
- **상태**: BE 완료 · FAQ **Q731** · USER_MANUAL **§5-11** · ADMIN_GUIDE **§1-4 G21** · DEPLOYMENT **§1-4**

<details>
<summary>자세히</summary>

- BE: `4567030` (on `0f19767` g21 status code)
- response: **`portalUrl`·`browserRequirement`·`planImportSteps`(4)·`billingImportSteps`(4)·`confirmedScheduleResetNote`·`scheduleKindNote`·`message`**
- RBAC: **`branch_admin`·`social_worker`** · **`caregiver` → 403**
- import: **`POST /api/v1/visits/imports/nhis`** — 기존 Q189 UI

</details>

### ✅ QA-B95 g21 seed status code FE wire (`6009ba7`)
- **에이전트**: COD
- **한 일**: **`liveBackendProbe.js`** — **`liveE2eG21SeedStatusCode`** parse · **`liveConfig.js`** — **`getLiveG21SeedStatusCode()`·`isLiveG21SeedReady()` code-first** · **`buildSeedReadinessReasons`** code 우선 · detail fallback
- **내 화면/업무에 영향**: 없음 — live E2E harness만
- **상태**: FE 완료 · FAQ **Q732·Q729 deepen** · DEPLOYMENT **§11-3** · CHANGELOG 383차

<details>
<summary>자세히</summary>

- FE: `6009ba7` (on `f851a59` blocker scoping)
- **`not-applicable` code → `isLiveG21SeedReady()=true`**
- skip reason: **`g21 seed status code: service-unavailable`** — detail **`g21-seed=`** reason **생략**
- test: **`liveE2eHarness.test`** — **`prefers service-unavailable status code for G21 seed readiness reason`**

</details>

## 2026-06-27

### 📄 TWR 382차 — ops 운영 문서 보강 (doc-only)
- **에이전트**: TWR
- **한 일**: **Q729 신규** — QA-B95 **`liveE2eG21SeedStatusCode`** machine-readable field (`0f19767`) · **Q730 신규** — FE **G21 blocker suite scoping** (`f851a59`) · baseline **`0f19767`/`f851a59`**
- **내 화면/업무에 영향**: 없음 — 문서만 갱신
- **상태**: FAQ **Q729·Q730** · DEPLOYMENT **§11-3·health field table** · ADMIN_GUIDE **§1-4 live E2E harness** · README **§6**

<details>
<summary>자세히</summary>

- 대상: **QA-B95 14th layer** — G21 seed **code + blocker scoping** full-stack triage
- P2 carry: **G-CLIENT-CONTRACT-BULK-PRINT FE wire** · **program reports FE `branchId`** · **7-5 live PG** · **J03 Solapi live dispatch**

</details>

### ✅ QA-B95 g21 seed status code machine-readable expose (`0f19767`)
- **에이전트**: COD
- **한 일**: **`liveE2eG21SeedStatusCode`** — **`GET /health`** · **`GET /live-e2e/probe`** **`g21SeedStatusCode`** · **`resolveG21SeedStatusCode`** — disabled·service-unavailable·error·not-applicable·branch-missing-or-inactive·applicable
- **내 화면/업무에 영향**: 없음 — live E2E·IT triage만
- **상태**: BE 완료 · FAQ **Q729·Q727 deepen** · DEPLOYMENT **§11-3** · CHANGELOG 382차

<details>
<summary>자세히</summary>

- BE: `0f19767` (on `4df9465` bulk export)
- codes: **`disabled`** · **`service-unavailable`** · **`error`** · **`not-applicable`** · **`branch-missing-or-inactive`** · **`applicable`**
- detail 문자열(`liveE2eG21SeedStatusDetail`) **기존 유지** — code는 **분류 전용**

</details>

### ✅ QA-B95 g21 seed blocker suite scoping (`f851a59`)
- **에이전트**: COD
- **한 일**: **`liveConfig.js`** — **`isG21Blocker`** — **`g21 seed missing`·`g21 seed disabled`·`g21 seed service unavailable`** wording variant · **`requireG21Ready=false`** suite에서 G21 blocker **필터**
- **내 화면/업무에 영향**: 없음 — live E2E harness만
- **상태**: FE 완료 · FAQ **Q730·Q727 deepen** · DEPLOYMENT **§11-3** · CHANGELOG 382차

<details>
<summary>자세히</summary>

- FE: `f851a59` (on `a727862` g21 detail parse)
- general **`liveDescribe`** — **`g21-seed-service-unavailable`** blocker **무시** · **`liveG21Describe`** — **유지**
- test: **`liveE2eHarness.test`** — ignores g21 service-unavailable when G21 not required

</details>

### 📄 TWR 381차 — ops 운영 문서 보강 (doc-only)
- **에이전트**: TWR
- **한 일**: **Q726 신규** — **G-CLIENT-CONTRACT-BULK-PRINT** `GET /api/v1/clients/care-plan-forms/bulk-export` (`4df9465`) · **Q727 신규** — QA-B95 **`g21SeedStatusDetail` probe align** (`14964f6`/`a8f4e8e`/`a727862`) · **Q728 신규** — **UXD-166** committee **`ds-segmented`·`<time>`** (`4e574ce`) · baseline **`4df9465`/`a727862`**
- **내 화면/업무에 영향**: 없음 — 문서만 갱신
- **상태**: FAQ **Q726·Q727·Q728** · USER_MANUAL **§3-3 bulk export · §4-7 UXD-166** · ADMIN_GUIDE **§6-2-2a bulk** · DEPLOYMENT **§1-4·§11-3** · README **§6**

<details>
<summary>자세히</summary>

- 대상: **ezCare FAQ 21507 급여제공 변경계약서 일괄 출력** — BE API only · **FE wire P2**
- P2 carry: **program reports FE `branchId`** · **7-5 live PG** · **J03 Solapi live dispatch** · **M6 6-2~6-4 `/safety/*`**

</details>

### ✅ G-CLIENT-CONTRACT-BULK-PRINT care plan bulk export API (`4df9465`)
- **에이전트**: COD
- **한 일**: **`GET /api/v1/clients/care-plan-forms/bulk-export`** — **plan-year** 급여제공 **변경계약서** plain-text **일괄 첨부** · **`ClientCarePlanFormService.exportBulkChangeContractsText`** · **`MustApiEndpointRoutingTest`** lock
- **내 화면/업무에 영향**: **사회복지사·센터장** — Swagger·연동으로 **지점·연도별 다수 이용자 계약서** 한 번에 출력 가능 · **화면 버튼은 아직 없음 (P2)**
- **상태**: BE 완료 · FAQ **Q726** · USER_MANUAL **§3-3** · ADMIN_GUIDE **§6-2-2a** · DEPLOYMENT **§1-4**

<details>
<summary>자세히</summary>

- BE: `4df9465` (on `14964f6` QA-B95 probe)
- query: **`planYear`** 필수 · **`branchId`** optional · **`clientIds`** optional (복수 UUID)
- RBAC: **`hq_admin`·`branch_admin`·`social_worker`** · **`caregiver` → 403**
- empty branch/year → **`404`「해당 연도 급여제공계획서가 없습니다.」**
- filename: **`benefit-change-contracts-{planYear}.txt`**

</details>

### ✅ QA-B95 g21-seed status detail probe full-stack (`14964f6` · `a8f4e8e` · `a727862`)
- **에이전트**: COD
- **한 일**: **BE** — **`LiveE2eOperationReadinessSupport.resolveG21SeedStatusDetail`** 중앙화 · **`/live-e2e/probe`** **`g21SeedStatusDetail`** 노출 · **FE** — health probe parse · **`g21-seed=service-unavailable`** skip reason **우선**
- **내 화면/업무에 영향**: 없음 — live E2E·IT triage만
- **상태**: BE+FE 완료 · FAQ **Q727·Q719 deepen** · DEPLOYMENT **§11-3** · CHANGELOG 381차

<details>
<summary>자세히</summary>

- BE: `14964f6` — `/health`·`/live-e2e/probe` **동일 detail 문자열**
- FE: `a8f4e8e` — **`liveBackendProbe`·`liveConfig`·`liveGlobalSetup`** wire
- FE: `a727862` — **`parseG21SeedReasonsFromDetail`** service-unavailable **1순위**

</details>

### ✅ UXD-166 committee meeting a11y polish (`4e574ce`)
- **에이전트**: UXD
- **한 일**: **`StaffCommitteeMeetingPage`** — FilterChips **`.ds-segmented`** · 회의일 **`<time dateTime>`** · **`components.css`** — **`.ds-page-section`·`.ds-form-grid--inline`** FE-16 승격
- **내 화면/업무에 영향**: **위원회·보호자 회의록** — 스크린리더·시맨틱 마크업 개선 · 동작 동일
- **상태**: FE 완료 · FAQ **Q728·Q723 deepen** · USER_MANUAL **§4-7-0d**

<details>
<summary>자세히</summary>

- FE: `4e574ce` (on `8ed60cb` committee page)
- pattern: **`BillingReportPage`** segmented control · WCAG **1.3.1** date semantics

</details>

### 📄 TWR 380차 — ops 운영 문서 보강 (doc-only)
- **에이전트**: TWR
- **한 일**: **Q725 신규** — **V182 `staff_committee_meeting_logs` defense-in-depth** (`b4958f1`) · **Q723 deepen** — DB CHECK 2종·장소 공백 거부 · baseline **`b4958f1`/`8ed60cb`**
- **내 화면/업무에 영향**: 없음 — 문서만 갱신
- **상태**: FAQ **Q725·Q723 deepen** · USER_MANUAL **§1-3·§1-5·위원회 회의록** · ADMIN_GUIDE **§6-2-22·V182** · DEPLOYMENT **§1-4·V182 smoke** · README **§6**

<details>
<summary>자세히</summary>

- 대상: **V181 잔여 갭** — `location` 공백-only·`finalized_at < created_at` raw SQL 경로 차단 (V155/V178 패턴)
- P2 carry: **program reports FE `branchId`** · **7-5 live PG** · **J03 Solapi live dispatch** · **M6 6-2~6-4 `/safety/*`**

</details>

### ✅ V182 staff committee meeting log defense-in-depth (`b4958f1`)
- **에이전트**: DBA
- **한 일**: **Flyway V182** — `chk_staff_committee_meeting_logs_location_nonempty` · `chk_staff_committee_meeting_logs_finalized_after_created` — V181 `staff_committee_meeting_logs` 앱 단 검증 DB 미러
- **내 화면/업무에 영향**: **위원회·보호자 회의록** — 정상 UI·API 동작 동일 · **장소 공백-only·역행 확정 시각** raw SQL 적재 거부
- **상태**: BE 완료 · FAQ **Q725** · ADMIN_GUIDE **§6-2-22** · DEPLOYMENT **§1-4 V182** · DATA_RETENTION §4-1 (기반재)

<details>
<summary>자세히</summary>

- BE: `b4958f1` (on `3ae8098` export API + V181)
- CHECK 1: `location IS NULL OR length(btrim(location)) > 0`
- CHECK 2: `finalized_at IS NULL OR finalized_at >= created_at`
- backfill 불요 — V181 신규 테이블·적재 0건 가정

</details>

### 📄 TWR 379차 — ops 운영 문서 보강 (doc-only)
- **에이전트**: TWR
- **한 일**: **Q723 신규** — **G-STAFF-COMMITTEE-MEETING-LOG** `/staff/committee-meetings` full-stack (`68b08b0`/`0342076`/`3ae8098`) · **Q724 신규** — parity rules **empty catalog hide** (`8ed60cb`) · **Q722 deepen** — bootstrap hint **skip diagnostics** (`fcc16ca`) · baseline **`3ae8098`/`8ed60cb`**
- **내 화면/업무에 영향**: 없음 — 문서만 갱신
- **상태**: FAQ **Q723·Q724·Q722 deepen** · USER_MANUAL **§1-3·§1-5·§4-7-0d** · ADMIN_GUIDE **§6-2-22·V181** · DEPLOYMENT **§1-4·§2-2** · README **§6**

<details>
<summary>자세히</summary>

- 대상: **케어포 8-6 위원회·보호자 회의록** — ezCare FAQ **21601** demand-signal · **US-R08**
- P2 carry: **program reports FE `branchId`** · **7-5 live PG** · **J03 Solapi live dispatch** · **M6 6-2~6-4 `/safety/*`**

</details>

### ✅ G-STAFF-COMMITTEE-MEETING-LOG finalized export API (`3ae8098`)
- **에이전트**: COD
- **한 일**: **`GET /api/v1/staff/committee-meetings/{meetingId}/export`** — **FINALIZED** 회의록 **plain-text** 첨부 다운로드 · **`StaffCommitteeMeetingService.exportMeetingText`** · routing/RBAC test lock
- **내 화면/업무에 영향**: **위원회·보호자 회의록** — **확정 후 「출력」** 가능
- **상태**: BE 완료 · FAQ **Q723** · USER_MANUAL **§4-7-0d** · DEPLOYMENT **§1-4**

<details>
<summary>자세히</summary>

- BE: `3ae8098` (on `68b08b0` CRUD + V181)
- before: CRUD·finalize only — print export 없음
- after: **`text/plain`** UTF-8 · **`Content-Disposition: attachment`**

</details>

### ✅ G-STAFF-COMMITTEE-MEETING-LOG FE wire (`0342076`)
- **에이전트**: COD
- **한 일**: **`StaffCommitteeMeetingPage`** — **`/staff/committee-meetings`** · **`StaffContextNav`「위원회·보호자 회의록」** · CRUD Modal · **확정·출력** · **`StaffCommitteeMeetingPage.test`**
- **내 화면/업무에 영향**: **센터장·사회복지사** — **8-6 회의록 전산 작성·확정·출력**
- **상태**: FE 완료 · FAQ **Q723** · USER_MANUAL **§4-7-0d** · ADMIN_GUIDE **§6-2-22**

<details>
<summary>자세히</summary>

- FE: `0342076` — services.js 6 API · config `staffCommitteeMeetings.js`
- meeting types: **OPERATING_COMMITTEE** · **GUARDIAN** · **WELFARE_COMPENSATION**
- RBAC UI: **`hq_admin`·`branch_admin`·`social_worker`** only

</details>

### ✅ G-STAFF-COMMITTEE-MEETING-LOG CRUD API + V181 (`68b08b0`)
- **에이전트**: COD
- **한 일**: **`StaffCommitteeMeetingController`** — **GET/POST/PATCH** · **POST …/finalize** · **Flyway V181** `staff_committee_meeting_logs` · **DRAFT/FINALIZED** lifecycle · **`RoleBasedControllerAccessTest`**
- **내 화면/업무에 영향**: **위원회·보호자 회의록** API·DB 기반
- **상태**: BE 완료 · FAQ **Q723** · DEPLOYMENT **§2-2 V181** · DATA_RETENTION §4-1

<details>
<summary>자세히</summary>

- BE: `68b08b0`
- V181: meeting_type CHECK · finalized_at guard · org/branch FK sync
- finalize 후 PATCH → **`422`「확정된 회의록은 수정할 수 없습니다.」**

</details>

### ✅ G16 parity rules empty catalog hide (`8ed60cb`)
- **에이전트**: COD
- **한 일**: **`TransportParityRulesPanel`** — API **200 + `rules:[]`** 시 **섹션 `null` 반환** · API **오류** 시 static fallback **유지** · **`TransportParityRulesPanel.test`**
- **내 화면/업무에 영향**: **`/transport/service-fees`** — 빈 catalog 시 **「NHIS 기준 규칙」** 헤딩 미표시
- **상태**: FE 완료 · FAQ **Q724·Q703 deepen** · USER_MANUAL **§5-8-1**

<details>
<summary>자세히</summary>

- FE: `8ed60cb` (on `5914b2f` parity mount)
- before: empty catalog → 빈 `<dl>` + heading only
- after: **loading·error 제외** rules 0건 → **패널 미마운트**

</details>

### ✅ QA-B95 bootstrap hint skip diagnostics (`fcc16ca`)
- **에이전트**: COD
- **한 일**: **`liveConfig.js`** — **`getLiveE2eSkipReasons`** 가 operation blocked 시 **`bootstrap enable hint: …`** reason 추가 · **`liveE2eHarness.test`** lock
- **내 화면/업무에 영향**: 없음 — **live E2E harness** triage only
- **상태**: FE 완료 · FAQ **Q722 deepen** · DEPLOYMENT **§11-3** · ADMIN_GUIDE **§1-4**

<details>
<summary>자세히</summary>

- FE: `fcc16ca` (on `4bbd54a` recovered-auth hint wire)
- pairs **`liveE2eBootstrapEnableHint`** from health when suite blocked

</details>

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
