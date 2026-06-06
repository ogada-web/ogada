<!-- doc:owner=BNK doc:audience=PLN updated=2026-06-06T18:00:00+09:00 -->
# 경쟁사 벤치마크 보고서 (BENCHMARK_REPORT.md)

> **작성**: benchmark_researcher 에이전트 `[BNK]`  
> **최종 갱신**: 2026-06-06 (3차 재검증)  
> **상태**: 3차 상세 조사 반영 — 공식 사이트·매뉴얼·공지·앱스토어·2026 롱텀 개편  
> **조사 범위**: 주간보호(주·야간보호) 중심 — 이용자·출석·건강·청구·대시보드·보호자·다지점·SaaS

---

## 1. 목적·방법

국내 주간보호·요양기관 관리 SaaS/ERP의 **서비스 제공 항목·기능·UX·가격·청구 흐름**을 공개 자료로 재조사해, ogada(`docs/REQUIREMENTS.md`, `docs/USER_STORIES.md`) 대비 **갭·차별화·MVP 우선순위**를 planner가 반영할 수 있게 정리한다.

| 항목 | 내용 |
|------|------|
| 조사일 | **2026-06-06** (3차 재검증 — 본 문서 갱신) |
| 1차 조사 | 2026-06-05 (planner, REQUIREMENTS §1-5) |
| 2차 조사 | 2026-06-06 (benchmark_researcher, 초판) |
| 근거 유형 | 공식 홈페이지, PDF 매뉴얼, 교육 공지, FAQ, 앱스토어, 롱텀 개편 공지 |
| 미확인 | 로그인 후 메뉴 전체·비공개 API·다지점 HQ 화면 — 「가정」으로 표기 |

---

## 2. 조사 대상 요약

| 서비스 | URL | 유형 | 주야간보호 | 시장 포지션 (공개 자료) |
|--------|-----|------|-----------|------------------------|
| **케어포** | https://www.carefor.co.kr/ | 민간 ERP (웹+앱) | ✅ 전용 모듈 | 사용자 지정 1순위. 전국 **14,000+** 기관(2024 공지·소개). 평가·청구·보호자앱 |
| **이지케어** | https://ezcare.easyms.co.kr/ | 민간 ERP (웹+앱) | ✅ 지원·확대 | 재가 ERP **점유 1위** 주장. 홈페이지 실시간 **9,210** 재가기관(2026.06.06). 방문+주간보호+**재무회계** |
| **엔젤시스템** | https://www.lcms.or.kr/ / https://www.silverangel.kr/ | 민간 ERP (웹+앱) | ✅ 지원 | 시설·주야간 통합사례관리. **CMS 본인부담 자동이체**. 평가·필수교육 연동 |
| **롱텀(공단)** | https://www.longtermcare.or.kr/ | 공단 공식 | ✅ 급여청구 | **무료**. 공단 급여청구·심사·입퇴소신고. **운영·본인부담·보호자 UX 약함** |

---

## 3. 경쟁사별 상세

### 3-1. 케어포 (Carefor)

| 항목 | 내용 |
|------|------|
| **조사일** | 2026-06-06 |
| **제공 형태** | 웹 브라우저 + **직원 모바일 앱** + **보호자 앱(가족돌봄앱)** |
| **온보딩** | 홈페이지 **셀프 회원가입** → 기관 정보(사업자·장기요양기관번호) 입력 → **1개월 무료** ([이용요금](https://www.carefor.co.kr/price/cost.php)) |
| **가격 (주야간)** | 수급자 수 구간별 **월 33,000원(부가세 포함)** — 10인 이하~131인 이상 동일 구간 요금표. 6개월 결제 +1개월, 12개월 +2개월 ([이용요금](https://www.carefor.co.kr/price/cost.php)) |

#### 주야간보호 모듈 (매뉴얼·소개 페이지)

[주요프로그램 구성](https://www.carefor.co.kr/intro_visit/composition.php), [주야간 사용메뉴얼 PDF](https://www.carefor.co.kr/ct_att/contents_article/0/202206/12/Dov8rzFqBv.pdf) 기준:

| # | 모듈 | 설명 |
|---|------|------|
| 1 | 수급자 관리 | 기초평가·급여계약·인정유효기간 |
| 2 | 이동 서비스 관리 | 픽업·드롭 구간, 이동서비스비 |
| 3 | 요양 급여제공 | 일일 요양 기록 |
| 4 | 간호/물리 급여제공 | 간호·물리치료 기록 |
| 5 | 프로그램 급여제공 | 프로그램·만족도·사진 |
| 6 | 위생·안전 점검 | 점검·체크리스트 |
| 7 | **본인부담금 관리** | 청구서·수납·선납·발송 |
| 8 | 직원 관리 | 자격·배치 |
| 9 | 기초설정·운영관리 | 기관·IP제한 등 |
| 10 | 부가서비스 | 보호자앱·홈페이지·CMS 등 |
| 11 | 직원 급여관리 | 급여 계산 |
| 12 | 수입·지출 관리 | 기관 회계 |

#### 청구·정산 (벤치마킹 핵심 — ogada와 동일 2단계)

[교육 공지 calmgno=43619](https://www.carefor.co.kr/cs/view_notice.php?calmgno=43619), [매뉴얼 7장](https://www.carefor.co.kr/ct_att/contents_article/0/202206/12/Dov8rzFqBv.pdf):

```
[일상] 케어포 — 출석·급여제공·일정
         ↓
[① 공단] 장기요양정보시스템(롱텀) — 입퇴소신고·청구서 전송·심사
         ↓
[② 연동] 공단 「청구내역상세」·「급여계약통보서」 엑셀 다운로드 → 케어포 업로드
         ↓
[③ 본인부담금] 케어포 — 개별/일괄 청구서·보호자앱 발송·CMS/간편결제(부가)
```

- 공단과 **실시간 API 직접 연동**보다 **엑셀 기반 연동** + 공단 포털 병행이 표준.
- 수급분류: 매뉴얼·FAQ 기준 **일반(15%) / 경감·의료(7.5%) / 기초(0%)** — ogada `copay_rates`와 대응.
- **NHIS 엑셀 import 상세** ([방문요양 매뉴얼 PDF](https://www.carefor.co.kr/pdf_manual/visitcare.pdf) §4-1, 주야간 동일 패턴 **가정**):
  - 메뉴: `4-1. 청구내역상세 엑셀업로드(공단연동)`
  - 업로드 후 수급자별 **공단 청구 건수**·월별 급여제공내역 조회
  - 공단 엑셀 **첫 열 `처리상태` 추가** 시 파서 실패 사례 ([공지 calmgno=44438](https://www.carefor.co.kr/cs/view_notice.php?calmgno=44438)) — ogada import 파서는 **선행 컬럼 스킵·정규화** 필요

#### 출석·현장 UX

| 방식 | 지원 | 근거 |
|------|------|------|
| 웹 수기 입력 | ✅ | 매뉴얼 전반 |
| **NFC 태그** (직원 앱) | ✅ | [App Store](https://apps.apple.com/us/app/%EC%BC%80%EC%96%B4%ED%8F%AC/id1220736809): 출퇴근·야간점검·현장 입력 |
| **보호자/이용자 QR 셀프** | ❌ (공개 자료 없음) | ogada B방식과 **다름** |
| RFID 급여제공 태그 | △ (방문·시설 중심) | 가족노트 등 제3자 문서에 RFID↔청구내역 비교 언급 — 주야간 전용 QR 아님 |

#### 보호자·모바일

- **가족돌봄앱**: 급여비용명세서·급여제공기록지·사진·동영상 조회 ([intro_visit](https://www.carefor.co.kr/intro_visit/composition.php)).
- 부가: **CMS·간편결제**, 기관 홈페이지·알림마당 연동.

#### 평가·규정 대응

- **2026 공단 평가지표** 반영 업데이트·교육·자료실 ([공지 calmgno=46130](https://www.carefor.co.kr/cs/view_notice.php?calmgno=46130)).
- 사례관리 회의록·참여 직종·대화체 기록 등 **평가 항목 전용 UI** (YouTube 매뉴얼 2025.12).

#### 다지점·SaaS

| 항목 | 판단 |
|------|------|
| 계정·기관 매핑 | △ **가정**: 1회원가입 = **장기요양기관번호 11자리 1개** ([가입 흐름](https://www.carefor.co.kr/price/cost.php), [기관기호 FAQ PDF](https://www.carefor.co.kr/ct_att/contents_article/0/notice/639bdbb2b41fe)). 지점마다 **별도 기관번호·별도 계정** 운영이 일반적 |
| 법인 다지점 HQ 대시보드 | △ 공개 자료 **미확인** — 서드파티 블로그에 「다기관 통합」 언급 있으나 **공식 메뉴·매뉴얼 근거 없음** |
| ogada 대비 | ogada **`platform_admin` + Organization-Branch + `/dashboard/hq`** 가 법인 단위 다지점에 **명시적** — 영업 차별 축 유지 |

#### 차별점·한계 (ogada 관점)

| 강점 | 한계 |
|------|------|
| 평가·서식·법령 변경 **즉시 반영** | 기능 범위 **과대** — MVP 범위 초과(회계·직원급여·평가 전항목) |
| 보호자앱·CMS **성숙** | 출석은 **NFC/수기** — 보호자 QR 셀프 미확인 |
| 청구 2단계·엑셀 연동 **업계 표준** | 셀프 가입 — B2B **플랫폼 개통**(`platform_admin`) 모델과 다름 |

---

### 3-2. 이지케어 (EasyCare)

| 항목 | 내용 |
|------|------|
| **조사일** | 2026-06-06 |
| **URL** | https://ezcare.easyms.co.kr/ |
| **제공 형태** | **웹 SaaS** + **EZCARE 모바일 앱** (2025~2026 출시, [App Store](https://apps.apple.com/kr/app/%EC%9D%B4%EC%A7%80%EC%BC%80%EC%96%B4-ezcare/id6740553966)) |
| **규모** | 홈페이지 실시간 **9,210** 재가기관 (2026.06.06, [ezcare.easyms.co.kr](https://ezcare.easyms.co.kr/)); 소개页 **8,931**(2026.03, [ezCare.html](https://ezcare.easyms.co.kr/new/ezCare.html)) |
| **포지션** | 방문요양 **1위** → **주간보호 ERP·재무회계·세무·4대보험** 통합 ([동아일보 2025.11](https://www.donga.com/news/It/article/all/20251127/132855747/1)) |

#### 핵심 모듈 ([기능 소개](https://ezcare.easyms.co.kr/new/ezCare_fnc.html))

| 모듈 | 기능 |
|------|------|
| 수급자·요양보호사 관리 | 인정유효기간, 서비스 이력, 본인부담금 수납, 서식 출력 |
| **일정관리** | 달력형, (가산)수가·본인부담금 **자동 계산**, 중복·오류 방지 |
| **공단 일정 가져오기** | 공단 엑셀(급여계획·청구일정) → 이지케어 일정 **대입** |
| 방문일정 집계 | 공단 청구액·본인부담금 합계 |
| **RFID 점검** | 태그 전송 ↔ 공단 계획 비교, 미전송·시간차 경고 ([FAQ](https://ezcare.easyms.co.kr/help/faq.ez?rowid=21647)) |
| 서식·평가 | 일정표·본인부담금청구서·평가 비치자료 |
| **재무회계** (별도/통합) | 결의·예산·세무·4대보험 — 주간보호 **차별화 축** |

#### 모바일·보호자 (3차 신규 확인)

| 프로필 | EZCARE 앱 | 기능 |
|--------|-----------|------|
| 관리자 | ✅ | PC 계정(시설코드/ID/PW)으로 기관 업무 조회 |
| 요양보호사 | ✅ | 기관 **초대** 후 이용 |
| 수급자/보호자 | ✅ | 기관 **초대** 후 **청구서·명세서** 교환·조회 |

- 2026.03.03 앱 업데이트: 「요양보호사, **주야간보호** 편의기능 확대」([Google Play](https://play.google.com/store/apps/details?hl=ko&id=com.easyms.ezcare))
- **ogada G1 갭**: 이지케어도 보호자 앱으로 **명세서 조회** 지원 — ogada v1.1은 **초대 기반 guardian 온보딩 + 명세 열람**이 최소 패리티

#### 주간보호 vs 방문요양

- RFID·태그·「관리자 일정」은 공개 FAQ가 **방문요양·사회복지사 방문** 중심.
- **주간보호 전용 출석 UX**는 공개 자료 **Thin** — 2025~2026 **주간보호 평가·환수 실무교육**·앱 주야간 기능 확대로 모듈 성숙 중.
- 가입 상담 폼에 **「주간보호」「방문+주간보호」** 기관유형 명시 ([ezcare.easyms.co.kr](https://ezcare.easyms.co.kr/)).

#### 청구·정산

- 케어포와 유사: **내부 일정·수가 계산** + **공단 엑셀 import** + 공단 포털 청구.
- 본인부담금 청구서·명세서 자동 생성 ([기능 소개](https://ezcare.easyms.co.kr/new/ezCare_fnc.html)).

#### 온보딩·가격

| 항목 | 내용 |
|------|------|
| 가입 | 홈페이지 **상담 신청** → 전화/방문 ([가입상담](https://ezcare.easyms.co.kr/)) |
| 공개 요금표 | ❌ — 영업 상담 |
| ogada 대비 | ogada **`platform_admin` 개통** vs 이지케어 **영업 주도** |

---

### 3-3. 엔젤시스템 (Angel / LCMS)

| 항목 | 내용 |
|------|------|
| **조사일** | 2026-06-06 |
| **URL** | https://www.lcms.or.kr/ (로그인·가입), https://www.silverangel.kr/ (소개) |
| **제공 형태** | 웹 + **직원 전용 모바일 앱** ([Google Play](https://play.google.com/store/apps/details?id=lcms.or.kr.angel)) |
| **가입** | **온라인 비대면 가입** ([상품안내](https://www.lcms.or.kr/reg/selectProductGuide.do)) |

#### 주야간보호 ([daycareEssentialWork](https://www.silverangel.kr/newSilverangel/daycare/daycareEssentialWork.do))

- 필수교육·운영규정·급여제공 지침 등 **평가 항목별 체크** UI.
- 「시스템 사용만으로 평가 준비」 포지셔닝.
- **홍보관** — 기관 홍보 페이지 (ogada 범위 외).

#### 기능 (공개 수준)

| 영역 | 지원 |
|------|------|
| 수급자·급여제공 기록 | ✅ PC·모바일 **역할별 메뉴 자동 구성** |
| 공단 청구 | ✅ 급여 기록 → **롱텀 연동** 청구 (소개·앱 설명) |
| **CMS 본인부담 자동이체** | ✅ 계좌·카드·가상계좌 ([lcms.or.kr](https://www.lcms.or.kr/)) |
| 보호자 포털 | △ (가정통신문·명세 이메일/SMS — [extraService](https://www.silverangel.kr/newSilverangel/service/extraService.do)) |
| 출석 QR | ❌ 공개 자료 없음 |
| **CMS 요금(부가)** | 월 **30,000원** + 건당 250원(자동이체)/300원(가상계좌) ([extraService](https://www.silverangel.kr/newSilverangel/service/extraService.do)) |

#### 2026 업데이트

- [공지] 시설·주야간 기능 추가·개선 (2026-03-31, silverangel.kr) — **PC=모바일 동등** 강조.

---

### 3-4. 롱텀 — 장기요양정보시스템 (공단)

| 항목 | 내용 |
|------|------|
| **조사일** | 2026-06-06 |
| **URL** | https://www.longtermcare.or.kr/ |
| **비용** | **무료** (공단 공식) |
| **역할** | 급여 **청구·심사·지급** 공식 채널. 입퇴소신고·종사자 근무통보·관리현황 통보 |
| **2026 개편** | 홈페이지 **2026-01-16** 개편 — **IE 접속 불가**, Chrome/Edge 필수 ([개편 안내](https://longtermcare.or.kr/npbs/e/g/540/openCyberCstMain.web?menuId=npe0000002594)) |

#### 제공·미제공

| ✅ 공단 역할 | ❌/△ 민간 ERP가 대체 |
|-------------|---------------------|
| 급여 제공 내역 등록·청구서 전송 | 일일 **건강·투약·식사** 운영 기록 |
| 심사·지급·명세 | **본인부담금** 수납·보호자 발송 |
| **청구내역상세** 등 **엑셀 export** | **다지점 통합 대시보드** |
| 입퇴소·계약 통보 | **QR/NFC 출석** UX |

> ogada MVP: 공단 **직접 전송·API 제외**, **엑셀 import로 reconciliation** — 업계 표준과 일치 (REQUIREMENTS §3-9).

---

## 4. 공통 패턴 (Cross-Competitor)

### 4-1. 청구·정산

| 단계 | 업계 공통 | ogada MVP |
|------|----------|-----------|
| A | 기관 ERP에서 출석·등급·수가 → **내부 계산** | ✅ §3-9 |
| B | **롱텀**에서 공단 급여 청구·전송 | 공단 UI (MVP **제외**) |
| C | 공단 **청구내역상세** 엑셀 ↓ ERP **upload** | ✅ NHIS import |
| C-1 | 엑셀 **컬럼 변동**(예: `처리상태` 선행열) | 파서 **스킵·정규화** — 케어포 [44438](https://www.carefor.co.kr/cs/view_notice.php?calmgno=44438) |
| D | ERP **본인부담금** 청구·명세·(후속) 발송·CMS | MVP: 생성·출력만, 발송/CMS **후속** |

### 4-2. 출석·현장

| 방식 | 케어포 | 이지케어 | 엔젤 | ogada MVP |
|------|--------|----------|------|-----------|
| 웹 수기 | ✅ | ✅ | ✅ | ✅ |
| NFC/RFID (직원·태그) | ✅ | ✅ (방문 강) | △ | ❌ |
| 보호자 **지점 QR** 셀프 | ❌ | ❌ | ❌ | ✅ **차별화** |

### 4-3. SaaS·온보딩

| 서비스 | 신규 기관 등록 | 다지점 |
|--------|---------------|--------|
| 케어포 | **셀프** 회원가입 + 1개월 무료 | △ 미확인 |
| 이지케어 | **상담 가입** | △ 미확인 |
| 엔젤 | **온라인 가입** | △ 미확인 |
| **ogada** | **`platform_admin` 개통 (A)** | ✅ **Org-Branch HQ** |

### 4-4. MVP 이후 경쟁사 Must-have (ogada Should/Could)

- 보호자 **알림톡/SMS**·일일 리포트 (케어포·이지케어)
- **CMS·간편결제** (케어포·엔젤)
- **공단 평가** 서식·체크리스트 자동화 (케어포·엔젤·이지케어)
- **재무회계** (이지케어)
- 프로그램·식단·이동서비스 (케어포 주야간 전 모듈)

---

## 5. ogada 대비 갭·차별화·MVP 제안

> planner 입력용 — REQUIREMENTS·USER_STORIES·API_SPEC 갱신 시 참고.

### 5-1. ogada **강점·차별화** (유지)

| # | 항목 | 근거 |
|---|------|------|
| 1 | **전국 B2B SaaS** — `platform_admin` Tenant 개통 | 경쟁사는 셀프/상담 **1기관=1계정** 성격. 파일럿·전국 판매에 ogada 모델 적합 |
| 2 | **다지점 HQ 대시보드** + Branch Switcher | 공개 경쟁사 자료에 동등 기능 **미확인** — 파일럿(2지점) 핵심 |
| 3 | **QR B방식** (보호자/이용자 → 지점 QR) | NFC·RFID **하드웨어 불필요**, 스마트폰만으로 파일럿 검증 가능 |
| 4 | **7역할 RBAC** + Tenant 격리 | 경쟁사는 직종별 메뉴는 있으나 `platform_admin`·`sysadmin` **SaaS 운영 역할** 분리 없음 |
| 5 | **MVP 집중** — 출석·건강·청구·대시보드 | 케어포/엔젤 **평가·회계·직원급여** 전범위 대비 **구현 속도·파일럿** 우선 |

### 5-2. **갭** (경쟁사 대비 MVP 부족 — 의도적/후속)

| # | 갭 | 경쟁사 | ogada | 제안 우선순위 |
|---|-----|--------|-------|--------------|
| G1 | 보호자 **풀 포털·앱** (사진·명세·푸시) | 케어포 ✅ | △ MVP: QR+열람 골격, 알림 **Should** | **v1.1** — 파일럿 후 |
| G2 | **CMS·간편결제** | 케어포·엔젤 ✅ | ❌ MVP 제외 | **v2** |
| G3 | **공단 평가** 자동화·2026 지표 | 케어포·엔젤 ✅ | ❌ MVP | **Could** — 영업 차별 아님, 파일럿 후 |
| G4 | **재무회계** | 이지케어 ✅ | ❌ | **Won't v1** |
| G5 | 이동서비스·프로그램·식단 **풀 모듈** | 케어포 ✅ | Should | 파일럿 **제외**, v1.1~ |
| G6 | NFC/RFID 출석 | 케어포·이지케어 | ❌ (QR 선택) | **의도적** — B방식 유지 |
| G7 | 공단 엑셀 **컬럼 스펙** 실측 | 업계 공통 | △ 가정 | **즉시** — 파일럿 센터 샘플 확보 (PLAN_NOTES #27) |
| G8 | 보호자 **명세서 모바일**(초대·조회) | 케어포·**이지케어 EZCARE** ✅ | △ MVP: QR+열람 골격 | **v1.1** — 초대 흐름·명세 탭 |

### 5-3. MVP 우선순위 제안 (planner)

| 순위 | 기능 | 이유 |
|------|------|------|
| P0 | Tenant·Branch·7역할·출석(수기)+건강 | 파일럿(`branch_admin`, `caregiver`) |
| P0 | 청구: 수가표(B)·copay·월별 명세·**NHIS import** | 케어포 동등 **Must** — USER_STORIES US-G05 |
| P0 | 지점/통합 **대시보드** | 1주차 완료 기준 |
| P1 | QR B + `guardian`/`client_user` | 파일럿 2경로 출석 |
| P1 | NHIS import **reconciliation UI** (MATCHED/DISCREPANCY) | 케어포 4단계 UX 벤치마크 |
| P2 | 보호자 **초대·명세 열람** + 기록 열람 (알림 없이) | G1·G8 — 이지케어 EZCARE 앱 패턴 벤치마크 |
| P3 | 프로그램·식사·직원·평가 | Should — 경쟁 **패리티** |

### 5-4. REQUIREMENTS·USER_STORIES 정합

| 문서 항목 | 벤치마크 검증 |
|-----------|--------------|
| §3-9 청구 2단계 | ✅ 케어포·이지케어와 **동일** |
| §3-3 QR B방식 | ✅ 경쟁사 대비 **차별화** — 유지 |
| §1-3 platform_admin | ✅ 경쟁사 셀프가입과 **의도적 차별** |
| §3-2-1 주민번호 암호화 | ✅ 법정 필수 — 경쟁사도 수집 (PLAN_NOTES #28) |
| §3-9-1 수가표 B방식 | ✅ 공단 개정 대응 — ERP 공통 |

---

## 6. 가격·TCO 참고 (기관 ERP)

| 서비스 | 공개 가격 | 비고 |
|--------|----------|------|
| 케어포 주야간 | **월 33,000원~** (구간 동일, 부가세 포함) | [cost.php](https://www.carefor.co.kr/price/cost.php) |
| 이지케어 | 상담 | 업무+재무 패키지 |
| 엔젤 | 상담 | ERP 상담 + CMS **월 30,000원** + 건당 수수료 ([extraService](https://www.silverangel.kr/newSilverangel/service/extraService.do)) |
| 롱텀 | 무료 | 청구만 |
| **ogada** | 미정 | **가정**: 지점·이용자 tier 또는 flat SaaS — 영업 정책 필요 |

---

## 7. 출처·조사 메타

| # | 출처 | URL | 조사일 |
|---|------|-----|--------|
| 1 | 케어포 홈·주야간 소개 | https://www.carefor.co.kr/intro_visit/composition.php | 2026-06-06 |
| 2 | 케어포 주야간 매뉴얼 PDF | https://www.carefor.co.kr/ct_att/contents_article/0/202206/12/Dov8rzFqBv.pdf | 2026-06-06 |
| 3 | 케어포 청구 교육 공지 | https://www.carefor.co.kr/cs/view_notice.php?calmgno=43619 | 2026-06-06 |
| 4 | 케어포 2026 평가 공지 | https://www.carefor.co.kr/cs/view_notice.php?calmgno=46130 | 2026-06-06 |
| 5 | 케어포 이용요금 | https://www.carefor.co.kr/price/cost.php | 2026-06-06 |
| 6 | 케어포 iOS 앱 (NFC) | https://apps.apple.com/us/app/%EC%BC%80%EC%96%B4%ED%8F%AC/id1220736809 | 2026-06-06 |
| 7 | 이지케어 기능 | https://ezcare.easyms.co.kr/new/ezCare_fnc.html | 2026-06-06 |
| 8 | 이지케어 규모 | https://www.easyms.co.kr/new/ezCare.html | 2026-06-06 |
| 9 | 이지케어 RFID FAQ | https://ezcare.easyms.co.kr/help/faq.ez?rowid=21647 | 2026-06-06 |
| 10 | 엔젤 LCMS·CMS | https://www.lcms.or.kr/ | 2026-06-06 |
| 11 | 엔젤 주야간 필수업무 | https://www.silverangel.kr/newSilverangel/daycare/daycareEssentialWork.do | 2026-06-06 |
| 12 | 공단 장기요양 | https://www.longtermcare.or.kr/ | 2026-06-06 |
| 13 | 케어포 청구내역상세 import 매뉴얼 | https://www.carefor.co.kr/pdf_manual/visitcare.pdf | 2026-06-06 |
| 14 | 케어포 처리상태 열 공지 | https://www.carefor.co.kr/cs/view_notice.php?calmgno=44438 | 2026-06-06 |
| 15 | 롱텀 2026 홈페이지 개편 | https://longtermcare.or.kr/npbs/e/g/540/openCyberCstMain.web?menuId=npe0000002594 | 2026-06-06 |
| 16 | 이지케어 EZCARE 앱 | https://apps.apple.com/kr/app/%EC%9D%B4%EC%A7%80%EC%BC%80%EC%96%B4-ezcare/id6740553966 | 2026-06-06 |
| 17 | 엔젤 CMS 요금 | https://www.silverangel.kr/newSilverangel/service/extraService.do | 2026-06-06 |
| 18 | 케어포 2026 평가 PDF | https://www.carefor.co.kr/ct_att/contents_article/0/202602/46102/lIxDliWswE.pdf | 2026-06-06 |

---

## 8. 다음 조사 우선순위

1. **공단 청구내역상세 엑셀** 실제 컬럼·`처리상태` 포함 여부 (파일럿 센터 샘플) — PLAN_NOTES #27
2. 케어포 **로그인 후 주야간 메뉴 트리** (체험 계정 또는 교육 PDF 추가)
3. 이지케어 **주간보호 전용** 화면·FAQ (방문과 분리) — EZCARE 앱 주야간 메뉴
4. 경쟁사 **다지점/본사 통합** — 공식 매뉴얼·고객센터 확인 (현재 △)
5. ogada **가격 tier** — 케어포 33,000원/월·엔젤 CMS 30,000원/월 TCO 벤치마크 (PLAN_NOTES #31)
6. 롱텀 **2026 UI** 청구내역상세 export 경로 스크린샷 (파일럿 온보딩 가이드용)

---

*planner 동기화: `build --role planner` | 갱신: `build --role benchmark_researcher`*
