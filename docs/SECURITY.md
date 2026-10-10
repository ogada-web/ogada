# 보안과 출시 확인

확인 기준: 2026-10-10 소스와 최근 QA. 전체 보안 감사·운영 출시 승인 결과는 아닙니다.

## 유지할 경계

서버에서 기관·허용 지점·역할·소유자를 검증합니다. 직원 근태 조회·처리는 본인만 허용하고 관리 인사 API와 배차 초안 접근을 제한합니다. 검증 범위는 [직원 권한](qa/STAFF_ACCESS_2026-10-10.md), [배차 복구](qa/DISPATCH_RESTORE_2026-10-10.md)에 기록되어 있습니다.

개인정보 최소 응답·마스킹·암호화를 유지합니다. 전체 개인정보·키·토큰을 로그나 문서에 저장하지 않습니다. 운영 인증 설정은 [ProductionSecretValidator](../src/backend/src/main/java/com/ogada/backend/security/ProductionSecretValidator.java)와 실제 환경 값을 확인합니다.

## 남은 확인

| 항목 | 현재 코드·실제 출시 확인 |
|---|---|
| 복원 가능한 백업 | [FileTenantBackupExecutor](../src/backend/src/main/java/com/ogada/backend/settings/domain/FileTenantBackupExecutor.java)는 기관 manifest를 작성합니다. 앱 SUCCESS만으로 DB·사진·첨부 복원을 검증하지 못합니다. 실제 DB 덤프·파일·키 관리와 빈 환경 복원·대조가 필요합니다. |
| 결제·CMS | [EasyPayConfig](../src/backend/src/main/java/com/ogada/backend/billing/easypay/config/EasyPayConfig.java), [FcmsConfig](../src/backend/src/main/java/com/ogada/backend/billing/cms/config/FcmsConfig.java)는 기본 stub을 등록합니다. 모의 승인에 의한 실수납 기록 변경 차단과 실제 연동을 검증해야 합니다. |
| 인증 저장·만료 | [session.js](../src/frontend/src/api/session.js)는 access를 메모리, refresh를 sessionStorage에 저장합니다. XSS 방어·갱신·만료·입력 복구를 검증해야 합니다. |
| 의존성 | 현재 lockfile과 pom을 출시 시점에 스캔합니다. 과거 CVE 보고서의 상태·버전은 현재 판정 근거로 사용하지 않습니다. 이번 정리에서 새 의존성 보안 감사는 수행하지 않았습니다. |
| 실제 운영 | TLS·비공개 DB·비밀 관리·오류 로그 마스킹·업로드·외부 링크·교차 기관 접근을 실제 구성에서 확인합니다. |
| 실업무 | 실제 결제·발송·NHIS 연동, 장애 복구·장시간 세션·부하·운영 복원은 UI·단위 검사로 대체하지 않습니다. |

## 보존·파기

과거 보존기간 문서는 법령·계약 확정 전 초안이었습니다. 확정 법정 기간이나 자동 파기 동작으로 취급하지 않습니다. 운영 전 유형별 근거·계약·기관 규정·보존 시작점·보류 사유와 백업 내 삭제 정책을 확정해야 합니다. 문서 정리를 이유로 운영 데이터를 삭제하거나 TTL을 변경하지 않습니다.

DB 구조·외래키·인덱스는 Flyway·서비스 코드가 기준입니다. 과거 제안·감사 원문은 [출처 이력](REFERENCES.md)에서 찾습니다.
