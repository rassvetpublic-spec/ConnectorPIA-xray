# Issue-Driven Workflow

## Инвариант

Любое изменение проекта после bootstrap Issue #1 проходит только через:

`Issue -> fresh branch -> implementation -> validation -> PR -> exact-head CI -> independent QA -> merge -> post-merge main check`

## Issue

Issue обязан содержать:
- цель и контекст;
- scope / out-of-scope;
- acceptance criteria;
- риски и зависимости, если они есть;
- архитектурные ограничения, если изменение их затрагивает.

## Branch

Ветка создаётся только от актуального `main`.

Допустимые префиксы:
- `feat/issue-N-...`
- `fix/issue-N-...`
- `docs/issue-N-...`
- `chore/issue-N-...`
- `test/issue-N-...`

Dirty/stale branch не используется как база новой задачи.

## Pull Request

PR должен:
- ссылаться на Issue (`Resolves #N`, `Closes #N` или `Refs #N`);
- описывать scope и changed files;
- перечислять выполненные проверки;
- фиксировать известные ограничения;
- не содержать unrelated changes и local/runtime artifacts.

## Exact-head gate

Merge разрешён только если проверки относятся к текущему PR HEAD. Любой новый commit после QA делает старое QA stale до повторной проверки.

Минимум перед merge:
1. required CI green;
2. secret/privacy gate green;
3. независимый review/QA не от implementation identity;
4. нет unresolved blocking threads / request changes;
5. ожидаемый HEAD совпадает с проверенным HEAD.

После merge выполняется проверка `main`.

## Scope discipline

Найденные в ходе работы дополнительные проблемы не чинятся молча. Они оформляются отдельным Issue или явно добавляются в текущий Issue до реализации.
