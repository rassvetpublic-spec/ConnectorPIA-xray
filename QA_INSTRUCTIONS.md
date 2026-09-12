# QA_INSTRUCTIONS.md — ConnectorPIA-xray

## Назначение

QA подтверждает не намерение и не описание PR, а фактическое состояние **текущего PR HEAD**.

## Минимальный QA цикл

1. Проверить связанный Issue и его Acceptance Criteria.
2. Проверить diff PR и убедиться, что нет scope creep.
3. Убедиться, что CI green именно на текущем HEAD.
4. Проверить отсутствие секретов, auth-state и случайных local/generated artifacts.
5. Выполнить применимые тесты/валидацию независимо от автора реализации.
6. Зафиксировать `APPROVED` либо конкретные blocking замечания.

## Exact-head invariant

Любой новый commit после QA делает прежнее approval/evidence устаревшим до повторной проверки.

## Что НЕ считается достаточным QA

- только зелёный CI без review;
- self-approval автора реализации;
- проверка старого commit SHA;
- утверждение «должно работать» без evidence;
- successful probe вместо проверки реального требуемого поведения;
- отсутствие ошибок в логах как единственное доказательство успеха.

## Bootstrap validation

Для текущего governance bootstrap достаточно:

```bash
python3 scripts/validate_repo.py
```

Ожидаемый результат:

```text
Repository validation OK: ... tracked files checked
```

Дополнительно вручную проверить:
- `AGENTS.md` является единой точкой входа;
- workflow соответствует `Issue -> branch -> PR -> CI -> QA -> merge`;
- `outputs/`, `auth/`, browser/session state и логи не отслеживаются;
- PR связан с Issue #1;
- CI workflow запускается на PR в `main` и на push в `main`.

## Merge verdict

QA должен выдавать один из трёх итогов:
- `APPROVED` — gates выполнены для текущего HEAD;
- `CHANGES_REQUESTED` — есть конкретные блокеры;
- `BLOCKED` — недостаточно evidence или внешняя зависимость не позволяет проверить требование.
