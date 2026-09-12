# Safe Sync & Privacy Gate

Публикация, синхронизация, PR и merge не могут обходить privacy/security checks.

## Приоритет

`PRIVACY > SECURITY > DATA_INTEGRITY > REPRODUCIBILITY > KNOWLEDGE > AUTOMATION`

Любая неопределённость вокруг секрета или auth-state трактуется fail-closed.

## Pipeline

`Scope -> Ownership -> Privacy -> Secrets -> Validation -> PR -> QA -> Merge`

### 1. Scope

Каждый файл классифицируется как один из:
- product/source;
- documentation/spec;
- test/fixture;
- derived artifact;
- generated/runtime;
- secret/private/local-only.

Generated/runtime и secret/private/local-only по умолчанию не публикуются.

### 2. Ownership

Перед добавлением внешних или локальных материалов проверить, имеем ли право хранить их в репозитории и в каком виде.

### 3. Privacy

Особенно чувствительными считаются:
- access/refresh tokens;
- cookies;
- session/browser/IDE state;
- OAuth/device auth state;
- API keys;
- private keys;
- локальные абсолютные пути и user identifiers, если они не нужны продукту;
- дампы сетевых заголовков и запросов с Authorization.

### 4. Secrets

До PR должен выполняться автоматический secret scan. Реальные значения не маскируются после попадания в историю — такой commit считается incident и требует rotation/revocation секрета.

### 5. Local outputs

Каталоги `outputs/`, `artifacts/`, runtime traces и аналогичные generated datasets считаются local-only, пока отдельный Issue не определит:
- зачем они нужны в Git;
- срок жизни;
- размер/формат;
- sanitization;
- canonical vs derived status.

### 6. Validation

Перед PR проверяются как минимум:
- структура обязательных governance-файлов;
- отсутствие очевидных секретов;
- отсутствие случайных generated/runtime файлов;
- применимые тесты проекта.

### 7. Merge

Merge запрещён при failed/unknown privacy, security или validation state, даже если прочие проверки зелёные.
