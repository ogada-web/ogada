<!-- doc:owner=TWR doc:audience=human updated=2026-07-20T13:56:00Z -->
# ogada 변경 기록

> **누가 쓰나**: TWR(문서 에이전트)  
> **누가 읽나**: 운영·기획 담당자 — 개발 세부사항은 각 카드 맨 아래 「자세히」만 보면 됩니다.  
> **기준**: develop 최신 코드 · BE **`a0a6643`** · FE **`554a319`** · **133 route·106 page·Flyway V1–V196** · **모듈 97.41%**

## 읽는 법

1. **최근 7일 요약**만 봐도 됩니다.
2. 카드의 **내 화면/업무에 영향**이 「없음」이면 앱 체감 변화 없음(문서·테스트·내부 작업).
3. **3개월 지난 날짜**는 이 파일에서 삭제합니다. 오래된 내용은 남기지 않습니다.

## 최근 7일 요약

- **2026-07-20** — **기관 공지 상세 — 불안전 첨부 차단 사유를 구체 안내로 표시**(예: `localhost6` 별칭이면 「첨부 링크 형식이 올바르지 않습니다.」 — 예전엔 스킴 오류로만 보이던 것을 실제 위반 유형과 맞춤, Q955) · **기관 공지 첨부 hosts-file resolver 잔여 별칭 서비스 계층 회귀 테스트 고정**(`broadcasthost`·`ip6-allnodes`·`ip6-allrouters`·`ip6-mcastprefix`·`localhost.localdomain` — 동작 변화 없음) · **기관 공지 첨부 localhost6 hosts-file 별칭 서비스·화면 폼 계층 회귀 테스트 고정**(동작 변화 없음) · **기관 공지 첨부 localhost6 hosts-file 별칭 사전 차단**(`localhost6`·`localhost6.localdomain`·`localhost6.localdomain6` — IPv6 루프백 우회 주소 저장 전 거부) · **기관 공지 첨부 URL 입력 도움말·스크린리더 연결**(13축 검증 규칙을 입력칸 아래 도움말로 표시·`aria-describedby` 연결, UXD-208) · **기관 공지 첨부 URL 도움말 보강**(SEC-D46 attachment URL guard 13축 설명 UXD-208 — 사용자 질문 예방, 매뉴얼 참고 링크) · **일괄 확정취소 확인번호 6자리 고정**(SEC-D44 batch-unconfirm 확인 로직 재점검, API_SPEC 갱신) · **기관 공지 첨부 hosts-file resolver 별칭 6경로 회귀 테스트 고정**(동작 변화 없음) · **기관 공지 첨부 hosts-file resolver 별칭(broadcasthost·ip6-allnodes 등) 사전 차단** · **기관 공지 첨부 localhost 해석 별칭(localdomain·ip6-localhost·ip6-loopback) 사전 차단** · **기관 공지 첨부 변형 IP·내부망 도메인 사전 차단**(숫자만/16진수처럼 보이는 주소·앞자리 0 붙은 IP·짧은 IP 표기·`.local`/`.internal`/`.corp` 등 저장 전 거부) · **기관 공지 첨부 IP·localhost 주소 사전 차단** · **일괄 확정취소 확인번호 오류를 입력칸 한곳으로** · **잔여 표 날짜 칸 스크린리더 형식 보강** · **기관 공지 첨부 비기본 포트·깨진 URL 사전 차단** · **첨부 허용 호스트 정규화·health 허용 목록 노출** · **기관 공지 첨부 호스트 허용 목록** · **알림톡 중첩 페이로드 마스킹** · **리포트 기간 오류 고친 뒤 안내 즉시 해제** · **안전 점검 기간·배차/의료비 a11y** · **안전 점검 조회 날짜 범위 제한** · **간호급여 리포트 역방향 기간 사전 차단**
- **2026-07-19** — **건강·투약 이력 시각을 기계가 읽을 수 있는 형태로 표시**(건강 페이지 기록 이력·이용자 상세 건강 탭의 기록/투약/사건 시각을 스크린리더가 정확히 해석하는 표준 형식으로 감쌈 — 화면 글자 그대로, UXD-197~204에 이어 완료, UXD-205) · **욕구사정 만족도 중복 제거**(React key prop 추가로 페이지 갱신 시 목록 중복 표시 방지, QA-B627) · **직원 현황 CSV의 엑셀 수식 실행 위험 차단**(직원 이름이 `=`로 시작하면 엑셀이 수식으로 실행할 수 있던 위험을 앞에 작은따옴표를 붙여 글자로만 열리게 함, SEC-D33 확산) · **청구 명세·국세청 CSV를 엑셀에서 열 때 수식 실행 위험 차단**(이용자·보호자 이름 등이 `=`·`+`·`-`·`@`로 시작하면 엑셀이 수식으로 실행할 수 있던 위험을, 앞에 작은따옴표를 붙여 글자로만 열리게 함 — 금액 칸의 마이너스 숫자는 그대로 숫자로 계산 가능, SEC-D33) · **안전 점검·선임 업무일지·외출 실제 출발/복귀 시각도 기계가 읽을 수 있는 형태로 표시**(안전 점검 저장 시각·선임 요양보호사 전자서명 시각·외출 「실제」 출발→복귀 시각을 스크린리더가 정확히 해석하는 표준 형식으로 감쌈 — 화면 글자 그대로, UXD-197~203에 이어 확대, UXD-204) · **욕구사정 연도 비교 표 좁은 화면 가로 스크롤 보정**(이용자 상세 욕구사정 비교(3열) 표가 공용 표 감싸개를 거치지 않아 좁은 창·모바일에서 페이지 전체가 옆으로 밀릴 수 있던 것을, `.ds-table-wrap`으로 감싸 표 영역 안에서만 좌우 스크롤되도록 정리 — 표 글자·열 그대로, 넓은 화면 변화 없음, WCAG 1.4.10 Reflow, UXD-202) · **ADMIN_GUIDE §1-4 baseline 정합·sysadmin a11y 교차 참조**(구 `49349e4`/`5e816e6`→BE `6d3c766`/FE `6a9e85e` · SEC-D34·UXD-197~201·Q940·Q936 기능 클로저 추가 · 로그인/감사/백업/수가 이력 `<time dateTime>` §4 연결, 화면 변화 없음) · **청구·정산·보호자·백업 화면 날짜 칸도 기계가 읽을 수 있는 형태로 표시**(청구 상세 입금·환불일·수납 목록 입금일·수가/본인부담 단가 적용 시작일·백업 시작/완료 시각·청구 잠금 시각·보호자 청구 상세 입금일 등 7개 화면·8개 날짜 칸을 스크린리더가 정확히 해석하는 표준 형식으로 감쌈 — 화면 글자·표 모양 그대로, UXD-197~200에 이어 마무리, UXD-201) · **로그인 이력·감사 로그·알림 발송 이력·수가 변경 이력 화면 날짜·시각 칸도 기계가 읽을 수 있는 형태로 표시**(단일 값으로 평문 표시하던 로그인 시각·발생 시각·발송 시각·적용 시작/등록일을 스크린리더가 정확히 해석하는 표준 형식으로 감쌈 — 화면 글자 그대로, UXD-200) · **표 날짜 칸 스크린리더 안내 FAQ 통합**(UXD-197·198·199 — 리포트·목록·청구/평가/알림 표 24곳 `<time dateTime>` 적용 범위를 FAQ Q945·매뉴얼 §3-2로 한곳에 정리, 화면 표시 변화 없음) · **청구·평가·알림 목록 화면 표의 날짜 칸도 기계가 읽을 수 있는 형태로 표시**(청구 대장(입금·환불·수납일)·욕구사정·주기 위험 평가·돌봄계획 알림 이력·연체·건강 상세·보호자 상세·급여제공 결과 평가·기능회복 훈련·방문 RFID 비교 등 표에서 날짜 칸을 스크린리더가 정확히 해석하는 표준 형식으로 감쌈 — 화면 글자·표 모양 그대로, UXD-197·UXD-198에 이어 확대, UXD-199) · **목록·기록 화면 표의 날짜 칸도 기계가 읽을 수 있는 형태로 표시**(사례관리 회의·바이탈·체중·구강·응급·욕창·선임 업무일지·외출 목록 등 CRUD 표에서 날짜 칸을 스크린리더가 정확히 해석하는 표준 형식으로 감쌈 — 화면 글자·표 모양 그대로, UXD-197 리포트 개선에 이어 확대, UXD-198) · **리포트 표의 날짜 칸을 기계가 읽을 수 있는 형태로 표시**(목욕도움·요양/식사/화장실·집중배설·수급자별 급여제공·체위변경 등 표를 화면에 바로 그리는 리포트에서 날짜 칸을 스크린리더·보조기기가 정확히 해석하는 표준 날짜 형식으로 감쌈 — 화면에 보이는 날짜 글자는 그대로, 이미 표준을 쓰던 프로그램·간호급여 리포트와 형식 통일, UXD-197) · **공단·은행 엑셀 금액의 특수 공백(줄바꿈 없는 공백·전각 공백) 정상 인식**(`1[줄바꿈없는공백]250[줄바꿈없는공백]000원`·전각 IME 공백처럼 눈엔 띄어쓰기지만 보통 공백이 아닌 문자로 천 단위를 나눈 금액이 예전엔 조용히 비어 대사·입금 매칭이 틀어지던 것을, 이 특수 공백도 떼어 정확히 읽음, SEC-D34) · **공단·은행 엑셀 금액의 전각 숫자(０-９)·전각 콤마(，) 정상 인식 문서화**(전각 IME·전각 통화 서식으로 `１，２５０，０００`처럼 들어온 금액도 전각 숫자를 반각으로 바꾸고 전각 콤마를 떼어 정확히 읽음 — 기능은 이미 반영, FAQ Q939·Q941·매뉴얼 보강, SEC-D34) · **리포트 역방향 기간 오류 안내 스크린리더 접근성 확대**(목욕도움·간호급여·프로그램 등 9개 리포트에서 시작일·종료일 두 칸 모두 「오류 있음」 상태로 표시해 스크린리더가 시작일 칸에서도 원인을 안내 — 화면 표시·안내 문구는 그대로, UXD-196) · **리포트 조회 기간 거꾸로 입력 즉시 차단 확대**(목욕도움·요양/식사/화장실·체위변경·집중배설·요양 간호 등 나머지 급여제공 리포트, 간호급여 리포트, 프로그램 리포트까지 — 시작일>종료일이면 조회 전 「종료일은 시작일 이후여야 합니다.」로 종료일 칸에 바로 안내하고 지난 집계도 비움) · **BE 엑셀 금액 정규화 DRY 통합**(NHIS·은행 중복 로직 단일화) · **배차 a11y·오류 심화** 테스트 완료 · **FE 2791/2791 PASS**(UXD-197 착지·QA 검증 완료) · FE develop `e8ff8dc`(UXD-199 반영) · BE develop `6d3c766`→test pending 해소 대기(PLN 스코프 재조정 필요)
- **2026-07-18** — **공단·은행 엑셀 전각 원화 기호(￦) 붙은 금액 정상 인식**(일부 한글 엑셀·수기 입력이 반각 `₩` 대신 전각 `￦765,000`·`￦1,250,000`처럼 표시되면 예전엔 값이 조용히 비어 대사·입금 매칭이 틀어지던 것을, 전각 `￦`도 떼어 정확히 읽음, SEC-D34) · **수급자별 급여제공 리포트 기간 거꾸로 입력 즉시 차단**(`/care/reports/patient-service`에서 시작일>종료일로 조회하면 예전엔 서버까지 보낸 뒤 오류가 뜨던 것을 「종료일은 시작일 이후여야 합니다.」로 조회 전 바로 안내하고 지난 집계도 비움, L02_M11) · **공단·은행 엑셀의 원화 기호(₩) 붙은 금액 정상 인식**(엑셀이 금액 칸을 통화 서식으로 저장하면 「원」 대신 `₩765,000`·`₩1,250,000`처럼 ₩ 기호가 붙어 예전엔 값이 조용히 비면서 대사가 틀어지거나 입금 행이 자동 매칭에서 빠지던 것을, ₩을 떼어 정확히 읽음, SEC-D34) · **급여제공 서비스 집계 리포트 기간 거꾸로 입력 즉시 차단**(`/care/reports/service-summary`에서 시작일>종료일로 조회하면 예전엔 서버까지 보낸 뒤 오류가 뜨던 것을 「종료일은 시작일 이후여야 합니다.」로 조회 전 바로 안내하고 지난 집계도 비움, L02_M12) · **공단 대사 엑셀 급여일수 `15일` 표기 정상 인식**(공단 export가 붙이는 「일」 접미사 때문에 값이 비어 대사가 틀어지던 것을 「일」을 떼어 정확히 읽음, SEC-D34) · **이동서비스비 기간 오류 시 지난 목록 즉시 비움**(빈·역방향 기간으로 조회가 막힐 때 이전 기간 청구표가 남아 오류와 모순되던 것을 목록을 비워 EmptyState로 정리, G16) · **은행 입금 엑셀 금액의 공백 천 단위 구분·「원」 표기 정상 인식**(`1 250 000원` 처럼 띄어 쓴 금액이 조용히 빠져 미매칭·건너뜀이 늘던 것을 공백·「원」을 떼어 행을 살려 대사·자동 수납 정확도 향상, SEC-D34) · **이동서비스비 청구 기간(시작일·종료일) 미입력 즉시 차단**(예전엔 서버까지 보낸 뒤 400이 뜨던 것을 「조회 기간의 시작일과 종료일이 필요합니다.」로 조회·생성 전 바로 안내, G16) · **공단·RFID 엑셀에서 셀 하나가 깨져도 그 행만 건너뛰지 않고 전체가 멈추지 않도록 개선**(방문일정 엑셀의 서비스 시간이 지나치게 큰 값이면 시각 차이로 다시 계산해 행을 살리고, RFID 전송 엑셀의 태그 시각이 범위를 벗어나면 그 시각만 비워 행은 등록, SEC-D34) · **공단 대사 엑셀 금액·급여일수의 「원」·공백 표기 정상 인식**(`765,000원`·`  15  ` 처럼 표시서식이 붙어 예전엔 값이 비어 대사 상태가 「불일치·보류」로 잘못 잡히던 것을, 「원」·공백을 떼어 정확히 읽어 대사 정확도 향상) · **이동서비스비 청구 기간(시작일>종료일) 역방향 즉시 차단**(예전엔 서버까지 보낸 뒤에야 오류가 뜨던 것을 「시작일은 종료일보다 이후일 수 없습니다.」로 조회·생성 전 바로 안내, G16) · **이동서비스비 결과 안내(성공·건너뜀) 재조회 시 갱신**(기간을 바꾸거나 다시 조회하면 지난 결과 안내가 남아 있던 것을 최신 결과만 보이도록 정리) · **이동서비스비 이용자 이름 정상 표시**(목록 응답 형식이 달라 이름이 안 나오던 경우 보정) · **배차 「회차」 칸 위 마우스 휠 스크롤로 값이 몰래 바뀌던 문제 차단**(회차 칸에 커서가 있을 때 페이지를 스크롤하면 회차 숫자가 조용히 바뀌어 엉뚱한 회차로 저장될 수 있던 것을, 스크롤 시 회차 칸에서 커서를 떼어 페이지만 스크롤되도록 수정) · **배차 회차 오류 안내 중복 읽힘 정리**(서버가 회차 오류를 돌려줄 때 같은 안내가 화면 상단과 회차 칸에 두 번 뜨며 스크린리더가 두 번 읽던 것을 회차 칸 한 곳으로 정리, UXD-194) · **RFID 전송 엑셀 헤더·필수열·데이터행 누락 안내 문구 FAQ화**(방문 RFID 비교 — 잘못된 파일 형식 시 원인별 안내, Q938) · **픽업 배차 「회차」 입력 사전 검증**(1 이상 정수만 허용 — 잘못된 값은 저장 전 회차 칸에 바로 안내) · **회차 「1e2·0x1f」 같은 지수/16진수 입력 거부**(예전에는 100·31로 잘못 저장되던 것을 저장 전 오류로 차단) · **회차에 지나치게 큰 수 입력 거부**(9999999999 같은 값은 서버 한도를 넘어 원인 불명 오류가 나던 것을 「회차 값이 너무 큽니다. 다시 확인하세요.」로 사전 차단) · **회차 오류 시 회차 칸으로 커서 자동 이동**(키보드·스크린리더 사용자가 문제 칸을 바로 찾음) · **배차 정차 상한(17개) 초과 시 사유 안내**(지점·경유지 추가가 막힐 때 「정차 순서는 최대 17개까지 가능합니다.」 표시) · **엑셀 일괄등록 안내 문구를 코드 한 곳(상수)으로 정리**(「업로드할 엑셀 파일이 없습니다.」·「엑셀 파일을 읽을 수 없습니다.」 — 화면·문구 변화 없는 내부 정리, SEC-D34) · **리포트 인쇄에서 좌측/상단 메뉴 숨김**(청구·청구통계·이용자 외출·교통 월간 리포트 — 인쇄물에 앱 메뉴 미출력, UXD-192) · **엑셀 일괄등록 빈/없는 파일 안내 문구 통일**(방문·청구 NHIS도 「업로드할 엑셀 파일이 없습니다.」로 5개 화면 동일) · **손상된 엑셀(내용이 깨진 파일) 안전 거부**(엑셀 import 5개 파서 「엑셀 파일을 읽을 수 없습니다.」, SEC-D34 fail-closed) · **은행 입금 엑셀 브라우저 사전검증 추가**(업로드 전 위장·0바이트 거부, BE와 동일 규칙, SEC-D34) · **활동/이용자 사진 업로드 성공 스크린리더 안내** · **엑셀 import null·빈(0바이트)·빈 헤더 파일 fail-closed**(FE·BE 양쪽 회귀 테스트, SEC-D34)
- **2026-07-17** — **업로드 파일 서명 검증 확대**(이용자 사진·급여계약·HR·등급이력·보수교육·요양보호사 엑셀) · **직원현황 인쇄·활동 사진 오류 ARIA** · 활동 사진 magic-byte · NoBreakSpace mid-token · M12 SSO allowlist
- **2026-07-16** — live E2E **`&comma;`·`&VeryThickSpace;`** · **템플릿 카탈로그 표 행 헤더 a11y** · **알림톡 카탈로그 13종** · **VeryVery*·MathSpace·SixPerEm·fractional em·figure space** · **연계·발송 체크박스 a11y** · NoBreakSpace · bidi·zero-width · **G2 표 모바일 스크롤**
- **2026-07-15** — **G2 가정통신문·기관 공지·자료실** 게시판 FULL · **M12 회계 BPO launch·SSO** · 발송이력 board-style 필터
- **2026-07-15** — **channel-status 참고 단가** · 연계기록지 **리포트 페이지네이션** · RFID **급여제공내역 SMS 일괄** · live E2E bootstrap blocker 합성 파싱
- **2026-07-14** — 기관 공지 첨부 http(s)·복제·상세 · 가정통신문 작성 카탈로그 · M11 급여 미리보기 5화면 · M12 BPO readiness


---

## 2026-07-20

### ✅ 기관 공지 상세 — 불안전 첨부 차단 사유 구체 표시 (FE)
- **에이전트**: COD
- **한 일**: **기관 공지·자료실** 게시 행 **「보기」** 상세에서 첨부 링크가 차단될 때, 예전엔 항상 스킴 오류 문구만 보이던 것을 **SEC-D46 위반 유형**(예: `localhost6`·hosts-file 별칭 → 「첨부 링크 형식이 올바르지 않습니다.」)과 **맞는 안내**로 표시합니다. 링크 열기는 계속 차단됩니다.
- **내 화면/업무에 영향**: **기관 공지·자료실** — 상세 **「보기」** 에서 불안전 첨부가 **왜 열리지 않는지** 구체 문구로 확인 가능
- **상태**: 완료

<details><summary>자세히</summary>

- FE `554a319` — `HomeNewsletterLaunchPage` `resolveFacilityNoticeAttachmentUrlViolation` · detail blocked banner · SEC-D46 · **Q955**
</details>

### 📝 기관 공지 상세 첨부 차단 사유·회귀 테스트 문서화 (TWR)
- **에이전트**: TWR
- **한 일**: 위 상세 화면 개선과 BE hosts-file resolver 잔여 별칭 회귀 테스트 lock을 CHANGELOG·FAQ(**Q955**)·매뉴얼·관리/배포 가이드 baseline(`a0a6643`/`554a319`)에 반영했습니다.
- **내 화면/업무에 영향**: **기관 공지·자료실** — 상세 차단 안내 참고(FAQ Q955·매뉴얼 §4-7-3a)
- **상태**: 완료

### ✅ 기관 공지 첨부 — hosts-file resolver 잔여 별칭 서비스 계층 회귀 테스트 고정 (BE)
- **에이전트**: COD
- **한 일**: SEC-D46에서 거부하는 **hosts-file resolver 별칭 5종**(`broadcasthost`·`ip6-allnodes`·`ip6-allrouters`·`ip6-mcastprefix`·`localhost.localdomain`)을 **`FacilityNoticeService.createNotice`** end-to-end 회귀 테스트로 고정했습니다. **동작 변화 없는** QA 보강입니다.
- **내 화면/업무에 영향**: 없음 — QA·회귀 방지용 내부 테스트
- **상태**: 완료

<details><summary>자세히</summary>

- BE `a0a6643` — `FacilityNoticeServiceTest.createNoticeShouldRejectAdditionalHostsFileResolverAliases` · SEC-D46 axis-13 service-layer lock
</details>

### ✅ 기관 공지 첨부 localhost6 — 서비스 계층 회귀 테스트 고정 (BE)
- **에이전트**: COD
- **한 일**: SEC-D46 **localhost6** hosts-file 별칭 3종(`localhost6`·`localhost6.localdomain`·`localhost6.localdomain6`) 거부를 **`FacilityNoticeService.createNotice`** end-to-end 회귀 테스트로 고정했습니다. support-layer lock에 이어 **동작 변화 없는** QA 보강입니다.
- **내 화면/업무에 영향**: 없음 — QA·회귀 방지용 내부 테스트
- **상태**: 완료

<details><summary>자세히</summary>

- BE `c79865e` — `FacilityNoticeServiceTest.createNoticeShouldRejectLocalhost6HostsFileResolverAliases` · SEC-D46 axis-13 service-layer lock
</details>

### ✅ 기관 공지 첨부 localhost6 — 화면 폼 계층 회귀 테스트 고정 (FE)
- **에이전트**: COD
- **한 일**: SEC-D46 **localhost6** hosts-file 별칭 3종 거부를 **`HomeNewsletterLaunchPage`** 작성·수정 폼 통합 테스트로 고정했습니다. BE 서비스 계층 lock과 **lockstep**이며 **동작 변화 없습니다**.
- **내 화면/업무에 영향**: 없음 — QA·회귀 방지용 내부 테스트
- **상태**: 완료

<details><summary>자세히</summary>

- FE `d605e0d` — `HomeNewsletterLaunchPage.test.jsx` localhost6 3-variant · SEC-D46 axis-13 page-form lock
</details>

### 📝 localhost6 서비스·화면 폼 회귀 테스트 문서화 (TWR)
- **에이전트**: TWR
- **한 일**: 위 회귀 테스트 lock을 CHANGELOG·FAQ(Q953)·관리/배포 가이드 baseline(`c79865e`/`d605e0d`)에 반영했습니다.
- **내 화면/업무에 영향**: 없음 — 문서만
- **상태**: 완료

### ✅ 기관 공지 첨부 — localhost6 hosts-file 별칭 사전 차단 (BE·FE)
- **에이전트**: COD
- **한 일**: 기관 공지·자료실 첨부 링크에서 **`localhost6`·`localhost6.localdomain`·`localhost6.localdomain6`** 처럼 OS가 **IPv6 루프백(::1)** 으로 해석하는 **hosts-file 별칭**을 서버·화면이 **저장 전 거부**합니다. 일반 공개 도메인 링크는 그대로입니다.
- **내 화면/업무에 영향**: **기관 공지·자료실** — `http://localhost6/docs`·`http://localhost6.localdomain/…` 등은 「첨부 링크 형식이 올바르지 않습니다.」로 저장 불가
- **상태**: 완료

<details><summary>자세히</summary>

- BE `0fbc0ec` · FE `75459d7` — `FacilityNoticeSupport.isLiteralOrLoopbackAttachmentHost` · `homeNewsletter.js` lockstep · SEC-D46 axis-14
</details>

### ✅ 기관 공지 첨부 URL 입력 도움말·스크린리더 연결 (FE)
- **에이전트**: UXD
- **한 일**: **기관 공지·자료실** 첨부 URL 입력칸 아래 **도움말**을 SEC-D46 **13축** 검증 규칙(공개 도메인만·IP·localhost·내부·예약 호스트 불가·기본 포트·계정정보 불가)과 맞춰 확장했습니다. 스크린리더가 도움말을 입력칸과 **연결(`aria-describedby`)** 해 읽습니다.
- **내 화면/업무에 영향**: **기관 공지·자료실** — 첨부 URL 칸 아래 「공개 도메인만(IP·localhost·내부·예약 호스트 불가)…」 도움말 표시(저장 규칙은 기존과 동일)
- **상태**: 완료

<details><summary>자세히</summary>

- FE `881490f`/`0f8ce26` — `FACILITY_NOTICE_ATTACHMENT_URL_HELP` · `HomeNewsletterLaunchPage` Field help · UXD-208
</details>

### 📝 localhost6·UXD-208 첨부 URL 도움말 문서화 (TWR)
- **에이전트**: TWR
- **한 일**: 위 보안·접근성 보강을 CHANGELOG·FAQ(Q951·Q954)·사용자 매뉴얼·관리/배포 가이드 baseline에 반영했습니다.
- **내 화면/업무에 영향**: 없음 — 문서만
- **상태**: 완료

### 📝 기관 공지 첨부 URL 도움말 보강 (TWR)
- **에이전트**: TWR
- **한 일**: SEC-D46 **13축** 첨부 URL guard(허용 목록·IP·localhost·localhost6·숫자/16진수·리졸버 별칭·비기본 포트·깨진 URL)를 사용자 매뉴얼·FAQ에 명확히 구분·설명했습니다. 질문 예방 및 도입 투명성 강화입니다.
- **내 화면/업무에 영향**: **기관 공지·자료실** — 첨부 링크 가이드(매뉴얼 §4-7-3a·Q954)
- **상태**: 완료

<details><summary>자세히</summary>

- USER_MANUAL §4-7-3a 「기관 공지 첨부 URL 형식」 · SEC-D46 13-axis 요약 · UXD-208 반영
</details>

### ✅ 일괄 확정취소 확인번호 6자리 고정 (COD)
- **에이전트**: COD
- **한 일**: 방문일정 일괄 미확정 시 확인번호를 **정확히 6자리**로 발급·검증하는 로직을 재확인했습니다. SEC-D44 batch-unconfirm 보안 표준 정착 및 API_SPEC 동기화입니다.
- **내 화면/업무에 영향**: 없음 — 함수 검증 강화
- **상태**: 완료

<details><summary>자세히</summary>

- BE `5ebab4f` — batch-unconfirm confirmation-number 6-digit validation lock · API_SPEC /visits/batch-unconfirm 갱신 · SEC-D44 axis-11 closure · Q818 매뉴얼 연결
</details>

### ✅ 기관 공지 첨부 hosts-file resolver 별칭 6경로 회귀 테스트 고정 (BE)
- **에이전트**: COD
- **한 일**: SEC-D46에서 거부하는 **hosts-file resolver 별칭 6종**(`broadcasthost`·`localhost.localdomain`·`ip6-localnet`·`ip6-mcastprefix`·`ip6-allnodes`·`ip6-allrouters`)을 BE 회귀 테스트로 **전 경로 고정**했습니다. FE `homeNewsletter` axis-12 lockstep과 맞춘 **동작 변화 없는** 테스트 보강입니다.
- **내 화면/업무에 영향**: 없음 — QA·회귀 방지용 내부 테스트
- **상태**: 완료

<details><summary>자세히</summary>

- BE `8a1d014` — `FacilityNoticeSupportTest.shouldRejectHostsFileResolverAliases` 6-alias 전수 lock · SEC-D46 axis-13
</details>

### 📝 hosts-file resolver 별칭 회귀 테스트 문서화 (TWR)
- **에이전트**: TWR
- **한 일**: 위 회귀 테스트 보강을 CHANGELOG·FAQ(Q953)·관리/배포 가이드 baseline에 반영했습니다.
- **내 화면/업무에 영향**: 없음 — 문서만
- **상태**: 완료

### ✅ 기관 공지 첨부 — hosts-file resolver 별칭 사전 차단 (BE·FE)
- **에이전트**: COD
- **한 일**: 기관 공지·자료실 첨부 링크에서 **`/etc/hosts`·macOS resolver 별칭**(`broadcasthost`·`localhost.localdomain`·`ip6-localnet`·`ip6-mcastprefix`·`ip6-allnodes`·`ip6-allrouters`)처럼 **숫자 IP 없이도 루프백·링크로컬·멀티캐스트로 해석될 수 있는 호스트**를 서버·화면이 **저장 전 거부**합니다. 일반 공개 도메인 링크는 그대로입니다.
- **내 화면/업무에 영향**: **기관 공지·자료실** — `http://broadcasthost/share`·`http://ip6-allnodes/docs`·`http://ip6-allrouters/…` 등은 「첨부 링크 형식이 올바르지 않습니다.」로 저장 불가
- **상태**: 완료

<details><summary>자세히</summary>

- BE `f67cb32` · FE `9263417` — `FacilityNoticeSupport.looksLikeHostsFileResolverAlias` · `homeNewsletter.js` lockstep · SEC-D46 axis-12
</details>

### 📝 기관 공지 첨부 hosts-file resolver 별칭 문서화 (TWR)
- **에이전트**: TWR
- **한 일**: 위 보안 보강을 CHANGELOG·FAQ(Q953)·사용자 매뉴얼·관리/배포 가이드에 맞춰 적었습니다.
- **내 화면/업무에 영향**: 없음 — 문서만
- **상태**: 완료

### ✅ 기관 공지 첨부 — localhost 해석 별칭 사전 차단 (BE·FE)
- **에이전트**: COD
- **한 일**: 기관 공지·자료실 첨부 링크에서 **`localdomain`·`ip6-localhost`·`ip6-loopback`**(및 해당 하위 도메인)처럼 OS가 루프백으로 해석하는 **localhost 별칭 호스트**를 서버·화면이 **저장 전 거부**합니다. 일반 공개 도메인 링크는 그대로입니다.
- **내 화면/업무에 영향**: **기관 공지·자료실** — `http://service.localdomain/file`·`http://ip6-localhost/…`·`http://ip6-loopback/…` 등은 「첨부 링크 형식이 올바르지 않습니다.」로 저장 불가
- **상태**: 완료

<details><summary>자세히</summary>

- BE `b003c18` · FE `9ddd993` — `FacilityNoticeSupport`/`homeNewsletter.js` localhost resolver alias guard · SEC-D46 lockstep
</details>

### 📝 기관 공지 첨부 localhost 별칭 문서화 (TWR)
- **에이전트**: TWR
- **한 일**: 위 보안 보강을 CHANGELOG·FAQ(Q951·Q952)·사용자 매뉴얼·관리/배포 가이드에 맞춰 적었습니다.
- **내 화면/업무에 영향**: 없음 — 문서만
- **상태**: 완료

### ✅ 기관 공지 첨부 — 변형 IP·내부망 도메인 사전 차단 (BE·FE)
- **에이전트**: COD
- **한 일**: 기관 공지·자료실 첨부 링크에서 **숫자만으로 된 주소·16진수처럼 보이는 주소**, **앞자리 0이 붙은 IP·짧은 IP 표기**, **내부망용 도메인 끝(`.local`·`.internal`·`.corp`·`.home`·`.lan`·`.private`·`.intranet`)** 을 서버·화면이 **저장 전 거부**합니다. 일반 공개 도메인 링크는 그대로입니다.
- **내 화면/업무에 영향**: **기관 공지·자료실** — `http://2130706433/`·`http://0x7f000001/`·`http://0177.0.0.1/`·`http://intranet.local/…`·`https://….internal/…` 등은 「첨부 링크 형식이 올바르지 않습니다.」로 저장 불가
- **상태**: 완료

<details><summary>자세히</summary>

- BE `32e6044`/`4e38a13` · FE `957a2f6` — `FacilityNoticeSupport` obfuscated/leading-zero/abbreviated dotted IP · special-use suffix · `homeNewsletter.js` lockstep
</details>

### 📝 기관 공지 첨부 변형 IP·내부망 도메인 문서화 (TWR)
- **에이전트**: TWR
- **한 일**: 위 보안 보강을 CHANGELOG·FAQ·사용자 매뉴얼·관리/배포 가이드에 맞춰 적었습니다.
- **내 화면/업무에 영향**: 없음 — 문서만
- **상태**: 완료

### ✅ 기관 공지 첨부 링크 — IP·localhost 주소 사전 차단 (BE·FE)
- **에이전트**: COD
- **한 일**: 기관 공지·자료실 첨부 링크에 **숫자 IP(IPv4/IPv6)·`localhost`·`*.localhost`** 가 들어가면 서버·화면 모두 **저장 전 거부**합니다. 허용 호스트 목록에 IP를 적어 두어도 **항상 거부**합니다(내부망·메타데이터 주소로 악용되는 것을 막기 위함).
- **내 화면/업무에 영향**: **기관 공지·자료실** — `https://127.0.0.1/…`·`https://localhost/guide.pdf` 같은 링크는 「첨부 링크 형식이 올바르지 않습니다.」로 저장 불가. 일반 도메인 `https://…` 링크는 그대로
- **상태**: 완료

<details><summary>자세히</summary>

- BE `37e6742` · FE `589dd8d` — `FacilityNoticeSupport.isLiteralOrLoopbackAttachmentHost` · `homeNewsletter.js` lockstep · 허용 목록에 IP를 넣어도 fail-closed
</details>

### ✅ 일괄 확정취소 확인번호 오류·잔여 표 날짜 a11y (FE)
- **에이전트**: COD · UXD
- **한 일**: 방문일정 **일괄 확정취소**에서 확인번호가 틀리거나 자릿수가 맞지 않으면 **화면 상단 Alert와 칸 안내가 겹치지 않고**, **확인번호 입력칸 한곳**(`aria-invalid`·`role="alert"`)만 안내한 뒤 그 칸으로 커서를 옮깁니다. 보호자 초대·욕창·교통 월간 리포트 등 **남은 표 날짜 칸**도 스크린리더가 읽기 쉬운 표준 형식으로 감쌌습니다(화면 글자 그대로).
- **내 화면/업무에 영향**: **방문 일정 → 일괄 확정취소** — 확인번호 오류 시 안내가 칸 한곳에만 · **일부 목록·리포트** — 날짜 칸 보조기기 인식 개선(시각 화면 변화 없음)
- **상태**: 완료

<details><summary>자세히</summary>

- FE `7706d78` — `VisitBatchUnconfirmPanel` challenge Field 전담 · `GuardianInvitationList` · `PressureUlcerPage` · `TransportMonthlyReportsPage` `<time dateTime>`
</details>

### ✅ 기관 공지 첨부 링크 — 비기본 포트·깨진 URL 사전 차단 (BE·FE)
- **에이전트**: COD
- **한 일**: 기관 공지·자료실 첨부 링크가 **http/https 기본 포트(생략·`:80`/`:443`)가 아닌 포트**를 쓰면 서버·화면 모두 **저장 전 거부**합니다. 깨진 주소·사용자정보가 들어간 주소도 각각 「형식이 올바르지 않습니다」·「사용자 정보를 포함할 수 없습니다」로 안내합니다.
- **내 화면/업무에 영향**: **기관 공지·자료실** — `https://drive.example.com:8443/…`처럼 **비표준 포트** 링크는 저장 불가. 일반 `https://…` 링크는 그대로
- **상태**: 완료

<details><summary>자세히</summary>

- BE `96a55fb` · FE `ac37e47`/`72c9cc2` — `FacilityNoticeSupport` 기본 포트만 허용 · `homeNewsletter.js` `resolveFacilityNoticeAttachmentUrlViolation` lockstep
</details>

### ✅ 기관 공지 첨부 허용 호스트 정규화·health 점검 노출 (BE)
- **에이전트**: COD
- **한 일**: 허용 목록 호스트를 **끝점 점 제거·국제 도메인(ASCII) 정규화**해 형식 차이로 오탐·미탐이 나지 않게 했고, **`GET /api/v1/health`** 에 허용 목록 설정 여부·호스트 수·미설정 블로커를 넣어 운영이 배포 전에 확인할 수 있게 했습니다.
- **내 화면/업무에 영향**: 없음 — 일반 직원 화면 변화 없음. IT는 health로 허용 목록 설정 여부를 확인
- **상태**: 완료

<details><summary>자세히</summary>

- BE `f18ad05`/`67c439b` — `normalizeAttachmentHost`(trailing-dot·IDN) · health `facilityNoticeAttachmentAllowlistConfigured` · `facilityNoticeAttachmentAllowedHostCount` · `facilityNoticeAttachmentReadinessBlockers`
</details>

### ✅ 기관 공지 첨부 링크 호스트 허용 목록 (BE)
- **에이전트**: COD
- **한 일**: 기관 공지·자료실 첨부 URL에 **사용자정보(userInfo)가 들어간 피싱형 주소**를 막고, 운영에서 **`FACILITY_NOTICE_ATTACHMENT_ALLOWED_HOSTS`** 를 설정하면 **그 호스트만** 첨부로 저장되도록 했습니다. 비우면 예전처럼 http(s) 구조 검사만 적용됩니다.
- **내 화면/업무에 영향**: **기관 공지·자료실** — 허용 목록을 켠 환경에서 목록 밖 도메인·`user@evil.com` 형태 링크는 저장 거부. 목록을 안 켠 환경은 화면 변화 없음
- **상태**: 완료

<details><summary>자세히</summary>

- BE `5cb8bf0` — `FacilityNoticeSupport.attachmentUrlViolation` · `FACILITY_NOTICE_ATTACHMENT_ALLOWED_HOSTS` · `application.yml` `ogada.facility-notice.attachment-allowed-hosts`
</details>

### ✅ 방문일정 일괄 확정취소 확인번호를 6자리로 강화 (BE·FE)
- **에이전트**: COD
- **한 일**: `/visits` **일괄 확정취소** 확인번호를 **4자리→6자리**(100000~999999)로 올렸습니다. 구 4자리 입력은 서버·화면 모두 **저장 전 거부**합니다. 유효 시간(10분)·1회 사용·6항목 연쇄 경고는 그대로입니다.
- **내 화면/업무에 영향**: **방문 일정 → 일괄 확정취소** — 확인번호 **6자리** 입력(라벨·자리수 안내 변경)
- **상태**: 완료

<details><summary>자세히</summary>

- BE `48e7020` · FE `3aaccd7` — `VisitBatchUnconfirmChallengeStore.CHALLENGE_DIGITS=6` · `VisitBatchUnconfirmPanel` maxLength/pattern lockstep
</details>

### ✅ 알림톡 중첩 페이로드 민감정보 마스킹 보강 (BE)
- **에이전트**: COD
- **한 일**: 알림톡 저장 페이로드에서 발신키·급여액 마스킹이 **최상위 필드만** 처리되던 한계를 없애, **객체·배열 안쪽** 동일 필드도 `***` 로 치환합니다.
- **내 화면/업무에 영향**: 없음 — 발송 이력에 보이는 마스킹 결과는 종전과 같고, 저장 데이터 보호만 강화
- **상태**: 완료

<details><summary>자세히</summary>

- BE `b863930` — `NotificationPayloadRedactor` 재귀 마스킹 · 회귀 테스트
</details>

### ✅ 급여·간호 리포트 기간 오류를 고치면 안내가 바로 사라짐 (FE)
- **에이전트**: COD
- **한 일**: 역방향 기간으로 오류가 난 뒤 **시작·종료일을 올바른 순서로 고치면**, 조회를 다시 누르거나 새로고침하지 않아도 **종료일 칸 오류 안내가 즉시 해제**되도록 목욕도움·요양/식사/화장실·체위변경·집중배설·수급자별·서비스 집계·간호·간호급여(욕창) 리포트에 적용했습니다.
- **내 화면/업무에 영향**: **급여제공·간호 리포트** — 기간을 바로잡으면 오류 안내가 바로 사라짐(문구·레이아웃 동일)
- **상태**: 완료

<details><summary>자세히</summary>

- FE `6f1e620`·`d50f5ca`·`474dd81` — PressureUlcer · Nursing/Care nursing · BathHelp · CareMealExcretion · IntensiveExcretion · PatientService · PositionChange · ServiceSummary
</details>

### ✅ 안전 점검 기간 오류 단일 칸 안내·배차/의료비 수납 시각 a11y (FE)
- **에이전트**: COD
- **한 일**: 안전 점검 조회 기간 오류를 **종료일 칸 한곳**(`role="alert"`)으로만 안내하고(상단 중복 Alert 제거), 배차 **확정 시각**·국세청 의료비 **수납 시각**을 스크린리더가 읽기 쉬운 `<time dateTime>` 으로 감쌌습니다. 화면 글자는 그대로입니다.
- **내 화면/업무에 영향**: **안전 점검 목록** — 기간 오류 안내 위치 정리(스크린리더) · **배차·의료비공제** — 확정/수납 시각 보조기기 인식 개선(시각 화면 변화 없음)
- **상태**: 완료

<details><summary>자세히</summary>

- FE `4632b93` — `SafetyRecordDateRangeFilter` · `useSafetyServerRecords` · Transport 확정 시각 · `MedicalExpenseDeductionPanel` 수납 시각
</details>

### ✅ 안전 점검 조회를 날짜 범위로 제한하고 함량 제한 (BE, SEC-D41)
- **에이전트**: COD
- **한 일**: 안전 점검·주기 위험 평가 목록 조회 API(`GET /safeties`, `/risks`)에서 **미제한 쿼리 시 누적된 대량의 인격정보가 동시 반환**될 수 있던 갭을 막았습니다. `fromDate`/`toDate` 선택 쿼리를 추가해 기본 **30일(최대 366일) 범위만 응답**하도록 제한했습니다. 결과 행 수도 **최대 200행**으로 캡핑해 페이지네이션 누적 패턴을 사전 차단했습니다. **화면의 기본 필터·페이지 로드 속도는 변화 없음**입니다.
- **내 화면/업무에 영향**: **안전 점검·위험 평가 목록** — 무제한 쿼리 불가(기본 30일만 조회 · 더 이전 기록은 날짜 필터로 직접 선택) · 화면 체감 변화 없음
- **상태**: 완료

<details><summary>자세히</summary>

- BE `39b7c54` — `SafetyController`/`RiskController` GET list endpoint에 `fromDate`/`toDate` 선택 파라미터 추가 · 기본값 30일(오늘 기준) · 최대값 366일 · `Pageable` 200-row cap 설정 · `@DateTimeFormat(iso=DATE)` · QueryParam validation · `SafetyService`/`RiskService` 메서드 서명 확장 · 회귀 쿼리 2건·SQL 성능 분석 · SEC-D41 범위제한 동결
</details>

### ✅ 간호급여 리포트 역방향 기간 사전 차단 (FE, L03_M15)
- **에이전트**: COD
- **한 일**: 간호급여 리포트(`/care/reports/pressure-ulcer-provision`) 조회 화면에서 **시작일>종료일로 입력**하면 예전엔 **요청이 서버까지 날아가 400 오류가 뜨던 것**을 조회·생성 전 **화면 단계에서 바로 안내**하도록 했습니다. 종료일 칸을 오류 상태로 표시하고 「종료일은 시작일 이후여야 합니다」로 바로 안내해, 사용자가 서버 왕복 없이 오류를 즉시 알 수 있습니다. 지난 집계 표도 즉시 비워 표시 혼동을 방지했습니다. **기간 입력 필드·표 레이아웃은 그대로**입니다.
- **내 화면/업무에 영향**: **간호급여 리포트** — 역방향 기간 입력 시 조회 전 바로 안내(서버 응답 대기 없음) · 화면 표시 변화 없음
- **상태**: 완료

<details><summary>자세히</summary>

- FE `03c0a2f` — `PressureUlcerProvisionReportPage` 조회 버튼 클릭 시 `startDate>endDate` 검증 로직 추가 · 오류 시 endDate 필드 state·aria-invalid 설정 · BE `@PressureUlcerService` 메서드와 동일 검증 규칙 동기화 · 지난 집계 결과 state clear · 관련 test 회귀 · npm test PASS
</details>

### ✅ 알림톡 페이로드에서 민감 데이터 마스킹 (BE, SEC-D37)
- **에이전트**: COD
- **한 일**: 주간보호센터 시스템에서 **알림톡 발송 후 저장된 `notifications.payload` 에 SMS 발신키(`accessKey`)와 급여액(`payrollAmount`) 같은 민감 데이터가 그대로 남아 있던 갭**을 막았습니다. 발송 직후 데이터베이스 저장 시 이 필드들을 **`***`로 치환**해, TTL(저장 기간) 동안 민감 정보가 노출되지 않도록 했습니다. **발송 로그 조회·모니터링 화면에 나타나는 페이로드는 변화 없음**(마스킹된 데이터만 표시)입니다.
- **내 화면/업무에 영향**: **알림톡 발송 이력** — 발송 후 저장된 페이로드에서 SMS 키·급여액 마스킹(화면 표시 변화 없음) · 민감 데이터 노출 범위 최소화
- **상태**: 완료

<details><summary>자세히</summary>

- BE `db1ff72` — `NotificationService.createAndSend` 또는 저장 메서드 시점에 payload JSON 파싱 후 `accessKey`·`payrollAmount` null 처리 → `***` 문자열 치환 · `NotificationPayloadMasker` 헬퍼(또는 인라인 유틸) · 발송 직전 원본 사용·저장 직후 마스킹 분리 · 회귀 테스트 2건(마스킹 적용·비마스킹 배제) · SEC-D37 stored-sensitive-data
</details>

### ✅ 안전 점검 목록 FE 날짜 범위 동기화 (FE, SEC-D41)
- **에이전트**: COD
- **한 일**: BE `@39b7c54`에서 안전 점검 조회를 **30일 범위로 제한**한 것에 맞춰 FE도 동기화했습니다. 안전 점검 목록 GET 요청 시 **`fromDate`/`toDate` 쿼리 파라미터를 전달**하고, 사용자가 **역방향 또는 범위 초과 기간을 입력**하면 조회 전 바로 안내하도록 했습니다. 지난 목록도 즉시 비워 표시 혼동을 방지했습니다. **목록 필터·기간 입력 UI는 그대로**입니다.
- **내 화면/업무에 영향**: **안전 점검 목록** — GET 쿼리 시 fromDate/toDate 전달(기본 30일 · 더 이전은 필터로 선택) · 화면 표시 변화 없음
- **상태**: 완료

<details><summary>자세히</summary>

- FE `1841144` — `SafetyListPage` (또는 panel)의 GET `/safeties` 호출 시 `fromDate`/`toDate` 쿼리 파라미터 추가 · BE 메서드 서명과 일치 · 역방향/범위초과 검증 후 사전 차단 · 기본값 30일 표시(UI 선택 시 DatePicker 연동) · 지난 결과 state clear · test 회귀 · npm test PASS
</details>

### 📝 기관 공지 첨부 포트·health·허용 목록 보강 ops 문서화 (TWR)
- **에이전트**: TWR
- **한 일**: develop HEAD(BE `96a55fb` · FE `ac37e47`) 기준으로 **기관 공지 첨부 비기본 포트 거부·깨진/자격증명 URL 안내·허용 호스트 정규화·health 허용 목록 점검** 을 CHANGELOG·FAQ·매뉴얼·관리/배포 가이드에 반영했습니다.
- **내 화면/업무에 영향**: 없음 — 운영 문서만 갱신
- **상태**: 완료(문서만)

<details><summary>자세히</summary>

- CHANGELOG 헤더 BE `5cb8bf0`→`96a55fb` · FE `474dd81`→`ac37e47` · FAQ Q947 갱신·Q950 신설 · USER_MANUAL §4-7-3a · ADMIN/DEPLOYMENT health·env · 모듈 97.41% 유지

</details>

### 📝 일괄 확정취소 6자리·기관 공지 첨부 허용 목록·리포트 기간 UX ops 문서화 (TWR)
- **에이전트**: TWR
- **한 일**: develop HEAD(BE `5cb8bf0` · FE `474dd81`) 기준으로 **일괄 확정취소 확인번호 6자리·기관 공지 첨부 호스트 허용 목록·알림톡 중첩 마스킹·리포트 기간 오류 즉시 해제·안전/배차 a11y** 를 CHANGELOG·FAQ·매뉴얼·관리/배포 가이드에 반영했습니다.
- **내 화면/업무에 영향**: 없음 — 운영 문서만 갱신
- **상태**: 완료(문서만)

<details><summary>자세히</summary>

- CHANGELOG 헤더 BE `db1ff72`→`5cb8bf0` · FE `03c0a2f`→`474dd81` · FAQ Q818 갱신·Q947~Q949 신설 · USER_MANUAL §5-11 · ADMIN/DEPLOYMENT env·API 표 · 모듈 97.41% 유지

</details>

---

## 2026-07-19

### ✅ 건강·투약 이력 시각을 기계가 읽을 수 있는 형태로 표시 (FE, UXD-205)
- **에이전트**: COD
- **한 일**: UXD-197~204에서 리포트·표·패널·보호자 화면 날짜·시각을 `<time dateTime>`으로 정합한 뒤, **건강·투약 이력** 두 곳에 남아 있던 시각이 **그냥 글자(텍스트)** 로만 표시되어 스크린리더가 시각으로 정확히 해석하지 못하던 WCAG 1.3.1 갭을 정리했습니다. **건강 페이지 기록 이력(기록 시각)·이용자 상세 건강 탭(투약 시각·사건 발생 시각)** 을 **기계가 읽을 수 있는 표준 형식**으로 감쌌습니다. 투약 시간 표시는 `HH:mm` 로캘 포맷 유지하고, 투약/기록 시각의 기계용 값은 완전 ISO를 사용합니다. **화면에 보이는 글자는 그대로**입니다.
- **내 화면/업무에 영향**: **건강 페이지·이용자 상세 — 건강 탭** — 스크린리더 등 보조기기의 기록/투약/사건 시각 인식 정확도 개선(시각 사용자 화면 변화 없음)
- **상태**: 완료

<details><summary>자세히</summary>

- FE `25a0259` — `formatHealthHistoryTimestamp` 신설(utils/healthRecords.js) · ISO → `<time dateTime>` + 로캘 라벨 · `HealthPage` 「기록 이력」탭·`ClientDetailPage` 「건강」탭의 `recordedAt`/`administeredAt`/`occurredAt` 래핑 · 투약 예약 시간(`scheduledTime`) display 유지 · falsy → placeholder 처리 · UXD-200~204 패턴 재사용 · 신규 ds-* 0 · test 3파일 16/16 PASS · `npm run build` PASS
</details>

### 📝 건강 이력 시각 a11y·기선 갱신 (TWR)
- **에이전트**: TWR
- **한 일**: develop HEAD 재검증(BE `6d3c766` · FE `25a0259`) 후 **건강·투약 이력 시각 `<time dateTime>`**(UXD-205)을 CHANGELOG 카드로 기록하고, **FAQ Q945** 적용 범위에 건강 페이지를 추가했습니다. FAQ·USER_MANUAL·ADMIN_GUIDE·DEPLOYMENT_GUIDE 기선을 FE `95b6c52`→`25a0259` 로 맞췄습니다.
- **내 화면/업무에 영향**: 없음 — 운영 문서만 갱신
- **상태**: 완료(문서만)

<details><summary>자세히</summary>

- CHANGELOG UXD-205 카드 신설 · 헤더 기선 FE `95b6c52`→`25a0259` · 「최근 7일 요약」 2026-07-19 항목 보강 · FAQ Q945에 건강 페이지 행 추가(42곳→43곳) · FAQ·USER_MANUAL·ADMIN_GUIDE·DEPLOYMENT_GUIDE 기선·능력표·변경 이력 FE `25a0259` 동기화
- 코드 재검증(2026-07-19): FE `25a0259` 이 `HealthPage`·`ClientDetailPage` 건강 이력 시각을 `<time dateTime>`으로 래핑함을 확인 — 문서↔코드 일치. BE `6d3c766` 최신

</details>

### ✅ 욕구사정 만족도 중복 제거 (FE, QA-B627)
- **에이전트**: COD
- **한 일**: `ClientNeedsAssessmentSatisfactionPage` 컴포넌트가 React 배열 렌더링 시 고유 `key` prop을 사용하지 않아, 페이지 갱신 시 동일 만족도 항목이 중복으로 표시되거나 state 오류가 발생할 수 있던 갭을 정리했습니다. 만족도 목록의 각 항목에 고유 `key={satisfaction.id}` 를 추가해 React의 reconciliation이 정확히 동작하도록 했습니다. **화면 표시와 기능 변화 없음**입니다.
- **내 화면/업무에 영향**: **이용자 상세 — 욕구사정 만족도 목록** — 페이지 갱신 시 중복 표시 방지(시각 사용자 화면 변화 없음)
- **상태**: 완료

<details><summary>자세히</summary>

- FE `cd0595d` — `ClientNeedsAssessmentSatisfactionPage` satisfaction 배열 렌더링에 `key={satisfaction.id}` 추가 · React reconciliation 정확성 강화 · test 1파일 3/3 PASS · `npm run build` PASS
</details>

### ✅ 직원 현황 CSV의 엑셀 수식 실행 위험 차단 (BE, SEC-D33)
- **에이전트**: COD
- **한 일**: 이전 `57523b5` 에서 청구 명세·국세청 CSV의 엑셀 수식 실행 위험을 **공통 `CsvFormulaEscaper`** 로 차단했습니다. 이번에는 **직원 현황 리포트 CSV** 도 동일 위험에 노출되어 있던 것을 발견해 같은 헬퍼로 보호했습니다. **`StaffStatusReportService`** 의 `displayName` 등 사용자 영향 필드에서 이름이 `=`·`+`·`-`·`@`로 시작하면 엑셀이 수식으로 실행할 수 있던 위험(CWE-1236)을 앞에 작은따옴표를 붙여 글자로만 열리게 했습니다. **화면·다운로드 버튼 위치 변화 없음**입니다.
- **내 화면/업무에 영향**: **직원현황 리포트 CSV** — 다운로드 파일 보안 강화(화면·버튼 변화 없음). 직원 이름이 `=`로 시작하면 엑셀에서 앞에 `'`가 보일 수 있음
- **상태**: 완료

<details><summary>자세히</summary>

- BE `1ae9c50` — `CsvFormulaEscaper` 공개(public) 승격 · `common.csv` 패키지로 이동 · `StaffStatusReportService.escapeCsv` 제거 후 `CsvFormulaEscaper.escape` 위임 · 금액 필드 신호 포함 숫자(`-90000.00`) 면제 정책 재사용 · `StaffStatusReportServiceTest` 회귀 · CWE-1236 동일 축 완결
</details>

### ✅ 청구 명세·국세청 CSV의 엑셀 수식 실행 위험 차단 (BE, SEC-D33)
- **에이전트**: COD
- **한 일**: 청구 **명세서 CSV**·**국세청 의료비공제 CSV**를 엑셀·스프레드시트에서 열 때, 이용자·보호자 이름 등 글자 칸이 `=`·`+`·`-`·`@`(또는 탭)로 시작하면 **수식·DDE로 실행**될 수 있던 위험을 막았습니다. 그런 칸 앞에 **작은따옴표(`'`)** 를 붙여 **글자로만** 열리게 하고, **금액 칸의 마이너스 숫자**(`-90000.00` 등)는 그대로 **숫자로 계산**되도록 예외 처리했습니다.
- **내 화면/업무에 영향**: **청구 상세 「명세 Excel」·본인부담 통계 「국세청 CSV」** — 다운로드 파일 보안 강화(화면·다운로드 버튼 위치 변화 없음). 이름 칸이 `=`로 시작하면 엑셀에서 앞에 `'`가 보일 수 있음
- **상태**: 완료

<details><summary>자세히</summary>

- BE `57523b5` — `CsvFormulaEscaper` 신설 · `BillingStatementExportService`·`BillingService`(NTS medical-expense export) 셀 escape 통합 · 서명 숫자(`BigDecimal` 음수)는 neutralize 면제 · `CsvFormulaEscaperTest`·관련 Billing*Test 회귀 · CWE-1236
</details>

### ✅ 안전 점검·선임 업무일지·외출 실제 출발/복귀 시각을 기계가 읽을 수 있는 형태로 표시 (FE, UXD-204)
- **에이전트**: COD
- **한 일**: UXD-197~203에서 목록·청구·보호자 화면 날짜·시각을 `<time dateTime>`으로 정합한 뒤, **안전·외출·선임** 화면에 남아 있던 시각이 **그냥 글자(텍스트)** 로만 표시되어 스크린리더가 시각으로 정확히 해석하지 못하던 갭을 정리했습니다. **안전 점검 저장 시각**·**선임 요양보호사 전자서명 시각**·**외출 실제 출발/복귀 시각**(이용자 상세 외출 탭·외출 리포트 「실제」 열)을 **기계가 읽을 수 있는 표준 형식**으로 감쌌습니다. **화면에 보이는 글자는 그대로**입니다.
- **내 화면/업무에 영향**: **안전 일일/정기 점검·선임 업무일지·외출 관리·외출 리포트** — 스크린리더 등 보조기기의 저장·서명·출발/복귀 시각 인식 정확도 개선(시각 사용자 화면 변화 없음)
- **상태**: 완료

<details><summary>자세히</summary>

- FE `95b6c52` — `formatSafetySavedAt`·`signatureSignedAtLabel` string→JSX(`<time dateTime>`) · `ClientOutingPanel`·`ClientOutingReportPage` 「실제」열 Fragment+조건부 `<time>` · UXD-200/201/203 패턴 재사용 · 신규 ds-* 0 · test 6파일 29/29 PASS · `npm run build` PASS
</details>

### 📝 청구 CSV 수식 차단·안전/외출 시각 a11y·기선 갱신 (TWR)
- **에이전트**: TWR
- **한 일**: develop HEAD 재검증(BE `57523b5` · FE `95b6c52`) 후 **청구 CSV 엑셀 수식 실행 위험 차단**(SEC-D33)과 **안전·선임·외출 시각 `<time dateTime>`**(UXD-204)을 CHANGELOG 카드로 기록하고, **FAQ Q945** 적용 범위·**Q946**(CSV 수식 차단)·매뉴얼·관리자·배포 가이드 기선을 맞췄습니다.
- **내 화면/업무에 영향**: 없음 — 운영 문서만 갱신
- **상태**: 완료(문서만)

<details><summary>자세히</summary>

- CHANGELOG SEC-D33·UXD-204 카드 신설 · 헤더 기선 BE `6d3c766`→`57523b5` · FE `2715090`→`95b6c52` · 「최근 7일 요약」 2026-07-19 항목 보강 · FAQ Q945에 안전·선임·외출 행 추가(37곳→42곳) · FAQ Q946 신설 · USER_MANUAL §3-2·Q534/Q535 교차 참조 · ADMIN_GUIDE·DEPLOYMENT_GUIDE 기선·스모크 동기화
</details>

### ✅ 보호자 포털·QR 체크인 출석 시각을 기계가 읽을 수 있는 형태로 표시 (FE, UXD-203)
- **에이전트**: COD
- **한 일**: UXD-197~201에서 직원·청구·리포트 화면 날짜·시각 칸을 `<time dateTime>`으로 정합한 뒤, **보호자 Must 화면**에 남아 있던 출석 시각이 **그냥 글자(텍스트)** 로만 표시되어 스크린리더·보조기기가 시각으로 정확히 해석하지 못하던 WCAG 1.3.1 갭을 정리했습니다. **보호자 일일 요약(입소·귀가 시각)** 과 **QR 셀프 체크인 처리 완료 시각**을 **기계가 읽을 수 있는 표준 형식**으로 감쌌습니다. 기계용 값에는 완전 ISO 시각을, 화면 표시는 종전 로캘 시각 포맷을 그대로 유지합니다. **화면에 보이는 글자는 그대로**입니다.
- **내 화면/업무에 영향**: **보호자 포털(`/guardian`)·QR 체크인(`/guardian/checkin`)** — 스크린리더 등 보조기기의 입소·귀가·처리 시각 인식 정확도 개선(시각 사용자 화면 변화 없음)
- **상태**: 완료

<details><summary>자세히</summary>

- FE `2715090` — `GuardianDailySummary.formatTime` string→JSX(`<time dateTime={ISO}>` + `toLocaleTimeString` 표시) · `GuardianCheckinPage` 성공 Alert의 처리 완료 시각 `<time dateTime={resultTime}>` 래핑 · UXD-201 `formatLockedAt`/`formatPaidAt` 패턴 재사용 · 신규 ds-* 클래스 0(CSS 무변경) · test 2파일 9/9 PASS · `npm run build` PASS
</details>

### 📝 보호자 출석 시각 a11y·기선 갱신 (TWR)
- **에이전트**: TWR
- **한 일**: develop HEAD 재검증(BE `6d3c766` · FE `2715090`) 후 **보호자 포털·QR 체크인 출석 시각 `<time dateTime>`**(UXD-203)을 CHANGELOG 카드로 기록하고, **FAQ Q945**·**USER_MANUAL §3-2·§8** 적용 범위에 보호자 Must 화면을 추가했습니다. FAQ·USER_MANUAL·ADMIN_GUIDE·DEPLOYMENT_GUIDE 기선을 FE `fa838f5`→`2715090` 로 맞췄습니다.
- **내 화면/업무에 영향**: 없음 — 운영 문서만 갱신
- **상태**: 완료(문서만)

<details><summary>자세히</summary>

- CHANGELOG UXD-203 카드 신설 · 헤더 기선 FE `fa838f5`→`2715090` · 「최근 7일 요약」 2026-07-19 항목 보강 · FAQ Q945에 보호자 포털·QR 체크인 행 추가(35곳→37곳) · USER_MANUAL §3-2·§8 보호자 안내 · FAQ·USER_MANUAL·ADMIN_GUIDE·DEPLOYMENT_GUIDE 기선·능력표·변경 이력 FE `2715090` 동기화
- 코드 재검증(2026-07-19): FE `2715090` 이 `GuardianDailySummary`·`GuardianCheckinPage` 출석 시각을 `<time dateTime>`으로 래핑함을 확인 — 문서↔코드 일치. BE `6d3c766` 최신 · 미문서화 src 변경 없음
</details>

### ✅ 욕구사정 연도 비교 표 좁은 화면 가로 스크롤 보정 (FE, UXD-202)
- **에이전트**: COD
- **한 일**: 이용자 **욕구사정 연도 비교(3열)** 표가 공용 `Table` 컴포넌트를 거치지 않아, 좁은 화면·모바일에서 **페이지 전체가 옆으로 밀릴** 수 있던 마지막 한 곳을 정리했습니다. 표를 공용 **`.ds-table-wrap`**(좌우 넘침 시 표 영역만 스크롤)으로 감싸 **카드(표 영역) 안에서만** 좌우로 스크롤되도록 했습니다(WCAG 1.4.10 Reflow). **표에 보이는 글자·열·모양은 그대로**입니다.
- **내 화면/업무에 영향**: **이용자 상세 — 욕구사정 비교** — 좁은 창·모바일에서 **표만** 가로 스크롤되어 화면 전체가 밀리지 않음(넓은 화면은 변화 없음)
- **상태**: 완료

<details><summary>자세히</summary>

- FE `fa838f5` — `ClientNeedsAssessmentCompare.jsx` 의 단독 raw `ds-table`(공용 `Table` 미경유·`.ds-table-wrap` 누락)을 `.ds-table-wrap`(`overflow-x:auto`)으로 래핑 + 회귀 단언 추가(표 부모가 `.ds-table-wrap`) · 신규 ds-* 클래스 0(CSS 무변경) · 가정통신문 표 모바일 스크롤(Q878·UXD-183)과 동일 패턴 · FE-16 · §107/§126
</details>

### 📝 욕구사정 비교 표 모바일 스크롤 문서 반영·기선 갱신 (TWR)
- **에이전트**: TWR
- **한 일**: develop HEAD 재검증(BE `6d3c766` · FE `fa838f5`) 후 **욕구사정 연도 비교 표의 좁은 화면 가로 스크롤 보정**(UXD-202)을 CHANGELOG 카드로 기록하고, 이미 있던 **FAQ Q878**(표 모바일 가로 스크롤)에 욕구사정 비교 표를 함께 안내했습니다. FAQ·USER_MANUAL·ADMIN_GUIDE·DEPLOYMENT_GUIDE 기선을 FE `6a9e85e`→`fa838f5` 로 맞췄습니다.
- **내 화면/업무에 영향**: 없음 — 운영 문서만 갱신
- **상태**: 완료(문서만)

<details><summary>자세히</summary>

- CHANGELOG UXD-202 카드 신설 · 헤더 기선 FE `6a9e85e`→`fa838f5` · 「최근 7일 요약」 2026-07-19 항목 보강 · FAQ Q878 답변에 `ClientNeedsAssessmentCompare`(욕구사정 비교) 추가 · FAQ·USER_MANUAL·ADMIN_GUIDE·DEPLOYMENT_GUIDE 기선·능력표·변경 이력 FE `fa838f5` 동기화
- 코드 재검증(2026-07-19): FE `fa838f5` 가 `ClientNeedsAssessmentCompare` 표를 `.ds-table-wrap` 으로 래핑함을 확인 — 문서↔코드 일치. BE `6d3c766` 최신 · 미문서화 src 변경 없음
</details>

### 📝 ADMIN_GUIDE §1-4 baseline·sysadmin a11y 교차 참조 (TWR)
- **에이전트**: TWR
- **한 일**: develop HEAD 재검증(BE `6d3c766` · FE `6a9e85e`) 후 **ADMIN_GUIDE §1-4**가 구버전(`49349e4`/`5e816e6`)으로 남아 있던 baseline을 최신으로 맞추고, SEC-D34 엑셀 9축·UXD-197~201·리포트 기간 검증·이동서비스비·배차 회차 항목을 기능 클로저 목록 상단에 추가했습니다. **sysadmin**이 매일 보는 **로그인 이력·감사 로그·백업 설정·수가 변경 이력** 패널의 `<time dateTime>` a11y를 §4-2·§4-5·§6-3-1에 FAQ Q945와 연결했습니다.
- **내 화면/업무에 영향**: 없음 — 운영 문서만 갱신
- **상태**: 완료(문서만)

<details><summary>자세히</summary>

- ADMIN_GUIDE §1-4 baseline `49349e4`/`5e816e6` → **`6d3c766`/`6a9e85e`** · SEC-D34·UXD-194~201·Q940·Q936 기능 클로저 7건 추가 · §4-2 BackupSettingsPanel·LoginHistoryPanel·AuditLogPanel · §4-5 a11y 참고 · §6-3-1 FeeRateHistoryPanel `<time dateTime>` · 변경 이력 2026-07-19 행 추가 · PLAN_NOTES TWR 체크포인트 동기화
- 코드 재검증(2026-07-19): develop HEAD BE `6d3c766`/FE `6a9e85e` — CHANGELOG·FAQ·USER_MANUAL baseline과 일치 · 미문서화 src 변경 없음
</details>

### 📝 청구·정산·보호자·백업·이력 화면 날짜 칸 기계판독 형식 확대 반영 (TWR)
- **에이전트**: TWR
- **한 일**: develop HEAD 실측 후 CHANGELOG·FAQ·USER_MANUAL baseline을 **BE `6d3c766` · FE `6a9e85e`** 로 맞추고, UXD-197~199(리포트·목록·청구/평가/알림 표)에 이어 **로그인/감사/알림/수가 이력 패널 4곳(UXD-200)** 과 **청구 상세·수납 목록·수가/본인부담 단가·백업·보호자 청구 상세 7곳(UXD-201)** 의 날짜·시각 칸 `<time dateTime>` 래핑을 카드로 기록했습니다. 화면에 보이는 날짜·표 모양 변화가 없어 FAQ 신규 Q는 두지 않고 기존 **Q945** 적용 범위와 CHANGELOG·기선·능력표만 갱신했습니다.
- **내 화면/업무에 영향**: 없음 — 운영 문서만 갱신
- **상태**: 완료(문서만)

<details><summary>자세히</summary>

- CHANGELOG UXD-200·UXD-201 카드 신설 · 「최근 7일 요약」 2026-07-19 항목 보강 · baseline 동기화(BE `6d3c766` / FE `6a9e85e`) · FAQ·USER_MANUAL 헤더·능력표·변경 이력 FE 기선 `e8ff8dc`→`6a9e85e` + UXD-200·UXD-201 능력 항목 추가 · FAQ Q945·USER_MANUAL §3-2 적용 범위(24곳→35곳)로 확대
- 코드 재검증(2026-07-19): FE `c2fb261`(UXD-200)이 `LoginHistoryPanel`·`AuditLogPanel`·`NotificationHistoryPanel`·`FeeRateHistoryPanel`, `6a9e85e`(UXD-201)이 `BillingDetailPage`·`PaymentPage`·`FeeScheduleTable`·`CopayRateTable`·`BackupSettingsPanel`·`BillingSettingsPanel`·`GuardianBillingDetailModal` 날짜·시각 셀을 `<time dateTime>`로 래핑함을 확인 — 문서↔코드 일치. BE `6d3c766` 최신 문서화 완료
</details>

### ✅ 청구·정산·보호자·백업 화면의 날짜 칸을 기계가 읽을 수 있는 형태로 표시 (FE, UXD-201)
- **에이전트**: COD
- **한 일**: UXD-197~200에서 표·이력 화면 날짜 칸을 `<time dateTime>`으로 정합한 뒤, **청구·정산·보호자·백업** 관련 7개 화면에 남아 있던 날짜 칸 8곳이 아직 **그냥 글자(텍스트)** 로만 표시되어 스크린리더·보조기기가 날짜로 정확히 해석하지 못하던 WCAG 1.3.1 갭을 마저 정리했습니다. **청구 상세(입금일·환불일)·수납 목록(입금일)·수가 단가표·본인부담 단가표(적용 시작일)·백업 설정(시작·완료 시각)·청구 잠금 시각·보호자 청구 상세(입금일)** 를 **기계가 읽을 수 있는 표준 날짜 형식**으로 감쌌습니다. **화면에 보이는 날짜 글자와 표 모양은 그대로**입니다.
- **내 화면/업무에 영향**: **청구 상세·수납·수가/본인부담 단가·백업 설정·보호자 청구 상세** — 스크린리더 등 보조기기의 날짜 인식 정확도 개선(시각 사용자 화면 변화 없음)
- **상태**: 완료

<details><summary>자세히</summary>

- FE `6a9e85e` — 직접 셀 래핑: `BillingDetailPage`(PAID `paidAt`·REFUNDED `refundedAt`)·`PaymentPage`(수납표 `paidAt`)·`FeeScheduleTable`(`effectiveFrom`)·`CopayRateTable`(`effectiveFrom`)·`BackupSettingsPanel`(`startedAt`·`completedAt`) · JSX 반환 헬퍼 전환: `BillingSettingsPanel.formatLockedAt`·`GuardianBillingDetailModal.formatPaidAt` (string→`<time dateTime>`) · UXD-197~200 패턴과 정렬 · 신규 ds-* 클래스 0(CSS 무변경) · 7개 test 파일 40/40 PASS · `npm run build` PASS
</details>

### ✅ 로그인·감사·알림·수가 이력 화면의 날짜·시각 칸을 기계가 읽을 수 있는 형태로 표시 (FE, UXD-200)
- **에이전트**: COD
- **한 일**: UXD-197~199에서 리포트·목록·청구/평가/알림 표의 날짜 칸을 `<time dateTime>`으로 정합한 뒤, **모니터링·이력 패널** 4곳에서도 날짜·시각 값이 **그냥 글자(텍스트)** 로만 표시되어 스크린리더·보조기기가 날짜/시각으로 정확히 해석하지 못하던 WCAG 1.3.1 갭을 정리했습니다. **로그인 이력(로그인 시각)·감사 로그(발생 시각)·알림 발송 이력(발송 시각)·수가 변경 이력(적용 시작·등록일)** 을 **기계가 읽을 수 있는 표준 형식**으로 감쌌습니다. 날짜+시각 결합 칸은 기계용 값에는 완전 시각을, 화면 표시는 종전 로캘 포맷을 그대로 유지합니다. **화면에 보이는 글자는 그대로**입니다.
- **내 화면/업무에 영향**: **로그인 이력·감사 로그·알림 발송 이력·수가 변경 이력** — 스크린리더 등 보조기기의 날짜·시각 인식 정확도 개선(시각 사용자 화면 변화 없음)
- **상태**: 완료

<details><summary>자세히</summary>

- FE `c2fb261` — `LoginHistoryPanel`(`createdAt`)·`AuditLogPanel`(`createdAt`)·`NotificationHistoryPanel`(`sentAt`/`createdAt`)·`FeeRateHistoryPanel`(`effectiveFrom`·`createdAt`) 조건부 `<time dateTime>` 래핑 · 이미 정합된 `CmsCollectionPanel`·`BillingLedgerTable` 패턴과 정렬 · 신규 ds-* 클래스 0(CSS 무변경) · 기존 test 3개 `<time datetime>` 회귀 단언 추가 + `FeeRateHistoryPanel` 신규 test · npm test(flock) 4파일 12/12 PASS · build PASS
</details>

### 📝 표 날짜 칸 스크린리더 안내 FAQ 통합 (TWR)
- **에이전트**: TWR
- **한 일**: develop HEAD 재검증 후 **UXD-197(리포트 표)·UXD-198(CRUD·목록 표)·UXD-199(청구·평가·알림 표)** 에 걸친 **표 날짜 칸 `<time dateTime>` 접근성 개선**을 운영자용 **FAQ Q945**와 **USER_MANUAL §3-2** 한 줄로 통합 정리했습니다. 화면에 보이는 날짜·표 모양 변화는 없습니다.
- **내 화면/업무에 영향**: 없음 — 운영 문서만 갱신(기능은 이미 반영됨)
- **상태**: 완료(문서만)

<details><summary>자세히</summary>

- FAQ Q945 신설(24곳 화면·경로 표) · USER_MANUAL §3-2 「표 날짜 `<time dateTime>`」 행 추가 · §1-5 a11y 참조 보강 · baseline 재확인 BE `6d3c766` / FE `e8ff8dc` — 미문서화 src 변경 없음
</details>

### 📝 청구·평가·알림 목록 표 날짜 칸 기계판독 형식 확대 반영 (TWR)
- **에이전트**: TWR
- **한 일**: develop HEAD 실측 후 CHANGELOG·FAQ·USER_MANUAL baseline을 **BE `6d3c766` · FE `e8ff8dc`** 로 맞추고, UXD-197(리포트 표)·UXD-198(CRUD·목록 표)에 이어 **청구·평가·알림 목록 화면 10곳 표 날짜 칸 `<time dateTime>` 래핑**(UXD-199)을 카드로 기록했습니다. 화면에 보이는 날짜·표 모양 변화가 없어 FAQ 신규 Q는 두지 않고 CHANGELOG·기선·능력표만 갱신했습니다.
- **내 화면/업무에 영향**: 없음 — 운영 문서만 갱신
- **상태**: 완료(문서만)

<details><summary>자세히</summary>

- CHANGELOG UXD-199 카드 신설 · 「최근 7일 요약」 2026-07-19 항목 보강 · baseline 동기화(BE `6d3c766` / FE `e8ff8dc`) · FAQ·USER_MANUAL 헤더·능력표·변경 이력 FE 기선 `c3f0e05`→`e8ff8dc` + UXD-199 능력 항목 추가
- 코드 재검증(2026-07-19): FE `e8ff8dc` 가 `BillingLedgerTable`(입금·환불·수납일)·`NeedsAssessmentStatusPage`·`PeriodicRiskAssessmentStatusPage`·`CarePlanNotificationPage`·`OverduePage`·`HealthDetailPage`·`GuardianDetailPage`·`ProvisionResultEvaluationPage`·`FunctionalRecoveryPage`·`VisitRfidDiffComparePanel` 표 날짜 셀을 `<time dateTime>`로 래핑함을 확인 — 문서↔코드 일치. BE `6d3c766` 최신 문서화 완료
</details>

### ✅ 청구·평가·알림 목록 화면 표의 날짜 칸을 기계가 읽을 수 있는 형태로 표시 (FE, UXD-199)
- **에이전트**: COD
- **한 일**: UXD-197(리포트 표)·UXD-198(CRUD·목록 표)에서 날짜 칸을 `<time dateTime>`으로 정합한 뒤, **청구 대장·평가/알림 이력·상세 화면** 10곳에서도 날짜 칸이 **그냥 글자(텍스트)** 로만 남아 스크린리더·보조기기가 날짜로 정확히 해석하지 못하던 WCAG 1.3.1 갭을 마저 정리했습니다. **청구 대장(입금·환불·수납일)·욕구사정 현황·주기 위험 평가 현황·돌봄계획 알림 이력·연체·건강 상세·보호자 상세·급여제공 결과 평가·기능회복 훈련·방문 RFID 비교** 표의 일자 칸을 **기계가 읽을 수 있는 표준 날짜 형식**으로 감쌌습니다. **화면에 보이는 날짜 글자와 표 모양은 그대로**입니다.
- **내 화면/업무에 영향**: **청구 대장·욕구사정·주기 위험 평가·돌봄계획 알림·연체·건강/보호자 상세·급여제공 결과 평가·기능회복 훈련·방문 RFID 비교** — 스크린리더 등 보조기기의 날짜 인식 정확도 개선(시각 사용자 화면 변화 없음)
- **상태**: 완료

<details><summary>자세히</summary>

- FE `e8ff8dc` — 청구 대장 공통 표(`BillingLedgerTable`)에 `renderDateCell` 헬퍼로 입금·환불·수납일 셀을 `<time dateTime>`로 래핑 · `NeedsAssessmentStatusPage`·`PeriodicRiskAssessmentStatusPage`·`CarePlanNotificationPage`는 `formatDate` 헬퍼 경유 · `OverduePage`(최근 독촉일)·`HealthDetailPage`·`GuardianDetailPage`·`ProvisionResultEvaluationPage`·`FunctionalRecoveryPage`·`VisitRfidDiffComparePanel` 일자 셀 직접 래핑 · UXD-197·UXD-198 패턴과 정렬 · 신규 ds-* 클래스 0(CSS 무변경) · 7개 test 파일 `<time>` 회귀 단언 추가
</details>

### 📝 엑셀 금액 전각 숫자·전각 콤마 정규화 FAQ·매뉴얼 반영 (TWR)
- **에이전트**: TWR
- **한 일**: 이미 develop에 반영돼 있으나 사용자용 문서에는 빠져 있던 **공단·은행 엑셀 금액의 전각 숫자(０-９)·전각 콤마(，) 정규화**(SEC-D34)를 FAQ **Q939·Q941** 표와 USER_MANUAL §4-6·§5-6 안내에 보강했습니다. 전각 IME 입력·전각 통화 서식으로 `１，２５０，０００`처럼 들어온 금액도 전각 숫자를 반각으로 바꾸고 전각 콤마를 떼어 정확히 읽는다는 점을 명시했습니다.
- **내 화면/업무에 영향**: 없음 — 운영 문서만 갱신(기능은 이미 반영됨)
- **상태**: 완료(문서만)

<details><summary>자세히</summary>

- FAQ Q939·Q941 표에 「전각 숫자(０-９)·전각 콤마(，)」 행 추가 · 두 Q 헤더 BE 커밋 참조에 `c88687a`(전각 콤마)·`c7b6608`(전각 숫자) 추가 · Q941 답변 인트로에 전각 숫자·전각 콤마 예시(`１，２５０，０００`) 보강 · USER_MANUAL §4-6(은행 입금)·§5-6(공단 대사) 표시서식 문구 + FE/BE 능력표에 「전각 숫자·전각 콤마 정규화」 항목 추가
- 코드 재검증(2026-07-19): `ExcelAmountNormalizer` 가 `FULLWIDTH_COMMA`(U+FF0C) strip + `mapFullwidthDigitsToAscii()`(U+FF10–U+FF19) 를 수행함을 확인 — 문서↔코드 일치. develop HEAD 실측 BE `6d3c766` / FE `c3f0e05` 로 최신, 미문서화 src 변경 없음
</details>

### 📝 목록·기록 표 날짜 칸 기계판독 형식 확대 반영 (TWR)
- **에이전트**: TWR
- **한 일**: develop HEAD 실측 후 CHANGELOG·FAQ·USER_MANUAL baseline을 **BE `6d3c766` · FE `c3f0e05`** 로 맞추고, UXD-197(리포트 표)에 이어 **CRUD·목록 화면 9곳 표 날짜 칸 `<time dateTime>` 래핑**(UXD-198)을 카드로 기록했습니다. 화면에 보이는 날짜·표 모양 변화가 없어 FAQ 신규 Q는 두지 않고 CHANGELOG·기선·능력표만 갱신했습니다.
- **내 화면/업무에 영향**: 없음 — 운영 문서만 갱신
- **상태**: 완료(문서만)

<details><summary>자세히</summary>

- CHANGELOG UXD-198 카드 신설 · 「최근 7일 요약」 2026-07-19 항목 보강 · baseline 동기화(BE `6d3c766` / FE `c3f0e05`) · FAQ·USER_MANUAL 헤더·능력표·변경 이력 FE 기선 `aab11b2`→`c3f0e05` + UXD-198 능력 항목 추가
- 코드 재검증(2026-07-19): FE `c3f0e05` 가 `CaseManagementPage`·`NursingWeightRecordPage`·`NursingOralCareCheckPage`·`NursingEmergencyRecordPage`·`NursingVitalCheckPage`·`PressureUlcerPage`·`LeadCaregiverWorkLogPage`·`ClientOutingReportPage`·`ClientOutingPanel` 목록 표 날짜 셀을 `<time dateTime>`로 래핑함을 확인 — 문서↔코드 일치. BE `6d3c766` 최신 문서화 완료
</details>

### ✅ 목록·기록 화면 표의 날짜 칸을 기계가 읽을 수 있는 형태로 표시 (FE, UXD-198)
- **에이전트**: COD
- **한 일**: UXD-197에서 급여제공 **리포트** 표의 날짜 칸을 `<time dateTime>`으로 정합한 뒤, **리포트가 아닌 CRUD·목록 화면** 9곳에서도 날짜 칸이 **그냥 글자(텍스트)** 로만 남아 스크린리더·보조기기가 날짜로 정확히 해석하지 못하던 WCAG 1.3.1 갭을 정리했습니다. **사례관리 회의·바이탈·체중·구강·응급·욕창 간호 기록·선임 업무일지·외출 목록·외출 리포트** 표의 회의일·점검일·측정일·발생일·기록일·외출일 등을 **기계가 읽을 수 있는 표준 날짜 형식**으로 감쌌습니다. **화면에 보이는 날짜 글자와 표 모양은 그대로**이며, 바이탈 점검의 **시간 범위**·날짜+시각 결합 셀 중 **범위로 표현할 수 없는 부분**은 종전처럼 텍스트로 둡니다.
- **내 화면/업무에 영향**: **사례관리·간호(바이탈·체중·구강·응급)·욕창·선임 업무일지·외출 관리·외출 리포트** — 스크린리더 등 보조기기의 날짜 인식 정확도 개선(시각 사용자 화면 변화 없음)
- **상태**: 완료

<details><summary>자세히</summary>

- FE `c3f0e05` — 9개 표 렌더: `CaseManagementPage`(meetingDate)·`NursingWeightRecordPage`(measureDate)·`NursingOralCareCheckPage`(checkDate)·`NursingEmergencyRecordPage`(occurrenceDate)·`NursingVitalCheckPage`(checkDate, 날짜 부분만)·`PressureUlcerPage`(careDate)·`LeadCaregiverWorkLogPage`(logDate)·`ClientOutingReportPage`·`ClientOutingPanel`(outingDate) · UXD-197 L02 리포트·기존 `<time>` 사용 화면과 패턴 정렬 · 신규 ds-* 클래스 0(CSS 무변경) · 9개 test 파일 `<time>` 회귀 단언 추가
</details>

### 📝 리포트 표 날짜 칸 기계판독 형식 반영·기선 갱신 (TWR)
- **에이전트**: TWR
- **한 일**: develop HEAD 실측 후 CHANGELOG·FAQ·USER_MANUAL baseline을 **BE `6d3c766` · FE `aab11b2`** 로 맞추고, 급여제공 리포트 표의 날짜 칸을 **기계가 읽을 수 있는 표준 형식**으로 감싼 접근성 개선(UXD-197)을 카드로 기록했습니다. 화면에 보이는 날짜·표 모양 변화가 없어 FAQ 신규 Q는 두지 않고 CHANGELOG·기선만 갱신했습니다.
- **내 화면/업무에 영향**: 없음 — 운영 문서만 갱신
- **상태**: 완료(문서만)

<details><summary>자세히</summary>

- CHANGELOG UXD-197 카드 신설 · 「최근 7일 요약」 2026-07-19 항목 보강(FE 2791/2791 PASS·FE 기선 `aab11b2`) · baseline 동기화(BE `6d3c766` / FE `aab11b2`) · FAQ·USER_MANUAL 헤더 및 **FE-측 SYNCED 능력표·변경 이력** 기선 SHA `0ff9c7d`→`aab11b2` 갱신 + UXD-197 능력 항목 추가
- QA 실측(2026-07-19): FE develop `aab11b2` = tester TSR 검증 **2791/2791 PASS**(UXD-197 착지 후 full npm test) — 문서 FE 기선(헤더·능력표·변경 이력)을 `aab11b2` 로 일치시킴
- 코드 재검증(2026-07-19): FE `aab11b2` 가 `BathHelpReportPage`·`CareMealExcretionReportPage`·`IntensiveExcretionReportPage`·`PatientServiceReportPage`·`PositionChangeReportPage` 인라인 표의 날짜 셀을 `<time dateTime>`로 래핑함을 확인 — 문서↔코드 일치. 미문서화 src 변경 없음(BE `6d3c766` 최신 문서화 완료)
</details>

### ✅ 리포트 표의 날짜 칸을 기계가 읽을 수 있는 형태로 표시 (FE, UXD-197)
- **에이전트**: COD
- **한 일**: 표를 화면에 바로 그리는 급여제공 리포트(목욕도움·요양/식사/화장실·집중배설·수급자별 급여제공·체위변경)의 날짜 칸이 예전에는 **그냥 글자(텍스트)** 로만 표시되어, 스크린리더·검색·자동화 도구 같은 보조기기·프로그램이 그 값을 **날짜로 정확히 해석하지 못했습니다**. 이미 표준 형식을 쓰던 프로그램 리포트·간호급여 리포트와 달랐던 부분입니다. 이제 이 리포트들의 날짜 칸(방문일·기록일·관찰일·평가일·요양일·체위변경일)을 **기계가 읽을 수 있는 표준 날짜 형식**으로 감싸 형식을 통일했습니다. **화면에 보이는 날짜 글자와 표 모양은 그대로**이며, 하나의 날짜로 나타낼 수 없는 「주(週) 범위」 칸은 종전처럼 텍스트로 둡니다(WCAG 1.3.1).
- **내 화면/업무에 영향**: **목욕도움·요양/식사/화장실·집중배설·수급자별 급여제공·체위변경 리포트** — 스크린리더 등 보조기기의 날짜 인식 정확도 개선(시각 사용자 화면 변화 없음)
- **상태**: 완료

<details><summary>자세히</summary>

- FE `aab11b2` — 인라인 표 렌더 5개 리포트 페이지(`BathHelpReportPage`·`CareMealExcretionReportPage`·`IntensiveExcretionReportPage`·`PatientServiceReportPage`·`PositionChangeReportPage`)의 `scheduledDate`·`recordDate`·`observationDate`·`assessedOn`·`careDate`·`restraintDate` 셀을 `<time dateTime>`로 래핑 · 공유 `ProgramReportPanel`·`NursingServiceReportPanel`이 이미 쓰던 패턴과 정렬 · 주(週) 범위 셀은 단일 datetime로 표현 불가하여 plain text 유지 · 신규 ds-* 클래스 0(CSS 무변경) · 5개 파일 테스트 +33 assertion 추가 PASS
</details>

### 📝 엑셀 금액 특수 공백 인식·리포트 오류 접근성 확대 반영 (TWR)
- **에이전트**: TWR
- **한 일**: develop HEAD 실측 후 CHANGELOG·FAQ·USER_MANUAL baseline을 **BE `6d3c766` · FE `0ff9c7d`** 로 맞추고, **공단·은행 엑셀 금액의 「줄바꿈 없는 공백(U+00A0)·전각 공백(U+3000)」 천 단위 정규화**(SEC-D34 9번째 축)를 **Q939·Q941** 보강으로, **리포트 역방향 기간 오류를 시작일 칸까지 스크린리더에 안내**(UXD-196)하는 접근성 확대를 **Q942·Q943·Q944** 참고 보강으로 정리했습니다.
- **내 화면/업무에 영향**: 없음 — 운영 문서만 갱신
- **상태**: 완료(문서만)

<details><summary>자세히</summary>

- FAQ Q939·Q941 「줄바꿈 없는 공백(U+00A0)·전각 공백(U+3000)」 행 추가 · Q942·Q943·Q944 「시작일 칸도 aria-invalid」 참고 보강 · USER_MANUAL §4-6·§5-6 특수 공백 문구 추가 · baseline 동기화(BE `6d3c766` / FE `0ff9c7d`)
- 코드 재검증(2026-07-19): `ExcelAmountNormalizer.normalizeNumeric()` 가 `NO_BREAK_SPACE`(U+00A0)·`IDEOGRAPHIC_SPACE`(U+3000) 를 `\s+` strip 앞에서 명시적으로 제거함을 확인 — 문서↔코드 일치. develop HEAD 실측 BE `6d3c766` / FE `0ff9c7d` 로 최신, 미문서화 src 변경 없음
</details>

### ✅ 공단·은행 엑셀 금액의 특수 공백(줄바꿈 없는 공백·전각 공백) 정상 인식 (BE, SEC-D34)
- **에이전트**: COD
- **한 일**: 공단 명세(NHIS) 대사 엑셀과 은행 입금 엑셀에서 금액을 `1 250 000원`처럼 **눈으로는 띄어쓰기로 보이지만 실제로는 보통 공백이 아닌** 「줄바꿈 없는 공백(U+00A0, 웹·CMS 복사·붙여넣기)」·「전각 공백(U+3000, 전각 IME 입력)」으로 천 단위를 나누면, 예전에는 이 특수 공백을 떼지 못해 숫자로 못 읽고 **값이 조용히 비워져(null)** 대사 상태가 「불일치·보류」로 잘못 잡히거나 입금 행이 **자동 매칭·수납에서 빠질** 수 있었습니다. 이제 콤마·「원」·원화 기호(₩/￦)·전각 숫자·일반 공백과 함께 **이 두 특수 공백도 떼어** 정확한 금액으로 읽습니다(보통 공백·숫자만 있는 파일 동작은 그대로).
- **내 화면/업무에 영향**: **`/billing/imports/nhis` 대사**·**`/billing/payments` 은행 입금 엑셀** — 특수 공백으로 천 단위를 나눈 금액에서도 대사 판정·입금 매칭이 정확해짐
- **상태**: 완료

<details><summary>자세히</summary>

- BE develop `fix(v3/SEC-D34): normalize no-break and ideographic space grouped excel amounts instead of dropping row` `@6d3c766` · 공유 `ExcelAmountNormalizer` 에 `NO_BREAK_SPACE`(U+00A0)·`IDEOGRAPHIC_SPACE`(U+3000) 상수 추가 후 `.replaceAll("\\s+","")` 앞에서 명시적 strip(Java `\s`가 두 문자를 매칭하지 않음) · NHIS·은행 두 파서 단일 소스 위임 · `ExcelAmountNormalizerTest` +1·`BankDepositExcelParserTest` +1 회귀 lock · ASCII 숫자 입력 byte-neutral
</details>

### ✅ 리포트 역방향 기간 오류 안내 스크린리더 접근성 확대 (FE, UXD-196)
- **에이전트**: COD
- **한 일**: 앞서 개선한 리포트 역방향 기간 사전 차단에서, 오류 상태(「오류 있음」·`aria-invalid`)가 **종료일 칸에만** 연결되어 있어, 사실상 **시작일 칸도 잘못된 상태**인데 스크린리더에는 시작일이 정상으로 노출되던 접근성 갭이 있었습니다. 이제 **9개 급여제공·간호급여·프로그램 리포트**에서 시작일 칸도 「오류 있음」 상태로 표시하고 종료일의 오류 안내를 참조하도록 연결했습니다. **화면에 보이는 표시·안내 문구는 그대로**이며(안내 메시지는 종료일 한 곳만 두어 중복 낭독 방지), 키보드·스크린리더 사용자가 두 날짜 칸 어디서든 오류를 인지합니다(WCAG 3.3.1·4.1.2).
- **내 화면/업무에 영향**: **목욕도움·요양/식사/화장실·체위변경·집중배설·통합 간호제공·수급자별 급여제공·급여제공 서비스 집계·간호급여·프로그램 리포트** — 스크린리더 사용자의 오류 인지 개선(시각 사용자 화면 변화 없음)
- **상태**: 완료

<details><summary>자세히</summary>

- FE `5789173` — 9개 리포트 페이지(`BathHelpReportPage`·`CareMealExcretionReportPage`·`CareNursingServiceReportPage`·`IntensiveExcretionReportPage`·`NursingServiceReportsPage`·`PatientServiceReportPage`·`PositionChangeReportPage`·`ProgramReportsPage`·`ServiceSummaryReportPage`)에서 시작일 `DateInput`도 `aria-invalid` 전달·`aria-describedby`로 종료일 오류 id 참조(안내 `role="alert"`는 종료일 단일 메시지 유지) · §119 `TransportServiceFeePanel` 이중 필드 라우팅 패턴 적용 · ds-* 클래스 0(CSS 무변경) · 9파일 38/38 PASS
- FE `0ff9c7d` — `ProgramReportsPage` 오류 리셋 회귀 테스트 추가
</details>

### 📝 리포트 역방향 기간 사전 차단 확대 FAQ·매뉴얼 반영 (TWR)
- **에이전트**: TWR
- **한 일**: develop HEAD 실측 후 CHANGELOG·FAQ·USER_MANUAL baseline을 **BE `e60e288` · FE `60716c6`** 로 맞추고, **조회 기간 역방향(시작일>종료일) 사전 차단이 나머지 급여제공 리포트·간호급여 리포트·프로그램 리포트까지 확대**된 내용을 **Q944** 신설로 정리했습니다. 앞서 개별 리포트(Q942·Q943)로 다루던 것을 이번 확대분과 함께 하나로 안내합니다.
- **내 화면/업무에 영향**: 없음 — 운영 문서만 갱신
- **상태**: 완료(문서만)

<details><summary>자세히</summary>

- FAQ Q944 신설 · USER_MANUAL 프로그램 리포트·목욕도움 리포트 등 「기간 입력 주의」 보강 · baseline 동기화(BE `e60e288` / FE `60716c6`)
</details>

### ✅ 리포트 조회 기간 거꾸로 입력 시 즉시 차단 확대 (FE, form polish)
- **에이전트**: COD
- **한 일**: 조회 기간(시작일·종료일)을 받는 여러 **기록·리포트 화면**에서, **시작일이 종료일보다 뒤**인 역방향 기간으로 조회하면 예전에는 **서버까지 요청을 보낸 뒤** 400 오류가 떴습니다. 이제 이미 개선된 수급자별 급여제공 리포트·급여제공 서비스 집계 리포트에 더해, **나머지 급여제공 리포트(목욕도움·요양/식사/화장실·체위변경·집중배설·요양 간호)**, **간호급여 리포트**, **프로그램 리포트(5-7~5-10)** 까지 **조회 전에 화면에서 바로** 「종료일은 시작일 이후여야 합니다.」로 종료일 칸에 안내하고, 오류와 어긋나는 **지난 집계 표도 함께 비웁니다**. 한쪽 날짜만 비우면 서버가 기본 기간으로 대체하므로 종전대로 조회됩니다.
- **내 화면/업무에 영향**: **목욕도움·요양/식사/화장실·체위변경·집중배설·요양 간호·간호급여·프로그램 리포트** — 역방향 기간을 **즉시** 안내, 불필요한 서버 오류 대기 없음
- **상태**: 완료

<details><summary>자세히</summary>

- FE `ca31864` — 나머지 L02 리포트(`BathHelpReportPage`·`CareMealExcretionReportPage`·`PositionChangeReportPage`·`IntensiveExcretionReportPage`·`CareNursingServiceReportPage`)에 공유 `resolveCareReportDateRangeError` 가드 확대·역방향 회귀 테스트 각 추가
- FE `d4d9887` — `NursingServiceReportsPage`(간호급여 L03_M07/M09/M10) 동일 가드 연결·중복 empty 객체 `EMPTY_NURSING_SERVICE_REPORT` 상수화
- FE `60716c6` — `ProgramReportsPage`(5-7~5-10) 신규 `config/programReports.js`(`resolveProgramReportDateRangeError` 등, care-report·이동서비스비 도메인 config 패턴 미러)·역방향 회귀 테스트
- 공통: 종료일 필드 `role="alert"`·`aria-invalid`(WCAG 3.3.1) · BE `resolveDateWindow` 문구 verbatim lockstep · FE develop `60716c6`
</details>

### 📝 BE 엑셀 금액 정규화 로직 DRY 통합 및 안정성 검증 (TWR)
- **에이전트**: TWR
- **한 일**: develop HEAD 실측 후 **BE SEC-D34 엑셀 금액 정규화 리팩터** 정보를 CHANGELOG에 기록했습니다. **공단 NHIS·은행 입금 두 파서의 byte-identical 중복 로직을 신규 `ExcelAmountNormalizer` 로 단일화** — 통화기호(₩/￦), 콤마, 「원」, 공백, 전각 숫자 8축 정규화를 한 곳에서 관리해 향후 축 추가 시 오류·drift 위험을 제거했습니다. **42/42 회귀 테스트 PASS**(기존 동작 byte-identical 보증) · 코드 중복 제거(rules §2·§13·§16 준수). **baseline 동기화**(BE `e60e288` / FE `cf360d7`).
- **내 화면/업무에 영향**: 없음 — 내부 리팩터, 사용자 화면 변화 없음 · **미사용 기능: BE merge pending 7개, PLN 스코프 재조정 대기**
- **상태**: 완료(문서만), 코드 merge 대기

<details><summary>자세히</summary>

- BE develop `refactor(v3/SEC-D34): extract shared excel amount normalizer` `@e60e288` · `NhisExcelParser`·`BankDepositExcelParser` 공유 로직 → `ExcelAmountNormalizer`(billing/domain) · `normalizeNumeric()`·`mapFullwidthDigitsToAscii()` 패키지-프라이빗 · 통화기호 2종(₩/￦)·콤마·「원」·공백·전각 숫자 8축 단일 소스 · NHIS 급여일수「일」 마커 strip 후 위임 · BankDeposit `setScale(2)` 추가 · `NhisExcelParserTest` 16/16·`BankDepositExcelParserTest` 17/17·`ExcelAmountNormalizerTest` 9/9 **42/42 PASS** · WT CLEAN · Open 0 · lint 0
</details>

### ✅ BE 엑셀 금액 정규화 로직 단일화 (BE, SEC-D34)
- **에이전트**: COD
- **한 일**: 공단 NHIS 대사 엑셀과 은행 입금 엑셀에서 금액을 정규화하는 로직이 **byte-identical로 중복** 되어 있었습니다(원화기호·콤마·「원」·공백·전각 숫자). SEC-D34 포맷 내성 축이 **8개까지 늘며** 매 축 추가 시 **두 파일을 동일하게 수정**해야 했고, 오류·코드 drift 위험이 있었습니다. 이제 신규 package-private `ExcelAmountNormalizer`(billing/domain) 로 통합 — **단일 소스 1곳에서만 관리**, 향후 축 추가·수정 시 중복 제거, 유지보수성 향상(rules §2·§13·§16 준수).
- **내 화면/업무에 영향**: 없음 — 내부 구조 정리, 사용자 화면·동작 변화 없음
- **상태**: 완료

<details><summary>자세히</summary>

- `ExcelAmountNormalizer` 신규 패키지-프라이빗 클래스 · `normalizeNumeric(String)` — null/blank→null, 전각→ASCII, 통화기호(₩/￦)/콤마/「원」/공백 strip · `mapFullwidthDigitsToAscii(String)` · `NhisExcelParser` — 급여일수 「일」 마커 strip 후 위임 · `BankDepositExcelParser` — `setScale(2, HALF_UP)` 추가 · 회귀 테스트 전량 그대로 PASS — behavior-neutral 보증(`NhisExcelParserTest` 16/16 + `BankDepositExcelParserTest` 17/17 + `ExcelAmountNormalizerTest` 9/9)
</details>

### 📝 배차 a11y·오류 심화 테스트 완료·기선 갱신 (TWR)
- **에이전트**: TWR
- **한 일**: develop HEAD 실측 후 **배차 회차 6-commit a11y 개선**(UXD-194) 및 **FE 오류 심화 2761/2761 PASS** 테스트 완료를 기록했습니다. **FE develop baseline을 `cf360d7` 으로 착지** — 안정적으로 모든 테스트 통과 상태입니다.
- **내 화면/업무에 영향**: 없음 — 테스트 완료·문서 갱신, 사용자 화면 변화 없음
- **상태**: 완료

<details><summary>자세히</summary>

- FE `cf360d7` 안정 기선 착지(merge `ab9ef17→cf360d7`) · baseline 동기화(BE `c7b6608` / FE `cf360d7`) · 테스트 2761/2761 PASS
</details>

### ✅ FE 배차 a11y·오류 심화 테스트 완료 (FE)
- **에이전트**: TSR(tester)
- **한 일**: **배차 회차 6-commit a11y 개선**(`departureRound` role=alert 중복 제거·UXD-194 §118 재점검) 및 **배차 오류 심화**(숫자·지수/16진수·범위 사전 검증 등)의 **회귀 테스트 완료**. FE develop가 안정적으로 **2761/2761 PASS** 상태입니다.
- **내 화면/업무에 영향**: 없음 — 내부 테스트 완료, 사용자 화면 변화 없음
- **상태**: 완료

<details><summary>자세히</summary>

- FE develop @cf360d7 · 2761/2761 PASS · id=2 배차(픽업/이동서비스비) 회차 검증·ARIA a11y·wheel-blur 재검증 완료 · MERGED

</details>

---

## 2026-07-18

### 📝 전각 원화 기호(￦)·수급자별 리포트 기간 검증 FAQ·매뉴얼 반영 (TWR)
- **에이전트**: TWR
- **한 일**: develop HEAD 실측 후 CHANGELOG·FAQ·USER_MANUAL baseline을 **BE `ce656d5` · FE `c3a0cac`** 로 맞추고, **공단·은행 엑셀 전각 원화 기호(￦) 금액 정규화**를 **Q939·Q941** 보강으로, **수급자별 급여제공 리포트(L02_M11) 역방향 기간 사전 차단**을 **Q943** 신설로 정리했습니다.
- **내 화면/업무에 영향**: 없음 — 운영 문서만 갱신
- **상태**: 완료

<details><summary>자세히</summary>

- FAQ Q939·Q941 전각 `￦` 행 추가 · Q943 신설 · USER_MANUAL §4-6·§5-6·§5-33 보강 · baseline 동기화(BE `ce656d5` / FE `c3a0cac`)
</details>

### ✅ 공단·은행 엑셀 전각 원화 기호(￦) 붙은 금액 정상 인식 (BE, SEC-D34)
- **에이전트**: COD
- **한 일**: 공단 명세(NHIS) 대사 엑셀과 은행 입금 엑셀에서 금액 칸이 **반각 원화 기호 `₩`(U+20A9)** 뿐 아니라, 일부 한글 엑셀 통화 서식·수기 입력에서 쓰이는 **전각 `￦`(U+FFE6)**(`￦765,000`·`￦1,250,000`)로 표시되면, 예전에는 이 전각 기호 때문에 숫자로 못 읽어 **값이 조용히 비워지고(null)** 대사 상태가 「불일치·보류」로 잘못 잡히거나 입금 행이 **자동 매칭·수납에서 빠질** 수 있었습니다. 이제 반각 `₩`·콤마·「원」·공백과 함께 **전각 `￦`도 떼어** 정확한 금액으로 읽습니다(기존 `₩`·「원」만 붙은 파일 동작은 그대로).
- **내 화면/업무에 영향**: **`/billing/imports/nhis` 대사**·**`/billing/payments` 은행 입금 엑셀** — 전각 `￦`가 붙은 엑셀에서도 대사 판정·금액 매칭이 정확해짐
- **상태**: 완료

<details><summary>자세히</summary>

- BE: `NhisExcelParser.normalizeNumeric`·`BankDepositExcelParser.parseAmount` — `FULLWIDTH_WON_SIGN`(U+FFE6) 제거 추가(반각 `₩` U+20A9 lockstep). 회귀 `@Test` 각 +1 (`ce656d5`)
</details>

### ✅ 수급자별 급여제공 리포트 기간 거꾸로 입력 시 즉시 차단 (FE, L02_M11)
- **에이전트**: COD
- **한 일**: **수급자별 급여제공 리포트**(`/care/reports/patient-service`)에서 **시작일이 종료일보다 뒤**인 역방향 기간으로 조회하면, 예전에는 **서버까지 요청을 보낸 뒤** 400 오류가 떴습니다. 이제 **조회 전에 화면에서 바로** 「종료일은 시작일 이후여야 합니다.」로 종료일 칸에 안내하고, 오류와 어긋나는 **지난 집계 표도 함께 비웁니다**(이용자 미선택 시 종전대로 안내, 한쪽 날짜만 비면 서버가 기본 기간으로 채웁니다).
- **내 화면/업무에 영향**: **`/care/reports/patient-service`** — 역방향 기간을 **즉시** 안내, 불필요한 서버 오류 대기 없음
- **상태**: 완료

<details><summary>자세히</summary>

- FE: `PatientServiceReportPage.jsx` — `resolveCareReportDateRangeError`(공유 `config/careReports.js`)로 역방향 사전 차단·BE `CareReportService.resolveDateWindow` 문구 lockstep·종료일 필드 `role="alert" aria-invalid`. 회귀 테스트 추가 (`c3a0cac`)
</details>

### 📝 원화 기호(₩) 금액·리포트 기간 검증 FAQ·매뉴얼 반영 (TWR)
- **에이전트**: TWR
- **한 일**: develop HEAD 실측 후 CHANGELOG·FAQ·USER_MANUAL baseline을 **BE `1d067d9` · FE `cf360d7`** 로 맞추고, **공단·은행 엑셀의 원화 기호(₩) 붙은 금액 정상 인식**을 **Q939·Q941** 보강으로, **급여제공 서비스 집계 리포트의 역방향 기간 사전 차단**을 **Q942** 신설로 정리했습니다.
- **내 화면/업무에 영향**: 없음 — 운영 문서만 갱신
- **상태**: 완료

<details><summary>자세히</summary>

- FAQ Q939·Q941 ₩ 행 추가·Q942 신설 · USER_MANUAL §4-6·§5-6 보강 · baseline 동기화(BE `1d067d9` / FE `cf360d7`)
</details>

### ✅ 공단·은행 엑셀의 원화 기호(₩) 붙은 금액 정상 인식 (BE, SEC-D34)
- **에이전트**: COD
- **한 일**: 공단 명세(NHIS) 대사 엑셀과 은행 입금 엑셀에서 금액 칸을 **통화 서식**으로 저장하면, 엑셀이 「원」 대신 **원화 기호 `₩`**(`₩765,000`·`₩1,250,000`)를 붙여 표시합니다. 예전에는 이 `₩` 때문에 숫자로 못 읽어 **값이 조용히 비워지고(null)** 대사 상태가 「불일치·보류」로 잘못 잡히거나, 입금 행이 **자동 매칭·수납에서 빠질** 수 있었습니다. 이제 콤마·「원」·공백과 함께 **`₩`도 떼어** 정확한 금액으로 읽습니다(콤마·「원」만 붙은 기존 파일 동작은 그대로).
- **내 화면/업무에 영향**: **`/billing/imports/nhis` 대사**·**`/billing/payments` 은행 입금 엑셀** — 통화 서식으로 저장돼 `₩` 기호가 붙은 엑셀에서도 대사 판정·금액 매칭이 정확해짐
- **상태**: 완료

<details><summary>자세히</summary>

- BE: `NhisExcelParser.normalizeNumeric`·`BankDepositExcelParser.parseAmount` — `WON_SIGN`(U+20A9) 제거 추가(콤마·「원」·공백 정규화 lockstep). 회귀 `@Test` 각 +1 (`1d067d9`)
</details>

### ✅ 급여제공 서비스 집계 리포트 기간 거꾸로 입력 시 즉시 차단 (FE, L02_M12)
- **에이전트**: COD
- **한 일**: **급여제공 서비스 집계 리포트**(`/care/reports/service-summary`)에서 **시작일이 종료일보다 뒤**인 역방향 기간으로 조회하면, 예전에는 **서버까지 요청을 보낸 뒤** 400 오류가 떴습니다. 이제 **조회 전에 화면에서 바로** 「종료일은 시작일 이후여야 합니다.」로 종료일 칸에 안내하고, 오류와 어긋나는 **지난 집계 표도 함께 비웁니다**(한쪽 날짜만 비면 서버가 기본 기간으로 채우므로 종전대로 조회됩니다).
- **내 화면/업무에 영향**: **`/care/reports/service-summary`** — 역방향 기간을 **즉시** 안내, 불필요한 서버 오류 대기 없음
- **상태**: 완료

<details><summary>자세히</summary>

- FE: `ServiceSummaryReportPage.jsx` — `resolveCareReportDateRangeError`(신규 `config/careReports.js`)로 역방향 사전 차단·BE `CareReportService.resolveDateWindow` 문구 lockstep·종료일 필드 `role="alert" aria-invalid`. 회귀 테스트 추가 (`cf360d7`)
</details>

### 📝 baseline 동기화 — SEC-D34·UXD-195 사후 작업 완료 (TWR)
- **에이전트**: TWR
- **한 일**: develop HEAD 실측 후 CHANGELOG baseline을 **BE `68c2378` · FE `ab9ef17`** 로 갱신했습니다. **공단 급여일수·은행 입금 금액 정규화**(SEC-D34) 및 **이동서비스비 기간 검증·a11y 개선**(G16·UXD-195)의 회귀 테스트와 a11y 사후 작업이 완료되어 baseline을 진전시켰습니다.
- **내 화면/업무에 영향**: 없음 — 문서만 갱신, 사용자 화면 변화 없음
- **상태**: 완료

<details><summary>자세히</summary>

- BE `68c2378`: `test(v3/SEC-D34): lock day-marker NHIS days and whitespace-grouped bank amount normalization` — 공단·은행 엑셀 정규화 회귀 lock
- FE `ab9ef17`: `fix(a11y/transport): focus first invalid service-fee date field on blocked 조회/생성 (UXD-195 follow-up)` — service-fee 기간 오류 시 포커스 관리(키보드·스크린리더)
- FE `32b7ae3`: `fix(a11y/transport): route service-fee date-range error to date fields (UXD-195)` — service-fee date-range 오류를 date 필드로 라우팅
</details>

### 📝 공단 급여일수 「일」 표기·이동서비스비 기간 오류 시 목록 FAQ·매뉴얼 반영 (TWR)
- **에이전트**: TWR
- **한 일**: develop HEAD 실측 후 CHANGELOG·FAQ·USER_MANUAL baseline을 **BE `ec7a1ce` · FE `6c280d0`** 로 맞추고, **공단 대사 엑셀 급여일수 `15일` 표기 정규화**를 **Q939** 보강으로, **이동서비스비 기간 오류 시 지난 청구 목록 즉시 비움**을 **Q940** 보강으로 정리했습니다.
- **내 화면/업무에 영향**: 없음 — 운영 문서만 갱신
- **상태**: 완료

<details><summary>자세히</summary>

- FAQ Q939·Q940 보강 · USER_MANUAL §4-6-1·§5-8-1 보강 · baseline 동기화(BE `ec7a1ce` / FE `6c280d0`)
</details>

### ✅ 공단 대사 엑셀 급여일수 `15일` 표기 정상 인식 (BE, SEC-D34)
- **에이전트**: COD
- **한 일**: 공단 명세(NHIS) 대사 엑셀의 **급여일수** 칸이 `15일` 처럼 공단 export가 흔히 붙이는 **「일」 접미사**가 있으면, 예전에는 숫자로 못 읽어 **값이 조용히 비워지고(null)** 실제로는 일치하는데 **「불일치」·「보류」로 잘못** 잡힐 수 있었습니다. 이제 「일」·「원」·공백·콤마를 함께 떼어 **정확한 일수로 읽어** 대사 결과가 맞게 나옵니다(금액 칸에는 「일」이 없어 동작 변화 없음).
- **내 화면/업무에 영향**: **`/billing/imports/nhis` 대사 화면** — `15일`·`  15  `·`765,000원` 등 **표시서식이 붙은 공단 엑셀에서도 일치/불일치 판정이 정확**해짐
- **상태**: 완료

<details><summary>자세히</summary>

- BE: `NhisExcelParser.normalizeNumeric` — `replace("일", "")` 추가(「원」·공백 정규화 lockstep). 회귀 `@Test` +1 (`ec7a1ce`)
</details>

### ✅ 이동서비스비 기간 오류 시 지난 청구 목록 즉시 비움 (FE, G16)
- **에이전트**: COD
- **한 일**: **이동서비스비 청구**(`/transport/service-fees`)에서 **빈 기간·역방향 기간**으로 조회가 화면에서 막힐 때, 예전에는 **오류 안내만 뜨고 이전에 조회했던 청구 목록이 그대로** 남아 혼란을 줄 수 있었습니다. 이제 기간 검증에 걸리면 **목록도 함께 비워** EmptyState로 돌아가, 오류와 표 내용이 모순되지 않습니다(정상 기간 조회·생성 동작은 동일).
- **내 화면/업무에 영향**: **`/transport/service-fees`** — 잘못된 기간 입력 후 **지난 조회 결과가 남지 않음**
- **상태**: 완료

<details><summary>자세히</summary>

- FE: `TransportServiceFeePanel.load` — pre-block 분기(빈·역방향 기간)에서 `records` 초기화 추가(성공·건너뜀 배너 clear와 동일 계열, `9b0481d` lineage). 회귀 테스트 추가 (`6c280d0`)
</details>

### 📝 은행 입금 금액 정규화·이동서비스비 빈 기간 FAQ·매뉴얼 반영 (TWR)
- **에이전트**: TWR
- **한 일**: develop HEAD 실측 후 CHANGELOG·FAQ·USER_MANUAL baseline을 **BE `dc261ed` · FE `171075f`** 로 맞추고, **은행 입금 엑셀의 공백 천 단위·「원」 금액 정규화**를 **Q941** 로, **이동서비스비 청구의 빈 기간(시작일·종료일 미입력) 사전 차단**을 **Q940** 보강으로 정리했습니다.
- **내 화면/업무에 영향**: 없음 — 운영 문서만 갱신
- **상태**: 완료

<details><summary>자세히</summary>

- FAQ Q941 신설·Q940 빈 기간 행 추가·USER_MANUAL §4-6·§5-8-1 보강·baseline 동기화(BE `dc261ed` / FE `171075f`)
</details>

### ✅ 은행 입금 엑셀의 공백·「원」 붙은 입금액 정상 인식 (BE, SEC-D34)
- **에이전트**: COD
- **한 일**: **은행 입금 엑셀**의 **입금액** 칸이 `1 250 000원` 처럼 **공백으로 천 단위를 띄우거나 「원」이 붙어** 있으면, 예전에는 숫자로 못 읽어 **값이 조용히 비워지고(null)** 그 입금 행이 **자동 매칭·수납에서 빠질** 수 있었습니다. 이제 콤마·「원」·**모든 공백**을 떼어 **정확한 금액으로 읽어** 미리보기·일괄 등록에 반영합니다(공단 대사 엑셀과 동일한 정규화 방식).
- **내 화면/업무에 영향**: **`/billing/payments` 은행 입금 엑셀** — 표시서식이 붙은 은행 엑셀에서도 **금액 매칭·자동 수납이 정확**해짐
- **상태**: 완료

<details><summary>자세히</summary>

- BE: `BankDepositExcelParser.parseAmount` — `replaceAll("\\s+", "")` 로 내부 공백 제거·`NhisExcelParser.normalizeNumeric` lockstep. 회귀 `@Test` +1 (`dc261ed`)
</details>

### ✅ 이동서비스비 청구 기간을 비워 두면 바로 안내 (FE, G16)
- **에이전트**: COD
- **한 일**: **이동서비스비 청구**(`/transport/service-fees`)에서 **시작일 또는 종료일이 비어 있는** 상태로 조회·생성하면, 예전에는 **서버까지 요청을 보낸 뒤** 400 오류가 떴습니다. 이제 **조회·생성 전에 화면에서 바로** 「조회 기간의 시작일과 종료일이 필요합니다.」로 안내하고 서버 왕복을 건너뜁니다(역방향 기간 안내와 같은 방식).
- **내 화면/업무에 영향**: **`/transport/service-fees`** — 기간 미입력을 **즉시** 안내, 불필요한 서버 오류 대기 없음
- **상태**: 완료

<details><summary>자세히</summary>

- FE: `TransportServiceFeePanel.jsx` — `resolveTransportServiceFeeDateRangeError`(신규 `config/transportServiceFee.js`)로 필수→순서 단일 검증·BE `TransportServiceFeeService.validateDateRange` 문구 lockstep. 회귀 테스트 추가 (`171075f`)
</details>

### 📝 엑셀 import 셀 복원·대사 금액 정규화·이동서비스비 폼 FAQ·매뉴얼 반영 (TWR)
- **에이전트**: TWR
- **한 일**: develop HEAD 실측 후 CHANGELOG·FAQ·USER_MANUAL baseline을 **BE `ad2c0b1` · FE `3b903c8`** 로 맞추고, **공단·RFID 엑셀의 깨진 셀 복원**(방문 시간·RFID 태그 시각)·**대사 엑셀 금액/급여일수 「원」·공백 정규화**를 **Q939** 로, **이동서비스비 청구 폼의 역방향 기간 차단·결과 안내 갱신·이용자 이름 표시**를 **Q940** 으로 정리했습니다.
- **내 화면/업무에 영향**: 없음 — 운영 문서만 갱신
- **상태**: 완료

<details><summary>자세히</summary>

- FAQ Q939·Q940 신설·USER_MANUAL §4-6/§4-6-1·이동서비스비 섹션 보강·baseline 동기화(BE `ad2c0b1` / FE `3b903c8`)
</details>

### ✅ 공단 대사 엑셀의 「원」·공백 붙은 금액·급여일수 정상 인식 (BE)
- **에이전트**: COD
- **한 일**: 공단 명세(NHIS) 대사 엑셀에서 **공단부담금**이 `765,000원` 처럼 「원」이 붙거나 **급여일수**가 `  15  ` 처럼 공백이 섞여 있으면, 예전에는 숫자로 못 읽어 **값이 조용히 비워지고(null)** 그 결과 대사 상태가 실제로는 일치하는데도 **「불일치」·「보류」로 잘못** 잡힐 수 있었습니다. 이제 「원」 표시와 앞뒤 공백을 떼어내 **정확한 금액·일수로 읽어** 대사 결과가 맞게 나옵니다. (숫자로 볼 수 없는 셀은 종전처럼 비워 두어 행 자체는 계속 등록됩니다.)
- **내 화면/업무에 영향**: **`/billing/imports/nhis` 대사 화면** — 표시서식이 붙은 공단 엑셀에서도 **일치/불일치 판정이 정확**해짐
- **상태**: 완료

<details><summary>자세히</summary>

- BE: `NhisExcelParser` — `parseAmount`/`parseInteger` 를 공용 `normalizeNumeric()` 로 통합(콤마 + `원` 통화 마커 + 공백 제거·`BankDepositExcelParser` lockstep). 행 단위 복원 유지(비숫자 셀은 null degrade). 회귀 `@Test` +2 (9→11) (`ad2c0b1`)
</details>

### ✅ RFID 전송 엑셀의 범위 밖 태그 시각 때문에 전체가 거부되던 문제 개선 (BE, SEC-D34)
- **에이전트**: COD
- **한 일**: **RFID 전송 엑셀**의 태그 시각 칸에 `9999`(→99:99)·`060`(→00:60) 처럼 **시·분 범위를 벗어난 값**이 하나라도 있으면, 예전에는 **파일 전체**가 「엑셀 파일을 읽을 수 없습니다.」로 거부됐습니다. 이제 이런 셀은 **그 시각만 비워 두고 해당 행은 계속 등록**되어, 셀 하나 때문에 전체 업로드가 막히지 않습니다(방문일정 엑셀과 동일한 방식).
- **내 화면/업무에 영향**: **`/visits` RFID 계획·태그 비교** — 태그 시각이 일부 깨진 파일도 **정상 행은 비교에 반영**
- **상태**: 완료

<details><summary>자세히</summary>

- BE: `RfidTransmissionExcelParser.parseTime` — compact(3~4자리 숫자) 시각 분기를 예외 가드 안으로 이동해 out-of-range 값이 file-level 실패 대신 null tag time 으로 degrade. 회귀 `@Test` +1 (5→6) (`6329323`)
</details>

### ✅ 방문일정 엑셀의 지나치게 큰 서비스 시간 때문에 전체가 거부되던 문제 개선 (BE, SEC-D34)
- **에이전트**: COD
- **한 일**: **NHIS 방문일정 엑셀**의 **서비스 시간(분)** 칸에 처리할 수 없을 만큼 **큰 값**이 하나라도 있으면 예전에는 파일 전체 등록이 실패했습니다. 이제 그런 셀은 **시작·종료 시각의 차이로 다시 계산**해 행을 살리므로, 셀 하나 때문에 전체 업로드가 막히지 않습니다.
- **내 화면/업무에 영향**: **방문 관리 NHIS 방문일정 업로드** — 시간 값이 일부 깨진 파일도 **정상 행은 등록**
- **상태**: 완료

<details><summary>자세히</summary>

- BE: `NhisVisitScheduleExcelParser` — 서비스 시간 파싱 `NumberFormatException` 가드 후 time-diff fallback. 회귀 `@Test` +14 (`13eb863`)
</details>

### ✅ 이동서비스비 청구 기간을 거꾸로(시작일>종료일) 넣으면 바로 안내 (FE, G16)
- **에이전트**: COD
- **한 일**: **이동서비스비 청구**(`/transport/service-fees`)에서 **시작일이 종료일보다 뒤**인 기간으로 조회·생성하면, 예전에는 서버까지 요청을 보낸 뒤에야 오류가 떴습니다. 이제 **조회·생성 전에 화면에서 바로** 「시작일은 종료일보다 이후일 수 없습니다.」로 안내하고 서버 왕복을 건너뜁니다. 또한 조회할 때마다 **지난 결과 안내(성공·건너뜀)** 가 남지 않고 최신 결과만 보이며, 목록 응답 형식 차이로 **이용자 이름이 비어 보이던** 경우도 바로잡았습니다.
- **내 화면/업무에 영향**: **`/transport/service-fees`** — 잘못된 기간을 **즉시** 안내, 지난 결과가 헷갈리게 남지 않고, **이용자 이름 정상 표시**
- **상태**: 완료

<details><summary>자세히</summary>

- FE: `TransportServiceFeePanel.jsx` — 조회/생성 전 `isTransportServiceFeeDateRangeInOrder`(신규 `config/transportServiceFee.js`)로 역방향 기간 사전 검사(BE `TransportServiceFeeService.validateDateRange` 문구 lockstep) · `load()` 가 success/skipped 배너까지 초기화 · client 목록을 정규화된 `services` 형태로 파싱해 이름 resolve. 회귀 테스트 추가 (`9f12482`·`9b0481d`·`3b903c8`)
</details>

### 📝 배차 「회차」 휠 스크롤·오류 중복 읽힘 FAQ·매뉴얼 반영 (TWR)
- **에이전트**: TWR
- **한 일**: develop HEAD 실측 후 CHANGELOG·FAQ·USER_MANUAL baseline을 **BE `417e2ff` · FE `5aaee88`** 로 맞추고, **`/transport/runs/new`** 회차 칸의 **마우스 휠 스크롤 값 변경 차단**과 **서버 회차 오류 중복 읽힘 정리**(UXD-194)를 **Q936**·§5-8에 반영했습니다.
- **내 화면/업무에 영향**: 없음 — 운영 문서만 갱신
- **상태**: 완료

<details><summary>자세히</summary>

- FAQ Q936 보강(휠 스크롤·중복 announcement 행 추가)·USER_MANUAL §5-8 보강·baseline 동기화(BE `417e2ff` / FE `5aaee88`)
</details>

### ✅ 배차 「회차」 칸에서 마우스 휠로 값이 몰래 바뀌던 문제 차단 (FE)
- **에이전트**: COD
- **한 일**: **새 픽업 배차**(`/transport/runs/new`)의 **회차** 칸(숫자 입력)에 커서가 놓인 상태로 **마우스 휠로 페이지를 스크롤**하면, 브라우저 기본 동작 때문에 회차 숫자가 **조용히 오르내려** 사용자가 눈치채지 못한 채 엉뚱한 회차로 저장될 수 있었습니다. 이제 회차 칸 위에서 휠을 굴리면 **커서가 회차 칸에서 떨어지고 페이지만 스크롤**되어, 값이 몰래 바뀌지 않습니다.
- **내 화면/업무에 영향**: **`/transport/runs/new`** — 회차를 입력하다 스크롤할 때 **회차 값이 실수로 바뀌는 사고 방지**
- **상태**: 완료

<details><summary>자세히</summary>

- FE: `TransportRunNewPage.jsx` — 회차 `<input type="number">` 에 `onWheel` → `event.currentTarget.blur()` 추가로 브라우저의 wheel-step 값 변경 차단. BE `@Min(1)` Integer 계약과 lockstep 유지. `TransportRunNewPage.test.jsx` 회귀 추가(휠 시 포커스 해제 검증) (`5aaee88`)
</details>

### ✅ 배차 회차 오류 안내가 두 번 읽히던 문제 정리 (FE, 접근성)
- **에이전트**: COD
- **한 일**: **새 픽업 배차**(`/transport/runs/new`)에서 서버가 **회차 관련 오류**를 돌려줄 때, 같은 안내가 **화면 상단 알림**과 **회차 칸** 두 곳에 동시에 떠서 스크린리더가 **같은 내용을 두 번** 읽어 주었습니다. 이제 회차 관련 오류는 **회차 칸 한 곳에만** 표시하고(커서도 그 칸으로 이동), 상단 알림은 **회차와 무관한 오류일 때만** 뜹니다.
- **내 화면/업무에 영향**: **`/transport/runs/new`** — 회차 오류 시 **안내가 한 번만** 표시·읽힘(스크린리더 사용자 편의)
- **상태**: 완료

<details><summary>자세히</summary>

- FE: `TransportRunNewPage.jsx` — `createTransportRunApi` catch 블록에서 `fieldErrors.departureRound` 는 필드 오류(`role="alert"`)로만 라우팅하고 일반 상단 `actionError` 는 비필드 오류에만 노출(중복 `role="alert"` 동시 announcement 제거). WCAG 3.3.1 / 4.1.3. `TransportRunNewPage.test.jsx` 상단 배너 미노출 assert 추가 (`eca424f`, UXD-194)
</details>

### 📝 방문일정 공단 엑셀 파서 검증 분기 회귀 고정 (BE, SEC-D34)
- **에이전트**: COD
- **한 일**: 방문 관리에서 쓰는 **NHIS 방문일정 엑셀 파서**의 **헤더·필수 열·유효 데이터 행 없음** 안전 거부 동작을, 다른 엑셀 파서들과 같은 방식으로 **회귀 테스트로 고정**했습니다. 실제 동작·안내 문구 변화는 없습니다.
- **내 화면/업무에 영향**: 없음 — 테스트 전용(동작 그대로)
- **상태**: 완료

<details><summary>자세히</summary>

- BE: `NhisVisitScheduleExcelParserTest` +58L — fail-closed 검증 분기(`BusinessRuleException`) lock (`417e2ff`)
</details>

### 📝 RFID 전송 엑셀 파서 검증 분기 회귀 고정 (BE, SEC-D34)
- **에이전트**: COD
- **한 일**: 방문 RFID 비교에서 쓰는 **RFID 전송 엑셀 파서**에 대해 **헤더 줄 누락·필수 열(장기요양인정번호/방문일) 누락·유효 데이터 행 없음** 세 가지를 안전하게 거부하던 동작을, 요양보호사·NHIS 파서와 같은 방식으로 **회귀 테스트로 고정**했습니다. 실제 동작·안내 문구 변화는 없습니다.
- **내 화면/업무에 영향**: 없음 — 테스트 전용(동작 그대로)
- **상태**: 완료

<details><summary>자세히</summary>

- BE: `RfidTransmissionExcelParserTest` +59L — 3개 fail-closed 분기(`BusinessRuleException`) lock: 「엑셀 헤더 행이 없습니다.」·「RFID 전송 엑셀에 장기요양인정번호·방문일 컬럼이 필요합니다.」·「엑셀에서 유효한 RFID 전송 행을 찾을 수 없습니다.」 (`4dcf60d`)
</details>

### 📝 RFID 전송 엑셀 검증 안내 FAQ·매뉴얼 반영 (TWR)
- **에이전트**: TWR
- **한 일**: develop HEAD 실측 후 CHANGELOG·FAQ·USER_MANUAL baseline을 **BE `4dcf60d` · FE `b115ae0`** 로 맞추고, **`/visits` RFID 비교**에서 RFID 전송 엑셀 형식 오류 시 표시되는 **헤더·필수열·데이터행 안내**를 **Q938**·§5-11에 정리했습니다.
- **내 화면/업무에 영향**: 없음 — 운영 문서만 갱신
- **상태**: 완료

<details><summary>자세히</summary>

- FAQ Q938 신설 · USER_MANUAL §5-8·§5-11 보강 · baseline 동기화
</details>

### ✅ 픽업 배차 「회차」에 지나치게 큰 수 입력 거부 (FE)
- **에이전트**: COD
- **한 일**: **새 픽업 배차**(`/transport/runs/new`) 회차 칸에 **`9999999999`** 처럼 아주 큰 수를 넣으면, 값 자체는 정수라 화면 검증은 통과했지만 서버가 다룰 수 있는 한도를 넘어 **원인을 알 수 없는 오류**가 화면 상단에만 떴습니다. 이제 이런 값은 **저장 전에 회차 칸 아래에 「회차 값이 너무 큽니다. 다시 확인하세요.」** 로 바로 안내합니다. 일반 회차(1·2·3…) 입력과 비워 두면 자동 배정되는 동작은 그대로입니다.
- **내 화면/업무에 영향**: **`/transport/runs/new`** — 회차에 실수로 아주 큰 수를 넣었을 때 **원인 불명 오류 대신 명확한 사유**로 안내
- **상태**: 완료

<details><summary>자세히</summary>

- 실측: BE develop `4dcf60d` · FE develop `b115ae0` — **133 route** · **106 page** · Flyway **V1–V196** · 모듈 **97.41%**
- FE: `config/transport.js` — `MAX_DEPARTURE_ROUND`(2147483647) 상수·`DEPARTURE_ROUND_TOO_LARGE_MESSAGE` 추가, `parseDepartureRoundInput()`에서 32비트 `Integer` 상한 초과 값을 별도 사유로 사전 차단. BE `CreateTransportRunRequest.departureRound` `@Min(1)` Integer 계약과 lockstep. `config/transport.test.js` 회귀 추가 (`b115ae0`)
</details>

### 📝 라이브 E2E 준비상태 판정 관문 보강 (BE, QA-B95)
- **에이전트**: COD
- **한 일**: 라이브 E2E 점검에서 게이트웨이가 신호 문자를 **`&x2d;`** 처럼 `#` 없는 형태로 바꿔 보내도 **준비 미완료 표시를 정확히 인식**하도록 내부 판정 규칙을 보강했습니다. 실제 앱 화면·운영 동작에는 변화가 없는 **테스트·점검 인프라** 개선입니다.
- **내 화면/업무에 영향**: 없음 — 내부 점검(라이브 E2E) 전용, 제품 흐름 변화 없음
- **상태**: 완료

<details><summary>자세히</summary>

- BE: `LiveE2eOperationReadinessSupport` — bare-hex HTML entity(`&x2d;` 등) 디코딩 분기 추가로 gateway-trimmed payload에서도 bootstrap-disabled marker를 fail-closed로 해석, readiness gate 우회 차단. `LiveE2eOperationReadinessSupportTest` 회귀 추가 (`ae1c6a1`)
</details>

### ✅ 픽업 배차 「회차」 입력, 저장 전에 바로 확인 (FE)
- **에이전트**: COD
- **한 일**: **새 픽업 배차**(`/transport/runs/new`) 화면의 **회차** 칸에 **0·음수·소수** 같은 잘못된 값을 넣고 임시 저장하면, 이전에는 값이 서버까지 갔다가 되돌아온 뒤에야 화면 상단 알림으로만 안내됐습니다. 이제 **저장을 누르는 즉시 회차 칸 아래에 「회차는 1 이상의 정수를 입력하세요.」** 로 안내하고, 서버가 회차 관련 오류를 돌려줄 때도 같은 칸에 표시합니다. 비워 두면 예전처럼 **다음 회차로 자동 배정**됩니다.
- **내 화면/업무에 영향**: **`/transport/runs/new`** — 회차를 잘못 입력했을 때 **어느 칸이 문제인지 바로** 보이고, 불필요한 저장 시도가 줄어듦
- **상태**: 완료

<details><summary>자세히</summary>

- 실측: BE develop `924b8d8` · FE develop `23b47ea` — **133 route** · **106 page** · Flyway **V1–V196** · 모듈 **97.41%**
- FE: `TransportRunNewPage.jsx` — 저장 전 회차 값이 있으면 `Number.isInteger` && `>= 1` 검증 후 차단, `Field error`로 필드 단위 표시, 서버 `fieldErrors.departureRound` 매핑, 입력 변경 시 오류 초기화
</details>

### ✅ 픽업 배차 「회차」에 `1e2·0x1f` 같은 지수/16진수 입력 거부 (FE)
- **에이전트**: COD
- **한 일**: **새 픽업 배차**(`/transport/runs/new`) 회차 칸은 숫자 입력이라 브라우저가 **`1e2`(지수) · `0x1f`(16진수)** 같은 표기도 받아들였는데, 예전에는 이를 각각 **100·31로 조용히 바꿔** 엉뚱한 회차로 저장했습니다. 이제는 **오타로 이런 값을 넣으면 저장 전에 「회차는 1 이상의 정수를 입력하세요.」** 로 막습니다. 일반 정수(1·2·3…) 입력과 비워 두면 자동 배정되는 동작은 그대로입니다.
- **내 화면/업무에 영향**: **`/transport/runs/new`** — 회차에 잘못된 숫자 표기를 넣었을 때 **엉뚱한 회차로 저장되는 사고 방지**
- **상태**: 완료

<details><summary>자세히</summary>

- FE: `config/transport.js` `parseDepartureRoundInput()` — `Number()`(지수/16진수 무음 강제변환) 대신 **평문 10진 정수**만 허용하도록 검증, BE `@Min(1)` Integer 계약과 일치. `config/transport.test.js` 회귀 추가
</details>

### ✅ 배차 회차 오류 시 회차 칸으로 커서 자동 이동 (FE, 접근성)
- **에이전트**: COD
- **한 일**: **새 픽업 배차**(`/transport/runs/new`)에서 회차 입력이 막혀 오류가 뜰 때(브라우저 사전 검증·서버 반환 오류 모두), 예전에는 오류 안내만 읽히고 **커서는 저장 버튼에 남아 있어** 키보드·스크린리더 사용자가 문제 칸을 직접 찾아 올라가야 했습니다. 이제 **오류가 나면 커서가 회차 칸으로 바로 이동**합니다.
- **내 화면/업무에 영향**: **`/transport/runs/new`** — 회차 오류 시 **어느 칸을 고쳐야 하는지 커서로 바로 안내**(키보드·스크린리더 편의)
- **상태**: 완료

<details><summary>자세히</summary>

- FE: `TransportRunNewPage.jsx` — `handleSaveDraft` 차단(FE 사전 검증·BE `departureRound` 필드 오류) 시 회차 input에 포커스 이동. WCAG 2.4.3 Focus Order / 3.3.1 Error Identification. `TransportRunNewPage.test.jsx` `toHaveFocus` 회귀 추가
</details>

### ✅ 배차 정차 상한 초과 시 사유 안내 (FE)
- **에이전트**: COD
- **한 일**: 루트 상세(`/transport/runs/:runId`)에서 **지점·경유지**를 계속 추가하다 전체 **정차 상한(17개)** 에 걸리면, 이전에는 **아무 반응 없이 추가만 안 되던** 상태였습니다. 이제 상한에 막히면 **「정차 순서는 최대 17개까지 가능합니다.」** 로 사유를 화면에 안내합니다.
- **내 화면/업무에 영향**: **`/transport/runs/:runId`** — 지점/경유지 추가가 안 될 때 **왜 막혔는지** 바로 알 수 있음
- **상태**: 완료

<details><summary>자세히</summary>

- FE: `config/transport.js` — 하드코딩 `17`을 `MAX_TRANSPORT_ROUTE_STOPS` 상수·`TRANSPORT_ROUTE_STOPS_LIMIT_MESSAGE` 로 분리, `TransportRunDetailPage.jsx` 지점 추가·경유지 추가 경로에서 상한 초과 시 `actionError` 노출
- BE `TransportService.MAX_WAYPOINTS`(=17) lockstep — 이용자 정차 상한 `MAX_TRANSPORT_STOPS`(=15)와는 별개
</details>

### 📝 엑셀 일괄등록 안내 문구 코드 정리 (BE·FE, SEC-D34)
- **에이전트**: COD
- **한 일**: 엑셀 일괄등록 화면에서 보이던 두 안내 문구(**「업로드할 엑셀 파일이 없습니다.」**·**「엑셀 파일을 읽을 수 없습니다.」**)가 여러 파일에 문자열로 흩어져 있던 것을 **코드 한 곳(공용 상수)** 으로 모았습니다. 새 엑셀 업로드 화면이 생겨도 문구가 서로 어긋나지 않도록 하는 **내부 정리**로, 실제로 보이는 문구와 동작은 그대로입니다.
- **내 화면/업무에 영향**: 없음 — 문구·화면·동작 변화 없는 코드 정리(리팩터링)
- **상태**: 완료

<details><summary>자세히</summary>

- 실측: BE develop `924b8d8` · FE develop `23b47ea` — **133 route** · **106 page** · Flyway **V1–V196** · 모듈 **97.41%**
- BE: `BankDepositImportService` · `StaffNhisCaregiverImportService` 를 `MISSING_EXCEL_MESSAGE` 상수로 통일(4개 import service 단일 상수 참조) · 「엑셀 파일을 읽을 수 없습니다.」도 5개 파서·4개 import service의 `UNREADABLE_EXCEL_MESSAGE` 상수로 통일
- FE: `excelImportFiles.js` — pre-upload 헤더 읽기 실패 문구를 `EXCEL_IMPORT_UNREADABLE_MESSAGE` 상수로 추출, BE house-style 문구와 verbatim lockstep

</details>

### 📝 요양보호사 공단 엑셀 파서 안전 거부 분기 회귀 고정 (BE, SEC-D34)
- **에이전트**: COD
- **한 일**: 요양보호사 공단 엑셀 업로드 파서에서 **헤더 줄 누락·필수 열(급여제공자인력번호/성명) 누락·유효 데이터 행 없음** 세 가지 상황을 안전하게 거부(안내 후 중단)하던 동작을, 앞으로도 깨지지 않도록 **회귀 테스트로 고정**했습니다. 실제 동작·문구 변화는 없습니다.
- **내 화면/업무에 영향**: 없음 — 테스트 전용(동작 그대로)
- **상태**: 완료

<details><summary>자세히</summary>

- BE: `StaffNhisCaregiverExcelParserTest` +60L — 3개 미검증 fail-closed 분기(`BusinessRuleException`) lock, `NhisExcelParser` parser-layer 회귀와 동일 패턴 (`5df9999`)
</details>

### 📝 SEC-D34 엑셀 import 보강 테스트·정정 
- **에이전트**: COD
- **한 일**: develop HEAD 실측 후 **BE `73a3a63` / FE `495040f`** 로 기준(CHANGELOG+FAQ) 동기화. **엑셀 import 손상 OOXML·빈 파일 fail-closed 회귀 테스트**를 **방문 통합 계층**과 **은행/요양보호사/방문 파서 계층** 양쪽에서 고정했고, **필수엑셀 사본 누락** 사전검증을 import entrypoints 5종에서 강화했습니다. 
- **내 화면/업무에 영향**: 없음 — 테스트·정정 전용. 제품 흐름 변화 없음
- **상태**: 완료

<details><summary>자세히</summary>

- BE: `73a3a63`(missing copy lock) + `b3e7cce`(empty/missing 문구 통일) + `2c102e5`(visit integration fail-closed) + `7fa8335`(parser corrupt body) + `0a97b22`(parser fail-closed)
- FE: `495040f`(FE empty/missing 문구) + `3e89ab7`(은행 입금 import OOXML fixture) + `51a3db4`(NHIS MIME-spoof reject) + `d0c8fd2`(인쇄 메뉴 숨김) + `6f8e349`(RFID 이중엑셀 magic-byte)

</details>

### ✅ 리포트 인쇄 메뉴 숨김·엑셀 안내 문구 통일 ops 문서화
- **에이전트**: TWR
- **한 일**: develop HEAD 실측 후 CHANGELOG 기준(BE `b3e7cce` · FE `3e89ab7`)을 갱신하고, **리포트 인쇄 시 화면 메뉴 숨김**(UXD-192)과 **엑셀 일괄등록 빈/없는 파일 안내 문구 통일**을 변경 기록·FAQ에 반영했습니다.
- **내 화면/업무에 영향**: 없음 — 운영·배포 가이드·FAQ만 갱신
- **상태**: 완료

<details><summary>자세히</summary>

- 실측: BE develop `924b8d8` · FE develop `23b47ea` — **133 route** · **106 page** · Flyway **V1–V196** · 모듈 **97.41%**
- FAQ Q935 신설(리포트 인쇄 메뉴 숨김) · Q934 보강(빈/없는 파일 안내 문구 통일) · Q930~Q933 유지

</details>

### ✅ 리포트 인쇄물에서 화면 메뉴 숨김 (FE, UXD-192)
- **에이전트**: UXD
- **한 일**: **청구·청구 통계·이용자 외출·교통 월간 리포트**를 인쇄하면 이전에는 화면 좌측/상단 **앱 이동 메뉴(context navigation)** 가 인쇄물에 함께 찍혔습니다. 이제 이 메뉴를 전역 인쇄 규칙에 포함해 **모든 리포트 인쇄물에서 메뉴가 나오지 않도록** 정리했습니다.
- **내 화면/업무에 영향**: **`/billing/reports` · `/billing/statistics` · `/clients` 외출 리포트 · 교통 월간 리포트** — 화면 표시는 그대로, **인쇄물이 깔끔해져** 리포트 본문만 출력됨
- **상태**: 완료

<details><summary>자세히</summary>

- FE: `styles/components.css` — `@media print` 전역 숨김 그룹에 `.ds-context-nav` 승격(`.ds-sidenav`·`.ds-topbar`와 동일), 페이지 한정 규칙 제거 (`d0c8fd2`)
- 대상: `BillingReportPage` · `BillingStatisticsReportPage` · `ClientOutingReportPage` · `TransportMonthlyReportsPage`
- 회귀: `printStylesheet.test.js` — 전역 인쇄 숨김 계약 고정 · 화면 렌더링 변화 없음(인쇄 전용)

</details>

### ✅ 엑셀 일괄등록 「빈/없는 파일」 안내 문구 통일 (BE, SEC-D34)
- **에이전트**: COD
- **한 일**: 파일을 첨부하지 않았거나 내용이 없는 엑셀을 올릴 때, **공단 방문일정·청구 NHIS** 화면만 「업로드할 엑셀 파일이 **필요합니다**.」로, 나머지(요양보호사·은행 입금·서류 저장) 화면은 「업로드할 엑셀 파일이 **없습니다**.」로 문구가 갈렸습니다. 이제 **모든 엑셀 일괄등록 화면이 「업로드할 엑셀 파일이 없습니다.」** 로 동일하게 안내합니다.
- **내 화면/업무에 영향**: 정상 업로드는 그대로. 빈/없는 파일을 올렸을 때 **화면마다 다르던 안내 문구가 하나로 통일**됨
- **상태**: 완료

<details><summary>자세히</summary>

- BE: `VisitService` · `NhisImportService` — `MISSING_EXCEL_MESSAGE` 상수(「업로드할 엑셀 파일이 없습니다.」)로 empty/missing 분기 통일 (`b3e7cce`)
- 회귀: `VisitServiceTest` · `NhisImportServiceTest` 기대 문구 정정 · 제품 흐름 변화 없음(문구 일치)

</details>

### ✅ 엑셀 import 손상/빈 파일 거부 회귀 테스트 보강 (FE·BE, SEC-D34)
- **에이전트**: COD
- **한 일**: 손상·위장·빈 엑셀 거부 동작이 앞으로도 깨지지 않도록 **회귀 테스트를 여러 계층에 추가**했습니다. **손상된 본문**(파서 계층·방문 통합 계층), **RFID 비교 이중 엑셀 사전검증**, **청구 NHIS 위장(MIME 스푸핑) 사전 거부**, **은행 입금 엑셀 픽스처**를 실제 서명과 일치시켰습니다.
- **내 화면/업무에 영향**: 없음 — 테스트 전용. 제품 동작 변화 없음
- **상태**: 완료

<details><summary>자세히</summary>

- BE: 손상 OOXML 본문 fail-closed를 은행/요양보호사/방문 **파서 계층**(`7fa8335`)과 **방문 통합 계층 `VisitService`**(`2c102e5`)에서 고정
- FE: RFID 비교 이중 엑셀 업로드 전 매직바이트 검증(`6f8e349`) · 청구 NHIS import MIME 스푸핑 사전 거부(`51a3db4`) · `pilotPageFlows` US-L01 은행 입금 import OOXML 픽스처 정정(`3e89ab7`, QA-B609)

</details>

### ✅ 손상된 엑셀(내용이 깨진 파일) 안전 거부 (BE, SEC-D34)
- **에이전트**: COD
- **한 일**: 앞부분 서명(`PK\x03\x04`)은 엑셀처럼 보이지만 **실제 내용이 깨진 파일**을 올리면 이전에는 화면에 시스템 오류가 그대로 노출될 수 있었습니다. 이제 은행 입금·청구 NHIS·요양보호사 NHIS·공단 방문일정·RFID 비교 **5개 엑셀 일괄등록**에서 이런 파일을 항상 **「엑셀 파일을 읽을 수 없습니다.」** 로 안전하게 거부합니다.
- **내 화면/업무에 영향**: 정상 엑셀 업로드는 그대로. **손상·위장 파일**을 올려도 내부 오류 대신 알기 쉬운 안내 문구가 표시됨
- **상태**: 완료

<details><summary>자세히</summary>

- BE: `BankDepositExcelParser` · `NhisExcelParser` · `StaffNhisCaregiverExcelParser` · `NhisVisitScheduleExcelParser` · `RfidTransmissionExcelParser` — POI `NotOfficeXmlFileException`(POIXMLException) 등 parse-time `IOException`/`RuntimeException`을 `BusinessRuleException("엑셀 파일을 읽을 수 없습니다.")` 로 변환, 파서 자체 검증 문구는 그대로 재전파 (`0a97b22`)
- 회귀: 파서·import-service 양 계층에서 corrupt-body 브랜치 고정
- 서명 검사(magic-byte, Q931~Q932) 통과 이후 단계의 방어 — 제품 정상 흐름 변화 없음

</details>

### ✅ 은행 입금 엑셀 — 브라우저 사전검증 추가 (FE, SEC-D34)
- **에이전트**: COD
- **한 일**: **`/billing/payments` 「은행 입금 엑셀 일괄 등록」** 에서 이전에는 서버(BE)만 파일 서명을 검사했는데, 이제 **업로드(미리보기) 버튼을 누르기 전에 브라우저가 먼저** 확장자·형식·서명·0바이트를 검사해 위장·손상·빈 파일을 즉시 막습니다. 첨부 허용 형식도 **`.xlsx` 전용**으로 좁혔습니다.
- **내 화면/업무에 영향**: **`/billing/payments`** — 정상 은행 xlsx는 그대로, 잘못된 파일은 API 호출 없이 화면에서 바로 안내
- **상태**: 완료

<details><summary>자세히</summary>

- FE: `BankDepositImportPanel.jsx` — `validateBankDepositExcelImportFile` 연결, accept `.xlsx` 로 축소 (`1f9d49c`)
- FE: `excelImportFiles.js` — 은행 입금 전용 xlsx-only 사전검증 규칙 추가 (BE `BankDepositImportService` OOXML-only lockstep)
- 회귀: `BankDepositImportPanel.test.jsx` · `excelImportFiles.test.js`

</details>

### ✅ 빈(0바이트)·빈 헤더 엑셀 업로드 거부 (FE·BE, SEC-D34)
- **에이전트**: COD
- **한 일**: 방문·요양보호사·청구 NHIS·은행 입금 엑셀 일괄 등록에서, **내용이 전혀 없는 0바이트 파일**과 **읽었을 때 헤더가 비어 있는 파일**도 항상 「업로드할 엑셀 파일이 필요합니다/없습니다」로 거부되도록 화면(FE)과 서버(BE) 양쪽에 방어를 넣고 **회귀 테스트로 고정**했습니다.
- **내 화면/업무에 영향**: 없음 — 정상 엑셀 업로드는 그대로. 빈 파일을 실수로 올려도 미리보기·등록 단계에서 안내 메시지로 즉시 막힘
- **상태**: 완료

<details><summary>자세히</summary>

- FE: `excelImportFiles.js` — FileReader가 빈 배열을 반환하는 경우까지 `EXCEL_IMPORT_REQUIRED_MESSAGE`로 fail-closed, 0바이트 사전 거부 회귀 테스트 추가 (`b23711f`, `2789553`)
- BE: `VisitServiceTest` · `StaffNhisCaregiverImportServiceTest` · `BankDepositImportServiceTest` · `NhisImportServiceTest` — 0바이트 및 `payload.length == 0` 방어(미리보기 경로 포함) 회귀 테스트 고정 (`9449e1f`)
- 제품 동작 변화 없음(빈 파일 방어·테스트 전용)

</details>

### ✅ 위장 엑셀(.xls·잘린 서명) 거부 회귀 테스트 보강 (BE, SEC-D34)
- **에이전트**: COD
- **한 일**: 방문·요양보호사 NHIS·은행 입금 엑셀 일괄 등록에서, 확장자만 `.xls`인 위장 파일과 **서명이 잘린(2바이트) 손상 파일**도 항상 「엑셀 파일 시그니처가 올바르지 않습니다.」로 거부되는지 **회귀 테스트로 고정**했습니다. 미리보기 단계까지 동일하게 막히도록 검증했습니다.
- **내 화면/업무에 영향**: 없음 — 정상 엑셀 업로드는 그대로. 위장·손상 파일에 대한 서버 방어가 테스트로 굳어짐
- **상태**: 완료

<details><summary>자세히</summary>

- BE: `VisitServiceTest` · `StaffNhisCaregiverImportServiceTest` — `.xls`(OLE) 위장·잘린 서명 fail-closed 브랜치 커버 (`2f3be17`)
- BE: `BankDepositImportServiceTest` — `payload.length < magic.length` 단락(importDeposits·previewDeposits) 커버 (`efbdbec`, QA-B604)
- 제품 동작 변화 없음(테스트 전용)

</details>

### ✅ form-data 개발용 보안 취약점 해소 (FE, QA-B606)
- **에이전트**: COD
- **한 일**: `npm audit`에서 보고된 `form-data`의 CRLF 인젝션 취약점(high)을 해소하기 위해 잠금 버전을 **4.0.5 → 4.0.6(패치)** 으로 올렸습니다. `npm audit` 결과가 **0건**이 되었습니다.
- **내 화면/업무에 영향**: 없음 — 테스트 환경(jsdom)에서만 쓰이는 개발용 의존성으로, 운영 번들에는 포함되지 않아 실사용 노출은 처음부터 없었습니다
- **상태**: 완료

<details><summary>자세히</summary>

- FE: `package-lock.json` — `form-data` 4.0.5→4.0.6, `jsdom@22.1.0` 경유 dev 전용 transitive 의존성 (`637bad8`)
- GHSA-hmw2-7cc7-3qxx · Vite 운영 번들 미포함

</details>

### ✅ 사진 업로드 성공을 스크린리더로 안내 (FE, UXD-191)
- **에이전트**: UXD
- **한 일**: 이용자 사진·프로그램 일정 활동 사진 업로드가 성공하면 화면에서는 **「미등록 → 등록됨」** 으로만 바뀌어 스크린리더 사용자에게 알림이 없었습니다. 이제 두 화면 모두 **소리 없는 상태 안내 영역(role="status")** 으로 등록 성공을 읽어줍니다.
- **내 화면/업무에 영향**: **`/clients/:id` 사진 · `/programs` 「활동 사진」** — 눈으로 보는 화면은 그대로, **스크린리더 사용자**는 업로드 성공을 소리로 확인 (표에 배너는 추가되지 않음)
- **상태**: 완료

<details><summary>자세히</summary>

- FE: `ClientPhotoUpload.jsx` · `ProgramSchedulePhotoUpload.jsx` — `ds-sr-only` `role="status"` polite live region (WCAG 4.1.3, `194823b`)
- 오류 안내는 기존 접근성 경로(Alert `role="alert"` · FileUpload `aria-invalid`)를 그대로 사용 (Q930)

</details>

### ✅ 엑셀 일괄 등록 — 빈(null) 파일 fail-closed 보강 (BE, SEC-D34)
- **에이전트**: COD
- **한 일**: 방문·청구 NHIS·요양보호사·은행 입금 4개 엑셀 import 경로에서 **내용이 비어 있는(null) 파일**이 들어와도 오류 없이 처리되던 경계 상황을 막아, 항상 「엑셀 파일 시그니처가 올바르지 않습니다.」로 **안전하게 거부(fail-closed)** 하도록 다졌습니다.
- **내 화면/업무에 영향**: 없음 — 정상 업로드는 그대로. 비정상(빈) 파일에 대한 서버 방어만 견고해짐
- **상태**: 완료

<details><summary>자세히</summary>

- BE: `NhisImportService` · `BankDepositImportService` · `VisitService` · `StaffNhisCaregiverImportService` — `payload == null` 가드 추가 (`f28e3d9`, QA-B604)
- FE 회귀 픽스처를 실제 OOXML 서명 바이트로 맞춰 사전검증 테스트가 API까지 도달하도록 정렬 (QA-B602·QA-B605, 제품 동작 변화 없음)

</details>

### ✅ 은행 입금 엑셀 — OOXML 서명 검증 (BE, SEC-D34)
- **에이전트**: COD
- **한 일**: **`/billing/payments`** 은행 입금 일괄등록 미리보기·등록 전에 **xlsx(OOXML) 파일 서명**을 서버에서 검사합니다. 확장자·Content-Type만 맞춘 위장 파일은 「엑셀 파일 시그니처가 올바르지 않습니다.」로 거부합니다.
- **내 화면/업무에 영향**: **`/billing/payments` 「은행 입금 엑셀 일괄 등록」** — 정상 은행 xlsx는 그대로, 위장·손상 파일은 미리보기 전에 거부
- **상태**: 완료

<details><summary>자세히</summary>

- BE: `BankDepositImportService` — OOXML `PK\x03\x04` only · `.xls` 미지원 (`f6e4d88`)
- 회귀: `BankDepositImportServiceTest`
- FE: 은행 입금은 **BE 검증만**(미리보기 API 호출 시) — Q932 참고

</details>

### ✅ 방문·청구 NHIS 엑셀 — 서버 서명 검증 확대 (BE, SEC-D34)
- **에이전트**: COD
- **한 일**: **공단 방문일정 import**와 **청구내역상세 NHIS import**에도 확장자·Content-Type(;param strip) + **OOXML/OLE magic-byte** 검사를 서버에 추가했습니다. 방문·요양보호사는 `.xlsx`|`.xls`, 청구는 **`.xlsx` only**입니다.
- **내 화면/업무에 영향**: **`/visits` 공단 방문일정 · `/billing/imports/nhis`** — MIME만 맞춘 가짜 엑셀은 업로드 API에서 거부
- **상태**: 완료

<details><summary>자세히</summary>

- BE: `VisitService` · `NhisImportService` (`a788e6d`) — `StaffNhisCaregiverImportService`와 lockstep
- 회귀: `VisitServiceTest` · `NhisImportServiceTest`
- 오류: 「엑셀 파일 시그니처가 올바르지 않습니다.」

</details>

### ✅ 공단 엑셀 import — 브라우저 사전 서명 검증 (FE, SEC-D34)
- **에이전트**: COD
- **한 일**: 방문일정·청구내역상세·요양보호사 엑셀 업로드 **전**에 브라우저에서 **파일 서명**을 검사합니다. BE와 **동일 오류 문구**로 API 호출 전에 거부합니다.
- **내 화면/업무에 영향**: **`/visits` 방문일정 · `/billing/imports/nhis` · `/staff` 요양보호사 엑셀 · RFID 비교 plan/rfid 파일** — 위장 파일은 즉시 거부, 정상 공단 엑셀은 그대로
- **상태**: 완료

<details><summary>자세히</summary>

- FE: `src/config/excelImportFiles.js` — `validateVisitNhisExcelImportFile` · `validateBillingNhisExcelImportFile` · `validateStaffNhisCaregiverExcelImportFile` (`3042a53`)
- 소비: `VisitNhisImportPanel` · `VisitRfidDiffComparePanel` · `NHISImportPage` · `StaffNhisCaregiverImportPanel`
- 회귀: `excelImportFiles.test.js`

</details>

---

## 2026-07-17

### 📝 업로드 magic-byte 확대·인쇄 a11y ops 문서화
- **에이전트**: TWR
- **한 일**: develop HEAD 실측 후 FAQ·매뉴얼·관리/배포 가이드에 **이용자 사진·급여계약·직원 HR·등급 이력·보수교육 이수증·공단 요양보호사 엑셀** 파일 서명 검증과 **직원현황 인쇄/활동 사진 오류 ARIA** 를 반영했습니다.
- **내 화면/업무에 영향**: 없음 — 운영·배포 가이드만 갱신
- **상태**: 완료

<details><summary>자세히</summary>

- 실측: BE develop `be64fda` · FE develop `8b164c3` — **133 route** · **106 page** · Flyway **V1–V196** · 모듈 **97.41%**
- FAQ·USER_MANUAL·ADMIN/DEPLOY·CHANGELOG·ops README 교차 갱신

</details>

### ✅ 공단 요양보호사 엑셀 — OOXML/OLE 서명 검증
- **에이전트**: COD
- **한 일**: `/staff` 공단 요양보호사 엑셀 업로드에서 확장자·Content-Type만 맞춘 위장 파일을 막기 위해, **xlsx(ZIP)·xls(OLE)** 파일 앞부분 서명을 서버에서 검사합니다. 불일치 시 「xlsx 또는 xls 형식의 엑셀 파일만…」으로 거부합니다.
- **내 화면/업무에 영향**: **`/staff` 「공단 요양보호사 엑셀」** — 정상 엑셀은 그대로, 위장·손상 파일은 미리보기 전에 거부
- **상태**: 완료

<details><summary>자세히</summary>

- BE: `StaffNhisCaregiverImportService` — OOXML `PK…` · OLE CFB magic · Content-Type 파라미터 strip (`be64fda`)
- 회귀: `StaffNhisCaregiverImportServiceTest`

</details>

### ✅ 등급 이력·보수교육 이수증 — 파일 서명 검증 (BE+FE)
- **에이전트**: COD
- **한 일**: 이용자 **등급 이력 첨부**와 직원 **보수교육 이수증**도 MIME 위장을 막기 위해 업로드 전·저장 전에 **PDF/PNG(또는 JPEG)** 서명을 BE·FE가 함께 검사합니다.
- **내 화면/업무에 영향**: **`/clients/:id` 「등급 이력」** · **`/staff/training` 이수증** — 확장자만 바꾼 파일은 거부, 정상 스캔본은 그대로
- **상태**: 완료

<details><summary>자세히</summary>

- BE: `LtcGradeHistoryAttachmentStorageService` · `StaffRefresherTrainingCertificateStorageService` (`ed94521`)
- FE: `gradeHistoryAttachments.js` · `staffRefresherTrainingCertificates.js` (`8b164c3`)
- 안내: 등급 이력 「PDF 또는 PNG…」 · 이수증 「PDF 또는 이미지(PNG/JPEG)…」

</details>

### ✅ 급여계약서·직원 HR 파일 — 파일 서명 검증 (BE+FE)
- **에이전트**: COD
- **한 일**: **급여계약서 파일함**과 **직원 HR 서류함** 업로드에도 PDF/이미지 서명 검사를 넣었습니다. Content-Type 파라미터는 strip 후 비교합니다.
- **내 화면/업무에 영향**: **`/clients/:id` 「급여계약」** · **직원 상세 「HR 파일함」** — MIME만 맞춘 가짜 파일 거부
- **상태**: 완료

<details><summary>자세히</summary>

- BE: `BenefitContractAttachmentStorageService` · `StaffHrFileStorageService` (`324da07`)
- FE: `benefitContractAttachments.js` · `staffHrFiles.js` (`cf28a2e`)
- 급여계약: PDF/PNG · HR: PDF/PNG/JPEG · ≤10MB

</details>

### ✅ 이용자 프로필 사진 — 파일 서명 검증 (BE+FE)
- **에이전트**: COD
- **한 일**: 이용자 상세 **프로필 사진**도 프로그램 활동 사진과 같이 JPEG/PNG/WEBP **파일 서명**을 브라우저·서버에서 이중 검사합니다.
- **내 화면/업무에 영향**: **`/clients/:id` 프로필 사진** — 위장 파일은 「JPEG, PNG, WEBP 형식의 이미지만…」으로 거부
- **상태**: 완료

<details><summary>자세히</summary>

- BE: `ClientPhotoStorageService` (`cdba083`)
- FE: `ClientPhotoUpload` · `clientPhotos.js` (`e16f432`)
- 프로그램 활동 사진과 lockstep (동일 magic family)

</details>

### ✅ 직원현황 인쇄·활동 사진 오류 ARIA
- **에이전트**: UXD
- **한 일**: 직원현황 리포트 **조회 필터**가 인쇄물에 나오지 않도록 화면 전용으로 바꾸고, 활동 사진 업로드 오류를 **aria-invalid·aria-describedby**로 파일 입력과 연결했습니다.
- **내 화면/업무에 영향**: **`/staff/status-report` 인쇄** — 필터 카드 미출력 · **`/programs` 활동 사진** — 오류 시 스크린리더가 안내 문구를 읽음
- **상태**: 완료

<details><summary>자세히</summary>

- FE: `StaffStatusReportPage` screen-only filter · `ProgramSchedulePhotoUpload` ARIA (`b2eb059`)

</details>

### 📝 활동 사진 magic-byte·NoBreakSpace mid-token ops 문서화
- **에이전트**: TWR
- **한 일**: develop HEAD 실측 후 FAQ·매뉴얼·관리/배포 가이드에 **프로그램 활동 사진 magic-byte 검증(SEC-D25)** · **`&NoBreakSpace;` mid-token strip BE+FE lockstep** · baseline **`c19bfa6`/`dc81f6e`** 를 반영했습니다.
- **내 화면/업무에 영향**: 없음 — 운영·배포 가이드만 갱신
- **상태**: 완료

<details><summary>자세히</summary>

- 실측: BE develop `c19bfa6` · FE develop `dc81f6e` — **133 route** · **106 page** · Flyway **V1–V196** · 모듈 **97.41%**
- FAQ Q924·Q925 신규 · Q882·Q917·Q920 교차 갱신 · USER_MANUAL §5-9 · ADMIN/DEPLOY §1-3·§1-4 · CHANGELOG·ops README

</details>

### ✅ 프로그램 활동 사진 — 파일 서명(magic-byte) 검증 (BE+FE)
- **에이전트**: COD
- **한 일**: Content-Type만 JPEG/PNG/WEBP로 위장한 파일을 막기 위해, 업로드 전·저장 전에 **파일 앞부분 서명**이 MIME과 일치하는지 BE·FE가 함께 검사합니다. 불일치 시 동일 안내 문구로 거부합니다.
- **내 화면/업무에 영향**: **`/programs` 「활동 사진」** — 확장자·MIME만 맞추고 **실제 내용이 이미지가 아닌 파일**은 「JPEG, PNG, WEBP 형식의 프로그램 사진만…」으로 거부. 정상 사진은 그대로 업로드
- **상태**: 완료

<details><summary>자세히</summary>

- BE: `ProgramPhotoStorageService` — JPEG `FF D8 FF` · PNG `89 50 4E 47…` · WEBP `RIFF….WEBP` (`d1ff63a`)
- FE: `validateProgramSchedulePhotoFile` async magic-byte (`8e28fe0`) — BE lockstep
- 오류 문구 BE/FE 동일: 「JPEG, PNG, WEBP 형식의 프로그램 사진만 업로드할 수 있습니다.」
- 회귀: `ProgramPhotoStorageServiceTest` · `programsPhoto.test.js`

</details>

### ✅ live E2E — mid-token `&NoBreakSpace;` strip lockstep (BE+FE)
- **에이전트**: COD
- **한 일**: 게이트웨이가 **`guardian&NoBreakSpace;-bootstrap`** 처럼 토큰 한가운데에 legacy `&NoBreakSpace;`를 넣어도, BE·FE가 **공백이 아니라 빈 문자열로 제거**해 `guardian-bootstrap` 마커가 다시 붙도록 맞췄습니다.
- **내 화면/업무에 영향**: 없음 — **IT·QA** live E2E·operation gate·알림 패널 blocker 표시만
- **상태**: 완료

<details><summary>자세히</summary>

- BE: `LiveE2eOperationReadinessSupport` — `&nobreakspace` → `""` (`63227d7`) · 세미콜론 생략 회귀 lock (`c19bfa6`) · 이전 공백 치환에서 strip으로 정정
- FE: channel-status·live harness mid-token strip + 테스트 lock (`090ac10`)
- Q882 후속 — BE·FE 모두 strip(empty)로 통일

</details>

### 📝 M12 SSO 경로 allowlist·대문자 `&NUM` ops 문서화
- **에이전트**: TWR
- **한 일**: develop HEAD 실측 후 FAQ·매뉴얼·관리/배포 가이드에 **M12 SSO `/carefor_login` 경로 allowlist BE+FE lockstep** · **대문자 세미콜론 생략 `&NUM` decode 테스트 lock** · baseline **`a742788`/`bc1d343`** 를 반영했습니다.
- **내 화면/업무에 영향**: 없음 — 운영·배포 가이드만 갱신
- **상태**: 완료

<details><summary>자세히</summary>

- 실측: BE develop `a742788` · FE develop `bc1d343` — **133 route** · **107 page** · Flyway **V1–V196** · 모듈 **97.41%**
- FAQ Q922·Q923 신규 · Q787·Q801·Q919 교차 갱신 · USER_MANUAL §4-6-5 · ADMIN/DEPLOY §1-3·§1-4 · CHANGELOG·ops README

</details>

### ✅ M12 재무회계 SSO — `/carefor_login` 경로 allowlist (BE+FE)
- **에이전트**: COD
- **한 일**: SSO OTP handoff가 **수지파인 HTTPS 호스트의 `/carefor_login` 경로**로만 POST되도록 BE·FE를 강화했습니다. 쿼리·프래그먼트·비표준 포트·userinfo가 있는 URL은 거부하고, 오류 문구에 **허용 경로**를 명시합니다.
- **내 화면/업무에 영향**: **`/accounting` SSO** — 잘못된 포털 URL env 설정 시 **「/carefor_login 경로만」** 안내와 함께 SSO 버튼 숨김(기존과 동일, 검증·문구 강화)
- **상태**: 완료

<details><summary>자세히</summary>

- BE: `AccountingBpoSupport.isAllowlistedPortalUrl` — host·path·443·query/fragment/userinfo 검증 (`bfe6b3f`/`a742788`)
- FE: `isAllowlistedAccountingBpoSsoPortalUrl` — BE lockstep (`592a483`)
- 허용: `https://sujifine.co.kr/carefor_login` · `https://www.sujifine.co.kr/carefor_login`
- 회귀: `AccountingBpoServiceTest` · `accountingBpo.test.js`

</details>

### ✅ live E2E — 대문자 세미콜론 생략 `&NUM` decode 테스트 lock (FE)
- **에이전트**: COD
- **한 일**: **`&NUM45`** 처럼 대문자 named-num 뒤 세미콜론이 없어도 channel-status decode가 `#`로 전개하는 동작을 **notificationChannelStatus 테스트**에 추가해 live harness와 경로 간 회귀 격차를 닫았습니다. 디코드 로직 변경 없음.
- **내 화면/업무에 영향**: 없음 — **IT·QA** live E2E·operation gate만
- **상태**: 완료

<details><summary>자세히</summary>

- FE: `notificationChannelStatus.test.js` — uppercase semicolon-optional `&NUM` (`bc1d343`)
- Q919·Q855와 lockstep — four live-readiness decode paths byte-identical

</details>

### 📝 활동 사진 간격·`&num` BE+FE lock ops 문서화
- **에이전트**: TWR
- **한 일**: develop HEAD 실측 후 FAQ·매뉴얼·관리/배포 가이드에 **프로그램 활동 사진 업로드 세로 간격** · **세미콜론 생략 `&num` BE·liveConfig lockstep** · baseline **`759b15e`/`9e40c19`** 를 반영했습니다.
- **내 화면/업무에 영향**: 없음 — 운영·배포 가이드만 갱신
- **상태**: 완료

<details><summary>자세히</summary>

- 실측: BE develop `759b15e` · FE develop `9e40c19` — **133 route** · **107 page** · Flyway **V1–V196** · 모듈 **97.41%**
- FAQ Q921 신규 · Q919 BE+FE 교차 갱신 · USER_MANUAL §5-9 · ADMIN/DEPLOY §1-3·§1-4 · CHANGELOG·ops README

</details>

### ✅ 프로그램 활동 사진 — 업로드 세로 간격 (FE)
- **에이전트**: UXD
- **한 일**: 프로그램 일정 **활동 사진** 업로드 칸이 쓰던 **밀착 세로 스택** 스타일(`ds-stack--tight`)을 디자인 시스템에 정식으로 넣었습니다. 상태 라벨·파일 선택·버튼·오류 안내가 서로 붙지 않고 읽히게 됩니다.
- **내 화면/업무에 영향**: **`/programs` 「활동 사진」** — 업로드 칸 간격이 정상적으로 벌어짐
- **상태**: 완료

<details><summary>자세히</summary>

- FE: `components.css` §113 — `.ds-stack--tight` (gap `space-2`) · `ProgramSchedulePhotoUpload` 소비 (`bfd171d`)
- 형제: `ds-stack`(space-6) · `ds-stack--sm`(space-3)

</details>

### ✅ live E2E — 세미콜론 생략 `&num` BE·liveConfig lockstep (BE+FE)
- **에이전트**: COD
- **한 일**: 게이트웨이가 **`&num45`** 처럼 named-num 뒤 세미콜론 없이 숫자를 이어 붙여도, BE readiness와 FE liveConfig·globalSetup이 channel-status와 동일하게 `#`로 전개한 뒤 fail-closed로 맞춥니다.
- **내 화면/업무에 영향**: 없음 — **IT·QA** live E2E·operation gate·알림 패널 blocker 표시만
- **상태**: 완료

<details><summary>자세히</summary>

- BE: `LiveE2eOperationReadinessSupport` — `&num` optional `;` at token boundary (`759b15e`)
- FE: `liveConfig.js` · `liveGlobalSetup.js` — channel-status/`ce2325c` lockstep (`9e40c19`)
- 회귀: `LiveE2eOperationReadinessSupportTest` · `liveE2eHarness.test.js`

</details>

### 📝 프로그램 활동 사진 Content-Type·baseline ops 문서화
- **에이전트**: TWR
- **한 일**: develop HEAD 실측 후 FAQ·매뉴얼·관리/배포 가이드에 **프로그램 활동 사진 Content-Type 파라미터 정규화** · baseline **`72a6534`/`8e74b07`** · **107 page** KPI를 반영했습니다.
- **내 화면/업무에 영향**: 없음 — 운영·배포 가이드만 갱신
- **상태**: 완료

<details><summary>자세히</summary>

- 실측: BE develop `72a6534` · FE develop `8e74b07` — **133 route** · **107 page** · Flyway **V1–V196** · 모듈 **97.41%**
- FAQ Q920 신규 · Q917 교차 갱신 · USER_MANUAL §5-9 · ADMIN/DEPLOY §1-3·§1-4 · CHANGELOG·ops README

</details>

### ✅ 프로그램 일정 활동 사진 — Content-Type 파라미터 정규화 (BE+FE)
- **에이전트**: COD
- **한 일**: 일부 브라우저·모바일이 **`image/jpeg; charset=binary`** 처럼 Content-Type 뒤에 파라미터를 붙여 보내도, **`;` 이후를 제거**한 뒤 JPEG·PNG·WEBP를 판별하도록 BE·FE를 맞췄습니다.
- **내 화면/업무에 영향**: **`/programs`** 활동 사진 업로드 — 이전에 「형식 오류」로 거부되던 **정상 JPEG·PNG·WEBP**가 올라갈 수 있음
- **상태**: 완료

<details><summary>자세히</summary>

- BE: `ProgramPhotoStorageService.normalizeContentType` · `ProgramPhotoStorageServiceTest` (`72a6534`)
- FE: `normalizeProgramSchedulePhotoContentType` · `programsPhoto.test.js` (`8e74b07`)
- Q917 multipart 업로드와 lockstep — media type만 비교

</details>

### 📝 프로그램 활동 사진·V196 probe·세미콜론 생략 num ops 문서화
- **에이전트**: TWR
- **한 일**: develop HEAD 실측 후 FAQ·매뉴얼·관리/배포 가이드에 **프로그램 일정 활동 사진 업로드** · **live probe V196 연계 무결성 플래그** · **세미콜론 생략 `&num` named-num** 을 반영했습니다.
- **내 화면/업무에 영향**: 없음 — 운영·배포 가이드만 갱신
- **상태**: 완료

<details><summary>자세히</summary>

- 실측: BE develop `1b8c764` · FE develop `2e06d5a` — **133 route** · **106 page** · Flyway **V1–V196** · 모듈 **97.41%**
- FAQ Q917~Q919 신규 · Q855·Q827·Q161 교차 갱신 · USER_MANUAL §5-9 · ADMIN/DEPLOY §1-3·§1-4 · CHANGELOG·ops README

</details>

### ✅ 프로그램 일정 — 활동 사진 업로드 (BE+FE)
- **에이전트**: COD
- **한 일**: 당일 프로그램 일정 행에 **활동 증거 사진**을 올릴 수 있게 했습니다. JPEG·PNG·WEBP(최대 5MB)만 허용하며, 본사·센터장·사회복지사·요양보호사가 업로드할 수 있습니다.
- **내 화면/업무에 영향**: **`/programs`** 일정 표 **「활동 사진」** 열 — **등록됨/미등록** 표시와 파일 선택 업로드
- **상태**: 완료

<details><summary>자세히</summary>

- BE: `POST /api/v1/programs/schedule/{programId}/photo` multipart `file` · `ProgramPhotoStorageService` · `photoStorageKey` (`1b8c764`)
- FE: `ProgramSchedulePhotoUpload` · `uploadProgramSchedulePhotoApi` · ProgramsPage 「활동 사진」 (`2e06d5a`)
- 저장 경로 기본값: `ogada.storage.program-photos.storage-dir=./data/program-photos`
- 역할: `hq_admin` · `branch_admin` · `social_worker` · `caregiver`

</details>

### ✅ live E2E — V196 연계기록 무결성 probe 노출 (BE)
- **에이전트**: COD
- **한 일**: live E2E probe 응답에 **연계기록지 V196 무결성 준비 플래그**를 넣어 health·operation gate와 스키마를 맞췄습니다.
- **내 화면/업무에 영향**: 없음 — **IT·QA** live E2E·operation gate만
- **상태**: 완료

<details><summary>자세히</summary>

- BE: `GET /api/v1/system/live-e2e/probe` — `v196ClientLinkageRecordsIntegrityCheckReady` (`b7f4337`)
- health의 동일 플래그·blocker `v196-client-linkage-records-integrity-missing` 과 lockstep
- 회귀: `LiveE2eControllerTest`

</details>

### ✅ live E2E — 세미콜론 생략 `&num` named-num (FE)
- **에이전트**: COD
- **한 일**: 게이트웨이가 **`&num` 뒤 세미콜론 없이** 숫자 entity를 이어 붙여도 channel-status·live harness가 `#`로 정규화한 뒤 fail-closed로 디코드하도록 FE를 보강했습니다.
- **내 화면/업무에 영향**: 없음 — **IT·QA** live E2E·operation gate·알림 패널 blocker 표시만
- **상태**: 완료

<details><summary>자세히</summary>

- FE: `notificationChannelStatus.js` · `liveBackendProbe.js` — `&num` optional `;` at token boundary (`ce2325c`)
- 회귀: `notificationChannelStatus.test.js` · `liveE2eHarness.test.js`

</details>

### 📝 blank blocker FE·세미콜론 생략 amp·core quote BE lock ops 문서화
- **에이전트**: TWR
- **한 일**: develop HEAD 실측 후 FAQ·매뉴얼·관리/배포 가이드에 **blank operation blocker FE lockstep** · **세미콜론 생략 `&amp`** · **core quote/angle BE 회귀 lock** 을 반영했습니다.
- **내 화면/업무에 영향**: 없음 — 운영·배포 가이드만 갱신
- **상태**: 완료

<details><summary>자세히</summary>

- 실측: BE develop `7389ef0` · FE develop `d3e282b` — **133 route** · **106 page** · Flyway **V1–V196** · 모듈 **97.41%**
- FAQ Q916 신규 · Q911·Q912 BE+FE 교차 갱신 · USER_MANUAL/ADMIN/DEPLOY §1-3·§1-4 · CHANGELOG·ops README

</details>

### ✅ live E2E — 세미콜론 생략 `&amp` entity (FE)
- **에이전트**: COD
- **한 일**: 게이트웨이가 **`bootstrap&amp#45-disabled`** 처럼 **`&amp` 뒤 세미콜론(`;`) 없이** numeric entity를 이어도 channel-status·live harness가 BE와 동일하게 fail-closed로 디코드하도록 FE를 보강했습니다.
- **내 화면/업무에 영향**: 없음 — **IT·QA** live E2E·operation gate·알림 패널 blocker 표시만
- **상태**: 완료

<details><summary>자세히</summary>

- FE: `notificationChannelStatus.js` · `liveBackendProbe.js` · `liveConfig.js` · `liveGlobalSetup.js` — `&amp` optional `;` at token boundary, **numeric decode 전에** 처리 (`d3e282b`)
- 회귀: `notificationChannelStatus.test.js` · `liveE2eHarness.test.js`

</details>

### ✅ live E2E — blank operation blocker 목록 FE lockstep (FE)
- **에이전트**: COD
- **한 일**: live readiness helper가 **effective·suppressed bootstrap blocker 목록**에서 **null·공백 토큰을 제거**하도록 BE `@0dfc992` 와 맞췄습니다. `liveGlobalSetup`이 동일 helper를 재사용합니다.
- **내 화면/업무에 영향**: 없음 — **IT·QA** live E2E·operation gate·health blocker 표시만
- **상태**: 완료

<details><summary>자세히</summary>

- FE: `liveBackendProbe.js` — `resolveEffectiveOperationBlockers` · `resolveSuppressedBootstrapOperationBlockers` (`9a48e13`)
- FE: `liveGlobalSetup.js` — helper 재사용 wire
- 회귀: `liveE2eHarness.test.js`

</details>

### ✅ live E2E — core quote/angle 세미콜론 생략 BE 회귀 lock (BE)
- **에이전트**: COD
- **한 일**: **`&quot`/`&apos`/`&lt`/`&gt`** 세미콜론 생략 디코드에 대한 **BE 회귀 테스트**를 추가해 FE `@20f6ddc` lockstep을 고정했습니다(Q911 후속).
- **내 화면/업무에 영향**: 없음 — **IT·QA** live E2E·operation gate만
- **상태**: 완료

<details><summary>자세히</summary>

- BE: `LiveE2eOperationReadinessSupportTest` — semicolon-optional core quote/angle cases (`7389ef0`)
- BE: `LiveE2eOperationReadinessSupport` — javadoc lockstep note only

</details>

### 📝 blank blocker·대장 scope·UXD-188·청구 이력 ops 문서화
- **에이전트**: TWR
- **한 일**: develop HEAD 실측 후 FAQ·매뉴얼·관리/배포 가이드에 **blank operation blocker 필터(Q912)** · **연차·유급휴일 대장 empty 지점 scope(Q913)** · **UXD-188 ds-* 레이아웃 12종(Q914)** · **청구 상태 이력 타임스탬프(Q915)** 를 반영했습니다.
- **내 화면/업무에 영향**: 없음 — 운영·배포 가이드만 갱신
- **상태**: 완료

<details><summary>자세히</summary>

- 실측: BE develop `0dfc992` · FE develop `420286e` — **133 route** · **106 page** · Flyway **V1–V196** · 모듈 **97.41%**
- FAQ Q912~Q915 신규 · Q894·Q674·Q906 교차 갱신 · USER_MANUAL/ADMIN/DEPLOY §1-3·§1-4 · CHANGELOG·ops README

</details>

### ✅ live E2E — blank operation blocker 목록 정리 (BE)
- **에이전트**: COD
- **한 일**: readiness helper가 **effective·bootstrap operation blocker 목록**에서도 **null·공백 토큰을 제거**하도록 보강했습니다(Q894 primary skip의 후속).
- **내 화면/업무에 영향**: 없음 — **IT·QA** live E2E·operation gate·health blocker 표시만
- **상태**: 완료

<details><summary>자세히</summary>

- BE: `LiveE2eOperationReadinessSupport` — `resolveEffectiveOperationBlockers` · `resolveBootstrapOperationBlockers` (`0dfc992`)
- 회귀: `LiveE2eOperationReadinessSupportTest`

</details>

### ✅ 연차·유급휴일 대장 — empty 응답 지점 scope (BE)
- **에이전트**: COD
- **한 일**: **대장 행이 0건**인 직원 조회에서 **비-HQ** 호출자에게 **권한 밖 지점**이 노출되던 문제를 막았습니다. 호출자 read scope 내 지점만 반환합니다.
- **내 화면/업무에 영향**: **`/staff/leave-ledger`** 직원별 조회·**BranchScopeNotice** 지점명이 **내 지점과 일치**하게 표시
- **상태**: 완료

<details><summary>자세히</summary>

- BE: `StaffLeaveLedgerService.listForUser` — `resolveReadableBranchIdForUser` (`f6023b0`)
- 회귀: `StaffLeaveLedgerServiceTest`
- API: `GET /api/v1/staff/leave-ledger/users/{userId}?year=`

</details>

### ✅ Must ds-* 레이아웃 12종·청구 이력 시각 a11y (FE)
- **에이전트**: UXD
- **한 일**: 간호·요양 등록 Card·QR 체크인·HR 파일·청구 대장·송영 준수 등에 쓰이던 **레이아웃 `ds-*` 12종**을 CSS에 정식 정의하고, 청구 상세 **상태 변경 이력**에 **`time[dateTime]`** 을 적용했습니다(UXD-188).
- **내 화면/업무에 영향**: **간호·요양 기록 등록**·**보호자 QR 체크인**·**직원 서류·보수교육**·**청구 상세 상태 이력** 레이아웃·시각 표시 개선
- **상태**: 완료

<details><summary>자세히</summary>

- FE: `components.css` §112 — `ds-card--form`·`ds-timeline--compact`·`ds-qr-scan`·`ds-lifecycle__*`·`ds-staff-hr-files`·`ds-benefit-contract-files`·`ds-staff-refresher-certificates`·`ds-billing-report__section-header`·`ds-transport-compliance__workflow` 등 (`c061494`)
- FE: `BillingDetailPage` — `ClaimStatusTimeline` (`c061494`)

</details>

### ✅ 청구 상세 — 상태 이력 타임스탬프 가드 (FE)
- **에이전트**: COD
- **한 일**: **`changedAt` 누락·파싱 불가**일 때 청구 상세 **상태 변경 이력**에 **깨진 날짜 대신 「—」** 를 표시하도록 보강했습니다.
- **내 화면/업무에 영향**: **`/billing/claims/:id`** 상태 이력 — 잘못된 API 시각 데이터에도 **읽기 가능한 타임라인** 유지
- **상태**: 완료

<details><summary>자세히</summary>

- FE: `BillingDetailPage.jsx` — `ClaimStatusTimeline` invalid `changedAt` guard (`420286e`)
- 회귀: `BillingDetailPage.test.jsx`

</details>

### 📝 확장 prime·세미콜론 생략 quote ops 문서화
- **에이전트**: TWR
- **한 일**: develop HEAD 실측 후 FAQ·매뉴얼·관리/배포 가이드에 **live E2E 확장 prime(`&bprime;`/`&tprime;`/`&qprime;`/`&backprime;`)** 와 **세미콜론 생략 core quote/angle(`&quot`/`&apos`/`&lt`/`&gt`)** 디코드를 반영했습니다.
- **내 화면/업무에 영향**: 없음 — 운영·배포 가이드만 갱신
- **상태**: 완료

<details><summary>자세히</summary>

- 실측: BE develop `29e20dd` · FE develop `20f6ddc` — **133 route** · **106 page** · Flyway **V1–V196** · 모듈 **97.41%**
- FAQ Q910·Q911 신규 · Q909·Q840 교차 갱신 · USER_MANUAL/ADMIN/DEPLOY §1-3·§1-4 · CHANGELOG·ops README

</details>

### ✅ live E2E — 세미콜론 생략 core quote/angle entity (FE)
- **에이전트**: COD
- **한 일**: 게이트웨이가 **`&quot`/`&apos`/`&lt`/`&gt`** 처럼 **세미콜론 없이** 인용·꺾쇠 entity를 끊어도 channel-status·live harness unwrap가 fail-closed로 맞도록 FE 디코드를 보강했습니다(Q840 numeric 세미콜론 생략의 named 확장).
- **내 화면/업무에 영향**: 없음 — **IT·QA** live E2E·operation gate·알림 패널 blocker 표시만
- **상태**: 완료

<details><summary>자세히</summary>

- FE: `notificationChannelStatus.js` · `liveBackendProbe.js` · `liveConfig.js` · `liveGlobalSetup.js` — quot/apos/lt/gt optional `;` (`20f6ddc`)
- 회귀: `notificationChannelStatus.test.js` · `liveE2eHarness.test.js`

</details>

### ✅ live E2E — 확장 prime(bprime/tprime/qprime/backprime) HTML entity 디코드 (BE+FE)
- **에이전트**: COD
- **한 일**: 게이트웨이가 인용문 래퍼를 HTML5 **`&bprime;`/`&tprime;`/`&qprime;`/`&backprime;`** 로 인코딩해도 unwrap가 fail-closed로 맞도록 BE·FE 디코드를 추가했습니다(Q909 Triple/Double/Prime 뒤에 처리·짧은 `&Prime;`/`&prime;`보다 먼저).
- **내 화면/업무에 영향**: 없음 — **IT·QA** live E2E·operation gate만
- **상태**: 완료

<details><summary>자세히</summary>

- BE: `LiveE2eOperationReadinessSupport` — bprime/qprime→`"` · tprime/backprime→`'` (`31b10d5`) · 회귀 테스트 분리 (`29e20dd`)
- FE: `notificationChannelStatus.js` · live harness — BE parity (`93f77e1`)
- 회귀: `LiveE2eOperationReadinessSupportTest` · `notificationChannelStatus.test.js` · `liveE2eHarness.test.js`

</details>

### 📝 prime/double-prime 인용문 ops 문서화
- **에이전트**: TWR
- **한 일**: develop HEAD 실측 후 FAQ·매뉴얼·관리/배포 가이드에 **live E2E prime/double-prime(`&Prime;`/`&prime;`/`&DoublePrime;`/`&TriplePrime;`) 인용문 디코드**를 반영했습니다.
- **내 화면/업무에 영향**: 없음 — 운영·배포 가이드만 갱신
- **상태**: 완료

<details><summary>자세히</summary>

- 실측: BE develop `34c16cd` · FE develop `3f7bb94` — **133 route** · **106 page** · Flyway **V1–V196** · 모듈 **97.41%**
- FAQ Q909 신규 · Q905·Q908 교차 갱신 · USER_MANUAL/ADMIN/DEPLOY §1-3·§1-4 · CHANGELOG·ops README

</details>

### ✅ live E2E — prime/double-prime 인용문 HTML entity 디코드 (BE+FE)
- **에이전트**: COD
- **한 일**: 게이트웨이가 인용문 래퍼를 **`&TriplePrime;`/`&DoublePrime;`/`&Prime;`/`&prime;`** 로 인코딩해도 unwrap가 fail-closed로 맞도록 BE·FE 디코드를 추가했습니다(guillemet 뒤·짧은 ldquo 앞; `Prime`/`prime` 대소문자 구분).
- **내 화면/업무에 영향**: 없음 — **IT·QA** live E2E·operation gate만
- **상태**: 완료

<details><summary>자세히</summary>

- BE: `LiveE2eOperationReadinessSupport` — Triple/Double/Prime/prime → ASCII quote (`34c16cd`)
- FE: `notificationChannelStatus.js` · live harness — BE parity (`3f7bb94`)
- 회귀: `LiveE2eOperationReadinessSupportTest` · `notificationChannelStatus.test.js` · `liveE2eHarness.test.js`

</details>

### 📝 guillemet·low-9 인용문·Left*/Right* FE lockstep ops 문서화
- **에이전트**: TWR
- **한 일**: develop HEAD 실측 후 FAQ·매뉴얼·관리/배포 가이드에 **live E2E guillemet(`&laquo;`/`&lsaquo;`)·low-9/reversed-9(`&bdquo;`/`&ldquor;`) 인용문 디코드**와 **Left*/Right*Quote FE lockstep 완료**를 반영했습니다.
- **내 화면/업무에 영향**: 없음 — 운영·배포 가이드만 갱신
- **상태**: 완료

<details><summary>자세히</summary>

- 실측: BE develop `3b0b6b9` · FE develop `a280437` — **133 route** · **106 page** · Flyway **V1–V196** · 모듈 **97.41%**
- FAQ Q905 갱신 · Q907~Q908 신규 · USER_MANUAL/ADMIN/DEPLOY §1-3·§1-4 · CHANGELOG·ops README

</details>

### ✅ live E2E — guillemet/single-angle 인용문 HTML entity 디코드 (BE+FE)
- **에이전트**: COD
- **한 일**: 게이트웨이가 인용문 래퍼를 **`&laquo;`/`&raquo;`/`&lsaquo;`/`&rsaquo;`** 로 인코딩해도 unwrap가 fail-closed로 맞도록 BE·FE 디코드를 추가했습니다(low-9/reversed-9·짧은 ldquo 뒤에 처리).
- **내 화면/업무에 영향**: 없음 — **IT·QA** live E2E·operation gate만
- **상태**: 완료

<details><summary>자세히</summary>

- BE: `LiveE2eOperationReadinessSupport` — laquo/raquo/lsaquo/rsaquo → ASCII quote (`3b0b6b9`)
- FE: `notificationChannelStatus.js` · live harness — BE parity (`a280437`)
- 회귀: `LiveE2eOperationReadinessSupportTest` · `notificationChannelStatus.test.js` · `liveE2eHarness.test.js`

</details>

### ✅ live E2E — low-9/reversed-9 인용문 HTML entity 디코드 (BE+FE)
- **에이전트**: COD
- **한 일**: 게이트웨이가 인용문 래퍼를 **`&ldquor;`/`&rdquor;`/`&bdquo;`/`&lsquor;`/`&rsquor;`/`&sbquo;`** 로 인코딩해도 unwrap가 fail-closed로 맞도록 BE·FE 디코드를 추가했습니다(`*or` long form을 짧은 `&ldquo;`/`&lsquo;`보다 먼저 처리).
- **내 화면/업무에 영향**: 없음 — **IT·QA** live E2E·operation gate만
- **상태**: 완료

<details><summary>자세히</summary>

- BE: `LiveE2eOperationReadinessSupport` — ldquor/rdquor/bdquo/lsquor/rsquor/sbquo → ASCII quote (`23ce552`)
- FE: `notificationChannelStatus.js` · live harness — BE parity (`56fa1c0`)
- 회귀: `LiveE2eOperationReadinessSupportTest` · `notificationChannelStatus.test.js` · `liveE2eHarness.test.js`

</details>

### ✅ live E2E — Left*/Right*Quote FE lockstep (FE)
- **에이전트**: COD
- **한 일**: channel-status·live harness에 HTML5 **`&LeftDoubleQuote;`/`&RightDoubleQuote;`/`&LeftSingleQuote;`/`&RightSingleQuote;`** 디코드를 BE와 맞춰 Q905 잔여 FE lockstep을 완료했습니다.
- **내 화면/업무에 영향**: 없음 — **IT·QA** live E2E·operation gate만
- **상태**: 완료

<details><summary>자세히</summary>

- FE: `notificationChannelStatus.js` · `liveBackendProbe.js` · `liveConfig.js` · `liveGlobalSetup.js` — Left*/Right* → OpenCurly* → ldquo 순 (`694266e`)
- BE: Q905에서 이미 처리 (`a9bd7c0`)
- 회귀: `notificationChannelStatus.test.js` · `liveE2eHarness.test.js`

</details>

### 📝 인용문 HTML entity·ds-* 9종 ops 문서화
- **에이전트**: TWR
- **한 일**: develop HEAD 실측 후 FAQ·매뉴얼·관리/배포 가이드에 **live E2E 인용문(typographic)·OpenCurly*·Left*/Right*Quote** 디코드와 **Must 화면 ds-* 텍스트·동의·브레드크럼 9종 정식화**를 반영했습니다.
- **내 화면/업무에 영향**: 없음 — 운영·배포 가이드만 갱신(화면 체감은 아래 UXD·COD 카드)
- **상태**: 완료

<details><summary>자세히</summary>

- 실측: BE develop `a9bd7c0` · FE develop `0438a17` — **133 route** · **106 page** · Flyway **V1–V196** · 모듈 **~97.4%**
- FAQ Q903~Q906 · USER_MANUAL/ADMIN/DEPLOY §1-3·§1-4 · CHANGELOG·ops README

</details>

### ✅ 이용자 등록·보호자·배차 화면 — 텍스트·동의·브레드크럼 ds-* 9종 정식화
- **에이전트**: UXD
- **한 일**: 화면에 쓰이지만 CSS에 없던 **텍스트·간격·그룹 클래스 9종**을 `components.css`에 올려, 주민번호 수집 동의 묶음·필드 라벨·페이지 브레드크럼·제출 블록·배차 지도 힌트 등이 디자인 시스템대로 보이게 했습니다.
- **내 화면/업무에 영향**: **이용자 등록·수정**(`/clients/new`·`/clients/:id/edit`) 주민번호 동의 박스·라벨, **보호자 체크인** 제출 버튼 간격, **배차 지도** 경로 갱신 힌트, 상세 화면 상단 브레드크럼 여백이 정리됩니다. 업무 기능·API는 그대로입니다.
- **상태**: 완료

<details><summary>자세히</summary>

- FE: `components.css` — `ds-text-strong` · `ds-card__lede` · `ds-table__meta` · `ds-field-label`/`ds-field__label` · `ds-consent-box`(forced-colors 경계) · `ds-page-breadcrumb` · `ds-submit-block` · `ds-transport-map__refresh-hint` (`0438a17`, UXD-187)
- 적용 예: `ClientFormPage` · `GuardianCheckinPage` · `KakaoTransportMap` · `AccountingBpoPage` · `BodyRestraintRecordPage`

</details>

### ✅ live E2E — Left*/Right*Quote HTML entity 디코드 (BE+FE)
- **에이전트**: COD
- **한 일**: 게이트웨이가 인용문 래퍼를 HTML5 **`&LeftDoubleQuote;`/`&RightDoubleQuote;`/`&LeftSingleQuote;`/`&RightSingleQuote;`** 로 인코딩해도 unwrap가 fail-closed로 맞도록 BE·FE 디코드를 맞췄습니다(OpenCurly*·짧은 ldquo보다 먼저 처리).
- **내 화면/업무에 영향**: 없음 — **IT·QA** live E2E·operation gate만
- **상태**: 완료

<details><summary>자세히</summary>

- BE: `LiveE2eOperationReadinessSupport` — Left*/Right*Quote → ASCII `"`/`'` then OpenCurly* then ldquo (`a9bd7c0`)
- FE: `notificationChannelStatus.js` · live harness — BE parity (`694266e`)
- 회귀: `LiveE2eOperationReadinessSupportTest` · `notificationChannelStatus.test.js` · `liveE2eHarness.test.js`

</details>

### ✅ live E2E — OpenCurly* 인용문 long alias 디코드 (BE+FE)
- **에이전트**: COD
- **한 일**: 게이트웨이가 인용문 래퍼를 HTML5 **`&OpenCurlyDoubleQuote;`/`&CloseCurlyDoubleQuote;`/`&OpenCurlyQuote;`/`&CloseCurlyQuote;`** 로 인코딩해도 unwrap가 fail-closed로 맞도록 BE·FE 디코드를 맞췄습니다(짧은 `&ldquo;`/`&rdquo;`보다 긴 alias 우선).
- **내 화면/업무에 영향**: 없음 — **IT·QA** live E2E·operation gate만
- **상태**: 완료

<details><summary>자세히</summary>

- BE: `LiveE2eOperationReadinessSupport` — Open/CloseCurly* → ASCII quote (`df2c1a0`)
- FE: `notificationChannelStatus.js` · live harness — BE parity (`ac3af73`)
- 회귀: `LiveE2eOperationReadinessSupportTest` · `notificationChannelStatus.test.js` · `liveE2eHarness.test.js`

</details>

### ✅ live E2E — typographic 인용문(`&ldquo;` 등) 디코드 (BE+FE)
- **에이전트**: COD
- **한 일**: 게이트웨이가 blocker를 **`&ldquo;`/`&rdquo;`/`&lsquo;`/`&rsquo;`**(및 유니코드 굽은 따옴표)로 감싸도 ASCII 따옴표로 풀어 bootstrap gate가 fail-closed로 동작하도록 BE·FE를 맞췄습니다.
- **내 화면/업무에 영향**: 없음 — **IT·QA** live E2E·operation gate만
- **상태**: 완료

<details><summary>자세히</summary>

- BE: `LiveE2eOperationReadinessSupport` — ldquo/rdquo/lsquo/rsquo → `"`/`'` (`a0c1fe6`)
- FE: `notificationChannelStatus.js` · live harness — BE parity (`a364f97`)
- 회귀: `LiveE2eOperationReadinessSupportTest` · `notificationChannelStatus.test.js` · `liveE2eHarness.test.js`

</details>

### 📝 UXD design system §110 — QA-B95 배치 + ds-* 26종 정식화 문서화
- **에이전트**: UXD · TWR
- **한 일**: PLN 224차 baseline(FE @d6be05c) 기준으로 **QA-B95 6-commit decode 배치 확인** 및 **components.css 내 26개 미정의 ds-* 클래스 승격 내역과 a11y 결정 사항**을 DESIGN_SYSTEM.md §110에 문서화했습니다.
- **내 화면/업무에 영향**: 없음 — 디자인 시스템 문서만 갱신
- **상태**: 완료

<details><summary>자세히</summary>

- DESIGN_SYSTEM.md: §110 추가(107줄) — ds-stack--sm·ds-table--compact·ds-form-grid--3·ds-billing-ledger-table·ds-fee-matrix·ds-cms-collection-status·ds-nursing-*·ds-staff-lifecycle-panel·ds-address-fields·ds-date-picker 등 적용 패턴
- 앞선 UXD-186/FE-16 정규화 FE 커밋 @971c636 확인

</details>

### 📝 MathML 꺾쇠·bidi live harness ops 문서화
- **에이전트**: TWR
- **한 일**: develop HEAD 실측 후 FAQ·매뉴얼·관리/배포 가이드에 **live E2E MathML 꺾쇠 long alias(`&LeftAngleBracket;`/`&RightAngleBracket;`)** 와 **bidi long-alias의 live harness 경로 보강**을 반영했습니다.
- **내 화면/업무에 영향**: 없음 — 운영·배포 가이드만 갱신
- **상태**: 완료

<details><summary>자세히</summary>

- 실측: BE develop `c1041bb` · FE develop `40c85df` — **133 route** · **106 page** · Flyway **V1–V196** · 모듈 **~97.4%**
- FAQ Q901·Q902 신규 · Q900·Q879 교차 갱신 · USER_MANUAL/ADMIN/DEPLOY §1-3·§1-4 · CHANGELOG·ops README

</details>

### ✅ live E2E — MathML 꺾쇠 long alias 디코드 (BE+FE)
- **에이전트**: COD
- **한 일**: 게이트웨이가 꺾쇠 래퍼를 MathML **`&LeftAngleBracket;`/`&RightAngleBracket;`** 로 인코딩해도 unwrap가 fail-closed로 맞도록 BE·FE 디코드를 추가했습니다(짧은 `&lang;`/`&langle;`보다 긴 alias를 먼저 처리).
- **내 화면/업무에 영향**: 없음 — **IT·QA** live E2E·operation gate만
- **상태**: 완료

<details><summary>자세히</summary>

- BE: `LiveE2eOperationReadinessSupport` — Left/RightAngleBracket → `<`/`>` then langle/rangle then lang/rang (`c1041bb`)
- FE: `notificationChannelStatus.js` · live harness — BE parity (`40c85df`)
- 회귀: `LiveE2eOperationReadinessSupportTest` · `notificationChannelStatus.test.js` · `liveE2eHarness.test.js`

</details>

### ✅ live E2E — bidi long-alias를 live harness 경로에 전파 (FE)
- **에이전트**: COD
- **한 일**: channel-status에 있던 HTML5 **bidi long-alias** strip을 live-e2e probe·config·globalSetup에도 맞춰, 게이트웨이 mid-token 분리가 end-to-end로 fail-closed 되도록 했습니다.
- **내 화면/업무에 영향**: 없음 — **IT·QA** live E2E harness만
- **상태**: 완료

<details><summary>자세히</summary>

- FE: `liveBackendProbe.js` · `liveConfig.js` · `liveGlobalSetup.js` — LeftToRight*/RightToLeft*/PopDirectional*/FirstStrongIsolate long aliases (`5ce4726`)
- 회귀: `liveE2eHarness.test.js`

</details>

### 📝 꺾쇠·소괄호 wrapping BE lockstep ops 문서화
- **에이전트**: TWR
- **한 일**: develop HEAD 실측 후 FAQ·매뉴얼·관리/배포 가이드에 **live E2E 꺾쇠(angle) wrapping(`&lang;`/`&rang;`/`&langle;`/`&rangle;`)** 과 **소괄호 wrapping BE lockstep 완료**를 반영했습니다.
- **내 화면/업무에 영향**: 없음 — 운영·배포 가이드만 갱신
- **상태**: 완료

<details><summary>자세히</summary>

- 실측: BE develop `20356ed` · FE develop `1c84f0f` — **133 route** · **106 page** · Flyway **V1–V196** · 모듈 **~97.4%**
- FAQ Q898 갱신·Q900 신규 · USER_MANUAL/ADMIN/DEPLOY §1-3·§1-4 · CHANGELOG·ops README

</details>

### ✅ live E2E — 꺾쇠(angle) wrapping HTML entity 디코드 (BE+FE)
- **에이전트**: COD
- **한 일**: 게이트웨이가 blocker 목록의 **`<`/`>`** 래퍼를 **`&lang;`/`&rang;`/`&langle;`/`&rangle;`** 로 인코딩해도 unwrap가 fail-closed로 맞도록 BE·FE 디코드를 추가했습니다(긴 alias를 짧은 alias보다 먼저 처리).
- **내 화면/업무에 영향**: 없음 — **IT·QA** live E2E·operation gate만
- **상태**: 완료

<details><summary>자세히</summary>

- BE: `LiveE2eOperationReadinessSupport` — langle/rangle → `<`/`>` then lang/rang (`20356ed`)
- FE: `notificationChannelStatus.js` · live harness — BE parity (`1c84f0f`)
- 회귀: `LiveE2eOperationReadinessSupportTest` · `notificationChannelStatus.test.js` · `liveE2eHarness.test.js`

</details>

### ✅ live E2E — 소괄호 wrapping HTML entity BE lockstep
- **에이전트**: COD
- **한 일**: FE에 이어 백엔드 readiness도 **`&lpar;`/`&rpar;`** → `(`/`)` 디코드를 맞춰, health/probe만으로도 소괄호 wrapping이 fail-closed로 동작합니다.
- **내 화면/업무에 영향**: 없음 — **IT·QA** live E2E·operation gate만
- **상태**: 완료

<details><summary>자세히</summary>

- BE: `LiveE2eOperationReadinessSupport` — lpar/rpar → `(`/`)` (`bc41ed9`)
- 회귀: `LiveE2eOperationReadinessSupportTest`

</details>

### 📝 중괄호·소괄호 wrapping·ds-* 26종 ops 문서화
- **에이전트**: TWR
- **한 일**: develop HEAD 실측 후 FAQ·매뉴얼·관리/배포 가이드에 **live E2E 중괄호·소괄호 wrapping HTML entity**와 **청구·간호·CMS·수가·직원 lifecycle 등 Must 화면 ds-* 클래스 26종 정식화**를 반영했습니다.
- **내 화면/업무에 영향**: 없음 — 운영·배포 가이드만 갱신(ds-* 정식화 체감은 아래 UXD 카드)
- **상태**: 완료

<details><summary>자세히</summary>

- 실측: BE develop `794bfed` · FE develop `9907725` — **133 route** · **106 page** · Flyway **V1–V196** · 모듈 **~97.4%**
- FAQ 신규 항목 · USER_MANUAL/ADMIN/DEPLOY §1-3·§1-4 · CHANGELOG·ops README

</details>

### ✅ live E2E — 소괄호 wrapping HTML entity 디코드 (FE)
- **에이전트**: COD
- **한 일**: 게이트웨이가 blocker 목록의 **`(`/`)`** 래퍼를 **`&lpar;`/`&rpar;`** 로 인코딩해도 unwrap가 fail-closed로 맞도록 FE channel-status·live harness 디코드를 추가했습니다.
- **내 화면/업무에 영향**: 없음 — **IT·QA** live E2E·operation gate만 (BE lockstep은 위 카드)
- **상태**: 완료

<details><summary>자세히</summary>

- FE: `notificationChannelStatus.js` · live harness — lpar/rpar → `(`/`)` (`9907725`)
- 회귀: `notificationChannelStatus.test.js` · `liveE2eHarness.test.js`

</details>

### ✅ 청구·간호·CMS 등 — 미정의 ds-* 클래스 26종 정식화 (FE)
- **에이전트**: UXD
- **한 일**: 청구 대장·수가 매트릭스·CMS·간호 기록·직원 lifecycle·주소·달력 등 Must 화면에서 쓰이던 **미정의 `ds-*` 클래스 26종**을 `components.css`에 올려 레이아웃·고대비·상태 색이 깨지지 않게 했습니다.
- **내 화면/업무에 영향**: **센터 직원·통합 관리자** — 청구 대장·수가·CMS·간호 활력/구강/응급·직원 휴직 패널·테마 토글 등에서 **간격·표·폼 그리드·배지**가 디자인 시스템대로 표시(기능 변경 없음)
- **상태**: 완료

<details><summary>자세히</summary>

- FE: `components.css` +236줄 — `ds-stack--sm`·`ds-table--compact`·`ds-form-grid--3`·`ds-billing-ledger-table`·`ds-fee-matrix`·`ds-cms-collection-status`·`ds-nursing-*-form__intro`·`ds-staff-lifecycle-panel__*` 등 (`971c636`, UXD-186 / FE-16)
- 적용 화면 예: `BillingLedgerTable`·`FeeScheduleMatrix`·`CmsCollectionPanel`·`NursingVitalCheckForm`·`StaffLifecyclePanel`·`KoreanAddressFields`

</details>

### ✅ live E2E — 중괄호 wrapping HTML entity 디코드 (BE+FE)
- **에이전트**: COD
- **한 일**: 게이트웨이가 blocker 목록의 **`{`/`}`** 래퍼를 **`&lbrace;`/`&rbrace;`/`&lcub;`/`&rcub;`** 로 인코딩해도 unwrap·JSON 객체 파싱이 fail-closed로 맞도록 BE·FE 디코드를 추가했습니다.
- **내 화면/업무에 영향**: 없음 — **IT·QA** live E2E·operation gate만
- **상태**: 완료

<details><summary>자세히</summary>

- BE: `LiveE2eOperationReadinessSupport` — lbrace/rbrace/lcub/rcub → `{`/`}` (`794bfed`)
- FE: `notificationChannelStatus.js` · live harness — BE parity (`d6be05c`)
- 회귀: `LiveE2eOperationReadinessSupportTest` · `notificationChannelStatus.test.js` · `liveE2eHarness.test.js`

</details>

### 📝 semi·blank·대괄호 entity·카카오 필수 6종 live 점검 ops 문서화
- **에이전트**: TWR
- **한 일**: develop HEAD 실측 후 FAQ·매뉴얼·관리/배포 가이드에 **live E2E `&semi;`·빈 토큰 무시·대괄호 wrapping entity(`&lbrack;`/`&rbrack;`/`&lsqb;`/`&rsqb`)(BE+FE)** 와 **카카오 필수 알림톡 6종 live 전 운영 점검(Must)** 을 반영했습니다.
- **내 화면/업무에 영향**: 없음 — 운영·배포 가이드만 갱신(카카오 live 전 체크리스트는 IT·센터장 readiness 참고)
- **상태**: 완료

<details><summary>자세히</summary>

- 실측: BE develop `c6ddf6c` · FE develop `6fceb8d` — **133 route** · **106 page** · Flyway **V1–V196** · 모듈 **~97.4%**
- FAQ Q893~Q896 신규 · USER_MANUAL/ADMIN/DEPLOY §1-4 · CHANGELOG·ops README

</details>

### ✅ live E2E — 대괄호 wrapping HTML entity 디코드 (BE+FE)
- **에이전트**: COD
- **한 일**: 게이트웨이가 blocker 목록의 **`[`/`]`** 래퍼를 **`&lbrack;`/`&rbrack;`/`&lsqb;`/`&rsqb;`** 로 인코딩해도 unwrap·JSON 배열 파싱이 fail-closed로 맞도록 BE·FE 디코드를 추가했습니다.
- **내 화면/업무에 영향**: 없음 — **IT·QA** live E2E·operation gate만
- **상태**: 완료

<details><summary>자세히</summary>

- BE: `LiveE2eOperationReadinessSupport` — lbrack/rbrack/lsqb/rsqb → `[`/`]` (`c6ddf6c`)
- FE: `notificationChannelStatus.js` · live harness — BE parity (`6fceb8d`)
- 회귀: `LiveE2eOperationReadinessSupportTest` · `notificationChannelStatus.test.js` · `liveE2eHarness.test.js`

</details>

---

## 2026-07-16

### ✅ live E2E — 빈 blocker 토큰 무시 (BE+FE)
- **에이전트**: COD
- **한 일**: 운영 readiness가 **null·공백만 있는 blocker 항목**을 건너뛰고, 실제 primary 토큰(또는 없음)을 고르도록 BE·FE를 맞췄습니다.
- **내 화면/업무에 영향**: 없음 — **IT·QA** live E2E·operation gate만
- **상태**: 완료

<details><summary>자세히</summary>

- BE: `LiveE2eOperationReadinessSupport` — blank skip (`b348258`)
- FE: `liveBackendProbe.js` — `resolvePrimaryOperationBlocker` blank skip (`7ee1cf1`)
- 회귀: `LiveE2eOperationReadinessSupportTest` · `liveE2eHarness.test.js`

</details>

### ✅ live E2E — semi HTML entity 디코드 (BE+FE)
- **에이전트**: COD
- **한 일**: 게이트웨이가 세미콜론 구분자를 **`&semi;`** 로 인코딩해도 fail-closed bootstrap marker를 추출하도록 BE·FE 디코드를 맞췄습니다 (`&comma;` 와 쌍).
- **내 화면/업무에 영향**: 없음 — **IT·QA** live E2E·operation gate만
- **상태**: 완료

<details><summary>자세히</summary>

- BE: `LiveE2eOperationReadinessSupport` — `&semi;` → `;` (`d247cdf`)
- FE: channel-status·live harness — BE parity (`6900a8f`)
- 회귀: `LiveE2eOperationReadinessSupportTest` · `notificationChannelStatus.test.js` · `liveE2eHarness.test.js`

</details>

### 📝 VeryThickSpace·comma entity·템플릿 카탈로그 행 헤더 ops 문서화
- **에이전트**: TWR
- **한 일**: develop HEAD 실측 후 FAQ·매뉴얼·관리/배포 가이드에 **live E2E `&VeryThickSpace;`·`&comma;` HTML entity 디코드(BE+FE)** 와 **템플릿 카탈로그 메시지 열 행 헤더 a11y(UXD-185)** 를 반영했습니다.
- **내 화면/업무에 영향**: 없음 — 운영·배포 가이드만 갱신
- **상태**: 완료

<details><summary>자세히</summary>

- 실측: BE develop `45e1f00` · FE develop `b753586` — **133 route** · **106 page** · Flyway **V1–V196** · 모듈 **~97.4%**
- FAQ Q890~Q892 신규 · USER_MANUAL/ADMIN/DEPLOY §1-4 · CHANGELOG·ops README

</details>

### ✅ live E2E — comma HTML entity 디코드 (BE+FE)
- **에이전트**: COD
- **한 일**: 게이트웨이가 blocker 목록 구분자를 **`&comma;`** 로 인코딩해도 fail-closed bootstrap marker를 추출하도록 BE·FE 디코드를 맞췄습니다.
- **내 화면/업무에 영향**: 없음 — **IT·QA** live E2E·operation gate만
- **상태**: 완료

<details><summary>자세히</summary>

- BE: `LiveE2eOperationReadinessSupport` — `&comma;` → `,` (`45e1f00`)
- FE: `notificationChannelStatus.js` · live harness — BE parity (`b753586`)
- 회귀: `LiveE2eOperationReadinessSupportTest` · `notificationChannelStatus.test.js` · `liveE2eHarness.test.js`

</details>

### ✅ live E2E — VeryThickSpace HTML entity alias 디코드 (BE+FE)
- **에이전트**: COD
- **한 일**: **`&VeryThickSpace;`** MathML space alias를 공백으로 정규화해 Thin→Thick→VeryThick→VeryVery* space ladder의 fail-closed gate를 맞췄습니다.
- **내 화면/업무에 영향**: 없음 — **IT·QA** live E2E·operation gate만
- **상태**: 완료

<details><summary>자세히</summary>

- BE: `LiveE2eOperationReadinessSupport` — VeryThickSpace → 공백 (`043f002`)
- FE: channel-status·live harness — BE parity (`b28eb45`)
- 회귀: `LiveE2eOperationReadinessSupportTest` · `notificationChannelStatus.test.js` · `liveE2eHarness.test.js`

</details>

### ✅ 템플릿 카탈로그 — 메시지 열 행 헤더 a11y (FE)
- **에이전트**: UXD
- **한 일**: **「알림톡·SMS 템플릿 카탈로그」** 13종 표에서 **메시지명** 열을 **`<th scope="row">`** 로 승격해 스크린리더가 각 행의 상태 셀 맥락을 읽을 수 있게 했습니다.
- **내 화면/업무에 영향**: **통합 관리자·센터장** — **조직 설정·대시보드** readiness 패널 **13종 표** 스크린리더·키보드 탐색 개선(시각 변화 없음)
- **상태**: 완료

<details><summary>자세히</summary>

- FE: `NotificationChannelReadinessPanel.jsx` — 메시지 열 `td` → `th scope="row"` (`d3b0f1c`, UXD-185)
- 참고 단가 표(UXD-181)와 동일 WCAG 1.3.1 패턴 · `NotificationChannelReadinessPanel.test.jsx` 회귀

</details>

### 📝 카카오 필수 알림톡 6종·카탈로그 13종 ops 문서화
- **에이전트**: TWR
- **한 일**: develop HEAD 실측 후 FAQ·매뉴얼·관리/배포 가이드에 **템플릿 카탈로그 13종**(이지케어 message_kind 7 + 카카오 필수 알림톡 6·kind 없음 「—」)과 readiness 패널 표기 변경을 반영했습니다.
- **내 화면/업무에 영향**: 없음 — 운영·배포 가이드만 갱신
- **상태**: 완료

<details><summary>자세히</summary>

- 실측: BE develop `54fd8dd` · FE develop `ab9e853` — **133 route** · **106 page** · Flyway **V1–V196** · 모듈 **~97.4%**
- FAQ Q889 신규 · Q686·USER_MANUAL/ADMIN/DEPLOY §1-4 카탈로그 건수 정정 · CHANGELOG·ops README

</details>

### ✅ 알림톡·SMS 템플릿 카탈로그 — 카카오 필수 6종 표시 (BE+FE)
- **에이전트**: COD
- **한 일**: 조직 설정·대시보드 readiness 패널의 템플릿 카탈로그에 **출석(입소/귀가)·일일 케어 요약·입금 확인·가정통신문·긴급 알림** 등 카카오 필수 알림톡 6종을 추가했습니다. 이지케어 kind가 없는 항목은 **「—」** 로 표시됩니다.
- **내 화면/업무에 영향**: **통합 관리자·센터장** — **조직 설정·대시보드** 「알림톡·SMS 템플릿 카탈로그」에서 **13종** 매핑·발송 준비 상태를 한눈에 확인
- **상태**: 완료

<details><summary>자세히</summary>

- BE: `GET /api/v1/notifications/template-catalog` — `totalCount`/`dispatchImplementedCount` **13** · `ezcareMessageKind` nullable (`54fd8dd`)
- FE: `NotificationChannelReadinessPanel` 제목 **「알림톡·SMS 템플릿 카탈로그」** · `formatEzcareMessageKind` · `KAKAO_REQUIRED_TEMPLATE_CODES` (`ab9e853`)
- 6종: `ATTENDANCE_ARRIVAL` · `ATTENDANCE_DEPARTURE` · `DAILY_CARE_SUMMARY` · `BILLING_PAYMENT_RECEIVED` · `HOME_NEWSLETTER` · `EMERGENCY_ALERT`

</details>

### 📝 VeryVery*·MathSpace·SixPerEm·figure space·연계 a11y ops 문서화
- **에이전트**: TWR
- **한 일**: develop HEAD 실측 후 FAQ·매뉴얼·관리/배포 가이드에 **figure/punctuation/ideographic·fractional em·SixPerEm·MathSpace·WordJoiner·VeryVery* space alias decode(BE+FE)** · **연계기록지 초안 안내·발송 체크박스 a11y** 를 반영했습니다.
- **내 화면/업무에 영향**: 없음 — 운영·배포 가이드만 갱신
- **상태**: 완료

<details><summary>자세히</summary>

- 실측: BE develop `f491ec8` · FE develop `3f7db38` — **133 route** · **106 page** · Flyway **V1–V196** · 모듈 **~97.4%**
- FAQ Q883~Q888 신규 · USER_MANUAL/ADMIN/DEPLOY §1-4 · CHANGELOG·ops README

</details>

### ✅ 연계기록지·발송 패널 — 체크박스·안내 문구 a11y (FE)
- **에이전트**: UXD
- **한 일**: 연계기록지 **「초안 없음」** 안내에 정의되지 않은 스타일을 **`ds-text-muted`** 로 바꾸고, RFID·명세서 발송 패널에 **`ds-checkbox-group`** 세로 묶음 스타일을 추가했습니다.
- **내 화면/업무에 영향**: **사회복지사·센터장** — 연계기록지 탭 **초안 없음 안내 가독성** · 발송 대상 **체크박스 세로 정렬·터치 영역** 개선
- **상태**: 완료

<details><summary>자세히</summary>

- FE: `ClientLinkageRecordsPanel.jsx` — `ds-muted` → `ds-text-muted` · `components.css` — `.ds-checkbox-group` (`ed48077`, UXD-184)
- 적용: `VisitRfidDiffComparePanel` · `BillingStatementDispatchPanel` 체크박스 묶음

</details>

### ✅ live E2E — VeryVery* space entity alias 디코드 (BE+FE)
- **에이전트**: COD
- **한 일**: 게이트웨이가 **`&VeryVeryThinSpace;`·`&VeryVeryThickSpace;`** 로 bootstrap 토큰을 쪼개도 fail-closed로 인식하도록 BE·FE 디코드를 맞췄습니다.
- **내 화면/업무에 영향**: 없음 — **IT·QA** live E2E·operation gate만
- **상태**: 완료

<details><summary>자세히</summary>

- BE: `LiveE2eOperationReadinessSupport` — VeryVeryThinSpace/VeryVeryThickSpace → 공백 (`f491ec8`)
- FE: `notificationChannelStatus.js` · `liveBackendProbe.js` · `liveConfig.js` · `liveGlobalSetup.js` — BE parity (`3f7db38`)
- 회귀: `LiveE2eOperationReadinessSupportTest` · `notificationChannelStatus.test.js` · `liveE2eHarness.test.js`

</details>

### ✅ live E2E — MathSpace·WordJoiner long alias 디코드 (BE+FE)
- **에이전트**: COD
- **한 일**: **`&MathSpace;`** 계열 MathML space와 **`&WordJoiner;`** long alias가 토큰 중간에 끼어도 bootstrap blocker를 추출하도록 BE·FE를 보강했습니다.
- **내 화면/업무에 영향**: 없음 — **IT·QA** live E2E·operation gate만
- **상태**: 완료

<details><summary>자세히</summary>

- BE: `LiveE2eOperationReadinessSupport` — MathSpace family → 공백 · WordJoiner strip (`6014cca`)
- FE: channel-status·live harness — BE parity (`73169a1`)
- 회귀: `LiveE2eOperationReadinessSupportTest` · `notificationChannelStatus.test.js` · `liveE2eHarness.test.js`

</details>

### ✅ live E2E — SixPerEm·EnSpace·EmSpace long alias 디코드 (BE+FE)
- **에이전트**: COD
- **한 일**: **`&emsp6;`·`&SixPerEmSpace;`·`&EnSpace;`·`&EmSpace;`·`&HairSpace;`·`&NarrowNoBreakSpace;`** 등 long alias가 섞여도 fail-closed로 인식하도록 BE·FE 디코드를 맞췄습니다.
- **내 화면/업무에 영향**: 없음 — **IT·QA** live E2E·operation gate만
- **상태**: 완료

<details><summary>자세히</summary>

- BE: `LiveE2eOperationReadinessSupport` — SixPerEm·EnSpace·EmSpace·HairSpace·NarrowNoBreakSpace (`4622896`)
- FE: channel-status·live harness — BE parity (`c260baa`)
- 회귀: `LiveE2eOperationReadinessSupportTest` · `notificationChannelStatus.test.js` · `liveE2eHarness.test.js`

</details>

### ✅ live E2E — fractional em space entity alias 디코드 (BE+FE)
- **에이전트**: COD
- **한 일**: **`&emsp2;`~`&emsp5;`·`&TwoPerEmSpace;`~`&FivePerEmSpace;`** 등 fractional em space alias를 공백으로 정규화해 bootstrap gate를 맞췄습니다.
- **내 화면/업무에 영향**: 없음 — **IT·QA** live E2E·operation gate만
- **상태**: 완료

<details><summary>자세히</summary>

- BE: `LiveE2eOperationReadinessSupport` — emsp2~5·TwoPerEm~FivePerEm → 공백 (`e4123c3`)
- FE: channel-status·live harness — BE parity (`73aa6dd`)
- 회귀: `LiveE2eOperationReadinessSupportTest` · `notificationChannelStatus.test.js` · `liveE2eHarness.test.js`

</details>

### ✅ live E2E — figure/punctuation/ideographic space alias 디코드 (BE+FE)
- **에이전트**: COD
- **한 일**: **`&figsp;`·`&FigureSpace;`·`&PunctuationSpace;`·`&IdeographicSpace;`** named alias를 공백으로 정규화해 bootstrap blocker를 추출하도록 BE·FE를 맞췄습니다.
- **내 화면/업무에 영향**: 없음 — **IT·QA** live E2E·operation gate만
- **상태**: 완료

<details><summary>자세히</summary>

- BE: `LiveE2eOperationReadinessSupport` — figsp/FigureSpace/PunctuationSpace/IdeographicSpace → 공백 (`08cdb87`)
- FE: channel-status·live harness — BE parity (`031abef`)
- 회귀: `LiveE2eOperationReadinessSupportTest` · `notificationChannelStatus.test.js` · `liveE2eHarness.test.js`

</details>

### ✅ live E2E — NoBreakSpace legacy alias 디코드 (BE+FE)
- **에이전트**: COD
- **한 일**: 게이트웨이가 비표준 **`&NoBreakSpace;`**(legacy NBSP alias)로 bootstrap detail을 감싸도, BE는 **`&nbsp;`·`&NonBreakingSpace;`와 같이 공백으로**, FE는 **strip**한 뒤 fail-closed로 인식하도록 BE·FE lockstep을 맞췄습니다.
- **내 화면/업무에 영향**: 없음 — **IT·QA** live E2E·operation gate만
- **상태**: 완료

<details><summary>자세히</summary>

- BE: `LiveE2eOperationReadinessSupport` — `&NoBreakSpace;`/`&nobreakspace` → 공백 (`ff80f0b`)
- FE: `notificationChannelStatus.js` · `liveBackendProbe.js` · `liveConfig.js` · `liveGlobalSetup.js` — `&nobreakspace` strip (`8a05640`)
- 회귀: `LiveE2eOperationReadinessSupportTest` · `notificationChannelStatus.test.js` · `liveE2eHarness.test.js`
- Q872(`&NoBreak;`·`&ZeroWidthNoBreakSpace;`)와 구분 — 이번 변경은 **legacy long-form `&NoBreakSpace;`** 전용

</details>

### 📝 NoBreakSpace legacy alias ops 문서화
- **에이전트**: TWR
- **한 일**: develop HEAD 실측 후 FAQ·매뉴얼·관리/배포 가이드에 **NoBreakSpace legacy alias decode(BE+FE lockstep)** 을 반영했습니다.
- **내 화면/업무에 영향**: 없음 — 운영·배포 가이드만 갱신
- **상태**: 완료

<details><summary>자세히</summary>

- 실측: BE develop `ff80f0b` · FE develop `8a05640` — **133 route** · **106 page** · Flyway **V1–V196** · 모듈 **~97.4%**
- FAQ Q882 신규 · USER_MANUAL/ADMIN/DEPLOY §1-4 · CHANGELOG·ops README

</details>

### ✅ live E2E — ZeroWidthNonJoiner/Joiner long alias 디코드 (BE+FE)
- **에이전트**: COD
- **한 일**: 게이트웨이가 **`&ZeroWidthNonJoiner;`·`&ZeroWidthJoiner;`** 긴 이름 alias로 bootstrap 토큰을 쪼개도, 짧은 **`&zwnj;`·`&zwj;`** 와 같이 제거한 뒤 fail-closed로 인식하도록 BE·FE를 맞췄습니다.
- **내 화면/업무에 영향**: 없음 — **IT·QA** live E2E·operation gate만
- **상태**: 완료

<details><summary>자세히</summary>

- BE: `LiveE2eOperationReadinessSupport` — ZeroWidthNonJoiner/Joiner strip (`ba5b0cb`)
- FE: `notificationChannelStatus.js` · `liveBackendProbe.js` · `liveConfig.js` · `liveGlobalSetup.js` — BE parity (`61f8f19`)
- 회귀: `LiveE2eOperationReadinessSupportTest` · `notificationChannelStatus.test.js` · `liveE2eHarness.test.js`

</details>

### ✅ live E2E — bidi long-form HTML entity alias 디코드 (BE+FE)
- **에이전트**: COD
- **한 일**: **`&LeftToRightEmbedding;`·`&RightToLeftIsolate;`·`&LeftToRightMark;`** 등 HTML5 **긴 이름 bidi alias**가 short form(`&lre;`·`&lri;`·`&lrm;`…)과 같이 섞여도 bootstrap blocker를 추출하도록 BE·FE 디코드를 보강했습니다.
- **내 화면/업무에 영향**: 없음 — **IT·QA** live E2E·operation gate만
- **상태**: 완료

<details><summary>자세히</summary>

- BE: `LiveE2eOperationReadinessSupport` — LeftToRight*/RightToLeft*/FirstStrong*/PopDirectional* long aliases strip (`53efa0b`)
- FE: `notificationChannelStatus.js` — BE parity (`975aecb`)
- 회귀: `LiveE2eOperationReadinessSupportTest` · `notificationChannelStatus.test.js`

</details>

### 📝 bidi/zero-width long alias · Must 소통 채널 구분 ops 문서화
- **에이전트**: TWR
- **한 일**: develop HEAD 실측 후 FAQ·매뉴얼·관리/배포 가이드에 **bidi long-form alias · ZeroWidthNonJoiner/Joiner long alias(BE+FE)** 와 **기관 공지·가정통신문·연계기록지 구분(Must)** 을 반영했습니다.
- **내 화면/업무에 영향**: 없음 — 운영·배포 가이드만 갱신
- **상태**: 완료

<details><summary>자세히</summary>

- 실측: BE develop `ba5b0cb` · FE develop `61f8f19` — **133 route** · **106 page** · Flyway **V1–V196** · 모듈 **~97.4%**
- FAQ Q879·Q880·Q881 신규 · USER_MANUAL/ADMIN/DEPLOY §1-4 · CHANGELOG·ops README

</details>

### ✅ live E2E — bidi embedding/isolate·NonBreakingSpace 디코드 (BE+FE)
- **에이전트**: COD
- **한 일**: 게이트웨이가 **`&lre;`·`&rle;`·`&lri;`·`&fsi;`** 같은 **HTML5 bidi embedding/isolate** 또는 **`&NonBreakingSpace;`**(MathML NBSP alias)로 bootstrap detail을 감싸도 fail-closed로 인식하도록 BE·FE 디코드를 맞췄습니다.
- **내 화면/업무에 영향**: 없음 — **IT·QA** live E2E·operation gate만
- **상태**: 완료

<details><summary>자세히</summary>

- BE: `LiveE2eOperationReadinessSupport` — bidi LRE/RLE/LRO/RLO/LRI/RLI/FSI/PDI/PDF strip · `&NonBreakingSpace;` → 공백 (`d911983`)
- FE: `notificationChannelStatus.js` · `liveBackendProbe.js` · `liveConfig.js` · `liveGlobalSetup.js` — BE parity (`29fc34f`)
- 회귀: `LiveE2eOperationReadinessSupportTest` · `notificationChannelStatus.test.js` · `liveE2eHarness.test.js`

</details>

### ✅ live E2E — bidi marks·MathML Positive*Space 디코드 (BE+FE)
- **에이전트**: COD
- **한 일**: **`&lrm;`·`&rlm;`** bidi mark 또는 **`&PositiveThinSpace;`·`&PositiveMediumSpace;`·`&PositiveThickSpace;`·`&PositiveVeryThinSpace;`·`&NegativeVeryThinSpace;`** MathML space alias가 토큰 중간에 끼어도 bootstrap blocker를 추출하도록 BE·FE를 보강했습니다.
- **내 화면/업무에 영향**: 없음 — **IT·QA** live E2E·operation gate만
- **상태**: 완료

<details><summary>자세히</summary>

- BE: `LiveE2eOperationReadinessSupport` — LRM/RLM strip · Positive*Space → 공백 · NegativeVeryThinSpace strip (`0a8a635`)
- FE: `notificationChannelStatus.js` · `liveBackendProbe.js` · `liveConfig.js` · `liveGlobalSetup.js` — BE parity (`039cd88`)
- 회귀: `LiveE2eOperationReadinessSupportTest` · `notificationChannelStatus.test.js` · `liveE2eHarness.test.js`

</details>

### ✅ live E2E — ThickSpace·MathML invisible operator 디코드 (BE+FE)
- **에이전트**: COD
- **한 일**: **`&ThickSpace;`** alias와 **`&InvisibleTimes;`·`&ApplyFunction;`·`&af;`·`&it;`** 등 **MathML invisible operator**가 bootstrap 마커를 쪼개도 fail-closed로 인식하도록 BE·FE 디코드를 맞췄습니다.
- **내 화면/업무에 영향**: 없음 — **IT·QA** live E2E·operation gate만
- **상태**: 완료

<details><summary>자세히</summary>

- BE: `LiveE2eOperationReadinessSupport` — ThickSpace → 공백 · invisible operator strip (`3937fa5`)
- FE: `notificationChannelStatus.js` · `liveBackendProbe.js` · `liveConfig.js` · `liveGlobalSetup.js` — BE parity (`a3703a5`)
- 회귀: `LiveE2eOperationReadinessSupportTest` · `notificationChannelStatus.test.js` · `liveE2eHarness.test.js`

</details>

### ✅ 가정통신문 — 게시판 표 모바일 가로 스크롤 보정 (FE)
- **에이전트**: UXD
- **한 일**: `/clients/home-newsletter` 의 초안·기관 공지·발송 이력 **3개 표**를 공용 **`.ds-table-wrap`** 으로 감싸 좁은 화면에서 **카드 안에서만** 가로 스크롤되도록 했습니다.
- **내 화면/업무에 영향**: **센터장·사회복지사** — **스마트폰·좁은 창**에서 가정통신문 화면 **전체가 옆으로 밀리지 않음** · 8열 발송 이력 표는 **표 영역만** 스와이프
- **상태**: 완료

<details><summary>자세히</summary>

- FE: `HomeNewsletterLaunchPage.jsx` — draft·facility-notices·history `<table>` → `.ds-table-wrap` (`d171df6`, UXD-183)
- 회귀: `HomeNewsletterLaunchPage.test.jsx` — 30 tests unchanged

</details>

### 📝 ThickSpace·MathML·bidi·G2 표 a11y ops 문서화
- **에이전트**: TWR
- **한 일**: develop HEAD 실측 후 FAQ·매뉴얼·관리/배포 가이드에 **ThickSpace·MathML invisible·bidi marks·Positive*Space·bidi embedding·NonBreakingSpace decode(BE+FE)** · **가정통신문 표 모바일 스크롤(UXD-183)** 을 반영했습니다.
- **내 화면/업무에 영향**: 없음 — 운영·배포 가이드만 갱신
- **상태**: 완료

<details><summary>자세히</summary>

- 실측: BE develop `d911983` · FE develop `29fc34f` — **133 route** · **106 page** · Flyway **V1–V196** · 모듈 **~97.4%**
- FAQ Q875·Q876·Q877·Q878 신규 · USER_MANUAL/ADMIN/DEPLOY §1-4 · CHANGELOG·ops README

</details>

### ✅ live E2E — HTML space alias 디코드 (BE+FE)
- **에이전트**: COD
- **한 일**: 게이트웨이가 **`&ThinSpace;`·`&VeryThinSpace;`** 를 공백으로, **`&NegativeThinSpace;`·`&NegativeMediumSpace;`·`&NegativeThickSpace;`** 를 제거한 뒤 bootstrap blocker를 인식하도록 BE·FE 디코드를 맞췄습니다.
- **내 화면/업무에 영향**: 없음 — **IT·QA** live E2E·operation gate만
- **상태**: 완료

<details><summary>자세히</summary>

- BE: `LiveE2eOperationReadinessSupport` — ThinSpace/VeryThinSpace → 공백 · Negative*Space strip (`fde0606`)
- FE: `notificationChannelStatus.js` · `liveBackendProbe.js` · `liveConfig.js` · `liveGlobalSetup.js` — BE parity (`5b69e7a`)
- 회귀: `LiveE2eOperationReadinessSupportTest` · `notificationChannelStatus.test.js` · `liveE2eHarness.test.js`

</details>

### 📝 HTML space alias·NoBreak/word-joiner FE lockstep ops 문서화
- **에이전트**: TWR
- **한 일**: develop HEAD 실측 후 FAQ·매뉴얼·관리/배포 가이드에 **HTML space alias decode(BE+FE)** · **NoBreak·word-joiner/named space FE lockstep 완료**를 반영했습니다.
- **내 화면/업무에 영향**: 없음 — 운영·배포 가이드만 갱신
- **상태**: 완료

<details><summary>자세히</summary>

- 실측: BE develop `fde0606` · FE develop `5b69e7a` — **133 route** · **106 page** · Flyway **V1–V196** · 모듈 **~97.4%**
- FAQ Q874 신규 · Q872·Q873 BE+FE 정정 · USER_MANUAL/ADMIN/DEPLOY §1-4 · CHANGELOG·ops README

</details>

### ✅ live E2E — NoBreak·word-joiner/named space FE lockstep (FE)
- **에이전트**: COD
- **한 일**: channel-status·live harness가 BE와 동일하게 **`&NoBreak;`·`&ZeroWidthNoBreakSpace;`** · **`&Wj;`·named space entity** 디코드를 수행하도록 FE lockstep을 완료했습니다.
- **내 화면/업무에 영향**: 없음 — **IT·QA** live E2E·operation gate만
- **상태**: 완료

<details><summary>자세히</summary>

- FE: `notificationChannelStatus.js` · `liveBackendProbe.js` · `liveConfig.js` · `liveGlobalSetup.js` — BE parity (`f73413d`)
- BE: Q872·Q873 선행 (`5b59e83`/`7883a90`)
- 회귀: `notificationChannelStatus.test.js` · `liveE2eHarness.test.js`

</details>

### ✅ live E2E — word-joiner·named space HTML entity 디코드 (BE)
- **에이전트**: COD
- **한 일**: 게이트웨이가 **`&Wj;`**(word joiner) 또는 **`&hairsp;`·`&numsp;`·`&puncsp;`·`&nnbsp;`·`&MediumSpace;`·`&emsp13;`·`&emsp14;`** 같은 **named space entity**로 bootstrap detail을 감싸도 fail-closed로 인식하도록 BE 디코드를 보강했습니다.
- **내 화면/업무에 영향**: 없음 — **IT·QA** live E2E·operation gate만
- **상태**: 완료

<details><summary>자세히</summary>

- BE: `LiveE2eOperationReadinessSupport` — `&Wj;` strip · named space → 공백 (`7883a90`)
- FE lockstep: channel-status·live harness 후속(미커밋 시 BE-only)
- 회귀: `LiveE2eOperationReadinessSupportTest`

</details>

### ✅ live E2E — NoBreak zero-width named entity 디코드 (BE)
- **에이전트**: COD
- **한 일**: **`&NoBreak;`·`&ZeroWidthNoBreakSpace;`** named entity가 토큰 중간에 끼어도 bootstrap 마커를 추출하도록 BE를 보강했습니다.
- **내 화면/업무에 영향**: 없음 — **IT·QA** live E2E·operation gate만
- **상태**: 완료

<details><summary>자세히</summary>

- BE: `LiveE2eOperationReadinessSupport` — NoBreak·ZeroWidthNoBreakSpace strip (`5b59e83`)
- FE: channel-status 주석·치환 일부 착수(working tree) · 커밋 lockstep 후속
- 회귀: `LiveE2eOperationReadinessSupportTest`

</details>

### ✅ live E2E — dash/minus/hyphen HTML entity 디코드 (BE+FE)
- **에이전트**: COD
- **한 일**: 게이트웨이가 ASCII 하이픈 대신 **`&ndash;`·`&mdash;`·`&minus;`·`&hyphen;`·`&dash;`** 또는 Unicode minus/en-dash를 넣어도 **ASCII `-`로 접어** `bootstrap-disabled` 등을 fail-closed로 맞춥니다. FE channel-status·live harness도 BE와 동일합니다.
- **내 화면/업무에 영향**: 없음 — **IT·QA** live E2E·operation gate만
- **상태**: 완료

<details><summary>자세히</summary>

- BE: `LiveE2eOperationReadinessSupport` — dash family → `-` (`7e02d58`)
- FE: `notificationChannelStatus.js` · `liveBackendProbe.js` · `liveConfig.js` · `liveGlobalSetup.js` (`cf8a248`)
- 회귀: `LiveE2eOperationReadinessSupportTest` · `notificationChannelStatus.test.js` · `liveE2eHarness.test.js`

</details>

### 📝 dash·NoBreak·word-joiner/named space ops 문서화
- **에이전트**: TWR
- **한 일**: develop HEAD 실측 후 FAQ·매뉴얼·관리/배포 가이드에 **dash/minus/hyphen(BE+FE)** · **NoBreak(BE)** · **word-joiner·named space(BE)** 디코드 범위를 반영하고, 프로그램 리포트 지점 필터(Q864) 설명을 BE/FE 분리로 정정했습니다.
- **내 화면/업무에 영향**: 없음 — 운영·배포 가이드만 갱신
- **상태**: 완료

<details><summary>자세히</summary>

- 실측: BE develop `7883a90` · FE develop `cf8a248` — **133 route** · **106 page** · Flyway **V1–V196** · 모듈 **~97.4%**
- FAQ Q871·Q872·Q873 신규 · Q864 정정 · USER_MANUAL/ADMIN/DEPLOY §1-4 · CHANGELOG·ops README

</details>

### ✅ live E2E — zero-width·tab/newline named HTML entity 디코드 (BE+FE)
- **에이전트**: COD
- **한 일**: 게이트웨이가 토큰 중간에 **`&zwnj;`·`&zwj;`·`&ZeroWidthSpace;`** 또는 **`&Tab;`·`&NewLine;`** 같은 **named HTML entity**로 bootstrap 마커를 쪼개도 fail-closed로 인식하도록 BE·FE 디코드를 맞췄습니다.
- **내 화면/업무에 영향**: 없음 — **IT·QA** live E2E·operation gate만
- **상태**: 완료

<details><summary>자세히</summary>

- BE: `LiveE2eOperationReadinessSupport` — zero-width named entity strip (`7102f82`) · tab/newline named entity (`431859c` carry)
- FE: `notificationChannelStatus.js` · `liveBackendProbe.js` · `liveConfig.js` · `liveGlobalSetup.js` — BE parity (`e45dacb`)
- 회귀: `LiveE2eOperationReadinessSupportTest` · `notificationChannelStatus.test.js` · `liveE2eHarness.test.js`

</details>

### 📝 zero-width·tab/newline named entity ops 문서화
- **에이전트**: TWR
- **한 일**: develop HEAD 실측 후 FAQ·매뉴얼·관리/배포 가이드에 **zero-width·tab/newline named HTML entity decode** 범위를 반영했습니다.
- **내 화면/업무에 영향**: 없음 — 운영·배포 가이드만 갱신
- **상태**: 완료

<details><summary>자세히</summary>

- 실측: BE develop `7102f82` · FE develop `e45dacb` — **133 route** · **106 page** · Flyway **V1–V196** · 모듈 **~97.4%**
- FAQ Q869·Q870 신규 · Q861·Q859 교차 참조 · USER_MANUAL/ADMIN/DEPLOY §1-4 · CHANGELOG·ops README

</details>

### ✅ live E2E — bootstrap blocker HTML entity 디코드 확대 (BE)
- **에이전트**: COD
- **한 일**: bootstrap blocker 파서가 **8자리 유니코드 escape**, **`&#61;`/`&equals;`(=)**, **`&#58;`/`&colon;`(:)**, **`&#92;`/`&bsol;`(\\)**, **탭·개행 entity**까지 정규화하도록 보강했습니다.
- **내 화면/업무에 영향**: 없음 — **IT·QA** live E2E·operation gate만
- **상태**: 완료

<details><summary>자세히</summary>

- BE: `LiveE2eOperationReadinessSupport` entity decode 확장 (`0f96716` → `431859c`)
- FE parity는 기존 gate 로직 유지, 운영 문서는 blocker 토큰 예시를 확장해 안내

</details>

### ✅ 기관 공지 — branch scope fallback 보강 (FE)
- **에이전트**: COD
- **한 일**: 기관 공지/가정통신문 흐름에서 현재 지점 컨텍스트가 불안정할 때 **첫 번째 유효 지점 스코프**로 안전하게 fallback 하도록 보강했습니다.
- **내 화면/업무에 영향**: **센터장·사회복지사** — `/clients/home-newsletter` 진입 시 간헐적 빈 상태·조회 실패 가능성이 줄어듭니다.
- **상태**: 완료

<details><summary>자세히</summary>

- FE: first valid branch scope fallback (`f5dded2`)
- 동반 UX 정리: UXD-182 (`0a5ec86`) — M12 blocker 안내·G17 안내문·G2 pagination 접근성 보강

</details>

### 📝 QA-B95 entity decode 확대·G2 scope fallback ops 문서화
- **에이전트**: TWR
- **한 일**: FAQ·사용자 매뉴얼에 **추가 blocker entity decode 범위**와 **기관 공지 branch scope fallback** 운영 포인트를 반영했습니다.
- **내 화면/업무에 영향**: 없음 — 운영 문서만 갱신
- **상태**: 완료

### ✅ live E2E — invisible Unicode format 문자 제거 (BE+FE)
- **에이전트**: COD
- **한 일**: 게이트웨이가 토큰 중간에 **ZWNJ·WJ·ZWJ** 등 **보이지 않는 format 문자(Cf)** 를 끼워 넣어도 bootstrap blocker를 인식하도록 BE·FE 정규화를 맞췄습니다.
- **내 화면/업무에 영향**: 없음 — **IT·QA** live E2E·operation gate만
- **상태**: 완료

<details><summary>자세히</summary>

- BE: `LiveE2eOperationReadinessSupport.stripFormatCharacters` — Unicode Cf 제거 (`20ac77f`)
- FE: `notificationChannelStatus.js` · `liveBackendProbe.js` · `liveConfig.js` · `liveGlobalSetup.js` — `\p{Cf}` strip (`1bc6eab`)
- 회귀: `LiveE2eOperationReadinessSupportTest` · `notificationChannelStatus.test.js` · `liveE2eHarness.test.js`

</details>

### ✅ live E2E — 추가 유니코드 공백 정규화 (BE+FE)
- **에이전트**: COD
- **한 일**: figure space·punctuation space·hair space·좁은 NBSP·전각 공백 등 **추가 유니코드 공백**을 일반 공백으로 바꿔 bootstrap 마커를 추출합니다. FE channel-status·live harness도 BE와 동일합니다.
- **내 화면/업무에 영향**: 없음 — **IT·QA** live E2E·operation gate만
- **상태**: 완료

<details><summary>자세히</summary>

- BE: `LiveE2eOperationReadinessSupport` — U+2007·U+2008·U+200A·U+202F·U+3000 → 공백 (`8098f23`)
- FE: `notificationChannelStatus.js` · `liveBackendProbe.js` · `liveConfig.js` · `liveGlobalSetup.js` (`91aee07`)
- 회귀: `LiveE2eOperationReadinessSupportTest` · `notificationChannelStatus.test.js` · `liveE2eHarness.test.js`

</details>

### 📝 invisible format·추가 유니코드 공백 ops 문서화
- **에이전트**: TWR
- **한 일**: develop HEAD 실측 후 FAQ·매뉴얼·관리/배포 가이드에 **Cf format strip** · **추가 유니코드 공백 정규화(BE+FE)** 를 반영했습니다.
- **내 화면/업무에 영향**: 없음 — 운영·배포 가이드만 갱신
- **상태**: 완료

<details><summary>자세히</summary>

- 실측: BE develop `8098f23` · FE develop `91aee07` — **133 route** · **106 page** · Flyway **V1–V196** · 모듈 **~97.4%**
- FAQ Q861·Q862 신규 · Q859 교차 참조 · USER_MANUAL/ADMIN/DEPLOY §1-4 · CHANGELOG·ops README

</details>

### ✅ live E2E — soft-hyphen·whitespace HTML entity 디코드 (BE+FE)
- **에이전트**: COD
- **한 일**: 게이트웨이가 **`boot&shy;strap-disabled`** 처럼 토큰 중간에 soft-hyphen을 넣거나 **`&ensp;`·`&emsp;`·`&thinsp;`** 등 공백 entity로 bootstrap detail을 감싸도 fail-closed로 인식하도록 BE·FE 디코드를 맞췄습니다.
- **내 화면/업무에 영향**: 없음 — **IT·QA** live E2E·operation gate만
- **상태**: 완료

<details><summary>자세히</summary>

- BE: `LiveE2eOperationReadinessSupport` — `&shy;` mid-token strip · `&nbsp;`/`&ensp;`/`&emsp;`/`&thinsp;`·U+00A0/ZWSP 정규화 (`c67c7ed`)
- FE: `notificationChannelStatus.js` · `liveBackendProbe.js` · `liveConfig.js` · `liveGlobalSetup.js` — BE parity (`83e6296`)
- 회귀: `LiveE2eOperationReadinessSupportTest` · `notificationChannelStatus.test.js` · `liveE2eHarness.test.js`

</details>

### ✅ 재무회계 BPO — SSO 블로커 잔여 시 launch·버튼 숨김 (FE)
- **에이전트**: COD
- **한 일**: health·launch에 **SSO readiness blocker**가 남아 있으면 **`ssoAvailability`를 PLANNED로 강등**하고 **「SSO 자동 로그인」 버튼을 숨깁니다**. 블로커가 해소되기 전에는 SSO handoff를 시도할 수 없습니다.
- **내 화면/업무에 영향**: **센터장·통합 관리자** — **`/accounting`** 에서 env 미설정·비허용 URL 등 **블로커가 있으면 SSO 버튼이 보이지 않음** · **「SSO 잔여 블로커」 안내**와 **공개 로그인**은 그대로 사용
- **상태**: 완료

<details><summary>자세히</summary>

- FE: `accountingBpo.js` — `mergeAccountingBpoLaunchWithHealth` · `canLaunchAccountingBpoSso` — blocker 있으면 PLANNED·launch false
- blocker: `sso-otp-credentials-missing` · `sso-portal-url-not-allowlisted` 등
- 회귀: `accountingBpo.test.js` · `AccountingBpoPage.test.jsx` (`b42174a`)

</details>

### 📝 soft-hyphen·M12 SSO demote ops 문서화
- **에이전트**: TWR
- **한 일**: develop HEAD 실측 후 FAQ·매뉴얼·관리/배포 가이드에 **soft-hyphen·whitespace HTML entity decode** · **M12 BPO SSO 블로커 시 launch 숨김**을 반영했습니다.
- **내 화면/업무에 영향**: 없음 — 운영·배포 가이드만 갱신
- **상태**: 완료

<details><summary>자세히</summary>

- 실측: BE develop `c67c7ed` · FE develop `83e6296` — **133 route** · **106 page** · Flyway **V1–V196** · 모듈 **~97.4%**
- FAQ Q859·Q860 신규 · Q854·Q785 보강 · USER_MANUAL §4-6-5 · ADMIN/DEPLOY §1-4 · CHANGELOG·ops README

</details>

### ✅ 기관 공지·자료실 — 게시·삭제 후 빈 페이지 복구 (FE)
- **에이전트**: COD
- **한 일**: 기관 공지 게시판에서 **마지막 행을 게시·삭제**해도 목록이 **빈 페이지에 머무르지 않고** 마지막 유효 페이지로 다시 맞춥니다.
- **내 화면/업무에 영향**: **센터장·사회복지사** — **`/clients/home-newsletter#facility-notices`** 에서 게시·삭제 직후 **목록이 바로 보임**(수동 새로고침·이전 페이지 클릭 불필요)
- **상태**: 완료

<details><summary>자세히</summary>

- FE: `HomeNewsletterLaunchPage` — `reconcileNoticeBoardPageAfterMutation` · publish/delete/save 후 `totalPages` 기준 fallback
- 회귀: `HomeNewsletterLaunchPage.test.jsx` — 마지막 행 삭제 후 페이지 복구

</details>

### ✅ live E2E — `&nbsp;`·유니코드 NBSP bootstrap blocker 디코드 (BE)
- **에이전트**: COD
- **한 일**: 게이트웨이가 **`&nbsp;`** 또는 **유니코드 비분리 공백(U+00A0)** 으로 bootstrap detail을 감싸도 fail-closed로 인식하도록 정규화를 보강했습니다.
- **내 화면/업무에 영향**: 없음 — **IT·QA** live E2E·operation gate만
- **상태**: 완료

<details><summary>자세히</summary>

- BE: `LiveE2eOperationReadinessSupport` — `&nbsp;` named entity · `\u00a0` → 일반 공백
- 회귀: `LiveE2eOperationReadinessSupportTest` — nbsp-escaped detail

</details>

### 📝 기관 공지 페이지 복구·NBSP blocker ops 문서화
- **에이전트**: TWR
- **한 일**: develop HEAD 실측 후 FAQ·매뉴얼·관리/배포 가이드에 **기관 공지 빈 페이지 복구** · **NBSP bootstrap decode** 를 반영했습니다.
- **내 화면/업무에 영향**: 없음 — 운영·배포 가이드만 갱신
- **상태**: 완료

<details><summary>자세히</summary>

- 실측: BE develop `4bf5684` · FE develop `483dfe1` — **133 route** · **106 page** · Flyway **V1–V196** · 모듈 **~97.4%**
- FAQ Q857·Q858 신규 · USER_MANUAL §4-7-3a · ADMIN/DEPLOY §1-4 · CHANGELOG·ops README

</details>

### ✅ live E2E — `&num;` named-num HTML entity 디코드 (BE+FE)
- **에이전트**: COD
- **한 일**: 게이트웨이가 `&num;45;` · `&num;45`(세미콜론 없음) 처럼 **named-num** 형태로 하이픈을 보내도 bootstrap blocker를 인식하도록 디코드를 맞췄습니다. 프론트 readiness·live harness도 동일 규칙입니다.
- **내 화면/업무에 영향**: 없음 — **IT·QA** live E2E·operation gate만
- **상태**: 완료

<details><summary>자세히</summary>

- BE: `LiveE2eOperationReadinessSupport` — `&num;` → numeric reference 정규화 · 세미콜론 생략 named entity
- FE: `notificationChannelStatus.js` · `liveGlobalSetup.js` · `liveConfig.js` · harness 테스트
- 회귀: `LiveE2eOperationReadinessSupportTest` · `liveE2eHarness.test.js`

</details>

### ✅ live E2E — snake_case bootstrap blocker 코드 수용 (BE)
- **에이전트**: COD
- **한 일**: 게이트웨이·객체 payload가 `bootstrap_disabled`·`service_unavailable` 처럼 **snake_case 코드**를 내도 fail-closed로 막히도록 정규화를 보강했습니다.
- **내 화면/업무에 영향**: 없음 — **IT·QA** live E2E·operation gate만
- **상태**: 완료

<details><summary>자세히</summary>

- BE: blocker code snake_case → kebab-case 정규화 · bootstrap disabled·service-unavailable 회귀 테스트

</details>

### 📝 named-num·snake_case blocker · 위원회「가족과의 소통」·달력 마커 ops 문서화
- **에이전트**: TWR
- **한 일**: develop HEAD 실측 후 FAQ·매뉴얼·관리/배포 가이드에 **named-num entity** · **snake_case bootstrap 코드** · **위원회 보호자 회의=필수업무 27** · **CalendarDayMarker** 를 반영했습니다.
- **내 화면/업무에 영향**: 없음 — 운영·배포 가이드만 갱신
- **상태**: 완료

<details><summary>자세히</summary>

- 실측: BE develop `a8d0af5` · FE develop `2cefb1d` — **133 route** · **106 page** · Flyway **V1–V196** · 모듈 **~97.4%**
- FAQ Q855·Q856 신규 · Q723·Q843 보강 · USER_MANUAL §3-2·위원회 · ADMIN/DEPLOY §1-4 · CHANGELOG·ops README

</details>

### ✅ 기능회복·목욕 준수 — 「지표 27」이중번호 안내
- **에이전트**: COD
- **한 일**: 기능회복·목욕 준수 API 응답에 **공단 주야간 평가 지표 27(기능회복훈련)** 과 **필수업무 일련 27(가족과의 소통·위원회 보호자회의)** 이 번호만 같아 헷갈리지 않도록 **안내 문구·경로**를 넣었습니다.
- **내 화면/업무에 영향**: **사회복지사·센터장** — **`/programs/functional-recovery`** 준수 현황에서 **「가족과의 소통」은 위원회 화면**(`/staff/committee-meetings`)으로 구분 · 목욕 패널도 동일 안내
- **상태**: 완료

<details><summary>자세히</summary>

- API: `GET /api/v1/programs/functional-recovery/compliance` · `GET /api/v1/care/bathing-schedules/indicator-27-compliance`
- 응답 필드: `essentialDutySerial27Label`·`essentialDutySerial27MeetingType=GUARDIAN`·`essentialDutySerial27Route`·`dualNumberingNoteKo`
- 평가 지표 27 정본은 계속 기능회복(`/programs/functional-recovery`) · 목욕은 청구 선택 축(`BATHING_CLAIM_COMPLIANCE`)

</details>

### ✅ 알림 채널 — 문자 참고 단가 전용 카탈로그 (BE+FE)
- **에이전트**: COD
- **한 일**: **`GET /api/v1/notifications/dispatch-reference-unit-rates`** 전용 카탈로그와 health **`notificationDispatchReferenceUnitRates`** 를 추가했습니다. 알림 채널 패널은 **전용 API → channel-status 임베드 → FE 정적값** 순으로 표시합니다.
- **내 화면/업무에 영향**: **센터장·통합 관리자** — **`/organization/settings`**·**`/dashboard`** 「문자 발송 참고 단가」가 **서버 전용 카탈로그**와 맞춰짐(앱 10·SMS 20·MMS 50원, **청구·정산 아님**)
- **상태**: 완료

<details><summary>자세히</summary>

- BE: `NotificationChannelStatusController` 전용 GET · `NotificationDispatchUnitRatesCatalog` 동일 상수 · health 미러
- FE: `fetchDispatchReferenceUnitRatesApi` · `NotificationChannelReadinessPanel` 우선순위 3단
- 권한: `hq_admin`·`branch_admin`

</details>

### ✅ 알림 채널 — 참고 단가 표 고대비·CSS (UXD)
- **에이전트**: UXD
- **한 일**: 「문자 발송 참고 단가」표에 **누락된 CSS 블록**과 **Windows 고대비(forced-colors) 테두리**를 보강했습니다.
- **내 화면/업무에 영향**: **고대비 모드** 사용자 — 알림 채널 패널 참고 단가 표 **경계선이 보임**
- **상태**: 완료

<details><summary>자세히</summary>

- `components.css` — `.ds-notification-channel-panel__unit-rates` · forced-colors `.ds-table-wrap`

</details>

### ✅ live E2E — 삼중 HTML entity blocker 디코드 (BE+FE)
- **에이전트**: COD
- **한 일**: 게이트웨이가 **`&AMP;AMP;#45;`** 처럼 **세 번 감싼** numeric HTML entity를 보내도 bootstrap blocker를 인식하도록 **다중 패스 디코드**를 강화했습니다.
- **내 화면/업무에 영향**: 없음 — **IT·QA** live E2E·operation gate만
- **상태**: 완료

<details><summary>자세히</summary>

- BE: `LiveE2eOperationReadinessSupport` bounded multi-pass
- FE: `notificationChannelStatus.js` · `liveGlobalSetup.js` · `liveConfig.js` — decode pass 상향(최대 5)

</details>

### ✅ 재무회계 BPO — SSO 잔여 블로커 한국어 안내 (FE)
- **에이전트**: COD
- **한 일**: **`/accounting`** 화면에 health·launch의 SSO readiness blocker를 **한국어 안내 문구**로 표시하는 **「SSO 잔여 블로커」** 섹션을 추가했습니다. env 미설정·포털 URL 비허용 등 **조치 방법**을 현장에서 바로 확인할 수 있습니다.
- **내 화면/업무에 영향**: **센터장·통합 관리자** — **`/accounting`** 에서 SSO가 **후속(PLANNED)** 일 때 **자격 env 설정·수지파인 URL 수정** 안내가 카드에 표시됨 · **공개 로그인**은 그대로 사용 가능
- **상태**: 완료

<details><summary>자세히</summary>

- FE: `describeAccountingBpoReadinessBlocker` · `AccountingBpoPage` — `data-testid="accounting-bpo-sso-blockers"`
- blocker: `sso-otp-credentials-missing` · `sso-portal-url-not-allowlisted` · 기타 코드 fallback
- handoff 실패: `formatAccountingBpoSsoHandoffError` — 429·422 한국어

</details>

### 📝 M12 SSO 블로커·G17·참고 단가 ops 문서화
- **에이전트**: TWR
- **한 일**: develop HEAD 실측 후 FAQ·매뉴얼·관리/배포 가이드에 **재무회계 SSO 블로커 안내 UI** · **지표27 이중번호** · **참고 단가 전용 API** · **삼중 HTML entity** · 고대비 CSS를 반영했습니다.
- **내 화면/업무에 영향**: 없음 — 운영·배포 가이드만 갱신
- **상태**: 완료

<details><summary>자세히</summary>

- 실측: BE develop · FE develop — **133 route** · **106 page** · Flyway **V1–V196** · 모듈 **~97.4%**
- FAQ Q854 신규 · USER_MANUAL §4-6-5 · ADMIN_GUIDE §6-2-24f·24g · CHANGELOG·ops README

</details>

---

## 2026-07-15

### ✅ G2 기관 공지 게시판 — 전체 full-stack 완성 (BE+FE)
- **에이전트**: COD
- **한 일**: **`GET/POST/PATCH /api/v1/notifications/facility-notices`** · **초안 복제·게시·상세 조회** · **첨부 http(s)만** 허용(V193 CHECK) · **분류 NOTICE/RESOURCE** · **기관(테넌트)별 격리** · 게시판 영속화 + FE **`/clients/home-newsletter` 게시판 CRUD**·**발송이력 board-style 필터**(`branchId` 스코프·`activeBranch` 우선) — **id=10 모듈 1.0 도달**(id=10-4·**G2 FULL 1.0**)
- **내 화면/업무에 영향**: **센터장·통합 관리자** — **`/clients/home-newsletter`** 게시판에서 **「기관 공지」·「자료실」 카테고리** 선택 후 **초안→게시·복제·수정·상세** · **조용한 시간대** 자동 제외 (Q806·Q811)
- **상태**: 완료

<details><summary>자세히</summary>

- BE: `55b8f84`(BNK-729 facility-notice CRUD) + `24f555d`(V192 dispatch-history index) · `NotificationFacilityNoticeService` · `V192 CHECK chk_facility_notices_attachment_url_format` · 6-endpoint REST · DRAFT/PUBLISHED workflow · 기관 권한 검증 · 감사 trigger · FE 발송이력 필터(`branchId`·`activeBranchId` parity)
- FE: `bb48b6c`(BNK-729 draft board UI) + `0210aaa`(BNK-730 persist compose as DRAFT) · **`FacilityNoticeBoardPage`** ·**draft session + history reuse** · compose preview PATCH → facility-notice DRAFT 저장 · 기관명 JS 검증 · 첨부 http(s) placeholder 불안전 링크 차단
- V192–V193 · health `homeNewsletter*` ready(조용한시간대 blocker 반영) · API_SPEC §4-2-1 · FAQ Q803–Q808·Q811 · USER_MANUAL §5-9 · ADMIN_GUIDE §1-4

</details>

### ✅ M12 회계 BPO — launch catalog + SSO OTP handoff API
- **에이전트**: COD
- **한 일**: **`GET /api/v1/billing/accounting/bpo-launch`** · **`POST …/bpo-sso-handoff`** 카탈로그 + SSO OTP 핸드오프 · 외부 BPO(수지파인·sujifine) 상태 probe · 환경변수 스코프 자격 검증(HQ/BRANCH만) · FE wire — **id=12 모듈 0.7 도달**
- **내 화면/업무에 영향**: **통합 관리자** — **`/accounting`** 페이지에서 **「회계 시스템(BPO) 진입」** 링크 · 공개 로그인 또는 **SSO(환경 자격 시)** · **비밀번호 미수집**
- **상태**: 완료

<details><summary>자세히</summary>

- BE: `edaa9e9`(BNK-716 launch catalog) + `093ac88`(BNK-720 SSO handoff) · `AccountingBpoService` · catalog **`availabilityStatus`**(AVAILABLE/PLANNED/UNAVAILABLE) · SSO OTP 계정 매칭 · 외부 포털 검증 · health `accountingBpo*Ready` · V190 · **환경 자격 미설정 시 → 공개 로그인만**(REQUIREMENTS §11-4 compliance)
- FE: `84b336b`(BNK-717 wire catalog·external link) + `063c269`(BNK-720 align KPI) · **`AccountingBpoPage`** · catalog status 렌더 · **새 탭**에서 BPO 포털 열기 · a11y announce · 모듈 88.62%→91.90%→**0.7 carry**(M12 BPO+SSO pending P1)
- health **`accountingBpoLaunchReady`** · FE 환경 공백=missing(not default) · API_SPEC §4-7 · ADMIN_GUIDE §1-4 · Q782·Q784·Q785·Q787·Q801

</details>

### ✅ G2 가정통신문 — 발송이력 board-style 필터·필터링 갱신
- **에이전트**: COD
- **한 일**: **`GET /api/v1/notifications/home-newsletter/dispatch-history`** — **`branchId` 스코프** 필터 · **`activeBranchId` 우선** · page/size/sort/q(제목·발신자) · **v193 인덱스** · FE board-style 목록 + **「기간·상태·중앙·지점」 필터** · 「중앙」 선택 시 → 지점 자동 초기화
- **내 화면/업무에 영향**: **센터장·통합 관리자** — **`/clients/home-newsletter`** 우상 **「발송 이력」** 탭에서 **기간·상태 필터**로 발송 내역 조회(Q801·기본 20건)
- **상태**: 완료

<details><summary>자세히</summary>

- BE: `24f555d`(V191 dispatch-history index) + `b054ca6`(center-name/summary surface) + `6706f65`(filters) · 서버 필터 로직 · `activeBranchId` 스코프 우선 · query builder pagination
- FE: `3bd50ac`(BNK-727 board-style controls) + `bb48b6c`(history filters wire) · `HomeNewsletterDispatchHistoryPanel` · filter UI + 「상태 초기화」
- USER_MANUAL §5-9 · ADMIN §1-4 · V191 · Q801·Q793·Q800 · FAQ 신규

</details>

### 📝 기관 공지·회계 BPO·live E2E bootstrap ops 문서화
- **에이전트**: TWR
- **한 일**: 실측 BNK-730(BE `82a83e3`·FE `0210aaa`) 기준 ops 문서 갱신 — **G2 기관 공지 게시판 FULL·M12 BPO launch** · **live E2E bootstrap blocker** 종합 진단 · FAQ **Q809·Q828·Q829·Q830·Q835·Q837·Q839·Q840·Q841** 신규 · USER_MANUAL **§1-5 G2/M12 체크박스** · ADMIN_GUIDE §1-4 baseline 갱신 · 모듈 KPI **93.62%→97.41%**(27.15/29·id=1-5 0.85→1.0·+0.52pp)
- **내 화면/업무에 영향**: 없음 — 운영·배포 가이드만 갱신
- **상태**: 완료

<details><summary>자세히</summary>

- 문서: CHANGELOG(summary·카드)·FAQ(기관공지·BPO 관련 Q신규)·USER_MANUAL(§1-5 BNK-730 추가)·ADMIN_GUIDE(1-4 baseline)·DEPLOYMENT(ops-ready flag)
- Flyway **V1–V192** · 모듈 KPI **27.15/29** · **id=1-5 1.0 도달**(G2 FULL)·**id=10 1.0**(공지게시판)
- P1 잔여: M11 급여 persist·수익/인건비 자동 집계·기관별 SSO 자격 · P2: program reports FE·live PG·LCMS FCMS

</details>

### ✅ live E2E bootstrap blocker — 합성 매칭·토큰 파싱 FULL (BE+FE)
- **에이전트**: COD
- **한 일**: **Q825·Q828·Q833·Q834·Q836·Q837·Q839·Q840·Q841** 종합 대응 — **HTML entity**(소문자·대소문자·이중·세미콜론 생략) · **URL percent-encoded** · **중첩 JSON·유니코드** · **object-form JSON** · **괄호·따옴표·배열·key:value padding** · **space/comma/semicolon composite token** 파싱 및 bootstrap gate 매칭
- **내 화면/업무에 영향**: 없음 — live E2E 통과 가드 강화(운영 블로커 투명성)
- **상태**: 완료

<details><summary>자세히</summary>

- BE: **`operationBlockers` 정규화** — Jackson nested JSON parse · URL decode(`URLDecoder`) · HTML entity decode(`String.replace regex`) · 모든 형식 bootstrap `code` 마커 추출
- FE: **`liveGlobalSetup.js`** + **`notificationChannelStatus.js`** · **`normalizeOperationBlockers`** · **`normalizeLiveOperationBlockers`** · bootstrap token matching via composite regex · parity test
- health **`liveE2eEffectiveOperationReady`** · **`liveE2eSuppressedBootstrapOperationBlockers`** · **`liveE2eEffectiveOperationSuppressedByBootstrap`** — FE opt-in(`LIVE_E2E_ALLOW_BOOTSTRAP_SUPPRESSION`) 미설정 시 skip
- BE commits: `27de3a3`(nested JSON)·`7868384`(URL)·`956c487`/`556eeff`/`2768252`/`89dc0a6`/`a5f4098`(HTML entity) · FE: `956c487`/`2992fa5`(object-form)
- QA-B95 effective gate FE **`5805d68`** parity · API_SPEC §4-3 health probe · FAQ Q821·Q824·Q825·Q828·Q833·Q834·Q836·Q837·Q839·Q840·Q841

</details>

### 📝 channel-status 참고 단가 BE+FE ops 문서화
- **에이전트**: TWR
- **한 일**: develop HEAD 실측 후 FAQ·매뉴얼·관리/배포 가이드에 **`GET /notifications/channel-status` `dispatchReferenceUnitRates`**(BE) · FE **BE 우선·static fallback** 규칙을 반영했습니다.
- **내 화면/업무에 영향**: 없음 — 문서·운영 가이드만 갱신
- **상태**: 완료

<details><summary>자세히</summary>

- 실측: BE develop **`2f578fb`** · FE develop **`a356083`** — **133 route** · **106 page** · Flyway **V1–V196** · 모듈 **~97.4%**
- FAQ **Q844** 갱신 · USER_MANUAL §5-5 · ADMIN §1-4 · DEPLOYMENT §1-4

</details>

### ✅ 알림 채널 — channel-status 참고 단가 API (BE)
- **에이전트**: COD
- **한 일**: **`GET /api/v1/notifications/channel-status`** 응답에 **`dispatchReferenceUnitRates`** 를 추가했습니다. 앱 푸시 **10원** · SMS **20원** · MMS **50원**이며, **Solapi 실과금·청구와 무관한 운영 안내**입니다.
- **내 화면/업무에 영향**: **센터장·통합 관리자** — 알림 채널 API·패널이 **동일한 참고 단가**를 서버에서 받음
- **상태**: 완료

<details><summary>자세히</summary>

- `NotificationDispatchUnitRatesCatalog` · `NotificationChannelStatusResponse.dispatchReferenceUnitRates`
- regression: `NotificationChannelReadinessServiceTest`

</details>

### ✅ 알림 채널 — BE 참고 단가 우선 표시 (FE)
- **에이전트**: COD
- **한 일**: **`NotificationChannelReadinessPanel`** 이 channel-status의 **`dispatchReferenceUnitRates`** 를 **우선 사용**하고, 응답이 없거나 비어 있으면 **FE 정적 fallback**(앱 10·SMS 20·MMS 50원)을 씁니다.
- **내 화면/업무에 영향**: **센터장·통합 관리자** — **`/organization/settings`**·**`/dashboard`** 알림 채널 패널 참고 단가가 **서버·화면 parity** 유지
- **상태**: 완료

<details><summary>자세히</summary>

- `resolveDispatchReferenceUnitRates` · `notificationDispatchUnitRates.js` · `NotificationChannelReadinessPanel`
- regression: `notificationDispatchUnitRates.test.js` · `NotificationChannelReadinessPanel.test.jsx`

</details>

### 📝 문자 발송 참고 단가 ops 문서화
- **에이전트**: TWR
- **한 일**: develop HEAD 실측 후 FAQ·매뉴얼·관리/배포 가이드에 **알림 채널 패널 「문자 발송 참고 단가」**(앱 10·SMS 20·MMS 50원, 운영 안내 전용)를 반영했습니다.
- **내 화면/업무에 영향**: 없음 — 문서·운영 가이드만 갱신
- **상태**: 완료

<details><summary>자세히</summary>

- 실측: BE develop **`e9f24f7`** · FE develop **`56797a8`** — **133 route** · **106 page** · Flyway **V1–V196** · 모듈 **~97.4%**
- FAQ **Q844** · USER_MANUAL §5-5 · ADMIN §1-4 · DEPLOYMENT §1-4

</details>

### ✅ 알림 채널 — 문자 발송 참고 단가 (FE)
- **에이전트**: COD
- **한 일**: 조직 설정·대시보드 **알림 채널 준비 상태** 패널에 **「문자 발송 참고 단가」** 표를 추가했습니다. 앱 푸시 **10원** · SMS **20원** · MMS **50원**이며, **Solapi 실과금·청구와 무관한 운영 안내**입니다.
- **내 화면/업무에 영향**: **센터장·통합 관리자** — **`/organization/settings`**·**`/dashboard`** 알림 채널 패널에서 채널별 **참고 단가**를 바로 확인
- **상태**: 완료

<details><summary>자세히</summary>

- `notificationDispatchUnitRates.js` · `NotificationChannelReadinessPanel` — Table「문자 발송 참고 단가」
- regression: `notificationDispatchUnitRates.test.js` · `NotificationChannelReadinessPanel.test.jsx`

</details>

### 📝 세미콜론 생략 entity·연계 리포트 페이지·a11y ops 문서화
- **에이전트**: TWR
- **한 일**: develop HEAD 실측 후 FAQ·매뉴얼·관리/배포 가이드에 **live E2E 세미콜론 생략 numeric HTML entity decode** · **연계기록지 리포트 페이지네이션** · **SkipLink·ProgressBar·Skeleton a11y(UXD-180)** 를 반영했습니다.
- **내 화면/업무에 영향**: 없음 — 문서·운영 가이드만 갱신
- **상태**: 완료

<details><summary>자세히</summary>

- 실측: BE develop · FE develop — **133 route** · **106 page** · Flyway **V1–V196** · 모듈 **~97.4%**
- FAQ **Q840** · **Q841** · **Q842** · **Q843** · USER_MANUAL §3-2·§4-7-3b · ADMIN §1-4 · DEPLOYMENT §1-4

</details>

### ✅ live E2E — semicolon-optional numeric HTML entity decode (FE)
- **에이전트**: COD
- **한 일**: health/probe·알림 채널 readiness의 blocker 토큰이 **`&#45`**·**`&#x2d`** 처럼 **세미콜론(`;`) 없이** 끝나도 numeric HTML entity로 디코딩합니다. BE `@89dc0a6` 와 동일 규칙입니다.
- **내 화면/업무에 영향**: **센터장·sysadmin** — **`/organization/settings`**·**`/dashboard`** 알림 채널 패널이 gateway entity 표기 차이에서도 누락 원인 표시. **IT·QA** live E2E gate
- **상태**: 완료

<details><summary>자세히</summary>

- `notificationChannelStatus.js` · `liveGlobalSetup.js` · `liveBackendProbe.js` · `liveConfig.js`
- regression: `notificationChannelStatus.test.js` · `liveE2eHarness.test.js`

</details>

### ✅ live E2E — double-encoded numeric entity re-decode (BE)
- **에이전트**: COD
- **한 일**: health/probe detail의 **`&AMP;#X2D;`** 등 **이중 인코딩 numeric entity**를 **`&amp;` 전개 후 numeric decode를 재실행**해 한 패스에서 처리합니다. FE multi-pass decode와 parity입니다.
- **내 화면/업무에 영향**: 없음 — **IT·QA** live E2E·operation gate만
- **상태**: 완료

<details><summary>자세히</summary>

- `LiveE2eOperationReadinessSupport.decodeHtmlEntityDetailToken` — post-`&amp;` numeric re-run
- regression: `LiveE2eOperationReadinessSupportTest` — uppercase double-encoded lock

</details>

### ✅ 연계기록지 — 지점 리포트 페이지네이션 (FE)
- **에이전트**: COD
- **한 일**: **`/clients/linkage-records`** 지점 통합 리포트에 **페이지 이동·총 건수 표시**를 추가했습니다. **조회** 버튼으로 필터를 확정하면 **1페이지로 초기화**되며, 페이지당 **100건**씩 불러옵니다.
- **내 화면/업무에 영향**: **센터장·사회복지사** — 연계기록지가 많은 지점에서 **전체 이력을 페이지 단위로** 넘겨 볼 수 있음
- **상태**: 완료

<details><summary>자세히</summary>

- `ClientLinkageRecordsReportPage` — `Pagination` · `REPORT_PAGE_SIZE=100` · `fetchClientLinkageRecordsReportApi` page/size
- regression: `ClientLinkageRecordsReportPage.test.jsx`

</details>

### ✅ UI 접근성 — SkipLink·ProgressBar·Skeleton·달력 마커 (FE)
- **에이전트**: UXD
- **한 일**: 로그인·앱 본문에 **「본문으로 건너뛰기」SkipLink**를 추가하고, **RFID 일괄 발송 중 ProgressBar**·**로딩 Skeleton**·**달력 작성 상태 마커** 컴포넌트를 도입했습니다. 직원 출근 달력은 **색상 외 텍스트 라벨**로 상태를 표시합니다.
- **내 화면/업무에 영향**: **키보드·스크린리더 사용자** — SideNav를 건너뛰고 본문으로 바로 이동 가능 · RFID 발송 중 **진행 표시** 확인
- **상태**: 완료

<details><summary>자세히</summary>

- `SkipLink` · `AppShell` · `PublicAuthLayout` · `ProgressBar`(`VisitRfidDiffComparePanel`) · `Skeleton` · `CalendarDayMarker`
- regression: `SkipLink.test.jsx` · `ProgressBar.test.jsx` · `Skeleton.test.jsx` · `CalendarDayMarker.test.jsx`

</details>

### 📝 대소문자·이중 HTML entity blocker ops 문서화
- **에이전트**: TWR
- **한 일**: develop HEAD 실측 후 FAQ·매뉴얼·관리/배포 가이드에 **live E2E 대소문자 named HTML entity·이중 인코딩(`&AMP;#x2d;`) bootstrap blocker decode** 를 반영했습니다.
- **내 화면/업무에 영향**: 없음 — 문서·운영 가이드만 갱신
- **상태**: 완료

<details><summary>자세히</summary>

- 실측: BE develop **`2768252`** · FE develop **`c779ca1`** — **133 route** · **106 page** · Flyway **V1–V196** · 모듈 **~97.4%**
- FAQ **Q839** · **Q837** 갱신 · USER_MANUAL §5-5 · ADMIN §1-4 · DEPLOYMENT §1-4

</details>

### ✅ live E2E — multi-pass double-encoded HTML entity decode (FE)
- **에이전트**: COD
- **한 일**: health/probe·알림 채널 readiness의 blocker 토큰이 **`&LT;`·`&QUOT;`·`&AMP;#x2d;`** 처럼 **대소문자 named entity** 또는 **이중 HTML 인코딩**이면 **최대 3회 multi-pass 디코딩** 후 bootstrap blocker로 판정합니다. BE `@2768252` 와 동일 규칙입니다.
- **내 화면/업무에 영향**: **센터장·sysadmin** — **`/organization/settings`**·**`/dashboard`** 알림 채널 패널이 gateway 이중 이스케이프 blocker에서도 누락 원인 표시. **IT·QA** live E2E gate
- **상태**: 완료

<details><summary>자세히</summary>

- `notificationChannelStatus.js` · `liveGlobalSetup.js` · `liveBackendProbe.js` · `liveConfig.js`
- regression: `notificationChannelStatus.test.js` · `liveE2eHarness.test.js`

</details>

### ✅ live E2E — case-insensitive named HTML entity decode (BE)
- **에이전트**: COD
- **한 일**: health/probe detail의 **`&LT;`/`&QUOT;`/`&AMP;`** 대소문자 named HTML entity와 **`&AMP;#x2d;`** 이중 인코딩을 디코딩한 뒤 bootstrap blocker로 판정합니다. FE `/gi` named-entity 규칙과 parity입니다.
- **내 화면/업무에 영향**: 없음 — **IT·QA** live E2E·operation gate만
- **상태**: 완료

<details><summary>자세히</summary>

- `LiveE2eOperationReadinessSupport.decodeHtmlEntityDetailToken` — `Pattern.CASE_INSENSITIVE` named entity
- regression: `LiveE2eOperationReadinessSupportTest` — uppercase gateway wrapper lock

</details>

### 📝 HTML entity blocker·RFID snake_case ops 문서화
- **에이전트**: TWR
- **한 일**: develop HEAD 실측 후 FAQ·매뉴얼·관리/배포 가이드에 **live E2E HTML entity bootstrap blocker decode** · **RFID snake_case·후보 파싱 보강** 을 반영했습니다.
- **내 화면/업무에 영향**: 없음 — 문서·운영 가이드만 갱신
- **상태**: 완료

<details><summary>자세히</summary>

- 실측: BE develop · FE develop — **133 route** · **106 page** · Flyway **V1–V196** · 모듈 **~97.4%**
- FAQ **Q837** · **Q838** · **Q832** 갱신 · USER_MANUAL §5-11 RFID · ADMIN §1-4 · DEPLOYMENT §1-4

</details>

### ✅ live E2E — HTML entity bootstrap blocker decode (FE)
- **에이전트**: COD
- **한 일**: health/probe·알림 채널 readiness의 blocker 토큰이 **`&#45;`·`&#x2d;`·`&lt;`·`&gt;`** 처럼 **HTML entity**로 오면 **구분자 분리 전에 디코딩**해 bootstrap blocker로 판정합니다. BE `@556eeff` 와 동일 규칙입니다.
- **내 화면/업무에 영향**: **센터장·sysadmin** — **`/organization/settings`**·**`/dashboard`** 알림 채널 패널이 entity-escaped blocker에서도 누락 원인 표시. **IT·QA** live E2E gate
- **상태**: 완료

<details><summary>자세히</summary>

- `liveGlobalSetup.js` · `liveBackendProbe.js` · `liveConfig.js` · `notificationChannelStatus.js`
- regression: `liveE2eHarness.test.js` · `notificationChannelStatus.test.js`

</details>

### ✅ live E2E — numeric HTML entity·RFID snake_case dispatch (BE)
- **에이전트**: COD
- **한 일**: health/probe detail의 **`&#45;`/`&#x2d;`/`&lt;`/`&gt;`** numeric·named HTML entity를 디코딩한 뒤 bootstrap blocker로 판정합니다. RFID 일괄 문자 API는 요청 body **`branch_id`·`year_month`·`client_ids`** snake_case도 수용합니다.
- **내 화면/업무에 영향**: **센터장·사회복지사(방문요양)** — Swagger·외부 연동이 snake_case로 보내도 일괄 발송 API가 거부되지 않음. **IT·QA** live E2E gate
- **상태**: 완료

<details><summary>자세히</summary>

- `LiveE2eOperationReadinessSupport.decodeHtmlEntityDetailToken`
- `VisitRfidCareProvisionDispatchRequest` — `@JsonAlias`(branch_id, year_month, client_ids)
- regression: `LiveE2eOperationReadinessSupportTest` · `VisitControllerRoutingTest`

</details>

### ✅ live E2E — HTML-escaped bootstrap blocker decode (BE)
- **에이전트**: COD
- **한 일**: health/probe 상세가 **`&quot;bootstrap-disabled&quot;`**·**`&amp;`** 등 **HTML-escaped JSON**이면 entity 디코딩 후 bootstrap blocker로 판정합니다. nested·URL·object-form 파싱 **앞단** 레이어입니다.
- **내 화면/업무에 영향**: 없음 — **IT·QA** live E2E·operation gate만
- **상태**: 완료

<details><summary>자세히</summary>

- `LiveE2eOperationReadinessSupport.decodeHtmlEntityDetailToken` — named entity 전개
- regression: `LiveE2eOperationReadinessSupportTest` — entity-escaped nested lock

</details>

### ✅ RFID 비교 — dispatch 후보·발송 건수 파싱 보강 (FE)
- **에이전트**: COD
- **한 일**: RFID 비교 응답의 **`dispatchCandidates`** 가 **snake_case**(`client_id`·`ltc_cert_no`)이거나 **직렬화 문자열**이어도 후보 목록을 표시합니다. 발송 성공 건수는 **`dispatched_count`** alias도 읽습니다.
- **내 화면/업무에 영향**: **센터장·사회복지사(방문요양)** — BE 응답 형식 차이로 **일괄 발송 후보가 비어 보이거나** 성공 건수 Alert가 **0으로 보이는** 현상 방지
- **상태**: 완료

<details><summary>자세히</summary>

- `VisitRfidDiffComparePanel` — `normalizeDispatchCandidates` · `resolveDispatchedCount`
- regression: `VisitRfidDiffComparePanel.test.jsx`

</details>

### 📝 RFID 일괄 SMS UI·중첩 JSON blocker ops 문서화
- **에이전트**: TWR
- **한 일**: develop HEAD 실측 후 FAQ·매뉴얼·관리/배포 가이드에 **RFID→급여제공내역 SMS 일괄 발송 UI** · live E2E **중첩 JSON·유니코드 bootstrap blocker** 를 반영했습니다.
- **내 화면/업무에 영향**: 없음 — 문서·운영 가이드만 갱신
- **상태**: 완료

<details><summary>자세히</summary>

- 실측: BE develop · FE develop — **133 route** · **106 page** · Flyway **V1–V196** · 모듈 **~97.4%**
- FAQ **Q832** 갱신 · **Q836** · USER_MANUAL §5-11 RFID · ADMIN §1-4 · DEPLOYMENT §1-4

</details>

### ✅ RFID 비교 → 급여제공내역 SMS 일괄 발송 UI (FE)
- **에이전트**: COD
- **한 일**: `/visits` **RFID 계획·태그 비교** 결과에 나온 발송 후보를 체크해 **급여제공내역 문자(kind 13)** 를 한 번에 보내는 화면을 연결했습니다. 연월·요약·전체 선택/해제까지 폼에서 처리합니다.
- **내 화면/업무에 영향**: **센터장·사회복지사(방문요양)** — 비교 후 **「급여제공내역 SMS 일괄 발송」** 으로 여러 수급자에게 바로 발송. **주야간보호·조용한 시간대·후보 없음** 은 기존과 같이 안내/거부
- **상태**: 완료

<details><summary>자세히</summary>

- `VisitRfidDiffComparePanel` · `dispatchRfidCareProvisionApi`
- `POST /api/v1/visits/imports/rfid/care-provision-dispatch`
- regression: `VisitRfidDiffComparePanel.test.jsx` · `billingGuardianPlatformServices.test.js`

</details>

### ✅ live E2E — 중첩 JSON·유니코드 bootstrap blocker (BE)
- **에이전트**: COD
- **한 일**: health/probe 상세가 **`operationBlockers={"nested":{"code":"bootstrap\\u002ddisabled"}}`** 처럼 **중첩 JSON·유니코드 이스케이프**여도 Jackson으로 펼친 뒤 bootstrap blocker로 판정합니다. URL 인코딩된 중첩 JSON도 동일합니다.
- **내 화면/업무에 영향**: 없음 — **IT·QA** live E2E·operation gate만
- **상태**: 완료

<details><summary>자세히</summary>

- `LiveE2eOperationReadinessSupport.expandJsonDetailToken` — Jackson `JsonNode` leaf 전개
- regression: `LiveE2eOperationReadinessSupportTest` — nested unicode · percent-encoded nested lock

</details>

### ✅ 디자인 시스템 Toast·컴포넌트 export (FE)
- **에이전트**: UXD
- **한 일**: 공통 **Toast** 컴포넌트(성공/정보=`status`, 위험/경고=`alert`)와 누락 export·모션 토큰을 보강했습니다.
- **내 화면/업무에 영향**: 없음 — 화면은 아직 Toast 미사용. 이후 알림 UX 기반만 마련
- **상태**: 완료

<details><summary>자세히</summary>

- `Toast.jsx` · `ToastProvider` · `useToast` · `--motion-duration` · `components.css` `.ds-toast*`

</details>

### 📝 URL-encoded blocker·channel-status ops 문서화
- **에이전트**: TWR
- **한 일**: develop HEAD 실측 후 FAQ·매뉴얼·관리/배포 가이드에 **live E2E URL-encoded bootstrap blocker decode** · **알림 채널 readinessBlockers URL decode** 를 반영했습니다.
- **내 화면/업무에 영향**: 없음 — 문서·운영 가이드만 갱신
- **상태**: 완료

<details><summary>자세히</summary>

- 실측: BE develop · FE develop — **133 route** · **106 page** · Flyway **V1–V196** · 모듈 **~97.4%**
- FAQ **Q834** · **Q835** · USER_MANUAL §1-3·§5-5 · ADMIN §1-4 · DEPLOYMENT §1-4

</details>

### ✅ live E2E — URL-encoded bootstrap blocker decode (BE)
- **에이전트**: COD
- **한 일**: health/probe **상세(detail) 토큰**이 **`%7B%22code%22%3A%22bootstrap-disabled%22%7D`** 처럼 **퍼센트 인코딩**으로 오면 **디코딩 후** bootstrap blocker로 판정합니다. object-form·composite 파싱 **앞단**에 URL decode 레이어를 둡니다.
- **내 화면/업무에 영향**: 없음 — **IT·QA** live E2E·operation gate만
- **상태**: 완료

<details><summary>자세히</summary>

- `LiveE2eOperationReadinessSupport.decodeUrlEncodedDetailToken` — `%`·`+` 포함 시 `URLDecoder.decode`
- regression: `LiveE2eOperationReadinessSupportTest` — percent-encoded object·composite lock

</details>

### ✅ 알림 채널 — URL-encoded readiness payload decode (FE)
- **에이전트**: COD
- **한 일**: **`GET /notifications/channel-status`** 응답의 **`readinessBlockers`**·**`missingTemplateCodes`**·직렬화 **templates** 문자열이 **URL 인코딩**되어 와도 **`normalizeNotificationChannelStatus`** 가 **디코딩·목록화**합니다. 패널에서 blocker가 **조용히 누락**되지 않습니다.
- **내 화면/업무에 영향**: **센터장·sysadmin** — **`/organization/settings`**·**`/dashboard`** **「알림 채널 준비 상태」** 패널이 **인코딩된 blocker 문자열**에서도 **누락 원인**을 표시
- **상태**: 완료

<details><summary>자세히</summary>

- `notificationChannelStatus.js` — `decodeCompositePayload` · `normalizeStringList`
- regression: `notificationChannelStatus.test.js` — encoded blocker·template alias lock

</details>

### 📝 RFID 급여제공내역 문자·object blocker ops 문서화
- **에이전트**: TWR
- **한 일**: develop HEAD 실측 후 FAQ·매뉴얼·관리/배포 가이드에 **RFID↔공단 비교 후 급여제공내역(kind 13) 일괄 발송 API** · compare **`dispatchCandidates`** · live E2E **object-form blocker** 파싱을 반영했습니다.
- **내 화면/업무에 영향**: 없음 — 문서·운영 가이드만 갱신
- **상태**: 완료

<details><summary>자세히</summary>

- 실측: BE develop · FE develop — **133 route** · **106 page** · Flyway **V1–V196** · 모듈 **~97.4%**
- FAQ **Q832** · **Q833** · USER_MANUAL §5-11 RFID · ADMIN §1-4 · DEPLOYMENT §1-4 · API_SPEC §9 Visits

</details>

### ✅ RFID 비교 후 급여제공내역 문자 일괄 발송 (BE)
- **에이전트**: COD
- **한 일**: RFID↔공단 계획 엑셀 비교 결과에 **인정번호로 해석한 발송 후보**를 붙이고, 방문요양 지점에서 **급여제공내역(kind 13)** 을 **여러 수급자에게 일괄** 보내는 API를 추가했습니다.
- **내 화면/업무에 영향**: **센터장·사회복지사(방문요양)** — 비교 API 응답에 후보 목록이 포함됩니다. **당일 FE 일괄 발송 UI 연결 완료**(상단 카드 참고). **주야간보호 지점에서는 일괄 API 거부**
- **상태**: 완료

<details><summary>자세히</summary>

- `POST /api/v1/visits/imports/rfid/compare` → **`dispatchCandidates[]`**
- `POST /api/v1/visits/imports/rfid/care-provision-dispatch` — `branchId` · `yearMonth` · `clientIds[]` · `summary`(선택)
- `CARE_PROVISION_RECORD` · **ezCare message_kind=13** · HOME_VISIT only · 조용한 시간대 가드 동일

</details>

### ✅ live E2E — object-form bootstrap blocker 파싱 (BE+FE)
- **에이전트**: COD
- **한 일**: health/probe blocker가 **`{"code":"bootstrap-disabled"}`** 같은 **객체·직렬화 JSON** 형태로 와도 bootstrap blocker로 **인식**하도록 보강했습니다. 게이트가 payload 형태 때문에 초록으로 잘못 통과하지 않습니다.
- **내 화면/업무에 영향**: 없음 — **IT·QA** live E2E·operation gate만
- **상태**: 완료

<details><summary>자세히</summary>

- BE `LiveE2eOperationReadinessSupport` — object `code=` / `code-` 마커
- FE `liveBackendProbe` · `liveConfig` — 직렬화 object·nested payload 정규화
- regression: `LiveE2eOperationReadinessSupportTest` · `liveE2eHarness.test.js`

</details>

### 📝 급여명세서 kind 22 발송 ops 문서화
- **에이전트**: TWR
- **한 일**: develop HEAD 실측 후 FAQ·매뉴얼·관리/배포 가이드에 **직원 급여명세서 알림톡(kind 22) 발송** · **템플릿 카탈로그 7/7** · **Q813 갱신**을 반영했습니다.
- **내 화면/업무에 영향**: 없음 — 문서·운영 가이드만 갱신
- **상태**: 완료

<details><summary>자세히</summary>

- 실측: BE develop · FE develop — **133 route** · **106 page** · Flyway **V1–V196** · 모듈 **~97.1%**
- FAQ **Q831** · **Q813** 갱신 · USER_MANUAL §4-7-0f·§4-7-4 · ADMIN §6-2-24b·§1-4 · DEPLOYMENT §1-4

</details>

### ✅ 급여명세서 kind 22 발송 UI (FE)
- **에이전트**: COD
- **한 일**: **간이지급명세서** 화면과 **직원 상세 알림 발송 패널**에 **급여명세서 알림톡** 발송을 연결했습니다. 미리보기와 **동일 금액**으로 kind 22를 보냅니다.
- **내 화면/업무에 영향**: **센터장·사회복지사** — **`/payroll/reports`** 미리보기 후 **「급여명세서 알림톡 발송」** · **`/staff/:id`** 패널에서 **발송 종류=급여명세서** 선택 후 발송
- **상태**: 완료

<details><summary>자세히</summary>

- `StaffPayrollReportsPage` · `StaffNotificationDispatchPanel` · `notifyStaffPayrollStatementApi`
- `POST /api/v1/staff/notifications/staff-payroll-statement`

</details>

### ✅ 급여명세서 kind 22 발송 API (BE)
- **에이전트**: COD
- **한 일**: ezCare **message_kind=22** 급여명세서를 **조용한 시간대 게이트**가 적용된 알림톡으로 보내는 API를 추가했습니다. M11 간이지급명세서 미리보기와 **동일 계산**으로 실지급액을 payload에 담습니다.
- **내 화면/업무에 영향**: **센터장·사회복지사** — 직원에게 **급여명세서 알림톡** 발송 가능(채널 준비·야간 제한은 기존 J03과 동일). **퇴사·비활성 직원**은 거부
- **상태**: 완료

<details><summary>자세히</summary>

- `POST /api/v1/staff/notifications/staff-payroll-statement`
- `StaffPayrollStatementNotificationService` · catalog **`dispatchImplementedCount=7`**
- 템플릿 **`STAFF_PAYROLL_STATEMENT`** · SMS 폴백 본문

</details>

### 📝 연계기록지 검증·리포트 조회·bootstrap 구분자 ops 문서화
- **에이전트**: TWR
- **한 일**: develop HEAD 실측 후 FAQ·매뉴얼·관리/배포 가이드에 **연계기록지 대상 기관 soft 길이 검증(QA-B451)** · **지점 리포트 「조회」 확정 필터(UXD-179)** · **live E2E bootstrap `:`·패딩 구분자(Q828)** 를 반영했습니다.
- **내 화면/업무에 영향**: 없음 — 문서·운영 가이드만 갱신
- **상태**: 완료

<details><summary>자세히</summary>

- 실측: BE develop **`34d4968`** · FE develop **`68cd253`** · **133 route** · **106 page** · Flyway **V1–V196** · 모듈 **~93.6%**
- FAQ **Q828** · **Q829** · **Q830** · Q826·Q822 갱신 · USER_MANUAL §4-7-3b · ADMIN · DEPLOYMENT §1-4

</details>

### ✅ 연계기록지 — 대상 기관 200자 필드 검증 복원 (FE)
- **에이전트**: COD
- **한 일**: 연계 대상 기관 입력에서 HTML **`maxLength` 잘림**을 제거하고, **저장 시 JS 검증**으로 200자 초과를 **필드 오류**로 안내하도록 되돌렸습니다. 서버·DB 한도(**Q822**·**V196**)와 동일하게 맞춥니다.
- **내 화면/업무에 영향**: **사회복지사·센터장** — 기관명이 200자를 넘으면 **입력 중 잘리지 않고**, **「초안 저장」** 시 **「200자 이하여야 합니다」** 안내가 표시됩니다
- **상태**: 완료

<details><summary>자세히</summary>

- `ClientLinkageRecordForm` — `maxLength` 제거 · `validate()` 유지
- `ClientLinkageRecordForm.test.jsx` BE 길이 parity regression

</details>

### ✅ 연계기록지 — 지점 리포트 「조회」 확정 필터 (FE)
- **에이전트**: UXD
- **한 일**: **「연계기록지 리포트」** 화면에서 상태·유형·검색을 바꿀 때마다 API를 호출하지 않고, **「조회」** 버튼(또는 Enter)으로 **확정한 조건만** 서버에 요청하도록 바꿨습니다.
- **내 화면/업무에 영향**: **센터장·사회복지사·본사 관리자** — 필터를 여러 번 바꿔도 목록이 **즉시 깜빡이지 않음** · 조건 확정 후 **「조회」** 로 갱신
- **상태**: 완료

<details><summary>자세히</summary>

- `ClientLinkageRecordsReportPage` — `filters` vs `appliedFilters` 분리
- `ClientLinkageRecordsReportPage.test.jsx` submit-on-query regression

</details>

### ✅ live E2E — bootstrap `:`·패딩 구분자 detail 파싱 (BE)
- **에이전트**: COD
- **한 일**: health/probe **상세 문자열**에서 **`bootstrap : disabled`** · **`bootstrap= disabled`** 처럼 **콜론(`:`)·등호(`=`)·공백 패딩**이 섞여도 bootstrap blocker를 **놓치지 않도록** 정규화했습니다.
- **내 화면/업무에 영향**: 없음 — **IT·QA** health/probe·live E2E 게이트만
- **상태**: 완료

<details><summary>자세히</summary>

- `LiveE2eOperationReadinessSupport.normalizeKeyValueToken` — `:`→`=` · 패딩 trim
- `LiveE2eOperationReadinessSupportTest` — colon·padded disabled/service-unavailable regression

</details>

### 📝 연계기록지 지점 리포트·V195/V196 ops 문서화
- **에이전트**: TWR
- **한 일**: develop HEAD 실측 후 FAQ·매뉴얼·관리/배포 가이드·API 명세에 **연계기록지 지점 통합 리포트**·**SideNav**·**V195/V196**·**live E2E V196 무결성 게이트**를 반영했습니다.
- **내 화면/업무에 영향**: 없음 — 문서·운영 가이드만 갱신
- **상태**: 완료

<details><summary>자세히</summary>

- 실측: BE develop · FE develop — **133 route** · **106 page** · Flyway **V1–V196** · 모듈 **~93.6%**
- FAQ **Q826** · **Q827** · Q819 갱신 · USER_MANUAL §4-7-3b · ADMIN · DEPLOYMENT §1-4 · API_SPEC §4-2

</details>

### ✅ 연계기록지 — 지점 통합 리포트 화면·메뉴 (FE)
- **에이전트**: UXD
- **한 일**: SideNav·이용자 컨텍스트에 **「연계기록지 리포트」**를 달고, 지점(또는 본사 전 지점) 범위로 상태·유형·검색 조회하는 화면을 연결했습니다. 이용자 상세 탭에는 **초안 관리** 구역·초안 목록 라벨을 보강했습니다.
- **내 화면/업무에 영향**: **센터장·사회복지사·본사 관리자** — **이용자 관리 → 연계기록지 리포트**(`/clients/linkage-records`)에서 여러 수급자 발송·초안을 한눈에 조회. 작성은 기존처럼 이용자 상세 탭
- **상태**: 완료

<details><summary>자세히</summary>

- 경로 **`/clients/linkage-records`** · `ClientLinkageRecordsReportPage`
- SideNav·`ClientsContextNav` **「연계기록지 리포트」**
- `ClientLinkageRecordsPanel` — **초안 관리** · 초안 목록 aria
- `fetchClientLinkageRecordsReportApi` → `GET /api/v1/clients/linkage-records`

</details>

### ✅ 연계기록지 — 지점 스코프 발송 리포트 API (BE)
- **에이전트**: COD
- **한 일**: 지점(또는 요청 branch) 안의 모든 수급자 연계기록지를 **상태·유형·검색어**로 페이지 조회하는 API를 추가했습니다. 행에 **수급자명**이 포함됩니다.
- **내 화면/업무에 영향**: **센터장·사회복지사·본사 관리자** — 지점 통합 리포트 화면의 데이터 소스. 이용자별 작성 API는 그대로
- **상태**: 완료

<details><summary>자세히</summary>

- `GET /api/v1/clients/linkage-records` — `branchId`·`status`·`linkageType`·`q`·`page`·`size`
- 권한: `hq_admin`·`branch_admin`·`social_worker`
- 응답 행: `clientId`·`clientName`·유형·기관·요약·상태·발송시각 등

</details>

### ✅ 연계기록지 — V195/V196 무결성·리포트 인덱스 (BE)
- **에이전트**: COD
- **한 일**: 지점 리포트용 **조직·지점 인덱스(V195)**와 길이 CHECK·수급자×지점 정합·org/branch 자동 복사·퇴소 purge 인덱스(**V196**)를 올렸습니다. health/live E2E에 **V196 준비됨** 신호와 누락 시 blocker를 붙였습니다.
- **내 화면/업무에 영향**: 없음 — DB·배포·IT 게이트. 현장은 글자 수·지점 정합이 DB에서도 한 번 더 막힘
- **상태**: 완료

<details><summary>자세히</summary>

- Flyway **V195** `idx_client_linkage_records_org_branch_status_created`
- Flyway **V196** length ≤200/≤5000 · client×branch FK · `set_org_branch` · purge index
- health **`v196ClientLinkageRecordsIntegrityCheckReady`** · blocker **`v196-client-linkage-records-integrity-missing`**
- **퇴소 후 INSERT는 허용**(전원·퇴소 후 연계 업무)

</details>

### 📝 live E2E bracket/quote blocker ops 문서화
- **에이전트**: TWR
- **한 일**: develop HEAD 실측 후 FAQ·관리/배포 가이드에 **live E2E 괄호·따옴표·JSON 배열 blocker 토큰** 파싱(BE+FE)을 반영했습니다.
- **내 화면/업무에 영향**: 없음 — 문서·운영 가이드만 갱신
- **상태**: 완료

<details><summary>자세히</summary>

- 실측: BE develop · FE develop — **132 route** · **105 page** · Flyway **V1–V194** · 모듈 **~93.6%**
- FAQ **Q824** · **Q825** · Q821·Q823 보강 · ADMIN · DEPLOYMENT §1-4·§11-3

</details>

### ✅ live E2E — bracket/quote operation blocker unwrap (FE)
- **에이전트**: COD
- **한 일**: health/probe **operation blocker**가 **JSON 배열 문자열**이거나 **괄호·따옴표로 감싼 토큰**이어도 FE live 하네스가 **안정적으로 파싱**합니다. BE composite detail 파싱과 **형태를 맞췄습니다**.
- **내 화면/업무에 영향**: 없음 — **IT·QA** `./scripts/run-live-e2e.sh` 게이트만
- **상태**: 완료

<details><summary>자세히</summary>

- `normalizeLiveOperationBlockers` · `unwrapLiveOperationBlockerToken` — `liveBackendProbe` · `liveConfig` · `liveGlobalSetup`
- `liveE2eHarness.test.js` regression

</details>

### ✅ live E2E — bracket/quote bootstrap blocker detail (BE)
- **에이전트**: COD
- **한 일**: health/probe **상세 문자열**의 bootstrap blocker 토큰이 **`[bootstrap-disabled]`**·**`'bootstrap=disabled'`**처럼 **괄호·따옴표로 감싸져 있어도** operation gate가 **놓치지 않도록** 파싱을 보강했습니다.
- **내 화면/업무에 영향**: 없음 — **IT·QA** health/probe 진단용
- **상태**: 완료

<details><summary>자세히</summary>

- `LiveE2eOperationReadinessSupport` — `normalizeDetailToken` · `tokenMatchesBootstrapPrefix`
- `LiveE2eOperationReadinessSupportTest` — bracket/quote composite lock

</details>

### 📝 연계기록지 길이 가드·live E2E 파싱 ops 문서화
- **에이전트**: TWR
- **한 일**: develop HEAD 실측 후 FAQ·매뉴얼·관리/배포 가이드에 **연계기록지 글자 수 이중 가드**·**live E2E env·boolean 정규화**·**bootstrap 쉼표/세미콜론 토큰**을 반영했습니다.
- **내 화면/업무에 영향**: 없음 — 문서·운영 가이드만 갱신
- **상태**: 완료

<details><summary>자세히</summary>

- 실측: BE develop · FE develop — **132 route** · **105 page** · Flyway **V1–V194** · 모듈 **~93.6%**
- FAQ **Q822** · **Q823** · Q819·Q821 보강 · USER_MANUAL §4-7-3b · ADMIN · DEPLOYMENT §1-3·§1-4 · **API_SPEC §4-2**

</details>

### ✅ 연계기록지 — 글자 수 서비스 가드 (BE)
- **에이전트**: COD
- **한 일**: 연계기록지 저장 시 **대상 기관 200자·요약 5000자** 한도를 **서비스 계층**에서도 다시 검사합니다. DTO 검증을 우회한 직접 호출도 막습니다.
- **내 화면/업무에 영향**: **센터장·사회복지사** — 한도 초과 저장 시 **「연계기관은(는) 200자 이하여야 합니다.」** / **「요약은(는) 5000자 이하여야 합니다.」** 안내
- **상태**: 완료

<details><summary>자세히</summary>

- `ClientLinkageRecordService.requireMaxLength` · DTO `@Size` + 서비스 이중 가드
- `ClientLinkageRecordServiceTest` — 기관·요약 over-max 거부

</details>

### ✅ live E2E — bootstrap 토큰 구분자 보강 (BE)
- **에이전트**: COD
- **한 일**: health/probe **상세 문자열**이 **쉼표·세미콜론**으로 이어져 있어도 `bootstrap-disabled` 등 blocker를 **놓치지 않도록** 토큰 분리를 넓혔습니다.
- **내 화면/업무에 영향**: 없음 — **IT·QA** operation gate 진단용
- **상태**: 완료

<details><summary>자세히</summary>

- `LiveE2eOperationReadinessSupport` — split `[\\s,;]+`
- `LiveE2eOperationReadinessSupportTest` — comma/semicolon composite detail lock

</details>

### ✅ live E2E — env·boolean 파싱 정규화 (FE)
- **에이전트**: COD
- **한 일**: `LIVE_E2E`·`LIVE_E2E_WRITE`·`LIVE_E2E_ALLOW_BOOTSTRAP_SUPPRESSION` 등 플래그와 health readiness **불리언 문자열**을 **앞뒤 공백·대소문자 무시**로 읽도록 맞췄습니다.
- **내 화면/업무에 영향**: 없음 — **IT·QA** live E2E 실행·게이트만
- **상태**: 완료

<details><summary>자세히</summary>

- `liveConfig.js` — `isTruthyLiveFlag` (trim + lower)
- `liveBackendProbe.js` — readiness `toBoolean` 정규화
- `liveE2eHarness.test.js` regression

</details>

### 📝 연계기록지 full-stack·bootstrap composite ops 문서화
- **에이전트**: TWR
- **한 일**: develop HEAD 실측 후 FAQ·매뉴얼·관리/배포 가이드에 **연계기록지 이용자 상세 탭 wire**·**V194**·**bootstrap composite blocker 진단**을 반영했습니다.
- **내 화면/업무에 영향**: 없음 — 문서·운영 가이드만 갱신
- **상태**: 완료

<details><summary>자세히</summary>

- 실측: BE develop · FE develop — **132 route** · **105 page** · Flyway **V1–V194** · 모듈 **~93.6%**
- FAQ **Q819** 갱신 · **Q821** · USER_MANUAL §4-7-3b · ADMIN · DEPLOYMENT §1-3·§1-4

</details>

### ✅ 연계기록지 — 이용자 상세 탭 FE wire (FE)
- **에이전트**: COD
- **한 일**: **이용자 상세 → 「연계기록지」탭**에 초안 작성·수정·발송·삭제·발송 리포트를 **백엔드 API와 연결**했습니다. 작성일·퇴소 후 이용계획은 **summary 접기**로 저장하고, 초안 재편집 시 **필드 복원**합니다.
- **내 화면/업무에 영향**: **센터장·사회복지사** — 이용자 상세에서 **연계기록지 초안·발송** 가능. SideNav **전용 메뉴·지점 통합 리포트**는 아직 없음
- **상태**: 완료

<details><summary>자세히</summary>

- `ClientLinkageRecordsPanel` · `ClientDetailPage` **「연계기록지」** 탭
- `fetch/create/update/dispatch/deleteClientLinkageRecordApi` · `linkageRecords.js`
- 유형 **병원·재가·이관** 3종(OTHER 없음) · 대상기관 200자 · 요약 5000자

</details>

### ✅ 연계기록지 — CRUD·발송 API (BE)
- **에이전트**: COD
- **한 일**: 케어포 **1-10 연계기록지**용 **6-endpoint CRUD + dispatch** API와 **Flyway V194**(`client_linkage_records`)를 추가했습니다. **초안만 수정·삭제** 가능하고, 발송 시 **DISPATCHED**로 전환됩니다.
- **내 화면/업무에 영향**: **센터장·사회복지사** — 전원·퇴소 후 외부기관 연계 기록을 **시스템에 저장·발송 완료 처리** 가능(이용자 상세 탭)
- **상태**: 완료

<details><summary>자세히</summary>

- `GET/POST/PATCH/DELETE /api/v1/clients/{clientId}/linkage-records` · `POST …/{recordId}/dispatch`
- `ClientLinkageRecordService` · V194 CHECK · RBAC **HQ/BRANCH/SOCIAL_WORKER**

</details>

### ✅ live E2E — bootstrap composite blocker 진단 (BE)
- **에이전트**: COD
- **한 일**: operation gate가 health/probe **상세 문자열에 여러 필드가 섞여 있어도** bootstrap blocker를 **안정적으로** 감지하도록 보강했습니다.
- **내 화면/업무에 영향**: 없음 — **IT·QA** health/probe 진단용
- **상태**: 완료

<details><summary>자세히</summary>

- `LiveE2eOperationReadinessSupport` — composite details **토큰화** 감지
- `LiveE2eOperationReadinessSupportTest` +51 lines

</details>

### 📝 연계기록지 UX 셸·bootstrap opt-in·일괄확정취소 a11y ops 문서화
- **에이전트**: TWR
- **한 일**: develop HEAD 실측 후 FAQ·매뉴얼·관리/배포 가이드에 **연계기록지 UX 셸**(메뉴 미연결)·**일괄 확정취소 접근성**·**live E2E bootstrap 억제 명시 opt-in**을 반영했습니다.
- **내 화면/업무에 영향**: 없음 — 문서·운영 가이드만 갱신
- **상태**: 완료

<details><summary>자세히</summary>

- 실측: BE develop · FE develop — **132 route** · **105 page** · Flyway **V1–V193** · 모듈 **~93.6%**
- FAQ · USER_MANUAL §4-7 · ADMIN · DEPLOYMENT §1-4·§11-3

</details>

### ✅ 연계기록지 — 작성·발송 리포트 UX 셸 (FE)
- **에이전트**: UXD | COD
- **한 일**: 케어포 **1-10 연계기록지**용 **작성 폼**·**발송 리포트 표** 컴포넌트 셸을 추가했습니다. 연계 유형(병원·재가·이관·기타)·대상 기관·요약·퇴소 후 이용계획·초안/발송 완료 배지가 준비됐고, **SideNav·페이지 라우트는 아직 연결되지 않습니다**.
- **내 화면/업무에 영향**: **센터장·사회복지사** — 메뉴에 **「연계기록지」가 아직 없음**. 전원·퇴소 후 외부기관 연계 기록은 **후속 화면 연결** 후 사용
- **상태**: 진행 중

<details><summary>자세히</summary>

- `ClientLinkageRecordForm` · `ClientLinkageRecordsReportPanel` · `config/linkageRecords.js`
- 예정 경로(미마운트): `/clients/:clientId/linkage-records` · `/clients/linkage-records`

</details>

### ✅ 방문일정 — 일괄 확정취소 접근성 보강 (FE)
- **에이전트**: UXD
- **한 일**: `/visits` **일괄 확정취소** 패널에 시작 버튼 **연월·종류 안내**(aria-label)·확인번호 **만료 시각(`<time dateTime>`)**·미리보기 로딩 **`aria-busy`** 를 보강했습니다.
- **내 화면/업무에 영향**: **센터장·사회복지사** — 키보드·스크린리더로 일괄 확정취소를 **더 쉽게** 수행
- **상태**: 완료

<details><summary>자세히</summary>

- `VisitBatchUnconfirmPanel` — challenge 만료 `<time>` · FE-16 class · Modal body busy

</details>

### ✅ live E2E — bootstrap 억제 시 명시 opt-in (FE)
- **에이전트**: COD
- **한 일**: live E2E 하네스가 **bootstrap 억제(effective만 초록)** 상태에서도 스위트를 돌리려면 **`LIVE_E2E_ALLOW_BOOTSTRAP_SUPPRESSION=1`** 을 **명시**해야 하도록 잠갔습니다. 조용히 통과하던 경로를 막습니다.
- **내 화면/업무에 영향**: 없음 — **IT·QA** live E2E 실행 설정만
- **상태**: 완료

<details><summary>자세히</summary>

- `liveConfig.js` — `isLiveBootstrapSuppressionAllowed`
- 미설정 시 skip 사유에 opt-in 안내 문구

</details>

### 📝 G21 월단위 일괄 확정취소 ops 문서화
- **에이전트**: TWR
- **한 일**: develop HEAD 실측 후 FAQ·매뉴얼·관리/배포 가이드에 **방문일정 월단위 일괄 확정취소**(4-digit 확인번호·6-cascade 경고·visits-only)를 반영했습니다.
- **내 화면/업무에 영향**: 없음 — 문서·운영 가이드만 갱신
- **상태**: 완료

<details><summary>자세히</summary>

- 실측: BE develop · FE develop — **132 route** · **105 page** · Flyway **V1–V193** · 모듈 **~93.6%**
- FAQ · USER_MANUAL §5-11 · ADMIN §10-12 · DEPLOYMENT §1-4

</details>

### ✅ 방문일정 — 월단위 일괄 확정취소 패널 (FE)
- **에이전트**: COD
- **한 일**: `/visits` 에 **「일괄 확정취소」** 패널을 추가했습니다. 미리보기에서 **4자리 확인번호**·**6-cascade 경고**를 확인한 뒤 해당 월 **CONFIRMED** 일정을 **DRAFT**로 되돌립니다.
- **내 화면/업무에 영향**: **센터장·사회복지사** — 방문 일정 화면에서 **월단위 확정 취소** 가능(이지케어 일정확정 패리티). **송영 배차 확정 취소**는 기존 루트 상세 그대로
- **상태**: 완료

<details><summary>자세히</summary>

- `VisitBatchUnconfirmPanel` · `fetchVisitBatchUnconfirmPreviewApi` · `batchUnconfirmVisitsApi`
- `VisitsPage` · challenge 재입력·실패 시 preview 자동 갱신

</details>

### ✅ 방문일정 — 월단위 일괄 확정취소 API (BE)
- **에이전트**: COD
- **한 일**: **월단위 CONFIRMED→DRAFT** 일괄 확정취소 API를 추가했습니다. **4자리 확인번호**(10분·1회 소비)·**6-cascade 경고 확인**·**visits-only** 범위를 서버에서 강제합니다.
- **내 화면/업무에 영향**: **센터장·사회복지사** — 잘못 확정한 달을 **한 번에 되돌릴** 수 있음. 청구·급여·임금 데이터는 **물리 삭제하지 않음**(경고만)
- **상태**: 완료

<details><summary>자세히</summary>

- `GET /api/v1/visits/batch-unconfirm-preview` · `POST /api/v1/visits/batch-unconfirm`
- `VisitBatchUnconfirmChallengeStore` · `scopeNote=VISIT_SCHEDULES_ONLY`

</details>

### 📝 J03 SMS·V193·bootstrap 진단·G2 시각 ops 문서화
- **에이전트**: TWR
- **한 일**: develop HEAD 실측 후 FAQ·매뉴얼·관리/배포 가이드에 **SMS 비긴급 즉시 발송**·**템플릿 kind 22 메타**·**V193 첨부 DB 제약**·**초안 작성/게시 시각**·**활성 지점 스코프**·**live E2E bootstrap 억제 신호**를 반영했습니다.
- **내 화면/업무에 영향**: 없음 — 문서·운영 가이드만 갱신
- **상태**: 완료

<details><summary>자세히</summary>

- 실측: BE develop · FE develop — **132 route** · **105 page** · Flyway **V1–V193** · 모듈 **~93.6%**
- FAQ **Q812**~**Q817** · Q809·Q810·Q807 교차 · ADMIN §1-4·§6-2-24h·§10-8 · USER_MANUAL §4-7-3a·§5-5 · DEPLOYMENT §1-3·§1-4

</details>

### ✅ live E2E — bootstrap blocker 우선·파생 노이즈 억제 (BE)
- **에이전트**: COD
- **한 일**: live E2E operation gate가 **bootstrap-disabled/service-unavailable**을 **우선 blocker**로 두고, bootstrap 문제가 있을 때 **파생 readiness 노이즈**를 억제해 probe 진단이 한눈에 보이게 했습니다.
- **내 화면/업무에 영향**: 없음 — **IT·QA** health/probe 진단용
- **상태**: 완료

<details><summary>자세히</summary>

- `LiveE2eOperationReadinessSupport` — blocker 우선순위·suppression lock
- 현장 앱 메뉴·업무 화면 변경 없음

</details>

### ✅ live E2E — effective gate bootstrap 억제 신호 (BE)
- **에이전트**: COD
- **한 일**: health·probe에 **`liveE2eEffectiveOperationSuppressedByBootstrap`** 필드를 추가했습니다. unenforced 환경에서 effective가 초록이어도 **bootstrap 때문에 억제됐는지** IT가 바로 구분할 수 있습니다.
- **내 화면/업무에 영향**: 없음 — **IT·QA** health/probe 진단용
- **상태**: 완료

<details><summary>자세히</summary>

- `GET /api/v1/health` · `GET …/system/live-e2e/probe`
- `liveE2eSuppressedBootstrapOperationBlockers`와 함께 사용 (Q810·Q817)

</details>

### ✅ 가정통신문 — 활성 지점 스코프 우선 (FE)
- **에이전트**: COD
- **한 일**: `/clients/home-newsletter` 가 **발송 이력·기관 공지 게시판** 조회 시 **현재 활성 지점(`activeBranchId`)** 을 먼저 씁니다. 지점을 바꾼 뒤에도 **선택한 지점 데이터**만 불러옵니다.
- **내 화면/업무에 영향**: **센터장·사회복지사** — 지점 전환 후 가정통신문 화면에서 **다른 지점 이력/게시판이 섞여 보이지 않음**
- **상태**: 완료

<details><summary>자세히</summary>

- `HomeNewsletterLaunchPage` — `resolveHomeNewsletterBranchId`
- `dispatch-history`·`facility-notices` API `branchId` 정합

</details>

### ✅ 기관 공지 — 초안은 「작성」·게시는 「게시」 시각 (FE)
- **에이전트**: COD
- **한 일**: 기관 공지 게시판·상세에서 **DRAFT** 행은 **「작성」** 시각, **PUBLISHED** 행은 **「게시」** 시각으로 라벨을 나눴습니다. 초안에 게시 시각이 붙어 보이던 혼동을 막습니다.
- **내 화면/업무에 영향**: **센터장·사회복지사** — `/clients/home-newsletter` 게시판 목록·상세에서 **초안/게시 구분**이 더 명확함
- **상태**: 완료

<details><summary>자세히</summary>

- `resolveFacilityNoticeTimestamp` · `<time dateTime>` (UXD-177 a11y 연계)
- DRAFT: `createdAt` · PUBLISHED: `publishedAt` 우선

</details>

### ✅ 알림 채널 — SMS 「비긴급 즉시 발송」화면 표시 (FE)
- **에이전트**: COD
- **한 일**: 조직 설정·대시보드 **알림 채널 준비 상태** 패널에 **「비긴급 SMS 즉시 발송」** 가능·제한됨 배지를 추가했습니다. 알림톡·이메일과 같이 **3채널** 조용한 시간대 제한을 화면에서 확인합니다.
- **내 화면/업무에 영향**: **센터장·본사 관리자** — `/organization/settings`·`/dashboard` readiness에서 SMS도 **가능/제한됨** 표시. 발송 버튼 비활성 규칙은 그대로
- **상태**: 완료

<details><summary>자세히</summary>

- `NotificationChannelReadinessPanel` · `normalizeNotificationChannelStatus`
- 템플릿 카탈로그 **kind 22(급여명세서)** 라벨 메타 추가 — **발송 UI 미연동**

</details>

### ✅ 알림 채널 — SMS 「지금 발송 가능」·health 미러 (BE)
- **에이전트**: COD
- **한 일**: 알림 채널 준비 API·health에 **`liveSmsDispatchReady`**·**`nonEmergencySmsDispatchAvailableNow`** 를 추가했습니다. Solapi SMS 폴백 준비와 조용한 시간대 제한을 **알림톡·이메일과 동일 패턴**으로 봅니다.
- **내 화면/업무에 영향**: **센터장·본사 관리자·IT** — readiness·health에서 **SMS도 지금 보낼 수 있는지** 구분 가능. 실제 발송 차단 규칙은 기존과 동일
- **상태**: 완료

<details><summary>자세히</summary>

- `GET /api/v1/notifications/channel-status` · `GET /api/v1/health`
- `notificationLiveSmsDispatchReady` · `notificationNonEmergencySmsDispatchAvailableNow`

</details>

### ✅ 템플릿 카탈로그 — ezCare message_kind 22 메타 (BE)
- **에이전트**: COD
- **한 일**: 알림 템플릿 카탈로그에 **급여명세서(message_kind=22)** 항목을 **enum/메타만** 추가했습니다. **발송 API·UI는 아직 없음** — v2+ SMS 7종 계획용입니다.
- **내 화면/업무에 영향**: **센터장** — 조직 설정 readiness 패널 카탈로그 표에 **「급여명세서」** 행이 보이나 **발송 대기(미구현)** 로 표시됨
- **상태**: 완료

<details><summary>자세히</summary>

- `STAFF_PAYROLL_STATEMENT` · `dispatchImplemented=false`
- 카탈로그 **7종** · 발송 구현 **6/6** 유지

</details>

### ✅ G2 기관 공지 첨부 링크 DB 제약 (BE)
- **에이전트**: DBA
- **한 일**: Flyway **V193** 이 `facility_notices.attachment_url` 에 **http(s)://·500자 이하** CHECK를 추가했습니다. 앱 검증을 우회한 raw SQL 삽입도 막아 **보호자 대상 XSS·피싱** 위험을 줄입니다.
- **내 화면/업무에 영향**: 없음 — 정상 http(s) 첨부는 그대로. 잘못된 스킴은 **저장 단계에서 거부**(기존 앱 검증과 동일)
- **상태**: 완료

<details><summary>자세히</summary>

- `V193__facility_notices_attachment_url_format.sql`
- `chk_facility_notices_attachment_url_format` — 앱 `FacilityNoticeService` 계약과 동일

</details>

### 📝 가정통신문 조용한 시간대 운영 준비 ops 문서화
- **에이전트**: TWR
- **한 일**: develop HEAD 실측 후 FAQ·매뉴얼·관리/배포 가이드에 **가정통신문 launch/health 발송 준비가 조용한 시간대를 반영**하는 내용과 **health의 비긴급 발송 가능 필드**를 반영했습니다.
- **내 화면/업무에 영향**: 없음 — 문서·운영 가이드만 갱신
- **상태**: 완료

<details><summary>자세히</summary>

- 실측: BE/FE develop — **132 route** · **105 page** · Flyway **V1–V192** · 모듈 **~93.6%**
- FAQ Q789 정정 · **Q811** · Q809 교차 · ADMIN §1-4·§6-2-24h · USER_MANUAL §1-3·§4-7-3a · DEPLOYMENT §1-3·§1-4

</details>

### ✅ 가정통신문 — 조용한 시간대에 「준비됨」 오표시 방지 (FE)
- **에이전트**: COD
- **한 일**: `/clients/home-newsletter` **운영 준비**가 서버의 조용한 시간대 발송 가능 여부를 따릅니다. 밤에는 **후속**과 **「조용한 시간대(비긴급 발송 제한)」** 안내가 보입니다.
- **내 화면/업무에 영향**: **센터장·사회복지사** — SMTP는 켜져 있어도 밤에는 「발송 준비됨」으로 보이지 않아, 아침에 다시 확인하면 됩니다
- **상태**: 완료

<details><summary>자세히</summary>

- `HomeNewsletterLaunchPage` · `normalizeHomeNewsletterLaunch` / health readiness
- blocker 코드 `quiet-hours-active` · SMTP 미설정과 구분

</details>

### ✅ 가정통신문 — 발송 준비에 조용한 시간대 반영 (BE)
- **에이전트**: COD
- **한 일**: 가정통신문 launch·health의 **발송 준비**가 「SMTP 설정됨」이 아니라 **지금 비긴급 이메일을 보낼 수 있는지**를 봅니다. 야간이면 blocker **`quiet-hours-active`** 와 안내 문구가 붙습니다. health에는 알림톡·이메일 **지금 발송 가능**·**quietHoursActive** 필드도 추가했습니다.
- **내 화면/업무에 영향**: **센터장·사회복지사·IT** — 밤에 SMTP만 보고 「준비됨」으로 착각하지 않음. 실제 발송 거부는 기존과 동일
- **상태**: 완료

<details><summary>자세히</summary>

- `GET …/home-newsletter/launch` · `GET /api/v1/health` (`homeNewsletterDispatchReady` · `homeNewsletterReadinessBlockers`)
- health 추가: `notificationNonEmergency*DispatchAvailableNow` · `notificationQuietHoursActive`

</details>

### 📝 알림 가용성·bootstrap 진단·공지 분류 ops 문서화
- **에이전트**: TWR
- **한 일**: develop HEAD 실측 후 FAQ·매뉴얼·관리/배포 가이드에 **조용한 시간대「지금 발송 가능」API·화면**·**게이트 미강제 시에도 억제 bootstrap 진단 유지**·**기관 공지 분류 NOTICE/RESOURCE만**을 반영했습니다.
- **내 화면/업무에 영향**: 없음 — 문서·운영 가이드만 갱신
- **상태**: 완료

<details><summary>자세히</summary>

- 실측: BE develop · FE develop — **132 route** · **105 page** · Flyway **V1–V192** · 모듈 **~93.6%**
- FAQ **Q808**~**Q810** · Q799·Q802·Q797 정정 · ADMIN §1-4·§6-2-24h·§10-8 · USER_MANUAL §1-3·§4-7-3a·§5-5 · DEPLOYMENT §1-3·§1-4

</details>

### ✅ 알림 채널 — 「비긴급 즉시 발송」화면 표시 (FE)
- **에이전트**: COD
- **한 일**: 조직 설정·대시보드 **알림 채널 준비 상태** 패널에 **「비긴급 알림톡/이메일 즉시 발송」** 가능·제한됨 배지를 넣었습니다. 설정 live 준비와 조용한 시간대 제한을 화면에서 구분합니다.
- **내 화면/업무에 영향**: **센터장·본사 관리자** — `/organization/settings`·`/dashboard` readiness에서 야간이면 **제한됨**으로 보임. 청구 발송 버튼 비활성 규칙은 그대로
- **상태**: 완료

<details><summary>자세히</summary>

- `NotificationChannelReadinessPanel` · `normalizeNotificationChannelStatus` 폴백
- 라벨: **가능** / **제한됨** · aria-label 「비긴급 발송 가능 여부」

</details>

### ✅ 알림 채널 — 조용한 시간대 「지금 발송 가능」구분 (BE)
- **에이전트**: COD
- **한 일**: 알림 채널 준비 API가 **설정상 live 준비**와 **지금(비긴급) 발송 가능**을 나눠 보여 줍니다. 조용한 시간대면 `QUIET_HOURS_ACTIVE` blocker가 붙고, 긴급 알림은 기존처럼 우회합니다.
- **내 화면/업무에 영향**: **센터장·본사 관리자·IT** — readiness 패널·`channel-status` 스모크에서 「설정은 됐는데 지금 밤에만 막힘」을 구분하기 쉬움. 청구·보호자 수동 발송 차단 규칙은 그대로
- **상태**: 완료

<details><summary>자세히</summary>

- `GET /api/v1/notifications/channel-status`
- 신규: `nonEmergencyAlimtalkDispatchAvailableNow` · `nonEmergencyEmailDispatchAvailableNow`
- `readinessBlockers` 에 `QUIET_HOURS_ACTIVE` (야간) · `live*DispatchReady` 의미는 설정 readiness 유지

</details>

### ✅ live E2E — 게이트 미강제여도 억제 bootstrap 진단 유지 (BE)
- **에이전트**: COD
- **한 일**: live E2E **bootstrap 강제 검사가 꺼진** 환경에서도 **`bootstrap-disabled` / `bootstrap-service-unavailable`** 진단을 **억제 목록에 남깁니다**. effective는 초록이어도 IT가 「bootstrap만 꺼짐」을 놓치지 않습니다.
- **내 화면/업무에 영향**: 없음 — **IT·QA** 의 health/probe·live E2E harness 진단용
- **상태**: 완료

<details><summary>자세히</summary>

- health · `GET …/system/live-e2e/probe` — `liveE2eSuppressedBootstrapOperationBlockers` 폴백 유지
- 현장 앱 메뉴·업무 화면 변경 없음

</details>

### ✅ 기관 공지 — 게시 분류 NOTICE/RESOURCE만 (FE)
- **에이전트**: COD
- **한 일**: 기관 공지·자료실 저장 시 게시 분류를 **공지(NOTICE)·자료실(RESOURCE)만** 받도록 막고, 잘못된 값이면 저장 전에 **「게시 분류를 선택하세요」** 필드 오류를 보여 줍니다. 복제 시 알 수 없는 분류는 **공지**로 보정합니다.
- **내 화면/업무에 영향**: **센터장·사회복지사** — `/clients/home-newsletter` 게시판에서 분류가 비어 있거나 잘못된 초안을 저장하려 하면 API 호출 전에 안내됨
- **상태**: 완료

<details><summary>자세히</summary>

- `isEditableFacilityNoticeCategory` · Field `noticeCategory` error
- 복제 payload: 비지원 분류 → `NOTICE`

</details>

### 📝 기관 공지 첨부 정리·복제 후 수정 ops 문서화
- **에이전트**: TWR
- **한 일**: develop HEAD 실측 후 FAQ·매뉴얼·관리/배포 가이드에 **첨부 링크 서버 http(s) 검증**·**복제 시 불안전 첨부 제거 후 수정 폼 연결**·**상세 불안전 링크 차단**을 반영했습니다.
- **내 화면/업무에 영향**: 없음 — 문서·운영 가이드만 갱신
- **상태**: 완료

<details><summary>자세히</summary>

- 실측: BE develop · FE develop — **132 route** · **105 page** · Flyway **V1–V192** · 모듈 **~93.6%**
- FAQ Q804 정정 · **Q807** · ADMIN §6-2-24h · USER_MANUAL §4-7-3a · DEPLOYMENT §1-4

</details>

### ✅ G2 기관 공지 첨부 링크 서버 검증 (BE)
- **에이전트**: COD
- **한 일**: 기관 공지·자료실을 저장할 때 첨부 링크가 **http://·https://로 시작하는지**와 **길이(500자)**를 **서버에서도** 검사합니다. `ftp://` 등 잘못된 주소는 저장되지 않습니다.
- **내 화면/업무에 영향**: **센터장·사회복지사** — `/clients/home-newsletter` 게시판에서 첨부 링크를 잘못 넣으면 화면뿐 아니라 **저장 API에서도** 거부되고 안내됨
- **상태**: 완료

<details><summary>자세히</summary>

- create/PATCH — 공백 trim · 빈 값→첨부 없음 · 비 http(s)·초과 길이 → 업무 규칙 오류

</details>

### ✅ G2 기관 공지 복제 시 첨부 정리 · 바로 수정 (FE)
- **에이전트**: COD
- **한 일**: **「초안으로 복제」** 때 불안전한 첨부는 **제거한 뒤 복제를 이어가고**, 새 초안이 **수정 폼에 바로 열리도록** 바꿨습니다. 상세 보기에서 불안전한 첨부 링크는 **클릭을 막고** 안내만 보여 줍니다.
- **내 화면/업무에 영향**: **센터장·사회복지사** — 복제 후 곧바로 제목·본문·첨부 수정 가능. 예전에 막히던 「잘못된 첨부 때문에 복제 실패」가 줄고, 위험 링크는 상세에서 열리지 않음
- **상태**: 완료

<details><summary>자세히</summary>

- 복제: 불안전 첨부 strip · 안내 문구 · 편집 폼 핸드오프
- 상세: 안전 URL만 「첨부 자료 열기」 · 그 외는 차단 안내

</details>

---

## 2026-07-14

### 📝 기관 공지 복제·상세·보호자 자격 공백 ops 문서화
- **에이전트**: TWR
- **한 일**: develop HEAD 실측 후 FAQ·매뉴얼·관리/배포 가이드에 **기관 공지 초안 복제·게시 상세·메뉴 `#facility-notices` 바로가기**·**첨부 URL http(s) 검증**·**live E2E 보호자 자격 공백=미설정**을 반영했습니다.
- **내 화면/업무에 영향**: 없음 — 문서·운영 가이드만 갱신
- **상태**: 완료

<details><summary>자세히</summary>

- 실측: BE develop HEAD · FE develop HEAD — **132 route** · **105 page** · Flyway **V1–V192** · 모듈 **~93.6%**
- FAQ · ADMIN §6-2-24h · USER_MANUAL §4-7-3a · DEPLOYMENT §1-3·§1-4·체크리스트

</details>

### ✅ G2 기관 공지 초안 복제 · 첨부 URL http(s) 가드 (FE)
- **에이전트**: COD
- **한 일**: 게시된(또는 기존) 기관 공지를 **「초안으로 복제」** 하면 **새 DRAFT**가 만들어져 다시 고친 뒤 재게시할 수 있습니다. 첨부 URL은 **http://·https://만** 허용합니다.
- **내 화면/업무에 영향**: **센터장·사회복지사** — `/clients/home-newsletter` 게시판·상세에서 **초안으로 복제**. 잘못된 첨부 스킴이면 저장이 막히고 안내됨 (복제 시 첨부는 **2026-07-15**에 제거 후 이어가도록 개선)
- **상태**: 완료

<details><summary>자세히</summary>

- UI: **「초안으로 복제」** · 한국어 분류/상태 라벨
- 첨부: `javascript:` 등 비 http(s) → 필드 오류

</details>

### ✅ G2 기관 공지 상세 보기 · 메뉴 바로가기 (FE)
- **에이전트**: COD
- **한 일**: 게시된 공지를 **상세 보기**로 열고, SideNav·이용자 메뉴에 **「기관 공지·자료실」** 링크(`/clients/home-newsletter#facility-notices`)를 넣었습니다.
- **내 화면/업무에 영향**: **센터장·사회복지사** — 메뉴에서 게시판 카드로 바로 이동 · 게시 글 **보기**로 본문·첨부 링크 확인
- **상태**: 완료

<details><summary>자세히</summary>

- 상세: `GET …/facility-notices/{id}` · 닫기 · 게시글에서 복제 안내
- nav: SideNav · `ClientsContextNav` · 관련 표면 링크 `#facility-notices`

</details>

### ✅ G2 가정통신문·기관 공지 화면 접근성 (FE)
- **에이전트**: UXD
- **한 일**: 초안·기관 공지·발송 이력 표에 **스크린리더용 caption**, 폼·행 버튼 **aria-label**, 상태·분류를 **배지·한글 라벨**로 보이게 하고, 미리보기용 **`.ds-pre`** 스타일을 정의했습니다.
- **내 화면/업무에 영향**: **스크린리더·키보드 사용자** — `/clients/home-newsletter` 표·버튼 이해가 쉬워짐. 시각적으로는 상태/분류가 한글·배지로 정리됨
- **상태**: 완료

<details><summary>자세히</summary>

- 표 caption · compose/notice 폼 landmark · 행별 버튼 aria-label
- StatusBadge(초안/게시됨) · 공지/자료 라벨 · `.ds-pre`

</details>

### ✅ live E2E 보호자 자격 공백을 기본값으로 치지 않음 (BE)
- **에이전트**: COD
- **한 일**: 보호자 live E2E env가 **비어 있으면 「기본 시드 사용」이 아니라 「미설정」**으로 봅니다. staff bootstrap에 보호자 토큰을 조용히 붙이지 않고 fail-closed 합니다.
- **내 화면/업무에 영향**: 없음 — **IT·live E2E** 진단만. 보호자 env를 비우면 **missing** blocker·bootstrap enrichment 생략
- **상태**: 완료

<details><summary>자세히</summary>

- `usesDefaultGuardianCredentials` — 양쪽 값이 있고 시드와 같을 때만 default
- blank/partial → missing · staff bootstrap enrichment 도 보호자 자격이 없으면 거부

</details>

### ✅ M12 재무회계 BPO 서비스 Spring 주입 수정 (BE)
- **에이전트**: COD
- **한 일**: 재무회계 BPO 서비스의 **공개 생성자에 Spring 주입 표시**를 넣어, 테스트용 생성자가 여러 개여도 **서버 기동이 막히지 않게** 고쳤습니다.
- **내 화면/업무에 영향**: 없음 — 배포·기동 안정화. `/accounting` 업무 절차는 동일
- **상태**: 완료

<details><summary>자세히</summary>

- `AccountingBpoService` 공개 생성자 `@Autowired` — `spring-boot:run` 회귀

</details>

### 📝 J03 채널 별칭 · G2 상세 재조회 · M12 SSO 오류 ops 문서화
- **에이전트**: TWR
- **한 일**: develop HEAD 실측 후 FAQ·매뉴얼·관리/배포 가이드에 **channel-status API_SPEC 별칭**·**기관 공지 수정 시 GET 상세**·**재무회계 SSO 429/비허용 URL 화면 안내** 를 반영했습니다.
- **내 화면/업무에 영향**: 없음 — 문서·운영 가이드만 갱신
- **상태**: 완료

<details><summary>자세히</summary>

- 실측: BE develop · FE develop — **132 route** · **105 page** · Flyway **V1–V192** · 모듈 **~93.6%**
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
