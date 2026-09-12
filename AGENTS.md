# AGENTS.md — ConnectorPIA-xray

Этот файл — каноническая точка входа для AI-агентов, IDE-агентов и автоматизации проекта.

## 1. Перед любой работой

1. Прочитать `README.md`.
2. Прочитать `AGENTS.md` полностью.
3. Прочитать применимые правила из `.agent/rules/`.
4. Проверить открытый Issue, к которому относится работа.
5. Проверить актуальность `main` и работать только из fresh branch.

Если Issue отсутствует — сначала создать Issue. Исключение было только одно: initial commit пустого репозитория в рамках Issue #1.

## 2. Канонический workflow

`Issue -> fresh branch -> implementation -> validation/tests -> PR -> exact-head CI -> independent QA -> merge -> post-merge main check`

### Обязательные условия
- Прямые продуктовые изменения `main` запрещены.
- Branch создаётся от актуального `main`.
- Имена веток: `feat/issue-N-slug`, `fix/issue-N-slug`, `docs/issue-N-slug`, `chore/issue-N-slug`.
- PR обязан содержать `Resolves #N`, `Closes #N` или `Refs #N`.
- Scope PR должен соответствовать Issue. Случайные и несвязанные изменения запрещены.
- Green CI относится только к проверенному HEAD. После изменения HEAD старое QA считается устаревшим.
- Merge допускается после проверки CI, отсутствия blocking review threads и независимого QA/approval.
- После merge проверить состояние `main`.

## 3. Приоритет инвариантов

`PRIVACY > SECURITY > DATA_INTEGRITY > REPRODUCIBILITY > KNOWLEDGE > AUTOMATION > CONVENIENCE`

При конфликте действует более левый приоритет. Неясность вокруг секретов, токенов, cookies, auth-state или приватных данных трактуется fail-closed.

## 4. Локальные материалы и outputs

Локальные каталоги, дампы, трассы, токены, cookies, browser/session state, runtime logs и сырые generated outputs не являются автоматически каноническими данными репозитория.

Перед импортом материалов из локальных `outputs`:
1. провести inventory;
2. классифицировать `source / derived / generated / secret / local-only`;
3. удалить или замаскировать секреты и персональные пути;
4. определить каноническое место хранения;
5. импортировать только через отдельный Issue/PR.

## 5. Секреты и авторизация

Никогда не коммитить:
- access/refresh tokens;
- cookies и session storage;
- OAuth/device/browser auth state;
- API keys и пароли;
- приватные ключи и сертификаты с private material;
- `.env` с реальными значениями;
- дампы заголовков Authorization;
- локальные профили браузера/IDE.

Разрешены только redacted fixtures и документированные placeholder-значения.

## 6. Источники истины

- Governance: `AGENTS.md` + `.agent/rules/`.
- Задачи и решения: GitHub Issues/PR.
- Архитектура: `docs/` после её появления.
- Код и тесты: только содержимое, слитое в `main`.
- Локальный runtime state не является source of truth репозитория.

Не создавать параллельные SSOT без отдельного архитектурного Issue.

## 7. Поведение агента

- Не спрашивать подтверждение для безопасных, обратимых действий внутри утверждённого Issue scope.
- Не расширять scope молча.
- Не выдавать подготовленный prompt/spec/probe за выполненную runtime-операцию.
- Явно различать `observed`, `inferred`, `planned`, `verified`.
- Не скрывать ошибки CI/QA и не обходить gate ради скорости.
- Экономить токены и лог-шум, но не удалять evidence, необходимый для проверки результата.

## 8. Merge

Merge — отдельное действие после gate. Предпочтителен squash merge для обычных Issue-веток, если конкретный Issue не требует сохранения истории коммитов.

Команда/разрешение пользователя `mtd/MTD/мтд`, если она используется в рабочем контексте проекта, означает разрешение выполнить merge после прохождения всех обязательных gates; она не отменяет CI/QA/security checks.
