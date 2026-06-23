<!-- doc:owner=TSR doc:audience=COD,TSR,PLN updated=2026-06-17 -->

# Vitest 동시 실행 방지 (VITEST_CONCURRENCY.md)

> 프론트엔드 단위 테스트(`npm test`)가 **한 번에 하나만** 돌도록 하는 운영 규칙과 도구.

---

## 배경

- **Vitest**는 `src/frontend`의 React 단위·통합 테스트 실행기다 (`package.json` → `vitest run`).
- 전체 스위트는 약 **1,600건 / 4~5분**이 정상이다.
- Vitest는 **워커 프로세스를 여러 개** 띄운다(병렬 실행). **한 번의 `npm test` 안에서** 워커가 여러 개인 것은 정상이다.
- 반면 **서로 다른 `npm test`가 동시에 여러 개** 떠 있으면 비정상이다. 에이전트·수동 실행이 겹치면 각각 2~3GiB RAM을 쓰며 **OOM·hang**이 난다.

### 정상 vs 비정상

| 상태 | 예시 | 판단 |
|------|------|------|
| 테스트 없음 | `ps`에 vitest 없음 | ✅ |
| 1회 실행 중 | `npm test` 1개 + 워커 2~4개 | ✅ |
| **중복 실행** | `npm test` **2개 이상**이 10분+ | ❌ 정리 필요 |

---

## 강제: flock 락 (`scripts/npm-test-locked.sh`)

`npm test`와 `npm run test:live-e2e`는 모두 이 스크립트를 경유한다.

```bash
cd src/frontend
npm test                  # → ../../scripts/npm-test-locked.sh → vitest run
npm test -- src/foo.test.jsx   # 인자 그대로 전달
```

- 락 파일: `/tmp/ogada-vitest.lock` (`OGADA_VITEST_LOCK_FILE`로 변경 가능)
- 이미 다른 테스트가 돌고 있으면 **즉시 exit 75**와 안내 메시지를 출력한다.
- **우회 금지**: `npx vitest run` 직접 호출, 별도 셸에서 동시 `npm test` — 모두 락을 피한다.

---

## 에이전트·개발자 규칙

1. **새 `npm test` 전** 기존 실행이 있는지 확인한다.
   ```bash
   ps aux | grep -E '[v]itest run'
   ```
2. **이미 돌고 있으면** 새로 시작하지 말고 끝날 때까지 기다리거나, hang이면 정리 스크립트를 쓴다.
3. **부분 테스트**도 `npm test -- <파일>` 한 줄로만 실행한다. 여러 터미널·에이전트에서 동시에 돌리지 않는다.
4. **전체 스위트**는 tester 파이프라인 또는 한 세션에서 **1회**만 실행한다.
5. 테스트가 **5분(부분) / 15분(전체) 이상** 무출력이면 hang으로 보고 `vitest-stop.sh` 후 원인을 조사한다.

`.agents/rules.md` §5와 `docs/AGENT_USAGE.md` §6도 동일 내용을 참조한다.

---

## 정리: `scripts/vitest-stop.sh`

멈춘·중복 vitest를 한 번에 종료한다.

```bash
./scripts/vitest-stop.sh
```

동작:

- `vitest run` / 관련 `npm test` 프로세스 종료
- `/tmp/ogada-vitest.lock` 삭제

정리 후 메모리 확인:

```bash
free -h
ps aux | grep -E '[v]itest' || echo "no vitest"
```

---

## 트러블슈팅

| 증상 | 조치 |
|------|------|
| `vitest: another npm test is already running` | 기존 실행 대기, 또는 `./scripts/vitest-stop.sh` |
| RAM 90%+ · load 폭증 | `vitest-stop.sh` → `free -h` 재확인 |
| transport/Kakao 맵 테스트만 오래 걸림 | 단일 파일만 격리 실행: `npm test -- src/components/transport/KakaoTransportMap.test.jsx` |
| 락 파일만 남고 프로세스 없음 | `rm -f /tmp/ogada-vitest.lock` |

---

## 관련 파일

| 경로 | 역할 |
|------|------|
| `src/frontend/package.json` | `test` / `test:live-e2e` → locked wrapper |
| `scripts/npm-test-locked.sh` | flock + `vitest run` |
| `scripts/vitest-stop.sh` | 중복·hang 프로세스 정리 |
| `docs/qa/TEST_REPORT.md` | 최신 테스트 회귀 결과 |
