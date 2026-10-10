# 검사 위치

현재 실행 방법은 루트 `docs/DEVELOPMENT.md`에 관리합니다.

- 프론트엔드 단위 검사: `src/frontend`의 잠금 적용 `npm test`.
- 백엔드 단위·권한 검사: `src/backend`의 Maven 테스트.
- 미리보기 프록시: `scripts/test_demo_preview_routes.py`, `scripts/test-demo-preview-server.py`.
- 실화면: `scripts/check-workspace-ui.py`, `scripts/check-transport-mobile-layout.py`.

구형 Cursor/Grok 실행기와 팀 파이프라인 전용 테스트는 해당 실행 구성과 함께 제거했습니다. 앱 테스트는 각 서브모듈에 유지합니다.
