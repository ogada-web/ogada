<!-- doc:owner=BNK doc:audience=PLN updated=2026-06-06T22:00:00+09:00 -->
# 경쟁사 기능·서비스 비교 매트릭스 (COMPETITOR_MATRIX.md)

> **작성**: benchmark_researcher 에이전트 `[BNK]`  
> **최종 갱신**: 2026-06-06 (4차 재검증)  
> **상태**: 4차 조사 — 이지케어 공개 tier 요금·2026 수가(등급×시간대)·케어포 2026 매뉴얼  
> **상세 분석**: `docs/BENCHMARK_REPORT.md`

---

## 범례

| 기호 | 의미 |
|------|------|
| ✅ | 명시적 지원 (공식 자료 근거) |
| ❌ | 미지원 또는 ogada MVP **의도적 제외** |
| △ | 부분 지원·가정·확인 필요 |

---

## 1. 핵심 기능·서비스 비교

| 기능/서비스 항목 | ogada (MVP) | 케어포 | 이지케어 | 엔젤시스템 | 롱텀(공단) | 비고·근거 |
|------------------|-------------|--------|----------|------------|------------|-----------|
| **이용자(수급자) 관리** | ✅ | ✅ | ✅ | ✅ | △ | 케어포 매뉴얼 §1; 이지케어 fnc; 엔젤 silverangel |
| **장기요양등급·인정번호** | ✅ | ✅ | ✅ | ✅ | ✅ | 공단 마스터 — 롱텀 연동 |
| **주민등록번호(청구용)** | ✅ 암호화 | △ 수집(업계 관행) | △ | △ | ✅ 청구명세 | ogada §3-2-1; 법정 필수 |
| **본인부담 구분(15/9/6/0%)** | ✅ | ✅ | ✅ | △ | ✅ | 케어포: 일반/경감/기초; ogada copay_rates — [2026 예시](https://www.gangnam.go.kr/board/happyapgu_faq/613/view.do) |
| **출석 — 수기(웹)** | ✅ | ✅ | ✅ | ✅ | ❌ | ERP 공통 |
| **출석 — NFC/RFID(직원·태그)** | ❌ | ✅ | ✅(방문↑) | △ | ❌ | [케어포 App](https://apps.apple.com/us/app/%EC%BC%80%EC%96%B4%ED%8F%AC/id1220736809); [이지케어 FAQ](https://ezcare.easyms.co.kr/help/faq.ez?rowid=21647) |
| **출석 — QR(보호자→지점)** | ✅ B방식 | ❌ | ❌ | ❌ | ❌ | **ogada 차별화** — REQUIREMENTS §3-3 |
| **건강·투약 기록** | ✅ | ✅ | △ | ✅ | ❌ | 케어포 요양/간호 모듈 |
| **식사·식단 관리** | △ Should | ✅ | △ | △ | ❌ | 케어포 매뉴얼·식단표 공지 |
| **프로그램·활동 기록** | △ Should | ✅ | △ | ✅ | ❌ | 케어포 §5; 엔젤 평가 |
| **이동서비스(픽업·드롭)** | ❌ | ✅ | △ | △ | ❌ | 케어포 주야간 핵심 |
| **관리자 대시보드(지점)** | ✅ | ✅ | ✅ | ✅ | ❌ | ogada Must |
| **통합 HQ 대시보드(다지점)** | ✅ | △ 1기관번호=1계정 | △ | △ | ❌ | **ogada 차별화** — 케어포 [getting_started](https://www.carefor.co.kr/cs/getting_started.php) 다기관 통합 매뉴얼 **없음** |
| **청구 — 내부 수가·명세 계산** | ✅ | ✅ | ✅ | ✅ | △ | ogada fee_schedules B방식; **시간대(duration_band) △** — G9 |
| **수가 — 등급×이용시간대(2026)** | △ 1밴드 가정 | ✅(가정) | ✅(가정) | △ | ✅ | [롱텀 2026 수가](https://www.longtermcare.or.kr/npbs/e/b/502/npeb502m01.web?menuId=npe0000002742) |
| **청구 — 공단 포털 전송** | ❌ MVP제외 | △(롱텀 UI) | △ | △ | ✅ | 공단 공식 |
| **청구 — 공단 엑셀 import** | ✅ | ✅ | ✅ | △ | ✅ export | [케어포 §4-1 PDF](https://www.carefor.co.kr/pdf_manual/visitcare.pdf); `처리상태`열 [44438](https://www.carefor.co.kr/cs/view_notice.php?calmgno=44438) |
| **본인부담금 청구·수납** | ✅(발송 제외) | ✅ | ✅ | ✅ | ❌ | ogada MVP: 생성·출력 |
| **CMS·간편결제** | ❌ | ✅ | △ | ✅ | ❌ | [케어포 FAQ](https://www.carefor.co.kr/cs/view_faq.php); [lcms.or.kr](https://www.lcms.or.kr/) |
| **보호자 포털/앱** | △ MVP골격 | ✅ 가족돌봄앱 | ✅ EZCARE앱 | △ | ❌ | [케어포](https://www.carefor.co.kr/intro_visit/composition.php); [이지케어 App](https://apps.apple.com/kr/app/%EC%9D%B4%EC%A7%80%EC%BC%80%EC%96%B4-ezcare/id6740553966) — **기관 초대** 필수 |
| **보호자 알림(SMS/알림톡)** | ❌ Should | ✅ | ✅ | △ | ❌ | 이지케어 문자 FAQ·1,000p 프로모 |
| **직원·근태 관리** | △ Should | ✅ | ✅ | ✅ | △ 종사자통보 | |
| **재무회계·세무** | ❌ | △ 부가 | ✅ | ❌ | ❌ | 이지케어 **강점** |
| **공단 평가·서식 지원** | ❌ | ✅ | ✅ | ✅ | ❌ | 케어포 2026 지표 ([공지](https://www.carefor.co.kr/cs/view_notice.php?calmgno=46130), [고시](https://www.carefor.co.kr/cs/view_pds.php?calmgno=46327)) |
| **SaaS 멀티테넌트** | ✅ | △ | ✅ | △ | — | 이지케어 웹 SaaS |
| **플랫폼 Admin(Tenant 개통)** | ✅ | ❌ | ❌ | ❌ | — | ogada **A방식** §1-3 |
| **7역할 RBAC** | ✅ | △ 직종메뉴 | △ | △ 직종메뉴 | — | ogada 명시적 역할 UI |
| **지점 Branch Switcher** | ✅ | △ | △ | △ | — | 파일럿 2지점 |
| **모바일(직원)** | △ 웹 반응형 | ✅ 앱 | ✅ 웹+EZCARE앱 | ✅ 앱 | ❌ | 이지케어 앱 2026.03 주야간 기능 확대 |
| **온보딩** | platform_admin | 셀프+1mo무료 | 상담 | 온라인가입 | 공단등록 | [carefor cost](https://www.carefor.co.kr/price/cost.php) |

---

## 2. 청구·연동 흐름 비교

| 단계 | 케어포 | 이지케어 | ogada MVP | 롱텀 |
|------|--------|----------|-----------|------|
| 1. 일일 운영 기록 | ERP 입력 | ERP 일정 | 출석·건강 | — |
| 2. 공단 급여 청구 | 롱텀 | 롱텀 | **기관이 롱텀** | ✅ |
| 3. 엑셀 연동 | 청구내역상세↑ | 계획/청구일정↑ | NHIS import | export |
| 4. 본인부담금 | 케어포 | 이지케어 | ogada `/billing` | — |
| 4-1. 엑셀 컬럼 변동 | `처리상태`열 스킵 | △ | 파서 정규화 | export 포맷 변경 |
| 4-2. 브라우저 설정 | Chrome/Edge **안전하지 않은 콘텐츠 허용** | △ | 파일럿 온보딩 가이드 | [케어포 FAQ](https://www.carefor.co.kr/cs/view_notice.php?cscmgno=1237) |
| 5. 보호자 발송·수납 | 앱·CMS | EZCARE앱·문자 | **후속** | — |

---

## 3. 출석 방식 비교

| | 케어포 | 이지케어 | 엔젤 | ogada |
|---|--------|----------|------|-------|
| 직원 웹 수기 | ✅ | ✅ | ✅ | ✅ |
| NFC/RFID | ✅ 직원앱 | ✅ 방문·RFID점검 | △ | ❌ |
| 보호자 QR 셀프 | ❌ | ❌ | ❌ | ✅ |
| 하드웨어 필요 | NFC 태그 | RFID(방문) | — | **없음**(QR 출력) |

---

## 4. SaaS·가격·규모

| 항목 | ogada | 케어포 | 이지케어 | 엔젤 |
|------|-------|--------|----------|------|
| 공개 이용자/기관 수 | — (신규) | 14,000+ 기관 | **9,210** 재가(2026.06.06) | — |
| **공개 월 요금 (주야간/업무)** | 미정 | **33,000원 flat**/월 (VAT포함, 수급자 구간 무관) | **10,000 + (N−10)×500 + VAT** (예: 37명=25,850) | ERP 상담 |
| 프로모션 | — | 1개월 무료 | 30일 무료 + 문자1,000p (2026.05.31까지 40%할인) | — |
| CMS 부가 | — | △ | △ | **30,000원/월** + 건당 250~300원 |
| 셋팅비 | — | 없음 | 1회(해지 시 미반환) | — |
| 데이터 호스팅 | 클라우드 SaaS | 웹 | 웹(설치無) | 웹 |

> **가격 벤치마크 (G10)**: 케어포 **flat 33k** vs 이지케어 **저인원 유리·고인원 33k+** — ogada tier 정책은 PLAN_NOTES #31.

---

## 5. ogada 갭 요약 (planner용)

| 우선순위 | 갭 | MVP | 후속 |
|----------|-----|-----|------|
| 🔴 | NHIS 엑셀 **실컬럼**·`처리상태`·reconciliation UX | △ 스키마 있음 | 파일럿 샘플 (G7) |
| 🔴 | **수가표 시간대(duration_band)** — 등급×시간 2차원 (G9) | △ 1밴드 가정 | 파일럿 표준시간 확인 → §3-9-1 |
| 🔴 | 청구 **케어포 동등** (수가B·copay·명세) | ✅ Must | — |
| 🟡 | 보호자 **초대·명세 앱**(G8) | △ | v1.1 — EZCARE 패턴 |
| 🟡 | 보호자 포털·알림 | △ | v1.1 |
| 🟡 | **가격 tier** (G10) | 미정 | 영업 — 케어포 flat vs 이지케어 tier |
| 🟡 | CMS·결제 | ❌ | v2 |
| 🟢 | 평가·프로그램·식단·이동·회계 | ❌/Should | Could/Won't |

---

## 6. REQUIREMENTS·USER_STORIES 대비 (4차)

| 문서 | 벤치마크 검증 | 4차 신규 |
|------|--------------|---------|
| §3-9-1 `fee_schedules` | 등급×연도 B방식 ✅ | **+ duration_band(시간대) 축** 검토 — G9 |
| §3-9-2 copay | 15/9/6/0% ✅ | 2026 공단 예시와 **일치** 확인 |
| US-G05 청구 | 케어포 2단계 ✅ | 2026 수가 개정 반영 — `hq_admin` 수가 입력 시 **2026 표** 참조 |
| US-G06 NHIS reconciliation | MATCHED/DISCREPANCY ✅ | 롱텀 엑셀 **브라우저 설정** 온보딩 추가 권고 |
| §1-3 platform_admin | 차별 ✅ | — |
| §3-3 QR B | 차별 ✅ | — |

---

## 7. 조사 메타

| 항목 | 값 |
|------|-----|
| **마지막 전체 갱신** | **2026-06-06** (4차) |
| **조사 에이전트** | benchmark_researcher `[BNK]` |
| **입력 문서** | REQUIREMENTS §1-5, PLAN_NOTES, USER_STORIES |
| **다음 조사 우선** | ① NHIS 엑셀 샘플 ② fee_schedules duration_band ③ 케어포 주야간_2026 PDF ④ EZCARE 주야간 ⑤ 다지점 ⑥ 가격 tier ⑦ 롱텀 export UI |

---

*상세 서술·URL 목록: `docs/BENCHMARK_REPORT.md` §3·§7*
