# Ogada SaaS 판매 준비도 점검

점검일: 2026-10-07. 확인한 실제 HEAD: backend `1e8857b`, frontend `5cf667b`.

이번 요청의 범위는 개선 항목 파악과 목록 작성이다. 애플리케이션 코드는 수정하지 않았다. 기존 작업 중인 파일도 변경하지 않았다.

## 판단과 조사 범위

현재 코드는 많은 업무 화면과 테스트를 갖췄지만, 유료 고객의 데이터를 맡아 운영하는 데 필요한 신뢰성에는 큰 공백이 있다. 특히 실제 데이터가 없는 백업의 성공 기록, 모의 결제를 실제 수납 기록으로 연결하는 동작, 조회 실패를 0건으로 표시하는 동작은 판매 전 해결해야 한다.

화면 수나 문서의 모듈 완성률을 판매 준비도의 근거로 삼으면 안 된다. 고객이 첫 데이터를 넣고, 매일 기록하고, 월말 청구하고, 오류와 장애에서 복구하는 전체 흐름을 통과해야 한다.

코드, 설정, 네비게이션, 배포 문서, 테스트 구성을 조사하고 프론트 빌드 및 일부 테스트를 실행했다. 운영 사이트, 실제 브라우저 화면, 운영 DB, 외부 결제·메시지 계정은 점검하지 않았다. 따라서 화면의 미적 품질·실제 로딩 시간·기관 간 정보 유출·운영 인프라 부재를 확정한 보고서가 아니다. 제품 UX에 관한 판단은 코드 구조에서 도출한 개선 가설이며 현장 검증이 필요하다.

## 우선순위와 증거 구분

- **P0**: 고객 데이터·금액·업무 판단을 신뢰할 수 있게 하기 위한 판매 전 조건.
- **P1**: 첫 유료 고객이 반복적으로 사용할 수 있도록 파일럿에서 해결할 조건.
- **P2**: 반복 판매와 고객 수 증가를 위한 상품화·확장 조건.
- **확인**: 현재 코드나 실행 결과로 확인했다.
- **구조상 우려**: 구현 구조는 확인했지만 실제 사용 영향은 추가 측정이 필요하다.
- **검증 필요**: 결함을 확정하지 않았으며 출시 검증이 필요하다.

간편결제·CMS·알림처럼 선택적인 기능은 실제 연동을 완성하거나, 판매 범위에서 제외하고 운영 화면과 API에서 안전하게 차단해야 한다. 모든 연동을 완성해야 첫 판매가 가능한 것은 아니다.

## 개선 목록

| ID | 우선순위 | 근거 수준 | 고쳐야 할 것 | 고객 영향 및 완료 기준 |
|---|---|---|---|---|
| 01 | P0 | 확인 | **실제 백업·복구 구현** | 현재는 기관 ID·생성 시각·포맷만 담은 JSON을 만들고 SUCCESS로 기록한다. DB·사진·첨부파일·필요한 키 관리까지 복구 가능한 백업을 구성하고, 빈 환경에 복원하여 기록과 파일을 대조해야 한다. 외부에서 이미 백업 중이라면 복구 실측 증거를 확보하고 앱의 성공 표시를 실제 백업과 연결한다. |
| 02 | P0 | 확인 | **모의 간편결제의 수납 기록 차단** | 유일하게 등록된 PG 구현은 stub이며 승인 성공을 반환한다. 서비스는 이를 SUCCEEDED와 본인부담 수납으로 연결한다. 운영에서 모의 결제가 금전 기록을 바꾸지 못하게 하고, 판매 시 실제 승인 검증·중복 요청·실패·취소 흐름을 검증한다. UI에는 stub 안내가 이미 있지만 안내만으로 데이터 변경 위험이 해결되지는 않는다. |
| 03 | P0 | 확인 | **CMS 모의 출금·정산의 운영 사용 차단** | FCMS 기본값이 stub이고 모의 출금 등이 성공으로 반환된다. CMS 서비스는 성공 결과를 수납 기록으로 연결한다. 미연동 기관은 요청 자체를 차단하고, 실제 제공 시 출금 결과 확인·실패·재시도·중복 방지·정산 대사를 검증한다. |
| 04 | P0 | 확인 | **조회 실패와 ‘0건’ 분리** | 대시보드 NHIS 목록 오류는 빈 목록, 미수금·급여 한도 조회 오류는 0으로 바뀐다. 미확인 상태를 정상처럼 보게 만든다. 실패한 지표는 ‘조회 실패/확인 필요’로 표시하고 개별 재시도 및 마지막 성공 시각을 제공한다. |
| 05 | P1 | 확인 | **작업 중 토큰 갱신·세션 복구** | 공통 API는 401 자동 갱신이 없고 AuthContext는 부팅 때만 refresh한다. 비활성 경고의 ‘연장’도 타이머만 초기화한다. 기본 30분 access token이 만료되면 활동 중에도 요청이 실패할 수 있다. 자동 갱신을 한 번만 공유하고, 인증 실패 시 입력을 보존하면서 재로그인으로 연결한다. |
| 06 | P1 | 확인 | **API 대기 시간과 장애 복구 처리** | 공통 fetch에 기본 timeout이 없다. 페이지별 옵션을 전달할 수 있지만 전체 요청의 대기 시간을 통제하는 정책이 없다. 조회에는 중단·재시도를 제공하고 저장은 결과 확인 및 중복 방지 없이 자동 재전송하지 않는다. |
| 07 | P1 | 확인 | **화면 예외 복구** | 루트·레이아웃을 포함해 ErrorBoundary 구현을 찾지 못했다. 렌더링 예외 및 lazy chunk 로딩 실패를 사용자가 복구할 수 있도록 페이지별 오류 화면·재시도·오류 추적을 연결한다. |
| 08 | P1 | 확인 | **고객 화면에서 개발 설명 제거** | 로그인 화면에 JWT·API 경로·sessionStorage 설명, 간편결제 패널에 ‘v2 P2·스텁’ 설명이 노출된다. ‘로그인이 유지되는 조건’, ‘서비스 이용 불가’, ‘관리자 문의’처럼 고객의 행동에 필요한 문구로 바꾸고 개발 상태는 관리 도구로 옮긴다. |
| 09 | P1 | 구조상 우려 | **메뉴와 첫 화면을 현장 업무 중심으로 축소** | hq_admin 92개, branch_admin 88개, social_worker 72개, caregiver 43개 메뉴를 계산했다. 역할 필터와 접기 기능은 있으나 현장 직원도 큰 메뉴 집합을 다룬다. 서비스 유형·기관 설정에 맞춰 필요한 메뉴만 노출하고 오늘 할 일·즐겨찾기·최근 이용자·업무 검색을 제공한다. 실제 직원이 핵심 업무를 도움 없이 수행하는지 검증한다. |
| 10 | P1 | 구조상 우려 | **대시보드의 행동 우선순위와 부분 로딩 개선** | 다수 compliance 지표·상태 카드와 fallback API를 조합한다. NHIS 조회가 기본 대시보드보다 먼저 대기된다. 오늘 처리할 출석·미작성 기록·청구 오류를 우선 보여주고, 상세 점검은 별도 영역으로 이동한다. 주요 카드부터 독립적으로 표시하고 요청 수·대기 시간을 측정한다. |
| 11 | P1 | 확인 | **초기 로딩 비용 축소** | 빌드 결과 메인 JS 1,318.22kB, gzip 324.28kB; 차트 JS 367.09kB, CSS 160.97kB. 여러 페이지를 App에서 정적 import한다. 주요 라우트를 분리하고 필요한 화면에서 차트를 불러온다. 실기기·저속 네트워크에서 로그인과 첫 업무 화면의 로딩 시간을 측정한다. 번들 크기만으로 체감 속도를 확정하지 않는다. |
| 12 | P1 | 구조상 우려 | **첨부파일 저장을 운영 배치 구조와 맞추기** | 이용자·프로그램 사진은 기본적으로 로컬 경로에 Files.write한다. 컨테이너 교체·다중 서버에서 파일이 사라지거나 서버마다 보이지 않을 수 있다. 기존 영속 볼륨 여부를 먼저 확인하고, 공유 저장소 또는 객체 저장소·접근 제어·백업·파일 정합성을 검증한다. |
| 13 | P1 | 확인 | **인증 요청 제한의 확장성과 메모리 관리** | AuthRateLimitService는 프로세스 안의 ConcurrentHashMap을 쓰며 오래된 키를 삭제하지 않는다. 다중 서버에서는 제한이 분산되고 고유 식별자가 계속 쌓일 수 있다. 키 만료·상한을 넣고 다중 서버 배포 시 공유 제한 또는 게이트웨이 정책을 적용한다. |
| 14 | P1 | 확인 | **브라우저에서 업무가 끝나는 테스트와 CI 마련** | live E2E는 Vitest/jsdom이며 현재 package.json에 실제 브라우저 E2E 명령이 없다. 저장소의 GitHub 워크플로는 실패 이슈 생성·에스컬레이션이며 빌드·테스트 작업을 찾지 못했다. 외부 CI 여부를 확인하고, 브라우저+실제 API+DB로 핵심 업무와 기관 격리를 검증하는 출시 게이트를 만든다. |
| 15 | P1 | 확인 | **배포 절차와 실제 저장소 일치** | README가 안내하는 .env.example·docker-compose.dev.yml·test:e2e가 없고, 문서는 Spring Boot 3.5.3이라지만 실제 pom은 3.3.1이다. 현재 코드 기준으로 설치·배포·키 주입·마이그레이션·롤백을 재현하고 성공한 버전만 기록한다. |
| 16 | P0 | 검증 필요 | **기관·지점·보호자 간 데이터 격리 실증** | JWT scope와 TenantContext, 역할 테스트는 존재한다. 유출이 확인된 것은 아니다. 실제로 기관 A/B를 만들고 목록·직접 ID 조회·다운로드·사진·검색·통계·지점 전환에서 다른 기관 및 연결되지 않은 보호자의 데이터가 나오지 않는지 검증한다. |
| 17 | P1 | 검증 필요 | **수납·일정·기록의 동시 변경 검증** | @Version·명시적 JPA lock·공통 idempotency 처리를 검색에서 찾지 못했다. DB 제약이나 조건부 갱신의 방어 여부까지 조사해야 하므로 중복 수납이나 덮어쓰기 결함을 확정하지 않는다. 이중 클릭·두 직원 동시 저장·네트워크 단절·중복 통지에서 금액이 한 번만 반영되고 충돌이 사용자에게 표시되는지 검증한다. |
| 18 | P1 | 구조상 우려 | **긴 기록 폼의 입력 보존** | 가정통신문에는 초안 기능이 있지만 공통 useBlocker/beforeunload 처리는 찾지 못했다. 건강·욕구사정·계획서 등 긴 폼에서 화면 이동·지점 변경·세션 만료·저장 실패 시 입력 보존과 이탈 경고가 동작하는지 점검한다. 민감정보를 장기간 브라우저에 남기는 방식은 피한다. |
| 19 | P1 | 검증 필요 | **실제 알림의 도달·실패 상태 검증** | SMS·알림톡·메일 기본값은 stub이고 개발 provider는 발송 성공을 반환한다. 실제 Solapi/SMTP 구현과 readiness UI는 이미 있다. 실제 운영 설정과 수신 결과를 확인하고, 미발송·접수·도달·실패를 구분하며 재시도와 중복 방지를 검증한다. |
| 20 | P1 | 검증 필요 | **암호화 키·운영 설정·장애 대응 검증** | PII AES-GCM 암호화는 존재하지만 해당 서비스는 사용 시 키를 검사한다. 키 누락·교체·백업 복원, 테스트 bootstrap 비활성, 운영 오류 수집·알림·처리 절차를 실제 배포에서 검증한다. 별도 운영 계층에 이미 구성돼 있을 수 있다. |
| 21 | P1 | 검증 필요 | **신규 기관의 첫날·월말 업무 완결성** | 기관·지점·직원·수급자·수가·보호자 설정 및 여러 import 기능은 있다. 신규 직원이 기존 엑셀을 가져와 첫 출석·일일 기록·청구·입금 대사를 끝내는 전체 흐름은 이번에 실행하지 못했다. 단계별 설정 체크리스트와 예제 파일·행별 오류·재가져오기·데이터 대조를 검증한다. |
| 22 | P2 | 검증 필요 | **SaaS 상품과 고객 수명주기 구성** | 검토한 기관 관리와 플랫폼 화면에서 요금제·구독·체험·서비스 이용 한도를 확인하지 못했다. 별도 운영 여부를 확인하고 상품별 제공 범위·계약·청구·연체·해지·데이터 반출·지원 창구를 정한다. 초기 수동 계약도 가능하지만 기관의 돌봄 청구와 SaaS 이용료를 별도로 관리해야 한다. |

## 중요한 코드 근거

- 백업: [FileTenantBackupExecutor.java](../../src/backend/src/main/java/com/ogada/backend/settings/domain/FileTenantBackupExecutor.java), [BackupRunService.java](../../src/backend/src/main/java/com/ogada/backend/settings/domain/BackupRunService.java)
- 간편결제: [EasyPayConfig.java](../../src/backend/src/main/java/com/ogada/backend/billing/easypay/config/EasyPayConfig.java), [StubEasyPayProvider.java](../../src/backend/src/main/java/com/ogada/backend/billing/easypay/provider/StubEasyPayProvider.java), [EasyPayService.java](../../src/backend/src/main/java/com/ogada/backend/billing/easypay/domain/EasyPayService.java), [EasyPayPanel.jsx](../../src/frontend/src/components/ui/EasyPayPanel.jsx)
- CMS: [StubFcmsClient.java](../../src/backend/src/main/java/com/ogada/backend/billing/cms/provider/StubFcmsClient.java), [CmsService.java](../../src/backend/src/main/java/com/ogada/backend/billing/cms/domain/CmsService.java)
- 조회 실패: [DashboardPage.jsx](../../src/frontend/src/pages/DashboardPage.jsx), 특히 NHIS `.catch(() => [])`, overdue/capGuard 예외의 0건 처리
- 세션·요청: [http.js](../../src/frontend/src/api/http.js), [AuthContext.jsx](../../src/frontend/src/auth/AuthContext.jsx), [SessionTimeoutProvider.jsx](../../src/frontend/src/components/ui/SessionTimeoutProvider.jsx)
- 화면 구조·메뉴: [main.jsx](../../src/frontend/src/main.jsx), [App.jsx](../../src/frontend/src/App.jsx), [navConfig.js](../../src/frontend/src/layout/navConfig.js), [AppShell.jsx](../../src/frontend/src/layout/AppShell.jsx)
- 개발 설명: [LoginPage.jsx](../../src/frontend/src/pages/LoginPage.jsx), [EasyPayPanel.jsx](../../src/frontend/src/components/ui/EasyPayPanel.jsx)
- 파일: [ClientPhotoStorageService.java](../../src/backend/src/main/java/com/ogada/backend/clients/domain/ClientPhotoStorageService.java), [ProgramPhotoStorageService.java](../../src/backend/src/main/java/com/ogada/backend/programs/domain/ProgramPhotoStorageService.java)
- 요청 제한: [AuthRateLimitService.java](../../src/backend/src/main/java/com/ogada/backend/auth/domain/AuthRateLimitService.java)
- 테스트·배포: [vitest.live.config.js](../../src/frontend/vitest.live.config.js), [package.json](../../src/frontend/package.json), [workflows](../../.github/workflows), [README.md](../../README.md), [DEPLOYMENT_GUIDE.md](../ops/DEPLOYMENT_GUIDE.md), [pom.xml](../../src/backend/pom.xml)
- 알림·암호화: [NotificationConfig.java](../../src/backend/src/main/java/com/ogada/backend/notification/config/NotificationConfig.java), [StubSmsProvider.java](../../src/backend/src/main/java/com/ogada/backend/notification/provider/StubSmsProvider.java), [PiiCryptoService.java](../../src/backend/src/main/java/com/ogada/backend/clients/domain/PiiCryptoService.java)

## 권장 실행 순서

1. **판매할 범위 확정 및 데이터 신뢰성 확보**: 01~04를 먼저 해결하고, 미연동 결제·CMS·알림은 실제 고객 데이터에서 사용할 수 없도록 한다. 16의 기관 격리와 20의 운영 설정을 검증한다.
2. **매일 쓰는 흐름 안정화**: 05~08, 17~19를 처리하여 세션·저장·오류 때문에 작업이 끊기거나 기록이 사라지지 않도록 한다.
3. **현장 경험 개선**: 09~11, 18, 21을 실제 기관 직원과 검증한다. 입소 등록 → 송영·출석 → 기록 → 청구·수납을 대표 시나리오로 삼는다.
4. **운영 재현과 반복 판매**: 12~15, 20, 22를 정리하여 새 고객과 새 서버에도 같은 품질로 배포·지원한다.

디자인 개선은 3단계의 중요한 과제다. 실제 화면을 브라우저로 점검해 글자 크기, 표 밀도, 모바일 입력, 클릭 수, 상태·오류 안내를 평가해야 한다. 이번 코드 점검만으로 디자인 완성도를 점수화하지 않았다.

## 판매 전 통과 조건

- 다른 기관·지점·보호자의 정보를 목록·직접 접근·파일 다운로드로 얻을 수 없다.
- 백업을 새 환경에 복원해 이용자 기록·청구·사진·첨부파일을 대조할 수 있다.
- 모의 승인·모의 출금·모의 발송이 운영의 실제 성공 기록으로 오인되지 않는다.
- 조회 실패를 정상·0건으로 표시하지 않는다.
- 토큰 만료·저장 실패·동시 수정·중복 요청 시 입력과 금액을 보호한다.
- 실제 직원이 신규 기관 설정, 일일 업무, 월말 청구·수납을 완료한다.
- 위 시나리오가 실제 브라우저·API·DB에서 재현되고 배포 전에 검사된다.
- 운영 배포·롤백·오류 감지·고객 지원 절차의 담당자와 실행 기록이 있다.

## 이번 검증 결과

- `npm run build`: 성공. 메인 JS 1,318.22kB(gzip 324.28kB), CSS 160.97kB(gzip 23.19kB), 500kB 초과 chunk 경고 확인.
- 프론트 인증·API 테스트: `http.test.js`, `session.test.js`, `AuthContext.test.jsx`, `sevenRoleRouteGuard.test.jsx` — **4개 파일 / 37개 테스트 통과**.
- 백엔드: `BackupRunServiceTest`, `EasyPayServiceTest`, `StubEasyPayProviderTest`, `AuthRateLimitServiceTest` — **26개 테스트 통과**. 첫 실행은 현재 환경의 Mockito JVM self-attach 제약으로 중단됐고, 기존 Byte Buddy agent를 JVM 시작 시 주입하여 재실행했다. 제품 결함으로 분류하지 않았다.
- 백엔드 재실행 명령: `mvn -o -Dtest=BackupRunServiceTest,EasyPayServiceTest,StubEasyPayProviderTest,AuthRateLimitServiceTest -DargLine=-javaagent:/home/ubuntu/.m2/repository/net/bytebuddy/byte-buddy-agent/1.14.17/byte-buddy-agent-1.14.17.jar test`
- 메뉴 측정: `navGroupsForRole()` 결과 hq_admin **92**, branch_admin **88**, social_worker **72**, caregiver **43**, guardian **2**개 항목.
- 현재 파일 기준 명시적인 `path="..."` 라우트 **132개**, `*Page.jsx` 파일 **106개**. 라우트 수에는 리다이렉트 등이 포함되며 기능 완성률을 뜻하지 않는다.
- 전체 테스트, 실제 브라우저 E2E, 운영 DB·파일 복원, 실결제·실발송, 부하 테스트는 실행하지 않았다. 일부 단위 테스트 통과는 판매 가능 판정을 뜻하지 않는다.
