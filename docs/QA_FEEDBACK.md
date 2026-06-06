# QA 피드백 (tester → planner → coder)

> **작성**: `tester` (test 브랜치 검증 후)  
> **반영**: `planner`가 `docs/ROADMAP.md`·`docs/USER_STORIES.md`·`docs/PLAN_NOTES.md`에 태스크화  
> **수정**: `coder`가 develop 브랜치에서 OPEN 항목 해결 후 `Fixed`로 이동

---

## 상태 흐름

```
tester 발견 → Open → planner 기획 반영(Planned) → coder 수정(Fixed)
```

| severity | 의미 |
|----------|------|
| BLOCK | test merge·승격 불가 — 즉시 수정 |
| HIGH | Must 기능 오동작 |
| MEDIUM | Should 수준·UX·문서 불일치 |
| LOW | 개선 제안 |

---

## Open

_(tester가 검증 중 발견한 미해결 이슈. 없으면 "없음" 유지)_

없음

---

## Planned

_(planner가 ROADMAP·PLAN_NOTES에 반영 완료, coder 대기 중)_

없음

---

## Fixed

_(coder가 develop에서 수정 완료)_

없음

---

## 기록 템플릿 (tester용)

```markdown
### [OPEN] v1 — 짧은 제목
- **id**: QA-YYYYMMDD-001
- **severity**: BLOCK | HIGH | MEDIUM | LOW
- **stream**: backend | frontend
- **version**: v1
- **found_at**: YYYY-MM-DD
- **summary**: 한 줄 요약
- **steps**: 재현 절차
- **expected**: 기대 결과 (USER_STORIES / API_SPEC 근거)
- **actual**: 실제 결과
- **artifacts**: transfer/.../test.md, docs/TEST_REPORT.md §...
```
