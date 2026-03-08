### Hexlet tests and linter status:

[![Actions Status](https://github.com/DenisZhutaev/qa-auto-engineer-python-project-241/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/DenisZhutaev/qa-auto-engineer-python-project-241/actions)

### Python CI

[![Python CI](https://github.com/DenisZhutaev/qa-auto-engineer-python-project-241/actions/workflows/python-ci.yml/badge.svg)](https://github.com/DenisZhutaev/qa-auto-engineer-python-project-241/actions)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=hexlet-boilerplates_python-package&metric=alert_status)](https://sonarcloud.io/dashboard?id=hexlet-boilerplates_python-package)
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=hexlet-boilerplates_python-package&metric=coverage)](https://sonarcloud.io/dashboard?id=hexlet-boilerplates_python-package)

## Gendiff

Compares two configuration files and shows the difference.

### Usage

```bash
gendiff first_file second_file
```

### Example

#### JSON

```bash
gendiff file1.json file2.json
```

Output:

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

Output:

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

#### Plain format

```bash
gendiff --format plain file1.json file2.json
```

Output:

```
Property 'follow' was removed
Property 'proxy' was removed
Property 'timeout' was updated. From 50 to 20
Property 'verbose' was added with value: True
```

#### JSON format

```bash
gendiff --format json file1.json file2.json
```

Output:

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

### As a library

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
