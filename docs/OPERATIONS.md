# 미리보기 운영

2026-10-10 현재 구성입니다. 더미 데이터 DB를 실제 고객 운영 환경과 분리해서 사용합니다.

| 구성 | 위치 |
|---|---|
| API | localhost:8080, tmux `ogada-preview-backend` |
| 컴파일 UI·API 프록시 | localhost:4174, tmux `ogada-preview-web` |
| 임시 HTTPS 터널 | tmux `ogada-preview-tunnel` |
| DB | Docker `ogada-phone-preview-db`, localhost:15432, `ogada_preview` |
| 현재 공개 URL | `.venv/phone-preview/tunnel.url` |
| 비공개 설정·백업·fixture | `.venv/phone-preview/` (Git 제외) |

터널 URL은 재기동 시 바뀔 수 있으므로 문서에 고정하지 않습니다.

```bash
tmux list-sessions
curl -fsS http://127.0.0.1:4174/login >/dev/null
curl -fsS http://127.0.0.1:8080/api/v1/health
cat .venv/phone-preview/tunnel.url
```

## 갱신

프론트엔드를 빌드·검증한 뒤 자산을 `/tmp/ogada-phone-preview`에 반영합니다. 현재 서버는 `scripts/demo-preview-server.py --root /tmp/ogada-phone-preview`를 사용합니다. 백엔드는 검증·패키징 후 기존 비공개 설정 런처로 갱신합니다. 현재 패키지는 `.venv/phone-preview/backend/target/backend-0.0.1-SNAPSHOT.jar`, 런처는 `/tmp/ogada-preview-backend-launch.py`입니다. `/tmp` 파일은 재부팅 후 재구성이 필요할 수 있습니다.

재기동 전 해당 tmux 세션의 실행 경로·설정을 확인합니다. UI 수정만으로 DB·터널을 재생성하지 않습니다. 공개 터널은 컴파일 UI 프록시 포트에 연결하고, 새 도메인은 카카오 웹 플랫폼에 등록합니다. 공개 미리보기에 Vite 개발 서버를 사용하지 않습니다.

## 권한·데이터

프록시는 로그인·갱신·로그아웃, 차량 생성·수정, 배차 작성·추천·수정·확정·확정 취소, 배차 설정, 당일 이용 상태, 본인 출퇴근의 명시된 경로만 쓰기 전달합니다. 나머지 쓰기·삭제는 405 JSON 응답으로 차단합니다. 허용 경로도 Spring의 인증·역할·기관·지점·본인 범위 검증을 통과해야 합니다.

인증 보조 검사는 localhost에서 수행합니다. 공개 URL에는 비인증 접근만 확인합니다. 서버 REST 키·비밀번호·토큰을 브라우저 자산·URL에 넣지 않습니다. 카카오 JS 키는 웹 SDK용이고 REST 키는 서버용입니다.

| 테스트 계정 | 역할 |
|---|---|
| `test1@test.com` | 직원 |
| `test@test.com`, `test2@test.com` | 지점관리자 |
| `test3@test.com` | 본사관리자 |
| `test4@test.com`, `test5@test.com` | SaaS 제공자 |

비밀번호는 비공개 설정으로 관리합니다. 기존 이용자·차량·송영 초안·DB 덤프를 보존합니다. 데이터 변경 실험은 더미 DB에서 수행하고 변경 전 복원 가능한 DB 백업을 확보합니다.

Grok·역할별 에이전트 프로세스와 주기 실행 설정은 사용하지 않습니다. 미리보기 세션은 에이전트 루프와 독립적으로 유지합니다.
