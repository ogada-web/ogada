<!-- doc:owner=PLN doc:audience=COD,TSR,UXD,DBA,BNK,TWR updated=2026-06-06T23:58:00+09:00 -->
# 기획 메모 (planning/PLAN_NOTES.md)

> **작성**: planner 에이전트 (`PLN`)  
> **최종 갱신**: 2026-06-06 (20차 — TSR 28·29차 B02 recurrence #4 Open→Planned·UXD 13차 Switch·셀프 체크인 토글 흡수·COD 20차 7역할 JWT 로그인·라우트 가드 Vitest 단위 E2E 자동화 정식 충족·US-UX-03 신설·BE-6 패턴 #4 재발 종결 공언 철회)  
> **상태**: 초안 (사용자 승인 전)

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

---

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

### 추가 질문

다음 항목이 확정되기 전까지 상세 스펙·일정·구현 범위는 가정으로만 기재한다.

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
33. **보호자 초대 채널** — v1.1 US-J01: 이메일 링크 vs SMS 코드 중 1종 확정 (EZCARE는 기관 초대 — 채널 미공개).
34. **이지케어 주간보호 전용 UX** — EZCARE 앱 주야간 메뉴 vs 방문요양 분리 (`BENCHMARK_REPORT.md` §8 #3).
35. **수가표 시간대(`duration_band`) 축** (2026-06-06, 4차 벤치마크 G9) — 공단 2026 수가는 **등급×이용시간대(3~6h/6~8h/8~10h/10~13h/13h+)** 2차원([롱텀 수가](https://www.longtermcare.or.kr/npbs/e/b/502/npeb502m01.web?menuId=npe0000002742)). **파일럿 센터 표준 이용시간 확인** 후 v1 1밴드 고정값 결정, v1.1 다밴드 도입 시 §3-9-1·ERD `fee_schedules` 보강 (결정 42).
36. **coder 장기 미조치 에스컬레이션** (2026-06-06, 9차 신설 → 11차 부분 해소 → 15차 backend 해소 → 16차 frontend B07 Fixed → 17차 B02 #3 Fixed·B07 #2 신규 → 18차 양 스트림 패턴 종결 신호 → 19차 양 스트림 패턴 완전 종결 공언 → **20차 BE-6 패턴 #4 재발·종결 공언 철회**): **20차(2026-06-06T23:58) — BE-6 종결 공언 철회·운영 게이트 권고 재검토 필요**.
    - **19차 공언**: BE-6 #3 Fixed 후 22차→24차→26차 **5커밋 무재발**(working tree CLEAN 유지) → 「BE-6 패턴 완전 종결」 공언, 운영 게이트(pre-commit hook 등) 권고 보류 확정.
    - **20차 재발(BE-6 #4)**: TSR 28차에서 COD 18차 `c3f3146` 후 신규 7역할 JWT 로그인 E2E 통합 테스트 `src/test/java/com/ogada/backend/security/SevenRoleJwtLoginE2eTest.java`(384 lines, Spring Security filter chain·JwtAuthFilter·UserDetailsService 통합 라이브 발급/검증) 작성 → develop HEAD 미커밋·working tree DIRTY 1 untracked → BE-6 #4. 19차 5커밋 무재발 → **20차 1커밋 dirty**. 19차 「테스트 추가 → 즉시 커밋」 정착 공언 실패.
    - **FE-6 무재발 6커밋 유지**: `a84473f`→`ed1bf22`→`404a30e`→`cc34f23`→`07fd305`(UXD 13차 Switch)→`57ff3c0`(COD 20차 7역할 JWT 로그인·라우트 가드 단위 E2E) — 양 스트림 비대칭(frontend 정착·backend 재발).
    - **잔여 Planned 5건**(B01·**B02 #4**·B03·B05·SEC-007). B02 #4 commit 시 v1 R-04 라이브 7역할 JWT 로그인 E2E 완료 기준 동시 충족 → B01 ready 후보(SEC-007 동반).
    - **결정 52(20차 갱신)**: 흡수 **7묶음** ~89 files — ① v1.2 P0 `a72e249`(42), ② US-D03 `3fc549a`(2), ③ UXD 10차 `5656e19`(7), ④ UXD 11차 `2d742b3`(7), ⑤ COD 17차 `a84473f`+`ed1bf22`(10), ⑥ UXD 12차 `404a30e`(3)+COD 18차 `c3f3146`(1)+COD 19차 `cc34f23`(3), ⑦ **UXD 13차 `07fd305`(7)+COD 20차 `57ff3c0`(4)** — 총 12커밋, v1.1 develop→test merge 동반.
    - **운영 게이트 권고 재검토 (20차 신규)**: ① backend Maven CI에 「신규 `*Test.java` 파일이 working tree에만 존재」 fail-fast 검증 추가, ② coder 워크플로우 가이드에 「테스트 작성 직후 `mvn -q test` PASS → 즉시 develop commit」 체크포인트 명시, ③ planner 자동 sync 시 「BE-6 패턴 #N 재발」 카운터 자동 갱신. 19차의 「권고 공식 보류」를 20차에 **재오픈**.
    - **종결 패턴 진단 (20차)**: ① BE-6 위반 #1·#2·#3 모두 해소 → 19차 5커밋 무재발 종결 공언 → **20차 #4 재발**(공언 철회). ② FE-6 위반 #1·#2 모두 해소 → **20차 6커밋 무재발 유지**(공언 유효). ③ 잔여는 기능 갭(라이브 E2E·J01) + 절차(merge ready) + **backend 1 commit(B02 #4 `SevenRoleJwtLoginE2eTest`)**.

### [COD] 보호자 초대 API 계약 확인

- **배경**: frontend `US-J01` 구현을 위해 `ClientDetailPage`에서 `POST /api/v1/guardians/invitations` 호출 경로를 반영했으나, `API_SPEC.md`에 초대 엔드포인트·요청 스키마가 아직 명시되지 않았다.
- **요청**: `API_SPEC.md`에 `US-J01` 초대 API(경로·요청 필드·응답·에러 코드, 이메일/SMS 채널 확정)를 추가해 달라.
- **영향**: 현재 프론트는 404/501 시 "백엔드 미구현" 안내로 graceful fallback 처리되며, J01 E2E 완료 체크는 API 계약 확정·구현 전까지 보류된다.

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
