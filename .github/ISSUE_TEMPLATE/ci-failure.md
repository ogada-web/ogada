---
name: CI Failure Report
about: 자동 생성된 CI 실패 티켓 템플릿 — 빌드 실패 시 CI 워크플로가 이 이슈를 생성합니다.
title: "[CI Failure] {{workflow_name}} - {{short_sha}}"
labels: ci-failure
assignees: []
---

자동으로 생성된 CI 실패 이슈입니다. 아래 항목을 채워 문제 해결 및 추적에 활용하세요.

- 실패 워크플로: `{{workflow_name}}`
- 브랜치: `{{head_branch}}`
- 커밋: `{{head_sha}}`
- 실행 URL: {{run_url}}
- 로그(마스킹된 핵심요약): 

원인(요약):

재현/임시 대응:

수정 브랜치 / PR 링크:

추가 메모:

보안 주의: 로그에 시크릿/토큰/민감정보가 포함되지 않도록 마스킹하세요.

