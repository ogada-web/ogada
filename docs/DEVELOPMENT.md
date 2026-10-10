# 개발과 검증

Java 17 이상, Maven, Node.js/npm, PostgreSQL을 사용합니다. Python은 보조 검사 도구입니다.

처음 가져온 저장소는 루트에서 `git submodule update --init`로 준비합니다. 기존 환경에서는 `git status`와 브랜치를 먼저 확인하고 소스를 재설정하지 않습니다. 루트는 `main`, 앱 변경은 각 서브모듈의 `develop`에서 수행합니다.

1. 전용 개발 DB와 `DB_URL`, `DB_USERNAME`, `DB_PASSWORD`를 준비합니다.
2. 루트 `.env.example`을 참고해 비공개 `.env`를 작성합니다. Vite는 루트 `.env`를 읽습니다. Spring Boot는 `.env`를 자동 로드하지 않으므로 실행 셸에 필요한 변수를 주입합니다.
3. 백엔드에서 `mvn spring-boot:run`, 프론트엔드에서 `npm ci` 후 `npm run dev`를 실행합니다. 기본 API는 8080, 개발 UI는 5173입니다. Flyway는 기동 시 개발 DB에 적용되므로 운영 DB 연결을 사용하지 않습니다.

공개 미리보기는 [별도 운영 구성](OPERATIONS.md)을 사용합니다.

## 검사

```bash
# src/frontend: 변경 관련 파일 선택
npm test -- src/layout/AppShell.test.jsx
npm run build

# src/backend: 필요 시 -Dtest=클래스명 으로 범위 지정
mvn test
mvn -DskipTests package

# 루트: Python 표준 라이브러리로 프록시 검사
python3 scripts/test_demo_preview_routes.py
python3 scripts/test-demo-preview-server.py
```

Vitest는 `scripts/npm-test-locked.sh`의 공용 잠금으로 한 번에 하나만 실행합니다. 다른 테스트 실행이 끝나기를 기다립니다. 종료가 필요하면 `scripts/vitest-stop.sh`를 사용합니다. Live E2E도 같은 잠금을 사용합니다.

브라우저 검사는 기존 `.venv`와 설치된 Chromium, 비공개 미리보기 설정을 사용합니다. 새 환경의 선택 의존성은 루트 `requirements.txt`에 있습니다. 현재 스크립트의 Chromium 경로는 이 환경 기준입니다.

```bash
.venv/bin/python scripts/check-workspace-ui.py
.venv/bin/python scripts/check-transport-mobile-layout.py
```

인증은 localhost에서만 수행하고 결과는 `/tmp`에 저장합니다. 첫 검사는 보이는 메뉴를 역할·너비별로 순회합니다. 둘째는 배차 복구 fixture가 필요하므로 계정 역할·날짜도 확인합니다.

실백엔드 E2E는 `scripts/run-live-e2e.sh`와 `npm run test:live-e2e`로 실행합니다. `scripts/dev-live-e2e.env`에 격리 DB 계정·이용자 ID를 지정합니다. `LIVE_E2E_WRITE=0`을 기본으로 유지하고 쓰기 검사·bootstrap은 전용 테스트 환경에서만 사용합니다. 과거 보호자 로그인 시나리오는 현재 비활성 역할 정책과 구분합니다.

## 완료 기준

실행한 관련 검사와 실행하지 않은 검증을 구분합니다. 앱 변경은 각 서브모듈에서 로컬 커밋한 뒤 루트 포인터를 반영합니다. 문서·도구 변경은 루트에서 커밋합니다. 자동 push·자동 브랜치 승격은 사용하지 않습니다.

기능·권한 변경은 기존 현재 문서를 수정합니다. 반복 조사·인계 파일을 만들지 않습니다. 실제 검증 증거가 필요할 때만 별도 QA 기록을 남깁니다.
