# Security Rule

## Запрещено коммитить

- реальные токены и API keys;
- cookies и session state;
- `.env` с секретами;
- OAuth/device/browser credentials;
- private keys;
- Authorization headers;
- экспортированные профили браузеров/IDE;
- credential databases;
- production dumps с чувствительными данными.

## Fixtures

Для тестов использовать только synthetic/redacted fixtures. Placeholder должен явно показывать, что значение нерабочее, например `REDACTED_TOKEN` или `example.invalid`.

## Инцидент

Если секрет попал в Git history:
1. остановить дальнейшую публикацию;
2. считать секрет скомпрометированным;
3. revoke/rotate секрет во внешней системе;
4. оформить отдельный security Issue с минимально необходимой информацией, без повторной публикации секрета;
5. очистку истории выполнять только осознанно и отдельно.

Удаление строки из последнего файла само по себе не делает опубликованный секрет безопасным.
