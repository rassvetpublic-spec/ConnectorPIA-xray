# ConnectorPIA-xray

Исследовательский и инженерный репозиторий проекта **ConnectorPIA-xray**.

## Governance

Каноническая точка входа для человека и AI-агента — [`AGENTS.md`](AGENTS.md).

Рабочий цикл проекта:

`Issue -> fresh branch -> implementation -> validation/tests -> PR -> exact-head CI -> independent QA -> merge -> post-merge main check`

Initial direct commit был единственным bootstrap-исключением для рождения `main` в изначально пустом репозитории (Issue #1). После него прямые продуктовые изменения `main` запрещены регламентом.

## Структура управления

- `AGENTS.md` — основной контракт работы в репозитории;
- `.agent/rules/` — детальные governance/security правила;
- `QA_INSTRUCTIONS.md` — независимый QA-контракт;
- `.github/ISSUE_TEMPLATE/` — постановка задач;
- `.github/PULL_REQUEST_TEMPLATE.md` — PR gate/checklist;
- `.github/workflows/ci.yml` — автоматический governance CI;
- `scripts/validate_repo.py` — fail-closed проверка структуры, local/generated paths и очевидных секретов.

## Privacy / local artifacts

Сырые локальные материалы не становятся каноническими автоматически.

По умолчанию не отслеживаются:
- `outputs/`;
- `artifacts/`;
- `logs/`;
- browser/IDE profiles;
- auth/session state;
- credentials и secrets.

Материалы из локального `outputs` импортируются только отдельным Issue/PR после inventory, классификации и sanitization.

## Текущее состояние

Issue #1 создаёт governance baseline. Предметная архитектура ConnectorPIA-xray и импорт локальных результатов должны развиваться отдельными Issues после завершения bootstrap.
