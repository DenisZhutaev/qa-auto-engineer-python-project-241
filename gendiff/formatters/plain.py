# gendiff.formatters.plain module


def _format_value(value):
    if value is True:
        return 'true'
    if value is False:
        return 'false'
    if value is None:
        return 'null'
    return str(value)


def format_plain(diff_tree, parent_key=''):
    lines = []

    for key, value in diff_tree.items():
        full_key = f'{parent_key}.{key}' if parent_key else key

        if isinstance(value, dict) and 'status' in value:
            status = value['status']

            if status == 'removed':
                lines.append(f"Property '{full_key}' was removed")
            elif status == 'added':
                lines.append(
                    f"Property '{full_key}' was added "
                    f"with value: {_format_value(value.get('value'))}"
                )
            elif status == 'changed':
                old_val = _format_value(value.get('old_value'))
                new_val = _format_value(value.get('new_value'))
                lines.append(
                    f"Property '{full_key}' was updated. "
                    f"From {old_val} to {new_val}"
                )
            elif status == 'unchanged':
                pass  # Skip unchanged properties in plain format
        else:
            lines.append(f"Property '{full_key}': {value}")

    return '\n'.join(lines)
