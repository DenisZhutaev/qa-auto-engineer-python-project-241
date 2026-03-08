### Статус тестов и линтера Hexlet

[![Actions Status](https://github.com/DenisZhutaev/qa-auto-engineer-python-project-241/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/DenisZhutaev/qa-auto-engineer-python-project-241/actions)

### Сборка Python CI

[![Python CI](https://github.com/DenisZhutaev/qa-auto-engineer-python-project-241/actions/workflows/python-ci.yml/badge.svg)](https://github.com/DenisZhutaev/qa-auto-engineer-python-project-241/actions)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=DenisZhutaev_qa-auto-engineer-python-project-241&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=DenisZhutaev_qa-auto-engineer-python-project-241)
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=DenisZhutaev_qa-auto-engineer-python-project-241&metric=coverage)](https://sonarcloud.io/summary/new_code?id=DenisZhutaev_qa-auto-engineer-python-project-241)

## Gendiff

Сравнивает два конфигурационных файла и показывает разницу.

### Использование

```bash
gendiff first_file second_file
```

### Пример

#### JSON

```bash
gendiff file1.json file2.json
```

Вывод:

```json
{
  - follow: False
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: True
}
```

#### YAML

```bash
gendiff file1.yml file2.yml
```

Вывод:

```yaml
{
  - follow: False
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: True
}
```

#### Формат plain

```bash
gendiff --format plain file1.json file2.json
```

Вывод:

```
Property 'follow' was removed
Property 'proxy' was removed
Property 'timeout' was updated. From 50 to 20
Property 'verbose' was added with value: True
```

#### Формат JSON

```bash
gendiff --format json file1.json file2.json
```

Вывод:

```json
{
  "follow": {
    "status": "removed",
    "value": false
  },
  "host": {
    "status": "unchanged",
    "value": "hexlet.io"
  },
  "proxy": {
    "status": "removed",
    "value": "123.234.53.22"
  },
  "timeout": {
    "status": "changed",
    "old_value": 50,
    "new_value": 20
  },
  "verbose": {
    "status": "added",
    "value": true
  }
}
```

### Как библиотека

```python
from gendiff import generate_diff

# Default (stylish)
diff = generate_diff('file1.json', 'file2.json')
print(diff)

# Plain format
diff = generate_diff('file1.json', 'file2.json', 'plain')
print(diff)

# JSON format
diff = generate_diff('file1.json', 'file2.json', 'json')
print(diff)
```
