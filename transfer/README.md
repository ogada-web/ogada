# 이관(transfer) 산출물

> **목적**: develop → test → operation 단계에서 QA(tester)가 관리하는 **이관 전용** 폴더  
> **규칙**: `coder`는 `src/`(develop 브랜치)만 수정. `tester`는 이 `transfer/` 및 test 브랜치만 다룸.

## 구조

```
transfer/
├── backend/          # 백엔드 이관 (backend/test 브랜치)
│   ├── checklists/   # 이관 전·후 체크리스트
│   ├── manifests/    # 배포·릴리스 매니페스트 (버전, 커밋, Flyway 버전 등)
│   └── packages/     # 이관 패키지 메타 (JAR 빌드 정보, diff 요약)
└── frontend/         # 프론트 이관 (frontend/test 브랜치)
    ├── checklists/
    ├── manifests/
    └── packages/
```

## 브랜치

| 스트림 | 개발 | 이관·검증 | 운영 |
|--------|------|-----------|------|
| backend | `backend/develop` | `backend/test` | `backend/operation` |
| frontend | `frontend/develop` | `frontend/test` | `frontend/operation` |

## QA(tester) 실행

```bash
# 백엔드 이관 검증·산출물 갱신
.venv/bin/python scripts/run_agent.py build --role tester --stream backend

# 프론트 이관
.venv/bin/python scripts/run_agent.py build --role tester --stream frontend
```
