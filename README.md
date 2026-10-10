# ogada

주간보호·방문요양 기관의 이용자, 돌봄 기록, 송영·배차, 직원 근무, 청구 업무를 관리하는 멀티테넌트 SaaS입니다.

현재 구현은 **React 18 + JavaScript/JSX + Vite**, **Spring Boot + Java 17**, **PostgreSQL + Flyway**입니다. 프론트엔드와 백엔드는 각각 `src/frontend`, `src/backend` Git 서브모듈입니다.

| 현재 문서 | 내용 |
|---|---|
| [현재 상태](docs/CURRENT_STATE.md) | 역할 4종, 화면 구분, 주요 업무 |
| [개발](docs/DEVELOPMENT.md) | 실행·테스트·커밋 방법 |
| [미리보기 운영](docs/OPERATIONS.md) | 서버·공개 링크·데이터 보호 |
| [보안과 출시 확인](docs/SECURITY.md) | 권한 경계, 보존 정책, 남은 확인 |
| [UI 기준](docs/UI_GUIDE.md) | 메뉴·모바일·공용 화면 표시 |
| [출처 이력](docs/REFERENCES.md) | 과거 조사 원문 찾는 방법 |

최근 검증: [UI 점검](docs/qa/UI_AUDIT_2026-10-10.md), [배차 복구](docs/qa/DISPATCH_RESTORE_2026-10-10.md), [직원 권한](docs/qa/STAFF_ACCESS_2026-10-10.md).

기본 작업 방식은 **단일 에이전트, 요청 단위 실행, 로컬 커밋**입니다. [AGENTS.md](AGENTS.md)를 따르고 기능 변경 시 기존 현재 문서를 수정합니다. 반복 조사·인계 문서를 새로 쌓지 않습니다.
